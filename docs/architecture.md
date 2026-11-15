# Kiến trúc phiên bản 0.2.0

## Hai dự án độc lập

Kho plugin chứa hướng dẫn, mẫu, schema và công cụ. Kho sách chứa các tệp do người
dùng biên soạn, ảnh và nguồn. Không tạo sách trong thư mục plugin hoặc cache.
Các đường dẫn đều tương đối, không gắn với tên tài khoản hoặc máy tác giả.

`skills/write-book/SKILL.md` điều phối các chế độ theo yêu cầu. Hướng dẫn được đọc
theo nhu cầu, không tải tất cả tài liệu tham chiếu trong mọi lượt làm việc.
`profiles/rural-tourism-vi.yaml` là cấu hình tùy chọn; `rural-tourism-decisions.md`
ghi cả yêu cầu, đề xuất còn mở và quyết định đã thay thế.

## Bản nguồn sách

`book.yaml` là thông tin cuốn sách và layout. `state.yaml` theo dõi việc đang làm;
`decisions.md` lưu quyết định; `outline.md` lưu đề cương; `terms.yaml` thống nhất thuật
ngữ; `evidence.yaml` liên kết nhận định với nguồn; `references.yaml` là danh mục CSL.
`chapters/` giữ văn bản và caption. `image/` giữ ảnh; các index giữ mapping và bố trí.

Caption chỉ có một bản trong Markdown. ID semantic không chứa số chương bắt buộc;
đánh số hiển thị sẽ do bộ trình bày tương lai xử lý. Vị trí ảnh trong Markdown và
index chỉ là hợp đồng nguồn, không tự làm một trình đọc Markdown thông thường
dàn ảnh cạnh chữ.

## Phiên bản

- `plugin.json` và bản tương thích có cùng plugin version.
- Hồ sơ sách có `schema_version: 1` và version plugin trong `state.yaml`.
- Phiên bản bản thảo do tác giả quản lý độc lập bằng commit/tag hoặc hồ sơ sách.
- 0.1.0 không chuyển đổi schema. Báo lỗi khi gặp schema khác, không tự sửa.

## Công cụ

`init_book.py` khởi tạo hồ sơ, không ghi đè, hỗ trợ dry-run, không viết chương.
`validate_book.py` chỉ đọc, dùng schema và kiểm tra liên kết. Cảnh báo còn thiếu
tư liệu trở thành lỗi khi chạy `--strict`. Không kiểm chứng sự thật, quyền ảnh,
độ phân giải hoặc chất lượng bố cục tự động.
`validate_repo.py` kiểm tra hợp đồng phát hành; `build_release.py` tạo ZIP và SHA256.

## Mở rộng sau này

0.2.0 giữ nguyên cấu trúc Codex. `scripts/build_standalone.py` sinh
`skills/write-book/` tự chứa từ nguồn plugin; tài nguyên được đặt dưới resources,
đường dẫn ở entrypoint được điều chỉnh khi sinh, không sửa nguồn Codex. Validator
phát hiện bản sinh lệch nguồn. Build release tạo cả ZIP plugin và ZIP skill độc lập.
Không duy trì ba bản quy tắc riêng; xem [đa nền tảng](platforms.md).

Skill trình chiếu có thể đọc mục, hình và nguồn theo ID để biên tập slide, nhưng
phải có mục đích, cấu trúc và quy tắc riêng. Không có skill rỗng trong bản 0.1.0.
Quarto/Pandoc là ứng viên dựng bản xem trước và xuất bản, chưa là phụ thuộc runtime.
Khi thêm renderer phải thử caption, ảnh cạnh chữ, toàn chiều rộng, bảng tiếp trang,
font Times New Roman và các khoảng cách đã chốt trên từng định dạng được hỗ trợ.
