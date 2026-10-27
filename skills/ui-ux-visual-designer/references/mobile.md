# Mobile apps and mobile web

Platform versions move every year. Values below were checked in October 2026 against Apple's iOS 26 guidance (Liquid Glass) and Material 3 Expressive (Android 16). iOS 27 may have shipped since: confirm current specifics on developer.apple.com and m3.material.io before quoting exact numbers, and name the platform and version in every brief ("iOS 26, SF Pro, tab bar with 4 tabs"), or designs drift into a web layout inside a phone frame.

## Frames and units
- iOS points = CSS px at 1x. Frames: 402 × 874 (current standard iPhone), 393 × 852, 430 × 932, 440 × 956 (largest: check line length), 375 × 667 (SE: the primary action must still fit). Android: 360 × 800 default, 412 × 915 large. iPad 820 × 1180 and 1024 × 1366.
- Safe areas (portrait): top about 59 to 62 pt, bottom 34 pt for the home indicator. Android 15+ is edge-to-edge by default: apply system insets, never fixed bar heights.
- Android window classes: compact < 600 (navigation bar, one pane) · medium 600 to 839 (rail) · expanded 840 to 1199 (rail, list-detail) · large 1200 to 1599 · extra-large ≥ 1600 (up to 3 panes). Lay out by available space, not by device or orientation.

## Platform decisions
| | iOS | Android |
|---|---|---|
| Touch target | 44 pt | 48 dp |
| Navigation | tab bar, up to 5 tabs, labels on every tab | navigation bar 3 to 5 destinations; rail on medium+; expanded rail replaces the drawer (navigation drawer is deprecated in M3 Expressive) |
| Body text | 17 pt (Body) | 16 sp (Body Large) / 14 sp (Body Medium) |
| Primary action | trailing nav-bar button or in content | FAB (one per screen, constructive only) or filled button |
| Back | leading chevron with previous title + edge swipe | system back (predictive back) + app-bar arrow |
| Dialogs | centred alert, 2 buttons side by side, 3+ stacked | end-aligned text buttons |
| Icons | SF Symbols (Apple platforms only) | Material Symbols |
| Font | SF Pro via the system (never embed SF files) | Roboto / Roboto Flex or the brand font |

## iOS essentials
- Side margins 16 pt (20 on the largest phones); keep controls out of the Dynamic Island and home-indicator zones.
- Tab bar: floats on Liquid Glass in iOS 26; up to 5 tabs, all labelled, filled symbol for the selected tab, no "More" overflow, visible across top-level sections. Navigation bar: Large Title (34 pt) on top-level screens collapsing to 17 pt semibold; at most 2 to 3 trailing actions.
- Sheets for short self-contained tasks: medium and large detents, a grabber on resizable sheets, Cancel leading and Done trailing, swipe-down dismissal asks before discarding unsaved changes, one sheet at a time.
- Dynamic Type sizes at the default (Large) setting: Large Title 34/41, Title 1 28/34, Title 2 22/28, Title 3 20/25, Headline 17/22 semibold, Body 17/22, Callout 16/21, Subheadline 15/20, Footnote 13/18, Caption 1 12/16, Caption 2 11/13. Use text styles, not fixed sizes; layouts survive 200%+ (wrap rather than truncate; two columns become one at accessibility sizes); avoid Ultralight, Thin and Light weights.
- Liquid Glass belongs to the navigation layer only (tab bars, toolbars, sheets, sidebars), never to content (cards, list rows, backgrounds). Do not fake it with heavy backdrop blur on web content cards. Controls on glass still need 4.5:1 and 3:1 over the brightest content scrolling beneath. Test Reduce Transparency and Increase Contrast.
- App icon: 1024 × 1024, layered (Icon Composer) with default, dark, clear and tinted appearances; no baked corners, shadows or highlights; no text unless essential.

## Material 3 Expressive essentials
- 48 dp targets (24 dp icons), at least 8 dp apart. Top app bar 64 dp with up to 3 actions plus overflow; medium and large variants collapse on scroll.
- FAB: medium 80 dp is the Expressive default (standard 56, large 96; the small FAB is deprecated); 16 dp from edges, above the navigation bar; list bottom padding = FAB height + 16.
- Type scale (sp): Display 57/45/36, Headline 32/28/24, Title 22/16/14, Body 16/14/12, Label 14/12/11. Android 14+ scales text non-linearly to 200%: test it.
- Shape scale: 4, 8, 12, 16, 20, 28, 32, 48, full; chips 8, cards 12, FAB 16, dialogs and bottom sheets 28.
- Colour roles: map primary/onPrimary, primaryContainer (subtle), tertiary (accent), error, surface and the five surfaceContainer tones (elevation by tone), outline (3:1 control edges) and outlineVariant (decorative). Brand-led apps keep their own scheme rather than dynamic colour.
- Adaptive icon: 108 × 108 dp layers, inner 66 dp never clipped, logo within 48 to 66 dp, plus a monochrome layer for themed icons.

## Cross-platform rules
- Keep the same: brand colours mapped to roles, IA, flows, labels, copy, empty states, imagery style, spacing base, accessibility rules.
- Adapt: navigation chrome, back behaviour, primary action placement, dialogs, system icons and font, native pickers, switches, share sheets and permission prompts (always native).
- Design first for the platform most users are on (check analytics). Never ship iOS-styled screens on Android or the reverse (tells: a Material FAB on iOS, a centred iOS alert on Android, a text-labelled back chevron on Android). Specify per screen which components are native and which are custom.

## Interaction patterns
- Thumb zone: primary actions in the lower half; destructive actions away from easy reach; edge targets larger.
- Bottom sheets: drag handle 32 to 36 × 4, max about 90% of the height, snap points (peek, half, full), dismiss by swipe or scrim tap and always a visible close button, content scrolls inside, honour the bottom safe area, no sheet on a sheet, no long forms.
- Gestures always have a visible alternative (WCAG 2.5.1 and 2.5.7); standard gestures keep their standard meanings; row swipes reveal actions (destructive ones get Undo); never override system edge gestures.
- Pull-to-refresh for time-ordered lists, with "Updated just now" and a refresh button too.
- Keyboard: the focused field scrolls above the keyboard; correct `inputmode`, `autocomplete` and `enterkeyhint`.
- Permissions asked in context, at the moment of need, with a sentence explaining why, and a path that still works if refused.
- Haptics for success, toggles and snaps, not every tap. Slow networks: show cached data with "Updated 5 min ago" and queue writes offline.
- Support both orientations unless essential (WCAG 1.3.4).

## Mobile web and responsive
- Mobile-first breakpoints: 640, 768, 1024, 1280, 1536. Above 1280 add margin, not more columns. Use container queries for components that live in different slot widths. Test 320 (WCAG reflow), 375, 390, 768, 1024, 1280, 1440, 1920, in-between widths (900, 1150), phone landscape 844 × 390, 200% zoom and the text-spacing override.
- Work order: content priority list → key screen at 390 → the same at 1440 → in-between frames only where structure changes → per-section breakpoint notes.
- `100svh` for full-screen heroes (fall back to `100vh`), `dvh` only for fixed overlays, never `width: 100vw` on blocks; `viewport-fit=cover` with `env(safe-area-inset-*)` on edge-fixed bars; never disable zoom; inputs at 16 px; sticky layers under 15% of the screen.
- Never hide decision-critical content on mobile: reorder or collapse it. Zigzag layouts never alternate on mobile (text then media every time). Modals become full-screen or bottom sheets.

## QA
Smallest, main and largest frames · 44/48 targets with 8 to 12 spacing · clear of the Island, status bar, home indicator and Android navigation · text styles survive 200% · contrast in light and dark appearances · navigation and back match the platform · loading, empty and error states per key screen · native components specified · icons supplied at every required size.
