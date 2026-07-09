# Media Sourcing Guide

## Current Status

All visual media in the student-facing site currently uses:
- **Original CSS/SVG animations** (preferred) — see `public/media/animations/`
- **Gradient-based card visuals** — no external dependencies
- **Text-only info cards** — no images required

## Adding Study Culture Media

If you want to add study meme images/GIFs to enhance the Pinterest aesthetic:

### Approved Sources (in priority order)

1. **Pixabay** — https://pixabay.com/
   - Use GIFs/images under Pixabay Content License
   - Commercial use allowed
   - No attribution required
   - Avoid content with visible brands/logos

2. **Wikimedia Commons** — https://commons.wikimedia.org/
   - Check INDIVIDUAL file license page
   - Prefer Public Domain / CC0
   - CC BY / CC BY-SA acceptable if attribution is added

3. **Your own original content**
   - Photos of your study materials
   - Original illustrations
   - Custom animations

### Process

1. Find suitable media from approved sources
2. Verify commercial-use permission on the original page
3. Download and save to `public/media/study-culture/` with descriptive filename
4. Add entry to `content/media-licenses.json`:
   ```json
   {
     "localPath": "/media/study-culture/your-file.webp",
     "title": "Original title from source",
     "creator": "Creator name",
     "source": "https://source-page-url",
     "provider": "Pixabay",
     "license": "Pixabay Content License",
     "licenseUrl": "https://pixabay.com/service/license-summary/",
     "attributionRequired": false,
     "commercialUseChecked": true,
     "checkedAt": "2026-07-10"
   }
   ```
5. Reference in `lib/library-memes.ts`
6. If attribution required, add to `/credits` page

### What NOT to Use

- Content from Pinterest, GIPHY, Tenor, Reddit, Instagram
- Movie/TV clips, anime scenes, celebrity reactions
- Recognizable copyrighted characters (Minions, SpongeBob, etc.)
- Random Google Images search results
- Content with unclear copyright status

### Current Original Animations

Located in `public/media/animations/`:
- `floating-books.svg` — Animated study books
- `coffee-steam.svg` — Coffee cup with steam animation
- `exam-paper-shuffle.svg` — Shuffling exam papers

These are original works and can be used freely throughout the site.

## Performance

- Optimize large GIFs before adding
- Consider WebP format for images
- Use `loading="lazy"` for below-fold images
- Provide width/height to prevent layout shift
- Respect `prefers-reduced-motion`

## Audit

Before deploying, search codebase for:
- `unsplash.com` — remove all instances
- `giphy.com`, `tenor.com` — not allowed
- `pinimg.com`, `reddit.com` — not allowed
- Any external image hotlinks

All student-facing media must be self-hosted and legally cleared.
