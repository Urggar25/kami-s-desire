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
# JOUR 1 : INTERRUPTION / CHOIX D'UN ARGUMENT
# La cinématique d'entrée reste le cut-in existant (corps + yeux animés).
# Cet écran prend ensuite le relais, avec les mêmes calques repositionnés.
# ---------------------------------------------------------------------------

transform noam_interupt_argument_arrive:
    alpha 0.0
    xoffset 80
    easeout 0.30 alpha 1.0 xoffset 0

transform noam_interupt_argument_portrait:
    alpha 0.0
    xoffset -95
    zoom 0.72
    easeout 0.38 alpha 1.0 xoffset 0

transform noam_interupt_argument_pulse:
    alpha 0.35
    ease 0.65 alpha 0.85
    ease 0.65 alpha 0.35
    repeat

screen noam_interupt_argument_screen():
    modal True
    zorder 305

    # L'écran de sélection ne réutilise pas l'animation de sortie du cut-in :
    # les trois calques restent assemblés à gauche, sans masquer les réponses.
    add Solid("#020913f5")
    add "images/character/noam/interupt_background.png":
        xalign 0.5
        yalign 0.5
        alpha 0.37

    add Solid("#57d9ff") at noam_interupt_argument_pulse:
        xpos 0 ypos 148 xsize 9 ysize 760

    fixed at noam_interupt_argument_portrait:
        xpos -270 ypos 175
        xysize (1040, 830)
        add Transform("images/character/noam/interupt_body.png", zoom=0.72)
        add Transform("images/character/noam/interupt_yeux_ouvert.png", zoom=0.72)

    frame at noam_interupt_argument_arrive:
        xpos 725 ypos 102
        xsize 1115 ysize 880
        background Solid("#081927ed")
        padding (40, 34)

        vbox:
            spacing 18

            text "NOAM  //  INTERRUPTION":
                size 25
                color "#55d8ff"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 3

            text "QU'EST-CE QUI INTERDIT CET APPEL ?":
                size 43
                color "#f1faff"
                font "fonts/Rajdhani-SemiBold.ttf"
                xsize 985

            text "Choisis l'argument que Noam doit opposer à Lysa.":
                size 24
                color "#aac6d8"
                xsize 985

            null height 12

            for number, argument in enumerate((
                ("reglement_conclave", "Règlement du Conclave"),
                ("commandements", "Les 10 Commandements"),
                ("surveillance", "La surveillance de Kami"),
                ("vote_secret", "Le secret des votes"),
                ("securite", "La sécurité de la station"),
            )):
                button:
                    xfill True
                    ysize 97
                    background Solid("#123044")
                    hover_background Solid("#245979")
                    padding (25, 13)
                    action Return(argument[0])

                    hbox:
                        spacing 24
                        yalign 0.5

                        text "{:02d}".format(number + 1):
                            color "#5ecbfa"
                            size 28
                            font "fonts/Rajdhani-SemiBold.ttf"
                            yalign 0.5

                        text argument[1]:
                            color "#f0f9ff"
                            size 31
                            font "fonts/Rajdhani-SemiBold.ttf"
                            yalign 0.5


label day1_noam_radio_interruption:
    # Animation réutilisable existante : background / body / yeux (clignement).
    call play_noam_interupt(blink=True) from _call_day1_radio_noam_interupt
    call screen noam_interupt_argument_screen
    return _return
