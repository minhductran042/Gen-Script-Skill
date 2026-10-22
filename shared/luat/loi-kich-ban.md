# Danh mục lỗi kịch bản và bảng chấm

Luật bắt buộc cho `vid-review`. `vid-viet-kich-ban` đọc file này để biết trước lỗi mà tránh.

- Mỗi lỗi có mã, mức mặc định, dấu hiệu nhận ra và hướng sửa.
- Mã có nhãn **[script]** được `kich_ban.py kiem` bắt tự động. Các mã còn lại do người review đọc và chấm.
- Gặp kiểu lỗi mới trong thực tế thì thêm dòng vào đây, kèm nguồn (dự án nào, beat nào).

---

## 1. Mức độ

| Mức | Nghĩa | Hệ quả |
|---|---|---|
| **Nặng** | Video sẽ hỏng: mất người xem ngay, không quay được, hoặc vi phạm | Phải sửa trước khi quay. Còn lỗi Nặng thì không ĐẠT |
| **Vừa** | Giảm giữ chân, giảm độ hiểu, hoặc tốn công khi quay / dựng | Nên sửa trong vòng sửa |
| **Nhẹ** | Có thể hay hơn | Gợi ý; được bỏ qua nếu có lý do |

Người review được nâng hoặc hạ mức một bậc nếu bối cảnh cụ thể đòi hỏi, và phải ghi lý do.

## 2. Danh mục

### HK: Hook

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| HK-01 | Nặng | Ba giây đầu không có lý do để dừng lướt | Mở bằng cảnh tĩnh, đi bộ, chào hỏi, giới thiệu; không có hành động, âm thanh hay chữ gây tò mò | Mở thẳng vào hành động; chọn một dạng ở `shared/nghe/hook-va-giu-chan.md` mục 2 |
| HK-02 | Nặng | Hook hứa một đằng, nội dung một nẻo | Câu hỏi hoặc tình huống ở hook không được trả lời ở cuối | Sửa hook cho khớp payoff, hoặc sửa payoff |
| HK-03 | Vừa | **[script]** Beat đầu không đánh dấu Hook hoặc không có mốc giây | Cột Mục đích beat 1 thiếu "Hook" hoặc thiếu `giay` | Ghi `Hook (0–3s)` |
| HK-04 | Vừa | Ẩn dụ / vấn đề chính chưa xuất hiện trong hook | Đồ vật hoặc vấn đề chính chỉ xuất hiện từ giữa video | Đưa đồ vật vào khung đầu tiên |
| HK-05 | Vừa | Hook không hiểu được khi tắt tiếng | Hook dựa hoàn toàn vào thoại, không có hình lạ hay chữ | Thêm Text nổi bật hoặc đổi sang hook bằng hình |
| HK-06 | Nhẹ | Chữ hook dài | Trên khoảng 10 từ | Rút còn 4–8 từ |

### GC: Giữ chân

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| GC-01 | Nặng | Không có câu hỏi kịch tính chính | Đọc hết 5 giây đầu vẫn không biết mình đang chờ điều gì | Viết lại logline; thêm mong muốn + trở ngại vào beat thiết lập |
| GC-02 | Vừa | Beat đi ngang | Hai beat liền nhau cùng một ý, mâu thuẫn không tăng | Gộp hai beat, hoặc làm beat sau tệ / hài hơn |
| GC-03 | Vừa | Lộ kết sớm | Câu chốt hoặc thông điệp nói ra trong nửa đầu video | Dời thông điệp xuống sau beat lật |
| GC-04 | Vừa | Đoán được kết | Đọc tới giữa đã đoán đúng | Thêm một chi tiết lệch hướng; đổi kiểu kết |
| GC-05 | Vừa | Đoạn chết trên khoảng 5 giây | Không có thông tin, hành động, góc hay âm thanh mới | Chèn phản ứng, đặc tả, đổi góc, hoặc cắt |
| GC-06 | Nhẹ | Thoại dài | Một lượt thoại trên khoảng 25 từ | Tách lượt, cắt ý, hoặc thay bằng hình |
| GC-07 | Vừa | Kéo dài sau payoff | Còn trên 1 beat sau câu chốt mà không phải miếng thoát | Cắt |

### AD: Ẩn dụ và hài

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| AD-01 | Nặng | Ẩn dụ không hiểu được nếu không giải thích | Không có khoảnh khắc mở khoá bằng hình; hoặc điểm khớp quá xa | Chọn ẩn dụ có điểm khớp rõ hơn (`an-du-va-hai.md` mục 3) |
| AD-02 | Vừa | Nhân vật giải thích ẩn dụ | Câu thoại nói thẳng "cái này giống như…", "đó chính là…" | Để hình nói; giữ tối đa một câu ngắn |
| AD-03 | Vừa | Thành bài giảng | Kết bằng triết lý, không có miếng thoát | Thêm beat thoát (hài nhẹ / hành động bình thường) |
| AD-04 | Vừa | Ẩn dụ đã nhàm | Ẩn dụ quen thuộc ai cũng đoán được | Đổi đồ vật, hoặc lật cách dùng ẩn dụ |
| AD-05 | Vừa | Hài cần ngữ cảnh người xem không có | Meme cũ, đùa nội bộ, tham chiếu quá hẹp | Đổi sang hài tình huống / nhân vật |
| AD-06 | Nhẹ | Nhịp hài sai | Từ gây cười không ở cuối câu; không có khoảng ngừng; nhân vật tự cười | Đảo câu, thêm ngừng, cắt sang phản ứng |
| AD-07 | Nhẹ | Nhiều ẩn dụ chồng nhau | Hơn một ẩn dụ chính | Giữ một, bỏ còn lại |
| AD-08 | Vừa | Thông điệp nuốt câu chuyện | Bỏ thông điệp đi thì câu chuyện bề mặt không còn gì để xem | Làm dày tầng bề mặt: xung đột, hài, chi tiết đời thường |
| AD-09 | Vừa | Thông điệp dạng mệnh lệnh | "Hãy…", "Đừng…", "Phải biết…" | Viết lại thành phát hiện / nghịch lý (`chu-de-va-thong-diep.md` mục 1) |
| AD-10 | Vừa | Rơi vào bẫy của nhóm chủ đề | Xem mục "Bẫy" của nhóm ở `chu-de-va-thong-diep.md` mục 2 | Theo hướng tránh của nhóm |
| AD-11 | Nhẹ | Nhiều thông điệp | Hơn một thông điệp chính | Giữ một |

### DA: Điện ảnh

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| DA-01 | Vừa | Beat chỉ có thoại | Nội dung chỉ là hai người nói chuyện; Ghi chú trống | Thêm hành động, đặc tả hoặc tiếng động mang nghĩa |
| DA-02 | Vừa | Kể bằng lời điều hình kể được | Thoại mô tả cảm xúc / sự việc mà hình đã thể hiện hoặc có thể thể hiện | Bỏ câu đó, thay bằng hình |
| DA-03 | Nhẹ | Góc máy đơn điệu | Ba beat liền nhau cùng một cỡ cảnh | Đổi cỡ cảnh theo cảm xúc |
| DA-04 | Nhẹ | Âm thanh không cụ thể | Ghi "có nhạc", "tiếng động" chung chung | Ghi tính chất nhạc, tiếng động bằng từ tượng thanh, lúc vào / ra |
| DA-05 | Nhẹ | Không có khoảnh khắc lặng | Không beat nào chỉ có hình + âm thanh | Thêm 1–2 giây lặng trước / sau lật |
| DA-06 | Nhẹ | Đồ vật ẩn dụ không có đặc tả | Đồ vật chỉ xuất hiện ở góc trung / toàn | Thêm đặc tả |
| DA-07 | Vừa | Biểu cảm không quay được | Cột Biểu cảm / Nội dung ghi cảm xúc trừu tượng mà không có hành động thể hiện | Ghi hành động nhìn thấy được |

### KT: Kết

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| KT-01 | Vừa | Kết không tạo hành động ở người xem | Không có lý do để xem lại, comment, tag hay lưu | Chọn một dạng kết ở `hook-va-giu-chan.md` mục 6 |
| KT-02 | Nhẹ | **[script]** Beat cuối không có Text nổi bật | Cột I beat cuối trống | Thêm câu chốt, hoặc ghi lý do cố ý để trống |
| KT-03 | Vừa | Kết bằng lời kêu gọi | "Nhớ follow", "like nếu thấy đúng" nằm trong câu chuyện | Bỏ; để caption làm việc đó |

### SX: Sản xuất

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| SX-01 | Nặng | **[script]** Số nhân vật vượt số diễn viên (6) | Đếm nhân vật khác nhau ở cột E | Gộp vai, bỏ vai phụ |
| SX-02 | Nặng | Không quay được với một máy quay / thiết bị hiện có | Cần hai góc cùng lúc mà không ghi "quay tách, ghép khi dựng"; cần flycam, cẩu, bám xe | Ghi cách quay tách, hoặc đổi cảnh |
| SX-03 | Vừa | Trên 2 bối cảnh | Cột Địa điểm đổi nhiều lần | Gộp bối cảnh |
| SX-04 | Vừa | Hành động không lặp lại được ở cảnh nhiều góc | Đổ, vỡ, xé, bẩn mà không ghi "chỉ quay một lần" / đạo cụ dự phòng | Ghi rõ, hoặc dời hành động sang một góc |
| SX-05 | Vừa | Đạo cụ thiếu trong dòng Đạo cụ | Đồ vật xuất hiện ở cột Nội dung nhưng không có trong danh sách | Bổ sung |
| SX-06 | Vừa | Hiệu ứng dựng không được viết ra | Kịch bản ngầm định hiệu ứng mà Ghi chú không ghi | Ghi ở cột Ghi chú |
| SX-07 | Nhẹ | Quá 4 nhân vật mà concept không cần | 5–6 nhân vật, có vai không có thoại hay chức năng | Bỏ vai |
| SX-08 | Vừa | Tổng thời lượng lệch mục tiêu trên 10% | Cộng giây các beat, hoặc ước theo thoại | Cắt theo thứ tự ở `cau-truc-va-nhip.md` mục 5 |
| SX-09 | Nặng | Vượt cơ cấu giới tính diễn viên (1 nữ, 5 nam) | Hai nhân vật nữ cùng lộ mặt, hoặc trên 5 nhân vật nam | Nhân vật nữ thứ hai chỉ nghe giọng / qua màn hình / quay tay, lưng; hoặc đổi giới tính vai |

### AT: An toàn

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| AT-01 | Nặng | Vi phạm mục "Cấm hẳn" | Xem `shared/luat/vung-cam.md` mục 1 | Đổi concept / cảnh theo cột "Thay bằng" |
| AT-02 | Vừa | Chạm mục "Hạn chế" mà chưa xử lý | Xem `vung-cam.md` mục 2 (nhạc bản quyền, thương hiệu, người lạ…) | Xử lý theo cột "Cách xử lý" |

### NH: Nháp và trình bày

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| NH-01 | Nặng | **[script]** Nội dung dán nhầm từ kịch bản khác | Một đoạn dài trùng nguyên văn giữa hai kịch bản | Viết lại beat |
| NH-02 | Vừa | **[script]** Ghi chú nháp / chữ không dấu lẫn vào thoại | Mệnh đề viết không dấu | Xoá hoặc viết lại có dấu |
| NH-03 | Vừa | **[script]** Thiếu trường bắt buộc | Mục đích, Nhân vật, Nội dung, Góc quay trống; thiếu tên, thời lượng, đạo cụ… | Điền |
| NH-04 | Nhẹ | Chú thích lẫn vào thoại | Câu trong ngoặc nằm giữa lời thoại, không rõ là thoại hay ghi chú | Đưa chỉ dẫn diễn ra trước câu thoại, hoặc sang Ghi chú |
| NH-05 | Nhẹ | Tên nhân vật không thống nhất | Một nhân vật được gọi hai tên khác nhau | Thống nhất |

### SR: Series

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| SR-01 | Nặng | Mâu thuẫn với kinh thánh series | Nhân vật hành xử trái tính cách, sự kiện trái tập trước | Đối chiếu `series.md` |
| SR-02 | Vừa | Tập không xem độc lập được | Người chưa xem tập trước không hiểu tình huống | Thêm thiết lập 2–3 giây; bỏ phụ thuộc |
| SR-03 | Nhẹ | Thiếu dấu hiệu nhận diện series | Không có tên series, câu mở quen, nhạc nhận diện | Thêm theo quy ước trong `series.md` |

### MAU: Bám mẫu (chỉ chấm khi brief có video mẫu, luật ở `bam-mau.md`)

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| MAU-01 | Nặng | Chép mẫu | Thoại, câu chốt, chữ nổi hay chuỗi hành động trùng một mục trong "Không được chép" (mục 9 của `phan-tich.md`), dù đổi vài chữ | Viết lại từ insight của mình; giữ chức năng của beat, đổi hẳn nội dung |
| MAU-02 | Vừa | Mất điểm hay muốn học | Brief ghi "học từ mẫu: hook / nhịp / …" mà kịch bản không có kỹ thuật tương ứng ở mục 5 của bản phân tích | Đưa lại đúng kỹ thuật đó, đặt ở vị trí tương đương |
| MAU-03 | Vừa | Đổi ít hơn mức bám cho phép | Mức "Cùng công thức" mà đổi dưới 3 trong 4 (vấn đề, đồ vật ẩn dụ, bối cảnh, quan hệ nhân vật) | Đổi thêm thứ còn giống mẫu nhất |
| MAU-04 | Vừa | Bắt trend mà không có gì riêng | Mức "Bắt trend" nhưng không có cú lật riêng, chỉ thay chữ | Thêm một cú lật hoặc góc nhìn mà video cùng trend khác chưa có |
| MAU-05 | Nhẹ | Học cả điểm yếu của mẫu | Kịch bản lặp một điểm ở mục 6 "Điểm yếu, không nên học" | Sửa theo mã lỗi đã ghi ở mục 6 |

## 3. Bảng chấm điểm (thang 10)

**CHƯA CHỐT:** team chưa đưa tiêu chí riêng. Bản dưới đây áp dụng cho tới khi team thay.

| Tiêu chí | Trọng số | 2 điểm (kém) | 6 điểm (được) | 10 điểm (xuất sắc) |
|---|---|---|---|---|
| **Hook** | 2.5 | Không có lý do dừng lướt | Có tò mò nhưng chỉ một lớp (hình hoặc chữ) | Hai lớp trở lên, ẩn dụ có trong khung đầu, hiểu được khi tắt tiếng |
| **Giữ chân, nhịp** | 2 | Có đoạn chết, đoán được kết | Mâu thuẫn tăng, một chỗ hơi chậm | Mỗi beat mới, có vòng mở, kết bất ngờ mà hợp lý |
| **Ẩn dụ** | 1.5 | Phải giải thích mới hiểu | Hiểu được, nhưng quen hoặc mở khoá bằng lời | Hiểu ngay, mới, mở khoá bằng hình, có diễn biến |
| **Hài** | 1.5 | Không cười được, hoặc hài gượng | Có 1–2 chỗ cười | Hài từ nhân vật, nhịp đúng, có miếng thoát |
| **Chất điện ảnh** | 1.5 | Chỉ có thoại | Có đặc tả hoặc âm thanh được thiết kế | Kể bằng hình, ánh sáng / âm thanh mang nghĩa, có khoảnh khắc lặng |
| **Quay được** | 1 | Có cảnh không quay được | Quay được nhưng tốn công | Gọn, thiết kế cho một máy quay, hiệu ứng dựng viết rõ |

Điểm tổng = Σ (điểm tiêu chí × trọng số) / 10.

**ĐẠT** khi không còn lỗi Nặng **và** điểm tổng ≥ 8.
