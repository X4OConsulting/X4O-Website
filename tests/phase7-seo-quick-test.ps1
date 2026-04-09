##############################################################################
# Phase 7 SEO Quick Validation Script (PowerShell)
# Tests robots.txt and sitemap.xml functionality
#
# Usage: .\tests\phase7-seo-quick-test.ps1 [-Url "https://yoursite.com"]
# Example: .\tests\phase7-seo-quick-test.ps1 -Url "https://staging--x4oconsultants.netlify.app"
#
# Date: February 16, 2026
##############################################################################

param(
    [string]$Url = "http://localhost:4321"
)

# Test counters
$script:TotalTests = 0
$script:PassedTests = 0
$script:FailedTests = 0

# Colors
function Write-Pass { Write-Host "[PASS]" -ForegroundColor Green }
function Write-Fail { Write-Host "[FAIL]" -ForegroundColor Red }
function Write-Header { param($Text) Write-Host $Text -ForegroundColor Cyan }
function Write-Info { param($Text) Write-Host $Text -ForegroundColor Yellow }

# Test function
function Test-Feature {
    param(
        [string]$TestName,
        [string]$Endpoint,
        [string]$ExpectedPattern,
        [string]$CheckType = "Content" # Can be "Content", "StatusCode", or "Header"
    )

    $script:TotalTests++
    Write-Host -NoNewline "Testing: $TestName ... "

    try {
        $response = Invoke-WebRequest -Uri "$Url$Endpoint" -UseBasicParsing -ErrorAction Stop

        $passed = $false

        switch ($CheckType) {
            "StatusCode" {
                if ($response.StatusCode -eq [int]$ExpectedPattern) {
                    $passed = $true
                }
            }
            "Header" {
                $headerValue = $response.Headers[$ExpectedPattern]
                if ($headerValue) {
                    $passed = $true
                }
            }
            "Content" {
                if ($response.Content -match $ExpectedPattern) {
                    $passed = $true
                }
            }
        }

        if ($passed) {
            Write-Pass
            $script:PassedTests++
        } else {
            Write-Fail
            Write-Host "  Expected: $ExpectedPattern" -ForegroundColor Gray
            $script:FailedTests++
        }
    }
    catch {
        Write-Fail
        Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Gray
        $script:FailedTests++
    }
}

# Header
Write-Header "============================================================="
Write-Header "       Phase 7 SEO Quick Validation Test Suite          "
Write-Header "============================================================="
Write-Host ""
Write-Info "Testing URL: $Url"
Write-Host ""

Write-Header "============================================================="
Write-Header " SEO Enhancement Tests"
Write-Header "============================================================="

# Test 1: robots.txt exists (HTTP 200)
Test-Feature -TestName "P7-SEO-001: robots.txt exists" `
             -Endpoint "/robots.txt" `
             -ExpectedPattern "200" `
             -CheckType "StatusCode"

# Test 2: robots.txt contains User-agent
Test-Feature -TestName "P7-SEO-002: robots.txt User-agent directive" `
             -Endpoint "/robots.txt" `
             -ExpectedPattern "User-agent: \*"

# Test 3: robots.txt contains Allow directive
Test-Feature -TestName "P7-SEO-002: robots.txt Allow directive" `
             -Endpoint "/robots.txt" `
             -ExpectedPattern "Allow: /"

# Test 4: robots.txt contains Sitemap URL
Test-Feature -TestName "P7-SEO-002: robots.txt Sitemap reference" `
             -Endpoint "/robots.txt" `
             -ExpectedPattern "Sitemap:"

# Test 5: sitemap-index.xml exists (HTTP 200)
Test-Feature -TestName "P7-SEO-003: sitemap-index.xml exists" `
             -Endpoint "/sitemap-index.xml" `
             -ExpectedPattern "200" `
             -CheckType "StatusCode"

# Test 6: sitemap-0.xml exists (HTTP 200)
Test-Feature -TestName "P7-SEO-003: sitemap-0.xml exists" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "200" `
             -CheckType "StatusCode"

# Test 7: sitemap contains homepage
Test-Feature -TestName "P7-SEO-004: sitemap contains homepage" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "<loc>https://x4o\.co\.za/</loc>"

# Test 8: sitemap contains contact page
Test-Feature -TestName "P7-SEO-004: sitemap contains contact page" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "<loc>https://x4o\.co\.za/contact</loc>"

# Test 9: sitemap contains consulting page
Test-Feature -TestName "P7-SEO-004: sitemap contains consulting page" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "consulting-and-advisory-services"

# Test 10: sitemap has valid XML namespace
Test-Feature -TestName "P7-SEO-005: sitemap XML namespace" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern 'xmlns="http://www\.sitemaps\.org/schemas/sitemap/0\.9"'

# Test 11: sitemap has urlset element
Test-Feature -TestName "P7-SEO-005: sitemap urlset element" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "<urlset"

# Test 12: robots.txt is text/plain
Test-Feature -TestName "P7-SEO-001: robots.txt Content-Type" `
             -Endpoint "/robots.txt" `
             -ExpectedPattern "text/plain"

# Test 13: sitemap is XML
Test-Feature -TestName "P7-SEO-006: sitemap Content-Type" `
             -Endpoint "/sitemap-0.xml" `
             -ExpectedPattern "(application/xml|text/xml)"

Write-Host ""
Write-Header "============================================================="
Write-Header " Test Summary"
Write-Header "============================================================="
Write-Host ""

Write-Host "Total Tests:  " -NoNewline
Write-Host $script:TotalTests -ForegroundColor Cyan

Write-Host "Passed:       " -NoNewline
Write-Host $script:PassedTests -ForegroundColor Green

Write-Host "Failed:       " -NoNewline
Write-Host $script:FailedTests -ForegroundColor Red

$passRate = [math]::Round(($script:PassedTests / $script:TotalTests) * 100, 1)
Write-Host "Pass Rate:    " -NoNewline
Write-Info "$passRate%"

Write-Host ""

if ($script:FailedTests -eq 0) {
    Write-Host "=============================================================" -ForegroundColor Green
    Write-Host "           [PASS] ALL TESTS PASSED SUCCESSFULLY              " -ForegroundColor Green
    Write-Host "=============================================================" -ForegroundColor Green
    Write-Host ""
    exit 0
} else {
    Write-Host "=============================================================" -ForegroundColor Red
    Write-Host "                [FAIL] SOME TESTS FAILED                     " -ForegroundColor Red
    Write-Host "=============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please review failed tests above and fix issues before deployment." -ForegroundColor Yellow
    Write-Host ""
    exit 1
}
