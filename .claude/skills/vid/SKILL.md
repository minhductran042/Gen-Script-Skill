---
name: vid
description: "Cửa vào duy nhất của bộ skill kịch bản video ngắn dọc (TikTok / YouTube Shorts) mang chất điện ảnh, tuyến ẩn dụ hài đời thường, khán giả 17–30. Gọi trống thì hiện menu (làm video mới, làm tiếp dự án dở, mổ video mẫu, review kịch bản có sẵn, lên series); có đối số thì tự chọn hướng: câu ý tưởng → làm video mới; link / file video → phân tích mẫu rồi làm theo; du-an/... hoặc 'tiếp' → làm tiếp; file .xlsx / .json → review; 'series' → lên series. Luồng làm video: chốt brief một lượt hỏi, brainstorm, chọn concept bằng thẻ xem trước, viết kịch bản theo format Excel của team (mỗi kịch bản một sheet có tổng quan), review bằng agent độc lập, sửa tối đa 2 vòng (chế độ nhanh 1 vòng), duyệt, xuất Excel kèm gói bàn giao. Làm được nhiều video một lượt. Giữ trạng thái để làm tiếp. Dùng khi user gõ /vid, nói 'làm kịch bản', 'có ý tưởng video', 'làm video từ mẫu này', 'làm theo video <link>', 'theo mẫu <tên>', 'làm 3 video về …', 'làm nhanh', 'tiếp tục kịch bản'."
argument-hint: "[ý tưởng | link / file video mẫu | theo mẫu <tên> | du-an/<thư mục> | tiếp | file kịch bản | series …] [nhanh]"
---

# /vid: cửa vào và điều phối

Skill này không tự sáng tác. Nó hiểu người dùng muốn gì, chốt đầu vào, gọi đúng skill ở từng bước, giữ hai điểm dừng
cho người dùng quyết, và gói đầu ra cho đội quay. Các skill con (`vid-brainstorm`, `vid-viet-kich-ban`, `vid-review`,
`vid-series`, `vid-phan-tich-mau`) vẫn gọi thẳng được khi người dùng chỉ cần một việc.

## Bản đồ

```
/vid ─→ [Cửa vào] chọn hướng (bước 0.0) ─→ review / series / mổ mẫu: giao skill con rồi dừng
                                       └─→ làm video mới / làm tiếp:
(có video mẫu?) ── có ──→ [0a] vid-phan-tich-mau (agent) ─ mau/<k>/phan-tich.md
      │ không: bỏ qua, không hỏi gì về mẫu          │
      ▼                                              ▼
[0] Brief ──────────── 00-brief.md
      │  thiếu thông tin → hỏi MỘT lượt (có mẫu thì gộp câu hỏi về mẫu vào lượt này)
[1] vid-brainstorm ─── 01-concepts.md
      │
   ⏸ Người dùng chọn concept
      │
[2] vid-viet-kich-ban ─ kich-ban-v1.json → kiem → kich-ban-v1.xlsx
      │
[3] vid-review (agent độc lập) ─ 03-review-v1.md
      │
   ĐẠT? ── không ──→ [4] sửa → v2 → [3]   (tối đa 2 vòng sửa; chế độ nhanh 1 vòng)
      │ có
   ⏸ Người dùng duyệt
      │
[5] Xuất ─ kich-ban-final.xlsx (mỗi kịch bản một sheet) + 05-ban-giao.md
```

Ngoài hai điểm dừng, không chen câu hỏi nào khác. Mọi câu hỏi về đầu vào gom trong một lượt ở bước 0.3.

Mọi file của một dự án nằm trong `du-an/<YYYY-MM-DD>-<slug>/`. `slug` là tên ngắn không dấu, nối bằng gạch ngang.

## Kiến thức dùng

Luôn đọc:
- `shared/cau-hinh.md`: sở thích mặc định của team; mục nào có ở đây thì không hỏi lại.
- `shared/luat/dieu-kien-san-xuat.md`: để biết brief nào làm được.
- `shared/nghe/khan-gia-va-nen-tang.md`: để chốt nhóm khán giả và nền tảng trong brief.
- `shared/nghe/chu-de-va-thong-diep.md`: để chốt nhóm chủ đề, thông điệp, và xử lý đầu vào chưa rõ.

Không đọc `shared/tham-khao/`, trừ khi brief ghi ở mục "Tham khảo". Các skill con tự đọc phần nghề của mình.

## Máy mới

Không bắt người dùng cài gì. Các script tự cài thứ còn thiếu vào `.cong-cu/venv` ở lần đầu (`kich_ban.py`: openpyxl;
`phan_tich_mau.py`: công cụ video). Lần đầu thấy dòng "Lần đầu: …" thì báo người dùng một dòng là đang tự cài.
Máy không có cả `py` lẫn `python3`: cài Python theo bước 0 của `vid-phan-tich-mau` rồi chạy lại lệnh vừa lỗi.

---

## Bước 0: Cửa vào và brief

### 0.0. Chọn hướng

Đọc đối số và lời người dùng theo thứ tự dưới; khớp dòng nào trước thì đi hướng đó. **Có đối số thì không hiện menu.**

| Đầu vào | Hướng |
|---|---|
| Trống (chỉ gõ `/vid`) | Hiện **menu** (dưới) |
| Thư mục `du-an/...` có `trang-thai.md`, hoặc "tiếp", "làm tiếp", "tiếp tục <tên>" | **Làm tiếp** (0.1) |
| File `.xlsx` / `.json` kịch bản, hoặc "review kịch bản này" | Giao `vid-review` (chạy bằng agent như bước 3), báo kết quả, dừng |
| "series", "nhiều tập", "lên khung series" | Giao `vid-series`, dừng |
| Link / file video mà người dùng nói "chỉ phân tích", "mổ video", "video này hay ở đâu" | Giao `vid-phan-tich-mau` chế độ độc lập, dừng |
| Link / file video kèm ý muốn làm video, hoặc "theo mẫu <tên>" | **Làm video mới có mẫu** (0.1a) |
| Câu ý tưởng / chủ đề, hoặc "làm <n> video về …" | **Làm video mới** (0.2) |

Thêm chữ **"nhanh"** ở bất kỳ hướng làm video nào thì bật chế độ nhanh (0.5).

**Menu khi gọi trống.** Trong Claude Code dùng câu hỏi có nút bấm; nơi không có nút bấm thì in danh sách đánh số và chờ
người dùng gõ số.

```
Bạn muốn làm gì?
1. Làm video mới      – có ý tưởng, chủ đề, hoặc để mình gợi ý
2. Làm tiếp dự án dở  – <tên dự án mới nhất> đang ở bước <X>   (chỉ hiện khi có dự án dở)
3. Mổ video mẫu       – dán link / file, xem vì sao video đó thu hút
4. Review kịch bản    – đưa file kịch bản có sẵn
(lựa chọn "Khác" luôn có: lên series, hoặc gõ tự do)
```

Chọn 1 mà chưa có ý tưởng thì đi tiếp vào 0.2; câu hỏi chủ đề nằm trong lượt hỏi 0.3, không hỏi riêng.

### 0.1. Làm tiếp

1. Tìm mọi `du-an/*/trang-thai.md` có `bước:` khác `xong`, xếp theo dòng `cập nhật:` mới nhất trước.
2. Người dùng nêu tên hoặc chỉ có một dự án dở: mở luôn. Nhiều dự án: hiện tối đa 4 dự án mới nhất thành nút bấm, mỗi
   nút ghi `<tên> · bước <X> · <ngày cập nhật>`.
3. Báo một dòng "đang ở bước X", rồi nhảy thẳng tới bước đó. Không có dự án dở nào thì báo một dòng và hiện menu.

### 0.1a. Video mẫu (chỉ khi người dùng đưa)

Nhận ra mẫu khi lời người dùng có: link video (tiktok.com, youtube.com, youtu.be, facebook.com, fb.watch,
instagram.com), đường dẫn file `.mp4` / `.mov`, ảnh chụp kèm câu "làm theo video này", hoặc "theo mẫu <tên>".
**Không có thì bỏ qua cả mục này**, không hỏi người dùng có mẫu không.

| Đầu vào | Làm gì |
|---|---|
| "theo mẫu <tên>" | Đọc `shared/tham-khao/mau/INDEX.md`, lấy `shared/tham-khao/mau/<slug>.md`. Không phân tích lại |
| Link / file (1–3 mẫu) | Gọi agent phân tích (dưới), mỗi mẫu ghi vào `du-an/<dự án>/mau/<k>/` |
| Ảnh chụp / mô tả | Như trên; agent tự chạy tầng 3 của `vid-phan-tich-mau` |

Báo người dùng một dòng "đang phân tích video mẫu" (lần đầu trên máy: "lần đầu cài công cụ và tải mô hình, khoảng 15
phút"; từ lần sau khoảng nửa phút cho video 20 giây). Gọi công cụ **Agent**
(subagent_type `general-purpose`) để ảnh và lời thoại của mẫu không chiếm ngữ cảnh phiên chính. Nhiều mẫu thì một agent
mỗi mẫu, gọi song song; xong thì một lượt nữa viết `tong-hop.md`.

```
Chạy skill vid-phan-tich-mau (.claude/skills/vid-phan-tich-mau/SKILL.md) cho <link | file>, chế độ trong luồng, ghi
vào du-an/<dự án>/mau/<k>/. Không hỏi người dùng; thiếu dữ liệu thì xuống tầng thấp hơn và ghi rõ trong phan-tich.md.

Xong khi: phan-tich.md đủ 10 mục theo khuôn, qua hết checklist bước 4 của skill; trả lại đúng khối "Báo người dùng"
ở bước 5.

Không làm: không brainstorm, không viết kịch bản, không ghi vào shared/, không lưu thư viện mẫu, không sửa
00-brief.md.
```

Agent lỗi hẳn (không tải, không cài được, không có ảnh): báo người dùng một dòng và đề nghị gửi file `.mp4` hoặc ảnh
chụp; người dùng bỏ qua thì đi tiếp không mẫu.

### 0.2. Điền brief

Tạo `du-an/<YYYY-MM-DD>-<slug>/`. Điền `00-brief.md` theo khung dưới. Với từng mục theo thứ tự: **suy ra được** từ lời
người dùng thì điền và đánh dấu `(suy ra)`; có trong **`shared/cau-hinh.md`** thì điền và đánh dấu `(cấu hình)`; có
**mặc định** trong khung thì điền và đánh dấu `(mặc định)`; còn lại thì đưa vào danh sách hỏi.

"Làm <n> video về …": ghi `Số video: <n>` ở mục "Số concept muốn nhận". Mỗi video sẽ là một kịch bản trong cùng file
JSON và một sheet trong cùng file Excel.

```markdown
# Brief: <tên tạm>

## Đầu vào gốc
<nguyên văn ý tưởng / mô tả video mẫu người dùng đưa>

## Định hướng
- Nhóm chủ đề: Tình yêu | Gia đình | Công việc / học hành | Bạn bè | Mạng xã hội | Tâm lý, nội tâm | Ước mơ | Xã hội
  (xem nghe/chu-de-va-thong-diep.md mục 2; có thể ghép hai nhóm)
- Chủ đề con: <…>
- Vấn đề / cảm xúc muốn chạm: <…>
- Thông điệp muốn lồng (nếu có): <một câu, dạng phát hiện>
- Câu chuyện bề mặt (nếu người dùng đã có): <…>
- Nhóm khán giả chính: 17–21 | 22–25 | 26–30 (xem nghe/khan-gia-va-nen-tang.md mục 1)
- Tông: ẩn dụ hài đời thường (mặc định) | chạm nhiều hơn hài | hài thuần | <khác>
- Dạng: độc lập (mặc định) | tập <n> của series <tên>
- Thời lượng mục tiêu: <30s | 60s | 90s>
- Nền tảng: TikTok + YouTube Shorts (mặc định)

## Ràng buộc của lần này
- Nhân vật / diễn viên chỉ định: <…>
- Bối cảnh muốn dùng / phải tránh: <…>
- Đạo cụ có sẵn muốn tận dụng: <…>
- Điều không muốn có: <…>

## Tham khảo (tuỳ chọn)
không | <file trong shared/tham-khao/> | <kịch bản người dùng đưa kèm>
- Video mẫu: <du-an/<dự án>/mau/<k>/phan-tich.md | shared/tham-khao/mau/<slug>.md | không>
- Học từ mẫu: <hook | cấu trúc, nhịp | ẩn dụ, thông điệp | điện ảnh | giọng hài | cả công thức>
- Mức bám: <Cảm hứng | Cùng công thức (mặc định) | Bắt trend> (xem shared/luat/bam-mau.md)

## Chế độ
đầy đủ (mặc định) | nhanh

## Số concept muốn nhận
<mặc định 6; chế độ nhanh 3> · Số video: <mặc định 1>
```

### 0.3. Hỏi một lượt

**Một lượt, tối đa 4 câu.** Trong Claude Code dùng câu hỏi có nút bấm (mỗi câu 2–4 lựa chọn, lựa chọn khuyên dùng đặt
đầu và ghi "(khuyên dùng)"); nơi không có nút bấm thì in câu hỏi đánh số, mỗi câu kèm gợi ý trả lời.

Các câu có thể cần hỏi, **xếp theo ưu tiên**. Lấy từ trên xuống tới đủ 4 câu; câu nào đã suy ra được, đã có trong
cấu hình, hoặc người dùng đã nói sẵn thì bỏ qua.

| Ưu tiên | Câu | Khi nào cần |
|---|---|---|
| 1 | Thời lượng: 30s · 60s · 90s | Không suy ra được, không có trong cấu hình, không có mẫu để theo |
| 2 | Nhóm chủ đề: 8 nhóm chia hai câu chọn nhiều, mỗi câu 4 nhóm (tính là 2 câu) | Hoàn toàn không có chủ đề (xem `chu-de-va-thong-diep.md` mục 3; các trường hợp khác tự đề xuất, ghi `(đề xuất)`) |
| 3 | Mức bám mẫu: Cùng công thức (khuyên dùng) · Cảm hứng · Bắt trend, mỗi lựa chọn một dòng giải thích từ `bam-mau.md` mục 1 | Có video mẫu |
| 4 | Học gì từ mẫu (chọn nhiều): hook · cấu trúc, nhịp · ẩn dụ, thông điệp · điện ảnh, giọng hài | Có video mẫu |
| 5 | Nhóm khán giả: 17–21 · 22–25 · 26–30 · cả ba | Không suy ra được, không có trong cấu hình |

Câu không được hỏi vì đã đủ 4: dùng giá trị khuyên dùng hoặc mặc định, ghi `(mặc định)` trong brief, và nhắc một dòng
"đã dùng mặc định cho <…>, sửa thì nói".

- **Không hỏi** các mục có mặc định trong khung (tông, nền tảng, dạng).
- **Không hỏi về tham khảo**, không hỏi có video mẫu không. Người dùng không nhắc thì ghi "không".
- **Có video mẫu**: trước lượt hỏi, đưa người dùng khối "Báo người dùng" của agent phân tích. Brief lấy từ bản phân tích
  những gì suy ra được, ghi `(theo mẫu)`: thời lượng (mẫu dài bao nhiêu thì đề xuất bấy nhiêu), nhóm chủ đề, nhóm khán
  giả, tông. Câu "lưu vào thư viện mẫu" **không** hỏi ở đây mà hỏi ở bước 5.
- Không còn câu nào cần hỏi: không hỏi gì, in tóm tắt brief một đoạn và đi thẳng vào bước 1.

Brief có series mà `du-an/<series>/series.md` chưa có: dừng và đề nghị chạy `vid-series` trước.

### 0.4. Ghi trạng thái

`trang-thai.md`:

```markdown
bước: 1-brainstorm
cập nhật: <YYYY-MM-DD HH:mm>
chế độ: đầy đủ | nhanh
concept đã chọn:
phiên bản kịch bản hiện tại:
số vòng sửa đã dùng: 0
```

Cập nhật file này sau **mỗi** bước. Bước 0.1 dựa vào dòng `bước:` và `cập nhật:` để tìm dự án dở.

### 0.5. Chế độ nhanh

Chỉ bật khi người dùng nói rõ ("nhanh", "làm nhanh", "không cần kỹ"). Không tự bật vì brief đơn giản.

| Bước | Đầy đủ | Nhanh |
|---|---|---|
| Brainstorm | ≥ 15 ý thô, 5–8 concept | ≥ 8 ý thô, 3 concept (vẫn giữ một concept "liều" nếu có ý đủ lạ) |
| Review | Agent độc lập | Agent độc lập (không bỏ) |
| Vòng sửa tối đa | 2 | 1 |

Hai điểm dừng vẫn giữ nguyên. Báo một dòng ở đầu: "chế độ nhanh: ít concept hơn, sửa tối đa 1 vòng".

### Dòng gợi ý lệnh tắt

Cuối mỗi điểm dừng in **một dòng** gợi ý, không giải thích thêm, ví dụ ở điểm dừng 1:
`Gợi ý: "C2" · "C1 + C3" · "ghép hook C2 + ẩn dụ C4" · "nghĩ lại, hài hơn" · "xem thêm" · "trạng thái"`.
Người dùng nói câu tự nhiên khác cũng xử lý như thường; không cần khớp đúng lệnh.

---

## Bước 1: Brainstorm

Gọi skill `vid-brainstorm` với `00-brief.md`, nhận `01-concepts.md`.

### ⏸ Điểm dừng 1: chọn concept

Không đưa nguyên `01-concepts.md`. Đưa **3 concept điểm cao nhất** thành câu hỏi có nút bấm, mỗi lựa chọn kèm **thẻ xem
trước** (mục "Thẻ xem trước" trong `01-concepts.md`, 6 dòng). Lựa chọn thứ 4 là "Xem thêm / ghép / nghĩ lại". Số video
lớn hơn 1 thì cho chọn nhiều. Nơi không có nút bấm: in bảng tóm tắt ở đầu `01-concepts.md` và chờ người dùng gõ.

| Người dùng chọn / nói | Làm gì |
|---|---|
| Một concept | Sang bước 2 |
| Nhiều concept, hoặc brief có "Số video: n" | Mỗi concept là một kịch bản trong cùng file JSON (`so` = 1, 2, 3…), sau này là một sheet trong cùng file Excel; viết lần lượt, review chung một lượt |
| "Xem thêm" | Đưa bảng tóm tắt đầy đủ (mọi concept), rồi hỏi lại |
| Ghép hai concept ("hook của C2 + ẩn dụ của C4") | Ghi concept ghép vào `01-concepts.md` mục "Concept ghép", rồi sang bước 2 |
| "Nghĩ lại theo hướng …" | Thêm hướng mới vào brief mục "Định hướng", chạy lại bước 1, giữ bản cũ thành `01-concepts-lan1.md` |
| Sửa một concept | Sửa trong `01-concepts.md`, rồi sang bước 2 |

Không tự chọn thay người dùng. Cuối điểm dừng in dòng gợi ý lệnh tắt.

---

## Bước 2: Viết kịch bản

Gọi `vid-viet-kich-ban` (chế độ viết mới) với brief + concept được chọn. Nhận về `kich-ban-v1.json` (đã qua `kiem`) và
`kich-ban-v1.xlsx`.

---

## Bước 3: Review độc lập

Gọi công cụ **Agent** (subagent_type `general-purpose`). Không review trong phiên đang viết: người viết tự chấm bài
mình thường chấm dễ và không thấy lỗ hổng của chính mình.

Prompt giao cho agent:

```
Chạy skill vid-review cho du-an/<dự án>/kich-ban-vN.json, ghi du-an/<dự án>/03-review-vN.md.

Được đọc: kịch bản, du-an/<dự án>/00-brief.md, shared/luat/, shared/nghe/, và file tham khảo mà brief ghi ở mục
"Tham khảo" (nếu có), kể cả phan-tich.md của video mẫu. Không đọc 01-concepts.md, các bản review trước, và mọi file
khác trong du-an/.
Không hỏi người dùng.

Xong khi: mọi beat đã đi qua đủ năm lượt đọc trong vid-review; mọi lỗi có mã, mức, vị trí, trích dẫn và gợi ý sửa viết
sẵn; có bảng điểm từng tiêu chí và kết luận ĐẠT / CHƯA ĐẠT.

Không làm: không sửa file kịch bản, không viết lại cả kịch bản, không đề xuất concept khác, không thêm việc ngoài bảng lỗi.
```

Vòng review thứ hai trở đi: cho agent đọc thêm `sua-v(N-1).md` để kiểm các lỗi cũ đã được sửa thật chưa.

Nhiều kịch bản trong một file: **một** agent review cả lô, báo cáo chia mục theo từng kịch bản, mỗi kịch bản một kết luận
ĐẠT / CHƯA ĐẠT riêng. Vòng sửa chỉ áp cho kịch bản CHƯA ĐẠT.

---

## Bước 4: Sửa

| Kết luận review | Làm gì |
|---|---|
| ĐẠT | Sang điểm dừng 2 |
| CHƯA ĐẠT, số vòng sửa < mức tối đa (2; chế độ nhanh 1) | Gọi `vid-viet-kich-ban` chế độ sửa với `03-review-vN.md`, nhận `kich-ban-v(N+1).json` và `sua-vN.md`, rồi quay lại bước 3 |
| CHƯA ĐẠT, đã sửa đủ số vòng tối đa | **Dừng.** Đưa người dùng: điểm hiện tại, các lỗi còn lại, và một câu nhận định lỗi nằm ở kịch bản hay ở concept. Người dùng quyết: sửa tiếp, đổi concept, hay chấp nhận |

Sửa mà điểm giảm so với vòng trước thì báo người dùng và đề nghị quay lại bản điểm cao hơn.

---

## Bước 5: Duyệt và bàn giao

### ⏸ Điểm dừng 2: duyệt

Đưa người dùng:

- đường dẫn `kich-ban-vN.xlsx`;
- điểm và kết luận của lần review cuối; nhiều kịch bản thì một bảng `| Kịch bản | Điểm | Kết luận | Lỗi còn lại |`;
- các lỗi Nhẹ còn lại (nếu có), mỗi lỗi một dòng.

Duyệt bằng nút bấm: **Duyệt, xuất bản cuối** (khuyên dùng) · **Sửa thêm** · **Đổi concept**. Nhiều kịch bản thì duyệt
một lần cho cả lô; người dùng muốn bỏ kịch bản nào thì nói tên. Cuối điểm dừng in dòng gợi ý lệnh tắt, ví dụ
`Gợi ý: "duyệt" · "sửa beat 3 KB2: …" · "review lại" · "bỏ KB3"`.

Người dùng sửa trực tiếp nội dung thì cập nhật JSON (không sửa tay Excel), chạy `kiem`, và hỏi có cần review lại không.

Dự án có video mẫu mà bản phân tích chưa nằm trong thư viện: sau khi duyệt, hỏi một câu "Lưu bản phân tích video mẫu
vào thư viện để lần sau gọi 'theo mẫu <tên>' không?" (Có · Không). Có thì làm theo mục Thư viện của `vid-phan-tich-mau`.

### Xuất bản cuối

```
py -I shared/scripts/kich_ban.py xuat du-an/<dự án>/kich-ban-vN.json du-an/<dự án>/kich-ban-final.xlsx
```

### Gói bàn giao `05-ban-giao.md`

Viết từ JSON bản cuối, để người quay và người dựng dùng ngay:

```markdown
# Bàn giao: <tên>

## Tổng quan
- Thời lượng mục tiêu · Số nhân vật · Bối cảnh

## Diễn viên và vai
| Vai | Số beat xuất hiện | Có thoại không | Ghi chú diễn |

## Đạo cụ (gộp mọi kịch bản)
| Đạo cụ | Số lượng | Dự phòng | Dùng ở beat |

## Thứ tự quay đề xuất
Gom theo bối cảnh, rồi theo góc máy, để một máy quay đỡ phải đổi chỗ:
| Lượt | Bối cảnh | Góc | Beat | Diễn viên cần có mặt | Ghi chú (quay một lần / ghép) |

## Cảnh chèn quay riêng (không cần diễn viên chính)
| Đặc tả | Beat | Ghi chú ánh sáng |

## Ghi chú cho người dựng
| Beat | Hiệu ứng / chữ / nhạc / tắt lặng | Mốc giây |
```

Ghi `trang-thai.md`: `bước: xong`.

---

## Không làm

- Không bỏ qua hai điểm dừng, kể cả ở chế độ nhanh.
- Không sửa quá số vòng tối đa (2; chế độ nhanh 1) khi chưa hỏi người dùng.
- Không hỏi quá một lượt 4 câu ở bước brief; không chen câu hỏi ngoài hai điểm dừng.
- Không tự bật chế độ nhanh.
- Không hiện menu khi người dùng đã đưa đối số.
- Không sửa tay file `.xlsx`. Sửa JSON rồi xuất lại.
- Không đọc `shared/tham-khao/` khi brief không ghi.
- Không hỏi người dùng có video mẫu không; chỉ xử lý mẫu khi người dùng tự đưa.
- Không phân tích video mẫu trong phiên chính; giao agent chạy `vid-phan-tich-mau`.
- Không lấy nội dung trong `shared/mau-format/` làm ý tưởng.
