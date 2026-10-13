## 🌐 REST API là gì?

- **REST** (Representational State Transfer) là một phong cách kiến trúc để thiết kế hệ thống phân tán.
- **REST API** là giao diện cho phép ứng dụng (web, mobile, desktop) giao tiếp với server thông qua các phương thức **HTTP**.

---

## ⚙️ Nguyên tắc chính của REST

- **Stateless (phi trạng thái)**: Mỗi request phải chứa đầy đủ thông tin, server không lưu trạng thái của client.
- **Client-Server**: Phân tách rõ ràng giữa phía client (giao diện) và server (xử lý dữ liệu).
- **Uniform Interface**: Giao tiếp thống nhất, tài nguyên được định danh bằng URL.
- **Cacheable**: Dữ liệu trả về có thể được cache để tăng hiệu năng.
- **Layered System**: Có thể tổ chức thành nhiều lớp (proxy, load balancer…).

---

## 📌 Các phương thức HTTP thường dùng

|Phương thức|Chức năng|Ví dụ URL|
|---|---|---|
|**GET**|Lấy dữ liệu|`/users` → lấy danh sách user|
|**POST**|Tạo mới dữ liệu|`/users` → thêm user mới|
|**PUT**|Cập nhật toàn bộ dữ liệu|`/users/123` → cập nhật user|
|**PATCH**|Cập nhật một phần dữ liệu|`/users/123` → đổi email|
|**DELETE**|Xóa dữ liệu|`/users/123` → xóa user|

---

## 📖 Ví dụ REST API cho cửa hàng sách

- `GET /books` → lấy danh sách sách.
- `GET /books/5` → lấy thông tin sách có ID = 5.
- `POST /books` → thêm sách mới.
- `PUT /books/5` → cập nhật sách ID = 5.
- `DELETE /books/5` → xóa sách ID = 5.


Để bạn dễ hình dung cách **REST API hoạt động**, mình sẽ minh họa bằng một ví dụ trực quan:

---

## 📖 Tình huống minh họa

Giả sử bạn có một ứng dụng **Quản lý Sách**. Người dùng muốn xem, thêm, sửa, hoặc xóa sách trong hệ thống. REST API sẽ là cầu nối giữa **client (ứng dụng)** và **server (cơ sở dữ liệu)**.

---

## 🔄 Quy trình hoạt động

1. **Client gửi yêu cầu (Request)**
    - Ví dụ: Người dùng mở app và muốn xem danh sách sách.
    - App sẽ gửi một HTTP request:
        
        ```
        GET /books
        ```
        
2. **Server xử lý yêu cầu**
    - Server nhận request, truy vấn cơ sở dữ liệu để lấy danh sách sách.
3. **Server trả về phản hồi (Response)**
    - Server gửi dữ liệu về cho client dưới dạng JSON:
        
        ```json
        [
          { "id": 1, "title": "Lập trình Python", "author": "Nguyễn Văn A" },
          { "id": 2, "title": "Thuật toán cơ bản", "author": "Trần Thị B" }
        ]
        ```
        
4. **Client hiển thị dữ liệu**
    - App sẽ hiển thị danh sách sách cho người dùng.

---

## 📌 Ví dụ các thao tác khác

- **Thêm sách mới**
    
    ```
    POST /books
    Body: { "title": "Machine Learning", "author": "Lê Văn C" }
    ```
    
    → Server thêm sách vào DB và trả về thông tin sách vừa tạo.
    
- **Cập nhật sách**
    
    ```
    PUT /books/2
    Body: { "title": "Thuật toán nâng cao", "author": "Trần Thị B" }
    ```
    
    → Server cập nhật sách có ID = 2.
    
- **Xóa sách**
    
    ```
    DELETE /books/1
    ```
    
    → Server xóa sách có ID = 1.
    

---

## 🖼️ Minh họa bằng sơ đồ

```
[Client (App)]  --->  [REST API]  --->  [Server/Database]
     |                     |                   |
     |--- Request -------->|                   |
     |<-- Response --------|                   |
```

---

👉 Bạn có muốn mình **viết code mẫu** (ví dụ bằng **Python Flask** hoặc **Node.js Express**) để minh họa chi tiết hơn cách REST API hoạt động không?

Trong ví dụ bạn đưa ra:

```
POST /books
Body: { "title": "Machine Learning", "author": "Lê Văn C" }
```

👉 Khi bạn **thêm sách mới** bằng REST API, **ID** thường không phải do client (người gửi request) cung cấp, mà sẽ được **server tự động tạo ra**.

---

## 📌 Cách tạo ID trong REST API

- **Tự động tăng (Auto Increment)**: Nếu dùng cơ sở dữ liệu quan hệ (MySQL, PostgreSQL…), mỗi bản ghi mới sẽ có ID tăng dần (ví dụ: 1, 2, 3, …).
- **UUID (Universally Unique Identifier)**: Một chuỗi ngẫu nhiên duy nhất, thường dùng trong hệ thống phân tán (ví dụ: `"550e8400-e29b-41d4-a716-446655440000"`).
- **Custom ID**: Một số hệ thống có thể sinh ID theo quy tắc riêng (ví dụ: `BOOK-001`, `BOOK-002`).

---

## 🛠️ Ví dụ phản hồi từ server

Sau khi thêm sách mới, server có thể trả về JSON như sau:

```json
{
  "id": 3,
  "title": "Machine Learning",
  "author": "Lê Văn C"
}
```

hoặc nếu dùng UUID:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Machine Learning",
  "author": "Lê Văn C"
}
```

---

✅ Tóm lại: **ID sẽ do server sinh ra** khi bạn gọi `POST /books`. Client chỉ cần gửi thông tin sách (title, author), còn ID sẽ được trả về trong response.

Bạn có muốn mình minh họa bằng **code mẫu Flask (Python)** để thấy rõ cách server tự động gán ID khi thêm sách không?

Đoạn văn **“gửi yêu cầu HTTP”** nếu đặt trong ngữ cảnh của trang nói về **REST API** hoặc cách ứng dụng giao tiếp với server, thì ý nghĩa chủ yếu là:

---

## 📌 Giải thích theo nội dung xung quanh

- **HTTP request (yêu cầu HTTP)** là hành động mà **client (ứng dụng, trình duyệt, app di động)** gửi đến **server** để yêu cầu một tài nguyên hoặc thực hiện một thao tác.
- Trong REST API, mỗi yêu cầu HTTP thường gồm:
    - **Phương thức (Method)**: như `GET`, `POST`, `PUT`, `DELETE` để xác định loại thao tác.
    - **URL (Endpoint)**: địa chỉ tài nguyên, ví dụ `/books/5`.
    - **Header**: thông tin bổ sung (ví dụ: định dạng dữ liệu, token xác thực).
    - **Body**: dữ liệu gửi kèm (thường dùng với `POST` hoặc `PUT`).

---

## 🔄 Vai trò trong ngữ cảnh REST API

- Khi người dùng muốn **lấy dữ liệu** (ví dụ danh sách sách), ứng dụng sẽ **gửi yêu cầu HTTP GET** đến server.
- Khi muốn **thêm dữ liệu mới**, ứng dụng sẽ **gửi yêu cầu HTTP POST** kèm theo nội dung trong body.
- Server nhận yêu cầu, xử lý, rồi **trả về phản hồi (HTTP response)** cho client.

---

## 🖼️ Minh họa ngắn gọn

```
Client (App) ---> gửi yêu cầu HTTP ---> Server (API)
```

Ví dụ cụ thể:

```
POST /books
Body: { "title": "Machine Learning", "author": "Lê Văn C" }
```

→ Đây chính là một **yêu cầu HTTP** để thêm sách mới vào hệ thống.

---

👉 Như vậy, cụm “gửi yêu cầu HTTP” trong đoạn văn chủ yếu ám chỉ **bước đầu tiên trong quá trình giao tiếp giữa client và server qua REST API**, nơi client gửi thông tin đến server để yêu cầu một hành động cụ thể.

Bạn có muốn mình minh họa thêm bằng **sơ đồ tuần tự (sequence diagram)** để thấy rõ luồng “gửi yêu cầu HTTP → xử lý → phản hồi” không?