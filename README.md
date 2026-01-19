# Coupling and Cohension

![Couping and Cohension](Coupling_Cohension.md)

---

# SOLID

![SOLID](SOLID.md)

---

# Design-Pattern

## 1. Creation Design Pattern

[Singleton](plantuml/CreationalDesignPatterns/Singleton/Singleton.md)

[FactoryMethod](plantuml/CreationalDesignPatterns/FactoryMethod/FactoryMethod.md)

## 2. Structural Design Pattern

[Adapter](plantuml/StructuralDesignPatterns/Adapter/Adapter.md)

## 3. Behavioral Design Pattern

[Strategy](plantuml/BehavioralDesignPatterns/Strategy/Strategy.md)
[Command](plantuml/BehavioralDesignPatterns/Command/Command.md)
[TemplateMethod](plantuml/BehavioralDesignPatterns/TemplateMethod/TemplateMethod.md)
[Observer](plantuml/BehavioralDesignPatterns/Observer/Observer.md)

---

# 📐 Design Patterns – Tóm tắt nhanh

## 1️⃣ Creational Design Pattern

| Pattern            | Mục đích                                       | Dùng khi nào                                      | Ví dụ                    |
| ------------------ | ---------------------------------------------- | ------------------------------------------------- | ------------------------ |
| **Singleton**      | Đảm bảo chỉ có **1 instance** của class        | Cần quản lý tài nguyên dùng chung, config, logger | Logger, Config           |
| **Factory Method** | Tạo object mà **không phụ thuộc class cụ thể** | Muốn mở rộng loại object mà không sửa code cũ     | Shape Factory, UI Button |

---

## 2️⃣ Structural Design Pattern

| Pattern     | Mục đích                                   | Dùng khi nào                  | Ví dụ                      |
| ----------- | ------------------------------------------ | ----------------------------- | -------------------------- |
| **Adapter** | Chuyển đổi **interface không tương thích** | Dùng thư viện cũ / bên thứ ba | Adapter ổ cắm, API Wrapper |

---

## 3️⃣ Behavioral Design Pattern

| Pattern             | Mục đích                                                     | Dùng khi nào                             | Ví dụ                  |
| ------------------- | ------------------------------------------------------------ | ---------------------------------------- | ---------------------- |
| **Strategy**        | Thay đổi thuật toán **runtime**                              | Có nhiều cách xử lý cho cùng 1 hành động | Payment, Sorting       |
| **Command**         | Đóng gói hành động thành object                              | Cần undo/redo, queue command             | Remote, Editor         |
| **Template Method** | Định nghĩa **khung thuật toán**, cho phép override từng bước | Quy trình giống nhau, khác chi tiết      | Game Loop              |
| **Observer**        | Quan hệ **1–n**, tự động notify                              | Event-driven, UI update                  | Listener, Notification |

---

## 🧠 Dấu hiệu nhận biết nhanh

| Câu hỏi                                      | Pattern phù hợp |
| -------------------------------------------- | --------------- |
| Chỉ cần 1 object duy nhất?                   | Singleton       |
| Tạo object nhưng không muốn phụ thuộc class? | Factory Method  |
| Interface không khớp nhau?                   | Adapter         |
| Muốn đổi thuật toán lúc runtime?             | Strategy        |
| Muốn undo / redo hành động?                  | Command         |
| Quy trình cố định, chi tiết thay đổi?        | Template Method |
| 1 object thay đổi → nhiều object cần biết?   | Observer        |
