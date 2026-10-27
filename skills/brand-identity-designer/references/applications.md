# Applications and specs

Design the touchpoints that matter for this business on their real formats. Platform pixel specs change often: the values below were checked in October 2026 (mostly from third-party guides, O = official page). Re-check in the platform's own crop or upload tool before final export, and keep text and key marks inside the central 60% of any banner, because mobile crops are rarely published.

## Which applications are core
| Business | Digital | Print | Signage | Vehicles | Uniforms | Social | Packaging |
|---|---|---|---|---|---|---|---|
| Home and local services | Core | Core | Often | Core | Core | Core | Rare |
| Clinics and health | Core | Core | Core | Rare | Core | Often | Rare |
| Professional services | Core | Core | Often | Rare | Rare | Often | Rare |
| Restaurants and hospitality | Core | Core | Core | Rare | Core | Core | Core |
| Retail and DTC | Core | Often | Often | Rare | Often | Core | Core |
| SaaS and digital | Core | Rare | Rare | Rare | Rare | Core | Rare |
| Nonprofits | Core | Core | Often | Rare | Often | Core | Rare |
| Events and venues | Core | Core | Core | Rare | Often | Core | Often |
Get physical specs from vendors before final artwork: vehicle templates for the exact make and model from the wrap installer, embroidery limits from the embroiderer, sign dimensions and permit limits from the sign maker.

## Channel checklists
- **Digital:** favicon and app icons; header and footer lockups in light and dark; social share image; email signature (logo at 2x display size, plain-text fallback); presentation template (title, section, content, data, quote, closing); proposal, quote and invoice templates; video intro and outro, lower thirds, call background.
- **Print:** business cards; letterhead; estimate, invoice and receipt forms; brochure or service menu; door hangers, yard signs, leaflets; appointment cards; menus; stickers and labels.
- **Signage:** fascia (check night legibility when lit), window vinyl with hours, wayfinding, A-frame, jobsite sign, pull-up banner. Letter height about 25 mm per 3 m of viewing distance (6 m: 50 mm, 15 m: 125 mm, 30 m: 250 mm); 3 to 6 words for moving traffic; sturdy medium-bold sans; check a full-size section from the real distance. US ADA rules apply to permanent room and wayfinding signs in public facilities.
- **Vehicles:** on the installer's template; phone and web legible from a following car on the rear doors; no type across door handles, panel gaps, fuel caps or vents; regulator-required licence numbers where the trade needs them.
- **Uniforms:** an embroidery version of the logo; hi-vis safety standards override brand colours; separate drawings for embroidery, screen print and heat transfer when one file cannot serve all.
- **Social:** one avatar (symbol or stacked mark on a solid ground, checked in a circle) for every platform and the Google Business Profile; covers per platform; post templates (announcement, review, before/after, offer, hiring, tip); story templates and highlight covers.
- **Packaging:** regulatory panels first, then brand the remaining space; labels, shipping boxes, inserts, bags, cups, tags.

## Print basics
CMYK only through the printer's profile; images 300 ppi at final size (large format 100 to 150); logos and text vector; bleed 3 mm (US 0.125 in); safe margin 3 to 5 mm on small items, 10 mm+ on posters; small text in 100% black only; hairlines at least 0.25 pt; press-ready PDF/X-1a or X-4 with fonts embedded or outlined. HTML and screen exports are RGB: treat them as layouts and proofs.
Sizes: business card US 3.5 × 2 in (88.9 × 50.8 mm), EU/UK 85 × 55 mm (91 × 61 with bleed); A4 210 × 297; A5 148 × 210; DL 99 × 210; US Letter 8.5 × 11 in; posters A3 to A1; roll-up banner about 850 × 2000 mm (keep the bottom 100 to 150 mm empty); yard sign 18 × 24 in. Card name 9 to 11 pt, details 7 to 8 pt (never under 6 pt).

## Web and app icons
- Favicon set: `favicon.ico` 32 (with 16 inside; give the link `sizes="32x32"` so browsers prefer the SVG), `icon.svg` (may carry a dark-scheme rule), `apple-touch-icon.png` 180 on a solid background (mark about 140 px), 192 and 512, a maskable 512 with the mark inside the central 80% circle, and a web manifest. Use the small-size drawing, not the master shrunk. (O)
- Social share image 1200 × 630 (minimum 600 × 315). (O)
- Apple app icon 1024 × 1024, square without baked corners, layered for Liquid Glass (background and foreground layers; default, dark, clear and tinted appearances), no baked highlights or shadows, no text unless essential. Android adaptive icon 108 × 108 dp layers with the inner 66 dp never clipped, plus a monochrome layer for themed icons; Play listing 512 × 512 PNG. Test at 29 pt (iOS Settings) and 48 dp on a busy wallpaper. Store specs change yearly: re-check.
- Email signature logo displayed 100 to 200 px wide, exported at 2x, under 50 KB, with a dark-mode-safe variant; avoid SVG (Outlook).

## Social sizes (re-check before export)
| Platform | Asset | Size |
|---|---|---|
| LinkedIn | personal banner | 1584 × 396; the photo covers the lower left; mobile crops the sides |
| LinkedIn | profile photo, company logo | 400 × 400 (covers older 300 × 300) |
| LinkedIn | company cover | sources conflict: 1128 × 191 (older) and 1512 × 256 (newer); design for the newer, export both, keep text central |
| LinkedIn | posts | 1200 × 627, 1080 × 1080, 1080 × 1350 (best feed presence); document carousels 1080 × 1350 or 1080 × 1080 per page, all pages the same size (O: max 100 MB, 300 pages) |
| Instagram | feed | 1080 × 1350 default (4:5), 1080 × 1440 (3:4), 1080 × 1080; the profile grid shows 3:4, so keep titles inside the central 1080 × 1440 |
| Instagram | stories, reels | 1080 × 1920; keep text out of the top ~14% and bottom ~35% and the right action column |
| Facebook | page cover | 851 × 315 (desktop shows ~820 × 312, mobile ~640 × 360: keep the central 640 px) |
| YouTube (O) | banner | 2560 × 1440 (min 2048 × 1152), safe area 1546 × 423 centred; profile 800 × 800; thumbnail 1280 × 720 |
| X (O) | profile, header | 400 × 400; 1500 × 500 (photo overlaps lower left) |
| TikTok | video | 1080 × 1920; keep the right 120 to 150 px and the bottom caption area clear |
| Google Business Profile (O) | photos, logo | 720 × 720 recommended (min 250 × 250); cover 1024 × 576 without text |
Avatars: 800 × 800 or larger, solid background (transparency renders inconsistently), padded for circular crops.

## Social design rules
A 1080-wide graphic shows at roughly 360 to 430 CSS px on a phone: text at least 40 px on the canvas (headlines 72 to 120), headline 8 words or fewer, one message per graphic, margins 64 to 80 px, the logo small and in the same corner every time (not on every carousel page). Carousels: page 1 hooks in 6 to 8 words, one idea per page, a constant grid and page counter, the call to action last. Scrim of 60% or more behind text on photos. Test a 9 to 12 post grid at phone width (family test). Several accounts under one brand share constants and get one distinct accent or device each. Avoid puzzle grids that break when one post is deleted.
