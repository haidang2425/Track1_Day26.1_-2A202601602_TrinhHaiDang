# Operating Dashboard — Cursus AI

> Bản tóm tắt vận hành 1 trang (Executive Summary) cho Cursus AI — AI Educational Copilot & Learning Companion for Higher Education. Toàn bộ số liệu đối soát chi tiết nằm trong worksheet nguồn `operating-dashboard.md`.

**Mô hình:** B2B · **Cập nhật:** 2026-08-28 · **Owner:** Product Operations

**Chẩn đoán:** B2B Higher Education — Khoa/Trường Đại học ký hợp đồng và thanh toán định kỳ từ ngân sách đào tạo và quỹ trợ giảng; Giảng viên và Sinh viên sử dụng trực tiếp qua Canvas LMS (chuẩn LTI 1.3).

**North Star Metric:** Time-to-first-value ≤ 5 ngày với ít nhất 50 sinh viên active trong khóa học (Hiện tại: 6 ngày — Trạng thái: Cảnh báo).

## Cây đèn 3 tầng (Signal Tree)

| Tầng · ID | Metric và định nghĩa ngắn | Hiện tại · [Xanh / Vàng / Đỏ] · Nguồn | Nhịp · Owner | Báo trước cho · Luật |
|---|---|---|---|---|
| L · L-01 | TTFV: Số ngày từ LTI đến khi đạt 50 resolution QA | 6 ngày · [≤5 / 6–10 / >10 ngày] · `[TB]` | Tuần · Product Ops | POC-to-paid · R-01 (Dừng) |
| L · L-02 | Weekly resolution rate: % SV active có ≥2 resolution/tuần | 58% · [≥65% / 45–64% / <45%] · `[TB]` | Tuần · Customer Success | TTFV & Churn · R-02 |
| O · O-01 | Pilot activation rate: % pilot đạt >500 resolution/30 ngày | 66% · [≥75% / 50–74% / <50%] · `[MH]` | Tuần · Product Ops | POC-to-paid · R-03 (Dừng) |
| O · O-02 | Chi phí AI / job: Token Claude Haiku + Infra / resolution | 840 đ · [≤1.000 / 1.001–1.800 / >1.800 đ] · `[MH]` | Tuần · FinOps | Gross Margin · R-04 |
| O · O-03 | POC-to-paid conversion: Tỷ lệ chuyển đổi sang hợp đồng năm | 50% · [≥60% / 40–59% / <40%] · `[BM]` | Tháng · Revenue Ops | ARR & Payback · R-03 (Dừng) |
| G · G-01 | Gross margin sau chi phí AI: (Doanh thu − COGS AI) / Doanh thu | 82% · [≥80% / 65–79% / <65%] · `[MH]` | Tháng · Finance | Runway & Payback · R-04 |
| G · G-02 | Net Revenue Retention (NRR): Tăng trưởng cohort sau mở rộng | 100% · [≥110% / 100–109% / <100%] · `[BM]` | Quý · Finance | LTV & Doanh thu · R-05 |

## Luật quyết định (Decision Rules)

| ID | NẾU · TRONG · VÀ | THÌ (Hành động bắt buộc) | KHÔNG THÌ (Cấm phản xạ sai) | Dừng? |
|---|---|---|---|:---:|
| R-01 | Median TTFV > 10 ngày · 2 cohort liên tiếp · ≥2 khoa/cohort | Đóng băng nhận pilot mới 14 ngày; rút gọn RAG syllabus còn 1 môn cốt lõi | CẤM giảm giá hợp đồng để bù đắp sự chậm trễ | CÓ |
| R-02 | Weekly resolution < 45% · 3 tuần liên tiếp · ≥100 SV active | Biệt phái 1 Product Ops hỗ trợ GV gắn bài tập vào Canvas widget | CẤM gửi email spam thúc ép sinh viên | KHÔNG |
| R-03 | Pilot activation < 50% · 2 kỳ liên tiếp · ≥4 pilot đang chạy | Dừng toàn bộ outbound sales mới; tối ưu onboarding 1-click cho giảng viên | CẤM tăng ngân sách sales để bù tỷ lệ kích hoạt thấp | CÓ |
| R-04 | Chi phí AI/job > 1.800 đ · 2 tuần liên tiếp · ≥1.000 resolution | Bật prompt caching, rút ngắn context RAG, chuyển routing model nhỏ hơn | CẤM tắt kiểm duyệt an toàn để giảm chi phí token | KHÔNG |
| R-05 | NRR < 100% · 2 quý liên tiếp · ≥3 hợp đồng khoa đến hạn | Tổ chức đối thoại trực tiếp Trưởng khoa về báo cáo giảm tải TA | CẤM gộp cơ hội bán mới từ trường khác vào NRR cũ | KHÔNG |

## Cổng gác 90 ngày (90-Day Stage Gates)

| Ngày | Metric gác cổng & Ngưỡng | Bằng chứng vật lý (Evidence) | Đạt / Trượt |
|---:|---|---|:---:|
| 30 | Độ chính xác RAG syllabus ≥ 85% & 3/3 Trưởng bộ môn nghiệm thu | Biên bản nghiệm thu kỹ thuật & Eval log 30 slices | GO / FIX |
| 60 | Tỷ lệ SV active giải bài tập tuần ≥ 50% trên 600 SV pilot | Telemetry log trích xuất từ Canvas LMS (LTI 1.3) | GO / PIVOT |
| 90 | Gross Margin sau AI ≥ 80% & có ≥ 2 hợp đồng B2B chính thức | Hợp đồng kinh tế đã ký ($14.400 ACV) & sao kê đợt 1 | GO / KILL |

**Kill Criteria:** Dừng dự án (KILL) vào ngày 90 nếu sau 2 chu kỳ tối ưu kỹ thuật RAG mà tỷ lệ chuyển đổi POC sang hợp đồng trả phí vẫn dưới 30% và không có khoa nào chấp nhận mức giá nền tối thiểu $1.50/sinh viên/tháng.

**Chưa đo được:** Tỷ lệ Trợ giảng (TA) tiết kiệm thực tế 70% thời gian giải đáp · Cần bảng đối soát số giờ trực TA trước/sau tích hợp tại 2 khoa pilot · Owner: Customer Success Lead · Ngày có số: 2026-09-30.
