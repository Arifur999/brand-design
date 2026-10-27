# Accessibility (WCAG 2.2 AA)

AA is the floor that laws and contracts cite. Design it in at the mockup stage: contrast, focus, targets, error states, headings. Native HTML first (`button`, `a[href]`, `label`, `select`, `details`, `dialog`); ARIA only for what HTML cannot express. Automated tools find only part of the problems; a keyboard and zoom pass by a person is part of done.

WCAG 2.2 added at A/AA: 2.4.11 Focus Not Obscured · 2.5.7 Dragging Movements · 2.5.8 Target Size (24 × 24 CSS px, or spacing so 24 px circles do not overlap; inline links and native controls exempt) · 3.2.6 Consistent Help · 3.3.7 Redundant Entry · 3.3.8 Accessible Authentication. Quick reference: w3.org/WAI/WCAG22/quickref.

## Design checklist (mockups, light and dark)
- **Colour:** body text 4.5:1; large text (24 px, or 18.66 px bold) 3:1; text over images at the worst point (use a scrim or panel); placeholders 4.5:1 if shown (better not to rely on them); button text 4.5:1 in every state; control boundaries (input borders, checkboxes, toggle tracks) and focus rings 3:1; meaningful icons and chart marks 3:1 or directly labelled; colour never the only cue (errors, status, required fields, links in text, chart series get an icon, text, underline or pattern). Links in body text underlined.
- **Type and reflow:** 200% zoom without loss; at 320 CSS px wide a single column without horizontal scroll (tables, maps and toolbars may scroll in their own container); text spacing override (line height 1.5, paragraph 2×, letters 0.12em, words 0.16em) survives, so no fixed-height text boxes; no images of text; body at least 16 px.
- **Focus:** visible on every interactive element (2 px ring, 2 px offset); sticky headers, CTA bars, cookie banners and chat widgets never fully cover the focused element (plan `scroll-padding`); focus order = visual order.
- **Targets and input:** 24 px minimum, 44 px default for touch (48 dp Android), 8 px gaps; every drag has a non-drag alternative (slider + number input, sortable list + move up/down, kanban + "Move to" menu, before/after slider + buttons); complex gestures have single-tap alternatives; no hover-only content; hover and focus popups are dismissible with Esc, hoverable and persistent.
- **Navigation and help:** consistent navigation order and naming, help in the same place on every page, at least two ways to find pages, a designed skip link, unique page titles, one h1 and no skipped heading levels.
- **Forms:** persistent visible labels; format hints before typing; required or optional stated in text; errors under the field with icon, border and a fix, plus a summary for long forms; fieldset and legend for radio and checkbox groups; no re-entering known data; legal, financial and data-changing submissions reversible, checked or confirmed; session timeouts warn and allow extension; authentication allows paste, password managers, show-password and passkeys, with no puzzle CAPTCHA lacking an alternative; one-time codes in one input (or segmented boxes that accept a full paste) with `autocomplete="one-time-code"`.
- **Content and media:** link text names the destination (no repeated "Read more"); alt text drafted with the copy; accurate captions (not raw auto-captions); transcripts for audio; no sensory-only instructions ("click the green button on the right").
- **Motion:** auto-moving content over 5 s needs pause, stop or hide (carousels, background video, tickers); nothing flashes more than 3 times per second; no autoplaying audio; a reduced-motion variant specified.

## Build checklist
- `lang` on the page and on foreign-language passages; unique titles updated on route changes; never `maximum-scale` or `user-scalable=no`.
- Real headings in order (size by class); landmarks (header, nav, exactly one main, footer) with all content inside one; distinct labels for multiple navs; skip link first; lists as lists; tables with header scope and caption; DOM order = visual order.
- Keyboard: everything operable, no traps (embedded maps, video, chat), no positive tabindex, `:focus-visible` styles (never `outline: none` without a replacement); modals move focus in, trap it, return it, close on Esc; menus and disclosures are buttons with `aria-expanded`; arrow keys inside composite widgets; focusing or changing a field never submits or navigates.
- Alt text: informative image = one sentence of what matters; decorative = `alt=""`; linked image = the destination; unlinked logo = the company name; chart = short summary plus a data table nearby; icon-only button = `aria-label` on the button with the icon hidden. Never "Image of"; under ~150 characters. Meaningful images are `<img>`, not CSS backgrounds.
- Forms: `label for`; the accessible name starts with the visible label (2.5.3); `aria-describedby` for hints and errors plus `aria-invalid`; status messages ("Saved", "3 results") via a polite live region; `autocomplete` tokens on personal data fields; never block paste.
- Names and roles: actions are buttons, navigation is links; no clickable divs; no empty links or buttons; states (`aria-expanded`, `aria-pressed`, `aria-current`) kept in sync; new-tab links say so.
- Sizes in `rem`; `min-height` rather than `height` on text containers; wide tables scroll in their own focusable wrapper; reduced motion removes parallax and large transitions (spinners stay).
- Third-party widgets (cookie banners, chat, booking, reviews, maps, payments) are part of the page: test them and offer an alternative route (phone, email, plain form).

## Testing procedure
1. Contrast of every pair in both themes, including hover, pressed, disabled, focus and text over photos (`scripts/color_tools.py audit`).
2. Automated scan with two engines when available (axe and WAVE catch different things), including after opening menus, dialogs and error states.
3. Keyboard pass from the address bar: skip link, logical order, focus never hidden, Enter, Space, arrows, Esc, focus return, forms and errors, pausing moving content.
4. 200% zoom, 320 px reflow, text-spacing override, phone landscape.
5. Screen reader spot check (VoiceOver, TalkBack or NVDA): headings, landmarks, alt text, control names, form and status announcements.
6. Reduced motion, captions, no flashing or sound.
Record page and state, issue, success criterion and level, severity (blocker, serious, moderate, minor). Launch rule: no blocker or serious issue on key templates. The most common failures on the web (WebAIM Million): low-contrast text, missing alt text, missing form labels, empty links, empty buttons, missing document language: fix them in the template layer.

## Legal context (not legal advice; checked October 2026, re-verify dates)
- **EU:** the European Accessibility Act applies since 28 June 2025 to e-commerce, consumer banking, e-books, electronic communications and passenger transport services, including non-EU businesses selling to EU consumers; microenterprises (fewer than 10 staff and ≤ €2m turnover) are exempt for services. EN 301 549 gives presumption of conformity; WCAG 2.2 AA covers it.
- **US:** ADA Title III applies to private businesses' websites (WCAG is the benchmark; lawsuits and demand letters are common, including against small businesses); the Title II rule for state and local government requires WCAG 2.1 AA with compliance dates in April 2027 and April 2028; Section 508 for federal work.
- **UK:** Equality Act 2010 (reasonable adjustments, WCAG AA as the benchmark); public sector regulations require WCAG 2.2 AA and an accessibility statement.
- Tell clients: design and build to WCAG 2.2 AA; accessibility is maintained, not finished; publish an accessibility statement with a working contact. Never sell or install overlay widgets as compliance (they cannot fix structure, they interfere with screen readers, and the US FTC fined one vendor $1M in January 2025).

## UX principles when they conflict
Precedence: accessibility → learned conventions (Jakob's law) → task speed and error prevention → persuasion. Laws predict direction, not guaranteed lifts.
Common misuses: "7 ± 2" does not set navigation length (menus are recognition, not recall; use card sorts and task data); Hick's law applies to weighed choices, not scanning ordered lists; the "3-click rule" has no research support (information scent matters); never fake incompleteness to exploit the Zeigarnik effect. Useful: Fitts (big, close targets for frequent actions), Tesler (move complexity into the system: autocomplete, detection, calculation), peak-end (design the confirmation page and the first email), Postel (accept any reasonable input format, normalise it), Doherty (respond within about 400 ms).
Research on a small budget: free signals (call recordings, reviews, site search logs) → one round of 5 remote tests on the top task → heuristic review and accessibility QA on every project → funnel analytics after launch. Five users per round per user group; heuristic reviews by 3 to 5 evaluators, severity 0 to 4.
