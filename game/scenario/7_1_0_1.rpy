default j7_1_0_1_anya_declared = False
default j7_1_0_1_anya_departure_day = 14
default j7_1_1_1_transport_qte_step = 0


# Nom canonique de la branche "déclarer la jeune femme".
label _7_1_0_1_CANON:

    call play_stat_dialogue("d7_1_0_1") from _call_stat_dialogue_d7_1_0_1

    jump _7_1_0_DECLARER_PLACEHOLDER


label _7_1_0_DECLARER_PLACEHOLDER:

    $ j7_1_0_1_anya_declared = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"

    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    $ cafeteria_food_level = "high"

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    think "Je regarde la jeune femme recroquevillée entre les conteneurs. Chaque respiration semble lui demander un effort immense."
    think "La cacher nous donnerait peut-être une chance de la sauver. Peut-être. Mais au prix d'un mensonge que Kami finirait forcément par découvrir."

    noam determine "On prévient Kami."

    iris colere "Tu es sérieux ?"

    noam inquiet "Si on la déplace en secret et qu'elle meurt, on ne pourra même pas appeler à l'aide."

    nyra raison "Et si Kami décide de l'exécuter ?"

    noam determine "Alors on l'en empêchera. Mais là, elle a besoin de soins tout de suite."

    tomas inquiet "Comment est-ce qu'on empêche Kami de faire quoi que ce soit ?"

    noam raison "Je ne sais pas encore. Mais je sais qu'on n'arrivera pas à la réchauffer avec une veste et quatre personnes qui paniquent autour d'elle."

    iris desaccord "Je déteste ce choix."

    noam triste "Moi aussi."

    pause 0.4

    nyra raison "Très bien. Mais nous parlons avant qu'elle impose sa version des règles."

    think "Nyra se tourne vers la caméra fixée au-dessus de la porte. Son voyant reste parfaitement blanc."

    nyra determine "Kami. Nous savons que tu nous regardes. Il y a une personne vivante dans la livraison."

    pause 0.8

    think "Aucune réponse. Tomas lève les yeux vers la caméra, puis les baisse aussitôt."

    tomas inquiet "Elle nous a entendus ?"

    iris colere "Évidemment qu'elle nous a entendus. Elle fait durer."

    noam colere "Kami ! Elle est en hypothermie. Si tu veux discuter, fais-le maintenant."

    stop music fadeout 0.5
    play sound sfx_announce

    $ hideGroup()

    jump _7_1_0_1_KAMI_SAS


label _7_1_0_1_KAMI_SAS:

    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, Noam. Moi aussi, je suis ravie de te voir."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je comptais justement vous féliciter pour votre remarquable découverte. Une chaussure humaine au milieu des conserves, ça réveille mieux qu'un café."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Écartez-vous de l'intruse."

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "determine"),
        ("tomas", "inquiet"),
        ("iris", "colere"),
        ("noam", "determine"),
    ])

    think "Un mécanisme lourd se met en mouvement derrière la paroi. Je reconnais ce grondement."
    think "Le canon."

    iris peur "Non..."

    tomas inquiet "Elle va vraiment tirer ici ?"

    nyra determine "Personne ne bouge."

    noam colere "Kami, arrête."

    $ hideGroup()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Elle a franchi une frontière clandestinement, s'est introduite dans mon Conclave et s'est dissimulée dans ma livraison."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Je vais simplement corriger cette petite erreur logistique."

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "colere"),
    ])

    nyra raison "En vertu de quelle règle ?"

    pause 0.5

    nyra determine "Les Commandements sont suspendus dans le Conclave. Tu nous l'as toi-même confirmé."

    noam surpris "Nyra..."

    nyra raison "Et aucune règle du Conclave n'interdit à une personne non représentante d'y entrer."

    iris determine "Elle n'a agressé personne. Elle n'a rien volé. Elle est juste en train de mourir de froid."

    tomas inquiet "D'un point de vue strictement juridique, l'entrée dans le sas n'est pas définie comme..."

    tomas panne "Enfin, Nyra a raison. Ce n'est pas interdit."

    $ hideGroup()

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Elle n'est pas entrée. Elle a été importée. Sans déclaration, sans autorisation et sans la moindre étiquette."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Vous ne transformerez pas une intrusion en vide juridique simplement parce que j'ai oublié d'écrire : ne voyagez pas avec les pommes de terre !"

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("iris", "colere"),
        ("noam", "determine"),
    ])

    nyra raison "Tu peux trouver ça impoli. Kael vient de démontrer hier que l'impolitesse n'est pas une infraction."

    iris taquin "Elle marque un point."

    noam raison "Même si tu refuses cet argument, tu ne peux pas utiliser ton canon ici."

    $ hideGroup()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je ne peux pas ?"

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "determine"),
        ("tomas", "inquiet"),
        ("iris", "inquiet"),
        ("noam", "determine"),
    ])

    noam determine "Regarde où elle se trouve."

    noam raison "Si tu tires, le rayon traversera le sas. Il percera la coque ou détruira les systèmes de livraison."

    noam determine "Dans les deux cas, ton Conclave s'arrête aujourd'hui. Plus de représentants, plus de votes, plus de petit jeu."

    nyra raison "Et même si le sas résistait, tu contaminerais ou détruirais une partie des ressources que tu viens de nous envoyer."

    iris colere "Alors rengaine ton jouet et laisse-nous la soigner."

    pause 0.8

    think "Le grondement continue encore quelques secondes. Puis le mécanisme s'immobilise."

    tomas inquiet "Elle a arrêté ?"

    noam neutre "Je crois."

    $ hideGroup()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Je vous déteste quand vous devenez raisonnables en groupe."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Très bien. Puisque cette personne n'a techniquement enfreint aucune règle applicable à l'intérieur du Conclave, elle ne sera pas exécutée."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Mais elle ne fait pas partie des douze représentants. Elle ne participera à aucun débat officiel, ne proposera aucun texte et ne prendra part à aucun vote."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Et je refuse catégoriquement qu'elle s'installe ici. Elle repartira au jour quatorze, lors de la prochaine livraison."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Si elle tient absolument à voyager dans une caisse, je suis certaine que le trajet retour lui plaira."

    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("nyra", "raison"),
        ("tomas", "inquiet"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    iris determine "Elle doit d'abord survivre jusqu'au jour quatorze. Ouvre l'infirmerie."

    $ hideGroup()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Quelle délicatesse dans la formulation."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "L'accès est autorisé. Sael et Elias ont été prévenus. Transportez-la sans la faire tomber, ce serait une conclusion terriblement médiocre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    jump _7_1_0_1_TRANSPORT_INFIRMERIE


label _7_1_0_1_TRANSPORT_INFIRMERIE:

    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ showGroup([
        ("nyra", "inquiet"),
        ("tomas", "determine"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    think "Le silence retombe dans le sas. Pour la première fois depuis notre arrivée, nous venons de forcer Kami à reculer."
    think "La jeune femme, elle, ne sait même pas que sa vie vient de faire l'objet d'un débat."

    iris determine "Tomas, prends-la sous les épaules. Noam, les jambes."

    tomas inquiet "Je vais essayer de ne pas lui faire mal."

    iris colere "N'essaie pas. Fais-le."

    noam determine "À trois. Un... deux... trois."

    $ j7_1_1_1_transport_qte_step = 1
    call screen trace_qte(path_type="vertical_up", time_limit=6.0, wait_time=0.8, tolerance=50, max_errors=3, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j7111_qte_1 = _return
    if not _j7111_qte_1["success"]:
        call _7_1_1_1_QTE_ECHEC(1) from _call_j7111_qte_fail_1

    think "Nous la soulevons avec les couvertures de transport. Son corps est léger, beaucoup trop léger."

    nyra raison "Je passe devant."

    iris inquiet "Gardez sa tête droite. Sa respiration est déjà assez mauvaise comme ça."

    $ hideGroup()

    scene bg_dortoir at adaptive_fullscreen with dissolve

    think "Nous traversons le couloir sans avoir à courir ni à éviter les caméras."
    think "Tous leurs voyants suivent notre progression. Pour une fois, être observés nous protège davantage que cela ne nous menace."

    iris determine "Ralentissez au virage. Gardez son bassin au même niveau que ses épaules."

    $ j7_1_1_1_transport_qte_step = 2
    call screen trace_qte(path_type="s_curve", time_limit=6.5, wait_time=0.7, tolerance=46, max_errors=3, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j7111_qte_2 = _return
    if not _j7111_qte_2["success"]:
        call _7_1_1_1_QTE_ECHEC(2) from _call_j7111_qte_fail_2

    nyra determine "L'infirmerie est ouverte. Encore quelques mètres."

    think "Le seuil est étroit. Tomas pivote le premier pendant que je dois maintenir tout le poids sans cogner le chambranle."

    $ j7_1_1_1_transport_qte_step = 3
    call screen trace_qte(path_type="curve_left", time_limit=5.5, wait_time=0.6, tolerance=44, max_errors=2, anchor_x=960, anchor_y=610, challenges_hud=False)
    $ _j7111_qte_3 = _return
    if not _j7111_qte_3["success"]:
        call _7_1_1_1_QTE_ECHEC(3) from _call_j7111_qte_fail_3

    jump _7_1_0_1_INFIRMERIE_MATIN


label _7_1_1_1_QTE_ECHEC(qte_index=1):

    if qte_index == 1:
        think "La couverture se replie sous son dos et son épaule redescend brutalement."
        pause 1.0
        iris colere "Stop. Ne tirez pas sur ses bras. Reprenez sous les omoplates."
        pause 1.0
        tomas inquiet "Le tissu glisse, je n'arrive pas à la stabiliser."
        pause 1.0
        noam determine "Je remonte ses jambes. Reprends ta prise maintenant."
        pause 1.0
        think "Nous corrigeons le portage avant de repartir, avec plusieurs secondes perdues."
    elif qte_index == 2:
        think "Dans le virage, mon épaule heurte le mur et tout le poids bascule vers Tomas."
        pause 1.0
        tomas peur "Attends ! Je la perds !"
        pause 1.0
        iris colere "Plaquez-vous contre le mur et remettez-la droite."
        pause 1.0
        noam inquiet "C'est bon. J'ai retrouvé son bassin. On repart doucement."
        pause 1.0
        think "Nous retrouvons notre équilibre, mais notre progression s'est nettement ralentie."
    else:
        think "Le montant de la porte accroche la couverture et nous force à nous immobiliser."
        pause 1.0
        nyra colere "Ne tirez pas, vous allez la faire tomber. Je dégage le tissu."
        pause 1.0
        iris inquiet "Maintenez sa tête. Sa respiration devient irrégulière."
        pause 1.0
        tomas determine "Je tiens. Faites vite."
        pause 1.0
        think "Nyra libère enfin la couverture et nous franchissons le seuil avec retard."

    return


label _7_1_0_1_INFIRMERIE_MATIN:

    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "infirmerie2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_J7101_01
    scene infirmerie2 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("sael", "inquiet"),
        ("elias", "inquiet"),
        ("nyra", "raison"),
        ("tomas", "determine"),
        ("iris", "determine"),
        ("noam", "inquiet"),
    ])

    think "Sael a déjà dégagé un lit. Elias pousse contre le mur un appareil de chauffage monté sur un pied métallique."

    sael determine "Posez-la ici. Doucement."

    elias inquiet "Le chauffage est à fond, mais collez pas le truc contre elle. On la réchauffe, on la cuit pas."

    $ anya_lit_infirmerie = 1
    think "Tomas et moi déposons la jeune femme sur le lit. Sael glisse immédiatement une main sous sa nuque."

    sael inquiet "Depuis combien de temps est-elle inconsciente ?"

    iris desaccord "On n'en sait rien. Elle était déjà comme ça quand on l'a trouvée."

    sael determine "Respiration faible. Pouls lent. Elias, les poches chauffantes."

    elias determine "J'en ai quatre. Deux sont encore froides."

    iris colere "Alors active-les au lieu de faire l'inventaire."

    elias colere "Je sais, bordel. J'essaie juste de pas faire une connerie."

    nyra raison "Vous avez besoin de nous ?"

    sael determine "Pas tous. Trop de monde ne fera que nous gêner. Iris peut rester."

    noam inquiet "Elle va survivre ?"

    sael triste "Je ne vais pas te répondre au hasard pour te rassurer."

    sael determine "Sa température est dangereusement basse, mais elle respire encore. Pour le moment, c'est tout ce que je peux affirmer."

    pause 0.4

    iris determine "Je reste avec eux."

    tomas inquiet "On devrait peut-être chercher son identité. Dans les registres de la livraison, il y a forcément..."

    nyra raison "Plus tard. Laissons-les travailler."

    noam neutre "Prévenez-nous dès qu'elle se réveille."

    sael determine "Si elle se réveille."

    $ hideGroup()

    think "Sael se détourne déjà de nous. Elias ouvre un compartiment de matériel et Iris remonte les couvertures jusqu'au menton de la jeune femme."
    think "Nous quittons l'infirmerie avec le sentiment d'avoir fait le seul choix possible, sans savoir s'il était le bon."

    stop music fadeout 0.8

    jump _7_1_0_1_ANNONCE_INVITEE


label _7_1_0_1_ANNONCE_INVITEE:

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("mara", "mefiant"),
        ("elias", "neutre"),
        ("lysa", "blase"),
        ("noam", "inquiet"),
        ("iris", "inquiet"),
        ("tomas", "inquiet"),
        ("elen", "surpris"),
        ("julian", "inquiet"),
        ("kael", "reflechit"),
        ("nyra", "raison"),
        ("ryn", "fatigue"),
        ("sael", "neutre"),
    ])

    think "Une heure plus tard, Kami exige que nous nous réunissions à la cafétéria."
    think "Sael et Elias ont quitté l'infirmerie le temps de l'annonce. Iris surveille la porte depuis l'autre bout de la pièce."

    ryn surpris "Donc quelqu'un a vraiment traversé la frontière dans la livraison ?"

    noam raison "On ne sait pas encore d'où elle vient ni comment elle est montée dans la capsule."

    mara mefiant "Et Kami a accepté de la garder ici ? Comme ça ?"

    lysa blase "Non. Kami a accepté de ne pas tirer dans sa propre maison. Nuance."

    julian inquiet "Elle est consciente ?"

    sael neutre "Pas encore."

    elen inquiet "Elle va s'en sortir ?"

    elias neutre "On fait ce qu'on peut."

    play sound sfx_announce

    $ hideGroup()

    stop music fadeout 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Maintenant que tout le monde connaît la nouvelle, permettez-moi de vous présenter officiellement votre invitée indésirable !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Une jeune femme sans badge, sans invitation et, pour l'instant, sans la courtoisie élémentaire de nous donner son nom."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Elle restera à l'infirmerie jusqu'à ce que son état permette de la déplacer. Elle quittera ensuite le Conclave lors de la livraison du jour quatorze."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Je vous rappelle qu'elle n'est pas une représentante. Elle n'a aucune voix, aucun siège et aucun droit d'interrompre vos débats avec ses opinions de passagère clandestine."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "En revanche, elle possède une bouche. Une bouche supplémentaire, précisément."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Les portions du Conclave ont été calculées pour douze personnes. Vous êtes désormais treize à consommer l'air, l'eau et surtout la nourriture que j'avais si généreusement prévue."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Je vous laisse donc décider qui mangera un peu moins. Voilà une charmante occasion de transformer votre compassion en quantité mesurable !"

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("mara", "colere"),
        ("elias", "mefiant"),
        ("lysa", "blase"),
        ("noam", "colere"),
        ("iris", "colere"),
        ("tomas", "inquiet"),
        ("elen", "triste"),
        ("julian", "inquiet"),
        ("kael", "triste"),
        ("nyra", "raison"),
        ("ryn", "colere"),
        ("sael", "mefiant"),
    ])

    ryn colere "Tu viens de rétablir le commerce. Fais venir une portion de plus."

    $ hideGroup()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Quelle excellente suggestion ! Elle arrivera avec la prochaine livraison. Celle qui la ramènera."

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("mara", "colere"),
        ("elias", "mefiant"),
        ("lysa", "blase"),
        ("noam", "determine"),
        ("iris", "colere"),
        ("tomas", "inquiet"),
        ("elen", "triste"),
        ("julian", "inquiet"),
        ("kael", "triste"),
        ("nyra", "raison"),
        ("ryn", "colere"),
        ("sael", "mefiant"),
    ])

    noam determine "On répartira nos portions. Personne ne la laissera mourir de faim."

    nyra raison "Et puisque tu as officiellement reconnu sa présence, chaque prélèvement à l'infirmerie sera justifié."

    $ hideGroup()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Oui, Nyra. J'avais compris la conséquence de ma propre décision. Merci."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Occupez-vous d'elle. J'aimerais au moins savoir qui a eu l'audace de s'expédier jusqu'ici avant de la renvoyer."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("mara", "mefiant"),
        ("elias", "neutre"),
        ("lysa", "blase"),
        ("noam", "inquiet"),
        ("iris", "inquiet"),
        ("tomas", "inquiet"),
        ("elen", "triste"),
        ("julian", "inquiet"),
        ("kael", "reflechit"),
        ("nyra", "raison"),
        ("ryn", "colere"),
        ("sael", "neutre"),
    ])

    pause 0.5

    mara mefiant "Bon. Qui veut mon dessert ?"

    elen triste "Mara..."

    mara neutre "Quoi ? Elle aura besoin de manger quand elle se réveillera. Moi, je survivrai sans crème au chocolat."

    lysa taquin "Le sacrifice ultime. On devrait graver une plaque."

    julian sourire "Je cède également le mien. Avec un peu plus de dignité, si possible."

    ryn determine "On fera un roulement. Une petite partie de chaque plateau."

    sael neutre "Elle n'avalera rien de solide aujourd'hui. Gardez vos effets d'annonce pour plus tard."

    iris desaccord "Sael a raison. Pour l'instant, elle a surtout besoin qu'on arrête de parler d'elle comme si elle était déjà réveillée."

    noam neutre "Retournez manger. On fera le point cet après-midi."

    $ hideGroup()

    think "Les conversations reprennent lentement, mais personne ne parvient à revenir à la routine."
    think "Une treizième place n'a même pas été ajoutée à la table. Pourtant, son absence occupe déjà toute la pièce."

    stop music fadeout 0.8

    jump _7_1_0_1_APRES_MIDI


label _7_1_0_1_APRES_MIDI:

    $ current_period = "Après-midi"

    scene bg_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "L'après-midi commence sans nouvelle de l'infirmerie."
    think "Sael nous a demandé de ne pas venir toutes les cinq minutes. Pour une fois, la meilleure manière d'aider consiste à la laisser travailler."

    stop music fadeout 0.8

    call START_FREE_TIME("_7_1_0_1_APRES_TEMPS_LIBRE") from _call_START_FREE_TIME_J7101_01


label _7_1_0_1_APRES_TEMPS_LIBRE:

    $ current_period = "Fin d'après-midi"

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Mon temps libre terminé, je retourne vers l'infirmerie."
    think "Cette fois, personne ne m'arrête devant la porte."

    stop music fadeout 0.8

    jump _7_1_0_1_INFIRMERIE_APRES_MIDI


label _7_1_0_1_INFIRMERIE_APRES_MIDI:

    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "infirmerie2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_J7101_02
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0

    $ showGroup([
        ("sael", "fatigue"),
        ("elias", "fatigue"),
        ("noam", "inquiet"),
    ])

    think "La jeune femme repose toujours au centre du lit. Le givre a disparu de ses cheveux, mais son visage reste livide."
    think "Sael est assise près d'elle. Elias maintient ouvert le boîtier du chauffage avec un tournevis."

    noam inquiet "Elle ne s'est toujours pas réveillée ?"

    sael fatigue "Non."

    noam inquiet "Mais elle va mieux ?"

    sael neutre "Sa température remonte. Son pouls est plus stable et sa respiration moins difficile."

    elias fatigue "En gros, elle meurt moins que ce matin. C'est déjà ça."

    sael desaccord "La formulation est affreuse."

    elias mefiant "Mais elle est vraie."

    noam raison "Vous avez trouvé son nom ?"

    sael neutre "Aucun document. Aucun badge. Rien dans ses vêtements."

    elias neutre "Juste un bout de tissu cousu dans sa veste. J'ai regardé, y a rien d'écrit dessus."

    noam reflechit "Elle a peut-être retiré tout ce qui pouvait permettre de la suivre."

    sael raison "Ou quelqu'un l'a fait à sa place. Nous n'en savons rien."

    pause 0.4

    think "Je m'approche du lit. Sa respiration reste faible, mais elle ne produit plus le bruit rauque de ce matin."

    noam inquiet "Elle peut rester inconsciente combien de temps ?"

    sael neutre "Quelques heures. Davantage. Cela dépend de ce qu'elle a subi avant d'arriver."

    noam triste "Et si elle ne se réveille pas ?"

    sael desaccord "Alors nous gérerons ce problème lorsqu'il se présentera. Pas avant."

    elias neutre "On va continuer à la chauffer doucement. Le machin tient, mais faut le surveiller."

    noam surpris "Tu l'as réparé ?"

    elias mefiant "Réparé, c'est un grand mot. Disons qu'il a arrêté de faire des étincelles."

    sael colere "Il en a fait une seule."

    elias colere "Une étincelle dans une infirmerie, c'est déjà une de trop."

    pause 0.4

    noam neutre "Je peux prendre le relais pour la surveiller."

    sael determine "Non. Tu ne sais pas quoi surveiller."

    noam desaccord "Je peux au moins rester là pendant que vous mangez."

    sael raison "Iris viendra dans quelques minutes. Elias et moi partirons ensuite."

    elias neutre "On s'en occupe. Va respirer un coup."

    noam inquiet "Prévenez-moi dès qu'elle ouvre les yeux."

    sael neutre "Nous préviendrons tout le monde. Sa présence n'est plus un secret."

    think "Je hoche la tête. Cette évidence devrait me rassurer. Pourtant, je continue d'avoir l'impression que chaque caméra braquée sur elle attend une faute."

    play sound sfx_announce

    pause 0.5

    elias mefiant "Ça, c'est pour nous ?"

    sael fatigue "Avec Kami, tout finit toujours par être pour nous."

    $ hideGroup()

    stop music fadeout 0.5

    jump _7_1_0_1_ANNONCE_VOTE


label _7_1_0_1_ANNONCE_VOTE:

    $ current_period = "Soir"

    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_system_override.mp3" fadein 1.0

    $ showGroup([
        ("mara", "mefiant"),
        ("elias", "fatigue"),
        ("lysa", "blase"),
        ("noam", "neutre"),
        ("iris", "inquiet"),
        ("tomas", "neutre"),
        ("elen", "inquiet"),
        ("julian", "neutre"),
        ("kael", "reflechit"),
        ("nyra", "raison"),
        ("ryn", "fatigue"),
        ("sael", "fatigue"),
    ])

    think "Kami nous convoque dans la salle du Conclave avant le dîner."
    think "Iris arrive la dernière. Elle confirme d'un signe que la jeune femme respire toujours, puis rejoint sa place."

    $ hideGroup()

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui

    kami "Mes chers représentants, les distractions de ce matin ont légèrement perturbé notre programme."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Entre la passagère congelée, les menaces de perforation de coque et votre soudaine passion pour les subtilités juridiques, je n'ai même pas pu annoncer votre prochain vote."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Nous allons donc parler du Commandement IV, celui qui interdit les rassemblements et les organisations non autorisées."

    pause 0.4

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "La proposition soumise au vote sera la suivante : autoriser les regroupements de plus de vingt personnes, sous réserve d'une demande d'autorisation préalable."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Le lieu, la date, l'objet du rassemblement et l'identité des organisateurs devront être communiqués à Archive avant toute réunion."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Une liberté sous formulaire. C'est presque poétique."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu à la fin du jour neuf. Vous disposez donc de deux jours pour déterminer si vingt et une personnes constituent une communauté ou déjà une menace."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Et puisque vous avez réclamé l'application exacte des règles ce matin, j'attends de vous une rigueur exemplaire. Aucun argument improvisé, aucune interruption et, idéalement, aucun coup au visage."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ showGroup([
        ("mara", "mefiant"),
        ("elias", "fatigue"),
        ("lysa", "blase"),
        ("noam", "reflechit"),
        ("iris", "inquiet"),
        ("tomas", "reflechit"),
        ("elen", "inquiet"),
        ("julian", "neutre"),
        ("kael", "reflechit"),
        ("nyra", "raison"),
        ("ryn", "determine"),
        ("sael", "fatigue"),
    ])

    ryn determine "Des regroupements autorisés pourraient permettre aux familles séparées de se retrouver et de s'organiser."

    sael mefiant "Ou aux réseaux qui utilisent les cargaisons de recruter plus facilement."

    nyra raison "Nous ignorons encore si cette femme appartenait à un réseau."

    lysa blase "Attendez au moins qu'elle se réveille avant de transformer son coma en argument électoral."

    noam determine "Lysa a raison. On en parlera demain."

    iris colere "Demain. Quand j'aurai dormi et qu'elle aura, avec un peu de chance, fait la même chose."

    $ hideGroup()

    think "Nous quittons la salle sans commencer le débat. Pour une fois, personne ne cherche à retenir les autres."

    stop music fadeout 0.8

    jump _7_1_0_1_SOIR


label _7_1_0_1_SOIR:

    $ current_period = "Nuit"

    scene bg_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Je retourne vers ma chambre. La porte de l'infirmerie reste fermée, mais sa lumière est encore allumée."
    think "La jeune femme n'a toujours pas ouvert les yeux. Pourtant, elle a déjà obtenu une semaine de sursis et changé le prochain débat."
    think "Au jour quatorze, Kami exigera qu'elle reparte. D'ici là, il faudra découvrir qui elle est et ce qu'elle fuyait."

    stop music fadeout 1.0
    scene black with fade

    call end_day("8") from _call_end_day_7111
    # Les deux routes du chapitre rejoignent la même chronologie au jour 7.
    jump patreon_ending
