- Là công cụ biểu thị **chặn trên (trường hợp tệ nhất)** về độ phức tạp của một thuật toán . Nó ước tính hiệu năng khi kích thước đầu vào ($N$) tiến dần đến vô cùng .
- Khi tính Big-O, người ta thường bỏ qua hằng số ($C$) và chỉ giữ lại thành phần có số mũ cao nhất (lớn nhất) trong phương trình hiệu năng vì Big O tập trung vào trường hợp tệ nhất  của thuật toán khi dữ liệu tiến đến vô cùng.
### 1. Nhóm thuật toán tối ưu (Nhanh)

- **O(1) - Hằng số (2:10):** Thời gian thực thi không phụ thuộc vào kích thước dữ liệu đầu vào. Ví dụ: Truy cập trực tiếp vào một phần tử trong mảng bằng _index_.
- **O(log N) - Logarit (3:32):** Thường thấy trong thuật toán **Binary Search** (Tìm kiếm nhị phân). Mỗi bước thuật toán cắt giảm một nửa không gian tìm kiếm, giúp xử lý dữ liệu cực nhanh ngay cả khi  lên tới hàng triệu.

### 2. Nhóm thuật toán trung bình

- **O(N) - Tuyến tính (6:52):** Thời gian tăng tỉ lệ thuận với . Ví dụ: Duyệt qua từng phần tử trong một mảng không sắp xếp.
- **O(N log N) (8:16):** Xuất hiện trong các thuật toán sắp xếp tối ưu như _Merge Sort_ hoặc _Quick Sort_. Đây là ngưỡng chấp nhận được cho hầu hết các bài toán lớn.

### 3. Nhóm thuật toán chậm (Cần tránh nếu có thể)

- **O(N²) - Bình phương (9:40):** Thường do sử dụng các vòng lặp lồng nhau (_nested loops_). Khi  tăng gấp đôi, thời gian chạy tăng gấp bốn.
- **O(2^N) - Mũ (15:13):** Tăng trưởng cực nhanh. Ví dụ: Giải bài toán _Fibonacci_ bằng phương pháp đệ quy thuần túy, nơi mỗi bước gọi lại tạo ra hai nhánh gọi mới.
- **O(N!) - Giai thừa (17:00):** Cấp độ chậm nhất, thường gặp trong các bài toán _backtracking_ (quay lui) phức tạp như _Traveling Salesman Problem_. Bạn nên tìm cách tối ưu hóa nếu thuật toán của mình rơi vào nhóm này.