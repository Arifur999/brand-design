# brand-design

Two Claude Skills for professional design work:

| Skill | Use it for |
|---|---|
| [`ui-ux-visual-designer`](skills/ui-ux-visual-designer/SKILL.md) | Websites, landing pages, funnels, web apps, SaaS, dashboards, mobile apps: discovery, IA, visual direction, components, states, accessibility, review and developer handoff |
| [`brand-identity-designer`](skills/brand-identity-designer/SKILL.md) | Brand strategy, positioning, logo and mark systems, typography, colour, visual language, applications, guidelines and token handoff; also critiques and refreshes |

The brand skill produces the identity and its tokens; the UI skill consumes them to design interfaces.

## How they stay token-efficient

Each skill loads in three layers, so a task only pays for what it uses:

1. **Name + description** (~200 tokens each), always visible so Claude knows when to use the skill.
2. **`SKILL.md`** (~105 lines): the workflow, principles, quality bar and a routing table, loaded when the skill triggers.
3. **`references/*.md`**: one file per topic (marketing pages, dashboards, mobile, logo, colour...), loaded only when the routing table says the task needs it. A landing page reads `foundations`, `direction`, `marketing-and-funnels` and `review`; it never loads the dashboard or mobile files.

The knowledge was distilled from about 1.4 MB of existing material (the Master Design System knowledge base, the `D:\dev\knowledge-base\design` files, earlier archived skills, and two public reference repos) down to about 1,600 lines across both skills.

## Layout

```
skills/
  ui-ux-visual-designer/
    SKILL.md
    references/   foundations, discovery, direction, marketing-and-funnels, apps-and-saas,
                  dashboards-and-data, mobile, components, industries, accessibility,
                  review, handoff, resources
    scripts/      color_tools.py, render.py
    evals/        test cases (prompt, expected outcome, graders)
  brand-identity-designer/
    SKILL.md
    references/   strategy, routes, logo, typography, color, visual-language, sectors,
                  applications, guidelines, review, resources
    scripts/      color_tools.py, render.py
    evals/
```

## Tools (Python standard library only, no installs)

- `scripts/color_tools.py`: WCAG contrast, OKLCH conversion, 11-step ramps that keep the exact brand hex, CIEDE2000 distance to competitor colours, colour-blind simulation, palette audits from a JSON file. Verified against WCAG reference values and the Sharma CIEDE2000 test data.
- `scripts/render.py`: renders HTML, SVG or URLs to PNG with the local Chrome, Edge or Chromium in headless mode: responsive captures at 375 / 768 / 1280 / 1536, and a logo contact sheet with true 16 and 32 px rasters enlarged. Narrow widths render in an exact-width frame because headless Chrome will not open a window narrower than about 500 px.

- `scripts/outline_text.py` (brand skill only): fetches open-licence fonts from the Google Fonts repository with their licence files, and turns text into outlined SVG paths with HarfBuzz shaping, so wordmarks and bilingual signs (Bangla included) need no installed fonts. The `outline` command needs `fonttools` and `uharfbuzz`; the skill asks before installing them.

Both skills carry identical copies of `color_tools.py` and `render.py` because each skill must work on its own when uploaded. Edit one copy and copy it to the other.

## Install

**Claude Code** (this machine): copy each folder in `skills/` to `%USERPROFILE%\.claude\skills\`, then start a new session.

```powershell
Copy-Item -Recurse -Force .\skills\ui-ux-visual-designer, .\skills\brand-identity-designer $env:USERPROFILE\.claude\skills\
```

**claude.ai** (web and desktop): Settings → Capabilities → Skills → upload each skill as a ZIP whose root folder is the skill folder (`ui-ux-visual-designer.zip` containing `ui-ux-visual-designer/SKILL.md`). The `evals/` folder may be left out of the upload.

## Maintenance

- Dated facts (platform sizes, iOS and Android specifics, legal dates, licence terms) are marked with their check date in the reference files. Re-check them about every six months, and always before quoting an exact number to a client.
- When a project teaches something general, add it to the one reference file it belongs in, not to `SKILL.md`, and keep `SKILL.md` near 100 lines.
- Re-run the test cases in `evals/` after changing a skill (with and without the skill) to check the change helped.
