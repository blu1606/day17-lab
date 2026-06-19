# Day 17 Lab Assignment - AI Prototyping & MVP (AI Trợ Lý - HR Persona)

Dự án **AI Trợ Lý** (Nhóm 09 - Vin AI thực chiến) là hệ thống đào tạo kỹ năng AI cá nhân hóa theo từng vai trò công việc. Bản thử nghiệm (Lab Day 17) này tập trung hoàn toàn vào phân khúc **Nhân viên Nhân sự (HR)**.

Tài liệu này trình bày các bước thực hiện bài Lab Day 17 để xác minh giả định quan trọng nhất của dự án bằng cách sử dụng các phương pháp thử nghiệm nhanh và rẻ hơn (Lean MVP/Wizard of Oz).

---

## 1. Giả thuyết Quan trọng Nhất (Riskiest Hypothesis)

- **Hypothesis:** "Nếu áp dụng phương pháp lộ trình SÁT công việc HR, thì nhân viên HR sẽ thấy phương pháp HIỆU QUẢ THẬT, và HỌC + ÁP DỤNG vào công việc MỖI NGÀY."
- **Loại rủi ro:** Rủi ro giá trị (Value Risk) & Rủi ro hành vi sử dụng (Usability/Habit Risk).
- **2 lớp con của giả định:**
  1. **Hiệu quả thật:** Lộ trình AI sát việc HR giúp tạo kết quả thật. Đo lường bằng: số giờ tiết kiệm/tuần (Mục tiêu: TB $\ge$ 3h/người/tuần) và kể được ít nhất 2 việc HR làm được nhờ AI.
  2. **Áp dụng mỗi ngày:** HR dùng đều đặn, không bỏ sau ngày đầu. Đo lường bằng: số ngày active/tuần (Mục tiêu: $\ge$ 60% người test tự dùng $\ge$ 4 ngày/tuần mà không cần nhắc).
- **Lưu ý:** Cố tình **chưa test** việc chi tiền, giới thiệu lên sếp, hay các vai trò khác để tránh làm nhiễu dữ liệu.

---

## 2. Cách Tiếp cận Thông thường (Tốn kém nhất)

Xây dựng toàn bộ hệ thống Web App hoàn chỉnh cho vai trò HR trước khi đi tìm người test:
1. Viết code Web App hoàn thiện bằng Next.js, Supabase, cài đặt cơ chế phân quyền, quản lý tài khoản.
2. Viết tay lộ trình HR đồ sộ (hơn 3 module kèm câu hỏi kiểm tra).
3. Tích hợp API OpenAI, LangChain để trợ lý AI streaming trực tiếp.
4. Xây dựng dashboard lưu nhật ký thời gian tiết kiệm và deploy lên Vercel.
- **Nhược điểm:** Tốn kém nhiều tuần code, chịu chi phí API cao khi chưa biết người dùng có thực sự cần hay không.

---

## 3. Ba (3) Cách Test Rẻ hơn để Kiểm chứng (Chi phí ≈ 0)

### Cách 1: Wizard of Oz cho HR ⭐ (Cách kiểm chứng chính)
- **Ý tưởng:** Chọn nhóm **5–8 HR thật**. Gửi lộ trình học qua Google Doc + lập một nhóm Zalo chung. Mỗi ngày giao 1 tác vụ HR cụ thể (ví dụ: "Dùng AI viết JD vị trí Python Developer"). Khi HR vướng mắc hoặc đặt câu hỏi, **founder tự tay đóng vai trợ lý AI** (sử dụng ChatGPT phía sau) trả lời bằng các ví dụ đúng nghiệp vụ HR.
- **Cách đo:** 
  - Cuối ngày khảo sát số giờ tiết kiệm và tác vụ làm được.
  - Theo dõi tỉ lệ người dùng tự giác tương tác $\ge$ 4 ngày/tuần.
- **Thời gian thực hiện:** Setup trong 0.5 ngày, chạy thử nghiệm trong 1 tuần.
- **File thực hiện:** `hr_prompter_simulator.py` (CLI mô phỏng cơ chế này).

### Cách 2: Form khảo sát hành vi HR
- **Ý tưởng:** Tạo Google Form liệt kê 8 tác vụ HR phổ biến (soạn JD, lọc CV, viết email mời phỏng vấn, soạn quy trình onboarding...). Hỏi xem tác vụ nào họ làm hàng ngày và muốn AI hỗ trợ nhất.
- **Cách đo:** Đánh giá mức độ khớp giữa nội dung lộ trình dự định xây dựng và công việc thực tế của họ.
- **Thời gian thực hiện:** 1 ngày.

### Cách 3: Clickable Prototype & Phỏng vấn
- **Ý tưởng:** Sử dụng lại Figma/HTML Mockup có sẵn của hệ thống lộ trình HR và prompt starter kit. Cho 3–5 HR tự thao tác bấm thử và thử nhập 1–2 prompt thực tế vào công việc của họ.
- **Cách đo:** Quan sát xem họ có tự hiểu giao diện không, prompt nào họ thấy hữu ích nhất để dùng hàng ngày và chỗ nào làm họ bối rối.
- **Thời gian thực hiện:** 2–3 ngày.
- **File thực hiện:** `hr_prompter_sandbox.html` (Bản HTML tương tác mô phỏng).

---

## 4. Hướng dẫn Chạy các Prototypes

### Bản 1: CLI Prompter Simulator cho HR
Chương trình dòng lệnh mô phỏng một phiên học viết prompt tuyển dụng của nhân viên HR với AI Trợ Lý. Hệ thống sẽ chấm điểm độ tinh thông viết prompt và ELO của bạn, cảnh báo nếu bạn lười suy nghĩ và đi copy prompt mẫu có sẵn.
```bash
python hr_prompter_simulator.py
```

### Bản 2: HTML Prompter Sandbox cho HR
Giao diện trực quan được thiết kế theo Sapia Design System (Cozy Avocado `#f4fce8`, tương tác 3D click, tuyệt đối không dùng màu tím). Trình giả lập cho phép HR nhập thử prompt soạn Email Mời Phỏng Vấn:
- Nút "Xem gợi ý gợi mở (Socratic)" chỉ dẫn từng bước hoàn thiện prompt (thêm yêu cầu, quyền lợi, địa điểm...).
- Bắt sự kiện Paste để cảnh báo gian lận/sao chép trực tiếp từ nguồn ngoài (khóa tăng ELO).
- Hiệu ứng âm thanh sinh động sử dụng Web Audio API tích hợp sẵn trong trình duyệt.
**Cách chạy:** Click đúp để mở trực tiếp file `hr_prompter_sandbox.html` trên trình duyệt.

### Bản 3: Weekly Activity Report Generator (Wizard of Oz Data)
Script tự động sinh báo cáo tuần dạng Markdown gửi cho quản lý/CEO thể hiện kết quả Wizard of Oz thử nghiệm trên 50 nhân viên HR thực tế (số giờ tiết kiệm, tỷ lệ active, sentinel logs và AI Reteach Slide Plan).
```bash
python gap_report_generator.py
```
Sau khi chạy, mở file `weekly_hr_activity_report.md` mới được tạo ra để xem chi tiết báo cáo.
