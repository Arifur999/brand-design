# Brand colour

Tags: `[strong]` `[limited]` `[practice]` `[popular-unsupported]`. Arithmetic: `scripts/color_tools.py`.

## Strategy
- **Differ first, fit second.** Colour is the weakest distinctive asset on its own: far lower fame and uniqueness than shapes, and the most shared (Ward et al. 2020; Phua et al. 2026). `[strong]` Ownership = shape + colour + years of consistent use.
- **A colour decision is hue + chroma + lightness + ground.** Saturation reads as power and backfires for gentle products (Labrecque et al. 2024) `[strong]`; a dark ground pulls a hue toward its negative meanings (Celhay et al. 2024) `[strong]`. Choose the ground as strategy.
- **Associations are vocabulary, not rationale.** People report colour-emotion associations; they are not shown to cause feelings or behaviour (Jonauskaite et al. 2025). `[strong]` Never "red converts" or "blue builds trust". `[popular-unsupported]`
- **Conform or differ:** strong brands gain from looking like themselves, weak ones from looking like the segment (Heitmann et al. 2020) `[strong]`; atypical designs win with exposure (Landwehr et al. 2013) `[strong]`. In high-risk categories (health, money, law, children) stay near the category family and differ by lightness, chroma or a small accent (Garaus & Halkias 2019). `[limited]` Moderate deviation beats extreme.
- **Competitor map:** collect each named competitor's primary and secondary colours (from their site or logo), convert to OKLCH (`color_tools.py info`), and look for an empty hue sector or lightness band.
- **Near colour = same colour:** `color_tools.py compare PRIMARY --against COMPETITOR...`. Reject a primary within ΔE2000 < 10 of a direct competitor, or the same hue sector (±20°) and ±0.08 L while both are chromatic; 10 to 20 is borderline. Courts treat close shades as one (BGH, Milka lilac, 2004); thresholds `[practice]`.
- **Local meaning:** check each market for political party, flag, team or mourning readings of the main pair; a national flag as an emblem ground is excluded (Paris Convention art. 6ter).
- **Refresh:** recognised and unshared → keep the hue, tune it; shared or unknown → free to move. Marketers overrate their own assets (Brus et al. 2025). `[limited]`

## Architecture
- Two layers: **brand colours** (identity, locked once approved, never edited to pass a UI check) and **roles** for light and dark modes that point at ramp steps. The anchor step holds the brand hex exactly (`color_tools.py ramp` marks it).
- 1 signature colour, 0 to 1 secondary, 1 accent, a tinted neutral family, 4 semantic (success, warning, danger, info). **2 to 3 hues total**: one hue and more than three both rate lower (O'Donovan et al. 2011). `[strong]`
- Neutrals tinted toward the brand hue (OKLCH chroma ≤ 0.045); chroma 0.05 to 0.09 reads as neither grey nor colour. `[practice]`
- The light ground is a decision: pure white reads clinical; stone and warm off-whites read warm (and cream is a model default, see `routes.md`). Dark mode is derived: tinted near-black, brand fills lightened along their ramp, kept small.
- Extended colours (≤ 5) for illustration and charts, never core roles. 60-30-10 has no research basis `[popular-unsupported]`; the loudest colour takes the least area. `[practice]`

## Pairing
- Harmony comes from lightness structure, chroma balance and hue count, not colour-wheel templates: one very light, one very dark, an orderly ladder between; surfaces from one hue family separated by lightness; the accent differs in hue and stays small (O'Donovan 2011; Schloss & Palmer 2011). `[strong]` Never justify a pick by "it's the complement".
- Well-rated directions: warm + cyan, orange + navy, green + blue or yellow, a light warm figure on a dark cool ground. `[strong]`
- Hue physics: yellow, lime and teal are vivid only when light (they need a dark partner for text); blue and violet are vivid only when dark; red and magenta peak at mid lightness and carry neither white nor black text well. Check with `color_tools.py info`.
- Avoid isoluminant pairs (both saturated, lightness difference small: they shimmer) and red-green as the only signal. Fix with lightness, not hue. `color_tools.py cvd` on every pair that must be told apart.

## Contrast rules for brand use
Text 4.5:1, large text 3:1, UI parts and the logo against its ground 3:1. Parts of a logo that must be told apart differ in lightness by at least 15 to 20 L* (this also protects one-colour and grayscale reproduction). Avoid pure #000 with pure #FFF for long text in dark mode (halation). Links that are not underlined need 3:1 against the surrounding body text as well as 4.5:1 against the ground. Light or thin type (300 and below, hairline serifs) needs 4.5:1 even when large. Write the passing pairs into the guidelines with their ratios; list forbidden pairs too.

## Print and production honesty
- Screen values are exact (HEX, RGB, OKLCH). CMYK and Pantone values derived on screen are **indicative**: a printer's ICC profile and a physical swatch book decide them. Label them "to be proofed" until they are.
- Pantone matching needs a current physical guide (coated and uncoated differ). Bright screen colours (saturated blues, greens, oranges) often fall outside CMYK; pick the print equivalent with the printer and record both.
- Vinyl, paint and embroidery have their own limited colour ranges; check with the fabricator for vehicles, signage and uniforms.
