# Visual foundations

The numbers and rules behind every interface. Defaults, not laws: break one when the brief gives a reason, and write the reason down.

## Hierarchy
- Tools, strongest to subtlest: size, weight, colour and contrast, spacing, position. Emphasise by de-emphasising the rest: make the label muted rather than the value huge; use weight and colour before size.
- One primary element per view (the headline or the main action). Button hierarchy: one primary (solid), secondary (outline or subtle), tertiary (text). Red only when the destructive action is the primary action of that view.
- 2 to 3 text colours: foreground, muted, tertiary for metadata. On coloured backgrounds tint the muted text toward the background hue instead of grey.
- 2 weights for UI text, at most 3 (400 body, 500 or 600 labels and headings). Nothing under 400 at small sizes.
- Scanning: text-heavy pages read in an F (front-load headings and the first two words of bullets); sparse landing pages read in a Z.
- Labels are often unnecessary: "12 left in stock" beats "Stock: 12".

## Layout and grid
- 12 columns desktop, 8 tablet, 4 mobile. Gutters 16 mobile, 24 tablet, 24 to 32 desktop.
- Containers: about 1280 px for marketing, 1152 px for calmer pages; side padding 16 / 24 / 32.
- Measure: 45 to 90 characters per line, aim for 60 to 75. Hero subheads about 40 to 45 characters wide in em terms (max-width ~42rem).
- Give elements the width they need; a 600 px form does not need 1200 px. Prefer intrinsic layouts (`repeat(auto-fit, minmax(min(18rem, 100%), 1fr))`) over breakpoint tables.
- Count distinct left edges on a page; fewer is calmer. Break the centred-everything habit with asymmetric splits (7/5, 8/4) where the content allows.

## Spacing
- 4 px base; use a constrained scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Adjacent steps should differ by at least ~25% or the difference is invisible.
- Inside < between < sections: card padding 16 to 24, gap between cards 24 to 32, sections 64 mobile to 96 to 128 desktop.
- A heading sits closer to what follows than to what precedes it.
- Start with too much whitespace and remove. Cramped layouts are the most common amateur tell. Dense UI is fine when density is consistent (pick one row height, e.g. 36 or 40, and keep it).

## Typography
- Body 16 to 18 px (never under 16 for inputs on mobile: iOS zooms). Line height 1.4 to 1.6 body, 1.1 to 1.25 headings, 1.0 to 1.1 for display above 48 px.
- Tracking: tighten large headings slightly (about -0.02em), loosen short all-caps labels (+0.05em), leave body at 0.
- Scale ratio: 1.2 dense UI, 1.25 general, 1.333 expressive marketing. 6 to 8 sizes total. Fluid marketing type: interpolate a small-screen scale (base 16, ratio 1.2) to a large-screen scale (base 18 to 20, ratio 1.25 to 1.333) with `clamp()`, always with a `rem` term so zoom still works (WCAG 1.4.4). App UI uses fixed sizes.
- One family is often enough; two at most, and if two, clearly different (serif display plus grotesk body, condensed display plus humanist body). Same-family optical sizes (display vs text cuts) add expression without a second voice.
- Tabular figures for prices, tables, counters and timers. Real quotes, apostrophes and ellipses. No all-caps beyond short labels; no centred text beyond 2 to 3 lines. `text-wrap: balance` on headings, `pretty` on paragraphs.
- Choose fonts from constraints first: languages and scripts to cover (Bangla, Arabic, Vietnamese diacritics), smallest size, weights, licence, web budget. Then set real content in candidates.

## Colour
- Structure: one accent for the primary action, links, focus ring and key highlights. In product UI the accent covers about 5% of the screen; on marketing pages a little more. If the accent is everywhere it stops signalling.
- Neutrals: a 10 to 12 step ramp tinted toward the brand hue (OKLCH chroma 0.005 to 0.02) so greys do not look dead.
- Semantic colours (success, warning, danger, info) each need a subtle background, a border, a solid and a text step. Never meaning by colour alone: add an icon and a word.
- Role-based scales (Radix model): steps 1 to 2 backgrounds, 3 to 5 component backgrounds (normal, hover, active), 6 to 8 borders (subtle, interactive, strong/focus), 9 to 10 solid fills, 11 to 12 text. Map design tokens onto roles, never onto raw hues.
- Work in OKLCH: equal L looks equally light across hues (HSL does not). Build ramps by stepping L at fixed hue and reducing chroma at the extremes; derive hover as L -0.05 to -0.08 in light mode, + in dark. `scripts/color_tools.py ramp` does this.
- Contrast (WCAG 2.2 AA): text 4.5:1; large text (24 px regular or 18.66 px bold) 3:1; UI parts and meaningful graphics (input borders, focus rings, chart lines, icons that carry meaning) 3:1 against neighbours. Thin or light weights (300 and below) need 4.5:1 even when large. Placeholder text is not a label.
- Dark mode is a second design, not a filter: background L 0.13 to 0.18 (not black), text L 0.93 to 0.97 (not white), elevation by lighter surfaces (+0.03 to 0.06 per layer) instead of shadows, accent lighter and less chromatic, every pair rechecked. Light text on dark looks bolder; drop a weight step for body if it glows.
- Saturated accents vibrate in small text: keep them for fills and display sizes.

## Depth, radius, borders
- One depth language per product: borders (precise, technical), shadows (softer, consumer) or tonal surfaces. Heavy borders plus heavy shadows look noisy.
- Shadows: light from above, positive y offset, blur grows with elevation, 2 to 3 layered shadows tinted toward the background hue. Levels: 0 page, 1 card, 2 dropdown or popover, 3 dialog or toast.
- Borders 1 px, low contrast for decoration; interactive borders must reach 3:1.
- One base radius, derived sizes. Nested radius = outer radius minus the padding between. Radius is personality: 0 to 4 precise or serious, 6 to 12 friendly or modern, pill for playful or for tags and buttons only. Hierarchy decides radius (full-bleed sections square, buttons softer), not "everything rounded-2xl".

## Gestalt and grouping
Proximity fixes most clutter without boxes. Similar things look and behave the same. Use common region (backgrounds, borders) sparingly. Align baselines in rows of cards. Overlays need a scrim (black 40 to 60%).

## Imagery and icons
- One photo treatment (grade, crop ratios from a short list: 16:9, 4:3, 1:1, 3:4). Real photos of the actual business beat stock. Always reserve the image's aspect ratio to avoid layout shift. Text over images needs a scrim to keep 4.5:1.
- One icon set, one stroke weight, sizes per context (16 inline, 20 in controls, 24 standalone), optically centred with text. Illustrations in one style drawn from the brand tokens, only when they have a job.

## Interaction states
Every interactive element: default, hover (pointer only), focus-visible (2 px ring with 2 px offset, at least 3:1, never removed), active or pressed, disabled (explain why when not obvious), loading (keep the label width, show progress), and where relevant selected, error and success. Show feedback within 100 ms; anything over 1 s needs a progress indicator.

## Motion
- Purpose only: show what changed, where something came from, or that the system is working. One orchestrated moment per page beats scattered effects.
- Durations: 100 to 150 ms for small state changes (hover, toggles), 200 to 300 ms for components entering (menus, dialogs), 300 to 500 ms for larger layout or page transitions; exits about 20% faster than entrances. Calm brands can go slower (400 to 600 ms fades); app UI stays at the short end.
- Easing: ease-out for entrances (e.g. `cubic-bezier(0.25, 1, 0.5, 1)`), ease-in for exits, ease-in-out for movement on screen; springs for direct manipulation.
- Animate `transform` and `opacity` only. Never animate keyboard-driven or high-frequency actions. Respect `prefers-reduced-motion` (replace movement with a fade or nothing). Nothing flashes more than 3 times per second.
- Intensity levels: 0 none, 1 state feedback only (default for apps), 2 plus subtle reveals, 3 one orchestrated sequence (marketing), 4 scroll storytelling (portfolios, launches). Choose the level in the direction and keep it.

## Quick defaults (when nothing else is decided)
Container 1280 with 16/24/32 side padding · body 16 to 18 at 1.5 · headings 1.1 to 1.2 slightly tightened · scale 1.25 · section padding 64 / 96 · card padding 24 · gap 24 to 32 · neutral ramp tinted to the brand hue · one accent · radius 8 to 10 with nested rule · focus ring 2 px + 2 px offset · targets 44 px for primary touch actions, 24 px absolute minimum · motion 150 / 220 / 320 ms, ease-out.
