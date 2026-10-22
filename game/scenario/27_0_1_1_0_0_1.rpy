# JOUR 27 — CEUX QUI N'EXISTENT PAS
# Route secrète : Noam est pris pour son double ; Noam-DG joue l'original.
# Keyper-IIB : présence de vie confirmée ; existence d'une « station de production ».
# Aucun détail sur la production ou les conditions de vie n'est encore connu.

default j27_secret_archive_read = []
default j27_secret_tomas_trust = 0
default j27_secret_vote_done = False
default j27_secret_report_seen = False
default j27_secret_alarm_choice = None

default j27_secret_iris_doubt = False

label _27_0_1_1_0_0_1_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"
    $ j27_secret_archive_read = []
    $ j27_secret_tomas_trust = 0
    $ j27_secret_vote_done = False
    $ j27_secret_report_seen = False
    $ j27_secret_alarm_choice = None
    $ j27_secret_iris_doubt = False

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bonjour, chers représentants ! Votre vote est prévu aujourd'hui à quatorze heures. Essayez de ne pas vous faire attendre !"
    scene black with dissolve
    play sound "audio/sfx_duct_scrape.wav" volume 0.30
    "Je me redresse d'un coup et cogne ma tête contre une barre métallique."
    noam fatigue "Aïe... Merde."
    "Je suis toujours dans le conduit, près du laboratoire. J'ai dû m'endormir ici, avec ma lampe contre la poitrine."
    "Sur mon téléphone, la conversation avec Iris s'arrête à hier. Aucun nouveau message."
    think "Je lui ai dit que je revenais. C'est mon double qui a dû rentrer à ma place."
    "Je pourrais lui écrire. Mais s'il a mon téléphone, ou si elle est avec lui, une simple question suffirait à tout faire déraper."
    "Je rampe jusqu'à la grille du laboratoire."
    think "Les autres doivent être là-bas..."

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    $ showGroup([("tomas", "reflexion", 0.22), ("elias", "fatigue", 0.49), ("noam", "fatigue", 0.78)])
    elias fatigue "Ah, le voilà. Je commençais à croire qu'il t'était arrivé quelque chose'."
    noam fatigue "J'ai passé la nuit dans les conduits. Franchement, je le recommande vraiment pas."
    elias reflechit "Hein ? Mais pourquoi t'as pas été pioncé dans sa chambre ?"
    elias raison "Tu n'avais pas dis qu'il dormait dans la chambre à Iris maintenant ? Pourquoi t'y es pas retourné ?"
    noam peur "... Hein ? Euh..."
    noam reflechit "Ouais je sais pas trop, j'y ai pas vraiment pensé..."
    tomas raison "Tu dormiras mieux ce soir. Là, on a pas vraiment le temps pour ça, on a un fenêtre assez courte pour consulter les archives."
    noam reflexion "Vous avez trouvé quelque chose d'intéressant ?"
    tomas neutre "Pas encore. Va falloir aller dans la salle des archives pour chercher des informations sur Keyper-IIB."
    elias raison "Et surtout va falloir faire gaffe à ce que ton original débarque pas. Il pourrait très bien s'y pointer sans prévenir."
    "Je mets une seconde à comprendre qu'ils parlent de moi. Chaque fois qu'ils prononcent « ton original », j'ai envie de me retourner pour vérifier qu'ils ne m'ont pas reconnu."
    noam inquiet "Vous voulez faire quoi de lui...?"
    elias sourire "Je vais lui demander de venir bricoler avec moi. Ça devrait l'occuper une bonne heure."
    tomas raison "Ouais. Pas de violence et pas de remplacement improvisé."
    "Il dit ça en vérifiant les accès sur son écran, comme s'il parlait de déplacer une caisse."
    "Je reste silencieux. Eux savent ce qu'ils ont fait pour être ici."
    tomas raison "Tu as réfléchis pour ton original depuis hier ?"
    noam inquiet "N-Non. Pourquoi...?"
    tomas neutre "Il faut qu'on décide ce qu'il adviendra de lui. Si tu veux prendre sa place au départ, on ne pourra pas éviter cette conversation éternellement."
    noam agace "... Mais on ne-"
    elias colere "Ouais, on sait très bien ce que tu en penses. On te comprends tu sais... Mais..."
    tomas triste "Si tu veux vraiment monter dans cette navette, tu n'as pas vraiment le choix..."
    tomas reflechit "Sinon, tu finiras sur Keyper. En tout cas vraisemblablement..."
    noam colere "STOP ! Je préfère qu'on arrête de parler comme si sa vie était un programme qu'on devait régler !"
    "Elias repose lentement son tournevis. J'ai parlé trop vite."
    elias triste "Wow excuse ! On savait que ça te dérangeait, mais pas à ce point-là..."
    tomas neutre "D'accord, d'accord. Je ne te force à rien mais il va falloir y réflechir."
    tomas reflechit "Et vite avant que Mara décide de vraiment passer à l'action."
    "Je regarde le sol. Si je réponds que je ne veux pas partir, je vais devoir expliquer pourquoi."
    noam fatigue "Je sais pas encore. C'est justement pour ça que j'ai besoin de comprendre ce que c'est vraiment que cette exoplanète là."
    tomas raison "Oui, c'est vrai que ça m'intrigue aussi énormément."
    "Le téléphone d'Elias vibre."
    elias neutre "Bon. Je vais chercher ton original. Je vous préviens dès qu'il est à la maintenance."
    $ hideGroup()
    "Il emporte sa caisse d'outils et ressort par la grille. Tomas reste devant son écran sans rien dire pendant plusieurs secondes."
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "inquiet", 0.65)])
    tomas fatigue "Tu sais, je ne t'en veux pas de trouver ça insupportable."
    noam reflexion "Quoi ?"
    tomas raison "Prendre la place de quelqu'un. On fait comme si c'était logique, parce que sinon certains d'entre nous ne supporteraient même plus de se regarder dans une glace."
    tomas triste "Mais... Ouais... C'est pas une situation simple à vivre..."
    "Je pensais trouver des gens prêts à tout pour tuer leurs doubles. C'est plus compliqué. Et, quelque part, c'est encore plus difficile à supporter."
    "Un signal retentit sur sa tablette."
    tomas raison "Elias l'a avec lui. On y va. Et Noam... si tu ne veux vraiment pas le remplacer, il faudra le dire aux autres. Pas seulement à moi."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je suis Tomas dans les conduits. À deux reprises, il s'arrête pour écouter derrière une grille. Chaque bruit me paraît beaucoup trop proche."
    noam reflexion "Le terminal ne signale pas les entrées ?"
    tomas neutre "Si. Mais ma tablette dispose d'une autorisation pour consulter la salle. Ce qu'on ne peut pas justifier, c'est d'y croiser un représentant."
    noam inquiet "Et si Kami regarde les caméras ?"
    tomas fatigue "Alors elle sait déjà qu'on est là. On va surtout éviter de lui donner une raison de venir poser des questions."
    "Nous sortons derrière un panneau technique."
    $ flashlight_off()
    scene bg_archive at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "raison", 0.37), ("noam", "inquiet", 0.66)])
    "Tomas présente sa tablette au lecteur. La porte s'ouvre et se referme derrière nous."
    tomas raison "Tu gardes un œil sur les accès. Je cherche les dossiers. Si quelqu'un arrive, tu me le dis, même si t'es pas sûr."
    noam neutre "Compris."
    "Sur l'écran, plusieurs registres apparaissent. Tomas remonte des lignes de dates, puis s'arrête."
    tomas surpris "Attends... Il y a une mise à jour automatique qui date de ce mois-ci."
    noam reflexion "Sur Keyper ?"
    tomas raison "Oui. Le dossier confirme une activité biologique en surface. Ce n'est pas une projection de sonde : il y a déjà de la vie là-bas."
    noam surpris "Des gens ?"
    tomas neutre "C'est écrit « présence de vie confirmée ». Pas qui, pas combien. Je refuse d'inventer le reste."
    "Il ouvre un second fichier."
    tomas reflexion "Et là... « station de production ». C'est tout. La rubrique qui devrait expliquer la fonction de l'installation est verrouillée."
    noam inquiet "Production de quoi ?"
    tomas agace "J'en sais rien. Je cherche."
    "Il essaie un autre onglet. Une notification apparaît en haut de l'écran."
    tomas inquiet "Merde. Quelqu'un vient de demander l'ouverture du couloir des archives."
    noam surpris "Mon original ?"
    tomas neutre "Je n'ai pas le nom. Elias le retient peut-être encore. Il faut fermer la session."
    "Un second signal. Cette fois, une lumière orange clignote au-dessus de la porte."
    tomas raison "Je peux sauvegarder une copie des références, mais ça prendra quelques secondes. À toi de voir : on part tout de suite, ou tu surveilles pendant que je termine."
    menu:
        "Lui demander de tout arrêter et partir immédiatement.":
            $ j27_secret_alarm_choice = "prudence"
            $ j27_secret_tomas_trust += 1
            noam inquiet "On sort. Maintenant. S'ils nous trouvent ici, les références ne serviront à rien."
            tomas reflexion "T'as raison. Je garde ce que j'ai déjà noté."
            "Il ferme la session. Nous gagnons l'accès technique au moment où un bruit de pas résonne dans le couloir."
        "Lui laisser quelques secondes pour enregistrer les références.":
            $ j27_secret_alarm_choice = "risque"
            noam determine "Enregistre-les. Je regarde la porte."
            tomas raison "Dix secondes. Après, on part quoi qu'il arrive."
            "Je fixe le voyant orange. Des pas approchent, s'arrêtent, puis reprennent."
            "Tomas copie le numéro du dossier et ferme la session à la dernière seconde."
            tomas fatigue "C'est bon. Bouge !"
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Nous regagnons le conduit sans parler. Tomas attend d'avoir replacé la plaque pour souffler."
    $ showGroup([("tomas", "fatigue", 0.35), ("noam", "inquiet", 0.65)])
    noam inquiet "C'était qui ?"
    tomas neutre "Aucune idée. Et ça ne me plaît pas."
    if j27_secret_alarm_choice == "risque":
        tomas raison "Au moins, j'ai le numéro de référence complet. On pourra vérifier d'où vient ce dossier."
        noam fatigue "J'ai vraiment cru qu'on allait se faire prendre."
    else:
        tomas raison "J'ai l'essentiel : la confirmation de vie et cette histoire de station. Pour le reste, il faudra revenir."
        noam reflexion "Tu crois que quelqu'un nous a vus ?"
    tomas fatigue "On ne le saura pas en restant ici."
    $ hideGroup()
    $ flashlight_off()

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "reflexion", 0.36), ("noam", "inquiet", 0.65)])
    "Tomas pose sa tablette sur la table. Il regarde plusieurs fois l'heure."
    tomas raison "Je dois rejoindre le Conclave. Tu restes ici pendant le vote."
    noam inquiet "Et si mon original vient ?"
    tomas neutre "Il sera au vote, normalement. Et tu connais la sortie vers le conduit."
    noam reflexion "Tu pourrais lui demander ce qu'il a fait hier soir ?"
    tomas surpris "À ton original ? Pourquoi ?"
    "Je sens mes joues chauffer. Je ne peux pas lui parler d'Iris sans devoir expliquer que je suis celui qui devrait être à sa place."
    noam fatigue "Laisse tomber."
    tomas raison "Je te laisse le terminal secondaire. J'y ai déposé ce qu'on a pu consulter. Pas touche au principal, d'accord ?"
    noam neutre "D'accord."
    $ hideGroup()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Chers représentants, il est quatorze heures ! Le vote va commencer. Rejoignez vos places, s'il vous plaît !"
    $ j27_secret_vote_done = True
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Tomas repart. Je reste seul. Quelque part dans la station, mon double est assis sur ma chaise, face à Iris."
    think "Et si elle trouvait qu'il la comprend mieux que moi ?"
    "Je chasse cette pensée et ouvre les copies laissées par Tomas."
    jump _27_0_1_1_0_0_1_DOCUMENTS

label _27_0_1_1_0_0_1_DOCUMENTS:
    menu:
        "Consulter les registres de transfert." if "transferts" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("transferts")
            "Je déroule des listes d'expéditions entre le Conclave et Keyper-IIB. Chaque entrée possède une date et un numéro de dossier, mais aucun nom."
            "Je n'arrive pas à savoir si les passagers étaient volontaires. Rien ne l'indique. Rien ne dit non plus qu'ils ont été forcés."
            think "On peut effacer toute une vie derrière une ligne de registre."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Examiner la classification des Doppelgängers." if "statut" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("statut")
            "Les représentants sont enregistrés individuellement. Une autre catégorie, appelée « unités biologiques de duplication », apparaît dans les règles de transfert."
            "Les textes qui définissent les droits des représentants n'y sont pas repris. Je cherche une mention du vote du jour vingt-quatre ; un renvoi apparaît, mais sans explication."
            think "Est-ce que les Commandements protègent les êtres que Kami refuse d'appeler des personnes ?"
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Ouvrir la fiche de Keyper-IIB." if "keyper" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("keyper")
            "Une fiche de suivi confirme la présence de vie sur Keyper-IIB. Les données sont récentes et ne parlent pas d'une simple possibilité d'implantation."
            "Sous la rubrique INSTALLATIONS, je ne trouve qu'une appellation : « station de production ». Le reste est inaccessible depuis cette copie."
            "Aucun plan, aucune image exploitable, aucune description de ce qui est produit."
            think "Il y a de la vie là-bas. Mais qu'est-ce qu'ils ont construit au milieu de tout ça ?"
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Lire les annotations de Tomas." if "notes" not in j27_secret_archive_read:
            $ j27_secret_archive_read.append("notes")
            "Une note de Tomas revient sans cesse sur le même problème : une règle qui protège les représentants protège-t-elle aussi ceux qui sont classés autrement ?"
            "Plus bas, il a écrit : « Demander à Zero ce qu'il sait de Keyper. Ne rien conclure avant d'avoir les documents complets. »"
            "Je repense à la manière dont il a parlé de mon remplacement. Il doute de beaucoup de choses, mais il n'a pas l'air de douter de son droit à continuer de vivre."
            jump _27_0_1_1_0_0_1_DOCUMENTS
        "Arrêter la consultation.":
            if len(j27_secret_archive_read) < 2:
                "Je m'apprête à fermer le terminal. Je n'ai presque rien lu et je risque de revenir devant les autres sans savoir de quoi ils parlent."
                jump _27_0_1_1_0_0_1_DOCUMENTS
            jump _27_0_1_1_0_0_1_APRES_VOTE

label _27_0_1_1_0_0_1_APRES_VOTE:
    $ j27_secret_report_seen = True
    "Je ferme les fichiers. Les minutes passent. J'ai le réflexe de regarder mon téléphone, encore et encore. Iris ne m'a rien écrit."
    call show_custom_title("En fin d'après-midi") from _call_j27_secret_late_afternoon
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.7
    "Des voix approchent par le conduit. Je range mon téléphone juste avant que Kael, Mara et Sael n'entrent."
    $ showGroup([("kael", "sourire", 0.14), ("mara", "taquin", 0.35), ("sael", "neutre", 0.57), ("noam", "reflexion", 0.80)])
    mara sourire "T'es encore là ? Je pensais que t'aurais fini par te sauver."
    noam neutre "Tomas m'a demandé de l'attendre."
    sael reflexion "Il n'est pas rentré ?"
    noam neutre "Pas encore. Le vote s'est bien passé ?"
    kael calme "Oui. Ton original a même réussi à mettre tout le monde d'accord sur une formulation."
    mara rire "J'aurais pas cru dire ça un jour, mais il a été plutôt bon."
    "Je fixe Mara. Ils sont en train de féliciter un autre homme d'avoir réussi mon propre vote."
    noam inquiet "Et Iris ?"
    mara taquin "Iris ? Ah, elle était ravie. Elle lui a attrapé le bras après la séance pour l'emmener discuter."
    noam surpris "Elle l'a emmené où ?"
    sael reflexion "Vers les dortoirs, je crois. Pourquoi ?"
    noam fatigue "Pour rien. Je pensais qu'elle lui poserait des questions sur le vote."
    mara sourire "Ben oui, sûrement. T'as peur qu'elle finisse par préférer ton original ?"
    "Je voudrais répondre que c'est ridicule. Le problème, c'est que je ne le trouve pas ridicule du tout."
    noam agace "Tu peux arrêter ?"
    mara reflexion "Oh. D'accord. Je plaisantais."
    kael calme "Mara, laisse-le."
    "Je baisse les yeux. Iris croit avoir passé la journée avec moi. Et moi, je suis ici à écouter des inconnus discuter de ce qu'on pourrait faire de mon existence."
    sael neutre "En tout cas, il n'a rien dit qui laisse penser qu'il soupçonne quelque chose."
    noam inquiet "Qu'est-ce que tu veux dire ?"
    sael reflexion "Que ton original continue sa vie. C'est plutôt une bonne nouvelle pour toi, non ?"
    "Je serre le bord de la table. Une bonne nouvelle. Tant qu'il ne soupçonne rien, ils peuvent décider quand et comment il disparaîtra."
    mara fatigue "Bon, puisqu'on en parle... tu comptes faire quoi, au juste ? On ne peut pas attendre la veille du départ pour se demander si tu montes dans la navette."
    noam agace "Vous pourriez me laisser réfléchir cinq minutes sans me rappeler que quelqu'un doit prendre une décision sur sa vie ?"
    mara surpris "Je te demande ce que toi tu veux faire, Noam. Pas de choisir sa mort sur un formulaire."
    noam inquiet "Et si je dis que je ne veux pas le remplacer ?"
    "Mara ouvre la bouche, puis la referme."
    mara reflexion "Alors il faudra trouver autre chose. Mais je te promets pas que ce sera simple."
    sael raison "Personne ici ne devrait te forcer à franchir cette limite. Par contre, il faut qu'on en parle ensemble."
    "Le mot « ensemble » me fait froid dans le dos. Je voudrais savoir si Mara accepterait aussi facilement qu'on laisse son original repartir à sa place."
    play sound sfx_creak volume 0.35
    "La grille grince. Elias arrive avec sa caisse à outils, suivi de Tomas."
    $ showGroup([("kael", "calme", 0.07), ("mara", "reflexion", 0.21), ("sael", "neutre", 0.35), ("elias", "fatigue", 0.49), ("tomas", "raison", 0.63), ("noam", "inquiet", 0.78)])
    elias fatigue "Plus jamais je lui demande de vérifier un panneau. Il a voulu tester chaque connexion."
    noam inquiet "Il s'est douté de quelque chose ?"
    elias neutre "Pas à ma connaissance. Il m'a surtout demandé pourquoi un circuit qui fonctionnait hier avait besoin de moi aujourd'hui."
    tomas raison "On a plus important. Les archives confirment une chose : Keyper-IIB n'est pas un monde désert. Il y a déjà de la vie là-bas."
    kael surpris "De la vie ? Tu parles de quoi exactement ?"
    tomas neutre "C'est justement ce qu'on ne sait pas. Le document confirme une présence biologique, sans la décrire. Je ne vais pas vous raconter qu'il s'agit de gens comme nous."
    mara reflexion "Et les transferts ?"
    tomas raison "Ils existent. Leur destination comporte une installation désignée comme « station de production ». Aucun autre détail accessible."
    sael inquiet "Production de quoi ?"
    tomas fatigue "Aucune idée. Le dossier de fonctionnement est verrouillé."
    elias reflexion "On a aussi un problème de classification. Dans certains registres, les Doppelgängers ne sont pas enregistrés comme des représentants."
    kael inquietude "Donc la protection votée au jour vingt-quatre pourrait ne pas nous concerner ?"
    tomas raison "Elle pourrait nous concerner. Ou pas. Les documents ne permettent pas de trancher et je refuse qu'on présente une inquiétude comme une certitude."
    mara agace "Ça te rassure, toi, qu'on soit réduits à une catégorie dans leur système ?"
    tomas neutre "Non. Mais si on veut contester ça, il nous faut comprendre exactement ce que Kami a prévu."
    sael raison "Est-ce qu'on peut obtenir le dossier auprès de Zero ?"
    kael calme "Je peux le contacter. S'il connaît cette installation, il saura peut-être où chercher."
    noam reflexion "Et s'il vous disait de laisser tomber ? Vous le feriez ?"
    "Tous les regards se tournent vers moi."
    kael surpris "Pourquoi il nous dirait ça ?"
    noam inquiet "J'en sais rien. J'essaie de comprendre jusqu'où vous êtes prêts à aller pour ceux qui sont là-bas."
    mara raison "On ne sait même pas qui est là-bas, Noam. Justement, on essaie de le découvrir."
    "Tomas change de fenêtre. L'écran revient sur les règles de transfert."
    tomas reflexion "Ce qui m'inquiète surtout, c'est qu'on ne sait toujours pas quel droit nous avons de refuser quoi que ce soit."
    elias neutre "Kami n'a pas besoin de nous détester pour nous traiter comme du matériel."
    "Sa phrase me reste en tête. Je les vois redouter ce qu'on leur réserve, tout en sachant qu'ils envisagent d'enlever à d'autres le droit de vivre."
    noam raison "Vous parlez de votre liberté, mais il y a des originaux qui n'ont plus le choix à cause de vous. Ça vous arrive d'y penser ?"
    "La conversation s'arrête net. Mara détourne les yeux."
    mara fatigue "Oui. Tous les jours, même quand j'essaie de faire comme si tout était normal."
    noam inquiet "Et ça change quoi ?"
    mara agace "Ça change rien à ce qui s'est passé. Tu veux que je dise le contraire ? Que je dors parfaitement bien et que tout ça m'amuse ?"
    noam fatigue "Non. Je veux juste comprendre comment on peut trouver ça horrible et préparer quand même un nouveau remplacement."
    tomas raison "C'est une question qu'on doit se poser. Et tu as le droit de nous la poser, même si elle nous dérange."
    sael reflexion "Mais il y a une différence entre reconnaître nos actes et décider que nous n'avons plus le droit d'exister."
    noam agace "Je n'ai jamais dit ça."
    tomas neutre "Alors on est d'accord sur au moins une chose. On ne touchera pas à ton original pour te forcer à partir."
    "Je retiens ma respiration. La promesse semble sincère. Mais elle n'engage peut-être que Tomas."
    if j27_secret_alarm_choice == "risque":
        tomas raison "Et grâce au numéro de dossier qu'on a récupéré, on a une piste à transmettre à Zero. Ça ne prouve rien de plus, mais ça nous évitera de repartir de zéro."
    else:
        tomas raison "Il nous manque encore la référence complète du dossier. On ne va pas risquer une autre intrusion aujourd'hui."
    if "keyper" in j27_secret_archive_read:
        noam reflexion "La fiche que j'ai lue ne disait même pas quelle forme de vie se trouve sur Keyper. Vous êtes sûrs qu'il faut déjà parler d'y envoyer quelqu'un ?"
        sael raison "Non. Et c'est justement pour ça qu'on doit obtenir des réponses avant de prendre la moindre décision."
    elif "statut" in j27_secret_archive_read:
        noam reflexion "Et cette classification... si elle ne nous reconnaît même pas comme des personnes, qui nous garantit qu'on pourra refuser le transfert ?"
        tomas neutre "Personne, pour l'instant."
    elif "notes" in j27_secret_archive_read:
        noam reflexion "Dans tes notes, tu voulais demander à Zero ce qu'il sait. Tu crois qu'il répondra ?"
        tomas raison "Je compte bien essayer. Mais il faudra vérifier ce qu'il nous dira."
    else:
        noam reflexion "Ces listes de transfert ne disent pas si les départs étaient volontaires."
        sael raison "Non. On ne peut pas conclure à leur place."
    "La discussion reprend, plus doucement. Kael propose de contacter Zero ; Elias cherche un moyen d'accéder à d'autres documents sans attirer l'attention."
    "Je ne participe presque plus. Je revois Iris entraînant mon double à l'écart, et j'entends encore Mara demander ce que je compte faire de mon original."
    mara fatigue "Bon. Je vais chercher à manger. Il y en a qui ont passé la journée ici sans avaler grand-chose."
    elias sourire "Pour une fois, tu parles de toi ou de nous ?"
    mara agace "Les deux, abruti."
    "Ils se dispersent autour de la table. J'en profite pour regarder une dernière fois mon téléphone."
    "Un nouveau message s'affiche. Iris."
    "Je l'ouvre si vite que je manque de faire tomber l'appareil."
    "« On doit parler de ce que tu m'as dit après le vote. Pas devant les autres. »"
    "Je relis la phrase. Trois fois."
    think "Ce que je lui ai dit ?"
    "Je n'ai pas assisté au vote. Je ne sais même pas ce que mon double a pu lui raconter."
    "Une autre notification apparaît : « Tu m'avais promis de ne rien me cacher. »"
    "Je range le téléphone avant que quelqu'un puisse voir ma tête."
    think "Qu'est-ce qu'il a fait, exactement, pendant que j'étais ici ?"
    $ j27_secret_iris_doubt = True
    $ hideGroup()
    stop music fadeout 1.5
    call end_day("28", sleeping=True) from _call_j27_secret_end_day_28
    # Route secrète du J28 : conserver les flags j27_secret_* pour les reprises.
    return