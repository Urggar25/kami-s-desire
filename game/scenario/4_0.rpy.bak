default j4_photo_pick_trace_attempts = 0
default j4_photo_put_trace_attempts = 0
default j4_tray_eaten = []
default j4_cafeteria_ryn_talked = False
default j4_cafeteria_julian_talked = False

screen day4_cafeteria_tv_pnc():
    modal True
    zorder 205

    add Solid("#000")
    use room_scene_background("cafeteria", navigation=False)

    $ television_path = "images/background/interact/cafeteria/cafeteria1/television.png"

    imagebutton:
        idle room_interaction_null()
        hover room_interaction_layer(television_path, "cafeteria", "hover")
        focus_mask room_interaction_layer(television_path, "cafeteria", "art")
        xpos 0
        ypos 0
        action Return("television")

    if not j4_cafeteria_ryn_talked:
        imagebutton:
            idle Transform(character_image("ryn", "colere"), zoom=1.00)
            hover Transform(character_image("ryn", "colere2"), zoom=1.00)
            focus_mask True
            xalign 0.22
            yalign 1.00
            action Return("ryn")
    else:
        add Transform(character_image("ryn", "colere"), zoom=1.00) xalign 0.22 yalign 1.00

    if not j4_cafeteria_julian_talked:
        imagebutton:
            idle Transform(character_image("julian", "neutre"), zoom=1.00)
            hover Transform(character_image("julian", "decu"), zoom=1.00)
            focus_mask True
            xalign 0.78
            yalign 1.00
            action Return("julian")
    else:
        add Transform(character_image("julian", "neutre"), zoom=1.00) xalign 0.78 yalign 1.00

    frame:
        xalign 0.03
        yalign 0.05
        background Solid("#071018dd")
        padding (18, 14)

        vbox:
            spacing 5
            text "OBJECTIF" size 18 color "#6FA6C6"
            text "Consulter la télévision" size 28 color "#A6D8FF"
            text "Ryn et Julian peuvent être interrogés." size 19 color "#DCE8F7"

screen day4_cafeteria_elen_gate():
    modal True
    zorder 205

    add Solid("#000")
    add "images/background/scene/cafeteria2.png" at cover_screen

    imagebutton:
        idle Transform(character_image("elen", "colere"), zoom=1.00)
        hover Transform(character_image("elen", "colere_noire"), zoom=1.00)
        focus_mask True
        xalign 0.55
        yalign 1.00
        action Return("elen")

screen day4_tray_pnc():
    modal True
    zorder 210

    add "images/background/interact/cafeteria/plateau/plateau.png" at cover_screen

    if "bread" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/pain.png"
            hover "images/background/interact/cafeteria/plateau/pain.png"
            xalign 0.29
            yalign 0.54
            action Return("bread")

    if "ration" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/ration.png"
            hover "images/background/interact/cafeteria/plateau/ration.png"
            xalign 0.50
            yalign 0.50
            action Return("ration")

    if "bar" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/barre.png"
            hover "images/background/interact/cafeteria/plateau/barre.png"
            xalign 0.65
            yalign 0.64
            action Return("bar")

    button:
        xalign 0.37
        yalign 0.68
        xsize 260
        ysize 170
        background None
        action Return("empty")

    textbutton "Terminer":
        xalign 0.84
        yalign 0.88
        xsize 190
        ysize 58
        action Return("finish")


label _4_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"

    pause 1.5  # Légèrement plus long pour accentuer la lourdeur

    call show_chapter_title("Début du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent")

    $ blink()
    "Je reviens à moi sous la lumière bleue des veilleuses."
    $ blink()
    think "Hier, il a suffi d'un non. Un seul et tout a été refusé."
    think "Le bouton vert est resté éteint, et le monde a repris sa place exacte."

    $ blink()
    think "Mon cœur bat comme s'il voulait économiser ses forces. Aurais-je pu faire autrement ?"
    think "On a gardé le système de rations. La sécurité. Mais aussi les chaînes avec."

    $ blink()
    pause 2.5  # Pause plus longue pour laisser peser le vide

    "Parmi les affaires qui ont été amenées ici lors de mon arrivée, il y avait cette photo."

    call day4_photo_take_trace from _call_day4_photo_take_trace

    scene bg_cg029 at adaptive_fullscreen with dissolve
    think "Le cadre est froid et le papier représente une famille souriante. Pas la mienne : ce sont des amis."
    $ unlock_gallery_image("bg_cg029")
    think "Pourquoi est-ce que je les regarde comme ça ?"
    think "Est-ce qu'ils sourient encore ? Est-ce qu'ils auraient préféré abandonner ces putains de bons de rationnement ?"

    call day4_photo_put_trace from _call_day4_photo_put_trace

    "Je repose la photo face contre la table."
    think "À quoi ça sert de se poser ce genre de questions... Je n'aurai pas la réponse."

    play sound sfx_announce
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Et bien booooonjour tout le monde ! J'espère que vous n'avez pas trop la gueule de bois ?!"
    kami "Il est huit heures et, bonne nouvelle : votre petite révolution a été annulée faute de courage."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Oh mais ne vous en faites pas, vous aurez bien des occasions de voir les conséquences de vos choix."
    kami "La situation reste impeccablement identique à tout ce que vous avez connu depuis un an : pas une pièce qui circule, pas une once de liberté supplémentaire."
    kami "Après tout, la liberté et la sécurité sont rarement compatibles !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C'est beau, non ? Ce calme avant… le calme."
    kami "Pas d'alarme. Pas de chaos. Juste la garantie que demain ressemblera exactement à aujourd'hui."
    kami "Mais vous avez confirmé ce que je pensais : l'humanité aime la liberté tant qu'elle ne menace pas son dîner."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Allez, ne faites pas cette tête ! Vous avez probablement sauvé des gens."
    kami "Vous verrez tout ça de vos propres yeux à la cafétéria. Les écrans sont chauds et vos rations sont prêtes."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    pause 1.0

    play sound sfx_drop
    "Un bruit sec retentit dans le couloir, comme si on avait donné un coup dans une surface métallique."

    jump _4_0_NAVIGATION_CAFETERIA

label day4_photo_take_trace:

    $ j4_photo_pick_trace_attempts = 0

label day4_photo_take_trace_loop:

    call screen trace_qte(path_type="curve_right", time_limit=6.0, wait_time=0.5, tolerance=70, max_errors=5, anchor_x=860, anchor_y=620)

    if _return["success"]:
        return

    $ j4_photo_pick_trace_attempts += 1
    if j4_photo_pick_trace_attempts >= 2:
        "Mes doigts glissent une première fois, puis finissent par trouver le bord du cadre."
        return

    "Je m'y reprends."
    jump day4_photo_take_trace_loop

label day4_photo_put_trace:

    $ j4_photo_put_trace_attempts = 0

label day4_photo_put_trace_loop:

    call screen trace_qte(path_type="arc", time_limit=5.0, wait_time=0.4, tolerance=72, max_errors=5, anchor_x=960, anchor_y=620)

    if _return["success"]:
        return

    $ j4_photo_put_trace_attempts += 1
    if j4_photo_put_trace_attempts >= 2:
        "Je finis par la reposer, maladroitement."
        return

    "Le cadre accroche mes doigts."
    jump day4_photo_put_trace_loop

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "Je sors de la chambre."
    think "Lumière froide. Portes fermées. Personne ne veut être le premier à sortir."

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_4_0_CAFETERIA
    $ current_scene_active = None

    "Je prends enfin la direction de la cafétéria."
    jump _4_0_CAFETERIA_ELEN

label _4_0_CAFETERIA_ELEN:

    $ decouverte_cafeteria = True

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "À peine entré dans la cafétéria, je repère Elen près du comptoir."
    think "Elle ne parle pas. Elle bouillonne."

label _4_0_CAFETERIA_ELEN_PARTIAL:

    call screen day4_cafeteria_elen_gate()

    if _return == "elen":
        $ showGroup([("elen", "colere", 0.55)])
        elen "Noam. Viens voir ça."
        jump _4_0_CAFETERIA_ECRANS

    jump _4_0_CAFETERIA_ELEN_PARTIAL

label _4_0_CAFETERIA_ECRANS:

    scene cafeteria2 at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "Je m'approche d'Elen quand elle se met à crier."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen "Allez, Goumi, s'il te plaît ! Un peu de cannelle. Ou du poivre. Ou un truc qui prouve que j'ai encore une langue ! Allez Steeuuuplait !"

    goumi "Demande refusée, représentante Elen."
    goumi "Les provisions restantes du Conclave ont été redirigées vers la Terre ce matin."

    elen "Quoi ?! Mais nooon, on n'a déjà presque rien ici !"

    elias "Moi, j'voulais juste des barres moins dégueulasses. C'est chaud, elles ont même pas de goût, celles-là."

    nyra "Je crois bien qu'on a pas le choix. J'imagine que c'est un ordre de Kami pour nous punir d'avoir échoué."

    goumi "Ordre direct de Kami. Priorité absolue à la distribution planétaire."

    elen "Mais c'est injuste ! On est coincés ici et on peut même pas avoir un tout petit truc qui soit… différent ?"

    elias "Ouais, on est censés bosser pour tout le monde et on bouffe des trucs immangeables."

    elen "…Je voulais juste que ça ait un peu de goût pour une fois."

    play sound sfx_announce
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh là là, ma petite Elen… Eh bien il faut assumer les conséquences du vote d'hier !"
    kami "Le Conclave ne va tout de même pas devenir un buffet pour privilégiés pendant que la Terre se serre la ceinture."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Équité. Justice. Sacrifice partagé. Vous aimiez beaucoup ces mots, hier."
    kami "Ne vous inquiétez pas trop… de nouvelles provisions arriveront au Jour 7."
    kami "En attendant, contentez-vous de ce que vous avez. Comme tout le monde."
    kami "Et surtout… comme vous l’avez vous-mêmes décidé hier."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "L’écran s’éteint. Elen reste figée deux secondes, les yeux humides. Puis elle tourne les talons et sort presque en courant."

    $ showGroup([
        ("mara", "agace"),
        ("julian", "decu"),
        ("ryn", "colere"),
        ("lysa", "determine"),
        ("kael", "calme"),
        ("iris", "desaccord"),
        ("noam", "neutre"),
    ])
    mara triste "Génial. Kami humilie Elen. Et nous, on contemple le décor. Quel collectif de rêve."

    julian colere "Pff, évidemment, c'était prévisible. Mais finalement, vous le méritez bien."
    julian taquin "Voilà donc la grande victoire que l'histoire retiendra d'hier."

    ryn colere "On a pas besoin de ton avis, Julian."

    lysa triste "C'est inutile de se prendre la tête. Ce qui est fait est fait."

    iris colere "Ouais, c'était évidemment trop en demander de se mettre d'accord."

    noam colere "Bon, calmez-vous. On avancera à rien avec cette mentalité."
    noam reflechit "Cette fois, on a échoué, mais on arrivera sans doute à faire passer autre chose. Ok ?!"

    "Personne ne répond. Chacun se regarde sans vraiment se parler."

    kael reflechit "En attendant, il ne faut pas se leurrer. On a décidé."
    kael triste "Je sais pas si on a foiré ou pas. Mais il faudra l'assumer."

    lysa triste "Ouais... On peut peut-être regarder la télévision, voir ce que les infos disent."

    noam reflechit "Ouais, c'est bien notre seul lien avec l'extérieur."
    noam triste "On devrait la regarder souvent, histoire de pas être tout le temps déconnecté."

    $ j4_cafeteria_ryn_talked = False
    $ j4_cafeteria_julian_talked = False
    call _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE from _call_4_0_cafeteria_television_obligatoire

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("mara", "triste"),
        ("ryn", "colere"),
        ("lysa", "triste"),
        ("kael", "calme"),
        ("iris", "hesitation"),
        ("noam", "reflexion"),
    ])

    think "Je pose ma ration intacte sur la table."

    lysa blase "Alors, Noam ? Tu regrettes qu’on n’ait pas osé ?"
    lysa reflechit "Ou tu es soulagé qu’on ait préféré rester dans nos petites chaînes bien confortables ?"

    menu:
        "Répondre franchement.":
            noam "Je crois que oui."
            noam "Mais je ne sais même pas ce que je regrette exactement."

        "Éviter son regard.":
            noam triste "J'en sais rien... Tu crois qu'ils nous en veulent ?"
            lysa "Je ne sais pas. En tout cas, ils auront à manger aujourd'hui."
            lysa blase "C'est déjà ça..."

        "Regarder les écrans avant de répondre.":
            think "Je regarde les files d'attente. Ma réponse ne vaut pas grand-chose face à ces files."
            noam "Je ne sais plus. J'en sais rien."

    noam reflechit "Je me demande si... ne rien risquer hier... c’était du confort. Ou juste de la peur."

    call day4_tray_scene from _call_day4_tray_scene

    think "Chacun fixe les écrans comme une sentence collective."
    think "On n'a rien gagné. On sait seulement qu'on aurait pu faire mieux."

    jump _4_0_TEMPS_LIBRE_1

label _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE:

    $ room_scene_indices["cafeteria"] = 1
    call screen day4_cafeteria_tv_pnc()

    if _return == "ryn":
        call _4_0_CAFETERIA_PNC_RYN from _call_4_0_cafeteria_pnc_ryn
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    if _return == "julian":
        call _4_0_CAFETERIA_PNC_JULIAN from _call_4_0_cafeteria_pnc_julian
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    if _return != "television":
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    scene bg_cg034 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg034")

    "Le flux d'information bascule sur une rue d'un district que je ne connais pas. Sous une tente, des bénévoles remplissent des sacs de vivres."
    "Les distributions de rationnement continuent. Les cartons passent de main en main, gratuitement, sans interruption."

    think "Sans sourire, également."

    kael "La chaîne tient encore. C'est comme d'hab, ce ne sont pas les institutions qui distribuent. Ce sont les bénévoles."

    iris "Ils donnent tout gratuitement… Alors que notre vote n'a rien arrangé. Pff, la haine."

    noam "Malgré l'échec, voir ça reste un soulagement. Au moins, les gens ne sont pas abandonnés."

    "Un homme récupère son sac sans un mot. Derrière lui, plusieurs personnes crachent au sol en quittant la file."
    "Leurs regards restent braqués sur les cartons et les tentes improvisées. La distribution continue, mais personne ne semble satisfait de ce qu'elle est devenue."

    ryn "Ils ont encore besoin de faire la queue pour qu'on leur donne de quoi tenir une journée. Évidemment qu'ils sont en colère."

    iris "Je te rappelle que t'hésitais encore à changer tout ça hier, c'est peut-être même toi qui as voté contre !"

    ryn "Quoi ?! T'insinues que c'est ma faute, c'est ça ?!"

    noam "Oh oh ! Du calme !"
    noam "C'est bon, c'est du passé, il faut passer à autre chose maintenant !"

    lysa "Le soulagement et l'humiliation dans la même image. Tantale aurait apprécié la mise en scène."

    julian "Tout ça me donne la nausée. Excusez-moi mais je préfère m'en aller."
    return


label _4_0_CAFETERIA_PNC_RYN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("ryn", "colere", 0.70)])

    noam "Ryn… ça va ?"

    ryn colere "Tu sais ce que je comprends pas ? Pourquoi tout le monde est aussi froid avec moi."
    ryn "Ils me regardent comme si j'avais provoqué tout ça. Comme si j'avais choisi les files et les ventres vides."

    noam "Les nerfs sont à vif. Ils cherchent peut-être juste quelqu'un sur qui les poser."

    ryn colere2 "J'ai fait que dire la vérité sur ce qui se passe à Limen !"
    ryn "Les gens attendent des heures. Ils se battent pour des rations. J'allais pas sourire et faire semblant que tout allait bien."

    noam reflexion "Dire la vérité ne veut pas toujours dire que les autres sont prêts à l'entendre."

    ryn colere "Alors qu'ils m'en veuillent. Ça rendra pas Limen moins affamée."

    $ j4_cafeteria_ryn_talked = True
    return


label _4_0_CAFETERIA_PNC_JULIAN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("julian", "neutre", 0.70)])

    noam "Tu ne dis rien. C'est pas vraiment ton genre."

    julian neutre "Je n'ai rien à ajouter."

    noam "Depuis quand ça t'arrête ?"

    julian "J'étais sûr que le texte passerait. Vraiment sûr."
    julian decu "Les arguments étaient là. Les conséquences aussi. Il suffisait de choisir."

    pause 0.4

    julian neutre "Qui a voté contre ?"

    noam surpris "Je ne sais pas. Et même si je le savais—"

    julian "Ce n'était pas une question compliquée, Noam. Qui a voté contre ?"

    noam inquiet "Pourquoi tu veux savoir ?"

    julian "Pour comprendre."
    julian decu "Pour l'instant."

    think "Pas de sourire. Pas de geste pour la caméra. Sa voix est basse, sèche, presque agressive."

    $ j4_cafeteria_julian_talked = True
    return

label day4_optional_news:

    scene bg_cg034 at adaptive_fullscreen with dissolve
    think "Les mêmes distributions continuent de défiler."
    think "Même file. Même attente. Même colère contenue."

    return

label day4_tray_scene:

    $ j4_tray_eaten = []
    think "Je baisse les yeux vers mon plateau."
    think "Il n'y a pas grand-chose à manger là-dedans. Rien n'a l'air vraiment bon."

label day4_tray_scene_loop:

    call screen day4_tray_pnc()

    if _return == "bread":
        $ j4_tray_eaten.append("bread")
        "Je croque."
        think "Ça fait plus de bruit que de goût."
    elif _return == "ration":
        $ j4_tray_eaten.append("ration")
        think "Tiède. Même la température refuse de prendre parti."
    elif _return == "bar":
        $ j4_tray_eaten.append("bar")
        think "Le genre d'aliment qu'on mange uniquement parce que le corps insiste."
    elif _return == "empty":
        think "Je fixe le vide."
        think "C'est idiot, mais c'est ça qui me met le plus en colère."
    elif _return == "finish":
        "Je repousse le plateau de quelques centimètres."
        return

    if len(j4_tray_eaten) >= 3:
        think "Mon corps a compris le message : il n'y aura rien de plus."
        return

    jump day4_tray_scene_loop

label _4_0_TEMPS_LIBRE_1:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"

    "Après le petit-déjeuner, j'ai un peu de temps devant moi."
    think "Je ne sais pas encore quoi faire."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 1.0

    think "L'après-midi s'étire et chacun se sépare. L'espoir d'hier a laissé place à un marasme de honte et de désespoir."
    think "Finalement, pourra-t-on changer quoi que ce soit ?"

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Ahem, je sais bien que vous n'êtes pas encore tout à fait remis, mais le temps ne s'écoule que dans un sens."
    kami "Il va donc falloir passer à la suite. Vous devriez donc venir dans la salle du Conclave !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Un nouveau vote vous attend. Attention, l'audimat monte en FLÈCHE !"

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "L'écran se coupe sous le rire aigu de Kami. Des portes s'ouvrent une à une, puis des pas traînent dans le couloir."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.0

    $ showGroup([
        ("ryn", "colere"),
        ("kael", "inquiet"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("nyra", "raison"),
    ])

    ryn colere "On est vraiment obligé de se retaper tout ça ?"

    kael triste "Julian ne viendra pas. J'ai frappé. Il m'a dit de le laisser."
    kael reflechit "Il avait l'air d'être encore malade."

    mara "On parle bien du même gars ? Genre celui qui faisait tout pour se faire remarquer hier ?"
    mara "MDR ! Quelqu'un pense à prévenir les caméras que leur héros est souffrant ?"

    tomas "M-Mara…"

    mara agace "Quoi ? Tu vas pas me dire que tu le défends ?!"
    mara colere "C'est pas toi qu'il est limite venu menacer hier ?"

    tomas reflechit "Menacer ? J-J'irais pas jusque-là mais..."

    nyra taquin "On a bien fait d'intervenir quand même. Il peut être lourd parfois."
    nyra reflechit "Mais bon, je pensais pas que ça l'affecterait autant. Je pensais que ce n'était que du cinéma."

    ryn colere "Cinéma ou pas, c'est plus reposant d'avoir ce mec loin de nous."
    ryn colere "Surtout si faut continuer ce putain de cirque."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bon, je vois que certains sont en train de chouiner dans leurs lits."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu feras gaffe, mon cher Julian, ton brouilleur n'a pas été réactivé !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Enfin, bref, poursuivons votre petite aventure démocratique ! Je vais donc vous annoncer le prochain vote..."

    play sound sfx_tambour
    pause 2.2

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Je cite : Autoriser les déplacements de personnes entre les districts."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Cette fois la formulation est claire et ne mérite aucune réédition !"
    kami "Oui : libre circulation entre tous les districts."
    kami "Non : les frontières restent fermées comme aujourd’hui."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "C’est simple. C'est binaire. Même vous, vous devriez réussir à comprendre celui-là."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    think "Le mot « frontières » reste dans l'air comme une odeur de brûlé."

    $ showGroup([
        ("lysa", "blase"),
        ("iris", "desaccord"),
        ("elias", "determine"),
        ("kael", "inquiet"),
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("nyra", "raison"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("elen", "triste"),
    ])
    lysa reflechit "On n’a même pas réussi à faire adopter le droit d’acheter ce qu’on veut, et on doit déjà débattre de l’ouverture des frontières ?"

    iris blase "Qu'est-ce qui pourrait mal tourner ? Si ce n'est retourner aux sources de toutes les guerres qui nous ont opposés ?"

    elias reflechit "Ouais, le sujet est chaud, il fera probablement pas l'unanimité. Mais c'est pas inutile."

    kael reflechit "À Orbite, le débat ne nous concerne pas vraiment. On a pas vraiment de frontières avec les autres districts nous."

    ryn sourire "Ah, enfin une proposition qui va dans le bon sens ! Parce que ça fait des années qu’on nous apprend à vivre séparés comme du bétail bien rangé."
    ryn colere "On est des humains putain de merde ! On devrait pouvoir aller partout où on veut !"

    mara colere "Je te rappelle qu'on est les esclaves de Kami, hein."

    ryn colere "À Limen, les frontières, c'est pas qu'une ligne sur une carte. C’est des types armés. C’est des gens qu’on enterre."
    ryn colere "C’est des gosses qui grandissent soit en pensant que de l’autre côté, y a forcément un ennemi, soit en se disant à tout prix qu'ils doivent se barrer de Limen."

    sael reflechit "Ces frontières ont du sens. Tu en parles comme si elles étaient là pour le seul plaisir de nous punir."

    ryn colere "Tu veux qu’on dise quoi ? Merci ?"

    sael determine "Je veux que tu arrêtes de faire semblant de ne pas savoir."
    sael reflechit "Les morts de Limen se souviennent du prix de ces lignes. Les Gardiens aussi."

    noam reflechit "Qu'est-ce que tu veux dire par là ?"

    ryn colere "Pff, comment elle pourrait en parler ! Le Mont Kensen, c'est super loin des frontières."
    ryn triste "Actuellement, quand quelqu'un traverse la frontière, il meurt sur le coup."

    pause 0.5

    ryn colere "BAM ! Un coup de laser dans la nuque."

    lysa blase "Et c'est pour ça que tu veux tout faire sauter ?"

    ryn colere "Parce que j'en ai ras le cul de ramasser des cadavres ! La frontière, je la connais ! Je la garde !"

    iris desaccord "Imaginons qu'on réouvre les frontières : les gens peuvent passer. Super. Et après ?"
    iris desaccord "C'est pas comme s'ils partaient ailleurs pour travailler avec ces foutus bons de rationnement."

    ryn triste "On revient encore là-dessus ?"

    nyra reflechit "Faut dire que tout est lié, Ryn !"

    ryn colere "Me dites pas que vous voulez ignorer tout ça ? Que vous voulez ENCORE voter contre ?!"
    ryn triste "Putain, c'est vraiment ce que vous voulez ? RÉPONDEZ !"

    sael determine "Les frontières sont une digue. Elles nous empêchent de nous faire submerger."
    sael determine "Elles ont un rôle. Et une histoire aussi."

    ryn colere "Non. Moi, j’en ai juste marre de vivre dans une cage."

    call day4_thread_debate_game from _call_day4_thread_debate_game

    sael determine "Alors vote pour. Mais ne compte pas sur moi pour autoriser ça. Je protégerai mes camarades de la haine des autres."
    sael colere "Je voterai contre."
    sael "Et cette fois, c'est certain. Maintenant, excusez-moi."

    hide sael
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Sael se lève ; la chaise racle le sol, puis la porte claque."
    with hpunch
    with vpunch

    mara taquin "SU-PER. À peine la prochaine proposition est-elle annoncée qu’elle est déjà foutue ?"
    mara colere "Un vote foire et, soudain, chacun étale sa névrose sur la table."

    ryn colere "Ferme-la, parle pas de ce que tu connais pas !"

    hide mara
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Mara part juste après elle, presque en rage."

    tomas "Je... Tout est allé trop vite."

    ryn colere "On va surtout nulle part. Comme d’habitude."

    nyra raison "On n'a même pas commencé le vrai débat. Alors dites-moi : vous voulez à tout prix avoir raison, ou enfin commencer à vous écouter pour pas que le vote finisse comme le précédent ?"

    think "Trois sièges vides. Le vote n'a même pas commencé. On est pas sorti de l'auberge..."

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    think "Le débat part comme un fil tiré jusqu'à la rupture."

    call screen day4_objection_fracturee()

    if _return == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure

    return

label day4_thread_debate_success:

    $ j4_argument_circulation_cadre = True
    noam "Attendez."
    noam "Ryn parle d'une cage. Sael parle d'une digue. Iris parle de ce qui arrivera après l'ouverture."
    noam "Vous ne défendez pas la même solution, mais vous refusez tous qu'une nouvelle décision transforme encore des gens en victimes."
    noam "Alors discutons d'un passage encadré : assez libre pour ne plus condamner, assez préparé pour ne pas abandonner."
    think "Ryn ravale sa colère. Iris ne détourne pas les yeux. Même Sael hésite avant de répondre."
    think "Je ne les ai pas ralliés. Mais, pour la première fois, ils discutent de la même chose."
    return

label day4_thread_debate_failure:

    noam "On peut peut-être ralentir et poser un cadre…"
    ryn "Non, Noam. Là, tu empiles juste nos mots pour éviter de choisir."
    sael "Tu veux traduire une peur que tu ne connais pas."
    iris "Et tu promets un cadre qui n'existe encore nulle part."
    think "Ma tentative se dissout avant même de devenir une proposition. Chacun récupère sa colère intacte."
    return

label _4_0_APRES_CLASH_PRE_FETE:

    play music "music/bgm_low_tension.mp3" fadein 2.0

    ryn colere "Super. On a réussi à se déchirer avant même de voter."

    tomas triste "C'est… c'est pas ce qu'on voulait."

    ryn triste "Et pourtant."

    kael reflechit "C'est probablement pas foutu encore, peut-être que quand elle sera..."

    nyra determine "Tu as entendu sa voix : ce soir, elle n'écoutera que sa colère. Il faudra essayer de lui parler calmement demain."

    elias reflechit "Bon. Quelqu'un propose un truc, ou on reste là comme des plantes mortes ? C'est chaud, même elles ont l'air plus vivantes."

    iris sourire "On pourrait se poser un coup à la salle de repos. Enfin, si cette brillante assemblée sait encore décompresser sans se prendre la tête."

    lysa reflechit "Décompresser ? Ouais. Bonne idée en théorie."

    think "Personne ne bouge ni ne répond. Au final, l'invitation meurt sans même être refusée."

    "Ils partent un par un. Tomas d'abord, puis Nyra, Kael et Ryn. Chacun vers sa solitude."
    think "Je reste seul devant les chaises vides et les verres intacts. On n'a pas tenu une journée. Pas même une."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    $ current_period = "Soir"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Finalement, je fais un petit tour par la cafétéria, histoire de prendre quelque chose à grignoter."

    think "Le couloir est désert. Le système, lui, n'a pas besoin de nous pour tourner."
    think "De la lumière sous la porte de Julian. Je ralentis, puis je passe."
    think "Je pourrais frapper. Enfin… pour lui dire quoi ?"

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ blink()
    "La porte de ma chambre se referme d'un clic. Je m'assieds dans le noir."

    pause 1.2

    $ blink()
    think "Sael qui part en claquant la porte. Julian derrière la sienne."
    think "Un siège vide, puis trois."

    pause 0.8

    think "On n'était ni d'accord ni particulièrement proches. Mais on était là. Même ça, on le perd."

    $ blink()
    think "Le plafond reste inerte, rassurant dans sa stupidité totale."

    pause 1.0

    think "La libre circulation ? C'est encore plus chaud à faire adopter !"
    think "Je ne sais plus ce que je veux. Enfin, je ne sais même plus ce qu'on sait faire ensemble."

    think "Ah et puis merde, j'ai même plus faim."
    "Je repose le bout de pain que j'avais embarqué sur mon bureau."

    $ blink()
    pause 0.6

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()
    think "Finalement, la fatigue rend mon corps encore plus lourd."
    think "Une porte s'ouvre dans le couloir. Quelqu'un d'autre ne dort pas."

    $ blink()
    pause 1.5

    think "Une voix. Un vote. Une table. Et douze façons de tout rater."

    pause 0.8

    think "Demain sera peut-être mieux. Je ne suis même plus sûr d'en avoir envie."

    $ blink()
    pause 1.0

    "Le sommeil arrive, lourd, sans rêve et sans réponse."

    $ current_day = 5
    pause 1.5

    call end_day("5") from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

# Total estimé journée 4_0 : ~8m
# Total jour 0-4 : 1h33