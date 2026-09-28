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

default flashlight_pattern = 0

# ------------------------------------------------------------
# Image sous lampe — masque mobile en boucle
# ------------------------------------------------------------
transform _flashlight_round:
    subpixel True
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    ease 0.58 xoffset 120 yoffset -78
    ease 0.58 xoffset 190 yoffset 0
    ease 0.58 xoffset 120 yoffset 78
    ease 0.58 xoffset 0 yoffset 112
    ease 0.58 xoffset -120 yoffset 78
    ease 0.58 xoffset -190 yoffset 0
    ease 0.58 xoffset -120 yoffset -78
    ease 0.58 xoffset 0 yoffset 0

transform _flashlight_eight:
    subpixel True
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    ease 0.60 xoffset 150 yoffset -92
    ease 0.60 xoffset 0 yoffset -18
    ease 0.60 xoffset -150 yoffset -92
    ease 0.60 xoffset 0 yoffset 0
    ease 0.60 xoffset 150 yoffset 92
    ease 0.60 xoffset 0 yoffset 18
    ease 0.60 xoffset -150 yoffset 92
    ease 0.60 xoffset 0 yoffset 0

transform _flashlight_horizontal:
    subpixel True
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    ease 1.20 xoffset -210
    ease 2.40 xoffset 210
    ease 1.20 xoffset 0

transform _flashlight_vertical:
    subpixel True
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    ease 1.20 yoffset -125
    ease 2.40 yoffset 125
    ease 1.20 yoffset 0

transform _flashlight_diagonal:
    subpixel True
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    ease 1.20 xoffset -190 yoffset -115
    ease 2.40 xoffset 190 yoffset 115
    ease 1.20 xoffset 0 yoffset 0

screen flashlight_reveal_overlay():
    zorder 860

    if flashlight_pattern == 0:
        add "images/effects/flashlight_vignette.svg" at _flashlight_round
    elif flashlight_pattern == 1:
        add "images/effects/flashlight_vignette.svg" at _flashlight_eight
    elif flashlight_pattern == 2:
        add "images/effects/flashlight_vignette.svg" at _flashlight_horizontal
    elif flashlight_pattern == 3:
        add "images/effects/flashlight_vignette.svg" at _flashlight_vertical
    else:
        add "images/effects/flashlight_vignette.svg" at _flashlight_diagonal

    timer 4.8 action Function(_flashlight_next_pattern) repeat True

init python:
    def _flashlight_next_pattern():
        previous = int(getattr(store, "flashlight_pattern", 0))
        choices = [value for value in range(5) if value != previous]
        store.flashlight_pattern = renpy.random.choice(choices)
        renpy.restart_interaction()

    def flashlight_on(pattern=None):
        if pattern is None:
            store.flashlight_pattern = renpy.random.randint(0, 4)
        else:
            store.flashlight_pattern = max(0, min(4, int(pattern)))
        renpy.show_screen("flashlight_reveal_overlay", _layer="lighting")

    def flashlight_off():
        renpy.hide_screen("flashlight_reveal_overlay", layer="lighting")


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
# Stress périphérique — tension organique sans masquer l'action
# ------------------------------------------------------------
transform _stress_breathe:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.0
    alpha 0.42
    block:
        ease 2.25 alpha 0.62 zoom 1.008
        ease 2.85 alpha 0.40 zoom 1.0
        repeat

init python:
    def danger_on():
        renpy.show_screen("danger_vignette")

    def danger_off():
        renpy.hide_screen("danger_vignette")

# Vignette sombre et diffuse : le centre de l'image reste totalement lisible.
screen danger_vignette():
    zorder 890

    add "images/effects/stress_vignette.svg" at _stress_breathe


# ------------------------------------------------------------
# Révélation de doppelgänger — noir, regard, sourire et screamer
# ------------------------------------------------------------
transform _doppel_dark_in:
    alpha 0.0
    linear 0.12 alpha 0.96

transform _doppel_eyes_reveal:
    subpixel True
    xalign 0.5 yalign 0.5
    alpha 0.0
    zoom 0.94
    pause 0.10
    easein 0.16 alpha 0.92 zoom 1.0
    block:
        pause 0.30
        linear 0.035 xoffset -3
        linear 0.035 xoffset 2
        linear 0.035 xoffset 0
        pause 0.38
        repeat

transform _doppel_smile_reveal:
    subpixel True
    xalign 0.5 yalign 0.5
    alpha 0.0
    zoom 0.98
    pause 0.34
    easein 0.20 alpha 0.88 zoom 1.0

transform _doppel_screamer:
    subpixel True
    xalign 0.5 yalign 0.5
    alpha 0.0
    zoom 0.72
    pause 0.30
    linear 0.06 alpha 1.0 zoom 1.28
    block:
        linear 0.025 xoffset -11 yoffset 5
        linear 0.025 xoffset 10 yoffset -4
        linear 0.025 xoffset -6 yoffset -3
        linear 0.025 xoffset 0 yoffset 0
        repeat

screen doppelganger_reveal_overlay(screamer=False):
    zorder 945

    add Solid("#000000") at _doppel_dark_in
    add "images/effects/doppelganger_eyes.svg" at _doppel_eyes_reveal
    if screamer:
        add "images/effects/doppelganger_smile.svg" at _doppel_screamer
    else:
        add "images/effects/doppelganger_smile.svg" at _doppel_smile_reveal

init python:
    def doppelganger_reveal(screamer=False, duration=1.05, restore_volume=0.72):
        """Isole un visage impossible dans le noir, avec un impact optionnel."""
        duration = max(0.68, float(duration))
        renpy.music.set_volume(0.04, delay=0.08, channel="music")
        renpy.play("audio/sfx_gresillement.mp3", channel="sound")
        renpy.show_screen("doppelganger_reveal_overlay", screamer=bool(screamer))
        renpy.pause(0.48, hard=True)
        if screamer:
            renpy.play("audio/sfx_exclamation_horror.mp3", channel="sound")
            shake(15, 0.24)
        renpy.pause(max(0.05, duration - 0.48), hard=True)
        renpy.hide_screen("doppelganger_reveal_overlay")
        renpy.music.set_volume(float(restore_volume), delay=0.70, channel="music")

transform slow_zoom_in:
    zoom 1.0
    linear 8.0 zoom 1.12

transform slow_zoom_creep:
    subpixel True
    zoom 1.0 xalign 0.5 yalign 0.5
    linear 12.0 zoom 1.18 xalign 0.45

transform unease_drift:
    subpixel True
    xoffset 0 yoffset 0
    block:
        linear 3.0 xoffset 4 yoffset -3
        linear 3.0 xoffset -4 yoffset 3
        repeat

transform hard_flash:
    alpha 1.0
    linear 0.12 alpha 0.0

transform breathe_dark:
    matrixcolor TintMatrix("#c8d0dd") * BrightnessMatrix(0.0)
    block:
        linear 2.5 matrixcolor TintMatrix("#c8d0dd") * BrightnessMatrix(-0.12)
        linear 2.5 matrixcolor TintMatrix("#c8d0dd") * BrightnessMatrix(0.0)
        repeat

image flash_white = Solid("#ffffff")
image flash_black = Solid("#000000")
image vignette_soft = Solid("#00000055")  # remplace par un vrai PNG vignette si dispo

# Transitions horreur
define creep_diss = Dissolve(2.2)
define snap_black = Dissolve(0.05)                 # coupe quasi-instant vers le noir
define slow_black = Dissolve(3.0)
define pulse_red  = Fade(0.15, 0.0, 0.15, color="#3a0000")
define blink      = Dissolve(0.08)

# Glitch transition (empilement rapide) — à utiliser avec 'with glitch_diss'
define glitch_diss = MultipleTransition([
    False, Dissolve(0.04),
    True,  Dissolve(0.04),
    False, Dissolve(0.04),
    True,  Dissolve(0.04),
    True
])

# Rupture de signal plus sèche que glitch_diss : l'image saute avant de tenir.
define signal_stutter = MultipleTransition([
    False, Dissolve(0.025),
    True,  Dissolve(0.025),
    False, Dissolve(0.050),
    True,  Dissolve(0.030),
    False, Dissolve(0.025),
    True
])

# Coupures dédiées aux pertes de mémoire et aux scènes d'étouffement.
define memory_rip = Fade(0.05, 0.16, 0.45, color="#d9f7ff")
define suffocation_cut = Fade(0.04, 0.38, 0.85, color="#240008")

# Pixellate montante (montée d'angoisse)
define dread_pix = Pixellate(1.2, 6)

transform afterimage:
    # rémanence fantôme qui s'efface
    alpha 0.55 zoom 1.02
    linear 1.6 alpha 0.0 zoom 1.06

transform push_in_fast:
    zoom 1.0
    easein 0.4 zoom 1.15

transform lean_left:
    subpixel True
    linear 6.0 xoffset -18 zoom 1.06

transform horror_push:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.0
    easein 5.0 zoom 1.16 yoffset 14

transform corridor_crawl:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.04 xoffset -8
    linear 8.0 zoom 1.18 xoffset 18

# Mouvements longs destinés aux décors seuls. Leur amplitude reste assez
# faible pour que l'animation soit ressentie sans distraire du dialogue.
transform living_background:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.04
    block:
        ease 5.8 xoffset -30 yoffset -14 zoom 1.10
        ease 6.8 xoffset 30 yoffset 12 zoom 1.04
        repeat

transform haunted_background:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.04
    linear 10.0 zoom 1.18 xoffset 30 yoffset 14

transform shuttle_background:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.04
    block:
        ease 4.5 xoffset -12 yoffset -14 rotate -0.35 zoom 1.075
        ease 4.5 xoffset 12 yoffset 14 rotate 0.35 zoom 1.04
        repeat


# ------------------------------------------------------------
# Ruptures audio horrifiques
# ------------------------------------------------------------
init python:
    def horror_audio_cut(duration=0.38, restore_volume=1.0):
        """Coupe brutalement la musique, ponctue le vide, puis la ramène."""
        renpy.music.set_volume(0.0, delay=0.05, channel="music")
        renpy.play("audio/sfx_audio_drop.wav", channel="sound")
        renpy.pause(max(0.05, float(duration)), hard=True)
        renpy.music.set_volume(float(restore_volume), delay=0.60, channel="music")

    def horror_music_slow(track="audio/music/bgm_cold_metadata_slow.mp3",
                          fadeout=0.45, fadein=0.80):
        """Bascule vers une variante réellement ralentie et assombrie."""
        renpy.music.play(
            track,
            channel="music",
            loop=True,
            fadeout=max(0.0, float(fadeout)),
            fadein=max(0.0, float(fadein)),
        )
