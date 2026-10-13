
# DATA → ML CHECKLIST

```text
Raw files
   ↓
1. Data inventory
   ↓
2. Understand data structure
   ↓
3. Clean & validate
   ↓
4. Reconstruct cold-chain trajectories
   ↓
5. Link exposure ↔ quality
   ↓
6. Build ML dataset
   ↓
7. Prevent leakage + split data
   ↓
8. EDA + final validation
   ↓
READY FOR ML
```

---

## STAGE 1 — Data inventory

### ☐ 1.1. Liệt kê toàn bộ file

Xác định:

- ☐ sensor files
    
- ☐ processed sensor files
    
- ☐ quality files
    
- ☐ metadata
    
- ☐ photos
    
- ☐ scripts
    
- ☐ documentation
    

### ☐ 1.2. Xác định cấu trúc thư mục

Ví dụ:

```text
01_src_subset_dataset_T_H
02_res_subset_dataset_T_H
03_src_...
04_res_...
...
13_src_extra_subset_dataset_Photo
```

### ☐ 1.3. Tạo data dictionary

Mỗi variable cần có:

|Variable|Meaning|Unit|Type|
|---|---|---|---|
|Time|timestamp|min|datetime|
|Temp|air temperature|°C|float|
|Hum|relative humidity|%|float|
|...|...|...|...|

### ☐ 1.4. Xác định entity / ID

Cực kỳ quan trọng:

```text
Shipment
Box
Mango
Sensor
Step
Experiment
Quality measurement
```

Phải biết **ID nào liên kết được với ID nào**.

---

# STAGE 2 — Hiểu cấu trúc dữ liệu

### ☐ 2.1. Hiểu cold-chain timeline

Phải reconstruct được:

```text
Step 0
Packing house
   ↓
Step 1
Cold storage
   ↓
Step 2
Truck
   ↓
...
Step 7
Flight
   ↓
Step 8
CDG
   ↓
...
Step 10
INRAE
```

### ☐ 2.2. Xác định timestamp

Kiểm tra:

- ☐ timezone
    
- ☐ timestamp format
    
- ☐ sampling interval
    
- ☐ missing timestamps
    
- ☐ duplicate timestamps
    

### ☐ 2.3. Hiểu sensor mapping

Ví dụ:

```text
Sensor
  ↓
Box
  ↓
Position
  ↓
Step
```

Không được nhầm:

> sensor ID ≠ mango ID ≠ box ID.

---

# STAGE 3 — Data cleaning & validation

### ☐ 3.1. Missing values

Kiểm tra:

```python
df.isna().sum()
```

và:

- ☐ missing percentage
    
- ☐ missing by sensor
    
- ☐ missing by step
    
- ☐ missing by time period
    

### ☐ 3.2. Duplicate

```python
df.duplicated()
```

### ☐ 3.3. Invalid values

Ví dụ:

```text
Temperature = -999
RH = 250%
pH = 40
```

→ phải phát hiện.

### ☐ 3.4. Outliers

Không được tự động xóa outlier.

Phân biệt:

```text
real excursion
     vs
sensor error
```

Đây rất quan trọng vì **temperature excursion chính là feature nghiên cứu**.

### ☐ 3.5. Sampling consistency

Kiểm tra:

```text
5 min
5 min
5 min
5 min
...
```

Nếu:

```text
5 min
5 min
35 min
5 min
```

phải ghi nhận gap.

---

# STAGE 4 — Reconstruct cold-chain exposure

Đây là **phần quan trọng nhất trước ML**.

### ☐ 4.1. Tạo trajectory

Ví dụ:

```text
box_01
   ↓
Step 0 → Step 1 → Step 2 → ... → Step 10
```

### ☐ 4.2. Ghép temperature

```text
air_temperature
```

### ☐ 4.3. Ghép mango/surface temperature

```text
mango_temperature
```

### ☐ 4.4. Ghép RH

```text
relative_humidity
```

### ☐ 4.5. Xác định exposure window

Ví dụ:

```text
D0 → transport → arrival
```

hoặc tùy research question:

```text
transport exposure
      ↓
quality at D3
```

Phải **chốt exposure window trước khi tạo feature**.

---

# STAGE 5 — Link exposure với quality

Đây là bước dễ sai nhất.

Ta cần tạo quan hệ:

```text
Exposure history
        ↓
Quality measurement
```

Ví dụ:

```text
Box 12
Transport exposure
      ↓
Mango quality
D0 / D3 / D6 / D9 / D12 / D15
```

### ☐ 5.1. Xác định quality unit

Là:

```text
box?
mango?
experiment?
```

### ☐ 5.2. Xác định quality timestamp

### ☐ 5.3. Mapping exposure → quality

### ☐ 5.4. Kiểm tra one-to-one / one-to-many

### ☐ 5.5. Kiểm tra unmatched records

# STAGE 6 — Build ML dataset

 bắt đầu **feature engineering**.

## 6.1 Summary features

☐ mean temperature  
☐ min temperature  
☐ max temperature  
☐ temperature SD  
☐ temperature variance  
☐ mean RH  
☐ min/max RH  
☐ mean mango temperature

---

## 6.2 Exposure features

☐ time above 20°C  
☐ time above 25°C  
☐ number of excursions  
☐ excursion duration  
☐ maximum excursion  
☐ cumulative exposure  
☐ temperature change rate  
☐ temperature variability

---

## 6.3 Interaction features



# STAGE 7 — Define target

tách:

### Input

```text
Cold-chain exposure
```

### Target

```text
Quality degradation
```

Ví dụ:

y=MassLossy = MassLoss

hoặc:

y=Δb∗y = \Delta b^*

hoặc:

y=ΔpHy = \Delta pH

hoặc:

y=ΔTSSy = \Delta TSS

### ☐ 7.1. Chọn target

### ☐ 7.2. Xác định prediction horizon

Ví dụ:

```text
Transport exposure
        ↓
Quality at D3
```

hay:

```text
Transport exposure
        ↓
Quality at D6
```

### ☐ 7.3. Xác định baseline quality

Có thể cần:

ΔQuality=Qualityt−QualityD0\Delta Quality = Quality_t - Quality_{D0}

thay vì dùng absolute quality.

---

# STAGE 8 — Leakage & train/test split

**Đây là gate bắt buộc trước khi chạy ML.**

### ☐ 8.1. Xác định unit độc lập

Ví dụ:

```text
mango
box
trajectory
```

### ☐ 8.2. Không random split từng sensor row

Sai:

```text
sensor rows
   ↓
random train/test
```

vì cùng một trajectory có thể xuất hiện ở cả train và test.

### ☐ 8.3. Group split

Ví dụ:

```text
Box 1 ─┐
Box 2 ─┤ Train
Box 3 ─┘

Box 4 ─┐
Box 5 ─┤ Test
```

hoặc GroupKFold.

### ☐ 8.4. Kiểm tra temporal leakage

Không được để information xảy ra **sau thời điểm prediction** lọt vào feature.

Ví dụ nếu:

```text
Predict quality at D6
```

thì không được dùng:

```text
D9
D12
D15
```

để tạo input.

---

# STAGE 9 — EDA trước ML

### ☐ 9.1. Temperature distribution

### ☐ 9.2. RH distribution

### ☐ 9.3. Mango vs air temperature

### ☐ 9.4. Temperature by supply-chain step

### ☐ 9.5. Exposure vs quality

Ví dụ:

```text
Time > 20°C
       ↓
Mass loss
```

### ☐ 9.6. Correlation

```python
df.corr(numeric_only=True)
```

Nhưng **correlation ≠ causal effect**.

### ☐ 9.7. Check target distribution

Ví dụ:

```text
Mass loss
0–5%
5–10%
10–15%
...
```

---

# STAGE 10 — Final ML-ready dataset

Chỉ tick **READY** khi có bảng kiểu:

|sample_id|exposure features|quality target|group_id|
|---|---|---|---|
|M001|...|...|Box01|
|M002|...|...|Box01|
|M003|...|...|Box02|
|...|...|...|...|

và biết rõ:

```text
X = exposure features
y = quality degradation
group = independent unit
```

Sau đó mới:

```text
                X
                ↓
       Train / Validation / Test
                ↓
       ┌────────┼────────┐
       ↓        ↓        ↓
      LR        RF      XGBoost
       └────────┼────────┘
                ↓
             Metrics
```

---



```text
DATA PREPARATION
□ 1. Inventory all files
□ 2. Build data dictionary
□ 3. Identify entities and IDs
□ 4. Reconstruct cold-chain timeline
□ 5. Validate timestamps and sampling intervals
□ 6. Clean missing/duplicate/invalid data
□ 7. Validate sensor anomalies
□ 8. Map sensor → box → step
□ 9. Map exposure → quality measurements
□ 10. Resolve unmatched records
□ 11. Define exposure window
□ 12. Define prediction target
□ 13. Define prediction horizon
□ 14. Create summary features
□ 15. Create exposure features
□ 16. Create interaction/domain features
□ 17. Check feature distributions
□ 18. Check target distributions
□ 19. Define independent sample/group
□ 20. Design leakage-safe train/test split
□ 21. Run EDA
□ 22. Document all preprocessing decisions
□ 23. Freeze ML-ready dataset
□ 24. Version dataset + preprocessing code
□ 25. READY FOR MODELING
```

**