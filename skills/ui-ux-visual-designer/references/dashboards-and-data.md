# Dashboards and data-dense software

If the environment offers a dedicated data-visualisation skill (for example `dataviz`), load it before writing chart code; this file decides what the dashboard shows and how it behaves.

## Strategy
- Start from the 3 to 5 questions the user asks every day; every widget answers one of them or is cut.
- Choose the type: **operational** (what needs attention now; compact; live or 1 to 5 minute refresh; fits one screen), **analytical** (why did it change; filters, drill-down, export), **strategic** (are we on track; comfortable; 4 to 6 KPIs against targets, one trend, short commentary), **customer-facing** (results in plain language; comfortable). One role, one default dashboard; never one dashboard for executives, operators and analysts at once.
- Hierarchy: KPI row → the one chart that explains the KPIs → breakdowns → a "needs attention" list or detail table. The most important number top left. Core status fits one screen at 1280 × 800, otherwise it is a report (Stephen Few). Every number has context (comparison period, target or benchmark). Everything clicks through to the filtered detail ("Overdue invoices 12" opens the table filtered to overdue).

## Layout
- Design at 1440 × 900; check 1280 × 800 and 1920 × 1080. 12 columns, 24 gutters, padding 24 to 32, max 1440 (fluid only for wallboards). Worked example: 1440 − 256 sidebar − 64 padding = 1120 content; a KPI tile (3 columns) is about 262 wide; a half-width chart about 548.
- Widget sizes: KPI tile 3 or 4 columns, 112 to 140 tall; primary trend 8 to 12 columns, 320 to 400 tall; secondary charts 4 to 6 columns, 240 to 320; ranked list 4 columns; detail table 12 columns, 10 rows then paginate. Heights snap to a few values per row: uneven card heights look unfinished.
- Cards: surface, large radius, padding 20 to 24, a border or a light shadow (not both strong); header = title, date-range subtitle, menu (export, details). Dense dashboards drop shadows and use borders or gaps.
- Global controls top right or in a filter bar under the page header: date range with presets (Today, Yesterday, Last 7, Last 30, This month, Last month, QTD, YTD, Custom) and "compare to previous period / same period last year", 2 to 4 filters, saved views, "Last updated 2 min ago" with refresh, and the time zone. Global filters are echoed in each widget subtitle; local filters sit in the card header. Apply instantly if queries return in under ~1 s, otherwise with an Apply button. Filter state lives in the URL.
- Responsive: ≥1280 full sidebar and 4 KPIs across; 1024 to 1279 rail and 2 to 3 across; 768 to 1023 drawer and priority-column tables; under 768 drawer or bottom tabs, KPIs 2 × 2, tables become cards. The mobile dashboard answers "what changed and what needs me", not analysis.

## KPI tiles
- Label (muted, names the period, info icon with the definition, in the user's words: "Jobs booked") · value 32 to 40 px with tabular figures and unit ("$48.2k", "3.4 days") · delta = arrow + sign + value + comparison ("+12% vs previous 30 days") in success or danger colour, never colour alone · per-metric good direction (rising refunds, churn or cost is bad: never hard-code "up = green") · optional sparkline over the same period, no axes · optional target ("82% of $60k goal").
- 3 to 5 tiles per row; 6 or more and none reads as important. Each tile loads, fails and empties on its own.

## Charts
- Pick by question: change over time → line (area only for a single series; columns for a few discrete periods) · compare categories → bar, horizontal for long labels, sorted by value unless the order means something, starting at zero · part of whole → stacked or 100% bar; a donut only for 2 to 4 parts; no pie beyond a handful of slices; never 3D · distribution → histogram or box plot · relationship → scatter · location → a map only when location is the point (a ranked bar is often better) · progress to goal → bullet chart or progress bar, never a gauge. Length and position are read most accurately; angle and area least.
- At most 5 to 7 series; group the rest into "Other". A fixed categorical palette order so a series keeps its colour across every widget; sequential (one hue light to dark) for magnitude; diverging around a neutral midpoint for above and below target. Highlight one series and grey the rest to make a point. Direct end labels instead of legends where possible.
- Honest axes: bars from zero; line charts may start above zero only when labelled and not exaggerating; the same scale for charts shown side by side; avoid dual y-axes (use two small charts sharing an x-axis). 3 to 5 low-contrast horizontal gridlines; tick labels with tabular figures and units.
- Line stroke 2 px (a highlighted series 2.5 to 3, others at 40 to 60% opacity); bar gaps 30 to 50% of bar width. Chart colours reach 3:1 against the card (WCAG 1.4.11) and are checked for colour-blind confusion (`scripts/color_tools.py cvd`).
- The title states the finding or the measure and period ("Refunds doubled after 12 Sept"); tooltips on hover and focus with exact values, units and dates; a "View as table" option for keyboard and screen-reader users; an empty period shows axes plus "No sales in this period", not a flat zero line.

## Data tables
Four jobs (NN/g): find a row, compare rows, view or edit one row, act on several rows.
- Anatomy: toolbar (title and count, search whose placeholder names the searched fields, 3 to 4 visible filters, column and density controls, primary action on the right) → applied filter chips with Clear all → sticky header → rows → footer with pagination and page size.
- Rows: compact 32 to 36, default 40 to 48, comfortable 52 to 56; cell padding 12 to 16; dividers or zebra stripes, not both; hover and selected states.
- Alignment: text left, truncated with the full value available; numbers right-aligned with tabular figures and fixed decimals, the unit once in the header ("Amount (USD)"); headers aligned like their data; never centre; codes in mono; one date format app-wide (`12 Oct 2026`), relative time only within a week with the exact time on hover; status as a badge with text, never a dot alone; actions at the right.
- The first column is the human identifier (not a database ID), the widest, sticky when scrolling sideways, and the row link. 5 to 8 default columns; the rest in a Columns menu that remembers the choice.
- Sorting: arrow only on the sorted column, `aria-sort` on the header; text sorts ascending first, numbers and dates descending first; the default sort answers the most common question (newest or most urgent).
- Selection: a checkbox column; selecting the page offers "Select all 1,204"; a bulk bar replaces the toolbar ("12 selected · actions · Clear"); destructive bulk actions confirm with the count and object, Undo where reversible.
- Row actions: 1 to 2 frequent inline icon buttons (labelled, visible on hover and focus and always on touch), the rest in a "…" menu; row click opens the record consistently (drawer for a quick look, page for full work); inline edit with Enter to save and Esc to cancel.
- Pagination for goal-driven work ("1 to 50 of 1,204", page size 25 / 50 / 100); infinite scroll only for feeds; Load more for product lists. Keep the position after an edit; on refetch show the previous data with a thin progress bar instead of a skeleton; virtualise above about 500 rows.
- Responsive strategy per table: horizontal scroll with a sticky first column and an edge shadow, priority columns (secondary values shown under the identifier), or cards of 3 to 5 label-value pairs below the small breakpoint. Use a real `<table>` with header scope and a caption.

## Data formatting
Tiles abbreviate (`$1.24M`, `48.2k`, 2 to 3 significant digits); tables and tooltips show full values. Fixed decimals per metric. Rate changes in percentage points. Signed deltas with the period. A currency code when more than one currency appears. Negative money as `-$420` (parentheses only for finance audiences). Never ambiguous dates like `03/04/26`. Durations in the two largest units ("3h 12m"). Missing data shown as a muted "n/a" with a tooltip, never as 0. Units muted and slightly smaller than values.

## Dashboard states
New account (what will appear, how to connect data, optional labelled sample data) · syncing (progress and estimate) · filtered to nothing (echo the filters, Clear) · genuine zero ("0 complaints this month" styled as good news, not as an empty state) · not enough data ("The trend appears after 7 days") · no permission (who grants it, Request access) · stale ("Showing data from 9:42 AM. Refresh failed. Retry"). One broken query never blanks the whole dashboard.

## Roles, tenants and density
Owner: strategic, comfortable. Manager: team performance, default density. Operator: work queue, compact, inline actions. Analyst: exploration, compact, export and saved views. External client: results summary, comfortable. Hide what a role can never access; show with an explanation what it could get (upgrade, admin grant); never chart data the user cannot open in detail. White-label or multi-tenant: the client logo top left and only the primary tokens swapped (re-check contrast per tenant); status colours, chart palette and layout stay.

## Generic dashboard tells (each needs a reason, or goes)
Gradient or glowing KPI cards · coloured left borders on cards · five or more equal KPI cards · pie, donut or gauge by default · decorative sparklines with no data behind them · random chart colours · centred table text · status as a coloured dot alone · every action as a primary button · density changing between pages · screens that exist only in the happy state.

## QA
Each widget maps to a written question · core status visible at 1280 × 800 · every number has unit, period and comparison · the chart type fits the question · categorical colours fixed across widgets and colour-blind checked · table numbers right-aligned with sticky headers · filters in the URL with the time zone shown · loading, empty, error and stale states per widget · role views checked · light and dark both at 4.5:1 for text and 3:1 for graphics · widths 1920, 1440, 1280, 1024, 768, 390. References: IBM Carbon (tables, data visualisation), Linear, Stripe, Vercel Geist.
