# Discovery and briefing

Read everything already supplied before asking. Ask only what changes the design, in one message, with your recommended answer first. If nobody can answer, assume, label the assumption, and continue.

## Question bank (pick the decisive few)
**All projects**
- Who is the primary audience, in what situation and on what device? What are they trying to get done, and what worries them?
- What is the one action that matters most, and how will success be measured (a number)?
- What exists already: brand guidelines, logo, fonts, colours, component library, a live site or app, analytics, real content and photos?
- What is in scope: pages, screens, flows, platforms, deadline?
- Two or three sites or apps you like (and what exactly), and anything you dislike?
- Technical constraints: stack or builder (Next.js, Webflow, WordPress/Elementor, Wix, Shopify, iOS, Android, Flutter), CMS, integrations?
- Who approves, and do they need to see options?

**Marketing site, landing page, funnel:** traffic source and the ad or message it follows; the offer and price; top objections; proof available (reviews with sources, results, licences, logos with permission); local or national; languages.
**Web app or SaaS:** user roles and what each may see; the top 3 tasks by frequency; data volumes (0, typical, extreme); onboarding goal (the first-value moment); existing screens to stay consistent with.
**Dashboard:** who uses it and how often; the 3 to 5 questions it must answer; metric definitions, sources, refresh rate, time zone; actions people take from it.
**Mobile app:** platforms and minimum OS versions; native or cross-platform; offline needs; notifications; device features (camera, location); store listing needs.
**Redesign:** what works today (keep it), what fails (evidence: analytics, complaints, support tickets), what must not change for existing users.

## Ask for materials when they would change the result
- Screenshots or a recording of the current product, especially states that are hard to reach.
- URLs of competitor or reference sites, with one sentence on what to take from each.
- Brand guidelines, logo files (SVG), font licences, photography.
- Real copy, real data samples (anonymised), the longest realistic names and values.
- Analytics or research findings, support tickets, reviews.
Say why you want each one ("so the dashboard handles your real account names, which run to 60 characters").

## Decide without asking
Spacing and type scales, grid, breakpoints, icon set, component patterns, state coverage, accessibility level (AA minimum), motion level for the project type, how many directions to show (2 to 3 only when taste decides). State these decisions; don't ask permission for them.

## One-page brief
```
Project: <type, pages/screens, platform>
Audience: <who> who <trigger> and want <outcome>, but worry about <barrier>
Primary action: <verb + object>   Success measure: <number>
Secondary action: <softer path>
Objections (top 5) → where each is answered
Proof available: <real items only>
Voice: <3 adjectives> · never <1>
Constraints: <stack, brand guidelines, content, legal, performance, languages>
Assumptions (to confirm): A1 ..., A2 ...
```

## Direction plan (after the brief)
```
Direction: <name>  · Idea: <one sentence from the business itself>
Adjectives: <3> · never: <1>
Palette: <4 to 6 named roles with values>
Type: <display / text / data, licences>
Layout: <grid idea, ASCII wireframe at 375 and 1280>
Shape and depth: <radius, borders or shadows>
Imagery: <real photos / product UI / illustration, treatment>
Motion: level <0 to 4>, the one orchestrated moment
Signature element: <what it is and the job it does>
Generic check: what I changed because it was generic
```

## Feedback and change control
- Classify every piece of feedback: **fix** (it is wrong against the brief: do it), **change** (a preference within scope: do it within the agreed rounds), **new scope** (a new page, feature or direction: say so and estimate before doing it).
- Ask for problems, not solutions ("what feels wrong for your customers?"), and tie questions to the brief's adjectives. "I don't like the colour" can mean a personal association, a competitor resemblance or an audience mismatch: find out which before changing anything.
- Two revision rounds per phase is normal; a third usually means the brief was unclear: go back to it.
- Approve structure before visuals and the key screen before the rest; feedback on colour while structure is open wastes rounds.

## Common failure modes and their corrections
| Failure | Correction |
|---|---|
| Generic SaaS look | derive the direction from the client's real materials; one signature element |
| Invented proof | design the slot, label `[needs: ...]` |
| Everything centred | left-align section headers and body; centre only a short closing CTA |
| Five weights, three accents | 2 to 3 weights, one accent |
| Grey text on colour | tint toward the background hue or use the on-colour token |
| 100vh hero hiding the CTA | height from content; CTA in the first mobile viewport |
| Desktop-only design | design 375 first for the key screen |
| Only the happy state | design empty, loading, error and permission states |
| Redrawn or recoloured client logo | use the client's files untouched |
| Drift from the system on later pages | add the new style to the system or remove it |
