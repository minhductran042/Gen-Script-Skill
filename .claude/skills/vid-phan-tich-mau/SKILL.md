---
name: vid-phan-tich-mau
description: "Phân tích video mẫu (link TikTok / YouTube / Reels, file .mp4, hoặc ảnh chụp + mô tả) để chỉ ra vì sao video thu hút: hook ba lớp, điểm giữ chân, cấu trúc beat, ẩn dụ và thông điệp, cơ chế hài, ngôn ngữ điện ảnh, nhịp dựng đo được (số cut, độ dài shot, khoảng lặng), lời thoại chép tự động có mốc giây, bình luận nổi bật. Mỗi nhận định kèm bằng chứng và tách đo được / suy đoán; có phần làm lại được với đội mình, công thức rút gọn để brainstorm, và danh sách không được chép. Lần đầu dùng tự cài công cụ (yt-dlp, ffmpeg, whisper), người dùng không phải cài gì. Dùng khi user dán link video, nói 'phân tích video này', 'video này hay ở đâu', 'mổ video mẫu', 'vì sao video này viral', 'video này flop vì sao'; vid-flow tự gọi khi brief có video mẫu. Viết kịch bản từ mẫu thì dùng vid-flow (nó gọi skill này rồi đi tiếp)."
argument-hint: <link | file.mp4 | ảnh chụp + mô tả> [flop] [lưu]
---

# Phân tích video mẫu

Đầu ra là một bản phân tích `phan-tich.md` trả lời được ba câu: video này **làm gì** (theo từng giây), **vì sao** nó
thu hút (có bằng chứng), và **mình học được gì** mà không chép.

Video mẫu là **tuỳ chọn** trong cả bộ skill. Skill này chỉ chạy khi người dùng đưa mẫu; không có mẫu thì không ai gọi
nó và luồng làm kịch bản không hỏi gì về mẫu.

## Chế độ

| Chế độ | Khi nào | Thư mục ghi |
|---|---|---|
| **Trong luồng** | `vid-flow` gọi (thường qua subagent) | `du-an/<dự án>/mau/<k>/` (k = 1, 2, 3 theo thứ tự mẫu) |
| **Độc lập** | Người dùng chỉ muốn mổ video, chưa viết kịch bản | `du-an/<YYYY-MM-DD>-mau-<slug>/` |
| **Nhiều mẫu** | 2–3 video cùng lúc | Mỗi mẫu một thư mục con, cộng `tong-hop.md` |
| **Mẫu flop** | Người dùng nói video này flop / không hiệu quả | Như trên; mục 5 đổi thành "Vì sao không giữ được người xem" |

## Kiến thức dùng

Luôn đọc, vì đây là thước đo để gọi tên những gì thấy trong mẫu:

- `shared/nghe/hook-va-giu-chan.md`: dạng hook `HK-D01..D12`, điểm rơi, kỹ thuật giữ chân, kiểu kết.
- `shared/nghe/cau-truc-va-nhip.md`: khung beat, cấu trúc khác, phân bổ giây.
- `shared/nghe/an-du-va-hai.md`: kiểu ẩn dụ, lúc lộ ẩn dụ, cơ chế hài, nhịp hài.
- `shared/nghe/ngon-ngu-dien-anh.md`: cỡ cảnh, chuyển động, ánh sáng, âm thanh, nhịp dựng.
- `shared/nghe/chu-de-va-thong-diep.md`: nhóm chủ đề, câu chuyện bề mặt và thông điệp.
- `shared/nghe/khan-gia-va-nen-tang.md`: nhóm tuổi, hành vi lướt.
- `shared/luat/dieu-kien-san-xuat.md`: để chấm phần "làm lại được với đội mình".
- `shared/luat/vung-cam.md`: mẫu có nội dung thuộc vùng cấm thì ghi rõ, không học phần đó.
- `shared/luat/loi-kich-ban.md`: điểm yếu của mẫu gọi bằng mã lỗi có sẵn.
- `shared/luat/bam-mau.md`: để viết mục "Không được chép".

---

## Bước 0: Công cụ (tự cài lần đầu)

Người dùng **không phải cài hay tìm hiểu gì**. Skill tự làm:

1. Có Python chưa: thử `py --version`, rồi `python3 --version`.
   - Không có trên Windows: `winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements`,
     rồi mở lại shell hoặc gọi thẳng `py`.
   - Không có trên macOS: `brew install python`. Linux: `sudo apt install -y python3 python3-venv`.
   - Không cài được (không có quyền, không có mạng): chuyển sang **tầng 3** ở bước 1 và báo một dòng lý do.
2. Chạy `py -I shared/scripts/phan_tich_mau.py kiem-cai` để biết đây có phải lần đầu không.
3. Gọi lệnh phân tích ở bước 1. Script tự kiểm, thiếu thì tự tạo môi trường riêng ở `.cong-cu/venv` và cài
   `yt-dlp`, `imageio-ffmpeg` (có sẵn ffmpeg), `faster-whisper`, `Pillow`, rồi tự tải mô hình chép lời khi cần.
   - **Thời gian:** lần đầu cài gói vài phút; `kiem-cai` báo `whisper small CHƯA TẢI` thì thêm **10–15 phút** tải mô hình
     (khoảng 480 MB, đã đo: 335 MB sau 8 phút). Từ lần thứ hai, video 20 giây chạy hết khoảng 30 giây.
   - Lần đầu: chạy lệnh ở **chế độ nền** (Bash `run_in_background`) và chờ thông báo xong, đừng để lệnh chạy trước mặt
     rồi bị cắt ở mốc 10 phút. Báo người dùng một dòng "lần đầu: đang cài công cụ và tải mô hình, khoảng 15 phút".
   - Người dùng cần nhanh: `--model base` (khoảng 140 MB, chép kém hơn), hoặc `--khong-chep` rồi dựa vào phụ đề `.vtt`.

Lệnh chạy bằng `py -I` trên Windows, `python3 -I` trên macOS / Linux. Đường dẫn tính từ gốc repo.

## Bước 1: Lấy dữ liệu

Chọn tầng cao nhất làm được; tầng trên lỗi thì tự xuống tầng dưới, không dừng.

| Tầng | Người dùng đưa | Lệnh | Ra |
|---|---|---|---|
| **1. Link** | Link TikTok, YouTube / Shorts, Reels, Facebook | `phan_tich_mau.py chay <link> <thư mục>` | `video.mp4`, `meta.json` (view, like, comment, ngày đăng, mô tả), `binh-luan.json` (bình luận nhiều like nhất), phụ đề `.vtt` nếu có, rồi như tầng 2 |
| **2. File** | File `.mp4` / `.mov` | `phan_tich_mau.py chay <file> <thư mục>` | `canh.json` (số đo dựng), `luoi-NN.jpg` (lưới ảnh có ghi giây, ô đỏ "CUT" là ngay sau một lần cắt), `khung/`, `loi.txt` + `loi.json` (lời có mốc giây) |
| **3. Thủ công** | Ảnh chụp màn hình, phụ đề, hoặc mô tả | không chạy script | Dựng dòng thời gian từ những gì có |

Tuỳ chọn: `--model base` chép nhanh hơn nhưng kém chính xác hơn; `--khong-chep` khi video chỉ có nhạc; `--nguong 0.2`
khi video cắt mềm (chuyển cảnh mờ) mà `so_cut` ra ít bất thường.

Tầng 3 chỉ hỏi phần còn thiếu, gộp một lượt:

```
1. Ảnh chụp 3 giây đầu và khoảnh khắc lật (nếu có)
2. Lời thoại / chữ trên màn hình (dán phụ đề càng tốt)
3. Video dài bao nhiêu giây, khoảng mấy lần cắt cảnh
4. (Tuỳ chọn) Bạn thích điều gì ở video này
```

Mẫu là **kịch bản chữ** (không phải video): bỏ bước 1, đọc thẳng kịch bản; mục 3 (số đo dựng) ghi "không có".

Link tải không được (TikTok chặn theo đợt, video riêng tư): báo một dòng, đề nghị người dùng tải tay file `.mp4` vào thư
mục dự án (tầng 2), hoặc gửi ảnh chụp (tầng 3).

## Bước 2: Đọc dữ liệu

Đọc mọi file bằng công cụ đọc file (Read), **không** in ra bằng `py -I -c "print(...)"`: trên Windows, `-I` bỏ qua
cấu hình mã hoá và in tiếng Việt / emoji sẽ lỗi `UnicodeEncodeError`.

Theo thứ tự, vì số đo giúp đọc ảnh đúng chỗ:

1. `canh.json`: `thoi_luong`, `khung_hinh`, `doc` (true = khung dọc), `cut_luc` (giây), `so_shot`, `shot_trung_binh`,
   `shot_dai_nhat`, `cut_trong_3s_dau`, `im_lang` (các đoạn **tắt tiếng thật**, dưới −35 dB từ 0,4s trở lên), `khung`
   (danh sách ảnh: `t`, `loai` = hook / cut / giua / cuoi).
2. `luoi-01.jpg`, `luoi-02.jpg`…: xem **hết**, theo thứ tự. Lưới 1 bắt đầu bằng 0,0–3,0s (0,5s một ảnh); sau đó có một
   ảnh ngay sau mỗi cut và ít nhất 2 giây một ảnh. Ghi cỡ cảnh, hành động, biểu cảm, chữ trên màn hình, màu, ánh sáng.
   Cần nhìn kỹ một khung thì mở file trong `khung/`.
3. `loi.txt` / `loi.json`: lời chia theo câu và quãng nghỉ, có mốc giây. `loi.json` có `xac_suat_ngon_ngu`, mỗi đoạn có
   `xac_suat_tu_thap_nhat` (0–1; dưới 0,4 thì `loi.txt` đã ghi "(nghe không chắc)"), và `khong_thoai` (quãng **không có
   lời nói** từ 0,8s, có thể vẫn có nhạc hay tiếng nền).
   - Lời chép lệch nguồn khác thì tin theo thứ tự: **chữ trên màn hình** > **phụ đề `.vtt`** > **lời whisper**. Ghi bản
     tin được vào dòng thời gian; chỗ lệch đáng kể thì ghi cả hai, ví dụ `"in front of" (whisper: "one of")`.
   - Mốc giây lấy từ `loi.json`; `.vtt` chỉ dùng để sửa chữ.
   - Video nhạc nền, ít thoại: whisper hay **bịa lời** từ lời bài hát. Lời không khớp hình thì bỏ.
4. `meta.json`: `title`, `uploader`, `duration`, `view_count`, `like_count`, `comment_count`, `upload_date`,
   `description`, `tags`, `track` / `artist` (nhạc nền). Trường nào `null` hoặc có `ghi_chu_...` thì ghi "không rõ",
   không suy ra. Số vô lý (ví dụ bình luận ít hơn like của một bình luận) cũng ghi "không rõ" kèm lý do.
5. `binh-luan.json`: danh sách `{like, text}`, chỉ gồm **bình luận gốc** (không có trả lời), xếp theo like giảm dần, tối
   đa 40. Gom thành nhóm ý (khen chỗ nào, nhắc lại câu nào, tag bạn bè vì sao), mỗi nhóm ghi tổng like. Đây là bằng
   chứng tốt nhất cho "người xem thích gì". TikTok thường không cho lấy bình luận: file rỗng thì ghi "không lấy được".

## Bước 3: Viết `phan-tich.md`

```markdown
# Phân tích mẫu: <tiêu đề ngắn>

- Nguồn: <link / file> · Nền tảng · Kênh · Ngày đăng
- Thời lượng · Khung (dọc / ngang) · Loại: mẫu hay | mẫu flop | khác dạng (không phải video giải trí dọc ngắn: ghi dạng gì)
- Số liệu: <view> view · <like> like · <comment | không rõ> bình luận · tỉ lệ like / view <x%> (chỉ dùng số có thật
  trong meta.json; số tự tính thì ghi "tính ra")
- Dữ liệu: tầng <1|2|3> · chép lời <model, ngôn ngữ, xác suất nhận ngôn ngữ> · nguồn chữ <whisper | .vtt | cả hai> ·
  bình luận gốc đọc được <n>

## 1. Một câu
Logline: <ai muốn gì, vướng gì, ra sao>. Câu hỏi kịch tính: <người xem chờ câu trả lời gì>.

## 2. Dòng thời gian
| Giây | Hình (cỡ cảnh, hành động) | Lời | Chữ trên màn hình | Âm thanh | Cut |
(chia dòng: mỗi shot một dòng; shot dài trên 4 giây thì chia tiếp theo đoạn lời trong loi.json hoặc theo hành động
đổi trong lưới ảnh; 3 giây đầu chia 0,5s nếu có thay đổi)

## 3. Số đo dựng (đo được)
Số cut · shot trung bình · shot dài nhất (ở giây nào, để làm gì) · cut trong 3 giây đầu ·
tắt tiếng thật (`im_lang` trong canh.json) · quãng không thoại (`khong_thoai` trong loi.json): giây nào, đứng trước
khoảnh khắc gì. Hai loại này khác nhau: im lặng hẳn là kỹ thuật dựng, không thoại mà còn tiếng nền là nhịp diễn.

## 4. Mổ theo lớp
### 4.1. Hook (0–3s)
Hình / âm / chữ (ba lớp) · dạng `HK-Dxx` · lời hứa với người xem
### 4.2. Giữ chân
| Giây | Chỗ người xem dễ rời đi | Mẫu giữ lại bằng kỹ thuật gì |
### 4.3. Cấu trúc và nhịp
Khung beat (đối chiếu cau-truc-va-nhip.md) · vị trí lật · phân bổ giây
### 4.4. Câu chuyện, thông điệp, chủ đề
Nhóm chủ đề · câu chuyện bề mặt · thông điệp · kiểu ẩn dụ · lúc lộ ẩn dụ
### 4.5. Hài
Cơ chế · nhịp (cài – chờ – bung)
### 4.6. Điện ảnh
Cỡ cảnh chủ đạo · chuyển động máy · ánh sáng · màu · âm thanh (tiếng động, nhạc, im lặng)
### 4.7. Kết
Kiểu kết · hành vi kéo theo (lưu, share, comment, xem lại)

## 5. Vì sao thu hút
| # | Điểm | Bằng chứng (giây / số đo / bình luận) | Đo được hay suy đoán |
Bình luận nói gì: <các nhóm ý, mỗi nhóm một dòng kèm số like>

## 6. Điểm yếu, không nên học
| Điểm | Ở giây | Mã lỗi tương ứng trong loi-kich-ban.md |

## 7. Làm lại được với đội mình không
| Yếu tố của mẫu | Đội làm được? (6 diễn viên: 1 nữ 5 nam, 1 máy quay, thiết bị hiện có) | Cách thay nếu không |

## 8. Công thức rút gọn
- Giữ (hằng số): dạng hook, khung beat có giây, nhịp dựng, kiểu kết, kỹ thuật giữ chân chính
- Đổi (biến số): vấn đề, đồ vật / hình ảnh ẩn dụ, bối cảnh, quan hệ nhân vật
- Khung beat trừu tượng: "0–2s <loại hành động>, 2–8s <…>, …" (không chứa nội dung cụ thể của mẫu)

## 9. Không được chép
Thoại đặc trưng, câu chốt, chữ nổi đặc trưng, chuỗi hành động đặc trưng, đồ vật / hình ảnh nhận diện, tên nhân vật
hay thương hiệu của kênh. Mỗi mục một dòng, trích nguyên văn để review dò được (MAU-01).

## 10. Đề xuất bổ sung nghề (nếu có)
Kỹ thuật thấy trong mẫu mà shared/nghe/ chưa có. Chỉ đề xuất, không tự sửa shared/.
```

### Luật viết

- **Mọi nhận định ở mục 4–5 có bằng chứng**: mốc giây, số đo trong `canh.json`, hoặc bình luận. Không có thì không viết.
- **Tách đo được và suy đoán.** "Cắt 6 lần trong 3 giây đầu" là đo được. "Người 22–25 thấy mình trong đó" là suy đoán.
  View cao không chứng minh lý do: không viết "video viral vì …" như một sự thật.
- **Gọi tên bằng từ vựng nghề có sẵn** (`HK-Dxx`, tên kỹ thuật, tên cơ chế hài). Hook không khớp dạng nào: ghi
  "không khớp dạng có sẵn", tả ba lớp hình / âm / chữ, đưa vào mục 10. Chỉ gắn lỗi `HK-01` khi ba giây đầu thật sự không
  có lý do để dừng lướt, không gắn chỉ vì không khớp dạng.
- **Mẫu khác dạng** (vlog, quảng cáo, phim ngang, video lịch sử…): vẫn đi đủ 10 mục, nhưng mục 5 tách rõ điều nào thu
  hút **nhờ bối cảnh riêng của video đó** (nổi tiếng sẵn, sự kiện, "video đầu tiên"…) và không học được.
- Mục 8 không được chứa nội dung cụ thể của mẫu; mục 9 thì trích nguyên văn.
- Mẫu flop: mục 5 thành "Vì sao không giữ được người xem", mỗi điểm gắn mã lỗi; mục 8 thành "Điều cần tránh".

## Bước 4: Tự kiểm trước khi trả

- [ ] Đã xem hết các file lưới, dòng thời gian phủ từ 0 tới hết thời lượng.
- [ ] Số trong mục 3 khớp `canh.json`; số liệu ở đầu file khớp `meta.json`.
- [ ] Mỗi dòng mục 5 có bằng chứng và nhãn đo được / suy đoán.
- [ ] Mục 7 đã đối chiếu điều kiện sản xuất (đặc biệt số nhân vật nữ lộ mặt, cảnh cần hai máy).
- [ ] Mục 8 không còn tên riêng, thoại hay đồ vật đặc trưng của mẫu.
- [ ] Mục 9 có ít nhất câu chốt và hook của mẫu (nếu có lời).

## Bước 5: Báo người dùng

Không đưa nguyên file. Đưa:

```
Mẫu: <tiêu đề> · <thời lượng> · <view> view
5 điểm làm video này thu hút:
1. <điểm> (<bằng chứng ngắn>)
…
Công thức: <một dòng khung beat>
Làm lại với đội mình: <được hết | cần thay: …>
File: <đường dẫn phan-tich.md>
```

Chế độ độc lập: hỏi thêm "Lưu vào thư viện mẫu để dùng lại không?" (xem mục Thư viện). Chế độ trong luồng: `vid-flow`
tự hỏi, skill này không hỏi.

### Nhiều mẫu: `tong-hop.md`

Sau khi có từng `phan-tich.md`: bảng so mục 3–4 của các mẫu; **điểm chung** (công thức lặp lại ở nhiều video thì đáng tin
hơn một video); điểm riêng của từng mẫu; một công thức chung ở dạng mục 8.

---

## Thư viện mẫu

`shared/tham-khao/mau/` giữ các bản phân tích đã duyệt để lần sau dùng lại mà không phân tích lại.

- **Chỉ ghi khi người dùng đồng ý.** Đây là ngoại lệ duy nhất cho luật "không tự ghi vào `tham-khao/`".
- Lưu: chép `phan-tich.md` thành `shared/tham-khao/mau/<slug>.md`, thêm một dòng vào `shared/tham-khao/mau/INDEX.md`.
  **Không** lưu video, ảnh, âm thanh vào thư viện (nặng, và là nội dung của người khác).
- Trùng nguồn với một mục đã có: hỏi ghi đè hay giữ cả hai.
- Dùng lại: người dùng nói "theo mẫu <slug>" thì `vid-flow` đọc file trong thư viện, không chạy lại skill này.

## Tự cải thiện

- Gặp lỗi công cụ mới và đã tìm ra cách xử lý: thêm một dòng vào bảng **Bẫy đã gặp** dưới đây, báo người dùng một dòng.
  Lỗi nằm trong script thì sửa `shared/scripts/phan_tich_mau.py`, chạy lại trên video vừa lỗi để chứng minh đã hết.
- Mục 10 của các bản phân tích là nguồn bổ sung cho `shared/nghe/`. Cùng một kỹ thuật xuất hiện ở từ 3 mẫu trở lên thì
  đề xuất người dùng thêm vào file nghề tương ứng; chỉ sửa khi người dùng đồng ý.

### Bẫy đã gặp

| Hiện tượng | Nguyên nhân | Xử lý (đã có trong script / skill) |
|---|---|---|
| `open() got an unexpected keyword argument 'metadata_errors'` khi chép lời | faster-whisper 1.2 gọi PyAV kiểu cũ, PyAV mới đã bỏ tham số | Script tự đọc `am-thanh.wav` thành mảng rồi đưa cho whisper, không qua PyAV |
| Cảnh báo symlink / HF_TOKEN của huggingface khi tải mô hình | Windows không bật Developer Mode; tải ẩn danh | Vô hại; script tắt hai cảnh báo này |
| Lời chép sai từ (ví dụ "trunks" thành "punks" với model base) | Model nhỏ | Mặc định dùng `small`; đối chiếu phụ đề `.vtt` và chữ trên màn hình |
| Lời bịa ra ở video chỉ có nhạc | Whisper đoán lời bài hát | Bỏ đoạn không khớp hình, hoặc chạy `--khong-chep` |
| Lệnh `chay` lần đầu bị cắt ở 10 phút | Tải mô hình small mất 10–15 phút | Lần đầu chạy nền (bước 0) |
| `comment_count` nhỏ vô lý (bằng số bình luận tải về) | yt-dlp ghi đè tổng số bằng số đã tải | Script đặt `null` kèm `ghi_chu_comment_count`; ghi "không rõ" |
| 60 bình luận tải về gần hết là trả lời của một bình luận | YouTube trả cả luồng trả lời | Script chỉ tải bình luận gốc |
| Một đoạn lời dài 8 giây, mốc giây thô | Whisper gộp nhiều câu thành một đoạn | Script lấy mốc từng từ rồi chia lại theo quãng nghỉ ≥ 0,6s và dấu câu |
| Lời whisper sai chữ dù độ tin cậy cao ("one of" thay "in front of") | Giới hạn của mô hình | Tin chữ trên màn hình > `.vtt` > whisper (bước 2) |
| `UnicodeEncodeError: 'charmap'` khi in json bằng `py -I -c` | `-I` bỏ qua cấu hình mã hoá trên Windows | Đọc file bằng Read, không in bằng Python |

## Không làm

- Không viết kịch bản, không đề xuất concept (việc của `vid-brainstorm`).
- Không chép thoại, câu chốt, chuỗi hành động của mẫu vào mục 8.
- Không khẳng định nguyên nhân viral như sự thật khi chỉ có số view.
- Không lưu vào `shared/tham-khao/mau/` khi người dùng chưa đồng ý; không lưu video, ảnh, âm thanh vào thư viện.
- Không tải lại hay đăng lại video mẫu ra ngoài; file tải về chỉ để phân tích trong thư mục dự án.
- Không bắt người dùng tự cài công cụ khi skill tự cài được.
