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


transform day1_radio_lysa_arrive:
    alpha 0.0
    xoffset -55
    easeout 0.40 alpha 1.0 xoffset 0

transform day1_radio_dialogue_arrive:
    alpha 0.0
    yoffset 16
    easeout 0.25 alpha 1.0 yoffset 0

transform day1_radio_selector_pulse:
    alpha 0.55
    ease 0.40 alpha 1.0
    ease 0.40 alpha 0.55
    repeat


screen noam_interupt_radio_duel():
    modal True
    zorder 305

    default line_index = 0
    default selected_argument = None
    default shots = 0
    default feedback = ""

    # Le timer est répétitif et ne provoque jamais de fin automatique.
    # Chaque phrase occupe exactement 4 s (sauf si le joueur quitte
    # l'écran par un tir réussi ou trois tirs manqués).
    timer 4.0 repeat True action [
        SetScreenVariable("line_index", (line_index + 1) % len(DAY1_RADIO_LINES)),
        SetScreenVariable("feedback", ""),
    ]

    add Solid("#090716")
    add "images/character/noam/interupt_background.png":
        xalign 0.5
        yalign 0.5
        alpha 0.62

    # Lysa reste présente pendant que son dialogue défile.
    add Transform(character_image("lysa", "blase"), zoom=0.80) at day1_radio_lysa_arrive:
        xpos 45
        ypos 132

    # Un panneau sombre derrière la bulle et les cartes maintient la
    # lisibilité sans cacher entièrement la direction artistique.
    add Solid("#050912dd"):
        xpos 540
        ypos 110
        xsize 1310
        ysize 835

    text "OBJECTION  //  SALLE D'OBSERVATION":
        xpos 585
        ypos 127
        size 28
        color "#f86cff"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "LYSA  •  RÉPLIQUE [line_index + 1] / 5":
        xpos 588
        ypos 187
        size 24
        color "#f3f7ff"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Bulle de la réplique active, celle que le joueur doit viser.
    frame at day1_radio_dialogue_arrive:
        xpos 572
        ypos 230
        xsize 1248
        ysize 184
        background Solid("#250d41ee")
        padding (26, 21)

        vbox:
            spacing 8
            text "CE QU'ELLE AFFIRME":
                size 19
                color "#f681ff"
            text DAY1_RADIO_LINES[line_index]:
                xsize 1180
                size 30
                color "#ffffff"
                font "fonts/Rajdhani-SemiBold.ttf"

    hbox:
        xpos 596
        ypos 427
        spacing 9
        for number in range(5):
            add Solid("#ef5dff" if number == line_index else "#67517b"):
                xsize 233
                ysize 6

    text "CHOISIS TON ARGUMENT, PUIS TIRE SUR LA RÉPLIQUE AU BON MOMENT":
        xpos 590
        ypos 469
        size 23
        color "#d8c7ee"
        font "fonts/Rajdhani-SemiBold.ttf"

    # Les cinq cartes sont cliquables sans interrompre le défilement.
    for number, argument in enumerate(DAY1_RADIO_ARGUMENTS):
        $ chosen = selected_argument == argument[0]
        button:
            xpos 580
            ypos (520 + number * 68)
            xsize 1238
            ysize 59
            background Solid("#273c62" if chosen else "#1a1234")
            hover_background Solid("#334d7a")
            action SetScreenVariable("selected_argument", argument[0])
            padding (16, 4)

            hbox:
                spacing 19
                yalign 0.5
                text argument[2]:
                    size 24
                    color "#ff7af7" if chosen else "#a0a6c0"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                text argument[1]:
                    size 28
                    color "#ffffff" if chosen else "#dfdcf6"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    yalign 0.5
                if chosen:
                    text "◀ ARMÉ":
                        size 22
                        color "#50ecff"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        yalign 0.5

    # Le bouton tire l'argument sélectionné sur la phrase ACTUELLE.
    # Une mauvaise cible ou un mauvais argument consomme une tentative,
    # mais aucun tir n'est imposé : les cinq phrases tournent à l'infini.
    button:
        xpos 1230
        ypos 891
        xsize 590
        ysize 92
        background Solid("#9426a1" if selected_argument else "#333044")
        hover_background Solid("#ca36cf" if selected_argument else "#333044")
        padding (18, 9)
        sensitive selected_argument is not None
        action If(
            selected_argument == "reglement_conclave"
            and line_index == DAY1_RADIO_TARGET_LINE,
            Return(("success", selected_argument)),
            [
                SetScreenVariable("shots", shots + 1),
                If(
                    shots + 1 >= DAY1_RADIO_MAX_SHOTS,
                    Return(("failure", selected_argument)),
                    SetScreenVariable("feedback", "Raté ! Mauvaise phrase ou mauvais argument. Réessaie.")
                )
            ]
        )
        text "TIRER L'ARGUMENT  ▶":
            xalign 0.5
            yalign 0.5
            size 33
            color "#ffffff"
            font "fonts/Rajdhani-SemiBold.ttf"

    text "TIRS RESTANTS : [DAY1_RADIO_MAX_SHOTS - shots]":
        xpos 596
        ypos 923
        size 22
        color "#ffb9c8"
        font "fonts/Rajdhani-SemiBold.ttf"

    if feedback:
        text feedback:
            xpos 580
            ypos 997
            xsize 1240
            size 22
            color "#ffb7cb"
            font "fonts/Rajdhani-SemiBold.ttf"


label day1_noam_radio_interruption:
    call screen noam_interupt_radio_duel
    $ _day1_radio_shot = _return
    if _day1_radio_shot[0] == "success":
        # Le cut-in de Noam surgit SEULEMENT quand le joueur trouve
        # la bonne réplique et y oppose le bon argument.
        call play_noam_interupt(blink=True) from _call_day1_radio_noam_interupt_success
    return _day1_radio_shot
