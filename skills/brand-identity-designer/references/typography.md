# Brand typography

Tags: `[strong]` `[limited]` `[practice]` `[popular-unsupported]`.

## Selection
- **Display carries the voice, text carries the reading.** People attribute consistent personas to typefaces (Brumberger 2003); persona fit matters most in display use, legibility everywhere else. `[limited]`
- Class and voice (vocabulary, culture-bound `[practice]`): grotesk honest, neo-grotesk neutral, geometric modern, humanist warm, old-style literary, Didone dramatic and fragile when small, slab sturdy, mono technical, script personal and hard to read in quantity.
- What holds up: round shapes read sweet and angular sour across countries (Velasco et al. 2015) `[strong]`. There is no "most legible font" (Wallace et al. 2022) `[strong]`; serif versus sans makes no difference once x-height is matched (Arditi & Cho 2005) `[strong]`; humanist sans reads better at a glance at small sizes (Dobres et al. 2016) `[limited]`. "Hard-to-read fonts are remembered better" failed replication. `[popular-unsupported]`
- **Constraints first:** languages and scripts (Bangla, Arabic, Turkish İ ğ ş, Vietnamese diacritics), smallest and largest size, weights needed, numbers (tabular figures if the brand shows prices or data), licence, web budget. Then set the real brand name and a real sentence in each candidate, never lorem.
- Run the reflex test (`routes.md`): Inter, Fraunces, Cormorant, Barlow Condensed, Space Grotesk, Poppins and friends are what every model proposes for the sector.
- Use competitors' type as a map: classify each competitor's heading and body faces by class; a crowded class is category code, an empty cell is room to differ. Leaders often use custom or commercial faces; an open-source route differs by class, width or features.

## Pairing modes (give routes different modes)
| Mode | Use |
|---|---|
| single family | one variable family; hierarchy from weight, optical size and width; lowest risk |
| superfamily | serif + sans sharing skeleton and x-height (IBM Plex, Source) |
| contrast | characterful display + neutral text |
| same designer | two faces by one designer or foundry |
| data face | adds a mono or tabular face only when the brand shows numbers |
Add a second family only if it does something the first cannot. One family per role, every family has a role. Keep x-height and cap-height ratios close when mixing inline.

## Checks (gates)
- **Glyph coverage:** every character of every brand language, including capitals with diacritics, in every weight used. Check the font's language support page (Google Fonts lists supported languages; foundries publish character sets) or test the real sentence rendered: a missing glyph falls back to another font letter by letter.
- **Licence** known and covers each use: logo, web, app, PDF embedding, signage, broadcast.
- **Tabular figures** (`tnum`) when the brand shows numbers.
- Warnings: a text family with fewer than 2 real weights; I, l and 1 confusable (use a stylistic set if available); high stroke contrast in the text role; display faces with hairlines used under about 24 px.
- Casing is the renderer's job: set the document language so Turkish i capitalises to İ.

## Licences
| Source | Rules |
|---|---|
| Google Fonts (mostly SIL OFL 1.1, some Apache) | Commercial use, logos, web, apps, print, self-hosting and redistribution with the licence file. Outlining into a logo needs no credit. Reserved Font Names: a modified version cannot keep the name. Per-family licence in `github.com/google/fonts` (`METADATA.pb`) |
| Fontshare, ITF Free Font License (most families; checked Oct 2026, verify) | Commercial use and logos (registrable as trademarks) allowed, no attribution. **No modifying or subsetting, no giving the files to clients, contractors or printers**: they download from Fontshare themselves. Deliver outlined artwork and PDFs with embedded fonts. 36 families are SIL OFL instead: check `license_type` per family at `api.fontshare.com/v2/fonts` |
| Adobe Fonts | Logos only as outlined artwork; live type in delivered files breaks when the subscription ends, and fonts cannot be handed to clients |
| Commercial foundries | Licensed per weight and per use (desktop, web by pageviews, app, ebook, broadcast); the client buys it in their own name. Trial fonts are for presentation only. Always give a free fallback that is rendered and named as a fallback, never as the original. Before using one in a logo, read the EULA for "logo", "trademark", "modified letterforms" and "transfer to client" |
| Client-supplied fonts | Use as given, never redistribute; if no file, keep the name and offer a fallback |

## Fresher alternatives to overused faces
Overused is fine when layout, colour and imagery are distinctive; never pick a rarer font that fails the checks above. Montserrat → Plus Jakarta Sans, Onest, Host Grotesk · Poppins → Figtree, Rethink Sans · Inter everywhere → Instrument Sans, Hanken Grotesk, Schibsted Grotesk, Switzer (F) · Playfair Display → Gloock, Bodoni Moda, Newsreader at display size · Open Sans, Roboto, Lato → Public Sans, Source Sans 3, Atkinson Hyperlegible Next · Bebas, Oswald → Big Shoulders, Sofia Sans Extra Condensed · Raleway → Jost, Manrope · Lora, Merriweather → Literata, Source Serif 4 · Space Grotesk → Familjen Grotesk · DM Sans → Albert Sans · Instrument Serif (the new default serif) → Young Serif, Gambetta (F), Sentient (F). Trend lists age fast: check current ubiquity on Typewolf and Fonts In Use before relying on this.

## Scripts beyond Latin
Fontshare is mostly Latin-only: check per family. Good starting points: Vietnamese (Be Vietnam Pro, Lexend, Manrope, Newsreader) · Cyrillic (Onest, Golos Text, IBM Plex Sans, Literata) · Arabic (IBM Plex Sans Arabic, Readex Pro, Noto Sans Arabic, Cairo) · Hebrew (Heebo, Assistant) · Devanagari (Anek Devanagari, Mukta, Hind) · Thai (IBM Plex Sans Thai, Kanit) · CJK (Noto Sans JP / SC / KR, self-hosted in slices).
**Bangla:** Hind Siliguri (sans, 300 to 700, widely used, no tabular figures) · Noto Sans Bengali (variable weight and width) · Anek Bangla (variable, matches Anek Latin; width axis for condensed headlines) · Noto Serif Bengali (editorial) · Tiro Bangla (literary headings) · Baloo Da 2 (rounded display: kids, food). Pairings: Hind Siliguri 400/600 + a Latin face with tabular figures for prices and phone numbers (Inter is a model default: prefer Public Sans or the route's own Latin face unless the brief justifies it) (business bilingual); Anek Bangla + Anek Latin (one voice); Noto Serif Bengali + Source Serif 4 (editorial). Rules: Latin face first in the stack, Bangla second; no uppercase, letter-spacing or italics on Bangla (emphasise by weight, colour or size); line height 1.6 to 1.8 body, 1.3 to 1.4 headings; Bangla often looks smaller, so set it 1 to 2 px larger; decide Bengali or Western digits once per project.

## Hierarchy in the guidelines
Type scale with roles (display, H1 to H3, body, small, label, data), weights, line heights, tracking for large display and for all-caps labels, maximum line length, and fallback stacks for email, Office documents and system contexts (name the system fonts that stand in, e.g. Georgia or Arial, with what changes).
