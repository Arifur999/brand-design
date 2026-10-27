#!/usr/bin/env python3
"""Render designs with a local headless Chrome, Edge or Chromium and report what is broken.
Standard library only (talks to the browser over the DevTools protocol). Read every PNG you produce.

Commands:
  shot INPUT --out FILE.png [--width 1280] [--height 900] [--full] [--dark] [--reduced-motion]
       [--scale 1] [--eval "JS"] [--wait 800]
       INPUT is an .html or .svg file or a URL. --full captures the whole page. --eval runs JavaScript
       before the capture (open a menu, show an error state, focus a field); it may return a Promise.
  responsive INPUT --outdir DIR [--dark] [--reduced-motion] [--eval "JS"]
       Full-page captures at 375, 768, 1280 and 1536 plus report.json.
  logo-sheet SVG --out FILE.png [--ground "#F7F7F5"] [--dark "#141414"] [--brand "#0F3D3E"] [--wordmark SVG]
       [--onecolour SVG]
       Contact sheet: large, 64, 32 and 16 px on light, dark and brand grounds, one-colour versions, and the
       real 16 and 32 px rasters enlarged. Pass --onecolour to show the actual one-colour master file.

Every capture prints a check line: horizontal overflow, h1 count, console errors, broken images, images
without alt, unnamed buttons or links, unlabelled form fields. Treat any non-zero value as a finding.
Set CHROME_PATH if the browser is not found automatically.
"""
import argparse
import base64
import html
import json
import os
import pathlib
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request

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
    if os.name == "nt" and len(str(path)) > 200 and not getattr(to_url, "warned", False):
        to_url.warned = True
        print(f"warning: long path ({len(str(path))} chars). Chrome on Windows cannot load files past 260 "
              "characters; if images are broken, work in a shorter folder.")
    return path.as_uri()

# ---------- minimal WebSocket client (RFC 6455, text frames) ----------


class WebSocket:
    def __init__(self, url):
        rest = url.split("://", 1)[1]
        hostport, path = rest.split("/", 1)
        host, port = hostport.split(":")
        self.sock = socket.create_connection((host, int(port)), timeout=60)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        head = b""
        while b"\r\n\r\n" not in head:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("websocket handshake failed")
            head += chunk
        if b" 101 " not in head.split(b"\r\n", 1)[0]:
            raise ConnectionError("websocket handshake refused")
        self.buf = head.split(b"\r\n\r\n", 1)[1]

    def _read(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(1 << 20)
            if not chunk:
                raise ConnectionError("browser closed the connection")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def _frame(self, opcode, payload):
        header = bytes([0x80 | opcode])
        n = len(payload)
        if n < 126:
            header += bytes([0x80 | n])
        elif n < 65536:
            header += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            header += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = os.urandom(4)
        self.sock.sendall(header + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))

    def send(self, text):
        self._frame(0x1, text.encode())

    def recv(self):
        message = b""
        while True:
            b0, b1 = self._read(2)
            opcode, n = b0 & 0x0F, b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._read(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._read(8))[0]
            mask = self._read(4) if b1 & 0x80 else None
            data = self._read(n)
            if mask:
                data = bytes(b ^ mask[i % 4] for i, b in enumerate(data))
            if opcode == 0x9:
                self._frame(0xA, data)
                continue
            if opcode == 0x8:
                raise ConnectionError("browser closed the connection")
            message += data
            if b0 & 0x80:
                return message.decode("utf-8", "replace")

# ---------- DevTools session ----------


class Browser:
    """One headless browser with one page, driven over the DevTools protocol."""

    def __init__(self):
        self.profile = tempfile.mkdtemp(prefix="render")
        self.proc = subprocess.Popen(
            [find_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
             "--no-default-browser-check", "--allow-file-access-from-files", "--remote-debugging-port=0",
             f"--user-data-dir={self.profile}", "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        port_file = pathlib.Path(self.profile) / "DevToolsActivePort"
        for _ in range(200):
            if port_file.exists() and port_file.read_text().strip():
                break
            time.sleep(0.05)
        else:
            self.close()
            raise RuntimeError("browser did not start its DevTools port")
        port = port_file.read_text().split()[0]
        for _ in range(100):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=5) as r:
                    pages = [t for t in json.load(r) if t.get("type") == "page"]
                if pages:
                    break
            except OSError:
                pass
            time.sleep(0.05)
        self.ws = WebSocket(pages[0]["webSocketDebuggerUrl"])
        self.next_id, self.events = 0, []
        for domain in ("Page", "Runtime", "Log"):
            self.call(f"{domain}.enable")

    def call(self, method, params=None, timeout=60):
        self.next_id += 1
        my_id = self.next_id
        self.ws.send(json.dumps({"id": my_id, "method": method, "params": params or {}}))
        deadline = time.time() + timeout
        while time.time() < deadline:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == my_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result", {})
            self.events.append(msg)
        raise TimeoutError(method)

    def wait_event(self, name, timeout=30):
        deadline = time.time() + timeout
        while time.time() < deadline:
            for i, e in enumerate(self.events):
                if e.get("method") == name:
                    return self.events.pop(i)
            self.ws.sock.settimeout(max(0.1, deadline - time.time()))
            try:
                self.events.append(json.loads(self.ws.recv()))
            except (socket.timeout, TimeoutError):
                break
            finally:
                self.ws.sock.settimeout(60)
        return None

    def evaluate(self, js, await_promise=True):
        r = self.call("Runtime.evaluate", {"expression": js, "awaitPromise": await_promise, "returnByValue": True})
        if "exceptionDetails" in r:
            raise RuntimeError("page script failed: " + r["exceptionDetails"].get("text", "")
                               + " " + str(r["exceptionDetails"].get("exception", {}).get("description", ""))[:300])
        return r.get("result", {}).get("value")

    def open(self, url, width, height, scale=1.0, dark=False, reduced_motion=False, transparent=False, mobile=None):
        mobile = width < 768 if mobile is None else mobile
        self.call("Emulation.setDeviceMetricsOverride",
                  {"width": width, "height": height, "deviceScaleFactor": scale, "mobile": mobile})
        self.call("Emulation.setEmulatedMedia", {"features": [
            {"name": "prefers-color-scheme", "value": "dark" if dark else "light"},
            {"name": "prefers-reduced-motion", "value": "reduce" if reduced_motion else "no-preference"}]})
        if transparent:
            self.call("Emulation.setDefaultBackgroundColorOverride", {"color": {"r": 0, "g": 0, "b": 0, "a": 0}})
        self.events.clear()
        self.call("Page.navigate", {"url": url})
        self.wait_event("Page.loadEventFired", timeout=45)

    def screenshot(self, out, full=False, scale=1.0):
        params = {"format": "png", "captureBeyondViewport": full}
        if full:
            dims = self.evaluate("({w: innerWidth, h: Math.min(Math.max(document.documentElement.scrollHeight,"
                                 " document.body ? document.body.scrollHeight : 0), 16000)})")
            params["clip"] = {"x": 0, "y": 0, "width": dims["w"], "height": dims["h"], "scale": 1}
        data = self.call("Page.captureScreenshot", params, timeout=120)["data"]
        out = pathlib.Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(base64.b64decode(data))
        return out

    def pdf(self, out, width_in, height_in):
        data = self.call("Page.printToPDF", {"paperWidth": width_in, "paperHeight": height_in, "printBackground": True,
                                             "marginTop": 0, "marginBottom": 0, "marginLeft": 0, "marginRight": 0,
                                             "pageRanges": "1"}, timeout=120)["data"]
        pathlib.Path(out).write_bytes(base64.b64decode(data))

    def console_errors(self):
        errors = []
        for e in self.events:
            m, p = e.get("method"), e.get("params", {})
            if m == "Runtime.exceptionThrown":
                errors.append(p.get("exceptionDetails", {}).get("text", "exception"))
            elif m == "Runtime.consoleAPICalled" and p.get("type") == "error":
                errors.append(" ".join(str(a.get("value", a.get("description", ""))) for a in p.get("args", [])))
            elif m == "Log.entryAdded" and p.get("entry", {}).get("level") == "error":
                errors.append(p["entry"].get("text", ""))
        return [e[:200] for e in errors]

    def close(self):
        try:
            self.proc.terminate()
            self.proc.wait(timeout=10)
        except Exception:
            pass
        shutil.rmtree(self.profile, ignore_errors=True)


SETTLE_JS = """(async () => {
  const pause = ms => new Promise(r => setTimeout(r, ms));
  if (document.fonts && document.fonts.ready) { await Promise.race([document.fonts.ready, pause(3000)]); }
  const step = Math.max(200, innerHeight * 0.8);
  for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await pause(120); }
  scrollTo(0, document.documentElement.scrollHeight); await pause(250);
  scrollTo(0, 0); await pause(400);
  return true;
})()"""

CHECK_JS = """(() => {
  const named = el => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('title') ||
    (el.getAttribute('aria-labelledby') ? 'x' : '') || (el.querySelector('img[alt]:not([alt=""]), svg title') ? 'x' : '')).trim();
  const visible = el => el.offsetParent !== null && !el.closest('[aria-hidden=true]') && getComputedStyle(el).visibility !== 'hidden';
  const fields = [...document.querySelectorAll('input:not([type=hidden]):not([type=submit]):not([type=button]), select, textarea')].filter(visible);
  const labelled = f => f.labels && f.labels.length || f.getAttribute('aria-label') || f.getAttribute('aria-labelledby') || f.title;
  return {
    viewport: innerWidth,
    overflow_px: Math.max(0, document.documentElement.scrollWidth - innerWidth),
    h1: document.querySelectorAll('h1').length,
    broken_images: [...document.images].filter(i => i.complete && i.naturalWidth === 0 && i.getAttribute('src')).map(i => i.getAttribute('src').slice(0, 80)),
    images_without_alt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
    unnamed_controls: [...document.querySelectorAll('button, a[href], [role=button]')].filter(el => !named(el)).length,
    unlabelled_fields: fields.filter(f => !labelled(f)).length,
    lang: document.documentElement.getAttribute('lang') || '',
    page_height: document.documentElement.scrollHeight
  };
})()"""


def check_line(name, checks, errors):
    flags = [f"overflow {checks['overflow_px']}px", f"h1 {checks['h1']}", f"console errors {len(errors)}",
             f"broken images {len(checks['broken_images'])}", f"img without alt {checks['images_without_alt']}",
             f"unnamed controls {checks['unnamed_controls']}", f"unlabelled fields {checks['unlabelled_fields']}"]
    if not checks["lang"]:
        flags.append("no lang attribute")
    return f"{name}: " + " | ".join(flags)


def capture(browser, target, out, width, height, full=False, dark=False, reduced=False, scale=1.0, js=None, wait=800):
    browser.open(to_url(target), width, height, scale, dark, reduced)
    time.sleep(wait / 1000)
    browser.evaluate(SETTLE_JS)
    if js:
        browser.evaluate(f"(async () => {{ {js} }})()")
        time.sleep(0.4)
    checks = browser.evaluate(CHECK_JS)
    errors = browser.console_errors()
    path = browser.screenshot(out, full=full, scale=scale)
    return path, checks, errors


def cmd_shot(args):
    b = Browser()
    try:
        path, checks, errors = capture(b, args.input, args.out, args.width, args.height, args.full, args.dark,
                                       args.reduced_motion, args.scale, args.eval, args.wait)
    finally:
        b.close()
    print(f"{path}  ({args.width}px wide{', dark' if args.dark else ''}{', full page' if args.full else ''})")
    print(check_line(f"w{args.width}", checks, errors))
    for e in errors:
        print(f"  console: {e}")


def cmd_responsive(args):
    outdir = pathlib.Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    suffix = "-dark" if args.dark else ""
    report = {}
    b = Browser()
    try:
        for w, h in ((375, 812), (768, 1024), (1280, 800), (1536, 864)):
            path, checks, errors = capture(b, args.input, outdir / f"w{w}{suffix}.png", w, h, True, args.dark,
                                           args.reduced_motion, 1.0, args.eval, args.wait)
            checks["console_errors"] = errors
            report[f"w{w}{suffix}"] = checks
            print(path)
            print("  " + check_line(f"w{w}", checks, errors))
    finally:
        b.close()
    (outdir / f"report{suffix}.json").write_text(json.dumps(report, indent=2), encoding="utf-8")


LOGO_TEMPLATE = """<!doctype html><meta charset="utf-8"><style>
body{{margin:0;padding:24px;font:12px/1.4 system-ui,sans-serif;background:#fff;color:#222}}
h2{{font-size:13px;margin:18px 0 8px}} .row{{display:flex;gap:12px;flex-wrap:wrap;align-items:stretch}}
.cell{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:16px;
min-width:120px;border:1px solid #ddd}} .cell span{{font-size:11px;opacity:.7}}
img{{display:block}} .black img{{filter:brightness(0)}} .white img{{filter:brightness(0) invert(1)}}
.ondark span{{color:#eee}} canvas{{image-rendering:pixelated;border:1px dashed rgba(128,128,128,.5)}}
</style>
<h2>Sizes on grounds</h2>
{rows}
<h2>One colour{onecolour_note}</h2>
<div class="row">{onecolour}</div>
<h2>Actual 16 and 32 px rasters, enlarged (look for clogged joins, lost gaps, letters that misread)</h2>
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
img.src = "mark.svg";
</script>"""


def cmd_logo_sheet(args):
    svg = pathlib.Path(args.svg).resolve()
    if not svg.exists():
        sys.exit(f"not found: {svg}")
    # Stage inputs in a short folder: Chrome on Windows cannot load file:// paths over 260 characters.
    stage = pathlib.Path(tempfile.mkdtemp(prefix="sheet"))
    shutil.copy(svg, stage / "mark.svg")
    grounds = [("light", args.ground), ("dark", args.dark)] + ([("brand", args.brand)] if args.brand else [])
    rows = []
    for label, color in grounds:
        cls = "cell" if label == "light" else "cell ondark"
        rows.append('<div class="row">' + "".join(
            f'<div class="{cls}" style="background:{html.escape(color)}"><img src="mark.svg" style="height:{size}px">'
            f'<span>{label}, {size}px</span></div>' for size in (160, 64, 32, 16)) + "</div>")
    if args.onecolour:
        shutil.copy(pathlib.Path(args.onecolour).resolve(), stage / "one.svg")
        note = " (the real one-colour master, drawn with currentColor)"
        onecolour = "".join(
            f'<div class="cell{" ondark" if bg == args.dark else ""}" style="background:{html.escape(bg)};color:{fg}">'
            f'<span style="display:block;height:{h}px;width:{h}px;background:{fg};-webkit-mask:url(one.svg) center/contain no-repeat;'
            f'mask:url(one.svg) center/contain no-repeat;opacity:1"></span><span>{label}, {h}</span></div>'
            for bg, fg, label, h in ((args.ground, "#000", "black", 96), (args.ground, "#000", "black", 24),
                                     (args.dark, "#fff", "white", 96), (args.dark, "#fff", "white", 24)))
    else:
        note = " (simulated by a filter: also check the real one-colour file with --onecolour)"
        onecolour = "".join(
            f'<div class="cell {cls}" style="background:{html.escape(bg)}"><img src="mark.svg" style="height:{h}px"><span>{label}, {h}</span></div>'
            for bg, cls, label, h in ((args.ground, "black", "black", 96), (args.ground, "black", "black", 24),
                                      (args.dark, "white ondark", "white", 96), (args.dark, "white ondark", "white", 24)))
    wordmark = ""
    if args.wordmark:
        shutil.copy(pathlib.Path(args.wordmark).resolve(), stage / "wordmark.svg")
        wordmark = ("<h2>Lockup / wordmark</h2><div class='row'>" + "".join(
            f'<div class="cell{" ondark" if c == args.dark else ""}" style="background:{html.escape(c)}">'
            f'<img src="wordmark.svg" style="height:{h}px"><span>{h}px high</span></div>'
            for c, h in ((args.ground, 64), (args.ground, 20), (args.dark, 20))) + "</div>")
    page = LOGO_TEMPLATE.format(rows="".join(rows), ground=html.escape(args.ground), dark=html.escape(args.dark),
                                wordmark=wordmark, onecolour=onecolour, onecolour_note=note)
    (stage / "sheet.html").write_text(page, encoding="utf-8")
    b = Browser()
    try:
        b.open((stage / "sheet.html").as_uri(), 1100, 900, mobile=False)
        time.sleep(0.6)
        out = b.screenshot(args.out, full=True)
    finally:
        b.close()
        shutil.rmtree(stage, ignore_errors=True)
    print(out)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--dark", action="store_true", help="emulate prefers-color-scheme: dark")
    common.add_argument("--reduced-motion", action="store_true", help="emulate prefers-reduced-motion: reduce")
    common.add_argument("--eval", help="JavaScript to run before the capture (state hook)")
    common.add_argument("--wait", type=int, default=800, help="extra milliseconds after load")
    s = sub.add_parser("shot", parents=[common])
    s.add_argument("input"); s.add_argument("--out", required=True)
    s.add_argument("--width", type=int, default=1280); s.add_argument("--height", type=int, default=900)
    s.add_argument("--full", action="store_true", help="capture the whole page height")
    s.add_argument("--scale", type=float, default=1.0)
    s.set_defaults(fn=cmd_shot)
    s = sub.add_parser("responsive", parents=[common])
    s.add_argument("input"); s.add_argument("--outdir", required=True)
    s.set_defaults(fn=cmd_responsive)
    s = sub.add_parser("logo-sheet")
    s.add_argument("svg"); s.add_argument("--out", required=True)
    s.add_argument("--ground", default="#F7F7F5"); s.add_argument("--dark", default="#141414")
    s.add_argument("--brand"); s.add_argument("--wordmark"); s.add_argument("--onecolour")
    s.set_defaults(fn=cmd_logo_sheet)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
