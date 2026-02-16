# Security Best Practices Guide

**Last Updated:** February 13, 2026
**For:** X4O Website Administrators

---

## Current Security Status

**Security Grade:** A (Excellent) ✅
**Last Security Audit:** February 13, 2026
**Critical Vulnerabilities:** 0 ✅
**Security Headers:** 7 of 7 deployed ✅

---

## Security Headers (Already Implemented)

### 1. X-Frame-Options: DENY

**What it does:** Prevents clickjacking attacks
**Status:** ✅ Deployed
**Protection:** Site cannot be embedded in iframes

### 2. Content-Security-Policy (CSP)

**What it does:** Prevents XSS attacks and unauthorized resource loading
**Status:** ✅ Deployed
**Current Policy:**
```
default-src 'self';
script-src 'self' 'unsafe-inline' https://www.netlify.app;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
font-src 'self' https://fonts.gstatic.com;
img-src 'self' data:;
connect-src 'self';
frame-ancestors 'none';
base-uri 'self';
form-action 'self';
```

### 3. X-Content-Type-Options: nosniff

**What it does:** Prevents MIME-sniffing attacks
**Status:** ✅ Deployed
**Protection:** Browser won't guess content types

### 4. X-XSS-Protection: 1; mode=block

**What it does:** Legacy browser XSS protection
**Status:** ✅ Deployed
**Protection:** Blocks detected XSS attempts

### 5. Referrer-Policy: strict-origin-when-cross-origin

**What it does:** Controls referrer information leakage
**Status:** ✅ Deployed
**Protection:** Limits data sent to external sites

### 6. Permissions-Policy

**What it does:** Restricts browser features
**Status:** ✅ Deployed
**Blocked:** geolocation, microphone, camera, payment, USB

### 7. Strict-Transport-Security (HSTS)

**What it does:** Forces HTTPS for 1 year
**Status:** ✅ Deployed (Netlify automatic)
**Protection:** Prevents downgrade to HTTP

---

## Security Maintenance Checklist

### Weekly
- [ ] No action needed (automated security maintained)

### Monthly
- [ ] Check npm dependencies: `npm audit`
- [ ] Review Netlify security logs (if available)
- [ ] Verify security headers still deployed

### Quarterly
- [ ] Run security header test: https://securityheaders.com/
- [ ] Test SSL configuration: https://www.ssllabs.com/ssltest/
- [ ] Review and update dependencies: `npm update`

### Annually
- [ ] Full security audit (rerun automated tests)
- [ ] Review all security practices
- [ ] Update this guide if needed

---

## Dependency Security

### Keep Dependencies Updated

**Check for Vulnerabilities:**
```bash
npm audit
```

**Expected Output:**
```
found 0 vulnerabilities
```

**If Vulnerabilities Found:**
```bash
# Fix automatically if possible
npm audit fix

# Force fix (may cause breaking changes)
npm audit fix --force

# Manual review and fix
npm update <package-name>
```

**Before Any Update:**
1. Test locally: `npm run dev`
2. Run build: `npm run build`
3. Test on staging before production

---

## Password & Access Security

### GitHub Repository Access

**Best Practices:**
- ✅ Use strong, unique password for GitHub
- ✅ Enable two-factor authentication (2FA)
- ✅ Use SSH keys for Git operations (not passwords)
- ⚠️ Never share GitHub credentials
- ⚠️ Never commit passwords or API keys to repository

**Set Up 2FA:**
1. Go to GitHub Settings → Password and authentication
2. Enable two-factor authentication
3. Use authenticator app (Google Authenticator, Authy)

### Netlify Access

**Best Practices:**
- ✅ Use strong, unique password
- ✅ Enable two-factor authentication
- ⚠️ Limit team member access (only add trusted users)
- ⚠️ Review access logs monthly

### Email Account Security (Google Workspace)

**Best Practices:**
- ✅ Strong password for admin@x4o.co.za and info@x4o.co.za
- ✅ Enable 2FA on Google account
- ✅ Review security checkup monthly
- ⚠️ Be cautious of phishing emails
- ⚠️ Don't click suspicious links

---

## Code Security

### Astro Framework Security

**Current Protection:**
- ✅ Automatic HTML escaping (prevents XSS)
- ✅ No server-side code execution (static site)
- ✅ No database (prevents SQL injection)

**Safe Variable Output:**
```astro
---
const userInput = "User provided text";
---

<!-- Safe: Astro auto-escapes -->
<p>{userInput}</p>
```

**Unsafe (Avoid):**
```astro
<!-- Dangerous: Unescaped HTML -->
<div set:html={userInput} />
```

**Only use `set:html` for**:
- Content you control 100%
- Markdown you've sanitized
- Never for user input

---

## Form Security

### Contact Form Protection (Already Implemented)

**1. Honeypot Field (Spam Protection)**
```astro
<!-- Hidden field bots will fill out -->
<input type="hidden" name="bot-field" />
```

**2. Netlify Forms Security**
- ✅ Built-in spam filtering
- ✅ Rate limiting
- ✅ Automatic sanitization

**3. HTML5 Validation**
```astro
<input type="email" required />
```

### Additional Form Security (If Adding New Forms)

**Required Attributes:**
- `required` on mandatory fields
- `type="email"` for email fields
- `maxlength` to prevent overflow
- Honeypot field for spam protection

**Example:**
```astro
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="bot-field" />
  <input type="text" name="name" required maxlength="100" />
  <input type="email" name="email" required />
  <textarea name="message" required maxlength="5000"></textarea>
</form>
```

---

## HTTPS & SSL Security

### Current Status

**SSL Certificate:**
- ✅ Let's Encrypt (free, auto-renewing)
- ✅ A+ rating on SSL Labs
- ✅ TLS 1.2+ only (secure)
- ✅ Auto-renewal every 90 days

### No Maintenance Needed

Netlify handles:
- Certificate provisioning
- Automatic renewal
- Strong cipher suites
- HTTP to HTTPS redirect

### Verify SSL Health (Quarterly)

**Test URL:** https://www.ssllabs.com/ssltest/
**Test:** https://x4o.co.za
**Expected Grade:** A or A+

**Red Flags:**
- Grade below A
- Certificate expiring soon (shouldn't happen with auto-renewal)
- Weak ciphers enabled

---

## DNS Security

### Current Configuration

**Domain Registrar:** IT-Guru (Kuilsrivier)
**DNS Records:**
- A record: 75.2.60.5 (Netlify)
- CNAME: www → x4oconsultants.netlify.app
- MX records: Google Workspace email (preserved)

### DNS Best Practices

**Do:**
- ✅ Keep registrar account secure (2FA)
- ✅ Only authorized person can change DNS
- ✅ Document all DNS changes

**Don't:**
- ❌ Share registrar login credentials
- ❌ Delete MX records (breaks email)
- ❌ Change A record without testing

### DNSSEC (Optional Future Enhancement)

**What it is:** DNS security extension
**Why:** Prevents DNS spoofing attacks
**Status:** Not currently implemented
**Risk:** Low (Netlify handles security)

---

## Backup Security

### Current Backup Strategy

**Primary Backup:** GitHub repository (full version history)

**Secondary Backup:** Netlify deploy history (last 100 deploys)

**Both Are Secure:**
- ✅ Private repositories
- ✅ Access controlled
- ✅ Geographic redundancy

### Additional Security Measures

**Recommended:**
- Export repository monthly to local backup
- Store credentials in secure password manager
- Document recovery procedures (see BACKUP.md)

---

## Content Injection Protection

### Static Site Benefits

**You're Protected From:**
- ✅ SQL Injection (no database)
- ✅ Command Injection (no server code)
- ✅ Server-Side Template Injection (build-time only)
- ✅ File Upload Attacks (no upload feature)
- ✅ XXE Attacks (no XML processing)

**Remaining Risks (Mitigated):**
- ✅ XSS: Protected by framework auto-escaping + CSP header
- ✅ Clickjacking: Protected by X-Frame-Options header
- ✅ CSRF: Not applicable (no authentication/sessions)

---

## Third-Party Security

### Current Third-Party Services

**Google Fonts:**
- Trusted source
- Subresource Integrity (SRI) not needed (Google managed)
- CSP allows: https://fonts.googleapis.com

**Netlify Forms:**
- Built-in Netlify service
- GDPR compliant
- No external third-party

### Adding New Third-Party Services

**Before Adding:**
1. Research service security reputation
2. Check privacy policy (GDPR/POPIA compliance)
3. Add to Content-Security-Policy if loading resources
4. Test on staging first

**Example: Adding Google Analytics**
```
# Update CSP in public/_headers
script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com
```

---

## Privacy & Compliance

### Current Status

**Data Collected:**
- Contact form submissions (name, email, message)
- Netlify server logs (IP addresses, user agents)

**Data Storage:**
- Forms: Netlify (US-based servers)
- Logs: Netlify (automatic after 30 days)

**Compliance:**
- ✅ HTTPS encryption
- ✅ Minimal data collection
- ⏸️ Privacy policy page (Phase 7 - if analytics added)
- ⏸️ Cookie consent (Phase 7 - if analytics added)

### GDPR/POPIA Requirements (When Adding Analytics)

**Must Have:**
1. Privacy policy page
2. Cookie consent banner
3. Data processing agreement
4. User opt-out mechanism
5. Data deletion process

**See:** `ANALYTICS_IMPLEMENTATION_GUIDE.md` for details

---

## Incident Response

### If Security Incident Occurs

**Immediate Actions:**
1. Change all passwords (GitHub, Netlify, email)
2. Enable 2FA if not already enabled
3. Review recent Git commits for unauthorized changes
4. Check Netlify deploy log for unexpected deployments
5. Scan for malware on local development machine

**Rollback Procedure:**
1. Identify last known good commit in GitHub
2. Revert to that commit:
   ```bash
   git checkout <good-commit-hash>
   git push origin main --force
   ```
3. Netlify auto-deploys the reverted version
4. Verify site is clean

**Contact:**
- Netlify Support: https://www.netlify.com/support/
- GitHub Support: https://support.github.com/

---

## Security Monitoring

### Automated Security Tests

**Scripts Available:**
- `tests/security-tests.ps1` (PowerShell)
- `tests/security-tests.sh` (Bash)

**Run Monthly:**
```bash
# Windows
powershell -ExecutionPolicy Bypass -File tests/security-tests.ps1

# Linux/Mac
./tests/security-tests.sh
```

**Expected Result:** All tests pass (100%)

### Online Security Scanners

**Run Quarterly:**

**1. Security Headers**
- URL: https://securityheaders.com/
- Test: https://x4o.co.za
- Expected: A or A+

**2. SSL Labs**
- URL: https://www.ssllabs.com/ssltest/
- Test: https://x4o.co.za
- Expected: A or A+

**3. Mozilla Observatory**
- URL: https://observatory.mozilla.org/
- Test: https://x4o.co.za
- Expected: A or higher

---

## Security Red Flags

### Immediate Action Required If:

**1. npm audit Shows Critical Vulnerabilities**
```bash
npm audit  # Should show 0 vulnerabilities
```
- Action: Run `npm audit fix` immediately
- Test locally before deploying

**2. Security Headers Missing**
- Test: https://securityheaders.com/
- Action: Verify `public/_headers` file is deployed
- Redeploy if needed

**3. SSL Certificate Issues**
- Warning in browser address bar
- Action: Contact Netlify support (auto-renewal should work)

**4. Unauthorized Git Commits**
- Check: `git log` for unknown commits
- Action: Change passwords, revert commits, enable 2FA

**5. Unexpected Emails from Forms**
- Spam bypass detected
- Action: Review Netlify spam settings, add CAPTCHA if severe

---

## Security Best Practices Summary

### Do:
- ✅ Keep npm dependencies updated
- ✅ Use strong, unique passwords
- ✅ Enable 2FA everywhere
- ✅ Run security tests monthly
- ✅ Test changes on staging first
- ✅ Review security quarterly

### Don't:
- ❌ Commit API keys or passwords to Git
- ❌ Use `set:html` with user input
- ❌ Disable security headers
- ❌ Share login credentials
- ❌ Skip 2FA setup
- ❌ Ignore npm audit warnings

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
**Security Status:** Excellent (Grade A, 0 vulnerabilities)
