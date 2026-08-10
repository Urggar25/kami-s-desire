# =============================================================
# DAY 1 — UI PROFESSIONNEL
# Palette cohérente avec day0_ui.rpy :
#   #06090D bg / #0D1520 surface / #1A2D3E bordure
#   #5CD3FF cyan / #3BCC82 vert / #F0A835 orange / #E03850 rouge
#   #D6E8F0 texte primaire / #7A98A8 texte secondaire
# =============================================================


# =============================================================
# INDICATEUR JOUR / PÉRIODE  (style Danganronpa — coin haut droit)
# =============================================================

default current_period = "Matin"

# -------------------------------------------------------------
# OVERLAY JOUR / PÉRIODE  — HUD sci-fi animé (coin haut droit)
# Drop-in : utilise current_day (int) + current_period (str)
# Assets : images/hud/*.png
# -------------------------------------------------------------

# Accent selon la période (fallback cyan)
init python:
    DAY_PERIOD_HUD_PNC_SCREENS = (
        "pnc_room",
        "pnc_chambre",
        "pnc_chambre_j8",
        "pnc_chambre_j12",
        "pnc_dortoir",
        "pnc_cafeteria",
        "pnc_archive",
        "pnc_conclave",
        "pnc_canon",
        "pnc_maintenance",
        "pnc_gymnase",
        "pnc_infirmerie",
        "pnc_livraison",
        "pnc_observation",
        "pnc_repos",
        "pnc_stockage",
        "day1_conclave_pnc",
        "day4_tray_pnc",
    )

    def day_period_hud_is_pnc_active():
        for screen_name in DAY_PERIOD_HUD_PNC_SCREENS:
            if renpy.get_screen(screen_name):
                return True
        return False

    def day_period_hud_should_show():
        if getattr(store, "current_day", 0) <= 0:
            return False
        if day_period_hud_is_pnc_active():
            return False
        return True

    if "day_period_hud" not in config.overlay_screens:
        config.overlay_screens.append("day_period_hud")

    def _hud_accent(p):
        p = (p or "").lower()
        if "matin" in p:                       return "#F0A835"   # orange lever
        if "midi" in p or "après" in p or "apres" in p: return "#5CD3FF"  # cyan plein jour
        if "soir" in p:                         return "#E86A45"   # ambre couchant
        if "nuit" in p:                         return "#8C6BFF"   # violet nuit
        return "#5CD3FF"

# --- Animations d'anneaux ---
transform hud_spin_cw(t=24.0, z=0.264):
    anchor (0.5, 0.5)
    zoom z
    rotate 0
    linear t rotate 360
    repeat

transform hud_spin_ccw(t=30.0, z=0.19):
    anchor (0.5, 0.5)
    zoom z
    rotate 360
    linear t rotate 0
    repeat

transform hud_scan(t=6.0, z=0.264):
    anchor (0.5, 0.5)
    zoom z
    rotate 0
    linear t rotate 360
    repeat

transform hud_static(z=0.287):
    anchor (0.5, 0.5)
    zoom z

transform hud_pulse(z0=0.322, z1=0.36):
    anchor (0.5, 0.5)
    zoom z0
    block:
        ease 1.7 zoom z1 alpha 1.0
        ease 1.7 zoom z0 alpha 0.72
        repeat

transform hud_sun_breathe(z0=0.273, z1=0.288):
    anchor (0.5, 0.5)
    zoom z0
    block:
        ease 1.9 zoom z1
        ease 1.9 zoom z0
        repeat

# --- Entrée / clignotement label ---
transform hud_appear:
    alpha 0.0
    xoffset 40
    easein 0.45 alpha 1.0 xoffset 0

transform hud_period_blink:
    alpha 0.55
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.55
    repeat


screen day_period_hud():
    if day_period_hud_should_show():
        use day_period_hud_content


screen day_period_hud_content():
    zorder 65

    $ _acc = _hud_accent(current_period)

    fixed at hud_appear:
        xalign 0.995
        yalign 0.028
        xysize (430, 150)

        # ---- Fond + cadre ----
        add Solid("#06090DDD") xpos 0 ypos 0 xsize 430 ysize 150
        add Solid("#5CD3FF")   xpos 0 ypos 0 xsize 430 ysize 2      # barre top
        add Solid("#5CD3FF33") xpos 0 ypos 148 xsize 430 ysize 2    # barre bottom
        add Solid("#5CD3FF55") xpos 0 ypos 0 xsize 2 ysize 150      # barre gauche
        # coins (brackets)
        add Solid("#5CD3FF") xpos 0 ypos 0 xsize 26 ysize 2
        add Solid("#5CD3FF") xpos 404 ypos 148 xsize 26 ysize 2

        # ---- Bloc texte gauche ----
        text "DAY":
            xpos 28 ypos 32
            size 20 color "#5CD3FF"
            font "fonts/Rajdhani-SemiBold.ttf" kerning 6

        text "%03d" % current_day:
            xpos 28 ypos 40
            size 64 color "#D6E8F0"
            font "fonts/day_font.ttf"
            outlines [(1, "#5CD3FF88", 0, 0)]
            offset (66, 0)

        # soulignement
        add Solid("#5CD3FF") xpos 30 ypos 116 xsize 170 ysize 2
        add Solid(_acc)      xpos 30 ypos 116 xsize 50  ysize 2

        text current_period at hud_period_blink:
            xpos 30 ypos 120
            size 22 color _acc
            font "fonts/Rajdhani-SemiBold.ttf" kerning 2

        # ligne de liaison texte -> cercle
        add Solid("#5CD3FF66") xpos 208 ypos 72 xsize 44 ysize 1

        # ---- Assemblage cercle animé (droite) ----
        fixed:
            xpos 268 ypos -5
            xysize (160, 160)

            add "images/hud/glow.png"       at hud_pulse(0.30, 0.34)     xpos 0.5 ypos 0.5
            add "images/hud/ring_ticks.png" at hud_spin_cw(24.0, 0.264)  xpos 0.5 ypos 0.5
            add "images/hud/scan_arc.png"   at hud_scan(5.0, 0.264)      xpos 0.5 ypos 0.5
            add "images/hud/ring_thin.png"  at hud_spin_ccw(38.0, 0.287) xpos 0.5 ypos 0.5
            add "images/hud/ring_dashed.png" at hud_spin_ccw(20.0, 0.19) xpos 0.5 ypos 0.5
            add "images/hud/core_dot.png"   at hud_static(0.55)          xpos 0.5 ypos 0.5
            add "images/hud/sun_icon.png"   at hud_sun_breathe           xpos 0.5 ypos 0.5


# =============================================================
# TRANSFORMS ENTRÉE / SORTIE  PERSONNAGES
# =============================================================

transform char_enter_left(xp=0.22):
    xalign xp yalign 1.0
    xoffset -70 alpha 0.0
    linear 0.28 xoffset 0 alpha 1.0

transform char_enter_right(xp=0.78):
    xalign xp yalign 1.0
    xoffset 70 alpha 0.0
    linear 0.28 xoffset 0 alpha 1.0

transform char_enter_center(xp=0.50):
    xalign xp yalign 1.0
    yoffset 40 alpha 0.0
    linear 0.28 yoffset 0 alpha 1.0

transform char_exit_left(xp=0.22):
    xalign xp yalign 1.0
    linear 0.22 xoffset -70 alpha 0.0

transform char_exit_right(xp=0.78):
    xalign xp yalign 1.0
    linear 0.22 xoffset 70 alpha 0.0

transform char_exit_center(xp=0.50):
    xalign xp yalign 1.0
    linear 0.22 yoffset 40 alpha 0.0


# =============================================================
# TRANSFORMS LOCAUX DAY1
# =============================================================

transform d1_blink:
    alpha 0.3
    linear 0.6 alpha 0.9
    linear 0.6 alpha 0.3
    repeat

transform d1_blink_fast:
    alpha 0.15
    linear 0.2 alpha 1.0
    linear 0.2 alpha 0.15
    repeat

transform d1_pulse_cyan:
    alpha 0.0
    linear 0.5 alpha 0.5
    linear 0.5 alpha 0.0
    repeat

transform d1_scanline:
    ypos 0.0
    linear 2.5 ypos 1.0
    repeat

transform d1_appear:
    alpha 0.0
    yoffset 10
    linear 0.25 alpha 1.0 yoffset 0

transform d1_card_hover:
    zoom 1.0
    linear 0.12 zoom 1.02
    linear 0.12 zoom 1.0
    repeat

transform d1_stamp_in:
    alpha 0.0
    zoom 2.0
    rotate -8
    easein 0.18 alpha 1.0 zoom 1.0
    easeout 0.06 zoom 1.04
    easein 0.06 zoom 1.0

transform d1_glitch:
    xoffset 0
    linear 0.04 xoffset -6
    linear 0.03 xoffset 8
    linear 0.03 xoffset -4
    linear 0.04 xoffset 0

transform d1_warning_flash:
    alpha 0.0
    linear 0.12 alpha 1.0
    linear 0.12 alpha 0.0
    linear 0.12 alpha 1.0
    linear 0.12 alpha 0.0
    linear 0.12 alpha 1.0
    pause 1.0
    linear 0.25 alpha 0.0


# =============================================================
# WAKEUP OVERLAY
# =============================================================

transform d1_wakeup_breathe(alpha_min=0.20, alpha_max=0.34):
    alpha alpha_min
    ease 2.8 alpha alpha_max
    ease 2.8 alpha alpha_min
    repeat

transform d1_wakeup_scan:
    alpha 0.0
    yoffset -120
    linear 0.25 alpha 0.16
    linear 2.4 yoffset 1200
    linear 0.25 alpha 0.0
    pause 0.6
    repeat

transform d1_wakeup_focus:
    alpha 0.0
    easeout 0.7 alpha 1.0

transform d1_wakeup_flash:
    alpha 0.0
    pause 0.18
    linear 0.06 alpha 0.18
    linear 0.28 alpha 0.0

screen day1_wakeup_overlay(level="heavy"):
    zorder 80

    if level == "heavy":
        add Solid("#02050BD8") at d1_wakeup_focus
        add "gui/day1/wakeup_blur_overlay.png" alpha 0.20 xysize (1920, 1080)
        add "gui/day1/wakeup_noise.png" alpha 0.075 xysize (1920, 1080) at d1_wakeup_breathe(0.05, 0.10)
        add "gui/day1/wakeup_vignette.png" alpha 0.72 xysize (1920, 1080)
        add Solid("#5CD3FF") xpos 0 ypos 0 xsize 1920 ysize 72 at d1_wakeup_scan
        add Solid("#FFFFFF") xysize (1920, 1080) at d1_wakeup_flash
        add Solid("#00000072") xpos 0 ypos 0 xsize 1920 ysize 112
        add Solid("#0000008A") xpos 0 ypos 930 xsize 1920 ysize 150
    elif level == "soft":
        add Solid("#02050B60") at d1_wakeup_focus
        add "gui/day1/wakeup_noise.png" alpha 0.035 xysize (1920, 1080) at d1_wakeup_breathe(0.02, 0.045)
        add "gui/day1/wakeup_vignette.png" alpha 0.42 xysize (1920, 1080)
        add Solid("#00000070") xpos 0 ypos 950 xsize 1920 ysize 130


# =============================================================
# TABLET INTERACTION — refait professionnel thème terminal
# =============================================================

screen day1_tablet_interaction():
    modal True
    zorder 100

    # Fond sombre
    add Solid("#020609EE")

    # Grille déco
    add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.25)
    add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.50)
    add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.75)
    add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1 ysize 1080 at Transform(xpos=0.33)
    add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1 ysize 1080 at Transform(xpos=0.67)

    # Panel principal
    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 780
        ysize 500
        background Frame(Solid("#0D1520F5"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 780
            ysize 500

            # Barre top
            add Solid("#5CD3FF") xpos 0 ypos 0 xsize 780 ysize 2

            # Bande titre
            add Solid("#0A111C") xpos 0 ypos 0 xsize 780 ysize 52

            # Ligne déco verticale gauche
            add Solid("#5CD3FF44") xpos 0 ypos 0 xsize 2 ysize 500

            # Header
            text "INTERFACE PUPITRE — CONCLAVE":
                xpos 22 ypos 14
                size 16
                color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 3

            # Statut badge
            text "SESSION : EN ATTENTE  ▸  VERROUILLÉ" at d1_blink:
                xpos 580 ypos 16
                size 11
                color "#E03850"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1

            # Séparateur
            add Solid("#1A2D3E") xpos 0 ypos 52 xsize 780 ysize 1

            # Corps — infos terminal
            vbox:
                xpos 22 ypos 72
                spacing 16

                # Ligne utilisateur
                hbox:
                    spacing 14
                    text "UTILISATEUR":
                        size 13
                        color "#7A98A8"
                        font "fonts/Rajdhani-SemiBold.ttf"
                    text "NOAM":
                        size 13
                        color "#D6E8F0"
                        font "fonts/Rajdhani-SemiBold.ttf"

                # Ligne statut
                hbox:
                    spacing 14
                    text "STATUT":
                        size 13
                        color "#7A98A8"
                        font "fonts/Rajdhani-SemiBold.ttf"
                    text "REPRÉSENTANT — CONCLAVE JOUR 1":
                        size 13
                        color "#F0A835"
                        font "fonts/Rajdhani-SemiBold.ttf"

                # Séparateur
                add Solid("#1A2D3E") xsize 730 ysize 1

                # Bloc accès
                frame:
                    xsize 736
                    background Frame(Solid("#0A111C"), 0, 0)
                    padding (16, 14)
                    vbox:
                        spacing 10
                        text "ACCÈS TABLETTE":
                            size 12
                            color "#7A98A8"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2

                        text "▸  AMENDEMENTS  —  VERROUILLÉ JUSQU'AU DÉPÔT":
                            size 14
                            color "#E03850"
                            font "fonts/Rajdhani-SemiBold.ttf"

                        text "▸  CODEX  —  ACCÈS PARTIEL":
                            size 14
                            color "#F0A835"
                            font "fonts/Rajdhani-SemiBold.ttf"

                        text "▸  COMMUNICATIONS  —  BLOQUÉES":
                            size 14
                            color "#E03850"
                            font "fonts/Rajdhani-SemiBold.ttf"

                # Avertissement
                frame:
                    xsize 736
                    background Frame(Solid("#200808"), 0, 0)
                    padding (14, 10)
                    hbox:
                        spacing 12
                        text "!" at d1_blink_fast:
                            size 20
                            color "#E03850"
                        text "INTERACTION ENREGISTRÉE — KAMI MONITORING ACTIF":
                            size 13
                            color "#E0385099"
                            font "fonts/Rajdhani-SemiBold.ttf"

            # Bouton retrait
            frame:
                xalign 0.5
                ypos 418
                background Frame(Solid("#0A111C"), 0, 0)
                padding (0, 0)
                button:
                    xsize 260
                    ysize 46
                    background Frame(Solid("#1A2D3E"), 0, 0)
                    hover_background Frame(Solid("#5CD3FF22"), 0, 0)
                    action Return(True)

                    fixed:
                        xsize 260
                        ysize 46
                        add Solid("#5CD3FF") xpos 0 ypos 0 xsize 260 ysize 1
                        add Solid("#5CD3FF") xpos 0 ypos 45 xsize 260 ysize 1
                        text "RETIRER LA MAIN":
                            xalign 0.5 yalign 0.5
                            size 14
                            color "#5CD3FF"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2

            # Scanline animée
            add Solid("#5CD3FF04") xpos 0 ypos 0 xsize 780 ysize 3 at d1_scanline


# =============================================================
# CODEX UNLOCK PANEL
# =============================================================

screen day1_codex_unlock_panel(entry_title):
    zorder 120

    frame at d1_appear:
        xalign 0.5
        ypos 68
        background Frame(Solid("#0D1520F0"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 600
            ysize 52

            add Solid("#3BCC82") xpos 0 ypos 0 xsize 600 ysize 2
            add Solid("#3BCC8233") xpos 0 ypos 2 xsize 600 ysize 50

            text "✦  CODEX  —  NOUVELLE ENTRÉE  :":
                xpos 16 ypos 8
                size 12
                color "#3BCC82"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            text kd_tr(entry_title):
                xpos 16 ypos 28
                size 16
                color "#D6E8F0"
                font "fonts/Rajdhani-SemiBold.ttf"


# =============================================================
# AMENDMENT TIMER — synchronisé avec système day0
# =============================================================

screen day1_amendment_timer():
    zorder 70

    # Variables écran pour le tick
    default _tick = 0
    timer 1.0 repeat True action SetScreenVariable("_tick", _tick + 1)

    $ _t = day0_timer_remaining()
    $ _ts = day0_timer_fmt(_t)
    $ _expired = (_t <= 0 and day0_timer_active)
    $ _warn = (_t < 300)  # rouge sous 5 min
    $ _bar_color = "#E03850" if _warn else "#F0A835"
    $ _txt_color = "#E03850" if _expired else ("#F0A835" if _warn else "#5CD3FF")

    frame:
        xpos 56
        ypos 50
        background Frame(Solid("#06090DEE"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 320
            ysize 68

            # Bande colorée gauche
            add Solid(_bar_color) xpos 0 ypos 0 xsize 4 ysize 68

            # Fond texturé
            add Solid("#FFFFFF05") xpos 4 ypos 0 xsize 316 ysize 68

            # Barre progression temps
            if not _expired:
                $ _pct = day0_timer_pct()
                add Solid(_bar_color + "22") xpos 4 ypos 0 xsize int(316 * _pct) ysize 68

            text "URN" + "E  OUVERTE":
                xpos 18 ypos 8
                size 11
                color "#7A98A8"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            if _expired:
                text "DÉPÔT CLOS" at d1_blink_fast:
                    xpos 18 ypos 26
                    size 26
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
            else:
                text _ts:
                    xpos 18 ypos 26
                    size 26
                    color _txt_color
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True

            text "FERMETURE  ▸  RESTANT":
                xpos 18 ypos 54
                size 10
                color "#3A5A6A"
                font "fonts/Rajdhani-SemiBold.ttf"


# =============================================================
# TUTORIEL — MINIJEU AMENDEMENT
# =============================================================

screen day1_tuto_amendment():
    modal True
    zorder 110

    add Solid("#000000CC")

    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 820
        background Frame(Solid("#0D1520F8"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 820
            ysize 460

            add Solid("#F0A835") xpos 0 ypos 0 xsize 820 ysize 2
            add Solid("#0A111C") xpos 0 ypos 0 xsize 820 ysize 52
            add Solid("#F0A83522") xpos 0 ypos 2 xsize 820 ysize 50

            text "TUTORIEL — PROPOSITION D'AMENDEMENT":
                xpos 22 ypos 14
                size 16
                color "#F0A835"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            add Solid("#1A2D3E") xpos 0 ypos 52 xsize 820 ysize 1

            vbox:
                xpos 22 ypos 70
                spacing 18

                text "Comment proposer un amendement :":
                    size 20
                    color "#D6E8F0"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "① Lisez attentivement les deux propositions de modification de Commandement.":
                    size 15
                    color "#7A98A8"

                text "② Sélectionnez la proposition qui vous semble la plus juste ou la plus utile.":
                    size 15
                    color "#7A98A8"

                text "③ La formulation officielle sera automatiquement retenue.":
                    size 15
                    color "#7A98A8"

                text "④ Une fois validé, l'amendement est anonymement déposé dans l'urne — sans retour possible.":
                    size 15
                    color "#F0A83599"

                add Solid("#1A2D3E") xsize 776 ysize 1

                text "⚠  Ce choix est définitif. Il engage Noam pour l'ensemble du Conclave.":
                    size 14
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"

            # Bouton
            button:
                xalign 0.5
                ypos 396
                xsize 280
                ysize 46
                background Frame(Solid("#1A2D3E"), 0, 0)
                hover_background Frame(Solid("#F0A83533"), 0, 0)
                action Hide("day1_tuto_amendment")

                fixed:
                    xsize 280
                    ysize 46
                    add Solid("#F0A835") xpos 0 ypos 0 xsize 280 ysize 1
                    text "COMPRIS — CONTINUER":
                        xalign 0.5 yalign 0.5
                        size 14
                        color "#F0A835"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 2


# =============================================================
# MINIJEU AMENDEMENT — TERMINAL CONSTITUTIONNEL
# Interface en deux phases :
#   PHASE A — Analyse des deux propositions (cartes expandables)
#   PHASE B — Validation + stamp dramatique
# =============================================================

transform d1_card_select_glow:
    alpha 0.0
    linear 0.18 alpha 1.0

transform d1_card_deselect:
    alpha 1.0
    linear 0.18 alpha 0.85

transform d1_validate_pulse:
    zoom 1.0
    linear 0.3 zoom 1.02
    linear 0.3 zoom 1.0
    repeat

screen day1_amendment_form():
    modal True
    zorder 100

    default selected = noam_amendement_choix if noam_amendement_choix else "information_locale"
    default phase = "select"  # "select" | "confirm"
    default hovered = None

    add Solid("#020609F5")

    # Grille déco
    add Solid("#5CD3FF06") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.20)
    add Solid("#5CD3FF06") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.50)
    add Solid("#5CD3FF06") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=0.80)

    # === PHASE SELECT ===
    if phase == "select":

        # Header
        frame at d1_appear:
            xalign 0.5
            ypos 30
            xsize 1200
            background Frame(Solid("#0D1520"), 0, 0)
            padding (0, 0)

            fixed:
                xsize 1200
                ysize 58

                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 1200 ysize 2
                add Solid("#0A111C") xpos 0 ypos 0 xsize 1200 ysize 58

                text "TERMINAL CONSTITUTIONNEL — PROPOSITION D'AMENDEMENT":
                    xpos 22 ypos 10
                    size 17
                    color "#5CD3FF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 3

                text "REPRÉSENTANT : NOAM  ▸  STATUT : BROUILLON  ▸  ANONYMAT : GARANTI":
                    xpos 22 ypos 34
                    size 11
                    color "#7A98A8"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 1

        # Cartes
        hbox:
            xalign 0.5
            ypos 108
            spacing 24

            for card in day1_amendment_cards:
                $ cid = card["id"]
                $ is_sel = (selected == cid)
                $ is_hov = (hovered == cid)

                button:
                    xsize 572
                    ysize 500
                    background Frame(Solid("#0D1B28" if is_sel else "#08111A"), 0, 0)
                    hover_background Frame(Solid("#0D1B28"), 0, 0)
                    action [SetScreenVariable("selected", cid)]
                    hovered SetScreenVariable("hovered", cid)
                    unhovered SetScreenVariable("hovered", None)

                    fixed:
                        xsize 572
                        ysize 500

                        # Bordure top colorée
                        add Solid("#5CD3FF" if is_sel else "#1A2D3E") xpos 0 ypos 0 xsize 572 ysize 2

                        # Indicateur sélection gauche
                        add Solid("#5CD3FF" if is_sel else "#1A2D3E22") xpos 0 ypos 0 xsize 4 ysize 500

                        # Badge sélectionné
                        if is_sel:
                            frame at d1_stamp_in:
                                xpos 504 ypos 10
                                background Frame(Solid("#5CD3FF22"), 0, 0)
                                padding (8, 4)
                                text "SÉLECTIONNÉ":
                                    size 10
                                    color "#5CD3FF"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    kerning 2

                        vbox:
                            xpos 20 ypos 18
                            xsize 532
                            spacing 14

                            # Titre
                            text card["title"]:
                                size 22
                                color ("#D6E8F0" if is_sel else "#7A98A8")
                                font "fonts/Rajdhani-SemiBold.ttf"

                            # Commandement
                            text card["commandment"]:
                                size 12
                                color ("#5CD3FF" if is_sel else "#3A5A6A")
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 2

                            add Solid("#1A2D3E") xsize 530 ysize 1

                            # Intention
                            frame:
                                xsize 530
                                background Frame(Solid("#060E18"), 0, 0)
                                padding (12, 10)
                                vbox:
                                    spacing 4
                                    text "INTENTION":
                                        size 11
                                        color "#F0A835"
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                        kerning 2
                                    text card["intent"]:
                                        size 14
                                        color "#C8DDE8"

                            # Formulation courte
                            frame:
                                xsize 530
                                background Frame(Solid("#060E18"), 0, 0)
                                padding (12, 10)
                                vbox:
                                    spacing 4
                                    text "FORMULATION":
                                        size 11
                                        color "#3BCC82"
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                        kerning 2
                                    text card["short_wording"]:
                                        size 13
                                        color "#B8D4C8"

                            # Risques
                            frame:
                                xsize 530
                                background Frame(Solid("#1A0808"), 0, 0)
                                padding (12, 10)
                                vbox:
                                    spacing 4
                                    text "RISQUE IDENTIFIÉ":
                                        size 11
                                        color "#E03850"
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                        kerning 2
                                    text card["risks"]:
                                        size 13
                                        color "#D89898"

        # Formulation officielle retenue
        $ selected_card = [c for c in day1_amendment_cards if c["id"] == selected][0]

        frame at d1_appear:
            xalign 0.5
            ypos 622
            xsize 1168
            background Frame(Solid("#0A111C"), 0, 0)
            padding (0, 0)

            fixed:
                xsize 1168
                ysize 68

                add Solid("#5CD3FF22") xpos 0 ypos 0 xsize 1168 ysize 68
                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 1168 ysize 1

                text "FORMULATION OFFICIELLE RETENUE :":
                    xpos 16 ypos 8
                    size 11
                    color "#5CD3FF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

                text selected_card["wording"]:
                    xpos 16 ypos 28
                    size 13
                    color "#D6E8F0"
                    xmaximum 1136

        # Bouton valider
        button at d1_validate_pulse:
            xalign 0.5
            ypos 704
            xsize 380
            ysize 56
            background Frame(Solid("#0A2A18"), 0, 0)
            hover_background Frame(Solid("#3BCC8233"), 0, 0)
            action [SetScreenVariable("phase", "confirm")]

            fixed:
                xsize 380
                ysize 56
                add Solid("#3BCC82") xpos 0 ypos 0 xsize 380 ysize 2
                add Solid("#3BCC82") xpos 0 ypos 54 xsize 380 ysize 2
                text "VALIDER LA PROPOSITION":
                    xalign 0.5 yalign 0.5
                    size 17
                    color "#3BCC82"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

    # === PHASE CONFIRM ===
    elif phase == "confirm":

        $ selected_card = [c for c in day1_amendment_cards if c["id"] == selected][0]

        # Fond dramatique
        add Solid("#010408F8")

        frame at d1_appear:
            xalign 0.5
            yalign 0.5
            xsize 780
            background Frame(Solid("#0D1520"), 0, 0)
            padding (0, 0)

            fixed:
                xsize 780
                ysize 480

                add Solid("#3BCC82") xpos 0 ypos 0 xsize 780 ysize 2
                add Solid("#0A111C") xpos 0 ypos 0 xsize 780 ysize 56

                text "CONFIRMATION — DÉPÔT DÉFINITIF":
                    xpos 22 ypos 16
                    size 17
                    color "#3BCC82"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

                add Solid("#1A2D3E") xpos 0 ypos 56 xsize 780 ysize 1

                vbox:
                    xpos 22 ypos 74
                    xsize 736
                    spacing 16

                    text selected_card["title"]:
                        size 26
                        color "#D6E8F0"
                        font "fonts/Rajdhani-SemiBold.ttf"

                    text selected_card["commandment"]:
                        size 13
                        color "#5CD3FF"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 2

                    add Solid("#1A2D3E") xsize 736 ysize 1

                    frame:
                        xsize 736
                        background Frame(Solid("#060E18"), 0, 0)
                        padding (14, 12)
                        text selected_card["wording"]:
                            size 14
                            color "#C8DDE8"

                    frame:
                        xsize 736
                        background Frame(Solid("#1A0808"), 0, 0)
                        padding (14, 10)
                        hbox:
                            spacing 10
                            text "!" at d1_blink_fast:
                                size 18
                                color "#E03850"
                            text "Ce dépôt est IRRÉVERSIBLE. L'amendement sera traité de façon anonyme.":
                                size 13
                                color "#E0385099"
                                font "fonts/Rajdhani-SemiBold.ttf"

                # Boutons
                hbox:
                    xalign 0.5
                    ypos 412
                    spacing 20

                    button:
                        xsize 200
                        ysize 46
                        background Frame(Solid("#1A1008"), 0, 0)
                        hover_background Frame(Solid("#F0A83522"), 0, 0)
                        action SetScreenVariable("phase", "select")
                        fixed:
                            xsize 200
                            ysize 46
                            add Solid("#F0A835") xpos 0 ypos 0 xsize 200 ysize 1
                            text "← MODIFIER":
                                xalign 0.5 yalign 0.5
                                size 14
                                color "#F0A835"
                                font "fonts/Rajdhani-SemiBold.ttf"

                    button:
                        xsize 280
                        ysize 46
                        background Frame(Solid("#0A2A18"), 0, 0)
                        hover_background Frame(Solid("#3BCC8233"), 0, 0)
                        action Return(selected)
                        fixed:
                            xsize 280
                            ysize 46
                            add Solid("#3BCC82") xpos 0 ypos 0 xsize 280 ysize 1
                            add Solid("#3BCC82") xpos 0 ypos 45 xsize 280 ysize 1
                            text "DÉPOSER DANS L'URNE →":
                                xalign 0.5 yalign 0.5
                                size 14
                                color "#3BCC82"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 1


# =============================================================
# URN CONFIRMATION
# =============================================================

screen day1_urn_confirmation():
    modal True
    zorder 105

    add Solid("#020609F0")

    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 680
        background Frame(Solid("#0D1520"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 680
            ysize 340

            add Solid("#3BCC82") xpos 0 ypos 0 xsize 680 ysize 2
            add Solid("#0A111C") xpos 0 ypos 0 xsize 680 ysize 56

            text "AMENDEMENT DÉPOSÉ":
                xpos 22 ypos 14
                size 20
                color "#3BCC82"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            add Solid("#1A2D3E") xpos 0 ypos 56 xsize 680 ysize 1

            vbox:
                xpos 22 ypos 74
                spacing 14

                hbox:
                    spacing 12
                    text "●":
                        size 16
                        color "#3BCC82"
                    text "RETRAIT IMPOSSIBLE":
                        size 16
                        color "#D6E8F0"
                        font "fonts/Rajdhani-SemiBold.ttf"

                hbox:
                    spacing 12
                    text "●":
                        size 16
                        color "#3BCC82"
                    text "ENREGISTREMENT CONFIRMÉ":
                        size 16
                        color "#D6E8F0"
                        font "fonts/Rajdhani-SemiBold.ttf"

                hbox:
                    spacing 12
                    text "●" at d1_blink_fast:
                        size 16
                        color "#F0A835"
                    text "ANONYMAT GARANTI — KAMI NE PEUT PAS IDENTIFIER L'AUTEUR":
                        size 14
                        color "#7A98A8"

                hbox:
                    spacing 12
                    text "●":
                        size 16
                        color "#5CD3FF"
                    text "TIRAGE AU SORT DEMAIN À 09:00":
                        size 14
                        color "#5CD3FF"
                        font "fonts/Rajdhani-SemiBold.ttf"

            button:
                xalign 0.5
                ypos 280
                xsize 300
                ysize 44
                background Frame(Solid("#1A2D3E"), 0, 0)
                hover_background Frame(Solid("#5CD3FF22"), 0, 0)
                action Return(True)

                fixed:
                    xsize 300
                    ysize 44
                    add Solid("#5CD3FF44") xpos 0 ypos 0 xsize 300 ysize 1
                    text "RECULER DE L'URNE":
                        xalign 0.5 yalign 0.5
                        size 14
                        color "#5CD3FF"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 1


# =============================================================
# PANNEAU BROUILLEUR — thème terminal
# =============================================================

screen day1_jammer_panel():
    modal True
    zorder 100

    add Solid("#020609EE")

    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 740
        background Frame(Solid("#0D1520"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 740
            ysize 510

            # Couleur selon état
            $ jcol = "#3BCC82" if noam_room_jammer_on else "#E03850"

            add Solid(jcol) xpos 0 ypos 0 xsize 740 ysize 2
            add Solid("#0A111C") xpos 0 ypos 0 xsize 740 ysize 56
            add Solid(jcol + "22") xpos 0 ypos 2 xsize 740 ysize 54

            text "INTERFACE CHAMBRE — BROUILLEUR":
                xpos 22 ypos 14
                size 17
                color jcol
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            add Solid("#1A2D3E") xpos 0 ypos 56 xsize 740 ysize 1

            vbox:
                xpos 22 ypos 76
                spacing 16

                # Statut principal
                frame:
                    xsize 696
                    background Frame(Solid("#060E18"), 0, 0)
                    padding (16, 14)

                    hbox:
                        spacing 16
                        text "●" at d1_blink:
                            size 28
                            color jcol
                        vbox:
                            spacing 4
                            text "BROUILLEUR : " + ("ACTIF" if noam_room_jammer_on else "INACTIF"):
                                size 20
                                color jcol
                                font "fonts/Rajdhani-SemiBold.ttf"
                            text "MODE PRIVÉ : " + ("ACTIVÉ" if noam_room_jammer_on else "DÉSACTIVÉ"):
                                size 14
                                color jcol + "88"
                                font "fonts/Rajdhani-SemiBold.ttf"

                # État caméras / audio
                if noam_room_jammer_on:
                    hbox:
                        spacing 12
                        vbox:
                            spacing 10

                            frame:
                                xsize 338
                                background Frame(Solid("#060E18"), 0, 0)
                                padding (12, 10)
                                hbox:
                                    spacing 10
                                    text "■":
                                        size 14
                                        color "#3BCC82"
                                    text "CAMÉRA : COUPÉE":
                                        size 14
                                        color "#7A98A8"

                            frame:
                                xsize 338
                                background Frame(Solid("#060E18"), 0, 0)
                                padding (12, 10)
                                hbox:
                                    spacing 10
                                    text "■":
                                        size 14
                                        color "#3BCC82"
                                    text "AUDIO : COUPÉ":
                                        size 14
                                        color "#7A98A8"

                        vbox:
                            spacing 10
                            frame:
                                xsize 338
                                background Frame(Solid("#060E18"), 0, 0)
                                padding (12, 10)
                                hbox:
                                    spacing 10
                                    text "■":
                                        size 14
                                        color "#3BCC82"
                                    text "CAPTEURS : COUPÉS":
                                        size 14
                                        color "#7A98A8"

                            frame:
                                xsize 338
                                background Frame(Solid("#0A2A18"), 0, 0)
                                padding (12, 10)
                                hbox:
                                    spacing 10
                                    text "■":
                                        size 14
                                        color "#3BCC82"
                                    text "KAMI : AVEUGLE":
                                        size 14
                                        color "#3BCC82"

                else:
                    frame:
                        xsize 696
                        background Frame(Solid("#200808"), 0, 0)
                        padding (14, 12)
                        hbox:
                            spacing 12
                            text "!" at d1_blink_fast:
                                size 18
                                color "#E03850"
                            text "SURVEILLANCE POTENTIELLE — KAMI PEUT OBSERVER CETTE PIÈCE":
                                size 13
                                color "#E0385099"
                                font "fonts/Rajdhani-SemiBold.ttf"

                # Bouton action
                if noam_room_jammer_on:
                    button:
                        xsize 350
                        ysize 46
                        background Frame(Solid("#200808"), 0, 0)
                        hover_background Frame(Solid("#E0385022"), 0, 0)
                        action SetVariable("noam_room_jammer_on", False)

                        fixed:
                            xsize 350
                            ysize 46
                            add Solid("#E03850") xpos 0 ypos 0 xsize 350 ysize 1
                            text "DÉSACTIVER LE BROUILLEUR":
                                xalign 0.5 yalign 0.5
                                size 14
                                color "#E03850"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 1
                else:
                    button:
                        xsize 350
                        ysize 46
                        background Frame(Solid("#0A2A18"), 0, 0)
                        hover_background Frame(Solid("#3BCC8222"), 0, 0)
                        action SetVariable("noam_room_jammer_on", True)

                        fixed:
                            xsize 350
                            ysize 46
                            add Solid("#3BCC82") xpos 0 ypos 0 xsize 350 ysize 1
                            text "RÉACTIVER LE BROUILLEUR":
                                xalign 0.5 yalign 0.5
                                size 14
                                color "#3BCC82"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 1

            # Bouton quitter
            button:
                xalign 0.5
                ypos 454
                xsize 260
                ysize 44
                background Frame(Solid("#0A111C"), 0, 0)
                hover_background Frame(Solid("#5CD3FF11"), 0, 0)
                action Return(noam_room_jammer_on)

                fixed:
                    xsize 260
                    ysize 44
                    add Solid("#5CD3FF33") xpos 0 ypos 0 xsize 260 ysize 1
                    text "QUITTER L'INTERFACE":
                        xalign 0.5 yalign 0.5
                        size 13
                        color "#7A98A8"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 1


# =============================================================
# TUTORIEL TRACE QTE (jour 1)
# =============================================================

screen day1_tuto_trace():
    modal True
    zorder 110

    add Solid("#000000CC")

    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 780
        background Frame(Solid("#0D1520F8"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 780
            ysize 380

            add Solid("#5CD3FF") xpos 0 ypos 0 xsize 780 ysize 2
            add Solid("#0A111C") xpos 0 ypos 0 xsize 780 ysize 52

            text "TUTORIEL — SYNCHRONISATION MOTRICE":
                xpos 22 ypos 14
                size 16
                color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            add Solid("#1A2D3E") xpos 0 ypos 52 xsize 780 ysize 1

            vbox:
                xpos 22 ypos 72
                spacing 16

                text "Comment répondre à un QTE de trace :":
                    size 19
                    color "#D6E8F0"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "① Une courbe ou un chemin s'affiche à l'écran.":
                    size 14
                    color "#7A98A8"

                text "② Suivez ce tracé avec votre souris le plus précisément possible.":
                    size 14
                    color "#7A98A8"

                text "③ Restez dans la tolérance indiquée (zone colorée) pour valider.":
                    size 14
                    color "#7A98A8"

                text "④ Trop d'erreurs = échec. Restez concentré et allez à un rythme régulier.":
                    size 14
                    color "#7A98A8"

                add Solid("#1A2D3E") xsize 736 ysize 1

                text "Ce QTE simule la perte de contrôle moteur de Noam au réveil.":
                    size 13
                    color "#5CD3FF88"
                    font "fonts/Rajdhani-SemiBold.ttf"

            button:
                xalign 0.5
                ypos 322
                xsize 280
                ysize 44
                background Frame(Solid("#1A2D3E"), 0, 0)
                hover_background Frame(Solid("#5CD3FF22"), 0, 0)
                action Hide("day1_tuto_trace")

                fixed:
                    xsize 280
                    ysize 44
                    add Solid("#5CD3FF") xpos 0 ypos 0 xsize 280 ysize 1
                    text "COMPRIS — LANCER LE QTE":
                        xalign 0.5 yalign 0.5
                        size 14
                        color "#5CD3FF"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 2
