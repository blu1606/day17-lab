# -*- coding: utf-8 -*-
import time
import sys

# Đảm bảo in đúng tiếng Việt trên terminal Windows/VSCode
if sys.platform.startswith('win'):
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def generate_report():
    print("🤖 EduGap Wizard of Oz Reporter đang chạy...")
    time.sleep(0.5)
    print("⏳ Đang phân tích dữ liệu tương tác của 50 sinh viên...")
    time.sleep(1.0)
    print("📊 Đang tổng hợp các sự kiện chống gian lận (Integrity Sentinel)...")
    time.sleep(0.8)
    print("💡 Đang đề xuất slide bổ trợ giảng dạy (AI Reteach Slide)...")
    time.sleep(0.7)

    report_content = """# 📊 Báo cáo Điểm yếu Kiến thức Tuần (Weekly Concept Gap Report)
**Học phần:** Cấu trúc dữ liệu & Giải thuật (CS201)  
**Tuần học:** Tuần 4 - Đệ quy & Độ phức tạp thuật toán  
**Sĩ số lớp:** 50 Sinh viên  
**Thời gian tạo:** Thứ Sáu lúc 22:00 (Hệ thống tự động đồng bộ hàng tuần)

---

## 1. Biểu đồ Mức độ Tinh thông Kiến thức (BKT Mastery Breakdown)

| Khái niệm (Concept) | Độ khó (Elo) | Tỉ lệ Tinh thông lớp (BKT Mastery) | Trạng thái cảnh báo |
| :--- | :---: | :---: | :---: |
| **Đệ quy - Base Case (Điều kiện dừng)** | 1250 | **32%** | 🚨 Nguy cấp (Cần bổ trợ) |
| **Độ phức tạp thời gian (Big O)** | 1200 | **45%** | ⚠ Cảnh báo |
| **Hàm đệ quy đuôi (Tail Recursion)** | 1300 | **58%** | ⚠ Cảnh báo |
| **Đệ quy Fibonacci / Nhị phân** | 1250 | **72%** | 👍 Tốt |
| **Vòng lặp cơ bản (Iteration)** | 950 | **92%** | 👍 Tốt |

---

## 2. Điểm yếu Kiến thức Lớn nhất của Lớp (Concept Gap #1)

- **Chủ đề chính:** `Đệ quy - Thiếu hoặc sai điều kiện dừng (Base Case)`
- **Triệu chứng hệ thống ghi nhận:** 
  - 18 sinh viên chạy chương trình bị lỗi **RecursionError: maximum recursion depth exceeded** (Lặp vô hạn).
  - Phần lớn sinh viên chưa hiểu cách trả về giá trị trực tiếp cho các trường hợp cơ bản nhất ($n=0$, $n=1$) mà vẫn tiếp tục gọi đệ quy tiếp.

---

## 3. Nhật ký An toàn Học thuật (Academic Integrity Sentinel)

Hệ thống chống gian lận EduGap theo dõi hành vi sao chép bài từ AI bên ngoài:
- **Số sinh viên tích cực tự học:** 42 / 50 sinh viên.
- **Tỉ lệ xem gợi ý Socratic (Hint ladder):** 84% (Sinh viên ưa chuộng gợi ý từng bước vì giúp họ hiểu bài mà không mất quá nhiều điểm ELO).
- **Hành vi Copy-Paste bị phát hiện (Đóng băng ELO):**
  - Đã kích hoạt **28 lượt cảnh báo** trên giao diện khi sinh viên cố tình paste code giải từ ChatGPT.
  - **Danh sách 3 sinh viên cần hỗ trợ 1-1** (Có hành vi paste lặp đi lặp lại trên 5 lần và ELO tụt dốc):
    1. *Nguyễn Văn A* (Paste 7 lần, ELO hiện tại: 1020)
    2. *Trần Thị B* (Paste 6 lần, ELO hiện tại: 1080)
    3. *Lê Hoàng C* (Paste 5 lần, ELO hiện tại: 1110)

---

## 4. Đề xuất Kế hoạch Giảng lại (AI Reteach Slide Plan)
*Tính năng "Labor Illusion" tự động thiết lập dàn slide bổ trợ cho Giảng viên dựa trên lỗi thực tế của lớp.*

### Slide 1: Đệ quy Không Lối Thoát (Hiểu về lỗi đệ quy vô hạn)
- **Hình ảnh minh họa gợi ý:** Một chiếc gương phản chiếu gương vô tận, hoặc một vòng lặp không có điểm dừng.
- **Nội dung chính:** Giải thích tại sao máy tính cần một điểm dừng để giải phóng bộ nhớ Stack.
- **Ví dụ thực tế:** Đoạn code lỗi phổ biến nhất trong tuần qua của lớp:
  ```python
  def fib(n):
      # Thiếu điều kiện dừng n <= 1
      return fib(n-1) + fib(n-2)
  ```
  *Giải thích cơ chế Stack Overflow khi gọi hàm này.*

### Slide 2: Công thức 2 bước thiết kế đệ quy chuẩn
- **Bước 1 (Base Case):** Tìm các đầu vào nhỏ nhất mà kết quả có thể tính ngay lập tức.
- **Bước 2 (Recursive Case):** Phân rã bài toán lớn thành bài toán nhỏ hơn cùng loại.
- **Minh họa bằng bảng chạy tay:** Lần vết hàm `fib(4)` từng bước cụ thể.

### Slide 3: Bài tập rèn luyện nhanh tại lớp (5 phút)
- **Đề bài:** Viết hàm tính tổng từ 1 đến n bằng đệ quy `sum_n(n)`.
- **Yêu cầu giảng viên:** Cho học sinh chỉ ra đâu là Base Case và đâu là Recursive Case trước khi code.

---

## 5. Phản hồi khảo sát nhanh (Wizard of Oz Validation Questions)

*Giảng viên vui lòng trả lời 3 câu hỏi sau để chúng tôi tối ưu công cụ:*
1. Bản báo cáo tuần này có giúp thầy/cô tiết kiệm thời gian chuẩn bị giáo án bổ trợ không?
2. Thầy/cô có đồng ý sử dụng slide đề xuất ở Mục 4 để giảng lại vào tuần tới không?
3. Thầy/cô muốn nhận báo cáo này qua Email, Slack, hay xem trực tiếp trên Web Dashboard?
"""

    with open("weekly_concept_gap_report.md", "w", encoding="utf-8") as f:
        f.write(report_content)

    print("\n✅ Tạo báo cáo thành công!")
    print("📄 File báo cáo đã được lưu tại: weekly_concept_gap_report.md")
    print("👉 Hãy gửi file markdown này cho Giảng viên để khảo sát ý kiến của họ.")

if __name__ == "__main__":
    generate_report()
