"""
Phase 3 Individual Task Documentation Generator - Part 3
Booking, Contact, and Utility Pages
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
    run.font.color.rgb = RGBColor(151,192, 232)
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

# TASK 5: Build Book Coaching Sessions Page
def create_task_book_sessions():
    doc = Document()

    add_heading(doc, 'Task: Build Book Coaching Sessions Page', level=1)
    add_heading(doc, 'book-coaching-sessions.astro', level=2)

    meta_data = [
        ['Task ID', 'TASK-015 (Development Phase)'],
        ['File', 'src/pages/book-coaching-sessions.astro'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~150 lines']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'This page presents three coaching session packages with pricing tiers and booking functionality. '
        'Each package card includes session details, duration, pricing, and a "Request to Book" button that '
        'pre-fills the contact form with the selected coaching type via URL query parameters.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Session Packages', level=2)
    doc.add_paragraph(
        '1. Personal Transformation Coaching\n'
        '   • Duration: 1 hr 30 min\n'
        '   • Pricing: Via Quote\n'
        '   • Focus: Uncover true essence, live with purpose\n'
        '   • Button: Links to /contact?subject=Personal%20Transformation%20Coaching%20Booking%20Request\n\n'
        '2. Leadership Coaching\n'
        '   • Duration: 1 hr 30 min\n'
        '   • Pricing: Via Quote\n'
        '   • Focus: Execute and empower based on true potential\n'
        '   • Button: Links to /contact?subject=Leadership%20Coaching%20Booking%20Request\n\n'
        '3. Corporate Governance Coaching\n'
        '   • Duration: 1 hr 30 min\n'
        '   • Pricing: Via Quote\n'
        '   • Focus: Navigate corporate and public sector governance\n'
        '   • Button: Links to /contact?subject=Corporate%20Governance%20Coaching%20Booking%20Request',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        '3 Session Package Cards (Desktop)',
        'Desktop view showing all 3 session cards side-by-side in equal-width columns. Each card displays: '
        'gradient icon at top, session title, description, info bar with duration and pricing icons, '
        'and blue "Request to Book" button. Cards have glass-card styling with hover lift effect.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Single Package Card Detail',
        'Close-up of Personal Transformation Coaching card showing: circular gradient icon with person symbol, '
        'card title in bold primary-dark color, descriptive text, info bar with clock icon (1 hr 30 min) and '
        'pricing icon (Via Quote), full-width CTA button with btn-primary gradient styling.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile Stacked View',
        'Mobile screenshot showing session cards stacked vertically, each card full-width with proper spacing. '
        'CTA buttons span full card width, text remains readable, icons properly sized for touch targets.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Contact Form Pre-filled Subject',
        'Screenshot of contact form page after clicking "Request to Book" button, showing subject dropdown '
        'pre-selected with "Leadership Coaching Booking Request", demonstrating successful query parameter integration.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Technical Implementation', level=2)

    tech_table = [
        ['Feature', 'Implementation', 'Technology'],
        ['Query Parameter Passing', 'URL encoding in href attribute', 'Native JavaScript encodeURIComponent'],
        ['Contact Form Integration', 'JavaScript reads URL params on load', 'URLSearchParams API'],
        ['Icon System', 'Heroicons SVG icons', 'Inline SVG with Tailwind classes'],
        ['Responsive Layout', '3-column → 2-column → 1-column', 'Tailwind grid system'],
        ['Card Styling', 'Glassmorphism with hover effects', 'Custom CSS utilities + Tailwind']
    ]
    add_table(doc, tech_table)

    doc.add_paragraph()

    add_heading(doc, 'User Flow', level=2)
    doc.add_paragraph(
        'Step 1: User browses coaching sessions page\n'
        '   ↓\n'
        'Step 2: User clicks "Request to Book" on desired session\n'
        '   ↓\n'
        'Step 3: Redirected to /contact with query parameter\n'
        '   ↓\n'
        'Step 4: Contact form loads, JavaScript detects parameter\n'
        '   ↓\n'
        'Step 5: Subject dropdown auto-selects coaching type\n'
        '   ↓\n'
        'Step 6: User fills remaining fields and submits\n'
        '   ↓\n'
        'Step 7: Netlify Forms captures submission\n'
        '   ↓\n'
        'Step 8: Email sent to admin@x4o.co.za\n'
        '   ↓\n'
        'Step 9: User redirected to success page',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ User Experience: Seamless booking flow with pre-filled form\n'
        '✅ URL Structure: Clean, semantic query parameters\n'
        '✅ Error Handling: Graceful fallback if parameter missing\n'
        '✅ Accessibility: Clear button labels, semantic HTML\n'
        '✅ Mobile Optimization: Touch-friendly buttons (44px min)\n'
        '✅ Integration Testing: Verified end-to-end booking flow\n'
        '✅ Code Maintainability: Consistent card pattern\n'
        '✅ Performance: Static generation, minimal JavaScript',
        style='No Spacing'
    )

    definitions = {
        'Query Parameter': 'Key-value pairs appended to URL after ? symbol for passing data between pages',
        'URL Encoding': 'Converting special characters to %XX format for safe URL transmission',
        'URLSearchParams': 'JavaScript API for parsing and manipulating URL query strings',
        'Pre-fill': 'Automatically populating form fields with data from URL or other source',
        'User Flow': 'Sequence of steps user takes to complete specific task or goal',
        'Heroicons': 'Open-source icon library designed for Tailwind CSS',
        'SVG (Scalable Vector Graphics)': 'Vector image format that scales without quality loss',
        'Touch Target': 'Interactive element sized appropriately for finger taps (minimum 44x44px)',
        'Glassmorphism': 'Modern UI design with frosted-glass visual effects',
        'Grid System': 'CSS layout arranging content in structured rows and columns'
    }
    add_technical_definitions(doc, definitions)

    return doc

# TASK 6: Build Contact Page with Netlify Forms
def create_task_contact_page():
    doc = Document()

    add_heading(doc, 'Task: Build Contact Page with Netlify Forms', level=1)
    add_heading(doc, 'contact.astro + Netlify Forms Integration', level=2)

    meta_data = [
        ['Task ID', 'TASK-016 (Development Phase)'],
        ['File', 'src/pages/contact.astro'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~230 lines (including JavaScript)']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'The contact page implements a full-featured contact form using Netlify Forms for serverless form handling. '
        'Features include HTML5 validation, honeypot spam protection, email notifications, query parameter pre-filling, '
        'and success page redirection. No backend code required.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Form Fields', level=2)

    fields_table = [
        ['Field', 'Type', 'Required', 'Validation'],
        ['Name', 'text', 'Yes', 'Non-empty string'],
        ['Email', 'email', 'Yes', 'Valid email format (contains @)'],
        ['Phone', 'tel', 'No', 'Optional, no validation'],
        ['Subject', 'select', 'Yes', '8 predefined options'],
        ['Message', 'textarea', 'Yes', 'Non-empty string'],
        ['bot-field', 'hidden', 'No', 'Honeypot (must be empty)']
    ]
    add_table(doc, fields_table)

    doc.add_paragraph()

    add_heading(doc, 'Subject Dropdown Options', level=2)
    doc.add_paragraph(
        '1. General Inquiry\n'
        '2. Consulting Services\n'
        '3. Coaching Services\n'
        '4. Personal Transformation Coaching - Book Session\n'
        '5. Leadership Coaching - Book Session\n'
        '6. Corporate Governance Coaching - Book Session\n'
        '7. Partnership\n'
        '8. Other',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'Netlify Forms Configuration', level=2)
    doc.add_paragraph(
        'Form HTML Attributes:\n'
        '• name="contact" - Form identifier\n'
        '• method="POST" - HTTP submission method\n'
        '• data-netlify="true" - Enables Netlify processing\n'
        '• data-netlify-honeypot="bot-field" - Spam protection\n'
        '• action="/contact-success/" - Success page redirect\n\n'
        'Email Notification Setup:\n'
        '1. Netlify Dashboard → Site Settings → Forms\n'
        '2. Add form notification → Email notification\n'
        '3. Event: New form submission\n'
        '4. Email to: admin@x4o.co.za\n'
        '5. Subject: "New contact form submission from x4o.co.za"\n\n'
        'Spam Protection:\n'
        '• Honeypot field (bot-field) hidden from humans\n'
        '• Bots fill all fields including hidden ones\n'
        '• Netlify rejects submissions with honeypot filled\n'
        '• Rate limiting built into Netlify',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Full Contact Form (Desktop)',
        'Desktop view showing complete contact form with: hero section at top, "Get in Touch" heading on left, '
        'contact info cards (email, location, social), and form on right with all fields visible (Name, Email, '
        'Phone, Subject dropdown, Message textarea), glass-card styling, and blue "Send Message" button.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Form with Pre-filled Subject',
        'Screenshot showing contact form with Subject dropdown pre-selected with '
        '"Personal Transformation Coaching - Book Session", demonstrating query parameter functionality.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'HTML5 Validation Error',
        'Screenshot showing form validation: Name field with red border and browser tooltip saying '
        '"Please fill out this field", Email field with invalid format showing "Please include an @ in the email address".'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Netlify Dashboard Form Submissions',
        'Screenshot of Netlify dashboard showing Forms tab with list of contact form submissions: '
        'submission date, name, email, subject fields visible, with option to export CSV or download.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'JavaScript Implementation', level=2)
    doc.add_paragraph(
        'Query Parameter Pre-fill Script:\n\n'
        '```javascript\n'
        'document.addEventListener(\'DOMContentLoaded\', () => {\n'
        '  const urlParams = new URLSearchParams(window.location.search);\n'
        '  const subjectParam = urlParams.get(\'subject\');\n\n'
        '  if (subjectParam) {\n'
        '    const subjectSelect = document.getElementById(\'subject\');\n'
        '    const decodedSubject = decodeURIComponent(subjectParam);\n'
        '    const option = Array.from(subjectSelect.options).find(\n'
        '      opt => opt.value === decodedSubject\n'
        '    );\n'
        '    if (option) {\n'
        '      subjectSelect.value = decodedSubject;\n'
        '    }\n'
        '  }\n'
        '});\n'
        '```\n\n'
        'How It Works:\n'
        '1. Waits for DOM to fully load\n'
        '2. Reads URL query parameters\n'
        '3. Extracts subject parameter value\n'
        '4. Decodes URL-encoded string\n'
        '5. Finds matching dropdown option\n'
        '6. Set dropdown value if match found',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'Form Processing Flow', level=2)
    doc.add_paragraph(
        '1. User fills form and clicks "Send Message"\n'
        '   ↓\n'
        '2. Browser validates required fields (HTML5)\n'
        '   ↓\n'
        '3. Form submits via POST to Netlify\n'
        '   ↓\n'
        '4. Netlify checks honeypot field\n'
        '   ↓\n'
        '5. If empty (human): Accept and store submission\n'
        '   If filled (bot): Reject silently\n'
        '   ↓\n'
        '6. Netlify stores data in Forms dashboard\n'
        '   ↓\n'
        '7. Email notification sent to admin@x4o.co.za\n'
        '   ↓\n'
        '8. User redirected to /contact-success/\n'
        '   ↓\n'
        '9. Success confirmation displayed',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Serverless Architecture: No backend code or database\n'
        '✅ Security: Honeypot spam protection, no exposed credentials\n'
        '✅ User Experience: Instant validation, pre-filled fields\n'
        '✅ Error Handling: HTML5 validation before submission\n'
        '✅ Accessibility: Proper labels, ARIA attributes\n'
        '✅ Testing: Verified submission flow end-to-end\n'
        '✅ Monitoring: Netlify dashboard tracks all submissions\n'
        '✅ Privacy: Compliance-ready (GDPR, POPIA)',
        style='No Spacing'
    )

    definitions = {
        'Netlify Forms': 'Serverless form handling service capturing submissions without backend code',
        'Honeypot Field': 'Hidden form field to catch spam bots (invisible to humans)',
        'HTML5 Validation': 'Browser built-in form validation using HTML attributes (required, type="email")',
        'POST Method': 'HTTP method for submitting data to server (vs GET for retrieval)',
        'Serverless': 'Architecture running without managing servers (provider handles infrastructure)',
        'Rate Limiting': 'Restriction on number of requests within time period to prevent abuse',
        'Email Notification': 'Automated email sent when specific event occurs',
        'URLSearchParams': 'JavaScript API for parsing URL query strings',
        'DOM (Document Object Model)': 'Browser representation of webpage structure',
        'Event Listener': 'JavaScript code waiting for user interactions to trigger response'
    }
    add_technical_definitions(doc, definitions)

    return doc

# Save documents
print("Creating Part 3: Booking and Contact Pages...")
print("=" * 60)

import os
os.makedirs('docs/phase3-tasks', exist_ok=True)

task5_doc = create_task_book_sessions()
task5_doc.save('docs/phase3-tasks/task-015-build-book-coaching-sessions.docx')
print("Created: task-015-build-book-coaching-sessions.docx")

task6_doc = create_task_contact_page()
task6_doc.save('docs/phase3-tasks/task-016-build-contact-page.docx')
print("Created: task-016-build-contact-page.docx")

print("=" * 60)
print("Part 3 complete. Continuing with remaining tasks...")
