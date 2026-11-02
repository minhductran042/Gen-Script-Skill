---
name: vid-brainstorm
description: "Brainstorm concept video ngắn dọc mang chất điện ảnh cho khán giả 17–30 trên TikTok / YouTube Shorts, theo tông cảm xúc người dùng chọn hoặc tự đề xuất (không mặc định hài hay ẩn dụ). Đi qua năm pha: đào vấn đề thật (insight), phân kỳ ít nhất 15 ý thô qua các lăng kính ẩn dụ (đồ vật, tình huống song song, phóng đại thể loại, nhân hoá, thế giới đảo luật, đảo vai) và kể thẳng (sự thật trần trụi, khoảnh khắc nhỏ, bí mật hé dần, đổi góc nhìn, nhảy thời gian), hội tụ bằng ma trận chấm điểm, phát triển thành thẻ concept (logline, tông cảm xúc, hook có mã dạng, cách kể, beat lật, kết, nhân vật, bối cảnh, rủi ro quay), rồi tự phản biện từng concept. Nhận đầu vào là ý tưởng thô, hoặc video / kịch bản mẫu mà người dùng muốn học cấu trúc rồi biến tấu khác đi. Dùng khi user nói 'brainstorm video', 'nghĩ ý tưởng', 'cho vài concept', 'từ video mẫu này nghĩ cái khác', 'ý tưởng về <chủ đề>'. Viết kịch bản đầy đủ thì dùng vid-viet-kich-ban; chạy cả quy trình thì dùng /vid."
argument-hint: <ý tưởng | đường dẫn 00-brief.md>
---

# Brainstorm concept

Mục tiêu: đưa người dùng **5–8 concept khác nhau thật sự**, mỗi concept đủ rõ để viết kịch bản ngay, và đã tự loại
những ý không quay được hoặc không giữ chân được.

## Kiến thức dùng

Luôn đọc:
- `du-an/*/06-sau-dang.md` nếu có: tông, hook nào đang hiệu quả với khán giả thật; chỉ để tham khảo, không giới hạn ý.
- `shared/nghe/chu-de-va-thong-diep.md`: 8 nhóm chủ đề, lồng câu chuyện với thông điệp, ghép chủ đề, xử lý đầu vào chưa rõ.
- `shared/nghe/khan-gia-va-nen-tang.md`: chọn nhóm khán giả, kiểm relatable.
- `shared/nghe/tong-cam-xuc.md`: ba trục tông, tám cảm xúc và cơ chế của từng cảm xúc.
- `shared/nghe/an-du-va-hai.md`: tìm và chấm ẩn dụ, cơ chế hài, kho bối cảnh / đồ vật. Chỉ dùng khi tông có ẩn dụ hoặc hài.
- `shared/nghe/hook-va-giu-chan.md`: mã dạng hook `HK-Dxx`, kiểu kết.
- `shared/nghe/cau-truc-va-nhip.md`: logline, câu hỏi kịch tính, các cấu trúc khác.
- `shared/luat/dieu-kien-san-xuat.md` mục 5: kiểm quay được.
- `shared/luat/vung-cam.md`.

Tham khảo: **chỉ khi brief ghi ở mục "Tham khảo"**, và chỉ đọc đúng thứ được nêu. Không có thì sáng tác tự do trong
khuôn luật và nghề. Không lấy nội dung trong `shared/mau-format/` làm ý tưởng hay ví dụ.

## Đầu vào

- `00-brief.md` (khi chạy từ /vid), hoặc lời người dùng.
- Gọi trực tiếp mà thiếu thời lượng: hỏi một lần, gộp các câu.
- Mục "Chế độ" của brief là **nhanh**: pha 2 tối thiểu 8 ý thô (trải đủ các nhóm lăng kính đang dùng), pha 3 chọn 3 concept (vẫn giữ một
  concept "liều" nếu có ý đủ lạ), pha 5 chỉ ghi điểm yếu nhất và cách sửa. Các luật loại ý (quay được, vùng cấm) giữ
  nguyên.
- Đầu vào chưa rõ chủ đề, câu chuyện hay thông điệp: xử lý theo `chu-de-va-thong-diep.md` mục 3, không chặn lại hỏi
  trừ trường hợp hoàn toàn không có chủ đề.

---

## Pha 1: Đào vấn đề

Ý tưởng người dùng đưa thường là một **chủ đề** ("chuyện tình yêu thời nay"). Concept tốt cần một **insight**: một sự
thật cụ thể (thường hơi đau, nhưng cũng có thể buồn cười, đáng sợ hay đáng tự hào) mà người xem nhận ra là đúng với mình nhưng chưa ai nói ra.

Trước tiên, đọc **tông** trong brief (`tong-cam-xuc.md` mục 2). Đã chốt thì mọi concept theo tông đó. "Để skill
đề xuất" hoặc chưa có thì mỗi concept tự mang tông suy từ insight, theo luật đa dạng ở mục 2 của file đó.

Rồi xác định **nhóm chủ đề** (`chu-de-va-thong-diep.md` mục 2):

- Brief chỉ có một nhóm: chọn 3–4 chủ đề con khác nhau trong nhóm, và thêm ít nhất **một cặp ghép** với nhóm khác (mục 1,
  bảng ghép).
- Brief không có nhóm (người dùng nói "tuỳ"): chọn 3 nhóm xa nhau.
- Dùng insight mẫu, hình ảnh và bẫy của nhóm để kích ý và để tránh, không chép nguyên insight mẫu.

Rồi với từng chủ đề con, trả lời các câu hỏi sau (ghi ngắn vào `01-concepts.md` mục "Insight"):

1. Chủ đề này xảy ra **ở đâu, lúc nào, với đồ vật gì** trong một ngày của người 17–30?
2. Người ta **làm gì** khi gặp nó (hành vi), khác với **nói gì** về nó (lời)? Khoảng lệch giữa làm và nói là mỏ kịch tính: hài hay đau là tuỳ tông.
3. Điều gì người ta **ngại thừa nhận** về nó?
4. Có **thói quen nhỏ** nào ai cũng có liên quan tới nó?
5. Chủ đề này **khác nhau thế nào** giữa ba nhóm tuổi 17–21, 22–25, 26–30?
6. Nếu phóng đại nó lên 10 lần thì nó thành cái gì?
7. Nếu kể thẳng, không đùa, thì **khoảnh khắc nào** làm người ta nghẹn, sợ hoặc rung động nhất?

Rút ra **3–5 insight**, mỗi insight một câu cụ thể. Ví dụ minh hoạ: chủ đề "bận rộn" → insight "ta trả lời tin nhắn công
việc trong 30 giây, nhưng để tin nhắn của mẹ tới tối".

## Pha 2: Phân kỳ (ít nhất 15 ý thô)

Với mỗi insight, cho ý thô đi qua các lăng kính theo Cách kể trong brief. Mỗi ý thô chỉ một dòng.

| Cách kể | Lăng kính dùng |
|---|---|
| Kể thẳng đời thực | Nhóm B |
| Ẩn dụ | Nhóm A (trừ khi người dùng muốn thêm) |
| Mượn thể loại | Phóng đại thể loại (quay nghiêm túc được, không cần hài) + nhóm B |
| Để skill đề xuất | Cả hai nhóm, mỗi nhóm ít nhất 6 ý |

**Nhóm A: ẩn dụ** (chi tiết ở `an-du-va-hai.md` mục 2)

| Lăng kính | Câu hỏi kích ý |
|---|---|
| Đồ vật | Đồ vật đời thường nào có cùng thuộc tính với insight? (đi qua kho bối cảnh ở `an-du-va-hai.md` mục 4) |
| Tình huống song song | Chuyện nhỏ nào diễn ra y hệt insight? |
| Phóng đại thể loại | Nếu quay insight này như phim hành động / kinh dị / tài liệu / toà án / thể thao thì sao? |
| Nhân hoá | Nếu cảm xúc / khái niệm này là một người thì nó trông thế nào, làm gì? |
| Thế giới đảo luật | Luật lạ nào làm insight hiện ra rõ? ("Nếu mỗi lần nói dối thì …") |
| Đảo vai | Đổi vai ai với ai thì insight lộ ra? |

**Nhóm B: kể thẳng**

| Lăng kính | Câu hỏi kích ý |
|---|---|
| Sự thật trần trụi | Nếu quay đúng chuyện này, không tô vẽ, thì cảnh nào khó xem nhất? |
| Khoảnh khắc nhỏ | Một cử chỉ, một tin nhắn, một giây nào chứa hết chuyện này? |
| Bí mật hé dần | Người xem nên biết điều gì trước nhân vật, và biết lúc nào? |
| Đổi góc nhìn | Kể từ phía người bị bỏ quên trong chuyện này thì khác thế nào? |
| Nhảy thời gian | Cùng một nơi, cùng một việc, ở hai thời điểm thì thấy gì? |

Luật phân kỳ:

- **Chưa chấm, chưa loại** trong pha này. Ý nghe ngớ ngẩn vẫn ghi.
- Mỗi lăng kính đang dùng ít nhất 2 ý (khi dùng cả hai nhóm thì ít nhất 1). Tổng ít nhất 15 ý thô.
- Ghi vào `01-concepts.md` mục "Ý thô" dạng `| # | Insight | Lăng kính | Cảm xúc | Ý (1 dòng) |`.

## Pha 3: Hội tụ

Chấm mọi ý thô theo ma trận dưới (1–5 điểm mỗi tiêu chí), ghi vào bảng ý thô:

| Tiêu chí | 1 điểm | 5 điểm |
|---|---|---|
| **Relatable** | Chỉ vài người hiểu | Ai trong nhóm khán giả chính cũng "y hệt mình" |
| **Khớp tông** | Không rõ gây cảm xúc gì, hoặc lệch tông đã chọn | Thấy rõ khoảnh khắc gây đúng cảm xúc, theo đúng cơ chế ở `tong-cam-xuc.md` mục 3 |
| **Sức hook** | Không nghĩ ra khung đầu nào lạ | Đã thấy rõ khung hình đầu tiên |
| **Độ mới** | Đã thấy nhiều trên nền tảng | Góc nhìn, tình huống hoặc hình ảnh chưa ai làm |
| **Chất điện ảnh** | Chỉ kể được bằng thoại | Kể được bằng hình, có đặc tả, có khoảnh khắc lặng |
| **Quay được** | Cần nhiều bối cảnh, người, thiết bị | 1–2 bối cảnh, ≤ 4 người, đồ có sẵn |

Chọn ra 5–8 ý để phát triển:

- Lấy theo tổng điểm từ cao xuống.
- **Loại ngay** ý có "Quay được" = 1 hoặc chạm vùng cấm, bất kể tổng điểm.
- **Bảo đảm đa dạng**: các concept cuối cùng không trùng ẩn dụ, và trải ít nhất 3 lăng kính và 3 dạng hook khác nhau.
  Tông do skill đề xuất thì thêm luật đa dạng ở `tong-cam-xuc.md` mục 2.
- **Đa dạng khuôn truyện**: không quá một nửa concept cùng một cấu trúc hoặc cùng một kiểu kết (chế độ nhanh: ít nhất 2
  kiểu). Cấu trúc chọn theo cảm xúc ở `tong-cam-xuc.md` mục 6, không mặc định có lật và miếng thoát.
- Giữ **một concept "liều"**: điểm không cao nhất nhưng lạ nhất. Đánh dấu `(liều)`.
- Brief không giới hạn nhóm chủ đề: các concept trải ít nhất 2 nhóm chủ đề.

## Pha 4: Phát triển thẻ concept

Mỗi concept một thẻ:

```markdown
### C<n>. <Tên concept> — Title: <TITLE IN HOA>
- **Nhóm chủ đề:** <nhóm> (+ <nhóm ghép> nếu có) · Chủ đề con: <…>
- **Tông:** <cảm xúc> · <cách kể> · <độ hài> · Đường cảm xúc: <nếu có>
- **Insight:** <một câu>
- **Câu chuyện bề mặt:** <tình huống cụ thể, một câu>
- **Thông điệp** (bỏ dòng này nếu Không) **(kiểu <phát hiện / nghịch lý / đánh đổi / nhìn lại / cho phép / đảo góc nhìn>):** <một câu dưới 15 từ>
- **Logline:** <Nhân vật> muốn <…> nhưng <…>, cho tới khi <…>.
- **Câu hỏi kịch tính:** <người xem chờ câu trả lời gì>
- **Cơ chế cảm xúc:** <cơ chế theo `tong-cam-xuc.md` mục 3, gắn với khoảnh khắc cụ thể trong concept>
- **Ẩn dụ** (bỏ dòng này nếu không dùng ẩn dụ): <hình ảnh> = <vấn đề>. Điểm khớp: <thuộc tính chung>. Diễn biến của đồ vật: <từ … tới …>
- **Hook (HK-Dxx – <tên dạng>):** <khung hình đầu + âm thanh + chữ nổi nếu có>
- **Cấu trúc:** <khung mặc định | kết quả trước | lặp ba lần | …>
- **Diễn biến chính:** <các chặng theo cấu trúc đã chọn; có lật thì ghi lật>
- **Kết (<dạng kết>):** <…>. Câu đọng: "<…>"
- **Cơ chế hài** (bỏ dòng này nếu Độ hài là Không): <cơ chế, kèm ví dụ cụ thể trong concept>
- **Khoảnh khắc điện ảnh:** <đặc tả / ánh sáng / âm thanh đắt nhất>
- **Khán giả chính:** <nhóm tuổi> · Người xem sẽ gửi cho ai, kèm câu gì: <…>
- **Nhân vật:** <số người, vai, tính cách một dòng>
- **Bối cảnh:** <1–2 nơi> · **Đạo cụ chính:** <…>
- **Rủi ro quay:** <cảnh nào khó với một máy quay, cần gì>
- **Làm series được không:** <có / không, công thức lặp nếu có>
```

## Pha 5: Tự phản biện

Với mỗi concept, đóng vai người phản biện và ghi 2–3 dòng dưới thẻ, mục "Phản biện":

- **Ba giây:** khung đầu có đủ để dừng lướt không?
- **Đoán kết:** người xem có đoán được kết từ hook không?
- **Đã thấy chưa:** ý này có quá quen trên nền tảng không?
- **Tông:** concept có thật sự gây đúng cảm xúc không, hay đang trôi về hài và ẩn dụ theo quán tính? Có rơi vào bẫy của cảm
  xúc đó không?
- **Lồng ghép** (chỉ khi có thông điệp)**:** bỏ thông điệp đi thì câu chuyện bề mặt còn xem được không? Thông điệp có thành mệnh lệnh không?
- **Bẫy của nhóm chủ đề:** concept có rơi vào bẫy ghi ở nhóm đó không?
- **Điểm yếu nhất** của concept là gì, và sửa được bằng cách nào?

Điểm yếu không sửa được thì thay concept đó bằng ý thô kế tiếp ở pha 3.

---

## Đầu vào có video / kịch bản mẫu

Chỉ áp khi brief ghi mẫu ở mục "Tham khảo", hoặc người dùng đưa mẫu trực tiếp. Không có mẫu thì bỏ qua mục này.

Skill này **không tự phân tích mẫu**. Cần có `phan-tich.md` do `vid-phan-tich-mau` viết (trong `du-an/<dự án>/mau/<k>/`
hoặc `shared/tham-khao/mau/<slug>.md` nếu lấy từ thư viện). Người dùng đưa mẫu trực tiếp mà chưa có bản phân tích thì
chạy `vid-phan-tich-mau` trước.

Đọc thêm `shared/luat/bam-mau.md`, rồi:

1. Chép mục 8 "Công thức rút gọn" của bản phân tích vào `01-concepts.md` mục "Cấu trúc rút từ mẫu", kèm mức bám và
   phần "học từ mẫu" ghi trong brief.
2. Chạy pha 1–5 như bình thường; insight ở pha 1 là của mình, **không lấy insight của mẫu**. Ràng buộc thêm ở pha 2 theo
   mức bám:
   - **Cảm hứng:** chỉ giữ thứ người dùng chỉ ra; các lăng kính chạy tự do.
   - **Cùng công thức:** giữ phần "Giữ" của mục 8, đổi ít nhất 3 trong 4 biến số.
   - **Bắt trend:** giữ phần nhận diện của trend, mọi ý thô phải có một cú lật riêng.
3. Ở pha 3, chấm thêm tiêu chí **"Khác mẫu"** (1 = gần như bản sao, 5 = chỉ còn công thức); loại ý có điểm 1.
4. Mỗi thẻ concept ghi thêm dòng **"Khác mẫu ở:"** (đổi những biến số nào) và **"Học từ mẫu:"** (giữ kỹ thuật nào).
5. Phản biện ở pha 5 thêm câu: có câu thoại, hình ảnh nào trùng mục 9 "Không được chép" không?
6. Nhiều mẫu có `tong-hop.md`: dùng công thức chung ở đó; concept có thể lấy hook của mẫu này, nhịp của mẫu kia.

---

## Đầu ra: `01-concepts.md`

```markdown
# Concept: <tên brief>

## Tóm tắt (để người dùng chọn)
| # | Tên / Title | Tông | Chủ đề | Thông điệp (nếu có) | Hook | Nhân vật · Bối cảnh | Độ khó quay | Điểm mạnh nhất |
(xếp theo tổng điểm pha 3 từ cao xuống)

## Thẻ xem trước
Mỗi concept đúng 6 dòng, mỗi dòng dưới khoảng 70 ký tự, để `/vid` đặt cạnh nút chọn:
### C<n>
Logline: <…>
Hook: <HK-Dxx> <khung đầu>
Tông: <cảm xúc> · <cách kể> · <độ hài>
Kết: <câu đọng>
Vai · nơi: <số người, nam / nữ> · <bối cảnh>
Độ khó quay: <Dễ | Vừa | Khó> · <điểm mạnh nhất>

## Insight
## Cấu trúc rút từ mẫu (nếu có)
## Ý thô (bảng phân kỳ + điểm)
## Concept (thẻ + phản biện)
## Tham khảo đã dùng
<"không" hoặc danh sách>
```

Độ khó quay: **Dễ** (1 bối cảnh, ≤ 3 người, không cảnh ghép), **Vừa**, **Khó** (2 bối cảnh hoặc ≥ 5 người hoặc có cảnh
ghép / quay một lần).

## Không làm

- Không viết kịch bản đầy đủ ở bước này.
- Không thêm hài hay ẩn dụ vào concept khi tông không có.
- Không tự chọn concept thay người dùng.
- Không chép thoại, cảnh hay chuỗi hành động của mẫu.
- Không tự phân tích video mẫu (việc của `vid-phan-tich-mau`).
- Không tự ghi vào `shared/tham-khao/`.
