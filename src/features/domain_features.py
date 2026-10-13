"""
Module trích xuất đặc trưng phơi nhiễm chuỗi lạnh (Exposure Feature Engineering).
Phụ trách chính: Member 2 (Data Lead) & Member 3 (ML Lead).
Bao gồm:
- Tier 1: Summary Statistics (Mean, Min, Max, Std).
- Tier 2: Domain/Physiology-Informed Features (VPD, Degree-Hours, Excursions, Thermal gradient).
"""

import numpy as np
import pandas as pd


def calculate_saturated_vapor_pressure(temp_celsius: np.ndarray) -> np.ndarray:
    """
    Tính áp suất hơi bão hòa e_s (kPa) theo công thức Tetens:
    e_s(T) = 0.61078 * exp((17.27 * T) / (T + 237.3))
    """
    return 0.61078 * np.exp((17.27 * temp_celsius) / (temp_celsius + 237.3))


def calculate_actual_vapor_pressure(temp_celsius: np.ndarray, rh_pct: np.ndarray) -> np.ndarray:
    """
    Tính áp suất hơi thực tế e_a (kPa):
    e_a(T, RH) = e_s(T) * (RH / 100)
    """
    e_s = calculate_saturated_vapor_pressure(temp_celsius)
    return e_s * (np.clip(rh_pct, 0.0, 100.0) / 100.0)


def calculate_vpd(t_air: np.ndarray, t_mango: np.ndarray, rh_pct: np.ndarray) -> np.ndarray:
    """
    Tính thâm hụt áp suất hơi nước (Vapor Pressure Deficit - VPD) (kPa):
    VPD = e_s(T_mango) - e_a(T_air, RH)
    Chỉ số vật lý cốt lõi dẫn động quá trình thoát hơi nước và mất khối lượng của quả.
    """
    e_s_mango = calculate_saturated_vapor_pressure(t_mango)
    e_a_air = calculate_actual_vapor_pressure(t_air, rh_pct)
    vpd = e_s_mango - e_a_air
    return np.maximum(0.0, vpd)


def calculate_degree_hours(temp_series: np.ndarray, dt_hours: float, threshold: float, mode: str = "above") -> float:
    """
    Tính tích phân độ-giờ (Degree-Hours):
    - mode="above": Tích lũy ứng suất nhiệt (Heat abuse): sum(max(0, T - threshold)) * dt
    - mode="below": Tích lũy tổn thương lạnh (Chilling injury): sum(max(0, threshold - T)) * dt
    """
    if mode == "above":
        diff = np.maximum(0.0, temp_series - threshold)
    elif mode == "below":
        diff = np.maximum(0.0, threshold - temp_series)
    else:
        raise ValueError(f"Unknown mode: {mode}")
    return float(np.sum(diff) * dt_hours)


def calculate_excursions(temp_series: np.ndarray, threshold: float, dt_hours: float, mode: str = "above"):
    """
    Tính số lần và thời lượng phơi nhiễm vượt ngưỡng:
    Trả về (num_excursions, total_duration_hours, max_excursion_peak)
    """
    if mode == "above":
        mask = temp_series > threshold
        excess = temp_series - threshold
    else:
        mask = temp_series < threshold
        excess = threshold - temp_series

    if not np.any(mask):
        return 0, 0.0, 0.0

    # Đếm số đợt excursion liên tục
    diffs = np.diff(mask.astype(int))
    starts = np.sum(diffs == 1) + (1 if mask[0] else 0)
    total_hours = float(np.sum(mask) * dt_hours)
    max_peak = float(np.max(excess[mask]))

    return int(starts), total_hours, max_peak


def extract_trajectory_exposure_features(df_box_sensor: pd.DataFrame, sampling_interval_min: float = 5.0) -> dict:
    """
    Trích xuất toàn bộ vector đặc trưng Tier 1 & Tier 2 từ chuỗi cảm biến của 1 thùng (Box trajectory).
    Input DataFrame bắt buộc chứa các cột:
    ['t_air', 't_mango', 'rh'] (hoặc ['temp_air', 'temp_mango', 'relative_humidity'])
    """
    dt_hours = sampling_interval_min / 60.0

    # Đồng bộ tên cột
    t_air = df_box_sensor.get("t_air", df_box_sensor.get("temp_air", None)).to_numpy(dtype=float)
    t_mango = df_box_sensor.get("t_mango", df_box_sensor.get("temp_mango", t_air)).to_numpy(dtype=float)
    rh = df_box_sensor.get("rh", df_box_sensor.get("relative_humidity", None)).to_numpy(dtype=float)

    total_transit_hours = len(t_air) * dt_hours

    # 1. TIER 1: Summary Statistics
    features = {
        "transit_duration_hours": total_transit_hours,
        # T_air stats
        "t_air_mean": float(np.mean(t_air)),
        "t_air_min": float(np.min(t_air)),
        "t_air_max": float(np.max(t_air)),
        "t_air_std": float(np.std(t_air)),
        # T_mango stats
        "t_mango_mean": float(np.mean(t_mango)),
        "t_mango_min": float(np.min(t_mango)),
        "t_mango_max": float(np.max(t_mango)),
        "t_mango_std": float(np.std(t_mango)),
        # RH stats
        "rh_mean": float(np.mean(rh)),
        "rh_min": float(np.min(rh)),
        "rh_max": float(np.max(rh)),
        "rh_std": float(np.std(rh)),
    }

    # 2. TIER 2: Domain & Physiology-Informed Features
    # Thermal gradient (T_mango - T_air)
    delta_t = t_mango - t_air
    features.update({
        "delta_t_mean": float(np.mean(delta_t)),
        "delta_t_max": float(np.max(delta_t)),
        "delta_t_min": float(np.min(delta_t)),
        "delta_t_std": float(np.std(delta_t)),
    })

    # Vapor Pressure Deficit (VPD)
    vpd = calculate_vpd(t_air, t_mango, rh)
    features.update({
        "vpd_mean": float(np.mean(vpd)),
        "vpd_max": float(np.max(vpd)),
        "vpd_min": float(np.min(vpd)),
        "vpd_std": float(np.std(vpd)),
        "vpd_integral_kpa_hours": float(np.sum(vpd) * dt_hours),
    })

    # Degree-Hours: Chilling (<12°C) vs Heat (>20°C, >25°C)
    features["chilling_degree_hours_sub12"] = calculate_degree_hours(t_mango, dt_hours, threshold=12.0, mode="below")
    features["heat_degree_hours_above20"] = calculate_degree_hours(t_mango, dt_hours, threshold=20.0, mode="above")
    features["heat_degree_hours_above25"] = calculate_degree_hours(t_mango, dt_hours, threshold=25.0, mode="above")

    # Excursions count & duration
    chill_cnt, chill_dur, chill_peak = calculate_excursions(t_mango, threshold=12.0, dt_hours=dt_hours, mode="below")
    features.update({
        "chilling_excursions_count": chill_cnt,
        "chilling_excursions_hours": chill_dur,
        "chilling_max_peak_deficit": chill_peak,
    })

    heat_cnt, heat_dur, heat_peak = calculate_excursions(t_mango, threshold=20.0, dt_hours=dt_hours, mode="above")
    features.update({
        "heat20_excursions_count": heat_cnt,
        "heat20_excursions_hours": heat_dur,
        "heat20_max_peak_excess": heat_peak,
    })

    return features
