# X4O (Pty) Limited - Website Project

## Project Overview
Modern responsive website for X4O Consultants Pty Ltd, migrating from Wix to a self-hosted Astro static site on Netlify.

**Live URL:** https://x4o.co.za
**Staging URL:** (Netlify branch deploy from `staging` branch)
**Company:** X4O (Pty) Limited
**Location:** Durbanville, Cape Town, South Africa

## Tech Stack
| Layer | Technology | Version |
|-------|-----------|---------|
| Framework | Astro | 5.x |
| Styling | Tailwind CSS | 4.x |
| Language | TypeScript | Strict |
| Forms | Netlify Forms | Built-in |
| Hosting | Netlify | Free tier |
| Container | Docker | Node 22 Alpine |

## Theme Colors
- **Primary (#97c0e8):** Headings, CTA buttons, active states
- **Primary Dark (#174069):** Subheadings, links, copyright, footer
- **UI Style:** Glassmorphism with backdrop-blur effects

## Project Structure
```
x4o-website-dev/
├── public/
│   ├── images/          # Company assets (logo, favicon, banner)
│   ├── favicon.ico
│   └── favicon.svg
├── src/
│   ├── assets/          # Build-processed assets
│   ├── components/
│   │   ├── Header.astro # Navigation with mobile menu
│   │   └── Footer.astro # Site footer
│   ├── layouts/
│   │   └── Layout.astro # Base HTML layout
│   ├── pages/
│   │   ├── index.astro                          # Homepage
│   │   ├── consulting-and-advisory-services.astro # Consulting page
│   │   ├── coaching-services.astro              # Coaching page
│   │   ├── book-coaching-sessions.astro         # Booking page
│   │   ├── contact.astro                        # Contact + Netlify form
│   │   └── partners.astro                       # Partners page
│   └── styles/
│       └── global.css   # Tailwind + theme + glassmorphism utilities
├── astro.config.mjs
├── netlify.toml         # Netlify build + redirect config
├── Dockerfile           # Multi-stage: dev + production
├── docker-compose.yml   # Dev + preview services
├── tsconfig.json
└── package.json
```

## Git Branching Strategy
- **main:** Production branch, deploys to https://x4o.co.za
- **staging:** Development branch, deploys to Netlify branch preview
- All development happens on `staging`
- Submit PR from `staging` to `main` for supervisor review
- Never push directly to `main`

## Key Commands
```bash
# Development
npm run dev          # Start dev server at localhost:4321
npm run build        # Build for production
npm run preview      # Preview production build

# Docker
docker compose up dev       # Dev with hot reload
docker compose up preview   # Production preview at :8080

# Git workflow
git checkout staging        # Work on staging branch
git add . && git commit     # Commit changes
git push origin staging     # Push to staging
# Then create PR on GitHub: staging -> main
```

## Contact Form (Netlify Forms)
- Form name: "contact"
- Spam protection: Honeypot field (bot-field)
- Email notifications go to: admin@x4o.co.za
- Configure in Netlify Dashboard: Site Settings > Forms > Form notifications

## Netlify Setup Steps
1. Connect GitHub repo to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Enable branch deploys for `staging`
5. Set custom domain: x4o.co.za
6. Configure form email notifications to admin@x4o.co.za
7. Enable HTTPS (automatic with Netlify)

## Company Assets Needed
Place in `public/images/`:
- `logo.png` - Company logo
- `favicon.ico` - Browser favicon (replace default)
- `x4o_banner.jpg` - Hero banner image

## Pages & Navigation
| Page | Path | Description |
|------|------|-------------|
| Home | / | Welcome, services overview, CTA |
| Consulting | /consulting-and-advisory-services | Project management, advisory, renewable energy |
| Coaching | /coaching-services | 4 coaching types with details |
| Book Sessions | /book-coaching-sessions | Booking cards for 3 session types |
| Contact | /contact | Netlify Forms contact form |
| Partners | /partners | Partner logos and collaborations |

## Social Media Automation
- Platform: Facebook
- Frequency: Weekly posts
- Tool: Meta Business Suite Planner (free, built-in scheduling)
- Alternative: Buffer (free tier, 3 channels)
- See SOCIAL-MEDIA-GUIDE.md for setup details

## Important Notes
- Site output is `static` (no SSR) for best Netlify free tier performance
- Netlify adapter removed in favor of static output for forms compatibility
- All forms must have `data-netlify="true"` attribute
- Images should be optimized before adding to public/images/
- The old Wix site at x4o.co.za will need DNS updated to point to Netlify
