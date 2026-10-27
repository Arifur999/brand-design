# Review: gates, rubric, critique

Run before every presentation and before delivery. Each result is PASS, FIX or FAIL with evidence (file name, render, number). For full identities, print work and final delivery, have an independent reviewer (a fresh subagent given the brief, this file and the files, not your reasoning) score it when subagents are available; otherwise label the report "self-review" and recommend a human review before the client sees it.

Research status matters: if competitor research did not run, G2 and G3 cannot pass. Say so.

## Gates
| Gate | Pass when |
|---|---|
| G1 Strategy | every major choice cites a line of the brief or platform |
| G2 Distinctiveness | compared with the competitor wall in grayscale at the same size; logo-off test passed; concept gate passed (`logo.md`) with the ownable decision and its source written down; no unjustified cliché or model default (`routes.md`, `sectors.md`) |
| G3 Originality | references logged as principles; reverse image search on finalists done, or listed as a human step (FIX) |
| G4 Small-size legibility | logo sheet viewed, including the enlarged 16 and 32 px rasters; avatar circle; squint and grayscale; primary touchpoint mock viewed |
| G5 Colour | `color_tools.py audit` passes for every text and UI pair used, light and dark; `compare` against competitor primaries; `cvd` on pairs that must be told apart; brand colour and action role separated where contrast requires |
| G6 Typography | licences recorded for each use including the logo; glyph coverage for every brand language; hierarchy and fallbacks set |
| G7 Production | SVG masters clean (no live text, no raster, viewBox, title, real holes); one-colour and reversed versions exist; exports open |
| G8 System cohesion | family test across 6 to 10 applications; constants and variables written |
| G9 Platform | sizes and safe areas checked against `applications.md`, with check dates |
| G10 Documentation | guideline values match the master files (hex, fonts, clear space, minimum sizes); no lorem; no fabricated proof |
| G11 Writing | real or marked-draft copy; every claim on an asset confirmed by the client or marked draft for approval |
| G12 Delivery | folder structure, naming, README, licences; white-label check; human refinement pass done or listed as pending |
A single asset on an approved brand runs only G4, G5, G7, G9, G10 and G11.

## Identity rubric (11 criteria, 1 to 4 each, 44 max)
**Ship at 34/44 or more, with no score below 3 on strategic fit, distinctiveness, small-size legibility or craft.** Below the bar, do not present it as finished; report what blocks it.

Anchors (apply to every criterion): **4** exemplary, nothing to fix, evidence attached · **3** solid, small fixes only · **2** a real weakness a client or reviewer would notice · **1** broken or missing.

| Criterion | What a 4 looks like | What a 2 looks like |
|---|---|---|
| Strategic fit | the lead trait is recognisable without being told; every choice traces to the brief | looks good but could belong to a different brief |
| Distinctiveness | stands apart from every named competitor at 32 px in grayscale; no unjustified cliché | shares a hue sector, type class or mark subject with a direct competitor |
| Simplicity with one ownable decision | reducible to one sentence and one unexpected decision | either generic, or several competing ideas |
| Small-size legibility | reads at 16 px and in a 40 px avatar; one colour works | details clog or vanish at 32 px; needs colour to read |
| Craft | optical balance, consistent weights and corners, kerned by eye, clean geometry | near-equal radii, uneven strokes, awkward joins |
| Colour system | roles, ramps, all used pairs pass, competitor distance checked, print values honestly labelled | pairs untested or failing, roles unclear |
| Type system | clear roles, licences fit every use, languages covered | licence or glyph coverage unknown, roles blurred |
| Supporting devices and imagery | a device derived from the mechanism, with rules; photo direction a photographer could follow | decoration with no rules, or none |
| Flexibility across applications | works on the core touchpoints, including one hard case | only shown on flattering mockups |
| Documentation accuracy | values in guidelines match the files; nothing invented | mismatched values or missing rules |
| Presentation clarity | idea first, equal finish across routes, a clear question for the client | a gallery without rationale |

Fix order: strategy misfit → distinctiveness and originality → legibility → accessibility → production → polish. Re-run affected checks after each important change.

## Report
```
Project · deliverable set · round · date · reviewer mode (independent / self-review) · research status
Gates: G1 PASS (evidence) ... G12 FIX (what is pending)
Rubric: criterion scores, total /44, ship bar met yes/no
Open issues: needs client / vendor / lawyer
```
Completion note to the person: delivered (files), route chosen and why (two lines tied to the brief), verified (what and how), assumed, not done or needs a human or vendor, next decision. Never call anything "final", "perfect" or "trademark-safe" without evidence.

## Critique mode (an existing identity)
1. **Context:** sector, competitors, position, markets, languages. Read the website and profiles first; ask at most 3 questions and write the rest as assumptions. Confirm which colours are the brand's before judging (sites carry other brands' colours in widgets and badges).
2. **First impression in two seconds:** what would a stranger say this brand is, and what do they remember?
3. **Gates** that apply (contrast, glyphs, licences, logo file quality, competitor colour distance, protected emblems). Unchecked gates are marked "not checked: reason", never passed.
4. **Findings,** two to four lines per component with evidence: logo (distinctive against the shelf? identifies without explaining? one colour, reversed, 16 px? construction issues? clichés?), type (role split, class against competitors, weights, tabular figures, licence cost), palette (category legibility versus differentiation, ownability, roles, drift into near-duplicates, production), cohesion (one mechanism or three unrelated picks? one loud thing or several?). "Feels modern" is not evidence; "primary L 0.62, C 0.19, saturated mid-light" is.
5. **Top three changes,** failed gates first (unreadable, then confusion with a competitor, licence, glyphs), then the biggest weakness against the brief, cheapest first among equals. Each states what exactly ("CTA fill #4FA3E0 to #1F6FB2"), the measured effect ("white label 2.6:1 to 5.1:1"), why (one sentence tied to the brief) and the cost (tokens, CSS, reprint, logo redraw). Name what is worth keeping. No overall score: a clean audit means nothing is measurably broken, not that the identity is good.
