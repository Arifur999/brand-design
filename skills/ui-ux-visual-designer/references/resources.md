# Resources: inspiration, type, icons, colour, standards

Evaluated 2026-10-27 (live fetch unless marked). Galleries show other people's copyrighted work: study the principle, never copy a layout, copy or asset. Licence terms change; re-read the licence page before shipping a paid or unusual resource in client work.

Verdicts: **Core** use by default · **Situational** when the task needs it · **Study** look and learn, never ship assets · **Avoid** for default use.

## Find patterns (by job)

| Need | Go to | Agent access | Verdict |
|---|---|---|---|
| Real app screens and flows (onboarding, paywalls, settings) | Mobbin (mobbin.com) | Only through its MCP on a paid Pro plan; terms forbid scraping and AI derivative use. Without MCP, ask the person for screenshots | Core if they have MCP, else ask |
| Searchable web and iOS screens | Refero (refero.design) | MCP and an official agent skill on paid plans; homepage is JS-only | Core if paid, else Situational |
| Navigation bars by type | Navbar Gallery (navbar.gallery) | Text fetch works: `/type/{mega-menu, dropdown, side-bar, search, announcement, full-screen, breadcrumbs}` | Study |
| Footers by style | footer.design | Text fetch: `/styles/{style}`, `/browse` | Study |
| CTA patterns | CTA Gallery (cta.gallery) | Text fetch: `/categories/{button, form, newsletter, pricing-subscription, modal-pop-up, call-to-buy, download}` | Study |
| Whole sections (hero, pricing, testimonials, footer) by industry | Unsection (unsection.com) | Category pages fetch: `/category/{type}-section-design`, `/industries`; deeper use needs login | Study |
| High-craft sites, motion, app icons | Recent (recent.design; godly.website redirects here; use no `www`) | Text fetch: `/websites`, `/app-icons` | Study |
| Bento layouts | Bento Grids (bentogrids.com) | JS-only, title only | Study, low priority |
| 404 pages | 404s.design | Text fetch | Study, low value |
| Mood boards across brand, graphic and UI | Savee (savee.com) | Login; MCP on paid plans | Study |
| Landing pages by industry | Land-book, Lapa Ninja, SaaS Landing Page, One Page Love, Siteinspire, Minimal Gallery | Land-book blocked agents (403) in the check; others fetched in Oct 2026 | Study |
| Dashboards that actually ship | Tremor blocks (tremor.so), Vercel Geist, GitHub Primer, IBM Carbon | Docs fetch | Situational |
| Dribbble and Behance | | | Mood only: many dashboard shots are unbuildable, fake data, poor contrast. Never a pattern source |

When a gallery cannot be fetched, do not guess what is on it. Ask the person for screenshots or URLs of examples they like; their taste anchors are worth more than a gallery sweep.

## Design systems to learn from

Vercel Geist and Web Interface Guidelines (vercel.com/design/guidelines, a strong interaction and QA checklist; docs pages work with `.md` appended) · shadcn/ui (base layer for React work) · Radix Colors (12-step role scales) · GitHub Primer (dense product UI, content guidelines) · IBM Carbon (enterprise data, tables, data viz) · Atlassian (tokens naming, voice) · Shopify Polaris (admin patterns; React version deprecated, read the guidance only) · Material 3 and Apple HIG (platform rules, see Standards).

## Typography

| Resource | Use for | Licence and access | Verdict |
|---|---|---|---|
| Google Fonts (fonts.google.com; files and per-family licence in `github.com/google/fonts` `METADATA.pb`) | Default free source | Mostly SIL OFL 1.1: commercial, web, apps, logos, self-hosting, redistribution with the notice. Some Apache 2.0 or UFL | Core |
| Fontshare (fontshare.com; catalogue as JSON at `api.fontshare.com/v2/fonts`, field `license_type`) | Distinctive free sans and display faces (Satoshi, General Sans, Cabinet Grotesk, Clash Display, Zodiak) | 64 families ITF Free Font License: commercial use and logos allowed, no attribution; **no modifying or subsetting, no giving files to clients, contractors or printers** (they download from Fontshare themselves). 36 families are SIL OFL | Core, check per family |
| Typewolf (typewolf.com) | Real-world pairings, Site of the Day with fonts named, free-font guides | Text fetch: `/site-of-the-day/{site}`, `/{font-name}`, `/google-fonts` | Core for discovery |
| Fonts In Use (fontsinuse.com) | Fonts in real work by industry and format | Text fetch: `/typefaces/...`, `/search/advanced`; images belong to contributors | Core for evidence, Study for images |
| WhatTheFont (myfonts.com) | Identify a font in a client's screenshot | Needs an image upload by a person; no agent API | Situational: ask the person to run it, or identify by eye and say it is a guess |
| Fontsource (fontsource.org) | npm self-hosting of open-source fonts | Not live-checked | Situational |
| Commercial foundries | When budget allows a face no competitor uses | Licence per weight and per use (desktop, web, app); the client buys it | Name it, give the licence note, provide a free fallback |

Type defaults that read as AI-made when chosen without a reason: Inter, Roboto, system UI everywhere; and the "trendy defaults" Space Grotesk, Geist, Instrument Serif, Plus Jakarta Sans, Outfit, Fraunces. They are fine when the brief justifies them.

## Icons

| Set | Licence | Notes | Verdict |
|---|---|---|---|
| Lucide (lucide.dev) | ISC (Feather parts MIT); no on-screen credit, keep the notice in source | Default for shadcn; 2 px round strokes, so it is also the most recognisable "default" look | Core |
| Phosphor (phosphoricons.com) | MIT | Six weights including duotone and fill: easy to give a product its own icon voice | Core |
| Tabler Icons (tabler.io/icons) | MIT | 6,000+ consistent 24 px / 2 px stroke icons | Core |
| Hugeicons, Remix Icon, Heroicons | Free tiers MIT; Remix Icon reportedly moved to its own licence in 2026 (verify); Heroicons small and slow-moving | Read the licence before use | Situational |
| Flaticon | Free icons require visible attribution, **may not be used in logos or trademarks**, licence per icon; mixed authors | Blocks agents; inconsistent styles across authors | Avoid by default |
| Icons8 | Free use requires a link back; paid removes it; sells AI-generated imagery alongside | Blocks agents; mixed provenance | Avoid by default |
| SF Symbols / Material Symbols | SF Symbols only inside apps on Apple platforms, never on websites or in logos | Use in native apps only | Situational |

Rules: one icon set per product, one stroke width, fixed sizes per context (16 inline, 20 in buttons and nav, 24 standalone). Icon-only buttons need an accessible name and a tooltip.

## Colour tools

oklch.com (picker and gamut, open source) · Radix Colors (accessible step scales) · Realtime Colors (preview a palette and type on a layout, exports CSS and Tailwind) · WebAIM contrast checker · APCA (apcacontrast.com) as a second opinion, never instead of WCAG 2 · Huemint is ML-generated: inspiration only, never an authority. For measurement use `scripts/color_tools.py` (contrast, ramps, colour-blind checks).

## Photos and illustration

Client's own photography first: real team, real jobs, real product. Unsplash and Pexels licences allow commercial use without credit but not selling unaltered copies; identifiable people must not be shown in a bad light; stock people lower trust for local businesses. Illustration: unDraw (free, recolourable) is fine for empty states but is everywhere, so never a signature; Open Peeps and Humaaans look dated (frozen around 2020); Storyset's free tier requires a credit. A signature illustration style means commissioning one illustrator. Never present AI-generated images as photographs of a real business, its people or its work. Full rules: `imagery.md`.

## Standards (primary sources)

| Source | Use |
|---|---|
| WCAG 2.2 Quick Reference (w3.org/WAI/WCAG22/quickref/) | Success criteria with filters; loads as text (large, read in parts) |
| Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) | iOS, iPadOS, macOS, visionOS rules; JS-rendered, read in a browser |
| Material Design 3 (m3.material.io) | Android and web; M3 Expressive is the current evolution (not "Material 4"); JS-rendered |
| Nielsen Norman Group (nngroup.com/articles), Laws of UX (lawsofux.com) | Evidence-based usability guidance |
| web.dev | Core Web Vitals and performance |
