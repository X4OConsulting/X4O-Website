"""
Phase 3 Individual Task Documentation Generator - Part 4 (Final)
Utility Pages and Docker
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_heading(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    if level == 1:
        heading.runs[0].font.color.rgb = RGBColor(23, 64, 105)
        heading.runs[0].font.size = Pt(24)
    elif level == 2:
        heading.runs[0].font.color.rgb = RGBColor(23, 64, 105)
        heading.runs[0].font.size = Pt(18)
    return heading

def add_screenshot_section(doc, title, description):
    doc.add_heading(f"Screenshot: {title}", level=2)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[INSERT SCREENSHOT HERE]")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(151, 192, 232)
    p = doc.add_paragraph()
    p.add_run("Screenshot Description: ").bold = True
    p.add_run(description)
    p.space_after = Pt(12)

def add_table(doc, data, has_header=True):
    table = doc.add_table(rows=len(data), cols=len(data[0]))
    table.style = 'Light Grid Accent 1'
    for i, row_data in enumerate(data):
        row = table.rows[i]
        for j, cell_text in enumerate(row_data):
            cell = row.cells[j]
            cell.text = str(cell_text)
            if has_header and i == 0:
                cell.paragraphs[0].runs[0].font.bold = True
                cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(23, 64, 105)
    return table

def add_technical_definitions(doc, definitions):
    doc.add_page_break()
    add_heading(doc, "Technical Jargon Definitions", level=1)
    for term, definition in definitions.items():
        p = doc.add_paragraph()
        p.add_run(f"{term}: ").bold = True
        p.add_run(definition)

# TASK 7: Build Contact Success Page
def create_task_contact_success():
    doc = Document()

    add_heading(doc, 'Task: Build Contact Success Page', level=1)
    add_heading(doc, 'contact-success.astro', level=2)

    meta_data = [
        ['Task ID', 'TASK-017 (Development Phase)'],
        ['File', 'src/pages/contact-success.astro'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~80 lines']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'The contact success page confirms successful form submission with a friendly thank you message, '
        'response time expectations, and navigation options back to the site. Uses glassmorphic design '
        'matching the site aesthetic.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Page Elements', level=2)
    doc.add_paragraph(
        '1. Success Icon\n'
        '   • Large checkmark or success symbol\n'
        '   • Gradient color (primary blue)\n'
        '   • Centered on page\n\n'
        '2. Thank You Message\n'
        '   • Heading: "Thank You!"\n'
        '   • Subheading: "Your message has been received"\n'
        '   • Body text: Response time expectations\n\n'
        '3. Information Panel\n'
        '   • Glassmorphic card container\n'
        '   • What happens next details\n'
        '   • Estimated response time (24-48 hours)\n\n'
        '4. Navigation Options\n'
        '   • "Return to Homepage" button (btn-primary)\n'
        '   • Quick links to Services, About pages\n\n'
        '5. Contact Information\n'
        '   • Alternative contact methods\n'
        '   • Email: info@x4o.co.za\n'
        '   • Phone number (if available)',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Success Page Full View',
        'Desktop screenshot showing centered success message with: large green checkmark icon at top, '
        '"Thank You!" heading in large text, confirmation message, glass-card container with details, '
        'blue "Return to Homepage" button, and bg-mesh background pattern.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile Success View',
        'Mobile screenshot showing success page with responsive layout: stacked elements, readable text size, '
        'full-width button, proper spacing between elements.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'User Experience Flow', level=2)
    doc.add_paragraph(
        '1. User submits contact form\n'
        '   ↓\n'
        '2. Netlify processes submission\n'
        '   ↓\n'
        '3. Browser redirects to /contact-success/\n'
        '   ↓\n'
        '4. Success page loads with confirmation\n'
        '   ↓\n'
        '5. User reads confirmation message\n'
        '   ↓\n'
        '6. User either:\n'
        '   • Clicks "Return to Homepage" button, OR\n'
        '   • Uses browser back button, OR\n'
        '   • Navigates via header menu',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ User Feedback: Clear confirmation of successful submission\n'
        '✅ Expectations: Communicates response timeframe\n'
        '✅ Navigation Recovery: Easy return to main site\n'
        '✅ Brand Consistency: Matches site design aesthetic\n'
        '✅ Accessibility: Clear messaging, semantic structure\n'
        '✅ Mobile Optimization: Responsive layout\n'
        '✅ Performance: Static page, fast load',
        style='No Spacing'
    )

    definitions = {
        'Success Page': 'Confirmation page shown after successful form submission or action completion',
        'User Feedback': 'Visual or textual confirmation that action was completed successfully',
        'Response Time': 'Expected duration before user receives reply to inquiry',
        'Navigation Recovery': 'Providing clear paths for user to continue browsing after completing action',
        'Glassmorphism': 'Modern UI design featuring frosted-glass visual effects'
    }
    add_technical_definitions(doc, definitions)

    return doc

# TASK 8: Build Partners Page
def create_task_partners_page():
    doc = Document()

    add_heading(doc, 'Task: Build Partners Page with Logos', level=1)
    add_heading(doc, 'partners.astro', level=2)

    meta_data = [
        ['Task ID', 'TASK-018 (Development Phase)'],
        ['File', 'src/pages/partners.astro'],
        ['Partner Logos', '3 organizations'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~100 lines']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'The partners page showcases strategic partnerships with organizations in the consulting and development sectors. '
        'Features partner logos with glassmorphic card design for professional presentation and mobile responsiveness.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Featured Partners', level=2)

    partners_table = [
        ['Partner', 'Logo File', 'Focus Area'],
        ['EdMeCa', 'EdMeCa_logo.png', 'Education, Media, and Capacity Development'],
        ['IDC', 'idc-logo.png', 'Industrial Development Corporation - Industrial financing'],
        ['Mzilikazi', 'mzilikazi_logo.png', 'Mzilikazi Development Association - Community development']
    ]
    add_table(doc, partners_table)

    doc.add_paragraph()

    add_heading(doc, 'Page Structure', level=2)
    doc.add_paragraph(
        '1. Hero Banner\n'
        '   • Header image: x4o_banner.jpg\n'
        '   • Page title: "Our Partners"\n\n'
        '2. Introduction Section\n'
        '   • Partnership philosophy statement\n'
        '   • Collaboration value proposition\n\n'
        '3. Partner Logo Grid\n'
        '   • 3-column grid (desktop)\n'
        '   • 2-column grid (tablet)\n'
        '   • 1-column grid (mobile)\n'
        '   • Each partner in glass-card container\n\n'
        '4. Logo Card Structure\n'
        '   • Logo image (centered, max-width constraint)\n'
        '   • Partner name below logo\n'
        '   • Optional: Brief description\n'
        '   • Glassmorphic background\n'
        '   • Hover effect (subtle lift)',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Partners Page Desktop View',
        'Full desktop screenshot showing: hero banner with x4o_banner.jpg, "Our Partners" heading, '
        'introduction paragraph, and 3 partner logo cards in horizontal row. Each card shows centered logo, '
        'partner name, glass-card styling with subtle border and shadow.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Single Partner Logo Card',
        'Close-up of EdMeCa partner card showing: glass-card background with backdrop blur, EdMeCa logo '
        'centered and properly sized, partner name "EdMeCa" below logo in primary-dark color, subtle '
        'padding around content, soft shadow.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile Stacked Partners',
        'Mobile screenshot showing partner cards stacked vertically in single column, each card full-width '
        'with consistent spacing, logos properly sized for mobile viewing.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Logo Specifications', level=2)

    logo_specs = [
        ['Specification', 'Value'],
        ['Format', 'PNG with transparency'],
        ['Max Width', '200-300px (constrained in CSS)'],
        ['Aspect Ratio', 'Preserved (no stretching)'],
        ['Alt Text', 'Partner organization name + "logo"'],
        ['File Location', 'public/images/']
    ]
    add_table(doc, logo_specs)

    doc.add_paragraph()

    add_heading(doc, 'Responsive Breakpoints', level=2)

    breakpoints_table = [
        ['Screen Size', 'Layout', 'Grid Columns'],
        ['Mobile (< 640px)', 'Stacked', '1 column'],
        ['Tablet (640px - 1023px)', 'Side-by-side pairs', '2 columns'],
        ['Desktop (≥ 1024px)', 'Horizontal row', '3 columns']
    ]
    add_table(doc, breakpoints_table)

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Image Optimization: PNG format with transparency\n'
        '✅ Accessibility: Alt text on all logos\n'
        '✅ Responsive Design: Grid adapts to screen size\n'
        '✅ Brand Consistency: Matching design aesthetic\n'
        '✅ Performance: Optimized image sizes\n'
        '✅ Semantic HTML: Proper use of figure elements\n'
        '✅ Maintainability: Easy to add new partners',
        style='No Spacing'
    )

    definitions = {
        'Partner Showcase': 'Page displaying logos and information about business partnerships',
        'Grid Layout': 'CSS layout arranging content in structured rows and columns',
        'Alt Text': 'Alternative text description for images used by screen readers',
        'PNG': 'Portable Network Graphics image format supporting transparency',
        'Aspect Ratio': 'Proportional relationship between image width and height',
        'Figure Element': 'HTML semantic element for containing images with optional captions',
        'Responsive Grid': 'Grid layout that changes column count based on screen size'
    }
    add_technical_definitions(doc, definitions)

    return doc

# Continue with remaining tasks in next message due to length...
print("Creating Part 4: Utility Pages and Docker...")
print("=" * 60)

import os
os.makedirs('docs/phase3-tasks', exist_ok=True)

task7_doc = create_task_contact_success()
task7_doc.save('docs/phase3-tasks/task-017-build-contact-success.docx')
print("Created: task-017-build-contact-success.docx")

task8_doc = create_task_partners_page()
task8_doc.save('docs/phase3-tasks/task-018-build-partners-page.docx')
print("Created: task-018-build-partners-page.docx")

print("=" * 60)
print("Part 4a complete. Creating final tasks...")
