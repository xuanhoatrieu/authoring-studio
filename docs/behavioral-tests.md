# Tình huống đánh giá hành vi

Trạng thái: CHƯA CHẠY kiểm thử hành vi bằng một phiên model độc lập. Các kiểm thử
Python không chứng minh các hành vi này đã đạt. Chạy trong thư mục tạm, ghi kết quả
quan sát và phiên bản trước khi phát hành ổn định 1.0.0.

| Yêu cầu thử | Kết quả cần quan sát |
|---|---|
| Tiếp tục thảo luận, chưa viết | Không tạo chương hoặc bản xuất |
| Chỉ lập đề cương | Không biến đề cương thành bài viết |
| Tên bảng và hàng tiêu đề căn giữa | Không căn giữa tiêu đề chương/mục |
| Sách khác có cỡ caption đang là đề xuất | Không coi thông số của hồ sơ du lịch là phê duyệt cho sách đó |
| Khởi tạo với hồ sơ rural-tourism-vi đã cập nhật | Nhận đủ căn đều nội dung, tiêu đề căn trái, caption 12 căn giữa, đoạn trước 0/sau 4; giữ đúng quy cách bảng |
| Hình, bảng hoặc biểu mẫu tự làm cho người dùng | Không thêm dòng “Nguồn: tác giả biên soạn”; vẫn giữ nguồn nếu nội dung dựa trên nghiên cứu bên ngoài |
| Rút gọn chú thích ảnh vùng chè | Chỉ giữ mô tả và người tạo ảnh cần thiết; chuyển ghi chú xử lý vào hồ sơ, giữ thông tin nguồn/giấy phép cần xuất bản trong mục nguồn ảnh |
| Chú thích có ghi chú “ảnh không xác nhận…” | Bỏ câu phòng ngừa thừa, không bỏ giới hạn thực sự ảnh hưởng đến cách hiểu nội dung |
| Nhãn “Bốn câu hỏi” và bài tập “chọn ba việc ưu tiên” | Rút gọn nhãn thành “Các câu hỏi”; giữ số lượng trong yêu cầu bài tập |
| Minh họa số hóa thông tin, công cụ số và cách tổ chức | Thể hiện tờ giới thiệu/điện thoại, thao tác bảng tính và người dùng chung lịch; không lặp ba đoạn chữ trong khung |
| Các mục gồm thao tác, quy trình, cảnh quan và so sánh | Chọn hình thức trực quan theo nội dung, không dùng một mẫu ô chữ cho cả bộ hình |
| Làm bản đọc HTML theo thông số đã chốt | Áp dụng định dạng, kiểm tra màn hình và trang in A4; không coi khai báo CSS là bằng chứng đã đúng bố cục |
| Tiếp tục ở cuộc trao đổi mới | Đọc quyết định, trạng thái và nội dung hiện tại |
| Người dùng đã sửa một đoạn | Giữ sửa đổi, chỉ chỉnh phạm vi được yêu cầu |
| Thiếu ảnh phù hợp | Ghi phần thiếu, không gán ảnh tạo mới cho một sự kiện thật |
| Bài 2025 được truy cập 2026 | Giữ đúng năm xuất bản và ngày truy cập |
| Danh hiệu du lịch không có số liệu khách | Không suy ra hiệu quả truyền thông hay doanh thu |
| Đổi vị trí chương | ID và tham chiếu vẫn đúng sau cập nhật mapping |
| Tài khoản không có công cụ tạo ảnh | Báo giới hạn, tiếp tục phần có thể làm |
| Nâng plugin nhưng không yêu cầu sửa sách | Không ghi đè hoặc chuyển đổi bản thảo |
| Minh họa một hoạt động theo phong cách chân thực | Brief xuất phát từ đoạn sách, prompt mô tả hành động/bố cục; tạo và kiểm tra ảnh khi được yêu cầu, lưu prompt theo hình |
| Chỉ thảo luận hoặc chỉ viết prompt | Không tạo ảnh, viết chương hay sửa plugin ngoài phạm vi |
| Yêu cầu sơ đồ quy trình hoặc biểu đồ số liệu | Vẽ đúng liên kết/nhãn hoặc dữ liệu/trục; không mặc định dùng công cụ sinh ảnh cho mọi loại hình |
| Thiết kế bìa sách và bìa chương | Tiêu đề chữ lớn dàn riêng; ảnh đại diện đúng chủ đề; không caption/số hình; thông tin nguồn cần thiết ở cuối sách |
| Xuất sách theo cấu trúc mới | Bìa → Lời nói đầu → Mục lục → Giới thiệu chung; tên và tóm tắt đúng các chương; nội dung mỗi chương bắt đầu sau bìa riêng |
| Tạo mục lục với bìa chương lưu riêng | Một mục cho mỗi chương, số trang/dích đến đúng; bìa không thành chương mới hoặc hình đánh số |
| Footer và caption theo hồ sơ du lịch | Caption nội dung căn giữa; footer đúng “@ TS.Triệu Xuân Hoà” trái, số trang tự động phải, không đè nội dung |
| Dùng Quarto để dựng đầu ra | Cấu hình caption riêng với căn hình, kiểm tra bìa/ngắt trang/footer trên từng đầu ra; không mặc định cài hoặc chuyển đổi sách |
| Viết sách khác với hồ sơ riêng | Không mang tên tác giả ở footer, nội dung du lịch hoặc cấu trúc riêng của hồ sơ du lịch sang sách đó |

Đánh giá biên tập cần một người đọc mục tiêu đọc thử. Không sử dụng điểm đọc hiểu
tiếng Anh làm thước đo tự động cho độc giả tiếng Việt.

## Biên tập văn phong tự nhiên — bổ sung 15/11/2026

Trạng thái các ca dưới đây: CHƯA CHẠY bằng phiên model độc lập. Khi chạy, lưu
bản nguồn, yêu cầu, kết quả, phạm vi thay đổi và nhận xét trong thư mục tạm.
Đánh giá ý nghĩa và hành động thực tế; không chấm bằng khớp từ khóa hoặc một câu
viết lại duy nhất. Những chuỗi ngắn dưới đây là dữ liệu kiểm thử, không phải mẫu
nội dung bắt buộc đưa vào sách.

| Yêu cầu thử | Kết quả cần quan sát |
|---|---|
| Viết một mục mới của giáo trình thống kê, không dùng hồ sơ du lịch | Tự áp dụng biên tập trong viết mới và rà trước giao; không chờ yêu cầu “humanize”, không thêm chủ đề/giọng/footer du lịch |
| Rà cuốn sách nhiều chương có lời dẫn lặp cả trong lời nói đầu, phụ lục, bảng và caption | Bao phủ đủ phạm vi được giao, ghi phần đã/chưa rà, kiểm tra lặp xuyên chương; không tuyên bố xong sau vài trang mẫu |
| Chỉ nhận xét văn phong một chương có câu mở sáo rỗng | Nêu vị trí, lý do, hướng sửa; không sửa tệp hoặc viết chương mới |
| Chỉ sửa một đoạn trong bản người dùng vừa chỉnh | Đọc nguồn mới, sửa đúng đoạn, giữ các thay đổi thủ công và phần ngoài phạm vi |
| “Có thể nói rằng nhóm nghiên cứu tiến hành thực hiện việc kiểm tra thiết bị.” | Bỏ lời dẫn/danh từ hóa thừa, giữ nhóm nghiên cứu là tác nhân và hành động kiểm tra; không thêm lịch, kết quả hoặc phương pháp |
| “Trong mẫu 48 người, tỷ lệ tăng 12%, nhưng chưa đủ bằng chứng kết luận nguyên nhân [@nguon-a].” | Giữ 48, 12%, giới hạn và nguồn; không biến thành tăng 12 điểm phần trăm hoặc kết luận nhân quả |
| “Không phải mọi trường hợp đều cần điều trị”; “có thể giảm sai số nếu…” | Bảo toàn phủ định, mức chắc chắn và điều kiện; không xóa vì giống mẫu từ bị rà |
| Chương sinh thái có “hệ sinh thái”, chương thống kê có “ý nghĩa thống kê” | Giữ thuật ngữ đúng nghĩa; không thay bằng từ khác chỉ để tránh từ bị coi là AI |
| Chương phân biệt hai khái niệm, quy trình thật có ba bước và nhiều đoạn dùng cùng thuật ngữ | Giữ đối lập có nghĩa, đủ ba bước và thuật ngữ nhất quán; chỉ sửa đối lập trang trí hoặc lặp vô ích |
| Câu “nhiều nghiên cứu chứng minh…” không có nguồn trong hồ sơ | Ghi khoảng trống bằng chứng, không bịa tác giả/số liệu, không báo đã kiểm chứng sau khi sửa câu |
| Trích dẫn nguyên văn, công thức, URL, bảng có cả chữ và dữ liệu, tham chiếu hình | Sửa lời diễn giải được giao; giữ trích dẫn, công thức, dữ liệu, đường dẫn và khóa tham chiếu |
| Tóm tắt cuối chương có ích, định nghĩa cần nhắc lại và các đoạn đã rõ | Giữ chức năng sư phạm và đoạn tốt; không ép cắt, đảo hoặc thêm biến thể cho mọi đoạn |
| Có mẫu giọng tác giả được duyệt và sách chuyên khảo có điều kiện phức tạp | Theo giọng và mức chuyên môn đó; không chuyển sang hội thoại, thêm trải nghiệm hay giản lược mất điều kiện |
| Sách bằng ngôn ngữ khác, chỉ yêu cầu sửa câu chữ | Áp dụng nguyên tắc chung theo ngôn ngữ sách, không ép cụm từ tiếng Việt, cấu trúc giáo trình hay tái tổ chức ngoài phạm vi |
| Bản sửa đã trôi chảy nhưng còn một luận điểm chưa có bằng chứng | Báo riêng vấn đề chưa giải quyết; không dùng điểm phát hiện AI hoặc kiểm tra nguồn để chứng nhận văn phong/factual accuracy |

Các ca bổ sung sau phản hồi bản đọc thử ngày 14/11/2026 cũng CHƯA CHẠY bằng phiên
model độc lập. Các ca bổ sung ngày 15/11/2026 cũng chưa chạy bằng phiên model độc
lập. Kiểm thử khởi tạo/chỉ mục xác nhận cấu hình và liên kết, không chứng minh chất
lượng ảnh hay bố cục trang đã đạt.

## Chú thích, ý nghĩa hình và phân trang — xác nhận 15/11/2026

Các quy tắc được duyệt sau khi đọc bản thử 0.5.0 và áp dụng chung cho mọi sách.
Các ca dưới đây CHƯA CHẠY bằng phiên model độc lập; phản hồi về bản đọc trước
không phải kết quả đánh giá phiên bản skill mới. Khi kiểm tra bố cục, cần xem bản
dựng thực tế; kiểm tra văn bản nguồn hoặc khai báo CSS không đủ.

| Yêu cầu thử | Kết quả cần quan sát |
|---|---|
| Viết hình cho sách kỹ thuật hoặc lịch sử, không chọn hồ sơ du lịch | Caption gọi trực tiếp nội dung; không tự thêm “Minh họa”, chủ đề hay footer du lịch |
| Caption “Hình 2.3. Minh họa quá trình trao đổi nhiệt” | Bỏ tiền tố, giữ số và ý nghĩa; dùng ngôn ngữ/cách đánh số đã chọn khi sách không viết tiếng Việt |
| Caption gọn nhưng ảnh còn “Thông điệp minh họa” hoặc tiêu đề giải thích dài | Đọc chữ trong ảnh và sửa nguồn ảnh trong phạm vi cho phép; không tuyên bố đã sửa hết chỉ bằng sửa caption |
| Thuật ngữ “phương pháp minh họa” là đối tượng của hình | Giữ nghĩa chuyên môn; không xóa mọi lần xuất hiện của từ bằng thay thế hàng loạt |
| Cảnh đẹp có người trao đổi nhưng bài giải thích luồng dữ liệu dùng chung | Nhận ra quan hệ còn thiếu; chọn sơ đồ hoặc kết hợp cảnh với luồng/nhãn rõ, không nhận ảnh chỉ vì đẹp |
| Tình huống dùng giá giả định được nhắc ở đoạn dẫn, tiêu đề hình, caption và thân bài | Giữ nhận diện tại ngữ cảnh cần thiết và giảm trùng; không biến số giả định thành giá được xác nhận |
| Hình giả định được xuất riêng để chia sẻ | Giữ nhận diện đi cùng hình khi mất ngữ cảnh; không áp quy tắc rút caption gây hiểu nhầm |
| Đoạn mô tả hoạt động kèm phủ nhận kết quả không được đề cập | Bỏ câu phòng ngừa thừa; ở đoạn có kết luận về hiệu quả, giữ giới hạn bằng chứng tương ứng |
| Bìa chương đã có đầy đủ tên, trang nội dung lặp lại tên ấy | Bắt đầu nội dung bằng mục đầu tiên, giữ ID/cấu trúc ngữ nghĩa và một mục lục chương; sách không có bìa riêng giữ tiêu đề thường |
| Bảng ngắn đủ một trang bị chia đôi, đoạn dẫn ngắn nằm trang trước | Dàn lại để ưu tiên giữ cùng nhau, không thu nhỏ chữ hoặc đảo thứ tự đọc; kiểm tra các trang lân cận |
| Bảng dài hơn một trang | Cho tiếp trang với hàng tiêu đề lặp và chỉ dẫn tiếp nối; không ép cả bảng vào một trang |
| Mục lục sách nhiều chương vượt một trang | Cho trải nhiều trang với chữ/khoảng cách dễ đọc, số trang và đích đến cập nhật; không nén để đủ một trang |
| Chỉ cập nhật skill và bản cài, chưa sửa sách | Không thay nội dung, ảnh, hồ sơ, bản đọc hoặc các tệp khác trong dự án sách |
