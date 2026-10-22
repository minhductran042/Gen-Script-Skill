---
name: vid-viet-kich-ban
description: "Viết kịch bản video ngắn dọc mang chất điện ảnh theo format Excel của team (STT, Tóm tắt - Title, Địa điểm, Mục đích, Nhân vật, Nội dung, Biểu cảm, Góc quay, Text nổi bật, Ghi chú) từ một concept đã chọn. Viết qua tám lượt: chốt xương sống (logline, câu hỏi kịch tính, cài – trả), dàn beat có mốc giây, lượt hình ảnh, lượt thoại, lượt âm thanh, lượt chữ nổi, lượt sản xuất cho một máy quay, rồi đọc thử bấm giờ. Ghi JSON làm bản gốc, soát bằng kich_ban.py kiem, xuất Excel. Có chế độ sửa theo file review và chế độ chuyển kịch bản viết tự do sang format. Dùng khi user nói 'viết kịch bản concept này', 'ra kịch bản chi tiết', 'sửa kịch bản theo review', 'xuất kịch bản ra Excel', 'chuyển kịch bản này sang format'. Nghĩ ý tưởng thì dùng vid-brainstorm; chấm kịch bản thì dùng vid-review."
argument-hint: <concept | 01-concepts.md + mã concept | kich-ban-vN.json + 03-review-vN.md để sửa>
---

# Viết và sửa kịch bản

## Kiến thức dùng

Luôn đọc:
- `shared/luat/format-kich-ban.md`: cách viết từng cột, cấu trúc JSON.
- `shared/luat/dieu-kien-san-xuat.md`: sáu diễn viên (1 nữ, 5 nam), một máy quay, hai người dựng.
- `shared/luat/vung-cam.md`.
- `shared/luat/loi-kich-ban.md`: biết trước lỗi để tránh.
- `shared/nghe/cau-truc-va-nhip.md`, `hook-va-giu-chan.md`, `an-du-va-hai.md`, `ngon-ngu-dien-anh.md`,
  `chu-de-va-thong-diep.md`.

Tham khảo: **chỉ khi brief ghi ở mục "Tham khảo"**, và chỉ đúng thứ được nêu. Không lấy nội dung trong
`shared/mau-format/`.

Brief có video mẫu: đọc thêm `shared/luat/bam-mau.md` và mục 8–9 của `phan-tich.md` mà brief chỉ tới. Viết xong, dò
từng câu thoại, chữ nổi và chuỗi hành động với mục 9 "Không được chép"; trùng thì viết lại trước khi bàn giao (MAU-01).
Không đọc dòng thời gian của mẫu khi viết, để khỏi bị kéo theo nội dung.

---

## Chế độ 1: Viết mới

Đầu vào: brief + một thẻ concept (từ `01-concepts.md` hoặc người dùng mô tả). Concept người dùng đưa thiếu logline,
ẩn dụ hay hook thì tự đề xuất phần thiếu, ghi rõ "đề xuất" ở đầu ra.

Viết qua tám lượt theo thứ tự. **Mỗi lượt chỉ tập trung một lớp**, không viết tất cả cùng lúc.

### Lượt 1: Xương sống

Ghi vào đầu `ghi-chu-viet.md` của dự án (file nháp, không xuất Excel):

- **Logline** và **câu hỏi kịch tính chính** (xem `cau-truc-va-nhip.md` mục 1).
- **Cài – trả**: chi tiết nào cài ở đầu, trả lại ở cuối với nghĩa gì.
- **Khoảnh khắc mở khoá ẩn dụ**: ở beat nào, bằng hình gì.
- **Thông điệp** (một câu, dạng phát hiện) và **câu chuyện bề mặt** chứa nó, theo luật lồng ghép ở
  `shared/nghe/chu-de-va-thong-diep.md` mục 1. Kiểm bẫy của nhóm chủ đề ở mục 2.
- **Câu đọng** ở beat chốt.
- **Đường cảm xúc**: nhân vật chính đi từ trạng thái nào tới trạng thái nào.

### Lượt 2: Dàn beat

- Chọn cấu trúc theo concept (khung mặc định hoặc cấu trúc khác ở `cau-truc-va-nhip.md` mục 4).
- Lập danh sách beat: mỗi beat có **Mục đích** (chức năng) và **mốc giây**, theo bảng phân bổ ở mục 3 của file đó.
- Kiểm: mỗi beat chỉ một chức năng; không có hai beat liền nhau cùng ý; tổng giây khớp mục tiêu.

### Lượt 3: Hình ảnh

Với từng beat, viết phần **hành động** của cột Nội dung, cột **Góc quay**, **Địa điểm**:

- Mỗi beat có **một hình ảnh chủ đạo**: cái người xem nhớ nếu chỉ thấy một khung của beat đó.
- Viết hành động máy quay thấy được, động từ cụ thể.
- Chọn cỡ cảnh theo cảm xúc: xa khi lạc lõng, gần khi nhận ra, đặc tả cho đồ vật ẩn dụ.
- Ít nhất **một đặc tả đồ vật ẩn dụ** và **một khoảnh khắc không thoại** trong cả kịch bản.
- Cột **Biểu cảm**: trạng thái + biểu hiện nhìn thấy được.

Kiểm bằng bài tắt tiếng (`hook-va-giu-chan.md` mục 7): chỉ đọc hành động, có hiểu câu chuyện không?

### Lượt 4: Thoại

Thêm thoại vào cột Nội dung, sau hành động:

- **Chỉ thêm thoại ở chỗ hình không tự kể được.** Câu nào hình đã nói thì bỏ.
- Mỗi lượt thoại ngắn, ưu tiên dưới khoảng 20 từ; nói như người trẻ nói: câu cụt, tiếng lóng vừa phải, xưng hô hợp quan
  hệ nhân vật.
- **Mỗi nhân vật một giọng**: một người nói ngắn và thẳng, người kia vòng vo; một người hay hỏi lại, người kia hay
  đùa. Che tên nhân vật đi mà vẫn đoán được ai nói thì đạt.
- **Câu đùa đặt từ gây cười ở cuối câu.** Trước câu đùa có một nhịp ngừng (ghi ở chỉ dẫn diễn).
- **Không có câu giải thích ẩn dụ.** Không có câu nói thẳng thông điệp trước beat lật.
- Chỉ dẫn diễn ngắn đặt trước câu thoại: `A (nói nhỏ): "…"`.

### Lượt 5: Âm thanh

Cột Ghi chú, phần âm thanh:

- Mỗi khoảnh khắc chính có **một tiếng động đặc trưng**, viết bằng từ tượng thanh.
- Nhạc: tính chất + lúc vào / ra. Không ghi tên bài có bản quyền (VC-13).
- Đặt **tắt lặng** ở một chỗ: thường ngay trước hoặc ngay sau beat lật.
- Ghi J-cut / L-cut khi cần âm thanh dẫn hình.

### Lượt 6: Chữ nổi

Cột Text nổi bật:

- Hook: chữ đặt tình huống hoặc câu hỏi, 4–8 từ (bắt buộc nếu hook dựa vào thoại).
- Giữa video: tối đa 1–2 chữ nhấn.
- Beat chốt: câu đọng lại.
- Không chép phụ đề thoại vào cột này.

### Lượt 7: Sản xuất

Đi qua mục 5 "Kiểm quay được" ở `dieu-kien-san-xuat.md`:

- Đếm nhân vật, bối cảnh.
- Gom mọi đồ vật trong cột Nội dung vào dòng **Đạo cụ**, kèm số lượng và dự phòng.
- Hành động không lặp lại được: ghi "chỉ quay một lần ở góc …" hoặc số đạo cụ dự phòng.
- Cảnh hai thứ cùng lúc: ghi "quay tách, ghép khi dựng".
- Mọi hiệu ứng dựng đã có ở Ghi chú.

### Lượt 8: Đọc thử bấm giờ

- Ước thời lượng từng beat theo `cau-truc-va-nhip.md` mục 5 (thoại + hành động + khoảng lặng). Ghi vào `giay`.
- Tổng lệch mục tiêu trên 10% thì cắt theo thứ tự ở mục đó.
- Đọc lại cả kịch bản một mạch, như người xem. Chỗ nào thấy chán thì sửa.
- Chạy ba bài kiểm ở `hook-va-giu-chan.md` mục 7.

### Soát và xuất

Ghi `du-an/<dự án>/kich-ban-v1.json` theo cấu trúc ở `format-kich-ban.md` mục 3, rồi:

```
py -I shared/scripts/kich_ban.py kiem du-an/<dự án>/kich-ban-v1.json
```

Còn lỗi Nặng hoặc Vừa thì sửa JSON và chạy lại tới khi hết. Lỗi Nhẹ được để lại nếu có lý do, ghi lý do vào
`ghi-chu-viet.md`.

```
py -I shared/scripts/kich_ban.py xuat du-an/<dự án>/kich-ban-v1.json du-an/<dự án>/kich-ban-v1.xlsx
```

Báo lại: đường dẫn hai file, tổng giây ước tính, số nhân vật, bối cảnh, kết quả `kiem`.

---

## Chế độ 2: Sửa theo review

Đầu vào: `kich-ban-vN.json` + `03-review-vN.md`.

1. Đọc hết review. Sắp lỗi theo thứ tự: **Nặng → Vừa → Nhẹ**, và trong cùng mức thì lỗi ở beat đầu trước.
2. Phân loại từng lỗi:
   - **Cục bộ**: sửa trong một beat (thoại dài, thiếu đặc tả, thiếu đạo cụ…).
   - **Cấu trúc**: phải đổi nhiều beat (lộ kết sớm, không có câu hỏi kịch tính, ẩn dụ không hiểu). Lỗi cấu trúc thì
     quay lại lượt 1–2 cho phần liên quan, không vá từng câu.
3. Sửa **mọi lỗi Nặng và Vừa**. Lỗi Nhẹ sửa khi không làm hỏng chỗ khác.
4. **Giữ nguyên** những gì review ghi ở "Điểm mạnh nên giữ". Sửa mà phải đụng vào điểm mạnh thì ghi lý do.
5. Sửa xong một lỗi cấu trúc thì chạy lại lượt 8 (bấm giờ) cho toàn kịch bản.
6. Ghi bản mới `kich-ban-v(N+1).json`, **không ghi đè** bản cũ.
7. Ghi `sua-vN.md`:

```markdown
| Mã lỗi | Beat | Loại (cục bộ / cấu trúc) | Đã sửa thế nào | Ảnh hưởng beat khác |
|---|---|---|---|---|
Lỗi không sửa: | Mã | Lý do |
```

8. Chạy `kiem` rồi `xuat` như chế độ 1.

Gợi ý sửa trong review là gợi ý, không bắt buộc chép nguyên văn. Có cách sửa tốt hơn thì dùng, và ghi vào `sua-vN.md`.

---

## Chế độ 3: Chuyển format

- Người dùng đưa kịch bản viết tự do (văn bản, Google Docs, ghi chú): dựng JSON theo format, **không đổi nội dung**.
  Tách beat theo chức năng. Cột nào không có thông tin thì để trống, rồi liệt kê cho người dùng các cột trống theo beat.
- Người dùng đưa file Excel đúng format:
  ```
  py -I shared/scripts/kich_ban.py doc <file.xlsx> du-an/<dự án>/kich-ban-v1.json
  ```
- Xong thì chạy `kiem` và báo kết quả. Không tự sửa nội dung, trừ khi người dùng yêu cầu.

---

## Không làm

- Không sửa tay file `.xlsx`.
- Không vượt 6 nhân vật hoặc 2 bối cảnh khi brief không cho phép.
- Không tự đổi concept đã được chọn. Thấy concept có vấn đề thì ghi một dòng cho người dùng.
- Không ghi đè phiên bản cũ.
