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
    noam surpris "Kami ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vous rappelle que l'unanimité est... est..."
    play sound "audio/sfx_glitch.mp3"
    kami "Ah ! Bon ! Vous connaissez la suite, mes petits... mes petits..."
    "Sa voix grésille, puis la diffusion s'arrête au milieu d'un rire."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
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
    elen gene "Oui, oui, je partage !"
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
    call kd_vn_cg_impact("#e4f0ff")
    scene bg_cg035 at adaptive_fullscreen with dissolve
    "À l'écran, des gens se sont installés devant un poste-frontière. Certains ont amené des chaises pliantes. Un enfant joue avec le ruban qui entoure une valise."
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
    "UN HOMME — Vous pouvez pousser votre matériel ? Ma mère n'arrive pas à passer."
    "JOURNALISTE — Excusez-moi. Madame, vous aussi, vous attendez quelqu'un ?"
    "UNE VIEILLE FEMME — Non, j'accompagne mon fils. Il s'est fait une idée et maintenant il veut rester là toute la journée."
    "UN HOMME — Maman..."
    "UNE VIEILLE FEMME — Quoi ? C'est vrai."
    "Le journaliste se décale. Au fond, des agents surveillent les barrières sans parler."
    "JOURNALISTE — La décision du Conclave est attendue cet après-midi. Pour le moment, aucune ouverture n'est annoncée."
    "Une petite fille demande à son père s'ils peuvent rentrer manger. Il lui promet d'y aller bientôt."
    "L'image change avant qu'on entende sa réponse."
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
    tomas inquiet "Kami, certaines tablettes indiquent treize heures cinquante et d'autres quatorze heures."
    kami "Je le sais, Tomas."
    noam "Tu peux nous dire quel horaire est le bon ?"
    kami "Bien sûr ! Bien... sûr."
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    kami "Venez main... maintenant."
    elen "Et pourquoi ça a changé ?"
    kami "Parce que j'en ai... j'en ai décidé ainsi, évidemment ! Tu veux aussi un justificatif si... signé ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous êtes attendus au Conclave. Merci. Mer... ci."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
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
    julian taquin "J'avais justement préparé..."
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
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("mara", "mefiant"), ("ryn", "colere"), ("sael", "neutre"), ("iris", "inquiet"), ("nyra", "reflechit"), ("kael", "reflechit"), ("elen", "inquiet"), ("lysa", "blase"), ("noam", "surpris")])
    iris inquiet "Elle a recommencé. C'est exactement ce qu'elle a fait ce matin."
    kael "Je vais vérifier le flux."
    iris "Pas seulement le flux ! Elle a répété Julian mot pour mot, avec le même délai !"
    mara "Iris, on a déjà compris qu'elle déconne !"
    iris colere "Et moi, je veux comprendre POURQUOI !"

    "Peu après le débat repart de plus belle."
    lysa neutre "Bon. Est-ce que quelqu'un a une proposition concrète ?"
    elen inquiet "Je ne veux pas que les familles attendent trois jours de plus."
    mara "Personne ne veut ça."
    ryn "Alors faites quelque chose."
    sael "Je te l'ai dit : pas sans sécurité."
    ryn colere "Mais on n'a PAS de sécurité à leur offrir !"
    sael colere "C'est justement pour ça que..."
    "Les haut-parleurs crachent un rire."
    kami "Ah ! Ah ah ! Oh, pardon, je..."
    "Le rire s'interrompt net."
    noam surpris "Kami ?"
    kami "Je vous écoute."
    "Iris relève la tête, attentive."
    iris inquiet "Non, attendez. Le rire s'est coupé avant la fin. C'est pas normal du tout."
    mara mefiant "On ne lui a rien demandé."
    kami "Vous avez parlé de sécurité. C'est un sujet important."
    nyra "Kami, tu voulais ajouter quelque chose ?"
    kami "Non."
    "Ryn hausse les épaules."
    ryn colere "Alors ne nous coupe pas."
    kami "Très bien."
    "Une seconde passe."
    kami "Très bien."
    "Le deuxième « très bien » est prononcé avec exactement la même intonation."
    iris reflechit "Ce n'est PAS un écho. Elle a reproduit la même intonation, sans réaction à ce qu'on lui disait."
    kael reflechit "Peut-être."
    "Kael jette un coup d'œil à sa tablette. Il ne dit rien."
    mara "On parlait des contrôles."
    ryn colere "Je sais de quoi on parlait."
    "Ryn reprend, mais le son du haut-parleur baisse soudain, puis revient."
    kami "Julian, tu voulais prendre la parole."
    julian surpris "Euh... non ?"
    kami "D'accord, Julian."
    julian "Je n'ai pas levé la main."
    kami "D'accord, Julian."
    julian colere "Mais enfin, ça suffit !"
    "Cette fois, elle ne répond pas."
    iris inquiet "Kami, tu m'entends ?"
    kami "Oui, Iris."
    iris "Tu peux nous expliquer pourquoi tu répètes les mêmes réponses ?"
    kami "Je ne répète pas les mêmes réponses."
    iris "..."
    lysa blase "Bon, on ne va pas y passer la journée."
    "Sur ma tablette, l'heure passe de 13 h 58 à 13 h 48, puis revient."
    noam inquiet "Kael, tu as vu ?"
    kael reflechit "Oui."
    "Il se lève et vérifie l'horloge murale. Elle indique toujours 13 h 58."
    nyra reflechit "Les affichages ne sont pas synchronisés."
    elias inquiet "Je peux regarder le réseau local."
    kael "Sans toucher aux consoles, s'il te plaît."
    elias "Je sais."
    "Un silence. Puis le sourire de Kami envahit l'écran principal, sans annonce."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je vous rappelle que le scrutin commencera à quatorze heures."
    noam "On sait."
    kami "Vous avez encore deux minutes."
    tomas surpris "Mais... il est treize heures cinquante-huit."
    kami "C'est exact, Tomas."
    elen inquiet "Alors pourquoi les tablettes disaient treize heures cinquante ?"
    kami "C'est exact, Tomas."
    "Elen tourne la tête vers lui. Tomas fait un geste impuissant."
    iris inquiet "Kami. Réponds à Elen."
    "Le sourire reste fixe."
    kami "Je vais lancer la procédure."
    iris "Non. Attends."
    kami "Je vais lancer la procé... procé... procédure."
    iris colere "Kami ! Arrête !"
    play sound "audio/sfx_glitch.mp3"
    with hpunch
    "Le portrait se décale brutalement en bandes, puis l'écran devient noir."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
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
    julian taquin "Tu vas nous dire qu'on doit redémarrer la station ?"
    kami "Ha ha ! Très drôle, Julian."
    julian "Je n'essayais pas vraiment..."
    iris reflechit "Elle peut répondre. C'est déjà bon signe."
    nyra reflechit "Kami, peux-tu afficher le même texte sur nos douze tablettes ? Sans lancer le scrutin."
    kami "Bien sûr !"
    "L'écran de Nyra reste vide."
    nyra "Je n'ai toujours rien."
    kami "Tout est affiché."
    nyra "Non."
    kami "Tout est affiché."
    "Nyra retourne sa tablette pour la montrer à l'écran."
    nyra "Regarde."
    kami "Je regarde."
    "Iris se lève."
    iris inquiet "Kami, arrête de répondre comme ça. Vérifie le canal avant de continuer."
    kami "Je n'ai pas besoin de..."
    pause 0.4
    kami "De..."
    "Le sourire de Kami se contracte. Le bord de son visage reste immobile alors que sa bouche continue de bouger."
    kami "Je n'ai pas besoin de vérification. Je suis opérationnelle."
    iris colere "Non ! Tu viens de bloquer sur une phrase ! Ça n'arrive pas à une IA comme toi !"
    noam inquiet "Iris, elle t'entend."
    iris "J'espère bien ! Je veux qu'elle me dise ce qui se passe, pas qu'elle récite une réponse toute faite !"
    iris "Alors laisse-les poser des questions."
    kami "Bien sûr, Iris."
    "L'écran s'éteint une nouvelle fois. Cette fois, les haut-parleurs émettent un souffle sourd."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("mara", "mefiant"), ("ryn", "neutre"), ("sael", "neutre"), ("iris", "inquiet"), ("nyra", "reflechit"), ("kael", "reflechit"), ("elen", "inquiet"), ("noam", "inquiet"), ("elias", "neutre")])
    stop music fadeout 0.2
    mara mefiant "On reporte."
    ryn neutre "Oui."
    elen inquiet "Attendez, on peut ?"
    nyra reflechit "Nous pouvons refuser de tenir le vote aujourd'hui. Mais pour modifier le texte, il faudra attendre une autre séance."
    mara "Je préfère ça à un résultat sorti d'une boîte cassée."
    kael reflechit "Je ne peux pas certifier l'état du système de dépouillement. Nous n'avons pas accès à ses journaux."
    elias "Par contre, les tableaux locaux fonctionnent encore. Ils enregistrent les changements du canal de séance."
    "Une alerte surgit sur ma tablette : « SESSION LOCALE — RETOUR EN ATTENTE »."
    noam "Kael, j'ai un menu de récupération."
    kael "Ne lance pas le scrutin. Essaie seulement de restaurer l'accès au dossier."
    noam "Et si ça ne marche pas ?"
    kael "Tu t'arrêtes. On n'est pas obligés de réparer Kami avec une tablette."
    "Elias se penche au-dessus de mon épaule."
    elias inquiet "Là. Le canal local. Tu peux le récupérer si tu suis la séquence."
    call j601_play_signal_instable from _call_j601_play_signal_instable
    $ j601_signal_stabilized = bool(_return)
    stop sound fadeout 0.5
    scene bg_conclave at adaptive_fullscreen with dissolve
    if j601_signal_stabilized:
        "Mon dossier réapparaît. Je reconnais la proposition sur les frontières, mais le bouton de validation reste grisé."
        noam surpris "Je l'ai !"
        kael "Tu as récupéré ton affichage. C'est bien. Mais ne touche pas à la validation."
        elias sourire "Au moins, on peut relire quelque chose !"
        $ j601_vote_verification = True
    else:
        "La procédure de récupération échoue. Mon écran revient à un menu vide."
        noam inquiet "Non. Ça ne marche pas."
        kael "Alors on n'insiste pas."
        elias fatigue "Je peux faire une capture depuis ma console si elle répond encore."
        $ j601_vote_verification = False
    "Les tablettes des autres représentants s'allument presque toutes à la fois."
    elen peur "Ça recommence."
    "Un bref clignotement traverse le plafond."
    "La porte du Conclave émet un double bip. Personne n'a essayé de sortir."
    tomas inquiet "C'est quoi, ce bruit ?"
    kael inquiet "Je ne sais pas."
    "Mara se lève pour aller vérifier. La porte s'ouvre normalement sous sa main."
    mara neutre "Bon. Au moins, on peut sortir."
    elen "C'est déjà ça."
    "Mais personne ne la suit."
    "La voix de Kami revient, beaucoup plus basse que d'habitude."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Tout va bien. Le système a retrouvé sa stabilité."
    iris inquiet "Kami ?"
    kami "Les procédures sont disponibles. Vous pouvez rester."
    iris "Est-ce que tu sais ce qui vient de se passer ?"
    kami "Je suis là, Iris."
    iris "Je sais que tu es là !"
    "Kami ne répond pas."
    kami "Restez, s'il vous plaît."
    "Il n'y a ni rire ni musique après sa phrase."
    "Iris baisse lentement sa tablette."
    iris fatigue "Ne faites rien. Pas encore."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("mara", "mefiant"), ("ryn", "inquiet"), ("sael", "neutre"), ("iris", "inquiet"), ("nyra", "raison"), ("kael", "reflechit"), ("elen", "inquiet"), ("noam", "inquiet")])
    jump _6_0_1_FRACTURE_QTE

label _6_0_1_FRACTURE_QTE:

    play music "music/bgm_low_tension.mp3" fadein 1.5
    "Kael et Nyra rapprochent leurs tablettes pour comparer ce qu'elles affichent."
    $ showGroup([("nyra", "raison", 0.25), ("kael", "reflechit", 0.52), ("iris", "inquiet", 0.78)])
    nyra reflechit "La proposition est bien revenue sur les douze écrans."
    kael "Les journaux locaux, eux, signalent une différence entre l'heure de séance et l'horloge de la station."
    iris "Ça peut être une transmission défectueuse. Ça n'implique pas une erreur dans les bulletins."
    nyra "Non. Mais ça nous empêche d'être certains du contraire."
    mara mefiant "Et donc ? On part et on revient quand elle sera remise ?"
    elen inquiet "On ne peut pas laisser les gens attendre en disant juste qu'on verra plus tard."
    ryn triste "On leur fera attendre trois jours de plus, quoi qu'on décide."
    elen "Non. Si on vote, au moins on aura essayé."
    ryn "Et si quelqu'un décide qu'on a voté autre chose ?"
    "Elen s'arrête."
    nyra "Je voudrais éviter qu'on confonde deux questions. La première, c'est : peut-on modifier les frontières aujourd'hui ? La seconde : est-ce que nous faisons confiance à cette procédure ?"
    lysa reflechit "La réponse à la deuxième me paraît assez claire."
    nyra "Ce n'est pas une raison pour inventer une réponse à la première."
    "Sur l'écran de ma tablette, une ligne d'erreur disparaît aussitôt qu'elle apparaît."
    elias inquiet "Attendez. Ça, on peut peut-être le conserver."
    noam "Quoi ?"
    elias "La trace du décalage. Pas le résultat du vote. Le problème de connexion lui-même."
    kael reflechit "S'il reste quelque chose après la session, ça nous donnera au moins un point de comparaison."
    noam "Tu veux que je fasse quoi ?"
    elias "Capture la séquence pendant qu'elle passe. Et ne valide absolument rien."
    "L'écran s'emplit de caractères qui se chevauchent. Je cherche les lignes qui reviennent."
    call j601_play_fracture from _call_j601_play_fracture
    $ j601_fracture_result = _return

    scene bg_conclave at adaptive_fullscreen with dissolve
    if j601_fracture_result:
        $ j601_fracture_trace_saved = True
        "Une notification confirme : « TRACE LOCALE CONSERVÉE »."
        noam "J'ai quelque chose."
        kael reflechit "Montre."
        "Il examine l'écran sans se précipiter."
        kael "Bien. L'écart existe, et il est horodaté. Ça ne nous dit toujours pas s'il touche au dépouillement."
        nyra "Mais on pourra poser une question précise au lieu d'accuser Kami au hasard."
    else:
        $ j601_fracture_trace_saved = False
        "La ligne s'efface. Rien n'a été enregistré."
        noam "Raté."
        elias fatigue "Je l'ai vue aussi. Ça ne suffit pas à en garder une copie."
        kael "On notera l'heure approximative. Pas plus."
    "Kami réapparaît sans bruit."
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Le texte est disponible. Le scrutin peut... peut commencer."
    mara colere "Non. Pas tant que tu ne nous auras pas expliqué ce qui s'est passé."
    kami "Je suis opérationnelle."
    mara "Ça ne répond pas à ma question."
    kami "Le scrutin peut commencer."
    nyra "Kami, peut-on suspendre la séance et reprendre le même texte quand tu auras vérifié ton système ?"
    "Un long silence."
    kami "La séance de ce jour se terminera sans amendement adopté en l'absence de vote unanime."
    elen inquiet "Ça veut dire quoi ?"
    kael reflechit "Que si nous quittons la salle, les restrictions restent. Et le prochain créneau est dans trois jours."
    mara "Alors je préfère sortir."
    ryn triste "Et rentrer chez nous avec quoi ? Un « on verra » ?"
    mara "Tu préférerais un résultat dont personne ne peut répondre ?"
    ryn "Non."
    "Il semble lui-même surpris d'avoir répondu si vite."
    tomas inquiet "On peut voter contre, pour laisser une trace de notre refus ?"
    nyra "On peut. Mais ça ne rendra pas le matériel plus fiable."
    tomas "Je sais. Je voudrais juste ne pas laisser un écran vide parler à ma place."
    lysa blase "Je comprends l'idée. Je ne dis pas que je l'aime."
    elen triste "Et si je vote pour ?"
    sael neutre "Tu voteras pour. Personne ne t'en empêche."
    elen "Tu ne m'en voudras pas ?"
    sael "Non."
    elen "Même après ce matin ?"
    sael "Elen, je ne vais pas commencer à t'en vouloir pour une chose que tu m'as déjà dite."
    "Elen hoche la tête."
    ryn neutre "Moi, je voulais voter pour."
    "Il regarde les boutons apparus sur sa tablette."
    ryn "Je le veux encore."
    elen "Alors fais-le."
    ryn triste "Je ne sais pas ce que Kami en fera."
    "Sael le regarde, mais n'intervient pas."
    ryn "Je ne veux pas qu'un oui de ma part serve à ouvrir des passages sans que les villages sachent comment se défendre."
    mara "Tu vas voter contre ?"
    ryn "Oui."
    elen triste "Ryn..."
    ryn "Je sais. Je sais ce que je dis."
    "Il se rassied et laisse sa tablette sur la table."
    noam inquiet "Kami, si on participe, tu peux au moins nous dire combien de bulletins ont été enregistrés ? Sans révéler les choix."
    kami "Douze bulletins seront comptabilisés."
    noam "Tu pourras vérifier le nombre après ?"
    kami "Oui, Noam."
    "Sa réponse est immédiate. Pour la première fois depuis un moment, elle semble nous avoir compris."
    iris inquiet "Je voudrais lui poser une question avant."
    iris "Kami, tu peux me dire si tu es en danger ?"
    "Personne ne bouge."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je suis là, Iris."
    iris "Je ne t'ai pas demandé si tu étais là."
    "Le visage de Kami reste affiché."
    kami "Je suis là."
    "Iris tourne la tête. Elle ne reprend pas la parole."
    $ j601_iris_confiance = -1

    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("mara", "doute"), ("ryn", "triste"), ("sael", "neutre"), ("iris", "inquiet"), ("nyra", "raison"), ("kael", "reflechit"), ("elen", "triste"), ("noam", "inquiet"), ("tomas", "inquiet")])
    play music "music/bgm_low_tension.mp3" fadein 0.8
    "Nous pouvons quitter la pièce. Nous pouvons aussi voter. Rien ne garantit que ça se passera normalement."
    "Kael vérifie une dernière fois que le texte affiché sur les tablettes est identique."
    kael "La formulation est la même sur les douze écrans. Je ne peux pas certifier ce qui se passera après."
    nyra "Chacun décide en connaissance de cause."
    "Les sièges grincent. Personne ne se lève."
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
    $ j601_vote_pressure = player_vote

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    "Les résultats défilent. Le premier « CONTRE » apparaît, puis un deuxième."
    "Tomas se penche en avant pour compter. Julian ne regarde plus l'écran."
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
    show screen kami_broadcast_ui
    show screen j601_kami_glitch
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.6
    kami "Résultat du scrutin. Douze... douze bulletins comptabilisés."
    kami "Unanimité non atteinte. La libre circulation entre les districts est rejetée."
    $ interject("REJETÉ", color="#FF4D6D")
    pause 0.4
    kami "Les restrictions restent... restent en vigueur."
    play sound "audio/sfx_glitch.mp3"
    "Je m'attends au rire habituel."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Fin de séance."
    "L'image s'efface. Pas de fanfare. Pas même un « à bientôt »."
    hide screen j601_kami_glitch
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.2

    $ showGroup([
        ("ryn", "triste"),
        ("sael", "neutre"),
        ("iris", "inquiet"),
        ("mara", "doute"),
        ("tomas", "inquiet"),
        ("julian", "decu"),
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
    ryn triste "Je vais devoir appeler les gens qui m'ont cru. Ceux qui pensaient que j'allais défendre l'ouverture."
    noam neutre "Tu peux leur dire ce qui s'est passé."
    ryn "Que j'ai changé d'avis devant une tablette ?"
    noam "Que tu n'avais pas confiance."
    ryn "Ça ne va pas les aider à rentrer chez eux."
    "Il s'essuie les yeux d'un geste brusque, avant de se lever."
    sael neutre "Je peux venir avec toi, si tu veux."
    ryn colere "Non."
    "Sael hoche la tête. Il attend peut-être une réplique. Elle n'en donne pas."
    "Ryn quitte la salle."
    elen triste "Je voulais juste..."
    mara "Je sais."
    "Julian se lève à son tour, puis se rassied."
    if j601_julian_echo:
        julian decu "J'avais préparé quelque chose pour après le vote."
        noam "Je me doute."
        julian "Je ne crois pas que ce soit le moment."
        noam "Non."
        "Il plie son brouillon et le garde dans sa poche."
    else:
        julian decu "On devrait au moins préparer une déclaration."
        lysa blase "Pas maintenant."
        julian neutre "D'accord."
        "Il ne sort pas son brouillon."
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
    elias inquiet "Peut-être qu'elle a désactivé le canal."
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
    lysa blase "Elle ne répond pas aux questions depuis tout à l'heure."
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
        "Dans mes fichiers, la trace de la panne attend encore d'être transférée à Kael."
        $ j601_repair_note = True
        think "Je vais la lui envoyer demain. Pourvu qu'il puisse en tirer quelque chose."
    else:
        "Je vérifie le journal des alertes. Rien sur la panne. Pas même une heure précise."
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
