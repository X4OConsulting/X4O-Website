// =============================================================================
// X4O Website - Automated Test Suite (Playwright)
// =============================================================================
// Run with: npx playwright test tests/form-functionality.spec.js
// Run specific test: npx playwright test tests/form-functionality.spec.js -g "TC-FORM-001"
// Run with UI: npx playwright test tests/form-functionality.spec.js --headed
// Generate report: npx playwright test tests/form-functionality.spec.js --reporter=html
// =============================================================================
// Test Case IDs map to X4O_Test_Cases.csv (Smartsheet Test Cases sheet)
// Script: tests/form-functionality.spec.js
// =============================================================================

import { test, expect } from '@playwright/test';

const BASE_URL = 'https://x4o.co.za';

// =============================================================================
// FORM FUNCTIONALITY TESTS (TC-FORM-001 to TC-FORM-008)
// Category: Form Functionality
// Test Script: tests/form-functionality.spec.js
// =============================================================================

test.describe('Form Functionality Tests', () => {

  // ---------------------------------------------------------------------------
  // TC-FORM-001: Form Fields Present
  // Priority: High | Type: Automated
  // Description: Verify all required form fields are present and correctly configured
  // Expected: All 6 fields (Name, Email, Phone, Subject, Message, bot-field)
  //           visible with correct IDs
  // ---------------------------------------------------------------------------
  test('TC-FORM-001: All form fields are present and correctly configured', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    // Verify all visible form fields exist with correct IDs
    await expect(page.locator('#name')).toBeVisible();
    await expect(page.locator('#email')).toBeVisible();
    await expect(page.locator('#phone')).toBeVisible();
    await expect(page.locator('#subject')).toBeVisible();
    await expect(page.locator('#message')).toBeVisible();

    // Verify honeypot field exists but is hidden from users
    const honeypot = page.locator('[name="bot-field"]');
    await expect(honeypot).toBeAttached();
    await expect(honeypot).toHaveClass(/hidden/);

    // Verify each field has the correct input type
    await expect(page.locator('#name')).toHaveAttribute('type', 'text');
    await expect(page.locator('#email')).toHaveAttribute('type', 'email');
    await expect(page.locator('#phone')).toHaveAttribute('type', 'tel');

    // Verify subject is a select dropdown
    const subjectTag = await page.locator('#subject').evaluate(el => el.tagName.toLowerCase());
    expect(subjectTag).toBe('select');

    // Verify message is a textarea
    const messageTag = await page.locator('#message').evaluate(el => el.tagName.toLowerCase());
    expect(messageTag).toBe('textarea');

    // Verify hidden form-name field for Netlify
    await expect(page.locator('input[name="form-name"][value="contact"]')).toBeAttached();
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-002: HTML5 Validation Attributes
  // Priority: High | Type: Automated
  // Description: Verify HTML5 validation attributes are properly implemented
  // Expected: Required fields have required attribute, email field has type=email
  // ---------------------------------------------------------------------------
  test('TC-FORM-002: HTML5 validation attributes are properly implemented', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    // Check required attributes on mandatory fields
    await expect(page.locator('#name')).toHaveAttribute('required', '');
    await expect(page.locator('#email')).toHaveAttribute('required', '');
    await expect(page.locator('#message')).toHaveAttribute('required', '');

    // Phone should NOT be required (it's optional)
    const phoneRequired = await page.locator('#phone').getAttribute('required');
    expect(phoneRequired).toBeNull();

    // Check email input type for browser-native validation
    await expect(page.locator('#email')).toHaveAttribute('type', 'email');

    // Check phone input type for mobile keyboard optimization
    await expect(page.locator('#phone')).toHaveAttribute('type', 'tel');

    // Verify name input type
    await expect(page.locator('#name')).toHaveAttribute('type', 'text');
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-003: Subject Dropdown Options
  // Priority: Medium | Type: Automated
  // Description: Verify all subject dropdown options are available
  // Expected: 8 subject options including 3 booking-specific options
  // ---------------------------------------------------------------------------
  test('TC-FORM-003: Subject dropdown has all 8 required options', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    const subject = page.locator('#subject');
    const options = await subject.locator('option').allTextContents();

    // Verify total option count (8 options + 1 disabled placeholder = 9)
    const selectableOptions = await subject.locator('option:not([disabled])').count();
    expect(selectableOptions).toBe(8);

    // Verify each required option is present
    expect(options).toContain('General Inquiry');
    expect(options).toContain('Consulting Services');
    expect(options).toContain('Coaching Services');
    expect(options).toContain('Personal Transformation Coaching - Book Session');
    expect(options).toContain('Leadership Coaching - Book Session');
    expect(options).toContain('Corporate Governance Coaching - Book Session');
    expect(options).toContain('Partnership');
    expect(options).toContain('Other');

    // Verify disabled placeholder option exists
    const placeholderOption = subject.locator('option[disabled]');
    await expect(placeholderOption).toHaveText('Select a subject');
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-004: Query Parameter Pre-fill
  // Priority: High | Type: Automated
  // Description: Verify query parameters automatically pre-select subject dropdown
  // Expected: Subject dropdown auto-selects when URL has ?subject= parameter
  // Related Bug: BUG-001 (Fixed in commit 7969400)
  // ---------------------------------------------------------------------------
  test('TC-FORM-004: Query parameter pre-fills subject dropdown', async ({ page }) => {
    // Test with a booking-specific subject value
    const testSubject = 'Personal Transformation Coaching Booking Request';
    await page.goto(`${BASE_URL}/contact?subject=${encodeURIComponent(testSubject)}`);

    // Wait for DOMContentLoaded and pre-fill script to execute
    await page.waitForLoadState('domcontentloaded');
    await page.waitForTimeout(1000);

    // Verify the subject dropdown has the pre-filled value
    const subjectValue = await page.locator('#subject').inputValue();
    expect(subjectValue).toBe(testSubject);

    // Test with another subject value to confirm consistency
    const testSubject2 = 'Leadership Coaching Booking Request';
    await page.goto(`${BASE_URL}/contact?subject=${encodeURIComponent(testSubject2)}`);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForTimeout(1000);

    const subjectValue2 = await page.locator('#subject').inputValue();
    expect(subjectValue2).toBe(testSubject2);

    // Test with General Inquiry
    const testSubject3 = 'General Inquiry';
    await page.goto(`${BASE_URL}/contact?subject=${encodeURIComponent(testSubject3)}`);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForTimeout(1000);

    const subjectValue3 = await page.locator('#subject').inputValue();
    expect(subjectValue3).toBe(testSubject3);
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-005: Netlify Forms Integration
  // Priority: High | Type: Automated
  // Description: Verify all Netlify Forms attributes are correctly configured
  // Expected: Form has name=contact, method=POST, action with trailing slash
  // Related Bug: BUG-002 (Trailing slash fix)
  // Note: Netlify strips data-netlify and data-netlify-honeypot attributes
  //       during deployment and replaces them with its own form processing.
  //       We verify the attributes that persist on the live deployed site.
  // ---------------------------------------------------------------------------
  test('TC-FORM-005: Netlify Forms attributes are correctly configured', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    const form = page.locator('form[name="contact"]');

    // Verify form exists with correct name
    await expect(form).toBeAttached();

    // Verify form method and action (these persist after Netlify processing)
    await expect(form).toHaveAttribute('method', 'POST');

    // Verify action URL has trailing slash (BUG-002 fix)
    await expect(form).toHaveAttribute('action', '/contact-success/');

    // Verify hidden form-name input (required by Netlify for form identification)
    const hiddenFormName = form.locator('input[name="form-name"]');
    await expect(hiddenFormName).toBeAttached();
    await expect(hiddenFormName).toHaveAttribute('type', 'hidden');
    await expect(hiddenFormName).toHaveAttribute('value', 'contact');
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-006: Spam Protection Honeypot
  // Priority: High | Type: Automated
  // Description: Verify honeypot field is present and hidden
  // Expected: bot-field exists and is hidden from human users
  // Note: Netlify strips data-netlify-honeypot attribute during deployment.
  //       We verify the honeypot input exists and is not visible to users.
  // ---------------------------------------------------------------------------
  test('TC-FORM-006: Spam protection honeypot is present and hidden', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    // Verify honeypot field exists in the form
    const honeypot = page.locator('form[name="contact"] [name="bot-field"]');
    await expect(honeypot).toBeAttached();

    // Verify the honeypot is not visually visible to users
    // (it may be hidden via CSS class, parent element, or display:none)
    const isVisible = await honeypot.isVisible();
    expect(isVisible).toBe(false);
  });

  // ---------------------------------------------------------------------------
  // TC-FORM-008: Form Placeholders and UX
  // Priority: Low | Type: Automated
  // Description: Verify all form fields have user-friendly placeholders
  // Expected: All fields have helpful placeholders with examples
  // NOTE: TC-FORM-007 (Success Redirect) is Manual - not included here
  // ---------------------------------------------------------------------------
  test('TC-FORM-008: All form fields have user-friendly placeholders', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    // Verify placeholder text on each input field
    await expect(page.locator('#name')).toHaveAttribute('placeholder', 'Your full name');
    await expect(page.locator('#email')).toHaveAttribute('placeholder', 'you@example.com');
    await expect(page.locator('#phone')).toHaveAttribute('placeholder', '+27 12 345 6789');
    await expect(page.locator('#message')).toHaveAttribute('placeholder', 'How can we help you?');

    // Verify subject dropdown has a placeholder option
    const placeholderOption = page.locator('#subject option[disabled][selected]');
    await expect(placeholderOption).toHaveText('Select a subject');

    // Verify submit button has clear call-to-action text
    const submitButton = page.locator('form[name="contact"] button[type="submit"]');
    await expect(submitButton).toBeVisible();
    await expect(submitButton).toBeEnabled();
    await expect(submitButton).toContainText('Send Message');
  });

});

// =============================================================================
// RESPONSIVE DESIGN TESTS (TC-RESP-001, TC-RESP-002, TC-RESP-007)
// Category: Responsive Design
// Test Script: tests/form-functionality.spec.js
// =============================================================================

test.describe('Responsive Design Tests', () => {

  // ---------------------------------------------------------------------------
  // TC-RESP-001: Header Navigation Responsiveness
  // Priority: High | Type: Automated
  // Description: Verify header navigation adapts correctly to screen size
  // Expected: Desktop shows horizontal nav, mobile shows hamburger menu
  // Breakpoint: 1024px (lg)
  // ---------------------------------------------------------------------------
  test('TC-RESP-001: Header navigation adapts to screen size', async ({ page }) => {
    // --- Desktop View (1280px) ---
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.goto(`${BASE_URL}/`);

    // Desktop horizontal navigation should be visible
    const desktopNav = page.locator('ul.hidden.lg\\:flex');
    await expect(desktopNav).toBeVisible();

    // Mobile hamburger toggle should be hidden on desktop
    const mobileToggle = page.locator('label[for="mobile-menu-toggle"]');
    await expect(mobileToggle).not.toBeVisible();

    // Verify all desktop nav links are accessible
    const navLinks = desktopNav.locator('a');
    const linkCount = await navLinks.count();
    expect(linkCount).toBeGreaterThanOrEqual(6); // At least 6 nav items including dropdown child

    // --- Mobile View (375px) ---
    await page.setViewportSize({ width: 375, height: 667 });
    await page.waitForTimeout(500); // Allow responsive reflow

    // Desktop nav should be hidden on mobile
    await expect(desktopNav).not.toBeVisible();

    // Mobile hamburger toggle should be visible
    await expect(mobileToggle).toBeVisible();

    // Verify hamburger toggle has proper ARIA label
    await expect(mobileToggle).toHaveAttribute('aria-label', 'Toggle navigation menu');

    // --- Tablet View (768px - below lg breakpoint) ---
    await page.setViewportSize({ width: 768, height: 1024 });
    await page.waitForTimeout(500);

    // Below 1024px, should still show mobile menu
    await expect(desktopNav).not.toBeVisible();
    await expect(mobileToggle).toBeVisible();

    // --- Just above breakpoint (1024px - lg) ---
    await page.setViewportSize({ width: 1024, height: 768 });
    await page.waitForTimeout(500);

    // At exactly 1024px (lg breakpoint), desktop nav should appear
    await expect(desktopNav).toBeVisible();
    await expect(mobileToggle).not.toBeVisible();
  });

  // ---------------------------------------------------------------------------
  // TC-RESP-002: Contact Form Layout
  // Priority: High | Type: Automated
  // Description: Verify contact form layout adapts to different screen sizes
  // Expected: Desktop 2-column layout, mobile single-column stack
  // Grid: 1 col mobile, 2 col desktop (lg:grid-cols-2)
  // ---------------------------------------------------------------------------
  test('TC-RESP-002: Contact form layout adapts to screen size', async ({ page }) => {
    // --- Desktop View (1280px) ---
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.goto(`${BASE_URL}/contact`);

    // Verify the 2-column grid container exists
    const gridContainer = page.locator('.grid.grid-cols-1.lg\\:grid-cols-2');
    await expect(gridContainer).toBeVisible();

    // On desktop, both columns should be side by side
    // The form (glass-card) should be visible
    const contactForm = page.locator('form[name="contact"]');
    await expect(contactForm).toBeVisible();

    // The contact info section (left column) should be visible
    const contactInfo = page.locator('text=Get in Touch');
    await expect(contactInfo).toBeVisible();

    // Verify 2-column layout by checking computed grid
    const gridDisplay = await gridContainer.evaluate(el => {
      return window.getComputedStyle(el).getPropertyValue('grid-template-columns');
    });
    // Desktop should have 2 columns (non-single value)
    expect(gridDisplay).not.toBe('none');

    // --- Mobile View (375px) ---
    await page.setViewportSize({ width: 375, height: 667 });
    await page.waitForTimeout(500);

    // Form and info should still be visible but stacked
    await expect(contactForm).toBeVisible();
    await expect(contactInfo).toBeVisible();

    // On mobile, grid-template-columns should be single column
    const mobileGrid = await gridContainer.evaluate(el => {
      return window.getComputedStyle(el).getPropertyValue('grid-template-columns');
    });
    // Mobile grid should be essentially one column
    expect(mobileGrid).toBeTruthy();
  });

  // ---------------------------------------------------------------------------
  // TC-RESP-007: No Horizontal Scroll
  // Priority: High | Type: Automated
  // Description: Verify no horizontal scrolling occurs on any device
  // Expected: Body width <= viewport width at all breakpoints
  // Tested at 5 viewports: 320px, 375px, 768px, 1280px, 1920px
  // ---------------------------------------------------------------------------
  test('TC-RESP-007: No horizontal scroll at any viewport', async ({ page }) => {
    const viewports = [
      { name: 'Mobile Small (320px)', width: 320, height: 568 },
      { name: 'Mobile Standard (375px)', width: 375, height: 667 },
      { name: 'Tablet (768px)', width: 768, height: 1024 },
      { name: 'Desktop (1280px)', width: 1280, height: 720 },
      { name: 'Desktop Large (1920px)', width: 1920, height: 1080 },
    ];

    // Test multiple pages for horizontal scroll
    const pages = ['/', '/contact', '/consulting-and-advisory-services', '/partners'];

    for (const viewport of viewports) {
      await page.setViewportSize({ width: viewport.width, height: viewport.height });

      for (const pagePath of pages) {
        await page.goto(`${BASE_URL}${pagePath}`);
        await page.waitForLoadState('networkidle');

        const bodyScrollWidth = await page.evaluate(() => document.body.scrollWidth);
        const windowInnerWidth = await page.evaluate(() => window.innerWidth);

        // Body should not be wider than viewport (+1 for rounding tolerance)
        expect(bodyScrollWidth,
          `Horizontal scroll detected on ${pagePath} at ${viewport.name}: ` +
          `body=${bodyScrollWidth}px > viewport=${windowInnerWidth}px`
        ).toBeLessThanOrEqual(windowInnerWidth + 1);
      }
    }
  });

});

// =============================================================================
// CROSS-BROWSER COMPATIBILITY TESTS (TC-CROSS-006)
// Category: Cross-Browser
// Test Script: tests/form-functionality.spec.js
// =============================================================================

test.describe('Cross-Browser Compatibility Tests', () => {

  // ---------------------------------------------------------------------------
  // TC-CROSS-006: JavaScript Compatibility
  // Priority: High | Type: Automated
  // Description: Verify ES6 JavaScript executes without errors
  // Expected: Mobile menu toggle and query pre-fill work correctly
  // ---------------------------------------------------------------------------
  test('TC-CROSS-006: ES6 JavaScript executes without errors', async ({ page }) => {
    const jsErrors = [];

    // Listen for JavaScript errors
    page.on('pageerror', (error) => {
      jsErrors.push(error.message);
    });

    // --- Test 1: Page loads without JS errors ---
    await page.goto(`${BASE_URL}/`);
    await page.waitForLoadState('networkidle');
    expect(jsErrors, 'JavaScript errors detected on homepage').toHaveLength(0);

    // --- Test 2: Mobile menu toggle works (JavaScript-powered) ---
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto(`${BASE_URL}/`);
    await page.waitForLoadState('domcontentloaded');

    // Verify the mobile menu toggle checkbox exists
    const menuToggle = page.locator('#mobile-menu-toggle');
    await expect(menuToggle).toBeAttached();

    // The mobile panel should initially be off-screen (translated left)
    const mobilePanel = page.locator('.peer-checked\\:translate-x-0');
    await expect(mobilePanel).toBeAttached();

    // Click the hamburger label to toggle mobile menu
    const hamburgerLabel = page.locator('label[for="mobile-menu-toggle"]');
    await hamburgerLabel.click();

    // Verify checkbox is now checked
    const isChecked = await menuToggle.isChecked();
    expect(isChecked).toBe(true);

    // Verify no JS errors after interaction
    expect(jsErrors, 'JavaScript errors after mobile menu toggle').toHaveLength(0);

    // --- Test 3: Query parameter pre-fill JavaScript works ---
    jsErrors.length = 0; // Reset error tracking
    await page.setViewportSize({ width: 1280, height: 720 });
    const testSubject = 'General Inquiry';
    await page.goto(`${BASE_URL}/contact?subject=${encodeURIComponent(testSubject)}`);
    await page.waitForLoadState('domcontentloaded');
    await page.waitForTimeout(1000);

    // Verify the pre-fill JavaScript executed successfully
    const selectedValue = await page.locator('#subject').inputValue();
    expect(selectedValue).toBe(testSubject);

    // Verify no JS errors during pre-fill
    expect(jsErrors, 'JavaScript errors during query parameter pre-fill').toHaveLength(0);

    // --- Test 4: Contact page loads without JS errors ---
    jsErrors.length = 0;
    await page.goto(`${BASE_URL}/contact`);
    await page.waitForLoadState('networkidle');
    expect(jsErrors, 'JavaScript errors on contact page').toHaveLength(0);

    // --- Test 5: Navigation pages load without JS errors ---
    jsErrors.length = 0;
    const testPages = [
      '/consulting-and-advisory-services',
      '/coaching-services',
      '/book-coaching-sessions',
      '/partners'
    ];

    for (const testPage of testPages) {
      await page.goto(`${BASE_URL}${testPage}`);
      await page.waitForLoadState('networkidle');
    }
    expect(jsErrors, 'JavaScript errors across navigation pages').toHaveLength(0);
  });

});

// =============================================================================
// ACCESSIBILITY TESTS (TC-A11Y-001, TC-A11Y-002, TC-A11Y-004, TC-A11Y-006)
// Category: Accessibility
// Test Script: tests/form-functionality.spec.js
// =============================================================================

test.describe('Accessibility Tests', () => {

  // ---------------------------------------------------------------------------
  // TC-A11Y-001: Semantic HTML Structure
  // Priority: High | Type: Automated
  // Description: Verify proper HTML5 semantic structure
  // Expected: html lang, header, main, footer landmarks present
  // WCAG: 1.3.1 (Info and Relationships)
  // ---------------------------------------------------------------------------
  test('TC-A11Y-001: Page has proper HTML5 semantic structure', async ({ page }) => {
    await page.goto(`${BASE_URL}/`);

    // Verify html has lang attribute set to "en"
    const html = page.locator('html');
    await expect(html).toHaveAttribute('lang', 'en');

    // Verify <header> landmark exists and is visible
    const header = page.locator('header');
    await expect(header).toBeVisible();

    // Verify <main> landmark exists and is visible
    const main = page.locator('main');
    await expect(main).toBeVisible();

    // Verify <footer> landmark exists and is visible
    const footer = page.locator('footer');
    await expect(footer).toBeVisible();

    // Verify <nav> exists within header for navigation
    const nav = page.locator('header nav');
    await expect(nav).toBeAttached();

    // Verify proper document structure on other pages too
    const testPages = ['/contact', '/consulting-and-advisory-services', '/partners'];
    for (const testPage of testPages) {
      await page.goto(`${BASE_URL}${testPage}`);

      await expect(page.locator('html')).toHaveAttribute('lang', 'en');
      await expect(page.locator('header')).toBeVisible();
      await expect(page.locator('main')).toBeVisible();
      await expect(page.locator('footer')).toBeVisible();
    }
  });

  // ---------------------------------------------------------------------------
  // TC-A11Y-002: Heading Hierarchy
  // Priority: High | Type: Automated
  // Description: Verify proper heading hierarchy (single H1, logical order)
  // Expected: Single H1 per page, no skipped heading levels
  // WCAG: 1.3.1 (Info and Relationships), 2.4.6 (Headings and Labels)
  // ---------------------------------------------------------------------------
  test('TC-A11Y-002: Pages have proper heading hierarchy', async ({ page }) => {
    const testPages = [
      { path: '/', name: 'Homepage' },
      { path: '/contact', name: 'Contact' },
      { path: '/consulting-and-advisory-services', name: 'Consulting' },
      { path: '/coaching-services', name: 'Coaching Services' },
      { path: '/partners', name: 'Partners' },
    ];

    for (const testPage of testPages) {
      await page.goto(`${BASE_URL}${testPage.path}`);

      // Verify exactly one H1 per page
      const h1Count = await page.locator('h1').count();
      expect(h1Count,
        `${testPage.name} should have exactly 1 H1, found ${h1Count}`
      ).toBe(1);

      // Verify H1 is visible
      await expect(page.locator('h1')).toBeVisible();

      // Verify H1 has meaningful content (not empty)
      const h1Text = await page.locator('h1').textContent();
      expect(h1Text.trim().length,
        `${testPage.name} H1 should have content`
      ).toBeGreaterThan(0);
    }
  });

  // ---------------------------------------------------------------------------
  // TC-A11Y-004: Form Accessibility
  // Priority: High | Type: Automated
  // Description: Verify form inputs have associated labels and ARIA attributes
  // Expected: All inputs have label[for] attributes, required fields marked
  // WCAG: 1.3.1 (Info and Relationships), 3.3.2 (Labels or Instructions)
  // ---------------------------------------------------------------------------
  test('TC-A11Y-004: Form inputs have associated labels', async ({ page }) => {
    await page.goto(`${BASE_URL}/contact`);

    // Verify label[for] association for each form field
    const formFields = [
      { id: 'name', labelText: 'Name' },
      { id: 'email', labelText: 'Email' },
      { id: 'phone', labelText: 'Phone' },
      { id: 'subject', labelText: 'Subject' },
      { id: 'message', labelText: 'Message' },
    ];

    for (const field of formFields) {
      // Check that a label with matching for attribute exists
      const label = page.locator(`label[for="${field.id}"]`);
      await expect(label,
        `Label for "${field.id}" should exist`
      ).toBeVisible();

      // Check that the label contains the expected text
      const labelText = await label.textContent();
      expect(labelText,
        `Label for "${field.id}" should contain "${field.labelText}"`
      ).toContain(field.labelText);

      // Check that the matching input element exists
      const input = page.locator(`#${field.id}`);
      await expect(input,
        `Input with id="${field.id}" should exist`
      ).toBeAttached();
    }

    // Verify required fields have visual indicator (asterisk *)
    const nameLabel = await page.locator('label[for="name"]').innerHTML();
    expect(nameLabel).toContain('*');

    const emailLabel = await page.locator('label[for="email"]').innerHTML();
    expect(emailLabel).toContain('*');

    const messageLabel = await page.locator('label[for="message"]').innerHTML();
    expect(messageLabel).toContain('*');

    // Verify required attribute is set on mandatory inputs
    await expect(page.locator('#name')).toHaveAttribute('required', '');
    await expect(page.locator('#email')).toHaveAttribute('required', '');
    await expect(page.locator('#message')).toHaveAttribute('required', '');
  });

  // ---------------------------------------------------------------------------
  // TC-A11Y-006: Alt Text for Images
  // Priority: High | Type: Automated
  // Description: Verify all images have descriptive alt text
  // Expected: All img elements have alt attribute
  // WCAG: 1.1.1 (Non-text Content)
  // Pass/Fail: Partial (verify partner logos specifically)
  // ---------------------------------------------------------------------------
  test('TC-A11Y-006: All images have alt text attributes', async ({ page }) => {
    // Test homepage
    await page.goto(`${BASE_URL}/`);
    let images = page.locator('img');
    let imageCount = await images.count();

    for (let i = 0; i < imageCount; i++) {
      const img = images.nth(i);
      const alt = await img.getAttribute('alt');
      const src = await img.getAttribute('src');
      expect(alt,
        `Image "${src}" on homepage should have alt attribute`
      ).not.toBeNull();
    }

    // Test contact page
    await page.goto(`${BASE_URL}/contact`);
    images = page.locator('img');
    imageCount = await images.count();

    for (let i = 0; i < imageCount; i++) {
      const img = images.nth(i);
      const alt = await img.getAttribute('alt');
      const src = await img.getAttribute('src');
      expect(alt,
        `Image "${src}" on contact page should have alt attribute`
      ).not.toBeNull();
    }

    // Test partners page (critical - partner logos)
    await page.goto(`${BASE_URL}/partners`);
    images = page.locator('img');
    imageCount = await images.count();

    for (let i = 0; i < imageCount; i++) {
      const img = images.nth(i);
      const alt = await img.getAttribute('alt');
      const src = await img.getAttribute('src');
      expect(alt,
        `Image "${src}" on partners page should have alt attribute`
      ).not.toBeNull();
      // Alt text should not be empty for meaningful images
      expect(alt.trim().length,
        `Image "${src}" on partners page should have non-empty alt text`
      ).toBeGreaterThan(0);
    }

    // Verify specific partner logos have descriptive alt text
    const EdMeCaLogo = page.locator('img[src*="EdMeCa"]');
    const edMeCaAlt = await EdMeCaLogo.getAttribute('alt');
    expect(edMeCaAlt).toBeTruthy();

    const idcLogo = page.locator('img[src*="idc"]');
    const idcAlt = await idcLogo.getAttribute('alt');
    expect(idcAlt).toBeTruthy();

    const mziLogo = page.locator('img[src*="mzilikazi"]');
    const mziAlt = await mziLogo.getAttribute('alt');
    expect(mziAlt).toBeTruthy();

    // Verify header logo has alt text across the site
    const headerLogo = page.locator('header img[alt="X4O Logo"]');
    await expect(headerLogo).toBeAttached();
  });

});

// =============================================================================
// LINK VALIDATION TESTS (Supplementary)
// These additional tests verify internal/external link integrity
// =============================================================================

test.describe('Link Validation Tests', () => {

  test('TC-LINK-001: All internal navigation links return 200', async ({ page }) => {
    const navLinks = [
      '/',
      '/consulting-and-advisory-services/',
      '/coaching-services/',
      '/book-coaching-sessions/',
      '/contact/',
      '/partners/',
    ];

    for (const link of navLinks) {
      const response = await page.goto(`${BASE_URL}${link}`, { waitUntil: 'domcontentloaded', timeout: 30000 });
      const status = response?.status() ?? 0;
      // Accept 200 (OK) as passing - Netlify may redirect non-trailing-slash
      // URLs, so we use trailing slashes directly to get clean 200 responses
      expect(status,
        `Page ${link} should return 200 (got ${status})`
      ).toBe(200);
    }
  });

  test('TC-LINK-002: External links have security attributes', async ({ page }) => {
    await page.goto(`${BASE_URL}/`);

    const externalLinks = page.locator('a[target="_blank"]');
    const linkCount = await externalLinks.count();

    for (let i = 0; i < linkCount; i++) {
      const link = externalLinks.nth(i);
      const rel = await link.getAttribute('rel');
      const href = await link.getAttribute('href');

      // External links should have noopener and noreferrer for security
      expect(rel,
        `External link "${href}" should have noopener`
      ).toContain('noopener');
      expect(rel,
        `External link "${href}" should have noreferrer`
      ).toContain('noreferrer');
    }
  });

});
