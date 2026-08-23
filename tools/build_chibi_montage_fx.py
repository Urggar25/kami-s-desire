"""Build the procedural FX textures used by the chibi montage engine.

Every texture is generated (no external art), so the montage stays self-contained
and can be re-tuned by editing the constants below and re-running the script.

    python tools/build_chibi_montage_fx.py
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "game" / "images" / "ui" / "chibi_montage"

BAND_W, BAND_H = 1920, 760

# Palette : bleu nuit du HUD + accent cyan du jeu (gui.accent_color).
BAND_RGB = (7, 19, 31)
ACCENT = (90, 196, 240)
ACCENT_SOFT = (58, 159, 202)


def save(array, name):
    """array : float RGBA HxWx4 in 0..255."""
    img = Image.fromarray(np.clip(array, 0, 255).astype(np.uint8), "RGBA")
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / name, optimize=True)
    print("  {:<16} {}x{}".format(name, img.width, img.height))
    return img


def rgba(h, w):
    return np.zeros((h, w, 4), dtype=np.float64)


def grid(h, w):
    ys, xs = np.mgrid[0:h, 0:w]
    return ys.astype(np.float64), xs.astype(np.float64)


def blur(img, radius):
    return img.filter(ImageFilter.GaussianBlur(radius))


def build_band():
    """Fond du bandeau cinema : degrade vertical + scanlines fines."""
    ys, _ = grid(BAND_H, BAND_W)
    out = rgba(BAND_H, BAND_W)
    out[..., 0], out[..., 1], out[..., 2] = BAND_RGB

    # Plus opaque sur les bords hauts/bas, plus leger au centre.
    t = np.abs(ys / (BAND_H - 1.0) * 2.0 - 1.0)
    alpha = 224 + 26 * (t ** 2)

    # Scanlines : une ligne assombrie toutes les 4 lignes.
    scan = (ys % 4 < 1)
    alpha = alpha + scan * 12

    out[..., 3] = alpha
    save(out, "band.png")


def build_stripes():
    """Rayures diagonales defilantes, seamless sur une periode de 32 px."""
    w = 2048
    ys, xs = grid(BAND_H, w)
    phase = (xs + ys * 0.62) % 32.0
    line = np.clip(1.0 - np.abs(phase - 1.5) / 2.0, 0.0, 1.0)

    out = rgba(BAND_H, w)
    out[..., 0], out[..., 1], out[..., 2] = 150, 214, 255
    out[..., 3] = line * 16.0
    save(out, "stripes.png")


def build_frame():
    """Cadre HUD : equerres d'angle, graduations, module lateral."""
    out = rgba(BAND_H, BAND_W)

    def line(x0, y0, x1, y1, color, alpha):
        out[y0:y1, x0:x1, 0] = color[0]
        out[y0:y1, x0:x1, 1] = color[1]
        out[y0:y1, x0:x1, 2] = color[2]
        out[y0:y1, x0:x1, 3] = np.maximum(out[y0:y1, x0:x1, 3], alpha)

    inset, length, thick = 30, 118, 3
    for cx in (inset, BAND_W - inset - length):
        for cy in (inset, BAND_H - inset - thick):
            line(cx, cy, cx + length, cy + thick, ACCENT, 205)
    for cx in (inset, BAND_W - inset - thick):
        for cy in (inset, BAND_H - inset - length):
            line(cx, cy, cx + thick, cy + length, ACCENT, 205)

    # Graduations le long du bord haut et bas.
    for x in range(430, 1500, 42):
        line(x, 0, x + 1, 9, ACCENT, 54)
        line(x, BAND_H - 9, x + 1, BAND_H, ACCENT, 54)

    # Module lateral droit : rail vertical + crans.
    rail_x = BAND_W - 74
    line(rail_x, 214, rail_x + 1, BAND_H - 214, ACCENT, 70)
    for i in range(9):
        y = 214 + i * ((BAND_H - 428) // 8)
        w = 16 if i % 2 == 0 else 9
        line(rail_x - w, y, rail_x, y + 1, ACCENT, 96)

    save(out, "frame.png")


def build_vignette():
    """Assombrissement doux des coins du bandeau."""
    ys, xs = grid(BAND_H, BAND_W)
    nx = (xs / (BAND_W - 1.0) * 2.0 - 1.0)
    ny = (ys / (BAND_H - 1.0) * 2.0 - 1.0)
    r = np.sqrt((nx * 0.82) ** 2 + (ny * 0.95) ** 2)
    a = np.clip((r - 0.52) / 0.62, 0.0, 1.0) ** 1.7

    out = rgba(BAND_H, BAND_W)
    out[..., 3] = a * 150.0
    save(out, "vignette.png")


def build_floor():
    """Degrade qui noie le bas du reflet dans la couleur du bandeau."""
    h, w = 100, BAND_W
    ys, _ = grid(h, w)
    out = rgba(h, w)
    out[..., 0], out[..., 1], out[..., 2] = BAND_RGB
    out[..., 3] = np.clip(ys / (h - 1.0), 0, 1) ** 1.25 * 250.0
    save(out, "floor.png")


def build_glow():
    """Halo radial place derriere le chibi."""
    size = 768
    ys, xs = grid(size, size)
    c = (size - 1) / 2.0
    r = np.sqrt(((xs - c) / c) ** 2 + ((ys - c) / c) ** 2)
    a = np.clip(1.0 - r, 0.0, 1.0) ** 2.4

    out = rgba(size, size)
    out[..., 0], out[..., 1], out[..., 2] = 126, 206, 255
    out[..., 3] = a * 108.0
    save(out, "glow.png")


def build_ring():
    """Anneau d'impact emis a chaque changement d'etape."""
    size = 512
    ys, xs = grid(size, size)
    c = (size - 1) / 2.0
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2)
    a = np.exp(-((r - 214.0) ** 2) / (2 * 15.0 ** 2)) * 235.0
    a += np.exp(-((r - 196.0) ** 2) / (2 * 44.0 ** 2)) * 55.0

    out = rgba(size, size)
    out[..., 0], out[..., 1], out[..., 2] = 198, 238, 255
    out[..., 3] = a
    save(out, "ring.png")


def build_speedlines():
    """Lignes de vitesse facon manga, transparentes au centre."""
    size = 1200
    rng = np.random.default_rng(70117)
    ys, xs = grid(size, size)
    c = (size - 1) / 2.0
    dx, dy = xs - c, ys - c
    r = np.sqrt(dx * dx + dy * dy) / c
    ang = np.arctan2(dy, dx)

    acc = np.zeros((size, size))
    for _ in range(58):
        a0 = rng.uniform(-np.pi, np.pi)
        width = rng.uniform(0.006, 0.026)
        start = rng.uniform(0.30, 0.52)
        d = np.abs(np.arctan2(np.sin(ang - a0), np.cos(ang - a0)))
        band = np.clip(1.0 - d / width, 0.0, 1.0) ** 0.8
        radial = np.clip((r - start) / (1.0 - start), 0.0, 1.0) ** 1.4
        acc = np.maximum(acc, band * radial)

    acc *= np.clip((1.0 - r) / 0.16, 0.0, 1.0)

    out = rgba(size, size)
    out[..., 0], out[..., 1], out[..., 2] = 226, 245, 255
    out[..., 3] = acc * 190.0
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")
    img = blur(img, 1.4)
    img.save(OUT / "speedlines.png", optimize=True)
    print("  {:<16} {}x{}".format("speedlines.png", img.width, img.height))


def build_spark():
    """Etincelle 4 branches."""
    size = 96
    ys, xs = grid(size, size)
    c = (size - 1) / 2.0
    dx, dy = np.abs(xs - c), np.abs(ys - c)
    r = np.sqrt(dx * dx + dy * dy)

    horiz = np.clip(1.0 - dy / 3.0, 0, 1) * np.clip(1.0 - dx / c, 0, 1) ** 1.6
    vert = np.clip(1.0 - dx / 3.0, 0, 1) * np.clip(1.0 - dy / c, 0, 1) ** 1.6
    core = np.clip(1.0 - r / 12.0, 0, 1) ** 1.5

    out = rgba(size, size)
    out[..., 0], out[..., 1], out[..., 2] = 255, 255, 255
    out[..., 3] = np.clip(np.maximum(np.maximum(horiz, vert), core), 0, 1) * 255.0
    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")
    img = blur(img, 0.8)
    img.save(OUT / "spark.png", optimize=True)
    print("  {:<16} {}x{}".format("spark.png", img.width, img.height))


def build_dot():
    """Poussiere douce (impact au sol, particules d'ambiance)."""
    size = 64
    ys, xs = grid(size, size)
    c = (size - 1) / 2.0
    r = np.sqrt((xs - c) ** 2 + (ys - c) ** 2) / c
    out = rgba(size, size)
    out[..., 0], out[..., 1], out[..., 2] = 255, 255, 255
    out[..., 3] = np.clip(1.0 - r, 0, 1) ** 2.2 * 255.0
    save(out, "dot.png")


def build_shadow():
    """Ombre portee elliptique sous le chibi."""
    w, h = 460, 128
    ys, xs = grid(h, w)
    cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
    r = np.sqrt(((xs - cx) / cx) ** 2 + ((ys - cy) / cy) ** 2)
    out = rgba(h, w)
    out[..., 3] = np.clip(1.0 - r, 0, 1) ** 1.9 * 165.0
    save(out, "shadow.png")


def build_streak():
    """Trainee lumineuse qui balaie le bandeau lors des coupes."""
    w, h = 900, BAND_H
    ys, xs = grid(h, w)
    cx = (w - 1) / 2.0
    shear = (ys / (h - 1.0) - 0.5) * 260.0
    d = np.abs(xs - cx - shear)
    a = np.exp(-(d ** 2) / (2 * 108.0 ** 2)) * 96.0
    a += np.exp(-(d ** 2) / (2 * 16.0 ** 2)) * 70.0

    out = rgba(h, w)
    out[..., 0], out[..., 1], out[..., 2] = 214, 240, 255
    out[..., 3] = a
    save(out, "streak.png")


def main():
    print("chibi montage FX -> {}".format(OUT))
    build_band()
    build_stripes()
    build_frame()
    build_vignette()
    build_floor()
    build_glow()
    build_ring()
    build_speedlines()
    build_spark()
    build_dot()
    build_shadow()
    build_streak()
    print("done")


if __name__ == "__main__":
    main()
