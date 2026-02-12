# -----------------------------------------------------------------------
# LIENS — NYRA
# -----------------------------------------------------------------------

default nyra_link = 0

label NYRA_LINK_INTERACT:

    menu:
        "Passer du temps avec Nyra ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if nyra_link == 0:
        jump nyra_link_1
    elif nyra_link == 1:
        jump nyra_link_2
    elif nyra_link == 2:
        jump nyra_link_3
    elif nyra_link == 3:
        jump nyra_link_4
    elif nyra_link == 4:
        jump nyra_link_5

    if last_room_label:
        jump expression last_room_label
    return

label nyra_link_1:

    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("nyra", "sourire", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Nyra a vidé une boîte de pions de vote sur la table centrale."
    play sound sfx_paper
    "Elle les aligne en trois cercles parfaits, puis en casse un sans prévenir."
    noam "Tu fais quoi, exactement ?"
    nyra "J'analyse la partie."
    noam "On n'a pas encore de vote officiel aujourd'hui."
    nyra "Le vote commence bien avant la salle de vote."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Regarde : ici, les loyaux."
    nyra "Ici, les opportunistes."
    nyra "Et là, les blessés qui cherchent un camp où respirer."
    noam "Tu mets vraiment les gens dans des catégories comme ça ?"
    nyra "Je les mets dans des dynamiques, pas dans des boîtes."
    noam "Ça reste froid."
    nyra "Froid, oui. Faux, non."
    play sound sfx_beep
    "Une alarme lointaine pulse une fois dans les hauts-parleurs."
    noam "Tu as l'air presque... amusée."
    $ showP("nyra", "taquin", 0.70)
    nyra "Presque ? C'est vexant."
    nyra "Le Conclave est un jeu d'équilibre."
    nyra "Le poids bouge, les positions glissent, personne n'est stable longtemps."
    noam "Tu parles d'alliances."
    nyra "Évidemment."
    nyra "Une alliance durable, c'est rare."
    nyra "Une alliance utile, c'est quotidien."
    noam "Cynique."
    nyra "Pratique."
    "Nyra fait tourner un pion entre ses doigts, concentrée."
    nyra "Supposons que tu veuilles faire passer une proposition risquée."
    nyra "Tu ne la présentes pas quand tout le monde est lucide."
    noam "Tu attends la fatigue ?"
    nyra "La fatigue, ou la peur, ou la culpabilité."
    noam "Ça ressemble à de la manipulation."
    $ showP("nyra", "raison", 0.70)
    nyra "C'est de la stratégie sociale."
    noam "Donc le timing compte plus que le contenu ?"
    nyra "Non."
    nyra "Le contenu gagne la guerre."
    nyra "Le timing gagne la bataille qui permet d'arriver à la guerre."
    noam "Tu peux défendre une idée à laquelle tu ne crois pas ?"
    nyra "Si ça révèle qui ment, oui."
    nyra "Si ça force une fracture utile, oui."
    noam "Tu te rends compte que tu fais peur ?"
    $ showP("nyra", "sourire", 0.70)
    nyra "C'est souvent ce qu'on dit quand on ne veut pas répondre au fond."
    "Je m'assois en face d'elle."
    noam "D'accord."
    noam "Alors va au fond : c'est quoi ton plan aujourd'hui ?"
    nyra "Observer qui parle vite quand un nom est mentionné."
    nyra "Observer qui évite les yeux quand une faute est évoquée."
    nyra "Observer qui plaisante trop fort pour cacher un camp déjà choisi."
    play sound sfx_drop
    "Un pion tombe au sol. Nyra ne le ramasse pas."
    nyra "Tu sais ce que j'aime dans les systèmes fermés ?"
    noam "La pression ?"
    nyra "Les contraintes."
    nyra "Quand le cadre est serré, les gens montrent leur vraie logique."
    noam "Ou leur panique."
    nyra "Exactement."
    nyra "La panique est une logique aussi."
    $ showP("noam", "hesitation", 0.24)
    noam "Et moi, je suis où sur ton plateau ?"
    "Elle relève la tête, l'air sincèrement attentive."
    nyra "Toi ?"
    nyra "Tu es une variable qui refuse d'être un pion."
    noam "C'est un compliment ?"
    nyra "C'est un risque."
    noam "Tu souris en disant ça."
    nyra "Jouer sérieusement, c'est encore jouer."
    nyra "Et les meilleures parties sont celles où l'autre côté apprend vite."
    noam "Tu veux que j'apprenne vite ?"
    nyra "Je veux savoir si tu tiens quand le rythme accélère."
    "Elle pousse six pions vers moi."
    nyra "Va. Compose une majorité en trois mouvements."
    noam "Maintenant ?"
    nyra "Maintenant."
    noam "Et si j'échoue ?"
    $ showP("nyra", "taquin", 0.70)
    nyra "Alors tu auras appris quelque chose d'utile avant que ça coûte des vies."
    "Je prends un pion, hésite, puis en déplace deux autres."
    "Nyra observe mes mains plus que mes choix."
    noam "Tu juges quoi, là ?"
    nyra "Ton ordre de priorité."
    nyra "Qui tu protèges en premier."
    nyra "Qui tu es prêt à contrarier tout de suite."
    noam "Donc ce n'était pas un exercice de vote."
    nyra "Bien sûr que non."
    nyra "C'était un exercice de lecture."
    play sound sfx_announce
    "L'annonce de rassemblement grésille au plafond."
    nyra "Viens."
    nyra "La partie réelle reprend."

    $ nyra_link = 1
    jump FREE_TIME_END

label nyra_link_2:

    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    scene bg_stockage at adaptive_fullscreen

    $ showP("nyra", "taquin", 0.70)
    $ showP("noam", "hesitation", 0.24)

    "Nyra m'attend dans le stockage avec deux chaises face à face."
    "Entre elles : une fiche blanche et un stylet."
    noam "Ça ressemble à un interrogatoire."
    nyra "Plutôt à un test de stabilité."
    noam "Super."
    nyra "Assieds-toi."
    play sound sfx_paper
    "Elle pose la fiche entre nous avec un soin presque cérémoniel."
    nyra "Question une."
    nyra "Ton allié vole un badge pour ouvrir une infirmerie verrouillée."
    nyra "Tu le dénonces ?"
    noam "Ça dépend."
    nyra "Réponse interdite."
    noam "Pratique."
    $ showP("nyra", "sourire", 0.70)
    nyra "Question deux."
    nyra "Tu peux sauver dix inconnus ou un proche qui te trahira peut-être demain."
    nyra "Tu choisis quoi ?"
    noam "C'est quoi ce tribunal tordu ?"
    nyra "Un piège, comme prévu."
    noam "Tu l'assumes sans honte."
    nyra "Toujours."
    noam "Pourquoi ?"
    nyra "Parce que je teste ta position, pas ta rhétorique."
    noam "Tu veux une vérité instantanée."
    nyra "Je veux ton réflexe avant ton discours."
    "Je croise les bras."
    noam "Et si je refuse de jouer ?"
    nyra "C'est déjà une réponse."
    noam "Laquelle ?"
    nyra "Tu préfères garder le contrôle du cadre."
    noam "Évidemment."
    nyra "Intéressant."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Question trois."
    nyra "Tu apprends qu'une rumeur contre toi circule."
    nyra "Tu l'éteins en public..."
    nyra "...ou tu la laisses vivre pour repérer qui l'alimente ?"
    noam "Tu laisses vivre."
    nyra "Pourquoi ?"
    noam "Pour cartographier le réseau."
    nyra "Tu vois ?"
    nyra "Tu joues déjà."
    noam "Je m'adapte à toi, c'est différent."
    nyra "Les deux peuvent être vrais."
    play sound sfx_beep
    "Un bip sec coupe le silence, puis la lumière revient normale."
    noam "Tu fais ça à tout le monde ?"
    nyra "Non."
    noam "Pourquoi moi ?"
    nyra "Parce que tu bouges entre deux lignes."
    noam "Lesquelles ?"
    nyra "Principe et efficacité."
    noam "Et toi, tu es de quel côté ?"
    $ showP("nyra", "raison", 0.70)
    nyra "Du côté qui reste debout à la fin."
    noam "Réponse pratique, encore."
    nyra "Réponse honnête, surtout."
    noam "Question pour toi, alors."
    nyra "Vas-y."
    noam "Tu préfères un allié fiable ou un allié brillant ?"
    nyra "Fiable sous pression."
    noam "Tu n'hésites pas ?"
    nyra "Jamais sur ça."
    noam "Même s'il te ralentit ?"
    nyra "On compense la lenteur."
    nyra "On ne compense pas la trahison."
    "Elle pivote le stylet vers moi comme une lame offerte."
    nyra "Question quatre."
    nyra "Si je te demande maintenant qui tu sacrifierais en premier..."
    nyra "Tu réponds ?"
    noam "Non."
    nyra "Pourquoi ?"
    noam "Parce que tu observerais ma micro-seconde de retard sur chaque nom."
    $ showP("nyra", "rire", 0.70)
    nyra "Exact."
    nyra "Tu apprends vite, Noam."
    noam "Tu me rends parano."
    nyra "Bonne compétence dans cette station."
    noam "Tu prends du plaisir à ça ?"
    nyra "À mesurer la cohérence des gens, oui."
    nyra "À les humilier, non."
    noam "Parfois la frontière est mince."
    nyra "Alors je la surveille."
    $ showP("nyra", "neutre", 0.70)
    nyra "Question finale."
    nyra "Tu peux mentir une fois, parfaitement, pour empêcher une exécution."
    nyra "Tu mens ?"
    "Je prends une inspiration lente."
    noam "Oui."
    "Nyra ne répond pas tout de suite."
    nyra "Tu as répondu vite."
    noam "Tu cherchais ça ?"
    nyra "Je cherchais si tu t'accordais le droit de salir ton image pour un résultat concret."
    noam "Et ?"
    nyra "Et tu le fais."
    noam "C'est mal ?"
    nyra "C'est dangereux."
    nyra "Mais utilisable."
    noam "Tu parles comme si j'étais une pièce de ton jeu."
    nyra "On est tous des pièces de quelqu'un."
    nyra "La seule question, c'est : sur quel plateau ?"
    play sound sfx_drop
    "Elle plie la fiche vierge sans y écrire un mot."
    noam "Tu n'as rien noté."
    nyra "Je n'avais pas besoin."
    noam "Tu retiens tout ?"
    nyra "Seulement ce qui compte quand tout brûle."
    noam "Et mon score, alors ?"
    $ showP("nyra", "sourire", 0.70)
    nyra "Tu réfléchis avant de répondre, et tu assumes quand tu tranches."
    noam "Je déteste parler avec toi."
    nyra "C'est un excellent début."

    $ nyra_link = 2
    jump FREE_TIME_END

label nyra_link_3:

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("nyra", "raison", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Dans l'archive, Nyra a recouvert un tableau de notes en colonnes."
    "Commandements. Usages. Non-dits."
    noam "Tu montes une constitution parallèle ?"
    nyra "Je cartographie la règle implicite."
    noam "Singulier ?"
    nyra "Oui."
    nyra "Parce qu'elle change de masque, pas de nature."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Règle implicite numéro un :"
    nyra "Ne ridiculise jamais un pivot devant témoins."
    noam "Même s'il ment ?"
    nyra "Surtout s'il ment."
    nyra "Si tu l'humilies, ses soutiens se rigidifient."
    noam "Donc tu perds des voix sur l'ego."
    nyra "Exact."
    nyra "Numéro deux :"
    nyra "Toujours offrir une sortie honorable à l'opposant."
    noam "Même quand il mérite de tomber ?"
    nyra "S'il tombe sans sortie, ses alliés cherchent vengeance."
    noam "Tu penses en chaîne de conséquences."
    nyra "Toujours."
    play sound sfx_paper
    "Elle colle une nouvelle note : FORME > FOND (dans l'instant)."
    noam "Ça me dérange, cette phrase."
    nyra "Elle devrait."
    nyra "Mais elle est vraie dans une salle tendue."
    noam "Raison au fond, défaite sur la forme."
    nyra "Le scénario le plus fréquent."
    noam "Et numéro trois ?"
    nyra "Ne prends jamais la parole juste après une panique collective."
    noam "Pourquoi ?"
    nyra "Parce qu'on n'écoute pas un argument quand on cherche encore son souffle."
    noam "Donc il faut laisser retomber."
    nyra "Ou cadrer l'émotion avant de parler du fond."
    noam "Tu sais faire ça ?"
    $ showP("nyra", "taquin", 0.70)
    nyra "Je m'entraîne."
    noam "Numéro quatre ?"
    nyra "Si tu attaques, attaque une structure, pas une personne."
    noam "Ça protège les egos ?"
    nyra "Ça protège ta marge de négociation après."
    noam "Tu laisses toujours une porte ouverte."
    nyra "Une porte, une fenêtre, une trappe."
    noam "Et numéro cinq ?"
    nyra "Ne révèle pas toute ton information au premier échange."
    noam "Rétention stratégique."
    nyra "Séquençage stratégique."
    noam "C'est le même mot avec du parfum."
    nyra "Peut-être."
    "Je lis ses notes plus bas."
    noam "'Ne jamais corriger quelqu'un sur un détail quand il a raison sur le principal.'"
    noam "C'est toi qui as écrit ça ?"
    nyra "Oui."
    noam "Tu le fais rarement."
    nyra "Je sais."
    nyra "J'essaie de progresser."
    play sound sfx_beep
    "Un terminal de l'archive bippe et affiche une requête refusée."
    noam "Et les Commandements officiels ?"
    nyra "Ils cadrent le visible."
    nyra "Les règles invisibles cadrent le réel."
    noam "Tu n'as pas peur d'être cynique ?"
    nyra "J'ai peur d'être naïve."
    noam "Différence ?"
    nyra "Le cynique doute de tout."
    nyra "Le naïf doute trop tard."
    noam "Tu te places où ?"
    nyra "Entre les deux, les jours où je dors assez."
    $ showP("noam", "surpris", 0.24)
    noam "Tu dors ?"
    $ showP("nyra", "rire", 0.70)
    nyra "Par tranches tactiques."
    noam "Nyra..."
    noam "Si quelqu'un ignore toutes ces règles implicites, il est condamné ?"
    $ showP("nyra", "neutre", 0.70)
    nyra "Pas condamné."
    nyra "Mais vulnérable."
    nyra "Il pensera perdre sur ses idées..."
    nyra "...alors qu'il perdra sur sa manière d'exister dans la pièce."
    noam "Violent, comme constat."
    nyra "Précis."
    "Elle prend un marqueur rouge et encadre une phrase."
    nyra "'Voir l'invisible avant qu'il te coûte le visible.'"
    noam "Tu as un slogan maintenant ?"
    nyra "J'ai une méthode."
    noam "Et si je refuse ta méthode ?"
    nyra "Alors fabrique la tienne."
    nyra "Mais ne viens pas au Conclave sans carte."
    noam "Tu me donnes un cours de survie ou de domination ?"
    nyra "Les deux se recoupent souvent ici."
    noam "Tu crois qu'on peut jouer propre ?"
    nyra "Oui."
    nyra "Propre ne veut pas dire doux."
    noam "Tu as déjà perdu à cause d'une règle implicite ?"
    "Son sourire disparaît une seconde."
    nyra "Oui."
    nyra "J'avais raison, j'ai parlé au mauvais moment."
    nyra "Ils n'ont retenu que mon ton."
    noam "Et depuis ?"
    nyra "Depuis, je regarde le tempo avant la vérité."
    play sound sfx_drop
    "Le marqueur claque contre le tableau."
    nyra "Souviens-toi de ça."
    nyra "Ceux qui ne voient pas les règles invisibles..."
    nyra "...perdent sans comprendre quand ils ont commencé à perdre."

    $ nyra_link = 3
    jump FREE_TIME_END

label nyra_link_4:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("nyra", "surpris", 0.70)
    $ showP("noam", "surpris", 0.24)

    "La baie d'observation tremble sous une secousse sourde."
    play sound sfx_gresillement
    "Les lumières vacillent. Nyra, elle, sourit."
    noam "Tu souris vraiment ?"
    $ showP("nyra", "sourire", 0.70)
    nyra "Oui."
    noam "Pourquoi ça te plaît ?"
    nyra "Parce que la tension rend tout net."
    nyra "Plus de décor. Plus de posture."
    nyra "Seulement des décisions."
    noam "Tu appelles ça plaisant ?"
    nyra "Stimulant."
    noam "Tu as une drôle de définition du mot."
    nyra "Je sais."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Quand il n'y a aucun enjeu réel..."
    nyra "...je m'éteins."
    noam "Tu t'ennuies."
    nyra "En une journée."
    noam "En une heure, non ?"
    nyra "Probablement."
    "Une autre vibration secoue les vitres."
    noam "La plupart des gens paniquent dans ce contexte."
    nyra "La plupart des gens cherchent à éviter le risque."
    nyra "Moi, je cherche à le mesurer."
    noam "Nuance dangereuse."
    nyra "Toutes les bonnes nuances sont dangereuses."
    noam "Tu te rends compte que ça peut te consumer ?"
    nyra "Bien sûr."
    nyra "Mais sans ça, je me dissous."
    noam "Tu n'as pas de mode repos ?"
    nyra "Si."
    nyra "Je l'appelle 'préparation du prochain coup'."
    noam "Ce n'est pas du repos."
    $ showP("nyra", "rire", 0.70)
    nyra "C'est mon équivalent."
    play sound sfx_beep
    "Un signal d'intégrité structurelle passe en jaune."
    noam "Tu vois ce jaune ?"
    noam "Ça ne te dit pas d'arrêter de jouer ?"
    nyra "Au contraire."
    nyra "Ça me dit que chaque geste compte."
    noam "Et si tu te trompes ?"
    nyra "Alors j'apprends vite."
    noam "Et si l'erreur tue quelqu'un ?"
    "Elle se fige, puis répond sans détour."
    $ showP("nyra", "neutre", 0.70)
    nyra "Alors ce n'est plus un jeu."
    nyra "C'est une dette."
    noam "Tu les comptes, tes dettes ?"
    nyra "Toutes."
    noam "Tu n'en parles jamais."
    nyra "Parce que les annoncer ne les rembourse pas."
    "Le grondement s'éloigne lentement."
    noam "Tu as déjà cherché le risque juste pour sentir quelque chose ?"
    nyra "Oui."
    noam "Et ?"
    nyra "C'était idiot."
    nyra "Le risque pour le frisson seul, c'est une addiction sans stratégie."
    noam "Donc tu ne veux pas le danger, tu veux l'enjeu."
    nyra "Exactement."
    nyra "Je veux une situation où mes choix ont un poids réel."
    noam "Tu pourrais l'avoir autrement."
    nyra "Peut-être."
    nyra "Mais ici, l'enjeu est brut."
    nyra "Impossible à ignorer."
    $ showP("noam", "inquiet", 0.24)
    noam "Parfois je t'écoute et j'ai l'impression que tu cours au bord du vide volontairement."
    nyra "Je marche au bord."
    nyra "Courir, c'est gaspiller de l'information."
    noam "Tu intellectualises même la peur."
    nyra "C'est ma manière de la tenir."
    noam "Donc tu as peur, quand même."
    nyra "Évidemment."
    nyra "Je ne suis pas intrépide."
    nyra "Je suis fonctionnelle sous contrainte."
    noam "Belle formule."
    nyra "Merci."
    "Elle pose sa paume contre la vitre froide."
    nyra "Tu veux la vérité ?"
    noam "Toujours."
    nyra "Le calme absolu me terrifie plus que l'alarme."
    noam "Pourquoi ?"
    nyra "Parce que dans le calme absolu, j'entends tout ce que j'évite."
    noam "Comme quoi ?"
    nyra "Comme le vide entre deux objectifs."
    noam "Et tu le remplis avec des défis."
    nyra "Oui."
    noam "C'est durable ?"
    nyra "Aucune stratégie n'est durable sans révision."
    nyra "Mais c'est celle qui me tient debout aujourd'hui."
    play sound sfx_announce
    "Une annonce ordonne de rejoindre les secteurs sécurisés."
    noam "On y va."
    $ showP("nyra", "raison", 0.70)
    nyra "On y va."
    nyra "Et on verra qui garde une tête froide quand le sol bouge encore."
    noam "Tu transformes même une évacuation en test."
    nyra "Chaque moment l'est, qu'on le veuille ou non."
    noam "Tu ne coupes jamais ?"
    nyra "Je coupe quand c'est fini."
    nyra "Et ici, ce n'est jamais fini."

    $ nyra_link = 4
    jump FREE_TIME_END

label nyra_link_5:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("nyra", "triste", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "La salle du Conclave est vide pour une fois."
    "Nyra ne trie rien, ne note rien, ne joue avec aucun pion."
    noam "Tu as l'air ailleurs."
    nyra "Je peux te parler sans masque, cinq minutes ?"
    noam "Oui."
    "Elle inspire lentement, comme avant un saut."
    nyra "Je ne supporte pas l'idée d'être éliminée."
    noam "Éliminée du jeu ?"
    nyra "Du jeu, du groupe, de la mémoire des autres."
    noam "Tu as peur d'être oubliée."
    $ showP("nyra", "vide", 0.70)
    nyra "Oui."
    nyra "Plus que j'ai peur de me blesser."
    nyra "Plus que j'ai peur de perdre un débat."
    noam "Depuis quand ?"
    nyra "Depuis longtemps."
    nyra "Avant même le Conclave."
    noam "Tu peux m'expliquer ?"
    nyra "Chez moi, seuls les gagnants restaient dans les histoires."
    nyra "Les autres devenaient des notes de bas de page."
    noam "Et tu as juré de ne pas finir en note."
    nyra "Exact."
    play sound sfx_paper
    "Elle lisse une feuille invisible du plat de la main."
    nyra "Tu vois ma manie de tout cadrer ?"
    noam "Oui."
    nyra "Ce n'est pas juste de l'ambition."
    nyra "C'est une digue contre cette peur-là."
    noam "La peur de disparaître."
    nyra "La peur d'être remplaçable au point de ne laisser aucune trace."
    noam "Personne n'est totalement remplaçable."
    nyra "C'est gentil."
    nyra "Ce n'est pas ce que la station enseigne."
    $ showP("nyra", "reflexion", 0.70)
    nyra "Ici, si tu tombes, le système continue sans cligner."
    noam "Tu confonds le système et les gens."
    nyra "Peut-être."
    nyra "Mais quand la fatigue cogne, je ne vois plus la nuance."
    noam "Alors gagner, pour toi..."
    nyra "...ce n'est pas un caprice."
    nyra "C'est une nécessité."
    noam "Une nécessité pour vivre ?"
    nyra "Pour exister."
    "Le mot reste suspendu entre nous."
    noam "Tu crois vraiment que seule la victoire valide ton existence ?"
    nyra "Rationnellement, non."
    nyra "Émotionnellement... souvent, oui."
    noam "Tu as déjà envisagé d'être importante sans être première ?"
    nyra "Je l'essaie."
    nyra "Mais ma tête revient toujours au classement."
    noam "Et quand tu perds ?"
    nyra "Je rejoue la scène cent fois."
    nyra "Je découpe chaque seconde."
    nyra "Je cherche l'instant où j'aurais pu inverser."
    noam "Ça doit épuiser."
    nyra "Ça m'évite de ressentir le reste."
    noam "Le reste ?"
    nyra "La honte."
    nyra "Le vide."
    nyra "La sensation d'être de trop."
    $ showP("noam", "triste", 0.24)
    noam "Nyra..."
    nyra "Je sais."
    nyra "Ce n'est pas glorieux."
    noam "Ce n'est pas honteux non plus."
    nyra "On verra."
    play sound sfx_beep
    "Un bip doux confirme la fermeture des portes du secteur."
    noam "Tu n'as pas besoin d'être parfaite pour compter."
    nyra "Dis ça au tableau des éliminés."
    noam "Je le dis à toi, maintenant."
    "Elle détourne les yeux, puis revient à moi."
    $ showP("nyra", "triste", 0.70)
    nyra "Tu sais ce qui me terrifie exactement ?"
    noam "Dis-moi."
    nyra "Que le jour où je sors, les autres reprennent leur rythme en deux heures."
    nyra "Que ma place se referme comme de l'eau."
    noam "Tu crois que l'impact se mesure à la durée du manque."
    nyra "Oui."
    noam "Et si l'impact se mesure aussi à ce que tu changes chez les gens ?"
    nyra "Alors je dois changer quelque chose de réel."
    noam "Tu le fais déjà."
    nyra "Parfois pour le pire."
    noam "Parfois pour le mieux."
    nyra "Je préfère 'parfois de manière décisive'."
    noam "Ça, c'est bien toi."
    $ showP("nyra", "sourire", 0.70)
    nyra "Désolée."
    noam "Pourquoi ?"
    nyra "Pour la version de moi qui transforme tout en partie."
    noam "Elle te protège."
    nyra "Elle m'isole aussi."
    noam "On peut travailler le premier sans nourrir le second."
    nyra "Tu parles comme un coach."
    noam "Je m'adapte à mon adversaire préféré."
    nyra "Adversaire ?"
    noam "Partenaire de duel, alors."
    nyra "Mieux."
    "Elle redresse les épaules, moins tendue."
    $ showP("nyra", "raison", 0.70)
    nyra "D'accord."
    nyra "Je continue de jouer pour gagner."
    nyra "Mais j'essaie de ne plus confondre défaite et disparition."
    noam "C'est déjà énorme."
    nyra "Ne t'emballe pas."
    nyra "Je rechuterai sûrement au prochain vote."
    noam "Alors je te le rappellerai."
    nyra "Marché conclu."
    play sound sfx_announce
    "L'annonce d'ouverture de séance retentit, nette."
    nyra "On y va."
    nyra "Cette fois, je joue pour gagner..."
    nyra "...et pour rester humaine au passage."

    $ nyra_link = 5
    jump FREE_TIME_END
