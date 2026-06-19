# Day 17 Lab Assignment - AI Prototyping & MVP (EduGap)

Dự án **EduGap** là một Gia sư AI Thích ứng (Adaptive-first AI Tutor) dành cho Giáo dục Đại học, giúp đo lường mức độ tinh thông (mastery) của sinh viên thông qua các câu hỏi và cung cấp gợi ý Socratic chống gian lận.

Tài liệu này trình bày các bước thực hiện bài Lab Day 17 để xác minh giả định quan trọng nhất của dự án bằng cách sử dụng các phương pháp thử nghiệm nhanh và rẻ hơn (Lean MVP).

---

## 1. Giả thuyết Quan trọng Nhất (Riskiest Hypothesis)

- **Hypothesis:** "Sinh viên thực sự muốn tự học qua gợi ý Socratic (Socratic Hints) và nguồn tài liệu tham khảo chính thống (Grounded Citations) thay vì chỉ muốn chép lời giải nhanh từ ChatGPT/Claude để đối phó lấy điểm."
- **Loại rủi ro:** Rủi ro giá trị (Value Risk) & Rủi ro hành vi sử dụng (Usability/Behavior Risk). Nếu sinh viên cảm thấy việc gợi ý Socratic quá phiền phức và luôn tìm cách gian lận để có kết quả nhanh nhất, giá trị cốt lõi của EduGap sẽ sụp đổ.

---

## 2. Cách Tiếp cận Truyền thống (Traditional/Planned Way)

Để test giả thuyết này, ban đầu nhóm dự kiến:
1. Thiết kế và build toàn bộ hệ thống Backend với LangChain, Langfuse, tích hợp cơ sở dữ liệu vector RAG chứa slide bài giảng.
2. Cài đặt thuật toán BKT (Bayesian Knowledge Tracing) và hệ thống tính điểm ELO động.
3. Thiết kế giao diện Web Chat mượt mà, đầy đủ tính năng xác thực người dùng.
4. Triển khai thử nghiệm (pilot) thực tế trên một lớp học khoảng 50 sinh viên trong vòng 1 tháng.
- **Nhược điểm:** Tốn kém rất nhiều thời gian (4-8 tuần phát triển), chi phí vận hành API cao, khó thay đổi nếu giả định sai từ đầu.

---

## 3. Ba (3) Cách Test Rẻ hơn để Kiểm chứng (Cheaper Validation Methods)

Để kiểm chứng giả thuyết trên với chi phí gần như bằng 0 và thực hiện trong vài giờ, chúng tôi đề xuất 3 cách test sau:

### Cách 1: CLI Socratic Chat Simulator (Mô phỏng CLI)
- **Ý tưởng:** Xây dựng một chương trình dòng lệnh (CLI) tương tác giả lập quá trình học tập. Sinh viên làm bài tập lập trình đệ quy và có các lựa chọn: *Tự làm bài*, *Yêu cầu gợi ý Socratic (mất ít ELO)*, *Tra cứu slide tham khảo*, hoặc *Gian lận bằng cách copy-paste*.
- **Mục tiêu test:** Đánh giá xem sinh viên có hiểu cơ chế tính điểm ELO phạt khi xem gợi ý, và họ có bị kích thích tự giải bài khi được cung cấp gợi ý gợi mở từng bước thay vì lời giải sẵn hay không.
- **File thực hiện:** `socratic_chat_simulator.py`

### Cách 2: Interactive Socratic Quiz (HTML Sandbox)
- **Ý tưởng:** Thiết kế một trang HTML tĩnh độc lập theo phong cách thiết kế Sapia (Avocado Green `#f4fce8`, tương tác 3D click dày 5px chân thật). Trang này chứa một câu hỏi trắc nghiệm/lập trình thực tế:
  - Khi sinh viên chọn "Xem gợi ý Socratic", nó sẽ mở ra một hộp thoại chứa các gợi ý từng bước (hint ladder) đi kèm mã trang slide bài giảng để họ tự mở slide đọc.
  - Khi sinh viên cố tình nhấn Ctrl+V (Paste) vào ô nhập bài giải, hệ thống sẽ bắt sự kiện `paste` toàn cục và hiển thị cảnh báo gian lận "Academic Integrity Alert!", đồng thời khóa tăng ELO.
- **Mục tiêu test:** Đo lường phản ứng trực quan và trải nghiệm người dùng của sinh viên đối với tính năng chống gian lận và gợi ý Socratic.
- **File thực hiện:** `socratic_quiz.html`

### Cách 3: Wizard of Oz Weekly Gap Report (Trình tạo báo cáo giả)
- **Ý tưởng:** Một script tự động tạo ra file báo cáo phân tích lỗ hổng kiến thức tuần gửi cho Giảng viên (Weekly Concept Gap Analysis). Bản báo cáo này mô phỏng kết quả phân tích của hệ thống AI đối với các câu hỏi đệ quy, đề xuất slide bài giảng giảng lại (AI Reteach Slides).
- **Mục tiêu test:** Gửi trực tiếp bản báo cáo Markdown/HTML này cho các giảng viên đại học để hỏi xem họ có thực sự muốn có báo cáo này hàng tuần để điều chỉnh bài giảng hay không (Value Risk phía Giảng viên).
- **File thực hiện:** `gap_report_generator.py`

---

## 4. Hướng dẫn Chạy Prototypes

### Bản 1: CLI Simulator
Chạy lệnh sau trong terminal:
```bash
python socratic_chat_simulator.py
```

### Bản 2: HTML Sandbox
Mở file `socratic_quiz.html` trực tiếp trên bất kỳ trình duyệt nào.

### Bản 3: Weekly Report Generator
Chạy lệnh sau để sinh báo cáo mẫu:
```bash
python gap_report_generator.py
```
Sau đó mở file `weekly_concept_gap_report.md` mới được tạo ra để xem kết quả.
