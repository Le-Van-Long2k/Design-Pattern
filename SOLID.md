# SOLID

| Principle | Tên đầy đủ                      | Nội dung                                                                                                                                     |
| --------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **SRP**   | Single Responsibility Principle | 👉 Mỗi lớp chỉ nên có một lý do để thay đổi                                                                                                  |
| **OCP**   | Open / Closed Principle         | 👉 Open cho việc mở rộng, Close cho việc sửa đổi<br>👉 Nếu code tuân theo OCP thì có thể thêm chức năng mới mà không sửa code cũ             |
| **LSP**   | Liskov Substitution Principle   | 👉 Các lớp dẫn xuất phải tuân thủ hành vi và các hợp đồng được định nghĩa bởi lớp cơ sở                                                      |
| **ISP**   | Interface Segregation Principle | 👉 Không ép class phải implement những method nó không cần, client không nên bị buộc phải phụ thuộc vào các giao diện mà chúng không sử dụng |
| **DIP**   | Dependency Inversion Principle  | 👉 Các mô-đun cấp cao không nên phụ thuộc vào các mô-đun cấp thấp; cả hai đều nên phụ thuộc vào các lớp trừu tượng                           |
