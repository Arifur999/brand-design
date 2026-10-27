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
- Accessibility notes: landmarks, heading outline, focus order, skip link, accessible names, live regions.
- SEO: titles, descriptions, heading structure, structured data, redirect map (for site projects).
- Acceptance criteria: the review rubric target (`review.md`), breakpoints tested, performance budget, the accessibility checklist.
- Native apps: per screen which components are native and which custom, the platform and OS version, all states, app icons at every required size.

## Boundaries
This skill decides the tokens, values, specs and states. Generating framework files (globals.css, component variants, test harnesses, contrast scripts in the repo) belongs to the codebase and to implementation skills when installed (for example `design-system-setup`, `dashboard-ui`, `nextjs-feature`). If none exist, write the code following the repo's conventions.

## White-label work
Deliver unbranded: no studio name in files, metadata, class names, staging URLs or comments. Licences registered to the partner or end client. Do not hand over paid UI kit source files to anyone without their own licence. Follow the partner's naming and framework conventions.
