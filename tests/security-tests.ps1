# X4O Website - Security Test Suite (PowerShell)
# Automated security testing script for production website
# Run from project root: .\tests\security-tests.ps1

Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "X4O Website - Security Test Suite" -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Test Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "Target: https://x4o.co.za"
Write-Host ""

# Test counters
$TotalTests = 0
$PassedTests = 0
$FailedTests = 0

# Test result function
function Test-Result {
    param(
        [bool]$Passed,
        [string]$Message
    )

    $script:TotalTests++

    if ($Passed) {
        Write-Host "[PASS] " -ForegroundColor Green -NoNewline
        Write-Host $Message
        $script:PassedTests++
    } else {
        Write-Host "[FAIL] " -ForegroundColor Red -NoNewline
        Write-Host $Message
        $script:FailedTests++
    }
}

Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-001: Dependency Vulnerability Scan"
Write-Host "------------------------------------------------------------------------"
try {
    $auditResult = npm audit --json 2>&1 | ConvertFrom-Json
    $vulnCount = $auditResult.metadata.vulnerabilities.total

    if ($vulnCount -eq 0) {
        Test-Result $true "SEC-001: No dependency vulnerabilities found"
    } else {
        Test-Result $false "SEC-001: Found $vulnCount vulnerabilities in dependencies"
    }
} catch {
    Write-Host "[SKIP] npm audit failed or npm not available" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-002: HTTPS Enforcement"
Write-Host "------------------------------------------------------------------------"
try {
    $httpResponse = Invoke-WebRequest -Uri "http://x4o.co.za" -MaximumRedirection 0 -ErrorAction SilentlyContinue
    if ($httpResponse -and ($httpResponse.StatusCode -eq 301 -or $httpResponse.StatusCode -eq 302)) {
        $location = $httpResponse.Headers['Location']
        if ($location -like "https://*") {
            Test-Result $true "SEC-002: HTTP to HTTPS redirect working (Status: $($httpResponse.StatusCode))"
        } else {
            Test-Result $false "SEC-002: Redirect exists but not to HTTPS"
        }
    } else {
        Test-Result $false "SEC-002: No redirect detected"
    }
} catch {
    # PowerShell treats 3xx as errors, check if it's actually a redirect
    if ($_.Exception.Message -like "*301*" -or $_.Exception.Message -like "*redirect*") {
        Test-Result $true "SEC-002: HTTP to HTTPS redirect working"
    } else {
        Test-Result $false "SEC-002: HTTP redirect check failed"
    }
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-004: X-Frame-Options Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $xframe = $response.Headers['X-Frame-Options']

    if ($xframe) {
        Test-Result $true "SEC-004: X-Frame-Options header present ($xframe)"
    } else {
        Test-Result $false "SEC-004: X-Frame-Options header MISSING"
    }
} catch {
    Test-Result $false "SEC-004: Unable to check X-Frame-Options header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-005: Content-Security-Policy Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $csp = $response.Headers['Content-Security-Policy']

    if ($csp) {
        Test-Result $true "SEC-005: Content-Security-Policy header present"
    } else {
        Test-Result $false "SEC-005: Content-Security-Policy header MISSING"
    }
} catch {
    Test-Result $false "SEC-005: Unable to check CSP header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-006: X-Content-Type-Options Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $xcontent = $response.Headers['X-Content-Type-Options']

    if ($xcontent) {
        Test-Result $true "SEC-006: X-Content-Type-Options header present ($xcontent)"
    } else {
        Test-Result $false "SEC-006: X-Content-Type-Options header MISSING"
    }
} catch {
    Test-Result $false "SEC-006: Unable to check X-Content-Type-Options header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-007: X-XSS-Protection Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $xxss = $response.Headers['X-XSS-Protection']

    if ($xxss) {
        Test-Result $true "SEC-007: X-XSS-Protection header present ($xxss)"
    } else {
        Test-Result $false "SEC-007: X-XSS-Protection header MISSING"
    }
} catch {
    Test-Result $false "SEC-007: Unable to check X-XSS-Protection header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-008: Referrer-Policy Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $referrer = $response.Headers['Referrer-Policy']

    if ($referrer) {
        Test-Result $true "SEC-008: Referrer-Policy header present ($referrer)"
    } else {
        Test-Result $false "SEC-008: Referrer-Policy header MISSING"
    }
} catch {
    Test-Result $false "SEC-008: Unable to check Referrer-Policy header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-009: Permissions-Policy Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $permissions = $response.Headers['Permissions-Policy']

    if ($permissions) {
        Test-Result $true "SEC-009: Permissions-Policy header present"
    } else {
        Test-Result $false "SEC-009: Permissions-Policy header MISSING"
    }
} catch {
    Test-Result $false "SEC-009: Unable to check Permissions-Policy header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-010: HSTS Header"
Write-Host "------------------------------------------------------------------------"
try {
    $response = Invoke-WebRequest -Uri "https://x4o.co.za" -UseBasicParsing
    $hsts = $response.Headers['Strict-Transport-Security']

    if ($hsts) {
        Test-Result $true "SEC-010: HSTS header present ($hsts)"
    } else {
        Test-Result $false "SEC-010: HSTS header MISSING"
    }
} catch {
    Test-Result $false "SEC-010: Unable to check HSTS header"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-029: DNS A Record Configuration"
Write-Host "------------------------------------------------------------------------"
try {
    $dnsResult = Resolve-DnsName -Name "x4o.co.za" -Type A -ErrorAction Stop
    $aRecord = $dnsResult | Where-Object { $_.Type -eq 'A' } | Select-Object -First 1 -ExpandProperty IPAddress

    if ($aRecord) {
        Test-Result $true "SEC-029: A record points to $aRecord"
    } else {
        Test-Result $false "SEC-029: Unable to resolve A record"
    }
} catch {
    Test-Result $false "SEC-029: DNS resolution failed"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-030: DNS CNAME Configuration"
Write-Host "------------------------------------------------------------------------"
try {
    $cnameResult = Resolve-DnsName -Name "www.x4o.co.za" -Type CNAME -ErrorAction Stop
    $cname = $cnameResult | Where-Object { $_.Type -eq 'CNAME' } | Select-Object -First 1 -ExpandProperty NameHost

    if ($cname) {
        Test-Result $true "SEC-030: CNAME www.x4o.co.za -> $cname"
    } else {
        Test-Result $false "SEC-030: CNAME not found or misconfigured"
    }
} catch {
    Test-Result $false "SEC-030: CNAME resolution failed"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-031: WWW to Non-WWW Redirect"
Write-Host "------------------------------------------------------------------------"
try {
    $wwwResponse = Invoke-WebRequest -Uri "https://www.x4o.co.za" -MaximumRedirection 0 -ErrorAction SilentlyContinue
    if ($wwwResponse -and $wwwResponse.StatusCode -eq 301) {
        $location = $wwwResponse.Headers['Location']
        if ($location -eq "https://x4o.co.za/" -or $location -like "https://x4o.co.za/*") {
            Test-Result $true "SEC-031: WWW redirects with 301 (Permanent) to $location"
        } else {
            Test-Result $false "SEC-031: Redirect exists but to wrong location: $location"
        }
    } else {
        Test-Result $false "SEC-031: No 301 redirect detected"
    }
} catch {
    # PowerShell treats 3xx as errors, check if it's actually a redirect
    if ($_.Exception.Message -like "*301*" -or $_.Exception.Message -like "*Moved*") {
        Test-Result $true "SEC-031: WWW redirects with 301 (Permanent)"
    } else {
        Test-Result $false "SEC-031: WWW redirect check failed"
    }
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-032: MX Records Email Security"
Write-Host "------------------------------------------------------------------------"
try {
    $mxRecords = Resolve-DnsName -Name "x4o.co.za" -Type MX -ErrorAction Stop
    $googleMx = $mxRecords | Where-Object { $_.NameExchange -like "*google.com*" }

    if ($googleMx) {
        Test-Result $true "SEC-032: Google Workspace MX records configured"
    } else {
        Test-Result $false "SEC-032: MX records not properly configured"
    }
} catch {
    Test-Result $false "SEC-032: MX record resolution failed"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-044: robots.txt Presence"
Write-Host "------------------------------------------------------------------------"
try {
    $robotsResponse = Invoke-WebRequest -Uri "https://x4o.co.za/robots.txt" -UseBasicParsing

    if ($robotsResponse.StatusCode -eq 200) {
        Test-Result $true "SEC-044: robots.txt file exists"
    } else {
        Test-Result $false "SEC-044: robots.txt file NOT FOUND (Status: $($robotsResponse.StatusCode))"
    }
} catch {
    Test-Result $false "SEC-044: robots.txt file NOT FOUND"
}

Write-Host ""
Write-Host "------------------------------------------------------------------------"
Write-Host "SEC-045: sitemap.xml Presence"
Write-Host "------------------------------------------------------------------------"
try {
    $sitemapResponse = Invoke-WebRequest -Uri "https://x4o.co.za/sitemap.xml" -UseBasicParsing

    if ($sitemapResponse.StatusCode -eq 200) {
        Test-Result $true "SEC-045: sitemap.xml file exists"
    } else {
        Test-Result $false "SEC-045: sitemap.xml file NOT FOUND (Status: $($sitemapResponse.StatusCode))"
    }
} catch {
    Test-Result $false "SEC-045: sitemap.xml file NOT FOUND"
}

Write-Host ""
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "Test Summary" -ForegroundColor Cyan
Write-Host "========================================================================" -ForegroundColor Cyan
Write-Host "Total Tests:  $TotalTests"
Write-Host "Passed:       " -NoNewline
Write-Host "$PassedTests" -ForegroundColor Green
Write-Host "Failed:       " -NoNewline
Write-Host "$FailedTests" -ForegroundColor Red

$PassRate = [math]::Round(($PassedTests / $TotalTests) * 100, 2)
Write-Host "Pass Rate:    $PassRate%"
Write-Host ""

if ($FailedTests -eq 0) {
    Write-Host "All security tests PASSED!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "Some security tests FAILED. Review results above." -ForegroundColor Yellow
    exit 1
}
