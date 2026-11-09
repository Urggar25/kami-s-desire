# 6_0_1.rpy
# Jour 6 - Branche statu quo post-accident café
# Style THL - version dialoguée, rythmée

default j601_border_news_seen = False

transform j601_sael_vote_strip:
    xalign 0.5
    yalign 0.5
    xysize (720, 1080)

label _6_0_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 6
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "low"

    $ blink()
    think "J'ouvre les yeux avant l'annonce. Deuxième vote aujourd'hui."
    think "Hier, Sael m'a expliqué pourquoi elle dirait non. Et Ryn m'a expliqué pourquoi il ne supporterait pas qu'elle le fasse."
    think "Pour changer, je suis coincé entre deux personnes qui ont de bonnes raisons de ne pas céder."
    think "J'avais espéré me réveiller avec une idée brillante. Un compromis, un argument imparable, n'importe quoi."
    think "À la place, j'ai une marque d'oreiller sur la joue. Ça va sûrement sauver beaucoup de monde."
    "J'attrape ma tablette. Quatorze heures. Il nous reste quelques heures pour nous convaincre de ce qu'on sait déjà."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "BOOOONJOUR, mes petits législateurs ! Aujourd'hui, deuxième grand vote ! J'espère que vous avez enfin appris à compter jusqu'à douze."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rendez-vous à quatorze heures au Conclave. Au programme : les frontières ! Et tous les charmants désaccords qui vont avec."
    "La dernière syllabe s'étire étrangement."
    "Le sourire de Kami reste figé une fraction de seconde."
    think "Je m'attends à une plaisanterie. Elle ne vient pas."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous pouvez encore discuter avant le scrutin ! Une dernière occasion de... de..."
    pause 0.7
    kami "...De vous mettre d'accord. Oui. C'est bien ça."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "La cafétéria est ouverte ! Profitez de vos délicieuses rations. Le ravitaillement est prévu demain matin."
    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    think "Je reste devant l'écran noir."
    think "Quand Kami veut nous faire peur, elle le fait avec une joie insupportable. Là, elle avait surtout l'air de chercher ses mots."
    think "Peut-être que je me fais des idées. Ce ne serait pas la première fois."
    think "Je vais quand même demander aux autres."
    "J'enfile ma veste et quitte la chambre. Au moins, si Kami a décidé d'inventer le bégaiement, elle aurait pu commencer par une meilleure blague."

    $ current_scene_active = "_6_0_1_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    call KD_ROUTE_J6_ELEN from _call_optional_kd_route_j6_elen
    tuto "(Rejoins la cafétéria.)"

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_6_0_1_CAFETERIA
    $ current_scene_active = None

    jump _6_0_1_CAFETERIA

label _6_0_1_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_263
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Une conversation traverse toute la cafétéria avant même que je pose un pied dedans."
    think "Au moins, cette fois, quelqu'un a trouvé un sujet qui n'est pas directement le vote. Enfin... j'espère."

    $ showGroup([
        ("elias", "fatigue"),
        ("mara", "neutre"),
        ("elen", "neutre"),
        ("lysa", "blase"),
        ("iris", "fatigue"),
        ("sael", "neutre"),
    ])

    elen inquiet "NOAM ! Dis-moi que tu as entendu ! Kami a fait... un truc !"
    noam surpris "Un truc ? Ça réduit peu les possibilités."
    elen inquiet "Elle s'est arrêtée au milieu d'une phrase ! Toute seule !"
    noam reflechit "J'ai vu. J'ai attendu la chute de sa blague, mais il n'y en avait pas."
    elias fatigue "Pareil dans le dortoir. Et sur ma tablette."
    elias inquiet "Pour une fois que ce n'est pas mon matériel qui plante, je sais même pas si je dois être soulagé."
    mara taquin "Elle a peut-être découvert qu'on pouvait réfléchir AVANT d'ouvrir la bouche."
    mara sourire "Une révolution technologique."
    lysa blase "Une IA qui hésite. Dramatique. Si elle commence à oublier les prénoms, je propose qu'on l'envoie à la retraite."
    iris reflechit "Non, il y a quelque chose qui cloche. Quand Kami se moque de nous, elle nous force à le remarquer."
    iris inquiet "Là, elle a repris comme si elle espérait qu'on n'avait rien vu."
    elen taquin "Ou alors... elle est fatiguée !"
    elen joie "Imaginez Kami à la plage ! Avec un tout petit parasol sur un serveur géant !"
    elias sourire "Et nous, pendant ce temps-là, on pourrait enfin commander autre chose que ces barres de rationnement."
    mara rire "Dans ce cas, je lui réserve les vacances les plus longues de l'histoire. Sans billet retour."
    sael mefiant "Vous avez fini ?"
    sael neutre "Elle contrôle les portes, les livraisons et les sanctions. Si elle a réellement un problème, je voudrais le savoir AVANT qu'on lui confie un nouveau vote."
    noam inquiet "Elias... la console d'hier. Tu crois qu'elle pourrait avoir provoqué ça ?"
    elias inquiet "Je... j'espère que non ! J'ai demandé à Kael de vérifier l'observatoire."
    elias reflechit "Un panneau de contrôle local, ça devrait pas pouvoir toucher Kami. Enfin... « devrait », c'est le mot qui m'embête."
    iris fatigue "Attends. L'accident du café ?"
    iris blase "Elias, tu ne vas pas te déclarer responsable de tous les dysfonctionnements de l'univers pour une tasse renversée."
    elias reflechit "Je m'accuse pas !"
    elias gene "Enfin, j'essaie de ne pas m'accuser avant d'avoir les résultats de Kael."
    "Goumi arrive avec les plateaux. Elias pousse immédiatement sa tasse vers le centre de la table."
    think "Sa tasse a désormais une zone de sécurité personnelle."
    mara taquin "Oh ! Regardez ! Elias applique les règles de sécurité du café !"
    elias sourire "Exactement ! Plus de boisson près des machines, des câbles ou des objets coûteux !"
    mara taquin "Il te reste l'option de boire debout dans le couloir."
    elias gene "C'est... pas idiot."
    lysa reflechit "Bon, avant qu'on rédige un code de la sécurité des boissons : quelqu'un a parlé à Sael ?"
    sael determine "Je suis juste en face de toi, Lysa."
    sael neutre "Tu peux encore t'adresser directement à moi. C'est autorisé."
    lysa blase "Je sais. Je voulais savoir si quelqu'un avait réussi à avoir une discussion, pas une déclaration de vote."
    sael neutre "Noam est venu me voir hier. On a parlé."
    sael determine "Et non, je n'ai pas changé d'avis."
    elen triste "J'ai vu des enfants attendre aux frontières à la télévision... Ils espèrent vraiment pouvoir revoir leurs proches."
    sael triste "Je le sais, Elen."
    sael determine "Et je ne pourrai pas regarder les miens en face si j'ouvre notre village à ceux qui nous attaquaient. Je suis désolée."
    mara agace "On n'arrive déjà pas à assurer les livraisons normales. Mais oui, ouvrons toutes les routes d'un coup. Qu'est-ce qui pourrait mal se passer ?"
    noam neutre "Il reste quelques heures. On pourrait au moins finir de manger avant de recommencer la guerre des frontières."
    iris sourire "Merci. J'aimerais avaler une bouchée sans qu'on m'annonce une crise internationale entre le pain et le café."
    "Elen se penche sur la tasse d'Elias."
    elen taquin "Tu sais que Goumi peut peut-être te servir dans un gobelet fermé ?"
    elias sourire "Tu veux rire, mais j'y ai pensé."
    mara blase "Je savais qu'il y aurait un débat plus idiot que celui sur les frontières."
    think "La conversation repart sur le café. Au bout de quelques répliques, même Sael esquisse un sourire."
    think "Pendant quelques minutes, tout ressemble à un petit-déjeuner normal."
    think "Puis l'écran de la cafétéria change de programme. Les conversations ralentissent d'elles-mêmes."
    "Une carte de Limen apparaît. Le présentateur annonce un reportage sur les familles rassemblées près des postes de contrôle."
    call _6_0_1_TV_FRONTIERES from _call_6_0_1_TV_FRONTIERES_matinale
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "Ceux qui attendent derrière les barrières ont déjà fait leur choix."
    think "À quelques sièges de moi, Sael a fait le contraire."
    think "Il va falloir les regarder en face au moment de voter."

    jump _6_0_1_TEMPS_LIBRE

label _6_0_1_TEMPS_LIBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_264
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Fin de matinée"

    think "Il reste quelques heures avant le vote."
    think "J'aimerais parler aux autres sans transformer chacune de leurs réponses en argument électoral. On a déjà donné hier."

    call START_FREE_TIME("_6_0_1_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_6_0_1


label _6_0_1_TV_FRONTIERES:

    $ j601_border_news_seen = True
    $ unlock_gallery_image("bg_cg035")
    scene bg_cg035 at adaptive_fullscreen with dissolve
    "La caméra survole un poste de contrôle. Des sacs au sol. Des enfants assis sur des valises. Des adultes qui scrutent les barrières comme si elles pouvaient s'ouvrir à force de les regarder."
    "JOURNALISTE — Des familles se sont rassemblées dès l'aube devant plusieurs passages de Limen. Elles attendent le résultat du vote sur la libre circulation."
    "UNE FEMME — Mon frère est juste de l'autre côté. Je sais où il habite. Je sais qu'il est vivant."
    "UNE FEMME — Mais je peux pas aller le voir. Alors oui, je suis venue. J'avais envie qu'il sache que j'attendais encore."
    "Un homme intervient derrière elle."
    "UN HOMME — Et ceux qui venaient piller nos villages, vous allez les laisser passer aussi ? Qui va les arrêter, cette fois ?"
    "LA FEMME — Je ne demande pas qu'on laisse entrer des criminels ! Je veux voir mon frère !"
    "UN HOMME — Et moi, je veux que mes enfants puissent dormir !"
    "Le journaliste essaie de reprendre la parole. Les deux continuent de se répondre."
    think "Même à des kilomètres d'ici, ils n'arrivent pas à terminer une phrase sans se disputer."
    think "Je pourrais presque entendre Ryn et Sael à leur place. Ça ne me fait pas rire."
    "La caméra recule. Des dizaines de personnes attendent en silence derrière la ligne."
    think "Personne ne s'avance. Tout le monde connaît le prix d'un pas de trop."
    return

label _6_0_1_TRANSITION_CONCLAVE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ current_period = "Après-midi"

    think "À l'approche du vote, je retrouve Elen et Tomas dans le dortoir."
    think "Tous les deux fixent leur tablette. Je reconnais l'expression de gens qui ne sont même plus d'accord avec une horloge."
    $ showGroup([("elen", "neutre", 0.25), ("tomas", "inquiet", 0.65), ("noam", "neutre", 0.85)])
    tomas inquiet "Euh... dites-moi que je ne deviens pas fou. Mon message dit maintenant treize heures cinquante."
    elen surpris "Quoi ? La mienne affiche toujours quatorze heures !"
    elen inquiet "On peut même plus se mettre d'accord sur l'heure ?!"
    noam inquiet "On va y aller. Je préfère arriver trop tôt que découvrir que Kami nous a fait voter sans nous."
    play sound "sfx/glitch_light.mp3"
    "Les lumières s'éteignent."
    "Une seconde plus tard, le couloir retrouve ses couleurs. L'écran mural, lui, montre un sourire de Kami parfaitement immobile."
    think "Je déteste déjà ce sourire. Quand il ne bouge pas, c'est encore pire."
    elen inquiet "Ça... c'est censé nous rassurer ?"
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes petits représentants ! Vous êtes déjà en route. Quelle efficacité ! Nous pouvons commencer légèrement... plus tôt."
    noam inquiet "Kami, pourquoi avancer l'heure ? On a reçu des messages différents."
    pause 0.4
    kami "L'horaire a été... ajusté."
    kami "Tout est normal. Rendez-vous au Conclave."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et venez tous ensemble ! Ce serait plus facile pour... pour..."
    kami "Ce serait plus facile. Voilà."
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    "Elen baisse les yeux. Sur sa tablette aussi, quatorze heures vient de devenir treize heures cinquante."
    elen inquiet "Je n'aime vraiment pas ça. D'habitude, elle nous fait peur exprès."
    elen inquiet "Là... elle a l'air de ne même pas comprendre ce qui lui arrive."
    tomas hesitation "Ça pourrait être juste un problème de transmission. Les appareils peuvent se désynchroniser, non ?"
    elen inquiet "Tomas, tu dis ça pour nous rassurer ou pour te rassurer toi-même ?"
    tomas hesitation "Les deux, je crois."
    noam neutre "Même si c'est une simple panne, je n'ai jamais vu Kami perdre le contrôle d'une annonce aussi longtemps."
    "Nous rejoignons les autres. Sael et Ryn arrivent ensemble, sans échanger un mot."
    think "Ils ne se sont pas disputés. Je suppose qu'on peut appeler ça une bonne nouvelle, jusqu'à preuve du contraire."

    jump _6_0_1_CONCLAVE_START

label _6_0_1_CONCLAVE_START:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_267
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.5

    "Julian est déjà en grande conversation avec Tomas. C'est presque rassurant : il semble lui parler, pas le coincer."
    think "À l'autre bout de la table, Ryn fixe Sael avec une intensité qui ne présage absolument rien de bon."
    $ showGroup([("ryn", "colere", 0.20), ("iris", "fatigue", 0.48), ("sael", "neutre", 0.78)])
    ryn colere "Bon. Avant qu'on vote, j'aimerais qu'on m'explique encore une fois pourquoi des familles devraient rester derrière ces foutues barrières !"
    sael determine "Je t'ai répondu hier. Tu n'étais pas d'accord, mais ça ne signifie pas que tu ne m'as pas entendue."
    ryn colere "JE T'AI ENTENDUE ! Mais il y a des gens qui meurent MAINTENANT ! Pas il y a dix ans, pas dans tes souvenirs !"
    iris desaccord "Ryn, arrête de lui faire dire qu'elle se fiche des morts. Tu sais très bien que c'est faux."
    ryn colere "Alors pourquoi elle peut nous faire perdre le vote à elle toute seule ?!"
    noam inquiet "Parce qu'on nous demande de tout ouvrir sans prévoir ce qu'on fera ensuite. On en revient toujours au même problème."
    sael neutre "Et je refuse qu'on transforme cette incertitude en pari sur la vie de mon village."
    "Ryn s'apprête à répliquer. Le grand écran s'allume avant qu'il puisse reprendre son souffle."
    think "Kami vient peut-être de nous sauver d'un deuxième round. C'est la première fois que j'envisage de la remercier."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Tout le monde est là ? Merveilleux ! Place au deuxième vote de l'histoire du Conclave : la libre circulation entre les districts !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et je vois que vous avez déjà commencé à vous détester ! Quelle efficacité ! J'en attendais presque moins de vous."
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_debate_low.mp3" fadein 1.0

    $ showGroup([
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("iris", "desaccord"),
        ("mara", "agace"),
        ("lysa", "blase"),
        ("elen", "inquiet"),
        ("nyra", "raison"),
    ])
    elen inquiet "Moi... j'aimerais que les gens puissent revoir leurs proches sans risquer leur vie."
    elen inquiet "C'est vraiment impossible de contrôler les passages sans laisser Kami tirer sur ceux qui approchent ?"
    mara agace "Bien sûr qu'on pourrait imaginer autre chose. Mais ce n'est pas ce qu'on vote."
    mara doute "Le texte dit « ouvrir ». Pas « réfléchir à un système de contrôle ». Et c'est une sacrée différence."
    ryn colere "À Limen, ça fait des années qu'on regarde mourir des gens devant des passages qu'on surveille nous-mêmes !"
    ryn colere "Vous voulez qu'on leur dise quoi ? « Encore un peu de patience, on cherche une formulation élégante » ?!"
    kael inquiet "Même si tout le monde veut traverser pacifiquement, le réseau de transport n'est pas prêt."
    kael reflechit "Les contrôles, les convois, les points de passage... On ne remet pas tout ça en route avec un bouton."
    lysa blase "Évidemment qu'il manque des détails. Il manquera toujours des détails."
    lysa reflechit "La vraie question, c'est combien de temps on accepte de garder les gens enfermés en attendant un plan sans défaut."
    nyra reflechit "Attendez. Vous êtes presque tous d'accord pour dire que les sanctions sont insupportables."
    nyra raison "Sael, si on ajoutait des contrôles aux passages, ce serait suffisant pour toi ?"
    sael determine "Non."
    sael mefiant "Même avec des contrôles, la réouverture rendrait le retour des groupes armés plus facile."
    sael determine "J'ai passé des années à faire en sorte que mon village puisse enfin dormir. Je ne vais pas l'exposer à nouveau."
    ryn colere "ALORS ON FAIT QUOI ?! On attend que toutes les familles soient mortes pour ne plus avoir de problème de frontières ?!"
    sael colere "ARRÊTE ! Je ne suis pas Kami ! Je n'ai écrit aucun de ses Commandements !"
    sael colere "Et pourtant, à t'entendre, chaque mort à la frontière serait déjà de ma faute !"
    "Iris frappe la table du plat de la main."
    iris colere "Vous pouvez vous parler SANS vous hurler dessus deux secondes ?!"
    "Une voix sort des haut-parleurs avant que quelqu'un réponde."
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Vos arguments sont tous... tous très..."
    kami "Il faudrait peut-être que vous..."
    pause 0.7
    "Le visage de Kami se fige."
    "Un grésillement coupe le silence."
    think "La phrase ne vient pas. Pour la première fois, elle a l'air incapable de trouver une méchanceté à ajouter."
    kami "Continuez. Poursuivez... poursuivez le débat. Je vous écoute."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    iris inquiet "Non. Désolée, mais là ça suffit."
    iris inquiet "Kami, qu'est-ce qui t'arrive ? Et ne nous fais pas ton numéro habituel."
    noam neutre "Kami ? Tu nous entends correctement ?"
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "ÉVIDEMMENT que je vous entends ! Douze représentants, une salle, mes caméras partout ! Je ne suis pas sourde !"
    "Le silence s'étire. Sa bouche reste ouverte une seconde de trop."
    think "Personne ne plaisante. Même Mara fixe l'écran sans sourire."
    kami "Vous n'avez pas terminé."
    kami "Il faut... il faut continuer."
    mara mefiant "Pourquoi « il faut » ?"
    mara colere "Qu'est-ce qu'on doit continuer exactement ? Notre débat, ou un spectacle que tu refuses d'arrêter ?"
    kami "Le débat doit..."
    kami "Il faut que vous... continuiez. Oui. Continuez."
    play sound "sfx/glitch_medium.mp3"
    "« Continuez. Continuez. Conti... »"
    "L'image se dédouble. La dernière syllabe se répète comme un disque rayé."
    think "Quelque chose ne va pas. Et cette fois, je ne crois plus à une mise en scène."
    elias inquiet "Kael ! C'est pas les haut-parleurs ! Le son décroche en même temps que l'image !"
    kael inquiet "Je vois. Et ses messages arrivent avec du retard sur ma tablette."
    kael reflechit "C'est comme si la transmission entière perdait des morceaux."
    nyra reflechit "Kami, est-ce qu'on doit suspendre la séance jusqu'au rétablissement des systèmes ?"
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    kami "NON !"
    kami "LE DÉBAT CONTINUE !"
    pause 0.3
    "Le son explose dans les haut-parleurs. Tomas se recule brutalement."
    tomas peur "AH ! Bon sang, on peut baisser le volume ?!"
    tomas inquiet "On ne t'empêche pas de faire une pause ! Tu peux même en prendre une longue, si ça t'aide !"
    kami "Je n'ai pas... besoin de... de..."
    play sound "sfx/glitch_heavy.mp3"
    "L'écran s'éteint."
    "Une seconde plus tard, Kami réapparaît. Ses lèvres bougent après que les mots ont déjà été prononcés."
    think "Je commence à regretter l'époque où son plus gros problème était son humour."
    think "On dirait qu'elle ne supporte pas l'idée qu'on arrête la séance."
    think "Pourtant, c'est elle qui n'arrive plus à la tenir."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    iris inquiet "Vous l'avez vue ? Elle n'arrivait même plus à synchroniser sa propre voix !"
    ryn colere "Alors on ARRÊTE ! On ne va pas voter pendant que l'IA qui gère le monde part en morceaux !"
    elen inquiet "Mais... si elle s'arrête vraiment, qu'est-ce qu'il se passe sur Terre ?"
    elen peur "Les rations ? Les frontières ? Les sanctions ? Tout ça dépend d'elle !"
    mara mefiant "Et elle nous dit de continuer à voter comme si tout était normal."
    mara agace "Pour une fois que j'aimerais qu'elle nous explique quelque chose, elle se met à répéter trois mots."
    "Les voix éclatent de tous les côtés."
    elias inquiet "Je peux vérifier les écrans, mais pas son réseau !"
    ryn colere "Alors on fait quoi ?!"
    nyra raison "Personne ne touche aux consoles avant qu'on sache ce qui se passe !"
    "Les lumières clignotent. D'un coup, tout le monde se tait."

    jump _6_0_1_SIGNAL_INSTABLE

# Durée : ~1m30


label _6_0_1_SIGNAL_INSTABLE:

    play sound "sfx/glitch_heavy.mp3"
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 0.5
    kami "J'ai besoin que vous restiez... que vous restiez ici. Ne quittez pas la salle."
    "Une alarme discrète se déclenche sur les haut-parleurs. L'écran principal affiche pendant une seconde un message de connexion interrompue."
    elias inquiet "C'est pas juste un souci avec les enceintes. Elle perd la communication avec les consoles, là."
    kael inquiet "Je le vois aussi sur ma tablette. Elle essaie de se reconnecter, mais le signal saute."
    iris inquiet "C'est censé être possible, ça ?"
    kael reflechit "Je sais pas. Et je préfère pas te répondre au hasard."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "La séance doit continuer normalement. Je vais... régler cela."
    "Sa voix s'interrompt. Sur les consoles des représentants, les notifications disparaissent brièvement avant de revenir."
    noam inquiet "On devrait peut-être attendre que tout fonctionne avant de voter."
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Non. Attendre n'est pas... nécessaire."
    play sound "sfx/glitch_loop.mp3"
    "Un grésillement plus fort résonne dans la salle. Je protège mes oreilles et je vois Elias se pencher vers le terminal devant lui."
    call j601_play_signal_instable from _call_j601_play_signal_instable
    stop sound fadeout 0.5

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_debate_low.mp3" fadein 1.0
    "Le bruit cesse d'un coup. Je regarde les écrans : certains affichent de nouveau nos dossiers, mais d'autres sont encore bloqués."
    elen inquiet "C'est bon ? On dirait qu'elle est revenue."
    kael inquiet "Pas complètement. Il y a des connexions qui répondent encore avec du retard."
    ryn colere "Et elle veut qu'on vote avec ça ? Elle se fout de nous ?"
    nyra reflechit "Personne n'a intérêt à se précipiter. Même si le vote doit finir par avoir lieu, il faut au moins que le système fonctionne."
    "Kami réapparaît sur l'écran central. Son visage est parfaitement immobile, alors que sa voix arrive avec une seconde de décalage."
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je suis toujours là. Les systèmes du Conclave sont... disponibles. Nous pouvons poursuivre."
    mara mefiant "C'est pas vrai, on vient de voir des écrans s'éteindre !"
    kami "Ils sont disponibles."
    "Personne ne répond. Même ceux qui veulent en finir ne semblent plus très pressés."

    jump _6_0_1_FRACTURE_QTE

label _6_0_1_FRACTURE_QTE:

    "Un nouveau message apparaît devant moi, mais les caractères changent avant que je puisse le lire. Plusieurs représentants se penchent sur leur tablette."
    noam inquiet "Attendez, il y a un problème avec l'affichage des votes. Chez vous aussi ?"
    tomas inquiet "Oui ! Enfin, je crois. J'avais le texte de l'amendement et maintenant ça me demande de confirmer autre chose."
    kael inquiet "Touchez à rien, je vais regarder si c'est un affichage temporaire."
    play sound "sfx/glitch_medium.mp3"
    "L'écran du Conclave affiche des données qui se mélangent avant de revenir à la proposition initiale."
    call j601_play_fracture from _call_j601_play_fracture
    $ j601_fracture_result = _return

    scene bg_conclave at adaptive_fullscreen with dissolve
    "Les écrans reviennent enfin sur le texte concernant les frontières. La proposition semble inchangée, mais plusieurs représentants gardent leur tablette à distance."
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Merci de votre patience. Nous allons maintenant passer au vote."
    elen inquiet "Mais attends, tu vas bien ? On peut pas juste faire comme si rien ne s'était passé !"
    kami "Les procédures ont été... rétablies. Vous pouvez voter."
    iris colere "Et si tu te trompes en comptant nos voix ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le système de dépouillement est distinct de l'affichage des débats. Il est opérationnel."
    kael reflechit "Je peux pas vérifier ça depuis ma tablette, mais on n'a pas beaucoup d'autres moyens de procéder."
    mara colere "C'est quand même magnifique. On va voter sur le fonctionnement du monde alors que celle qui le dirige arrive à peine à terminer ses phrases."
    sael determine "Je ne fais pas confiance à ce qui vient de se passer, mais je n'ai pas changé d'avis. Je voterai contre l'ouverture des frontières."
    ryn colere "On le sait, Sael. T'as pas besoin de me le rappeler à chaque fois."
    sael mefiant "Je m'adresse aux autres aussi, pas seulement à toi."
    noam inquiet "Je veux juste être sûr qu'on vote bien sur la même proposition. Kami, tu peux nous la répéter une dernière fois ?"
    pause 0.3
    kami "Autoriser la libre circulation des personnes entre les districts. Aucune autre modification n'est prévue."
    lysa blase "Bon, au moins on sait ce qu'on nous demande. Je suis pas rassurée pour autant."
    "Un voyant s'allume sur les tablettes. Le vote est officiellement ouvert."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 0.7
    jump _6_0_1_VOTE

label j601_sael_vote_animation:

    window hide
    show expression Solid("#02050cdd") as j601_sael_vote_backdrop zorder 250
    with Dissolve(0.12)

    show expression Solid("#E84A5F", xsize=4, ysize=1080) as j601_sael_vote_left zorder 252:
        xpos 596
    show expression Solid("#E84A5F", xsize=4, ysize=1080) as j601_sael_vote_right zorder 252:
        xpos 1320

    show expression "images/background/interact/animation/sael_contre/sael_contre1.png" as j601_sael_vote_frame zorder 251 at j601_sael_vote_strip
    with moveinright
    pause 0.55

    show expression "images/background/interact/animation/sael_contre/sael_contre2.png" as j601_sael_vote_frame zorder 251 at j601_sael_vote_strip
    with Dissolve(0.12)
    pause 0.42

    play sound "audio/sfx_vote_contre.wav"
    show expression "images/background/interact/animation/sael_contre/sael_contre3.png" as j601_sael_vote_frame zorder 251 at j601_sael_vote_strip
    with hpunch
    pause 0.85

    hide j601_sael_vote_frame
    hide j601_sael_vote_left
    hide j601_sael_vote_right
    hide j601_sael_vote_backdrop
    with Dissolve(0.18)
    window auto
    return

label _6_0_1_VOTE:

    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    $ _vote_result = renpy.call_screen("vote_screen")

    # Résultats imposés pour le vote J6_0_1
    # Pour : Julian, Tomas + éventuellement Noam
    # Abstention : Elias + éventuellement Noam
    # Contre : tous les autres + éventuellement Noam

    $ player_vote = vote_phase3_player_choice if vote_phase3_player_choice in ("pour", "contre", "abstention") else "abstention"

    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    $ vote_phase3_results = [
        ("Julian", "pour"),
        ("Tomas", "pour"),
        ("Elias", "abstention"),
        ("Ryn", "contre"),
        ("Nyra", "contre"),
        ("Kael", "contre"),
        ("Mara", "contre"),
        ("Lysa", "contre"),
        ("Iris", "contre"),
        ("Elen", "contre"),
        ("Sael", "contre"),
        ("Noam", player_vote),
    ]

    $ renpy.random.shuffle(vote_phase3_results)

    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    pause 0.8

    $ amendement_passe = False

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    "Le résultat s'affiche. Les votes contre sont nettement majoritaires, et l'amendement est rejeté. Je reconnais le nom de Sael dans le dépouillement."
    if player_vote == "pour":
        think "J'ai voté pour malgré les risques, parce que je voulais qu'on donne enfin une chance aux familles séparées. Le résultat ne change rien à ce que j'ai choisi."
    elif player_vote == "contre":
        think "J'ai aussi voté contre. Je n'ai pas réussi à me convaincre qu'une ouverture immédiate serait sans danger, même si je déteste ce que les frontières font subir aux gens."
    else:
        think "Je me suis abstenu. Avec toutes ces incertitudes, je n'ai pas réussi à trancher, mais je sais que mon abstention ne rendra service à personne aujourd'hui."
    $ hideGroup()
    call j601_sael_vote_animation from _call_j601_sael_vote_animation
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    think "Sael a tenu parole. Elle n'avait jamais dit qu'elle hésitait, mais voir son vote affiché rend la situation plus difficile pour Ryn."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Résultat du vote : absence d'unanimité. La proposition d'ouverture des frontières est rejetée."
    $ interject("REJETÉ", color="#FF4D6D")
    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Les restrictions actuelles restent donc en vigueur. Nous nous retrouverons pour le prochain vote."
    "Sa voix paraît presque normale, mais son image disparaît avant la fin de la transition habituelle."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "colere"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("mara", "doute"),
        ("tomas", "inquiet"),
        ("julian", "decu"),
        ("elias", "fatigue"),
        ("lysa", "fatigue"),
    ])
    ryn colere "C'est donc fini. Tous ceux qui attendaient devant les frontières vont rentrer chez eux, et nous, on va faire quoi ? On va encore se dire qu'on a fait de notre mieux ?"
    sael triste "Je sais que tu es en colère. Je ne te demande pas d'être d'accord avec moi."
    ryn colere "Bah heureusement, parce que j'y arriverai pas !"
    mara agace "Ryn, elle avait annoncé sa position avant le vote. Tu pouvais pas découvrir ça aujourd'hui."
    ryn triste "Je sais, Mara. Mais ça m'empêche pas d'avoir envie de hurler."
    tomas inquiet "Moi, ce qui me fait peur, c'est qu'on ait voté alors que Kami avait un problème. Comment on sait que tout a été enregistré correctement ?"
    kael reflechit "Le dépouillement a affiché douze votes, et les vérifications de base semblent correctes. Ça ne nous dit pas pourquoi Kami a perdu le signal."
    iris inquiet "Donc on vient de constater que la seule chose qui contrôle nos vies peut tomber en panne, et on a juste le droit de rentrer dans nos chambres ?"
    elias fatigue "Je vais demander à Kael si on peut vérifier quelque chose sur les systèmes de la station. Je sais pas si on aura accès à grand-chose, mais au moins on peut essayer."
    julian decu "Je voulais une victoire pour le Conclave. À la place, on a deux votes rejetés et une IA qui arrive à peine à tenir une réunion."
    lysa blase "Pour une fois, t'as résumé la situation sans nous expliquer pourquoi tu aurais fait mieux."
    julian taquin "Profites-en, ça risque de pas se reproduire."
    "Quelques personnes sourient malgré elles. Ryn ne réagit pas et quitte la salle sans saluer personne."
    think "Le vote est terminé, mais les interruptions de Kami préoccupent presque autant le groupe que le résultat. Personne ne sait vraiment ce qui a provoqué ces problèmes."

    jump _6_0_1_FIN_JOURNEE

# Durée : ~3m00

label _6_0_1_FIN_JOURNEE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_274
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ showGroup([
        ("lysa", "fatigue"),
        ("mara", "doute"),
        ("elen", "inquiet"),
        ("kael", "fatigue"),
        ("iris", "fatigue"),
        ("tomas", "inquiet"),
    ])
    elen inquiet "Vous croyez qu'elle va recommencer à parler normalement demain ? Parce que je dois dire que ça m'a vraiment fait peur."
    iris reflechit "J'aimerais bien savoir ce qui lui arrive. Elle est insupportable d'habitude, mais au moins on sait à quoi s'attendre."
    mara agace "Moi, je veux surtout savoir si on peut faire quelque chose si ses systèmes tombent en panne. On va pas attendre tranquillement qu'elle nous annonce une catastrophe."
    kael reflechit "Je vais vérifier les messages techniques qu'on a reçus. Et je vais regarder ce qui s'est passé dans l'observatoire hier, même si je doute que les deux soient liés."
    lysa blase "Tu penses vraiment qu'elle va te laisser accéder à ses systèmes ?"
    kael calme "Probablement pas. Mais je peux au moins examiner ceux de la station."
    tomas inquiet "Si vous trouvez quelque chose, vous nous le direz, hein ?"
    iris sourire "Évidemment, Tomas. On va pas garder ça pour organiser une petite surprise."
    "Les autres se séparent peu à peu. Elen propose à ceux qui le souhaitent de passer à la salle de repos, mais je préfère rentrer."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_275
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "decu", 0.25), ("elias", "fatigue", 0.55), ("ryn", "colere", 0.85)])
    julian decu "Ryn, je sais que t'es déçu. Mais tu pouvais pas vraiment espérer que Sael change d'avis au dernier moment."
    ryn colere "Julian, pas maintenant. S'il te plaît."
    julian neutre "Je voulais juste..."
    elias fatigue "Laisse-le, Julian. On a tous eu une journée assez compliquée."
    julian decu "Bon, d'accord. Je vais pas insister."
    "Ryn repart vers sa chambre. Julian hésite à le suivre, puis renonce. Elias me fait un signe avant de rejoindre Kael."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_276
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    "Je m'assieds sur mon lit en repensant à ce qu'on a vu aujourd'hui."
    think "Kami a perdu le contrôle de ses transmissions pendant plusieurs minutes. Elle dit que tout fonctionne normalement, mais je ne l'ai jamais vue aussi pressée de terminer une réunion."
    think "Et puis il y a eu cet incident dans la salle d'observation hier. Je ne sais pas si ça a un rapport, et ce serait absurde d'en être certain sans aucune preuve."
    "Je consulte une dernière fois ma tablette. Le résultat du vote s'affiche toujours, accompagné d'un message confirmant que les frontières restent fermées."
    think "Je pense aux familles qui attendaient devant les postes de contrôle. Demain, elles sauront que rien n'a changé."
    "Je pose la tablette, éteins la lumière et me couche."
    pause 0.5
    play sound "sfx/glitch_light.mp3"
    "L'écran mural s'allume une seconde. Je me redresse, mais il est déjà éteint."
    think "Il n'y a eu ni annonce ni message. Peut-être que ce n'était qu'un problème d'affichage, mais je n'arrive pas à me rendormir tout de suite."
    $ blink()
    "Je finis par fermer les yeux."

    $ kami_grant_chapter_2_reward()

    call show_chapter_title("Fin du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_3

    pause 1.0

    #jump patreon_ending

    call end_day("7", sleeping=True) from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE

# total : 8m
# Total jour 0-6 : 1h49
