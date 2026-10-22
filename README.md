# Bộ skill kịch bản video ngắn

Mở Claude Code ở thư mục này (`D:\scripts-gen-skills`) thì các skill trong `.claude/skills/` tự được nạp.
Bắt đầu nhanh: `/vid-flow <ý tưởng>`.

## Luồng

```
 Ý tưởng thô (± tham khảo tuỳ chọn, ± link / file video mẫu tuỳ chọn)
          │
   [0a] chỉ khi có video mẫu: vid-phan-tich-mau (agent) ─ vì sao mẫu thu hút + công thức + không được chép
          │
   [0] vid-flow: chốt brief ─ thiếu thì hỏi một lượt (có mẫu: học gì, mức bám, lưu thư viện)
          │
   [1] vid-brainstorm ─ insight → ≥15 ý thô → chấm → 5–8 concept → tự phản biện
          │
   ⏸ người dùng chọn / ghép / yêu cầu nghĩ lại
          │
   [2] vid-viet-kich-ban ─ 8 lượt viết → kiem → JSON + Excel
          │
   [3] vid-review (agent độc lập) ─ 5 lượt đọc → bảng lỗi có mã + điểm
          │
   Đạt? ─ không → [4] sửa → review lại (tối đa 2 vòng, quá thì hỏi người dùng)
          │ có
   ⏸ người dùng duyệt
          │
   [5] kich-ban-final.xlsx + 05-ban-giao.md (đạo cụ, thứ tự quay, cảnh chèn, ghi chú dựng)
```

Series: chạy `/vid-series` trước để có `series.md`, rồi mỗi tập đi qua `vid-flow`.

## Skill

| Skill | Làm gì | Gọi khi |
|---|---|---|
| `vid-flow` | Điều phối cả luồng, giữ trạng thái, gói bàn giao | Làm một video từ đầu tới cuối, hoặc làm tiếp |
| `vid-brainstorm` | Năm pha: insight, phân kỳ, hội tụ, thẻ concept, phản biện | Chỉ cần ý tưởng |
| `vid-viet-kich-ban` | Viết mới (8 lượt), sửa theo review, chuyển format | Có concept, cần kịch bản |
| `vid-review` | Năm lượt đọc, bảng lỗi có mã, điểm theo mốc | Có kịch bản, cần góp ý |
| `vid-series` | Loại series, động cơ tập, nhân vật cố định, danh sách tập | Làm nhiều tập |
| `vid-phan-tich-mau` | Tải / tách video mẫu, đo nhịp dựng, chép lời, mổ theo lớp, vì sao thu hút, công thức, thư viện mẫu | Có video mẫu; `vid-flow` tự gọi |

## Cấu trúc

```
.claude/skills/            6 skill
shared/
  luat/                    RÀNG BUỘC CỨNG, luôn áp
    format-kich-ban.md       10 cột, cách viết từng cột, JSON
    dieu-kien-san-xuat.md    9 người, 1 máy quay, hệ quả khi viết, kiểm "quay được"
    vung-cam.md              cấm hẳn / hạn chế, cách thay thế
    loi-kich-ban.md          danh mục lỗi có mã + bảng chấm có mốc
    bam-mau.md               ba mức bám video mẫu, điều cấm chép (chỉ áp khi có mẫu)
  nghe/                    KIẾN THỨC NGHỀ, luôn dùng làm thước đo
    chu-de-va-thong-diep.md  8 nhóm chủ đề, lồng câu chuyện – thông điệp, ghép chủ đề, xử lý đầu vào chưa rõ
    khan-gia-va-nen-tang.md  ba nhóm tuổi, hành vi lướt, TikTok vs Shorts, độc lập vs series
    hook-va-giu-chan.md      12 dạng hook, điểm rơi người xem, kỹ thuật giữ chân, kiểu kết
    an-du-va-hai.md          cách tìm và chấm ẩn dụ, kho đồ vật, cơ chế và nhịp hài
    ngon-ngu-dien-anh.md     từ vựng góc máy, bố cục dọc, ánh sáng, âm thanh, dựng
    cau-truc-va-nhip.md      logline, khung beat, phân bổ giây, cấu trúc khác, ước thời lượng
  tham-khao/               THAM KHẢO TUỲ CHỌN, chỉ đọc khi brief ghi
    mau/                     thư viện bản phân tích video mẫu (INDEX.md), chỉ lưu khi người dùng đồng ý
  scripts/kich_ban.py      doc (xlsx→json) · kiem (soát) · xuat (json→xlsx)
  scripts/phan_tich_mau.py cai · chay (tải → tách khung, đo cut → chép lời) · tai · tach · chep
.cong-cu/                  công cụ tự cài lần đầu (venv, mô hình chép lời); không commit
  mau-format/              file Excel mẫu ĐỊNH DẠNG (không dùng nội dung)
du-an/<ngày>-<slug>/       đầu ra của từng video / series
```

## Lệnh script

```
py -I shared/scripts/kich_ban.py doc  <file.xlsx> <ra.json>
py -I shared/scripts/kich_ban.py kiem <kich-ban.json>
py -I shared/scripts/kich_ban.py xuat <kich-ban.json> <ra.xlsx>
```

Máy không có `py` thì dùng `python3`. Cần `openpyxl` (`pip install openpyxl`).

Phân tích video mẫu (skill tự gọi, không cần gõ tay):

```
py -I shared/scripts/phan_tich_mau.py chay <link | file.mp4> <thư mục ra>
py -I shared/scripts/phan_tich_mau.py kiem-cai
```

Lần đầu chạy, script tự tạo `.cong-cu/venv` và cài yt-dlp, ffmpeg (qua imageio-ffmpeg), faster-whisper, Pillow; lần
đầu chép lời tải thêm mô hình (small khoảng 480 MB). Người mới clone repo không phải cài gì ngoài Python; không có
Python thì skill tự cài bằng winget / brew / apt.

## Dùng tham khảo cho một lần làm

Nói kèm khi gọi, ví dụ `/vid-flow <ý tưởng>, tham khảo shared/tham-khao/kho-hook.md`.
Không nói gì thì skill không đọc `tham-khao/`.

Video mẫu cũng là tuỳ chọn: `/vid-flow <ý tưởng> <link video>` hoặc `/vid-flow <ý tưởng>, theo mẫu <slug>`. Không đưa
mẫu thì luồng không hỏi gì về mẫu. Chỉ muốn mổ video: `/vid-phan-tich-mau <link>`.

## Còn CHƯA CHỐT

Trong `shared/luat/`: độ tuổi 6 diễn viên (giới tính đã chốt: 1 nữ, 5 nam), bảng kiêm nhiệm, thiết bị, bối cảnh có sẵn, vùng cấm riêng của
team, bảng tiêu chí chấm của team. Điền thẳng vào file, không cần sửa SKILL.md.
