"""
Convert X4O_SCOPE.md to Word DOCX format
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re

def add_table_border(table):
    """Add borders to table"""
    tbl = table._element
    tblPr = tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)

    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), '000000')
        tblBorders.append(border)
    tblPr.append(tblBorders)

def parse_markdown_to_docx(md_file, docx_file):
    """Convert markdown file to Word document"""
    doc = Document()

    # Set up styles
    styles = doc.styles

    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    in_code_block = False
    code_lines = []
    in_table = False
    table_data = []

    while i < len(lines):
        line = lines[i].rstrip()

        # Handle code blocks
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                # End of code block - add to document
                in_code_block = False
                para = doc.add_paragraph('\n'.join(code_lines))
                para.style = 'Normal'
                for run in para.runs:
                    run.font.name = 'Courier New'
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(0, 0, 0)
                para.paragraph_format.left_indent = Inches(0.5)
                para.paragraph_format.space_before = Pt(6)
                para.paragraph_format.space_after = Pt(6)
                code_lines = []
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Handle tables
        if line.startswith('|') and not in_table:
            # Start of table
            in_table = True
            table_data = []
            table_data.append([cell.strip() for cell in line.split('|')[1:-1]])
            i += 1
            # Skip separator line
            if i < len(lines) and '---' in lines[i]:
                i += 1
            continue

        if in_table:
            if line.startswith('|'):
                table_data.append([cell.strip() for cell in line.split('|')[1:-1]])
                i += 1
                continue
            else:
                # End of table - add to document
                in_table = False
                if table_data:
                    table = doc.add_table(rows=len(table_data), cols=len(table_data[0]))
                    add_table_border(table)

                    # Fill table
                    for row_idx, row_data in enumerate(table_data):
                        for col_idx, cell_data in enumerate(row_data):
                            cell = table.rows[row_idx].cells[col_idx]
                            cell.text = cell_data
                            # Header row formatting
                            if row_idx == 0:
                                for paragraph in cell.paragraphs:
                                    for run in paragraph.runs:
                                        run.font.bold = True
                                        run.font.size = Pt(10)
                                cell.paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                                # Shade header row
                                shading_elm = OxmlElement('w:shd')
                                shading_elm.set(qn('w:fill'), 'D9E9F7')
                                cell._element.get_or_add_tcPr().append(shading_elm)

                    table.style = 'Light Grid Accent 1'
                    doc.add_paragraph()  # Add spacing after table
                table_data = []
                # Don't increment i, process this line normally
                continue

        # Handle headings
        if line.startswith('# '):
            p = doc.add_heading(line[2:], level=1)
            p.runs[0].font.color.rgb = RGBColor(23, 64, 105)  # Primary Dark
            i += 1
            continue

        if line.startswith('## '):
            p = doc.add_heading(line[3:], level=2)
            p.runs[0].font.color.rgb = RGBColor(23, 64, 105)
            i += 1
            continue

        if line.startswith('### '):
            p = doc.add_heading(line[4:], level=3)
            p.runs[0].font.color.rgb = RGBColor(23, 64, 105)
            i += 1
            continue

        # Handle bullet lists
        if line.startswith('- '):
            text = line[2:]
            # Handle bold text
            para = doc.add_paragraph(style='List Bullet')
            if '**' in text:
                parts = re.split(r'\*\*(.*?)\*\*', text)
                for idx, part in enumerate(parts):
                    run = para.add_run(part)
                    if idx % 2 == 1:  # Bold parts
                        run.font.bold = True
            else:
                para.add_run(text)
            i += 1
            continue

        # Handle empty lines
        if not line:
            doc.add_paragraph()
            i += 1
            continue

        # Handle regular paragraphs with bold formatting
        para = doc.add_paragraph()
        if '**' in line:
            parts = re.split(r'\*\*(.*?)\*\*', line)
            for idx, part in enumerate(parts):
                run = para.add_run(part)
                if idx % 2 == 1:  # Bold parts
                    run.font.bold = True
        else:
            para.add_run(line)

        i += 1

    # Save document
    doc.save(docx_file)
    print(f"Successfully converted to {docx_file}")

if __name__ == "__main__":
    print("\n" + "="*80)
    print("X4O Test Reports - Markdown to DOCX Converter")
    print("="*80 + "\n")

    files = [
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-01-form-functionality.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-01-form-functionality-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-02-responsive-design.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-02-responsive-design-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-03-maintenance-mode.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-03-maintenance-mode-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-04-branch-deploys.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-04-branch-deploys-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-05-dns-resolution.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-05-dns-resolution-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-06-cross-browser.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-06-cross-browser-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-07-accessibility.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-07-accessibility-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-08-lighthouse.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\test-report-08-lighthouse-updated.docx"),
        (r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\PLAYWRIGHT_TEST_SUMMARY.md",
         r"c:\Users\keena\Projects\x4o-website-dev\docs\phase4-testing\PLAYWRIGHT_TEST_SUMMARY.docx")
    ]

    print("Converting 9 markdown reports to DOCX format...\n")

    for i, (md_file, docx_file) in enumerate(files, 1):
        print(f"[{i}/9] Converting {md_file.split('\\')[-1]}...")
        try:
            parse_markdown_to_docx(md_file, docx_file)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

    print("\n" + "="*80)
    print("Conversion Complete!")
    print("="*80)
    print("\nOutput files location: docs\\phase4-testing\\")
    print("\nFiles created:")
    print("  - test-report-01-form-functionality-updated.docx")
    print("  - test-report-02-responsive-design-updated.docx")
    print("  - test-report-03-maintenance-mode-updated.docx")
    print("  - test-report-04-branch-deploys-updated.docx")
    print("  - test-report-05-dns-resolution-updated.docx")
    print("  - test-report-06-cross-browser-updated.docx")
    print("  - test-report-07-accessibility-updated.docx")
    print("  - test-report-08-lighthouse-updated.docx")
    print("  - PLAYWRIGHT_TEST_SUMMARY.docx")
    print("\nYou can now open these files in Microsoft Word.\n")
