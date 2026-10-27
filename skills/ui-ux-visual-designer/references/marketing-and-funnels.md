# Marketing sites, landing pages and funnels

## Before layout: the page brief
- One page: business in one sentence · ONE primary audience · their trigger (what just happened) · alternatives (including doing nothing) · 2 to 4 unique attributes · value and proof · category frame · ONE primary action and one softer secondary · top 5 objections · voice (3 adjectives + 1 never). The category frame changes the page ("family dentistry" versus "sedation dentistry for anxious adults").
- Message stack for the hero and every major section: headline = outcome → subhead = how and for whom → one concrete proof → CTA (verb + object) with a risk-reducer line.
- Five-second test: what is it, who is it for, what would you click. If 2 of 3 testers fail, rewrite the hero first.
- Objections drive sections: each is answered at a nameable place (a section, a proof, an FAQ entry, microcopy by the button). Mine the wording from reviews of the top 3 competitors.
- Evidence worth knowing: grade 5 to 7 copy converted at roughly double college-level copy in Unbounce's dataset; 57% of viewing time is above the fold and 74% in the first two screens (NN/g 2018); most people scan.
- Paid traffic: the headline echoes the ad's words (message match); one page per ad group or audience.

## Rhythm and spacing
- Section padding: desktop 96, tablet 80, mobile 64; compact bands (logos, stats) 48 to 64. Hero top 80 to 128 desktop, 48 to 64 mobile. Heading to subhead 16, subhead to CTA 32 (24 mobile). Card gap 24 to 32. Section header text 640 to 720 wide.
- The gap between sections is at least 1.5x the largest gap inside them. Two adjacent sections on the same surface must not stack two full paddings (192 px reads as the end of the page): reduce one or add a divider.
- Surfaces: tint groups related sections (no zebra striping); at most 2 inverse bands per page; a primary-filled band only for the closing CTA; two different tints never touch.
- One filled primary button per viewport (the nav and hero may share the same action). One label per action across the whole page.
- Pacing: screens 1 to 2 hook and quick proof; 2 to 4 relevance; middle builds belief; late sections decide (pricing, comparison, FAQ); end on action. Never more than 2 text-heavy sections in a row. A CTA every 2 to 3 sections. Read the h2s alone: they should tell the story.
- Section counts: single-goal landing page 5 to 9; homepage 7 to 12; long sales page 12 to 18 (high-consideration offers only).
- Above-the-fold check at 1280 × 720 and 390 × 844: the headline passes the five-second test; one CTA visible on mobile; a trust cue in or just under the first viewport; a real visual; nav = logo + up to 7 items + CTA; no auto carousel; the next section peeks into view.

## Hero
- Headline 6 to 12 words (under ~70 characters), 60 to 64 px desktop (72 only for 6 words or fewer), 36 to 44 mobile. Subhead 15 to 30 words, 560 to 640 px wide. CTA 2 to 4 words, verb first, 48 to 56 px tall on mobile, trust line under it. Height comes from content, never forced 100vh. The hero image is the LCP element: never lazy, high fetch priority, explicit dimensions.
- Specific beats clever: "Same-week AC repair in Austin" beats "Comfort, reimagined".
- Pick a hero type by job: **split text + image** (default; 6/6 or 5/7) · **centred statement** (brand-led; do not carry centring down the page) · **full-bleed photo or video** (hospitality, real estate; scrim at least 60% behind text; muted looping video with poster and a visible pause) · **product UI showcase** (crop the UI on mobile, never shrink a 1440 px dashboard; realistic numbers) · **form in hero** (paid traffic and quotes; up to 5 fields; multi-step starts with the easiest question, contact details last) · **search-led** (56 to 64 px input) · **editorial type** (96 to 160 px, line height 0.95 to 1.05, plain subhead) · **interactive 3D** (poster first, lazy start, static under reduced motion, keyboard alternative) · **local trust stack** (service + area headline, rating with source and count, licensed and insured, phone as secondary, real team photo).

## Sections that matter (specs)
- **Navigation:** 64 to 72 px desktop, 56 to 64 mobile; 4 to 7 plain-noun items; current page marked by more than colour; CTA far right; test the 1024 to 1280 px wrap. Mega menus only for 3+ categories with 5+ children each, opened by click or with a 150 to 300 ms hover-intent delay; close with Esc, outside click and focus-out. Sticky headers may shrink after 80 to 120 px of scroll and hide on scroll-down; set `scroll-padding-top` so focus is never hidden (WCAG 2.4.11). All sticky elements together under 15% of a phone screen. Mobile drawer: the word "Menu" beside the icon, 48 px rows, CTA pinned at the bottom, focus trapped. Never a header CTA and a bottom bar for the same action. Patterns by type: navbar.gallery.
- **Logo cloud:** 5 to 8 logos, 24 to 40 px high, monochrome, a specific label ("Used by 1,200 dental practices"); skip it with fewer than 4 recognisable logos; never invent logos.
- **Problem:** only for considered purchases; at most 3 pains in customers' words with concrete consequences; skip for urgent intent.
- **Features:** benefit-first titles of 3 to 6 words. Layouts: grid (3, 6 or 9 items, no orphan, cards only when clickable), zigzag (max 4 rows, text before media on mobile), bento (4 to 7 tiles, one hero tile, one idea per tile, real content in every tile), tabs (3 to 5, no auto-advance), sticky scroll (off on mobile).
- **How it works:** 3 to 4 verb-led steps with timing ("Day 1"); step 1 is the customer's small effort; CTA after.
- **Stats:** 3 to 4 verifiable numbers with unit, context and timeframe; never 5+; never invented.
- **Testimonials:** real name, role, company or location, photo, a specific result, 15 to 50 words, a date. Quote wall, single hero quote, or video with captions. No auto-advancing carousels. Self-serving review stars on your own site get no rich results; fake or AI-generated testimonials are illegal under the US FTC rule (October 2024).
- **Pricing:** show prices. 3 tiers by default (2 to 4), named by audience; "Most popular" only if true; the CTA above the feature list so buttons align; 5 to 8 features ("Everything in Team, plus"); billing toggle defaults to the period you want to sell with the exact saving; comparison table with sticky header and first column and text labels on icons. "Starting at" pricing explains what is included, 3 to 5 price factors and a typical range. Hidden fees at checkout are a leading cause of abandonment (Baymard).
- **FAQ:** 6 to 10 questions ordered price, timing, risk, process, fit; the first sentence of each answer is the direct answer; native disclosure elements; several may be open at once. Do not design for FAQ rich results (Google has restricted them).
- **Before/after:** same crop, angle and light; a native range input with a 44 px handle; caption with location and scope.
- **Comparison with alternatives:** 6 to 10 buyer criteria with concrete values, concede one thing the alternative does better, date and sources (accuracy is a legal exposure).
- **Closing CTA band:** h2 of 8 words or fewer, the same action as the hero, no competing CTA directly below.
- **Contact:** a response promise, 3 to 5 single-column fields, success replaces the form with the next step and timeline; a honeypot rather than a puzzle CAPTCHA; address as text; mobile shows channels first (48 px call button).
- **Footer:** targets at least 24 px (44 px rows on mobile); local name, address and phone must match the Google Business Profile exactly; no stale years or dead social links. Patterns: footer.design.
- **Cookie banner:** Reject as prominent as Accept; nothing pre-ticked; never covers the hero CTA or focused elements; overlays rather than pushes content.
- **404:** a real 404 status, search plus 3 to 5 useful links, written in the brand voice.

## Page blueprints (write the goal and CTA label first, then cut from the stack)
- **Product or SaaS homepage (8 to 12):** nav with CTA → hero (UI showcase or statement) → logo cloud → problem (new categories only) → features → deep dive → quote or case teaser → integrations → pricing teaser → closing CTA → footer. Self-serve versus sales-led: one is primary, the other a text link.
- **Local service homepage (8 to 11):** nav with phone (sticky call or book bar on mobile) → trust-stack hero → rating badges → services (each with its own page) → 3 to 4 concrete promises ("Arrival window texted 30 minutes ahead" beats "Reliable service") → how it works with timing → before/after → reviews with name, suburb and service → service areas → owner → FAQ → CTA with phone → footer with NAP. Licence and insurance in the hero, not only the footer.
- **Paid landing page (6 to 10):** minimal header without nav → hero echoing the ad (often with the form) → trust strip → 3 benefits tied to the ad angle → how it works → testimonials from the same segment → objection FAQ (5 to 7) → repeat CTA → minimal footer. Every exit is a leak; defer chat widgets.
- **Service detail:** h1 = the search name, included and excluded list, process, price factors or range, service-specific proof and FAQ, related services.
- **E-commerce product page:** gallery (5 to 8 images including scale) beside a sticky buy box (rating, price, option buttons up to ~8, unavailable options greyed with a reason, delivery date, returns line); benefits; specs; reviews with distribution and photos; mobile sticky add-to-cart; add-to-cart opens a mini cart rather than redirecting.
- **Pricing page:** tiers visible in the first desktop viewport, the billing unit explicit, the plan most customers should pick highlighted (not the most expensive), pricing FAQ (billing, refunds, changes, tax).
- **About:** a 150 to 300 word origin story with a specific moment, values as behaviours ("We reply within one business day"), verifiable milestones, team with consistent photo crops, a CTA at the end.
- **Case study:** outcome and metric headline, a 10-second summary box, challenge, approach, results with baseline and timeframe, quote, written client approval.
- **Portfolio:** 9 to 15 projects, leading with the work that matches the clients wanted next; each links to a context page.

## Funnels (multi-step journeys)
- Map the funnel before designing pages: traffic source → landing or opt-in → thank-you → nurture (email) → sales page → checkout → confirmation → upsell or onboarding. Write the one job and the one metric for each step.
- **Opt-in page:** one offer, one field (email) or as few as possible, the deliverable shown (cover, preview, outline), what happens next.
- **Thank-you page:** confirm, say exactly what arrives where and when, offer the one next step (a booking, a low-cost offer, a share); it is also where conversion tracking fires.
- **Sales page:** long only when the price and risk justify it; the objection list is the outline; proof next to every claim; the same CTA repeated at natural decision points; guarantee and risk-reversal near the price.
- **Checkout:** no navigation, a summary with the total (no surprises), guest checkout, the fewest fields, trust signals at payment, inline validation, clear errors that keep input.
- **Upsells and order bumps:** one relevant offer at a time, a clear and equally visible "No thanks" with neutral wording (no confirmshaming), never pre-ticked.
- **Webinar and waitlist:** the viewer's local time and add-to-calendar; name and email only; no fake scarcity or fake counts.
- Keep the visual and verbal thread consistent across steps so people know they are in the same place; show progress in multi-step forms.
- Honest urgency only (a real deadline, capacity or season). Banned dark patterns: confirmshaming, roach motels, sneaking items into the basket, hidden costs, forced continuity, disguised ads, trick questions, pre-ticked consent, nagging, fake social proof (several are illegal in the EU, UK and US).

## Conversion and trust
- CTA labels: verb + outcome, never "Submit", "Click here" or "Learn more" alone; the confirmation echoes the label ("Estimate booked"). Neutral labels inside apps.
- Proof ladder, strongest first: named result with numbers and person → platform-sourced reviews with recency ("4.9 on Google, 312 reviews, latest 3 days ago") → permitted client logos → volume numbers → certifications and licences → media mentions → anonymous initials (avoid).
- Trust by business type: B2B (logos, metric case studies, compliance badges only if held, status page) · e-commerce (price and delivery before checkout, returns near add-to-cart, photo reviews) · local (phone in header, licence and insurance, service area, rating, response promise) · healthcare (clinician names and credentials, insurance, emergency guidance) · finance and legal (registration numbers, plain fees) · nonprofit (where the money goes) · hospitality (real photos, price per night, cancellation policy).
- Forms: single column, labels above, steps of 3 to 6 fields easiest first, mark "(optional)", never clear input on error, say who responds and when, ask for a phone number only if you will call.
- Mobile: sticky bottom CTA bar 56 to 64 px plus the safe-area inset, `tel:` links, numeric keyboards, no full-screen entry interstitials.
- Test the big things (offer, headline, form length, structure), not button colours; with low traffic, use 5-person sessions or five-second tests.

## Copy rules
- Sentence case, front-loaded meaning, one term per concept, grade 6 to 8 reading level.
- Banned filler: seamless, robust, cutting-edge, next-generation, revolutionise, leverage, empower, unlock, elevate, world-class, best-in-class, one-stop shop, "in today's fast-paced world".
- Before and after: "Elevate your business with cutting-edge solutions" → "Send invoices in 30 seconds and get paid 9 days sooner"; "Learn more" → "See 40 finished pool builds"; "Trusted by thousands" → "4.9 from 612 Google reviews".
- Headline formulas (vary across pages): outcome + timeframe · outcome for an audience · the problem named in the customer's words · an objection removed.
- Placeholders are plausible, specific drafts marked `[needs: client confirmation]`, never lorem, Acme or invented proof.

## SEO and performance that design must support
One h1 with the key phrase; heading levels by structure, not size; one page per service and per area with unique content; descriptive link text; alt text; structured data matching visible content (the most specific LocalBusiness subtype for local firms). Core Web Vitals at the 75th percentile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Budgets: hero image under ~150 KB (AVIF or WebP), at most 2 font families, no third-party scripts above the fold, explicit dimensions on all media, reveal animations on transform and opacity only.
