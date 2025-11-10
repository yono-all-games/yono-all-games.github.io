# App Referrals Site

A fast, mobile-optimized web app for app referrals built with AMP technology.

## Features

- 🚀 AMP-powered for instant loading
- 📱 Mobile-first UI design
- 🎮 Dynamic app listings
- 🔍 Search functionality
- 📊 Category filtering
- 🌐 SEO optimized
- 💫 Smooth animations

## Structure

```
├── index.html          # Main landing page
├── app.html           # App details template
├── assets/
│   └── icons/        # App icons
├── data/
│   └── apps.json     # App data
└── generate-icons.py  # Icon generation script
```

## Updating Content

1. To add/update apps:
   - Edit `data/apps.json`
   - Run `python3 generate-icons.py` to create new icons
   - Commit and push changes

2. To update design:
   - Modify CSS in `index.html` and `app.html`
   - Test with AMP validator
   - Commit and push changes

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yono-all-games/yono-all-games.github.io.git
   ```

2. Make changes and test locally using a web server:
   ```bash
   python -m http.server 8000
   ```

3. Visit http://localhost:8000 to preview

4. Validate AMP pages:
   - Use [AMP Validator](https://validator.ampproject.org/)
   - Or add '#development=1' to the URL

## Deployment

The site is automatically deployed through GitHub Pages:

1. Push to main branch:
   ```bash
   git add .
   git commit -m "Update message"
   git push origin main
   ```

2. Changes will be live at: https://yono-all-games.github.io/

## Maintaining

1. Regular tasks:
   - Update app links in apps.json
   - Generate new icons if needed
   - Test all referral links
   - Validate AMP compliance

2. Performance monitoring:
   - Check Google Search Console
   - Monitor loading speed
   - Test on various devices

## Tech Stack

- AMP HTML
- AMP Components
- JSON for data
- SVG for icons
- GitHub Pages for hosting