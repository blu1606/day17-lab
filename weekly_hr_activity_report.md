# 📊 Báo cáo Hoạt động Tuần & MVP Validation (Weekly HR Activity Report)
**Dự án:** AI Trợ Lý (Phân khúc Nhân sự - HR) — Nhóm 09  
**Nội dung thử nghiệm:** Lộ trình AI sát công việc HR (Tuần 1: Luyện viết Prompt tuyển dụng)  
**Quy mô mẫu test:** 8 nhân viên HR thực tế  
**Phương pháp xác minh:** Wizard of Oz (Google Doc lộ trình + Nhóm tương tác Zalo hỗ trợ prompt tức thời)  
**Thời gian tạo:** Thứ Sáu lúc 22:00 (Hệ thống tự động đồng bộ hàng tuần)

---

## 1. Kết quả Kiểm chứng Giả định Rủi ro nhất (Hypothesis Validation)

Giả định cốt lõi: *"Nếu áp dụng lộ trình SÁT công việc HR, nhân viên HR sẽ thấy hiệu quả thật và tự giác học + sử dụng mỗi ngày."*

### ⚡ Lớp 1 — Đo lường Hiệu quả thật
- **Tiêu chí PASS:** Tiết kiệm trung bình $\ge$ 3 giờ/người/tuần + mỗi người kể được ít nhất 2 tác vụ làm được bằng AI.
- **Kết quả thực tế:** 
  - **Giờ tiết kiệm trung bình:** **3.4 giờ/người/tuần** ➔ **[ĐẠT - PASS]**
  - **Tác vụ cụ thể đã thực hiện thành công nhờ AI:**
    1. Soạn JD tuyển dụng các vị trí kỹ thuật phức tạp (Python Developer, Data Engineer).
    2. Sàng lọc & tóm tắt nhanh nội dung của 20+ CV ứng viên gửi về.
    3. Viết email mời phỏng vấn & soạn thư từ chối ứng viên lịch sự, chuẩn văn hóa doanh nghiệp.

### 🔁 Lớp 2 — Đo lường Tần suất sử dụng mỗi ngày (Habit Risk)
- **Tiêu chí PASS:** $\ge$ 60% người test (tương đương $\ge$ 5/8 người) tự giác active $\ge$ 4 ngày/tuần không cần nhắc.
- **Kết quả thực tế:**
  - **Số ngày active trung bình:** 4.5 ngày/tuần.
  - **Tỉ lệ người tự giác active $\ge$ 4 ngày/tuần:** **75%** (6 trên 8 người dùng) ➔ **[ĐẠT - PASS]**
  - **Chi tiết danh sách người đạt tiêu chí:** Nguyễn Văn A, Trần Thị B, Lê Hoàng C, Phạm Văn D, Đỗ Thị E, Vũ Văn F.

➔ **KẾT LUẬN CHUNG:** Giả định cốt lõi **HOÀN TOÀN ĐẠT (PASS)**. Nhóm đủ điều kiện để bắt đầu viết code triển khai phiên bản lộ trình HR thật trên ứng dụng Web/App.

---

## 2. Nhật ký An toàn Học thuật & Hỗ trợ (Sentinel Logs)

Hệ thống ghi nhận mức độ tương tác và phát hiện sao chép prompt mẫu của học viên:
- **Tỉ lệ xem gợi ý gợi mở (Socratic) (Hint ladder):** 82% (Học viên có xu hướng xem gợi ý gợi mở để tự viết prompt riêng giúp tối ưu hóa hiệu quả câu lệnh của mình).
- **Hành vi dán prompt mẫu trực tiếp bị phát hiện:**
  - Đã kích hoạt **12 lượt cảnh báo** trên màn hình giả lập khi học viên copy-paste nguyên văn prompt mẫu có sẵn mà không chịu điền thông tin bối cảnh riêng của doanh nghiệp.
  - **Danh sách 2 học viên cần hỗ trợ 1-1** (Gặp khó khăn khi viết prompt chi tiết, có xu hướng dán prompt mẫu nhiều lần):
    1. *Nguyễn Văn A* (Paste 5 lần, ELO hiện tại: 1050)
    2. *Trần Thị B* (Paste 4 lần, ELO hiện tại: 1090)

---

## 3. Đề xuất Dàn Bài Giảng Lại (AI Reteach Slide Plan)
*Hệ thống tự động đề xuất dàn slide bổ trợ cho buổi họp review tuần của HR Manager dựa trên khó khăn thực tế của nhân viên.*

### Slide 1: Prompt Chung Chung vs. Prompt Trúng Việc
- **Nội dung:** So sánh kết quả AI viết JD khi dùng câu lệnh sơ sài (ví dụ: *"Hãy viết JD Python Dev"*) so với câu lệnh đầy đủ bối cảnh đãi ngộ, kinh nghiệm.
- **Phân tích lỗi:** Chỉ ra tại sao câu lệnh thiếu thông tin dẫn đến JD bị chung chung, không tuyển được người phù hợp.

### Slide 2: Công thức Prompt 4 thành phần cho HR
- **Nội dung:** Hướng dẫn cấu trúc chuẩn của một prompt tuyển dụng:
  1. **Role (Vai trò):** Đóng vai là nhà tuyển dụng chuyên nghiệp...
  2. **Context (Bối cảnh):** Quy mô công ty, văn hóa làm việc...
  3. **Task (Nhiệm vụ):** Viết email mời phỏng vấn hoặc soạn JD...
  4. **Output Format (Định dạng):** Độ dài, ngôn ngữ, giọng điệu...

### Slide 3: Thực hành nhanh tại lớp (5 phút)
- **Nhiệm vụ:** Soạn prompt yêu cầu AI viết email chào mừng nhân viên mới (Onboarding Email).
- **Yêu cầu:** Mọi người tự viết tay prompt riêng, không sao chép mẫu có sẵn.

---

## 4. Câu hỏi Khảo sát Phản hồi (Wizard of Oz Feedback)

*Vui lòng phản hồi nhanh 3 câu hỏi dưới đây:*
1. Dữ liệu báo cáo hiệu suất và số giờ tiết kiệm của nhân viên HR tuần này có đủ thuyết phục thầy/cô duyệt ngân sách mua sản phẩm không?
2. Thầy/cô có muốn bổ sung thêm các tác vụ HR nào khác vào Lộ trình AI tuần tới không?
3. Thầy/cô thấy giao diện và báo cáo này hiển thị rõ ràng, trực quan chưa?
