
Ba loại lỗi và cách xử lý

**LOẠI 1 Lỗi cú pháp (Compile Error)**
- Code KHÔNG chạy được.
- Trình biên dịch CHỈ RA chỗ sai.
- → DỄ NHẤT - đọc thông báo lỗi (chương 2)

**LOẠI 2 Lỗi runtime**
- Code BIÊN DỊCH OK nhưng
- khi chạy → crash giữa chừng.
- → Tìm dòng crash → kiểm tra chia 0, mảng tràn, tràn số

**LOẠI 3 Lỗi logic**
- Code biên dịch OK, chạy OK,
- nhưng KẾT QUẢ SAI.
- → KHÓ NHẤT - dùng PRINT DEBUG (chương 2 tình huống 4)

LOẠI 4 : lỗi chấm điểm 

## 1. Nhóm lỗi phổ biến (WA, TLE, RTE)

- Wrong Answer (WA)
    
    - Nguyên nhân: Thuật toán sai logic, sót trường hợp đặc biệt (Corner cases: n=0, số âm, số cực lớn), hoặc bị tràn số.
    - Cách khắc phục:
        
        - Kiểm tra lại kiểu dữ liệu, đổi `int` sang `long long` (C++) hoặc `Int64` (Pascal).
        - Tự sinh test nhỏ (Corner cases) để chạy thử bằng tay.
        - Viết code trâu (Brute force) để so sánh kết quả với code tối ưu nhằm tìm ra test sai.
        
    
- Time Limit Exceeded (TLE)
    
    - Nguyên nhân: Độ phức tạp thuật toán quá lớn (ví dụ: O(N²) với N = 10⁵), hoặc bị vòng lặp vô hạn.
    - Cách khắc phục:
        
        - Đếm số phép tính: Máy chủ thường chạy được ≈ 10⁸ phép tính trong 1 giây. Dựa vào đó để hạ độ phức tạp thuật toán (ví dụ: từ O(N²) xuống $O(N \log N)$ hoặc O(N)).
        - Thêm dòng tối ưu nhập xuất ở đầu hàm `main` (đối với C++): `cin.tie(NULL); ios_base::sync_with_stdio(false);`.
        - Thay `endl` bằng `'\n'` để tránh làm trống bộ đệm liên tục.
        
    
- Runtime Error (RTE)
    
    - Nguyên nhân: Truy cập mảng ngoài phạm vi, chia cho số 0, hoặc đệ quy quá sâu gây tràn ngăn xếp (Stack Overflow).
    - Cách khắc phục:
        
        - Tăng kích thước mảng lớn hơn giới hạn đề bài ít nhất 5 đơn vị (ví dụ: N = 10⁵ thì khai báo `int a[100005]`).
        - Khai báo mảng lớn ở vùng biến toàn cục (Global), không khai báo bên trong hàm `main`.
        - Kiểm tra điều kiện trước phép chia: `if (b != 0) c = a / b;`.
        - Khử đệ quy bằng cách chuyển sang thuật toán lặp (Quy hoạch động trạng thái/vòng lặp) nếu cấu trúc đệ quy quá sâu.
        
    

## 2. Nhóm lỗi tài nguyên (MLE, OLE, CE)

- Memory Limit Exceeded (MLE)
    
    - Nguyên nhân: Khai báo mảng quá lớn hoặc lưu trữ quá nhiều trạng thái không cần thiết.
    - Cách khắc phục:
        
        - Tính toán dung lượng: Một mảng `int a[10^7]` tốn khoảng 10⁷ × 4 bytes ≈ 40 MB. Nếu đề cho 256MB, không được khai báo vượt quá 6 × 10⁷ phần tử `int`.
        - Tối ưu mảng bằng cách dùng kỹ thuật "cuộn mảng" (Rolling array) trong quy hoạch động để tái sử dụng bộ nhớ.
        
    
- Output Limit Exceeded (OLE)
    
    - Nguyên nhân: Code in ra lượng dữ liệu khổng lồ, thường do đặt lệnh `print`/`cout` nhầm bên trong một vòng lặp vô hạn.
    - Cách khắc phục: Kiểm tra lại các điều kiện dừng của vòng lặp `while` hoặc `for`. Đảm bảo không in thừa các dòng thông báo gỡ lỗi (debug log) khi nộp bài.
    
- Compile Error (CE)
    
    - Nguyên nhân: Lỗi cú pháp, thiếu thư viện, hoặc dùng hàm thuộc phiên bản ngôn ngữ mới mà hệ thống chấm không hỗ trợ.
    - Cách khắc phục:
        
        - Đọc kỹ dòng thông báo lỗi (Line number và mã lỗi) do hệ thống trả về.
        - Đảm bảo chọn đúng phiên bản cấu hình trình biên dịch khi nộp bài (ví dụ: chọn C++17 hoặc C++20 thay vì C++11 nếu có dùng các hàm mới).
        - Sử dụng thư viện tổng hợp `#include <bits/stdc++.h>` (đối với C++) để tránh thiếu thư viện.
        
    

## 3. Nhóm lỗi đặc biệt (PE, ILE)

- Presentation Error (PE)
    
    - Nguyên nhân: Thuật toán đúng hoàn toàn nhưng in ra thừa/thiếu dấu cách hoặc dấu xuống dòng so với định dạng mẫu.
    - Cách khắc phục: Đọc kỹ yêu cầu: "in trên một dòng cách nhau bởi dấu cách" hay "mỗi kết quả trên một dòng". Kiểm tra xem có bị in thừa dấu cách ở cuối dòng hay không.
    
- Idleness Limit Exceeded (ILE)
    
    - Nguyên nhân: Thường gặp trong các bài toán tương tác (Interactive), do chương trình đợi dữ liệu từ hệ thống chấm nhưng không giải phóng bộ đệm để gửi câu hỏi đi.
    - Cách khắc phục: Thêm lệnh xóa bộ đệm ngay sau khi in lệnh hỏi: Dùng `cout << endl;` (C++), `fflush(stdout);` (C/C++), hoặc `sys.stdout.flush()` (Python).
    



**Loại 3 (logic) KHÓ NHẤT vì KHÔNG có thông báo lỗi gì cả**

> 3 loại lỗi C++ - mỗi loại có cách xử lý khác

---
 
 
 
 
## Quy trình DEBUG 5 bước
1. **Xác định TRIỆU CHỨNG cụ thể**
   *Code làm gì? Nên làm gì? Khác nhau ở đâu?*
2. **Tạo TEST CASE nhỏ nhất tái hiện bug**
   *100 phần tử → 10 → 5 → 3. Càng nhỏ càng dễ*
3. **Hình thành GIẢ THUYẾT về nguyên nhân**
   *ĐOÁN trước khi sửa: 'có thể do off-by-one'*
4. **KIỂM CHỨNG giả thuyết bằng print debug**
   *Thêm cout → chạy → xem giả thuyết đúng không*
5. **Sửa, kiểm tra, và RÚT KINH NGHIỆM**
   *Viết vào sổ tay debug → kinh nghiệm tích lũy*

**BƯỚC 5 quan trọng nhất - tích lũy KINH NGHIỆM cho lần sau!**

> Sau 50-100 bug → bạn nhìn triệu chứng là đoán được nguyên nhân

---

## 10 Dấu hiệu nhanh
*Bảng nhận diện nhanh - học thuộc tiết kiệm hàng GIỜ debug*

| **TRIỆU CHỨNG** | **NGUYÊN NHÂN THƯỜNG GẶP** |
| :--- | :--- |
| Kết quả lệch 1 đơn vị | Off-by-one: < ↔ <=, i=1 thay 0 |
| Kết quả số ngẫu nhiên | Quên khởi tạo (int sum; thiếu = 0) |
| Kết quả âm khi đáng dương | Tràn số: dùng int khi cần long long |
| Treo, không in gì | Vòng lặp vô hạn - thiếu cập nhật biến |
| Crash khi chạy | Truy cập mảng ngoài, chia cho 0 |
| Đúng test nhỏ, sai test lớn | Tràn số / mảng quá nhỏ / quá chậm |
| Đúng test đầu, sai test sau | Quên RESET biến giữa các test |
| Chỉ sai vài phần tử | Lỗi ở PHẦN TỬ BIÊN (đầu/cuối) |
| Output sai định dạng | Thiếu endl, dư ký tự, không xuống dòng |
| Kết quả khác mỗi lần chạy | Biến chưa khởi tạo - bug nghiêm trọng |

> Triệu chứng → Nguyên nhân thường gặp