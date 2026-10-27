# Design system and developer handoff

The goal of handoff: a developer can build it without asking a question, and the result matches the design at every breakpoint and in every state.

## Tokens
- Make five decisions first and write them down: brand hue, radius, density, fonts, elevation style.
- Three layers:
  1. **Primitives** (reference scales): `brand-50` … `brand-950`, `neutral-*`, status ramps, in OKLCH. Components never use them directly.
  2. **Semantic roles** (the contract): `background`, `surface`, `surface-raised`, `surface-sunken`, `border-subtle` (decorative only), `border` (3:1 control edges), `border-strong`, `text`, `text-muted`, `text-subtle`, `text-inverse`, `primary`, `primary-hover`, `primary-pressed`, `primary-subtle`, `on-primary`, `accent`, `on-accent`, `success` / `warning` / `danger` / `info` each with `-subtle` and `on-`, `focus-ring`, `overlay`. Light and dark differ **only** at this layer.
  3. **Component tokens**: `sidebar-width`, `chart-1` … `chart-5`, `kpi-value-size`, control heights.
- Also: spacing (4 px base), radius set, shadows, type scale (fixed for apps, `clamp()` with a rem term for marketing), motion durations and easings, z-index layers, breakpoints.
- Every fill has an `on-` partner and only these pairs are guaranteed; list the tested pairs with ratios for both themes (`scripts/color_tools.py audit`). When the brand colour fails 4.5:1 for button text, keep the exact hex for the logo and large graphics and map `primary` to the first darker step that passes.
- Name by job, not hue (`primary`, not `blue`). One source of truth; generated files read-only.
- Formats: CSS custom properties always (light on `:root`, dark on `[data-theme="dark"]` and under `prefers-color-scheme: dark` for `:root:not([data-theme="light"])`). W3C Design Tokens (DTCG) JSON (`$value`, `$type`, aliases like `{color.brand.600}`) when a pipeline consumes it: Style Dictionary, Tokens Studio or Figma Variables (one file per mode, since DTCG has no modes). Tailwind v4: tokens in CSS with `@theme inline` mapping semantic roles; no `dark:` colour overrides in components.
- Platforms: Webflow variables collections (primitives → theme → type → space → radius) with modes for light and dark; Elementor global colours mapped to roles; iOS and Android: map roles to the platform's colour roles (`mobile.md`).

## Handoff package
- Designs at 390 and 1440 (plus 768 and 1024 where the structure changes), in light and dark if both ship.
- Token sheet (values, tested pairs with ratios).
- Component inventory: variants, props, and **every state** (default, hover, focus-visible, active, disabled, loading, error, selected, empty).
- Per-section responsive notes in one format: `Section · base · md · lg · image sizes · hidden or changed`.
- Interaction spec for each animation: trigger, properties, duration, easing, delay, reduced-motion behaviour.
- Final copy per page with heading levels marked; microcopy for errors, empty states and confirmations; alt-text sheet.
- Forms: fields, validation rules and timing, error messages, destination, success state, spam protection, analytics event.
- Data: content model or CMS fields with types and character limits; templates for 0, 1, many and long-title cases.
- Assets: logo SVG (primary, reversed, icon) with PNG fallbacks; favicon set and Apple touch icon; social share image 1200 × 630; photos at 2x named descriptively; the icon set named; fonts with licences and loading notes.
- Fontshare (ITF licence) fonts: give the client the download link, never the files.
- Accessibility notes: landmarks, heading outline, focus order, skip link, accessible names, live regions.
- SEO: titles, descriptions, heading structure, structured data, redirect map (for site projects).
- Acceptance criteria: the review rubric target (`review.md`), breakpoints tested, performance budget, the accessibility checklist.
- Native apps: per screen which components are native and which custom, the platform and OS version, all states, app icons at every required size.

## Boundaries
This skill decides the tokens, values, specs and states. Generating framework files (globals.css, component variants, test harnesses, contrast scripts in the repo) belongs to the codebase and to implementation skills when installed (for example `dashboard-ui`, `nextjs-feature`, `nextjs-app-setup`). If none exist, write the code following the repo's conventions.

## White-label work
Deliver unbranded: no studio name in files, metadata, class names, staging URLs or comments. Licences registered to the partner or end client. Do not hand over paid UI kit source files to anyone without their own licence. Follow the partner's naming and framework conventions.

## Builder platforms and Figma
Name every variable, global and style exactly as the semantic role (`text-muted`, not `grey-text`). Platform facts checked Oct 2026, verify on large projects.

**Webflow**
- Pick one class framework per site, never mixed: Client-First (partners expect it; `section_hero`, `padding-global`, `is-` combos) for client-edited sites, Lumos (fluid by default, `u-` utilities, variable-first) for experienced builders. Follow the partner's choice on white-label work.
- Variables in collections: Primitives, Theme (semantic, references primitives), Type, Space, Radius. Classes reference semantic variables only; never a hex in a class. Modes handle light/dark and per-breakpoint values. Variables accept `clamp()`, `calc()`, `min()`, `max()`, `color-mix()`, so paste fluid type in directly.
- Desktop-first breakpoints (base 992 and up, 991, 767, 478); add 1440 and 1920 only when the design changes there.
- Components for every repeated section; expose props only for what editors change; use variants (primary/ghost, light/dark band) instead of combo-class piles.
- CMS: model first (fields, types, required, character limits with editor help text). Limits (Webflow Help Center, checked Oct 2026, verify): 40 collection lists per page, 100 items shown per list by default, 10 nested lists, 3 nesting levels. Design templates for 0, 1, many and long-title cases; every image field gets a fallback.
- Interactions budget per page: 1 hero sequence under 800 ms readable at frame 1; reveals opacity plus 8 to 16 px, 300 to 500 ms, once; 1 scroll-linked effect; Lottie 1 to 2 under 100 KB each; 3 to 5 reusable presets site-wide. Reduced-motion fallback shows the end state. Never hide content until JS runs (crawlers, slow connections).
- Images: hero eager, rest lazy; AVIF/WebP conversion on; alt text set once in the asset, overridden per use.

**Elementor**
- v4 (Atomic Editor) is default for new sites since April 2026 (verify): use Variables (colour, size, font) and Classes as the token layer; they work on Atomic Elements only, not legacy widgets. Existing v3 sites keep kit Global Colors and Fonts.
- Global colours mapping: Primary to heading colour (`text`), Secondary to `text-muted`, Text to `text`, Accent to `primary`; add custom globals named after the roles (`bg`, `surface`, `border`, `primary-hover`, `on-primary`, `danger`). Alias them in CSS (`--text: var(--e-global-color-text)`). Dark mode is custom CSS, quote it separately.
- Content width 1200 to 1280, containers not sections/columns, nesting 4 levels or fewer, at most one addon pack, no hero sliders.

**WordPress block themes**
- Tokens live in `theme.json`: `settings.color.palette` (slugs = role names), `typography.fontFamilies` (self-hosted `fontFace`), `fluid` font sizes, `spacing.spacingSizes`, `styles.elements` for links/buttons/headings. Editors then pick tokens, not hex. Dark variants as `styles/*.json` style variations. Build repeated sections as block patterns.

**Figma deliverable must contain**
- A cover (name, version, status, date) and a Styleguide page (colour roles with tested ratios, type scale, spacing, radius, elevation, icons).
- Variables from the token roles in collections Primitives and Semantic, with Light and Dark modes; spacing, radius and type as variables; styles only for effects and text where variables cannot.
- Components with variants and properties (boolean, text, instance swap) covering every state; built with auto layout and constraints; nothing detached or hand-spaced.
- Naming: `Component/Variant/State` for components, pages `Cover`, `Styleguide`, `Components`, then one page per flow; frames named by screen.
- Screens at 390 and 1440 (plus 768 and 1024 where structure changes), in both modes if both ship, with real copy; annotations for interactions and responsive behaviour; dev-ready sections marked.
