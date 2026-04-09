#!/usr/bin/env python3
"""Convert all Phase 6 documentation markdown files to DOCX format."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re
import os

def convert_markdown_to_docx(md_file, docx_file):
    """Convert markdown file to DOCX."""

    print(f"Converting {os.path.basename(md_file)}...")

    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create a new Document
    doc = Document()

    # Split content into lines
    lines = content.split('\n')

    in_code_block = False

    for line in lines:
        # Handle code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            p = doc.add_paragraph(line)
            if p.runs:
                run = p.runs[0]
                run.font.name = 'Courier New'
                run.font.size = Pt(9)
            continue

        # Skip empty lines
        if not line.strip():
            doc.add_paragraph()
            continue

        # H1: Main title
        if line.startswith('# '):
            p = doc.add_heading(line[2:], level=1)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # H2: Section headers
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        # H3: Subsection headers
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        # H4: Sub-subsection headers
        elif line.startswith('#### '):
            doc.add_heading(line[5:], level=4)
        # Bullet points
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            # Remove markdown formatting
            text = text.replace('**', '').replace('*', '')
            doc.add_paragraph(text, style='List Bullet')
        # Numbered lists
        elif re.match(r'^\d+\.', line.strip()):
            text = re.sub(r'^\d+\.\s*', '', line.strip())
            # Remove markdown formatting
            text = text.replace('**', '').replace('*', '')
            doc.add_paragraph(text, style='List Number')
        # Table separators (skip)
        elif line.strip().startswith('|---') or line.strip().startswith('|-'):
            continue
        # Tables
        elif '|' in line and line.count('|') >= 2:
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if cells:
                # Remove markdown formatting from cells
                cells = [cell.replace('**', '') for cell in cells]
                doc.add_paragraph(' | '.join(cells))
        # Horizontal rules
        elif line.strip() == '---':
            doc.add_paragraph('_' * 80)
        # Regular paragraphs
        else:
            # Remove markdown formatting
            text = line.replace('**', '').replace('*', '')
            doc.add_paragraph(text)

    # Save the document
    doc.save(docx_file)
    print(f'  Success: Created {os.path.basename(docx_file)}')

def main():
    """Convert all Phase 6 documentation files."""

    print("=" * 80)
    print("X4O Website - Phase 6 Documentation Converter")
    print("=" * 80)
    print()

    # Define files to convert
    files = [
        ('CLAUDE.md', 'CLAUDE.docx'),
        ('README.md', 'README.docx'),
        ('MAINTENANCE.md', 'MAINTENANCE.docx'),
        ('BACKUP.md', 'BACKUP.docx'),
        ('SOCIAL-MEDIA-GUIDE.md', 'SOCIAL-MEDIA-GUIDE.docx'),
    ]

    converted = 0
    errors = 0

    for md_file, docx_file in files:
        try:
            if os.path.exists(md_file):
                convert_markdown_to_docx(md_file, docx_file)
                converted += 1
            else:
                print(f'  ERROR: Not found: {md_file}')
                errors += 1
        except Exception as e:
            print(f'  ERROR converting {md_file}: {e}')
            errors += 1

    print()
    print("=" * 80)
    print("Conversion Complete!")
    print("=" * 80)
    print(f"Converted: {converted} files")
    print(f"Errors: {errors} files")
    print()
    print("DOCX files created:")
    for _, docx_file in files:
        if os.path.exists(docx_file):
            print(f"  - {docx_file}")
    print()

if __name__ == '__main__':
    main()
