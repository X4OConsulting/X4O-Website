# X4O Website Backup & Recovery Guide

## Quick Recovery Steps

If something goes wrong, follow these steps:

### 1. Restore from Git
```bash
# Reset to last known good commit
git log --oneline -10        # Find the good commit
git checkout <commit-hash>   # Restore to that state

# Or reset staging branch
git checkout staging
git reset --hard origin/staging
```

### 2. Rebuild from Scratch
```bash
npm install
npm run build
```

### 3. Restore Assets
Company assets should be kept in `public/images/`:
- `logo.png` - Company logo
- `x4o_banner.jpg` - Hero banner image
- `favicon1.jpg` - Favicon source

Original assets are also stored in `src/assets/` as backup copies.

## Project Backup Checklist

### Critical Files (Must back up)
- [ ] `src/` directory (all pages, components, layouts, styles)
- [ ] `public/images/` (company assets)
- [ ] `astro.config.mjs`
- [ ] `netlify.toml`
- [ ] `package.json`
- [ ] `CLAUDE.md`

### Configuration Files
- [ ] `Dockerfile`
- [ ] `docker-compose.yml`
- [ ] `.gitignore`
- [ ] `tsconfig.json`

## Content Backup (Scraped from Original Wix Site)

### Homepage
- **Title:** Enterprise Systems Delivery Advisory | X4O (Pty) Limited | Cape Town
- **Description:** At X4O, we believe that technology should support and enhance your organization's success, not constrain it.
- **Tagline:** Supporting You As You Grow

### Services
1. Project & Programme Management
2. Advisory (13 areas of expertise)
3. Renewable Energy Advisory (11 service areas)
4. Coaching (Personal Transformation, Corporate Governance, Leadership, Finance)

### Coaching Sessions
- Personal Transformation Coaching - 1 hr 30 min - Via Quote
- Leadership Coaching - 1 hr 30 min - Via Quote
- Corporate Governance Coaching - 1 hr 30 min - Via Quote

### Contact Information
- Email: info@x4o.co.za / admin@x4o.co.za
- Location: Durbanville, Cape Town, South Africa
- Company: X4O (Pty) Limited

## DNS Migration Notes (Wix to Netlify)

When ready to switch from Wix to Netlify:

1. **In Netlify Dashboard:**
   - Go to Site Settings > Domain Management
   - Add custom domain: x4o.co.za
   - Note the Netlify DNS nameservers provided

2. **At your domain registrar:**
   - Update nameservers to Netlify's nameservers, OR
   - Update A record to point to Netlify's load balancer IP
   - Update CNAME for www to redirect to x4o.co.za

3. **DNS propagation takes 24-48 hours**
   - Keep Wix active until DNS fully propagates
   - Test with: `dig x4o.co.za` or `nslookup x4o.co.za`

4. **After DNS propagates:**
   - Verify site loads correctly
   - Test contact form submissions
   - Cancel Wix subscription

## Emergency Contacts
- Netlify Support: https://www.netlify.com/support/
- Domain Registrar: (update with your registrar info)
