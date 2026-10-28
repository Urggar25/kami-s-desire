# JOUR 29 — ROUTE SECRÈTE : IRIS CHOISIE AU J28
# Double focalisation : original Noam, puis Noam-DG, puis original Noam.
# Point d'arrêt narratif : révélation d'Iris au laboratoire, fin du chapitre.
# Les narrations à la première personne pendant la séquence centrale
# appartiennent EXPLICITEMENT au double, et non à l'original.
default j29_iris_double_created = False
default j29_iris_pov_double = False

label _29_0_1_1_0_0_1_2_REVEIL:
    $ current_day = 29
    $ day_id = 29
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"
    $ j29_iris_double_created = False
    $ j29_iris_pov_double = False
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    "Je me réveille sur la banquette du labo. J'ai la bouche pâteuse et j'ai presque pas dormi."
    "La dernière chose que j'ai vue avant de dormir, c'est le message d'Iris. Elle a dit oui à mon double."
    "C'est moi qui ai dit Iris. J'arrête pas d'y repenser. Si je fais rien, mon double va peut-être rentrer à ma place."
    "Si mon double retourne sur Terre à ma place, Juliette l'accueillera comme son frère. Et moi, je resterai ici."
    "Il a l'air sympa. Mais s'il décide qu'il veut garder ma vie, je fais quoi ? Je vais pas réussir à le forcer."
    "Avec Iris hors du chemin, j'aurai peut-être une chance de récupérer ma place sans que tout le monde comprenne."
    "C'est dégueulasse de penser comme ça. Je le sais."
    $ showGroup([("nyra", "neutre", 0.20), ("noam", "fatigue", 0.52), ("kael", "calme", 0.81)])
    nyra neutre "Bon, t'es debout. On a décidé comment on fait."
    noam inquiet "Déjà ?"
    kael calme "Elias a préparé le matériel. Mara et Tomas vont s'occuper d'Iris. Elias va faire sortir ton original."
    noam surpris "Pourquoi ? Il est avec elle ?"
    nyra raison "Oui. Et il faut qu'il parte avant qu'on arrive."
    noam inquiet "Je peux venir. Je peux lui parler, à Iris."
    nyra neutre "Non. Toi, tu restes là."
    noam colere "Mais attends, c'est moi qui ai proposé Iris !"
    nyra raison "Justement. Depuis tout à l'heure, t'arrêtes pas de trembler."
    noam desaccord "Ça va, je te dis."
    nyra raison "Non, ça va pas. Si tu te retrouves devant elle, tu vas paniquer. Et là, on est foutus."
    noam inquiet "Et si quelque chose tourne mal ?"
    nyra neutre "On s'en occupera. Pas toi."
    kael inquiet "Écoute, Noam... Je préfère aussi que tu restes ici. On te dira quand c'est fini."
    noam colere "Donc je dois juste attendre ici pendant que vous allez la tuer ?"
    nyra raison "Tu ne viens pas. C'est non. Et si tu comptes sortir derrière notre dos, dis-le maintenant."
    "Je regarde la grille. Elle n'est pas verrouillée. Mais Kael attend ma réponse, lui aussi."
    noam fatigue "... Non. Je reste."
    nyra neutre "D'accord."
    "Elle se détourne déjà pour vérifier son terminal."
    noam reflexion "Et mon original ? Vous allez faire quoi de lui ?"
    kael calme "Faut surtout pas qu'il revienne pendant qu'on s'occupe d'Iris. On a prévu le coup."
    noam inquiet "Kael, attends..."
    kael fatigue "Ouais. Je sais."
    $ hideGroup()
    "Ils repartent. Je garde les yeux sur la grille jusqu'à ce qu'elle se referme."
    "Je pourrais encore courir les prévenir. Iris et lui. Les deux."
    "Mais si je le fais, je leur explique quoi ? Que je me suis fait passer pour mon propre double et que j'ai choisi de la sacrifier ?"
    "Je serre la tablette contre moi."
    "Je m'assois. J'ai rien d'autre à faire."
    stop music fadeout 1.0
    scene black with fade
    centered "{size=+8}Pendant ce temps...{/size}"
    $ j29_iris_pov_double = True
    jump _29_0_1_1_0_0_1_2_DOUBLE

label _29_0_1_1_0_0_1_2_DOUBLE:
    # Changement de point de vue. Le « je » désigne désormais Noam-DG,
    # celui qu'Iris prend pour l'original. Aucun appel à think, volontairement.
    $ current_period = "Après-midi"
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "Iris me pousse doucement du pied pour que je lui fasse de la place sur le lit."
    $ showGroup([("dg_noam", "sourire", 0.30), ("iris", "agace", 0.70)])
    iris agace "Eh, pousse-toi un peu ! Tu prends tout le lit !"
    dg_noam taquin "Ah bon ? Je croyais que tu voulais te rapprocher."
    iris surpris "Hein ?"
    dg_noam sourire "Bah quoi ?"
    iris agace "Non mais... T'es vraiment content de toi, en plus !"
    "Elle me donne un petit coup de coude, puis vient s'installer contre mon épaule comme si de rien n'était."
    dg_noam rire "Tu peux dire que tu veux rester contre moi, tu sais."
    iris agace "Tu peux aussi te taire, ça marche bien."
    "Je ris. Elle ne se décale pas."
    dg_noam neutre "Franchement, on est bien, là."
    iris reflexion "Pourquoi ? Parce que je râle pas assez ?"
    dg_noam sourire "Non, parce qu'on est tous les deux."
    "Elle baisse les yeux vers nos mains, qu'elle a fini par joindre sans s'en rendre compte."
    iris hesitation "Ouais, bon... c'est vrai."
    dg_noam taquin "Oh, elle est d'accord avec moi !"
    iris colere "J'ai pas dit ça !"
    dg_noam rire "Si, si. Un peu."
    "Elle essaie de garder un air fâché, puis finit par rire aussi."
    iris sourire "Tu sais que t'es vraiment nul pour draguer ?"
    dg_noam sourire "Pourtant, t'es toujours là."
    iris taquin "Pour l'instant."
    dg_noam neutre "Ah, sympa."
    iris sourire "De rien."
    "On reste un moment à discuter de ce qu'on fera après le Conclave. Pour la première fois, ça ressemble à de vrais projets."
    iris reflexion "Par contre, après, on fait comment ? Pour se voir, je veux dire. Avec les districts et Kami..."
    dg_noam raison "Je viendrai te voir à Nexus."
    iris agace "Tu dis ça comme si on pouvait prendre le train."
    dg_noam sourire "Je sais bien. Mais on peut essayer, non ?"
    iris inquiet "Tu ferais vraiment ça ?"
    dg_noam neutre "Bah oui."
    "Elle tourne la tête vers moi. Cette fois, elle ne fait pas de plaisanterie."
    iris sourire "... Moi aussi, j'aimerais bien."
    "Elle m'embrasse rapidement, puis se recule avant que je puisse dire quoi que ce soit."
    iris agace "Voilà. Et maintenant tu te moques pas."
    dg_noam taquin "J'ai rien dit !"
    iris colere "T'allais le faire !"
    "On éclate de rire tous les deux."
    "J'ai pas envie de bouger. Je sais même plus depuis combien de temps on est là."
    "Il y a deux petits coups à la porte, puis quelqu'un frappe plus fort."
    elias fatigue "Noam ! Eh, Noam, t'es là ?"
    iris agace "Oh non... Qu'est-ce qu'il a encore fait ?"
    dg_noam neutre "Ouais, j'arrive !"
    "J'entrebâille la porte. Elias se tient dans le couloir, les manches sales et les cheveux en bataille."
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.28), ("dg_noam", "neutre", 0.73)])
    elias fatigue "Hé, tu peux venir m'aider deux minutes ?"
    dg_noam reflexion "Pourquoi ? Qu'est-ce que t'as fait ?"
    elias agace "Y a une armoire qui s'est cassé la gueule dans la maintenance. J'en ai partout et j'arrive pas à la relever."
    dg_noam surpris "Attends, comment t'as fait tomber une armoire ?"
    elias colere "J'en sais rien, putain ! Tu viens m'aider ou pas ?"
    dg_noam sourire "Ouais, bouge pas."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "neutre", 0.33), ("dg_noam", "sourire", 0.70)])
    dg_noam neutre "Je vais aider Elias, il a renversé une armoire. Je reviens."
    iris blase "Une armoire ? Mais il est pas possible..."
    dg_noam sourire "Je fais vite."
    iris taquin "Ouais, ouais. Cinq minutes, hein."
    "Elle me prend par le col et me vole un dernier baiser."
    iris sourire "Bon, vas-y. Et traîne pas trois heures."
    dg_noam sourire "Promis."
    $ hideGroup()
    jump _29_0_1_1_0_0_1_2_MAINTENANCE

label _29_0_1_1_0_0_1_2_MAINTENANCE:
    scene maintenance1 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.5
    "Dans la salle de maintenance, plusieurs bacs sont renversés. Une armoire métallique est couchée devant les étagères."
    $ showGroup([("elias", "fatigue", 0.28), ("dg_noam", "neutre", 0.75)])
    dg_noam surpris "Mais qu'est-ce que t'as foutu ?"
    elias agace "J'ai tiré un tiroir, ça a basculé ! Je sais, c'est débile. Tu peux m'aider, s'il te plaît ?"
    dg_noam reflexion "Ouais, bon. Ça va être lourd."
    elias neutre "Attends, je me mets là. Vas-y, soulève."
    "On pousse l'armoire, qui résiste d'abord avant de racler le sol."
    elias colere "Stop ! Attends, y a une caisse en dessous !"
    "Je m'arrête. Elias tire une caisse coincée sous la tôle et la pose à l'écart."
    elias fatigue "OK. Là, on y va. À trois."
    dg_noam neutre "Un, deux..."
    elias colere "Trois ! Vas-y !"
    "On force ensemble. Le meuble retrouve enfin sa position, dans un grincement insupportable."
    dg_noam fatigue "Ah putain... J'ai cru qu'on allait se la reprendre dessus."
    elias fatigue "Ouais. Faut vraiment que je fixe ce truc."
    "Je ramasse les quelques outils éparpillés autour de nous."
    elias neutre "Laisse, je finirai de ranger."
    dg_noam surpris "T'es sûr ? Y en a encore partout."
    elias fatigue "Ouais, t'inquiète. Retourne voir Iris."
    dg_noam taquin "Quoi ? Pourquoi tu dis ça ?"
    elias neutre "Parce que t'as l'air pressé. Allez, va."
    "Il baisse aussitôt les yeux vers ses outils. Je lui donne une petite tape sur l'épaule."
    dg_noam sourire "Bon... merci. À plus."
    $ hideGroup()
    "Je repars en pensant à Iris. Elle va forcément se moquer de moi en apprenant que ça nous a pris autant de temps."
    jump _29_0_1_1_0_0_1_2_RETOUR

label _29_0_1_1_0_0_1_2_RETOUR:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    "Dans le couloir des chambres, tout est calme. Je m'arrête devant la porte d'Iris, puis frappe deux petits coups."
    dg_noam taquin "C'est bon, on a sauvé ton armoire !"
    "Pas de réponse."
    dg_noam sourire "Eh, tu dors ou quoi ?"
    "J'ouvre la porte."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    "Iris est là. Mara et Tomas aussi."
    "Pendant une seconde, je ne comprends pas ce que je vois. Tomas tient Iris contre lui, un torchon plaqué sur son visage."
    "Sa tête repose de travers, beaucoup trop loin sur son épaule."
    "Il la lâche."
    "Elle tombe au sol sans essayer de se rattraper."
    dg_noam surpris "Iris... ?"
    "Mara se retourne brusquement."
    mara inquiet "Merde, il est là."
    "Je regarde Iris. Son bras est resté coincé sous son corps."
    dg_noam inquiet "Mais... Qu'est-ce que vous faites ?"
    "Je fais un pas. Tomas ne me regarde même pas."
    dg_noam peur "IRIS !"
    "Je me mets à rire. Je sais même pas pourquoi. Je voudrais m'arrêter, mais j'y arrive pas."
    dg_noam peur "Non, mais... Iris ? Réponds-moi, putain !"
    "Je m'avance vers elle. Je ne vois même plus Mara bouger."
    "Un choc me frappe à l'arrière du crâne."
    with vpunch
    "La chambre penche d'un seul coup. J'essaie de me retenir au mur, mais mes doigts glissent."
    "Le visage d'Iris se brouille devant moi."
    "Je lui avais dit que je revenais."
    scene black with fade
    pause 1.0
    $ j29_iris_pov_double = False
    jump _29_0_1_1_0_0_1_2_LABO

label _29_0_1_1_0_0_1_2_LABO:
    # Retour au véritable Noam : pas de narration du double après ce point.
    $ current_period = "Soir"
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata_slow.mp3" fadein 1.0
    "La grille du laboratoire s'ouvre. Mara entre la première, suivie de Tomas et d'Elias."
    "Je me lève pour voir ce qu'ils ramènent."
    "Deux corps."
    "Le premier porte mon visage. L'autre est Iris."
    "J'ai à peine le temps de les reconnaître que mon estomac se soulève. Je me précipite vers une poubelle et je vomis."
    $ showGroup([("noam", "desespoir", 0.29), ("kael", "inquiet", 0.72)])
    kael inquiet "Noam, assieds-toi. T'es blanc comme un linge."
    noam peur "C'est... c'est mon double..."
    "Je m'essuie la bouche du revers de la main. Mon double ne bouge plus. Iris non plus."
    noam colere "Vous deviez l'éloigner !"
    mara fatigue "C'est ce qu'on a fait. Mais il est revenu."
    noam colere "Et vous l'avez buté, lui aussi ?!"
    tomas fatigue "Il a vu Iris. Il a commencé à gueuler. On savait plus quoi faire."
    noam desespoir "Putain... putain..."
    "Je voulais récupérer ma place. Maintenant mon double est là, sans bouger."
    "Iris lui faisait confiance. Et moi, je l'ai quand même choisie."
    nyra raison "Noam, regarde ailleurs. Ils vont lancer la machine."
    noam colere "Regarder ailleurs ? Mais tu te fous de moi ?!"
    nyra neutre "Tu peux t'énerver après. Là, laisse-les travailler."
    "J'ouvre la bouche, mais rien ne sort."
    $ hideGroup()
    "Elias écarte des instruments sur l'établi. Kael rallume les écrans de la machine."
    $ showGroup([("kael", "reflexion", 0.16), ("elias", "fatigue", 0.40), ("tomas", "inquiet", 0.64), ("noam", "fatigue", 0.86)])
    elias fatigue "J'ai gardé les réglages de la dernière fois. Par contre, faut pas que ça bloque au démarrage."
    kael neutre "Ouais, je lance ça. Tomas, t'as son affaire ?"
    tomas neutre "Ouais, tiens."
    "Il dépose un petit objet personnel d'Iris sur la table, à côté du terminal. Personne ne le lui donne encore."
    kael calme "On fait le corps d'abord. Après, on lui donne l'objet."
    elias fatigue "Ouais, OK."
    "Le système se met en marche. Je reste contre le mur, incapable de détacher les yeux de la machine."
    "Les indicateurs défilent. Kael vérifie deux fois les paramètres, puis retire ses mains des commandes."
    elias surpris "Hé, attends... Elle bouge, là ?"
    kael surpris "Quoi ? Mais on lui a même pas donné l'objet !"
    "À l'intérieur, la nouvelle Iris remue les doigts."
    "Elle ouvre les yeux."
    $ j29_iris_double_created = True
    $ hideGroup()
    jump _29_0_1_1_0_0_1_2_REVELATION

label _29_0_1_1_0_0_1_2_REVELATION:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "surpris", 0.27), ("elias", "surpris", 0.53), ("noam", "surpris", 0.79)])
    iris surpris "Alors ? Ça a marché ?"
    "Sa voix me fait sursauter. C'est la même que tout à l'heure, dans ma tête. Mais elle sourit."
    iris joie "Attendez, là... Je suis vraiment réveillée ?!"
    elias surpris "Euh... Ouais. Apparemment."
    iris sourire "Mais c'est dingue ! Ça marche !"
    "Elle regarde ses mains, puis les commandes au-dessus d'elle."
    iris reflexion "Attends... Pourquoi on est pas dans la même salle ?"
    "Son sourire disparaît lorsqu'elle remarque nos visages."
    iris inquiet "Euh... Vous êtes qui ?"
    noam inquiet "Iris ? Tu... tu me reconnais pas ?"
    iris surpris "Ben non. On se connaît ?"
    tomas inquiet "Putain, elle nous connaît pas..."
    iris colere "Mais c'est qui, tout le monde, là ? Et Reus, il est où ?"
    kael surpris "Reus ?"
    iris inquiet "Bah oui, Reus ! Il devait venir voir le résultat. Il est passé où ?"
    "Elle se redresse trop vite, jette un regard autour d'elle et recule sur la table d'examen."
    iris peur "Attendez... Je suis où, exactement ? C'est quoi cet endroit ?"
    noam raison "On est au Conclave. Sur une station spatiale."
    iris inquiet "Au Conclave ? C'est quoi, ça ?"
    elias fatigue "C'est... enfin, on est des représentants. On est là pour voter."
    iris colere "Voter sur quoi ?!"
    noam raison "Sur les Commandements de Kami. On essaie de les changer."
    iris surpris "Attends, les commandements de qui ?"
    noam inquiet "De Kami."
    iris reflexion "C'est qui, Kami ?"
    "Personne ne répond tout de suite. Je regarde Kael. Lui aussi semble perdu."
    iris peur "Non mais vous pouvez m'expliquer ce qui se passe ? Pourquoi vous me regardez tous comme ça ?"
    "Elle se tourne vers le terminal de fabrication. Son expression change."
    iris reflexion "Mmh... Bon, y a encore des bugs, apparemment. Ça, je devrais pouvoir le régler."
    noam surpris "Attends, quoi ? Tu sais te servir de cette machine ?"
    iris colere "MAIS ENFIN, J'AI PARTICIPÉ À LA CRÉATION DE CETTE MACHINE, ÉVIDEMMENT !"
    $ hideGroup()
    stop music fadeout 0.2
    scene black with fade
    pause 1.2
    call show_chapter_title("Fin du chapitre 9", "Chapitre 9 — Le dernier départ")
    return
