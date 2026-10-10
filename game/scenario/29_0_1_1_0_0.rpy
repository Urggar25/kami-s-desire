# =============================================================================
# JOUR 29 — DE L'AUTRE COTE
# Route 0_1_1_0_0 — suite directe du J28 « Le temps qui reste ».
# Le joueur ignore encore la nature et le nombre des remplaçants.
# =============================================================================

label _29_0_1_1_0_0_REVEIL:
    $ current_day = 29
    $ day_id = 29
    $ current_period = "Matin"

    scene black
    play music "music/bgm_cold_metadata.mp3" fadein 1.5

    "Un coup sec me réveille. Je ne sais pas depuis combien de temps je dors, mais j'ai encore les chaussures aux pieds et le dos douloureux d'avoir dormi recroquevillé sur le bord du lit."
    "Un second coup résonne contre le mur. Cette fois, j'entends aussi le frottement d'un objet lourd que l'on traîne sur le sol."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Iris est déjà assise à côté de moi. Elle me regarde sans bouger et pose lentement un doigt devant ses lèvres."
    "J'ouvre la bouche par réflexe, mais elle secoue immédiatement la tête."

    $ showGroup([
        ("iris", "peur", 0.36),
        ("noam", "inquiet", 0.64),
    ])

    "Un grincement aigu traverse la porte. Puis viennent trois coups rapides, suffisamment violents pour faire trembler la commode que nous avons placée contre l'entrée."
    "Je tends la main vers mon téléphone. Iris m'arrête avant que j'en active l'écran et me montre le bas de la porte. Une ombre passe devant la lumière du couloir."
    "Nous attendons sans un mot."

    play sound sfx_creak volume 0.45

    "Quelque chose cogne contre le chambranle, suivi d'un bruit de visseuse. Je reconnais le ronronnement d'un outil électrique, mais impossible de comprendre ce qu'on est en train d'installer."
    "J'entends parfois des pas s'éloigner, puis revenir. Au moins deux personnes semblent transporter du matériel."
    "L'une d'elles laisse échapper un rire étouffé."

    "Iris serre les dents. Elle tend lentement le bras vers le tournevis posé sur sa table de nuit et le glisse sous son oreiller."
    "Je vérifie l'heure : sept heures quarante-deux. Quand je regarde de nouveau, presque dix minutes se sont écoulées et les coups n'ont toujours pas cessé."
    "Le bruit se déplace parfois le long du mur, du côté de la ventilation, avant de revenir devant la porte. Un objet métallique tombe avec fracas et je sursaute si violemment que le matelas glisse sous moi."

    "Iris me fixe, les yeux écarquillés. De l'autre côté, personne ne réagit."
    "Je finis par m'asseoir contre son lit pour ne plus risquer de faire bouger quoi que ce soit. Elle pose sa main sur mon épaule, sans quitter l'entrée des yeux."
    "La visseuse recommence."

    "Je ne sais plus depuis combien de temps nous attendons. Mes jambes sont engourdies et le voyant de ma tablette, restée sous la couverture, m'obsède presque autant que les coups."
    "Puis la dernière vibration s'arrête."
    "Nous distinguons quelques pas dans le couloir, un petit choc contre le métal et le bruit d'un objet que quelqu'un laisse tomber."
    "Le silence revient enfin."

    pause 1.0

    "Iris attend encore longtemps avant de se pencher vers moi. Quand elle parle, sa voix est à peine audible."

    iris inquiet "T'as entendu la même chose que moi ? Ils étaient en train de travailler juste devant la porte."
    noam inquiet "Ouais... J'ai cru qu'ils essayaient de forcer la serrure, mais ils ont passé un temps fou à déplacer des trucs."
    iris reflexion "Je vais regarder. Reste ici et fais pas de bruit, même si je te demande quelque chose."
    noam desaccord "Iris, attends. Si quelqu'un est encore derrière, on peut pas simplement ouvrir et espérer qu'il soit parti."
    iris determine "Je vais entrouvrir. Je préfère savoir ce qu'ils ont fait plutôt que rester là jusqu'à demain sans même vérifier."

    "Elle repousse la commode de quelques centimètres. Les pieds grincent sur le sol et nous nous figeons tous les deux, mais rien ne se produit dans le couloir."
    "Iris déverrouille la porte avec une lenteur exaspérante et abaisse la poignée."

    play sound sfx_creak volume 0.5

    "La porte s'ouvre à peine. Iris pousse davantage, puis appuie de toute son épaule. Quelque chose de rigide la bloque depuis l'extérieur."
    "Elle me fait signe d'approcher. Je me glisse à côté d'elle et regarde dans l'ouverture."
    "Des planches de bois traversent l'encadrement de part en part. Des plaques métalliques ont été vissées entre elles, à différents angles, et plusieurs tiges semblent avoir été enfoncées jusque dans les murs du couloir."
    "On dirait qu'on a construit un échafaudage contre notre porte. Chaque pièce renforce la suivante, si bien que je serais incapable de dire ce qu'il faudrait retirer en premier."

    noam inquiet "Ils nous ont enfermés..."
    iris colere "Putain, mais c'est quoi ce délire ?! Qui aurait eu le temps de construire un truc pareil ?"

    "Quelque chose bouge derrière les planches."
    "Je distingue d'abord un œil dans l'ombre, puis une mèche de cheveux et le haut d'une joue. Un visage se rapproche jusqu'à occuper presque entièrement l'interstice."
    "Elias."

    $ showGroup([
        ("elias", "sourire", 0.17),
        ("iris", "peur", 0.49),
        ("noam", "inquiet", 0.80),
    ])

    elias sourire "Ah ! Putain, vous êtes réveillés ! On commençait à croire que vous aviez décidé de dormir jusqu'au départ."

    "Sa voix est reconnaissable, mais quelque chose cloche. Certains mots sont prononcés très lentement, et d'autres sortent d'un coup, comme s'il essayait de retrouver sa manière habituelle de parler."
    "Son sourire reste en place alors qu'il change légèrement l'inclinaison de sa tête pour mieux nous voir."

    elias neutre "Vous avez fait quoi, hier ? On vous a cherchés partout. Même Lysa est venue vous voir, et vous l'avez laissée poireauter devant la porte."
    elias sourire "Franchement, c'est vexant. On peut plus se parler, maintenant ? Vous avez peur de nous ou quoi ?"
    iris colere "Enlève ces planches. Tout de suite."
    elias sourire "Oh, doucement ! J'ai passé toute la matinée à monter ça. Vous imaginez le boulot ?"

    "Il passe deux doigts entre les plaques et tapote le bord de la porte, comme pour vérifier l'épaisseur du bois."
    "J'essaye de voir si quelqu'un se tient derrière lui, mais il ne laisse apparaître que son visage et une partie de son épaule."

    noam inquiet "Elias, pourquoi vous avez fait ça ? On vous a rien demandé."
    elias neutre "Bah justement ! Vous voulez plus venir avec les autres, vous répondez à personne et vous restez dans votre chambre. On peut pas vous laisser vous isoler comme ça."
    noam desaccord "Alors vous nous enfermez ? Ça t'arrive d'écouter ce que tu racontes ?!"
    elias sourire "Mais non, Noam. C'est pas pour vous punir. Si vous voulez pas vous mêler au groupe, le groupe va vous aider."

    "Son sourire s'élargit. Je vois maintenant ses dents entre les deux planches et je me demande comment il parvient à rester dans cette position sans avoir mal au cou."
    "Iris recule vers la poignée. Elias laisse sa main descendre dans l'ouverture, puis glisse brusquement tout son avant-bras entre la porte et le chambranle."

    elias sourire "Allez, viens ! Donne-moi au moins ta main, qu'on arrête de—"

    "Iris tire de toutes ses forces."

    play sound sfx_creak volume 0.85
    call impact_fx("brutal", direction="left")

    "La porte heurte le bras d'Elias avec un bruit épouvantable. Je distingue un premier craquement, puis un second, plus sec, comme si quelque chose venait de céder sous le poids du battant."
    "Elias hurle."
    "Iris ne relâche pas immédiatement la poignée. Elle reste penchée contre la porte, les deux mains crispées, tandis qu'Elias frappe contre le bois avec son autre bras."

    elias peur "AAAAH ! PUTAIN ! OUVRE ! OUVRE, MERDE !"
    iris colere "RETIRE TON BRAS !"
    elias peur "J'PEUX PAS ! TU M'AS PÉTÉ LE—"

    "Un troisième craquement retentit lorsque Iris desserre légèrement la porte et qu'Elias arrache enfin son bras de l'ouverture."
    "Je m'attends à entendre ses pas s'éloigner vers l'infirmerie, mais il ne bouge pas."
    "Ses cris s'arrêtent d'un seul coup."

    pause 0.8

    "Quelqu'un renifle derrière les planches. Puis j'entends un petit rire, presque gêné, comme s'il venait de se rendre compte qu'il avait fait trop de bruit."

    elias sourire "Ah... Ahahaha... Putain, Iris ! Vous êtes vraiment pas faciles à aider !"

    "Le rire prend de l'ampleur. Elias respire difficilement entre deux éclats et cogne parfois quelque chose contre la barricade."
    "Iris réussit enfin à verrouiller la porte. Elle garde les mains sur la poignée, incapables de se détacher du métal."

    elias sourire "Bon, on reviendra quand vous serez de meilleure humeur. Faites pas de conneries, hein ? On tient à vous !"

    "Des pas s'éloignent dans le couloir. Le rire les accompagne encore quelques secondes, puis disparaît derrière une porte."
    "Je tire Iris vers moi. Elle résiste d'abord, comme si elle s'attendait à voir le battant s'ouvrir malgré le verrou, puis finit par reculer."

    $ hideGroup()
    $ showGroup([
        ("iris", "peur", 0.35),
        ("noam", "inquiet", 0.65),
    ])

    iris peur "Je lui ai broyé le bras... Noam, t'as entendu ? Je lui ai vraiment broyé le bras."
    noam inquiet "Je sais. Il l'avait coincé dans la porte et il essayait de passer. T'as fait ce que tu pouvais pour qu'il nous lâche."
    iris peur "Mais il rigolait ! Il avait le bras coincé et après... Il rigolait comme si ça lui avait rien fait !"

    "Ses mains tremblent si fort qu'elle n'arrive pas à replacer la commode. Je m'en charge pendant qu'elle recule jusqu'au lit."
    "Lorsqu'elle s'assoit, elle regarde fixement ses doigts, encore rouges d'avoir serré la poignée."
    "Je reste quelques secondes devant elle sans savoir quoi faire, puis m'assois à mon tour."

    noam inquiet "On va pas rouvrir. Pas après ça."
    iris fatigue "J'ai pas l'intention de recommencer."

    "Elle se frotte les bras et relève brusquement la tête vers la ventilation."
    "Je comprends immédiatement ce qu'elle pense. Si Elias a passé la matinée à bloquer la porte, il a peut-être aussi travaillé sur les autres accès."

    $ hideGroup()
    jump _29_0_1_1_0_0_SORTIE


label _29_0_1_1_0_0_SORTIE:
    $ current_period = "Midi"
    call show_custom_title("Un peu plus tard")
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Nous déplaçons le petit meuble sous la grille de ventilation. Iris me passe le tournevis qu'elle a récupéré hier dans la salle de maintenance."
    "Je retire deux vis avant de réaliser qu'elles tournent dans le vide. La grille ne bouge pas d'un millimètre."
    "En éclairant les bords avec mon téléphone, j'aperçois une plaque supplémentaire derrière les barreaux. Elle a été fixée de l'autre côté, et ses attaches sont hors de portée."

    $ showGroup([
        ("iris", "inquiet", 0.35),
        ("noam", "reflexion", 0.65),
    ])

    noam inquiet "Ils ont aussi fermé la ventilation. Même en arrachant la grille, on tomberait sur cette plaque."
    iris colere "Évidemment. Ils connaissent les conduits, ils savent très bien qu'on pourrait essayer de passer par là."
    noam reflexion "On pourrait peut-être attaquer les fixations par les côtés, mais il faudrait un outil électrique. Avec ce tournevis, je vais juste abîmer le mur."
    iris fatigue "Et si on faisait assez de bruit pour qu'ils viennent vérifier, on serait encore moins avancés."

    "Je repose la grille sans remettre les vis, puis tente de contacter Julian. Son téléphone sonne longtemps avant que l'appel soit coupé."
    "J'essaie Elen. Même résultat."
    "Le téléphone de Lysa apparaît juste en dessous de leurs noms. Je garde le doigt suspendu devant l'écran, puis le range sans appeler."

    iris inquiet "Tu pensais à Lysa ?"
    noam fatigue "Elle était là hier soir. Elle nous demandait juste de lui répondre et aujourd'hui Elias vient nous reprocher de l'avoir laissée dehors. Je sais pas ce qu'on doit en penser."
    iris reflexion "Je sais ce que j'ai entendu ce matin. S'il veut qu'on ouvre, c'est pas pour discuter. Et je veux pas qu'on laisse quelqu'un d'autre décider à notre place."

    "Nous fouillons rapidement la chambre pour inventorier ce que nous avons : deux bouteilles presque pleines, quelques biscuits, deux téléphones, ma tablette et les outils d'Iris."
    "Les biscuits viennent d'un paquet qu'elle garde habituellement pour les nuits où elle travaille tard. Nous nous partageons ce qui reste sans vraiment avoir faim."
    "Je tente une dernière fois d'appeler Kami. La connexion s'établit, mais aucune voix ne répond."

    noam colere "Kami ! Il y a des gens qui ont barricadé une porte de l'intérieur de ta station ! Tu vas vraiment nous laisser enfermés jusqu'au départ ?!"

    "L'écran de ma tablette reste figé sur l'icône de communication. Je coupe l'appel avant d'entendre ma propre voix se répéter une nouvelle fois dans le silence."
    "Iris prend la bouteille d'eau, boit une gorgée et me la tend."

    iris fatigue "Arrête de compter sur elle. Si elle avait envie de faire quelque chose, on le saurait déjà."
    noam fatigue "Je sais. C'est juste que j'arrive pas à comprendre pourquoi elle nous laisse faire n'importe quoi depuis des jours."
    iris reflexion "Moi non plus. Mais pour l'instant, j'aimerais surtout savoir si la barricade tient jusqu'au sol ou si on peut atteindre les boulons par en dessous."

    "Nous retournons près de la porte. Je déplace la commode juste assez pour passer le téléphone dans l'espace inférieur. L'appareil ne peut pas traverser : une plaque a également été installée derrière le seuil."
    "Les têtes de vis que je distingue sont toutes orientées vers le couloir. Quelqu'un a pris soin de ne nous laisser aucun accès aux fixations."

    "Iris s'appuie contre le mur et se laisse glisser jusqu'au sol."
    "Je n'essaie pas de lui annoncer que nous finirons par trouver une sortie. Pour le moment, je n'en vois aucune."

    $ hideGroup()
    jump _29_0_1_1_0_0_VOIX


label _29_0_1_1_0_0_VOIX:
    $ current_period = "Après-midi"
    call show_custom_title("Dans l'après-midi")
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "Au début, nous croyons que le couloir est redevenu désert. Puis quelqu'un frappe trois coups légers contre les planches."
    "Iris se redresse aussitôt et récupère le tournevis qu'elle avait posé près de sa chaussure."
    "Je lui fais signe de ne pas bouger."

    mara sourire "Hé, les voisins ! On vous a pas vus au déjeuner. Vous boudez encore ?"

    "La voix de Mara est si familière que j'ai presque le réflexe de lui répondre. Elle parle exactement comme elle le ferait depuis une table de la cafétéria."
    "Un objet frappe le métal à intervalles réguliers, comme une cuillère contre un verre."

    mara sourire "J'aurais bien demandé à Goumi de vous préparer un plateau, mais apparemment il a pas la notion du service en chambre. C'est con, hein ?"

    "Elle attend, puis pousse un soupir exagéré."

    mara neutre "Bon... Si vous changez d'avis, vous savez où nous trouver. Enfin, vous le saviez avant qu'Elias fasse son bricolage."

    "Un rire lui échappe, suivi d'un raclement prolongé contre la barricade. Je ne sais pas si elle est encore là lorsqu'une autre voix s'élève, plus près de la poignée."

    tomas raison "Noam, c'est Tomas. Je voudrais éviter qu'on passe toute la journée à se menacer à travers une porte."
    tomas raison "Personne ne vous demande de renoncer à vos inquiétudes. Simplement, nous devons trouver une solution avant le vote de demain."

    "Je m'approche presque malgré moi. C'est précisément la voix qu'aurait prise Tomas pendant un débat : calme, soucieuse de ne pas provoquer de conflit."

    tomas reflexion "Vous avez certainement remarqué que l'installation est solide. Je vous conseille de ne pas tenter de la démonter de votre côté, vous risqueriez de vous blesser."

    "La dernière phrase me glace plus que toutes les précédentes."
    "Je regarde Iris. Elle a entendu, elle aussi."

    tomas raison "Nous repasserons plus tard. Réfléchissez à ce que vous voulez faire, mais ne vous mettez pas en danger inutilement."

    "Ses pas s'éloignent. Iris souffle enfin, mais elle n'a pas relâché le tournevis."

    $ showGroup([
        ("iris", "inquiet", 0.36),
        ("noam", "inquiet", 0.64),
    ])

    iris inquiet "T'as entendu ? Il sait exactement comment ils l'ont fixée. Et il nous demande gentiment de pas essayer de sortir."
    noam reflexion "Il aurait pu vouloir nous aider. Mais pourquoi personne ne parle d'enlever ces planches ?"
    iris colere "Parce qu'ils veulent qu'on reste ici ! Je sais pas ce qui leur prend, mais c'est pas en leur demandant poliment qu'ils vont changer d'avis."

    "Je n'ai rien à lui répondre."
    "Un peu plus tard, les coups reprennent, plus légers. Quelqu'un tape d'abord contre la porte, puis contre le mur près du lit, comme s'il essayait de suivre nos déplacements."
    "Nous restons immobiles jusqu'à ce que le bruit s'arrête."

    "Quelques minutes passent. Un frottement remonte le long du bois, suivi d'une expiration rauque, beaucoup trop proche de la serrure."
    "Je n'arrive pas à savoir si quelqu'un respire réellement de l'autre côté ou s'amuse à imiter ce son."
    "Iris monte le volume de sa tablette, puis le coupe aussitôt. Elle ne supporte pas davantage d'entendre de la musique pendant que quelqu'un rôde devant sa porte."

    "Trois coups rapides retentissent. Puis deux plus lents."
    "Je me tourne vers Iris. C'est exactement le rythme qu'elle m'avait appris pour venir dormir chez elle."

    iris peur "C'est pas possible..."
    noam inquiet "Quelqu'un nous a entendus l'autre soir ?"
    iris reflexion "J'en sais rien. Mais t'ouvres pas. Même si tu crois reconnaître ma voix."

    "Les coups recommencent, dans le même ordre, puis se transforment en une série de frappes irrégulières."
    "Quelqu'un pouffe derrière la porte et s'éloigne."

    "Nous ne savons plus quoi faire de nos mains. Je reprends le tournevis, le repose, puis retourne vérifier le verrou alors que je l'ai déjà contrôlé plusieurs fois."
    "Iris m'attire contre elle sur le lit pour que nous restions à l'écart de l'entrée."

    $ hideGroup()
    jump _29_0_1_1_0_0_JULIAN


label _29_0_1_1_0_0_JULIAN:
    "Je commence à somnoler malgré moi lorsqu'un choc violent retentit dans le couloir."
    "Quelqu'un court. Je reconnais le bruit des semelles qui dérapent sur le sol lisse, puis une voix éclate tout près de nous."

    julian peur "NOAM ! OUVRE !"

    "Je bondis vers la porte. Iris me saisit par le bras avant que je l'atteigne."
    "Julian frappe des deux poings contre les planches. Il parle si vite que certains mots se perdent dans sa respiration."

    julian peur "Ils sont derrière moi ! Je peux pas... Merde, y a plus de passage ! Noam, je sais que t'es là, aide-moi !"

    "Un fracas métallique couvre la fin de sa phrase. Quelque chose heurte la barricade et la fait vibrer jusque dans le cadre de la porte."
    "Iris m'entraîne en arrière. Je me dégage juste assez pour regarder l'ouverture près de la poignée, mais je ne distingue qu'un morceau de tissu et une ombre qui passe trop vite."

    noam inquiet "Julian !"

    "Le prénom m'échappe avant que j'aie le temps de réfléchir. Iris me plaque immédiatement une main sur la bouche."
    "De l'autre côté, les pas s'arrêtent."

    julian peur "Noam ?! Putain, je t'ai entendu ! Enlève ça ! Je t'en supplie, je sais pas ce qu'ils veulent !"

    "Je tente de tirer la poignée. La porte bouge de quelques centimètres et bute aussitôt contre la barricade."
    "Iris me prend les deux poignets pour m'empêcher de recommencer. Elle secoue la tête avec une énergie désespérée."

    "Un autre bruit éclate dans le couloir. Julian lâche un cri si brutal que je recule avant même de comprendre ce qui se passe."
    "On entend quelque chose traîner sur le sol, puis une succession de pas précipités qui s'éloignent."

    julian peur "LÂCHEZ-MOI ! NON, ATTENDEZ !"

    "Sa voix s'éloigne au milieu d'un vacarme de métal et de frottements. Un dernier choc résonne à l'autre bout du couloir."
    "Puis plus rien."

    pause 1.0

    "Je reste debout devant la porte, le visage à quelques centimètres du bois."
    "Iris n'a pas lâché mon poignet."

    $ showGroup([
        ("iris", "peur", 0.37),
        ("noam", "desespoir", 0.64),
    ])

    noam desespoir "Il était là... Il nous a entendus. Pourquoi j'ai pas essayé plus tôt ? On aurait peut-être pu lui faire une ouverture, quelque chose..."
    iris peur "Avec quoi ? T'as vu ce qu'ils ont construit ! Même si on arrachait la porte, on pourrait pas passer à travers."
    noam colere "On aurait dû faire quelque chose !"
    iris colere "Je sais, Noam ! Je sais ! Mais j'aurais fait quoi ? Je serais sortie pour me faire attraper avec lui ?!"

    "Elle me lâche aussitôt, comme si elle regrettait d'avoir crié."
    "Je regarde ses mains. Elle tremble tellement qu'elle doit les coincer entre ses genoux pour les immobiliser."

    noam fatigue "Désolé. Je sais que t'as raison. Je supporte juste plus d'entendre quelqu'un nous demander de l'aide sans pouvoir bouger."
    iris inquiet "Moi non plus. Et si Julian est vraiment tombé sur eux, on sait même pas où ils l'ont emmené."

    "J'essaie de le rappeler. Le téléphone sonne longtemps. Cette fois, personne ne décroche."
    "J'ouvre ma conversation avec Elen et tape quelques mots pour lui demander si elle sait où est Julian. Le message part, mais reste sans réponse."
    "La dernière fois que nous l'avons vu, Julian essayait de réconforter Elen après la mort de Nyra. Il cherchait ses mots, les mains encore tachées de sang, sans réussir à lui arracher une réaction."
    "Je me demande s'il avait trouvé le courage de lui parler à nouveau ce matin."

    "Iris se rapproche et s'assoit près de moi. Elle ne dit rien pendant plusieurs minutes, puis finit par poser sa tête contre mon épaule."
    "Je n'ose pas lui promettre que Julian va revenir."

    $ hideGroup()
    jump _29_0_1_1_0_0_SOIR


label _29_0_1_1_0_0_SOIR:
    $ current_period = "Soir"
    call show_custom_title("En début de soirée")
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Les bruits ne s'arrêtent pas complètement. Parfois, quelqu'un passe dans le couloir et frappe deux ou trois coups avant de repartir ; parfois, plusieurs voix discutent assez près pour que nous reconnaissions leurs propriétaires sans comprendre ce qu'elles racontent."
    "Nous avons renoncé à approcher la porte. Les outils sont posés entre nous, sur le lit, et je garde ma tablette à portée de main malgré sa batterie presque vide."
    "Je regarde une nouvelle fois notre petite réserve d'eau. Iris a bu moins que moi depuis ce matin, mais refuse que je lui donne la moitié de ma bouteille."

    $ showGroup([
        ("iris", "fatigue", 0.35),
        ("noam", "fatigue", 0.65),
    ])

    iris fatigue "Arrête de regarder ça. On tiendra jusqu'à demain matin, et après on trouvera bien quelque chose."
    noam fatigue "Tu disais déjà ça hier. On savait pas encore qu'ils allaient nous construire un mur devant la porte."
    iris agace "Merci, Noam. J'avais presque réussi à l'oublier pendant trente secondes."

    "Elle sourit malgré elle, puis se tourne vers le mur quand un bruit de pas s'arrête devant notre chambre."
    "Une voix douce nous parvient de l'autre côté des planches."

    lysa inquiet "Noam ? Iris ? C'est encore moi."

    "Je sens Iris se raidir. Hier, Lysa semblait incapable de comprendre pourquoi nous ne lui répondions pas. Aujourd'hui, sa voix est presque paisible."

    lysa fatigue "Je voulais pas vous faire peur, hier. Je sais que vous m'avez entendue, mais ça fait rien. On peut recommencer, d'accord ?"

    "Elle attend assez longtemps pour que je commence à me demander si elle espère vraiment une réponse."

    lysa inquiet "Elen est avec nous. Julian aussi... Enfin, il va nous rejoindre. Vous devriez pas rester seuls pour le dernier vote."

    "Je tourne la tête vers Iris. Elle secoue lentement la sienne."
    "Lysa effleure la porte avec ses ongles. Le bruit est si léger que j'ai du mal à croire qu'il vient du même endroit que les coups du matin."

    lysa neutre "Bon. Je vais vous laisser réfléchir. Ce serait dommage qu'on se retrouve demain sans même avoir pu se parler."

    "J'entends ses pas s'éloigner, puis une voix plus grave que je ne parviens pas à identifier lui adresse quelques mots."
    "Quelqu'un rit très brièvement."

    noam inquiet "Elle a dit que Julian allait les rejoindre. Ils l'ont peut-être attrapé, mais il est peut-être encore vivant."
    iris fatigue "Ou alors elle dit ça parce qu'elle sait qu'on l'a entendu appeler. J'en sais rien. Je sais plus rien, Noam."

    "Elle ferme les yeux et passe les mains sur son visage. Quand elle les retire, je remarque qu'elle a les joues humides."
    "Je m'approche, mais elle détourne la tête pour essuyer rapidement ses larmes."

    iris peur "J'ai peur qu'ils finissent par entrer. J'ai peur de dormir, j'ai peur de bouger, et j'ai même peur de te demander ce qu'on va faire demain."
    noam inquiet "On peut rester réveillés à tour de rôle. Je peux prendre le début de la nuit, comme ça tu te reposeras un peu."
    iris fatigue "Tu tiens même plus debout. Fais pas semblant de pouvoir veiller sur tout le monde."

    "Elle me regarde un instant, puis tend la main vers moi. Je la prends sans chercher à lui répondre."
    "Nous restons assis ainsi jusqu'à ce que les lumières du Conclave commencent à diminuer."

    $ hideGroup()
    jump _29_0_1_1_0_0_ANNONCE


label _29_0_1_1_0_0_ANNONCE:
    $ current_period = "Nuit"
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Les voix ont fini par disparaître du couloir. Le silence me semble presque plus difficile à supporter maintenant que j'ai passé la journée à souhaiter qu'il revienne."
    "Iris s'est allongée sur son lit. Elle garde ses vêtements et le tournevis près de l'oreiller."
    "Je ferme les yeux quelques secondes lorsque le haut-parleur de la chambre s'allume dans un léger grésillement."

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Mes chers représentants ! J'espère que vous avez passé une excellente journée."

    "Iris se redresse immédiatement. Je fixe le petit haut-parleur près de la porte."

    kami "Un dernier rappel avant notre grande finale : demain, à huit heures précises, vous voterez sur le remplacement de la sanction d'élimination par un effacement de mémoire."
    kami "Il s'agira de votre tout dernier vote. Je compte donc sur chacun d'entre vous pour être à l'heure !"

    $ bc_show("noam", "colere")
    noam colere "Kami ! On est enfermés ! Il y a des planches et des plaques de métal devant notre porte ! Tu le sais forcément !"

    "Le haut-parleur reste silencieux pendant quelques secondes. J'attends presque une réponse, malgré tout ce qui s'est passé ces derniers jours."

    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Sur ce, bonne nuit à tous ! Reposez-vous bien. Vous en aurez besoin pour demain !"

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    "Le haut-parleur s'éteint."
    "Je regarde Iris, puis les meubles entassés devant la porte."

    $ showGroup([
        ("iris", "inquiet", 0.36),
        ("noam", "inquiet", 0.64),
    ])

    iris inquiet "Huit heures... Ils attendent vraiment qu'on se présente demain, alors qu'ils nous ont enfermés toute la journée."
    noam reflexion "S'ils ont passé autant de temps à construire cette barricade, c'est pas pour nous laisser sortir tranquillement au réveil."
    iris peur "Alors qu'est-ce qu'ils vont faire ?"

    "Je ne sais pas quoi lui répondre. Je regarde la ventilation condamnée, puis le cadre de la porte que nous avons cessé d'approcher."
    "Depuis ce matin, nous n'avons pas trouvé un seul moyen de sortir. Pourtant, quelqu'un pourrait ouvrir cette barricade de l'autre côté à n'importe quel moment."

    noam fatigue "Je crois qu'il faut qu'on garde nos affaires près de nous. Si quelqu'un essaie d'entrer demain, on aura peut-être quelques secondes pour réagir."
    iris reflexion "D'accord. Mais je veux pas que tu t'éloignes de moi, quoi qu'il arrive."
    noam raison "Je resterai avec toi."

    "Elle tend la main pour éteindre la lampe, puis s'arrête."
    "Un bruit de métal retentit dans le couloir. Un seul coup, comme si quelqu'un venait de tester la solidité des planches."
    "Nous restons immobiles jusqu'à ce que le silence revienne."
    "Iris éteint finalement la lumière."

    "Demain, il faudra quitter cette chambre. Je ne sais pas comment, ni ce qui nous attendra une fois la porte franchie."
    "Je me recouche auprès d'Iris et garde la main près des outils."

    $ hideGroup()
    stop music fadeout 1.5
    call end_day("30", sleeping=True) from _call_j29_stay_end_day_30
    jump _30_0_1_1_0_0_REVEIL
