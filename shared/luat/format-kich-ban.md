# Format kịch bản

Luật bắt buộc. Định dạng lấy từ file mẫu của team: `shared/mau-format/du-anh-demo.xlsx`. File đó **chỉ là mẫu định
dạng**: dùng để biết cột, bố cục và cách trình bày ô. Không học nội dung, giọng văn, hook hay ẩn dụ từ đó.

Script `kich_ban.py xuat` sinh đúng định dạng này. Không đổi tên hay thứ tự cột.

---

## 1. Bố cục một kịch bản trong Excel

| Dòng | Nội dung | Mẫu |
|---|---|---|
| 1 | Tên kịch bản + thời lượng, chữ đậm | `Kịch bản <số>: <tên> (Thời lượng dự kiến: <thời lượng>)` |
| 2 | Thời điểm – Nội/Ngoại (tuỳ chọn, gộp ô A:Z) | `<SÁNG / TRƯA / CHIỀU / ĐÊM> - <Nội / Ngoại>` |
| 3 | Đạo cụ | `Đạo cụ: <liệt kê đủ, kèm số lượng>` |
| 4 | Dòng tiêu đề cột, nền vàng | Xem mục 2 |
| 5… | Mỗi dòng một beat | |

Nhiều kịch bản nối tiếp nhau trong cùng một sheet, không có dòng trống ở giữa.

Định dạng ô (script tự áp): font Google Sans cỡ 8 (dòng tên kịch bản in đậm), nội dung Google Sans Text cỡ 8 nghiêng, màu
`#1F1F1F`, dòng tiêu đề cột nền vàng `#FFFF00`, cột F rộng 32.25, cột J rộng 11.25, ô tự xuống dòng.

## 2. Cách viết từng cột

Một dòng là **một beat**: một đơn vị chức năng của câu chuyện (xem `shared/nghe/cau-truc-va-nhip.md`). Không phải mỗi
câu thoại một dòng, cũng không phải cả cảnh một dòng.

### A. STT

Số thứ tự kịch bản. Chỉ ghi ở dòng beat đầu tiên.

### B. Tóm tắt – Title

Chỉ ghi ở dòng beat đầu. Gồm hai phần:

- **Tóm tắt** 1–2 câu: ai, tình huống gì, đi tới đâu. Viết như logline, không kể lại từng beat.
- `Title: <TIÊU ĐỀ IN HOA>`: tiêu đề hiện trên video hoặc làm caption. Ngắn (2–6 từ), gợi tò mò, không lộ kết.

| Kém | Tốt |
|---|---|
| Title: CÂU CHUYỆN VỀ SỰ KIÊN NHẪN | Title: ĐỢI THÊM 5 PHÚT? |

### C. Địa điểm

Bối cảnh cụ thể đủ để người quay chọn được chỗ: "Ban công phòng trọ tầng 4, nhìn ra dãy nhà đối diện", không chỉ "phòng
trọ". Chỉ ghi ở dòng đầu, trừ khi beat đổi địa điểm.

### D. Mục đích

Chức năng của beat, dùng tên trong khung beat: Hook, Thiết lập, Leo thang, Lật, Khoảng lặng, Chốt, Thoát. Có thể thêm
mô tả ngắn: `Leo thang – bạn cùng phòng vạch trần`.

- **Beat đầu bắt buộc** có chữ "Hook" và mốc giây: `Hook (0–3s)`.
- Các beat sau nên có mốc giây, để người review kiểm được nhịp.

### E. Nhân vật

Ai xuất hiện trong beat. Nối bằng `+`: `A + B`. Độc diễn: `A (Độc diễn)`. Giọng ngoài hình: `Voice A`.

- Dùng **cùng một tên** cho một nhân vật từ đầu tới cuối.
- Tổng số nhân vật khác nhau ≤ 6 (script kiểm).

### F. Nội dung

Phần quan trọng nhất. Viết **hành động trước, thoại sau**.

**Hành động:**

- Viết cái **máy quay thấy được**: tay làm gì, đồ vật nào, ai đi đâu. Không viết suy nghĩ.
- Động từ cụ thể: "đặt mạnh cốc xuống bàn", không viết "tỏ ra bực".
- Tiếng động đặc trưng ghi trong ngoặc kép: `"cạch"`, `"rè rè"`.
- Hành động có giây riêng trong beat thì ghi: `Hành động (0–2s): …`.

**Thoại:**

- Mẫu: `A: "…"`. Voice-over: `Voice A: "…"`. Thoại nghĩ trong đầu: `A (nghĩ): "…"`.
- Mỗi lượt thoại ngắn, ưu tiên dưới khoảng 20 từ. Nói như người trẻ nói ngoài đời.
- Chỉ dẫn diễn ngắn đặt trong ngoặc đơn **trước** câu thoại: `A (thở dài): "…"`. Không đặt ghi chú giữa câu thoại.

| Kém | Tốt |
|---|---|
| A buồn vì B không quan tâm mình. A: "Cậu không bao giờ quan tâm tới cảm xúc của tớ cả, lúc nào cũng chỉ có điện thoại thôi." | A đặt đĩa trái cây đã gọt lên bàn. B không ngẩng lên, tay vẫn lướt. A kéo đĩa về phía mình, ăn một miếng `"rộp"`. A: "Ngon phết." |

### G. Biểu cảm

Trạng thái cảm xúc của nhân vật trong beat, kèm biểu hiện nhìn thấy được nếu cần: `Ngượng – cười gượng, tránh nhìn`.
Nhiều nhân vật thì tách: `A: hào hứng; B: thờ ơ`.

### H. Góc quay

Dùng từ vựng chuẩn ở `shared/nghe/ngon-ngu-dien-anh.md` mục 2: Toàn, Trung, Trung hai người, Cận <ai>, Đặc tả <vật>,
Qua vai, POV, Góc thấp / cao, Từ sau lưng, Phản chiếu. Có chuyển động thì ghi thêm: `Cận A – đẩy vào chậm`.

Beat có nhiều góc thì ghi theo thứ tự: `Trung hai người → Cận B (phản ứng)`.

### I. Text nổi bật

Chữ hiện trên màn hình. Để trống nếu beat không cần.

- Hook: chữ đặt tình huống hoặc câu hỏi, 4–8 từ.
- Giữa video: chữ nhấn câu thoại đắt nhất, hoặc chữ hài (chú thích, đếm số).
- Beat chốt: câu đọng lại.
- Không chép lại phụ đề thoại vào cột này. Phụ đề là việc của người dựng.

### J. Ghi chú

Những gì người quay và người dựng cần biết:

- **Âm thanh**: tiếng động, nhạc (tính chất + lúc vào / ra), tắt lặng.
- **Ánh sáng**: nguồn sáng khi nó mang nghĩa.
- **Bắt nét, chuyển nét.**
- **Dựng**: ghép khung, jump cut, slow motion, đứng hình, giữ khung N giây.
- **Sản xuất**: "chỉ quay một lần", "cần 3 cốc dự phòng", "quay tách, ghép khi dựng".

## 3. Bản JSON (bản gốc để sửa)

Mọi kịch bản lưu dạng JSON. Excel chỉ là bản xuất ra từ JSON.

```json
{
  "du_an": "<tên sheet>",
  "kich_ban": [
    {
      "so": 1,
      "ten": "<tên kịch bản>",
      "thoi_luong": "~60s",
      "boi_canh": "<SÁNG - Nội>",
      "dao_cu": "<đạo cụ 1>, <đạo cụ 2>",
      "tom_tat": "<tóm tắt>",
      "title": "<TITLE IN HOA>",
      "dia_diem": "<bối cảnh>",
      "canh": [
        {
          "muc_dich": "<tên beat, beat đầu có chữ Hook>",
          "giay": "0–3s",
          "nhan_vat": "<A> + <B>",
          "noi_dung": "<hành động>\n<A>: \"<thoại>\"",
          "bieu_cam": "<cảm xúc>",
          "goc_quay": "<góc máy>",
          "text_noi_bat": "",
          "ghi_chu": "<âm thanh / ánh sáng / dựng / sản xuất>"
        }
      ]
    }
  ]
}
```

- `giay` bắt buộc ở beat Hook, nên có ở các beat còn lại. Khi xuất Excel, `giay` được nối vào cột Mục đích.
- Beat đổi địa điểm thì ghi thêm `canh[i].dia_diem`.
- Xuống dòng trong ô dùng `\n`.
