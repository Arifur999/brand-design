# Imagery: photography, illustration, text over images, delivery

Every image proves or explains something, or it goes. Photos prove, illustrations explain. Foundations covers the one-treatment rule; this file covers the decisions behind it. Source licences: `resources.md`.

## Photo, stock or illustration
| Situation | Use |
|---|---|
| Local and service business, clinic, trades, restaurant, property | Real photography: hired, or a guided phone shoot |
| Software, finance, insurance, process | Real product UI, diagrams, illustration; real team photos on About and Contact |
| Sensitive topics (mental health, legal trouble, conditions) | Illustration, or non-identifying photos (hands, objects, rooms) |
| Not built yet (developments, upcoming products) | Renders or illustration, labelled as such |
| Blog headers, atmosphere | Curated stock, graded to match the library |
| Team, testimonials, before/after, portfolio, premises, results | Only real, permissioned photos. Never stock, never AI |

## Photo direction (one page per project, each choice traced to a brand trait)
- **Subject:** what proves the main claim. "Fast" shows arrival and speed; "careful" shows hands and detail.
- **Light:** soft daylight (warm, honest); high-key (clean, clinical); low-key with one source (premium); hard flash (editorial, raw).
- **Grade:** warm (friendly), true colour (food, products, property: accuracy sells), cool and slightly desaturated (technical). One preset or LUT for the whole library, stock included.
- **Composition:** eye level (trust), low angle (strength), overhead (food, product), wide with context (scale), tight detail (craft). Alternate tight and wide down a page.
- **People:** candid action beats posed smiles; direct-to-camera only for team portraits (eye contact builds accountability). Match the real audience in age, body, ethnicity and ability.
- **Show context** stock cannot fake: the technician at a recognisable home, the dentist in the real operatory.
- **Leave room for type:** a quiet area (sky, wall, blurred background) on the headline side, at least 40% of the frame.
- **Banned tropes:** handshakes, pointing at laptops, headset "agents", generic skylines.
- Retouch lightly: remove cables, bins, stray signs; keep skin, materials and wear real.

## Shot-list template (send to client or photographer before the shoot)
| Shot | Orientation | Used for |
|---|---|---|
| Hero: work or team in context | Landscape and vertical of the same setup | Hero 16:9 desktop, 4:5 mobile |
| Team portraits, same background, light, framing | Vertical 4:5 | About, team grid |
| Action: work in progress | Both | Service pages, social |
| Details: tools, materials, hands, finishes | Both | Feature cards, section breaks |
| Place: exterior with signage, interior, vehicles | Landscape | Contact, location pages |
| Results: before/after from the same spot, angle, time of day | Same orientation for both | Portfolio, case studies |
| Customer moments (signed releases) | Both | Testimonials |

- Phone shoot rules: clean the lens, daylight, eye level, 1x lens (no digital zoom), no beauty filter, 3 frames per setup in both orientations, before/after at the same time of day.
- Hire a photographer when the site must prove the business is real and local, the founder is part of what is sold, colour accuracy sells, or it is a launch or rebrand (one shoot feeds site, Google Business Profile, social, ads).

## Aspect ratio per component (one ratio per component type)
| Ratio | Use |
|---|---|
| 21:9 | Cinematic band; becomes 4:5 or 1:1 on mobile |
| 16:9 | Hero, video, default card media |
| 3:2 | Editorial and blog images |
| 4:3 | Service and product cards, galleries |
| 1:1 | Avatars, thumbnails, product tiles |
| 4:5 | Team portraits, mobile hero, Instagram/Facebook portrait |
| 9:16 | Stories, Reels, full-screen mobile |
| 1.91:1 | Open Graph (1200 x 630); keep faces and text central |

Reserve space with `width`/`height` or `aspect-ratio`. Control the focal point per image with `object-position` (for example `50% 30%` for a high face). Never crop people at joints (wrists, elbows, knees); team grids share headroom and an eye line about a third from the top.

## Treatments
- Duotone or monochrome only to unify mismatched sources: all images in a section or none. Text over duotone still needs the contrast check.
- Grain 3 to 6%. Soft crop (image dissolving into the section): use `mask-image`, not a coloured gradient overlay, which breaks in dark mode.
- Cutout that crosses its frame: one per page, never over body text, forms or CTAs, clean edges at 2x, never mixed with boxed photos in one viewport.

## Text over images (contrast measured at the worst pixel: lightest pixel under light text)
Scrim opacity needed over a pure white pixel (computed with WCAG luminance, re-verified):

| Text | Scrim colour | 4.5:1 | 3:1 (large text) |
|---|---|---|---|
| #FFFFFF | rgb(20 18 16) | 58% | 45% |
| #FFFFFF | black | 54% | 42% |
| #F7F6F3 | rgb(20 18 16) | 60% | 48% |

- Use 60% behind normal text unless you can prove the image is darker there. A 50% overlay token alone does not protect small text.
- Options, best first: crop so text lands on a dark quiet area, gradient scrim from the text side (60% or more across the text block), solid panel overlapping the edge, text beside the image. Paragraphs, forms and anything over 2 lines go beside, not on.
- `text-shadow` is not a contrast fix; a faint extra at most.
- Dark mode pitfall: `text-inverse` turns dark in dark themes. Over images use fixed #FFFFFF, never the token.
- Video backgrounds: scrim must hold for the brightest frame, visible pause control (WCAG 2.2.2), stops under reduced motion. Recheck the mobile crop, where the subject moves under the text.

## Illustration
| Style | Feel | Risk |
|---|---|---|
| Flat vector | Clean, friendly | Looks templated unless recoloured |
| Line / editorial | Calm, premium | Breaks up small; match icon stroke |
| Isometric | Technical | Dates fast, hard to keep consistent |
| 3D / clay | Playful, tactile | Heavy files, uncanny when half-real |
| Hand-drawn | Human, crafted | Needs one illustrator |
| Abstract geometric | Brand-led | Says little without copy |

- Consistency: one style from one source, palette locked to tokens (recolour to primary, accent, neutrals), line weight equal to the icon set, one perspective, a deliberate approach to skin tones and bodies, at most one illustration per section. Never mix illustrated characters and real people in one frame.
- Illustration wins for abstract services, how-it-works, sensitive topics, empty states, data concepts. Photos win for physical services, food, places, property, people-led trust.
- Sources (checked Oct 2026, verify): unDraw is free and recolourable but everywhere, so never the signature; Storyset free tier requires credit, so treat it as unusable on client sites; Humaaans, Open Peeps and Blush are dated (frozen about 2020). A signature style means commissioning one illustrator.

## Licences and releases
- Get a written licence covering web, social, ads and print with no end date. Keep model releases for identifiable people and property releases for private interiors.
- Unsplash and Pexels: free commercial use, but no model-release guarantee, so keep identifiable people out of ads and endorsement-like contexts; reverse-search a hero for overuse. Unsplash+ is a separate paid licence.
- Confirm you may show client work in your own portfolio (white-label and NDA work often forbids it).
- Log source and licence for every file; file names descriptive (`team-portrait-lead-hygienist-4x5.avif`).

## AI-generated images
- Allowed: abstract backgrounds, textures, patterns; conceptual editorial illustration in the site's illustration style; moodboards and labelled placeholders replaced before launch; cleaning or extending a real photo without changing facts.
- Never: staff, founders, "our team", customers, testimonial avatars, before/after or project results, premises, vehicles, food or products presented as real, clinical outcomes, anything resembling a real person or brand.
- The US FTC rule on reviews and testimonials (in force Oct 2024, verify) bans testimonials misrepresenting who gave them, including non-existent people. An AI face beside a quote is the client's legal risk.
- Label where a viewer could take it for a photo ("AI-generated illustration"); record tool and prompt; check commercial terms.
- If used: no close-up faces, strip generated text, inspect hands, teeth, reflections, repeating patterns; grade and add grain to match the library.

## When the client has no photos
1. Do not fill with stock people. Design the slot and label it in the mockup: `[needs: photo, crew on job, 4:5]`, `[needs: before/after, same angle, landscape]`.
2. Send the client the shot list above as a one-page checklist with orientation and use, plus the phone rules, within the first week (photos are the usual launch blocker).
3. Let product UI (annotated frames), typography at scale, real numbers and real documents (licence, certificate) carry the page until photos arrive.
4. Ship a layout that survives either way: image frames with a solid `surface-sunken` fill and fixed ratio, so a late swap causes no shift.
5. Budget a shoot in the proposal; list placeholder frames as open items in the handoff.

## Delivery (responsive images)
- Formats: photos AVIF with WebP then JPEG fallback; screenshots PNG or lossless WebP; logos, icons, illustration SVG; loops MP4 H.264 with a poster. Starting quality: AVIF 50 to 60, WebP 75 to 80, JPEG 75 to 82; compare at 100% zoom.
- Weight targets: hero 200 KB (mobile 120 KB), content image 100 KB, card 40 KB, avatar 15 KB, background loop 2 MB (10 to 15 s, 720p, no audio).
- Export at 2x the largest display width at most (full-bleed tops out near 2400 to 2560 px). `srcset` plus an honest `sizes`, or the browser fetches the wrong file.
- LCP (hero): real `<img>` (not a CSS background), `fetchpriority="high"`, never `loading="lazy"`, never faded in from opacity 0, art-directed `<picture>` with a 4:5 mobile crop. Everything below the fold: `loading="lazy" decoding="async"`. Targets: LCP 2.5 s, CLS 0.1.
- Alt text: purpose in one sentence; `alt=""` for decoration or when a caption already says it; verbatim for text in images; no "image of"; no keyword stuffing.
