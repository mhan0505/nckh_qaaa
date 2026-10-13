

**Tổng quan 7 bước:**

1. **Đọc đề và đặt lại bằng LỜI CỦA MÌNH**
2. **Giải TAY với ví dụ nhỏ**
3. **Viết PSEUDOCODE chi tiết**
4. **Xác định KHUNG CODE C++**
5. **Điền LOGIC CHÍNH vào khung**
6. **Kiểm thử với nhiều TEST CASE**
7. **TINH CHỈNH và làm sạch code**

> **ĐỪNG BỎ BƯỚC! Người mới hay nhảy thẳng vào bước 5.**

---


**BƯỚC 1**
**Đọc đề và đặt lại bằng lời của mình**

**Tại sao bước này QUAN TRỌNG?**

> Tâm lý học: khi đọc, não 'ĐIỀN VÀO' những gì mình mong đợi thấy, không phải những gì THỰC SỰ viết.

→ **Bạn sẽ giải đúng BÀI KHÁC, không phải bài thầy giao!**

> Đây là sai lầm TỒN THỜI GIAN NHẤT của người học

---

**Quy trình: ĐỌC 2 LẦN → GẶP ĐỀ → VIẾT TAY 3 ĐIỂM**

**① ĐẦU VÀO**
*Bài cho mình cái gì? Dạng dữ liệu? Kích thước?*

**② ĐẦU RA**
*Cần in ra cái gì? Định dạng thế nào?*

**③ YÊU CẦU CỐT LÕI**
*Tóm tắt 1 CÂU bằng lời của bạn (KHÔNG copy đề)*

> 3 việc cần ghi ra giấy SAU KHI gặp đề

---



**Áp dụng - bài DEMO của chương:**

**ĐỀ BÀI:**
Cho dãy N số nguyên dương. 'Số đặc biệt' = số LỚN HƠN TỔNG các số đứng trước nó. Đếm số 'đặc biệt'. Số đầu LUÔN được tính.

**① ĐẦU VÀO:** 1 số N (số phần tử) + N số nguyên dương

**② ĐẦU RA:** 1 số duy nhất - số lượng 'số đặc biệt'

**③ YÊU CẦU CỐT LÕI:** Đếm các phần tử > tổng các phần tử đứng trước

> Đã làm rõ: 'số nguyên DƯƠNG' (không có 0/âm), 'số đầu xử lý riêng'

> Nền vững rồi - sẵn sàng cho Bước 2!




**BƯỚC 2**
**Giải tay với ví dụ nhỏ**

**3 lợi ích cùng lúc khi giải tay:**

① Kiểm tra mình HIỂU ĐỀ đúng chưa
② Tự THIẾT KẾ thuật toán (không phải nghĩ trong đầu)
③ Có sẵn KẾT QUẢ MẪU để kiểm tra code sau

> **Bài dễ: giải tay 2 phút → tiết kiệm sai lầm**
> **Bài khó: giải tay 10 phút → tiết kiệm 2 TIẾNG debug!**

> Bước CÓ GIÁ TRỊ NHẤT - nhưng bị bỏ qua nhiều nhất

---


**BƯỚC 3**
**Viết pseudocode (mã giả)**

> **PSEUDOCODE LÀ GÌ?**
> Viết các bước thuật toán bằng TIẾNG VIỆT có CẤU TRÚC,
> gần với code thật nhưng không phụ thuộc cú pháp.

**Khi viết tiếng Việt → não tập trung vào LOGIC, không phân tâm bởi cú pháp**

> Pseudocode = cầu nối giữa TƯ DUY và CODE THẬT

---


**5 quy tắc viết pseudocode tốt:**

 Mỗi dòng = MỘT BƯỚC rõ ràng (không gộp)
② Dùng ĐỘNG TỪ chỉ thao tác: Đọc, Lưu, So sánh, Tăng, In
③ Tên biến CỤ THỂ: count, total (không 'biến nào đó')
④ THUẬT NGỮ thể hiện cấu trúc (vòng lặp, if)
⑤ ĐÁNH SỐ các bước chính (1, 2, 3a, 3b..)

> 5 quy tắc viết pseudocode TỐT

---



**Pseudocode cho bài demo:**

```
Bước 1: Đọc N từ input
Bước 2: Đọc N số vào mảng arr
Bước 3: count = 1    (số đầu luôn tính)
Bước 4: sum = arr[0]  (tổng các số đứng trước)
Bước 5: Duyệt i từ 1 đến N-1:
  5a. NẾU arr[i] > sum THÌ:
        tăng count thêm 1
  5b. Cộng arr[i] vào sum
Bước 6: In count
```

**Mỗi bước pseudocode → 1-2 dòng code C++ ở bước 5**

> Logic đã rõ - dịch sang C++ chỉ là việc máy móc

---


**2 sai lầm phổ biến:**

**Sai 1: QUÁ CHUNG CHUNG**
> "Tìm số lớn nhất rồi in ra."
→ *Đây là TÓM TẮT ĐỀ, không phải pseudocode!*

**Sai 2: QUÁ CHI TIẾT (thành code thật)**
```cpp
for (int i = 0; i < n; i++) {
    if (arr[i] > max) max = arr[i];
}
```
→ *Đây là C++ rồi, mất ý nghĩa pseudocode!*

**ĐÚNG: đủ chi tiết để dịch sang C++, đủ trừu tượng để tập trung logic**

> Tránh 2 sai lầm phổ biến khi viết pseudocode


**BƯỚC 4**
**Xác định khung code C++**

**Khung code chuẩn cho mọi bài C++:**

```cpp
#include <iostream>
using namespace std;

int main() {
    // === PHẦN 1: ĐỌC DỮ LIỆU ===
    int n;
    cin >> n;
    int arr[1000];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // === PHẦN 2: KHAI BÁO BIẾN ===
    // (điền vào theo bài cụ thể)

    // === PHẦN 3: LOGIC CHÍNH ===
    // (điền theo pseudocode)

    // === PHẦN 4: IN KẾT QUẢ ===
    // (điền vào)
}
```
*(Chú thích trên ảnh: 4 phần rõ ràng - chỉ cần điền vào!)*

---


**BƯỚC 5**
**Điền logic chính vào khung**

**Bạn đã có:**
*   ✓ Pseudocode chi tiết (bước 3)
*   ✓ Khung code C++ (bước 4)
*   ✓ Biến đã khai báo (count, sum)
*   ✓ Phần in kết quả đã có

**Quy trình DỊCH từng dòng pseudocode → C++:**

1.  Đọc 1 dòng pseudocode
2.  Viết COMMENT trong code C++ bằng nguyên văn dòng đó
3.  Dịch comment thành 1-2 dòng C++ ngay dưới
4.  Sang dòng pseudocode tiếp theo, lặp lại

> Mỗi dòng pseudocode → comment → 1-2 dòng C++

---



**Dịch song song:**

**PSEUDOCODE:**
```text
Bước 5: Duyệt i từ
1 đến N-1:
5a. NẾU arr[i] > sum:
    tăng count + 1
5b. Cộng arr[i]
    vào sum
```

**C++:**
```cpp
// Bước 5: Duyệt
for (int i = 1; i < n; i++) {
    // 5a: nếu arr[i] > sum
    if (arr[i] > sum) {
        count++;
    }
    // 5b: cộng arr[i] vào sum
    sum += arr[i];
}
```

**Comment giữ nguyên cấu trúc pseudocode → DỄ ĐỐI CHIẾU**

> Đây là cách code chuyên nghiệp!

---



**Code HOÀN CHỈNH:**

```cpp
#include <iostream>
using namespace std;
int main() {
    int n; cin >> n;
    int arr[1000];
    for (int i = 0; i < n; i++) cin >> arr[i];

    int count = 1;
    long long sum = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] > sum) count++;
        sum += arr[i];
    }

    cout << count << endl;
    return 0;
}
```

> Đây là CODE HOÀN CHỈNH cuối cùng

---


**BƯỚC 6**
**Kiểm thử với các test case**

> **Sai lầm phổ biến:** Viết xong, chạy với 1 test qua đề bài, thấy đúng → nộp. Code có thể 'ĐÚNG TÌNH CỜ' với 1 test!

**Lập trình viên CHUYÊN NGHIỆP: kiểm thử ÍT NHẤT 5-7 test khác nhau**

> Sai lầm: 1 test đúng → nộp luôn → DỄ SAI


Dưới đây là nội dung được trích xuất từ các ảnh tiếp theo (Bước 6 tiếp, Bước 7 và Tổng kết):

---


**5 loại test case cần thử:**

① **Test CƠ BẢN** – Test từ đề bài. Phải đúng tuyệt đối.
 **Test BẰNG TAY** – Test đã giải tay ở Bước 2. So sánh với giải tay.
③ **Test BIÊN** – N = 1, N nhỏ nhất, N lớn nhất. Lộ lỗi off-by-one.
④ **Test ĐẶC BIỆT** – Toàn số giống nhau, đã sắp xếp, giảm dần...
⑤ **Test SAI** – Tạo test 'sẽ làm code sai'. Vẫn đúng → tự tin hơn.

> 5 LOẠI test case cần thử

---


**6 test cho bài demo:**

| Test case | Kết quả | Loại test |
| :--- | :---: | :--- |
| N=6, arr={3,1,5,8,2,20} | **3** | Test giải tay |
| N=1, arr={5} | **1** | Test biên (N nhỏ) |
| N=3, arr={1,1,1} | **1** | Toàn số giống nhau |
| N=4, arr={1,2,4,8} | **4** | Dãy nhân đôi - mọi số đặc biệt |
| N=5, arr={10,1,1,1,1} | **1** | Số đầu lớn, sau toàn nhỏ |
| N=4, arr={100,200,1,500} | **3** | Có số nhỏ ở giữa |


**BƯỚC 7**
**Tinh chỉnh và làm sạch code**

**Danh sách kiểm tra:**

- [ ] Xóa COUT DEBUG đã dùng trước đó
- [ ] Đặt TÊN BIẾN rõ ràng (student_count thay vì n)
- [ ] THỤT LỀ nhất quán (4 spaces hoặc 1 tab)
- [ ] COMMENT giải thích 'tại sao', không 'cái gì'
- [ ] Loại bỏ code THỪA (biến không dùng, vòng dư...)
- [ ] KÍCH THƯỚC mảng đủ lớn cho test case lớn nhất
- [ ] KIỂU DỮ LIỆU phù hợp (long long? double?)

> Danh sách kiểm tra LÀM SẠCH code

---


**TỔNG KẾT QUY TRÌNH 7 BƯỚC**

| Bước | Nội dung |
| :---: | :--- |
| **BƯỚC 1** | Đọc đề + đặt lại bằng lời mình |
| **BƯỚC 2** | Giải TAY với ví dụ nhỏ |
| **BƯỚC 3** | Viết PSEUDOCODE chi tiết |
| **BƯỚC 4** | Xác định KHUNG CODE C++ |
| **BƯỚC 5** | Điền LOGIC chính |
| **BƯỚC 6** | Kiểm thử 5-7 TEST CASE |
| **BƯỚC 7** | TINH CHỈNH và làm sạch |

> Áp dụng cho MỌI bài lập trình - không bao giờ tắc