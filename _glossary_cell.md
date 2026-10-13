---
# 📖 TỪ ĐIỂN THUẬT NGỮ (GLOSSARY) — Dành cho người mới explore data

> Đọc mục này **trước** khi chạy các cell bên dưới. Mỗi thuật ngữ được giải thích theo 3 lớp:
> **(1) Nghĩa thông thường → (2) Nghĩa trong dataset cụ thể này → (3) Ví dụ số liệu thật.**

---

## A. Thuật ngữ về THIẾT BỊ & ĐO LƯỜNG

### 1. iButton (DS1922L / DS1923)
- **Nghĩa chung**: một "nút" ghi dữ liệu (data logger) hình đồng xu nhỏ của hãng Dallas/Maxim, tự ghi nhiệt độ vào bộ nhớ trong theo chu kỳ, không cần dây.
- **Trong dataset**: đây chính là các **sensor** được thả *vào trong thùng* cùng xoài. Có 62 cái cho 31 thùng.
  - `DS1922L` = bản chỉ đo **nhiệt độ** → file tên kết thúc bằng `_Temp`.
  - `DS1923` = bản đo **nhiệt độ + độ ẩm** → file tên kết thúc bằng `_Temp_Hum`.
- **Điểm mấu chốt khi explore**: mỗi file log = **một iButton tại một vị trí**, không phải một "cảm biến" trừu tượng.

### 2. Data logger / Sensor_ID
- **Sensor_ID**: mã định danh duy nhất của từng thiết bị đo (thường nằm ở dòng header của file iButton gốc). Khi merge nhiều chặng (`00_All_Recording...`), Sensor_ID cho biết các file Step rời rạc có phải **cùng một con cảm biến** hay không.

### 3. Sampling step (bước nhảy thời gian / chu kỳ lấy mẫu)
- Chuỗi thời gian cách đều nhau bao lâu thì ghi 1 điểm. Dataset này = **5 phút** (README xác nhận, notebook kiểm chứng lại trên cả 342 file).
- Nghĩa là 1 giờ có 12 dòng dữ liệu; 1 ngày = 288 dòng. Dùng để tính kỳ vọng số dòng và phát hiện gap.

### 4. Resolution (độ phân giải) vs Uncertainty (độ bất định ±)
- **Resolution 0.5°C**: giá trị nhỏ nhất thiết bị *phân biệt được* → số liệu nhiệt độ sẽ **nhảy bậc 0.5** (31.5, 32.0... chứ không bao giờ ra 31.7). Đừng nhầm bước nhảy 0.5°C này với "gap" hay "bất thường".
- **Uncertainty ±0.6°C (k=2)**: khoảng tin cậy ~95% quanh giá trị đọc. Nghĩa vật lý: nếu log ghi `31.6`, nhiệt độ *thực* nằm đâu đó trong `[31.0 ; 32.2]`.
  - Hệ quả khi explore: chênh lệch giữa 2 cảm biến < 0.6–1.2°C **chưa chắc là khác biệt thật** — phải so với độ bất định trước khi kết luận.
- **k = 2**: hệ số mở rộng (coverage factor) trong đo lường học, k=2 ≈ mức tin cậy 95%.

### 5. Tiếp xúc (contact) vs Không khí (air) vs Khoang ngoài
- `T_mangoes`: iButton **áp/bỏ trong quả** → đo khối thịt quả, phản ánh nhiệt tâm quả, trễ hơn không khí.
- `T_Air`: iButton đo **không khí lồng trong thùng carton**.
- Khoang ngoài: nhiệt độ **bên ngoài thùng** (kho lạnh INRAE 16°C/21°C, sàn bay...) — môi trường lớn.

---

## B. Thuật ngữ về CHUỖI LẠNH (COLD CHAIN)

### 6. Cold chain (chuỗi lạnh)
Toàn bộ hành trình giữ lạnh từ vườn → người ăn. Mỗi "khâu" là một **Step** (0→10): Packing House → Tiền lạnh → Xe → Sân bay đi → Bay → Sân bay đến → Lưu kho...
Mục tiêu đề tài: tìm khâu nào để nhiệt độ "trượt" khỏi dải an toàn (>~8–10°C gây hỏng/qu chín nhanh).

### 7. ULD (Unit Load Device)
- Container/kiện chuẩn dùng chất hàng lên máy bay thân rộng. README: **1 ULD chứa 148 thùng carton**, trong đó **31 thùng được gắn cảm biến** đặt ở các vị trí khác nhau.
- Vì vậy Box_ID `X_Y_Z` mô tả **vị trí hình học trong ULD** (xem mục C).

### 8. Pre-cooling (tiền lạnh, Step 1 – Cold Storage)
Làm lạnh nhanh ngay sau thu hoạch để "rút" nhiệt đồng ruộng (field heat) khỏi quả trước khi xếp lên máy bay. Step dài nhất (~20h) trong timeline.

### 9. Chilling injury (CI – tổn thương lạnh)
Hỏng do bảo quản quá lạnh (<~5–8°C với cây nhiệt đới như xoài): rám vỏ, chín ép, vị lạ. Là lý do thí nghiệm chọn 2 mức lưu kho **16°C vs 21°C** (an toàn, gần ngưỡng CI) để đối chiếu tốc độ suy giảm phẩm chất.

---

## C. Thuật ngữ về CẤU TRÚC THỰC THỂ

### 10. Box_ID dạng `X_Y_Z` (ví dụ `1_1_1`, `3_3_12`)
Không phải "tầng/vị trí" tùy tiện — **đây là tọa độ pallet trong ULD** (được cộng sự Pháp xác nhận trong README/script):
```
X = hàng dọc (row)      : 1 … 4   (1 = sát cửa/lối đi ←→ 4 = sâu trong ULD)
Y = hàng ngang (column) : 1 … 4   (trái ↔ phải)
Z = cột đứng (stack)    : 1 … 12  (1 = đáy ←→ 12 = đỉnh)
```
- 4×4×12 = 192 ô khả dĩ, thực tế 148 thùng, 31 thùng có cảm biến.
- **Ý nghĩa khi explore**: X,Y,Z quyết định thùng chịu gió lạnh/gió nóng thế nào → vì sao README nói có "10 box đỉnh, 9 box giữa chiều cao, 5 box đáy..." (chọn theo vị trí cực đoan để bắt gradient nhiệt).
- ⚠️ Đừng nhầm `X_Y_Z` trong file sensor (vị trí ULD) với số `1_/2_/3_/4_` đầu file quality (**configuration** — xem mục E).

### 11. Mango_ID dạng `BOX_NAME` ví dụ `1_1_1/1-1A`
Chuỗi ghép trong file màu/khối lượng, tách được thành 3 phần:
```
1_1_1   /   1     -   1A
 │        │         └─ vị trí đo trên quả (1..6) + mã lô ảnh
 │        └─ quả thứ # trong thùng (1..14)
 └─ Box_ID (thùng)
```
File weight dùng `M_1_1_1/7` = khối lượng **quả số 7 trong thùng (1,1,1)**. Mỗi thùng 14 quả, chia 2 nhóm 7 bởi một vách ngăn (partition).

### 12. Entity hierarchy (phân cấp thực thể)
Sơ đồ "trong-này-chứa-trong-kia": Shipment → Pallet/ULD → Box → Mango → Sensor. Mọi bảng khi explore nên giữ đủ khóa ngoại này (dạng `box`, `mango`) để group-by/pivot được mà không gộp nhầm.

---

## D. Thuật ngữ về PHẨM CHẤT XOÀI (QUALITY ATTRIBUTES)

### 13. Khối lượng M (Mass) — đơn vị gam
Xoài mất nước → hao hụt khối lượng (weight loss). So sánh M_D15/M_D0 (% thất thoát) là chỉ số thương mại quan trọng. Cân KERN ±0.008g — rất nhỏ so với quả ~350g, tức nhiễu cân bỏ qua được.

### 14. Màu CIE L\*a\*b\* (spectrophotometer CM-700d)
Không gian màu chuẩn quốc tế, 3 trục độc lập:
| Trục | Nghĩa | Xoài chín thì... |
|---|---|---|
| **L\*** | Độ sáng, 0 (đen) → 100 (trắng) | thay đổi nhẹ |
| **a\*** | **−a = xanh lá**, **+a = đỏ/đỏ cam** | tăng (lá → sắc đỏ/cam) |
| **b\*** | **−b = xanh dương**, **+b = vàng** | **tăng mạnh** (xoài chuyển vàng) |
- Ví dụ thật (file color): `1_1_1/1-1A`: b\* = 34.09 (D0) → 51.55 (D9) → 46.85 (D15): quả vàng dần rồi hơi chững — tín hiệu chín.
- Đo **6 vị trí/quả** (các后缀 `-1A ... -6F`), trung bình 3 lần đo liên tiếp.
- Tổng hợp thành chỉ số vàng hóa thường dùng: `Chromaticity = √(a*² + b*²)` hoặc `hue angle = atan2(b*, a*)`.

### 15. pH
Độ acid (thang log, 0–14,越低 càng chua). Xoài chín: acid hữu cơ giảm → **pH tăng nhẹ** (≈4.0 → 4.5+). Máy Starter 300 ±0.03.

### 16. TSS / °Brix (Total Soluble Solids)
Tổng chất rắn hòa tan (chủ yếu đường) — khúc xạ kế PAL-BrixAcid1 ±0.4°Bx. Xoài chín: tinh bột → đường → **TSS tăng** (≈11 → 15°Bx). Kết hợp pH → tỷ lệ maturité `TSS/pH` càng cao càng ngọt/chín.

### 17. D0, D3, D6, D9, D12, D15 ("ngày")
Ngày lấy mẫu **sau khi đến phòng lab** (D0 = 18/04/2023, D15 = 05/05/2023), đo định kỳ 3 ngày/lần trong 15 ngày lưu kho. Đây là chuỗi thời gian **rời, thưa** (6 mốc) — khác hẳn chuỗi sensor dày 5 phút. Trong file color, cột `L_D3, a_D3, b_D3...` = giá trị tại từng ngày.

---

## E. Thuật ngữ về TỔ CHỨC FILE & THÍ NGHIỆM

### 18. `src` vs `res` (source vs result)
- `NN_src_subset_dataset_*` = **dữ liệu thô** (raw values, txt từng điểm đo).
- `NN_res_subset_dataset_*` = **dữ liệu đã xử lý** (min/max/trung bình/std + đồ thị) do script R sinh ra.
- Explore nên luôn bắt đầu từ `src`; `res` dùng để đối chiếu kết quả tính toán của mình có khớp nhóm nghiên cứu gốc không.

### 19. Configuration 1_ / 2_ / 3_ / 4_ (thiết kế thí nghiệm)
4 cách *chọn mẫu* khi đo phẩm chất (khác bản chất, đừng trộn khi phân tích!):
| Prefix | Cách chọn | Nhiệt độ lưu kho |
|---|---|---|
| `1_` | thùng ở **vị trí cực đoan** trong ULD (đỉnh/đáy/góc) | 21°C |
| `2_` | thùng **ngẫu nhiên** ở vị trí không cực đoan | 21°C |
| `3_` | **quả ngẫu nhiên** bất kỳ, không quan tâm vị trí thùng | 21°C |
| `4_` | quả ngẫu nhiên bất kỳ | 16°C |
→ Chỉ `4_` là nhánh 16°C; `1_,2_,3_` đều 21°C. Muốn so sánh 2 nhiệt độ: dùng `3_` vs `4_` (cùng kiểu random) để công bằng.

### 20. `SR` (folder 11/12) = Storage Room
3 file log **toàn trình** của 3 iButton đặt **trong kho lạnh INRAE** (không gắn thùng) — đại diện "khoang ngoài", 2 chế độ 16°C & 21°C.

### 21. Metadata
"Dữ liệu về dữ liệu": tên file encode Step+vị trí, README encode thiết bị/sai số, script R encode quy trình. Notebook Stage 1 chủ yếu là **giải metadata thành cột dataframe**.

### 22. Timezone / UTC / Local time
Timestamp trong file là **giờ địa phương nơi đặt cảm biến** (Việt Nam/Thái Lan: Asia/Ho_Chi_Minh ~ ICT; Pháp: Europe/Paris CET/CEST) nhưng **không ghi chú thích timezone trong file** → cạm bẫy số 1 khi nối các chặng. Chuẩn xử lý: localize đúng múi giờ từng chặng → convert all to UTC → mới được tính gap/duration. (Notebook cell 2.2 làm việc này.)

### 23. Gap / Duplicate / Backward jump
- **Gap**: khoảng trống > 1 bước mẫu (ở đây > 10 phút = bất thường; thường do rút/iButton nghỉ).
- **Duplicate**: 2 dòng cùng timestamp (lỗi đọc/xuất file).
- **Backward jump**: timestamp lùi (đổi đồng hồ, đổi TZ, hoặc gộp file sai).
Ba loại này là "smell test" đầu tiên của mọi chuỗi thời gian.

### 24. Tương quan trễ (lagged cross-correlation)
Nhiệt tâm quả không phản ứng tức thì với T_air vì khối quả có **nhiệt dung lớn** → đường cong T_mangoes là T_Air bị "làm trơn + trễ". Phân tích tương quan theo lag (5/10/15/30 phút) tìm lag mà hệ số tương quan cực đại ⇒ thời hằng nhiệt của quả (thermal time constant, τ). Đây là cơ sở để dự đoán nhiệt quả khi chỉ đo được không khí.

### 25. Symlink (liên kết mềm)
"Shortcut" tới file/thư mục gốc — cấu trúc chuẩn hóa `data/raw/sensor/`, `data/raw/quality/` tạo bằng symlink để **không nhân bản dữ liệu**; khi đếm file nhớ lọc trùng (`resolve()`), nếu không số liệu sẽ gấp đôi.

### 26. Regex (biểu thức chính quy)
Ngôn ngữ mô tả khuôn mẫu chuỗi, dùng để "bẻ khóa" tên file: ví dụ `^(\d+)_(\w+)_([1-4]_[1-4]_\d{1,2})_Temp(_Hum)?\.txt$` tách đồng thời Step, StepName, Box_ID, loại kênh của 342 file cùng lúc.

---

## F. SỔ TAY EXPLOR nhanh (thứ tự nên đi)

1. Mở `data/raw/0_README.txt` — mọi câu trả lời nghiệp vụ nằm đây.
2. Cell 1.1.b: chạy regex → thấy ngay 100% tên file decode được.
3. Vẽ 1 file sensor (`0_Packing_House_1_1_1_Temp_Hum.txt`): 3 đường T_mangoes/T_Air/RH_Air, để ý bậc nhảy 0.5°C.
4. Nối 11 chặng của 1 box → timeline đầy đủ (cell 2.1) — cẩn thận TZ (cell 2.2).
5. Mở file quality: pivot từ wide (`L_D0...b_D15`) sang long (`Box, Mango, Day, L, a, b`) rồi mới plot trend theo ngày.
6. Đối chiếu `res_*` (đã xử lý) với số mình tính được — khớp = hiểu đúng dữ liệu.
