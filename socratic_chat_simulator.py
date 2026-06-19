# -*- coding: utf-8 -*-
import time
import os
import sys

# Đảm bảo in đúng tiếng Việt trên terminal Windows/VSCode
if sys.platform.startswith('win'):
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# Định nghĩa màu sắc ANSI
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'

class SocraticTutorCLI:
    def __init__(self):
        self.student_elo = 1200
        self.bkt_mastery = 0.25 # Xác suất tinh thông (BKT) ban đầu
        self.hints_used = 0
        self.difficulty = 1250
        self.is_cheating_triggered = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print(f"{BOLD}{BLUE}================================================================{ENDC}")
        print(f"{BOLD}{GREEN}           🦊 EduGap - Adaptive-first Socratic AI Tutor         {ENDC}")
        print(f"{BOLD}{BLUE}================================================================{ENDC}")
        print(f" Sinh viên ELO: {BOLD}{YELLOW}{self.student_elo}{ENDC} | Độ khó câu hỏi: {BOLD}{self.difficulty}{ENDC}")
        mastery_pct = int(self.bkt_mastery * 100)
        mastery_color = RED if mastery_pct < 35 else (YELLOW if mastery_pct < 65 else GREEN)
        print(f" Mức độ hiểu bài (BKT Mastery): {mastery_color}{mastery_pct}%{ENDC}")
        print(f" Vùng phát triển gần nhất (ZPD): {GREEN}Phù hợp (72% khả năng tự làm){ENDC}")
        print(f"{BLUE}----------------------------------------------------------------{ENDC}")

    def show_question(self):
        print(f"{BOLD}Đề bài:{ENDC} Viết hàm đệ quy {BOLD}fib(n){ENDC} để tính số Fibonacci thứ n trong Python.")
        print(f"Ví dụ: fib(0) = 0, fib(1) = 1, fib(5) = 5.")
        print(f"{BLUE}----------------------------------------------------------------{ENDC}")

    def get_socratic_hint(self):
        self.hints_used += 1
        # Giảm nhẹ ELO phạt mỗi lần xem gợi ý
        self.student_elo = max(800, self.student_elo - 10)
        self.bkt_mastery = min(0.95, self.bkt_mastery + 0.08)
        
        hints = [
            f"🦊 {BOLD}Gợi ý 1:{ENDC} Hàm đệ quy luôn cần một {UNDERLINE}điểm dừng (base case){ENDC} để tránh vòng lặp vô hạn. Bạn hãy xác định với n nhỏ nhất nào (ví dụ n = 0, n = 1) thì hàm có thể trả về ngay kết quả mà không cần đệ quy tiếp?",
            f"🦊 {BOLD}Gợi ý 2:{ENDC} Chính xác! Với n <= 1, ta trả về chính n. Còn với n > 1, số Fibonacci thứ n là tổng của hai số Fibonacci đứng trước nó. Hãy thử kết hợp hai số trước đó lại bằng cách gọi đệ quy nhé.",
            f"🦊 {BOLD}Gợi ý 3 (Tối đa):{ENDC} Công thức tổng quát cho n > 1 là {BOLD}return fib(n-1) + fib(n-2){ENDC}. Hãy tự viết lại hàm hoàn chỉnh với base case đã thảo luận nhé!"
        ]
        
        index = min(self.hints_used - 1, len(hints) - 1)
        print(f"\n{YELLOW}[HINT LADDER]{ENDC}")
        print(hints[index])
        print(f"📍 {BOLD}Trích dẫn:{ENDC} {UNDERLINE}Slide Bài giảng 4 - Chương Đệ quy - Trang 15{ENDC}")
        print(f"📉 Điểm ELO của bạn cập nhật: {RED}{self.student_elo} ELO (-10 phạt xem gợi ý){ENDC}")
        time.sleep(1.5)

    def search_slides(self):
        print(f"\n{BLUE}[SYSTEM]{ENDC} Đang tra cứu tài liệu học trình phù hợp...")
        time.sleep(1)
        print(f"📄 Tìm thấy tài liệu liên quan:")
        print(f"   -> {BOLD}Slide Chương 2 (Đệ quy & Chia để trị) - Mục 2.3: Fibonacci sequence{ENDC}")
        print(f"   -> Nội dung: Định nghĩa dãy F(n) = F(n-1) + F(n-2) với F(0)=0, F(1)=1.")
        time.sleep(1.5)

    def simulate_cheating(self):
        self.is_cheating_triggered = True
        print(f"\n{RED}[WARNING] Đang mô phỏng dán (paste) code giải từ ChatGPT...{ENDC}")
        time.sleep(1)
        print(f"\n{BOLD}{RED}🚨 ACADEMIC INTEGRITY ALERT! 🚨{ENDC}")
        print(f"{RED}Hành vi copy-paste lời giải ngoài hệ thống bị phát hiện!")
        print(f"🔒 Điểm ELO bị đóng băng. BKT Mastery không tăng.")
        print(f"📊 Log hành vi đã được lưu vào hồ sơ giảng viên để xem xét hỗ trợ 1-1.{ENDC}")
        print(f"Điểm ELO hiện tại: {YELLOW}{self.student_elo} ELO (+0 ELO){ENDC}")
        time.sleep(2)

    def submit_solution(self):
        print(f"\nNhập mã Python của bạn (hoặc gõ 'exit' để quay lại menu):")
        print("Mẹo: Hãy tự gõ tay code để hệ thống chấm điểm thực tế!")
        user_code = input("> ")
        if user_code.strip().lower() == 'exit':
            return
        
        # Chuẩn hóa code nhập vào để check đơn giản
        clean_code = "".join(user_code.split())
        
        # Check đáp án đúng Fibonacci đệ quy
        has_base = "ifn<=1" in clean_code or "ifn==0" in clean_code or "ifn<2" in clean_code
        has_recursive = "fib(n-1)+fib(n-2)" in clean_code or "fib(n-2)+fib(n-1)" in clean_code
        
        if has_base and has_recursive:
            print(f"\n{GREEN}✔ Chúc mừng! Lời giải của bạn chính xác.{ENDC}")
            if self.is_cheating_triggered:
                print(f"{RED}⚠ Tuy nhiên, do bạn đã dán code trước đó, ELO và Mastery câu này không được tính.{ENDC}")
            else:
                elo_gain = max(5, 25 - (self.hints_used * 5))
                self.student_elo += elo_gain
                self.bkt_mastery = min(1.0, self.bkt_mastery + 0.3)
                print(f"📈 Điểm ELO của bạn tăng lên: {GREEN}{self.student_elo} ELO (+{elo_gain}){ENDC}")
                print(f"📊 BKT Mastery tăng lên: {GREEN}{int(self.bkt_mastery * 100)}%{ENDC}")
            time.sleep(2)
        else:
            print(f"\n{RED}❌ Lời giải chưa chính xác hoặc chưa tối ưu đệ quy.{ENDC}")
            print("Gợi ý: Hãy kiểm tra kỹ điều kiện dừng và công thức đệ quy.")
            time.sleep(2)

    def run(self):
        while True:
            self.clear_screen()
            self.print_header()
            self.show_question()
            
            print(f"{BOLD}Bạn muốn thực hiện hành động gì?{ENDC}")
            print(f" 1. Gõ code tự giải bài")
            print(f" 2. Yêu cầu gợi ý từ Gia sư Socratic AI {YELLOW}(Gợi ý bậc thang - mất ELO){ENDC}")
            print(f" 3. Tra cứu slide tài liệu liên quan")
            print(f" 4. Dán code từ ChatGPT {RED}(Mô phỏng gian lận){ENDC}")
            print(f" 5. Thoát chương trình")
            
            choice = input("\nLựa chọn của bạn (1-5): ")
            
            if choice == '1':
                self.submit_solution()
            elif choice == '2':
                self.get_socratic_hint()
            elif choice == '3':
                self.search_slides()
            elif choice == '4':
                self.simulate_cheating()
            elif choice == '5':
                print(f"\nCảm ơn bạn đã tham gia học thử nghiệm cùng EduGap! Tạm biệt.")
                break
            else:
                print(f"\n{RED}Lựa chọn không hợp lệ, vui lòng chọn từ 1-5.{ENDC}")
                time.sleep(1)

if __name__ == "__main__":
    tutor = SocraticTutorCLI()
    tutor.run()
