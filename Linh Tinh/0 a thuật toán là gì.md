- **Thuật toán là gì?** (0:13 - 1:07): Thuật toán được định nghĩa là một quy trình hoặc hướng dẫn từng bước cụ thể để giải quyết một vấn đề. 
- Để một chuỗi các bước được coi là thuật toán, nó phải thỏa mãn 3 yếu tố cốt lõi:

1. **Rõ ràng (Đơn nghĩa):** Mỗi bước phải chuẩn xác, không gây hiểu lầm.
    
2. **Khả thi:** Có thể thực hiện được bằng các nguồn lực sẵn có.
    
3. **Hữu hạn:** Phải có điểm dừng, không thể chạy mãi mãi.

## Ví dụ đời thường: Luộc một quả trứng lòng đào

Bạn muốn có một quả trứng lòng đào hoàn hảo (Output) từ một quả trứng sống (Input). Thuật toán của bạn sẽ là:

- **Bước 1:** Đun sôi nước max nhiệt độ nếu bếp điên , max lửa nếu bếp gas .
    
- **Bước 2:** Khi nước sôi, hạ nhỏ lửa và nhẹ nhàng thả trứng vào.
    
- **Bước 3:** Bật đồng hồ bấm giờ đúng **6 phút**.
    
- **Bước 4:** Trong lúc đợi, chuẩn bị một bát nước đá hoặc nếu không có đá thì cho vào chậu nước 

    
- **Bước 5:** Hết 6 phút, vớt ngay trứng ra và thả vào bát nước đá trong 3 phút.
    
- **Bước 6:** Bóc vỏ. Kết thúc.
    

> Nếu bạn thay đổi Bước 3 thành _"Đợi một lúc"_ thay vì _"6 phút"_, quy trình này mất đi tính **rõ ràng** và không còn là một thuật toán tốt, vì "một lúc" với mỗi người là khác nhau.

## Ví dụ trong Khoa học dữ liệu / Lập trình: Thuật toán Tìm kiếm Nhị phân (Binary Search)

Hãy tưởng tượng bạn có một mảng số đã được sắp xếp từ nhỏ đến lớn: `[2, 5, 8, 12, 16, 23, 38, 56, 72]` và bạn cần tìm xem số **23** nằm ở đâu.

Thay vì tìm tuyến tính (đếm từng số từ đầu đến cuối rất mất thời gian), thuật toán Tìm kiếm Nhị phân sẽ "chặt đôi" mảng để tìm:

- **Bước 1:** Lấy phần tử ở chính giữa mảng (số **16**).
    
- **Bước 2:** So sánh: Vì $23 > 16$, thuật toán biết ngay số 23 (nếu có) chỉ có thể nằm ở nửa bên phải. Loại bỏ hoàn toàn nửa bên trái `[2, 5, 8, 12]`.
    
- **Bước 3:** Lặp lại với nửa còn lại `[23, 38, 56, 72]`. Lấy số ở giữa (lúc này là **38** hoặc **56**, giả sử chọn **38**).
    
- **Bước 4:** So sánh: Vì $23 < 38$, loại bỏ nửa bên phải `[38, 56, 72]`.
    
- **Bước 5:** Nửa còn lại duy nhất là số **23**. Tìm thấy vị trí! Kết thúc.




- **Tại sao cần phân tích thuật toán?** (1:14 - 2:47): Để giải quyết cùng một vấn đề, có thể có nhiều phương pháp (thuật toán) khác nhau. Việc phân tích giúp chúng ta chọn ra giải pháp **tối ưu nhất** về mặt thời gian và hiệu quả, tương tự như việc so sánh các phương tiện di chuyển từ bắc vào nam , có nhiều lựa chọn (...... liệt kê ra ) thì cta chọn đường bay vì .... 
- 
- 



## 1. Tại sao cần phân tích thuật toán?

Hãy tưởng tượng bạn cần xử lý một tập dữ liệu gồm $100$ bản ghi, một thuật toán tồi và một thuật toán tối ưu có thể chỉ chênh lệch nhau vài mili giây – mắt người không thể nhận ra. Nhưng nếu dữ liệu tăng lên $10.000.000$ bản ghi (thực tế trong kinh doanh và Big Data), thuật toán tốt chạy nhanh , tồi thì chạy chậm , ví dụ bằng các phương tiện di chuyển 

Phân tích thuật toán giúp chúng ta:

- **Dự đoán hiệu năng trước khi cài đặt:** Bạn không cần phải tốn công viết hàng nghìn dòng code hay thuê máy chủ đắt tiền để chạy thử mới biết nó nhanh hay chậm. Phân tích toán học giúp bạn biết trước xu hướng vận hành của nó.
    
- **Đánh giá khả năng mở rộng (Scalability):** Giúp trả lời câu hỏi: _"Khi quy mô dữ liệu (Input) tăng lên gấp $10$ hoặc gấp $100$ lần, tài nguyên máy tính cần thêm sẽ tăng theo cấp số cộng, cấp số nhân, hay lũy thừa?"_
    
- **Lựa chọn và đánh đổi (Trade-off):** Không có thuật toán nào hoàn hảo cho mọi bài toán. Có những thuật toán chạy cực nhanh nhưng ngốn rất nhiều RAM, ngược lại có thuật toán tiết kiệm bộ nhớ nhưng lại xử lý lâu. Phân tích giúp bạn chọn đúng "vũ khí" phù hợp với tài nguyên hiện có.
    
[slide 6 ]
## 2. Các yếu tố cốt lõi khi phân tích thuật toán

Để đánh giá một thuật toán, người ta không dùng thước đo bằng "giây" hay "megabyte" tuyệt đối (vì chúng thay đổi tùy thuộc vào cấu hình máy tính mạnh hay yếu). Thay vào đó, người ta phân tích dựa trên sự phụ thuộc của thuật toán vào **kích thước đầu vào ($n$)**.
> đọc trên vnoi 
Hai yếu tố quan trọng nhất cần phân tích là:

### Đánh giá Độ phức tạp Thời gian (Time Complexity)

Đây là yếu tố đo lường **số lượng phép toán cơ bản** mà thuật toán phải thực hiện dưới dạng một hàm số của $n$.

Để chuẩn hóa, người ta sử dụng **Ký pháp Big-O ($O$)** để biểu diễn biên trên (trường hợp xấu nhất) của thời gian chạy:

- $O(1)$ - Độ phức tạp hằng số: Thời gian không đổi dù dữ liệu lớn bao nhiêu (Ví dụ: Truy cập một phần tử trong mảng qua chỉ số).
    
- $O(\log n)$ - Độ phức tạp lôgarit: Cực kỳ tối ưu, quy mô dữ liệu tăng gấp đôi thì số bước chỉ tăng thêm $1$ (Ví dụ: Tìm kiếm nhị phân).
    
- $O(n)$ - Độ phức tạp tuyến tính: Thời gian tăng tỷ lệ thuận với dữ liệu (Ví dụ: Tìm kiếm tuần tự, duyệt qua danh sách).
    
- $O(n \log n)$ - Thường gặp ở các thuật toán sắp xếp tối ưu như Merge Sort, Quick Sort.
    
- $O(n^2)$ - Độ phức tạp bình phương: Thường xuất hiện khi có $2$ vòng lặp lồng nhau. Khi $n$ lớn, hệ thống rất dễ bị nghẽn (Ví dụ: Sắp xếp nổi bọt - Bubble Sort).
    

### Đánh giá Độ phức tạp Không gian (Space Complexity)

Yếu tố này đo lường **lượng bộ nhớ tối đa** (RAM) mà thuật toán cần sử dụng trong quá trình thực thi, cũng dưới dạng một hàm của $n$.

- Thuật toán có cấu trúc dữ liệu phụ trợ càng ít tạo ra các bản sao dữ liệu trong bộ nhớ thì độ phức tạp không gian càng thấp (lý tưởng là $O(1)$).
    
- Nhiều thuật toán đệ quy hoặc thuật toán phân tách dữ liệu (như Merge Sort) đòi hỏi không gian bộ nhớ lớn ($O(n)$) để lưu trữ các trạng thái tạm thời.
    



