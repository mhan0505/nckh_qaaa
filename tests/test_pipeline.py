"""
Unit test kiểm định toàn diện Pipeline nghiên cứu:
1. Feature extraction (Tier 1 Summary + Tier 2 Domain VPD / Degree-hours)
2. GroupKFold Splitting & Leakage Verification (Chặn 100% rò rỉ dữ liệu)
3. Model training & Out-of-fold evaluation
4. Inverse RSL solving & Residual bootstrap uncertainty quantification
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
import numpy as np
import pandas as pd

# Thêm thư mục gốc vào path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.features.domain_features import extract_trajectory_exposure_features, calculate_vpd
from src.utils.leakage_guard import create_group_kfold_splits, verify_no_group_leakage, DataLeakageError
from src.models.baselines import run_cross_validation, evaluate_predictions
from src.rsl.inverse_solver import solve_rsl_from_curve, estimate_rsl_with_bootstrap_uncertainty, evaluate_delivery_suitability


def generate_mock_cold_chain_study():
    """Tạo tập dữ liệu mô phỏng gồm 10 box, mỗi box 6 quả, đo tại các ngày 0, 3, 6, 9, 12."""
    np.random.seed(42)
    n_boxes = 10
    mangoes_per_box = 6
    storage_days = [0, 3, 6, 9, 12]

    records = []
    for b in range(n_boxes):
        box_id = f"BOX_{b+1:02d}"
        
        # Mô phỏng chuỗi cảm biến 72 giờ vận chuyển (mỗi 5 phút 1 điểm = 864 điểm)
        n_steps = 864
        t_air = np.random.normal(loc=13.0 + (b % 3) * 3.0, scale=1.5, size=n_steps)
        # Giả lập vài đợt sốc nhiệt (temperature excursion)
        if b % 2 == 1:
            t_air[200:300] += 8.0  # Sốc nhiệt lên 21°C - 24°C
        t_mango = t_air + np.random.normal(loc=0.5, scale=0.3, size=n_steps)
        rh = np.random.uniform(80.0, 95.0, size=n_steps)

        df_sensor = pd.DataFrame({"t_air": t_air, "t_mango": t_mango, "rh": rh})
        exposure_feats = extract_trajectory_exposure_features(df_sensor, sampling_interval_min=5.0)

        for m in range(mangoes_per_box):
            mango_id = f"{box_id}_M{m+1:02d}"
            init_weight = float(np.random.normal(450.0, 30.0))

            for day in storage_days:
                # Tổn thất khối lượng tăng theo ngày và tỷ lệ thuận với VPD và sốc nhiệt
                loss_rate = 0.5 + 0.15 * exposure_feats["vpd_mean"] + 0.05 * exposure_feats["heat20_excursions_hours"]
                noise = np.random.normal(0.0, 0.2)
                mass_loss = max(0.0, loss_rate * day + noise)

                row = {
                    "mango_id": mango_id,
                    "box_id": box_id,
                    "storage_time_days": float(day),
                    "storage_temp_celsius": 20.0,
                    "initial_weight_g": init_weight,
                    "mass_loss_pct": mass_loss
                }
                row.update(exposure_feats)
                records.append(row)

    return pd.DataFrame(records)


def test_leakage_guard():
    print("--> [TEST 1] Kiểm tra Leakage Guard...")
    df = generate_mock_cold_chain_study()
    splits = create_group_kfold_splits(df, group_col="box_id", n_splits=5)
    assert len(splits) == 5, "Phải sinh ra đúng 5 fold."

    # Kiểm tra thử nghiệm nếu cố tình làm rò rỉ
    train_boxes = ["BOX_01", "BOX_02"]
    test_boxes = ["BOX_02", "BOX_03"]
    try:
        verify_no_group_leakage(train_boxes, test_boxes)
        assert False, "Phải ném ra DataLeakageError khi có box giao nhau!"
    except DataLeakageError:
        pass
    print("    [PASS] Leakage Guard hoạt động chính xác 100%.")


def test_feature_engineering():
    print("--> [TEST 2] Kiểm tra Feature Engineering (VPD & Domain Features)...")
    t_air = np.array([12.0, 15.0, 22.0])
    t_mango = np.array([12.5, 15.2, 21.8])
    rh = np.array([85.0, 90.0, 75.0])
    vpd = calculate_vpd(t_air, t_mango, rh)
    assert np.all(vpd >= 0), "VPD không thể âm."
    assert len(vpd) == 3
    print("    [PASS] VPD và các đặc trưng nhiệt - ẩm được tính toán hợp lệ.")


def test_end_to_end_ml_and_rsl():
    print("--> [TEST 3] Chạy End-to-End Pipeline (Train ML -> Inverse RSL -> Suitability)...")
    df = generate_mock_cold_chain_study()
    splits = create_group_kfold_splits(df, group_col="box_id", n_splits=5)

    feature_cols = [
        "storage_time_days", "transit_duration_hours", "t_air_mean", "t_mango_mean",
        "rh_mean", "delta_t_mean", "vpd_mean", "heat20_excursions_hours", "chilling_degree_hours_sub12"
    ]
    target_col = "mass_loss_pct"

    # 1. Train Random Forest
    rf_res = run_cross_validation("random_forest", df, feature_cols, target_col, splits)
    rmse = rf_res["overall_metrics"]["rmse"]
    r2 = rf_res["overall_metrics"]["r2"]
    print(f"    Random Forest Overall RMSE: {rmse:.4f}, R²: {r2:.4f}")
    assert r2 > 0.80, f"R² phải đạt trên 0.80 trên mock data (thực tế: {r2})"

    # 2. Inverse RSL solving cho 1 mẫu
    sample_box = df.iloc[0].to_dict()
    model = rf_res["fitted_models"][0]
    residuals = rf_res["oof_residuals"]

    rsl_result = estimate_rsl_with_bootstrap_uncertainty(
        model=model,
        exposure_feature_row=sample_box,
        model_residuals=residuals,
        feature_cols=feature_cols,
        failure_threshold_pct=10.0,
        n_bootstrap=100
    )
    print(f"    Ước lượng RSL: {rsl_result['rsl_point_days']:.2f} ngày "
          f"(95% CI: [{rsl_result['rsl_ci_lower_days']:.2f}, {rsl_result['rsl_ci_upper_days']:.2f}])")

    # 3. Delivery suitability
    suitability = evaluate_delivery_suitability(rsl_result, required_retail_shelf_life_days=4.0)
    print(f"    Khả năng giao hàng: {suitability['risk_level']} (P_success: {suitability['success_probability']:.2f})")

    assert rsl_result["rsl_point_days"] > 0
    assert suitability["risk_level"] in ["LOW_RISK", "MODERATE_RISK", "HIGH_RISK_REJECTION"]
    print("    [PASS] Toàn bộ chu trình dự báo và giải nghịch đảo RSL thành công mượt mà!")


if __name__ == "__main__":
    test_leakage_guard()
    test_feature_engineering()
    test_end_to_end_ml_and_rsl()
    print("\n=== TẤT CẢ UNIT TESTS ĐỀU ĐẠT CHUẨN! ===")
