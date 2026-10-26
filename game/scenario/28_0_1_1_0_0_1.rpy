# JOUR 28 — UNE PLACE POUR DEUX
# Route secrète : Noam se fait passer pour son Doppelgänger.
# Le choix du dernier double est enregistré ici. La mise en œuvre aura lieu au J29.
default j28_secret_target = None
default j28_secret_plan_decided = False
default j28_secret_iris_exchange = False
default j28_secret_zero_contact = False

label _28_0_1_1_0_0_1_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"
    $ j28_secret_target = None
    $ j28_secret_plan_decided = False
    $ j28_secret_iris_exchange = False
    $ j28_secret_zero_contact = False
    call show_chapter_title("Début du chapitre 9", "Chapitre 9 — Le dernier départ")
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je me réveille avec un mal de dos horrible. J'ai encore dormi sur la banquette du labo."
    "Je cherche mon téléphone entre les coussins. Il a dû tomber pendant la nuit."
    "Je le récupère aussitôt. Les messages d'Iris sont toujours là."
    think "« On doit parler de ce que tu m'as dit après le vote. »"
    "Iris pense qu'on a parlé hier. Sauf que moi, j'étais ici pendant qu'il était avec elle."
    noam fatigue "Putain..."
    tomas fatigue "Ah, t'es réveillé ? Cette banquette est vraiment pourrie."
    $ showGroup([("tomas", "fatigue", 0.32), ("noam", "fatigue", 0.69)])
    "Tomas est déjà devant l'ordinateur, avec une tasse vide."
    noam fatigue "T'as dormi ici aussi ?"
    tomas neutre "Pas vraiment. Mara s'est levée à six heures, elle a réveillé tout le monde."
    noam taquin "Ah ouais ? Elle faisait quoi ?"
    tomas fatigue "Du café. Pour elle. Elle m'a même pas demandé si j'en voulais."
    "Je m'assois en grimaçant."
    noam reflexion "T'as trouvé quelque chose sur Keyper ?"
    tomas raison "Non. J'ai relu ce passage dix fois et je comprends toujours pas."
    noam neutre "Tu devrais peut-être dormir un peu."
    tomas fatigue "Ouais, merci. Ça m'aide vachement."
    "Mon téléphone vibre."
    call messenger_play("iris", "iris", [("iris", "Bon, tu comptes me répondre ou pas ?"), ("iris", "J'ai pas dormi des masses, merci pour ça."), ("iris", "Et non, c'est pas un reproche. Enfin, pas complètement.")], objective_text="Lire les messages d'Iris")
    "Je relis le message. Je sais pas quoi répondre."
    tomas reflexion "C'est ton double qui t'écrit ?"
    noam hesitation "Non. Iris."
    tomas neutre "Ah."
    "Il essaie de reprendre sa lecture, puis relève la tête."
    tomas taquin "C'est Iris ? T'as l'air bizarre."
    noam surpris "Pourquoi ?"
    tomas neutre "Bah, t'as l'air inquiet. Ça va ?"
    noam fatigue "C'est compliqué."
    tomas neutre "D'accord. Au fait, Kael nous a demandé de rester ici."
    noam reflexion "Pourquoi ?"
    tomas raison "Il a eu des nouvelles de Zero. Il veut nous parler."
    noam inquiet "Zero va venir ?"
    tomas fatigue "J'en sais rien. Kael m'a rien dit d'autre."
    noam neutre "Ouais, d'accord."
    tomas reflexion "Et toi, sinon ? Ça va ?"
    noam fatigue "Pas trop."
    tomas fatigue "Ouais, pareil."
    "Il pousse une chaise vers moi du pied."
    tomas neutre "Assieds-toi là plutôt. C'est un peu moins inconfortable."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_REUNION

label _28_0_1_1_0_0_1_REUNION:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.9
    "Mara arrive avec deux tasses. Elias la suit avec un sac et sa caisse à outils."
    $ showGroup([("mara", "rire", 0.13), ("elias", "fatigue", 0.37), ("tomas", "fatigue", 0.61), ("noam", "neutre", 0.84)])
    elias fatigue "La prochaine fois, tu portes ton sac toute seule."
    mara rire "Oh ça va ! Je t'ai demandé de le porter deux minutes !"
    elias colere "C'est pas deux minutes ! Tu m'as aussi filé ta caisse !"
    mara taquin "Bah t'avais qu'à me dire non !"
    tomas neutre "Mara, y en a un pour moi ?"
    mara rire "Ah non, j'ai pris les deux."
    tomas fatigue "Sérieux..."
    "Nyra et Sael arrivent. Nyra pose une tablette sur la table."
    $ showGroup([("nyra", "neutre", 0.11), ("sael", "neutre", 0.29), ("mara", "taquin", 0.46), ("elias", "fatigue", 0.64), ("noam", "neutre", 0.83)])
    sael mefiant "Vous pourriez parler moins fort ?"
    mara taquin "C'est Elias, il râle depuis tout à l'heure."
    elias fatigue "Parce que tu me fais chier !"
    nyra neutre "Kael arrive. Vous finirez après."
    mara agace "Oui, bon, ça va."
    "Kael entre et referme la grille. Mara pose enfin ses tasses."
    $ showGroup([("kael", "calme", 0.05), ("nyra", "neutre", 0.19), ("mara", "neutre", 0.33), ("tomas", "reflexion", 0.47), ("elias", "fatigue", 0.61), ("sael", "neutre", 0.75), ("noam", "inquiet", 0.91)])
    kael calme "Bon, tout le monde est là ? On peut commencer ?"
    mara taquin "Tu dis ça à chaque fois."
    kael sourire "Oui, je sais."
    "Kael affiche les six districts sur le terminal."
    kael calme "J'ai parlé à Zero. Il dit qu'on a presque fini."
    tomas reflexion "Presque ?"
    kael neutre "Il manque encore Harmonie et Nexus."
    noam reflexion "Attends, comment ça ?"
    kael calme "Pour Harmonie, tant que t'as pas pris la place de ton original, ça bloque."
    "J'évite de regarder les autres. Ils parlent de moi sans le savoir."
    kael calme "Et pour Nexus, il faudrait un double d'Iris ou de Julian."
    elias reflexion "On peut pas partir comme ça ? Il faut vraiment les six ?"
    kael calme "Zero dit que oui. Moi aussi j'aimerais comprendre pourquoi."
    tomas raison "Et Keyper ? Tu lui as demandé ?"
    kael neutre "Oui."
    tomas reflexion "Et ?"
    kael calme "Et alors ?"
    tomas agace "Il a toujours pas répondu."
    mara agace "Mais putain ! On lui a montré ce qu'on a trouvé et il dit rien ?"
    tomas raison "Tomas, on sait ! Tu vas pas recommencer toute la réunion d'hier ?"
    nyra raison "Bah si, tant qu'on n'a pas de réponse ! Ça vous dérange pas ?"
    "Nyra montre la date sur sa tablette. Elias s'approche."
    elias fatigue "Deux jours, c'est très court. On fabrique pas un double en cinq minutes !"
    noam reflexion "Il vous faut combien de temps ?"
    elias raison "Si on trouve les pièces aujourd'hui, on peut en faire un. Un seul."
    mara taquin "Et sans tout casser, cette fois ?"
    elias colere "Mara, putain, tu peux arrêter ?"
    mara rire "Oh, ça va, je rigole !"
    kael calme "Il nous manque des pièces et un objet qui appartient à la personne."
    noam surpris "Un objet ? Pour quoi faire ?"
    elias neutre "Un vêtement, un truc qu'elle garde souvent avec elle... Il nous faut ses traces. Sinon la copie sera ratée."
    mara taquin "Donc ses chaussettes, ça marche ?"
    elias fatigue "Mais j'en sais rien, Mara ! Arrête deux secondes !"
    tomas reflexion "Et tu sais où trouver les pièces ?"
    elias raison "Je crois. Y a une réserve vers la maintenance. Mais faut décider qui on copie avant."
    "Kael montre Nexus sur l'écran. Personne ne répond tout de suite."
    sael mefiant "Vous êtes en train de choisir lequel des deux va mourir ?"
    mara agace "Tu proposes quoi ? On attend qu'on nous envoie sur Keyper ?"
    tomas desaccord "On sait même pas ce qu'il y a là-bas !"
    mara colere "Bah justement ! Moi, j'ai pas envie de le découvrir !"
    "Nyra pose sa tablette et se lève."
    nyra raison "Julian, ce serait plus facile."
    elias neutre "Ouais, sa chambre est accessible. On connaît le passage."
    mara reflexion "Et il mange souvent tout seul. Je l'ai encore vu hier."
    tomas reflexion "Pourquoi tu fais attention à ça ?"
    mara taquin "Quoi ? T'es jaloux ?"
    tomas fatigue "Non, je demande."
    nyra raison "Julian nous donne Nexus. Avec Iris, on pourrait aussi régler Harmonie."
    elias surpris "Attends, comment ?"
    nyra raison "Si Iris n'est plus avec l'autre Noam, on pourra l'approcher plus facilement."
    "Elle me regarde. Je comprends tout de suite."
    noam inquiet "Vous comptez faire quoi de lui ?"
    nyra neutre "Le remplacer."
    mara reflexion "Mara relève la tête et nous regarde."
    nyra raison "Il passe tout son temps avec Iris. Tant qu'elle est là, on pourra pas l'approcher."
    elias colere "Mais Iris va nous démonter si elle nous trouve !"
    nyra raison "Je sais, Elias."
    elias fatigue "Bah alors pourquoi tu proposes ça ?"
    nyra colere "Parce que ça nous donnerait une chance de faire les deux ! J'ai jamais dit que c'était facile !"
    "Mara s'appuie contre la table."
    mara reflexion "Donc si on choisit Iris, Noam pourrait prendre la place de l'autre. C'est ça ?"
    nyra raison "Oui, s'il accepte."
    tomas desaccord "Sauf qu'il a déjà dit non !"
    mara agace "Et alors ? Il a le droit de changer d'avis !"
    tomas raison "Mais on va pas s'en prendre à Iris pour le faire changer d'avis !"
    noam colere "Non mais attendez ! Vous êtes sérieux, là ? Iris a rien demandé !"
    "Ils se tournent tous vers moi."
    nyra reflexion "Noam, on cherche une solution. Tu proposes quoi, toi ?"
    noam inquiet "Je sais pas, mais... pas ça ! Pas Iris !"
    mara agace "Mais tu sais très bien ce qu'on fait, Noam ! On cherche quelqu'un à remplacer !"
    noam colere "Je sais, Mara ! Me prends pas pour un con !"
    mara colere "Bah alors arrête de nous engueuler et propose autre chose !"
    tomas colere "Mara, ça suffit ! Il a le droit de pas vouloir !"
    mara colere "Et moi j'ai le droit d'avoir peur de Keyper ! Vous voulez qu'on attende quoi, le jour du départ ?"
    elias fatigue "Elias soupire et passe une main sur son visage."
    sael mefiant "Si c'est Iris, faut prévoir ce qu'on fait si elle nous surprend. Parce qu'elle va pas se laisser faire."
    nyra raison "C'est bien pour ça qu'on va pas y aller tout de suite."
    tomas desaccord "Julian, c'est moins dangereux. Pourquoi vous voulez compliquer les choses ?"
    nyra reflexion "Moins dangereux pour qui ?"
    tomas raison "Pour tout le monde, Nyra !"
    nyra neutre "Pas pour ceux qui vont rester ici si on laisse tomber Harmonie."
    noam inquiet "Tu parles de moi ?"
    nyra raison "Oui. On va pas attendre indéfiniment que tu changes d'avis."
    "Je serre les dents. Si je leur dis qui je suis, je sais pas ce qu'ils vont me faire."
    elias fatigue "Moi je vote Julian. J'ai pas envie qu'Iris nous tombe dessus."
    mara agace "Iris. Si ça peut nous permettre de finir, je préfère tenter ça."
    tomas raison "Julian. Et je veux pas qu'on touche à l'original de Noam sans son accord."
    sael mefiant "Julian. Au moins on connaît les risques."
    nyra neutre "Iris. J'ai déjà expliqué pourquoi."
    "Kael regarde les autres, puis se tourne vers moi."
    kael calme "Bon. On est pas d'accord."
    mara taquin "Ah bah moi, je suis d'accord !"
    kael neutre "Oui, Mara, on a compris."
    "Mon téléphone vibre. Je regarde discrètement l'écran."
    call messenger_play("iris", "iris", [("iris", "Bon, je vais dire un truc et après tu fais comme si j'avais rien dit."), ("iris", "Hier, quand t'as arrêté de plaisanter deux minutes... j'ai aimé ça."), ("iris", "Voilà. Tu peux reprendre ton sourire insupportable.")], objective_text="Lire le message d'Iris")
    "Je lis le message d'Iris deux fois. C'est à mon double qu'elle devrait écrire."
    mara taquin "Oh, Noam ! Tu nous écoutes ou pas ?"
    noam hesitation "Hein ? Oui, pardon, je suis là."
    mara rire "Ouais, on voit ça !"
    kael calme "Noam, on peut pas décider sans t'en parler. Tu connais Iris, tu sais comment elle réagit."
    noam reflexion "Moi ?"
    kael neutre "Oui. Tu préfères qu'on prépare Julian ou Iris ? Pour ton original, on en reparlera."
    "Je pourrais leur dire qui je suis. Mais si je fais ça, ils vont pas juste me laisser repartir."
    tomas raison "Kael, lui mets pas tout sur le dos."
    kael calme "Je lui demande son avis, c'est tout."
    "Je regarde Tomas. Personne dit rien. Ils attendent ma réponse."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_CHOIX

label _28_0_1_1_0_0_1_CHOIX:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "reflexion", 0.18), ("kael", "calme", 0.40), ("noam", "hesitation", 0.76)])
    menu (screen="critical_choice", noam_expr="hesitation", cc_targets={"Choisir Julian":{"label":"_28_0_1_1_0_0_1_JULIAN"},"Choisir Iris":{"label":"_28_0_1_1_0_0_1_IRIS"}}):
        "QUEL REPRÉSENTANT DE NEXUS FAUT-IL COPIER ?"
        "Choisir Julian":
            $ j28_secret_target = "julian"
            jump _28_0_1_1_0_0_1_JULIAN
        "Choisir Iris":
            $ j28_secret_target = "iris"
            jump _28_0_1_1_0_0_1_IRIS

label _28_0_1_1_0_0_1_JULIAN:
    $ j28_secret_target = "julian"
    noam raison "Julian. Je préfère qu'on choisisse Julian."
    nyra reflexion "Et pour Harmonie, on fait quoi ?"
    noam desaccord "Je sais. Mais Iris sait se défendre. Si vous la surprenez, ça va très mal se passer."
    elias neutre "Voilà. C'est ce que j'essaie de dire !"
    mara agace "Ouais, ça t'arrange bien."
    noam inquiet "Peut-être. Mais je veux pas qu'on s'en prenne à elle juste pour pouvoir approcher mon original."
    tomas raison "Je suis d'accord avec Noam."
    mara fatigue "Bon. Julian, alors. J'espère qu'on va pas le regretter."
    kael calme "D'accord. On prépare Julian et on s'arrête là aujourd'hui."
    "Je pense à Julian. Lui non plus a rien demandé. Et c'est moi qui l'ai choisi."
    jump _28_0_1_1_0_0_1_APRES_CHOIX

label _28_0_1_1_0_0_1_IRIS:
    $ j28_secret_target = "iris"
    noam fatigue "Iris."
    "Je le dis avant d'avoir vraiment réfléchi."
    noam hesitation "Si vous voulez vraiment les six districts, c'est Iris qu'il faut choisir."
    elias surpris "Attends, t'es sérieux ?"
    mara surpris "Oh putain ! Je pensais pas que tu dirais ça !"
    tomas desaccord "Noam, réfléchis. T'es pas obligé d'accepter juste pour qu'on arrête de se disputer !"
    noam inquiet "Je sais ! Et j'ai pas dit que je remplacerais mon original après !"
    nyra raison "Mais si on choisit Iris, ce serait quand même le but."
    noam colere "Oui, Nyra, j'ai compris ! Tu peux arrêter de me le répéter ?"
    "Nyra détourne les yeux."
    sael mefiant "Si vous choisissez Iris, personne y va sans qu'on sache exactement comment faire. D'accord ?"
    elias fatigue "Déjà faut retrouver les pièces. On fera rien aujourd'hui."
    mara neutre "Bon. Iris, alors. On verra demain."
    "Je regarde son prénom sur l'écran. Je viens de la mettre en danger."
    kael calme "D'accord. On prépare ça demain. Rien ce soir."
    jump _28_0_1_1_0_0_1_APRES_CHOIX

label _28_0_1_1_0_0_1_APRES_CHOIX:
    $ j28_secret_plan_decided = True
    $ current_period = "Midi"
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.18), ("kael", "calme", 0.39), ("tomas", "reflexion", 0.61), ("noam", "inquiet", 0.83)])
    "Elias ouvre sa caisse et commence à vérifier ses outils."
    elias fatigue "Bon, il faut que j'aille chercher les pièces. Y en a un qui vient m'aider ?"
    tomas taquin "T'as vraiment besoin de quelqu'un ?"
    elias agace "Bah oui, parce que je vais pas tout porter tout seul !"
    kael calme "C'est où, déjà ?"
    elias neutre "Une réserve à côté de la maintenance. J'y ai vu des boîtiers qui pourraient faire l'affaire."
    tomas reflexion "Ça va prendre longtemps ?"
    elias fatigue "J'en sais rien. Si les pièces sont encore là, ça ira vite. Sinon faudra chercher."
    noam neutre "Je viens avec toi."
    elias surpris "Hein ? Toi ?"
    noam fatigue "Ouais, j'ai envie de sortir un peu d'ici."
    elias neutre "Bon, viens. Mais me fais pas toucher à n'importe quoi, hein."
    tomas taquin "Essaie de pas le perdre dans un conduit, comme la dernière fois."
    elias fatigue "Mais je l'ai pas perdu !"
    noam surpris "Attends, qui ?"
    tomas rire "Moi ! Il est parti et j'ai dû retrouver le chemin !"
    elias colere "Parce que t'avais pris le mauvais passage !"
    "Je rigole. Tomas secoue la tête."
    kael calme "Pour l'objet personnel, on attend demain. Aujourd'hui, personne entre dans leur chambre."
    if j28_secret_target == "iris":
        tomas raison "Surtout Iris. Si elle nous repère, c'est fini."
    else:
        tomas raison "Même Julian. On en parle avant, pas d'initiative dans notre coin."
    elias neutre "Ouais, compris. Allez, on y va."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_EXPEDITION

label _28_0_1_1_0_0_1_EXPEDITION:
    $ current_period = "Après-midi"
    call show_custom_title("En début d'après-midi") from _call_j28_secret_title_afternoon
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.6
    $ flashlight_on(0)
    "Elias pousse son sac dans le conduit. Il se coince régulièrement et il commence à s'énerver."
    $ showGroup([("elias", "fatigue", 0.30), ("noam", "neutre", 0.70)])
    elias fatigue "Putain, il passe pas, ce sac !"
    noam taquin "C'est toi qui l'as pris."
    elias neutre "Je sais ! J'avais pas prévu que ça serait aussi étroit !"
    "Il tire dessus d'un coup sec. Le sac passe enfin."
    noam reflexion "Pourquoi tu voulais pas choisir Iris ?"
    elias fatigue "Parce que si elle nous voit, elle va nous mettre une raclée. Et puis... j'ai pas envie de lui faire ça."
    noam raison "Et à Julian, ça te dérange pas ?"
    elias neutre "Bien sûr que si ! Je dis juste que ça sera moins compliqué."
    "On arrive à une bifurcation. Elias cherche son chemin."
    elias fatigue "Franchement, j'aurais préféré qu'on ait pas à choisir. Mais il faut bien faire quelque chose."
    noam inquiet "T'as quand même remplacé ton original, toi."
    elias neutre "Ouais."
    "Son sac se coince encore. Il jure entre ses dents."
    elias colere "Putain de saloperie..."
    noam reflexion "T'avais jamais pensé à lui parler ?"
    elias fatigue "Pour lui dire quoi ? Salut, c'est moi, mais pas vraiment moi ? Il m'aurait cru ?"
    noam neutre "Je sais pas. T'aurais pu essayer."
    elias reflexion "J'y ai pensé, d'accord ? Plusieurs fois."
    "Il finit par tirer le sac et se tourne vers moi."
    elias fatigue "Au début, j'étais content d'être à sa place. Enfin, je croyais que ça me ferait du bien. Mais maintenant, quand je rentre dans sa chambre, j'ai parfois l'impression que je devrais pas être là."
    noam inquiet "Tu regrettes ?"
    elias neutre "Je sais pas, Noam. Je sais vraiment pas."
    "Il récupère son sac, puis reprend."
    elias fatigue "Des fois, ouais. Mais c'est fait maintenant, alors... je sais pas."
    noam neutre "Ouais."
    elias neutre "Bon, aide-moi avec ce foutu sac."
    $ hideGroup()
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ flashlight_off()
    "On arrive dans la réserve. Elias ouvre plusieurs tiroirs et fouille parmi les pièces."
    $ showGroup([("elias", "reflechit", 0.32), ("noam", "reflexion", 0.68)])
    noam taquin "T'es sûr que c'est ici ?"
    elias fatigue "Ouais. Enfin, c'était ici la dernière fois. Attends."
    noam reflexion "Et si les pièces sont plus là ?"
    elias neutre "Bah on cherchera ailleurs ! Laisse-moi deux minutes."
    "Il sort un boîtier d'une caisse."
    elias joie "Ah ! Voilà, c'est ça !"
    noam sourire "Bon, ça au moins, c'est trouvé."
    elias rire "Je t'avais dit que c'était là !"
    "Je tiens le sac pendant qu'il vérifie les connecteurs."
    elias neutre "Tiens ça. Non, pas comme ça ! De l'autre côté... voilà."
    noam fatigue "Tu peux demander normalement, aussi."
    elias joie "Quoi ?"
    noam taquin "Non, rien. Continue."
    elias fatigue "Ouais, bah bouge pas alors."
    "On entend quelqu'un marcher de l'autre côté de la porte. Elias s'arrête immédiatement."
    elias inquiet "Chut. Baisse-toi !"
    noam peur "C'est qui ?"
    elias fatigue "J'en sais rien ! Baisse-toi, je te dis !"
    "On se cache derrière les caisses. Dans la pièce voisine, quelqu'un ouvre un tiroir."
    noam inquiet "Et s'il entre ici ?"
    elias neutre "Attends, laisse-moi écouter."
    noam surpris "Tu crois qu'il nous a entendus ?"
    elias fatigue "Si tu continues à parler, oui !"
    "Je me tais. Elias regarde la porte."
    elias fatigue "Putain, arrête de poser des questions !"
    "J'essaie de retenir un rire nerveux. Elias m'attrape le bras."
    "Les pas passent près de la porte, puis s'éloignent. On attend encore un peu."
    elias fatigue "Bon. La prochaine fois, je viens tout seul."
    noam sourire "Tu vas porter tout ça comment ?"
    elias neutre "Je trouverai quelqu'un qui parle moins."
    "Il remet les pièces dans le sac et le referme."
    elias neutre "C'est bon, on a tout. On rentre."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Au retour, le sac est encore plus lourd. On s'arrête à un endroit où on peut souffler."
    "Je profite de la pause pour regarder mon téléphone."
    call messenger_play("iris", "iris", [("iris", "Bon. Je suis peut-être un peu lourde avec mes messages."), ("iris", "Je voulais juste dire que j'ai passé un bon moment avec toi hier."), ("iris", "Et que j'aimerais bien recommencer. Voilà. C'est tout."), ("iris", "Enfin, pas TOUT, mais je vais arrêter de m'enfoncer.")], objective_text="Lire les messages d'Iris")
    "J'aimerais demander à Iris ce qui s'est passé hier. Mais si je fais ça, il faudra que je lui explique tout."
    elias neutre "Tu viens ?"
    noam fatigue "Ouais, j'arrive."
    elias rire "C'est Iris ?"
    noam inquiet "Ouais."
    elias neutre "Tu lui répondras après. Allez, on y va."
    $ hideGroup()
    $ flashlight_off()
    jump _28_0_1_1_0_0_1_RETOUR

label _28_0_1_1_0_0_1_RETOUR:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Nyra et Kael sont devant le terminal. Tomas a sorti ses notes. Elias pose le sac par terre."
    $ showGroup([("nyra", "reflexion", 0.14), ("kael", "calme", 0.34), ("elias", "fatigue", 0.54), ("noam", "inquiet", 0.80)])
    elias joie "Bon, j'ai trouvé les pièces."
    nyra reflexion "Toutes ?"
    elias agace "Tout ce qui manquait, oui."
    kael sourire "Bien."
    elias fatigue "Ouais, bah vous pourrez venir les porter la prochaine fois."
    nyra neutre "Tu les as vérifiées ?"
    elias colere "Mais oui, Nyra ! Tu crois que j'ai ramassé n'importe quoi ?"
    nyra reflexion "Je demande, c'est tout."
    elias fatigue "Bah oui. Elles marchent."
    "Kael intervient avant qu'ils se disputent encore."
    kael calme "On laisse tout ici. On verra le reste demain."
    noam reflexion "Et l'objet de la personne ?"
    if j28_secret_target == "julian":
        nyra raison "Pour Julian, il faudra trouver quelque chose dans sa chambre. Mais on attend demain."
        tomas raison "Et vous m'en parlez avant d'y aller. J'ai pas envie de découvrir ça après."
        elias fatigue "T'inquiète, j'ai assez rampé pour aujourd'hui."
        "Je pense à Julian. Il doit être tranquillement dans sa chambre, sans savoir ce qu'on prépare."
    else:
        nyra raison "Pour Iris, il faudra trouver un moment où elle sera pas dans sa chambre."
        elias fatigue "Bon courage. Elle reste presque tout le temps avec l'autre Noam."
        tomas raison "Alors on attend. On se précipite pas."
        "Je serre mon téléphone dans ma main. Iris m'a encore écrit, et ils préparent déjà la suite."
    sael mefiant "Et si elle nous surprend, on fait quoi ?"
    mara agace "On en parlera demain, Sael."
    sael raison "Non. Je veux qu'on y pense avant d'essayer."
    "Mara soupire. Tomas ferme son dossier."
    noam reflexion "Et Zero ? Il a répondu ?"
    kael calme "Toujours rien sur Keyper. Mais il sait qu'on a choisi quelqu'un pour Nexus."
    tomas fatigue "Super. Et il compte nous répondre quand ?"
    kael neutre "Je lui ai redemandé, Tomas. Dès que j'ai une réponse, je vous la donne."
    tomas agace "Je sais. Ça m'énerve, c'est tout."
    "Je les laisse parler et je sors. J'ai besoin d'être seul."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_OBSERVATION

label _28_0_1_1_0_0_1_OBSERVATION:
    $ current_period = "Soir"
    call show_custom_title("En fin d'après-midi") from _call_j28_secret_title_evening
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    $ flashlight_on(0)
    "J'ai besoin de m'éloigner du laboratoire. Je prends le conduit vers les dortoirs, puis m'arrête en entendant du bruit sous une grille qui donne sur la cafétéria."
    $ flashlight_off()
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    "Iris, Elen et Julian sont installés autour d'une table. Noam est avec eux."
    "Non. Pas Noam."
    $ showGroup([("julian", "sourire", 0.13), ("elen", "content", 0.37), ("dg_noam", "sourire", 0.63), ("iris", "sourire", 0.86)])
    julian sourire "Attends, attends ! Donc ta petite sœur te battait au baby-foot et tu veux qu'on te laisse jouer contre nous ?"
    dg_noam rire "J'ai pas dit qu'elle me battait tout le temps !"
    elen rire "Tu viens de dire qu'elle gagnait neuf parties sur dix !"
    dg_noam taquin "Oui, mais la dixième, je m'en souviens très bien."
    iris rire "T'es vraiment incapable de reconnaître une défaite, en fait."
    dg_noam sourire "C'est faux. Je reconnais très bien les défaites des autres."
    julian rire "Oh, ça, c'était gratuit !"
    "Ils rient tous. Moi, je reste derrière la grille."
    "L'histoire est vraie. Juliette gagnait presque toujours. Et je me rappelle parfaitement de cette dixième partie."
    iris taquin "Bon, demain, tu joues avec moi. Je veux voir ça."
    dg_noam sourire "Tu vas regretter de m'avoir proposé."
    iris rire "Oh, j'ai déjà des regrets, t'inquiète."
    elen content "Vous pourriez être gentils l'un avec l'autre cinq minutes ?"
    iris taquin "Mais je suis très gentille ! C'est lui qui cherche."
    dg_noam taquin "Je confirme. Elle est adorable."
    iris surpris "Ah ouais ?"
    dg_noam sourire "Ouais."
    "Iris ouvre la bouche pour répliquer. Elle n'y arrive pas tout de suite."
    iris agace "Pfff... Tu fais exprès."
    julian taquin "Je crois qu'on vient d'assister à un événement historique. Iris n'a plus rien à répondre."
    iris colere "Toi, je t'ai pas sonné !"
    "Elen éclate de rire. Mon double continue de sourire."
    "Il se passe une main derrière la nuque, exactement comme je le fais quand je suis gêné."
    think "Il a mes souvenirs. Même mes gestes. Et eux, ils voient rien."
    "Iris s'approche un peu de lui pour lui murmurer quelque chose. Je n'entends pas les mots, seulement le rire qu'il étouffe derrière sa main."
    "Je recule lentement. Je n'ai plus envie de voir la suite."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "À peine ai-je quitté la grille que mon téléphone vibre."
    call messenger_play("iris", "iris", [("iris", "T'as vu comment Julian a fait la tête ? J'en rigole encore."), ("iris", "Et arrête de raconter des trucs mignons sur ta sœur, après j'ai l'air bête à sourire toute seule."), ("iris", "Bon. À plus tard, idiot.")], objective_text="Lire le message d'Iris")
    "Je relis les messages. Elle vient de me raconter une conversation que j'ai entendue sans y participer."
    noam fatigue "Ouais... À plus tard."
    "Personne ne m'entend."
    $ j28_secret_iris_exchange = True
    $ flashlight_off()
    jump _28_0_1_1_0_0_1_FIN

label _28_0_1_1_0_0_1_FIN:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Le laboratoire est presque vide. Kael rassemble quelques documents pendant que les matériaux d'Elias attendent sur la table."
    $ showGroup([("kael", "calme", 0.33), ("noam", "fatigue", 0.69)])
    kael calme "Ah, te voilà. Je pensais que tu étais reparti te cacher dans les conduits."
    noam fatigue "J'ai failli. Mais je commence à détester dormir là-dedans."
    kael sourire "Tu m'étonnes."
    "Il referme un dossier."
    kael calme "J'ai renvoyé un message à Zero. Il devrait pouvoir nous répondre demain."
    noam reflexion "Sur Keyper ?"
    kael neutre "Entre autres. J'espère."
    noam inquiet "Tu sais, t'as pas l'air de beaucoup douter de lui."
    kael reflexion "Si, bien sûr que je doute. Mais je vois pas ce que ça changerait de le répéter toute la journée."
    noam raison "Je sais pas. Peut-être ceux qui te suivent."
    "Kael reste un instant silencieux."
    kael calme "C'est pas faux. Mais je lui dois assez pour vouloir entendre ce qu'il a à dire avant de décider qu'il nous a laissés tomber."
    noam reflexion "Assez comment ?"
    kael neutre "C'est une longue histoire. On en reparlera."
    "Il regarde le terminal puis revient vers moi."
    if j28_secret_target == "iris":
        kael calme "Pour Iris, on n'a encore rien tenté. Demain, on décidera comment récupérer ce qu'il faut et qui fait quoi."
        noam fatigue "Ouais. Je sais."
    else:
        kael calme "Pour Julian, même chose. On n'a fait que choisir son nom. On verra demain comment préparer le reste."
        noam fatigue "Ouais. Je sais."
    kael neutre "Tu peux encore dire que tu ne veux pas qu'on touche à ton original. Je préfère que tu le dises franchement plutôt que de nous laisser croire le contraire."
    noam inquiet "Et si je le dis, ça changera quelque chose ?"
    kael calme "Pour moi, oui. Pour tout le monde, je peux pas te le promettre."
    "Il reprend ses documents et se dirige vers la grille."
    kael neutre "Essaie de dormir un peu, Noam."
    noam neutre "Toi aussi."
    "Il me fait un signe et s'éloigne."
    $ hideGroup()
    $ j28_secret_zero_contact = True
    "Je reste seul dans le laboratoire. Je m'assois sur la banquette de la veille, puis sors mon téléphone."
    "Un nouveau message d'Iris s'affiche."
    call messenger_play("iris", "iris", [("iris", "Bon, avant que je change d'avis, faut que je te demande un truc."), ("iris", "Hier, quand tu m'as dit que tu voulais qu'on soit ensemble..."), ("iris", "Tu le pensais vraiment ?"), ("iris", "Parce que si c'était juste pour me faire rougir, je te préviens, je te déteste."), ("iris", "Et si c'était sérieux... bah moi aussi, abruti. ❤️")], objective_text="Lire le dernier message d'Iris")
    "Je lis une première fois. Puis une deuxième."
    "Mon double lui a dit qu'il voulait être avec elle."
    "Et Iris vient de lui répondre oui."
    "Je commence à taper une réponse. « Iris, il faut que je t'explique... » Je l'efface aussitôt."
    think "Je voulais lui dire. Mais c'était à moi de le faire."
    "Le téléphone reste allumé dans ma main. Je ne réponds pas."
    "À côté, les pièces récupérées avec Elias attendent qu'on décide quoi en faire. Sur le terminal éteint, le nom d'Iris ou de Julian a disparu, mais je sais qu'il y est enregistré."
    "Demain, ils prépareront la suite."
    "Et quelque part dans les dortoirs, un autre Noam se prépare peut-être à rejoindre Iris."
    stop music fadeout 1.5
    # Le J29 exploitera j28_secret_target. Aucune création ni remplacement au J28.
    call end_day("29", sleeping=True) from _call_j28_secret_end_day_29
    return
