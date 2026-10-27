# Brand resources

Evaluated 2026-10-27 (live fetch unless noted). Reference sites show other people's protected work: study principles, never copy marks, layouts or assets. Re-read a licence before shipping anything unusual in client work.

## Studying identity work
| Source | Use for | Agent access | Verdict |
|---|---|---|---|
| Brand New (underconsideration.com/brandnew) | Critical reviews of real identity launches and refreshes; see what a sector already looks like and what critics call out | Text fetch: `/brandnew/archives/{slug}.php`, `/category/industry/{x}`, `/tag/{x}` | Core |
| BP&O (bpando.org) | Identity and packaging reviews with design-side commentary | Text fetch: `/search/`, `/logos/{slug}/` | Core |
| Fonts In Use (fontsinuse.com) | Typefaces in real brand work by industry and format; evidence for how a face behaves in use | Text fetch: `/typefaces/...`, `/in/1/topics/...` (industry), `/search/advanced` | Core |
| Typewolf (typewolf.com) | Pairings and fonts named on real sites | Text fetch | Core for discovery |
| Logobook (logobook.com) | Marks indexed by shape, letter and object: use it to check whether an idea is already common | Text fetch: `/shape/circle/`, `/letter/a/` | Study (a cliché check, not inspiration to copy) |
| Branding Style Guides (brandingstyleguides.com) | Real brand guideline documents: structure and depth | Text fetch | Study |
| Standards Manual (standardsmanual.com) | Reissued classic manuals (NASA, NYCTA, EPA): system thinking | Books (paid) | Study |
| Savee, Recent (recent.design) | Mood and art direction | Savee needs login; Recent fetches | Study |

When a competitor's identity matters, read their own website and social profiles, collect their colours (`color_tools.py info`) and type classes, and log them in the competitor map. Do not guess what is on a site you could not load; ask the person for screenshots.

## Fonts
- **Google Fonts** (mostly SIL OFL): default safe source for logos, web, apps and documents. Per-family licence at `github.com/google/fonts`.
- **Fontshare** (ITF Free Font License for most families, SIL OFL for some; check per family, checked Oct 2026): distinctive display faces; logos allowed; no file handover or subsetting for ITF families (see `typography.md`).
- **Commercial foundries** when budget allows a face no competitor uses (licence per weight and use; the client buys).
- **WhatTheFont** (myfonts.com): identify a font from a client's image; needs a person to upload. If you identify by eye, say it is a guess.

## Icons for brand systems
Lucide (ISC), Phosphor (MIT, six weights), Tabler (MIT) are safe for applications and UI. A brand with a strong drawing style may need a custom icon set drawn on the mark's grid. **Flaticon** free icons need visible attribution and may not be used in logos or trademarks; **Icons8** free use needs a link back and it sells AI-generated imagery: avoid both by default. Never build a logo from a stock icon.

## Colour
oklch.com (picker, gamut view) · Realtime Colors (preview a palette and fonts on a layout) · Huemint is ML-generated: inspiration only. Measurements come from `scripts/color_tools.py`. Pantone and CMYK come from physical guides and the printer, not from a website conversion.

## Standards and legal starting points
WCAG 2.2 quick reference (w3.org/WAI/WCAG22/quickref) for contrast · WIPO Global Brand Database (branddb.wipo.int) and the national register (USPTO, EUIPO TMview, UK IPO, Bangladesh DPDT) for a first trademark screen, always followed by a lawyer's clearance · Paris Convention article 6ter list for protected emblems and flags.

## Mockups
Composite or drawn mockups from licensed sources (for example LS Graphics, Shots.so, Apple Design Resources; checked Oct 2026, verify each licence) or drawn in HTML/SVG. Label every mockup as a mockup; never present a composite as a photograph of a finished sign or vehicle.
