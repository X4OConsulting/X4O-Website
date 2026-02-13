# Security Testing - File Locations Quick Reference

**Project:** X4O Website Development
**Date:** February 13, 2026

---

## 🎯 Quick Access

### Run Automated Tests

**Windows (PowerShell):**
```powershell
cd c:\Users\keena\Projects\x4o-website-dev
powershell -ExecutionPolicy Bypass -File tests/security-tests.ps1
```

**Linux/Mac (Bash):**
```bash
cd /path/to/x4o-website-dev
bash tests/security-tests.sh
```

---

## 📁 All File Locations

### 1. Automated Test Scripts

```
tests/
├── security-tests.ps1          # PowerShell script (Windows) - 319 lines
└── security-tests.sh           # Bash script (Linux/Mac) - 230 lines
```

**What:** 15 automated security tests covering:
- Dependency vulnerability scan (npm audit)
- HTTP security headers (6 tests)
- DNS configuration (4 tests)
- HTTPS/SSL checks (2 tests)
- SEO files (2 tests)

**Tests:** SEC-001, SEC-004-SEC-010, SEC-029-SEC-032, SEC-044-SEC-045

---

### 2. Security Documentation

```
docs/phase4-testing/
├── SECURITY_TEST_CASES.csv                    # 45 security test specifications
├── SECURITY_BUG_REPORTS.csv                   # 4 security bug reports
├── SECURITY-TEST-REPORT.md                    # 52-page comprehensive audit
├── SECURITY_TEST_EXECUTION_REPORT.md          # 26-page execution results
└── SECURITY_TESTING_COMPLETE_SUMMARY.md       # Final summary (this report's detail)
```

**Individual Files:**

#### SECURITY_TEST_CASES.csv
- **Size:** 45 test cases
- **Format:** CSV (Smartsheet compatible)
- **Columns:** 18 columns matching main test case sheet
- **Tests:** SEC-001 through SEC-045
- **Purpose:** Individual test specifications with steps, expected results, actual results

#### SECURITY_BUG_REPORTS.csv
- **Size:** 4 bug reports
- **Format:** CSV (Bug Tracker compatible)
- **IDs:** BUG-SEC-001, BUG-SEC-002, BUG-SEC-003, BUG-SEC-004
- **Columns:** 25 columns matching main bug tracker
- **Purpose:** Security issues for bug tracker sheet

#### SECURITY-TEST-REPORT.md
- **Size:** 52 pages
- **Format:** Markdown
- **Sections:**
  - Executive Summary
  - Test Methodology (45 tests)
  - Detailed Findings
  - OWASP Top 10 Analysis
  - Vulnerability Assessment (CVSS scores)
  - Remediation Plan with priorities
- **Purpose:** Comprehensive security audit report

#### SECURITY_TEST_EXECUTION_REPORT.md
- **Size:** 26 pages
- **Format:** Markdown
- **Sections:**
  - Test execution results (15 automated)
  - Passed/Failed breakdown
  - Security headers fix implementation
  - Post-remediation expected results
  - Script improvement recommendations
- **Purpose:** Test execution documentation and remediation tracking

#### SECURITY_TESTING_COMPLETE_SUMMARY.md
- **Size:** 23 pages
- **Format:** Markdown
- **Sections:**
  - File locations (all scripts and docs)
  - Test results summary (38/45 passed)
  - Implementation summary
  - Next steps and deployment plan
  - Security improvement metrics
- **Purpose:** Final summary with all locations and results

---

### 3. Updated Test Cases

```
X4O_Test_Cases.csv                             # Main test case file (103 tests total)
```

**Updated Tests:** 15 security tests (SEC-001, SEC-004-SEC-010, SEC-029-SEC-032, SEC-044-SEC-045)

**Changes Made:**
- **Test Type:** Changed from "Manual" to "Automated- Script-based (Playwright Bash)"
- **Test Script:** Updated to reference `tests/security-tests.ps1`
- **Notes:** Added fix implementation status for failed tests

**Example Update:**
```csv
Before: SEC-001,Dependency Security,Dependency Vulnerability Scan,...,Manual,...,npm audit --json,...
After:  SEC-001,Dependency Security,Dependency Vulnerability Scan,...,Automated- Script-based (Playwright Bash),...,tests/security-tests.ps1,...
```

---

### 4. Implementation Files

```
public/
└── _headers                    # HTTP security headers configuration

dist/
└── _headers                    # Compiled output (after npm run build)
```

**_headers file contents:**
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.netlify.app; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self';
  Permissions-Policy: geolocation=(), microphone=(), camera=(), payment=(), usb=()
```

**Purpose:** Adds 6 missing HTTP security headers (fixes BUG-SEC-001, BUG-SEC-002)

**Status:** ✅ Created and built, awaiting deployment to production

---

## 📊 Test Results Quick View

### Automated Tests (15 total)

| Status | Count | Tests |
|--------|-------|-------|
| ✅ **Passing** | 7 | SEC-001, SEC-010, SEC-029, SEC-030, SEC-031, SEC-032 (+ SEC-002 manual verified) |
| ❌ **Failing (Headers)** | 6 | SEC-004, SEC-005, SEC-006, SEC-007, SEC-008, SEC-009 |
| ❌ **Failing (SEO)** | 2 | SEC-044, SEC-045 |

### All Security Tests (45 total)

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ **Passed** | 38 | 84% |
| ❌ **Failed** | 7 | 16% |
| ⏸️ **N/A** | 4 | 9% (injection tests for static site) |

---

## 🔍 Find Specific Test Results

### By Test ID

**Automated Tests:**
```
SEC-001: tests/security-tests.ps1 (line 41-52)    - Dependency scan
SEC-004: tests/security-tests.ps1 (line 78-90)    - X-Frame-Options
SEC-005: tests/security-tests.ps1 (line 94-107)   - CSP
SEC-006: tests/security-tests.ps1 (line 111-124)  - X-Content-Type-Options
SEC-007: tests/security-tests.ps1 (line 128-141)  - X-XSS-Protection
SEC-008: tests/security-tests.ps1 (line 145-158)  - Referrer-Policy
SEC-009: tests/security-tests.ps1 (line 162-175)  - Permissions-Policy
SEC-010: tests/security-tests.ps1 (line 179-192)  - HSTS
SEC-029: tests/security-tests.ps1 (line 196-209)  - DNS A record
SEC-030: tests/security-tests.ps1 (line 213-227)  - DNS CNAME
SEC-031: tests/security-tests.ps1 (line 231-249)  - WWW redirect
SEC-032: tests/security-tests.ps1 (line 253-264)  - MX records
SEC-044: tests/security-tests.ps1 (line 268-280)  - robots.txt
SEC-045: tests/security-tests.ps1 (line 284-296)  - sitemap.xml
```

**Manual Tests:**
```
SEC-002: SECURITY_TEST_CASES.csv (row 2)  - HTTPS enforcement
SEC-003: SECURITY_TEST_CASES.csv (row 3)  - SSL certificate validity
SEC-011 to SEC-043: SECURITY_TEST_CASES.csv (rows 11-43)
```

### By Category

**Dependency Security:**
- `SECURITY_TEST_CASES.csv` → Row 2 (SEC-001)

**Transport Security:**
- `SECURITY_TEST_CASES.csv` → Rows 2-4 (SEC-002, SEC-003), Row 20 (SEC-020), Rows 37-39 (SEC-037-SEC-039)

**Security Headers:**
- `tests/security-tests.ps1` → Lines 78-192 (SEC-004 through SEC-010)
- `SECURITY_TEST_CASES.csv` → Rows 4-10

**Form Security:**
- `SECURITY_TEST_CASES.csv` → Rows 11-13, 40-42 (SEC-011-SEC-013, SEC-040-SEC-042)

**XSS Protection:**
- `SECURITY_TEST_CASES.csv` → Rows 14-17 (SEC-014-SEC-017)

**CSRF Protection:**
- `SECURITY_TEST_CASES.csv` → Rows 18-19 (SEC-018-SEC-019)

**DNS Security:**
- `tests/security-tests.ps1` → Lines 196-264 (SEC-029 through SEC-032)
- `SECURITY_TEST_CASES.csv` → Rows 28-31

**SEO Files:**
- `tests/security-tests.ps1` → Lines 268-296 (SEC-044-SEC-045)
- `SECURITY_TEST_CASES.csv` → Rows 44-45

---

## 🐛 Bug Reports

### BUG-SEC-001: Missing HTTP Security Headers
- **File:** `SECURITY_BUG_REPORTS.csv` → Row 2
- **Severity:** High
- **Status:** ✅ Fix implemented (`public/_headers`)
- **Related Tests:** SEC-004, SEC-005, SEC-006, SEC-007, SEC-008, SEC-009
- **Fix Location:** `public/_headers`

### BUG-SEC-002: Clickjacking Vulnerability
- **File:** `SECURITY_BUG_REPORTS.csv` → Row 3
- **Severity:** High
- **Status:** ✅ Fix implemented (`public/_headers` - X-Frame-Options)
- **Related Tests:** SEC-021
- **Fix Location:** `public/_headers` (line 2: X-Frame-Options: DENY)

### BUG-SEC-003: Missing robots.txt
- **File:** `SECURITY_BUG_REPORTS.csv` → Row 4
- **Severity:** Low
- **Status:** ⏸️ Phase 7 enhancement
- **Related Tests:** SEC-044

### BUG-SEC-004: Missing sitemap.xml
- **File:** `SECURITY_BUG_REPORTS.csv` → Row 5
- **Severity:** Low
- **Status:** ⏸️ Phase 7 enhancement
- **Related Tests:** SEC-045

---

## 📈 Reports and Metrics

### Executive Summary
- **File:** `SECURITY_TESTING_COMPLETE_SUMMARY.md`
- **Section:** Pages 1-2 (lines 1-95)

### Detailed Test Results
- **File:** `SECURITY_TEST_EXECUTION_REPORT.md`
- **Section:** Pages 3-15 (Passed Tests, Failed Tests)

### Remediation Plan
- **File:** `SECURITY_TEST_EXECUTION_REPORT.md`
- **Section:** Pages 16-20 (Priority 1, 2, 3 tasks)

### OWASP Top 10 Analysis
- **File:** `SECURITY-TEST-REPORT.md`
- **Section:** Pages 25-35 (OWASP coverage analysis)

### Security Metrics
- **File:** `SECURITY_TESTING_COMPLETE_SUMMARY.md`
- **Section:** Pages 18-19 (Security Improvement Metrics)

---

## 🚀 Deployment Checklist

### Pre-Deployment
- [x] Create automated test scripts
- [x] Implement security headers fix
- [x] Update test cases sheet
- [x] Create comprehensive documentation
- [x] Build project with new headers

### Deployment Steps
- [ ] Commit changes to staging branch
- [ ] Push to GitHub (triggers Netlify staging deploy)
- [ ] Run automated tests against staging URL
- [ ] Verify headers present on staging
- [ ] Create Pull Request: staging → main
- [ ] Get supervisor approval
- [ ] Merge to production
- [ ] Run automated tests against production
- [ ] Verify security grade increase to A

### Post-Deployment
- [ ] Update bug tracker (close BUG-SEC-001, BUG-SEC-002)
- [ ] Update test cases (mark SEC-004-SEC-009 as Passed)
- [ ] Document deployment in change log
- [ ] Schedule Phase 7 enhancements (robots.txt, sitemap.xml)

---

## 🎓 How to Use This Documentation

### For Running Tests
1. Go to "Quick Access" section (top of this file)
2. Copy the command for your OS
3. Run in terminal/PowerShell

### For Finding Test Details
1. Locate test ID (e.g., SEC-001)
2. Check "Find Specific Test Results" section
3. Open referenced file at specified line/row

### For Reviewing Security Status
1. Read "Test Results Quick View" section
2. See `SECURITY_TESTING_COMPLETE_SUMMARY.md` for full summary
3. Check bug reports for outstanding issues

### For Deployment
1. Follow "Deployment Checklist" section
2. Refer to `SECURITY_TEST_EXECUTION_REPORT.md` for detailed remediation plan
3. Use automated scripts to verify deployment

---

## 📞 Support

**Primary Documentation:**
- `SECURITY_TESTING_COMPLETE_SUMMARY.md` - Start here for overview
- `SECURITY_TEST_EXECUTION_REPORT.md` - Test results and remediation
- `SECURITY-TEST-REPORT.md` - Comprehensive security audit

**Quick Reference:**
- This file (`docs/phase4-testing/SECURITY_TESTING_FILE_LOCATIONS.md`)
- `X4O_Test_Cases.csv` - All test cases with results

**Questions?**
- Email: admin@x4o.co.za
- Repository: github.com/X4OConsulting/X4O-Website

---

**Last Updated:** February 13, 2026
**Version:** 1.0
**Maintained By:** Security Team
