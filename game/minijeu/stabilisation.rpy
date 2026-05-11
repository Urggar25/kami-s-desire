# ============================================================
# MINI-JEU JOUR 8 — STABILISATION
# QTE narratif type fracture_QTE
#
# Appel :
#   call j801_play_stabilisation
#   $ j801_stabilisation_result = _return
# ============================================================

default j801_stab_step = 0
default j801_stab_success_count = 0
default j801_stab_fail_count = 0
default j801_stab_done = False
default j801_stab_time_left = 50.0
default j801_stab_next_event = 1.0
default j801_stab_prompt_active = False
default j801_stab_qte_time = 0.0
default j801_stab_qte_max_time = 4.0
default j801_stab_kael_line = ""
default j801_stab_noam_line = ""
default j801_stab_status = "STABILISATION"
default j801_stab_flash = 0.0
default j801_stab_shake = 0
default j801_stab_result = False
default j801_stab_options = []
default j801_stab_selected_key = ""
default j801_stab_selected_label = ""
default j801_stab_selected_response = ""
default j801_stab_selected_effect = ""

# IMPORTANT :
# Remplace "bg_repos" par le nom exact de ton décor de salle de repos si besoin.
default j801_stab_background = "bg_repos"


init python:
    import random

    J801_STAB_TICK = 0.05
    J801_STAB_TOTAL_TIME = 50.0

    j801_stab_events = [
        {
            "kael": "QUI EST ENTRÉ DANS MA CHAMBRE ?!",
            "delay": 0.8,
            "window": 4.2,
            "options": [
                {
                    "key": "K_SPACE",
                    "label": "ESPACE",
                    "response": "Kael. Respire.",
                    "effect": "calm",
                    "kael_success": "Respirer ?! Quelqu’un est entré chez moi, Noam !",
                    "kael_fail": "PERSONNE RÉPOND ?! PERSONNE ?!"
                }
            ]
        },
        {
            "kael": "Quelqu’un a fouillé sous mon oreiller !",
            "delay": 1.0,
            "window": 4.3,
            "options": [
                {
                    "key": "K_z",
                    "label": "Z",
                    "response": "On va comprendre.",
                    "effect": "reason",
                    "kael_success": "Comprendre ? Je veux savoir qui.",
                    "kael_fail": "Vous comprenez pas. Vous comprenez rien !"
                },
                {
                    "key": "K_s",
                    "label": "S",
                    "response": "Je suis là.",
                    "effect": "empathy",
                    "kael_success": "Alors regarde-moi et dis-moi qui a fait ça.",
                    "kael_fail": "J’étais censé être en sécurité ici !"
                }
            ]
        },
        {
            "kael": "C’était la seule photo physique que j’avais d’elle !",
            "delay": 1.0,
            "window": 4.6,
            "options": [
                {
                    "key": "K_q",
                    "label": "Q",
                    "response": "On va la retrouver.",
                    "effect": "promise",
                    "kael_success": "Tu peux pas promettre ça.",
                    "kael_fail": "LA SEULE ! Vous entendez ?!"
                },
                {
                    "key": "K_d",
                    "label": "D",
                    "response": "Dis-nous où elle était.",
                    "effect": "focus",
                    "kael_success": "Sous mon oreiller. Toujours au même endroit.",
                    "kael_fail": "Je l’avais cachée ! Je l’avais cachée !"
                }
            ]
        },
        {
            "kael": "Léa a six ans. Six ans. Et j’ai même pas le droit de savoir si elle va bien.",
            "delay": 1.2,
            "window": 5.0,
            "options": [
                {
                    "key": "K_RETURN",
                    "label": "ENTRÉE",
                    "response": "Kael, regarde-moi.",
                    "effect": "anchor",
                    "kael_success": "Je... je te regarde.",
                    "kael_fail": "Et maintenant on m’enlève même ça."
                }
            ]
        },
        {
            "kael": "Qui savait ? Hein ? Qui savait que je la gardais là ?!",
            "delay": 1.0,
            "window": 4.5,
            "options": [
                {
                    "key": "K_z",
                    "label": "Z",
                    "response": "Personne ne t’accuse.",
                    "effect": "calm",
                    "kael_success": "Alors pourquoi j’ai l’impression que tout le monde me regarde ?",
                    "kael_fail": "Arrêtez de me regarder comme ça !"
                },
                {
                    "key": "K_s",
                    "label": "S",
                    "response": "Pose la chaise.",
                    "effect": "direct",
                    "kael_success": "Je... merde.",
                    "kael_fail": "Non ! Non, je pose rien !"
                }
            ]
        },
        {
            "kael": "Quelqu’un ici l’a prise. Quelqu’un ici est entré.",
            "delay": 1.0,
            "window": 4.5,
            "options": [
                {
                    "key": "K_q",
                    "label": "Q",
                    "response": "On ne sait pas encore.",
                    "effect": "reason",
                    "kael_success": "Moi je sais qu’elle a disparu.",
                    "kael_fail": "Ne me fais pas ce ton calme !"
                },
                {
                    "key": "K_d",
                    "label": "D",
                    "response": "Ne vise personne sans preuve.",
                    "effect": "firm",
                    "kael_success": "Je sais. Je sais, putain...",
                    "kael_fail": "Des preuves ?! Ma chambre est vide !"
                }
            ]
        },
        {
            "kael": "Je la regardais tous les soirs.",
            "delay": 1.3,
            "window": 4.5,
            "options": [
                {
                    "key": "K_SPACE",
                    "label": "ESPACE",
                    "response": "Je sais.",
                    "effect": "empathy",
                    "kael_success": "Non. Tu sais pas.",
                    "kael_fail": "Tous les soirs. Même quand j’arrivais pas à dormir."
                }
            ]
        },
        {
            "kael": "C’était pas un objet. C’était pas du matériel. C’était elle.",
            "delay": 1.2,
            "window": 5.0,
            "options": [
                {
                    "key": "K_RETURN",
                    "label": "ENTRÉE",
                    "response": "C’était important.",
                    "effect": "empathy",
                    "kael_success": "Oui.",
                    "kael_fail": "Vous allez encore dire que c’est juste une photo ?"
                },
                {
                    "key": "K_s",
                    "label": "S",
                    "response": "Assieds-toi.",
                    "effect": "direct",
                    "kael_success": "Je peux pas.",
                    "kael_fail": "Je peux pas m’asseoir !"
                }
            ]
        },
    ]

    def j801_stab_reset():
        store.j801_stab_step = 0
        store.j801_stab_success_count = 0
        store.j801_stab_fail_count = 0
        store.j801_stab_done = False
        store.j801_stab_time_left = J801_STAB_TOTAL_TIME
        store.j801_stab_next_event = 0.8
        store.j801_stab_prompt_active = False
        store.j801_stab_qte_time = 0.0
        store.j801_stab_qte_max_time = 4.0
        store.j801_stab_kael_line = "Kael tremble au milieu de la pièce."
        store.j801_stab_noam_line = ""
        store.j801_stab_status = "STABILISATION"
        store.j801_stab_flash = 0.0
        store.j801_stab_shake = 0
        store.j801_stab_result = False
        store.j801_stab_options = []
        store.j801_stab_selected_key = ""
        store.j801_stab_selected_label = ""
        store.j801_stab_selected_response = ""
        store.j801_stab_selected_effect = ""

    def j801_stab_glitch_text(text):
        chars = ["#", "%", "&", "@", "█", "▒", "▓", "░", "/", "\\", "0", "1"]
        result = []

        for c in text:
            if c == " ":
                result.append(c)
            elif random.random() < 0.35:
                result.append(random.choice(chars))
            else:
                result.append(c)

        return "".join(result)

    def j801_stab_start_event():
        if store.j801_stab_step >= len(j801_stab_events):
            return

        event = j801_stab_events[store.j801_stab_step]

        store.j801_stab_kael_line = event["kael"]
        store.j801_stab_noam_line = ""
        store.j801_stab_options = event["options"]
        store.j801_stab_qte_time = event["window"]
        store.j801_stab_qte_max_time = event["window"]
        store.j801_stab_prompt_active = True
        store.j801_stab_status = "RÉPONDS"
        store.j801_stab_flash = 0.12

    def j801_stab_press(key_name):
        if store.j801_stab_done:
            return

        if not store.j801_stab_prompt_active:
            return

        chosen = None

        for option in store.j801_stab_options:
            if option["key"] == key_name:
                chosen = option
                break

        if chosen is None:
            store.j801_stab_fail_count += 1
            store.j801_stab_status = "MAUVAISE RÉACTION"
            store.j801_stab_flash = 0.20
            store.j801_stab_shake = min(5, store.j801_stab_shake + 1)
            store.j801_stab_noam_line = ""
            store.j801_stab_kael_line = j801_stab_glitch_text(store.j801_stab_kael_line)
        else:
            store.j801_stab_success_count += 1
            store.j801_stab_status = "RÉPONSE"
            store.j801_stab_flash = 0.08
            store.j801_stab_shake = max(0, store.j801_stab_shake - 1)
            store.j801_stab_selected_key = chosen["key"]
            store.j801_stab_selected_label = chosen["label"]
            store.j801_stab_selected_response = chosen["response"]
            store.j801_stab_selected_effect = chosen["effect"]
            store.j801_stab_noam_line = "Noam : " + chosen["response"]
            store.j801_stab_kael_line = chosen["kael_success"]

        store.j801_stab_prompt_active = False
        store.j801_stab_qte_time = 0.0
        store.j801_stab_step += 1

        if store.j801_stab_step < len(j801_stab_events):
            store.j801_stab_next_event = j801_stab_events[store.j801_stab_step]["delay"]
        else:
            store.j801_stab_next_event = 2.2

    def j801_stab_timeout():
        if store.j801_stab_done:
            return

        if not store.j801_stab_prompt_active:
            return

        event = j801_stab_events[store.j801_stab_step]
        fallback = random.choice(event["options"])

        store.j801_stab_fail_count += 1
        store.j801_stab_status = "TROP TARD"
        store.j801_stab_flash = 0.25
        store.j801_stab_shake = min(5, store.j801_stab_shake + 1)
        store.j801_stab_noam_line = ""
        store.j801_stab_kael_line = fallback["kael_fail"]

        store.j801_stab_prompt_active = False
        store.j801_stab_qte_time = 0.0
        store.j801_stab_step += 1

        if store.j801_stab_step < len(j801_stab_events):
            store.j801_stab_next_event = j801_stab_events[store.j801_stab_step]["delay"]
        else:
            store.j801_stab_next_event = 2.2

    def j801_stab_tick():
        if store.j801_stab_done:
            return

        store.j801_stab_time_left = max(0.0, store.j801_stab_time_left - J801_STAB_TICK)

        if store.j801_stab_flash > 0.0:
            store.j801_stab_flash = max(0.0, store.j801_stab_flash - J801_STAB_TICK)

        if store.j801_stab_prompt_active:
            store.j801_stab_qte_time -= J801_STAB_TICK

            if store.j801_stab_qte_time <= 0.0:
                j801_stab_timeout()

        else:
            store.j801_stab_next_event -= J801_STAB_TICK

            if store.j801_stab_step < len(j801_stab_events) and store.j801_stab_next_event <= 0.0:
                j801_stab_start_event()

        if store.j801_stab_step >= len(j801_stab_events) and not store.j801_stab_prompt_active:
            store.j801_stab_next_event -= J801_STAB_TICK

            if store.j801_stab_next_event <= 0.0:
                store.j801_stab_done = True
                store.j801_stab_result = store.j801_stab_success_count >= 4
                store.j801_stab_kael_line = "…je voulais juste garder quelque chose d’elle…"
                store.j801_stab_noam_line = ""

        if store.j801_stab_time_left <= 0.0:
            store.j801_stab_done = True
            store.j801_stab_result = store.j801_stab_success_count >= 4
            store.j801_stab_kael_line = "…je voulais juste garder quelque chose d’elle…"
            store.j801_stab_noam_line = ""


transform j801_stab_cam_light:
    xoffset 0 yoffset 0
    linear 0.10 xoffset 2 yoffset -1
    linear 0.10 xoffset -2 yoffset 1
    linear 0.10 xoffset 0 yoffset 0
    pause 0.12
    repeat

transform j801_stab_cam_hard:
    xoffset 0 yoffset 0
    linear 0.04 xoffset 8 yoffset -4
    linear 0.04 xoffset -7 yoffset 3
    linear 0.04 xoffset 4 yoffset -5
    linear 0.04 xoffset 0 yoffset 0
    pause 0.08
    repeat

transform j801_stab_prompt_pulse:
    zoom 1.0
    alpha 1.0
    linear 0.08 zoom 1.08 alpha 0.88
    linear 0.08 zoom 1.0 alpha 1.0
    pause 0.12
    repeat


screen j801_stabilisation_screen():

    modal True
    zorder 280

    timer J801_STAB_TICK repeat True action Function(j801_stab_tick)

    key "K_z" action Function(j801_stab_press, "K_z")
    key "K_q" action Function(j801_stab_press, "K_q")
    key "K_s" action Function(j801_stab_press, "K_s")
    key "K_d" action Function(j801_stab_press, "K_d")
    key "K_SPACE" action Function(j801_stab_press, "K_SPACE")
    key "K_RETURN" action Function(j801_stab_press, "K_RETURN")
    key "K_KP_ENTER" action Function(j801_stab_press, "K_RETURN")

    add Solid("#07050B")

    if j801_stab_shake >= 3:
        add j801_stab_background at j801_stab_cam_hard:
            xalign 0.5
            yalign 0.5
            zoom 1.04
    else:
        add j801_stab_background at j801_stab_cam_light:
            xalign 0.5
            yalign 0.5
            zoom 1.02

    add Solid("#00000060")

    if j801_stab_flash > 0.0:
        add Solid("#FF334433")

    if j801_stab_shake >= 2:
        add Solid("#FF000014")

    for i in range(0, 1080, 9):
        add Solid("#FFFFFF05", xysize=(1920, 1)) xpos 0 ypos i

    add "kael fatigue":
        xpos 0.04
        ypos 0.05
        zoom 0.88

    frame:
        xalign 0.5
        yalign 0.055
        xsize 1180
        ysize 86
        background Solid("#120B18DD")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 2

            text "STABILISATION":
                xalign 0.5
                size 44
                color "#FFFFFF"
                bold True
                outlines [(3, "#0B1028", 0, 0)]

            text "Réponds vite. Ne le laisse pas repartir seul dans sa panique.":
                xalign 0.5
                size 20
                color "#D8B7FF"

    frame:
        xalign 0.62
        yalign 0.24
        xsize 1140
        ysize 270
        background Solid("#000000AA")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            text "Kael":
                xalign 0.5
                size 42
                color "#FFFFFF"
                bold True
                outlines [(4, "#0B1028", 0, 0)]

            text "[j801_stab_kael_line]":
                xalign 0.5
                xmaximum 1040
                size 46
                color "#FFFFFF"
                text_align 0.5
                outlines [(4, "#0B1028", 0, 0)]

    if j801_stab_noam_line != "":
        frame:
            xalign 0.62
            yalign 0.44
            xsize 980
            ysize 82
            background Solid("#081326DD")

            text "[j801_stab_noam_line]":
                xalign 0.5
                yalign 0.5
                xmaximum 900
                size 30
                color "#9DDFFF"
                text_align 0.5
                outlines [(3, "#0B1028", 0, 0)]

    if j801_stab_prompt_active:
        hbox:
            xalign 0.62
            yalign 0.66
            spacing 50

            for option in j801_stab_options:
                button:
                    xsize 440
                    ysize 230
                    background Solid("#10172CDD")
                    hover_background Solid("#263B68EE")
                    action Function(j801_stab_press, option["key"])
                    at j801_stab_prompt_pulse

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 18

                        text option["label"]:
                            xalign 0.5
                            size 78
                            color "#FFFFFF"
                            bold True
                            outlines [(5, "#0B1028", 0, 0)]

                        text option["response"]:
                            xalign 0.5
                            xmaximum 390
                            size 30
                            color "#D8B7FF"
                            text_align 0.5
                            outlines [(3, "#0B1028", 0, 0)]

        frame:
            xalign 0.62
            yalign 0.84
            xsize 760
            ysize 34
            background Solid("#000000AA")

            bar:
                xalign 0.5
                yalign 0.5
                xsize 700
                ysize 16
                value AnimatedValue(value=j801_stab_qte_time, range=j801_stab_qte_max_time, delay=0.05)
                left_bar Solid("#9DDFFF")
                right_bar Solid("#441522")

    frame:
        xalign 0.5
        yalign 0.94
        xsize 1080
        ysize 82
        background Solid("#050914DD")

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 55

            text "TEMPS [j801_stab_time_left:.1f]":
                size 24
                color "#DDF8FF"

            if j801_stab_status in ("TROP TARD", "MAUVAISE RÉACTION"):
                text "[j801_stab_status]":
                    size 24
                    color "#FFB3C1"
            else:
                text "[j801_stab_status]":
                    size 24
                    color "#9DDFFF"

            text "RÉPONSES [j801_stab_success_count]/[len(j801_stab_events)]":
                size 24
                color "#DDF8FF"

            if j801_stab_shake >= 3:
                text "CHAOS [j801_stab_shake]/5":
                    size 24
                    color "#FF6B9A"
            else:
                text "CHAOS [j801_stab_shake]/5":
                    size 24
                    color "#DDF8FF"

    if j801_stab_done:
        timer 1.2 action Return(j801_stab_result)


label j801_play_stabilisation:

    $ j801_stab_reset()
    $ result_stabilisation = renpy.call_screen("j801_stabilisation_screen")
    return result_stabilisation