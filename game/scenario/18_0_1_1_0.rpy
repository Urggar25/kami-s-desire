label _18_0_1_1_0_REVEIL_CHAMBRE:

    $ cafeteria_food_level = "null"
    $ current_day = 18
    $ current_period = "Nuit"
    $ noam_has_juliette_drawing = False

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background
    play music "music/bgm_cold_metadata.mp3" fadein 2.0
    $ danger_on()
    $ flashlight_on()

    $ showP("mara", "stress", 0.72)

    "Le bruit résonne encore quelque part dans le conduit."
    "Je reste figé, une main posée contre la paroi métallique, comme si le simple fait de bouger pouvait prévenir ce qui se trouve plus loin de ma présence."

    noam peur "..."

    "Je tends l'oreille. Pendant quelques secondes, il n'y a plus rien. Seulement ma respiration, beaucoup trop forte dans cet espace étroit, et le léger grincement de la tôle sous mon poids."

    mara "Noam ?"

    "Sa voix me parvient depuis ma chambre, étouffée par plusieurs mètres de conduit."

    mara stress "Réponds-moi, bordel."

    noam inquiet "Je suis là."

    mara "Tu bouges pas. Je vais chercher Elias."

    noam "D'accord."

    mara "Et cette fois, tu fais exactement ce que je te dis."

    noam "Je bouge pas."

    "J'entends ses pas s'éloigner dans ma chambre, puis la porte se refermer."
    $ hideGroup()
    "Le silence revient aussitôt."

    pause 1.0

    "Je regarde une dernière fois la treizième grille devant moi. Derrière, la pièce technique reste plongée dans l'obscurité. Rien ne bouge."
    "Ça devrait me rassurer. Ça ne marche pas."

    noam reflexion "Qu'est-ce que c'est que cet endroit... ?"

    "Je recule lentement jusqu'au croisement, puis je m'adosse comme je peux contre la paroi. Pour la première fois depuis que je suis entré ici, je regrette vraiment d'avoir démonté cette grille."

    "Les minutes passent beaucoup plus lentement que prévu. J'essaie de compter, puis j'abandonne rapidement. À force d'écouter chaque vibration, j'ai l'impression d'entendre du mouvement partout."

    noam hesitation "Mara... ?"

    "Aucune réponse."

    noam inquiet "Mara ?"

    "Toujours rien. Je regarde derrière moi, vers le chemin qui mène à ma chambre."

    think "Elle a peut-être juste mis du temps à le trouver."

    "Je vérifie une nouvelle fois la pièce derrière la grille. Rien n'a changé."

    pause 1.5

    $ showP("mara", "rire", 0.72)
    mara "Noam ?"

    "Je sursaute si fort que mon coude frappe la paroi."

    noam surpris "Putain !"

    mara rire "Eh bah, t'es vraiment à cran."
    $ danger_off()

    noam colere "Tu pouvais prévenir avant de gueuler dans le conduit !"

    mara "J'ai appelé deux fois. C'est toi qui répondais pas."

    "Sa lampe apparaît au loin, puis Mara rampe jusqu'à moi. Elle souffle en s'installant tant bien que mal dans le passage."

    $ showGroup([
        ("noam", "inquiet", 0.34),
        ("mara", "agace", 0.66),
    ])

    mara agace "J'ai fait le tour. Pas d'Elias."

    noam inquiet "Il est pas dans sa chambre ?"

    mara "Non. Pas à la maintenance non plus. J'ai même regardé à la cafétéria et dans la salle de repos. Rien."

    noam reflexion "C'est bizarre."

    mara taquin "Ou alors monsieur a simplement décidé qu'il avait mieux à faire que venir sauver deux abrutis coincés dans un mur."

    "Je laisse échapper un souffle qui ressemble presque à un rire, mais mon regard revient immédiatement vers la treizième ouverture."

    mara mefiant "C'est là ?"

    noam "Ouais."

    "Mara s'approche à son tour de la grille et éclaire la pièce."

    mara reflexion "..."

    noam "Tu vois quelque chose ?"

    mara "Des câbles. Des supports. Deux ou trois gros blocs au fond."

    noam "Et la trace au sol ?"

    mara "Ouais."

    "Elle bouge lentement sa lampe, puis soupire."

    mara agace "Bon. Ça nous avance pas beaucoup."

    noam "J'ai entendu quelque chose derrière moi."

    mara "Dans le conduit ?"

    noam "Oui. Et la trace dans la poussière était pas là quand je suis passé."

    "Mara tourne la tête vers le passage derrière nous."

    mara mefiant "T'es sûr ?"

    noam "Non."

    mara "Au moins t'es honnête."

    noam "Mais j'ai vraiment entendu quelque chose."

    mara stress "Alors on va éviter de rester plantés ici pendant trois heures."

    noam "Tu veux repartir ?"

    mara "Je veux surtout voir où on est avant de repartir. On a déjà fait la moitié du boulot."

    "Je la regarde, un peu surpris."

    noam "Il y a trente secondes tu voulais que je sorte de là."

    mara agace "Il y a trente secondes t'étais seul dans le noir à jouer au héros. Maintenant je suis là. Nuance."

    noam taquin "Ça change tout ?"

    mara rire "Évidemment. Je suis très rassurante comme présence."

    noam "C'est pas le premier mot qui me vient."

    mara "Continue et je te laisse ici."

    "Son ton est parfaitement normal. Ça suffit à faire retomber un peu la tension."

    "Je pointe la grille devant nous."

    noam "On regarde juste cette pièce. Après on revient chercher Elias quand il réapparaît."

    mara "Ça me va."

    jump _18_0_1_1_SALLE_ROBOTS


label _18_0_1_1_SALLE_ROBOTS:

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0

    $ showGroup([
        ("noam", "surpris", 0.34),
        ("mara", "taquin", 0.66),
    ])

    "La grille tient avec quatre vis identiques à celles de ma chambre. Cette fois, j'ai gardé le tournevis."

    mara taquin "Regarde-moi ça. Une nuit dans les murs et monsieur devient déjà professionnel du cambriolage."

    noam "Tu veux le faire ?"

    mara "Non, non. Je critique beaucoup mieux quand quelqu'un d'autre travaille."

    "Je retire la dernière vis et retiens la grille avant qu'elle ne tombe. L'ouverture est juste assez large pour passer."

    noam "Je passe en premier."

    mara "Quelle galanterie."

    "Je me glisse de l'autre côté et descends prudemment. Mes pieds rencontrent enfin un sol stable."

    "La pièce est plus grande que je le pensais. Très basse par endroits, encombrée de câbles et de structures métalliques, elle ressemble moins à une salle normale qu'à un espace qu'on aurait construit entre deux autres zones du Conclave."

    noam surpris "Mara..."

    mara "Quoi ?"

    noam "Viens voir."

    "Elle passe à son tour, jure en accrochant sa manche, puis se redresse à côté de moi."

    $ unlock_gallery_image("bg_cg046")
    $ hideGroup()
    scene bg_cg046 at adaptive_fullscreen with flash_white

    $ investigation_add("salle_goumi")
    tuto "Inspecte librement la salle. Les éléments majeurs sont nécessaires ; les détails d'ambiance restent optionnels."
    call investigation_room_run from _call_investigation_room_j18
    $ investigation_add("mara_exploration", notify=False)

    mara surpris "Ah ouais."

    "Nos lampes balayent lentement la pièce. Plusieurs établis occupent un mur entier. Il y a des boîtes de pièces, des bras articulés, des coques démontées et deux stations verticales installées au fond."

    "Je m'arrête devant l'un des établis. Deux grosses batteries sont posées sous une série de composants électroniques encore emballés."

    noam reflexion "Attends."

    mara "Quoi ?"

    "Je prends ma lampe et éclaire les batteries de plus près. Le boîtier, les connecteurs, même les bandes orange sur le côté me rappellent immédiatement quelque chose."

    noam inquiet "Attends... Elias cherchait exactement ces batteries quand le matos a disparu de la réserve."

    mara mefiant "T'es sûr ?"

    noam "Oui. Les grosses batteries. Et certains de ces composants aussi."

    "Je fouille du regard les étagères. Il y en a quelques-uns, mais clairement pas tout ce qui avait disparu."

    mara reflexion "Donc quelqu'un a amené une partie du matos volé ici."

    noam inquiet "On dirait."

    "Je repose la lampe sur les deux stations du fond."

    "Sur chacune d'elles repose une silhouette ronde que je reconnais immédiatement."

    noam surpris "Des Goumi."

    mara "Deux."

    "L'un est presque entièrement monté. L'autre est ouvert sur le côté, avec une partie de sa coque déposée sur l'établi."

    mara reflexion "Donc c'est ici qu'ils réparent ces machins."

    noam reflexion "Ou qu'ils les remplacent."

    "Je m'approche sans toucher. À cette distance, le robot paraît beaucoup moins sympathique que ceux qui se promènent habituellement dans le Conclave. Sans ses mouvements et sa voix, ce n'est plus qu'une machine compacte remplie de câbles et de pièces mécaniques."

    mara taquin "Tu vas pas me dire que t'étais attaché émotionnellement à Goumi ?"

    noam "Pas vraiment."

    mara "T'as l'air déçu."

    noam "Je savais que c'était un robot."

    mara "Ouais, mais entre le savoir et voir ses tripes sur une table..."

    "Elle se penche légèrement vers l'unité démontée, puis recule."

    mara "C'est glauque."

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "surpris", 0.34),
        ("mara", "mefiant", 0.66),
    ])

    noam "Un peu."

    "Je regarde autour de nous. Aucun écran n'est allumé. Aucune lumière ne clignote. Tout semble parfaitement inerte."

    noam reflexion "Donc ils doivent réparer les robots ici... sans les faire passer dans les couloirs."

    mara mefiant "Donc ils prennent les conduits."

    noam "Peut-être."

    mara "Ça expliquerait la taille."

    "Je regarde l'ouverture par laquelle nous sommes arrivés."

    noam "Et le réseau qui passe derrière les chambres."

    mara "Ça, par contre, j'aime toujours pas."

    "Je m'approche d'un autre conduit qui quitte la pièce sur le côté. Il est plus large que celui des dortoirs et descend légèrement avant de se diviser en plusieurs branches."

    noam reflexion "Ça continue."

    mara "Évidemment que ça continue. Pourquoi quelque chose serait simple ici ?"

    noam "On avait dit qu'on regardait juste la pièce."

    mara rire "Et techniquement, on regarde toujours la pièce. Juste... la sortie de la pièce."

    noam taquin "Belle mauvaise foi."

    mara "Merci. J'y travaille depuis des années."

    "Je souris malgré moi. Puis je m'accroupis près de l'ouverture."

    "Un léger courant d'air vient de l'intérieur. Plus loin, je distingue une lumière régulière qui passe à travers une autre grille."

    noam "Si ça rejoint vraiment le reste du Conclave, on peut peut-être comprendre le plan sans ramper trois kilomètres."

    mara "Voilà. Dix minutes. Et après on retourne se coucher comme des gens sains d'esprit."

    noam "Dix minutes."

    "Je passe à nouveau dans le conduit. Mara me suit sans discuter."

    jump _18_0_1_1_RESEAU_CONCLAVE


label _18_0_1_1_RESEAU_CONCLAVE:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0
    $ flashlight_on()

    $ showGroup([
        ("noam", "reflexion", 0.34),
        ("mara", "mefiant", 0.66),
    ])

    "Cette partie du réseau est beaucoup plus confortable. Je peux avancer à quatre pattes sans me cogner constamment les épaules contre les parois."

    "Après quelques mètres, le conduit se sépare. Une branche remonte vers les dortoirs. Une autre continue droit devant."

    mara "On est où, là ?"

    noam reflexion "Si ma chambre est derrière nous... probablement entre les dortoirs et la cafétéria."

    mara "Probablement, c'est rassurant."

    noam "Tu veux faire demi-tour ?"

    mara "Pas encore."

    "Nous continuons. Une première grille apparaît sur notre droite. Je coupe ma lampe et m'approche doucement."

    "De l'autre côté, des chaises sont empilées près d'une table basse. Même dans la pénombre, je reconnais immédiatement la salle de repos."

    noam inquiet "La salle de repos."

    mara "Sérieux ?"

    "Elle se penche par-dessus mon épaule pour regarder."

    mara reflexion "Donc ça passe vraiment partout."

    "Nous repartons. Plus loin, une nouvelle bifurcation descend légèrement. À travers une autre grille, j'aperçois des rangées d'étagères."

    noam "Le stockage."

    mara "Et là-bas ?"

    "Elle montre une branche plus étroite."

    noam "Aucune idée."

    mara rire "Très utile, monsieur le guide."

    "Nous avançons encore. À chaque nouvelle ouverture, le même malaise revient. Le réseau ne relie pas quelques zones techniques. Il double presque entièrement les couloirs auxquels nous avons accès."

    "On pourrait traverser une bonne partie du Conclave sans apparaître une seule fois dans les espaces communs."

    noam panne "..."

    mara mefiant "T'y penses aussi ?"

    noam "À quoi ?"

    mara "Au fait qu'on dort juste derrière ces grilles depuis plus de deux semaines."

    noam inquiet "Ouais." id j18_reseau_noam_ouais

    mara "Super. Je vais adorer retrouver mon lit."

    noam "Je pense que je vais remettre ma grille correctement."

    mara taquin "Moi je vais mettre une armoire devant."

    noam "Pratique pour l'aération."

    mara "Je préfère mourir étouffée que me réveiller avec Ryn qui sort du mur."

    "Je ris malgré moi."

    noam "Pourquoi Ryn ?"

    mara "Parce qu'il a la tête parfaite pour sortir d'une bouche d'aération à trois heures du matin."

    noam "Je lui dirai."

    mara colere "Tu fais ça et je te pousse dans le prochain trou."

    "Nous continuons encore un peu. Le conduit tourne sur la gauche, puis descend suffisamment pour que je doive prendre appui avec les mains."

    "Au loin, j'entends un bourdonnement régulier."

    noam reflexion "On doit être près d'une autre salle."

    mara "Tu reconnais le bruit ?"

    noam "Non."

    "Une grille apparaît plus bas, encore trop loin pour voir ce qu'il y a derrière."

    "Je commence à descendre."

    mara "Attends."

    "Je m'arrête." id j18_reseau_arret

    noam "Quoi ?"

    "Mara éclaire au-dessus de nous. Un conduit secondaire part presque verticalement sur quelques mètres avant de tourner."

    mara reflexion "T'avais vu ça ?"

    noam "Non."

    mara "Ça monte vers quelque chose."

    noam "Et le passage en bas aussi."

    mara "Ouais, mais en bas on voit déjà une grille. Ça va juste donner dans une autre pièce."

    noam "C'est un peu le principe de ce qu'on est en train de chercher."

    mara rire "T'es chiant quand tu veux."

    "Elle pointe le conduit supérieur avec sa lampe."

    mara "Là, on sait même pas où ça mène. Si on veut comprendre le réseau, c'est plus intéressant."

    "Je regarde à nouveau vers le bas. La lumière derrière la grille est blanche, beaucoup plus forte que celle des autres salles, mais d'ici je ne distingue absolument rien."

    noam reflexion "..." id j18_reseau_silence_noam

    mara "On regarde cinq minutes et après on redescend si tu veux."

    noam "D'accord."

    "Je me détourne de la grille et commence à grimper dans la branche qu'elle m'a montrée."

    "Quelques secondes plus tard, la lumière blanche disparaît derrière nous."

    jump _18_0_1_1_ZONE_ETROITE


label _18_0_1_1_ZONE_ETROITE:

    scene bg_cavite_technique at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "desaccord", 0.34),
        ("mara", "taquin", 0.66),
    ])

    "Le nouveau passage se resserre rapidement. Je dois avancer presque à plat ventre, les bras tendus devant moi pour pousser la lampe."

    noam desaccord "Tu pouvais pas choisir le conduit le plus large ?"

    mara "C'est toi qui es passé devant."

    noam "Parce que tu m'as montré celui-là."

    mara rire "Et t'as obéi. C'est mignon."

    noam "Je te déteste."

    mara taquin "Je sais. Ça te donne du charme."

    "Je secoue la tête et continue."

    "Au bout de quelques mètres, le passage débouche enfin dans une petite cavité technique. Ce n'est pas vraiment une pièce, plutôt un espace laissé entre deux parois, assez haut pour s'asseoir mais pas pour se tenir debout."

    "Une trappe métallique est fixée au fond."

    noam reflexion "On a trouvé quelque chose."

    mara "Je savais que j'avais raison."

    noam "Tu savais rien du tout."

    mara "Laisse-moi savourer."

    "Je m'approche de la trappe. Elle n'a pas de poignée de notre côté, seulement deux petites attaches métalliques."

    noam "Ça doit s'ouvrir de l'autre côté."

    mara "Ou avec ça."

    "Elle me tend le tournevis."

    noam "Tu veux vraiment qu'on démonte encore un truc ?"

    mara "On a commencé une carrière, autant aller jusqu'au bout."

    "Je soupire et glisse la lame contre la première attache. Elle résiste."

    mara "Force un peu."

    noam "J'essaie."

    mara "Pas comme ça. Mets-le plus bas."

    noam "Tu veux prendre ma place ?"

    mara "J'aimerais bien, mais j'ai malheureusement une morphologie beaucoup trop avantageuse pour cet espace."

    noam taquin "Évidemment."

    mara rire "Tu vois, tu commences à comprendre."

    "Je pousse un peu plus fort. L'attache bouge de quelques millimètres, puis revient en place."

    noam desaccord "Ça bougera pas."

    mara "Attends. Passe-moi la lampe."

    "Je lui tends. Pendant qu'elle éclaire le mécanisme, je me penche davantage."

    "Un bruit sourd résonne derrière la trappe."

    noam inquiet "T'as entendu ?"

    mara "Ouais."

    "Nous restons silencieux."

    "Le bruit ne revient pas."

    noam "C'était de l'autre côté."

    mara mefiant "Ou dans le mur."

    noam "Ça change pas grand-chose."

    mara "On peut essayer l'autre attache."

    "Je regarde la trappe, puis le passage derrière nous."

    "Depuis quelques minutes, l'air me paraît plus lourd. Ça n'a probablement rien de réel, mais l'espace étroit commence à me donner l'impression que les parois se rapprochent lentement."

    noam hesitation "Non."

    mara "Non quoi ?"

    noam "On arrête."

    mara "Maintenant ?"

    noam "Ouais."

    mara agace "On est littéralement à deux vis de voir ce qu'il y a derrière."

    noam "Et on sait pas ce qu'il y a derrière."

    mara "C'était un peu le but."

    noam inquiet "Je sais. Mais j'ai pas envie de rester ici."

    "Elle me regarde sans répondre immédiatement."

    mara neutre "T'es pas bien ?"

    noam "J'en sais rien. J'ai juste..."

    "Je cherche mes mots."

    noam hesitation "J'aime pas ça. J'aime vraiment pas ça."

    mara taquin "Ça, c'est un diagnostic particulièrement précis."

    noam colere "Mara."

    "Mon ton sort plus sec que prévu. Elle lève immédiatement une main."

    mara "D'accord. On sort."

    "Je récupère le tournevis et commence à reculer vers l'ouverture."

    mara "Attends deux secondes, au moins laisse-moi regarder si—"

    noam determine "Non, Mara. J'ai dit qu'on sort."

    "Un silence passe."

    mara neutre "Très bien."

    "Elle ne discute plus."

    "Je me retourne comme je peux et commence à ramper vers le conduit principal. Après quelques mètres, mon épaule accroche une plaque métallique et quelque chose claque derrière moi."

    noam surpris "Merde !"

    "Je tire sur mon bras. La manche de ma veste est coincée dans une petite pièce saillante."

    mara "Bouge pas."

    noam inquiet "Je suis coincé."

    mara "J'ai vu. Bouge pas ou tu vas déchirer tout le bordel."

    "Elle se rapproche et libère ma manche avec le tournevis."

    mara taquin "Voilà. Sauvé une deuxième fois. Je commence à pouvoir facturer."

    noam reflexion "Tu m'avais déjà sorti ça à la cafétéria."

    mara "Quoi ?"

    noam "La facture. Quand tu m'avais laissé m'asseoir avec vous."

    "Mara me regarde une seconde de trop."

    mara taquin "Ah. Ouais. Peut-être."

    noam hesitation "Peut-être ?"

    mara agace "Tu tiens vraiment un registre de toutes mes blagues ?"

    noam "Merci quand même."

    mara "De rien. Maintenant avance avant que tu changes encore d'avis."

    "Je reprends ma progression."

    "Quelques secondes plus tard, un bruit métallique retentit derrière nous. Plus net cette fois."

    "Je m'arrête."

    mara stress "Continue."

    noam "Mais—"

    mara "T'as voulu sortir. Alors on sort."

    "Elle n'a pas tort."

    "Je continue sans regarder derrière moi."

    jump _18_0_1_1_RETOUR_RESEAU


label _18_0_1_1_RETOUR_RESEAU:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve

    $ showGroup([
        ("noam", "fatigue", 0.34),
        ("mara", "taquin", 0.66),
    ])

    "Le conduit principal me paraît immense quand nous le retrouvons enfin. Je m'assois quelques secondes contre la paroi et prends une longue inspiration."

    mara "Ça va mieux ?"

    noam "Ouais."

    mara "T'es devenu blanc d'un coup."

    noam "J'avais l'impression d'étouffer."

    mara taquin "Tu vois ? Ma poitrine n'était donc pas le principal problème d'espace."

    noam desaccord "T'es obligée ?"

    mara rire "Absolument."

    "Je souris malgré moi et essuie mon front avec ma manche."

    noam reflexion "On devrait vraiment revenir avec Elias."

    mara "Ouais. Avec du matériel, surtout. Et une corde. Et peut-être quelqu'un qui sait où il met les pieds."

    noam "Merci pour nous."

    mara "Je parle surtout de toi. Moi j'étais excellente."

    "Nous reprenons le chemin des dortoirs."

    "En passant devant les différentes grilles, je ne cherche même plus à identifier les salles. Maintenant que je sais qu'elles sont là, chaque ouverture me paraît plus intrusive que la précédente."

    "Quelqu'un pourrait rester ici, écouter une conversation, attendre qu'une pièce se vide, puis continuer son chemin sans jamais croiser personne dans les couloirs."

    think "Et personne ne nous a jamais parlé de ce réseau."

    "Je ralentis devant une bifurcation."

    mara "Quoi encore ?"

    noam "Rien." id j18_retour_noam_rien

    mara "T'as cette tête-là quand c'est pas rien."

    noam "Je réfléchis juste."

    mara taquin "Ah. Grave erreur."

    "Je reprends sans répondre."

    "Quelques minutes plus tard, nous retrouvons enfin le passage derrière les dortoirs, puis la grille ouverte de ma chambre."

    jump _18_0_1_1_SORTIE_CHAMBRE


label _18_0_1_1_SORTIE_CHAMBRE:

    $ flashlight_off()
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    "Je descends maladroitement sur mon bureau et manque de faire tomber la lampe. Quand mes pieds touchent enfin le sol de ma chambre, j'ai presque envie de m'allonger directement par terre."

    "Mara sort à son tour, beaucoup moins élégamment qu'elle ne l'aurait probablement souhaité."

    mara colere "Putain de grille."

    noam sourire "Très gracieux."

    mara "Ferme-la."

    "Elle remet ses cheveux en place et regarde l'ouverture derrière nous."

    mara reflexion "Donc... résumé."

    noam "Il y a un réseau technique derrière les murs qui relie au moins les chambres, la salle de repos, le stockage et probablement beaucoup d'autres salles."

    mara "Avec une pièce pleine de Goumi au milieu."

    noam "Et d'autres passages qu'on n'a pas explorés."

    mara "Et un petit trou de merde dans lequel monsieur a décidé de faire une crise de claustrophobie."

    noam desaccord "J'ai pas fait une crise."

    mara taquin "T'étais blanc comme le mur."

    noam "J'étais fatigué."

    mara "Bien sûr."

    "Je récupère la grille et la pose devant l'ouverture sans la revisser."

    noam reflexion "On doit en parler à Elias."

    mara "Oui."

    noam "Et aux autres ?"

    "Mara hausse une épaule."

    mara "À toi de voir."

    noam "Pourquoi à moi ?"

    mara "Parce que si tu vas dire maintenant à Ryn qu'on peut ramper derrière sa chambre, il va passer les quatre prochains jours avec un meuble devant sa ventilation et une crise de nerfs dès que quelqu'un tousse dans le couloir."

    noam "C'est pas complètement faux."

    mara "Et vu l'ambiance depuis hier, j'suis pas sûre que rajouter 'au fait, y'a des passages secrets derrière vos lits' soit notre meilleure idée du siècle."

    noam reflexion "On vérifie d'abord avec Elias."

    mara "Voilà. Pour une fois que tu dis un truc intelligent."

    noam taquin "Tu sais être rassurante."

    mara rire "Je sais. C'est mon charme naturel."

    "Elle se dirige vers la porte, puis s'arrête."

    mara "Je vais essayer de le trouver encore une fois."

    noam "Je viens avec toi."

    mara "Non."

    noam "Pourquoi ?"

    mara "Parce qu'il est bientôt midi, que t'as passé la nuit à ramper dans des conduits et que t'as une tête à faire peur à Iris. Bois un truc, lave-toi et respire cinq minutes."

    noam "Je vais bien."

    mara agace "Ouais, et moi je suis raffinée. Assieds-toi."

    "Je la regarde quelques secondes, puis abandonne."

    noam "D'accord."

    mara taquin "Bon garçon."

    "Elle ouvre la porte."

    noam "Mara."

    "Elle se retourne."

    noam "Merci d'être revenue."

    mara content "Ouais, bon. Commence pas à devenir sentimental, ça va me mettre mal à l'aise."

    "Elle disparaît dans le couloir."

    "Je reste seul avec la grille démontée."

    noam inquiet "..."

    "Même ouverte, la bouche d'aération semble soudain beaucoup plus sombre qu'avant."

    $ current_period = "Matin"

    jump _18_0_1_1_CAFETERIA_MIDI


label _18_0_1_1_CAFETERIA_MIDI:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_130
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Une douche et vingt minutes assis sur mon lit suffisent à me faire sentir presque humain. Presque."

    "En sortant de ma chambre, je jette malgré moi un regard vers le mur derrière lequel passe le conduit. Rien ne le distingue des autres."

    "C'est probablement ça qui me dérange le plus."

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_131
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "La cafétéria est moins bruyante que d'habitude. Une bonne partie du groupe est présente, mais les conversations restent basses. La décision d'hier plane encore au-dessus de tout le monde."

    $ showGroup([
        ("nyra", "neutre", 0.10),
        ("tomas", "reflechit", 0.25),
        ("lysa", "blase", 0.40),
        ("iris", "fatigue", 0.55),
        ("elen", "neutre", 0.70),
        ("ryn", "fatigue", 0.85),
    ])

    elen "Noam ! T'étais où ? On t'a pas vu ce matin."

    noam hesitation "J'ai mal dormi."

    iris fatigue "Waouh, ça se voit pas du tout."

    lysa blase "Laisse-le. Il teste une nouvelle technique : avoir l'air plus mort chaque jour."

    noam taquin "Ça marche ?"

    lysa "Très bien. Encore deux jours et on te met dans le stockage."

    "Je m'assois avec eux et prends quelque chose à manger."

    "Pendant quelques minutes, personne ne parle de M16, des votes ou de Kami. Ça ressemble presque à un déjeuner normal."

    "Presque."

    tomas reflechit "J'ai recalculé le temps qu'il nous reste."

    iris agace "Et voilà. C'était trop beau."

    tomas "Désolé."

    nyra "Vas-y."

    tomas "Si on maintient le refus de participer jusqu'au jour vingt-et-un, on perd définitivement le prochain vote et probablement toute possibilité d'en organiser un autre avant le départ."

    ryn colere "On le sait."

    tomas "Je sais. Je dis juste que maintenant... chaque journée qu'on perd, on la récupérera pas."

    nyra reflexion "Et si on reprend maintenant sans réponse, on lui apprend juste qu'elle a qu'à attendre qu'on cède."

    iris "Donc on a le choix entre perdre du temps et perdre du temps autrement. Fantastique."

    elen inquiet "On peut peut-être encore la faire changer d'avis."

    lysa blase "Avec quoi ? Ta pancarte ?"

    elen "Elle était bien, ma pancarte."

    iris "Elle était écrite sur un carton de livraison."

    elen "Ça lui donnait un côté authentique."

    "Ryn laisse échapper un rire bref malgré lui."

    ryn taquin "Je la trouvais pas mal."

    nyra "Le problème n'est pas le slogan."

    elen "Je sais."

    "Son sourire retombe un peu."

    elen inquiet "Je veux juste pas qu'on commence à se retourner les uns contre les autres encore une fois."

    nyra "Alors on ne le fera pas."

    tomas "Ça risque quand même d'arriver si on n'est pas tous d'accord sur la durée du boycott."

    ryn colere "Tu veux déjà reprendre ?"

    tomas desaccord "J'ai pas dit ça."

    ryn "T'en parles beaucoup pour quelqu'un qui veut pas le faire."

    tomas "Parce que quelqu'un doit parler des conséquences avant qu'on arrive au jour vingt et un en faisant semblant de les découvrir."

    nyra "Il a raison sur ce point."

    "Ryn se renfonce dans sa chaise, visiblement peu convaincu."

    lysa blase "C'est quand même magnifique. On a organisé notre première grève hier et vingt-quatre heures plus tard on débat déjà de quand l'arrêter."

    iris "Bienvenue dans la révolution."

    elen "On pourrait faire un planning."

    "Tout le monde se tourne vers elle."

    elen surpris "Quoi ?"

    iris "Rien. Continue de ne surtout pas comprendre pourquoi c'est drôle."

    "Quelques rires étouffés parcourent la table. La tension retombe juste assez pour qu'on recommence à manger."

    "Je profite du moment pour regarder autour de moi."

    "Au-dessus d'une porte, une grille d'aération se fond presque complètement dans le mur."

    noam panne "..."

    lysa "Elle t'a fait quoi ?"

    noam surpris "Quoi ?" id j18_cafeteria_noam_quoi

    lysa "La ventilation."

    "Elle pointe vaguement du menton dans la même direction."

    lysa taquin "Ça fait trente secondes que tu la regardes comme si elle venait d'insulter ta mère."

    noam hesitation "Rien. Je suis juste fatigué."

    iris fatigue "Tu devrais vraiment dormir cet après-midi."

    noam "Ouais."

    "Je baisse les yeux vers mon assiette."

    think "Pas maintenant."

    "Je veux d'abord parler à Elias."

    $ hideGroup()

    jump _18_0_1_1_CHERCHE_ELIAS


label _18_0_1_1_CHERCHE_ELIAS:

    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    "Après le repas, je quitte la cafétéria avec une seule idée en tête : retrouver Elias."

    "Je commence par la salle de maintenance."

    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_j18_maintenance_door
    scene bg_maintenance at adaptive_fullscreen with dissolve

    "Il n'y a personne."

    noam desaccord "Évidemment."

    "Je vérifie rapidement les établis et les quelques outils laissés en place, sans toucher à rien. Rien n'indique où il est parti."

    "Je ressors."

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je passe ensuite par les dortoirs. Au moment où j'arrive près de sa chambre, la porte s'ouvre."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("elias", "fatigue", 0.70),
    ])

    elias fatigue "Ah."

    noam surpris "Elias."

    elias "Quoi ?"

    noam "Je te cherchais."

    elias "Pourquoi ?"

    "Je regarde instinctivement autour de nous."

    noam hesitation "Pas ici."

    elias inquiet "Ça commence bien."

    noam "J'ai trouvé quelque chose cette nuit."

    elias "Quel genre de quelque chose ?"

    noam "Un passage derrière ma chambre."

    "Il me fixe quelques secondes."

    elias "Un passage ?"

    noam "Un réseau de maintenance. Enfin... un vrai passage. On peut ramper dedans."

    elias inquiet "T'es entré ?"

    noam "Oui."

    elias colere "Putain, Noam..."

    noam "Mara était avec moi."

    elias "C'est censé améliorer l'idée ?"

    noam "Pas vraiment."

    "Il passe une main sur son visage."

    elias fatigue "Montre-moi."

    noam "Maintenant ?"

    elias "Tu voulais me trouver, non ?"

    noam "Oui."

    elias "Alors montre."

    "Son ton ne laisse pas vraiment de place au débat."

    "Nous prenons la direction de ma chambre."

    jump _18_0_1_1_ELIAS_GRILLE


label _18_0_1_1_ELIAS_GRILLE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("elias", "neutre", 0.70),
    ])

    "Elias s'accroupit devant la grille simplement posée contre le mur. Il l'écarte, éclaire l'intérieur avec sa tablette et reste silencieux un moment."

    elias neutre "..."

    noam "Alors ?"

    elias "C'est pas juste une gaine d'air."

    noam "On avait remarqué."

    elias colere "Merci."

    "Il passe une main sur le bord métallique."

    elias "Y'a des renforts. Des passages de câbles. Le fond est fait pour supporter du poids."

    noam "Des robots ?"

    elias "Possible."

    noam "On a trouvé une salle avec deux Goumi derrière les dortoirs."

    "Il relève immédiatement la tête."

    elias inquiet "Deux Goumi ?"

    noam "Un entier, un démonté. Des établis, des pièces."

    elias "Et vous avez touché à quoi ?"

    noam "À rien."

    elias "Bien."

    noam "Tu connaissais cet endroit ?"

    elias "Non."

    "Il répond sans hésitation."

    elias "La maintenance où je bosse, c'est les portes, les outils, les petits trucs. Pas ces machins-là."

    noam reflexion "Donc y'a bien des zones qu'on nous a jamais montrées."

    elias "Ça, on le savait déjà un peu."

    noam "Pas à ce point-là."

    "Il éclaire encore l'intérieur, puis se redresse."

    elias "Je vais pas rentrer maintenant."

    noam surpris "Pourquoi ?"

    elias "Parce que vous avez déjà foutu vos mains partout sans savoir si le sol tient, si y'a de l'électricité, des pièces mobiles ou je sais pas quoi."

    noam "On a fait attention."

    elias "C'est ce que disent les gens juste avant de casser un truc."

    noam taquin "Ça t'arrive jamais ?"

    "Il me regarde."

    elias colere "Très drôle."

    noam sourire "Un peu."

    "Il soupire."

    elias "Je vais préparer deux lampes correctes, une corde et de quoi bloquer les grilles. On y retourne demain si on doit y retourner."

    noam "Pourquoi demain ?"

    elias "Parce que t'as l'air crevé et que moi aussi."

    noam "Mara disait exactement la même chose."

    elias "Pour une fois qu'elle dit pas une connerie."

    "Je m'assois au bord du lit."

    noam reflexion "Tu crois qu'on doit prévenir les autres ?"

    elias "Pas tant qu'on sait pas ce que c'est."

    noam "C'est aussi ce qu'on s'est dit."

    elias "Alors pour une fois, vous avez eu une bonne idée."

    "Il remet la grille devant l'ouverture et revisse seulement deux attaches."

    noam "Pourquoi pas les quatre ?"

    elias "Parce que si on doit la rouvrir demain, j'ai pas envie de perdre dix minutes."

    noam "Et si quelque chose veut entrer cette nuit ?"

    "Il s'arrête."

    elias inquiet "Quelque chose ?"

    noam hesitation "J'ai entendu du bruit dans le conduit."

    elias "Quand ?"

    noam "Cette nuit. Plusieurs fois."

    "Il regarde la grille, puis moi."

    elias "Mets le bureau devant."

    noam "Tu crois vraiment que—"

    elias "J'en sais rien. Mais ça coûte rien."

    "Il se lève."

    elias "Et si t'entends encore quelque chose, tu viens me chercher. Tu rentres pas dedans tout seul."

    noam "Promis."

    elias "Promis pour de vrai."

    noam taquin "Oui, papa."

    elias colere "Va te faire foutre."

    "Il sort sans attendre ma réponse."

    $ hideGroup()

    jump _18_0_1_1_APRES_MIDI_CALME


label _18_0_1_1_APRES_MIDI_CALME:

    $ current_period = "Après-midi"

    scene bg_observation at adaptive_fullscreen, living_background with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Je passe une partie de l'après-midi dans la salle d'observation. Pas vraiment pour regarder la planète, plutôt parce qu'il n'y a aucune grille d'aération directement derrière ma tête."

    "C'est ridicule. Je le sais. Ça ne m'empêche pas de choisir ma place en fonction."

    $ showGroup([
        ("noam", "neutre", 0.25),
        ("lysa", "blase", 0.75),
    ])

    lysa "Tu sais que tu fais peur à voir ?"

    noam "On me l'a déjà dit aujourd'hui."

    lysa "Ah. Donc je suis pas originale. Décevant."

    "Elle s'assoit sur le fauteuil voisin sans me demander mon avis."

    lysa "Tu fuis quelqu'un ?"

    noam "Non."

    lysa "Quelque chose ?"

    "Je tourne la tête vers elle."

    noam "Pourquoi tu demandes ça ?"

    lysa taquin "Parce que t'as choisi le seul siège de cette salle qui n'est pas collé à un mur."

    "Je regarde mon fauteuil."

    noam panne "..."

    lysa "Bravo Sherlock."

    noam sourire "J'avais pas remarqué."

    lysa "Bien sûr."

    "Elle regarde la planète derrière la vitre."

    lysa blase "Tout le monde devient bizarre ici. J'imagine que c'est contagieux."

    noam reflexion "Tu regrettes le boycott ?"

    lysa "Non."

    "Elle répond immédiatement."

    lysa "Je regrette juste qu'on ait aucun plan derrière."

    noam "Nyra pense qu'on peut encore mettre la pression."

    lysa "Nyra pense toujours qu'un problème finit par céder si tu le regardes assez froidement."

    noam "Et toi ?"

    lysa "Moi je pense que Kami peut attendre quatre jours sans dormir, sans manger et sans commencer à paniquer."

    "Elle soupire."

    lysa "Nous, beaucoup moins."

    noam "Tu veux reprendre les votes ?"

    lysa "J'en sais rien."

    "Elle tourne enfin la tête vers moi."

    lysa triste "Et c'est ça qui m'emmerde."

    "Je reste silencieux."

    lysa "On voulait une réponse. Maintenant on a juste une date de départ."

    noam reflexion "On a encore trois jours."

    lysa blase "Ouais. Garde espoir. C'est gratuit."

    "Un petit sourire apparaît au coin de ses lèvres."

    lysa taquin "Enfin, jusqu'au moment où ça te tue."

    noam sourire "Toujours aussi rassurante."

    lysa "Je fais de mon mieux."

    "Nous restons encore quelques minutes devant la vitre sans parler."

    "Pour la première fois depuis ce matin, je réussis presque à oublier les conduits."

    $ hideGroup()
    call START_FREE_TIME("_18_0_1_1_SOIR_CHAMBRE") from _call_START_FREE_TIME_J18


label _18_0_1_1_SOIR_CHAMBRE:

    $ current_period = "Soir"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    "Quand je retourne vers ma chambre, le couloir des dortoirs est presque vide."

    "Je ralentis devant chaque porte sans vraiment le vouloir. Derrière le mur, je sais maintenant qu'un autre passage suit exactement le même trajet."

    "Deux couloirs parallèles. L'un éclairé, visible, surveillé. L'autre plongé dans le noir."

    noam inquiet "..."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_j18_chambre_door
    scene bg_chambre at adaptive_fullscreen, living_background with dissolve

    "La première chose que je regarde en entrant, c'est la grille."

    "Toujours en place."

    "Je ferme la porte, puis pousse mon bureau de quelques centimètres devant l'ouverture. Pas complètement. Juste assez pour qu'il fasse du bruit si quelqu'un essaie de la déplacer."

    noam desaccord "C'est ridicule."

    "Je le laisse quand même."

    "Je m'allonge sans enlever immédiatement mes vêtements. Mon corps est épuisé, mais ma tête refuse encore de ralentir."

    think "La pièce des Goumi. Le réseau. Toutes ces grilles."
    think "Pourquoi personne ne nous a jamais parlé de ça ?"

    "Je repense à la branche que Mara m'a montrée, à la petite cavité, à cette trappe que nous n'avons pas réussi à ouvrir."

    think "On reviendra avec Elias."

    "Cette idée devrait suffire pour ce soir."

    "Je ferme les yeux."

    pause 2.0

    "Quelques minutes passent. Peut-être davantage."

    $ current_period = "Nuit"

    stop music fadeout 2.0

    "Puis un léger frottement me réveille."
    $ danger_on()
    $ cam_move(fx=0.72, fy=0.48, z=1.13, t=9.0)

    noam panne "..."

    "Je ne bouge pas." id j18_nuit_immobile

    "Le bruit revient."

    play sound "audio/sfx_duct_scrape.wav" volume 0.72

    "Quelque chose glisse lentement contre le métal, quelque part derrière le mur."

    "Je tourne les yeux vers le bureau."

    "Il n'a pas bougé."

    "Le frottement se rapproche."

    noam peur "..."

    "Je retiens ma respiration."

    "Un léger grincement résonne juste derrière la grille."

    "Puis plus rien."

    pause 2.5

    "Je reste allongé, les yeux ouverts dans l'obscurité."

    "Une seconde. Deux. Dix."

    "Rien."

    "Je commence presque à croire que le bruit s'est arrêté quand quelque chose heurte doucement la paroi."

    play sound "audio/sfx_metal_clank.mp3" volume 0.72
    pause 0.8

    "Une seule fois."

    "Puis le frottement repart dans l'autre sens."

    "Il s'éloigne lentement jusqu'à disparaître complètement."

    noam peur "..."

    "Je ne me lève pas. Je n'appelle personne."

    "Je reste simplement là, les yeux fixés sur la grille, avec une certitude que je n'avais pas encore ce matin."

    play sound "audio/sfx_tinnitus.wav" volume 0.55
    "{cps=9}Ce réseau n'est pas vide.{/cps}"

    $ cam_reset(t=0.0)
    scene black with dread_pix
    $ danger_off()
    pause 1.0

    pause 1.0

    call end_day("19") from _call_end_day_19
    jump _19_0_1_1_0_REVEIL_CHAMBRE
