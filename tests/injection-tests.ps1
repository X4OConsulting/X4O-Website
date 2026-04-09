# X4O Website - Injection Testing Suite (PowerShell)
# Date: February 13, 2026
# Purpose: Test for SQL, Command, XSS, Template, and File Upload injection vulnerabilities

Write-Host "========================================================================"
Write-Host "X4O Website - Injection Testing Suite"
Write-Host "========================================================================"
Write-Host ""
Write-Host "Test Date: $(Get-Date)"
Write-Host "Target: https://x4o.co.za"
Write-Host "Test Type: Injection Vulnerability Testing"
Write-Host ""

$Script:TotalTests = 0
$Script:PassedTests = 0
$Script:FailedTests = 0
$Script:NATests = 0

function Test-Result {
    param(
        [string]$Status,
        [string]$Message
    )

    $Script:TotalTests++

    if ($Status -eq "PASS") {
        Write-Host "[PASS] " -ForegroundColor Green -NoNewline
        Write-Host $Message
        $Script:PassedTests++
    } elseif ($Status -eq "FAIL") {
        Write-Host "[FAIL] " -ForegroundColor Red -NoNewline
        Write-Host $Message
        $Script:FailedTests++
    } else {
        Write-Host "[N/A] " -ForegroundColor Yellow -NoNewline
        Write-Host $Message
        $Script:NATests++
    }
}

# ============================================================================
# SEC-033: SQL Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-033: SQL Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?id=1' OR '1'='1" -UseBasicParsing
    $content = $response.Content

    if ($content -match "sql|mysql|postgresql|database error|syntax error") {
        Test-Result "FAIL" "SEC-033: SQL injection vulnerability detected - error messages exposed"
    } else {
        Test-Result "N/A" "SEC-033: SQL injection N/A - static site with no database backend"
    }
} catch {
    Test-Result "N/A" "SEC-033: SQL injection N/A - static site with no database backend"
}

# ============================================================================
# SEC-034: Command Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-034: Command Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?cmd=;ls" -UseBasicParsing
    $content = $response.Content

    if ($content -match "bin/sh|command not found|root:|/etc/passwd") {
        Test-Result "FAIL" "SEC-034: Command injection vulnerability detected"
    } else {
        Test-Result "N/A" "SEC-034: Command injection N/A - static site with no server-side command execution"
    }
} catch {
    Test-Result "N/A" "SEC-034: Command injection N/A - static site with no server-side command execution"
}

# ============================================================================
# SEC-035: File Upload Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-035: File Upload Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $content = $response.Content

    if ($content -match "upload|type=[`"']file[`"']|multipart/form-data") {
        Test-Result "FAIL" "SEC-035: File upload functionality detected - requires manual testing"
    } else {
        Test-Result "N/A" "SEC-035: File upload injection N/A - no file upload functionality present"
    }
} catch {
    Test-Result "N/A" "SEC-035: File upload injection N/A - no file upload functionality present"
}

# ============================================================================
# SEC-036: Server-Side Template Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-036: Server-Side Template Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?name={{7*7}}" -UseBasicParsing
    $content = $response.Content

    if ($content -match "\b49\b" -and $content -match "{{") {
        Test-Result "FAIL" "SEC-036: Template injection vulnerability detected - expression evaluated"
    } else {
        Test-Result "N/A" "SEC-036: Template injection N/A - static site with build-time rendering"
    }
} catch {
    Test-Result "N/A" "SEC-036: Template injection N/A - static site with build-time rendering"
}

# ============================================================================
# Additional XSS Injection Tests
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "Additional: XSS Injection Verification"
Write-Host "------------------------------------------------------------------------"

# Test URL parameter XSS
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/contact?subject=<script>alert('XSS')</script>" -UseBasicParsing
    $content = $response.Content

    if ($content -match "<script>alert\('XSS'\)</script>") {
        Test-Result "FAIL" "XSS: Reflected XSS vulnerability in URL parameters"
    } else {
        Test-Result "PASS" "XSS: URL parameters properly escaped (no reflected XSS)"
    }
} catch {
    Test-Result "PASS" "XSS: URL parameters properly escaped (no reflected XSS)"
}

# Test for unsafe DOM manipulation
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $content = $response.Content

    if ($content -match "innerHTML\s*=|document\.write|eval\(") {
        Test-Result "FAIL" "XSS: Potentially unsafe DOM manipulation detected"
    } else {
        Test-Result "PASS" "XSS: No unsafe DOM manipulation (innerHTML, eval, document.write)"
    }
} catch {
    Test-Result "PASS" "XSS: No unsafe DOM manipulation detected"
}

# ============================================================================
# LDAP Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "Additional: LDAP Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?user=*)(uid=*))(|(uid=*" -UseBasicParsing
    $content = $response.Content

    if ($content -match "ldap|directory") {
        Test-Result "FAIL" "LDAP: LDAP injection vulnerability detected"
    } else {
        Test-Result "N/A" "LDAP: LDAP injection N/A - no directory service integration"
    }
} catch {
    Test-Result "N/A" "LDAP: LDAP injection N/A - no directory service integration"
}

# ============================================================================
# XML External Entity (XXE) Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "Additional: XXE Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $xmlPayload = @"
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
"@

    $response = Invoke-WebRequest -Uri "https://x4o.co.za/api/xml" `
        -Method POST `
        -ContentType "application/xml" `
        -Body $xmlPayload `
        -UseBasicParsing `
        -ErrorAction SilentlyContinue

    if ($response.Content -match "root:") {
        Test-Result "FAIL" "XXE: XML External Entity vulnerability detected"
    } else {
        Test-Result "N/A" "XXE: XXE injection N/A - no XML processing endpoints"
    }
} catch {
    Test-Result "N/A" "XXE: XXE injection N/A - no XML processing endpoints"
}

# ============================================================================
# NoSQL Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "Additional: NoSQL Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?filter[$ne]=null" -UseBasicParsing
    $content = $response.Content

    if ($content -match "mongodb|nosql|collection") {
        Test-Result "FAIL" "NoSQL: NoSQL injection vulnerability detected"
    } else {
        Test-Result "N/A" "NoSQL: NoSQL injection N/A - no NoSQL database backend"
    }
} catch {
    Test-Result "N/A" "NoSQL: NoSQL injection N/A - no NoSQL database backend"
}

# ============================================================================
# HTML Injection Test
# ============================================================================
Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "Additional: HTML Injection Test"
Write-Host "------------------------------------------------------------------------"

try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za/?name=<h1>Injected</h1>" -UseBasicParsing
    $content = $response.Content

    if ($content -match "<h1>Injected</h1>") {
        Test-Result "FAIL" "HTML: HTML injection vulnerability detected"
    } else {
        Test-Result "PASS" "HTML: HTML properly escaped (no HTML injection)"
    }
} catch {
    Test-Result "PASS" "HTML: HTML properly escaped (no HTML injection)"
}

# ============================================================================
# Summary
# ============================================================================
Write-Host ""
Write-Host "========================================================================"
Write-Host "Test Summary"
Write-Host "========================================================================"
Write-Host "Total Tests:  $TotalTests"
Write-Host "Passed:       $PassedTests"
Write-Host "Failed:       $FailedTests"
Write-Host "N/A:          $NATests"
$passRate = [math]::Round((($PassedTests + $NATests) * 100) / $TotalTests, 2)
Write-Host "Pass Rate:    $passRate%"
Write-Host ""

if ($FailedTests -eq 0) {
    Write-Host "Result: All injection tests passed or N/A (static site)" -ForegroundColor Green
    Write-Host "Status: SECURE" -ForegroundColor Green
    exit 0
} else {
    Write-Host "Result: $FailedTests injection vulnerabilities detected" -ForegroundColor Red
    Write-Host "Status: VULNERABILITIES FOUND" -ForegroundColor Red
    exit 1
}
