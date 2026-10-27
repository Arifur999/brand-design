# Visual direction: distinct, not default

## Why AI interfaces look alike
Models sample the most common patterns, so without direction they produce the statistical average of the web ("distributional convergence", Anthropic, *Improving frontend design through skills*). In a 2025 scoring of 1,590 Show HN pages, 22% showed four or more of the tells below and 32% two or three (Krebs, *Scoring Show HN pages for AI design patterns*). Visitors recognise the look and read it as low effort. Banning a default just moves you to the next default, so the method is: decide from the business, then check.

## The tells (each needs a reason in the brief, or it goes)
- **Colour and surface:** purple or indigo gradients on white; gradient text and buttons; permanent dark mode with neon glows; glass on every surface; abstract blobs, mesh gradients and floating 3D shapes unrelated to the business. Newer defaults: warm cream (~#F4F1EA) with a high-contrast serif and terracotta (~#D97757); near-black with one acid-green or vermilion accent; broadsheet layout with hairline rules and zero radius everywhere; navy plus gold for law, finance and property.
- **Type:** Inter or system UI for everything with no decision behind it; the trendy defaults (Space Grotesk, Geist, Instrument Serif, Plus Jakarta Sans, Outfit, Fraunces); one accented word in the headline (italic serif, gradient or coloured word); tracked all-caps eyebrow above every heading; pill badge above the H1 ("New: AI-powered"); monospace meta labels joined with middle dots; an arrow after every link.
- **Layout and components:** centred hero, three icon-topped feature cards, testimonial carousel, CTA band (the template); bento grid of uniform tiles with no real content; identical rounded-2xl cards with the same soft grey shadow; coloured left borders on cards; a row of three big stats; 01/02/03 numbering on things that are not a sequence; emoji or generic line icons as feature icons.
- **Content and motion:** "Powerful features to help you grow" copy; fake logos (Acme, Globex) or fake testimonials; shimmer, sparkle, spinning gradient borders, AI glow; fade-and-slide-up on every section; hover lift on every card.
- **Dashboards:** glowing or gradient KPI cards; five or more equal KPI cards; pie, donut or gauge by default; fake sparklines; random chart colours; centred table text; status as a coloured dot alone; every action a primary button.

## Techniques for distinctiveness
1. **Derive the direction from the business, in writing.** Its materials, place, customers, vernacular and the product's own truth: a roofer's world is asphalt, copper flashing, safety orange and crew trucks; a ledger product is ruled rows and two-currency columns. Write a token plan before any screen: 3 adjectives plus one "never", 4 to 6 named colours with roles, type roles, layout concept (ASCII wireframe), radius and depth, imagery, motion level, 3 principles.
2. **One signature element** that does real work and is only true of this product: an annotated product frame that traces one real job, a before/after slider for a renovator, a seasonal service calendar, a typographic work index. Spend boldness there; everything else stays quiet. Remove one accessory before shipping.
3. **Typographic personality:** a real scale, decisive weight contrast, hand-chosen line breaks in the headline, width or optical axes used on purpose.
4. **A colour story from something true:** the truck livery, the storefront, the product packaging. One dominant colour, one neutral family, one sharp accent used sparingly.
5. **Real imagery direction:** write a shot list (crew on a real job, before/after from the same angle, the founder at work, product in context) and one treatment. If there are no photos, the product UI or typography carries the page; budget a shoot rather than using stock people.
6. **Layout rhythm:** asymmetric splits, image bleeding off one edge, one or two grid-breaking moments per page, sections alternating full-bleed, contained, dense and airy.
7. **Texture with a reason:** paper grain for a print-heritage brand, a blueprint grid for engineers; never generic noise.
8. **Details:** written micro-copy on empty states, errors and success; real favicon and social image; a 404 in the brand voice. Custom cursors only where the cursor is the concept, never on lead-gen or e-commerce.
9. **Rework component-library defaults:** retheme every token (background, foreground, primary, radius, ring, border) before using a component; build heroes, cards and section shells yourself; keep the library for behaviour-heavy primitives (dialog, menu, tabs, inputs).

## Effects budget
One or two effect types per page (grain, gradient, glass, glow, texture, shadow drama), at most one per viewport, none on forms, checkout or dashboards. Removal test: delete the effect; if nothing is lost, leave it out.

## The generic check (run before presenting)
1. "Would I have produced this plan for any similar brief?" If yes, change the generic part and say what you changed.
2. **Logo swap test:** put a competitor's logo on the page. If every claim and visual still fits, the page is not specific enough.
3. Count the tells present; each one stays only with a written reason.
4. Name the signature element and the job it does.

## Direction recipes (starting points, never the answer)
Take the palette hue from something real the client owns (van wrap, signage, packaging, storefront) and check each recipe font against the type of 3 named competitors: if a competitor already uses it, swap it. A recipe used unchanged is a template.
Fonts: (G) Google Fonts, (F) Fontshare (check the per-family licence).

| Recipe | Fits | Type | Palette | Shape and depth | Imagery and motion | Signature idea |
|---|---|---|---|---|---|---|
| Workwear trust | HVAC, roofing, plumbing, electrical, pest control | Barlow Condensed 600/700 (G) display, Public Sans (G) body | spruce #0F3D3E dominant, signal amber #F2A900 for CTA only, concrete #E7E6E1, ink #1A1D1F | 6 px buttons, 8 px cards, borders and solid blocks, no blur shadows | Crew in uniform on real jobs, trucks, before/after, named technicians; motion level 1 | Trust bar styled like a vehicle decal (licence number, years, guarantee) |
| Calm clinical | dental, med spa, vets, physio | Newsreader (G) light display, Figtree (G) body | porcelain #F6F8F7, deep teal #245B57, mist #D7E7E2, plum accent #7A3E65, ink #1E2A29 | 14 to 20 px soft radii, one light shadow on floating items | Real clinicians and rooms, natural light; slow 400 ms fades | "First visit, step by step" strip with real photos (answers anxiety) |
| Swiss technical | B2B SaaS, dev tools, data and infra | Hanken Grotesk (G) throughout, a mono only in code | paper oklch(0.985 0.004 100), graphite oklch(0.25 0.01 260), rule oklch(0.9 0.005 100), one signal colour, highlighter for annotations only | 4 to 6 px, hairlines, shadow only on product frames | Real product UI, annotated; short muted loops or an interactive demo | Annotated product frame doing the feature section's job |
| Editorial studio | agencies, consultancies, architects, publishers | Zodiak (F) or Gloock (G) very large, Instrument Sans (G) body | stone #E9EAE6, ink #22201C, cobalt #2340D9 for links and one block, warm grey #8C877E | 0 to 2 px, no shadows, structure from whitespace and scale (not hairlines everywhere) | Large project images with client and result; one headline sequence | Selected-work index as a typographic list revealing images on hover and focus |
| Quiet luxury | high-end builders and remodelers, interiors, boutique hotels, real estate | Bodoni Moda (G) display, Jost (G) 300/400 body | olive black #2E3328, limestone #D9D4C7, brass #A88B4A, ivory #F5F3EE | 0 radius, no shadows | Full-bleed architecture and twilight photography; slow 600 to 900 ms crossfades | One full-viewport project film or sequence; consultation CTA, not "Buy" |
| Friendly bold | pet services, kids, cafes, consumer apps | Bricolage Grotesque (G) with width and optical axes, Rethink Sans (G) body | buttercup #FFD23F, tomato #EE4B2B, sky #8EC5FF, ink #1D1A33, paper #FFFBF0 | 20 px to pill, 2 px ink borders, hard offset shadow (4 px 4 px 0 ink) on CTA and featured cards only | Real customer or pet photos in organic frames, a few hand-drawn doodles; springy press state | Gallery of real "after" photos with names |
| Raw brutalist | creative portfolios, music, fashion, indie products | Archivo (G) variable at extreme width and 800 to 900 weight | white, black, one loud accent (ultramarine #3A2BFF or safety orange #FF5F00) | 0 radius, 2 px solid borders | Raw crops, one duotone; instant state changes | Type at viewport scale you scroll through |
| Grounded organic | landscaping, farms, wellness, food | Young Serif (G) or Fraunces soft axis display, Work Sans (G) body | moss #3F5E3A, pale sage #EEF1EA, bark #4A3B2E, sun #E9B949 for CTA, fern #8BAA6B | 12 px, one soft shadow on overlapping photo cards | Seasonal project photos, before/after from the same spot; gentle fades | Seasonal services calendar that drives repeat bookings |

Note that several recipe fonts sit on the trendy-default list; that is acceptable when the recipe's reason applies, but for a client whose competitors already use them, swap the face.

## Presenting directions
- Offer options only when the decision depends on taste or brand strategy; otherwise decide and explain.
- 2 to 3 directions, never more; recommend one. More options hurt choice when options are complex (Chernev et al., 2015).
- Directions must differ in structure, type and imagery, not only palette. Each gets: one sentence of idea, the token plan, the same key screen rendered at the same size, and one line on what it risks.
- Ask "which direction best expresses [the adjective the brief chose]?", not "which do you like?". Use AskUserQuestion with previews, or a rendered comparison board.
- If the person wants parts of different directions, rebuild a coherent direction from those parts and say what you had to change to make them fit.
