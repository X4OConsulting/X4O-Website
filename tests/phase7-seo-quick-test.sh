#!/bin/bash

##############################################################################
# Phase 7 SEO Quick Validation Script
# Tests robots.txt and sitemap.xml functionality
#
# Usage: ./tests/phase7-seo-quick-test.sh [URL]
# Example: ./tests/phase7-seo-quick-test.sh https://staging--x4oconsultants.netlify.app
#
# Date: February 16, 2026
##############################################################################

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default URL (can be overridden)
BASE_URL="${1:-http://localhost:4321}"

# Test counters
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║        Phase 7 SEO Quick Validation Test Suite          ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "Testing URL: ${YELLOW}$BASE_URL${NC}"
echo ""

# Function to run a test
run_test() {
    local test_name="$1"
    local test_command="$2"
    local expected_pattern="$3"

    ((TOTAL_TESTS++))
    echo -ne "Testing: $test_name ... "

    result=$(eval "$test_command" 2>&1)
    exit_code=$?

    if [ $exit_code -eq 0 ]; then
        if echo "$result" | grep -q "$expected_pattern"; then
            echo -e "${GREEN}✓ PASS${NC}"
            ((PASSED_TESTS++))
            return 0
        fi
    fi

    echo -e "${RED}✗ FAIL${NC}"
    echo -e "  Expected: $expected_pattern"
    echo -e "  Got: $result"
    ((FAILED_TESTS++))
    return 1
}

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " SEO Enhancement Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Test 1: robots.txt exists (HTTP 200)
run_test "P7-SEO-001: robots.txt exists" \
    "curl -s -o /dev/null -w '%{http_code}' $BASE_URL/robots.txt" \
    "200"

# Test 2: robots.txt contains User-agent
run_test "P7-SEO-002: robots.txt User-agent directive" \
    "curl -s $BASE_URL/robots.txt" \
    "User-agent: \\*"

# Test 3: robots.txt contains Allow directive
run_test "P7-SEO-002: robots.txt Allow directive" \
    "curl -s $BASE_URL/robots.txt" \
    "Allow: /"

# Test 4: robots.txt contains Sitemap URL
run_test "P7-SEO-002: robots.txt Sitemap reference" \
    "curl -s $BASE_URL/robots.txt" \
    "Sitemap:"

# Test 5: sitemap-index.xml exists (HTTP 200)
run_test "P7-SEO-003: sitemap-index.xml exists" \
    "curl -s -o /dev/null -w '%{http_code}' $BASE_URL/sitemap-index.xml" \
    "200"

# Test 6: sitemap-0.xml exists (HTTP 200)
run_test "P7-SEO-003: sitemap-0.xml exists" \
    "curl -s -o /dev/null -w '%{http_code}' $BASE_URL/sitemap-0.xml" \
    "200"

# Test 7: sitemap contains homepage
run_test "P7-SEO-004: sitemap contains homepage" \
    "curl -s $BASE_URL/sitemap-0.xml" \
    "<loc>https://x4o.co.za/</loc>"

# Test 8: sitemap contains contact page
run_test "P7-SEO-004: sitemap contains contact page" \
    "curl -s $BASE_URL/sitemap-0.xml" \
    "<loc>https://x4o.co.za/contact</loc>"

# Test 9: sitemap contains consulting page
run_test "P7-SEO-004: sitemap contains consulting page" \
    "curl -s $BASE_URL/sitemap-0.xml" \
    "consulting-and-advisory-services"

# Test 10: sitemap has valid XML namespace
run_test "P7-SEO-005: sitemap XML namespace" \
    "curl -s $BASE_URL/sitemap-0.xml" \
    "xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\""

# Test 11: sitemap has urlset element
run_test "P7-SEO-005: sitemap urlset element" \
    "curl -s $BASE_URL/sitemap-0.xml" \
    "<urlset"

# Test 12: sitemap Content-Type header
run_test "P7-SEO-006: sitemap Content-Type" \
    "curl -s -I $BASE_URL/sitemap-0.xml | grep -i content-type" \
    "application/xml\\|text/xml"

# Test 13: robots.txt Content-Type header
run_test "P7-SEO-001: robots.txt Content-Type" \
    "curl -s -I $BASE_URL/robots.txt | grep -i content-type" \
    "text/plain"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Test Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "Total Tests:  ${BLUE}$TOTAL_TESTS${NC}"
echo -e "Passed:       ${GREEN}$PASSED_TESTS${NC}"
echo -e "Failed:       ${RED}$FAILED_TESTS${NC}"
echo ""

PASS_RATE=$(awk "BEGIN {printf \"%.1f\", ($PASSED_TESTS/$TOTAL_TESTS)*100}")
echo -e "Pass Rate:    ${YELLOW}$PASS_RATE%${NC}"
echo ""

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║             ✓ ALL TESTS PASSED SUCCESSFULLY              ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    exit 0
else
    echo -e "${RED}╔══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║                  ✗ SOME TESTS FAILED                     ║${NC}"
    echo -e "${RED}╚══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "Please review failed tests above and fix issues before deployment."
    echo ""
    exit 1
fi
