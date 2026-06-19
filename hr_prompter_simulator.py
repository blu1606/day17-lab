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

class HRPrompterTutorCLI:
    def __init__(self):
        self.student_elo = 1200
        self.bkt_mastery = 0.25 # Xác suất tinh thông prompt ban đầu
        self.hints_used = 0
        self.difficulty = 1250
        self.is_cheating_triggered = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print(f"{BOLD}{BLUE}================================================================{ENDC}")
        print(f"{BOLD}{GREEN}      🦊 AI Trợ Lý HR - Lộ Trình Luyện Prompt Tinh Thông         {ENDC}")
        print(f"{BOLD}{BLUE}================================================================{ENDC}")
        print(f" Nhân viên HR ELO: {BOLD}{YELLOW}{self.student_elo}{ENDC} | Độ khó tác vụ: {BOLD}{self.difficulty}{ENDC}")
        mastery_pct = int(self.bkt_mastery * 100)
        mastery_color = RED if mastery_pct < 35 else (YELLOW if mastery_pct < 65 else GREEN)
        print(f" Mức độ tinh thông Prompt (BKT): {mastery_color}{mastery_pct}%{ENDC}")
        print(f" Vùng phát triển gần nhất (ZPD): {GREEN}Phù hợp (72% khả năng tự viết prompt){ENDC}")
        print(f"{BLUE}----------------------------------------------------------------{ENDC}")

    def show_question(self):
        print(f"{BOLD}Tác vụ HR:{ENDC} Viết một prompt để AI tự động soạn thảo {BOLD}JD tuyển dụng vị trí Python Developer{ENDC}.")
        print("Mục tiêu: Prompt phải giúp AI tạo ra JD đầy đủ yêu cầu kỹ thuật, đãi ngộ và địa điểm.")
        print(f"{BLUE}----------------------------------------------------------------{ENDC}")

    def get_prompter_hint(self):
        self.hints_used += 1
        # Giảm nhẹ ELO phạt mỗi lần xem gợi ý để giữ động lực
        self.student_elo = max(800, self.student_elo - 10)
        self.bkt_mastery = min(0.95, self.bkt_mastery + 0.08)
        
        hints = [
            f"🦊 {BOLD}Gợi ý 1:{ENDC} Để viết JD chính xác, prompt của bạn cần cung cấp thông tin {UNDERLINE}đầu vào cơ bản{ENDC}: Vai trò cụ thể (Python Developer), số năm kinh nghiệm yêu cầu, và các kỹ năng/framework chính (ví dụ: Django, FastAPI). Bạn đã đưa các thông tin này vào chưa?",
            f"🦊 {BOLD}Gợi ý 2:{ENDC} Rất tốt! Ngoài kỹ năng chuyên môn, hãy yêu cầu AI viết thêm về {UNDERLINE}đãi ngộ, quyền lợi (lương, bảo hiểm, ngày phép){ENDC} và địa điểm làm việc (Hà Nội, TP.HCM...) để JD trông chuyên nghiệp và thu hút ứng viên hơn.",
            f"🦊 {BOLD}Gợi ý 3 (Tối đa):{ENDC} Một cấu trúc prompt mẫu hoàn chỉnh: {BOLD}'Hãy đóng vai chuyên viên tuyển dụng, viết JD tuyển dụng Python Developer có 2 năm kinh nghiệm làm việc với Django, địa điểm Hà Nội, mức lương thỏa thuận cùng chế độ bảo hiểm sức khỏe.'{ENDC}. Hãy tự viết lại phiên bản của riêng bạn nhé!"
        ]
        
        index = min(self.hints_used - 1, len(hints) - 1)
        print(f"\n{YELLOW}[HINT LADDER]{ENDC}")
        print(hints[index])
        print(f"📍 {BOLD}Trích dẫn tài liệu:{ENDC} {UNDERLINE}Lộ trình AI cho HR - Chương 1 - Slide trang 10{ENDC}")
        print(f"📉 Điểm ELO của bạn cập nhật: {RED}{self.student_elo} ELO (-10 phạt xem gợi ý){ENDC}")
        time.sleep(1.5)

    def search_slides(self):
        print(f"\n{BLUE}[SYSTEM]{ENDC} Đang tra cứu tài liệu học trình HR liên quan...")
        time.sleep(1)
        print(f"📄 Tìm thấy tài liệu trong Lộ trình AI cho HR:")
        print(f"   -> {BOLD}Chương 1: Prompting Cơ bản trong Tuyển dụng - Mục 1.2: Viết JD hiệu quả{ENDC}")
        print(f"   -> Nội dung: Prompt cấu trúc chuẩn gồm 4 phần: Vai trò (Role), Bối cảnh (Context), Nhiệm vụ (Task) và Định dạng đầu ra (Output format).")
        time.sleep(1.5)

    def simulate_cheating(self):
        self.is_cheating_triggered = True
        print(f"\n{RED}[WARNING] Đang mô phỏng sao chép (copy-paste) prompt mẫu có sẵn...{ENDC}")
        time.sleep(1)
        print(f"\n{BOLD}{RED}🚨 ACADEMIC INTEGRITY ALERT! 🚨{ENDC}")
        print(f"{RED}Phát hiện hành vi Copy-Paste prompt mẫu từ thư viện ngoài!")
        print(f"🔒 Hệ thống đóng băng điểm ELO (+0 ELO). Mức tinh thông không tăng.")
        print(f"📊 Hành vi sao chép lười suy nghĩ đã được ghi nhận trong lịch sử hoạt động để HR Manager hỗ trợ 1-1.{ENDC}")
        print(f"Điểm ELO hiện tại: {YELLOW}{self.student_elo} ELO (+0 ELO){ENDC}")
        time.sleep(2)

    def submit_prompt(self):
        print(f"\nNhập prompt của bạn (hoặc gõ 'exit' để quay lại menu):")
        print("Mẹo: Hãy tự suy nghĩ và tự gõ prompt để hệ thống kiểm tra năng lực thật!")
        user_prompt = input("> ")
        if user_prompt.strip().lower() == 'exit':
            return
        
        # Chuẩn hóa prompt để kiểm tra từ khóa cơ bản
        clean_prompt = user_prompt.lower()
        
        has_role = "python" in clean_prompt or "developer" in clean_prompt or "dev" in clean_prompt
        has_exp = "kinh nghiệm" in clean_prompt or "năm" in clean_prompt or "exp" in clean_prompt or "year" in clean_prompt
        has_details = "lương" in clean_prompt or "quyền lợi" in clean_prompt or "chế độ" in clean_prompt or "địa điểm" in clean_prompt or "hà nội" in clean_prompt or "hồ chí minh" in clean_prompt
        
        if has_role and has_exp and has_details:
            print(f"\n{GREEN}✔ Chúc mừng! Prompt của bạn rất tốt, chứa đầy đủ các thành phần cần thiết.{ENDC}")
            if self.is_cheating_triggered:
                print(f"{RED}⚠ Tuy nhiên, do bạn đã sao chép (cheat) trước đó, ELO và Mastery câu này không được cộng.{ENDC}")
            else:
                elo_gain = max(5, 25 - (self.hints_used * 5))
                self.student_elo += elo_gain
                self.bkt_mastery = min(1.0, self.bkt_mastery + 0.3)
                print(f"📈 Điểm ELO của bạn tăng lên: {GREEN}{self.student_elo} ELO (+{elo_gain}){ENDC}")
                print(f"📊 BKT Mastery tăng lên: {GREEN}{int(self.bkt_mastery * 100)}%{ENDC}")
            time.sleep(2)
        else:
            print(f"\n{RED}❌ Prompt chưa đầy đủ thông tin để AI sinh JD chất lượng.{ENDC}")
            print("Gợi ý: Cần bổ sung thêm yêu cầu kinh nghiệm, kỹ năng chính hoặc quyền lợi đãi ngộ.")
            time.sleep(2)

    def run(self):
        while True:
            self.clear_screen()
            self.print_header()
            self.show_question()
            
            print(f"{BOLD}Bạn muốn thực hiện hành động gì?{ENDC}")
            print(f" 1. Gõ prompt tự viết")
            print(f" 2. Yêu cầu gợi ý từ Sofi AI {YELLOW}(Gợi ý bậc thang - mất ELO){ENDC}")
            print(f" 3. Tra cứu Slide đào tạo HR")
            print(f" 4. Dán prompt mẫu có sẵn {RED}(Mô phỏng copy prompt){ENDC}")
            print(f" 5. Thoát chương trình")
            
            choice = input("\nLựa chọn của bạn (1-5): ")
            
            if choice == '1':
                self.submit_prompt()
            elif choice == '2':
                self.get_prompter_hint()
            elif choice == '3':
                self.search_slides()
            elif choice == '4':
                self.simulate_cheating()
            elif choice == '5':
                print(f"\nCảm ơn bạn đã tham gia khóa đào tạo AI Trợ Lý cho HR! Hẹn gặp lại.")
                break
            else:
                print(f"\n{RED}Lựa chọn không hợp lệ, vui lòng chọn từ 1-5.{ENDC}")
                time.sleep(1)

if __name__ == "__main__":
    tutor = HRPrompterTutorCLI()
    tutor.run()
