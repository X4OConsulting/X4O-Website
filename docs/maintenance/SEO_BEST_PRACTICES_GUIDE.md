# SEO Best Practices Guide

**Last Updated:** February 13, 2026
**For:** X4O Website Administrators

---

## Current SEO Status

**Implemented:**
- ✅ HTTPS enforcement
- ✅ Mobile-responsive design
- ✅ Fast page loads (Lighthouse 95+)
- ✅ Semantic HTML
- ✅ Meta descriptions on all pages
- ✅ OpenGraph tags for social sharing
- ✅ Alt text on images
- ✅ Clean URLs (no query parameters)

**Missing (Phase 7 Tasks):**
- ⏸️ robots.txt file
- ⏸️ sitemap.xml
- ⏸️ JSON-LD structured data

---

## SEO Checklist for Content Updates

### Every Page Should Have:

**1. Unique Page Title (50-60 characters)**
```astro
<Layout title="Your Page Title Here | X4O Consultants">
```

**2. Meta Description (150-160 characters)**
```astro
<Layout
  title="Page Title"
  description="Compelling description that makes users want to click. Include keywords naturally."
>
```

**3. One H1 Heading Per Page**
```astro
<h1>Main Page Heading (Use Primary Keyword)</h1>
```

**4. Structured Headings (H2, H3)**
```astro
<h2>Section Heading</h2>
<h3>Subsection Heading</h3>
```

**5. Alt Text on All Images**
```astro
<img src="/images/logo.png" alt="X4O Consultants logo" />
```

---

## Keyword Strategy

### Target Keywords

**Primary Keywords:**
- Project management consulting
- Advisory services South Africa
- Renewable energy consulting
- Business coaching Durbanville

**Long-tail Keywords:**
- Project management consultants Cape Town
- Business advisory services South Africa
- Executive coaching Durbanville
- Renewable energy project management

### Where to Use Keywords

**High Priority:**
- Page titles (frontmatter `title`)
- H1 headings
- First paragraph of page
- Meta descriptions

**Medium Priority:**
- H2/H3 subheadings
- Image alt text
- Navigation anchor text

**Low Priority (Use Naturally):**
- Body content
- Footer text

---

## Content Best Practices

### Writing for SEO

**Good:**
- Natural language
- Answer user questions
- Clear, concise paragraphs
- Keyword density 1-2% (natural usage)

**Avoid:**
- Keyword stuffing
- Duplicate content
- Thin content (< 300 words)
- Hidden text

### Content Length

**Recommended:**
- Homepage: 400-600 words
- Service pages: 600-1000 words
- Blog posts (if added): 1000-2000 words

### Internal Linking

**Link to related pages:**
```astro
<a href="/consulting-and-advisory-services">Learn more about our consulting services</a>
```

**Benefits:**
- Helps users navigate
- Distributes page authority
- Helps search engines understand site structure

---

## Technical SEO

### URL Structure

**Good URLs:**
- `/consulting-and-advisory-services` ✅
- `/coaching-services` ✅
- `/partners` ✅

**Bad URLs:**
- `/page?id=123` ❌
- `/content.php` ❌
- `/p123` ❌

### Site Speed

**Current Status:** Excellent (Lighthouse 95+)

**To Maintain:**
- Optimize images (< 500KB)
- Minimize large JavaScript files
- Use WebP format (Phase 7 enhancement)

### Mobile-Friendliness

**Current Status:** Fully responsive

**Test:** Google Mobile-Friendly Test
https://search.google.com/test/mobile-friendly

---

## Future SEO Enhancements (Phase 7)

### 1. Create robots.txt

**File:** `public/robots.txt`
**Content:**
```
User-agent: *
Allow: /
Sitemap: https://x4o.co.za/sitemap.xml

User-agent: *
Disallow: /admin/
Disallow: /private/
```

**Why:** Tells search engines which pages to crawl

### 2. Create sitemap.xml

**Installation:**
```bash
npm install @astrojs/sitemap
```

**Configuration:** `astro.config.mjs`
```javascript
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://x4o.co.za',
  integrations: [tailwind(), sitemap()],
});
```

**Why:** Helps search engines discover all pages

### 3. Add JSON-LD Structured Data

**Organization Schema:**
```astro
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "X4O Consultants Pty Ltd",
  "url": "https://x4o.co.za",
  "logo": "https://x4o.co.za/images/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "info@x4o.co.za",
    "contactType": "Customer Service"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Durbanville",
    "addressRegion": "Western Cape",
    "addressCountry": "ZA"
  }
}
</script>
```

**Why:** Rich snippets in search results

---

## Google Search Console Setup

### 1. Verify Ownership

**URL:** https://search.google.com/search-console

**Verification Methods:**
- HTML file upload to `public/` folder
- DNS TXT record (via IT-Guru)
- HTML meta tag in Layout.astro

### 2. Submit Sitemap

**After creating sitemap.xml:**
1. Go to Search Console → Sitemaps
2. Submit: `https://x4o.co.za/sitemap.xml`

### 3. Monitor Performance

**Check Weekly:**
- Total clicks and impressions
- Average position
- Top queries
- Pages with errors

---

## Local SEO

### Google My Business

**Recommended Setup:**
1. Create Google Business Profile
2. Add business info:
   - Name: X4O Consultants Pty Ltd
   - Category: Business Consulting
   - Address: Durbanville, Cape Town
   - Phone: [Your phone]
   - Website: https://x4o.co.za
3. Verify business
4. Add photos and description

### Local Citations

**List Business On:**
- Google Business Profile
- Bing Places
- Yellow Pages South Africa
- Snupit
- Brabys

**Consistency is Key:**
- Use same business name everywhere
- Same address format
- Same phone number

---

## Social Media SEO

### OpenGraph Tags (Already Implemented)

**Current Implementation:**
```astro
<meta property="og:type" content="website" />
<meta property="og:url" content="https://x4o.co.za/" />
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="Page description" />
<meta property="og:image" content="https://x4o.co.za/images/og-image.jpg" />
```

**Benefits:**
- Better social media sharing
- Professional link previews
- More clicks from social

### Recommended: Add Open Graph Image

**Create:** 1200×630px image for social sharing
**Save As:** `public/images/og-image.jpg`
**Update:** Layout.astro with image URL

---

## SEO Monitoring

### Key Metrics to Track

**Weekly:**
- Google Search Console impressions/clicks
- Top performing pages
- Search queries bringing traffic

**Monthly:**
- Lighthouse SEO score (should stay 95+)
- Page speed (Core Web Vitals)
- Broken links check

**Quarterly:**
- Keyword ranking changes
- Competitor analysis
- Content refresh needs

### Tools

**Free:**
- Google Search Console
- Google Analytics (once implemented)
- Google PageSpeed Insights
- Bing Webmaster Tools

**Paid (Optional):**
- SEMrush
- Ahrefs
- Moz

---

## Quick SEO Wins

### 1. Update Meta Descriptions

Make them compelling and unique per page (not just keyword stuffing).

### 2. Add Alt Text to All Images

Describe what's in the image naturally.

### 3. Fix Broken Links

Run link checker monthly, fix any 404s.

### 4. Add Internal Links

Link service pages to each other where relevant.

### 5. Improve Page Load Speed

Optimize any large images (compress before uploading).

---

## Troubleshooting

**Page Not Showing in Google:**
- Check robots.txt isn't blocking
- Submit sitemap to Search Console
- Wait 2-4 weeks for indexing
- Request indexing in Search Console

**Ranking Dropped:**
- Check for technical errors
- Verify site is still mobile-friendly
- Check Core Web Vitals
- Review content quality

**Low Click-Through Rate:**
- Improve meta descriptions
- Make titles more compelling
- Add structured data for rich snippets

---

## SEO Checklist for New Pages

When adding new pages:
- [ ] Unique, descriptive title (50-60 chars)
- [ ] Compelling meta description (150-160 chars)
- [ ] One H1 with primary keyword
- [ ] H2/H3 subheadings with related keywords
- [ ] 600+ words of quality content
- [ ] Alt text on all images
- [ ] Internal links to/from related pages
- [ ] Mobile-responsive check
- [ ] Page speed test (< 3 seconds)
- [ ] Add to sitemap (auto with @astrojs/sitemap)

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
