# JOUR 26 — LA CHAMBRE CLOSE (route Tomas, vote rejeté).
# Point de vue strict de Noam ; cause du décès et meurtrier non révélés.
default j26_alt_corps = False
default j26_alt_flacon = False
default j26_alt_vent = False
default j26_alt_verrou = False
default j26_alt_bazar = False
default j26_alt_elen = False
default j26_alt_julian = False
default j26_alt_kael = False
default j26_alt_ryn = False
default j26_alt_nyra = False
default j26_alt_boycott = False

label _26_0_1_1_0_1_REVEIL:
    $ current_day = 26
    $ day_id = 26
    $ current_period = "Matin"
    $ j26_alt_corps = False
    $ j26_alt_flacon = False
    $ j26_alt_vent = False
    $ j26_alt_verrou = False
    $ j26_alt_bazar = False
    $ j26_alt_elen = False
    $ j26_alt_julian = False
    $ j26_alt_kael = False
    $ j26_alt_ryn = False
    $ j26_alt_nyra = False
    $ j26_alt_boycott = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Ma tablette s'allume sur un message de Tomas, envoyé hier soir. « Merci pour tout à l'heure. On se voit demain. »"
    "J'ai lu le message sans répondre. Je le relis comme si ça pouvait me donner une idée de ce qu'il avait derrière la tête."
    think "Il devait être sacrément épuisé pour s'excuser de nous avoir demandé de l'aide."
    "Je commence à écrire « On mange ensemble ? » puis j'efface. Il dort sûrement enfin."
    noam fatigue "Je lui garde une place."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j26_alt_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _26_0_1_1_0_1_CAFETERIA
# Durée : 45 s — Total : 45 s.

label _26_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j26_alt_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    $ showGroup([("julian", "neutre", 0.080), ("iris", "fatigue", 0.220), ("mara", "taquin", 0.360), ("elen", "fatigue", 0.500), ("lysa", "blase", 0.640), ("noam", "neutre", 0.780), ("nyra", "neutre", 0.920)])
    "Julian tapote la table avec sa cuillère. Mara a déjà piqué une tartine dans l'assiette d'Iris."
    julian reflexion "Vous avez lu le texte de demain ?"
    mara taquin "Tu veux nous le réciter avant qu'on ait le droit de mâcher ?"
    iris blase "Julian, il est trop tôt pour ça."
    julian agace "Je pose juste une question !"
    "Je tire la chaise vide à côté de moi."
    noam neutre "Tomas est pas descendu ?"
    lysa blase "Il se cache sous la table pour éviter Julian."
    julian fatigue "Vous avez fini ?"
    elen sourire "Il doit dormir. Hier il était tellement crevé..."
    noam reflexion "Tu l'as croisé après le dîner ?"
    elen inquiet "Oui. Il arrêtait pas de regarder derrière lui. Il m'a demandé s'il pouvait prendre ma chambre."
    mara taquin "Oh. Vous avez dormi ensemble ?"
    elen colere "Non ! On a échangé nos chambres !"
    mara rire "Ah, tout de suite, c'est moins intéressant."
    elen fatigue "Il avait peur de retourner chez lui. Quelqu'un tambourinait encore à sa porte, hier soir."
    noam surpris "Quelqu'un ? Tu l'as vu ?"
    elen reflexion "Non. J'ai entendu les coups en passant. Je me suis pas arrêtée."
    julian fatigue "On va pas reparler de cette histoire toute la matinée."
    noam raison "Pourquoi pas ?"
    julian agace "Parce que ça lui a déjà gâché sa soirée !"
    "Il repose sa cuillère avec un bruit sec. Personne ne répond."
    lysa inquiet "En tout cas, manquer le petit-déjeuner, c'est pas son genre."
    elen fatigue "Il voulait juste dormir. Je lui ai dit de mettre son réveil."
    nyra neutre "Alors n'allez pas lui tomber dessus à six."
    noam neutre "Elen, on va frapper. S'il dort, on le laisse tranquille."
    elen content "Ouais. Viens."
    lysa neutre "Je viens aussi. Il me doit un café."
    iris blase "Dites-lui que le sien refroidit."
    $ hideGroup()
    jump _26_0_1_1_0_1_PORTE
# Durée : 2m00 — Total : 2m45.

label _26_0_1_1_0_1_PORTE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("elen", "inquiet", 0.25), ("lysa", "neutre", 0.49), ("noam", "neutre", 0.73)])
    "Elen s'arrête devant sa porte. Elle frappe deux petits coups, puis attend en souriant encore."
    elen neutre "Tomas ? Allez, debout. C'est moi."
    pause 0.5
    lysa reflexion "Il a peut-être mis quelque chose sur ses oreilles."
    elen inquiet "Tomas ? Tu m'entends ?"
    play sound "audio/sfx_knock.mp3"
    "Elle essaie la poignée. Son sourire disparaît."
    elen surpris "Ah. Il a fermé."
    noam neutre "T'as ta tablette ?"
    elen inquiet "Ça changera rien, il a mis le verrou. Il m'a dit qu'il ferait ça pour pas qu'on l'emmerde."
    noam inquiet "Tomas ! C'est Noam ! Ouvre deux secondes !"
    pause 0.7
    "Je colle l'oreille contre la porte. Rien. Même pas un mouvement."
    lysa inquiet "Bon. Là, j'aime pas du tout."
    elen inquiet "Il doit dormir. Il a juste... il dort vraiment profondément, des fois."
    noam raison "Elen, recule. Je vais chercher Elias. Et Sael."
    elen inquiet "Pourquoi Sael ?"
    noam fatigue "Parce que si Tomas va mal, elle saura quoi faire."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE
# Durée : 1m30 — Total : 4m15.

label _26_0_1_1_0_1_DECOUVERTE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "Elias arrive avec Kael et sa boîte à outils. Sael les suit d'un pas pressé. Elle comprend à nos têtes que quelque chose ne va pas."
    $ showGroup([("kael", "reflexion", 0.070), ("elias", "fatigue", 0.242), ("elen", "inquiet", 0.414), ("sael", "inquiet", 0.586), ("noam", "inquiet", 0.758), ("lysa", "inquiet", 0.930)])
    kael reflexion "Il a mis le verrou intérieur ?"
    elen inquiet "Oui. Enfin, c'est ce qu'il m'a dit hier. Vous pouvez ouvrir ?"
    elias raison "Faut passer par le boîtier. Je vais essayer."
    elen peur "Mais dépêche-toi !"
    elias inquiet "Je fais ce que je peux, Elen."
    sael raison "Elias, laisse-moi le passage quand tu ouvriras."
    elias surpris "OK, OK."
    "Elias s'accroupit. Il cherche une prise avec son outil, jure entre ses dents et recommence."
    elen inquiet "Ça fait super longtemps."
    elias agace "Ça fait vingt secondes ! Arrête de me parler, j'essaie de pas tout arracher !"
    "J'aurais presque envie de lui dire de se calmer, mais je regarde toujours la porte. Tomas n'a pas répondu une seule fois, même avec tout ce bruit."
    play sound "audio/sfx_knock.mp3"
    noam inquiet "Tomas ! Hé ! Réponds, même si tu veux qu'on se casse !"
    "Rien. Elias serre les dents, tire sur le mécanisme et recule d'un coup."
    elias neutre "C'est ouvert. Bougez pas."
    "Le verrou cède avec un claquement. Il pousse la porte."
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflexion", 0.070), ("elias", "fatigue", 0.242), ("elen", "inquiet", 0.414), ("sael", "inquiet", 0.586), ("noam", "inquiet", 0.758), ("lysa", "inquiet", 0.930)])
    "L'air est lourd. Il y a une odeur aigre, des barquettes ouvertes au pied du lit et des vêtements partout. Je commence à chercher Tomas du regard, puis j'arrête de regarder le reste."
    noam fatigue "Oh, merde..."
    elen fatigue "J'avais laissé des trucs partout, je..."
    "Il est allongé sur le dos, habillé comme hier, la main pendant au bord du matelas."
    stop music fadeout 0.6
    pause 0.7
    noam inquiet "Tomas ?"
    "Je lui touche l'épaule. Son t-shirt est trempé et ses cheveux collent à son front."
    noam peur "Hé... c'est pas drôle. Tomas ?"
    elen peur "Pourquoi il a pas enlevé sa veste ? Tomas, t'as trop chaud ?"
    noam panique "Réveille-toi !"
    sael raison "Noam. Écarte-toi."
    "Sael s'agenouille près de Tomas. Elle cherche son pouls, puis vérifie sa respiration. Je me retrouve derrière elle sans me souvenir d'avoir bougé."
    elen inquiet "Sael ?"
    sael raison "Une seconde."
    pause 0.5
    "Sael vérifie une seconde fois. Elle a cessé de nous regarder."
    elen peur "Dis quelque chose !"
    sael inquiet "Je ne trouve pas de pouls..."
    noam surpris "Quoi ?"
    sael raison "Noam, recule. S'il te plaît."
    "Sael vérifie encore. J'entends Elen demander quelque chose, mais je n'arrive pas à suivre."
    "Un carillon retentit dans les haut-parleurs. Sael relève la tête, les doigts encore sur le cou de Tomas."
    play sound sfx_announce
    $ hideGroup()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    kami "Ding, dong, ding, dong ! Une annonce exceptionnelle pour tous mes chers représentants !"
    kami "Un corps a été découvert dans la chambre d'Elen ! Oui, un vrai corps !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Tous les représentants sont invités à se rendre immédiatement sur les lieux de la découverte !"
    kami "Hiiii ! J'ai toujours voulu faire ça !"
    hide screen kami_broadcast_ui
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflexion", 0.07), ("elias", "fatigue", 0.242), ("elen", "peur", 0.414), ("sael", "triste", 0.586), ("noam", "vide", 0.758), ("lysa", "inquiet", 0.93)])
    elen peur "Un corps ? Elle parle de Tomas ?"
    "Des pas résonnent dans le couloir. Nyra apparaît sur le seuil presque aussitôt."
    $ showGroup([("kael", "reflexion", 0.06), ("elias", "fatigue", 0.207), ("elen", "peur", 0.353), ("sael", "triste", 0.500), ("noam", "vide", 0.647), ("lysa", "inquiet", 0.793), ("nyra", "inquiet", 0.94)])
    nyra inquiet "Qu'est-ce qui s'est passé ?"
    "Elle ouvre la porte en grand et la cale pour qu'elle ne puisse plus se refermer."
    nyra raison "Il faut aérer. Cette odeur est irrespirable."
    sael fatigue "Merci, Nyra. Elle commence à me monter à la tête."
    noam inquiet "Sael... ?"
    "Sael retire lentement ses mains. Elle regarde Elen."
    sael triste "Elen... Tomas est mort."
    pause 1.0
    elen peur "Non. Attends. Tu peux pas savoir aussi vite."
    noam vide "..."
    elen colere "Mais essayez encore ! Vous avez essayé quoi, là ?!"
    sael inquiet "On a vérifié, Elen. Je suis désolée."
    "Elen avance vers le lit comme pour refaire elle-même ce que Sael vient de faire, mais Lysa la rattrape avant qu'elle trébuche."
    elen triste "Il a même pas défait le lit..."
    elen peur "Je lui avais dit qu'il pouvait prendre des affaires dans l'armoire s'il voulait."
    "Elle regarde Tomas, puis sa propre main, qui tient encore la carte d'accès de sa chambre."
    pause 0.6
    lysa inquiet "Viens, Elen. Viens dans le couloir."
    elen peur "Mais il va être tout seul."
    lysa triste "Sael est avec lui. Allez, viens."
    "Elen finit par se laisser entraîner dans le couloir. Je reste devant le lit. Je pourrais compter les secondes qui passent, mais je sais plus depuis combien de temps je suis là."
    "Une main se pose sur mon épaule. C'est Sael."
    $ showGroup([("sael", "fatigue", 0.31), ("noam", "vide", 0.66)])
    sael fatigue "Noam. Tu peux sortir ? J'ai besoin d'un peu de place."
    noam fatigue "Je lui ai parlé hier."
    sael triste "Je sais."
    noam inquiet "Il cherchait encore ce truc sur Keyper. Il m'en parlait, il..."
    sael triste "Je sais, Noam. Écoute... va t'asseoir un peu. Je viens te voir après."
    "Je sors. Nyra est toujours près de la porte, qu'elle maintient grande ouverte."
    $ showGroup([("nyra", "inquiet", 0.30), ("noam", "fatigue", 0.69)])
    nyra inquiet "Sael n'a pas encore trouvé ce qui lui est arrivé ?"
    noam fatigue "Non."
    "Nyra jette un regard vers l'intérieur de la pièce. Elle ne lâche pas la porte."
    nyra reflexion "Je vais la laisser ouverte encore un moment. L'air doit circuler."
    noam neutre "Sael a demandé qu'on ne touche à rien."
    nyra raison "Je sais. Je ne rentre pas."
    $ hideGroup()
    jump _26_0_1_1_0_1_APRES_CHOC

label _26_0_1_1_0_1_APRES_CHOC:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "Lysa a installé Elen sur une banquette. Elias est resté près de la porte, les yeux fixés sur son outil."
    $ showGroup([("elen", "triste", 0.20), ("lysa", "inquiet", 0.44), ("noam", "fatigue", 0.69)])
    elen triste "J'ai laissé toutes mes affaires là-dedans. Même mes vieilles chaussettes..."
    lysa inquiet "Elen..."
    elen colere "Non, mais il a dû voir le bordel ! Je lui ai dit de pas faire attention, et maintenant il est..."
    noam fatigue "Tu veux de l'eau ?"
    elen triste "Non. Arrêtez de me demander si je veux quelque chose."
    "Lysa écarte discrètement le gobelet qu'elle avait pris pour elle. Je m'assois à côté d'Elen sans trouver quoi dire."
    pause 0.3
    elen fatigue "Ils vont le mettre où ?"
    noam neutre "À l'infirmerie, je pense."
    elen triste "Et ses affaires ? Ses trucs, dans sa chambre... On va y toucher ?"
    lysa raison "Pas maintenant. On verra plus tard, d'accord ?"
    "Elen acquiesce, puis secoue la tête comme si elle venait d'accepter quelque chose sans l'avoir entendu."
    "J'entends plusieurs personnes arriver en courant. Julian manque de percuter Kael au tournant du couloir."
    $ showGroup([("elen", "triste", 0.070), ("lysa", "inquiet", 0.213), ("noam", "fatigue", 0.357), ("julian", "inquiet", 0.500), ("mara", "agace", 0.643), ("kael", "inquiet", 0.787), ("elias", "fatigue", 0.930)])
    julian inquiet "Noam ! C'est quoi cette histoire ? On m'a dit que Tomas..."
    noam fatigue "C'est vrai."
    julian surpris "Non. Attends. Tu l'as vu ?"
    mara agace "Julian, on vient de te dire oui."
    julian colere "Je te parle pas, Mara !"
    mara colere "Moi non plus j'ai pas envie de te parler, crois-moi !"
    "Ryn arrive derrière eux. Il a dû courir ; il respire encore fort."
    $ showGroup([("elen", "triste", 0.070), ("lysa", "inquiet", 0.193), ("noam", "fatigue", 0.316), ("julian", "inquiet", 0.439), ("mara", "agace", 0.561), ("kael", "inquiet", 0.684), ("elias", "fatigue", 0.807), ("ryn", "inquiet", 0.930)])
    ryn inquiet "Il s'est passé quoi ? Il est tombé ?"
    kael raison "On sait juste qu'on a trouvé la porte verrouillée."
    ryn inquiet "Et personne a entendu un bruit ? Même pas Elen ?"
    kael inquiet "Elle a dormi dans sa chambre à lui. On l'a déjà dit."
    ryn agace "Arrêtez de me répondre comme si j'étais con !"
    noam colere "Alors arrête de gueuler sur tout le monde ! Sael essaie de bosser !"
    "Ryn ouvre la bouche, prêt à me répondre. Il regarde mes mains, qui tremblent tellement que j'ai dû les serrer dans mes poches, et se tait."
    $ showGroup([("elen", "peur", 0.070), ("lysa", "inquiet", 0.177), ("noam", "fatigue", 0.285), ("julian", "inquiet", 0.393), ("mara", "agace", 0.500), ("kael", "inquiet", 0.607), ("elias", "fatigue", 0.715), ("ryn", "inquiet", 0.823), ("nyra", "inquiet", 0.930)])
    elen peur "Mais attendez... c'est ma chambre."
    nyra inquiet "Oui ?"
    elen colere "C'était moi qui devais être là. Vous comprenez pas ? S'il y a quelqu'un qui..."
    nyra fatigue "On sait pas si quelqu'un est entré."
    elen colere "Alors arrête de parler comme si tu savais tout !"
    "Nyra baisse les yeux. Je m'attends à ce qu'elle réponde, mais elle ne le fait pas."
    noam fatigue "Elen, on va pas régler ça dans ce couloir."
    "Personne ne proteste. On entend juste Elias ranger ses outils, un par un, beaucoup trop bruyamment."
    "Je m'assois de l'autre côté du couloir. Personne n'a vraiment envie de retourner à la cafétéria."
    pause 0.5
    "Quand Sael ressort enfin, elle semble aussi épuisée que nous."
    $ showGroup([("elen", "peur", 0.070), ("lysa", "inquiet", 0.166), ("noam", "fatigue", 0.261), ("julian", "inquiet", 0.357), ("mara", "agace", 0.452), ("kael", "inquiet", 0.548), ("elias", "fatigue", 0.643), ("ryn", "inquiet", 0.739), ("nyra", "inquiet", 0.834), ("sael", "fatigue", 0.930)])
    sael fatigue "On va l'emmener à l'infirmerie. Mais je veux d'abord des photos de la chambre."
    noam reflexion "Sael... il est mort de quoi ?"
    sael inquiet "Je n'en sais rien, Noam."
    "Elle se passe une main sur le visage. Je n'avais encore jamais entendu sa voix dérailler comme ça."
    sael fatigue "Je n'ai aucune cause certaine. Il faudra examiner le corps correctement."
    noam fatigue "Ouais."
    lysa inquiet "On peut faire quelque chose ?"
    sael raison "Empêchez les autres d'entrer. Et surtout, que personne ne touche plus à rien."
    "Elle hésite, puis se tourne vers moi."
    sael reflexion "Noam, t'as ta tablette ?"
    noam inquiet "Ouais... pourquoi ?"
    sael triste "Il faut photographier Tomas. Les draps, ses vêtements. Je peux demander à Elias, si tu veux."
    "Je regarde la tablette dans ma main. Hier encore, je m'en servais pour répondre à ses messages. Je finis par hocher la tête."
    noam fatigue "Non. Je vais le faire."
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    "Je lève la tablette vers le lit. Je dois recommencer deux fois avant de réussir à garder les mains assez stables pour cadrer Tomas."
    call j26_photograph("j26_photo_tomas", "j26_elen_corps", (0.355, 0.535), 2.1) from _call_j26_tomas_photo
    "Sael me demande aussi de garder une image du sol. Je me concentre sur les emballages, simplement pour ne plus avoir le lit en face de moi."
    call j26_photograph("j26_photo_dechets", "j26_elen_corps", (0.67, 0.80), 2.0) from _call_j26_dechets_photo
    "Pour le verrou, Elias me montre les dégâts sur le boîtier du couloir. Il confirme avoir forcé la fermeture intérieure."
    $ investigation_add("j26_tomas_verrou", notify=False)
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Quand je ressors, ma tablette est encore ouverte sur la dernière photo. Je l'éteins sans la regarder."
    $ hideGroup()
    jump _26_0_1_1_0_1_INSPECTION_INTRO


# Catalogue local : salles, actions point-and-click et fiches du dossier.
init 10 python:
    J26A_ROOMS = {
        "dortoir": {
            "title": "DORTOIRS — CHAMBRE D'ELEN",
            "background": "j26_elen_vide",
            "description": "La chambre est sous surveillance. Sael a autorisé quelques examens ciblés.",
            "actions": [
                "flacon",
                "grille"
            ]
        },
        "infirmerie": {
            "title": "INFIRMERIE",
            "background": "infirmerie2",
            "description": "Sael travaille sur les premières constatations médicales.",
            "actions": [
                "iris"
            ]
        },
        "repos": {
            "title": "SALLE COMMUNE",
            "background": "bg_repos",
            "description": "Elen essaie de reprendre ses esprits. Sael attend un peu plus loin.",
            "actions": [
                "elen",
                "sael"
            ]
        },
        "cafeteria": {
            "title": "CAFÉTÉRIA",
            "background": "bg_cafeteria",
            "description": "Julian et Nyra sont revenus à la cafétéria après la découverte.",
            "actions": [
                "julian",
                "nyra"
            ]
        },
        "maintenance": {
            "title": "MAINTENANCE",
            "background": "bg_maintenance",
            "description": "Kael et Elias examinent les équipements du couloir.",
            "actions": [
                "kael"
            ]
        },
        "gymnase": {
            "title": "GYMNASE",
            "background": "bg_gymnase",
            "description": "Ryn est venu s'isoler.",
            "actions": [
                "ryn"
            ]
        },
        "archive": {
            "title": "ARCHIVES",
            "background": "bg_archive",
            "description": "Les dernières recherches de Tomas pourraient encore être accessibles.",
            "actions": [
                "notes"
            ]
        },
        "observation": {
            "title": "OBSERVATION",
            "background": "bg_observation",
            "description": "La console sur laquelle Tomas travaillait est restée allumée.",
            "actions": [
                "console"
            ]
        },
        "conclave": {
            "title": "SALLE DU CONCLAVE",
            "background": "bg_conclave",
            "description": "Une salle vide. Celle où Tomas a voté contre.",
            "actions": []
        }
    }
    J26A_ACTIONS = {
        "flacon": {
            "title": "Examiner le flacon",
            "description": "Observer et photographier le flacon, sans perturber le travail de Sael.",
            "label": "_26_0_1_1_0_1_PA_FLACON",
            "evidence": "j26_tomas_flacon"
        },
        "grille": {
            "title": "Observer la grille d'aération",
            "description": "Vérifier les plaques de protection et la circulation de l'air.",
            "label": "_26_0_1_1_0_1_PA_GRILLE",
            "evidence": "j26_tomas_aeration"
        },
        "iris": {
            "title": "Parler à Sael",
            "description": "Demander ce que les constatations permettent réellement de conclure.",
            "label": "_26_0_1_1_0_1_PA_IRIS",
            "evidence": "j26_tomas_rapport"
        },
        "elen": {
            "title": "Parler à Elen",
            "description": "Revenir avec précaution sur l'échange de chambres et la dernière soirée.",
            "label": "_26_0_1_1_0_1_PA_ELEN",
            "evidence": "j26_tomas_echange"
        },
        "sael": {
            "title": "Interroger Sael",
            "description": "Lui demander où elle se trouvait après le dîner.",
            "label": "_26_0_1_1_0_1_PA_SAEL",
            "evidence": "j26_tomas_alibi_sael"
        },
        "julian": {
            "title": "Interroger Julian",
            "description": "Revenir sur sa dispute avec Tomas et ses déplacements.",
            "label": "_26_0_1_1_0_1_PA_JULIAN",
            "evidence": "j26_tomas_alibi_julian"
        },
        "nyra": {
            "title": "Interroger Nyra",
            "description": "Lui demander où elle a passé la nuit après l'avoir croisée aux dortoirs.",
            "label": "_26_0_1_1_0_1_PA_NYRA",
            "evidence": "j26_tomas_alibi_nyra"
        },
        "kael": {
            "title": "Interroger Kael et Elias",
            "description": "Vérifier le verrou et les accès de maintenance.",
            "label": "_26_0_1_1_0_1_PA_KAEL",
            "evidence": "j26_tomas_verrou"
        },
        "ryn": {
            "title": "Interroger Ryn",
            "description": "Vérifier son alibi après les tensions de la veille.",
            "label": "_26_0_1_1_0_1_PA_RYN",
            "evidence": "j26_tomas_alibi_ryn"
        },
        "notes": {
            "title": "Rechercher les travaux de Tomas",
            "description": "Consulter les documents laissés en cours sur Keyper-IIB.",
            "label": "_26_0_1_1_0_1_PA_NOTES",
            "evidence": "j26_tomas_keyper"
        },
        "console": {
            "title": "Examiner la console",
            "description": "Vérifier ce qu'on peut déduire des manipulations de Tomas.",
            "label": "_26_0_1_1_0_1_PA_CONSOLE",
            "evidence": "j26_tomas_console"
        }
    }
    INVESTIGATION_ENTRIES.update({
        "j26_photo_tomas": {"category": "preuves", "title": "TOMAS — VÊTEMENTS TREMPÉS", "desc": "La chemise et les cheveux de Tomas étaient trempés lors de la découverte de son corps.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "j26_elen_corps"},
        "j26_photo_dechets": {"category": "preuves", "title": "DÉCHETS DANS LA CHAMBRE", "desc": "Barquettes, emballages et affaires abandonnées : une odeur forte régnait dans la chambre.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "j26_elen_corps"},
        "j26_photo_verrou": {"category": "preuves", "title": "PORTE VERROUILLÉE", "desc": "Elias a dû forcer le mécanisme engagé depuis l'intérieur pour entrer dans la chambre d'Elen.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "CONSTATATION", "manual_only": True},
        "j26_photo_grille": {"category": "preuves", "title": "PLAQUE DEVANT L'AÉRATION", "desc": "Une plaque de protection ferme le passage physique dans la bouche d'aération ; l'air peut toujours circuler.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "j26_elen_vide"},
        "j26_photo_flacon_detail": {"category": "preuves", "title": "PHOTO — ÉTIQUETTE DES SOMNIFÈRES", "desc": "Cliché complémentaire du flacon examiné avec Sael.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j26_photo_grille_detail": {"category": "preuves", "title": "PHOTO — FIXATIONS DE L'AÉRATION", "desc": "Cliché complémentaire des attaches de la plaque dans la chambre d'Elen.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j26_photo_flacon": {"category": "preuves", "title": "FLACON DE SOMNIFÈRES PRESQUE VIDE", "desc": "Un flacon presque vide a été retrouvé parmi les affaires de la chambre. Rien ne prouve que Tomas en ait pris.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "j26_elen_flacon"},
        "j26_core_mort": {"category": "evenements", "title": "DÉCOUVERTE DU CORPS", "desc": "Tomas a été retrouvé mort dans la chambre d'Elen, derrière une porte verrouillée de l'intérieur.", "day": "J26", "origin": "DORTOIRS", "status": "CONFIRMÉ", "manual_only": True},
        "j26_core_sudation": {"category": "preuves", "title": "PREMIÈRES CONSTATATIONS", "desc": "Sael a constaté l'absence de respiration et une importante sudation. La cause de la mort reste inconnue.", "day": "J26", "origin": "DORTOIRS", "status": "CONFIRMÉ", "manual_only": True},
        "j26_tomas_flacon": {"category": "preuves", "title": "FLACON DE SOMNIFÈRES", "desc": "Un flacon presque vide a été découvert près du lit. Rien ne prouve que Tomas a pris ces comprimés.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_aeration": {"category": "preuves", "title": "GRILLE D'AÉRATION", "desc": "Une plaque empêche physiquement le passage par la grille, mais laisse l'air circuler.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_rapport": {"category": "hypotheses", "title": "CAUSE DU DÉCÈS INCERTAINE", "desc": "Sael a constaté une sudation importante et aucune blessure évidente. Elle ne confirme ni suicide ni empoisonnement.", "day": "J26", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_echange": {"category": "evenements", "title": "ÉCHANGE DE CHAMBRES", "desc": "Tomas et Elen ont échangé leurs chambres pour éviter des visiteurs hostiles. Elen a entendu quelqu'un tambouriner à la porte de Tomas sans voir qui. Elle nie être revenue chez elle la nuit.", "day": "J26", "origin": "TÉMOIGNAGE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_sael": {"category": "personnes", "title": "ALIBI DE SAEL", "desc": "Sael dit avoir passé une partie de la soirée à l'infirmerie, sans témoin constant.", "day": "J26", "origin": "TÉMOIGNAGE DE SAEL", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_julian": {"category": "personnes", "title": "ALIBI DE JULIAN", "desc": "Julian dit avoir passé la soirée avec Ryn et Mara, mais se montre très mal à l'aise sur la suite de sa nuit. Il nie avoir connu l'échange de chambres.", "day": "J26", "origin": "TÉMOIGNAGE DE JULIAN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_nyra": {"category": "personnes", "title": "ALIBI DE NYRA", "desc": "Nyra dit être allée se coucher après sa rencontre avec Noam dans le couloir. Aucun témoin ne confirme la nuit entière.", "day": "J26", "origin": "TÉMOIGNAGE DE NYRA", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_verrou": {"category": "preuves", "title": "VERROU INTÉRIEUR", "desc": "Elias a forcé le verrou engagé depuis l'intérieur. Les protections d'aération sont en place.", "day": "J26", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_ryn": {"category": "personnes", "title": "ALIBI DE RYN", "desc": "Ryn dit avoir passé la soirée avec Julian et Mara puis être allé dormir.", "day": "J26", "origin": "TÉMOIGNAGE DE RYN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_keyper": {"category": "evenements", "title": "DERNIÈRES RECHERCHES DE TOMAS", "desc": "Tomas consultait encore Keyper-IIB et les quotas la veille de sa mort. Cela n'établit aucun mobile.", "day": "J26", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_console": {"category": "anomalies", "title": "CONSOLE D'OBSERVATION", "desc": "La session technique de Tomas a été fermée sans incident apparent. Noam se souvient d'un petit objet examiné la veille.", "day": "J26", "origin": "OBSERVATION", "status": "À VÉRIFIER", "manual_only": True},
    })

label _26_0_1_1_0_1_INSPECTION_INTRO:
    $ current_period = "Après-midi"
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Sael me laisse revenir dans la chambre. Le lit est vide. Ça ne devrait pas me surprendre, et pourtant je m'arrête net."
    $ showGroup([("sael", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    sael raison "Tu peux regarder, mais on ne touche à rien sans me prévenir."
    noam raison "D'accord."
    sael reflexion "Pas de blessure évidente. Rien qui explique ce qu'on a trouvé."
    noam inquiet "Et il était trempé. Tu crois que..."
    sael fatigue "J'ai vu. Ça peut avoir plusieurs causes."
    noam neutre "Même avec la porte fermée ?"
    sael raison "Un verrou ne dit pas pourquoi quelqu'un meurt."
    noam fatigue "Je sais. Mais j'aimerais bien qu'il nous dise au moins comment."
    sael fatigue "Moi aussi."
    noam inquiet "Tu dois en avoir marre qu'on te demande une réponse toutes les trente secondes."
    sael raison "Je préfère que tu me poses une question plutôt que de décider seul qu'il a été empoisonné."
    noam fatigue "C'est une façon polie de me dire de me taire ?"
    sael neutre "C'est une façon polie de te demander de réfléchir avant de parler."
    noam fatigue "D'accord. C'était bien ça."
    "Je regarde la tôle devant l'aération. Sael me laisse la photographier sans toucher aux attaches."
    $ hideGroup()
    call j26_photograph("j26_photo_grille", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j26_grille_photo
    $ showGroup([("sael", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    "Les fixations semblent en place. Un filet d'air passe encore sur le côté."
    sael inquiet "Elen est avec Lysa ?"
    noam fatigue "Oui. Elle a réussi à dormir un peu."
    sael neutre "Tant mieux."
    "Je baisse ma tablette, mais je revois encore Tomas sur le lit."
    noam reflexion "Je vais demander aux autres ce qu'ils faisaient hier soir."
    sael fatigue "Fais attention à la manière dont tu poses tes questions. Elen n'a pas besoin de se sentir accusée."
    noam neutre "Je sais."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE_FLACON

label _26_0_1_1_0_1_DECOUVERTE_FLACON:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    "Avant de quitter la chambre, Sael remarque un objet derrière la table de chevet."
    $ showGroup([("sael", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    sael surpris "Attends. Qu'est-ce que c'est ?"
    "Elle se penche et découvre un petit flacon presque vide."
    noam surpris "Il était là depuis le début ?"
    sael reflexion "On dirait. Je regarde l'étiquette."
    "Elle le tourne sous la lampe."
    sael raison "Des comprimés pour dormir."
    noam inquiet "Tomas en prenait ?"
    sael raison "Je n'en sais rien. Et ce flacon n'est peut-être même pas à lui."
    sael fatigue "Prends une photo avant qu'on le mette de côté."
    $ hideGroup()
    scene j26_elen_flacon at adaptive_fullscreen with dissolve
    call j26_photograph("j26_photo_flacon", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_photo
    "Sael me demande de laisser le flacon en place pour le moment."
    $ showGroup([("sael", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    noam fatigue "Tu crois qu'il aurait pu en prendre trop ?"
    sael fatigue "Je ne sais même pas s'il en a pris un seul."
    noam inquiet "Hier soir, il était vraiment pas bien..."
    sael raison "Justement. Ne tire pas de conclusion avant qu'on ait des résultats."
    "Sael prépare un sachet, puis laisse le flacon en place pour une dernière photographie de l'étiquette."
    noam fatigue "D'accord."
    $ j26_alt_flacon = True
    $ hideGroup()
    jump _26_0_1_1_0_1_ENQUETE

label _26_0_1_1_0_1_ENQUETE:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je retrouve Lysa dans la salle commune. Elle tient une tasse de café qu'elle n'a pas touchée. Nyra est en face, la tablette posée sur ses genoux."
    $ showGroup([("nyra", "neutre", 0.22), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.71)])
    lysa fatigue "Elen dort enfin. Si quelqu'un la réveille pour lui poser des questions, je lui casse les jambes."
    noam reflexion "Je vais devoir lui parler à un moment."
    lysa inquiet "Bah pas maintenant."
    nyra raison "On peut déjà voir ailleurs. Les gens vont commencer à se raconter des choses, et demain on saura plus ce qui s'est vraiment passé."
    noam fatigue "J'ai pas envie de passer pour le type qui suspecte tout le monde."
    lysa neutre "Alors commence par leur parler normalement. Et si quelqu'un te dit de dégager, tu dégages."
    noam neutre "OK."
    "Je cherche sur la tablette les dernières notes de Tomas. Il y a tellement de pistes que je pourrais y passer la nuit."
    nyra raison "Tu vas t'épuiser si tu veux tout faire aujourd'hui."
    lysa reflexion "Commence par ce qui te semble important. On n'aura pas le temps de retourner toute la station aujourd'hui."
    noam sourire "Tu comptes ça comme un conseil médical ?"
    lysa fatigue "Comme une menace."
    "Je regarde l'heure sur ma tablette. Je vais devoir choisir où commencer si je veux encore voir les autres ce soir."
    $ investigation_pa_begin(26, 5)
    $ investigation_unlocked = True
    $ investigation_add("j26_core_mort", notify=False)
    $ investigation_add("j26_core_sudation", notify=False)
    $ free_time_active = False
    $ conclave_lock = False
    $ dortoir_lock = False
    $ exploration_libre_active = True
    $ exploration_libre_allowed_rooms = list(J26A_ROOMS.keys())
    $ current_scene_active = None
    $ corridor_current = "dortoir"
    $ hideGroup()
    jump _26_0_1_1_0_1_PA_MAP

label _26_0_1_1_0_1_PA_MAP:
    # Compatibilité avec les anciens jumps et sauvegardes.
    jump _26_0_1_1_0_1_PA_CORRIDORS

label _26_0_1_1_0_1_PA_CORRIDORS:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_j26a_pa_corridors
    $ investigation_pa_current_room = _return
    if investigation_pa_current_room not in J26A_ROOMS:
        jump _26_0_1_1_0_1_PA_CORRIDORS
    jump _26_0_1_1_0_1_PA_ROOM

label _26_0_1_1_0_1_PA_ROOM:
    call screen investigation_pa_room(investigation_pa_current_room, J26A_ROOMS, J26A_ACTIONS)
    if _return == "finish":
        jump _26_0_1_1_0_1_BILAN
    if _return == "corridors":
        call EXIT_ROOM_TO_CORRIDOR from _call_j26a_pa_exit_room_native
        jump _26_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_selected = _return
    if not investigation_pa_can_take(investigation_pa_selected):
        jump _26_0_1_1_0_1_PA_ROOM
    call INVESTIGATION_PA_CHOICE(J26A_ACTIONS[investigation_pa_selected], investigation_pa_current_room) from _call_j26a_pa_choice_native
    if not _return:
        jump _26_0_1_1_0_1_PA_ROOM
    if not investigation_pa_spend(investigation_pa_selected):
        jump _26_0_1_1_0_1_PA_ROOM
    call expression J26A_ACTIONS[investigation_pa_selected]["label"] from _call_j26a_pa_action_dynamic
    $ investigation_add(J26A_ACTIONS[investigation_pa_selected]["evidence"])
    if investigation_pa_remaining == 0:
        "Je regarde l'heure. Il se fait tard. Les autres nous attendent pour faire le point."
        jump _26_0_1_1_0_1_BILAN
    jump _26_0_1_1_0_1_PA_ROOM


label _26_0_1_1_0_1_PA_FLACON:
    scene j26_elen_flacon at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    $ showGroup([("sael", "fatigue", 0.34), ("noam", "neutre", 0.68)])
    noam reflexion "Tu ne l'as toujours pas emporté ?"
    sael raison "Je voulais le photographier de près avant. Ne le touche pas."
    "Elle me désigne le flacon encore posé à l'écart."
    noam reflexion "Il en reste presque pas..."
    sael raison "On ne sait même pas combien il en contenait hier."
    noam inquiet "Tu pourras savoir s'il en a pris ?"
    sael fatigue "Je vais essayer. Pas forcément aujourd'hui."
    $ hideGroup()
    call investigation_take_manual_photo("j26_photo_flacon_detail", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_detail_photo
    $ showGroup([("sael", "fatigue", 0.34), ("noam", "neutre", 0.68)])
    "Sael vérifie l'étiquette et range le sachet dans son matériel."
    noam fatigue "J'aimerais juste être sûr..."
    sael neutre "Je sais. Moi aussi."
    $ j26_alt_flacon = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_GRILLE:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam reflexion "Tu vois la tôle, là-haut ?"
    lysa raison "Ouais. C'est Elias qui avait mis ces protections, non ?"
    noam reflexion "Il devait les avoir posées partout. Je veux revoir les fixations."
    "Je reprends un cliché. Lysa reste derrière moi, les bras croisés."
    $ hideGroup()
    call investigation_take_manual_photo("j26_photo_grille_detail", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j26_grille_detail_photo
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    "Les clous sont toujours en place. Je passe la main près du bord et sens l'air sur mes doigts."
    noam raison "On dirait que personne l'a bougée."
    lysa neutre "Ou alors il a fallu la remettre exactement comme avant. Mais va savoir."
    noam reflexion "Tu sens ? Ça souffle quand même."
    lysa blase "Encore heureux. Bon, t'as ta photo ?"
    noam neutre "Ouais. Je sais pas si ça servira."
    lysa raison "Bah on la garde. Ce sera toujours mieux que de se fier à nos souvenirs."
    $ j26_alt_vent = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_IRIS:
    # Identifiant de label historique conservé pour les sauvegardes.
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Le lit de Tomas est dissimulé derrière un rideau. Sael est penchée sur ses notes."
    $ showGroup([("sael", "fatigue", 0.34), ("noam", "inquiet", 0.68)])
    sael fatigue "Si tu viens chercher une cause de décès, je n'en ai pas encore."
    noam raison "Je voulais juste savoir ce qui te paraît bizarre."
    sael reflexion "Il n'avait pas de blessure visible. Ses vêtements étaient trempés. C'est ce qu'on peut dire pour le moment."
    noam inquiet "Tu crois qu'il a souffert ?"
    sael triste "Je ne peux pas te répondre."
    noam fatigue "D'accord."
    noam raison "Et l'odeur dans la chambre ?"
    sael reflexion "Elle m'a donné mal à la tête. Il y avait beaucoup de nourriture avariée, mais je ne peux pas dire d'où venait exactement cette odeur."
    noam neutre "Tu me préviens quand tu sais quelque chose ?"
    sael raison "Oui. Et Noam... ne regarde pas derrière le rideau, d'accord ?"
    noam neutre "D'accord. Je te laisse travailler."
    $ j26_alt_corps = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_ELEN:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Elen est recroquevillée sous une couverture. Lysa lève les yeux vers moi avec une expression qui me fait comprendre que je ferais mieux d'avoir une très bonne raison d'être là."
    $ showGroup([("elen", "triste", 0.23), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.71)])
    noam neutre "Elen... Tu préfères que je revienne ?"
    elen fatigue "Non. T'as quelque chose à me demander, je sais."
    noam neutre "Je veux pas t'embêter."
    elen triste "Alors demande. J'en ai marre que tout le monde chuchote quand j'arrive."
    noam fatigue "On essayait juste de te laisser souffler."
    elen triste "En me regardant comme si j'allais tomber en morceaux ? Ça aide pas."
    noam fatigue "Ouais. Désolé."
    elen triste "Je veux bien qu'on s'inquiète pour moi. Mais j'ai toujours une bouche, vous savez."
    lysa inquiet "Et tu sais très bien t'en servir."
    elen fatigue "Alors pose ta question. Et si j'ai pas envie de répondre, je te le dirai."
    "Elle essaie de sourire, n'y arrive pas, puis attend sans détourner les yeux."
    pause 0.3
    noam reflexion "Hier, quand tu lui as proposé ta chambre... il avait dit quoi ?"
    elen fatigue "Pas grand-chose. Il a demandé si j'étais sûre. Deux fois."
    lysa inquiet "Et toi ?"
    elen triste "Je lui ai dit que j'avais pas peur d'une bande d'idiots qui tapent aux portes. Il a rigolé un peu, même."
    "Elle tire sur le bord de la couverture."
    noam raison "Et ces coups à la porte de Tomas, tu les as entendus quand ?"
    elen inquiet "Avant qu'on échange. Je passais devant sa chambre et quelqu'un tambourinait dessus. C'était violent, pas juste quelqu'un qui frappait pour discuter."
    noam reflexion "T'as vu qui c'était ?"
    elen fatigue "Non. Je voulais pas me mêler d'une autre dispute. J'ai continué mon chemin."
    noam raison "Après, vous avez fait quoi ?"
    elen fatigue "On s'est souhaité bonne nuit. Moi, je suis allée dans sa chambre, et j'en ai pas bougé."
    noam neutre "Vous étiez seuls quand vous en avez parlé ?"
    elen reflexion "Je sais pas. On était dans le couloir. Des gens passaient, je crois. Pourquoi ?"
    noam inquiet "Je me demandais juste qui était au courant."
    elen fatigue "Tu penses que quelqu'un a attendu qu'il aille dans ma chambre ?"
    noam fatigue "J'en sais rien, Elen."
    "Lysa me lance un regard noir. Je m'en veux aussitôt de ne pas avoir arrêté plus tôt."
    noam inquiet "Le petit flacon que Sael a trouvé, c'était à toi ?"
    elen surpris "Quel flacon ?"
    noam raison "Un truc pour dormir."
    elen fatigue "Peut-être. J'en ai dans ma trousse, parfois. Je sais même pas combien il en restait."
    elen triste "Il m'avait rien demandé, Tomas. Il voulait juste dormir..."
    "Elle se couvre le visage et se met à pleurer. Lysa se penche près d'elle."
    lysa inquiet "C'est bon, Noam."
    noam fatigue "Ouais. Désolé."
    elen triste "Non, attends... C'est pas toi."
    noam neutre "Je repasserai plus tard."
    $ j26_alt_elen = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_SAEL:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("sael", "neutre", 0.35), ("noam", "neutre", 0.69)])
    sael reflexion "Tu viens pour Tomas ?"
    noam fatigue "Ouais. Tu te rappelles où t'étais hier soir ?"
    "Sael repose son linge. Pas d'un coup, mais assez fort pour que je comprenne."
    sael neutre "C'est donc à mon tour."
    noam inquiet "Je voulais pas..."
    sael raison "Alors pose ta question."
    noam neutre "À l'infirmerie ?"
    sael neutre "D'abord. Iris m'a vue. Ensuite, j'ai fermé et je suis allée dormir."
    noam reflexion "T'as croisé Ryn ?"
    sael reflexion "Dans le couloir. Il râlait encore contre le vote."
    noam fatigue "Et ensuite ?"
    sael raison "Ensuite, Noam, j'ai dormi. Je n'ai pas de témoin pour ça et je n'en inventerai pas."
    "Je baisse les yeux vers le linge qu'elle n'a pas repris."
    sael fatigue "J'ai un mort à examiner, et tu me demandes de prouver que je n'en suis pas responsable."
    noam fatigue "Pardon. Je savais pas comment te le demander."
    sael raison "La prochaine fois, commence par ça. Je t'aurais répondu pareil."
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Julian tourne sa cuillère dans un café froid. Quand je m'assois en face de lui, il arrête aussitôt."
    $ showGroup([("julian", "agace", 0.35), ("noam", "neutre", 0.70)])
    julian agace "Vas-y. Pose ta question."
    noam reflexion "Je voulais savoir si t'avais revu Tomas après le dîner."
    julian colere "Non. Et si tu veux savoir où j'étais : avec Ryn et Mara. Après, je suis rentré."
    noam agace "Tu peux me laisser poser mes questions au lieu de deviner ?"
    julian fatigue "..."
    "Il repousse sa tasse jusqu'au bord de la table."
    noam raison "Vous êtes restés longtemps ensemble ?"
    julian reflexion "J'en sais rien. Une heure ? Deux ? On parlait de ce fichu vote."
    noam raison "Et après, t'as fait quoi exactement ?"
    "Julian jette un regard vers la sortie. Il serre sa tasse jusqu'à blanchir les jointures."
    julian fatigue "Je te l'ai dit. Je suis rentré."
    noam reflexion "Directement ?"
    julian agace "Tu veux un compte rendu minute par minute de ma soirée ?"
    noam neutre "Je veux juste comprendre."
    "Il ouvre la bouche, puis la referme. Son regard ne se pose plus sur moi."
    julian fatigue "J'ai traîné un peu. Voilà. Je vais pas faire semblant de me rappeler chaque détour."
    noam neutre "Et tu savais qu'Elen et Tomas avaient échangé leurs chambres ?"
    julian surpris "Quoi ?"
    noam neutre "Il avait peur qu'on revienne l'emmerder. Il a dormi chez elle."
    "Julian fixe sa tasse. Sa cuillère glisse et tombe sur la table."
    julian triste "..."
    julian fatigue "Merde."
    noam inquiet "Quoi ?"
    julian triste "Je lui ai dit des horreurs hier. Devant tout le monde."
    noam neutre "Ouais, je sais."
    julian agace "Et toi, tu fais quoi, là ? Tu viens me dire que c'est de ma faute ?"
    noam fatigue "Non, Julian. J'ai pas dit ça."
    julian triste "Ouais... pardon. J'ai juste pas envie que la dernière chose qu'il ait entendue de moi, ce soit ça."
    "Il ramasse sa cuillère. Il n'en fait rien, la garde simplement entre ses doigts."
    $ j26_alt_julian = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_NYRA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("nyra", "neutre", 0.36), ("noam", "neutre", 0.70)])
    nyra reflexion "T'as une sale tête. Assieds-toi."
    noam fatigue "Je voulais te demander..."
    nyra sourire "Hier soir ? Tu cherches qui a croisé qui. J'imagine que je suis sur la liste."
    noam neutre "Tu me facilites pas la tâche."
    nyra raison "Je suis rentrée après qu'on s'est croisés. Je n'ai pas revu Tomas."
    noam reflexion "Tu savais pour l'échange de chambres ?"
    nyra hesitation "Qu'Elen voulait l'aider, oui. Pas où Tomas allait dormir exactement."
    "Nyra pousse une tasse vers moi."
    nyra neutre "Et toi ? À quelle heure tu es rentré ?"
    noam surpris "Moi ?"
    nyra sourire "Je réponds à tes questions. Je me disais qu'on pouvait essayer dans les deux sens."
    noam fatigue "J'ai pas regardé l'heure."
    nyra raison "Voilà. Tu vois pourquoi les souvenirs de chacun ne suffisent pas."
    noam inquiet "Tu crois que quelqu'un ment ?"
    nyra neutre "Je crois qu'on est tous fatigués. Si tu pars de l'idée qu'on te ment, tu n'entendras plus rien d'autre."
    "Elle reprend sa tasse. Je ne sais toujours pas si elle essaie de m'aider ou d'orienter mes questions."
    $ j26_alt_nyra = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    $ showGroup([("kael", "calme", 0.21), ("elias", "fatigue", 0.45), ("noam", "neutre", 0.70)])
    "Elias a gardé l'outil dont il s'est servi ce matin sur l'établi. Il le fait tourner entre ses doigts sans s'en rendre compte."
    noam raison "La porte d'Elen... elle était vraiment verrouillée de l'intérieur ?"
    elias fatigue "Ouais. Tu veux voir l'outil que j'ai flingué pour l'ouvrir ?"
    "Il me montre le métal tordu sur l'établi."
    noam inquiet "T'es sûr qu'on pouvait pas passer avec un badge ?"
    elias agace "Noam. Si un badge suffisait, tu crois que j'aurais massacré ce truc ?"
    kael neutre "Le verrou intérieur bloque le lecteur. Les conduits ont aussi une protection."
    elias fatigue "C'est moi qui l'ai posée. Et avant que tu demandes : oui, l'air passe. Non, une personne passe pas."
    noam reflexion "Et hier soir, vous étiez ensemble ?"
    kael reflexion "On a réparé une fuite ici. Après on est partis chacun de notre côté."
    elias fatigue "Je suis rentré. J'ai pas vu Tomas."
    noam raison "Les badges ont dû laisser une trace ?"
    kael neutre "Des heures de passage. Pas des visages. Je regarderai."
    elias inquiet "Tu crois qu'il nous a entendus forcer la porte ?"
    noam fatigue "Je crois pas, Elias."
    "Il repose son outil. Cette fois, il le laisse sur la table."
    $ j26_alt_verrou = True
    $ j26_alt_kael = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_RYN:
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Ryn frappe dans un sac sans y mettre de force. Quand il me voit, il donne un dernier coup plus violent et se retourne."
    $ showGroup([("ryn", "agace", 0.35), ("noam", "neutre", 0.69)])
    ryn agace "Quoi ?"
    noam raison "Je voulais te demander pour hier soir."
    ryn colere "Je sais. Tout le monde veut me demander pour hier soir."
    noam fatigue "Je te demande si t'as revu Tomas."
    ryn colere "Non ! J'étais avec Julian et Mara. Après, je suis rentré."
    noam neutre "À quelle heure ?"
    "Ryn se retourne et frappe le sac si fort que la chaîne grince."
    ryn colere "J'EN SAIS RIEN ! Ça va, maintenant ?!"
    noam colere "Non. Pas si tu me hurles dessus chaque fois que je pose une question."
    ryn agace "Tu crois que je fais quoi depuis ce matin ? Que je me dis que c'est bien fait pour lui ?"
    noam fatigue "J'ai pas dit ça."
    ryn fatigue "Hier, je lui ai dit qu'il nous avait tous lâchés. Devant tout le monde."
    noam neutre "Je sais. J'étais là."
    ryn fatigue "Ouais. Moi aussi. Et je me la repasse en boucle, cette scène."
    "Il me montre ses poings, puis les cache aussitôt."
    ryn fatigue "J'aurais voulu lui parler autrement. Voilà. T'as ton témoignage."
    noam inquiet "Ryn..."
    ryn triste "Vas-y. Sors, s'il te plaît."
    $ j26_alt_ryn = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_NOTES:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je retrouve le terminal que Tomas utilisait. Il a laissé une page de chiffres à moitié ouverte, comme s'il comptait revenir dessus après le dîner."
    noam reflexion "Keyper-IIB..."
    "Des quotas, des effectifs, des codes que je n'arrive toujours pas à comprendre. Hier, Tomas aurait déjà commencé à m'expliquer pourquoi une colonne ne collait pas."
    "L'historique indique qu'il a consulté ces documents jusqu'à la veille. Je me surprends à regarder l'heure de sa dernière recherche."
    noam fatigue "T'étais encore là-dessus..."
    "Je copie le titre et la date. C'est peut-être important. Ou peut-être que je fais ça parce que je n'ai aucune idée d'où commencer."
    return

label _26_0_1_1_0_1_PA_CONSOLE:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "La salle d'observation est vide. Je retrouve la console où Tomas m'avait montré la carte de Keyper et, pendant une seconde, je m'attends à le voir arriver derrière moi."
    "Les derniers réglages datent de sa visite. Rien ne saute aux yeux."
    "Je repense au petit truc métallique qu'il tenait hier. Je l'avais vu le reposer en me parlant, mais j'ai passé la suite de la conversation à regarder la carte."
    noam reflexion "Merde. C'était où, déjà ?"
    "Je cherche dans les tiroirs, puis sur les étagères. Aucun des petits boîtiers ne ressemble vraiment à ce dont je me souviens."
    noam fatigue "Si j'avais su que c'était la dernière fois..."
    "Je ferme le tiroir. Je ne sais même pas si cet appareil avait la moindre importance."
    return


label _26_0_1_1_0_1_BILAN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    $ current_period = "Soir"
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Quand je reviens dans la salle commune, Lysa est toujours devant son café de ce matin. J'ai parlé à plein de gens, et tout ce que j'ai envie de faire, c'est m'asseoir."
    $ showGroup([("lysa", "fatigue", 0.21), ("nyra", "neutre", 0.46), ("noam", "fatigue", 0.70)])
    lysa reflexion "T'as trouvé quelque chose ?"
    noam fatigue "Plein de choses. Une réponse, non."
    nyra raison "Montre-moi ce que tu as noté, pas ce que tu crois."
    "Je fais défiler les témoignages sur la tablette. Lysa ne regarde même pas l'écran."
    if "iris" in investigation_pa_completed:
        noam neutre "Sael ne sait toujours pas comment il est mort."
        lysa fatigue "Et elle va pas le deviner parce qu'on lui demande plus fort."
    if "flacon" in investigation_pa_completed:
        noam reflexion "Il y a ce flacon pour dormir. Presque vide."
        nyra raison "Mais aucune preuve que Tomas ait pris ces comprimés."
    if "elen" in investigation_pa_completed:
        noam inquiet "Elen a entendu quelqu'un frapper très fort à la porte de Tomas. Elle n'a pas vu qui."
        lysa inquiet "J'espère que tu lui as pas fait répéter ça cinq fois."
        noam fatigue "Non."
    if "julian" in investigation_pa_completed:
        noam neutre "Julian était avec Ryn et Mara. Après, il devient flou."
    if "ryn" in investigation_pa_completed:
        noam fatigue "Ryn confirme leur soirée. Il a surtout envie de cogner dans un mur."
        lysa blase "Ça, c'est pas une nouveauté."
    if "nyra" in investigation_pa_completed:
        nyra neutre "Et je t'ai dit que je suis rentrée me coucher. Sans témoin."
    if "kael" in investigation_pa_completed or "grille" in investigation_pa_completed:
        noam reflexion "Le verrou était engagé. La grille aussi. Voilà ce qu'on a pu vérifier."
    if "notes" in investigation_pa_completed or "console" in investigation_pa_completed:
        noam fatigue "Et Tomas travaillait encore sur Keyper hier."
        lysa neutre "Il avait toujours un truc à terminer."
    if investigation_pa_remaining > 0:
        lysa reflexion "T'as pas pu voir tout le monde ?"
        noam fatigue "Non. Et je commence à plus entendre mes propres questions."
    else:
        lysa fatigue "T'as même fait le tour de la station."
        noam fatigue "Ouais. Tout ça pour une tablette pleine de points d'interrogation."
    noam reflexion "Avec cette porte fermée... je me demande s'il s'est pas donné la mort."
    lysa inquiet "T'as même pas une cause de décès, Noam !"
    noam agace "Je dis pas que j'en suis sûr. J'essaie de comprendre."
    nyra raison "Alors ne transforme pas une possibilité en conclusion. Ni devant Elen, ni devant les autres."
    noam fatigue "Ouais. D'accord."
    "Je ferme la tablette. Lysa a toujours son café entre les mains, mais elle n'y a pas touché."

    pause 0.4
    lysa triste "L'autre jour, il avait pris ma place à table. Je lui ai fait toute une histoire pour ça."
    noam inquiet "Lysa..."
    lysa fatigue "Il s'est levé direct. Et après, il m'a demandé si je voulais son dessert. Quel idiot..."
    "Elle essaie de rire, mais ça ne sort pas. Elle essuie rapidement ses yeux et repousse sa tasse."
    lysa fatigue "Bon. On a rendez-vous avec les autres, non ?"
    nyra reflexion "Ouais. Faudra leur dire qu'on n'a pas trouvé de réponse."
    noam raison "Ils vont adorer."
    $ hideGroup()
    jump _26_0_1_1_0_1_REUNION

label _26_0_1_1_0_1_REUNION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "La place de Tomas est vide. J'ai beau le savoir, je regarde quand même sa chaise avant de m'asseoir."
    $ showGroup([("julian", "fatigue", 0.080), ("elen", "triste", 0.185), ("noam", "fatigue", 0.290), ("iris", "fatigue", 0.395), ("ryn", "agace", 0.500), ("sael", "neutre", 0.605), ("nyra", "neutre", 0.710), ("lysa", "neutre", 0.815), ("mara", "fatigue", 0.920)])
    julian reflexion "On est tous là ?"
    elen fatigue "Pas tous."
    julian triste "..."
    julian fatigue "Oui. Pardon."
    "Personne ne sait comment commencer. Sael finit par prendre la parole."
    sael raison "J'ai pas grand-chose à vous dire. Je cherche toujours ce qui a causé sa mort."
    elen inquiet "Et les médicaments ?"
    sael raison "J'ai trouvé un flacon dans la chambre. Je ne sais pas s'il en a pris."
    elen triste "C'était ma chambre..."
    sael fatigue "Je sais, Elen. Pardon."
    elen inquiet "Je veux dire... et si quelqu'un venait pour moi ? Si c'était pas Tomas qui devait dormir là ?"
    noam raison "On sait pas si quelqu'un est entré. Elias a dû forcer le verrou."
    elen triste "Mais alors comment il est mort ?"
    "Sael reste silencieuse. Elle serre un instant les mâchoires."
    sael fatigue "J'aimerais vraiment pouvoir te répondre. Là, je peux pas."
    "Elen baisse la tête. Personne ne lui demande d'arrêter de pleurer."
    ryn reflexion "Hier, il était déjà pas bien. Vous l'avez tous vu."
    julian fatigue "Ouais. Y avait pas grand monde qui l'aidait, hein."
    ryn agace "Tu vas pas commencer à me faire la morale ! T'as passé la soirée à lui hurler dessus !"
    julian colere "Et toi, tu faisais quoi ? Tu lui apportais des fleurs ?"
    noam colere "Vous pouvez arrêter deux secondes ?!"
    "Julian se redresse. Ryn serre les poings, mais aucun des deux ne bouge."
    julian triste "Je lui ai dit qu'il gâchait tout pour nous. Je voulais pas que ça se termine comme ça."
    ryn fatigue "Personne voulait ça. Putain."
    if "julian" in investigation_pa_completed or "ryn" in investigation_pa_completed:
        noam neutre "J'ai parlé à deux ou trois personnes. On se rappelle même pas tous des mêmes heures."
        julian reflexion "Donc tu penses que quelqu'un ment ?"
        noam raison "Non, Julian. Je dis juste que j'ai rien pu vérifier."
    sael raison "Hé. On a déjà passé assez de temps à s'en vouloir ces derniers jours. Vous allez pas recommencer ici."
    nyra neutre "Sael a dit qu'elle cherchait encore. On peut peut-être lui laisser une nuit avant de tout retourner."
    noam raison "Ouais. Pour ce soir, on arrête."
    if "flacon" in investigation_pa_completed:
        noam neutre "Et le flacon, on sait même pas à qui étaient les comprimés."
    if "kael" in investigation_pa_completed:
        noam raison "Même avec ce verrou, je comprends pas ce qu'il s'est passé."
    if "elen" in investigation_pa_completed:
        noam raison "Tomas avait juste voulu dormir ailleurs. C'est tout ce qu'Elen lui avait proposé."
    julian reflexion "Il y a aussi le vote de demain."
    elen colere "Quoi ?"
    julian inquiet "J'ai pas dit qu'on devait le faire ! Mais Kami va forcément en parler. Vous le savez."
    elen colere "Tomas vient de mourir, Julian. Tu peux pas nous laisser cinq minutes ?"
    julian fatigue "Je sais ! Mais si on fait rien et qu'elle nous tombe dessus, c'est encore nous qui allons payer !"
    noam raison "Alors on lui répondra tous. Ensemble. Mais on va pas s'asseoir demain pour voter comme si de rien n'était."
    elen triste "Moi, de toute façon, je pourrai pas."
    lysa neutre "Moi non plus."
    mara fatigue "Pareil. Elle nous gonfle déjà assez comme ça."
    "Un à un, les autres finissent par approuver. Julian regarde les places vides, puis pose les mains sur la table."
    julian fatigue "OK. Mais je veux pas qu'on laisse quelqu'un assumer ça tout seul."
    $ j26_alt_boycott = True
    $ hideGroup()
    play sound sfx_announce
    stop music fadeout 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Oh ! Un boycott collectif ? Vous êtes adorables !"
    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "Moi qui avais préparé un beau débat sur le droit d'exprimer son opinion..."
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Je rappelle tout de même qu'un décès ne suspend pas automatiquement le calendrier du Conclave."
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Mais si vous ne participez pas, aucun nouveau Commandement ne sera adopté demain."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Allez, reposez-vous. Essayez juste de ne pas perdre un autre représentant, d'accord ?"
    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.070), ("elen", "triste", 0.177), ("noam", "fatigue", 0.285), ("iris", "fatigue", 0.393), ("ryn", "agace", 0.500), ("sael", "neutre", 0.607), ("nyra", "neutre", 0.715), ("lysa", "neutre", 0.823), ("mara", "fatigue", 0.930)])
    elen colere "Je peux plus l'entendre."
    iris agace "Ouais. Moi non plus."
    "Personne ne se lève tout de suite. Je regarde encore la place de Tomas, puis je pousse ma chaise."
    noam fatigue "Venez. On s'en va."
    $ hideGroup()
    jump _26_0_1_1_0_1_NUIT

label _26_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "J'ai enfin fermé ma porte. Je pose la tablette sur mon lit sans même prendre le temps d'enlever mes chaussures."
    "Dans le couloir, quelqu'un passe en parlant à voix basse. J'entends une porte se refermer. Tout est normal. Et c'est ça qui me donne envie de hurler."
    "Hier, Tomas était là. Il aurait pu venir me demander si je savais comment trier ses dossiers ou s'il avait droit à une deuxième portion de café."
    "J'aurais râlé. Je lui aurais dit de se débrouiller. Et demain, il serait revenu."
    pause 0.3
    "Je retrouve dans les anciens messages une conversation où il me demandait si je pouvais vérifier une référence sur sa tablette. J'avais répondu « après le dîner ». Je ne l'ai jamais fait."
    noam fatigue "Merde, Tomas..."
    "J'ouvre le dossier d'enquête. J'y ai rangé des heures, des noms, des photos. Je reste longtemps sur la première, celle du lit, avant de faire défiler les autres."
    if "flacon" in investigation_pa_completed:
        "Je revois le flacon de somnifères. Je sais même pas s'il est lié à sa mort."
    if "elen" in investigation_pa_completed:
        "Je repense à Elen qui répétait qu'elle voulait juste l'aider à dormir."
    if "julian" in investigation_pa_completed or "ryn" in investigation_pa_completed:
        "Je me rappelle aussi la colère des autres. Et leur tête, aujourd'hui, quand ils ont compris qu'il ne reviendrait pas."
    if "notes" in investigation_pa_completed or "console" in investigation_pa_completed:
        "Il travaillait encore sur Keyper. J'avais l'impression que c'était la seule chose qui lui donnait encore envie de parler."
    else:
        "Hier, il cherchait toujours des réponses sur Keyper, cette station dont il m'avait parlé."
    "Il y avait aussi ce petit appareil qu'il avait reposé dans la salle d'observation. J'ai à peine regardé."
    noam reflexion "J'ai beau retourner ça dans tous les sens... Je vois pas comment ça pourrait être autre chose qu'un suicide."
    "La porte était verrouillée de l'intérieur. Elias a dû forcer le mécanisme. La plaque devant la grille bloquait le passage, même si l'air circulait encore."
    "Et surtout, personne n'avait de raison valable de s'en prendre à Elen. Pas à ma connaissance, en tout cas."
    "Tomas était épuisé, il avait peur, et on a trouvé des somnifères. Ça dessine une explication terriblement simple, même si Sael n'a confirmé aucune cause de décès."
    noam fatigue "Mais il y a quelque chose qui me gêne."
    "Je revois son dernier message. Je repense à ses recherches inachevées et à la chambre qu'il avait choisie pour se cacher."
    noam raison "Je vais continuer à creuser. J'ai besoin d'en être sûr."
    "Demain, j'irai dans sa chambre. Je veux comprendre ce qu'il avait commencé, et ce qu'il comptait faire après."
    "Je ferme le dossier. Une seconde plus tard, je le rouvre, comme si quelque chose allait apparaître."
    "Rien. J'éteins enfin l'écran."
    stop music fadeout 1.0
    call end_day("27", sleeping=True) from _call_j26_alt_end_day_27
    jump _27_0_1_1_0_1_REVEIL
