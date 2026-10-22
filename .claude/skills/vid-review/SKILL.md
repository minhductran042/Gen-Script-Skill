---
name: vid-review
description: "Review một kịch bản video ngắn dọc qua năm lượt đọc với năm vai: người lướt (3 giây đầu, tắt tiếng), người xem hết (nhịp, đoán kết, ẩn dụ, hài), đạo diễn (chất điện ảnh), đội sản xuất (một máy quay, sáu diễn viên, bối cảnh, đạo cụ, dựng), và nền tảng (vùng cấm, bản quyền). Mỗi lỗi có mã từ danh mục (HK, GC, AD, DA, KT, SX, AT, NH, SR), mức Nặng / Vừa / Nhẹ, vị trí beat và giây, trích nguyên văn, và gợi ý sửa viết sẵn. Chấm điểm theo bảng tiêu chí có mốc, kết luận ĐẠT / CHƯA ĐẠT, ghi điểm mạnh nên giữ. Nhận JSON hoặc file Excel đúng format team. Dùng khi user nói 'review kịch bản', 'kịch bản này ổn chưa', 'chấm kịch bản', 'chỗ nào chưa ổn', 'cải tiến kịch bản này', 'góp ý kịch bản'. Không sửa kịch bản (sửa thì dùng vid-viet-kich-ban chế độ sửa)."
argument-hint: <kich-ban-vN.json | file .xlsx>
---

# Review kịch bản

Mục tiêu: người viết đọc báo cáo là **biết sửa gì, ở đâu, sửa thế nào**, không phải đoán. Mọi nhận xét phải chỉ được
về một chỗ cụ thể trong kịch bản.

## Kiến thức dùng

Luôn đọc:
- `shared/luat/loi-kich-ban.md`: danh mục lỗi, mức, bảng chấm.
- `shared/luat/dieu-kien-san-xuat.md`, `vung-cam.md`, `format-kich-ban.md`.
- `shared/nghe/` (cả sáu file): làm thước đo.
- `00-brief.md` của dự án nếu có: mục tiêu, nhóm khán giả, thời lượng. Series thì đọc thêm `series.md`.

Tham khảo: chỉ khi brief ghi. Có tham khảo thì thêm một câu hỏi: kịch bản có đúng tinh thần tham khảo người dùng chọn
không. Không có tham khảo thì **không chấm theo bất kỳ phong cách riêng nào**, chỉ chấm theo luật và nghề.

Brief có video mẫu: đọc thêm `shared/luat/bam-mau.md` và `phan-tich.md` của mẫu (mục 5, 6, 8, 9), rồi chấm nhóm lỗi
`MAU-01..05`: dò thoại, chữ nổi, chuỗi hành động với mục 9; kiểm kỹ thuật người dùng muốn học (mục "Học từ mẫu" trong
brief) có mặt không; đếm số biến số đã đổi theo mức bám. Mỗi lỗi MAU trích cả câu trong kịch bản lẫn câu trong mẫu.

---

## Bước 0: Chuẩn bị

1. Đầu vào là `.xlsx` thì đọc ra JSON trước:
   ```
   py -I shared/scripts/kich_ban.py doc <file.xlsx> <thư mục dự án>/kich-ban-v1.json
   ```
   Không có thư mục dự án thì tạo `du-an/<YYYY-MM-DD>-review-<slug>/`.
2. Chạy soát cấu trúc, giữ nguyên kết quả để dán vào báo cáo:
   ```
   py -I shared/scripts/kich_ban.py kiem <kich-ban.json>
   ```
3. Vòng review lại (có `sua-v(N-1).md`): lập danh sách lỗi cũ để kiểm ở bước 6.

## Bước 1: Lượt người lướt

Đọc **chỉ beat đầu**, như người đang lướt.

- Ba giây đầu có lý do để dừng không? (HK-01)
- Hook dùng mấy lớp (hình / âm / chữ)? Hiểu được khi tắt tiếng không? (HK-05)
- Ẩn dụ hoặc vấn đề đã có trong khung đầu chưa? (HK-04)
- Hook thuộc dạng nào (`HK-Dxx`)? Dạng đó có được làm đúng cách chưa?

## Bước 2: Lượt người xem hết

Đọc tuần tự, **dừng ở giữa kịch bản** và ghi lại kết bạn đoán. Rồi đọc tiếp.

- Câu hỏi kịch tính chính rõ trong 5 giây đầu chưa? (GC-01)
- Đánh dấu chỗ nào thấy chán, chậm, trùng ý. (GC-02, GC-05)
- Kết có trùng điều bạn đoán ở giữa không? (GC-04)
- Thông điệp lộ ra ở beat nào? Có trước beat lật không? (GC-03)
- Ẩn dụ: hiểu ngay không, mở khoá bằng hình hay bằng lời, có nhàm không? (AD-01, AD-02, AD-04)
- Hài: cười ở đâu, cơ chế gì, nhịp đúng chưa? Có miếng thoát sau phần chạm không? (AD-03, AD-05, AD-06)
- Kết khiến người xem làm gì (xem lại, comment, tag, lưu)? (KT-01, KT-03)
- Sau payoff còn kéo dài không? (GC-07)
- Hook hứa gì, kết có trả đúng không? (HK-02)
- Lồng ghép (`chu-de-va-thong-diep.md` mục 1): bỏ thông điệp đi câu chuyện còn xem được không? Thông điệp là phát hiện
  hay mệnh lệnh? Có nhiều hơn một thông điệp không? Có rơi vào bẫy của nhóm chủ đề không? (AD-08, AD-09, AD-10)

## Bước 3: Lượt đạo diễn

Đối chiếu với `shared/nghe/ngon-ngu-dien-anh.md` mục 10.

- Beat nào chỉ có thoại? (DA-01)
- Câu thoại nào kể điều hình kể được? (DA-02)
- Cỡ cảnh có thay đổi theo cảm xúc không? (DA-03)
- Âm thanh, ánh sáng có cụ thể và mang nghĩa không? (DA-04)
- Có khoảnh khắc lặng, có đặc tả đồ vật ẩn dụ không? (DA-05, DA-06)
- Biểu cảm có quay được không? (DA-07)

## Bước 4: Lượt đội sản xuất

Đối chiếu với `shared/luat/dieu-kien-san-xuat.md` mục 5. Hình dung **người quay đọc kịch bản này đêm trước buổi quay**:

- Cảnh nào cần hai máy, hoặc thiết bị không có? (SX-02)
- Hành động nào không lặp lại được mà phải quay nhiều góc? (SX-04)
- Đạo cụ có đủ trong danh sách không? (SX-05)
- Hiệu ứng dựng có được viết ra không? (SX-06)
- Số người, số bối cảnh có hợp lý không? (SX-01, SX-03, SX-07)
- Có quá 1 nhân vật nữ lộ mặt hoặc quá 5 nhân vật nam không? (SX-09)
- Cộng giây các beat (hoặc ước theo thoại): có lệch mục tiêu trên 10% không? (SX-08)

## Bước 5: Lượt nền tảng

Đối chiếu với `shared/luat/vung-cam.md`: mục cấm hẳn (AT-01), mục hạn chế (AT-02). Series thì đối chiếu thêm với
`series.md` (SR-01, SR-02, SR-03).

## Bước 6: Gom và viết lỗi

Mỗi lỗi một dòng, đủ sáu phần:

| Phần | Cách viết |
|---|---|
| **Mã** | Mã trong danh mục. Không có mã phù hợp thì `MOI-<n>` |
| **Mức** | Mức mặc định; nâng / hạ một bậc phải ghi lý do |
| **Vị trí** | `KB<số> beat <n>` + giây nếu có |
| **Trích** | Nguyên văn đoạn có vấn đề, ngắn |
| **Vấn đề** | Vì sao đây là vấn đề với người xem / người quay. Một câu |
| **Gợi ý sửa** | Viết sẵn câu thoại, hành động hay ghi chú thay thế. Không viết "nên hay hơn", "cần cải thiện" |

Luật gom:

- Cùng một nguyên nhân xuất hiện ở nhiều beat thì gộp thành một lỗi, vị trí ghi các beat.
- Lỗi cấu trúc (ảnh hưởng nhiều beat) ghi rõ "cấu trúc" ở cột Vấn đề, để người sửa biết phải dàn lại.
- Vòng review lại: với mỗi lỗi cũ, ghi **Đã sửa / Sửa chưa đạt / Chưa sửa**. Lỗi mới phát sinh do lần sửa thì ghi
  "phát sinh khi sửa".

## Bước 7: Chấm điểm

Theo bảng ở `loi-kich-ban.md` mục 3. Mỗi tiêu chí:

- Chấm 1–10, so với ba mốc (2 / 6 / 10) của bảng.
- Ghi **một câu lý do** có dẫn tới beat cụ thể.
- Điểm phải nhất quán với bảng lỗi: còn HK-01 thì tiêu chí Hook không quá 4; còn SX-02 thì "Quay được" không quá 4.

Kết luận **ĐẠT** khi không còn lỗi Nặng **và** điểm tổng ≥ 8. Ngược lại là **CHƯA ĐẠT**.

## Bước 8: Điểm mạnh nên giữ

Ghi 2–4 điều làm tốt, có vị trí cụ thể. Mục này để người sửa không phá mất cái hay. Không ghi khen chung chung.

---

## Đầu ra: `03-review-vN.md`

```markdown
# Review kich-ban-vN: <tên>

**Kết luận: ĐẠT | CHƯA ĐẠT** · Điểm <x.x>/10 · <n> Nặng · <n> Vừa · <n> Nhẹ
**Vấn đề lớn nhất (một câu):** <…>

## Soát cấu trúc (kich_ban.py kiem)
<dán nguyên kết quả>

## Lỗi
| # | Mã | Mức | Vị trí | Trích | Vấn đề | Gợi ý sửa |
|---|----|-----|--------|-------|--------|-----------|

## Kiểm lỗi vòng trước (vòng 2 trở đi)
| Mã cũ | Vị trí | Trạng thái | Ghi chú |

## Điểm
| Tiêu chí | Trọng số | Điểm | Lý do |
|---|---|---|---|
| **Tổng** | | **x.x** | |

## Điểm mạnh nên giữ
- <vị trí>: <điều làm tốt>

## Kết đoán ở giữa kịch bản
<ghi lại điều người review đoán ở bước 2, và có trúng không>

## Mã lỗi mới đề xuất (nếu có)
| Mã tạm | Mức | Lỗi | Dấu hiệu | Hướng sửa |
```

Một file JSON có nhiều kịch bản thì mỗi kịch bản một mục kết luận, bảng lỗi và bảng điểm riêng.

## Không làm

- Không sửa file kịch bản.
- Không viết lại toàn bộ kịch bản. Mọi gợi ý gắn với một lỗi cụ thể.
- Không chấm ĐẠT khi còn lỗi Nặng.
- Không đề xuất concept khác, không thêm việc ngoài bảng lỗi.
- Không chấm theo phong cách tham khảo khi brief không ghi tham khảo.
