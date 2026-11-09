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
    think "Je me réveille avant l'annonce de Kami. Aujourd'hui, on doit voter sur l'ouverture des frontières, et j'ai encore en tête ce que Sael m'a raconté."
    think "Elle a clairement dit qu'elle voterait contre. Je ne sais pas si j'aurais fait le même choix à sa place, mais je comprends mieux pourquoi elle refuse."
    "J'enfile mes vêtements et je vérifie l'heure sur ma tablette."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Booooonjour, tout le monde ! Aujourd'hui, c'est votre deuxième vote. Vous devez commencer à connaître la procédure."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à quatorze heures pour vous prononcer sur la circulation entre les districts."
    "Sa voix se coupe très brièvement au milieu de la phrase. L'écran reste figé un instant, puis l'animation reprend."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous pourrez discuter avant, bien sûr. Je vous laisse une dernière occasion de... de..."
    pause 0.7
    kami "De vous mettre d'accord. Voilà."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "La cafétéria est ouverte. Profitez-en, la prochaine livraison arrivera demain matin."
    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    think "Je reste un moment à regarder l'écran éteint. Kami a déjà fait semblant de buguer pour nous provoquer, mais cette fois, elle n'a même pas essayé d'en rire."
    think "Je vais voir si les autres ont remarqué la même chose."
    "Je ramasse ma veste sur la chaise et je quitte la chambre."

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

    "En arrivant à la cafétéria, j'entends plusieurs conversations. L'ambiance n'est pas particulièrement joyeuse, mais au moins les gens se parlent."

    $ showGroup([
        ("elias", "fatigue"),
        ("mara", "neutre"),
        ("elen", "neutre"),
        ("lysa", "blase"),
        ("iris", "fatigue"),
        ("sael", "neutre"),
    ])

    elen inquiet "Noam ! Dis-moi que t'as entendu l'annonce de Kami. Elle s'est arrêtée en plein milieu d'une phrase, non ?"
    noam reflechit "Ouais. J'ai même cru que l'écran avait planté chez moi."
    elias fatigue "Elle a fait pareil dans le dortoir. C'est pas juste le haut-parleur de ta chambre."
    mara taquin "Peut-être qu'elle a enfin appris à réfléchir avant de parler. Ça lui ferait pas de mal."
    lysa blase "C'est bizarre, mais elle nous a déjà fait des blagues plus tordues. Je vais pas commencer à paniquer pour une phrase ratée."
    iris reflechit "Ce qui m'inquiète, c'est qu'elle ne l'a pas commentée. D'habitude, quand elle veut nous faire peur, elle insiste jusqu'à ce qu'on réagisse."
    elen taquin "Ou alors elle est crevée ! On devrait lui demander si elle a besoin de vacances."
    elias sourire "Imagine Kami en vacances. Tous les distributeurs nous laisseraient enfin choisir ce qu'on veut."
    mara rire "Ça, ce serait une vraie raison de fêter quelque chose."
    sael mefiant "Vous pouvez plaisanter, mais c'est elle qui commande les systèmes de la station. Si elle rencontre vraiment un problème, je préférerais qu'on le sache avant le vote."
    noam inquiet "Tu crois que ça peut venir de la station ?"
    elias inquiet "J'en sais rien. Après ce que j'ai fait hier, j'ai demandé à Kael de vérifier le panneau de l'observatoire. Ça m'étonnerait qu'une console grillée puisse perturber Kami, mais je peux pas te le garantir."
    iris fatigue "Attends. Vous parlez de l'accident du café ? Ça n'a peut-être aucun rapport, Elias. Ne commence pas à t'accuser de tout."
    elias reflechit "Je m'accuse pas ! Je dis juste que je vais lui demander, c'est tout."
    "Goumi passe près de la table pour déposer un plateau. Elias pousse aussitôt sa tasse au milieu de la table, loin de la console et du bord."
    mara taquin "Tiens, il a retenu la leçon !"
    elias sourire "Oui, oui, ça va. Je pose mes boissons loin de tout ce qui coûte cher, désormais."
    lysa reflechit "Bon, et pour le vote ? Quelqu'un a réussi à parler à Sael ?"
    sael determine "Je suis là, Lysa. Tu peux me demander directement."
    lysa blase "Je demandais surtout si vous aviez discuté ensemble. Je sais déjà ce que tu vas voter."
    sael neutre "Noam est venu me voir hier. Je lui ai expliqué mes raisons, mais je reste contre."
    elen triste "C'est dommage. J'aimerais tellement qu'on trouve un moyen pour que les familles puissent se retrouver."
    sael triste "Moi aussi. Mais je n'accepterai pas d'ouvrir les frontières sans savoir comment on protégera mon village."
    mara agace "Et moi, je refuse qu'on fasse comme si ça allait régler tous nos problèmes. On n'arrive déjà pas à gérer les distributions."
    noam neutre "On en reparlera au Conclave. On a encore quelques heures, autant éviter de se disputer pendant le petit-déjeuner."
    iris sourire "Excellente idée. J'aimerais finir mon repas sans avoir à arbitrer une bagarre."
    "Les conversations reprennent autour de la table. Elias raconte à Elen ce que Kael lui a dit sur sa console, tandis que Mara et Lysa discutent de ce qu'elles voudraient demander à Kami."
    think "Tout le monde semble avoir remarqué quelque chose d'étrange ce matin, mais personne ne sait quoi en penser. Pour le moment, le Conclave fonctionne normalement."
    "Avant de partir, je remarque qu'un reportage sur les frontières de Limen vient de commencer à la télévision."
    call _6_0_1_TV_FRONTIERES from _call_6_0_1_TV_FRONTIERES_matinale
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "Je comprends pourquoi Ryn tient tellement à ce vote, mais je repense aussi aux habitants que Sael veut protéger. Je ne sais pas comment on pourrait satisfaire tout le monde avec le texte actuel."

    jump _6_0_1_TEMPS_LIBRE

label _6_0_1_TEMPS_LIBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_264
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Fin de matinée"

    think "Il reste un peu de temps avant le vote. Je vais en profiter pour voir les autres, sans forcément revenir sur nos désaccords d'hier."

    call START_FREE_TIME("_6_0_1_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_6_0_1


label _6_0_1_TV_FRONTIERES:

    $ j601_border_news_seen = True
    $ unlock_gallery_image("bg_cg035")
    scene bg_cg035 at adaptive_fullscreen with dissolve
    "La télévision montre des rassemblements aux points de passage de Limen. Des familles attendent derrière les barrières, avec des sacs et parfois leurs enfants."
    "JOURNALISTE — Plusieurs groupes se sont réunis ce matin. Ils espèrent que le vote du Conclave permettra de circuler à nouveau entre les districts."
    "UNE FEMME — Mon frère habite de l'autre côté. Ça fait des années qu'on n'a pas pu se voir, alors oui, je suis venue. Même si je ne sais pas ce qu'ils vont décider."
    "Un homme interrogé quelques mètres plus loin explique au contraire qu'il redoute l'ouverture des passages et demande comment les autorités contrôleront les groupes violents."
    think "Les deux réponses me rappellent exactement la dispute entre Ryn et Sael. Ici aussi, les gens sont loin d'être tous d'accord."
    "Le direct continue sur une vue des barrières. Personne ne tente de les franchir."
    return

label _6_0_1_TRANSITION_CONCLAVE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ current_period = "Après-midi"

    think "À l'approche de quatorze heures, les représentants commencent à rejoindre le Conclave. Je retrouve Elen et Tomas dans le couloir du dortoir."
    $ showGroup([("elen", "neutre", 0.25), ("tomas", "inquiet", 0.65), ("noam", "neutre", 0.85)])
    tomas inquiet "Vous avez encore reçu un message de Kami ? Elle nous a avancé l'heure de dix minutes, je crois."
    elen surpris "Moi, ma tablette dit toujours quatorze heures. Elle a peut-être envoyé la mauvaise notification."
    noam inquiet "C'est possible. On ferait mieux d'aller voir, de toute façon."
    play sound "sfx/glitch_light.mp3"
    "Les éclairages du couloir s'éteignent une fraction de seconde. Quand ils reviennent, l'écran mural affiche une image de Kami, figée."
    elen inquiet "Bon... ça aussi, elle l'avait prévu ?"
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes représentants ! Je constate que vous êtes déjà en route. Parfait. Nous pouvons commencer un peu plus tôt."
    noam inquiet "Kami ? Pourquoi l'heure a changé ?"
    pause 0.4
    kami "L'horaire a été... ajusté. Aucun problème. Rendez-vous au Conclave."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et tâchez d'arriver tous ensemble, ce serait plus simple pour... enfin, ce serait plus simple."
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    "Elen regarde sa tablette. Le nouvel horaire apparaît maintenant sur l'écran, comme si elle avait reçu la notification avec du retard."
    elen inquiet "J'aime pas ça. S'il y a un problème avec elle, elle pourrait au moins nous le dire."
    tomas hesitation "C'est peut-être juste un problème de communication. Je veux dire, ça arrive, non ?"
    noam neutre "Ouais, ça arrive. Mais pas très souvent avec Kami."
    "Nous rejoignons le reste du groupe devant l'entrée du Conclave. Sael arrive en dernier, accompagnée de Ryn. Ils ne se parlent pas, mais ils ne se disputent pas non plus."

    jump _6_0_1_CONCLAVE_START

label _6_0_1_CONCLAVE_START:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_267
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.5

    "Quand j'entre, plusieurs personnes sont déjà assises. Julian échange quelques mots avec Tomas ; à l'autre bout de la table, Ryn fixe la place de Sael."
    $ showGroup([("ryn", "colere", 0.20), ("iris", "fatigue", 0.48), ("sael", "neutre", 0.78)])
    ryn colere "Avant de commencer, j'aimerais quand même comprendre pourquoi certains refusent qu'on ouvre les frontières. Il y a des gens qui attendent depuis ce matin aux points de passage."
    sael determine "Je t'ai déjà répondu hier. Je ne veux pas exposer les habitants de mon village aux attaques qu'on a subies."
    ryn colere "Mais moi, je te parle des gens qui meurent maintenant ! Tu peux pas continuer à faire comme s'ils existaient pas."
    iris desaccord "Ryn, personne fait comme s'ils existaient pas. Vous avez tous les deux expliqué ce qui se passe chez vous, on a compris."
    ryn colere "Alors pourquoi on en est toujours au même point ?"
    noam inquiet "Parce que l'amendement est trop vague. Il dit qu'on ouvre les passages, mais personne ne sait ce qui se passera ensuite."
    sael neutre "C'est exactement pour ça que je voterai contre."
    "Ryn commence à répondre, mais l'écran principal s'allume avant qu'il ait terminé."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Tout le monde est là ? Bien ! Nous allons débattre de la proposition autorisant la libre circulation entre les districts."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je suis ravie de voir que certains d'entre vous ont déjà commencé. Continuez, je vous en prie !"
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
    elen inquiet "Moi, j'aimerais juste qu'on arrête de tuer les gens qui essaient de retrouver leur famille. Je sais bien qu'il y a eu des attaques, mais on pourrait peut-être contrôler les passages autrement."
    mara agace "Sauf que c'est pas ce qu'il y a dans le texte. Il suffit qu'on vote oui et tout ouvre, sans qu'on sache comment ça va se passer."
    ryn colere "Ça fait des années qu'on doit surveiller des frontières qu'on n'a même pas le droit de traverser. Vous pouvez pas nous demander d'attendre encore !"
    kael inquiet "Il faudra aussi adapter les transports. Si tous les passages ouvrent d'un coup, je vois pas comment les systèmes actuels vont suivre."
    lysa blase "Oui, mais si on attend d'avoir un plan parfait, personne ne pourra jamais sortir. Ça me dérange aussi."
    nyra reflechit "Vous êtes pas si loin d'être d'accord sur le problème. Mais vous voulez pas prendre le même risque. Sael, c'est bien le texte tel qu'il est qui te bloque ?"
    sael determine "Non, Nyra. Je suis opposée à l'ouverture des frontières. Même avec des contrôles, je pense que ça facilitera le retour des groupes armés. Je ne veux pas prendre ce risque."
    ryn colere "Alors qu'est-ce qu'on est censés faire ? Garder les gens enfermés pour toujours ?"
    sael colere "Je suis pas celle qui a mis ces règles en place ! Arrête de me demander de répondre pour Kami !"
    "Le ton monte. Iris frappe doucement la table pour essayer d'intervenir, mais elle s'interrompt quand Kami reprend la parole."
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Vous avez tous de très bonnes... de bonnes raisons, oui. Vous pourriez peut-être..."
    pause 0.7
    "Son visage reste figé. Un grésillement traverse les haut-parleurs avant que sa voix reprenne."
    kami "Poursuivez le débat. Je vous écoute."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    iris inquiet "Bon, ça commence à faire beaucoup pour une seule journée. Est-ce qu'on pourrait lui demander directement si tout va bien ?"
    noam neutre "Kami ? Tu nous entends ?"
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Évidemment que je vous entends. Vous êtes douze, dans une pièce que je surveille en permanence."
    "Elle marque une nouvelle pause. Cette fois, personne ne dit rien."
    kami "Vous n'avez pas terminé. Il faut continuer."
    mara mefiant "Attends, pourquoi il faut ? Tu peux pas simplement nous dire ce qui se passe avec toi ?"
    kami "Il faut que... le débat doit... continuer."
    play sound "sfx/glitch_medium.mp3"
    "L'image se déforme. Une partie de la phrase se répète plusieurs fois, sans que Kami termine sa réponse."
    elias inquiet "Les enceintes font pas ce bruit d'habitude. Kael, t'as une idée ?"
    kael inquiet "Ça ressemble pas à une panne du système audio. L'image et le son décrochent en même temps."
    nyra reflechit "Kami, est-ce qu'on doit interrompre la séance ?"
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    kami "Non ! Le débat continue !"
    pause 0.3
    "Sa réponse est si forte que Tomas se recule dans son fauteuil."
    tomas inquiet "D'accord, mais... personne t'empêche de nous donner quelques minutes."
    kami "Je n'ai pas besoin de..."
    play sound "sfx/glitch_heavy.mp3"
    "L'écran devient noir, puis l'image réapparaît avec un retard évident sur sa voix."
    think "Même si elle voulait nous faire peur, je ne comprends pas pourquoi elle insisterait autant pour qu'on continue à parler."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    iris inquiet "Vous avez vu ça ? Elle a complètement perdu l'image pendant une seconde."
    ryn colere "Qu'elle coupe la séance alors ! On va pas faire semblant que tout va bien juste pour lui faire plaisir."
    elen inquiet "Attendez, si elle va vraiment mal, qu'est-ce qui se passe pour les gens sur Terre ? Les frontières, les rations... Tout dépend d'elle !"
    mara mefiant "C'est exactement ce qui m'inquiète. Et elle veut quand même nous faire voter."
    "Les représentants commencent à parler tous en même temps. Avant que quelqu'un arrive à les calmer, les lumières clignotent à nouveau."

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
