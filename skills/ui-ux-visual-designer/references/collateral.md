# Collateral: email, social, decks, print

Non-web deliverables agencies are asked for alongside sites and apps. Use the existing identity (tokens, type, imagery rules); logos, naming and brand guidelines belong to `brand-identity-designer`. Platform sizes change often: recheck before a paid campaign or a large print run (checked Oct 2026, verify).

| Format | Canvas | Hard rules |
|---|---|---|
| Email | 600 px wide, one column on mobile | Live text, 16 px body (14 px floor), tables, HTML under 102 KB |
| Instagram feed | 1080 x 1350 (4:5) or 1080 x 1440 (3:4) | Key content inside the 3:4 crop; text 40 px or more on canvas |
| Stories, Reels, TikTok | 1080 x 1920 | Top 14%, bottom 35%, sides 6% free of text and logos |
| LinkedIn | 1200 x 627 link; 1080 x 1350 portrait or carousel | One message per graphic |
| Deck | 1920 x 1080 | One idea per slide, 24 px minimum, sentence titles |
| Print | Trim size plus 3 mm bleed, CMYK, 300 ppi | Text 3 to 5 mm inside trim, vector text |

## HTML email
- **Layout:** 600 px content (560 to 640), `width:100%; max-width:600px`. One column for anything read on a phone; two columns only for product grids or footer links, stacking below 480 px. Template order: preheader, header (logo 120 to 200 px wide), hero (headline, one image, CTA), 1 to 3 blocks, secondary CTA, footer.
- **Tables:** classic Outlook for Windows renders with Word's engine and ignores much CSS layout. Nested tables with `role="presentation"`, fluid-hybrid columns, ghost tables for Outlook only where needed. New Outlook uses a browser engine, but classic stays in use with no published end date (verify).
- **Gmail clipping:** keep HTML under 102 KB or the rest hides behind "View entire message". Images do not count; conditional code and inlined styles are the usual cause.
- **Type:** body 16 px at 1.5; headline 24 to 32 px (22 px floor on mobile); button label 16 to 18 px semibold; 14 px only for footer and fine print. Contrast 4.5:1 for all text including footer.
- **Fonts:** always a full stack (`'Brand Sans', Arial, Helvetica, sans-serif`) and design for the fallback. Classic Outlook may show Times New Roman when a web font is first, so declare the web font only inside a media query or non-Outlook conditional.
- **Bulletproof buttons:** a table cell with background colour and padding, a link inside, 44 px tall minimum, full width on mobile. Rounded corners need VML for classic Outlook; otherwise accept square corners there rather than an image button. One primary CTA, a text link for the secondary.
- **Live text:** headlines, body and buttons are HTML. Images at 2x pixels with `width` set in HTML, under 100 KB each where possible.
- **Image blocking and alt text:** many clients block images until allowed. Every image has `alt`, styled (font, colour on the `img` tag) so blocked images stay readable; the email must still make sense, and the CTA still work, with images off.
- **Dark mode** (clients: no change, partial inversion, full inversion; design for all three):
  - `<meta name="color-scheme" content="light dark">` plus `@media (prefers-color-scheme: dark)` for clients that honour it (Apple Mail).
  - Logos as transparent PNG with a light outline or padding, or swap a light logo in the dark query.
  - Off-black on off-white (#1C1A17 on #FFFFFF-ish) inverts more gracefully than #000 on #FFF.
  - No text baked into images over backgrounds that may invert.
  - Test Apple Mail, Gmail (web, iOS, Android), Outlook (classic, new, Outlook.com), one Android client, light and dark.
- **Accessibility and compliance:** `lang` on `<html>`, real `<h1>`/`<h2>`, descriptive link text ("View your invoice", not "Click here"), preheader 40 to 90 characters that adds to the subject. Marketing email needs an unsubscribe link and the sender's postal address (US CAN-SPAM; check the audience's region).

## Social graphics
| Platform | Placement | Size | Notes |
|---|---|---|---|
| Instagram | Feed | 1080 x 1350 (4:5) | 3:4 (1080 x 1440) supported; grid previews at 3:4 so a 4:5 post loses about 34 px per side (verify) |
| Instagram | Story, Reel | 1080 x 1920 | Reel cover grid crop is 3:4 centre: loses 240 px top and bottom |
| Facebook | Page cover | Upload 851 x 315 | Sides crop on mobile: keep text in the centre 640 px; profile photo covers bottom-left |
| LinkedIn | Link / landscape | 1200 x 627 | Also link preview |
| LinkedIn | Portrait, carousel page | 1080 x 1350 | Same size on every page |
| LinkedIn | Personal banner / company cover | 1584 x 396 / 1128 x 191 | Profile photo overlaps bottom-left |
| X | Image / header | 1600 x 900 / 1500 x 500 | Header avatar overlaps bottom-left on mobile |
| YouTube | Thumbnail | 1280 x 720 | Duration stamp covers bottom-right; test at 320 px wide |
| YouTube | Channel banner | 2560 x 1440 | Text inside centred 1546 x 423 |
| TikTok | Video | 1080 x 1920 | Keep right 120 to 150 px and the caption area clear |
| Web share | Open Graph | 1200 x 630 | Message central; some apps crop to square |

- **Vertical safe zone (1080 x 1920):** top 0 to 270 px (profile, progress bar), bottom 1250 to 1920 (caption, reply bar, CTA), sides 65 px. Usable centre about 950 x 980. Ads with disclaimers need the bottom 40% clear.
- **Legibility at phone scale:** a 1080 px graphic shows at about 360 to 430 CSS px, a third of its size. For 14 px on screen use 40 px or more on canvas; headlines 72 to 120 px; margins 64 to 80 px.
- Headline 8 words or fewer, one message per graphic, body copy goes in the caption. Contrast 4.5:1; over photos a 60% scrim or solid panel (`imagery.md`).
- Logo small (60 to 100 px tall), same corner every post, not on every carousel slide. Carousel: slide 1 is the hook in 6 to 8 words, one point per slide, last slide the CTA, same grid and a "1/7" cue.
- Do not reuse one 1080 x 1080 for every placement. Add alt text where allowed; the only copy of key information never lives only in the image.

## Presentation decks
- **Canvas:** 1920 x 1080 (13.333 x 7.5 in); 4:3 only if the projector demands. Margins 96 px (80 to 120); 12 columns, 32 px gutters; title in the same top-left spot on every content slide.
- **Sizes at 1920 x 1080:** cover title 72 to 96; slide title 44 to 56 (a full sentence, 2 lines); key number 96 to 200 (one per slide); body 28 to 36; **24 px minimum for anything the audience must read**, chart labels and table cells included; sources 18 to 20 (the only exception). Two weights, none thin (projectors wash them out).
- **Titles state the takeaway:** "Repeat bookings doubled after the reminder emails", not "Booking data".
- **Words:** presented slide about 30 words of body at most, one idea, one visual; send-ahead deck up to about 75 words; bullets 3 to 5, one line each. Eight bullets means two slides. Detail goes to speaker notes or appendix.
- **Charts:** one per slide; title says what it proves; highlight the one series in `primary`, mute the rest to grey; label directly, drop the legend and heavy gridlines; bars start at zero; no 3D, no pie over 5 slices, no dual axes; tables 6 rows by 5 columns at most, numbers right-aligned; source line bottom-left on every data slide.
- **Contrast and motion:** 4.5:1 minimum, aim 7:1 for body (projectors lose contrast). One primary mode per deck (dark for dark rooms and video, light for bright rooms and print). Transitions none or a quick fade.
- Slide types to design once: cover, agenda (decks over 15 slides only), divider, big statement, key number, chart, comparison, process (3 to 5 steps), quote with photo, full-bleed image, team, timeline, options, next steps, appendix.
- Export PDF to send (fonts embedded, links live), PPTX to edit; use fonts available in Google Slides if the client will edit there, else supply the files (never Fontshare files, see `typography.md`).

## Print basics
- **Colour:** CMYK through the profile the printer names (FOGRA in Europe, GRACoL in the US are common), never a blind RGB-to-CMYK. Bright RGB oranges, greens and blues shift: check brand colours on a hard proof. Spot (Pantone) when the logo colour must match exactly.
- **Resolution:** 300 ppi at final printed size; large format viewed from afar 100 to 150 ppi. Logos and text stay vector (a 72 ppi web logo on a banner is the classic failure).
- **Bleed:** 3 mm past trim on every side (US 0.125 in). **Safe area:** text and logos 3 to 5 mm inside trim on small items, 10 mm or more on posters and brochures. Poster bleed is often 5 mm: ask.
- **Black:** small text 100% K only. Large solid areas in rich black (for example C60 M40 Y40 K100) within the printer's total ink limit. Hairlines 0.25 pt minimum.
- **Delivery:** press-ready PDF/X-1a or PDF/X-4 as the printer requests, fonts embedded or outlined, crop marks and bleed included.
- HTML exports are RGB: treat as layouts and proofs. Set `@page { size: 91mm 61mm; }` (EU card with bleed), export PDF, then convert and preflight in a print tool or let the printer convert after you approve a proof.

| Item | Trim | With 3 mm bleed |
|---|---|---|
| Business card EU / US | 85 x 55 mm / 3.5 x 2 in | 91 x 61 mm / 3.75 x 2.25 in |
| A4 / A5 flyer | 210 x 297 / 148 x 210 mm | 216 x 303 / 154 x 216 mm |
| DL | 99 x 210 mm | 105 x 216 mm |
| Roll-up banner | 850 x 2000 mm typical | Printer template; keep bottom 100 to 150 mm free |

- Print type: card name 9 to 11 pt, card details 7 to 8 pt (never under 6), flyer body 9 to 12 pt, flyer headline 24 to 48 pt, legal 6 to 7 pt minimum.
- Signage: 1 inch of letter height per 10 feet of viewing distance (about 25 mm per 3 m); moving traffic 3 to 6 words. Sturdy sans, medium to bold, strong contrast, no text over photos; print one section at full size and check from the real distance. US public-facility signs fall under ADA rules (tactile characters, Braille, mounting height).

## What to request from the client before starting
- Email: sending platform (Mailchimp, Klaviyo, other: it limits dark-mode and VML support), list size and region (compliance), sender name, postal address, the ESP's merge-tag syntax.
- Social: which platforms are actually posted to, the logo as SVG and PNG on transparent, brand fonts with licences that allow design-tool use, who approves posts.
- Deck: where it is presented (room, projector, video call) and whether it is read without a presenter; the editing tool (PowerPoint, Keynote, Google Slides) decides font and effect limits.
- Print: the printer's name and their template, paper stock, finish, quantity, profile (FOGRA or GRACoL), PDF/X version. Ask for a hard proof on any run over a few hundred pieces.

## Pitfalls to check before delivery
- Image-only emails, or CTAs that are pictures of buttons; tested in one client and one theme only.
- Social graphics with paragraph text, or headlines in the bottom third of a Reel.
- Deck titles that name the topic ("Overview", "Results", "Next steps") instead of the point; 14 px chart labels on a projected slide.
- Print files in RGB, without bleed, or with text 1 mm from the trim; web-resolution logos on large formats.
- Signs designed on a laptop and never checked at real size and distance.
- Fonts that are not licensed for embedding in PDFs or for the client's editing tool.

## Acceptance checklist
- [ ] Email: under 102 KB, tested in 6 clients in light and dark, readable with images off, one CTA of 44 px, unsubscribe and address present.
- [ ] Social: each placement has its own export at the exact size, text clear of safe zones, readable at 320 px wide.
- [ ] Deck: no text under 24 px except sources, every title a sentence, each chart has a source line and one highlighted series, PDF and PPTX both exported.
- [ ] Print: CMYK via the printer's profile, 3 mm bleed, safe margin respected, 300 ppi, fonts outlined or embedded, PDF/X as requested, proof approved in writing.
