"""
Module huấn luyện và đánh giá các mô hình học máy (ML Benchmark Suite).
Phụ trách chính: Member 3 (ML Lead).
Bao gồm:
- Linear Baselines: Ridge & ElasticNet.
- Tabular SOTA Trees: Random Forest, LightGBM, XGBoost.
- Đánh giá chéo theo GroupKFold và tổng hợp metrics: RMSE, MAE, R².
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from sklearn.linear_model import Ridge, ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import xgboost as xgb
import lightgbm as lgb


def get_model_instance(model_name: str, **kwargs):
    """Factory hàm khởi tạo mô hình ML theo cấu hình."""
    name = model_name.lower()
    if name == "ridge":
        return Ridge(alpha=kwargs.get("alpha", 1.0))
    elif name == "elasticnet":
        return ElasticNet(alpha=kwargs.get("alpha", 0.1), l1_ratio=kwargs.get("l1_ratio", 0.5), random_state=42)
    elif name == "random_forest":
        return RandomForestRegressor(
            n_estimators=kwargs.get("n_estimators", 100),
            max_depth=kwargs.get("max_depth", 8),
            random_state=kwargs.get("random_state", 42),
            n_jobs=-1
        )
    elif name == "xgboost":
        return xgb.XGBRegressor(
            n_estimators=kwargs.get("n_estimators", 150),
            learning_rate=kwargs.get("learning_rate", 0.05),
            max_depth=kwargs.get("max_depth", 6),
            subsample=kwargs.get("subsample", 0.8),
            random_state=kwargs.get("random_state", 42),
            verbosity=0
        )
    elif name == "lightgbm":
        return lgb.LGBMRegressor(
            n_estimators=kwargs.get("n_estimators", 150),
            learning_rate=kwargs.get("learning_rate", 0.05),
            max_depth=kwargs.get("max_depth", 6),
            random_state=kwargs.get("random_state", 42),
            verbosity=-1
        )
    else:
        raise ValueError(f"Không hỗ trợ mô hình: {model_name}")


def evaluate_predictions(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Tính các chỉ số đo lường hiệu năng dự báo."""
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    r2 = float(r2_score(y_true, y_pred))
    return {"rmse": rmse, "mae": mae, "r2": r2}


def run_cross_validation(
    model_name: str,
    df: pd.DataFrame,
    feature_cols: List[str],
    target_col: str,
    splits: List[Tuple[np.ndarray, np.ndarray]],
    model_params: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Chạy GroupKFold Cross-Validation cho 1 mô hình.
    Trả về:
    - mean_metrics: Trung bình RMSE, MAE, R² trên các fold
    - std_metrics: Độ lệch chuẩn
    - oof_predictions: Mảng out-of-fold predictions
    - fitted_models: Danh sách model sau khi fit trên từng fold
    - oof_residuals: Thặng dư sai số để Member 4 dùng cho Bootstrap
    """
    if model_params is None:
        model_params = {}

    oof_preds = np.zeros(len(df))
    fold_metrics = []
    fitted_models = []

    for fold_idx, (train_idx, val_idx) in enumerate(splits):
        X_train = df.iloc[train_idx][feature_cols]
        y_train = df.iloc[train_idx][target_col].values

        X_val = df.iloc[val_idx][feature_cols]
        y_val = df.iloc[val_idx][target_col].values

        model = get_model_instance(model_name, **model_params)
        model.fit(X_train, y_train)

        val_preds = model.predict(X_val)
        oof_preds[val_idx] = val_preds

        metrics = evaluate_predictions(y_val, val_preds)
        fold_metrics.append(metrics)
        fitted_models.append(model)

    y_all = df[target_col].values
    overall_metrics = evaluate_predictions(y_all, oof_preds)
    oof_residuals = y_all - oof_preds

    return {
        "model_name": model_name,
        "overall_metrics": overall_metrics,
        "fold_metrics": fold_metrics,
        "oof_predictions": oof_preds,
        "oof_residuals": oof_residuals,
        "fitted_models": fitted_models
    }
