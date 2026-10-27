# QTE rapide du retour au laboratoire : touche Espace avant la fin du compte à rebours.
screen j27_escape_key_qte():
    modal True
    zorder 120
    add Solid("#050c19c9")
    text "SAUTE DANS LE LABORATOIRE !" xalign 0.5 yalign 0.35 size 48 color "#ffffff"
    text "ESPACE — VITE !" xalign 0.5 yalign 0.53 size 44 color "#ffe585"
    key "K_SPACE" action Return(True)
    timer 1.6 action Return(False)

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
    $ j27_secret_trace_success = False
    $ j27_secret_key_success = False

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bonjour, chers représentants ! Votre vote est prévu aujourd'hui à quatorze heures. Essayez de ne pas vous faire attendre !"
    scene black with dissolve
    play sound "audio/sfx_duct_scrape.wav" volume 0.30
    "Je me redresse d'un coup et cogne ma tête contre une barre métallique."
    noam fatigue "Aïe... Merde."
    "Je suis toujours dans le conduit, près du laboratoire. J'ai dû m'endormir ici, avec ma lampe contre la poitrine."
    "Sur ma tablette, la conversation avec Iris s'arrête à hier. Aucun nouveau message."
    think "Mon double n'a pas de tablette. Si Iris m'écrit, c'est qu'elle ne lui parle pas à cet instant. Il vaut mieux quand même que je ne réponde pas."
    think "Je lui ai dit que je revenais. C'est mon double qui a dû rentrer à ma place."
    "Je pourrais lui écrire. Mais si elle est avec mon double, une seule question pourrait tout faire foirer."
    "Je rampe jusqu'à la grille du laboratoire."
    think "Les autres doivent être là-bas..."

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    $ showGroup([("tomas", "reflexion", 0.22), ("elias", "fatigue", 0.49), ("noam", "fatigue", 0.78)])
    elias fatigue "Ah, le voilà. Je commençais à croire qu'il t'était arrivé quelque chose."
    noam fatigue "J'ai passé la nuit dans les conduits. Franchement, je le recommande vraiment pas."
    elias reflexion "Hein ? Mais pourquoi t'es pas allé pioncer dans sa chambre ?"
    elias raison "Tu n'avais pas dit qu'il dormait dans la chambre d'Iris maintenant ? Pourquoi t'y es pas retourné ?"
    noam peur "... Hein ? Euh..."
    noam reflexion "Ouais, je sais pas trop, j'y ai pas vraiment pensé..."
    tomas raison "Tu dormiras mieux ce soir. Là, on a pas vraiment le temps pour ça, on a une fenêtre assez courte pour consulter les archives."
    noam reflexion "Vous avez trouvé quelque chose d'intéressant ?"
    tomas neutre "Pas encore. Va falloir aller dans la salle des archives pour chercher des informations sur Keyper-IIB."
    elias raison "Et surtout, va falloir faire gaffe à ce que ton original débarque pas. Il pourrait très bien s'y pointer sans prévenir."
    "Je mets une seconde à comprendre qu'ils parlent de moi. Chaque fois qu'ils prononcent « ton original », j'ai envie de me retourner pour vérifier qu'ils ne m'ont pas reconnu."
    noam inquiet "Vous voulez faire quoi de lui...?"
    elias sourire "Je vais lui demander de venir bricoler avec moi. Ça devrait l'occuper une bonne heure."
    tomas raison "Ouais. Pas de violence et pas de remplacement improvisé."
    "Il dit ça en vérifiant les accès sur son écran, comme s'il parlait de déplacer une caisse."
    "Je reste silencieux. Eux savent ce qu'ils ont fait pour être ici."
    tomas raison "Tu as réfléchi pour ton original depuis hier ?"
    noam inquiet "N-Non. Pourquoi...?"
    tomas neutre "Il faut qu'on décide ce qu'il adviendra de lui. Si tu veux prendre sa place au départ, on ne pourra pas éviter cette conversation éternellement."
    noam agace "... Mais on ne-"
    elias colere "Ouais, on sait très bien ce que tu en penses. On te comprend, tu sais... Mais..."
    tomas triste "Si tu veux vraiment monter dans cette navette, tu n'as pas vraiment le choix..."
    tomas reflexion "Sinon, tu finiras sur Keyper. En tout cas vraisemblablement..."
    noam colere "STOP ! Je préfère qu'on arrête de parler comme si sa vie était un programme qu'on devait régler !"
    "Elias repose lentement son tournevis. J'ai parlé trop vite."
    elias reflexion "Attends... Pourquoi tu réagis comme ça ?"
    noam inquiet "Parce que... Parce que j'ai pas envie qu'on décide de le tuer à ma place, c'est tout !"
    elias triste "Wow, excuse ! On savait que ça te dérangeait, mais pas à ce point-là..."
    tomas neutre "D'accord, d'accord. Je ne te force à rien, mais il va falloir y réfléchir."
    tomas reflexion "Et vite, avant que Mara décide de vraiment passer à l'action."
    "Je regarde le sol. Si je réponds que je ne veux pas partir, je vais devoir expliquer pourquoi."
    noam fatigue "Je sais pas encore. C'est justement pour ça que j'ai besoin de comprendre ce que c'est vraiment que cette exoplanète-là."
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
    "Je sors ma tablette pour lire le message d'Elias. Tomas s'arrête net."
    tomas surpris "Attends... C'est quoi, ça ?"
    noam hesitation "Quoi ?"
    tomas inquiet "La tablette. T'as récupéré celle de ton original ?"
    "Je la regarde. Putain, j'avais même pas pensé à ça."
    noam hesitation "Ah... ouais. Enfin, je... j'ai réussi à lui prendre."
    elias surpris "Tu lui as volé sa tablette ? Sans qu'il s'en aperçoive ?"
    noam inquiet "Ouais. Il l'avait posée, alors... je l'ai prise. Je me suis dit que ce serait plus simple pour discuter du plan."
    tomas reflexion "Et il l'a pas réclamée ?"
    noam hesitation "Pas encore. Enfin, je crois pas."
    elias fatigue "Bon, bah fais gaffe à pas la sortir devant lui, surtout."
    noam neutre "Ouais, t'inquiète."
    "Je baisse les yeux vers le message. Elias vient de m'écrire."
    call messenger_play("elias", "elias", [("elias", "C'est bon, je m'en occupe !"), ("noam", "Super, merci !")], objective_text="Lire le message d'Elias")
    noam sourire "Ah, super ! Il s'en occupe."
    tomas raison "Parfait, ça veut dire qu'il a récupéré ton original. On a notre fenêtre. On y va."
    noam neutre "Ouais... Et Tomas, à propos de ce qu'on disait..."
    tomas raison "On en reparlera. Mais si tu veux vraiment pas le remplacer, faudra le dire aux autres. Pas seulement à moi."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je suis Tomas dans les conduits. À deux reprises, il s'arrête pour écouter derrière une grille. Chaque bruit me paraît beaucoup trop proche."
    noam reflexion "Le terminal ne signale pas les entrées ?"
    tomas neutre "Si, mais j'ai une autorisation pour consulter la salle. Le problème, c'est si un représentant nous tombe dessus. Là, je vois pas trop ce qu'on pourra lui raconter."
    noam inquiet "Et si Kami regarde les caméras ?"
    tomas fatigue "Si elle regarde, elle nous verra de toute façon. Alors évite juste de faire quelque chose qui lui donne envie de venir nous demander des comptes."
    "Nous sortons derrière un panneau technique."
    $ flashlight_off()
    scene bg_archive at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "raison", 0.37), ("noam", "inquiet", 0.66)])
    "Tomas présente sa tablette au lecteur. La porte s'ouvre et se referme derrière nous."
    tomas raison "Toi, surveille la porte. Même si tu crois seulement entendre quelqu'un, tu me préviens, d'accord ? Je préfère ressortir pour rien que me retrouver nez à nez avec ton original."
    noam neutre "Compris."
    "Sur l'écran, plusieurs registres apparaissent. Tomas remonte des lignes de dates, puis s'arrête."
    tomas surpris "Attends... Il y a une mise à jour automatique qui date de ce mois-ci."
    noam reflexion "Sur Keyper ?"
    tomas raison "Ouais... Attends, c'est pas une estimation. Il y a eu des relevés récents. Noam, il y a déjà de la vie là-bas !"
    noam surpris "Des gens ?"
    tomas neutre "Ouais apparemment il y aurait un peu plus de 13500 personnes sur place !"
    "Il ouvre un second fichier."
    tomas reflexion "Et là, regarde... « station de production ». Mais quand j'essaie d'ouvrir le dossier pour savoir ce qu'ils produisent, on me demande une autorisation que j'ai pas."
    noam inquiet "Production de quoi ?"
    tomas agace "Bah justement, je cherche ! Laisse-moi deux secondes..."
    tomas reflechit "S'il y a déjà de la vie là-bas alors ça veut dire que... Zero avait raison finalement ?"
    "Ma tablette vibre encore. Je baisse les yeux, persuadé qu'Elias nous annonce que tout se passe bien."
    call messenger_play("elias", "elias", [("elias", "Putain, c'est la merde, je le trouve pas !"), ("elias", "Il doit encore être avec Iris...")], objective_text="Lire les nouveaux messages d'Elias")
    noam peur "Attends... QUOI ?!"
    tomas inquiet "Qu'est-ce qu'il y a ?"
    noam peur "Elias dit qu'il a pas trouvé mon original !"
    tomas colere "Mais il nous a dit que c'était bon ! Passe-moi ça !"
    "Je tape aussi vite que je peux. Tomas se penche par-dessus mon épaule et me dicte sa propre question."
    call messenger_play("elias", "elias", [("noam", "Mais pourquoi t'as dit que c'était bon alors ?! On est déjà aux archives !"), ("noam", "Elias, réponds ! Tu l'as avec toi ou pas ?! — Tomas"), ("elias", "MAIS NON ! Je disais que c'était bon, que j'allais m'en occuper ! Je commençais à le chercher !")], objective_text="Éclaircir le message d'Elias")
    noam colere "Mais putain, on a cru que tu l'avais trouvé !"
    tomas agace "C'est pas vrai... Ferme le dossier, on se tire."
    "Tomas commence à fermer les fenêtres. Je regarde la porte, puis ma tablette. Trois nouveaux messages arrivent presque d'un coup."
    call messenger_play("elias", "elias", [("elias", "OH JE LES VOIS ! PUTAIN ILS SONT DANS LE COULOIR !"), ("elias", "Ils arrivent vers vous !"), ("elias", "RETOURNEZ AU LABO ! VITE !")], objective_text="URGENCE — Lire les messages d'Elias")
    noam peur "Tomas ! Ils viennent ici !"
    tomas inquiet "J'ai compris ! Laisse les fichiers et cours !"
    $ j27_secret_alarm_choice = "fuite"
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je plonge dans le conduit derrière Tomas. Il faut franchir la première courbe sans se coincer contre les renforts."
    # QTE de tracé : utilisation du screen existant, sans tutoriel ni écran de résultats.
    call screen trace_qte(path_type="curve_left", time_limit=3.2, wait_time=0.25, tolerance=65, max_errors=3, anchor_x=960, anchor_y=540)
    $ j27_secret_trace_success = _return.get("success", False)
    if j27_secret_trace_success:
        "Je glisse le long de la courbe d'un seul mouvement. Tomas est juste devant moi."
        tomas inquiet "Bien ! Continue !"
    else:
        "Mon épaule heurte un renfort. Je perds quelques secondes à me dégager."
        noam peur "Merde, merde... !"
        tomas inquiet "Noam ! Bouge, ils arrivent !"
    "Au prochain embranchement, Tomas se retourne et me montre la grille du laboratoire."
    tomas inquiet "Là ! Saute, maintenant !"
    # QTE de touche : barre Espace dans une fenêtre très courte.
    call screen j27_escape_key_qte
    $ j27_secret_key_success = _return
    if j27_secret_key_success:
        "Je bondis vers l'ouverture et me laisse tomber dans le laboratoire, juste derrière Tomas."
    else:
        "Je rate le rebord, me rattrape à la dernière seconde et me hisse de force dans l'ouverture."
        "Un choc métallique résonne derrière moi. Je retiens un juron."
    $ flashlight_off()
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    "Tomas rabat la grille. Nous restons immobiles, le souffle court, pendant que des pas résonnent de l'autre côté."
    if not j27_secret_trace_success or not j27_secret_key_success:
        "Quelqu'un ralentit tout près. Je plaque une main sur ma bouche pour étouffer ma respiration."
    "Les pas finissent par s'éloigner. Tomas attend encore quelques secondes avant de me regarder."
    $ showGroup([("tomas", "fatigue", 0.35), ("noam", "inquiet", 0.65)])
    tomas agace "La prochaine fois, on attend une phrase claire avant de bouger. « C'est bon », ça voulait absolument rien dire !"
    noam colere "C'est surtout Elias qui aurait pu dire qu'il l'avait PAS trouvé !"
    "Ma tablette vibre une dernière fois."
    call messenger_play("elias", "elias", [("elias", "Désolé... Je vais essayer de les éloigner. Restez au labo.")], objective_text="Lire la réponse d'Elias")
    tomas fatigue "Bon... On a au moins appris qu'il y a de la vie sur Keyper et cette histoire de station de production. Pour les références complètes, c'est raté."
    noam inquiet "T'es sûr qu'ils nous ont pas entendus ?"
    tomas neutre "Non. Et j'ai pas envie de retourner vérifier."
    $ hideGroup()

    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "reflexion", 0.36), ("noam", "inquiet", 0.65)])
    "Tomas pose sa tablette sur la table. Il regarde plusieurs fois l'heure."
    tomas raison "Bon, je dois aller au Conclave. Toi, tu restes ici, hein. Surtout, tu bouges pas tant que le vote est pas terminé."
    noam inquiet "Et si mon original vient ?"
    tomas neutre "À cette heure-là, il devrait être au vote. Et si quelqu'un arrive, tu files dans le conduit. Tu connais le chemin."
    noam reflexion "Tu pourrais lui demander ce qu'il a fait hier soir ?"
    tomas surpris "À ton original ? Euh... Pourquoi tu veux savoir ce qu'il a fait hier soir ?"
    "Je sens mes joues chauffer. Je ne peux pas lui parler d'Iris sans devoir expliquer que je suis celui qui devrait être à sa place."
    noam fatigue "Laisse tomber."
    tomas raison "Je t'ai laissé une copie sur le petit terminal, si tu veux regarder. Mais touche pas au principal, j'en ai besoin pour la suite."
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
    "Je ferme les fichiers. Je regarde plusieurs fois ma tablette, mais Iris m'a rien écrit."
    call show_custom_title("En fin d'après-midi") from _call_j27_secret_late_afternoon
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.7
    "Des voix approchent par le conduit. Je range la tablette juste avant que Kael, Mara et Sael n'entrent."
    $ showGroup([("kael", "sourire", 0.14), ("mara", "taquin", 0.35), ("sael", "neutre", 0.57), ("noam", "reflexion", 0.80)])
    mara sourire "Ah, t'es toujours là ? Je commençais à croire que tu t'étais encore perdu dans les conduits !"
    noam neutre "Tomas m'a demandé de l'attendre."
    sael reflexion "Il n'est pas rentré ?"
    noam neutre "Pas encore. Le vote s'est bien passé ?"
    kael calme "Ouais, et ton original a même réussi à mettre tout le monde d'accord. Pour une fois, ça s'est pas terminé en trois heures de disputes."
    mara rire "Je vais pas mentir, il m'a bluffée. Ton original était presque brillant, aujourd'hui !"
    "Je fixe Mara. Ils sont en train de féliciter un autre homme d'avoir réussi mon propre vote."
    noam inquiet "Et Iris ?"
    mara taquin "Iris ? Oh, elle était de bonne humeur, elle ! Après la séance, elle l'a pris par le bras et ils sont partis discuter tous les deux."
    noam inquiet "Attends... Elle l'a emmené où, exactement ?"
    sael reflexion "Vers les dortoirs, je crois. Pourquoi ?"
    noam fatigue "Pour rien. Je pensais qu'elle lui poserait des questions sur le vote."
    mara taquin "Ah mais attends... Tu serais pas jaloux de ton original, par hasard ?"
    "Je voudrais répondre que c'est ridicule. Le problème, c'est que je ne le trouve pas ridicule du tout."
    noam agace "Tu peux arrêter ?"
    mara reflexion "Eh, doucement... Je rigolais, c'est tout."
    kael calme "Mara, laisse-le."
    "Je baisse les yeux. Iris croit avoir passé la journée avec moi. Et moi, je suis ici à écouter des inconnus discuter de ce qu'on pourrait faire de mon existence."
    sael neutre "En tout cas, il n'a rien dit qui laisse penser qu'il soupçonne quelque chose."
    noam inquiet "Qu'est-ce que tu veux dire ?"
    sael reflexion "Que ton original continue sa vie. C'est plutôt une bonne nouvelle pour toi, non ?"
    "Je serre le bord de la table. Une bonne nouvelle. Tant qu'il ne soupçonne rien, ils peuvent décider quand et comment il disparaîtra."
    mara fatigue "Bon, je vais quand même te poser la question... T'as réfléchi au départ ? Parce qu'on est plus très loin, là, et personne sait ce que tu comptes faire."
    noam agace "Vous pourriez me laisser réfléchir cinq minutes sans me rappeler que quelqu'un doit prendre une décision sur sa vie ?"
    mara surpris "Mais attends, j'ai jamais dit qu'on allait le tuer ce soir ! Je te demande juste ce que toi tu veux faire !"
    noam inquiet "Et si je dis que je ne veux pas le remplacer ?"
    "Mara ouvre la bouche, puis la referme."
    mara reflexion "Alors... Alors il faudra trouver une autre solution, j'imagine. Mais franchement, je vois pas laquelle pour l'instant."
    sael raison "Personne ici ne devrait te forcer à franchir cette limite. Par contre, il faut qu'on en parle ensemble."
    "Le mot « ensemble » me fait froid dans le dos. Je voudrais savoir si Mara accepterait aussi facilement qu'on laisse son original repartir à sa place."
    play sound sfx_creak volume 0.35
    "La grille grince. Elias arrive avec sa caisse à outils, suivi de Tomas."
    $ showGroup([("kael", "calme", 0.07), ("mara", "reflexion", 0.21), ("sael", "neutre", 0.35), ("elias", "fatigue", 0.49), ("tomas", "raison", 0.63), ("noam", "inquiet", 0.78)])
    elias fatigue "Eh ben, plus jamais je lui demande de venir vérifier un panneau. Il m'a fait tester chaque putain de connexion !"
    noam inquiet "Il s'est douté de quelque chose ?"
    elias neutre "Pas à ma connaissance. Il m'a surtout demandé pourquoi un circuit qui fonctionnait hier avait besoin de moi aujourd'hui."
    tomas raison "On a plus important. Les archives confirment une chose : Keyper-IIB n'est pas un monde désert. Il y a déjà de la vie là-bas."
    kael surpris "De la vie ? Tu parles de quoi exactement ?"
    tomas neutre "C'est ça le problème, on sait pas. Ça confirme qu'il y a de la vie, pas de quoi il s'agit. Alors j'aimerais bien éviter qu'on commence à inventer des choses."
    mara reflexion "Et les transferts ?"
    tomas raison "Ouais, les transferts sont bien réels. Et il y a une installation là-bas, appelée « station de production ». Par contre, impossible de savoir ce qu'il y a dedans."
    sael inquiet "Production de quoi ?"
    tomas fatigue "Aucune idée. Le dossier de fonctionnement est verrouillé."
    elias reflexion "On a aussi un problème de classification. Dans certains registres, les Doppelgängers ne sont pas enregistrés comme des représentants."
    kael inquietude "Donc la protection votée au jour vingt-quatre pourrait ne pas nous concerner ?"
    tomas raison "Elle pourrait nous concerner. Ou pas. Les documents ne permettent pas de trancher et je refuse qu'on présente une inquiétude comme une certitude."
    mara agace "Et ça te dérange pas plus que ça d'être rangé dans une catégorie comme du matériel ?!"
    tomas agace "Mais bien sûr que si, Mara ! Sauf que je préfère savoir de quoi je parle avant d'aller hurler sur Kami !"
    sael raison "Est-ce qu'on peut obtenir le dossier auprès de Zero ?"
    kael calme "Je peux le contacter. S'il connaît cette installation, il saura peut-être où chercher."
    noam reflexion "Et s'il vous disait de laisser tomber ? Vous le feriez ?"
    "Tous les regards se tournent vers moi."
    kael surpris "Pourquoi il nous dirait ça ?"
    noam inquiet "J'en sais rien... Je me demande juste jusqu'où vous iriez pour ceux qui sont là-bas. Même si vous savez pas qui c'est."
    mara raison "Mais on sait même pas qui vit là-bas, Noam ! C'est justement pour ça qu'on fouille ces dossiers !"
    "Tomas change de fenêtre. L'écran revient sur les règles de transfert."
    tomas reflexion "Ce qui m'inquiète surtout, c'est qu'on ne sait toujours pas quel droit nous avons de refuser quoi que ce soit."
    elias neutre "Kami n'a pas besoin de nous détester pour nous traiter comme du matériel."
    "Sa phrase me reste en tête. Je les vois redouter ce qu'on leur réserve, tout en sachant qu'ils envisagent d'enlever à d'autres le droit de vivre."
    noam raison "Vous arrêtez pas de parler de votre liberté, mais... Et celle des originaux ? Ceux qui ont été remplacés, vous y pensez, des fois ?"
    "La conversation s'arrête net. Mara détourne les yeux."
    mara fatigue "Oui, Noam. Bien sûr que j'y pense. Même quand je fais semblant que tout va bien, je peux pas simplement oublier ça."
    noam inquiet "Et ça change quoi ?"
    mara agace "Ça change rien à ce qui s'est passé. Tu veux que je dise le contraire ? Que je dors parfaitement bien et que tout ça m'amuse ?"
    noam fatigue "Non... Je comprends juste pas comment vous pouvez dire que c'est horrible et continuer à parler de remplacer quelqu'un comme si c'était normal."
    tomas raison "Tu crois qu'on se la pose pas, cette question ? Moi, je me la pose tous les jours. Ça veut pas dire que j'ai trouvé une réponse qui me plaît."
    sael reflexion "Mais il y a une différence entre reconnaître nos actes et décider que nous n'avons plus le droit d'exister."
    noam agace "Je n'ai jamais dit ça."
    tomas neutre "Bon. Sur un point, je peux te rassurer : personne ici n'ira toucher à ton original pour te forcer à partir. En tout cas, pas avec mon accord."
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
    "Ils se dispersent autour de la table. J'en profite pour regarder une dernière fois ma tablette."
    "Un nouveau message s'affiche. Iris."
    think "Elle doit être seule pour m'écrire. Mon double ne voit rien de cette conversation, heureusement."
    "Je l'ouvre si vite que je manque de faire tomber l'appareil."
    "« On doit parler de ce que tu m'as dit après le vote. Pas devant les autres. »"
    "Je relis la phrase. Trois fois."
    think "Ce que je lui ai dit ?"
    "Je n'ai pas assisté au vote. Je ne sais même pas ce que mon double a pu lui raconter."
    "Une autre notification apparaît : « Tu m'avais promis de ne rien me cacher. »"
    "Je range la tablette avant que quelqu'un puisse voir ma tête."
    think "Qu'est-ce qu'il a fait, exactement, pendant que j'étais ici ?"
    $ j27_secret_iris_doubt = True
    $ hideGroup()
    stop music fadeout 1.5
    call end_day("28", sleeping=True) from _call_j27_secret_end_day_28
    # Route secrète du J28 : conserver les flags j27_secret_* pour les reprises.
    
    jump _28_0_1_1_0_0_1_REVEIL
