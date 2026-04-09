"""
Convert all maintenance guides from Markdown to DOCX
"""
import subprocess
import os
import sys

# Define input directory
input_dir = 'docs/maintenance'

# List of markdown files to convert
md_files = [
    'CONTENT_UPDATE_GUIDE.md',
    'SEO_BEST_PRACTICES_GUIDE.md',
    'PERFORMANCE_OPTIMIZATION_GUIDE.md',
    'ANALYTICS_IMPLEMENTATION_GUIDE.md',
    'SECURITY_BEST_PRACTICES_GUIDE.md',
    'WEBSITE_ADMINISTRATOR_TRAINING_GUIDE.md'
]

print("Converting Maintenance Guides to DOCX...")
print("=" * 60)

converted = 0
failed = 0

for md_file in md_files:
    input_path = os.path.join(input_dir, md_file)
    output_path = os.path.join(input_dir, md_file.replace('.md', '.docx'))

    if not os.path.exists(input_path):
        print(f"[SKIP] {md_file} - File not found")
        continue

    try:
        # Convert using pandoc
        subprocess.run([
            'pandoc',
            input_path,
            '-o', output_path,
            '--from=markdown',
            '--to=docx'
        ], check=True, capture_output=True, text=True)

        # Get file size
        size = os.path.getsize(output_path)
        size_kb = size / 1024

        print(f"[SUCCESS] {md_file}")
        print(f"          -> {md_file.replace('.md', '.docx')} ({size_kb:.1f} KB)")
        converted += 1

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {md_file}")
        print(f"        {e.stderr}")
        failed += 1

print("=" * 60)
print(f"Conversion Complete!")
print(f"  Converted: {converted}")
print(f"  Failed: {failed}")
print(f"  Total: {len(md_files)}")
