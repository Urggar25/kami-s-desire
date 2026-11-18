# 6_0_1.rpy
# Jour 6 - Branche statu quo post-accident café
# Style THL - version dialoguée, rythmée

default j601_border_news_seen = False
default j601_signal_stabilized = False
default j601_fracture_trace_saved = False

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
    "Je cherche ma tablette dans les draps avant de comprendre qu'elle est sous mon coude."
    "Le rappel du vote s'affiche sur ma tablette : quatorze heures, libre circulation entre les districts."
    think "La marque d'oreiller sur ma joue constitue pour l'instant ma seule contribution au débat."
    "Hier, Sael m'a laissé entrer dans sa chambre. J'ai surtout appris que comprendre quelqu'un ne suffit pas à le faire changer d'avis."
    "Je relis l'horaire. Il reste quelques heures avant que Ryn et elle ne se retrouvent à la même table."

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
    "Je tends l'oreille. Le son vient-il de se couper ?"
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

    iris colere "Non, mais c'est quoi, ce pain ?! Il faudrait une autorisation de port d'arme pour le couper !"
    mara taquin "Mâche doucement. Si tu te casses une dent, on va devoir organiser un vote pour la remplacer."
    elen rire "Mara !"
    iris blase "Vous rigolerez moins quand je vous servirai ça en briques de construction."
    elias fatigue "Est-ce que vous pourriez ne pas crier ? J'ai mal dormi."
    lysa blase "Une ambiance familiale. Il ne manque qu'une dispute sur l'héritage."
    elen inquiet "NOAM ! Dis-moi que tu as entendu ! Kami a fait... un truc !"
    noam surpris "Un truc ? Ça réduit peu les possibilités."
    elen inquiet "Elle s'est arrêtée au milieu d'une phrase ! Toute seule !"
    noam reflechit "J'ai vu. J'ai attendu la chute de sa blague, mais il n'y en avait pas."
    mara taquin "Un truc ? Écoutez-la, notre enquêteuse. Nous voilà bien avancés."
    elen colere "Je ne suis pas une enquêteuse !"
    mara sourire "Je n'ai jamais dit que tu étais une bonne enquêteuse."
    elias fatigue "Pareil dans le dortoir. Et sur ma tablette."
    elias inquiet "Pour une fois que ce n'est pas mon matériel qui plante, je sais même pas si je dois être soulagé."
    mara taquin "Elle a peut-être découvert qu'on pouvait réfléchir AVANT d'ouvrir la bouche."
    mara sourire "Une révolution technologique."
    lysa blase "Une IA qui hésite. Dramatique. Si elle commence à oublier les prénoms, je propose qu'on l'envoie à la retraite."
    iris colere "Je n'ai jamais cru dire ça, mais est-ce que vous pourriez prendre Kami au sérieux DEUX SECONDES ?!"
    lysa taquin "Tu viens vraiment de défendre Kami ? Je veux une capture d'écran."
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
    mara taquin "Je propose qu'on mette un périmètre de sécurité autour d'Elias. Deux mètres pour les cafés. Dix pour les consoles."
    elias reflechit "Je m'accuse pas !"
    elias gene "Enfin, j'essaie de ne pas m'accuser avant d'avoir les résultats de Kael."
    "Goumi arrive avec les plateaux. Elias pousse immédiatement sa tasse vers le centre de la table."
    think "Sa tasse a désormais une zone de sécurité personnelle."
    mara taquin "Oh ! Regardez ! Elias applique les règles de sécurité du café !"
    elias sourire "Exactement ! Plus de boisson près des machines, des câbles ou des objets coûteux !"
    mara taquin "Il te reste l'option de boire debout dans le couloir."
    elias gene "C'est... pas idiot."
    mara rire "IL Y RÉFLÉCHIT VRAIMENT !"
    iris blase "Arrêtez de l'encourager. On va finir avec une notice de sécurité sur les gobelets."
    elias colere "C'EST MOI QUI AI FAIT TOMBER LA TASSE, PAS LE GOBELET !"
    lysa blase "Pardon. La commission d'enquête va rouvrir son dossier."
    lysa reflechit "Bon, avant qu'on rédige un code de la sécurité des boissons : quelqu'un a parlé à Sael ?"
    sael determine "Je suis juste en face de toi, Lysa."
    sael neutre "Tu peux encore t'adresser directement à moi. C'est autorisé."
    lysa blase "Je sais. Je voulais savoir si quelqu'un avait réussi à avoir une discussion, pas une déclaration de vote."
    elen sourire "On pourrait peut-être manger ensemble, juste une fois, sans se disputer ?"
    mara taquin "C'est adorable. Et après, on se fait tous un câlin ?"
    elen colere "Je proposais juste un petit-déjeuner !"
    mara sourire "C'est encore plus ambitieux qu'un amendement."
    sael neutre "Noam est venu me voir hier. On a parlé."
    sael determine "Et non, je n'ai pas changé d'avis."
    iris fatigue "Personne ne te demande de te justifier à chaque bouchée."
    sael neutre "Alors pourquoi tout le monde me regarde ?"
    "Elias plonge soudain le nez dans son assiette. Mara, elle, ne baisse pas les yeux."
    elen triste "J'ai vu des enfants attendre aux frontières à la télévision... Ils espèrent vraiment pouvoir revoir leurs proches."
    sael triste "Je le sais, Elen."
    sael determine "Et je ne pourrai pas regarder les miens en face si j'ouvre notre village à ceux qui nous attaquaient. Je suis désolée."
    mara agace "On n'arrive déjà pas à assurer les livraisons normales. Mais oui, ouvrons toutes les routes d'un coup. Qu'est-ce qui pourrait mal se passer ?"
    elen determine "On pourrait aussi arrêter de parler de ces familles comme d'une catastrophe à transporter !"
    mara neutre "Je les ai vues, Elen."
    "Elen attend une plaisanterie. Mara n'en ajoute pas."
    elias gene "Euh... quelqu'un veut ma ration ? J'ai plus faim."
    lysa blase "Magnifique tentative de diversion, Elias."
    elias fatigue "C'était pas une diversion."
    noam neutre "Il reste quelques heures. On pourrait au moins finir de manger avant de recommencer la guerre des frontières."
    iris sourire "Merci. J'aimerais avaler une bouchée sans qu'on m'annonce une crise internationale entre le pain et le café."
    "Elen se penche sur la tasse d'Elias."
    elen taquin "Tu sais que Goumi peut peut-être te servir dans un gobelet fermé ?"
    elias sourire "Tu veux rire, mais j'y ai pensé."
    mara blase "Je savais qu'il y aurait un débat plus idiot que celui sur les frontières."
    "Elen attrape discrètement le gobelet d'Elias, visse dessus le couvercle d'une petite boîte et le lui rend comme un trophée."
    elen joie "Voilà. Le premier dispositif anti-Elias de l'histoire !"
    elias sourire "Attends... mais ça marche !"
    mara rire "Ça y est. Notre civilisation a atteint son apogée."
    "Sael laisse échapper un rire bref. Ryn n'est même pas là pour le lui reprocher."
    think "Puis l'écran de la cafétéria change de programme. Les conversations ralentissent d'elles-mêmes."
    "Une carte de Limen apparaît. Le présentateur annonce un reportage sur les familles rassemblées près des postes de contrôle."
    call _6_0_1_TV_FRONTIERES from _call_6_0_1_TV_FRONTIERES_matinale
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "Ceux qui attendent derrière les barrières ont déjà fait leur choix."
    think "À quelques sièges de moi, Sael continue de fixer son assiette."
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
    "UNE FEMME — Il déteste le thé que je lui apporte à chaque anniversaire. J'en ai quand même gardé une boîte pour lui."
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
    elen taquin "Ton horloge aussi est en avance sur ton cerveau ?"
    tomas gene "Non, justement. Enfin, je crois que non."
    noam taquin "Tomas, tu as déjà regardé le mauvais jour sur un calendrier."
    tomas inquiet "Une fois ! Et il était mal imprimé !"
    elen rire "Tu avais quand même essayé de corriger le calendrier au stylo."
    elen surpris "Quoi ? La mienne affiche toujours quatorze heures !"
    elen inquiet "On peut même plus se mettre d'accord sur l'heure ?!"
    noam inquiet "On va y aller. Je préfère arriver trop tôt que découvrir que Kami nous a fait voter sans nous."
    play sound "audio/sfx_glitch.mp3"
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
    play music "music/bgm_low_tension.mp3" fadein 1.5
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_6_0_1

    "Julian est debout derrière une chaise. Il attend que quelqu'un le regarde avant de prendre la parole."
    julian sourire "Mesdames, messieurs, je propose de nous écouter jusqu'au bout, dans un esprit de..."
    iris blase "Assieds-toi, Julian."
    julian hesitation "Mais je n'ai même pas terminé !"
    mara taquin "On t'écoutait. C'est justement pour ça qu'on t'arrête."
    julian taquin "Je vois. Mon talent oratoire dérange déjà les puissants."
    lysa blase "Et quelques personnes ordinaires, accessoirement."
    "Julian tire sa chaise avec un bruit exagéré. Personne ne lui offre les applaudissements espérés."
    think "À l'autre bout de la table, Ryn fixe Sael avec une intensité qui ne présage absolument rien de bon."
    $ showGroup([("ryn", "colere", 0.20), ("iris", "fatigue", 0.48), ("sael", "neutre", 0.78)])
    ryn colere "Une question, Sael. Une seule. Si on vote non, tu diras quoi aux gens qui attendent devant les barrières ?"
    sael determine "La vérité. Que je n'accepterai pas de faire courir ce risque à mon village."
    ryn colere "Et tu penses que ça va leur suffire ?!"
    sael mefiant "Non. Mais je préfère une vérité qu'ils détesteront à une promesse que je ne peux pas tenir."
    elen inquiet "Ryn, laisse-moi..."
    ryn colere "PAS MAINTENANT !"
    elen colere "J'allais dire que je suis d'accord avec toi !"
    "Ryn reste bouche ouverte. Elen en profite avant qu'il retrouve sa voix."
    elen determine "Je veux qu'ils puissent passer. Mais je ne sais pas non plus comment protéger les villages."
    kael reflechit "Et je ne peux pas vous promettre que les convois et les points de contrôle seront prêts demain."
    ryn colere "Donc on ne fait rien ? Voilà notre grand plan ?!"
    noam inquiet "Non. Mais le texte nous demande de prendre une décision sur ce qu'on fait aujourd'hui."
    "Ryn serre les poings. Cette fois, il ne trouve pas immédiatement de réplique."
    "Le grand écran s'allume."
    think "Kami vient peut-être de nous sauver d'un deuxième round. C'est la première fois que j'envisage de la remercier."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Tout le monde est là ? Merveilleux ! Place au deuxième vote de l'histoire du Conclave : la libre circulation entre les districts !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et je vois que vous avez déjà commencé à vous détester ! Quelle efficacité ! J'en attendais presque moins de vous."
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

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
    mara agace "On peut l'espérer. Mais entre un passage ouvert et un passage sûr, il y a quelques détails."
    mara doute "Et ce sont précisément les détails que le texte ne contient pas."
    tomas inquiet "J'aurais peut-être dû demander la définition exacte d'« ouvrir »..."
    iris colere "Tomas, ne commence pas une bataille de dictionnaire !"
    tomas gene "Je... je faisais simplement remarquer..."
    mara taquin "Laisse, Tomas. On sait que tu as un dictionnaire affectif."
    noam neutre "On peut éviter de se battre aussi sur les guillemets ?"
    lysa blase "Trop tard. Le débat vient de perdre toute dignité."
    ryn colere "À Limen, ça fait des années qu'on regarde mourir des gens devant des passages qu'on surveille nous-mêmes !"
    ryn colere "Et pendant qu'on parle logistique, eux, ils continuent d'attendre !"
    kael inquiet "Je le sais. Mais si tu veux que je t'organise des convois, il me faut autre chose qu'une date et de la bonne volonté."
    lysa blase "Évidemment qu'il manque des détails. Il manquera toujours des détails."
    lysa reflechit "La vraie question, c'est combien de temps on accepte de garder les gens enfermés en attendant un plan sans défaut."
    nyra reflechit "Attendez. Le scrutin ne porte pas sur un dispositif de contrôle, mais sur une autorisation générale."
    nyra raison "Sael, même si nous ajoutions des garanties, accepterais-tu de les étudier ?"
    sael neutre "Je les étudierais. Ça ne veut pas dire que j'accepterais."
    ryn colere "Et moi, je les attendrais pendant combien d'années, tes garanties ?!"
    sael mefiant "Tu m'as demandé hier pourquoi je refusais. Je t'ai répondu."
    ryn colere "Tu m'as parlé de ton village. Je te parle de tous ceux qui n'ont plus de village où rentrer !"
    sael colere "Et tu voudrais que je me comporte comme si le mien ne comptait pas ?!"
    ryn colere "Je n'ai pas dit ça !"
    sael colere "C'est ce que j'entends, moi !"
    "Ryn ouvre la bouche, puis la referme. Pendant une seconde, il paraît comprendre la formule qu'elle vient de lui renvoyer."
    "Iris frappe la table du plat de la main."
    iris colere "Vous pouvez vous parler SANS vous hurler dessus deux secondes ?!"
    "Une voix sort des haut-parleurs avant que quelqu'un réponde."
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Vos arguments sont tous... tous très..."
    pause 0.7
    "L'image s'immobilise, mais aucun son ne grésille. Je tends l'oreille."
    kami "Continuez. Poursuivez le débat. Je vous écoute."
    think "Aucune pique sur Ryn, aucune remarque sur Sael. C'est presque plus inquiétant que son silence."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0

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
    kami "Il faut continuer."
    julian hesitation "Je ne voudrais pas être désagréable, mais je crois que notre présidente de séance est en train de..."
    iris colere "NE FINIS PAS CETTE PHRASE !"
    julian peur "Très bien ! Je ne la finis pas !"
    mara mefiant "Pourquoi « il faut » ?"
    mara colere "Ce vote est censé être notre décision, pas un spectacle que tu refuses d'arrêter."
    "Kami ne lui répond pas. Son sourire reste à l'écran alors que Mara attend une riposte."
    iris inquiet "C'est la première fois qu'elle laisse passer une occasion pareille."
    play sound "audio/sfx_glitch.mp3"
    "Un quadrillage traverse l'écran. Pendant un instant, l'heure du scrutin disparaît et revient avec dix minutes d'écart."
    elen peur "Elle vient de changer l'heure ENCORE ?!"
    kael inquiet "Ce n'est plus seulement la voix. Les données de séance ne restent pas synchronisées."
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
    play sound "audio/trailer/trl_glitch_stutter.wav"
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
    mara agace "On s'inquiète pour le scrutin alors que personne ne sait si les portes s'ouvriront demain matin !"
    ryn colere "Je m'en fous des portes !"
    iris colere "TOI, TU T'EN FOUS ! Mais tout le monde n'habite pas dans ta tête !"
    lysa neutre "Pour une fois, on est tous d'accord sur une chose : personne n'a la moindre idée de ce qui nous arrive."
    "Un instant, même Ryn se tait."
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

    play sound "audio/trailer/trl_glitch_stutter.wav"
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 0.5
    kami "Restez... restez dans cette salle."
    kami "J'ai besoin que vous... vous restiez. Ne partez pas."
    "Un bip discret se déclenche. Sur l'écran, une ligne apparaît : « CONNEXION INTERROMPUE »."
    think "Elle disparaît aussitôt. Pas assez vite pour que Kael la manque."
    elias inquiet "Ça y est, j'ai des erreurs de communication partout ! Ça ne vient pas des enceintes !"
    kael inquiet "Je vois les mêmes. Le système tente de se reconnecter, puis perd à nouveau le signal."
    kael reflechit "On a plusieurs appareils indépendants qui décrochent en même temps. Ce n'est pas normal."
    iris inquiet "Attends, Kami est censée contrôler toute la station. Comment elle peut perdre sa propre connexion ?"
    kael reflechit "Je n'en sais rien. Et inventer une explication maintenant nous ferait plus de mal que de bien."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je vais rétablir le canal de la séance."
    "Sur ma tablette, le dossier de vote se ferme sans que j'aie touché l'écran."
    "À sa place apparaît une ligne technique : « SESSION LOCALE — CANAL D'URGENCE »."
    elen peur "HÉ ! MON DOSSIER A DISPARU !"
    lysa blase "Une démocratie qui range les bulletins avant le scrutin. Quel gain de temps."
    noam inquiet "Kami, on doit suspendre la séance !"
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Non."
    pause 0.4
    kami "Restez ici."
    kami "Je vous en prie."
    "Plus personne ne bouge. Elle n'a jamais eu besoin de nous supplier pour nous garder dans une pièce."
    play sound "audio/sfx_static.mp3"
    "Un grésillement traverse la salle. Je plaque mes mains sur mes oreilles."
    "Devant moi, des caractères défilent à toute vitesse."
    elias inquiet "Noam ! Regarde ton écran ! Il y a quelque chose à faire, je crois !"
    call j601_play_signal_instable from _call_j601_play_signal_instable
    $ j601_signal_stabilized = bool(_return)
    stop sound fadeout 0.5

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0
    if j601_signal_stabilized:
        "La ligne d'erreur de ma tablette disparaît. J'arrive à rouvrir le dossier de vote, mais les écrans des autres répondent encore avec du retard."
        noam surpris "Le mien est revenu !"
        kael reflechit "Tu as stabilisé ton canal local. Pas celui de Kami. Ne prends pas ça pour une réparation."
        think "J'aurais préféré qu'il me laisse savourer ma victoire quelques secondes."
    else:
        "Ma tablette revient à l'écran d'accueil. Le dossier de vote refuse toujours de s'ouvrir."
        noam inquiet "J'ai essayé de récupérer le canal, mais je n'y arrive pas !"
        elias inquiet "C'est pas toi. Les écrans perdent la connexion les uns après les autres."
        kael inquiet "On va éviter de nouvelles manipulations. Personne ne doit valider un texte qu'il ne peut pas lire."
    elen inquiet "C'est terminé ? Dites-moi que c'est terminé..."
    mara neutre "On n'a même pas encore commencé à voter, Elen."
    elen inquiet "C'est bien ça qui m'inquiète."
    ryn colere "Et on est censés mettre nos bulletins dans ÇA ?! Autant tirer au sort !"
    nyra reflechit "On ne vote pas avant de savoir si le scrutin peut être enregistré correctement. C'est le minimum."
    ryn colere "Je voulais voter pour. Mais là ? Elle pourrait nous faire approuver une exécution collective à la place !"
    kael reflechit "C'est impossible à vérifier depuis nos tablettes."
    elen inquiet "Alors même si on voulait ouvrir les frontières..."
    mara neutre "On ne va pas signer un texte sur un écran qui change tout seul."
    lysa blase "Formidable. Après avoir perdu une fois parce qu'on n'était pas d'accord, on va perdre parce qu'on est tous terrifiés par le matériel."
    noam inquiet "Ne décidons rien tant que le texte ne s'affiche pas normalement."
    "Kami réapparaît. Son sourire est parfaitement immobile."
    "Sa voix arrive une seconde avant que ses lèvres bougent."
    think "C'est peut-être la même IA. J'ai pourtant l'impression de regarder quelque chose qui essaie de l'imiter."
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je suis... toujours là."
    kami "Les systèmes du Conclave sont disponibles. Nous pouvons poursuivre."
    mara mefiant "Tu plaisantes ?! On vient de voir nos tablettes s'éteindre sous nos yeux !"
    kami "Les systèmes sont disponibles."
    kami "Ils sont... disponibles."
    "Personne ne lui répond."
    think "Je n'ai jamais vu autant de gens refuser de parler à Kami en même temps. Pas même Ryn."

    jump _6_0_1_FRACTURE_QTE

label _6_0_1_FRACTURE_QTE:

    "Une notification apparaît devant moi."
    "Ses caractères changent avant que je puisse finir de les lire. Une seconde ligne prend sa place."
    think "La tablette me demande quelque chose. Le problème, c'est que la question ne reste jamais la même."
    noam inquiet "Euh... votre tablette aussi vient de changer le texte à l'écran ?"
    tomas inquiet "OUI ! Enfin, non ! J'avais la proposition sur les frontières..."
    tomas peur "Maintenant ça me demande de confirmer quelque chose que je n'ai jamais vu !"
    kael inquiet "TOUCHEZ À RIEN ! Pas de confirmation tant que le texte n'est pas stable !"
    elias gene "Même si le bouton clignote ?"
    mara colere "ELIAS !"
    elias colere "J'AI PAS APPUYÉ ! C'ÉTAIT UNE QUESTION !"
    tomas inquiet "À sa décharge, le bouton clignote vraiment très fort."
    iris blase "C'est merveilleux. On va mourir à cause d'un bouton lumineux."
    kael colere "SURTOUT s'il clignote !"
    play sound "audio/sfx_glitch.mp3"
    "Les données s'entremêlent sur l'écran principal."
    "Pendant une seconde, les mots « libre circulation » sont remplacés par des signes incompréhensibles."
    think "Je comprends pourquoi Tomas a retiré ses mains de la tablette. Je fais la même chose."
    call j601_play_fracture from _call_j601_play_fracture
    $ j601_fracture_result = _return

    scene bg_conclave at adaptive_fullscreen with dissolve
    "Les caractères se stabilisent enfin."
    "Le texte sur les frontières est revenu. Même formulation. Mêmes boutons."
    if j601_fracture_result:
        $ j601_fracture_trace_saved = True
        "Une dernière ligne subsiste sur ma tablette : « DÉCALAGE ENTRE CANAL DE SÉANCE ET CONTRÔLE LOCAL — TRACE CONSERVÉE »."
        noam inquiet "Kael, regarde. J'ai réussi à garder une trace de l'erreur."
        kael reflechit "Ne l'efface surtout pas. Ce n'est pas une preuve que le vote est falsifié, mais on pourra comparer les journaux."
        elias inquiet "Donc... on a peut-être un moyen de vérifier après ?"
        kael calme "Un point de départ. Pas encore une réponse."
    else:
        $ j601_fracture_trace_saved = False
        "Je tente de retrouver la ligne qui a remplacé le texte. Elle a disparu, et la tablette ne me propose aucun historique."
        noam inquiet "J'ai perdu l'erreur. Je sais ce que j'ai vu, mais je ne peux pas le montrer."
        nyra reflechit "Alors nous ne prétendrons pas avoir identifié une modification. Nous savons seulement que l'affichage a été instable."
        think "C'est peut-être la différence la plus pénible : avoir eu peur de quelque chose sans pouvoir dire exactement quoi."
    think "Personne n'a envie d'être le premier à toucher son écran."
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Merci de votre... patience."
    kami "Nous allons maintenant procéder au vote."
    elen inquiet "NON ! Attends, Kami !"
    elen inquiet "Tu vas bien ? Parce que nous, on vient de voir la moitié de tes écrans devenir fous !"
    kami "Les procédures ont été rétablies."
    kami "Vous pouvez voter. Vous devez... vous pouvez voter."
    iris colere "Et si tu comptes mal ?! On a douze vies politiques entre les mains, pas un exercice de calcul !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le dépouillement utilise un système distinct."
    kami "Il est opérationnel."
    kami "Il est opérationnel."
    kael reflechit "Je ne peux pas vérifier ce système depuis ici."
    kael doute "Ça ne veut pas dire qu'il est défectueux. Mais je ne peux pas vous garantir qu'il ne l'est pas."
    ryn colere "Ça suffit pour moi. Je voterai contre. Pas contre les gens aux frontières : contre ce cirque !"
    elen triste "Ryn..."
    ryn colere "JE SAIS ! Je sais ce que je voulais ce matin."
    "Il baisse les yeux vers son écran. Derrière le bouton « POUR », le texte a enfin cessé de trembler."
    ryn triste "J'ai passé trois jours à demander qu'on ouvre ces foutues frontières."
    ryn triste "Et maintenant, je peux même pas garantir à ceux qui attendent que c'est bien leur liberté que je suis en train de voter."
    sael triste "Ryn..."
    ryn colere "Ne me console pas. Surtout pas toi."
    "Sael détourne les yeux. Pour une fois, elle le laisse finir."
    ryn triste "C'est moi qui vais leur dire que j'ai voté non. Personne d'autre."
    lysa reflechit "C'est justement ce qui me fait peur. Je voulais voter pour aussi."
    lysa blase "Mais quand l'urne électronique essaie de nous manger les mains, je préfère garder mes deux bras."
    nyra raison "Rejeter la proposition ne répare pas le système. Ça empêche au moins d'engager immédiatement un changement qu'on ne contrôle plus."
    elen inquiet "Je n'arrive plus à savoir quel choix fera le moins de mal."
    mara neutre "Moi non plus. Et je déteste dire ça."
    mara colere "Formidable ! Notre démocratie tient dans une boîte qui bégaie et qui nous interdit de vérifier ses calculs !"
    mara mefiant "On est vraiment censés lui faire confiance ?"
    sael determine "Je n'aime pas ce qui vient de se passer."
    sael determine "Mais l'amendement est le même. Mon choix aussi. Je voterai contre."
    ryn colere "ON SAIT, SAEL ! Tu pourrais arrêter de le répéter comme si ça rendait la chose plus facile ?!"
    sael mefiant "Je ne te parle pas à toi seul, Ryn."
    sael neutre "Si tu veux que je respecte ta position, commence par respecter la mienne."
    noam inquiet "D'accord. Alors une dernière chose avant le vote."
    noam inquiet "Kami, redis-nous exactement le texte. Pas ton résumé. Le texte."
    pause 0.3
    kami "« Autoriser la libre circulation des personnes entre les districts. »"
    kami "Aucune... aucune autre modification n'est prévue."
    lysa blase "Très bien. On sait ce qu'on vote."
    lysa blase "Il ne manque plus qu'à espérer que notre vote arrive au bon endroit. Un détail."
    "Les voyants des tablettes passent au vert."
    "Le scrutin s'ouvre."
    think "Ce matin, certains voulaient ouvrir les frontières à tout prix. Maintenant, je les regarde reculer devant leurs propres tablettes."
    think "Je comprends leur peur. Je n'arrive pas à oublier ceux qui attendent derrière les barrières."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 0.7
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

    "Les votes défilent sur l'écran."
    "Un contre. Puis un autre. Encore un."
    think "Je savais qu'il n'y aurait pas d'unanimité. Mais voir les refus s'accumuler donne à la défaite un tout autre poids."
    "Le texte est rejeté. L'écran n'indique que les totaux ; aucun nom n'accompagne les bulletins."
    think "Sael a annoncé son intention de voter contre. Je n'ai aucun moyen de connaître son bulletin, ni celui de Ryn."
    think "Je repense à sa promesse, et au regard que Ryn a posé sur son propre écran."
    if player_vote == "pour":
        think "J'ai voté pour."
        think "Pas parce que j'ignorais les risques. Parce que je n'arrivais plus à accepter que des familles soient condamnées à attendre derrière une barrière."
        think "Ça ne rend pas les peurs de Sael moins réelles."
    elif player_vote == "contre":
        think "J'ai voté contre."
        think "Je n'ai pas réussi à accepter une ouverture immédiate, sans garantie pour ceux qui vivent près des passages."
        think "Ça ne m'empêchera pas de revoir le visage de la femme à la télévision."
    else:
        think "Je me suis abstenu."
        think "Deux décisions m'effrayaient. Je n'ai pas su choisir laquelle j'étais prêt à assumer."
        think "Je sais qu'il y a des gens qui appelleraient ça de la prudence. D'autres, de la lâcheté."
    $ hideGroup()
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    "Au bout de la table, Sael fixe les résultats. Je ne peux rien lire sur son visage."
    "Ryn, lui, n'a pas détourné les yeux une seule fois."
    think "Le vote est secret. Cela n'empêche personne d'imaginer le bulletin de son voisin."
    think "Je voudrais lui dire quelque chose. Pour une fois, je n'ai aucune phrase qui me paraît utile."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Résultat... du scrutin."
    kami "Absence d'unanimité. La libre circulation entre les districts... est rejetée."
    $ interject("REJETÉ", color="#FF4D6D")
    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Les restrictions restent en vigueur."
    kami "Nous nous retrouverons pour... pour le prochain vote."
    kami "Merci de... votre participation."
    "Son image disparaît sans musique de conclusion, sans sarcasme, sans la moindre remarque supplémentaire."
    think "Je crois que c'est la première fois que Kami annonce une défaite sans avoir l'air de savourer le résultat."
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
    ryn colere "C'EST TOUT ?!"
    elen triste "Ryn, tu as voté contre, toi aussi..."
    ryn colere "JE SAIS !"
    ryn triste "Je sais très bien ce que j'ai fait."
    "Sael détourne la tête. Elle pourrait lui répondre. Elle ne le fait pas."
    ryn colere "Les gens qui attendaient ce matin vont rentrer chez eux. Encore. Et nous, on va faire quoi ? Se féliciter d'avoir débattu proprement ?!"
    iris fatigue "Personne ne se félicite, Ryn."
    ryn colere "J'ai pas demandé ton avis !"
    iris colere "Eh bien, tu l'as !"
    julian hesitation "On pourrait peut-être éviter..."
    lysa blase "Non, Julian. Pas maintenant."
    sael triste "Ryn..."
    sael triste "Je sais ce que ce vote signifie pour toi. Je ne te demande pas de m'approuver."
    ryn colere "ALORS ME DEMANDE RIEN !"
    ryn triste "Parce que là... j'y arriverais pas."
    mara agace "Elle t'avait prévenu, Ryn. Elle n'a pas changé son vote en douce juste pour te faire mal."
    ryn triste "Je sais."
    ryn triste "Mais je me demande comment je vais expliquer ce résultat à ceux qui attendaient."
    tomas inquiet "Euh... excusez-moi, mais on vient vraiment de voter alors que Kami ne tenait pas sa connexion ?!"
    tomas inquiet "On sait au moins si nos douze votes ont tous été enregistrés ?"
    kael reflechit "Douze bulletins sont comptabilisés. Ça correspond au nombre de représentants."
    if j601_fracture_trace_saved:
        kael inquiet "Mais le décalage que Noam a conservé n'est pas expliqué. Je vais comparer sa trace aux journaux de la station."
        nyra raison "Cela ne permet pas de déduire le vote de qui que ce soit. Et c'est très bien ainsi."
    else:
        kael inquiet "Mais sans trace de la perturbation sur les tablettes, je ne peux pas vérifier ce qui s'est passé pendant la coupure."
        nyra reflechit "Alors nous devons reconnaître ce que nous ignorons, au lieu de prétendre que l'absence de preuve suffit à nous rassurer."
    iris inquiet "Attendez... C'est pas juste le vote qui m'inquiète."
    iris inquiet "La seule chose qui gère les sanctions, nos repas et jusqu'aux portes vient de décrocher en pleine séance. Et on n'a aucun moyen de savoir pourquoi ?"
    elias fatigue "Kael et moi, on peut inspecter les systèmes locaux."
    elias gene "Ça me permettra aussi de vérifier que je n'ai pas laissé une catastrophe derrière moi avec mon café."
    julian decu "Deux votes. Deux échecs."
    julian decu "Et maintenant, on découvre que notre arbitre peut s'interrompre au milieu d'une phrase. On est censés rassurer qui, exactement ?"
    lysa blase "Pour une fois, tu as résumé nos problèmes sans ajouter que tu aurais personnellement sauvé le monde."
    julian taquin "Ne t'y habitue pas. Je prépare une déclaration officielle sur mon incroyable modestie."
    "Un rire discret parcourt la table. Il s'éteint presque aussitôt."
    "Ryn se lève et quitte la salle sans saluer personne."
    think "Personne ne tente de le retenir."
    think "Ce matin, Ryn voulait forcer la porte. Cet après-midi, il a lui-même voté pour qu'elle reste fermée."
    think "Je ne sais pas lequel des deux lui fait le plus mal."

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
    elen inquiet "Vous croyez que Kami sera... redevenue normale demain ?"
    mara taquin "On pourrait lui offrir une carte de rétablissement. « Reviens vite, tes humiliations nous manquent »."
    tomas gene "Les cartes de rétablissement sont plutôt destinées à..."
    iris blase "Tomas, c'était une blague."
    tomas inquiet "Je sais. Je cherchais juste... enfin, laisse tomber."
    elen sourire "Je pourrais quand même en fabriquer une."
    mara surpris "NON ! Elen, s'il te plaît, ne l'encourage pas !"
    elen inquiet "Je ne pensais pas dire ça un jour, mais ses insultes me manquent presque."
    iris reflechit "Elle est insupportable, mais d'habitude ses réactions suivent une logique."
    iris inquiet "Aujourd'hui, elle avait l'air de lutter pour terminer ses propres phrases."
    mara agace "Moi, j'aimerais surtout savoir ce qu'on fait si elle s'éteint pour de bon."
    mara mefiant "On a un plan ? Une trousse de secours pour intelligence artificielle ? Ou on s'assoit et on attend le prochain bip ?"
    kael reflechit "Je vais regarder les journaux d'erreurs de la station. Et vérifier le panneau de l'observatoire."
    kael calme "Je ne pense pas qu'un café renversé puisse provoquer ça, mais je préfère éliminer cette possibilité plutôt que deviner."
    lysa blase "Bonne chance pour demander à Kami l'accès aux fichiers qui prouvent qu'elle n'a aucun problème."
    lysa taquin "Je sens qu'elle va adorer."
    kael calme "Pas aux siens. Aux systèmes de la station, peut-être."
    kael reflechit "Et si même ça nous est refusé, ce sera déjà une information."
    tomas inquiet "Et si vous trouvez quelque chose..."
    tomas inquiet "Vous nous prévenez ? Même si c'est une mauvaise nouvelle ?"
    iris sourire "Bien sûr."
    mara taquin "Et si on découvre que Kami nous espionne, on lui fera un compte rendu détaillé de nos soupçons."
    kael calme "Mara, il nous faut les journaux de la station. Pas une nouvelle dispute."
    mara sourire "Tu me retires mes deux seuls loisirs."
    iris blase "On n'a pas l'intention d'organiser une fête-surprise avec une panne mondiale."
    "Elen propose une partie de cartes pour éviter que tout le monde s'enferme dans sa chambre."
    elen sourire "Sans débat ! Promis !"
    mara taquin "Tu dis ça comme si une partie de cartes ne pouvait pas déclencher une guerre."
    "Quelques-uns acceptent. Je préfère rentrer."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_275
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "decu", 0.25), ("elias", "fatigue", 0.55), ("ryn", "colere", 0.85)])
    julian decu "Ryn... Je sais que ça s'est mal passé. Mais Sael avait prévenu qu'elle voterait contre."
    ryn colere "Et moi, je me suis présenté comme son contraire toute la journée. Pour finir par voter exactement comme elle."
    julian hesitation "Oui... je sais. C'est justement..."
    ryn colere "Non, tu ne sais pas."
    julian hesitation "Je veux dire... tu ne pouvais pas vraiment t'attendre à autre chose."
    ryn colere "Julian. Pas maintenant."
    ryn triste "S'il te plaît."
    julian neutre "Je voulais juste essayer de..."
    julian hesitation "Bon. D'accord."
    elias fatigue "Laisse-le tranquille."
    elias gene "Je sais que tu veux arranger les choses, mais... pas comme ça."
    julian decu "Je n'insiste pas."
    julian decu "Bonne soirée, Ryn."
    "Ryn s'éloigne."
    "Julian fait un pas dans sa direction, puis s'arrête. Elias lui adresse un petit signe et rejoint Kael."
    think "Hier, Julian aurait probablement insisté jusqu'à obtenir une réponse. Ce soir, il laisse Ryn partir."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_276
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    "Je m'assieds sur mon lit. La station est silencieuse."
    "Ma tablette affiche toujours le résultat du vote : « REJETÉ »."
    think "La femme du reportage avait gardé une boîte de thé pour son frère. Demain, elle devra encore la conserver."
    think "Ryn a demandé qu'on ouvre les frontières pendant trois jours. Aujourd'hui, il a annoncé qu'il voterait contre."
    think "Je pourrais lui en vouloir. Mais devant ma propre tablette, j'avais peur moi aussi."
    if j601_fracture_trace_saved:
        "Une petite icône signale la trace d'incident conservée dans mon dossier."
        think "Kael a promis de la regarder. Ce serait presque rassurant si je savais ce qu'on cherchait."
    else:
        "Je cherche la ligne étrange apparue au Conclave. Rien. Pas même un message d'erreur."
        think "Impossible de raconter exactement ce que j'ai vu. Il ne reste que ma mémoire, et elle n'a jamais été très utile devant un tribunal."
    "Je pose la tablette sur mon bureau. Pour une fois, je n'ai pas envie de regarder le prochain bulletin de vote."
    "L'écran s'allume tout seul."
    "Pas la grande diffusion de Kami. Juste une notification discrète, sans logo ni sonnerie."
    "« FIN DE SESSION IMPOSSIBLE — PARTICIPANTS REQUIS »"
    think "Des participants ? À cette heure-ci ?"
    "Je tends le doigt vers la notification. Avant que je la touche, elle disparaît."
    "Je consulte le journal des alertes. Il est vide."
    "J'attends quelques secondes, puis j'éteins la tablette. Cette fois, je vérifie qu'elle est bien éteinte."
    think "Kami nous avait demandé de rester au Conclave. Et si sa séance n'était pas terminée pour elle ?"
    $ blink()
    "Je finis par fermer les yeux. La question, elle, refuse de me laisser dormir."

    $ kami_grant_chapter_2_reward()

    call show_chapter_title("Fin du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_3

    pause 1.0

    #jump patreon_ending

    call end_day("7", sleeping=True) from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE

# total : 8m
# Total jour 0-6 : 1h49
