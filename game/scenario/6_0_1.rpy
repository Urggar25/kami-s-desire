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

    pause 1.0

    $ blink()

    think "J'ouvre les yeux après une longue nuit de sommeil."
    think "J'ai enfin pu dormir convenablement. Peut-être parce que je sais déjà ce que cette journée nous réserve."
    think "Finalement, ça ne sert à rien de se prendre la tête pour un vote déjà perdu d'avance."

    play sound sfx_announce

    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.4

    kami "Eh bien bonjouur à tous ! Aujourd'hui est le jour que vous attendez tant ! C'est jour de vote !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote sur la libre circulation entre districts aura lieu aujourd'hui à qu-quatorze heure, dans le conclave."

    pause 0.8
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    pause 0.8

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais vous commencez déjà à avoir l'habitude de cette petite routine, n-n-'est-ce pas ?."

    "La voix grésille, elle est étrange. Presque comme modifiée."

    scene bg_diffusion_professeur at adaptive_fullscreen
    with vpunch

    pause 0.1

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Votre présence est-est... Recommandée."
    pause 2.0

    scene bg_diffusion_triste at adaptive_fullscreen
    with dissolve

    kami "Vous avez l'air fatigués. Enfin... J'imagine."

    scene bg_diffusion_colere at adaptive_fullscreen
    with dissolve

    kami "Vous me semblez, bi-bien moins intéréssant que ces derniers jours.."
    kami "C'est très contrariant."

    pause 0.4

    scene bg_diffusion_einstein at adaptive_fullscreen
    with hpunch

    pause 0.1

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Les jouets se cassent toujours plus vite une fois qu'on commence à jouer sérieusement avec eux."

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    think "L'écran s'éteint rapidement. Sans l'éclat de rire désormais habituel de Kami."
    think "Qu'est-ce qui a bien pu se passer ? Elle n'était pas comme d'habitude..."

    noam "C'est quoi ce bordel, encore..."

    pause 0.4

    think "Kami simule tout : joie, tendresse, colère, même ses silences. Mais... Pas là. Du moins j'en ai pas eu l'impression."

    $ _j601_reveil_trace_score = 0

    call screen trace_qte(path_type="s_curve", time_limit=4.2, wait_time=0.25, tolerance=78, max_errors=4, anchor_x=960, anchor_y=650, start_radius=120)
    if _return["success"]:
        $ _j601_reveil_trace_score = 1

    think "Je me lève. Mes jambes répondent avec un léger retard."

    pause 0.4

    think "Ma veste est par terre, beaucoup trop loin. Je la ramasse, l'enfile et gagne la porte."

    if _j601_reveil_trace_score >= 1:
        think "Je me relève rapidement. Je n'ai pas vraiment envie d'aller à la cafétéria."
    else:
        think "Mes jambes sont encore endormies. J'ai franchement la flemme de me lever."

    think "Mais bon, faut y aller. C'est tout."

    $ current_scene_active = "_6_0_1_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    tuto "(Rejoins la cafétéria.)"

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_6_0_1_CAFETERIA
    $ current_scene_active = None

    jump _6_0_1_CAFETERIA

label _6_0_1_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_263
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    pause 0.8

    think "Ils sont presque tous là. Ils parlent un peu tous dans leur coin, mais pas vraiment ensemble."

    call play_stat_dialogue("d6_0_1") from _call_stat_dialogue_d6_0_1

    $ showGroup([
        ("elias", "fatigue"),
        ("mara", "neutre"),
        ("elen", "neutre"),
        ("lysa", "blase"),
        ("iris", "fatigue"),
        ("sael", "neutre"),
    ])

    play sound "sfx/glass_spill.mp3"

    "CLAC. Encore."

    elias "Putain—"

    call screen trace_qte(path_type="arc", time_limit=1.8, wait_time=0.1, tolerance=86, max_errors=3, anchor_x=960, anchor_y=650, start_radius=125)
    $ _j601_verre_score = tq_progress

    if _j601_verre_score >= 0.82:
        think "Ma main part avant ma tête. Je redresse le verre ; quelques gouttes seulement tombent sur le sol."
        elias inquiet "Oh putain. Merci. C'était chaud, là. Encore..."
    elif _j601_verre_score >= 0.35:
        think "Trop tard. Le verre frappe la table ; ma manche arrête l'eau avant Mara."
        elias inquiet "Merde, merde. J'ai fait quoi, là ? C'est chaud."
        mara agace "Putain, je suis trempée Elias ! Tu pourrais faire gaffe un peu non ?!"
    else:
        think "Je tends le bras trop lentement. Le verre bascule entièrement."
        elias inquiet "Et merde. Fait chier, c'est chaud."
        mara colere "... J'ai tout pris sur la tronche ! Je vais finir par te tuer !"

    mara agace "Mais tu n'arrêtes pas de faire tout le temps tomber des trucs, c'est maladif ou quoi ?!"
    elias triste "J’ai pas—"

    mara "Kael m'a dit qu'hier ta maladresse t'a enfermé dans une salle. Aujourd'hui, tu viens directement m'agresser avec elle."

    elen inquiet "... C'est pas drôle. Il a pas fait exprès, enfin je crois pas..."
    elen joie "Faudrait être fou pour te rendre de mauvaise humeur dès le matin."

    mara "Je confirme. Faudrait être fou."

    elias inquiet "J'ai glissé. Je suis vraiment désolé Mara ! Vraiment désolé."

    mara neutre "Comme d'habitude : je suis toujours au mauvais endroit, au pire moment."

    elen neutre "Vous avez entendu Kami ? Enfin oui, évidemment, mais vous avez entendu comment elle parlait ? C'était TROOOOP chelou !"

    mara mefiant "Ouais. C'était pas son petit théâtre habituel. C'est vrai."

    lysa reflexion "Elle était beaucoup plus ... Expéditive. Comme si ça la saoulait de nous parler."

    elen taquin "Whaou ! Tu crois qu'elle nous fait une dépression ? Genre un Burn-Out ?!"

    lysa rire "Je crois pas que ce soit possible !"

    elias reflechit "Kami joue toujours un rôle. C'est son truc. En soi, elle nous imite."

    lysa blase "Ouais. Mais là c'était pas comme d'habitude."

    mara colere "Tu m'étonnes qu'elle était pas comme d'habitude. Elle bégayait ! D'où Kami bégaye d'abord !"

    lysa reflechit "Tu crois qu'il lui est arrivé quelque chose ?"

    mara mefiant "Non. Enfin… j'en sais rien. C'était bizarre. Même pour elle."

    noam reflechit "Ouais. On verra bien si ça continuera plus tard, mais je m'étais aussi fait la réflexion."

    "Nous avons chacun continué à manger, plus en silence, nos rations sèches et sans goût."
    think "Finalement, personne n'a parlé du vote. Personne n'a osé."
    think "Où alors, tout le monde sait que c'est inutile."

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

    window hide
    scene expression "images/background/cg/bg_cg035.png" at adaptive_fullscreen
    show expression Solid("#47b9d8", xsize=1920, ysize=4) as j601_tv_feed_line:
        ypos 148
    show expression Text("DIRECT // FRONTIÈRES DE LIMEN", size=54, color="#D9F6FF", font="fonts/Rajdhani-SemiBold.ttf") as j601_tv_feed_title:
        xalign 0.5
        ypos 62
    show expression Text("AFFLUENCE AUX POSTES DE CONTRÔLE  •  PASSAGE TOUJOURS INTERDIT", size=28, color="#FFCF70", font="fonts/Barlow-Light.ttf") as j601_tv_feed_alert:
        xalign 0.5
        ypos 930
    with Dissolve(0.25)
    window auto

    "La chaîne d'information s'ouvre sur une vue aérienne des frontières limenoises."
    "Des centaines de personnes se massent devant les postes de contrôle. Certaines portent des sacs. D'autres tiennent leurs enfants par la main."
    "Les barrières restent fermées. De l'autre côté, les gardes forment une ligne immobile."

    "JOURNALISTE — Depuis ce matin, les rassemblements se multiplient le long des principaux points de passage."
    "JOURNALISTE — Beaucoup espèrent que le vote du Conclave permettra une réouverture immédiate des frontières."

    "Une femme lève les yeux vers la caméra. Derrière elle, la foule avance d'un pas chaque fois qu'une rumeur traverse les rangs."
    "UNE FEMME — On ne demande pas un miracle. On veut juste pouvoir passer si le vote dit oui."

    think "Ils attendent déjà. Comme si notre vote était une promesse et pas une formalité condamnée d'avance."
    think "Sael votera contre. Mara aussi. Tous ces gens l'ignorent encore."

    "L'image saute. Le direct disparaît derrière un bandeau de programmes préenregistrés."
    think "Je coupe le son. La foule reste imprimée dans le noir de l'écran."

    window hide
    hide j601_tv_feed_title
    hide j601_tv_feed_alert
    hide j601_tv_feed_line
    with Dissolve(0.2)
    window auto
    return

label _6_0_1_TRANSITION_CONCLAVE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ current_period = "Après-midi"

    pause 0.6

    "Et puis enfin, l'heure du Conclave est arrivée."

    think "Nous nous sommes rassemblés sans parler. Sans même nous regarder."

    play sound "sfx/glitch_light.mp3"

    window hide
    show expression Solid("#000000") as j601_lights_out zorder 300
    with None
    pause 0.55
    show expression Solid("#000000") as j601_lights_out zorder 300:
        alpha 1.0
        linear 2.4 alpha 0.0
    pause 2.4
    hide j601_lights_out
    window auto

    think "Les lumières vibrent une seconde, puis reviennent."

    noam "Pourquoi rien ne va dans cette journée ?!"

    show screen kami_broadcast_ui

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Oh. Déjà en mouvement ? Il restait encore un peu de temps."
    pause 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with hpunch
    pause 0.5
    scene bg_diffusion_colere at adaptive_fullscreen
    kami "C’est bien. C’est très bien."
    scene bg_diffusion_professeur at adaptive_fullscreen
    kami "Nous pouvons… anticiper."
    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch
    kami "Le vote peut commencer plus tôt."
    kami "Immédiatement, même. Ça m'arrange beaucoup."

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.5

    think "Le couloir reprend comme si rien ne s'était passé. Puis je remarque qu'il manque quelqu'un."

    menu:
        "Sael ?":
            $ _j601_absent_pick = "sael"
        "Iris ?":
            $ _j601_absent_pick = "iris"
        "Elias ?":
            $ _j601_absent_pick = "elias"
        "Kael ?":
            $ _j601_absent_pick = "kael"

    if _j601_absent_pick == "sael":
        think "Sael. Oui. C'est elle. Où est-elle ? Elle était là il y a une seconde !"

        $ showGroup([
            ("sael", "neutre"),
            ("noam", "neutre"),
        ])

        "Sael est derrière le groupe, elle ne bouge plus. Elle fixe un angle vide du couloir."

        noam inquiet "Sael ?"
        think "Elle ne répond pas tout de suite."

        sael reflechit "... J'ai vu quelqu'un. Là-bas."

        think "Je regarde. Seulement le couloir vide."

        noam reflechit "Il n'y a personne. Enfin… je ne vois personne."

        sael triste "... Oui. Tu as sans doute raison…"

        hide sael with fade
        hide noam with fade

    else:
        think "Non. Ce n'est pas ça."
        "Je recompte tout le monde.."
        think "Ah si, tout le monde est bien là. Pourquoi j'ai eu cette impression tout à coup ?"

    noam "Bon, on y va. On va essayer de survivre à ce moment."

    jump _6_0_1_CONCLAVE_START

label _6_0_1_CONCLAVE_START:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_267
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate_low.mp3" fadein 1.5

    pause 0.8

    think "Nous entrons et prenons nos places sans ralentir."
    think "Nos corps connaissent déjà le chemin."

    $ showGroup([("ryn", "neutre", 0.2), ("iris", "fatigue", 0.5), ("sael", "neutre", 0.8)])

    think "Ryn s'assoit. Iris croise les bras. Sael regarde droit devant."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "... Ah oui. Vous voilà. Début du débat."

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Proposition : autoriser la libre circulation entre districts."

    scene bg_diffusion_taquin at adaptive_fullscreen

    kami "Vous connaissez déjà comment tout ça fonctionne. Je ne vais pas me répéter inutilement."

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Alors. Parlez. Débattez."

    pause 2.0

    "Personne ne parle. Pas une seule tentative."
    think "À quoi bon ...?"

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "... Intéressant"

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Vous souhaitez déjà sauter à la conclusion sans passer par le processus.."
    kami "Sur le principe, ça m'irait mais..."

    think "Sa voix bloque sur le mot."

    play sound "sfx/glitch_medium.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Corrigez."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Corrigez."
    kami "Corrigez."

    think "Le mot reste trop longtemps, comme si elle cherchait la suite."

    scene bg_diffusion_professeur at adaptive_fullscreen

    kami "Engagez-vous."
    kami "Débattez."
    kami "Simulez au moins."

    think "Toujours rien."

    $ showGroup([("ryn", "colere", 0.2), ("iris", "fatigue", 0.5), ("sael", "neutre", 0.8)])

    ryn colere "Putain mais qu'est-ce qui t'arrive ? De toute façon ça sert à rien de débattre ! On connaît déjà la fin !"

    iris colere "Pff, à quoi bon jouer son jeu. Tout ça ne servirait à rien."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen

    kami "..."

    pause 0.2

    play sound "sfx/glitch_heavy.mp3"

    scene bg_diffusion_einstein at adaptive_fullscreen with vpunch

    kami "Interaction insuffisante. Les gens n'aiment pas !"

    scene bg_diffusion_colere at adaptive_fullscreen

    kami "Ajustement en cours."

    think "Son image tremble plus fort, plus longtemps. Elle ne revient pas tout de suite."

    think "... Là. Ce n'est clairement pas normal."

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Maintenez le signal."

    pause 0.3

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
    kami ""

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
    scene black with dissolve

    $ _vote_result = renpy.call_screen("vote_screen")

    if _vote_result == "pour":
        scene Solid("#0AFF8844")
        with Dissolve(0.12)
    elif _vote_result == "contre":
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene Solid("#AAB0BF44")
        with Dissolve(0.12)

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

    hide sael

    think "C'est terminé."
    think "Mais rien n'est réglé."

    with moveinright

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
    iris colere "Et je veux que ce cirque s'arrête. Nous ne changerons rien tant que Kami sera là."

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

    call end_day("7") from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE

# total : 8m
# Total jour 0-6 : 1h49
