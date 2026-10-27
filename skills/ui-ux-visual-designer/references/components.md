# Components and interaction states

Only the specs that are easy to get wrong. Read when designing or reviewing components, or building a design system.

## Principles
- One height scale for all controls: 32 (dense tables, toolbars) / 40 (app default) / 48 (marketing CTAs, mobile forms). Never mix sizes in one row. On touch, give 32 px controls a 44 px hit area with a pseudo-element.
- One primary button per view, dialog or card group.
- States change colour roles only (primary → primary-hover); never invent new colours for states.
- Focus: `outline: 2px solid var(--focus-ring); outline-offset: 2px` (offset −2 px inside clipping containers such as scrolling tab lists and tables).
- Radius by hierarchy: controls 8, cards 12, modals and panels 16, pills, badges, avatars and switches full; inner radius = outer minus padding.
- Weights: 400 body, 500 labels and buttons, 600 titles; 3 weights at most. Labels in sentence case without trailing colons; no all-caps labels or badges.
- Spacing: label to control 8, related buttons 12, field to field 24, groups 40+.
- Avoid disabled controls. Prefer leaving them enabled and explaining on submit, or `aria-disabled="true"` (stays focusable, can show a reason) with the reason nearby. Native `disabled` gets no hover or focus and cannot explain itself.

## Buttons
- Variants: primary (filled), secondary (surface + 1 px border), ghost, destructive, link (underlined). Sizes: 32 (padding 12, icon 16), 40 (16, icon 20), 48 (24). Minimum width = height; max 480 in forms.
- Loading: `aria-busy`, a spinner replaces the leading icon, the label changes to the present participle ("Saving"), the width does not change, repeat clicks are ignored; then past tense ("Saved") for about 1.5 s or a toast.
- Labels: verb + object, 1 to 3 words; the confirm button repeats the dialog's verb.
- Don't: two primary buttons side by side; a ghost button as the main hero CTA; more than 4 icon buttons in a row (use "More actions"); a tooltip as an icon button's only name. Toggle icon buttons use `aria-pressed`.

## Inputs
- Text input heights 32 / 40 / 48; width from content (postcode about 10 characters). The default border reaches 3:1 on its surface; focus adds the ring; read-only is a sunken fill but still focusable and copyable (not disabled); error = `aria-invalid`, danger border, icon and message. Do not turn every valid field green; show success only for async checks ("Username available").
- Textarea: at least 3 lines, vertical resize, grows to about 10 lines; a counter that turns into an error over the limit ("Shorten to 500 characters"), never cutting off typing; announce the counter only near the limit.
- Select (4 to 15 options): native `<select>` where possible (type-ahead and mobile pickers come free); never a select for yes/no; no default that silently opts in. Combobox for more than 15: max height 320, matched text bold, "No matches for 'x'", optional "Create 'x'", first Esc closes, second clears.
- Checkbox 20 px with 44 px rows (the whole row is the target); indeterminate for "select all"; phrased positively; never pre-ticked for consent (GDPR Recital 32).
- Radio: 2 to 6 visible options in a fieldset, arrows move, preselect the safest or most common, never a single radio.
- Switch: track 40 × 24, instant effect only; the label names the setting and never changes with state ("Booking reminders", never "On/Off"); on async save keep the new position with a small spinner and revert with an error if it fails; `role="switch"`.
- Slider: always shows the value and unit; pairs with a number input for precision; clicking the track works; ranges use two labelled thumbs.
- Date picker: day cells 40 (44 touch); unavailable days explain themselves on focus ("Fully booked"); a locale hint for typed dates; typed entry always works.
- Search field: `type="search"` inside `<search>`, a clear button that returns focus, Esc clears, a label naming the scope ("Name, email or ID"), never a bare "Search…".

## Containers and feedback
- **Card:** padding 24 (20 mobile, 16 dense), radius 12, a subtle border, no shadow at rest; interactive cards get a hover border or shadow and lift 2 px at most; whole-card links use the stretched-link pattern (not the whole card inside `<a>`); no cards inside cards; no thick coloured left borders.
- **Badge:** 20 or 24 tall, subtle fill with role-coloured text, 1 to 2 words, the same status uses the same word and tone everywhere, at most 3 per item.
- **Chip:** 32 tall; selected = subtle fill, border and a check (not colour alone); filter chips are toggle buttons; removable chips have a separate remove button with a name ("Remove Austin").
- **Avatar:** 24 / 32 / 40 / 48 / 64; initials on a subtle fill; status dot with a text equivalent; groups show 4 then "+N".
- **Alert:** icon in the role colour, a title of 8 words or fewer saying what happened, the body saying what to do; text stays in the normal text colour; danger alerts are not dismissible until fixed.
- **Toast:** see `apps-and-saas.md`; inverse surface, the live region exists before the first toast, anything it offers (Undo) is reachable elsewhere.
- **Tooltip:** 300 ms hover delay, immediate on keyboard focus, max 240 wide, flips at edges, no links or essential information, not on touch.
- **Menu:** 180 to 320 wide, items 36 (44 touch), destructive items last after a separator; never `role="menu"` for site navigation (use a disclosure button).
- **Modal:** 400 / 560 / 800 wide, max height `min(85vh, 760px)`, padding 24, native `<dialog>` with `showModal()`; initial focus on the first input, or on Cancel for destructive confirmations; no close on overlay click with unsaved input.
- **Drawer and bottom sheet:** drawer 400 / 560 / 720 (full width under 640); sheet max 90vh; no nesting.
- **Tabs:** 48 tall (40 compact), 2 px indicator, up to 6 tabs, active tab in the URL; tabs are not filters (use a segmented control for values). Segmented control: 2 to 5 options; the selected option needs an outline, because a surface-on-sunken fill alone is nearly invisible.
- **Accordion:** trigger at least 48 tall, content up to 70 characters wide, never hiding pricing terms; opens when the URL hash points inside.
- **Breadcrumb:** an ordered list in `nav aria-label="Breadcrumb"`, the current page not linked; on mobile only the parent with a back chevron.
- **Pagination:** "Previous" and "Next" written out, a summary naming the items, focus moves to the results heading after a page change.
- **Progress:** never goes backwards, no fake 99% hang; spinners appear after 300 ms, stay at least 500 ms once shown, become an error with Retry after about 15 s. Skeletons match the final layout and swap in with no layout shift.
- **Stepper:** 3 to 6 steps, completed steps clickable, future steps not, `aria-current="step"`; on mobile "Step 2 of 4: Payment" with a bar.
- **Empty state:** icon or small illustration, a heading, 1 to 2 lines, one primary action; first-use and no-results messages differ.

## Marketing components
- Pricing card: featured plan with a 2 px outline at the same size as the others; excluded features omitted or written "Not included" (never a grey X alone); CTA "Start with Pro".
- Testimonial: `figure`, `blockquote`, `figcaption`; quote up to 60 characters wide; stars with a text equivalent ("5 out of 5") and the source ("Google review").
- Feature blocks: vary layouts between sections; never the same three-card grid twice on a page.
- Logo row: 24 to 32 tall (square marks up to 40), monochrome via `currentColor`.
