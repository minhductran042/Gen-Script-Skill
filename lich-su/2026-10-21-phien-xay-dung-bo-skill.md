# Phiên xây dựng bộ skill kịch bản video ngắn: 2026-10-21

Ghi lại toàn bộ phiên làm việc: lời người dùng (giữ nguyên văn), câu trả lời của trợ lý (tóm tắt đủ ý), các quyết định
đã chốt, file đã tạo, và việc còn treo. Phiên mở trong repo `D:\SotaProject\P6\p6-skills`; bộ skill được dựng ở
`D:\scripts-gen-skills`.

---

## Mục lục

1. Hỏi chung: xây skill cần gì, tổ chức thế nào
2. Ý tưởng bộ skill kịch bản video: cần đưa gì
3. Thiết kế workflow brainstorm → viết → review
4. Dựng bộ skill thô (format Excel + điều kiện sản xuất)
5. Sửa: file Excel chỉ là mẫu format
6. Sửa: tham khảo là tuỳ chọn
7. Viết lại chi tiết (không chép giọng người dùng)
8. Thêm 8 nhóm chủ đề, lồng câu chuyện – thông điệp
9. Brainstorm cách dùng mượt (chưa làm)
10. Tổng hợp quyết định, cấu trúc hiện tại, việc còn treo

---

## 1. Hỏi chung: xây skill cần gì, tổ chức thế nào

**Người dùng:**
> hien tai toi muon tu xay dung 1 skill rieng cho cong viec ca nhan cua minh va toi chua baoh xay 1 bo skill bao gio,
> hien tai trong project nay dang duoc xay rat nhieu skill va 1 so skill su dung kha tot , tôi muốn biết khi xây dựng 1
> skill thì cần những điều kiện gì, tổ chức như thế nào, chia thế nào để xây dựng ra 1 bộ skill tốt

**Trợ lý (tóm tắt):** xem cấu trúc repo p6-skills (43 skill trong `skills/`, agent trong `.claude/agents/`, luật chung
trong `rules/`) rồi trả lời:

- **Skill là gì:** thư mục có `SKILL.md`. Claude đọc `description` để quyết định khi nào gọi, gọi thì nạp toàn bộ
  `SKILL.md`. Skill cá nhân đặt ở `~/.claude/skills/<tên>/`, skill theo project ở `.claude/skills/`.
- **Điều kiện đáng làm skill:** việc lặp lại; có đầu vào / đầu ra rõ ("xong khi nào"); có kiến thức riêng Claude không
  tự biết.
- **Tổ chức một skill:** `SKILL.md` (bắt buộc) + `workflow.md` + `references/` + `scripts/` + `tests/`. Frontmatter
  quan trọng nhất: `name`, `description` (làm gì, câu kích hoạt, khi nào KHÔNG dùng), `argument-hint`. Thân: mục đích,
  dùng / không dùng khi, đầu vào, các bước, tiêu chí xong, cấm làm.
- **Chia nội dung:** quy trình ở `SKILL.md`; luật, mẫu, danh mục lỗi ở `references/`; việc cần chính xác ở `scripts/`;
  luật dùng chung ở `rules/`. `SKILL.md` nên khoảng 100–300 dòng (repo có từ 18 tới 841 dòng).
- **Chia bộ skill:** một skill một việc, một đầu ra; đặt tên theo tiền tố `<dự-án>-<vai>-<việc>`; một skill điều phối
  gọi các skill thành phần; có skill trợ giúp chọn skill khi bộ lớn; tránh chồng chéo (repo có 4 skill sinh testcase).
- **Thứ tự xây:** chọn một việc → làm tay một lần với Claude → viết `SKILL.md` tối giản → thử bằng `/tên` và bằng câu tự
  nhiên → mỗi lần sai thêm vào "bẫy hay gặp" → chỗ không ổn định thì chuyển thành script → có 3–4 skill ổn mới nối.
- Gợi ý skill `anthropic-skills:skill-creator` có sẵn.

---

## 2. Ý tưởng bộ skill kịch bản video: cần đưa gì

**Người dùng:**
> hiện tại tôi đang muốn tạo 1 bộ skill không liên quan đến các phần của repo này mà muốn tạo 1 skill liên quan đến gen
> và brainstorm kịch bản video tiktok cho 1 team để quay video dạng ngắn mang yếu tố điện ảnh, độ tuổi hướng đến từ 17
> đến 30, hành vi sử dụng nền tảng hay hành vi xem video hướng đến là để giải trí, nội dung video có thể chia theo dạng
> series hoặc dạng độc lập, kịch bản thường phải có hook để thu hút, giữ chân người xem ngay từ các giây phút đầu để họ
> xem được đến cuối video, tuyến nội dung đời thường mang tính ẩn dụ hài hước hoặc do input người dùng đưa vào, đa số
> là sẽ đăng lên nền tảng Tiktok Youtube, đầu ra tôi sẽ đưa cho bạn 1 format kịch bản online tôi sẽ đưa cho bạn format
> sau. Bây giờ hãy brainstorm giúp tôi tôi sẽ phải đưa cho bạn gì để xây dựng bộ skill này 1 cách tốt nhất nếu như đầu
> vào tôi đưa cho bạn chỉ là ý tưởng hoặc các video mẫu bạn có thể sáng tạo bắt chước theo 1 cách khác

(Lần đầu bị ngắt giữa chừng; người dùng gửi lại kèm: "tham khảo cách xây dựng các skill đã có".)

**Trợ lý (tóm tắt):** xem `p6-qc-gen-testcase-medix`, `p6-dev-so-ui-ban-ve-medix`, `p6-skill-feedback` và rút cách
làm áp sang được:

| Cách làm trong repo | Áp sang skill kịch bản |
|---|---|
| Khuôn đầu ra cố định | Format kịch bản online |
| Danh mục lỗi có mã từ thực tế | Danh mục "kịch bản hỏng" có mã |
| Tinh hoa rút từ bản tốt | Kho hook, công thức, giọng văn |
| Vòng tự review | Tự chấm theo bảng tiêu chí |
| Thiếu đầu vào thì hỏi, không đoán | Hỏi gộp một lượt |
| Skill điều phối + skill con | Brainstorm → viết → review |
| Vòng feedback | Ghi video viral / flop để cập nhật |

Cần đưa: **bắt buộc**: format + một kịch bản đã điền, 3–5 video chuẩn có bóc tách (trợ lý không xem được video, cần
mô tả theo giây / ảnh chụp / phụ đề), 2–3 video flop, điều kiện sản xuất. **Nên có:** định nghĩa "điện ảnh" của team,
giọng hài và vùng cấm, thông số nền tảng, nhân vật cố định (series), tiêu chí chấm. **Về sau:** số liệu sau đăng.
Đề xuất chia: `vid-brainstorm`, `vid-phan-tich-mau`, `vid-viet-kich-ban`, `vid-review-kich-ban`, `vid-series`,
`vid-shared/references/`. Gói tối thiểu để bắt đầu: format + mẫu, 3 video bóc tách, điều kiện sản xuất, vùng cấm.

---

## 3. Thiết kế workflow brainstorm → viết → review

**Người dùng:**
> tôi muốn đưa việc này thành 1 workflow từ brainstorm, tạo kịch bản, review kịch bản (các phần không ổn, có thể cải
> tiến,... ví dụ nội dung chứa trong đó), thì như nào

**Trợ lý (tóm tắt):** một skill điều phối, các bước truyền nhau bằng file trong thư mục dự án, có điểm dừng cho người
dùng.

```
Ý tưởng → [0 Thu đầu vào] → [1 Brainstorm] → ⏸ chọn concept → [2 Viết] → [3 Review]
→ Đạt? không → [4 Sửa] → [3] (tối đa 2 vòng) → ⏸ duyệt → [5 Xuất + shot list]
```

- Bảng vào / ra / "xong khi" cho từng bước; thư mục `du-an/<ngày>-<ý tưởng>/` với `00-brief.md`, `01-concepts.md`,
  `02-kich-ban-vN`, `03-review-vN`, `05-final`, `trang-thai.md` (checkpoint).
- Review bằng bảng mã lỗi (HK hook, GC giữ chân, AD ẩn dụ, DA điện ảnh, KT kết, SX sản xuất, AT an toàn, SR series),
  mức Nặng / Vừa / Nhẹ, mẫu `03-review-v1.md`, luật dừng: hết lỗi Nặng và điểm ≥ 8, quá 2 vòng thì hỏi người dùng.
- Review bằng **subagent độc lập** (người viết tự chấm thường dễ).
- Khung `SKILL.md` cho skill điều phối. Thứ tự dựng: viết kịch bản → review → brainstorm → ráp.

---

## 4. Dựng bộ skill thô

**Người dùng:**
> D:\scripts-gen-skills "C:\Users\admin\Downloads\Dư Ảnh - Kịch bản Demo.xlsx" xây dựng cho cho tôi bộ skill thô vào
> trong folder trên , format gen ra tôi gửi ở treen , điều kiện sản xuất : bao gồm 9 người: 4 người lên kịch bản, 6
> người diễn, 1 người quay , 2 người dựng video,

**Trợ lý đã làm:**

- Đọc file Excel: 1 sheet "Kịch bản Demo", 3 kịch bản, 10 cột (STT, Tóm tắt - Title, Địa điểm, Mục đích, Nhân vật,
  Nội dung, Biểu cảm, Góc quay, Text nổi bật, Ghi chú). Định dạng: font Google Sans 8 (tên kịch bản đậm), Google Sans
  Text 8 nghiêng, màu `#1F1F1F`, dòng tiêu đề cột nền vàng `#FFFF00`, cột F rộng 32.25, J rộng 11.25, dòng 2 gộp A:Z.
- Dựng 5 skill (`vid-flow`, `vid-brainstorm`, `vid-viet-kich-ban`, `vid-review`, `vid-series`), `CLAUDE.md`,
  `README.md`, `shared/references/`, và script `shared/scripts/kich_ban.py` với ba lệnh:
  - `doc` (xlsx → json), `kiem` (soát cấu trúc, thoát 1 khi có lỗi Nặng), `xuat` (json → xlsx đúng định dạng).
- Chạy thử trên file mẫu: đọc → xuất → đọc lại ra dữ liệu giống hệt (`roundtrip equal: True`). `kiem` bắt 4 lỗi có thật
  trong file: NH-01 (kịch bản 2 beat 1 dán nhầm hook của kịch bản 1), NH-02 (dòng nháp không dấu ở kịch bản 1 beat
  cuối), HK-03 (kịch bản 3 beat 1 thiếu mốc giây), KT-02 (kịch bản 3 beat cuối thiếu Text nổi bật). Heuristic NH-02 đã
  được chỉnh để không bắt nhầm cụm tiếng Anh ("Zoom out ra xa").
- Điều kiện sản xuất: 4 + 6 + 1 + 2 = 13 vị trí > 9 người → có kiêm nhiệm (chưa chốt ai kiêm gì). Hệ quả: tối đa 6
  nhân vật, một máy quay (cảnh chia đôi phải quay tách ghép khi dựng, thoại chốt chữ để diễn lặp từng góc), hai người
  dựng song song.

---

## 5. Sửa: file Excel chỉ là mẫu format

**Người dùng:**
> 3 kich ban trong excel toi gui khong phai la 3 video mẫu đã bóc tách theo khung ở mục 2.A , cai toi gui chi la mau
> format cho ban de sau gen file excel ra, nen khong dung cac mau nay trong phan reference se ghi sau

**Trợ lý đã làm:** đổi `shared/mau/` → `shared/mau-format/`; xoá mọi nội dung rút từ 3 kịch bản khỏi phần tham chiếu
(phong cách, kho hook, giọng hài thành khung trống "CHƯA CÓ"); thay ví dụ trong format bằng chỗ trống `<…>`; bỏ dòng
"Nguồn: mẫu…" trong danh mục lỗi; bỏ các mặc định lấy từ mẫu (60–75s, bối cảnh nháp, tên góc quay). Grep xác nhận
không còn từ nào của nội dung mẫu.

---

## 6. Sửa: tham khảo là tuỳ chọn

**Người dùng:**
> hien tai cac skill dang rat tho va dang ngan, dieu nay co duoc chi tiet hon khong khi toi dua ban day du cac thong
> tin, nho cac reference chi la tham khao, skill khong phai la script nao gen ra cung dua tren cac kich ban do, y toi la
> neu nguoi dung muon thi co the dua tham khao

**Trợ lý đã làm:** tách `shared/references/` thành:

- `shared/luat/`: luôn đọc (format, điều kiện sản xuất, vùng cấm, danh mục lỗi).
- `shared/tham-khao/`: chỉ đọc khi brief ghi ở mục "Tham khảo" (phong cách, kho hook, giọng hài, kèm `README.md` hướng
  dẫn). Không nói gì thì skill không đọc, sáng tác tự do trong khuôn luật.

Trả lời "có chi tiết hơn được không": được, kèm bảng thông tin nào làm sâu phần nào (quy trình team, cách brainstorm,
luật viết từng cột, feedback thật, tiêu chí chấm, số liệu sau đăng, thông tin diễn viên / thiết bị).

---

## 7. Viết lại chi tiết

**Người dùng:**
> hien tai cac skill toi thay duoc viet kha so sai, dac biet la duoc viet theo giong van cua toi, toi chi dua cac phan
> cho ban input de tao ra skill, toi muon duoc mo ta chi tiet, tu brainstorm ra de skill tot hon, vd
> (dán file `yeu-cau-chung.md` 6 dòng)
> ghi ntn y het cua toi, qua so sai

**Trợ lý đã làm:** thêm lớp `shared/nghe/` (kiến thức nghề, luôn dùng) và viết lại toàn bộ, khoảng 1.770 dòng:

| File | Nội dung chính |
|---|---|
| `nghe/khan-gia-va-nen-tang.md` | Ba nhóm tuổi 17–21 / 22–25 / 26–30 (đời sống, nỗi đau, kiểu hài, lý do chia sẻ); "xem để giải trí" nghĩa là gì; 6 hành vi lướt và hệ quả; TikTok vs Shorts, vùng an toàn chữ; độc lập vs series |
| `nghe/hook-va-giu-chan.md` | Hook ba lớp; 12 dạng hook `HK-D01..D12`; luật hook; điểm rơi người xem; 8 kỹ thuật giữ chân; 7 kiểu kết; 3 bài kiểm |
| `nghe/an-du-va-hai.md` | Điểm khớp; 6 kiểu ẩn dụ; 7 tiêu chí; cách tìm ẩn dụ + kho đồ vật 8 bối cảnh; lúc lộ ẩn dụ; 8 cơ chế hài + nhịp hài |
| `nghe/ngon-ngu-dien-anh.md` | Từ vựng cỡ cảnh / góc máy cho khung dọc; chuyển động có động cơ; bố cục; ánh sáng tối thiểu; âm thanh 3 lớp; màu, đạo cụ; nhịp dựng; diễn cho máy cận |
| `nghe/cau-truc-va-nhip.md` | Logline + câu hỏi kịch tính; khung 7 beat; phân bổ giây 30 / 60 / 90s; 6 cấu trúc khác; ước thời lượng; thứ tự cắt |
| `luat/dieu-kien-san-xuat.md` | Hệ quả theo từng vị trí (6 diễn viên, 1 máy quay, 2 dựng, 4 viết); bối cảnh; thiết bị; checklist "quay được" |
| `luat/format-kich-ban.md` | Cách viết từng cột kèm ví dụ kém / tốt; JSON |
| `luat/vung-cam.md` | Cấm hẳn VC-01..07, hạn chế VC-11..17, cách thay thế |
| `luat/loi-kich-ban.md` | 49 mã lỗi (sau mục 8 là 53), bảng chấm có mốc 2 / 6 / 10, trọng số tổng 10 |

Skill:

- `vid-brainstorm`: 5 pha: đào insight → phân kỳ ≥ 15 ý qua 6 lăng kính → hội tụ bằng ma trận 6 tiêu chí (đa dạng,
  một concept "liều") → thẻ concept → tự phản biện.
- `vid-viet-kich-ban`: 8 lượt (xương sống, dàn beat, hình ảnh, thoại, âm thanh, chữ nổi, sản xuất, đọc thử bấm giờ);
  chế độ sửa phân biệt lỗi cục bộ / cấu trúc; chế độ chuyển format.
- `vid-review`: 5 lượt đọc với 5 vai; mỗi lỗi có câu sửa viết sẵn; điểm phải nhất quán với bảng lỗi.
- `vid-flow`: xử lý chọn nhiều / ghép / nghĩ lại; báo khi điểm giảm; gói bàn giao `05-ban-giao.md` (đạo cụ, thứ tự quay
  gom theo bối cảnh, cảnh chèn, ghi chú dựng).
- `vid-series`: 3 loại series, động cơ tập, nhân vật 6 mục, dấu hiệu nhận diện, cập nhật kinh thánh.

Con số giây / độ dài ghi rõ là kinh nghiệm nghề, chưa đo trên kênh của team; chính sách nền tảng ghi "kiểm lại trước
khi đăng".

---

## 8. Thêm 8 nhóm chủ đề, lồng câu chuyện – thông điệp

**Người dùng (lần đầu, bị ngắt):**
> - Thuần điện ảnh, lòng ghép kiểu các câu chuyện, các thông điệp, Các nhóm chủ đề to: Tình yêu, Gia đình, Công việc/học
> hành, Bạn bè, Mạng xã hội, Tâm lý nội tâm, Ước mơ, Xã hội — có thể thêm các phần này vào skill nếu đầu vào người dùng
> không mô tả rõ

**Người dùng (sửa lại):**
> lòng ghép kiểu các câu chuyện, các thông điệp, [8 nhóm chủ đề] có thể thêm các phần này vào skill nếu đầu vào người
> dùng không mô tả rõ — tôi nhầm ghi thêm phần này thôi

→ Không thêm tông "thuần điện ảnh", chỉ thêm phần chủ đề và lồng ghép.

**Trợ lý đã làm:** tạo `shared/nghe/chu-de-va-thong-diep.md`:

- Hai tầng (câu chuyện bề mặt / thông điệp), 5 luật lồng ghép, 6 kiểu thông điệp, bảng ghép hai nhóm chủ đề.
- 8 nhóm, mỗi nhóm: chủ đề con, insight mẫu, thông điệp có thể lồng, hình ảnh / bối cảnh, nhóm tuổi chạm mạnh, bẫy. Nhóm
  Xã hội giới hạn ở hành vi, lối sống, không chính trị.
- Bảng xử lý đầu vào chưa rõ (không có chủ đề → hỏi kèm bảng 8 nhóm, "tuỳ" → chọn 3 nhóm xa nhau; chỉ tên nhóm → tự chọn
  chủ đề con + một cặp ghép; có thông điệp / câu chuyện → tự bổ sung phần thiếu).

Nối vào `vid-flow` (brief thêm nhóm chủ đề, chủ đề con, thông điệp, câu chuyện bề mặt), `vid-brainstorm` (pha 1 xác định
nhóm trước; thẻ concept thêm chủ đề / câu chuyện / thông điệp; concept trải ≥ 2 nhóm; phản biện thêm lồng ghép và bẫy),
`vid-viet-kich-ban` (lượt 1 chốt thông điệp), `vid-review` + danh mục lỗi (AD-08 thông điệp nuốt câu chuyện, AD-09 dạng
mệnh lệnh, AD-10 rơi vào bẫy nhóm, AD-11 nhiều thông điệp), `vid-series`.

---

## 9. Brainstorm cách dùng mượt (chưa làm)

**Người dùng:**
> brainstorm cách sử dụng skill 1 cách mượt mà nhất: khi người dùng chỉ gọi skill thì skill đưa cho người dùng các phần
> để trả lời cho người dùng submit các phần cần thiết để tạo kịch bản (đấy là tôi lấy ví dụ, bạn có thể brainstorm thêm)

**Trợ lý đề xuất:**

1. **Một cửa vào `/vid`**: gọi trống thì hiện menu nút bấm: Làm video mới / Tiếp tục dự án (đọc `du-an/`, hiện dự án dở
   và bước) / Review kịch bản có sẵn / Lên series / Khác.
2. **Ba cách nhập**: nhanh (`/vid bố ít nói, 60s`), hỏi bằng nút bấm (mặc định khi gọi trống; tối đa 2 vòng, mỗi vòng ≤ 4
   câu), phiếu file (`00-brief.md` sửa trong editor rồi gõ "xong").
   - Vòng 1: Ý tưởng (có ý tưởng / gợi ý theo chủ đề / từ video mẫu / tuỳ) · Thời lượng (30 / 60 / 90s) · Dạng (độc lập
     / series) · Khán giả (17–21 / 22–25 / 26–30 / cả ba).
   - Vòng 2 (khi chọn gợi ý theo chủ đề): 8 nhóm chia hai câu chọn nhiều, mỗi câu 4 nhóm.
3. **Hồ sơ mặc định** `shared/cau-hinh.md`: mục nào đã có thì không hỏi lại.
4. **Tóm tắt brief một màn** + nút [Chạy brainstorm] [Sửa], chỉ hiện khi có từ 2 mục "đề xuất".
5. **Chọn concept bằng thẻ xem trước** cạnh từng lựa chọn; hiện 3 concept điểm cao nhất + "Xem thêm / ghép / nghĩ lại".
6. **Lệnh tắt**: `tiếp`, `ghép C2 + hook C4`, `nghĩ lại, hài hơn`, `sửa beat 3: …`, `review lại`, `trạng thái`, `mở`.
7. **Cuối luồng**: tự mở Excel; duyệt bằng 3 nút; `trang-thai.md` ghi người phụ trách.

Đề xuất làm: 1, 2, 3, 5, 6 (4 và 7 làm kèm). Lưu ý: màn hỏi nút bấm chỉ có trong Claude Code, nơi khác thì skill tự
chuyển sang phiếu văn bản đánh số.

**Trạng thái:** đang chờ người dùng chọn làm theo đề xuất hay chỉnh trước.

---

## 10. Tổng hợp

### Quyết định đã chốt

| # | Quyết định |
|---|---|
| 1 | Bộ skill đặt ở `D:\scripts-gen-skills`, skill trong `.claude/skills/` |
| 2 | Kịch bản lưu JSON làm bản gốc; Excel chỉ là bản xuất; không sửa tay Excel |
| 3 | Format đầu ra = file "Dư Ảnh - Kịch bản Demo.xlsx", **chỉ là mẫu định dạng**, không dùng nội dung |
| 4 | Điều kiện sản xuất: 9 người (4 viết, 6 diễn, 1 quay, 2 dựng), có kiêm nhiệm |
| 5 | Ba lớp kiến thức: `luat/` (luôn áp), `nghe/` (luôn dùng làm thước đo), `tham-khao/` (chỉ khi brief ghi) |
| 6 | Skill phải viết chi tiết, tự triển khai từ ý người dùng, không chép giọng người dùng |
| 7 | Tuyến nội dung: lồng câu chuyện – thông điệp; 8 nhóm chủ đề dùng khi đầu vào chưa rõ |
| 8 | Không thêm tông "thuần điện ảnh" (người dùng ghi nhầm) |
| 9 | Review chạy bằng agent độc lập; ĐẠT = không lỗi Nặng và điểm ≥ 8; tối đa 2 vòng sửa |

### Cấu trúc hiện tại

```
D:\scripts-gen-skills\
├── CLAUDE.md
├── README.md
├── .claude/skills/
│   ├── vid-flow/SKILL.md
│   ├── vid-brainstorm/SKILL.md
│   ├── vid-viet-kich-ban/SKILL.md
│   ├── vid-review/SKILL.md
│   └── vid-series/SKILL.md
├── shared/
│   ├── luat/        format-kich-ban · dieu-kien-san-xuat · vung-cam · loi-kich-ban
│   ├── nghe/        khan-gia-va-nen-tang · hook-va-giu-chan · an-du-va-hai · ngon-ngu-dien-anh
│   │                cau-truc-va-nhip · chu-de-va-thong-diep
│   ├── tham-khao/   README · phong-cach · kho-hook · giong-hai   (khung trống, CHƯA CÓ)
│   ├── scripts/kich_ban.py      doc · kiem · xuat
│   └── mau-format/  du-anh-demo.xlsx · du-anh-demo.json
├── du-an/           đầu ra từng dự án
└── lich-su/         ghi chép phiên (file này)
```

### Đã kiểm

- `kich_ban.py`: vòng đọc → xuất → đọc giữ nguyên dữ liệu; `kiem` bắt đúng 4 lỗi có thật trong file mẫu.
- Không còn đường dẫn hỏng, không còn chữ lấy từ nội dung file mẫu.

### Chưa kiểm

- Chưa chạy thử cả luồng `vid-flow` với một ý tưởng thật.

### Việc còn treo

- Chờ người dùng duyệt đề xuất mục 9 (cửa vào `/vid`, hỏi bằng nút bấm, hồ sơ mặc định, thẻ xem trước, lệnh tắt).
- **CHƯA CHỐT** trong `shared/luat/`: ngoại hình, thế mạnh diễn của 6 diễn viên (giới tính chốt 2026-10-22: 1 nữ, 5 nam, thêm mã SX-09; độ tuổi chốt 2026-11-02: 21–22, thêm mã SX-10), bảng kiêm nhiệm, thiết bị, bối cảnh có sẵn, vùng
  cấm riêng của team, bảng tiêu chí chấm của team.
- **CHƯA CÓ** trong `shared/tham-khao/`: phong cách, kho hook, giọng hài (tuỳ chọn, team ghi khi muốn).

---

## 11. Phiên 2026-10-22: giới tính diễn viên, skill phân tích video mẫu

**Người dùng:** "giới tính và độ tuổi của 6 diễn viên : 1 nữ 5 nam" → ghi vào `dieu-kien-san-xuat.md` (tối đa 1 nhân
vật nữ lộ mặt, 5 nam; nữ thứ hai chỉ nghe giọng / qua màn hình), thêm mã SX-09. Độ tuổi vẫn CHƯA CHỐT.

**Người dùng:** muốn khi đưa video reference thì bộ skill tự phân tích điểm hay, vì sao thu hút để áp vào kịch bản;
video mẫu chỉ là tuỳ chọn. Chốt: tách skill, tự cài công cụ lần đầu cho người mới clone repo, làm luôn ba mức bám mẫu và
thư viện mẫu.

Đã làm:

- `shared/scripts/phan_tich_mau.py`: `cai`, `kiem-cai`, `chay`, `tai`, `tach`, `chep`. Tự tạo `.cong-cu/venv` và cài
  yt-dlp, imageio-ffmpeg, faster-whisper, Pillow ở lần đầu rồi tự chạy lại trong venv. Đo: cut, độ dài shot, cut trong
  3 giây đầu, khoảng lặng; lưới ảnh 4×3 có ghi giây, ô đỏ CUT; chép lời có mốc giây; số liệu và bình luận nhiều like.
- Đã kiểm: chạy từ máy chưa cài gì với một video YouTube 19s (tự cài, tải, tách, chép lời đều chạy); video giả có cut ở
  2,0s và 4,0s, im lặng 1,0–3,0s → script đo ra đúng các số đó.
- Lỗi gặp và đã sửa: faster-whisper 1.2 gọi PyAV kiểu cũ (`metadata_errors`) → script tự đọc wav.
- `.claude/skills/vid-phan-tich-mau/SKILL.md`: 3 tầng đầu vào (link / file / thủ công), khuôn `phan-tich.md` 10 mục,
  bằng chứng bắt buộc và tách đo được / suy đoán, phần làm lại được với đội, công thức rút gọn, danh sách không được
  chép, nhiều mẫu, mẫu flop, thư viện, bảng "Bẫy đã gặp" để tự cải thiện.
- `shared/luat/bam-mau.md`: ba mức Cảm hứng / Cùng công thức (mặc định) / Bắt trend, điều cấm ở mọi mức.
- `loi-kich-ban.md`: nhóm MAU-01..05.
- Nối vào `vid-flow` (bước 0.1a chỉ chạy khi người dùng tự đưa mẫu, phân tích bằng agent, gộp 3 câu hỏi học gì / mức
  bám / lưu thư viện vào lượt hỏi brief), `vid-brainstorm`, `vid-viet-kich-ban`, `vid-review`.
- `shared/tham-khao/mau/INDEX.md`, `.gitignore` (bỏ `.cong-cu/` và video, âm thanh, khung hình của mẫu), README,
  CLAUDE.md.

Sau đó trong cùng phiên:

- Excel: Times New Roman 13 / 12, bỏ chữ nghiêng, mỗi kịch bản một sheet có khối TỔNG QUAN (JSON thêm `overview`);
  `doc` vẫn đọc file kiểu cũ.
- Workflow `/vid` (người dùng duyệt sau khi tự phản biện): đổi tên `vid-flow` → `vid` làm cửa vào duy nhất (gọi trống
  hiện menu, có đối số tự chọn hướng), brief một lượt tối đa 4 câu theo ưu tiên, `shared/cau-hinh.md` chỉ chứa sở
  thích, chọn concept bằng 3 thẻ xem trước, chế độ nhanh chỉ khi người dùng nói rõ (3 concept, 1 vòng sửa), nhiều
  video một lượt → một file nhiều sheet, review và duyệt cả lô một lần, một dòng gợi ý lệnh tắt ở mỗi điểm dừng.
- Push: lịch sử local không chung gốc với GitHub → rebase lên `Initial commit`; push nhầm lên repo Sotatek-DucTran8
  rồi gỡ (force về `8f9817d`); origin đổi sang `minhductran042/Gen-Script-Skill`, push bị 403 vì tài khoản đăng nhập
  không có quyền ghi.

---

## 12. Phiên 2026-11-02: độ tuổi diễn viên, tông cảm xúc

**Người dùng:** "độ tuổi diễn viên: 21-22" → ghi vào `dieu-kien-san-xuat.md`: vai bố mẹ, ông bà, sếp trung niên không lộ
mặt (trừ khi cố tình gây hài); thêm mã SX-10 (Vừa) và câu kiểm trong `vid-review`. Ngoại hình, thế mạnh diễn vẫn CHƯA CHỐT.

**Người dùng:**
> hiện tai, bat ky kich ban nao tao ra deu co xu huong hai huoc va an du, dieu nay khong giong y tuong ban dau cua toi lam
> vi dieu nay khien cho kich ban tao ra hien tai bi go bo trong viec phai co hai huoc va an du, co the nguoi dung khong
> muon vay hoac dieu nay khien cho kich ban tao ra bi bo buoc, bay gio toi muon kich ban tao ra co the do nguoi dung dua
> vao hoac brainstorm giup toi de xu ly cho phan nay mot cach tot nhat de cai thien skill nay tot hon (noi chung la xu ly
> phan tong cam xuc cho kich ban) , brainstorm de de xuat cho phan nay

**Nguyên nhân tìm được:** hài và ẩn dụ bị ép ở cả bốn khâu: tông mặc định trong `cau-hinh.md` và lệnh không hỏi tông; hai
tiêu chí và hai dòng bắt buộc của brainstorm; yêu cầu bắt buộc ở lượt viết; Ẩn dụ + Hài chiếm 3/10 trọng số review. Kịch
bản không hài, không ẩn dụ tối đa 7.6 điểm, không thể ĐẠT, nên vòng sửa tự kéo về hài.

**Người dùng duyệt đề xuất, đã làm:**

- Thêm `shared/nghe/tong-cam-xuc.md`: ba trục độc lập (Cảm xúc chủ đạo, Cách kể, Độ hài), đường cảm xúc, bảng chốt tông
  từ đầu vào, tám cảm xúc với cơ chế và bẫy, luật nào áp theo tông.
- `cau-hinh.md`: để trống Tông, không còn mặc định. `/vid`: thêm khung tông trong brief, thêm câu hỏi tông (lựa chọn đầu
  là "Để skill đề xuất"); mục 0.3 đánh lại ưu tiên.
- `vid-brainstorm`: thêm nhóm năm lăng kính kể thẳng; thay "Ẩn dụ rõ", "Tiềm năng hài" bằng "Khớp tông", "Độ mới"; thẻ
  concept và thẻ xem trước có dòng Tông; dòng ẩn dụ, hài thành tuỳ chọn; khi skill tự đề xuất thì trải ít nhất 3 cảm xúc, 2
  cách kể, không quá một nửa dùng ẩn dụ hoặc lấy hài làm chính.
- `vid-viet-kich-ban`: các yêu cầu ẩn dụ, hài chỉ áp khi tông có; thêm đỉnh cảm xúc, kiểm tông ở lượt 8; không đổi tông khi
  sửa.
- `vid-review` + `loi-kich-ban.md`: thay tiêu chí Ẩn dụ, Hài bằng "Sức mạnh cảm xúc", "Cách kể" (trọng số giữ 1.5 mỗi tiêu
  chí); thêm nhóm CX-01..05; mã AD áp theo tông; AD-03 không còn đòi miếng thoát.
- `vid-series`, `vid-phan-tich-mau` (mục 4.5 thành "Tông cảm xúc và hài"), `format-kich-ban.md`, các file `nghe/`, CLAUDE.md,
  README: bỏ các chỗ ngầm định hài, ẩn dụ.
- `kich_ban.py` không đổi: `overview.tong` vẫn là một chuỗi, ghi `<cảm xúc> · <cách kể> · <độ hài>`.

**Chưa kiểm:** chưa chạy thử cả luồng `/vid` với tông mới trên một ý tưởng thật.

### Rà soát toàn dự án và sửa (cùng ngày)

**Người dùng:** "Đọc lai tong quan ca du an, check lai cac phan da tot, cac phan co the gay cho viec tao kich ban khong
duoc tot, cac phan \"nen\" cai thien de xuat cho skill tot hon, sau do tu phan bien lai xem da tot hay chua", rồi "sửa cac
phan tren de cai thien skill".

Bằng chứng từ `du-an/`: 12/12 concept kết bằng miếng hài thoát; 5/5 kịch bản đúng 8 beat; điểm 7.6–8.25 sát ngưỡng; mã MOI
không vào danh mục và trùng nghĩa.

Đã sửa:

- Lỗi của bản tông: thêm dòng "Tông đã chốt" trong brief, ghi ở điểm dừng 1; viết và review lấy tông theo từng kịch bản.
- Thông điệp thành lựa chọn Có / Không: `thong_diep` không còn bắt buộc, AD-08, 09, 11 và phần thông điệp của GC-03 chỉ áp khi có.
- Khung truyện theo cảm xúc (`tong-cam-xuc.md` mục 6, mục luật áp đổi thành mục 7): lật không bắt buộc, số beat theo chuyện;
  GC-04, GC-05, mốc "kết bất ngờ", ngắt nhịp 3–5 giây áp theo tông. Brainstorm thêm luật đa dạng cấu trúc và kiểu kết.
- `kich_ban.py kiem`: không đếm vai chỉ nghe giọng; thêm SX-03, SX-08, SX-09, GC-06, HK-06, NH-06 (mới); `tong` thành bắt buộc,
  báo lỗi nếu còn "đề xuất".
- Thêm SX-11 (vùng giao diện che), SX-12 (liên tục hình); `/vid` hỏi đưa mã mới vào danh mục sau khi duyệt.
- Review: điểm hai chữ số, không làm tròn khi so ngưỡng, ghi "sát ngưỡng" với 7.8–8.2.
- Thêm `06-sau-dang.md` để ghi số liệu sau đăng; brainstorm đọc làm tham khảo.
- Checklist quay được thêm tuổi; vai học sinh không có tình huống lãng mạn; sửa README, `tham-khao/README.md`.

Giữ nguyên, chờ người dùng quyết: `.gitignore` bỏ qua `lich-su/`, `du-an/`; kiểu xuống dòng lẫn lộn CRLF / LF.

---

## 13. Phiên 2026-11-02: dùng được trên Codex

**Người dùng:** "hien toi muon bo skill nay su dung duoc tren codex, them cac phan de bo skill nay co the su dung duoc voi
codex hay hien tai da co the dung"

Trước đó chưa dùng được: Codex quét `.agents/skills`, đọc `AGENTS.md`, không đọc `.claude/skills` hay `CLAUDE.md`.

Đã làm:

- Chuyển hướng dẫn dự án sang `AGENTS.md`; `CLAUDE.md` chỉ còn dòng nhập `@AGENTS.md`.
- `shared/scripts/dong_bo_codex.py` sinh `.agents/skills/<tên>/SKILL.md` trỏ về `.claude/skills/`, có `--kiem`. Không dùng symlink
  vì symlink git hỏng trên Windows khi chưa bật Developer Mode.
- `.codex/config.toml` bật mạng trong sandbox, cần cho tự cài công cụ và tải video; chỉ có hiệu lực khi project được tin cậy.
- `vid/SKILL.md` thêm bảng hai công cụ (gọi skill, hỏi, subagent); không tạo được subagent thì không tự review, chuyển sang
  phiên mới. Prompt review ghi rõ đường dẫn skill. `vid-phan-tich-mau` bỏ tên công cụ riêng của Claude Code.

**Chưa kiểm:** máy này không có Codex, chưa chạy thử thật.
