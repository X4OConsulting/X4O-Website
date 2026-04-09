# ============================================================================
# X4O Website - Convert Test Reports from Markdown to DOCX (PowerShell)
# ============================================================================
#
# This script converts the updated markdown test reports to Word format
#
# Prerequisites:
#   - Pandoc must be installed (https://pandoc.org/installing.html)
#   - Or install via Chocolatey: choco install pandoc
#
# Usage:
#   .\convert-reports-to-docx.ps1
#
# ============================================================================

Write-Host ""
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "X4O Test Reports - Markdown to DOCX Converter" -ForegroundColor Cyan
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host ""

# Check if pandoc is installed
$pandocInstalled = Get-Command pandoc -ErrorAction SilentlyContinue

if (-not $pandocInstalled) {
    Write-Host "ERROR: Pandoc is not installed or not in PATH" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Pandoc:"
    Write-Host "  1. Download from: https://pandoc.org/installing.html"
    Write-Host "  2. Or use Chocolatey: choco install pandoc"
    Write-Host "  3. Restart PowerShell after installation"
    Write-Host ""
    pause
    exit 1
}

$pandocVersion = pandoc --version | Select-String "pandoc" -SimpleMatch | Select-Object -First 1
Write-Host "Pandoc found: $pandocVersion" -ForegroundColor Green
Write-Host ""

# Set directories
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$phase4Dir = Join-Path (Split-Path -Parent $scriptDir) "docs\phase4-testing"
$outputDir = $phase4Dir

Write-Host "Converting test reports to DOCX format..." -ForegroundColor Yellow
Write-Host ""

# Convert Form Functionality Report
Write-Host "[1/3] Converting Form Functionality report..." -ForegroundColor Cyan
$inputFile1 = Join-Path $phase4Dir "test-report-01-form-functionality.md"
$outputFile1 = Join-Path $outputDir "test-report-01-form-functionality-updated.docx"

try {
    pandoc $inputFile1 `
        -o $outputFile1 `
        --from markdown `
        --to docx `
        --highlight-style tango

    Write-Host "      SUCCESS: test-report-01-form-functionality-updated.docx" -ForegroundColor Green
} catch {
    Write-Host "      ERROR: Failed to convert Form Functionality report" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}
Write-Host ""

# Convert Accessibility Report
Write-Host "[2/3] Converting Accessibility report..." -ForegroundColor Cyan
$inputFile2 = Join-Path $phase4Dir "test-report-07-accessibility.md"
$outputFile2 = Join-Path $outputDir "test-report-07-accessibility-updated.docx"

try {
    pandoc $inputFile2 `
        -o $outputFile2 `
        --from markdown `
        --to docx `
        --highlight-style tango

    Write-Host "      SUCCESS: test-report-07-accessibility-updated.docx" -ForegroundColor Green
} catch {
    Write-Host "      ERROR: Failed to convert Accessibility report" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}
Write-Host ""

# Convert Playwright Test Summary
Write-Host "[3/3] Converting Playwright Test Summary..." -ForegroundColor Cyan
$inputFile3 = Join-Path $phase4Dir "PLAYWRIGHT_TEST_SUMMARY.md"
$outputFile3 = Join-Path $outputDir "PLAYWRIGHT_TEST_SUMMARY.docx"

try {
    pandoc $inputFile3 `
        -o $outputFile3 `
        --from markdown `
        --to docx `
        --highlight-style tango

    Write-Host "      SUCCESS: PLAYWRIGHT_TEST_SUMMARY.docx" -ForegroundColor Green
} catch {
    Write-Host "      ERROR: Failed to convert Playwright Test Summary" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}
Write-Host ""

Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host "Conversion Complete!" -ForegroundColor Green
Write-Host "============================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Output files location: $outputDir" -ForegroundColor Yellow
Write-Host ""
Write-Host "Files created:" -ForegroundColor Yellow
Write-Host "  - test-report-01-form-functionality-updated.docx"
Write-Host "  - test-report-07-accessibility-updated.docx"
Write-Host "  - PLAYWRIGHT_TEST_SUMMARY.docx"
Write-Host ""
Write-Host "You can now open these files in Microsoft Word." -ForegroundColor Green
Write-Host ""
