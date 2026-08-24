label _4_1_REVEIL_CHAMBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_206
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"

    $ showGroup([("noam", "inquiet", 0.50)])

    $ blink()
    think "Je me réveille avant l'annonce de Kami. La lumière des veilleuses est encore allumée."
    $ blink()
    think "Hier, nous avons tous voté pour rétablir le commerce. Pour la première fois, un amendement a été adopté."
    think "Sur le moment, j'étais surtout soulagé. On avait enfin réussi à changer quelque chose."
    think "Maintenant que je suis seul, je repense surtout à ce que le texte a supprimé avec les bons de rationnement."
    think "À Nexus ou à Orbite, les échanges devraient reprendre rapidement. À Limen, beaucoup de gens n'ont rien à vendre et presque rien à acheter."
    think "Si le nouveau système ne profite qu'à ceux qui avaient déjà des ressources, notre victoire risque de ne pas en être une pour tout le monde."

    play sound sfx_announce
    "L'écran mural s'allume dans un bip aigu."

    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Huit heures pile, mes petits pionniers du chaos ! Debout, la révolution n'attend pas !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit point matinal, puisque vous adorez qu'on vous mette le nez dans les conséquences de vos décisions."
    kami "À Nexus et Orbite, les premiers marchés improvisés sont déjà ouverts. Les objets circulent et de nouvelles monnaies locales apparaissent !"
    kami "Pendant ce temps, à Limen... Disons que les files d'attente sont plus longues que votre liste de regrets."
    kami "Quelques trocs sauvages, quelques bagarres et beaucoup de gens qui découvrent qu'une liberté ne remplit pas automatiquement un estomac."
    kami "Alors, mes champions du changement, toujours aussi fiers d'avoir appuyé sur le gros bouton vert ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais pourquoi est-ce que je vous raconte tout ? Les écrans de la cafétéria vous montreront les résultats en direct !"
    kami "Allez donc admirer votre toute première victoire. Vous l'avez bien mérité !"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_207
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    $ showGroup([("noam", "inquiet", 0.50)])

    think "L'écran s'éteint. Kami a évidemment choisi les images qui nous feront le plus douter, mais elle n'a probablement pas eu besoin d'inventer les files de Limen."

    play sound sfx_drop
    "Un bruit sourd traverse le couloir, suivi d'une voix étouffée. Quelqu'un vient certainement de se lever trop vite."
    think "Je devrais aller voir les résultats moi-même avant de commencer à regretter sur la seule parole de Kami."

    jump _4_1_CAFETERIA_ECRANS

# Durée : 1m35
# Total : 1h 55m 35s

label _4_1_CAFETERIA_ECRANS:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_208
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    $ showGroup([
        ("lysa", "determine"),
        ("kael", "calme"),
        ("ryn", "colere"),
        ("julian", "detendu"),
        ("mara", "joie"),
        ("tomas", "hesitation"),
        ("elen", "joie"),
        ("iris", "desaccord"),
        ("nyra", "raison"),
        ("noam", "raison"),
        ("sael", "mefiant"),
    ])

    think "La plupart des représentants sont déjà installés devant les écrans. Je prends une ration et m'assieds avec eux."
    "Une voix synthétique accompagne les images qui défilent : premiers marchés ouverts à Nexus, hausse des exportations à Orbite, files persistantes à Limen."

    lysa reflechit "Les gens commencent déjà à s'organiser. Même à Limen, certains ont mis en place des systèmes de troc."

    kael calme "À Orbite, les exportations augmentent plus vite que prévu. Les outils et les filtres partent en premier."

    ryn colere "Évidemment que ça fonctionne chez vous ! À Limen, ils commencent à se battre pour un sac de nourriture."
    ryn colere "Regardez la file devant l'ancien centre ! Ils attendent encore des rations qui n'arriveront plus !"

    julian detendu "Le système vient à peine de changer. Il faut laisser aux gens le temps de créer de nouveaux échanges."
    julian sourire "On ne peut pas demander un changement mondial et lui reprocher de ne pas être terminé avant le petit-déjeuner."

    mara taquin "Pour une fois, je suis plutôt d'accord avec lui. Profitez-en, ça n'arrivera probablement pas souvent."
    mara neutre "Mais Ryn a raison sur un point : ceux qui n'ont rien à échanger vont prendre cher en premier."

    tomas hesitation "Les prix bougent déjà beaucoup. À Nexus, certains produits ont presque doublé de valeur depuis hier."
    tomas reflechit "Ce n'est pas forcément durable, mais... Enfin, on manque encore de données."

    elen joie "C'est normal que ce soit un peu le bazar au début ! Les gens vont pouvoir vendre ce qu'ils fabriquent et choisir ce qu'ils veulent acheter."
    elen content "Avec un peu de chance, on pourra même retrouver du vrai chocolat ! Pas les barres qui ont juste la bonne couleur."

    iris desaccord "Choisir avec quel argent ? Ceux qui n'ont rien regarderont les autres acheter depuis le bout de la file."
    iris colere "On savait que supprimer les rations ferait ça. On a quand même voté pour."

    nyra raison "Alors il faut regarder ce qui manque au nouveau système au lieu de prétendre qu'il fonctionne déjà parfaitement."
    nyra reflechit "Sans règles communes, les premiers marchés profiteront forcément à ceux qui possèdent déjà le plus."

    noam reflexion "On a remplacé les bons du jour au lendemain. Les gens n'ont même pas eu le temps de comprendre avec quoi ils allaient payer."
    noam inquiet "Ça ne veut pas dire qu'on a forcément eu tort. Mais on aurait dû mieux prévoir la transition."

    sael mefiant "À Limen, les gens ont toujours échangé entre eux. Ils continueront."
    sael triste "Ceux qui n'ont plus rien dépendront seulement de voisins qui n'ont presque rien non plus."

    think "Sur l'écran, un homme quitte la file de Limen avec les mains vides. Ma ration est encore intacte devant moi."

    think "Lysa détourne enfin les yeux de l'écran pour me regarder."
    lysa determine "Tu regrettes déjà ?"
    lysa reflechit "Ce n'est pas toi qui voulais qu'on se batte pour changer les choses ?"
    lysa sourire "Au moins, là, on a réussi."

    noam hesitation "Je ne sais pas encore. J'aimerais seulement que notre victoire ne condamne pas ceux qu'on voulait aider."

    think "Personne ne célèbre plus vraiment le résultat d'hier. Nous continuons seulement de regarder ce qu'il produit."

    jump _4_1_TEMPS_LIBRE_1

# Durée : 1m20
# Total : 1h 56m 55s

label _4_1_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_209
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    think "Il reste encore plusieurs heures avant que Kami nous annonce la suite. Je devrais profiter de ce moment pour penser à autre chose."

    call START_FREE_TIME("_4_1_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_4_1

# Durée : 1m05
# Total : 1h 58m 0s

label _4_1_RETOUR_CONCLAVE_ANALYSE:
    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_210
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.8

    $ showGroup([("noam", "neutre", 0.50)])

    think "Je viens à peine de quitter mon temps libre lorsque l'alarme retentit dans le couloir."

    play sound sfx_announce

    $ hideGroup()
    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention, mes petits représentants adorés ! Rassemblement immédiat dans la salle principale."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Il est temps de préparer le prochain vote. Alors dépêchez-vous, nos téléspectateurs ne vont pas attendre la fin de vos siestes digestives !"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_211
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([("noam", "fatigue", 0.50)])

    think "Je prends la direction du Conclave. Les autres sortent peu à peu de leurs chambres et me rejoignent dans le couloir."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_212
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    $ showGroup([
        ("julian", "determine"),
        ("ryn", "colere"),
        ("elen", "inquiet"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("iris", "desaccord"),
        ("kael", "triste"),
        ("nyra", "raison"),
        ("noam", "raison"),
        ("lysa", "blase"),
        ("sael", "mefiant"),
    ])

    think "Nous sommes presque tous installés lorsque Julian vérifie une dernière fois les sièges."

    julian determine "Nous sommes au complet. Autant commencer dès que Kami daignera se montrer."

    ryn colere "Tu es vraiment pressé de découvrir la prochaine façon de foutre le bordel ?"

    elen inquiet "Ça peut être une bonne proposition aussi ! On a réussi une fois, alors peut-être que la suivante sera encore mieux."

    mara agace "Regarde les écrans de Limen et répète-moi qu'on a réussi. J'ai besoin de rire."

    tomas hesitation "On ne sait même pas ce qu'elle va annoncer. On devrait peut-être attendre avant de recommencer à se disputer."

    iris desaccord "Pour une fois, je suis d'accord avec Tomas. Vous pourrez vous étrangler après avoir lu le sujet."

    kael reflechit "Les conséquences du dernier vote ne sont même pas encore stabilisées. C'est beaucoup trop tôt pour décider autre chose."

    nyra raison "Nous aurons trois jours pour le faire. Pour le moment, il faut seulement écouter."

    noam neutre "Enfin une proposition raisonnable. Attendons au moins que Kami nous donne une raison de paniquer."

    lysa blase "Elle ne devrait plus tarder. Elle aime beaucoup trop les entrées dramatiques pour nous laisser commencer sans elle."

    sael mefiant "Elle est déjà là."

    think "Sael fixe l'écran central. Une seconde plus tard, il s'allume."

    play sound sfx_announce

    $ hideGroup()
    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Maintenant que tout le monde est enfin installé, nous pouvons annoncer le prochain vote !"
    kami "Et cette fois, j'ai choisi quelque chose de parfaitement simple. Roulement de tambour !"

    play sound sfx_tambour
    pause 1.5

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser les déplacements de personnes entre les districts ?"
    kami "Un vote pour permettra à chacun de franchir librement les frontières. Un vote contre conservera les restrictions actuelles."
    $ unlock_codex_page("frontieres_interdistricts", with_notification=False)

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et promis, aucune petite réécriture surprise cette fois-ci ! L'énoncé est exactement celui que vous venez de lire."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_213
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    $ showGroup([
        ("ryn", "colere"),
        ("kael", "triste"),
        ("sael", "mefiant"),
        ("lysa", "blase"),
        ("noam", "determine"),
        ("julian", "determine"),
        ("elias", "determine"),
        ("iris", "desaccord"),
        ("mara", "agace"),
        ("nyra", "raison"),
        ("tomas", "hesitation"),
    ])

    think "Le mot « frontières » suffit à changer l'attitude de Ryn. Il se penche immédiatement vers son micro."

    ryn colere "Il faut voter pour. Je veux même pas entendre qu'on pourrait encore garder ces foutues frontières fermées."
    ryn triste "J'ai passé des années à empêcher des gens de les atteindre. J'en ai vu creuser des tranchées sans savoir exactement où le rayon allait tomber."

    kael surpris "Tu étais un Gardien ?"

    ryn fatigue "Ouais. On devait arrêter les gens plusieurs mètres avant la frontière pour éviter qu'ils se fassent exécuter."
    ryn triste "Au début, personne ne connaissait son tracé exact. Beaucoup de Gardiens sont morts en essayant de le trouver."

    sael triste "Leurs tranchées ont fini par dessiner une limite visible. Sans eux, il y aurait eu beaucoup plus de morts."
    $ unlock_codex_page("frontieres_limen", with_notification=False)

    ryn colere "Et maintenant on devrait continuer à garder cette limite pour toujours ? Non. Je veux que ça s'arrête."

    lysa reflechit "Tu as passé des années à empêcher les gens de traverser. Et maintenant tu veux leur ouvrir la route."

    ryn triste "Parce que je sais exactement ce que la fermeture leur coûte."

    noam raison "Ryn ne veut pas seulement supprimer une frontière. Il veut surtout que personne ne meure encore en essayant de la franchir."

    julian determine "Et il a raison. Les districts ont besoin de pouvoir se rejoindre, travailler ensemble et partager leurs ressources."

    lysa blase "Tout ça serait merveilleux si les districts avaient oublié en un an les guerres qu'ils menaient depuis des générations."
    lysa reflechit "Ouvrir une frontière ne fait pas disparaître ceux qui attendent de l'autre côté pour reprendre un conflit."

    elias reflechit "Elle a pas tort. Kami a arrêté les combats, mais elle a pas effacé la colère des gens."

    iris desaccord "Donc quoi ? On garde tout le monde enfermé parce qu'une partie pourrait devenir violente ?"

    sael mefiant "Je voterai contre."

    ryn surpris "Quoi ? Après tout ce que je viens de dire ?"

    sael determine "Mon peuple vit près du Mont Kensen. Avant Kami, les groupes armés de Limen traversaient régulièrement nos terres."
    sael triste "J'ai vu ce que ces déplacements transportaient avec eux. Des armes, de la colère et des morts."
    sael mefiant "Pour vous, cette proposition ouvre des routes. Pour moi, elle rouvre celles que la guerre empruntait."

    think "Sael croise les bras. Elle ne regarde déjà plus Ryn."

    elias colere "Mais tu peux pas décider pour tout le monde uniquement à cause de ce qui s'est passé avant !"
    elias inquiet "Si les gens peuvent bouger, les médecins et les ressources pourront bouger aussi. Ça sauvera des vies."

    sael colere "Tu crois que je n'y ai pas réfléchi ?"
    sael determine "Ma réponse est non. Je ne vais pas risquer la vie des miens pour réparer la frontière de Limen."

    elias colere "C'est pas seulement la frontière de Limen !"

    sael triste "Tu ne sais rien de ce que cette route a déjà coûté aux miens."

    hide sael
    with moveoutright

    play sound sfx_door volume 8.0
    "Sael se lève d’un coup. Elle tourne les talons et quitte la salle en claquant la porte."
    with hpunch

    mara surpris "Sael, attends !"
    mara colere "Putain, vous pouviez pas discuter deux minutes sans lui sauter à la gorge ?"

    hide mara
    with moveoutright

    play sound sfx_door volume 8.0
    "Mara se lève et la suit en courant hors de la pièce."
    with hpunch

    julian determine "Laissez-la partir. Elle ne changera pas d'avis dans cet état."
    julian inquiet "Mais on ne peut pas non plus laisser sa peur condamner le texte avant même le débat."

    noam reflexion "Je ne crois pas que ce soit seulement de la peur. Elle pense réellement protéger son peuple."

    ryn colere "On ne peut pas laisser ça comme ça."
    ryn colere "Sael est trop bornée. Elle va tout faire foirer !"

    kael inquiet "Elle a ses raisons. Les ignorer ne la fera pas revenir."

    nyra raison "On connaît maintenant le principal point de blocage. Il faudra trouver une réponse concrète avant le vote."

    tomas hesitation "On pourrait peut-être parler de contrôles aux frontières, ou d'une ouverture progressive... Enfin, si le texte nous le permet."

    iris desaccord "Bravo. Vous avez transformé un débat politique en concours pour savoir qui blesserait Sael le plus vite. Très efficace."

    "Iris se lève à son tour et quitte la pièce."

    hide iris
    with moveoutleft

    think "Le débat vient à peine de commencer et Sael a déjà annoncé son vote contre. Une seule voix suffira à rejeter le texte."

    jump _4_1_APRES_CLASH_PRE_FETE

# Durée : 3m05
# Total : 2h 01m 05s

label _4_1_APRES_CLASH_PRE_FETE:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_214
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    $ showGroup([
        ("julian", "decu"),
        ("elen", "joie"),
        ("noam", "raison"),
        ("nyra", "surpris"),
    ])

    think "Après le départ d'Iris, personne ne semble savoir si la réunion est réellement terminée. Elen finit par se lever."

    elen joie "Bon ! On ne va pas rester là à se regarder comme si quelqu'un venait de mourir."
    elen content "On a adopté notre premier amendement hier. Je propose qu'on fête ça ce soir !"

    noam surpris "Une fête ? Maintenant ?"

    elen inquiet "Justement maintenant. Si on retourne tous dans nos chambres après ça, demain personne ne voudra encore se parler."
    elen joie "Je m'occupe de la nourriture, des boissons et de la musique. On se retrouve dans la salle de repos !"

    julian sourire "Pour une fois, je soutiens pleinement cette initiative. Une victoire mérite au moins un verre."

    noam reflexion "Je ne sais pas si on peut encore appeler ça une victoire après ce qu'on a vu ce matin."

    elen desaccord "On peut être inquiets et quand même souffler un peu. Les deux sont possibles !"
    elen reflexion "Nyra, tu peux aller chercher Mara et Sael ? Je pense qu'elles t'écouteront plus facilement."

    nyra surpris "Moi ? Pourquoi est-ce que ce serait plus facile avec moi ?"

    elen taquin "Parce que tu sais parler aux gens sans les énerver en moins de dix secondes. C'est un talent rare ici."

    nyra reflexion "Je vais essayer. Mais je ne te garantis pas qu'elles accepteront."

    hide nyra
    with moveoutright

    think "Nyra quitte la salle à la suite de Mara et Sael."

    elen inquiet "Et toi, Noam, tu peux aller chercher Iris ? Elle est sûrement retournée dans sa chambre."

    noam hesitation "Pourquoi moi ?"

    elen taquin "Parce que toi aussi, tu dépasses rarement les dix secondes. Puis elle t'aime bien. Enfin, je crois."

    noam surpris "Quoi ? Mais..."

    elen joie "Merci Noam ! Moi, je vais tout préparer !"

    think "Elle s'éloigne avant que je puisse refuser."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_215
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([("noam", "hesitation", 0.50)])

    think "Je prends la direction de la chambre d'Iris en essayant de trouver une manière normale de lui proposer une fête après notre dispute."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_216
    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([("noam", "hesitation", 0.50)])

    "La porte est entrouverte. Je frappe doucement."

    iris fatigue "C'est qui ?"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_iris") from _call_MAYBE_PLAY_SCRIPTED_DOOR_217
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "triste", 0.70),
        ("noam", "hesitation", 0.30),
    ])

    think "Iris est assise sur son lit, les bras autour des genoux. Elle se redresse légèrement en me voyant."

    iris fatigue "Ah... C'est toi."
    iris desaccord "Tu es venu me dire que j'ai encore abandonné une discussion trop tôt ?"

    noam neutre "Non. Pour être honnête, je crois que tout le monde avait besoin que cette discussion s'arrête."

    think "Je m'assieds à l'autre bout du lit en laissant suffisamment d'espace entre nous."

    $ hideGroup()
    scene bg_cg018 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg018")

    noam hesitation "Elen organise une petite fête dans la salle de repos. Elle pense que ça nous évitera de finir la journée en nous détestant tous."

    iris desaccord "Sael claque une porte, Mara lui court après et notre réponse stratégique, c'est de sortir l'alcool ? Brillant."

    noam taquin "Présenté comme ça, le plan a effectivement quelques défauts."
    noam raison "Mais rester seule à repenser à la scène ne changera rien non plus. Ça pourrait nous faire du bien de souffler un peu."

    iris reflexion "Tu marques un point. Et ça m'agace beaucoup."
    iris fatigue "D'accord, je viens. Mais si Julian fait un discours de plus de quinze secondes, je lui fais avaler son verre."

    noam taquin "Je l'arrêterai. Enfin... juste après les quinze secondes."
    
    "Iris retient un sourire et se lève."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_iris") from _call_MAYBE_PLAY_SCRIPTED_DOOR_218
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "taquin", 0.70),
        ("noam", "sourire", 0.30),
    ])

    iris taquin "Ne prends pas cet air satisfait."
    noam sourire "Je n'ai pas d'air satisfait."
    iris taquin "C'est pire. Tu as ton air innocent."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_219
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "neutre", 0.70),
        ("noam", "sourire", 0.30),
    ])

    think "La musique nous rejoint avant la salle. Au moins, Elen n'a pas perdu de temps."

    $ repos_party_active = True
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_220
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    $ showGroup([
        ("elen", "content"),
        ("julian", "sourire"),
        ("ryn", "fatigue"),
        ("nyra", "neutre"),
        ("mara", "neutre"),
        ("sael", "mefiant"),
        ("iris", "neutre"),
        ("noam", "neutre"),
    ])

    think "Elen a déjà sorti les rations alcoolisées. Julian sert les verres pendant que Nyra arrive avec Mara et Sael."

    elen content "Ah ! Vous êtes là ! Prenez un verre avant que Julian transforme le service en cérémonie officielle !"
    elen joie "On a gagné hier. Enfin, aujourd'hui c'est compliqué, mais hier on a gagné, donc ça compte encore un peu !"

    think "Personne ne paraît réellement d'humeur à faire la fête. Pourtant, presque tout le monde accepte un verre."

    jump _4_1_FETE_IMPROVISEE

# Durée : 1m25
# Total : 2h 02m 30s

label _4_1_FETE_IMPROVISEE:
    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_221
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    $ showGroup([
        ("elen", "content"),
        ("iris", "fatigue"),
        ("julian", "sourire"),
        ("elias", "reflechit"),
        ("lysa", "blase"),
        ("mara", "neutre"),
        ("noam", "neutre"),
    ])

    "Elen a suspendu quelques tissus devant les veilleuses et installé une enceinte au milieu de la salle."

    elen content "J'ai compté les verres trois fois et les rations deux fois ! Après, j'ai commencé à goûter, donc les chiffres sont peut-être moins fiables."

    iris taquin "Une organisation irréprochable. Kami peut préparer sa démission."

    elen joie "Tu vois ! Je savais que tu finirais par aimer l'idée !"

    iris blase "Ce n'était pas un compliment... Laisse tomber."

    julian sourire "Puisque tout le monde est servi, je propose de boire à notre premier amendement adopté."
    julian determine "Nous avons osé changer les choses. Nous devons maintenant avoir le courage d'en assumer les conséquences."

    elias reflechit "On peut boire à l'espoir, ouais. Mais avec ce qu'on a vu ce matin, j'ai du mal à appeler ça une victoire."

    lysa blase "Dans ce cas, buvons au fait d'avoir survécu à notre première décision. C'est moins ambitieux."

    mara taquin "Déprimant, prudent et alcoolisé. Ça me convient parfaitement."

    think "Les verres commencent à se lever lorsque l'écran s'allume. Kami refuse évidemment de rater le toast."

    play sound sfx_announce
    $ hideGroup()
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous n'alliez quand même pas organiser une fête sans m'inviter ? Moi qui fournis l'alcool, la salle et même la surveillance !"
    kami "Trinquons donc à votre courage. Ou à votre inconscience, je n'ai pas encore terminé l'analyse."
    kami "Amusez-vous bien, mes petits représentants. Je regarderai tout !"

    hide screen kami_broadcast_ui
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_222
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    $ showGroup([
        ("mara", "ivre"),
        ("tomas", "hesitation"),
        ("iris", "desaccord"),
        ("lysa", "blase"),
        ("elen", "joie"),
        ("ryn", "fatigue"),
        ("noam", "neutre"),
    ])

    elen joie "Bon ! Si même notre geôlière trinque avec nous, on a officiellement le droit de monter le son !"

    ryn fatigue "C'est probablement la règle la plus sensée de la journée."

    think "Les verres se remplissent une nouvelle fois. Au bout de quelques minutes, Ryn accepte même de danser avec Elen."

    mara ivre "Bon, ça suffit les mines d'enterrement. J'ai une bouteille vide et une idée particulièrement mauvaise. Qui joue ?"

    "La bouteille tourne sur la table basse."

    tomas hesitation "Euh... C'est quoi exactement, le jeu de la bouteille ? Je n'ai jamais joué."

    mara taquin "Oh, Tomas… Cette innocence va me tuer."
    mara taquin "On la fait tourner. Elle désigne deux personnes et elles s'embrassent si elles en ont envie."
    mara neutre "Et si quelqu'un refuse, on passe au tour suivant. Je suis joueuse, pas gardienne de prison."

    iris desaccord "C'est ridicule et probablement conçu pour créer des problèmes. Je vais me coucher."

    "Mara lui barre le passage d'un pas, sans la toucher."

    mara taquin "Attends, Iris. Tu peux rester sans participer. Mais priver cette soirée de ton regard assassin, ça devient personnel."

    iris fatigue "Tu es épuisante."
    iris gene "Bon. Je reste. Et je joue… seulement si Noam joue aussi."

    lysa reflechit "Pourquoi Noam ?"

    iris gene "Pour rien ! Enfin— parce que c'est moins stupide si tout le monde participe. C'est tout."
    
    mara taquin "Bien sûr. Une décision purement scientifique."

    iris colere "Un mot de plus et je révise mon oui."

    menu:
        "Accepter de jouer":
            $ jeu_bouteille_accepte = True
            noam taquin "D'accord. Puisque mon sacrifice permet de faire avancer la science..."
            jump _4_1_JEU_BOUTEILLE

        "Refuser poliment":
            $ jeu_bouteille_accepte = False
            noam neutre "Pas ce soir. Je vais vous laisser mener l'expérience sans moi."
            mara taquin "Refus accepté. Mais tu restes quand même témoin des dégâts."
            jump _4_1_FIN_SOIREE

# Durée : 1m30
# Total : 2h 04m 00s

label _4_1_JEU_BOUTEILLE:

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_223
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_romantic_atmosphere.mp3" fadein 1.5

    $ showGroup([("mara", "ivre", 0.50), ("noam", "surpris", 0.88), ("lysa", "blase", 0.12)])
    mara ivre "Premier tour ! Choisis bien, petite bouteille, j'ai une réputation à tenir."

    "La bouteille tourne au milieu de la table, ralentit, puis s'arrête devant moi."

    noam surpris "Moi ? Évidemment..."

    "Mara la relance. Cette fois, le goulot désigne Lysa."

    lysa blase "Évidemment. Le hasard a un sens de l'humour particulièrement médiocre."
    lysa reflechit "Tu es d'accord, Noam ?"

    noam hesitation "Oui. Enfin... oui, je suis d'accord."

    mara taquin "Parfait ! Et pas de négociation diplomatique pendant le baiser."

    $ hideGroup()
    scene bg_cg019 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg019")

    "Lysa hausse légèrement un sourcil avant de se rapprocher."
    think "Je n'ai même pas le temps de trouver quelque chose à dire."
    "Ses lèvres rencontrent les miennes. Le baiser est bref, mais elle reste près de moi une seconde avant de reculer."

    elen joie "Ooooooh !"

    iris blase "Respire, Elen."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_224
    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showGroup([
        ("julian", "joie"),
        ("elen", "joie"),
        ("lysa", "gene"),
        ("mara", "ivre"),
        ("tomas", "gene"),
        ("sael", "mefiant"),
    ])
    julian joie "Un premier tour particulièrement convaincant. Je valide totalement le concept."

    elen joie "Lysa ! Tu as rougi ! C'était beaucoup trop mignon !"

    lysa gene "C'est l'alcool. Pas lui."
    lysa taquin "Cela dit, il embrasse mieux qu'il ne termine ses phrases. La barre était assez basse."

    noam taquin "Je vais choisir de prendre ça pour un compliment."

    mara ivre "Deuxième tour ! La bouteille exige visiblement davantage de chaos."

    "La bouteille tourne… s’arrête sur Tomas."

    tomas surpris "Oh non... Pourquoi moi ?"

    "La bouteille pointe Sael."

    sael surpris "..."

    mara taquin "Sael et Tomas. Même moi, je n'aurais pas osé prévoir ça."

    sael neutre "Tomas ?"

    tomas gene "Je... Oui. Enfin, seulement si toi aussi."

    sael sourire "Alors approche. Il n'y a rien à craindre."

    $ hideGroup()
    scene bg_cg020 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg020")

    "Sael pose une main sur la nuque de Tomas et l'embrasse doucement. Quand elle recule, il est écarlate."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_225
    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showGroup([
        ("elen", "joie"),
        ("julian", "taquin"),
        ("tomas", "gene"),
        ("mara", "ivre"),
        ("kael", "surpris"),
        ("elias", "jaloux"),
    ])
    elen joie "Sael ! C'était tellement doux ! Tomas, tu respires encore ?"

    julian taquin "La question mérite effectivement une réponse officielle. Tomas ?"

    tomas gene "Je... je crois."

    mara ivre "Il vit ! On peut donc passer au dernier tour. Cette fois, on termine en beauté."

    "La bouteille tourne… s’arrête sur Kael."

    kael surpris "Moi ?"

    "La bouteille repart et pointe Elias."

    elias surpris "Euh... Moi ?"

    mara taquin "Kael et Elias. Cette bouteille a décidément beaucoup de goût."

    kael gene "Je..."
    kael gene "Je ne sais pas."

    elias inquiet "Tu n'es pas obligé, Kael. Vraiment."
    elias neutre "Moi, ça me va. Mais si tu n'en as pas envie, on passe au tour suivant."

    kael gene "... D'accord."

    elias inquiet "Tu es sûr ?"

    kael gene "Oui. Avant que je change d'avis."

    $ hideGroup()
    scene bg_cg021 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg021")

    "Ils se rapprochent lentement. Elias pose une main sur la nuque de Kael et aucun des deux ne recule immédiatement après le baiser."

    elias fatigue "C'était seulement pour le jeu..."

    kael gene "Oui. Seulement le jeu."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos_fete") from _call_MAYBE_PLAY_SCRIPTED_DOOR_226
    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showGroup([("mara", "ivre", 0.12), ("kael", "gene", 0.50)])

    mara ivre "Je retire tout ce que j'ai dit : cette bouteille est une artiste. On remet ça demain ?"

    kael gene "Non. Définitivement non."

    jump _4_1_FIN_SOIREE

# Durée : 1m40
# Total : 2h 05m 40s

label _4_1_FIN_SOIREE:

    $ repos_party_active = False
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_227
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    $ showGroup([("noam", "fatigue", 0.50)])

    think "La fête se termine bien plus tard que prévu. Je quitte les autres et regagne lentement ma chambre."
    think "J'ai suffisamment bu pour que le couloir semble bouger légèrement sous mes pieds."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_228
    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([("noam", "fatigue", 0.50)])

    think "Je retire ma veste puis m'assieds sur le lit. Mes chaussures me demandent déjà plus d'efforts que je ne peux leur en donner."

    $ blink()
    think "Je repense au débat, au départ de Sael, puis à son retour dans la salle de repos, alors que rien n'est vraiment réglé."

    $ blink()
    think "Pendant quelques heures, nous avons réussi à rire ensemble. Demain, il faudra pourtant recommencer à parler du vote."

    think "Je parviens finalement à retirer mes chaussures et m'allonge sans prendre le temps de me changer."
    $ blink()

    $ hideGroup()
    scene bg_cg012 at adaptive_fullscreen with dissolve
    think "Sael a déjà annoncé qu'elle votera contre. Si elle ne change pas d'avis, la libre circulation n'a aucune chance d'être adoptée."
    think "J'essaierai de lui parler demain. Pour le moment, je n'arrive même plus à garder les yeux ouverts."

    $ current_day = 5
    pause 1.5

    call end_day("5") from _call_end_day_5_1
    jump _5_1_REVEIL_CHAMBRE

# Durée : 0m35
# Total : 2h 06m 15s
