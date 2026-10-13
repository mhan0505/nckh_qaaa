"""
Module bảo vệ và xác thực không rò rỉ dữ liệu (Leakage Guard).
Phụ trách chính: Member 2 (Data Lead) & Member 3 (ML Lead).
Bảo đảm tính hợp lệ khoa học nghiêm ngặt: Tuyệt đối không để quả xoài cùng Box/Shipment rơi vào cả Train và Test.
"""

from typing import List, Tuple, Any, Set
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold


class DataLeakageError(Exception):
    """Lỗi nghiêm trọng: Phát hiện rò rỉ dữ liệu giữa tập Train và Test/Validation."""
    pass


def verify_no_group_leakage(train_groups: Any, test_groups: Any) -> bool:
    """
    Kiểm tra tính rời rạc tuyệt đối giữa các nhóm trong tập Train và Test.
    Ném ngoại lệ DataLeakageError nếu có bất kỳ nhóm nào giao nhau.
    """
    set_train = set(train_groups)
    set_test = set(test_groups)

    overlap = set_train.intersection(set_test)
    if len(overlap) > 0:
        raise DataLeakageError(
            f"NGHIÊM TRỌNG: Phát hiện rò rỉ dữ liệu (Data Leakage)! "
            f"Có {len(overlap)} box/chuyến hàng xuất hiện ở cả Train và Test: {list(overlap)[:5]}"
        )
    return True


def create_group_kfold_splits(
    df: pd.DataFrame,
    group_col: str = "box_id",
    n_splits: int = 5,
    seed: int = 42
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Tạo các fold phân chia theo GroupKFold.
    Bảo đảm:
    1. Mỗi Box chỉ nằm trong đúng 1 fold test.
    2. Toàn bộ các fold đều được kiểm tra verify_no_group_leakage trước khi trả về.
    """
    if group_col not in df.columns:
        raise ValueError(f"Cột định danh nhóm '{group_col}' không tồn tại trong DataFrame.")

    unique_groups = df[group_col].unique()
    if len(unique_groups) < n_splits:
        raise ValueError(
            f"Số lượng nhóm độc lập ({len(unique_groups)}) nhỏ hơn số fold yêu cầu ({n_splits}). "
            f"Vui lòng giảm n_splits xuống tối đa {len(unique_groups)}."
        )

    gkf = GroupKFold(n_splits=n_splits)
    groups = df[group_col].values
    splits = []

    for fold, (train_idx, val_idx) in enumerate(gkf.split(df, groups=groups)):
        train_boxes = df.iloc[train_idx][group_col].values
        val_boxes = df.iloc[val_idx][group_col].values

        # Kiểm định chống rò rỉ
        verify_no_group_leakage(train_boxes, val_boxes)
        splits.append((train_idx, val_idx))

    return splits
