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

label _4_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"

    call show_chapter_title("Début du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_2
    $ blink()
    think "Je me réveille un peu avant l'annonce de Kami. J'ai mal dormi, mais j'ai surtout envie d'arrêter de repenser à ce qui s'est passé hier."
    think "Le vote a échoué. Je suis déçu, même si je ne suis toujours pas sûr qu'on aurait dû supprimer les rations."

    "Sur mon bureau, une photographie de quelques amis attire mon attention."
    scene bg_cg029 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg029")
    think "Je reconnais leurs sourires. On avait pris cette photo avant mon départ, un jour où personne n'avait besoin de se demander ce que Kami allait décider pour lui."
    think "J'aimerais savoir ce qu'ils ont pensé du vote. Il faudrait déjà que je puisse les appeler."
    "Je repose le cadre et j'attrape mes vêtements."

    play sound sfx_announce
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Booooonjour, mes petits représentants ! Bien remis de votre premier vote ?"
    kami "Les rations restent en place, les frontières aussi, et personne n'a besoin d'apprendre à faire ses courses. Quelle victoire pour les habitudes !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ne vous inquiétez pas, vous aurez d'autres propositions à examiner. En attendant, j'ai réorganisé certaines livraisons pour que la Terre profite du système que vous avez décidé de garder."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vous conseille d'aller prendre votre petit-déjeuner. Elen risque d'avoir quelques questions. J'ai hâte de l'entendre !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    pause 0.3
    play sound sfx_drop
    "Un objet tombe bruyamment dans le couloir. Quelqu'un jure, puis s'éloigne."
    think "Je finis de m'habiller et je prends ma tablette. Autant aller manger."

    jump _4_0_NAVIGATION_CAFETERIA

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "Je sors de la chambre."
    think "Je croise Elias dans le couloir. Il me fait un signe rapide avant de continuer vers la cafétéria."

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_4_0_CAFETERIA
    $ current_scene_active = None

    "Je prends enfin la direction de la cafétéria."
    jump _4_0_CAFETERIA_ELEN

label _4_0_CAFETERIA_ELEN:

    $ decouverte_cafeteria = True

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_193
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "J'entends Elen discuter avec Goumi au comptoir. Je m'approche pour voir ce qui se passe."
    jump _4_0_CAFETERIA_ECRANS

label _4_0_CAFETERIA_ECRANS:

    scene cafeteria2 at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "Je m'approche d'Elen quand elle se met à crier."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen colere "Goumi, je te demande juste un peu de cannelle ! Hier, t'avais tout un rayon d'épices, elles sont passées où ?"
    goumi "Demande refusée. Les provisions non essentielles du Conclave ont été réaffectées aux distributions terrestres."
    elen surpris "Non essentielles ?! Mais j'ai pas demandé un gâteau de dix étages !"
    elias inquiet "Il reste des barres et des rations normales, ou on mange les emballages maintenant ?"
    goumi "Les repas nécessaires à votre alimentation restent disponibles."
    elias fatigue "Bon, ça, c'est déjà ça. Mais elles ont aucun goût, tes barres."
    nyra reflechit "Attendez, ça concerne seulement les extras ou toutes les livraisons ?"
    goumi "Les provisions non essentielles. Prochain réapprovisionnement prévu au jour 7."
    elen colere "C'est trop facile ! Hier tu nous fais choisir entre deux trucs impossibles, et aujourd'hui tu me retires même la cannelle !"
    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Oh, Elen ! Tu es adorable quand tu essaies de négocier avec Goumi. Il n'a pas d'épices cachées pour tes beaux yeux."
    kami "Les rations restent gratuites, vous vous souvenez ? Les habitants de la Terre en ont besoin bien plus que mes douze invités."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Alors j'ai envoyé une partie de vos réserves là-bas. Pas de famine à bord, ne dramatisez pas ! Vous aurez simplement moins de choix jusqu'à la prochaine livraison."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu pourrais appeler ça de la solidarité, Elen. Après tout, vous avez voulu conserver ce système !"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    elen colere "Mais j'étais POUR l'amendement, moi ! Et puis les gens sur Terre ont besoin de manger, pas de ma cannelle !"
    elias neutre "Techniquement, ça reste de la nourriture..."
    elen colere "Elias, aide-moi un peu !"
    elias inquiet "Désolé. J'essayais."
    "Elen repose son plateau et sort de la cafétéria en marmonnant qu'elle n'a plus faim."
    $ showGroup([
        ("mara", "agace"),
        ("julian", "decu"),
        ("ryn", "colere"),
        ("lysa", "determine"),
        ("kael", "calme"),
        ("iris", "desaccord"),
        ("noam", "neutre"),
    ])
    mara taquin "Je pensais pas voir Elen déclarer la guerre pour un pot de cannelle."
    iris colere "C'est pas la cannelle, Mara. Kami vient de nous rappeler qu'elle peut retirer ce qu'elle veut quand ça l'amuse."
    julian colere "Voilà. Et hier, on avait une chance de changer les choses. Je suis ravi qu'on ait préféré garder les bons."
    ryn colere "Tu vas nous refaire la leçon à chaque repas ?"
    julian taquin "Seulement tant que vous trouverez ça normal d'avoir besoin de la permission de Kami pour acheter du poivre."
    lysa blase "Il marque un point, malheureusement. Mais crier sur Ryn changera pas le résultat."
    ryn colere "Pourquoi tu me regardes quand tu dis ça ? Vous savez même pas qui a voté contre !"
    noam inquiet "Personne le sait, Ryn. Et je crois pas qu'on avancera en essayant de deviner."
    mara colere "Moi, ce qui m'énerve, c'est qu'on s'engueule entre nous alors que Kami est celle qui décide de tout."
    kael reflechit "On pourrait regarder ce que montrent les écrans. Si les réserves sont vraiment parties sur Terre, ça devrait se voir."
    lysa neutre "Ouais, allons voir. Au moins, on aura autre chose que des suppositions."
    noam neutre "D'accord. Je veux aussi savoir si les distributions continuent normalement."

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

    think "Je m'assieds avec mon petit-déjeuner. Lysa regarde encore l'écran, puis se tourne vers moi."
    lysa blase "Alors, tu regrettes le vote d'hier ?"
    menu:
        "Dire que oui.":
            noam triste "Ouais, un peu. J'aurais aimé qu'on arrive à décider quelque chose, même si le texte de Kami était franchement inquiétant."
            lysa neutre "Au moins, tu sais pourquoi t'es déçu."
        "Dire qu'il était trop risqué.":
            noam inquiet "Quand j'ai compris qu'on supprimerait les rations, j'ai eu peur de ce qui arriverait à ceux qui n'ont rien."
            lysa reflechit "Je peux pas vraiment t'en vouloir pour ça. C'était un sacré risque."
        "Admettre que tu ne sais pas.":
            noam neutre "J'en sais rien. J'étais motivé hier matin, et maintenant j'ai l'impression qu'on a été piégés quoi qu'on fasse."
            lysa blase "Ça, je crois qu'on est plusieurs à le penser."
    iris fatigue "Bon, vous allez en parler jusqu'au prochain vote ou on peut au moins finir de manger ?"
    mara taquin "T'inquiète, à midi on discutera de la disparition du sel."
    "Je mange en écoutant leur discussion. Personne n'a l'air ravi, mais Elias et Iris commencent déjà à se chamailler sur la façon de rendre les barres de céréales mangeables."

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

label _4_0_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_199
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"

    "Après le petit-déjeuner, j'ai un peu de temps devant moi."
    think "Je ne sais pas encore quoi faire."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8

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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_202
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0

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
    $ unlock_codex_page("frontieres_interdistricts", with_notification=False)
    $ unlock_dossier_arg("p2_formulation")

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "C’est simple. C'est binaire. Même vous, vous devriez réussir à comprendre celui-là."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0

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
    $ unlock_dossier_arg("p2_orbite")

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
    $ unlock_dossier_arg("p2_frontiere_limen")

    pause 0.5

    ryn colere "BAM ! Un coup de laser dans la nuque."

    lysa blase "Et c'est pour ça que tu veux tout faire sauter ?"

    ryn colere "Parce que j'en ai ras le cul de ramasser des cadavres ! La frontière, je la connais ! Je la garde !"
    $ unlock_codex_page("frontieres_limen", with_notification=False)
    $ unlock_codex_page("mont_kensen", with_notification=False)
    $ unlock_codex_page("gardiens_limen", with_notification=False)

    iris desaccord "Imaginons qu'on réouvre les frontières : les gens peuvent passer. Super. Et après ?"
    iris desaccord "C'est pas comme s'ils partaient ailleurs pour travailler avec ces foutus bons de rationnement."

    ryn triste "On revient encore là-dessus ?"

    nyra reflechit "Faut dire que tout est lié, Ryn !"

    ryn colere "Me dites pas que vous voulez ignorer tout ça ? Que vous voulez ENCORE voter contre ?!"
    ryn triste "Putain, c'est vraiment ce que vous voulez ? RÉPONDEZ !"

    sael determine "Les frontières, c'est ce qui nous empêche de revivre ça. Moi, je veux pas voir revenir la guerre."
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

    play music "music/bgm_world_decline.mp3" fadein 2.0

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
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Finalement, je fais un petit tour par la cafétéria, histoire de prendre quelque chose à grignoter."

    think "Le couloir est désert. Le système, lui, n'a pas besoin de nous pour tourner."
    think "De la lumière sous la porte de Julian. Je ralentis, puis je passe."
    think "Je pourrais frapper. Enfin… pour lui dire quoi ?"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
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

    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

# Total estimé journée 4_0 : ~8m
# Total jour 0-4 : 1h33
