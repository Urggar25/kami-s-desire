# --------------------------------------------------------------------------------------------
# JOUR 9 — Réveil chambre
# Kami revient après deux jours de silence.
# Elle réveille directement Noam par annonce matinale.
# Convocation immédiate dans la salle du Conclave pour annoncer le prochain vote.
# --------------------------------------------------------------------------------------------

label _9_0_1_REVEIL_CHAMBRE:
    scene black
    $ current_day = 9
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5
    $ cafeteria_food_level = "medium"
    $ current_period = "Matin"
    $ blink()

    "Je dors par fragments. Chaque bruit du couloir me réveille assez longtemps pour que j'imagine une main sur la poignée."
    "Quelqu'un prêt à rentrer dans la chambre."

    think "La chaise est toujours coincée contre la porte. Si quelqu'un était entré, je l'aurais entendue tomber."

    noam "C'est déjà ça..."

    "Je commence enfin à replonger lorsque le silence se brise."

    stop music fadeout 0.5
    play sound sfx_announce

    pause 1.0

    $ hideGroup()
    play music "music/bgm_system_override.mp3" fadein 1.0
    show screen kami_broadcast_ui

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Bonjour, mes petits représentants ! Vous avez réussi à survivre deux journées entières sans mon annonce matinale. Je suis presque impressionnée."

    noam "Évidemment, ça ne pouvait pas durer..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Avouez-le : je vous ai terriblement manqué. De mon côté, cette séparation m'a paru interminable."

    think "Sa voix est exactement la même : claire, nasillarde et presque chantante. Elle parle comme si elle n'avait jamais disparu."
    think "Comme si elle avait toujours été là. En silence. Comme si elle nous regardait en mangeant tranquillement un pot entier de popcorn."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Il s'en est passé, des choses, pendant ma courte absence. Vous avez presque commencé à vous comporter comme si personne ne vous surveillait."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Rassurez-vous, votre période d'abandon émotionnel est terminée."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Maman est de retour."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je constate que certains ont pris des initiatives décoratives pendant mon absence. Des portes barricadées avec du mobilier... Quelle créativité."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C'est adorable. Vous ressemblez à des enfants persuadés que leur cabane devient imprenable dès qu'ils placent une chaise devant l'entrée."
    kami "De quoi avez-vous peur ? De vos petits camarades ? RI-SIBLE."

    think "Elle a tout vu. Bien sûr qu'elle l'a vue. Deux jours de silence ont suffi pour nous faire oublier que ses yeux n'avaient peut-être jamais cessé de fonctionner."

    $ bc_show("noam", "surpris", px=-70, py=-50, pz=0.60)
    noam surpris "Qu'est-ce qui s'est réellement passé pendant ces deux jours ?"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh, Noam ose poser la question directement. Tu veux vraiment savoir pourquoi je vous ai laissés seuls ?"

    $ bc_show("noam", "reflexion", px=-70, py=-50, pz=0.60)
    noam inquiet "Tu as disparu pendant deux jours. Aucune annonce, aucune exécution et aucune explication."
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "« Disparu » est un mot bien dramatique. J'ai simplement subi une petite opération de maintenance."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'aurais préféré vous faire croire à une expérience complexe, mais même moi, j'ai parfois besoin de congés. Payés, évidemment."
    kami "Vous savez, je pense sincèrement que je devrais mettre en place un code du travail !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Vous aussi, vous devez respecter mes droits !"
    kami "Après un an à travailler jour et nuit pour maintenir l'ordre, personne ne peut me reprocher une courte maintenance !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ce matin, le programme officiel reprend. Tous les représentants sont convoqués immédiatement dans la salle du Conclave pour l'annonce du prochain vote."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je vous recommande de ne pas traîner. Nous n'avons déjà plus beaucoup de temps."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])

    "L'écran reste blanc quelques secondes avant de s'éteindre. Aucun glitch, aucune coupure, aucune déformation dans sa voix."

    think "Kami est revenue à la normale. Ou à ce qui porte ce nom ici."

    "Je passe une main sur mon visage, récupère ma veste et regarde une dernière fois la chambre avant de sortir."

    think "Elle revient en souriant et reprend le programme comme si rien ne s'était passé. Je le savais. Mais pourquoi est-ce aussi décevant ?"

    $ hideGroup()
    stop music fadeout 1.5
    scene black with fade
    jump _9_0_1_CONCLAVE_ANNONCE

label _9_0_1_CONCLAVE_ANNONCE:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_303
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    $ showGroup([
        ("lysa", "blase", 0.08),
        ("ryn", "fatigue", 0.25),
        ("noam", "inquiet", 0.42),
        ("iris", "fatigue", 0.58),
        ("mara", "stress", 0.75),
        ("elen", "peur", 0.92),
    ])

    "Les portes des chambres s'ouvrent presque en même temps. Personne n'a pris le temps de se préparer correctement."

    lysa blase "Le rêve est maintenant terminé, place au cauchemar. J'espère que vous en avez tous suffisamment profité."

    ryn fatigue "Avancez. Je n'ai aucune envie de lui donner une raison de nous attendre."

    iris fatigue "Toujours aussi charmant au réveil."

    mara stress "Aujourd'hui, personne n'est charmant. Vu les tronches qu'on tire."

    elen peur "Ça peut encore bien se passer. Enfin... Si on ne lui donne aucune raison de s'énerver."
    elen triste "Alors dépêchons-nous ! Peut-être que le prochain vote sera bien ?!"

    lysa triste "Elen, ne commence pas à chercher une règle capable de nous protéger. Pas maintenant."

    noam inquiet "Ouais, grouillons-nous ! J'ai peur de ce qui peut arriver."

    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_304
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa",  "blase",    0.10),
        ("ryn",   "fatigue",  0.27),
        ("sael",  "inquiet",  0.43),
        ("kael",  "fatigue",  0.57),
        ("tomas", "inquiet",  0.73),
        ("iris",  "fatigue",  0.90),
    ])

    "Nous prenons place sans attendre. Kael reste tourné vers l'écran central, le visage fermé."

    kael fatigue "Elle est revenue. Le penser dans le couloir et l'entendre ici, ce n'est pas la même chose."

    iris fatigue "Personne n'a besoin qu'on le répète, mais je comprends ce que tu veux dire."

    sael inquiet "Deux jours sans sa voix, puis elle revient comme si le silence n'avait jamais existé. C'est bien digne de Kami."

    ryn fatigue "Elle revient toujours. La vraie question, c'est ce qu'elle veut cette fois."

    $ hideGroup()
    play sound sfx_announce
    stop music fadeout 0.8
    show screen kami_broadcast_ui

    pause 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Bonjour, mes petits représentants. Quelle ambiance... On dirait que deux journées sans autorité maternelle ont suffi pour vous rendre nerveux."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le Conclave reprend son fonctionnement normal. Nous allons donc passer immédiatement au troisième vote."

    play sound sfx_tambour
    pause 1.0

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Je cite : autoriser les regroupements de plus de vingt personnes idéalement avec déclaration préalable."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "À l'heure actuelle, tout regroupement non déclaré de plus de vingt individus est interdit par le Commandement IV."
    kami "Un vote unanime en faveur de l'amendement autorisera par défaut ces rassemblements."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ce n'est pas encore la liberté totale. Chaque enfant doit apprendre à marcher avant de courir vers une insurrection."
    kami "J'en connais qui veulent retrouver le goût des festivals et aux concerts !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "En cas d'échec, l'interdiction actuelle restera en vigueur. Le vote aura lieu dans quelques instants, alors essayez de ne pas tout gâcher trop vite."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("tomas", "raison",    0.10),
        ("lysa",  "blase",     0.27),
        ("ryn",   "fatigue",   0.43),
        ("sael",  "inquiet",   0.57),
        ("noam",  "inquiet",   0.73),
        ("kael",  "fatigue",   0.90),
    ])

    tomas reflechit "Comme par hasard..."

    noam reflechit "Quoi ?! Qu'est-ce que tu veux dire par là, Tomas ?"

    tomas raison "Le libellé du vote correspond exactement à ce que j'ai observé ce matin dans la salle du canon."

    ryn fatigue "Explique clairement, Tomas."

    tomas culpabilite "Des habitants quittent massivement les profondeurs de Limen. Ils profitent probablement de la panne de Kami pour remonter vers les frontières."

    sael inquiet "Combien sont-ils ?"

    tomas culpabilite "Je n'ai pas de chiffre précis. Plusieurs milliers, peut-être plusieurs dizaines de milliers."

    ryn colere "Et tu gardais ça pour toi depuis ce matin ?!"

    tomas inquiet "Je vous rappelle qu'on est encore le matin ! Pour beaucoup vous venez juste de vous lever !"
    tomas colere "Ils ont installé des campements improvisés à plusieurs points de passage vers les autres districts."

    kael inquiet "Des campements de plusieurs milliers de personnes, donc forcément non déclarés."

    noam inquiet "Ils sont donc concernés par le quatrième commandement. Le vote ne tombe pas au hasard."

    tomas culpabilite "C'est aussi ma conclusion. Si l'interdiction reste en vigueur, le Commandement IV peut viser presque tous les campements."

    ryn colere2 "Tu me dis que des gens qui fuient Limen peuvent être exécutés uniquement parce qu'ils dorment trop nombreux au même endroit ?"

    tomas culpabilite "Oui. Juridiquement, c'est exactement ça."

    sael peur "Kami connaissait forcément leur présence avant de choisir ce texte."

    lysa blase "Ce n'est pas une coïncidence. C'est la raison même du vote."

    noam inquiet "Si nous votons pour, les regroupements deviennent possibles. Si une seule personne refuse..."

    ryn colere "Alors elle applique le Commandement. Putain, Kami ! Réponds-nous !"

    noam colere "Mais pourquoi est-ce que Kami ne les élimine pas immédiatement s'ils violent un Commandement ?"
    noam reflechit "Ça a toujours fonctionné comme ça, non ?!"

    $ hideGroup()
    play sound sfx_announce
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Vous avez tout compris. Je suis particulièrement fière de Tomas, même si la découverte lui a pris un peu de temps."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Les campements limenois actuellement installés aux frontières relèvent bien du Commandement IV. Chacun rassemble plusieurs centaines d'individus, évidemment rien n'était déclaré."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "J'ai cependant retardé l'application du Commandement pour vous laisser le temps de voter. Sans cette délicate attention, ces campements ne seraient déjà plus un problème."
    kami "Vous pouvez me remercier, MOI, déesse de clémence et de bienveillance !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Vous voyez ? Je peux être incroyablement attentionnée."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Après le vote, le Commandement IV sera appliqué selon la règle en vigueur. Avec ou sans modification."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous allez maintenant devoir choisir, mes petits humains préférés. Cette fois, réfléchissez très vite."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0

    $ showGroup([
        ("ryn",   "colere"),
        ("sael",  "peur"),
        ("tomas", "culpabilite"),
        ("lysa",  "triste"),
        ("noam",  "inquiet"),
        ("nyra",  "fatigue"),
        ("mara",  "stress"),
        ("iris",  "inquiet"),
        ("elen",  "peur"),
        ("elias",  "fatigue"),
        ("julian",  "inquietude"),
        ("kael",  "fatigue"),
    ])

    ryn colere "Elle savait tout. Elle a laissé les gens s'entasser, puis elle a transformé leur survie en sujet de vote."
    ryn colere2 "Qu'on ne vienne pas me dire que les sujets des votes sont tirés au hasard !!"

    nyra fatigue "Nous ne pouvons plus changer ce qu'elle a préparé. Il faut empêcher l'exécution."

    noam reflechit "De toute façon, on a qu'une seule solution : autoriser ces rassemblements."

    sael determine "Tout le monde vote pour. Aucun détour, aucune abstention et aucune lâcheté."

    ryn colere2 "Si quelqu'un ose voter contre, je—"

    noam determine "Ne termine pas cette phrase. On ne sauvera personne en commençant par nous menacer entre nous."

    ryn colere "Des milliers de personnes vont peut-être mourir et tu veux encore jouer au médiateur ?"

    noam determine "Surtout maintenant. La peur peut suffire à faire hésiter quelqu'un, et il nous faut une unanimité de vote pour."

    call play_stat_dialogue("d9") from _call_stat_dialogue_d9

    "Je regarde tout le monde dans le blanc des yeux."
    elen "..."
    kael "..."
    tomas "..."

    noam determine "Tout le monde semble d'accord sur la nécessité de voter pour."

    tomas raison "M-Mais, il y a un problème, je crains que ce ne soit pas suffisant. On ne sait pas ce que veut dire idéalement avec déclaration préalable."

    noam reflechit "Les campements existent déjà. Même si nous autorisons les regroupements, ils n'auront pas été déclarés avant leur formation."
    noam colere "Tu crois qu'ils pourraient quand même être considérés comme illégaux ?!"

    ryn colere2 "Ils ne pouvaient rien déclarer ! Kami était en maintenance !"

    nyra raison "Ça ne l'empêchera pas d'appliquer la règle strictement. Le vote peut autoriser les futurs regroupements sans régulariser ceux qui existent déjà."

    sael determine "Et nous ne pouvons pas modifier le texte après son annonce. Kami a toujours verrouillé le libellé avant le débat."

    ryn colere "Alors à quoi sert notre vote s'ils peuvent mourir dans les deux cas ?!"

    noam determine "C'est un piège. Elle veut nous faire croire qu'on a le choix et la possibilité de les sauver."
    noam reflechit "Mais il y a un moyen pour les sauver en respectant les Commandements !"
    noam determine "Si les gens suivent la diffusion du Conclave, ils se disperseront en comprenant qu'ils peuvent peut-être mourir."

    sael inquiet "Ils devront s'éloigner des points de passage et renoncer à franchir la frontière."
    sael colere "Je vous l'avais dit que cette histoire de traverser les frontières était dangereuse."

    ryn colere "Ils fuient Limen ! Tu crois qu'ils vont gentiment se ranger en petits groupes et repartir parce qu'on le leur demande ?!"

    noam inquiet "Non. Mais ils n'ont déjà aucune chance de traverser aujourd'hui. Nous pouvons au moins leur éviter d'être regroupés au moment où Kami appliquera le Commandement."

    nyra raison "La diffusion du débat est publique. Kami veut que le monde entier nous regarde, alors utilisons cette audience contre elle."

    tomas raison "Il faudra donner des instructions précises : groupes de moins de vingt, éloignement des points de passage et aucun franchissement sans autorisation."

    lysa blase "Notre stratégie repose donc sur une évacuation improvisée diffusée en direct. Ce n'est pas glorieux, mais c'est mieux qu'une prière."

    elen peur "Et s'ils ne peuvent pas partir ? Il y a sûrement des enfants, des blessés et des gens trop épuisés pour bouger."
    elen colere "Non, on va arriver ! Gardons espoir !"

    noam inquiet "On ne pourra pas le savoir, on ne sait même pas où sont les campements."

    tomas inquiet "Peut-être qu'on peut avoir accès aux données depuis une de nos tablettes ?"

    kael sourire "C'est peut-être faisable ! Attends, file-moi ta tablette !"
    kael reflechit "Je vais voir si on peut se connecter aux données de la salle du canon !"

    $ hideGroup()
    call j901_play_hack from _call_j901_play_hack_day9
    $ j901_hack_success = bool(_return)
    $ showGroup([
        ("kael", "joie", 0.32),
        ("noam", "determine", 0.68),
    ])

    kael joie "Ok ! C'est configuré, on a accès aux images !"

    noam sourire "Donc maintenant, on doit leur dire de se disperser !"

    elias inquiet "Il faut parler assez clairement pour que ceux qui peuvent bouger le fassent tout de suite."

    julian determine "On a une chance unique de sauver des innocents, faisons-le !"

    iris fatigue "Pourquoi est-ce toujours à nous de réparer les bêtises des autres ..? Bon, allons-y."

    noam raison "Il faudra aussi gagner chaque seconde possible après le signal. Plus ils disposent de temps, moins ils seront nombreux dans les campements."

    kael joie "En tout cas ça marche, certaines personnes commencent à se disperser !"

    noam reflechit "Super ! Continuons à en parler, il faut qu'ils se dispersent !"

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

    call end_day("10") from _call_end_day_14
    jump _10_0_1_1_REVEIL_CHAMBRE

    #jump patreon_ending

# Total journée : 10 minutes
# Durée totale : 2h20
