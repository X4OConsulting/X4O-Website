"""
Phase 4 Testing Reports Generator - Part 1
Creates individual DOCX reports for Form Functionality and Responsive Design tests
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os

# Brand colors
PRIMARY_COLOR = RGBColor(151, 192, 232)  # #97c0e8
PRIMARY_DARK = RGBColor(23, 64, 105)     # #174069

def set_heading_format(run, size=14, color=PRIMARY_DARK, bold=True):
    """Apply consistent heading formatting"""
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.name = 'Inter'

def add_status_badge(paragraph, status):
    """Add colored status badge"""
    run = paragraph.add_run(f' [{status}]')
    run.font.bold = True
    if status == 'PASSED':
        run.font.color.rgb = RGBColor(0, 128, 0)  # Green
    elif status == 'FAILED':
        run.font.color.rgb = RGBColor(255, 0, 0)  # Red
    elif status == 'PARTIAL':
        run.font.color.rgb = RGBColor(255, 165, 0)  # Orange

def create_form_functionality_report():
    """Create Form Functionality Testing Report"""
    doc = Document()

    # Title
    title = doc.add_heading('Form Functionality Testing Report', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    set_heading_format(title.runs[0], size=18, color=PRIMARY_DARK)

    # Metadata table
    doc.add_paragraph()
    table = doc.add_table(rows=8, cols=2)
    table.style = 'Light Grid Accent 1'

    metadata = [
        ('Test Category', 'Form Functionality Testing'),
        ('Test Date', 'February 11, 2026'),
        ('Tester', 'Keenan Husselmann'),
        ('Environment', 'Production (https://x4o.co.za)'),
        ('Total Test Cases', '8'),
        ('Passed', '8'),
        ('Failed', '0'),
        ('Pass Rate', '100%')
    ]

    for i, (label, value) in enumerate(metadata):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = value
        table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    # Test Objective
    doc.add_heading('Test Objective', 1)
    doc.add_paragraph(
        'Verify contact form accepts input, validates fields correctly, prevents spam, '
        'and redirects to success page upon submission. Ensure Netlify Forms integration '
        'is functioning correctly and query parameter pre-fill works for booking requests.'
    )

    # Test Environment
    doc.add_heading('Test Environment', 1)
    env_table = doc.add_table(rows=4, cols=2)
    env_table.style = 'Light List Accent 1'

    env_data = [
        ('URL', 'https://x4o.co.za/contact'),
        ('Form Name', 'contact'),
        ('Backend', 'Netlify Forms'),
        ('Spam Protection', 'Honeypot field (bot-field)')
    ]

    for i, (label, value) in enumerate(env_data):
        env_table.rows[i].cells[0].text = label
        env_table.rows[i].cells[1].text = value

    # Test Cases
    doc.add_page_break()
    doc.add_heading('Test Cases & Results', 1)

    # TC-FORM-001
    tc1 = doc.add_heading('TC-FORM-001: Form Fields Present', 2)
    add_status_badge(tc1, 'PASSED')

    doc.add_paragraph('Objective: Verify all required form fields are present and correctly configured.')

    fields_table = doc.add_table(rows=7, cols=5)
    fields_table.style = 'Light Grid Accent 1'

    headers = ['Field', 'Type', 'Required', 'Present', 'ID Attribute']
    for i, header in enumerate(headers):
        cell = fields_table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    fields_data = [
        ('Name', 'text', 'Yes', '✅', 'name'),
        ('Email', 'email', 'Yes', '✅', 'email'),
        ('Phone', 'tel', 'No', '✅', 'phone'),
        ('Subject', 'select', 'No', '✅', 'subject'),
        ('Message', 'textarea', 'Yes', '✅', 'message'),
        ('bot-field', 'hidden', 'No', '✅', '(honeypot)')
    ]

    for i, row_data in enumerate(fields_data, start=1):
        for j, value in enumerate(row_data):
            fields_table.rows[i].cells[j].text = value

    doc.add_paragraph('\nResult: All 6 fields present and correctly configured.').runs[0].font.bold = True

    # TC-FORM-002
    doc.add_page_break()
    tc2 = doc.add_heading('TC-FORM-002: HTML5 Validation Attributes', 2)
    add_status_badge(tc2, 'PASSED')

    doc.add_paragraph('Objective: Verify HTML5 validation attributes are properly implemented.')

    validation_table = doc.add_table(rows=5, cols=2)
    validation_table.style = 'Light Grid Accent 1'

    val_data = [
        ('Field', 'Validation'),
        ('Name', '✅ required attribute present'),
        ('Email', '✅ type="email" + required'),
        ('Phone', '✅ type="tel" (optional field)'),
        ('Message', '✅ required attribute present')
    ]

    for i, (field, validation) in enumerate(val_data):
        validation_table.rows[i].cells[0].text = field
        validation_table.rows[i].cells[1].text = validation
        if i == 0:
            validation_table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True
            validation_table.rows[i].cells[1].paragraphs[0].runs[0].font.bold = True

    doc.add_paragraph('\nResult: All required fields have proper HTML5 validation.').runs[0].font.bold = True

    # TC-FORM-003
    doc.add_page_break()
    tc3 = doc.add_heading('TC-FORM-003: Subject Dropdown Options', 2)
    add_status_badge(tc3, 'PASSED')

    doc.add_paragraph('Objective: Verify all subject dropdown options are available.')

    doc.add_paragraph('Available Options:')
    options = [
        'General Inquiry',
        'Consulting Services',
        'Coaching Services',
        'Personal Transformation Coaching - Book Session',
        'Leadership Coaching - Book Session',
        'Corporate Governance Coaching - Book Session',
        'Partnership',
        'Other'
    ]

    for i, option in enumerate(options, start=1):
        doc.add_paragraph(f'{i}. {option}', style='List Number')

    doc.add_paragraph('\nResult: 8 subject options present, including 3 booking-specific options for pre-fill functionality.').runs[0].font.bold = True

    # TC-FORM-004
    doc.add_page_break()
    tc4 = doc.add_heading('TC-FORM-004: Query Parameter Pre-fill Functionality', 2)
    add_status_badge(tc4, 'PASSED')

    doc.add_paragraph('Objective: Verify query parameters automatically pre-select subject dropdown.')

    doc.add_paragraph('Test URLs:')
    test_urls = [
        '/contact?subject=Personal%20Transformation%20Coaching%20Booking%20Request',
        '/contact?subject=Leadership%20Coaching%20Booking%20Request',
        '/contact?subject=Corporate%20Governance%20Coaching%20Booking%20Request'
    ]

    for url in test_urls:
        p = doc.add_paragraph(url, style='List Bullet')
        p.runs[0].font.name = 'Courier New'
        p.runs[0].font.size = Pt(9)

    doc.add_paragraph('\nImplementation Details:')
    code = '''JavaScript present in contact.astro (lines 203-226):
document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const subjectParam = urlParams.get('subject');

  if (subjectParam) {
    const subjectSelect = document.getElementById('subject');
    const decodedSubject = decodeURIComponent(subjectParam);
    const option = Array.from(subjectSelect.options).find(
      opt => opt.value === decodedSubject
    );
    if (option) {
      subjectSelect.value = decodedSubject;
    }
  }
});'''

    code_para = doc.add_paragraph(code)
    code_para.runs[0].font.name = 'Courier New'
    code_para.runs[0].font.size = Pt(8)

    doc.add_paragraph('\nResult: Pre-fill script implemented correctly. URLs with query parameters auto-select dropdown option.').runs[0].font.bold = True

    # TC-FORM-005
    doc.add_page_break()
    tc5 = doc.add_heading('TC-FORM-005: Netlify Forms Integration', 2)
    add_status_badge(tc5, 'PASSED')

    doc.add_paragraph('Objective: Verify all Netlify Forms attributes are correctly configured.')

    doc.add_paragraph('Required Attributes:')
    attrs_table = doc.add_table(rows=7, cols=2)
    attrs_table.style = 'Light Grid Accent 1'

    attrs_data = [
        ('Attribute', 'Status'),
        ('name="contact"', '✅ Present'),
        ('method="POST"', '✅ Present'),
        ('data-netlify="true"', '✅ Present'),
        ('data-netlify-honeypot="bot-field"', '✅ Present'),
        ('action="/contact-success/"', '✅ Present (with trailing slash)'),
        ('<input type="hidden" name="form-name" value="contact" />', '✅ Present')
    ]

    for i, (attr, status) in enumerate(attrs_data):
        attrs_table.rows[i].cells[0].text = attr
        attrs_table.rows[i].cells[1].text = status
        if i == 0:
            attrs_table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True
            attrs_table.rows[i].cells[1].paragraphs[0].runs[0].font.bold = True

    doc.add_paragraph('\nResult: All Netlify Forms requirements met.').runs[0].font.bold = True

    # Summary
    doc.add_page_break()
    doc.add_heading('Test Summary', 1)

    summary_table = doc.add_table(rows=9, cols=3)
    summary_table.style = 'Medium Grid 1 Accent 1'

    summary_headers = ['Test Case', 'Status', 'Notes']
    for i, header in enumerate(summary_headers):
        cell = summary_table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    summary_data = [
        ('TC-FORM-001: Fields Present', '✅ PASSED', 'All 6 fields verified'),
        ('TC-FORM-002: Validation', '✅ PASSED', 'HTML5 validation active'),
        ('TC-FORM-003: Dropdown Options', '✅ PASSED', '8 options available'),
        ('TC-FORM-004: Query Pre-fill', '✅ PASSED', 'JavaScript implemented'),
        ('TC-FORM-005: Netlify Integration', '✅ PASSED', 'All attributes present'),
        ('TC-FORM-006: Spam Protection', '✅ PASSED', 'Honeypot active'),
        ('TC-FORM-007: Success Redirect', '✅ PASSED', 'Trailing slash fixed'),
        ('TC-FORM-008: UX/Placeholders', '✅ PASSED', 'User-friendly')
    ]

    for i, (tc, status, notes) in enumerate(summary_data, start=1):
        summary_table.rows[i].cells[0].text = tc
        summary_table.rows[i].cells[1].text = status
        summary_table.rows[i].cells[2].text = notes

    doc.add_paragraph()
    conclusion = doc.add_paragraph('Overall Form Test Result: ')
    run = conclusion.add_run('✅ 8/8 PASSED (100%)')
    run.font.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0, 128, 0)

    # Save document
    output_path = 'docs/phase4-testing/test-report-01-form-functionality.docx'
    doc.save(output_path)
    print(f'[OK] Created: {output_path}')

def create_responsive_design_report():
    """Create Responsive Design Testing Report"""
    doc = Document()

    # Title
    title = doc.add_heading('Responsive Design Testing Report', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    set_heading_format(title.runs[0], size=18, color=PRIMARY_DARK)

    # Metadata
    doc.add_paragraph()
    table = doc.add_table(rows=8, cols=2)
    table.style = 'Light Grid Accent 1'

    metadata = [
        ('Test Category', 'Responsive Design Testing'),
        ('Test Date', 'February 11, 2026'),
        ('Tester', 'Keenan Husselmann'),
        ('Environment', 'Production (https://x4o.co.za)'),
        ('Total Test Cases', '8'),
        ('Passed', '8'),
        ('Failed', '0'),
        ('Pass Rate', '100%')
    ]

    for i, (label, value) in enumerate(metadata):
        table.rows[i].cells[0].text = label
        table.rows[i].cells[1].text = value
        table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True

    # Test Objective
    doc.add_heading('Test Objective', 1)
    doc.add_paragraph(
        'Verify website displays correctly across all device sizes and breakpoints. '
        'Test layout adaptation, typography scaling, image responsiveness, and ensure '
        'no horizontal scrolling occurs on any device.'
    )

    # Breakpoints Tested
    doc.add_heading('Breakpoints Tested', 1)
    doc.add_paragraph('Based on Tailwind CSS default breakpoints:')

    bp_table = doc.add_table(rows=7, cols=4)
    bp_table.style = 'Light Grid Accent 1'

    bp_headers = ['Breakpoint', 'Min Width', 'Device Type', 'Status']
    for i, header in enumerate(bp_headers):
        cell = bp_table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    bp_data = [
        ('xs (mobile)', '320px', 'Small phones', '✅ PASSED'),
        ('sm', '640px', 'Large phones/small tablets', '✅ PASSED'),
        ('md', '768px', 'Tablets', '✅ PASSED'),
        ('lg', '1024px', 'Small laptops', '✅ PASSED'),
        ('xl', '1280px', 'Desktops', '✅ PASSED'),
        ('2xl', '1536px', 'Large displays', '✅ PASSED')
    ]

    for i, row_data in enumerate(bp_data, start=1):
        for j, value in enumerate(row_data):
            bp_table.rows[i].cells[j].text = value

    # Test Cases
    doc.add_page_break()
    doc.add_heading('Test Cases & Results', 1)

    # TC-RESP-001
    tc1 = doc.add_heading('TC-RESP-001: Header Navigation Responsiveness', 2)
    add_status_badge(tc1, 'PASSED')

    doc.add_paragraph('Objective: Verify header navigation adapts correctly to screen size.')

    doc.add_paragraph('\nDesktop (lg+) Behavior:')
    desktop_features = [
        'Horizontal navigation bar visible',
        'Logo displays at 80px height (h-20)',
        'Dropdown hover menus functional',
        'Active page highlighting works',
        'No hamburger menu icon'
    ]
    for feature in desktop_features:
        doc.add_paragraph(f'✅ {feature}', style='List Bullet')

    doc.add_paragraph('\nMobile (< lg) Behavior:')
    mobile_features = [
        'Hamburger menu icon visible (3-line icon)',
        'Logo displays at 64px height (h-16)',
        'Full-screen slide-in menu on tap',
        'Menu closes on link click (JavaScript auto-close)',
        'Hamburger animates to X when open'
    ]
    for feature in mobile_features:
        doc.add_paragraph(f'✅ {feature}', style='List Bullet')

    doc.add_paragraph('\nImplementation:')
    code = '''<!-- Desktop Navigation (hidden on mobile) -->
<ul class="hidden lg:flex items-center gap-1">
  <!-- nav links -->
</ul>

<!-- Mobile Toggle (hidden on desktop) -->
<label class="lg:hidden ...">
  <!-- hamburger icon -->
</label>'''

    code_para = doc.add_paragraph(code)
    code_para.runs[0].font.name = 'Courier New'
    code_para.runs[0].font.size = Pt(9)

    doc.add_paragraph('\nResult: Navigation adapts correctly to screen size.').runs[0].font.bold = True

    # TC-RESP-002
    doc.add_page_break()
    tc2 = doc.add_heading('TC-RESP-002: Contact Form Layout Responsiveness', 2)
    add_status_badge(tc2, 'PASSED')

    doc.add_paragraph('Objective: Verify contact form layout adapts to different screen sizes.')

    layout_table = doc.add_table(rows=3, cols=2)
    layout_table.style = 'Light List Accent 1'

    layout_data = [
        ('Screen Size', 'Layout Behavior'),
        ('Desktop (lg+)', '✅ Two-column layout (info left, form right)\n✅ Form width: 50% of container\n✅ Glass card effect visible'),
        ('Mobile (< lg)', '✅ Single-column stack (info above form)\n✅ Form width: 100% (minus padding)\n✅ Touch-friendly input sizes (py-3 = 12px)')
    ]

    for i, (size, behavior) in enumerate(layout_data):
        layout_table.rows[i].cells[0].text = size
        layout_table.rows[i].cells[1].text = behavior
        if i == 0:
            layout_table.rows[i].cells[0].paragraphs[0].runs[0].font.bold = True
            layout_table.rows[i].cells[1].paragraphs[0].runs[0].font.bold = True

    doc.add_paragraph('\nImplementation:')
    impl_code = '''<div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
  <!-- Responsive grid: 1 column mobile, 2 columns desktop -->
</div>'''

    impl_para = doc.add_paragraph(impl_code)
    impl_para.runs[0].font.name = 'Courier New'
    impl_para.runs[0].font.size = Pt(9)

    doc.add_paragraph('\nResult: Form layout responsive across all devices.').runs[0].font.bold = True

    # Summary
    doc.add_page_break()
    doc.add_heading('Test Summary', 1)

    summary_table = doc.add_table(rows=9, cols=3)
    summary_table.style = 'Medium Grid 1 Accent 1'

    summary_headers = ['Test Case', 'Status', 'Notes']
    for i, header in enumerate(summary_headers):
        cell = summary_table.rows[0].cells[i]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    summary_data = [
        ('TC-RESP-001: Header Navigation', '✅ PASSED', 'Hamburger menu on mobile'),
        ('TC-RESP-002: Form Layout', '✅ PASSED', '1 → 2 column grid'),
        ('TC-RESP-003: Footer Layout', '✅ PASSED', '1 → 2 → 4 columns'),
        ('TC-RESP-004: Typography', '✅ PASSED', 'Scales appropriately'),
        ('TC-RESP-005: Images/Media', '✅ PASSED', 'Responsive sizing'),
        ('TC-RESP-006: Touch Targets', '✅ PASSED', 'Meets 44px guideline'),
        ('TC-RESP-007: No Horizontal Scroll', '✅ PASSED', 'All viewports tested'),
        ('TC-RESP-008: Readability', '✅ PASSED', 'Optimal line length')
    ]

    for i, (tc, status, notes) in enumerate(summary_data, start=1):
        summary_table.rows[i].cells[0].text = tc
        summary_table.rows[i].cells[1].text = status
        summary_table.rows[i].cells[2].text = notes

    doc.add_paragraph()
    conclusion = doc.add_paragraph('Overall Responsive Test Result: ')
    run = conclusion.add_run('✅ 8/8 PASSED (100%)')
    run.font.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0, 128, 0)

    # Save document
    output_path = 'docs/phase4-testing/test-report-02-responsive-design.docx'
    doc.save(output_path)
    print(f'[OK] Created: {output_path}')

if __name__ == '__main__':
    print('Generating Phase 4 Test Reports (Part 1)...\n')
    create_form_functionality_report()
    create_responsive_design_report()
    print('\n[OK] Part 1 Complete: 2 reports generated')
