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
    think "J'ai dû dormir deux heures. Peut-être trois, si je compte les moments où je regardais le plafond en essayant de ne pas penser au vote."
    think "Raté, évidemment."
    think "On a perdu. Un seul « non » a suffi."
    think "Le pire, c'est que je ne sais toujours pas si ce « non » nous a sauvés d'une catastrophe."

    "Sur mon bureau, le cadre avec la photo de mes amis a légèrement glissé. Je le redresse."
    scene bg_cg029 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg029")
    think "On avait pris cette photo avant mon départ. On avait mis une éternité à se mettre d'accord sur qui se plaçait où."
    think "À l'époque, ça me semblait être le pire débat de ma vie."
    think "Ils ont dû voir le résultat. Qu'est-ce qu'ils en pensent ?"
    think "J'aimerais leur poser la question. Je n'ai même pas le droit de passer un appel."
    "Je repose le cadre. Mon reflet dans la vitre a une tête à faire fuir le petit-déjeuner."

    play sound sfx_announce
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Booooonjour, mes petits représentants ! Alors ? Bien dormi après votre magnifique première défaite ?"
    kami "Les rations restent gratuites, les frontières fermées, et personne n'aura besoin de réapprendre à faire les courses. Quelle audace ! Quel souffle révolutionnaire !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ne boudez pas ! Il y aura d'autres votes. Pour l'instant, j'ai ajusté quelques livraisons : puisque vous tenez tant à la distribution gratuite, autant en faire profiter la Terre !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Allez donc prendre votre petit-déjeuner. Je sens qu'Elen va adorer le menu de ce matin. Rien que d'y penser, je suis ravie !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    pause 0.3
    play sound sfx_drop
    "Un fracas éclate dans le couloir, suivi d'un juron. Quelqu'un vient probablement de commencer sa journée aussi bien que moi."
    think "Je m'habille et j'attrape ma tablette. Kami a insisté sur le petit-déjeuner. Ça ne m'inspire aucune confiance."

    jump _4_0_NAVIGATION_CAFETERIA

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "Je sors. Dans le dortoir, tout le monde semble avoir adopté la même stratégie : ne regarder personne dans les yeux."
    think "Elias me salue en passant. Il ouvre la bouche comme pour me dire quelque chose, puis se ravise."
    think "Même lui ne sait plus comment entamer une conversation. Voilà qui promet."

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_4_0_CAFETERIA
    $ current_scene_active = None

    "J'arrive devant la cafétéria. Avant même d'ouvrir la porte, j'entends une voix familière."
    jump _4_0_CAFETERIA_ELEN

label _4_0_CAFETERIA_ELEN:

    $ decouverte_cafeteria = True

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_193
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "Elen semble mener un interrogatoire serré. Son suspect : un robot de service. Je connais déjà le perdant."
    jump _4_0_CAFETERIA_ECRANS

label _4_0_CAFETERIA_ECRANS:

    scene cafeteria2 at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "Elen frappe du plat de la main sur le comptoir. Goumi ne bronche pas. C'est probablement ce qui l'énerve le plus."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen colere "GOUMI ! Hier, tu avais de la cannelle ! Hier ! Est-ce que quelqu'un a cambriolé le rayon des épices pendant la nuit ?!"
    goumi "Demande refusée. Provisions non essentielles réaffectées aux distributions terrestres."
    elen surpris "NON ESSENTIELLES ?! C'est de la cannelle, pas un lustre en or !"
    elias inquiet "Euh... juste pour savoir, les repas normaux sont encore là ? Ou je dois apprendre à cuisiner les emballages ?"
    goumi "Apports nutritionnels nécessaires maintenus. Repas standards disponibles."
    elias reflechit "Ah. Bon. On survivra, alors. Dommage que la survie ait un goût de carton."
    nyra reflechit "Un instant. Réaffectées à quelles distributions ? Et qu'est-ce qui a été retiré exactement ?"
    goumi "Provisions non essentielles uniquement. Réapprovisionnement du Conclave prévu au jour 7."
    elen colere "Mais c'est une punition ! On a refusé le commerce et maintenant on doit vivre comme si la gourmandise était un crime !"
    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Ooooh, Elen ! Si tu savais comme tu es mignonne quand tu menaces un robot pour un pot de cannelle !"
    kami "Vous avez gardé les rations gratuites. J'envoie donc les provisions superflues là où elles peuvent servir. Les habitants de la Terre passent avant mes douze petits pensionnaires."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rassurez-vous, personne ne mourra de faim à bord. Enfin, pas à cause de la cannelle. Vous aurez simplement un peu moins de choix jusqu'au prochain ravitaillement."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C'est ça, la solidarité ! Vous avez choisi de conserver le système, je vous montre à quel point votre choix est généreux. Tu devrais me remercier !"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    elen colere "MAIS MOI, J'AVAIS DIT OUI ! Et depuis quand les gens sur Terre ont besoin de MA cannelle pour survivre ?!"
    elias neutre "Techniquement... c'est un produit alimentaire."
    elen colere "ELIAS ! C'EST PAS LE MOMENT D'ÊTRE TECHNIQUE !"
    elias inquiet "Désolé ! Je pensais que ça comptait comme un soutien..."
    "Elen repose son plateau avec une dignité blessée, puis quitte la cafétéria en annonçant qu'elle n'a plus faim. Personne ne la croit vraiment."
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

    "L'écran montre une distribution de nourriture dans un district que je ne connais pas. Des bénévoles remplissent des sacs et les donnent à une longue file de personnes."
    elias inquiet "Bon, les livraisons ont pas été coupées. Ça, c'est déjà une bonne chose."
    kael reflechit "Les bénévoles continuent à distribuer ce qu'ils reçoivent. On voit pas si les quantités ont augmenté, par contre."
    iris fatigue "Et voilà pourquoi Elen a plus de cannelle. Je suppose qu'on devrait applaudir."
    ryn colere "T'as vu combien ils sont à attendre ? Ça fait des heures qu'ils font la queue, et certains repartiront quand même sans rien."
    noam inquiet "Je suis content qu'ils reçoivent encore quelque chose, mais ça change pas ce qui nous posait problème hier."
    lysa blase "Exactement. On a évité un changement qui pouvait être dangereux, mais c'est pas pour ça que le système actuel marche bien."
    "Une femme explique à la caméra qu'elle a attendu toute la matinée. Le journaliste lui demande ce qu'elle pense du vote."
    "Elle répond qu'elle aurait aimé que les représentants trouvent une solution, mais qu'elle est soulagée de ne pas perdre ses bons."
    mara reflechit "Bah voilà. Même dehors, les gens savent pas ce qu'ils auraient préféré."
    iris desaccord "Et nous, on avait encore moins d'informations. Franchement, je veux bien critiquer le résultat, mais on pouvait pas faire de miracles."
    julian colere "On aurait quand même pu essayer au lieu de tout refuser."
    ryn colere "T'as pas fini ? On a voté à bulletin secret, alors arrête de regarder les autres comme si tu savais qui a dit non !"
    julian decu "J'ai rien dit sur toi."
    ryn colere "T'as pas besoin de le dire !"
    nyra neutre "On n'a aucun moyen de savoir qui a voté contre. Ce serait peut-être plus utile de regarder ce qu'on peut faire au prochain vote."
    julian decu "Ouais, bon. Je vais manger ailleurs."
    "Julian quitte la table. Ryn le suit des yeux, mais ne répond pas."
    return

label _4_0_CAFETERIA_PNC_RYN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("ryn", "colere", 0.70)])

    noam inquiet "Ryn, t'as l'air de vouloir casser quelque chose. Ça va ?"
    ryn colere "Pas vraiment. J'ai l'impression que depuis hier, tout le monde pense que c'est moi qui ai voté contre."
    noam neutre "Personne peut le savoir. Même moi, je sais pas qui a voté quoi."
    ryn colere2 "Je sais ! Mais comme j'ai parlé de Limen et des rations, ils ont décidé que c'était forcément moi."
    noam inquiet "T'as quand même dit que les supprimer d'un coup serait dangereux. C'est peut-être pour ça qu'ils te soupçonnent."
    ryn colere "Et j'avais pas le droit de le dire ? Chez nous, y a des gens qui comptent sur ces distributions. J'allais pas faire semblant que tout irait bien !"
    noam neutre "Non, t'avais raison d'en parler. J'aurais juste aimé qu'on ait plus de temps pour trouver quelque chose."
    ryn triste "Moi aussi. Mais si Julian me cherche encore, je vais finir par lui répondre autrement."
    noam inquiet "Évite, s'il te plaît. On va devoir revoter ensemble dans quelques jours."
    ryn colere "Ouais, bah dis-lui ça à lui aussi."

    $ j4_cafeteria_ryn_talked = True
    return


label _4_0_CAFETERIA_PNC_JULIAN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("julian", "neutre", 0.70)])

    noam neutre "T'as même pas touché à ton plateau. Tu te sens pas bien ?"
    julian decu "J'ai pas faim. Et j'ai pas tellement envie d'entendre les autres se féliciter d'avoir tout laissé comme avant."
    noam inquiet "Personne se félicite, Julian. Tout le monde était inquiet à cause des rations."
    julian colere "Ouais, et maintenant les gens vont continuer à faire la queue pendant qu'on trouve des excuses."
    noam neutre "On n'avait pas que des excuses. Le texte était vraiment dangereux."
    julian decu "Tu sais qui a voté contre ?"
    noam surpris "Non. Pourquoi tu me demandes ça ?"
    julian neutre "Parce que quelqu'un a empêché le vote de passer, et j'aimerais comprendre pourquoi."
    noam inquiet "On était douze autour de la table. Personne te le dira si la personne veut rester anonyme."
    julian colere "C'est pratique, quand même. Tu peux ruiner les efforts des autres et te cacher derrière le scrutin secret."
    noam colere "Attends, c'est aussi pour ça qu'il est secret ! Si on commence à faire pression sur ceux qui sont pas d'accord, on va jamais avancer."
    julian decu "Je sais. Tu m'as déjà fait le discours hier."
    "Il détourne les yeux vers son assiette. Pour une fois, il n'essaie même pas d'avoir le dernier mot."
    julian neutre "Laisse-moi un peu tranquille, Noam."

    $ j4_cafeteria_julian_talked = True
    return

label day4_optional_news:

    scene bg_cg034 at adaptive_fullscreen with dissolve
    think "La télévision montre toujours les distributions. Certains repartent avec des sacs pleins, d'autres attendent leur tour, mais je ne peux pas savoir combien de gens seront servis aujourd'hui."

    return

label _4_0_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_199
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"

    think "Je vais profiter du temps libre pour voir autre chose que les écrans de la cafétéria. Je n'ai pas envie de passer la journée à discuter du même vote."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8

    think "Pendant l'après-midi, j'ai croisé des représentants qui avaient déjà repris leurs habitudes. Elias cherchait quelque chose à bricoler et Elen essayait de convaincre Goumi de lui trouver du chocolat."
    play sound sfx_announce
    pause 0.4
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes petits représentants, il faudrait venir au Conclave ! Je vais vous annoncer la prochaine proposition."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous serez un peu plus détendus cette fois. Enfin, personnellement, je préfère quand vous vous disputez."
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Je rejoins les autres. Ryn marche devant moi en râlant parce qu'il comptait faire une sieste."

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

    ryn colere "On est vraiment obligés de revenir ici ? On a pas déjà assez perdu de temps hier ?"
    kael inquiet "Ça risque de durer. Julian n'est même pas venu, il m'a dit qu'il voulait rester dans sa chambre."
    mara taquin "Julian qui rate une occasion de se montrer devant les caméras ? Il doit vraiment aller mal."
    tomas hesitation "Il avait pas l'air bien, ce matin. Je crois que le vote lui a fait plus de mal qu'il veut l'admettre."
    mara agace "Il a surtout passé la journée d'hier à te mettre la pression, toi. Tu vas pas me dire que ça t'a plu."
    tomas inquiet "Non, mais j'ai pas envie qu'on recommence à se disputer à cause de lui."
    nyra reflechit "Personne ne l'excuse, mais s'il est malade, il faut le laisser tranquille. Kael, tu penses qu'il reviendra pour le vote ?"
    kael calme "Il a dit qu'il serait là quand il le faudrait. J'en sais pas plus."
    ryn colere "Bon. Il manque quelqu'un, on a compris. On peut savoir pourquoi on est revenus ?"

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Alors, j'en vois un qui manque à l'appel ! Julian, mon chéri, tu comptes passer toute la journée à bouder ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh, ne vous inquiétez pas, je peux annoncer une proposition sans lui. Je lui ferai parvenir son invitation pour le vote."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Et maintenant, passons à la suite ! Votre prochaine proposition est..."

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

    think "Ryn se redresse aussitôt. Sael, elle, ne réagit pas, mais je vois qu'elle serre les mains sur ses genoux."

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
    elen surpris "Ah, ça, c'est pas du tout la même chose que les magasins !"
    ryn sourire "Enfin ! Ça, c'est une proposition que je peux soutenir !"
    lysa blase "T'as même pas attendu qu'elle finisse de parler."
    ryn colere "Parce que je sais de quoi je parle ! À Limen, tu traverses la frontière et Kami te descend. Et après, c'est nous qui récupérons le corps."
    $ unlock_dossier_arg("p2_frontiere_limen")
    iris desaccord "D'accord, mais si tout le monde peut aller partout du jour au lendemain, ça va pas poser des problèmes ?"
    ryn colere "Tu préfères qu'on continue à tuer les gens qui essaient de partir ?!"
    iris colere "C'est pas ce que j'ai dit ! Tu peux arrêter de gueuler deux secondes ?"
    elias reflechit "En fait, ce serait surtout bien pour voir les autres districts, non ? Même juste visiter quelqu'un."
    kael calme "Orbite est un peu à part. Nos déplacements passent déjà par des autorisations spécifiques, pas par les frontières terrestres."
    $ unlock_dossier_arg("p2_orbite")
    sael desaccord "Moi, je suis contre. Je vous le dis tout de suite, je ne veux pas qu'on ouvre ces frontières."
    elen inquiet "Déjà ? Mais on peut en discuter avant !"
    sael determine "On peut discuter. Ça changera pas ce que j'ai vu avant qu'elles soient fermées."
    ryn colere "Voilà ! Elle veut même pas écouter !"
    sael mefiant "Et toi, tu m'as demandé pourquoi j'étais contre ?"
    ryn colere "Vas-y, explique-moi pourquoi c'est si important de laisser Kami tirer sur des gens !"
    sael colere "Arrête de me faire dire des choses que j'ai pas dites !"
    nyra reflechit "Sael, tu parles des attaques contre ton village ? Tu peux nous expliquer ce qui s'est passé ?"
    sael triste "Avant Kami, des groupes armés venaient jusqu'à chez nous. Ils prenaient des récoltes, menaçaient les familles, et si quelqu'un essayait de les arrêter, ça se terminait mal."
    sael determine "Depuis qu'on ne peut plus passer librement d'un district à l'autre, on n'a plus eu à vivre ça. Je ne vais pas prendre le risque de voir ces gens revenir."
    elen triste "Je savais pas... Je suis désolée."
    ryn colere "Et moi, j'en ai marre de ramasser les cadavres de gens qui essaient simplement de rejoindre leur famille ! Tu crois que c'est moins grave ?"
    sael mefiant "Non. Mais si tu ouvres tout sans contrôle, comment tu empêches les groupes armés de revenir ?"
    ryn colere "Je suis un Gardien de Limen ! Je connais les frontières, je passe mes journées à les surveiller !"
    $ unlock_codex_page("frontieres_limen", with_notification=False)
    $ unlock_codex_page("mont_kensen", with_notification=False)
    $ unlock_codex_page("gardiens_limen", with_notification=False)
    mara agace "Et tu crois qu'il y aurait pas une autre façon de surveiller les passages que de tirer sur tout le monde ?"
    sael determine "Peut-être, mais ce n'est pas ce que propose le texte. Il dit qu'on ouvre les frontières entre tous les districts. C'est non."
    tomas inquiet "Et si on demandait à Kami de laisser passer les gens avec une autorisation ? Je sais pas, une demande pour voir sa famille..."
    lysa blase "Ça reviendrait à lui demander la permission pour tout. Comme maintenant, mais avec plus de paperasse."
    iris desaccord "Au moins, ça éviterait peut-être certaines morts. Mais pour travailler ou déménager, il faudrait aussi pouvoir se déplacer."
    ryn colere "Vous êtes en train de tout compliquer pour rien ! On devrait simplement pouvoir sortir de chez nous sans se faire tuer !"
    sael colere "Et chez moi, on devrait pouvoir dormir sans avoir peur de revoir ceux qui nous attaquaient !"
    "Ryn se lève brusquement. Sael ne recule pas. Je vois Nyra déplacer sa chaise pour pouvoir intervenir si la dispute dégénère."
    noam inquiet "Ryn, attends. Sael a peur que les attaques reprennent. Ça veut pas dire qu'elle est d'accord avec les exécutions aux frontières."
    ryn colere "Je le sais, Noam ! Mais elle est en train de dire qu'elle votera non alors qu'on a enfin une chance d'arrêter ces morts !"
    sael determine "Oui, je voterai contre. Je ne veux pas ouvrir les frontières et je ne changerai pas d'avis parce que tu cries."
    "Elen essaie d'intervenir, mais Ryn parle en même temps qu'elle. Nyra me regarde brièvement, comme pour me demander d'essayer quelque chose."

    call day4_thread_debate_game from _call_day4_thread_debate_game

    sael determine "J'ai entendu ce que vous proposez. Mais pour moi, ouvrir les frontières, même avec des précautions, c'est trop dangereux."
    ryn colere "Tu sais que ça veut dire qu'on va continuer à ramasser des morts ?!"
    sael triste "Je sais. Et ça me fait horreur. Mais je refuse de risquer la vie des gens de mon village pour ça."
    sael determine "Je voterai contre. Je préfère être claire maintenant plutôt que de vous laisser croire que je pourrais changer d'avis."
    "Sael se lève. Ryn voudrait répondre, mais elle prend déjà la direction de la porte."
    hide sael
    with moveoutright
    play sound "sound/sfx_door.ogg"
    "Sael quitte la salle sans se retourner."
    mara agace "Bon, au moins elle a été claire. Par contre, Ryn, tu vas arrêter de lui hurler dessus ?"
    ryn colere "C'est facile pour toi ! Tu récupères pas des morts à la frontière !"
    mara colere "Et tu crois que tu sais ce que les autres ont vécu ? Elle t'a parlé de son village et t'as même pas essayé de l'écouter."
    ryn colere "Je l'ai écoutée ! Elle est contre, de toute façon. Alors ça sert à quoi ?!"
    mara agace "Eh ben très bien. Continue à t'énerver contre tout le monde, on va sûrement avancer comme ça."
    "Mara récupère sa tablette et quitte la salle à son tour, visiblement agacée par la dispute."
    hide mara
    with moveoutright
    play sound "sound/sfx_door.ogg"
    tomas inquiet "Je pensais pas qu'ils se prendraient autant la tête..."
    elen triste "Moi non plus. Mais si Sael dit non, on peut plus rien faire, c'est ça ?"
    nyra reflechit "Il faudra peut-être lui reparler, mais pas aujourd'hui. Elle a été très claire, et le vote n'aura lieu que dans quelques jours."
    ryn triste "J'en ai marre. Je pensais vraiment que celle-là, on pouvait la faire passer."
    think "On vient à peine de découvrir la nouvelle proposition et Sael a déjà annoncé qu'elle votera contre. Je comprends mieux pourquoi après ce qu'elle a raconté, même si je n'ai pas envie qu'on abandonne."

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    think "Je cherche comment intervenir sans aggraver la dispute. Ryn et Sael ont tous les deux de bonnes raisons d'avoir peur, mais personne n'arrive à écouter l'autre."

    call screen day4_objection_fracturee()

    if _return == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure

    return

label day4_thread_debate_success:
    $ j4_argument_circulation_cadre = True
    noam inquiet "Attendez, on parle de deux problèmes différents. Ryn veut qu'on arrête de tuer ceux qui traversent, et Sael a peur que des gens dangereux puissent de nouveau venir chez elle."
    noam neutre "Est-ce qu'on pourrait au moins imaginer un système où on contrôle les passages sans abattre les gens ?"
    iris reflechit "Ça serait déjà mieux que ce qu'on a maintenant. Mais ça demanderait de changer d'autres règles."
    ryn inquiet "Moi, ça me va si les gens peuvent arrêter de crever pour avoir voulu sortir de leur district."
    sael determine "Je comprends ce que tu proposes, Noam. Mais l'amendement parle d'ouvrir les frontières, pas de mettre en place ce système. Je reste contre."
    nyra reflechit "Au moins, on a identifié ce qui bloque. On pourra chercher si une autre proposition peut répondre aux deux problèmes."
    think "Ryn se rassoit. Il n'est pas convaincu par Sael, mais il l'a laissée finir cette fois. Elle n'a pas changé d'avis et ne prétend pas le contraire."
    return

label day4_thread_debate_failure:
    noam inquiet "Attendez, je crois qu'on pourrait trouver une autre façon de faire..."
    ryn colere "Une autre façon de faire quoi ? On sait même pas ce que tu proposes !"
    sael desaccord "Tu peux pas simplement nous demander de faire confiance à tout le monde. J'ai déjà essayé, et ça s'est mal terminé."
    iris fatigue "Je crois que là, personne arrive à réfléchir calmement. On ferait mieux d'arrêter avant de dire des trucs qu'on regrettera."
    think "Je n'arrive pas à les faire discuter. Sael reste contre et Ryn est encore plus agacé qu'avant."
    return

label _4_0_APRES_CLASH_PRE_FETE:

    play music "music/bgm_world_decline.mp3" fadein 2.0

    ryn colere "Bon, on a réussi à se disputer alors qu'on vient juste de découvrir le sujet. Ça commence bien."
    elias reflechit "Ouais, bah moi, je vais manger. Je sais pas vous, mais j'ai pas envie de passer tout l'après-midi à m'engueuler."
    iris sourire "Pour une fois, je suis d'accord avec toi. On pourrait se retrouver à la salle de repos plus tard, sans parler de politique."
    lysa blase "On peut essayer. Mais faudra confisquer la tablette de Ryn."
    ryn colere "Oh, ça va, toi !"
    elen joie "Moi je viens ! Si Goumi veut bien me laisser avoir du chocolat, je partage."
    kael calme "Je passerai peut-être après. Il faut que je vérifie quelque chose avant."
    nyra neutre "D'accord. Et demain, on essaiera de discuter sans se mettre à hurler dès le début."
    "Les autres commencent à quitter la salle. Iris et Elen discutent déjà de ce qu'elles pourraient faire à la salle de repos, tandis que Ryn s'éloigne de son côté."
    think "Sael a annoncé qu'elle voterait contre. Ce n'est pas une bonne nouvelle, mais au moins je comprends mieux ce qui lui fait peur. Je me demande si on arrivera à parler de tout ça plus calmement."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Je passe rapidement à la cafétéria pour prendre un morceau de pain avant de retourner dans ma chambre."
    "En traversant le dortoir, je remarque de la lumière sous la porte de Julian. J'hésite à frapper, puis je continue. Il m'a clairement dit qu'il voulait qu'on le laisse tranquille."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je pose le pain sur mon bureau et je m'assieds sur le lit."
    think "J'ai cru qu'on pourrait repartir de zéro avec ce nouveau vote. Mais Sael a déjà décidé qu'elle voterait contre, et je peux difficilement lui en vouloir après ce qu'elle nous a raconté."
    think "Ryn, lui, ne supporte plus de voir des gens mourir près des frontières. J'aimerais bien qu'on puisse les aider sans mettre d'autres personnes en danger."
    "J'entends des voix dans le couloir, puis un rire que je reconnais comme celui d'Elen. Au moins, certains ont réussi à se changer les idées."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    think "Je vais essayer de dormir. Demain, on aura peut-être l'occasion de parler à Sael sans toute la salle autour."
    $ blink()
    "Je finis par m'endormir."

    $ current_day = 5
    pause 1.5

    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

# Total estimé journée 4_0 : ~8m
# Total jour 0-4 : 1h33
