#!/usr/bin/env python3
"""Colour arithmetic for brand and UI work. Standard library only.

Commands (run with --help on any):
  info      HEX...                      hex, rgb, OKLCH, contrast on white and black
  contrast  FG BG [FG BG ...]           WCAG 2.2 ratio with AA text / large / UI verdicts
  ramp      HEX [--name N] [--css]      11-step OKLCH ramp (50..950); the anchor step keeps the exact hex
  compare   HEX --against HEX...        CIEDE2000 distance to competitor colours (confusion check)
  cvd       HEX HEX...                  pairwise distance under protan / deutan / tritan simulation
  audit     FILE.json                   check every declared pair of a palette (see audit --help)

Thresholds used (state them as practice, not science):
  contrast: text 4.5, large text 3.0, UI parts and graphics 3.0 (WCAG 2.2 SC 1.4.3 / 1.4.11)
  confusion: dE2000 < 10 = same colour to a shopper, 10-20 borderline
  cvd: dE2000 < 10 under a simulation = pair is not distinguishable by colour alone
"""
import argparse
import json
import math
import re
import sys

# ---------- conversions ----------

def parse_hex(value):
    v = value.strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", v):
        raise ValueError(f"not a hex colour: {value}")
    return tuple(int(v[i:i + 2], 16) / 255 for i in (0, 2, 4))


def to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def rgb_to_oklab(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_linear(lab):
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def rgb_to_oklch(rgb):
    L, a, b = rgb_to_oklab(rgb)
    C = math.hypot(a, b)
    H = math.degrees(math.atan2(b, a)) % 360 if C > 1e-4 else 0.0
    return L, C, H


def oklch_to_rgb(L, C, H):
    """OKLCH to sRGB, reducing chroma until the colour fits the sRGB gamut."""
    def attempt(c):
        a, b = c * math.cos(math.radians(H)), c * math.sin(math.radians(H))
        return oklab_to_linear((L, a, b))

    lin = attempt(C)
    if not all(-1e-6 <= x <= 1 + 1e-6 for x in lin):
        lo, hi = 0.0, C
        for _ in range(30):
            mid = (lo + hi) / 2
            if all(-1e-6 <= x <= 1 + 1e-6 for x in attempt(mid)):
                lo = mid
            else:
                hi = mid
        lin = attempt(lo)
    return tuple(linear_to_srgb(max(0.0, min(1.0, x))) for x in lin)


def fmt_oklch(rgb):
    L, C, H = rgb_to_oklch(rgb)
    return f"oklch({L:.3f} {C:.3f} {H:.1f})"

# ---------- contrast ----------

def luminance(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def verdict(ratio, kind="text"):
    need = {"text": 4.5, "large": 3.0, "ui": 3.0}[kind]
    return "PASS" if ratio >= need else "FAIL"

# ---------- CIEDE2000 ----------

def rgb_to_lab(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.0
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116

    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e2000(rgb1, rgb2):
    L1, a1, b1 = rgb_to_lab(rgb1)
    L2, a2, b2 = rgb_to_lab(rgb2)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360 if C1p else 0
    h2p = math.degrees(math.atan2(b2, a2p)) % 360 if C2p else 0
    dLp, dCp = L2 - L1, C2p - C1p
    if C1p * C2p == 0:
        dhp = 0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    elif h2p - h1p > 180:
        dhp = h2p - h1p - 360
    else:
        dhp = h2p - h1p + 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dhp / 2))
    Lpm, Cpm = (L1 + L2) / 2, (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hpm = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hpm = (h1p + h2p + 360) / 2
    else:
        hpm = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hpm - 30)) + 0.24 * math.cos(math.radians(2 * hpm))
         + 0.32 * math.cos(math.radians(3 * hpm + 6)) - 0.20 * math.cos(math.radians(4 * hpm - 63)))
    dtheta = 30 * math.exp(-(((hpm - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    Sl = 1 + (0.015 * (Lpm - 50) ** 2) / math.sqrt(20 + (Lpm - 50) ** 2)
    Sc = 1 + 0.045 * Cpm
    Sh = 1 + 0.015 * Cpm * T
    Rt = -math.sin(math.radians(2 * dtheta)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))

# ---------- colour vision deficiency (Machado et al. 2009, severity 1.0) ----------

CVD = {
    "protan": ((0.152286, 1.052583, -0.204868), (0.114503, 0.786281, 0.099216), (-0.003882, -0.048116, 1.051998)),
    "deutan": ((0.367322, 0.860646, -0.227968), (0.280085, 0.672501, 0.047413), (-0.011820, 0.042940, 0.968881)),
    "tritan": ((1.255528, -0.076749, -0.178779), (-0.078411, 0.930809, 0.147602), (0.004733, 0.691367, 0.303900)),
}


def simulate(rgb, kind):
    lin = [srgb_to_linear(c) for c in rgb]
    out = [sum(row[i] * lin[i] for i in range(3)) for row in CVD[kind]]
    return tuple(linear_to_srgb(max(0.0, min(1.0, x))) for x in out)

# ---------- ramp ----------

STEPS = (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)
TARGET_L = (0.975, 0.945, 0.885, 0.810, 0.720, 0.635, 0.555, 0.475, 0.395, 0.315, 0.250)


def build_ramp(rgb):
    L, C, H = rgb_to_oklch(rgb)
    anchor = min(range(len(TARGET_L)), key=lambda i: abs(TARGET_L[i] - L))
    shift = L - TARGET_L[anchor]
    ramp = []
    for i, tl in enumerate(TARGET_L):
        if i == anchor:
            ramp.append((STEPS[i], rgb, True))
            continue
        # follow the anchor's offset near it, fade the offset toward the ends
        li = max(0.12, min(0.985, tl + shift * max(0.0, 1 - abs(i - anchor) / 4)))
        # chroma tapers toward very light and very dark steps to stay in gamut and calm
        edge = min(li, 1 - li)
        ci = C * min(1.0, edge / 0.25) if edge < 0.25 else C
        ramp.append((STEPS[i], oklch_to_rgb(li, ci, H), False))
    return ramp

# ---------- commands ----------

WHITE, BLACK = (1.0, 1.0, 1.0), (0.0, 0.0, 0.0)


def cmd_info(args):
    for h in args.colors:
        rgb = parse_hex(h)
        r, g, b = (round(c * 255) for c in rgb)
        print(f"{to_hex(rgb)}  rgb({r} {g} {b})  {fmt_oklch(rgb)}  "
              f"on white {contrast_ratio(rgb, WHITE):.2f}:1  on black {contrast_ratio(rgb, BLACK):.2f}:1")


def cmd_contrast(args):
    if len(args.colors) % 2:
        sys.exit("give colours in FG BG pairs")
    for fg, bg in zip(args.colors[::2], args.colors[1::2]):
        ratio = contrast_ratio(parse_hex(fg), parse_hex(bg))
        print(f"{fg.upper():>8} on {bg.upper():<8} {ratio:5.2f}:1  text {verdict(ratio)}  "
              f"large {verdict(ratio, 'large')}  ui {verdict(ratio, 'ui')}")


def cmd_ramp(args):
    rgb = parse_hex(args.color)
    name = args.name
    rows = build_ramp(rgb)
    if args.css:
        for step, c, _ in rows:
            print(f"  --{name}-{step}: {fmt_oklch(c)}; /* {to_hex(c)} */")
        return
    print(f"{'step':>5}  {'hex':8}  {'oklch':26}  {'vs white':>8}  {'vs black':>8}")
    for step, c, anchor in rows:
        mark = "  <- anchor (exact brand hex)" if anchor else ""
        print(f"{step:>5}  {to_hex(c)}  {fmt_oklch(c):26}  {contrast_ratio(c, WHITE):7.2f}  "
              f"{contrast_ratio(c, BLACK):7.2f}{mark}")


def cmd_compare(args):
    base = parse_hex(args.color)
    bL, bC, bH = rgb_to_oklch(base)
    for other in args.against:
        o = parse_hex(other)
        de = delta_e2000(base, o)
        oL, oC, oH = rgb_to_oklch(o)
        dh = abs((bH - oH + 180) % 360 - 180)
        same_family = bC > 0.04 and oC > 0.04 and dh <= 20 and abs(bL - oL) <= 0.08
        label = "SAME COLOUR" if de < 10 or same_family else ("borderline" if de < 20 else "distinct")
        print(f"{args.color.upper()} vs {other.upper()}: dE2000 {de:5.1f}  dHue {dh:5.1f}  dL {bL - oL:+.3f}  -> {label}")


def cmd_cvd(args):
    cols = [(h.upper(), parse_hex(h)) for h in args.colors]
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            (n1, c1), (n2, c2) = cols[i], cols[j]
            parts = [f"normal {delta_e2000(c1, c2):5.1f}"]
            flags = []
            for kind in CVD:
                de = delta_e2000(simulate(c1, kind), simulate(c2, kind))
                parts.append(f"{kind} {de:5.1f}")
                if de < 10:
                    flags.append(kind)
            note = f"  CONFUSABLE for {', '.join(flags)}: add lightness difference, icon or label" if flags else ""
            print(f"{n1} / {n2}: " + "  ".join(parts) + note)


def cmd_audit(args):
    with open(args.file, encoding="utf-8") as fh:
        spec = json.load(fh)
    colors = {k: parse_hex(v) for k, v in spec["colors"].items()}
    failures = 0
    for pair in spec["pairs"]:
        fg, bg, kind = pair[0], pair[1], (pair[2] if len(pair) > 2 else "text")
        ratio = contrast_ratio(colors[fg], colors[bg])
        result = verdict(ratio, kind)
        failures += result == "FAIL"
        print(f"{result}  {fg} on {bg} ({kind}): {ratio:.2f}:1")
    print(f"\n{len(spec['pairs']) - failures}/{len(spec['pairs'])} pairs pass")
    sys.exit(1 if failures else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("info"); s.add_argument("colors", nargs="+"); s.set_defaults(fn=cmd_info)
    s = sub.add_parser("contrast"); s.add_argument("colors", nargs="+"); s.set_defaults(fn=cmd_contrast)
    s = sub.add_parser("ramp"); s.add_argument("color"); s.add_argument("--name", default="brand")
    s.add_argument("--css", action="store_true", help="print CSS custom properties"); s.set_defaults(fn=cmd_ramp)
    s = sub.add_parser("compare"); s.add_argument("color"); s.add_argument("--against", nargs="+", required=True)
    s.set_defaults(fn=cmd_compare)
    s = sub.add_parser("cvd"); s.add_argument("colors", nargs="+"); s.set_defaults(fn=cmd_cvd)
    s = sub.add_parser("audit", description='FILE.json: {"colors": {"text": "#1A1D1F", "bg": "#FFFFFF"}, '
                       '"pairs": [["text", "bg", "text"], ["border", "bg", "ui"]]}; kind is text | large | ui')
    s.add_argument("file"); s.set_defaults(fn=cmd_audit)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
