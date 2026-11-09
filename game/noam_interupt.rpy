# Noam — cut-in d'interruption. Durée fixe : 2,00 secondes.
# Les images du corps et des yeux doivent partager le même canevas de dessin.
# Déclencheur public : call play_noam_interupt

# Transition générale : sortie rapide pendant les 0,25 dernières secondes.
transform noam_interupt_exit:
    alpha 1.0
    pause 1.74
    easein 0.26 alpha 0.0

# Fond : fondu d'entrée sans mouvement.
transform noam_interupt_bg_fade:
    alpha 0.0
    linear 0.38 alpha 1.0

# Une seule transformation commune au corps ET aux deux calques d'yeux :
# entrée depuis le bas, léger overshoot, recul élastique et micro-impact.
transform noam_interupt_rise:
    subpixel True
    yoffset 900
    zoom 1.0
    pause 0.50
    easeout 0.20 yoffset -24 zoom 1.055
    linear 0.035 xoffset -7
    linear 0.035 xoffset 6
    easeout 0.14 xoffset 0 yoffset 0 zoom 1.0

# Clignement unique, bref, optionnel (garder le regard fixe en passant False).
transform noam_interupt_eyes_open:
    alpha 1.0
    pause 1.18
    alpha 0.0
    pause 0.10
    alpha 1.0

transform noam_interupt_eyes_closed:
    alpha 0.0
    pause 1.18
    alpha 1.0
    pause 0.10
    alpha 0.0

screen noam_interupt_screen(blink=True):
    modal True
    zorder 300

    fixed at noam_interupt_exit:
        xfill True
        yfill True

        add "images/character/noam/interupt_background.png" at noam_interupt_bg_fade:
            xalign 0.5
            yalign 0.5

        fixed at noam_interupt_rise:
            xfill True
            yfill True
            add "images/character/noam/interupt_body.png":
                xalign 0.5
                yalign 0.5
            if blink:
                add "images/character/noam/interupt_yeux_ouvert.png" at noam_interupt_eyes_open:
                    xalign 0.5
                    yalign 0.5
                add "images/character/noam/interupt_yeux_ferme.png" at noam_interupt_eyes_closed:
                    xalign 0.5
                    yalign 0.5
            else:
                add "images/character/noam/interupt_yeux_ouvert.png":
                    xalign 0.5
                    yalign 0.5

    # Les effets utilisent le canal sound du jeu ; le chronométrage reste
    # entièrement piloté par cet écran, sans attente entre deux sons.
    timer 0.70 action Play("sound", "audio/sfx_interrupt_impact.wav")
    timer 1.70 action Play("sound", "audio/sfx_interrupt_outro.wav")
    timer 2.00 action Return()

label play_noam_interupt(blink=True):
    play sound "audio/sfx_interrupt_intro.wav"
    call screen noam_interupt_screen(blink=blink)
    return


# ---------------------------------------------------------------------------
# JOUR 1 — DUEL D'ARGUMENTS : Lysa / radio de la salle d'observation.
# 5 répliques, 4 secondes par réplique, boucle illimitée jusqu'au tir.
# L'animation Noam existante est la conséquence d'un tir réussi, pas un
# écran d'introduction. Aucun nouveau fichier graphique nécessaire.
# ---------------------------------------------------------------------------

init python:
    DAY1_RADIO_LINES = (
        "Cette radio fonctionne, j'en suis sûre. Je vais trouver comment l'utiliser.",
        "Kami a dit que les Dix Commandements ne s'appliquaient pas dans le Conclave.",
        "J'ai essayé plusieurs fréquences. Le signal existe, c'est juste l'appel qui est bloqué.",
        "Il n'y a aucune règle qui nous interdit de contacter quelqu'un à l'extérieur !",
        "Je vais essayer encore une fois. Il doit bien y avoir un moyen de joindre ma sœur.",
    )

    DAY1_RADIO_ARGUMENTS = (
        ("reglement_conclave", "Règlement du Conclave", "01"),
        ("commandements", "Les 10 Commandements", "02"),
        ("surveillance", "La surveillance de Kami", "03"),
        ("vote_secret", "Le secret des votes", "04"),
        ("securite", "La sécurité de la station", "05"),
    )

    DAY1_RADIO_TARGET_LINE = 3
    DAY1_RADIO_MAX_SHOTS = 3


# ---------------------------------------------------------------------------
# Duel radio V2 — une vraie cible à toucher, des expressions changeantes,
# une barre de temps visible et une réponse audiovisuelle pour chaque tir.
# La logique narrative reste identique : 5 phrases, 3 tirs, même argument
# gagnant et même cut-in de Noam au succès.
# ---------------------------------------------------------------------------

init python:
    DAY1_RADIO_EXPRESSIONS = ("determine", "reflexion", "colere", "opposition", "fatigue")

    def day1_radio_miss_reason(argument_id, line_index):
        if argument_id == "reglement_conclave":
            return "LYSA : « Attends au moins que je termine ma phrase ! »"
        if line_index == DAY1_RADIO_TARGET_LINE:
            return "LYSA : « Tu me contredis avec ça ? Quel rapport ?! »"
        return "LYSA : « Ça n'explique toujours pas pourquoi l'appel échoue ! »"


transform day1_radio_lysa_arrive:
    subpixel True
    alpha 0.0
    xoffset -70
    easeout 0.38 alpha 1.0 xoffset 0

transform day1_radio_dialogue_arrive:
    subpixel True
    alpha 0.0
    xoffset 55
    zoom 0.98
    easeout 0.19 alpha 1.0 xoffset -8 zoom 1.015
    easeout 0.11 xoffset 0 zoom 1.0

transform day1_radio_selector_pulse:
    alpha 0.6
    ease 0.35 alpha 1.0
    ease 0.35 alpha 0.6
    repeat

transform day1_radio_shot_flash:
    alpha 0.0
    linear 0.05 alpha 0.32
    linear 0.26 alpha 0.0

transform day1_radio_shot_trail:
    subpixel True
    xzoom 0.0
    alpha 1.0
    easeout 0.15 xzoom 1.0
    pause 0.10
    linear 0.17 alpha 0.0

transform day1_radio_impact_stamp:
    subpixel True
    alpha 0.0
    zoom 1.42
    rotate -5
    pause 0.08
    easeout 0.15 alpha 1.0 zoom 1.0 rotate 0
    pause 0.22
    linear 0.15 alpha 0.0

# Interface de confrontation : inspiration des duels de réfutation
# narratifs, mais composition et ressources propres à Kami's Desires.
# Coordonnées basées sur la scène 1920x1080 du jeu.
screen noam_interupt_radio_duel():
    modal True
    zorder 305

    default line_index = 0
    default line_elapsed = 0.0
    default selected_argument = None
    default shots = 0
    default shot_state = ""
    default shot_feedback = ""

    # Un seul compte à rebours : évite la désynchronisation de deux timers.
    if shot_state == "":
        timer 0.05 repeat True action If(
            line_elapsed >= 3.95,
            [
                SetScreenVariable("line_index", (line_index + 1) % len(DAY1_RADIO_LINES)),
                SetScreenVariable("line_elapsed", 0.0)
            ],
            SetScreenVariable("line_elapsed", min(4.0, line_elapsed + 0.05))
        )
    else:
        timer 0.68 action If(
            shot_state == "hit",
            Return(("success", selected_argument)),
            If(
                shot_state == "fail",
                Return(("failure", selected_argument)),
                [
                    SetScreenVariable("shot_state", ""),
                    SetScreenVariable("line_elapsed", 0.0)
                ]
            )
        )

    # Le duel se déroule réellement dans le décor où se trouvent les héros.
    add "bg_observation"
    add Solid("#0806108c")

    # Cadre supérieur : bandes et diagonales minimalistes, sans panneaux
    # opaques recouvrant toute la scène.
    add Solid("#0a0c1be0"):
        xpos 0
        ypos 0
        xsize 1920
        ysize 97
    add Solid("#f14467"):
        xpos 0
        ypos 96
        xsize 1920
        ysize 4
    add Solid("#0c0c1ab0"):
        xpos 0
        ypos 904
        xsize 1920
        ysize 176

    text "OBJECTION  /  RADIO BLOQUÉE":
        xpos 61
        ypos 26
        size 33
        color "#ffffff"
        font "fonts/Rajdhani-SemiBold.ttf"
    text "SALLE D'OBSERVATION     •     DUEL 01":
        xpos 1270
        ypos 34
        size 22
        color "#ffc3cf"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Noam occupe l'avant-plan gauche, comme l'accusateur dans une
    # confrontation. Lysa reste visible au fond, sur la droite.
    add Transform(character_image("noam", "determine"), zoom=1.13):
        xpos -125
        ypos 126
    add Solid("#f24a66a8"):
        xpos 414
        ypos 123
        xsize 5
        ysize 730

    for number in range(len(DAY1_RADIO_LINES)):
        if line_index == number:
            add Transform(character_image("lysa", DAY1_RADIO_EXPRESSIONS[number]), zoom=0.61) at day1_radio_lysa_arrive:
                xpos 1513
                ypos 309

    # Déclaration de Lysa, suspendue sur le décor et encadrée comme une
    # affirmation à réfuter. Elle reste la véritable cible cliquable.
    add Solid("#170a17db"):
        xpos 755
        ypos 127
        xsize 1085
        ysize 224
    add Solid("#f4546d"):
        xpos 755
        ypos 127
        xsize 1085
        ysize 5

    text "AFFIRMATION DE LYSA    //    [line_index + 1] / 5":
        xpos 790
        ypos 147
        size 25
        color "#ffb0be"
        font "fonts/Rajdhani-SemiBold.ttf"

    for number in range(len(DAY1_RADIO_LINES)):
        if line_index == number:
            button at day1_radio_dialogue_arrive:
                xpos 775
                ypos 191
                xsize 1040
                ysize 153
                background Solid("#20152488")
                hover_background Solid("#77243cdd")
                padding (20, 15)
                sensitive (selected_argument is not None and shot_state == "")
                action If(
                    selected_argument == "reglement_conclave" and line_index == DAY1_RADIO_TARGET_LINE,
                    [
                        SetScreenVariable("shot_feedback", "OBJECTION ! LE RÈGLEMENT INTERDIT D'INITIER UN APPEL."),
                        SetScreenVariable("shot_state", "hit"),
                        Play("sound", "audio/sfx_interrupt_impact.wav")
                    ],
                    [
                        SetScreenVariable("shot_feedback", day1_radio_miss_reason(selected_argument, line_index)),
                        SetScreenVariable("shots", shots + 1),
                        SetScreenVariable("shot_state", "fail" if shots + 1 >= DAY1_RADIO_MAX_SHOTS else "miss"),
                        Play("sound", "audio/sfx_beep.mp3")
                    ]
                )
                vbox:
                    spacing 9
                    text DAY1_RADIO_LINES[line_index]:
                        xsize 985
                        size 35
                        color "#ffffff"
                        outlines [(2, "#120814", 0, 0)]
                        font "fonts/Rajdhani-SemiBold.ttf"
                    text ("▶  CLIQUE POUR RÉFUTER" if selected_argument else "CHOISIS UNE PREUVE POUR ARMÉR TON OBJECTION"):
                        size 20
                        color ("#8bf5ff" if selected_argument else "#c9adba")
                        font "fonts/Rajdhani-SemiBold.ttf"

    # Indicateurs des cinq répliques et de celle actuellement prononcée.
    hbox:
        xpos 790
        ypos 365
        spacing 10
        for number in range(len(DAY1_RADIO_LINES)):
            add Solid("#fc6178" if number == line_index else "#65535e"):
                xsize 198
                ysize 6

    text "PREUVES   //   CHOISIS AVEC LA SOURIS, PUIS CLIQUE SUR SA PHRASE":
        xpos 484
        ypos 414
        size 25
        color "#ffffff"
        outlines [(2, "#100a17", 0, 0)]
        font "fonts/Rajdhani-SemiBold.ttf"

    # Cinq propositions en bande horizontale, rappelant la sélection
    # verticale des preuves du modèle, sans lui emprunter ses assets.
    for number, argument in enumerate(DAY1_RADIO_ARGUMENTS):
        $ chosen = (selected_argument == argument[0])
        button:
            xpos 474
            ypos (461 + number * 79)
            xsize 920
            ysize 71
            background Solid("#254e5eee" if chosen else "#111322e3")
            hover_background Solid("#49334aed")
            insensitive_background Solid("#171220c9")
            sensitive (shot_state == "")
            action SetScreenVariable("selected_argument", argument[0])
            padding (19, 7)
            hbox:
                spacing 23
                yalign 0.5
                text argument[2]:
                    size 25
                    color ("#88f7ff" if chosen else "#b4b9c7")
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                text argument[1]:
                    size 30
                    color "#ffffff"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                if chosen:
                    text "◀ PRÊT":
                        size 22
                        color "#8bf6ff"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        yalign 0.5

    # Bas d'écran façon tableau de duel : horloge centrale, avertissement
    # rouge, énergie / essais. Le chrono fonctionne sur la réplique active.
    add Solid("#c62a45"):
        xpos 635
        ypos 923
        xsize 650
        ysize 62
    add Solid("#25151ef0"):
        xpos 649
        ypos 930
        xsize 620
        ysize 48
    text "TEMPS  [ '%.2f' % max(0.0, 4.0 - line_elapsed) ] s":
        xpos 830
        ypos 934
        size 34
        color "#ffffff"
        font "fonts/Rajdhani-SemiBold.ttf"
    add Solid("#3c1821"):
        xpos 649
        ypos 1004
        xsize 620
        ysize 17
    add Solid("#6bf575" if line_elapsed < 3.1 else "#fc5565"):
        xpos 649
        ypos 1004
        xsize max(0, int(620 * (1.0 - line_elapsed / 4.0)))
        ysize 17

    text "OBJECTIONS  [DAY1_RADIO_MAX_SHOTS - shots] / [DAY1_RADIO_MAX_SHOTS]":
        xpos 1362
        ypos 950
        size 29
        color "#ffffff"
        font "fonts/Rajdhani-SemiBold.ttf"
    text "NOAM  VS  LYSA":
        xpos 73
        ypos 961
        size 27
        color "#ffb8c5"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Impact uniquement après le clic sur la phrase. Le cut-in animé
    # existant de Noam reste la récompense après une objection valide.
    if shot_state != "":
        add Solid("#ffffff" if shot_state == "hit" else "#ff4267") at day1_radio_shot_flash
        add Solid("#8cf4ff" if shot_state == "hit" else "#fd5d75") at day1_radio_shot_trail:
            xpos 435
            ypos 320
            xsize 1370
            ysize 9
        text ("OBJECTION !" if shot_state == "hit" else "RATÉ !"):
            xpos 815
            ypos 243
            size (91 if shot_state == "hit" else 72)
            color ("#a4fbff" if shot_state == "hit" else "#ff7286")
            outlines [(3, "#10070c", 0, 0)]
            font "fonts/Rajdhani-SemiBold.ttf"
            at day1_radio_impact_stamp
        add Solid("#0a091bef"):
            xpos 480
            ypos 819
            xsize 943
            ysize 75
        text shot_feedback:
            xpos 508
            ypos 835
            xsize 897
            size 25
            color ("#85fbff" if shot_state == "hit" else "#ffd0d7")
            font "fonts/Rajdhani-SemiBold.ttf"


label day1_noam_radio_interruption:
    call screen noam_interupt_radio_duel
    $ _day1_radio_shot = _return
    if _day1_radio_shot[0] == "success":
        # Le cut-in de Noam surgit SEULEMENT quand le joueur trouve
        # la bonne réplique et y oppose le bon argument.
        call play_noam_interupt(blink=True) from _call_day1_radio_noam_interupt_success
    return _day1_radio_shot
