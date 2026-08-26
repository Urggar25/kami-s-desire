#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_hack_assets.py
====================
Genere le kit graphique et sonore du minijeu de hacking du jour 9.

Images  -> game/minijeu/hack/assets/
Sons    -> game/minijeu/hack/audio/

Tout est procedural (Pillow + numpy) : le script est idempotent, on peut
le relancer pour retoucher la charte sans casser le reste du projet.

Usage :
    python tools/build_hack_assets.py
"""

import math
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "game" / "minijeu" / "hack" / "assets"
SND_DIR = ROOT / "game" / "minijeu" / "hack" / "audio"
FONT_PATH = ROOT / "game" / "fonts" / "Rajdhani-SemiBold.ttf"

IMG_DIR.mkdir(parents=True, exist_ok=True)
SND_DIR.mkdir(parents=True, exist_ok=True)

SS = 4                      # supersampling des tuiles
TILE = 192                  # taille finale d'une tuile
RATE = 44100

# ---------------------------------------------------------------------------
# Charte
# ---------------------------------------------------------------------------
CYAN = (0x4A, 0xE3, 0xFF)
CYAN_DEEP = (0x12, 0x6E, 0x96)
ICE = (0xE4, 0xFA, 0xFF)
RED = (0xFF, 0x3D, 0x5C)
RED_DEEP = (0x8C, 0x12, 0x28)
AMBER = (0xFF, 0xA5, 0x3D)
VIOLET = (0xB6, 0x72, 0xFF)
MINT = (0x5C, 0xFF, 0xC0)


# ---------------------------------------------------------------------------
# Helpers image
# ---------------------------------------------------------------------------
def mask(size):
    return Image.new("L", size, 0)


def rgba(size, color=(0, 0, 0, 0)):
    return Image.new("RGBA", size, color)


def stamp(base, m, color, alpha=255):
    """Colorise un masque L et le compose sur base."""
    layer = Image.new("RGBA", base.size, tuple(color) + (0,))
    a = m if alpha >= 255 else m.point(lambda v: v * alpha // 255)
    layer.putalpha(a)
    return Image.alpha_composite(base, layer)


def glow(base, m, color, radius, strength=1.0, alpha=255):
    """Ajoute une lueur douce issue d'un masque."""
    g = m.filter(ImageFilter.GaussianBlur(radius))
    g = g.point(lambda v: min(255, int(v * strength)))
    return stamp(base, g, color, alpha)


def vgrad(size, top, bottom):
    """Degrade vertical RGBA opaque."""
    w, h = size
    ramp = np.linspace(0.0, 1.0, h, dtype=np.float32)
    top = np.array(top, dtype=np.float32)
    bottom = np.array(bottom, dtype=np.float32)
    col = top[None, :] * (1.0 - ramp[:, None]) + bottom[None, :] * ramp[:, None]
    out = np.zeros((h, w, 4), dtype=np.uint8)
    out[:, :, :3] = np.repeat(col.astype(np.uint8)[:, None, :], w, axis=1)
    out[:, :, 3] = 255
    return Image.fromarray(out, "RGBA")


def chamfer(x0, y0, x1, y1, c, corners=(1, 1, 1, 1)):
    """Polygone rectangulaire a coins coupes (tl, tr, br, bl)."""
    tl, tr, br, bl = corners
    pts = []
    pts += [(x0 + c, y0)] if tl else [(x0, y0)]
    pts += [(x1 - c, y0), (x1, y0 + c)] if tr else [(x1, y0)]
    pts += [(x1, y1 - c), (x1 - c, y1)] if br else [(x1, y1)]
    pts += [(x0 + c, y1), (x0, y1 - c)] if bl else [(x0, y1)]
    if tl:
        pts += [(x0, y0 + c)]
    return pts


def poly_star(cx, cy, r_out, r_in, points, rot=0.0):
    pts = []
    for i in range(points * 2):
        r = r_out if i % 2 == 0 else r_in
        a = rot + i * math.pi / points
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def hexagon(cx, cy, r, rot=math.pi / 6):
    return [(cx + r * math.cos(rot + i * math.pi / 3),
             cy + r * math.sin(rot + i * math.pi / 3)) for i in range(6)]


def finish(img, size=TILE):
    return img.resize((size, size), Image.LANCZOS)


def save(img, name):
    path = IMG_DIR / name
    img.save(path, "PNG", optimize=True)
    print("  img  {:<26} {}".format(name, img.size))


# ---------------------------------------------------------------------------
# Tuiles
# ---------------------------------------------------------------------------
S = TILE * SS          # canvas de travail
M = int(S * 0.045)     # marge


def tile_floor():
    """Couloir : creux, presque noir, pour trancher avec les modules."""
    img = rgba((S, S))
    gap = int(S * 0.018)
    m = mask((S, S))
    d = ImageDraw.Draw(m)
    d.rectangle((gap, gap, S - gap, S - gap), fill=255)
    plate = vgrad((S, S), (0x06, 0x0D, 0x15), (0x03, 0x08, 0x0E))
    plate.putalpha(m.point(lambda v: v * 242 // 255))
    img = Image.alpha_composite(img, plate)

    line = mask((S, S))
    dl = ImageDraw.Draw(line)
    dl.rectangle((gap, gap, S - gap, S - gap), outline=255, width=int(S * 0.006))
    img = stamp(img, line, (0x0C, 0x22, 0x30), 190)

    dot = mask((S, S))
    dd = ImageDraw.Draw(dot)
    c = S // 2
    r = int(S * 0.016)
    dd.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = stamp(img, dot, (0x18, 0x44, 0x5C), 150)
    return finish(img)


def tile_wall(variant=0):
    img = rgba((S, S))
    body = mask((S, S))
    d = ImageDraw.Draw(body)
    pad = int(S * 0.02)
    cut = int(S * 0.14)
    d.polygon(chamfer(pad, pad, S - pad, S - pad, cut), fill=255)

    img = glow(img, body, CYAN_DEEP, S * 0.05, 0.55, 130)

    plate = vgrad((S, S), (0x26, 0x58, 0x78), (0x0C, 0x22, 0x34))
    plate.putalpha(body)
    img = Image.alpha_composite(img, plate)

    inner = mask((S, S))
    di = ImageDraw.Draw(inner)
    p2 = int(S * 0.10)
    di.polygon(chamfer(p2, p2, S - p2, S - p2, int(cut * 0.62)), fill=255)
    plate2 = vgrad((S, S), (0x14, 0x33, 0x49), (0x09, 0x1B, 0x28))
    plate2.putalpha(inner)
    img = Image.alpha_composite(img, plate2)

    edge = mask((S, S))
    de = ImageDraw.Draw(edge)
    de.polygon(chamfer(pad, pad, S - pad, S - pad, cut), outline=255, width=int(S * 0.014))
    img = glow(img, edge, CYAN, S * 0.022, 1.0, 115)
    img = stamp(img, edge, (0x58, 0xBE, 0xE4), 235)

    circ = mask((S, S))
    dc = ImageDraw.Draw(circ)
    w = int(S * 0.011)
    c = S // 2
    if variant == 0:
        dc.line([(c, int(S * 0.22)), (c, int(S * 0.78))], fill=255, width=w)
        dc.line([(int(S * 0.30), c), (int(S * 0.70), c)], fill=255, width=w)
        r = int(S * 0.05)
        dc.ellipse((c - r, c - r, c + r, c + r), outline=255, width=w)
    elif variant == 1:
        dc.line([(int(S * 0.22), int(S * 0.36)), (int(S * 0.62), int(S * 0.36)),
                 (int(S * 0.78), int(S * 0.52))], fill=255, width=w)
        dc.line([(int(S * 0.22), int(S * 0.66)), (int(S * 0.52), int(S * 0.66))], fill=255, width=w)
        for px, py in ((0.22, 0.36), (0.78, 0.52), (0.52, 0.66)):
            r = int(S * 0.028)
            dc.ellipse((int(S * px) - r, int(S * py) - r, int(S * px) + r, int(S * py) + r), fill=255)
    else:
        dc.polygon(hexagon(c, c, int(S * 0.20)), outline=255, width=w)
        dc.polygon(hexagon(c, c, int(S * 0.10)), fill=255)
    img = glow(img, circ, CYAN, S * 0.018, 0.8, 120)
    img = stamp(img, circ, (0x6E, 0xD8, 0xF8), 200)

    led = mask((S, S))
    dl = ImageDraw.Draw(led)
    r = int(S * 0.022)
    for px, py in ((0.16, 0.16), (0.84, 0.16), (0.16, 0.84), (0.84, 0.84)):
        dl.ellipse((int(S * px) - r, int(S * py) - r, int(S * px) + r, int(S * py) + r), fill=255)
    img = glow(img, led, CYAN, S * 0.03, 1.2, 150)
    img = stamp(img, led, ICE, 235)
    return finish(img)


def _icon_plate(accent, deep):
    """Les modules sont des glyphes poses sur le couloir, pas des panneaux :
    le plateau reste lisible (couloirs sombres, murs en relief)."""
    img = rgba((S, S))
    m = mask((S, S))
    d = ImageDraw.Draw(m)
    c = S // 2
    r = int(S * 0.33)
    d.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, m, deep, S * 0.11, 0.60, 135)
    return img


def tile_goal():
    img = _icon_plate(MINT, (0x0E, 0x6B, 0x52))
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    d.polygon(hexagon(c, c, int(S * 0.35)), outline=255, width=int(S * 0.013))
    r_in = int(S * 0.215)
    d.ellipse((c - r_in, c - r_in, c + r_in, c + r_in), outline=255, width=int(S * 0.011))
    for i in range(6):
        a = math.pi / 6 + i * math.pi / 3
        d.line([(c + r_in * math.cos(a), c + r_in * math.sin(a)),
                (c + int(S * 0.35) * math.cos(a), c + int(S * 0.35) * math.sin(a))],
               fill=255, width=int(S * 0.010))
    img = glow(img, art, MINT, S * 0.03, 1.0, 150)
    img = stamp(img, art, (0x9C, 0xFF, 0xE0), 225)

    core = mask((S, S))
    dc = ImageDraw.Draw(core)
    r = int(S * 0.115)
    dc.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, core, MINT, S * 0.075, 1.5, 210)
    img = stamp(img, core, (0xEA, 0xFF, 0xF6), 255)
    return finish(img)


def tile_oneway():
    """Fleche vers le HAUT (pivotee dans le moteur)."""
    img = _icon_plate(CYAN, CYAN_DEEP)
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    for k, off in enumerate((0.30, 0.10, -0.10)):
        y = c + int(S * off)
        w = int(S * (0.20 - k * 0.012))
        d.line([(c - w, y), (c, y - int(S * 0.10)), (c + w, y)],
               fill=255, width=int(S * 0.024), joint="curve")
    d.line([(c - int(S * 0.24), c + int(S * 0.36)), (c + int(S * 0.24), c + int(S * 0.36))],
           fill=255, width=int(S * 0.014))
    img = glow(img, art, CYAN, S * 0.035, 1.15, 165)
    img = stamp(img, art, ICE, 240)
    return finish(img)


def tile_firewall(locked=True):
    accent = VIOLET if locked else MINT
    deep = (0x4A, 0x1E, 0x8C) if locked else (0x0E, 0x6B, 0x52)
    img = _icon_plate(accent, deep)
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    d.polygon(hexagon(c, c, int(S * 0.36), rot=0.0), outline=255, width=int(S * 0.013))
    bw = int(S * 0.125)
    d.rounded_rectangle((c - bw, c, c + bw, c + int(S * 0.155)),
                        radius=int(S * 0.018), outline=255, width=int(S * 0.016))
    if locked:
        d.arc((c - int(S * 0.085), c - int(S * 0.155), c + int(S * 0.085), c + int(S * 0.015)),
              180, 360, fill=255, width=int(S * 0.016))
    else:
        d.arc((c - int(S * 0.175), c - int(S * 0.155), c - int(S * 0.005), c + int(S * 0.015)),
              180, 335, fill=255, width=int(S * 0.016))
    r = int(S * 0.020)
    d.ellipse((c - r, c + int(S * 0.070) - r, c + r, c + int(S * 0.070) + r), fill=255)
    for i in range(4):
        x = c + int(S * (-0.113 + i * 0.075))
        y = c + int(S * 0.245)
        s = int(S * 0.024)
        d.rectangle((x - s, y - s, x + s, y + s), outline=255, width=int(S * 0.009))
    img = glow(img, art, accent, S * 0.033, 1.1, 160)
    img = stamp(img, art, (0xF2, 0xE6, 0xFF) if locked else (0xDD, 0xFF, 0xF2), 235)
    return finish(img)


def tile_beacon():
    img = _icon_plate(AMBER, (0x8C, 0x53, 0x10))
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    base_y = c + int(S * 0.26)
    d.polygon([(c - int(S * 0.12), base_y), (c + int(S * 0.12), base_y),
               (c + int(S * 0.07), base_y - int(S * 0.09)), (c - int(S * 0.07), base_y - int(S * 0.09))],
              outline=255, width=int(S * 0.014))
    for i, r in enumerate((0.13, 0.21, 0.29)):
        d.arc((c - int(S * r), base_y - int(S * (0.09 + r)),
               c + int(S * r), base_y - int(S * (0.09 - r))),
              200, 340, fill=255, width=int(S * (0.014 - i * 0.002)))
    d.ellipse((c - int(S * 0.035), base_y - int(S * 0.135),
               c + int(S * 0.035), base_y - int(S * 0.065)), fill=255)
    img = glow(img, art, AMBER, S * 0.035, 1.15, 170)
    img = stamp(img, art, (0xFF, 0xE9, 0xC4), 240)
    return finish(img)


def tile_boost():
    img = _icon_plate(CYAN, CYAN_DEEP)
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    r = int(S * 0.31)
    d.ellipse((c - r, c - r, c + r, c + r), outline=255, width=int(S * 0.011))
    for i in range(8):
        a = i * math.pi / 4 + math.pi / 8
        d.line([(c + int(S * 0.34) * math.cos(a), c + int(S * 0.34) * math.sin(a)),
                (c + int(S * 0.42) * math.cos(a), c + int(S * 0.42) * math.sin(a))],
               fill=255, width=int(S * 0.014))
    for k, off in enumerate((-0.17, 0.01, 0.19)):
        x = c + int(S * off)
        h = int(S * (0.19 - k * 0.015))
        d.line([(x - int(S * 0.055), c - h), (x + int(S * 0.075), c), (x - int(S * 0.055), c + h)],
               fill=255, width=int(S * 0.026), joint="curve")
    img = glow(img, art, CYAN, S * 0.038, 1.25, 185)
    img = stamp(img, art, ICE, 245)
    return finish(img)


def tile_trap():
    img = _icon_plate(RED, RED_DEEP)
    c = S // 2
    art = mask((S, S))
    d = ImageDraw.Draw(art)
    d.polygon(poly_star(c, c, int(S * 0.38), int(S * 0.235), 8, rot=math.pi / 8),
              outline=255, width=int(S * 0.015))
    r = int(S * 0.20)
    d.ellipse((c - r, c - r, c + r, c + r), outline=255, width=int(S * 0.013))
    for i in range(4):
        a = i * math.pi / 2 + math.pi / 4
        d.line([(c + int(S * 0.07) * math.cos(a), c + int(S * 0.07) * math.sin(a)),
                (c + int(S * 0.18) * math.cos(a), c + int(S * 0.18) * math.sin(a))],
               fill=255, width=int(S * 0.012))
    img = glow(img, art, RED, S * 0.035, 1.1, 175)
    img = stamp(img, art, (0xFF, 0xC9, 0xD2), 240)

    core = mask((S, S))
    dc = ImageDraw.Draw(core)
    r = int(S * 0.06)
    dc.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, core, RED, S * 0.07, 1.5, 210)
    img = stamp(img, core, (0xFF, 0xEC, 0xEF), 255)
    return finish(img)


# ---------------------------------------------------------------------------
# Jetons
# ---------------------------------------------------------------------------
def token_player():
    img = rgba((S, S))
    c = S // 2
    halo = mask((S, S))
    dh = ImageDraw.Draw(halo)
    r = int(S * 0.30)
    dh.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, halo, CYAN, S * 0.10, 0.75, 170)

    art = mask((S, S))
    d = ImageDraw.Draw(art)
    ro = int(S * 0.40)
    for i in range(4):
        d.arc((c - ro, c - ro, c + ro, c + ro), i * 90 + 12, i * 90 + 68,
              fill=255, width=int(S * 0.020))
    ri = int(S * 0.29)
    d.ellipse((c - ri, c - ri, c + ri, c + ri), outline=255, width=int(S * 0.013))
    d.polygon([(c, c - int(S * 0.22)), (c + int(S * 0.19), c + int(S * 0.13)),
               (c - int(S * 0.19), c + int(S * 0.13))], outline=255, width=int(S * 0.018))
    img = glow(img, art, CYAN, S * 0.03, 1.2, 200)
    img = stamp(img, art, ICE, 250)

    core = mask((S, S))
    dc = ImageDraw.Draw(core)
    r = int(S * 0.085)
    dc.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, core, (0xB6, 0xF3, 0xFF), S * 0.085, 1.7, 235)
    img = stamp(img, core, (0xFF, 0xFF, 0xFF), 255)
    return finish(img)


def token_enemy():
    """Sentinelle : losange anguleux, silhouette distincte des pieges."""
    img = rgba((S, S))
    c = S // 2
    halo = mask((S, S))
    dh = ImageDraw.Draw(halo)
    r = int(S * 0.30)
    dh.ellipse((c - r, c - r, c + r, c + r), fill=255)
    img = glow(img, halo, RED, S * 0.10, 0.85, 180)

    art = mask((S, S))
    d = ImageDraw.Draw(art)
    outer = [(c, c - int(S * 0.42)), (c + int(S * 0.31), c),
             (c, c + int(S * 0.42)), (c - int(S * 0.31), c)]
    d.polygon(outer, outline=255, width=int(S * 0.020))
    inner = [(c, c - int(S * 0.24)), (c + int(S * 0.18), c),
             (c, c + int(S * 0.24)), (c - int(S * 0.18), c)]
    d.polygon(inner, outline=255, width=int(S * 0.013))
    # ailerons lateraux
    for sx in (-1, 1):
        d.line([(c + sx * int(S * 0.33), c - int(S * 0.10)),
                (c + sx * int(S * 0.44), c),
                (c + sx * int(S * 0.33), c + int(S * 0.10))],
               fill=255, width=int(S * 0.015), joint="curve")
    # fente optique
    d.polygon([(c - int(S * 0.135), c), (c, c - int(S * 0.062)),
               (c + int(S * 0.135), c), (c, c + int(S * 0.062))], fill=255)
    img = glow(img, art, RED, S * 0.032, 1.25, 215)
    img = stamp(img, art, (0xFF, 0xB8, 0xC4), 250)

    core = mask((S, S))
    dc = ImageDraw.Draw(core)
    dc.ellipse((c - int(S * 0.040), c - int(S * 0.024),
                c + int(S * 0.040), c + int(S * 0.024)), fill=255)
    img = glow(img, core, (0xFF, 0x6C, 0x82), S * 0.085, 1.8, 240)
    img = stamp(img, core, (0xFF, 0xF0, 0xF2), 255)
    return finish(img)


def radial_glow(color, size=256, power=2.2):
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    c = (size - 1) / 2.0
    r = np.sqrt((xx - c) ** 2 + (yy - c) ** 2) / c
    a = np.clip(1.0 - r, 0.0, 1.0) ** power
    out = np.zeros((size, size, 4), dtype=np.uint8)
    out[:, :, 0] = color[0]
    out[:, :, 1] = color[1]
    out[:, :, 2] = color[2]
    out[:, :, 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


# ---------------------------------------------------------------------------
# Habillage plein ecran
# ---------------------------------------------------------------------------
W, H = 1920, 1080


def font(size):
    try:
        return ImageFont.truetype(str(FONT_PATH), size)
    except Exception:
        return ImageFont.load_default()


def bezel():
    img = rgba((W, H))

    inner = (30, 22, W - 30, H - 22)
    cut = 46
    hole = chamfer(inner[0], inner[1], inner[2], inner[3], cut)

    frame = mask((W, H))
    df = ImageDraw.Draw(frame)
    df.rectangle((0, 0, W, H), fill=255)
    df.polygon(hole, fill=0)
    img = stamp(img, frame, (0x03, 0x06, 0x0A), 255)

    bev = mask((W, H))
    db = ImageDraw.Draw(bev)
    db.rectangle((6, 4, W - 6, H - 4), outline=255, width=3)
    img = stamp(img, bev, (0x11, 0x2A, 0x3A), 190)

    stroke = mask((W, H))
    ds = ImageDraw.Draw(stroke)
    ds.polygon(hole, outline=255, width=3)
    img = glow(img, stroke, CYAN, 9, 0.8, 130)
    img = stamp(img, stroke, (0x3D, 0xD2, 0xFF), 225)

    stroke2 = mask((W, H))
    ds2 = ImageDraw.Draw(stroke2)
    ds2.polygon(chamfer(inner[0] - 12, inner[1] - 10, inner[2] + 12, inner[3] + 10, cut + 8),
                outline=255, width=1)
    img = stamp(img, stroke2, (0x1C, 0x6A, 0x8C), 150)

    br = mask((W, H))
    dbr = ImageDraw.Draw(br)
    L = 150
    for (x, y, sy) in ((inner[0], inner[1] + cut, 1), (inner[2], inner[1] + cut, 1),
                       (inner[0], inner[3] - cut, -1), (inner[2], inner[3] - cut, -1)):
        dbr.line([(x, y), (x, y + sy * L)], fill=255, width=5)
    for (x, y, sx) in ((inner[0] + cut, inner[1], 1), (inner[2] - cut, inner[1], -1),
                       (inner[0] + cut, inner[3], 1), (inner[2] - cut, inner[3], -1)):
        dbr.line([(x, y), (x + sx * L, y)], fill=255, width=5)
    img = glow(img, br, AMBER, 10, 0.7, 120)
    img = stamp(img, br, (0xFF, 0x9A, 0x3C), 235)

    tick = mask((W, H))
    dt = ImageDraw.Draw(tick)
    for x in range(inner[0] + 220, inner[2] - 220, 26):
        dt.line([(x, 10), (x, 17)], fill=255, width=2)
        dt.line([(x, H - 10), (x, H - 17)], fill=255, width=2)
    for y in range(inner[1] + 200, inner[3] - 200, 26):
        dt.line([(10, y), (17, y)], fill=255, width=2)
        dt.line([(W - 10, y), (W - 17, y)], fill=255, width=2)
    img = stamp(img, tick, (0x2A, 0x7C, 0xA0), 120)

    d = ImageDraw.Draw(img)
    f = font(15)
    d.text((44, 3), "SDN//INTRUSION.SUITE   v4.11", font=f, fill=(0x4E, 0xA8, 0xC8, 220))
    d.text((W - 320, 3), "CANAL J-09   AES-256   LIVE", font=f, fill=(0x4E, 0xA8, 0xC8, 220))
    d.text((44, H - 21), "TRACE ROUTE // KAMI.SENTINEL", font=f, fill=(0x4E, 0xA8, 0xC8, 200))
    d.text((W - 270, H - 21), "SIGNAL 100%   40 Mbps", font=f, fill=(0xC8, 0x77, 0x36, 210))
    return img


def vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    nx = (xx - W / 2.0) / (W / 2.0)
    ny = (yy - H / 2.0) / (H / 2.0)
    r = np.sqrt(nx ** 2 * 0.86 + ny ** 2)
    a = np.clip((r - 0.42) / 0.78, 0.0, 1.0) ** 1.7
    out = np.zeros((H, W, 4), dtype=np.uint8)
    out[:, :, 3] = (a * 205).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def scanlines():
    out = np.zeros((H, W, 4), dtype=np.uint8)
    out[0::3, :, 3] = 26
    out[1::3, :, 3] = 8
    return Image.fromarray(out, "RGBA")


def grain(size=256, seed=7):
    rng = np.random.default_rng(seed)
    n = rng.integers(0, 255, (size, size)).astype(np.uint8)
    out = np.zeros((size, size, 4), dtype=np.uint8)
    out[:, :, 0] = 140
    out[:, :, 1] = 190
    out[:, :, 2] = 210
    out[:, :, 3] = (n // 9).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def hexfield(size=256):
    """Fond du vide : trame hexagonale tuilable."""
    big = size * 2
    img = rgba((big, big))
    m = mask((big, big))
    d = ImageDraw.Draw(m)
    r = size / 6.0
    dx = r * math.sqrt(3)
    dy = r * 1.5
    row = 0
    y = -dy
    while y < big + dy:
        x = -dx if row % 2 == 0 else -dx / 2
        while x < big + dx:
            d.polygon(hexagon(x, y, r * 0.92, rot=math.pi / 2), outline=255, width=2)
            x += dx
        y += dy
        row += 1
    img = stamp(img, m, (0x14, 0x4E, 0x6B), 46)
    return img.resize((size, size), Image.LANCZOS)


def edge_glow(w=1620, h=760, thickness=110):
    """Lueur interne blanche (teintee au runtime)."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    dist = np.minimum.reduce([xx, yy, (w - 1) - xx, (h - 1) - yy])
    a = np.clip(1.0 - dist / float(thickness), 0.0, 1.0) ** 2.0
    out = np.zeros((h, w, 4), dtype=np.uint8)
    out[:, :, :3] = 255
    out[:, :, 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


def panel(size=160, cut=34, fill=(0x06, 0x14, 0x20, 0xE8), accent=(0x2A, 0x9C, 0xC6, 0xC0)):
    img = rgba((size, size))
    m = mask((size, size))
    d = ImageDraw.Draw(m)
    pts = chamfer(1, 1, size - 1, size - 1, cut, corners=(1, 0, 1, 0))
    d.polygon(pts, fill=255)
    img = stamp(img, m, fill[:3], fill[3])
    o = mask((size, size))
    do = ImageDraw.Draw(o)
    do.polygon(pts, outline=255, width=2)
    img = stamp(img, o, accent[:3], accent[3])
    return img


def bar_gradient(w=1024, h=24):
    stops = [(0.00, (0xFF, 0x22, 0x4C)), (0.18, (0xFF, 0x46, 0x38)),
             (0.42, (0xFF, 0xB0, 0x2E)), (0.68, (0x3C, 0xE0, 0xFF)),
             (1.00, (0x8E, 0xFF, 0xEA))]
    arr = np.zeros((h, w, 4), dtype=np.uint8)
    for x in range(w):
        t = x / float(w - 1)
        col = stops[-1][1]
        for i in range(len(stops) - 1):
            a, ca = stops[i]
            b, cb = stops[i + 1]
            if a <= t <= b:
                k = (t - a) / max(1e-6, b - a)
                col = [int(ca[j] + (cb[j] - ca[j]) * k) for j in range(3)]
                break
        arr[:, x, :3] = col
    arr[:, :, 3] = 255
    img = Image.fromarray(arr, "RGBA")
    sheen = np.zeros((h, w, 4), dtype=np.uint8)
    ramp = (np.abs(np.linspace(-1, 1, h)) ** 2 * 120).astype(np.uint8)
    sheen[:, :, 3] = ramp[:, None]
    return Image.alpha_composite(img, Image.fromarray(sheen, "RGBA"))


def build_images():
    print("Images :")
    save(tile_floor(), "hk_floor.png")
    for i in range(3):
        save(tile_wall(i), "hk_wall_{}.png".format(i))
    save(tile_goal(), "hk_goal.png")
    save(tile_oneway(), "hk_oneway.png")
    save(tile_firewall(True), "hk_firewall.png")
    save(tile_firewall(False), "hk_firewall_open.png")
    save(tile_beacon(), "hk_beacon.png")
    save(tile_boost(), "hk_boost.png")
    save(tile_trap(), "hk_trap.png")
    save(token_player(), "hk_player.png")
    save(token_enemy(), "hk_enemy.png")
    save(radial_glow(CYAN), "hk_glow_cyan.png")
    save(radial_glow(RED), "hk_glow_red.png")
    save(radial_glow(MINT), "hk_glow_mint.png")
    save(radial_glow(VIOLET), "hk_glow_violet.png")
    save(radial_glow(AMBER), "hk_glow_amber.png")
    save(bezel(), "hk_bezel.png")
    save(vignette(), "hk_vignette.png")
    save(scanlines(), "hk_scanlines.png")
    save(grain(), "hk_grain.png")
    save(hexfield(), "hk_hexfield.png")
    save(edge_glow(), "hk_edge.png")
    save(panel(), "hk_panel.png")
    save(panel(accent=(0xC6, 0x2A, 0x4A, 0xC8), fill=(0x18, 0x06, 0x0C, 0xE8)), "hk_panel_red.png")
    save(bar_gradient(), "hk_bar.png")


# ---------------------------------------------------------------------------
# Sons
# ---------------------------------------------------------------------------
RNG = np.random.default_rng(20260826)


def t_axis(dur):
    return np.arange(int(RATE * dur)) / float(RATE)


def env(t, attack=0.005, decay=None, curve=2.0):
    total = t[-1] if len(t) else 1.0
    decay = decay if decay is not None else total
    a = np.clip(t / max(1e-6, attack), 0.0, 1.0)
    r = np.clip((total - t) / max(1e-6, decay), 0.0, 1.0) ** curve
    return a * r


def sweep(t, f0, f1, curve=1.0):
    if not len(t):
        return t
    x = (t / t[-1]) ** curve
    f = f0 + (f1 - f0) * x
    return np.sin(2 * np.pi * np.cumsum(f) / RATE)


def noise(n):
    return RNG.uniform(-1.0, 1.0, n)


def lowpass(sig, alpha):
    """Filtre passe-bas 1 pole, vectorise via recurrence exponentielle."""
    sig = np.asarray(sig, dtype=np.float64)
    n = len(sig)
    if n == 0:
        return sig
    decay = 1.0 - alpha
    idx = np.arange(n)
    # implementation directe mais suffisamment rapide pour ces durees
    out = np.empty(n)
    acc = 0.0
    for i in idx:
        acc += alpha * (sig[i] - acc)
        out[i] = acc
    _ = decay
    return out


def write_wav(name, sig, peak=0.85):
    sig = np.asarray(sig, dtype=np.float64)
    m = np.max(np.abs(sig)) or 1.0
    sig = sig / m * peak
    data = (sig * 32000).astype("<i2").tobytes()
    path = SND_DIR / name
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(RATE)
        f.writeframes(data)
    print("  snd  {:<26} {:.2f}s".format(name, len(sig) / float(RATE)))


def snd_move():
    t = t_axis(0.075)
    s = sweep(t, 900, 1450, 0.6) * env(t, 0.002, 0.07, 3.0)
    s += 0.25 * np.sin(2 * np.pi * 2200 * t) * env(t, 0.001, 0.02, 4.0)
    return s * 0.7


def snd_key():
    t = t_axis(0.045)
    return np.sin(2 * np.pi * 1560 * t) * env(t, 0.001, 0.04, 3.5) * 0.6


def snd_deny():
    t = t_axis(0.18)
    s = np.sign(np.sin(2 * np.pi * 118 * t)) * 0.35
    s += np.sin(2 * np.pi * 176 * t) * 0.5
    s += lowpass(noise(len(t)), 0.05) * 0.4
    return s * env(t, 0.004, 0.16, 2.2)


def snd_dash():
    t = t_axis(0.42)
    s = lowpass(noise(len(t)), 0.30) * env(t, 0.01, 0.4, 2.4) * 0.8
    s += sweep(t, 260, 1650, 1.5) * env(t, 0.006, 0.36, 2.0) * 0.55
    s += sweep(t, 1800, 420, 0.8) * env(t, 0.002, 0.18, 3.0) * 0.30
    return s


def snd_hit():
    t = t_axis(0.55)
    s = lowpass(noise(len(t)) * env(t, 0.001, 0.28, 2.6) * 0.9, 0.22)
    s += sweep(t, 420, 55, 0.7) * env(t, 0.001, 0.5, 1.6) * 0.9
    crush = np.repeat(s[::90], 90)[:len(t)] * 0.45
    if len(crush) < len(t):
        crush = np.pad(crush, (0, len(t) - len(crush)))
    return s + crush


def snd_alert():
    t = t_axis(0.62)
    half = len(t) // 2
    s = np.zeros(len(t))
    for k, f in enumerate((980, 1240)):
        seg = t[:half]
        tone = np.sin(2 * np.pi * f * seg) * env(seg, 0.004, 0.22, 2.0)
        s[k * half:k * half + len(tone)] += tone
    s += lowpass(noise(len(t)), 0.02) * 0.18 * env(t, 0.01, 0.6, 1.5)
    return s


def snd_unlock():
    notes = (523.25, 659.25, 783.99, 1046.5)
    out = np.zeros(int(RATE * 0.7))
    for i, f in enumerate(notes):
        t = t_axis(0.34)
        tone = (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2 * t)) * env(t, 0.004, 0.3, 3.0)
        off = int(RATE * 0.075 * i)
        out[off:off + len(tone)] += tone[:len(out) - off] * 0.6
    return out


def snd_trap():
    t = t_axis(0.75)
    s = sweep(t, 620, 90, 1.6) * env(t, 0.002, 0.7, 1.8) * 0.8
    s += lowpass(noise(len(t)), 0.5) * env(t, 0.001, 0.10, 4.0) * 0.8
    s += np.sign(np.sin(2 * np.pi * 62 * t)) * env(t, 0.02, 0.6, 2.0) * 0.35
    return s


def snd_beacon():
    t = t_axis(1.0)
    s = np.sin(2 * np.pi * 1568 * t) * env(t, 0.003, 0.95, 3.2) * 0.6
    s += np.sin(2 * np.pi * 2350 * t) * env(t, 0.003, 0.55, 3.6) * 0.25
    return s


def snd_goal():
    out = np.zeros(int(RATE * 1.7))
    for i, f in enumerate((392.0, 523.25, 659.25, 783.99, 1046.5)):
        t = t_axis(1.3)
        tone = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 2 * t)
                + 0.18 * np.sin(2 * np.pi * f * 3 * t)) * env(t, 0.008, 1.2, 2.4)
        off = int(RATE * 0.085 * i)
        out[off:off + len(tone)] += tone[:len(out) - off] * 0.45
    t = t_axis(1.7)
    out[:len(t)] += sweep(t, 400, 3200, 2.2) * env(t, 0.4, 1.0, 2.0) * 0.12
    return out


def snd_fail():
    t = t_axis(1.5)
    s = sweep(t, 220, 42, 1.3) * env(t, 0.01, 1.4, 1.4) * 0.8
    s += lowpass(noise(len(t)), 0.03) * env(t, 0.02, 1.3, 1.8) * 0.35
    s += np.sign(np.sin(2 * np.pi * 88 * t)) * env(t, 0.2, 0.9, 2.2) * 0.18
    return s


def snd_countdown():
    t = t_axis(0.14)
    return np.sin(2 * np.pi * 1180 * t) * env(t, 0.002, 0.12, 3.0) * 0.55


def snd_ambient(dur=16.0):
    """Drone bouclable : partiels multiples de 1/dur + souffle croisefondu."""
    n = int(RATE * dur)
    t = np.arange(n) / float(RATE)
    base = 1.0 / dur
    s = np.zeros(n)
    for target, amp in ((55.0, 0.50), (82.5, 0.30), (110.0, 0.18), (164.8, 0.09)):
        mult = int(round(target / base))
        s += amp * np.sin(2 * np.pi * mult * base * t)
    s *= 0.65 + 0.35 * np.sin(2 * np.pi * base * t)

    tail = int(RATE * 1.5)
    raw = lowpass(noise(n + tail), 0.010)
    head = raw[:n].copy()
    fade = np.linspace(0.0, 1.0, tail)
    head[:tail] = head[:tail] * fade + raw[n:n + tail] * (1.0 - fade)
    s += head * 0.55

    for k in range(4):
        off = int(RATE * (1.4 + k * 3.7))
        pt = t_axis(1.1)
        ping = np.sin(2 * np.pi * (1320 if k % 2 else 990) * pt) * env(pt, 0.01, 1.05, 3.4)
        if off + len(ping) < n:
            s[off:off + len(ping)] += ping * 0.10
    return s


def build_sounds():
    print("Sons :")
    write_wav("hk_move.wav", snd_move(), 0.55)
    write_wav("hk_key.wav", snd_key(), 0.5)
    write_wav("hk_deny.wav", snd_deny(), 0.6)
    write_wav("hk_dash.wav", snd_dash(), 0.8)
    write_wav("hk_hit.wav", snd_hit(), 0.92)
    write_wav("hk_alert.wav", snd_alert(), 0.7)
    write_wav("hk_unlock.wav", snd_unlock(), 0.75)
    write_wav("hk_trap.wav", snd_trap(), 0.8)
    write_wav("hk_beacon.wav", snd_beacon(), 0.6)
    write_wav("hk_goal.wav", snd_goal(), 0.85)
    write_wav("hk_fail.wav", snd_fail(), 0.85)
    write_wav("hk_tick.wav", snd_countdown(), 0.45)
    write_wav("hk_ambient.wav", snd_ambient(), 0.42)


if __name__ == "__main__":
    build_images()
    build_sounds()
    print("Termine.")
