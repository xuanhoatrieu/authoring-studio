# Chuẩn bị đưa lên GitHub

Kho được quản lý độc lập tại `xuanhoatrieu/authoring-studio`, theo lựa chọn công khai
của chủ sở hữu. Không chứa bản thảo sách hoặc ảnh của sách.

## Đưa kho lên lần đầu

Tạo một repository GitHub trống tên `authoring-studio` trong tài khoản `xuanhoatrieu`.
Kiểm tra tệp đang đưa vào Git; không thêm `.venv`, `dist`, bí mật hoặc bản thảo.
Nếu muốn cấp quyền sử dụng mã nguồn công khai, chọn giấy phép rồi cập nhật LICENSE;
bản hiện tại giữ bản quyền, không tự cấp giấy phép mở.

Chạy trong thư mục gốc kho:

```sh
git status
git add .
git commit -m "Prepare authoring-studio 0.1.0"
git branch -M main
git remote add origin https://github.com/xuanhoatrieu/authoring-studio.git
git push -u origin main
```

Nếu đã có commit hoặc remote thì bỏ qua bước tương ứng; không ghi đè remote.
Git cần tên/email của người dùng được cấu hình; không tạo danh tính giả để commit.

## Phát hành 0.1.0

```sh
python scripts/validate_repo.py --tag v0.1.0
python -m unittest discover -s tests -v
python scripts/build_release.py
git tag -a v0.1.0 -m "Authoring Studio 0.1.0"
git push origin v0.1.0
```

Workflow kiểm tra trên Linux, macOS và Windows; chỉ khi các kiểm tra qua mới dựng
gói và tạo GitHub Release từ tag. Release có ZIP plugin và SHA256. Workflow không
push bản thảo và không cấp quyền cài plugin cho tài khoản khác.
Nên bật bảo vệ nhánh và immutable releases nếu phù hợp. Không di chuyển tag đã phát hành.

## Lần phát hành sau

1. Chỉnh sửa trên nhánh làm việc; ghi thay đổi trong CHANGELOG.
2. Tăng version trong hai manifest; thêm `docs/releases/<version>.md`.
3. Chạy kiểm thử và xem các thay đổi với bản trước.
4. Với thay đổi schema, bổ sung công cụ chuyển đổi riêng có sao lưu và kiểm thử.
5. Commit, tag đúng version, push khi được yêu cầu phát hành.

PATCH sửa lỗi tương thích; MINOR thêm tính năng tương thích; MAJOR thay đổi không
tương thích. Trong giai đoạn 0.x, cũng ghi rõ mọi thay đổi không tương thích, không
cho rằng người dùng tự hiểu. Plugin version khác book schema và bản thảo version.

## Nguồn

- https://developers.openai.com/plugins/build/plugins
- https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
