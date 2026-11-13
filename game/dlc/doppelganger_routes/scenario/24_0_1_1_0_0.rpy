default j24_vital_vote = None
default j24_tomas_convinced = False
default j24_production_inquiry = False


label _24_0_1_1_0_0_REVEIL:

    $ current_day = 24
    $ day_id = 24
    $ j24_production_inquiry = False
    $ current_period = "Matin"

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    $ blink()

    "Je me réveille avec la lumière de ma chambre encore allumée et la joue écrasée contre l'oreiller, dans une position suffisamment inconfortable pour me faire comprendre que je n'ai presque pas bougé de la nuit."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Pendant quelques secondes, je reste allongé à fixer le plafond sans vraiment penser à quoi que ce soit, puis mon regard descend presque automatiquement vers la grille d'aération."

    "Le bureau est toujours poussé devant."

    think "Bon... Au moins, personne n'a essayé de sortir de là cette nuit."

    "C'est une pensée parfaitement normale à avoir au réveil."

    "Je soupire et me redresse, encore engourdi. Ma tablette est restée allumée sur la table de chevet, avec le compte rendu de Sael ouvert exactement là où je l'avais abandonné hier soir."

    "Réflexes normaux, mémoire normale, perception normale, aucune anomalie visible à l'imagerie."

    think "Donc officiellement, tout va merveilleusement bien dans ma tête."

    "Je referme le document avant d'avoir la mauvaise idée de le relire une quatrième fois."

    "Aujourd'hui, au moins, je devrais avoir autre chose à faire que d'essayer de comprendre si j'ai réellement vu Mara morte ou si mon cerveau a décidé de me faire vivre la pire blague de l'histoire."

    "Le vote annoncé il y a deux jours doit avoir lieu cet après-midi."

    think "Un toit où dormir, de l'eau potable et suffisamment à manger."

    "Sur le papier, c'est probablement le vote le plus simple qu'on nous ait proposé depuis notre arrivée."

    think "Donc avec notre talent, on devrait réussir à transformer ça en catastrophe avant midi."

    "Je me lève, enfile mes vêtements et m'approche du bureau pour le remettre à sa place, mais ma main reste quelques secondes sur le dossier de la chaise."

    "Je finis par ne déplacer le meuble que de quelques centimètres, juste assez pour pouvoir prétendre à moi-même que j'ai fait un effort."

    noam fatigue "C'est déjà ça."

    "Je récupère mon téléphone et quitte la chambre."

    stop music fadeout 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_j24_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le dortoir est beaucoup plus animé que les jours précédents. Une porte est ouverte au bout du couloir, j'entends quelqu'un rire derrière une autre et, quelque part vers la cafétéria, Elen parle suffisamment fort pour être parfaitement identifiable sans même comprendre ce qu'elle raconte."

    think "Bizarrement, ça fait du bien."

    "Je prends la direction de la cafétéria sans traîner davantage."

    jump _24_0_1_1_0_0_PETIT_DEJEUNER


label _24_0_1_1_0_0_PETIT_DEJEUNER:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j24_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "Quand j'entre, presque tout le monde est déjà installé. La conversation traverse la pièce dans tous les sens et, pour une fois, personne ne semble parler à voix basse comme s'il craignait qu'un mot de travers fasse exploser la station."

    $ showGroup([
        ("julian", "joie", -0.08),
        ("elen", "content", 0.04),
        ("lysa", "blase", 0.16),
        ("tomas", "reflexion", 0.28),
        ("nyra", "neutre", 0.40),
        ("ryn", "neutre", 0.52),
        ("sael", "neutre", 0.64),
        ("mara", "taquin", 0.76),
        ("elias", "fatigue", 0.88),
        ("iris", "fatigue", 1.00),
        ("kael", "calme", 1.12),
        ("noam", "neutre", 1.22),
    ])

    elen joie "Noam ! Viens, on était justement en train de parler du vote !"

    noam reflexion "Vous avez commencé sans moi ?"

    iris blase "On a surtout commencé à manger sans toi. Tu sais, le monde continue de tourner, tu n'es pas central à toutes nos discussions."

    mara taquin "Personnellement, je voulais attendre. Je trouve ça important de partager les moments de plaisir."

    iris agace "Elle parle du petit-déjeuner. Enfin... j'espère."

    mara rire "Pour une fois, oui."

    "Je récupère un plateau pendant que Julian se redresse sur sa chaise avec l'air d'un candidat sur le point de prononcer son discours de victoire."

    julian joie "Mon cher Noam, tu arrives au meilleur moment. Nous étions précisément en train de constater que, pour une fois, l'humanité avait réussi à nous proposer quelque chose sur lequel douze adultes raisonnables devraient pouvoir tomber d'accord."

    lysa blase "Onze adultes raisonnables et Julian."

    julian surpris "Je refuse cette attaque gratuite."

    lysa neutre "Elle était très peu coûteuse."

    ryn rire "Ça commence bien."

    "Je m'assois entre Iris et Elias pendant que Goumi dépose mon plateau devant moi."

    goumi "Bonjour Noam. Portion habituelle."

    noam sourire "Merci."

    elen content "Du coup, toi aussi t'es pour, hein ?"

    noam reflexion "Pour qu'on garantisse à tout le monde de l'eau potable, un toit et de quoi manger ?"

    elen joie "Oui !"

    noam taquin "Je sais pas, c'est assez radical."

    elen surpris "Hein ?"

    iris fatigue "Il plaisante."

    elen rire "Ah, ça me rassure !"

    noam sourire "Évidemment que je suis pour."

    ryn neutre "Voilà. Donc on est tous d'accord, on fait le vote et on passe à autre chose."

    sael raison "C'est le minimum pour vivre. Il ne devrait même pas y avoir besoin de voter pour ça."

    kael calme "Sur certaines stations d'Orbite, la question de l'eau suffit déjà à déterminer combien de personnes peuvent rester dans un habitat. Une garantie comme celle-là aurait un vrai effet."

    nyra raison "À condition qu'elle soit réellement appliquée, mais oui. Le principe est difficile à contester."

    elias neutre "Moi je vois même pas ce qu'on peut raconter pendant le débat. T'as faim, on te donne à bouffer. T'as soif, on te donne de l'eau. T'as nulle part où dormir, on te trouve un toit."

    mara taquin "Pour le toit, si jamais il manque de place, je suis prête à partager mon lit."

    iris blase "Personne n'est surpris."

    mara sourire "Après j'ai quand même mes standings ! Tout le monde ne peut pas venir, hein."

    julian sourire "Moi je trouve cette proposition extrêmement généreuse."

    mara taquin "Je savais que t'étais un homme de goût."

    elen rire "Arrêtez !"

    "La discussion continue quelques secondes dans la même ambiance, suffisamment légère pour que je commence presque à croire que Ryn avait raison et que le débat pourrait réellement être expédié sans drame."

    "Puis je remarque Tomas."

    "Depuis que je suis arrivé, il n'a pratiquement rien dit. Il garde les yeux fixés sur sa tablette et fait tourner sa cuillère dans une tasse qui, à en juger par le bruit du métal contre la céramique, est vide depuis un bon moment."

    noam reflexion "Tomas ?"

    tomas surpris "Hm ?"

    noam reflexion "On t'a perdu ?"

    tomas neutre "Non."

    noam taquin "Tu fais quand même une excellente imitation."

    "Il regarde sa tasse, semble seulement maintenant réaliser ce qu'il est en train de faire et pose sa cuillère."

    tomas fatigue "Je réfléchissais au vote."

    elen content "Bah t'es pour aussi, non ?"

    tomas neutre "Oui."

    "Sa réponse est immédiate, mais il retourne presque aussitôt vers sa tablette sans rien ajouter."

    noam taquin "T'as failli dire « techniquement ». J'ai vu tes lèvres bouger."
    tomas colere "J'ai rien dit !"
    elias rire "C'est vrai, il l'a pensé très fort."
    iris blase "Laissez-le avaler quelque chose, déjà."
    "Tomas essaye de boire. Sa tasse est vide."
    mara taquin "Et voilà. Même sa tasse est contre lui."
    tomas fatigue "Vous pouvez arrêter deux minutes ?"
    ryn desaccord "Bah parle alors ! Ça fait depuis ce matin que tu regardes ce texte comme s'il t'avait insulté."
    tomas stress "Parce que je suis POUR ! Mais..."
    "Il s'arrête. La salle entière attend la suite."
    julian sourire "Mesdames et messieurs, nous assistons à la naissance d'un « mais » historique."
    tomas colere "Julian, ferme-la !"
    elen inquiet "Tomas, t'as dormi combien de temps ?"
    tomas fatigue "Je sais pas. Pas assez."
    noam reflexion "Tu veux nous montrer ce qui bloque ?"
    tomas fatigue "Si je savais, je l'aurais déjà montré."
    sael raison "Alors mange et arrête de te torturer devant nous."
    tomas reflexion "C'est pas si simple."
    elen content "Je peux te faire un truc ! Un vrai petit-déjeuner."
    tomas inquiet "Non ! Enfin... merci. Mais non."
    "Il replie sa tablette, puis la rouvre aussitôt. Je commence à comprendre pourquoi il a l'air épuisé."
    tomas fatigue "Je vais aux archives. Il me manque quelque chose, j'en suis sûr."
    nyra raison "Si tu trouves, viens au débat avec des faits, pas juste une intuition."
    tomas neutre "Ouais."


    call play_stat_dialogue("j24") from _call_play_stat_dialogue_3

    ryn desaccord "Et si tu trouves rien ?"

    tomas fatigue "Alors j'aurai rien à présenter."

    ryn reflexion "Mais tu votes pour ?"

    tomas fatigue "J'ai dit que j'étais pour."

    "Il se lève, récupère son plateau et commence à partir."

    noam reflexion "Tomas."

    tomas fatigue "Quoi ?"

    noam taquin "Ta tablette."

    "Il s'arrête, regarde sa main vide puis revient la récupérer au milieu des sourires qu'une moitié de la table essaie très mal de cacher."

    mara taquin "Solide matinée."

    tomas colere "Mara..."

    mara rire "J'ai rien dit !"

    "Il quitte finalement la cafétéria."

    pause 0.5

    elen inquiet "Il est bizarre aujourd'hui."

    iris reflexion "Un peu."

    elias fatigue "Il est juste crevé."

    ryn neutre "Ouais, enfin il oublie sa tablette alors qu'il vient de dire qu'il va relire un texte dessus."

    nyra raison "La fatigue suffit largement à expliquer ça."

    lysa blase "Chez les Romains, on aurait probablement ouvert un poulet pour vérifier."

    iris fatigue "On ne va ouvrir personne."

    sael reflexion "Mamie disait qu'un esprit qui manque de sommeil ressemble à un feu qu'on laisse mourir : il chauffe encore, mais éclaire de moins en moins."

    mara taquin "Ta mamie avait vraiment une phrase pour tout."

    sael neutre "Oui."

    "Tout le monde semble accepter plus ou moins facilement l'explication de la fatigue."

    "Moi aussi, en théorie."

    think "En théorie."

    "Je repousse cette pensée presque aussitôt."

    think "Non. Pas aujourd'hui."

    "Je n'ai aucune envie de recommencer à analyser chaque geste étrange de chaque personne présente dans le Conclave."

    noam raison "On verra ce qu'il dit pendant le débat. S'il a une réserve, on l'écoute, et si elle tient pas debout, on lui répond."

    ryn neutre "T'as envie de passer deux heures là-dessus ?"

    noam taquin "Non."

    noam reflexion "Mais s'il est le seul à avoir un doute, autant éviter de lui gueuler dessus jusqu'à ce qu'il vote comme nous juste pour qu'on soit tranquilles."

    nyra raison "Ce serait effectivement une assez mauvaise manière d'obtenir l'unanimité."

    ryn agace "J'ai compris."

    elen content "De toute façon, ça va passer !"

    iris blase "Tu veux vraiment dire ça à voix haute ?"

    elen surpris "Pourquoi ?"

    iris fatigue "Laisse tomber."

    "La conversation repart progressivement vers d'autres sujets et, chose inhabituelle depuis plusieurs jours, je me retrouve à participer réellement au lieu de simplement écouter tout le monde en attendant que quelque chose tourne mal."

    think "Ça me manquait peut-être plus que je pensais."

    $ hideGroup()

    jump _24_0_1_1_0_0_ARCHIVES


label _24_0_1_1_0_0_ARCHIVES:
    call KD_ROUTE_J24_JULIAN from _call_optional_kd_route_j24_julian
    # Navigation libre vers l'objectif avant la scène scénarisée.
    call START_EXPLORATION_LIBRE("_24_0_1_1_0_0_ARCHIVES_ARRIVEE", title="Rejoindre les Archives", destination_room="archive") from _call_exploration__24_0_1_1_0_0_ARCHIVES

label _24_0_1_1_0_0_ARCHIVES_ARRIVEE:
    call KD_EXTRA_J24_LYSA from _call_kd_extra_j24_lysa

    $ current_period = "Matin"

    call show_custom_title("Un peu plus tard") from _call_show_custom_title_j24_1

    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Après le petit-déjeuner, je tourne quelques minutes dans les couloirs sans destination précise. Je pourrais retourner dans ma chambre, mais l'idée de rester seul avec le bureau, la grille et le rapport médical de Sael suffit à me faire continuer tout droit."

    think "Finalement, Tomas et son problème incompréhensible ont au moins l'avantage de m'occuper."

    "Je finis donc par prendre la direction des Archives."

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_j24_door_3
    scene bg_archive at adaptive_fullscreen with dissolve

    "Tomas est exactement là où je m'attendais à le trouver, penché devant l'écran principal avec plusieurs fenêtres ouvertes côte à côte."

    $ showGroup([
        ("tomas", "reflexion", 0.35),
        ("noam", "neutre", 0.65),
    ])

    noam reflexion "Alors ?"

    tomas surpris "Putain !"

    noam surpris "Je viens d'ouvrir une porte, Tomas."

    tomas fatigue "J'étais concentré."

    noam taquin "Ça aussi, j'avais deviné."

    "Je m'approche de l'écran. Trois documents presque identiques sont affichés côte à côte."

    noam reflexion "Pourquoi t'as trois fois le texte ?"

    tomas raison "Non, attends, c'est pas trois fois pareil. Là, c'est le texte déposé. Au milieu, celui que Kami a enregistré. Et le dernier, c'est moi qui l'ai recopié pour comparer. Enfin... pour vérifier les mots."

    noam reflexion "Et il y en a une ?"

    tomas neutre "Non."

    noam reflexion "Donc les trois sont identiques."

    tomas fatigue "Oui."

    noam taquin "C'était une manière très longue de répondre oui."

    tomas colere "Je sais."

    "Il ferme la copie qu'il a rédigée, hésite, puis la rouvre presque immédiatement."

    noam reflexion "Tu cherches quoi exactement ?"
    tomas fatigue "Je sais pas ! Tu vas me demander ça combien de fois ?"
    noam fatigue "D'accord. Mauvaise question."
    "Il pointe une ligne du texte, puis une autre. Son doigt tremble légèrement."
    tomas raison "Là. « Disposer ». Un puits à vingt kilomètres, c'est disposer d'eau ?"
    noam reflexion "Pas pour celui qui doit faire l'aller-retour."
    tomas reflexion "Voilà. Et pour manger ? « Suffisamment », ça veut dire quoi ? Assez pour tenir debout ?"
    noam taquin "Je connais au moins une personne qui mourrait si on rationnait les desserts."
    tomas colere "NOAM !"
    noam fatigue "Pardon."
    tomas fatigue "C'est pas le mot. Enfin si, le mot est mauvais, mais c'est pas ça..."
    "Il passe d'une fenêtre à l'autre. Trois exemplaires du même texte. J'ai envie de lui arracher la tablette des mains."
    noam agace "Tu fais trois fois le même travail."
    tomas reflexion "Parce que si je rate une différence..."
    noam fatigue "Il n'y en a pas. Tu me l'as dit."
    tomas colere "Tu comprends pas !"
    "Sa voix résonne dans les archives. Il s'immobilise aussitôt."
    tomas fatigue "Excuse-moi. J'ai dormi trois heures. J'arrive même plus à finir une idée."
    noam inquiet "Ça, j'avais remarqué."
    tomas neutre "Merci."
    noam reflexion "Écoute. On peut arrêter de relire la même phrase. Soit tu vas jusqu'au bout de ton doute, soit tu vas manger."
    tomas fatigue "Tu viens de me proposer deux choses que j'arrive pas à faire."
    noam sourire "Ouais. Je sais."
    "Il regarde les documents une dernière fois et finit par fermer l'un des trois."
    tomas reflexion "Bon. On essaie autrement."
    noam reflexion "Le texte te fait peur, ou ce que Kami pourrait en faire ?"
    tomas hesitation "Je... c'est peut-être la même chose."
    "Pour la première fois depuis mon arrivée, il ne cherche pas immédiatement à me corriger."


    menu (screen="critical_choice", noam_expr="reflexion", cc_targets={"On ne peut pas attendre un texte parfait.":{"label":"_24_0_1_1_0_0_ARCHIVES_PRINCIPE"},"Vérifions ce que Kami devra produire.":{"label":"_24_0_1_1_0_0_ARCHIVES_PRODUCTION"}}):
        "Que conseiller à Tomas ?"
        "On ne peut pas attendre un texte parfait.":
            $ j24_production_inquiry = False
            jump _24_0_1_1_0_0_ARCHIVES_PRINCIPE
        "Vérifions ce que Kami devra produire.":
            $ j24_production_inquiry = True
            jump _24_0_1_1_0_0_ARCHIVES_PRODUCTION

# Durée : choix majeur, environ 30 s.
label _24_0_1_1_0_0_ARCHIVES_PRINCIPE:
    noam raison "Bon. Tu vas le dire au débat."
    tomas surpris "Dire quoi ? « Bonjour, j'ai un problème dont j'ai oublié le nom » ?"
    noam taquin "Au moins ça changerait de Julian."
    tomas fatigue "J'aimerais surtout ne pas passer pour l'idiot qui bloque le vote."
    noam reflexion "Je peux t'aider à formuler ce que t'as trouvé."
    tomas colere "Tu veux encore m'expliquer ma propre question ?"
    noam agace "Non ! Mais tu me demandes de t'écouter depuis une heure et dès que je parle, tu me sautes dessus !"
    "Tomas me dévisage. J'ai envie de récupérer ma phrase et de la remettre dans ma bouche."
    noam fatigue "Pardon. Je suis aussi crevé que toi."
    tomas fatigue "Non. T'as raison. Je suis insupportable."
    noam taquin "Ça, je voulais pas le dire."
    "Il sourit enfin, très brièvement."
    tomas hesitation "Si je trouve une vraie raison de voter contre ?"
    noam reflexion "Alors explique-la. Mais faut que ce soit une raison, pas juste une peur."
    tomas reflechit "Tu me demandes beaucoup, là."
    noam raison "Je sais. Et si t'as besoin que je t'aide à parler, je le ferai."
    tomas fatigue "J'ai pas besoin d'une béquille."
    noam sourire "D'accord. Alors je reste à côté, juste au cas où."
    "Je me dirige vers la porte. Il ne me retient pas tout de suite."
    tomas hesitation "Noam."
    noam reflexion "Oui ?"
    tomas fatigue "Non. Rien."
    noam blase "Tu vas finir par me rendre dingue."
    "Il retourne à son écran. Cette fois, il ne cherche plus à répondre."


    "Je le laisse devant ses documents et quitte les Archives."

    $ hideGroup()

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Une fois la porte refermée, je reste quelques secondes dans le couloir en repensant à la conversation."

    think "Fatigué."

    "C'est probablement tout."

    think "Et contrairement à hier, je refuse de transformer le moindre comportement bizarre en affaire d'État."

    "Je reprends ma route."

    jump _24_0_1_1_0_0_AVANT_VOTE


label _24_0_1_1_0_0_ARCHIVES_PRODUCTION:
    $ current_period = "Matin"
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "neutre", 0.65)])
    noam reflexion "Attends. On regarde tout du mauvais côté."
    tomas surpris "Comment ça ?"
    noam raison "On cherche des pièges dans les mots. Mais elle doit bien avoir prévu comment donner à manger aux gens."
    tomas reflexion "Les stocks... ouais. On peut vérifier les projections."
    "Il ouvre un tableau rempli de chiffres et me laisse le regarder."
    noam fatigue "Pourquoi il manque autant de ressources ?"
    tomas raison "Parce qu'il faudrait augmenter la production. Je veux savoir où."
    "Il remonte rapidement une colonne, puis s'arrête net."
    tomas surpris "Oh."
    noam reflexion "Quoi, « oh » ?"
    "Une ligne apparaît en évidence sur l'écran."
    "KEYPER-IIB — STATION DE PRODUCTION"
    "UNITÉS ÉID-0 — QUOTAS À RÉVISER SI LE COMMANDEMENT EST ADOPTÉ"
    noam surpris "Keyper-IIB ? C'est où ?"
    tomas inquiet "Je... aucune idée."
    noam reflexion "Et ÉID-0 ?"
    tomas fatigue "Arrête de me poser la question exactement au moment où je me la pose !"
    "Il tente d'ouvrir le dossier. Accès refusé."
    tomas colere "Putain. Évidemment."
    noam raison "Des unités de production, c'est peut-être juste des machines."
    tomas reflexion "Peut-être. Mais pourquoi des quotas ? Et si c'est des gens ?"
    noam inquiet "T'as une raison de le penser ?"
    tomas fatigue "Non. Justement, j'ai RIEN. Et je vais devoir voter avec ça."
    "Il recommence à chercher. Je lui pousse sa tasse, vide depuis le matin."
    noam taquin "Tu veux au moins un verre d'eau ? Un vrai, avec quelque chose dedans."
    tomas fatigue "Ouais. Merci."
    "Il la regarde une seconde avant de revenir au dossier verrouillé."
    noam reflexion "On garde les références. On les ressortira si quelqu'un nous pose une question."
    tomas neutre "Je vais les noter. Je préfère qu'on ne les perde pas."


    "Tomas conserve une copie des chiffres. Je quitte les archives en le laissant devant sa tablette."
    $ hideGroup()
    jump _24_0_1_1_0_0_AVANT_VOTE

# Durée : environ 2m30.

label _24_0_1_1_0_0_AVANT_VOTE:

    call show_custom_title("Peu avant le vote") from _call_show_custom_title_j24_2

    $ current_period = "Après-midi"

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Une bonne partie du groupe s'est retrouvée dans la salle commune avant de rejoindre le Conclave. Julian et Elen ont lancé une partie de baby-foot, Ryn commente chaque action sans qu'on lui ait rien demandé et Iris essaie de lire sur le canapé en donnant l'impression qu'elle pourrait tuer quelqu'un si le niveau sonore augmente encore."

    $ showGroup([
        ("ryn", "sourire", 0.10),
        ("elen", "joie", 0.24),
        ("julian", "determine", 0.38),
        ("iris", "blase", 0.52),
        ("mara", "taquin", 0.66),
        ("nyra", "neutre", 0.80),
        ("noam", "sourire", 0.94),
    ])

    elen joie "BUT !"

    julian colere "Non ! Tu as fait tourner la barre !"

    elen rire "Bah oui, c'est le principe !"

    julian colere "Pas comme ça ! Il existe une éthique du baby-foot !"

    ryn rire "L'éthique dit surtout que t'es en train de te faire éclater."

    iris blase "J'aimerais rappeler qu'il existe aussi une notion appelée silence."

    mara taquin "Tu peux venir dans ma chambre si tu veux du calme."

    iris colere "Non désolée, t'es canon mais pas mon genre."

    mara sourire "Oh ! Quel dommage."

    "Je m'installe sur l'accoudoir du canapé en regardant Elen marquer un deuxième but pendant que Julian accuse cette fois la table d'être légèrement inclinée."

    nyra reflexion "Tu as vu Tomas ?"

    noam neutre "Oui."

    ryn reflexion "Et alors ?"

    noam reflexion "Il cherche toujours."

    ryn fatigue "Super."

    noam raison "Mais au moins, je crois que son problème concerne surtout la manière dont le Commandement pourra être interprété."

    nyra raison "Ça correspond à ce qu'il disait ce matin."

    ryn desaccord "Ça reste quand même un putain de toit et de la bouffe."

    noam neutre "Je sais."

    ryn reflexion "Tu penses qu'il peut voter contre ?"

    noam hesitation "Je sais pas."

    "Ryn abandonne immédiatement son sourire."

    ryn colere "Sérieusement ?"

    noam raison "Il n'a jamais dit qu'il voulait voter contre."

    ryn colere "Ouais, mais il est en train de chercher une raison depuis ce matin !"

    noam reflexion "Et alors ?"

    ryn surpris "Comment ça, et alors ?"

    noam raison "S'il trouve réellement un problème qu'aucun de nous n'a vu, je préfère qu'il nous le dise avant qu'on vote."

    ryn desaccord "Et s'il trouve rien mais qu'il reste bloqué sur son mauvais pressentiment ?"

    noam reflexion "Alors on discute avec lui."

    ryn fatigue "Tu crois vraiment que tu vas régler ça juste en discutant ?"

    noam taquin "C'est un concept assez novateur ici, je sais."

    "Nyra laisse échapper un petit rire."

    nyra raison "Il n'a pas tort."

    ryn agace "J'ai pas dit qu'il avait tort."

    iris blase "Tu prends juste exactement le ton de quelqu'un qui pense qu'il a tort."

    ryn colere "Je parle toujours comme ça !"

    iris neutre "Oui."

    "Je souris malgré moi."

    noam reflexion "Laissez-le parler pendant le débat. S'il n'arrive pas à expliquer ce qui lui pose problème, on lui posera les bonnes questions jusqu'à ce qu'on comprenne."

    nyra reflexion "Tu sembles déjà avoir décidé que tu allais t'en charger."

    noam surpris "Moi ?"

    iris blase "Non, Goumi."

    noam agace "Très drôle."

    iris sourire "T'as toujours fait ça."

    noam reflexion "Quoi ?"

    iris neutre "Quand deux personnes arrivent pas à se comprendre, tu reformules jusqu'à ce qu'elles réalisent qu'elles parlent presque de la même chose."

    noam taquin "Tu dis ça comme si c'était pathologique."

    iris blase "Ça l'est un peu."

    ryn sourire "Pour une fois, ça peut servir."

    noam agace "Merci pour la confiance."

    ryn taquin "De rien."

    "La remarque devrait probablement m'agacer davantage qu'elle ne le fait."

    "Depuis plusieurs jours, j'ai surtout l'impression de courir derrière des problèmes que je ne comprends pas, des souvenirs impossibles et des choses cachées dans les murs du Conclave. L'idée de devoir simplement écouter quelqu'un et essayer de comprendre son raisonnement paraît presque reposante."

    think "Ça, au moins, je sais faire."

    play sound sfx_announce

    "Le signal de Kami coupe la partie de baby-foot au moment où Julian allait annoncer sa remontée historique."

    iris fatigue "C'est l'heure."

    elen joie "On va gagner !"

    iris desaccord "Tu veux vraiment continuer à dire ça avant les votes ?"

    elen sourire "Oui."

    ryn rire "Laisse-la."

    $ hideGroup()

    jump _24_0_1_1_0_0_CONCLAVE


label _24_0_1_1_0_0_CONCLAVE:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_j24_door_4
    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.2

    "Lorsque nous arrivons dans la Salle du Conclave, Tomas est déjà installé et relit encore la proposition sur sa tablette. Tout le monde prend progressivement sa place, dans une ambiance presque détendue par rapport aux derniers votes."

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "blase", 0.25),
        ("julian", "sourire", 0.37),
        ("iris", "neutre", 0.49),
        ("tomas", "reflexion", 0.60),
        ("elen", "content", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "neutre", 1.08),
        ("sael", "neutre", 1.20),
    ])

    play sound sfx_announce
    stop music fadeout 0.5

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Mes chers représentants, nous voici déjà au vingt-quatrième jour."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Et j'ai le plaisir de constater que vous êtes tous encore là."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Enfin... On se comprends !"

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "La proposition soumise aujourd'hui est très simple."

    kami "Ajouter un nouveau Commandement garantissant à toute personne un toit où dormir, de l'eau potable et une alimentation suffisante."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "C'est mignon, non ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Après tout ce que vous avez déjà réussi à compliquer depuis votre arrivée, je suis véritablement curieuse de voir ce que vous allez faire de celui-ci."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Le débat est ouvert."

    hide screen kami_broadcast_ui
    stop music fadeout 0.6

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 1.0

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "blase", 0.25),
        ("julian", "sourire", 0.37),
        ("iris", "neutre", 0.49),
        ("tomas", "reflexion", 0.60),
        ("elen", "content", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "neutre", 1.08),
        ("sael", "neutre", 1.20),
    ])

    if j24_production_inquiry:
        jump _24_0_1_1_0_0_CONCLAVE_PRODUCTION_DEBAT

    julian sourire "Puisque notre chère Kami semble attendre un spectacle, je propose exceptionnellement de la décevoir et d'être tous d'accord en moins de cinq minutes."

    iris blase "Pour une fois, je soutiens ton plan."

    elen joie "Moi aussi ! Je vote pour, évidemment."

    ryn neutre "Pareil."

    sael raison "Il n'y a rien à discuter sur le principe. Personne ne devrait manquer de ces choses."

    nyra sourire "Tout le monde semble être d'accord."
    julian sourire "Voilà ! Une fois dans notre vie, nous pouvons faire quelque chose sans nous arracher la tête."
    elen joie "Je propose qu'on fête ça après !"
    iris blase "On n'a pas encore voté."
    elen surpris "Ah. Oui."
    mara taquin "Julian vient d'annoncer la victoire, donc préparez-vous au désastre."
    julian sourire "Je note votre manque de confiance. Il sera mentionné dans mes mémoires."
    lysa blase "Fais vite. À ce rythme, tu vas devoir écrire un tome par échec."
    "Tomas ne rit pas. Il relit la même ligne depuis tout à l'heure."

    "Tous les regards se dirigent finalement vers Tomas. Il garde encore quelques secondes les yeux fixés sur sa tablette avant de relever la tête."

    tomas neutre "Je suis favorable au texte."

    "Tomas prend quelques secondes avant de reprendre, comme s'il essayait encore de mettre de l'ordre dans un raisonnement qui lui échappe depuis le matin."

    tomas reflexion "Je ne remets pas en cause l'objectif du Commandement. Je veux que ce soit très clair avant qu'on commence."

    tomas raison "Personne ne devrait manquer d'eau, de nourriture ou d'un endroit où dormir. Là-dessus, je pense qu'on est tous d'accord."

    elen neutre "Oui."

    tomas reflexion "Ce qui me pose problème, c'est que le texte est extrêmement général et qu'en créant une obligation aussi large sans préciser ce qu'on entend exactement par accès, suffisance ou même logement..."

    "Il s'interrompt."

    ryn agace "Et ?"
    tomas inquiet "Et... j'ai pas terminé."
    elen inquiet "C'est à cause du mot « suffisamment » ?"
    tomas reflexion "Entre autres. Ça peut sembler ridicule, mais un mot comme ça..."
    iris blase "Non, Tomas. Personne n'a dit que c'était ridicule. Respire."
    mara taquin "Si tu prends une heure pour le mot « suffisamment », on va manquer d'eau avant le vote."
    tomas colere "Mara, c'est précisément ce que j'essaie d'éviter !"
    "Mara entrouvre la bouche, surprise. Pour une fois, Tomas ne lui laisse pas le temps de répondre."

    tomas colere "Attends !"

    "Tomas ferme les yeux quelques secondes."

    tomas reflexion "Je..."

    "Il rouvre les yeux vers sa tablette."

    tomas fatigue "Putain."

    noam inquiet "T'as perdu ton idée ?"

    tomas fatigue "Je l'avais."

    iris reflexion "Tu veux reprendre depuis le début ?"

    tomas colere "Non, je veux juste me souvenir de ce que j'étais en train de dire."

    "Son irritation monte rapidement, mais elle semble moins dirigée vers nous que contre lui-même."

    tomas reflexion "Le problème, c'est..."

    "Il fait défiler le texte et pointe une ligne."

    tomas raison "Si on considère qu'une personne « dispose » d'eau simplement parce qu'il existe un point d'eau quelque part dans sa région, est-ce que le Commandement est respecté ?"

    nyra raison "Probablement pas si l'accès est irréaliste."

    tomas reflexion "Probablement. Mais ce mot-là n'est pas dans le texte."

    kael calme "On ne peut pas tout préciser dans chaque Commandement."

    tomas raison "Je sais. C'est justement le problème avec les principes généraux : on laisse toujours une partie de l'application à l'autorité chargée de les faire respecter."

    ryn colere "Donc quoi ? On vote contre parce que le texte fait pas cinquante pages ?"

    tomas colere "J'ai pas dit ça !"

    ryn desaccord "Ça fait depuis ce matin que tu cherches une raison de pas voter pour."
    noam determine "Ryn, tu lui fais dire ce qu'il n'a pas dit. On va clarifier ça."
    call refutation_run("j24_tomas")
    if _return[0] == "success":
        call play_noam_interupt
        tomas fatigue "Merci. Je suis pour le principe. J'ai juste peur qu'on vote un texte vide."
    else:
        tomas colere "Je ne suis pas contre ! Je demande juste qu'on écoute ma réserve !" 

    tomas colere "Non ! J'essaie de comprendre si ma réserve est suffisamment importante pour qu'on la prenne en compte ! C'est pas la même chose !"

    ryn colere "Bah explique-la alors !"

    tomas colere "J'ESSAIE !"

    "Le ton claque suffisamment fort pour que toute la salle se taise."

    "Tomas s'en rend compte immédiatement et détourne les yeux."

    tomas fatigue "Désolé."

    noam raison "C'est rien."

    ryn neutre "..."

    noam agace "Bon, arrêtez de lui demander s'il est pour ! Il l'a dit trois fois."
    ryn colere "Et nous on attend quoi, exactement ?"
    tomas colere "J'en sais rien ! C'est ça qui me rend dingue !"
    noam reflexion "Attends... tout à l'heure, t'as parlé d'un puits à vingt kilomètres."
    tomas surpris "Hein ?"
    noam raison "Tu disais que Kami pouvait prétendre donner de l'eau à quelqu'un sans qu'il puisse réellement aller la chercher."
    elen inquiet "Mais elle ferait vraiment ça ?"
    iris desaccord "Elen, c'est Kami. Elle pourrait appeler une flaque « accès universel à l'eau » juste pour nous voir râler."
    tomas raison "Exactement ! On va peut-être lui offrir un moyen de dire que tout va bien alors que des gens crèvent encore."
    sael raison "Chez moi, une source qui reste inaccessible n'a jamais nourri personne."
    julian sourire "Épatant. Nous avons donc découvert que les mots peuvent mentir. Peut-on voter ?"
    tomas colere "Tu vois ? C'est pour ça que je voulais pas en parler !"
    noam agace "Julian, tu peux arrêter de faire le présentateur deux secondes ?"
    julian fatigue "Je... oui. Bon."
    "Tomas regarde ses mains. Il a l'air plus soulagé qu'heureux qu'on ait enfin compris."
    tomas fatigue "Je veux pas être celui qui aura laissé passer ça."
    noam reflexion "Ouais. Là, je comprends."


    noam reflexion "Si on refuse le texte aujourd'hui, qu'est-ce qu'on améliore ?"
    tomas reflexion "Rien. Mais si on l'accepte tel quel..."
    ryn desaccord "Attends. Chez moi, des gens ont même pas de quoi boire. Tu préfères qu'ils n'aient rien ?"
    tomas colere "J'AI PAS DIT ÇA !"
    noam fatigue "Ryn, laisse-le finir. S'il te plaît."
    ryn fatigue "Ouais, bon..."
    noam hesitation "J'aime pas non plus ce texte. Enfin... je l'aime bien, mais pas comme il est écrit."
    iris blase "C'est très clair, Noam."
    noam fatigue "Je sais. Je fais de mon mieux."
    tomas reflexion "Tu trouves aussi qu'il manque quelque chose ?"
    noam raison "Ouais. Sauf qu'on a pas de texte de remplacement. Et les gens qui ont faim aujourd'hui, ils attendent pas qu'on trouve le mot parfait."
    sael raison "Ça, je peux le comprendre. Mais une promesse vide peut faire plus de mal qu'une absence de promesse."
    elen inquiet "Et quelqu'un qui n'a pas mangé depuis hier, on lui dit quoi ? Qu'on recommence dans trois jours ?"
    "Sael ne répond pas tout de suite."
    tomas fatigue "Vous croyez que j'ai pas pensé à ces gens ?"
    noam agace "Personne dit ça. C'est justement pour eux que tu t'acharnes."
    nyra raison "On ne peut pas réécrire la proposition ici. C'est ce texte-là ou rien."
    julian neutre "Alors la question, c'est : ce rien, on en fait quoi ?"
    noam reflexion "Tomas... si Kami applique le Commandement au strict minimum, est-ce que ça aide quand même quelqu'un ?"
    tomas hesitation "Peut-être. Au moins ceux qui n'ont absolument rien."
    noam raison "Voilà. C'est ce qui me fait pencher pour."
    tomas reflexion "Et si dans une semaine on découvre qu'elle distribue juste de quoi survivre ?"
    noam fatigue "Alors tu pourras me le rappeler. Très fort, même. Je sais que tu sais faire."
    "Quelques rires nerveux passent autour de la table. Tomas, lui, ne sourit pas."
    noam hesitation "Je peux pas te promettre que ça se passera bien. Franchement, ça me fout la trouille."
    noam raison "Mais j'ai encore plus peur de dire non et de rentrer chez moi en sachant qu'on pouvait au moins leur donner ça."
    tomas fatigue "Tu sais que ça me rassure pas ?"
    noam sourire "Ouais. Moi non plus."
    "Tomas revient au texte. Cette fois, il le lit sans le faire défiler."


    tomas fatigue "C'est agaçant."

    noam surpris "Quoi ?"

    tomas fatigue "Ton raisonnement."

    noam taquin "Merci."

    tomas fatigue "C'était pas un compliment."

    noam sourire "Je prends quand même."

    "Il souffle et se frotte le front."

    tomas raison "Je maintiens que le texte est beaucoup trop vague et que j'aimerais sincèrement qu'on puisse préciser au moins ce qu'on entend par « suffisante »."

    noam neutre "D'accord."

    tomas raison "Et si dans une semaine on découvre que Kami considère qu'une ration ridicule remplit le Commandement, je veux que personne ne prétende qu'on n'avait pas vu le problème."

    nyra neutre "Ce sera noté."

    tomas reflexion "Mais..."

    "Il hésite encore, cette fois beaucoup moins longtemps."

    tomas neutre "Je ne vais pas m'opposer au texte."

    elen joie "Yes !"

    ryn sourire "Enfin."

    tomas colere "J'ai pas fini !"

    ryn neutre "Désolé."

    tomas raison "Je voterai pour."

    pause 0.5

    "Elen laisse échapper un petit cri de victoire tandis que Julian applaudit deux fois comme si nous venions de conclure un sommet diplomatique."

    julian sourire "Mesdames et messieurs, notre médiateur vient encore de sauver la civilisation."

    noam agace "J'ai rien sauvé du tout."

    nyra raison "Tu as identifié précisément ce qui bloquait la discussion."

    noam reflexion "J'ai juste reformulé ce qu'il disait."

    tomas neutre "Non."

    "Je tourne la tête vers lui."

    tomas raison "J'arrivais justement pas à le dire."

    pause 0.3

    tomas neutre "Donc... merci."

    noam surpris "Waouh."

    tomas fatigue "Commence pas."

    noam sourire "J'ai rien dit."

    ryn sourire "Pour une fois, t'as été utile."

    iris colere "Ryn !"

    ryn surpris "Quoi ?!"

    noam rire "Non, laisse."

    "Je me surprends moi-même à rire."

    ryn reflexion "Je voulais pas dire que t'étais inutile avant. Enfin..."

    iris blase "Arrête."

    ryn neutre "Ouais."

    "Autour de la table, la tension retombe d'un coup. Le vote n'a même pas encore commencé que tout le monde semble déjà considérer la question comme réglée."

    "Et moi, pendant quelques secondes, je reste simplement assis à regarder les autres reprendre leurs discussions."

    think "Utile."

    "Le mot me revient malgré moi."

    "Ces derniers jours, j'ai eu l'impression de devenir le type qu'on surveille, qu'on soigne, qu'on rassure ou qu'on empêche de faire une connerie."

    "Aujourd'hui, quelqu'un avait un problème qu'il n'arrivait pas à formuler et j'ai réussi à l'aider à le comprendre."

    think "Ça faisait longtemps."

    play sound sfx_announce

    "La voix de Kami revient avant que j'aie le temps de m'attarder davantage sur cette pensée."

    stop music fadeout 0.5

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Eh bien."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Voilà qui était presque constructif."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je commençais à oublier que vous en étiez capables."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Puisque Tomas semble finalement avoir retrouvé ses mots..."

    "Tomas lève les yeux vers l'écran."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Nous pouvons passer au vote."

    hide screen kami_broadcast_ui
    stop music fadeout 0.6

    jump _24_0_1_1_0_0_VOTE


label _24_0_1_1_0_0_CONCLAVE_PRODUCTION_DEBAT:
    julian sourire "Bon. Pour une fois, on peut être tous d'accord en moins de cinq minutes ?"
    elen joie "Oui !"
    ryn neutre "Pareil."
    tomas fatigue "Attendez."
    julian fatigue "Non..."
    tomas agace "Je peux juste finir une phrase ?"
    nyra raison "Vas-y."
    tomas reflexion "J'ai regardé les projections de production, ce matin. Avec Noam."
    noam neutre "On a trouvé une installation dont on avait jamais entendu parler."
    tomas raison "Keyper-IIB. Si ce Commandement passe, les quotas de certaines unités là-bas augmentent."
    elias surpris "Des unités de quoi ?"
    tomas fatigue "Je sais pas. C'est ça qui m'embête."
    nyra reflexion "Tu n'as pas réussi à ouvrir la fiche ?"
    tomas neutre "Non. Accès refusé."
    kael calme "Ça peut être une station automatisée."
    tomas raison "Oui. Mais on n'en sait rien."
    ryn agace "Donc on va tout bloquer parce qu'un tableau est pas assez détaillé ?"
    tomas colere "J'ai pas dit ça !"
    julian agace "Tu le sous-entends assez fort."
    tomas colere "J'essaie de comprendre comment elle va tenir sa promesse !"
    elen inquiet "Mais c'est quand même pour aider les gens..."
    tomas fatigue "Je sais, Elen."
    sael reflexion "Si les quotas concernent des travailleurs, il faudrait effectivement savoir dans quelles conditions."
    tomas raison "Voilà ! Merci."
    iris reflexion "Et s'il s'agit juste de machines ?"
    tomas fatigue "Alors j'aurai eu peur pour rien. Je l'espère, même."
    julian agace "Ça reste une hypothèse. Les gens qui ont faim, eux, c'est pas une hypothèse."
    noam raison "C'est moi qui lui ai demandé de vérifier. Ça vaut le coup qu'on l'écoute."
    julian colere "Et pendant qu'on écoute, qu'est-ce qu'on fait pour ceux qui attendent sur Terre ?!"
    tomas colere "Tu peux arrêter de me parler comme si je voulais les laisser crever ?!"
    ryn colere "Bah dis-nous ce que tu veux faire, alors !"
    tomas stress "J'EN SAIS RIEN !"
    "Il s'arrête, ferme les yeux et reprend plus bas."
    tomas fatigue "Si. Je sais que je veux pas voter pour un truc que j'ai même pas pu vérifier."
    nyra neutre "On ne pourra pas le vérifier aujourd'hui. Alors il faut choisir."
    elen inquiet "Tomas... tu vas voter contre ?"
    tomas hesitation "Je..."
    pause 0.4
    tomas fatigue "Oui."
    julian colere "Tu plaisantes ?!"
    tomas colere "Non !"
    julian colere "Tu sais ce que ça implique ?!"
    tomas stress "Oui, Julian ! Arrête de me le répéter !"
    noam agace "Julian, baisse d'un ton."
    julian colere "Et toi, Noam ! C'est toi qui l'as envoyé fouiller ces dossiers !"
    noam neutre "Je lui ai dit de regarder les conséquences. Pas de voter contre."
    tomas fatigue "C'est mon vote. Laissez Noam tranquille."
    elen inquiet "Tu pourrais peut-être juste t'abstenir..."
    tomas reflexion "Si je m'abstiens, le texte passe."
    elen neutre "Oui..."
    tomas fatigue "C'est justement pour ça que je vais voter contre. Désolé."
    mara agace "Bon, on a compris. On va se crier dessus jusqu'à demain ?"
    lysa blase "Julian a déjà pris de l'avance."
    julian colere "Très drôle."
    lysa neutre "Je rigolais pas."
    "Tomas fixe sa tablette. Il ne regarde plus personne, même quand Elen essaie de lui parler."
    play sound sfx_announce
    stop music fadeout 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Ah ! Voilà qui est nettement plus amusant."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous avez suffisamment parlé. Place au vote."
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    jump _24_0_1_1_0_0_VOTE

# Durée : environ 3m30.

label _24_0_1_1_0_0_VOTE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2

    "Le texte apparaît une dernière fois sur l'écran central tandis que le système ouvre les votes."

    "Toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    think "Après toute cette discussion, la phrase paraît presque ridiculement courte."

    "Tomas garde encore quelques secondes les yeux sur son interface avant de valider son choix. Les autres font de même et les pupitres s'éteignent progressivement autour de la table."

    "Cette fois, il ne reste plus que le mien."

    # Réutilise l'interface de vote commune aux autres débats.
    # Noam choisit POUR ou ABSTENTION ; dans l'autre route Tomas vote CONTRE.
    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None
    $ vote_phase3_amendment_override = "Toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    stop music fadeout 0.8

    $ _j24_vote_ui_result = renpy.call_screen("vote_screen", allowed_choices=("pour", "abstention"))

    if vote_phase3_player_choice == "pour":
        $ j24_vital_vote = "for"
    else:
        $ j24_vital_vote = "abstain"

    # Les onze autres représentants votent POUR.
    # Noam est ajouté avec le choix effectué dans l'interface.
    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None
    $ vote_phase3_results = [
        ("Ryn", "pour"),
        ("Julian", "pour"),
        ("Nyra", "pour"),
        ("Kael", "pour"),
        ("Mara", "pour"),
        ("Elias", "pour"),
        ("Lysa", "pour"),
        ("Iris", "pour"),
        ("Tomas", "contre" if j24_production_inquiry else "pour"),
        ("Elen", "pour"),
        ("Sael", "pour"),
        ("Noam", vote_phase3_player_choice if vote_phase3_player_choice in ("pour", "abstention") else "abstention"),
    ]
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    $ amendement_passe = (vote_phase3_counts["contre"] == 0)
    $ vote_phase3_amendment_override = None

    play music "music/bgm_fatal_assembly.mp3" fadein 0.8

    jump _24_0_1_1_0_0_RESULTAT


label _24_0_1_1_0_0_RESULTAT:
    if j24_production_inquiry:
        jump _24_0_1_1_0_0_RESULTAT_REJET

    stop music fadeout 0.5
    play sound sfx_announce

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    scene bg_diffusion_champagne at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    if j24_vital_vote == "for":

        kami "Douze voix pour."

        scene bg_diffusion_amour at adaptive_fullscreen with dissolve

        kami "Une unanimité parfaite."

        scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

        kami "Je dois reconnaître que vous me surprenez."

    else:

        kami "Onze voix pour."

        scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

        kami "Et une abstention."

        scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

        kami "Noam aime décidément beaucoup laisser une petite marge entre ses convictions et sa signature."

        think "Merci pour l'analyse."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Mais aucune voix contre."

    kami "Le nouveau Commandement est donc adopté."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "À compter de maintenant, toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Félicitations."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Aujourd'hui, vous avez réellement changé quelque chose."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Essayez de profiter de cette sensation avant votre prochain vote."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fallin_love.mp3" fadein 1.0

    $ showGroup([
        ("elias", "joie", -0.11),
        ("mara", "sourire", 0.01),
        ("noam", "sourire", 0.13),
        ("lysa", "neutre", 0.25),
        ("julian", "joie", 0.37),
        ("iris", "sourire", 0.49),
        ("tomas", "neutre", 0.60),
        ("elen", "joie", 0.72),
        ("kael", "sourire", 0.84),
        ("nyra", "neutre", 0.96),
        ("ryn", "sourire", 1.08),
        ("sael", "sourire", 1.20),
    ])

    elen joie "On l'a fait !"

    julian joie "Enfin une victoire qui ne nécessite pas d'expliquer pourquoi personne n'est mort !"

    iris blase "Tu avais vraiment besoin de préciser ça ?"

    julian sourire "Oui."

    ryn rire "Pour une fois, je suis d'accord avec lui."

    mara sourire "Putain, ça fait du bien quand ça se passe normalement."

    lysa blase "Ne prononce jamais cette phrase dans une histoire tragique."

    elen inquiet "Lysa !"

    lysa neutre "Je préviens."

    "Elen contourne la table avec suffisamment d'enthousiasme pour que je comprenne trop tard ce qu'elle prépare."

    noam inquiet "Elen, non."

    elen joie "Viens là !"

    $ hideGroup()
    $ unlock_gallery_image("bg_cg062")
    scene bg_cg062 at adaptive_fullscreen with dissolve

    "Elle m'attrape dans ses bras malgré ma tentative extrêmement convaincante de reculer d'environ dix centimètres."

    noam gene "Pourquoi moi ?!"

    elen rire "Parce que c'est toi qui as convaincu Tomas !"

    noam agace "Il était déjà pour !"

    tomas raison "Pas complètement."

    "Je tourne la tête vers lui."

    tomas neutre "Enfin... j'étais pour le principe, mais j'aurais pu m'abstenir ou refuser de valider le texte si j'avais continué à penser qu'on ignorait quelque chose d'important."

    noam reflexion "Donc tu admets que je t'ai convaincu ?"

    tomas fatigue "N'en profite pas."

    noam sourire "Je vais en profiter énormément."

    tomas fatigue "J'aurais dû me taire."

    julian sourire "Trop tard. Le héros du jour est désigné."

    noam colere "Arrêtez avec ça."

    nyra neutre "Tu l'as laissé parler quand plus personne voulait l'écouter. C'était pas gagné."
    noam taquin "Ça me fait une ligne sur mon CV ?"
    nyra sourire "Pas avant qu'on voie si le vote tient trois jours."
    noam fatigue "Merci pour la confiance."


    ryn sourire "En gros, t'as été utile."

    iris colere "Tu peux arrêter de dire ça comme s'il ne l'était jamais ?!"

    ryn surpris "Mais c'est pas ce que je veux dire !"

    iris agace "Alors apprends à parler."

    ryn colere "Vous me cassez les couilles..."

    noam rire "Ça va, Iris."

    "Elle tourne les yeux vers moi."

    noam sourire "Je prends le compliment."

    ryn reflexion "Merci."

    noam taquin "Profite, ça arrivera pas souvent."

    ryn rire "Connard."

    "Les discussions repartent progressivement tandis que tout le monde commence à quitter la salle."

    "Je reste encore quelques secondes assis, juste assez longtemps pour regarder le nouveau Commandement s'ajouter à la liste sur l'écran central."

    think "On a vraiment réussi."

    "Pas évité une catastrophe."

    "Pas limité les dégâts d'un mauvais choix."

    "Pas trouvé une manière de survivre à une règle de Kami."

    "Nous avons réellement ajouté quelque chose qui n'existait pas avant."

    "Et, pour une fois, j'ai le sentiment d'avoir participé autrement qu'en étant celui à qui les choses arrivent."

    $ hideGroup()

    jump _24_0_1_1_0_0_APRES_VOTE


label _24_0_1_1_0_0_RESULTAT_REJET:
    stop music fadeout 0.5
    play sound sfx_announce
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    if j24_vital_vote == "for":
        kami "Onze voix pour. Une voix contre."
    else:
        kami "Dix voix pour. Une abstention. Une voix contre."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Un seul vote contre, et c'est terminé. Vous adorez l'unanimité, n'est-ce pas ?"
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Le Commandement est rejeté. Rien ne change."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "C'est dommage. J'aurais adoré voir ce que vous alliez faire de cette jolie promesse."
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    $ showGroup([("tomas", "fatigue", 0.15), ("julian", "colere", 0.36), ("elen", "inquiet", 0.57), ("noam", "inquiet", 0.79)])
    elen inquiet "Non... C'est pas possible."
    julian colere "T'as vraiment fait ça."
    tomas fatigue "Ouais."
    julian colere "Onze personnes voulaient que les gens aient de quoi vivre !"
    tomas agace "J'ai pas voté pour les laisser mourir !"
    julian colere "Ah bon ? C'est exactement ce que tu viens de faire !"
    noam agace "Julian, ça suffit."
    julian colere "Non ! Il va quand même pas s'en tirer avec un « désolé » !"
    elen inquiet "Tomas, tu aurais pu..."
    tomas fatigue "Je suis désolé, Elen. Vraiment."
    julian agace "C'est tout ce que t'as à dire ?"
    tomas colere "Putain, tu veux que je te dise quoi ?!"
    pause 0.4
    tomas fatigue "Non. Laisse tomber. J'ai plus envie de parler."
    "Tomas récupère sa tablette et quitte la salle. Il ne se retourne pas."
    elen inquiet "Il faudrait peut-être aller le voir."
    noam fatigue "Laissez-lui un peu d'air. On reparlera demain."
    julian agace "On aurait dû reparler de tout ça avant qu'il vote."
    "Personne ne trouve quoi répondre."
    $ hideGroup()
    jump _24_0_1_1_0_0_SOIR_REJET

# Durée : environ 2m00.

label _24_0_1_1_0_0_SOIR_REJET:
    $ current_period = "Soir"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Tomas s'est enfermé dans sa chambre. Les autres se dispersent sans vraiment se dire au revoir."
    $ showGroup([("elen", "inquiet", 0.36), ("noam", "fatigue", 0.64)])
    elen inquiet "Il a même pas voulu que je lui apporte à manger."
    noam fatigue "Il a juste besoin de dormir."
    elen inquiet "Tu crois ?"
    noam neutre "Je crois, ouais."
    elen fatigue "Bon... Bonne nuit."
    noam neutre "Bonne nuit, Elen."
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je regarde un instant ma tablette. Le Commandement n'a pas été ajouté."
    think "Keyper-IIB..."
    "Je me demande si j'ai bien fait de pousser Tomas à fouiller ces archives. Je voulais juste qu'il comprenne ce qui le gênait."
    "Pour l'instant, il a surtout réussi à se mettre tout le monde à dos."
    "Je coupe la lumière sans avoir trouvé quoi lui dire demain."
    stop music fadeout 1.0
    call end_day("25", sleeping=True) from _call_j24_rejet_end_day_25
    jump _25_0_1_1_0_1_REVEIL

# Durée : environ 1m30.

label _24_0_1_1_0_0_APRES_VOTE:

    $ current_period = "Après-midi"

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Personne ne propose officiellement de célébrer le vote, mais une heure plus tard presque tout le monde est réuni dans la salle commune avec des boissons, quelques biscuits récupérés à la cafétéria et Julian qui a décrété qu'une victoire politique devait obligatoirement être suivie d'une victoire à la machine d'arcade."

    $ showGroup([
        ("mara", "rire", 0.12),
        ("julian", "colere", 0.28),
        ("elen", "rire", 0.44),
        ("ryn", "sourire", 0.60),
        ("iris", "sourire", 0.76),
        ("noam", "sourire", 0.92),
    ])

    julian colere "La manette a un problème !"

    elen rire "Elle avait aucun problème quand tu gagnais !"

    julian hesitation "Parce qu'elle s'est dégradée pendant la partie."

    ryn rire "Bien sûr."

    iris blase "Tu pourrais aussi envisager l'hypothèse révolutionnaire selon laquelle t'as juste perdu."

    julian colere "Je refuse cette interprétation."

    mara taquin "Tomas devrait vérifier la formulation."

    noam rire "Laissez-le tranquille."

    "La partie se poursuit et je profite enfin d'un moment où personne ne me demande de justifier quoi que ce soit."

    menu:
        "Passer un moment avec Julian et Elen.":
            $ showGroup([("julian", "determine", 0.25), ("elen", "joie", 0.50), ("noam", "sourire", 0.75)])
            julian determine "Noam ! Prends la deuxième manette. Elen refuse de reconnaître mon talent."
            elen rire "J'ai gagné trois fois !"
            noam taquin "Tu sais qu'un champion est censé gagner de temps en temps ?"
            julian "J'ai surtout un sens aigu du suspense."
            "Je m'installe entre eux. Julian perd encore une partie, puis insiste pour une revanche jusqu'à ce qu'Elen menace de débrancher la machine."
            elen joie "Tu vas raconter quoi sur Terre ? Que tu t'es fait battre par moi ?"
            julian sourire "Que j'ai généreusement offert la victoire pour célébrer notre vote."
            noam rire "Je raconterai la vraie version."
            julian "Traître. Tu viens de ruiner ma légende."

        "Échanger quelques mots avec Tomas et Nyra.":
            $ showGroup([("tomas", "reflexion", 0.25), ("nyra", "neutre", 0.50), ("noam", "neutre", 0.75)])
            "Tomas et Nyra ont quitté le canapé pour comparer leurs tablettes, malgré la fête."
            noam taquin "Vous avez vraiment décidé de travailler aujourd'hui ?"
            tomas "On essaie juste de comprendre comment expliquer le vote aux gens, sans leur promettre davantage que ce qu'il change."
            nyra raison "Je lui ai dit d'attendre demain pour rédiger son discours."
            tomas inquiet "Ça ne sera pas un discours. Juste un compte rendu."
            noam sourire "On vient de gagner. Vous pouvez poser vos tablettes dix minutes."
            "Nyra éteint immédiatement la sienne. Tomas la regarde, hésite, puis l'imite."
            nyra taquin "Voilà. C'était assez simple, finalement."
            tomas sourire "J'espère que tu n'as pas l'intention de noter cette conversation dans le compte rendu."

        "Retrouver Lysa à l'écart.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "sourire", 0.65)])
            "Lysa s'est installée près du distributeur, assez loin pour échapper aux cris de Julian."
            noam sourire "Tu ne joues pas ?"
            lysa blase "Je préfère regarder le naufrage à une distance raisonnable."
            noam "On dirait quand même que tu t'amuses."
            lysa taquin "Ne répète pas ça. J'ai une réputation."
            "Elle pousse vers moi un gobelet qu'elle n'a pas touché."
            lysa neutre "Tiens. J'en ai pris deux sans faire attention."
            noam taquin "Tu m'offres un verre ? Ça va être noté dans les archives."
            lysa blase "Continue et je le reprends."
            "Nous restons un moment à écouter les protestations de Julian. Pour une fois, Lysa ne cherche pas à remplir le silence."

    $ hideGroup()

    "Je ris avec les autres sans avoir besoin de me forcer, ce qui m'arrive suffisamment peu ces derniers jours pour que je le remarque immédiatement."

    "Pendant un moment, le Conclave ressemble presque à ce qu'il aurait dû être dès le départ : douze personnes qui viennent de prendre une décision ensemble et qui peuvent passer une heure à se moquer du mauvais perdant de service sans penser à ce qu'il y a derrière les murs."

    julian determine "Revanche."

    elen joie "Quand tu veux !"

    iris fatigue "Vous allez y passer l'après-midi."

    elen rire "Oui !"

    "Iris finit par quitter le canapé pour venir s'asseoir près de moi."

    iris sourire "Ça faisait longtemps."

    noam reflexion "Quoi ?"

    iris neutre "Que je t'avais pas vu comme ça."

    noam surpris "Comme quoi ?"

    iris agace "Normal."

    noam taquin "Ça fait plaisir."

    iris blase "Tu sais ce que je veux dire."

    "Je regarde Julian recommencer sa partie avec Elen sous les commentaires de Ryn."

    noam reflexion "Ouais."

    iris sourire "T'avais l'air bien pendant le débat."

    noam taquin "Je pensais qu'on jugeait les arguments, pas la prestation."

    iris agace "Arrête deux secondes."

    noam sourire "D'accord."

    iris reflexion "Depuis plusieurs jours, t'es toujours en train de courir après un truc, de te demander si t'as oublié quelque chose ou si t'as vu quelque chose que personne d'autre a vu."

    "Son ton reste léger, mais suffisamment précis pour faire disparaître une partie de mon sourire."

    iris neutre "Aujourd'hui, t'étais juste... toi."

    noam reflexion "C'est censé être rassurant ?"

    iris sourire "Un peu."

    "Je baisse les yeux vers ma boisson."

    noam reflexion "Ça m'avait manqué."

    iris surpris "Quoi ?"

    noam neutre "Avoir un problème que je peux comprendre."

    "Je cherche mes mots quelques secondes."

    noam reflexion "Tomas n'arrivait pas à expliquer ce qui le bloquait, mais au moins il y avait quelque chose à comprendre. Je pouvais l'écouter, lui poser des questions et essayer de trouver où ça coinçait."

    noam fatigue "C'est quand même plus simple que de se demander si son propre cerveau invente des cadavres."

    iris fatigue "La comparaison aide beaucoup."

    noam sourire "Je trouve aussi."

    iris reflexion "Et tu l'as aidé."

    noam neutre "Ouais."

    iris sourire "Donc profite un peu au lieu de chercher immédiatement pourquoi ça va forcément mal finir."

    "Je tourne la tête vers elle."

    noam taquin "Tu me connais beaucoup trop bien."

    iris blase "Malheureusement."

    "Elle me donne un petit coup d'épaule avant de se lever."

    iris sourire "Allez. Viens voir Julian perdre une deuxième fois."

    julian colere "J'ENTENDS !"

    iris rire "Parfait."

    "Je me lève et la suis."

    $ hideGroup()

    jump _24_0_1_1_0_0_SOIR


label _24_0_1_1_0_0_SOIR:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_j24_door_5
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Il est déjà tard quand je quitte finalement les autres. Julian conteste toujours le résultat de sa deuxième partie, Elen lui propose une troisième revanche et j'entends encore Mara rire au bout du couloir lorsque je rejoins les dortoirs."

    "Sa voix me fait ralentir pendant une fraction de seconde."

    "Hier soir, le simple fait de l'entendre derrière ma porte m'avait glacé."

    "Aujourd'hui, la sensation est toujours là, quelque part au fond de mon ventre, mais elle ne prend pas toute la place."

    think "C'est déjà mieux."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_j24_door_6
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "En entrant dans ma chambre, je retrouve le bureau à sa place et la grille d'aération toujours dégagée. Cela ne m'empêche pas de regarder le conduit avec méfiance."

    "Je le regarde quelques secondes avant de le tirer encore un peu, suffisamment pour libérer presque entièrement l'aération sans pour autant le remettre complètement à sa place."

    think "On avance."

    "Je m'assois sur le lit et ouvre machinalement ma tablette."

    "La liste des Commandements a déjà été mise à jour."

    "Le nouveau texte est là, ajouté aux autres comme s'il avait toujours existé."

    "Toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    "Je relis la phrase plusieurs fois, non pas parce que j'y cherche un piège, mais parce qu'elle me paraît étrangement concrète."

    "Quelque part sur Terre, des gens qui n'avaient aucune garantie hier en ont désormais une, aussi imparfaite soit-elle."

    "Ce n'est probablement pas la révolution que Julian voudrait raconter dans ses mémoires, mais c'est quelque chose qui n'existait pas ce matin."

    think "Et j'ai participé à ça."

    "Je reste un moment avec cette pensée."

    "Elle me paraît presque prétentieuse, mais pour une fois je n'essaie pas immédiatement de la corriger."

    noam sourire "Pas mal."

    "Je pose la tablette à côté de moi puis repense malgré moi à Tomas."

    "Sa tasse vide qu'il essayait de boire, sa tablette oubliée, les trois versions identiques du texte et cette manière étrange de perdre le fil d'une idée qu'il semblait pourtant avoir parfaitement en tête."

    think "Il était juste crevé."

    "Je fixe le plafond."

    think "Moi aussi j'étais juste crevé quand tout a commencé."

    "La comparaison suffit à faire disparaître une partie de ma bonne humeur."

    noam fatigue "Non."

    "Je me redresse légèrement."

    noam fatigue "Pas ce soir."

    "Pour une fois, je refuse de transformer une journée normale en enquête avant même d'avoir une raison de le faire."

    "Si Tomas agit encore bizarrement demain, je lui parlerai. S'il va mieux, j'aurai simplement passé dix minutes à m'inquiéter pour quelqu'un qui avait mal dormi."

    "Je coupe la tablette et m'allonge."

    "Avant d'éteindre la lumière, mon regard revient une dernière fois vers la grille d'aération."

    "Elle ne bouge pas, aucun bruit ne vient du conduit et, pendant quelques secondes, elle redevient simplement ce qu'elle est censée être : une grille dans un mur."

    think "Aujourd'hui, j'ai été utile."

    "Je ferme les yeux avec un sourire que personne n'est là pour voir."

    think "Ça me suffit largement."

    stop music fadeout 1.5

    call show_chapter_title("Fin du chapitre 7", "Chapitre 7 — Un semblant de normalité") from _call_show_chapter_title_7
    call end_day("25", sleeping=True) from _call_j24_stay_end_day_25
    jump _25_0_1_1_0_0_REVEIL
