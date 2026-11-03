---
name: vid-review
description: "Review một kịch bản video ngắn dọc qua năm lượt đọc với năm vai: người lướt (3 giây đầu, tắt tiếng), người xem hết (nhịp, đoán kết, đúng cảm xúc, công cụ kể), đạo diễn (chất điện ảnh), đội sản xuất (một máy quay, sáu diễn viên, bối cảnh, đạo cụ, dựng), và nền tảng (vùng cấm, bản quyền). Mỗi lỗi có mã từ danh mục (HK, GC, AD, CX, DA, TH, KT, SX, AT, NH, SR), mức Nặng / Vừa / Nhẹ, vị trí beat và giây, trích nguyên văn, và gợi ý sửa viết sẵn. Chấm điểm theo bảng tiêu chí có mốc, kết luận ĐẠT / CHƯA ĐẠT, ghi điểm mạnh nên giữ. Nhận JSON hoặc file Excel đúng format team. Dùng khi user nói 'review kịch bản', 'kịch bản này ổn chưa', 'chấm kịch bản', 'chỗ nào chưa ổn', 'cải tiến kịch bản này', 'góp ý kịch bản'. Không sửa kịch bản (sửa thì dùng vid-viet-kich-ban chế độ sửa)."
---

# vid-review

File này do `shared/scripts/dong_bo_codex.py` sinh ra, không sửa tay.

Nội dung skill nằm ở `.claude/skills/vid-review/SKILL.md`, dùng chung với Claude Code. Đọc toàn bộ file đó rồi làm đúng theo.
Đường dẫn trong đó tính từ thư mục gốc repo. Đầu vào là lời người dùng sau `$vid-review`.
