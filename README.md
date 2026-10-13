# Dynamic Cold-Chain Exposure Representation & Remaining Shelf Life (RSL) Prediction

Đề tài Nghiên cứu Khoa học (NCKH) về mô hình hóa mức độ phơi nhiễm chuỗi lạnh và dự đoán thời gian sử dụng còn lại của xoài xuất khẩu đường dài.

---

## 1. Cấu trúc thư mục (Repository Layout)

```text
d:\nckh_qaaa\
├── configs/
│   └── experiment_config.yaml         # Cấu hình siêu tham số, seed, ngưỡng hư hỏng
├── data/
│   ├── raw/                           # Dữ liệu gốc cảm biến và đo chất lượng xoài
│   ├── processed/                     # Dữ liệu đã làm sạch và reconstruct trajectory
│   └── features/                      # Bảng đặc trưng Tier 1, Tier 2, Tier 3
├── src/
│   ├── data/                          # (M2) Cleaner & Trajectory Builder
│   ├── features/                      # (M2 + M3) Domain features (VPD, Degree-Hours, Excursions)
│   ├── models/                        # (M3) ML Benchmarks (Ridge, RF, XGBoost) & CV Trainer
│   ├── rsl/                           # (M4) Inverse RSL Solver, Uncertainty & Delivery Suitability
│   └── utils/                         # (All) Leakage Guard & Metrics
├── experiments/
│   ├── run_benchmark.py               # Master runner so sánh đa tầng biểu diễn
│   ├── benchmark_results.csv          # Kết quả số liệu thực nghiệm
│   └── table_results.tex              # Bảng mã nguồn LaTeX sẵn sàng nộp paper
└── tests/
    └── test_pipeline.py               # Unit test kiểm định toàn diện hệ thống
```

---

## 2. Phân công 4 thành viên (4-Member Team Ownership)

| Thành viên | Vai trò chính | Nhiệm vụ chính trong Repo |
| :--- | :--- | :--- |
| **Member 1** | **Research Lead** | Problem Statement, Related Work, Research Gap, viết Paper & làm Slide |
| **Member 2** | **Data Lead** | Data ingestion, làm sạch chuỗi thời gian, `src/features/domain_features.py` (VPD, Excursion) |
| **Member 3** | **ML Lead** | `src/models/baselines.py`, GroupKFold CV loop, huấn luyện mô hình và bóc tách SHAP values |
| **Member 4** | **Quality/RSL Lead**| `src/rsl/inverse_solver.py`, giải nghiệm $t^*$, Bootstrap CI, kiểm định ý nghĩa thống kê |

---

## 3. Cách chạy và Kiểm thử (Quick Start)

### Chạy Unit Test kiểm tra tính toàn vẹn và chống rò rỉ dữ liệu (Leakage Guard)
```bash
python tests/test_pipeline.py
```

### Chạy Thực nghiệm So sánh Đa tầng Biểu diễn (Benchmark)
```bash
python experiments/run_benchmark.py
```
Sau khi chạy xong, kết quả số liệu sẽ tự động được xuất ra `experiments/benchmark_results.csv` và `experiments/table_results.tex`.
