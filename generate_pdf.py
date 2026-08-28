import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register TrueType fonts for full Vietnamese Unicode support
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'C:/Windows/Fonts/ariali.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'C:/Windows/Fonts/arialbi.ttf'))

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        name='MainTitle',
        fontName='Arial-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0F172A')
    )
    
    sub_title_style = ParagraphStyle(
        name='SubTitle',
        fontName='Arial-Italic',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#475569')
    )

    h2_style = ParagraphStyle(
        name='Heading2',
        fontName='Arial-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=4,
        spaceAfter=2
    )

    meta_style = ParagraphStyle(
        name='MetaText',
        fontName='Arial',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#1E293B')
    )

    meta_bold = ParagraphStyle(
        name='MetaBold',
        fontName='Arial-Bold',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )

    body_style = ParagraphStyle(
        name='TableBody',
        fontName='Arial',
        fontSize=6.8,
        leading=8.5,
        textColor=colors.HexColor('#1E293B')
    )

    body_bold = ParagraphStyle(
        name='TableBodyBold',
        fontName='Arial-Bold',
        fontSize=6.8,
        leading=8.5,
        textColor=colors.HexColor('#0F172A')
    )

    header_style = ParagraphStyle(
        name='TableHeader',
        fontName='Arial-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.white
    )

    callout_style = ParagraphStyle(
        name='CalloutText',
        fontName='Arial',
        fontSize=7,
        leading=9.2,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # ================= PAGE 1: 1-PAGE OPERATING DASHBOARD =================
    story.append(Paragraph("OPERATING DASHBOARD — CURSUS AI (Higher Education)", title_style))
    story.append(Paragraph("Học viên: <b>Trịnh Hải Đăng</b> | Mã học viên: <b>2A202601602</b> | Mô hình: <b>B2B</b> | Cập nhật: <b>2026-08-28</b> | Owner: <b>Product Operations Lead</b>", meta_style))
    story.append(Spacer(1, 2))
    
    diag_text = (
        "<b>Chẩn đoán:</b> Cursus AI là B2B vì Khoa/Trường Đại học ký hợp đồng và trả phí định kỳ ($14.400 ACV/khoa) từ ngân sách vận hành đào tạo & quỹ TA; Giảng viên và Sinh viên sử dụng trực tiếp qua Canvas LMS LTI 1.3.<br/>"
        "<b>North Star Metric:</b> <b>Time-to-first-value &le; 5 ngày</b> với ít nhất 50 sinh viên active trong khóa học (Hiện tại: 6 ngày | Trạng thái: 🟡)."
    )
    story.append(Paragraph(diag_text, meta_style))
    story.append(Spacer(1, 3))

    # Table 1: 3-Tier Signal Dashboard
    story.append(Paragraph("1. CÂY TÍN HIỆU 3 TẦNG (Signal Tree & Indicator Thresholds)", h2_style))
    
    col_widths_p1 = [42, 120, 160, 65, 80, 88]
    data_p1 = [
        [
            Paragraph("Tầng · ID", header_style),
            Paragraph("Tên đèn & Định nghĩa", header_style),
            Paragraph("Ngưỡng: 🟢 Xanh | 🟡 Vàng | 🔴 Đỏ", header_style),
            Paragraph("Hiện tại · Nguồn", header_style),
            Paragraph("Nhịp · Owner", header_style),
            Paragraph("Báo trước cho · Luật", header_style)
        ],
        [
            Paragraph("<b>L · L-01</b>", body_style),
            Paragraph("<b>Time-to-first-value (TTFV)</b><br/>Số ngày từ kết nối LTI đến khi đạt 50 resolution QA", body_style),
            Paragraph("🟢 &le;5 ngày | 🟡 6–10 ngày | 🔴 >10 ngày", body_style),
            Paragraph("6 ngày<br/>[TB] Pilot cohort", body_style),
            Paragraph("Tuần<br/>Product Ops", body_style),
            Paragraph("POC-to-paid & SV active<br/><b>R-01 (Dừng)</b>", body_style)
        ],
        [
            Paragraph("<b>L · L-02</b>", body_style),
            Paragraph("<b>Weekly student resolution rate</b><br/>% SV active có &ge;2 resolution đạt chuẩn QA / tuần", body_style),
            Paragraph("🟢 &ge;65% | 🟡 45–64% | 🔴 <45%", body_style),
            Paragraph("58%<br/>[TB] ĐHBK log", body_style),
            Paragraph("Tuần<br/>Customer Success", body_style),
            Paragraph("TTFV & Churn sớm<br/><b>R-02</b>", body_style)
        ],
        [
            Paragraph("<b>O · O-01</b>", body_style),
            Paragraph("<b>Pilot activation rate</b><br/>% pilot khoa đạt >500 resolution trong 30 ngày", body_style),
            Paragraph("🟢 &ge;75% | 🟡 50–74% | 🔴 <50%", body_style),
            Paragraph("66%<br/>[MH] MH-02", body_style),
            Paragraph("Tuần<br/>Product Ops", body_style),
            Paragraph("POC-to-paid conversion<br/><b>R-03 (Dừng)</b>", body_style)
        ],
        [
            Paragraph("<b>O · O-02</b>", body_style),
            Paragraph("<b>Chi phí AI / completed job</b><br/>Tổng Token Claude Haiku + Infra chia resolution QA", body_style),
            Paragraph("🟢 &le;1.000 đ | 🟡 1.001–1.800 đ | 🔴 >1.800 đ", body_style),
            Paragraph("840 đ<br/>[MH] MH-01", body_style),
            Paragraph("Tuần<br/>FinOps", body_style),
            Paragraph("Gross Margin & Runway<br/><b>R-04</b>", body_style)
        ],
        [
            Paragraph("<b>O · O-03</b>", body_style),
            Paragraph("<b>POC-to-paid conversion</b><br/>% pilot chuyển đổi thành hợp đồng năm chính thức", body_style),
            Paragraph("🟢 &ge;60% | 🟡 40–59% | 🔴 <40%", body_style),
            Paragraph("50%<br/>[BM] ICONIQ '26", body_style),
            Paragraph("Tháng<br/>Revenue Ops", body_style),
            Paragraph("ARR & CAC payback<br/><b>R-03 (Dừng)</b>", body_style)
        ],
        [
            Paragraph("<b>G · G-01</b>", body_style),
            Paragraph("<b>Gross margin sau chi phí AI</b><br/>(Doanh thu &minus; toàn bộ COGS AI) ÷ Doanh thu", body_style),
            Paragraph("🟢 &ge;80% | 🟡 65–79% | 🔴 <65%", body_style),
            Paragraph("82%<br/>[MH] MH-01", body_style),
            Paragraph("Tháng<br/>Finance", body_style),
            Paragraph("Runway & Payback 12m<br/><b>R-04</b>", body_style)
        ],
        [
            Paragraph("<b>G · G-02</b>", body_style),
            Paragraph("<b>Net Revenue Retention (NRR)</b><br/>Doanh thu cohort sau mở rộng môn/lớp và churn", body_style),
            Paragraph("🟢 &ge;110% | 🟡 100–109% | 🔴 <100%", body_style),
            Paragraph("100%<br/>[BM] Benchmarkit", body_style),
            Paragraph("Quý<br/>Finance", body_style),
            Paragraph("LTV & Định giá cty<br/><b>R-05</b>", body_style)
        ]
    ]

    t1 = Table(data_p1, colWidths=col_widths_p1)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(t1)
    story.append(Spacer(1, 3))

    # Table 2: Decision Rules
    story.append(Paragraph("2. LUẬT QUYẾT ĐỊNH VẬN HÀNH (Decision Rules: NẾU &minus; TRONG &minus; VÀ &minus; THÌ &minus; KHÔNG THÌ)", h2_style))
    col_widths_r = [28, 140, 195, 155, 37]
    data_r = [
        [
            Paragraph("ID", header_style),
            Paragraph("NẾU · TRONG · VÀ (Điều kiện kích hoạt)", header_style),
            Paragraph("THÌ (Hành động bắt buộc có động từ)", header_style),
            Paragraph("KHÔNG THÌ (Phản xạ sai bị CẤM)", header_style),
            Paragraph("Dừng?", header_style)
        ],
        [
            Paragraph("<b>R-01</b>", body_style),
            Paragraph("<b>Median TTFV > 10 ngày</b> trong 2 cohort liên tiếp VÀ mỗi cohort có &ge;2 khoa", body_style),
            Paragraph("<b>Đóng băng tiếp nhận pilot mới trong 14 ngày</b> và tinh gọn RAG syllabus xuống đúng 1 môn học cốt lõi", body_style),
            Paragraph("<b>CẤM:</b> Không giảm giá để bù đắp sự chậm trễ trong thấy giá trị", body_style),
            Paragraph("<b>CÓ ⏹</b>", body_bold)
        ],
        [
            Paragraph("<b>R-02</b>", body_style),
            Paragraph("<b>Weekly resolution rate < 45%</b> trong 3 tuần VÀ có &ge;100 SV trong danh sách", body_style),
            Paragraph("<b>Biệt phái 1 Product Ops</b> trực tiếp hỗ trợ giảng viên gắn bài tập tuần vào widget Canvas", body_style),
            Paragraph("<b>CẤM:</b> Không gửi email spam thúc ép sinh viên khi UI chưa tiện", body_style),
            Paragraph("KHÔNG", body_style)
        ],
        [
            Paragraph("<b>R-03</b>", body_style),
            Paragraph("<b>Pilot activation rate < 50%</b> trong 2 kỳ đánh giá VÀ có &ge;4 pilot đang chạy", body_style),
            Paragraph("<b>Dừng toàn bộ outbound sales mới</b> và tập trung tối ưu kịch bản onboarding 1-click cho giảng viên", body_style),
            Paragraph("<b>CẤM:</b> Không tăng ngân sách sales để bù pilot kích hoạt kém", body_style),
            Paragraph("<b>CÓ ⏹</b>", body_bold)
        ],
        [
            Paragraph("<b>R-04</b>", body_style),
            Paragraph("<b>AI cost / job > 1.800 đ</b> trong 2 tuần liên tiếp VÀ có &ge;1.000 resolution phát sinh", body_style),
            Paragraph("<b>Bật prompt caching</b>, cắt giảm độ dài context RAG và chuyển truy vấn đơn giản sang model tier nhỏ", body_style),
            Paragraph("<b>CẤM:</b> Không tắt bộ lọc kiểm duyệt để giảm cost token ảo", body_style),
            Paragraph("KHÔNG", body_style)
        ],
        [
            Paragraph("<b>R-05</b>", body_style),
            Paragraph("<b>NRR < 100%</b> trong 2 quý liên tiếp VÀ có &ge;3 hợp đồng khoa đến kỳ gia hạn", body_style),
            Paragraph("<b>Tổ chức phiên làm việc trực tiếp Trưởng khoa</b> đánh giá báo cáo giảm tải TA và xử lý rào cản", body_style),
            Paragraph("<b>CẤM:</b> Không gộp hợp đồng mới từ trường khác vào NRR tài khoản cũ", body_style),
            Paragraph("KHÔNG", body_style)
        ]
    ]
    t2 = Table(data_r, colWidths=col_widths_r)
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#047857')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F0FDF4')])
    ]))
    story.append(t2)
    story.append(Spacer(1, 3))

    # Table 3: 90-Day Gates & Kill criteria
    story.append(Paragraph("3. CỔNG GÁC 90 NGÀY & KILL CRITERIA", h2_style))
    col_widths_g = [45, 175, 135, 135, 65]
    data_g = [
        [
            Paragraph("Cổng", header_style),
            Paragraph("Metric gác cổng duy nhất", header_style),
            Paragraph("Ngưỡng qua cổng có số", header_style),
            Paragraph("Bằng chứng vật lý đối soát", header_style),
            Paragraph("Quyết định", header_style)
        ],
        [
            Paragraph("<b>Ngày 30</b><br/>(Learning)", body_style),
            Paragraph("Xác nhận Pain Moment & độ chính xác RAG syllabus từ 3 Trưởng bộ môn", body_style),
            Paragraph("&ge;85% Factual Accuracy & 3/3 bộ môn nghiệm thu", body_style),
            Paragraph("Biên bản nghiệm thu KT & file log 30 slices", body_style),
            Paragraph("Đạt: <b>GO</b><br/>Trượt: <b>FIX</b>", body_style)
        ],
        [
            Paragraph("<b>Ngày 60</b><br/>(Operation)", body_style),
            Paragraph("Weekly active student resolution rate trên hệ thống Canvas LMS", body_style),
            Paragraph("&ge;50% trên tổng số 600 sinh viên tại 2 khoa pilot", body_style),
            Paragraph("Báo cáo trích xuất telemetry log LTI 1.3", body_style),
            Paragraph("Đạt: <b>GO</b><br/>Trượt: <b>PIVOT</b>", body_style)
        ],
        [
            Paragraph("<b>Ngày 90</b><br/>(Business)", body_style),
            Paragraph("Gross Margin sau AI cost và chuyển đổi hợp đồng B2B chính thức", body_style),
            Paragraph("Gross Margin &ge;80% & có &ge;2 deal B2B ($14.4K)", body_style),
            Paragraph("Hợp đồng kinh tế đã ký & sao kê thanh toán", body_style),
            Paragraph("Đạt: <b>GO</b><br/>Trượt: <b>KILL</b>", body_style)
        ]
    ]
    t3 = Table(data_g, colWidths=col_widths_g)
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#B45309')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FFFBEB')])
    ]))
    story.append(t3)
    story.append(Spacer(1, 2))

    footer_p1 = (
        "<b>Kill criteria:</b> KILL dự án vào ngày 90 nếu sau 2 chu kỳ tối ưu RAG mà tỷ lệ POC-to-paid vẫn &lt;30% và không có khoa nào chấp nhận giá sàn $1.50/SV/tháng.<br/>"
        "<b>Chưa đo được:</b> Tỷ lệ TA tiết kiệm thực tế 70% thời gian &bull; Cần bảng đối soát giờ trực của TA tại 2 khoa &bull; Owner: Customer Success Lead &bull; Ngày có số: 2026-09-30."
    )
    story.append(Paragraph(footer_p1, meta_style))

    # ================= PAGE 2: APPENDIX & AUDIT TRAIL =================
    story.append(PageBreak())

    story.append(Paragraph("PHỤ LỤC: KIỂM KÊ, CHỨNG MINH NGƯỠNG & AI CRITIQUE", title_style))
    story.append(Paragraph("Phụ lục đối soát dữ liệu Unit Economics Day 24-25, Nguồn Benchmark công khai & Biên bản phản biện", sub_title_style))
    story.append(Spacer(1, 3))

    # Appendix 1: Model Derived Thresholds [MH]
    story.append(Paragraph("A. PHỤ LỤC NGƯỠNG SUY TỪ MÔ HÌNH UNIT ECONOMICS [MH]", h2_style))
    col_widths_mh = [38, 115, 145, 125, 132]
    data_mh = [
        [
            Paragraph("ID", header_style),
            Paragraph("Metric áp dụng", header_style),
            Paragraph("Input Day 24&ndash;25 (Đầy đủ đơn vị)", header_style),
            Paragraph("Phép tính toán học (Có số & dấu =)", header_style),
            Paragraph("Kết quả & Ngưỡng áp dụng", header_style)
        ],
        [
            Paragraph("<b>MH-01</b>", body_style),
            Paragraph("<b>Chi phí AI tối đa / resolution</b><br/>(Áp dụng O-02 & G-01)", body_style),
            Paragraph("Giá bán: 9.100 đ/job ($0.35)<br/>GM mục tiêu: 84%<br/>Chi phí biến đổi khác: 600 đ/job", body_style),
            Paragraph("<b>9.100 &times; (1 &minus; 0.84) &minus; 600 = 856 đ</b><br/>Trần chịu đựng: 9.100 &times; (1 &minus; 0.65) &minus; 600 = 2.585 đ", body_style),
            Paragraph("🟢 &le;1.000 đ/job (An toàn GM >82%)<br/>🟡 1.001&ndash;1.800 đ (GM 70&ndash;80%)<br/>🔴 >1.800 đ (Báo động vi phạm GM)", body_style)
        ],
        [
            Paragraph("<b>MH-02</b>", body_style),
            Paragraph("<b>Tỷ lệ kích hoạt Pilot tối thiểu</b><br/>(Áp dụng O-01)", body_style),
            Paragraph("Mục tiêu doanh thu: Ký 3 hợp đồng B2B ($14.400 ACV) từ phễu 4 pilot khoa", body_style),
            Paragraph("<b>3 &divide; 4 = 75%</b><br/>Mức hòa vốn GTM: 2 &divide; 4 = 50%", body_style),
            Paragraph("🟢 &ge;75% (Đạt kế hoạch 3 deal)<br/>🟡 50&ndash;74% (Cần tối ưu chuyển đổi)<br/>🔴 <50% (Đỏ vì mất đường đạt ARR)", body_style)
        ]
    ]
    tmh = Table(data_mh, colWidths=col_widths_mh)
    tmh.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(tmh)
    story.append(Spacer(1, 3))

    # Appendix 2: Candidate Lights Inventory (11 rows)
    story.append(Paragraph("B. KIỂM KÊ TOÀN BỘ 11 ĐÈN ỨNG VIÊN B2B (Handbook Candidate Inventory)", h2_style))
    col_widths_inv = [135, 28, 42, 350]
    data_inv = [
        [
            Paragraph("Đèn ứng viên B2B từ Handbook", header_style),
            Paragraph("Tầng", header_style),
            Paragraph("Trạng thái", header_style),
            Paragraph("Bằng chứng hiện có / Kế hoạch đo lường chi tiết", header_style)
        ],
        [
            Paragraph("Time-to-first-value (TTFV)", body_style),
            Paragraph("L", body_style),
            Paragraph("✅", body_style),
            Paragraph("Log tích hợp LTI 1.3 và event 50 resolution đầu tiên của sinh viên", body_style)
        ],
        [
            Paragraph("Pipeline coverage", body_style),
            Paragraph("L", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Chuẩn hóa stage cơ hội và CRM pipeline của 8 khoa mục tiêu trước 2026-09-15", body_style)
        ],
        [
            Paragraph("% deal chết ở khâu security/procurement", body_style),
            Paragraph("L", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Theo dõi lý do từ chối về DPA/bảo mật RAG trong CRM trước 2026-09-15", body_style)
        ],
        [
            Paragraph("POC &rarr; paid", body_style),
            Paragraph("O", body_style),
            Paragraph("✅", body_style),
            Paragraph("Biên bản MOU và kết quả chuyển đổi từ 3 pilot sang hợp đồng chính thức", body_style)
        ],
        [
            Paragraph("Sales cycle (ngày)", body_style),
            Paragraph("O", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Đo số tuần từ demo LTI đến ký hợp đồng mua sắm khoa trước 2026-09-30", body_style)
        ],
        [
            Paragraph("Usage depth trong tài khoản", body_style),
            Paragraph("O", body_style),
            Paragraph("✅", body_style),
            Paragraph("Telemetry log tỷ lệ sinh viên kích hoạt giải bài tập tuần trên Canvas", body_style)
        ],
        [
            Paragraph("Chi phí triển khai &divide; ACV", body_style),
            Paragraph("O", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Timesheet hỗ trợ cấu hình syllabus và RAG index trước 2026-09-20", body_style)
        ],
        [
            Paragraph("Tập trung doanh thu", body_style),
            Paragraph("O", body_style),
            Paragraph("✅", body_style),
            Paragraph("Bảng theo dõi ACV 3 hợp đồng khoa đầu tiên so với tổng ARR", body_style)
        ],
        [
            Paragraph("NRR", body_style),
            Paragraph("G", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Đo lường mở rộng số lớp/môn sau 2 học kỳ trước 2027-03-31", body_style)
        ],
        [
            Paragraph("Gross Margin", body_style),
            Paragraph("G", body_style),
            Paragraph("✅", body_style),
            Paragraph("Đối soát billing token Claude Haiku và chi phí hạ tầng vector DB", body_style)
        ],
        [
            Paragraph("CAC payback", body_style),
            Paragraph("G", body_style),
            Paragraph("🔧", body_style),
            Paragraph("Tính fully-loaded CAC sau khi hoàn thành 3 thương vụ đầu trước 2026-10-31", body_style)
        ]
    ]
    tinv = Table(data_inv, colWidths=col_widths_inv)
    tinv.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#334155')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(tinv)
    story.append(Spacer(1, 3))

    # Appendix 3: AI Critique & Peer Review
    story.append(Paragraph("C. GHI NHẬN AI CRITIQUE & PHẢN BIỆN CHUYÊN MÔN", h2_style))
    col_widths_ai = [155, 65, 165, 170]
    data_ai = [
        [
            Paragraph("Ý kiến phản biện AI", header_style),
            Paragraph("Quyết định", header_style),
            Paragraph("Thay đổi đã thực hiện", header_style),
            Paragraph("Lý do & Thuyết minh chuyên môn", header_style)
        ],
        [
            Paragraph("TTFV cho trường đại học cần đo theo số resolution học tập thay vì chỉ số lượng SV đăng nhập", body_style),
            Paragraph("<b>Chấp nhận</b>", body_style),
            Paragraph("Định nghĩa TTFV là thời gian đạt 50 resolution học tập đạt chuẩn QA", body_style),
            Paragraph("Tránh bẫy vanity metric khi sinh viên đăng nhập nhưng không thực sự học", body_style)
        ],
        [
            Paragraph("Nên lấy benchmark NRR SaaS chung 101% làm ngưỡng đỏ", body_style),
            Paragraph("<b>Bác bỏ</b>", body_style),
            Paragraph("Giữ ngưỡng đỏ là &lt;100% và xanh là &ge;110%", body_style),
            Paragraph("Trong B2B giáo dục, nếu NRR &lt;100% nghĩa là khoa bị cắt giảm môn học", body_style)
        ],
        [
            Paragraph("Cần có cơ chế kiểm soát token cost tránh sinh viên spam câu hỏi ngoài bài học", body_style),
            Paragraph("<b>Chấp nhận</b>", body_style),
            Paragraph("Bổ sung rule R-04 kích hoạt prompt caching & dynamic routing", body_style),
            Paragraph("Bảo vệ biên lợi nhuận gộp 84% khỏi nguy cơ đội chi phí inference", body_style)
        ]
    ]
    tai = Table(data_ai, colWidths=col_widths_ai)
    tai.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4C1D95')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#FAF5FF')])
    ]))
    story.append(tai)

    doc.build(story)
    print(f"Generated {filename} successfully.")

if __name__ == '__main__':
    build_pdf('TrinhHaiDang_Day26_dashboard.pdf')
    build_pdf('submissions/2A202601602/TrinhHaiDang_Day26_dashboard.pdf')
