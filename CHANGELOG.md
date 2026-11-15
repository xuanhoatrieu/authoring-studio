# Changelog

## 0.2.0 — 2026-11-15

- Giữ cấu trúc plugin Codex; sinh thêm gói write-book độc lập cho Antigravity và
  Hermes Agent/Desktop từ cùng nguồn, có toàn bộ tài nguyên và manifest phiên bản.
- Thêm hướng dẫn cài/cập nhật/khôi phục theo host, kiểm tra gói sinh khớp nguồn,
  kiểm thử helper trong gói giải nén và hai ZIP tái lập kèm SHA256.
- Theo xác nhận ngày 15/11/2026 sau khi đọc bản thử 0.5.0, áp dụng chung tên hình
  trực tiếp “Hình x.x. Nội dung của hình.”; bỏ tiền tố “Minh họa” và “Ví dụ” thừa.
- Rà đồng thời thân bài, chữ trong ảnh và caption; kiểm tra quan hệ/thao tác thực
  sự nhìn thấy trong hình, giữ nhận diện giả định ở ngữ cảnh cần thiết.
- Bỏ lời phòng ngừa cho suy diễn đoạn văn không đặt ra; giữ giới hạn có ý nghĩa.
- Bổ sung quy tắc dàn trang chung: không lặp tên đầy đủ sau bìa chương riêng,
  ưu tiên giữ bảng ngắn và đoạn dẫn cùng hình/bảng; mục lục được trải nhiều trang.
  Cập nhật plugin không tự sửa bản thảo hiện có.
- Tích hợp bước biên tập văn phong tự nhiên vào viết mới, sửa và rà toàn sách;
  dùng chung cho mọi hồ sơ, có hướng dẫn cụ thể cho giáo trình tiếng Việt.
- Tham khảo academic-humanizer, avoid-ai-writing và humanizer để rà từ thừa,
  lập luận theo khuôn, lặp ý và giọng phô trương; bảo toàn thuật ngữ, dữ kiện,
  mức chắc chắn, nguồn và phạm vi sửa. Không dùng danh sách từ cấm máy móc.
- Bổ sung kiểm tra độ bao phủ toàn sách và các tình huống đánh giá biên tập;
  phân biệt kiểm thử cấu trúc với chất lượng văn phong cần đánh giá thực tế.
- Bỏ dòng tự ghi công cho hình, bảng và biểu mẫu tự biên soạn; giữ dẫn nguồn bên ngoài.
- Rút gọn chú thích, chuyển ghi chú xử lý ảnh vào hồ sơ và giữ ghi công cần thiết
  trong mục nguồn ảnh; bỏ số đếm, lời dẫn và câu phòng ngừa thừa.
- Yêu cầu minh họa thể hiện nội dung, chọn hình thức theo thao tác/quy trình/quan hệ,
  không mặc định lặp các khung chứa chữ.
- Chốt căn đều nội dung, tiêu đề căn trái, chú thích hình 12 pt căn giữa, đoạn trước
  0/sau 4 pt trong hồ sơ rural-tourism-vi; bảo toàn lịch sử và các lựa chọn còn mở.
- Yêu cầu áp dụng và kiểm tra định dạng trên bản đọc/bản xuất được yêu cầu;
  bổ sung kiểm thử truyền cấu hình và các tình huống đánh giá hành vi.
- Thêm thiết kế brief/prompt theo nội dung; lưu prompt của ảnh, đặc tả sơ đồ/biểu đồ
  và kiểm tra kết quả. Cảnh minh họa có thể chủ động tạo theo phong cách chân thực.
- Chốt thứ tự bìa sách, lời nói đầu, mục lục, giới thiệu chung; mỗi chương có bìa
  riêng, nội dung ở trang tiếp theo; chữ tiêu đề dàn riêng với ảnh.
- Ảnh bìa không caption, không số hình; mở rộng chỉ mục ảnh/schema 1 và bộ kiểm
  tra để hỗ trợ vai trò bìa và đường dẫn prompt, vẫn nhận bản ghi hình nội dung cũ.
- Thêm footer “@ TS.Triệu Xuân Hoà” bên trái và số trang tự động bên phải trong
  hồ sơ du lịch; giữ lịch sử caption căn trái đã được thay bằng căn giữa.

## 0.1.0 — 2026-11-14

- Thêm plugin authoring-studio và skill write-book.
- Tách quy trình chung khỏi hồ sơ sách du lịch; lưu các quyết định và điểm còn mở.
- Chốt quy cách tên bảng và hàng tiêu đề đầu tiên căn giữa.
- Thêm mẫu Markdown/YAML, schema 1, khởi tạo không ghi đè và kiểm tra liên kết.
- Thêm kiểm thử, đóng gói có checksum, marketplace và hướng dẫn GitHub.
- Chưa tạo nội dung sách hoặc skill trình chiếu.
