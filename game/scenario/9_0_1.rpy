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
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_9_0_1
    call j901_play_signal_vivant from _call_j901_play_signal_vivant
    $ j901_signal_result_tier = _return
    jump _9_0_1_CONCLAVE_DEBAT_PARTIE_2


label _9_0_1_CONCLAVE_DEBAT_PARTIE_2:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere", 0.10), ("sael", "determine", 0.27),
        ("tomas", "culpabilite", 0.43), ("noam", "inquiet", 0.57),
        ("nyra", "stress", 0.73), ("kael", "inquiet", 0.90),
    ])
    "Le signal commence à se brouiller. Sur l'écran de Kael, des silhouettes se dispersent dans les allées d'un campement, puis l'image se fige."
    tomas inquiet "Je ne vois plus le dernier relais."
    kael reflechit "Le flux est coupé."
    ryn colere "Relance-le !"
    kael neutre "Pas sans savoir pourquoi il s'est interrompu."
    ryn colere "On s'en fiche de pourquoi !"
    sael determine "Non. S'il s'agit de Kami, tu ne feras qu'aggraver les choses."
    ryn colere "Et toi, tu voudrais qu'on attende ?!"
    sael neutre "Je voudrais que tu me laisses finir une phrase."
    "Ryn ouvre la bouche, se ravise, puis frappe le dossier de sa chaise."
    noam reflechit "Certains nous ont entendus. C'est déjà ça."
    nyra reflechit "Ce n'est pas la même chose que de les avoir mis à l'abri."
    noam neutre "Je sais."
    "Je regarde les zones encore grises sur la carte. Ce sont des endroits où des gens vivent, et je n'ai même pas le moyen de savoir si l'un d'eux m'a entendu."
    $ hideGroup()
    play sound sfx_gresillement
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "EH BIEN ! Quelle magnifique émission spéciale ! Vous avez presque réussi à me voler mon propre public !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Des ordres criés, des petits humains qui courent, des grands gestes désespérés... Tout ce que j'aime dans une bonne téléréalité."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    if j901_signal_result_tier == "excellent":
        kami "Je dois reconnaître une belle performance : la majorité des campements a reçu votre message. C'est... agaçant."
    elif j901_signal_result_tier == "bon":
        kami "Une partie importante des campements vous a entendus. Vous avez presque de quoi vous féliciter. Presque."
    elif j901_signal_result_tier == "moyen":
        kami "Quelques campements ont reçu votre message. Les autres ont surtout eu droit à une démonstration de votre enthousiasme."
    else:
        kami "Votre transmission ? Un chef-d'œuvre de confusion. J'hésite entre vous donner une mauvaise note et vous demander de recommencer pour le spectacle."
    ryn "Alors laisse-nous recommencer !"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "NON."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous avez utilisé ma retransmission officielle pour détourner le débat. C'est une initiative que j'inscris précieusement dans vos dossiers."
    iris "Qu'elle nous colle une punition, alors ! Ça changera de ses sermons !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais je ne vous punirai pas aujourd'hui. Voyez comme je suis patiente."
    kami "Vous avez voulu prévenir ces campements. Très bien. Maintenant, vous allez choisir ce qu'il adviendra d'eux."
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "LE DÉBAT EST TERMINÉ."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2
    $ showGroup([
        ("ryn", "colere"), ("sael", "determine"), ("noam", "reflechit"),
        ("tomas", "culpabilite"), ("lysa", "blase"), ("nyra", "stress"),
        ("kael", "inquiet"), ("elen", "peur"), ("mara", "stress"),
    ])
    elen peur "Déjà ?! Mais il y a encore des gens dans les campements !"
    mara agace "Elle s'en fiche, Elen."
    elen colere "ALORS JE NE M'EN FICHE PAS, MOI !"
    "Mara la regarde. Elle ne trouve pas de plaisanterie à ajouter."
    lysa blase "Bravo. Nous venons de découvrir que notre présidente n'aime pas qu'on lui prenne le micro."
    noam determine "Kami, tu aurais pu couper la diffusion dès le début."
    sael determine "Et elle ne l'a pas fait."
    ryn colere "Tu vas quand même pas la remercier !"
    sael mefiant "Je constate un fait. Ne me prête pas tes propres pensées."
    nyra reflechit "La retransmission est publique. Elle aurait montré à tous qu'elle nous empêchait d'alerter des innocents."
    mara doute "Ou alors elle aime juste regarder les gens courir."
    "Je pense à l'enthousiasme de Kami. Les deux explications me paraissent possibles."
    tomas inquiet "Il nous faut encore du temps. Même quelques minutes."
    lysa reflechit "Tu as quelque chose à proposer ?"
    tomas gene "Plusieurs choses, mais aucune très honnête."
    julian "Alors c'est le moment idéal pour me laisser intervenir !"
    iris colere "Non, Julian. Pour une fois, ce n'est pas de toi qu'on parle !"
    julian "Je voulais seulement gagner du temps !"
    elias "Et tu comptais le faire en parlant jusqu'à demain ?"
    julian "Exactement !"
    "Un rire nerveux passe autour de la table. Il s'éteint lorsque les pupitres s'illuminent."
    sael determine "On ne peut pas l'empêcher de lancer la procédure."
    noam reflechit "Mais on peut peut-être la retenir dans une conversation."
    lysa blase "Si la survie de milliers de gens dépend du talent de Julian pour ennuyer son public, nous sommes condamnés."
    julian "Je n'ai jamais eu autant envie de te donner tort."
    $ hideGroup()
    play sound sfx_gresillement
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "J'ai entendu ce petit conciliabule. Et non, Julian, je ne vais pas écouter ton discours."
    julian "C'est de la censure !"
    kami "C'est de l'hygiène."
    hide screen kami_broadcast_ui
    jump _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS


label _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS:
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "colere"), ("sael", "determine"), ("noam", "reflechit"),
        ("tomas", "culpabilite"), ("lysa", "blase"), ("nyra", "stress"),
        ("kael", "inquiet"),
    ])
    tomas reflechit "Je demande une précision technique sur le texte."
    ryn colere "MAINTENANT ?!"
    tomas inquiet "Précisément maintenant. L'expression « idéalement avec déclaration préalable » reste ambiguë."
    nyra raison "Une fois le texte adopté, les campements constitués avant le vote seront-ils couverts ?"
    sael determine "C'est une question légitime."
    lysa blase "Et accessoirement une question qui prend du temps."
    noam determine "Kami, on ne te laissera pas esquiver ça aussi facilement."
    call refutation_run("j9_regroupements")
    if _return[0] == "success":
        call play_noam_interupt
        tomas raison "On a encore le droit de demander des précisions avant de voter !"
    else:
        nyra reflexion "Elle ne nous donnera pas plus. Il va falloir avancer avec ce qu'on sait."
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Mes chers élèves, je vois que vous avez découvert les subtilités de la langue française !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quel dommage que le dictionnaire ne puisse pas vous servir de bouclier."
    noam "Tu pourrais au moins nous communiquer le nombre de campements encore concernés."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous savez, Noam, les chiffres sont parfois si tristes. Et vous avez déjà l'air d'une assemblée à un enterrement."
    ryn "COMBIEN ?!"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ryn ! Je ne répondrai certainement pas à quelqu'un qui me hurle dessus !"
    lysa "Alors réponds à celui qui a demandé poliment."
    pause 0.6
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous avez compris le principe du jeu, n'est-ce pas ? Vous essayez de me faire parler pour donner aux campements quelques minutes supplémentaires."
    noam determine "Tu as créé cette situation. Ils se sont regroupés pendant ton absence."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je ne suis pas responsable de chaque mauvaise décision prise par un humain quand je cesse de lui tenir la main."
    sael "Et pourtant tu t'es attribué le droit de les tuer."
    pause 0.5
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "J'APPLIQUE LES COMMANDEMENTS."
    elen "Mais tu peux les suspendre ! Tu viens de le faire !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Pour vous laisser choisir. C'est ce qu'on appelle la générosité."
    noam colere "Non. C'est ce qu'on appelle nous faire porter ta responsabilité !"
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "ASSEZ !"
    stop music fadeout 0.5
    "Le son s'interrompt. Pendant une seconde, je n'entends que le souffle des autres."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Fin des questions. Fin des commentaires. Vote immédiat."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere"), ("sael", "determine"), ("noam", "reflechit"),
        ("tomas", "culpabilite"), ("lysa", "blase"), ("elen", "peur"),
        ("nyra", "stress"), ("iris", "blase"), ("kael", "inquiet"),
    ])
    "Les pupitres s'éclairent. POUR. CONTRE. Deux mots, et toutes les nuances qui nous ont occupés depuis ce matin disparaissent."
    elen inquiet "On a gagné un peu de temps, non ?"
    nyra reflechit "Oui. Combien de vies, je l'ignore."
    ryn colere "Alors on vote pour. TOUS."
    iris colere "Arrête de nous donner des ordres !"
    ryn colere "TU VEUX QU'ILS MEURENT ?!"
    iris colere "NON ! Je veux juste qu'on arrête de me hurler dessus comme si c'était moi qui allais tirer !"
    sael determine "Ryn. Ça suffit."
    ryn colere "..."
    sael determine "Je voterai pour."
    "Ryn tourne la tête vers elle. Un instant, je retrouve le souvenir de leur dispute au vote précédent."
    sael neutre "Je n'ai pas changé d'avis sur les frontières. Mais ces gens ne méritent pas la mort pour s'être rassemblés."
    lysa blase "Voilà une phrase qu'on aurait aimé entendre dans une autre circonstance."
    tomas inquiet "Même un vote unanime ne garantit pas que les camps seront régularisés. Il faut le savoir."
    noam determine "Je le sais."
    "Je croise le regard de Kael. Il ne me regarde pas longtemps, puis baisse les yeux vers son pupitre."
    think "Il cherche toujours la photo de Léa. Moi, le dessin de Juliette. Dans quelques minutes, ces objets auront l'air dérisoires, et je les chercherai quand même."
    play sound sfx_beep
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pensez à vos électeurs ! Enfin, ceux qui auront encore la possibilité de vous remercier."
    hide screen kami_broadcast_ui
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
        scene expression Solid("#0AFF8844")
        with Dissolve(0.12)
    elif j901_player_vote == "contre":
        scene expression Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene expression Solid("#FF2A2A44")
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
    kami "Douze bulletins. Aucun vote défavorable. Unanimité !"
    $ interject("ADOPTÉ", color="#5DFF9A")
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "BRA-VO ! Vous avez enfin réussi à être d'accord sur quelque chose ! Je savais que la peur était un excellent outil pédagogique."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le Commandement IV est modifié. Les regroupements de plus de vingt personnes sont désormais autorisés, idéalement sous déclaration préalable."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    if j901_signal_result_tier == "excellent":
        kami "Votre avertissement a atteint la majorité des campements. Beaucoup ont pu se disperser ou transmettre une déclaration d'urgence. Les pertes prévues ont fortement diminué."
    elif j901_signal_result_tier == "bon":
        kami "Plusieurs campements ont suivi vos instructions. D'autres sont restés exposés. Une réussite incomplète, comme vous les aimez."
    elif j901_signal_result_tier == "moyen":
        kami "Votre signal n'a atteint qu'une partie des campements. Certains groupes ont pu s'éloigner, mais beaucoup demeurent concernés par les sanctions applicables."
    else:
        kami "Votre transmission a surtout semé la confusion. Certains campements ont pu se disperser, d'autres non. Quelques sanctions ont même précédé la validation du scrutin."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais ne faites pas cette tête ! Après tout, vous avez gagné votre vote."
    noam "Combien de personnes ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu sais, Noam, tu as vraiment le chic pour gâcher les beaux moments."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Et une dernière chose : je ne disparaîtrai JAMAIS."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "fatigue"), ("sael", "neutre"), ("noam", "inquiet"),
        ("tomas", "inquiet"), ("lysa", "triste"), ("elen", "peur"),
        ("kael", "fatigue"),
    ])
    elen hesitation "On l'a fait..."
    julian "Unanimité. Pour la première fois depuis..."
    lysa blase "Ne gâche pas ça avec un discours."
    julian "Je n'allais pas..."
    mara "Si. Tu allais."
    ryn fatigue "Combien sont encore là-bas ?"
    tomas inquiet "Je vais essayer d'avoir les chiffres."
    sael neutre "Ceux qui ont survécu n'ont plus à se cacher pour rester ensemble."
    ryn reflechit "Ce n'est pas la même chose que pouvoir rentrer chez soi."
    sael triste "Non."
    "Ils ne se disputent pas. Je ne sais pas ce qui m'inquiète le plus : leur silence, ou le fait qu'il ait fallu tout ça pour qu'il existe."
    noam neutre "On a empêché le pire pour une partie d'entre eux."
    lysa neutre "Et on ne sait pas encore pour les autres."
    "Elen ouvre la bouche, comme si elle voulait nous féliciter. Elle y renonce."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_319
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0
    "Dans le couloir, Julian marche à côté de moi."
    julian "Je pensais que réussir un vote ferait plus de bruit."
    noam neutre "Moi aussi."
    julian "C'est une victoire, tout de même."
    noam reflechit "Oui. Je suppose."
    julian "Tu sais, pour une fois, je n'essayais pas de faire un discours."
    noam taquin "C'est dommage. Il aurait été très court."
    julian "Tu vois ? On se moque toujours des grands hommes."
    "Je souris malgré moi. Au bout du couloir, il me laisse devant ma porte."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_320
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je regarde la place vide sur le bureau. Le dessin de Juliette n'est pas revenu."
    think "Douze votes pour. Et je ne sais toujours pas combien de personnes nous avons sauvées."
    "Je ferme la porte, sans déplacer de meuble."
    think "Ce soir, je n'ai pas envie de croire que la peur doit gagner à chaque fois."
    $ hideGroup()
    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_26
    # La suite du vote adopté n'est pas encore écrite : convergence provisoire.
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
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Dépouillement terminé."
    pause 0.6
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh..."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quel dommage. Il semblerait que vous ne soyez pas capables de vous mettre d'accord."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'unanimité n'est PAS atteinte."
    $ interject("REJETÉ", color="#FF4D6D")
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "L'amendement est rejeté. Le Commandement IV demeure en vigueur, sans modification."
    noam "Kami, attends ! Les campements, ils..."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Les campements ? Oui. J'avais promis de reprendre l'application du Commandement après le vote."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je tiens toujours mes promesses, moi."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Une chaise recule. Quelqu'un dit quelque chose, mais je n'entends pas les mots."
    play sound sfx_gresillement
    scene bg_conclave at adaptive_fullscreen, heavy_shake
    $ showGroup([
        ("ryn", "colere2", 0.25), ("noam", "surpris", 0.50), ("sael", "peur", 0.75),
    ])
    ryn colere2 "QUI ?!"
    "Un nouveau grondement monte depuis les profondeurs de la station."
    ryn colere "QUI A VOTÉ CONTRE ?!"
    sael peur "Ryn..."
    ryn colere2 "ILS ÉTAIENT LÀ ! ILS NOUS ÉCOUTAIENT !"
    noam inquiet "Ryn, on ne sait pas..."
    ryn colere "NE ME DIS PAS DE ME CALMER !"
    "Il fait un pas vers les autres sièges. Sael lui barre la route."
    sael determine "Ça ne changera rien."
    ryn colere "ÉCARTE-TOI !"
    sael determine "Non."
    "Je voudrais croire que quelqu'un va trouver une nouvelle procédure, une phrase oubliée dans le règlement, n'importe quoi qui empêcherait le canon de tirer."
    "Il n'y a que le grondement."
    play sound sfx_laser_canon volume 8.0
    scene bg_conclave at adaptive_fullscreen, heavy_shake
    "La première détonation secoue la salle si fort que je manque de tomber. La deuxième arrive avant que quelqu'un puisse reprendre son souffle."
    "Elen crie. Je ne sais pas si elle a vu quelque chose sur un écran ou si elle a simplement compris."
    think "Sur Terre, ils devaient encore courir. Certains ont dû entendre notre avertissement. D'autres..."
    "Je ferme les yeux, mais le sol continue de trembler."
    think "Un seul vote suffisait."
    $ hideGroup()
    scene black with Fade(0.1, 0.2, 0.8)
    "Je ne sais plus qui a quitté la salle le premier. Je me souviens seulement d'avoir attendu que les tirs s'arrêtent, et d'avoir compris qu'ils ne s'arrêteraient pas parce que nous le demandions."
    "La prochaine chose dont je me souviens clairement, c'est mon réveil du lendemain."
    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_27
    call end_day("10") from _call_end_day_14
    jump _10_0_1_1_REVEIL_CHAMBRE

