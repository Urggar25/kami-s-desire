# -----------------------------------------------------------------------
# LIENS — ELIAS
# -----------------------------------------------------------------------

default elias_link = 0


label ELIAS_LINK_INTERACT:

    menu:
        "Passer du temps avec Elias ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if elias_link == 0:
        jump elias_link_1
    elif elias_link == 1:
        jump elias_link_2
    elif elias_link == 2:
        jump elias_link_3
    elif elias_link == 3:
        jump elias_link_4
    elif elias_link == 4:
        jump elias_link_5

    if last_room_label:
        jump expression last_room_label
    return


label elias_link_1:

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "neutre", 0.70)

    elias "Tu arrives pile à l'heure."
    elias "Je fais toujours les mêmes séries."
    elias "Même cadence, mêmes gestes."

    "Il regarde sa montre, pas moi."
    "Ses doigts comptent dans le vide."

    elias "Si je saute une séquence, je perds le rythme."
    elias "C'est plus simple de suivre un plan."

    think "Il parle du corps, mais c'est autre chose qu'il aligne."

    $ elias_link = 1

    jump FREE_TIME_END


label elias_link_2:

    scene bg_maintenance at adaptive_fullscreen

    $ showP("elias", "ecoute", 0.65)

    elias "Le bras d'articulation a pris du jeu."
    elias "Trois millimètres."
    elias "C'est suffisant pour fausser tout l'angle."

    "Il resserre une vis. Trop fort."

    elias "Les approximations finissent toujours par coûter plus cher."
    elias "On croit gagner du temps, et on perd tout."

    "Sa voix claque un peu trop."

    $ elias_link = 2

    jump FREE_TIME_END


label elias_link_3:

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "reflechit", 0.70)

    elias "Je devais réorganiser les stations."
    elias "Mais il manque des pièces."
    elias "On fera avec."

    "Il range pourtant chaque poids au millimètre."

    elias "Ce n'est pas un échec."
    elias "Juste un compromis."

    "Il serre la mâchoire sans s'en rendre compte."

    $ elias_link = 3

    jump FREE_TIME_END


label elias_link_4:

    scene bg_maintenance at adaptive_fullscreen

    $ showP("elias", "neutre", 0.68)

    elias "Les règles évitent les discussions inutiles."
    elias "Tout le monde sait quoi faire."
    elias "Pas besoin d'interpréter les intentions."

    "Il trace une ligne imaginaire sur une table."

    elias "Le vote, c'est bien."
    elias "Si le cadre est clair."

    think "Il parle d'organisation. Pas de lui."

    $ elias_link = 4

    jump FREE_TIME_END


label elias_link_5:

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "fatigue", 0.70)

    "La salle est presque vide."
    "Il essuie une barre, lentement."

    elias "Je dors mal quand les choses sont mal définies."
    elias "C'est tout."

    "Ses yeux restent fixes, comme s'il comptait encore."

    $ elias_link = 5

    jump FREE_TIME_END
