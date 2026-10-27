#!/usr/bin/env python3
"""Turn text into outlined SVG paths (for wordmarks, lockups and signs), and fetch open-licence fonts.

Commands:
  fetch FAMILY --out DIR        download a Google Fonts family (SIL OFL / Apache) from github.com/google/fonts,
                                with its licence file. Example: fetch "Hind Siliguri" --out fonts/
  outline FONT TEXT --out FILE.svg [--size 100] [--tracking 0] [--var wght=700] [--fill "#1E2A4A"]
                                shape TEXT with HarfBuzz (correct kerning, ligatures and conjuncts for Bangla,
                                Devanagari, Arabic) and write a lint-clean SVG of filled paths, no live text.
                                Tracking is in 1/1000 em. Prints the advance width and bounds.

`fetch` needs only the standard library. `outline` needs two packages: fonttools and uharfbuzz.
If they are missing, ask the person before installing (`pip install fonttools uharfbuzz`); otherwise deliver
the lockup as HTML with the licensed web font and mark it "outline before production".
OFL fonts may be outlined into a logo. Fontshare (ITF licence) fonts may be used in logos but the font files
must not be modified, subset or handed over; outlining artwork is fine, shipping the font is not.
"""
import argparse
import json
import pathlib
import sys
import urllib.parse
import urllib.request


def cmd_fetch(args):
    slug = args.family.lower().replace(" ", "")
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for licence_dir in ("ofl", "apache", "ufl"):
        api = f"https://api.github.com/repos/google/fonts/contents/{licence_dir}/{urllib.parse.quote(slug)}"
        try:
            with urllib.request.urlopen(urllib.request.Request(api, headers={"User-Agent": "outline_text"}), timeout=30) as r:
                listing = json.load(r)
        except Exception:
            continue
        got = []
        for item in listing:
            name = item["name"]
            if name.endswith((".ttf", ".otf")) or name.upper().startswith(("OFL", "LICENSE")):
                urllib.request.urlretrieve(item["download_url"], out / name)
                got.append(name)
        print(f"{args.family} ({licence_dir.upper()}): " + ", ".join(got))
        return
    sys.exit(f"'{args.family}' not found in google/fonts (check spelling, or download it manually with its licence)")


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def cmd_outline(args):
    try:
        import uharfbuzz as hb
        from fontTools.pens.boundsPen import BoundsPen
        from fontTools.pens.svgPathPen import SVGPathPen
        from fontTools.pens.transformPen import TransformPen
    except ImportError:
        sys.exit("outline needs fonttools and uharfbuzz. Ask before installing: pip install fonttools uharfbuzz")
    blob = hb.Blob.from_file_path(args.font)
    face = hb.Face(blob)
    font = hb.Font(face)
    if args.var:
        font.set_variations({k: float(v) for k, v in (pair.split("=") for pair in args.var)})
    buf = hb.Buffer()
    buf.add_str(args.text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    scale = args.size / face.upem
    tracking = args.tracking / 1000 * args.size
    pen, bounds_pen = SVGPathPen(None, ntos=fmt), BoundsPen(None)
    x = 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        t = (scale, 0, 0, -scale, x + pos.x_offset * scale, -pos.y_offset * scale)
        font.draw_glyph_with_pen(info.codepoint, TransformPen(pen, t))
        font.draw_glyph_with_pen(info.codepoint, TransformPen(bounds_pen, t))
        x += pos.x_advance * scale + tracking
    if bounds_pen.bounds is None:
        sys.exit("nothing drawn: does the font contain these characters?")
    x0, y0, x1, y1 = bounds_pen.bounds
    missing = sum(1 for info in buf.glyph_infos if info.codepoint == 0)
    pad = args.size * 0.02
    vb = f"{fmt(x0 - pad)} {fmt(y0 - pad)} {fmt(x1 - x0 + 2 * pad)} {fmt(y1 - y0 + 2 * pad)}"
    title = args.text.replace("&", "&amp;").replace("<", "&lt;")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img"><title>{title}</title>'
           f'<path fill="{args.fill}" d="{pen.getCommands()}"/></svg>\n')
    pathlib.Path(args.out).write_text(svg, encoding="utf-8")
    print(f"{args.out}  advance {fmt(x - tracking)}  bounds {fmt(x0)},{fmt(y0)} to {fmt(x1)},{fmt(y1)}  "
          f"baseline y=0" + (f"  WARNING: {missing} missing glyph(s)" if missing else ""))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("fetch"); s.add_argument("family"); s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_fetch)
    s = sub.add_parser("outline"); s.add_argument("font"); s.add_argument("text"); s.add_argument("--out", required=True)
    s.add_argument("--size", type=float, default=100); s.add_argument("--tracking", type=float, default=0)
    s.add_argument("--var", nargs="*", help="variable axes, e.g. wght=700 wdth=90")
    s.add_argument("--fill", default="currentColor")
    s.set_defaults(fn=cmd_outline)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
