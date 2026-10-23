# JOUR 28 — UNE PLACE POUR DEUX
# Route secrète : Noam se fait passer pour son Doppelgänger.
# Le choix Iris/Julian est enregistré ici ; aucune copie n'est créée ni aucun original remplacé avant J29.
# Contrat J29 : j28_secret_target = "iris" ou "julian".
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
    "J'ouvre les yeux devant un plafond que je ne reconnais toujours pas. Je me suis endormi sur une banquette du laboratoire, avec les genoux repliés et le téléphone coincé sous mon bras."
    "Pendant quelques secondes, je cherche pourquoi je ne suis pas dans ma chambre. Puis le visage de Mara, les dossiers de Keyper et surtout les deux messages d'Iris me reviennent d'un seul coup."
    think "« Tu m'avais promis de ne rien me cacher. »"
    "Je consulte l'heure. Il est encore tôt. Pas de réponse de mon double, évidemment : je n'ai même pas osé lui demander ce qu'il lui avait raconté."
    "La conversation d'Iris est toujours ouverte. Je pourrais lui répondre que je ne comprends pas, mais elle pense avoir passé la journée d'hier avec moi."
    noam fatigue "C'est pas possible..."
    "À la table, Tomas est déjà penché sur un écran. Il a dû dormir encore moins que moi."
    $ showGroup([("tomas", "fatigue", 0.34), ("noam", "fatigue", 0.68)])
    tomas fatigue "Si tu cherches du café, il n'y en a plus. Mara a tout pris et soutient maintenant que c'est une question de sécurité collective."
    noam fatigue "Je cherchais surtout à savoir quelle heure il est."
    tomas neutre "Huit heures passées. Kael veut nous voir tous ici ce matin, alors évite de disparaître dans tes conduits habituels."
    noam reflexion "Tous ? Même ceux qui sont censés être avec les représentants ?"
    tomas raison "Ceux qui peuvent venir sans se faire remarquer. Il dit avoir eu des nouvelles de Zero."
    "Je relève immédiatement la tête. Zero. Le nom que tout le monde prononce comme s'il devait suffire à régler leurs problèmes."
    noam reflexion "Il va venir ?"
    tomas neutre "Non, Kael n'a rien dit de pareil. Il a parlé d'une réunion, pas d'une visite."
    noam inquiet "Et pour Keyper ? Il a répondu ?"
    tomas fatigue "J'espère bien. Mais je préfère attendre de savoir ce qu'il a réellement dit."
    "Tomas retourne à ses fichiers et je baisse les yeux vers mon téléphone au moment où il vibre."
    call messenger_play("iris", "iris", [("iris", "T'es déjà levé, ou tu comptes encore me faire attendre une éternité ?"), ("iris", "Et oui, je sais, je râle dès le matin. Tu vas survivre."), ("iris", "C'était bien, hier. Même si t'as été franchement bizarre sur la fin.")], objective_text="Lire les messages d'Iris")
    "Je relis le dernier message, partagé entre le soulagement de la savoir en vie et la colère de comprendre qu'elle remercie quelqu'un d'autre."
    think "Bien, hier ? Qu'est-ce qu'ils ont fait après le vote ?"
    tomas reflexion "Un problème ?"
    noam hesitation "Non. Enfin, je crois pas."
    tomas raison "Ça n'a pas l'air convaincant, mais je vais me contenter de ça."
    "Je ferme la conversation avant de commettre l'erreur de lui répondre. Pour Iris, le Noam qui a passé la journée avec elle est encore quelque part dans les dortoirs."
    "Pour moi, il est devenu impossible de savoir ce qu'elle attend désormais de lui."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_REUNION

label _28_0_1_1_0_0_1_REUNION:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.9
    "Mara entre la première, une tasse brûlante à la main. Elias la suit avec une caisse d'outils dont le contenu s'entrechoque à chaque pas."
    "Nyra arrive peu après avec Sael. Je l'avais peu entendue jusque-là : elle n'a pourtant pas l'air de venir assister silencieusement à la réunion."
    "Kael ferme la grille derrière eux et vérifie la tablette posée au centre de la table."
    $ showGroup([("kael", "calme", 0.06), ("nyra", "neutre", 0.20), ("mara", "neutre", 0.34), ("tomas", "neutre", 0.48), ("elias", "fatigue", 0.62), ("sael", "neutre", 0.76), ("noam", "inquiet", 0.91)])
    mara taquin "Bon, on peut commencer ? J'ai dû expliquer à un Goumi que mon café était pas une pièce détachée, alors j'aimerais avoir une bonne raison de m'être levée."
    elias fatigue "T'as surtout piqué le café de tout le monde."
    mara rire "Voilà, exactement. Et je compte le rentabiliser."
    kael calme "J'ai eu un échange avec Zero. Il considère que nous sommes proches du résultat recherché, mais il reste deux districts qui ne sont pas correctement couverts."
    noam reflexion "Couverts ?"
    kael calme "Infiltrés. Les autres secteurs ont déjà au moins une personne capable de tenir une place parmi les représentants."
    "Il affiche six noms de districts sur le terminal. Deux restent signalés comme incomplets : HARMONIE et NEXUS."
    tomas raison "Je précise qu'on parle d'infiltration, pas d'une liste de droits de passage pour la navette. Les registres de transfert sont toujours incomplets."
    mara agace "On peut aussi parler de ce qui nous reste à faire au lieu de repartir sur Keyper pendant trois heures ?"
    kael calme "Harmonie dépend de Noam. Et pour Nexus, ni Julian ni Iris n'ont été remplacés."
    "Je baisse les yeux juste assez pour ne pas laisser paraître le choc. Je connaissais les doubles déjà installés dans le laboratoire ; je n'avais jamais vu leur situation présentée aussi froidement."
    elias reflexion "Et on a encore du temps pour fabriquer quelqu'un ?"
    kael calme "Pour une seule personne, oui. Le départ approche et il nous reste deux jours utiles. Zero ne prévoit pas d'autre fenêtre."
    noam inquiet "Pourquoi une seule ?"
    elias fatigue "Parce qu'un double, ça sort pas d'une imprimante à jouets, bordel. Il faut les pièces, le milieu biologique, le réglage et surtout du temps. Même en lançant ça maintenant, on pourra pas recommencer une seconde fois."
    tomas raison "Il faut également un objet ayant appartenu à l'original. Les données seules ne suffisent pas à obtenir une copie suffisamment fidèle."
    noam reflexion "Un objet personnel ?"
    elias neutre "Ouais. Un truc qu'il a réellement utilisé, pas une saloperie ramassée au hasard. Ça nous aide à affiner la copie. Je vais pas te faire un cours, mais sans ça, la finition est moins bonne."
    nyra raison "Et il nous manque encore une partie des matériaux. Elias devra aller les récupérer avant qu'on puisse lancer quoi que ce soit."
    noam inquiet "Donc vous comptez faire un nouveau double aujourd'hui ?"
    kael calme "Non. Aujourd'hui, il faut décider qui et réunir ce qui manque. La préparation de l'opération viendra ensuite."
    "Je respire un peu mieux. Pas longtemps."
    mara reflexion "Bon. Deux candidats, un seul créneau. On va éviter de faire comme si la réponse était évidente."
    nyra raison "Julian est le choix le plus simple. Sa grille d'aération n'a pas été condamnée. Il se déplace seul, il passe du temps à la cafétéria et une intervention dans sa chambre serait relativement facile à organiser."
    elias raison "Voilà. Pour une fois, on pourrait faire quelque chose sans risquer de se faire arracher la tête."
    sael mefiant "Tu parles d'entrer dans la chambre d'un homme qui dort. Je ne suis pas sûre que le mot « facile » soit approprié."
    elias fatigue "J'ai pas dit que ça me faisait plaisir. J'ai dit que ça serait moins compliqué."
    tomas raison "En plus, remplacer Julian permettrait au moins de couvrir Nexus. On n'a aucune raison de compromettre tout le monde avec une opération plus difficile."
    nyra neutre "Si. Nous en avons une."
    "Nyra touche l'écran. Le nom de Julian disparaît et celui d'Iris reste seul."
    nyra raison "Iris est beaucoup plus difficile à approcher. Elle passe presque tout son temps avec l'original de Noam, elle se méfie facilement et elle sait se défendre."
    nyra raison "Mais si nous parvenons à la remplacer, l'original de Noam perdra la personne qui le protège en permanence. Harmonie pourrait alors être infiltré à son tour."
    "Je relève brusquement la tête. Elle vient de décrire Iris comme un obstacle à faire disparaître."
    mara reflexion "Autrement dit, un seul nouveau double, deux districts réglés. Ça me plaît déjà davantage."
    tomas desaccord "Uniquement si Noam décide réellement de remplacer son original. Ce n'est pas ce qu'il nous a dit hier."
    nyra raison "Je n'ai jamais prétendu le contraire. Mais retirer un obstacle n'oblige personne à agir ; cela rend simplement l'opération possible."
    noam colere "Vous pourriez arrêter de parler d'Iris comme d'un verrou qu'il suffit de démonter ?!"
    "Mara repose brutalement sa tasse."
    mara agace "On parle de tout le monde comme ça depuis le début, Noam ! Tu découvres seulement maintenant que c'est dégueulasse ?"
    noam inquiet "Non. C'est justement pour ça que je vous demande d'arrêter."
    nyra reflexion "Tu as le droit de refuser d'agir contre ton original. Mais nous devons décider de ce que nous faisons pour Nexus, indépendamment de ton refus."
    sael raison "Et si Iris résiste ? Vous avez prévu quoi ?"
    nyra neutre "C'est précisément le problème. Avec Julian, le risque immédiat est faible. Avec Iris, il est élevé, mais le bénéfice potentiel l'est aussi."
    elias colere "Ouais, enfin, « bénéfice potentiel », c'est joli sur ton tableau. Moi, je te rappelle qu'elle peut envoyer n'importe lequel d'entre nous à l'infirmerie avant qu'on ait sorti une phrase."
    mara rire "Je confirme, j'ai pas particulièrement envie de vérifier combien de dents elle peut faire sauter."
    tomas raison "Il faut distinguer trois choses : créer une copie, atteindre l'original et réussir à tenir sa place. Même si la première étape réussit, les deux autres ne sont pas garanties."
    kael calme "C'est pour cette raison que nous ne lançons rien sans accord."
    noam reflexion "Et Zero, il veut qui ?"
    kael calme "Zero veut Nexus infiltré. Il nous laisse choisir le moyen. C'est tout ce que je peux confirmer."
    noam inquiet "Vous trouvez pas bizarre qu'il soit capable de fixer des objectifs sans vous expliquer pourquoi il faut absolument remplir toutes ces cases ?"
    mara agace "Tu veux qu'on commence à remettre en cause l'ensemble du plan à deux jours du départ ?"
    tomas raison "Ce n'est pas une question absurde, Mara. Je préfère simplement qu'on la traite séparément, sans prétendre qu'on aura les réponses maintenant."
    "Le téléphone vibre dans ma poche. Je connais déjà le nom avant de regarder l'écran."
    call messenger_play("iris", "iris", [("iris", "Au fait, j'ai réfléchi à ce que tu m'as dit après le vote."), ("iris", "Je crois qu'on devrait arrêter de tourner autour du pot tous les deux."), ("iris", "Et ne me sors pas ton air innocent. Tu sais très bien de quoi je parle.")], objective_text="Lire le nouveau message d'Iris")
    "Je sens mes joues chauffer. Hier, j'étais seul dans ce laboratoire pendant que mon double lui parlait. Maintenant elle me répond comme si nous avions pris une décision ensemble."
    think "Qu'est-ce que tu lui as dit ?"
    mara taquin "Hé, le rêveur ! On est en train de décider quelque chose, là. Tu veux revenir sur Terre cinq minutes ?"
    noam hesitation "Ouais. Je vous écoute."
    nyra raison "Alors écoute bien. Avec Julian, Nexus peut être infiltré plus facilement. Avec Iris, nous prenons plus de risques, mais Harmonie devient potentiellement accessible."
    sael mefiant "Et dans les deux cas, une personne peut perdre sa place. C'est aussi un élément de la décision."
    kael calme "Je crois que nous avons tous compris les arguments."
    "Il regarde successivement Tomas, Mara et Elias. Aucun ne bouge."
    kael calme "Noam, tu es le premier concerné par la seconde option. Si tu refuses, Iris devient un choix beaucoup moins intéressant. Je veux savoir quelle possibilité tu es prêt à défendre."
    "Je pourrais tout arrêter en disant que je suis le véritable Noam. Mais ils sauraient immédiatement que je les ai trompés depuis deux jours, et je ne sais pas ce qu'ils feraient à Iris ou à Julian."
    "Si je refuse de répondre, ils choisiront sans moi. Si je réponds, j'aurai moi-même désigné quelqu'un."
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
    noam raison "Julian. Je pense qu'il faut choisir Julian."
    nyra reflexion "Tu choisis la solution qui demande le moins de risques immédiats."
    noam inquiet "Oui. Et je refuse que vous considériez Iris comme un moyen de me forcer à faire quelque chose."
    tomas raison "Ce n'est pas déraisonnable. Julian reste une option suffisante pour Nexus."
    mara agace "Suffisante, ouais. Pour Harmonie, on pourra toujours aller se faire voir."
    elias neutre "Pour Harmonie, il peut encore changer d'avis sans qu'on lui colle un pistolet sous le nez. C'est pas obligé de se décider dans cette pièce."
    "La colère de Mara ne m'atteint presque pas. Je viens peut-être de sauver Iris, mais seulement en donnant le nom de Julian."
    think "Je lui ai parlé hier. Il m'a jamais rien fait."
    kael calme "D'accord. Nous préparons l'option Julian. Aucun remplacement n'est décidé pour aujourd'hui."
    jump _28_0_1_1_0_0_1_APRES_CHOIX

label _28_0_1_1_0_0_1_IRIS:
    $ j28_secret_target = "iris"
    noam fatigue "Iris. Si vous voulez vraiment maximiser vos chances, c'est Iris."
    "Je prononce son prénom et j'ai aussitôt envie de le reprendre."
    mara surpris "Eh ben... Je pensais vraiment pas t'entendre dire ça."
    nyra raison "C'est la stratégie la plus ambitieuse. Pas la plus facile."
    tomas desaccord "Je m'y oppose. On ne peut pas décider d'une opération contre Iris sur la seule promesse que Noam remplacera ensuite son original."
    noam inquiet "J'ai pas promis ça ! Je dis seulement que, si vous devez choisir, c'est l'option qui correspond à votre objectif."
    elias fatigue "Putain, je sens déjà que je vais regretter cette réunion."
    sael mefiant "Si on retient Iris, il faudra au minimum éviter toute intervention précipitée. Elle est constamment avec quelqu'un et elle réagit vite."
    kael calme "Très bien. Nous étudions l'option Iris, sans lancer de remplacement aujourd'hui. Et personne ne prendra de décision à la place de Noam pour Harmonie."
    "Tomas me regarde longtemps avant de détourner les yeux. J'ai obtenu exactement ce que je voulais éviter : ils me croient prêt à sacrifier Iris pour leur plan."
    think "Elle m'écrit depuis ce matin. Et moi, je viens de donner son nom."
    jump _28_0_1_1_0_0_1_APRES_CHOIX

label _28_0_1_1_0_0_1_APRES_CHOIX:
    $ j28_secret_plan_decided = True
    $ current_period = "Midi"
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.18), ("kael", "calme", 0.39), ("tomas", "reflexion", 0.61), ("noam", "inquiet", 0.83)])
    elias neutre "Bon. Maintenant qu'on a fini de se bouffer le nez, j'ai besoin de matériel. Et je vais pas le sortir de ma poche."
    kael calme "Dis-nous ce qu'il manque."
    elias raison "Des raccords pour la chambre, deux boîtiers de contrôle et un lot de supports neufs. J'ai repéré une réserve technique dans le secteur de maintenance. Elle n'est pas sur notre trajet habituel."
    tomas reflexion "Il faut que quelqu'un t'accompagne. Une personne seule avec une caisse pleine de pièces, ça attire vite l'attention."
    noam hesitation "Je peux venir."
    elias surpris "Toi ? Après la tronche que tu tirais pendant la réunion ?"
    noam fatigue "Justement. J'ai besoin de bouger."
    elias neutre "Bon. Mais tu touches à rien avant que je te dise ce qu'on prend."
    kael calme "Et aucun objet personnel aujourd'hui. Nous avons décidé de la cible, pas de la façon de l'approcher. Ce point sera préparé demain."
    if j28_secret_target == "iris":
        tomas raison "C'est particulièrement important pour Iris. Aucun contact improvisé."
    else:
        tomas raison "Même pour Julian, nous ne nous permettrons pas une intrusion improvisée."
    "Mara marmonne quelque chose derrière nous. J'attrape une petite lampe, heureux de pouvoir sortir de cette pièce avant qu'elle recommence."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_EXPEDITION

label _28_0_1_1_0_0_1_EXPEDITION:
    $ current_period = "Après-midi"
    call show_custom_title("En début d'après-midi") from _call_j28_secret_title_afternoon
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    play music "music/bgm_cold_metadata.mp3" fadein 0.6
    "Elias avance devant moi dans le conduit. Il traîne un sac souple qui cogne contre les plaques à chaque changement de direction."
    $ showGroup([("elias", "fatigue", 0.32), ("noam", "inquiet", 0.69)])
    elias fatigue "La prochaine fois, je prends quelqu'un de moins grand. Tu bloques toute la circulation."
    noam fatigue "Y a une circulation, maintenant ?"
    elias sourire "Ouais, moi. Et j'aimerais bien circuler."
    "Je parviens à sourire malgré moi. Il y a quelque chose d'absurde à plaisanter avec l'homme qui prépare peut-être le remplacement de l'un de mes amis."
    noam reflexion "Elias, tout à l'heure... Quand Nyra parlait de deux districts d'un coup, t'avais pas l'air convaincu."
    elias neutre "J'étais pas convaincu. Ça te surprend ?"
    noam raison "T'as pourtant participé aux autres remplacements."
    elias fatigue "Et ça veut dire que je dois être content de recommencer ?"
    "Je n'ai pas de réponse. Elias s'arrête devant une intersection, pose le sac et vérifie l'espace derrière une grille."
    elias raison "Je vais te dire un truc. Au début, j'étais persuadé qu'en prenant une place, tout deviendrait normal. T'as les souvenirs, le visage, les gens qui t'attendent... Qu'est-ce qui pourrait manquer ?"
    noam inquiet "Et alors ?"
    elias fatigue "Et alors y a pas de bouton pour effacer ce que t'as fait avant. Même quand tout le monde te sourit."
    "Il reprend le sac avec une grimace."
    elias neutre "Allez. C'est pas le moment de faire une séance chez Sael. On a des pièces à trouver."
    $ hideGroup()
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ flashlight_off()
    "Nous débouchons dans une partie encombrée de l'atelier. Elias observe les étagères et ouvre un premier boîtier."
    $ showGroup([("elias", "reflechit", 0.34), ("noam", "reflexion", 0.69)])
    elias reflexion "Les raccords devraient être là. Enfin... Si personne s'en est servi pour réparer un autre truc."
    noam reflexion "Tu sais précisément quoi prendre ?"
    elias neutre "Plus ou moins. L'idée, c'est surtout de pas embarquer tout l'atelier et de laisser une panne derrière nous."
    "Nous passons plusieurs minutes à comparer des boîtiers identiques, jusqu'à ce qu'Elias en trouve un dont les connecteurs ne sont pas abîmés."
    elias joie "Ah ! Voilà ! Tu vois, quand je dis que je retrouve toujours mes affaires, c'est pas complètement du bluff."
    noam taquin "Tu viens de passer dix minutes à dire que quelqu'un avait volé tes pièces."
    elias rire "Ouais, bah il les avait rangées au mauvais endroit. C'est presque pareil."
    "Je place les pièces dans le sac pendant qu'il vérifie le dernier tiroir. Des voix résonnent soudain dans le couloir voisin."
    noam peur "Elias..."
    elias inquiet "Ouais, j'ai entendu. Ferme le sac, doucement."
    "Nous nous immobilisons. Quelqu'un s'arrête de l'autre côté de la cloison. Je distingue le bruit d'un outil qu'on pose sur une table."
    noam inquiet "C'est qui ?"
    elias fatigue "Comment tu veux que je sache ? Si j'avais une fenêtre, je regarderais."
    "La personne semble chercher quelque chose. Un tiroir coulisse, puis un second."
    "Elias m'indique du menton le passage entre deux rangées de caisses. Je m'y glisse en retenant ma respiration."
    "Après une interminable minute, les pas s'éloignent enfin."
    elias fatigue "Bon. Voilà pourquoi je voulais pas venir tout seul."
    noam reflexion "Parce que je suis utile ?"
    elias neutre "Parce que si on se fait coincer, au moins je pourrai dire que c'était ton idée."
    "Il pousse le sac dans mes bras. Je le rattrape de justesse."
    noam colere "Très drôle."
    elias rire "Je sais. Allez, on dégage."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Nous repartons avant que quelqu'un décide de revenir. Les pièces pèsent beaucoup plus lourd que prévu et Elias doit plusieurs fois m'aider à passer les intersections."
    "Je profite d'une courte pause pour consulter mon téléphone."
    call messenger_play("iris", "iris", [("iris", "Bon, puisque monsieur est occupé, je vais parler toute seule."), ("iris", "J'ai toujours trouvé ça un peu ridicule, les gens qui se cherchent pendant des semaines sans jamais rien se dire."), ("iris", "Et apparemment, je suis en train de faire exactement pareil. Génial."), ("iris", "Réponds quand tu peux. Et arrête de sourire comme un idiot en lisant ça, je te vois d'ici.")], objective_text="Lire les messages d'Iris")
    "Je fixe la dernière phrase. Elle a raison sur un point : je souris malgré moi. Mais le sourire disparaît presque aussitôt."
    think "Elle pense parler à celui qui l'a regardée hier. Pas à moi."
    elias neutre "On repart ?"
    noam fatigue "Ouais. Désolé."
    $ hideGroup()
    $ flashlight_off()
    jump _28_0_1_1_0_0_1_RETOUR

label _28_0_1_1_0_0_1_RETOUR:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Lorsque nous revenons au laboratoire, Kael et Nyra sont en pleine discussion devant un terminal. Tomas prend des notes à l'écart."
    $ showGroup([("nyra", "reflexion", 0.15), ("kael", "calme", 0.35), ("elias", "fatigue", 0.55), ("noam", "inquiet", 0.78)])
    elias joie "Livraison ! Et pour une fois, j'ai pas cassé le contenu en route."
    nyra neutre "Il faudra vérifier les pièces avant de les installer."
    elias agace "Tu crois vraiment que j'ai traîné ce sac sur la moitié de la station pour rapporter des boulons au hasard ?"
    nyra raison "Non. Mais nous n'avons pas les moyens de découvrir une pièce défectueuse après le lancement."
    elias fatigue "Ouais, bon. Je vais vérifier, alors."
    "Elias vide le sac devant eux et commence à trier les composants. Je reste près de la porte, incapable de rejoindre leur enthousiasme."
    kael calme "Nous disposons maintenant des matériaux manquants. C'est une étape, pas une autorisation d'agir."
    noam reflexion "Et pour l'objet personnel ?"
    nyra raison "Il faudra en obtenir un qui appartienne réellement à la cible. On ne va pas improviser une récupération aujourd'hui."
    if j28_secret_target == "julian":
        nyra raison "La chambre de Julian reste accessible par les conduits. Nous avons donc une option relativement simple à préparer pour demain."
        tomas raison "Simple ne veut pas dire sans conséquence. Je veux qu'on vérifie le trajet et le moment avant toute tentative."
        "Je pense au sourire de Julian, à ses plaisanteries devant le café. Depuis ce matin, tout ce qu'il fait peut devenir une information utile pour ceux qui comptent lui prendre sa place."
    else:
        nyra raison "Pour Iris, c'est plus difficile. Elle reste proche de l'original de Noam et sa chambre ne peut pas être approchée aussi facilement."
        kael calme "Dans ce cas, nous devons préparer un moyen de l'éloigner sans éveiller ses soupçons. Nous ne déciderons pas de cela dans l'urgence."
        "Je serre les doigts autour de mon téléphone. Le même appareil sur lequel Iris m'a envoyé des messages presque tendres toute la journée."
    sael mefiant "Je veux aussi savoir ce qu'on fera si la personne choisie découvre l'opération. Ça mérite d'être discuté avant, pas une fois qu'elle sera devant nous."
    mara agace "On peut au moins finir une étape sans annoncer toutes les catastrophes possibles ?"
    tomas raison "Non, Mara. Pas cette fois."
    "Le ton de Tomas arrête net la discussion. Mara hausse les épaules, mais ne répond pas."
    noam reflexion "Et Zero ? Vous avez pu lui demander pour Keyper ?"
    kael calme "Je lui ai transmis les références que nous possédons. Il veut d'abord savoir si nous parvenons à terminer le plan ici."
    tomas desaccord "Ça ne répond pas à la question."
    kael calme "Je sais. Je compte lui redemander."
    "Je regarde autour de moi. Ils veulent tous quitter cet endroit, mais aucun ne semble savoir avec certitude ce qui les attend s'ils échouent."
    "Le pire, c'est que je comprends maintenant leur peur. Et que cela ne m'empêche absolument pas d'avoir peur d'eux."
    $ hideGroup()
    jump _28_0_1_1_0_0_1_OBSERVATION

label _28_0_1_1_0_0_1_OBSERVATION:
    $ current_period = "Soir"
    call show_custom_title("En fin d'après-midi") from _call_j28_secret_title_evening
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    $ flashlight_on(0)
    "Je prétexte vouloir me reposer et quitte le laboratoire. En réalité, je n'arrive plus à supporter le bruit des outils derrière moi."
    "Je connais assez bien le chemin des dortoirs pour revenir jusqu'à une grille donnant sur la cafétéria. J'entends des voix et je m'immobilise."
    $ flashlight_off()
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    "Julian est assis à une table avec Elen et Iris. Un quatrième personnage leur tourne légèrement le dos. Je connais sa silhouette avant même qu'il relève la tête."
    "C'est moi. Ou plutôt celui qui porte mon visage."
    $ showGroup([("julian", "sourire", 0.13), ("elen", "content", 0.37), ("dg_noam", "sourire", 0.63), ("iris", "sourire", 0.86)])
    julian sourire "Tu peux raconter ce que tu veux, Noam, mais je refuse de croire que tu étais aussi nul au baby-foot."
    dg_noam rire "J'ai jamais dit que j'étais nul ! J'ai dit que ma sœur me battait quand on était petits."
    elen rire "C'est encore pire !"
    iris taquin "Moi je trouve ça plutôt mignon. Au moins, il sait perdre sans nous faire un discours de vingt minutes."
    julian sourire "Pardon ? Je prends cette attaque personnellement."
    "Je reste immobile derrière la grille. Il vient de parler de Juliette. De ma sœur. D'un souvenir qui m'appartient et qu'il raconte comme s'il avait vécu à ma place."
    dg_noam taquin "Julian, si tu veux, on peut refaire une partie demain. Je te laisserai même gagner les dix premières secondes."
    julian rire "Voilà qui est insultant, mais généreux."
    "Elen rit. Iris se penche vers mon double et lui donne un léger coup de coude."
    iris sourire "Fais pas trop le malin, toi. Je t'ai vu jouer."
    dg_noam sourire "Je me défends."
    iris taquin "C'est bien ce qui m'inquiète."
    "Ils échangent un sourire que je ne connais pas. Aucun des autres ne remarque quoi que ce soit d'anormal."
    "Je pourrais frapper contre la grille. Dire que je suis là, que le Noam assis avec eux n'est pas celui qu'ils croient. Mais cela reviendrait à provoquer une catastrophe dont je ne maîtrise rien."
    think "Ils sont bien ensemble. Ils ont même pas besoin que je sois là."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je recule enfin. Le métal gémit sous mon poids, juste assez pour me faire sursauter. Personne ne vient regarder derrière la grille."
    "Mon téléphone vibre encore. Pour la première fois aujourd'hui, je voudrais qu'il s'arrête."
    call messenger_play("iris", "iris", [("iris", "Tu sais, quand t'as parlé de ta sœur tout à l'heure, j'ai trouvé ça adorable."), ("iris", "Voilà, je l'ai dit. Profites-en, ça arrivera pas souvent."), ("iris", "Et au fait : c'est moi ou t'es devenu vachement plus courageux pour dire ce que tu ressens ?")], objective_text="Lire le message d'Iris")
    "Elle vient de me décrire une scène que j'ai observée depuis un conduit. Comme si j'avais été assis à côté d'elle, avec ma tasse sur la table."
    noam fatigue "Arrête..."
    "Je ne sais même pas à qui je parle. À Iris, qui ne peut pas m'entendre ? À mon double, qui ne sait pas que je suis juste derrière le mur ? Ou à moi-même, qui continue de laisser tout cela se produire ?"
    $ j28_secret_iris_exchange = True
    $ flashlight_off()
    jump _28_0_1_1_0_0_1_FIN

label _28_0_1_1_0_0_1_FIN:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Le laboratoire s'est vidé lorsque je reviens. Seul Kael travaille encore devant un terminal, tandis que les pièces rapportées par Elias sont soigneusement alignées sur la table."
    $ showGroup([("kael", "calme", 0.33), ("noam", "fatigue", 0.69)])
    kael calme "Tu es rentré. Je me demandais si tu allais encore dormir dans les conduits."
    noam fatigue "J'y ai pensé, mais j'ai pas envie de me réveiller avec une barre dans le crâne."
    kael sourire "C'est un argument acceptable."
    "Il referme une fenêtre sur son écran."
    kael calme "J'ai de nouveau contacté Zero. Nous devrions obtenir des réponses demain."
    noam reflexion "Sur Keyper ?"
    kael neutre "Sur ce qu'il sera possible de faire ensuite. Je n'ai rien de plus précis à te promettre."
    noam inquiet "Vous lui faites vraiment confiance, tous ?"
    kael calme "Pas de la même manière. Certains lui doivent beaucoup. D'autres voudraient lui poser exactement les questions que tu poses."
    noam raison "Et toi ?"
    kael neutre "Moi, je préfère lui parler plutôt que de décider ce qu'il pense à sa place."
    "Je ne réponds pas. Il y a quelque chose dans sa prudence qui me rappelle Tomas, mais Kael ne donne pas l'impression d'avoir peur de ce que Zero pourrait dire."
    if j28_secret_target == "iris":
        kael calme "La décision concernant Iris est enregistrée. Demain, nous verrons comment préparer cette option. Personne n'agit cette nuit."
        "Je contemple son nom sur le terminal. Je l'ai prononcé devant tout le monde. Je ne peux même pas prétendre que je n'étais pas là."
    else:
        kael calme "La décision concernant Julian est enregistrée. Demain, nous préparerons cette option. Personne n'agit cette nuit."
        "Je contemple son nom sur le terminal. Iris est peut-être à l'abri pour le moment, mais ce n'est pas une bonne nouvelle pour Julian."
    kael calme "Essaie de dormir. Nous aurons besoin de toi demain."
    "Il éteint le terminal et s'éloigne vers les conduits. Je reste seul avec le bourdonnement des appareils et mes pensées."
    $ hideGroup()
    $ j28_secret_zero_contact = True
    "Je m'assois sur la banquette et reprends mon téléphone. J'ai reçu des messages d'Iris toute la journée sans être capable de lui répondre correctement."
    "Un dernier message apparaît."
    call messenger_play("iris", "iris", [("iris", "Bon. Je sais que t'es occupé, alors je vais faire simple."), ("iris", "J'ai repensé à ce que tu m'as dit hier, après le vote."), ("iris", "Quand t'as dit que tu voulais qu'on arrête de faire semblant et qu'on soit ensemble..."), ("iris", "Tu le pensais vraiment, hein ?"), ("iris", "Parce que moi, oui. Et si tu te moques de moi demain, je te jure que je te tue. ❤️")], objective_text="Lire le dernier message d'Iris")
    "Je lis les phrases plusieurs fois. Il lui a dit qu'il voulait être avec elle. Il a utilisé mes mots, mes souvenirs, mon visage, et il lui a fait une promesse à laquelle je n'ai jamais participé."
    "Je commence à écrire une réponse, puis je l'efface. Je pourrais lui dire que moi aussi je le veux, mais elle croirait que je confirme une conversation que nous n'avons jamais eue."
    think "Je voulais lui parler. Lui dire ce que je ressentais, un jour. Pas apprendre qu'un autre l'avait fait pour moi."
    "Je pose le téléphone à côté de moi, l'écran encore allumé."
    "Sur la table, les matériaux récupérés cet après-midi attendent d'être utilisés. Demain, quelqu'un commencera à préparer la copie d'Iris ou de Julian."
    "Il me reste deux jours avant la navette. Deux jours pour retrouver ma place, prévenir les autres, comprendre Zero et découvrir ce qui attend ceux qu'on laissera derrière."
    "Je n'ai même pas réussi à répondre à un seul message d'Iris."
    stop music fadeout 1.5
    # Le jour 29_0_1_1_0_0_1 utilisera j28_secret_target et préparera le plan choisi.
    # Ne pas déclencher ici une création ou un remplacement.
    call end_day("29", sleeping=True) from _call_j28_secret_end_day_29
    return
