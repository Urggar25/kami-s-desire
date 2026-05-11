# ============================================================
# MINI-JEU JOUR 6_0_1 — FRACTURE
# QTE nerveux après SIGNAL INSTABLE
# Durée : ~36 secondes maximum
# Appel scénario :
#   call j601_play_fracture
#   $ j601_fracture_result = _return
# ============================================================

default j601_fracture_step = 0
default j601_fracture_success_count = 0
default j601_fracture_fail_count = 0
default j601_fracture_done = False
default j601_fracture_prompt_active = False
default j601_fracture_current_key = ""
default j601_fracture_current_label = ""
default j601_fracture_time_left = 36.0
default j601_fracture_qte_time = 0.0
default j601_fracture_next_event = 1.2
default j601_fracture_line = ""
default j601_fracture_warning = "FRACTURE INIT"
default j601_fracture_flash = 0.0
default j601_fracture_result = False



init python:
    import random
    import math

    J601_FRACTURE_TICK = 0.05
    J601_FRACTURE_TOTAL_TIME = 36.0

    j601_fracture_phrases = [
        "Cet amendement permettra à chaque citoyen de voyager librement sans restriction ni visa… visa…",
        "Les districts ne seront plus des prisons dorées. Chacun pourra… pourra… pourra enfin…",
        "Les Gardiens n’auront plus à mourir pour des lignes imaginaires sur une carte. C’est… c’est… absurde…",
        "Il est temps d’ouvrir les frontières et de… briser… brûler… non…"
    ]

    j601_fracture_keys = ["K_z", "K_q", "K_s", "K_d", "K_SPACE", "K_RETURN"]

    def j601_fracture_glitch_text(text):
        glitch_chars = ["#", "%", "&", "@", "█", "▒", "▓", "░", "/", "\\", "0", "1"]

        result = []
        for c in text:
            if c == " ":
                result.append(c)
            elif random.random() < 0.45:
                result.append(random.choice(glitch_chars))
            else:
                result.append(c)

        return "".join(result)

    j601_fracture_events = [
        {
            "line": "La libre circulation entre districts... districts...",
            "key": "K_a",
            "label": "A",
            "delay": 2.3,
            "window": 1.05,
            "warning": "LOOP VOCAL"
        },
        {
            "line": "...va enfin permettre la vrai... la vraie liberté.",
            "key": "K_SPACE",
            "label": "ESPACE",
            "delay": 2.5,
            "window": 0.95,
            "warning": "CORRECTION FORCÉE"
        },
        {
            "line": "Plus de barrières inutiles.",
            "key": "K_LEFT",
            "label": "←",
            "delay": 2.4,
            "window": 1.00,
            "warning": "VOIX GRAVE"
        },
        {
            "line": "Vous allez enfin pouvoir... mourir... je veux dire bouger librement !",
            "key": "K_UP",
            "label": "↑",
            "delay": 2.2,
            "window": 0.90,
            "warning": "LAPSUS CRITIQUE"
        },
    ]

    def j601_fracture_reset():
        store.j601_fracture_done = False
        store.j601_fracture_success_count = 0
        store.j601_fracture_fail_count = 0

        store.j601_fracture_sequence_length = random.randint(5, 8)
        store.j601_fracture_step = 0

        store.j601_fracture_prompt_active = False
        store.j601_fracture_qte_time = 0.0

        store.j601_fracture_current_key = ""
        store.j601_fracture_current_label = ""

        store.j601_fracture_line = ""
        store.j601_fracture_display_line = ""

        store.j601_fracture_next_event = 1.5

    def j601_fracture_start_event():
        if store.j601_fracture_step >= store.j601_fracture_sequence_length:
            return

        phrase = random.choice(j601_fracture_phrases)
        key = random.choice(j601_fracture_keys)

        store.j601_fracture_line = phrase
        store.j601_fracture_current_key = key
        store.j601_fracture_current_label = key.replace("K_", "")

        store.j601_fracture_qte_time = random.uniform(0.9, 1.1)
        store.j601_fracture_prompt_active = True

    def j601_fracture_press(key_name):
        if not store.j601_fracture_prompt_active:
            return

        if key_name == store.j601_fracture_current_key:
            store.j601_fracture_success_count += 1
            store.j601_fracture_display_line = store.j601_fracture_line
        else:
            store.j601_fracture_fail_count += 1
            store.j601_fracture_display_line = j601_fracture_glitch_text(store.j601_fracture_line)

        store.j601_fracture_prompt_active = False
        store.j601_fracture_step += 1
        store.j601_fracture_next_event = random.uniform(1.5, 2.5)

    def j601_fracture_tick():

        if store.j601_fracture_done:
            return

        if store.j601_fracture_prompt_active:
            store.j601_fracture_qte_time -= 0.05

            if store.j601_fracture_qte_time <= 0:
                store.j601_fracture_fail_count += 1
                store.j601_fracture_display_line = j601_fracture_glitch_text(store.j601_fracture_line)

                store.j601_fracture_prompt_active = False
                store.j601_fracture_step += 1
                store.j601_fracture_next_event = random.uniform(1.5, 2.5)

        else:
            store.j601_fracture_next_event -= 0.05

            if store.j601_fracture_next_event <= 0:
                j601_fracture_start_event()

        if store.j601_fracture_step >= store.j601_fracture_sequence_length:
            store.j601_fracture_display_line = "Vu que vous ne voulez pas débattre, il est temps maintenant de mour... voter... voter..."
            store.j601_fracture_done = True


transform j601_fracture_glitch:
    alpha 0.94
    xoffset 0
    yoffset 0
    linear 0.04 xoffset 10 yoffset -2
    linear 0.04 xoffset -8 yoffset 2
    linear 0.05 xoffset 5
    linear 0.08 xoffset 0 yoffset 0
    pause 0.16
    repeat

transform j601_fracture_prompt_pulse:
    zoom 1.0
    alpha 1.0
    linear 0.08 zoom 1.15 alpha 0.85
    linear 0.08 zoom 1.0 alpha 1.0
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

    add Solid("#02040C")

    for i in range(0, 1080, 8):
        add Solid("#FFFFFF07", xysize=(1920, 1)) xpos 0 ypos i

    if j601_fracture_flash > 0.0:
        add Solid("#FF2E6338")

    add "bg_diffusion_colere" at j601_fracture_glitch:
        xalign 0.5
        yalign 0.35
        zoom 0.84

    add Solid("#030611AA")

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
            text "FRACTURE":
                xalign 0.5
                size 44
                color "#D9F8FF"
                bold True
            text "Réagissez aux failles de Kami avant qu’elles disparaissent.":
                xalign 0.5
                size 20
                color "#9FC7D8"

    frame:
        xalign 0.5
        yalign 0.22
        xsize 1180
        ysize 92
        background Solid("#00000099")
        text "[j601_fracture_display_line]":
            xalign 0.5
            yalign 0.5
            size 30
            color "#FFFFFF"
            text_align 0.5

    frame:
        xalign 0.5
        yalign 0.80
        xsize 980
        ysize 120
        background Solid("#07101FDB")
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 70
            text "TEMPS [j601_fracture_time_left:.1f]":
                size 26
                color "#DDF8FF"
            if j601_fracture_warning == "FRACTURE CAPTÉE":
                text "[j601_fracture_warning]":
                    size 26
                    color "#5DFF9A"
            else:
                text "[j601_fracture_warning]":
                    size 26
                    color "#FF6B9A"
            text "RÉUSSITES [j601_fracture_success_count]/4":
                size 26
                color "#DDF8FF"

    if j601_fracture_prompt_active:
        frame:
            xalign 0.5
            yalign 0.52
            xsize 250
            ysize 250
            background Solid("#101B33EE")
            at j601_fracture_prompt_pulse

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                text "[j601_fracture_current_label]":
                    xalign 0.5
                    size 86
                    color "#7DF9FF"
                    bold True

                text "FRACTURE":
                    xalign 0.5
                    size 24
                    color "#FF6B9A"
                    bold True

                bar:
                    xalign 0.5
                    xsize 180
                    ysize 10
                    value AnimatedValue(value=j601_fracture_qte_time, range=1.1, delay=0.05)
                    left_bar Solid("#7DF9FF")
                    right_bar Solid("#2A2F45")

    if j601_fracture_success_count >= 1:
        add Solid("#7DF9FF22", xysize=(300, 2)) xpos 790 ypos 355 rotate 12
    if j601_fracture_success_count >= 2:
        add Solid("#FF6B9A26", xysize=(360, 2)) xpos 760 ypos 470 rotate -18
    if j601_fracture_success_count >= 3:
        add Solid("#FFFFFF22", xysize=(420, 2)) xpos 740 ypos 590 rotate 26
    if j601_fracture_success_count >= 4:
        add Solid("#7DF9FF33", xysize=(500, 2)) xpos 710 ypos 650 rotate -8

    if j601_fracture_done:
        timer 0.2 action Return(j601_fracture_result)


label j601_play_fracture:

    $ j601_fracture_reset()
    $ result_fracture = renpy.call_screen("j601_fracture_screen")
    return result_fracture