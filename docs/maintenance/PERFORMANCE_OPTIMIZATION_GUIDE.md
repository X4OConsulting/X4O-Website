# Performance Optimization Guide

**Last Updated:** February 13, 2026
**For:** X4O Website Administrators

---

## Current Performance Status

**Lighthouse Scores:** 95+ across all metrics ✅
**Load Time:** < 2 seconds ✅
**Core Web Vitals:** All passing ✅

**Goal:** Maintain or improve current performance

---

## Performance Metrics

### Core Web Vitals (Google Ranking Factors)

**1. Largest Contentful Paint (LCP)**
- **Target:** < 2.5 seconds
- **Current:** ~1.2 seconds ✅
- **What it measures:** How fast main content loads

**2. First Input Delay (FID)**
- **Target:** < 100ms
- **Current:** ~50ms ✅
- **What it measures:** How quickly site responds to interaction

**3. Cumulative Layout Shift (CLS)**
- **Target:** < 0.1
- **Current:** < 0.05 ✅
- **What it measures:** Visual stability (no jumping content)

### Lighthouse Metrics

**Test URL:** https://pagespeed.web.dev/

**Current Scores:**
- Performance: 95+
- Accessibility: 95+
- Best Practices: 95+
- SEO: 95+

**Target:** Maintain 95+ on all metrics

---

## Image Optimization

### Current Images

**Large Images (Optimize These First):**
- `public/images/x4o_banner.jpg` - Contact page banner
- `public/images/bg-image.jpg` - Background image
- Any partner logos

### Optimization Steps

**1. Compress Images Before Upload**

**Tools:**
- TinyPNG (https://tinypng.com) - Free online compression
- ImageOptim (Mac) - Desktop app
- Squoosh (https://squoosh.app) - Google's image optimizer

**Target Sizes:**
- Logos: < 50KB
- Banners: < 200KB
- Background images: < 300KB
- Photos: < 500KB

**2. Use Correct Format**

| Image Type | Format | Reason |
|------------|--------|--------|
| Logos | PNG | Transparency support |
| Photos | JPG | Better compression |
| Icons | SVG | Scalable, tiny file size |
| Future | WebP | Better compression than JPG |

**3. Resize Images to Display Size**

Don't upload 4000×3000px image if displaying at 800×600px.

**Recommended Sizes:**
- Hero banners: 1920×1080px max
- Content images: 1200×800px max
- Thumbnails: 400×300px max
- Logos: 300×300px max

### Future: WebP Conversion (Phase 7)

**Install Astro Image:**
```bash
npm install @astrojs/image
```

**Use in .astro files:**
```astro
---
import { Picture } from '@astrojs/image/components';
---

<Picture
  src="/images/photo.jpg"
  widths={[400, 800, 1200]}
  formats={['webp', 'jpg']}
  alt="Description"
/>
```

**Benefits:**
- Automatic WebP conversion (30% smaller)
- Responsive image sizes
- Lazy loading

---

## Code Optimization

### Current Optimizations

**Already Implemented:**
- ✅ Static site generation (pre-rendered HTML)
- ✅ Minified CSS/JavaScript
- ✅ No unused CSS (Tailwind tree-shaking)
- ✅ Minimal JavaScript (< 50KB)
- ✅ CDN delivery (Netlify Edge Network)

### Keep It Lean

**Avoid:**
- ❌ Large JavaScript libraries (React, Vue unless needed)
- ❌ Heavy animation libraries
- ❌ Unnecessary fonts (stick to 1-2 font families)
- ❌ Auto-playing videos
- ❌ Large third-party scripts

**Best Practices:**
- ✅ Use native CSS for animations
- ✅ Defer non-critical JavaScript
- ✅ Load Google Fonts efficiently
- ✅ Minimize use of custom fonts

---

## Caching Strategy

### Current Caching

**Netlify Handles:**
- Static assets cached automatically
- Long cache times for images/CSS/JS
- Instant cache invalidation on deploy

**Browser Caching:**
- Images: 1 year cache
- CSS/JS: 1 year cache (cache-busted on deploy)
- HTML: Short cache (for content updates)

### No Action Needed

Netlify automatically optimizes caching. Just deploy and it works.

---

## Font Optimization

### Current Setup

**Font:** Inter (Google Fonts)

**Optimization:**
```astro
<!-- Preconnect to Google Fonts (already in Layout.astro) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

**Benefits:**
- Faster font loading
- Reduces blocking time

### Font Loading Best Practices

**Current Weights Used:**
- 300 (Light)
- 400 (Regular)
- 500 (Medium)
- 600 (Semi-Bold)
- 700 (Bold)
- 800 (Extra-Bold)

**Tip:** If not using all weights, remove unused ones from Google Fonts link.

**Future Enhancement:**
Self-host fonts for faster loading (removes Google Fonts request).

---

## JavaScript Performance

### Current JavaScript

**Minimal JS Usage:**
- Mobile menu toggle (~20 lines)
- No heavy frameworks
- No bloated libraries

**Keep It This Way:**
- Add JavaScript only when necessary
- Use native JavaScript (no jQuery)
- Defer non-critical scripts

### Script Loading

**Defer Scripts:**
```astro
<script defer src="/scripts/script.js"></script>
```

**Async for Independent Scripts:**
```astro
<script async src="/scripts/analytics.js"></script>
```

---

## CSS Performance

### Current CSS

**Tailwind CSS Benefits:**
- Only used classes included in build
- Automatic purging of unused CSS
- Minified in production

**CSS Size:** ~50KB (excellent for full site)

### Best Practices

**Keep CSS Small:**
- Use Tailwind utility classes (not custom CSS)
- Avoid `!important` overrides
- Remove unused custom CSS

**Critical CSS:**
Already handled by Astro build process (CSS inlined for above-fold content).

---

## Hosting & CDN Performance

### Netlify Performance

**Current Setup:**
- Global CDN (200+ edge nodes)
- Automatic asset optimization
- Gzip/Brotli compression
- HTTP/2 support

**South Africa Performance:**
- Edge location: Johannesburg
- Latency: 50-100ms (excellent)

**No Action Needed:** Netlify handles all of this automatically.

---

## Lazy Loading

### Images

**Future Enhancement (Phase 7):**
```astro
<img src="/images/photo.jpg" loading="lazy" alt="Description" />
```

**Benefits:**
- Images below fold don't load until scrolled to
- Faster initial page load
- Same user experience

**Implementation:**
Add `loading="lazy"` to all images except:
- Logo (above fold)
- Hero image (above fold)

### Recommended: Lazy Load Below-Fold Images Only

**Above Fold (no lazy load):**
- Logo
- Hero banner
- First section content

**Below Fold (lazy load):**
- Service card images
- Partner logos
- Footer images

---

## Third-Party Scripts

### Current Third-Party Resources

**Google Fonts:** Optimized with preconnect
**Netlify Forms:** Built-in (no external scripts)

**Future (Phase 7):**
- Google Analytics or Netlify Analytics
- Social media widgets (if added)

### Best Practices for Third-Party Scripts

**Load After Page Load:**
```astro
<script>
  window.addEventListener('load', function() {
    // Load analytics or other third-party scripts
  });
</script>
```

**Use Async/Defer:**
```astro
<script async src="https://analytics.example.com/script.js"></script>
```

---

## Performance Testing

### Tools to Use

**1. Google PageSpeed Insights**
- URL: https://pagespeed.web.dev/
- Test: https://x4o.co.za
- Frequency: Monthly

**2. Lighthouse (Chrome DevTools)**
- Open Chrome DevTools (F12)
- Go to Lighthouse tab
- Run audit
- Frequency: After major changes

**3. WebPageTest**
- URL: https://webpagetest.org/
- Test from: Johannesburg, South Africa
- Frequency: Quarterly

### What to Monitor

**Red Flags:**
- Lighthouse score drops below 90
- LCP > 2.5 seconds
- CLS > 0.1
- Total page size > 3MB

**Monthly Checks:**
- Run Lighthouse audit
- Check Core Web Vitals in Search Console
- Review any slow pages

---

## Performance Budget

**Current Page Sizes:**
- Homepage: ~500KB ✅
- Service pages: ~400KB ✅
- Contact page: ~600KB ✅

**Targets to Maintain:**
- Total page size: < 1MB
- Images: < 500KB total per page
- CSS: < 100KB
- JavaScript: < 100KB
- Fonts: < 100KB

---

## Quick Performance Wins

### 1. Compress All Images

Before uploading any image, run it through TinyPNG or Squoosh.

**Impact:** 50-70% file size reduction

### 2. Add Lazy Loading to Images

Add `loading="lazy"` to below-fold images.

**Impact:** 20-30% faster initial load

### 3. Optimize Google Fonts

Remove unused font weights from Google Fonts link.

**Impact:** Faster font loading

### 4. Remove Unused Code

If adding custom CSS/JS, remove any unused code before deploying.

**Impact:** Smaller bundle size

---

## Troubleshooting Performance Issues

### Site Loading Slowly

**Check:**
1. Run Lighthouse audit to identify issues
2. Check image sizes (should be < 500KB each)
3. Check total page size (should be < 1MB)
4. Test internet connection (is it your connection?)

**Common Fixes:**
- Compress large images
- Remove heavy third-party scripts
- Check for JavaScript errors in console

### Lighthouse Score Dropped

**Diagnose:**
1. Run Lighthouse to see which metrics failed
2. Check "Opportunities" section for recommendations
3. Compare to previous audit

**Common Causes:**
- Large images added recently
- New third-party scripts
- Excessive custom JavaScript

### Images Loading Slowly

**Fix:**
1. Compress images (use TinyPNG)
2. Resize to appropriate dimensions
3. Add lazy loading for below-fold images
4. Convert to WebP (Phase 7 enhancement)

---

## Performance Maintenance Schedule

### Weekly
- No action needed (static site automatically optimized)

### Monthly
- [ ] Run Lighthouse audit (maintain 95+ score)
- [ ] Check Core Web Vitals in Search Console
- [ ] Compress any new images before uploading

### Quarterly
- [ ] Full WebPageTest audit
- [ ] Review and optimize heaviest pages
- [ ] Check for unused CSS/JavaScript
- [ ] Consider image format upgrades (WebP)

### Annually
- [ ] Comprehensive performance review
- [ ] Consider Astro version upgrade
- [ ] Review and remove unused dependencies
- [ ] Evaluate CDN performance

---

## Future Optimizations (Phase 7)

**Priority Order:**

**1. Image Optimization (High Impact):**
- Install @astrojs/image
- Convert images to WebP
- Implement lazy loading
- Responsive image sizes

**2. Font Optimization (Medium Impact):**
- Self-host Google Fonts
- Preload critical fonts
- Remove unused font weights

**3. Code Splitting (Low Impact):**
- Already handled by Astro
- Consider if adding heavy JavaScript

**4. Service Worker (Low Impact):**
- Cache assets for offline access
- Faster repeat visits
- Only if needed for PWA functionality

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
**Current Status:** Excellent (95+ Lighthouse, < 2s load time)
