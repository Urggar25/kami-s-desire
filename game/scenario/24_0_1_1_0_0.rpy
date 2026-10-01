# =============================================================================
# JOUR 24 — Vote sur les besoins vitaux
# Noam fait pencher le groupe vers l'adoption.
# =============================================================================

default j24_vital_vote = None

label _24_0_1_1_0_0_REVEIL:
    $ current_day = 24
    $ day_id = 24
    $ current_period = "Matin"

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "L'ambiance est presque légère au petit-déjeuner. Ça me paraît suspect rien que de le penser."

    $ showGroup([
        ("julian", "joie"),
        ("elen", "joie"),
        ("tomas", "reflexion"),
        ("nyra", "raison"),
        ("ryn", "neutre"),
        ("iris", "blase"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("elias", "fatigue"),
        ("noam", "neutre"),
    ])

    julian joie "Aujourd'hui, mes amis, on gagne."

    iris blase "Il est huit heures du matin."

    julian sourire "Et déjà tu essaies de tuer l'espoir."

    elen joie "Moi je suis avec lui ! Un toit, de l'eau, à manger. On peut pas rater ça."

    tomas reflexion "On peut toujours rater quelque chose."

    elen inquiet "Tomas..."

    tomas hesitation "Je dis pas qu'il faut voter contre. Je dis juste que le mot 'suffisant' laisse beaucoup de marge."

    nyra raison "Et qu'un Commandement oblige Kami à interpréter le texte. C'est pas un détail."

    ryn desaccord "Vous allez vraiment réussir à compliquer de l'eau et un toit ?"

    tomas reflexion "Non, mais si tu écris un droit absolu sans préciser les moyens..."

    ryn agace "Voilà. Tu compliques."

    mara taquin "Moi je suis pour le droit au lit. Surtout si on précise pas avec qui."

    iris blase "Évidemment."

    julian joie "Vous voyez ? Même Mara participe au progrès social."

    mara rire "Je participe beaucoup."

    noam reflexion "Le problème, c'est pas le principe. C'est la confiance dans l'application."

    nyra raison "Exactement."

    elen triste "Mais si on commence à refuser les trucs simples parce qu'on a peur de ce que Kami peut en faire... on vote plus jamais rien."

    "La phrase tombe plus lourdement que prévu."

    julian sourire "Merci."

    elen surpris "Quoi ?"

    julian sourire "C'était très bien."

    elen neutre "Ah."

    "Je regarde autour de la table. Personne n'est vraiment contre. Pourtant personne n'a l'air prêt à dire oui sans réserve."

    noam reflexion "On peut passer la journée à chercher où elle peut nous piéger."

    iris blase "Et elle peut."

    noam raison "Oui. Mais là... si on refuse même ça uniquement parce que c'est elle qui l'appliquera, alors c'est plus nous qui décidons. C'est encore elle."

    tomas inquiet "Tu veux dire qu'on vote pour malgré le risque."

    noam reflexion "Je veux dire qu'on vote pour le texte. Et qu'on surveille ce qu'elle en fait."

    nyra reflexion "C'est pas très confortable comme position."

    noam taquin "Depuis quand on fait du confortable ici ?"

    ryn sourire "Ça me va."

    sael raison "À moi aussi."

    iris fatigue "Pff... ouais. D'accord."

    tomas hesitation "Je... oui. D'accord aussi."

    julian joie "Voilà !"

    elen joie "On l'a !"

    "Julian et Elen se tapent dans la main comme s'ils venaient de gagner une élection."

    iris blase "Vous êtes insupportables."

    julian sourire "Mais victorieux."

    $ hideGroup()

label _24_0_1_1_0_0_VOTE:
    $ current_period = "Après-midi"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showGroup([
        ("julian", "joie"),
        ("elen", "joie"),
        ("tomas", "neutre"),
        ("nyra", "raison"),
        ("ryn", "neutre"),
        ("iris", "blase"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("elias", "neutre"),
        ("kael", "calme"),
        ("lysa", "blase"),
        ("noam", "reflexion"),
    ])

    "Le texte est relu une dernière fois."

    julian joie "Je vote pour."

    elen joie "Pour !"

    ryn neutre "Pour."

    sael raison "Pour."

    iris fatigue "Pour."

    tomas hesitation "Pour."

    nyra raison "Pour."

    mara taquin "Pour. Et je réclame toujours le supplément vin."

    elias neutre "Pour."

    kael calme "Pour."

    lysa blase "Pour."

    "Tous les regards finissent sur moi."

    menu:
        "Voter POUR le nouveau Commandement":
            $ j24_vital_vote = "for"
            noam determine "Pour."
        "S'abstenir au dernier moment":
            $ j24_vital_vote = "abstain"
            noam hesitation "Je... je m'abstiens."

    if j24_vital_vote == "abstain":
        "Un silence passe."
        julian surpris "Sérieux ?"
        noam reflexion "Je bloque pas le texte. Je veux juste pas faire semblant d'être certain."
        nyra raison "L'abstention n'empêche pas l'unanimité des suffrages exprimés."
        iris blase "Donc ça passe quand même."
    else:
        "Julian ferme les yeux une seconde comme s'il venait réellement de gagner quelque chose."

    play sound sfx_announce
    stop music fadeout 0.5
    scene bg_diffusion_champagne at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Eh bien !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Regardez-moi cette belle unanimité."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je suis presque déçue. Pas une crise, pas un ultimatum, pas même une petite menace."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Le nouveau Commandement est adopté."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showGroup([
        ("julian", "joie"),
        ("elen", "joie"),
        ("iris", "blase"),
        ("noam", "neutre"),
    ])

    elen joie "On l'a fait !"

    julian joie "Enfin une victoire propre !"

    iris blase "Vous allez nous faire un tour d'honneur ?"

    julian sourire "Excellente idée."

    elen rire "Viens !"

    "Ils partent vraiment faire le tour de la table sous les protestations."

    noam taquin "Ils jouent aux héros."

    iris fatigue "Laisse-les. Pour une fois qu'on peut rire sans que quelqu'un saigne."

    "Je la regarde."

    noam reflexion "Tu sais vraiment casser une ambiance."

    iris sourire "Je fais ce que je peux."

    $ hideGroup()

label _24_0_1_1_0_0_FIN:
    $ current_period = "Soir"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Pour la première fois depuis longtemps, je me couche avec le souvenir d'une journée qui n'a pas complètement déraillé."

    think "Ça ne durera probablement pas."

    call end_day("25", sleeping=True) from _call_j24_stay_end_day_25
    jump _25_0_1_1_0_0_REVEIL
