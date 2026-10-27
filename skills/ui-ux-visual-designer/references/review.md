# Review: gates, rubric, critique

Use before presenting any design, and as the whole procedure in critique or audit mode. Evidence before scores: a render, a measured number or a quoted element. "Make it pop" is not a finding.

## 1. Captures (first)
- `python scripts/render.py responsive FILE --outdir shots/` writes full-page captures at 375, 768, 1280 and 1536 plus `report.json`, and prints a check line per width (overflow, h1 count, console errors, broken images, images without alt, unnamed controls, unlabelled fields). Every non-zero value is a finding until explained.
- Repeat with `--dark` when dark mode ships and `--reduced-motion` when there is motion. Reach states with `--eval`, for example `shot FILE --out menu.png --width 375 --eval "document.querySelector('[aria-controls=menu]').click()"`; capture the empty, error, loading and dialog states the same way.
- Squint test at 1280: the first three blobs you see are the three most important things. Grayscale test: hierarchy survives without colour.
- Read every PNG and note what you see, not what you intended.

## 2. Gates (any failure blocks presenting)
| Gate | Pass when | How |
|---|---|---|
| Contrast | text 4.5:1, large text 3:1, control edges, focus rings and meaningful graphics 3:1, in every shipped theme and state | `color_tools.py audit` on the pairs actually used |
| Colour-only meaning | none: status, errors, links in text, chart series carry an icon, word, underline or pattern | look; `color_tools.py cvd` on status and chart colours |
| Reflow | no horizontal scroll at 375 (and 320 for public sites) | 375 capture, right edge |
| Structure | one h1, ordered headings, landmarks, labelled controls, named icon buttons | read the markup |
| Keyboard | everything reachable in visual order; focus visible and never covered by sticky elements; Esc closes the top layer | markup and CSS; interactive test when a browser tool exists |
| Targets | 24 px minimum, 44 px for primary touch targets | measure |
| Real content | no lorem, no fabricated proof, no "[COMPANY NAME]"; placeholders marked `[needs: ...]` | read the copy |
| Licences | every font, icon set and image licensed for this use | `resources.md` |
| States | loading, empty, error and success exist for every data view; hover, focus, disabled, loading for controls | captures or the state list |

## 3. Score (10 criteria, 0 to 4 each, 40 max)
0 missing or broken · 1 poor, slows or puts people off · 2 acceptable with clear issues a professional would fix before launch · 3 good, minor polish · 4 excellent, reference grade.

| # | Criterion | 1 looks like | 4 looks like |
|---|---|---|---|
| 1 | Clarity of purpose | slogan headline, 2 to 3 equal CTAs | outcome headline, one CTA visible at 390 and 1440, h2s tell the story; passes the five-second test |
| 2 | Visual hierarchy | everything the same weight | clear first, second, third read; one dominant element per section; passes squint and grayscale |
| 3 | Typography | > 2 families or > 3 weights, body < 16 on mobile, lines > 90 characters, off-scale sizes | ≤ 2 families, 3 weights, body 16 to 18 at ~1.5, 60 to 75 characters, balanced headings, tabular figures |
| 4 | Colour and contrast | text under 4.5:1, grey on colour, several meaningless accents, inverted dark mode | everything passes, neutrals carry the layout, the accent is rare and purposeful, status colours only for status, dark mode designed |
| 5 | Spacing and alignment | off-scale values, the same space inside and between groups | every value on the scale; section gaps clearly larger than internal gaps; few shared edges |
| 6 | Consistency | three button styles for one action, one-off colours and radii | everything maps to tokens and components; one label per action; radius by hierarchy |
| 7 | Imagery and icons | generic stock, mixed icon sets, emoji | real photos or one deliberate illustration style; one icon set and stroke; every image proves something |
| 8 | Interaction states | default only, no focus, no empty or error states | all states designed; motion within tokens and reduced-motion safe |
| 9 | Accessibility | contrast failures, tiny targets, unnamed icon buttons, colour-only meaning | WCAG 2.2 AA met in the design; keyboard and zoom paths work |
| 10 | Conversion and usability | long forms, buried proof, hidden prices, dead ends, mobile CTA screens down | shortest path, proof where decisions happen, objections answered before the CTA, only necessary fields, every page ends with a next step |

**Verdict:** 36 to 40 reference grade · **34 to 35 client-ready** · 30 to 33 polish before presenting · under 30 revise from the brief, structure or direction. **Client work needs 34 or more with no criterion below 3, and Accessibility and Clarity at 4.** Any 0 blocks regardless of total. For apps and dashboards, read criterion 10 as task efficiency (fewest steps for the top tasks, clear recovery from errors).

Also run the generic check (`direction.md`): tells present only with written reasons, logo-swap test, the signature element named. For dashboards add the QA list in `dashboards-and-data.md`; for mobile, the QA list in `mobile.md`.

## 4. Report and fix loop
```
| # | Criterion | Score | Evidence | Fix (element + problem + change) |
| 1 | Clarity | 2 | w375.png: CTA below the fold | Hero CTA: move above the image on mobile, label "Book a free inspection" |
```
Total, blocking items, verdict. Fix in this order: blockers (broken flows, failed forms, accessibility failures) → clarity → conversion path → hierarchy → colour and contrast → typography → spacing → consistency → states → imagery polish. Re-capture and re-score what changed; stop after three rounds and report what remains open. Write fixes as element + problem + change ("Hero CTA: outline, same weight as nav links. Change to filled primary, 48 px, label 'Book a free inspection'").

## 5. Independent review and pre-handoff checklist
For every client deliverable, when subagents exist, give a fresh reviewer the brief, this file and the PNGs (not your reasoning) and ask for gates and scores with evidence. Where you disagree, the lower score stands unless you can point to evidence. Without subagents, label the report "self-review".

Before handoff, tick every line:
- **Content:** real copy proofread in one English variant; CTA labels identical everywhere; numbers, prices, phones and licence numbers checked against the brief; testimonials approved; legal pages linked; dates and copyright current.
- **Visual:** tokens only (no stray hex, radius or font); 4 px spacing scale; type scale with ≤ 2 families and ≤ 3 weights; contrast 4.5:1 text and 3:1 edges in both themes; one icon set; consistent photo crops; no near-miss alignments (overlap clearly by 24+ or separate by 16+).
- **Interaction:** no `#` links; all states including loading; focus ring never hidden; forms tested end to end (delivery, spam, success); `tel:`, `mailto:` and map links work; reduced motion leaves everything visible.
- **Responsive:** 320, 375, 768, 1024, 1440, 1920 without sideways scroll; nav does not wrap at 1024 to 1280; primary CTA in the first mobile viewport; sticky layers under 15% of the screen.
- **Media and performance:** hero image ≤ 200 KB, others ≤ 150 KB; dimensions on all media; fonts subset and self-hosted where the licence allows; LCP ≤ 2.5 s, CLS ≤ 0.1, INP ≤ 200 ms when measurable.
- **Launch:** favicon set and Apple touch icon; titles, descriptions and a 1200 × 630 share image; custom 404; analytics events named.

## 6. Critique mode (someone else's design or a live site)
1. Context: audience, goal, platform. Read the site or files; ask at most 3 questions and write the rest as assumptions.
2. First impression in two seconds: what a stranger would say it is.
3. Gates, then the 10 criteria with evidence, then the **top three changes**: exactly what to change ("CTA fill #4FA3E0 to #1F6FB2"), the measured effect ("white label 2.6:1 to 5.1:1"), why (tied to the goal), and the cost (CSS only, copy, new photography, rebuild).
4. Name what works before what does not. Critique the work, never the person. A clean audit means nothing measurable is broken, not that the design is good.

## 7. What a self-review cannot prove
Real devices, screen-reader behaviour, real users completing the task, live performance on real networks, and whether the copy is true. Say which were not checked. For high-stakes work recommend a five-user test on the most important task and a screen-reader pass.
