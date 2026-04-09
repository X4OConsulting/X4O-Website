# Content Update Guide

**Last Updated:** February 13, 2026
**For:** X4O Website Administrators

---

## Quick Start

The X4O website is built with Astro (static site). To update content, you need to:
1. Edit `.astro` files in `src/pages/`
2. Build the site
3. Deploy via Git push

---

## Common Content Updates

### Update Homepage Hero Section

**File:** `src/pages/index.astro`
**Location:** Lines 10-25 (hero section)

```astro
<h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
  Your New Headline Here
</h1>
<p class="text-xl text-white/90 mb-8">
  Your new subheading text here
</p>
```

### Update Services Section

**File:** `src/pages/consulting-and-advisory-services.astro`
**Location:** Service cards section

```astro
<h3>Service Title</h3>
<p>Service description text goes here</p>
```

### Update Contact Information

**Files to Update:**
- `src/components/Footer.astro` (footer contact info)
- `src/pages/contact.astro` (contact page)

**Common Fields:**
- Email: `info@x4o.co.za`
- Phone: Update in Footer.astro
- Address: Update in Footer.astro

### Update Partner Logos

**File:** `src/pages/partners.astro`
**Image Location:** `public/images/`

**Steps:**
1. Add new logo to `public/images/partner_logo.png`
2. Edit `partners.astro`
3. Add new image tag:
```astro
<img src="/images/partner_logo.png" alt="Partner Name" />
```

---

## Text Content Updates

### Editing Page Text

**All text content is in `.astro` files:**
- Homepage: `src/pages/index.astro`
- Services: `src/pages/consulting-and-advisory-services.astro`
- Coaching: `src/pages/coaching-services.astro`
- Contact: `src/pages/contact.astro`

**How to Edit:**
1. Open file in text editor (VS Code recommended)
2. Find text to update (plain text between HTML tags)
3. Edit the text
4. Save file

### Adding New Pages

**Steps:**
1. Create new file: `src/pages/new-page.astro`
2. Copy structure from existing page
3. Update content
4. Add navigation link in `src/components/Header.astro`

---

## Image Updates

### Replace Images

**Image Location:** `public/images/`

**Steps:**
1. Add new image to `public/images/`
2. Keep same filename OR update references in `.astro` files
3. Recommended formats: JPG (photos), PNG (logos with transparency)
4. Optimize images before uploading (< 500KB recommended)

### Update Logo

**File:** `public/images/logo.png`
**Used In:** `src/components/Header.astro` and `Footer.astro`

**Steps:**
1. Replace `public/images/logo.png` with new logo
2. Keep filename same for automatic update
3. Or update references in Header.astro and Footer.astro

---

## Building and Deploying

### Local Testing

```bash
# Start development server
npm run dev

# View at http://localhost:4321
```

### Build for Production

```bash
# Create production build
npm run build

# Preview production build
npm run preview
```

### Deploy to Production

**Automatic Deployment via Git:**

```bash
# 1. Commit changes
git add .
git commit -m "Update homepage content"

# 2. Push to staging (test first)
git push origin staging

# 3. Verify staging: https://staging--x4oconsultants.netlify.app

# 4. Merge to main (production)
git checkout main
git merge staging
git push origin main

# 5. Auto-deploys to https://x4o.co.za in ~60 seconds
```

---

## Content Update Checklist

**Before Updating:**
- [ ] Have text/images ready
- [ ] Know which page to update
- [ ] Test locally first

**After Updating:**
- [ ] Verify locally (npm run dev)
- [ ] Build succeeds (npm run build)
- [ ] Test on staging before production
- [ ] Check mobile view
- [ ] Verify links still work

**After Deployment:**
- [ ] Check production site loads
- [ ] Test updated content displays correctly
- [ ] Verify no broken images/links

---

## Troubleshooting

**Build Fails:**
- Check for syntax errors in .astro files
- Missing quotes or closing tags
- Run `npm run build` to see error details

**Images Not Showing:**
- Verify image is in `public/images/`
- Check filename matches reference (case-sensitive)
- Use `/images/filename.png` path (leading slash)

**Content Not Updated:**
- Clear browser cache (Ctrl+Shift+R)
- Wait 1-2 minutes for CDN cache to clear
- Verify Git push succeeded

---

## Need Help?

**Documentation:**
- CLAUDE.md - Full technical documentation
- README.md - User-friendly guide
- Astro docs: https://docs.astro.build

**Contact:**
- Email: admin@x4o.co.za
- GitHub Issues: Report problems at repository

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
