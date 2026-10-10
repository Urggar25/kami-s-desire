# JOUR 26 — Route 0_1_1_0_0 — La preuve
# Branche : Noam choisit de révéler la photographie à Kami.
# Dans cette route, Mara, Elias, Tomas, Kael et Sael sont déjà des Doppelgängers.
# L'identité des remplaçants n'est pas connue des protagonistes.
# La journée se poursuit directement dans les conduits, de nuit.

default j26_camera_choice = None
default j26_photo_revealed = False

label _26_0_1_1_0_0_REVEIL:
    $ current_day = 26
    $ day_id = 26
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.5
    $ blink()
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Je me réveille dans le lit d'Iris, coincé contre le bord après une nuit agitée."
    "Depuis que je dors chez elle, nous partageons le même lit ; à force de me retourner, j'ai dû lui laisser très peu de place."
    "Iris est déjà réveillée. Assise à côté de moi, une tasse à la main, elle me regarde avec des yeux aussi fatigués que les miens."

    $ showGroup([
        ("iris", "fatigue", 0.37),
        ("noam", "fatigue", 0.64),
    ])

    iris fatigue "La prochaine fois, je te laisse le bord du lit. J'ai passé la nuit à t'entendre te retourner dans tous les sens."
    noam fatigue "T'aurais pu me réveiller. Même si je vais pas me plaindre après t'avoir demandé de m'héberger."
    iris blase "Ah, donc tu admets enfin que je t'ai rendu service ? C'est bien. Note la date, on n'est pas près de revoir ça."

    "Elle essaie de sourire, mais ses yeux retournent aussitôt vers la tablette posée près d'elle."
    "Je reconnais l'application dans laquelle nous avons enregistré la photographie hier."

    noam reflexion "Tu l'as encore regardée ?"
    iris inquiet "Deux fois. Je voulais vérifier son visage. Et maintenant, je me demande si on a pas raté quelque chose derrière la cloison."
    noam inquiet "Hier, pendant le jeu, j'étais persuadé que Mara allait comprendre. Elle a plaisanté tout l'après-midi et c'est moi qui avais l'air suspect."
    iris reflexion "C'est bien ce qui me dérange. J'avais l'impression de parler à la même Mara que depuis le premier jour."

    "Je récupère mon téléphone entre les draps. Aucun message, aucune annonce particulière de Kami."
    "Depuis plusieurs jours, ce silence me paraissait reposant ; ce matin, j'aimerais presque qu'elle nous interrompe pour nous obliger à parler d'autre chose."

    noam raison "On ne peut pas continuer à garder ça pour nous."
    noam raison "Il y a encore quatre jours avant le départ et je ne sais même pas si Mara est la seule concernée."
    iris fatigue "Je sais, Noam. Le problème, c'est qu'il suffit qu'on en parle à la mauvaise personne pour que le corps disparaisse avant qu'on ait pu le montrer à qui que ce soit."

    "Je me retourne vers la caméra installée au-dessus de la porte. Elle a suivi le mouvement de ma tête lorsque je me suis levé."

    think "Il y a peut-être quelqu'un qui sait déjà."

    noam reflexion "Et Kami ? Elle a accès aux caméras, aux enregistrements, à tous les systèmes de maintenance."
    noam reflexion "Si quelque chose s'est passé dans cette station, elle devrait pouvoir le vérifier."
    iris agace "Tu veux demander de l'aide à Kami ? Après tout ce qu'elle nous a fait ?!"
    noam raison "Je dis pas qu'elle va nous aider. Mais elle peut pas laisser un imposteur repartir à la place d'un représentant."
    iris reflexion "Ou alors elle sait déjà et c'est précisément pour ça qu'elle ne nous en a jamais parlé."

    "Je n’ai pas de réponse. Iris me tend le tee-shirt que j’avais laissé sur la chaise."

    iris neutre "Habille-toi. On va manger, et après on décide."
    iris neutre "Mais je te demande une chose : tant qu'on n'a pas choisi quoi faire, évite d'aller provoquer Mara tout seul."
    noam sourire "Promis. Et merci pour cette nuit, vraiment."
    iris blase "Ouais, ouais. Tu me remercieras en arrêtant de me piquer toute la couverture quand ce bordel sera terminé."

    $ hideGroup()
    stop music fadeout 1.0
    jump _26_0_1_1_0_0_CAFETERIA

label _26_0_1_1_0_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est déjà animée lorsque nous arrivons."
    "Julian tente de convaincre Goumi de lui donner une deuxième portion, tandis qu'Elen se penche au-dessus des cartes du jeu d'hier pour en relire les règles."
    "À la grande table, Mara discute avec Elias et Tomas."
    "Elle éclate de rire au moment où je passe la porte et je ralentis malgré moi, avant qu'Iris me pousse discrètement dans le dos."

    $ showGroup([
        ("mara", "rire", 0.20),
        ("elias", "fatigue", 0.43),
        ("tomas", "neutre", 0.65),
        ("iris", "neutre", 0.85),
    ])

    mara rire "Ah bah voilà les deux disparus ! Vous vous êtes donné rendez-vous pour arriver en retard ?"
    iris agace "On est venus manger, Mara. Laisse-nous au moins le temps de prendre une assiette."
    julian sourire "Je défends le droit de chacun à apprécier les plaisirs de cette table. Est-ce donc un crime ?"
    elias fatigue "T'es surtout en train de faire chier Goumi depuis dix minutes. Prends ton plateau et va t'asseoir."

    "Je m'installe près d'Iris, en laissant volontairement une chaise entre Mara et moi."
    "Elle le remarque aussitôt, mais se contente de reprendre son verre."

    mara reflexion "Au fait, j'espère que j'ai pas été trop lourde hier soir. J'avais déjà un peu bu quand je t'ai croisé."
    noam hesitation "Non, t'inquiète. C'est juste que je voulais me coucher tôt."
    mara sourire "Ouais, j'avais compris. Je vais pas te courir après jusque dans ton lit, j'ai quand même un peu de dignité."

    "Elle adresse un clin d'œil à Julian, qui proteste aussitôt. Je fixe mon plateau pendant qu'ils s'accusent mutuellement d'avoir triché la veille."
    "Je connais son rire, ses plaisanteries douteuses et sa façon de parler plus fort que les autres."
    "Pourtant, dès que je relève les yeux, je revois le corps derrière la cloison."

    $ hideGroup()
    $ showGroup([
        ("kael", "calme", 0.23),
        ("sael", "neutre", 0.48),
        ("nyra", "reflexion", 0.72),
    ])

    kael calme "Le prochain vote ne devrait pas prendre toute l'après-midi, si on arrive à régler la question du recours."
    kael calme "Ça nous laisserait une soirée tranquille avant le départ."
    sael raison "Encore faudrait-il que le recours serve à quelque chose."
    sael raison "Si Kami reste juge de ses propres décisions, personne n'aura le courage de la contester longtemps."
    nyra reflexion "C'est précisément ce qu'on devrait clarifier avant demain."
    nyra reflexion "Une règle qui paraît généreuse peut être complètement inutile une fois appliquée."
    nyra reflexion "On l'a suffisamment constaté depuis le début du Conclave."

    "La discussion glisse sur la formulation de l'amendement."
    "Tomas corrige une remarque de Julian, qui prétend n'avoir besoin d'aucune leçon de droit pour reconnaître une bonne idée."
    "Iris reste silencieuse, les doigts serrés autour de son verre."

    think "Ils parlent déjà de demain. Comme si nous n'avions plus qu'à voter et attendre la navette."

    "Au moment de quitter la table, Mara me rattrape en attrapant doucement la manche de mon vêtement."

    $ hideGroup()
    $ showGroup([
        ("mara", "doute", 0.40),
        ("noam", "inquiet", 0.64),
    ])

    mara doute "Hé, je te demande juste un truc."
    mara doute "Je sais bien que je peux être envahissante, mais depuis quelques jours t'as l'air de prendre peur dès que je m'approche."
    mara doute "Si j'ai dit quelque chose qui t'a blessé, j'aimerais mieux que tu me le dises."
    noam inquiet "Tu n'as rien fait, Mara. J'ai encore pas mal de choses en tête et je crois que ça se voit plus que je ne voudrais."
    mara neutre "Bon... Je vais te croire, alors. Mais fais gaffe à pas trop t'enfermer dans tes histoires, d'accord ? On est presque au bout."

    "Elle lâche ma manche et repart rejoindre Elias."
    "Je reste immobile quelques secondes, avec l'impression désagréable d'avoir menti à quelqu'un qui me faisait sincèrement confiance."

    $ hideGroup()
    jump _26_0_1_1_0_0_DECISION

label _26_0_1_1_0_0_DECISION:
    $ current_period = "Après-midi"
    call show_custom_title("Un peu plus tard") from _call_j26_00_custom_title_1
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "De retour dans la chambre d'Iris, nous affichons la photographie sur sa tablette. Le visage de Mara est parfaitement reconnaissable."
    "À côté du corps, on distingue une partie de la cloison que nous avons déplacée ainsi que la carcasse d'un Goumi."

    $ showGroup([
        ("iris", "reflexion", 0.36),
        ("noam", "raison", 0.63),
    ])

    noam raison "Si je montre ça à Kami, elle saura au moins que nous ne parlons pas d'une simple impression."
    noam raison "Et si elle dispose d'enregistrements de la salle, elle pourra les comparer à notre photographie."
    iris inquiet "Tu comptes lui montrer devant tout le monde ?"
    iris inquiet "Parce que si elle répond par les haut-parleurs, Mara pourrait l'apprendre avant qu'on ait eu le temps de prévenir qui que ce soit."
    noam reflexion "Je pensais aller dans la salle du Conclave."
    noam reflexion "Il y a des caméras partout, et je pourrais projeter la photo sur l'écran central."
    noam reflexion "Mais tu as raison : à partir du moment où je fais ça, on ne contrôle plus ce qui se passe ensuite."

    "Je regarde longuement le fichier. Hier, j'aurais donné n'importe quoi pour obtenir une preuve que je n'avais pas halluciné."
    "Aujourd'hui, je l'ai sous les yeux et je ne sais toujours pas quoi en faire."

    iris neutre "Tu peux encore décider d'attendre. Je ne vais pas te forcer à raconter cette histoire."

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Que faire de la photographie ?"
        "Montrer le corps de Mara à Kami":
            $ j26_camera_choice = "reveal"
            $ j26_photo_revealed = True
            jump _26_0_1_1_0_0_CAMERA
        "Garder la découverte secrète":
            $ j26_camera_choice = "secret"
            # Embranchement majeur réservé pour une autre route.
            jump _26_0_1_1_0_0_SECRET_PLACEHOLDER

label _26_0_1_1_0_0_SECRET_PLACEHOLDER:
    # Route non écrite : ne pas rediriger artificiellement vers la révélation.
    "Je referme le fichier. Nous n'allons rien annoncer pour le moment."
    return

label _26_0_1_1_0_0_CAMERA:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "La salle du Conclave est vide. Iris referme la porte pendant que je branche ma tablette au terminal de présentation."
    "Le terminal reconnaît ma tablette et ouvre ses dossiers. Je retrouve la photographie que nous avons prise hier."
    call j26_transferer_photo from _call_j26_transferer_photo
    "La photographie occupe maintenant le grand écran. À cette taille, les blessures et les plis de la veste de Mara sont encore plus difficiles à regarder."
    "Je relève les yeux vers la caméra installée au-dessus de nos sièges. Son objectif pivote légèrement dans ma direction."

    $ showGroup([
        ("iris", "inquiet", 0.34),
        ("noam", "determine", 0.65),
    ])

    iris inquiet "Je suis toujours pas convaincue que ce soit une bonne idée."
    iris inquiet "Mais si elle nous écoute, autant lui donner des faits précis plutôt que de lui demander ce qu'elle sait déjà."
    noam determine "C'est ce que je vais faire. Et si elle accepte de vérifier les caméras, on aura peut-être enfin une explication."

    "Je me place face à l'objectif."
    "Je m'attends presque à voir apparaître le visage de Kami avant même d'avoir terminé ma première phrase, comme chaque fois que nous avons essayé de discuter des Commandements."

    noam raison "Kami, j'ai besoin de ton attention."
    noam raison "Hier, Iris et moi avons trouvé un cadavre dans une pièce située derrière la salle de maintenance des Goumi."
    noam raison "J'ai déjà vu ce corps plusieurs jours auparavant, mais j'étais seul et personne ne m'a cru."
    "Je désigne l'écran central."
    noam determine "Voici une photographie prise sur place."
    noam determine "Le corps ressemble en tous points à celui de Mara, notre représentante d'Axiome, alors que Mara continue de vivre parmi nous."
    noam determine "Nous avons parlé avec elle ce matin même."
    iris raison "Je confirme ce qu'il raconte."
    iris raison "On a déplacé un Goumi, trouvé une pochette de tissu coincée derrière lui, puis retiré une plaque de métal."
    iris raison "Le cadavre se trouvait derrière cette plaque, dans une cavité."

    "Nous attendons une réaction."
    "Le projecteur continue de diffuser la photographie et l'objectif de la caméra reste braqué sur nous, mais aucune voix ne retentit."

    noam inquiet "Kami, tu nous surveilles depuis le début."
    noam inquiet "Tu as forcément accès aux enregistrements des couloirs et des salles de maintenance."
    noam inquiet "Je ne te demande même pas de nous croire : je te demande de vérifier ce qu'il s'est passé."

    "Je regarde vers l'écran où elle apparaît habituellement. Il reste noir."

    noam raison "Dans quatre jours, nous sommes censés repartir sur Terre."
    noam raison "Si quelqu'un a réellement pris la place de Mara, tu comprends bien que ça ne concerne plus seulement notre sécurité dans le Conclave."
    noam raison "Il faut savoir qui tu vas laisser quitter cette station."

    "Iris lève la tête à son tour, comme si elle cherchait à savoir si la caméra nous suivait toujours."

    iris inquiet "Kami, je sais que tu peux nous entendre. On n'est pas en train de parler d'un vote ou de contester tes règles."
    iris inquiet "On te signale la présence d'un cadavre dans ta station. Tu pourrais au moins nous dire si tu comptes vérifier."

    "Personne ne répond. Même les écrans autour de la table restent éteints, alors que j'ai vu Kami les activer à distance des dizaines de fois."

    noam colere "Tu trouves toujours le moyen de nous interrompre quand ça t'amuse, et maintenant qu'on te signale peut-être un meurtre, tu n'as rien à dire ?!"
    noam colere "Je ne comprends pas ce que tu attends pour réagir !"

    "Ma voix résonne dans la salle. Je laisse passer encore quelques secondes, puis baisse les yeux vers la photographie."

    think "Elle a entendu. C'est impossible qu'elle n'ait pas entendu."

    iris fatigue "On ferait mieux d'arrêter. Si elle veut répondre, elle sait où nous trouver."
    noam fatigue "Je pensais qu'elle serait au moins curieuse. D'habitude, elle se mêle de tout ce qu'on fait..."

    "Je n'ai pas le temps de terminer. La porte s'ouvre derrière nous et Tomas entre dans la salle, un dossier sous le bras."
    "Il s'arrête dès qu'il aperçoit la photographie."

    $ hideGroup()
    $ showGroup([
        ("tomas", "surpris", 0.22),
        ("iris", "inquiet", 0.50),
        ("noam", "hesitation", 0.78),
    ])

    tomas surpris "Vous faites quoi ici ? Je venais récupérer des documents pour le vote de demain, mais... Attendez, c'est Mara sur cette image ?"
    noam inquiet "Tomas, on allait justement devoir t'en parler. Iris et moi avons découvert ce corps hier dans les conduits."
    noam inquiet "C'est une des raisons pour lesquelles j'avais tellement de mal à accepter les conclusions de l'examen médical."
    tomas reflexion "Un corps ? Tu veux dire que tu as trouvé une personne morte qui ressemble à Mara, alors qu'on vient encore de déjeuner avec elle ?"
    iris colere "C'est exactement ça, Tomas. Et avant que tu me demandes si Noam a rêvé, j'étais avec lui. J'ai vu la même chose et j'ai pris cette photo."

    "Tomas s'approche de l'écran."
    "Il ne recule pas devant l'image, mais l'observe avec une attention presque excessive, en examinant le contour du visage et les bords de la cloison."

    tomas reflexion "Je ne remets pas en cause le fait que vous soyez tous les deux persuadés d'avoir vu quelque chose."
    tomas reflexion "En revanche, cette photographie ne suffit pas à établir qu'il s'agit réellement de Mara."
    tomas reflexion "Vous savez comme moi que les ordinateurs de la salle d'observation permettent de retoucher des images, et même d'en créer de toutes pièces."
    noam desaccord "On n'a jamais dit que cette photo devait suffire à elle seule ! Mais elle correspond exactement à ce qu'on a vu."
    noam desaccord "Si tu veux, je peux te donner le fichier original avec les informations de prise de vue."
    tomas raison "Et les informations d'un fichier peuvent elles aussi être modifiées."
    tomas raison "Ce que je veux dire, c'est qu'on ne peut pas accuser une représentante sur la base d'une image numérique."
    tomas raison "Tu imagines les conséquences si on se trompe ?"

    "Il ne suffit pas de lui montrer cette photographie. Je dois lui expliquer comment nous en sommes arrivés là, sans perdre le fil de ce que nous avons découvert."
    call j26_preuve_impossible from _call_j26_preuve_impossible
    if j26_preuve_success:
        noam determine "Ce n\u0027est pas seulement une photographie, Tomas. J\u0027ai aperçu ce corps avant même de trouver le tissu, puis Iris a constaté la même chose que moi avant que nous prenions la photo."
        tomas reflexion "Cela rend votre récit cohérent, je te l\u0027accorde. Mais ce n\u0027est pas une expertise de l\u0027image, et nous devons vérifier les lieux."

    iris colere "Personne ne cherche à fabriquer une accusation !"
    iris colere "On a trouvé un cadavre dans les murs de cette station et on veut qu'il soit examiné."
    iris colere "Pourquoi tu commences déjà à parler de faux ?"
    tomas inquiet "Parce qu'il y a une photo de Mara, apparemment morte, sur l'écran du Conclave. Et vous étiez en train de montrer ça à Kami."
    tomas inquiet "J'aimerais comprendre ce que vous comptiez obtenir sans prévenir les autres."

    "La question me prend de court."
    "Quelques minutes plus tôt, j'étais persuadé d'avoir enfin trouvé une manière raisonnable de présenter les faits."
    "Maintenant, Tomas a l'air de nous reprocher d'avoir essayé de rendre cette découverte publique."

    noam raison "Je voulais que Kami vérifie ses enregistrements."
    noam raison "Elle contrôle toutes les caméras du Conclave et devrait être capable de déterminer si quelqu'un a déplacé le corps."
    noam raison "Mais elle n'a absolument pas répondu."
    tomas fatigue "Dans ce cas, il faut parler aux autres."
    tomas fatigue "Je comprends que vous ayez hésité. Mais vous pouvez pas cacher une découverte pareille et attendre qu'on vous fasse confiance."
    iris inquiet "On sait pas si toutes les personnes présentes ici sont encore celles qu'on a rencontrées au premier jour. C'est pour ça qu'on a hésité."
    tomas surpris "Vous pensez qu'il pourrait y en avoir d'autres ?"
    noam inquiet "Je sais pas combien. Mais si quelqu'un peut prendre la place de Mara, il peut recommencer avec les autres."

    "Tomas baisse les yeux vers le dossier qu'il tient toujours, puis le pose sur une chaise."

    tomas determine "Je vais chercher les autres. On en parlera ensemble, devant la photographie. Personne ne doit découvrir ça par des rumeurs."

    "Il sort avant qu'Iris ait trouvé quoi lui répondre. Elle me regarde longuement, puis reporte son attention sur la photographie."

    iris fatigue "J'espère vraiment qu'il a raison et qu'ils vont nous écouter."
    iris fatigue "Parce qu'à partir de maintenant, on pourra difficilement prétendre que Mara ne sait rien."

    $ hideGroup()
    jump _26_0_1_1_0_0_CONFRONTATION

label _26_0_1_1_0_0_CONFRONTATION:
    $ current_period = "Soir"
    call show_custom_title("En début de soirée") from _call_j26_00_custom_title_2
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Les représentants entrent par petits groupes. Ryn arrive avec Nyra, suivis de Sael et d'Elen."
    "Lysa me lance un regard interrogateur avant même d'avoir vu l'écran."
    "Mara est l'une des dernières à entrer, accompagnée d'Elias et de Kael."
    "Tomas leur a visiblement expliqué qu'il s'agissait d'une découverte importante, mais il a évité de prononcer le nom de Mara devant tout le monde."
    "Lorsque celle-ci reconnaît son propre visage sur la photographie, elle s'arrête devant sa chaise."

    $ showGroup([
        ("mara", "doute", 0.18),
        ("ryn", "colere", 0.39),
        ("tomas", "raison", 0.61),
        ("noam", "inquiet", 0.83),
    ])

    ryn colere "Bon, quelqu'un peut nous expliquer pourquoi Tomas nous a tous fait venir ici comme si on était en plein vote ?"
    ryn colere "Il m'a parlé d'un cadavre, mais j'aimerais bien savoir ce qu'il se passe avant que ça dégénère encore."
    tomas raison "Noam et Iris disent avoir découvert un corps qui ressemble à Mara dans une zone de maintenance."
    tomas raison "La photographie est censée avoir été prise hier."
    tomas raison "Je leur ai expliqué qu'on peut fabriquer cette image sur les ordinateurs de la salle d'observation. Mais écoutons-les avant de conclure."
    mara doute "Attends... C'est censé être moi, là ? Tu m'as fait venir pour m'annoncer qu'il y avait mon cadavre caché dans la station ?"

    "Elle cherche d'abord une réaction amusée autour de la table, comme si elle s'attendait à ce que quelqu'un lui explique une plaisanterie de très mauvais goût."
    "Personne ne rit."

    noam raison "Hier matin, un morceau de tissu s'est coincé dans la ventilation de ma chambre."
    noam raison "Iris et moi avons décidé de suivre les conduits pour voir d'où il provenait."
    noam raison "On a retrouvé un tissu identique derrière un Goumi, dans la salle où Elias stockait le matériel."
    noam raison "Derrière, il y avait une plaque qui cachait une ouverture dans le mur."
    iris inquiet "Et derrière cette ouverture, il y avait un corps."
    iris inquiet "J'ai reconnu Mara immédiatement, mais j'ai demandé à Noam de me confirmer que je ne me trompais pas."
    iris inquiet "On est restés suffisamment longtemps pour prendre une photo et vérifier ce qu'on pouvait sans tout déplacer."
    sael reflexion "Vous avez touché le corps ? Vérifié s'il y avait encore une respiration ou un pouls ?"
    sael reflexion "Si vous avez trouvé quelqu'un dans cet état, vous auriez dû m'appeler au lieu de repartir."
    noam fatigue "L'odeur et l'état du corps ne laissaient pas vraiment de doute."
    noam fatigue "Je l'avais déjà vu dans cette salle quelques jours avant, et quand j'avais tenté d'en parler, personne ne m'avait cru."
    lysa inquiet "Attends, tu veux dire que c'est exactement ce que tu racontais quand on t'a ramené à l'infirmerie ?"
    lysa inquiet "La Mara morte, la salle des Goumi... tout ça ?"
    noam raison "Oui. Sauf que cette fois Iris était avec moi, et qu'on a pu photographier ce qu'on avait trouvé."

    $ hideGroup()
    $ showGroup([
        ("mara", "doute", 0.25),
        ("elen", "inquiet", 0.48),
        ("iris", "colere", 0.72),
    ])

    elen inquiet "Mais... Mara est juste devant nous."
    elen inquiet "On a passé l'après-midi ensemble hier, et ce matin encore on mangeait à la même table."
    elen inquiet "Vous pensez vraiment qu'il y aurait quelqu'un qui lui ressemble au point de pouvoir la remplacer ?"
    iris colere "Je sais à quel point ça paraît absurde, Elen. Hier encore j'aurais dit exactement la même chose que toi."
    iris colere "Mais cette image, je sais où on l'a prise. Et ce corps, je l'ai vu."
    mara desaccord "Donc tu me regardes depuis ce matin en te demandant si je suis une espèce d'imposture ? C'est bien ça ?"
    mara desaccord "Parce que j'avais remarqué que vous faisiez des têtes bizarres, mais je pensais pas que ça allait jusque-là."

    "Elle se tourne vers moi. Elle n'a plus du tout l'air de plaisanter."

    mara doute "Noam, hier soir je t'ai demandé si je t'avais fait quelque chose. Tu m'as répondu que tout allait bien."
    mara doute "Et aujourd'hui tu m'amènes devant tout le monde pour montrer une photo de mon cadavre ?"
    mara doute "Tu pourrais au moins m'expliquer à quel moment t'as décidé que j'étais plus moi."
    noam inquiet "Je n'ai jamais dit que je savais exactement ce que tu étais."
    noam inquiet "J'essaie seulement de comprendre comment on peut avoir trouvé une personne qui te ressemble autant."
    mara agace "Mais écoute-toi ! Tu parles de moi comme si j'étais un truc à examiner."
    mara agace "Je suis là depuis le premier jour, j'ai voté avec vous, je vous ai aidés quand ça allait mal..."
    mara agace "Qu'est-ce que je suis censée faire de plus pour que vous arrêtiez de me regarder comme ça ?"

    "Je cherche quelque chose à lui répondre, mais elle n'attend pas que je trouve."
    "Elle s'avance jusqu'à l'écran et contemple la photographie pendant un long moment."

    mara triste "Tu sais ce qui est le plus dégueulasse ? C'est même pas cette photo."
    mara triste "J'ai pas demandé à la voir, et je vais probablement l'avoir dans la tête pendant des semaines."
    mara triste "Le pire, c'est de me dire que vous avez passé une journée entière avec moi en pensant que je pouvais vous faire du mal."
    mara triste "Hier, quand je t'ai demandé de venir boire un verre, je voulais simplement qu'on passe un peu de temps ensemble avant de rentrer."
    mara triste "Je savais que t'allais pas très bien et je m'étais dit qu'une soirée à raconter des conneries te ferait peut-être du bien."
    mara triste "Maintenant j'apprends que pendant tout ce temps, tu pensais peut-être que j'étais venue pour te tuer."

    "Sa voix n'a rien de théâtral."
    "Elle paraît surtout fatiguée, comme si elle venait de comprendre pourquoi je l'évitais depuis plusieurs jours."
    "Elen pose une main sur son épaule, et Mara ne la repousse pas."

    mara doute "Je sais que je fais souvent la conne."
    mara doute "Je me moque de tout le monde, je dis des trucs déplacés et j'ai sûrement dépassé les bornes plus d'une fois."
    mara doute "Mais je pensais qu'au moins ici, j'avais fini par avoir quelques amis. C'est ridicule, hein ?"
    mara doute "Ça fait presque un mois que je vous appelle ma bande de bras cassés. Et maintenant, il suffit d'une photo pour que vous me tourniez le dos ?"

    "Elle me regarde à nouveau, les yeux humides."
    "Je voudrais lui rappeler le corps derrière la cloison. Mais je repense à nos premières conversations, à ses plaisanteries et aux fois où elle a détendu l'atmosphère."

    mara triste "Alors regarde-moi, Noam. Tu m'as connue pendant vingt-six jours."
    mara triste "Est-ce que t'es vraiment capable de me dire, là, devant eux, que je suis pas Mara ?"

    "La question me laisse sans voix. Je ne peux pas lui répondre oui, parce que je n'ai aucune explication à ce que nous avons découvert."
    "Mais lui répondre non reviendrait à ignorer le cadavre que j'ai vu de mes propres yeux."

    noam inquiet "Je ne sais pas qui est la personne qu'on a trouvée. Et je ne sais pas pourquoi elle te ressemble."
    noam inquiet "Mais je sais que si on refuse de vérifier simplement parce que tu es là devant nous, on risque de passer à côté de quelque chose de beaucoup plus grave."

    "Mara recule d'un pas. Elle secoue la tête, puis reprend sa place sans un mot. Elen s'assoit près d'elle et lui prend la main."

    $ hideGroup()
    $ showGroup([
        ("lysa", "desaccord", 0.19),
        ("tomas", "raison", 0.39),
        ("nyra", "reflexion", 0.61),
        ("ryn", "determine", 0.81),
    ])

    lysa desaccord "Noam a déjà eu une période compliquée. Même avec Iris comme témoin, j'ai du mal à croire qu'il existe une deuxième Mara morte derrière un mur."
    tomas raison "La photo pourrait avoir été créée sur les ordinateurs de l'observatoire."
    tomas raison "Ça ne signifie pas qu'ils mentent, mais on peut pas accuser Mara sur cette base."
    nyra reflexion "On n'a pas besoin de juger Mara. Il y aurait un corps dans une pièce précise : c'est ça qu'on peut vérifier."
    ryn determine "On arrête de tourner autour de cette photo et on va voir derrière ce putain de mur. J'ai pas envie de soupçonner tout le monde jusqu'au départ."

    "L'idée provoque un murmure autour de la table."
    "Sael approuve immédiatement, en précisant qu'elle veut vérifier elle-même l'état du cadavre. Mara relève la tête."

    $ hideGroup()
    $ showGroup([
        ("mara", "triste", 0.22),
        ("sael", "raison", 0.45),
        ("elias", "fatigue", 0.66),
        ("noam", "reflexion", 0.86),
    ])

    mara triste "Je viens aussi. Si vous comptez examiner un corps avec ma tête, je veux pas attendre ici qu'on décide si j'ai le droit de rentrer chez moi."
    sael raison "Si le corps est toujours là, il faudra éviter de déplacer quoi que ce soit avant que je l'aie examiné."
    sael raison "Et je préfère prévenir : avec les moyens de l'infirmerie, je pourrai peut-être déterminer certaines choses, mais certainement pas tout expliquer sur-le-champ."
    elias fatigue "Vous voulez faire passer tout le monde là-dedans ? Y a des endroits où on rampe sur le ventre, et la lumière est pourrie."
    noam raison "Je peux vous guider. Iris et moi avons fait le trajet hier, et l'ouverture se trouve assez près de ma chambre pour qu'on n'ait pas besoin de traverser toute la station."
    elias reflexion "On ferait mieux d'y aller demain matin. On aura le temps de préparer les lampes et au moins on verra où on met les pieds."

    "Plusieurs représentants acquiescent."
    "Ryn semble prêt à accepter le report, mais je revois le morceau de tissu coincé derrière le Goumi et l'espace dans lequel le corps avait été dissimulé."

    noam determine "Non. Il faut y aller maintenant."
    elias fatigue "Noam, je viens de t'expliquer pourquoi c'était une mauvaise idée."
    elias fatigue "On aura la même ventilation demain, sauf qu'on aura dormi et qu'on pourra s'organiser sans faire ça dans le noir."
    noam colere "Et si quelqu'un déplace le corps cette nuit ? Demain, on aura plus que cette photo, et Tomas vient de vous dire pourquoi elle ne suffira pas."
    tomas reflexion "Tu présumes qu'une personne serait suffisamment au courant de votre découverte pour intervenir cette nuit."
    noam raison "On vient d'en parler à tout le monde et j'ai montré la photo à Kami. On peut plus garantir que le corps restera là."

    "Iris se rapproche de moi. Elle regarde Elias, puis les autres représentants qui semblent encore hésiter."

    iris determine "Je suis d'accord avec Noam."
    iris determine "Si vous voulez vraiment vérifier, autant le faire pendant que vous savez encore où chercher."
    iris determine "Je connais le chemin et je peux vous aider à passer les endroits difficiles."
    kael calme "On peut au moins récupérer des lampes avant de partir."
    kael calme "Ça n'a aucun sens de se précipiter et de se blesser dans un conduit simplement pour gagner quelques heures."
    ryn determine "Alors on prend ce qu'il faut et on y va."
    ryn determine "Ceux qui veulent rester ici peuvent rester, mais moi je préfère voir ce corps de mes propres yeux plutôt que continuer à écouter tout le monde parler d'images truquées."

    "Une dernière discussion s'engage sur le nombre de personnes capables de passer dans les conduits."
    "Nyra fait remarquer qu'il serait absurde d'envoyer douze représentants se coincer dans une même galerie."
    "Sael insiste pour accompagner le groupe ; Elias accepte finalement d'apporter le matériel nécessaire à l'ouverture de la cloison."

    elen inquiet "Je préférerais qu'on y aille tous ensemble, au moins jusqu'à la chambre de Noam."
    elen inquiet "Je n'ai aucune envie d'attendre ici pendant que vous découvrez peut-être quelque chose d'horrible."
    mara neutre "Moi, en tout cas, je viens."
    mara neutre "J'ai pas passé une demi-heure à m'entendre expliquer que je suis peut-être morte pour rester sagement à table pendant que vous allez vérifier."

    "Personne ne tente de la convaincre de renoncer."
    "Je ne sais pas si les autres acceptent sa présence parce qu'ils ont confiance en elle, ou parce qu'ils auraient autant de mal que moi à lui demander de rester à l'écart."

    $ hideGroup()
    jump _26_0_1_1_0_0_EXPEDITION

label _26_0_1_1_0_0_EXPEDITION:
    $ current_period = "Nuit"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "Nous quittons la salle du Conclave en direction des dortoirs. À cette heure, le couloir est désert, mais nous sommes assez nombreux pour y faire un vacarme considérable."
    "Elias transporte une caisse de lampes et d'outils. Derrière lui, les autres discutent encore de l'intérêt de cette expédition, sans parvenir à se mettre d'accord sur ce qu'ils comptent faire en arrivant."

    $ showGroup([
        ("elias", "fatigue", 0.22),
        ("nyra", "reflexion", 0.50),
        ("ryn", "determine", 0.78),
    ])

    elias fatigue "On va pas entrer à douze dans le même conduit. C'est assez étroit comme ça, et si quelqu'un se coince, tout le monde restera bloqué derrière."
    nyra reflexion "On peut avancer par groupes de trois, en laissant quelques minutes entre chaque départ. Le premier groupe vérifie le passage et prévient les suivants si nécessaire."
    ryn determine "D'accord, mais Noam passe devant. C'est lui qui connaît le chemin, et j'ai pas envie qu'on passe la nuit à tourner dans ces foutus tuyaux."

    "Je commence à répondre, mais Iris me devance en s'avançant d'un pas."

    $ hideGroup()
    $ showGroup([
        ("iris", "determine", 0.25),
        ("noam", "reflexion", 0.50),
        ("sael", "mefiant", 0.75),
    ])

    iris determine "Dans ce cas, je pars avec lui. Je l'ai accompagné hier et je compte pas le laisser retourner tout seul là-dedans après ce qu'on a trouvé."
    noam reflexion "Je peux quand même me débrouiller pour parcourir quelques mètres sans toi, tu sais."
    iris colere "Tant mieux pour toi. Moi, je viens, et c'est pas négociable."
    sael mefiant "Je serai la troisième. Si ce corps existe, mieux vaut que je puisse l'examiner avant que tout le monde commence à fouiller autour."

    "Personne ne s'y oppose. Julian propose de prendre le départ suivant avec Elen et Mara, ce qui provoque quelques regards embarrassés, mais Mara accepte sans discuter."
    "Tomas et Kael partent avec Nyra dans le troisième groupe. Ryn, Elias et Lysa ferment la marche."
    "Je remarque qu'Iris vérifie deux fois le fonctionnement de sa lampe avant de m'en tendre une. Elle ne m'a pas lâché des yeux depuis que nous avons quitté le Conclave."

    scene bg_chambre at adaptive_fullscreen with dissolve
    "Nous entrons dans ma chambre pendant qu'Elias pose sa caisse près du bureau. Je lève les yeux vers la grille d'aération, bien au-dessus du bureau, puis récupère le tournevis qu'il me tend."

    $ hideGroup()
    $ showGroup([
        ("elias", "fatigue", 0.24),
        ("iris", "inquiet", 0.50),
        ("noam", "reflexion", 0.76),
    ])

    elias fatigue "Les vis ont déjà pris cher avec tous vos allers-retours. Faites gaffe en retirant la grille, j'ai pas de quoi la remplacer cette nuit."
    iris inquiet "On va faire attention. Vous nous laissez juste un peu d'avance avant de faire entrer le deuxième groupe."
    elias neutre "Ouais, j'ai compris. Si vous avez un souci, vous revenez nous le dire au lieu de jouer aux héros."

    "Je retire la grille et la pose contre le bureau. L'air qui sort du conduit est froid, chargé de cette odeur de poussière que je commence malheureusement à bien connaître."
    "Sael récupère une petite trousse dans la caisse d'Elias, tandis qu'Iris vérifie que son téléphone est bien dans sa poche."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    $ flashlight_on(0)
    play sound sfx_creak volume 0.35

    "Je m'engage le premier dans l'ouverture. Iris me suit immédiatement, et Sael referme la marche avec sa trousse coincée contre elle."
    "Le conduit grince légèrement sous notre poids. Nous avançons à genoux, en éclairant tour à tour les renforts et les embranchements pour éviter de nous tromper de direction."

    $ showGroup([
        ("iris", "inquiet", 0.27),
        ("noam", "reflexion", 0.52),
        ("sael", "mefiant", 0.77),
    ])

    sael mefiant "Vous m'avez dit que le corps était dissimulé derrière une cloison. Comment avez-vous découvert l'ouverture ?"
    noam reflexion "On a remarqué qu'un Goumi avait été déplacé. Derrière, il y avait une plaque métallique et un morceau de tissu coincé dans une fixation."
    iris inquiet "Et l'odeur aussi. Dès qu'on a ouvert, on a compris qu'il y avait quelque chose derrière."
    sael reflexion "Alors évitez de toucher au corps quand nous arriverons. Il faut au moins que je puisse voir sa position avant de le déplacer."

    "Je hoche la tête et reprends notre progression. Derrière moi, Iris se retourne régulièrement pour vérifier que Sael parvient à nous suivre."
    "Au dernier embranchement, je reconnais la tôle légèrement tordue contre laquelle je m'étais cogné la première fois. La grille de la salle des Goumi se trouve juste après."

    think "J'espère seulement que rien n'a changé depuis hier."

    "Je m'approche de l'ouverture, dirige ma lampe à travers les barreaux et retrouve la silhouette immobile des deux Goumi de rechange."
    "Rien ne paraît avoir bougé."

    noam reflexion "C'est ici. Je vais retirer la grille, puis je vous aiderai à descendre."
    iris inquiet "D'accord, mais attends que je sois juste derrière toi. J'ai aucune envie de rester coincée toute seule dans ce truc."

    "Je libère la grille et me laisse glisser sur l'établi. Iris me passe sa lampe avant de descendre à son tour, puis nous aidons Sael à trouver un appui."

    $ hideGroup()
    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve

    "La salle est exactement comme nous l'avons laissée. La plaque qui masque la cavité est toujours appuyée contre le mur, et le Goumi que nous avions poussé est resté sur le côté."
    "Iris s'arrête près de la cloison. Je devine à sa manière de tenir sa lampe qu'elle hésite à regarder derrière."

    $ showGroup([
        ("iris", "peur", 0.22),
        ("noam", "inquiet", 0.50),
        ("sael", "mefiant", 0.78),
    ])

    iris peur "C'est là. Hier, on a écarté cette plaque pour voir ce qu'il y avait derrière... J'aimerais vraiment ne pas avoir à recommencer."
    sael mefiant "Reculez un peu et éclairez-moi. Je vais regarder avant qu'on touche à quoi que ce soit."

    "Sael s'accroupit, saisit le bord de la plaque avec précaution et la déplace suffisamment pour dégager l'ouverture. Une odeur épouvantable s'en échappe aussitôt."
    "Je détourne la tête par réflexe, puis oblige mes yeux à revenir vers la cavité."

    scene bg_cg040 at adaptive_fullscreen with dissolve

    "Mara est toujours là, recroquevillée dans le même espace trop étroit pour elle. Sa veste est coincée sous son bras, exactement comme hier, et son visage apparaît dès que Sael dirige la lampe vers l'intérieur."
    "Je sens Iris agripper ma manche. Elle ne dit rien, mais son regard passe du cadavre à Sael, comme si elle attendait encore qu'on nous annonce que tout cela était une erreur."

    $ showGroup([
        ("iris", "peur", 0.23),
        ("noam", "inquiet", 0.50),
        ("sael", "reflexion", 0.77),
    ])

    noam inquiet "C'est bien elle. Tu vois maintenant pourquoi je pouvais pas attendre demain ?"
    sael reflexion "Je vois un corps qui lui ressemble, oui. Laisse-moi vérifier le reste avant de me demander d'en tirer une conclusion."
    iris inquiet "Tu peux au moins nous dire depuis combien de temps elle est morte ?"
    sael reflexion "Pas comme ça. Il faut d'abord regarder son état, ses blessures et les conditions dans lesquelles elle a été conservée."

    "Sael pose sa trousse près de la cloison, enfile une paire de gants et commence son examen. Je lui laisse la place, pendant qu'Iris s'éloigne vers l'établi pour respirer un peu moins cette odeur."
    "Elle approche la lampe du visage, observe le cou et les vêtements, puis examine la position du bras coincé sous le corps. Ses gestes sont lents et suffisamment précis pour que je n'ose plus lui poser de questions."

    sael reflexion "Il y a des lésions au niveau du cou, mais je préfère ne rien avancer avant d'avoir vu l'autre côté. Vous avez pris des photos hier ?"
    noam raison "Oui, sur ma tablette. Je peux te les montrer quand tu veux, il y en a plusieurs sous des angles différents."
    sael mefiant "Garde-les. J'aurai besoin de les comparer avec ce que je vois, surtout si le corps a été déplacé avant votre découverte."

    "Un bruit métallique résonne au-dessus de nous. Iris relève aussitôt sa lampe vers la grille."

    iris inquiet "C'est sûrement le deuxième groupe. Ils sont déjà arrivés à la dernière bifurcation."
    noam reflexion "Je vais les aider à descendre. Sael, tu peux continuer sans nous ?"
    sael neutre "Oui. Et demande-leur de ne pas s'approcher de la cloison pour le moment."

    $ hideGroup()
    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve

    "Julian apparaît le premier dans l'ouverture. Je l'aide à prendre appui sur l'établi, puis Elen descend à son tour. Mara arrive derrière eux et s'arrête un instant en voyant l'endroit où nous nous trouvons."

    # Deuxième groupe arrivé : les six représentants restent visibles.
    $ showGroup([
        ("julian", "inquiet", 0.12),
        ("elen", "peur", 0.27),
        ("mara", "doute", 0.42),
        ("sael", "reflexion", 0.57),
        ("iris", "peur", 0.72),
        ("noam", "inquiet", 0.87),
    ])

    julian inquiet "Eh bien... Je commence à comprendre pourquoi personne ne vient jamais ici. On a dû ramper pendant dix bonnes minutes pour rejoindre une salle où il n'y a même pas de sortie normale."
    elen inquiet "Vous avez trouvé quelque chose ? On a senti une odeur bizarre avant même d'arriver à la grille."

    "Je me décale pour leur laisser voir la cloison ouverte. Sael est toujours accroupie devant le corps, occupée à examiner les vêtements."
    "Elen porte aussitôt la main à sa bouche. Julian cesse de parler et demeure quelques secondes à regarder, incapable de trouver quoi dire."

    elen peur "Oh non... Mais c'est vraiment..."
    julian peur "Mon Dieu. Noam, je pensais que vous aviez peut-être confondu quelque chose, mais... On voit parfaitement son visage."

    "Je regarde Mara. Elle s'est avancée de quelques pas, sans rejoindre les autres, et fixe maintenant l'ouverture avec une expression que je n'arrive pas à comprendre."

    mara doute "C'est... C'est quoi ce truc ? Vous êtes en train de me dire que quelqu'un a laissé une fille qui me ressemble derrière ce mur ?"
    noam inquiet "C'est exactement ce qu'on essaie de comprendre depuis hier. Sael est en train de l'examiner pour savoir ce qui lui est arrivé."
    mara stress "Mais putain, Noam... Tu te rends compte de ce que ça fait de voir sa propre tête sur un cadavre ?!"

    "Sa voix tremble légèrement. Elen se rapproche d'elle et lui pose une main dans le dos, tandis que Julian détourne enfin les yeux du corps."

    elen inquiet "Mara, viens t'asseoir un moment. T'es pas obligée de regarder ça, et Sael a sûrement besoin de place pour travailler."
    mara fatigue "Non, ça va... Enfin non, ça va pas, évidemment. Mais je veux savoir ce que c'est, moi aussi."

    "Je n'insiste pas. Après tout, il serait difficile de lui interdire de regarder alors que nous avons exigé qu'elle vienne vérifier par elle-même."
    "Sael continue son examen pendant que Julian aide Elen à déplacer une caisse pour que Mara puisse s'asseoir. Pendant quelques minutes, personne n'élève la voix."
    "Je commence même à croire que nous allons enfin pouvoir discuter de cette découverte sans nous accuser mutuellement."

    play sound sfx_creak volume 0.6

    "Un choc résonne dans le conduit, suivi de plusieurs frottements précipités. Je lève la tête juste au moment où quelqu'un appelle depuis l'ouverture."

    tomas peur "Noam ! Vous êtes là ?! Aidez-nous à descendre, vite !"

    "Je me précipite vers l'établi. Tomas apparaît à quatre pattes dans le conduit, essoufflé, et manque de tomber en essayant de passer ses jambes par l'ouverture."
    "Kael arrive juste derrière lui. Tous les deux ont le visage tendu et regardent sans cesse dans la direction d'où ils viennent."

    $ hideGroup()
    # Arrivée de Tomas et Kael : huit représentants dans la pièce.
    # On conserve les six déjà présents et on ajoute les nouveaux arrivants.
    $ showGroup([
        ("julian", "inquiet", 0.075),
        ("elen", "peur", 0.195),
        ("mara", "stress", 0.315),
        ("sael", "mefiant", 0.435),
        ("tomas", "peur", 0.555),
        ("kael", "inquietude", 0.675),
        ("iris", "inquiet", 0.795),
        ("noam", "inquiet", 0.915),
    ])

    noam inquiet "Qu'est-ce qui vous arrive ? Où est Nyra ? Elle était censée venir avec vous."
    tomas peur "C'est Ryn ! Il a complètement pété les plombs dans les conduits, il s'est jeté sur Nyra sans prévenir !"
    iris inquiet "Quoi ?! Mais pourquoi est-ce qu'il aurait fait ça ? Ils se sont disputés ?"
    kael inquietude "On n'en sait rien ! On avançait vers le dernier embranchement quand il nous a rejoints. Il a attrapé Nyra et l'a cognée contre la paroi avant qu'on ait le temps de comprendre ce qui se passait."

    "Tomas s'appuie contre l'établi pour reprendre son souffle. Kael reste près de la grille, comme s'il craignait de voir Ryn surgir derrière lui."

    tomas peur "J'ai essayé de lui faire lâcher prise, Kael aussi ! Il nous a repoussés comme si on existait même pas, et il a continué à la cogner contre les parois !"
    noam colere "Vous l'avez laissée là-bas ?! Elle est toujours avec lui ?"
    kael inquietude "On a dû reculer. Ryn était incontrôlable, Noam ! Il frappait tout ce qui s'approchait de lui, et dans un conduit aussi étroit, on pouvait même pas passer à côté pour récupérer Nyra."

    "Le bruit de notre conversation a attiré tout le monde près de l'établi. Elen abandonne la caisse sur laquelle elle venait de s'asseoir et se précipite vers nous."

    # Le groupe est toujours au complet dans la salle : aucun personnage ne disparaît.
    $ showGroup([
        ("julian", "inquiet", 0.075),
        ("elen", "peur", 0.195),
        ("mara", "stress", 0.315),
        ("sael", "mefiant", 0.435),
        ("tomas", "peur", 0.555),
        ("kael", "inquietude", 0.675),
        ("iris", "determine", 0.795),
        ("noam", "inquiet", 0.915),
    ])

    elen peur "Mais Nyra est blessée ? Est-ce qu'elle a réussi à s'échapper ?"
    tomas peur "Je sais pas ! On l'entendait encore quand on est partis, mais je sais pas dans quel état elle est maintenant !"
    julian inquiet "Attendez, attendez... Ryn nous a accompagnés jusqu'aux dortoirs sans aucun problème. Qu'est-ce qui a bien pu lui prendre d'un seul coup ?"
    sael mefiant "Il faut aller la chercher. Si elle s'est cogné la tête, on ne peut pas la laisser seule avec lui en attendant qu'il se calme."

    "Je regarde l'ouverture au-dessus de l'établi. Je connais le chemin jusqu'au dernier embranchement, mais je n'arrive pas à imaginer Ryn s'attaquer ainsi à Nyra, encore moins sans raison."
    "Iris me rejoint et attrape la lampe que j'avais posée près de la caisse. Son expression a changé : elle ne regarde plus le cadavre de Mara, mais le conduit d'où viennent d'arriver Tomas et Kael."

    iris determine "Noam, on va voir ce qui se passe. Mais cette fois, tu restes à côté de moi. Je veux pas qu'on se retrouve séparés dans ces couloirs."

    "Je récupère ma lampe, pendant que Sael referme rapidement sa trousse. Derrière nous, Mara demande à Kael de lui expliquer encore une fois ce qu'il a vu, mais je n'écoute déjà plus sa réponse."

    think "Nyra est peut-être encore là-bas, à quelques mètres de nous."

    "Je me dirige vers l'établi et lève les yeux vers l'ouverture."

    $ flashlight_off()
    stop music fadeout 1.0
    call end_day("27") from _call_j26_stay_end_day_27
    jump _27_0_1_1_0_0_REVEIL
