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
    "Je me réveille en repensant aux pancartes d'hier. Des gens veulent empêcher Tomas de rentrer sur Terre."
    "Ma tablette affiche le rappel du vote de demain. J'ai vraiment pas envie de retourner autour de cette table."
    think "J'espère que Tomas a réussi à dormir."
    noam fatigue "Allez. Petit-déjeuner."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j26_alt_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _26_0_1_1_0_1_CAFETERIA
# Durée : 45 s — Total : 45 s.

label _26_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j26_alt_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    $ showGroup([("julian", "neutre", 0.23), ("iris", "fatigue", 0.48), ("mara", "taquin", 0.74)])
    julian reflexion "Vous avez lu le nouveau texte ? Sur les sanctions pour les opinions ?"
    iris fatigue "J'ai essayé. Puis t'as commencé à parler."
    mara sourire "Moi j'ai retenu qu'on avait le droit de dire que Julian était chiant."
    julian agace "C'est pas ce que dit le texte !"
    $ showGroup([("elen", "fatigue", 0.23), ("lysa", "blase", 0.48), ("noam", "neutre", 0.74)])
    noam neutre "Salut."
    elen sourire "Salut, Noam !"
    lysa reflexion "Attendez. Tomas est où ?"
    $ showGroup([("julian", "fatigue", 0.24), ("elen", "fatigue", 0.49), ("noam", "neutre", 0.74)])
    julian fatigue "Il nous évite encore."
    elen reflexion "Je pense qu'il dort. Il était vraiment fatigué."
    $ showGroup([("lysa", "inquiet", 0.24), ("elen", "fatigue", 0.49), ("noam", "neutre", 0.74)])
    lysa inquiet "Il est jamais en retard, même quand il a dormi deux heures."
    elen neutre "Je lui ai prêté ma chambre hier soir. On a échangé."
    $ showGroup([("mara", "taquin", 0.22), ("elen", "neutre", 0.49), ("noam", "neutre", 0.74)])
    mara taquin "Oh ! Monsieur a passé la nuit dans ton lit ?"
    elen colere "Mara !"
    mara rire "Quoi ?! C'était gratuit, je sais, mais fallait que je la fasse."
    $ showGroup([("lysa", "inquiet", 0.22), ("elen", "inquiet", 0.49), ("noam", "neutre", 0.74)])
    noam surpris "Pourquoi vous avez changé de chambre ?"
    elen inquiet "Il avait peur que quelqu'un revienne frapper à sa porte. Je me suis dit qu'il serait plus tranquille chez moi."
    noam reflexion "Ah. C'était donc ça, votre conversation d'hier soir."
    elen neutre "Ouais. J'ai dormi dans sa chambre, lui dans la mienne."
    lysa inquiet "Mais il est toujours pas arrivé."
    $ showGroup([("nyra", "neutre", 0.22), ("elen", "inquiet", 0.49), ("noam", "neutre", 0.74)])
    nyra raison "On peut aller voir sans lui faire peur. Il a eu assez de monde sur le dos."
    noam neutre "Elen, tu viens avec moi ?"
    elen content "Oui."
    $ showGroup([("lysa", "neutre", 0.22), ("elen", "content", 0.49), ("noam", "neutre", 0.74)])
    lysa neutre "Je viens aussi."
    $ showGroup([("iris", "blase", 0.24), ("elen", "neutre", 0.49), ("noam", "neutre", 0.74)])
    iris blase "Réveillez-le doucement. S'il vous engueule, vous l'aurez mérité."
    $ hideGroup()
    jump _26_0_1_1_0_1_PORTE
# Durée : 2m00 — Total : 2m45.

label _26_0_1_1_0_1_PORTE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("elen", "inquiet", 0.25), ("lysa", "neutre", 0.49), ("noam", "neutre", 0.73)])
    "Elen s'arrête devant sa chambre et frappe."
    elen neutre "Tomas ? C'est Elen. T'es réveillé ?"
    pause 0.5
    lysa reflexion "Frappe plus fort."
    elen inquiet "Tomas ?!"
    play sound "audio/sfx_knock.mp3"
    "Pas de réponse. Elen essaie la poignée."
    elen surpris "C'est fermé."
    noam neutre "De l'intérieur ?"
    elen inquiet "Oui. Il avait dit qu'il fermerait le verrou pour être tranquille."
    noam raison "T'as pas un accès de secours ?"
    elen neutre "Pas quand le verrou intérieur est mis."
    noam inquiet "Tomas ! Ouvre, s'il te plaît !"
    pause 0.7
    lysa inquiet "Ça sent pas bon."
    elen inquiet "Je suis pas retournée dans ma chambre depuis qu'on a échangé. Je lui ai dit bonne nuit et je suis partie."
    noam raison "D'accord. On va chercher Kael et Elias. Et Iris."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE
# Durée : 1m30 — Total : 4m15.

label _26_0_1_1_0_1_DECOUVERTE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "Elias arrive avec Kael. Iris n'a même pas pris le temps d'enfiler sa blouse. Elen recule pour leur laisser de la place."
    $ showGroup([("kael", "reflexion", 0.18), ("elias", "fatigue", 0.42), ("elen", "inquiet", 0.68)])
    kael reflexion "Vous avez essayé le lecteur extérieur ?"
    elen inquiet "Oui ! Trois fois ! Il répond pas."
    elias raison "Si le verrou intérieur est mis, on peut pas ouvrir de dehors."
    elen peur "Alors fais quelque chose !"
    elias inquiet "Je vais le forcer, mais... ça va casser le mécanisme."
    iris colere "Elias, on se fout de la serrure !"
    elias surpris "OK ! Je fais !"
    "Il s'agenouille devant le boîtier. L'outil ripe une première fois."
    elen inquiet "Pourquoi ça marche pas ?"
    elias agace "Parce que c'est pas prévu pour être ouvert comme ça ! Donne-moi dix secondes !"
    "Je regarde la porte. Tomas est peut-être simplement endormi. C'est ce que je me répète pendant qu'Elias s'acharne."
    play sound "audio/sfx_knock.mp3"
    noam inquiet "Tomas ! C'est nous ! Si tu nous entends, réponds, s'il te plaît !"
    "Personne ne répond. Elias se redresse enfin."
    elias neutre "C'est bon. Reculez."
    "Le verrou cède avec un claquement. Il pousse la porte."
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "fatigue", 0.23), ("iris", "inquiet", 0.47), ("noam", "inquiet", 0.72)])
    "Une odeur épouvantable me saute au visage. Je me bouche le nez et regarde autour de moi : des barquettes oubliées, des vêtements au sol, des emballages sous le bureau."
    noam fatigue "Putain, c'est quoi, cette odeur ?"
    elen fatigue "Je... j'avais pas rangé. Désolée..."
    "Puis je vois Tomas."
    stop music fadeout 0.6
    "Il est allongé sur le lit, dans la même tenue qu'hier. Une de ses mains dépasse du drap."
    pause 0.7
    noam inquiet "Tomas ?"
    "Je m'approche. Sa chemise est trempée. Ses cheveux sont collés à son front."
    noam peur "Hé. Tomas, réveille-toi."
    $ showGroup([("iris", "inquiet", 0.24), ("elen", "peur", 0.50), ("noam", "peur", 0.76)])
    elen peur "Il fait quoi ? Pourquoi il bouge pas ?"
    noam panique "Tomas ! Hé, tu m'entends ?!"
    iris determine "Noam, laisse-moi passer !"
    "Elle lui prend le poignet, puis pose deux doigts contre son cou."
    elen inquiet "Alors ?"
    iris determine "Attends."
    pause 0.5
    "Iris se penche près de son visage. Elle ne dit rien."
    elen peur "Iris !"
    iris inquiet "Je trouve pas de pouls."
    noam surpris "Quoi ?"
    iris determine "Il respire pas. Reculez, s'il vous plaît."
    "Elle vérifie encore. J'entends Elen demander quelque chose, mais je n'arrive pas à suivre."
    "Sael arrive et rejoint Iris près du lit. Toutes les deux échangent quelques mots à voix basse."
    $ showGroup([("sael", "triste", 0.21), ("elen", "peur", 0.48), ("noam", "vide", 0.74)])
    elen inquiet "Vous allez le réveiller, hein ?"
    sael triste "Elen..."
    elen peur "Non. Dis pas ça."
    sael triste "Je suis désolée. Il est mort."
    pause 1.0
    elen peur "Non ! Non, tu te trompes ! Il dormait, c'est tout !"
    noam vide "..."
    elen colere "Vous pouvez pas juste le laisser comme ça ! Faites quelque chose !"
    sael inquiet "On a vérifié. Elen, je suis désolée."
    "Elen essaie de s'approcher, mais ses jambes semblent lâcher. Lysa, revenue derrière nous, la retient par les épaules."
    $ showGroup([("lysa", "inquiet", 0.22), ("elen", "triste", 0.49), ("noam", "vide", 0.76)])
    elen triste "Je lui ai donné ma chambre..."
    elen peur "Je voulais juste qu'il soit tranquille. C'est tout."
    "Elle cherche le visage de Tomas derrière nous, comme si elle espérait qu'il allait soudain se redresser."
    pause 0.6
    lysa inquiet "Viens. On sort une minute."
    elen peur "Mais il est là !"
    lysa triste "Je sais. Viens juste avec moi."
    "Elen finit par se laisser entraîner dans le couloir. Je reste devant le lit. Je pourrais compter les secondes qui passent, mais je sais plus depuis combien de temps je suis là."
    "Une main se pose sur mon épaule. C'est Iris."
    $ showGroup([("iris", "fatigue", 0.31), ("noam", "vide", 0.66)])
    iris fatigue "Noam. Tu peux sortir aussi ? J'ai besoin de place."
    noam fatigue "Je lui ai parlé hier."
    iris triste "Je sais."
    noam inquiet "Il était... il allait pas bien, mais il cherchait encore des trucs, il..."
    iris triste "Noam, s'il te plaît. Va t'asseoir."
    "Je sors. Sur le seuil, je croise Nyra qui vient d'arriver."
    $ showGroup([("nyra", "inquiet", 0.30), ("noam", "fatigue", 0.69)])
    nyra inquiet "Qu'est-ce qui s'est passé ?"
    noam fatigue "Tomas est mort."
    nyra peur "..."
    nyra inquiet "Merde."
    "Elle jette un coup d'œil dans la chambre, puis détourne les yeux."
    nyra reflexion "L'odeur est horrible. Il faudrait laisser la porte ouverte pour aérer."
    iris fatigue "Oui... Je veux juste que vous ne touchiez à rien pour l'instant."
    nyra raison "D'accord."
    $ hideGroup()
    jump _26_0_1_1_0_1_APRES_CHOC

label _26_0_1_1_0_1_APRES_CHOC:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "Lysa a installé Elen sur une banquette. Elias est resté près de la porte, les yeux fixés sur son outil."
    $ showGroup([("elen", "triste", 0.20), ("lysa", "inquiet", 0.44), ("noam", "fatigue", 0.69)])
    elen triste "Je lui ai dit qu'il serait tranquille dans ma chambre..."
    lysa inquiet "Elen, arrête. Tu voulais l'aider."
    elen colere "Mais il avait peur ! Il avait peur de dormir tout seul et j'ai juste... je lui ai dit de prendre mon lit !"
    noam fatigue "Tu pouvais pas savoir."
    elen triste "Je sais, je sais... Arrêtez de me dire ça."
    "Je voudrais trouver autre chose. Je n'ai rien."
    pause 0.3
    elen fatigue "Vous allez l'emmener où ?"
    noam neutre "Iris et Sael sont avec lui. Je sais pas encore."
    lysa raison "On va attendre ce qu'elles nous disent."
    "Elen se frotte les yeux. Lysa reste assise sans lui demander de parler."
    "J'entends plusieurs personnes arriver en courant. Julian manque de percuter Kael au tournant du couloir."
    $ showGroup([("julian", "inquiet", 0.24), ("mara", "agace", 0.48), ("noam", "fatigue", 0.73)])
    julian inquiet "C'est vrai ?! Quelqu'un m'a dit qu'il était mort !"
    noam fatigue "Oui."
    julian surpris "Mais... quoi ? Comment ?!"
    mara agace "On sait pas. Il faut arrêter de hurler, on entend rien."
    julian colere "Je hurle pas !"
    mara colere "Tu veux que j'appelle ça comment ?!"
    "Ryn déboule à son tour et essaie de regarder par-dessus nos épaules."
    $ showGroup([("ryn", "inquiet", 0.24), ("kael", "inquiet", 0.48), ("noam", "fatigue", 0.73)])
    ryn inquiet "Vous l'avez trouvé comme ça ? Personne a entendu quelque chose ?"
    kael raison "On a forcé la porte. Le verrou intérieur était engagé."
    ryn inquiet "Vous êtes sûrs que personne d'autre était dans cette chambre ?"
    kael inquiet "On a vérifié, oui."
    ryn agace "Alors pourquoi on le laisse là ?!"
    noam colere "Parce qu'Iris est avec lui ! Tu veux qu'on fasse quoi, Ryn ?!"
    "Ma voix monte toute seule. Ryn se tait. Je me rends compte que j'ai les mains qui tremblent."
    $ showGroup([("elen", "peur", 0.24), ("nyra", "inquiet", 0.48), ("noam", "fatigue", 0.73)])
    elen peur "Mais si c'était moi, normalement ? Si quelqu'un voulait entrer chez moi ?"
    nyra inquiet "Elen, on sait même pas s'il y a eu une agression."
    elen colere "Alors c'est QUOI ? Il est mort dans mon lit !"
    nyra fatigue "Je sais. Je dis juste qu'il faut laisser Iris regarder."
    noam fatigue "On peut pas répondre à ça, Elen. Pas maintenant."
    "Plus personne ne parle pendant quelques secondes. On n'a pas de réponse, et ça ne rassure personne."
    "Je m'assois de l'autre côté du couloir. Personne n'a vraiment envie de retourner à la cafétéria."
    pause 0.5
    "Quand Iris ressort enfin, elle semble aussi épuisée que nous."
    $ showGroup([("iris", "fatigue", 0.23), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.69)])
    iris fatigue "Sael prépare le transfert à l'infirmerie. Je veux photographier quelques éléments avant qu'on bouge le corps."
    noam reflexion "Tu sais comment il est mort ?"
    iris agace "Non. J'ai pas une réponse en dix minutes, Noam."
    noam fatigue "Désolé."
    iris raison "Et je veux que personne ne commence à raconter des choses sur sa mort avant qu'on ait vérifié."
    lysa inquiet "On a le droit d'aider ?"
    iris neutre "Deux personnes. Et pas tout de suite. J'ai besoin de finir."
    iris reflexion "Noam... Tu pourrais m'aider pour les photos ? J'ai besoin qu'on garde une trace de l'état de la chambre avant le transfert."
    noam inquiet "Tu veux que je photographie Tomas ?"
    iris triste "Oui. Si tu peux. Sinon je demanderai à Elias."
    "Je serre ma tablette un moment. Je n'ai aucune envie de faire ça, mais c'est peut-être la dernière fois qu'on pourra vérifier dans quel état on l'a trouvé."
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    "Je cadre les draps et ses vêtements trempés sans m'attarder sur son visage."
    call j26_photograph("j26_photo_tomas", "j26_elen_corps", (0.355, 0.535), 2.1) from _call_j26_tomas_photo
    "Je cadre ensuite les déchets éparpillés sur le sol. Je vérifie le résultat avant de ranger la tablette."
    call j26_photograph("j26_photo_dechets", "j26_elen_corps", (0.67, 0.80), 2.0) from _call_j26_dechets_photo
    "Pour le verrou, Elias me montre les dégâts sur le boîtier du couloir. Il confirme avoir forcé la fermeture intérieure."
    $ investigation_add("j26_tomas_verrou", notify=False)
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Iris reprend sa place auprès de Sael. Je sors en gardant la tablette serrée contre moi. Je n’ai plus envie de regarder ces images."
    $ hideGroup()
    jump _26_0_1_1_0_1_INSPECTION_INTRO


# Catalogue local : salles, actions point-and-click et fiches du dossier.
init 10 python:
    J26A_ROOMS = {
        "dortoir": {
            "title": "DORTOIRS — CHAMBRE D'ELEN",
            "background": "j26_elen_vide",
            "description": "La chambre est sous surveillance. Iris a autorisé quelques examens ciblés.",
            "actions": [
                "flacon",
                "grille"
            ]
        },
        "infirmerie": {
            "title": "INFIRMERIE",
            "background": "infirmerie2",
            "description": "Iris travaille sur les premières constatations médicales.",
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
            "description": "Julian et Nyra sont restés ici après la découverte.",
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
            "description": "Observer et photographier le flacon, sans perturber le travail d'Iris.",
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
            "title": "Parler à Iris",
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
        "j26_photo_flacon_detail": {"category": "preuves", "title": "PHOTO — ÉTIQUETTE DES SOMNIFÈRES", "desc": "Cliché complémentaire du flacon examiné avec Iris.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j26_photo_grille_detail": {"category": "preuves", "title": "PHOTO — FIXATIONS DE L'AÉRATION", "desc": "Cliché complémentaire des attaches de la plaque dans la chambre d'Elen.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j26_photo_flacon": {"category": "preuves", "title": "FLACON DE SOMNIFÈRES PRESQUE VIDE", "desc": "Un flacon presque vide a été retrouvé parmi les affaires de la chambre. Rien ne prouve que Tomas en ait pris.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "j26_elen_flacon"},
        "j26_core_mort": {"category": "evenements", "title": "DÉCOUVERTE DU CORPS", "desc": "Tomas a été retrouvé mort dans la chambre d'Elen, derrière une porte verrouillée de l'intérieur.", "day": "J26", "origin": "DORTOIRS", "status": "CONFIRMÉ", "manual_only": True},
        "j26_core_sudation": {"category": "preuves", "title": "PREMIÈRES CONSTATATIONS", "desc": "Iris et Sael ont constaté l'absence de respiration et une importante sudation. La cause de la mort reste inconnue.", "day": "J26", "origin": "DORTOIRS", "status": "CONFIRMÉ", "manual_only": True},
        "j26_tomas_flacon": {"category": "preuves", "title": "FLACON DE SOMNIFÈRES", "desc": "Un flacon presque vide a été découvert près du lit. Rien ne prouve que Tomas a pris ces comprimés.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_aeration": {"category": "preuves", "title": "GRILLE D'AÉRATION", "desc": "Une plaque empêche physiquement le passage par la grille, mais laisse l'air circuler.", "day": "J26", "origin": "CHAMBRE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_rapport": {"category": "hypotheses", "title": "CAUSE DU DÉCÈS INCERTAINE", "desc": "Iris a constaté une sudation importante et aucune blessure évidente. Elle ne confirme ni suicide ni empoisonnement.", "day": "J26", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_echange": {"category": "evenements", "title": "ÉCHANGE DE CHAMBRES", "desc": "Tomas et Elen ont échangé leurs chambres pour éviter des visiteurs hostiles. Elen nie être revenue chez elle la nuit.", "day": "J26", "origin": "TÉMOIGNAGE D'ELEN", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_sael": {"category": "personnes", "title": "ALIBI DE SAEL", "desc": "Sael dit avoir passé une partie de la soirée à l'infirmerie, sans témoin constant.", "day": "J26", "origin": "TÉMOIGNAGE DE SAEL", "status": "À VÉRIFIER", "manual_only": True},
        "j26_tomas_alibi_julian": {"category": "personnes", "title": "ALIBI DE JULIAN", "desc": "Julian dit avoir été avec Ryn et Mara puis être rentré. Il nie avoir connu l'échange de chambres.", "day": "J26", "origin": "TÉMOIGNAGE DE JULIAN", "status": "À VÉRIFIER", "manual_only": True},
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
    "Plus tard, Iris me laisse entrer quelques minutes. Tomas a été transféré à l'infirmerie. Le lit est vide, mais le drap porte encore la trace de sa présence."
    $ showGroup([("iris", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    iris raison "J'ai pris les photos nécessaires. Si tu veux m'aider, ne déplace rien sans me prévenir."
    noam raison "D'accord."
    iris reflexion "J'ai pas trouvé de blessure extérieure évidente. Et les draps étaient vraiment trempés."
    noam inquiet "Ça veut dire quoi ?"
    iris fatigue "J'en sais rien. Ça peut correspondre à plusieurs causes. Je veux pas te donner une réponse au hasard."
    noam neutre "La porte était fermée de l'intérieur."
    iris raison "Oui. Elias a dû forcer le verrou. C'est noté."
    "Iris a gardé la pièce intacte autant que possible. Je prends une photo de la protection métallique devant la bouche d'aération."
    $ hideGroup()
    call j26_photograph("j26_photo_grille", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j26_grille_photo
    $ showGroup([("iris", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    "Je regarde les vis une dernière fois. Elles sont en place, mais il y a toujours de l'air qui passe."
    iris inquiet "Et Elen ?"
    noam fatigue "Lysa est avec elle."
    iris neutre "Bien. Évite de lui poser trop de questions tout de suite."
    noam reflexion "J'avais envie de comprendre ce qui s'est passé. Mais j'ai pas envie de passer ma journée à leur demander où ils étaient comme si..."
    iris raison "Comme s'ils étaient tous suspects ?"
    noam fatigue "Ouais."
    iris neutre "Alors fais pas ça n'importe comment. Tomas mérite qu'on soit prudents."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE_FLACON

label _26_0_1_1_0_1_DECOUVERTE_FLACON:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    "Avant que je parte, Iris se penche vers les affaires restées près du lit."
    $ showGroup([("iris", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    iris surpris "Attends. C'est quoi, ça ?"
    "Elle sort un petit flacon de médicaments, presque vide."
    noam surpris "C'était là depuis ce matin ?"
    iris reflexion "Je l'avais pas vu. C'est un somnifère."
    noam inquiet "Tu crois qu'il en a pris ?"
    iris raison "Je sais pas. Je vais vérifier, mais je peux pas te dire ça à l'œil."
    "Iris pose un instant le flacon sur la table de chevet, sans toucher au bouchon, pour que je puisse le photographier."
    $ hideGroup()
    scene j26_elen_flacon at adaptive_fullscreen with dissolve
    call j26_photograph("j26_photo_flacon", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_photo
    "Iris me demande de laisser le flacon sur la table de chevet, sans y toucher, jusqu'aux prélèvements."
    $ showGroup([("iris", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    noam fatigue "Tu veux dire qu'il aurait pu... se suicider ?"
    iris fatigue "C'est une hypothèse. Pas une conclusion, Noam. On ne sait ni s'il a pris ces comprimés, ni quand."
    noam inquiet "Mais hier, il avait peur. Il était vraiment mal..."
    iris raison "Et ça ne nous permet pas de décider à sa place de ce qu'il a fait."
    noam fatigue "OK. Je vais prévenir les autres, mais sans dire que c'est sûr."
    $ j26_alt_flacon = True
    $ hideGroup()
    jump _26_0_1_1_0_1_ENQUETE

label _26_0_1_1_0_1_ENQUETE:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je retrouve Nyra et Lysa dans la salle commune. Elles ont commencé à noter les horaires dont on se souvient."
    $ showGroup([("nyra", "neutre", 0.22), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.71)])
    lysa fatigue "Elen a fini par s'endormir un peu. Je préfère qu'on la laisse tranquille."
    nyra raison "On peut commencer par les lieux et les gens qui acceptent de parler. Sans forcer."
    noam reflexion "Et si quelqu'un refuse ?"
    lysa neutre "Il refuse. On n'est pas la police."
    nyra raison "C'est pour ça qu'on devrait limiter les recherches. On a déjà perdu toute la matinée, et Iris a besoin de travailler."
    noam neutre "OK. Cinq vraies actions. Pas plus aujourd'hui."
    lysa reflexion "Tu vas compter ?"
    noam sourire "Si ça peut m'éviter de passer toute la soirée à harceler les autres, oui."
    nyra sourire "D'accord. Et tu notes bien la différence entre un alibi et une simple déclaration."
    "Je sors ma tablette. On pourra se déplacer librement, mais je choisirai les éléments que je veux vraiment approfondir."
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
        "Ma tablette vibre : je n'ai plus de points d'action. Il faut faire le point avec les informations que j'ai."
        jump _26_0_1_1_0_1_BILAN
    jump _26_0_1_1_0_1_PA_ROOM


label _26_0_1_1_0_1_PA_FLACON:
    scene j26_elen_flacon at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "neutre", 0.68)])
    noam reflexion "Iris, le flacon est encore là ?"
    iris neutre "Oui. J'attendais de pouvoir faire des prélèvements propres."
    "Elle me le montre sans me laisser le toucher."
    noam reflexion "Il est presque vide."
    iris raison "Ce qui ne dit rien sur qui l'a vidé, ni quand."
    noam neutre "C'est écrit somnifère."
    iris fatigue "Oui. C'est une piste. Mais on ne sait toujours pas si Tomas l'a avalé."
    noam inquiet "Tu peux savoir s'il en a pris ?"
    iris raison "Je vais essayer. Pour l'instant, je peux pas."
    "Je m'approche pour photographier une nouvelle fois l'étiquette."
    $ hideGroup()
    call investigation_take_manual_photo("j26_photo_flacon_detail", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_detail_photo
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "neutre", 0.68)])
    "Je note le nom. Iris récupère le flacon."
    noam fatigue "Désolé. Je voulais juste..."
    iris neutre "Je sais. Mais je préfère qu'on vérifie avant de raconter quoi que ce soit."
    $ j26_alt_flacon = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_GRILLE:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam reflexion "La grille... Tu te souviens de ce qu'Elias avait installé ?"
    lysa raison "Les protections pour pas que quelqu'un se balade dans les conduits. Tu m'avais raconté."
    "Je décide de reprendre un cliché des fixations pour comparer leur état."
    $ hideGroup()
    call investigation_take_manual_photo("j26_photo_grille_detail", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j26_grille_detail_photo
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    "Aucun des clous ne semble avoir été retiré récemment."
    noam raison "La plaque est toujours fixée."
    lysa neutre "Donc personne a pu passer sans l'enlever."
    noam reflexion "Ouais. Mais regarde, l'air circule encore."
    lysa blase "Heureusement, sinon Elen vivrait dans une boîte de conserve."
    noam neutre "Je sais pas si ça sert à quelque chose. Je préfère le garder."
    lysa raison "Note ce que tu vois, pas ce que t'imagines."
    $ j26_alt_vent = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Le lit sur lequel repose Tomas est dissimulé derrière un rideau. Je m'arrête devant sans oser l'ouvrir."
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "inquiet", 0.68)])
    iris fatigue "Je viens juste de commencer. Tu voulais savoir quoi ?"
    noam raison "Ce qu'on peut dire avec certitude."
    iris reflexion "Il était mort quand je l'ai examiné. Je n'ai pas vu de blessure externe évidente. Il était très humide, ses vêtements aussi."
    noam inquiet "Tu crois qu'il a eu mal ?"
    iris triste "J'en sais rien. Et j'ai pas envie de te dire oui ou non pour te rassurer."
    noam fatigue "OK."
    iris neutre "J'ai encore des analyses à faire. Ne confonds pas « suicide », « empoisonnement » et « cause inconnue ». Pour l'instant, on est au troisième."
    noam raison "Et l'odeur dans la chambre ?"
    iris reflexion "Il y avait des déchets. Ça peut expliquer beaucoup de choses. J'ai eu mal à la tête en entrant, mais j'en tirerai aucune conclusion."
    noam neutre "Tu m'appelles si ça avance ?"
    iris raison "Oui. Mais Noam..."
    noam reflexion "Quoi ?"
    iris fatigue "Laisse-moi travailler un peu, d'accord ?"
    noam neutre "Ouais. Merci."
    $ j26_alt_corps = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_ELEN:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Elen est assise avec une couverture sur les épaules. Lysa m'adresse un regard qui veut clairement dire de ne pas l'embêter."
    $ showGroup([("elen", "triste", 0.23), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.71)])
    noam neutre "Elen... Ça te dérange si je te demande juste un truc ?"
    elen fatigue "C'est pour Tomas ?"
    noam neutre "Ouais. On peut le faire une autre fois."
    elen triste "Non. Vas-y. Je vais pas disparaître si tu me poses une question."
    pause 0.3
    noam reflexion "Pourquoi vous avez échangé les chambres hier ?"
    elen fatigue "Il avait peur que des gens reviennent l'insulter. Il arrêtait pas de regarder derrière lui, même quand on était dans le couloir."
    lysa inquiet "Tu lui as proposé ton lit ?"
    elen triste "Ouais. Je lui ai dit que moi, je m'en foutais qu'on vienne frapper. Qu'au pire, je leur dirais de dégager."
    noam raison "Et après ?"
    elen fatigue "On s'est dit bonne nuit. Je suis allée chez lui. J'ai pas bougé jusqu'au matin."
    noam neutre "Tu sais si quelqu'un a entendu ?"
    elen reflexion "Je sais pas. Il y avait des gens qui passaient, je crois. Je regardais pas."
    noam inquiet "Le flacon qu'on a trouvé... Il était à toi ?"
    elen surpris "Quel flacon ?"
    noam raison "Des médicaments pour dormir."
    elen fatigue "J'en ai peut-être dans ma trousse. J'en prends pas souvent. Je sais pas combien il en restait."
    elen triste "Il avait même pas besoin de mes médicaments. Il voulait juste qu'on le laisse tranquille..."
    "Elle commence à pleurer. Lysa me fait signe d'arrêter."
    noam fatigue "OK. C'est bon. Merci, Elen."
    elen triste "Je suis désolée. Je peux pas..."
    noam neutre "T'as rien à finir. On reparlera plus tard."
    $ j26_alt_elen = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_SAEL:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("sael", "neutre", 0.35), ("noam", "neutre", 0.69)])
    sael reflexion "J'ai entendu que tu poses des questions à tout le monde."
    noam fatigue "Je voudrais surtout savoir ce qu'on a fait hier soir."
    sael raison "J'étais à l'infirmerie une partie de la soirée. J'ai rangé du matériel, puis je suis allée me coucher."
    noam neutre "Quelqu'un peut confirmer ?"
    sael neutre "Iris m'a vue plus tôt. Après, non. Je n'ai pas de témoin pour chaque minute."
    noam raison "Et Ryn ?"
    sael reflexion "Je l'ai croisé dans le couloir. Il avait l'air de mauvaise humeur."
    noam fatigue "Ça, c'est pas nouveau."
    sael neutre "Je ne te donnerai pas un alibi inventé juste parce que tu as besoin d'en avoir un."
    noam raison "C'est pas ce que je te demande."
    sael inquiet "J'espère. Parce qu'aujourd'hui, tout le monde souffre. Ce serait facile de chercher un responsable et de ne plus regarder le reste."
    noam neutre "Je note seulement ce que tu me dis."
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Julian remue son café depuis un moment. Quand je lui demande si je peux m'asseoir, il pose la tasse un peu trop fort."
    $ showGroup([("julian", "agace", 0.35), ("noam", "neutre", 0.70)])
    julian agace "Tu viens me demander si j'ai tué Tomas ?"
    noam reflexion "J'allais te demander où t'étais après le dîner."
    julian colere "Je le savais !"
    noam agace "Mais laisse-moi finir deux secondes !"
    julian fatigue "..."
    noam raison "Je sais que tu t'es disputé avec lui. Tout le monde le sait. Je veux juste savoir ce qu'il s'est passé après."
    julian reflexion "J'étais avec Ryn et Mara dans la salle commune. On a parlé, puis je suis rentré dormir."
    noam neutre "Vers quelle heure ?"
    julian fatigue "J'en sais rien, Noam. J'avais pas de raison de noter l'heure."
    noam raison "Tu savais pour son échange de chambre avec Elen ?"
    julian surpris "Hein ? Quel échange ?"
    noam neutre "Il dormait chez Elen parce qu'il avait peur qu'on vienne le déranger."
    julian triste "..."
    julian fatigue "Putain."
    noam inquiet "Julian ?"
    julian triste "Je l'ai pourri devant tout le monde. Et j'ai même pas réalisé qu'il avait peur de nous."
    noam neutre "Tu pouvais pas savoir ce qui allait arriver."
    julian agace "Arrête. J'ai été un connard avec lui. Mais j'ai pas... enfin, j'ai jamais voulu ça."
    noam fatigue "Je sais pas encore ce qui s'est passé. C'est pour ça que je pose des questions."
    julian triste "Ouais."
    $ j26_alt_julian = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_NYRA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("nyra", "neutre", 0.36), ("noam", "neutre", 0.70)])
    nyra reflexion "Tu as besoin de quelque chose ?"
    noam raison "Je pose les mêmes questions à tout le monde. Hier soir, après qu'on s'est croisés aux dortoirs..."
    nyra neutre "Je suis allée dans ma chambre."
    noam reflexion "Et après ?"
    nyra sourire "J'ai dormi, Noam."
    noam neutre "Tu peux comprendre pourquoi je demande."
    nyra raison "Oui. T'as même pas besoin de te justifier."
    noam reflexion "Tu savais que Tomas et Elen avaient échangé ?"
    nyra hesitation "Je savais qu'elle essayait de l'aider, mais j'ai pas entendu ce qu'ils avaient décidé."
    noam neutre "Tu n'es pas retournée dans les couloirs ?"
    nyra raison "Non. Et je sais bien que j'ai pas de témoin pour le prouver."
    noam fatigue "Je déteste faire ça."
    nyra neutre "Alors fais-le correctement, et on évitera de se raconter n'importe quoi sur Tomas."
    "Elle reprend sa tasse. Je m'éloigne avec une réponse simple et aucun moyen de la vérifier."
    $ j26_alt_nyra = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    $ showGroup([("kael", "calme", 0.21), ("elias", "fatigue", 0.45), ("noam", "neutre", 0.70)])
    noam raison "Je voudrais comprendre comment vous avez ouvert la chambre."
    elias reflexion "J'ai forcé le verrou intérieur avec l'outil. Tu m'as vu."
    noam neutre "Oui. Avant ça, il était bien engagé ?"
    elias raison "Oui. Le lecteur extérieur était bloqué. Ça arrive quand tu verrouilles depuis le dedans."
    kael reflexion "Ça n'empêche pas de passer par une autre entrée, mais les accès aux chambres ont tous des protections."
    noam raison "Les conduits aussi ?"
    kael neutre "Oui. Elias a posé les plaques. Tu peux toujours faire circuler l'air, pas une personne."
    elias agace "Heureusement, on allait pas priver tout le monde d'oxygène."
    noam reflexion "Et hier soir, vous étiez où ?"
    kael raison "Avec Elias pour finir des réparations. On s'est quittés après."
    elias fatigue "On a fermé l'atelier, puis je suis rentré. J'ai pas croisé Tomas."
    noam raison "Vous avez enregistré quelque chose ?"
    kael reflexion "Il y a un journal des accès, mais c'est pas une caméra. Je regarderai si ça peut aider."
    noam neutre "Merci."
    $ j26_alt_verrou = True
    $ j26_alt_kael = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_RYN:
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Ryn frappe dans un sac sans vraiment y mettre de force. Il s'arrête en me voyant."
    $ showGroup([("ryn", "agace", 0.35), ("noam", "neutre", 0.69)])
    ryn agace "Quoi ?"
    noam raison "Tu étais où hier soir après la cafétéria ?"
    ryn colere "Ah. Ça y est. On fait le tour des suspects."
    noam fatigue "Je te demande juste où tu étais."
    ryn agace "Avec Julian et Mara, dans la salle commune. Ensuite je suis allé dormir."
    noam neutre "T'as parlé à Tomas après ?"
    ryn colere "Non. Et heureusement, parce que je lui aurais encore dit des trucs que je regretterais aujourd'hui."
    pause 0.3
    ryn fatigue "Écoute... Je lui en voulais pour le vote, oui. Mais je voulais qu'il arrête de nous mettre dans la merde. Pas qu'il crève."
    noam raison "Je sais."
    ryn agace "Non, tu sais rien. Ni toi ni moi. Vous savez même pas comment il est mort."
    noam fatigue "C'est justement ça qui me fait peur."
    ryn triste "Ouais... Moi aussi."
    $ j26_alt_ryn = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_NOTES:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Le terminal que Tomas utilisait est encore ouvert à une page technique. Je me souviens de sa façon de reculer sa chaise dès qu'il trouvait une incohérence."
    noam reflexion "Keyper-IIB..."
    "Les lignes indiquent des quotas et des effectifs, toujours sans expliquer à quoi correspondent les unités."
    "Je ne trouve aucun nouveau dossier, mais l'historique montre qu'il consultait encore ces documents hier."
    noam fatigue "Il essayait encore de comprendre..."
    "Je prends une copie du titre et de la date, sans toucher au reste. Rien ne permet d'affirmer qu'il a été tué à cause de ces recherches."
    return

label _26_0_1_1_0_1_PA_CONSOLE:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "La salle d'observation est vide. Je retrouve le pupitre près duquel Tomas m'avait montré la carte de Keyper."
    "Je regarde l'historique de la console : rien d'inhabituel. Les derniers réglages datent de sa visite."
    "Un souvenir me revient. Il tenait un petit appareil métallique, puis l'avait reposé quand je suis arrivé."
    noam reflexion "C'était quoi, déjà, ce truc... ?"
    "Je cherche du regard le boîtier, mais je ne le reconnais pas parmi les outils posés ici. Je préfère ne pas tirer de conclusion."
    noam fatigue "Je me souviens même pas de sa forme exacte."
    return


label _26_0_1_1_0_1_BILAN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    $ current_period = "Soir"
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Le temps a passé plus vite que je ne pensais. J'ai pris quelques notes, parlé à des gens et, surtout, interrompu beaucoup de personnes qui auraient préféré qu'on les laisse en paix."
    $ showGroup([("lysa", "fatigue", 0.21), ("nyra", "neutre", 0.46), ("noam", "fatigue", 0.70)])
    lysa reflexion "Alors ?"
    noam fatigue "J'ai pas beaucoup de choses certaines."
    nyra raison "C'est déjà bien de s'en rendre compte."
    if "iris" in investigation_pa_completed:
        noam raison "Iris ne peut pas confirmer la cause. Elle veut encore faire des analyses."
        lysa neutre "Au moins, on ne va pas raconter que c'est forcément un suicide."
    else:
        noam reflexion "Iris a besoin de temps. On ne sait toujours pas comment il est mort."
    if "flacon" in investigation_pa_completed:
        lysa reflexion "Et ce flacon ?"
        noam raison "Presque vide, mais on ne sait pas s'il a avalé ce qu'il y avait dedans."
    if "elen" in investigation_pa_completed:
        noam raison "Elen confirme qu'ils ont échangé leurs chambres. Elle dit ne pas être ressortie de celle de Tomas."
        lysa inquiet "Elle a vraiment pas besoin qu'on la questionne encore ce soir."
    if "julian" in investigation_pa_completed:
        noam neutre "Julian était avec Ryn et Mara. Il n'avait pas entendu parler de l'échange."
    if "ryn" in investigation_pa_completed:
        noam neutre "Ryn dit la même chose pour leur soirée. Il était furieux, mais ça fait pas de lui un meurtrier."
    if "nyra" in investigation_pa_completed:
        noam reflexion "Nyra, tu m'as dit que t'étais allée te coucher après qu'on s'est croisés."
        nyra neutre "Oui. Et je peux pas le prouver davantage."
    if "kael" in investigation_pa_completed:
        noam raison "Kael et Elias ont confirmé le verrou. Et le passage physique par les grilles était bloqué."
    if "grille" in investigation_pa_completed:
        noam reflexion "J'ai regardé la grille. La plaque ne laisse passer personne, mais l'air circule."
        nyra neutre "Ça ne prouve rien sur ce qui s'est passé. Mais garde la photo."
    if "notes" in investigation_pa_completed or "console" in investigation_pa_completed:
        noam fatigue "Tomas travaillait encore sur ses recherches. J'ai du mal à croire qu'il pensait tout arrêter hier."
        lysa raison "Noam, ça veut rien dire sur son état d'esprit. On peut travailler et aller très mal."
        noam neutre "Je sais."
    if investigation_pa_remaining > 0:
        lysa reflexion "T'as gardé des pistes de côté ?"
        noam raison "Oui. J'ai pas voulu déranger tout le monde aujourd'hui."
        nyra raison "On aura le temps demain. C'est mieux que de tirer des conclusions en forçant les gens à parler."
    else:
        lysa fatigue "Et t'as plus l'énergie de continuer."
        noam fatigue "Franchement, non."
    pause 0.4
    lysa triste "Je me suis engueulée avec Tomas la semaine dernière parce qu'il avait déplacé mon plateau. C'est débile, mais c'est à ça que je pense."
    noam inquiet "Lysa..."
    lysa fatigue "Non, laisse. J'ai pas envie de pleurer maintenant."
    nyra reflexion "On a une réunion. Il faut leur dire ce qu'on sait, et ce qu'on ne sait pas."
    noam raison "D'accord. Mais pas un procès."
    $ hideGroup()
    jump _26_0_1_1_0_1_REUNION

label _26_0_1_1_0_1_REUNION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "La place de Tomas est vide. J'ai beau le savoir, je regarde quand même sa chaise avant de m'asseoir."
    $ showGroup([("julian", "fatigue", 0.20), ("elen", "triste", 0.46), ("noam", "fatigue", 0.73)])
    julian reflexion "On est tous là ?"
    elen fatigue "Pas tous."
    julian triste "..."
    julian fatigue "Oui. Pardon."
    "Personne ne sait comment commencer. Iris finit par prendre la parole."
    $ showGroup([("iris", "fatigue", 0.23), ("elen", "triste", 0.49), ("noam", "fatigue", 0.74)])
    iris raison "Je vais le dire clairement. Pour l'instant, je ne peux pas déterminer comment Tomas est mort."
    elen inquiet "Même avec le flacon qu'on a trouvé ?"
    iris raison "Ça ne prouve rien. Je veux continuer les analyses. S'il vous plaît, arrêtez de parler comme si on avait déjà une réponse."
    elen triste "D'accord."
    elen inquiet "Et ma chambre ? Au début, je me suis demandé si quelqu'un m'en voulait à moi."
    noam raison "La porte était verrouillée. On a pas de preuve que quelqu'un soit entré."
    iris fatigue "Et on n'a pas de preuve qu'il y ait eu une agression. Je veux vraiment que vous gardiez ça en tête."
    elen triste "Oui. Je sais."
    $ showGroup([("julian", "fatigue", 0.20), ("ryn", "agace", 0.45), ("noam", "neutre", 0.72)])
    ryn reflexion "Mais hier, il allait vraiment mal. On l'a tous vu."
    julian fatigue "Oui. Et je lui ai crié dessus."
    ryn agace "Moi aussi, j'étais en colère. Ça veut pas dire qu'on l'a tué !"
    noam raison "Personne ne dit ça. On essaie juste de comprendre."
    julian triste "J'arrête pas de penser à la dernière fois que je lui ai parlé. Je lui ai même pas demandé comment il allait."
    ryn fatigue "Ouais..."
    if "julian" in investigation_pa_completed or "ryn" in investigation_pa_completed:
        noam neutre "J'ai parlé à certains d'entre vous. Vos déclarations ne suffisent pas à construire une chronologie certaine."
        julian reflexion "C'est-à-dire ?"
        noam raison "Ça veut dire qu'on ne sait pas. Pas que quelqu'un ment."
    $ showGroup([("sael", "neutre", 0.21), ("nyra", "neutre", 0.47), ("noam", "neutre", 0.73)])
    sael raison "La mort de Tomas n'est pas une raison pour nous accuser mutuellement au hasard."
    nyra neutre "On devrait attendre le rapport d'Iris et garder les éléments qu'on a trouvés. Rien de plus pour ce soir."
    noam raison "Je suis d'accord."
    if "flacon" in investigation_pa_completed:
        noam neutre "Le flacon ne démontre pas le suicide."
    if "kael" in investigation_pa_completed:
        noam raison "La porte était verrouillée. Mais ça n'explique pas tout."
    if "elen" in investigation_pa_completed:
        noam raison "Et Tomas avait échangé sa chambre pour être plus tranquille. Elen ne pouvait pas prévoir ce qui allait se passer."
    $ showGroup([("julian", "reflexion", 0.22), ("elen", "triste", 0.48), ("noam", "fatigue", 0.73)])
    julian reflexion "Il reste le vote de demain."
    elen colere "Non. On va pas faire ça."
    julian inquiet "Je sais, mais Kami attend une décision. Et si on ne dit rien..."
    elen colere "Tomas est mort ce matin, Julian ! Tu veux qu'on s'assoit là demain comme si on avait juste perdu une chaise ?!"
    julian fatigue "Non ! Je veux juste pas qu'elle nous punisse encore pour avoir laissé tomber un vote !"
    noam raison "Alors on lui dit ensemble. Pas de vote demain."
    elen triste "Moi, je serai pas là."
    $ showGroup([("lysa", "neutre", 0.21), ("mara", "fatigue", 0.47), ("noam", "neutre", 0.73)])
    lysa neutre "Moi non plus."
    mara fatigue "Pareil. Franchement, qu'elle se débrouille."
    "Les autres acquiescent un à un. Julian finit par baisser les yeux."
    $ showGroup([("julian", "fatigue", 0.21), ("elen", "triste", 0.47), ("noam", "neutre", 0.72)])
    julian fatigue "Bon. D'accord. Mais on assume tous, alors."
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
    $ showGroup([("elen", "triste", 0.26), ("iris", "fatigue", 0.50), ("noam", "fatigue", 0.75)])
    elen colere "Elle me dégoûte."
    iris agace "Ouais. Moi aussi."
    noam fatigue "On rentre."
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
    "Je regarde les arguments obtenus aujourd'hui. Aucun ne dit avec certitude ce qui lui est arrivé."
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
    "Demain, je voudrais retourner dans sa chambre. Juste voir ce qu'il a laissé. Peut-être que ça m'aidera à comprendre ce qu'il essayait de faire."
    "J'éteins l'écran."
    stop music fadeout 1.0
    call end_day("27", sleeping=True) from _call_j26_alt_end_day_27
    jump _27_0_1_1_0_1_REVEIL
