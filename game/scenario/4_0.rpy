default j4_cafeteria_ryn_talked = False
default j4_cafeteria_julian_talked = False
# Résultat du débat : la question du vote reste entière, les relations non.
default j4_frontieres_result = "non_joue"

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

    $ current_day = 4
    $ j4_frontieres_result = "non_joue"
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    call show_chapter_title("Début du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_2

    play sound sfx_drop
    "Un bruit de métal heurte le sol dans le couloir. Un juron suit, aussitôt étouffé."
    think "Ça, au moins, c'est un réveil qui ne parle pas de politique."
    "Je tends l'oreille. Des pas s'éloignent. Pas un cri, pas une alarme. Simplement quelqu'un qui a dû perdre une bataille contre sa valise."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    think "Cette nuit, j'ai rêvé de l'urne. Chaque fois que j'essayais d'y glisser un bulletin, une main le ressortait."
    think "Un seul non, et tout s'est arrêté. J'aimerais pouvoir prétendre que je sais si c'est une bonne nouvelle."

    scene bg_cg029 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg029")
    "Le cadre sur mon bureau a glissé de travers."
    think "Sur la photo, Juliette fait une grimace derrière mon épaule. On avait dû la recommencer quatre fois parce qu'elle refusait de rester sérieuse."
    think "Je pourrais lui raconter ce qui s'est passé. Sauf que je n'ai pas le droit de l'appeler."
    "Je redresse le cadre. Juliette continue de me tirer la langue."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonjour, mes petits perdants ! J'ai une excellente nouvelle : vous avez tous survécu à votre premier exercice de démocratie."
    kami "Et une moins bonne : le monde est toujours exactement comme hier. Quelle débauche de progrès !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Puisque vous avez conservé la distribution gratuite, j'ai fait partir quelques provisions supplémentaires sur Terre. Vous allez être très fiers de vous."
    kami "Elen, je te conseille de prendre ton petit-déjeuner tôt. Pour une fois, je ne plaisante pas."
    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    think "Quand Kami prend soin de préciser qu'elle ne plaisante pas, c'est généralement qu'elle prépare quelque chose de particulièrement drôle pour elle."
    "J'attrape ma tablette, passe ma veste et sors avant qu'elle décide de me réveiller une seconde fois."

    jump _4_0_NAVIGATION_CAFETERIA

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"

    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "En sortant, je croise Elias accroupi devant un casier ouvert. Un outil roule jusqu'à ma chaussure."
    elias gene "Ah ! Merci. Je répare rien, hein. Je vérifie juste que... enfin, ça s'est ouvert tout seul."
    noam sourire "Tu t'es fait attaquer par une boîte à outils ?"
    elias inquiet "Moque-toi. Cette boîte, au moins, elle ne me demandera pas comment j'ai voté."
    "Il récupère l'outil, referme brutalement le casier et file avant que je trouve quoi répondre."

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
    elen colere "Mais c'est une punition ! J'ai voté pour le commerce, et c'est ma cannelle qu'on condamne !"
    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Ooooh, Elen ! Si tu savais comme tu es mignonne quand tu menaces un robot pour un pot de cannelle !"
    kami "J'envoie les provisions superflues là où elles peuvent servir. Et avant que vous me demandiez : oui, les sacs sont déjà partis. Les habitants de la Terre passent avant mes douze petits pensionnaires."
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
    mara taquin "Un pot de cannelle, et voilà notre premier mouvement révolutionnaire. J'espère qu'Elen a prévu un drapeau."
    iris colere "Tu peux rire, mais elle vient de déplacer nos provisions sans consulter personne."
    julian decu "On aurait pu lui enlever ce pouvoir hier."
    ryn colere "Hier, on votait sur un texte qui supprimait aussi les rations. Tu as oublié ce détail ?"
    julian colere "Non. Et je n'ai pas oublié que quelqu'un a décidé à notre place de ne rien tenter."
    lysa blase "Incroyable. Il a réussi à accuser un bulletin de vote sans même le voir."
    ryn colere "Arrête de tourner autour de moi et dis-le si t'as quelque chose à dire !"
    julian neutre "Je n'ai prononcé aucun nom."
    "Ryn repousse son plateau. Mara attrape aussitôt sa tasse pour la mettre à l'abri."
    mara neutre "Vous voulez rejouer le dépouillement ? Parce qu'on avait déjà une excellente ambiance hier."
    noam inquiet "Julian, laisse tomber. Tu ne sais même pas combien de personnes ont voté contre."
    julian decu "C'est bien le problème."
    kael reflechit "Vous pourriez vous battre après avoir vérifié les livraisons ? La télévision diffuse les distributions depuis une heure."
    iris desaccord "Ça ne nous dira pas si Kami avait le droit de nous priver de nourriture."
    kael calme "Non. Mais on saura au moins si quelqu'un l'a reçue."
    "Ryn regarde l'écran. Julian fait semblant de ne pas voir que Ryn regarde."

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

    think "Je m'installe enfin. Lysa a les yeux sur le sachet oublié près de l'écran. Je me demande si elle a faim ou si elle prépare encore une question désagréable."
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
    think "Elen a cessé de réclamer sa cannelle. C'est un changement plus étrange que l'annonce de Kami."

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

    "Sur l'écran, des bénévoles remplissent des sacs de nourriture. Une petite fille saute pour voir par-dessus les adultes."
    elias inquiet "Bon... les livraisons continuent. Je m'attendais presque à voir un entrepôt vide."
    kael reflechit "On voit des sacs, pas les stocks. Mais il y a au moins quelque chose à distribuer."
    "Une bénévole ouvre un carton. Plusieurs sachets portent le même marquage que ceux de notre cafétéria."
    elen "Hé ! C'est nos sachets !"
    "Je me retourne. Elen était censée avoir quitté la pièce pour toujours. Elle a manifestement revu ses conditions."
    iris taquin "Tu es revenue pour identifier le cadavre de ta cannelle ?"
    elen desaccord "Non ! Je voulais voir si Goumi mentait. Et puis... attends."
    "Sur l'écran, la petite fille reçoit un sachet, l'ouvre et plonge aussitôt le nez dedans."
    elen surpris "Mais... elle sourit."
    ryn neutre "Bien sûr qu'elle sourit. Tu crois qu'ils ont souvent le droit à ça, là-bas ?"
    elen inquiet "C'était juste de la cannelle, pour moi."
    "La journaliste tend son micro à une femme derrière la fillette."
    "Elle remercie les bénévoles, puis demande quand arriveront les prochains sacs. On lui répond qu'aucune date n'est confirmée."
    lysa blase "Une bonne livraison. Et aucune garantie pour demain. Les deux peuvent être vrais."
    nyra reflechit "Si Kami veut nous montrer qu'elle distribue mieux, il faudrait les chiffres d'avant et d'après. Pas seulement une caméra."
    mara neutre "Laisse-lui au moins la joie de se féliciter elle-même. Elle ne fait que ça depuis hier."
    elen triste "Bon... Si elle les a vraiment reçus, tant mieux."
    iris reflechit "Ça ne rend pas la décision de Kami correcte."
    elen desaccord "J'ai pas dit ça ! Je peux être contente pour elle ET en colère pour moi, non ?!"
    elias sourire "Ça, je pense qu'on peut tous voter pour."
    "Personne ne rit longtemps."
    "Julian ne regarde pas la fillette. Il regarde Ryn."
    ryn colere "Quoi ?! T'as toujours pas fini avec moi ?!"
    julian decu "Je ne t'ai rien demandé."
    ryn colere "T'as pas besoin d'ouvrir la bouche pour m'accuser !"
    nyra neutre "Vous êtes en train de transformer un regard en résultat de scrutin. Arrêtez."
    "Julian emporte son plateau presque intact. Ryn s'assoit. Cette fois, il ne touche plus à son repas."
    return

label _4_0_CAFETERIA_PNC_RYN:    return

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

    think "J'ai croisé Elias avec ses outils, puis Elen demandant à Goumi si une tablette de chocolat pouvait être considérée comme un traitement d'urgence."
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

    ryn colere "ON REVIENT ENCORE ICI ?! Hier on y a passé la moitié de la journée !"
    kael inquiet "Julian a prévenu qu'il ne viendrait pas. J'ai cru qu'il plaisantait."
    mara taquin "Julian qui fuit une caméra ? Vous avez vérifié qu'il était vivant ?"
    tomas hesitation "Il avait vraiment l'air mal. Je lui ai écrit, mais j'ai effacé le message avant de l'envoyer."
    mara agace "Tomas, tu n'as pas à t'excuser d'être fâché contre lui."
    tomas colere "Je sais ! Mais je n'ai pas dit que je souhaitais qu'il reste seul !"
    "Mara ouvre la bouche, surprise. Tomas baisse déjà les yeux vers sa tablette."
    nyra neutre "On peut lui laisser une journée. On aura assez de raisons de nous disputer sans aller le chercher."

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
    elen surpris "Attendez ! Ça veut dire que je pourrais aller rendre visite à quelqu'un sans demander la permission ?"
    ryn sourire "ENFIN ! Un texte qui sert à quelque chose !"
    lysa blase "Tu l'as adopté en quatre secondes. Nouveau record."
    ryn colere "À Limen, on ramasse des gens qui ont tenté de rejoindre leur famille. Alors oui, j'ai pas besoin d'une semaine pour réfléchir !"
    $ unlock_dossier_arg("p2_frontiere_limen")
    iris reflechit "Et les contrôles ? Sans rien pour organiser les passages, on pourrait avoir d'autres problèmes."
    ryn colere "Donc on les laisse se faire abattre ?!"
    iris colere "J'ai dit qu'il fallait réfléchir aux contrôles ! Pas tirer sur les gens !"
    elias reflechit "Moi, j'aimerais juste pouvoir aller voir des amis sans remplir un dossier. Ça fait si longtemps que..."
    "Elias se tait. Personne ne lui demande de finir."
    kael calme "Sur Orbite, les accès sont déjà surveillés. La situation est différente."
    $ unlock_dossier_arg("p2_orbite")
    sael mefiant "Et les villages qui ne disposent pas de votre surveillance ?"
    ryn colere "On peut surveiller les routes ! On a déjà des gardiens !"
    sael neutre "On en a moins que toi, Ryn."
    "Elle laisse passer quelques secondes, les doigts serrés sur le bord de la table."
    sael neutre "Avant la fermeture, des hommes armés venaient chez nous. Ils prenaient la nourriture, les outils. Parfois ils repartaient avec quelqu'un."
    elen triste "Avec... quelqu'un ?"
    sael triste "On espérait qu'il revienne. On finissait par arrêter de regarder le chemin."
    "Le sourire de Ryn disparaît. Même Mara ne trouve rien à ajouter."
    sael mefiant "Depuis la fermeture, ils ne viennent plus. Vous pouvez trouver ça injuste. Moi, je me souviens de la première nuit où les enfants ont dormi sans sursauter."
    ryn triste "Chez moi, il y a des enfants qui n'ont plus personne à attendre."
    sael triste "Je sais."
    ryn colere "Non. Je crois pas que tu saches !"
    sael colere "Parce que tu es le seul à avoir ramassé un corps, peut-être ?"
    "Ryn se lève, puis se rassoit brutalement."
    nyra raison "Sael, Ryn, personne ne vous demande de comparer vos morts."
    tomas hesitation "On pourrait faire des passages autorisés, avec des gardiens, une liste..."
    ryn colere "Une liste ?! Tu veux savoir combien de noms on a déjà sur nos listes, Tomas ?!"
    tomas peur "Non, je... je parlais de la sécurité, pas..."
    sael mefiant "Une liste n'empêchera pas les bandes armées de franchir les passages."
    iris desaccord "Alors qu'est-ce que tu proposes ? On ne peut pas dire que les tirs sont abominables et les conserver pour toujours."
    sael colere "Ceux qui s'approchent savent pourtant ce qui les attend !"
    "La phrase tombe d'un coup. Sael se fige, comme si elle avait elle-même entendu quelqu'un d'autre parler."
    ryn triste "Oui. Ils le savent."
    ryn triste "Et ils y vont quand même. Tu crois qu'ils font ça pour le plaisir ?"
    sael triste "Ryn, je..."
    ryn colere "Laisse tomber. Maintenant, au moins, je sais ce que tu penses."
    sael colere "NON ! Tu sais ce que j'ai dit parce que j'ai peur ! Ne décide pas à ma place de ce que je pense !"
    mara agace "Vous faites exactement ce que Kami attend de vous. Ça vous rend pas malades ?"
    ryn colere "Si ! Et alors ? Ça va faire revenir ceux que j'ai enterrés ?!"
    sael determine "Je ne peux pas approuver une ouverture sans garantie pour mon village. Pas avec ce texte."
    elen inquiet "Attendez... On pourrait peut-être en discuter ? On a encore deux jours..."
    sael triste "Discuter, oui. Mais je ne vous mentirai pas pour vous faire plaisir."
    "Ryn détourne la tête. Nyra me regarde : pas comme si j'avais une réponse, plutôt comme si j'étais le dernier à ne pas avoir crié."
    call day4_thread_debate_game from _call_day4_thread_debate_game

    if j4_frontieres_result == "pont":
        jump _4_0_DEBAT_APAISE
    else:
        jump _4_0_DEBAT_ROMPU

label _4_0_DEBAT_APAISE:
    "Personne ne bouge. Ryn a baissé les yeux vers ses mains."
    sael reflechit "J'ai dit que ceux qui traversaient savaient ce qui les attendait."
    sael triste "C'était ignoble. Je n'aurais pas dû dire ça."
    ryn triste "Non. Tu n'aurais pas dû."
    sael triste "Je ne peux pas te promettre un vote pour. Mais si tu veux me parler des passages surveillés... je t'écouterai."
    ryn neutre "Alors je te parlerai. Quand j'aurai arrêté d'avoir envie de te hurler dessus."
    mara sourire "Une discussion sans hurlements ? Je prends une photo, personne ne me croira."
    sael neutre "Mara. Pas maintenant."
    mara agace "Oui, bon. Je sais."
    sael determine "Pour l'amendement présenté, je suis contre. Pour le reste, ma porte n'est pas fermée."
    "Elle quitte la salle. Ryn attend que la porte se referme avant de souffler."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "triste"), ("nyra", "raison"),
        ("mara", "agace"), ("tomas", "hesitation"), ("elen", "triste")
    ])
    ryn triste "J'ai cru qu'elle allait me dire que ça n'avait pas compté."
    noam calme "Elle l'a reconnu. Ça ne change pas tout."
    ryn neutre "Non. Mais ça change quelque chose."
    tomas sourire "Alors... il y a encore une conversation possible."
    "Personne n'applaudit. Il n'y a rien à célébrer. Mais Ryn range sa chaise au lieu de la pousser."
    jump _4_0_APRES_CLASH_PRE_FETE

label _4_0_DEBAT_ROMPU:
    sael colere "Vous voulez que je promette quoi ? Que les hommes qui nous ont attaqués ne reviendront pas ?!"
    ryn colere "Je veux que tu regardes en face les gens qu'on tue en prétendant protéger les autres !"
    sael colere "Et moi, je refuse de te donner mon village comme preuve de bonne volonté !"
    "Tomas recule sa chaise. Le bruit fait sursauter Elen."
    tomas inquiet "Sael, je crois que personne ne te demande..."
    sael mefiant "Tomas, s'il te plaît. Pas toi aussi."
    sael determine "Je voterai contre. Et je ne discuterai plus de ça aujourd'hui."
    "La porte se referme derrière elle avant que Ryn ait trouvé de quoi répondre."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "colere"), ("nyra", "raison"),
        ("mara", "agace"), ("tomas", "hesitation"), ("elen", "triste")
    ])
    mara colere "Tu l'as entendue parler de son village, oui ou non ?!"
    ryn colere "Je l'ai entendue dire non !"
    mara agace "Ouais. Ça, on avait remarqué."
    ryn colere "Tu vas me faire la morale aussi ? Tu sais pas ce que c'est !"
    mara neutre "Non. Et je ne vais pas prétendre le contraire."
    mara colere "Mais toi, tu prétends savoir ce qu'elle pense, alors que tu n'as même pas écouté la moitié de ses phrases."
    "Mara part à son tour. Ryn ne la rappelle pas."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "triste"), ("nyra", "raison"),
        ("tomas", "hesitation"), ("elen", "triste")
    ])
    ryn triste "Je voulais juste que quelqu'un dise que ce n'était pas normal."
    iris triste "Personne n'a dit que c'était normal."
    ryn colere "Alors pourquoi ça continue ?!"
    "Cette fois, personne ne cherche à répondre à sa place."
    jump _4_0_APRES_CLASH_PRE_FETE

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:
    think "Je cherche une phrase qui ne demande ni à Ryn d'oublier les morts aux frontières, ni à Sael de rouvrir la porte à ceux qui l'ont terrorisée."
    call refutation_run("j4_frontieres") from _call_day4_frontieres_refutation
    if _return[0] == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure
    return

label day4_thread_debate_success:
    $ j4_frontieres_result = "pont"
    noam determine "Ryn, tu peux lui reprocher de refuser le texte. Pas de vouloir qu'on tue des gens."
    ryn colere "Et je suis censé faire quoi de ceux qui meurent ?!"
    noam inquiet "Ne les abandonne pas. Mais écoute ce qu'elle a vécu avant de lui demander de te suivre."
    sael reflechit "Je ne veux pas qu'on tue qui que ce soit. Je ne veux pas non plus retrouver ces hommes chez nous."
    ryn triste "Alors il faut surveiller les passages. Pas les fermer avec des tirs."
    sael mefiant "Tu peux me garantir que ce sera possible ?"
    ryn neutre "Non."
    "Sael relève enfin les yeux vers lui."
    ryn neutre "Je peux te promettre d'y travailler. C'est tout."
    sael reflechit "C'est la première chose que tu me dis aujourd'hui sans décider à ma place."
    $ unlock_dossier_arg("p2_dialogue_possible")
    return

label day4_thread_debate_failure:
    $ j4_frontieres_result = "rupture"
    noam inquiet "Il doit bien y avoir une solution... des contrôles, une exception, quelque chose !"
    ryn colere "QUELLE exception ?! Tu comprends même pas pourquoi on se dispute !"
    sael mefiant "Tu nous demandes encore de te faire confiance sans rien proposer de précis."
    noam hesitation "Je voulais juste éviter que vous..."
    sael colere "Que nous quoi ? Que nous ayons peur ? Ça te dérange tant que ça ?"
    iris fatigue "Noam, arrête. Là, tu leur demandes de se calmer pour qu'on se sente mieux, nous."
    "J'essaie de reprendre la parole, mais Ryn et Sael se regardent sans plus m'écouter."
    $ unlock_dossier_arg("p2_confiance_brisee")
    return

label _4_0_APRES_CLASH_PRE_FETE:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    if j4_frontieres_result == "pont":
        elen inquiet "Alors... c'est une mauvaise nouvelle et une petite bonne nouvelle ? Je ne sais pas quoi faire de mes mains."
        lysa blase "Essaie de ne pas lancer une campagne de soutien. Juste pour aujourd'hui."
        ryn neutre "On n'a rien gagné. Mais demain, j'essaierai de parler à Sael sans gueuler."
        iris taquin "Prends un chronomètre. Je veux voir combien de secondes tu tiens."
        ryn colere "Oh, ça va !"
    else:
        tomas inquiet "Je... je crois qu'on devrait les laisser tranquilles."
        elen triste "Même Ryn ? Il a l'air tellement mal."
        lysa blase "Surtout Ryn. À moins que tu aies envie de servir de punching-ball à sa mauvaise humeur."
        ryn colere "Je suis encore là, vous savez !"
        iris fatigue "On sait. Tout le couloir doit savoir."
    "Elias se lève, pousse sa chaise, puis se ravise en voyant tout le monde sursauter."
    elias gene "Je voulais juste aller manger. Pardon."
    iris sourire "Excellente idée. Et ce soir, salle de repos. Interdiction de prononcer les mots vote, frontière et amendement."
    elen joie "Même si c'est pour proposer une soirée vraiment géniale ?!"
    lysa taquin "Surtout si c'est toi qui la proposes."
    elen desaccord "Mais j'ai même pas commencé !"
    kael calme "Je vous rejoindrai après. J'ai un petit service à demander dans le dortoir."
    think "Pour une fois, personne ne lui demande lequel."
    jump _4_0_SOIREE_SANS_VOTE

label _4_0_SOIREE_SANS_VOTE:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_evening
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "En arrivant devant la salle de repos, j'entends Elen réclamer un arbitre. Puis un deuxième."
    think "Elle a donc réussi à organiser un conflit sans employer aucun des mots interdits."
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_lounge
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elen", "joie"), ("iris", "taquin"), ("lysa", "blase"),
        ("elias", "sourire"), ("tomas", "sourire"), ("ryn", "neutre"),
        ("noam", "neutre")
    ])
    elen joie "Noam ! Viens ! Elias prétend qu'il a gagné, mais il a triché !"
    elias colere "J'ai pas triché ! J'ai juste rattrapé le dé avant qu'il tombe !"
    iris taquin "Tu as rattrapé le dé et choisi la face. À ce niveau-là, autant écrire le résultat au marqueur."
    tomas sourire "On pourrait recommencer la manche ? Sans toucher au dé cette fois."
    lysa blase "Il faudrait déjà qu'Elen arrête de changer les règles quand elle perd."
    elen desaccord "Je les change pas ! Je les améliore !"
    "Iris éclate de rire. Elen lui lance un coussin ; il frappe Tomas, qui n'avait rien demandé."
    tomas surpris "Moi ?! Mais j'étais de ton côté !"
    elen peur "Pardon ! C'était une attaque diplomatique ratée !"
    ryn sourire "Pour une fois, j'ai rien à voir avec la bagarre. Notez bien la date."
    elias taquin "Tu veux qu'on fasse un compte rendu ?"
    ryn colere "Je vais te faire un compte rendu, moi !"
    iris sourire "Attention. Trois mots interdits et tu sors."
    ryn surpris "J'en ai dit combien ?!"
    lysa sourire "Zéro. Mais on aime te voir paniquer."
    "Je me surprends à rire. Une vraie partie a enfin commencé, sans que personne puisse en annoncer le vainqueur à l'avance."
    if j4_frontieres_result == "pont":
        "Ryn attrape un coussin tombé à terre, le pose près de Tomas et se rassoit."
        ryn neutre "Je crois que j'ai été un peu con, tout à l'heure."
        tomas hesitation "Tu veux une réponse honnête ?"
        ryn sourire "Non. C'était une erreur de ma part."
        "Tomas sourit sans rien ajouter."
    else:
        "Elen tend un dé à Ryn. Il le regarde sans le prendre."
        elen inquiet "Tu n'aimes pas jouer ?"
        ryn triste "Si. Pas ce soir."
        "Il se lève. Elias fait mine de le retenir, puis renonce."
        lysa neutre "Laisse-le. Il reviendra quand il aura envie de nous insulter à nouveau."
    "Kael apparaît à la porte, les mains dans les poches."
    kael calme "J'ai raté quoi ?"
    elen joie "La plus belle injustice de l'histoire des jeux de société !"
    kael sourire "Parfait. J'ai passé ma journée à réparer des choses, j'aimerais bien en casser une."
    iris taquin "Assieds-toi, on a justement besoin de quelqu'un pour expliquer à Elias comment fonctionne un dé."
    elias colere "VOUS ALLEZ ME LÂCHER AVEC CE DÉ ?!"
    "Personne ne prononce les trois mots interdits. Pourtant, la place vide de Sael, et celle de Julian, finissent par se remarquer."
    jump _4_0_FIN_SOIREE

label _4_0_FIN_SOIREE:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    "Une lumière filtre sous la porte de Julian."
    think "Je pourrais frapper. Mais il m'a demandé de le laisser tranquille, et je n'ai pas envie de recommencer à décider pour les autres."
    "Plus loin, j'aperçois un morceau de tissu sombre noué à une poignée. Sael doit déjà être rentrée."
    if j4_frontieres_result == "pont":
        think "Ryn lui reparlera peut-être. Ce n'est pas une victoire ; je n'aurais pas cru qu'un simple peut-être puisse me soulager autant."
    else:
        think "Ryn n'a pas passé la soirée avec nous. Je ne sais pas s'il est rentré dans sa chambre ou s'il cherche encore les mots qu'il aurait voulu dire."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je retrouve la photo sur le bureau. Juliette me tire toujours la langue."
    think "Ce matin, je voulais savoir si un non pouvait être une bonne nouvelle."
    think "Ce soir, j'ai surtout découvert qu'on pouvait vouloir sauver les mêmes personnes et finir par ne plus pouvoir se parler."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    "Un éclat de rire résonne derrière la cloison. Elen, évidemment. Puis une voix lui demande de baisser le ton."
    think "Au moins, ils ont continué la partie sans moi."
    $ blink()
    "Je ferme les yeux. Demain, je pourrai essayer d'écouter Sael sans lui demander de justifier son bulletin."
    $ current_day = 5
    pause 1.5
    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

