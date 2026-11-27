label _12_0_1_1_REVEIL_CHAMBRE:
    $ cafeteria_food_level = "low"
    $ current_period = "Nuit"
    $ current_day = 12
    $ noam_has_juliette_drawing = False
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0
    play sound sfx_creak volume 0.6
    "Un frottement me réveille. Ça vient de la chambre, tout près du lit."
    $ investigation_add("bruits_chambre")
    noam faible "Y a quelqu'un ?"
    "Rien. La ventilation tourne et le couloir reste silencieux."
    think "Soit quelqu'un est entré, soit je viens d'interroger une chaise. Très bon début."
    "Je tends la main vers l'interrupteur sans quitter la pièce des yeux."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "La lumière s'allume. Porte fermée. Chaise près du bureau. Rien ne saute aux yeux."
    "Je teste le verrou deux fois. Il tient."
    think "J'ai entendu ce bruit. Je vais pas encore laisser Kami m'expliquer que j'ai rêvé."
    noam fatigue "Je vérifie tout. Après, seulement, je me recouche."
    $ pnc_room = "chambre_j12"
    $ pnc_flags = {}
    $ room_scene_indices["chambre"] = 1
    call screen pnc_chambre_j12()
    return

    # Durée : 0m45 + exploration


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
    "Le souffle de la grille est régulier. Je reste quand même l'oreille collée au métal."
    noam fatigue "Allez. Fais juste ton boulot."
    "Pas de pas. Pas de frottement. Rien derrière le bruit du ventilateur."
    think "Elias serait fier. Une machine fonctionne et personne n'a besoin de taper dessus."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_sous_lit:
    $ pnc_flags["lit"] = True
    "Je m'accroupis et soulève la couverture."
    noam hesitation "Si quelqu'un est dessous, préviens avant que je fasse une crise cardiaque."
    "Une chaussette, de la poussière, rien d'autre."
    noam fatigue "J'ai mon coupable. Il fait du trente-neuf."
    "Je pose la chaussette sur le lit. Je regarde encore une seconde, juste pour être sûr."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_television:
    $ pnc_flags["television"] = True
    "L'écran mural est froid. Aucun voyant, aucune annonce."
    noam fatigue "Pour une fois, reste éteint."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_placard:
    $ pnc_flags["placard"] = True
    "J'ouvre le placard d'un coup. Les cintres claquent et je sursaute comme un idiot."
    noam colere "Putain..."
    "Un sweat dépasse de l'étagère. À côté, la poussière porte une trace de paume."
    "Je compare avec ma main. Même taille, peut-être. Impossible de me rappeler quand j'ai touché cette étagère."
    think "Encore un truc assez bizarre pour m'empêcher de dormir, pas assez pour prouver quoi que ce soit."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_bureau:
    $ pnc_flags["bureau"] = True
    "La tablette est là. Mon badge aussi, face contre le bureau."
    noam reflexion "Je l'avais remis comme ça ?"
    "Je le retourne, puis je m'arrête."
    think "Parfait. Demain, je ne saurai plus dans quel sens je l'ai laissé."
    noam fatigue "Bravo, Noam."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_salle_de_bain:
    $ pnc_flags["salle_de_bain"] = True
    "La salle de bain est vide. Dans le miroir, j'ai les yeux rouges et la tête de quelqu'un qui ment quand il dit que ça va."
    noam taquin "Très rassurant."
    "Je me passe de l'eau sur le visage. En ressortant, je vérifie quand même derrière la porte."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_brouilleur:
    $ pnc_flags["brouilleur"] = True
    "Le voyant du brouilleur pulse normalement."
    noam reflexion "Sept jours pour revoir une chambre..."
    "Le boîtier n'a pas été forcé. Il protège la chambre de Kami et il protège aussi celui qui entre."
    think "On doit voter là-dessus dans quelques heures. Évidemment."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_tablette:
    $ pnc_flags["tablette"] = True
    "L'historique de la tablette ne montre aucune activité pendant la nuit."
    noam fatigue "Ça aurait été trop simple."
    "J'ouvre la conversation avec Elias, puis je referme avant d'écrire."
    think "Je vais pas le réveiller pour lui demander si ma chambre a respiré."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_photo_juliette:
    $ pnc_flags["photo_juliette"] = True
    "L'emplacement du dessin de Juliette est toujours vide. Je passe un doigt sur le bord du cadre."
    noam faible "Je vais le retrouver."
    think "Cette fois, je la tiens."
    call screen pnc_chambre_j12()
    return


label _12_0_1_1_recoucher:
    if len(pnc_flags) < 3:
        think "Pas encore. Il me faut au moins trois vérifications, sinon je vais recommencer dans cinq minutes."
        call screen pnc_chambre_j12()
        return
    "Je reviens au milieu de la chambre. Rien d'autre ne manque. Je n'ai toujours aucune preuve d'une intrusion."
    noam fatigue "Super enquête. Une chaussette et une trace qui est peut-être la mienne."
    "Je coupe la lumière et me recouche. Avant de fermer les yeux, je vérifie encore le verrou."
    jump _12_0_1_1_CAFETERIA


label _12_0_1_1_CAFETERIA:
    $ current_period = "Matin"
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    "Au bout d'une heure à écouter la ventilation, j'abandonne."
    noam fatigue "Il me faut du café. Beaucoup."
    "Je m'habille et sors sans toucher au reste de la chambre."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_52
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Le couloir est vide et frais. Pour l'instant, personne ne me demande comment je vais."
    call START_EXPLORATION_LIBRE("_12_0_1_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_nav_j12_cafeteria


label _12_0_1_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_53
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play sound sfx_door
    $ showGroup([("noam", "fatigue", 0.50)])
    goumi vide "Bonjour, Noam. Tu arrives avant le service."
    noam fatigue "C'est interdit ?"
    goumi vide "Non. C'est inhabituel."
    noam taquin "Donc je suis suspect ?"
    goumi vide "Je n'ai pas dit cela."
    noam fatigue "Tant mieux. J'ai eu ma dose d'interrogatoires."
    "Derrière le comptoir, Goumi range des assiettes d'un bras et aligne des tranches de pain de l'autre."
    goumi vide "Que souhaites-tu manger ?"
    noam neutre "Du pain, des œufs, ce que tu as."
    goumi vide "Des œufs, oui. Pour le pain, une tranche."
    noam taquin "Une seule ? C'est une punition ?"
    goumi vide "Non. Le stock est anormalement bas."
    noam reflechit "Anormalement ?"
    goumi vide "Les réserves ont diminué plus vite que prévu. J'ai réduit les portions jusqu'à la livraison du jour quatorze."
    $ investigation_add("manque_nourriture")
    noam inquiet "On est toujours douze."
    goumi vide "Je sais compter les représentants. Je ne connais pas la cause de l'écart."
    noam taquin "Tu veux que je mène une enquête sur les tranches de pain ?"
    goumi vide "Je ne possède pas de protocole d'enquête sur les tranches de pain."
    noam fatigue "C'était une blague."
    goumi vide "Souhaites-tu que j'en crée un ?"
    noam surpris "Non !"
    goumi vide "Compris."
    "Je regarde les étagères derrière lui. Deux compartiments sont presque vides."
    think "Un dessin, une photo, des batteries, des vidéos. Maintenant de la nourriture."
    noam neutre "Une tranche, ça ira."
    goumi vide "Très bien. Avec un verre d'eau. Sael m'a demandé d'y veiller."
    noam taquin "Même les robots me surveillent maintenant."
    goumi vide "Je surveille ton plateau. Pas tes pensées."
    noam fatigue "Ça nous change."
    "Je m'assieds avec mon plateau."
    elen joie "GOUUUUMI !"
    "Je sursaute si fort que ma fourchette tape contre l'assiette."
    $ showGroup([("noam", "fatigue", 0.55), ("elen", "rire", 0.25)])
    play music "music/bgm_fallin_love.mp3" fadein 2.0
    elen joie "Noam ?! Mais tu fais quoi debout à cette heure ?"
    noam fatigue "Je mange."
    elen taquin "Je vois ça ! Je veux dire : VOLONTAIREMENT ?"
    noam taquin "Apparemment, je suis devenu une attraction."
    elen rire "Une attraction qui s'est écroulée en plein Conclave, oui !"
    "Son sourire disparaît dès qu'elle entend sa propre phrase."
    elen hesitation "Pardon. C'était nul."
    noam neutre "Un peu."
    elen fatigue "Tu vas mieux ?"
    noam sourire "Je tiens debout. C'est déjà pas mal."
    elen joie "Voilà ! Faut commencer par là ! Goumi, sers-moi le petit-déjeuner de la championne !"
    goumi vide "Une portion standard ?"
    elen content "Deux portions de pain et..."
    goumi vide "Une portion standard."
    elen colere "Attends, tu viens de décider à ma place ?!"
    goumi vide "Je t'informe des quantités disponibles."
    elen desaccord "Mais hier tu m'as déjà servi moins !"
    goumi vide "Les stocks ont encore diminué."
    elen surpris "Encore ?!"
    noam taquin "Tu as mangé pendant ton sommeil, peut-être."
    elen colere "HÉ ! J'ai jamais fait ça ! Enfin..."
    elen hesitation "Une fois. Mais j'étais petite et le gâteau était déjà dans ma chambre, donc ça compte pas."
    noam rire "D'accord. L'enquête est close."
    "Elle se laisse tomber sur la chaise en face de moi, son plateau à peine rempli."
    elen triste "C'est pas drôle, en fait. Si Goumi doit commencer à compter les tranches de pain..."
    noam neutre "On sera livrés le quatorzième."
    elen reflexion "Oui. Je sais. Mais pourquoi il en manque déjà ?"
    "Je hausse les épaules. Elle regarde les étagères, puis ma tranche."
    elen neutre "Tu veux ma portion ?"
    noam surpris "Quoi ?"
    elen determine "T'as été malade. Tu devrais manger davantage."
    noam fatigue "Tu vas pas commencer à me surveiller, toi aussi."
    elen desaccord "Non ! Enfin... juste pendant que tu manges."
    goumi vide "Les recommandations de Sael ne prévoient pas une surveillance permanente."
    elen surpris "Goumi ! T'étais pas obligé de le dire comme ça !"
    noam taquin "Voilà. Même Goumi trouve que tu en fais trop."
    elen taquin "D'accord, d'accord ! Je mange mon pain. Mais si tu tombes dans les pommes, je garde le droit de dire « je te l'avais dit »."
    noam sourire "Marché conclu. Et tu peux arrêter de me regarder mâcher."
    "Elen ramène son assiette contre elle."
    elen taquin "Je t'en garde quand même une si tu changes d'avis."
    noam sourire "Je note."

    "Elle tient trois bouchées avant de reposer sa fourchette."
    elen inquiet "Noam ?"
    noam neutre "Oui ?"
    elen hesitation "Tu es fâché contre nous ?"
    noam inquiet "Pourquoi tu dis ça ?"
    elen fatigue "Parce que tu nous évites. Et quand je te demande comment ça va, tu réponds toujours « ça va »."
    noam fatigue "Je suis juste fatigué."
    elen desaccord "Tu vois ?"
    noam desaccord "Elen, j'ai pas envie d'en parler. Tu peux pas me tirer les mots de la bouche."
    "Elle recule légèrement sur sa chaise."
    elen triste "Je voulais juste t'aider."
    noam inquiet "Je sais. Mais..."
    elen fatigue "D'accord. Je vais pas insister."
    "Elle se remet à couper un morceau d'œuf déjà trop petit."
    noam fatigue "Je suis pas fâché contre toi."
    elen neutre "D'accord."
    noam hesitation "J'arrive juste pas à expliquer ce qui se passe dans ma tête."
    elen neutre "Alors explique pas. On peut juste manger."
    noam sourire "Ouais. Ça, je sais faire."

    elen taquin "Au fait, tu sais ce que j'ai rêvé cette nuit ?"
    noam fatigue "Je vais regretter de demander ?"
    elen rire "Kami était un cupcake géant. Elle nous faisait voter pour choisir qui aurait le droit de la manger."
    noam surpris "Hein ?"
    elen joie "J'ai voté pour tout le monde. Je voulais pas qu'on se dispute."
    noam taquin "Et ça s'est terminé comment ?"
    elen triste "Elle m'a mangée, moi."
    "Elle rit toute seule, puis voit ma tête."
    elen neutre "C'était qu'un rêve."
    noam sourire "Ouais."
    "Je lui parle de la chaussette sous le lit. Elle part immédiatement sur une théorie de recyclage clandestin du linge."
    elen joie "Moi je te dis que la station recycle nos affaires en secret !"
    noam taquin "Un grand complot des chaussettes."
    elen determine "Exactement !"
    "Pendant quelques minutes, on parle d'un truc qui ne peut tuer personne. Ça fait du bien."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_54
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    play sound sfx_announce
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "BONJOUR, mes petits représentants ! Debout, debout. Nous avons une liberté individuelle à disséquer."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous avez bien dormi. Enfin... certains ont préféré fouiller leur chambre au milieu de la nuit. Très discrètement."
    "Je m'arrête net."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote sur les brouilleurs aura lieu aujourd'hui à QUATORZE HEURES précises."
    $ unlock_dossier_chapter(4)
    kami "Ne me forcez pas à venir vous chercher. J'ai douze adultes à surveiller et, bizarrement, aucun ne se comporte comme tel."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous pouvez débattre. Vous pouvez même m'expliquer pourquoi ne pas être observé serait un besoin essentiel. J'adore quand vous rebaptisez vos privilèges."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Si le texte est rejeté, les zones qui utilisent encore ces appareils seront sanctionnées. Pas les appareils. Les zones. Je préfère éviter les malentendus après coup."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Quatorze heures. Soyez à l'heure, soyez beaux et essayez de ne pas vous détester avant le scrutin. Gardez-en un peu pour après."
    hide screen kami_broadcast_ui
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0
    think "Elle m'a regardé fouiller. Et elle voulait que je le sache."
    "La douleur derrière mes yeux revient. Je prends le couloir de l'infirmerie."
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "bg_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_56
    scene bg_infirmerie at adaptive_fullscreen with dissolve
    sael surpris "Noam ?"
    "Je m'arrête devant l'armoire à pharmacie. Sael arrive du fond de la pièce."
    sael mefiant "Tu cherches quelque chose ?"
    noam fatigue "J'ai encore mal à la tête."
    sael inquiet "Tu aurais pu commencer par me le dire."
    noam taquin "Ça aurait été trop simple."
    sael neutre "Assieds-toi."
    "Elle vérifie ma température, puis suit mon regard vers la porte."
    sael reflechit "Tu ne m'écoutes pas."
    noam hesitation "Si."
    sael desaccord "Alors qu'est-ce que je viens de dire ?"
    noam fatigue "Que..."
    sael neutre "Voilà."
    "Elle sort une boîte de médicaments et lit l'étiquette."
    sael determine "Si ça continue, tu prends la dose indiquée. Pas plus. Et tu ne fouilles pas cette armoire tout seul."
    noam neutre "Compris."
    sael inquiet "Tu n'as presque pas dormi, c'est ça ?"
    noam fatigue "Pas beaucoup."
    sael neutre "Alors tu retournes te reposer avant le vote. Si tu tombes encore, je te ramène moi-même dans ta chambre."
    noam taquin "C'est une menace ?"
    sael mefiant "Une promesse."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_57
    scene bg_chambre at adaptive_fullscreen with fade
    "Je m'allonge sans réussir à fermer les yeux. Le vote approche. Quelqu'un sait peut-être ce que j'ai vu et, dans quelques heures, on va décider s'il peut continuer à se cacher."
    "J'ouvre la conversation d'Elen, puis je regarde le cadre vide."
    noam fatigue "Pas maintenant."
    call KD_ROUTE_J12_JULIAN from _call_optional_kd_route_j12_julian
    call OFFER_DAILY_EXPLORATION(
        "_12_0_1_1_ATTENTE_VOTE", 1,
        ["dortoir", "cafeteria", "maintenance", "conclave"],
        _("Rejoindre le vote"), "conclave"
    ) from _call_offer_exploration_j12

    # Durée : 4m10 + rencontre optionnelle et exploration

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
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_12_0_1_1
    "Quand j'arrive, Julian utilise l'écran noir de sa tablette comme miroir. Mara le regarde faire avec un sourire mauvais."
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    julian taquin "Un vote peut être historique. On ne se présente pas devant l'histoire avec un col froissé."
    mara taquin "Ton col est de travers. Depuis ce matin."
    julian surpris "QUOI ?!"
    "Il se retourne vers l'écran mural. Mara éclate de rire."
    lysa blase "T'es cruelle, Mara."
    mara taquin "Je sais. Ça me détend."
    iris fatigue "Génial. On va perdre le vote parce qu'il cherche son bon profil."
    elen rire "Au moins, pendant ce temps-là, on parle pas du vote !"
    "Personne ne rit. Elen se tasse dans son siège."
    ryn colere "Moi, j'ai très envie qu'on en parle, du vote."
    tomas inquiet "On a encore quelques minutes. Ce n'est peut-être pas la peine de..."
    ryn colere "De quoi ? De se préparer ?"
    tomas hesitation "De commencer en s'engueulant."
    ryn colere "Bonne chance."
    "Elias fixe un gobelet vide. Kael garde les deux mains autour de sa tablette."
    noam neutre "Salut."
    elias fatigue "Tiens. T'es encore debout."
    noam taquin "Je vois que tout le monde est très original aujourd'hui."
    elias sourire "J'ai décidé de suivre la mode."
    iris inquiet "Noam, tu tiens le coup ?"
    noam fatigue "Sael m'a posé quatre questions et j'en ai raté une. Apparemment, je vis encore."
    sael neutre "J'ai posé quatre questions."
    noam taquin "Et elles étaient toutes difficiles."
    sael mefiant "Tu as dormi combien d'heures ?"
    noam fatigue "Ça fait une cinquième."
    "Sael me lance un regard qui promet une sixième question. Ryn repousse son siège."
    ryn colere "Bon. Qui compte voter contre ? Qu'on perde pas une heure à faire semblant."
    nyra raison "Non, Ryn. On ne va pas demander à chacun de déclarer son vote devant les autres. Tu connais la règle."
    ryn colere "Je pose une question, pas un bulletin."
    sael determine "Tu veux surtout mettre la pression avant qu'ils parlent."
    ryn colere "Je veux pas découvrir après coup qu'un de nous nous a plantés."
    "Je relève la tête."
    mara stress "Tu peux choisir un autre mot que 'plantés' ? Juste aujourd'hui ?"
    ryn colere "J'ai pas dit que j'allais le faire !"
    lysa blase "C'est précisément pour ça que tu devrais choisir un autre verbe."
    "Deux personnes rient. Ça s'arrête tout de suite."
    play sound sfx_announce
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "VOILÀÀÀ ! Douze représentants, douze avis et déjà plusieurs menaces avant l'ouverture. Vous êtes efficaces aujourd'hui."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous devez décider si les dispositifs de brouillage peuvent être possédés, fabriqués et utilisés librement, dans les limites des autres Commandements."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Il faut l'unanimité. Un seul vote contraire, une seule petite main qui tremble, et les interdictions restent en place."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je vous laisse débattre. Dites tout ce que vous n'oserez plus vous dire après le résultat."
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
    mara stress "Moi, c'est oui. J'en ai marre de baisser la voix jusque dans ma salle de bain."
    julian taquin "La liberté de tes conversations avec toi-même mérite effectivement notre mobilisation."
    mara taquin "Tu veux que je te raconte ce que j'y fais ?"
    julian surpris "Non merci !"
    elen inquiet "Je veux pouvoir parler dans ma chambre sans me demander si Kami garde chaque mot. C'est tout."
    $ unlock_dossier_arg("p4_intimite")
    iris reflechit "Ce qui m'intéresse, c'est ce qu'elle détecte encore quand un brouilleur tourne. Le signal ? La consommation ? Une anomalie dans son propre réseau ?"
    ryn colere "C'est pas un examen sur Kami, Iris."
    iris colere "Non, c'est exactement le problème ! Si elle voit encore le brouilleur, on doit savoir ce qu'il cache vraiment."
    kael triste "Il cache assez pour qu'on ne voie pas qui est entré dans ma chambre."
    "Elias pose son gobelet vide."
    elias reflechit "Ouais. Si quelqu'un entre pendant que ça tourne, on fait quoi ? On attend sept jours ?"
    nyra raison "Elias, je comprends que tu veuilles qu'on puisse identifier quelqu'un qui entre dans une chambre. Mais on peut chercher une solution sans donner à Kami accès à tout ce qu'on fait chez nous."
    $ unlock_dossier_arg("p4_preuves")
    ryn colere "Et tu proposes quoi ? Qu'on laisse Kami fouiller nos chambres dès qu'il manque une chaussette ?"
    kael colere "Il ne manque pas une chaussette. On m'a pris la photo de ma sœur."
    $ unlock_dossier_arg("p4_voleur")
    sael mefiant "Ryn, arrête. Personne n'a dit que ce vol n'était pas grave."
    tomas raison "Même si le texte passe, le délai d'accès reste de sept jours. Les images sont bloquées, pas détruites. Enfin... normalement."
    $ unlock_dossier_arg("p4_delai")
    julian taquin "Sept jours ? Mon prochain discours aura déjà été remplacé par deux autres."
    lysa blase "On peut commencer dès maintenant."
    noam reflexion "Et les couloirs ? Les brouilleurs bloquent aussi les images dehors ?"
    iris inquiet "Noam, pourquoi tu demandes ça ?"
    noam fatigue "Pour rien. Laissez tomber."
    lysa blase "Soit tu poses ta question, soit tu arrêtes de nous demander de la deviner."
    noam inquiet "J'ai dit laissez tomber."
    "Elle ne répond pas. Son regard reste posé sur moi un instant de trop."
    ryn colere "J'en ai marre de demander la permission pour fermer ma propre porte !"
    sael neutre "Moi aussi. Ça n'efface pas ce qui est arrivé à Kael."
    noam inquiet "Et si quelqu'un se sert déjà de ces appareils pour entrer dans nos chambres ?"
    mara stress "Noam..."
    noam colere "On en parle depuis des jours et on n'a toujours rien trouvé ! Pas une trace !"
    nyra raison "Noam, rien ne nous permet encore de dire que les brouilleurs ont servi à ça. J'aimerais qu'on ne parte pas de cette hypothèse pour décider du vote."
    "Nyra parle sans hausser le ton. Je l'entends quand même comme un reproche."


    call play_stat_dialogue("j12") from _call_play_stat_dialogue_11
    iris reflechit "Kael a déjà demandé les archives. On sait pourquoi elles sont bloquées."
    kael fatigue "Je sais surtout qu'on me demande d'attendre."
    noam reflexion "Et les couloirs, eux..."
    "Je m'interromps. Lysa me regarde."
    lysa reflechit "Quoi, les couloirs ?"
    noam fatigue "Rien. Continuez."
    lysa blase "Ouais. Encore rien."
    ryn colere "Je vote pour. Je vais pas demander à une caméra la permission d'aller pisser."
    mara taquin "Ça te ferait pas de mal de demander la permission avant certaines choses."
    ryn colere "QUOI, ENCORE ?!"
    call kd_vn_reaction("ryn", "colere", "#ff9c55")
    sael determine "On peut vouloir garder les brouilleurs et admettre qu'ils ont peut-être servi à quelqu'un. Les deux sont vrais."
    elias reflechit "Voilà. C'est ça que j'essayais de dire."
    iris taquin "En beaucoup moins clair."
    elias fatigue "Je sais."
    "Les voix se recouvrent. Chacun défend sa chambre, sa peur, son vol. Personne ne parle de la même chose."
    noam inquiet "Et si quelqu'un se sert des brouilleurs pour nous faire du mal ?"
    "La question m'échappe plus sèchement que je ne le voudrais."
    julian inquiet "Alors on cherche qui. On ne rend pas nos chambres à Kami parce que l'un de nous pourrait mal agir."
    noam reflechit "Et si c'est déjà arrivé ?"
    iris inquiet "Noam..."
    kael triste "Quelqu'un est déjà entré. Ma photo a disparu."
    mara stress "Et le dessin de Juliette aussi."
    lysa reflechit "Personne n'a encore prouvé que les brouilleurs avaient servi à ces vols."
    "Elle dit ça en me regardant. Je détourne les yeux."
    nyra raison "On va continuer à chercher vos affaires, tous les deux. Mais je refuse qu'on décide que les brouilleurs sont responsables simplement parce qu'on n'a rien trouvé d'autre."
    "Elle a raison. C'est précisément ce qui m'énerve."
    jump _12_0_1_1_DEBAT_VOTE

    # Durée : 3m40 + choix statistique


label _12_0_1_1_DEBAT_VOTE:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    "Kami lance une simulation censée nous forcer à choisir. À chaque manche, protéger quelqu'un revient à retirer quelque chose à tous les autres."
    call j12_play_trolley_problem from _call_j12_play_trolley_problem
    $ j12011_vote_data = _return
    scene bg_conclave at adaptive_fullscreen with fade
    "Quand l'interface disparaît, les discussions reprennent avant même que j'aie lâché la commande."
    think "Cinq choix. Cinq façons de finir avec une raison de s'en vouloir."
    jump _12_0_1_1_DEBAT_TRAITRE

    # Durée : 0m35 + mini-jeu


label _12_0_1_1_DEBAT_SECURITE:
    # Compatibilité des anciennes sauvegardes : les débats alternatifs
    # rejoignent désormais la confrontation commune.
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5
    $ showGroup([
        ("noam", "fatigue", 0.18), ("kael", "calme", 0.42),
        ("mara", "stress", 0.66), ("nyra", "raison", 0.88),
    ])
    noam inquiet "Si on dit oui, les caméras serviront encore à quelque chose ?"
    kael triste "Pas pour ma chambre. Pas tout de suite."
    mara stress "Et si on dit non, ça veut dire que Kami pourra nous écouter quand elle veut."
    noam desaccord "Je sais ! C'est ça qui m'énerve."
    nyra raison "Je ne peux pas te promettre que tu retrouveras ton dessin si on vote contre. Et si on vote pour, je ne peux pas non plus te promettre que personne ne recommencera."
    noam fatigue "Super. On est bien avancés."
    "Mara ouvre la bouche, regarde Kael et renonce à sa plaisanterie."


    jump _12_0_1_1_DEBAT_TRAITRE

    # Durée : 0m35


label _12_0_1_1_DEBAT_LIBERTE:
    # Compatibilité des anciennes sauvegardes : conserver ce label.
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5
    $ showGroup([
        ("noam", "fatigue", 0.18), ("ryn", "colere", 0.42),
        ("sael", "mefiant", 0.66), ("lysa", "inquiet", 0.88),
    ])
    ryn colere "J'ai pas signé pour que Kami me regarde dormir !"
    sael mefiant "Et les personnes à qui l'on a volé quelque chose, elles ont signé pour qu'on ne cherche jamais ?"
    ryn colere "J'ai pas dit ça."
    noam reflexion "Moi non plus, je sais plus où mettre la limite."
    lysa blase "Ça nous change des gens qui savent tout."
    "Ryn lui lance un regard noir. Elle ne baisse pas les yeux."


    jump _12_0_1_1_DEBAT_TRAITRE

    # Durée : 0m30


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
    mara stress "Bon. On a retourné le problème dans tous les sens. On vote ?"
    tomas inquiet "Il reste deux précisions sur le texte. Peut-être trois."
    ryn colere "Sérieusement, Tomas ?!"
    tomas raison "Oui. Le texte ne dit pas clairement ce qu'on fait des dispositifs déjà installés."
    elias fatigue "Oh, non. On va refaire l'épisode des campements."
    elen inquiet "Ne dis pas ça..."
    julian taquin "Je propose un amendement interdisant l'expression « déclaration préalable »."
    iris desaccord "Julian, ferme-la une seconde."
    "Tout le monde repart en même temps. Elen se mord la lèvre. Elias s'enfonce dans son fauteuil. Kael serre sa tablette contre la table."
    think "Hier, ils étaient dans ma chambre. Aujourd'hui, je cherche lequel d'entre eux pourrait effacer une caméra."
    "Je croise le regard de Lysa. Elle a déjà compris que je n'écoute plus."
    lysa inquiet "Noam ?"
    noam fatigue "..."
    mara agace "De toute façon, on peut y passer trois jours, ça changera rien au..."
    noam colere "ARRÊTEZ !"
    with vpunch
    play sound sfx_metal_clank
    "Ma chaise heurte le sol derrière moi."
    elen inquiet "Noam ?"
    noam colere "Vous pouvez vous taire trente secondes ?!"
    ryn colere "C'est littéralement le sujet du vote !"
    noam colere "JE SAIS !"
    iris inquiet "Noam, assieds-toi."
    noam inquiet "Non. J'ai besoin de vous dire un truc."
    sael mefiant "Alors parle. Mais arrête de crier sur tout le monde."
    noam reflexion "Hier, j'ai consulté les caméras du couloir près de l'infirmerie. Le moment où j'ai cru voir quelqu'un."
    julian hesitation "Et ?"
    noam inquiet "Ils ont été supprimés."
    "Ryn inspire pour répondre. Tomas parle avant lui."
    tomas surpris "Supprimés ? Pas simplement indisponibles à cause du brouillage ?"
    noam colere "SUPPRIMÉS. Le terminal l'a affiché."
    kael inquiet "Tu es sûr de l'heure ?"
    noam desaccord "J'ai vérifié !"
    lysa reflechit "Et Kami t'a dit quoi ?"
    noam inquiet "Que ça venait d'un accès autorisé. Pas d'elle."
    "Nyra cesse enfin de prendre des notes."
    mara stress "Un accès autorisé à bord de la station ?"
    noam reflexion "Oui."
    elias reflechit "Attends. Un accès autorisé, ça peut être une console de maintenance. Y en a plusieurs qui..."
    noam colere "Tu crois que j'ai pas pensé à ça ?!"
    elias colere "JE DEMANDE !"
    "Il se raidit. Je viens de lui tomber dessus alors qu'il essaie seulement de comprendre."
    noam fatigue "Désolé."
    elias fatigue "Ouais."
    nyra raison "Attends. Un segment a réellement été supprimé, ça mérite qu'on s'en occupe. Mais on n'a toujours pas le nom de la personne qui l'a fait."
    noam inquiet "Je sais !"
    ryn colere "Alors pourquoi tu nous regardes comme si l'un de nous avait fait le coup ?"
    "Je regarde la table. Je n'ai pas de réponse qui ne les accuse pas."
    iris inquiet "Noam, tu as encore mal à la tête ?"
    noam colere "Arrête avec ça, Iris !"
    iris colere "Je te pose une question !"
    noam desespoir "Je sais même plus ce que j'ai vu ! Peut-être que y avait rien, peut-être que quelqu'un était vraiment là... et le seul truc qui pouvait me répondre a disparu !"
    elen inquiet "Mais on peut chercher ensemble..."
    call cutin("noam") from _call_kd_cutin_12_noam
    noam colere "Et si c'était justement quelqu'un ici qui l'avait effacé ?!"
    "Cette fois, personne ne répond."
    pause 0.6
    call reactions([("mara", "stress"), ("ryn", "colere"), ("julian", "inquiet")]) from _call_kd_reactions_12_accusation
    mara stress "Tu crois que c'est l'un de nous ?"
    noam peur "J'en sais rien. C'est ça le problème."
    ryn colere "C'est trop facile, ça. Tu balances un truc pareil et après tu sais pas ?"
    sael determine "Ryn, recule."
    ryn colere "Je suis assis !"
    sael mefiant "Alors reste-le."
    "Elen regarde autour de la table comme si quelqu'un allait lever la main."
    julian inquiet "Il faut vérifier les accès. Mais on ne va pas choisir un coupable parce que Kami t'a poussé jusque-là."
    noam colere "Tu crois que je m'amuse ?!"
    julian colere "NON ! Je crois que tu vas mal et qu'elle s'en sert ! Et là, tu lui facilites le travail !"
    "Julian se tait. Toute sa belle assurance a disparu."
    kael calme "Les images de ma chambre sont bloquées sept jours. Celles du couloir ont été supprimées. Ce sont deux choses différentes."
    noam fatigue "Je sais."
    kael colere "Alors arrête de tout mélanger. Moi aussi, je veux une réponse."
    $ close_up("lysa")
    lysa reflechit "Noam. Tu peux dire que t'as peur. T'as même de bonnes raisons."
    lysa inquiet "Mais si tu nous regardes tous comme des coupables, on va finir par te répondre comme si on l'était."
    noam fatigue "Je voulais juste savoir."
    nyra raison "Noam, donne-moi ce qu'on a de concret. Un segment effacé, un accès que Kami dit autorisé, aucun nom. Si tu veux qu'on retrouve quelqu'un, il faut partir de là."
    noam desaccord "Arrête avec tes listes, Nyra ! C'est de moi qu'on parle, là !"
    "Nyra serre la mâchoire, puis se tait."
    iris desaccord "Noam, ça suffit. Elle essaie de t'aider."
    noam colere "J'ai pas besoin que tout le monde m'aide !"
    "Ma voix se casse sur le dernier mot."
    elen fatigue "D'accord..."
    "Elen baisse les yeux. Ce matin, elle m'a proposé la moitié de son petit-déjeuner."
    ryn fatigue "On a encore un vote."
    tomas inquiet "Et... on doit toujours prendre une décision sur les brouilleurs."
    noam fatigue "Alors votez."
    iris inquiet "Noam..."
    noam desaccord "Je veux juste sortir."
    "Je pars avant que quelqu'un puisse répondre."
    jump _12_0_1_1_APRES_EXPLOSION

    # Durée : 3m25


label _12_0_1_1_APRES_EXPLOSION:
    stop music fadeout 1.0
    "Une chaise bouge derrière moi."
    elen inquiet "Je devrais peut-être..."
    sael neutre "Laisse-le respirer."
    "Je ne sais pas si elle a raison. Je suis juste soulagé que personne ne me rattrape."
    play sound sfx_door
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_65
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Je marche trop vite et dois m'appuyer contre le mur au premier croisement."
    think "J'ai parlé des images. Au moins, ça, je l'ai fait."
    think "Et j'ai accusé tout le monde de quelque chose que je ne peux pas prouver."
    noam fatigue "Merde..."
    "Elias m'a aidé avec la ventilation. Elen voulait partager son pain. Julian vient de m'engueuler parce qu'il pense que Kami me manipule."
    think "Et moi, je les ai tous mis dans la même case."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_66
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ current_period = "Soir"
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0
    "La chambre est comme je l'ai laissée. Je reste une seconde dans l'entrée avant de refermer."
    noam fatigue "Quel abruti..."
    "Je m'assieds au bord du lit. Sur la tablette, l'heure du vote passe sans moi."
    think "Ils vont décider. Je ne sais même pas si j'ai encore le droit de leur en vouloir."
    "J'ouvre la messagerie. Le nom d'Elen est en haut. Je n'écris rien."
    "Je ne bouge pas."
    "Un frottement vient du conduit. Je lève les yeux d'un coup."
    pause 1.0
    "Le ventilateur accélère, puis reprend son rythme. Cette fois, je reconnais le bruit."
    noam fatigue "D'accord. Pas ce soir."
    "Je m'allonge sans retirer mes vêtements."
    think "Demain, je lui parle. Pour de vrai."
    "Je m'endors avant de pouvoir décider par quoi commencer."
    scene black with fade
    stop music fadeout 3.0
    call show_chapter_title("Fin du chapitre 4", "Chapitre 4 — Quelque chose ne tourne pas rond") from _call_show_chapter_title_18
    call end_day("13", sleeping=True) from _call_end_day_12_0_1_1
    # L'autre branche J13 n'a pas encore de scénario.
    if getattr(store, "j12011_wire_result", "security") != "security":
        call screen kd_route_vote_convergence
    jump _13_0_1_1_0_REVEIL_CHAMBRE

    # Durée : 1m35
    # Total estimé : 14m40 + exploration, choix statistique et mini-jeu
