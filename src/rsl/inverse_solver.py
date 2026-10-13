"""
Module giải nghịch đảo RSL (Inverse RSL Solving) và Đánh giá khả năng giao hàng (Delivery Suitability).
Phụ trách chính: Member 4 (Quality/RSL Lead).
Bao gồm:
- Inverse solver giải t* khi Q_hat(t*) = Q_threshold (8-10% Mass Loss).
- Residual bootstrap uncertainty quantification (Khoảng tin cậy RSL).
- Delivery suitability classification & risk probability P(RSL >= t_required).
"""

import numpy as np
from scipy.interpolate import interp1d
from typing import Tuple, Dict, Any


def solve_rsl_from_curve(
    storage_days_grid: np.ndarray,
    predicted_mass_loss_curve: np.ndarray,
    failure_threshold_pct: float = 10.0,
    max_shelf_life_cap: float = 30.0
) -> float:
    """
    Giải tìm thời điểm t* (ngày) mà hàm suy giảm cắt ngưỡng hư hỏng thương mại:
    Q_hat(t*) = failure_threshold_pct (ví dụ: 10% Mass loss).
    Nếu mẫu đã vượt ngưỡng ngay tại Day 0, trả về 0.0.
    Nếu sau max_shelf_life_cap mà chưa vượt ngưỡng, trả về max_shelf_life_cap.
    """
    # Nếu ngay lúc đến đã hỏng
    if predicted_mass_loss_curve[0] >= failure_threshold_pct:
        return 0.0

    # Nếu trong toàn dải thời gian không chạm ngưỡng
    if predicted_mass_loss_curve[-1] < failure_threshold_pct:
        # Ngoại suy tuyến tính từ 2 điểm cuối
        d_last = storage_days_grid[-1]
        d_prev = storage_days_grid[-2]
        q_last = predicted_mass_loss_curve[-1]
        q_prev = predicted_mass_loss_curve[-2]
        slope = (q_last - q_prev) / max(1e-6, (d_last - d_prev))
        if slope <= 0:
            return float(max_shelf_life_cap)
        extrapolated_t = d_last + (failure_threshold_pct - q_last) / slope
        return float(min(extrapolated_t, max_shelf_life_cap))

    # Tìm đoạn cắt ngưỡng đầu tiên (monotonic hoặc nội suy)
    f_interp = interp1d(predicted_mass_loss_curve, storage_days_grid, kind="linear", bounds_error=False, fill_value="extrapolate")
    t_star = float(f_interp(failure_threshold_pct))
    return float(np.clip(t_star, 0.0, max_shelf_life_cap))


def estimate_rsl_with_bootstrap_uncertainty(
    model,
    exposure_feature_row: dict,
    model_residuals: np.ndarray,
    feature_cols: list,
    failure_threshold_pct: float = 10.0,
    n_bootstrap: int = 500,
    t_grid_max: float = 20.0,
    num_grid_points: int = 200,
    confidence_level: float = 0.95
) -> Dict[str, Any]:
    """
    Ước lượng RSL kèm khoảng tin cậy bất định (Uncertainty Quantification) qua Residual Bootstrap.
    Trả về:
    - rsl_point: Ước lượng điểm (ngày)
    - rsl_ci_lower: Cận dưới khoảng tin cậy
    - rsl_ci_upper: Cận trên khoảng tin cậy
    - bootstrap_distribution: Mảng RSL từ các mẫu bootstrap
    """
    t_grid = np.linspace(0.0, t_grid_max, num_grid_points)

    # Tạo bảng query giả lập dọc theo trục thời gian lưu kho t
    query_df_list = []
    for t in t_grid:
        row = dict(exposure_feature_row)
        row["storage_time_days"] = t
        query_df_list.append(row)

    import pandas as pd
    query_df = pd.DataFrame(query_df_list)[feature_cols]

    # Dự báo đường cong cơ sở
    base_curve = model.predict(query_df)
    rsl_point = solve_rsl_from_curve(t_grid, base_curve, failure_threshold_pct)

    # Bootstrap phân bố thặng dư (Residuals)
    bootstrap_rsls = []
    n_res = len(model_residuals)
    alpha = (1.0 - confidence_level) / 2.0

    for _ in range(n_bootstrap):
        sampled_residuals = np.random.choice(model_residuals, size=len(t_grid), replace=True)
        perturbed_curve = np.maximum(0.0, base_curve + sampled_residuals)
        # Đảm bảo đường cong tăng đơn điệu
        monotonic_curve = np.maximum.accumulate(perturbed_curve)
        boot_t = solve_rsl_from_curve(t_grid, monotonic_curve, failure_threshold_pct)
        bootstrap_rsls.append(boot_t)

    bootstrap_rsls = np.array(bootstrap_rsls)
    ci_lower = float(np.percentile(bootstrap_rsls, 100 * alpha))
    ci_upper = float(np.percentile(bootstrap_rsls, 100 * (1.0 - alpha)))

    return {
        "rsl_point_days": rsl_point,
        "rsl_ci_lower_days": ci_lower,
        "rsl_ci_upper_days": ci_upper,
        "rsl_std_days": float(np.std(bootstrap_rsls)),
        "bootstrap_samples": bootstrap_rsls
    }


def evaluate_delivery_suitability(
    rsl_estimates: Dict[str, Any],
    required_retail_shelf_life_days: float = 4.0
) -> Dict[str, Any]:
    """
    Đánh giá khả năng đáp ứng yêu cầu giao hàng của lô hàng (Delivery Suitability).
    - is_suitable: True nếu RSL ước lượng điểm >= yêu cầu bán lẻ.
    - success_probability: P(RSL >= t_required) tính từ phân phối bootstrap.
    - risk_level: LOW / MEDIUM / HIGH.
    """
    point_rsl = rsl_estimates["rsl_point_days"]
    boot_samples = rsl_estimates["bootstrap_samples"]

    p_success = float(np.mean(boot_samples >= required_retail_shelf_life_days))
    is_suitable = bool(point_rsl >= required_retail_shelf_life_days)

    if p_success >= 0.85:
        risk_level = "LOW_RISK"
    elif p_success >= 0.50:
        risk_level = "MODERATE_RISK"
    else:
        risk_level = "HIGH_RISK_REJECTION"

    return {
        "required_days": required_retail_shelf_life_days,
        "predicted_rsl_days": point_rsl,
        "is_suitable": is_suitable,
        "success_probability": p_success,
        "risk_level": risk_level
    }
