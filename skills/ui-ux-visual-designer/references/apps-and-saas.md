# Web apps and SaaS products

Target feel for working software: calm and dense, closer to Linear or Stripe than to a marketing page. Chrome stays neutral; the brand shows in the primary action, focus ring, charts and logo. Design the screens in this order: main list or table (it sets density and the toolbar) → record detail → home dashboard → create/edit form → settings and billing → onboarding and first-run empty states → auth → notifications, search, errors and 404.

## Baseline numbers
Control heights 32 compact, 40 default desktop, 44 to 48 touch · body 16/24 for reading, 14/20 for dense UI · page padding 24 to 32 desktop, 16 mobile · card padding 20 to 24 · related controls 8 to 12 apart, groups 24 to 32 · content max 1440 for dashboards, 720 for forms and settings, 680 to 760 for chat and reading · response limits: 0.1 s feels instant, 1 s keeps flow, 10 s loses attention.
Density: comfortable (row 48, control 36, text 14) by default; compact (row 36, control 32, text 13) only for data tables, never on touch screens. Get density by removing decoration (borders, shadows, padding) before shrinking text.

## Shell and navigation
- Pick one primary pattern: top bar (4 to 7 items, wide content) · sidebar (5 to 15 items in labelled groups; full at wide screens, icon rail at medium, drawer below) · bottom tabs (3 to 5, mobile only) · a command palette only as a supplement.
- Sidebar: 240 to 280 expanded, 64 to 72 as a rail (persist the state); workspace switcher, search and "New" on top; main nav; groups; help, settings and user pinned at the bottom. Items 32 to 40 tall, icons 16 to 20, active item marked by background and `aria-current`, at most 2 nesting levels; rail icons get tooltips on hover and focus. More than 12 items means the IA needs a second level, not a longer list. Hide what the role can never open.
- Top bar about 56 tall: sidebar toggle, breadcrumb (only 3+ levels deep, last crumb unlinked), search, notifications, theme, user menu. Page actions live in the page header: h1, one muted sentence, at most one primary action.
- Tabs for sibling views of one object, with the active tab in the URL.
- Command palette (Ctrl/Cmd+K, shortcut shown in the search field): 560 to 640 wide, near the top, groups for recent, pages, actions and people; Enter runs, Esc closes; destructive commands still confirm.
- Multi-tenant and role-aware: org switcher at the top; destructive confirmations name the org ("Delete 12 products from Dhaka Branch?"); one permission table drives routes, navigation and visible actions; "view as" shows a persistent banner with Exit; plan-gated features show an upgrade note or are hidden, never a button that errors after the click; read-only with a one-line reason ("Only owners can change billing") beats unexplained disabled controls.
- Avoid: sidebar + top tabs + bottom tabs for the same level; icon-only navigation; navigation that reorders itself; a hamburger on desktop hiding fewer than 7 items.

## Onboarding
- The goal is time to first value: define that moment first, then remove everything between sign-up and it. Defer invites, photos, billing and integrations.
- Combine an empty-state-led start with a checklist of 3 to 6 verb-led tasks (time estimate, deep link, self-checking, "2 of 5" progress, first item pre-completed, dismissible, removed when done). A welcome survey of 1 to 3 questions only if the answers visibly personalise, with Skip. Sample data clearly labelled and removable in one click.
- Coachmarks one at a time, triggered by context, never shown again after dismissal. Skip tutorial carousels.

## Authentication
- Card 400 to 440 wide; inputs 44 to 48 with labels above. Sign-up: email + password or email only; no confirm-password field (offer show-password); up to 3 equal social buttons ("Continue with Google"); terms as a line under the button; marketing consent separate and unchecked; land in the product, or on a verification screen that shows the address, Resend with a cooldown and Change email.
- Sign-in: identifier first (routes SSO and passkeys); correct `autocomplete` tokens (`email`, `current-password`, `new-password`, `one-time-code`); "Forgot password?" visible before an error; generic failure message; never clear the email; throttle with growing delays rather than permanent lockout.
- One-time codes: numeric input with `autocomplete="one-time-code"` (or boxes that accept a full paste), auto-submit on the last digit; magic links single-use and expiring in 10 to 15 minutes, with a code in the same email.
- Passwords (NIST SP 800-63B rev 4): minimum 15 characters when it is the only factor (8 with MFA), allow at least 64, no composition rules, no forced periodic change, block common and breached passwords with an explanation, allow paste and password managers. Puzzle CAPTCHAs without an alternative fail WCAG 3.3.8.
- Offer passkeys after a successful sign-in; MFA by authenticator or passkey before SMS; recovery codes with copy and download.

## Forms
- Single column; short related pairs may share a row (city and postcode, expiry and CVC). Labels above, never placeholder-as-label, no floating labels. Width hints the answer (postcode short, email medium). Field gap 20 to 24; groups as fieldsets with 32 above. Form width 400 to 560.
- Input types: phone, card and codes as `type="text" inputmode="numeric"` (not `number`); 16 px text on mobile; `enterkeyhint`; no spellcheck on codes and emails. Fewer than 5 options: radios; 5 to 15: select; more: searchable combobox. Known dates (birth) as three fields; chosen dates as a picker plus typed input. No Reset button.
- **Validation (default):** validate required fields on submit; validate format fields when the user leaves a field they have typed in; once an error shows, re-check as they type so it clears immediately. Live feedback while typing only for password rules, counters and availability checks (debounced 300 to 500 ms). On submit, focus the first invalid field (short forms) or an error summary linking to fields (3+ errors). Map server errors to fields; general errors in an inline alert, never only a toast. Never disable the submit button to signal invalid input (it cannot explain why); disable it only while submitting, with a spinner and the label kept.
- Error text: what happened and how to fix it, under the field, with an icon, linked by `aria-describedby`, never blaming, input kept ("Enter an email address like name@example.com").
- Multi-step after about 8 fields or with branching: 3 to 5 steps, one topic each, named progress ("Step 2 of 4: Property details"), easy questions first and payment last, Back keeps answers, autosave long forms, a review step with Change links, never ask for the same information twice (WCAG 3.3.7).
- Buttons: Cancel then primary, right-aligned on desktop; stacked full-width with primary on top on mobile; labels are verb + object ("Save changes", "Create invoice").

## Search and filters
- A visible search field when search is primary (240 to 480 wide); on focus show recent searches and suggestions; suggestions after 1 to 2 characters, debounced 150 to 300 ms. Results keep the query, show a count, tolerate typos; zero results echo the query and suggest corrections or a way to get help.
- Facets: a left column on desktop (or a dropdown bar for 5 filters or fewer); on mobile a "Filters (n)" sheet with a live "Show 128 results" button; OR within a facet, AND across facets; counts next to values; 5 to 7 values then "Show all"; ranges as slider plus two number inputs; applied filters as chips with Clear all; query, filters, sort and page in the URL so Back works.

## States (every view has all of them, each reachable for review)
| State | Shows |
|---|---|
| First load | skeleton in the final layout's shape (nothing under 300 ms; skeleton 1 to 10 s; over 10 s determinate progress, Cancel, run in background) |
| Refetch | real data + a thin progress indicator |
| Empty, first use | what will appear here + the one action (or who can do it) |
| Empty, filtered or no results | which filter or query caused it + Clear filters |
| Cleared | a brief positive message, no CTA ("All caught up") |
| Error | plain sentence + Retry, the rest of the page still works; page-level errors give cause, action, support link and a copyable reference ID |
| Offline | persistent banner, queued actions marked pending, confirmed when synced |
| No permission | who can grant access + Request access, or read-only with a reason |
| Success | a short past-tense confirmation, Undo when reversible |
Optimistic UI for likes, renames, toggles and reorders, with rollback and Retry. An endless spinner is an undesigned error: after 10 to 15 s say "taking longer than usual" and offer Retry. Never flash "No data" before the first fetch ends.

## Overlays and messages
- Choose the container: own URL, shareable, or more than a few minutes of work → page; keep the list visible → side sheet or drawer (record views get `?view=<id>`); a brief decision → modal; a small choice on a control → popover; on mobile options → bottom sheet.
- Modals: 400 / 560 / 720 wide, up to about 6 fields, max height 85vh with fixed header and footer; focus trapped and returned; never a modal on a modal; closing a dirty form asks before discarding; clicking outside never discards typed work; no modals on page load.
- Confirmation only for irreversible actions: the title names the object ("Delete 'Q3 report'?"), the body states the consequence, buttons name the action ("Delete report" / "Cancel"), default focus on Cancel; type-the-name for workspace-level destruction. Reversible actions happen immediately with Undo in a toast (8 to 10 s).
- Toasts confirm the user's own action: 3 to 6 words, past tense, one position for the whole product, 360 to 420 wide, at most 3 stacked, one action at most, timer paused on hover and focus, `role="status"`. Errors that need action never auto-dismiss and never appear only in a toast; validation never uses toasts.
- Inline alerts for anything the user must read; banners for account-wide state (trial ending, payment failed, offline).
- Notification centre: bell with a capped badge ("9+"), grouped by day, "Actor action object" sentences, deep links that mark as read, Mark all read; a preference matrix of events × channels with digests; defaults on only for events about the user.

## Settings
Personal (profile, security, notifications, preferences) separate from workspace (general, members, billing, integrations, API). Desktop: left sub-navigation 200 to 240 with content up to 720; mobile: a category list then one page per category. Rows: label, a description of what changes for whom, the control. Toggles apply instantly with a quiet "Saved"; text fields save per section card with a Save button and an unsaved-changes warning; never mix both models in one group. Danger zone last, in its own card, with the consequence in plain words and an export offered first. Secrets masked (`sk_live_…4f2a`) with Copy and Regenerate; a new key is shown once with a warning.

## Checkout and subscriptions
Guest checkout first; all costs visible before the payment step; fewer fields matter more than fewer steps; express wallets at the top; promo code behind a link; "billing same as shipping" on by default; address autocomplete. Form beside a sticky order summary (mobile: a collapsible total bar). One card-number field with auto-spacing and brand detection, one expiry field, CVC help, hosted payment fields, a visibly distinct secure area. The pay button states the total ("Pay $128.40"), then "Processing payment…"; a decline keeps the fields and explains plainly. Confirmation: order number, next steps, delivery estimate, email sent. Subscriptions: renewal date, price and cancellation terms before payment; cancelling as easy as signing up (a legal requirement in several places).

## AI features (Microsoft Human-AI Interaction guidelines, Google PAIR)
- Chat: reading column 680 to 760; composer grows 1 to 8 lines; Enter sends on desktop; the send button becomes Stop while generating; a standing disclosure ("AI can make mistakes. Check important information."); 3 to 4 product-specific starter prompts; copy, regenerate and feedback on answers; auto-scroll only when the user is at the bottom.
- Streaming: show the user's message and a working indicator within 100 ms; agent steps in plain language in a collapsible activity block; Stop keeps partial output labelled "Stopped"; screen readers get updates at completion, never per token.
- Citations at the claim with a preview; honest uncertainty ("I couldn't find this in your documents"); label AI drafts.
- Control ladder: read-only actions run freely; edits to user content show a preview or diff with Accept, Reject and Edit; reversible writes run with Undo and versioning; irreversible or external actions (send, pay, delete, publish) need an explicit confirmation showing what and to whom. A chatbot must never be the only way to do something a button does in one step. No blue-to-purple gradient as the AI signature.

## Bilingual and Bangla interfaces
`lang` set per locale and `lang="bn"` on Bangla fragments; Bangla font (Hind Siliguri, Noto Sans Bengali, Anek Bangla) listed after the Latin font; looser line height for Bangla (body 1.6 to 1.75, headings 1.35 to 1.4); Bangla text one step larger; no uppercase, letter-spacing or synthetic italics on Bangla (emphasise by weight); one numeral system per screen, Latin digits in tables, lakh grouping for BDT (4,82,300); allow 30 to 50% string growth. The same thinking applies to any second script.

## Dark mode for apps
Designed, not inverted: tinted near-black background, each layer slightly lighter, borders at low opacity, elevation by surface lightness, brand colours lighter and less saturated, separate chart colours, logo variants for dark; Light / Dark / System choice. Default to dark only for monitoring, developer, trading and long-session tools.
