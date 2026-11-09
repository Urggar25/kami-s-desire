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

screen noam_interupt_radio_duel():
    modal True
    zorder 305

    default line_index = 0
    default line_elapsed = 0.0
    default selected_argument = None
    default shots = 0
    default shot_state = ""
    default shot_feedback = ""

    # Les lignes sont répétées, mais le compte à rebours est réellement
    # visible. Pendant l'impact, la réplique et les contrôles sont gelés.
    if shot_state == "":
        timer 0.05 repeat True action SetScreenVariable("line_elapsed", min(4.0, line_elapsed + 0.05))
        timer 4.0 repeat True action [
            SetScreenVariable("line_index", (line_index + 1) % len(DAY1_RADIO_LINES)),
            SetScreenVariable("line_elapsed", 0.0),
        ]
    else:
        timer 0.68 action If(
            shot_state == "hit",
            Return(("success", selected_argument)),
            If(
                shot_state == "fail",
                Return(("failure", selected_argument)),
                [SetScreenVariable("shot_state", ""), SetScreenVariable("line_elapsed", 0.0)]
            )
        )

    # Fond existant, assombri pour faire ressortir l'affrontement.
    add Solid("#070715")
    add "images/character/noam/interupt_background.png":
        xalign 0.5
        yalign 0.5
        alpha 0.44
    add Solid("#09091ad8"):
        xpos 422
        ypos 34
        xsize 1458
        ysize 1010
    add Solid("#d64cf4"):
        xpos 418
        ypos 0
        xsize 5
        ysize 1080

    # Lysa n'est plus une illustration immobile : sa pose change selon
    # l'argument qu'elle défend. Chaque nouvelle image est réintroduite.
    for number in range(len(DAY1_RADIO_LINES)):
        if line_index == number:
            add Transform(character_image("lysa", DAY1_RADIO_EXPRESSIONS[number]), zoom=0.82) at day1_radio_lysa_arrive:
                xpos 15
                ypos 130

    text "OBJECTION // SALLE D'OBSERVATION":
        xpos 500
        ypos 67
        size 31
        color "#f075fa"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "DUEL 01  /  LYSA":
        xpos 1520
        ypos 74
        size 23
        color "#b5abc8"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "RÉPLIQUE [line_index + 1] / [len(DAY1_RADIO_LINES)]":
        xpos 510
        ypos 141
        size 27
        color "#ffffff"
        font "fonts/Rajdhani-SemiBold.ttf"

    # La phrase est directement cliquable : le joueur tire SUR elle.
    # Boucle conditionnelle : l'ATL d'apparition repart à chaque réplique.
    for number in range(len(DAY1_RADIO_LINES)):
        if line_index == number:
            button at day1_radio_dialogue_arrive:
                xpos 500
                ypos 206
                xsize 1330
                ysize 225
                background Solid("#29113fea" if selected_argument else "#221432ef")
                hover_background Solid("#513077")
                padding (29, 19)
                sensitive selected_argument is not None and shot_state == ""
                action If(
                    selected_argument == "reglement_conclave" and line_index == DAY1_RADIO_TARGET_LINE,
                    [
                        SetScreenVariable("shot_feedback", "OBJECTION ! Le règlement interdit d'émettre un appel."),
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
                    spacing 16
                    text "CIBLE  //  [ 'CLIQUE POUR TIRER' if selected_argument else 'ARME UN ARGUMENT CI-DESSOUS' ]":
                        size 19
                        color "#67eaff" if selected_argument else "#db9ee6"
                        font "fonts/Rajdhani-SemiBold.ttf"
                    text DAY1_RADIO_LINES[line_index]:
                        xsize 1245
                        size 38
                        color "#ffffff"
                        font "fonts/Rajdhani-SemiBold.ttf"

    # Jauge qui se vide pendant les 4 s de la réplique active.
    add Solid("#433352"):
        xpos 510
        ypos 449
        xsize 1310
        ysize 11
    add Solid("#69e7ff" if line_elapsed < 3.1 else "#ff6689"):
        xpos 510
        ypos 449
        xsize max(0, int(1310 * (1.0 - line_elapsed / 4.0)))
        ysize 11

    hbox:
        xpos 510
        ypos 480
        spacing 11
        for number in range(len(DAY1_RADIO_LINES)):
            add Solid("#e65af8" if number == line_index else "#5a466f"):
                xsize 253
                ysize 5

    text "01  CHOISIS UNE PREUVE      02  CLIQUE SUR LA PHRASE AU BON MOMENT":
        xpos 508
        ypos 534
        size 24
        color "#e2d5f3"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Argumentaire compact en deux colonnes. L'état sélectionné est
    # évident et les cartes sont désactivées pendant l'impact.
    for number, argument in enumerate(DAY1_RADIO_ARGUMENTS):
        $ chosen = selected_argument == argument[0]
        button:
            xpos (505 + (number % 2) * 666)
            ypos (600 + (number // 2) * 104)
            xsize 642
            ysize 91
            background Solid("#23405e" if chosen else "#1d1835")
            hover_background Solid("#354566")
            insensitive_background Solid("#262239")
            sensitive shot_state == ""
            action SetScreenVariable("selected_argument", argument[0])
            padding (17, 10)

            hbox:
                spacing 15
                yalign 0.5
                text argument[2]:
                    size 25
                    color "#74edff" if chosen else "#a69abf"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                text argument[1]:
                    size 29
                    color "#ffffff" if chosen else "#e4ddf5"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                if chosen:
                    text "●":
                        size 28
                        color "#76f0ff"
                        yalign 0.5
                        at day1_radio_selector_pulse

    # Sixième emplacement : rappel des tirs, sans bouton géant inutile.
    add Solid("#0d1028d8"):
        xpos 1171
        ypos 808
        xsize 642
        ysize 91
    text "TIRS RESTANTS : [DAY1_RADIO_MAX_SHOTS - shots] / [DAY1_RADIO_MAX_SHOTS]":
        xpos 1193
        ypos 830
        size 29
        color "#ffb7cb"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "L'ARGUMENT NE PART QUE SI TU CLIQUES SUR LA RÉPLIQUE DE LYSA.":
        xpos 510
        ypos 958
        size 22
        color "#c5b7df"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Tir visible et réaction contextualisée, avant de valider la réussite
    # ou le dernier échec. Aucune autre interaction n'est possible ici.
    if shot_state != "":
        add Solid("#67ecff" if shot_state == "hit" else "#ff437f") at day1_radio_shot_flash
        add Solid("#83f5ff" if shot_state == "hit" else "#ff6487") at day1_radio_shot_trail:
            xpos 490
            ypos 323
            xsize 1334
            ysize 7
        text "OBJECTION !" if shot_state == "hit" else "ARGUMENT REJETÉ":
            xpos 600
            ypos 247
            size 76 if shot_state == "hit" else 56
            color "#85f7ff" if shot_state == "hit" else "#ff7f9d"
            outlines [(3, "#0a071d", 0, 0)]
            font "fonts/Rajdhani-SemiBold.ttf"
            at day1_radio_impact_stamp
        add Solid("#0b071df2"):
            xpos 505
            ypos 919
            xsize 1320
            ysize 90
        text shot_feedback:
            xpos 530
            ypos 943
            xsize 1255
            size 27
            color "#86edff" if shot_state == "hit" else "#ffb6c9"
            font "fonts/Rajdhani-SemiBold.ttf"


label day1_noam_radio_interruption:
    call screen noam_interupt_radio_duel
    $ _day1_radio_shot = _return
    if _day1_radio_shot[0] == "success":
        # Le cut-in de Noam surgit SEULEMENT quand le joueur trouve
        # la bonne réplique et y oppose le bon argument.
        call play_noam_interupt(blink=True) from _call_day1_radio_noam_interupt_success
    return _day1_radio_shot
