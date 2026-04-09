# Analytics Implementation Guide

**Last Updated:** February 13, 2026
**For:** X4O Website Administrators

---

## Current Status

**Analytics:** Not yet implemented
**Recommendation:** Choose between Google Analytics 4 or Netlify Analytics
**Timeline:** Phase 7 enhancement

---

## Option 1: Google Analytics 4 (GA4) - Recommended

### Why GA4?

**Pros:**
- ✅ Free forever
- ✅ Comprehensive data (user behavior, traffic sources, conversions)
- ✅ Event tracking
- ✅ Real-time reporting
- ✅ Integration with Google Search Console
- ✅ Industry standard

**Cons:**
- ❌ Requires cookie consent (GDPR/POPIA compliance)
- ❌ External JavaScript (small performance impact)
- ❌ Privacy concerns (data stored on Google servers)

### Setup Google Analytics 4

**Step 1: Create GA4 Property**

1. Go to https://analytics.google.com/
2. Click "Start measuring"
3. Create Account:
   - Account name: "X4O Consultants"
   - Data sharing settings: Choose preferences
4. Create Property:
   - Property name: "X4O Website"
   - Time zone: (GMT+02:00) South Africa
   - Currency: South African Rand (ZAR)
5. Fill out business information
6. Choose "Web" platform
7. Enter website URL: https://x4o.co.za
8. Create stream

**Step 2: Get Measurement ID**

Copy your Measurement ID (format: `G-XXXXXXXXXX`)

**Step 3: Add to Website**

Edit `src/layouts/Layout.astro` and add before `</head>`:

```astro
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script is:inline>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

**Step 4: Deploy**

```bash
git add src/layouts/Layout.astro
git commit -m "feat: add Google Analytics 4"
git push origin staging

# Test on staging first, then merge to main
```

**Step 5: Verify**

1. Go to GA4 → Reports → Realtime
2. Visit your website
3. You should see your visit in real-time

### Important Events to Track

**Auto-Tracked (No Code Needed):**
- Page views
- User engagement
- First visit
- Scroll depth
- Outbound link clicks

**Custom Events (Optional Future Addition):**
- Form submissions
- Button clicks
- Email link clicks
- Phone number clicks

**Example Custom Event:**
```astro
<button onclick="gtag('event', 'book_session_click', {
  'event_category': 'engagement',
  'event_label': 'Executive Coaching'
});">
  Book Session
</button>
```

---

## Option 2: Netlify Analytics - Privacy-Focused

### Why Netlify Analytics?

**Pros:**
- ✅ Privacy-friendly (no cookies, no consent needed)
- ✅ No JavaScript required (server-side tracking)
- ✅ No performance impact
- ✅ Ad-blocker resistant
- ✅ GDPR/POPIA compliant by default

**Cons:**
- ❌ Costs $9/month
- ❌ Less detailed data than GA4
- ❌ No user behavior flow
- ❌ Basic reporting only

### Setup Netlify Analytics

**Step 1: Enable in Netlify Dashboard**

1. Go to https://app.netlify.com/
2. Select your site (x4oconsultants)
3. Go to "Analytics" tab
4. Click "Enable Analytics"
5. Confirm $9/month charge

**Step 2: Wait for Data**

- No code changes needed
- Data starts collecting immediately
- Historical data not available (starts from enable date)

**Step 3: View Reports**

Available data:
- Page views
- Unique visitors
- Top pages
- Traffic sources
- Bandwidth usage

---

## Option 3: Plausible Analytics - Lightweight Alternative

### Why Plausible?

**Pros:**
- ✅ Privacy-friendly (GDPR compliant)
- ✅ No cookie consent needed
- ✅ Lightweight (< 1KB script)
- ✅ Simple, clean dashboard
- ✅ Open source

**Cons:**
- ❌ Costs €9/month (~R190/month)
- ❌ Less detailed than GA4
- ❌ Requires manual setup

### Setup Plausible

**Step 1: Create Account**

1. Go to https://plausible.io/
2. Sign up for account
3. Add site: x4o.co.za

**Step 2: Add Script**

Add to `src/layouts/Layout.astro` before `</head>`:

```astro
<script defer data-domain="x4o.co.za" src="https://plausible.io/js/script.js"></script>
```

**Step 3: Deploy and Verify**

Same process as GA4.

---

## Recommended Choice

**For X4O Website: Google Analytics 4**

**Reasons:**
1. Free (important for small business)
2. Most comprehensive data
3. Integration with Google Ads (if used in future)
4. Standard in industry
5. You already have Google Workspace account

**Privacy Compliance:**
- Add cookie consent banner (required for GDPR/POPIA)
- Add privacy policy page explaining data collection
- Allow users to opt-out

---

## Key Metrics to Monitor

### Traffic Metrics

**Page Views**
- How many pages visited
- Which pages are most popular

**Users**
- Unique visitors to your site
- New vs. returning visitors

**Sessions**
- Number of visits to your site
- Average session duration

**Bounce Rate**
- Percentage of single-page visits
- Target: < 60%

### Acquisition (Where Traffic Comes From)

**Direct**
- Typed URL directly or bookmarked
- Email links

**Organic Search**
- Google, Bing searches
- Most important for SEO

**Referral**
- Links from other websites
- Partner sites, directories

**Social**
- Facebook, LinkedIn, Instagram
- Track social media effectiveness

### Behavior Metrics

**Top Pages**
- Most visited pages
- Optimize these first

**Average Time on Page**
- How long users read content
- Longer = more engagement

**Exit Pages**
- Where users leave site
- May indicate problems or completion

---

## Setting Up Goals/Conversions

### Important Conversions to Track

**1. Contact Form Submission**

In GA4, create conversion event:
- Event name: `form_submit`
- Mark as conversion in GA4 admin

**2. Email Link Clicks**

Track when users click email links:
- Event name: `email_click`

**3. Phone Number Clicks**

Track when users click phone number:
- Event name: `phone_click`

**4. Book Session Button Clicks**

Track coaching session bookings:
- Event name: `book_session_click`

---

## Privacy & Compliance

### GDPR/POPIA Requirements

If using GA4, you must:

**1. Add Cookie Consent Banner**

**Option A: Manual Implementation**
```astro
<!-- Simple cookie banner -->
<div id="cookie-banner" style="position: fixed; bottom: 0; width: 100%; background: #333; color: white; padding: 1rem; display: none;">
  <p>We use cookies to analyze our traffic. <a href="/privacy-policy">Privacy Policy</a></p>
  <button onclick="acceptCookies()">Accept</button>
</div>

<script>
  if (!localStorage.getItem('cookiesAccepted')) {
    document.getElementById('cookie-banner').style.display = 'block';
  }

  function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-banner').style.display = 'none';
    // Load GA4 here
  }
</script>
```

**Option B: Use Service**
- CookieYes (https://www.cookieyes.com/) - Free tier available
- Cookiebot (https://www.cookiebot.com/) - Paid

**2. Create Privacy Policy Page**

Create `src/pages/privacy-policy.astro`:

**Must Include:**
- What data is collected (page views, device info, location)
- Why it's collected (improve website, understand users)
- How it's used (analytics, reports)
- How long it's stored (GA4: up to 14 months default)
- User rights (access, deletion, opt-out)
- Contact info for data requests

**Template:**
See `docs/templates/privacy-policy-template.md` (to be created)

**3. Add Opt-Out Mechanism**

Allow users to disable GA4:
```astro
<a href="#" onclick="gaOptout(); return false;">Opt-out of Google Analytics</a>

<script>
  function gaOptout() {
    document.cookie = 'ga-disable-G-XXXXXXXXXX=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
    window['ga-disable-G-XXXXXXXXXX'] = true;
    alert('Google Analytics has been disabled.');
  }
</script>
```

---

## Analytics Dashboard Setup

### GA4 Custom Reports

**Create Reports For:**

**1. Traffic Overview**
- Page views by date
- Users by traffic source
- Top landing pages

**2. SEO Performance**
- Organic search traffic
- Top search queries (from Search Console integration)
- SEO conversion rate

**3. Page Performance**
- Page views by page
- Average time on page
- Bounce rate by page

**4. Conversion Tracking**
- Form submissions
- Email clicks
- Phone clicks
- Session bookings

---

## Integration with Google Search Console

**Why Integrate:**
- See which search queries bring traffic
- Understand keyword performance
- Track Google ranking improvements

**How to Integrate:**

1. Go to GA4 Admin → Product Links
2. Click "Search Console Links"
3. Click "Link"
4. Select Search Console property (if set up)
5. Confirm linking

**Benefits:**
- Search performance data in GA4
- Combined SEO and behavior analytics

---

## Troubleshooting

### Analytics Not Tracking

**Check:**
1. Measurement ID is correct (G-XXXXXXXXXX)
2. Script is in `<head>` section of Layout.astro
3. Site was deployed after adding script
4. Ad blocker is disabled (for testing)
5. Real-time report in GA4 shows activity

### Data Looks Wrong

**Common Issues:**
- Bot traffic (GA4 auto-filters most)
- Your own visits (exclude your IP in GA4 settings)
- Duplicate tracking code (check only one script)

### Privacy Concerns

**Solutions:**
- Use Netlify Analytics instead (no cookies)
- Or use Plausible or Fathom
- Add clear privacy policy
- Provide opt-out mechanism

---

## Analytics Best Practices

### Do:
- ✅ Check analytics weekly
- ✅ Set up custom reports for important metrics
- ✅ Track conversions (form submissions)
- ✅ Respect user privacy
- ✅ Comply with GDPR/POPIA

### Don't:
- ❌ Track personally identifiable information (PII)
- ❌ Obsess over daily fluctuations
- ❌ Ignore privacy regulations
- ❌ Use analytics without consent banner (if using GA4)

---

## Monthly Analytics Checklist

**Review These Metrics:**
- [ ] Total users vs. last month
- [ ] Most popular pages
- [ ] Traffic sources (organic vs. direct vs. referral)
- [ ] Bounce rate by page
- [ ] Average session duration
- [ ] Conversion rate (form submissions)
- [ ] Top search queries (if Search Console integrated)

**Actions Based on Data:**
- High bounce rate page? → Improve content or loading speed
- Low conversion rate? → Improve calls-to-action
- Traffic dropped? → Check SEO or recent changes
- New traffic source? → Investigate and optimize

---

## Cost Comparison

| Service | Cost | Features | Privacy | Best For |
|---------|------|----------|---------|----------|
| **Google Analytics 4** | Free | Comprehensive | Requires consent | Most businesses |
| **Netlify Analytics** | $9/month | Basic | Very private | Privacy-focused |
| **Plausible** | €9/month | Basic | Very private | EU/privacy-focused |
| **Fathom** | $14/month | Basic | Very private | Privacy-focused |

**Recommendation for X4O:** Start with GA4 (free), add privacy policy and cookie banner.

---

**Guide Version:** 1.0
**Last Updated:** February 13, 2026
**Status:** Analytics not yet implemented (Phase 7 task)
