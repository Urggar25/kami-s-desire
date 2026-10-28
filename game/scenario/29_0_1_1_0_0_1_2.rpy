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
    "Je me réveille sur la banquette du laboratoire avec la bouche sèche et l'impression d'avoir passé la nuit à réfléchir."
    "La dernière chose que j'ai vue avant de dormir, c'est le message d'Iris. Elle a dit oui à mon double."
    "J'ai choisi Iris. Pas parce que je veux lui faire du mal. Parce que je ne vois plus comment récupérer ma place autrement."
    "Si mon double retourne sur Terre à ma place, Juliette l'accueillera comme son frère. Et moi, je resterai ici."
    "Il me paraît gentil. C'est peut-être ce qui m'inquiète le plus : je ne saurais même pas comment l'obliger à partir s'il changeait d'avis."
    "En faisant remplacer Iris, j'espère provoquer un changement qui me permettra d'échanger nos places sans que les autres s'en aperçoivent."
    "Je sais ce que ça implique. J'essaie seulement de ne pas y penser."
    $ showGroup([("nyra", "neutre", 0.20), ("noam", "fatigue", 0.52), ("kael", "calme", 0.81)])
    nyra neutre "Tu es réveillé. Bien. On a arrêté le plan."
    noam inquiet "Déjà ?"
    kael calme "Elias a préparé le matériel. Mara et Tomas s'occuperont d'Iris. Elias va éloigner ton original."
    noam surpris "Pourquoi mon original ?"
    nyra raison "Parce qu'il est toujours avec elle. Il doit quitter la pièce avant qu'on intervienne."
    noam inquiet "Je peux aider. Je la connais, je peux lui parler."
    nyra neutre "Non. Tu restes ici."
    noam colere "Quoi ? Mais c'est moi qui ai choisi Iris !"
    nyra raison "Justement. Regarde-toi. Tu trembles depuis que je suis entrée."
    noam desaccord "Ça va. Je peux me contrôler."
    nyra raison "Tu n'arrives même pas à soutenir mon regard. Si tu paniques devant elle, toute l'opération échoue."
    noam inquiet "Et si quelque chose tourne mal ?"
    nyra neutre "Tu ne pourras rien arranger en étant sur place."
    kael inquiet "Nyra a raison sur un point : tu es trop mal pour faire ça. On te préviendra quand ce sera terminé."
    noam colere "Vous me demandez de rester assis pendant que vous allez la tuer ?"
    nyra raison "Je t'interdis de participer. Et si tu comptes sortir d'ici pour intervenir, dis-le tout de suite."
    "Je regarde la grille. Elle n'est pas verrouillée. Mais Kael attend ma réponse, lui aussi."
    noam fatigue "Non. Je bougerai pas."
    nyra neutre "Bien."
    "Elle se détourne déjà pour vérifier son terminal."
    noam reflexion "Et mon original ? Vous allez lui faire quoi ?"
    kael calme "Il ne faut pas qu'il revienne et qu'il voie les deux Iris. Le reste, on l'a prévu."
    noam inquiet "Kael..."
    kael fatigue "Je sais. Je suis désolé."
    $ hideGroup()
    "Ils repartent. Je garde les yeux sur la grille jusqu'à ce qu'elle se referme."
    "Je pourrais encore courir les prévenir. Iris et lui. Les deux."
    "Mais si je le fais, je leur explique quoi ? Que je me suis fait passer pour mon propre double et que j'ai choisi de la sacrifier ?"
    "Je serre la tablette contre moi."
    "Il ne reste qu'à attendre."
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
    iris agace "Tu prends toute la place. T'es au courant qu'il y a deux personnes, ici ?"
    dg_noam taquin "Je pensais que tu préférais être collée à moi."
    iris surpris "Pardon ?"
    dg_noam sourire "Tu m'as entendu."
    iris agace "Non, j'ai dû mal entendre. Ça sonnait beaucoup trop prétentieux."
    "Elle me donne un petit coup de coude, puis vient s'installer contre mon épaule comme si de rien n'était."
    dg_noam rire "Tu peux juste dire que tu veux un câlin."
    iris agace "Et toi tu peux arrêter de parler."
    "Je ris. Elle ne se décale pas."
    dg_noam neutre "Ça fait du bien, quand même."
    iris reflexion "Quoi ? D'être insupportable ?"
    dg_noam sourire "Non. D'être ici. Avec toi."
    "Elle baisse les yeux vers nos mains, qu'elle a fini par joindre sans s'en rendre compte."
    iris hesitation "Ouais... C'est pas désagréable."
    dg_noam taquin "Ah ! Un compliment."
    iris colere "J'ai dit PAS DÉSAGRÉABLE !"
    dg_noam rire "D'accord, d'accord !"
    "Elle essaie de garder un air fâché, puis finit par rire aussi."
    iris sourire "Tu sais que t'as une façon vraiment nulle de draguer ?"
    dg_noam sourire "Ça a marché, non ?"
    iris taquin "J'ai encore le temps de changer d'avis."
    dg_noam neutre "Je devrais peut-être m'inquiéter."
    iris sourire "Un peu."
    "On reste un moment à discuter de ce qu'on fera après le Conclave. Pour la première fois, ça ressemble à de vrais projets."
    iris reflexion "Je sais même pas comment on va faire avec les déplacements entre districts. Kami va sûrement nous pourrir la vie."
    dg_noam raison "On trouvera. Je peux venir à Nexus."
    iris agace "Tu dis ça comme si c'était à deux rues d'ici."
    dg_noam sourire "Je sais. Mais j'ai envie d'essayer."
    iris inquiet "Tu le penses vraiment ?"
    dg_noam neutre "Oui."
    "Elle tourne la tête vers moi. Cette fois, elle ne fait pas de plaisanterie."
    iris sourire "Moi aussi."
    "Elle m'embrasse rapidement, puis se recule avant que je puisse dire quoi que ce soit."
    iris agace "Bon. Voilà. T'as gagné. Pas un mot."
    dg_noam taquin "Je vais essayer, mais j'ai une mémoire excellente."
    iris colere "NOAM !"
    "On éclate de rire tous les deux."
    "J'aimerais que l'après-midi ne se termine jamais. Quand elle me regarde comme ça, j'oublie presque ce que les autres attendent de moi."
    "Il y a deux petits coups à la porte, puis quelqu'un frappe plus fort."
    elias fatigue "Hé ! Noam ! T'es là ?"
    iris agace "Pitié, qu'est-ce qu'il a encore cassé ?"
    dg_noam neutre "J'arrive !"
    "J'entrebâille la porte. Elias se tient dans le couloir, les manches sales et les cheveux en bataille."
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.28), ("dg_noam", "neutre", 0.73)])
    elias fatigue "Putain, j'ai besoin d'un coup de main."
    dg_noam reflexion "Qu'est-ce qui se passe ?"
    elias agace "Une armoire s'est effondrée dans la maintenance. Y a du matos partout. J'arrive pas à la remettre debout tout seul."
    dg_noam surpris "Une armoire entière ?"
    elias colere "Ouais ! Elle est tombée, j'te dis ! Tu viens ou tu comptes m'interroger jusqu'à demain ?"
    dg_noam sourire "Bon, j'arrive."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "neutre", 0.33), ("dg_noam", "sourire", 0.70)])
    dg_noam neutre "Elias a fait tomber une armoire. Je vais l'aider, je reviens."
    iris blase "Évidemment. Il pouvait pas laisser un meuble tranquille."
    dg_noam sourire "J'en ai pour cinq minutes."
    iris taquin "C'est ce que tu dis toujours."
    "Elle me prend par le col et me vole un dernier baiser."
    iris sourire "Allez, va sauver son armoire. Mais reviens vite."
    dg_noam sourire "Promis."
    $ hideGroup()
    jump _29_0_1_1_0_0_1_2_MAINTENANCE

label _29_0_1_1_0_0_1_2_MAINTENANCE:
    scene maintenance1 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.5
    "Dans la salle de maintenance, plusieurs bacs sont renversés. Une armoire métallique est couchée devant les étagères."
    $ showGroup([("elias", "fatigue", 0.28), ("dg_noam", "neutre", 0.75)])
    dg_noam surpris "Comment t'as réussi à faire ça ?"
    elias agace "Tu vas pas t'y mettre toi aussi ! J'ai tiré sur un tiroir, le truc a basculé, fin de l'histoire."
    dg_noam reflexion "Ça va être lourd."
    elias neutre "Tu prends ce côté. Je soulève l'autre."
    "On pousse l'armoire, qui résiste d'abord avant de racler le sol."
    elias colere "Attends ! Attends, y a un truc dessous !"
    "Je m'arrête. Elias tire une caisse coincée sous la tôle et la pose à l'écart."
    elias fatigue "Bon. On recommence. À trois."
    dg_noam neutre "Un, deux..."
    elias colere "Trois !"
    "On force ensemble. Le meuble retrouve enfin sa position, dans un grincement insupportable."
    dg_noam fatigue "Putain, j'ai cru qu'il allait nous retomber dessus."
    elias fatigue "Ouais. Je vais le fixer cette fois."
    "Je ramasse les quelques outils éparpillés autour de nous."
    elias neutre "Laisse, je vais finir. T'en as déjà fait assez."
    dg_noam surpris "T'es sûr ? Y a encore plein de trucs par terre."
    elias fatigue "Je sais, merci. Je m'en occupe. Retourne voir Iris."
    dg_noam taquin "Ça se voit tant que ça ?"
    elias neutre "Ouais. Allez, file."
    "Il baisse aussitôt les yeux vers ses outils. Je lui donne une petite tape sur l'épaule."
    dg_noam sourire "Merci. À tout à l'heure."
    $ hideGroup()
    "Je repars en pensant à Iris. Elle va forcément se moquer de moi en apprenant que ça nous a pris autant de temps."
    jump _29_0_1_1_0_0_1_2_RETOUR

label _29_0_1_1_0_0_1_2_RETOUR:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    "Dans le couloir des chambres, tout est calme. Je m'arrête devant la porte d'Iris, puis frappe deux petits coups."
    dg_noam taquin "C'est le service de réparation d'armoires !"
    "Pas de réponse."
    dg_noam sourire "Je préviens, j'ai bien mérité un autre câlin."
    "J'ouvre la porte."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    "Iris est là. Mara et Tomas aussi."
    "Pendant une seconde, je ne comprends pas ce que je vois. Tomas tient Iris contre lui, un torchon plaqué sur son visage."
    "Sa tête repose de travers, beaucoup trop loin sur son épaule."
    "Il la lâche."
    "Elle tombe au sol sans essayer de se rattraper."
    dg_noam surpris "Iris... ?"
    "Mara se retourne brusquement."
    mara inquiet "Merde. Déjà ?"
    "Je regarde Iris. Son bras est resté coincé sous son corps."
    dg_noam inquiet "Hé... Hé, arrêtez. C'est quoi, ça ?"
    "Je fais un pas. Tomas ne me regarde même pas."
    dg_noam peur "IRIS !"
    "Un rire m'échappe. Sec, absurde, incontrôlable. Je ris encore alors que j'essaie de prononcer son nom, parce que ça ne peut pas être vrai."
    dg_noam peur "Non... Non, elle était... Elle était là y a cinq minutes..."
    "Je m'avance vers elle. Je ne vois même plus Mara bouger."
    "Un choc me frappe à l'arrière du crâne."
    with vpunch
    "La chambre penche d'un seul coup. J'essaie de me retenir au mur, mais mes doigts glissent."
    "Le visage d'Iris se brouille devant moi."
    "Je voulais juste revenir."
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
    kael inquiet "Noam ? Assieds-toi."
    noam peur "C'est... C'est lui..."
    "Je m'essuie la bouche du revers de la main. Mon double ne bouge plus. Iris non plus."
    noam colere "Vous aviez dit que vous l'éloigneriez !"
    mara fatigue "On l'a éloigné. Il est revenu plus tôt que prévu."
    noam colere "Et alors vous l'avez tué ?!"
    tomas fatigue "Il nous a vus avec Iris. On n'a pas réussi à le calmer."
    noam desespoir "Putain..."
    "Je pensais récupérer sa place. Je ne pensais pas le retrouver étendu sur une table."
    "Iris avait accepté de sortir avec lui hier. Elle lui faisait confiance. Et moi, j'ai décidé qu'on pouvait se servir d'elle."
    nyra raison "Noam. Ne regarde pas les corps. Elias et Kael doivent commencer."
    noam colere "Tu veux que je fasse quoi ? Que je regarde le mur ?!"
    nyra neutre "Je veux que tu ne les empêches pas de terminer. Rien de plus."
    "Je voudrais lui répondre, mais je n'arrive plus à trouver les mots."
    $ hideGroup()
    "Elias écarte des instruments sur l'établi. Kael rallume les écrans de la machine."
    $ showGroup([("kael", "reflexion", 0.16), ("elias", "fatigue", 0.40), ("tomas", "inquiet", 0.64), ("noam", "fatigue", 0.86)])
    elias fatigue "J'ai encore les réglages du dernier essai. Il faut surtout que ça démarre sans se bloquer."
    kael neutre "Je m'occupe de la séquence. Tomas, tu as récupéré l'objet d'Iris ?"
    tomas neutre "Oui. Il est là."
    "Il dépose un petit objet personnel d'Iris sur la table, à côté du terminal. Personne ne le lui donne encore."
    kael calme "D'abord le corps. Ensuite les souvenirs."
    elias fatigue "Ouais. Une chose à la fois."
    "Le système se met en marche. Je reste contre le mur, incapable de détacher les yeux de la machine."
    "Les indicateurs défilent. Kael vérifie deux fois les paramètres, puis retire ses mains des commandes."
    elias surpris "Attends, ça bouge déjà ?"
    kael surpris "Quoi ? On n'a pas lancé le transfert des souvenirs."
    "À l'intérieur, la nouvelle Iris remue les doigts."
    "Elle ouvre les yeux."
    $ j29_iris_double_created = True
    $ hideGroup()
    jump _29_0_1_1_0_0_1_2_REVELATION

label _29_0_1_1_0_0_1_2_REVELATION:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "surpris", 0.27), ("elias", "surpris", 0.53), ("noam", "surpris", 0.79)])
    iris surpris "Alors ?! Ça a marché ?!"
    "Sa voix me fait sursauter. C'est la même que tout à l'heure, dans ma tête. Mais elle sourit."
    iris joie "Attendez... Je suis réveillée ? Ça a vraiment réussi ?!"
    elias surpris "Euh... Ouais. Enfin, on dirait."
    iris sourire "Oh putain ! Mais c'est génial !"
    "Elle regarde ses mains, puis les commandes au-dessus d'elle."
    iris reflexion "Par contre, c'est bizarre... Vous avez changé la salle ?"
    "Son sourire disparaît lorsqu'elle remarque nos visages."
    iris inquiet "Attendez. Vous êtes qui, vous ?"
    noam inquiet "Iris... Tu me reconnais pas ?"
    iris surpris "Je devrais ?"
    tomas inquiet "Elle ne nous connaît pas..."
    iris colere "Et pourquoi je devrais vous connaître ?! Reus est où ?"
    kael surpris "Reus ?"
    iris inquiet "Oui, Reus ! Il devait être là pour les résultats. Où est-ce qu'il est ?"
    "Elle se redresse trop vite, jette un regard autour d'elle et recule sur la table d'examen."
    iris peur "Attendez, on est où, là ? C'est pas le laboratoire !"
    noam raison "On est au Conclave. C'est une station spatiale."
    iris inquiet "Au quoi ?"
    elias fatigue "Le Conclave. On est les représentants... enfin, on est là pour les votes."
    iris colere "Quels votes ?!"
    noam raison "On doit changer les Commandements de Kami. C'est pour ça qu'on est ici."
    iris surpris "Les commandements de qui ?"
    noam inquiet "De Kami."
    iris reflexion "C'est qui, Kami ?"
    "Personne ne répond tout de suite. Je regarde Kael. Lui aussi semble perdu."
    iris peur "Non, mais sérieusement, qu'est-ce qui se passe ? Et pourquoi vous avez tous l'air aussi bizarres ?"
    "Elle se tourne vers le terminal de fabrication. Son expression change."
    iris reflexion "Mmhh... Il doit encore y avoir des bugs. Je devrais pouvoir régler ça !"
    noam surpris "Quoi ? Tu sais comment fonctionne cette machine ?!"
    iris colere "MAIS ENFIN, J'AI PARTICIPÉ À LA CRÉATION DE CETTE MACHINE, ÉVIDEMMENT !"
    $ hideGroup()
    stop music fadeout 0.2
    scene black with fade
    pause 1.2
    call show_chapter_title("Fin du chapitre 9", "Chapitre 9 — Le dernier départ")
    return
