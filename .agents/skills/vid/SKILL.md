---
name: vid
description: "Cửa vào duy nhất của bộ skill kịch bản video ngắn dọc (TikTok / YouTube Shorts) mang chất điện ảnh, tông cảm xúc do người dùng chọn hoặc skill đề xuất (không mặc định hài hay ẩn dụ), khán giả 17–30. Gọi trống thì hiện menu (làm video mới, làm tiếp dự án dở, mổ video mẫu, review kịch bản có sẵn, lên series); có đối số thì tự chọn hướng: câu ý tưởng → làm video mới; link / file video → phân tích mẫu rồi làm theo; du-an/... hoặc 'tiếp' → làm tiếp; file .xlsx / .json → review; 'series' → lên series. Luồng làm video: chốt brief một lượt hỏi, brainstorm, chọn concept bằng thẻ xem trước, viết kịch bản theo format Excel của team (mỗi kịch bản một sheet có tổng quan), review bằng agent độc lập, sửa tối đa 2 vòng (chế độ nhanh 1 vòng), duyệt, xuất Excel kèm gói bàn giao. Làm được nhiều video một lượt. Giữ trạng thái để làm tiếp. Dùng khi user gõ /vid, nói 'làm kịch bản', 'có ý tưởng video', 'làm video từ mẫu này', 'làm theo video <link>', 'theo mẫu <tên>', 'làm 3 video về …', 'làm nhanh', 'tiếp tục kịch bản'."
---

# vid

File này do `shared/scripts/dong_bo_codex.py` sinh ra, không sửa tay.

Nội dung skill nằm ở `.claude/skills/vid/SKILL.md`, dùng chung với Claude Code. Đọc toàn bộ file đó rồi làm đúng theo.
Đường dẫn trong đó tính từ thư mục gốc repo. Đầu vào là lời người dùng sau `$vid`.
