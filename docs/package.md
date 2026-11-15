# Authoring Studio 0.2.0

Gói này là plugin, không chứa bản thảo. `plugin.json` ở gốc gói; `skills/write-book`
chứa skill. `.codex-plugin/plugin.json` là bản tương thích. Cài bằng giao diện nhập
plugin được host hỗ trợ, hoặc dùng marketplace trong kho nguồn GitHub.

Khi dùng skill, chọn thư mục sách nằm ngoài thư mục plugin/cache. `profiles/` chứa
hồ sơ mẫu du lịch cùng quyết định đã thống nhất. Chỉ dùng profile khi đúng dự án.
Không có bộ xuất DOCX/PPTX/PDF hoặc skill trình chiếu trong phiên bản này.

Các helper Python cần môi trường riêng với `requirements.txt`; không cần helper
để đọc hướng dẫn hoặc chỉnh Markdown. Không tự cài thư viện toàn máy.

Kiểm tra nguồn: `python scripts/validate_book.py /path/to/book`.
Khởi tạo hồ sơ khi được yêu cầu: `python scripts/init_book.py /path/to/new-book --title "Tên sách"`.
Lệnh khởi tạo không viết chương và không ghi đè thư mục đã tồn tại.

Đọc LICENSE trước khi phân phối lại. Phiên bản này chưa lựa chọn giấy phép mở.
