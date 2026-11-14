# Cài đặt và cập nhật

Đối chiếu theo tài liệu OpenAI ngày 14/11/2026. Các thao tác khả dụng tùy phiên bản
ứng dụng, tài khoản và chính sách workspace. Cài từ Git không đồng nghĩa xuất hiện
trong thư mục plugin công khai. Chưa kiểm thử cài trong ứng dụng của người dùng.

## Dùng kho trên máy

Trong ứng dụng hỗ trợ marketplace, thêm thư mục gốc kho này làm nguồn, rồi cài
plugin Authoring Studio. Hoặc với Codex CLI có lệnh plugin:

```sh
codex plugin marketplace add /path/to/authoring-studio
codex plugin add authoring-studio@authoring-studio-marketplace
```

Mở cuộc trao đổi mới sau khi cài và kiểm tra skill write-book được nhận diện.
Plugin được chạy từ bản cài/cache; sửa kho nguồn chưa chắc cập nhật bản đang cài.

## Dùng GitHub trên máy hoặc tài khoản khác

Sau khi kho đã được push và tag đã tồn tại:

```sh
codex plugin marketplace add xuanhoatrieu/authoring-studio --ref v0.1.0
codex plugin add authoring-studio@authoring-studio-marketplace
```

Nguồn được thêm là repository, không phải URL raw của marketplace.json. Marketplace
name là `authoring-studio-marketplace`, khác plugin name `authoring-studio`.
Nếu kho riêng tư, máy/tài khoản cần quyền GitHub phù hợp. Mỗi môi trường có thể cần
cài lại plugin và cung cấp các công cụ tìm nguồn/tạo ảnh riêng.

## Cập nhật

Ghim tag giữ nguyên bản đã chọn. Để chuyển từ v0.1.0 sang tag khác, đổi Git ref của
nguồn marketplace trong giao diện/CLI hỗ trợ, làm mới nguồn rồi cập nhật/cài lại
plugin. Kiểm tra bản đã cài trong trang chi tiết; không chỉ kiểm tra kho nguồn.

Nếu cố ý theo dõi nhánh (ví dụ `main`), luồng CLI được tài liệu mô tả là:

```sh
codex plugin marketplace upgrade authoring-studio-marketplace
codex plugin add authoring-studio@authoring-studio-marketplace
```

Không mặc định ứng dụng tự cập nhật mọi tài khoản sau một lần push. Với workspace
quản lý qua GitHub, dùng cơ chế import/sync của quản trị workspace; quyền cài đặt và
các kết nối dịch vụ vẫn được quản lý riêng.

## Quay lại phiên bản cũ

Chọn tag cũ và cài lại, giữ nguyên thư mục sách. Trước thay đổi schema trong tương
lai phải sao lưu; quay lại plugin không tự quay lại dữ liệu đã được chuyển đổi.

## Kiểm tra máy mới

- Đúng plugin version và schema sách.
- Đã đồng bộ riêng thư mục sách cùng ảnh và nguồn.
- Công cụ tìm nguồn/tạo ảnh khả dụng nếu công việc cần.
- Python và phụ thuộc chỉ cần cho các helper.
- Times New Roman cần được xác nhận khi xuất bản; không âm thầm thay phông.

Nguồn: https://developers.openai.com/plugins/build/plugins
