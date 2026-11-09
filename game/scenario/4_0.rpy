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
    mara taquin "On vient d'assister à la première insurrection de pâtisserie de l'histoire. Je suis presque émue."
    iris colere "Arrête. C'est pas la cannelle, le problème. C'est que Kami retire nos provisions quand ça lui chante et appelle ça une leçon de morale."
    julian colere "Voilà ! Hier, on aurait pu changer ça ! Mais quelqu'un a préféré qu'on continue à demander la permission pour une pincée de poivre !"
    ryn colere "Tu vas nous ressortir ton discours à chaque petit-déjeuner ? On a voté, bordel !"
    julian taquin "Tant qu'on trouvera normal de supplier une machine pour assaisonner un repas, oui. Tu veux que je parle moins fort ?"
    lysa blase "Il a raison sur le fond. Voilà, je l'ai dit, j'ai honte. Mais engueuler Ryn ne va pas faire réapparaître le commerce."
    ryn colere "ET POURQUOI TU ME REGARDES ?! Vous en savez rien ! Personne ne sait qui a voté contre !"
    noam inquiet "Personne ne sait. Et si on commence à traquer un bulletin anonyme, autant demander à Kami de filmer les isoloirs."
    mara colere "Vous vous disputez pour savoir à qui reprocher une pénurie d'épices. Pendant ce temps, Kami se marre derrière son écran. Beau travail."
    kael reflechit "On peut peut-être vérifier ce qu'elle raconte. Les écrans diffusent les distributions sur Terre. Si les stocks ont bougé, ça devrait laisser une trace."
    lysa neutre "Bonne idée. Une information vérifiable, pour changer. J'avais presque oublié ce que ça faisait."
    noam neutre "Allons voir. Si les gens ont toujours faim malgré les livraisons, Kami ne pourra pas balayer ça d'une plaisanterie."

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

    think "Je m'installe enfin avec mon plateau. Lysa n'a pas quitté l'écran des yeux. Je sens venir une question dont je n'aimerai pas la réponse."
    lysa blase "Alors, Noam ? Tu regrettes le résultat ou tu regrettes surtout de ne pas avoir gagné ?"
    menu:
        "Dire que oui.":
            noam triste "Un peu. J'aurais voulu qu'on arrive à faire quelque chose ensemble. Même si la version de Kami me terrifiait."
            lysa neutre "Au moins, tu sais ce que tu regrettes. C'est déjà mieux que certains."
        "Dire qu'il était trop risqué.":
            noam inquiet "Quand j'ai lu « suppression des rations », j'ai pensé à ceux qui n'auraient aucun moyen de payer leur premier repas."
            lysa reflechit "Oui. Et on ne peut pas traiter cette peur comme une preuve de lâcheté."
        "Admettre que tu ne sais pas.":
            noam neutre "Je ne sais même pas ce que j'espérais. Hier matin, j'étais sûr qu'on pourrait changer les choses. Aujourd'hui, j'ai l'impression qu'on ne pouvait que se tromper."
            lysa blase "Bienvenue au club des gens qui ne savent plus si leur prudence est une victoire."
    iris fatigue "Vous comptez faire le procès du petit-déjeuner jusqu'à ce soir ? Parce que mon pain refroidit. Enfin... il sèche. C'est pire."
    mara taquin "Patience, Iris. À midi, on débattra du sel. Et à seize heures, on votera sur l'existence du dessert."
    "J'essaie de manger. Elias propose de ramollir les barres dans de l'eau chaude. Iris lui demande s'il compte aussi les réparer avec un tournevis."
    think "On n'est d'accord sur rien. Mais entendre une dispute à propos de céréales me repose presque."

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

    "Sur l'écran, des bénévoles remplissent des sacs de nourriture. La file s'étend hors du cadre."
    think "Je ne reconnais pas le district. Je reconnais les regards de ceux qui attendent."
    elias inquiet "Bon... les livraisons continuent. C'est toujours ça. J'avais peur de voir des entrepôts vides."
    kael reflechit "On voit des sacs distribués, pas les stocks. Ça prouve que le système fonctionne encore. Pas qu'il fonctionne mieux."
    iris fatigue "Donc voilà où est partie la cannelle d'Elen. Enfin, j'espère qu'ils n'ont pas prévu de nourrir la file entière avec ça."
    ryn colere "Regardez cette queue ! On va nous expliquer qu'ils ont tous été servis, mais la moitié attend encore dehors !"
    noam inquiet "Au moins, ils reçoivent quelque chose. Mais on ne voit pas ceux qui repartiront les mains vides."
    lysa blase "On a peut-être évité un désastre. Ça ne transforme pas les pénuries actuelles en réussite."
    "Une femme explique à la caméra qu'elle a attendu toute la matinée. Le journaliste lui demande ce qu'elle pense du vote."
    "Elle répond qu'elle aurait aimé que les représentants trouvent une solution, mais qu'elle est soulagée de ne pas perdre ses bons."
    mara reflechit "Elle a peur de perdre ses bons, mais elle voudrait aussi que les choses changent. Pas facile de lui donner tort."
    iris desaccord "On nous a demandé de choisir entre deux risques sans nous laisser prévoir une transition. On était censés faire quel miracle, exactement ?"
    julian colere "On aurait pu essayer ! À force de refuser chaque risque, on va continuer à regarder les mêmes images pendant trente jours !"
    ryn colere "TU VAS ME FIXER COMME ÇA ENCORE LONGTEMPS ?! Le vote était secret ! T'as pas un détecteur de traîtres dans les yeux !"
    julian decu "Je n'ai pas prononcé ton nom."
    ryn colere "JUSTEMENT ! T'AS PAS BESOIN !"
    nyra neutre "Vous êtes en train de fabriquer une accusation à partir d'un regard. Le secret du vote n'est pas un indice. C'est une règle."
    julian decu "Très bien. Je vous laisse avec vos certitudes. Moi, je vais essayer de manger."
    "Julian s'éloigne, son plateau à peine entamé. Ryn le suit des yeux sans ajouter un mot."
    think "C'est presque plus inquiétant que s'il avait crié."
    return

label _4_0_CAFETERIA_PNC_RYN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("ryn", "colere", 0.70)])

    noam inquiet "Ryn... tu comptes manger ce plateau ou le lancer contre le mur ?"
    ryn colere "Fais pas semblant de pas voir. Depuis hier, tout le monde me regarde comme si j'avais saboté le vote !" 
    noam neutre "On ne sait pas qui a voté contre. Même si tu me le demandais, je pourrais pas te répondre."
    ryn colere2 "Je SAIS ! Mais comme j'ai osé parler de Limen et des rations, ils ont décidé que ça suffisait à faire de moi le coupable !"
    noam inquiet "Tu as été l'un des plus inquiets. Je suppose que certains prennent tes arguments pour un aveu."
    ryn colere "Et alors ?! Je devais mentir ? À Limen, des familles dépendent de ces sacs ! J'avais pas le droit de défendre les miens ?!"
    noam neutre "Tu avais raison de le dire. J'aurais seulement voulu qu'on puisse proposer autre chose qu'un oui ou un non."
    ryn triste "Moi aussi..."
    ryn colere "Mais si Julian continue à me fixer comme un traître, je vais finir par lui demander des explications. Et j'aurai pas envie de sourire."
    noam inquiet "Essaie de ne pas lui donner une nouvelle raison de t'accuser. On doit encore voter ensemble."
    ryn colere "Alors va lui dire. Pour une fois que tu distribuerais les conseils dans les deux sens."

    $ j4_cafeteria_ryn_talked = True
    return


label _4_0_CAFETERIA_PNC_JULIAN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("julian", "neutre", 0.70)])

    noam neutre "Julian, ça fait dix minutes que tu fixes la même tranche de pain. Tu veux la convaincre de quelque chose ?"
    julian decu "Pas faim. Et j'en ai assez d'entendre des gens se féliciter d'avoir conservé les pénuries."
    noam inquiet "Personne ne fête le résultat. Tout le monde a vu ce qu'on risquait en supprimant les rations d'un coup."
    julian colere "Et maintenant, des familles continueront à attendre des heures pour un paquet de riz ! Mais bon, nous avons été prudents. Quelle consolation !"
    noam neutre "Ce n'était pas une excuse. Le texte pouvait aussi faire des morts. Tu le sais."
    julian decu "Dis-moi quelque chose, Noam... Tu sais qui a voté contre ?"
    noam surpris "Non. Et je croyais qu'on était d'accord pour ne pas poser cette question."
    julian neutre "Parce que quelqu'un nous a fait échouer. Je voudrais au moins comprendre ce qu'il avait en tête."
    noam inquiet "On était douze. Si la personne voulait expliquer son vote, elle l'aurait déjà fait. C'est son droit."
    julian colere "C'est formidable, ce système ! On peut faire échouer tout le monde sans jamais devoir s'en expliquer !"
    noam colere "Justement ! Le vote est secret pour qu'on ne puisse pas punir ceux qui ne sont pas d'accord. Tu veux vraiment nous enlever ça aussi ?"
    julian decu "Oui. Tu me l'as déjà expliqué hier. Devant Tomas, si tu te souviens."
    "Julian baisse les yeux vers son plateau. Je m'attends à une réplique bien sentie. Elle ne vient pas."
    think "Son silence me met presque plus mal à l'aise que son arrogance."
    julian neutre "Laisse-moi seul, Noam. S'il te plaît."

    $ j4_cafeteria_julian_talked = True
    return

label day4_optional_news:

    scene bg_cg034 at adaptive_fullscreen with dissolve
    think "Les images de distribution tournent en boucle. Des sacs remplis, des files interminables, des sourires devant la caméra."
    think "Je voudrais savoir combien de personnes repartiront réellement avec quelque chose. L'écran ne le dit pas."

    return

label _4_0_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_199
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"

    think "Je quitte la cafétéria avant que quelqu'un propose un deuxième décompte des voix. Je pourrais essayer de parler aux autres... de n'importe quoi qui ne ressemble pas à une élection."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8

    think "J'ai croisé Elias avec des outils, puis Elen poursuivant Goumi pour savoir si le chocolat faisait partie des denrées essentielles."
    think "L'ambiance s'est presque normalisée. C'est précisément le moment que choisit Kami pour intervenir."
    play sound sfx_announce
    pause 0.4
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes petits représentants ! Retour au Conclave ! Une nouvelle proposition vous attend, et elle ne se dévoilera pas toute seule !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous avez profité de votre repos. Personnellement, j'ai trouvé vos disputes beaucoup trop courtes. Nous allons remédier à ça !"
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Ryn râle dans le couloir. À l'entendre, Kami vient personnellement de lui voler la plus belle sieste de sa vie."

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

    ryn colere "ON REVIENT ENCORE ICI ?! Hier on y a passé la moitié de la journée, c'était pas suffisant ?!"
    kael inquiet "Ça risque surtout de commencer sans tout le monde. Julian m'a dit qu'il resterait dans sa chambre. Il n'avait pas l'air d'humeur à discuter."
    mara taquin "Julian qui renonce à une caméra ?! Vous avez vérifié qu'il respirait ? Normalement, elles le suivent naturellement."
    tomas hesitation "Il avait vraiment l'air mal. Je crois que le résultat lui reste en travers de la gorge... même si j'ai pas très envie d'aller lui demander."
    mara agace "Après la façon dont il t'a traité hier, tu vas quand même t'inquiéter pour lui ? Tomas, tu as un problème avec le fait de dire non."
    tomas inquiet "Je peux être en colère contre ce qu'il a fait sans vouloir qu'il aille mal ! C'est pas incompatible, si ?"
    nyra reflechit "Non, ce n'est pas incompatible. Kael, il t'a dit s'il participerait au prochain vote ?"
    kael calme "Il m'a dit qu'il viendrait quand ce serait nécessaire. Pour le reste, j'ai pas insisté."
    ryn colere "Bon, on va faire l'appel toute la journée ou elle peut nous annoncer ce fichu texte ?!"

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Ooooh ! Un siège vide ! Julian, mon chéri, tu boudes encore ? Pourtant, je t'avais réservé ton meilleur angle de caméra !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Rassurez-vous, nous pouvons commencer sans notre star. Je lui enverrai un rappel pour le vote. Peut-être avec des fleurs."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Et maintenant... attention, mes petits représentants... Votre deuxième proposition est..."

    play sound sfx_tambour
    pause 2.2

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Je cite : « Autoriser les déplacements de personnes entre les districts. »"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Cette fois, pas de réécriture, pas de petite surprise grammaticale ! La proposition est suffisamment claire pour rester telle quelle."
    kami "Un vote favorable : les personnes peuvent circuler entre les districts."
    kami "Un vote défavorable : on conserve les frontières actuelles. Et les sanctions qui vont avec, évidemment."
    $ unlock_codex_page("frontieres_interdistricts", with_notification=False)
    $ unlock_dossier_arg("p2_formulation")

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Deux possibilités, pas de petite clause cachée. Alors ? Vous voyez, je sais être généreuse !"

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0

    think "Ryn se redresse comme si quelqu'un venait de le brancher sur une prise. Sael, elle, n'a pas bougé."
    think "Ses mains se sont pourtant refermées sur ses genoux. Ce détail me plaît beaucoup moins."

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
    elen surpris "Attendez ! Là on parle de sortir des districts ? Genre... aller voir quelqu'un sans demander la permission ?"
    ryn sourire "ENFIN ! Un vrai texte ! Là, oui, je signe avec mes deux mains !"
    lysa blase "Tu veux qu'on te donne déjà un bulletin, ou tu peux attendre que Kami finisse sa phrase ?"
    ryn colere "Parce que je sais ce que ça veut dire ! À Limen, quelqu'un franchit la ligne et Kami l'abat. Et c'est nous qui allons ramasser ce qui reste !"
    $ unlock_dossier_arg("p2_frontiere_limen")
    iris desaccord "Je suis contre les exécutions aux frontières, évidemment. Mais si tout le monde peut circuler sans contrôle dès demain, comment on gère les risques ?"
    ryn colere "DONC ON CONTINUE À LES TUER ?! C'est ça, ton idée ?!"
    iris colere "MAIS NON ! Tu pourrais m'écouter jusqu'au bout avant de me faire dire le contraire ?!"
    elias reflechit "Moi, j'imaginais juste... pouvoir aller voir quelqu'un dans un autre district. Un ami, de la famille. Sans avoir l'impression de préparer une évasion."
    kael calme "Orbite est un cas particulier. On a déjà des contrôles d'accès propres à la station. Ça ne se résume pas aux frontières terrestres."
    $ unlock_dossier_arg("p2_orbite")
    sael desaccord "Moi, je voterai contre."
    elen inquiet "Déjà ?! Mais... on vient à peine de découvrir le texte ! Tu peux nous laisser au moins une discussion ?"
    sael determine "Je suis prête à vous écouter. Mais ça n'effacera pas ce que j'ai vu avant la fermeture des frontières."
    ryn colere "Vous avez entendu ?! Elle a déjà décidé ! Alors à quoi bon faire semblant de débattre ?!"
    sael mefiant "Tu m'as demandé pourquoi j'avais peur ? Une seule fois ?"
    ryn colere "Alors explique ! Explique-moi pourquoi tu préfères qu'on continue à se faire descendre aux frontières !"
    sael colere "JE N'AI PAS DIT ÇA ! Tu vas me laisser terminer une phrase, oui ?!"
    nyra reflechit "Sael. Hier, tu as parlé des attaques contre ton village. Est-ce que tu peux nous expliquer ce qui s'est passé ?"
    sael triste "Avant la fermeture, des hommes armés entraient chez nous. Ils prenaient la nourriture. Parfois, ils frappaient les gens."
    sael triste "Quand quelqu'un refusait de leur ouvrir, il y avait des blessés. Et parfois pire."
    sael determine "Depuis que les passages sont fermés, ils ne sont pas revenus."
    sael determine "Je ne vais pas risquer de les voir de nouveau devant nos maisons pour prouver que je suis généreuse."
    elen triste "Je... je savais pas que c'était arrivé chez toi."
    ryn colere "Et moi, je relève des corps à la frontière ! Des gens qui voulaient rejoindre leurs proches ! Tu crois que je peux continuer à les regarder mourir ?!"
    sael mefiant "Non. Je sais que c'est insupportable. Mais si on ouvre tout, comment tu garantis qu'aucune bande armée ne traversera ?"
    ryn colere "Je suis Gardien de Limen ! Surveiller les frontières, c'est mon métier ! On peut les surveiller sans assassiner tous ceux qui approchent !"
    $ unlock_codex_page("frontieres_limen", with_notification=False)
    $ unlock_codex_page("mont_kensen", with_notification=False)
    $ unlock_codex_page("gardiens_limen", with_notification=False)
    mara agace "On est en train de faire comme s'il n'existait que deux méthodes : ouvrir en grand ou fusiller les passants. Vous trouvez ça normal ?"
    sael determine "Peut-être qu'on pourrait organiser des passages sûrs. Mais ce n'est PAS ce que dit ce texte. Il dit qu'on ouvre les frontières. Toutes. Sans autre garantie."
    sael determine "Alors c'est non."
    tomas inquiet "On pourrait peut-être faire des demandes pour visiter un proche ? Un système d'autorisations, sans... sans risques ?"
    lysa blase "Magnifique. On remplacera les frontières mortelles par des formulaires. Je suis sûre que Kami adore."
    iris desaccord "Des autorisations éviteraient peut-être des morts. Mais il faudrait aussi permettre de déménager, de travailler, de circuler. Pas seulement rendre visite à sa grand-mère."
    ryn colere "VOUS COMPRENEZ PAS ?! On devrait pouvoir quitter notre district sans se faire tirer dessus ! C'est quand même pas une demande de fou !"
    sael colere "ET CHEZ MOI, ON DEVRAIT POUVOIR DORMIR SANS AVOIR PEUR DE LES VOIR REVENIR !"
    "Ryn se lève brusquement. Sael ne recule pas. Je vois Nyra déplacer sa chaise pour pouvoir intervenir si la dispute dégénère."
    noam inquiet "Ryn ! Sael ne défend pas les exécutions. Elle essaie de protéger son village. Ça n'efface pas ce qui se passe à Limen."
    ryn colere "JE LE SAIS ! Mais elle s'apprête à dire non au seul texte qui pourrait empêcher ces morts ! Tu veux que je réagisse comment ?!"
    sael determine "Oui, je voterai contre. Je refuse de mettre mon village en danger. Et me hurler dessus ne me fera pas changer d'avis."
    "Elen essaie d'intervenir, mais Ryn parle en même temps qu'elle. Nyra me regarde brièvement, comme pour me demander d'essayer quelque chose."

    call day4_thread_debate_game from _call_day4_thread_debate_game

    sael determine "Je vous ai écoutés. Je sais ce que vous voulez empêcher."
    sael determine "Mais ouvrir toutes les frontières sans garantie, c'est prendre un risque que je ne peux pas imposer à mon village."
    ryn colere "ET TU SAIS CE QUE ÇA VEUT DIRE POUR NOUS ?! On va continuer à ramasser des cadavres !"
    sael triste "Oui, je sais."
    sael triste "Et je déteste que notre sécurité repose sur la mort d'autres personnes. Mais je ne vais pas mettre les miens en danger pour faire semblant d'être courageuse."
    sael determine "Alors je voterai contre. Je vous le dis maintenant, parce que je refuse de vous laisser espérer une voix que vous n'aurez pas."
    "Sael se lève. Ryn ouvre la bouche, puis la referme. Pour une fois, aucun d'eux n'a de quoi répondre."
    hide sael
    with moveoutright
    play sound "sound/sfx_door.ogg"
    "La porte se referme derrière Sael. Personne ne la rappelle."
    mara agace "Bon. Voilà. Une voix contre annoncée avant même le vote. On peut maintenant arrêter de lui hurler dessus ?"
    ryn colere "FACILE À DIRE ! C'est pas toi qui ramasses les gens morts en traversant une frontière !"
    mara colere "Et toi, tu sais ce qu'elle a dû vivre pour arriver à dire ça ?! Elle vient de te raconter ce qui s'est passé dans son village, et tu n'as entendu que son bulletin !"
    ryn colere "JE L'AI ÉCOUTÉE ! Et elle a dit non ! Alors on est censés faire quoi ? Se réjouir de sa franchise ?!"
    mara agace "Très bien. Continue à crier sur ceux qui ne partagent pas ton avis. Ça a merveilleusement fonctionné jusqu'ici."
    "Mara reprend sa tablette et s'éloigne à grands pas."
    think "Elle a presque l'air plus en colère contre Ryn que contre le texte."
    hide mara
    with moveoutright
    play sound "sound/sfx_door.ogg"
    tomas inquiet "Je... j'ai l'impression qu'on vient de perdre le vote avant même d'avoir reçu nos bulletins."
    elen triste "On pourrait peut-être lui reparler ? Je veux dire... pas pour lui forcer la main, mais pour comprendre..."
    nyra reflechit "Pas aujourd'hui. Elle vient de nous expliquer quelque chose de personnel. Revenir à la charge maintenant serait la meilleure manière de lui donner raison de se méfier."
    ryn triste "C'était la première proposition qui pouvait sauver des gens à Limen."
    ryn triste "Et je crois qu'on vient de la voir mourir avant même le vote."
    think "Un seul « non » suffit."
    think "Hier, cette règle m'a paru injuste. Aujourd'hui, j'ai entendu la personne qui pourrait la faire jouer."
    think "Et je ne sais toujours pas comment lui dire qu'elle a tort."

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    think "Ryn parle de ceux qui meurent en voulant traverser. Sael parle de ceux qui risqueraient de mourir si tout le monde pouvait entrer."
    think "Je cherche une phrase qui ne demande à aucun des deux d'oublier ses morts."

    call screen day4_objection_fracturee()

    if _return == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure

    return

label day4_thread_debate_success:
    $ j4_argument_circulation_cadre = True
    noam inquiet "Attendez ! Vous parlez de deux catastrophes différentes. Ryn veut arrêter les exécutions aux frontières. Sael veut empêcher le retour de ceux qui attaquaient son village."
    noam neutre "Il doit bien exister un moyen de contrôler les passages sans tirer sur tous ceux qui approchent. Pas forcément dans ce texte, mais... un moyen."
    iris reflechit "Ça paraît déjà plus sensé. Mais il faudrait des contrôles, des garanties... pas juste écrire « on ouvre » et croiser les doigts."
    ryn inquiet "Moi, tant que les gens peuvent arrêter de mourir pour avoir voulu rejoindre leur famille, je suis prêt à en discuter."
    sael determine "C'est une piste, Noam. Mais elle ne figure pas dans le texte."
    sael determine "Je voterai sur ce qui est écrit. Et ce qui est écrit ne protège pas mon village."
    nyra reflechit "Au moins, on voit enfin où se trouve le désaccord. Si un autre amendement peut traiter les deux risques, il faudra l'envisager."
    think "Ryn finit par se rasseoir. Sael n'a pas changé d'avis. Lui non plus."
    think "Mais ils ont au moins réussi à s'écouter jusqu'au bout. Ça ressemble à un progrès minuscule, et presque ridicule."
    return

label day4_thread_debate_failure:
    noam inquiet "Attendez ! Peut-être qu'on pourrait... enfin, ouvrir seulement certains passages..."
    ryn colere "Lesquels ?! Ceux qui ne t'arrangent pas ?! Tu vois bien que tu ne sais pas toi-même ce que tu proposes !"
    sael desaccord "Noam, je ne peux pas accepter des promesses vagues sur la sécurité. J'ai déjà cru des gens qui m'assuraient qu'il n'y avait aucun risque."
    iris fatigue "Stop. On est en train de demander à des gens terrifiés de nous expliquer calmement pourquoi ils ont peur. Ça ne marchera pas maintenant."
    think "J'ai essayé d'improviser une solution. J'ai surtout donné à chacun une nouvelle raison de se braquer."
    think "Sael reste contre. Ryn a l'air prêt à se battre avec sa chaise."
    return

label _4_0_APRES_CLASH_PRE_FETE:

    play music "music/bgm_world_decline.mp3" fadein 2.0

    ryn colere "Bon. Bravo à tous. On n'a même pas encore voté et on a déjà réussi à se foutre sur la gueule."
    elias reflechit "Moi, je vais manger. Je refuse de mourir d'épuisement pendant une discussion où personne ne m'a demandé mon avis."
    iris sourire "Étonnamment, Elias vient d'avoir une bonne idée. On pourrait se retrouver en salle de repos ce soir. Et je propose une règle : pas un mot de politique."
    lysa blase "Très bien. Mais on confisque le droit de parole à Ryn avant d'entrer."
    ryn colere "OH, ÇA VA ! Je suis parfaitement capable de passer une soirée sans parler des frontières !"
    elen joie "MOI JE VIENS ! Et s'il reste du chocolat quelque part, je le retrouve. Faites-moi confiance !"
    kael calme "Je passerai peut-être après. J'ai encore un détail à vérifier avant de pouvoir me détendre."
    nyra neutre "Très bien. Et demain, si on pouvait attendre au moins cinq minutes avant de hurler, ce serait un progrès mesurable."
    "Iris et Elen commencent aussitôt à débattre des activités autorisées en salle de repos. Ryn s'éloigne en protestant qu'il n'a jamais eu besoin qu'on surveille ses conversations."
    think "J'entends presque la même dispute qu'il y a cinq minutes. Elle me paraît pourtant beaucoup moins grave."
    think "Sael a annoncé qu'elle votera contre. Une seule voix suffit, et nous avons déjà cette voix."
    think "Je n'ai pas envie de lui en vouloir. C'est presque ce qui me fait le plus peur."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Je récupère un morceau de pain à la cafétéria. Rien d'extraordinaire. Aujourd'hui, personne ne s'est battu pour le pain. C'est déjà ça."
    "Une lumière filtre sous la porte de Julian."
    think "Je pourrais frapper. Il m'a demandé de le laisser tranquille ce matin."
    think "Je reste une seconde devant sa chambre, puis je repars. Je ne suis pas sûr de lui rendre service en insistant."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je pose le pain sur mon bureau. Je ne sais même plus pourquoi je l'ai pris."
    think "Ce matin, je voulais oublier le vote d'hier."
    think "Ce soir, je connais déjà une personne qui votera contre le prochain. Et pour des raisons que je n'arrive pas à balayer."
    think "Ryn veut empêcher de nouvelles morts. Sael aussi."
    think "C'est peut-être la chose la plus absurde de cette journée : ils se sont presque battus en voulant protéger les autres."
    "Un éclat de rire me parvient du couloir. Elen, sans doute. Une seconde plus tard, quelqu'un lui demande de parler moins fort."
    think "Au moins, la station ressemble encore parfois à un endroit où l'on peut simplement vivre."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    think "Demain, je pourrai peut-être parler à Sael sans lui demander de choisir entre son village et les morts de Limen."
    think "J'espère surtout réussir à poser une question avant de proposer une solution."
    $ blink()
    "Je ferme les yeux."
    think "Un non a déjà été annoncé. Le vote n'aura lieu que dans deux jours."
    think "Il reste du temps. Je ne sais pas encore si c'est une chance, ou une façon de prolonger l'attente."

    $ current_day = 5
    pause 1.5

    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

# Total estimé journée 4_0 : ~8m
# Total jour 0-4 : 1h33
