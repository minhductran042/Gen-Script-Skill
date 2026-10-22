# Workspace kịch bản video ngắn

Bộ skill brainstorm, viết và review kịch bản video ngắn dọc mang chất điện ảnh cho TikTok / YouTube Shorts.
Đọc `README.md` để biết luồng và cấu trúc thư mục. Cửa vào duy nhất cho người dùng là `/vid`; sở thích mặc định
của team ở `shared/cau-hinh.md`.

- Trả lời người dùng bằng tiếng Việt.
- Mọi kịch bản lưu dạng JSON (`kich-ban-vN.json`) làm bản gốc, Excel chỉ là bản xuất. Sửa JSON rồi xuất lại, không
  sửa tay file Excel do script sinh.
- Ba lớp kiến thức trong `shared/`:
  - `luat/`: **ràng buộc cứng** (format, điều kiện sản xuất, vùng cấm, danh mục lỗi). Luôn áp. Mục ghi **CHƯA CHỐT**
    thì dùng giá trị tạm và ghi rõ trong đầu ra.
  - `nghe/`: **kiến thức nghề** (khán giả, hook, ẩn dụ, điện ảnh, cấu trúc). Luôn dùng làm thước đo, nhưng là nguyên
    tắc, không phải công thức bắt buộc. Brief của lần làm được ghi đè.
  - `tham-khao/`: **tham khảo tuỳ chọn** do team cung cấp. Chỉ đọc khi brief của lần đó ghi ở mục "Tham khảo". Không
    tự ghi vào thư mục này, trừ `tham-khao/mau/` khi người dùng đồng ý lưu bản phân tích video mẫu.
- Video mẫu là tuỳ chọn. Không hỏi người dùng có mẫu không; có mẫu thì phân tích bằng `vid-phan-tich-mau` và áp
  `shared/luat/bam-mau.md`. Công cụ phân tích tự cài vào `.cong-cu/` lần đầu, không bắt người dùng cài.
- `shared/mau-format/` chỉ là mẫu định dạng Excel. Không lấy nội dung, giọng văn, hook hay ẩn dụ từ đó.
- Ví dụ trong `shared/nghe/` là minh hoạ, không đưa nguyên vào kịch bản.
- Xong việc được giao thì dừng, không kết thúc bằng danh sách đề xuất mới.
