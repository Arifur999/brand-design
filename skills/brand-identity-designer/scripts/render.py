#!/usr/bin/env python3
"""Render designs to PNG with a local headless Chrome, Edge or Chromium, so you can look at them.
Standard library only. Read every PNG you produce; a render you did not look at proves nothing.

Commands:
  shot   INPUT --out FILE.png [--width 1280] [--height 900] [--scale 1]
         INPUT is an .html or .svg file or a URL. Use a tall --height for a long page.
  responsive INPUT --outdir DIR [--height 1800]
         375, 768, 1280 and 1536 wide captures (the breakpoints a reviewer checks).
  logo-sheet SVG --out FILE.png [--ground "#F5F3EE"] [--dark "#141414"] [--brand "#0F3D3E"] [--wordmark SVG]
         Contact sheet: large, 64, 32 and 16 px on light, dark and brand grounds, one-colour black and white,
         plus the real 16 and 32 px rasters enlarged so clogged joins and lost details are visible.

Set CHROME_PATH if the browser is not found automatically.
"""
import argparse
import html
import os
import pathlib
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib

CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def find_browser():
    env = os.environ.get("CHROME_PATH")
    if env and pathlib.Path(env).exists():
        return env
    for c in CANDIDATES:
        if pathlib.Path(c).exists():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No Chrome, Edge or Chromium found. Install one or set CHROME_PATH.")


def to_url(target):
    if target.startswith(("http://", "https://", "file://", "data:")):
        return target
    path = pathlib.Path(target).resolve()
    if not path.exists():
        sys.exit(f"not found: {target}")
    if os.name == "nt" and len(str(path)) > 200:
        print(f"warning: long path ({len(str(path))} chars). Chrome on Windows fails to load files, and images the "
              "page references, past 260 characters; if the render shows broken images, work in a shorter folder.")
    return path.as_uri()


MIN_WINDOW = 520  # headless Chrome will not open a narrower window


def crop_png_width(path, width):
    """Crop a PNG to its left `width` pixels in place (8-bit RGB or RGBA, non-interlaced)."""
    data = pathlib.Path(path).read_bytes()
    pos, chunks = 8, []
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        chunks.append((data[pos + 4:pos + 8], data[pos + 8:pos + 8 + length]))
        pos += 12 + length
    ihdr = chunks[0][1]
    w, h, depth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", ihdr)
    if depth != 8 or ctype not in (2, 6) or interlace or width >= w:
        return
    bpp = 4 if ctype == 6 else 3
    raw = zlib.decompress(b"".join(body for kind, body in chunks if kind == b"IDAT"))
    stride, prev, out = w * bpp, bytearray(w * bpp), bytearray()
    for y in range(h):
        ftype = raw[y * (stride + 1)]
        line = bytearray(raw[y * (stride + 1) + 1:(y + 1) * (stride + 1)])
        if ftype == 1:
            for i in range(bpp, stride):
                line[i] = (line[i] + line[i - bpp]) & 255
        elif ftype == 2:
            line = bytearray((a + b) & 255 for a, b in zip(line, prev))
        elif ftype == 3:
            for i in range(stride):
                left = line[i - bpp] if i >= bpp else 0
                line[i] = (line[i] + ((left + prev[i]) >> 1)) & 255
        elif ftype == 4:
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                b, c = prev[i], (prev[i - bpp] if i >= bpp else 0)
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        out += b"\x00" + line[:width * bpp]
        prev = line

    def chunk(kind, body):
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)

    new_ihdr = struct.pack(">IIBBBBB", width, h, depth, ctype, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", new_ihdr) + chunk(b"IDAT", zlib.compress(bytes(out), 6)) + chunk(b"IEND", b"")
    pathlib.Path(path).write_bytes(png)


def shoot(target, out, width, height, scale=1.0, wait_ms=2500):
    browser = find_browser()
    out = pathlib.Path(out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    requested = width
    with tempfile.TemporaryDirectory() as profile:
        if width < MIN_WINDOW:
            # A phone-width viewport is an iframe of the exact width, cropped back to that width afterwards.
            # Sites that refuse framing (X-Frame-Options) render blank here: capture them at 520+ instead.
            frame = pathlib.Path(profile) / "frame.html"
            frame.write_text(
                f'<!doctype html><body style="margin:0;background:#9a9a9a">'
                f'<iframe src="{html.escape(to_url(target))}" style="border:0;width:{width}px;height:{height}px;'
                f'background:#fff;display:block"></iframe></body>', encoding="utf-8")
            target, width = str(frame), MIN_WINDOW
        cmd = [
            browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
            "--no-default-browser-check", "--allow-file-access-from-files", f"--user-data-dir={profile}",
            f"--window-size={width},{height}", f"--force-device-scale-factor={scale}",
            f"--virtual-time-budget={wait_ms}", f"--screenshot={out}", to_url(target),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if not out.exists():
        sys.exit(f"render failed: {result.stderr.strip()[-600:]}")
    if requested < width:
        crop_png_width(out, round(requested * scale))
        width = requested
    print(f"{out}  ({width}x{height} viewport @{scale}x)")
    return out


LOGO_TEMPLATE = """<!doctype html><meta charset="utf-8"><style>
body{{margin:0;padding:24px;font:12px/1.4 system-ui,sans-serif;background:#fff;color:#222}}
h2{{font-size:13px;margin:18px 0 8px}} .row{{display:flex;gap:12px;flex-wrap:wrap;align-items:stretch}}
.cell{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:16px;
min-width:120px;border:1px solid #ddd}} .cell span{{font-size:11px;opacity:.7}}
img{{display:block}} .black img{{filter:brightness(0)}} .white img{{filter:brightness(0) invert(1)}} .white span,.ondark span{{color:#eee}}
canvas{{image-rendering:pixelated;border:1px dashed rgba(128,128,128,.5)}}
</style>
<h2>Sizes on grounds (real browser rendering)</h2>
{rows}
<h2>One colour</h2>
<div class="row">
 <div class="cell black" style="background:{ground}"><img src="{src}" style="height:96px"><span>black, 96</span></div>
 <div class="cell black" style="background:{ground}"><img src="{src}" style="height:24px"><span>black, 24</span></div>
 <div class="cell white" style="background:{dark}"><img src="{src}" style="height:96px"><span>white, 96</span></div>
 <div class="cell white" style="background:{dark}"><img src="{src}" style="height:24px"><span>white, 24</span></div>
</div>
<h2>Actual 16 and 32 px rasters, enlarged 8x and 4x (look for clogged joins, lost gaps, letters that misread)</h2>
<div class="row">
 <div class="cell" style="background:{ground}"><canvas id="c16" width="16" height="16" style="width:128px;height:128px"></canvas><span>16 px</span></div>
 <div class="cell" style="background:{ground}"><canvas id="c32" width="32" height="32" style="width:128px;height:128px"></canvas><span>32 px</span></div>
 <div class="cell ondark" style="background:{dark}"><canvas id="d16" width="16" height="16" style="width:128px;height:128px"></canvas><span>16 px on dark</span></div>
</div>
{wordmark}
<script>
const img = new Image();
img.onload = () => {{
  for (const [id, s, bg] of [["c16",16,"{ground}"],["c32",32,"{ground}"],["d16",16,"{dark}"]]) {{
    const cv = document.getElementById(id), ctx = cv.getContext("2d");
    ctx.fillStyle = bg; ctx.fillRect(0,0,s,s);
    const r = Math.min(s / img.naturalWidth, s / img.naturalHeight);
    const w = img.naturalWidth * r, h = img.naturalHeight * r;
    ctx.drawImage(img, (s-w)/2, (s-h)/2, w, h);
  }}
}};
img.src = "{src}";
</script>"""


def cmd_logo_sheet(args):
    svg = pathlib.Path(args.svg).resolve()
    if not svg.exists():
        sys.exit(f"not found: {svg}")
    # Stage inputs in a short folder: Chrome on Windows cannot load file:// paths over 260 characters.
    stage = pathlib.Path(tempfile.mkdtemp(prefix="sheet"))
    shutil.copy(svg, stage / "mark.svg")
    src = (stage / "mark.svg").as_uri()
    grounds = [("light", args.ground), ("dark", args.dark)] + ([("brand", args.brand)] if args.brand else [])
    rows = []
    for label, color in grounds:
        cells = "".join(
            f'<div class="cell" style="background:{html.escape(color)}"><img src="{src}" style="height:{size}px">'
            f'<span style="color:{"#fff" if label != "light" else "#222"}">{label}, {size}px</span></div>'
            for size in (160, 64, 32, 16))
        rows.append(f'<div class="row">{cells}</div>')
    wordmark = ""
    if args.wordmark:
        shutil.copy(pathlib.Path(args.wordmark).resolve(), stage / "wordmark.svg")
        wm = (stage / "wordmark.svg").as_uri()
        wordmark = ("<h2>Lockup / wordmark</h2><div class='row'>" + "".join(
            f'<div class="cell" style="background:{html.escape(c)}"><img src="{wm}" style="height:{h}px">'
            f'<span>{h}px high</span></div>' for c, h in ((args.ground, 64), (args.ground, 20), (args.dark, 20))) + "</div>")
    page = LOGO_TEMPLATE.format(rows="".join(rows), src=src, ground=html.escape(args.ground),
                                dark=html.escape(args.dark), wordmark=wordmark)
    sheet = stage / "sheet.html"
    sheet.write_text(page, encoding="utf-8")
    try:
        shoot(str(sheet), args.out, 1100, 1460 if args.wordmark else 1240)
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("shot")
    s.add_argument("input"); s.add_argument("--out", required=True)
    s.add_argument("--width", type=int, default=1280); s.add_argument("--height", type=int, default=900)
    s.add_argument("--scale", type=float, default=1.0)
    s.set_defaults(fn=lambda a: shoot(a.input, a.out, a.width, a.height, a.scale))
    s = sub.add_parser("responsive")
    s.add_argument("input"); s.add_argument("--outdir", required=True); s.add_argument("--height", type=int, default=1800)
    s.set_defaults(fn=lambda a: [shoot(a.input, pathlib.Path(a.outdir) / f"w{w}.png", w, a.height)
                                 for w in (375, 768, 1280, 1536)])
    s = sub.add_parser("logo-sheet")
    s.add_argument("svg"); s.add_argument("--out", required=True)
    s.add_argument("--ground", default="#F7F7F5"); s.add_argument("--dark", default="#141414")
    s.add_argument("--brand"); s.add_argument("--wordmark")
    s.set_defaults(fn=cmd_logo_sheet)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
