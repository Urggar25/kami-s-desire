# ============================================================
# MINI-JEU JOUR 6_0_1 — FRACTURE
# Une seule fracture/QTE à la fois. Trois erreurs maximum.
# Appel scénario :
#   call j601_play_fracture
#   $ j601_fracture_result = _return
# ============================================================

default j601_fracture_step = 0
default j601_fracture_success_count = 0
default j601_fracture_fail_count = 0
default j601_fracture_lives = 3
default j601_fracture_max_lives = 3
default j601_fracture_done = False
default j601_fracture_prompt_active = False
default j601_fracture_current_key = ""
default j601_fracture_current_label = ""
default j601_fracture_time_left = 36.0
default j601_fracture_qte_time = 0.0
default j601_fracture_qte_max_time = 2.4
default j601_fracture_next_event = 0.8
default j601_fracture_line = ""
default j601_fracture_warning = "TRANSMISSION EN ATTENTE"
default j601_fracture_flash = 0.0
default j601_fracture_result = False
default j601_fracture_sequence_length = 6
default j601_fracture_display_line = "Connexion au canal de Kami…"
default j601_fracture_text_tick = 0.0


init python:
    import random

    J601_FRACTURE_TICK = 0.05
    J601_FRACTURE_TOTAL_TIME = 36.0

    j601_fracture_phrases = [
        "LIMEN TOMBE. VOUS REGARDEZ, VOUS COMPRENEZ RIEN.",
        "MAIS VOUS VOTEZ QUAND MÊME. INTÉRESSANT, N’EST-CE PAS ?",
        "LES DISTRICTS NE SERONT PLUS DES PRISONS DORÉES.",
        "LES GARDIENS MEURENT POUR DES LIGNES IMAGINAIRES.",
        "OUVREZ LES FRONTIÈRES. BRISEZ… BRÛLEZ… NON.",
        "ÉCOUTEZ CHAQUE MOT. LE SIGNAL NE MENT PAS."
    ]

    j601_fracture_keys = ["K_z", "K_q", "K_s", "K_d", "K_SPACE", "K_RETURN"]

    J601_FRACTURE_KEY_LABELS = {
        "K_z": "Z", "K_q": "Q", "K_s": "S", "K_d": "D",
        "K_SPACE": "ESPACE", "K_RETURN": "ENTRÉE",
    }

    def j601_fracture_glitch_text(text, amount=0.22):
        glitch_chars = ["#", "%", "&", "@", "█", "▒", "▓", "░", "/", "\\", "0", "1"]
        result = []
        for char in text:
            if char == " " or random.random() >= amount:
                result.append(char)
            else:
                result.append(random.choice(glitch_chars))
        return "".join(result)

    def j601_fracture_reset():
        store.j601_fracture_step = 0
        store.j601_fracture_success_count = 0
        store.j601_fracture_fail_count = 0
        store.j601_fracture_lives = store.j601_fracture_max_lives
        store.j601_fracture_done = False
        store.j601_fracture_prompt_active = False
        store.j601_fracture_current_key = ""
        store.j601_fracture_current_label = ""
        store.j601_fracture_time_left = J601_FRACTURE_TOTAL_TIME
        store.j601_fracture_qte_time = 0.0
        store.j601_fracture_qte_max_time = 2.4
        store.j601_fracture_next_event = 0.8
        store.j601_fracture_line = ""
        store.j601_fracture_display_line = "Connexion au canal de Kami…"
        store.j601_fracture_warning = "TRANSMISSION EN ATTENTE"
        store.j601_fracture_flash = 0.0
        store.j601_fracture_result = False
        store.j601_fracture_text_tick = 0.0

    def j601_fracture_start_event():
        # Garde stricte : jamais plus d'un QTE actif à l'écran.
        if (store.j601_fracture_prompt_active or store.j601_fracture_done
                or store.j601_fracture_success_count >= store.j601_fracture_sequence_length):
            return

        phrase_index = store.j601_fracture_success_count % len(j601_fracture_phrases)
        store.j601_fracture_line = j601_fracture_phrases[phrase_index]
        store.j601_fracture_display_line = store.j601_fracture_line
        store.j601_fracture_current_key = random.choice(j601_fracture_keys)
        store.j601_fracture_current_label = J601_FRACTURE_KEY_LABELS[store.j601_fracture_current_key]

        progress = store.j601_fracture_success_count / float(max(1, store.j601_fracture_sequence_length - 1))
        store.j601_fracture_qte_max_time = max(1.35, 2.45 - progress * 0.85)
        store.j601_fracture_qte_time = store.j601_fracture_qte_max_time
        store.j601_fracture_prompt_active = True
        store.j601_fracture_warning = "FRACTURE DÉTECTÉE"

    def j601_fracture_lose_life(reason):
        store.j601_fracture_fail_count += 1
        store.j601_fracture_lives = max(0, store.j601_fracture_lives - 1)
        store.j601_fracture_display_line = j601_fracture_glitch_text(store.j601_fracture_line, 0.48)
        store.j601_fracture_warning = reason
        store.j601_fracture_flash = 0.32
        store.j601_fracture_prompt_active = False
        store.j601_fracture_qte_time = 0.0
        store.j601_fracture_next_event = 0.7
        if renpy.loadable("audio/sfx_qte_miss.wav"):
            renpy.play("audio/sfx_qte_miss.wav", channel="sound")

    def j601_fracture_press(key_name):
        if not store.j601_fracture_prompt_active or store.j601_fracture_done:
            return

        if key_name != store.j601_fracture_current_key:
            j601_fracture_lose_life("MAUVAISE TOUCHE — VIE PERDUE")
            return

        store.j601_fracture_success_count += 1
        store.j601_fracture_step = store.j601_fracture_success_count
        store.j601_fracture_display_line = store.j601_fracture_line
        store.j601_fracture_warning = "FRACTURE CAPTÉE"
        store.j601_fracture_prompt_active = False
        store.j601_fracture_qte_time = 0.0
        store.j601_fracture_next_event = 0.65
        if renpy.loadable("audio/sfx_qte_hit.wav"):
            renpy.play("audio/sfx_qte_hit.wav", channel="sound")

    def j601_fracture_finish(success, message):
        store.j601_fracture_result = success
        store.j601_fracture_done = True
        store.j601_fracture_prompt_active = False
        store.j601_fracture_display_line = message
        store.j601_fracture_warning = "SÉQUENCE STABILISÉE" if success else "TRANSMISSION PERDUE"

    def j601_fracture_tick():
        if store.j601_fracture_done:
            return

        store.j601_fracture_time_left = max(0.0, store.j601_fracture_time_left - J601_FRACTURE_TICK)
        store.j601_fracture_flash = max(0.0, store.j601_fracture_flash - J601_FRACTURE_TICK)
        store.j601_fracture_text_tick -= J601_FRACTURE_TICK

        if store.j601_fracture_lives <= 0:
            j601_fracture_finish(False, "SIGNAL ROMPU. VOUS N’ENTENDEZ PLUS QUE DU BRUIT.")
            return

        if store.j601_fracture_time_left <= 0.0:
            j601_fracture_finish(False, "TEMPS ÉCOULÉ. LA TRANSMISSION S’EFFONDRE.")
            return

        if store.j601_fracture_success_count >= store.j601_fracture_sequence_length:
            j601_fracture_finish(True, "IL EST TEMPS MAINTENANT DE MOUR… VOTER. VOTER.")
            return

        if store.j601_fracture_prompt_active:
            store.j601_fracture_qte_time = max(0.0, store.j601_fracture_qte_time - J601_FRACTURE_TICK)
            if store.j601_fracture_text_tick <= 0.0:
                store.j601_fracture_display_line = j601_fracture_glitch_text(store.j601_fracture_line, 0.08)
                store.j601_fracture_text_tick = 0.12
            if store.j601_fracture_qte_time <= 0.0:
                j601_fracture_lose_life("TROP TARD — VIE PERDUE")
        else:
            store.j601_fracture_next_event -= J601_FRACTURE_TICK
            if store.j601_fracture_next_event <= 0.0:
                j601_fracture_start_event()


transform j601_fracture_kami_glitch:
    alpha 0.96
    xoffset 0
    yoffset 0
    linear 0.06 xoffset 7 yoffset -2
    linear 0.05 xoffset -5 yoffset 2
    linear 0.08 xoffset 0 yoffset 0
    pause 0.32
    repeat

transform j601_fracture_text_glitch:
    alpha 1.0
    xoffset 0
    linear 0.04 xoffset 3
    linear 0.04 xoffset -3
    linear 0.05 xoffset 0
    pause 0.22
    repeat

transform j601_fracture_prompt_pulse:
    zoom 1.0
    alpha 1.0
    linear 0.16 zoom 1.035 alpha 0.88
    linear 0.16 zoom 1.0 alpha 1.0
    repeat


screen j601_fracture_screen():
    modal True
    zorder 260

    timer J601_FRACTURE_TICK repeat True action Function(j601_fracture_tick)

    key "K_z" action Function(j601_fracture_press, "K_z")
    key "K_q" action Function(j601_fracture_press, "K_q")
    key "K_s" action Function(j601_fracture_press, "K_s")
    key "K_d" action Function(j601_fracture_press, "K_d")
    key "K_SPACE" action Function(j601_fracture_press, "K_SPACE")
    key "K_RETURN" action Function(j601_fracture_press, "K_RETURN")
    key "K_KP_ENTER" action Function(j601_fracture_press, "K_RETURN")

    $ kami_asset = "images/minigame/signal_instable/kami_transmission_glitch_v2.png"
    $ qte_ratio = j601_fracture_qte_time / max(0.01, j601_fracture_qte_max_time)
    $ global_ratio = j601_fracture_time_left / J601_FRACTURE_TOTAL_TIME

    add Solid("#010713")
    add kami_asset:
        alpha 0.22
    add Solid("#010713A8")

    # Kami est isolée sur le tiers gauche, comme sur la référence.
    add Transform(Crop((500, 40, 920, 1000), kami_asset), xysize=(736, 800), blur=0.8):
        xpos 20
        ypos 120
        at j601_fracture_kami_glitch
    add Transform(Crop((500, 40, 920, 1000), kami_asset), xysize=(736, 800), matrixcolor=TintMatrix("#20D9FF"), alpha=0.18):
        xpos 10
        ypos 120
    add Transform(Crop((500, 40, 920, 1000), kami_asset), xysize=(736, 800), matrixcolor=TintMatrix("#FF315F"), alpha=0.12):
        xpos 32
        ypos 120

    for scan_y in range(0, 1080, 7):
        add Solid("#8BCBFF0B", xysize=(1920, 1)) xpos 0 ypos scan_y

    if j601_fracture_flash > 0.0:
        add Solid("#FF2E4F42")

    # Statut de transmission.
    frame:
        xpos 24
        ypos 22
        xsize 450
        ysize 104
        padding (28, 16)
        background Solid("#071426E8")
        vbox:
            spacing 4
            text "◉  KAMI — TRANSMISSION EN COURS" size 25 color "#78AEFF" bold True
            text "Connexion : INSTABLE" size 20 color "#FF6875"

    # Vies : chaque erreur ou expiration en retire une.
    frame:
        xpos 1540
        ypos 22
        xsize 350
        ysize 132
        padding (24, 14)
        background Solid("#071426E8")
        vbox:
            xalign 0.5
            spacing 7
            text "VIES RESTANTES" xalign 0.5 size 23 color "#8FAACA" bold True
            hbox:
                xalign 0.5
                spacing 18
                for life_index in range(j601_fracture_max_lives):
                    text "♥":
                        size 48
                        color ("#FF6673" if life_index < j601_fracture_lives else "#293342")
                        outlines [(2, "#B42F44" if life_index < j601_fracture_lives else "#596273", 0, 0)]

    # Transmission textuelle, volontairement animée et instable.
    frame:
        xpos 680
        ypos 150
        xsize 1160
        ysize 360
        padding (38, 28)
        background Solid("#020A16C8")
        vbox:
            xalign 0.5
            spacing 12
            text "KAMI" xalign 0.5 size 34 color "#649BFF" bold True
            text "[j601_fracture_display_line]":
                xalign 0.5
                xmaximum 1060
                size 46
                color "#E7F3FF"
                bold True
                text_align 0.5
                outlines [(2, "#3E74A7AA", 0, 0)]
                at j601_fracture_text_glitch
            text "APPUYEZ SUR LA TOUCHE AFFICHÉE POUR CONTINUER À ÉCOUTER.":
                xalign 0.5
                size 21
                color "#5F8CC5"

    # Un seul QTE existe à la fois : aucune rangée de touches pré-affichées.
    if j601_fracture_prompt_active:
        frame:
            xpos 960
            ypos 535
            xsize 440
            ysize 230
            padding (24, 18)
            background Solid("#071426F2")
            at j601_fracture_prompt_pulse
            vbox:
                xalign 0.5
                spacing 12
                text "FRACTURE [j601_fracture_success_count + 1]/[j601_fracture_sequence_length]":
                    xalign 0.5
                    size 21
                    color "#6EA8E9"
                frame:
                    xalign 0.5
                    xminimum 190
                    yminimum 104
                    padding (28, 12)
                    background Solid("#10233BEF")
                    text "[j601_fracture_current_label]":
                        xalign 0.5
                        yalign 0.5
                        size (55 if j601_fracture_current_label in ("ESPACE", "ENTRÉE") else 74)
                        color "#EAF7FF"
                        bold True
                bar:
                    xalign 0.5
                    xsize 330
                    ysize 12
                    value qte_ratio
                    left_bar Solid("#4FAEFF")
                    right_bar Solid("#16283A")
    else:
        frame:
            xpos 960
            ypos 570
            xsize 440
            ysize 130
            background Solid("#071426C8")
            text "SIGNAL SUIVANT…":
                xalign 0.5
                yalign 0.5
                size 30
                color "#5F8CC5"

    # Progression globale et chrono.
    frame:
        xpos 640
        ypos 805
        xsize 1240
        ysize 152
        padding (32, 18)
        background Solid("#061120E8")
        vbox:
            spacing 10
            hbox:
                xfill True
                text "SÉQUENCE [j601_fracture_success_count]/[j601_fracture_sequence_length]" size 24 color "#80B5FF" bold True
                text "TEMPS  [j601_fracture_time_left:04.1f] s" xalign 1.0 size 24 color ("#FF6875" if j601_fracture_time_left < 10.0 else "#D9EDFF") bold True
            bar:
                xsize 1176
                ysize 15
                value AnimatedValue(value=j601_fracture_success_count, range=j601_fracture_sequence_length, delay=0.12)
                left_bar Solid("#4FAEFF")
                right_bar Solid("#15283D")
            text "[j601_fracture_warning]":
                xalign 0.5
                size 24
                color ("#67F0BE" if j601_fracture_warning in ("FRACTURE CAPTÉE", "SÉQUENCE STABILISÉE") else "#FF6875")
                bold True

    frame:
        xpos 24
        ypos 965
        xsize 1856
        ysize 86
        padding (28, 13)
        background Solid("#050E1BE8")
        hbox:
            spacing 160
            text "⚠  Chaque erreur vous éloigne de la vérité." size 22 color "#FF6875"
            text "CONSEIL : restez concentré. Un seul signal apparaît à la fois." size 22 color "#88A5C8"

    if j601_fracture_done:
        timer 1.4 action Return(j601_fracture_result)


label j601_play_fracture:
    $ j601_fracture_reset()
    $ result_fracture = renpy.call_screen("j601_fracture_screen")
    return result_fracture
