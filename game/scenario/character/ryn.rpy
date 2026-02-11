# -----------------------------------------------------------------------
# LIENS — RYN
# -----------------------------------------------------------------------

default ryn_link = 0

label RYN_LINK_INTERACT:

    menu:
        "Passer du temps avec Ryn ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if ryn_link == 0:
        jump ryn_link_1
    elif ryn_link == 1:
        jump ryn_link_2
    elif ryn_link == 2:
        jump ryn_link_3
    elif ryn_link == 3:
        jump ryn_link_4
    elif ryn_link == 4:
        jump ryn_link_5

    if last_room_label:
        jump expression last_room_label
    return

label ryn_link_1:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen

    $ showP("ryn", "fatigue", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Ryn termine des tractions, puis saute au sol dans un bruit sourd."
    play sound sfx_drop

    noam "Tu parles souvent de la frontière de LIMEN. C'était comment ?"
    ryn "Pas héroïque. Juste rude."
    ryn "Vent coupant, tours qui grincent, patrouilles trop longues."
    noam "Et les gens ?"
    $ showP("ryn", "reflechit", 0.70)
    ryn "Les gens tenaient parce qu'ils n'avaient pas le luxe de tomber."
    noam "Tu regrettes cette vie ?"
    ryn "Je regrette certains visages. Le reste, non."

    $ ryn_link = 1
    jump FREE_TIME_END

label ryn_link_2:

    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_sas at adaptive_fullscreen

    $ showP("ryn", "colere", 0.70)
    $ showP("noam", "hesitation", 0.24)

    play sound sfx_door
    "La porte se referme derrière moi. Ryn est déjà tendu."

    noam "Pourquoi tu exploses si vite ?"
    ryn "Parce que chez nous, hésiter coûtait un bras, parfois une vie."
    noam "Tu pourrais ralentir ici."
    $ showP("ryn", "desaccord", 0.70)
    ryn "Ralentir, c'est une habitude qui reste quand ça recommence."
    noam "Tu préfères être trop dur ?"
    ryn "Toujours. Trop dur se corrige. Trop lent, ça enterre."
    play sound sfx_beep
    noam "Je comprends mieux... sans aimer."
    ryn "T'as pas besoin d'aimer. Juste de savoir d'où ça vient."

    $ ryn_link = 2
    jump FREE_TIME_END

label ryn_link_3:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("ryn", "inquiet", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Ryn fixe l'obscurité derrière la vitre, comme s'il comptait des noms."
    noam "Tu as laissé du monde derrière toi ?"
    ryn "Oui. Trop."
    noam "Tu veux retourner à LIMEN après ça ?"
    $ showP("ryn", "determine", 0.70)
    ryn "Évidemment. LIMEN c'est pas juste un territoire, c'est les miens."
    noam "Même après tout ce que tu critiques ?"
    ryn "On peut détester la boue et protéger la maison quand même."
    noam "Tu leur dois quoi ?"
    ryn "De ne pas les oublier pendant que je joue au Conclave."

    $ ryn_link = 3
    jump FREE_TIME_END

label ryn_link_4:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("ryn", "reflechit", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Ryn s'interrompt au milieu d'une phrase et serre la mâchoire."
    noam "Quoi ?"
    ryn "Rien."
    noam "Si, dis-le."
    ryn "Je me demande parfois si se battre suffit vraiment."
    "Le silence tombe, lourd."
    play sound sfx_paper
    $ showP("ryn", "colere2", 0.70)
    ryn "Putain. Voilà, c'est sorti."
    noam "T'as le droit de douter."
    ryn "Ouais... mais je déteste ça."

    $ ryn_link = 4
    jump FREE_TIME_END

label ryn_link_5:

    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("ryn", "determine", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Ryn frappe du poing dans sa paume avant le vote."
    play sound sfx_clap

    noam "Tu vas voter comment ?"
    ryn "Comme toujours : pour protéger les miens."
    noam "Même si ça te met tout le monde à dos ?"
    ryn "Même là."
    noam "Et la morale dans tout ça ?"
    $ showP("ryn", "neutre", 0.70)
    ryn "Chez moi, la morale vient après la survie."
    noam "Tu assumes ce prix ?"
    ryn "Je l'assume. Et je dors mieux avec ça qu'avec des principes qui laissent des corps derrière."

    $ ryn_link = 5
    jump FREE_TIME_END
