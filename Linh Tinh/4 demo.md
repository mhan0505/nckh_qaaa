# p1 : thuật toán là j :
- **Thuật toán là gì?** là một chuỗi các bước hướng dẫn cụ thể để giải quyết một vấn đề.
-  Để một chuỗi các bước được coi là thuật toán, nó phải thỏa mãn 3 yếu tố cốt lõi:

1. **Rõ ràng (Đơn nghĩa):** Mỗi bước phải chuẩn xác, không gây hiểu lầm.
    
2. **Khả thi:** Có thể thực hiện được bằng các nguồn lực sẵn có.
    
3. **Hữu hạn:** Phải có điểm dừng, không thể chạy mãi mãi.
- **Tại sao cần phân tích thuật toán?** mỗi vấn đề có thể có nhiều giải pháp. Việc phân tích giúp lập trình viên tìm ra thuật toán **tối ưu nhất** về hiệu năng và tài nguyên.
- **yếu tố khi phân tích thuật toán** : độ phức tạp : thời gian và k gian 

# p2 : BigO Notation và ví dụ
- Là công cụ biểu thị **chặn trên (trường hợp tệ nhất)** về độ phức tạp của một thuật toán . Nó ước tính hiệu năng khi kích thước đầu vào ($N$) tiến dần đến vô cùng .
- Khi tính Big-O, người ta thường bỏ qua hằng số ($C$) và chỉ giữ lại thành phần có số mũ cao nhất (lớn nhất) trong phương trình hiệu năng
	-  Độ phức tạp hằng số — $O(1)$
	- **O(log N)** Độ phức tạp logarit. Thường thấy trong _Binary Search
	- **O(N)** Độ phức tạp tuyến tính. Thời gian chạy tỉ lệ thuận với kích thước đầu vào
	- **O(N log N)**
	- **O(N²)**
	- **O(2^N)**
	- **O(N!)**
 
  # p3 : 1 số code nền :
 - 1. Căn bậc hai
 - 2.  tổng chữ số: "10 ≡ 1 (mod 9)"
 - 3. Sàng Eratosthenes và tư duy "harmonic"
 - 4. Digit DP: Đếm số theo tính chất của chữ số
 - 5. Tổng tiền tố: Biến cả một đoạn thành một điểm
 - 6. Mảng hiệu: Cập nhật một đoạn bằng hai phép gán
 - 7. Hai con trỏ và cửa sổ trượt: Tính đơn điệu
 -  8. Tìm kiếm nhị phân trên đáp án: Biến bài toán "Tối ưu" thành bài toán "Kiểm tra"
 