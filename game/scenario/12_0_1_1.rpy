label _12_0_1_1_REVEIL_CHAMBRE:
    $ cafeteria_food_level = "low"
    $ current_period = "Nuit"
    $ current_day = 12
    $ noam_has_juliette_drawing = False
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0
    play sound sfx_creak volume 0.6
    "Un bruit me tire du sommeil."
    "Pas celui de la porte. Quelque chose de plus proche. Un frottement, à peine audible, comme si on avait déplacé un objet sur le sol."
    $ investigation_add("bruits_chambre")
    noam faible "... Qui est là ?"
    "Je n'obtiens aucune réponse."
    think "D'accord. Je suis réveillé depuis trois secondes et je commence déjà à parler au mobilier."
    "Je reste allongé. La ventilation souffle normalement. Dans le couloir, rien ne bouge."
    "Je tends la main jusqu'à l'interrupteur."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "L'éclairage me fait cligner des yeux. La porte est fermée. La chaise est à sa place, près du bureau."
    noam hesitation "..."
    "Je vérifie le verrou, puis me retourne vers la pièce."
    think "J'ai entendu quelque chose. J'en suis sûr. Ou alors je recommence à me fabriquer des souvenirs."
    "Hier, les images du couloir avaient disparu. Maintenant, j'ai peur jusque dans ma chambre."
    noam fatigue "Non. Cette fois, je vérifie."
    $ pnc_room = "chambre_j12"
    $ pnc_flags = {}
    $ room_scene_indices["chambre"] = 1
    call screen pnc_chambre_j12()
    return


screen pnc_chambre_j12():
    modal True
    zorder 200
    use room_scene_background("chambre")
    use room_scene_interactions("chambre", {
        "chambre1_aeration": "_12_0_1_1_aeration",
        "chambre1_lit": "_12_0_1_1_sous_lit",
        "chambre1_television": "_12_0_1_1_television",
        "chambre1_tiroir": "_12_0_1_1_bureau",
        "chambre2_armoire": "_12_0_1_1_placard",
        "chambre2_porte_dehors": "_12_0_1_1_recoucher",
        "chambre2_porte_sdb": "_12_0_1_1_salle_de_bain",
        "chambre3_brouilleur": "_12_0_1_1_brouilleur",
        "chambre3_photo_juliette": "_12_0_1_1_photo_juliette",
        "chambre3_tablette": "_12_0_1_1_tablette",
    })
    if room_scene_stem("chambre") == "chambre3" and not noam_has_juliette_drawing:
        $ missing_photo_path = "images/background/interact/chambre/chambre3/photo_juliette.png"
        imagebutton:
            idle room_interaction_null()
            hover room_interaction_null()
            focus_mask room_interaction_layer(missing_photo_path, "chambre", "art")
            xpos 0 ypos 0
            action Jump("_12_0_1_1_photo_juliette")
    frame:
        xalign 0.5 yalign 0.04
        background Solid("#071722DC")
        padding (18, 10)
        text _("FOUILLER LA CHAMBRE  ·  [len(pnc_flags)]/3 INDICES MINIMUM") size 18 color "#DCEFFC"


label _12_0_1_1_aeration:
    $ pnc_flags["aeration"] = True
    "Je m'approche de la grille. Le souffle est régulier, cette fois."
    noam fatigue "Tu vas pas recommencer, toi aussi."
    "Je tends l'oreille. Pas de bruit de pas. Juste la ventilation qui tourne."
    think "Elias serait ravi d'apprendre qu'une machine fait enfin son travail."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_sous_lit:
    $ pnc_flags["lit"] = True
    "Je soulève la couverture, puis m'accroupis pour regarder sous le lit."
    noam hesitation "Bon. Si quelqu'un est là, on peut éviter de se faire peur mutuellement ?"
    "De la poussière, une chaussette et rien d'autre."
    noam fatigue "Formidable. Un suspect, taille trente-neuf."
    "Je récupère la chaussette, puis la pose sur le lit. Je reste malgré moi un instant à regarder sous le sommier."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_television:
    $ pnc_flags["television"] = True
    "Je touche le bord de l'écran mural. Il est froid et éteint."
    think "Pas d'annonce. Pas de visage souriant pour m'expliquer que j'ai rêvé."
    noam fatigue "Pourvu que ça dure."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_placard:
    $ pnc_flags["placard"] = True
    "J'ouvre le placard d'un coup. Les cintres s'entrechoquent, et je sursaute à mon propre bruit."
    noam colere "Putain..."
    "Un sweat est coincé de travers sur l'étagère du haut. Dans la poussière, une marque ressemble à une empreinte de paume."
    "J'approche ma main. La trace pourrait être la mienne. Je n'arrive plus à me rappeler quand j'ai rangé ce sweat."
    think "C'est exactement comme le badge : assez pour m'inquiéter, jamais assez pour être sûr."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_bureau:
    $ pnc_flags["bureau"] = True
    "La tablette est là. Le badge aussi, retourné."
    noam reflexion "Je l'avais remis comme ça ?"
    "Je le retourne, puis m'interromps."
    think "Voilà. Maintenant, si je le retrouve à l'envers demain, je ne saurai même plus comment je l'ai laissé."
    noam fatigue "Bravo, Noam."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_salle_de_bain:
    $ pnc_flags["salle_de_bain"] = True
    "La salle de bain est vide. Le miroir me renvoie un visage pâle, avec des cernes que je ne me connaissais pas."
    noam taquin "Belle tête. Tu devrais te présenter aux élections."
    "L'eau du robinet coule quelques secondes. Je me passe les mains sur le visage."
    "En ressortant, je vérifie quand même derrière la porte."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_brouilleur:
    $ pnc_flags["brouilleur"] = True
    "Le voyant du brouilleur pulse tranquillement."
    noam reflexion "Sept jours pour revoir une chambre..."
    "Le boîtier n'a pas l'air abîmé. Je le fixe, comme s'il allait me donner le nom de celui qui a pris le dessin."
    think "Ce truc est censé protéger ma vie privée. C'est aussi lui qui rendrait une intrusion si difficile à prouver."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_tablette:
    $ pnc_flags["tablette"] = True
    "J'ouvre l'historique de ma tablette. Aucune activité inhabituelle."
    noam fatigue "Ça aurait été trop simple."
    "Je passe à deux doigts d'envoyer un message à Elias pour lui demander s'il est réveillé, puis je renonce."
    think "Il mérite probablement une nuit sans que je lui parle de bruits dans les murs."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_photo_juliette:
    $ pnc_flags["photo_juliette"] = True
    "L'emplacement du dessin de Juliette est toujours vide."
    "Je touche le bord du cadre, puis retire ma main."
    noam faible "Je vais le retrouver."
    "Je suis incapable de dire si je fais cette promesse à elle ou à moi."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_recoucher:
    if len(pnc_flags) < 3:
        think "Pas encore. Si je me recouche sans vérifier, je vais simplement rester à écouter le moindre bruit."
        call screen pnc_chambre_j12()
        return
    "Je reviens au milieu de la pièce. Rien ne manque de plus. Rien ne permet de dire que quelqu'un est entré."
    noam fatigue "Bon. Je suis officiellement le pire enquêteur du Conclave."
    "Je coupe l'éclairage, puis me recouche."
    "Juste avant de fermer les yeux, je vérifie une dernière fois le verrou."
    jump _12_0_1_1_CAFETERIA


label _12_0_1_1_CAFETERIA:
    $ current_period = "Matin"
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    "Je ne parviens pas à retrouver le sommeil. Au bout d'une heure, je finis par abandonner."
    noam fatigue "Super. Je vais avoir besoin d'un café assez fort pour réveiller un mort."
    think "Mauvais choix de mots."
    "Je m'habille et sors en laissant la chambre exactement comme je l'ai trouvée."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_52
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Les couloirs sont déserts. Il fait enfin frais."
    think "Un moment sans personne. Ça devrait être agréable."
    call START_EXPLORATION_LIBRE("_12_0_1_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_nav_j12_cafeteria


label _12_0_1_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_53
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play sound sfx_door
    $ showGroup([("noam", "fatigue", 0.50)])
    goumi "Bonjour, Noam. Tu arrives avant le service."
    noam fatigue "C'est interdit ?"
    goumi "Non. C'est une donnée statistiquement inhabituelle."
    noam taquin "Donc je suis suspect ?"
    goumi "Je n'ai pas dit cela."
    noam fatigue "Tant mieux. J'ai eu ma dose d'interrogatoires."
    "Goumi pivote derrière le comptoir. Un de ses bras range des assiettes tandis que l'autre aligne des tranches de pain d'une précision presque insultante."
    goumi "Que souhaites-tu manger ?"
    noam neutre "Du pain, des œufs, ce que tu as."
    goumi "Je peux te servir des œufs. Pour le pain, ce sera une tranche."
    noam taquin "Une seule ? C'est une punition ?"
    goumi "Non. Le stock est anormalement bas."
    noam reflechit "Anormalement ?"
    goumi "Oui. Nos réserves ont diminué plus vite que prévu. J'ai revu les portions jusqu'à la livraison du quatorzième jour."
    $ investigation_add("manque_nourriture")
    noam inquiet "On est douze, pourtant. Enfin, douze représentants..."
    goumi "Je connais le nombre de représentants, Noam."
    noam fatigue "Ouais. Pardon."
    goumi "Je ne connais pas la cause de l'écart."
    "Je fixe les réserves visibles derrière le comptoir. Le robot a peut-être seulement recalculé les portions. Mais je n'arrive plus à trouver ça banal."
    noam neutre "Une tranche, ça ira."
    goumi "Très bien. Et un verre d'eau. Sael m'a indiqué que tu devais t'hydrater régulièrement."
    noam taquin "Même les robots me surveillent maintenant."
    goumi "Je sers des repas. Je ne surveille pas tes pensées."
    noam fatigue "Ça nous change."
    "Je m'assieds avec mon plateau. Pendant quelques minutes, la cafétéria ressemble enfin à un endroit normal."
    elen "GOUUUUMI !"
    "Je sursaute si fort que ma fourchette tape contre l'assiette."
    $ showGroup([("noam", "fatigue", 0.55), ("elen", "rire", 0.25)])
    play music "music/bgm_fallin_love.mp3" fadein 2.0
    elen joie "Noam ?! Mais tu fais quoi debout à cette heure ?"
    noam fatigue "Je mange."
    elen taquin "Je vois ça ! Je veux dire : VOLONTAIREMENT ?"
    noam taquin "Apparemment, je suis devenu une attraction."
    elen rire "Une attraction qui a failli mourir au Conclave, oui !"
    "Elle s'arrête brusquement."
    elen hesitation "Pardon. C'était nul."
    noam neutre "Un peu."
    elen fatigue "Tu vas mieux ?"
    noam sourire "Je tiens debout. C'est déjà pas mal."
    elen joie "Voilà ! Faut commencer par là ! Goumi, sers-moi le petit-déjeuner de la championne !"
    goumi "Une portion standard ?"
    elen content "Deux portions de pain et..."
    goumi "Une portion standard."
    elen colere "Attends, tu viens de décider à ma place ?!"
    goumi "Je t'informe des quantités disponibles."
    elen desaccord "Mais hier tu m'as déjà servi moins !"
    goumi "Les stocks ont encore diminué."
    elen surpris "Encore ?!"
    noam taquin "Tu as mangé pendant ton sommeil, peut-être."
    elen colere "HÉ ! J'ai jamais fait ça ! Enfin..."
    "Elle réfléchit avec beaucoup trop de sérieux."
    elen hesitation "Une fois, quand j'étais petite. Mais c'était un gâteau. Et on avait laissé la boîte à côté du lit."
    noam rire "D'accord. L'enquête est close."
    "Elle se laisse tomber sur la chaise en face de moi, son plateau à peine rempli."
    elen triste "C'est pas drôle, en fait. Si Goumi doit commencer à compter les tranches de pain..."
    noam neutre "On sera livrés le quatorzième."
    elen reflexion "Oui. Je sais. Mais pourquoi il en manque déjà ?"
    "Je hausse les épaules. Pour une fois, elle ne cherche pas immédiatement une plaisanterie."
    elen neutre "Tu veux ma portion ?"
    noam surpris "Quoi ?"
    elen determine "T'as été malade. Tu devrais manger davantage."
    noam neutre "Elen, tu as négocié cinq minutes pour avoir deux tranches."
    elen taquin "C'est vrai. Elles ont une grande valeur sentimentale."
    noam sourire "Garde-les."
    "Elle fait mine de protéger son pain de ses deux mains."
    elen rire "D'accord. Mais je te préviens : si tu t'écroules à nouveau, je dirai que c'est parce que tu as refusé mon offre !"
    noam taquin "Je prends le risque."
    "Elle mange en silence pendant quelques bouchées, puis pose brutalement sa fourchette."
    elen inquiet "Noam ?"
    noam neutre "Oui ?"
    elen hesitation "Tu es fâché contre nous ?"
    "La question me surprend."
    noam inquiet "Pourquoi tu dis ça ?"
    elen fatigue "Depuis le malaise, tu te tiens à l'écart. Tu regardes les gens d'une manière bizarre. Et hier..."
    noam fatigue "Hier, je cherchais des réponses."
    elen reflechit "Tu peux les chercher avec nous, tu sais."
    noam neutre "Peut-être."
    "Elle hoche la tête et reprend son repas. Je m'attendais à devoir lui expliquer pourquoi je voulais être seul. Elle ne me le demande pas."
    elen taquin "Au fait, tu sais ce que j'ai rêvé cette nuit ?"
    noam fatigue "Je vais regretter de demander ?"
    elen rire "Kami était un cupcake géant et elle nous ordonnait de voter pour choisir qui aurait le droit de la manger."
    noam surpris "Hein ?"
    elen joie "J'ai voté pour tout le monde. Je voulais pas qu'on se dispute."
    noam taquin "Et ça s'est terminé comment ?"
    elen triste "Elle m'a mangée, moi."
    "Je la regarde. Elen se met à rire, puis s'arrête devant mon expression."
    elen neutre "C'était qu'un rêve."
    noam sourire "Ouais."
    "Nous finissons de manger. Je me surprends à lui raconter que j'ai retrouvé une chaussette sous mon lit, ce qui la lance dans une théorie complètement absurde sur les disparitions de linge."
    elen joie "Moi je te dis que la station recycle nos affaires en secret !"
    noam taquin "Un grand complot des chaussettes."
    elen determine "Exactement !"
    "Pendant quelques minutes, j'oublie pourquoi je suis venu si tôt."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_54
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    play sound sfx_announce
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "BONJOUR, mes petits représentants !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous avez bien dormi ! Enfin, à part ceux qui ont décidé de refaire leur chambre en pleine nuit."
    "Je m'arrête net."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote sur les brouilleurs aura lieu aujourd'hui à QUATORZE HEURES précises."
    $ unlock_dossier_chapter(4)
    kami "Ne me forcez pas à aller vous chercher. J'ai un emploi du temps chargé et douze enfants déjà beaucoup trop difficiles à gérer."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous pouvez débattre. Vous pouvez même essayer de me convaincre que la vie privée est un besoin essentiel. J'adore vos petites demandes de privilèges."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais n'oubliez pas : si le texte est rejeté, les zones qui utilisent encore ces appareils seront sanctionnées."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "À tout à l'heure ! Et faites-vous beaux. Votre vote pourrait bien devenir mémorable !"
    hide screen kami_broadcast_ui
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0
    think "Elle a parlé de ma chambre. Elle sait que j'étais réveillé."
    noam fatigue "Évidemment."
    "Je prends le couloir de l'infirmerie, presque sans réfléchir. Le mal de tête de la veille est revenu."
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "bg_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_56
    scene bg_infirmerie at adaptive_fullscreen with dissolve
    sael "Noam ?"
    "Je m'arrête devant l'armoire à pharmacie. Sael arrive du fond de la pièce."
    sael mefiant "Tu cherches quelque chose ?"
    noam fatigue "J'ai encore mal à la tête."
    sael inquiet "Tu aurais pu commencer par me le dire."
    noam taquin "Ça aurait été trop simple."
    sael neutre "Assieds-toi."
    "Elle vérifie ma température et me pose quelques questions. Je ne peux pas m'empêcher de regarder vers le couloir."
    sael reflechit "Tu ne m'écoutes pas."
    noam hesitation "Si."
    sael desaccord "Alors qu'est-ce que je viens de dire ?"
    noam fatigue "Que..."
    sael neutre "Voilà."
    "Elle sort une boîte de médicaments et vérifie l'étiquette."
    sael determine "Si la douleur persiste, on suivra la posologie indiquée. Et tu ne te sers pas au hasard dans l'armoire, compris ?"
    noam neutre "Compris."
    sael inquiet "Tu n'as presque pas dormi, c'est ça ?"
    noam fatigue "Pas beaucoup."
    sael neutre "Alors repose-toi avant le vote. Tu ne rendras service à personne si tu recommences à tomber."
    noam sourire "Promis."
    "Elle n'a pas l'air convaincue, mais me laisse partir."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_57
    scene bg_chambre at adaptive_fullscreen with fade
    "Je m'allonge sur le lit en regardant l'heure défiler."
    think "Quatorze heures. Un vote pour décider si l'on doit garder les brouilleurs. Et quelque part, quelqu'un sait peut-être ce que j'ai vu."
    "J'envisage un instant de retourner parler à Elen. Puis je regarde l'endroit vide où reposait le dessin."
    noam fatigue "Pas maintenant."
    call KD_ROUTE_J12_JULIAN from _call_optional_kd_route_j12_julian
    call OFFER_DAILY_EXPLORATION(
        "_12_0_1_1_ATTENTE_VOTE", 1,
        ["dortoir", "cafeteria", "maintenance", "conclave"],
        _("Rejoindre le vote"), "conclave"
    ) from _call_offer_exploration_j12

# Compatibilité des sauvegardes créées avant la navigation par destination.
# Ces deux points étaient générés par les anciens appels de porte du J12 et
# peuvent encore se trouver dans la pile de retour d'une partie en cours.
label _call_MAYBE_PLAY_SCRIPTED_DOOR_59:
    jump _12_0_1_1_ATTENTE_VOTE

label _call_MAYBE_PLAY_SCRIPTED_DOOR_60:
    jump _12_0_1_1_ATTENTE_VOTE

label _12_0_1_1_ATTENTE_VOTE:

    $ current_period = "Après-midi"
    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_world_decline.mp3" fadein 3.0

    "J'arrive dans la salle du Conclave alors que les derniers représentants prennent place."
    think "14h… Le moment est venu."

    "Les haut-parleurs crachent soudain la voix de Kami."

    play sound sfx_announce
    show screen kami_broadcast_ui
    pause 1.0

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mes chers représentants, votre attention s’il vous plaît."
    kami "Le débat sur l’autorisation ou l’interdiction des dispositifs de brouillage va débuter dans quelques minutes."
    kami "Je vous attends tous dans la Salle du Conclave. Ne tardez pas~"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et essayez de ne pas vous entretuer avant le vote, ce serait dommage."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Presque tout le monde est déjà là. L’ambiance est lourde, électrique."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "triste", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    "Je m’installe discrètement à ma place habituelle."

    tomas "Bon… on y est."
    tomas "Je pense qu’on est tous d’accord pour dire que ce vote est crucial."

    mara "Évidemment qu’on autorise les brouilleurs !"
    $ unlock_dossier_arg("p4_intimite")
    mara stress "J’en peux plus de savoir que Kami peut nous mater 24h/24 !"

    elen "Moi aussi ! J’ai envie de pouvoir danser dans ma chambre sans me sentir jugée !"

    julian taquin "Et moi j’ai envie de pouvoir dire des conneries sans que Kami les enregistre pour plus tard."

    iris "C’est clair… La vie privée, c’est important."

    "Je les écoute en silence, les bras croisés."

    think "Tout le monde est pour."
    think "Même ceux qui étaient hésitants hier semblent avoir basculé."

    sael "Techniquement, tant qu’on respecte les Commandements, on devrait pouvoir avoir notre intimité."

    kael calme "… Tant qu’on respecte les Commandements, oui."

    "Je serre les mâchoires."

    think "Et si on n’avait pas de brouilleurs…"
    think "Est-ce qu’on aurait pu savoir qui m’a volé mes affaires ?"
    think "Est-ce qu’on aurait pu savoir qui a volé la photo de la sœur de Kael ?"

    think "Les brouilleurs… ils protègent peut-être notre intimité…"
    think "… mais ils protègent surtout ceux qui veulent agir dans l’ombre."

    "Cette pensée me reste en travers de la gorge."

    ryn colere "Moi je dis qu’on autorise tout ça. Point final."
    ryn "J’en ai marre de vivre dans un putain de reality show."

    nyra raison "Il faut juste faire attention aux conséquences. Si tout le monde a des brouilleurs, on ne pourra plus rien prouver."
    $ unlock_dossier_arg("p4_preuves")

    "Je reste muet."

    think "Exactement."
    think "Les brouilleurs permettent l’insécurité."
    think "Ils permettent à quelqu’un de se faire passer pour moi, d’effacer des preuves, de voler… sans qu’on puisse jamais rien prouver."

    "Iris me jette un regard en coin."

    iris inquiet "Noam… tu dis rien ?"

    $ bc_show("noam", "fatigue", px=-70, py=-50, pz=0.85)
    noam fatigue "… Je réfléchis."
    $ bc_hide()

    julian taquin "Allez, Noam ! T’es pas d’accord pour qu’on ait enfin un peu d’intimité ?"

    "Je hausse légèrement les épaules."

    noam "Si… bien sûr."

    think "Mais à quel prix ?"

    "La discussion continue autour de moi, animée, presque enthousiaste."
    "Moi, je reste en retrait, perdu dans mes pensées."

    think "Si on vote pour les brouilleurs… on donne encore plus de pouvoir à celui qui se cache parmi nous."
    think "Et je suis le seul à m’en rendre compte ?"

    pause 1.5

    jump _12_0_1_1_DEBAT_VOTE

label _12_0_1_1_DEBAT_VOTE:

    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0

    "Tout le monde parle. Moi, je n'arrive plus à suivre ce qui se dit."

    call j12_play_trolley_problem from _call_j12_play_trolley_problem
    $ j12011_vote_data = _return

    scene bg_conclave at adaptive_fullscreen with fade

    # Le débat a déjà eu lieu avant la simulation : reprendre directement
    # sur la révélation de Noam, sans rejouer les arguments.
    jump _12_0_1_1_DEBAT_TRAITRE

label _12_0_1_1_DEBAT_SECURITE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 2.5

    "La Salle du Conclave est pleine. Tout le monde est présent. L’air est lourd, chargé d’électricité."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas "Bon… on ne va pas tourner autour du pot pendant trois heures."
    tomas "Le vote est clair : est-ce qu’on autorise les dispositifs de brouillage, oui ou non ?"

    mara stress "Pour moi c’est évident ! On autorise !"
    mara "J’en peux plus de vivre comme dans une télé-réalité où Kami nous mate 24h sur 24 !"
    mara "Je veux pouvoir me changer, parler librement, ou même pleurer sans que quelqu’un, ou quelque chose, analyse mes larmes !"

    elen "Moi aussi ! J’ai envie de danser comme une folle dans ma chambre sans me demander si elle est en train de me noter sur 10 !"

    julian taquin "Et moi j’ai envie de pouvoir dire que Kami est une grosse sadique sans qu’elle me le rappelle gentiment le lendemain."

    "Quelques rires nerveux parcourent la salle."

    call play_stat_dialogue("j12") from _call_play_stat_dialogue_11

    elias fatigue "Je comprends l’idée, mais le sujet est quand même important."
    elias fatigue "Sans ça, Kami pourra plus ni nous surveiller, ni nous protéger..."

    lysa inquiet "Alors pas vraiment."
    lysa inquiet "Même avec les brouilleurs, Kami peut avoir accès aux vidéos, mais après une semaine de délai."
    $ unlock_dossier_arg("p4_delai")

    nyra raison "Je peux comprendre l’envie d’intimité… mais il ne faut pas oublier les risques."
    nyra "Si tout le monde a des brouilleurs, comment on prouve quoi que ce soit ?"
    nyra "Le vol chez Kael, par exemple… on ne saura jamais qui c’était."

    kael "… Exactement."

    "Kael parle d’une voix basse, mais tout le monde se tait un instant."

    kael "Si on autorise les brouilleurs, peut-être que je ne saurai jamais qui m'a volé la photo de ma sœur."
    $ unlock_dossier_arg("p4_voleur")
    kael "Je veux savoir qui c'est."

    ryn colere "Et alors ? Tu préfères vivre en prison dorée juste pour avoir une chance de choper un voleur ?"
    ryn "Moi je dis : l'important c'est d'être libre. On n’est pas des animaux de foire."

    sael mefiant "C’est facile à dire tant que ce n’est pas toi qui t’es fait voler un truc précieux."

    "La discussion s’enflamme petit à petit. Je reste silencieux, les bras croisés, à écouter."

    think "Tout le monde penche pour l’autorisation…"
    think "Même ceux qui étaient hésitants hier ont l'air plus convaincus."

    iris "Noam ? Tu dis rien ?"

    "Tous les regards se tournent vers moi."

    noam fatigue "… Je réfléchis."

    julian taquin "Noam, on peut au moins décider de ce qu'on fait dans nos chambres, non ? T'es avec nous ?"

    think "Si on vote pour les brouilleurs…"
    think "Tout le monde pourra vivre l'esprit plus serein..."
    think "Il faudra plusieurs jours à Kami pour savoir ce qui se passe sous les brouilleurs..."

    think "Mais si on vote contre…"
    think "On reste sous la surveillance totale de Kami."
    think "Elle saura tout. Absolument tout. Tout le temps."

    "Je serre les dents."

    noam raison "… La sécurité."

    "Le mot sort plus sèchement que prévu."

    noam "Je ne dis pas que ça me plaît."
    noam fatigue "Je ne dis pas que vivre sous caméra, c’est normal."
    noam determine "Mais les brouilleurs ne protègent pas seulement notre intimité. Ils nous protègent aussi de ceux qui veulent profiter de cette intimité."

    elen "Noam…"

    noam "S’il n’y avait pas eu ces zones mortes, ces coupures, ces moyens de disparaître…"
    noam colere "On saurait déjà qui a volé les affaires de Kael."
    noam colere "Et on saurait aussi qui a touché aux miennes."

    "Kael relève lentement les yeux vers moi."

    kael reflechit "…"

    noam fatigue "On peut appeler ça liberté si vous voulez."
    noam "Je ne suis au final pas sûr que ce soit l'idéal."

    mara stress "Donc ta solution, c’est de laisser Kami nous regarder jusque dans nos chambres ?"

    noam desaccord "il n'y a pas de solution parfaite."

    "Je sens tous les regards peser sur moi."

    "La discussion reprend de plus belle autour de moi, mais je n’écoute plus vraiment."

    pause 1.5

    jump _12_0_1_1_DEBAT_TRAITRE

label _12_0_1_1_DEBAT_LIBERTE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 2.5

    "La Salle du Conclave est pleine à craquer. L’atmosphère est électrique, presque fiévreuse."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas "Très bien… Il faut qu'on arrête de tourner autour du pot."
    tomas "Le vote d’aujourd’hui est clair : est-ce qu’on autorise les dispositifs de brouillage, oui ou non ?"

    mara stress "Autoriser ! Évidemment qu’on autorise !"
    mara "Je refuse de continuer à vivre comme une souris de laboratoire !"
    mara "Je veux pouvoir fermer ma porte, parler librement, pleurer, crier, ou même me disputer sans que Kami analyse tout ce que je fais !"

    elen "Exactement ! J’en ai marre de me sentir observée même quand je danse seule dans ma chambre !"

    julian taquin "Moi je veux pouvoir insulter Kami tranquillement sans qu’elle me le ressorte six mois plus tard avec un petit smiley sadique."

    elias fatigue "Je ne vais pas mentir… moi aussi, l’idée de pouvoir respirer deux minutes sans caméra me tente."
    elias reflechit "Même si je comprends aussi l'intérêt des caméras."

    lysa inquiet "Ça ne règle pas tout. Mais continuer comme ça, avec Kami partout, tout le temps… C'est quand même particulier..."

    ryn colere "Liberté ! Point final !"
    ryn "On n’est pas des putains de prisonniers ! On mérite de pouvoir avoir un minimum d’intimité dans cet enfer !"

    "Plusieurs voix s’élèvent en soutien. L’énergie est clairement du côté de la liberté."

    nyra raison "Je comprends l’envie… vraiment."
    nyra "Mais on ne peut pas ignorer les risques. Si tout le monde porte un brouilleur, comment on prouve quoi que ce soit ?"

    kael "… Comme ce qui m’est arrivé."

    "Le silence retombe un instant."

    kael calme "Kami m'a dit que si on interdit les brouilleurs, je n’aurai probablement jamais accès aux images de ma chambre."
    kael triste "Les brouilleurs seront désinstallés dans toutes les chambres, les images capturées avec..."
    kael "Le voleur restera invisible. Pour toujours."

    sael mefiant "Et si on les interdit ? On reste sous la surveillance totale de Kami. C’est encore moins la solution."

    mara "Exactement ! On échange une prison contre une autre !"
    mara "Moi je préfère risquer l’insécurité plutôt que de vivre dans une cage dorée."
    mara "Qu'est-ce que je risque hein ?! A part qu'un bel homme ait envie de se glisser dans ma chambre ?"

    "La discussion devient de plus en plus animée. Je reste silencieux, les bras croisés, à écouter."

    iris "Noam ? Tu n’as toujours rien dit ?"

    "Les regards convergent vers moi."

    noam fatigue "… Je réfléchis encore."

    julian taquin "Noam ! On a une chance de récupérer un peu de liberté. Tu vas quand même pas nous laisser passer à côté ?"

    "Je sens ma mâchoire se crisper."

    noam fatigue "… Ouais."

    "Le mot me laisse un goût amer dans la bouche."

    noam "Je ne dis pas que c’est sans risque."
    noam hesitation "Je ne dis pas que Kael a tort. Ni Nyra. Ni Tomas."
    noam "Mais si on accepte que Kami voie tout, tout le temps, alors on ne vote plus pour notre sécurité."
    noam desaccord "On vote pour notre obéissance totale à ses règles, même quand elles sont absurdes."

    elen "Donc tu es avec nous ?"

    noam fatigue "Je suis avec personne."
    noam "Je veux juste qu’on garde un endroit où on peut juste être soi-même."

    mara stress "Voilà. C’est exactement ça."

    kael calme "Et si quelqu’un utilise cet endroit pour voler encore ?"

    noam "Alors il faudra le coincer autrement."
    noam "..."

    "Je baisse légèrement les yeux."

    think "Je ne crois même pas totalement à ce que je viens de dire."
    think "Pas comme eux."
    think "Pas tant que je ne sais pas qui, parmi eux, est responsable de tout ça."

    "La discussion reprend de plus belle, passionnée et bruyante."
    "Moi, je reste en retrait, le cœur lourd et l’esprit tourmenté."

    pause 1.5

    jump _12_0_1_1_DEBAT_TRAITRE

label _12_0_1_1_DEBAT_TRAITRE:

    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    "Le débat fait rage depuis plusieurs minutes. Les voix se chevauchent, les arguments fusent."

    mara stress "Bon, on passe au vote et on autorise les brouilleurs, point final ! J’en peux plus de cette surveillance constante !"

    ryn colere "Ouais ! On n’est pas des putains de cobayes !"

    tomas "O-Ouais... C'est peut-être pour le mieux..."

    "Je sens quelque chose craquer en moi."
    "Toutes ces discussions… ces belles paroles… alors que quelqu’un, ici, a effacé les images des caméras."

    noam colere "FERMEZ-LA !"
    with vpunch

    "Le silence tombe d’un coup sur la salle. Tout le monde se tourne vers moi, stupéfait."

    iris inquiet "Noam… ?"

    noam colere "Vous êtes tous là à débattre comme si tout était normal !"
    noam colere "Comme si on était une grande famille heureuse qui doit juste choisir entre avoir un peu d'intimité et vivre en sécurité !"
    noam desespoir "Mais vous êtes aveugles ou quoi ?!"

    julian hesitation "Noam, calme-toi mec…"

    noam colere "Me calmer ?!"
    noam desespoir "Quelqu’un a supprimé les enregistrements des caméras hier soir !"
    noam colere "Dans le couloir près de la salle de stockage ! Juste avant l’annonce !"
    noam peur "Et ce quelqu’un est ici ! Parmi nous !"

    "Un silence de plomb s’abat sur la salle."

    sael mefiant "… Quoi ? De quoi tu parles ?!"

    noam colere "J’ai demandé à Kami de me montrer les images. Elles ont été effacées !"
    noam colere "Nettoyées. Comme si elles n’avaient jamais existé !"
    noam panne "Et ce n’est pas Kami qui l’a fait ! Elle me l’a dit elle-même !"

    mara stress "Attends… tu es en train de nous dire que quelqu’un aurait supprimé les images des caméras ?"
    mara colere "Mais pourquoi quelqu'un irait faire ça ?!"

    noam colere "Oui !"
    noam panne "Quelqu’un qui était là hier soir. Quelqu’un qui savait exactement ce qu’il faisait !"

    elen inquiet "Noam… tu es sûr de ce que tu dis ? Tu étais encore malade hier, peut-être que…"

    noam colere "Ne me parle pas comme si j’étais fou, Elen !"
    noam peur "Il s'est passé quelque chose de bizarre dans ce couloir !"
    noam colere "Et tout a été effacé !"

    ryn colere "Et tu nous accuses nous ?! T’es sérieux là ?!"

    noam colere "Oui ! Parce que c’est forcément l’un d’entre vous !"
    noam triste "Qui d’autre aurait pu le faire ?!"

    kael calme "... Noam. Respire."

    noam colere "Non ! Je ne respire plus !"
    noam fatigue "Quelqu’un ici joue un double jeu !"
    noam colere "Quelqu’un qui sourit, qui vote avec nous, qui fait semblant de s’inquiéter pour moi… et qui efface des preuves dans mon dos !"

    iris inquiet "Noam, arrête… Tu es épuisé, tu as fait un malaise hier, tu—"

    noam colere "Ne me dis pas que je suis épuisé, Iris !"
    noam colere "Je sais ce que j’ai vu !"
    noam peur "Et je sais qu’un de vous ment !"

    sael mefiant "Et tu accuses qui exactement ? Balance un nom si tu es si sûr de toi !"

    noam triste "Je ne sais pas encore qui !"
    noam colere "Mais je sais que c’est l’un d’entre vous !"
    noam fatigue "Je ne sais pas ! Mais quelqu’un ici est un traître !"

    julian hesitation "Woah woah… Noam, tu dérapes là…"
    julian "Un traître ? Carrément ?!"

    elen inquiet "Noam… on est tous avec toi. On s’est inquiétés pour toi hier…"

    lysa inquiet "Personne ne gagne quoi que ce soit à te voir t’effondrer devant nous."

    elias fatigue "Et personne ne devrait voter pendant que tout le monde se jauge comme ça."

    noam fatigue "Arrêtez avec ça !"
    noam inquiet "Je ne veux plus entendre que vous vous inquiétez pour moi !"
    noam colere "L’un de vous a supprimé ces images ! L’un de vous cache quelque chose !"
    noam culpabilite "Et vous êtes tous là à débattre tranquillement sur les brouilleurs comme si rien ne s’était passé !"

    "Ma voix se brise légèrement sur la fin. Je suis essoufflé, tremblant de rage et de fatigue."

    nyra raison "Noam… si ce que tu dis est vrai, on doit en parler calmement. Accuser tout le monde ne nous aidera pas."

    noam colere "Calmement ?!"
    noam desaccord "Comment tu veux que je sois calme ?!"

    "Le silence qui suit est assourdissant."

    iris inquiet "Noam… regarde-moi."
    iris "On est tous fatigués. On est tous sur les nerfs. Mais on est une équipe."

    noam panne "... Une équipe ?"
    noam peur "Une équipe où quelqu’un poignarde les autres dans le dos."

    "Je reste debout, les mains tremblantes."

    "Tout le monde me regarde maintenant avec un mélange de peur, de pitié et de suspicion."

    jump _12_0_1_1_APRES_EXPLOSION

label _12_0_1_1_APRES_EXPLOSION:

    noam fatigue "J’en ai marre."

    iris inquiet "Noam…"

    noam colere "Non."
    noam fatigue "Ce débat ne mène nulle part."

    tomas inquiet "On n’a pas fini le vote."

    noam desaccord "Alors finissez-le sans moi."

    "Personne ne répond."

    "Je tourne les talons avant que quelqu’un trouve une nouvelle phrase pour me retenir."

    play sound sfx_door
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_65
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Le couloir me paraît trop long."
    "Trop blanc."
    "Trop silencieux après tout ce bruit."

    think "Je suis allé trop loin."
    think "Ou pas assez."
    think "Je ne sais plus."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_66
    scene bg_chambre at adaptive_fullscreen with dissolve
    play sound sfx_creak volume 0.6

    $ current_period = "Soir"

    "Je referme la porte de ma chambre derrière moi."
    "Le déclic de la serrure me fait presque sursauter."

    noam fatigue "Putain…"

    "Je ne prends même pas le temps d’enlever correctement mes vêtements."
    "Je m’allonge sur le lit, encore tendu, encore furieux, encore honteux."

    think "Je ne veux plus penser."
    think "Pas au vote."
    think "Pas à Kael."
    think "Pas aux brouilleurs."
    think "Pas à celui qui ment."

    pause 1.5

    "Le sommeil finit par me tomber dessus d’un coup, lourd et sale, comme une coupure de courant."

    scene black with fade
    stop music fadeout 3.0

    call show_chapter_title("Fin du chapitre 4", "Chapitre 4 — Quelque chose ne tourne pas rond") from _call_show_chapter_title_18
    call end_day("13", sleeping=True) from _call_end_day_12_0_1_1

    # L'autre branche J13 n'a pas encore de scenario.
    # getattr evite aussi un NameError sur les sauvegardes ou ce resultat
    # n'a jamais ete defini par le debat.
    if getattr(store, "j12011_wire_result", "security") != "security":
        call screen kd_route_vote_convergence
    jump _13_0_1_1_0_REVEIL_CHAMBRE

# Total journée : 14 minutes 30
# Durée totale : 2h56,20
