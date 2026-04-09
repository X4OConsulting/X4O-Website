# Automated Testing Framework Decision

**Document Type:** Technical Decision Document
**Phase:** Phase 1 - Planning & Requirements
**Date:** February 7, 2026
**Status:** Approved
**Owner:** Security Team / Keenan Husselmann

---

## Decision Summary

**Decision:** Use PowerShell and Bash shell scripts for automated security testing instead of JavaScript testing frameworks.

**Rationale:** Cross-platform compatibility, no additional dependencies, suitable for CI/CD integration, and appropriate for external API/URL testing.

---

## Context

The X4O website requires automated security testing to validate security headers, HTTPS enforcement, DNS configuration, and injection vulnerability protection. We need to choose an automation framework that can:

1. Test external URLs (production and staging environments)
2. Validate HTTP response headers
3. Execute on Windows, Linux, and Mac platforms
4. Integrate with CI/CD pipelines (GitHub Actions, Azure DevOps)
5. Require minimal setup and dependencies
6. Provide clear pass/fail reporting

## Options Considered

### Option 1: Playwright (JavaScript) ✓ Selected for Functional Testing

**Pros:**
- Already used for functional testing (form-functionality.spec.js)
- Cross-browser testing capability
- Screenshot and video recording
- Strong community support
- Modern async/await syntax

**Cons:**
- Overkill for simple HTTP header checks
- Requires Node.js runtime and npm packages
- Browser automation overhead for API-style tests
- More complex setup for simple curl-like requests

**Decision:** Use Playwright for functional/UI testing only, not security testing.

### Option 2: Shell Scripts (PowerShell + Bash) ✅ Selected for Security Testing

**Pros:**
- Native to Windows (PowerShell) and Linux/Mac (Bash)
- No additional dependencies required
- Direct HTTP testing with curl/Invoke-WebRequest
- Fast execution (< 30 seconds per script)
- Simple exit codes for CI/CD integration (0 = pass, 1 = fail)
- Easy to understand and maintain
- Suitable for external URL testing
- Cross-platform with 2 versions

**Cons:**
- Need to maintain 2 versions (PowerShell and Bash)
- Limited compared to full testing frameworks

**Decision:** ✅ Selected for security testing automation.

### Option 3: Jest + Supertest (JavaScript)

**Pros:**
- JavaScript testing framework
- Good HTTP API testing capabilities
- Familiar to JavaScript developers

**Cons:**
- Requires Node.js and npm dependencies
- Designed for internal API testing, not external URLs
- Overhead for simple header validation
- Less suitable for production URL testing

**Decision:** Not selected (overkill for security header validation).

### Option 4: Python + Requests Library

**Pros:**
- Simple HTTP testing with requests library
- Cross-platform Python runtime
- Easy to write and maintain

**Cons:**
- Requires Python runtime installation
- Additional dependency (requests library)
- Not native to Windows or standard Linux installs
- More setup required than shell scripts

**Decision:** Not selected (adds unnecessary dependency).

---

## Final Decision

**Selected Approach:** Dual shell script implementation

### Implementation Details

**Security Testing Scripts:**

**1. PowerShell Scripts (Windows)**
- `tests/security-tests.ps1` - Security headers + DNS testing
- `tests/injection-tests.ps1` - Injection vulnerability testing

**2. Bash Scripts (Linux/Mac)**
- `tests/security-tests.sh` - Security headers + DNS testing
- `tests/injection-tests.sh` - Injection vulnerability testing

**Script Features:**
- Color-coded output (green = pass, red = fail, yellow = N/A)
- Test counters and pass rate percentage
- Exit codes (0 = success, 1 = failure)
- Execution time < 30 seconds per script
- Production URL verification
- No external dependencies (uses curl built-in)

**Platform Coverage:**
- Windows: PowerShell 5.1+ (built-in since Windows 7)
- Linux: Bash 4.0+ (standard on all modern distros)
- macOS: Bash or Zsh (built-in)
- WSL: Bash scripts work natively
- CI/CD: Both scripts compatible with GitHub Actions, Azure DevOps

---

## Testing Categories Automated

### Security Headers Testing (15 tests)
- X-Frame-Options validation
- Content-Security-Policy validation
- X-Content-Type-Options validation
- X-XSS-Protection validation
- Referrer-Policy validation
- Permissions-Policy validation
- Strict-Transport-Security validation
- HTTP to HTTPS redirect
- www to non-www redirect
- DNS resolution (4 tests)

### Injection Testing (10 tests)
- SQL injection (N/A verification)
- Command injection (N/A verification)
- File upload injection (N/A verification)
- Server-side template injection (N/A verification)
- Reflected XSS (escaping verification)
- DOM-based XSS (code analysis)
- LDAP injection (N/A verification)
- XXE injection (N/A verification)
- NoSQL injection (N/A verification)
- HTML injection (escaping verification)

---

## CI/CD Integration Plan (Phase 7)

**GitHub Actions Example:**

```yaml
name: Security Tests
on: [push, pull_request]
jobs:
  security-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Security Tests (PowerShell)
        run: |
          powershell -ExecutionPolicy Bypass -File tests/security-tests.ps1
          powershell -ExecutionPolicy Bypass -File tests/injection-tests.ps1

  security-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Security Tests (Bash)
        run: |
          chmod +x tests/security-tests.sh tests/injection-tests.sh
          ./tests/security-tests.sh
          ./tests/injection-tests.sh
```

**Benefits:**
- Tests run on every push/PR
- Automated security validation
- Fails CI build if security tests fail
- Cross-platform verification

---

## Comparison Matrix

| Criteria | Playwright | Shell Scripts | Jest/Supertest | Python |
|----------|------------|---------------|----------------|--------|
| **Setup Complexity** | Medium | Low | Medium | Medium |
| **Dependencies** | Node.js + npm | None | Node.js + npm | Python + pip |
| **Execution Speed** | Slow (browser) | Fast (curl) | Medium | Medium |
| **CI/CD Integration** | Good | Excellent | Good | Good |
| **Cross-Platform** | Excellent | Good (2 versions) | Good | Good |
| **Maintenance** | Medium | Low | Medium | Low |
| **URL Testing** | Medium | Excellent | Good | Excellent |
| **Suitable for Security** | No (overkill) | ✅ Yes | Medium | Yes |

---

## Benefits of Selected Approach

**Technical Benefits:**
1. ✅ Zero external dependencies (curl is built-in)
2. ✅ Fast execution (< 30 seconds per script)
3. ✅ Native to target platforms
4. ✅ Simple exit codes for automation
5. ✅ Direct HTTP inspection without browser overhead

**Maintenance Benefits:**
1. ✅ Easy to understand (shell scripting basics)
2. ✅ No package.json or dependency management
3. ✅ No breaking changes from npm package updates
4. ✅ Scripts can run standalone without build process

**Operational Benefits:**
1. ✅ Works on developer machines without setup
2. ✅ Works in CI/CD environments natively
3. ✅ Can be run manually for quick verification
4. ✅ Color output makes failures immediately visible

---

## Trade-offs Accepted

**Maintaining Two Versions:**
- Accepted: Need to maintain PowerShell and Bash versions
- Mitigation: Keep test logic identical, only syntax differs
- Benefit: True cross-platform compatibility

**Limited Compared to Full Framework:**
- Accepted: Shell scripts less sophisticated than Playwright
- Mitigation: Appropriate for security header validation
- Benefit: Simpler and faster for the use case

**Not Suitable for UI Testing:**
- Accepted: Cannot test visual elements or JavaScript behavior
- Mitigation: Use Playwright for functional/UI testing
- Benefit: Right tool for the right job

---

## Success Criteria

**Must Have:**
- ✅ Scripts execute on Windows (PowerShell)
- ✅ Scripts execute on Linux/Mac (Bash)
- ✅ All security header tests automated
- ✅ All injection tests automated
- ✅ Clear pass/fail output with color coding
- ✅ Exit codes for CI/CD integration

**Nice to Have:**
- ✅ Execution time under 30 seconds
- ✅ Test counters and pass rate calculation
- ✅ Detailed error messages for failures
- ✅ No external dependencies required

---

## Implementation Timeline

**Phase 4: Testing** (February 13, 2026)

1. **Security Header Scripts** (2 hours)
   - tests/security-tests.ps1
   - tests/security-tests.sh

2. **Injection Test Scripts** (2 hours)
   - tests/injection-tests.ps1
   - tests/injection-tests.sh

3. **Testing & Documentation** (1 hour)
   - Execute scripts against staging/production
   - Document usage in tests/README.md
   - Verify cross-platform compatibility

**Phase 7: Maintenance** (Future)

4. **CI/CD Integration** (1 hour)
   - Create GitHub Actions workflow
   - Configure automated security testing
   - Set up failure notifications

---

## Alternative Considered: Hybrid Approach

**Concept:** Use Playwright for security testing but with API-only mode

**Why Not Selected:**
- Still requires Node.js runtime and npm packages
- Browser context overhead even in API mode
- Unnecessary complexity for HTTP header validation
- Shell scripts are more appropriate for this use case

**When to Reconsider:**
- If we need JavaScript execution testing (CSP violations, etc.)
- If we add client-side security features requiring DOM testing
- If we consolidate all testing into single framework

---

## Approval & Sign-Off

**Decision Made By:** Security Team / Keenan Husselmann
**Stakeholders Consulted:** Development Team
**Approval Date:** February 7, 2026
**Implementation Phase:** Phase 4 (Testing)
**Status:** ✅ Approved and Implemented

---

**Document Version:** 1.0
**Last Updated:** February 7, 2026
