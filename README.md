# X4O (Pty) Limited - Official Website

Modern, responsive website for X4O Consultants built with Astro and Tailwind CSS.

**Live Site:** [x4o.co.za](https://x4o.co.za)
**Staging:** Netlify branch deploy from `staging` branch

---

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

Development server runs at `http://localhost:4321`

---

## 📁 Project Structure

```
x4o-website-dev/
├── public/              # Static assets (images, favicon)
├── src/
│   ├── components/      # Reusable components (Header, Footer)
│   ├── layouts/         # Page layouts
│   ├── pages/           # Website pages (Astro routes)
│   └── styles/          # Global CSS and Tailwind config
├── netlify.toml         # Netlify deployment config
└── package.json
```

---

## 🌐 Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Landing page with services overview |
| Consulting | `/consulting-and-advisory-services` | Consulting services details |
| Coaching | `/coaching-services` | Coaching offerings |
| Book Session | `/book-coaching-sessions` | Coaching booking options |
| Contact | `/contact` | Contact form (Netlify Forms) |
| Partners | `/partners` | Partner logos and info |

---

## 🎨 Tech Stack

- **Framework:** Astro 5.x (Static Site Generation)
- **Styling:** Tailwind CSS 4.x
- **Language:** TypeScript (Strict mode)
- **Forms:** Netlify Forms (contact submissions)
- **Hosting:** Netlify
- **Container:** Docker (Node 22 Alpine)

---

## 🔄 Git Workflow

**Branches:**
- `main` - Production (deploys to x4o.co.za)
- `staging` - Development (deploys to Netlify preview)

**Development Process:**
1. Work on `staging` branch
2. Test changes on staging deployment
3. Create Pull Request: `staging` → `main`
4. Get supervisor approval
5. Merge to `main` for production deployment

**Never push directly to `main`**

---

## 📧 Contact Form

- **Form Handler:** Netlify Forms
- **Form Name:** `contact`
- **Spam Protection:** Honeypot field
- **Notifications:** Configured in Netlify dashboard
- **Email:** admin@x4o.co.za

**Setup:** Configure form notifications in Netlify dashboard under Site Settings → Forms

---

## 🛠️ Maintenance Mode

Enable/disable maintenance mode using `netlify.toml`:

```toml
# Enable maintenance mode (uncomment)
[[redirects]]
  from = "/*"
  to = "/maintenance.html"
  status = 200
  force = true
```

See `MAINTENANCE.md` for detailed instructions.

---

## 🐳 Docker Commands

```bash
# Development with hot reload
docker compose up dev

# Production preview
docker compose up preview
```

---

## 📖 Documentation

- `CLAUDE.md` - Project overview and guidelines
- `MAINTENANCE.md` - Maintenance mode instructions
- `BACKUP.md` - Backup and recovery procedures
- `SOCIAL-MEDIA-GUIDE.md` - Social media automation setup

---

## 🎨 Brand Colors

- **Primary:** `#97c0e8` (Light Blue) - Headings, CTAs, buttons
- **Primary Dark:** `#174069` (Dark Blue) - Subheadings, links, footer
- **UI Style:** Glassmorphism with backdrop-blur effects

---

## 📱 Features

✅ Fully responsive design
✅ Glassmorphism UI effects
✅ Contact form with spam protection
✅ Partner logos showcase
✅ Maintenance mode support
✅ SEO optimized (meta tags, Open Graph)
✅ Fast static site generation

---

## 🔧 Common Commands

```bash
# Install dependencies
npm install

# Development
npm run dev              # Start dev server

# Production
npm run build            # Build for production
npm run preview          # Preview production build

# Docker
docker compose up dev    # Dev with hot reload
docker compose up preview # Preview at :8080

# Git
git checkout staging     # Switch to staging
git push origin staging  # Push to staging
```

---

## 📝 Support

For questions or issues, contact the development team or refer to the documentation files.

---

**Built with ❤️ by the X4O Development Team**
