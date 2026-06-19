# 📩 LAB DAY 17 — MVP & TEST GIẢ ĐỊNH (BẢN 2 — TẬP TRUNG HR)

**Dự án:** AI Trợ Lý — Nhóm 09 (Vin AI thực chiến)
**Phạm vi bản 2:** chỉ test **1 persona = nhân viên HR/nhân sự**, **1 giả định duy nhất**.
**Lý do thu hẹp:** test 1 vai trò + 1 câu hỏi giúp ra kết quả nhanh, sạch, rẻ nhất — đúng tinh thần Lean Startup (xác minh từng giả định một).

---

## Bước 1 — Giả định rủi ro nhất (chỉ 1 giả định)

> **Nếu áp dụng phương pháp lộ trình SÁT công việc HR, thì nhân viên HR sẽ thấy phương pháp HIỆU QUẢ THẬT, và HỌC + ÁP DỤNG vào công việc MỖI NGÀY.**

Loại rủi ro: **Value Risk** (giá trị) + một phần **Usability** (dùng đều đặn).
Cố tình **KHÔNG test** ở bản này: sẵn sàng chi tiền, giới thiệu lên sếp, các vai trò khác. → để tránh nhiễu, chỉ đo đúng 1 thứ: *hiệu quả + dùng hằng ngày*.

**2 lớp con của giả định:**

| # | Lớp | Câu hỏi kiểm chứng | Chỉ số đo |
|---|---|---|---|
| 1 | **Hiệu quả thật** | Lộ trình AI sát việc HR có tạo ra kết quả công việc thật không? | Việc HR cụ thể làm được nhờ AI · số giờ tiết kiệm/tuần |
| 2 | **Áp dụng mỗi ngày** | HR có học & dùng đều đặn, không bỏ sau ngày 1? | Số ngày active/tuần · số tác vụ HR dùng AI/ngày |

**Vì sao nếu sai thì dự án sụp đổ:** Nếu chính HR — người trực tiếp đánh giá & đề xuất công cụ đào tạo trong công ty — dùng thử mà không thấy hiệu quả và không áp dụng hằng ngày, thì không có cửa nào để sản phẩm đi tiếp lên cấp công ty. HR là "người gác cổng" của mô hình B2B.

**Ví dụ công việc HR để bám vào (lộ trình sát nghề):**
viết JD tuyển dụng · sàng lọc & tóm tắt CV · soạn email mời/từ chối phỏng vấn · soạn câu hỏi phỏng vấn theo vị trí · viết thông báo nội bộ · tóm tắt biên bản phỏng vấn · soạn quy trình onboarding · trả lời nhanh câu hỏi chính sách nhân sự.

---

## Bước 2 — Cách làm thông thường (tốn kém nhất)

Build đầy đủ web app cho vai trò HR rồi mới đi tìm người test: code Next.js + Supabase, viết tay lộ trình HR (≥3 module + starter kit + quiz), trợ lý AI streaming + rate-limit, nhật ký giờ tiết kiệm, deploy Vercel tốn chi phí OpenAI. → nhiều tuần dev + rủi ro làm xong mới biết HR không cần.

---

## Bước 3 — 3 cách RẺ HƠN để test giả định (chi phí ≈ 0, tính bằng ngày)

### Cách 1 — Concierge / Wizard of Oz cho HR ⭐ (test thẳng nhất)
Chọn **5–8 nhân viên HR thật**. Gửi mỗi người 1 "lộ trình AI cho HR" dạng Google Doc + 1 nhóm Zalo.
Mỗi ngày trong **1 tuần**, giao 1 tác vụ HR nhỏ (vd hôm nay: "dùng AI viết JD vị trí X"). Họ hỏi gì → **founder tự tay đóng vai trợ lý AI** (ChatGPT phía sau) trả lời bằng ví dụ đúng nghề HR.
- **Đo lớp 1 (hiệu quả):** cuối ngày hỏi "AI giúp bạn tiết kiệm mấy giờ? làm được việc gì?" → ghi Google Sheet.
- **Đo lớp 2 (mỗi ngày):** đếm bao nhiêu/8 người mở ra dùng đủ ≥4 ngày/tuần mà không cần nhắc.
- **Thời gian:** dựng nửa ngày, chạy 1 tuần.

### Cách 2 — Landing/Form khảo sát hành vi HR
Trang/Google Form ngắn mô tả lộ trình HR + danh sách tác vụ → hỏi HR: tác vụ nào bạn làm hằng ngày? bạn muốn AI hỗ trợ việc nào nhất? → đo **mức độ khớp** giữa nội dung lộ trình và việc HR thật sự làm mỗi ngày (kiểm chứng "sát công việc").
- **Thời gian:** 1 ngày.

### Cách 3 — Clickable Prototype + phỏng vấn HR
Dùng lại 8 màn hình có sẵn, mở phần lộ trình HR + starter kit, cho 3–5 HR tự bấm và thử 1–2 prompt mẫu vào việc thật.
- **Đo:** họ có tự hiểu & dùng được ngay không · prompt nào họ thấy "dùng được mỗi ngày" · chỗ nào khựng.
- **Thời gian:** 2–3 ngày.

---

## Bước 4 — Prototype phác thảo

**Cách 1 — Wizard of Oz HR (luồng thủ công):**
```
Mỗi sáng: gửi 1 tác vụ HR trong nhóm Zalo ("hôm nay: AI sàng lọc 10 CV")
        ↓
HR làm → hỏi lại khi vướng
        ↓
[Founder] mở ChatGPT → trả lời theo ví dụ HR (giả làm "Trợ lý AI")
        ↓
Cuối ngày: "tiết kiệm mấy giờ? làm được việc gì?" → Google Sheet
        ↓
Cuối tuần: đếm số người dùng ≥4/7 ngày → kết luận lớp 2
```

**Cách 2 — Form khảo sát khớp việc:**
```
[Liệt kê 8 tác vụ HR] → HR tick "làm hằng ngày / thỉnh thoảng / không"
                      → "muốn AI hỗ trợ việc nào nhất?"
→ đo nội dung lộ trình có trúng việc hằng ngày của HR không
```

**Cách 3 — Prototype phỏng vấn:**
```
Mở màn lộ trình HR + starter kit → HR tự bấm, thử 1 prompt vào việc thật
Hỏi: "prompt nào bạn sẽ dùng lại mỗi ngày?"
```

---

## Bước 5 — Thuyết trình (khung 3 phút)

1. **Giả định duy nhất:** HR thấy lộ trình sát việc HIỆU QUẢ + ÁP DỤNG MỖI NGÀY.
2. **Nếu sai → sụp đổ:** HR là người gác cổng B2B; HR không dùng thì không lên được cấp công ty.
3. **Thay vì code app** → test bằng Wizard of Oz HR (chính) + form khớp việc + prototype phỏng vấn.
4. **Tiêu chí PASS:**
   - Hiệu quả → TB ≥3h/người/tuần tiết kiệm + mỗi người kể được ≥2 việc HR làm được nhờ AI.
   - Áp dụng mỗi ngày → ≥60% người test (vd ≥5/8) tự dùng ≥4 ngày/tuần mà không cần nhắc.
5. **Quyết định:** PASS → mới code lộ trình HR thật. FAIL → chỉnh nội dung cho sát việc HR hơn trước khi tốn 1 dòng code.

---

## 📝 TEMPLATE ĐIỀN NHANH (bản 2 — HR)

```markdown
1. Tên dự án: AI Trợ Lý — bản test vai trò HR (Nhóm 09)

2. Giả định rủi ro nhất (1 giả định duy nhất):
   - "Chúng tôi tin rằng NHÂN VIÊN HR gặp khó khăn khi MUỐN DÙNG AI VÀO CÔNG VIỆC
     HR NHƯNG KHÔNG BIẾT BẮT ĐẦU TỪ ĐÂU / DÙNG SAO CHO ĐÚNG.
     Nếu chúng tôi làm LỘ TRÌNH AI SÁT CÔNG VIỆC HR + TRỢ LÝ GIẢI THÍCH BẰNG VÍ DỤ
     ĐÚNG NGHỀ HR, họ sẽ THẤY HIỆU QUẢ THẬT và HỌC + ÁP DỤNG VÀO VIỆC MỖI NGÀY.
     Chúng tôi biết mình đúng khi: (1) TB ≥3H/NGƯỜI/TUẦN TIẾT KIỆM + mỗi người kể
     được ≥2 việc HR làm được nhờ AI [hiệu quả]; (2) ≥60% người test TỰ DÙNG
     ≥4 NGÀY/TUẦN không cần nhắc [áp dụng mỗi ngày]."
   - (KHÔNG test ở bản này: chi tiền, giới thiệu lên sếp, các vai trò khác.)

3. Cách làm tốn kém ban đầu định hướng:
   - Code đầy đủ web app cho vai trò HR rồi mới đi tìm người test.

4. 3 Cách kiểm thử thay thế cực rẻ (MVP):
   - Cách 1 (Wizard of Oz HR): 5–8 HR thật + Google Doc lộ trình + nhóm Zalo;
     founder tự tay đóng vai trợ lý AI, giao 1 tác vụ HR/ngày trong 1 tuần,
     đo giờ tiết kiệm + số ngày active (≈0đ).
   - Cách 2 (Form khảo sát khớp việc): liệt kê 8 tác vụ HR → đo lộ trình có trúng
     việc HR làm hằng ngày không (1 ngày).
   - Cách 3 (Prototype phỏng vấn): dùng 8 màn hình có sẵn, 3–5 HR thử prompt vào
     việc thật, đo prompt nào "dùng được mỗi ngày" (2–3 ngày).
```
