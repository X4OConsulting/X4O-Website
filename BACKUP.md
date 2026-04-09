# X4O Website - Backup & Recovery Guide

**Document Type:** Disaster Recovery Procedures
**Purpose:** Backup strategies and recovery procedures for x4o.co.za
**Last Updated:** February 13, 2026
**Prepared By:** Keenan Husselmann

---

## Table of Contents

1. [Overview](#overview)
2. [Backup Strategy](#backup-strategy)
3. [What Gets Backed Up](#what-gets-backed-up)
4. [Recovery Procedures](#recovery-procedures)
5. [Content Backup (Original Wix Site)](#content-backup-original-wix-site)
6. [Asset Restoration](#asset-restoration)
7. [DNS Migration Reference](#dns-migration-reference)
8. [Emergency Contacts](#emergency-contacts)

---

## Overview

The X4O website is a **static site** hosted on **Netlify** with source code stored in **GitHub**. This architecture provides multiple layers of redundancy:

### Backup Layers

| Layer | Backup Method | Recovery Time | Location |
|-------|--------------|---------------|----------|
| **Source Code** | Git version control | 5 minutes | GitHub repository |
| **Deployment History** | Netlify deploy snapshots | 2 minutes | Netlify dashboard |
| **Assets** | Git + local copies | 10 minutes | GitHub + local machine |
| **Content** | Documentation files | 15 minutes | CLAUDE.md, content inventory |

### Recovery Time Objectives (RTO)

- **Minor issue (broken link, typo):** 5-10 minutes
- **Broken deployment:** 2-5 minutes (rollback via Netlify)
- **Catastrophic failure (repo deleted):** 30-60 minutes (restore from local clone)
- **Complete site rebuild:** 2-4 hours (from documentation)

### Recovery Point Objectives (RPO)

- **Maximum data loss:** Last Git commit (typically < 1 hour for active development)
- **Deployment history:** Last 100 deploys (Netlify retention)
- **Asset backup:** Up to date with Git commits

---

## Backup Strategy

### 1. Git Version Control (Primary Backup)

**What:** All source code, configuration, and documentation
**Where:** GitHub repository (https://github.com/X4OConsulting/X4O-Website)
**Frequency:** Every commit (continuous)
**Retention:** Unlimited history

**Branches:**
- `main` - Production code (live on x4o.co.za)
- `staging` - Development code (preview deployments)

**Recovery Method:**
```bash
# Clone repository from scratch
git clone https://github.com/X4OConsulting/X4O-Website.git x4o-website

# Or restore specific file from history
git checkout <commit-hash> -- path/to/file.astro
```

### 2. Netlify Deploy History (Secondary Backup)

**What:** Built site snapshots (HTML/CSS/JS output)
**Where:** Netlify dashboard (https://app.netlify.com/sites/x4oconsultants)
**Frequency:** Every deploy (automatic)
**Retention:** Last 100 deploys

**Recovery Method:**
1. Go to Netlify Dashboard → Deploys
2. Find the working deploy
3. Click **⋮ (three dots)** → **Publish deploy**
4. Site instantly reverts to that version

### 3. Local Development Clone (Tertiary Backup)

**What:** Complete repository copy on developer machine
**Where:** `c:\Users\keena\Projects\x4o-website-dev`
**Frequency:** Manual Git pull (daily/weekly)
**Retention:** Current state + local commits

**Recovery Method:**
```bash
# Push local changes to GitHub if remote is lost
git remote set-url origin https://github.com/X4OConsulting/X4O-Website.git
git push -u origin main
```

### 4. Documentation Backup

**What:** Project scope, content inventory, configuration notes
**Where:** CLAUDE.md, README.md, docs/ folder
**Frequency:** Updated with each major change
**Retention:** Full history in Git

---

## What Gets Backed Up

### Critical Files (Must Back Up)

#### 1. Source Code (`src/` directory)

```
src/
├── components/
│   ├── Header.astro         # Navigation component
│   └── Footer.astro         # Footer with social links
├── layouts/
│   └── Layout.astro         # Base HTML template
├── pages/
│   ├── index.astro          # Homepage
│   ├── consulting-and-advisory-services.astro
│   ├── coaching-services.astro
│   ├── book-coaching-sessions.astro
│   ├── contact.astro
│   ├── contact-success.astro
│   ├── partners.astro
│   └── 404.astro
└── styles/
    └── global.css           # Tailwind CSS + custom styles
```

**Backup status:** ✅ Fully backed up in Git

#### 2. Static Assets (`public/` directory)

```
public/
├── images/
│   ├── logo.png             # X4O company logo
│   ├── x4o_banner.jpg       # Hero banner image
│   ├── EdMeCa_logo.png      # EdMeCa partner logo
│   ├── idc-logo.png         # IDC partner logo
│   ├── mzilikazi_logo.png   # Mzilikazi partner logo
│   └── bg-image.jpg         # Background image
├── favicon.ico              # Browser favicon (ICO format)
├── favicon.jpg              # Favicon source (JPG)
└── maintenance.html         # Maintenance mode page
```

**Backup status:** ✅ Fully backed up in Git
**Original files:** Also stored locally at `c:\Users\keena\Projects\x4o-website-dev\public\images`

#### 3. Configuration Files

| File | Purpose |
|------|---------|
| `astro.config.mjs` | Astro framework configuration |
| `netlify.toml` | Netlify build and redirect rules |
| `package.json` | NPM dependencies and scripts |
| `package-lock.json` | Locked dependency versions |
| `tsconfig.json` | TypeScript compiler settings |
| `tailwind.config.mjs` | Tailwind CSS customization |
| `Dockerfile` | Docker container configuration |
| `docker-compose.yml` | Docker orchestration |

**Backup status:** ✅ All in Git repository

#### 4. Documentation Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Technical specification and developer guide |
| `README.md` | User-friendly project overview |
| `MAINTENANCE.md` | Maintenance mode procedures |
| `BACKUP.md` | This file (backup and recovery guide) |
| `SOCIAL-MEDIA-GUIDE.md` | Social media automation instructions |

**Backup status:** ✅ All in Git repository

---

## Recovery Procedures

### Scenario 1: Restore from Git History

**Use case:** Accidental file deletion, broken code change, or corrupted file

#### Quick Recovery (Restore Single File)

```bash
# 1. View file history to find last good version
git log --oneline -- src/pages/contact.astro

# 2. See what changed in a specific commit
git show <commit-hash>:src/pages/contact.astro

# 3. Restore file from that commit
git checkout <commit-hash> -- src/pages/contact.astro

# 4. Commit the restoration
git add src/pages/contact.astro
git commit -m "Restore contact page from commit <commit-hash>"
git push origin main
```

#### Full Repository Reset

```bash
# 1. Find last known good commit
git log --oneline -10

# 2. Hard reset to that commit (DANGER: loses all changes after)
git reset --hard <commit-hash>

# 3. Force push to GitHub (requires confirmation)
git push --force origin main
```

**⚠️ WARNING:** Hard reset discards all commits after the target commit. Use only when necessary.

#### Safe Alternative: Revert Commits

```bash
# Revert the last commit (creates new commit that undoes it)
git revert HEAD

# Revert multiple commits
git revert HEAD~3..HEAD  # Reverts last 3 commits

# Push the revert
git push origin main
```

---

### Scenario 2: Restore from Netlify Deploy History

**Use case:** Bad deployment, broken build, or production issue

#### Steps:

1. **Go to Netlify Dashboard:**
   - URL: https://app.netlify.com/sites/x4oconsultants/deploys

2. **Find a Working Deploy:**
   - Look for deploys with green checkmark (Published)
   - Check deploy date/time and commit message
   - Click deploy to see preview

3. **Test the Old Deploy:**
   - Click **Preview deploy** link
   - Verify it works correctly
   - Check contact form, navigation, images

4. **Restore (Publish) the Old Deploy:**
   - Click **⋮ (three dots)** next to the deploy
   - Select **Publish deploy**
   - Confirm the action

5. **Verify Site is Restored:**
   - Visit https://x4o.co.za
   - Test all functionality
   - Site is now restored (instant, no build required)

**Note:** This only restores the **deployed site**, not the Git repository. To sync Git with the restored version:

```bash
# Find the commit hash for the restored deploy (in Netlify dashboard)
git reset --hard <commit-hash>
git push --force origin main
```

---

### Scenario 3: Rebuild from Scratch

**Use case:** Complete repository loss, catastrophic data corruption, or learning exercise

#### Prerequisites:

- Documentation files (CLAUDE.md, README.md)
- Asset files (logo.png, x4o_banner.jpg, partner logos)
- Netlify account access
- GitHub account

#### Steps:

**1. Create New Repository**

```bash
# Create new directory
mkdir x4o-website-rebuild
cd x4o-website-rebuild

# Initialize Git
git init

# Create new repo on GitHub (via web UI)
# Then link local to remote:
git remote add origin https://github.com/X4OConsulting/X4O-Website-Rebuild.git
```

**2. Initialize Astro Project**

```bash
# Install Astro with Tailwind template
npm create astro@latest . -- --template minimal --typescript strict

# Add Tailwind CSS integration
npx astro add tailwind
```

**3. Install Dependencies**

```bash
npm install
```

**4. Restore Configuration Files**

Recreate from CLAUDE.md specifications:

- `astro.config.mjs` - Copy from CLAUDE.md Appendix
- `netlify.toml` - Copy from CLAUDE.md Infrastructure section
- `tailwind.config.mjs` - Copy Tailwind customization
- `tsconfig.json` - Use Astro strict preset

**5. Restore Source Code**

Use CLAUDE.md "Project Structure" section as reference:

- Create `src/components/Header.astro` and `Footer.astro`
- Create `src/layouts/Layout.astro`
- Create all pages in `src/pages/`
- Create `src/styles/global.css`

**6. Restore Assets**

Copy from local backup or original files:

- `public/images/` - All image assets
- `public/favicon.ico`
- `public/maintenance.html`

**7. Test Locally**

```bash
npm run dev
```

Visit http://localhost:4321 and verify all pages work.

**8. Deploy to Netlify**

```bash
# Build production version
npm run build

# Push to GitHub
git add .
git commit -m "Initial rebuild from documentation"
git push -u origin main
```

Connect repository to Netlify via dashboard and deploy.

**Estimated time:** 2-4 hours (depending on familiarity with codebase)

---

## Content Backup (Original Wix Site)

The following content was migrated from the original Wix site (scraped before migration). Use this as reference for content restoration if needed.

### Homepage Content

**Page Title:**
```
Enterprise Systems Delivery Advisory | X4O (Pty) Limited | Cape Town
```

**Meta Description:**
```
At X4O, we believe that technology should support and enhance your organization's success, not constrain it.
```

**Hero Section:**
```
Welcome to X4O
Supporting You As You Grow

We are a team of experienced professionals dedicated to helping organizations
leverage technology to achieve their strategic objectives.
```

**Services Overview:**

1. **Project & Programme Management**
   - Enterprise project delivery
   - Agile and waterfall methodologies
   - PMO setup and optimization

2. **Advisory Services (13 Areas)**
   - Business Process Optimization
   - Change Management
   - Digital Transformation
   - Enterprise Architecture
   - IT Governance
   - Risk Management
   - Strategy Development
   - Technology Selection
   - Vendor Management
   - Cloud Migration
   - Cybersecurity Advisory
   - Data Analytics
   - DevOps Implementation

3. **Renewable Energy Advisory (11 Service Areas)**
   - Solar PV systems design
   - Wind energy feasibility
   - Green hydrogen projects
   - Energy storage solutions
   - Grid integration studies
   - Regulatory compliance
   - Funding and financing
   - Project management
   - Due diligence
   - Operations and maintenance
   - Training and capacity building

4. **Coaching Services**
   - Personal Transformation Coaching
   - Corporate Governance Coaching
   - Leadership Coaching
   - Financial Coaching

### Coaching Sessions (Booking Page)

**Session Types:**

1. **Personal Transformation Coaching**
   - Duration: 1 hour 30 minutes
   - Price: Via Quote
   - Focus: Personal growth, career development, life balance

2. **Leadership Coaching**
   - Duration: 1 hour 30 minutes
   - Price: Via Quote
   - Focus: Leadership skills, team management, executive presence

3. **Corporate Governance Coaching**
   - Duration: 1 hour 30 minutes
   - Price: Via Quote
   - Focus: Board effectiveness, compliance, risk oversight

### Contact Information

**Email:**
- Primary: info@x4o.co.za
- Administrative: admin@x4o.co.za

**Location:**
- Durbanville, Cape Town, South Africa

**Company:**
- X4O (Pty) Limited

**Social Media:**
- LinkedIn: X4O Consultants
- Facebook: X4O Consultants
- Instagram: @x4oconsultants
- YouTube: X4O Consultants

### Partners

**Partner Organizations:**

1. **EdMeCa (Pty) Ltd**
   - Logo: `public/images/EdMeCa_logo.png`
   - Description: Educational and Mentorship Capacity Development

2. **IDC (Industrial Development Corporation)**
   - Logo: `public/images/idc-logo.png`
   - Description: South African national development finance institution

3. **Mzilikazi Development and Advisory Services**
   - Logo: `public/images/mzilikazi_logo.png`
   - Description: Advisory and development services

---

## Asset Restoration

### Image Assets Location

**Primary location:** `c:\Users\keena\Projects\x4o-website-dev\public\images`

**Backup location:** Git repository (GitHub)

### Asset Inventory

| File | Size | Format | Purpose |
|------|------|--------|---------|
| `logo.png` | ~50 KB | PNG (transparent) | Company logo (header) |
| `x4o_banner.jpg` | ~200 KB | JPEG | Hero banner (contact, partners pages) |
| `EdMeCa_logo.png` | ~30 KB | PNG | Partner logo |
| `idc-logo.png` | ~40 KB | PNG | Partner logo |
| `mzilikazi_logo.png` | ~35 KB | PNG | Partner logo |
| `bg-image.jpg` | ~150 KB | JPEG | Background image |
| `favicon.ico` | ~5 KB | ICO | Browser favicon |
| `favicon.jpg` | ~10 KB | JPEG | Favicon source |

### Restore Assets from Git

```bash
# Restore all images from specific commit
git checkout <commit-hash> -- public/images/

# Or restore single image
git checkout main -- public/images/logo.png

# Commit restoration
git add public/images/
git commit -m "Restore image assets"
git push origin main
```

### Asset Optimization (Future Enhancement)

**Recommended optimizations:**

1. **Convert to WebP format** (smaller file size, better compression)
   ```bash
   # Using cwebp tool
   cwebp -q 80 x4o_banner.jpg -o x4o_banner.webp
   ```

2. **Compress existing JPEGs**
   - Use TinyPNG or ImageOptim
   - Target: 70-80% quality, < 100 KB per image

3. **Add responsive images**
   - Generate multiple sizes (320w, 640w, 1024w, 1920w)
   - Use Astro Image component with srcset

---

## DNS Migration Reference

**⚠️ Use only when migrating domain or DNS provider**

### Current DNS Configuration (Netlify)

**A Record (Root Domain):**
```
Type: A
Name: @ (or blank)
Value: 75.2.60.5 (Netlify load balancer)
TTL: 3600 seconds (1 hour)
```

**CNAME Record (www subdomain):**
```
Type: CNAME
Name: www
Value: x4oconsultants.netlify.app
TTL: 3600 seconds
```

**MX Records (Google Workspace Email):**
```
Priority 1:  ASPMX.L.GOOGLE.COM
Priority 5:  ALT1.ASPMX.L.GOOGLE.COM
Priority 5:  ALT2.ASPMX.L.GOOGLE.COM
Priority 10: ALT3.ASPMX.L.GOOGLE.COM
Priority 10: ALT4.ASPMX.L.GOOGLE.COM
```

**⚠️ CRITICAL:** Never delete or modify MX records - email service will break!

### DNS Migration Workflow

**Scenario:** Moving domain from Registrar A to Registrar B

1. **Before Migration:**
   - Document all current DNS records (screenshot or export)
   - Verify Netlify is the authoritative DNS for x4o.co.za
   - Ensure Google Workspace email is working

2. **Migration Day:**
   - Update nameservers at new registrar to point to Netlify
   - OR recreate all DNS records at new registrar
   - Keep old registrar active until DNS propagates

3. **DNS Propagation (24-48 hours):**
   - Monitor with: `dig x4o.co.za` or `nslookup x4o.co.za`
   - Test website from different networks
   - Test email sending/receiving

4. **After Full Propagation:**
   - Verify website loads correctly (x4o.co.za and www.x4o.co.za)
   - Test contact form submissions
   - Test email delivery
   - Cancel old registrar service

### DNS Verification Commands

```bash
# Check A record
nslookup x4o.co.za

# Check CNAME record
nslookup www.x4o.co.za

# Check MX records
nslookup -type=MX x4o.co.za

# Detailed DNS info
dig x4o.co.za ANY
```

---

## Emergency Contacts

### Internal Contacts

**Website Administrator:**
- Name: Keenan Husselmann
- Email: admin@x4o.co.za
- Role: Project owner, site administrator

**Company Email:**
- General: info@x4o.co.za
- Administrative: admin@x4o.co.za

### External Services

**Hosting Platform:**
- Service: Netlify
- Dashboard: https://app.netlify.com/sites/x4oconsultants
- Support: https://www.netlify.com/support/
- Status: https://www.netlifystatus.com/

**Version Control:**
- Service: GitHub
- Repository: https://github.com/X4OConsulting/X4O-Website
- Support: https://support.github.com/

**Email Provider:**
- Service: Google Workspace
- Admin Console: https://admin.google.com
- Support: https://support.google.com/a/

**Domain Registrar:**
- Provider: [Update with actual registrar]
- Login: [Add when known]
- Support: [Add when known]

---

## Backup Verification Checklist

Perform quarterly (every 3 months):

- [ ] Verify Git repository is accessible and up-to-date
- [ ] Check Netlify deploy history shows recent builds
- [ ] Confirm local clone exists and is synced
- [ ] Test Git restore procedure (restore old file, then revert)
- [ ] Test Netlify rollback (publish old deploy, then re-publish current)
- [ ] Verify all asset files are in Git repository
- [ ] Review documentation files (CLAUDE.md, README.md) for accuracy
- [ ] Update this backup guide if procedures have changed

---

## Document Information

**Document Version:** 2.0
**Last Updated:** February 13, 2026
**Last Tested:** February 13, 2026
**Next Review:** May 2026 (Quarterly)

**Related Documents:**
- CLAUDE.md - Technical specification
- MAINTENANCE.md - Maintenance mode procedures
- README.md - User-friendly project guide

---

**END OF DOCUMENT**
