default seen_voyeur_julian_iris = False
default seen_voyeur_mara_tomas = False
default seen_voyeur_nyra = False
default got_argument_echanges_discrets = False


label temps_libre_salle_repos:

    $ seen_voyeur_julian_iris = True

    scene bg_repos at adaptive_fullscreen
    play sound "audio/sfx_door.mp3"

    "La salle de repos est presque vide."
    "Le ronronnement des néons couvre à peine un souffle retenu, derrière un paravent replié."

    think "Je m'arrête net."
    think "Deux voix. Basses. Trop proches pour une simple conversation."

    $ showP("julian", "taquin", 0.62)
    $ showP("iris", "colere", 0.80)

    julian "Tu grognes encore, mais tu t'es pas reculée."
    iris "Je grogne parce que tu parles trop."
    iris "Et retire pas ça de son contexte."

    "Un rire bref lui échappe malgré elle."
    "Le tissu du paravent frissonne, comme si une main glissait sous une veste."

    $ showP("julian", "sourire", 0.62)
    julian "Tu vois ? Tu souris quand même."

    $ showP("iris", "hesitation", 0.80)
    iris "T'approche pas de mon cou—"
    "Il l'embrasse juste sous l'oreille."
    "Le souffle d'Iris se coupe une seconde."

    iris "...T'es insupportable."
    julian "Et toi, impossible à quitter."

    "Des caresses lentes passent sous les couches de tissu, discrètes, précises."
    "Leur respiration se mélange, nerveuse, électrique."

    $ showP("iris", "taquin", 0.80)
    iris "Si quelqu'un nous voit, je nie tout."
    julian "Alors on va leur laisser aucun angle."

    think "Je recule d'un pas."
    think "Le parquet grince à peine. Ils n'entendent rien."
    think "Je me retire dans le couloir, sans bruit."

    hide julian
    hide iris
    jump REPOS_TP


label temps_libre_salle_archive:

    $ seen_voyeur_mara_tomas = True

    scene bg_archive at adaptive_fullscreen
    play sound "audio/sfx_paper.mp3"

    "Entre deux rayonnages, une lampe de lecture reste allumée."
    "Je distingue Mara, adossée à un meuble bas, et Tomas, raide comme un câble tendu."

    $ showP("mara", "sourire", 0.74)
    $ showP("tomas", "panne", 0.38)

    mara "Attends... t'es sérieux ? Jamais, jamais ?"
    tomas "J-je... non. Pas vraiment."
    tomas "Enfin, non."

    $ showP("mara", "sourire", 0.74)
    mara "C'est presque mignon."
    mara "Viens. Je te guide. Tu paniques pas, tu suis."

    "Elle prend sa main avec assurance et la fait glisser sous le tissu de sa jupe, juste assez pour l'obliger à sentir la chaleur de sa peau."
    "Tomas rougit jusqu'aux oreilles."

    $ showP("tomas", "reflechit", 0.38)
    tomas "Je... je dois faire quoi ?"
    mara "Rien d'héroïque. Doucement."
    mara "Comme si tu apprenais une machine délicate."

    "Il bouge à peine les doigts."
    "Mara souffle un rire bas, puis guide son poignet vers le haut de son buste, par-dessus son chemisier."

    $ showP("mara", "sourire", 0.74)
    mara "Voilà. Là. Tu vois ?"
    mara "Tu trembles, mais t'apprends vite."

    $ showP("tomas", "raison", 0.38)
    tomas "Pardon. Je veux pas mal faire."
    mara "Tu fais pas mal."
    mara "Tu découvres. Nuance."

    think "Je détourne les yeux avant que ça aille plus loin."
    think "Le bruit des pages couvre mes pas quand je ressors."

    hide mara
    hide tomas
    jump ARCHIVE_TP


label temps_libre_salle_dortoir:

    $ seen_voyeur_nyra = True

    scene bg_dortoir at adaptive_fullscreen

    "Le dortoir est silencieux, sauf un son étouffé au fond du couloir."
    "Un rythme court. Un souffle contrôlé."

    think "La porte de Nyra est entrouverte de quelques centimètres."
    think "Je n'aurais pas dû regarder."

    scene bg_chambre at adaptive_fullscreen
    play sound "audio/sfx_shower.mp3"

    $ showP("nyra", "raison", 0.70)

    "À travers la fente, je la vois, jupe remontée sur les cuisses, chemisier ouvert juste assez pour laisser sa peau prendre la lumière froide."
    "Dans sa main, un petit appareil bricolé vibre par impulsions régulières."

    nyra "Tiens le rythme."
    nyra "Pas plus vite. C'est moi qui décide."

    "Elle garde le dos droit, le regard fixé sur son reflet sombre dans la vitre."
    "Ses mouvements restent précis, presque militaires, malgré la chaleur qui lui casse la voix par moments."

    $ showP("nyra", "reflexion", 0.70)
    nyra "Encore."
    nyra "Respire. Contrôle."

    "Un gémissement lui échappe, bref, aussitôt avalé."
    "Elle reprend le tempo, maîtresse d'elle-même jusqu'au bout des doigts."

    think "Je recule lentement."
    think "Aucune latte ne craque."
    think "Elle ne lève jamais les yeux vers la porte."
    think "Je disparais dans le couloir sans être vu."

    hide nyra
    jump DORTOIR_TP


label temps_libre_salle_stockage_argument:

    scene bg_stockage at adaptive_fullscreen
    play sound "audio/sfx_paper.mp3"

    "Au fond de la salle de stockage, deux silhouettes parlent à voix basse entre les caisses."
    "Sael tend un filtre à air. Nyra lui passe une pochette de joints d'étanchéité en échange."

    $ showP("sael", "neutre", 0.30)
    $ showP("nyra", "neutre", 0.76)

    sael "Filtre propre. Deux semaines si tu le ménages."
    nyra "Parfait. Ces joints éviteront une fuite sur la ligne secondaire."

    $ showP("sael", "raison", 0.30)
    sael "Chez nous, je troquais déjà ça contre des repas chauds."
    sael "Pas légal. Juste nécessaire."

    $ showP("nyra", "taquin", 0.76)
    nyra "À Orbite, un lot de légumes valait une réparation express."
    nyra "Même logique, autre décor."

    sael "Le système appelle ça du désordre."
    nyra "Moi j'appelle ça des gens qui s'adaptent."

    "Elles referment les contenants, sobres, efficaces, comme un rituel rodé."

    think "Donc les échanges discrets existent déjà."
    think "Sans effondrement. Sans chaos."

    if not got_argument_echanges_discrets:
        $ got_argument_echanges_discrets = True
        $ add_argument("Échanges discrets déjà actifs")
        show screen argument_unlock("Échanges discrets déjà actifs")

    think "Je me retire avant qu'elles ne me repèrent."

    hide sael
    hide nyra
    jump STOCKAGE_TP
