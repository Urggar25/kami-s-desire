# --------------------------------------------------------------------------------------------
# JOUR 9 — Réveil chambre
# Kami revient après deux jours de silence.
# Elle réveille directement Noam par annonce matinale.
# Convocation immédiate dans la salle du Conclave pour annoncer le prochain vote.
# --------------------------------------------------------------------------------------------

label _9_0_1_REVEIL_CHAMBRE:
    scene black
    $ current_day = 9
    $ cafeteria_food_level = "medium"
    $ current_period = "Matin"
    $ noam_has_juliette_drawing = False
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5
    $ blink()
    "Quelque chose me cogne le genou."
    "J'ouvre un œil. C'est la chaise que j'ai bloquée sous la poignée hier soir."
    think "Parfait. Première victime de notre grand complot nocturne : moi."
    "Je la repousse du pied, puis regarde le bureau. La place du dessin de Juliette est toujours vide."
    think "Je recommence à calculer combien de personnes ont pu entrer dans ma chambre, et combien de fois je me suis déjà posé cette question."
    "Une seconde, je crois entendre du bruit dans le couloir."
    noam inquiet "Qui est là... ?"
    "Aucune réponse."
    think "Je deviens ridicule. Je n'ai qu'à attendre que quelqu'un vienne me demander si je peux prêter mon tiroir pour bloquer une autre porte."
    "Je remets la tête contre l'oreiller."
    stop music fadeout 0.5
    play sound sfx_announce
    pause 0.6
    think "..."
    think "Non."
    $ hideGroup()
    play music "music/bgm_system_override.mp3" fadein 0.7
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "BONJOUUUUR, mes adorables petits rescapés !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Alors ? Qui a bien dormi ? Qui a pleuré ? Qui a profité de mes deux jours de congé pour devenir une personne intéressante ?"
    noam fatigue "Toi, en tout cas, tu n'as pas changé."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh, Noam ! Déjà debout ? Tu me déçois, j'avais misé sur une troisième grasse matinée."
    noam colere "Qu'est-ce qui t'est arrivé ?!"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bonjour à toi aussi. Dans la civilisation, on répond au salut avant l'interrogatoire."
    noam inquiet "Tu as cessé de répondre pendant deux jours. Après les pannes du vote, on a cru que..."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Que j'étais MORTE ?!"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "C'est touchant. Et très vexant. Une petite maintenance, mes chéris ! Rien qu'une maintenance."
    noam reflechit "Et les exécutions ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Quoi, les exécutions ?"
    noam colere "Le compteur est resté à zéro !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Ah ! Les chiffres. Vous avez donc appris à lire autre chose que vos menus de cafétéria. J'en suis émue."
    noam inquiet "Tu n'as pas répondu."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je ne suis pas tenue de fournir un compte rendu détaillé de mes opérations internes à chaque enfant qui s'inquiète parce qu'on l'a laissé sans surveillance !"
    pause 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "En parlant de surveillance... certains ont transformé leurs chambres en forteresses. Une chaise contre une porte ? Sérieusement ?"
    think "Mon regard descend vers la chaise, encore couchée près du lit."
    kami "J'espère au moins que la révolution du mobilier vous a apporté le sommeil."
    noam reflechit "Tu as vu ce qu'il s'est passé dans nos chambres ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Tu parles de la poussière ? Du désordre ? De ton goût très discutable pour les vêtements froissés ?"
    noam inquiet "Je parle des affaires qui ont disparu."
    pause 0.7
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je parle, moi, du troisième vote."
    think "Elle a entendu. Elle a choisi de ne pas répondre."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Vous êtes TOUS convoqués dans la salle du Conclave ! Immédiatement ! Et essayez de ne pas traîner. Nous avons un programme chargé."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ah, et remettez les meubles à leur place. Je refuse de présider un parlement qui a peur des chaises."
    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])
    "L'écran s'éteint. Je reste un instant sans bouger, la manche de ma veste dans la main."
    think "Elle me nargue pour une chaise, mais ne dit rien d'une photo et d'un dessin volés."
    noam reflechit "Maintenance, hein..."
    "Je soulève la chaise pour dégager la porte. Elle a laissé une marque au sol."
    think "Voilà. Si quelqu'un entre encore ce soir, au moins le plancher pourra témoigner."
    $ hideGroup()
    stop music fadeout 1.5
    scene black with fade
    call KD_ROUTE_J9_ELEN from _call_optional_kd_route_j9_elen
    call OFFER_DAILY_EXPLORATION(
        "_9_0_1_CONCLAVE_ANNONCE", 1,
        ["conclave", "cafeteria", "archive"],
        "Sur le chemin du Conclave", "conclave"
    ) from _call_offer_exploration_j9_main

label _9_0_1_CONCLAVE_ANNONCE:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_303
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    $ showGroup([
        ("lysa", "blase", 0.08), ("ryn", "fatigue", 0.25),
        ("noam", "inquiet", 0.42), ("iris", "fatigue", 0.58),
        ("mara", "stress", 0.75), ("elen", "peur", 0.92),
    ])
    iris colere "JE REFUSE !"
    mara taquin "Ah. Voilà une excellente manière de commencer le vote."
    iris colere "Je refuse qu'elle appelle ça une maintenance ! Une maintenance, ça se planifie ! Ça se documente !"
    lysa blase "Tu veux qu'elle t'envoie son agenda ?"
    iris inquiet "Je veux juste savoir comment une IA qui contrôle la planète peut s'arrêter deux jours sans laisser de trace !"
    ryn fatigue "Moi, je veux juste qu'on arrive à cette foutue salle."
    elen sourire "Au moins, elle a l'air d'aller mieux !"
    mara stress "Elle allait mieux aussi quand elle nous a fait voter pour des gens qui allaient mourir."
    elen peur "Je sais. Je voulais seulement..."
    lysa neutre "Tu voulais qu'on ait une bonne nouvelle. Je sais."
    "Elen se tait. Iris regarde un écran mural, comme si elle espérait y voir apparaître une explication."
    julian "Mes chers collègues !"
    "Julian nous rejoint, les cheveux encore ébouriffés, les bras ouverts comme s'il venait inaugurer une statue."
    mara taquin "Tu as oublié ton peigne ou tu t'es coiffé avec une brosse à chaussures ?"
    julian "J'ai privilégié la ponctualité sur l'esthétique."
    lysa blase "Une première historique."
    julian "J'apprécierais que cette date soit enregistrée."
    ryn colere "ON PEUT AVANCER ?!"
    "Il part devant nous. Personne ne se moque de lui."
    noam reflechit "Ryn..."
    ryn fatigue "Quoi ?"
    noam inquiet "Tu as pensé aux gens des frontières ?"
    "Il s'arrête si brutalement que Julian manque de le heurter."
    ryn colere "Depuis le vote ? Pas une minute sans y penser."
    sael "Alors regarde où tu marches."
    "Sael arrive par l'autre bout du couloir. Elle dépasse Ryn sans ralentir."
    ryn colere "Tu as quelque chose à dire ?"
    sael "Oui. Nous sommes en retard."
    lysa blase "Une réponse parfaite. Personne ne devrait pouvoir se disputer avec ça."
    "Ryn lui emboîte le pas en serrant les dents."
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_304
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "blase", 0.10), ("ryn", "fatigue", 0.27),
        ("sael", "inquiet", 0.43), ("kael", "fatigue", 0.57),
        ("tomas", "inquiet", 0.73), ("iris", "fatigue", 0.90),
    ])
    "Kael est déjà assis. Il fixe la table sans toucher à sa tablette."
    iris reflechit "Kael ?"
    kael fatigue "Elle était sous mon oreiller."
    iris hesitation "Quoi ?"
    kael fatigue "La photo. Elle était sous mon oreiller. Je l'ai vérifié encore ce matin."
    "Iris ouvre la bouche, puis s'installe en silence."
    tomas inquiet "J'ai trouvé un élément dans les données de Limen. Enfin... j'espère qu'il ne s'agit pas de..."
    ryn fatigue "Tomas, si tu as quelque chose à dire, dis-le."
    tomas reflechit "Des mouvements de population. À proximité des frontières."
    sael inquiet "Combien ?"
    tomas inquiet "Les chiffres sont incomplets. Je vérifie."
    play sound sfx_announce
    stop music fadeout 0.8
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Oh, quel comité d'accueil ! Vous êtes presque tous là. Ça me change de ces deux journées où vous avez fait semblant de savoir vous gouverner."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Aujourd'hui : troisième vote ! Et je vous ai choisi une question qui devrait vous passionner."
    play sound sfx_tambour
    pause 0.5
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser les regroupements de plus de vingt personnes, idéalement avec déclaration préalable."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je vous rappelle le Commandement IV : les rassemblements non déclarés de plus de vingt individus sont interdits."
    kami "Si vous adoptez l'amendement à l'unanimité, la nouvelle règle s'appliquera immédiatement. Sinon, rien ne change."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Concerts, réunions de famille, manifestations... Je vous imagine déjà en train de réserver des places pour un festival de mauvaises décisions."
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("tomas", "inquiet", 0.10), ("lysa", "blase", 0.27),
        ("ryn", "fatigue", 0.43), ("sael", "inquiet", 0.57),
        ("noam", "inquiet", 0.73), ("kael", "fatigue", 0.90),
    ])
    julian "Enfin ! Une proposition qui permettrait aux gens de se réunir sans avoir à compter jusqu'à dix-neuf !"
    lysa blase "Tu comptes vraiment jusqu'à dix-neuf, toi ?"
    julian "Non, j'ai du personnel pour ça."
    mara "Quel personnel ? Tu ne sais même pas ranger ton plateau."
    "Tomas n'a pas levé les yeux."
    tomas inquiet "Ce n'est pas un hasard."
    noam reflechit "Tu parlais de mouvements de population..."
    tomas reflechit "Oui. Depuis hier soir, plusieurs groupes remontent de Limen vers les points de passage. Ils ont installé des campements."
    ryn colere "Des gens qui cherchent à sortir de là. Enfin."
    sael mefiant "Des gens qui s'approchent des frontières malgré notre refus."
    ryn colere "Tu vas leur demander de faire demi-tour ?!"
    sael determine "Je n'ai rien dit de tel."
    tomas inquiet "Attendez. Les campements rassemblent peut-être des milliers de personnes."
    kael reflechit "Sans déclaration préalable ?"
    tomas neutre "Il n'y a aucune déclaration enregistrée."
    "Le silence tombe plus vite que je ne l'aurais cru."
    noam inquiet "Le Commandement IV..."
    iris inquiet "Kami n'a pas appliqué les sanctions pendant deux jours."
    tomas inquiet "C'est probablement pour ça qu'ils ont osé se regrouper. Mais si elle vient de reprendre..."
    ryn colere "Non. NON !"
    sael peur "Ils sont au même endroit. En nombre."
    lysa reflechit "Et notre sujet du jour tombe exactement là-dessus."
    noam inquiet "Kami, tu savais pour ces campements ?"
    $ hideGroup()
    play sound sfx_announce
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Oh, vous avez trouvé ! Je commençais à croire que vous aviez perdu la capacité de relier deux informations."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Plusieurs campements limenois dépassent largement le seuil autorisé. Aucun n'a été déclaré."
    kami "J'ai suspendu temporairement l'application du Commandement à leur égard. Je voulais vous laisser la possibilité de trancher."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'aurais pu régler le problème sans vous consulter. Mais ce n'aurait pas été très amusant, vous ne trouvez pas ?"
    ryn "Tu te fous de nous ?!"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh, Ryn. Du calme. J'ai été d'une patience exemplaire."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote aura lieu aujourd'hui. Ensuite, le Commandement IV sera appliqué dans sa version alors en vigueur."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Vous avez donc toutes les cartes en main. Essayez de ne pas les manger."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere"), ("sael", "peur"), ("tomas", "inquiet"),
        ("lysa", "triste"), ("noam", "inquiet"), ("nyra", "fatigue"),
        ("mara", "stress"), ("iris", "inquiet"), ("elen", "peur"),
        ("elias", "fatigue"), ("julian", "inquietude"), ("kael", "fatigue"),
    ])
    ryn colere "ELLE LES A LAISSÉS SE RASSEMBLER ! POUR NOUS REGARDER LES CONDAMNER !"
    sael determine "Alors il faut voter pour."
    ryn colere "Tu viens de dire quoi ?"
    sael determine "Pour. Tu m'as bien entendue."
    ryn surpris "..."
    sael mefiant "Ne me remercie pas. Je refuse encore l'ouverture des frontières. Je refuse aussi qu'on tue des familles pour s'être arrêtées au même endroit."
    mara neutre "Il y a une différence entre ouvrir les passages et laisser les gens s'asseoir ensemble."
    elen inquiet "Ils ne se sont pas assis pour s'amuser ! Ils attendent qu'on les laisse partir !"
    mara agace "Je sais, Elen ! Je n'ai pas dit le contraire !"
    elias reflechit "Et si le vote passe, les camps sont sauvés ?"
    tomas hesitation "Pas forcément."
    ryn colere "QUOI, ENCORE ?!"
    tomas inquiet "Le mot « idéalement » me gêne. Et rien ne garantit que les campements déjà formés seront régularisés."
    iris colere "Elle peut donc nous faire voter pour un truc et punir les gens quand même ?!"
    nyra raison "Il faut envisager cette possibilité."
    julian "C'est une escroquerie !"
    lysa blase "Un contrat dont elle écrit seule les petites lignes."
    kael reflechit "Si nous devons agir, il nous faut des images des campements et un moyen de diffuser des instructions."
    noam reflechit "La séance est retransmise sur Terre..."
    sael determine "Alors utilisons-la."
    ryn colere "On leur dit de se disperser. Tout de suite."
    tomas reflechit "Par groupes de moins de vingt, hors des points de passage et sans traverser les frontières. Ce n'est pas une garantie, mais..."
    elen peur "Et ceux qui ne peuvent pas marcher ?"
    "Personne ne répond immédiatement."
    noam inquiet "Il faut au moins leur faire parvenir l'alerte. Même si ça ne suffit pas."
    $ unlock_dossier_arg("p3_campements")
    call play_stat_dialogue("d9") from _call_stat_dialogue_d9
    tomas inquiet "J'ai les données de la salle du Canon. Il faut les relier aux tablettes."
    kael neutre "Passe-moi la tienne."
    tomas gene "Tu peux juste..."
    kael reflechit "Pas le temps de faire un cours. On verra les détails après."
    "Tomas lui donne sa tablette. C'est sans doute la première fois qu'il interrompt volontairement une explication."
    $ hideGroup()
    call j901_play_hack from _call_j901_play_hack_day9
    $ j901_hack_success = bool(_return)
    $ showGroup([("kael", "inquiet", 0.32), ("noam", "inquiet", 0.68)])
    if j901_hack_success:
        kael sourire "On a un retour vidéo. Pas de toutes les zones, mais assez pour lancer une alerte."
    else:
        kael inquiet "La connexion tient à peine. J'ai quelques images et un flux instable."
    noam determine "Alors on n'attend pas. Même si ça coupe, il faut essayer."
    kael neutre "Je lance."
    $ hideGroup()
    stop music fadeout 1.5
    scene black with fade
    jump _9_0_1_CONCLAVE_DEBAT

label _9_0_1_CONCLAVE_DEBAT:
    $ current_period = "Après-midi"
    call j901_play_signal_vivant from _call_j901_play_signal_vivant
    $ j901_signal_result_tier = _return
    jump _9_0_1_CONCLAVE_DEBAT_PARTIE_2

label _9_0_1_CONCLAVE_DEBAT_PARTIE_2:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("ryn",   "colere",      0.10),
        ("sael",  "determine",   0.27),
        ("tomas", "culpabilite", 0.43),
        ("noam",  "inquiet",     0.57),
        ("nyra",  "stress",      0.73),
        ("kael",  "inquiet",     0.90),
    ])

    "Le signal disparaît peu à peu, comme si quelqu'un interagissait avec le signal. La tablette de Kael montre des silhouettes qui commencent à courir avant de s'éteindre à son tour."

    think "Certains ont entendu. Je ne sais pas combien, ni s'ils auront le temps de prévenir les autres."

    $ hideGroup()
    play sound sfx_gresillement
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Voilà donc votre grande tentative : détourner mon signal pour transformer le Conclave en alerte d'évacuation."
    kami "C'était presque intelligent, nous verrons ce que les gens feront de vos doux conseils."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Quelques humains qui crient très fort parce qu'ils viennent enfin de comprendre qu'ils sont en retard. C'était presque émouvant."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    if j901_signal_result_tier == "excellent":
        kami "Je reconnais une véritable efficacité technique. La majorité des campements a reçu votre avertissement. Ce serait presque respectable, si votre impertinence ne gâchait pas tout."
    elif j901_signal_result_tier == "bon":
        kami "Vous avez atteint une partie importante des campements. Pas tous, mais suffisamment pour vous donner l'impression d'avoir repris la main."
        kami "Seulement, ce n'est qu'une vague impression."
    elif j901_signal_result_tier == "moyen":
        kami "J'ai bien cru que vous arriveriez à un résultat probant. Agir et donner l'impression d'agir restent deux choses différentes."
    else:
        kami "Même ce détournement, vous l'avez presque entièrement raté. Je serais déçue si je n'avais pas trouvé votre panique aussi divertissante."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Dans tous les cas, votre intrusion, votre intention et votre insolence sont enregistrées."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je vais pourtant être généreuse : votre petit théâtre n'interrompra pas la procédure officielle."

    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Le Conclave n'est pas une antenne de secours."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "C'est un lieu de décision. Et il est temps de voter."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2
    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "determine"),
        ("noam",  "reflechit"),
        ("tomas", "culpabilite"),
        ("lysa",  "blase"),
        ("nyra",  "stress"),
        ("kael",  "inquiet"),
    ])

    noam reflechit "Kami dit ça, mais si elle l'avait voulu, elle aurait pu couper notre signal."

    ryn colere "Elle savait qu'ils nous entendaient. Elle a laissé passer le signal juste assez longtemps pour les regarder courir."
    ryn colere2 "Tu as posé leurs vies sur cette table et tu en es presque à la remercier ?!"

    nyra reflechit "Finalement, avait-elle vraiment le choix ? Tout est filmé, tout le monde aurait vu qu'elle tenterait de nous censurer."

    noam sourire "Il lui aurait été difficile de se faire passer pour la gentille qui nous a attendus avant de faire appliquer les règles."

    sael determine "Alors qu'elle nous laisse terminer. Il nous faut quelques minutes supplémentaires seulement. Même les condamnés ont droit à une dernière parole."

    $ hideGroup()
    play sound sfx_gresillement
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Non. Vous avez déjà pris suffisamment de temps au Conclave. Il va désormais être temps de voter."

    jump _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS

label _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS:
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "determine"),
        ("noam",  "reflechit"),
        ("tomas", "culpabilite"),
        ("lysa",  "blase"),
        ("nyra",  "stress"),
        ("kael",  "inquiet"),
    ])

    tomas raison "Kami, tu peux nous dire quel est le statut des campements qui ont commencé à se disperser ? Leur situation a-t-elle changé pendant la procédure ?"

    nyra raison "Donne-nous un relevé en direct. Si tu veux une décision qui soit adaptée, montre-nous l'état réel du terrain avant le vote."

    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu veux savoir combien de personnes restent en danger avant de lever la main ? C'est touchant, mais le vote porte sur une règle, pas sur une situation précise."
    kami "Dois-je vous rappeler que si les gens se sont entassés, c'est avant tout de VOTRE faute ?!"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Quelle idée de dire devant le monde entier que je n'appliquerais plus les Commandements !"
    kami "Les Commandements sont ABSOLUS ! Je vous fais déjà une fleur considérable en retardant leur exécution."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je ne peux rien faire de plus pour vous aider à soulager votre conscience."

    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "determine"),
        ("noam",  "reflechit"),
        ("tomas", "culpabilite"),
        ("lysa",  "blase"),
        ("nyra",  "stress"),
        ("kael",  "inquiet"),
    ])

    noam triste "Au contraire, Kami. Tu as abandonné ton poste. C'est cet abandon de poste qui a donné de l'espoir aux gens."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais c'est qu'il me remet la faute dessus, en plus ?!"
    kami "J'ai bien compris votre petit stratagème, vous voulez m'emmener dans un débat inutile pour gagner du temps."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "La décence vous oblige justement à voter vite. Après tout, c'est moi qui donne le tempo ici."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "determine"),
        ("noam",  "reflechit"),
        ("tomas", "culpabilite"),
        ("lysa",  "blase"),
        ("nyra",  "stress"),
        ("kael",  "inquiet"),
    ])

    noam determine "Quand bien même, tu cherches à nous faire porter la responsabilité du tir, alors que tu contrôles le canon et le temps que tu nous accordes."
    noam colere "Tu pourrais sauver des gens innocents !"

    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Celui qui ne respecte pas les règles n'est pas innocent. La nuance vous échappe uniquement parce qu'elle vous est désagréable."

    noam colere "Mais..."

    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Assez."
    kami "Le débat est terminé. Les demandes de délai, de clarification et les appels à la décence sont rejetés."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    kami "Vous devez voter. Immédiatement."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "determine"),
        ("noam",  "reflechit"),
        ("tomas", "culpabilite"),
        ("lysa",  "blase"),
        ("elen",  "sourire"),
        ("nyra",  "stress"),
        ("iris",  "blase"),
        ("kael",  "inquiet"),
    ])

    "Les douze pupitres s'allument. Sur chacun, les mêmes mots apparaissent : POUR et CONTRE."

    elen joie "On a réussi à gagner du temps, beaucoup ont dû réussir à se sauver !"

    iris blase "T'es bien naïve. Mais on a plus vraiment le choix de toute façon..."

    play sound sfx_beep

    "Personne ne regarde vraiment son écran. Tous cherchent sur les visages des autres le moindre signe d'hésitation."

    think "Une seule voix contre suffit. Une seconde de peur peut annuler tout ce que nous venons de tenter."

    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vous rappelle que ne pas voter n'est pas une échappatoire. Dans le contexte actuel, votre silence aurait une valeur morale particulièrement intéressante."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je suis certaine que les Limenois apprécieront toutes vos nuances."

    hide screen kami_broadcast_ui

    $ hideGroup()
    jump _9_0_1_VOTE

label _9_0_1_VOTE:
    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    scene black with dissolve

    $ _vote_result = renpy.call_screen("vote_screen")
    $ j901_player_vote = _vote_result if _vote_result in ("pour", "contre") else "contre"
    $ j901_vote_adopte = (j901_player_vote == "pour")

    if j901_player_vote == "pour":
        scene Solid("#0AFF8844")
        with Dissolve(0.12)
    elif j901_player_vote == "contre":
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    $ showGroup([("noam", "inquiet", 0.50)])

    "Les pupitres enregistrent les choix puis s'éteignent les uns après les autres. Aucun nom, aucune main levée, seulement douze bulletins anonymes."

    think "Personne ne sait ce que les autres viennent de faire. Dans quelques secondes, un seul vote peut condamner tous les campements."

    $ hideGroup()
    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    if j901_vote_adopte:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "pour"),
        ]
    else:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "contre"),
        ]

    $ renpy.random.shuffle(vote_phase3_results)
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    pause 0.8

    $ j901_vote_adopte = (vote_phase3_counts["contre"] == 0)

    if j901_vote_adopte:
        jump _9_0_1_FIN_JOURNEE_VOTE_ADOPTE
    else:
        jump _9_0_1_FIN_JOURNEE_VOTE_REFUSE

label _9_0_1_FIN_JOURNEE_VOTE_ADOPTE:
    $ hideGroup()
    $ current_period = "Soir"
    stop music fadeout 0.8
    play sound sfx_announce

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.2

    kami "Résultat du vote : unanimité des suffrages exprimés. Aucun vote défavorable enregistré."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "L'unanimité a été atteinte. Les Commandements sont donc modifiés et ils s'appliquent immédiatement."
    $ interject("ADOPTÉ", color="#5DFF9A")

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Les regroupements de plus de vingt personnes sont désormais autorisés sous déclaration préalable. Application immédiate."

    if j901_signal_result_tier == "excellent":
        kami "La majorité des campements a eu le temps de se disperser ou de transmettre une déclaration d'urgence. Les pertes anticipées sont fortement réduites."
    elif j901_signal_result_tier == "bon":
        kami "Plusieurs campements ont reçu votre avertissement et se sont dispersés. Une partie des groupes sont néanmoins restés exposés."
    elif j901_signal_result_tier == "moyen":
        kami "Votre signal incomplet a atteint une fraction des campements. Une part significative des personnes sera éliminée pour ne pas avoir respecté les Commandements."
    else:
        kami "Votre signal a été largement inefficace. Le vote protège les campements encore reconnus comme tels, mais plusieurs applications du Commandement ont précédé l'enregistrement."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous voyez ? Lorsque vous obéissez à la procédure, des vies peuvent être sauvées. Ou pas."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Quelle belle leçon collective. Ah, et n'oubliez pas !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je ne disparaîtrai jamais !"

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Personne ne répond. Nous avons obtenu l'unanimité, mais le bilan de Kami transforme le soulagement en quelque chose de trop lourd pour être appelé une victoire."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_319
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    "Le retour jusqu'aux chambres se fait sans discussion. Les portes s'ouvrent et se ferment tandis que nos pas résonnent dans le couloir."

    think "Nous avons sauvé ceux qui ont eu le temps de nous écouter. Pour les autres... Nous avons fait ce qu'on a pu..."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_320
    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je rentre dans ma chambre. Je reste debout devant le lit, les mains vides et la gorge sèche."

    think "Nous avons gagné. Non... Nous avons voté assez vite pour que Kami puisse appeler ça une victoire."
    think "On a essayé de gagner du temps. Mais est-ce que ce sera suffisant ?"

    "Je m'assieds et fixe l'écran mural entièrement noir."

    think "Demain matin, il se rallumera et tout reprendra comme avant..."
    think "Putain mais quel enfer !"

    $ hideGroup()
    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_26
    # La suite du vote adopte est encore en developpement ; le J10 jouable
    # correspond au rejet et aux tirs du canon, pas a cette issue.
    call screen kd_route_vote_convergence
    $ j901_vote_adopte = False
    call end_day("10") from _call_end_day_13
    jump _10_0_1_1_REVEIL_CHAMBRE

label _9_0_1_FIN_JOURNEE_VOTE_REFUSE:
    $ current_period = "Soir"
    $ hideGroup()
    stop music fadeout 0.6
    play sound sfx_announce

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Résultat du vote : absence d'unanimité."
    $ interject("REJETÉ", color="#FF4D6D")
    kami "L'amendement est rejeté."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "L'interdiction des regroupements de plus de vingt personnes demeure en vigueur. Les campements limenois restent donc des rassemblements illégaux."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Le Commandement IV rentre donc de nouveau en application, selon vos désirs."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Pendant une seconde, personne ne réagit. Puis nous comprenons tous en même temps ce que signifie son dernier mot."

    play sound sfx_gresillement

    scene bg_conclave at adaptive_fullscreen, heavy_shake
    $ showGroup([
        ("ryn", "colere2", 0.25),
        ("noam", "surpris", 0.50),
        ("sael", "peur", 0.75),
    ])

    "Le Conclave tremble. Très loin sous nos pieds, un mécanisme immense commence à s'aligner."

    ryn colere2 "Non ! Putain mais qui a voté contre ?!"
    ryn colere "Vous êtes des grands malades !!"

    "Personne ne répond. Tout le monde baisse la tête. Cet échec, c'est le nôtre."

    think "Ai-je bien fait de voter contre ?"

    "Tout le monde se disperse alors que les murs tremblent sous les tirs incessants du Conclave."

    play sound sfx_laser_canon volume 8.0

    scene bg_conclave at adaptive_fullscreen, heavy_shake

    $ hideGroup()
    scene black with Fade(0.1, 0.2, 0.8)

    "Je ne sais même plus comment a fini cette journée."
    "La seule chose dont je me souviens, c’est mon réveil du lendemain."

    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_27
    call end_day("10") from _call_end_day_14
    jump _10_0_1_1_REVEIL_CHAMBRE

    #jump patreon_ending

# Total journée : 10 minutes
# Durée totale : 2h20
