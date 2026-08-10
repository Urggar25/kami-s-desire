# ============================================================
# MINI-JEU JOUR 6_0_1 — SIGNAL INSTABLE
# Objectif : maintenir le signal dans la zone verte centrale.
# Durée : 38 secondes.
# Contrôles :
# - Flèche gauche / Q / A : pousser le signal à gauche
# - Flèche droite / D : pousser le signal à droite
# - Espace / Entrée / clic bouton QTE : valider les éclats QTE
# ============================================================

default j601_signal_time_left = 38.0
default j601_signal_phase = 1
default j601_signal_cursor = 50.0
default j601_signal_velocity = 0.0
default j601_signal_green_time = 0.0
default j601_signal_errors = 0
default j601_signal_done = False
default j601_signal_success = False
default j601_signal_qte_active = False
default j601_signal_qte_time = 0.0
default j601_signal_qte_x = 0.5
default j601_signal_qte_y = 0.35
default j601_signal_next_qte = 8.0
default j601_signal_wave_dir = 1
default j601_signal_noise_line = "KAMI_SIGNAL::STABILITY_CHECK"
default j601_signal_warning = ""
default j601_signal_last_flash = 0.0
default j601_signal_display_line = ""

# NOTE: doublons j601_signal_get_zone / j601_signal_glitch_text supprimés
# (les définitions canoniques sont plus bas dans ce fichier).

init python:
    import random
    import math

    J601_SIGNAL_TOTAL_TIME = 38.0
    J601_SIGNAL_TICK = 0.05

    def j601_signal_reset():
        store.j601_signal_time_left = J601_SIGNAL_TOTAL_TIME
        store.j601_signal_phase = 1
        store.j601_signal_cursor = 50.0
        store.j601_signal_velocity = 0.0
        store.j601_signal_green_time = 0.0
        store.j601_signal_errors = 0
        store.j601_signal_done = False
        store.j601_signal_success = False
        store.j601_signal_qte_active = False
        store.j601_signal_qte_time = 0.0
        store.j601_signal_qte_x = 0.5
        store.j601_signal_qte_y = 0.35
        store.j601_signal_next_qte = 8.0
        store.j601_signal_wave_dir = random.choice([-1, 1])
        store.j601_signal_noise_line = "KAMI_SIGNAL::STABILITY_CHECK"
        store.j601_signal_warning = ""
        store.j601_signal_last_flash = 0.0

    def j601_signal_in_green():
        return 30.0 <= store.j601_signal_cursor <= 70.0

    def j601_signal_phase_update(elapsed):
        if elapsed < 10.0:
            store.j601_signal_phase = 1
        elif elapsed < 30.0:
            store.j601_signal_phase = 2
        else:
            store.j601_signal_phase = 3

    def j601_signal_nudge(amount):
        if store.j601_signal_done:
            return
        # Micro-ajustement volontairement limité : il faut tapoter, pas bourriner.
        if store.j601_signal_phase == 1:
            multiplier = 0.75
        elif store.j601_signal_phase == 2:
            multiplier = 0.95
        else:
            multiplier = 1.10
        store.j601_signal_velocity += amount * multiplier
        store.j601_signal_velocity = max(-9.0, min(9.0, store.j601_signal_velocity))

    def j601_signal_qte_hit():
        if store.j601_signal_done:
            return
        if store.j601_signal_qte_active:
            store.j601_signal_qte_active = False
            store.j601_signal_qte_time = 0.0
            store.j601_signal_warning = "RECALIBRAGE"
            store.j601_signal_last_flash = 0.20
            # Réinitialisation temporaire : ramène vers le centre et calme la vitesse.
            store.j601_signal_cursor = (store.j601_signal_cursor * 0.45) + 27.5
            store.j601_signal_velocity *= 0.15
        else:
            # Appuyer dans le vide crée une petite erreur.
            store.j601_signal_velocity += random.choice([-1.5, 1.5])

    def j601_signal_spawn_qte(elapsed):
        store.j601_signal_qte_active = True
        store.j601_signal_qte_time = 0.95 if store.j601_signal_phase == 2 else 0.75
        store.j601_signal_qte_x = random.uniform(0.38, 0.62)
        store.j601_signal_qte_y = random.uniform(0.25, 0.50)
        store.j601_signal_next_qte = elapsed + random.uniform(4.0, 6.0 if store.j601_signal_phase == 2 else 3.2)
        store.j601_signal_warning = "PIXEL FRACTURE"

    def j601_signal_tick():
        if store.j601_signal_done:
            return

        store.j601_signal_time_left = max(0.0, store.j601_signal_time_left - J601_SIGNAL_TICK)
        elapsed = J601_SIGNAL_TOTAL_TIME - store.j601_signal_time_left
        j601_signal_phase_update(elapsed)

        base_line = j601_signal_update_line(elapsed)
        store.j601_signal_display_line = j601_signal_glitch_text(base_line)

        if store.j601_signal_phase == 1:
            base_pull = random.uniform(-0.14, 0.14)
            friction = 0.90
        elif store.j601_signal_phase == 2:
            base_pull = random.uniform(-0.34, 0.34)
            friction = 0.93
        else:
            base_pull = random.uniform(-0.55, 0.55)
            friction = 0.96

        if store.j601_signal_phase >= 2:
            wave_power = 0.20 if store.j601_signal_phase == 2 else 0.42
            wave = math.sin(elapsed * (2.2 if store.j601_signal_phase == 2 else 4.6)) * wave_power
            store.j601_signal_velocity += wave * store.j601_signal_wave_dir

        spike_chance = 0.018 if store.j601_signal_phase == 2 else 0.055 if store.j601_signal_phase == 3 else 0.004
        if random.random() < spike_chance:
            spike = random.choice([-1, 1]) * random.uniform(2.8, 6.4)
            store.j601_signal_velocity += spike
            store.j601_signal_warning = "SPIKE"

        if store.j601_signal_phase == 3 and random.random() < 0.075:
            store.j601_signal_velocity += random.choice([-1, 1]) * random.uniform(3.0, 7.5)
            store.j601_signal_last_flash = 0.15
            store.j601_signal_warning = "DESYNCHRONISATION"

        store.j601_signal_velocity += base_pull
        store.j601_signal_velocity *= friction
        store.j601_signal_velocity = max(-12.0, min(12.0, store.j601_signal_velocity))
        store.j601_signal_cursor += store.j601_signal_velocity * J601_SIGNAL_TICK * 10.0

        if store.j601_signal_cursor < 0.0:
            store.j601_signal_cursor = 0.0
            store.j601_signal_velocity = abs(store.j601_signal_velocity) * 0.65
            store.j601_signal_errors += 1
        elif store.j601_signal_cursor > 100.0:
            store.j601_signal_cursor = 100.0
            store.j601_signal_velocity = -abs(store.j601_signal_velocity) * 0.65
            store.j601_signal_errors += 1

        if j601_signal_in_green():
            store.j601_signal_green_time += J601_SIGNAL_TICK
            if store.j601_signal_warning not in ("RECALIBRAGE",):
                store.j601_signal_warning = "STABLE"
        else:
            if store.j601_signal_cursor < 15.0 or store.j601_signal_cursor > 85.0:
                store.j601_signal_errors += 0.035
                store.j601_signal_warning = "CRITIQUE"
            else:
                store.j601_signal_warning = "INSTABLE"

        if store.j601_signal_phase >= 2 and (not store.j601_signal_qte_active) and elapsed >= store.j601_signal_next_qte:
            j601_signal_spawn_qte(elapsed)

        if store.j601_signal_qte_active:
            store.j601_signal_qte_time -= J601_SIGNAL_TICK
            if store.j601_signal_qte_time <= 0.0:
                store.j601_signal_qte_active = False
                store.j601_signal_qte_time = 0.0
                store.j601_signal_errors += 1
                store.j601_signal_velocity += random.choice([-1, 1]) * 5.0
                store.j601_signal_warning = "QTE MANQUÉ"

        if store.j601_signal_last_flash > 0.0:
            store.j601_signal_last_flash = max(0.0, store.j601_signal_last_flash - J601_SIGNAL_TICK)

        if random.random() < 0.08:
            store.j601_signal_noise_line = random.choice([
                "KAMI_SIGNAL::OFFSET_ERROR",
                "VOICE_LAYER::UNSYNC",
                "AMENDMENT_TEXT::READ_FAIL",
                "AUTHORITY_CORE::STABLE?",
                "DISTRICT_MOVEMENT::PENDING",
                "HARMONIC_LINK::DAMAGED",
                "OBSERVATION_NODE::NO_RESPONSE",
                "CONTROL_LOOP::RETRY",
            ])

        if store.j601_signal_time_left <= 0.0:
            store.j601_signal_done = True
            store.j601_signal_success = (store.j601_signal_green_time >= 17.0 and store.j601_signal_errors < 12)

    # Jour 6 : 

    def j601_signal_get_zone():
        c = store.j601_signal_cursor
        if 30.0 <= c <= 70.0:
            return "green"
        elif 15.0 <= c <= 85.0:
            return "orange"
        else:
            return "red"

    j601_signal_lines = [
        (0.0, "Le présent amendement vise à autoriser la libre circulation entre les districts afin de…"),
        (10.0, "…permettre aux citoyens de se déplacer librement sans autorisation préalable des Responsables de District. Ceci dans le but de…"),
        (20.0, "…favoriser les échanges, le commerce et… et… l’unité… l’unité… l’unité…"),
        (30.0, "Vous allez enfin pouvoir vivre… circuler… mourir… non… bouger comme bon vous semble !"),
        (33.0, "Assez ! Peu importe. Vous avez compris l’idée."),
        (36.0, "Ce n’est qu’un vulgaire bout de papier de toute façon…")
    ]

    def j601_signal_update_line(elapsed):
        current = j601_signal_lines[0][1]
        for t, line in j601_signal_lines:
            if elapsed >= t:
                current = line
        return current

    def j601_signal_glitch_text(text):
        zone = j601_signal_get_zone()

        if zone == "green":
            glitch_chance = 0.03
        elif zone == "orange":
            glitch_chance = 0.22
        else:
            glitch_chance = 0.62

        glitch_chars = ["#", "%", "&", "@", "?", "█", "░", "▒", "▓", "/", "\\", "0", "1"]

        result = []
        for char in text:
            if char == " ":
                result.append(char)
            elif random.random() < glitch_chance:
                result.append(random.choice(glitch_chars))
            else:
                result.append(char)

        return "".join(result)

transform j601_signal_kami_soft:
    xalign 0.5
    yalign 0.5
    alpha 0.90
    xoffset 0
    yoffset 0
    linear 0.16 alpha 0.96 xoffset 2
    linear 0.08 alpha 0.86 xoffset -3 yoffset 1
    linear 0.22 alpha 0.94 xoffset 0 yoffset 0
    pause 0.28
    repeat

transform j601_signal_kami_hard:
    xalign 0.5
    yalign 0.5
    alpha 0.96
    xoffset 0
    yoffset 0
    linear 0.035 xoffset 13 yoffset -3 alpha 0.78
    linear 0.025 xoffset -11 yoffset 4 alpha 1.0
    linear 0.045 xoffset 5 yoffset -1
    linear 0.06 xoffset 0 yoffset 0 alpha 0.91
    pause 0.10
    repeat

transform j601_signal_text_soft:
    alpha 0.95
    xoffset 0
    linear 0.09 xoffset 2 alpha 0.82
    linear 0.06 xoffset -2 alpha 1.0
    linear 0.12 xoffset 0 alpha 0.95
    pause 0.34
    repeat

transform j601_signal_text_hard:
    alpha 1.0
    xoffset 0
    yoffset 0
    linear 0.03 xoffset 7 yoffset -2 alpha 0.72
    linear 0.03 xoffset -6 yoffset 2 alpha 1.0
    linear 0.05 xoffset 0 yoffset 0 alpha 0.88
    pause 0.08
    repeat

transform j601_signal_cursor_pulse:
    alpha 1.0
    linear 0.20 alpha 0.48
    linear 0.20 alpha 1.0
    repeat

transform j601_qte_pulse:
    zoom 1.0
    alpha 1.0
    linear 0.12 zoom 1.18 alpha 0.75
    linear 0.12 zoom 1.0 alpha 1.0
    repeat

screen j601_signal_instable_screen():

    modal True
    zorder 250

    key "K_LEFT" action Function(j601_signal_nudge, -1.8)
    key "K_q" action Function(j601_signal_nudge, -1.8)
    key "K_a" action Function(j601_signal_nudge, -1.8)
    key "K_RIGHT" action Function(j601_signal_nudge, 1.8)
    key "K_d" action Function(j601_signal_nudge, 1.8)
    key "K_SPACE" action Function(j601_signal_qte_hit)
    key "K_RETURN" action Function(j601_signal_qte_hit)
    key "K_KP_ENTER" action Function(j601_signal_qte_hit)

    timer J601_SIGNAL_TICK repeat True action Function(j601_signal_tick)

    $ kami_signal_asset = "images/minigame/signal_instable/kami_transmission_glitch_v2.png"
    $ signal_zone = j601_signal_get_zone()
    $ signal_color = "#48F5FF" if signal_zone == "green" else "#FFD166" if signal_zone == "orange" else "#FF526A"
    $ signal_text_transform = j601_signal_text_soft if j601_signal_phase == 1 else j601_signal_text_hard

    add Solid("#020711")

    if j601_signal_phase < 3:
        add kami_signal_asset at j601_signal_kami_soft
    else:
        add kami_signal_asset at j601_signal_kami_hard

    # Dédoublement chromatique et flou animé de la transmission.
    if j601_signal_phase == 1:
        add Transform(kami_signal_asset, blur=2.0, alpha=0.16, xoffset=-5, matrixcolor=TintMatrix("#44E9FF")) at j601_signal_kami_soft
    elif j601_signal_phase == 2:
        add Transform(kami_signal_asset, blur=5.0, alpha=0.20, xoffset=-10, matrixcolor=TintMatrix("#36DFFF")) at j601_signal_kami_soft
        add Transform(kami_signal_asset, blur=3.0, alpha=0.12, xoffset=10, matrixcolor=TintMatrix("#FF3C72")) at j601_signal_kami_soft
    else:
        add Transform(kami_signal_asset, blur=9.0, alpha=0.25, xoffset=-16, matrixcolor=TintMatrix("#1FDFFF")) at j601_signal_kami_hard
        add Transform(kami_signal_asset, blur=6.0, alpha=0.20, xoffset=17, matrixcolor=TintMatrix("#FF285F")) at j601_signal_kami_hard

    add Solid("#0207112A")

    for i in range(0, 1080, 6):
        add Solid("#BFEFFF0A", xysize=(1920, 1)) xpos 0 ypos i

    for i in range(7):
        add Solid("#42DFFF18", xysize=(110 + ((i * 73) % 250), 2)) xpos ((i * 307) % 1750) ypos (95 + i * 79)

    if j601_signal_last_flash > 0.0:
        add Solid("#FF345533")

    frame:
        xpos 24
        ypos 20
        xsize 500
        ysize 62
        background Solid("#06101DDD")
        padding (24, 13)
        text "CONCENTRATION : SYNCHRO":
            size 27
            color "#46A9FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 2.0

    frame:
        xalign 0.975
        ypos 20
        xsize 300
        ysize 118
        background Solid("#06101DEE")
        padding (18, 10)
        vbox:
            xalign 0.5
            spacing 3
            text "TEMPS RESTANT":
                xalign 0.5
                size 18
                color "#7089A8"
            text "00:[j601_signal_time_left:04.1f]":
                xalign 0.5
                size 49
                color ("#FF6875" if j601_signal_time_left < 10.0 else "#D8E8F7")
                font "fonts/Rajdhani-SemiBold.ttf"

    frame:
        xpos 24
        ypos 140
        xsize 350
        ysize 300
        background Solid("#07111EEB")
        padding (28, 22)
        vbox:
            spacing 15
            text "OBJECTIF":
                size 27
                color "#42A5FF"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "Concentrez-vous pour comprendre Kami.\n\nGardez le curseur dans la zone de concentration.":
                size 23
                color "#D4DDE7"
                line_spacing 8
            text "STABILITÉ [j601_signal_green_time:.1f] / 17.0 s":
                size 19
                color signal_color

    frame:
        xpos 24
        ypos 464
        xsize 350
        ysize 148
        background Solid("#170A12E8")
        padding (28, 20)
        vbox:
            spacing 10
            text "!  DISTRACTIONS":
                size 25
                color "#FF526A"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "Ne laissez pas le curseur sortir de la zone.":
                size 21
                color "#E9828E"
                line_spacing 6

    # Le texte de Kami se corrompt et se déplace en direct.
    frame:
        xpos 1330
        ypos 168
        xsize 566
        ysize 408
        background Solid("#050B14EE")
        padding (30, 23)
        vbox:
            spacing 16
            text (
                "KAMI  [[TRANSMISSION]" if j601_signal_phase == 1
                else "KAMI  [[TRANSMISSION INSTABLE]" if j601_signal_phase == 2
                else "KAMI  [[RUPTURE DE SIGNAL]"
            ):
                size 26
                color "#9DB2CE"
                font "fonts/Rajdhani-SemiBold.ttf"

            fixed:
                xsize 500
                ysize 230

                if j601_signal_phase >= 2:
                    text "[j601_signal_display_line]":
                        xpos -3
                        ypos 1
                        xmaximum 500
                        size 26
                        color "#39DFFF55"
                        line_spacing 8
                        at signal_text_transform
                    text "[j601_signal_display_line]":
                        xpos 4
                        ypos -1
                        xmaximum 500
                        size 26
                        color "#FF3B6B44"
                        line_spacing 8
                        at signal_text_transform

                text "[j601_signal_display_line]":
                    xmaximum 500
                    size 26
                    color "#E7ECF2"
                    line_spacing 8
                    at signal_text_transform

            text "[j601_signal_noise_line]":
                size 16
                color "#4FD9FF88"

            text "PHASE [j601_signal_phase]  //  ERREURS [j601_signal_errors:.1f]":
                size 17
                color "#8192A8"

    # QTE flash sur l'hologramme.
    if j601_signal_qte_active:
        button:
            xpos int(1920 * j601_signal_qte_x) - 68
            ypos int(1080 * j601_signal_qte_y) - 68
            xsize 136
            ysize 136
            background Solid("#FF2E63CC")
            hover_background Solid("#F7FBFFFF")
            action Function(j601_signal_qte_hit)
            at j601_qte_pulse
            text "FRACTURE\nESPACE":
                xalign 0.5
                yalign 0.5
                text_align 0.5
                size 20
                color "#FFFFFF"
                bold True

    # Panneau de concentration inférieur.
    frame:
        xpos 24
        ypos 650
        xsize 1872
        ysize 402
        background Solid("#050B14F2")
        padding (36, 18)

        vbox:
            xalign 0.5
            spacing 11

            text "ZONE DE CONCENTRATION":
                xalign 0.5
                size 30
                color "#43A9FF"
                font "fonts/Rajdhani-SemiBold.ttf"

            fixed:
                xsize 1540
                ysize 116
                xalign 0.5

                add Solid("#280914") xpos 0 ypos 30 xysize (231, 46)
                add Solid("#4C2E15") xpos 231 ypos 30 xysize (231, 46)
                add Solid("#0B3452") xpos 462 ypos 18 xysize (616, 70)
                add Solid("#4C2E15") xpos 1078 ypos 30 xysize (231, 46)
                add Solid("#280914") xpos 1309 ypos 30 xysize (231, 46)

                add Solid("#267DD066") xpos 462 ypos 11 xysize (3, 84)
                add Solid("#267DD066") xpos 1075 ypos 11 xysize (3, 84)
                add Solid("#40A9FF22") xpos 478 ypos 22 xysize (584, 62)

                add Solid("#DCEBFF") xpos int((j601_signal_cursor / 100.0) * 1540) - 7 ypos 12 xysize (14, 84) at j601_signal_cursor_pulse
                add Solid(signal_color) xpos int((j601_signal_cursor / 100.0) * 1540) - 3 ypos 5 xysize (6, 98)

                text "!" xpos 72 ypos 4 size 72 color "#FF526A"
                text "!" xpos 1415 ypos 4 size 72 color "#FF526A"

            text "[j601_signal_warning]":
                xalign 0.5
                size 25
                color signal_color
                font "fonts/Rajdhani-SemiBold.ttf"

            hbox:
                xalign 0.5
                spacing 70

                textbutton "←  FLÈCHE GAUCHE":
                    xsize 330
                    ysize 64
                    action Function(j601_signal_nudge, -1.8)

                textbutton "TRANSMISSION EN COURS  //  ESPACE : RECALIBRER":
                    xsize 650
                    ysize 64
                    action Function(j601_signal_qte_hit)

                textbutton "FLÈCHE DROITE  →":
                    xsize 330
                    ysize 64
                    action Function(j601_signal_nudge, 1.8)

    if j601_signal_done:
        timer 0.2 action Return(j601_signal_success)


label j601_play_signal_instable:

    $ j601_signal_reset()
    $ result_signal = renpy.call_screen("j601_signal_instable_screen")
    return result_signal
