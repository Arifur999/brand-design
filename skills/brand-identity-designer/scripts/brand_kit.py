#!/usr/bin/env python3
"""Production files for an approved identity. Standard library plus the local browser (via render.py).

Commands:
  lint SVG... [--forbid WORD ...] [--max-colours 3]
        Check logo masters: no live text, raster images, filters or foreignObject; a viewBox; a <title>;
        no fixed width/height; colour count; forbidden words (white-label check) in the file.
  onecolour SVG --out FILE.svg
        Write a one-colour master: every fill and stroke becomes currentColor (review it: knockouts drawn as
        light shapes become solid and must be real holes instead).
  export SVG --outdir DIR [--name brand-horizontal-fullcolor] [--widths 500 1000 2000] [--square] [--pdf]
        Transparent PNGs at each width (or padded squares for symbols), and a vector PDF if --pdf.
  icons SYMBOL.svg --outdir DIR --bg "#1E2A4A" [--fg "#F6F1E8"] [--name "Brand"] [--theme "#1E2A4A"]
        favicon.ico (16, 32, 48), icon.svg, apple-touch-icon.png (180, solid ground), icon-192.png, icon-512.png,
        icon-512-maskable.png (mark inside the central 80% circle), site.webmanifest and the <head> snippet.
        Use the small-size drawing of the symbol, not the master shrunk.
  tokens PALETTE.json --outdir DIR
        From {"name": "...", "brand": {"primary": "#hex", ...}, "roles": {"light": {"background": "#hex", ...},
        "dark": {...}}} write tokens.css, tokens.json (W3C DTCG) and swatches.html with tested pairs.
  boolean OP A.svg B.svg --out FILE.svg       (OP: union | difference | intersection | xor)
        Real path booleans for cut terminals and shared strokes. Needs skia-pathops: ask the person before
        installing it (pip install skia-pathops). Each input is the first <path> of its file.
"""
import argparse
import json
import pathlib
import re
import shutil
import struct
import sys
import tempfile
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from render import Browser  # noqa: E402
from color_tools import contrast_ratio, parse_hex, rgb_to_oklch  # noqa: E402

COLOUR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|oklch\([^)]*\)")


def read_svg(path):
    p = pathlib.Path(path)
    if not p.exists():
        sys.exit(f"not found: {path}")
    return p.read_text(encoding="utf-8")


def view_box(svg):
    m = re.search(r'viewBox="([^"]+)"', svg)
    if not m:
        sys.exit("the SVG has no viewBox: add one before exporting")
    x, y, w, h = (float(v) for v in m.group(1).replace(",", " ").split())
    return x, y, w, h


def cmd_lint(args):
    failures = 0
    for f in args.svgs:
        svg = read_svg(f)
        problems = []
        for tag in ("<text", "<image", "<foreignObject", "<filter", "<style", "<script"):
            if tag in svg:
                problems.append(f"contains {tag}>")
        if "viewBox=" not in svg:
            problems.append("no viewBox")
        if "<title" not in svg:
            problems.append("no <title> (accessible name)")
        root = svg[:svg.find(">")]
        if re.search(r'\s(width|height)="', root):
            problems.append("fixed width/height on <svg> (keep only the viewBox)")
        if "<!--" in svg or "<metadata" in svg:
            problems.append("comments or metadata left in the file")
        colours = {c.lower() for c in COLOUR_RE.findall(svg)}
        if len(colours) > args.max_colours:
            problems.append(f"{len(colours)} colours (max {args.max_colours}): {', '.join(sorted(colours))}")
        for word in args.forbid or []:
            if word.lower() in svg.lower():
                problems.append(f"forbidden word '{word}' present")
        status = "PASS" if not problems else "FAIL"
        failures += bool(problems)
        print(f"{status}  {f}" + "".join(f"\n      - {p}" for p in problems))
    sys.exit(1 if failures else 0)


def cmd_onecolour(args):
    svg = read_svg(args.svg)
    svg = re.sub(r'(fill|stroke)="(?!none)[^"]*"', r'\1="currentColor"', svg)
    svg = re.sub(r"(fill|stroke)\s*:\s*(?!none)[^;\"]+", r"\1:currentColor", svg)
    if 'fill="currentColor"' not in svg and "<svg" in svg:
        svg = svg.replace("<svg", '<svg fill="currentColor"', 1)
    pathlib.Path(args.out).write_text(svg, encoding="utf-8")
    print(f"{args.out}  (check shapes that were knockouts: they are now solid)")


def render_svg(browser, svg_path, out_png, width, height, pad=0.0, bg=None):
    """Render an SVG into an exact pixel box, centred, optional padding fraction and solid background."""
    stage = pathlib.Path(tempfile.mkdtemp(prefix="kit"))
    try:
        shutil.copy(svg_path, stage / "a.svg")
        inner_w, inner_h = width * (1 - 2 * pad), height * (1 - 2 * pad)
        page = (f'<!doctype html><meta name="viewport" content="width=device-width"><style>html,body{{margin:0;width:{width}px;height:{height}px;'
                f'background:{bg or "transparent"};display:grid;place-items:center;overflow:hidden}}'
                f'img{{max-width:{inner_w}px;max-height:{inner_h}px;width:{inner_w}px;height:{inner_h}px;'
                f'object-fit:contain}}</style><img src="a.svg">')
        (stage / "p.html").write_text(page, encoding="utf-8")
        browser.open((stage / "p.html").as_uri(), width, height, transparent=bg is None, mobile=False)
        time.sleep(0.3)
        browser.screenshot(out_png)
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def cmd_export(args):
    svg = pathlib.Path(args.svg).resolve()
    _, _, vw, vh = view_box(read_svg(svg))
    out = pathlib.Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    name = args.name or svg.stem
    b = Browser()
    try:
        for w in args.widths:
            if args.square:
                path = out / f"{name}-{w}.png"
                render_svg(b, svg, path, w, w, pad=0.1)
            else:
                h = max(1, round(w * vh / vw))
                path = out / f"{name}-{w}w.png"
                render_svg(b, svg, path, w, h)
            print(path)
        if args.pdf:
            stage = pathlib.Path(tempfile.mkdtemp(prefix="kitpdf"))
            shutil.copy(svg, stage / "a.svg")
            w_in = 8.0
            h_in = w_in * vh / vw
            (stage / "p.html").write_text(
                f'<!doctype html><style>@page{{size:{w_in}in {h_in}in;margin:0}}html,body{{margin:0}}'
                f'img{{display:block;width:{w_in}in;height:{h_in}in}}</style><img src="a.svg">', encoding="utf-8")
            b.open((stage / "p.html").as_uri(), 800, 800, mobile=False)
            time.sleep(0.3)
            b.pdf(out / f"{name}.pdf", w_in, h_in)
            shutil.rmtree(stage, ignore_errors=True)
            print(out / f"{name}.pdf  (vector PDF, RGB: CMYK and spot versions come from the printer's profile)")
    finally:
        b.close()


def write_ico(pngs, out):
    """ICO container holding PNG images (supported by every current browser and Windows Vista+)."""
    entries, blobs = [], []
    offset = 6 + 16 * len(pngs)
    for size, path in pngs:
        data = pathlib.Path(path).read_bytes()
        entries.append(struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0, 1, 32, len(data), offset))
        blobs.append(data)
        offset += len(data)
    pathlib.Path(out).write_bytes(struct.pack("<HHH", 0, 1, len(pngs)) + b"".join(entries) + b"".join(blobs))


def cmd_icons(args):
    svg = pathlib.Path(args.svg).resolve()
    if args.fg:
        recoloured = pathlib.Path(tempfile.mkdtemp(prefix="fg")) / "mark.svg"
        text = read_svg(svg)
        text = re.sub(r'(fill|stroke)="(?!none)[^"]*"', lambda m: f'{m.group(1)}="{args.fg}"', text)
        if 'fill="' not in text:
            text = text.replace("<svg", f'<svg fill="{args.fg}"', 1)
        recoloured.write_text(text, encoding="utf-8")
        svg = recoloured
    colours = [c for c in COLOUR_RE.findall(read_svg(svg)) if c.startswith("#")] or ["#000000"]
    for c in set(colours):
        if contrast_ratio(parse_hex(c), parse_hex(args.bg)) < 3:
            print(f"warning: mark colour {c} is under 3:1 on the tile {args.bg}; pass --fg with the reversed colour")
    out = pathlib.Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="ico"))
    b = Browser()
    try:
        ico_parts = []
        for s in (16, 32, 48):
            p = tmp / f"f{s}.png"
            # A reversed mark needs its tile in the favicon too, or it vanishes on light browser tabs.
            render_svg(b, svg, p, s, s, pad=0.1 if args.fg else 0.04, bg=args.bg if args.fg else None)
            ico_parts.append((s, p))
        write_ico(ico_parts, out / "favicon.ico")
        render_svg(b, svg, out / "apple-touch-icon.png", 180, 180, pad=0.11, bg=args.bg)
        render_svg(b, svg, out / "icon-192.png", 192, 192, pad=0.08, bg=args.bg)
        render_svg(b, svg, out / "icon-512.png", 512, 512, pad=0.08, bg=args.bg)
        render_svg(b, svg, out / "icon-512-maskable.png", 512, 512, pad=0.2, bg=args.bg)
    finally:
        b.close()
        shutil.rmtree(tmp, ignore_errors=True)
    if args.fg:
        mark = read_svg(svg)
        vb = re.search(r'viewBox="([^"]+)"', mark).group(1)
        inner = mark[mark.index(">") + 1:mark.rindex("</svg>")]
        (out / "icon.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>{args.name or "icon"}</title>'
            f'<rect width="100" height="100" rx="18" fill="{args.bg}"/>'
            f'<svg x="12" y="12" width="76" height="76" viewBox="{vb}">{inner}</svg></svg>\n', encoding="utf-8")
    else:
        shutil.copy(svg, out / "icon.svg")
    manifest = {"name": args.name or "", "short_name": args.name or "", "theme_color": args.theme or args.bg,
                "background_color": args.bg, "display": "standalone",
                "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                          {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                          {"src": "/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    (out / "site.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    snippet = ('<link rel="icon" href="/favicon.ico" sizes="32x32">\n<link rel="icon" href="/icon.svg" type="image/svg+xml">\n'
               '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<link rel="manifest" href="/site.webmanifest">\n'
               f'<meta name="theme-color" content="{args.theme or args.bg}">\n')
    (out / "head-snippet.html").write_text(snippet, encoding="utf-8")
    for f in sorted(out.iterdir()):
        print(f)


def cmd_tokens(args):
    spec = json.loads(pathlib.Path(args.palette).read_text(encoding="utf-8"))
    out = pathlib.Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    roles = spec.get("roles", {})
    light, dark = roles.get("light", {}), roles.get("dark", {})

    def block(sel, values, indent="  "):
        return f"{sel} {{\n" + "".join(f"{indent}--{k}: {v};\n" for k, v in values.items()) + "}\n"

    css = "/* Generated from " + pathlib.Path(args.palette).name + ". Components use roles, never brand values. */\n"
    css += block(":root", {**{f"brand-{k}": v for k, v in spec.get("brand", {}).items()}, **light})
    if dark:
        css += block('[data-theme="dark"]', dark)
        css += "@media (prefers-color-scheme: dark) {\n" + block('  :root:not([data-theme="light"])', dark, "    ") + "}\n"
    (out / "tokens.css").write_text(css, encoding="utf-8")

    dtcg = {"brand": {k: {"$type": "color", "$value": v} for k, v in spec.get("brand", {}).items()}}
    for mode, values in (("light", light), ("dark", dark)):
        if values:
            dtcg[mode] = {k: {"$type": "color", "$value": v} for k, v in values.items()}
    (out / "tokens.json").write_text(json.dumps(dtcg, indent=2), encoding="utf-8")

    rows = []
    for mode, values in (("light", light), ("dark", dark)):
        for k, v in values.items():
            if k.startswith("on-") and k[3:] in values:
                r = contrast_ratio(parse_hex(v), parse_hex(values[k[3:]]))
                rows.append((mode, k, k[3:], r))
        for text_role in ("text", "text-muted", "foreground", "muted-foreground"):
            for bg_role in ("background", "surface"):
                if text_role in values and bg_role in values:
                    rows.append((mode, text_role, bg_role, contrast_ratio(parse_hex(values[text_role]), parse_hex(values[bg_role]))))

    def swatch(name, hexv):
        L, C, H = rgb_to_oklch(parse_hex(hexv))
        return (f'<div class="sw"><div class="chip" style="background:{hexv}"></div><b>{name}</b>'
                f'<code>{hexv.upper()}</code><code>oklch({L:.3f} {C:.3f} {H:.0f})</code></div>')

    page = ['<!doctype html><meta charset="utf-8"><title>Swatches</title><style>body{font:14px/1.45 system-ui,sans-serif;'
            'margin:32px;color:#1a1a1a}h2{font-size:15px;margin:28px 0 10px}.grid{display:flex;flex-wrap:wrap;gap:14px}'
            '.sw{width:150px;display:grid;gap:3px}.chip{height:72px;border-radius:6px;border:1px solid #0002}code{font-size:12px;color:#555}'
            'table{border-collapse:collapse}td,th{padding:6px 12px;border-bottom:1px solid #ddd;text-align:left}'
            '.fail{color:#b42318;font-weight:600}</style>', f"<h1>{spec.get('name', 'Palette')}</h1>"]
    page.append("<h2>Brand colours</h2><div class='grid'>" + "".join(swatch(k, v) for k, v in spec.get("brand", {}).items()) + "</div>")
    for mode, values in (("Light roles", light), ("Dark roles", dark)):
        if values:
            page.append(f"<h2>{mode}</h2><div class='grid'>" + "".join(swatch(k, v) for k, v in values.items()) + "</div>")
    page.append("<h2>Tested pairs (only these pairs are guaranteed)</h2><table><tr><th>Mode</th><th>Text</th><th>On</th><th>Ratio</th><th>Body text</th></tr>")
    for mode, fg, bg, r in rows:
        ok = "pass" if r >= 4.5 else ("large text and UI only" if r >= 3 else "<span class='fail'>fails</span>")
        page.append(f"<tr><td>{mode}</td><td>{fg}</td><td>{bg}</td><td>{r:.2f}:1</td><td>{ok}</td></tr>")
    page.append("</table>")
    (out / "swatches.html").write_text("".join(page), encoding="utf-8")
    print(f"{out / 'tokens.css'}\n{out / 'tokens.json'}\n{out / 'swatches.html'}  ({len(rows)} tested pairs)")


def cmd_boolean(args):
    try:
        import pathops
    except ImportError:
        sys.exit("boolean needs skia-pathops. Ask before installing: pip install skia-pathops. "
                 "Without it, use fill-rule=\"evenodd\" compound paths for holes and flag the detail for the vector pass.")
    from fontTools.svgLib.path import parse_path  # fontTools ships with skia-pathops installs via pip deps
    from fontTools.pens.svgPathPen import SVGPathPen

    def load(f):
        d = re.search(r'<path[^>]*\sd="([^"]+)"', read_svg(f)).group(1)
        p = pathops.Path()
        parse_path(d, p.getPen())
        return p, read_svg(f)

    a, a_svg = load(args.a)
    b, _ = load(args.b)
    op = {"union": pathops.PathOp.UNION, "difference": pathops.PathOp.DIFFERENCE,
          "intersection": pathops.PathOp.INTERSECTION, "xor": pathops.PathOp.XOR}[args.op]
    result = pathops.op(a, b, op)
    pen = SVGPathPen(None)
    result.draw(pen)
    vb = re.search(r'viewBox="([^"]+)"', a_svg).group(1)
    pathlib.Path(args.out).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img"><title>{pathlib.Path(args.out).stem}</title>'
        f'<path fill="currentColor" d="{pen.getCommands()}"/></svg>\n', encoding="utf-8")
    print(args.out)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("lint"); s.add_argument("svgs", nargs="+"); s.add_argument("--forbid", nargs="*")
    s.add_argument("--max-colours", type=int, default=3); s.set_defaults(fn=cmd_lint)
    s = sub.add_parser("onecolour"); s.add_argument("svg"); s.add_argument("--out", required=True); s.set_defaults(fn=cmd_onecolour)
    s = sub.add_parser("export"); s.add_argument("svg"); s.add_argument("--outdir", required=True); s.add_argument("--name")
    s.add_argument("--widths", type=int, nargs="+", default=[500, 1000, 2000]); s.add_argument("--square", action="store_true")
    s.add_argument("--pdf", action="store_true"); s.set_defaults(fn=cmd_export)
    s = sub.add_parser("icons"); s.add_argument("svg"); s.add_argument("--outdir", required=True)
    s.add_argument("--bg", required=True); s.add_argument("--fg", help="recolour the mark for the tile (the reversed colour)")
    s.add_argument("--name"); s.add_argument("--theme"); s.set_defaults(fn=cmd_icons)
    s = sub.add_parser("tokens"); s.add_argument("palette"); s.add_argument("--outdir", required=True); s.set_defaults(fn=cmd_tokens)
    s = sub.add_parser("boolean"); s.add_argument("op", choices=["union", "difference", "intersection", "xor"])
    s.add_argument("a"); s.add_argument("b"); s.add_argument("--out", required=True); s.set_defaults(fn=cmd_boolean)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
