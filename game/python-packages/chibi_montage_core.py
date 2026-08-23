# -*- coding: utf-8 -*-
"""Coeur mathematique du montage chibi.

Python pur, sans aucune dependance a Ren'Py : ce module decrit la
sequence sous forme d'une liste d'operations de dessin pour un instant
donne. Deux consommateurs l'utilisent :

  - game/chibi_montage.rpy         -> rendu dans le jeu (Ren'Py)
  - tools/preview_chibi_montage.py -> apercu video hors du jeu (Pillow)

Les deux partagent donc exactement la meme animation : impossible que
l'apercu et le jeu divergent.

Une operation est un dict :

  {"kind": "img", "src": ("fx", "ring") | ("cell", 3),
   "crop": (x, y, w, h) | None,      # en pixels source
   "cx", "cy",                       # centre de la zone dessinee, ecran
   "xzoom", "yzoom", "rotate", "alpha",
   "bright": 0.0, "tint": None}

  {"kind": "solid", "color": "#rrggbb", "x", "y", "w", "h", "alpha"}

  {"kind": "text", "style": "caption", "index": 0, "x", "y", "alpha"}

Le rognage (clip) est resolu ici, en amont : les operations sortent deja
bornees au bandeau, aucun moteur n'a besoin de gerer du decoupage.
"""

import math
import random


# ------------------------------------------------------------------
# Constantes de scene (espace de design 1920x1080)
# ------------------------------------------------------------------
SCREEN_W = 1920
SCREEN_H = 1080
BAND_H = 760
BAND_CY = 540.0

FX_DIR = "images/ui/chibi_montage/"

FX_SIZE = {
    "band": (1920, 760),
    "stripes": (2048, 760),
    "frame": (1920, 760),
    "vignette": (1920, 760),
    "floor": (1920, 100),
    "glow": (768, 768),
    "ring": (512, 512),
    "speedlines": (1200, 1200),
    "spark": (96, 96),
    "dot": (64, 64),
    "shadow": (460, 128),
    "streak": (900, 760),
}

ACCENT = "#5ac4f0"
EDGE = "#a8e4ff"
SEG_OFF = "#456278"
FLASH = "#eaf6ff"
TEXT_DIM = "#9dc3dc"

FONT_HUD = "fonts/Rajdhani-SemiBold.ttf"
FONT_SOFT = "fonts/Barlow-Light.ttf"

TEXT_STYLES = {
    "kicker": {"font": FONT_HUD, "size": 27, "color": TEXT_DIM, "kerning": 6},
    "counter": {"font": FONT_HUD, "size": 36, "color": ACCENT, "kerning": 3},
    "caption": {"font": FONT_HUD, "size": 66, "color": "#ffffff", "kerning": 2,
                "shadow": (0, 3, "#04121c")},
    "ghost": {"font": FONT_HUD, "size": 320, "color": ACCENT, "kerning": 0},
    "footer": {"font": FONT_SOFT, "size": 24, "color": TEXT_DIM, "kerning": 4},
    "footer_final": {"font": FONT_SOFT, "size": 24, "color": ACCENT, "kerning": 4},
}

# Bloc HUD de gauche.
TX = 196
Y_BAR = 392
Y_KICKER = 397
Y_COUNTER = 452
Y_CAPTION = 498
Y_GAUGE = 612
Y_FOOTER = 650
SEG_W = 56
SEG_H = 7
SEG_GAP = 10
GHOST_X = 742
GHOST_Y = 292

# Variante compacte : sequence sans legendes ni compteur, le bloc se
# resserre autour de la jauge et reste centre sur le bandeau.
Y_BAR_LEAN = 470
Y_KICKER_LEAN = 475
Y_GAUGE_LEAN = 534
Y_FOOTER_LEAN = 574


# ------------------------------------------------------------------
# Courbes
# ------------------------------------------------------------------
def clamp(x, lo=0.0, hi=1.0):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def out_cubic(x):
    x = clamp(x)
    return 1.0 - (1.0 - x) ** 3


def in_cubic(x):
    x = clamp(x)
    return x * x * x


# ------------------------------------------------------------------
# Description d'une sequence
# ------------------------------------------------------------------
class ChibiStep(object):
    """Une case de la planche, son timing et son habillage."""

    def __init__(self, cell, hold, caption, sfx=None, volume=0.55,
                 tint=None, shiver=0.0, hop=1.0, final=False):
        self.cell = cell            # index de la case dans la planche
        self.hold = hold            # duree d'affichage, en secondes
        self.caption = caption      # legende affichee a gauche
        self.sfx = sfx              # son joue au moment de la coupe
        self.volume = volume
        self.tint = tint            # teinte "#rrggbb" (froid, chaud...)
        self.shiver = shiver        # amplitude du grelottement, en px
        self.hop = hop              # intensite du saut d'arrivee
        self.final = final          # etape de conclusion : gros impact


class ChibiMontageSpec(object):
    """Tout ce qui decrit une sequence, independamment du moteur."""

    def __init__(self, sheet, sheet_size, cols, content, steps,
                 kicker=u"SEQUENCE", footer=u"", footer_final=None,
                 chibi_x=1240, feet_y=852, zoom=0.88, seed=70117,
                 captions=True):
        self.sheet = sheet
        self.sheet_w, self.sheet_h = sheet_size
        self.cols = cols
        self.content_top, self.content_bottom = content
        self.steps = steps
        self.kicker = kicker
        self.footer = footer
        self.footer_final = footer_final if footer_final is not None else footer
        self.chibi_x = float(chibi_x)
        self.feet_y = float(feet_y)
        self.zoom = float(zoom)
        self.seed = seed
        # captions=False : ni legende d'etape, ni compteur, ni filigrane ;
        # l'image porte la sequence toute seule.
        self.captions = captions

    def cell_rect(self, index):
        """Decoupe reguliere de la planche : ni trou ni recouvrement."""
        x0 = int(round(index * self.sheet_w / float(self.cols)))
        x1 = int(round((index + 1) * self.sheet_w / float(self.cols)))
        return (x0, x1 - x0)


# ------------------------------------------------------------------
# La chronologie : produit les operations de dessin
# ------------------------------------------------------------------
class ChibiTimeline(object):

    T_IN = 0.36         # ouverture du volet
    T_OUT = 0.46        # fermeture du volet
    T_FADE = 0.22       # disparition du contenu pendant la fermeture

    def __init__(self, spec):
        self.spec = spec

        self.starts = []
        t = self.T_IN
        for step in spec.steps:
            self.starts.append(t)
            t += step.hold
        self.t_end = t
        self.duration = t + self.T_OUT

        # Particules deterministes : la sequence est reproductible a
        # l'identique, et le rendu ne tire jamais au hasard.
        rng = random.Random(spec.seed)
        self.sparks = []
        self.dust = []
        for step in spec.steps:
            count = 22 if step.final else 7
            burst = []
            for k in range(count):
                burst.append((
                    (2.0 * math.pi * k / count) + rng.uniform(-0.30, 0.30),
                    rng.uniform(210.0, 430.0) * (1.35 if step.final else 1.0),
                    rng.uniform(0.30, 0.72) * (1.30 if step.final else 1.0),
                    rng.uniform(0.34, 0.62) * (1.45 if step.final else 1.0),
                    rng.uniform(-360.0, 360.0),
                ))
            self.sparks.append(burst)

            puffs = []
            for k in range(5):
                puffs.append((
                    rng.uniform(-1.0, 1.0),
                    rng.uniform(0.55, 1.00),
                    rng.uniform(0.55, 0.95),
                ))
            self.dust.append(puffs)

    # -- SFX : exactement les memes temps que la chronologie visuelle --
    def sound_cues(self):
        rv = []
        for i, step in enumerate(self.spec.steps):
            if step.sfx:
                rv.append((self.starts[i], step.sfx, step.volume))
        return rv

    def step_at(self, st):
        index = 0
        for i, start in enumerate(self.starts):
            if st >= start:
                index = i
        return index, max(0.0, st - self.starts[index])

    # --------------------------------------------------------------
    # Fabriques d'operations
    # --------------------------------------------------------------
    def _img(self, out, src, size, cx, cy, xzoom, yzoom, alpha,
             clip=None, rotate=0.0, bright=0.0, tint=None, origin=(0, 0)):
        """Ajoute une image, eventuellement rognee au rectangle `clip`.

        Le rognage est calcule cote source : ce qui sort du bandeau n'est
        jamais dessine, meme quand l'effet est plus grand que lui.
        """
        if alpha <= 0.004:
            return

        bw, bh = size
        ax, ay = abs(xzoom), abs(yzoom)
        if ax <= 0.0 or ay <= 0.0:
            return

        dw, dh = bw * ax, bh * ay
        dx, dy = cx - dw / 2.0, cy - dh / 2.0
        crop = (0, 0, bw, bh)

        if clip is not None:
            left = max(dx, clip[0])
            top = max(dy, clip[1])
            right = min(dx + dw, clip[0] + clip[2])
            bottom = min(dy + dh, clip[1] + clip[3])
            if right - left < 1.5 or bottom - top < 1.5:
                return

            sx0 = (left - dx) / ax
            sx1 = (right - dx) / ax
            if yzoom >= 0.0:
                sy0 = (top - dy) / ay
                sy1 = (bottom - dy) / ay
            else:
                # Image retournee : la ligne du haut vient d'en bas.
                sy0 = bh - (bottom - dy) / ay
                sy1 = bh - (top - dy) / ay

            sx = max(0, min(int(sx0), bw - 1))
            sy = max(0, min(int(sy0), bh - 1))
            sw = max(1, min(int(math.ceil(sx1)) - sx, bw - sx))
            sh = max(1, min(int(math.ceil(sy1)) - sy, bh - sy))
            crop = (sx, sy, sw, sh)

            # Le centre suit la zone reellement conservee.
            cx = dx + (sx + sw / 2.0) * ax
            if yzoom >= 0.0:
                cy = dy + (sy + sh / 2.0) * ay
            else:
                cy = dy + (bh - sy - sh / 2.0) * ay

        out.append({
            "kind": "img", "src": src,
            "crop": (origin[0] + crop[0], origin[1] + crop[1],
                     crop[2], crop[3]),
            "cx": cx, "cy": cy,
            "xzoom": xzoom, "yzoom": yzoom,
            "rotate": rotate, "alpha": alpha,
            "bright": bright, "tint": tint,
        })

    def _fx(self, out, name, cx, cy, zoom, alpha, clip=None, rotate=0.0):
        self._img(out, ("fx", name), FX_SIZE[name], cx, cy, zoom, zoom,
                  alpha, clip=clip, rotate=rotate)

    def _solid(self, out, color, x, y, w, h, alpha):
        if alpha <= 0.004 or w < 1 or h < 1:
            return
        out.append({"kind": "solid", "color": color, "x": x, "y": y,
                    "w": int(round(w)), "h": int(round(h)), "alpha": alpha})

    def _text(self, out, style, index, x, y, alpha):
        if alpha <= 0.004:
            return
        out.append({"kind": "text", "style": style, "index": index,
                    "x": x, "y": y, "alpha": alpha})

    # --------------------------------------------------------------
    # Liste de dessin pour l'instant st
    # --------------------------------------------------------------
    def ops(self, st):
        spec = self.spec
        out = []
        if st >= self.duration:
            return out

        # --- Volet : ouverture puis fermeture ---
        if st < self.T_IN:
            open_p = out_cubic(st / self.T_IN)
            content = clamp((open_p - 0.40) / 0.60)
        elif st > self.t_end:
            open_p = 1.0 - in_cubic((st - self.t_end) / self.T_OUT)
            content = 1.0 - clamp((st - self.t_end) / self.T_FADE)
        else:
            open_p = 1.0
            content = 1.0

        band_h = max(2.0, BAND_H * open_p)
        band_top = BAND_CY - band_h / 2.0
        clip = (0.0, band_top, float(SCREEN_W), band_h)

        index, u = self.step_at(st)
        step = spec.steps[index]
        last = (index == len(spec.steps) - 1)

        # ---------- fond du bandeau ----------
        self._fx(out, "band", SCREEN_W / 2.0, BAND_CY, 1.0, 1.0, clip)
        self._fx(out, "stripes",
                 SCREEN_W / 2.0 - ((st * 22.0) % 32.0), BAND_CY, 1.0,
                 0.9 * content, clip)

        # ---------- scene ----------
        if content > 0.004 and st >= self.starts[0]:
            self._stage(out, st, index, step, u, content, clip,
                        band_top, band_h)

        # ---------- habillage HUD ----------
        self._fx(out, "vignette", SCREEN_W / 2.0, BAND_CY, 1.0, 0.85, clip)
        self._fx(out, "frame", SCREEN_W / 2.0, BAND_CY, 1.0, content, clip)

        # Liseres : ils s'illuminent a chaque coupe.
        pulse = (0.55 + 0.45 * math.exp(-u / 0.13)) * clamp(open_p * 2.0)
        self._solid(out, EDGE, 0, int(band_top), SCREEN_W, 3, pulse)
        self._solid(out, EDGE, 0, int(band_top + band_h) - 3, SCREEN_W, 3, pulse)

        if content > 0.004:
            self._hud(out, st, index, step, u, last, content)

            # Flash de conclusion.
            if last and u < 0.45:
                self._solid(out, FLASH, 0, int(band_top), SCREEN_W,
                            int(band_h), 0.42 * math.exp(-u / 0.10) * content)

        return out

    # --------------------------------------------------------------
    def _stage(self, out, st, index, step, u, content, clip,
               band_top, band_h):
        """Le chibi et tout ce qui gravite autour de lui."""
        spec = self.spec
        x0, cw = spec.cell_rect(step.cell)
        sh = spec.sheet_h
        zoom = spec.zoom
        cell_size = (cw, sh)

        # --- Deformation d'arrivee : squash & stretch amorti ---
        e = clamp(u / 0.30)
        damp = (1.0 - e) ** 2
        osc = math.cos(e * math.pi * 2.15) * damp
        xz = 1.0 - 0.15 * osc
        yz = 1.0 + 0.19 * osc

        # --- Saut d'arrivee ---
        yoff = -52.0 * step.hop * math.sin(math.pi * clamp(u / 0.32))
        xoff = 0.0
        rot = (6.5 if index % 2 == 0 else -6.5) * damp * step.hop

        # --- Respiration une fois pose ---
        settled = clamp((u - 0.28) / 0.26)
        breath = math.sin(st * 2.0 * math.pi / 1.7)
        yz *= 1.0 + 0.014 * breath * settled
        yoff += 4.0 * breath * settled

        # --- Grelottement (torse nu) ---
        if step.shiver > 0.0:
            amp = step.shiver * (0.55 + 0.45 * math.cos(u * 2.6))
            xoff += amp * math.sin(u * 47.0)
            yoff += amp * 0.35 * math.sin(u * 61.0)

        # --- Conclusion : leger zoom avant ---
        if step.final:
            grow = 1.0 + 0.055 * out_cubic(u / 0.85)
            xz *= grow
            yz *= grow
            yoff -= 12.0 * out_cubic(u / 0.85)

        sx = zoom * xz
        sy = zoom * yz
        cx = spec.chibi_x + xoff
        # Les pieds (content_bottom) doivent tomber sur feet_y.
        cy = spec.feet_y + yoff - (spec.content_bottom - sh * 0.5) * sy
        torso_y = (spec.feet_y + yoff
                   - 0.52 * (spec.content_bottom - spec.content_top) * sy)

        # ---- Halo ----
        halo = 0.40 + 0.08 * math.sin(st * 1.9) + 0.26 * math.exp(-u / 0.18)
        self._fx(out, "glow", cx, torso_y,
                 1.30 + 0.05 * math.sin(st * 1.4), halo * content, clip)

        # ---- Lignes de vitesse ----
        if u < 0.32:
            k = u / 0.32
            self._fx(out, "speedlines", cx, torso_y,
                     (1.42 if step.final else 1.20) * (0.94 + 0.14 * k),
                     (1.0 - k) ** 1.5 * 0.50 * content, clip)

        # ---- Anneau d'impact ----
        if u < 0.42:
            k = u / 0.42
            self._fx(out, "ring", cx, torso_y,
                     (0.45 + 2.05 * out_cubic(k)) * (1.30 if step.final else 1.0),
                     (1.0 - k) ** 1.8 * 0.30 * content, clip)

        # ---- Reflet au sol, noye par le degrade du plancher ----
        self._img(out, ("cell", step.cell), cell_size,
                  cx, 2.0 * spec.feet_y - cy, sx, -sy,
                  0.22 * content, clip=clip, origin=(x0, 0))
        self._fx(out, "floor", SCREEN_W / 2.0,
                 band_top + band_h - FX_SIZE["floor"][1] / 2.0,
                 1.0, content, clip)

        # ---- Ombre portee : elle s'ecrase quand il retombe ----
        self._fx(out, "shadow", cx, spec.feet_y + 6,
                 clamp(1.00 + yoff / 150.0, 0.34, 1.06),
                 0.72 * content, clip)

        # ---- Poussiere soulevee par le saut ----
        if u < 0.40 and step.hop > 0.0:
            for (side, scale, life) in self.dust[index]:
                if u > life:
                    continue
                p = u / life
                self._fx(out, "dot",
                         cx + side * (34.0 + 130.0 * p),
                         spec.feet_y - 8.0 - 30.0 * math.sin(math.pi * p) * scale,
                         (0.7 + 1.7 * p) * scale,
                         (1.0 - p) ** 1.6 * 0.45 * content, clip)

        # ---- Image remanente de la case precedente ----
        if u < 0.20 and index > 0:
            k = u / 0.20
            prev = spec.steps[index - 1].cell
            px0, pcw = spec.cell_rect(prev)
            gz = zoom * (1.0 + 0.09 * k)
            # Ancree sur le sol, sans le saut ni la deformation : la case
            # precedente reste ou elle etait et s'evapore sur place.
            self._img(out, ("cell", prev), (pcw, sh),
                      spec.chibi_x - 18.0 * k,
                      spec.feet_y - (spec.content_bottom - sh * 0.5) * gz,
                      gz, gz, (1.0 - k) ** 1.6 * 0.40 * content,
                      bright=0.30, origin=(px0, 0))

        # ---- Le chibi ----
        bright = 0.78 * math.exp(-u / 0.055)
        self._img(out, ("cell", step.cell), cell_size, cx, cy, sx, sy,
                  content, rotate=(rot if abs(rot) > 0.05 else 0.0),
                  bright=(bright if bright >= 0.02 else 0.0),
                  tint=(None if bright >= 0.02 else step.tint),
                  origin=(x0, 0))

        # ---- Etincelles ----
        for (ang, speed, size, life, spin) in self.sparks[index]:
            if u >= life:
                continue
            p = u / life
            px = cx + math.cos(ang) * speed * u
            py = torso_y + math.sin(ang) * speed * u + 340.0 * u * u
            fade = (1.0 - p) ** 1.4
            edge = clamp(min(py - clip[1], clip[1] + clip[3] - py) / 46.0)
            if edge <= 0.0:
                continue
            self._fx(out, "spark", px, py, size * (0.45 + 0.95 * fade),
                     fade * 0.9 * content * edge, rotate=spin * u)

        # ---- Trainee lumineuse qui balaie le bandeau ----
        if u < 0.36:
            k = u / 0.36
            self._fx(out, "streak",
                     -420.0 + (SCREEN_W + 840.0) * out_cubic(k), BAND_CY, 1.0,
                     math.sin(math.pi * k) * (0.75 if step.final else 0.40) * content,
                     clip)

    # --------------------------------------------------------------
    def _hud(self, out, st, index, step, u, last, content):
        """Bloc de gauche : intitule, jauge d'etapes, pied de bloc."""
        spec = self.spec
        n = len(spec.steps)

        if spec.captions:
            y_bar, y_kicker = Y_BAR, Y_KICKER
            y_gauge, y_footer = Y_GAUGE, Y_FOOTER

            # Entree puis sortie de la legende.
            alpha = out_cubic(u / 0.24)
            slide = -36.0 * (1.0 - alpha)
            if not last:
                left = step.hold - u
                if left < 0.16:
                    fade_out = clamp(left / 0.16)
                    alpha *= fade_out
                    slide += 22.0 * (1.0 - fade_out)
            alpha *= content

            # Numero d'etape en filigrane, entre le texte et le chibi.
            self._text(out, "ghost", index, GHOST_X + slide * 0.5, GHOST_Y,
                       0.085 * alpha)
            self._text(out, "counter", index, TX + slide, Y_COUNTER, alpha)
            self._text(out, "caption", index, TX + slide * 1.4, Y_CAPTION,
                       alpha)
        else:
            y_bar, y_kicker = Y_BAR_LEAN, Y_KICKER_LEAN
            y_gauge, y_footer = Y_GAUGE_LEAN, Y_FOOTER_LEAN

        # Barre d'accent + intitule de la sequence.
        self._solid(out, ACCENT, TX, y_bar, 6, 54, 0.95 * content)
        self._text(out, "kicker", 0, TX + 22, y_kicker, 0.85 * content)

        # Jauge d'etapes.
        for i in range(n):
            x = TX + i * (SEG_W + SEG_GAP)
            if i < index:
                self._solid(out, ACCENT, x, y_gauge, SEG_W, SEG_H,
                            0.90 * content)
            elif i == index:
                grow = out_cubic(u / 0.22)
                h = SEG_H + 7.0 * (1.0 - grow)
                self._fx(out, "dot", x + SEG_W / 2.0, y_gauge + SEG_H / 2.0,
                         1.9, (1.0 - grow) * 0.55 * content)
                self._solid(out, ACCENT, x, y_gauge + (SEG_H - h) / 2.0,
                            SEG_W, h, content)
            else:
                self._solid(out, SEG_OFF, x, y_gauge, SEG_W, SEG_H,
                            0.30 * content)

        # Pied du bloc : la chute change a la derniere etape.
        style = "footer_final" if last else "footer"
        fade = content * (out_cubic(u / 0.30) if last else 1.0)
        self._text(out, style, 0, TX, y_footer, 0.85 * fade)
