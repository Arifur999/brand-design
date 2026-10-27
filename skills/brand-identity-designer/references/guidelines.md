# Guidelines, handoff, production and legal

## Format and depth
- Brand portal (for brands with staff, partners and vendors; changes over time), a PDF or HTML brand book (small business, one-off; version and date on the cover and in the filename, e.g. `acme-brand-guidelines-v1.0-2026-10.pdf`), and always a **one-page brand sheet** (logo, colours, fonts, three rules) in addition.
- The guidelines are the identity's first application: build them in the brand's own system. Show more than tell (every rule has a visual, every "don't" shows the real mistake), explain why, put what is used most first (a quick-reference page), describe only the approved system (no invented mission statements or stats).

| Depth | For | Contains |
|---|---|---|
| Lite | local business, starter | intro, purpose and promise, personality, short voice chart, logo, colour, typography, graphic device if any, short photography, key applications, accessibility, downloads, contacts, changelog |
| Standard | most clients | Lite in full + brand story, full voice, devices, photography, iconography, illustration if used, short motion, layout grid, full applications |
| Full | multi-location, franchise, product company | Standard + co-branding and sub-brands, dark theme and data colours, shot lists, full motion, tone map and messaging, every touchpoint |

## Sections (use only those the system has)
1. **Intro:** who it is for, how to use it, what to do when it does not cover something; route readers by job ("making a social post? read 4, 6 and 9").
2. **Brand story:** purpose, what we do for whom, positioning, promise, proof.
3. **Personality:** ranked "this, not that".
4. **Voice and tone:** one line, voice chart, tone by situation, 3+ before/after pairs from the client's real copy, writing rules, English variant.
5. **Logo:** the idea; versions table; colourways (full colour on light, on dark, black, white, one brand colour) and which ground each sits on; clear space diagram from the mark's own unit; minimum sizes in px and mm; approved backgrounds; 6 to 10 misuses including 1 to 2 only this mark can suffer; co-branding.
6. **Colour:** table (name, role, token, HEX, RGB, OKLCH, CMYK, spot, contrast); proportions per medium as a starting point, not a rule (the familiar 60-30-10 has no research basis: write the proportion the system actually uses, typically neutral-led with the loudest colour on the least area); ramps 50 to 950; **accessible pairs with ratios** and colours that may never carry text; dark theme; status colours.
7. **Typography:** roles with source and licence coverage, fallbacks for email and Office, hierarchy table, specimen on a real page, rules.
8. **Graphic elements:** each device with origin, scale, crop, colour, placement, don'ts; at least 3 real layouts.
9. **Photography:** approach, direction table, 6 to 12 approved examples, shot list, what to avoid, treatments.
10. **Iconography**, 11. **Illustration**, 12. **Motion** (principles, timing, logo animation storyboard, reduced motion).
13. **Layout:** grids, signature compositions, social safe areas, print margins and bleed.
14. **Applications:** real mockups with callouts and production specs (material, size, method, vendor).
15. **Accessibility commitments** written as testable statements (WCAG 2.2 AA, 4.5:1 and 3:1, 16 px body, never colour alone, alt text, captions, visible focus, reduced motion, 44 px targets, accessible PDFs, minimum print sizes) with who checks and how often.
16. **Downloads:** the logo package, icons, avatars, fonts or links, swatches and tokens, templates; every link points to the single source of truth.
17. **Governance:** brand owner, steward, approval table (template posts need no approval; new formats and print need the marketing lead; signage, vehicles, uniforms and packaging need a proof and the owner; logo or colour changes only by the designer with owner sign-off); quarterly listing audit, yearly physical audit. Fix drift with a better template or a missing asset, not a stricter rule.
18. **Changelog.**

Delivery checklist: no brackets or guidance notes left; every rule has a visual; colour values verified in every mode; CMYK and spot values approved on physical proofs or labelled "unproofed, indicative"; only passing contrast pairs published; font licences confirmed for every listed use; links work; version and date on cover and filename; one-page sheet and vendor pack exported; spelling in one English variant.

## Token handoff (to developers and to ui-ux-visual-designer)
- Export only an audited palette: a failing pair spreads to every screen.
- Three layers: reference scale (`primary-50` to `primary-950`) → semantic roles (`background`, `surface`, `surface-raised`, `border`, `text`, `text-muted`, `primary`, `primary-hover`, `on-primary`, `accent`, `on-accent`, `success` / `warning` / `danger` / `info` with `-subtle` and `on-`, `focus-ring`, `overlay`) → component tokens (the developer's job). Name by job, not hue (`primary`, not `blue`); colour names like "Harbor Blue" live in the guidelines.
- Fills pair only with their `on-` partner; components use roles, never raw steps (a step in a component breaks dark mode).
- When the brand colour fails contrast as a button, keep the exact hex for the logo and large graphics, and map the interactive role to the first darker ramp step that reaches 4.5:1 with its label. Never recolour the logo to fix contrast, and never edit a locked brand colour for a UI check.
- Status colours are not brand colours: if the brand is red, orange or green, shift the danger or success hue 15 to 25 degrees away from it and always pair status with an icon and a word.
- Files: `tokens.css` (light on `:root`, dark on `[data-theme="dark"]` and `prefers-color-scheme`), `tokens.json` in W3C Design Tokens (DTCG) format, one JSON per mode for Figma Variables (DTCG has no modes), and a swatches page with HEX, RGB, OKLCH, ramps and the tested pairs with ratios. Fonts as CSS variables with fallback stacks and embed code; no font files unless the licence allows it. Logo colours are artwork, not tokens.

## File package
```
<brand>-logo-package-v1.0/
  README.txt   what each file is for; colour values per mode; font names and licences; clear space; minimum sizes; guidelines link and version; contact
  01-primary-horizontal/   svg pdf png
  02-stacked/  03-symbol/  04-wordmark/
  05-favicon-app/  06-social-avatars/
  07-print/    cmyk and spot PDFs (only once proofed; otherwise a note saying who produces them)
  08-sign-embroidery-vinyl/   cut-ready files: one-colour versions welded into a single outline (no overlapping
                              shapes, or cutters double-cut), multi-colour versions with one layer per colour,
                              artwork at real size with the measurements; DXF on the sign maker's request
                              (weld with `brand_kit.py boolean union`, which needs skia-pathops)
  09-source/   master vector, outlined
  10-legal/    font licence list, trademark screening log, authorship note
```
Names: `brand-lockup-colourway-mode.ext`, lowercase, hyphens (e.g. `fieldline-horizontal-fullcolor-rgb.svg`); never `final2`. SVG with outlined text, viewBox, `<title>`, no fixed size, no raster; PNG transparent at 500 / 1000 / 2000 px wide for lockups and 256 / 512 / 1024 square for symbols; vector PDF for print; EPS only on request. Produce them with `scripts/brand_kit.py`: `lint` every master (add `--forbid <studio name>` for white-label), `onecolour` for the currentColor master, `export` for transparent PNGs and a vector PDF, `icons` for the favicon set, app icons and manifest, `tokens` for tokens.css, DTCG tokens.json and the swatches page. Open every output once. CMYK, spot and EPS files come from a vector app with the printer's profile: list them as pending, never fake them.
- **Editable templates** for the assets the client makes most (social posts, presentation, letterhead, quote or invoice) in the tool their staff use (Canva or Figma when connected), with logo and type layers locked. Templates beat rules: drift comes from missing templates.

## Print and production honesty
Screen values are exact; CMYK, Pantone, RAL and vinyl codes come from the printer's ICC profile, physical swatch books and fabricator charts. Flow: approve sRGB hex → ask the printing condition (printer, paper, profile) → ICC-aware CMYK with the profile named beside each value → physical proof → the approved sample replaces derived values. Common profiles to confirm: GRACoL 2013 or SWOP (US coated), PSO Coated v3 / FOGRA51 (EU coated), PSO Uncoated v3 / FOGRA52. Pantone needs a current physical guide (C and U differ). Vivid blues, greens and oranges dull in CMYK: consider a spot colour. Uncoated and kraft stocks shift colours: provide separate values or a one-colour version. Embroidery: a simplified drawing, text at least about 6 mm tall (confirm with the digitiser), about 6 thread colours maximum, no gradients.

| Material or condition | What changes | Do |
|---|---|---|
| Uncoated paper | colours print darker and flatter | separate uncoated values; open counters |
| Kraft board | light colours vanish, blues go grey, reds go brick | white underlay or a one-colour version |
| Clear or coloured label film | inks go transparent | white underlay under colour |
| Backlit signs | colour shifts when lit | approve samples by day and at night |
| Large dark areas | 100% K looks grey | rich black (for example C60 M40 Y40 K100 within the printer's ink limit); small text stays 100% K |
| Proofing | | an agreed tolerance, typically ΔE00 of 2 to 3 against the approved sample |
| Pantone | most libraries need a paid Pantone Connect licence in design apps (since 2022) | choose from a physical guide; record number, C or U, and edition |

## Legal and authorship (not legal advice; checked October 2026)
- Purely AI-generated material is not protected by US copyright (US Copyright Office report, January 2025; the human-authorship requirement has been upheld in court; verify current status with counsel); human selection, arrangement and modification are protectable. Keep a **process file** per project (word maps, construction notes, numbered candidates, selections and edits, dates) as the authorship record, and record the human refinement pass.
- Trademark screening ladder (designer scope; report "no obvious conflicts found in [registers, classes, date]", never "cleared"): reverse image search (Google Lens, TinEye) in colour and black → USPTO trademark search (tmsearch.uspto.gov) → WIPO Global Brand Database (image search, Madrid, Article 6ter emblems) → EUIPO / TMview for the EU → UK IPO → the client's national register → unregistered use (web, maps, company registries, domains, handles). Nice classes, e.g. HVAC services 37, dental and landscaping 44, SaaS 42 and downloadable software 9, marketing 35: confirm in the official class list.
- Refer to a lawyer when a similar mark exists in a related class, the client will file or trade in several countries, the brand is high-value, the name is descriptive or geographic, it resembles a famous mark, or the client asks for a clearance opinion.
- Protected emblems are off limits: red cross, red crescent and red crystal, government seals, coats of arms, national flags as emblem grounds, official certification marks (use official badge files only, with permission).

## White-label and client separation
White-label deliverables carry the partner's brand or none: no studio names, URLs, credits or metadata (check SVG comments, PDF metadata, file author fields, filenames). Present through the partner. Licences registered to the partner or end client; only resources that need no credit. One client's names, files and specs never appear in another client's work; only generalised lessons move.
