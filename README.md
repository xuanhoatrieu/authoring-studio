# Authoring Studio

**Phiên bản 0.1.0** — Plugin biên soạn sách từ bản nguồn, có skill `write-book`.

Plugin lưu quy trình nghiên cứu, lập đề cương, biên soạn, minh họa và biên tập.
Nội dung sách được lưu trong dự án riêng bằng Markdown và YAML. Phiên bản này
không viết sẵn chương sách, không có skill trình chiếu, không có bộ xuất DOCX/PPTX/PDF.

## Bắt đầu

1. Mở thư mục kho này thành một dự án riêng để chỉnh sửa plugin.
2. Cài plugin qua marketplace của kho hoặc gói phát hành theo hướng dẫn
   [cài đặt và cập nhật](docs/install-update.md).
3. Mở một thư mục khác cho bản thảo. Yêu cầu skill đọc các quy ước trước khi làm việc.

Ví dụ yêu cầu:

> Dùng write-book để thảo luận phương án biên soạn sách. Chưa viết nội dung.

> Dùng write-book để tiếp tục dự án ở thư mục tôi chọn. Đọc hồ sơ và các quyết định
> đã thống nhất trước khi chỉnh sửa mục được yêu cầu.

> Kiểm tra liên kết ảnh và nguồn trong bản thảo. Không sửa nội dung hoặc xuất tệp.

## Nội dung đã có

- Skill ngắn, chia hướng dẫn theo công việc; dùng được với công cụ sẵn có của host.
- Hồ sơ mẫu cho sách du lịch nông nghiệp, nông thôn và toàn bộ quy ước đã thống nhất.
- Markdown cho văn bản; YAML cho hồ sơ, ảnh, bảng, nguồn, thuật ngữ và trạng thái.
- Công cụ khởi tạo không ghi đè, không tạo chương; kiểm tra nguồn chỉ đọc.
- Kiểm tra ảnh, caption, mã liên kết, nguồn trích dẫn, đường dẫn và phiên bản schema.
- Marketplace Git, khai báo plugin portable và khai báo tương thích Codex.
- Kiểm thử, đóng gói ZIP có SHA256, cấu hình kiểm tra và phát hành GitHub Actions.

## Phạm vi và giới hạn

0.1.0 chưa có trình dựng bố cục, đọc chất lượng ảnh tự động, chuyển đổi schema,
tự đồng bộ bản thảo hay tự cập nhật plugin. Cấu hình A4 biểu thị quy cách cần đạt;
không phải chứng nhận một bản in đã đạt. Kiểm tra cấu trúc không thay thế kiểm chứng
nguồn, quyền sử dụng ảnh, nhận xét biên tập hoặc đọc thử với độc giả.

Tìm nguồn và tạo ảnh dùng các công cụ có sẵn trong tài khoản đang làm việc. Skill
không tự cấp quyền hay mang theo các dịch vụ này sang tài khoản khác.

## Quy ước bảng đã chốt

Tên bảng và mọi ô ở hàng tiêu đề đầu tiên căn giữa. Số liệu trong thân bảng căn
giữa; chữ căn trái và giữa theo chiều dọc. Trong bảng giãn dòng đơn và giãn đoạn
trước/sau 0 pt. Quy tắc này không căn giữa tiêu đề chương hoặc các mục.

Hồ sơ đầy đủ: [quyết định của sách du lịch](plugins/authoring-studio/profiles/rural-tourism-decisions.md).
Các lựa chọn chưa chốt được giữ là pending, không biến thành phê duyệt của tác giả.

## Kiểm tra và đóng gói

Cần Python 3.10 trở lên. Hướng dẫn không yêu cầu Python khi chỉ đọc hoặc dùng skill.

```sh
python -m venv .venv
```

Kích hoạt môi trường theo hệ điều hành:

```sh
# macOS / Linux
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Sau đó:

```sh
python -m pip install -r plugins/authoring-studio/requirements.txt
python scripts/validate_repo.py --tag v0.1.0
python -m unittest discover -s tests -v
python scripts/build_release.py
```

Gói nằm trong `dist/`, không được commit vào Git. CI tạo lại gói cho mỗi tag.

## Khởi tạo bản thảo khi được yêu cầu

Thay đường dẫn ví dụ bằng thư mục mới nằm ngoài kho plugin:

```sh
python plugins/authoring-studio/scripts/init_book.py /path/to/new-book --title "Tên sách" --dry-run
python plugins/authoring-studio/scripts/init_book.py /path/to/new-book --title "Tên sách"
python plugins/authoring-studio/scripts/validate_book.py /path/to/new-book
```

Thêm `--profile rural-tourism-vi` để dùng hồ sơ du lịch đã thống nhất. Công cụ chỉ
tạo hồ sơ, thư mục ảnh và thư mục chương rỗng. Không cần chạy để sử dụng plugin.

## GitHub và các phiên bản

[Hướng dẫn phát hành](docs/github-release.md) mô tả tạo repository, push, tag,
Release, cách kiểm tra phiên bản và quay lại bản trước. [Kiến trúc](docs/architecture.md)
giải thích phần dùng chung và phần của từng cuốn sách.

Plugin và bản thảo có phiên bản riêng. Cài plugin trên máy mới không tải cuốn sách.
Không chỉnh trực tiếp bản plugin trong bộ nhớ đệm cài đặt; sửa kho nguồn và phát hành.

## Bản quyền

Chưa chọn giấy phép mã nguồn mở: xem [LICENSE](LICENSE). Kho công khai không tự
cấp giấy phép mã nguồn mở. Chủ sở hữu có thể sử dụng trên các máy/tài khoản của mình.
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
liệt kê các dự án tham khảo; không chứa mã được sao chép từ các skill đó.
