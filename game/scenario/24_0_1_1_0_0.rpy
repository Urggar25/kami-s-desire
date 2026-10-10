default j24_vital_vote = None
default j24_tomas_convinced = False


label _24_0_1_1_0_0_REVEIL:

    $ current_day = 24
    $ day_id = 24
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

    noam reflexion "Il y a un « mais »."

    tomas fatigue "Pourquoi il y aurait forcément un mais ?"

    noam taquin "Parce que t'as exactement la tête que tu fais avant de commencer une phrase par « techniquement »."

    elias rire "C'est vrai."

    tomas colere "Vous avez tous décidé de m'emmerder ce matin ?"

    iris blase "Non, mais maintenant que tu proposes..."

    tomas fatigue "Super."

    "Je prends une bouchée avant de reprendre, sans insister davantage sur le ton."

    noam reflexion "Tu es favorable au texte, mais quelque chose te gêne."

    tomas reflexion "Je..."

    "Il regarde l'écran devant lui, puis lève les yeux vers nous."

    tomas hesitation "Je crois."

    ryn surpris "Tu crois ?"

    tomas stress "Oui, Ryn. Je crois."

    ryn desaccord "Comment tu peux ne pas savoir si quelque chose te gêne ?"

    tomas colere "Parce que j'essaie encore de comprendre ce que c'est !"

    "Le ton monte suffisamment vite pour couper quelques conversations autour de nous."

    ryn agace "D'accord, tranquille."

    tomas fatigue "Je suis tranquille."

    iris blase "Non, pas vraiment."

    noam raison "Attendez, laissez-le expliquer. On a tous déjà vu que ça ne sert à rien de se brusquer."

    "Tomas inspire lentement puis fait défiler le texte sur sa tablette."

    tomas reflexion "Le principe est évidemment bon. Je ne discute même pas de ça. Toute personne doit avoir de quoi manger, boire et un endroit où vivre, très bien."
    tomas raison "Ce qui me dérange, c'est peut-être... Enfin, je sais pas, est-ce que c'est seulement possible tout ça ?!"

    nyra reflexion "Comment produire assez pour fournir tout le monde ?"

    tomas hesitation "Ouais... Je ne sais pas encore. Y'a quelque chose qui me semble bizarre dans cette proposition."
    tomas colere "Mais j'arrive pas à mettre le doigt dessus."

    ryn fatigue "On est bien avancés."

    noam reflexion "« En quantité suffisante » ? C'est ça qui te semble bizarre ?"

    "Cette fois il hésite plus longtemps."

    tomas reflexion "Peut-être aussi."

    elen inquiet "Mais suffisante, ça veut juste dire suffisamment pour manger normalement, non ?"

    tomas raison "Dans le langage courant, oui. Juridiquement, ça dépend de ce qu'on met derrière. Enfin... juridiquement, c'est pas exactement le bon terme puisque les Commandements sont leur propre système normatif, mais vous voyez ce que je veux dire."

    "Il s'interrompt brusquement."

    tomas reflexion "Non. C'est pas ça."

    noam reflexion "Qu'est-ce qui n'est pas ça ?"

    tomas fatigue "Mon problème."

    julian hesitation "Tu avais pourtant commencé ton exposé habituel."

    tomas reflexion "Je sais."

    julian neutre "Et tu ne sais plus ?"

    "Un court silence tombe autour de lui."
    "Tomas baisse les yeux vers son écran et relit plusieurs fois la même ligne, les lèvres légèrement entrouvertes comme s'il attendait que le raisonnement lui revienne tout seul."

    elen inquiet "T'as bien dormi cette nuit ?"

    "Il relève la tête presque brutalement."

    tomas surpris "Pourquoi tu me demandes ça ?"

    elen surpris "Bah... parce que t'as l'air fatigué."

    tomas reflexion "Ah."

    pause 0.3

    tomas fatigue "Non. Pas très bien."

    elen sourire "Ça doit être ça alors."

    tomas neutre "Probablement."

    "Il reprend sa tasse et la porte machinalement à ses lèvres avant de constater une deuxième fois qu'elle est vide."

    "Je croise le regard d'Iris. Elle hausse très légèrement un sourcil."

    think "D'accord. Même elle a remarqué."

    noam reflexion "Tu veux qu'on reprenne tranquillement ?"

    tomas fatigue "Non, laisse tomber."

    noam raison "Si tu as une vraie réserve sur le texte, autant la comprendre avant le débat."

    tomas fatigue "Je viens de te dire que j'arrive pas à la formuler."

    noam neutre "Justement."

    tomas colere "Noam, j'ai dit laisse tomber."

    "La réponse sort beaucoup plus sèchement que prévu. Tomas détourne immédiatement les yeux, visiblement conscient de son propre ton."

    tomas fatigue "Désolé."

    noam neutre "C'est pas grave."

    tomas reflexion "Je vais relire le texte aux Archives. Il y a peut-être quelque chose que j'ai raté."

    nyra raison "Si tu trouves une objection concrète, il faudra la présenter cet après-midi."

    tomas neutre "Oui."

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

    tomas raison "C'est pas exactement trois fois le même document. À gauche, c'est la proposition originale déposée. Au milieu, la version enregistrée par Kami après le tirage au sort. À droite, c'est une retranscription que j'ai faite moi-même pour vérifier s'il y avait une différence de formulation."

    noam reflexion "Et il y en a une ?"

    tomas neutre "Non."

    noam reflexion "Donc les trois sont identiques."

    tomas fatigue "Oui."

    noam taquin "C'était une manière très longue de répondre oui."

    tomas colere "Je sais."

    "Il ferme la copie qu'il a rédigée, hésite, puis la rouvre presque immédiatement."

    noam reflexion "Tu cherches quoi exactement ?"

    tomas fatigue "Si je le savais, j'aurais probablement déjà terminé."

    noam neutre "Logique."

    tomas reflexion "Le problème, c'est que plus je relis le texte, moins je vois ce qui me gêne. Et pourtant, j'ai toujours cette impression qu'il y a quelque chose."

    noam raison "Quelque chose qui permettrait à Kami de contourner le Commandement ?"

    tomas hesitation "Peut-être."

    noam reflexion "Ou quelque chose qui pourrait avoir un effet pervers ?"

    tomas reflexion "C'est ce que je pensais au début, mais je ne trouve aucun mécanisme évident."

    "Il fait défiler le texte jusqu'à la phrase centrale."

    tomas raison "« Toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante. »"

    tomas reflexion "Regarde « disposer » par exemple. Est-ce qu'on parle d'un accès immédiat ? D'un accès raisonnable ? D'une simple disponibilité théorique ?"

    noam raison "Si tu dois marcher vingt kilomètres pour avoir de l'eau, j'aurais du mal à dire que t'en disposes réellement."

    tomas reflexion "Moi aussi, mais le texte ne le dit pas."

    noam neutre "D'accord."

    tomas raison "Et « alimentation suffisante », ça veut dire quoi ? Suffisante pour ne pas mourir ? Suffisante pour être en bonne santé ? Est-ce qu'on parle de quantité, de qualité, d'apports nutritionnels ?"

    noam reflexion "Là, on commence à retrouver ton problème."

    tomas hesitation "Oui..."

    "Il garde les yeux sur l'écran quelques secondes puis secoue lentement la tête."

    tomas fatigue "Non."

    noam surpris "Non ?"

    tomas fatigue "C'est pas ça."

    noam reflexion "Pourtant, tu viens de donner deux objections assez précises."

    tomas reflexion "Ce sont des imprécisions. Elles me gênent, évidemment, mais ce n'est pas ce que j'essayais de comprendre depuis ce matin."

    noam neutre "Et tu sais toujours pas ce que c'était ?"

    tomas fatigue "Non."

    "Son visage se ferme légèrement. Il passe une main sur son front et reste un moment immobile devant les trois documents."

    noam inquiet "Ça t'arrive souvent d'oublier une idée en plein milieu ?"

    tomas fatigue "Évidemment que oui."

    noam reflexion "À ce point-là ?"

    tomas colere "Noam."

    noam neutre "Je demande."

    tomas fatigue "J'ai mal dormi, je suis fatigué et ça fait vingt-quatre jours qu'on vit dans une station avec une IA qui transforme chaque phrase en potentiel piège juridique. Donc oui, aujourd'hui je suis un peu moins efficace que d'habitude."

    noam taquin "Un peu."

    tomas fatigue "Merci."

    "Je m'adosse à la table à côté de lui."

    noam raison "Bon. On reprend autrement."

    tomas reflexion "Comment ?"

    noam reflexion "Tu es pour le principe."

    tomas neutre "Oui."

    noam reflexion "Tu ne veux pas empêcher les gens d'avoir un toit, de l'eau ou à manger."

    tomas fatigue "Évidemment que non."

    noam reflexion "Donc ton doute ne porte pas sur l'objectif."

    tomas raison "Non."

    noam reflexion "Il porte soit sur la façon dont c'est écrit, soit sur ce que Kami pourra en faire."

    "Tomas reste silencieux, puis acquiesce lentement."

    tomas neutre "Probablement."

    noam raison "Alors garde ça pour le débat."

    tomas surpris "Quoi ?"

    noam reflexion "Ton doute."

    tomas fatigue "Je vais pas me lever devant onze personnes pour leur annoncer que quelque chose me gêne sans savoir quoi."

    noam taquin "Tu viens de le faire au petit-déjeuner."

    tomas colere "Et ça s'est très bien passé, comme tu as pu le constater."

    noam sourire "Justement, cette fois je serai préparé."

    tomas reflexion "À quoi ?"

    noam raison "À essayer de comprendre ce que t'essaies de dire au lieu de laisser Ryn te demander toutes les vingt secondes si tu votes pour."

    "Un léger sourire apparaît malgré lui."

    tomas taquin "Ça va être difficile."

    noam sourire "Je suis courageux."

    tomas reflexion "..."

    "Son expression redevient rapidement sérieuse."

    tomas fatigue "Et si je trouve une vraie raison de m'y opposer ?"

    noam neutre "Alors tu l'expliques."

    tomas surpris "Même si ça fait échouer le vote ?"

    noam raison "Si ta raison est assez importante pour qu'on préfère ne pas adopter le Commandement, oui."

    "Il me regarde un instant comme s'il attendait autre chose."

    noam reflexion "Je vais pas te demander de voter pour juste parce que les onze autres trouvent le texte évident."

    tomas neutre "..."

    noam raison "Mais si tu veux bloquer quelque chose qui peut améliorer concrètement la vie des gens, faudra qu'on sache pourquoi."

    tomas reflexion "Ça me paraît raisonnable."

    noam taquin "Ça m'arrive."

    tomas fatigue "Très rarement."

    noam sourire "À tout à l'heure."

    "Je me redresse et me dirige vers la porte."

    tomas hesitation "Noam."

    "Je me retourne."

    noam reflexion "Oui ?"

    tomas reflexion "Tu..."

    "Il s'interrompt et semble chercher ses mots beaucoup plus longtemps que la question ne le justifie."

    tomas fatigue "Non, rien."

    noam blase "Tu fais vraiment ça aujourd'hui ?"

    tomas fatigue "J'ai dit rien."

    noam taquin "D'accord."

    "Je le laisse devant ses documents et quitte les Archives."

    $ hideGroup()

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Une fois la porte refermée, je reste quelques secondes dans le couloir en repensant à la conversation."

    think "Fatigué."

    "C'est probablement tout."

    think "Et contrairement à hier, je refuse de transformer le moindre comportement bizarre en affaire d'État."

    "Je reprends ma route."

    jump _24_0_1_1_0_0_AVANT_VOTE


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

    julian sourire "Puisque notre chère Kami semble attendre un spectacle, je propose exceptionnellement de la décevoir et d'être tous d'accord en moins de cinq minutes."

    iris blase "Pour une fois, je soutiens ton plan."

    elen joie "Moi aussi ! Je vote pour, évidemment."

    ryn neutre "Pareil."

    sael raison "Il n'y a rien à discuter sur le principe. Personne ne devrait manquer de ces choses."

    nyra sourire "Tout le monde semble être d'accord."

    "Tous les regards se dirigent finalement vers Tomas. Il garde encore quelques secondes les yeux fixés sur sa tablette avant de relever la tête."

    tomas neutre "Je suis favorable au texte."

    "Tomas prend quelques secondes avant de reprendre, comme s'il essayait encore de mettre de l'ordre dans un raisonnement qui lui échappe depuis le matin."

    tomas reflexion "Je ne remets pas en cause l'objectif du Commandement. Je veux que ce soit très clair avant qu'on commence."

    tomas raison "Personne ne devrait manquer d'eau, de nourriture ou d'un endroit où dormir. Là-dessus, je pense qu'on est tous d'accord."

    elen neutre "Oui."

    tomas reflexion "Ce qui me pose problème, c'est que le texte est extrêmement général et qu'en créant une obligation aussi large sans préciser ce qu'on entend exactement par accès, suffisance ou même logement..."

    "Il s'interrompt."

    ryn agace "Et ?"

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

    tomas colere "Non ! J'essaie de comprendre si ma réserve est suffisamment importante pour qu'on la prenne en compte ! C'est pas la même chose !"

    ryn colere "Bah explique-la alors !"

    tomas colere "J'ESSAIE !"

    "Le ton claque suffisamment fort pour que toute la salle se taise."

    "Tomas s'en rend compte immédiatement et détourne les yeux."

    tomas fatigue "Désolé."

    noam raison "C'est rien."

    ryn neutre "..."

    noam reflexion "On va arrêter deux secondes de chercher à savoir si tu votes pour ou contre."

    tomas surpris "Quoi ?"

    noam raison "Depuis ce matin, tout le monde te pose la même question et, à chaque fois, tu réponds que tu es pour avant de recommencer à chercher ce qui te gêne."

    noam reflexion "Donc le problème est probablement ailleurs."

    tomas reflexion "..."

    noam raison "Oublie le vote une minute. Qu'est-ce que tu crains concrètement si le texte est adopté ?"

    "Tomas ouvre la bouche, puis reste silencieux suffisamment longtemps pour que je commence à croire que ma question n'a rien arrangé."

    tomas hesitation "Que..."

    "Il baisse les yeux."

    tomas reflexion "Que ça ne change rien."

    pause 0.4

    noam reflexion "Explique."

    tomas raison "Qu'on adopte un Commandement qui donne l'impression de protéger tout le monde, mais dont les mots permettent quand même une application minimale."

    "Il semble retrouver progressivement le fil."

    tomas raison "Une quantité de nourriture suffisante pour survivre, mais pas pour être réellement en bonne santé. Un toit, oui, mais dans quelles conditions ? De l'eau potable, oui, mais combien et à quelle distance ?"

    tomas reflexion "On pourrait voter aujourd'hui en pensant qu'on garantit des conditions de vie dignes alors que le texte garantit peut-être simplement la survie."

    noam reflexion "D'accord."

    "Je prends quelques secondes pour reprendre son raisonnement."

    noam raison "Donc tu n'as pas peur que le Commandement impose quelque chose de mauvais."

    tomas neutre "Non."

    noam reflexion "Tu as peur qu'on se satisfasse d'un texte insuffisant parce qu'il sonne bien."

    "Tomas me regarde."

    tomas surpris "Oui."

    "Sa réponse sort presque immédiatement."

    tomas raison "Voilà. C'est ça."

    noam reflexion "Et que Kami puisse ensuite nous répondre qu'elle respecte le Commandement même si son application est volontairement minimale."

    tomas raison "Exactement."

    "Il se redresse légèrement, comme si le simple fait d'avoir enfin réussi à formuler son problème venait de retirer une partie de la tension qu'il accumule depuis le matin."

    julian sourire "Il fallait donc un traducteur de Tomas."

    tomas fatigue "C'est ce que j'essaye de vous dire depuis ce matin."

    "Quelques rires circulent, mais je garde les yeux sur Tomas."

    noam raison "Ta réserve est légitime."

    ryn desaccord "Oh non..."

    noam agace "Tu peux attendre trente secondes ?"

    ryn neutre "Vas-y."

    noam reflexion "Le texte est vague et je pense que personne ici peut sérieusement garantir que Kami l'appliquera exactement comme nous l'imaginons."

    nyra raison "C'est vrai."

    noam reflexion "Mais il y a une chose que j'essaie de comprendre."

    tomas neutre "Quoi ?"

    noam raison "Si on refuse le texte aujourd'hui, qu'est-ce qu'on améliore ?"

    "Tomas ne répond pas tout de suite."

    tomas reflexion "Rien."

    noam reflexion "Les gens qui n'ont pas suffisamment à manger ?"

    tomas neutre "Ils n'obtiennent rien."

    noam reflexion "Ceux qui n'ont pas d'eau potable ?"

    tomas fatigue "Rien non plus."

    noam reflexion "Et ceux qui n'ont pas de logement ?"

    tomas neutre "Pareil."

    noam raison "Donc aujourd'hui, la situation actuelle ne leur garantit même pas cette version minimale qui t'inquiète."

    tomas reflexion "Oui, mais—"

    noam raison "Je sais."

    "Je lève légèrement la main avant qu'il continue."

    noam reflexion "Je ne dis pas que ton problème disparaît."

    noam raison "Je dis simplement qu'on est peut-être en train de comparer un texte imparfait à un texte parfait qui n'existe pas."

    "Tomas reste silencieux."

    noam reflexion "En fait nous n'avons qu'une seule question à nous poser : est-ce que ça va dans le bon sens ?"
    noam raison "On ne pourra jamais avoir de grandes réussites avec ce fonctionnement."

    nyra raison "Oui, on ne peut même pas proposer des modifications aux amendements."
    nyra reflexion "Si on le pourrait ça serait très différents, mais..."

    noam sourire "Cette proposition c'est à prendre ou à laisser. Est-ce que pour toi ça va dans le bon sens ou pas ?"

    "Il semble surpris par ma réponse."

    tomas surpris "Tu admets ça ? Que c'est imparfait ?"

    noam taquin "Tu préfères que je mente pour gagner le débat ?"

    tomas reflexion "Non. C'est hônnete."

    noam raison "Je peux pas te garantir que ce texte sera appliqué parfaitement. Je peux pas non plus te garantir qu'on aura l'occasion de l'améliorer."

    noam reflexion "Par contre, je peux regarder ce qu'il y a aujourd'hui."

    "Je désigne le texte affiché au centre de la salle."

    noam raison "Aujourd'hui, rien n'oblige Kami à garantir ces trois choses."

    noam raison "Après le vote, si on l'adopte, ce sera le cas."

    tomas reflexion "Même avec une interprétation minimale."

    noam neutre "Même avec une interprétation minimale."

    tomas reflexion "..."

    noam raison "Si quelqu'un n'a absolument rien à manger aujourd'hui et qu'après ce vote Kami est obligée de lui garantir au moins de quoi survivre, c'est insuffisant."

    noam reflexion "Mais c'est mieux que rien."

    "Tomas baisse légèrement les yeux."

    noam reflexion "Et si quelqu'un dort dehors sans aucun abri, je préfère lui garantir un toit imparfait maintenant plutôt que de lui expliquer qu'on a refusé parce qu'on espérait écrire quelque chose de mieux plus tard."

    "Cette fois, personne n'intervient."

    noam raison "Tu as raison de vouloir éviter qu'on se contente du minimum."

    noam raison "Mais je pense qu'on se tromperait si, pour éviter un minimum insuffisant, on refusait aussi ce minimum à ceux qui n'ont rien."

    pause 0.5

    "Tomas reste encore quelques secondes immobile devant sa tablette. Son regard passe du texte à moi, puis aux autres représentants."

    tomas reflexion "..."

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


label _24_0_1_1_0_0_VOTE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2

    "Le texte apparaît une dernière fois sur l'écran central tandis que le système ouvre les votes."

    "Toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    think "Après toute cette discussion, la phrase paraît presque ridiculement courte."

    "Tomas garde encore quelques secondes les yeux sur son interface avant de valider son choix. Les autres font de même et les pupitres s'éteignent progressivement autour de la table."

    "Cette fois, il ne reste plus que le mien."

    # Réutilise l'interface de vote commune aux autres débats.
    # J24 ne propose volontairement que POUR ou ABSTENTION.
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
        ("Tomas", "pour"),
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

    nyra raison "Tu as surtout fait ce que tu fais le mieux."

    noam reflexion "C'est-à-dire ?"

    nyra neutre "Tu as écouté quelqu'un que le reste de la salle commençait à considérer comme un obstacle et tu as compris que son problème n'était pas celui qu'il essayait lui-même d'expliquer."

    "La formulation me prend suffisamment au dépourvu pour que je ne trouve rien à répondre immédiatement."

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

    call end_day("25", sleeping=True) from _call_j24_stay_end_day_25
    jump _25_0_1_1_0_0_REVEIL