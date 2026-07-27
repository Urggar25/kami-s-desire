#!/usr/bin/env python3
# Génère les assets images du minijeu "amendement_brouillon" — qualité pro procédurale.
import os, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance

random.seed(1789)
OUT = "/sessions/modest-charming-mayer/mnt/kami-s-desire/game/minijeu/amend_assets"
os.makedirs(OUT, exist_ok=True)

def save(img, name):
    img.save(os.path.join(OUT, name))
    print("ok", name)

def noise_layer(w, h, amp=18, seed=0):
    rnd = random.Random(seed)
    small = Image.new("L", (max(1,w//4), max(1,h//4)))
    px = small.load()
    for y in range(small.height):
        for x in range(small.width):
            px[x, y] = rnd.randint(128-amp, 128+amp)
    return small.resize((w, h), Image.BILINEAR)

def radial_vignette(w, h, strength=1.0, cx=0.5, cy=0.5):
    v = Image.new("L", (w, h), 0)
    px = v.load()
    maxr = math.hypot(w*max(cx,1-cx), h*max(cy,1-cy))
    for y in range(h):
        for x in range(w):
            r = math.hypot(x-w*cx, y-h*cy)/maxr
            px[x, y] = int(max(0, min(255, 255*(r**1.7)*strength)))
    return v

def make_desk():
    W, H = 1920, 1080
    base = Image.new("RGB", (W, H), (14, 18, 24))
    grad = Image.new("L", (1, H))
    for y in range(H):
        grad.putpixel((0, y), int(30 + 22*(y/H)))
    grad = grad.resize((W, H))
    base = Image.composite(Image.new("RGB",(W,H),(26,32,40)), base, grad)
    n = noise_layer(W, H, amp=10, seed=3).convert("RGB")
    base = ImageChops.overlay(base, n)
    base = Image.blend(base, n, 0.06)
    d = ImageDraw.Draw(base, "RGBA")
    for i in range(0, H, 3):
        a = random.randint(0, 8)
        d.line([(0, i), (W, i)], fill=(255, 255, 255, a))
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).ellipse([W*0.5-620, H*0.5-460, W*0.5+620, H*0.5+460], fill=90)
    halo = halo.filter(ImageFilter.GaussianBlur(180))
    warm = Image.new("RGB", (W, H), (60, 72, 88))
    base = Image.composite(warm, base, halo)
    vg = radial_vignette(W, H, strength=1.15)
    base = Image.composite(Image.new("RGB", (W, H), (4, 6, 9)), base, vg)
    save(base.convert("RGB"), "amend_desk.png")

SHEET_W, SHEET_H = 1200, 840
PAPER_W, PAPER_H = 1150, 792
PAD_X = (SHEET_W - PAPER_W)//2
PAD_Y = (SHEET_H - PAPER_H)//2

def paper_mask(w, h, seed=7):
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, w-1, h-1], radius=10, fill=255)
    rnd = random.Random(seed)
    for _ in range(60):
        edge = rnd.choice(["t", "b", "l", "r"])
        if edge in ("t", "b"):
            x = rnd.randint(0, w); y = 0 if edge == "t" else h
            r = rnd.randint(2, 7)
            d.ellipse([x-r, y-r, x+r, y+r], fill=0)
        else:
            y = rnd.randint(0, h); x = 0 if edge == "l" else w
            r = rnd.randint(2, 7)
            d.ellipse([x-r, y-r, x+r, y+r], fill=0)
    return m.filter(ImageFilter.GaussianBlur(0.6))

def paper_face(w, h, seed=7):
    base = Image.new("RGB", (w, h), (232, 226, 210))
    fib = noise_layer(w, h, amp=14, seed=seed).convert("RGB")
    base = ImageChops.overlay(base, fib)
    base = Image.blend(base, fib, 0.10)
    stains = Image.new("L", (w, h), 0)
    sd = ImageDraw.Draw(stains)
    rnd = random.Random(seed+1)
    for _ in range(18):
        x, y = rnd.randint(0, w), rnd.randint(0, h)
        r = rnd.randint(40, 160)
        sd.ellipse([x-r, y-r, x+r, y+r], fill=rnd.randint(10, 26))
    stains = stains.filter(ImageFilter.GaussianBlur(50))
    base = Image.composite(Image.new("RGB", (w, h), (214, 205, 184)), base, stains)
    ivg = radial_vignette(w, h, strength=0.5)
    base = Image.composite(Image.new("RGB", (w, h), (206, 198, 178)), base, ivg)
    d = ImageDraw.Draw(base, "RGBA")
    for y in range(120, h-60, 74):
        d.line([(60, y), (w-60, y)], fill=(120, 130, 150, 26))
    d.line([(150, 40), (150, h-40)], fill=(150, 90, 90, 34))
    return base

def make_sheet():
    canvas = Image.new("RGBA", (SHEET_W, SHEET_H), (0, 0, 0, 0))
    mask = paper_mask(PAPER_W, PAPER_H)
    face = paper_face(PAPER_W, PAPER_H)
    shadow = Image.new("RGBA", (SHEET_W, SHEET_H), (0, 0, 0, 0))
    sh = Image.new("L", (SHEET_W, SHEET_H), 0)
    ImageDraw.Draw(sh).rounded_rectangle([PAD_X+8, PAD_Y+14, PAD_X+PAPER_W+8, PAD_Y+PAPER_H+18], radius=12, fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    shadow.putalpha(sh)
    canvas = Image.alpha_composite(canvas, shadow)
    paper = Image.new("RGBA", (PAPER_W, PAPER_H))
    paper.paste(face, (0, 0))
    paper.putalpha(mask)
    canvas.alpha_composite(paper, (PAD_X, PAD_Y))
    save(canvas, "amend_sheet.png")
    return mask

def make_wrinkle(level, mask):
    W, H = SHEET_W, SHEET_H
    smask = Image.new("L", (W, H), 0)
    smask.paste(mask, (PAD_X, PAD_Y))
    mask = smask
    lum = Image.new("L", (W, H), 128)
    d = ImageDraw.Draw(lum)
    rnd = random.Random(50+level)
    n_folds = 4 + level*5
    for _ in range(n_folds):
        x1 = rnd.randint(PAD_X, PAD_X+PAPER_W)
        y1 = rnd.randint(PAD_Y, PAD_Y+PAPER_H)
        ang = rnd.uniform(0, math.pi)
        ln = rnd.randint(120, 420)
        x2 = x1 + math.cos(ang)*ln; y2 = y1 + math.sin(ang)*ln
        d.line([(x1, y1), (x2, y2)], fill=rnd.randint(90, 110), width=rnd.randint(2, 4))
        off = 3
        d.line([(x1+off, y1+off), (x2+off, y2+off)], fill=rnd.randint(150, 170), width=rnd.randint(1, 2))
    lum = lum.filter(ImageFilter.GaussianBlur(1.2))
    rgba = Image.merge("RGBA", (lum, lum, lum, mask.point(lambda v: int(v*(0.35+0.18*level)))))
    if level >= 2:
        big = Image.new("L", (W, H), 128)
        bd = ImageDraw.Draw(big)
        for _ in range(3+level):
            bx = rnd.randint(PAD_X, PAD_X+PAPER_W)
            by = rnd.randint(PAD_Y, PAD_Y+PAPER_H)
            r = rnd.randint(80, 220)
            bd.ellipse([bx-r, by-r*0.4, bx+r, by+r*0.4], fill=rnd.randint(105, 150))
        big = big.filter(ImageFilter.GaussianBlur(18))
        big_rgba = Image.merge("RGBA", (big, big, big, mask.point(lambda v: int(v*0.28))))
        rgba = Image.alpha_composite(rgba, big_rgba)
    save(rgba, "amend_wrinkle%d.png" % level)

def make_smudge():
    w, h = 240, 96
    a = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(a)
    rnd = random.Random(11)
    for _ in range(90):
        x = rnd.randint(10, w-10); y = int(h/2 + rnd.gauss(0, h*0.18))
        r = rnd.randint(4, 16)
        d.ellipse([x-r, y-r, x+r, y+r], fill=rnd.randint(20, 70))
    for _ in range(40):
        y = rnd.randint(8, h-8)
        x1 = rnd.randint(6, w//2); x2 = rnd.randint(w//2, w-6)
        d.line([(x1, y), (x2, y)], fill=rnd.randint(15, 55), width=1)
    a = a.filter(ImageFilter.GaussianBlur(2.2))
    col = Image.new("RGBA", (w, h), (70, 68, 74, 0))
    col.putalpha(a)
    save(col, "amend_smudge.png")

def make_strike():
    w, h = 300, 60
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    rnd = random.Random(22)
    ink = (28, 26, 40, 235)
    pts = []
    n = 26
    for i in range(n):
        x = 10 + (w-20)*i/(n-1)
        y = h/2 + math.sin(i*0.9)*rnd.uniform(6, 12) + rnd.uniform(-4, 4)
        pts.append((x, y))
    d.line(pts, fill=ink, width=4, joint="curve")
    pts2 = [(x, y+rnd.uniform(-5, 5)) for (x, y) in pts]
    d.line(pts2, fill=(28, 26, 40, 170), width=3, joint="curve")
    save(img.filter(ImageFilter.GaussianBlur(0.5)), "amend_strike.png")

def make_circle():
    w, h = 340, 150
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    rnd = random.Random(33)
    for loop in range(2):
        pts = []
        steps = 80
        rx, ry = w/2-16-loop*3, h/2-14-loop*3
        for i in range(steps+12):
            t = i/steps*2*math.pi
            j = rnd.uniform(-5, 5)
            x = w/2 + math.cos(t)*(rx+j)
            y = h/2 + math.sin(t)*(ry+j)
            pts.append((x, y))
        d.line(pts, fill=(30, 24, 44, 230) if loop == 0 else (30, 24, 44, 150), width=4-loop, joint="curve")
    save(img.filter(ImageFilter.GaussianBlur(0.4)), "amend_circle.png")

def make_note():
    w, h = 300, 110
    mask = paper_mask(w, h, seed=99)
    face = paper_face(w, h, seed=99)
    face = ImageEnhance.Brightness(face).enhance(1.04)
    img = Image.new("RGBA", (w, h))
    img.paste(face, (0, 0))
    img.putalpha(mask.point(lambda v: int(v*0.96)))
    save(img, "amend_note.png")
    dark = ImageEnhance.Brightness(face).enhance(0.9)
    img2 = Image.new("RGBA", (w, h)); img2.paste(dark, (0, 0)); img2.putalpha(mask.point(lambda v:int(v*0.9)))
    save(img2, "amend_note_locked.png")

def make_eraser():
    w, h = 190, 130
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = Image.new("L", (w, h), 0)
    ImageDraw.Draw(sh).rounded_rectangle([26, 40, w-14, h-16], radius=18, fill=120)
    sh = sh.filter(ImageFilter.GaussianBlur(9))
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0)); shadow.putalpha(sh)
    img = Image.alpha_composite(img, shadow)
    d = ImageDraw.Draw(img)
    body = [18, 22, w-24, h-26]
    d.rounded_rectangle(body, radius=16, fill=(214, 150, 158, 255))
    d.rounded_rectangle([18, 22, w-24, 74], radius=16, fill=(230, 176, 182, 255))
    d.rounded_rectangle([18, 22, 62, h-26], radius=14, fill=(120, 96, 104, 255))
    d.rectangle([54, 24, 66, h-28], fill=(150, 120, 128, 255))
    rnd = random.Random(44)
    for _ in range(40):
        x = rnd.randint(24, w-30); y = rnd.randint(28, h-32)
        d.line([(x, y), (x+rnd.randint(-6, 6), y+rnd.randint(-4, 4))], fill=(255, 255, 255, 40))
    d.rounded_rectangle(body, radius=16, outline=(90, 60, 66, 160), width=2)
    save(img, "amend_eraser.png")

def make_shadow():
    w, h = 900, 1080
    img = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(img)
    d.ellipse([w*0.5-120, h*0.28-120, w*0.5+120, h*0.28+120], fill=170)
    d.polygon([(w*0.5-260, h), (w*0.5-190, h*0.42), (w*0.5+190, h*0.42), (w*0.5+260, h)], fill=170)
    img = img.filter(ImageFilter.GaussianBlur(60))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.putalpha(img.point(lambda v: int(v*0.85)))
    save(out, "amend_shadow.png")

def make_room_wide():
    W, H = 1920, 1080
    img = Image.new("RGB", (W, H), (8, 10, 14))
    d = ImageDraw.Draw(img, "RGBA")
    for y in range(H):
        t = y/H
        d.line([(0, y), (W, y)], fill=(int(6+10*t), int(8+12*t), int(12+16*t)))
    cx, cy = W*0.5, H*0.30
    rows = 6
    for r in range(rows):
        rr = 210 + r*150
        col = 26 + r*6
        seat_col = (col, col+4, col+10, 255)
        n_seats = 8 + r*3
        for s in range(n_seats):
            ang = math.pi*(0.08 + 0.84*s/(n_seats-1))
            sx = cx + math.cos(ang)*rr*1.5
            sy = cy + math.sin(ang)*rr*0.7
            if sy > H-40 or sx < -60 or sx > W+60:
                continue
            bw = max(14, 46 - r*3); bh = max(10, 30 - r*2)
            d.rounded_rectangle([sx-bw, sy-bh, sx+bw, sy+bh], radius=4, fill=seat_col)
            d.rectangle([sx-bw, sy-bh-bh*0.7, sx+bw, sy-bh+2], fill=(col-6, col-2, col+4, 255))
    nx, ny = W*0.5, H*0.72
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).ellipse([nx-360, ny-420, nx+360, ny+220], fill=70)
    halo = halo.filter(ImageFilter.GaussianBlur(120))
    img = Image.composite(Image.new("RGB", (W, H), (54, 62, 74)), img, halo)
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([nx-150, ny+60, nx+150, ny+160], radius=6, fill=(22, 26, 32, 255))
    d.polygon([(nx-60, ny+66), (nx+60, ny+66), (nx+52, ny+120), (nx-52, ny+120)], fill=(210, 202, 184, 255))
    d.ellipse([nx-40, ny-70, nx+40, ny+10], fill=(16, 18, 24, 255))
    d.polygon([(nx-95, ny+70), (nx-60, ny-30), (nx+60, ny-30), (nx+95, ny+70)], fill=(14, 16, 22, 255))
    d.line([(nx-58, ny-28), (nx-88, ny+60)], fill=(90, 120, 150, 120), width=3)
    d.line([(nx+58, ny-28), (nx+88, ny+60)], fill=(90, 120, 150, 90), width=3)
    vg = radial_vignette(W, H, strength=1.35, cy=0.42)
    img = Image.composite(Image.new("RGB", (W, H), (2, 3, 5)), img, vg)
    n = noise_layer(W, H, amp=8, seed=9).convert("RGB")
    img = Image.blend(img, n, 0.05)
    save(img, "amend_room_wide.png")

make_desk()
mask = make_sheet()
for lv in (1, 2, 3):
    make_wrinkle(lv, mask)
make_smudge(); make_strike(); make_circle(); make_note(); make_eraser(); make_shadow(); make_room_wide()
print("DONE images")
