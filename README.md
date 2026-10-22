# Bộ skill kịch bản video ngắn

Mở Claude Code ở thư mục gốc của repo thì các skill trong `.claude/skills/` tự được nạp.
Chỉ cần nhớ một lệnh: **`/vid`**.

## Lần đầu trên máy mới

Cần có sẵn: [Claude Code](https://docs.claude.com/en/docs/claude-code) đã đăng nhập, Git, Python 3 (Windows: `py --version`;
macOS / Linux: `python3 --version`).

```
git clone https://github.com/minhductran042/Gen-Script-Skill.git
cd Gen-Script-Skill
claude
```

1. Claude Code hỏi có tin thư mục này không: chọn đồng ý. Skill chỉ được nạp khi mở Claude Code **đúng thư mục repo**.
2. Gõ `/vid`. Thấy menu (làm video mới, mổ video mẫu, review kịch bản…) là chạy được.
3. Khi skill chạy lệnh `py …` / `python3 …`, Claude Code hỏi quyền: cho phép.
4. (Tuỳ chọn) điền `shared/cau-hinh.md` để đỡ bị hỏi lại thời lượng, khán giả.

Không phải tự cài thư viện nào. Lần đầu dùng tới, script tự tạo `.cong-cu/venv` (không đưa lên git, máy nào tự cài
máy đó) và cài vào đó:

| Lúc | Tự cài | Mất bao lâu |
|---|---|---|
| Lần đầu xuất / đọc Excel kịch bản | `openpyxl` (chỉ khi Python của máy chưa có) | Vài giây |
| Lần đầu phân tích video mẫu | yt-dlp, ffmpeg, faster-whisper, Pillow + mô hình chép lời (~480 MB) | Khoảng 15 phút; từ lần sau video 20 giây mất ~30 giây |

Máy chưa có Python: khi phân tích video mẫu, skill tự cài bằng winget (Windows) / brew (macOS) / apt (Linux); hoặc tự
cài Python 3 từ python.org (Windows: tích "Add python.exe to PATH").

Kiểm công cụ phân tích video: `py -I shared/scripts/phan_tich_mau.py kiem-cai`. Mạng chặn TikTok (thường là mạng công
ty) thì lưu video về máy rồi đưa file `.mp4`, hoặc gửi ảnh chụp màn hình.

| Gõ | Kết quả |
|---|---|
| `/vid` | Menu: làm video mới · làm tiếp dự án dở · mổ video mẫu · review kịch bản |
| `/vid bố ít nói, 60s` | Làm video mới từ ý tưởng |
| `/vid làm 3 video về deadline` | Ba kịch bản, một file Excel ba sheet |
| `/vid <link video> làm theo cái này` | Phân tích mẫu rồi làm video theo công thức của mẫu |
| `/vid theo mẫu <tên>` | Dùng bản phân tích đã lưu trong thư viện |
| `/vid tiếp` | Làm tiếp dự án dở |
| `/vid du-an/<...>/kich-ban-v2.json` | Review kịch bản có sẵn |
| `/vid series …` | Lên khung series |
| thêm chữ `nhanh` | Chế độ nhanh: 3 concept, sửa tối đa 1 vòng |

Sở thích mặc định của team (thời lượng, khán giả, tông…) ghi ở `shared/cau-hinh.md`; mục nào đã ghi thì không bị hỏi lại.

## Luồng

```
 /vid ─ chọn hướng (menu khi gọi trống)
          │
   [0a] chỉ khi có video mẫu: vid-phan-tich-mau (agent) ─ vì sao mẫu thu hút + công thức + không được chép
          │
   [0] chốt brief ─ một lượt hỏi, tối đa 4 câu bằng nút bấm; mục có trong cau-hinh.md thì không hỏi
          │
   [1] vid-brainstorm ─ insight → ≥15 ý thô → chấm → 5–8 concept → tự phản biện (nhanh: 8 ý, 3 concept)
          │
   ⏸ chọn trong 3 concept điểm cao nhất (thẻ xem trước) / xem thêm / ghép / nghĩ lại
          │
   [2] vid-viet-kich-ban ─ 8 lượt viết → kiem → JSON + Excel
          │
   [3] vid-review (agent độc lập) ─ 5 lượt đọc → bảng lỗi có mã + điểm
          │
   Đạt? ─ không → [4] sửa → review lại (tối đa 2 vòng, nhanh 1 vòng; quá thì hỏi người dùng)
          │ có
   ⏸ người dùng duyệt (cả lô một lần)
          │
   [5] kich-ban-final.xlsx (mỗi kịch bản một sheet, có Tổng quan) + 05-ban-giao.md
```

Series: chạy `/vid-series` trước để có `series.md`, rồi mỗi tập đi qua `/vid`.

## Skill

| Skill | Làm gì | Gọi khi |
|---|---|---|
| `/vid` | Cửa vào duy nhất: chọn hướng, điều phối cả luồng, giữ trạng thái, gói bàn giao | Mọi lúc; các skill dưới gọi thẳng khi chỉ cần một việc |
| `vid-brainstorm` | Năm pha: insight, phân kỳ, hội tụ, thẻ concept, phản biện | Chỉ cần ý tưởng |
| `vid-viet-kich-ban` | Viết mới (8 lượt), sửa theo review, chuyển format | Có concept, cần kịch bản |
| `vid-review` | Năm lượt đọc, bảng lỗi có mã, điểm theo mốc | Có kịch bản, cần góp ý |
| `vid-series` | Loại series, động cơ tập, nhân vật cố định, danh sách tập | Làm nhiều tập |
| `vid-phan-tich-mau` | Tải / tách video mẫu, đo nhịp dựng, chép lời, mổ theo lớp, vì sao thu hút, công thức, thư viện mẫu | Có video mẫu; `/vid` tự gọi |

## Cấu trúc

```
.claude/skills/            6 skill (vid là cửa vào)
shared/
  cau-hinh.md              sở thích mặc định của team, mục đã ghi thì /vid không hỏi lại
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

Máy không có `py` thì dùng `python3`. Không cần cài `openpyxl` tay: thiếu thì script tự cài vào `.cong-cu/venv`.

Phân tích video mẫu (skill tự gọi, không cần gõ tay):

```
py -I shared/scripts/phan_tich_mau.py chay <link | file.mp4> <thư mục ra>
py -I shared/scripts/phan_tich_mau.py kiem-cai
```

Lần đầu chạy, script tự tạo `.cong-cu/venv` và cài yt-dlp, ffmpeg (qua imageio-ffmpeg), faster-whisper, Pillow; lần
đầu chép lời tải thêm mô hình (small khoảng 480 MB). Người mới clone repo không phải cài gì ngoài Python; không có
Python thì skill tự cài bằng winget / brew / apt.

## Dùng tham khảo cho một lần làm

Nói kèm khi gọi, ví dụ `/vid <ý tưởng>, tham khảo shared/tham-khao/kho-hook.md`.
Không nói gì thì skill không đọc `tham-khao/`.

Video mẫu cũng là tuỳ chọn: `/vid <ý tưởng> <link video>` hoặc `/vid <ý tưởng>, theo mẫu <slug>`. Không đưa
mẫu thì luồng không hỏi gì về mẫu. Chỉ muốn mổ video: `/vid-phan-tich-mau <link>`.

## Còn CHƯA CHỐT

Trong `shared/luat/`: độ tuổi 6 diễn viên (giới tính đã chốt: 1 nữ, 5 nam), bảng kiêm nhiệm, thiết bị, bối cảnh có sẵn, vùng cấm riêng của
team, bảng tiêu chí chấm của team. Điền thẳng vào file, không cần sửa SKILL.md.
