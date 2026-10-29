# Cut-in d'interruption de Noam — durée totale fixe : 2 secondes.
# Les quatre textures restent indépendantes, pour préserver le clignement.
# Les calques body/yeux partagent exactement le même transform de déplacement.

transform noam_interupt_bg_fade:
    alpha 0.0
    linear 0.38 alpha 1.0

transform noam_interupt_rise:
    subpixel True
    yoffset 900
    pause 0.50
    easeout 0.23 yoffset 0
    yoffset 0

transform noam_interupt_eyes_open:
    alpha 1.0
    pause 1.12
    alpha 0.0
    pause 0.12
    alpha 1.0

transform noam_interupt_eyes_closed:
    alpha 0.0
    pause 1.12
    alpha 1.0
    pause 0.12
    alpha 0.0

screen noam_interupt_screen():
    modal True
    zorder 300

    # Les textures sont centrées sur un même repère, sans rééchantillonnage
    # individuel des yeux : les PNG sont supposés exportés sur le même canevas.
    add "images/character/noam/interupt_background.png" at noam_interupt_bg_fade:
        xalign 0.5
        yalign 0.5

    fixed at noam_interupt_rise:
        xfill True
        yfill True
        add "images/character/noam/interupt_body.png":
            xalign 0.5
            yalign 0.5
        add "images/character/noam/interupt_yeux_ouvert.png" at noam_interupt_eyes_open:
            xalign 0.5
            yalign 0.5
        add "images/character/noam/interupt_yeux_ferme.png" at noam_interupt_eyes_closed:
            xalign 0.5
            yalign 0.5

    # Pas de clic nécessaire : fin de l'animation à 2.00 s précisément.
    timer 2.0 action Return()

label play_noam_interupt:
    call screen noam_interupt_screen
    return
