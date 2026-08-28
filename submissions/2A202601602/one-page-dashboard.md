# Operating Dashboard — Cursus AI

> Bản rút gọn để xuất trang 1 PDF. Mọi giá trị phải khớp worksheet nguồn; chi
> tiết nguồn và hai phép tính `[MH]` nằm ở phụ lục trang 2.

**Model:** B2B · **Cập nhật:** 2026-08-28 · **Owner phiên họp:** Product Operations Lead

**Chẩn đoán:** B2B · Khoa/Trường Đại học trả tiền · Giảng viên & Sinh viên sử dụng trực tiếp qua Canvas LTI 1.3

**North Star:** Time-to-first-value dưới 5 ngày với ít nhất 50 sinh viên active · hiện tại 6 ngày · mục tiêu ≤5 ngày · trạng thái 🟡

## Cây đèn 3 tầng

| Tầng · ID | Metric và định nghĩa ngắn | Hiện tại · 🟢 / 🟡 / 🔴 · Nguồn | Nhịp · Owner | Báo trước cho · Luật |
|---|---|---|---|---|
| L · L-01 | Time-to-first-value (Số ngày đạt 50 resolution QA) | 6 ngày · ≤5 / 6–10 / >10 ngày · [TB] | Tuần · Product Ops | POC-to-paid · R-01 |
| L · L-02 | Weekly student resolution rate (% SV active có ≥2 job) | 58% · ≥65% / 45–64% / <45% · [TB] | Tuần · Customer Success | TTFV · R-02 |
| O · O-01 | Pilot activation rate (% pilot có >500 resolution) | 66% · ≥75% / 50–74% / <50% · [MH] | Tuần · Product Ops | POC-to-paid · R-03 |
| O · O-02 | Chi phí AI trên mỗi job (Token + Infra inference) | 840 đ · ≤1.000 / 1.001–1.800 / >1.800 đ · [MH] | Tuần · FinOps | Gross Margin · R-04 |
| G · G-01 | Gross margin sau chi phí AI (Doanh thu trừ COGS AI) | 82% · ≥80% / 65–79% / <65% · [MH] | Tháng · Finance | Runway · R-04 |
| G · G-02 | Net Revenue Retention (NRR sau expansion và churn) | 100% · ≥110% / 100–109% / <100% · [BM] | Quý · Finance | LTV · R-05 |

## Luật quyết định

| ID | NẾU · TRONG · VÀ | THÌ | KHÔNG THÌ | Dừng? |
|---|---|---|---|---|
| R-01 | Median TTFV > 10 ngày · 2 cohort liên tiếp · Mỗi cohort ≥2 khoa | Đóng băng nhận pilot mới 14 ngày & tinh gọn RAG 1 môn | Không giảm giá để bù chậm thấy giá trị | CÓ |
| R-02 | Weekly resolution rate < 45% · 3 tuần · Có ≥100 sinh viên | Biệt phái 1 Product Ops hỗ trợ giảng viên gắn Canvas widget | Không gửi email spam thúc ép sinh viên | KHÔNG |
| R-03 | Pilot activation rate < 50% · 2 kỳ đánh giá · Có ≥4 pilot | Dừng outbound sales & tối ưu onboarding 1-click cho GV | Không tăng ngân sách sales để bù pilot hỏng | CÓ |
| R-04 | AI cost mỗi job > 1.800 đ · 2 tuần · Có ≥1.000 resolution | Bật prompt caching, giảm RAG context & hạ model tier | Không tắt bộ lọc kiểm duyệt an toàn | KHÔNG |
| R-05 | NRR < 100% · 2 quý liên tiếp · Có ≥3 hợp đồng gia hạn | Họp trực tiếp Trưởng khoa giải quyết rào cản tính năng | Không gộp deal mới từ trường khác vào NRR | KHÔNG |

## Cổng 90 ngày

| Ngày | Một metric · ngưỡng | Evidence | Đạt / Trượt |
|---:|---|---|---|
| 30 | Xác nhận Pain & Eval RAG syllabus · ≥85% Factual Accuracy | Biên bản nghiệm thu KT & eval log 30 slices | GO / FIX |
| 60 | Weekly active resolution rate · ≥50% trên 600 sinh viên | Telemetry log xuất từ Canvas LMS LTI | GO / PIVOT |
| 90 | Gross margin sau AI & B2B deal · GM ≥80% & 2 deal B2B ($14.4K) | Hợp đồng kinh tế ký kết & sao kê thanh toán | GO / KILL |

**Kill criteria:** KILL dự án vào ngày 90 nếu sau 2 chu kỳ tối ưu RAG mà tỷ lệ POC-to-paid vẫn <30% và không có khoa nào chấp nhận giá sàn $1.50/SV/tháng.

**Chưa đo được:** Tỷ lệ TA tiết kiệm thực tế 70% thời gian · cần bảng đối soát giờ trực của TA tại 2 khoa pilot · owner Customer Success Lead · có số ngày 2026-09-30
