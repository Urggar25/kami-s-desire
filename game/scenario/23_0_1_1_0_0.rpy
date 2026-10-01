# =============================================================================
# JOUR 23 — Route 0_1_1_0_0
# Sael s'inquiète des "hallucinations" de Noam.
# Les examens médicaux sont normaux.
# =============================================================================

label _23_0_1_1_0_0_REVEIL:
    $ current_day = 23
    $ day_id = 23
    $ current_period = "Matin"

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2

    "Je dors mal. Pas à cause d'un bruit cette fois. Juste parce que mon cerveau a décidé de rejouer Mara morte, Mara vivante, puis Elias qui me dit que tout va bien."

    "Quand je me lève, le bureau est toujours coincé sous la grille. Je le laisse là."

    think "Très sain comme début de journée."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showGroup([
        ("sael", "reflexion"),
        ("iris", "fatigue"),
        ("mara", "taquin"),
        ("noam", "fatigue"),
    ])

    sael reflexion "Tu dors mal."

    noam blase "Bonjour à toi aussi."

    sael neutre "T'as les yeux rouges. Et hier t'as encore parlé de trucs que personne d'autre a vus."

    mara taquin "Moi je trouve ça charmant. Un homme mystérieux, traumatisé, potentiellement hanté..."

    iris agace "Mara."

    mara sourire "Je complimente."

    sael raison "Je veux te faire passer des examens."

    noam surpris "Pardon ?"

    sael neutre "À l'infirmerie. Pas un rite. Des vrais examens."

    noam reflexion "Tu crois vraiment que j'hallucine."

    sael fatigue "Je sais pas. Justement."

    "Elle dit ça sans agressivité. Ça me coupe un peu."

    iris reflexion "Quels examens ?"

    sael raison "Réflexes. Pupilles. Mémoire. Scanner. IRM si la machine veut bien marcher."

    iris blase "Et tu comptes faire ça toute seule ?"

    sael neutre "Je sais utiliser le matériel."

    iris agace "C'est pas la question."

    sael desaccord "Alors pose la bonne question."

    iris determine "Je viens."

    noam surpris "Attends, j'ai rien accepté."

    mara taquin "Trop tard. T'as deux mamans maintenant."

    iris colere "Tu veux vraiment continuer ?"

    mara rire "Oui."

    noam fatigue "Bon... d'accord. On vérifie. Mais pas de sel."

    sael taquin "Pas de sel."

    $ hideGroup()

label _23_0_1_1_0_0_INFIRMERIE:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Une heure plus tard, je suis assis sur une table d'examen avec des capteurs sur les tempes."

    $ showGroup([
        ("sael", "raison", 0.25),
        ("iris", "blase", 0.50),
        ("noam", "fatigue", 0.75),
    ])

    sael raison "Regarde la lumière."

    noam neutre "Je regarde."

    sael agace "Pas moi. La lumière."

    noam blase "Je regardais la lumière."

    iris taquin "Non. Tu la regardais elle parce que t'avais peur qu'elle sorte une aiguille."

    noam colere "Je surveille."

    sael neutre "Tes pupilles sont normales."

    "Elle passe à mes réflexes, puis me fait suivre une série de formes sur l'écran."

    sael raison "Tu te souviens de ce que t'as mangé hier midi ?"

    noam neutre "Oui."

    sael "Avant-hier ?"

    noam hesitation "Euh... un truc en sauce."

    iris blase "Test concluant, il est humain."

    noam blase "Merci."

    sael colere "Je plaisante pas."

    iris fatigue "Moi non plus."

    "Sael soupire mais continue. Les tests s'enchaînent, parfois sérieux, parfois franchement ridicules."

    sael raison "Donne-moi les noms des représentants dans l'ordre où tu les as rencontrés."

    noam reflexion "Lysa, Iris... Elias, je crois. Après..."

    iris agace "Tu crois ?"

    noam fatigue "J'étais kidnappé dans l'espace, Iris."

    iris blase "Excuse pratique."

    "Sael note quelque chose."

    noam inquiet "Quoi ?"

    sael raison "Rien. Tu hésites comme quelqu'un qui se souvient. Pas comme quelqu'un qui récite."

    noam reflexion "C'est rassurant ?"

    sael neutre "Un peu."

    "Puis vient l'IRM."

    scene black with fade

    "Je déteste l'idée avant même d'entrer dans la machine."

    scene infirmerie2 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("sael", "reflexion", 0.25),
        ("iris", "inquiet", 0.50),
        ("noam", "fatigue", 0.75),
    ])

    iris inquiet "Si tu veux sortir, tu sors. On s'en fout de finir."

    noam taquin "Tu deviens gentille, ça m'inquiète plus que l'IRM."

    iris agace "Ferme-la et allonge-toi."

    sael raison "Ça dure pas longtemps."

    noam blase "Vous dites tous ça avant les trucs qui durent longtemps."

    "Je m'allonge. La machine se referme autour de ma tête."

    scene black with dissolve

    "Le bruit commence. Régulier. Mécanique. Rien à voir avec les coups que j'ai entendus dans les conduits."

    "J'essaie de penser à autre chose."

    think "Si quelque chose ne va pas dans ma tête, au moins on le saura."

    "Quelques minutes plus tard, la machine s'arrête."

    scene infirmerie2 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("sael", "reflexion", 0.28),
        ("iris", "inquiet", 0.52),
        ("noam", "fatigue", 0.76),
    ])

    noam inquiet "C'est mauvais, ce silence."

    iris inquiet "Sael ?"

    sael raison "C'est normal."

    noam surpris "Normal comment ?"

    sael raison "Normal normal. Pas de lésion. Pas de trace d'hypoxie. Pas d'hémorragie. Rien qui explique des hallucinations."

    iris reflexion "Donc il n'hallucine pas."

    sael fatigue "J'ai pas dit ça. J'ai dit que son cerveau a l'air normal."

    noam blase "C'est censé me rassurer."

    sael fatigue "Moi, ça me rassure pas."

    pause 0.4

    iris inquiet "Pourquoi ?"

    sael reflexion "Parce que s'il a vraiment vu ce qu'il dit avoir vu... alors le problème est pas dans sa tête."

    "Personne ne répond."

    "Pour la première fois depuis plusieurs jours, j'aurais presque préféré qu'elle trouve quelque chose."

    $ hideGroup()

label _23_0_1_1_0_0_SOIR:
    $ current_period = "Soir"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je relis le compte rendu sur ma tablette. Tout est normal."

    think "Donc soit je suis fou d'une manière qu'une IRM ne voit pas..."

    "Je m'arrête."

    think "Soit j'ai vraiment vu Mara morte."

    "Je pose la tablette face contre le lit."

    "La deuxième possibilité me fait beaucoup plus peur."

    call end_day("24", sleeping=True) from _call_j23_stay_end_day_24
    jump _24_0_1_1_0_0_REVEIL
