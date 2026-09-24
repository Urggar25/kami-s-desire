label _10_1_0_0_REVEIL:

    $ current_day = 10
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"

    scene black with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    $ blink()

    pause 0.8

    "Je me réveille avec cette impression désagréable d'avoir à peine fermé les yeux."

    scene bg_chambre at adaptive_fullscreen with Fade(1.5, 0.0, 2.0)

    "Pendant quelques secondes, je reste allongé sans bouger, jusqu'à ce que les souvenirs d'hier reviennent les uns après les autres."

    think "Ryn. Les conteneurs. Les questions qu'il posait à Anya. Et cette annonce de Kami sur les nouveaux contrôles."

    noam reflexion "..."

    "Je me tourne sur le côté et attrape ma tablette. Aucun message."

    think "Évidemment."

    "Nyra avait raison sur un point : Ryn aurait pu dénoncer Anya depuis longtemps."

    think "Il ne l'a pas fait."

    "Ça ne suffit pourtant pas à me rassurer."

    noam fatigue "Bon..."

    "Je me redresse et commence à m'habiller."

    think "J'ai faim. Et réfléchir le ventre vide ne va probablement pas me rendre plus intelligent."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Le Conclave est déjà bien réveillé. Quelques portes sont ouvertes, plusieurs voix résonnent dans le couloir et quelqu'un passe devant moi avec une tasse beaucoup trop pleine."

    think "Une matinée normale. Enfin, notre version de normale."

    jump _10_1_0_0_CAFETERIA


label _10_1_0_0_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    "La cafétéria est déjà bien remplie."

    $ showGroup([
        ("elen", "joie", 0.10),
        ("julian", "sourire", 0.28),
        ("mara", "neutre", 0.46),
        ("tomas", "neutre", 0.64),
        ("iris", "fatigue", 0.82),
    ])

    elen joie "Je vous préviens, je commence officiellement à préparer mon festival."

    mara reflexion "Tu n'as aucun budget."

    elen sourire "Détail."

    julian taquin "Aucun lieu."

    elen "Détail."

    tomas reflexion "Aucune autorisation."

    elen desaccord "Mais on vient littéralement de voter pour ça !"

    mara "On a voté pour autoriser les regroupements, pas pour te nommer ministre des festivals."

    elen joie "Pas encore."

    iris fatigue "Il est beaucoup trop tôt pour cette conversation."

    julian sourire "Il est toujours trop tôt pour les ambitions politiques d'Elen."

    "Je récupère un plateau et m'installe avec eux."

    noam sourire "Bonjour."

    iris fatigue "Toi, t'as mieux dormi que moi."

    noam taquin "C'était difficile de faire pire."

    iris desaccord "Ne recommence pas."

    noam sourire "Je n'ai rien dit."

    "Elle me lance un regard qui signifie très clairement qu'elle sait exactement ce que je n'ai rien dit."

    tomas reflexion "Anya va mieux ?"

    "Iris lui répond presque immédiatement, sans baisser la voix plus que nécessaire."

    iris fatigue "Mon problème de plomberie ? Oui, il va très bien."

    pause 0.4

    tomas surpris "..."

    noam gene "..."

    mara reflexion "Quel problème de plomberie ?"

    iris desaccord "Ma douche."

    mara "Ah."

    iris fatigue "Elle fait du bruit toute la nuit."

    julian taquin "Ça arrive aux vieilles installations."

    iris colere "Julian."

    julian sourire "Je parle de la douche."

    "Je baisse légèrement les yeux vers mon plateau pour éviter de sourire."

    think "On devient beaucoup trop mauvais pour cacher ça."

    $ hideGroup()

    play sound sfx_announce

    stop music fadeout 0.8

    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Oh, quelle adorable petite scène ! Le petit-déjeuner en famille."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Profitez bien de vos conversations privées tant que vous le pouvez."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Parce que justement, le prochain vote concernera un sujet qui devrait particulièrement vous intéresser."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "L'autorisation des dispositifs de brouillage."

    "Plusieurs conversations s'arrêtent immédiatement."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous connaissez déjà ces merveilleux petits appareils. Certains d'entre vous en possèdent dans leurs chambres. Ils permettent de perturber localement mes systèmes de surveillance audio et vidéo."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Une invention profondément vexante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Imaginez : moi, privée de vos conversations les plus intimes. Vos petites disputes. Vos secrets."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Vos déclarations d'amour maladroites."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le vote déterminera donc si leur utilisation peut officiellement être autorisée dans les districts. Mais évidemment, j'aime la cohérence."

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Si une seule personne vote contre leur autorisation..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Alors je considérerai qu'il serait particulièrement incohérent de laisser ces dispositifs actifs ici."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Tous les brouilleurs présents dans les chambres des représentants seront donc désactivés et retirés."

    "Mon corps se raidit immédiatement."

    think "Merde."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Après tout, vous n'allez pas demander à vos citoyens de vivre sous surveillance tout en vous réservant un petit espace privé, n'est-ce pas ?"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Ce serait terriblement hypocrite."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous aurez jusqu'à demain pour réfléchir."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Bonne journée, mes petits cachottiers."

    hide screen kami_broadcast_ui

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    $ showGroup([
        ("mara", "reflexion", 0.10),
        ("tomas", "reflexion", 0.28),
        ("iris", "inquiet", 0.46),
        ("noam", "inquiet", 0.64),
        ("nyra", "neutre", 0.82),
    ])

    "Pendant quelques secondes, personne ne parle."

    mara reflexion "Bon."

    tomas reflexion "Ça va être un vote compliqué."

    iris inquiet "Ouais."

    "Son regard rencontre le mien une fraction de seconde, à peine assez longtemps pour être remarqué. Nyra, elle, le remarque."

    nyra reflexion "Noam."

    noam inquiet "Hm ?"

    nyra raison "Viens avec moi deux minutes."

    mara "Vous avez fini de manger ?"

    nyra "Pas vraiment."

    "Elle se lève pourtant immédiatement."

    noam "Je reviens."

    $ hideGroup()

    jump _10_1_0_0_NYRA


label _10_1_0_0_NYRA:

    scene couloir_principal at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("noam", "inquiet", 0.32),
        ("nyra", "raison", 0.70),
    ])

    "Nyra attend que la porte de la cafétéria se referme derrière nous avant de ralentir."

    nyra raison "On a un problème, et je préfère vérifier que tu as compris exactement lequel."

    noam desaccord "Si les brouilleurs disparaissent, Kami récupère le son et l'image de toutes les chambres. Oui, j'avais remarqué."

    noam inquiet "Si les brouilleurs disparaissent..."

    nyra raison "Kami récupère le son et l'image de toutes les chambres."

    noam "Et Anya tient probablement moins d'une heure."

    nyra "Probablement beaucoup moins."

    "Elle garde son calme, mais ses bras sont croisés beaucoup plus fermement que d'habitude."

    noam reflexion "On peut peut-être la déplacer."

    nyra raison "Où ?"

    noam "Je sais pas."

    nyra "Toutes les salles communes sont surveillées. L'infirmerie est surveillée. Les couloirs sont surveillés. Les chambres sans brouilleur seront surveillées."

    nyra "Et même si nous trouvions un endroit temporaire, elle devrait manger, se laver et dormir."

    noam fatigue "D'accord."

    nyra reflexion "Donc non. Nous ne devons pas préparer un plan B."

    noam surpris "Pardon ?"

    nyra determine "Nous devons faire passer le vote."

    noam inquiet "Donc il nous faut l'unanimité."

    nyra determine "Oui. Une seule voix contre, et Anya n'a plus de cachette."

    pause 0.5

    noam inquiet "Tu crois que quelqu'un votera contre ?"

    nyra raison "Oui."

    noam surpris "Qui ?"

    nyra "Je n'en sais rien."

    noam desaccord "Très rassurant."

    nyra reflexion "Tomas défend souvent les systèmes de sécurité. Elias aussi. Ryn peut considérer la surveillance comme nécessaire pour maintenir l'ordre. Mara pourrait demander des garanties."

    nyra "Sael peut avoir peur de ce que les gens feront avec une protection totale contre les caméras."

    noam "Donc pratiquement tout le monde."

    nyra "Exactement."

    "Elle s'approche légèrement."

    nyra raison "Le problème, c'est que pour eux, ce vote est théorique."

    noam reflexion "Et pour nous, il décide si Anya survit."

    nyra "Oui."

    noam inquiet "On peut pas leur dire."

    nyra "Évidemment que non."

    "Elle soupire doucement."

    nyra reflexion "Il va donc falloir les convaincre pour d'autres raisons."

    noam "Tu penses pouvoir le faire ?"

    "Nyra me regarde avec une expression parfaitement neutre."

    nyra taquin "Noam."

    noam "Oui ?"

    nyra "C'est littéralement mon travail."

    pause 0.4

    noam sourire "Vu comme ça."

    nyra raison "Pendant le débat, laisse-moi parler."

    noam surpris "C'est tout ?"

    nyra "Non. S'ils commencent à défendre la surveillance, ne les contredis pas."

    noam reflexion "Pourquoi ?"

    nyra taquin "Parce qu'ils feront une partie du travail à ma place."

    "Elle tourne déjà les talons."

    noam reflexion "Je sens que je vais regretter de demander."

    nyra "Probablement."

    $ hideGroup()

    jump _10_1_0_0_TEMPS_LIBRE


label _10_1_0_0_TEMPS_LIBRE:

    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.5

    "Le reste de la matinée passe lentement et, à l'heure du déjeuner, les conversations tournent déjà presque toutes autour du prochain vote."

    think "Pour une fois, je préférerais que personne n'y réfléchisse trop."

    # TEMPS LIBRE
    # Insérer ici le système de temps libre de la journée.

    jump _10_1_0_0_DEBAT


label _10_1_0_0_DEBAT:

    call MAYBE_PLAY_SCRIPTED_DOOR("salle_commune", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_3
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "En milieu d'après-midi, plusieurs représentants se retrouvent naturellement dans la salle commune. Personne n'avait réellement prévu de débat ; il commence simplement lorsque Tomas pose une question."

    $ showGroup([
        ("tomas", "raison", 0.08),
        ("elias", "reflechit", 0.25),
        ("mara", "reflexion", 0.42),
        ("nyra", "neutre", 0.58),
        ("noam", "reflexion", 0.75),
        ("iris", "neutre", 0.92),
    ])

    tomas raison "Vous voulez vraiment autoriser n'importe qui à bloquer complètement les caméras ? Je comprends l'argument de la vie privée, mais on oublie un peu vite pourquoi elles ont été installées."

    iris reflexion "Tu penses vraiment qu'elles empêchent tant de choses que ça ?"

    tomas raison "Pas tout, évidemment. Mais une agression dans une rue, quelqu'un qui s'effondre, un incendie, un accident... Quand il y a des caméras, on peut comprendre plus vite ce qui s'est passé et parfois intervenir avant que ça empire."

    elias reflechit "Je suis assez d'accord avec lui. J'aime pas l'idée d'être observé en permanence, mais la surveillance, c'est pas seulement du contrôle. Ça peut aussi protéger les gens."

    mara reflexion "Donc vous seriez contre les brouilleurs ?"

    tomas inquiet "Je sais pas encore. Je dis juste qu'en les autorisant partout, on crée aussi des zones où quelqu'un peut faire n'importe quoi sans laisser de trace."

    elias "C'est surtout ça qui me gêne."

    nyra raison "Et vous avez raison sur ce point : les caméras sont utiles. Elles dissuadent certains crimes, facilitent les enquêtes et peuvent sauver des gens. Mais le vote ne porte pas sur leur suppression ; il porte sur la possibilité de s'y soustraire ponctuellement."

    "Tomas se redresse légèrement, déjà prêt à répondre, mais Nyra enchaîne avant qu'il puisse reprendre son argument."

    nyra "Si je suis votre raisonnement jusqu'au bout, parce qu'une caméra peut protéger quelqu'un, personne ne devrait jamais pouvoir échapper à une caméra. Pourtant, j'imagine qu'aucun de vous n'accepterait d'en avoir une dans sa chambre, dans un vestiaire, pendant une consultation médicale ou au milieu d'une conversation privée."

    elias reflexion "Évidemment que non, mais ce sont des espaces privés. Une rue, c'est différent."

    nyra raison "Justement. La vraie question est de savoir qui décide où commence la vie privée. Une réunion syndicale dans un local public ? Une discussion entre un avocat et son client ? Une réunion politique ? Un rendez-vous médical dans un bâtiment appartenant à l'État ? La frontière est beaucoup moins évidente qu'entre une chambre et une rue."

    mara reflexion "Là-dessus, elle a raison. On ne peut pas simplement décréter que tout ce qui n'est pas chez toi appartient à la surveillance."

    tomas raison "D'accord, mais un brouilleur peut aussi être utilisé volontairement dans la rue pour masquer un crime. Ce risque existe toujours."

    nyra "Bien sûr, et je ne cherche pas à prétendre le contraire. Une voiture peut servir à fuir après un crime, un médicament peut être détourné, un réseau informatique peut servir à voler des données. Le fait qu'un outil puisse être mal utilisé n'implique pas forcément qu'il faille l'interdire."

    mara "On réglemente son utilisation."

    nyra sourire "Exactement. Et c'est beaucoup plus facile de réglementer une filière légale que des appareils clandestins dont personne ne connaît ni le fabricant, ni la puissance, ni l'utilisateur."

    elias reflechit "Donc tu voudrais autoriser les brouilleurs mais définir des endroits où ils resteraient interdits."

    nyra raison "Oui. Hôpitaux, zones de sécurité, certains bâtiments administratifs, éventuellement certains événements. On protège les endroits où la surveillance est réellement nécessaire sans considérer que chaque citoyen doit être observable en permanence."

    tomas reflexion "Ça règle une partie du problème, mais si tu légalises ces appareils, tu vas forcément en multiplier le nombre."

    nyra "Oui, et c'est aussi là que l'interdiction me semble économiquement absurde. Une filière légale signifie de l'extraction de matières premières, du transport, de la transformation, de l'assemblage, de la maintenance, de la certification et du développement logiciel."

    elias reflexion "Donc beaucoup d'emplois."

    nyra "Exactement. Et surtout des appareils qu'on peut enregistrer, tester et limiter techniquement. Avec une interdiction totale, les brouilleurs ne disparaissent pas ; ils deviennent simplement un marché clandestin réservé à ceux qui savent où les trouver."

    iris taquin "Je crois que Nyra vient de transformer un débat sur la surveillance en politique industrielle."

    julian sourire "Et personne n'a réussi à l'arrêter."

    "Tomas soupire en regardant Nyra, plus amusé qu'agacé."

    tomas desaccord "J'ai quand même l'impression que tu nous fais dire ce qui t'arrange depuis dix minutes."

    nyra taquin "Je vous pose des questions. Si vos réponses m'arrangent, je n'y peux rien."

    noam sourire "C'est exactement ce qu'elle m'avait annoncé ce matin."

    tomas reflexion "Je reste convaincu qu'on sous-estime le rôle protecteur des caméras."

    nyra raison "Et moi je pense que tu viens justement de donner le meilleur argument pour conserver les caméras là où elles sont utiles. Mais conserver la surveillance n'oblige pas à interdire toute possibilité d'intimité."

    "Elle marque une courte pause avant de regarder successivement Tomas puis Elias."

    nyra "Le choix n'est pas entre surveillance totale et absence totale de surveillance. Il est entre un système où la caméra reste la règle mais où certaines personnes peuvent créer un espace privé, et un système où personne n'a jamais le droit de dire : ici, maintenant, je ne veux pas être observé."

    "Cette fois, Tomas ne répond pas immédiatement. Elias baisse les yeux, réfléchit quelques secondes puis se redresse."

    elias reflechit "Présenté comme ça, je voterais probablement pour l'autorisation, à condition qu'il y ait des restrictions claires sur certains lieux."

    tomas reflexion "Moi, j'ai encore besoin d'y réfléchir. Mais je suis moins opposé qu'au début."

    iris sourire "Ça ressemble beaucoup à une victoire."

    nyra taquin "Pas encore. Il nous faut l'unanimité."

    "La phrase paraît parfaitement innocente pour les autres. Pour moi, elle signifie tout autre chose."

    think "Et elle le sait très bien."

    $ hideGroup()

    jump _10_1_0_0_ARCHIVES


label _10_1_0_0_ARCHIVES:

    $ current_period = "Fin d'après-midi"

    scene couloir_principal at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    "En fin d'après-midi, je traverse les couloirs sans destination particulière."

    "Le débat tourne encore dans ma tête."

    think "Si Nyra arrive à convaincre Tomas, on devrait pouvoir faire passer le vote. Devrait."

    "Je ralentis devant la salle des archives."

    think "Je ne viens pratiquement jamais ici."

    "La porte est légèrement entrouverte et une lumière bleutée passe par l'ouverture."

    noam reflexion "..."

    "Je m'approche."

    # Remplacer bg_archives si l'identifiant exact de la salle diffère dans le projet.
    call MAYBE_PLAY_SCRIPTED_DOOR("archives", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_4
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "La salle est presque vide ; des rangées de terminaux longent les murs, mais un seul est allumé, celui devant lequel Ryn est assis."

    $ showGroup([
        ("ryn", "reflexion", 0.68),
    ])

    "Il ne m'a pas entendu entrer."

    "Son écran affiche plusieurs fenêtres disposées en mosaïque."

    "Des images de hangars."

    "Des quais."

    "Des camions."

    "Des conteneurs filmés depuis différents angles."

    think "Des caméras."

    "Je reste près de l'entrée."

    "Ryn ouvre une fiche."

    "Numéro de conteneur."

    "Origine."

    "Destination."

    "Scellé."

    "Statut."

    "Il fait défiler plusieurs images, puis clique sur une option."

    "\"CONTRÔLE NON PRIORITAIRE\""

    "Une nouvelle fiche apparaît."

    "Encore quelques secondes."

    "\"CONTRÔLE NON PRIORITAIRE\""

    "Puis une troisième."

    "\"INSPECTION RECOMMANDÉE\""

    "Ryn s'arrête."

    "Il consulte les images plus attentivement."

    "Zoom sur une paroi."

    "Zoom sur un scellé."

    "Puis il change manuellement le statut."

    "\"DESTRUCTION — ANOMALIE STRUCTURELLE\""

    think "Qu'est-ce que..."

    "Un autre conteneur."

    "\"CONTRÔLE NON PRIORITAIRE\""

    "Encore un."

    "\"CONTRÔLE NON PRIORITAIRE\""

    "Encore."

    "\"CONTRÔLE NON PRIORITAIRE\""

    think "Il valide presque tout."

    "Je reste encore un moment à l'observer et, plus je regarde, moins la scène ressemble à un simple contrôle administratif."

    "Ryn examine chaque conteneur suffisamment longtemps pour savoir exactement ce qu'il fait."

    "Mais il en écarte énormément des inspections physiques."

    think "Comme s'il essayait de faire passer quelque chose."

    "Ou quelqu'un."

    "Je quitte enfin l'ombre de l'entrée."

    noam "Tu bosses ?"

    "Ryn sursaute brutalement."

    $ showGroup([
        ("noam", "neutre", 0.28),
        ("ryn", "surpris", 0.72),
    ])

    ryn surpris "Putain !"

    "Il se retourne immédiatement."

    ryn colere "Noam ?!"

    noam gene "Désolé."

    ryn desaccord "Tu fais quoi ici ?"

    noam "Je pourrais te poser la même question."

    "Il jette un coup d'œil vers l'écran puis se détend légèrement."

    ryn reflexion "Personne ne vient jamais ici à part Tomas de temps en temps. Je participe aux missions rémunérées annoncées par Kami."

    noam reflexion "Les contrôles de cargaison ?"

    ryn neutre "Oui. Je vérifie les signalements automatiques avant qu'un conteneur parte en inspection physique."

    noam "Les contrôles de cargaison."

    ryn "Oui."

    noam reflexion "Je pensais que c'était destiné aux habitants des districts."

    ryn "Rien n'interdit aux représentants d'y participer."

    noam "Et tu fais quoi exactement ?"

    ryn raison "Je vérifie les signalements automatiques. Les caméras analysent les conteneurs avant leur inspection physique. Déformation. Scellé endommagé. Poids incohérent. Température. Données de trajet."

    noam reflexion "Et tu décides lesquels doivent être contrôlés."

    ryn "En partie."

    noam "Ou détruits."

    ryn "S'ils présentent un risque."

    noam reflexion "Et lesquels ne doivent surtout pas être ouverts."

    "Il tourne lentement la tête vers moi."

    ryn reflexion "..."

    "Je regarde l'écran."

    noam "T'en valides beaucoup."

    ryn desaccord "Le système automatique fait beaucoup de faux positifs."

    noam "Hm."

    ryn "Quoi ?"

    noam "Rien."

    "Je m'approche du bureau."

    "Ryn se raidit légèrement."

    noam reflexion "Ça paie suffisamment bien pour que tu passes ton après-midi ici ?"

    ryn reflexion "Correctement. Mais ce n'est pas vraiment pour l'argent que je fais ça."

    "Je regarde encore l'écran."

    "Une nouvelle cargaison apparaît."

    "Limen."

    "Destination : Nexus."

    "Ryn la sélectionne."

    "Une alerte jaune s'affiche."

    "\"MASSE INCOHÉRENTE\""

    "Il observe les images quelques secondes."

    "Puis clique."

    "\"CONTRÔLE NON PRIORITAIRE\""

    pause 0.5

    "Je m'approche encore."

    noam "Ryn."

    ryn "Quoi ?"

    "Je baisse la voix au minimum."

    noam "{i}Je sais pour Anya.{/i}"

    pause 1.0

    "Son visage se vide complètement."

    $ showGroup([
        ("noam", "determine", 0.30),
        ("ryn", "peur", 0.70),
    ])

    ryn peur "{i}...{/i}"

    "Ses yeux quittent immédiatement les miens."

    "Écran."

    "Porte."

    "Caméra au plafond."

    "Puis moi."

    ryn inquiet "{i}Ne dis pas ce nom ici.{/i}"

    noam determine "{i}Il n'y a personne.{/i}"

    ryn colere "{i}J'ai dit : ne dis pas ce nom ici.{/i}"

    "Je me penche un peu plus près."

    noam "{i}Je sais que tu l'as vue.{/i}"

    "Ryn ne répond rien."

    noam "{i}Elle m'a raconté.{/i}"

    ryn desaccord "{i}Alors pourquoi tu viens me confronter ici ?{/i}"

    noam "{i}Parce que je voulais comprendre.{/i}"

    ryn "{i}Comprendre quoi ?{/i}"

    noam "{i}Pourquoi tu l'as aidée.{/i}"

    "Il me fixe."

    noam "{i}Tu aurais pu appeler Kami.{/i} {i}Tu aurais pu la dénoncer.{/i} {i}Tu ne l'as pas fait.{/i}"

    "Ryn serre légèrement la mâchoire."

    noam "{i}Et depuis tout à l'heure, tu marques la moitié des conteneurs comme ne devant pas être contrôlés.{/i}"

    ryn reflexion "{i}...{/i}"

    noam "{i}Je sais qu'Anya est cachée.{/i} {i}Je lui ai permis de rester.{/i}"

    "Son expression change une nouvelle fois."

    "Cette fois, ce n'est plus de la peur que je lis sur son visage, mais de la surprise."

    ryn surpris "{i}Toi ?{/i}"

    noam "{i}Avec Iris, Nyra et Tomas.{/i}"

    ryn "{i}...{/i}"

    noam "{i}Kami n'est pas au courant.{/i}"

    ryn desaccord "{i}Évidemment.{/i}"

    noam "{i}Et peu de représentants le savent.{/i}"

    "Ryn passe une main sur son visage."

    ryn fatigue "{i}Putain.{/i}"

    noam reflexion "{i}Quoi ?{/i}"

    ryn fatigue "{i}Je pensais qu'elle était arrivée ici par accident et qu'Iris avait simplement décidé de la cacher.{/i}"

    noam "{i}C'est plus ou moins ça.{/i}"

    ryn "{i}Et toi, tu participes.{/i}"

    noam "{i}Oui.{/i}"

    ryn reflexion "{i}Nyra aussi.{/i}"

    noam "{i}Oui.{/i}"

    ryn "{i}Tomas ?{/i}"

    noam "{i}Oui.{/i}"

    pause 0.5

    ryn fatigue "{i}...{/i}"

    noam "{i}Alors maintenant, tu peux me répondre.{/i}"

    ryn reflexion "{i}À quoi ?{/i}"

    noam "{i}Pourquoi tu fais ça.{/i}"

    "Je désigne l'écran."

    "Ryn reste silencieux longtemps."

    "Il regarde la fiche du conteneur Limen-Nexus."

    "Puis le statut qu'il vient lui-même de modifier."

    ryn triste "{i}Parce que j'en ai marre.{/i}"

    noam reflexion "{i}De quoi ?{/i}"

    ryn triste "{i}De voir les frontières.{/i}"

    "Sa voix est basse."

    ryn "{i}De voir des gens attendre derrière.{/i} {i}De voir des familles séparées.{/i} {i}Des gens qui essaient de passer et qu'on repousse.{/i} {i}Ou pire.{/i}"

    "Il baisse les yeux."

    ryn triste "{i}J'ai passé des années à les empêcher de traverser.{/i}"

    noam reflexion "{i}Quand tu étais gardien.{/i}"

    ryn "{i}Oui.{/i}"

    "Il laisse échapper un rire très court, sans amusement."

    ryn triste "{i}On nous disait qu'on protégeait les districts.{/i} {i}Qu'on empêchait les trafics.{/i} {i}Les passages clandestins.{/i} {i}Les menaces.{/i} {i}Et je l'ai cru.{/i}"

    "Ses doigts se referment légèrement autour de la souris."

    ryn colere2 "{i}J'ai arrêté des gens qui voulaient juste rentrer chez eux.{/i} {i}J'ai renvoyé des familles.{/i} {i}J'ai obéi à des ordres stupides parce que c'était mon travail.{/i}"

    noam inquiet "{i}Ryn...{/i}"

    ryn "{i}Et maintenant les frontières sont encore pires qu'avant.{/i} {i}Sauf que cette fois, il n'y a même plus besoin de gardiens.{/i}"

    "Il désigne les caméras."

    ryn desaccord "{i}Tout est automatisé.{/i} {i}Chaque conteneur.{/i} {i}Chaque camion.{/i} {i}Chaque anomalie.{/i} {i}Chaque mouvement.{/i}"

    pause 0.5

    ryn triste "{i}Alors quand Kami a proposé ces missions...{/i}"

    noam reflexion "{i}Tu t'es inscrit.{/i}"

    ryn "{i}Oui.{/i} {i}Au début, juste pour voir.{/i}"

    "Il ouvre l'historique."

    "Des dizaines de validations apparaissent."

    ryn reflexion "{i}Puis j'ai compris que le système faisait confiance aux contrôleurs humains pour une partie des décisions.{/i}"

    noam "{i}Et tu as commencé à laisser passer certains conteneurs.{/i}"

    ryn "{i}Ceux qui me semblent suspects pour les bonnes raisons.{/i}"

    noam reflexion "{i}Les bonnes raisons ?{/i}"

    ryn "{i}Une masse légèrement supérieure.{/i} {i}Une modification thermique.{/i} {i}Une trace sur un scellé.{/i} {i}Des choses qui peuvent vouloir dire qu'une personne est cachée à l'intérieur.{/i}"

    noam inquiet "{i}Tu peux savoir ça juste avec les images ?{/i}"

    ryn "{i}Pas toujours.{/i} {i}Mais après des années à travailler aux frontières...{/i}"

    "Il hausse légèrement les épaules."

    ryn fatigue "{i}Tu reconnais certains signes.{/i}"

    noam reflexion "{i}Et les conteneurs que tu marques pour destruction ?{/i}"

    ryn "{i}Ceux qui risquent réellement de tuer quelqu'un.{/i}"

    noam surpris "{i}Comment ça ?{/i}"

    ryn "{i}Conteneur frigorifique.{/i} {i}Ventilation défectueuse.{/i} {i}Produits chimiques.{/i} {i}Trajet trop long.{/i} {i}Si quelqu'un s'est caché dedans, il faut provoquer une inspection avant le départ.{/i}"

    noam "{i}Donc tu ne détruis pas vraiment le conteneur.{/i}"

    ryn "{i}Le statut oblige les équipes à le retirer de la ligne.{/i} {i}Il est ouvert avant destruction.{/i}"

    noam reflexion "{i}Et si quelqu'un est dedans ?{/i}"

    ryn "{i}Alors avec un peu de chance, il a le temps de partir avant que le signalement remonte plus haut.{/i}"

    "Je regarde l'écran autrement."

    "Chaque décision que je prenais pour une simple validation administrative ressemble soudain à autre chose."

    think "Il ne choisit pas des caisses. Il essaie de choisir qui a une chance de passer."

    noam "{i}C'est pour ça que tu posais toutes ces questions à Anya.{/i}"

    ryn "{i}Oui.{/i}"

    noam "{i}Tu voulais comprendre comment son réseau fonctionnait.{/i}"

    ryn "{i}Je voulais savoir quels signes le système pouvait détecter.{/i}"

    noam reflexion "{i}Pour mieux les masquer.{/i}"

    ryn "{i}Ou pour ne pas les signaler.{/i}"

    pause 0.6

    ryn triste "{i}Je peux pas rouvrir les frontières.{/i} {i}Je peux pas annuler ce que j'ai fait avant.{/i} {i}Mais ça...{/i}"

    "Il montre l'écran."

    ryn "{i}Ça, je peux le faire.{/i}"

    noam "{i}Ta façon de te rattraper.{/i}"

    ryn "{i}Appelle ça comme tu veux.{/i} {i}Moi j'appelle surtout ça arrêter d'être inutile.{/i}"

    "Un silence s'installe."

    "Puis Ryn ouvre une autre fenêtre."

    ryn reflexion "{i}Tu veux m'aider ?{/i}"

    noam surpris "{i}Quoi ?{/i}"

    ryn "{i}Les missions sont ouvertes à plusieurs personnes.{/i} {i}Je peux te montrer comment ça fonctionne.{/i}"

    noam "{i}Tu veux que je participe aux contrôles ?{/i}"

    ryn "{i}Pas aux contrôles.{/i}"

    "Il désigne le bouton de validation."

    ryn "{i}À ce qui passe entre.{/i}"

    noam reflexion "{i}...{/i}"

    ryn "{i}Plus nous sommes nombreux à traiter les dossiers, plus je peux couvrir de routes.{/i} {i}Et plus il devient difficile de voir qu'une seule personne valide systématiquement certains profils.{/i}"

    noam inquiet "{i}Si Kami comprend ce que tu fais...{/i}"

    ryn "{i}Je sais.{/i}"

    noam "{i}On risque quoi ?{/i}"

    ryn "{i}Je sais pas.{/i}"

    noam desaccord "{i}Très rassurant.{/i}"

    ryn "{i}Tu voulais la vérité.{/i}"

    "Il me regarde droit dans les yeux."

    ryn determine "{i}Je ne vais pas te mentir maintenant.{/i}"

    pause 0.5

    ryn "{i}Alors ?{/i}"

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Aider Ryn à faire passer des conteneurs ?"

        "Participer aux contrôles.":
            jump _10_1_0_0_AIDER_RYN

        "Ne pas participer.":
            jump _10_1_0_0_REFUSER_RYN


label _10_1_0_0_AIDER_RYN:

    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ showGroup([
        ("noam", "determine", 0.30),
        ("ryn", "reflexion", 0.70),
    ])

    noam determine "{i}D'accord. Je t'aide.{/i}"

    ryn surpris "{i}Tu es sûr ?{/i}"

    noam "{i}Non. Mais je préfère aider en sachant ce qu'on fait plutôt que faire semblant de ne rien voir.{/i}"

    "Ryn laisse échapper un léger rire."

    ryn fatigue "{i}Au moins, t'es honnête.{/i}"

    noam reflexion "{i}Je veux juste une règle.{/i}"

    ryn "{i}Laquelle ?{/i}"

    noam determine "{i}On ne joue pas avec la vie des gens.{/i} {i}Si un conteneur est réellement dangereux, on le fait ouvrir.{/i} {i}Même si ça signifie que quelqu'un risque d'être découvert.{/i}"

    ryn raison "{i}Évidemment.{/i}"

    noam "{i}Et si tu as un doute...{/i}"

    ryn "{i}Je bloque.{/i}"

    noam "{i}D'accord.{/i}"

    "Ryn déplace légèrement sa chaise et m'indique la place à côté de lui."

    ryn "{i}Alors assieds-toi.{/i}"

    noam gene "{i}Maintenant ?{/i}"

    ryn "{i}Tu pensais que la révolution attendait demain ?{/i}"

    noam sourire "{i}Dit comme ça...{/i}"

    "Je prends place."

    ryn raison "{i}Première règle : ne valide jamais uniquement à partir du poids.{/i} {i}Deuxième règle : regarde toujours la température.{/i} {i}Troisième règle...{/i}"

    "Je regarde les dizaines de dossiers qui attendent encore."

    think "Je suis vraiment en train d'aider des gens à franchir clandestinement les frontières."

    pause 0.5

    think "Il y a encore quelques jours, j'aurais probablement trouvé cette idée complètement folle."

    "Une fiche apparaît."

    "Limen."

    "Destination : Nexus."

    "Alerte mineure."

    "Ryn me regarde."

    ryn reflexion "{i}Celui-là ?{/i}"

    "Je me penche vers l'écran."

    noam reflexion "{i}Montre-moi.{/i}"

    $ ryn_border_help = True

    jump _10_1_0_0_SOIR


label _10_1_0_0_REFUSER_RYN:

    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("noam", "inquiet", 0.30),
        ("ryn", "reflexion", 0.70),
    ])

    noam inquiet "{i}Non. Je comprends pourquoi tu le fais, mais je ne veux pas participer directement.{/i}"

    "Ryn acquiesce immédiatement, sans chercher à discuter."

    ryn "{i}D'accord. Je vais pas essayer de te culpabiliser pour ça.{/i}"

    "Il revient vers son écran."

    noam reflexion "{i}Je comprends pourquoi tu le fais.{/i}"

    ryn "{i}Mais tu veux pas le faire toi-même.{/i}"

    noam "{i}Pas comme ça.{/i}"

    ryn reflexion "{i}Je comprends aussi.{/i}"

    noam "{i}Je dirai rien.{/i}"

    "Ryn s'arrête."

    ryn "{i}Même à Nyra ?{/i}"

    noam reflexion "{i}...{/i}"

    ryn "{i}Je demande pas une promesse.{/i}"

    noam "{i}Je vais réfléchir.{/i}"

    ryn "{i}Ça me va.{/i}"

    noam "{i}Et Anya ?{/i}"

    "Il se tourne légèrement vers moi."

    ryn raison "{i}Son secret reste un secret.{/i}"

    noam "{i}Merci.{/i}"

    ryn fatigue "{i}Ne me remercie pas.{/i}"

    "Il sélectionne une nouvelle fiche."

    ryn "{i}J'aurais dû commencer à faire ça bien avant.{/i}"

    $ ryn_border_help = False

    jump _10_1_0_0_SOIR


label _10_1_0_0_SOIR:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_5
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5

    "Lorsque je quitte finalement les archives, le Conclave est déjà beaucoup plus calme."

    "Je marche lentement vers ma chambre."

    think "Ce matin, je pensais surtout que Ryn cachait quelque chose. J'avais raison."

    "Je repense aux conteneurs."

    "Aux validations."

    "À tous ces numéros qui représentaient peut-être quelqu'un comme Anya."

    think "Je ne sais pas encore si ce qu'il fait est courageux ou complètement irresponsable. Probablement un peu des deux."

    "Je passe devant la chambre d'Iris."

    "Aucune voix."

    "Aucun bruit."

    think "Et demain, tout dépendra du vote."

    "Si une seule personne vote contre..."

    "Je regarde machinalement la caméra au bout du couloir."

    think "Plus de brouilleur. Plus de cachette. Plus d'Anya."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10_1_0_0_6
    scene bg_chambre at adaptive_fullscreen with fade

    "Je m'allonge sur le lit sans même allumer la lumière."

    think "Nyra doit convaincre Tomas. Elias. Tous les autres."

    pause 0.5

    think "Une seule voix. C'est tout ce qu'il faut pour tout foutre en l'air."

    "Je ferme les yeux."

    scene black with fade
    stop music fadeout 4.0

    call end_day("11") from _call_end_day_10100
    #jump _11_1_0_0_REVEIL

    jump patreon_ending
