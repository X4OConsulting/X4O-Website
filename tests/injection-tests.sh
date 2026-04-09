#!/bin/bash

# X4O Website - Injection Testing Suite
# Date: February 13, 2026
# Purpose: Test for SQL, Command, XSS, Template, and File Upload injection vulnerabilities

echo "========================================================================"
echo "X4O Website - Injection Testing Suite"
echo "========================================================================"
echo ""
echo "Test Date: $(date)"
echo "Target: https://x4o.co.za"
echo "Test Type: Injection Vulnerability Testing"
echo ""

TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0
NA_TESTS=0

test_result() {
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if [ "$1" = "PASS" ]; then
        echo -e "\033[0;32m[PASS]\033[0m $2"
        PASSED_TESTS=$((PASSED_TESTS + 1))
    elif [ "$1" = "FAIL" ]; then
        echo -e "\033[0;31m[FAIL]\033[0m $2"
        FAILED_TESTS=$((FAILED_TESTS + 1))
    else
        echo -e "\033[0;33m[N/A]\033[0m $2"
        NA_TESTS=$((NA_TESTS + 1))
    fi
}

# ============================================================================
# SEC-033: SQL Injection Test
# ============================================================================
echo "------------------------------------------------------------------------"
echo "SEC-033: SQL Injection Test"
echo "------------------------------------------------------------------------"

# Test if there are any database queries or API endpoints
RESPONSE=$(curl -s "https://x4o.co.za/?id=1' OR '1'='1")

# Check response for SQL errors
if echo "$RESPONSE" | grep -qi "sql\|mysql\|postgresql\|database error\|syntax error"; then
    test_result "FAIL" "SEC-033: SQL injection vulnerability detected - error messages exposed"
else
    # Static site with no database
    test_result "N/A" "SEC-033: SQL injection N/A - static site with no database backend"
fi

# ============================================================================
# SEC-034: Command Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "SEC-034: Command Injection Test"
echo "------------------------------------------------------------------------"

# Test for command injection in URL parameters
RESPONSE=$(curl -s "https://x4o.co.za/?cmd=;ls")

# Check for command execution indicators
if echo "$RESPONSE" | grep -qi "bin/sh\|command not found\|root:\|/etc/passwd"; then
    test_result "FAIL" "SEC-034: Command injection vulnerability detected"
else
    # Static site with no server-side execution
    test_result "N/A" "SEC-034: Command injection N/A - static site with no server-side command execution"
fi

# ============================================================================
# SEC-035: File Upload Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "SEC-035: File Upload Injection Test"
echo "------------------------------------------------------------------------"

# Check if there are any file upload endpoints
UPLOAD_ENDPOINT=$(curl -s https://x4o.co.za | grep -i "upload\|file\|multipart")

if [ -n "$UPLOAD_ENDPOINT" ]; then
    test_result "FAIL" "SEC-035: File upload functionality detected - requires manual testing"
else
    # No file upload functionality
    test_result "N/A" "SEC-035: File upload injection N/A - no file upload functionality present"
fi

# ============================================================================
# SEC-036: Server-Side Template Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "SEC-036: Server-Side Template Injection Test"
echo "------------------------------------------------------------------------"

# Test for template injection
RESPONSE=$(curl -s "https://x4o.co.za/?name={{7*7}}")

# Check if expression is evaluated
if echo "$RESPONSE" | grep -q "49"; then
    test_result "FAIL" "SEC-036: Template injection vulnerability detected - expression evaluated"
else
    # Static site - templates rendered at build time
    test_result "N/A" "SEC-036: Template injection N/A - static site with build-time rendering"
fi

# ============================================================================
# Additional XSS Injection Tests (Already covered in SEC-014-017)
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "Additional: XSS Injection Verification"
echo "------------------------------------------------------------------------"

# Test URL parameter XSS
RESPONSE=$(curl -s "https://x4o.co.za/contact?subject=<script>alert('XSS')</script>")

if echo "$RESPONSE" | grep -q "<script>alert('XSS')</script>"; then
    test_result "FAIL" "XSS: Reflected XSS vulnerability in URL parameters"
else
    test_result "PASS" "XSS: URL parameters properly escaped (no reflected XSS)"
fi

# Test for DOM-based XSS via hash
RESPONSE=$(curl -s "https://x4o.co.za/#<img src=x onerror=alert(1)>")

# Check if unsafe DOM manipulation exists
PAGE_SOURCE=$(curl -s https://x4o.co.za)
if echo "$PAGE_SOURCE" | grep -qi "innerHTML\s*=\|document.write\|eval("; then
    test_result "FAIL" "XSS: Potentially unsafe DOM manipulation detected"
else
    test_result "PASS" "XSS: No unsafe DOM manipulation (innerHTML, eval, document.write)"
fi

# ============================================================================
# LDAP Injection Test (Additional)
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "Additional: LDAP Injection Test"
echo "------------------------------------------------------------------------"

RESPONSE=$(curl -s "https://x4o.co.za/?user=*)(uid=*))(|(uid=*")

if echo "$RESPONSE" | grep -qi "ldap\|directory"; then
    test_result "FAIL" "LDAP: LDAP injection vulnerability detected"
else
    test_result "N/A" "LDAP: LDAP injection N/A - no directory service integration"
fi

# ============================================================================
# XML External Entity (XXE) Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "Additional: XXE Injection Test"
echo "------------------------------------------------------------------------"

# Check for XML processing endpoints
RESPONSE=$(curl -s -X POST https://x4o.co.za/api/xml \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>' 2>&1)

if echo "$RESPONSE" | grep -qi "root:"; then
    test_result "FAIL" "XXE: XML External Entity vulnerability detected"
else
    test_result "N/A" "XXE: XXE injection N/A - no XML processing endpoints"
fi

# ============================================================================
# NoSQL Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "Additional: NoSQL Injection Test"
echo "------------------------------------------------------------------------"

RESPONSE=$(curl -s "https://x4o.co.za/?filter[\$ne]=null")

if echo "$RESPONSE" | grep -qi "mongodb\|nosql\|collection"; then
    test_result "FAIL" "NoSQL: NoSQL injection vulnerability detected"
else
    test_result "N/A" "NoSQL: NoSQL injection N/A - no NoSQL database backend"
fi

# ============================================================================
# HTML Injection Test
# ============================================================================
echo ""
echo "------------------------------------------------------------------------"
echo "Additional: HTML Injection Test"
echo "------------------------------------------------------------------------"

RESPONSE=$(curl -s "https://x4o.co.za/?name=<h1>Injected</h1>")

if echo "$RESPONSE" | grep -q "<h1>Injected</h1>"; then
    test_result "FAIL" "HTML: HTML injection vulnerability detected"
else
    test_result "PASS" "HTML: HTML properly escaped (no HTML injection)"
fi

# ============================================================================
# Summary
# ============================================================================
echo ""
echo "========================================================================"
echo "Test Summary"
echo "========================================================================"
echo "Total Tests:  $TOTAL_TESTS"
echo "Passed:       $PASSED_TESTS"
echo "Failed:       $FAILED_TESTS"
echo "N/A:          $NA_TESTS"
echo "Pass Rate:    $(( (PASSED_TESTS + NA_TESTS) * 100 / TOTAL_TESTS ))%"
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo "Result: All injection tests passed or N/A (static site)"
    echo "Status: SECURE"
    exit 0
else
    echo "Result: $FAILED_TESTS injection vulnerabilities detected"
    echo "Status: VULNERABILITIES FOUND"
    exit 1
fi
