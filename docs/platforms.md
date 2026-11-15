# Dùng chung trên Codex, Antigravity và Hermes Agent/Desktop

## Nguồn và gói cài

0.2.0 duy trì một bộ nguồn tại `plugins/authoring-studio/`. Cấu trúc, marketplace,
tên và cách gọi plugin Codex giữ nguyên. Không đổi các đường dẫn tài nguyên Codex.
`scripts/build_standalone.py` tạo `skills/write-book/` từ nguồn đó; không sửa tay
bản sinh. Chạy lại sau khi sửa nguồn, rồi commit cả nguồn và bản sinh. Validator
so sánh từng byte để phát hiện lệch phiên bản hoặc tài nguyên bị thiếu.

Release có hai ZIP kèm SHA256:

- `authoring-studio-0.2.1.zip`: plugin theo cấu trúc cũ cho Codex.
- `write-book-standalone-0.2.1.zip`: thư mục `write-book/` tự chứa cho host đọc Agent Skills.

Gói độc lập có SKILL.md, references, resources/templates, profiles, schemas,
scripts, requirements và manifest phiên bản. Nó không cần các tệp nằm bên ngoài
thư mục skill. Manifest tài nguyên chỉ phục vụ helper đọc phiên bản, không yêu cầu
Antigravity/Hermes cài plugin Codex. Metadata giao diện Codex không đưa vào gói độc lập.

## Codex

Giữ marketplace `authoring-studio-marketplace` và plugin `authoring-studio`.
Làm theo [cài và cập nhật](install-update.md), chọn tag `v0.2.1` khi cài từ GitHub.
Không cài thêm gói độc lập vào cùng Codex để tránh trùng skill. Mở cuộc trao đổi
mới và xác nhận bản cài là 0.2.1. Nâng plugin không nâng hay sửa bản thảo.

## Antigravity

Giải nén gói độc lập. Với phạm vi dự án, đặt cả thư mục `write-book/` vào
`<workspace>/.agents/skills/`; không chỉ chép SKILL.md. Khi ứng dụng nhận skill,
yêu cầu dùng `write-book` và đọc đúng thư mục sách trước khi làm việc.

Vị trí toàn máy khác nhau giữa các bề mặt Antigravity; không áp một đường dẫn
toàn máy cho tất cả. Đối chiếu tài liệu của App/CLI/IDE đang sử dụng. Phạm vi dự
án là lựa chọn cài đặt đầu tiên được hướng dẫn ở đây. Tùy bản ứng dụng, cần mở lại
cuộc trao đổi hoặc tải lại workspace để nhận thay đổi.

## Hermes Agent và Desktop

Với Hermes, cài thư mục skill độc lập vào `skills/` của Hermes home/profile đang
dùng (mặc định `~/.hermes/skills/write-book/`). Desktop kết nối backend từ xa thì
cài vào backend/profile từ xa đó, không chỉ máy đang mở cửa sổ Desktop.

Kho có sẵn đường dẫn chuẩn `skills/write-book/SKILL.md` để dùng làm nguồn GitHub.
Theo tài liệu Hermes hiện tại, có thể thêm tap và cài qua Skills Hub/CLI:

```sh
hermes skills tap add xuanhoatrieu/authoring-studio
hermes skills install xuanhoatrieu/authoring-studio/write-book
```

Kiểm tra nguồn và phiên bản được cài; cú pháp/quản lý profile phụ thuộc bản Hermes.
Nếu bản đó không nhận tap, dùng gói ZIP độc lập. Gọi `/write-book` hoặc yêu cầu
agent sử dụng skill. Không dùng chức năng tự học để viết lại bản phát hành chuẩn;
lưu thay đổi mong muốn trong kho nguồn và xây dựng lại gói.

## Cập nhật và khôi phục

Phân biệt plugin version, bundle version và schema sách. Giữ schema 1 trong 0.2.0.
Tải bản phát hành/tag cụ thể, đối chiếu SHA256 với tệp checksum. Trước khi thay
thư mục đã cài, sao lưu toàn thư mục ra ngoài vùng nhận diện skill và kiểm tra
chỉnh sửa cá nhân. Không chép đè mù các tệp do người dùng sửa; giữ bản cũ, đối chiếu
và đưa sửa đổi cần giữ về nguồn trước. Không trộn tệp cũ/mới bằng chép đè một phần.

Với gói ZIP, thay cả thư mục sau khi kiểm tra/sao lưu. Với Hermes Hub, dùng cơ chế
kiểm tra/cập nhật của bản Hermes đang cài; không ép ghi đè bản sửa cục bộ. Với Codex,
dùng trình quản lý plugin. Khôi phục bằng bản skill/plugin đã sao lưu hoặc tag cũ.
Không đụng đến thư mục sách khi cập nhật, khôi phục hoặc thay nền tảng.

## Kiểm tra khả năng khi sử dụng

Quy tắc biên soạn chung; công cụ do host cung cấp. Agent kiểm tra khả năng đọc/ghi
tệp, chạy Python, tìm nguồn, tạo/đọc ảnh và dựng/xem trang trước các bước cần chúng.
Không mặc định tên công cụ hoặc nhà cung cấp model giống Codex. Nếu thiếu công cụ,
ghi phần chưa làm, tiếp tục phần độc lập; không báo prompt là ảnh đã tạo hay CSS
là bố cục đã được xem. Không tự cài dịch vụ hoặc thư viện toàn máy.

Để kiểm tra helper, tạo môi trường Python riêng từ `resources/requirements.txt`,
rồi chạy `resources/scripts/init_book.py` và `validate_book.py` với dự án tạm nằm
ngoài thư mục skill. Bản Codex vẫn dùng `scripts/` ở gốc plugin như trước.

Kiểm tra thực tế trên host: nhận diện skill → chỉ thảo luận không tạo chương →
khởi tạo dự án tạm khi được yêu cầu → viết/sửa phạm vi nhỏ → kiểm tra ảnh/nguồn
và bản dựng nếu công cụ khả dụng. Ghi rõ host/version và bước chưa kiểm tra.

0.2.0 đã kiểm tra đóng gói, liên kết và helper của gói giải nén. Chưa xác nhận
end-to-end trên Antigravity/Hermes Desktop khi không có các ứng dụng đó trong
môi trường kiểm tra; cấu trúc tương thích không chứng minh hành vi model đã đạt.

Tài liệu đối chiếu ngày 15/11/2026:

- [Antigravity Agent Skills](https://antigravity.google/docs/skills)
- [Hermes Skills System](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- [Hermes Desktop](https://github.com/fathah/hermes-desktop)
