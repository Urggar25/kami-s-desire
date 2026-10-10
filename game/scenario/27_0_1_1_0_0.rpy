# =============================================================================
# JOUR 27 — LES TÉMOINS
# Route 0_1_1_0_0 — suite directe de l'expédition nocturne du jour 26.
# Nyra meurt ; Ryn accuse Tomas, tandis que Tomas, Kael et Elias accusent Ryn.
# Aucun personnage ne connaît la nature des individus qui leur ressemblent.
# =============================================================================

label _27_0_1_1_0_0_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Nuit"

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    $ flashlight_on(1)

    "Sael referme sa trousse si brusquement que plusieurs instruments s'entrechoquent. Elle en conserve un seul à la main, puis se tourne vers Tomas."

    $ showGroup([
        ("noam", "inquiet", 0.06),
        ("iris", "inquiet", 0.18),
        ("sael", "mefiant", 0.30),
        ("julian", "inquiet", 0.42),
        ("mara", "doute", 0.54),
        ("elen", "inquiet", 0.66),
        ("tomas", "peur", 0.78),
        ("kael", "inquiet", 0.90),
    ])

    sael mefiant "Où est-elle ? Dis-moi exactement où vous l'avez laissée."
    tomas peur "Au deuxième embranchement, après la plaque qui grince. On a voulu revenir la chercher, mais Ryn... Il nous laissait pas approcher."
    iris colere "Alors arrête de parler et montre-nous !"

    "Tomas ouvre la bouche, puis renonce à répondre. Il se hisse dans le conduit et nous indique de le suivre."
    "Iris me saisit le poignet avant que j'aie posé le pied sur l'établi. Elle me retient juste assez longtemps pour s'assurer que je la regarde."

    iris inquiet "Tu passes devant moi. Et tu m'attends aux embranchements, d'accord ?"
    noam inquiet "D'accord."

    "Nous nous engageons dans la ventilation presque en même temps. Julian aide Elen à franchir la grille ; elle lui demande d'arrêter de la tenir par le bras, puis s'excuse aussitôt sans se retourner."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play sound sfx_creak volume 0.35

    "Tomas avance rapidement malgré l'étroitesse du passage. Sael lui demande deux fois de ralentir : chaque mouvement trop brusque fait vibrer les plaques sous nos genoux."
    "Je garde une main sur le renfort le plus proche et l'autre autour de ma lampe. Derrière moi, Iris respire beaucoup trop vite."

    $ showGroup([
        ("tomas", "peur", 0.18),
        ("sael", "mefiant", 0.38),
        ("iris", "inquiet", 0.59),
        ("noam", "inquiet", 0.80),
    ])

    sael mefiant "Elle était consciente quand vous êtes partis ?"
    tomas peur "Je sais pas. Je l'ai appelée, elle a pas répondu. Kael m'a dit qu'il fallait aller vous chercher et j'ai... J'ai pas vérifié davantage."
    iris inquiet "Mais elle respirait ? Tomas, t'as regardé si elle respirait ?"
    tomas peur "J'EN SAIS RIEN !"

    "Il s'arrête au milieu du passage. Pendant quelques secondes, on n'entend plus que le frottement des vêtements contre la tôle."
    tomas inquiet "Pardon. Je voulais pas crier."

    "Nous repartons. Au détour d'un renfort, ma lampe accroche une trace sombre sur la paroi. J'avance encore, persuadé qu'il s'agit de rouille, jusqu'à ce que je distingue plusieurs empreintes de doigts."
    "Plus loin, le sang s'est insinué dans les joints et a coulé le long du métal. La quantité me fait ralentir malgré moi."

    think "Pas autant... Il peut pas y en avoir autant."

    "J'entends quelqu'un sangloter au bout du conduit. Ce n'est qu'en m'approchant que je reconnais Ryn."
    ryn peur "S'il te plaît... Nyra, regarde-moi. Juste une fois, putain..."

    "Je débouche dans une portion plus large du réseau."
    "Nyra est étendue sur le côté, une jambe repliée sous elle. Une large blessure lui ouvre l'arrière de la tête et son sang couvre le bas de la paroi contre laquelle elle repose."
    "Ryn est agenouillé à ses pieds. Il garde ses deux mains posées sur sa veste, mais lorsqu'il les soulève pour nous appeler, je vois qu'elles sont couvertes de sang jusqu'aux poignets."

    $ hideGroup()
    $ showGroup([
        ("ryn", "peur", 0.20),
        ("sael", "mefiant", 0.42),
        ("iris", "peur", 0.64),
        ("noam", "inquiet", 0.84),
    ])

    ryn peur "Sael ! Viens, vite ! Elle bouge plus, je comprends pas... Je lui parle depuis tout à l'heure et elle..."

    "Il s'écarte pour lui laisser de la place, mais revient aussitôt sur ses genoux, incapable de quitter Nyra des yeux."
    sael mefiant "Ryn, recule. Il faut que je puisse l'examiner."
    ryn peur "J'ai essayé de la mettre sur le dos, mais sa tête... J'ai vu le sang et j'ai arrêté. J'aurais peut-être dû la relever, non ?"

    "Sael ne lui répond pas. Elle prend le poignet de Nyra, cherche son pouls, puis recommence au niveau du cou."
    "Elen apparaît derrière nous. Sael se penche alors sur le visage de Nyra, et je vois ses épaules se raidir."

    elen peur "Sael ? Elle a quoi ? Pourquoi tu lui fais pas quelque chose ?"
    "Sael approche son oreille de la bouche de Nyra, puis se redresse et vérifie ses yeux à la lumière de la lampe."
    elen peur "SAEL ?!"

    "Sael reprend le pouls. Je la regarde déplacer ses doigts de quelques millimètres, comme si le problème venait simplement de l'endroit où elle les avait posés."
    "Enfin, elle retire sa main."

    sael fatigue "Je suis désolée..."
    elen peur "Non. Tu sais pas encore. Tu peux pas savoir si tu regardes même pas depuis deux minutes !"
    sael fatigue "Elen, elle ne respire plus. Sa blessure..."
    elen colere "Alors fais-la respirer ! C'est pour ça qu'on t'a demandé de venir !"

    "Elen essaie de passer entre Iris et moi. Julian la retient pour l'empêcher de heurter Sael, mais elle se retourne contre lui avec une violence qui nous surprend tous."
    elen colere "LÂCHE-MOI !"

    "Elle lui frappe l'avant-bras, puis s'immobilise en voyant qu'il n'essaie même plus de la retenir."
    "Julian a le teint livide. Il fixe la blessure de Nyra sans paraître comprendre pourquoi Elen lui crie dessus."

    julian inquiet "Je... Je voulais pas..."
    elen peur "On peut la sortir d'ici ! À l'infirmerie, y a des machines, non ? On peut pas juste la laisser comme ça !"

    "Sael ouvre sa trousse une nouvelle fois. Elle en sort un instrument, le garde quelques secondes au-dessus de ses genoux, puis le repose exactement à l'endroit où il était."
    sael fatigue "Je voudrais pouvoir la ramener. Mais elle est morte, Elen."

    "Elen recule d'un pas. Elle tourne la tête vers Julian, puis vers Iris, en attendant visiblement que l'un de nous contredise Sael."
    "Personne ne parle."

    elen peur "Mais... On a mangé ensemble hier. Elle m'a dit qu'elle voulait me montrer..."

    "Elle s'interrompt, cherche sa phrase et secoue la tête. Ses yeux se remplissent de larmes avant qu'elle réussisse à prononcer un autre mot."
    "Julian lui tend les bras ; cette fois, elle s'y jette en pleurant si fort qu'il doit se plaquer contre le mur pour garder l'équilibre."
    "Il passe une main derrière sa tête et la serre contre lui. Il regarde Sael par-dessus son épaule, les lèvres entrouvertes, sans trouver quoi lui demander."

    $ showGroup([
        ("elen", "peur", 0.12),
        ("julian", "inquiet", 0.27),
        ("mara", "triste", 0.42),
        ("ryn", "peur", 0.57),
        ("sael", "fatigue", 0.72),
        ("iris", "peur", 0.87),
        ("noam", "inquiet", 0.97),
    ])

    "Je remarque alors la lampe de Nyra, abandonnée contre son genou. Elle est encore allumée et éclaire le mur derrière elle, là où le sang s'est accumulé."
    "Je voudrais détourner le regard, mais je reste fixé sur ce faisceau inutile jusqu'à sentir Iris me serrer la main."

    think "Elle devait simplement arriver après nous. C'était le plan."

    "Ryn se remet à genoux près de Nyra et tente de prendre sa main. Sael l'arrête doucement avant qu'il la soulève."
    ryn peur "Non, attends... T'as pas compris. Elle parlait encore quand... Quand il..."
    "Il regarde la blessure. Les mots semblent lui échapper, et il se passe une main sur le visage, y laissant une traînée rouge."
    ryn peur "Nyra, allez... Me laisse pas là, s'il te plaît."

    "Mara rejoint Elen. Sans plaisanter, sans même demander la permission, elle lui pose une main dans le dos. Elen s'accroche à sa manche tout en continuant de pleurer contre Julian."

    sael fatigue "Ryn, je dois la couvrir. Il faut que tu me laisses un peu de place."
    ryn peur "Tu vas pas l'emmener maintenant ? Attends, j'ai même pas pu lui..."

    "Il se penche vers Nyra, et Tomas s'avance derrière nous."
    tomas inquiet "Ryn, laisse-la. Tu lui as déjà fait assez de mal."

    "Ryn se retourne d'un seul coup. Pendant un instant, je crois qu'il va se jeter sur Tomas."

    ryn colere "TOI !"
    ryn colere "T'oses encore ouvrir ta gueule ?!"

    "Il rampe vers lui, les poings serrés. Tomas recule, mais la paroi lui barre presque immédiatement le passage."
    "Iris et Kael s'interposent pendant que Sael protège le corps de Nyra."

    $ hideGroup()
    $ showGroup([
        ("ryn", "colere", 0.15),
        ("tomas", "peur", 0.31),
        ("kael", "inquiet", 0.47),
        ("iris", "colere", 0.63),
        ("noam", "inquiet", 0.79),
        ("sael", "fatigue", 0.95),
    ])

    ryn colere "C'est lui ! Je l'ai vu prendre Nyra par la tête ! Il l'a cognée contre le mur et... Je lui ai sauté dessus pour qu'il arrête !"
    tomas peur "C'est faux ! On t'a vu la frapper, Ryn ! Kael et moi, on a essayé de te retenir !"
    ryn colere "Menteur ! Regarde-la, putain ! REGARDE CE QUE T'AS FAIT !"
    kael inquiet "Ryn, recule. Je comprends que tu sois dans un état terrible, mais Tomas n'a rien fait à Nyra. On a essayé de vous séparer, tous les deux."

    "Ryn veut répondre, puis ses yeux reviennent vers le corps. Ses bras retombent et il se laisse glisser le long de la paroi."
    ryn peur "J'avais sa main... Elle bougeait encore. Pourquoi vous m'avez laissé avec elle si longtemps ?"

    "Tomas détourne les yeux. Kael se passe une main sur la nuque, incapable de rester tout à fait immobile."
    iris colere "Ça suffit ! Vous êtes sérieux, là ?! Elle est morte à deux mètres de vous, et tout ce que vous trouvez à faire, c'est de vous hurler dessus !"

    "Sa voix résonne dans le passage. Même Elen cesse de pleurer pendant une seconde avant de reprendre, le visage caché contre Julian."

    noam inquiet "Ryn, raconte-nous ce qui s'est passé, mais pas maintenant. Laisse Sael... Laisse-nous au moins sortir Nyra d'ici."
    ryn fatigue "Vous me croyez pas."

    "Il ne me regarde même pas."
    ryn fatigue "Je l'ai pas tuée, Noam. Je l'ai pas tuée..."

    "Sael recouvre doucement le visage de Nyra. Ryn tend le bras comme pour l'en empêcher, puis le retire avant de la toucher."

    "Je regarde autour de moi, à la recherche d'une lampe ou d'une autre couverture à lui passer. C'est alors que quelque chose me frappe."

    noam inquiet "Attendez... Elias et Lysa. Ils étaient dans le dernier groupe avec Ryn. Où est-ce qu'ils sont ?"

    "Julian relève la tête. Tomas et Kael échangent un regard, mais aucun des deux ne répond immédiatement."
    tomas inquiet "Je... Je les ai pas vus après les premiers cris. J'essayais d'atteindre Nyra et Ryn nous barrait le passage."
    kael inquiet "Ils étaient derrière nous quand on a quitté ta chambre. Après, je ne sais pas."
    elen peur "On a encore perdu quelqu'un ? Non... S'il vous plaît, dites-moi qu'ils sont juste repartis !"

    "Je dirige ma lampe vers le conduit vide. Il y a plusieurs embranchements sur le chemin du retour, et personne ne sait s'ils ont pu s'y engager."
    "Sael ferme sa trousse une seconde fois. Elle garde les yeux baissés sur la couverture qui recouvre Nyra."

    sael fatigue "Il faut la ramener. On cherchera les deux autres dès qu'on aura vérifié les dortoirs, mais je ne veux pas laisser son corps ici."
    julian inquiet "Je peux aider à la porter. Tu me montreras comment faire, parce que... Je voudrais pas lui faire encore mal."

    "Il s'arrête. Sael ne corrige pas ses mots et lui montre simplement comment maintenir la couverture pendant le trajet."
    "Elen refuse d'abord de s'écarter ; Mara lui parle tout bas jusqu'à ce qu'elle accepte de laisser passer le corps."

    "Ryn tend de nouveau les mains, prêt à aider. Kael les lui repousse, et son visage se ferme aussitôt."
    ryn colere "Me touche pas !"
    "Il regarde Nyra, puis baisse les bras en tremblant."
    ryn peur "Je voulais juste... D'accord. J'y touche pas."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve

    "Nous mettons beaucoup plus de temps à rentrer qu'à venir. La couverture accroche les renforts et, à chaque passage difficile, Julian demande à Sael de vérifier si Nyra est correctement soutenue."
    "Elen suit derrière eux avec Mara. Par moments, je l'entends respirer par petites secousses ; parfois, elle prononce le prénom de Nyra si doucement que j'ai du mal à savoir si elle parle aux autres."
    "Ryn ferme la marche sous la surveillance de Tomas et de Kael. Je ne les vois presque pas, mais leurs voix s'élèvent deux fois avant qu'Iris leur ordonne de se taire."

    "Lorsque la grille de ma chambre apparaît enfin, je suis soulagé d'une façon qui me fait aussitôt honte."

    $ flashlight_off()
    scene bg_chambre at adaptive_fullscreen with dissolve

    "J'atterris maladroitement sur l'établi. Iris me tend la trousse de Sael, puis se fige en regardant derrière mon lit."
    "Elias est debout près de la porte. Lysa, assise sur le matelas, serre un verre d'eau entre ses mains."

    $ showGroup([
        ("elias", "inquiet", 0.18),
        ("lysa", "inquiet", 0.40),
        ("iris", "inquiet", 0.62),
        ("noam", "inquiet", 0.84),
    ])

    noam surpris "Elias ? Lysa ? Mais vous étiez où ? On vous cherchait partout !"
    elias fatigue "On est revenus par l'autre côté. Quand ça a commencé à gueuler, j'ai embarqué Lysa, j'allais pas la laisser coincée là-dedans."
    lysa inquiet "J'ai rien compris. Il me tirait par le bras et j'entendais encore des coups derrière nous... Je lui ai dit d'attendre les autres, mais il a continué."

    "Une voix nous demande de dégager la sortie. Je m'écarte, et Elias remarque enfin la couverture que Sael et Julian font passer par la grille."
    elias inquiet "Qu'est-ce que... C'est Nyra ?"

    "Il regarde Julian, puis Sael. Aucun des deux ne lui répond tout de suite."
    sael fatigue "On doit la conduire à l'infirmerie."
    elias inquiet "Elle... Non. Attends, non, elle est pas..."
    sael fatigue "Elle est morte, Elias."

    "Lysa porte brusquement une main à sa bouche. Le verre lui échappe et tombe sur le sol, mais elle ne semble même pas l'entendre."
    lysa peur "Non... Quand on est partis, elle criait encore. Je l'ai entendue !"
    elias inquiet "Putain..."

    "Il recule jusqu'à la porte. Elen apparaît derrière le corps et, en apercevant Lysa, se précipite vers elle."
    "Elles s'étreignent si maladroitement qu'elles se cognent contre le bord du bureau. Lysa répète qu'elle ne savait pas, qu'elle croyait Nyra simplement blessée."
    "Je les laisse passer, tandis que Sael nous ordonne d'écarter les meubles pour dégager le chemin."

    $ hideGroup()
    $ showGroup([
        ("elias", "inquiet", 0.08),
        ("lysa", "peur", 0.20),
        ("elen", "peur", 0.32),
        ("julian", "inquiet", 0.44),
        ("mara", "triste", 0.56),
        ("tomas", "inquiet", 0.68),
        ("kael", "inquiet", 0.80),
        ("ryn", "peur", 0.92),
        ("iris", "inquiet", 0.98),
        ("noam", "inquiet", 0.99),
    ])

    "Lorsque Ryn sort à son tour, Elias se redresse. Il le fixe quelques secondes avant de détourner les yeux vers le sang sur sa veste."
    ryn peur "Elias... Dis-leur. T'étais derrière nous, t'as forcément vu Tomas !"

    "Elias reste silencieux assez longtemps pour que Ryn s'approche."
    elias fatigue "J'ai vu Nyra contre la paroi. Je t'ai vu la tenir, Ryn. Après, j'ai pris Lysa et je suis parti."
    ryn colere "C'est pas ce que je te demande ! Tomas l'a frappée avant ! Dis-leur ce qu'il a fait !"
    elias inquiet "Je peux pas dire ça. De là où j'étais, c'est toi que j'ai vu lui cogner la tête contre le mur."

    "Ryn ouvre la bouche, mais rien n'en sort. Il regarde Elias comme s'il ne reconnaissait plus sa voix."
    ryn peur "Non... Toi, au moins, tu..."
    "Il se tourne vers Lysa."
    ryn peur "Lysa. Toi, tu sais. T'as entendu, tu peux leur dire."
    lysa peur "J'ai entendu Nyra crier. Quand je me suis retournée, j'ai vu des gens se débattre, mais Elias m'a entraînée et... Je sais pas qui a commencé."
    ryn fatigue "D'accord... D'accord."

    "Il fait quelques pas en arrière, heurte la chaise et s'y laisse tomber. Je m'attendais à ce qu'il hurle de nouveau ; au lieu de ça, il fixe ses mains sales avec une expression qui me serre la gorge."
    "Elen n'a pas lâché Lysa. Tomas paraît vouloir ajouter quelque chose, puis se ravise en croisant le regard d'Iris."

    iris colere "On sort Nyra de cette chambre. Et personne ne règle ses comptes ici, vous m'entendez ? Personne !"

    "Sael et Julian passent devant. Mara vient les aider à franchir la porte, tandis qu'Elen suit derrière eux sans cesser de regarder la couverture."
    "Je m'attarde auprès de Ryn."
    noam inquiet "Viens avec nous. On va à l'infirmerie, et Sael pourra au moins te regarder les mains."
    ryn fatigue "Elles ont rien. C'est le sang de Nyra."
    "Il les contemple encore une seconde avant de se relever."

    $ hideGroup()
    $ current_period = "Matin"
    scene couloir_infirmerie at adaptive_fullscreen with dissolve

    "Quand nous atteignons l'infirmerie, la lumière du matin s'est déjà allumée dans les couloirs. J'ai l'impression qu'elle arrive beaucoup trop tôt."
    "Sael nous fait entrer, puis demande à Julian de l'aider à transporter Nyra dans une pièce séparée."

    scene bg_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Elen essaie de les suivre. Sael lui explique qu'elle doit d'abord nettoyer le corps, mais Elen secoue la tête avec obstination."

    $ showGroup([
        ("elen", "peur", 0.10),
        ("julian", "inquiet", 0.25),
        ("sael", "fatigue", 0.40),
        ("mara", "triste", 0.55),
        ("iris", "inquiet", 0.70),
        ("noam", "inquiet", 0.85),
    ])

    elen peur "Je vais pas la laisser toute seule. Hier encore elle... Sael, je veux juste rester à côté d'elle."
    sael fatigue "Je te laisserai la revoir, je te le promets. Donne-moi quelques minutes pour m'occuper d'elle."
    elen colere "Tu dis ça depuis tout à l'heure ! Quelques minutes pour quoi, maintenant ? Elle est morte !"

    "Sael baisse les yeux, sans protester. C'est Julian qui approche une chaise d'Elen et lui propose de s'asseoir."
    "Elle refuse, puis s'effondre dessus avant même qu'il ait terminé de la mettre en place."
    "Mara s'agenouille devant elle et lui prend les mains. Je n'entends pas ce qu'elle lui dit, mais Elen finit par cacher son visage contre son épaule."

    "Julian reste près de la porte par laquelle Nyra a disparu. Il a toujours du sang sur les manches et s'obstine à tirer dessus pour les cacher sous sa veste."
    julian inquiet "J'aurais dû lui parler davantage. Nyra venait parfois s'asseoir à notre table et je trouvais toujours quelque chose de plus important à raconter..."
    "Il s'arrête, gêné de s'entendre parler."
    julian fatigue "Pardon. C'est idiot."
    iris inquiet "Non, Julian."

    "Il hoche la tête, mais ses yeux se remplissent de larmes. Il s'éloigne vers le lavabo et commence à se laver les mains."
    "Je le vois frotter entre ses doigts jusqu'à ce que sa peau rougisse, alors qu'il n'y reste presque plus de sang."

    "De l'autre côté de la salle, Ryn attend debout, près de Tomas et Kael. Dès que Sael revient, il se dirige vers elle."

    ryn fatigue "Je peux la voir ? Juste... Avant que vous fassiez quoi que ce soit. Je veux lui parler."
    sael fatigue "Pas tout de suite. Laisse-moi finir, Ryn."
    ryn peur "Tu vas pas m'empêcher de lui dire au revoir, quand même ?"

    "Tomas s'approche."
    tomas inquiet "Je pense qu'il vaudrait mieux que Ryn reste à l'écart pour le moment."
    ryn colere "Tu vas me lâcher, oui ?!"

    "Elen relève la tête en entendant sa voix. Ses yeux se posent sur les vêtements ensanglantés de Ryn, puis elle se lève si vite que Mara n'a pas le temps de la retenir."
    elen colere "ARRÊTE DE HURLER !"
    "Ryn se fige."
    elen colere "On l'a ramenée ici parce qu'elle est morte, et toi tu passes ton temps à te battre avec Tomas ! Tu peux pas la laisser tranquille, juste une fois ?!"
    ryn peur "Elen... C'est pas moi qui..."
    elen peur "Je veux pas savoir ! Pas maintenant !"

    "Sa voix se brise. Elle essaie de reprendre sa phrase, n'y parvient pas et se rassoit en pleurant de plus belle."
    "Ryn fait un pas vers elle, mais Mara le regarde en secouant légèrement la tête. Il recule."

    "Je sens Iris chercher ma main. Elle la serre, sans commentaire."
    think "Ce matin, on était encore tous là."

    "Sael finit par demander à chacun de rester quelques instants dans la salle. Elle voudrait parler des événements et vérifier que personne d'autre n'a été blessé."
    "Sa voix est ferme, mais lorsqu'elle ramasse sa trousse, celle-ci lui échappe et tombe sur le sol. Elle reste un instant à fixer les instruments dispersés avant de s'agenouiller pour les récupérer."

    sael fatigue "Pardon... J'ai besoin d'une minute."

    "Personne ne bouge pour l'aider. Je crois que nous avons tous compris qu'elle préférait qu'on la laisse faire."

    $ current_period = "Après-midi"
    call show_custom_title("Quelques heures plus tard")

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    "Les heures ont passé sans que nous décidions vraiment quoi faire. Elen n'a presque pas bougé de sa chaise, et Julian revient régulièrement avec de l'eau qu'elle refuse de boire."
    "Sael a terminé de s'occuper de Nyra. Elle n'a pas voulu répondre aux questions sur les circonstances exactes de sa mort, seulement répété que la blessure était compatible avec plusieurs chocs violents."
    "Ryn est toujours dans la salle. Tomas et Kael restent à distance, mais le surveillent chaque fois qu'il se lève."

    $ hideGroup()
    $ showGroup([
        ("noam", "inquiet", 0.04),
        ("iris", "inquiet", 0.13),
        ("sael", "fatigue", 0.22),
        ("elen", "peur", 0.31),
        ("julian", "inquiet", 0.40),
        ("mara", "triste", 0.49),
        ("elias", "fatigue", 0.58),
        ("lysa", "inquiet", 0.67),
        ("tomas", "inquiet", 0.76),
        ("kael", "inquiet", 0.85),
        ("ryn", "fatigue", 0.94),
    ])

    tomas inquiet "On peut pas faire comme si rien ne s'était passé. Ryn ne peut pas repartir seul dans les dortoirs, pas après ce qu'on a vu."
    ryn colere "Après ce que VOUS racontez avoir vu ! C'est pas la même chose !"
    kael inquiet "Tu as essayé de nous sauter dessus deux fois depuis qu'on est revenus. Même ceux qui n'ont pas vu l'agression ont peur maintenant."

    "Ryn se tourne vers Elen. Elle baisse immédiatement les yeux, et je vois son visage changer lorsqu'il comprend qu'elle n'essaiera pas de le défendre."
    ryn fatigue "Tu as peur de moi, toi aussi ?"
    "Elen ferme les yeux. Julian pose une main sur le dossier de sa chaise, mais elle ne lui répond pas."

    sael fatigue "Je peux lui laisser une chambre ici. Il sera à l'écart, avec un lit et de quoi appeler si nécessaire. Je ne veux pas d'une punition improvisée, seulement éviter une autre bagarre."
    iris colere "Et qui décide qu'il doit être enfermé ? On n'a même pas réussi à comprendre ce qui s'est passé là-haut !"
    mara triste "Iris, personne n'est bien avec cette idée. Mais si Ryn s'emporte encore, on fait quoi ? On attend qu'il y ait quelqu'un d'autre par terre ?"

    "Iris serre les dents. Elle regarde Ryn, puis Elen, et finit par détourner les yeux."
    elias fatigue "Je peux bricoler des menottes à l'atelier, au cas où il essaierait de forcer la porte. Je dis pas qu'il faut lui mettre tout de suite, mais il vaut mieux avoir de quoi le retenir."

    "Ryn relève lentement la tête."
    ryn peur "Des... Tu veux me menotter ?"
    elias inquiet "Je veux éviter que quelqu'un soit blessé, Ryn."
    ryn colere "Mais c'est Tomas qui l'a tuée ! Et maintenant, c'est moi que vous voulez enfermer pendant qu'il se promène tranquillement ?!"

    "Il se lève. Elias tend un bras pour lui barrer le passage, mais Ryn le repousse d'un coup d'épaule. L'armoire derrière eux résonne sous le choc."
    "Julian abandonne son verre et vient aider Elias, tandis que Kael s'approche par l'autre côté."

    ryn colere "Me touchez pas ! Je veux sortir !"
    julian inquiet "Ryn, arrête ! Il y a Elen derrière nous, fais attention !"

    "Ryn essaie de passer entre eux. Dans le mouvement, Julian perd l'équilibre et heurte le bord d'un lit."
    "Je m'avance pour le retenir, puis attrape le bras de Ryn avant qu'il reparte vers la porte."

    noam determine "Ryn, stop ! Regarde ce que t'es en train de faire !"

    "Il se débat encore une seconde. En se retournant, il découvre que je le tiens moi aussi."
    "Il cesse immédiatement de tirer."
    ryn peur "Toi aussi, Noam ?"

    "Je desserre un peu ma prise, sans oser le lâcher."
    ryn peur "Putain... Tu crois vraiment que j'ai pu faire ça ?"

    "Il attend ma réponse. Je sens Julian reprendre appui derrière moi, mais je n'arrive plus à regarder autre chose que le visage de Ryn."
    noam inquiet "Je sais pas, Ryn. J'ai rien vu. Mais je veux pas qu'il arrive encore quelque chose à quelqu'un."
    ryn peur "J'ai rien fait à Nyra..."

    "Sa voix s'éteint. Il baisse la tête et se laisse ramener vers le lit."
    "Elias relâche son autre bras, puis recule jusqu'à la porte. Pour la première fois depuis notre retour, personne ne parle pendant plusieurs secondes."

    sael fatigue "Je vais ouvrir la chambre au fond du couloir. Ryn, tu pourras te laver et te reposer. On verra plus tard pour le reste."
    ryn fatigue "Je veux juste revoir Nyra."
    sael fatigue "Pas maintenant. Je te laisserai lui dire au revoir quand tout le monde se sera calmé."

    "Ryn lève les yeux vers elle, puis hoche la tête sans protester."
    "Il passe à côté de moi en évitant de me regarder. Je remarque qu'il garde les mains serrées contre son pantalon, comme s'il cherchait encore à dissimuler les taches de sang."

    "Sael l'accompagne dans une chambre isolée de l'infirmerie. Lorsque la porte se referme, j'entends le verrou s'enclencher."
    "Le bruit fait sursauter Elen. Elle se remet à pleurer, cette fois sans même essayer de le cacher."

    "Elias se tourne vers nous, puis vers la porte."
    elias fatigue "Je vais préparer les attaches. On les utilisera que si c'est nécessaire."
    iris colere "Tu feras surtout en sorte qu'elles restent sur une table tant qu'il ne cherche pas à sortir. Il vient de perdre Nyra lui aussi."
    "Elias ne discute pas. Il quitte la salle, suivi quelques instants plus tard par Kael."

    "Je m'assois près d'Iris. J'ai mal aux genoux et aux épaules, mais c'est seulement maintenant que je m'en rends compte."
    "Devant nous, Julian réussit enfin à faire boire quelques gorgées d'eau à Elen. Elle lui demande soudain si Nyra avait souffert. Il regarde Sael, complètement démuni."
    "Sael pose sa main sur celle d'Elen, sans lui promettre quoi que ce soit."

    $ current_period = "Soir"
    call show_custom_title("En début de soirée")

    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "La porte de Ryn est toujours verrouillée. Sael passe régulièrement le voir ; il refuse de manger, mais accepte l'eau qu'elle lui apporte."
    "Elias est revenu de l'atelier avec une paire de menottes artisanales. Il les a laissées à l'infirmerie sans les utiliser."
    "Julian et Elen ont accepté d'assurer une première garde dans le couloir. Julian a dû convaincre Elen de s'éloigner quelques minutes de la pièce où repose Nyra, et elle a fini par accepter à condition de rester à proximité."

    $ hideGroup()
    $ showGroup([
        ("iris", "fatigue", 0.37),
        ("noam", "fatigue", 0.64),
    ])

    "Iris s'adosse au mur près de moi. Ses yeux sont rouges et elle n'a presque rien mangé."
    iris fatigue "J'arrive pas à croire qu'on l'a laissée là-bas. Hier, elle était encore à table avec nous..."

    "Elle s'arrête et se frotte les yeux du revers de la main."
    noam fatigue "Moi non plus."

    "Iris regarde la porte de Ryn."
    iris inquiet "J'ai encore l'impression qu'il va sortir et nous expliquer que c'était une énorme erreur. Qu'on a mal compris quelque chose."
    noam reflexion "Il accuse Tomas. Tomas, Kael et Elias l'accusent. Lysa n'a pas vu le début... Ça ne nous dit pas ce qui est vrai."
    iris fatigue "Je sais. C'est bien ça qui me rend malade."

    "Elle se laisse glisser sur le banc du couloir et enfouit son visage dans ses mains."
    iris inquiet "J'ai eu peur de Ryn, tout à l'heure. Quand il s'est levé, j'ai pensé qu'il allait nous frapper nous aussi. Et maintenant, je me demande si on vient pas d'enfermer quelqu'un qui essayait simplement de défendre Nyra."

    "Je m'assois à côté d'elle."
    noam fatigue "Quand je l'ai attrapé, il m'a regardé comme si j'étais le dernier à pouvoir encore l'aider. Je savais même pas quoi lui dire."

    "Iris se tourne vers moi. Elle semble vouloir répondre, puis regarde le sol."
    iris fatigue "Je me souviens que Nyra m'avait demandé mon avis sur le prochain vote. J'étais pressée et je lui ai dit qu'on en parlerait demain."

    "Sa voix tremble. Elle attend quelques secondes avant de reprendre, sans relever la tête."
    iris peur "On était censés en parler demain, Noam."

    "Je pose une main sur son épaule. Elle ne me repousse pas."
    "Au bout du couloir, Julian entrouvre la porte pour demander quelque chose à Sael. Je reconnais la voix d'Elen derrière lui, étouffée par de nouveaux sanglots."

    "Je pense au corps de Mara, toujours caché derrière sa cloison. Personne n'a eu la force de reprendre l'enquête, et je n'en ai pas davantage envie ce soir."
    "Ce n'est pas seulement parce que je suis épuisé. Je n'arrive plus à regarder un autre représentant sans repenser à Nyra, à Ryn et aux trois récits qui ne peuvent pas être vrais en même temps."

    think "On devait simplement vérifier une photographie."

    "Iris se relève lorsque Sael nous appelle pour le changement de garde. Avant de rejoindre les autres, elle essuie ses joues et me tend la main pour m'aider à me lever."
    "Nous retournons vers l'infirmerie. Personne ne semble vouloir rentrer seul dans les dortoirs et, pour une fois, je préfère rester avec eux."

    stop music fadeout 1.2
    call end_day("28", sleeping=True) from _call_j27_stay_end_day_28
    jump _28_0_1_1_0_0_REVEIL
