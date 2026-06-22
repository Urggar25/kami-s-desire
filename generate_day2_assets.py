"""
Génère les assets GUI pour le système d'arguments du Jour 2.
Exécuter depuis la racine du projet : python generate_day2_assets.py
"""
import os
try:
    from PIL import Image, ImageDraw
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw

OUT = os.path.join("game", "gui", "day2")
os.makedirs(OUT, exist_ok=True)

def save(img, name):
    path = os.path.join(OUT, name)
    img.save(path)
    print(f"  ✓ {name}")

# ── argument_card_bg.png (460 × 260) ──────────────────────────────────────────
img = Image.new("RGBA", (460, 260))
d = ImageDraw.Draw(img)
d.rounded_rectangle([0, 0, 459, 259], radius=10, fill=(8, 22, 38, 245))
d.rounded_rectangle([0, 0, 459, 259], radius=10, outline=(0, 185, 235, 190), width=2)
d.rectangle([18, 10, 442, 13], fill=(0, 185, 235, 130))
for y in range(80, 245, 22):
    d.line([(18, y), (442, y)], fill=(30, 65, 100, 55), width=1)
d.polygon([(415, 238), (459, 238), (459, 259), (415, 259)], fill=(0, 185, 235, 80))
save(img, "argument_card_bg.png")

# ── argument_drop_zone.png (560 × 330) ────────────────────────────────────────
img2 = Image.new("RGBA", (560, 330))
d2 = ImageDraw.Draw(img2)
d2.rounded_rectangle([0, 0, 559, 329], radius=12, fill=(4, 12, 22, 210))
dc = (0, 185, 235, 150)
for x in range(14, 548, 16):
    d2.rectangle([x, 2, x + 8, 5], fill=dc)
    d2.rectangle([x, 324, x + 8, 327], fill=dc)
for y in range(14, 318, 16):
    d2.rectangle([2, y, 5, y + 8], fill=dc)
    d2.rectangle([554, y, 557, y + 8], fill=dc)
# mallette
bx, by = 225, 72
d2.rounded_rectangle([bx, by + 32, bx + 110, by + 100], radius=7,
                      fill=(0, 100, 160, 200), outline=(0, 185, 235, 200), width=2)
d2.rounded_rectangle([bx + 32, by + 10, bx + 78, by + 38], radius=6,
                      outline=(0, 185, 235, 200), width=3, fill=(4, 12, 22, 0))
d2.rectangle([bx + 48, by + 58, bx + 62, by + 76], fill=(0, 210, 255, 210))
# flèche
ax, ay = 265, 180
pts = [(ax, ay), (ax + 22, ay), (ax + 22, ay + 18),
       (ax + 32, ay + 18), (ax + 11, ay + 42), (ax - 10, ay + 18), (ax, ay + 18)]
d2.polygon(pts, fill=(0, 185, 235, 190))
save(img2, "argument_drop_zone.png")

# ── vote_panel_bg.png (330 × 830) ─────────────────────────────────────────────
for fname, w, h, col_fill, col_border in [
    ("vote_panel_pour_bg.png",    330, 830, (14, 45, 24, 235), (30, 160,  80, 180)),
    ("vote_panel_unknown_bg.png", 330, 830, (10, 26, 42, 235), (25,  70, 110, 180)),
    ("vote_panel_contre_bg.png",  330, 830, (42, 12, 18, 235), (160, 30,  50, 180)),
]:
    im = Image.new("RGBA", (w, h))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle([0, 0, w - 1, h - 1], radius=8, fill=col_fill)
    dr.rounded_rectangle([0, 0, w - 1, h - 1], radius=8, outline=col_border, width=1)
    dr.rectangle([10, 6, w - 10, 9], fill=(*col_border[:3], 100))
    save(im, fname)

# ── vote_char_card_*.png (152 × 124) ──────────────────────────────────────────
for name, fill, border in [
    ("vote_char_pour",    (14, 60, 28, 240), (30, 180,  80, 220)),
    ("vote_char_unknown", (16, 38, 58, 240), (40, 100, 150, 180)),
    ("vote_char_contre",  (60, 14, 22, 240), (180, 35,  55, 220)),
]:
    im = Image.new("RGBA", (152, 124))
    dr = ImageDraw.Draw(im)
    dr.rounded_rectangle([0, 0, 151, 123], radius=6, fill=fill)
    dr.rounded_rectangle([0, 0, 151, 123], radius=6, outline=border, width=2)
    dr.rectangle([6, 4, 146, 7], fill=(*border[:3], 150))
    save(im, f"{name}.png")

# ── argument_found_bg.png (440 × 112) ─────────────────────────────────────────
im = Image.new("RGBA", (440, 112))
dr = ImageDraw.Draw(im)
dr.rounded_rectangle([0, 0, 439, 111], radius=6, fill=(10, 34, 54, 235))
dr.rounded_rectangle([0, 0, 439, 111], radius=6, outline=(0, 155, 205, 160), width=1)
dr.rectangle([0, 0, 4, 111], fill=(0, 185, 235, 210))
save(im, "argument_found_bg.png")

# ── argument_locked_bg.png (440 × 112) ────────────────────────────────────────
im = Image.new("RGBA", (440, 112))
dr = ImageDraw.Draw(im)
dr.rounded_rectangle([0, 0, 439, 111], radius=6, fill=(10, 16, 24, 215))
dr.rounded_rectangle([0, 0, 439, 111], radius=6, outline=(40, 58, 78, 120), width=1)
dr.rectangle([0, 0, 4, 111], fill=(50, 70, 92, 150))
save(im, "argument_locked_bg.png")

print("\nAssets générés dans", OUT)
