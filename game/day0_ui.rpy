# =============================================================
# DAY 0 — UI PROFESSIONNEL
# Scanner badge, téléphone, commandements, timer, sélection, flashback
# Palette : #06090D bg / #0D1520 surface / #1A2D3E bordure
#           #5CD3FF cyan / #3BCC82 vert / #F0A835 orange / #E03850 rouge
#           #D6E8F0 texte primaire / #7A98A8 texte secondaire
# =============================================================


# =============================================================
# TRANSFORMS LOCAUX DAY0
# =============================================================

transform d0_blink:
    alpha 0.25
    linear 0.55 alpha 0.85
    linear 0.55 alpha 0.25
    repeat

transform d0_blink_fast:
    alpha 0.15
    linear 0.22 alpha 1.0
    linear 0.22 alpha 0.15
    repeat

transform d0_pulse_green:
    alpha 0.0
    linear 0.45 alpha 0.55
    linear 0.45 alpha 0.0
    repeat

transform d0_sweep:
    yoffset 0
    alpha 0.0
    linear 0.08 alpha 0.9
    linear 0.75 yoffset 202
    linear 0.12 alpha 0.0
    yoffset 0
    pause 0.18
    repeat

transform d0_selection_spin:
    alpha 0.65
    linear 0.28 alpha 1.0
    linear 0.28 alpha 0.65
    repeat

transform d0_stamp_appear:
    alpha 0.0
    zoom 2.2
    rotate -12
    easein 0.18 alpha 1.0 zoom 1.0
    easeout 0.06 zoom 1.04
    easein 0.06 zoom 1.0

transform d0_flash_update:
    alpha 1.0
    linear 0.25 alpha 0.0
    linear 0.25 alpha 1.0

transform d0_bar_fill(w=0):
    xsize w

transform d0_appear:
    alpha 0.0
    yoffset 8
    linear 0.22 alpha 1.0 yoffset 0

transform d0_scanline_move:
    ypos 0.0
    linear 3.0 ypos 1.0
    repeat

# Flashback overlay
transform d0_flashback_vignette:
    alpha 0.0
    linear 0.6 alpha 1.0

transform d0_flashback_out:
    alpha 1.0
    linear 0.5 alpha 0.0

transform d0_grain_scroll:
    xpos 0 ypos 0
    linear 8.0 xpos -40 ypos -30
    linear 8.0 xpos 0 ypos 0
    repeat

transform d0_title_flash:
    alpha 0.0
    linear 0.15 alpha 1.0
    pause 0.9
    linear 0.2 alpha 0.0


# =============================================================
# TIMER — SYSTÈME DYNAMIQUE
# =============================================================

default day0_timer_end_time  = 0.0
default day0_timer_total     = 0.0
default day0_timer_active    = False
default day0_timer_end_label = None
default day0_timer_flash_id  = 0

init python:
    def day0_timer_now():
        import time
        return time.time()

    def day0_timer_init(h=0, m=0, s=0, total_seconds=None, end_label=None):
        """Initialise et démarre le timer. Appeler AVANT show screen day0_countdown_overlay."""
        if total_seconds is None:
            total_seconds = h * 3600 + m * 60 + s
        store.day0_timer_end_time  = day0_timer_now() + total_seconds
        store.day0_timer_total     = float(total_seconds)
        store.day0_timer_active    = True
        store.day0_timer_end_label = end_label

    def day0_timer_set(new_total_seconds):
        """Modifie le temps restant avec animation de flash."""
        store.day0_timer_end_time = day0_timer_now() + new_total_seconds
        store.day0_timer_flash_id += 1
        renpy.restart_interaction()

    def day0_timer_remaining():
        if not store.day0_timer_active:
            return 0.0
        return max(0.0, store.day0_timer_end_time - day0_timer_now())

    def day0_timer_fmt(t=None):
        if t is None:
            t = day0_timer_remaining()
        h = int(t) // 3600
        m = (int(t) % 3600) // 60
        s = int(t) % 60
        return "%02d:%02d:%02d" % (h, m, s)

    def day0_timer_pct():
        if store.day0_timer_total <= 0:
            return 0.0
        return max(0.0, min(1.0, day0_timer_remaining() / store.day0_timer_total))


# =============================================================
# ÉCRAN TIMER — COUNTDOWN OVERLAY
# Réutilisable : day0_timer_init(...) puis show screen day0_countdown_overlay
# =============================================================

screen day0_countdown_overlay():
    zorder 140

    # Variables locales
    default _tick       = 0
    default _flash_id   = day0_timer_flash_id
    default _do_flash   = False

    # Rafraîchissement toutes les 0.5 s
    timer 0.5 repeat True action SetScreenVariable("_tick", _tick + 1)

    # Détection mise à jour manuelle
    if day0_timer_flash_id != _flash_id:
        timer 0.0 action [
            SetScreenVariable("_flash_id", day0_timer_flash_id),
            SetScreenVariable("_do_flash", True),
        ]
    if _do_flash:
        timer 0.55 action SetScreenVariable("_do_flash", False)

    # Calculs live
    $ _t      = day0_timer_remaining()
    $ _ts     = day0_timer_fmt(_t)
    $ _pct    = day0_timer_pct()
    $ _expired = (_t <= 0 and day0_timer_active)
    $ _warn   = (_t < 1800 and not _expired)  # rouge sous 30 min
    $ _orange = (_t < 3600 and not _expired)  # orange sous 1h

    $ _bar_color = "#E03850" if _expired or _warn else ("#F0A835" if _orange else "#3BCC82")
    $ _txt_color = "#E03850" if _expired else ("#F0A835" if _orange or _warn else "#5CD3FF")

    # Marqueur expiration : désactive le timer
    if _expired:
        timer 0.05 action SetVariable("day0_timer_active", False)

    # ── Panneau ──────────────────────────────────────────────
    frame:
        xalign 0.99
        yalign 0.04
        xsize  460
        background Frame(Solid("#06090DDD"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 460
            ysize 88

            # Bande gauche colorée
            add Solid(_bar_color) xpos 0 ypos 0 xsize 4 ysize 88

            # Barre de progression en fond
            add Solid("#FFFFFF0A") xpos 4 ypos 0 xsize 456 ysize 88
            if _pct > 0:
                add Solid(_bar_color + "28") xpos 4 ypos 0 xsize int(456 * _pct) ysize 88

            # Ligne déco supérieure
            add Solid(_bar_color + "55") xpos 4 ypos 0 xsize 456 ysize 1

            # Label
            text "ACHEMINEMENT — CONCLAVE":
                xpos 18 ypos 10
                size 13
                color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            # Timer principal
            if _do_flash:
                text _ts at d0_flash_update:
                    xpos 18 ypos 28
                    size 34
                    color _txt_color
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
            elif _expired:
                text "DÉLAI EXPIRÉ" at d0_blink_fast:
                    xpos 18 ypos 28
                    size 28
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
            else:
                text _ts:
                    xpos 18 ypos 28
                    size 34
                    color _txt_color
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True

            # Sous-label
            text "LIMITE : 22:00  ▸  RESTANT":
                xpos 18 ypos 66
                size 13
                color "#3A5A6A"
                font "fonts/Rajdhani-SemiBold.ttf"

            # Icône alerte si urgent
            if _warn or _expired:
                text "⚠":
                    xpos 410 ypos 26
                    size 28
                    color _bar_color
                    at d0_blink_fast

            # Barre progression fine (bas du panneau)
            add Solid("#1A2D3E") xpos 4 ypos 86 xsize 456 ysize 2
            if _pct > 0:
                add Solid(_bar_color) xpos 4 ypos 86 xsize int(456 * _pct) ysize 2


# =============================================================
# ÉCRAN SCANNER BADGE
# =============================================================

screen day0_security_badge_scan():
    modal True
    zorder 250

    default scan_phase = 0  # 0=attente  1=scan  2=validé

    # Fond
    add Solid("#030609F0")

    # ── Cadre terminal ──────────────────────────────────────
    frame:
        xalign 0.5
        yalign 0.5
        xsize  1080
        ysize  640
        background Solid("#06090D")
        padding (0, 0)

        fixed:
            xsize 1080
            ysize 640

            # Bande top
            add Solid("#0D1520") xpos 0 ypos 0 xsize 1080 ysize 52
            add Solid("#1A2D3E") xpos 0 ypos 52 xsize 1080 ysize 1

            # Titre terminal
            text "PORTIQUE DE SÉCURITÉ — DISTRICT HARMONIE":
                xpos 22 ypos 14
                size 18
                color "#5CD3FF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            # Status indicator
            text "● ACTIF":
                xpos 900 ypos 18
                size 14
                color "#3BCC82"
                font "fonts/Rajdhani-SemiBold.ttf"
                at d0_blink

            text "LECTEUR CIVIL / IDENTIFICATION OBLIGATOIRE":
                xpos 22 ypos 62
                size 13
                color "#3A5A6A"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1

            # ── Zone gauche : badge draggable ────────────────
            if scan_phase == 0:
                timer 0.05 repeat True action If(
                    day0_badge_dropped,
                    [Play("sound", sfx_beep), SetScreenVariable("scan_phase", 1), SetVariable("day0_badge_dropped", False)]
                )

            # Instruction
            if scan_phase == 0:
                frame:
                    xpos 40 ypos 80
                    xsize 560 ysize 530
                    background Solid("#08111A")
                    padding (0, 0)

                    fixed:
                        xsize 560 ysize 530

                        # Grille déco
                        add Solid("#0D1A24") xpos 0 ypos 0 xsize 560 ysize 530

                        text "POSER LE BADGE SUR LA ZONE DE LECTURE":
                            xalign 0.5 ypos 28
                            size 15
                            color "#3A5A6A"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 1

                        text "Chaque entrée est enregistrée.":
                            xalign 0.5 ypos 54
                            size 14
                            color "#283C4A"
                            font "fonts/Rajdhani-SemiBold.ttf"

                        # Zone drop visible
                        add Solid("#0F1E2B") xpos 140 ypos 108 xsize 280 ysize 300
                        add Solid("#1A2D3E") xpos 140 ypos 108 xsize 280 ysize 1
                        add Solid("#1A2D3E") xpos 140 ypos 407 xsize 280 ysize 1
                        add Solid("#1A2D3E") xpos 140 ypos 108 xsize 1 ysize 300
                        add Solid("#1A2D3E") xpos 419 ypos 108 xsize 1 ysize 300

                        text "↓  ZONE DE LECTURE  ↓":
                            xalign 0.5 ypos 246
                            size 14
                            color "#1A3040"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            at d0_blink


            else:
                # Badge statique après scan
                frame:
                    xpos 40 ypos 80
                    xsize 560 ysize 530
                    background Solid("#08111A")
                    padding (0, 0)
                    fixed:
                        xsize 560 ysize 530

                        text "BADGE ENREGISTRÉ":
                            xalign 0.5 ypos 28
                            size 15
                            color ("#3BCC82" if scan_phase == 2 else "#F0A835")
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 1

                        # Badge rendu statique
                        fixed:
                            xpos 94 ypos 165
                            xsize 372 ysize 218

                            add Solid("#0D1B28") xpos 0 ypos 0 xsize 372 ysize 218
                            add Solid("#3BCC8244" if scan_phase == 2 else "#F0A83544") xpos 0 ypos 0 xsize 372 ysize 1
                            add Solid("#3BCC8244" if scan_phase == 2 else "#F0A83544") xpos 0 ypos 217 xsize 372 ysize 1
                            add Solid("#3BCC8244" if scan_phase == 2 else "#F0A83544") xpos 0 ypos 0 xsize 1 ysize 218
                            add Solid("#3BCC8244" if scan_phase == 2 else "#F0A83544") xpos 371 ypos 0 xsize 1 ysize 218

                            add Solid("#5CD3FF18") xpos 0 ypos 0 xsize 372 ysize 8
                            add Solid("#06101A") xpos 14 ypos 20 xsize 88 ysize 112
                            add Solid("#0D1E2C") xpos 16 ypos 22 xsize 84 ysize 108
                            add Solid("#1A3040") xpos 30 ypos 52 xsize 56 ysize 56
                            add Solid("#1A3040") xpos 44 ypos 28 xsize 28 ysize 28
                            add Solid("#0D1E2C") xpos 28 ypos 68 xsize 60 ysize 6

                            text "DISTRICT HARMONIE":
                                xpos 116 ypos 22 size 11 color "#5CD3FF"
                                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                            text "NOAM":
                                xpos 116 ypos 58 size 26 color "#D6E8F0"
                                font "fonts/Rajdhani-SemiBold.ttf" bold True
                            text "Médiateur civil · Secteur 3":
                                xpos 116 ypos 90 size 13 color "#7A98A8"
                                font "fonts/Rajdhani-SemiBold.ttf"

                            add Solid("#030609") xpos 0 ypos 148 xsize 372 ysize 22

            # ── Zone droite : terminal lecteur ───────────────
            frame:
                xpos 600 ypos 80
                xsize 450 ysize 530
                background Solid("#08111A")
                padding (0, 0)

                fixed:
                    xsize 450 ysize 530

                    # Titre zone
                    text "LECTEUR BIOMÉTRIQUE":
                        xpos 18 ypos 16
                        size 13
                        color "#3A5A6A"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        kerning 1

                    # Fenêtre scan
                    add Solid("#030609") xpos 108 ypos 52 xsize 234 ysize 310
                    add Solid("#1A2D3E") xpos 108 ypos 52 xsize 234 ysize 1
                    add Solid("#1A2D3E") xpos 108 ypos 361 xsize 234 ysize 1
                    add Solid("#1A2D3E") xpos 108 ypos 52 xsize 1 ysize 310
                    add Solid("#1A2D3E") xpos 341 ypos 52 xsize 1 ysize 310

                    # Coins scanning visuels
                    add Solid("#5CD3FF") xpos 108 ypos 52 xsize 16 ysize 3
                    add Solid("#5CD3FF") xpos 108 ypos 52 xsize 3 ysize 16
                    add Solid("#5CD3FF") xpos 325 ypos 52 xsize 16 ysize 3
                    add Solid("#5CD3FF") xpos 339 ypos 52 xsize 3 ysize 16
                    add Solid("#5CD3FF") xpos 108 ypos 359 xsize 16 ysize 3
                    add Solid("#5CD3FF") xpos 108 ypos 344 xsize 3 ysize 16
                    add Solid("#5CD3FF") xpos 325 ypos 359 xsize 16 ysize 3
                    add Solid("#5CD3FF") xpos 339 ypos 344 xsize 3 ysize 16

                    if scan_phase == 0:
                        # Attente — zone orange pulsante
                        add Solid("#F0A83520") xpos 109 ypos 53 xsize 232 ysize 308 at d0_blink

                        text "EN ATTENTE":
                            xalign 0.5 ypos 194
                            size 16
                            color "#F0A835"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2
                            at d0_blink

                        # Icône loupe
                        text "◉":
                            xalign 0.5 ypos 140
                            size 42
                            color "#1A2D3E"
                            at d0_blink

                    elif scan_phase == 1:
                        # Scan actif
                        add Solid("#F0A83514") xpos 109 ypos 53 xsize 232 ysize 308

                        # Ligne de scan qui descend
                        add Solid("#F0A835CC") xpos 109 ypos 53 xsize 232 ysize 3 at d0_sweep
                        add Solid("#F0A83544") xpos 109 ypos 53 xsize 232 ysize 24 at d0_sweep

                        text "ANALYSE EN COURS":
                            xalign 0.5 ypos 190
                            size 16
                            color "#F0A835"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2

                        # Barre de progression fictive animée
                        add Solid("#1A2D3E") xpos 50 ypos 390 xsize 350 ysize 10
                        timer 1.15 action [Play("sound", sfx_beep), SetScreenVariable("scan_phase", 2)]

                    else:
                        # Validé
                        add Solid("#3BCC8218") xpos 109 ypos 53 xsize 232 ysize 308

                        text "✓":
                            xalign 0.5 ypos 130
                            size 68
                            color "#3BCC82"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            at d0_appear

                        text "ACCÈS AUTORISÉ":
                            xalign 0.5 ypos 232
                            size 18
                            color "#3BCC82"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2
                            at d0_appear

                        add Solid("#3BCC8255") xpos 109 ypos 360 xsize 232 ysize 2
                        timer 0.9 action Return(True)

                    # Statut texte bas
                    if scan_phase == 0:
                        text "Présenter le badge dans la zone.":
                            xpos 18 ypos 400 size 15 color "#7A98A8"
                            font "fonts/Rajdhani-SemiBold.ttf"
                        text "Comparaison profil civil en cours.":
                            xpos 18 ypos 422 size 13 color "#3A5A6A"
                            font "fonts/Rajdhani-SemiBold.ttf"
                    elif scan_phase == 1:
                        text "VALIDATION DE L'IDENTITÉ...":
                            xpos 18 ypos 400 size 15 color "#F0A835"
                            font "fonts/Rajdhani-SemiBold.ttf"
                        text "Comparaison du profil avec les autorisations locales.":
                            xpos 18 ypos 422 size 13 color "#3A5A6A"
                            font "fonts/Rajdhani-SemiBold.ttf" xmaximum 410
                    else:
                        text "PASSAGE CONFIRMÉ":
                            xpos 18 ypos 400 size 15 color "#3BCC82"
                            font "fonts/Rajdhani-SemiBold.ttf"
                        text "Comportement conforme. Identité reconnue.":
                            xpos 18 ypos 422 size 13 color "#3A5A6A"
                            font "fonts/Rajdhani-SemiBold.ttf"

                    # Numéro de transaction
                    text "TX: HRM-" + ("------" if scan_phase == 0 else "004712"):
                        xpos 18 ypos 494
                        size 12
                        color "#1A2D3E"
                        font "fonts/Rajdhani-SemiBold.ttf"

            # Drag badge au-dessus du lecteur
            if scan_phase == 0:
                draggroup:
                    xsize 1080
                    ysize 640

                    drag:
                        drag_name "day0_badge_drag"
                        xpos 134
                        ypos 245
                        xsize 372
                        ysize 218
                        draggable True
                        droppable False
                        dragged day0_badge_dragged

                        # Carte badge inline
                        fixed:
                            xsize 372
                            ysize 218

                            # Corps carte
                            add Solid("#0D1B28") xpos 0 ypos 0 xsize 372 ysize 218
                            add Solid("#1A2D3E") xpos 0 ypos 0 xsize 372 ysize 1
                            add Solid("#1A2D3E") xpos 0 ypos 217 xsize 372 ysize 1
                            add Solid("#1A2D3E") xpos 0 ypos 0 xsize 1 ysize 218
                            add Solid("#1A2D3E") xpos 371 ypos 0 xsize 1 ysize 218

                            # Bande holographique top
                            add Solid("#5CD3FF18") xpos 0 ypos 0 xsize 372 ysize 8
                            add Solid("#5CD3FF08") xpos 0 ypos 8 xsize 372 ysize 4

                            # Zone photo
                            add Solid("#06101A") xpos 14 ypos 20 xsize 88 ysize 112
                            add Solid("#0D1E2C") xpos 16 ypos 22 xsize 84 ysize 108
                            # Silhouette (pur code)
                            add Solid("#1A3040") xpos 30 ypos 52 xsize 56 ysize 56  # corps
                            add Solid("#1A3040") xpos 44 ypos 28 xsize 28 ysize 28  # tête
                            add Solid("#0D1E2C") xpos 28 ypos 68 xsize 60 ysize 6   # séparateur

                            # Infos texte
                            text "DISTRICT HARMONIE":
                                xpos 116 ypos 22
                                size 11
                                color "#5CD3FF"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 2

                            text "IDENTIFIANT CIVIL":
                                xpos 116 ypos 40
                                size 10
                                color "#3A5A6A"
                                font "fonts/Rajdhani-SemiBold.ttf"

                            text "NOAM":
                                xpos 116 ypos 58
                                size 26
                                color "#D6E8F0"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                bold True

                            text "Médiateur civil · Secteur 3":
                                xpos 116 ypos 90
                                size 13
                                color "#7A98A8"
                                font "fonts/Rajdhani-SemiBold.ttf"

                            text "REF: HRM-003-0847-N":
                                xpos 116 ypos 110
                                size 11
                                color "#3A5A6A"
                                font "fonts/Rajdhani-SemiBold.ttf"

                            # Barre magnétique bas
                            add Solid("#030609") xpos 0 ypos 148 xsize 372 ysize 22
                            add Solid("#0A1520") xpos 0 ypos 170 xsize 372 ysize 18

                            # Puce chip
                            add Solid("#F0A83540") xpos 14 ypos 148 xsize 32 ysize 22
                            add Solid("#F0A835") xpos 14 ypos 150 xsize 32 ysize 2
                            add Solid("#F0A835") xpos 14 ypos 168 xsize 32 ysize 2

                            # Code barres déco
                            for _bx in range(0, 280, 4):
                                add Solid("#FFFFFF08") xpos (80 + _bx) ypos 170 xsize 2 ysize 16

                            # Coin DRAG
                            text "▶  GLISSER":
                                xpos 116 ypos 192
                                size 12
                                color "#5CD3FF"
                                font "fonts/Rajdhani-SemiBold.ttf"
                                at d0_blink

                    drag:
                        drag_name "day0_scanner_drop"
                        xpos 708
                        ypos 132
                        xsize 234
                        ysize 310
                        draggable False
                        droppable True
                        add Solid("#00000000")


            # ── Bas de l'écran ────────────────────────────────
            add Solid("#0D1520") xpos 0 ypos 596 xsize 1080 ysize 44
            add Solid("#1A2D3E") xpos 0 ypos 596 xsize 1080 ysize 1

            text "KAMI INFRASTRUCTURE · CONTRÔLE CIVIL AUTOMATISÉ · TOUTE ENTRÉE EST ENREGISTRÉE":
                xalign 0.5 ypos 608
                size 12
                color "#1A2D3E"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1


# =============================================================
# ÉCRAN TÉLÉPHONE
# =============================================================

screen day0_phone_override():
    modal True
    zorder 250

    default attempts = 0

    # Fond sombre
    add Solid("#020406F0")

    # ── Corps du téléphone ───────────────────────────────────
    frame:
        xalign 0.5
        yalign 0.5
        xsize  400
        ysize  780
        background Solid("#0A0F14")
        padding (0, 0)

        fixed:
            xsize 400 ysize 780

            # ── Coque extérieure ──
            add Solid("#141C24") xpos 0 ypos 0 xsize 400 ysize 780
            add Solid("#1A2630") xpos 0 ypos 0 xsize 400 ysize 1    # top
            add Solid("#1A2630") xpos 0 ypos 779 xsize 400 ysize 1  # bottom
            add Solid("#1A2630") xpos 0 ypos 0 xsize 1 ysize 780    # left
            add Solid("#1A2630") xpos 399 ypos 0 xsize 1 ysize 780  # right

            # Encoche (notch) centrée
            add Solid("#0A0F14") xpos 140 ypos 0 xsize 120 ysize 26
            add Solid("#0A0F14") xpos 162 ypos 0 xsize 76 ysize 30
            # Caméra frontale
            add Solid("#0D1520") xpos 182 ypos 8 xsize 12 ysize 12
            add Solid("#1A2D3E44") xpos 183 ypos 9 xsize 10 ysize 10
            # Haut-parleur
            add Solid("#0D1520") xpos 152 ypos 14 xsize 26 ysize 5

            # ── Écran ──
            add Solid("#060C12") xpos 14 ypos 30 xsize 372 ysize 680

            # ── Barre de statut ──
            add Solid("#08111A") xpos 14 ypos 30 xsize 372 ysize 30

            text "09:47":
                xpos 24 ypos 35
                size 13
                color "#9BBCCC"
                font "fonts/Rajdhani-SemiBold.ttf"
                bold True

            # Signal barres
            for _si in range(4):
                add Solid("#9BBCCC44" if _si >= (2 if attempts > 0 else 4) else "#9BBCCC"):
                    xpos (330 + _si * 8) ypos (42 - _si * 3)
                    xsize 5
                    ysize (6 + _si * 3)

            # Batterie
            add Solid("#9BBCCC33") xpos 360 ypos 37 xsize 20 ysize 10
            add Solid("#9BBCCC") xpos 361 ypos 38 xsize (14 if attempts < 3 else 4) ysize 8
            add Solid("#9BBCCC") xpos 380 ypos 41 xsize 3 ysize 4

            # ── Contenu dynamique selon attempts ──────────────

            if attempts == 0:
                # Écran verrouillé
                text "🔒":
                    xalign 0.5 ypos 160
                    size 52
                    color "#D6E8F0"

                text "ÉCRAN VERROUILLÉ":
                    xalign 0.5 ypos 240
                    size 20
                    color "#D6E8F0"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

                text "Glisser vers le haut pour déverrouiller":
                    xalign 0.5 ypos 278
                    size 14
                    color "#4A6878"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    at d0_blink

                # Horloge grande
                text "09:47":
                    xalign 0.5 ypos 310
                    size 58
                    color "#CCDDE8"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True

                text "VENDREDI — JOUR 0":
                    xalign 0.5 ypos 380
                    size 15
                    color "#3A5A6A"
                    font "fonts/Rajdhani-SemiBold.ttf"

                # Ligne notif
                add Solid("#0D1A24") xpos 30 ypos 430 xsize 340 ysize 60
                add Solid("#E0385044") xpos 30 ypos 430 xsize 4 ysize 60
                text "Signal : --   •   Réseau : indisponible":
                    xpos 44 ypos 442
                    size 13
                    color "#7A98A8"
                    font "fonts/Rajdhani-SemiBold.ttf"
                text "Recherche de réseau...":
                    xpos 44 ypos 462
                    size 12
                    color "#3A5A6A"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    at d0_blink

            elif attempts == 1:
                text "⚠":
                    xalign 0.5 ypos 160
                    size 52
                    color "#F0A835"

                text "AUCUN RÉSEAU":
                    xalign 0.5 ypos 244
                    size 24
                    color "#F0A835"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

                text "Recherche des relais civils en cours...":
                    xalign 0.5 ypos 286
                    size 15
                    color "#7A98A8"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    at d0_blink

                add Solid("#0D1A24") xpos 30 ypos 330 xsize 340 ysize 1

                text "ERR_NET_001 · Aucun opérateur disponible":
                    xpos 30 ypos 346
                    size 13
                    color "#3A5A6A"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "Les services de communication\nsont temporairement indisponibles.":
                    xalign 0.5 ypos 390
                    size 15
                    color "#9BBCCC"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    text_align 0.5

            elif attempts == 2:
                text "✗":
                    xalign 0.5 ypos 148
                    size 64
                    color "#E03850"

                text "APPEL REFUSÉ":
                    xalign 0.5 ypos 240
                    size 26
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2

                text "Appels d'urgence indisponibles.":
                    xalign 0.5 ypos 282
                    size 16
                    color "#B0C8D4"
                    font "fonts/Rajdhani-SemiBold.ttf"

                add Solid("#1A0A0D") xpos 30 ypos 320 xsize 340 ysize 70
                add Solid("#E03850") xpos 30 ypos 320 xsize 2 ysize 70

                text "Code : INFRASTRUCTURE NON SOUVERAINE":
                    xpos 42 ypos 332
                    size 12
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 1

                text "Tous les canaux de communication\ndépendent désormais de KAMI.":
                    xpos 42 ypos 356
                    size 14
                    color "#7A98A8"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "ERR_NET_403 · ACCÈS BLOQUÉ":
                    xalign 0.5 ypos 430
                    size 13
                    color "#3A2030"
                    font "fonts/Rajdhani-SemiBold.ttf"

            elif attempts == 3:
                text "MESSAGE NON ENVOYÉ":
                    xalign 0.5 ypos 158
                    size 22
                    color "#E03850"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 1

                add Solid("#1A0A0D") xpos 30 ypos 202 xsize 340 ysize 130
                add Solid("#E03850") xpos 30 ypos 202 xsize 1 ysize 130
                add Solid("#E0385022") xpos 31 ypos 202 xsize 339 ysize 130

                text "KAMI":
                    xpos 46 ypos 214
                    size 16
                    color "#E08080"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True

                add Solid("#2A1018") xpos 46 ypos 232 xsize 308 ysize 1

                text "Merci de cesser toute tentative de\nréinitialisation du réseau.\nCette conversation est enregistrée.":
                    xpos 46 ypos 244
                    size 14
                    color "#C0A0A0"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "Le réseau de communication\nne vous appartient plus.":
                    xalign 0.5 ypos 370
                    size 16
                    color "#B0C8D4"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    text_align 0.5

                text "• 1 message non distribué":
                    xalign 0.5 ypos 440
                    size 13
                    color "#E0385088"
                    font "fonts/Rajdhani-SemiBold.ttf"

            else:
                # Prise de contrôle totale
                add Solid("#0A0500") xpos 14 ypos 30 xsize 372 ysize 680
                add Solid("#F0A83508") xpos 14 ypos 30 xsize 372 ysize 680 at d0_blink_fast

                # Scanlines effet glitch
                for _gl in range(0, 680, 24):
                    add Solid("#F0A83510") xpos 14 ypos (30 + _gl) xsize 372 ysize 1

                text "CONTRÔLE DISTANT ACTIF":
                    xalign 0.5 ypos 200
                    size 20
                    color "#F0A835"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 2
                    bold True

                text "Verrouillage de l'interface.":
                    xalign 0.5 ypos 242
                    size 16
                    color "#C0A070"
                    font "fonts/Rajdhani-SemiBold.ttf"

                text "KAMI":
                    xalign 0.5 ypos 300
                    size 38
                    color "#F0A835"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
                    at d0_blink_fast

                text "Cet appareil est désormais\nsous surveillance directe.":
                    xalign 0.5 ypos 360
                    size 15
                    color "#806040"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    text_align 0.5

                timer 1.0 action Return(True)

            # ── Boutons d'action ──────────────────────────────
            add Solid("#08111A") xpos 14 ypos 710 xsize 372 ysize 60

            hbox:
                xpos 14 ypos 716
                xsize 372
                spacing 0

                if attempts < 4:
                    textbutton "Rallumer":
                        xsize 124 ysize 48
                        background Solid("#0D1A24")
                        hover_background Solid("#1A2D40")
                        text_size 15
                        text_color "#7ABDD0"
                        text_hover_color "#D6E8F0"
                        text_font "fonts/Rajdhani-SemiBold.ttf"
                        text_xalign 0.5
                        action [Play("sound", sfx_gresillement), SetScreenVariable("attempts", attempts + 1)]

                    add Solid("#1A2630") xpos 0 ypos 4 xsize 1 ysize 40

                    textbutton "Appeler":
                        xsize 124 ysize 48
                        background Solid("#0D1A24")
                        hover_background Solid("#1A2D40")
                        text_size 15
                        text_color "#7ABDD0"
                        text_hover_color "#D6E8F0"
                        text_font "fonts/Rajdhani-SemiBold.ttf"
                        text_xalign 0.5
                        action [Play("sound", sfx_beep), SetScreenVariable("attempts", attempts + 1)]

                    add Solid("#1A2630") xpos 0 ypos 4 xsize 1 ysize 40

                    textbutton "Envoyer":
                        xsize 124 ysize 48
                        background Solid("#0D1A24")
                        hover_background Solid("#1A2D40")
                        text_size 15
                        text_color "#7ABDD0"
                        text_hover_color "#D6E8F0"
                        text_font "fonts/Rajdhani-SemiBold.ttf"
                        text_xalign 0.5
                        action [Play("sound", sfx_gresillement), SetScreenVariable("attempts", attempts + 1)]
                else:
                    text "···":
                        xalign 0.5 ypos 8
                        size 28
                        color "#3A5A6A"
                        at d0_blink

            # Indicateur home
            add Solid("#1A2630") xpos 160 ypos 768 xsize 80 ysize 4


# =============================================================
# ÉCRAN COMMANDEMENTS (registre)
# =============================================================

screen day0_commandments_registry():
    modal True
    zorder 250

    default page = 0

    $ _cmd_title = day0_commandment_pages[page][0]
    $ _cmd_text  = day0_commandment_pages[page][1]
    $ _cmd_label = "%d / %d" % (page + 1, len(day0_commandment_pages))

    add Solid("#04060AEE")

    frame:
        xalign 0.5
        yalign 0.5
        xsize  1200
        ysize  740
        background Solid("#0A0D10")
        padding (0, 0)

        fixed:
            xsize 1200 ysize 740

            # ── Page gauche — sommaire / contexte ────────────
            add Solid("#E8E2D4") xpos 0 ypos 0 xsize 530 ysize 700
            add Solid("#D8D0BE") xpos 0 ypos 700 xsize 530 ysize 40

            # Titre page gauche
            text "REGISTRE DES COMMANDEMENTS":
                xpos 32 ypos 28
                size 20
                color "#1A1410"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 3
                bold True

            add Solid("#1A1410") xpos 32 ypos 56 xsize 460 ysize 1

            text "District HARMONIE · Consultation surveillée":
                xpos 32 ypos 66
                size 14
                color "#5A5048"
                font "fonts/Rajdhani-SemiBold.ttf"

            add Solid("#1A1410") xpos 32 ypos 90 xsize 460 ysize 1

            # Liste des commandements
            vbox:
                xpos 32 ypos 108
                spacing 0

                for _pi, (_pnum, _ptxt) in enumerate(day0_commandment_pages):
                    frame:
                        xsize 462
                        ysize 48
                        background Solid("#D0C8B6" if _pi == page else "#00000000")
                        padding (12, 0)

                        hbox:
                            spacing 16

                            text _pnum:
                                size 15
                                color ("#5CD3FF" if _pi == page else "#6A5A48")
                                font "fonts/Rajdhani-SemiBold.ttf"
                                bold True
                                xminimum 24

                            text "Commandement %s" % _pnum:
                                size 14
                                color ("#1A1410" if _pi == page else "#5A5048")
                                font "fonts/Rajdhani-SemiBold.ttf"

            text "KAMI ARCHIVE · REF: CMD-HRM-01":
                xpos 32 ypos 658
                size 12
                color "#8A7A68"
                font "fonts/Rajdhani-SemiBold.ttf"

            text _cmd_label:
                xpos 32 ypos 716
                size 14
                color "#5A5048"
                font "fonts/Rajdhani-SemiBold.ttf"

            # ── Séparateur ────────────────────────────────────
            add Solid("#1A1410") xpos 530 ypos 0 xsize 1 ysize 740
            add Solid("#0A0D10") xpos 531 ypos 0 xsize 8 ysize 740

            # ── Page droite — contenu du commandement ─────────
            add Solid("#F0EAD8") xpos 539 ypos 0 xsize 661 ysize 700
            add Solid("#D8D0BE") xpos 539 ypos 700 xsize 661 ysize 40

            # Numéro du commandement (grand)
            text "COMMANDEMENT":
                xpos 562 ypos 28
                size 14
                color "#8A7A68"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 3

            text _cmd_title:
                xpos 562 ypos 50
                size 64
                color "#1A1410"
                font "fonts/Rajdhani-SemiBold.ttf"
                bold True

            add Solid("#1A1410") xpos 562 ypos 128 xsize 600 ysize 2

            # Texte du commandement
            text _cmd_text:
                xpos 562 ypos 148
                xmaximum 596
                size 22
                color "#1A1410"
                font "fonts/Rajdhani-SemiBold.ttf"
                line_spacing 10

            # ── Boutons navigation ────────────────────────────
            hbox:
                xpos 562 ypos 716
                spacing 12

                textbutton "◀ Précédent":
                    xsize 170
                    ysize 36
                    sensitive (page > 0)
                    background Solid(("#1A1410" if page > 0 else "#C8C0AE"))
                    hover_background Solid(("#2A2418" if page > 0 else "#C8C0AE"))
                    text_size 15
                    text_color ("#E8E2D4" if page > 0 else "#8A7A68")
                    text_hover_color ("#FFFFFF" if page > 0 else "#8A7A68")
                    text_font "fonts/Rajdhani-SemiBold.ttf"
                    text_xalign 0.5
                    action [Play("sound", sfx_paper), SetScreenVariable("page", page - 1)]

                textbutton "Suivant ▶":
                    xsize 170 ysize 36
                    sensitive (page < len(day0_commandment_pages) - 1)
                    background Solid("#1A1410" if page < len(day0_commandment_pages) - 1 else "#C8C0AE")
                    hover_background Solid("#2A2418")
                    text_size 15
                    text_color ("#E8E2D4" if page < len(day0_commandment_pages) - 1 else "#8A7A68")
                    text_hover_color "#FFFFFF"
                    text_font "fonts/Rajdhani-SemiBold.ttf"
                    text_xalign 0.5
                    action [Play("sound", sfx_paper), SetScreenVariable("page", page + 1)]

                textbutton "Fermer":
                    xsize 120 ysize 36
                    background Solid("#2A3A4A")
                    hover_background Solid("#3A5060")
                    text_size 15
                    text_color "#7ABDD0"
                    text_hover_color "#D6E8F0"
                    text_font "fonts/Rajdhani-SemiBold.ttf"
                    text_xalign 0.5
                    action Return(True)


# =============================================================
# ÉCRAN SÉLECTION REPRÉSENTANTS
# =============================================================

screen day0_representative_selection():
    modal True
    zorder 250

    default tick   = 0
    default locked = False
    default seq    = 0  # pour id unique

    # Timer de défilement
    if not locked:
        timer 0.06 repeat True action [
            SetScreenVariable("tick", tick + 1),
            SetScreenVariable("seq", seq + 1),
        ]

    add Solid("#03060AF2")

    frame:
        xalign 0.5
        yalign 0.5
        xsize  1160
        ysize  700
        background Solid("#06090D")
        padding (0, 0)

        fixed:
            xsize 1160 ysize 700

            # ── Header ────────────────────────────────────────
            add Solid("#0D1520") xpos 0 ypos 0 xsize 1160 ysize 58
            add Solid("#5CD3FF") xpos 0 ypos 58 xsize 1160 ysize 1

            text "DISTRICT HARMONIE — SÉLECTION DES REPRÉSENTANTS":
                xpos 24 ypos 14
                size 20
                color "#D6E8F0"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2
                bold True

            if not locked:
                text "Cliquez pour arrêter la sélection":
                    xpos 24 ypos 38
                    size 14
                    color "#5CD3FF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    at d0_blink

            # ── Colonne gauche — liste noms ───────────────────
            add Solid("#08111A") xpos 24 ypos 74 xsize 480 ysize 590

            text "PROFILS EN ANALYSE":
                xpos 36 ypos 86
                size 13
                color "#3A5A6A"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            vbox:
                xpos 24 ypos 110
                spacing 4

                for _ni in range(7):
                    $ _name = day0_selection_names[(tick + _ni) % len(day0_selection_names)]
                    $ _is_winner = locked and (_ni == 2 or _ni == 4)
                    $ _is_losers = locked and not _is_winner

                    frame:
                        xsize 480
                        ysize 66
                        background Solid(
                            "#0A1E1488" if _is_winner else
                            ("#0D1520" if not locked else "#06090D")
                        )
                        padding (0, 0)

                        fixed:
                            xsize 480 ysize 66

                            # Barre gauche colorée
                            add Solid(
                                "#3BCC82" if _is_winner else
                                ("#1A2D3E" if not locked else "#1A0A0E")
                            ) xpos 0 ypos 0 xsize 3 ysize 66

                            # Numéro rang
                            text "%02d" % (_ni + 1):
                                xpos 12 ypos 22
                                size 14
                                color "#3A5A6A"
                                font "fonts/Rajdhani-SemiBold.ttf"

                            if locked and _is_winner:
                                text _name:
                                    xpos 46 ypos 16
                                    size 24
                                    color "#3BCC82"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    bold True

                                text "✓  SÉLECTIONNÉ":
                                    xpos 46 ypos 42
                                    size 12
                                    color "#3BCC8288"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    kerning 2

                            elif locked:
                                text "PROFIL ÉCARTÉ":
                                    xpos 46 ypos 22
                                    size 18
                                    color "#2A3A44"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                            else:
                                # Nom défilant
                                text _name:
                                    xpos 46 ypos 20
                                    size 22
                                    color "#D6E8F0"
                                    font "fonts/Rajdhani-SemiBold.ttf"

            # ── Colonne droite — critères analyse ─────────────
            add Solid("#08111A") xpos 524 ypos 74 xsize 612 ysize 590

            text "CRITÈRES D'ANALYSE":
                xpos 540 ypos 86
                size 13
                color "#3A5A6A"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            vbox:
                xpos 540 ypos 112
                spacing 18

                for _ci, _crit in enumerate(day0_selection_criteria):
                    $ _bar_w = int(((tick * (13 + _ci * 7) + _ci * 37) % 100) * 3.6)
                    $ _bar_w2 = max(40, _bar_w)

                    frame:
                        xsize 580
                        ysize 72
                        background Solid("#06090D")
                        padding (0, 0)

                        fixed:
                            xsize 580 ysize 72

                            text (_crit.upper()):
                                xpos 0 ypos 0
                                size 14
                                color ("#5CD3FF" if not locked else "#3A5A6A")
                                font "fonts/Rajdhani-SemiBold.ttf"
                                kerning 1

                            if not locked:
                                text "EN COURS…":
                                    xpos 400 ypos 2
                                    size 12
                                    color "#3A5A6A"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    at d0_blink
                            else:
                                text "VALIDÉ":
                                    xpos 400 ypos 2
                                    size 12
                                    color "#3BCC8288"
                                    font "fonts/Rajdhani-SemiBold.ttf"

                            # Fond barre
                            add Solid("#0D1520") xpos 0 ypos 26 xsize 580 ysize 18

                            # Barre animée (Ren'Py accepte l'ATL inline sur add)
                            add Solid("#1A3A6A") xpos 0 ypos 26 xsize _bar_w2 ysize 18

                            # Highlight top barre
                            add Solid("#5CD3FF22") xpos 0 ypos 26 xsize _bar_w2 ysize 4

                            # Valeur %
                            text "%d %%" % (_bar_w2 // 4):
                                xpos 0 ypos 48
                                size 12
                                color "#3A5A6A"
                                font "fonts/Rajdhani-SemiBold.ttf"

            # ── Résultat final (locked) ───────────────────────
            if locked:
                # Fond overlay révélation
                add Solid("#06090DEE") xpos 0 ypos 0 xsize 1160 ysize 700 at d0_appear

                # Cadre résultat
                frame:
                    xalign 0.5
                    yalign 0.5
                    xsize 700
                    ysize 320
                    background Solid("#06090D")
                    padding (0, 0)

                    fixed:
                        xsize 700 ysize 320

                        add Solid("#3BCC82") xpos 0 ypos 0 xsize 700 ysize 2
                        add Solid("#3BCC82") xpos 0 ypos 318 xsize 700 ysize 2
                        add Solid("#3BCC82") xpos 0 ypos 0 xsize 2 ysize 320
                        add Solid("#3BCC82") xpos 698 ypos 0 xsize 2 ysize 320
                        add Solid("#3BCC8218") xpos 2 ypos 2 xsize 696 ysize 316

                        text "SÉLECTION VALIDÉE":
                            xalign 0.5 ypos 28
                            size 18
                            color "#3BCC82"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 4
                            at d0_appear

                        add Solid("#3BCC8244") xpos 40 ypos 62 xsize 620 ysize 1

                        text "REPRÉSENTANTS — DISTRICT HARMONIE":
                            xalign 0.5 ypos 76
                            size 14
                            color "#3A5A6A"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            kerning 2

                        text "NOAM":
                            xalign 0.35 ypos 110
                            size 48
                            color "#D6E8F0"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            bold True
                            at d0_stamp_appear

                        text "LYSA":
                            xalign 0.65 ypos 110
                            size 48
                            color "#D6E8F0"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            bold True
                            at d0_stamp_appear

                        add Solid("#3BCC8244") xpos 40 ypos 180 xsize 620 ysize 1

                        text "Médiateur civil":
                            xalign 0.35 ypos 194
                            size 14
                            color "#3BCC8288"
                            font "fonts/Rajdhani-SemiBold.ttf"

                        text "Coordination logistique":
                            xalign 0.65 ypos 194
                            size 14
                            color "#3BCC8288"
                            font "fonts/Rajdhani-SemiBold.ttf"

                        text "Acheminement sous 6 heures — Sanctions applicables en cas de retard.":
                            xalign 0.5 ypos 240
                            size 13
                            color "#2A3A44"
                            font "fonts/Rajdhani-SemiBold.ttf"
                            xmaximum 620

                        add Solid("#3BCC8244") xpos 40 ypos 270 xsize 620 ysize 1

                        text "REF: HRM-SEL-0001":
                            xalign 0.5 ypos 286
                            size 12
                            color "#1A2D3E"
                            font "fonts/Rajdhani-SemiBold.ttf"

                timer 2.0 action Return(True)

            # ── Bouton plein écran pour verrouiller ───────────
            if not locked:
                button:
                    xpos 0 ypos 0
                    xsize 1160 ysize 700
                    background Solid("#00000000")
                    action [Play("sound", sfx_beep), SetScreenVariable("locked", True)]

            # ── Footer ────────────────────────────────────────
            add Solid("#0D1520") xpos 0 ypos 658 xsize 1160 ysize 42
            add Solid("#5CD3FF") xpos 0 ypos 658 xsize 1160 ysize 1
            text "KAMI — SÉLECTION AUTOMATISÉE · DISTRICT HARMONIE · SÉANCE 14-3":
                xalign 0.5 ypos 670
                size 12
                color "#1A2D3E"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1


# =============================================================
# FLASHBACK OVERLAY — Souvenir de Kami
# Usage :
#   show screen day0_flashback_overlay
#   with d0_flashback_entry
# ... flashback content ...
#   hide screen day0_flashback_overlay
#   with d0_flashback_exit
# =============================================================

# Transitions
define d0_flashback_entry = Fade(0.3, 0.2, 0.4, color="#1A0A30")
define d0_flashback_exit  = Dissolve(0.6)

screen day0_flashback_overlay():
    zorder 80  # sous le texte/dialogue mais au-dessus du décor

    # Vignette sombre aux coins
    add Solid("#0A0520EE") xpos 0 ypos 0 xsize config.screen_width ysize 40
    add Solid("#0A0520EE") xpos 0 ypos (config.screen_height - 40) xsize config.screen_width ysize 40
    add Solid("#0A0520BB") xpos 0 ypos 0 xsize 60 ysize config.screen_height
    add Solid("#0A0520BB") xpos (config.screen_width - 60) ypos 0 xsize 60 ysize config.screen_height

    # Teinture violacée légère (souvenir)
    add Solid("#180A3008") xpos 0 ypos 0 xsize config.screen_width ysize config.screen_height

    # Grain filmique (lignes horizontales fines)
    for _gy in range(0, config.screen_height, 6):
        add Solid("#FFFFFF06") xpos 0 ypos _gy xsize config.screen_width ysize 1

    # Label "SOUVENIR" en haut à gauche
    frame:
        xpos 24 ypos 22
        background Solid("#0A052088")
        padding (10, 4)

        hbox:
            spacing 8
            add Solid("#8855CC") xpos 0 ypos 6 xsize 3 ysize 12
            text "SOUVENIR":
                size 14
                color "#AA88CC"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 4

    # Ligne du temps — fin du flashback (indicateur discret)
    add Solid("#8855CC44") xpos 0 ypos (config.screen_height - 8) xsize config.screen_width ysize 2


# =============================================================
# TRANSFORMS UTILITAIRES pour le flashback (appelables depuis labels)
# =============================================================

transform d0_memory_tint:
    matrixcolor TintMatrix("#D0C0FF") * BrightnessMatrix(-0.05)
