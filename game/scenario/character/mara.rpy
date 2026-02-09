# -----------------------------------------------------------------------
# LIENS — MARA
# -----------------------------------------------------------------------

default mara_link = 0


label MARA_LINK_INTERACT:

    menu:
        "Passer du temps avec Mara ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if mara_link == 0:
        jump mara_link_1
    elif mara_link == 1:
        jump mara_link_2
    elif mara_link == 2:
        jump mara_link_3
    elif mara_link == 3:
        jump mara_link_4
    elif mara_link == 4:
        jump mara_link_5

    if last_room_label:
        jump expression last_room_label
    return


label mara_link_1:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "sourire", 0.60)

    mara "Tiens, toi."
    mara "T'es venu pour le café ou pour les ragots ?"

    "Elle laisse planer la question, amusée."

    mara "Je plaisante."
    mara "Enfin… pas complètement."

    think "Elle observe plus qu'elle ne parle."

    $ mara_link = 1

    jump FREE_TIME_END


label mara_link_2:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)

    mara "Tomas fait toujours semblant de ne rien écouter."
    mara "Elen se croit invisible."
    mara "Et Kael…"

    "Elle hausse les épaules avec un sourire en coin."

    mara "Chacun joue son rôle."
    mara "On dirait un concours, non ?"

    $ mara_link = 2

    jump FREE_TIME_END


label mara_link_3:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "colere", 0.60)

    mara "Tu sais ce qui m'agace ?"
    mara "Les gens qui pensent qu'ils peuvent me contredire devant tout le monde."

    "Elle se reprend aussitôt, sourire revenu."

    mara "C'est rien."
    mara "Juste une mauvaise journée."

    "Ses doigts tapent sur la table plus vite que son ton."

    $ mara_link = 3

    jump FREE_TIME_END


label mara_link_4:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)

    mara "Tu sais, la réputation, c'est un costume."
    mara "On le porte parce que tout le monde regarde."
    mara "Et quand on l'enlève, il n'y a plus personne."

    "Elle parle comme d'un jeu sérieux."

    mara "Je préfère qu'on sache à quoi s'attendre."

    $ mara_link = 4

    jump FREE_TIME_END


label mara_link_5:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "fatigue", 0.60)

    "La cafétéria se vide."
    "Elle laisse tomber ses épaules une seconde."

    mara "Je joue un rôle."
    mara "C'est plus simple que d'expliquer."

    "Elle relève la tête, déjà ailleurs."

    $ mara_link = 5

    jump FREE_TIME_END
