# Jour 0 — panoramas Kami. Travelling GPU natif Ren'Py (ATL), sans
# DynamicDisplayable ni recreation de Transform 30 fois par seconde.
define D0_KAMI_FRESCO_DIR = "images/ui/0/s4_kami/"
define D0_KAMI_FRESCO_DURATION = 30.0
define D0_KAMI_FRESCO_ZOOM = 1.85

init python:
    _d0_kami_fresco_cache = {}

    def d0_kami_fresco_image(index):
        path = D0_KAMI_FRESCO_DIR + "fresque_%d.png" % index
        w, h = config.screen_width, config.screen_height
        key = (index, w, h)
        if key not in _d0_kami_fresco_cache:
            if not renpy.loadable(path):
                _d0_kami_fresco_cache[key] = Solid("#060a13", xsize=w, ysize=h)
            else:
                iw, ih = renpy.image_size(path)
                scale = max(float(w) / iw, float(h) / ih) * D0_KAMI_FRESCO_ZOOM
                sw, sh = int(iw * scale), int(ih * scale)
                # Une seule composition calculee par fresque et resolution.
                _d0_kami_fresco_cache[key] = Transform(Image(path), xysize=(sw, sh))
        return _d0_kami_fresco_cache[key]

# subpixel True supprime les sauts de pixels lors d'un lent travelling.
# xalign 0 : bord gauche visible ; xalign 1 : bord droit visible.
# L'ATL continue de jouer entre les interactions de dialogue.
transform d0_kami_fresco_pan:
    subpixel True
    xalign 0.0
    yalign 0.5
    linear D0_KAMI_FRESCO_DURATION xalign 1.0

transform d0_kami_fresco_reveal:
    alpha 1.0
    linear 0.65 alpha 0.0

screen d0_kami_fresco_screen(index):
    zorder -10
    # Ni timer ni modal : ne bloque jamais la lecture des repliques.
    add d0_kami_fresco_image(index) at d0_kami_fresco_pan
    add Solid("#060a13") at d0_kami_fresco_reveal
