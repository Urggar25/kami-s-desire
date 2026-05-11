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

init python:
    import random

    def j601_signal_get_zone():
        c = store.j601_signal_cursor
        if 30 <= c <= 70:
            return "green"
        elif 15 <= c <= 85:
            return "orange"
        else:
            return "red"

    def j601_signal_glitch_text(text):
        zone = j601_signal_get_zone()

        if zone == "green":
            glitch_chance = 0.05
        elif zone == "orange":
            glitch_chance = 0.25
        else:
            glitch_chance = 0.60

        chars = list(text)
        for i in range(len(chars)):
            if random.random() < glitch_chance:
                chars[i] = random.choice([
                    "#", "%", "&", "@", "?", "█", "░", "▒", "▓",
                    random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                ])
        return "".join(chars)

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
        store.j601_signal_qte_x = random.uniform(0.25, 0.75)
        store.j601_signal_qte_y = random.uniform(0.20, 0.48)
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

transform j601_signal_glitch_slow:
    alpha 0.88
    xoffset 0
    yoffset 0
    linear 0.08 xoffset 3
    linear 0.05 xoffset -4
    linear 0.10 xoffset 0
    pause 0.4
    repeat

transform j601_signal_glitch_hard:
    alpha 0.94
    xoffset 0
    yoffset 0
    linear 0.04 xoffset 8 yoffset -2
    linear 0.04 xoffset -7 yoffset 2
    linear 0.05 xoffset 3 yoffset 0
    linear 0.08 xoffset 0 yoffset 0
    pause 0.18
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

    add Solid("#030611")

    # Fond CRT / lignes.
    for i in range(0, 1080, 8):
        add Solid("#FFFFFF08", xysize=(1920, 1)) xpos 0 ypos i

    # Flash d'interférence.
    if j601_signal_last_flash > 0.0:
        add Solid("#FF3D6E33")

    # Hologramme central de Kami.
    if j601_signal_phase == 1:
        add "bg_diffusion_professeur" at j601_signal_glitch_slow:
            xalign 0.5
            yalign 0.36
            zoom 0.82
    elif j601_signal_phase == 2:
        add "bg_diffusion_einstein" at j601_signal_glitch_slow:
            xalign 0.5
            yalign 0.36
            zoom 0.82
    else:
        add "bg_diffusion_colere" at j601_signal_glitch_hard:
            xalign 0.5
            yalign 0.36
            zoom 0.82

    # Voile sombre pour lisibilité.
    add Solid("#03061199")

    # Titre.
    frame:
        xalign 0.5
        yalign 0.055
        xsize 1120
        ysize 86
        background Solid("#081326DD")
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 2
            text "SIGNAL INSTABLE":
                xalign 0.5
                size 42
                color "#D9F8FF"
                bold True
            text "Maintenez le curseur dans la zone verte. Corrigez les fractures avec ESPACE.":
                xalign 0.5
                size 20
                color "#9FC7D8"

    # Texte de Kami / phase.
    frame:
        xalign 0.5
        yalign 0.19
        xsize 1220
        ysize 118
        background Solid("#00000099")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 6

            text (
                "KAMI // LECTURE DE L'AMENDEMENT" if j601_signal_phase == 1
                else "KAMI // DÉSYNCHRONISATION VOCALE" if j601_signal_phase == 2
                else "KAMI // CONTRÔLE INSTABLE"
            ):
                xalign 0.5
                size 22
                color "#7DF9FF"
                bold True

            text "[j601_signal_display_line]":
                xalign 0.5
                xmaximum 1120
                size 26
                color "#FFFFFF"
                text_align 0.5

    # Lignes de code bruitées.
    vbox:
        xpos 64
        ypos 170
        spacing 8
        text "[j601_signal_noise_line]":
            size 18
            color "#62E6FF99"
        text "PHASE [j601_signal_phase] // TIME [j601_signal_time_left:.1f]":
            size 18
            color "#FF6B9A99"
        text "ERRORS [j601_signal_errors:.1f] // GREEN [j601_signal_green_time:.1f]":
            size 18
            color "#FFFFFF77"

    # QTE flash sur l'hologramme.
    if j601_signal_qte_active:
        button:
            xpos int(1920 * j601_signal_qte_x) - 55
            ypos int(1080 * j601_signal_qte_y) - 55
            xsize 110
            ysize 110
            background Solid("#FF2E63AA")
            hover_background Solid("#FFFFFFCC")
            action Function(j601_signal_qte_hit)
            at j601_qte_pulse
            text "ESPACE":
                xalign 0.5
                yalign 0.5
                size 22
                color "#FFFFFF"
                bold True

    # Panneau inférieur.
    frame:
        xalign 0.5
        yalign 0.88
        xsize 1280
        ysize 210
        background Solid("#07101FDB")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 14

            hbox:
                xalign 0.5
                spacing 60
                text "TEMPS [j601_signal_time_left:.1f]":
                    size 28
                    color "#DDF8FF"
                text "[j601_signal_warning]":
                    size 28
                    color (
                        "#5DFF9A" if j601_signal_warning == "STABLE"
                        else "#FFD166" if j601_signal_warning in ("INSTABLE", "RECALIBRAGE")
                        else "#FF4D6D"
                    )
                text "ZONE VERTE [j601_signal_green_time:.1f]s":
                    size 28
                    color "#DDF8FF"

            fixed:
                xsize 1000
                ysize 54
                xalign 0.5

                # Barre segmentée : rouge 15 / orange 15 / vert 40 / orange 15 / rouge 15.
                add Solid("#B00020") xpos 0 ypos 7 xysize (150, 40)
                add Solid("#E8872E") xpos 150 ypos 7 xysize (150, 40)
                add Solid("#26C96F") xpos 300 ypos 7 xysize (400, 40)
                add Solid("#E8872E") xpos 700 ypos 7 xysize (150, 40)
                add Solid("#B00020") xpos 850 ypos 7 xysize (150, 40)

                add Solid("#FFFFFF55") xpos 300 ypos 0 xysize (2, 54)
                add Solid("#FFFFFF55") xpos 700 ypos 0 xysize (2, 54)

                # Curseur.
                add Solid("#FFFFFF") xpos int((j601_signal_cursor / 100.0) * 1000) - 6 ypos 0 xysize (12, 54)
                add Solid("#7DF9FF") xpos int((j601_signal_cursor / 100.0) * 1000) - 3 ypos 0 xysize (6, 54)

            hbox:
                xalign 0.5
                spacing 22

                textbutton "◀ GAUCHE":
                    xsize 210
                    ysize 52
                    action Function(j601_signal_nudge, -1.8)

                textbutton "QTE / ESPACE":
                    xsize 230
                    ysize 52
                    action Function(j601_signal_qte_hit)

                textbutton "DROITE ▶":
                    xsize 210
                    ysize 52
                    action Function(j601_signal_nudge, 1.8)

    if j601_signal_done:
        timer 0.2 action Return(j601_signal_success)


label j601_play_signal_instable:

    $ j601_signal_reset()
    $ result_signal = renpy.call_screen("j601_signal_instable_screen")
    return result_signal