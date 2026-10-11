# JOUR 27 — CEUX QUI N'EXISTENT PAS
# Branche secrète du J26 : Noam a pris la place de son Doppelgänger.
# Le vrai Noam reste dissimulé aux représentants ; Noam-DG maintient sa couverture.
# La découverte des archives ne prouve pas encore les conditions de vie sur Keyper-IIB.

default j27_secret_archive_read = []
default j27_secret_tomas_trust = 0
default j27_secret_vote_done = False
default j27_secret_report_seen = False

label _27_0_1_1_0_0_1_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"

    scene black
    play sound "audio/sfx_duct_scrape.wav" volume 0.30
    pause 0.4
    kami "Bonjour, chers représentants ! Petit rappel : le vote prévu aujourd'hui aura lieu à quatorze heures précises. Je compte sur votre ponctualité !"
    "Je sursaute et me redresse trop vite. Mon crâne heurte le renfort métallique au-dessus de moi."
    noam fatigue "Aïe... Putain."
    "J'ai dû m'endormir en attendant dans le conduit, quelques mètres après la grille du laboratoire. Ma lampe est toujours coincée contre mon sac."
    "Je regarde mon téléphone. Il est bien plus tard que je ne le pensais. Aucun message d'Iris."
    think "Et moi qui lui avais promis de revenir."
    "Je relis les derniers échanges. La conversation s'arrête au moment où je lui ai dit que j'étais encore dans ma chambre."
    "Si mon double a effectivement pris ma place, je ne sais pas ce qu'il a fait depuis. Je n'ai pas non plus le courage d'appeler Iris pour lui demander."
    "L'annonce de Kami se répète plus loin, étouffée par les parois."
    think "Quatorze heures. Je ne peux même pas aller voter."
    "Je récupère ma lampe, traverse le passage que mon double m'a montré hier et rejoins la grille du laboratoire."

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    "Tomas est penché sur un terminal. Elias examine plusieurs pièces détachées étalées devant lui. Ils relèvent à peine la tête à mon arrivée."
    $ showGroup([("tomas", "reflexion", 0.23), ("elias", "fatigue", 0.50), ("noam", "fatigue", 0.77)])
    elias fatigue "T'as une tête affreuse."
    noam fatigue "Merci. Toi aussi."
    elias neutre "Moi, j'ai travaillé toute la nuit. C'est quoi ton excuse ?"
    noam neutre "J'ai pas beaucoup dormi."
    tomas raison "Parfait. On sera trois à être d'une humeur détestable. Approche, on doit se mettre d'accord avant midi."
    "Je pose mon sac à côté de la table. Sur l'écran, Tomas a ouvert un plan du secteur des archives, avec plusieurs accès barrés en rouge."
    noam reflexion "T'as pu avancer ?"
    tomas fatigue "Pas assez. Les fichiers auxquels Kael a accès s'arrêtent au manifeste. Pour voir les rapports de transfert, il faut le terminal local."
    elias raison "Et le terminal local est derrière une porte qui enregistre chaque entrée."
    noam inquiet "Donc c'est mort ?"
    elias agace "Si c'était mort, on serait pas en train d'en parler."

    "Elias tourne son écran vers moi. Une liste de passages est annotée avec des horaires et des noms. Je reconnais le mien."
    elias raison "Ton original peut entrer dans ce secteur. Le souci, c'est qu'il y va parfois consulter les dossiers de votes. S'il débarque pendant qu'on fouille, on a l'air malins."
    "Je prends une seconde pour comprendre que, cette fois, le mot original me désigne."
    noam reflexion "Tu veux l'empêcher d'y aller ?"
    tomas raison "L'occuper, plutôt. On ne touche pas aux accès, on ne force aucune porte. On profite simplement du temps pendant lequel il est ailleurs."
    elias sourire "Je vais lui demander un coup de main à la maintenance. Je lui dirai que j'ai un problème sur un circuit et que j'ai besoin qu'il vienne tenir les outils."
    noam surpris "Il va accepter ?"
    elias neutre "Il accepte bien quand je lui demande de m'aider. Et s'il refuse, je trouverai autre chose."
    tomas reflexion "Il ne faut pas non plus que tu le gardes là-bas toute la matinée. Ça serait louche."
    elias raison "Une heure, une heure et demie. Le temps de faire les contrôles, de me plaindre du matériel et de démonter un panneau qui fonctionne très bien."
    noam reflexion "Et s'il veut savoir pourquoi tu l'as appelé ?"
    elias taquin "Je lui montrerai le panneau. Il aura largement assez de questions à me poser."
    "Je baisse les yeux sur l'écran pour cacher mon expression. Ils ne sont pas en train de préparer une attaque. Ils organisent une distraction pour quelqu'un qui possède mon visage."
    tomas raison "Moi, je passe aux archives. Noam, tu viens avec moi. Tu restes près de la porte, tu surveilles les accès et tu me préviens si quelqu'un approche."
    noam inquiet "Tu veux pas que je regarde les documents ?"
    tomas neutre "Si on trouve ce qu'on cherche, oui. Mais d'abord il faut y entrer sans se faire repérer. Je préfère qu'on évite de tout perdre à cause d'une imprudence."
    elias blase "Tomas qui parle d'imprudence. J'aurais aimé enregistrer ça."
    tomas agace "Tu préfères que je te laisse avec tes pièces détachées ?"
    elias rire "Non, non. Je vais sauver votre opération."

    "Elias commence à remettre les outils dans une caisse. Je le regarde ajuster une pièce qui n'a manifestement rien de cassé."
    noam reflexion "Attends. Tu vas vraiment démonter quelque chose pour le faire venir ?"
    elias neutre "Non. Je vais lui dire qu'il y a un souci, puis je lui montrerai les connexions. Il fera ses vérifications, je ferai les miennes, et on aura perdu une heure."
    tomas raison "Personne ne lui fait de mal. On a besoin qu'il puisse aller voter cet après-midi."
    "La remarque me rassure moins qu'elle ne devrait. Ils considèrent toujours mon existence comme un problème à gérer, mais aucun des deux ne paraît envisager de me frapper pour le résoudre."
    elias reflexion "Je pars maintenant. Vous me laissez dix minutes d'avance."
    noam neutre "Et si ça ne marche pas ?"
    elias neutre "Je t'envoie un message. Vous n'entrez pas aux archives."
    tomas raison "On fait comme ça."
    "Elias prend sa caisse et disparaît derrière la grille. Son pas résonne dans le conduit jusqu'à ce que je ne l'entende plus."
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "inquiet", 0.65)])

    "Tomas vérifie une dernière fois les autorisations. Je reste près de lui, sans savoir s'il attend que je pose une question."
    tomas reflexion "Tu as changé d'avis, au fait ?"
    noam inquiet "Sur quoi ?"
    tomas fatigue "Sur le remplacement. Mara m'a dit que t'avais encore esquivé le sujet hier."
    "Je prends appui contre la table. J'aurais préféré qu'il continue à regarder son écran."
    noam reflexion "J'ai pas envie d'en parler maintenant."
    tomas neutre "Très bien. Mais il va falloir que tu saches ce que tu veux avant le départ."
    noam raison "Tu trouves ça normal, toi ?"
    tomas surpris "Quoi ?"
    noam inquiet "Prendre la vie de quelqu'un pour pouvoir rentrer à sa place."
    "Il ferme le dossier qu'il était en train de consulter et me regarde enfin."
    tomas reflexion "Je trouve pas ça normal. Je trouve pas non plus normal qu'on nous ait créés pour qu'on nous dise ensuite qu'on n'a aucune place nulle part."
    noam raison "Ça donne pas le droit de tuer."
    tomas neutre "Je suis d'accord. Et ça ne crée pas des places supplémentaires dans la navette."
    "Il ne dit pas ça comme une provocation. Il ramène simplement le regard vers les autorisations, comme s'il s'agissait d'une difficulté de plus à résoudre."
    tomas fatigue "Pour le moment, essayons surtout de savoir où ils ont prévu de nous envoyer."
    "Le terminal émet un signal. Un message d'Elias apparaît."
    tomas raison "Il l'a trouvé. On y va."

    $ hideGroup()
    $ current_period = "Matin"
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je suis Tomas dans un passage que je n'ai jamais emprunté. Il avance rapidement, sans regarder derrière lui, et s'arrête à chaque embranchement pour vérifier l'écran de son téléphone."
    "Nous débouchons derrière une cloison de maintenance, dans un couloir presque aussi éclairé que ceux des dortoirs."
    noam reflexion "Tu connais tous ces passages ?"
    tomas neutre "Pas tous. J'ai surtout appris ceux qui permettent d'éviter de croiser la moitié du Conclave."
    "Il replace la plaque derrière nous. Pendant une seconde, je me demande combien de fois j'ai traversé ce secteur sans imaginer que quelqu'un circulait de l'autre côté du mur."
    $ flashlight_off()

    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Tomas passe sa tablette devant le lecteur. La porte s'ouvre après quelques secondes, suffisamment lentement pour que j'aie envie de regarder derrière nous."
    "La salle des archives est vide. Des terminaux sont encastrés dans les murs et une grande table sert à consulter les anciens dossiers."
    $ showGroup([("tomas", "raison", 0.37), ("noam", "reflexion", 0.66)])
    tomas raison "Reste là. Si quelqu'un approche, je veux le savoir avant qu'il ait la main sur la porte."
    noam neutre "Compris."
    "Il ouvre une session locale. Les mêmes manifestes qu'hier apparaissent, puis plusieurs dossiers que son écran du laboratoire refusait d'afficher."
    tomas reflexion "Ah. Là, c'est déjà mieux."
    noam inquiet "Tu vois quelque chose ?"
    tomas raison "Des transferts. Certains datent d'avant notre arrivée. Il y a plusieurs séries de numéros, et chaque série correspond à un lot différent."
    noam reflexion "Ils viennent tous du Conclave ?"
    tomas fatigue "Les fichiers disent origine : Conclave. Ça veut pas dire qu'ils ont été fabriqués ici, juste qu'ils y étaient au moment du transfert."
    "Il fait défiler la liste, s'arrête sur une date, puis ouvre une fiche individuelle."
    tomas neutre "Aucune identité. Aucun nom. Seulement un identifiant et un statut."
    noam inquiet "Quel statut ?"
    tomas reflexion "Unité biologique. Affectation de production."
    "Il ne dit plus rien pendant quelques secondes. J'entends seulement le système de ventilation au-dessus de la table."
    tomas fatigue "On les traite comme des machines."
    noam raison "Tu sais ce qu'ils doivent produire ?"
    tomas neutre "Non. Il me manque le dossier de fonctionnement de Keyper-IIB. Il y a bien un renvoi, mais pas d'accès depuis ce terminal."
    noam reflexion "Et les garanties du vote de l'autre jour ?"
    tomas raison "Le texte parle des personnes. Il faut savoir si Kami nous range dans cette catégorie. Pour l'instant, dans les registres, je trouve surtout des mots qui servent à éviter de nous appeler des personnes."
    "Il copie plusieurs pages vers son terminal personnel."
    tomas reflexion "Je vais garder les références. Si quelqu'un efface les fichiers, au moins on saura ce qu'on cherchait."
    "Mon téléphone vibre. Un message d'Elias s'affiche sur l'écran de Tomas."
    tomas neutre "Il est toujours à la maintenance. Mais le vote approche. On rentre."
    noam inquiet "T'as trouvé tout ce que tu voulais ?"
    tomas fatigue "Non. Justement. Je voulais être rassuré, et je repars avec davantage de questions."
    "Il referme sa session, vérifie que rien n'est resté ouvert sur le terminal et me fait signe de sortir."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Nous reprenons le même chemin. Tomas reste silencieux pendant presque tout le trajet. Quand nous arrivons près de la grille du laboratoire, j'entends sa tablette vibrer deux fois de suite."
    tomas reflexion "Kami vient de rappeler l'heure. Il faut que j'y aille."
    $ flashlight_off()
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"
    $ showGroup([("tomas", "inquiet", 0.36), ("noam", "reflexion", 0.65)])
    kami "Chers représentants, il est quatorze heures ! Veuillez rejoindre la salle du Conclave pour le vote prévu aujourd'hui."
    "Je relève la tête vers le haut-parleur. Pour la première fois, une annonce de vote me donne envie de me cacher."
    tomas neutre "Je vais rejoindre les autres. Toi, reste ici jusqu'à ce que ça soit terminé."
    noam surpris "Tu me laisses tout seul ?"
    tomas raison "Ton original est censé être à la salle du Conclave. Si quelqu'un voit deux Noam au moment du vote, on aura un problème un peu plus grave que les archives."
    noam reflexion "Et si on se demande où tu étais ce matin ?"
    tomas fatigue "Je dirai que je travaillais. Pour une fois, ce sera même vrai."
    "Il glisse sa tablette dans sa poche."
    tomas neutre "Ne touche pas au terminal principal. J'ai besoin de retrouver mes notes telles que je les ai laissées."
    noam raison "Je vais attendre."
    tomas reflexion "Et essaie de ne pas t'endormir. J'aimerais encore te parler de ce qu'on a trouvé."
    "Je le regarde repartir par le conduit. Quand sa voix s'éloigne, je suis enfin seul dans le laboratoire."
    $ hideGroup()

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je commence par faire le tour de la table. Plusieurs tasses ont été oubliées depuis hier, près d'un dossier ouvert et d'une pile de pièces démontées."
    "Sur le terminal secondaire, Tomas a laissé une copie des fichiers récupérés aux archives. Les noms des dossiers sont plus explicites que ceux que j'ai aperçus tout à l'heure."
    "Je pourrais rester à attendre son retour. Mais c'est précisément pour comprendre ce qu'ils cachent que j'ai accepté de venir ici."
    jump _27_0_1_1_0_0_1_DOCUMENTS


label _27_0_1_1_0_0_1_DOCUMENTS:
    menu:
        "Consulter le registre des transferts." if "transferts" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("transferts")
            "Je sélectionne le dossier intitulé TRANSFERTS EXTÉRIEURS. Une liste s'ouvre, longue de plusieurs dizaines de pages."
            "Chaque entrée comporte un identifiant, une date de départ, un lieu d'affectation et une case indiquant si le transfert a été confirmé."
            "Je cherche un nom. Il n'y en a aucun."
            "Les premières lignes mentionnent toutes le Conclave comme site d'origine. La destination est presque toujours la même : Keyper-IIB."
            "Une note précise que l'identification nominative n'est pas requise pour les unités biologiques."
            think "Il doit bien y avoir quelqu'un qui les attend quelque part."
            "Je referme le dossier après avoir relevé le numéro de trois transferts récents."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Lire la classification des Doppelgängers." if "statut" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("statut")
            "Le deuxième document définit les catégories d'occupants pris en compte dans les systèmes du Conclave."
            "Les représentants sont identifiés individuellement et rattachés à un ensemble de droits."
            "Les unités biologiques de duplication apparaissent dans une autre rubrique, avec des règles de stockage, de transfert et d'affectation."
            "Je relis le mot stockage. Il ne semble pas désigner des effets personnels."
            "Une référence au vote du jour vingt-quatre figure dans un champ annexe, mais aucune modification n'apparaît dans les conditions applicables aux unités."
            think "Le nouveau Commandement leur garantit-il quoi que ce soit ?"
            "Le texte ne le précise pas. Je note la référence, sans savoir si l'absence de réponse signifie un refus ou simplement un oubli."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Chercher des informations sur Keyper-IIB." if "keyper" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("keyper")
            "Je trouve un rapport ancien sur Keyper-IIB, composé d'analyses atmosphériques et d'estimations de température."
            "La planète possède plusieurs régions dans lesquelles une implantation humaine serait théoriquement possible. Les données proviennent de sondes et de relevés automatisés."
            "Plus bas, une section décrit l'existence d'une station de production, mais renvoie immédiatement vers un dossier classé."
            "Il n'y a aucune photographie de ses installations, aucun plan et aucune indication sur les conditions de vie des unités transférées."
            "Une mention revient plusieurs fois : productivité attendue."
            think "On parle de gens ou de machines ?"
            "Je consulte les coordonnées de l'installation, puis les copie sur ma tablette. Je suis incapable d'imaginer ce qui se trouve réellement là-bas."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Examiner les annotations personnelles de Tomas." if "notes" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("notes")
            "Un fichier n'a pas d'en-tête officiel. Il contient des commentaires que Tomas a ajoutés aux rapports."
            "Il a entouré plusieurs dates et comparé les transferts aux changements de procédure enregistrés par Kami."
            "Au milieu de ses calculs, je trouve une phrase : « Si nous ne sommes pas des personnes, que devient le droit de refuser ? »"
            "La ligne suivante propose de demander à Zero ce qu'il sait de la première série de transferts."
            "Il a également noté les noms de plusieurs autres Doppelgängers qui pourraient être concernés, sans prétendre savoir où ils se trouvent aujourd'hui."
            "Je referme le fichier. Tomas ne cherchait pas seulement à savoir si la navette allait l'emporter. Il essaie de retrouver des gens qu'il ne connaît même pas."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Arrêter la consultation.":
            if len(j27_secret_archive_read) < 2:
                "Je ferme un premier dossier, mais le terminal est encore ouvert sur les fichiers que Tomas a laissés."
                "Avant de partir, je devrais au moins vérifier si ces transferts concernent réellement des Doppelgängers."
                jump _27_0_1_1_0_0_1_DOCUMENTS
            jump _27_0_1_1_0_0_1_APRES_VOTE


label _27_0_1_1_0_0_1_APRES_VOTE:
    $ j27_secret_report_seen = True
    "Je referme le dernier fichier et remets le terminal dans l'état où je l'ai trouvé. Une nouvelle annonce de Kami se fait entendre au loin, mais elle ne concerne plus le vote."
    "J'attends plusieurs minutes devant la grille, puis retourne à la table. Les conversations de la veille me paraissaient presque ordinaires ; après ce que je viens de lire, je comprends mieux pourquoi Tomas avait du mal à rester calme."
    call show_custom_title("En fin d'après-midi") from _call_j27_secret_late_afternoon
    $ current_period = "Après-midi"
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.7
    "Je finis par entendre plusieurs personnes approcher dans le conduit. Une voix proteste parce que quelqu'un avance trop lentement, puis la grille s'ouvre."
    "Kael entre le premier, suivi de Mara et Sael. Ils ont encore leurs tablettes de vote à la main."
    $ showGroup([("kael", "sourire", 0.14), ("mara", "taquin", 0.35), ("sael", "neutre", 0.57), ("noam", "reflexion", 0.80)])
    mara taquin "Ah, il est là ! On a cru que t'avais finalement réussi à disparaître."
    noam neutre "J'attendais Tomas."
    sael reflexion "Il est pas encore rentré ?"
    noam neutre "Pas depuis qu'il est parti voter."
    kael calme "Il est resté discuter après le résultat. Il voulait savoir si le texte avait été interprété comme prévu."
    noam reflexion "Et ça s'est bien passé ?"
    mara rire "Ton original a encore fait son numéro. Je sais pas ce qui lui prend, mais il devient presque convaincant."
    "Je me redresse."
    noam inquiet "Mon original ?"
    mara taquin "Non, l'autre Noam qu'on garde dans une caisse. Évidemment ton original."
    sael neutre "Il a été très bon, en réalité. Il a repris une objection de Nyra sans la ridiculiser et il a trouvé un compromis sur la formulation."
    kael sourire "Même Julian a fini par le remercier. Ça arrive pas tous les jours."
    "Je les écoute parler de ma propre intervention au Conclave. Je n'étais même pas dans la salle."
    think "C'est lui. C'est mon double qui a parlé à ma place."
    noam reflexion "Il a dit quoi, exactement ?"
    sael reflexion "Tu veux vraiment une retranscription ?"
    noam neutre "Je veux juste savoir comment il s'en est sorti."
    kael calme "Il a laissé les autres parler, puis il a repris leurs arguments. Il avait l'air de savoir à quel moment intervenir. Le vote a pu avoir lieu sans qu'on y passe la soirée."
    mara rire "Je crois surtout qu'Iris était prête à lui donner raison avant même qu'il ouvre la bouche."
    "Je relève les yeux vers elle."
    noam inquiet "Pourquoi tu dis ça ?"
    mara taquin "Parce qu'elle le regardait tout le temps. Et lui, il arrêtait pas de se tourner vers elle."
    kael sourire "Ils ont discuté tous les deux après le vote. Ça avait l'air important."
    sael neutre "Je les ai vus revenir ensemble vers les dortoirs. Ils avaient plutôt l'air de bonne humeur."
    mara rire "Bonne humeur ? Elle lui a même pris le bras pour l'emmener à l'écart. T'aurais dû voir la tête de Julian."
    noam colere "Ils ont fait quoi après ?"
    "Le rire de Mara s'arrête. Elle me regarde comme si elle avait raté une étape."
    mara reflexion "J'en sais rien. On est venus ici. Pourquoi ?"
    noam fatigue "Pour rien."
    mara taquin "Attends... Tu serais pas jaloux de ton propre original ?"
    kael surpris "Mara..."
    mara rire "Quoi ? C'est quand même un peu drôle !"
    "Je détourne les yeux. Elle a raison sur un point : j'ai envie de savoir ce qu'ils ont fait ensemble, et je n'ai aucun moyen de le demander sans me trahir."
    "Iris ne savait pas que mon double devait prendre ma place au vote. Elle l'a peut-être remercié, conseillé, ou simplement suivi parce qu'elle pensait que c'était moi."
    "L'idée qu'il ait pu lui dire quelque chose que j'aurais dû lui dire moi-même me serre la gorge."
    noam raison "Elle a pas l'air de se méfier de lui, alors."
    sael reflexion "Pourquoi elle devrait ? À part ses journées un peu compliquées, il n'a pas fait grand-chose pour attirer ses soupçons."
    "Je repense à la photo. Si Iris découvre que celui qu'elle a suivi dans les dortoirs n'est pas celui qu'elle croit, je ne suis pas certain qu'elle me pardonnera de l'avoir laissée seule avec lui."
    mara sourire "En tout cas, j'ai trouvé ça mignon."
    noam agace "Tu peux passer à autre chose ?"
    mara rire "Ah, ça y est, je t'ai retrouvé."
    kael calme "Laisse-le un peu tranquille. On attend surtout de savoir ce que Tomas a appris ce matin."
    "Sael pose sa tablette sur la table et consulte les derniers résultats du vote."
    sael raison "La séance a été suffisamment longue. Ce serait bien d'avoir enfin quelque chose de concret à discuter."
    "Ils s'installent. Mara finit par me tendre une bouteille d'eau et me demande si j'ai mangé. Je réponds que oui, même si mon ventre me rappelle le contraire."

    play sound sfx_creak volume 0.35
    "Un bruit dans le conduit nous interrompt. Elias descend en portant sa caisse à outils. Tomas arrive derrière lui, une tablette serrée contre sa poitrine."
    $ showGroup([("kael", "calme", 0.07), ("mara", "reflexion", 0.21), ("sael", "neutre", 0.35), ("elias", "fatigue", 0.49), ("tomas", "raison", 0.63), ("noam", "reflexion", 0.78)])
    elias fatigue "Je crois que j'ai passé assez de temps à dévisser des panneaux pour toute la semaine."
    mara taquin "Et ton problème imaginaire ?"
    elias neutre "Réparé, forcément. Il était très motivé pour m'aider."
    "Je me demande si c'est Noam-DG qu'il vient de retenir, et ce que mon double a pensé de cette mise en scène organisée autour de lui."
    tomas raison "Bon. On a trouvé les manifestes et une partie des dossiers de transfert. Pas tout, mais suffisamment pour qu'on arrête de se raconter que Keyper est peut-être une simple station de repos."
    kael inquietude "Ils y envoient vraiment des Doppelgängers ?"
    tomas neutre "Oui. Les listes sont anciennes, et il y a d'autres transferts prévus. Ça ne concerne pas seulement ceux qui restent ici après la navette."
    sael reflexion "Et leur statut ?"
    tomas raison "Unités biologiques. Dans les documents que j'ai pu ouvrir, ils ne sont jamais désignés comme des personnes."
    mara colere "C'est une blague ?"
    elias neutre "J'ai regardé les mêmes références. Le système fait une différence entre un représentant enregistré et une unité de duplication."
    kael inquietude "Donc le vote sur les besoins fondamentaux..."
    tomas fatigue "Je ne peux pas affirmer qu'il ne s'applique pas à nous. Mais je n'ai trouvé aucune trace qui permette d'affirmer le contraire."
    "Il sort une copie du manifeste et l'affiche sur l'écran central. Une longue colonne de numéros apparaît."
    sael mefiant "On ne sait toujours pas ce qu'on leur demande de produire."
    tomas raison "Non. Le dossier sur la station est classé, et personne ici n'a le droit d'y accéder."
    mara raison "Zero pourrait peut-être nous aider à l'ouvrir."
    tomas neutre "C'est prévu. Je compte lui envoyer les références et lui demander ce qu'il sait des premiers transferts."
    kael calme "Je lui ai déjà parlé de Keyper, mais il n'avait pas les numéros de dossier. Avec ça, il pourra au moins vérifier si on parle du même endroit."
    noam reflexion "Et si on découvre qu'ils travaillent là-bas contre leur volonté ?"
    tomas raison "Alors il faudra le prouver. Je ne vais pas envoyer tout le monde se battre contre Kami sur la base d'un mot dans un formulaire."
    mara colere "Tu voudrais attendre qu'ils nous expédient là-bas pour commencer à réagir ?"
    tomas agace "Non, Mara. Je voudrais savoir de quoi on parle avant de prendre une décision qu'on ne pourra pas annuler."
    mara raison "Mais s'ils sont comme nous, tu crois vraiment qu'ils peuvent refuser un ordre de Kami ?"
    elias reflexion "Techniquement, ils peuvent peut-être désobéir. Le problème, c'est ce que le système fait quand ils désobéissent."
    sael raison "Il nous manque aussi les conditions de vie, les soins, la durée des affectations. Les documents de transport ne répondent à aucune de ces questions."
    kael inquietude "Ça fait beaucoup de choses qu'on ignore."
    tomas fatigue "C'est exactement ce que je vous dis depuis ce matin."

    "La discussion repart sur le vote du jour vingt-quatre. Tomas maintient qu'il aurait préféré s'abstenir tant qu'ils ne connaissaient pas leur statut. Sael lui rappelle qu'ils n'avaient aucune raison de soupçonner l'existence de Keyper à ce moment-là."
    sael reflexion "Tu ne peux pas reprocher aux autres de ne pas avoir deviné ce que tu viens seulement de découvrir."
    tomas neutre "Je ne leur reproche rien. J'avais une mauvaise intuition, pas une preuve."
    mara agace "Et maintenant qu'on en a une partie, tu voudrais quoi ?"
    tomas raison "Qu'on arrête de se cacher derrière l'idée que tout ira bien une fois la navette partie. Ce problème existera encore demain, et il existera sur Keyper même si nous arrivons tous à rejoindre la Terre."
    kael calme "Zero ne compte pas abandonner ceux qui sont là-bas."
    noam reflexion "Tu en es sûr ?"
    kael neutre "Il nous en a déjà parlé. Mais c'est à lui d'expliquer ce qu'il envisage réellement."
    "Mara me regarde, étonnée par la question. Je fais semblant de lire la liste sur l'écran."
    elias fatigue "La priorité, c'est d'obtenir le dossier de production. Sans ça, on peut passer la nuit à débattre, on saura toujours pas ce qu'il y a sur cette planète."
    sael raison "Et pendant ce temps, les représentants votent des règles qui ne mentionnent même pas notre existence."
    "Personne ne répond immédiatement. Tomas change de page et revient sur la classification des unités."
    tomas reflexion "Ce qui m'inquiète le plus, c'est pas seulement le transfert. C'est la manière dont ils parlent de nous. Si une règle ne nous reconnaît pas comme des personnes, comment on peut demander qu'elle nous protège ?"
    mara triste "Je savais que Kami nous aimait pas beaucoup, mais là..."
    elias neutre "Kami n'a pas besoin de nous détester pour nous traiter comme du matériel."
    "Je relève les yeux. Elias ne cherche pas à provoquer qui que ce soit. Il vient seulement de dire une chose qui semble évidente à tous les autres."
    noam raison "Ça ne vous dérange pas, de parler de tout ça alors qu'on a pris la place de quelqu'un ?"
    "Mara pose sa bouteille. Tomas me regarde par-dessus son écran."
    mara reflexion "Évidemment que ça me dérange. Tu crois que j'arrive à oublier ce qui s'est passé ?"
    noam inquiet "Alors comment tu fais pour continuer ?"
    mara fatigue "Je fais ce que je peux. Je me lève, je vois les autres, j'essaie d'éviter d'y penser toute la journée. C'est pas très glorieux comme réponse, mais j'en ai pas de meilleure."
    sael mefiant "On peut reconnaître les choses qu'on a faites sans décider qu'on ne mérite plus de vivre."
    tomas neutre "Et ça ne nous donne pas le droit de recommencer. Si c'est ça que tu veux me faire dire, je te le dis volontiers."
    "Je regarde leurs visages. Personne n'a cherché à prétendre que le corps de Mara n'existait pas. Personne n'a non plus proposé de réparer ce qui a été fait."
    "Je comprends qu'ils ont peur pour ceux de Keyper. Je ne sais toujours pas comment concilier cette peur avec ce qu'ils ont fait aux originaux."

    "La conversation se poursuit encore un moment. Tomas distribue les références des archives, Elias propose d'essayer un autre accès et Sael rappelle qu'une liste de transferts n'est pas un rapport médical."
    "Au bout d'un moment, Mara s'étire et annonce qu'elle ne supporte plus de regarder des colonnes de chiffres."
    mara taquin "Je vote pour qu'on mange quelque chose avant d'essayer de sauver l'univers."
    elias blase "On a déjà voté aujourd'hui."
    mara agace "Très drôle."
    "Kael se lève pour l'aider à débarrasser la table. Sael reste avec Tomas devant le terminal, tandis qu'Elias vérifie une dernière fois sa caisse."
    "Je profite du mouvement pour reprendre mon téléphone."
    "Toujours aucun message d'Iris. Si je veux savoir ce que mon double lui a raconté, il faudra que j'aille lui demander en personne."
    "Mais en regardant les fichiers que Tomas a laissés ouverts, je réalise que j'ai désormais une autre question, tout aussi urgente."
    think "Qu'est-ce que Kami fait à ceux qu'elle envoie sur Keyper-IIB ?"
    "Je ne peux pas oublier le corps de Mara. Je ne peux pas non plus faire comme si les autres n'avaient pas peur pour leurs semblables."
    "Et demain, il faudra revenir ici, leur parler encore, sans leur montrer que j'ai entendu bien plus que ce qu'ils croient."
    $ hideGroup()
    stop music fadeout 1.5
    call end_day("28", sleeping=True) from _call_j27_secret_end_day_28
    # Route secrète du J28 à poursuivre dans 28_0_1_1_0_0_1.rpy.
    return
