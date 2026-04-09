# X4O Website - Maintenance Mode Guide

**Document Type:** Operational Procedures
**Purpose:** Enable/Disable Maintenance Mode for x4o.co.za
**Last Updated:** February 13, 2026
**Applies To:** Production (main branch) only

---

## Table of Contents

1. [What is Maintenance Mode?](#what-is-maintenance-mode)
2. [Files and Configuration](#files-and-configuration)
3. [Enable Maintenance Mode](#enable-maintenance-mode)
4. [Disable Maintenance Mode](#disable-maintenance-mode)
5. [Customizing the Maintenance Page](#customizing-the-maintenance-page)
6. [Important Notes](#important-notes)
7. [Emergency Rollback](#emergency-rollback)
8. [Pre-Deployment Checklist](#pre-deployment-checklist)

---

## What is Maintenance Mode?

When enabled, all visitors to **x4o.co.za** will see a maintenance page instead of the regular website. This is useful during:

- **Domain migrations** - DNS updates or nameserver changes
- **Major website updates** - Significant content or feature changes
- **System upgrades** - Framework or dependency updates
- **Database maintenance** - Data migrations or structural changes
- **Security patches** - Critical security updates

**Impact:**
- ✅ Visitors see a professional maintenance message
- ✅ Email service continues to work (Google Workspace unaffected)
- ❌ Contact form is disabled (users should email info@x4o.co.za directly)
- ❌ All website pages are inaccessible

**Scope:**
- Production site (main branch) only
- Staging branch is NEVER affected
- Duration: Typically 1-4 hours

---

## Files and Configuration

### Key Files

| File | Purpose |
|------|---------|
| `public/maintenance.html` | Standalone maintenance page shown to visitors |
| `netlify.toml` | Netlify configuration with redirect rules |

### Maintenance Page Location

The maintenance page is a **static HTML file** at:
```
c:\Users\keena\Projects\x4o-website-dev\public\maintenance.html
```

This file is always deployed with every build, but only shown when maintenance mode is enabled.

---

## Enable Maintenance Mode

### Method 1: Using Netlify Redirects (Recommended)

**Advantages:**
- Version controlled (tracked in Git)
- Reproducible across deployments
- Can be scheduled via Git commits

**Steps:**

#### Step 1: Update `netlify.toml`

1. Open `netlify.toml` in your code editor
2. Find the `[[redirects]]` section
3. **Add this redirect AT THE TOP** of the redirects section:

```toml
# ============================================================
# MAINTENANCE MODE - Uncomment to enable
# ============================================================
[[redirects]]
  from = "/*"
  to = "/maintenance.html"
  status = 200
  force = true
```

**Example (before enabling):**
```toml
[build]
  command = "npm run build"
  publish = "dist"

# Redirects (www → non-www)
[[redirects]]
  from = "https://www.x4o.co.za/*"
  to = "https://x4o.co.za/:splat"
  status = 301
  force = true
```

**Example (after enabling):**
```toml
[build]
  command = "npm run build"
  publish = "dist"

# ============================================================
# MAINTENANCE MODE - Uncomment to enable
# ============================================================
[[redirects]]
  from = "/*"
  to = "/maintenance.html"
  status = 200
  force = true

# Redirects (www → non-www)
[[redirects]]
  from = "https://www.x4o.co.za/*"
  to = "https://x4o.co.za/:splat"
  status = 301
  force = true
```

#### Step 2: Commit and Push to Main Branch

```bash
# Switch to main branch
git checkout main

# Stage the change
git add netlify.toml

# Commit with descriptive message
git commit -m "Enable maintenance mode for [reason]"

# Push to production
git push origin main
```

#### Step 3: Wait for Deployment

- Netlify automatically detects the push
- Build starts within 10-30 seconds
- Deployment completes in 1-2 minutes
- Monitor at: https://app.netlify.com/sites/x4oconsultants/deploys

#### Step 4: Verify Maintenance Mode

1. **Visit the website:** https://x4o.co.za
2. **Expected result:** Maintenance page displays
3. **Check different pages:**
   - https://x4o.co.za/contact
   - https://x4o.co.za/consulting-and-advisory-services
   - All should show maintenance page

---

### Method 2: Using Netlify Dashboard (No Code Changes)

**Advantages:**
- No Git commits required
- Instant activation/deactivation
- No waiting for builds

**Disadvantages:**
- Not version controlled
- Manual dashboard access required
- Could be forgotten after maintenance

**Steps:**

1. Go to **Netlify Dashboard:** https://app.netlify.com
2. Select your **X4O site** (x4oconsultants)
3. Navigate to **Site configuration → Redirects and rewrites**
4. Click **Add redirect rule**
5. Configure:
   - **Source:** `/*`
   - **Destination:** `/maintenance.html`
   - **HTTP Status Code:** `200`
   - **Force:** Yes (check the box)
6. Click **Save**
7. Site enters maintenance mode immediately (no build required)

---

## Disable Maintenance Mode

### If You Used Method 1 (netlify.toml):

#### Step 1: Edit `netlify.toml`

**Option A: Comment Out** (preserves for future use)
```toml
# ============================================================
# MAINTENANCE MODE - Uncomment to enable
# ============================================================
# [[redirects]]
#   from = "/*"
#   to = "/maintenance.html"
#   status = 200
#   force = true
```

**Option B: Delete Entirely**
```toml
# Delete the entire maintenance redirect block
```

#### Step 2: Commit and Push

```bash
git add netlify.toml
git commit -m "Disable maintenance mode - site is live"
git push origin main
```

#### Step 3: Wait for Deployment

- 1-2 minutes for build and deploy
- Site returns to normal operation

#### Step 4: Verify Site is Live

1. Visit https://x4o.co.za
2. Homepage should load normally
3. Test contact form
4. Check all navigation links

---

### If You Used Method 2 (Netlify Dashboard):

1. Go to **Netlify Dashboard**
2. Navigate to **Site configuration → Redirects and rewrites**
3. Find the maintenance redirect rule
4. Click the **Delete** icon (trash can)
5. Click **Save**
6. Site returns to normal immediately

---

## Customizing the Maintenance Page

### Edit the Maintenance Page

File location: `public/maintenance.html`

**What to customize:**

1. **Estimated downtime:**
```html
<p>We expect to be back online by [TIME] SAST.</p>
```

2. **Maintenance reason:**
```html
<p>We are currently performing [REASON] to improve your experience.</p>
```

3. **Contact information:**
```html
<p>For urgent inquiries, email us at <a href="mailto:info@x4o.co.za">info@x4o.co.za</a></p>
```

4. **Page title:**
```html
<title>X4O - Scheduled Maintenance</title>
```

**Example customizations:**

```html
<!-- Domain migration -->
<h1>We're Upgrading Our Website</h1>
<p>We are migrating to a new hosting platform for improved performance.</p>
<p>Expected completion: February 15, 2026 at 2:00 PM SAST</p>

<!-- Security update -->
<h1>Security Update in Progress</h1>
<p>We are applying important security updates to keep your data safe.</p>
<p>We'll be back online within the hour.</p>

<!-- Major feature launch -->
<h1>Exciting Updates Coming Soon!</h1>
<p>We're adding new features to enhance your experience.</p>
<p>Check back at 3:00 PM SAST for the new site.</p>
```

### Styling Changes

The maintenance page uses inline CSS and matches X4O's brand colors:
- Primary Blue: `#97c0e8`
- Dark Blue: `#174069`
- White text on dark backgrounds

To change styling, edit the `<style>` section in `maintenance.html`.

---

## Important Notes

### What Continues to Work

✅ **Email Service** - Google Workspace email (@x4o.co.za) operates independently
✅ **Staging Site** - Staging branch deployments are unaffected
✅ **Netlify Dashboard** - All admin functions remain available
✅ **Git Repository** - GitHub repository is accessible

### What is Disabled

❌ **Website pages** - All routes redirect to maintenance page
❌ **Contact form** - Netlify Forms are inaccessible during maintenance
❌ **Navigation** - Links do not work (all redirect to maintenance page)
❌ **Analytics** - Page view tracking may be affected

### Duration Guidelines

- **Short maintenance (< 1 hour):** Acceptable without notice
- **Medium maintenance (1-4 hours):** Notify users via email/social media if possible
- **Long maintenance (> 4 hours):** Mandatory advance notice to stakeholders

### Communication Template

**Email/Social Media Post:**
```
🔧 Scheduled Maintenance Notice

We'll be performing scheduled maintenance on our website:
📅 Date: [DATE]
🕐 Time: [START TIME] - [END TIME] SAST
⏱️ Duration: Approximately [DURATION]

During this time:
- Website will be temporarily unavailable
- Email service continues to work normally
- For urgent inquiries: info@x4o.co.za

We apologize for any inconvenience and appreciate your patience.

- The X4O Team
```

---

## Emergency Rollback

If something goes wrong during or after enabling maintenance mode:

### Quick Rollback (Undo Last Commit)

```bash
# Check what the last commit changed
git log -1

# Revert the last commit (creates a new commit that undoes it)
git revert HEAD

# Push the revert
git push origin main
```

This immediately undoes the maintenance mode change and restores the site (1-2 minute build time).

### Nuclear Option (Hard Reset)

**⚠️ WARNING: This discards all uncommitted changes**

```bash
# Reset to the commit before maintenance mode
git log --oneline -5             # Find the commit hash before maintenance
git reset --hard <commit-hash>   # Reset to that commit
git push --force origin main     # Force push (requires approval)
```

Only use this if revert fails or you need instant rollback.

### Netlify Dashboard Rollback

1. Go to **Netlify Dashboard → Deploys**
2. Find the last successful deploy before maintenance mode
3. Click **⋮ (three dots)** → **Publish deploy**
4. Site instantly rolls back to that version

---

## Pre-Deployment Checklist

Before enabling maintenance mode, ensure:

- [ ] **Reason documented** - Why is maintenance needed?
- [ ] **Duration estimated** - How long will it take?
- [ ] **Supervisor notified** - Have leadership approval
- [ ] **Users notified** (if applicable) - Email/social media announcement sent
- [ ] **Staging tested** - Test maintenance page on staging first
- [ ] **Backup plan ready** - Know how to rollback if needed
- [ ] **Contact method confirmed** - Info@x4o.co.za is monitored
- [ ] **Team available** - Someone can respond to issues during maintenance
- [ ] **Re-enable plan scheduled** - Set calendar reminder to disable maintenance mode

---

## Example Workflows

### Workflow 1: Domain Migration

**Scenario:** Migrating x4o.co.za DNS from old registrar to Netlify DNS

1. **Pre-migration (1 week before):**
   - Email clients: "Website will be unavailable on [DATE] for 2-4 hours"
   - Update maintenance.html with expected downtime

2. **Day of migration:**
   - 9:00 AM: Enable maintenance mode via netlify.toml
   - 9:05 AM: Update DNS records at registrar
   - 9:30 AM - 11:00 AM: Monitor DNS propagation
   - 11:00 AM: Verify new DNS works
   - 11:10 AM: Disable maintenance mode

3. **Post-migration:**
   - Test all pages and contact form
   - Send "All clear" email to clients

### Workflow 2: Urgent Security Patch

**Scenario:** Critical security vulnerability in Astro framework

1. **Immediate action:**
   - Enable maintenance mode via Netlify Dashboard (instant)
   - Apply security patch locally
   - Test on staging branch

2. **Deployment:**
   - Push fix to main branch
   - Netlify builds with security patch
   - Disable maintenance mode via dashboard (instant)

3. **Total downtime:** 10-15 minutes

---

## Support and Contacts

**Website Administrator:** Keenan Husselmann (admin@x4o.co.za)
**Netlify Dashboard:** https://app.netlify.com/sites/x4oconsultants
**GitHub Repository:** https://github.com/X4OConsulting/X4O-Website

**Netlify Support:** https://www.netlify.com/support/ (if deployment issues occur)

---

**Document Version:** 2.0
**Last Reviewed:** February 13, 2026
**Next Review:** August 2026 (or before major changes)

---

**END OF DOCUMENT**
