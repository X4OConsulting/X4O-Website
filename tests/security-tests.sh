#!/bin/bash

# X4O Website - Security Test Suite
# Automated security testing script for production website
# Run from project root: bash tests/security-tests.sh

echo "========================================================================"
echo "X4O Website - Security Test Suite"
echo "========================================================================"
echo ""
echo "Test Date: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Target: https://x4o.co.za"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

# Test result function
test_result() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}[PASS]${NC} $2"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    else
        echo -e "${RED}[FAIL]${NC} $2"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
}

echo "------------------------------------------------------------------------"
echo "SEC-001: Dependency Vulnerability Scan"
echo "------------------------------------------------------------------------"
if command -v npm &> /dev/null; then
    npm audit --json > security-audit-result.json 2>&1
    VULN_COUNT=$(grep -o '"total":[0-9]*' security-audit-result.json | tail -1 | grep -o '[0-9]*')
    if [ "$VULN_COUNT" = "0" ]; then
        test_result 0 "SEC-001: No dependency vulnerabilities found"
    else
        test_result 1 "SEC-001: Found $VULN_COUNT vulnerabilities in dependencies"
    fi
else
    echo -e "${YELLOW}[SKIP]${NC} npm not available"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-002: HTTPS Enforcement"
echo "------------------------------------------------------------------------"
HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://x4o.co.za)
if [ "$HTTP_RESPONSE" = "301" ] || [ "$HTTP_RESPONSE" = "302" ]; then
    test_result 0 "SEC-002: HTTP to HTTPS redirect working (Status: $HTTP_RESPONSE)"
else
    test_result 1 "SEC-002: HTTP redirect failed (Status: $HTTP_RESPONSE)"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-003: SSL Certificate Validity"
echo "------------------------------------------------------------------------"
if command -v openssl &> /dev/null; then
    CERT_EXPIRY=$(echo | openssl s_client -servername x4o.co.za -connect x4o.co.za:443 2>/dev/null | openssl x509 -noout -enddate 2>/dev/null | cut -d= -f2)
    if [ -n "$CERT_EXPIRY" ]; then
        test_result 0 "SEC-003: Valid SSL certificate (Expires: $CERT_EXPIRY)"
    else
        test_result 1 "SEC-003: Unable to verify SSL certificate"
    fi
else
    echo -e "${YELLOW}[SKIP]${NC} openssl not available"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-004: X-Frame-Options Header"
echo "------------------------------------------------------------------------"
XFRAME=$(curl -s -I https://x4o.co.za | grep -i "x-frame-options")
if [ -n "$XFRAME" ]; then
    test_result 0 "SEC-004: X-Frame-Options header present ($XFRAME)"
else
    test_result 1 "SEC-004: X-Frame-Options header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-005: Content-Security-Policy Header"
echo "------------------------------------------------------------------------"
CSP=$(curl -s -I https://x4o.co.za | grep -i "content-security-policy")
if [ -n "$CSP" ]; then
    test_result 0 "SEC-005: Content-Security-Policy header present"
else
    test_result 1 "SEC-005: Content-Security-Policy header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-006: X-Content-Type-Options Header"
echo "------------------------------------------------------------------------"
XCONTENT=$(curl -s -I https://x4o.co.za | grep -i "x-content-type-options")
if [ -n "$XCONTENT" ]; then
    test_result 0 "SEC-006: X-Content-Type-Options header present"
else
    test_result 1 "SEC-006: X-Content-Type-Options header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-007: X-XSS-Protection Header"
echo "------------------------------------------------------------------------"
XXSS=$(curl -s -I https://x4o.co.za | grep -i "x-xss-protection")
if [ -n "$XXSS" ]; then
    test_result 0 "SEC-007: X-XSS-Protection header present"
else
    test_result 1 "SEC-007: X-XSS-Protection header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-008: Referrer-Policy Header"
echo "------------------------------------------------------------------------"
REFERRER=$(curl -s -I https://x4o.co.za | grep -i "referrer-policy")
if [ -n "$REFERRER" ]; then
    test_result 0 "SEC-008: Referrer-Policy header present"
else
    test_result 1 "SEC-008: Referrer-Policy header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-009: Permissions-Policy Header"
echo "------------------------------------------------------------------------"
PERMISSIONS=$(curl -s -I https://x4o.co.za | grep -i "permissions-policy")
if [ -n "$PERMISSIONS" ]; then
    test_result 0 "SEC-009: Permissions-Policy header present"
else
    test_result 1 "SEC-009: Permissions-Policy header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-010: HSTS Header"
echo "------------------------------------------------------------------------"
HSTS=$(curl -s -I https://x4o.co.za | grep -i "strict-transport-security")
if [ -n "$HSTS" ]; then
    test_result 0 "SEC-010: HSTS header present ($HSTS)"
else
    test_result 1 "SEC-010: HSTS header MISSING"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-020: Mixed Content Check"
echo "------------------------------------------------------------------------"
MIXED_HTTP=$(curl -s https://x4o.co.za | grep -o 'http://[^"]*' | grep -v 'http://www.w3.org')
if [ -z "$MIXED_HTTP" ]; then
    test_result 0 "SEC-020: No HTTP resources found on HTTPS page"
else
    test_result 1 "SEC-020: Found HTTP resources: $MIXED_HTTP"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-029: DNS A Record Configuration"
echo "------------------------------------------------------------------------"
if command -v nslookup &> /dev/null; then
    A_RECORD=$(nslookup x4o.co.za 2>/dev/null | grep "Address:" | tail -1 | awk '{print $2}')
    if [ -n "$A_RECORD" ]; then
        test_result 0 "SEC-029: A record points to $A_RECORD"
    else
        test_result 1 "SEC-029: Unable to resolve A record"
    fi
else
    echo -e "${YELLOW}[SKIP]${NC} nslookup not available"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-030: DNS CNAME Configuration"
echo "------------------------------------------------------------------------"
if command -v nslookup &> /dev/null; then
    CNAME=$(nslookup www.x4o.co.za 2>/dev/null | grep "canonical name" | awk '{print $NF}')
    if [ -n "$CNAME" ]; then
        test_result 0 "SEC-030: CNAME www.x4o.co.za -> $CNAME"
    else
        test_result 1 "SEC-030: CNAME not found or misconfigured"
    fi
else
    echo -e "${YELLOW}[SKIP]${NC} nslookup not available"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-031: WWW to Non-WWW Redirect"
echo "------------------------------------------------------------------------"
WWW_REDIRECT=$(curl -s -o /dev/null -w "%{http_code}" https://www.x4o.co.za)
if [ "$WWW_REDIRECT" = "301" ]; then
    test_result 0 "SEC-031: WWW redirects with 301 (Permanent)"
else
    test_result 1 "SEC-031: WWW redirect failed or not 301 (Got: $WWW_REDIRECT)"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-032: MX Records Email Security"
echo "------------------------------------------------------------------------"
if command -v nslookup &> /dev/null; then
    MX_RECORDS=$(nslookup -type=MX x4o.co.za 2>/dev/null | grep "mail exchanger")
    if echo "$MX_RECORDS" | grep -q "ASPMX.L.GOOGLE.COM"; then
        test_result 0 "SEC-032: Google Workspace MX records configured"
    else
        test_result 1 "SEC-032: MX records not properly configured"
    fi
else
    echo -e "${YELLOW}[SKIP]${NC} nslookup not available"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-044: robots.txt Presence"
echo "------------------------------------------------------------------------"
ROBOTS_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://x4o.co.za/robots.txt)
if [ "$ROBOTS_STATUS" = "200" ]; then
    test_result 0 "SEC-044: robots.txt file exists"
else
    test_result 1 "SEC-044: robots.txt file NOT FOUND (Status: $ROBOTS_STATUS)"
fi

echo ""
echo "------------------------------------------------------------------------"
echo "SEC-045: sitemap.xml Presence"
echo "------------------------------------------------------------------------"
SITEMAP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://x4o.co.za/sitemap.xml)
if [ "$SITEMAP_STATUS" = "200" ]; then
    test_result 0 "SEC-045: sitemap.xml file exists"
else
    test_result 1 "SEC-045: sitemap.xml file NOT FOUND (Status: $SITEMAP_STATUS)"
fi

echo ""
echo "========================================================================"
echo "Test Summary"
echo "========================================================================"
echo "Total Tests:  $TOTAL_TESTS"
echo -e "Passed:       ${GREEN}$PASSED_TESTS${NC}"
echo -e "Failed:       ${RED}$FAILED_TESTS${NC}"
PASS_RATE=$((PASSED_TESTS * 100 / TOTAL_TESTS))
echo "Pass Rate:    $PASS_RATE%"
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}All security tests PASSED!${NC}"
    exit 0
else
    echo -e "${YELLOW}Some security tests FAILED. Review results above.${NC}"
    exit 1
fi
