---
name: vid-flow
description: "Quy trình trọn gói làm kịch bản video ngắn dọc (TikTok / YouTube Shorts) mang chất điện ảnh, tuyến ẩn dụ hài đời thường, khán giả 17–30: chốt brief, brainstorm nhiều concept, người dùng chọn, viết kịch bản theo format Excel của team, review bằng agent độc lập theo bảng lỗi có mã, sửa tối đa 2 vòng, người dùng duyệt, rồi xuất Excel kèm gói bàn giao cho người quay và người dựng (đạo cụ, thứ tự quay gom theo bối cảnh, cảnh chèn, ghi chú dựng). Giữ trạng thái để làm tiếp lần sau. Đưa kèm link / file video mẫu (tuỳ chọn) thì tự phân tích mẫu bằng vid-phan-tich-mau rồi viết theo công thức của mẫu ở mức bám người dùng chọn. Dùng khi user nói 'làm kịch bản', 'có ý tưởng video', 'lên kịch bản từ ý tưởng này', 'làm video từ mẫu này', 'làm theo video <link>', 'theo mẫu <tên>', 'tiếp tục kịch bản <dự án>'. Chỉ mổ video mẫu, không viết kịch bản, thì dùng vid-phan-tich-mau. Chỉ brainstorm thì dùng vid-brainstorm; chỉ review kịch bản có sẵn thì dùng vid-review; lên khung nhiều tập thì dùng vid-series."
argument-hint: <ý tưởng> [link / file video mẫu | theo mẫu <tên>] | du-an/<thư mục> để tiếp tục
---

# Điều phối: từ ý tưởng tới kịch bản quay được

Skill này không tự sáng tác. Nó chốt đầu vào, gọi đúng skill ở từng bước, giữ hai điểm dừng cho người dùng quyết, và
gói đầu ra cho đội quay.

## Bản đồ

```
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
   ĐẠT? ── không ──→ [4] sửa → v2 → [3]   (tối đa 2 vòng sửa)
      │ có
   ⏸ Người dùng duyệt
      │
[5] Xuất ─ kich-ban-final.xlsx + 05-ban-giao.md
```

Mọi file của một dự án nằm trong `du-an/<YYYY-MM-DD>-<slug>/`. `slug` là tên ngắn không dấu, nối bằng gạch ngang.

## Kiến thức dùng

Luôn đọc:
- `shared/luat/dieu-kien-san-xuat.md`: để biết brief nào làm được.
- `shared/nghe/khan-gia-va-nen-tang.md`: để chốt nhóm khán giả và nền tảng trong brief.
- `shared/nghe/chu-de-va-thong-diep.md`: để chốt nhóm chủ đề, thông điệp, và xử lý đầu vào chưa rõ.

Không đọc `shared/tham-khao/`, trừ khi brief ghi ở mục "Tham khảo". Các skill con tự đọc phần nghề của mình.

---

## Bước 0: Chốt brief

### 0.1. Làm tiếp hay làm mới

- Đối số là thư mục `du-an/...` đã có, hoặc người dùng nói "tiếp tục <tên>": đọc `trang-thai.md`, báo người dùng một
  dòng "đang ở bước X", rồi nhảy thẳng tới bước đó.
- Ngược lại thì tạo thư mục mới.

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

Điền `00-brief.md` theo khung dưới. Với từng mục: **suy ra được** từ lời người dùng thì điền và đánh dấu `(suy ra)`; có
**mặc định** thì điền mặc định; còn lại thì đưa vào danh sách hỏi.

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

## Số concept muốn nhận
<mặc định 6>
```

### 0.3. Hỏi một lần

- **Bắt buộc phải có**: thời lượng mục tiêu. Không suy ra được thì hỏi.
- **Đầu vào chưa rõ chủ đề / câu chuyện / thông điệp**: xử lý theo bảng ở `shared/nghe/chu-de-va-thong-diep.md`
  mục 3. Chỉ trường hợp "không có chủ đề" mới đưa bảng 8 nhóm để hỏi; các trường hợp còn lại tự đề xuất, ghi `(đề xuất)`.
- **Không hỏi** các mục có mặc định. Ghi mặc định và để người dùng sửa nếu muốn.
- **Không hỏi về tham khảo.** Người dùng không nhắc thì ghi "không".
- **Có video mẫu** thì brief lấy từ bản phân tích những gì suy ra được, ghi `(theo mẫu)`: thời lượng (mẫu dài bao
  nhiêu thì đề xuất bấy nhiêu), nhóm chủ đề, nhóm khán giả, tông. Đưa người dùng khối "Báo người dùng" của agent, rồi
  gộp vào cùng lượt hỏi (trong Claude Code dùng câu hỏi có nút bấm):
  1. Học gì từ mẫu (chọn nhiều): hook · cấu trúc, nhịp · ẩn dụ, thông điệp · điện ảnh, giọng hài.
  2. Mức bám: Cùng công thức (khuyên dùng) · Cảm hứng · Bắt trend. Mỗi lựa chọn kèm một dòng giải thích lấy từ
     `bam-mau.md` mục 1.
  3. Lưu bản phân tích vào thư viện mẫu để lần sau gọi "theo mẫu <tên>" không: Có · Không. Có thì làm theo mục
     Thư viện của `vid-phan-tich-mau`.
  Người dùng đã nói sẵn ("học cái hook thôi", "làm kiểu trend này") thì không hỏi lại câu đó.
- Mọi câu hỏi gộp trong **một** tin nhắn, đánh số, mỗi câu kèm gợi ý trả lời.

Brief có series mà `du-an/<series>/series.md` chưa có: dừng và đề nghị chạy `vid-series` trước.

### 0.4. Ghi trạng thái

`trang-thai.md`:

```markdown
bước: 1-brainstorm
cập nhật: <YYYY-MM-DD HH:mm>
concept đã chọn:
phiên bản kịch bản hiện tại:
số vòng sửa đã dùng: 0
```

Cập nhật file này sau **mỗi** bước.

---

## Bước 1: Brainstorm

Gọi skill `vid-brainstorm` với `00-brief.md`, nhận `01-concepts.md`.

### ⏸ Điểm dừng 1: chọn concept

Đưa người dùng **bảng tóm tắt** ở đầu `01-concepts.md`, không đưa nguyên file. Người dùng có thể:

| Người dùng nói | Làm gì |
|---|---|
| Chọn một concept | Sang bước 2 |
| Chọn nhiều concept | Mỗi concept là một kịch bản trong cùng file JSON (`so` = 1, 2, 3…), review chung một lượt |
| Ghép hai concept ("hook của C2 + ẩn dụ của C4") | Ghi concept ghép vào `01-concepts.md` mục "Concept ghép", rồi sang bước 2 |
| "Brainstorm lại theo hướng …" | Thêm hướng mới vào brief mục "Định hướng", chạy lại bước 1, giữ bản cũ thành `01-concepts-lan1.md` |
| Sửa một concept | Sửa trong `01-concepts.md`, rồi sang bước 2 |

Không tự chọn thay người dùng.

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

---

## Bước 4: Sửa

| Kết luận review | Làm gì |
|---|---|
| ĐẠT | Sang điểm dừng 2 |
| CHƯA ĐẠT, số vòng sửa < 2 | Gọi `vid-viet-kich-ban` chế độ sửa với `03-review-vN.md`, nhận `kich-ban-v(N+1).json` và `sua-vN.md`, rồi quay lại bước 3 |
| CHƯA ĐẠT, đã sửa 2 vòng | **Dừng.** Đưa người dùng: điểm hiện tại, các lỗi còn lại, và một câu nhận định lỗi nằm ở kịch bản hay ở concept. Người dùng quyết: sửa tiếp, đổi concept, hay chấp nhận |

Sửa mà điểm giảm so với vòng trước thì báo người dùng và đề nghị quay lại bản điểm cao hơn.

---

## Bước 5: Duyệt và bàn giao

### ⏸ Điểm dừng 2: duyệt

Đưa người dùng:

- đường dẫn `kich-ban-vN.xlsx`;
- điểm và kết luận của lần review cuối;
- các lỗi Nhẹ còn lại (nếu có), mỗi lỗi một dòng.

Người dùng sửa trực tiếp nội dung thì cập nhật JSON (không sửa tay Excel), chạy `kiem`, và hỏi có cần review lại không.

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

- Không bỏ qua hai điểm dừng.
- Không sửa quá 2 vòng khi chưa hỏi người dùng.
- Không sửa tay file `.xlsx`. Sửa JSON rồi xuất lại.
- Không đọc `shared/tham-khao/` khi brief không ghi.
- Không hỏi người dùng có video mẫu không; chỉ xử lý mẫu khi người dùng tự đưa.
- Không phân tích video mẫu trong phiên chính; giao agent chạy `vid-phan-tich-mau`.
- Không lấy nội dung trong `shared/mau-format/` làm ý tưởng.
