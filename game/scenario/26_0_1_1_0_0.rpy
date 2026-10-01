# =============================================================================
# JOUR 26 — Face caméra
# Noam rend publiquement l'existence probable des doubles.
# Tomas l'entend et prévient le groupe.
# =============================================================================

default j26_camera_tone = None
default j26_public_reveal = False

label _26_0_1_1_0_0_REVEIL:
    $ current_day = 26
    $ day_id = 26
    $ current_period = "Matin"

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je n'ai presque pas dormi."

    "À chaque fois que je ferme les yeux, je vois deux Mara : celle du conduit et celle qui rigole à table."

    think "Si je parle, je déclenche quelque chose."

    think "Si je me tais, eux continuent."

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "inquiet", 0.42),
        ("noam", "fatigue", 0.62),
    ])

    iris inquiet "T'as décidé."

    noam fatigue "Ça se voit ?"

    iris blase "Oui."

    noam reflexion "Je vais parler."

    iris fatigue "Évidemment."

    noam inquiet "Tu veux m'arrêter ?"

    iris desaccord "Non. J'ai envie de te dire que c'est une idée de merde et que j'aurais probablement fait pareil."

    noam taquin "Très rassurant."

    iris blase "Je suis là pour ça."

    $ hideGroup()

label _26_0_1_1_0_0_CAMERA:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Je choisis la salle du Conclave parce que je sais où sont les caméras."

    "Pour une fois, je veux qu'elles me voient."

    $ showGroup([
        ("iris", "inquiet", 0.30),
        ("noam", "reflexion", 0.58),
    ])

    iris inquiet "Dernière chance de te dégonfler."

    noam fatigue "Merci."

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Comment le dire ?"
        "Raconter seulement ce que j'ai vu":
            $ j26_camera_tone = "facts"
            noam determine "Je raconte les faits. Rien de plus."
        "Dire clairement que des doubles nous remplacent":
            $ j26_camera_tone = "accuse"
            noam determine "Non. Je vais dire ce que je pense que ça veut dire."

    iris fatigue "D'accord."

    "Je me place face à l'objectif."

    noam hesitation "Je sais pas combien de personnes regardent ça. Et franchement... je sais même pas comment commencer."

    "Ma bouche est sèche."

    noam reflexion "Depuis plusieurs jours, il se passe des choses dans le Conclave qu'on n'arrive pas à expliquer. Des disparitions. Du matériel qui bouge. Des gens qui... qui reviennent pas exactement comme avant."

    if j26_camera_tone == "facts":
        noam determine "Hier, avec Iris, j'ai trouvé le corps de Mara dans les conduits. Je l'avais déjà vu avant. Cette fois Iris était avec moi."
        noam inquiet "Et Mara est pourtant toujours ici. Elle parle avec nous. Elle mange avec nous. Donc je sais pas ce qu'elle est, mais il y a deux réalités qui peuvent pas être vraies en même temps."
    else:
        noam determine "Hier, avec Iris, j'ai trouvé le corps de Mara dans les conduits. Et la Mara qu'on connaît continue de se promener dans la station."
        noam colere "Je pense que certains représentants ont été remplacés par des doubles. Je sais pas comment. Je sais pas combien. Mais je crois que c'est ce qui se passe."

    noam inquiet "Si vous regardez ça depuis la Terre... ne partez pas du principe que la personne qui rentrera avec notre visage sera forcément nous."

    iris peur "Noam..."

    noam determine "Je voulais que ce soit public. Maintenant ça l'est."

    $ j26_public_reveal = True

    "Une voix vient de l'entrée."

    tomas surpris "Qu'est-ce que tu viens de dire ?"

    $ showGroup([
        ("iris", "inquiet", 0.22),
        ("tomas", "surpris", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    noam inquiet "Tomas..."

    tomas peur "Non. Non, attends. Le corps de Mara ? Un double ? Tu racontes ça aux caméras avant de nous le dire ?"

    iris colere "Baisse d'un ton."

    tomas colere "Je baisse rien du tout !"

    noam inquiet "On savait pas à qui faire confiance."

    tomas stress "Et tu crois que maintenant ça va être mieux ?!"

    "Il recule déjà vers la porte."

    noam surpris "Tomas, attends."

    tomas peur "Je vais chercher les autres."

    iris colere "Tomas !"

    "Il part."

    $ showGroup([
        ("iris", "colere", 0.38),
        ("noam", "fatigue", 0.62),
    ])

    iris colere "Voilà. C'est parti."

    noam fatigue "Ouais."

    iris inquiet "T'as intérêt à être prêt."

    noam inquiet "Je le suis pas."

    iris fatigue "Moi non plus."

    $ hideGroup()

label _26_0_1_1_0_0_SOIR:
    $ current_period = "Soir"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showGroup([
        ("ryn", "colere"),
        ("tomas", "stress"),
        ("nyra", "inquiet"),
        ("sael", "mefiant"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("mara", "neutre"),
        ("elias", "fatigue"),
        ("kael", "calme"),
        ("iris", "colere"),
        ("noam", "inquiet"),
    ])

    ryn colere "C'est quoi ce bordel ?!"

    noam colere "Je viens de l'expliquer."

    ryn colere "Aux caméras ! Pas à nous !"

    julian inquiet "Je croyais que l'incident était terminé. Je croyais qu'on avait... je sais pas, qu'on était sortis de cette merde."

    elen peur "Mara, dis quelque chose."

    mara neutre "Qu'est-ce que tu veux que je dise ? Que je suis pas morte ? Je suis là."

    iris colere "On a vu ton corps."

    mara desaccord "Alors vous avez vu quelque chose qui me ressemble."

    sael mefiant "Ou quelque chose ici te ressemble."

    pause 0.3

    elias fatigue "Vous êtes en train de partir très loin."

    noam reflexion "Elias, si je te demandais où t'étais le jour vingt-deux pendant plusieurs heures, tu me répondrais quoi ?"

    elias mefiant "Que je bossais."

    noam neutre "Où ?"

    elias neutre "Maintenance."

    tomas stress "Je t'ai cherché là-bas."

    "Elias tourne lentement la tête vers Tomas."

    elias neutre "T'as dû me rater."

    tomas peur "Ouais..."

    kael calme "Ça suffit pour ce soir."

    ryn colere "Non, ça suffit pas du tout."

    kael inquiet "Si on commence à s'accuser sans méthode, on va s'entre-tuer."

    iris blase "Très pratique comme conseil."

    kael inquiet "Tu m'accuses aussi ?"

    iris colere "J'accuse personne. J'écoute."

    "Le silence qui suit est pire que les cris."

    nyra raison "On se sépare pas cette nuit."

    ryn determine "Enfin une bonne idée."

    mara taquin "Super. Soirée pyjama paranoïaque."

    "Personne ne rit."

    $ hideGroup()

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je rentre tard."

    "Avant de fermer la porte, je vois Mara au bout du couloir."

    "Elle me regarde."

    "Pas de sourire."

    "Puis elle disparaît derrière l'angle."

    think "Ils savent."

    call end_day("27", sleeping=True) from _call_j26_stay_end_day_27
    jump _27_0_1_1_0_0_REVEIL
