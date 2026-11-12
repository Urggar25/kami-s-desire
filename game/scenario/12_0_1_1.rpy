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
    play music "music/bgm_world_decline.mp3" fadein 2.0
    "Lorsque j'arrive, plusieurs représentants sont debout. Julian gesticule avec une tablette à la main pendant que Mara fait semblant de ne pas l'écouter."
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    julian taquin "Je vous explique qu'on ne peut pas se présenter à un vote pareil sans un minimum de dignité vestimentaire !"
    mara agace "Et moi je t'explique que ton col est de travers depuis ce matin."
    julian surpris "QUOI ?!"
    "Il se précipite sur le reflet d'un écran éteint."
    lysa blase "T'es cruelle, Mara."
    mara taquin "Je sais. Ça me détend."
    iris fatigue "Vous pouvez le laisser tranquille ? Il va encore monopoliser une heure à se recoiffer."
    elen rire "Au moins, on parlerait pas du vote !"
    "Elle s'interrompt en remarquant les regards des autres."
    ryn colere "Moi, j'ai très envie qu'on en parle, du vote."
    tomas inquiet "On a encore quelques minutes. Ce n'est pas la peine de..."
    ryn colere "De quoi ? De se préparer ?"
    tomas "De commencer en s'engueulant."
    ryn colere "Bonne chance."
    "Elias s'est installé devant un verre vide. Il ne participe pas. Kael, lui, garde les mains sur la tablette qu'il n'a pas quittée depuis notre arrivée."
    noam neutre "Salut."
    elias fatigue "Tiens. Le survivant."
    noam taquin "Je vois que tout le monde est très original aujourd'hui."
    elias sourire "J'ai décidé de suivre la mode."
    iris inquiet "Noam, tu tiens le coup ?"
    noam fatigue "Sael m'a fait passer un interrogatoire médical. Je suppose que oui."
    sael neutre "J'ai posé quatre questions."
    noam taquin "Et elles étaient toutes difficiles."
    sael mefiant "Tu as dormi combien d'heures ?"
    noam fatigue "Ça fait une cinquième."
    "Sael soupire. Au fond de la salle, Ryn repousse violemment un siège."
    ryn colere "BON. Qui est contre les brouilleurs ? Qu'on sache tout de suite."
    nyra raison "Ce n'est pas comme ça que fonctionne un scrutin secret."
    ryn colere "Je pose une question, pas un bulletin."
    sael determine "Et tu mets les gens sous pression avant qu'ils aient parlé."
    ryn colere "Je veux éviter un nouveau vote où quelqu'un nous poignarde dans le dos."
    "Je relève la tête. L'expression me reste désagréablement en travers de la gorge."
    mara stress "T'as pas besoin de parler de poignarder quelqu'un à chaque fois qu'on entre ici."
    ryn colere "J'ai pas dit que j'allais le faire !"
    lysa blase "C'est précisément pour ça que tu devrais choisir un autre verbe."
    "Un rire nerveux traverse la table, trop bref pour faire oublier ce qui s'est passé au jour neuf."
    play sound sfx_announce
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "VOILÀÀÀ ! Vous êtes presque à l'heure ! Et quel joli brouhaha, j'aurais dû vendre des billets."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Aujourd'hui, vous devez décider si les dispositifs de brouillage peuvent être possédés, fabriqués et utilisés librement dans les limites des autres Commandements."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Unanimité favorable : l'autorisation entre en vigueur. Sinon, les interdictions et les sanctions prévues s'appliqueront aux zones qui continueront à les utiliser."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je vous laisse un dernier instant pour exprimer vos idées. Et rappelez-vous : parler n'a jamais suffi à éviter un vote."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    mara stress "C'est oui. Pour moi, ça ne devrait même pas se discuter."
    $ unlock_dossier_arg("p4_intimite")
    elen joie "Moi aussi. Je veux pouvoir parler dans ma chambre sans me demander si Kami garde chaque phrase quelque part."
    julian taquin "Et je tiens particulièrement à pouvoir critiquer ce lieu sans qu'une IA me rappelle mes propos au petit-déjeuner."
    iris desaccord "Tu le fais déjà."
    julian "Précisément. Je suis un homme de principes."
    elias reflechit "Ouais, enfin... ça a aussi des inconvénients."
    mara agace "Tu peux pas commencer par être d'accord et t'arrêter là, une fois ?"
    elias fatigue "J'ai essayé. Ça m'a tenu quatre secondes."
    nyra raison "Il faut distinguer le droit à la vie privée du fait qu'un brouilleur peut compliquer une enquête."
    $ unlock_dossier_arg("p4_preuves")
    ryn colere "Donc tu veux que Kami puisse fouiller nos vies dès qu'une affaire tourne mal ?"
    nyra reflechit "Ce n'est pas ce que j'ai dit."
    ryn colere "Ça y ressemble."
    kael calme "Ce serait quand même bien d'avoir les images quand on nous vole quelque chose."
    "Sa voix est calme. Tout le monde l'a entendue."
    $ unlock_dossier_arg("p4_voleur")
    sael mefiant "Tu sais que personne ici ne minimise ce qui t'est arrivé."
    kael triste "Alors arrêtez de me demander de patienter."
    "Sael ne répond pas."
    elen inquiet "Mais si on interdit les brouilleurs, on n'aura jamais la certitude de ce qui s'est passé dans sa chambre..."
    tomas raison "Pas forcément. Il y a ce délai de sept jours. Les données restent indisponibles pendant cette période, même avec l'appareil en place."
    $ unlock_dossier_arg("p4_delai")
    call play_stat_dialogue("j12") from _call_play_stat_dialogue_11
    iris reflechit "On sait déjà tout ça. Kael a essayé d'accéder aux archives."
    kael fatigue "Oui. J'ai essayé."
    noam reflexion "Et les couloirs, eux..."
    "Je m'interromps. Lysa me regarde."
    lysa reflechit "Quoi, les couloirs ?"
    noam fatigue "Rien. Continuez."
    lysa blase "Formidable. C'est devenu une habitude."
    ryn colere "Je vote pour, et c'est tout ! Je suis pas venu jusqu'ici pour demander à une caméra la permission d'aller pisser."
    mara taquin "Ça te ferait pas de mal de demander la permission avant certaines choses."
    ryn colere "QUOI, ENCORE ?!"
    sael determine "On peut être favorables au texte sans nier les risques. Et on peut parler des risques sans vouloir condamner ceux qui utilisent ces appareils."
    elias reflechit "Merci. C'est à peu près ce que j'essayais de dire."
    iris taquin "En beaucoup moins clair."
    elias fatigue "Je sais."
    "J'ai l'impression que nous rejouons la même dispute depuis des jours, avec des arguments différents et les mêmes visages de plus en plus fatigués."
    noam inquiet "Et si quelqu'un se sert des brouilleurs pour nous faire du mal ?"
    "La question m'échappe plus sèchement que je ne le voudrais."
    julian inquiet "C'est une possibilité. Mais on ne peut pas retirer toute liberté simplement parce que quelqu'un pourrait mal agir."
    noam reflechit "Et si c'est déjà arrivé ?"
    iris inquiet "Noam..."
    kael calme "C'est déjà arrivé. On m'a pris la photo de Léa."
    mara stress "Et Noam a perdu le dessin de sa sœur."
    lysa reflechit "Personne n'a encore prouvé que les brouilleurs avaient servi à ces vols."
    "Elle dit ça en me regardant. Je détourne les yeux."
    nyra raison "On devrait éviter de confondre ce qu'on sait et ce qu'on imagine."
    "C'est une remarque raisonnable. Elle me donne pourtant envie de taper sur la table."
    jump _12_0_1_1_DEBAT_VOTE


label _12_0_1_1_DEBAT_VOTE:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    "Le débat se poursuit, malgré les rappels de Kami. Je voudrais qu'on tranche, puis je me rappelle ce qui peut arriver lorsqu'on tranche trop vite."
    call j12_play_trolley_problem from _call_j12_play_trolley_problem
    $ j12011_vote_data = _return
    scene bg_conclave at adaptive_fullscreen with fade
    "Je reste assis après la simulation. Plusieurs représentants ont déjà recommencé à parler autour de moi."
    think "Quoi qu'on choisisse, on ne peut pas faire disparaître les risques en refusant d'y penser."
    jump _12_0_1_1_DEBAT_TRAITRE


label _12_0_1_1_DEBAT_SECURITE:
    # Compatibilité des anciennes sauvegardes : les débats alternatifs
    # rejoignent désormais la confrontation commune.
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5
    $ showGroup([
        ("noam", "fatigue", 0.18), ("kael", "calme", 0.42),
        ("mara", "stress", 0.66), ("nyra", "raison", 0.88),
    ])
    noam reflexion "Je sais ce que vous allez dire : qu'il faut accepter le risque pour avoir un peu de liberté."
    mara stress "Si tu veux nous répondre, réponds. Mais nous fais pas le discours à notre place."
    noam inquiet "Quelqu'un a volé des affaires dans nos chambres, et les caméras ne nous aideront pas avant plusieurs jours."
    kael calme "Je le sais. Crois-moi."
    nyra raison "Le problème existe. Autoriser les brouilleurs ne le résoudra pas, mais les interdire n'effacera pas les vols."
    noam fatigue "Je sais."
    "Je baisse les yeux. Ce que je voudrais vraiment dire n'a presque rien à voir avec les appareils."
    jump _12_0_1_1_DEBAT_TRAITRE


label _12_0_1_1_DEBAT_LIBERTE:
    # Compatibilité des anciennes sauvegardes : conserver ce label.
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5
    $ showGroup([
        ("noam", "fatigue", 0.18), ("ryn", "colere", 0.42),
        ("sael", "mefiant", 0.66), ("lysa", "inquiet", 0.88),
    ])
    ryn colere "J'ai pas signé pour qu'une IA puisse regarder chez moi quand elle veut !"
    sael mefiant "Personne ne te demande de lui remettre tes clés."
    noam reflexion "Je veux aussi qu'elle nous laisse tranquilles. Je sais juste plus si ça suffira à nous protéger."
    lysa reflechit "Ça ne suffira pas. Mais ça n'en fait pas une mauvaise décision."
    "Ryn se tait. Moi aussi."
    jump _12_0_1_1_DEBAT_TRAITRE


label _12_0_1_1_DEBAT_TRAITRE:
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    mara stress "Bon. On a fait le tour, non ? On peut enfin voter ?"
    tomas inquiet "Il manque encore quelques précisions sur le texte."
    ryn colere "Sérieusement, Tomas ?!"
    tomas raison "Oui, sérieusement. Le statut des dispositifs existants, par exemple."
    elias fatigue "Oh, non. On va refaire l'épisode des campements."
    elen inquiet "Ne dis pas ça..."
    julian taquin "Je propose qu'on vote pour ne plus jamais entendre l'expression « déclaration préalable »."
    iris desaccord "Julian, ferme-la une seconde."
    "Les discussions repartent. Je regarde successivement les visages. Elen qui se mord la lèvre, Elias qui s'enfonce dans son fauteuil, Kael qui ne lâche pas sa tablette."
    think "Hier, ils étaient tous dans ma chambre. Ils m'ont apporté à manger. J'ai même ri avec eux."
    think "Les données de la caméra ont été supprimées. Kami a dit qu'un accès autorisé était responsable."
    "Je regarde le siège de Lysa. Elle me fixe déjà."
    lysa inquiet "Noam ?"
    noam fatigue "..."
    mara agace "Non, mais c'est bon, on peut discuter pendant trois jours de toute façon, ça changera rien au..."
    noam colere "ARRÊTEZ !"
    with vpunch
    "Ma voix claque plus fort que prévu. Mara tourne la tête vers moi, stupéfaite."
    elen inquiet "Noam ?"
    noam colere "Vous pouvez arrêter de parler des brouilleurs pendant trente secondes ?!"
    ryn colere "C'est littéralement le sujet du vote !"
    noam colere "JE SAIS !"
    "Je me lève. Ma chaise recule brutalement."
    iris inquiet "Noam, assieds-toi."
    noam inquiet "Non. J'ai besoin de vous dire un truc."
    sael mefiant "Alors dis-le. Mais sans hurler."
    noam reflexion "Hier, j'ai demandé à Kami les enregistrements du couloir près de l'infirmerie. À l'heure où j'ai cru voir quelque chose."
    julian hesitation "Et ?"
    noam inquiet "Ils ont été supprimés."
    "Le silence n'arrive pas immédiatement. Ryn commence à répondre, mais Tomas le coupe."
    tomas surpris "Supprimés ? Pas simplement indisponibles à cause du brouillage ?"
    noam colere "SUPPRIMÉS. Le terminal l'a affiché."
    kael calme "Tu es sûr du créneau ?"
    noam desaccord "J'ai vérifié !"
    lysa reflechit "Et Kami t'a dit quoi ?"
    noam inquiet "Que ça venait d'un accès autorisé. Pas d'elle."
    "Nyra relève la tête. Elle ne dit rien tout de suite."
    mara stress "Un accès autorisé à bord de la station ?"
    noam reflexion "Oui."
    elias reflechit "Attends, ça peut être un compte technique. Les consoles de maintenance ont des accès..."
    noam colere "Tu crois que j'ai pas pensé à ça ?!"
    elias colere "JE DEMANDE !"
    "Je le vois se raidir. Je comprends trop tard que je viens de lui sauter dessus sans raison."
    noam fatigue "Désolé."
    elias fatigue "Ouais."
    nyra raison "Une suppression effective est importante. Mais elle ne désigne pas son auteur."
    noam inquiet "Je sais !"
    ryn colere "Alors pourquoi tu nous regardes comme si l'un de nous avait fait le coup ?"
    "Je n'ai pas de réponse."
    iris inquiet "Noam, tu as encore mal à la tête ?"
    noam colere "Arrête avec ça, Iris !"
    iris colere "Je te pose une question !"
    noam desespoir "Je sais plus ce que j'ai vu. Je sais plus si j'ai eu peur pour une vraie raison. Et la seule chose qui aurait pu me répondre a disparu !"
    "Je sens ma gorge se serrer. Les mots sortent de travers."
    elen inquiet "Mais on peut chercher ensemble..."
    noam colere "Et si c'était justement quelqu'un ici qui l'avait effacé ?!"
    "Cette fois, tout s'arrête."
    pause 0.6
    mara stress "Tu nous accuses ?"
    noam peur "Je... Je sais pas."
    ryn colere "C'est trop facile, ça. Tu balances un truc pareil et après tu sais pas ?"
    sael determine "Ryn, recule."
    ryn colere "Je suis assis !"
    sael mefiant "Alors reste-le."
    "Elen regarde Mara, puis moi. Kael fixe obstinément la table."
    julian inquiet "Il faut vérifier. Pas se mettre à désigner des coupables parce que Kami s'est amusée avec toi."
    noam colere "Tu crois que je m'amuse ?!"
    julian colere "NON ! Je crois que quelqu'un devrait t'empêcher de te faire manipuler pendant que tu vas mal !"
    "Je me tais. Julian aussi. Il semble immédiatement regretter le ton qu'il vient d'employer."
    kael calme "Les images de ma chambre sont bloquées pendant sept jours. Celles du couloir sont supprimées. Ce sont deux problèmes différents."
    noam fatigue "Je sais."
    kael triste "Alors arrête de parler comme si tu avais déjà une réponse."
    "Il ne hausse pas la voix. Je baisse les yeux."
    lysa reflechit "Noam, tu as le droit d'avoir peur. Tu n'as pas besoin d'être certain pour le dire."
    lysa inquiet "Mais si tu commences à nous accuser tous, tu vas finir par nous pousser à te répondre comme si on était coupables."
    "Je regarde ses mains. Elles sont posées à plat sur la table."
    noam fatigue "Je voulais juste savoir."
    nyra raison "Alors conservons les faits : le segment a été effacé, l'accès était autorisé selon Kami, et tu ignores ce que montraient ces images."
    noam desaccord "Tu peux arrêter de résumer ma vie en trois points ?!"
    "Nyra ne répond pas. Elle serre légèrement la mâchoire."
    iris desaccord "Elle essaye de t'aider, idiot."
    noam colere "J'ai pas besoin que tout le monde m'aide !"
    "Ma voix se brise. Je déteste le silence qui suit."
    elen fatigue "D'accord..."
    "Elle baisse les yeux sur sa tablette. Je me rappelle qu'elle m'a proposé son pain ce matin."
    "Je voudrais lui dire que je ne parlais pas d'elle. Je n'arrive pas à ouvrir la bouche."
    ryn fatigue "On a encore un vote."
    tomas inquiet "Et rien de tout ça n'a répondu à la question des brouilleurs."
    noam fatigue "Alors votez."
    iris inquiet "Noam..."
    noam desaccord "Je veux juste sortir."
    "Je tourne les talons avant que quelqu'un se lève pour me retenir."
    jump _12_0_1_1_APRES_EXPLOSION


label _12_0_1_1_APRES_EXPLOSION:
    stop music fadeout 1.0
    "Personne ne me suit immédiatement. J'entends une chaise bouger derrière moi, puis la voix d'Elen."
    elen "Il faudrait peut-être..."
    sael "Laisse-le."
    "Je ne sais pas si elle a raison. Je suis seulement soulagé qu'on ne m'arrête pas."
    play sound sfx_door
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_65
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Je marche trop vite. Au bout de quelques mètres, je m'arrête contre le mur pour reprendre mon souffle."
    think "J'ai parlé des images. Au moins, ça, je l'ai fait."
    think "Et j'ai accusé tout le monde de quelque chose que je ne peux pas prouver."
    noam fatigue "Merde..."
    "Je repense à Elias qui m'a aidé avec la ventilation, à Elen et son pain, à Julian qui s'est énervé pour me défendre malgré lui."
    "Ce ne sont pas des preuves. Ce sont des gens."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_66
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ current_period = "Soir"
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0
    "La chambre est exactement comme je l'ai laissée. Le bureau, le lit, la chaise. Il me faut une seconde pour oser refermer la porte."
    noam fatigue "Quel abruti..."
    "Je m'assieds au bord du matelas. Ma tablette affiche l'heure. Le vote a lieu sans moi."
    think "Je ne sais même pas comment ils vont voter. Hier, j'aurais cru que ça m'importait plus que tout."
    "Je laisse la tablette de côté. Un instant, j'imagine retourner là-bas pour m'excuser."
    "Je ne bouge pas."
    "Le silence est interrompu par un léger bruit dans le conduit."
    "Je lève immédiatement les yeux."
    pause 1.0
    "Cette fois, c'est la ventilation. Le souffle augmente, puis redescend."
    noam fatigue "D'accord. Pas ce soir."
    "Je tire la couverture sur moi. Il fait encore assez chaud pour que je la repousse aussitôt."
    think "J'espère qu'Elen ne croit pas que je lui en veux."
    "C'est la dernière pensée claire que j'ai avant de m'endormir."
    scene black with fade
    stop music fadeout 3.0
    call show_chapter_title("Fin du chapitre 4", "Chapitre 4 — Quelque chose ne tourne pas rond") from _call_show_chapter_title_18
    call end_day("13", sleeping=True) from _call_end_day_12_0_1_1
    # L'autre branche J13 n'a pas encore de scénario.
    if getattr(store, "j12011_wire_result", "security") != "security":
        call screen kd_route_vote_convergence
    jump _13_0_1_1_0_REVEIL_CHAMBRE
