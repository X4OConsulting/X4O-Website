@echo off
REM ============================================================================
REM X4O Website - Convert Test Reports from Markdown to DOCX
REM ============================================================================
REM
REM This script converts the updated markdown test reports to Word format
REM
REM Prerequisites:
REM   - Pandoc must be installed (https://pandoc.org/installing.html)
REM   - Or install via Chocolatey: choco install pandoc
REM
REM Usage:
REM   convert-reports-to-docx.bat
REM
REM ============================================================================

echo.
echo ============================================================================
echo X4O Test Reports - Markdown to DOCX Converter
echo ============================================================================
echo.

REM Check if pandoc is installed
where pandoc >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Pandoc is not installed or not in PATH
    echo.
    echo Please install Pandoc:
    echo   1. Download from: https://pandoc.org/installing.html
    echo   2. Or use Chocolatey: choco install pandoc
    echo   3. Restart your terminal after installation
    echo.
    pause
    exit /b 1
)

echo Pandoc found:
pandoc --version | findstr /C:"pandoc"
echo.

REM Set directories
set "PHASE4_DIR=..\docs\phase4-testing"
set "OUTPUT_DIR=..\docs\phase4-testing"

echo Converting test reports to DOCX format...
echo.

REM Convert Form Functionality Report
echo [1/3] Converting Form Functionality report...
pandoc "%PHASE4_DIR%\test-report-01-form-functionality.md" ^
    -o "%OUTPUT_DIR%\test-report-01-form-functionality-updated.docx" ^
    --from markdown ^
    --to docx ^
    --highlight-style tango

if %ERRORLEVEL% EQU 0 (
    echo       SUCCESS: test-report-01-form-functionality-updated.docx
) else (
    echo       ERROR: Failed to convert Form Functionality report
)
echo.

REM Convert Accessibility Report
echo [2/3] Converting Accessibility report...
pandoc "%PHASE4_DIR%\test-report-07-accessibility.md" ^
    -o "%OUTPUT_DIR%\test-report-07-accessibility-updated.docx" ^
    --from markdown ^
    --to docx ^
    --highlight-style tango

if %ERRORLEVEL% EQU 0 (
    echo       SUCCESS: test-report-07-accessibility-updated.docx
) else (
    echo       ERROR: Failed to convert Accessibility report
)
echo.

REM Convert Playwright Test Summary
echo [3/3] Converting Playwright Test Summary...
pandoc "%PHASE4_DIR%\PLAYWRIGHT_TEST_SUMMARY.md" ^
    -o "%OUTPUT_DIR%\PLAYWRIGHT_TEST_SUMMARY.docx" ^
    --from markdown ^
    --to docx ^
    --highlight-style tango

if %ERRORLEVEL% EQU 0 (
    echo       SUCCESS: PLAYWRIGHT_TEST_SUMMARY.docx
) else (
    echo       ERROR: Failed to convert Playwright Test Summary
)
echo.

echo ============================================================================
echo Conversion Complete!
echo ============================================================================
echo.
echo Output files location: %OUTPUT_DIR%
echo.
echo Files created:
echo   - test-report-01-form-functionality-updated.docx
echo   - test-report-07-accessibility-updated.docx
echo   - PLAYWRIGHT_TEST_SUMMARY.docx
echo.
echo You can now open these files in Microsoft Word.
echo.
pause
