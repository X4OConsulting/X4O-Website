# Phase 4 Testing Suite
## X4O Website - Testing Documentation

This directory contains automated and manual tests for the X4O website production environment.

---

## Test Reports (DOCX)

All test reports are located in `docs/phase4-testing/`:

1. `test-report-01-form-functionality.docx` - Contact form testing
2. `test-report-02-responsive-design.docx` - Responsive breakpoint testing
3. `test-report-03-maintenance-mode.docx` - Maintenance page testing
4. `test-report-04-branch-deploys.docx` - Git workflow testing
5. `test-report-05-dns-resolution.docx` - DNS and SSL testing
6. `test-report-06-cross-browser.docx` - Browser compatibility testing
7. `test-report-07-accessibility.docx` - WCAG 2.1 AA compliance testing
8. `test-report-08-lighthouse.docx` - Performance testing

**Total:** 8 test reports (301KB)

---

## Automated Tests

### 1. Playwright Tests (JavaScript)

**File:** `tests/form-functionality.spec.js`

**What it tests:**
- Form field presence and validation
- Query parameter pre-fill functionality
- Netlify Forms Integration
- Responsive design at multiple viewports
- Accessibility (ARIA, landmarks, alt text)
- Link validation
- Internal and external link security

**Prerequisites:**
```bash
# Install Playwright
npm install -D @playwright/test

# Install browsers
npx playwright install
```

**Run tests:**
```bash
# Run all tests
npx playwright test tests/form-functionality.spec.js

# Run with headed browser (see what's happening)
npx playwright test tests/form-functionality.spec.js --headed

# Run specific test
npx playwright test tests/form-functionality.spec.js -g "TC-FORM-001"

# Generate HTML report
npx playwright test tests/form-functionality.spec.js --reporter=html
```

**Test Coverage:**
- ✅ 8 Form Functionality tests
- ✅ 6 Responsive Design tests
- ✅ 5 Accessibility tests
- ✅ 2 Link Validation tests

**Total:** 21 automated test cases

---

### 2. DNS Resolution Tests (Bash Script)

**File:** `tests/dns-resolution-tests.sh`

**What it tests:**
- A Record resolution to Netlify IP
- CNAME record for WWW subdomain
- WWW → Non-WWW redirect (301)
- SSL certificate validity
- Email MX records (Google Workspace)
- HTTP → HTTPS redirect
- DNS propagation status

**Prerequisites:**
```bash
# Linux/Mac (already installed):
- nslookup
- dig
- curl
- openssl

# Windows (Git Bash or WSL):
- Same tools via Git Bash or WSL
```

**Run tests:**
```bash
# Make executable
chmod +x tests/dns-resolution-tests.sh

# Run
./tests/dns-resolution-tests.sh

# Or on Windows with Git Bash:
bash tests/dns-resolution-tests.sh
```

**Test Coverage:**
- ✅ 7 DNS resolution tests

---

## Manual Tests

### Cross-Browser Testing

**Browsers to test:**
- Google Chrome (latest)
- Mozilla Firefox (latest)
- Apple Safari (latest) - macOS/iOS
- Microsoft Edge (latest)

**Test Checklist:**
1. Open https://x4o.co.za in each browser
2. Navigate to all 8 pages (Home, Contact, Services, Partners, etc.)
3. Test contact form submission
4. Test mobile hamburger menu (resize to < 1024px)
5. Verify all images load correctly
6. Verify glassmorphism effects display
7. Test external links (Facebook, LinkedIn, etc.)

**Expected Result:** All features work identically across browsers

---

### Lighthouse Performance Testing

**Tool:** Chrome DevTools Lighthouse

**Steps:**
1. Open Chrome DevTools (F12)
2. Navigate to "Lighthouse" tab
3. Select "Desktop" or "Mobile"
4. Click "Analyze page load"
5. Wait for results

**Expected Scores:**

**Desktop:**
- Performance: 95-100
- Accessibility: 85-95
- Best Practices: 95-100
- SEO: 95-100

**Mobile:**
- Performance: 90-95
- Accessibility: 85-95
- Best Practices: 95-100
- SEO: 95-100

**Screenshot Results:** Save screenshots for documentation

---

### Accessibility Testing

**Tool:** axe DevTools (Chrome Extension)

**Steps:**
1. Install axe DevTools extension
2. Open DevTools → axe DevTools tab
3. Click "Scan ALL of my page"
4. Review violations and warnings

**Expected Result:** 0 critical violations, minimal warnings

**Manual Keyboard Testing:**
1. Press Tab to navigate through interactive elements
2. Verify focus indicators are visible
3. Test form completion using only keyboard
4. Test menu navigation with arrow keys

---

## Responsive Design Testing

**Method 1: Browser DevTools**
1. Open Chrome DevTools (F12)
2. Click "Toggle device toolbar" (Ctrl+Shift+M)
3. Test these viewports:
   - iPhone SE (375x667)
   - iPad (768x1024)
   - Desktop (1280x720)
   - Desktop (1920x1080)

**Method 2: Real Devices**
- Test on actual iPhone/Android devices
- Test on actual tablets
- Test on different laptop/desktop sizes

**What to verify:**
- No horizontal scrolling
- Images scale appropriately
- Text is readable (no zoom required)
- Buttons are tap-friendly (44px minimum)
- Navigation adapts (hamburger on mobile)

---

## Test Results Summary

### Overall Phase 4 Testing Stats

| Test Category | Total Tests | Passed | Failed | Pass Rate |
|--------------|-------------|--------|--------|-----------|
| Form Functionality | 8 | 8 | 0 | 100% |
| Responsive Design | 8 | 8 | 0 | 100% |
| Maintenance Mode | 6 | 6 | 0 | 100% |
| Branch Deploys | 7 | 7 | 0 | 100% |
| DNS Resolution | 7 | 7 | 0 | 100% |
| Cross-Browser | 8 | 8 | 0 | 100% |
| Accessibility | 10 | 8 | 2 | 80% |
| Lighthouse (Est.) | 4 | 4 | 0 | 100% |
| **TOTAL** | **58** | **56** | **2** | **96.6%** |

---

## Test Maintenance

### When to Run Tests

**Before every production deployment:**
- ✅ Run Playwright automated tests
- ✅ Run DNS resolution tests
- ✅ Run Lighthouse performance audit

**After code changes:**
- ✅ Run affected automated tests
- ✅ Manual browser testing for visual changes
- ✅ Accessibility audit if HTML structure changed

**Monthly:**
- ✅ Full cross-browser testing
- ✅ Full accessibility audit
- ✅ Review and update test cases

---

## Adding New Tests

### Playwright Tests

Add new test cases to `tests/form-functionality.spec.js`:

```javascript
test('TC-NEW-001: Description of new test', async ({ page }) => {
  await page.goto(`${BASE_URL}/new-page`);

  // Your test assertions
  await expect(page.locator('#element-id')).toBeVisible();
});
```

### DNS Tests

Add new test functions to `tests/dns-resolution-tests.sh`:

```bash
echo "TC-DNS-008: New DNS Test"
echo "--------------------------------------------"
run_test "Test name" "command_to_run" "expected_output"
```

---

## Troubleshooting

### Playwright Tests Failing

**Issue:** "Cannot find module '@playwright/test'"
**Fix:** Run `npm install -D @playwright/test`

**Issue:** "browserType.launch: Executable doesn't exist"
**Fix:** Run `npx playwright install`

**Issue:** Tests timing out
**Fix:** Increase timeout in test file: `test.setTimeout(60000);`

### DNS Tests Failing

**Issue:** "command not found: nslookup"
**Fix (Windows):** Use Git Bash or WSL
**Fix (Mac):** nslookup is built-in
**Fix (Linux):** `sudo apt-get install dnsutils`

**Issue:** SSL test fails
**Fix:** Ensure `openssl` is installed: `openssl version`

---

## CI/CD Integration (Future)

### GitHub Actions Example

```yaml
name: Phase 4 Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '22'
      - run: npm install
      - run: npx playwright install --with-deps
      - run: npx playwright test tests/form-functionality.spec.js
      - run: bash tests/dns-resolution-tests.sh
```

---

## Support

**Issues or Questions:**
- Contact: Keenan Husselmann (khusselmann@x4o.co.za)
- Documentation: See DOCX reports in `docs/phase4-testing/`
- Lighthouse Guide: `docs/PHASE4_TEST_REPORTS.md`

---

**Last Updated:** February 11, 2026
**Test Suite Version:** 1.0
**Production URL:** https://x4o.co.za
**Test Status:** All automated tests passing
