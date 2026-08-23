# ============================================================
# version_2_1_trailer_kit.rpy
# Boîte à outils cinéma de la bande-annonce 2.1.
#
# Contient uniquement des transforms, styles et screens : aucune
# logique de jeu, aucune écriture dans les sauvegardes.
# Le montage lui-même vit dans version_2_1_trailer.rpy.
#
# Sommaire :
#   1.  Canaux audio dédiés
#   2.  Transitions
#   3.  Transforms caméra (push / pull / pan / snap)
#   4.  Transforms de titrage cinétique
#   5.  Transforms de glitch (dédoublement chromatique)
#   6.  Styles typographiques
#   7.  Chrome permanent : letterbox, grain, contrôles
#   8.  Cartons de titre animés
#   9.  Bandeau de citation (lower third)
#  10.  Vitrines de mini-jeux
#  11.  Carton final / logo
#
# Note de montage : le chapitre n'est jamais découpé en « jours » à
# l'écran. Le trailer se lit comme un seul mouvement continu.
# ============================================================


# ------------------------------------------------------------
# 1. CANAUX AUDIO DÉDIÉS
# Trois canaux pour empiler les SFX sans se couper mutuellement.
# ------------------------------------------------------------
default persistent.trl_skip_splash = False

init -8 python:
    import math as _trl_math

    for _trl_chan, _trl_loop in (("trl_a", False), ("trl_b", False), ("trl_amb", True)):
        try:
            renpy.music.register_channel(_trl_chan, mixer="sfx", loop=_trl_loop)
        except Exception:
            pass

    def trl_arc_points(count=24, cx=960, cy=690, spread=210, rise=430, bend=2.4):
        """Points d'une courbe de tracé, réutilisés par la vitrine Synchro."""
        pts = []
        for _i in range(count):
            _t = _i / float(max(1, count - 1))
            pts.append((
                int(cx + spread * _trl_math.sin(_t * bend)),
                int(cy - rise * _t),
            ))
        return pts

    def trl_localize(value):
        """Traduit avant toute concaténation, découpe ou animation du texte."""
        if value is None:
            return None
        return renpy.translate_string(value)

    TRL_TRACE_PATH = trl_arc_points()

    TRL_OBJ_LANES = [366, 458, 550, 642, 734]

    def trl_refresh_localized_data():
        """Reconstruit les textes Python après chaque changement de langue."""
        global TRL_FA_TILES, TRL_OBJ_SHARDS, TRL_AMEND_NOTES

        # Données des vitrines. Déclarées ici plutôt que dans les screens :
        # le langage de screen n'accepte que des `$` d'une seule ligne.
        TRL_FA_TILES = [
            (trl_localize(_("AUTORISER")),     340, 720, 0.00, 0, -132),
            (trl_localize(_("LES")),           640, 720, 0.16, 0, -132),
            (trl_localize(_("DÉPLACEMENTS")),  790, 720, 0.32, 0, -132),
            (trl_localize(_("ENTRE")),        1160, 720, 0.48, 0, -132),
            (trl_localize(_("DISTRICTS")),    1330, 720, 0.64, 0, -132),
        ]

        TRL_OBJ_SHARDS = [
            (trl_localize(_("FRONTIÈRES")), 0.00, 382, "#FF6877"),
            (trl_localize(_("CADAVRES")),   0.42, 468, "#D9E1E8"),
            (trl_localize(_("TU")),         0.78, 556, "#55A9FF"),
            (trl_localize(_("N'Y ÉTAIS")),  1.06, 640, "#FF6877"),
            (trl_localize(_("PAS")),        1.44, 722, "#55A9FF"),
        ]

        # (texte, x, y, délai, décalage X d'entrée, décalage Y d'entrée, rotation)
        TRL_AMEND_NOTES = [
            (trl_localize(_("TOUT CITOYEN")),         596, 372, 0.15, -160,  -90, -2),
            (trl_localize(_("PEUT CIRCULER")),        900, 366, 0.45,  180, -110,  2),
            (trl_localize(_("ENTRE LES DISTRICTS")),  596, 452, 0.80, -140,  120, -1),
            (trl_localize(_("SANS AUTORISATION")),   1010, 448, 1.15,  200,  130,  3),
        ]

    trl_refresh_localized_data()


# ------------------------------------------------------------
# 2. TRANSITIONS
# ------------------------------------------------------------
define trl_cut       = Fade(0.0, 0.06, 0.14, color="#000000")
define trl_hardcut   = Dissolve(0.001)
define trl_flash     = Fade(0.05, 0.0, 0.26, color="#CFF6FF")
define trl_flash_red = Fade(0.05, 0.0, 0.30, color="#D01A2E")
define trl_slowfade  = Dissolve(0.9)
define trl_soft      = Dissolve(0.45)
define trl_blink     = Fade(0.10, 0.05, 0.10, color="#000000")


# ------------------------------------------------------------
# 3. TRANSFORMS CAMÉRA
# Tous partent de `fit "cover"` pour remplir le cadre 16/9 quelle
# que soit la résolution native de la CG.
# ------------------------------------------------------------
transform trl_push(t=6.0, z0=1.00, z1=1.09, x0=0.5, x1=0.5, y0=0.5, y1=0.5):
    fit "cover"
    xalign x0
    yalign y0
    zoom z0
    linear t zoom z1 xalign x1 yalign y1

transform trl_pull(t=6.0, z0=1.12, z1=1.00, x0=0.5, x1=0.5):
    fit "cover"
    xalign x0
    yalign 0.5
    zoom z0
    linear t zoom z1 xalign x1

transform trl_pan(t=6.0, x0=0.32, x1=0.68, z=1.10):
    fit "cover"
    yalign 0.5
    zoom z
    xalign x0
    linear t xalign x1

# Entrée sèche : utilisée dans les rafales de montage.
transform trl_snap(z0=1.22, z1=1.04, t=0.9):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom z0
    alpha 0.0
    easeout 0.10 alpha 1.0
    easeout t zoom z1

# Plan de mémoire : arrivée latérale rapide.
transform trl_memory(side=-1, t=0.34):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom 1.06
    alpha 0.0
    xoffset (90 * side)
    easeout t alpha 1.0 xoffset 0

# Respiration douce pour les plans tenus longtemps.
transform trl_breathe(t=7.0, z0=1.03, z1=1.06):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom z0
    block:
        linear t zoom z1
        linear t zoom z0
        repeat

# Tremblement continu (climax).
transform trl_unstable(amp=5, z=1.08):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom z
    block:
        linear 0.05 xoffset amp yoffset -amp
        linear 0.05 xoffset -amp yoffset amp
        linear 0.05 xoffset (amp // 2) yoffset (amp // 2)
        linear 0.05 xoffset 0 yoffset 0
        repeat


# ------------------------------------------------------------
# 4. TITRAGE CINÉTIQUE
# Chaque mot arrive avec un décalage : lecture rythmée, pas un
# simple fondu de bloc.
# ------------------------------------------------------------
transform trl_word_in(d=0.0, rise=30):
    alpha 0.0
    yoffset rise
    pause d
    easeout 0.40 alpha 1.0 yoffset 0

transform trl_word_slam(d=0.0):
    alpha 0.0
    zoom 1.9
    pause d
    easein 0.13 alpha 1.0 zoom 1.0
    easeout 0.06 zoom 1.05
    easein 0.06 zoom 1.0

transform trl_word_jitter(d=0.0):
    alpha 0.0
    zoom 1.7
    pause d
    easein 0.11 alpha 1.0 zoom 1.0
    block:
        linear 0.04 xoffset 4
        linear 0.04 xoffset -3
        linear 0.04 xoffset 0
        pause 0.5
        repeat

transform trl_rule_grow(d=0.25, w=1.0):
    xzoom 0.0
    alpha 0.0
    pause d
    easeout 0.50 xzoom w alpha 1.0

transform trl_kicker_in(d=0.0):
    alpha 0.0
    xoffset -22
    pause d
    easeout 0.45 alpha 1.0 xoffset 0

# Balayage lumineux derrière les grands titres.
transform trl_sweep(d=0.4, t=1.1):
    xpos -400
    alpha 0.0
    pause d
    linear 0.12 alpha 0.55
    linear t xpos 2100
    linear 0.12 alpha 0.0

transform trl_fade_in(d=0.0, t=0.6):
    alpha 0.0
    pause d
    linear t alpha 1.0

transform trl_pulse(lo=0.30, hi=0.95, t=0.5):
    alpha lo
    block:
        linear t alpha hi
        linear t alpha lo
        repeat

transform trl_slow_rotate(t=26.0):
    rotate 0
    block:
        linear t rotate 360
        repeat

transform trl_counter_rotate(t=34.0):
    rotate 360
    block:
        linear t rotate 0
        repeat


# ------------------------------------------------------------
# 5. GLITCH — dédoublement chromatique
# ------------------------------------------------------------
transform trl_rgb_left(amp=12, spd=0.07):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom 1.06
    block:
        linear spd xoffset -amp
        linear spd xoffset (-amp // 3)
        linear spd xoffset -amp
        repeat

transform trl_rgb_right(amp=12, spd=0.06):
    fit "cover"
    xalign 0.5
    yalign 0.5
    zoom 1.06
    block:
        linear spd xoffset amp
        linear spd xoffset (amp // 3)
        linear spd xoffset amp
        repeat

transform trl_tear(h=26, t=0.11):
    alpha 0.0
    block:
        pause 0.6
        alpha 0.85
        pause t
        alpha 0.0
        pause 0.25
        alpha 0.6
        pause 0.06
        alpha 0.0
        repeat

transform trl_scan_drift(t=5.0):
    yoffset -1080
    block:
        linear t yoffset 1080
        repeat

transform trl_noise_flicker:
    alpha 0.05
    block:
        linear 0.09 alpha 0.16
        linear 0.07 alpha 0.04
        linear 0.11 alpha 0.13
        repeat


# ------------------------------------------------------------
# 6. STYLES
# ------------------------------------------------------------
style trl_h1:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 92
    color "#F4F9FC"
    outlines [(3, "#02060C", 0, 0)]
    kerning 3.0

style trl_h2 is trl_h1:
    size 60
    color "#DCEAF3"
    kerning 4.0

style trl_kicker:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 24
    color "#5CD3FF"
    kerning 8.0
    outlines [(2, "#02060C", 0, 0)]

style trl_quote:
    font "fonts/Barlow-Light.ttf"
    size 38
    color "#EEF5FA"
    line_spacing 8
    outlines [(3, "#02060C", 0, 1)]

style trl_speaker:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#66D7FF"
    kerning 6.0
    outlines [(2, "#02060C", 0, 0)]

style trl_micro:
    font "fonts/Barlow-Light.ttf"
    size 17
    color "#6E9FB6"
    kerning 3.0

style trl_hud:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 21
    color "#7DF9FF"
    kerning 3.0
    outlines [(2, "#02060C", 0, 0)]

style trl_hud_big is trl_hud:
    size 44
    color "#E4F2FA"
    kerning 2.0

style trl_skip_button is button:
    background Solid("#03081088")
    hover_background Solid("#12384CDD")
    padding (20, 10, 20, 10)

style trl_skip_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 19
    color "#6FA5BE"
    hover_color "#E4F7FF"
    kerning 3.0


# ------------------------------------------------------------
# 7. CHROME PERMANENT
# ------------------------------------------------------------
screen trl_controls():
    zorder 990

    key "K_ESCAPE" action Jump("version_2_1_trailer_end")
    key "mouseup_3" action Jump("version_2_1_trailer_end")
    key "K_SPACE"  action NullAction()

    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856
        ypos 26
        xanchor 1.0
        action Jump("version_2_1_trailer_end")


# Bandes cinéma fixes : présentes du premier au dernier plan.
screen trl_letterbox(h=88):
    zorder 940
    add Solid("#000000") xpos 0 ypos 0 xsize 1920 ysize h
    add Solid("#000000") xpos 0 ypos (1080 - h) xsize 1920 ysize h


# Traitement image. `heat` monte de 0.0 (acte 1) à 1.0 (climax) :
# le grain, les scanlines et la teinte rouge s'intensifient avec lui.
screen trl_grade(heat=0.0):
    zorder 930

    add "gui/main_menu_kami/vignette.png":
        alpha (0.55 + 0.30 * heat)
    add "gui/main_menu_kami/scanlines.png":
        alpha (0.07 + 0.12 * heat)
    add "gui/main_menu_kami/scanlines.png" at trl_scan_drift(6.5 - 3.5 * heat):
        alpha (0.05 + 0.10 * heat)

    if heat > 0.45:
        add Solid("#FFFFFF") at trl_noise_flicker:
            xsize 1920
            ysize 3
            ypos 486
        add Solid("#D8203A"):
            xsize 1920
            ysize 1080
            alpha (0.05 * (heat - 0.45) / 0.55)

    if heat > 0.7:
        add Solid("#9AF4FF") at trl_tear(t=0.09):
            xsize 1920
            ysize 22
            ypos 318
        add Solid("#FF3A5C") at trl_tear(t=0.07):
            xsize 1920
            ysize 14
            ypos 742


# Dégradé bas de cadre : garantit la lisibilité des citations.
screen trl_scrim(height=380, top=0.0, bottom=0.88):
    $ trl_steps = 20
    $ trl_band = height // trl_steps
    for trl_i in range(trl_steps):
        add Solid("#01050B"):
            xsize 1920
            ysize (trl_band + 1)
            ypos (1080 - height + trl_i * trl_band)
            alpha (top + (bottom - top) * (trl_i / float(trl_steps - 1)))


# ------------------------------------------------------------
# 8. CARTONS DE TITRE ANIMÉS
# Les mots de `line1` arrivent en cascade, la règle horizontale
# se déploie, puis `line2` conclut.
# ------------------------------------------------------------
screen trl_title(line1, line2=None, kicker=None, accent="#5CD3FF", slam=False, danger=False, bg=None, bg_alpha=0.22):
    zorder 400

    $ line1 = trl_localize(line1)
    $ line2 = trl_localize(line2)
    $ kicker = trl_localize(kicker)

    add Solid("#01040A")

    if bg:
        add bg at trl_push(9.0, 1.04, 1.14):
            alpha bg_alpha
    else:
        add "gui/main_menu_kami/bg_orbit.png" at trl_push(11.0, 1.02, 1.10):
            alpha 0.16

    add "gui/main_menu_kami/scanlines.png" alpha 0.10
    add "gui/main_menu_kami/vignette.png" alpha 0.70

    $ trl_w1 = line1.split(" ")
    $ trl_w2 = line2.split(" ") if line2 else []
    $ trl_base = 0.10 if kicker is None else 0.34

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 26

        if kicker:
            hbox:
                xalign 0.5
                spacing 16
                add Solid(accent, xsize=54, ysize=2) yalign 0.5 at trl_rule_grow(0.05)
                text kicker at trl_kicker_in(0.10):
                    style "trl_kicker"
                    color accent
                add Solid(accent, xsize=54, ysize=2) yalign 0.5 at trl_rule_grow(0.05)

        hbox:
            xalign 0.5
            spacing 26
            for trl_i, trl_word in enumerate(trl_w1):
                if slam:
                    text trl_word at trl_word_slam(trl_base + 0.11 * trl_i):
                        style "trl_h1"
                        color ("#FFECEC" if danger else "#F4F9FC")
                elif danger:
                    text trl_word at trl_word_jitter(trl_base + 0.09 * trl_i):
                        style "trl_h1"
                        color "#FFECEC"
                else:
                    text trl_word at trl_word_in(trl_base + 0.09 * trl_i):
                        style "trl_h1"

        if trl_w2:
            add Solid(accent, xsize=420, ysize=2):
                xalign 0.5
                at trl_rule_grow(trl_base + 0.10 * len(trl_w1))
            hbox:
                xalign 0.5
                spacing 20
                for trl_j, trl_word2 in enumerate(trl_w2):
                    text trl_word2 at trl_word_in(trl_base + 0.16 + 0.10 * (len(trl_w1) + trl_j), 18):
                        style "trl_h2"
                        color ("#FFC9CE" if danger else "#BFE6F7")

    # Balayage lumineux : la petite touche qui « vend » le carton.
    add Solid("#FFFFFF") at trl_sweep(trl_base + 0.30, 1.05):
        xsize 260
        ysize 1080
        alpha 0.0


# Slam plein écran d'un mot unique (staccato de l'acte 4).
screen trl_shout(word, accent="#FF3A5C", psize=210):
    zorder 620

    $ word = trl_localize(word)

    add Solid("#00000099") at trl_fade_in(0.0, 0.06)
    add "images/background/debat/fatal_assembly_1.png" at trl_snap(1.30, 1.05, 0.7):
        alpha 0.35

    text word at trl_word_slam(0.0):
        xalign 0.5
        yalign 0.46
        size psize
        font "fonts/Rajdhani-SemiBold.ttf"
        color accent
        kerning 8
        outlines [(9, "#04060C", 0, 0), (3, "#FFFFFF", 0, 0)]


# ------------------------------------------------------------
# 9. BANDEAU DE CITATION (lower third)
# ------------------------------------------------------------
screen trl_quote(text_line, speaker, accent="#5CD3FF", tag=None):
    zorder 320

    $ text_line = trl_localize(text_line)
    $ speaker = trl_localize(speaker)
    $ tag = trl_localize(tag)

    use trl_scrim(400, 0.0, 0.90)

    vbox:
        xpos 156
        ypos 748
        xsize 1180
        spacing 14

        hbox:
            spacing 14
            add Solid(accent, xsize=3, ysize=22) yalign 0.5 at trl_rule_grow(0.05, 1.0)
            text speaker at trl_kicker_in(0.10):
                style "trl_speaker"
                color accent
            if tag:
                text tag at trl_kicker_in(0.20):
                    style "trl_micro"
                    yoffset 3

        text ("« " + text_line + " »") at trl_word_in(0.16, 16):
            style "trl_quote"
            xmaximum 1180


# ------------------------------------------------------------
# 11. VITRINES DE MINI-JEUX
# Reproductions animées, non interactives, du chrome réel de
# chaque mini-jeu. Aucune ne renvoie de valeur : elles sont
# affichées avec `show screen` et retirées avec `hide screen`.
# ------------------------------------------------------------

# Cadre commun.
screen trl_mg_chrome(title, subtitle, accent="#7DF9FF"):
    zorder 260

    $ title = trl_localize(title)
    $ subtitle = trl_localize(subtitle)

    add Solid("#01050B")
    add "gui/main_menu_kami/bg_orbit.png" at trl_push(14.0, 1.05, 1.12):
        alpha 0.10

    transclude

    add Solid("#01050B") xsize 1920 ysize 96 ypos 88 alpha 0.72

    hbox:
        xpos 156
        ypos 112
        spacing 18
        add Solid(accent, xsize=4, ysize=52) at trl_rule_grow(0.0, 1.0)
        vbox:
            spacing 3
            text _("APERÇU MINI-JEU") at trl_kicker_in(0.05):
                style "trl_kicker"
                size 18
                color accent
            text title at trl_kicker_in(0.12):
                style "trl_hud_big"
                size 40

    text subtitle at trl_kicker_in(0.22):
        style "trl_micro"
        xpos 1764
        ypos 132
        xanchor 1.0
        text_align 1.0


# --- 11.a  SYNCHRONISATION MOTRICE (trace_qte) ---------------
transform trl_trace_cursor:
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 690
    alpha 0.0
    block:
        easein 0.30 alpha 1.0
        easeout 0.20 zoom 0.80
        pause 0.45
        easeout 0.42 xpos 1078 ypos 582
        easeout 0.42 xpos 1155 ypos 475
        easeout 0.42 xpos 1164 ypos 367
        easeout 0.42 xpos 1102 ypos 260
        easein 0.14 zoom 1.0
        pause 0.35
        linear 0.25 alpha 0.0
        pause 0.30
        repeat

transform trl_trace_ring:
    zoom 1.0
    alpha 0.85
    block:
        ease 0.55 zoom 1.16 alpha 1.0
        ease 0.55 zoom 1.00 alpha 0.85
        repeat

transform trl_trace_gauge:
    xzoom 1.0
    block:
        linear 3.4 xzoom 0.16
        linear 0.01 xzoom 1.0
        repeat

transform trl_trace_label:
    alpha 0.0
    block:
        pause 0.5
        linear 0.18 alpha 1.0
        pause 0.9
        linear 0.18 alpha 0.0
        pause 1.6
        repeat

screen trl_mg_trace():
    use trl_mg_chrome(_("SYNCHRONISATION MOTRICE"), _("RÉVEIL SOUS CONTRÔLE")):

        add "images/background/scene/chambre1.png" at trl_push(9.0, 1.06, 1.14):
            alpha 0.34
        add Solid("#020711") alpha 0.45

        # Le tracé à suivre : halo large + point net, pour que la
        # courbe se lise immédiatement à l'écran.
        for trl_p in TRL_TRACE_PATH:
            add Solid("#7DF9FF"):
                xsize 20
                ysize 20
                xpos (trl_p[0] - 6)
                ypos (trl_p[1] - 6)
                alpha 0.16
            add Solid("#BFF6FF"):
                xsize 9
                ysize 9
                xpos trl_p[0]
                ypos trl_p[1]
                alpha 0.90

        add "images/hud/glow.png":
            xysize (300, 300)
            xpos 810
            ypos 540
            alpha 0.30
        add "images/hud/ring_dashed.png" at trl_trace_ring:
            xysize (190, 190)
            xpos 865
            ypos 595
            alpha 1.0
        add "images/hud/ring_thin.png" at trl_slow_rotate(9.0):
            xysize (150, 150)
            xpos 885
            ypos 615
            alpha 0.75

        # Cible d'arrivée.
        add "images/hud/scan_arc.png" at trl_counter_rotate(7.0):
            xysize (170, 170)
            xpos 1017
            ypos 175
            alpha 0.85
        add "images/hud/core_dot.png" at trl_pulse(0.35, 0.95, 0.6):
            xysize (22, 22)
            xpos 1091
            ypos 249

        # Curseur du joueur.
        add Transform("images/hud/core_dot.png", xysize=(34, 34)) at trl_trace_cursor

        text _("MAINTENIR  ▸  GLISSER") at trl_trace_label:
            xalign 0.5
            ypos 852
            style "trl_hud"
            size 30

        # Jauge de temps.
        add Solid("#0A1626") xpos 660 ypos 800 xsize 600 ysize 18
        add Solid("#7DF9FF") at trl_trace_gauge:
            xpos 660
            ypos 800
            xsize 600
            ysize 18

        text _("PRÉCISION  98 / 100"):
            style "trl_hud"
            xpos 1764
            ypos 806
            xanchor 1.0


# --- 11.b  RÉDACTION D'AMENDEMENT ----------------------------
# Contrepoint chaud et manuscrit au milieu du HUD cyan : c'est la
# mécanique signature du chapitre (« un seul amendement chacun »).
transform trl_amend_note(d=0.0, dx=0, dy=0, rot=0):
    alpha 0.0
    xoffset dx
    yoffset dy
    rotate (rot - 6)
    zoom 1.12
    pause d
    easeout 0.34 alpha 1.0 xoffset 0 yoffset 0 rotate rot zoom 1.0

transform trl_amend_pen:
    alpha 0.0
    xpos 1180
    ypos 606
    pause 2.1
    linear 0.20 alpha 1.0
    linear 0.55 xpos 1330 ypos 600
    linear 0.30 alpha 0.0

screen trl_mg_amendement():
    use trl_mg_chrome(_("RÉDACTION D'AMENDEMENT"), _("UNE SEULE PROPOSITION"), "#E0C48A"):

        add "minijeu/amend_assets/amend_desk.png" at trl_push(9.0, 1.03, 1.09)
        add Solid("#050308") alpha 0.22

        add "minijeu/amend_assets/amend_sheet.png":
            xpos 500
            ypos 196
            zoom 0.78

        # day_font n'a pas le point médian : on reste sur des tirets.
        text _("AMENDEMENT - COMMANDEMENT VI - MOUVEMENT"):
            font "fonts/day_font.ttf"
            size 27
            color "#2A2436"
            xpos 590
            ypos 296

        # Fragments manuscrits qui viennent se verrouiller sur la ligne.
        for trl_n in TRL_AMEND_NOTES:
            frame at trl_amend_note(trl_n[3], trl_n[4], trl_n[5], trl_n[6]):
                xpos trl_n[1]
                ypos trl_n[2]
                background Frame("minijeu/amend_assets/amend_note_locked.png", 30, 20)
                padding (18, 10)
                text trl_n[0]:
                    font "fonts/day_font.ttf"
                    size 30
                    color "#20202E"

        add "minijeu/amend_assets/amend_strike.png" at trl_fade_in(1.55, 0.35):
            xpos 640
            ypos 520
            zoom 0.70
            alpha 0.75

        add "images/hud/core_dot.png" at trl_amend_pen:
            xysize (16, 16)

        # Rappel de la règle, en HUD froid : le contraste fait tout.
        frame:
            xpos 1462
            ypos 250
            xsize 302
            ysize 214
            background Solid("#06111DE8")
            padding (22, 18)
            vbox:
                spacing 10
                text _("CONTRAINTE") style "trl_hud" size 22 color "#E0C48A"
                text _("Un amendement.\nUn seul.\nPersonne ne saura\nqui l'a écrit."):
                    style "trl_quote"
                    size 23
                    xmaximum 258


# --- 11.c  FATAL ASSEMBLY (débat / phase 1) ------------------
transform trl_fa_tile(d=0.0, tx=0, ty=0):
    alpha 0.0
    zoom 1.15
    pause d
    easeout 0.30 alpha 1.0 zoom 1.0
    pause 0.55
    easeout 0.45 xoffset tx yoffset ty
    pause 1.6
    alpha 0.0
    xoffset 0
    yoffset 0
    pause 0.2
    repeat

screen trl_mg_fatal():
    use trl_mg_chrome(_("FATAL ASSEMBLY"), _("RECONSTITUER LE TEXTE OFFICIEL")):

        add "images/background/scene/conclave2.png" at trl_push(9.0, 1.05, 1.13):
            alpha 0.30

        # Panneau Kami : l'IA commente le débat.
        frame:
            xpos 156
            ypos 236
            xsize 720
            ysize 190
            background Solid("#071421EE")
            padding (18, 18)
            hbox:
                spacing 20
                frame:
                    xsize 152
                    ysize 152
                    background Solid("#0D253BEE")
                    padding (0, 0)
                    add "images/character/kami/analyse.png":
                        xysize (152, 152)
                        alpha 0.95
                vbox:
                    spacing 8
                    text "KAMI" style "trl_hud" size 24 color "#5FD5FF"
                    text _("Remettez les mots dans le bon ordre."):
                        style "trl_quote"
                        size 27
                        xmaximum 480
                    text _("Montrez-moi que vous comprenez ce que vous votez."):
                        style "trl_micro"
                        size 20
                        xmaximum 480

        # Ligne de reconstitution.
        add Solid("#0A1B2AEE") xpos 300 ypos 560 xsize 1320 ysize 118
        add Solid("#3EBEFF66") xpos 300 ypos 560 xsize 1320 ysize 2
        add Solid("#3EBEFF33") xpos 300 ypos 676 xsize 1320 ysize 2

        # Tuiles de mots qui viennent se ranger.
        for trl_t in TRL_FA_TILES:
            frame at trl_fa_tile(trl_t[3], trl_t[4], trl_t[5]):
                xpos trl_t[1]
                ypos trl_t[2]
                background Solid("#123049EE")
                padding (20, 12)
                text trl_t[0]:
                    style "trl_hud"
                    size 30
                    color "#EAF6FF"

        frame:
            xpos 1360
            ypos 236
            xsize 404
            ysize 190
            background Solid("#071421EE")
            padding (22, 18)
            vbox:
                spacing 10
                text _("PRESSION") style "trl_hud" size 22 color "#FFD166"
                add Solid("#231B0F") xsize 356 ysize 20
                add Solid("#FFD166") at trl_pulse(0.6, 1.0, 0.8):
                    xsize 250
                    ysize 20
                    yoffset -20
                text _("Le Conclave vous regarde.") style "trl_micro" size 19


# --- 11.d  OBJECTION FRACTURÉE -------------------------------
transform trl_obj_word(d=0.0, y=420, dur=1.55):
    alpha 0.0
    xpos 1420
    ypos y
    pause d
    block:
        alpha 0.0
        xpos 1420
        linear 0.10 alpha 1.0
        linear dur xpos 470
        linear 0.12 alpha 0.0
        pause 0.45
        repeat

transform trl_obj_shield:
    alpha 0.25
    block:
        pause 0.9
        linear 0.06 alpha 1.0
        pause 0.22
        linear 0.20 alpha 0.25
        pause 0.9
        repeat

transform trl_obj_idle(amp=8, t=1.5):
    yoffset 0
    block:
        linear t yoffset (-amp)
        linear t yoffset 0
        repeat

screen trl_mg_objection():
    use trl_mg_chrome(_("OBJECTION FRACTURÉE"), _("DUEL VERBAL"), "#FF6877"):

        add "gui/day4/objection/objection_bg.png" at trl_push(9.0, 1.04, 1.11):
            alpha 0.55
        add Solid("#020711C4")

        for trl_lane in TRL_OBJ_LANES:
            add Solid("#5CD3FF16") xpos 420 ypos trl_lane xsize 1080 ysize 2

        add Transform(character_image("noam", "determine"), zoom=0.82) at trl_obj_idle(9, 1.6):
            xpos -60
            yalign 1.0
        add Transform(character_image("ryn", "colere"), zoom=0.82) at trl_obj_idle(7, 1.9):
            xpos 1420
            yalign 1.0

        # Barres de vie.
        frame:
            xpos 156
            ypos 236
            xsize 420
            ysize 92
            background Solid("#071522EE")
            padding (22, 14)
            vbox:
                spacing 8
                text "NOAM" style "trl_hud" size 24 color "#DCEBFF"
                add Solid("#173246") xsize 356 ysize 14
                add Solid("#55B9FF") xsize 268 ysize 14 yoffset -14

        frame:
            xpos 1344
            ypos 236
            xsize 420
            ysize 92
            background Solid("#160D18EE")
            padding (22, 14)
            vbox:
                spacing 8
                text "RYN" style "trl_hud" size 24 color "#FFE4E8" xalign 1.0
                add Solid("#40202A") xsize 356 ysize 14
                add Solid("#FF6877") xsize 152 ysize 14 yoffset -14

        # Bouclier ESPACE.
        add Solid("#5CD3FF") at trl_obj_shield:
            xpos 420
            ypos 330
            xsize 44
            ysize 460
        text _("ESPACE"):
            style "trl_hud"
            xpos 476
            ypos 545

        # Projectiles : chaque mot de la phrase adverse.
        for trl_s in TRL_OBJ_SHARDS:
            text trl_s[0] at trl_obj_word(trl_s[1], trl_s[2]):
                style "trl_hud"
                size 34
                color trl_s[3]

        frame:
            xpos 330
            ypos 858
            xsize 1260
            ysize 96
            background Solid("#07111CE8")
            padding (28, 16)
            hbox:
                spacing 74
                vbox:
                    spacing 3
                    text _("GRIS") style "trl_hud" size 22 color "#D9E1E8"
                    text _("Ne rien faire") style "trl_micro" size 18
                vbox:
                    spacing 3
                    text _("ROUGE") style "trl_hud" size 22 color "#FF6877"
                    text _("Esquiver") style "trl_micro" size 18
                vbox:
                    spacing 3
                    text _("BLEU") style "trl_hud" size 22 color "#55A9FF"
                    text _("Renvoyer l'argument") style "trl_micro" size 18


# --- 11.e  VOTE À L'UNANIMITÉ --------------------------------
transform trl_vote_card(d=0.0):
    alpha 0.0
    yoffset 40
    pause d
    easeout 0.40 alpha 1.0 yoffset 0

transform trl_vote_timer:
    xzoom 1.0
    linear 5.0 xzoom 0.0

# Le verdict est un screen à part, montré au moment voulu par le
# montage : plus fiable qu'une longue pause ATL, et le SFX se cale
# exactement sur l'impact.
transform trl_stamp:
    alpha 0.0
    zoom 3.2
    easein 0.16 alpha 1.0 zoom 1.0
    easeout 0.08 zoom 1.08
    easein 0.08 zoom 1.0

screen trl_mg_vote():
    zorder 260

    add "images/background/scene/conclave3.png" at trl_push(9.0, 1.04, 1.12)
    add Solid("#020509D8")
    add "gui/main_menu_kami/scanlines.png" alpha 0.10

    frame:
        xalign 0.5
        ypos 176
        xsize 980
        ysize 96
        background Solid("#070A0EE8")
        padding (28, 16)
        vbox:
            spacing 10
            hbox:
                xalign 0.5
                spacing 70
                text _("VOTE EN COURS") style "trl_hud" size 32 color "#D7D2C8"
                text _("UNANIMITÉ REQUISE") style "trl_hud" size 32 color "#FFD166"
            fixed:
                xsize 900
                ysize 14
                add Solid("#161A20") xsize 900 ysize 14
                add Solid("#9CD7E6") at trl_vote_timer:
                    xsize 900
                    ysize 14

    hbox:
        xalign 0.5
        ypos 360
        spacing 40

        frame at trl_vote_card(0.05):
            xsize 440
            ysize 340
            background Solid("#162016DD")
            padding (0, 0)
            vbox:
                align (0.5, 0.5)
                spacing 18
                text "+" xalign 0.5 size 62 color "#A7BE83" font "fonts/Rajdhani-SemiBold.ttf"
                text _("VOTE POUR") xalign 0.5 style "trl_hud" size 40 color "#A7BE83"
                text _("Changer les règles") xalign 0.5 style "trl_micro" size 21

        frame at trl_vote_card(0.17):
            xsize 440
            ysize 340
            background Solid("#1A1A1ADD")
            padding (0, 0)
            vbox:
                align (0.5, 0.5)
                spacing 18
                text "=" xalign 0.5 size 62 color "#A9AAA6" font "fonts/Rajdhani-SemiBold.ttf"
                text _("ABSTENTION") xalign 0.5 style "trl_hud" size 40 color "#A9AAA6"
                text _("Laisser le système trancher") xalign 0.5 style "trl_micro" size 21

        frame at trl_vote_card(0.29):
            xsize 440
            ysize 340
            background Solid("#221211DD")
            padding (0, 0)
            vbox:
                align (0.5, 0.5)
                spacing 18
                text "−" xalign 0.5 size 62 color "#B96455" font "fonts/Rajdhani-SemiBold.ttf"
                text _("VOTE CONTRE") xalign 0.5 style "trl_hud" size 40 color "#B96455"
                text _("Maintenir le cadre") xalign 0.5 style "trl_micro" size 21

    text _("11 VOIX  ·  1 SUFFIT À TOUT BLOQUER") at trl_fade_in(0.6, 0.6):
        xalign 0.5
        ypos 760
        style "trl_kicker"
        size 26


# Verdict : tampon rouge qui s'abat sur l'écran de vote.
# Chaque élément est un displayable simple porteur de son propre ATL —
# un conteneur (vbox/hbox) muni d'un `at` ne se rend pas de façon
# fiable ici, contrairement à `text at ...` et `frame at ...`.
screen trl_mg_verdict():
    zorder 268

    add Solid("#25040A") alpha 0.45

    add Solid("#FF3A4E") at trl_rule_grow(0.10, 1.0):
        xalign 0.5
        ypos 688
        xsize 1500
        ysize 3

    text _("AMENDEMENT REJETÉ") at trl_stamp:
        xalign 0.5
        ypos 704
        size 86
        font "fonts/Rajdhani-SemiBold.ttf"
        color "#FF3A4E"
        kerning 6
        outlines [(7, "#0B0203", 0, 0)]

    text _("UNANIMITÉ NON ATTEINTE — LE MONDE NE CHANGERA PAS AUJOURD'HUI") at trl_word_in(0.34, 14):
        xalign 0.5
        ypos 826
        style "trl_kicker"
        size 26
        color "#FF7C88"

    add Solid("#FF3A4E") at trl_rule_grow(0.24, 1.0):
        xalign 0.5
        ypos 880
        xsize 1500
        ysize 3


# --- 11.f  SIGNAL INSTABLE -----------------------------------
transform trl_sig_cursor:
    xpos 700
    block:
        linear 1.05 xpos 1120
        linear 0.85 xpos 830
        linear 0.95 xpos 1180
        linear 0.75 xpos 960
        repeat

transform trl_sig_kami(amp=10):
    xalign 0.5
    yalign 0.42
    zoom 0.92
    block:
        linear 0.08 xoffset amp
        linear 0.06 xoffset (-amp)
        linear 0.10 xoffset 0
        pause 0.5
        repeat

screen trl_mg_signal():
    use trl_mg_chrome(_("SIGNAL INSTABLE"), _("COMPRENDRE KAMI"), "#48F5FF"):

        add Solid("#020711")

        # Dédoublement chromatique. Volontairement SANS `blur=` : sur
        # certains GPU la passe de flou masque les frères dessinés après.
        $ trl_kami_sig = "images/minigame/signal_instable/kami_transmission_glitch_v2.png"
        add Transform(trl_kami_sig, xysize=(1108, 624), matrixcolor=TintMatrix("#36DFFF")) at trl_sig_kami(22):
            alpha 0.34
        add Transform(trl_kami_sig, xysize=(1108, 624), matrixcolor=TintMatrix("#FF3C72")) at trl_sig_kami(-20):
            alpha 0.30
        add Transform(trl_kami_sig, xysize=(1100, 620)) at trl_sig_kami(9):
            alpha 0.92

        for trl_i in range(0, 1080, 6):
            add Solid("#BFEFFF09") xsize 1920 ysize 1 xpos 0 ypos trl_i

        # Jauge de concentration.
        add Solid("#08131FEE") xpos 460 ypos 800 xsize 1000 ysize 74
        add Solid("#12324A")   xpos 490 ypos 826 xsize 940 ysize 22
        add Solid("#48F5FF44") xpos 800 ypos 826 xsize 320 ysize 22
        add Solid("#48F5FF")   xpos 800 ypos 822 xsize 320 ysize 4
        add Solid("#FFFFFF") at trl_sig_cursor:
            ypos 814
            xsize 8
            ysize 46

        text _("ZONE DE CONCENTRATION"):
            style "trl_micro"
            xpos 800
            ypos 886

        frame:
            xpos 156
            ypos 250
            xsize 380
            ysize 250
            background Solid("#07111EE8")
            padding (26, 22)
            vbox:
                spacing 14
                text _("OBJECTIF") style "trl_hud" size 26 color "#42A5FF"
                text _("Restez lucide.\nComprenez ce qu'elle dit vraiment."):
                    style "trl_quote"
                    size 24
                    xmaximum 320
                text _("STABILITÉ 11.4 / 17.0 s") style "trl_hud" size 20 color "#FFD166"

        frame:
            xpos 1444
            ypos 250
            xsize 320
            ysize 130
            background Solid("#170A12EC")
            padding (22, 16)
            vbox:
                spacing 6
                text _("TEMPS RESTANT") style "trl_micro" xalign 0.5
                text "00:08.4" at trl_pulse(0.55, 1.0, 0.5):
                    xalign 0.5
                    style "trl_hud_big"
                    size 52
                    color "#FF6875"


# --- 11.g  FRACTURE — QTE ------------------------------------
transform trl_qte_ring:
    zoom 2.2
    alpha 0.0
    block:
        linear 0.10 alpha 0.95
        linear 0.75 zoom 1.02
        linear 0.10 alpha 0.0
        pause 0.35
        zoom 2.2
        repeat

transform trl_qte_key:
    alpha 0.0
    zoom 1.4
    block:
        easeout 0.14 alpha 1.0 zoom 1.0
        pause 0.72
        easein 0.10 zoom 1.25 alpha 0.0
        pause 0.35
        repeat

transform trl_qte_hit:
    alpha 0.0
    block:
        pause 0.86
        linear 0.05 alpha 0.55
        linear 0.22 alpha 0.0
        pause 0.18
        repeat

screen trl_mg_fracture():
    use trl_mg_chrome(_("FRACTURE"), _("LE CANAL SE DÉCHIRE"), "#FF3A5C"):

        add Solid("#050208")
        add "images/background/cg/bg_cg012.png" at trl_unstable(4, 1.10):
            alpha 0.80
        add Solid("#2A0410") alpha 0.42
        add Solid("#FF3A5C") at trl_qte_hit:
            xsize 1920
            ysize 1080

        add Transform("images/hud/ring_dashed.png", matrixcolor=TintMatrix("#FF4560")) at trl_qte_ring:
            xysize (340, 340)
            xalign 0.5
            yalign 0.47

        frame at trl_qte_key:
            xalign 0.5
            yalign 0.47
            xsize 220
            ysize 130
            background Solid("#12050CEE")
            padding (0, 0)
            text _("ESPACE"):
                align (0.5, 0.5)
                style "trl_hud"
                size 46
                color "#FFE9EE"

        # Vies restantes.
        hbox:
            xpos 156
            ypos 250
            spacing 16
            text _("INTÉGRITÉ") style "trl_hud" size 24 color "#FF7C88" yoffset 4
            add Solid("#FF3A5C") xsize 26 ysize 26 yoffset 4
            add Solid("#FF3A5C") xsize 26 ysize 26 yoffset 4
            add Solid("#3A1420") xsize 26 ysize 26 yoffset 4

        text _("TRANSMISSION CORROMPUE — SÉQUENCE 4 / 6"):
            style "trl_micro"
            xpos 156
            ypos 300
            color "#FF9AA6"

        vbox:
            xalign 0.5
            ypos 780
            spacing 10
            text _("« Ma-Maintenez. Le. Si-signal. »") at trl_pulse(0.45, 1.0, 0.35):
                xalign 0.5
                style "trl_quote"
                size 34
                color "#FFD9DF"
            text _("KAMI // CANAL 07"):
                xalign 0.5
                style "trl_micro"
                color "#FF7C88"


# ------------------------------------------------------------
# 12. CARTON FINAL
# ------------------------------------------------------------
transform trl_logo_in:
    alpha 0.0
    zoom 1.16
    easeout 0.55 alpha 1.0 zoom 1.0
    block:
        linear 5.0 zoom 1.03
        repeat

screen trl_endcard(sub1, sub2, note=None):
    zorder 460

    $ sub1 = trl_localize(sub1)
    $ sub2 = trl_localize(sub2)
    $ note = trl_localize(note)

    add Solid("#01040A")
    add "gui/main_menu_kami/bg_orbit.png" at trl_push(16.0, 1.04, 1.12):
        alpha 0.18

    # Le logo est calé haut : le bloc de texte occupe le tiers bas
    # sans jamais mordre sur le lettrage « KAMI'S DESIRES ».
    add "images/logo.png" at trl_logo_in:
        fit "contain"
        xalign 0.5
        ypos 104
        xysize (980, 654)

    add "gui/main_menu_kami/scanlines.png" alpha 0.12
    add "gui/main_menu_kami/vignette.png" alpha 0.72

    add Solid("#5CD3FF") at trl_rule_grow(0.55, 1.0):
        xalign 0.5
        ypos 806
        xsize 520
        ysize 2

    text sub1 at trl_word_in(0.70, 16):
        xalign 0.5
        ypos 830
        style "trl_h2"
        size 40
        color "#E6F4FB"

    text sub2 at trl_word_in(0.90, 14):
        xalign 0.5
        ypos 890
        style "trl_kicker"
        size 24

    if note:
        text note at trl_fade_in(1.30, 0.8):
            xalign 0.5
            ypos 934
            style "trl_micro"
            size 19
            color "#89B7CC"


# Épilogue : deux lignes froides sur fond noir.
screen trl_epilogue(line1, line2=None, delay2=1.6):
    zorder 470

    $ line1 = trl_localize(line1)
    $ line2 = trl_localize(line2)

    add Solid("#000000")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 26

        text line1 at trl_fade_in(0.25, 0.8):
            xalign 0.5
            style "trl_kicker"
            size 30
            color "#8FDFFF"

        if line2:
            text line2 at trl_word_jitter(delay2):
                xalign 0.5
                style "trl_kicker"
                size 34
                color "#FF5E6E"
