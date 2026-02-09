# Maintenance Mode Guide

This guide explains how to enable and disable maintenance mode for the X4O website on the production (main) branch.

## What is Maintenance Mode?

When enabled, all visitors to x4o.co.za will see a maintenance page instead of the regular website. This is useful during:
- Domain migrations
- Major updates
- System upgrades
- Database maintenance

## Files

- **Maintenance Page**: `public/maintenance.html`
- **Normal Site**: All other pages in `src/pages/`

## How to Enable Maintenance Mode

### Method 1: Using Netlify Redirects (Recommended)

1. **Update `netlify.toml`** - Add this redirect AT THE TOP of the `[[redirects]]` section:

```toml
# MAINTENANCE MODE - Uncomment to enable
[[redirects]]
  from = "/*"
  to = "/maintenance.html"
  status = 200
  force = true
```

2. **Commit and push to main branch**:
```bash
git checkout main
git add netlify.toml
git commit -m "Enable maintenance mode"
git push origin main
```

3. **Wait for deployment** - Netlify will redeploy (1-2 minutes)

4. **Verify** - Visit https://x4o.co.za to confirm maintenance page is showing

### Method 2: Using Netlify Dashboard (No code changes)

1. Go to Netlify dashboard: https://app.netlify.com
2. Select your X4O site
3. Go to **Site settings > Build & deploy > Post processing > Snippet injection**
4. Add a snippet that redirects to `/maintenance.html`

OR

1. Go to **Redirects and rewrites**
2. Add a new redirect:
   - From: `/*`
   - To: `/maintenance.html`
   - Status: 200
   - Force: Yes

## How to Disable Maintenance Mode

### If you used Method 1 (netlify.toml):

1. **Edit `netlify.toml`** - Comment out or remove the maintenance redirect:

```toml
# MAINTENANCE MODE - Uncomment to enable
# [[redirects]]
#   from = "/*"
#   to = "/maintenance.html"
#   status = 200
#   force = true
```

2. **Commit and push**:
```bash
git add netlify.toml
git commit -m "Disable maintenance mode"
git push origin main
```

3. **Wait for deployment** - Site will be back online in 1-2 minutes

### If you used Method 2 (Netlify Dashboard):

1. Go to Netlify dashboard
2. Remove the redirect/snippet you added
3. Site will be back online immediately

## Important Notes

- **Staging branch is NOT affected** - Maintenance mode only affects the main/production branch
- **Email still works** - Google Workspace email continues to function normally
- **Contact form is disabled** - Users can't submit forms during maintenance (they should email instead)
- **Test first on staging** - Always test changes on staging before applying to main

## Customizing the Maintenance Page

Edit `public/maintenance.html` to change:
- Message text
- Contact information
- Styling/colors
- Estimated downtime

## Emergency Rollback

If something goes wrong:

```bash
git revert HEAD
git push origin main
```

This will immediately undo the last commit and restore the site.

## Pre-Deployment Checklist

Before enabling maintenance mode:

- [ ] Notify users via email/social media if possible
- [ ] Test maintenance page on staging first
- [ ] Confirm all team members are aware
- [ ] Set a target time to disable maintenance mode
- [ ] Have rollback plan ready

## Example: Domain Migration Workflow

1. **Enable maintenance mode on main branch**
2. **Update DNS records with hosting company**
3. **Wait for DNS propagation** (1-24 hours)
4. **Verify new domain works**
5. **Disable maintenance mode on main branch**
6. **Site is live on new domain**
