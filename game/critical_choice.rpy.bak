# ============================================================
# critical_choice.rpy — HUD des CHOIX CRITIQUES
# Réservé aux décisions majeures (PAS les petits choix).
# Supporte 2 à 4 options, layout adaptatif, Noam glitché.
#
# Usage dans le scénario :
#   menu (screen="critical_choice", noam_expr="hesitation"):
#       "Titre affiché en haut"
#       "Option A":
#           ...
#       "Option B":
#           ...
#
#   - Le "titre" = la ligne de menu sans bloc (caption).
#   - noam_expr : expression du layered image noam (def. "reflexion").
#   - Fonctionne avec 2, 3 ou 4 options (max 4).
# ============================================================

define CC_DIR = "images/hud/critical_choice"

# ------------------------------------------------------------
# Positions des panneaux selon le nombre d'options
# (xpos, ypos) en fraction d'écran, ancrage centre (0.5,0.5)
# ------------------------------------------------------------
init python:
    CC_LAYOUT = {
        1: [(0.500, 0.640)],
        2: [(0.250, 0.580), (0.750, 0.580)],
        3: [(0.238, 0.500), (0.762, 0.500), (0.500, 0.820)],
        4: [(0.238, 0.450), (0.762, 0.450), (0.238, 0.740), (0.762, 0.740)],
    }

    def cc_positions(n):
        return CC_LAYOUT.get(n, CC_LAYOUT[2])

# ------------------------------------------------------------
# Noam glitché (aberration chromatique + jitter)
# ------------------------------------------------------------
transform cc_noam_base:
    subpixel True
    zoom 1.22 xalign 0.5 yanchor 1.0 ypos 1.05
    block:
        pause 1.1
        ease 0.02 xoffset -3
        ease 0.02 xoffset 4
        ease 0.02 xoffset 0
        pause 0.6
        ease 0.02 xoffset 2
        ease 0.02 xoffset -1
        ease 0.02 xoffset 0
        pause 0.5
        repeat

transform cc_noam_ghost(dx, tint):
    subpixel True
    zoom 1.22 xalign 0.5 yanchor 1.0 ypos 1.05
    matrixcolor TintMatrix(tint)
    additive 1.0
    alpha 0.30
    xoffset dx
    block:
        pause 1.1
        ease 0.03 xoffset dx * 3
        ease 0.05 xoffset dx
        pause 0.6
        ease 0.03 xoffset dx * 2
        ease 0.05 xoffset dx
        pause 0.5
        repeat

# léger scan/flicker sur l'ensemble du personnage
transform cc_noam_flicker:
    block:
        alpha 1.0
        pause 2.3
        linear 0.03 alpha 0.82
        linear 0.03 alpha 1.0
        pause 1.7
        linear 0.02 alpha 0.9
        linear 0.02 alpha 1.0
        repeat

# ------------------------------------------------------------
# Entrées animées
# ------------------------------------------------------------
transform cc_panel_in(delay=0.0):
    alpha 0.0 zoom 0.86
    pause delay
    parallel:
        easein 0.28 alpha 1.0
    parallel:
        easeout 0.34 zoom 1.0

transform cc_title_in:
    alpha 0.0 yoffset -22
    parallel:
        easein 0.4 alpha 1.0
    parallel:
        easeout 0.45 yoffset 0

transform cc_title_glitch:
    block:
        xoffset 0
        pause 1.4
        linear 0.02 xoffset -4
        linear 0.02 xoffset 5
        linear 0.02 xoffset 0
        pause 0.9
        linear 0.02 xoffset 3
        linear 0.02 xoffset 0
        repeat

transform cc_bar_pulse:
    block:
        alpha 0.75
        linear 0.9 alpha 1.0
        linear 0.9 alpha 0.75
        repeat

# ------------------------------------------------------------
# ÉCRAN
# ------------------------------------------------------------
screen critical_choice(items, noam_expr="reflexion"):
    style_prefix "cc"
    modal True
    zorder 210

    python:
        _cc_choices = [i for i in items if i.action]
        _cc_caps = [i.caption for i in items if not i.action]
        _cc_title = _cc_caps[0] if _cc_caps else ""
        _cc_n = len(_cc_choices)
        _cc_pos = cc_positions(_cc_n)

    # Fond assombri
    add Solid("#03070de6")

    # Noam glitché (centre)
    fixed:
        xsize 1920 ysize 1080
        at cc_noam_flicker
        add ("noam " + noam_expr) at cc_noam_ghost(-7, "#ff2d6b")
        add ("noam " + noam_expr) at cc_noam_ghost(7, "#33e0ff")
        add ("noam " + noam_expr) at cc_noam_base

    # Overlays glitch
    add CC_DIR + "/scanlines.png"
    add CC_DIR + "/vignette.png"

    # Réticule sur le visage
    add CC_DIR + "/reticle.png" xpos 0.5 ypos 0.30 anchor (0.5, 0.5) at Transform(alpha=0.9)

    # Titre glitché
    if _cc_title:
        fixed:
            xsize 1920 ysize 200
            ypos 0.045
            at cc_title_in
            fixed:
                at cc_title_glitch
                text _cc_title style "cc_title_ghost_m" xalign 0.5 ypos 0 offset (-4, 2) at Transform(alpha=0.55)
                text _cc_title style "cc_title_ghost_c" xalign 0.5 ypos 0 offset (4, -2) at Transform(alpha=0.55)
                text _cc_title style "cc_title" xalign 0.5 ypos 0

    # Options
    for idx, i in enumerate(_cc_choices):
        $ px, py = _cc_pos[idx] if idx < len(_cc_pos) else (0.5, 0.5 + idx * 0.12)
        button:
            action i.action
            xpos px ypos py
            anchor (0.5, 0.5)
            xysize (560, 128)
            background CC_DIR + "/panel_idle.png"
            hover_background CC_DIR + "/panel_hover.png"
            selected_background CC_DIR + "/panel_hover.png"
            at cc_panel_in(0.15 + idx * 0.08)
            text i.caption style "cc_option_text" align (0.5, 0.5)

    # Barre de confirmation
    frame:
        style "cc_confirm_bar"
        xalign 0.5 yalign 0.965
        at cc_bar_pulse
        hbox:
            spacing 14
            align (0.5, 0.5)
            frame:
                style "cc_key_badge"
                text "A" style "cc_key_text"
            text _("Confirmer") style "cc_confirm_text"

# ------------------------------------------------------------
# STYLES
# ------------------------------------------------------------
style cc_title is default
style cc_title_ghost_m is cc_title
style cc_title_ghost_c is cc_title
style cc_option_text is default
style cc_confirm_bar is frame
style cc_confirm_text is default
style cc_key_badge is frame
style cc_key_text is default

style cc_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 82
    color "#ffffff"
    outlines [(2, "#0a1a2acc", 0, 0)]
    kerning 2.0

style cc_title_ghost_m:
    color "#ff2d6b"
    outlines []

style cc_title_ghost_c:
    color "#33e0ff"
    outlines []

style cc_option_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 40
    color "#d6f2ff"
    hover_color "#06131f"
    selected_color "#06131f"
    kerning 1.0
    text_align 0.5
    xmaximum 470
    outlines []

style cc_confirm_bar:
    background Fixed(
        Solid("#040b14e0"),
        Solid("#5cd3ff40", ysize=2),
        Solid("#5cd3ff40", ysize=2, yalign=1.0),
    )
    xsize 460
    padding (26, 12, 26, 12)

style cc_confirm_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 30
    color "#bfe9ff"
    kerning 3.0

style cc_key_badge:
    background Solid("#5cd3ff")
    xsize 38 ysize 38
    padding (0, 0, 0, 0)

style cc_key_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 26
    color "#04121e"
    xalign 0.5
    yalign 0.5
