# -----------------------------------------------------------------------
# LIENS — SAEL
# -----------------------------------------------------------------------

default sael_link = 0

label SAEL_LINK_INTERACT:

    menu:
        "Passer du temps avec Sael ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if sael_link == 0:
        jump sael_link_1
    elif sael_link == 1:
        jump sael_link_2
    elif sael_link == 2:
        jump sael_link_3
    elif sael_link == 3:
        jump sael_link_4
    elif sael_link == 4:
        jump sael_link_5

    if last_room_label:
        jump expression last_room_label
    return

label sael_link_1:

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    scene bg_sas at adaptive_fullscreen

    $ showP("sael", "reflechit", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Sael ajuste les lanières de ses gants avec une précision rituelle."
    noam "C'est une habitude de ta tribu ?"
    sael "Oui. Chez nous : force, endurance, silence."
    noam "Le silence aussi ?"
    $ showP("sael", "raison", 0.70)
    sael "Parler trop tôt fait fuir l'air quand il faut tenir longtemps."
    noam "Vous aviez des rites ?"
    sael "Lever avant l'aube, course, garde, puis repas sans plainte."
    play sound sfx_tambour
    sael "Le tambour donnait la cadence. Même maintenant, mon corps l'entend encore."

    $ sael_link = 1
    jump FREE_TIME_END

label sael_link_2:

    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("sael", "neutre", 0.70)
    $ showP("noam", "hesitation", 0.24)

    noam "Tu parles de Kami comme d'une divinité."
    sael "Comme d'une puissance supérieure, oui."
    noam "Par foi ?"
    $ showP("sael", "determine", 0.70)
    sael "Par logique. Une entité capable d'imposer ça à tous... mérite un statut à part."
    noam "Donc c'est rationnel, pas naïf."
    sael "Exactement. Je n'agenouille pas mon esprit, j'adapte mes chances."
    noam "Tu n'y vois jamais d'injustice ?"
    sael "Si. Mais l'univers ne nous doit pas l'équité."

    $ sael_link = 2
    jump FREE_TIME_END

label sael_link_3:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen

    $ showP("sael", "mefiant", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Sael observe deux candidats s'entraîner, bras croisés."
    noam "Pour toi, c'est quoi être fort ?"
    sael "Tenir debout quand plus personne ne te regarde."
    noam "Et la faiblesse ?"
    $ showP("sael", "triste", 0.70)
    sael "Elle ne m'agace pas. Elle m'inquiète."
    noam "Pourquoi ?"
    sael "Parce qu'une faiblesse ignorée devient une faille qui avale tout le groupe."
    noam "Donc tu juges moins que tu surveilles."
    $ showP("sael", "raison", 0.70)
    sael "Oui. Je préfère renforcer que mépriser."

    $ sael_link = 3
    jump FREE_TIME_END

label sael_link_4:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("sael", "determine", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Sael pose une carte de la station sur la table."
    noam "Tu marques les zones à risque ?"
    sael "Oui. Et les zones sacrifiables."
    noam "Sacrifiables..."
    sael "Certaines vies doivent parfois être perdues pour que d'autres passent."
    noam "Tu dis ça avec un calme glaçant."
    play sound sfx_drop
    $ showP("sael", "reflechit", 0.70)
    sael "Parce que crier n'annule pas le calcul."
    noam "Tu pourrais choisir autrement."
    sael "Parfois oui. Pas toujours."

    $ sael_link = 4
    jump FREE_TIME_END

label sael_link_5:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("sael", "culpabilite", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Sael fixe l'emblème de Kami au centre de la salle."
    noam "Tu n'as pas peur de mourir, pas vrai ?"
    sael "Non."
    noam "Alors qu'est-ce qui te fait trembler ?"
    $ showP("sael", "triste", 0.70)
    sael "Son jugement."
    noam "Kami ?"
    sael "Oui. Mourir n'est qu'une fin. Être déclarée indigne... ça, c'est pire."
    play sound sfx_announce
    $ showP("sael", "determine", 0.70)
    sael "Je peux accepter la mort. Pas d'être rejetée par ce qui décide du sens."

    $ sael_link = 5
    jump FREE_TIME_END
