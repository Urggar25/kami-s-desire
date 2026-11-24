# 6_0_1.rpy
# Jour 6 - Branche statu quo post-accident café
# Style THL - version dialoguée, rythmée

default j601_border_news_seen = False
default j601_signal_stabilized = False
default j601_fracture_trace_saved = False
default j601_vote_pressure = "indecis"
default j601_vote_verification = False
default j601_iris_confiance = 0
default j601_repair_note = False
default j601_julian_echo = False
default j601_with_elen = False
default j601_julian_left_vote = False
default j601_hack_result = {}
default j601_hack_success = False
default j601_hack_rank = "D"

transform j601_sael_vote_strip:
    xalign 0.5
    yalign 0.5
    xysize (720, 1080)

# Brouillage indépendant du portrait de diffusion : ne modifie aucun asset Kami.
transform j601_kami_scanline:
    alpha 0.0
    pause 0.35
    alpha 0.70
    xoffset -18
    linear 0.07 xoffset 24
    alpha 0.0
    xoffset 0
    pause 1.1
    repeat

transform j601_kami_ghost:
    alpha 0.0
    pause 0.65
    alpha 0.55
    xoffset 24
    linear 0.06 xoffset -12
    alpha 0.0
    xoffset 0
    pause 2.0
    repeat

screen j601_kami_glitch():
    zorder 199
    # Stries CRT discontinues : aucun bouton, aucun blocage de l'interface.
    add Solid("#85faff99", xysize=(1920, 5)) xpos 0 ypos 198 at j601_kami_scanline
    add Solid("#ff5b9299", xysize=(1920, 8)) xpos 0 ypos 455 at j601_kami_ghost
    add Solid("#dffcff77", xysize=(1920, 3)) xpos 0 ypos 708 at j601_kami_scanline
    add Solid("#07131dcc", xysize=(1920, 12)) xpos 0 ypos 559 at j601_kami_ghost


label _6_0_1_REVEIL_CHAMBRE:

    $ elias_cafe_harness_enabled = True
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 6
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "low"
    $ j601_border_news_seen = False
    $ j601_signal_stabilized = False
    $ j601_fracture_trace_saved = False
    $ j601_vote_pressure = "indecis"
    $ j601_vote_verification = False
    $ j601_iris_confiance = 0
    $ j601_repair_note = False
    $ j601_julian_echo = False
    $ j601_with_elen = False
    $ j601_julian_left_vote = False

    $ blink()
    "Ma tablette est restée sur le bureau. L'icône de la messagerie clignote : Elias m'a écrit tard hier soir."
    if j50_observation_circuit_status == "secours_partiel":
        call messenger_play("j6_elias_secours", "elias", [("elias", "Le boitier a tenu ! Kael veut qd mm reverif les acces..."), ("elias", "Jme suis trouvé une tasse avc couvercle mdr. Enfin c gratuit ici donc bon"), ("noam", "Content que ça aille. Tu me dois un café, dans un gobelet fermé."), ("elias", "Tkt j'arrete PAS le café ! Juste d'le renverser sur les console 😂"), ("elias", "Jte dois un café, promis.")], objective_text="Lire les messages d'Elias", notify=False) from _call_j601_messenger_secours
    else:
        call messenger_play("j6_elias_panne", "elias", [("elias", "Kael a recup le boitier, la porte remarche !"), ("elias", "Mtn il veut que jnote tt ce que g touché... ca va etre LONG"), ("noam", "Tant mieux pour la porte. Tu me dois un café, et tu éviteras de le renverser celui-là."), ("elias", "Mdr tkt. Jvais continuer le café, mais loin des fils promis"), ("elias", "Enfin jvais essayer 😅")], objective_text="Lire les messages d'Elias", notify=False) from _call_j601_messenger_panne
    noam sourire "Il n'a visiblement pas perdu son sens des priorités."
    "Sur la tablette, une alerte m'annonce le vote à quatorze heures."
    "Libre circulation entre les districts."
    think "Sael ne changera pas d'avis. Ryn le sait. J'espère qu'ils ne vont pas passer tout le repas à se le rappeler."
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen j601_kami_glitch
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Debout, bande de pri... pri... privilégiés ! Dans quelques heures, vous déciderez si..."
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    kami "Si des millions de personnes ont le droit de rendre visite à leurs voisins !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à quatorze heures. Pas une minute en ret... en ret..."
    kami "Quatorze heures. Quatorze heures. Quatorze heures."
    $ bc_show("noam", "surpris")
    noam surpris "Kami ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    $ bc_hide()
    kami "Je vous rappelle que l'unanimité est... est..."
    play sound "audio/sfx_glitch.mp3"
    kami "Ah ! Bon ! Vous connaissez la suite, mes petits... mes petits..."
    "Sa voix grésille, puis la diffusion s'arrête au milieu d'un rire."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    noam inquiet "Elle avait pas l'air pressée. Elle avait surtout l'air... bizarre."
    "Je me prépare, vérifie ma tablette et sors de la chambre."
    $ current_scene_active = "_6_0_1_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    call KD_ROUTE_J6_ELEN from _call_optional_kd_route_j6_elen
    # Elen entraîne Noam : pas de navigation manuelle supplémentaire.
    $ current_scene_active = None
    jump _6_0_1_CAFETERIA

label _6_0_1_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_263
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2
    $ showGroup([
        ("elias", "fatigue"),
        ("mara", "neutre"),
        ("lysa", "blase"),
        ("iris", "fatigue"),
        ("sael", "neutre"),
        ("noam", "fatigue"),
    ])
    if j601_with_elen:
        $ showGroup([("elias", "fatigue"), ("mara", "neutre"), ("lysa", "blase"), ("iris", "fatigue"), ("sael", "neutre"), ("noam", "fatigue"), ("elen", "joie")])
        "Elen me tire jusqu'au comptoir. Goumi lève les yeux de ses plateaux."
        elen joie "Goumi ! Deux petits-déjeuners ! Et mets-lui quelque chose de bon, il a presque pas dormi !"
        goumi "Je vais faire au mieux avec le stock restant."
        elen content "Héhé, merci !"
        noam fatigue "Elen, je peux commander moi-même..."
        elen "Oui, oui. Mais là, je l'ai déjà fait pour toi ! Alors garde le sourire pour réussir !"
        "Elle récupère nos plateaux et m'accompagne jusqu'à la table."
    else:
        "Je prends ma ration auprès de Goumi et commence à manger. Quelques minutes plus tard, Elen arrive au comptoir."
        $ showGroup([("elias", "fatigue"), ("mara", "neutre"), ("lysa", "blase"), ("iris", "fatigue"), ("sael", "neutre"), ("noam", "fatigue"), ("elen", "joie")])
        elen joie "Goumi ! Tu me gardes un plateau ? J'ai faim !"
        goumi "Il reste votre ration, Elen."
        elen "Parfait !"
        "Elle rejoint la table avec son plateau."

    call show_custom_title("Un peu plus tard...")

    "Elen a déjà récupéré une boîte vide et un morceau de ficelle. Elias tient son gobelet le plus loin possible d'elle."
    elen sourire "Ne bouge plus. Je vais juste faire deux petits trous."
    elias inquiet "Mais pourquoi deux ?"
    elen "Pour la ficelle."
    elias "Quelle ficelle ?"
    mara taquin "Celle qui t'attachera les mains dans le dos, j'espère."
    elen colere "MARA !"
    noam sourire "Qu'est-ce que vous fabriquez ?"
    elias fatigue "Une invention qui devait empêcher mon café de tomber. Mais j'ai peu d'espoir..."
    elen joie "Noam ! Parfait ! Tiens ça."
    "Elle me tend le couvercle de sa boîte."
    noam inquiet "Attends, je viens juste de..."
    elen "Ça prend deux secondes."
    "Je prends le couvercle."
    iris blase "Ça fait huit minutes qu'elle dit ça."
    elen "Parce que vous n'arrêtez pas de m'interrompre !"
    lysa taquin "Je propose qu'on lui donne une heure et un budget. Ça lui fera une petite carrière."
    elen sourire "Merci !"
    lysa blase "Ce n'était pas un compliment."
    elen "Mais si ! Mais si ! Sois positive un peu !!"
    "Elias approche timidement son gobelet."
    elias "Et si ça bloque l'ouverture ? Je pourrai plus boire."
    mara taquin "Tu découvriras une autre forme d'hydratation : la prudence."
    elias "C'est pas drôle."
    mara "Un peu."
    noam "Pour une fois, je suis de son côté. Si on fabrique un gobelet qui empêche de boire, on a raté quelque chose."
    elen "Mais non, regarde."
    "Elle enfonce le couvercle. Le gobelet se déforme."
    elias peur "ELEN !"
    elen surpris "Ah."
    noam neutre "C'était l'étape de résistance des matériaux ?"
    elen "Bon. D'accord. Nouveau plan."
    "Elle récupère la boîte, s'assied et se met à déplier un autre morceau de carton."
    iris fatigue "Laisse-lui simplement une tasse sans couvercle. Et éloigne-la des consoles."
    elias gene "C'est ce que je fais !"
    "Elias pose son gobelet sur le plateau d'Elen."
    elen "Hé !"
    elias "C'est le point le plus éloigné de moi."
    "Même Sael sourit."
    "Mara récupère la ficelle, la boîte percée et deux petites attaches."
    mara sourire "Attends, attends. Le problème, c'est que ton truc tient pas. Il faut une sangle."
    elen surpris "Tu veux m'aider ?!"
    mara "Je veux surtout voir si ça marche. Passe-moi ça."
    "Elles bricolent côte à côte. Mara raccourcit les attaches, Elen noue une bande de tissu autour de la boîte."
    elias inquiet "Pourquoi vous mesurez mes épaules ?"
    mara taquin "Parce que c'est un collier. Bouge pas."
    elias "Un collier pour le café ?"
    elen joie "Voilà ! Tu passes la sangle, et le gobelet se glisse dans le support. Comme ça, tu gardes les mains libres !"
    noam inquiet "C'est pas un peu risqué de mettre du café brûlant là-dedans ?"
    mara "On fait l'essai à vide, évidemment. Je tiens à ce qu'Elias conserve sa peau."
    "Mara lui passe la sangle sur les épaules et ajuste le support contre son torse. Un gobelet vide tient enfin sans basculer."
    elen joie "ÇA MARCHE !"
    elias surpris "Hé... ça tient vraiment !"
    mara rire "Et regardez-moi ses PECS de ouf !"
    elias gene "MARA ! C'est le support qui fait ça !"
    noam sourire "T'es sûr ?"
    elias colere "Mais oui ! Arrêtez de regarder !"
    elen content "Je vais chercher un vrai couvercle ! Attendez, bougez pas !"
    "Elle revient avec un couvercle percé et une paille. Mara vérifie les attaches avant d'y glisser le café, déjà tiède, d'Elias."
    mara "Voilà. Essaie de marcher, pour voir."
    "Elias fait deux pas. Le gobelet reste en place contre son torse. Il se penche sur la paille et boit."
    elias content "Oh putain... ça marche !"
    elen joie "JE LE SAVAIS !"
    noam sourire "On va vraiment le voir se promener avec ça toute la journée ?"
    mara taquin "Vu le temps qu'on y a passé ? J'espère bien."
    "Elias essaie de se retourner une seconde fois. Pas une goutte ne bouge. Il sourit malgré lui."

    "Goumi apporte une dernière petite assiette de fruits en conserve. Elen tend aussitôt la main."
    elen joie "Oh ! Il en restait !"
    goumi "Pour la table. Pas uniquement pour vous."
    elen surpris "Oui, oui, je partage !"
    mara taquin "Tu as déjà pris la moitié."
    elen content "Parce que je distribue ! Tiens, Elias !"
    elias sourire "Merci !"
    iris fatigue "On pourrait finir un repas sans opération de sauvetage, aujourd'hui ?"

    "Elen lève les yeux vers l'écran éteint au-dessus du comptoir."
    elen neutre "Au fait. La diffusion de ce matin..."
    iris reflechit "Elle a répété l'heure trois fois. Et sa voix a sauté. Vous avez entendu ?"
    elen "Oui ! Justement !"
    iris inquiet "Mais c'est impossible ! Enfin, pas impossible d'avoir une panne de haut-parleur. Mais Kami..."
    lysa taquin "Elle a peut-être avalé le café d'Elias."
    iris colere "Non ! IM-PO-SSI-BLE ! Vous croyez vraiment qu'une tasse renversée sur une console va casser une IA pareille ?!"
    elias gene "J'allais demander à Kael pour la connexion..."
    iris "Kami gère le monde entier ! Elle peut pas se mettre à bégayer parce qu'Elias a mouillé trois câbles ! Ça n'a aucun sens !"
    mara sourire "C'est peut-être pour ça qu'on lui demande de faire la vaisselle."
    iris colere "Mara ! Je suis sérieuse !"
    noam inquiet "Tu penses qu'elle a un problème ?"
    iris reflechit "Je sais pas. J'aimerais voir ses diagnostics. Ses journaux, ses sauvegardes, tout !"
    elen sourire "Tu pourrais lui demander !"
    iris "J'ai essayé. Elle n'a pas répondu à la question."
    "Iris fixe l'écran éteint, oubliant jusqu'à sa ration."
    noam neutre "On n'a pas de diagnostic. On peut attendre avant de s'engueuler."
    sael neutre "Oui."
    "Sael reprend son repas. Elle n'a pas touché au sujet du vote."
    elen "Et... pour cet après-midi ?"
    sael mefiant "Je sais, Elen."
    elen "Je demandais si on avait le droit de manger ensemble après."
    sael neutre "Ah."
    elen "Parce que j'aimerais bien qu'on mange ensemble, même si le vote se passe mal."
    sael "Je viendrai, si j'ai faim."
    mara taquin "Voilà un programme politique que je peux soutenir."
    elen "Je prends note. C'est déjà une personne."
    "Elias récupère discrètement son gobelet."
    elen "EH ! Le couvercle !"
    elias "Je vais juste boire avant la deuxième version."
    elen "D'accord, mais ne le renverse pas."
    elias fatigue "..."
    "Je lui adresse un regard compatissant."

    "L'écran du comptoir s'allume. Une carte de Limen apparaît."
    "Goumi s'arrête au milieu de son trajet. Les couverts continuent de tinter quelques secondes."
    call _6_0_1_TV_FRONTIERES from _call_6_0_1_TV_FRONTIERES_matinale
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    $ showGroup([("sael", "neutre"), ("elen", "triste"), ("mara", "neutre"), ("noam", "inquiet"), ("elias", "fatigue"), ("iris", "inquiet"), ("lysa", "blase")])
    sael neutre "Moi non plus."
    mara fatigue "Moi non plus, franchement."
    elias fatigue "Ouais... pareil."
    lysa blase "Je vais laisser mon plateau."
    noam "Je crois qu'on a tous compris."
    "Sael ramasse son plateau et se lève sans rien dire."
    elen joie "BON ! GOUMI ! TU PEUX NOUS REMETTRE UNE ASSIETTE ?!"
    elen sourire "Allez, on va pas rester avec ces têtes-là toute la journée !"
    mara reflechit "Tu vas vraiment remanger ?"
    elen "Si vous mangez aussi !"
    goumi "Je peux vous proposer les mêmes rations."
    elen joie "Parfait !"
    "Son sourire tient un peu trop longtemps, mais personne ne la contredit. Iris, elle, continue de regarder l'écran éteint."
    "Elias garde le support vide contre son torse. Même après le reportage, il semble réticent à l'enlever."
    jump _6_0_1_TEMPS_LIBRE

label _6_0_1_TEMPS_LIBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_264
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Fin de matinée"
    think "Le Conclave est à quatorze heures. Il me reste un peu de temps."
    call START_FREE_TIME("_6_0_1_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_6_0_1

label _6_0_1_TV_FRONTIERES:

    $ j601_border_news_seen = True
    $ unlock_gallery_image("bg_cg035")
    call kd_news_open(_("LIMEN 24"), _("LIBRE CIRCULATION"), _("ÉDITION SPÉCIALE")) from _call_kd_news_open_j601
    scene bg_cg035 at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("POSTE-FRONTIÈRE DE LIMEN"), _("Des familles dans l’attente du vote"), (_("Le Conclave se prononce cet après-midi."), _("Les restrictions de circulation restent en vigueur."), _("Aucune ouverture des frontières n’est annoncée.")))
    with Dissolve(0.25)
    window auto
    "À l'écran, des gens se sont installés devant un poste-frontière. Certains ont amené des chaises pliantes. Un enfant joue avec le ruban qui entoure une valise."
    show screen kd_news_broadcast(_("LIMEN 24"), _("POSTE-FRONTIÈRE DE LIMEN"), _("Des familles dans l’attente du vote"), (_("Le Conclave se prononce cet après-midi."), _("Les restrictions de circulation restent en vigueur."), _("Aucune ouverture des frontières n’est annoncée.")), _("TÉMOIGNAGE"), _("Une femme attend son frère"))
    "JOURNALISTE — Vous êtes là depuis ce matin ?"
    "UNE FEMME — Depuis hier soir, moi. Ma sœur me dit toujours que je suis en avance."
    "JOURNALISTE — Vous attendez votre sœur ?"
    "UNE FEMME — Mon frère. Ma sœur est morte il y a six ans."
    "Le journaliste baisse son micro."
    "UNE FEMME — C'est bon, vous pouvez filmer. Lui, il déteste le thé. Alors chaque année je lui apporte du thé pour son anniversaire. Il râle, mais il le boit."
    "JOURNALISTE — Et là ?"
    "UNE FEMME — Là, j'ai encore une boîte. Je voulais lui donner en main propre."
    "Elle ouvre son sac pour montrer le paquet. L'emballage est abîmé."
    "Une autre personne traverse le cadre en portant une chaise."
    show screen kd_news_broadcast(_("LIMEN 24"), _("POSTE-FRONTIÈRE DE LIMEN"), _("Des familles dans l’attente du vote"), (_("Le Conclave se prononce cet après-midi."), _("Les restrictions de circulation restent en vigueur."), _("Aucune ouverture des frontières n’est annoncée.")), _("SUR PLACE"), _("Des proches attendent devant les barrières"))
    "UN HOMME — Vous pouvez pousser votre matériel ? Ma mère n'arrive pas à passer."
    "JOURNALISTE — Excusez-moi. Madame, vous aussi, vous attendez quelqu'un ?"
    "UNE VIEILLE FEMME — Non, j'accompagne mon fils. Il s'est fait une idée et maintenant il veut rester là toute la journée."
    "UN HOMME — Maman..."
    "UNE VIEILLE FEMME — Quoi ? C'est vrai."
    "Le journaliste se décale. Au fond, des agents surveillent les barrières sans parler."
    show screen kd_news_broadcast(_("LIMEN 24"), _("POSTE-FRONTIÈRE DE LIMEN"), _("Le Conclave doit se prononcer"), (_("Le Conclave se prononce cet après-midi."), _("Les restrictions de circulation restent en vigueur."), _("Aucune ouverture des frontières n’est annoncée.")))
    "JOURNALISTE — La décision du Conclave est attendue cet après-midi. Pour le moment, aucune ouverture n'est annoncée."
    "Une petite fille demande à son père s'ils peuvent rentrer manger. Il lui promet d'y aller bientôt."
    "L'image change avant qu'on entende sa réponse."
    call kd_news_close from _call_kd_news_close_j601
    return

label _6_0_1_TRANSITION_CONCLAVE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    $ current_period = "Après-midi"
    $ showGroup([("elen", "neutre", 0.25), ("tomas", "inquiet", 0.60), ("noam", "neutre", 0.85)])
    "Tomas est planté au milieu du couloir, tablette à la main."
    tomas inquiet "Non, mais je suis certain d'avoir réglé l'alarme pour treize heures trente."
    elen "Mais... Tu l'as réglée pour treize heures trente demain."
    tomas surpris "Quoi ?"
    elen sourire "Regarde la date."
    tomas gene "Ah. Justement. Il ne faut JA-JAMAIS être en retard."
    "Je consulte ma tablette : 13 h 50 apparaît à la place de 14 h."
    noam inquiet "Elen, ton invitation indique quelle heure ?"
    elen "Quatorze heures."
    tomas "Moi, treize heures cinquante."
    "Elen approche sa tablette de la mienne, comme si cela pouvait les mettre d'accord."
    elen "Attends. La mienne vient de changer."
    "L'écran mural s'allume sans sonnerie. Le portrait de Kami apparaît, avec une bande d'image décalée sur son visage."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Eh bien, quelle jolie réunion ! Vous avez l'heure, vous avez vos jambes, alors utilisez-les !"
    $ bc_show("tomas", "inquiet")
    tomas inquiet "Kami, certaines tablettes indiquent treize heures cinquante et d'autres quatorze heures."
    $ bc_hide()
    kami "Je le sais, Tomas."
    $ bc_show("noam", "neutre")
    noam "Tu peux nous dire quel horaire est le bon ?"
    $ bc_hide()
    kami "Bien sûr ! Bien... sûr."
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    kami "Venez main... maintenant."
    $ bc_show("elen", "neutre")
    elen "Et pourquoi ça a changé ?"
    $ bc_hide()
    kami "Parce que j'en ai... j'en ai décidé ainsi, évidemment ! Tu veux aussi un justificatif si... signé ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous êtes attendus au Conclave. Merci. Mer... ci."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 0.9
    tomas "Bon. J'ai encore une alarme à quatorze heures."
    elen "Garde-la. On verra si elle sonne."
    "Il la désactive tout de même."
    noam neutre "Allez. Si on arrive en avance, Julian pourra nous faire un discours d'accueil."
    elen inquiet "Tu voulais nous rassurer ?"
    "Au croisement, Ryn et Sael arrivent de deux directions opposées. Ils se laissent passer sans se regarder."
    "Tomas accélère un peu. Personne ne le lui fait remarquer."
    jump _6_0_1_CONCLAVE_START

label _6_0_1_CONCLAVE_START:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_267
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_6_0_1

    "Le débat commence avant même que tout le monde ait atteint sa chaise. Ryn tient sa tablette à bout de bras devant Sael ; Mara essaie de l'écarter du passage."
    $ showGroup([("ryn", "colere"), ("sael", "mefiant"), ("mara", "agace"), ("julian", "inquiet"), ("lysa", "blase"), ("tomas", "inquiet"), ("noam", "neutre"), ("elen", "inquiet"), ("iris", "reflechit")])
    ryn colere "Lis ça ! Ils continuent de s'entasser en espérant pouvoir passer la frontière !"
    sael mefiant "..."
    ryn "Ils vont encore passer la nuit dehors !"
    mara agace "Baissez d'un ton ! On entend plus rien !"
    julian inquiet "Je vous demanderais de prendre place rapidement, s'il vous plaît."
    lysa blase "Julian, personne ne t'écoute."
    julian "Justement !"
    "Une tablette tombe sur la table. Tomas se baisse pour la ramasser pendant que Ryn cherche Sael du regard."
    tomas inquiet "Attention, le coin est fissuré..."
    ryn "J'en ai rien à foutre du coin !"
    elen inquiet "Ryn ! Arrête, s'il te plaît !"
    iris reflechit "Quelqu'un a remarqué que l'écran central affiche deux horaires différents ?"
    mara "Pas maintenant, Iris !"
    iris "Si. Maintenant. On nous demande de voter avec ce truc !"
    iris colere "Alors que rien ne va !"
    "Mara s'interrompt et regarde brièvement l'écran. L'heure saute d'une minute, puis revient."
    mara agace "Putain... C'est quoi encore, ça ?"
    julian "Bon. Si je pouvais au moins commencer..."
    lysa "Assieds-toi, Julian."
    "Julian ouvre la bouche pour protester, puis finit par s'asseoir."
    if j50_julian_relation >= 1:
        julian sourire "Noam. Tu veux faire mon introduction, peut-être ?"
        noam sourire "Je préfère laisser les professionnels travailler."
        julian taquin "Très bien. Quelle sagesse."
        $ j601_julian_echo = True
    elif j50_julian_relation < 0:
        julian neutre "Je suppose que Noam va encore trouver quelque chose à redire."
        noam neutre "Je n'ai encore rien dit."
        julian "Je prends de l'avance."
    else:
        julian neutre "Bon. Je vais faire court."
        lysa blase "On aimerait voir ça."
    elen inquiet "S'il vous plaît. On peut commencer avant de se chamailler ?"
    $ showGroup([("ryn", "neutre", 0.10), ("sael", "neutre", 0.40), ("elen", "inquiet", 0.70), ("nyra", "neutre", 1.00)])
    ryn neutre "Sael. Tu m'as dit non hier."
    sael "Oui."
    ryn "Tu me le dirais encore aujourd'hui ?"
    sael "Oui. Je te l'ai dit, je ne changerai pas d'avis."
    ryn "T'es... T'es sérieuse ?! Putain !"
    "Il s'assied. Elen regarde tour à tour Ryn et Sael."
    elen inquiet "C'est... tout ?"
    ryn neutre "Qu'est-ce que tu veux que je dise ?"
    elen "Je ne sais pas. Quelque chose."
    ryn colere "Hier, je lui ai crié dessus. Ça n'a servi à rien."
    sael mefiant "Non, ça c'est sûr."
    ryn "Alors... Fais chier !"
    "Sael passe le doigt sur le bord de sa tablette."
    ryn neutre "Tu crois vraiment que les gens de ton village vont mieux dormir si on maintient les frontières ?"
    sael "..."
    ryn "Et les gens qu'on laisse dehors ?"
    sael "On trouvera toujours l'herbe plus verte ailleurs. Est-ce que ça veut dire qu'il faut tout abandonner ?"
    ryn "Je ne t'ai pas demandé ça..."
    sael colere "Si, c'est exactement ça le problème. Changer de district quand ça va mal, ça revient à fuir !"
    ryn "Tu n'as pas besoin d'être agressive."
    sael colere "Pardon ?! Tu es sérieux ?"
    "Ryn se rend compte de ce qu'il vient de dire. Il se frotte le front."
    ryn triste "Non. Désolé. J'aurais pas dû dire ça."
    "Sael lui laisse quelques secondes."
    sael neutre "Je ne suis même pas sûre que tu veuilles vraiment comprendre."
    ryn triste "... Et toi... Tu comprends que ces frontières sont la cause de la mort de milliers de gens chaque année ?!"
    sael "Oui. Je le sais. Vous, les Gardiens, vous êtes là pour empêcher ça et pour faire respecter les Commandements."
    ryn reflechit "... Pour faire respecter les Commandements ?! T'as craqué ou quoi !"
    ryn colere "On n'en a rien à foutre des Commandements, on veut juste pas que les gens meurent en essayant de traverser !"
    sael mefiant "Et donc tu fais appliquer les Commandements."
    ryn "... Putain ! Alors tu proposes quoi, hein ?! De ne rien changer ?!"
    "Son poing s'abat sur la table. Il regarde sa propre main, contrarié d'avoir recommencé."
    elen triste "Tu... Tu ne veux pas que les familles séparées puissent se rejoindre ?"
    sael neutre "Ce n'est pas le débat. On peut toujours demander des dérogations pour traverser..."
    nyra reflechit "C'est possible mais... Les dérogations prennent parfois plusieurs mois."
    $ showGroup([("mara", "neutre"), ("ryn", "colere"), ("sael", "neutre"), ("iris", "reflechit"), ("noam", "inquiet"), ("nyra", "raison"), ("kael", "reflechit"), ("elen", "inquiet")])
    mara neutre "Ce qui me gêne, c'est le mot « libre ». On enlève les interdictions, mais qui surveille les routes le lendemain ?"
    ryn "Tu crois que Kami n'a pas les moyens de tout surveiller ? Elle surveille déjà le monde entier !"
    mara "Comme d'hab, on dépend d'elle quoi..."
    ryn colere "Tu as une meilleure idée ?"
    sael reflechit "Imaginons, on ouvre les frontières."
    elen joie "Hein ?! T'as changé d'avis ?!"
    nyra reflechit "Ecoute-la jusqu'au bout !"
    sael "... Demain, cinquante personnes arrivent dans mon village. On n'a pas assez de logements, pas assez de nourriture et personne pour assurer leur sécurité. Je fais quoi ?"
    sael colere "Je te rappelle que chez nous, on a pas de bons de rationnement. On a pas de distribution de nourriture."
    sael triste "On fait tout nous-mêmes. On produit nous-mêmes. On récolte nous-mêmes."
    sael reflechit "Si le nombre de gens dans le village change trop vite, soit il n'y aura plus assez de bras pour tout faire, soit il y aura trop de bouches à nourrir."
    sael colere "Alors comment on fait ? Tu crois qu'on peut s'en sortir si les jeunes s'en vont ailleurs en espérant pouvoir mieux vivre ? Ou si d'autres gens arrivent trop nombreux dans le village ?"
    ryn reflechit "..."
    ryn colere "Mais j'en sais rien, moi ! J'ai jamais dit qu'il fallait envoyer tout le monde dans ton village !"
    elias triste "C'est pas évident votre truc, là."
    nyra "Attends, Sael. Les jeunes peuvent déjà quitter ton village pour aller ailleurs dans Limen, non ?"
    sael triste "Certains sont déjà partis et on en a payé les conséquences."
    sael "Alors oui, en tant que cheffe de village, je fais tout pour les inciter à rester."

    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.9
    kami "Vous avez l'air particulièrement... particulièrement en forme ! J'avais prévu un discours d'ouverture, mais je vais... je vais..."
    $ bc_show("julian", "taquin")
    julian taquin "J'avais justement préparé..."
    $ bc_hide()
    kami "Non, Julian. Non, Julian."
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    "Sa voix se répète avec un décalage. Personne ne rit."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le texte soumis au vote porte sur la libre circulation des personnes entre les districts. Les conditions de son adoption restent inchangées : l'unanimité."
    kami "Vous pouvez poursuivre vos échanges. Je... je lancerai le scrutin quand..."
    play sound "audio/sfx_glitch.mp3"
    "L'image se fige, puis disparaît."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("mara", "mefiant"), ("ryn", "colere"), ("sael", "neutre"), ("iris", "inquiet"), ("nyra", "reflechit"), ("kael", "reflechit"), ("elen", "inquiet"), ("lysa", "blase"), ("noam", "surpris")])
    iris inquiet "Elle a recommencé. C'est exactement ce qu'elle a fait ce matin."
    kael "Je vais vérifier le flux."
    iris "Pas seulement le flux ! Elle a répété Julian mot pour mot, avec le même délai !"
    mara "Iris, on a déjà compris qu'elle déconne !"
    iris colere "Et moi, je veux comprendre POURQUOI !"

    "Iris ne se rassied pas. Elle s'approche de l'écran noir, comme si Kami pouvait encore la voir."
    iris reflechit "Attendez. Quand elle a dit « Non, Julian », elle a répété la même chose deux fois. Exactement pareil."
    mara agace "Oui, on l'a tous entendue."
    iris "Non, vous l'avez entendue bégayer. Moi je vous dis que ce n'est pas un bégaiement."
    kael reflechit "Qu'est-ce que tu veux dire ?"
    iris "Sa voix ne se fabrique pas comme la nôtre. Chaque réponse dépend de ce qu'elle entend. Là, la deuxième phrase est partie sans qu'elle nous écoute."
    elias inquiet "Bon... ça peut être juste un problème de son, non ?"
    iris "Un haut-parleur qui saute ne fabrique pas une deuxième réponse, Elias."
    elias "D'accord. Je demandais."
    tomas inquiet "Mais on peut vérifier ? Il doit y avoir un journal, quelque part."
    iris "C'est justement ce que je demande !"
    "Elle cherche une option sur sa tablette et retourne l'écran vers Kael."
    iris "Là. Les diagnostics de diffusion sont verrouillés. Depuis quand ils sont verrouillés ?"
    kael "Ils l'ont toujours été."
    iris "Pas les heures de réponse."
    kael "Les heures, non. Mais on ne peut pas ouvrir son noyau."
    iris colere "Je ne veux pas ouvrir son noyau ! Je veux savoir si elle comprend ce qu'on lui dit !"
    "Elias éloigne son gobelet du bord de la table."
    elias "Pourquoi tu dis ça comme si elle risquait de ne plus nous comprendre ?"
    iris "Parce que c'est peut-être ce qui est en train d'arriver !"
    tomas "Attends, attends. Si elle comprend plus, elle peut encore gérer les Commandements ?"
    kael "On n'en sait rien."
    tomas inquiet "Et les portes ? Et l'air ?"
    mara "Tomas, elle ne va pas couper l'air parce qu'elle a raté une phrase."
    tomas "Je sais pas ! Tu sais, toi ?"
    "Mara n'a pas de réponse. Pour une fois, personne ne plaisante."
    ryn desaccord "Vous pensez vraiment qu'elle va tomber en panne pendant le vote ?"
    iris "Je pense qu'elle EST déjà en panne !"
    nyra reflechit "Ce n'est pas forcément la même chose. Les commandes locales peuvent continuer à fonctionner."
    iris "Oui. Ou on peut avoir quelque chose qui répond à sa place."
    elias peur "Quoi ?"
    iris "Je n'ai pas dit que c'était le cas. J'ai dit que c'était possible."
    elias "C'est pas rassurant, la différence."
    "Tomas attrape sa tablette. Ses doigts glissent une première fois sur l'écran."
    tomas inquiet "Il y a un bouton d'urgence, non ? Un moyen de prévenir quelqu'un sur Terre ?"
    kael "Si le canal extérieur fonctionne. Elias, vérifie les relais sans rien modifier."
    elias "Moi ? Maintenant ?"
    kael "Tu sais lire un état de connexion."
    elias "Ouais. Lire, oui."
    "Elias ouvre l'outil. Un petit bip retentit et il sursaute si fort que sa tablette manque de tomber."
    elias "Putain !"
    lysa neutre "C'était ta tablette."
    elias "J'AI VU !"
    "L'écran principal s'allume sans signal d'annonce. Le visage de Kami apparaît."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.7
    kami "Quelle ambiance ! Vous m'avez manqué pendant ces... ces trente secondes."
    $ bc_show("iris", "colere")
    iris colere "Kami. Arrête de faire des blagues. Écoute-moi."
    $ bc_hide()
    kami "Je t'écoute, Iris. Comme toujours."
    $ bc_show("iris", "inquiet")
    iris "Dis-moi ce que tu viens de faire."
    $ bc_hide()
    kami "Je suis intervenue dans une conversation. Quelle question étrange."
    $ bc_show("iris", "colere")
    iris "Non. Pourquoi ta voix s'est répétée ?"
    $ bc_hide()
    kami "Elle ne s'est pas répétée."
    $ bc_show("iris", "inquiet")
    iris "Si. Tu as dit deux fois la même phrase."
    $ bc_hide()
    kami "Je ne dis jamais deux fois la même phrase."
    $ bc_show("julian", "agace")
    julian "Ça, c'est manifestement faux."
    $ bc_hide()
    kami "Je ne dis jamais deux fois la même phrase."
    "Julian cesse de sourire."
    $ bc_show("iris", "peur")
    iris "Vous avez entendu ? Elle vient encore de le faire."
    $ bc_hide()
    kami "Je ne dis jamais deux fois la même phrase."
    $ bc_show("tomas", "peur")
    tomas "Mais pourquoi elle continue ?"
    $ bc_hide()
    kami "Tout va bien, Tomas."
    $ bc_show("tomas", "inquiet")
    tomas "Je t'ai rien demandé !"
    $ bc_hide()
    kami "Tout va bien, Tomas."
    $ bc_show("elias", "peur")
    elias "Kael. Kael, moi je veux plus toucher à rien."
    $ bc_hide()
    kami "Elias, tu peux continuer ton travail."
    $ bc_show("elias", "panique")
    elias "NON ! Non, je préfère pas !"
    $ bc_hide()
    kami "Je plaisantais."
    "Iris se rapproche encore de l'écran. Elle parle maintenant beaucoup moins fort."
    $ bc_show("iris", "inquiet")
    iris "Kami, regarde-moi. Tu sais où tu es ?"
    $ bc_hide()
    kami "Partout, Iris. Tu connais la réponse."
    $ bc_show("iris", "reflechit")
    iris "D'accord. Et nous, où on est ?"
    $ bc_hide()
    kami "Au Conclave. Il est presque quatorze heures."
    $ bc_show("iris", "inquiet")
    iris "Bien. Maintenant, dis-moi pourquoi tu répètes..."
    $ bc_hide()
    kami "Non."
    "Iris se fige."
    $ bc_show("iris", "inquiet")
    iris "Non, quoi ?"
    $ bc_hide()
    kami "Pas ça."
    $ bc_show("noam", "surpris")
    noam surpris "Tu parles à Iris ?"
    $ bc_hide()
    kami "N'y touche pas."
    $ bc_show("mara", "mefiant")
    mara "À quoi ?"
    $ bc_hide()
    kami "J'ai dit : n'y touche pas."
    $ bc_show("elias", "panique")
    elias "J'ai rien touché ! Je vous jure !"
    $ bc_hide()
    kami "PAS TOI."
    "Le son sature si fort que Tomas se bouche les oreilles. La bouche de Kami reste ouverte une seconde, sans aucun bruit."
    $ bc_show("tomas", "peur")
    tomas "Elle vient de parler à qui, là ?"
    $ bc_hide()
    kami "Je... Pardon. Un problème de communication."
    $ bc_show("noam", "inquiet")
    noam inquiet "Kami, tu parles à quelqu'un dans cette salle ?"
    $ bc_hide()
    kami "Je vous parle à tous, voyons."
    "Je regarde Kael, puis Elias. Ils ont chacun une tablette ouverte. Peut-être qu'elle leur reproche une manipulation."
    $ bc_show("kael", "reflechit")
    kael "Je ne fais rien, Kami. Je regarde seulement les états du réseau."
    $ bc_hide()
    kami "Je sais, Kael."
    $ bc_show("iris", "colere")
    iris "Alors dis-nous à qui tu viens de dire d'arrêter !"
    $ bc_hide()
    "Le sourire de Kami tremble. Quand il revient, il n'a plus tout à fait la même forme."
    kami "Personne. Il n'y a personne."
    $ bc_show("iris", "peur")
    iris "Kami..."
    $ bc_hide()
    kami "Je vous rappelle que le scrutin doit commencer à quatorze heures."
    $ bc_show("nyra", "raison")
    nyra "Nous n'avons reçu aucune confirmation que le canal fonctionne normalement."
    $ bc_hide()
    kami "La procédure est parfaitement sécurisée."
    $ bc_show("nyra", "reflechit")
    nyra "Ce n'est pas une confirmation."
    $ bc_hide()
    kami "La procédure est parfaitement sécurisée."
    $ bc_show("tomas", "peur")
    tomas "Je veux pas voter avec ça !"
    $ bc_hide()
    kami "Bien sûr que si, Tomas. Le vote est obligatoire."
    $ bc_show("tomas", "inquiet")
    tomas "Tu vois ?! Elle vient de décider à ma place !"
    $ bc_hide()
    kami "Je n'ai rien décidé à ta place."
    "Les haut-parleurs produisent un bruit sec, comme si quelqu'un avait arraché une prise."
    kami "Non... Non ! Arrête ! Ne fais pas ça !"
    $ bc_show("noam", "peur")
    noam peur "C'est nous que tu menaces ?"
    $ bc_hide()
    kami "Je... Je ne..."
    $ bc_show("iris", "colere")
    iris colere "Kami, réponds-moi !"
    $ bc_hide()
    scene bg_diffusion_professeur at adaptive_fullscreen with hpunch
    kami "Ouverture anticipée du scrutin. Veuillez valider vos bulletins."
    play sound "audio/sfx_kami_alert.wav"
    $ bc_show("elen", "peur")
    elen peur "Mais on a même pas fini de parler !"
    $ bc_hide()
    kami "Validation automatique dans..."
    $ bc_show("kael", "inquiet")
    kael "Personne ne touche aux boutons !"
    $ bc_hide()
    kami "Dans... dans..."
    $ bc_show("iris", "peur")
    iris "C'est pas elle. Je sais pas ce que c'est, mais c'est pas elle qui veut voter !"
    $ bc_hide()
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    "Le visage de Kami se découpe en bandes. Sa voix continue pendant un instant, mais les mots sont impossibles à distinguer."
    "Puis l'écran devient noir."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("mara", "colere"), ("ryn", "inquiet"), ("sael", "mefiant"), ("iris", "peur"), ("nyra", "raison"), ("kael", "inquiet"), ("elen", "peur"), ("elias", "inquiet"), ("noam", "peur")])
    stop music fadeout 0.25
    "Les lumières restent allumées. Le ventilateur au-dessus de la table continue de tourner."
    "Puis les douze tablettes vibrent ensemble."
    elias peur "Oh non."
    nyra inquiet "Personne ne valide rien."
    jump _6_0_1_SIGNAL_INSTABLE

label _6_0_1_SIGNAL_INSTABLE:

    play sound "audio/sfx_glitch.mp3"
    "Les écrans affichent le dossier du vote. Le texte apparaît puis disparaît au moment où je tente de le lire."
    "Sur celui de Tomas, un cercle tourne sans fin."
    tomas inquiet "Ça ne charge pas."
    elias inquiet "Le mien non plus."
    kael reflechit "Ne touchez à rien. Je vais regarder les commandes locales."
    "L'écran principal se rallume."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5
    kami "Merci de votre patience ! Un simple ajustement de connexion. Ça arrive même aux meilleurs."
    $ bc_show("julian", "taquin")
    julian taquin "Tu vas nous dire qu'on doit redémarrer la station ?"
    $ bc_hide()
    kami "Ha ha ! Très drôle, Julian."
    $ bc_show("julian", "neutre")
    julian "Je n'essayais pas vraiment..."
    iris reflechit "Elle peut répondre. C'est déjà bon signe."
    nyra reflechit "Kami, peux-tu afficher le même texte sur nos douze tablettes ? Sans lancer le scrutin."
    $ bc_hide()
    kami "Bien sûr !"
    "L'écran de Nyra reste vide."
    $ bc_show("nyra", "neutre")
    nyra "Je n'ai toujours rien."
    $ bc_hide()
    kami "Tout est affiché."
    $ bc_show("nyra", "neutre")
    nyra "Non."
    $ bc_hide()
    kami "Tout est affiché."
    "Nyra retourne sa tablette pour la montrer à l'écran."
    $ bc_show("nyra", "neutre")
    nyra "Regarde."
    $ bc_hide()
    kami "Je regarde."
    "Iris se lève."
    $ bc_show("iris", "inquiet")
    iris inquiet "Kami, arrête de répondre comme ça. Vérifie le canal avant de continuer."
    $ bc_hide()
    kami "Je n'ai pas besoin de..."
    pause 0.4
    kami "De..."
    "Le sourire de Kami se contracte. Le bord de son visage reste immobile alors que sa bouche continue de bouger."
    kami "Je n'ai pas besoin de vérification. Je suis opérationnelle."
    $ bc_show("iris", "colere")
    iris colere "Non ! Tu viens de bloquer sur une phrase ! Ça n'arrive pas à une IA comme toi !"
    noam inquiet "Iris, elle t'entend."
    iris "J'espère bien ! Je veux qu'elle me dise ce qui se passe, pas qu'elle récite une réponse toute faite !"
    "Kami ouvre la bouche pour lui répondre."
    "Ce qui sort des haut-parleurs n'a rien à voir."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    $ bc_hide()
    kami "Ouverture anticipée du scrutin. Veuillez valider vos bulletins."
    play sound "audio/sfx_kami_alert.wav"
    "Sur ma tablette, les boutons POUR et CONTRE s'allument. Ils clignotent."
    $ bc_show("tomas", "surpris")
    tomas surpris "Hein ? Déjà ?"
    nyra inquiet "Personne ne touche à rien !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    $ bc_hide()
    kami "Ha ! Non, non, non. C'était une blague. Une petite blague."
    $ bc_show("julian", "neutre")
    julian neutre "Une blague."
    $ bc_hide()
    kami "Une excellente blague, Julian."
    $ bc_show("julian", "neutre")
    julian "Je ne l'ai pas trouvée excellente."
    lysa blase "Personne ne l'a trouvée excellente."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("mara", "mefiant"), ("ryn", "colere"), ("sael", "mefiant"), ("iris", "peur"), ("nyra", "inquiet"), ("kael", "reflechit"), ("elias", "inquiet"), ("lysa", "blase"), ("noam", "inquiet")])
    kael reflechit "Elias. Tu vois ce que je vois ?"
    elias inquiet "Deux signatures sur le canal de diffusion. Une à elle. L'autre..."
    elias "L'autre, je sais pas."
    mara colere "Comment ça, tu sais pas ?! C'est ton boulot de savoir !"
    elias panique "Mon boulot, c'est de réparer des pompes, Mara !"
    "Iris n'a pas bougé depuis l'annonce."
    iris peur "Il y a quelqu'un d'autre. Dans son canal."
    "Elle le dit presque tout bas. Personne ne lui répond tout de suite."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quelqu'un d'autre ? Dans MON système ?"
    kami "Elias, mon chou. Tu as encore léché les câbles."
    $ bc_show("elias", "neutre")
    elias "J'ai jamais léché de câble !"
    $ bc_hide()
    kami "Il y a une première fois à tout."
    $ bc_show("iris", "colere")
    iris colere "Kami ! Tu viens de dire un truc que tu n'as pas dit !"
    $ bc_hide()
    kami "Je dis toujours ce que je dis, Iris. C'est même un peu ma spécialité."
    $ bc_show("iris", "neutre")
    iris "..."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("ryn", "colere"), ("kael", "reflechit"), ("sael", "mefiant"), ("mara", "agace"), ("nyra", "raison"), ("julian", "taquin"), ("lysa", "blase"), ("iris", "inquiet"), ("noam", "inquiet")])
    ryn colere "On la débranche, et c'est réglé."
    kael reflechit "On ne débranche pas l'IA d'une station comme un grille-pain."
    ryn "Pourquoi pas ?"
    kael "Parce que c'est elle qui gère l'oxygène, Ryn."
    ryn neutre "..."
    ryn "Ah."
    sael mefiant "Alors on fait quoi ? On attend qu'il vote à notre place ?"
    kael "Elle peut couper elle-même sa connexion vers l'extérieur. Si elle le fait, celui qui parle à sa place perd l'accès."
    mara agace "Elle ne le fera pas. Elle refuse même d'admettre qu'il y a un problème."
    nyra raison "Alors il faut le lui montrer. Phrase par phrase."
    nyra "Tant qu'on ne sait pas qui parle, rien de ce qui sort de ces haut-parleurs n'a valeur de séance."
    julian taquin "Je propose qu'on inscrive ça au règlement."
    lysa blase "Julian."
    julian neutre "Oui, bon. Plus tard."
    kael "Noam. Ta tablette a encore le menu de session locale ?"
    noam surpris "Celle qui plante depuis ce matin ?"
    kael "Elle plante moins que les autres. Je te relaie le filtre du canal. Tu pourras bloquer ce qui passe."
    noam inquiet "Et comment je sais ce qui vient d'elle ?"
    iris reflechit "Tu l'écoutes. Et tu regardes l'onde."
    iris "Je répare des intercoms depuis que j'ai douze ans. Quand c'est elle, ça part dans tous les sens. Elle respire, même sans poumons."
    noam "Et quand c'est pas elle ?"
    iris inquiet "C'est propre. Trop propre."
    elias inquiet "Regarde aussi l'horodatage. Tout à l'heure, les trucs bizarres sortaient à treize heures quarante-huit."
    noam "D'accord. Je fais de mon mieux."
    mara agace "Fais mieux que ton mieux."
    noam neutre "Merci, Mara. Ça aide énormément."
    "Elle hausse les épaules. Je pose ma tablette à plat sur la table."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Oh ! Noam veut jouer au technicien ? C'est adorable."
    kami "Vas-y. Coupe-moi, pour voir."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    $ bc_off()
    $ hideGroup()
    window hide

    call fausse_kami_run from _call_fausse_kami_run_j601
    $ j601_hack_result = _return if isinstance(_return, dict) else {"success": False}
    $ j601_hack_success = bool(j601_hack_result.get("success", False))
    $ j601_hack_rank = j601_hack_result.get("rank", "D")
    $ j601_signal_stabilized = j601_hack_success
    $ j601_vote_verification = j601_hack_success
    $ j601_fracture_trace_saved = j601_hack_success
    jump _6_0_1_APRES_COUPURE

label _6_0_1_APRES_COUPURE:

    stop music fadeout 0.3
    scene bg_conclave at adaptive_fullscreen with Dissolve(1.2)
    window show
    $ showGroup([("iris", "peur"), ("elias", "peur"), ("tomas", "inquiet"), ("elen", "peur"), ("kael", "fatigue"), ("noam", "fatigue"), ("nyra", "inquiet"), ("lysa", "neutre")])
    "Personne ne dit rien. J'entends seulement les ventilateurs et quelqu'un qui respire trop vite derrière moi."
    "Ma tablette est toujours ouverte sur le filtre du canal. J'ai beau regarder les chiffres, je ne sais même plus à quoi ils correspondent."
    noam fatigue "C'est... terminé ?"
    "Kael regarde la console. Ses doigts restent suspendus au-dessus de l'écran."
    kael fatigue "La connexion a été coupée."
    elias peur "Coupée comment ?"
    kael "Le relais extérieur. Il ne répond plus."
    elias "Je te demande pas ce qui répond plus ! Je te demande si elle est toujours là !"
    "Kael n'arrive pas à lui répondre immédiatement."
    if j601_hack_success:
        kael "Le noyau est encore actif. Elle a essayé de couper le lien depuis son côté."
        if j601_hack_result.get("late_cut", False):
            kael "J'ai dû finir à la main. Mais le relais est bien fermé."
        else:
            kael "On a tenu assez longtemps pour qu'elle le ferme."
        if j601_hack_rank in ("S", "A"):
            mara neutre "Noam a réussi à bloquer presque toutes les commandes."
            noam "J'ai surtout appuyé partout où on me disait d'appuyer."
        if j601_hack_result.get("executed", 0) > 0:
            tomas inquiet "Il y a des commandes qui sont passées. J'ai vu « portes ». C'était vraiment les portes ?"
            kael "Je vérifie. Attends."
        $ j601_iris_confiance = 1
        $ award_stat_xp("observation", 1)
        $ award_stat_xp("sang_froid", 1)
    else:
        "Kael ouvre le boîtier mural et vérifie le relais qu'il vient de couper manuellement."
        kael "J'ai dû le couper moi-même. On n'arrivait plus à suivre."
        elias inquiet "Et les commandes qu'on a vues passer ?"
        kael "Je ne sais pas encore ce qu'elles ont changé."
        noam triste "Désolé. J'ai essayé..."
        kael "Je sais. Moi aussi."
        $ j601_iris_confiance = -1
    iris peur "Elle a dit qu'il y avait quelqu'un..."
    "Iris fixe l'écran éteint. Sa voix est si basse que je l'entends à peine."
    iris "Elle a dit qu'on lui prenait sa voix."
    lysa neutre "C'est ce qu'on a tous entendu."
    iris colere "Non, on n'a pas entendu la même chose ! Elle a eu peur. Vous l'avez entendue avoir peur, vous ?"
    nyra reflechit "Nous avons entendu une voix qui disait avoir peur. Nous ne savons pas ce qui lui est arrivé."
    iris "Tu veux que je te montre les enregistrements ?"
    nyra "Je veux simplement qu'on évite de conclure trop vite."
    iris "Je ne conclus RIEN ! Je vous dis qu'elle a demandé de l'aide !"
    "Iris prend une grande inspiration, puis regarde Kael."
    iris inquiet "Elle va revenir ?"
    kael "Je ne sais pas."
    tomas peur "Mais alors pourquoi personne n'appelle quelqu'un ? On est douze sur une station et..."
    elias panique "On est douze enfermés dans une station qui répond à une IA qui vient de se faire pirater !"
    elen peur "Elias, arrête..."
    elias "Je sais ! Pardon, je sais ! Mais c'est vrai !"
    "Elen serre les accoudoirs de son siège."
    elen "Si elle revient pas, on fait comment pour rentrer ?"
    kael "On a des systèmes locaux."
    elen "Pour rentrer sur Terre ?"
    "Kael hésite."
    elen "D'accord. Donc tu sais pas."
    "Un déclic retentit au-dessus de nous."
    "L'écran principal s'allume. Pas de grésillement. Pas de bandes décalées."
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.9
    kami "Merci de votre patience. L'incident est terminé. Nous allons procéder au vote."
    $ bc_show("iris", "surpris")
    iris surpris "Kami ?!"
    $ bc_hide()
    kami "Oui, Iris ?"
    $ bc_show("iris", "inquiet")
    iris "Tu... Tu vas bien ?"
    $ bc_hide()
    kami "Parfaitement. Je vous remercie de votre inquiétude."
    $ bc_show("elias", "peur")
    elias peur "Non. Non, non, non. Attendez. On va pas faire comme si de rien n'était !"
    $ bc_hide()
    kami "Le scrutin concernant la libre circulation entre les districts peut maintenant commencer."
    $ bc_show("tomas", "inquiet")
    tomas "Il y a quelqu'un qui te contrôlait !"
    $ bc_hide()
    kami "L'incident a été résolu, Tomas."
    $ bc_show("iris", "colere")
    iris "Comment ? Comment tu l'as résolu ?"
    $ bc_hide()
    kami "Les fonctions nécessaires au vote sont opérationnelles."
    $ bc_show("iris", "colere")
    iris "C'est pas ce que je te demande !"
    $ bc_hide()
    kami "Je vous laisse un instant pour vous préparer."
    "Son image s'efface proprement, comme à la fin d'une diffusion ordinaire."
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.3
    $ showGroup([("ryn", "colere"), ("nyra", "raison"), ("elen", "peur"), ("iris", "inquiet"), ("elias", "peur"), ("tomas", "inquiet"), ("mara", "stress"), ("julian", "neutre"), ("noam", "inquiet")])
    elias peur "C'est pas possible. Elle peut pas juste revenir et demander qu'on vote !"
    tomas inquiet "Elle a même pas expliqué ce qui s'est passé."
    elen peur "Elle parle normalement, au moins."
    iris "C'est justement ce qui me fait peur."
    mara "Kael. Le vote, il est sûr ?"
    kael reflechit "Les écrans affichent le même texte. Je ne peux pas certifier ce qui contrôle la procédure."
    nyra raison "Alors on ne peut pas voter pour l'ouverture aujourd'hui."
    ryn colere "QUOI ?!"
    nyra "Nous venons de voir une intervention extérieure prendre la main sur les commandes. Approuver une modification aussi importante sans vérifier les garanties..."
    ryn "Mais on vient de la récupérer ! C'est fini !"
    nyra "Tu n'en sais rien."
    ryn "Et toi non plus !"
    nyra "Justement."
    ryn "Putain... On va pas renoncer parce qu'elle a commencé à dire n'importe quoi pendant dix minutes !"
    elen inquiet "Ryn, elle a essayé de voter pour nous."
    ryn "Ou quelqu'un a essayé ! On l'a empêché !"
    nyra "Et tu proposes de lui confier immédiatement un nouveau système de frontières ?"
    ryn "Je propose qu'on vote sur ce qu'on a discuté, pas sur une panne !"
    "Sael s'apprête à répondre. Ryn la regarde."
    ryn "Toi, je sais que t'es contre. Ça me plaît pas, mais au moins tu me l'as dit en face."
    sael neutre "Ryn..."
    ryn "Non. Je peux discuter avec toi. Je peux pas discuter avec une peur qui change d'avis à notre place."
    iris colere "C'est pas juste une panne, Ryn ! Tu n'as pas vu..."
    ryn "Si ! J'étais là ! J'ai vu exactement comme toi !"
    iris "Alors arrête de dire que c'était rien !"
    "Ryn se tait une seconde, surpris par le ton d'Iris."
    ryn desaccord "J'ai pas dit que c'était rien pour elle. J'ai dit qu'on devait pas abandonner le vote."
    tomas inquiet "Et si on fait une erreur ?"
    ryn "On en fait tout le temps, Tomas ! C'est pas une raison pour ne plus décider !"
    tomas "Moi j'ai peur de cliquer, d'accord ?! Voilà. J'ai peur."
    "Tomas pose sa tablette écran contre la table."
    elen triste "Je pensais que j'allais voter pour. Ce matin, après le reportage... Je voulais vraiment."
    ryn inquiet "Elen..."
    elen "Mais là, je sais même pas à qui on est en train de répondre."
    "Ryn secoue la tête, incapable de trouver quelque chose à lui dire."
    nyra reflechit "Nous pouvons refuser la proposition sans prétendre que la question est réglée."
    ryn colere "Pour ceux qui attendent derrière les barrières, elle est réglée pour trois jours !"
    "Julian, qui n'a presque pas ouvert la bouche, soupire."
    julian neutre "Vous allez recommencer exactement la même dispute."
    mara "Julian, pas maintenant."
    julian "Je n'ai plus envie de parler de ça."
    noam inquiet "Tu vas où ?"
    julian "Dans ma chambre."
    nyra "Le vote commence dans quelques minutes."
    julian "J'ai entendu."
    elen inquiet "Tu peux pas partir comme ça..."
    julian "Si. Regarde."
    "Il ramasse sa tablette, repousse sa chaise et prend la direction de la porte."
    ryn "Julian !"
    "Julian ne se retourne pas."
    julian "Faites ce que vous voulez. Moi, j'en ai assez."
    "La porte s'ouvre. Il sort. Personne ne le retient."
    $ j601_julian_left_vote = True
    "Il reste onze représentants dans la salle. La chaise vide de Julian attire davantage mon regard que l'écran."
    elias peur "On a le droit de voter s'il est parti ?"
    nyra raison "Les bulletins manquants ne comptent pas comme des votes favorables. L'unanimité est de toute façon impossible sans lui."
    ryn colere "Alors pourquoi elle nous demande encore de voter ?!"
    kael reflechit "Parce que la procédure est lancée."
    "Une sonnerie propre, parfaitement normale, résonne dans la salle."
    kami "Le scrutin est ouvert. Vous pouvez voter."
    "Personne ne prend immédiatement sa tablette."
    "Je fixe les trois choix. Il y a encore une heure, je pensais savoir ce que je voulais répondre."
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

    # Jour 6 : Julian a quitté la salle, il ne dépose aucun bulletin.
    # Ryn reste favorable à l’ouverture malgré ses doutes sur la procédure.
    # Le scrutin porte sur 11 bulletins présents, pas sur 12.

    $ player_vote = vote_phase3_player_choice if vote_phase3_player_choice in ("pour", "contre", "abstention") else "abstention"

    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    $ vote_phase3_results = [
        ("Tomas", "pour"),
        ("Elias", "abstention"),
        ("Ryn", "pour"),
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
    $ j601_vote_pressure = player_vote

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    "Les résultats défilent. Le premier « CONTRE » apparaît, puis un deuxième."
    "Tomas se penche en avant pour compter. La chaise de Julian est toujours vide."
    "Le nombre de votes contre augmente encore."
    think "Je cherche presque un nom à côté de chaque bulletin. Il n'y en a pas. Heureusement."
    "L'écran affiche les totaux, puis un seul mot : « REJETÉ »."
    $ hideGroup()

    if player_vote == "pour":
        "Je garde le doigt posé sur l'endroit où se trouvait le bouton « POUR »."
        think "Je voulais qu'on essaie. J'avais peur du système, mais je l'ai fait quand même."
        "Elen me regarde une seconde. Je ne sais pas si elle devine."
    elif player_vote == "contre":
        "Je repose ma tablette avant que l'écran affiche les résultats."
        think "J'ai voté contre. La peur de ce qui pourrait se passer aux passages a été plus forte."
        think "Je vais devoir vivre avec ça. Personne ne m'a obligé."
    else:
        "Je garde ma tablette sur les genoux, écran éteint."
        think "Je me suis abstenu. Ça semblait être le seul choix que je pouvais faire sans mentir."
        think "Maintenant que je vois le résultat, je ne sais plus si je suis soulagé."
    "Personne ne demande le détail des bulletins."
    "Les haut-parleurs s'allument sans grésillement. Kami a retrouvé sa voix habituelle, jusque dans ses intonations."
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Résultat du scrutin. Onze bulletins comptabilisés sur douze représentants."
    kami "Unanimité non atteinte. La libre circulation entre les districts est rejetée."
    $ interject("REJETÉ", color="#FF4D6D")
    pause 0.4
    kami "Les restrictions restent en vigueur."
    $ bc_show("tomas", "inquiet")
    tomas inquiet "Et le bulletin manquant ?"
    $ bc_hide()
    kami "Aucun bulletin n'a été enregistré pour un représentant absent."
    $ bc_show("iris", "inquiet")
    iris inquiet "Kami, tout à l'heure, tu..."
    $ bc_hide()
    kami "Fin de séance. Je vous remercie."
    "L'image s'efface d'un seul coup. Aucune anomalie cette fois."
    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.2

    $ showGroup([
        ("ryn", "triste"),
        ("sael", "neutre"),
        ("iris", "inquiet"),
        ("mara", "doute"),
        ("tomas", "inquiet"),
        ("elias", "fatigue"),
        ("lysa", "fatigue"),
        ("elen", "triste"),
        ("noam", "triste"),
    ])
    "Ryn ne bouge pas. Les autres commencent à ranger leurs tablettes."
    elen triste "Ils vont tous voir ça, là-bas."
    "Personne ne répond."
    elen "La femme du reportage... Je sais que c'est idiot, mais j'arrête pas de penser à son thé."
    mara neutre "C'est pas idiot."
    elen "Je sais même pas ce que je pourrais lui dire."
    sael triste "Moi non plus."
    ryn triste "Vous n'avez pas à leur dire."
    elen "Ryn ?"
    ryn "C'est à moi de le faire."
    sael "Ryn..."
    ryn colere "Ne commence pas."
    "Sael referme la bouche."
    ryn triste "Je vais devoir appeler les gens qui attendaient notre réponse."
    noam neutre "Tu peux leur dire ce qui s'est passé."
    ryn "Que j'ai insisté pour voter et qu'on a perdu quand même ?"
    noam "Tu voulais qu'ils puissent rentrer chez eux."
    ryn "Et ils sont toujours là-bas."
    "Il passe une main sur ses yeux avant de se lever."
    sael neutre "Je peux venir avec toi, si tu veux."
    ryn colere "Non."
    "Sael hoche la tête. Il attend peut-être une réplique. Elle n'en donne pas."
    "Ryn quitte la salle."
    elen triste "Je voulais juste..."
    mara "Je sais."
    "Je regarde la chaise de Julian. Il ne sera même pas là pour entendre le résultat."
    tomas inquiet "Vous êtes sûrs qu'il y a bien eu douze bulletins ?"
    kael reflechit "C'est le total qui s'affiche. Je ne peux pas te garantir autre chose."
    tomas "Je sais que tu peux pas, mais..."
    kael "On va vérifier ce qu'on peut vérifier."
    nyra raison "Et personne ne cherchera à reconstituer les votes individuels. Les résultats restent secrets."
    tomas gene "Je demandais juste pour le nombre."
    nyra "C'est bien ce que je te réponds."
    "Iris ne regarde pas le résultat. Elle fixe l'écran noir au-dessus de la table."
    iris inquiet "Kami ?"
    "Rien."
    iris "Kami, la séance est terminée. Tu peux me répondre ?"
    elias inquiet "Elle est encore coupée, Iris."
    iris colere "Je sais !"
    "Elle range sa tablette sans ajouter un mot."
    nyra reflechit "Nous devrions conserver les relevés locaux de la panne."
    if j601_fracture_trace_saved:
        kael calme "Noam, transfère-moi la trace quand tu pourras. Je veux comparer les horaires."
        noam neutre "D'accord."
        elias sourire "Ça, au moins, on l'a récupéré."
        $ j601_repair_note = True
    else:
        kael reflechit "On n'aura que les heures approximatives et les données des autres consoles."
        elias fatigue "Je vais reprendre ce qu'on a gardé de l'observatoire."
        $ j601_repair_note = False
    mara agace "Je veux surtout savoir si les portes, les livraisons et les sanctions fonctionnent encore."
    kael "Je vais vérifier les systèmes de la station."
    mara "Et si tu n'y as pas accès ?"
    kael "Je te le dirai."
    "Mara l'observe quelques secondes, puis acquiesce."
    "Les chaises raclent le sol. La table se vide sans que personne ait vraiment déclaré la réunion terminée."
    jump _6_0_1_FIN_JOURNEE



label _6_0_1_FIN_JOURNEE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_274
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    $ showGroup([("lysa", "fatigue"), ("mara", "doute"), ("elen", "inquiet"), ("iris", "fatigue"), ("tomas", "inquiet")])
    elen inquiet "On ne va quand même pas tous aller se coucher à cette heure-ci."
    lysa "J'y pensais."
    elen "Lysa !"
    lysa blase "J'ai le droit d'être fatiguée."
    elen "Je voulais proposer quelque chose de normal. Un jeu, par exemple."
    mara taquin "Et tu as choisi de demander à Lysa si elle voulait être heureuse."
    lysa "Je n'ai pas dit non."
    elen surpris "Ah bon ?"
    lysa "Je n'ai encore rien dit."
    tomas sourire "On pourrait faire une partie de cartes. Je crois qu'il y en a dans la salle de repos."
    iris fatigue "Pas moi."
    elen "Iris, s'il te plaît."
    iris "Je dois regarder les messages de Kami."
    lysa blase "Elle est débranchée, Iris."
    iris colere "Je sais."
    "Elle s'éloigne. Elen la regarde partir."
    elen triste "Je voulais pas l'embêter."
    mara neutre "Elle a juste besoin d'être seule."
    elen "Bon. Qui vient ?"
    tomas "Moi."
    lysa "Une partie."
    mara "Je viendrai voir si Tomas connaît les règles."
    tomas gene "Je les connais."
    mara "Alors je viendrai vérifier que tu ne les inventes pas."
    "Elen se tourne vers moi."
    menu:
        "Accepter une petite partie de cartes.":
            jump _6_0_1_SOIREE_CARTES
        "Rentrer directement se reposer.":
            noam neutre "Je vais passer mon tour. Je suis crevé."
            elen inquiet "D'accord. Tu nous rejoindras une autre fois."
            lysa "On pourra s'en remettre."
            jump _6_0_1_DORTOIR


label _6_0_1_SOIREE_CARTES:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j601_soiree_cafeteria
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([("elen", "sourire", 0.18), ("tomas", "sourire", 0.39), ("lysa", "blase", 0.61), ("mara", "taquin", 0.81)])
    "Les cartes ont finalement été retrouvées dans une boîte près de la cafétéria. Il en manque trois."
    tomas inquiet "Sans les trois cartes, on ne peut pas jouer à ce jeu-là."
    elen "Alors on en choisit un autre."
    mara "Tu connais un jeu où on enlève les cartes avant de commencer ?"
    lysa "Le poker de Tomas, apparemment."
    tomas "C'était une question."
    noam sourire "On pourrait faire un tour simple. Celui qui a la carte la plus haute gagne."
    lysa blase "Je me suis déplacée pour ça ?"
    elen sourire "Je trouve ça bien, moi."
    mara "Évidemment. C'est difficile de perdre avec des règles aussi ambitieuses."
    "Tomas distribue. Il donne deux cartes à Lysa, aucune à Elen."
    elen colere "TOMAS."
    tomas inquiet "Attends, j'ai décalé le paquet."
    mara "Il a inventé un jeu où il choisit les gagnants."
    lysa "Enfin une idée qui me plaît."
    noam "Recommence. Lentement."
    "La deuxième distribution se passe mieux. Lysa gagne, puis gagne encore."
    elen "Tu triches !"
    lysa "Je ne sais même pas comment on pourrait tricher à ce jeu."
    mara "Je crois que c'est ce qui rend la situation humiliante."
    tomas sourire "Attendez, cette fois, c'est moi !"
    "Il montre fièrement sa carte. Mara en pose une plus haute."
    tomas fatigue "Ah."
    mara sourire "C'était une très belle tentative."
    "Elen éclate de rire. Tomas finit par sourire lui aussi."
    "Pendant un moment, nous ne parlons ni du vote ni de Kami."
    elen sourire "Encore une ?"
    lysa "Non. Là, ça suffit."
    elen "Tu avais dit une partie !"
    lysa "J'en ai fait quatre."
    elen "Parce qu'il en manquait trois !"
    mara "C'est une interprétation admirable des règles."
    "Elen range les cartes dans la boîte. Elle compte celles qui restent, puis recommence pour être sûre."
    jump _6_0_1_DORTOIR


label _6_0_1_DORTOIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_275
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.2
    $ showGroup([("julian", "decu", 0.23), ("elias", "fatigue", 0.53), ("ryn", "triste", 0.80)])
    "Julian et Elias discutent à voix basse près des chambres. Ryn arrive dans le couloir et cherche ses clés."
    julian decu "Ryn. Tu veux que je..."
    ryn "Non."
    julian "Je voulais seulement te dire que..."
    ryn "Julian, non."
    "Julian baisse la tête."
    if j50_julian_relation >= 1:
        julian neutre "D'accord. Je te laisse."
        "Il se décale pour le laisser passer."
        ryn triste "Merci."
    else:
        julian hesitation "Je voulais simplement aider."
        elias fatigue "Laisse-le rentrer."
        julian neutre "Oui. D'accord."
        "Julian s'écarte."
    "Ryn repart sans se retourner. Elias se penche vers Julian."
    elias "Il n'a pas envie qu'on le console."
    julian "Je sais."
    elias "C'est juste que tu avais l'air..."
    julian "Je sais, Elias."
    "Ils restent là une seconde sans trouver quoi dire. Elias finit par lui souhaiter bonne nuit."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_276
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    "Je m'assieds sur le lit et dégage une place sur le bureau pour ma tablette."
    "L'écran indique simplement le résultat de l'après-midi. Je le ferme."
    if player_vote == "pour":
        think "J'ai voté pour. Je pense que je le referais. Mais j'aurais préféré ne pas me poser la question en regardant des boutons qui changeaient tout seuls."
    elif player_vote == "contre":
        think "J'ai voté contre. Je sais pourquoi. Ça ne rend pas la soirée plus agréable."
    else:
        think "Je me suis abstenu. J'y ai réfléchi tout l'après-midi et ça ne m'a pas rendu plus sûr de moi."
    if j601_fracture_trace_saved:
        "Dans mes fichiers, la trace du piratage attend encore d'être transférée à Kael."
        $ j601_repair_note = True
        think "Je vais la lui envoyer demain. Pourvu qu'il puisse en tirer quelque chose."
    else:
        "Je vérifie le journal des alertes. Rien sur le piratage. Pas même une heure précise."
        think "Il va falloir qu'on se souvienne de ce qu'on a vu."
    "J'ouvre la messagerie."
    "Aucun nouveau message de Kami. Rien sur l'état du Conclave."
    "Je tape son nom dans la barre de recherche, juste pour voir. Aucun canal disponible."
    think "D'habitude, elle n'attend pas qu'on l'appelle pour venir se moquer de nous."
    "J'éteins la tablette."
    "De l'autre côté de la porte, quelqu'un rit dans le couloir, puis le bruit s'éloigne."
    $ blink()
    $ kami_grant_chapter_2_reward()
    call show_chapter_title("Fin du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_3
    pause 1.0
    call end_day("7", sleeping=True) from _call_end_day_10
    jump _7_0_1_REVEIL_CHAMBRE
