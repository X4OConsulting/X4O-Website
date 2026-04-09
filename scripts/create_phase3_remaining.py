"""
Phase 3 Development Documentation Generator - Part 2
Creates remaining DOCX files for Phase 3 deliverables
"""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def add_page_break(doc):
    """Add a page break"""
    doc.add_page_break()

def add_heading(doc, text, level=1):
    """Add a styled heading"""
    heading = doc.add_heading(text, level=level)
    if level == 1:
        heading.runs[0].font.color.rgb = RGBColor(23, 64, 105)  # Primary dark
        heading.runs[0].font.size = Pt(24)
    elif level == 2:
        heading.runs[0].font.color.rgb = RGBColor(23, 64, 105)
        heading.runs[0].font.size = Pt(18)
    return heading

def add_screenshot_section(doc, title, description):
    """Add a screenshot placeholder section"""
    doc.add_heading(f"Screenshot: {title}", level=2)

    # Add placeholder box
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[INSERT SCREENSHOT HERE]")
    run.bold = True
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(151, 192, 232)  # Primary color

    # Add description
    p = doc.add_paragraph()
    p.add_run("Screenshot Description: ").bold = True
    p.add_run(description)
    p.space_after = Pt(12)

def add_table(doc, data, has_header=True):
    """Add a formatted table"""
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
    """Add technical jargon definitions section"""
    doc.add_page_break()
    add_heading(doc, "Technical Jargon Definitions", level=1)

    for term, definition in definitions.items():
        p = doc.add_paragraph()
        p.add_run(f"{term}: ").bold = True
        p.add_run(definition)

# ============================================================
# DOCUMENT 3: Service Pages Development
# ============================================================
def create_service_pages_doc():
    doc = Document()

    # Title
    add_heading(doc, 'Service Pages Development', level=1)
    add_heading(doc, '3 Service Pages - Consulting, Coaching, Booking', level=2)

    # Metadata
    meta_data = [
        ['Files', '3 pages (consulting-and-advisory-services.astro, coaching-services.astro, book-coaching-sessions.astro)'],
        ['Purpose', 'Detailed service information and booking options'],
        ['Status', '✅ Complete'],
        ['Total Lines', '~450 lines combined']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Overview
    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'Three service pages provide comprehensive information about X4O\'s offerings: Consulting & Advisory Services, '
        'Coaching Services, and Book Coaching Sessions. Each page uses consistent design patterns with glassmorphic '
        'cards and clear call-to-action elements.'
    )

    # Pages Breakdown
    add_heading(doc, 'Page 1: Consulting & Advisory Services', level=2)
    doc.add_paragraph(
        'File: consulting-and-advisory-services.astro\n\n'
        'Services Showcased:\n'
        '1. Project Management\n'
        '   • Full project lifecycle management\n'
        '   • Risk assessment and mitigation\n'
        '   • Stakeholder coordination\n\n'
        '2. Advisory Services\n'
        '   • Strategic business planning\n'
        '   • Process optimization\n'
        '   • Compliance consulting\n\n'
        '3. Renewable Energy Solutions\n'
        '   • Solar energy implementation\n'
        '   • Energy efficiency audits\n'
        '   • Sustainability consulting',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'Page 2: Coaching Services', level=2)
    doc.add_paragraph(
        'File: coaching-services.astro\n\n'
        'Services Showcased:\n'
        '1. Professional Development Coaching\n'
        '   • Career advancement strategies\n'
        '   • Leadership skill building\n'
        '   • Performance improvement\n\n'
        '2. Business Growth Coaching\n'
        '   • Strategic planning facilitation\n'
        '   • Market expansion guidance\n'
        '   • Operational efficiency\n\n'
        '3. Project Management Coaching\n'
        '   • PM certification preparation\n'
        '   • Methodology implementation\n'
        '   • Team leadership training\n\n'
        '4. Executive Coaching\n'
        '   • C-suite leadership development\n'
        '   • Decision-making frameworks\n'
        '   • Organizational transformation',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'Page 3: Book Coaching Sessions', level=2)
    doc.add_paragraph(
        'File: book-coaching-sessions.astro\n\n'
        'Session Packages:\n'
        '1. Single Session (1 hour)\n'
        '   • One-time consultation\n'
        '   • Specific problem solving\n'
        '   • Quick guidance\n\n'
        '2. Starter Package (3 sessions)\n'
        '   • Three 1-hour sessions\n'
        '   • Goal setting + implementation\n'
        '   • Follow-up support\n\n'
        '3. Professional Package (6 sessions)\n'
        '   • Six 1-hour sessions\n'
        '   • Comprehensive development plan\n'
        '   • Ongoing accountability',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Screenshots
    add_screenshot_section(
        doc,
        'Consulting Services Page (Desktop)',
        'Full desktop view showing the consulting page header banner (x4o_banner.jpg), '
        'page title "Consulting & Advisory Services", introduction paragraph, and 3 service cards '
        'displayed in a grid. Each card should show: glass effect, service icon, title, '
        'bullet point list of offerings, and gradient background.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Coaching Services - 4 Cards Grid',
        'Desktop view of the coaching services page showing all 4 coaching type cards in a 2x2 grid. '
        'Cards should display: Professional Development Coaching, Business Growth Coaching, '
        'Project Management Coaching, and Executive Coaching. Each with glass-card styling, '
        'descriptive text, and visual separationbetween cards.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Book Sessions Page - Package Cards',
        'Screenshot showing the three booking package cards side-by-side (desktop): Single Session, '
        'Starter Package, and Professional Package. Each card should show: package name in bold, '
        'session count, duration details, key features as bullet points, and "Contact Us to Book" button '
        'at the bottom with btn-primary styling.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile View - Coaching Services Stacked',
        'Mobile screenshot showing coaching service cards stacked vertically in single column. '
        'Should show hamburger menu at top, page title, and at least 2 coaching cards stacked '
        'with full-width layout and proper spacing between cards.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Design Patterns
    add_heading(doc, 'Design Patterns Used', level=2)
    patterns_data = [
        ['Pattern', 'Usage', 'CSS Class'],
        ['Glass Cards', 'Service/package containers', '.glass-card'],
        ['Hero Banner', 'Page header image', 'x4o_banner.jpg'],
        ['Grid Layout', '2-3 column service display', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3'],
        ['CTA Buttons', 'Booking/contact actions', '.btn-primary'],
        ['Icon Integration', 'Visual service indicators', 'Emoji/icons in headings']
    ]
    add_table(doc, patterns_data)

    doc.add_paragraph()

    # SDLC Best Practices
    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Content Consistency: All service pages follow same structure\n'
        '✅ Reusable Components: Layout, Header, Footer used across all pages\n'
        '✅ Responsive Design: Mobile-first breakpoints applied\n'
        '✅ SEO Optimization: Unique titles and descriptions per page\n'
        '✅ User Flow: Clear navigation from services → booking\n'
        '✅ Accessibility: Semantic headings (h1 → h2 → h3)\n'
        '✅ Performance: Static generation, no client-side JavaScript\n'
        '✅ Maintainability: Consistent code structure across pages',
        style='No Spacing'
    )

    # Technical Definitions
    definitions = {
        'Grid Layout': 'CSS layout system that divides page into rows and columns for responsive multi-column designs',
        'Glass Card': 'Container component with glassmorphism effect (blur, transparency, subtle border)',
        'CTA Button': 'Call-to-Action button designed to prompt user interaction (booking, contact, etc.)',
        'Responsive Breakpoints': 'Screen width thresholds where layout changes (mobile → tablet → desktop)',
        'Hero Banner': 'Large prominent image at the top of a page used for visual impact',
        'Semantic HTML': 'Using HTML elements that clearly describe their meaning (header, nav, main, article)',
        'Static Generation': 'Pre-rendering pages at build time for fast delivery without server processing',
        'Component Reusability': 'Using same code components across multiple pages to avoid duplication'
    }
    add_technical_definitions(doc, definitions)

    return doc

# ============================================================
# DOCUMENT 4: Contact System Development
# ============================================================
def create_contact_system_doc():
    doc = Document()

    # Title
    add_heading(doc, 'Contact System Integration', level=1)
    add_heading(doc, 'Netlify Forms + Email Notifications', level=2)

    # Metadata
    meta_data = [
        ['Files', 'contact.astro, contact-success.astro'],
        ['Integration', 'Netlify Forms (built-in service)'],
        ['Spam Protection', 'Honeypot field (bot-field)'],
        ['Email Delivery', 'admin@x4o.co.za'],
        ['Status', '✅ Complete'],
        ['Monthly Limit', '100 submissions/month (free tier)']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Overview
    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'The contact system leverages Netlify Forms for serverless form handling without backend infrastructure. '
        'Form submissions are captured, spam-filtered, and delivered via email to the admin inbox. '
        'Users receive instant confirmation on a success page after submission.'
    )

    # Contact Form Structure
    add_heading(doc, 'Contact Form Fields', level=2)
    form_fields = [
        ['Field Name', 'Type', 'Required', 'Validation'],
        ['Name', 'text', 'Yes', 'Non-empty'],
        ['Email', 'email', 'Yes', 'Valid email format'],
        ['Phone', 'tel', 'No', 'Optional'],
        ['Subject', 'select', 'Yes', '4 predefined options'],
        ['Message', 'textarea', 'Yes', 'Minimum length'],
        ['bot-field', 'hidden', 'No', 'Honeypot (spam trap)']
    ]
    add_table(doc, form_fields)

    doc.add_paragraph()

    # Subject Options
    add_heading(doc, 'Subject Dropdown Options', level=2)
    subjects = [
        'General Inquiry',
        'Consulting Services',
        'Coaching Services',
        'Partnership Opportunity'
    ]
    for subject in subjects:
        doc.add_paragraph(f'• {subject}', style='List Bullet')

    doc.add_paragraph()

    # Form Processing Flow
    add_heading(doc, 'Form Processing Flow', level=2)
    doc.add_paragraph(
        '1. User fills out contact form\n'
        '   ↓\n'
        '2. Client-side validation (HTML5 required attributes)\n'
        '   ↓\n'
        '3. Form submission via POST to Netlify\n'
        '   ↓\n'
        '4. Netlify checks honeypot field (bot-field)\n'
        '   ↓\n'
        '5. If honeypot empty (human): Accept submission\n'
        '   If honeypot filled (bot): Reject silently\n'
        '   ↓\n'
        '6. Netlify stores submission in dashboard\n'
        '   ↓\n'
        '7. Email notification sent to admin@x4o.co.za\n'
        '   ↓\n'
        '8. User redirected to /contact-success/ page\n'
        '   ↓\n'
        '9. Success page displays confirmation message',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Screenshots
    add_screenshot_section(
        doc,
        'Contact Form (Desktop)',
        'Full desktop view of the contact page showing: banner image at top (x4o_banner.jpg), '
        'page heading "Contact Us", contact form with all fields visible (Name, Email, Phone, '
        'Subject dropdown, Message textarea), glass-card styling on form container, and blue '
        'gradient "Send Message" button at bottom.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Subject Dropdown Menu',
        'Close-up screenshot of the Subject dropdown field in expanded state, showing all 4 options: '
        'General Inquiry, Consulting Services, Coaching Services, Partnership Opportunity. '
        'Dropdown should show hover state on one option.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Form Validation Error State',
        'Screenshot showing form with validation errors: Name field empty with red border, '
        'Email field with invalid format showing browser validation message, Required field '
        'indicators visible (asterisks or red outlines).'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Contact Success Page',
        'Full view of the contact-success.astro page showing: large checkmark or success icon, '
        'heading "Thank You!", confirmation message stating "Your message has been received", '
        'sub-text about response time, and "Return to Homepage" button. Glass effect on '
        'confirmation card.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile Contact Form',
        'Mobile view of contact form showing: stacked field layout (full-width inputs), '
        'properly sized touch targets for inputs (minimum 44px height), submit button '
        'spanning full width, proper spacing between fields for easy thumb navigation.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Netlify Configuration
    add_heading(doc, 'Netlify Forms Configuration', level=2)
    doc.add_paragraph(
        'Form HTML Attributes:\n'
        '• name="contact" - Form identifier\n'
        '• method="POST" - HTTP method\n'
        '• data-netlify="true" - Enables Netlify processing\n'
        '• data-netlify-honeypot="bot-field" - Spam protection\n'
        '• action="/contact-success/" - Redirect after submit\n\n'
        'Email Notification Setup (in Netlify Dashboard):\n'
        '1. Site Settings → Forms → Form notifications\n'
        '2. Add notification → Email notification\n'
        '3. Event to listen for: New form submission\n'
        '4. Email to notify: admin@x4o.co.za\n'
        '5. Subject: "New contact form submission from x4o.co.za"\n'
        '6. Save notification settings',
        style='No Spacing'
    )

    doc.add_paragraph()

    # Spam Protection
    add_heading(doc, 'Spam Protection Strategy', level=2)
    doc.add_paragraph(
        'Honeypot Technique:\n'
        '• Hidden field "bot-field" (display: none)\n'
        '• Invisible to human users\n'
        '• Bots auto-fill all form fields, including hidden ones\n'
        '• Netlify rejects submissions with honeypot filled\n\n'
        'Additional Protection:\n'
        '• Rate limiting (Netlify built-in)\n'
        '• Akismet integration (available on paid plans)\n'
        '• reCAPTCHA (can be added if spam increases)',
        style='No Spacing'
    )

    doc.add_paragraph()

    # SDLC Best Practices
    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Serverless Architecture: No backend code or database required\n'
        '✅ Security: Honeypot spam protection, no exposed API keys\n'
        '✅ User Experience: Instant feedback on submission\n'
        '✅ Error Handling: HTML5 validation before submission\n'
        '✅ Accessibility: Proper form labels and ARIA attributes\n'
        '✅ Testing: Verified submission flow end-to-end\n'
        '✅ Monitoring: Netlify dashboard tracks submissions\n'
        '✅ Documentation: Clear setup instructions for maintenance',
        style='No Spacing'
    )

    # Technical Definitions
    definitions = {
        'Netlify Forms': 'Serverless form handling service that captures submissions without backend code',
        'Honeypot Field': 'Hidden form field used to catch spam bots (invisible to humans, filled by bots)',
        'Form Validation': 'Checking user input meets requirements before submission (email format, required fields)',
        'POST Method': 'HTTP method for submitting data to a server (vs GET which retrieves data)',
        'Serverless': 'Application architecture that runs without managing servers (provider handles infrastructure)',
        'Rate Limiting': 'Restriction on number of requests allowed within a time period to prevent abuse',
        'Success Page': 'Confirmation page shown after successful form submission',
        'Email Notification': 'Automated email sent when specific event occurs (form submission)',
        'Spam Protection': 'Techniques to prevent automated bot submissions (honeypots, CAPTCHA, rate limits)',
        'HTML5 Validation': 'Browser built-in form validation using HTML attributes (required, type="email")'
    }
    add_technical_definitions(doc, definitions)

    return doc

# ============================================================
# DOCUMENT 5: Utility Pages Development
# ============================================================
def create_utility_pages_doc():
    doc = Document()

    # Title
    add_heading(doc, 'Utility Pages Implementation', level=1)
    add_heading(doc, 'Partners Page + Custom 404 Error Page', level=2)

    # Metadata
    meta_data = [
        ['Files', 'partners.astro, 404.astro'],
        ['Purpose', 'Partner showcase + error handling'],
        ['Status', '✅ Complete'],
        ['Total Lines', '~120 lines combined']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Partners Page
    add_heading(doc, 'Partners Page Overview', level=2)
    doc.add_paragraph(
        'File: partners.astro\n\n'
        'The partners page showcases strategic partnerships with organizations in the consulting '
        'and development sectors. Features partner logos with glassmorphic card design for professional presentation.\n\n'
        'Partners Featured:\n'
        '1. EdMeCa (Education, Media, and Capacity Development)\n'
        '   • Logo: EdMeCa_logo.png\n'
        '   • Focus: Capacity building and development\n\n'
        '2. IDC (Industrial Development Corporation)\n'
        '   • Logo: idc-logo.png\n'
        '   • Focus: Industrial financing and development\n\n'
        '3. Mzilikazi Development Association\n'
        '   • Logo: mzilikazi_logo.png\n'
        '   • Focus: Community development initiatives',
        style='No Spacing'
    )

    doc.add_paragraph()

    # 404 Page
    add_heading(doc, 'Custom 404 Error Page', level=2)
    doc.add_paragraph(
        'File: 404.astro\n\n'
        'User-friendly error page displayed when a visitor navigates to a non-existent URL. '
        'Provides helpful navigation back to main site areas instead of generic browser error.\n\n'
        'Features:\n'
        '• Large "404" heading with gradient text\n'
        '• Friendly error message: "Oops! Page Not Found"\n'
        '• Helpful description text\n'
        '• "Return to Homepage" button (btn-primary)\n'
        '• Quick links to main sections (Services, Contact)\n'
        '• Glassmorphic card design matching site aesthetic\n'
        '• Organic background pattern (bg-mesh)',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Screenshots
    add_screenshot_section(
        doc,
        'Partners Page with 3 Logos',
        'Desktop view showing the partners page with: page banner (x4o_banner.jpg), heading '
        '"Our Partners", introductory text about partnerships, and 3 partner logo cards displayed '
        'in a grid. Each card should show: glass-card effect, centered logo image, partner name '
        'below logo, and consistent spacing between cards.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        '404 Error Page Layout',
        'Full desktop view of the custom 404 error page showing: large "404" text with gradient '
        'effect, "Oops! Page Not Found" heading, descriptive apologetic message, "Return to Homepage" '
        'button with btn-primary styling, and additional quick links below. Background should show '
        'bg-mesh pattern. Glass card containing the error message centered on page.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Partner Logo Card Close-up',
        'Close-up of a single partner logo card showing: glass-card background with backdrop blur, '
        'partner logo centered (e.g., EdMeCa logo), subtle border, soft shadow, and proper padding '
        'around logo. Card should demonstrate glassmorphism effect clearly.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile 404 Page',
        'Mobile screenshot of 404 error page showing: responsive layout with stacked content, '
        '404 text scaled appropriately for mobile, error message clearly readable, "Return to Homepage" '
        'button full-width or centered, and hamburger menu visible at top.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    # Design Implementation
    add_heading(doc, 'Design Implementation Details', level=2)

    design_table = [
        ['Page', 'Layout Pattern', 'Key CSS Classes'],
        ['Partners', 'Grid (3 columns → 1 column mobile)', '.glass-card, grid, grid-cols-3'],
        ['404', 'Centered card on bg pattern', '.glass-card, .text-gradient, .bg-mesh, .btn-primary']
    ]
    add_table(doc, design_table)

    doc.add_paragraph()

    # SDLC Best Practices
    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Error Handling: Custom 404 improves user experience vs browser default\n'
        '✅ Branding Consistency: 404 page matches site design (not generic error)\n'
        '✅ Navigation Recovery: Clear pathback to main site from error page\n'
        '✅ Image Optimization: Partner logos properly sized and formatted\n'
        '✅ Responsive Design: Partner cards stack on mobile devices\n'
        '✅ Semantic HTML: Proper use of figure/img elements for logos\n'
        '✅ Accessibility: Alt text on all partner logos\n'
        '✅ SEO: 404 page returns proper HTTP 404 status code',
        style='No Spacing'
    )

    # Technical Definitions
    definitions = {
        '404 Error': 'HTTP status code indicating a requested page was not found on the server',
        'Custom Error Page': 'Branded error page that replaces generic browser error messages',
        'Partner Showcase': 'Page displaying logos and information about business partnerships',
        'Grid Layout': 'CSS layout that arranges content in rows and columns for structured display',
        'HTTP Status Code': 'Three-digit code sent by server indicating request result (200=success, 404=not found)',
        'Alt Text': 'Alternative text description for images used by screen readers and SEO',
        'Figure Element': 'HTML semantic element for containing images with optional captions',
        'Navigation Recovery': 'Providing clear paths for users to return to main site content from error pages'
    }
    add_technical_definitions(doc, definitions)

    return doc

# Save all remaining documents
print("Creating remaining Phase 3 documentation...")
print("=" * 60)

# Generate Service Pages doc
service_doc = create_service_pages_doc()
service_doc.save('docs/phase3-development/service-pages-development.docx')
print("Created: service-pages-development.docx")

# Generate Contact System doc
contact_doc = create_contact_system_doc()
contact_doc.save('docs/phase3-development/contact-system-development.docx')
print("Created: contact-system-development.docx")

# Generate Utility Pages doc
utility_doc = create_utility_pages_doc()
utility_doc.save('docs/phase3-development/utility-pages-development.docx')
print("Created: utility-pages-development.docx")

print("=" * 60)
print("Part 2 complete. Continuing with final documents...")
