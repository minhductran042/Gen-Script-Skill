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
| HK-06 | Nhẹ | **[script]** Chữ hook dài | Trên khoảng 10 từ | Rút còn 4–8 từ |

### GC: Giữ chân

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| GC-01 | Nặng | Không có câu hỏi kịch tính chính | Đọc hết 5 giây đầu vẫn không biết mình đang chờ điều gì | Viết lại logline; thêm mong muốn + trở ngại vào beat thiết lập |
| GC-02 | Vừa | Beat đi ngang | Hai beat liền nhau cùng một ý, mâu thuẫn không tăng | Gộp hai beat, hoặc đẩy cảm xúc của beat sau lên |
| GC-03 | Vừa | Lộ kết sớm | Câu chốt, hoặc thông điệp nếu có, nói ra trong nửa đầu video | Dời xuống sau đỉnh hoặc beat lật |
| GC-04 | Vừa | Đoán được kết (chỉ khi chuyện dựa vào bất ngờ) | Đọc tới giữa đã đoán đúng | Thêm một chi tiết lệch hướng; đổi kiểu kết |
| GC-05 | Vừa | Đoạn chết trên khoảng 5 giây | Không có thông tin, hành động, góc hay âm thanh mới, và cảm xúc không lớn thêm (cảnh giữ lâu có chủ đích ở tông chậm không phải lỗi) | Chèn phản ứng, đặc tả, đổi góc, hoặc cắt |
| GC-06 | Nhẹ | **[script]** Thoại dài | Một lượt thoại trên khoảng 25 từ. Được bỏ qua nếu là lượt thoại đỉnh | Tách lượt, cắt ý, hoặc thay bằng hình |
| GC-07 | Vừa | Kéo dài sau payoff | Còn trên 1 beat sau câu chốt mà không phải miếng thoát hay hình kết | Cắt |
| GC-08 | Vừa | Dài mà không có lý do | Có đoạn trên 20 giây không có thông tin mới, không đổi thế, cảm xúc không lớn thêm; cắt đi chuyện không mất gì. Đây là căn cứ duy nhất để đề nghị rút ngắn, phải chỉ ra đúng đoạn | Cắt đoạn đó, hoặc thêm một điều mới có thật trong chuyện |

### AD: Ẩn dụ, hài và thông điệp

Áp theo công cụ kịch bản dùng (`shared/nghe/tong-cam-xuc.md` mục 7): AD-01, 02, 04, 07 chỉ khi dùng Ẩn dụ; AD-05, 06 chỉ khi dùng Hài; AD-08, 09,
11 chỉ khi có thông điệp; AD-03, 10 áp mọi tông. Thiếu thứ kịch bản không chọn thì không phải lỗi.

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| AD-01 | Nặng | Ẩn dụ không hiểu được nếu không giải thích | Không có khoảnh khắc mở khoá bằng hình; hoặc điểm khớp quá xa | Chọn ẩn dụ có điểm khớp rõ hơn (`an-du-va-hai.md` mục 3) |
| AD-02 | Vừa | Nhân vật giải thích ẩn dụ | Câu thoại nói thẳng "cái này giống như…", "đó chính là…" | Để hình nói; giữ tối đa một câu ngắn |
| AD-03 | Vừa | Thành bài giảng | Kết bằng lời triết lý, nói hộ người xem | Cắt câu giảng, để hình hoặc hành động bình thường khép lại; kịch bản dùng Hài thì thêm miếng thoát |
| AD-04 | Vừa | Ẩn dụ đã nhàm | Ẩn dụ quen thuộc ai cũng đoán được | Đổi đồ vật, hoặc lật cách dùng ẩn dụ |
| AD-05 | Vừa | Hài cần ngữ cảnh người xem không có | Meme cũ, đùa nội bộ, tham chiếu quá hẹp | Đổi sang hài tình huống / nhân vật |
| AD-06 | Nhẹ | Nhịp hài sai | Từ gây cười không ở cuối câu; không có khoảng ngừng; nhân vật tự cười | Đảo câu, thêm ngừng, cắt sang phản ứng |
| AD-07 | Nhẹ | Nhiều ẩn dụ chồng nhau | Hơn một ẩn dụ chính | Giữ một, bỏ còn lại |
| AD-08 | Vừa | Thông điệp nuốt câu chuyện | Bỏ thông điệp đi thì câu chuyện bề mặt không còn gì để xem | Làm dày tầng bề mặt: xung đột, hài, chi tiết đời thường |
| AD-09 | Vừa | Thông điệp dạng mệnh lệnh | "Hãy…", "Đừng…", "Phải biết…" | Viết lại thành phát hiện / nghịch lý (`chu-de-va-thong-diep.md` mục 1) |
| AD-10 | Vừa | Rơi vào bẫy của nhóm chủ đề | Xem mục "Bẫy" của nhóm ở `chu-de-va-thong-diep.md` mục 2 | Theo hướng tránh của nhóm |
| AD-11 | Nhẹ | Nhiều thông điệp | Hơn một thông điệp chính | Giữ một |

### CX: Tông cảm xúc

Áp mọi tông, chấm theo tông đã chọn ở brief.

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| CX-01 | Nặng | Lệch tông | Cảm xúc đọng lại khác tông đã chọn; hoặc có công cụ brief đã khoá (có hài khi brief ghi "không hài"), hoặc hài vượt liều của cảm xúc (`tong-cam-xuc.md` mục 5) | Viết lại beat đỉnh theo cơ chế ở `tong-cam-xuc.md` mục 3; bỏ phần lệch |
| CX-02 | Vừa | Cảm xúc không leo thang | Cảm xúc đều từ đầu đến cuối, không có đỉnh | Dồn tới một beat đỉnh; beat trước chuẩn bị cho nó |
| CX-03 | Vừa | Sến, ép cảm xúc | Nhạc, tiếng khóc hoặc thoại gọi tên cảm xúc thay cho tình huống | Bỏ phần ép, thay bằng hành động nhỏ, cụ thể |
| CX-04 | Vừa | Hài phá cảnh lặng | Miếng hài chen vào ngay đỉnh cảm xúc hoặc khoảng lặng | Dời hài ra xa đỉnh ít nhất một beat, hoặc bỏ |
| CX-05 | Nhẹ | Đường cảm xúc gãy | Chuyển cảm xúc đột ngột, không có chi tiết bắc cầu | Thêm một chi tiết hoặc khoảng ngừng ở chỗ chuyển |

### DA: Điện ảnh

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| DA-01 | Vừa | Beat nói suông | Thoại không làm đổi tình thế, **và** không có dàn cảnh, phản ứng hay đổi cỡ cảnh | Thêm việc cho đoạn thoại, hoặc dàn cảnh theo `ngon-ngu-dien-anh.md` mục 11 |
| DA-02 | Vừa | Kể bằng lời điều hình kể được | Câu chỉ nói cho người xem nghe, mô tả điều hình đã thể hiện. Câu nhân vật cần nói với nhau (tấn công, biện hộ, che giấu) không phải lỗi | Bỏ câu đó, thay bằng hình |
| DA-03 | Nhẹ | Góc máy đơn điệu | Ba beat liền nhau cùng một cỡ cảnh | Đổi cỡ cảnh theo cảm xúc |
| DA-04 | Nhẹ | Âm thanh không cụ thể | Ghi "có nhạc", "tiếng động" chung chung | Ghi tính chất nhạc, tiếng động bằng từ tượng thanh, lúc vào / ra |
| DA-05 | Nhẹ | Không có khoảnh khắc lặng | Không beat nào chỉ có hình + âm thanh | Thêm 1–2 giây lặng trước / sau lật |
| DA-06 | Nhẹ | Đồ vật ẩn dụ không có đặc tả (chỉ khi dùng ẩn dụ) | Đồ vật chỉ xuất hiện ở góc trung / toàn | Thêm đặc tả |
| DA-07 | Vừa | Biểu cảm không quay được | Cột Biểu cảm / Nội dung ghi cảm xúc trừu tượng mà không có hành động thể hiện | Ghi hành động nhìn thấy được |

### TH: Thoại và độ gần gũi

Áp mọi chủ đề và mọi tông, thước đo ở `shared/nghe/thoai-va-do-gan.md`. Không có thoại nhiều thì không phải lỗi.

| Mã | Mức | Lỗi | Dấu hiệu | Hướng sửa |
|---|---|---|---|---|
| TH-01 | Vừa | Thoại như văn viết | Đọc thành tiếng thấy giả; câu trọn vẹn, văn vẻ, xưng hô không đúng quan hệ | Viết lại như người đang nói: câu cụt, ngắt lời, chi tiết cụ thể |
| TH-02 | Vừa | Nhân vật không có lý do riêng | Nhân vật chỉ tồn tại để phục vụ tình huống, không muốn gì cho mình. Hài phóng đại thì hạ xuống Nhẹ | Cho nhân vật một mong muốn và một lý lẽ của mình |

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
| SX-03 | Vừa | **[script]** Trên 2 bối cảnh | Cột Địa điểm đổi nhiều lần | Gộp bối cảnh |
| SX-04 | Vừa | Hành động không lặp lại được ở cảnh nhiều góc | Đổ, vỡ, xé, bẩn mà không ghi "chỉ quay một lần" / đạo cụ dự phòng | Ghi rõ, hoặc dời hành động sang một góc |
| SX-05 | Vừa | Đạo cụ thiếu trong dòng Đạo cụ | Đồ vật xuất hiện ở cột Nội dung nhưng không có trong danh sách | Bổ sung |
| SX-06 | Vừa | Hiệu ứng dựng không được viết ra | Kịch bản ngầm định hiệu ứng mà Ghi chú không ghi | Ghi ở cột Ghi chú |
| SX-07 | Nhẹ | Quá 4 nhân vật mà concept không cần | 5–6 nhân vật, có vai không có thoại hay chức năng | Bỏ vai |
| SX-08 | Vừa | **[script]** Tổng thời lượng lệch mục tiêu trên 10% | Cộng giây các beat, hoặc ước theo thoại. Brief ghi "Theo chuyện" thì `thoi_luong` là khoảng đã bấm giờ, script so với khoảng đó | Cắt theo thứ tự ở `cau-truc-va-nhip.md` mục 5 |
| SX-09 | Nặng | **[script]** Vượt cơ cấu giới tính diễn viên (1 nữ, 5 nam) | Hai nhân vật nữ cùng lộ mặt, hoặc trên 5 nhân vật nam (script chỉ đếm vai có ghi `nữ`) | Nhân vật nữ thứ hai chỉ nghe giọng / qua màn hình / quay tay, lưng; hoặc đổi giới tính vai |
| SX-10 | Vừa | Vai lộ mặt lệch xa độ tuổi diễn viên (21–22) | Bố mẹ, ông bà, sếp trung niên lộ mặt mà không phải chủ ý gây hài | Chỉ nghe giọng / qua màn hình / quay tay, lưng; hoặc đổi vai về cùng lứa |
| SX-11 | Vừa | Chữ, nút hoặc hành động chính nằm trong vùng giao diện che | Đặt ở đáy hoặc cạnh phải khung (`khan-gia-va-nen-tang.md`). Nguồn: gói dùng thử beat 4–5, phòng trọ | Dời vào vùng an toàn, ghi vị trí ở Ghi chú |
| SX-12 | Vừa | Lệch liên tục hình hoặc không gian giữa các beat quay tách | Đồ trên người, vị trí ngồi, mức đồ ăn mâu thuẫn giữa các beat. Nguồn: gói dùng thử, phòng trọ | Ghi sơ đồ vị trí và dòng "Liên tục" ở Lưu ý sản xuất |

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
| NH-06 | Nhẹ | **[script]** Mốc giây thiếu hoặc không liền nhau | Beat thiếu `giay`, hoặc mốc đầu beat khác mốc cuối beat trước | Sửa mốc giây |

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
| **Hook** | 2.5 | Không có lý do dừng lướt | Có tò mò nhưng chỉ một lớp (hình hoặc chữ) | Hai lớp trở lên, vấn đề hoặc ẩn dụ chính có trong khung đầu, hiểu được khi tắt tiếng |
| **Giữ chân, nhịp** | 2 | Có đoạn chết, đoán được kết | Mâu thuẫn tăng, một chỗ hơi chậm | Mỗi beat mới, có vòng mở, kết bất ngờ mà hợp lý hoặc trọn vẹn đúng tông |
| **Sức mạnh cảm xúc** | 1.5 | Không gây được cảm xúc rõ, hoặc lệch tông | Đúng tông nhưng nhẹ, hoặc có chỗ gượng | Gây đúng cảm xúc đã chọn, có đỉnh rõ, không gượng; có hài thì hài từ nhân vật, nhịp đúng |
| **Cách kể** | 1.5 | Phải giải thích mới hiểu, hoặc chung chung | Hiểu được, nhưng quen | Hiểu ngay và mới. Ẩn dụ: mở khoá bằng hình, có diễn biến. Kể thẳng: chi tiết cụ thể, thật. Mượn thể loại: đúng luật thể loại |
| **Chất điện ảnh** | 1.5 | Đứng nói suông, không dàn cảnh | Có đặc tả, dàn cảnh hoặc âm thanh được thiết kế | Hình, thoại, âm thanh cùng kể; ánh sáng / âm thanh mang nghĩa, có khoảnh khắc lặng |
| **Quay được** | 1 | Có cảnh không quay được | Quay được nhưng tốn công | Gọn, thiết kế cho một máy quay, hiệu ứng dựng viết rõ |

Điểm tổng = Σ (điểm tiêu chí × trọng số) / 10, giữ hai chữ số thập phân, không làm tròn khi so ngưỡng. Mọi tiêu chí chấm theo
tông đã chọn; không trừ điểm vì thiếu hài, ẩn dụ, lật hay thông điệp.

**ĐẠT** khi không còn lỗi Nặng **và** điểm tổng ≥ 8.
