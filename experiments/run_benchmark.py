"""
Master Benchmark Experiment Runner:
So sánh đa tầng biểu diễn:
- Tier 1: Baseline Summary Statistics
- Tier 2: Domain/Physiology-Informed Features (VPD, Degree-Hours, Thermal Gradient)
- Tier 1 + 2: Combined Features
Qua các mô hình: Ridge, Random Forest, XGBoost.
Kết quả được xuất ra bảng Markdown và định dạng bảng LaTeX cho Member 1 dán trực tiếp vào Paper.
"""

import sys
import os
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import yaml
import numpy as np
import pandas as pd
from src.utils.leakage_guard import create_group_kfold_splits
from src.models.baselines import run_cross_validation
from tests.test_pipeline import generate_mock_cold_chain_study


def main():
    print("=" * 70)
    print("CHẠY THỰC NGHIỆM ĐỐI SÁNH ĐA TẦNG BIỂU DIỄN & MÔ HÌNH HỌC MÁY")
    print("=" * 70)

    # Đọc cấu hình
    config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "experiment_config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Lấy dữ liệu (mô phỏng hoặc thực tế từ data/processed)
    data_file = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "mango_analysis_ready.parquet")
    if os.path.exists(data_file):
        print(f"Đọc dữ liệu thực tế từ: {data_file}")
        df = pd.read_parquet(data_file)
    else:
        print("Chưa có data thực tế trong data/processed -> Đang sinh mock study để benchmark...")
        df = generate_mock_cold_chain_study()

    target_col = cfg["targets"]["primary"]
    splits = create_group_kfold_splits(df, group_col=cfg["data"]["group_column"], n_splits=cfg["data"]["n_splits"])

    # Định nghĩa các nhóm đặc trưng
    tier1_features = [
        "storage_time_days", "transit_duration_hours",
        "t_air_mean", "t_air_min", "t_air_max", "t_air_std",
        "t_mango_mean", "t_mango_min", "t_mango_max", "t_mango_std",
        "rh_mean", "rh_min", "rh_max", "rh_std"
    ]

    tier2_features = [
        "storage_time_days", "transit_duration_hours",
        "delta_t_mean", "delta_t_max", "delta_t_std",
        "vpd_mean", "vpd_max", "vpd_integral_kpa_hours",
        "chilling_degree_hours_sub12", "heat20_excursions_hours", "chilling_excursions_hours"
    ]

    tier_combined = list(set(tier1_features + tier2_features))

    representations = {
        "Tier 1 (Summary Stats)": tier1_features,
        "Tier 2 (Domain/Physiology)": tier2_features,
        "Tier 1 + 2 (Combined)": tier_combined
    }

    models_to_test = ["ridge", "random_forest", "xgboost"]
    results_list = []

    for rep_name, feats in representations.items():
        print(f"\n[BENCHMARK] Đang đánh giá Biểu diễn: {rep_name} ({len(feats)} features)...")
        for m_name in models_to_test:
            res = run_cross_validation(m_name, df, feats, target_col, splits)
            m_metrics = res["overall_metrics"]
            results_list.append({
                "Representation": rep_name,
                "Model": m_name.upper(),
                "RMSE": m_metrics["rmse"],
                "MAE": m_metrics["mae"],
                "R2": m_metrics["r2"]
            })
            print(f"  - Model {m_name.upper():<14} | RMSE: {m_metrics['rmse']:.4f} | MAE: {m_metrics['mae']:.4f} | R²: {m_metrics['r2']:.4f}")

    df_res = pd.DataFrame(results_list)

    # Xuất ra thư mục experiments
    out_dir = os.path.dirname(__file__)
    csv_out = os.path.join(out_dir, "benchmark_results.csv")
    df_res.to_csv(csv_out, index=False)
    print(f"\n Đã lưu kết quả chi tiết ra: {csv_out}")

    # Tạo bảng LaTeX cho Paper của Member 1
    latex_table = df_res.to_latex(index=False, float_format="%.4f")
    latex_out = os.path.join(out_dir, "table_results.tex")
    with open(latex_out, "w", encoding="utf-8") as f:
        f.write(latex_table)
    print(f" Đã lưu mã nguồn bảng LaTeX ra: {latex_out}")


if __name__ == "__main__":
    main()
