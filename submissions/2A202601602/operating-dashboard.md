# Operating Dashboard — Cursus AI

> Đây là **worksheet nguồn** để validator và rubric truy vết evidence. Sau khi
> hoàn tất, rút gọn phần vận hành sang
> `templates/one-page-dashboard-template.md`; không ép bảng 12 cột này lên một trang.

- Học viên: Trịnh Hải Đăng
- Mã học viên: 2A202601602
- Mô hình: B2B
- Cập nhật: 2026-08-28
- North Star: Time-to-first-value dưới 5 ngày với ít nhất 50 sinh viên active

## Chẩn đoán mô hình

Cursus AI là mô hình B2B vì các Khoa/Trường Đại học (Trưởng khoa / Trưởng phòng Đào tạo) trực tiếp trả tiền định kỳ từ ngân sách đào tạo và quỹ trợ giảng, giảng viên và sinh viên của trường là người dùng trực tiếp trên nền tảng Canvas LMS thông qua chuẩn LTI 1.3 mà không cần duy trì quan hệ thương mại độc lập với từng sinh viên.

| Dữ liệu đầu vào | Trạng thái | Nằm ở đâu hoặc cần gì để đo | Ngày có số |
|---|---|---|---|
| Unit economics Day 24 | Đo được | Bảng tính tài chính Day 24 và model LTV/CAC, CAC payback | 2026-08-28 |
| Value Metric và Cost/Job Day 25 | Đo được | Evidence pack Day 25 với 5 thành phần Cost/Job và benchmark Claude Haiku | 2026-08-28 |

## Kiểm kê đèn ứng viên

| Đèn ứng viên từ handbook | Tầng | Trạng thái | Bằng chứng hiện có hoặc kế hoạch đo |
|---|---|---|---|
| Time-to-first-value (TTFV) | L | ✅ | Log tích hợp LTI 1.3 và event 50 resolution đầu tiên của sinh viên |
| Pipeline coverage | L | 🔧 | Chuẩn hóa stage cơ hội và CRM pipeline của 8 khoa mục tiêu trước 2026-09-15 |
| % deal chết ở khâu security/procurement | L | 🔧 | Theo dõi lý do từ chối về DPA/bảo mật RAG trong CRM trước 2026-09-15 |
| POC → paid | O | ✅ | Biên bản MOU và kết quả chuyển đổi từ 3 pilot sang hợp đồng chính thức |
| Sales cycle (ngày) | O | 🔧 | Đo số tuần từ demo LTI đến ký hợp đồng mua sắm khoa trước 2026-09-30 |
| Usage depth trong tài khoản | O | ✅ | Telemetry log tỷ lệ sinh viên kích hoạt giải bài tập tuần trên Canvas |
| Chi phí triển khai ÷ ACV | O | 🔧 | Timesheet hỗ trợ cấu hình syllabus và RAG index trước 2026-09-20 |
| Tập trung doanh thu | O | ✅ | Bảng theo dõi ACV 3 hợp đồng khoa đầu tiên so với tổng ARR |
| NRR | G | 🔧 | Đo lường mở rộng số lớp/môn sau 2 học kỳ trước 2027-03-31 |
| Gross Margin | G | ✅ | Đối soát billing token Claude Haiku và chi phí hạ tầng vector DB |
| CAC payback | G | 🔧 | Tính fully-loaded CAC sau khi hoàn thành 3 thương vụ đầu trước 2026-10-31 |

## Đèn báo sớm

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| L-01 | Time-to-first-value | Số ngày từ khi bàn giao LTI 1.3 đến khi khoa đạt 50 resolution học tập thật đạt chuẩn QA; median theo cohort | Tuần · Product Operations | 6 ngày | ≤5 ngày | 6–10 ngày | >10 ngày | [TB] Dùng cohort thử nghiệm 2 khoa ĐHQG và ĐHBK làm tạm chuẩn và chốt baseline vào 2026-10-31 | 2026-08-28 | POC-to-paid và tỷ lệ kích hoạt sinh viên | R-01 |
| L-02 | Weekly student resolution rate | Tỷ lệ sinh viên có ít nhất 2 resolution học tập đạt chuẩn mỗi tuần chia tổng sinh viên active trong danh sách môn | Tuần · Customer Success | 58% | ≥65% | 45–64% | <45% | [TB] Dữ liệu pilot 150 sinh viên tại ĐHBK; chốt baseline chính thức sau 3 cohort vào 2026-10-31 | 2026-08-28 | Time-to-first-value và gia hạn hợp đồng | R-02 |

## Đèn vận hành

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| O-01 | Tỷ lệ kích hoạt Pilot thành công | Tỷ lệ pilot đạt trên 500 resolution trong 30 ngày chia tổng số pilot khoa bắt đầu triển khai | Tuần · Product Operations | 66% | ≥75% | 50–74% | <50% | [MH] MH-02 cần ít nhất 3/4 pilot activate để đạt chỉ tiêu 3 hợp đồng B2B chính thức | 2026-08-28 | POC-to-paid | R-03 |
| O-02 | Chi phí AI trên mỗi job hoàn thành | Tổng token Claude Haiku và chi phí inference Vector DB chia số resolution thành công đạt chuẩn QA | Tuần · FinOps | 840 đ | ≤1.000 đ | 1.001–1.800 đ | >1.800 đ | [MH] MH-01 suy từ gross margin mục tiêu 84% và trần chi phí AI từ Day 25 | 2026-08-28 | Gross margin | R-04 |
| O-03 | POC-to-paid conversion rate | Số pilot khoa chuyển đổi thành hợp đồng hàng năm chính thức chia tổng số pilot kết thúc trong kỳ | Tháng · Revenue Operations | 50% | ≥60% | 40–59% | <40% | [BM] ICONIQ State of Go-to-Market 2026 https://www.iconiq.com/growth/reports/state-of-go-to-market-2026 tham chiếu tỷ lệ chuyển đổi POC sang hợp đồng trả phí ~50% | 2026-08-28 | ARR và CAC payback | R-03 |

## Đèn kết quả

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| G-01 | Gross margin sau chi phí AI | Doanh thu trừ toàn bộ chi phí biến đổi (API token, hosting, retry, HITL) chia doanh thu | Tháng · Finance | 82% | ≥80% | 65–79% | <65% | [MH] MH-01 đặt trần chi phí AI để duy trì gross margin mục tiêu trên 80% theo mô hình Day 24-25 | 2026-08-28 | Runway và CAC payback | R-04 |
| G-02 | Net Revenue Retention | Doanh thu cohort khoa cuối năm chia doanh thu đầu năm sau khi tính mở rộng thêm môn/ngành và hủy hợp đồng | Quý · Finance | 100% | ≥110% | 100–109% | <100% | [BM] Benchmarkit 2025 SaaS Performance Metrics https://www.benchmarkit.ai/2025benchmarks trung vị NRR 101% và mục tiêu top quartile 110% | 2026-08-28 | LTV và tăng trưởng doanh thu dài hạn | R-05 |

## Luật quyết định

| ID | NẾU | TRONG | VÀ | THÌ | KHÔNG THÌ | Luật dừng? |
|---|---|---|---|---|---|---|
| R-01 | Median TTFV > 10 ngày | 2 cohort triển khai liên tiếp | Mỗi cohort có ít nhất 2 khoa tham gia | Đóng băng tiếp nhận pilot mới trong 14 ngày và tinh gọn quy trình cấu hình RAG syllabus xuống đúng 1 môn học cốt lõi | Không giảm giá hợp đồng để bù đắp sự chậm trễ trong việc chứng minh giá trị | CÓ |
| R-02 | Weekly resolution rate < 45% | 3 tuần liên tiếp | Có ít nhất 100 sinh viên trong danh sách lớp | Biệt phái 1 chuyên viên Product Ops trực tiếp hỗ trợ giảng viên gắn bài tập tuần vào widget Canvas | Không gửi email spam thúc ép sinh viên khi giao diện chưa thuận tiện | KHÔNG |
| R-03 | Pilot activation rate < 50% | 2 kỳ đánh giá liên tiếp | Có ít nhất 4 pilot khoa đang chạy | Dừng toàn bộ hoạt động outbound sales mới và tập trung tối ưu hóa kịch bản onboarding 1-click cho giảng viên | Không tăng ngân sách sales để tìm thêm pilot mới khi tỷ lệ kích hoạt chưa đạt chuẩn | CÓ |
| R-04 | Chi phí AI trên mỗi job > 1.800 đ | 2 tuần liên tiếp | Có ít nhất 1.000 resolution phát sinh | Bật tính năng prompt caching, cắt giảm độ dài context RAG và chuyển các truy vấn đơn giản sang model tier nhỏ hơn | Không tắt bộ lọc an toàn và kiểm duyệt chất lượng để giảm chi phí token ảo | KHÔNG |
| R-05 | NRR < 100% | 2 quý liên tiếp | Có ít nhất 3 hợp đồng khoa đến kỳ gia hạn | Tổ chức phiên làm việc trực tiếp với Trưởng khoa để đánh giá báo cáo giảm tải cho TA và giải quyết các rào cản tính năng | Không tính toán gộp cơ hội bán mới từ các trường khác vào chỉ số duy trì tài khoản cũ | KHÔNG |

## Cổng gác 90 ngày

| Ngày | Metric gác cổng | Ngưỡng | Bằng chứng vật lý | Nếu đạt | Nếu trượt |
|---:|---|---|---|---|---|
| 30 | Xác nhận Pain Moment và độ chính xác RAG syllabus từ 3 Trưởng bộ môn | ≥85% Factual Accuracy và 3/3 bộ môn ký biên bản nghiệm thu kỹ thuật | Biên bản nghiệm thu kỹ thuật và file eval log 30 slices | GO | FIX |
| 60 | Tỷ lệ sinh viên active giải bài tập tuần | ≥50% trên tổng số 600 sinh viên tại 2 khoa pilot | Báo cáo trích xuất telemetry log từ Canvas LTI | GO | PIVOT |
| 90 | Gross margin sau chi phí AI và chuyển đổi hợp đồng chính thức | Gross margin ≥80% và có ít nhất 2 hợp đồng B2B chính thức | Hợp đồng kinh tế đã ký và sao kê thanh toán đợt 1 | GO | KILL |

## Kill criteria

KILL dự án vào ngày 90 nếu sau 2 chu kỳ tối ưu kỹ thuật RAG mà tỷ lệ chuyển đổi POC sang hợp đồng trả phí vẫn dưới 30% và không có khoa nào đồng ý mức giá nền tối thiểu $1.50/sinh viên/tháng.

## Chưa đo được

| Đèn hoặc giả định | Cần gì để đo | Ai chịu trách nhiệm | Ngày có số |
|---|---|---|---|
| Tỷ lệ Trợ giảng (TA) tiết kiệm thực tế 70% thời gian giải đáp | Bảng đối soát số giờ trực của TA trước và sau khi tích hợp Cursus tại 2 khoa | Customer Success Lead | 2026-09-30 |

## Phụ lục ngưỡng suy từ mô hình

| ID | Metric | Input Day 24–25 | Phép tính | Kết quả và ngưỡng áp dụng |
|---|---|---|---|---|
| MH-01 | Chi phí AI tối đa trên mỗi resolution | Giá bán đề xuất 9.100 đ/job ($0.35); Gross margin mục tiêu 84%; Chi phí biến đổi phi AI (HITL, Infra, Overhead) là 600 đ/job | 9.100 × (1 − 0.84) − 600 = 856 | Xanh khi chi phí AI ≤1.000 đ/job; Vàng 1.001–1.800 đ/job; Đỏ khi >1.800 đ/job (áp dụng cho O-02 và G-01) |
| MH-02 | Tỷ lệ kích hoạt Pilot tối thiểu | Mục tiêu ký 3 hợp đồng B2B trả phí ($14.400 ACV/deal) từ phễu 4 khoa pilot tham gia thử nghiệm | 3 ÷ 4 = 75% | Xanh khi tỷ lệ kích hoạt ≥75%; Vàng 50–74%; Đỏ khi <50% do không còn đường đạt kế hoạch doanh thu (áp dụng cho O-01) |

## Ghi nhận AI critique

| Phản biện | Chấp nhận hay bác bỏ | Thay đổi đã thực hiện | Lý do |
|---|---|---|---|
| TTFV cho trường đại học cần đo theo số resolution học tập thay vì chỉ số lượng SV đăng nhập | Chấp nhận | Đặt ngưỡng đạt 50 resolution học tập thật đạt chuẩn QA | Tránh ảo tưởng khi sinh viên chỉ mở app nhưng không thực sự học tập |
| Nên lấy benchmark NRR SaaS chung 101% làm ngưỡng đỏ | Bác bỏ | Đặt ngưỡng đỏ là <100% và xanh là ≥110% | Trong phân khúc giáo dục đại học, nếu NRR dưới 100% nghĩa là khoa bị teo tóp số lớp đăng ký |
| Cần có cơ chế kiểm soát token cost tránh sinh viên spam câu hỏi ngoài bài học | Chấp nhận | Đưa rule R-04 với prompt caching và chuyển model tier tự động | Bảo vệ biên lợi nhuận gộp 84% khỏi nguy cơ vượt trần inference cost |
