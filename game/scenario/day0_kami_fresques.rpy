# Jour 0 : trois fresques panoramiques du souvenir de Kami.
# Chaque fresque traverse l'écran de gauche a droite pendant 30 secondes.
define D0_KAMI_FRESCO_DIR = "images/ui/0/s4_kami/"
define D0_KAMI_FRESCO_DURATION = 30.0
define D0_KAMI_FRESCO_ZOOM = 1.85

init python:
    def d0_kami_fresco_frame(st, at, index):
        path = D0_KAMI_FRESCO_DIR + "fresque_%d.png" % index
        w, h = config.screen_width, config.screen_height
        if not renpy.loadable(path):
            # Ne pas faire planter le prologue si un asset manque.
            return Fixed(Solid("#060a13"), xysize=(w, h)), 0.20

        iw, ih = renpy.image_size(path)
        # Le zoom s'applique au panorama lui-meme ; le cadre Ren'Py
        # demeure a la taille du viewport et masque les debordements.
        scale = max(float(w) / iw, float(h) / ih) * D0_KAMI_FRESCO_ZOOM
        sw, sh = int(iw * scale), int(ih * scale)
        progress = min(1.0, max(0.0, st / D0_KAMI_FRESCO_DURATION))
        x = int((w - sw) * progress)
        y = (h - sh) // 2
        picture = Transform(Image(path), xysize=(sw, sh), xpos=x, ypos=y)
        return Fixed(Solid("#060a13"), picture, xysize=(w, h)), 0.033

    def d0_kami_fresco(index):
        return DynamicDisplayable(d0_kami_fresco_frame, index)

screen d0_kami_fresco_screen(index):
    # Simple fond animé, jamais modal : les dialogues restent au-dessus
    # et le travelling continue pendant que le joueur lit et clique.
    zorder -10
    add d0_kami_fresco(index)
    add Solid("#060a13") at d0_kami_fresco_reveal

transform d0_kami_fresco_reveal:
    alpha 1.0
    ease 0.65 alpha 0.0
