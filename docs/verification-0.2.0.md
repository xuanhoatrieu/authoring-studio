# Kiểm tra 0.2.0 — 15/11/2026

- 25 kiểm thử Python đạt trên máy phát triển, gồm các ca nguồn hiện có và gói độc lập.
- Validator kho với tag v0.2.0 đạt; hai entrypoint skill qua quick_validate.
- Hai ZIP xây dựng hai lần cho checksum trùng; gói Codex chứa nguyên byte tệp nguồn.
- Gói độc lập giải nén ngoài kho: liên kết Markdown nằm trong gói và tồn tại;
  helper khởi tạo/kiểm tra cả hồ sơ generic và rural-tourism-vi chạy thành công.
- Chặn tạo bản thảo bên trong thư mục cài skill; bản sinh thiếu tài nguyên bị phát hiện.
- Không chạy tác vụ trong Antigravity/Hermes Desktop vì môi trường chưa có ứng dụng.
  Chưa coi các ca đánh giá hành vi model là đạt; xem behavioral-tests.md.
- CI chạy cùng bộ kiểm tra trên Linux, macOS, Windows trước khi tạo GitHub Release.
  Kết quả thực tế được ghi ở workflow của tag, không suy ra từ kiểm thử máy phát triển.

Giữ nguyên schema 1, không thực hiện migration hoặc viết lại sách.
