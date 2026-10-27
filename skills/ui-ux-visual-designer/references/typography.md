# Typography: choosing, testing, loading, scripts

Sizes, line height, tracking and the scale live in `foundations.md`. This file covers which fonts to pick, how to prove the choice, and how to ship it. Measured values below come from the files Google Fonts serves (checked Oct 2026, verify: fonts update).

## Choosing a type system: six filters, in this order
A font that fails an early filter is out, however good it looks.
1. **Licence.** Pass: SIL OFL (Google Fonts, part of Fontshare), ITF Free Font License (Fontshare). Fail: "free for personal use", trials (Pangram Pangram included), unknown origin, desktop-only licences on a website. A commercial face is the client's purchase, per weight and per use; name it and give a free fallback.
2. **Scripts.** Every script published today and within two years (latin-ext for Polish, Turkish, Vietnamese; Cyrillic; Bengali). Missing glyphs fall back mid-word and look broken. Fontshare faces are mostly Latin-only: check the character set first.
3. **Weights.** Regular plus a 600 or 700, ideally an italic for body. Load 2 to 3 per family, 4 in total at most.
4. **x-height and apertures.** Body and UI at 0.50 em or more; open apertures survive 12 to 14 px. Ambiguous glyphs (Il1, O0) must differ in codes and IDs.
5. **Format.** Variable font or WOFF2 statics. Reject TTF/OTF-only and kits of dozens of files.
6. **Personality.** Matches the direction in `direction.md`, not the trend.

Category limits: display faces at 32 px and up only (never paragraphs, buttons, nav, forms); script faces 1 to 3 words, once per page, never caps; high-contrast serifs (Bodoni, Didone) break below about 24 px.

| x-height (em) | Meaning | Examples |
|---|---|---|
| 0.50 and up | Comfortable at 16 px body | Inter .546, Manrope .540, Public Sans .517, Figtree .500, Lora .500 |
| 0.44 to 0.49 | Body at 17 to 18 px, or headings only | Source Sans 3 .486, Source Serif 4 .492, Fraunces .469, Newsreader .441 |
| Below 0.42 | Display only (24 px and up) | Crimson Pro .420, EB Garamond .405 (needs about 21.5 px to match Inter at 16), Cormorant .386 |

When two families share a line (Bangla plus Latin, or fallback plus web font), `font-size-adjust: ex-height 0.53` equalises lowercase height.

## Variable or static
- One static Inter weight is about 23.7 KB WOFF2 (latin), the weight axis file about 48.3 KB, weight plus optical size about 72.9 KB. 2 statics or fewer: statics. 3 or more weights, or animated weight: variable (also gives 450 and 550).
- Optical size (`opsz`) pays off on editorial sites running 14 px captions to 72 px headlines: keep `font-optical-sizing: auto`. Families with `opsz` on Google Fonts: Inter, Fraunces, Newsreader, Literata, Source Serif 4, Bodoni Moda, Bricolage Grotesque. Halve the usual display tightening when `opsz` is on.
- Set standard axes with `font-weight` and `font-stretch`; reserve `font-variation-settings` for custom axes (it overrides and resets the others).
- Width axis (`wdth`) gives condensed mobile headlines from one file (Archivo, Mona Sans, Anek Bangla, Instrument Sans). Extremes look odd at body sizes.
- Dark mode: light-on-dark looks bolder, so drop body weight 25 to 50 units on a variable font. Set `font-synthesis: none` on `html` so missing styles show instead of smearing.

## Test a pairing on real content
- Set the real H1, a 3-line paragraph, a table row with prices, a button, a form label with an error and the longest name in both candidates, at 375 and 1440 px. Lorem ipsum hides the problems.
- Pairing rules: two families at most; clearly different (serif display plus grotesk body, condensed display plus humanist body) or the same family at different optical sizes. Two similar sans read as a mistake.
- Check: body at 16 px for 10 seconds (do lines blur?), digits in a table (aligned?), the italic and 600 weights exist, all-caps label with +0.08em tracking, 320 px headline wrap (no orphan word, 4 lines maximum), 200% zoom.
- Look the pair up on Fonts In Use and Typewolf for real branding before presenting.

## Hierarchy recipes
| Pattern | Recipe |
|---|---|
| Marketing section header | Eyebrow (optional, 2 to 4 words, never two) in overline; H2 as a claim not a label ("Same-day repairs in Austin", not "Our services"); lead in `body-lg` muted, max 56ch, one lead only; gap 12 / 16 / 24 |
| App page header | H1 at 30/40 fixed, one-line `body-sm` muted description, actions right on the same row; no eyebrow (breadcrumbs do it) |
| Card | `h4` title (1 to 2 lines), description in `body-sm` muted clamped to 3 lines, `caption` metadata |
| KPI tile | `caption` label muted on top; value in `h1` or display with tabular figures; unit smaller and lighter; delta in `body-sm` with icon and word ("up 12%") |
| Form field | Label `body-sm` 500, input 16 px, helper `body-sm` muted, error `body-sm` danger with icon |
| Long article | Title, `body-lg` standfirst, byline `body-sm`, body 18 px in 65ch, space above H2 2 to 3 times the space below |

Change at most two of size, weight, colour between adjacent levels. Emphasis inside body is 600 or 700 of the same family. Underline links in body copy (colour alone fails WCAG 1.4.1).

## Numerals
- **Tabular lining** (`font-variant-numeric: tabular-nums lining-nums`) for tables, prices in lists, KPIs, timers, anything that updates live (stops jitter). Right-align numeric columns and headers; same decimals per column; real minus U+2212 in finance.
- **Proportional** in running prose. **Oldstyle** (`onum`) only in serif body text where numbers are rare; never in data. Slashed zero for codes and order IDs.
- Defaults tabular: IBM Plex Sans, Roboto, Open Sans, Lato, Source Sans 3, Hanken Grotesk, Mulish, Nunito, Source Serif 4, Newsreader. Has `tnum`: Inter, Geist, Manrope, Instrument Sans, Plus Jakarta Sans, Figtree, Public Sans, Work Sans, Outfit, Montserrat, Archivo, Barlow, Space Grotesk, Bricolage Grotesque, Atkinson Hyperlegible Next, Literata, Lora.
- None (avoid for data): DM Sans, Poppins, Lexend, Albert Sans, Libre Franklin, Quicksand, Fredoka, Oswald, Playfair Display, Fraunces, Instrument Serif, Libre Baskerville, Hind Siliguri. Set numbers in a mono or second family instead.

## Web font loading
1. **Self-host WOFF2 only**, no TTF/OTF/WOFF/EOT in `@font-face`. Sources: Google Fonts download, Fontsource, `next/font`.
2. **Subset** with `unicode-range` so a subset downloads only when used. Latin for English and Western Europe; add latin-ext only for Polish, Czech, Turkish, Vietnamese.
3. **`font-display: swap`** for body and headings; `optional` for decorative faces.
4. **Preload one file** (body regular or the variable file), two at most, with `crossorigin` even same-origin (otherwise it downloads twice).
5. **Metric-matched fallback** so swap causes no layout shift: an `@font-face` named "X Fallback" with `src: local("Arial")` and `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override: 0%`. Put it in the stack right after the web font.

| Web font (fallback Arial) | size-adjust | ascent | descent |
|---|---|---|---|
| Inter | 107.56% | 90.07% | 22.43% |
| Instrument Sans | 102.03% | 95.07% | 24.50% |
| Manrope | 101.63% | 104.89% | 29.52% |
| Geist | 104.71% | 95.98% | 28.17% |
| Source Serif 4 | 106.76% | 97.04% | 31.38% |
| Fraunces | 104.62% | 93.49% | 24.37% |

6. **Budget:** under about 100 KB of fonts on first view (two subset variable files land at 50 to 100 KB). `rem`-based `clamp()` only, never `vw` alone (WCAG 1.4.4).
7. **Privacy:** the Munich Regional Court (LG München I, 3 O 17493/20, Jan 2022) held that loading Google Fonts from Google's servers sends the visitor's IP address to Google without consent and awarded damages. For EU and UK clients self-host. Elementor: load Google Fonts locally.
8. **Fontshare (ITF licence):** commercial use and logos allowed, no credit, but no modifying or subsetting and no passing files to clients or printers. Give the client the download link, never the files; never commit the files to a public repo or template. Subsetting such a font for an EU self-host is a licence conflict: use an OFL face instead (verify the per-family licence on fontshare.com).

## Fonts by script (all Google Fonts, OFL)
| Script | Reliable families |
|---|---|
| Vietnamese | Be Vietnam Pro, Inter, Public Sans, Plus Jakarta Sans, Manrope, Lexend, Newsreader, Fraunces |
| Cyrillic | Inter, Manrope, Onest, Golos Text, Geist, IBM Plex Sans, Literata, Roboto |
| Greek | Inter, Manrope, IBM Plex Sans, Literata, Commissioner, Noto Sans |
| Arabic / Persian | Noto Sans Arabic, IBM Plex Sans Arabic, Readex Pro, Cairo, Rubik; Vazirmatn (Persian); Noto Naskh Arabic or Amiri (traditional) |
| Hebrew | Heebo, Assistant, Rubik, Noto Sans Hebrew |
| Devanagari | Noto Sans Devanagari, Anek Devanagari, Mukta, Hind, IBM Plex Sans Devanagari; Tiro Devanagari Hindi (serif) |
| Thai | Noto Sans Thai, IBM Plex Sans Thai, Kanit, Prompt |
| CJK | Noto Sans JP, SC, KR: huge; self-host with the same slicing via Fontsource |

Never letter-space or uppercase Arabic, Devanagari or Bangla (joins break); line height 1.6 to 1.8.

## Bangla
| Family | Style | Notes |
|---|---|---|
| Hind Siliguri | Sans, 300 to 700 | Default body and UI; no tabular figures, so use the Latin face for prices and phone numbers |
| Noto Sans Bengali | Sans, variable 100 to 900 | One file, many weights |
| Anek Bangla | Sans, variable wght and wdth | Modern brands; pairs with Anek Latin; condensed headlines on mobile |
| Noto Serif Bengali | Serif, variable | Editorial, formal documents |
| Tiro Bangla | Serif 400 and italic | Literary headings, `h2` and up only |
| Baloo Da 2 | Rounded display | Kids, food, friendly consumer |
| Galada | Display | Festive one-offs (Pohela Boishakh, Eid) |

- Pairings: business bilingual Hind Siliguri 400/600 plus Inter 400/600; one voice Anek Bangla throughout; editorial Noto Serif Bengali body, Noto Sans Bengali 500 UI, Source Serif 4 and Source Sans 3 for Latin; premium Tiro Bangla headings plus Hind Siliguri body with Fraunces or Source Serif 4.
- Stack order: Latin face first, Bangla second, so each script picks its own font. List Bangla first only for its built-in Latin.
- Bangla looks smaller than Latin at the same px: body 17 to 18 px under `:lang(bn)`.
- Digits: Bengali (০১২৩) or Latin, decided once with the client; prices and phone numbers usually follow what customers type on their phones. Latin digits in tables.
- Self-host only `bengali` and `latin` subsets with `unicode-range`; preload the Bangla body file on Bangla-first pages. Set `lang="bn"` on `html` or the block so screen readers switch voice.

```css
:root { --font-sans: "Inter", "Hind Siliguri", system-ui, sans-serif; }
:lang(bn) { line-height: 1.7; letter-spacing: 0; font-synthesis: none; font-size: 1.0625em; }
:lang(bn) .t-overline { text-transform: none; font-weight: 600; } /* no capitals in Bangla */
```
Headings in Bangla: line height 1.3 to 1.4. Emphasis by weight or colour, never italic.

## Overused fonts and swaps
Fine when layout, colour and imagery are distinctive; swap when competitors share the face and the swap still passes the six filters.
| Overused | Swap to |
|---|---|
| Montserrat | Plus Jakarta Sans, Onest, Host Grotesk |
| Poppins | Figtree, Outfit, Rethink Sans |
| Inter (as the only voice) | Instrument Sans, Hanken Grotesk, Geist, Schibsted Grotesk, Switzer; or keep Inter for UI plus a display face |
| Clash Display | Cabinet Grotesk, Funnel Display, Bricolage Grotesque |
| Satoshi, General Sans | Switzer, Host Grotesk, Ranade, Rethink Sans |
| Playfair Display | Playfair (new optical-size family), Fraunces, Gloock, Bodoni Moda |
| Open Sans, Roboto, Lato | Public Sans, Source Sans 3, Atkinson Hyperlegible Next |
| Bebas Neue, Oswald | Big Shoulders, Sofia Sans Extra Condensed, Barlow Condensed |
| Raleway | Jost, Manrope, Urbanist |
| Lora, Merriweather | Literata, Source Serif 4, Newsreader |
| Space Grotesk | Familjen Grotesk, Martian Mono (headings), Geist Mono |
| DM Sans | Rethink Sans, Hanken Grotesk, Albert Sans (headings only) |
| Instrument Serif | Newsreader at display opsz, Gambetta or Sentient (Fontshare), Young Serif |
