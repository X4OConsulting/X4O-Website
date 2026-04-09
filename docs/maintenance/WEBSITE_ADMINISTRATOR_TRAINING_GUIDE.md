# Website Administrator Training Guide

**Website:** https://x4o.co.za
**For:** X4O Website Administrators
**Last Updated:** February 13, 2026

---

## Welcome!

This guide will teach you everything you need to manage the X4O website, even if you're not a developer.

**What You'll Learn:**
- How to update text content
- How to change images
- How to add new pages
- How to deploy changes
- Common troubleshooting

---

## Prerequisites

### Required Tools

**1. Text Editor (Choose One):**
- **VS Code** (Recommended) - Free, user-friendly
  - Download: https://code.visualstudio.com/
- Notepad++ (Windows alternative)
- TextEdit (Mac - use plain text mode)

**2. Git (Version Control):**
- Download: https://git-scm.com/downloads
- Used to save and deploy changes

**3. Node.js (Build Tool):**
- Download: https://nodejs.org/ (LTS version)
- Used to build the website locally

### Required Accounts

**1. GitHub Account:**
- Repository: https://github.com/X4OConsulting/X4O-Website
- Access: Contact admin@x4o.co.za for access

**2. Netlify Account:**
- Dashboard: https://app.netlify.com/
- Access: Contact admin@x4o.co.za for access

---

## Section 1: Understanding the Website

### What is a Static Site?

The X4O website is a **static site**, meaning:
- No database (all content is in files)
- Pre-built pages (faster loading)
- Deployed via Git (changes tracked)

### File Structure (Simplified)

```
x4o-website-dev/
├── src/
│   ├── pages/           ← Your content is here
│   │   ├── index.astro       (Homepage)
│   │   ├── contact.astro      (Contact page)
│   │   └── ...                (Other pages)
│   ├── components/      ← Header and Footer
│   └── layouts/         ← Page template
├── public/              ← Images and static files
│   └── images/          ← All images here
└── docs/                ← Documentation (guides)
```

**What You'll Edit:**
- `src/pages/*.astro` - Page content
- `public/images/` - Images

---

## Section 2: Making Your First Update

### Step-by-Step: Update Homepage Text

**Goal:** Change the homepage headline

**Step 1: Open Project in VS Code**

1. Open VS Code
2. File → Open Folder
3. Select `x4o-website-dev` folder
4. Click "Open"

**Step 2: Find the File**

1. In left sidebar, click `src` folder
2. Click `pages` folder
3. Click `index.astro`

**Step 3: Find the Text**

Press `Ctrl+F` (Windows) or `Cmd+F` (Mac) and search for the current headline.

**Step 4: Edit the Text**

```astro
<!-- OLD -->
<h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
  Welcome to X4O Consultants
</h1>

<!-- NEW -->
<h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
  Your New Headline Here
</h1>
```

**Step 5: Save the File**

Press `Ctrl+S` (Windows) or `Cmd+S` (Mac)

**Step 6: Test Locally (Optional but Recommended)**

Open Terminal in VS Code (View → Terminal):
```bash
npm run dev
```

Open browser to `http://localhost:4321` and verify your change.

**Step 7: Deploy (See Section 3)**

---

## Section 3: Deploying Changes

### Method 1: Using VS Code (Recommended)

**Step 1: Save All Changes**

File → Save All (or `Ctrl+K S`)

**Step 2: Open Source Control**

Click Source Control icon in left sidebar (looks like branches)

**Step 3: Stage Changes**

Click `+` next to changed files (or click `+` next to "Changes" to stage all)

**Step 4: Write Commit Message**

In text box at top, write a brief description:
```
Update homepage headline
```

**Step 5: Commit**

Click the checkmark icon (✓) or press `Ctrl+Enter`

**Step 6: Push to Staging**

1. Click `...` (three dots) at top of Source Control panel
2. Click "Push to..." → select "staging"
3. Wait for confirmation

**Step 7: Verify on Staging**

Open: https://staging--x4oconsultants.netlify.app

Check if your change looks correct.

**Step 8: Deploy to Production**

1. In Source Control, click `...` → Branch → Checkout to → "main"
2. Click `...` → Branch → Merge Branch → select "staging"
3. Click `...` → Push
4. Wait 1-2 minutes for deployment

**Step 9: Verify on Production**

Open: https://x4o.co.za

Your change should now be live!

### Method 2: Using Command Line

For advanced users comfortable with terminal:

```bash
# 1. Stage changes
git add .

# 2. Commit changes
git commit -m "Update homepage headline"

# 3. Push to staging (test first)
git push origin staging

# 4. Verify staging works

# 5. Merge staging to main (production)
git checkout main
git merge staging
git push origin main
```

---

## Section 4: Common Tasks

### Task 1: Update Contact Information

**Files to Edit:**
- `src/components/Footer.astro` (footer email/phone)
- `src/pages/contact.astro` (contact page)

**Example: Update Email Address**

In `Footer.astro`, find:
```astro
<a href="mailto:info@x4o.co.za">info@x4o.co.za</a>
```

Change to:
```astro
<a href="mailto:newemail@x4o.co.za">newemail@x4o.co.za</a>
```

Save, commit, push (see Section 3).

### Task 2: Update an Image

**Step 1: Prepare New Image**

- Resize to appropriate size (homepage banner: 1920×1080px max)
- Compress image (use https://tinypng.com/)
- Save with descriptive filename (e.g., `new_banner.jpg`)

**Step 2: Add Image to Project**

1. Copy your image file
2. Paste into `public/images/` folder
3. Note the exact filename

**Step 3: Update Image Reference**

If replacing existing image, you can either:

**Option A:** Keep same filename (automatic update)
- Replace `public/images/old_image.jpg` with new image
- Rename new image to match old filename
- Deploy (no code changes needed)

**Option B:** Update reference in code
- Add new image to `public/images/new_image.jpg`
- Find old image reference in `.astro` file:
  ```astro
  <img src="/images/old_image.jpg" alt="Description" />
  ```
- Change to:
  ```astro
  <img src="/images/new_image.jpg" alt="Description" />
  ```

Save, commit, push.

### Task 3: Add New Service to Services Page

**File:** `src/pages/consulting-and-advisory-services.astro`

**Find the Services Section:**

Look for existing service card:
```astro
<div class="glass-card p-8 rounded-xl">
  <h3 class="text-2xl font-semibold text-primary-dark mb-4">
    Existing Service
  </h3>
  <p class="text-gray-700 leading-relaxed">
    Service description here.
  </p>
</div>
```

**Copy and Paste Below:**

Duplicate the entire `<div class="glass-card...">...</div>` block.

**Update Text:**

Change the heading and description to your new service.

Save, commit, push.

### Task 4: Update Navigation Menu

**File:** `src/components/Header.astro`

**Find Navigation Section:**

Look for:
```astro
<nav class="hidden md:flex space-x-8">
  <a href="/">Home</a>
  <a href="/contact">Contact</a>
  <!-- Add new link here -->
</nav>
```

**Add New Link:**

```astro
<a href="/new-page">New Page Name</a>
```

Save, commit, push.

---

## Section 5: Adding a New Page

**Step 1: Create New File**

1. Right-click `src/pages/` folder in VS Code
2. Click "New File"
3. Name it: `my-new-page.astro`

**Step 2: Copy Template from Existing Page**

1. Open `src/pages/partners.astro` (simple page to copy)
2. Copy all content (`Ctrl+A`, `Ctrl+C`)
3. Paste into your new file (`Ctrl+V`)

**Step 3: Update Page Content**

Change the frontmatter (top section):
```astro
---
import Layout from '../layouts/Layout.astro';
const pageTitle = "My New Page Title";
const pageDescription = "Description for SEO (150-160 characters)";
---
```

Change the page content:
```astro
<Layout title={pageTitle} description={pageDescription}>
  <main>
    <section class="py-20">
      <div class="container mx-auto px-4">
        <h1>My New Page Heading</h1>
        <p>Your content here...</p>
      </div>
    </section>
  </main>
</Layout>
```

**Step 4: Add to Navigation**

Edit `src/components/Header.astro` and add link:
```astro
<a href="/my-new-page">New Page</a>
```

**Step 5: Test Locally**

```bash
npm run dev
```

Visit: http://localhost:4321/my-new-page

**Step 6: Deploy**

Save, commit, push (see Section 3).

Your new page will be at: https://x4o.co.za/my-new-page

---

## Section 6: Troubleshooting

### Problem: Build Failed

**Symptoms:** Error message when pushing to Git

**Common Causes:**
- Syntax error in .astro file (missing quote, bracket, etc.)
- Image file referenced but not uploaded

**Solution:**
1. Read error message carefully
2. Check for typos in code
3. Verify all image files exist in `public/images/`
4. Test locally: `npm run build`

### Problem: Changes Not Showing

**Symptoms:** Pushed to production but old content still shows

**Solutions:**
1. Clear browser cache (`Ctrl+Shift+R` or `Cmd+Shift+R`)
2. Wait 1-2 minutes for CDN cache to clear
3. Verify Git push succeeded (check GitHub repository)
4. Check Netlify deploy log for errors

### Problem: Image Not Displaying

**Common Causes:**
- Image filename doesn't match reference (case-sensitive)
- Image not in `public/images/` folder
- Forgot leading slash in path

**Check:**
```astro
<!-- Correct -->
<img src="/images/photo.jpg" alt="Description" />

<!-- Wrong (missing leading slash) -->
<img src="images/photo.jpg" alt="Description" />

<!-- Wrong (wrong folder) -->
<img src="/photo.jpg" alt="Description" />
```

### Problem: Form Not Sending Emails

**Check:**
1. Netlify dashboard → Site settings → Forms
2. Verify email notification is configured
3. Check spam folder for form emails
4. Test with real email address (not disposable)

**Fix:**
1. Go to Netlify dashboard
2. Site settings → Forms → Form notifications
3. Add email notification to admin@x4o.co.za

### Problem: "Permission Denied" Error

**Cause:** Don't have write access to GitHub repository

**Solution:**
Contact admin@x4o.co.za to request access.

---

## Section 7: Monthly Maintenance

### Checklist (30 minutes/month)

**Content Review:**
- [ ] Check all pages load correctly
- [ ] Verify contact information is current
- [ ] Test contact form submission
- [ ] Review and respond to form submissions

**Security:**
- [ ] Run security tests: `npm audit`
- [ ] Check for dependency updates
- [ ] Verify SSL certificate is valid (should auto-renew)

**Performance:**
- [ ] Run Lighthouse audit (Chrome DevTools)
- [ ] Check page load speeds
- [ ] Verify all images load

**Backup:**
- [ ] Verify GitHub repository has latest changes
- [ ] Export local backup (optional)

---

## Section 8: Getting Help

### Documentation Resources

**Main Guides:**
- `README.md` - Project overview
- `CLAUDE.md` - Full technical documentation
- `docs/maintenance/CONTENT_UPDATE_GUIDE.md` - Detailed content updates
- `docs/maintenance/SEO_BEST_PRACTICES_GUIDE.md` - SEO tips
- `docs/maintenance/PERFORMANCE_OPTIMIZATION_GUIDE.md` - Speed optimization
- `CHANGELOG.md` - Version history

### Support Contacts

**Website Issues:**
- Email: admin@x4o.co.za

**Technical Documentation:**
- Astro Docs: https://docs.astro.build/
- Tailwind Docs: https://tailwindcss.com/docs
- Netlify Docs: https://docs.netlify.com/

### Common Questions

**Q: How often should I update the website?**
A: Update whenever content needs changing. Test on staging first for major changes.

**Q: Can I break the website?**
A: Unlikely! Changes are versioned in Git, so you can always revert. Test on staging first.

**Q: What happens if I delete a file by accident?**
A: Git tracks all changes. You can restore any deleted file from version history.

**Q: How do I know if the site is down?**
A: Set up UptimeRobot (see Phase 7 tasks) for automatic monitoring and alerts.

**Q: Should I edit files on Netlify or GitHub?**
A: Always edit locally in VS Code, then push to GitHub. Don't edit directly on web platforms.

---

## Section 9: Quick Reference

### File Locations

| What to Update | File Location |
|----------------|---------------|
| **Homepage content** | `src/pages/index.astro` |
| **Services pages** | `src/pages/consulting-and-advisory-services.astro`, etc. |
| **Contact form** | `src/pages/contact.astro` |
| **Navigation menu** | `src/components/Header.astro` |
| **Footer** | `src/components/Footer.astro` |
| **Images** | `public/images/` |

### Essential Commands

```bash
# Install dependencies (first time)
npm install

# Start local development server
npm run dev

# Build for production (test before deploying)
npm run build

# Preview production build
npm run preview

# Check for vulnerabilities
npm audit
```

### Git Commands

```bash
# See what changed
git status

# Stage all changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to staging
git push origin staging

# Switch to main branch
git checkout main

# Merge staging to main
git merge staging

# Push to production
git push origin main
```

---

## Congratulations!

You now know the basics of managing the X4O website. Remember:

1. **Test locally first** (`npm run dev`)
2. **Deploy to staging** before production
3. **Commit often** with clear messages
4. **Ask for help** when unsure

**Questions?** Contact admin@x4o.co.za

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
**For:** X4O Website Administrators
