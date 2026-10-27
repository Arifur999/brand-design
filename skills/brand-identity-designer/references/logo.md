# Logo and mark system

Evidence tags: `[strong]` `[limited]` `[practice]`.

## What a mark must do
- **Identify, not explain.** Meaning comes from use; the hard requirements are one colour and very small sizes (Rand 1991). `[practice]`
- **Distinctive, appropriate, simple, not empty.** Liked, recognisable marks are natural, harmonious and moderately elaborate (Henderson & Cote 1998) `[limited]`; complex marks gain more with exposure, so a new brand leans simple (van Grinsven & Das 2016). `[limited]`
- **Literal is a trade-off.** Descriptive marks help new, small brands, less once known, and hurt in negative categories (Luffarelli et al. 2019) `[limited]`. Describe in a descriptor line or one hint, never with the category's literal object.
- **Shape language follows the axes** (context-bound `[limited]`): round reads soft, angular durable (Jiang et al. 2016); asymmetry reads exciting and hurts a brand that is not (Luffarelli et al. 2019b).
- **Refresh is evolution.** Rounding an angular logo lowered committed customers' attitudes (Walsh et al. 2011) `[limited]`. Name what is kept before drawing.

## Mark types
Wordmark (name in custom-detailed type; best for short, distinctive names) · lettermark or monogram (long names, formal brands; needs a drawn idea, not two letters in a circle) · symbol + wordmark (when the symbol will be used alone: app icons, avatars, favicons) · emblem (name inside a shape; heritage, crafts, sports; weak at small sizes, so needs a simplified small version) · dynamic system (a fixed core with variable parts; only when the brand has many outputs and a team to run it).

Quick chooser: short distinctive name → wordmark plus a monogram for small sizes · long or descriptive name → combination mark · the mark must appear without the name (app icon, van roof, embossing) → a symbol is needed · heritage central → emblem as a secondary mark · umbrella of changing content → dynamic system with a fixed core. By business: trades get a bold wordmark plus a simple symbol for vans and caps; clinics a wordmark or a calm abstract symbol; law and accounting a typographic idea; SaaS a symbol that works as an app icon on day one; retail and DTC wordmark first. Evidence: less familiar brands do better with text-based logos, familiar ones with image-based (Morgan et al. 2021) `[limited]`.

## Process (per round, every route on one contact sheet)
1. Per route, 4 to 6 one-sentence ideas; each says why it is this brand's and not the category's.
2. Build one. First write the construction in words: primitives, grid unit, radii, angles, stroke-to-gap ratios.
3. Render `python scripts/render.py logo-sheet mark.svg --out sheet.png --brand "#HEX" [--wordmark lockup.svg]` and **look**. A broken mark can pass every automated check; only looking catches it.
4. One named defect per mark per round, at most two rounds (a third only to clear a gate or a cliché reading). Render feedback helps a little; extra rounds add breakage. `[limited]`
5. Read it cold at 16 px: does a letter read as another, does a join clog, does a gap close?

## Concept gate (kill a candidate if any answer is yes)
1. Could it sit on a stock-logo template site for a company in another category? (Stripes under a peak, a letter in a rounded square, a circle with a swoosh, a shape inside a badge.)
2. Is the wordmark an unmodified or lightly kerned off-the-shelf face with no ownable decision?
3. Is the idea the category's literal object (tooth, paw, leaf, wave, roof chevron, mountain peak, snowflake)?
4. Can you not state its ownable decision and its source in one sentence?
5. Does it resemble anything on the competitor shelf or in the references at 32 px in grayscale?
Survivors get the **primary touchpoint test**: mock the mark on the brand's main real surface (van side for trades, Google Business profile on a phone for clinics, app icon for software, avatar for personal brands) before choosing.

## SVG construction
- `viewBox="0 0 100 100"` for symbols. Build from primitives (circle, rect, rounded rect, polygon, short arcs, simple paths), each with a semantic `id`. Models place primitives well and fail at complex free-form geometry (Chat2SVG; SVGenius; VGBench). `[limited]`
- **Fills, not strokes** in masters (strokes become outlines anyway and scale wrongly). Holes are real: `fill-rule="evenodd"` or a compound path, never a background-coloured shape on top (it breaks on any other ground).
- **Compute, don't eyeball:** endpoints from sin and cos, repeated parts share exact radius, angle and thickness. Write coordinates to 1 or 2 decimals.
- No `<text>`, `<image>`, filters or `foreignObject` in a master: live text falls back to another font on other machines. Wordmarks are outlined type: `python scripts/outline_text.py fetch "Family Name" --out fonts/` downloads an open-licence family with its licence, and `outline_text.py outline FONT "Text" --out wordmark.svg --tracking 20` shapes it with HarfBuzz (correct kerning, and correct conjuncts and vowel signs for Bangla and other complex scripts) into filled paths. It needs `fonttools` and `uharfbuzz`; if they are missing, ask the person before installing them. Without them, deliver the lockup as HTML with the licensed web font for presentation only and flag "outline before production". Never hand-draw letters of a complex script.
- Colour by role in the system (`primary`, `accent`, `ink`); in files, use the exact brand hex and keep a one-colour version that uses `currentColor`.
- Provide `symbol-small.svg`, a simplified drawing for 16 to 32 px, when details clog.

| Failure | Fix |
|---|---|
| False hole (white shape over a ring) | real evenodd or compound path; check on a coloured ground |
| Almost-equal angles, radii, weights | one grid unit, computed coordinates |
| Hand-drawn letters misread | glyphs from a real font plus one boolean detail |
| Detail creep | no addition without a named defect |
| Mark vanishes on dark or brand ground | a reversed version, or a tile, decided per ground |

## Wordmarks and lockups `[practice]`
- Wordmark from the route's display face, tracked and kerned by eye at large size, plus at most one ownable detail (a cut terminal, a shared stroke, the symbol's angle or radius in one letter) made with `scripts/brand_kit.py boolean` on the outlined letters. Custom letters only for short names. **Customise only OFL fonts** (Google Fonts): the ITF Fontshare licence forbids modifying the font, so Fontshare faces may be used for wordmarks only as set, never cut or redrawn.
- Symbol corners, cut angles and weight follow the type's contrast and terminals; a round symbol with a hard grotesk only as deliberate contrast.
- Lockups: horizontal and stacked; unit = cap height; symbol aligned optically to the cap-height band (round forms overshoot slightly).
- Clear space from the mark's own unit (e.g. the height of the "x" or the symbol's stem). Minimum size just above where the defining feature disappears, in px and mm.
- Note 1 to 2 misuses only this mark can suffer (filled-in stencil gap, symbol moved off its axis) plus the general ones (stretching, recolouring, effects, busy grounds).
- Parts that sit side by side differ in lightness, not only hue.
- OFL fonts may be outlined and modified into a logo with no attribution; ITF Fontshare faces may be used unmodified in a logo; commercial licences need written permission for logo use and modified letterforms.
- Build in black and white first and judge the silhouette before any colour; colour comes last.

## Craft rules that are easy to miss
- Optical corrections at the system stage: overshoot round and pointed forms 1 to 3% past the baseline and cap height (match the display font's O to H ratio); reversed marks (light on dark) look heavier, so thin them slightly, judged at 32 px; optical centre sits slightly above the geometric centre; horizontals slightly thinner than verticals; thin strokes at junctions (ink traps help heavy marks survive small sizes and print).
- Kern for equal-looking areas, not distances; check AV, AW, LT, LY, Ty, Te, To, Va, rn (reads as m), cl (reads as d), and capital-to-lowercase pairs; flip upside down or blur to judge shapes. All-caps wordmarks need positive tracking.
- Counters open enough for small sizes and ink spread on uncoated paper and fabric; hairlines vanish in embroidery and vinyl, so set a minimum stroke.
- Remove one element at a time: if the mark does not get worse, leave it out. Simple is not generic: distinctiveness is one unexpected decision. Silhouette test: filled solid black, is it still this brand?
- Construction grids help drawing; optical corrections override the grid. Golden-ratio overlays added afterwards are presentation theatre: never justify a mark with them.
- Dating trends to avoid as the defining feature: a gradient carrying the idea; translucent overlaps that fail in one colour; bevels, gloss, drop shadows; hairline monoline geometry with nothing to say; this year's free display font unmodified; a lowercase sans plus a dot as the whole idea. Never put a tagline, phone number or year inside the logo.

## Stress tests (record pass or fail in the handover)
Favicon at 16 and 32 px on light and dark tabs · circular avatar at 40 and 110 px · one colour solid black · reversed on brand colour and near-black · grayscale (parts differ in lightness, not only hue) · on three busy real photos (define scrim, panel or reversed treatment) · embroidery at 50 to 75 mm wide (text under ~6 mm is a risk; confirm with the embroiderer) · cut vinyl (no gradients, hairlines or tiny islands) · photocopy · a 1 to 2 s animation whose end frame equals the static mark · squint from 3 to 4 m. Minimum size starting points to test, never copy: horizontal lockup 100 px / 25 mm, stacked 64 px / 18 mm, symbol 16 px with the small drawing or 24 px standard / 6 mm. Below the minimum switch to a compact lockup rather than shrinking.

## Checks
Gates: SVG rules above; 16 and 32 px renders inspected; one-colour version works; the mark reaches 3:1 against every ground it is shown on, or sits on a declared tile (WCAG 1.4.11 as practice; logos are formally exempt); the thinnest feature survives the minimum size; type licence covers logo use. Warnings (judgement): more than 3 colours, near-equal radii or angles, detail growth without a named defect, a cliché from `routes.md` without a written reason.

## Bilingual and multi-script lockups `[practice]`
- Decide which script leads from the audience and the sign's main reader; the other script is set to match, not shrunk into a tagline.
- Match optical size, not point size: Bangla, Devanagari and Arabic need a larger size than Latin to look equal (compare the Latin x-height with the Bangla body under the headline); match stroke weight by eye at the real viewing distance.
- Align on a shared baseline or a shared headline (Bangla hangs from the matra line); never let one script float between the other's lines.
- Prefer families designed together or with matching skeletons (Anek, Noto, Hind with a humanist sans); outline both with `outline_text.py` so shaping is correct.
- Right-to-left scripts mirror lockup order and arrows; numerals follow the market's convention.
- A native reader checks spelling, word breaks and connotations before anything is painted or printed.
