




4 MỨC ĐỘ HIỂU THUẬT TOÁN

	Mức 1 – Hiểu khái niệm  Biết thuật toán dùng để làm gì
	Mức 2 – Hiểu vận hành  Tự mô phỏng từng bước trên giấy
	Mức 3 – Hiểu cấu trúc  Bóc tách vai trò từng biến, lý do từng lệnh
	Mức 4 – Hiểu sáng tạo  Tinh chỉnh, kết hợp thuật toán để giải bài khó


---

## Mức 1 – Định nghĩa

**Mức 1: Hiểu khái niệm**
**ĐỊNH NGHĨA**
Biết TÊN thuật toán, biết nó GIẢI QUYẾT vấn đề gì, diễn đạt ý tưởng cốt lõi bằng 1-2 câu.

**VÍ DỤ**
*"Tìm kiếm nhị phân là chia đôi liên tục để thu hẹp khoảng tìm kiếm."*

> Đây là câu phát biểu chuẩn của thuật toán tìm kiếm nhị phân

| **ĐỦ để:** | **KHÔNG đủ để:** |
| :--- | :--- |
| ✓ Nói chuyện về thuật toán | ✗ Viết code |
| ✓ Làm trắc nghiệm chọn đáp án | ✗ Áp dụng vào bài tập có biến thể |
| ✓ Trả lời câu hỏi miệng | ✗ Tự debug khi code sai |
| ✓ Giải thích cho bạn nghe | ✗ Giải bài tương tự |


---

## Mức 2 – Hiểu vận hành

**Mức 2: Hiểu vận hành (Operational)**
*   Biết chính xác thuật toán làm GÌ ở từng bước
*   Mô phỏng được trên giấy với ví dụ cụ thể
*   Ghi rõ giá trị TỪNG BIẾN tại TỪNG thời điểm



-> CÓ THỂ MÔ PHỎNG ĐƯỢC TRÊN GIẤY LÀ OK 



---

##  Mức 3 – Hiểu cấu trúc
**Mức 3: Hiểu cấu trúc (Structural)**

*   **VAI TRÒ từng biến:** biến nào ĐẾM, biến nào LƯU KẾT QUẢ, biến nào TẠM
*   **LÝ DO mỗi bước:** tại sao bước này ở đây, không phải chỗ khác
*   **PATTERN tổng quát:** đây là 'vòng lặp tìm cực trị', 'duyệt mảng cộng dồn'...

> **KẾT QUẢ: Giải được không chỉ bài đã học, mà cả các bài BIẾN THỂ, TƯƠNG TỰ, CÙNG DẠNG**

> Mức 3 thấy được 'KHUNG XƯƠNG' của thuật toán


>>> # nhắc lại code binary search buổi trước , đoạn cập nhật biến mid 

---

## Mức 4 – Hiểu sáng tạo

**Mức 4: Hiểu sáng tạo (Creative)**

*   Tự THIẾT KẾ thuật toán cho bài toán mới
*   KẾT HỢP nhiều thuật toán đã biết
*   TỐI ƯU thuật toán có sẵn

> **Đây là mức của LẬP TRÌNH VIÊN GIỎI và THÍ SINH thi học sinh giỏi Tin học**

> Đừng vội lên mức 4 - hãy chắc Mức 2 và 3 trước



---
**TỰ ĐÁNH GIÁ NGAY**

Lấy một thuật toán bạn nghĩ là mình "đã hiểu". Tự hỏi:

1. Mô phỏng được với mảng [5,2,8,1,9] mà không nhìn sách?
2. Giải thích được vai trò của TỪNG biến?
3. Nếu đổi đề bài (tìm số nhỏ thứ 2), biết sửa chỗ nào?

*   **Cả 3 = CÓ:** Bạn ở Mức 3 - sẵn sàng viết code
*   **Chỉ câu 1 = Có:** Bạn ở Mức 2 - viết được nhưng chậm
*   **Cả 3 = không chắc:** Bạn ở Mức 1 - cần làm rõ thuật toán hơn


---


**1.3. Tại sao Mức 1 không đủ?**

**Lý do 1: Ngôn ngữ CON NGƯỜI ≠ ngôn ngữ MÁY**

| **Bạn nói:** | **Máy cần:** |
| :---: | :---: |
| *"so sánh hai phần tử liền kề"*<br>→ Trong đầu bạn có hình ảnh 2 con số đứng cạnh nhau | 1. truy_cap_vi_tri(arr, i)<br>2. truy_cap_vi_tri(arr, i+1)<br>3. so_sanh_lon_hon(a, b) |

*(Mũi tên "dịch" từ trái sang phải)*

> Cùng 1 ý, con người nói 1 câu, máy cần 3 lệnh!

---


**Lý do 2: Khái niệm BỎ QUA chi tiết kỹ thuật**

**Ví dụ: thuật toán "Sắp xếp nổi bọt"**

> Khái niệm: "so sánh 2 phần tử liền kề, đổi chỗ nếu sai thứ tự"

**Khái niệm KHÔNG nói:**
*   Bắt đầu so sánh từ đâu? (đầu hay cuối mảng)
*   Vòng lặp ngoài chạy đến đâu thì dừng?
*   Nếu mảng đã sắp xếp giữa chừng, có dừng sớm được không?
*   Khi đổi chỗ, có cần BIẾN TẠM không

**1.4. Bài kiểm tra tự đánh giá**

**Sắp xếp nổi bọt với mảng arr = [6,7,1,3,5]**

### **Lượt quét 1: Đưa phần tử lớn nhất về cuối mảng**

_Mảng ban đầu:_ $[6, 7, 1, 3, 5]$

1. **So sánh `6` và `7`:** Đúng thứ tự ($6 < 7$) $\rightarrow$ Giữ nguyên.
    
    - Mảng: $[6, 7, 1, 3, 5]$
        
2. **So sánh `7` và `1`:** Ngược thứ tự ($7 > 1$) $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[6, 1, 7, 3, 5]$
        
3. **So sánh `7` và `3`:** Ngược thứ tự ($7 > 3$) $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[6, 1, 3, 7, 5]$
        
4. **So sánh `7` và `5`:** Ngược thứ tự ($7 > 5$) $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[6, 1, 3, 5, 7]$
        

> **Kết thúc lượt 1:** Phần tử **`7`** (lớn nhất) đã cố định ở cuối mảng.

### **Lượt quét 2: Xử lý đoạn mảng còn lại $[6, 1, 3, 5]$**

1. **So sánh `6` và `1`:** Ngược thứ tự $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[1, 6, 3, 5, 7]$
        
2. **So sánh `6` và `3`:** Ngược thứ tự $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[1, 3, 6, 5, 7]$
        
3. **So sánh `6` và `5`:** Ngược thứ tự $\rightarrow$ **Hoán đổi**.
    
    - Mảng: $[1, 3, 5, 6, 7]$
        

> **Kết thúc lượt 2:** Phần tử **`6`** đã yên vị ở vị trí chính xác của nó.

### **Lượt quét 3: Xử lý đoạn mảng $[1, 3, 5]$**

1. **So sánh `1` và `3`:** Đúng thứ tự $\rightarrow$ Giữ nguyên.
    
    - Mảng: $[1, 3, 5, 6, 7]$
        
2. **So sánh `3` và `5`:** Đúng thứ tự $\rightarrow$ Giữ nguyên.
    
    - Mảng: $[1, 3, 5, 6, 7]$
        

> **Kết thúc lượt 3:** Trong suốt lượt quét này, không có bất kỳ cặp phần tử nào phải hoán đổi. Thuật toán có thể tối ưu bằng cách dừng sớm tại đây.

### **Kết quả cuối cùng**

Mảng đã được sắp xếp tăng dần: **$[1, 3, 5, 6, 7]$**

### **Phản biện ngắn**

Nhìn vào lượt quét thứ 3, ta thấy mảng thực tế đã được sắp xếp xong từ trước đó, nhưng thuật toán vẫn phải chạy qua để kiểm tra.

- Nếu viết code chay bằng 2 vòng lặp lồng nhau thông thường mà _không có biến cờ hiệu (`swapped`)_ để kiểm tra xem có sự hoán đổi nào xảy ra hay không, độ phức tạp trong trường hợp mảng gần như đã sắp xếp xong sẽ bị lãng phí như thế nào?



# # chapter 2 : các khó khăn thường gặp 


---
# Tình huống 1

**TÌNH HUỐNG 1**
**"Nhìn đề bài, đầu óc trống rỗng"**

**[1] Mô tả tình huống**

**ĐỀ BÀI:**
Cho dãy N số nguyên. Đếm số cặp (i, j) sao cho i < j và arr[i] + arr[j] chia hết cho 3.

**Bạn hiểu đề... nhưng KHÔNG BIẾT bắt đầu từ đâu**

```
int main() { |
```

*30 phút trôi qua... vẫn trống rỗng.*

> Đề không khó, từ ngữ hiểu hết – nhưng đầu trống không



---



**[3] Giải pháp**

1. **Đầu VÀO của bài là gì?** *(dạng dữ liệu, kích thước)*
2. **Đầu RA cần là gì?** *(1 số? 1 dãy? 1 chuỗi?)*
3. **Bài thuộc DẠNG nào?** *(count ? search? sort? Kiểm tra?)*
4. **Với VÍ DỤ NHỎ, kết quả là bao nhiêu?** *(tự tạo 3-4 phần tử)*
5. **Mình sẽ giải bằng TAY như thế nào?** ← **QUAN TRỌNG NHẤT**

> Giải pháp: 5 CÂU HỎI mở khóa bất kỳ bài nào

**[4] Áp dụng cho đề bài thực tế**

arr = {1, 2, 3, 4}. Đếm cặp (i,j), i<j, (arr[i]+arr[j]) % 3 == 0

| i=0 | i=1 | i=2 | i=3 |
|-----|-----|-----|-----|
| **1** | **2** | **3** | **4** |

**Đếm: 2**

**Liệt kê các cặp:**
- (0,1): 1+2=3 ✅
- (0,2): 1+3=4 ❌
- (0,3): 1+4=5 ❌
- (1,2): 2+3=5 ❌
- (1,3): 2+4=6 ✅
- (2,3): 3+4=7 ❌

→ **Đó CHÍNH LÀ thuật toán! Duyệt cặp, kiểm tra điều kiện, đếm.**

> Bây giờ chuyển sang code chỉ là DỊCH lại các bước này



 còn cách tối ưu hơn ở phần sau 
---

nói 1 chút về cách học các cú pháp : 



**"Biết phải dùng vòng lặp, nhưng không biết viết"**

**[1] Mô tả tình huống**

- Đã giải tay xong ✓
- Biết phải có vòng lặp ✓
- Nhớ cú pháp for ✓
- `for (` ← dùng ở đây ✗

**Biến đếm chạy từ đâu? Dừng khi nào? Bên trong làm gì?**

> Càng nghĩ càng rối - vì học cú pháp như 'công thức cố định'

---



**[2] Phân tích tâm lý**

**BẠN học cú pháp như công thức cố định:**

```cpp
for (int i = 1; i <= 10; i++) {
    cout << i << " ";
}
```
→ *Chỉ nhớ ví dụ này, không biết biến đổi*

**Đúng ra phải học CẤU TRÚC TỔNG QUÁT:**

```cpp
for ( KHỞI_TẠO ; ĐIỀU_KIỆN_TIẾP_TỤC ; CẬP_NHẬT ) {
    CÔNG_VIỆC_TRONG_VÒNG_LẶP
}
```
4 ô trống → 4 câu hỏi để điền vào
→ *Mỗi chỗ cần ĐIỀN TÙY BÀI, không có công thức cố định*

---



**[3] Giải pháp: 4 câu hỏi**

1. **Mình cần biến đếm để LÀM GÌ?** *(chỉ số mảng arr[i]? hay đếm số lần?)*
2. **Biến đếm BẮT ĐẦU từ giá trị nào?** *(0? 1? n-1? i+1?)*
3. **Vòng lặp DỪNG khi nào?** *(i < n? hay i <= n? CẨN THẬN off-by-one!)*
4. **Sau mỗi vòng, biến đếm THAY ĐỔI thế nào?** *(i++? i-=2? i*=2? i=(i+1)/2?)*

Lỗi **off-by-one (OBOE)** là một trong những cái bẫy kinh điển và dễ gặp nhất khi lập trình. Nói một cách đơn giản, lỗi này xảy ra khi một vòng lặp hoặc một phép tính điều kiện chạy **thừa hoặc thiếu chính xác 1 bước** (quá 1 phần tử hoặc chưa tới phần tử cuối).

Gốc rễ của vấn đề thường nằm ở **sự lệch pha** trong cách con người đếm (bắt đầu từ 1) và cách máy tính tư duy (đếm từ 0).

### Các kịch bản "sập bẫy" phổ biến

#### 1. Duyệt mảng (Vòng lặp `for`)

Đây là nơi OBOE xuất hiện nhiều nhất, đặc biệt là khi dùng toán tử so sánh cấu hình biên.

- **Bẫy `<=` (Chạy quá 1 phần tử):**
    
    C++
    
    ```
    int arr[5] = {6, 7, 1, 3, 5};
    // Mảng có 5 phần tử, chỉ số (index) hợp lệ là từ 0 đến 4.
    for (int i = 0; i <= 5; i++) { 
        cout << arr[i] << " "; // Khi i = 5, arr[5] sẽ truy cập vào vùng nhớ rác hoặc gây lỗi Segmentation Fault!
    }
    ```
    
- **Bẫy `<` (Chạy thiếu 1 phần tử):**
    
    Ngược lại, nếu bạn muốn lặp $n$ lần nhưng lại bắt đầu từ `i = 1` và điều kiện là `i < n`, vòng lặp sẽ dừng sớm và chỉ chạy được $n-1$ lần.
    

#### 2. Tính toán khoảng cách hoặc độ dài ( Fencepost Error)

Hãy tưởng tượng bạn muốn xây một hàng rào dài 100 mét, cứ mỗi 10 mét bạn cắm một cây cột. Bạn cần bao nhiêu cây cột?

- Tính nhanh: $100 / 10 = 10$ cây?
    
- Thực tế: Bạn cần **11 cây** (vì phải tính cả cây cột ở vạch 0 mét ban đầu).
    

Trong lập trình, khi tính số lượng phần tử trong một đoạn từ chỉ số `đầu` đến `cuối`, công thức đúng phải là:

$$\text{Số phần tử} = \text{cuối} - \text{đầu} + 1$$

Nếu quên cộng $1$, bạn đã dính lỗi off-by-one.



Để tránh việc phải căng não đếm xem nên dùng `<` hay `<=`, các kỹ sư hệ thống thường áp dụng các nguyên tắc thiết kế bất biến:

1. **Ưu tiên khoảng nửa mở (Half-open intervals): $[a, b)$**
    
    Tức là bao gồm điểm đầu nhưng loại trừ điểm cuối. Hầu hết các ngôn ngữ hiện đại (Python với `range(a, b)`, C++ với các iterator `begin()` và `end()`) đều thiết kế theo kiểu này.
    
    - Nếu khoảng là $[0, n)$, số phần tử chính bằng $n$.
        
    - Vòng lặp chuẩn luôn là: `for (int i = 0; i < n; i++)`
        


> **LI OFF-BY-ONE:** mảng N phần tử có chỉ số 0 → N-1
> Đúng: `i < n` | Sai: `i <= n` | Sai: `i = 1; i < n` (bỏ số)

> Off-by-one là lỗi phổ biến nhất của người mới

---


**[4] Áp dụng - cùng đề bài hồi nãy** (cặp tổng chiaw hết cho 3 )

- **Q1: Biến đếm để LÀM GÌ?** → Cần 2 chỉ số: i và j → 2 vòng lặp lồng nhau
- **Q2: BẮT ĐẦU từ đâu?** → i từ 0, j từ i + 1 (vì j > i)
- **Q3: DỪNG khi nào?** → i < n - 1, j < n
- **Q4: CẬP NHẬT thế nào?** → i++ và j++

> Áp dụng cho đề bài 'đếm cặp tổng chia hết cho 3'

---


**[4] Áp dụng - cùng đề bài hồi nãy**

**Ráp lại 4 câu trả lời → CODE:**

```cpp
int count = 0;
for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
        if ((arr[i] + arr[j]) % 3 == 0) {
            count++;
        }
    }
}
cout << count << endl;
```

> 4 câu hỏi → 4 câu trả lời → CODE ra ngay

Bài này đang đếm số cặp `(i, j)` mà `(arr[i] + arr[j]) % 3 == 0`.

> ### tối ưu (mở rộng) 

**Ý tưởng tối ưu:** thay vì duyệt mọi cặp O(n²), chỉ cần quan tâm đến **phần dư khi chia 3** của từng phần tử — vì `(a + b) % 3 == 0` khi và chỉ khi phần dư của a và b **cộng lại chia hết cho 3**.

sử dụng tư duy toán học (đồng dư thức) kết hợp mảng tần suất để tối ưu toán bộ quá trình xử lý chỉ trong **$O(n)$**

Chỉ có 3 nhóm phần dư: **0, 1, 2**

- Nhóm 0 + Nhóm 0 ✅
- Nhóm 1 + Nhóm 2 ✅
- Nhóm 2 + Nhóm 1 ✅



 bài toán: **Đếm số cặp phần tử $(arr[i], arr[j])$ (với $i < j$) trong mảng sao cho tổng của chúng chia hết cho 3.**

### 1. Phân loại bằng phép chia lấy dư (`arr[i] % 3`)

Bất kỳ một số nguyên nào khi chia cho 3 cũng chỉ có 3 loại số dư khả thi: **0, 1, hoặc 2**.

Để tổng của hai số chia hết cho 3, tổng hai số dư của chúng phải chia hết cho 3. Có hai trường hợp xảy ra:

- **Trường hợp 1:** Một số chia hết cho 3 (dư 0) cộng với một số khác cũng chia hết cho 3 (dư 0). Ví dụ: $3 + 6 = 9 \pmod 3$.
    
- **Trường hợp 2:** Một số chia cho 3 dư 1 kết hợp với một số chia cho 3 dư 2. Ví dụ: $4 \pmod 3 = 1$ và $5 \pmod 3 = 2$, tổng $4 + 5 = 9 \pmod 3$.
    
# NHỚ CODE COMMENT TRƯỚC 
### 2. Bước 1: Gom nhóm và đếm tần suất

C++

```
long long cnt[3] = {0, 0, 0};
for (int i = 0; i < n; i++) {
    cnt[arr[i] % 3]++;
}
```

- Mảng `cnt` kích thước bằng 3 đóng vai trò như các "thùng chứa" (buckets) dùng để đếm số lượng phần tử thuộc từng nhóm số dư:
    
    - `cnt[0]`: Số lượng phần tử chia hết cho 3.
        
    - `cnt[1]`: Số lượng phần tử chia cho 3 dư 1.
        
    - `cnt[2]`: Số lượng phần tử chia cho 3 dư 2.
        
- **Tránh bẫy tràn số (Overflow):** Khai báo kiểu `long long` cho `cnt` là một nước đi rất kỹ lưỡng. Khi $n$ lớn (ví dụ $10^5$), số lượng phần tử trong mỗi nhóm có thể lên tới $10^5$, lúc tính số cặp ở bước sau sẽ vượt quá giới hạn của kiểu `int`.
    

### 3. Bước 2: Công thức tổ hợp để tính số cặp

Sau khi đã có số lượng phần tử của từng nhóm, ta áp dụng toán tổ hợp để đếm số cặp thỏa mãn.

#### Nhóm chia hết cho 3 (Dư 0)

C++

```
count += cnt[0] * (cnt[0] - 1) / 2;
```

- _Lưu ý:_ Trong prompt của bạn bị thiếu dấu `*` ở đoạn này do lỗi gõ phím, cú pháp đúng phải có phép nhân.
    
- Để tạo thành một cặp chia hết cho 3 từ nhóm này, ta cần chọn ra 2 phần tử bất kỳ từ `cnt[0]` phần tử sẵn có.
    
- Đây chính là công thức tính số tổ hợp chập 2 của $k$ phần tử:
    
    $$C_k^2 = \frac{k \times (k - 1)}{2}$$
    
    _(Trong đó $k = cnt[0]$)_.
    

#### Nhóm dư 1 kết hợp nhóm dư 2

C++

```
count += cnt[1] * cnt[2];
```

- _Lưu ý:_ Đoạn này cũng cần có dấu nhân `*` ở giữa.
    
- Để tạo thành một cặp, ta bắt buộc phải chọn **1 phần tử** từ nhóm dư 1 (có `cnt[1]` cách chọn) và **1 phần tử** từ nhóm dư 2 (có `cnt[2]` cách chọn).
    
- Theo quy tắc nhân trong tổ hợp, tổng số cặp tạo thành sẽ là: $cnt[1] \times cnt[2]$.
    

### Ví dụ minh họa trực quan

Giả sử mảng ban đầu là: `arr = [3, 6, 1, 4, 2]` ($n = 5$)

1. **Chạy qua vòng lặp gom nhóm:**
    
    - `3 % 3 = 0`, `6 % 3 = 0` $\rightarrow$ `cnt[0] = 2`
        
    - `1 % 3 = 1`, `4 % 3 = 1` $\rightarrow$ `cnt[1] = 2`
        
    - `2 % 3 = 2` $\rightarrow$ `cnt[2] = 1`
        
2. **Tính toán kết quả:**
    
    - Cặp từ nhóm dư 0: $2 \times (2 - 1) / 2 = \mathbf{1}$ cặp (chính là cặp $(3, 6)$).
        
    - Cặp từ nhóm dư 1 và dư 2: $2 \times 1 = \mathbf{2}$ cặp (gồm cặp $(1, 2)$ và $(4, 2)$).
        
3. **Tổng cộng:** `count = 1 + 2 = 3` cặp thỏa mãn.
    
```cpp
long long cnt[3] = {0, 0, 0};
for (int i = 0; i < n; i++) {
    cnt[arr[i] % 3]++;
}

long long count = 0;
count += cnt[0] * (cnt[0] - 1) / 2;  // cặp trong nhóm dư 0
count += cnt[1] * cnt[2];             // cặp nhóm dư 1 + nhóm dư 2

cout << count << endl;
```
### Phản biện ngắn

Đoạn code trên chạy rất mượt với các số nguyên dương. Tuy nhiên, nếu mảng `arr` chứa **số nguyên âm** (ví dụ: `-3`, `-1`), phép toán `arr[i] % 3` trong C++ sẽ trả về kết quả âm (ví dụ `-1 % 3 = -1`).

Lúc này, câu lệnh `cnt[arr[i] % 3]++` sẽ cố gắng truy cập vào chỉ số âm của mảng (`cnt[-1]`), gây ra lỗi tràn bộ nhớ (Out of bounds). Để hệ thống này chạy an toàn 100% với cả số âm, bạn sẽ chỉnh sửa công thức lấy dư ở dòng `arr[i] % 3` như thế nào để đưa số dư về khoảng từ `0` đến `2`?


Để xử lý triệt để số dư âm trong C++, mục tiêu của chúng ta là biến các kết quả dư âm như `-1` hay `-2` về đúng nhóm của nó trong toán học:

- Số chia 3 dư `-1` thực chất là thiếu 1 để chia hết, nghĩa là nó đồng dư với **`2`** (ví dụ: $-1 \equiv 2 \pmod 3$).
    
- Số chia 3 dư `-2` thực chất là thiếu 2 để chia hết, nghĩa là nó đồng dư với **`1`** (ví dụ: $-2 \equiv 1 \pmod 3$).
    

Để đưa mọi giá trị số dư về khoảng từ `0` đến `2` mà không cần dùng câu lệnh điều kiện `if`, dân chuyên hệ thống thường dùng một "mẹo" toán học dịch chuyển biên sau đây:

C++

```
(arr[i] % 3 + 3) % 3
```

### Cơ chế hoạt động của công thức này:

1. **`arr[i] % 3`**: Phép chia lấy dư thông thường của C++, có thể trả về `-2, -1, 0, 1, 2`.
    
2. **`+ 3`**: Cộng thêm đúng bằng giá trị của số chia để đảm bảo kết quả tạm thời chắc chắn là một số dương (biến `-2` thành `1`, `-1` thành `2`).
    
3. **`% 3`**: Chia lấy dư một lần nữa. Bước này cực kỳ quan trọng vì nếu ban đầu `arr[i] % 3` đã là số dương (ví dụ là `1`), sau khi `+ 3` nó sẽ thành `4`, và phép `% 3` cuối cùng này sẽ đưa nó về lại đúng vị trí ban đầu là `1`.
    

Áp dụng vào vòng lặp của bạn để "vô địch" mọi bộ test case (kể cả số âm):

C++

```
for (int i = 0; i < n; i++) {
    int remainder = (arr[i] % 3 + 3) % 3;
    cnt[remainder]++;
}
```


Công thức `(val % M + M) % M` là một pattern kinh điển để xử lý số dư âm trong lập trình thi đấu và cấu trúc dữ liệu.






**Độ phức tạp:** O(n) thay vì O(n²)

Với n = 100.000 thì code cũ chạy ~10 tỷ phép tính, code mới chỉ ~100.000 — nhanh hơn **100.000 lần**.




# Tình huống 6

**TÌNH HUỐNG 6**
**"Bài này hiểu, bài tương tự lại tắc"**

**[1] Mô tả tình huống**

| Bài CŨ (đã làm):                                    | Bài MỚI (tương tự):                                     |
| :-------------------------------------------------- | :------------------------------------------------------ |
| Tìm số NHỎ NHẤT trong mảng<br>→ "Ơ! Mình làm được!" | Tìm số NHỎ THỨ HAI trong mảng<br>→ "Hả? Bài gì lạ vậy?" |

> Cùng dạng nhưng vẫn tắc - vì bạn học BÀI, không phải học MẪU

---




### **MẫU NỀN TẢNG**
*Duyệt mảng • Tính tổng • Đếm*

**MẪU 1 Duyệt mảng (Array Traversal)**

```cpp
for (int i = 0; i < n; i++) {
    // Làm gì đó với arr[i]
}
```
từ đó mở rộng ra các hướng khác :
- → Duyệt ngược: i = n-1; i >= 0; i--
- → Bước nhảy: i += 2 (chỉ phần tử chẵn)
- → Từ phần tử thứ 2: i = 1
- → Nửa đầu: i < n/2

> Mẫu 1: Duyệt mảng - xuất hiện trong HẦU HẾT bài có mảng

---


**MẪU 2 Tính tổng (Sum Accumulation)**

```cpp
long long sum = 0;       // bước 1: khởi tạo
for (int i = 0; i < n; i++) {
    sum += arr[i];       // bước 2: cộng dồn
}
```


> **Dùng long long! int tràn số khi tổng > 2 tỷ**

> Mẫu 2: Tính tổng - cộng dồn từng phần tử

---


**MẪU 3 Đếm (Counting)**

```cpp
int count = 0;          // khởi tạo bộ đếm
for (int i = 0; i < n; i++) {
    if (/* điều kiện */) {
        count++;        // tăng đếm
    }
}
```


> Mẫu 3: Đếm - giống tính tổng nhưng +1 thay vì +giá trị

---



**So sánh Mẫu 2 vs Mẫu 3:**

| **MẪU 2: Tính tổng** | **MẪU 3: Đếm** |
| :--- | :--- |
| `long long sum = 0;`<br>`for (i = 0; i < n; i++)`<br>`if (điều kiện)`<br>`sum += arr[i]`<br>`// 1 CỘNG GIÁ TRỊ` | `int count = 0;`<br>`for (i = 0; i < n; i++)`<br>`if (điều kiện)`<br>`count++;`<br>`// 1 TĂNG 1` |

**Hiểu mẫu → nhận ra: nhiều bài KHÁC NHAU thực ra cùng cấu trúc**

> So sánh Mẫu 2 và Mẫu 3 - khác đúng 1 dòng



### **Mẫu 4 & 5**
*Tìm cực trị • Tìm kiếm tuyến tính*

**MẪU 4 Tìm cực trị (Find Extremum)**

```cpp
int max_value = arr[0];   // khởi tạo bằng phần tử đầu
for (int i = 1; i < n; i++) {
    if (arr[i] > max_value) { // so sánh
        max_value = arr[i];   // cập nhật
    }
}
```


*   Khởi tạo = arr[0], KHÔNG phải = 0 (mảng có thể toàn âm!)
*   i = 1 (không phải 0) vì arr[0] đã dùng làm khởi tạo
*   Biến thể: tìm VỊ TRÍ → lưu max_pos thay max_value

> Mẫu 4: Tìm cực trị - lớn nhất/nhỏ nhất, nhiều biến thể

---



**MẪU 5 Tìm kiếm tuyến tính (Linear Search)**

```cpp
bool found = false;
for (int i = 0; i < n; i++) {
    if (arr[i] == target) {
        found = true;
        break;    // dừng ngay khi tìm thấy
    }
}
```
*(Hình minh họa mảng: 3, 7, 2, 9, 5, 8, 1. Text: Tìm target = 9. Tìm thấy! BREAK)*

**Mảng 1 triệu phần tử, target ở vị trí 5 → break tiết kiệm 999,995 vòng!**

> 'break' không phải tùy chọn - là BẮT BUỘC với bài lớn

---



### **Mẫu 6 & 7**
*Lọc phần tử • Vòng lặp lồng nhau*

**MẪU 6 Lọc phần tử (Filter)**

```cpp
int result[1000];
int result_size = 0;

for (int i = 0; i < n; i++) {
    if (/* điều kiện */) {
        result[result_size] = arr[i];
        result_size++;
    }
}
```


**result_size = 3 → result chỉ có 3 phần tử đầu là kết quả**

> Mẫu 6: Lọc - tạo mảng MỚI chứa phần tử thỏa điều kiện

---



**MẪU 7 Vòng lặp lồng nhau (Nested Loops)**

```cpp
// Mọi cặp (i, j) với i < j
for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
        // Xử lý cặp (arr[i], arr[j])
    }
}
```


**Độ phức tạp O(n²) - với n = 100,000 → 10 TỶ thao tác (quá chậm!)**

> Quy tắc: n ≤ 10,000 OK. n ≥ 100,000 → cần thuật toán khác




---



### **Mẫu 8 & 9**
*Hoán đổi • Vòng lặp while*

**MU 8 Hoán đổi (Swap)**

| **Cách 1: Biến tạm (kinh điển)** | **Cách 2: hàm swap có sẵn** |
| :--- | :--- |
| `int temp = a;`<br>`a = b;` | `#include <algorithm>`<br>`swap(a, b);` |



---


**MẪU 9 Vòng lặp while**

> **QUY TẮC CHỌN VÒNG LẶP:**
> BIẾT trước số lần → dùng FOR | KHÔNG BIẾT → dùng WHILE

**DEMO: Đếm số chữ số của n = 1234**
n = 0, count = 4

```cpp
int count = 0;
while (n > 0) {
    n = n / 10;   // bỏ chữ số cuối
    count++;
}
```

**Trong while, BẮT BUỘC có biến điều kiện thay đổi → tránh lặp VÔ HẠN!**

> Mẫu 9: while - khi KHÔNG biết trước số lần lặp


NHẮC TỚI 1 LỖI CHẴN LẺ -> VÒNG LẶP VÔ HẠN : I = 1 , WHILE (I  !=10) {I = I +2 }



---


### **Mẫu 11 & 12**
*Hàm con • Đọc input động*

**MẪU 11 Hàm con (Function)**

```cpp
int find_max(int arr[], int n) {
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max_val)
            max_val = arr[i];
    }
    return max_val;
}

int main() {
    int arr[] = {3, 7, 2, 9, 5};
    int result = find_max(arr, 5);
    cout << result;    // 9
}
```

**NGUYÊN TẮC: 1 HÀM = 1 VIỆC**
- ✓ find_max: tìm max (không in, không sửa)
- ✓ print_array: in mảng (không tính)
- ✓ is_prime: kiểm tra (trả true/false)

> Mẫu 11: Hàm con - công cụ tổ chức code KHÔNG xa xỉ

---



**MẪU 12 Đọc input động (Dynamic Input)**

| **Đọc đến HẾT FILE:**                                                                                          | **Đọc đến SỐ 0:**                                                                                                        |
| :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| `int x;`<br>`int arr[1000];`<br>`int n = 0;`<br>`while (cin >> x) {`<br>`    arr[n] = x;`<br>`    n++;`<br>`}` | `int x;`<br>`int arr[1000];`<br>`int n = 0;`<br>`while (cin >> x && x != 0) {`<br>`    arr[n] = x;`<br>`    n++;`<br>`}` |
|                                                                                                                |                                                                                                                          |

**cin >> x trả về FALSE khi hết input → tự động dừng**

> Cấu trúc này có Vẻ kỳ lạ nhưng RẤT phổ biến trong bài thi

### Mẫu 13–15: Chuỗi, Số học, Mảng 2 chiều

**Mẫu 13 – Duyệt chuỗi (String Traversal)**

cpp

```cpp
string s;
cin >> s;
int n = s.length();

for (int i = 0; i < n; i++) {
    // làm gì đó với s[i]
    if (s[i] == 'a') count++;       // so sánh ký tự
    s[i] = toupper(s[i]);           // đổi hoa/thường
}
```

Biến thể phổ biến:

- Đếm ký tự xuất hiện: `freq[s[i] - 'a']++`
- Kiểm tra palindrome: so sánh `s[i]` với `s[n-1-i]`


> Chuỗi về bản chất là **mảng ký tự** — mọi mẫu duyệt mảng đều áp dụng được


