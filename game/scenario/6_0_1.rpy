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

    jump _6_0_1_TEMPS_LIBRE

label _6_0_1_TEMPS_LIBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_264
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Fin de matinée"

    think "Il reste encore plusieurs heures avant le vote. Assez pour que chacun recommence à éviter les autres."
    think "Je devrais profiter de ce temps avant que Kami nous rappelle au Conclave."

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
    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "Maintenez."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Le."

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "Signal."

    think "Son image saute en boucle."

    scene bg_conclave at adaptive_fullscreen with vpunch

    $ showGroup([("iris", "inquiet", 0.3), ("ryn", "colere", 0.6), ("lysa", "blase", 0.85)])

    iris "C'est quoi, ce cirque—"

    ryn "Elle bugue complet là ?"

    lysa "Ouais, c'est bien ce qu'on disait tout à l'heure."

    play sound "sfx/glitch_loop.mp3"

    # --- LANCEMENT MINI-JEU ---
    call j601_play_signal_instable from _call_j601_play_signal_instable
    # --------------------------

    stop sound fadeout 0.5

    think "Le bruit coupe net."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "..."

    think "Pas un silence : un trou."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Stabilisation."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Incomplète."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Insuffisante."

    kami "Imprécise."

    think "Sa voix accroche encore."

    play sound "sfx/glitch_light.mp3"

    kami "Corrigez."

    kami "Encore."

    think "Son image reste figée une fraction de trop."

    think "..."

    think "Elle dérape."

    think "Ou elle fait semblant."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    think "Personne ne commente. Nous attendons seulement la suite."

    jump _6_0_1_FRACTURE_QTE

# Durée : ~1m30 (hors mini-jeu)


label _6_0_1_FRACTURE_QTE:

    call j601_play_fracture from _call_j601_play_fracture
    $ j601_fracture_result = _return

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Puisque vous refusez de débattre…"
    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch
    kami "Il est temps maintenant de mour—"
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Voter."
    kami "Voter."
    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "Pardon."
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Correction effectuée."

    play sound "sfx/glitch_heavy.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch
    kami "Le débat est clos."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    think "Personne ne bouge."

    $ showGroup([
        ("mara", "doute"),
        ("iris", "peur"),
        ("ryn", "neutre"),
        ("lysa", "blase"),
        ("tomas", "inquiet"),
        ("elen", "inquiet"),
        ("sael", "neutre"),
        ("kael", "inquiet"),
    ])

    iris colere "... Elle vient de dire quoi là ?!"

    ryn reflechit "J-je sais pas, c'était incompréhensible."

    mara mefiant "Bien sûr que si, tu as parfaitement compris ce qu'elle a voulu dire."

    iris inquiet "Vous avez entendu la même chose que moi ?"

    mara "Moi, j'ai entendu « mourir »."

    lysa reflechit "Elle a aussi dit voter."

    mara rire "Ouais. Après. Trop tard."
    mara reflechit "Je sais pas exactement ce qu'elle a voulu nous dire, mais clairement, vu son état, moi je prends pas le risque de voter pour un truc qui change les règles du monde."

    iris colere "Ouais, c'est clair. C'est beaucoup trop dangereux."

    tomas reflechit "Peut-être... Qu'il y a un truc qu'on a pas compris dans le texte ?"

    elen triste "Bof ! On peut pas voter là-dessus ! On sait même pas ce qu'elle a dit !"

    lysa blase "Et pourtant, ils attendent tous notre réponse."

    elen inquiet "Non, mais vraiment— Si Kami bugge pendant qu’elle annonce le texte, qu’est-ce qui se passe si on vote pour ?"

    sael colere "On ne sait pas. De toute façon j'avais déjà prévu de voter contre."
    sael triste "Vous pouvez faire ce que vous voulez, ce texte ne passera pas."

    ryn colere "Même si ça pourrait aider tes proches ? Tu es vraiment prête à l'assumer devant eux ?!"

    mara colere "On ne va pas revenir sur le sujet. Puis avec les trucs chelous qui se passent, c'est une raison de plus pour voter contre."

    iris triste "Ce changement-là attendra. C'est tout."

    ryn triste "M-..."

    sael triste "Un jour, tu comprendras."

    think "Elle ne va pas..."

    $ hideGroup()

    call j601_sael_vote_animation from _call_j601_sael_vote_animation

    pause 0.6

    $ showGroup([
        ("mara", "doute"),
        ("iris", "peur"),
        ("ryn", "neutre"),
        ("lysa", "blase"),
        ("tomas", "inquiet"),
        ("elen", "inquiet"),
        ("sael", "neutre"),
        ("kael", "inquiet"),
    ])

    ryn colere "Putain mais pourquoi t'as fait ça ?!"

    noam colere "C'est son choix. Il faut le respecter."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5

    kami "HEP HEP HEP ! On était pas-pas au moment du vote !"

    scene bg_diffusion_amour at adaptive_fullscreen with hpunch

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with hpunch
    kami "Bref. Le débat était déjà clos. Finissons-en."

    play sound "sfx/glitch_light.mp3"

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.0

    "Kami semble particulièrement pressée d'en finir."

    jump _6_0_1_VOTE

# Durée : ~3m10 hors mini-jeu

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

    think "Le résultat reste affiché quelques secondes. Il n'a surpris personne."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Résultat du vote."
    $ interject("REJETÉ", color="#FF4D6D")
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Ab— Absence d'unanimité. Amendement rejeté."

    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "La libre circulation entre… demeure interdite."

    scene bg_diffusion_taquin at adaptive_fullscreen
    kami "Statu quo maintenu."

    scene bg_diffusion_colere at adaptive_fullscreen
    kami "Prévis—ble. Décevant. Mais prévisible."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "colere"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("mara", "doute"),
        ("tomas", "inquiet"),
        ("julian", "sourire"),
        ("elias", "fatigue"),
        ("lysa", "fatigue"),
    ])

    ryn colere "Putain..."

    iris triste "Je sais même pas quoi dire face à ce qui vient de se passer."

    sael triste "C'était de toute façon nécessaire."

    ryn colere "...Ne dis pas ça."

    sael triste "Je le pense."

    ryn triste "C'est bien ça le problème."

    tomas "C'était... catastrophique."

    julian triste "... Évidemment. Cette conclusion était certaine."
    julian taquin "C'est ce qui arrive quand je reste loin des débats."

    think "Quel enfoiré celui-là."

    elias triste "De toute façon, on savait comment ça finirait. T'aurais rien pu changer."
    elias "Les bugs ont juste rendu le choix encore plus évident."

    think "Elias ne défend même pas son choix. Il est vidé."

    "Tout le monde repart peu à peu."

    hide sael with moveoutright

    think "C'est terminé."
    think "Mais rien n'est réglé."

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
        ("sael", "fatigue"),
    ])

    elen triste "Waaa, vraiment trop dég de ce qui s'est passé !"

    lysa blase "Ouais. C'était vraiment étrange ce qui s'est passé."
    lysa colere "J'espère juste qu'elle pètera pas un câble demain."

    iris blase "Ils voulaient du changement ? Deux votes, deux échecs."
    iris colere "Franchement, qu'est-ce que vont dire les gens ?"

    mara colere "On en a rien à foutre de l'avis des gens."
    mara taquin "T'as vraiment cru que leurs avis m'intéressent."

    tomas triste "Franchement, je-je crois bien qu'on va jamais réussir à faire passer un amendement."

    elias colere "On sert vraiment à rien..."

    iris triste "Je veux prendre une douche."
    iris colere "Et j'en ai marre qu'elle décide tout pour nous ! Qu'elle garde son cerveau de génie, mais qu'elle nous foute la paix deux minutes !"

    kael "Navré hein, mais ça ça sera pas demain la veille."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_275
    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([("julian", "decu", 0.25), ("elias", "fatigue", 0.55), ("ryn", "colere", 0.85)])

    julian triste "On va vraiment faire comme si rien ne s'était passé ?"
    julian colere "Remarquable stratégie collective. Si on continue comme ça, on échouera tous les trois jours."

    ryn colere "Fais pas comme si t'en avais quelque chose à foutre."

    elias triste "Arrêtez. Vous deux."
    elias colere "On n'est pas des gamins. Arrêtez."
    elias neutre "Ne vous battez pas ici."

    julian "Où alors ?"

    noam colere "Bon j'ai pas de temps pour vos chamailleries."
    noam triste "Bonne nuit, et faites moins de bruit."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_276
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    think "La porte de ma chambre se referme. Le calme revient. Il m'avait manqué."
    think "J'ai voté. Ils ont voté. Kami a déliré toute la journée…"

    think "Je laisse tomber ma veste et reste debout sans raison."
    think "Qu'est-ce qui s'est passé ?"

    think "Pourquoi la machine qui dirige le monde s'est-elle mise à dérailler ?"
    think "Est-ce que ça aurait un rapport avec l'incident d'hier ? Elias aurait-il endommagé quelque chose dont Kami dépend ?"

    noam "Non. Impossible... Ce serait beaucoup trop simple."

    think "Rien n'avait de sens dans ce qu'elle disait..."
    think "Un lapsus. Une menace. Un bug."

    think "Lapsus, menace ou panne. Trois réponses, aucune utile."

    think "Quelque chose a changé."
    think "Je l'ai pensé ce matin. Maintenant, ce n'est plus qu'une impression."

    play sound "sfx/glitch_light.mp3"

    think "L'écran mural clignote une fois. Je me retourne. Il n'y a rien."
    think "Je passe de l'eau froide sur mon visage. Pas assez froide. Le miroir me rend celui du matin, un peu plus fatigué."

    think "Je retourne au lit sans me changer complètement."

    think "Demain, ça ira mieux."
    noam "Mmhh, si seulement c'était possible..."

    think "Tant pis."
    think "Mes paupières deviennent lourdes. Derrière le silence, très loin ou très près, la voix de Kami résonne dans ma tête."

    $ blink()

    $ kami_grant_chapter_2_reward()

    call show_chapter_title("Fin du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_3

    pause 1.0

    #jump patreon_ending

    call end_day("7", sleeping=True) from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE

# total : 8m
# Total jour 0-6 : 1h49
