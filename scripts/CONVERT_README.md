# Test Report Conversion Scripts

This folder contains scripts to convert the updated markdown test reports to Microsoft Word (.docx) format.

## Files Created

- `convert-reports-to-docx.bat` - Windows batch script
- `convert-reports-to-docx.ps1` - PowerShell script (recommended)

## Prerequisites

### Install Pandoc

**Option 1: Chocolatey (Recommended)**
```bash
choco install pandoc
```

**Option 2: Direct Download**
1. Download from: https://pandoc.org/installing.html
2. Run the installer
3. Restart your terminal

**Verify Installation:**
```bash
pandoc --version
```

## Usage

### Option 1: Run Batch Script (Simple)

```bash
cd scripts
convert-reports-to-docx.bat
```

### Option 2: Run PowerShell Script (Recommended)

```powershell
cd scripts
.\convert-reports-to-docx.ps1
```

If you get a security error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\convert-reports-to-docx.ps1
```

## Output

The scripts will convert these markdown files to DOCX:

1. `test-report-01-form-functionality.md` → `test-report-01-form-functionality-updated.docx`
2. `test-report-07-accessibility.md` → `test-report-07-accessibility-updated.docx`
3. `PLAYWRIGHT_TEST_SUMMARY.md` → `PLAYWRIGHT_TEST_SUMMARY.docx`

**Output Location:** `docs/phase4-testing/`

## What Gets Converted

- ✅ Headings (H1-H6)
- ✅ Tables
- ✅ Code blocks
- ✅ Lists (ordered and unordered)
- ✅ **Bold**, *italic*, `code` formatting
- ✅ Links
- ✅ Horizontal rules

## Troubleshooting

### "Pandoc not found"

**Solution:** Install Pandoc using one of the methods above, then restart your terminal.

### "File not found"

**Solution:** Make sure you're running the script from the `scripts/` directory:
```bash
cd c:\Users\keena\Projects\x4o-website-dev\scripts
```

### PowerShell execution policy error

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Manual Conversion (Alternative)

If you prefer to convert files individually:

```bash
# Navigate to the phase4-testing directory
cd docs/phase4-testing

# Convert Form Functionality report
pandoc test-report-01-form-functionality.md -o test-report-01-form-functionality-updated.docx

# Convert Accessibility report
pandoc test-report-07-accessibility.md -o test-report-07-accessibility-updated.docx

# Convert Playwright summary
pandoc PLAYWRIGHT_TEST_SUMMARY.md -o PLAYWRIGHT_TEST_SUMMARY.docx
```

## Customizing Output

### Add a table of contents

```bash
pandoc input.md -o output.docx --toc
```

### Use a custom reference document (Word template)

```bash
pandoc input.md -o output.docx --reference-doc=template.docx
```

### Change syntax highlighting style

```bash
pandoc input.md -o output.docx --highlight-style=pygments
```

Available styles: `pygments`, `tango`, `espresso`, `zenburn`, `kate`, `monochrome`, `breezedark`, `haddock`

## Support

For Pandoc documentation: https://pandoc.org/MANUAL.html

For X4O project support: khusselmann@x4o.co.za
