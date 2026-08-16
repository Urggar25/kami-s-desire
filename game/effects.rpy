# ============================================================
# effects.rpy — Game feel / juice centralisé
# Shakes paramétrés, flashs, letterbox, interjections type
# Danganronpa / Ace Attorney. ATL + Python pur, zéro asset.
#
# Usage rapide :
#   with flash_white          # impact lumineux
#   with flash_red            # coup / danger
#   $ shake()                 # secousse standard
#   $ shake(18, 0.5)          # secousse forte
#   $ impact()                # flash + shake combinés
#   $ letterbox_on()          # bandes cinéma
#   $ letterbox_off()
#   $ interject("OBJECTION !")            # slam texte plein écran
#   $ interject("VERDICT", color="#ff3344")
# ============================================================


# ------------------------------------------------------------
# Transitions flash
# ------------------------------------------------------------
define flash_white  = Fade(0.06, 0.0, 0.30, color="#ffffff")
define flash_red    = Fade(0.06, 0.0, 0.35, color="#c81e2e")
define flash_cyan   = Fade(0.06, 0.0, 0.30, color="#5cd3ff")
define cut_black    = Fade(0.0, 0.08, 0.20, color="#000000")

define quick_dissolve = Dissolve(0.15)
define soft_dissolve  = Dissolve(0.6)


# ------------------------------------------------------------
# Shake paramétré (remplace avantageusement screen_shake/heavy_shake)
# ------------------------------------------------------------
init python:
    import random as _random
    from functools import partial as _partial

    def _shake_func(trans, st, at, intensity=10, duration=0.30, vertical=0.5):
        if st > duration:
            trans.xoffset = 0
            trans.yoffset = 0
            return None
        # Amortissement progressif
        damp = 1.0 - (st / duration)
        trans.xoffset = int(_random.uniform(-intensity, intensity) * damp)
        trans.yoffset = int(_random.uniform(-intensity, intensity) * damp * vertical)
        return 0.0

    def shake(intensity=10, duration=0.30, layers=("bgcam", "master")):
        """Secousse de caméra amortie sur les layers du jeu."""
        tr = Transform(function=_partial(_shake_func, intensity=intensity, duration=duration))
        for ly in layers:
            renpy.show_layer_at([tr], layer=ly)
        # Nettoyage : réapplique la caméra courante après la secousse
        renpy.pause(duration, hard=True)
        for ly in layers:
            renpy.show_layer_at([], layer=ly)
        # Restaure le zoom cinéma s'il était actif
        cam_restore_current(t=0.0, layers=layers)

    def impact(intensity=14, duration=0.35, color="#ffffff"):
        """Flash + shake : ponctuation forte (révélation, coup, twist)."""
        renpy.with_statement(Fade(0.05, 0.0, 0.25, color=color))
        shake(intensity, duration)


# ------------------------------------------------------------
# Letterbox cinéma
# ------------------------------------------------------------
transform _letterbox_top_in(h=110, t=0.4):
    xpos 0 ypos 0 xanchor 0 yanchor 0
    xsize config.screen_width
    ysize 0
    easeout t ysize h

transform _letterbox_bot_in(h=110, t=0.4):
    xpos 0 ypos config.screen_height xanchor 0 yanchor 1.0
    xsize config.screen_width
    ysize 0
    easeout t ysize h

screen letterbox_overlay(h=110, t=0.4):
    zorder 900
    add Solid("#000") at _letterbox_top_in(h, t)
    add Solid("#000") at _letterbox_bot_in(h, t)

init python:
    def letterbox_on(h=110, t=0.4):
        renpy.show_screen("letterbox_overlay", h=h, t=t)

    def letterbox_off():
        renpy.hide_screen("letterbox_overlay")


# ------------------------------------------------------------
# Interjection type Ace Attorney / Danganronpa
# Slam de texte plein écran + shake, auto-hide.
# ------------------------------------------------------------
transform _interject_slam:
    alpha 0.0
    zoom 3.0
    rotate -6
    easein 0.12 alpha 1.0 zoom 1.0
    easeout 0.05 zoom 1.06
    easein 0.05 zoom 1.0
    pause 0.9
    linear 0.15 alpha 0.0

transform _interject_bg:
    alpha 0.0
    linear 0.08 alpha 1.0
    pause 1.04
    linear 0.15 alpha 0.0

screen interjection_screen(txt, color="#5cd3ff"):
    zorder 950
    modal True

    add Solid("#000000aa") at _interject_bg

    text txt at _interject_slam:
        xalign 0.5
        yalign 0.42
        size 160
        font "fonts/Rajdhani-SemiBold.ttf"
        color color
        outlines [(8, "#050813", 0, 0), (3, "#ffffff", 0, 0)]
        kerning 6

    timer 1.35 action Hide("interjection_screen")

init python:
    def interject(txt, color="#5cd3ff", shake_after=True):
        renpy.show_screen("interjection_screen", txt=txt, color=color)
        if shake_after:
            shake(12, 0.30)
            renpy.pause(1.05, hard=True)
        else:
            renpy.pause(1.35, hard=True)


# ------------------------------------------------------------
# Pulsation d'alerte (bord d'écran rouge) — tension / danger
# ------------------------------------------------------------
transform _danger_pulse:
    alpha 0.0
    block:
        linear 0.8 alpha 0.35
        linear 0.8 alpha 0.10
        repeat

init python:
    def danger_on():
        renpy.show_screen("danger_vignette")

    def danger_off():
        renpy.hide_screen("danger_vignette")

# Vignette rouge par bandes (sans shader, sans image)
screen danger_vignette():
    zorder 890

    add Solid("#c81e2e") at _danger_pulse:
        xpos 0 ypos 0 xsize config.screen_width ysize 14
    add Solid("#c81e2e") at _danger_pulse:
        xpos 0 ypos (config.screen_height - 14) xsize config.screen_width ysize 14
    add Solid("#c81e2e") at _danger_pulse:
        xpos 0 ypos 0 xsize 14 ysize config.screen_height
    add Solid("#c81e2e") at _danger_pulse:
        xpos (config.screen_width - 14) ypos 0 xsize 14 ysize config.screen_height
