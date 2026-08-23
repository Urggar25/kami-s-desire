"""Render the chibi montage outside Ren'Py, straight from its shared core.

The drawing operations come from game/python-packages/chibi_montage_core.py,
the very module the in-game engine consumes, so the preview cannot drift
from what the player sees.

    python tools/preview_chibi_montage.py                 # -> preview.gif
    python tools/preview_chibi_montage.py --fps 30 --scale 0.5
    python tools/preview_chibi_montage.py --sheet 0.4,1.5,2.8  # planche PNG
    python tools/preview_chibi_montage.py --check              # validation seule
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
sys.path.insert(0, str(GAME / "python-packages"))

import chibi_montage_core as cmc  # noqa: E402


# The spec mirrors the `define` in game/chibi_montage.rpy.
SPEC = cmc.ChibiMontageSpec(
    sheet="images/background/interact/animation/noam_change/noam_change_frames.png",
    sheet_size=(3104, 724),
    cols=8,
    content=(17, 697),
    chibi_x=1240,
    feet_y=852,
    zoom=0.88,
    captions=False,
    kicker=u"SÉQUENCE — HABILLAGE",
    footer=u"LYSA ATTEND DEVANT LA PORTE",
    footer_final=u"CINQ MINUTES. À PEU PRÈS.",
    steps=[
        cmc.ChibiStep(0, 0.62, u"RÉVEIL"),
        cmc.ChibiStep(1, 0.54, u"ENCORE EN PYJAMA"),
        cmc.ChibiStep(2, 0.70, u"BRRR.", tint="#c6d8ff", shiver=5.0),
        cmc.ChibiStep(3, 0.60, u"CHEMISE"),
        cmc.ChibiStep(4, 0.56, u"BOUTONS ALIGNÉS"),
        cmc.ChibiStep(5, 0.62, u"VESTE"),
        cmc.ChibiStep(6, 0.54, u"MANCHES AJUSTÉES"),
        cmc.ChibiStep(7, 1.15, u"PRÊT.", hop=1.15, final=True),
    ],
)


class Renderer(object):

    def __init__(self, spec, background=None):
        self.spec = spec
        self.timeline = cmc.ChibiTimeline(spec)
        self.sheet = Image.open(GAME / spec.sheet).convert("RGBA")
        self.fx = {
            name: Image.open(GAME / (cmc.FX_DIR + name + ".png")).convert("RGBA")
            for name in cmc.FX_SIZE
        }
        self.fonts = {}
        self.background = background

    def font(self, style):
        info = cmc.TEXT_STYLES[style]
        key = (info["font"], info["size"])
        if key not in self.fonts:
            self.fonts[key] = ImageFont.truetype(str(GAME / info["font"]),
                                                 info["size"])
        return self.fonts[key]

    # -- helpers ---------------------------------------------------
    @staticmethod
    def _rgb(color):
        color = color.lstrip("#")
        return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def _scale_alpha(img, alpha):
        if alpha >= 0.999:
            return img
        band = img.getchannel("A").point(lambda v: int(v * alpha))
        img = img.copy()
        img.putalpha(band)
        return img

    def _source(self, op):
        kind, key = op["src"]
        return self.fx[key] if kind == "fx" else self.sheet

    # -- one frame -------------------------------------------------
    def frame(self, st):
        if self.background is not None:
            canvas = self.background.copy()
        else:
            canvas = Image.new("RGBA", (cmc.SCREEN_W, cmc.SCREEN_H),
                               (16, 20, 26, 255))
        draw = ImageDraw.Draw(canvas)

        for op in self.timeline.ops(st):
            kind = op["kind"]

            if kind == "img":
                x, y, w, h = op["crop"]
                piece = self._source(op).crop((x, y, x + w, y + h))

                dw = max(1, int(round(w * abs(op["xzoom"]))))
                dh = max(1, int(round(h * abs(op["yzoom"]))))
                piece = piece.resize((dw, dh), Image.LANCZOS)
                if op["xzoom"] < 0:
                    piece = piece.transpose(Image.FLIP_LEFT_RIGHT)
                if op["yzoom"] < 0:
                    piece = piece.transpose(Image.FLIP_TOP_BOTTOM)

                if op["bright"]:
                    add = int(op["bright"] * 255)
                    r, g, b, a = piece.split()
                    lut = [min(255, v + add) for v in range(256)]
                    piece = Image.merge("RGBA", (r.point(lut), g.point(lut),
                                                 b.point(lut), a))
                elif op["tint"]:
                    tr, tg, tb = self._rgb(op["tint"])
                    r, g, b, a = piece.split()
                    piece = Image.merge("RGBA", (
                        r.point(lambda v: v * tr // 255),
                        g.point(lambda v: v * tg // 255),
                        b.point(lambda v: v * tb // 255), a))

                if op["rotate"]:
                    # Ren'Py tourne dans le sens horaire, PIL dans l'autre.
                    piece = piece.rotate(-op["rotate"], resample=Image.BICUBIC,
                                         expand=True)

                piece = self._scale_alpha(piece, op["alpha"])
                canvas.alpha_composite(
                    piece,
                    (int(round(op["cx"] - piece.width / 2.0)),
                     int(round(op["cy"] - piece.height / 2.0))))

            elif kind == "solid":
                patch = Image.new("RGBA", (op["w"], op["h"]),
                                  self._rgb(op["color"])
                                  + (int(op["alpha"] * 255),))
                canvas.alpha_composite(patch, (int(op["x"]), int(op["y"])))

            else:
                info = cmc.TEXT_STYLES[op["style"]]
                body = self.text_body(op)
                layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
                pen = ImageDraw.Draw(layer)
                shadow = info.get("shadow")
                if shadow:
                    self._draw_spaced(pen, op["x"] + shadow[0],
                                      op["y"] + shadow[1], body,
                                      self.font(op["style"]),
                                      self._rgb(shadow[2]) + (170,),
                                      info.get("kerning", 0))
                self._draw_spaced(pen, op["x"], op["y"], body,
                                  self.font(op["style"]),
                                  self._rgb(info["color"]) + (255,),
                                  info.get("kerning", 0))
                canvas.alpha_composite(self._scale_alpha(layer, op["alpha"]))

        del draw
        return canvas

    @staticmethod
    def _draw_spaced(pen, x, y, body, font, fill, kerning):
        """Reproduit l'interlettrage de Ren'Py (`kerning`)."""
        if not kerning:
            pen.text((x, y), body, font=font, fill=fill)
            return
        for char in body:
            pen.text((x, y), char, font=font, fill=fill)
            x += pen.textlength(char, font=font) + kerning

    def text_body(self, op):
        spec = self.spec
        style, i = op["style"], op["index"]
        if style == "kicker":
            return spec.kicker
        if style == "footer":
            return spec.footer
        if style == "footer_final":
            return spec.footer_final
        if style == "counter":
            return u"ÉTAPE %02d / %02d" % (i + 1, len(spec.steps))
        if style == "ghost":
            return u"%02d" % (i + 1)
        return spec.steps[i].caption


def check(spec):
    """Valide chaque operation de dessin sur toute la sequence.

    Garde-fou contre les erreurs qui ne se verraient qu'au runtime Ren'Py :
    rognage hors de l'image source, opacite hors bornes, zoom nul, NaN.
    """
    timeline = cmc.ChibiTimeline(spec)
    sheet = (spec.sheet_w, spec.sheet_h)
    total = 0
    peak = 0

    for i in range(int(timeline.duration * 240) + 240):
        st = i / 240.0
        ops = timeline.ops(st)
        peak = max(peak, len(ops))
        for op in ops:
            total += 1
            alpha = op["alpha"]
            assert 0.0 <= alpha <= 1.0 and alpha == alpha, (st, op)

            if op["kind"] == "img":
                bw, bh = (cmc.FX_SIZE[op["src"][1]]
                          if op["src"][0] == "fx" else sheet)
                x, y, w, h = op["crop"]
                assert 0 <= x and 0 <= y and w >= 1 and h >= 1, (st, op)
                assert x + w <= bw and y + h <= bh, (st, op, bw, bh)
                assert abs(op["xzoom"]) > 0 and abs(op["yzoom"]) > 0, (st, op)
                for key in ("cx", "cy", "xzoom", "yzoom", "rotate"):
                    value = op[key]
                    assert value == value and abs(value) < 1e6, (st, key, value)
            elif op["kind"] == "solid":
                assert op["w"] >= 1 and op["h"] >= 1, (st, op)
            else:
                assert op["style"] in cmc.TEXT_STYLES, op
                assert 0 <= op["index"] < len(spec.steps), op

    print("ok : %d operations valides sur %.2f s (%d max par image)"
          % (total, timeline.duration, peak))
    print("coupes :", ", ".join("%.2f" % s for s in timeline.starts))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fps", type=float, default=25.0)
    ap.add_argument("--scale", type=float, default=0.5)
    ap.add_argument("--out", default=str(ROOT / "tmp" / "chibi_montage_preview.gif"))
    ap.add_argument("--sheet", default=None,
                    help="temps séparés par des virgules -> planche PNG")
    ap.add_argument("--check", action="store_true",
                    help="valide la sequence sans rien dessiner")
    ap.add_argument("--background", default=None,
                    help="image de fond derrière le bandeau")
    args = ap.parse_args()

    if args.check:
        check(SPEC)
        return

    background = None
    if args.background:
        background = Image.open(args.background).convert("RGBA").resize(
            (cmc.SCREEN_W, cmc.SCREEN_H))

    renderer = Renderer(SPEC, background)
    duration = renderer.timeline.duration
    size = (int(cmc.SCREEN_W * args.scale), int(cmc.SCREEN_H * args.scale))

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.sheet:
        times = [float(t) for t in args.sheet.split(",")]
        cols = 2
        rows = (len(times) + cols - 1) // cols
        sheet = Image.new("RGB", (size[0] * cols, size[1] * rows), (18, 18, 22))
        pen = ImageDraw.Draw(sheet)
        for i, t in enumerate(times):
            img = renderer.frame(t).convert("RGB").resize(size)
            sheet.paste(img, ((i % cols) * size[0], (i // cols) * size[1]))
            pen.text(((i % cols) * size[0] + 8, (i // cols) * size[1] + 6),
                     "t=%.2f" % t, fill=(255, 214, 0))
        sheet.save(out.with_suffix(".png"))
        print("planche ->", out.with_suffix(".png"))
        return

    frames = []
    n = int(duration * args.fps)
    for i in range(n):
        st = i / args.fps
        frames.append(renderer.frame(st).convert("RGB").resize(size))
        if i % 25 == 0:
            print("  frame %d/%d" % (i, n))

    frames[0].save(out, save_all=True, append_images=frames[1:],
                   duration=int(1000 / args.fps), loop=0, optimize=True)
    print("apercu ->", out, "(%.2f s, %d images)" % (duration, n))


if __name__ == "__main__":
    main()
