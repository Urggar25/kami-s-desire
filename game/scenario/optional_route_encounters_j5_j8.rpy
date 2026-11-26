# Rencontres facultatives sur les trajets scénarisés, J5-J8.
# Chaque rencontre se joue une seule fois par passage dans le label de trajet ;
# le joueur peut continuer immédiatement. Aucun effet sur les votes ou indices.

label KD_ROUTE_J5_NYRA:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Nyra consulte sa tablette près du croisement. Elle relève la tête quand je passe."
    menu:
        "Échanger quelques mots avec Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "neutre", 0.65)])
            nyra "Tu vas à l'Observation ?"
            noam "Je voudrais voir ce qui se passe en bas."
            nyra "Pour chercher quoi ?"
            noam reflexion "Je sais pas exactement. Voir comment les choses évoluent."
            nyra raison "Alors commence par choisir une question. Sinon tu vas passer une heure devant des images sans rien apprendre."
            noam taquin "Tu fais toujours un programme avant de regarder par une fenêtre ?"
            nyra "Non. Mais je ne confonds pas regarder et comprendre."
            noam "Je te dirai si je trouve quelque chose."
            nyra neutre "Seulement si tu sais ce que tu as trouvé."
            $ hideGroup()
        "Continuer vers l'Observation.":
            pass
    return

label KD_ROUTE_J5_LYSA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa est adossée au mur. Elle me voit arriver de l'autre côté du couloir."
    menu:
        "Parler à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "neutre", 0.65)])
            lysa "C'était quoi, cette réunion de crise avec Kael et Nyra ?"
            noam reflexion "Kael avait besoin de parler."
            lysa "J'avais compris. Il est passé devant moi sans même répondre quand je lui ai dit bonjour."
            noam "Il s'inquiète pour sa sœur."
            lysa neutre "Ah."
            "Elle perd son sourire un instant."
            lysa "Je vais éviter de lui sortir une blague idiote, alors."
            noam taquin "C'est une première."
            lysa blase "Profite. Ça n'arrivera pas souvent."
            $ hideGroup()
        "Rejoindre la cafétéria.":
            pass
    return

screen j601_elen_clic_couloir():
    modal True
    zorder 180
    imagebutton:
        idle Transform(character_image("elen", "joie"), zoom=0.85)
        hover Transform(character_image("elen", "content"), zoom=0.88)
        xalign 0.72
        yalign 1.0
        focus_mask True
        action Return(True)
    frame:
        xalign 0.5
        yalign 0.08
        background Solid("#071822cc")
        padding (20, 10)
        text "Clique sur Elen pour lui parler" size 26 color "#ffffff"

label KD_ROUTE_J6_ELEN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Elen sort des dortoirs au moment où je prends la direction de la cafétéria. Elle me fait de grands signes."
    call screen j601_elen_clic_couloir
    $ showGroup([("elen", "content", 0.35), ("noam", "fatigue", 0.65)])
    elen content "Noam ! Hé ! T'as dormi ?"
    noam fatigue "Un peu. Enfin... pas beaucoup."
    elen surpris "Oh non ! Mais t'as mangé au moins ?"
    noam "Elen, je viens de me lever."
    elen joie "Alors on va manger ! Ça va te faire du bien, tu vas voir !"
    noam surpris "Attends, je comptais justement..."
    "Elle m'attrape par le poignet et commence déjà à marcher."
    elen content "Allez, viens ! Goumi doit avoir préparé quelque chose. Tu réfléchiras mieux le ventre plein !"
    noam "Je sais marcher tout seul !"
    elen rire "Je sais ! Mais là, tu marches pas assez vite."
    $ hideGroup()
    $ j601_with_elen = True
    return

label KD_ROUTE_J6_JULIAN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Julian attend près de la porte de la salle de repos. Il me fait un grand signe."
    menu:
        "Écouter Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
            julian "Avant d'entrer, une question stratégique : tu comptes défendre quoi ?"
            noam "Je vais surtout écouter les autres."
            julian taquin "Ah, la fameuse stratégie du type qui attend que tout le monde s'énerve."
            noam "Ça marche mieux que tes discours improvisés."
            julian "Mes discours sont des œuvres en constante évolution."
            noam "Tu as au moins une proposition ?"
            julian hesitation "Oui. Éviter que Ryn et Sael recommencent à se hurler dessus."
            noam sourire "Pour une fois, on est d'accord."
            julian sourire "Tu vois ? Je rassemble déjà les foules."
            $ hideGroup()
        "Entrer dans la salle de repos.":
            pass
    return

label KD_ROUTE_J7_ELIAS:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Elias transporte une caisse de matériel. Il la pose par terre pour reprendre son souffle."
    menu:
        "Donner un coup de main à Elias.":
            $ showGroup([("elias", "fatigue", 0.35), ("noam", "neutre", 0.65)])
            elias "Ah, merci ! Prends ce côté, ça glisse un peu. Je l'avais mise sur le chariot, mais Nyra en avait besoin."
            noam "Tu vas où avec tout ça ?"
            elias "Au stockage. J'essaie de trouver de quoi continuer mon projet. Le truc, c'est que dès que je récupère une pièce, j'en trouve une autre qui va pas avec. Hier soir, j'ai passé deux heures à refaire un réglage."
            noam "Tu devrais demander un coup de main à Kael."
            elias "Il m'aide déjà quand il a le temps. Mais j'aimerais bien lui montrer un truc qui marche, tu vois ? Pas débarquer à chaque fois avec un machin démonté dans les mains."
            "On soulève la caisse. Elias manque de coincer son pied dessous."
            elias "Attends, attends ! Mon lacet."
            "Je repose mon côté. Il refait son lacet."
            noam "T'as besoin que je vienne jusqu'au stockage ?"
            elias "Non, laisse, t'as déjà aidé. Je te montrerai ce que j'ai fait quand ça sera présentable. Enfin, si j'arrive à le finir avant qu'on rentre."
            noam "Ça me ferait plaisir."
            elias sourire "Cool. Va manger, je vais me prendre un café après."
            $ hideGroup()
        "Continuer vers la cafétéria.":
            pass
    return

label KD_ROUTE_J7_LYSA_SECRET:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa apparaît au croisement des dortoirs. Je ralentis malgré moi."
    menu:
        "Répondre à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "inquiet", 0.65)])
            lysa "Encore par ici ? Tu cherches ta chambre ou celle d'Iris ?"
            noam hesitation "Pourquoi tu me demandes ça ?"
            lysa taquin "Parce que t'as la tête de quelqu'un qui essaie d'avoir l'air naturel. C'est raté."
            noam "Je voulais juste lui parler."
            lysa "Bon courage. Elle a l'air d'une humeur charmante aujourd'hui."
            noam "Merci du conseil."
            lysa blase "Et arrête de regarder derrière toi comme ça, c'est franchement louche."
            noam sourire "Je ferai un effort."
            lysa "S'il te plaît. C'est fatigant à regarder."
            $ hideGroup()
        "Passer sans s'arrêter.":
            pass
    return

label KD_ROUTE_J7_NYRA_GUEST:
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    "Nyra sort d'un couloir adjacent avec ses relevés de rationnement."
    menu:
        "Discuter avec Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "inquiet", 0.65)])
            nyra "Tu vas voir l'invitée ?"
            noam "Oui. Je voulais savoir si son état s'améliore."
            nyra "J'espère aussi. Mais il faudra régler la question des rations."
            noam "Tu penses déjà à la nourriture ?"
            nyra raison "Il faudra bien que quelqu'un y pense. Kami ne nous en donnera pas davantage par gentillesse."
            noam "Elle est à peine consciente, Nyra."
            nyra "Je ne lui reproche rien. Je dis seulement qu'on devra répartir autrement ce qu'il nous reste."
            noam reflexion "D'accord. On en reparle quand on en saura plus."
            nyra "C'est ce que je comptais faire."
            $ hideGroup()
        "Aller directement à l'infirmerie.":
            pass
    return

label KD_ROUTE_J8_JULIAN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Julian passe devant moi, s'arrête et revient sur ses pas."
    menu:
        "Parler à Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "fatigue", 0.65)])
            julian "Tu sais que tu fais une tête absolument catastrophique ?"
            noam "Bonjour à toi aussi."
            julian taquin "J'hésitais entre te proposer une partie et appeler Sael."
            noam "Ni l'un ni l'autre, merci."
            julian "D'accord. Alors une question facile : café ou thé ?"
            noam reflexion "Quoi ?"
            julian "Je t'offre une boisson à la cafétéria. Pas besoin de parler si t'en as pas envie."
            noam fatigue "Ça ira. Mais merci."
            julian neutre "Bon. Si tu changes d'avis, je serai là."
            noam sourire "Je note."
            $ hideGroup()
        "Continuer vers la cafétéria.":
            pass
    return
