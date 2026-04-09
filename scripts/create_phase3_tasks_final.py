"""
Phase 3 Individual Task Documentation Generator - Part 5 (Final)
404 Page, Maintenance Page, and Docker
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

# TASK 9: Build 404 Error Page
def create_task_404_page():
    doc = Document()

    add_heading(doc, 'Task: Build 404 Error Page', level=1)
    add_heading(doc, '404.astro - Custom Not Found Page', level=2)

    meta_data = [
        ['Task ID', 'TASK-019 (Development Phase)'],
        ['File', 'src/pages/404.astro'],
        ['HTTP Status', '404 Not Found'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~90 lines']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'Custom 404 error page displayed when visitors navigate to non-existent URLs. Provides user-friendly '
        'error messaging, navigation recovery options, and maintains brand consistency instead of showing '
        'generic browser error pages.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Page Elements', level=2)
    doc.add_paragraph(
        '1. Large "404" Text\n'
        '   • Oversized typography (6xl or larger)\n'
        '   • Gradient text effect (.text-gradient)\n'
        '   • Centered on page\n\n'
        '2. Error Message\n'
        '   • Heading: "Oops! Page Not Found"\n'
        '   • Friendly tone, not intimidating\n'
        '   • Brief explanation\n\n'
        '3. Description Text\n'
        '   • "The page you\'re looking for doesn\'t exist"\n'
        '   • Possible reasons (mistyped URL, moved page)\n'
        '   • Apologetic but helpful tone\n\n'
        '4. Navigation Options\n'
        '   • "Return to Homepage" button (btn-primary)\n'
        '   • Quick links section:\n'
        '     - Services\n'
        '     - Contact\n'
        '     - About\n\n'
        '5. Background\n'
        '   • bg-mesh pattern\n'
        '   • Glass card container for content\n'
        '   • Matches site aesthetic',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Full 404 Page Desktop',
        'Desktop screenshot showing: centered glass-card container on bg-mesh background, large "404" text '
        'with gradient effect, "Oops! Page Not Found" heading, apologetic message, "Return to Homepage" '
        'button with btn-primary styling, and quick links section below.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile 404 Page',
        'Mobile view showing 404 error page with: scaled-down "404" text still prominent, headings readable, '
        'full-width CTA button, quick links stacked vertically, proper spacing for touch navigation.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Error Handling Best Practices', level=2)
    doc.add_paragraph(
        '✅ User-Friendly Language:\n'
        '   • Avoid technical jargon\n'
        '   • Friendly, apologetic tone\n'
        '   • Clear explanation of what happened\n\n'
        '✅ Navigation Recovery:\n'
        '   • Clear path back to homepage\n'
        '   • Alternative destination options\n'
        '   • Working header navigation\n\n'
        '✅ HTTP Status Code:\n'
        '   • Returns proper 404 status\n'
        '   • Prevents indexing by search engines\n'
        '   • Signals error to analytics tools',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_heading(doc, 'Common 404 Triggers', level=2)

    triggers_table = [
        ['Scenario', 'Example', 'User Action'],
        ['Mistyped URL', 'x4o.co.za/servces (missing "i")', 'Return to homepage or search'],
        ['Old/Outdated Link', 'Link from old Wix site', 'Use new navigation'],
        ['Deleted Page', 'Page removed after redesign', 'Browse category pages'],
        ['Typo in Bookmark', 'User saved incorrect URL', 'Update bookmark']
    ]
    add_table(doc, triggers_table)

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ User Experience: Friendly error handling vs generic browser message\n'
        '✅ Brand Consistency: Custom 404 matches site design\n'
        '✅ Navigation Recovery: Clear recovery paths\n'
        '✅ SEO: Proper HTTP 404 status code\n'
        '✅ Analytics: 404 errors tracked in Netlify/GA\n'
        '✅ Accessibility: Clear messaging, semantic structure\n'
        '✅ Mobile Optimization: Responsive layout\n'
        '✅ Performance: Static page, fast load',
        style='No Spacing'
    )

    definitions = {
        '404 Error': 'HTTP status code indicating requested page was not found on server',
        'HTTP Status Code': 'Three-digit code sent by server indicating request result (200=success, 404=not found)',
        'Custom Error Page': 'Branded error page replacing generic browser error messages',
        'Navigation Recovery': 'Providing clear paths for users to return to main site content',
        'Indexing': 'Process where search engines catalog web pages for search results',
        'Browser Error': 'Generic error page shown by browser when custom page not available',
        'URL (Uniform Resource Locator)': 'Web address pointing to specific page or resource'
    }
    add_technical_definitions(doc, definitions)

    return doc

# TASK 10: Build Maintenance Page
def create_task_maintenance_page():
    doc = Document()

    add_heading(doc, 'Task: Build Standalone Maintenance Page', level=1)
    add_heading(doc, 'public/maintenance.html', level=2)

    meta_data = [
        ['Task ID', 'TASK-020 (Development Phase)'],
        ['File', 'public/maintenance.html'],
        ['Purpose', 'Scheduled maintenance downtime page'],
        ['Status', '✅ Complete'],
        ['Lines of Code', '~150 lines (standalone HTML)']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'Standalone maintenance page displayed during scheduled maintenance windows. Self-contained HTML file '
        'with inline CSS (no external dependencies) that can be activated by modifying netlify.toml redirect rules. '
        'Informs visitors of maintenance status and expected return time.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Page Elements', level=2)
    doc.add_paragraph(
        '1. Maintenance Icon/Image\n'
        '   • Wrench/tool icon or "Under Construction" graphic\n'
        '   • SVG or inline image (no external files)\n'
        '   • Centered and prominent\n\n'
        '2. Status Message\n'
        '   • Heading: "Scheduled Maintenance"\n'
        '   • Clear communication about downtime\n\n'
        '3. Information Panel\n'
        '   • Current status: "We\'re currently updating our systems"\n'
        '   • Expected completion time\n'
        '   • Apology for inconvenience\n\n'
        '4. Contact Information\n'
        '   • Email: info@x4o.co.za\n'
        '   • Phone number (if urgent)\n'
        '   • Social media links\n\n'
        '5. Inline CSS Styling\n'
        '   • All styles in <style> tag\n'
        '   • No external CSS files\n'
        '   • Glassmorphic aesthetic maintained',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Activation Method', level=2)
    doc.add_paragraph(
        'To Enable Maintenance Mode:\n\n'
        '1. Edit netlify.toml\n'
        '2. Add redirect rule at TOP of [[redirects]] section:\n\n'
        '   [[redirects]]\n'
        '     from = "/*"\n'
        '     to = "/maintenance.html"\n'
        '     status = 503\n'
        '     force = true\n\n'
        '3. Commit and push to triggerbuild\n'
        '4. Maintenance page now shown for all URLs\n\n'
        'To Disable Maintenance Mode:\n\n'
        '1. Remove the redirect rule from netlify.toml\n'
        '2. Commit and push\n'
        '3. Site returns to normal operation',
        style='No Spacing'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Maintenance Page Desktop',
        'Desktop screenshot showing maintenance page with: centered container, construction/wrench icon, '
        '"Scheduled Maintenance" heading, message explaining updates in progress, estimated completion time, '
        'contact information section, inline CSS styling matching X4O brand colors.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Mobile Maintenance View',
        'Mobile screenshot showing responsive maintenance page: scaled content, readable text, centered icon, '
        'touch-friendly contact buttons, proper spacing for mobile viewing.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Technical Specifications', level=2)

    tech_specs = [
        ['Specification', 'Value', 'Reason'],
        ['File Type', 'Standalone HTML', 'Works even if build system down'],
        ['CSS Location', 'Inline <style> tag', 'No external dependencies'],
        ['JavaScript', 'None or minimal inline', 'Maximum reliability'],
        ['Images', 'Inline SVG or data URIs', 'No external file loading'],
        ['HTTP Status', '503 Service Unavailable', 'Proper maintenance signal'],
        ['Favicon', 'Inline or excluded', 'Avoid broken images']
    ]
    add_table(doc, tech_specs)

    doc.add_paragraph()

    add_heading(doc, 'Maintenance Scenarios', level=2)

    scenarios_table = [
        ['Scenario', 'Duration', 'Activation Method'],
        ['Scheduled updates', '1-4 hours', 'Plan ahead, announce via email/social'],
        ['Emergency fixes', '15-60 minutes', 'Quick activation, minimal notice'],
        ['Major migrations', '4-24 hours', 'Scheduled window, extensive communication'],
        ['Testing deployments', '5-15 minutes', 'Staging environment preferred']
    ]
    add_table(doc, scenarios_table)

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Reliability: Standalone page works even if build system fails\n'
        '✅ Communication: Clear status and timeline\n'
        '✅ Zero Dependencies: Inline CSS/SVG, no external files\n'
        '✅ HTTP Status: Proper 503 code signals temporary unavailability\n'
        '✅ Contact Options: Alternative ways to reach company\n'
        '✅ Brand Consistency: Matches site aesthetic\n'
        '✅ Mobile Responsive: Works on all devices\n'
        '✅ Documentation: Clear activation/deactivation instructions',
        style='No Spacing'
    )

    definitions = {
        'Maintenance Mode': 'State where website is temporarily unavailable for updates or fixes',
        'Standalone HTML': 'Self-contained HTML file with all code/styles inline (no external dependencies)',
        'Inline CSS': 'CSS code written directly in HTML <style> tag vs external .css file',
        'HTTP 503': 'Service Unavailable status code indicating temporary downtime',
        'Redirect Rule': 'Server configuration routing URLs to different destinations',
        'Data URI': 'Encoding scheme embedding files directly in HTML (data:image/png;base64,...)',
        'SVG (Scalable Vector Graphics)': 'Vector image format that can be inline in HTML',
        'netlify.toml': 'Configuration file for Netlify deployment settings'
    }
    add_technical_definitions(doc, definitions)

    return doc

# TASK 11: Docker Containerization
def create_task_docker():
    doc = Document()

    add_heading(doc, 'Task: Implement Docker Containerization', level=1)
    add_heading(doc, 'Dockerfile + docker-compose.yml', level=2)

    meta_data = [
        ['Task ID', 'TASK-021 (Development Phase)'],
        ['Files', 'Dockerfile, docker-compose.yml'],
        ['Base Image', 'node:22-alpine'],
        ['Status', '✅ Complete']
    ]
    add_table(doc, meta_data, has_header=False)

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Overview', level=2)
    doc.add_paragraph(
        'Docker containerization packages the X4O website with all dependencies into isolated, portable containers. '
        'Multi-stage build optimizes production image size (~50MB). Docker Compose orchestrates development and '
        'preview environments for consistent local development.'
    )

    doc.add_paragraph()

    add_heading(doc, 'Dockerfile Structure', level=2)
    doc.add_paragraph(
        'Multi-Stage Build:\n\n'
        'Stage 1: Builder\n'
        '• FROM node:22-alpine AS builder\n'
        '• Install all dependencies (including devDependencies)\n'
        '• Copy source code\n'
        '• Run npm run build\n'
        '• Output: dist/ folder with built static files\n\n'
        'Stage 2: Production\n'
        '• FROM node:22-alpine (fresh clean image)\n'
        '• Copy only dist/ from builder stage\n'
        '• Copy package.json for metadata\n'
        '• Install ONLY production dependencies\n'
        '• EXPOSE 4321\n'
        '• CMD ["npm", "run", "preview"]\n\n'
        'Result:\n'
        '• Builder stage: ~500MB (with build tools)\n'
        '• Production stage: ~50MB (90% reduction)',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'docker-compose.yml Services', level=2)

    services_table = [
        ['Service', 'Purpose', 'Port', 'Command'],
        ['dev', 'Development with hot reload', '4321:4321', 'npm run dev'],
        ['preview', 'Production preview', '8080:4321', 'npm run preview']
    ]
    add_table(doc, services_table)

    doc.add_paragraph()

    add_heading(doc, 'Development Workflow', level=2)
    doc.add_paragraph(
        'Daily Development:\n\n'
        '1. Start dev server:\n'
        '   docker compose up dev\n\n'
        '2. Open browser:\n'
        '   http://localhost:4321\n\n'
        '3. Edit files in src/\n'
        '   • Changes trigger hot reload\n'
        '   • Browser updates automatically\n\n'
        '4. Stop containers:\n'
        '   Ctrl+C or docker compose down\n\n'
        'Pre-deployment Testing:\n\n'
        '1. Build production image:\n'
        '   docker compose build preview\n\n'
        '2. Run production preview:\n'
        '   docker compose up preview\n\n'
        '3. Test at:\n'
        '   http://localhost:8080\n\n'
        '4. Verify:\n'
        '   • All pages load\n'
        '   • No console errors\n'
        '   • Forms work correctly',
        style='No Spacing'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Dockerfile Multi-Stage Build',
        'Screenshot of Dockerfile in VS Code showing: two FROM statements (builder and production stages), '
        'builder stage with npm ci and npm run build, production stage copying only dist/, syntax highlighting, '
        'clear stage separation with comments.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'docker-compose.yml Configuration',
        'Screenshot of docker-compose.yml showing: two services (dev and preview), buildtarget configuration, '
        'port mappings (4321 and 8080), volume mount for dev service, YAML syntax highlighting.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Terminal: docker compose up dev',
        'Terminal screenshot showing: docker compose up dev command output, container building, npm install, '
        'Astro dev server starting, "Local: http://localhost:4321" success message with green checkmark.'
    )

    doc.add_paragraph()

    add_screenshot_section(
        doc,
        'Docker Desktop Running Containers',
        'Screenshot of Docker Desktop showing: two container rows (dev and preview), green running indicator, '
        'port mappings visible, CPU/memory usage,container logs accessible, stop/restart buttons.'
    )

    doc.add_paragraph()
    doc.add_paragraph('─' * 60)
    doc.add_paragraph()

    add_heading(doc, 'Benefits of Containerization', level=2)

    benefits_table = [
        ['Benefit', 'Description'],
        ['Environment Consistency', 'Dev, staging, prod all use identical Node 22 + dependencies'],
        ['Onboarding Speed', 'New developers run `docker compose up` - no local setup'],
        ['Isolation', 'Project dependencies don\'t conflict with other projects'],
        ['Portability', 'Runs anywhere Docker installed (Windows, Mac, Linux)'],
        ['Reproducibility', 'Same Dockerfile always produces same container'],
        ['Resource Efficiency', 'Alpine Linux keeps containers lightweight']
    ]
    add_table(doc, benefits_table)

    doc.add_paragraph()

    add_heading(doc, 'Image Layer Breakdown', level=2)

    layers_table = [
        ['Layer', 'Size', 'Contents'],
        ['node:22-alpine base', '~40 MB', 'Alpine Linux + Node.js 22'],
        ['Dependencies (npm)', '~8 MB', 'Astro, Tailwind, TypeScript'],
        ['Built files (dist/)', '~2 MB', 'HTML, CSS, JS, images'],
        ['Total Production', '~50 MB', 'Complete runnable container']
    ]
    add_table(doc, layers_table)

    doc.add_paragraph()

    add_heading(doc, 'SDLC Best Practices Applied', level=2)
    doc.add_paragraph(
        '✅ Environment Parity: Dev/staging/prod use same configuration\n'
        '✅ Build Optimization: Multi-stage reduces image by 90%\n'
        '✅ Security: Alpine Linux minimal attack surface\n'
        '✅ Developer Experience: Single command to start\n'
        '✅ CI/CD Ready: Dockerfile usable in pipelines\n'
        '✅ Immutable Builds: Same Dockerfile = same result\n'
        '✅ Resource Efficiency: Lightweight containers\n'
        '✅ Documentation: Comments explain each step',
        style='No Spacing'
    )

    definitions = {
        'Docker': 'Platform for packaging applications into containers (isolated environments with dependencies)',
        'Container': 'Lightweight standalone package containing code, runtime, libraries, and settings',
        'Docker Image': 'Blueprint/template used to create containers (like a class in OOP)',
        'Dockerfile': 'Text file with instructions for building Docker image',
        'Multi-stage Build': 'Docker technique using multiple FROM statements for optimized images',
        'Docker Compose': 'Tool for defining and running multi-container applications using YAML',
        'Alpine Linux': 'Minimal Linux distribution (~5MB) optimized for containers',
        'Volume Mount': 'Linking folder on host to folder in container (for live file editing)',
        'Hot Reload': 'Automatic browser refresh when source code changes',
        'Port Mapping': 'Forwarding container port to host (4321:4321 = container→localhost)',
        'Build Context': 'Directory containing files Docker can access during build',
        'Layer': 'Read-only filesystem change in Docker image (each instruction creates layer)',
        'devDependencies': 'npm packages needed only for development (build tools, not runtime)'
    }
    add_technical_definitions(doc, definitions)

    return doc

# Generate final documents
print("Creating Part 5: Final Tasks (404, Maintenance, Docker)...")
print("=" * 60)

import os
os.makedirs('docs/phase3-tasks', exist_ok=True)

task9_doc = create_task_404_page()
task9_doc.save('docs/phase3-tasks/task-019-build-404-page.docx')
print("Created: task-019-build-404-page.docx")

task10_doc = create_task_maintenance_page()
task10_doc.save('docs/phase3-tasks/task-020-build-maintenance-page.docx')
print("Created: task-020-build-maintenance-page.docx")

task11_doc = create_task_docker()
task11_doc.save('docs/phase3-tasks/task-021-docker-containerization.docx')
print("Created: task-021-docker-containerization.docx")

print("=" * 60)
print("✅ ALL PHASE 3 TASK DOCUMENTATION COMPLETE!")
print("=" * 60)
print("\nTotal Task Documents Created: 11")
print("\nLocation: docs/phase3-tasks/")
print("\n Files:")
print("  1. task-011-initialize-astro-project.docx")
print("  2. task-012-build-homepage.docx")
print("  3. task-013-build-consulting-advisory-page.docx")
print("  4. task-014-build-coaching-services-page.docx")
print("  5. task-015-build-book-coaching-sessions.docx")
print("  6. task-016-build-contact-page.docx")
print("  7. task-017-build-contact-success.docx")
print("  8. task-018-build-partners-page.docx")
print("  9. task-019-build-404-page.docx")
print(" 10. task-020-build-maintenance-page.docx")
print(" 11. task-021-docker-containerization.docx")
print("\n" + "=" * 60)
