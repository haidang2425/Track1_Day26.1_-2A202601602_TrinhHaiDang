# Track 1 - Day 26: AI Product Handbook — Operating Dashboard

## Vận hành theo mô hình kinh doanh B2B Higher Education (Đèn nào bật trước?)

- **Học viên:** Trịnh Hải Đăng
- **Mã học viên (MSSV):** 2A202601602
- **Sản phẩm:** Cursus AI — AI Educational Copilot & Learning Companion for Higher Education
- **Mô hình kinh doanh:** B2B (Khoa / Trường Đại học & Cao đẳng)
- **Repo bài nộp:** [haidang2425/Track1_Day26.1_-2A202601602_TrinhHaiDang](https://github.com/haidang2425/Track1_Day26.1_-2A202601602_TrinhHaiDang)
- **Liên kết các chặng trước:** [Day 24](https://github.com/haidang2425/Track1_Day24_2A202601602_TrinhHaiDang) · [Day 25](https://github.com/haidang2425/Track1_Day25_2A202601602_TrinhHaiDang)

---

## 1. Danh mục Artifacts nộp bài

| STT | Tên Artifact | Định dạng | Vị trí | Mô tả nội dung |
| :-: | --- | :---: | :---: | --- |
| 1 | `TrinhHaiDang_Day26_dashboard.pdf` | PDF Document | Root & `submissions/` | File PDF chuẩn Executive 2 trang A4 (Trang 1: Bảng điều khiển 1 trang, Trang 2: Phụ lục đối soát và phản biện). |
| 2 | `TrinhHaiDang_Day26_dashboard.docx` | MS Word (.docx) | Root & `submissions/` | File Word gốc báo cáo chuẩn định dạng hành chính, bảng biểu rõ ràng. |
| 3 | `operating-dashboard.md` | Markdown (.md) | `submissions/2A202601602/` | Worksheet nguồn chứa đầy đủ evidence để script `validate_submission.py` kiểm tra cấu trúc. |
| 4 | `one-page-dashboard.md` | Markdown (.md) | `submissions/2A202601602/` | Bản tóm tắt 1 trang cô đọng toàn bộ tín hiệu và luật quyết định. |

---

## 2. Báo cáo Chi tiết 5 Trạm Vận hành (5 Checkpoints)

### 2.1 Trạm 1 — Chẩn đoán Mô hình & Dữ liệu đầu vào

- **Chẩn đoán mô hình:** Cursus AI vận hành theo mô hình **B2B** do các Khoa/Trường Đại học (Trưởng khoa / Trưởng phòng Đào tạo) trực tiếp ký hợp đồng và thanh toán định kỳ ($14.400 ACV/khoa) từ ngân sách vận hành đào tạo và quỹ trợ giảng (TA); Giảng viên và Sinh viên của trường là người dùng trực tiếp trên nền tảng Canvas LMS thông qua chuẩn quốc tế LTI 1.3 mà không cần duy trì quan hệ thương mại độc lập với từng sinh viên.
- **North Star Metric:** **Time-to-first-value ≤ 5 ngày** với ít nhất 50 sinh viên active trong khóa học (Hiện tại: 6 ngày — Trạng thái: Cần lưu ý / Cảnh báo).
- **Kiểm kê dữ liệu đầu vào:**
  - *Unit economics Day 24:* Đo được (Bảng tính tài chính Day 24, model LTV/CAC, CAC payback 12 tháng).
  - *Value Metric & Cost/Job Day 25:* Đo được (Evidence pack Day 25, 5 thành phần chi phí $0.0559/job, benchmark Claude Haiku 4.5).

### 2.2 Trạm 2 & 3 — Cây Tín hiệu 3 Tầng & Các Ngưỡng Vận hành (Signal Tree & Operating Thresholds)

| Tầng · ID | Tên chỉ số & Định nghĩa | Hiện tại | Vùng Xanh (Đạt) | Vùng Vàng (Cảnh báo) | Vùng Đỏ (Nguy hiểm) | Nguồn | Nhịp · Owner | Báo trước cho · Luật |
| --- | --- | :---: | :---: | :---: | :---: | --- | --- | --- |
| **L · L-01** | **Time-to-first-value (TTFV):** Số ngày từ kết nối LTI đến khi đạt 50 resolution QA | 6 ngày | ≤5 ngày | 6–10 ngày | >10 ngày | `[TB]` Pilot cohort | Tuần · Product Ops | POC-to-paid · **R-01 (Dừng)** |
| **L · L-02** | **Weekly student resolution rate:** Tỷ lệ SV active có ≥2 resolution QA / tuần | 58% | ≥65% | 45–64% | <45% | `[TB]` ĐHBK log | Tuần · Customer Success | TTFV & Churn · **R-02** |
| **O · O-01** | **Pilot activation rate:** Tỷ lệ pilot khoa đạt >500 resolution trong 30 ngày | 66% | ≥75% | 50–74% | <50% | `[MH]` MH-02 | Tuần · Product Ops | POC-to-paid · **R-03 (Dừng)** |
| **O · O-02** | **Chi phí AI trên mỗi job:** Tổng token Claude Haiku + Infra chia resolution QA | 840 đ | ≤1.000 đ | 1.001–1.800 đ | >1.800 đ | `[MH]` MH-01 | Tuần · FinOps | Gross Margin · **R-04** |
| **O · O-03** | **POC-to-paid conversion:** Tỷ lệ pilot chuyển đổi thành hợp đồng năm chính thức | 50% | ≥60% | 40–59% | <40% | `[BM]` ICONIQ '26 | Tháng · Revenue Ops | ARR & CAC payback · **R-03 (Dừng)** |
| **G · G-01** | **Gross margin sau chi phí AI:** (Doanh thu − toàn bộ COGS AI) ÷ Doanh thu | 82% | ≥80% | 65–79% | <65% | `[MH]` MH-01 | Tháng · Finance | Runway & Payback · **R-04** |
| **G · G-02** | **Net Revenue Retention (NRR):** Doanh thu cohort sau mở rộng môn/lớp và churn | 100% | ≥110% | 100–109% | <100% | `[BM]` Benchmarkit | Quý · Finance | LTV & Tăng trưởng · **R-05** |

### 2.3 Trạm 4 — Hệ thống 5 Luật Quyết định (Decision Rules)

| ID | Điều kiện kích hoạt (NẾU · TRONG · VÀ) | Hành động bắt buộc (THÌ) | Phản xạ sai bị CẤM (KHÔNG THÌ) | Luật dừng? |
| --- | --- | --- | --- | :---: |
| **R-01** | **Median TTFV > 10 ngày** trong 2 cohort liên tiếp VÀ mỗi cohort có ≥2 khoa | **Đóng băng tiếp nhận pilot mới trong 14 ngày** và tinh gọn quy trình cấu hình RAG syllabus xuống đúng 1 môn học cốt lõi | **CẤM:** Không giảm giá hợp đồng để bù đắp sự chậm trễ trong việc chứng minh giá trị | **CÓ (Dừng pilot)** |
| **R-02** | **Weekly resolution rate < 45%** trong 3 tuần VÀ có ≥100 SV trong danh sách | **Biệt phái 1 chuyên viên Product Ops** trực tiếp hỗ trợ giảng viên gắn bài tập tuần vào widget Canvas | **CẤM:** Không gửi email spam thúc ép sinh viên khi giao diện chưa thuận tiện | **KHÔNG** |
| **R-03** | **Pilot activation rate < 50%** trong 2 kỳ đánh giá VÀ có ≥4 pilot đang chạy | **Dừng toàn bộ hoạt động outbound sales mới** và tập trung tối ưu hóa kịch bản onboarding 1-click cho giảng viên | **CẤM:** Không tăng ngân sách sales để tìm thêm pilot khi tỷ lệ kích hoạt chưa đạt chuẩn | **CÓ (Dừng sales)** |
| **R-04** | **AI cost / job > 1.800 đ** trong 2 tuần liên tiếp VÀ có ≥1.000 resolution phát sinh | **Bật tính năng prompt caching**, cắt giảm context RAG và chuyển truy vấn đơn giản sang model tier nhỏ hơn | **CẤM:** Không tắt bộ lọc kiểm duyệt an toàn để giảm chi phí token ảo | **KHÔNG** |
| **R-05** | **NRR < 100%** trong 2 quý liên tiếp VÀ có ≥3 hợp đồng khoa đến kỳ gia hạn | **Tổ chức phiên làm việc trực tiếp Trưởng khoa** đánh giá báo cáo giảm tải TA và giải quyết các rào cản tính năng | **CẤM:** Không tính toán gộp cơ hội bán mới từ các trường khác vào NRR tài khoản cũ | **KHÔNG** |

### 2.4 Trạm 5 — Cổng gác 90 ngày, Kill Criteria & Phụ lục [MH]

- **Cổng Ngày 30 (Learning Validation):** Xác nhận Pain Moment & độ chính xác RAG syllabus từ 3 Trưởng bộ môn: Đạt ≥ 85% Factual Accuracy & 3/3 bộ môn nghiệm thu kỹ thuật -> Đạt: **GO** / Trượt: **FIX**.
- **Cổng Ngày 60 (Operational Execution):** Tỷ lệ sinh viên active giải bài tập tuần ≥ 50% trên tổng số 600 sinh viên tại 2 khoa pilot -> Đạt: **GO** / Trượt: **PIVOT**.
- **Cổng Ngày 90 (Business Viability):** Gross Margin sau chi phí AI ≥ 80% và có ≥ 2 hợp đồng B2B chính thức ($14.400 ACV) -> Đạt: **GO** / Trượt: **KILL**.
- **Kill Criteria:** Dừng dự án (KILL) vào ngày 90 nếu sau 2 chu kỳ tối ưu kỹ thuật RAG mà tỷ lệ chuyển đổi POC sang hợp đồng trả phí vẫn dưới 30% và không có khoa nào đồng ý mức giá nền tối thiểu $1.50/sinh viên/tháng.

#### Phụ lục Ngưỡng suy từ Mô hình Unit Economics [MH]:

1. **`MH-01` (Chi phí AI tối đa / resolution):**
   - Công thức: `Giá bán 9.100 đ x (1 - 0.84 GM) - 600 đ (Biến phí khác) = 856 đ/job`
   - Phân vùng áp dụng (cho `O-02` và `G-01`):
     - Vùng Xanh (Đạt): ≤ 1.000 đ/job
     - Vùng Vàng (Cảnh báo): 1.001 – 1.800 đ/job
     - Vùng Đỏ (Nguy hiểm): > 1.800 đ/job

2. **`MH-02` (Tỷ lệ kích hoạt Pilot tối thiểu):**
   - Công thức: `Mục tiêu 3 hợp đồng B2B / 4 pilot khoa = 75%`
   - Phân vùng áp dụng (cho `O-01`):
     - Vùng Xanh (Đạt): ≥ 75%
     - Vùng Vàng (Cảnh báo): 50% – 74%
     - Vùng Đỏ (Nguy hiểm): < 50%

---

## 3. Quality Gate & Kết quả Kiểm định

Hệ thống kiểm tra chất lượng và tính nhất quán được thực thi tự động:

```bash
python scripts/validate_rubric.py
# PASS: public rubric package v2.0.0 is internally consistent

python scripts/validate_submission.py examples/b2b-supportpilot-example.md
# PASS: examples/b2b-supportpilot-example.md meets the structural minimum bar

python scripts/validate_submission.py submissions/2A202601602/operating-dashboard.md
# PASS: submissions/2A202601602/operating-dashboard.md meets the structural minimum bar

python -m unittest discover -s tests -v
# Ran 30 tests in 0.45s ... OK (30/30 tests passed)
```

---

*Báo cáo hoàn thiện bởi Trịnh Hải Đăng (MSSV: 2A202601602) — Track 1 AI Product.*
