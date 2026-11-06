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
    "Je reste un moment allongé, les yeux ouverts. Hier soir, Tomas n'arrivait même plus à traverser un couloir sans tomber sur quelqu'un qui lui en voulait."
    "Sur ma tablette, le rappel du vote de demain s'affiche au-dessus des messages d'hier. Je le fais disparaître d'un geste."
    think "J'espère au moins qu'il a pu dormir."
    noam fatigue "Bon. Faut manger."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j26_alt_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _26_0_1_1_0_1_CAFETERIA
# Durée : 45 s — Total : 45 s.

label _26_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j26_alt_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    $ showGroup([("julian", "neutre", 0.23), ("iris", "fatigue", 0.48), ("mara", "taquin", 0.74)])
    julian reflexion "Non mais vous l'avez lu, le texte de demain ?"
    iris fatigue "Julian, je viens d'arriver."
    mara sourire "Y a un article qui interdit de parler avant le café ?"
    julian agace "Ah, très drôle. Je vous pose une question, c'est tout."
    $ showGroup([("elen", "fatigue", 0.23), ("lysa", "blase", 0.48), ("noam", "neutre", 0.74)])
    noam neutre "Salut."
    elen sourire "Salut, Noam !"
    lysa reflexion "Tomas a déjà mangé ?"
    $ showGroup([("julian", "fatigue", 0.24), ("elen", "fatigue", 0.49), ("noam", "neutre", 0.74)])
    julian fatigue "J'en sais rien. Il a peut-être pas envie de nous voir."
    elen reflexion "Non, il dort sûrement. Il était crevé hier."
    $ showGroup([("lysa", "inquiet", 0.24), ("elen", "fatigue", 0.49), ("noam", "neutre", 0.74)])
    lysa inquiet "Tomas ? Celui qui vient nous réveiller parce qu'on est en retard de deux minutes ?"
    elen neutre "Il était vraiment pas bien. Je lui ai proposé ma chambre, hier."
    $ showGroup([("mara", "taquin", 0.22), ("elen", "neutre", 0.49), ("noam", "neutre", 0.74)])
    mara taquin "Attends. Vous avez dormi ensemble ?"
    elen colere "Mais non ! On a échangé, c'est tout !"
    mara rire "Oh, ça va."
    $ showGroup([("lysa", "inquiet", 0.22), ("elen", "inquiet", 0.49), ("noam", "neutre", 0.74)])
    noam surpris "Pourquoi ?"
    elen inquiet "Il voulait plus rester chez lui. Il arrêtait pas de regarder la porte, après les histoires d'hier. Alors j'ai dit qu'il pouvait prendre ma chambre."
    noam reflexion "C'est de ça que vous parliez dans le couloir..."
    elen neutre "Ouais. Il devait juste dormir et venir manger avec nous. Je lui ai même dit de pas oublier son réveil."
    lysa inquiet "Bah, allons voir. Ça fait un moment, là."
    $ showGroup([("nyra", "neutre", 0.22), ("elen", "inquiet", 0.49), ("noam", "neutre", 0.74)])
    nyra raison "Oui. Mais évitez de débarquer à six. Il a déjà assez la tête à l'envers."
    noam neutre "Elen, on y va ?"
    elen content "Ouais, j'arrive."
    $ showGroup([("lysa", "neutre", 0.22), ("elen", "content", 0.49), ("noam", "neutre", 0.74)])
    lysa neutre "Je viens. J'ai laissé mon café, alors il a intérêt à être debout."
    $ showGroup([("iris", "blase", 0.24), ("elen", "neutre", 0.49), ("noam", "neutre", 0.74)])
    iris blase "Dites-lui que son petit-déjeuner sera froid. Il déteste ça."
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
    noam raison "Elen, recule. Je vais chercher Elias. Et Iris."
    elen inquiet "Pourquoi Iris ?"
    noam fatigue "Parce que je préfère qu'elle soit là."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE
# Durée : 1m30 — Total : 4m15.

label _26_0_1_1_0_1_DECOUVERTE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "Elias arrive avec Kael, sa boîte à outils à moitié ouverte. Iris les suit, encore en tenue de repos. Personne ne lui a expliqué pourquoi on l'avait appelée."
    $ showGroup([("kael", "reflexion", 0.18), ("elias", "fatigue", 0.42), ("elen", "inquiet", 0.68)])
    kael reflexion "Il a mis le verrou intérieur ?"
    elen inquiet "Oui. Enfin, c'est ce qu'il m'a dit hier. Vous pouvez ouvrir ?"
    elias raison "Faut passer par le boîtier. Je vais essayer."
    elen peur "Mais dépêche-toi !"
    elias inquiet "Je fais ce que je peux, Elen."
    iris colere "Elias, pousse-toi un peu, je veux être devant quand ça s'ouvre."
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
    $ showGroup([("elen", "fatigue", 0.23), ("iris", "inquiet", 0.47), ("noam", "inquiet", 0.72)])
    "L'air est lourd. Il y a une odeur aigre, des barquettes ouvertes au pied du lit et des vêtements partout. Je commence à chercher Tomas du regard, puis j'arrête de regarder le reste."
    noam fatigue "Oh, merde..."
    elen fatigue "J'avais laissé des trucs partout, je..."
    "Il est allongé sur le dos, habillé comme hier, la main pendant au bord du matelas."
    stop music fadeout 0.6
    pause 0.7
    noam inquiet "Tomas ?"
    "Je lui touche l'épaule. Son t-shirt est trempé et ses cheveux collent à son front."
    noam peur "Hé... c'est pas drôle. Tomas ?"
    $ showGroup([("iris", "inquiet", 0.24), ("elen", "peur", 0.50), ("noam", "peur", 0.76)])
    elen peur "Pourquoi il a pas enlevé sa veste ? Tomas, t'as trop chaud ?"
    noam panique "Réveille-toi !"
    iris determine "Noam. Pousse-toi."
    "Elle se penche sur lui, cherche son pouls, puis vérifie sa respiration. Je me retrouve derrière elle sans me souvenir d'avoir bougé."
    elen inquiet "Iris ?"
    iris determine "Attends."
    pause 0.5
    "Iris vérifie une seconde fois. Elle a cessé de nous regarder."
    elen peur "Dis quelque chose !"
    iris inquiet "Je sens rien..."
    noam surpris "Quoi ?"
    iris determine "Noam, recule. S'il te plaît."
    "Elle vérifie encore. J'entends Elen demander quelque chose, mais je n'arrive pas à suivre."
    "Sael arrive et rejoint Iris près du lit. Toutes les deux échangent quelques mots à voix basse."
    $ showGroup([("sael", "triste", 0.21), ("elen", "peur", 0.48), ("noam", "vide", 0.74)])
    elen inquiet "Vous faites quoi ? Pourquoi vous lui parlez pas ?"
    sael triste "Elen, viens avec moi."
    elen peur "Non. Non, attends. Iris, t'as pas fini, hein ?"
    "Iris ne répond pas tout de suite. Sael baisse les yeux."
    sael triste "Elen... Tomas est mort."
    pause 1.0
    elen peur "Non. Attends. Tu peux pas savoir aussi vite."
    noam vide "..."
    elen colere "Mais essayez encore ! Vous avez essayé quoi, là ?!"
    sael inquiet "On a vérifié, Elen. Je suis désolée."
    "Elen avance vers le lit comme pour refaire elle-même ce qu'Iris vient de faire, mais Lysa la rattrape avant qu'elle trébuche."
    $ showGroup([("lysa", "inquiet", 0.22), ("elen", "triste", 0.49), ("noam", "vide", 0.76)])
    elen triste "Il a même pas défait le lit..."
    elen peur "Je lui avais dit qu'il pouvait prendre des affaires dans l'armoire s'il voulait."
    "Elle regarde Tomas, puis sa propre main, qui tient encore la carte d'accès de sa chambre."
    pause 0.6
    lysa inquiet "Viens, Elen. Viens dans le couloir."
    elen peur "Mais il va être tout seul."
    lysa triste "Iris est avec lui. Allez, viens."
    "Elen finit par se laisser entraîner dans le couloir. Je reste devant le lit. Je pourrais compter les secondes qui passent, mais je sais plus depuis combien de temps je suis là."
    "Une main se pose sur mon épaule. C'est Iris."
    $ showGroup([("iris", "fatigue", 0.31), ("noam", "vide", 0.66)])
    iris fatigue "Noam. Tu peux sortir ? J'ai besoin que tu me laisses travailler."
    noam fatigue "Je lui ai parlé hier."
    iris triste "Je sais."
    noam inquiet "Il cherchait encore ce truc sur Keyper. Il m'en parlait, il..."
    iris triste "Je sais, Noam. Écoute... va t'asseoir un peu. Je viens te voir après."
    "Je sors. Sur le seuil, je croise Nyra qui vient d'arriver."
    $ showGroup([("nyra", "inquiet", 0.30), ("noam", "fatigue", 0.69)])
    nyra inquiet "C'est Tomas ? Qu'est-ce qu'il a ?"
    noam fatigue "Il est mort."
    nyra peur "..."
    nyra inquiet "Oh, merde."
    "Elle regarde derrière moi. Je crois qu'elle va entrer, mais elle s'arrête sur le seuil."
    nyra reflexion "Ça sent... vous devriez peut-être ouvrir un peu."
    iris fatigue "Pas tout de suite. Laissez-moi finir ici."
    nyra raison "Oui. Pardon."
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
    $ showGroup([("julian", "inquiet", 0.24), ("mara", "agace", 0.48), ("noam", "fatigue", 0.73)])
    julian inquiet "Noam ! C'est quoi cette histoire ? On m'a dit que Tomas..."
    noam fatigue "C'est vrai."
    julian surpris "Non. Attends. Tu l'as vu ?"
    mara agace "Julian, on vient de te dire oui."
    julian colere "Je te parle pas, Mara !"
    mara colere "Moi non plus j'ai pas envie de te parler, crois-moi !"
    "Ryn arrive derrière eux. Il a dû courir ; il respire encore fort."
    $ showGroup([("ryn", "inquiet", 0.24), ("kael", "inquiet", 0.48), ("noam", "fatigue", 0.73)])
    ryn inquiet "Il s'est passé quoi ? Il est tombé ?"
    kael raison "On sait juste qu'on a trouvé la porte verrouillée."
    ryn inquiet "Et personne a entendu un bruit ? Même pas Elen ?"
    kael inquiet "Elle a dormi dans sa chambre à lui. On l'a déjà dit."
    ryn agace "Arrêtez de me répondre comme si j'étais con !"
    noam colere "Alors arrête de gueuler sur tout le monde ! Iris essaie de bosser !"
    "Ryn ouvre la bouche, prêt à me répondre. Il regarde mes mains, qui tremblent tellement que j'ai dû les serrer dans mes poches, et se tait."
    $ showGroup([("elen", "peur", 0.24), ("nyra", "inquiet", 0.48), ("noam", "fatigue", 0.73)])
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
    "Quand Iris ressort enfin, elle semble aussi épuisée que nous."
    $ showGroup([("iris", "fatigue", 0.23), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.69)])
    iris fatigue "Sael va l'emmener à l'infirmerie. Avant, il faut que je garde des images de la chambre."
    noam reflexion "Iris... il est mort de quoi ?"
    iris agace "J'en sais rien, Noam !"
    "Elle se passe une main sur le visage. Je n'avais encore jamais entendu sa voix dérailler comme ça."
    iris fatigue "Pardon. J'en sais rien. Et je peux pas le regarder cinq minutes et te sortir une cause."
    noam fatigue "Ouais."
    lysa inquiet "On peut faire quelque chose ?"
    iris neutre "Vous pouvez déjà empêcher les autres de rentrer. J'ai besoin qu'on touche plus à rien."
    "Elle hésite, puis se tourne vers moi."
    iris reflexion "Noam, t'as ta tablette ?"
    noam inquiet "Ouais... pourquoi ?"
    iris triste "Il faut photographier Tomas. Les draps, ses vêtements. Je peux demander à Elias, si tu veux."
    "Je regarde la tablette dans ma main. Hier encore, je m'en servais pour répondre à ses messages. Je finis par hocher la tête."
    noam fatigue "Non. Je vais le faire."
    scene j26_elen_corps at adaptive_fullscreen with dissolve
    "Je lève la tablette vers le lit. Je dois recommencer deux fois avant de réussir à garder les mains assez stables pour cadrer Tomas."
    call j26_photograph("j26_photo_tomas", "j26_elen_corps", (0.355, 0.535), 2.1) from _call_j26_tomas_photo
    "Iris me demande aussi de garder une image du sol. Je me concentre sur les emballages, simplement pour ne plus avoir le lit en face de moi."
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
    "Quand Iris me laisse revenir, le lit est vide. Je savais qu'ils avaient emmené Tomas, mais voir l'oreiller sans sa tête me fait quand même quelque chose."
    $ showGroup([("iris", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    iris raison "Tu peux regarder, mais touche pas aux affaires. J'ai pas fini ici."
    noam raison "Ouais."
    "Elle s'arrête devant le drap roulé en boule."
    iris reflexion "J'ai pas vu de blessure. Rien qui explique ce qu'on a trouvé."
    noam inquiet "Et il était trempé. Tu crois que..."
    iris fatigue "Je sais, j'ai vu. J'en reviens aussi à ça, mais j'ai rien de sûr."
    noam neutre "Même avec la porte fermée ?"
    iris raison "Une porte fermée, ça nous dit pas pourquoi quelqu'un meurt, Noam."
    "Je regarde la tôle fixée devant l'aération. Iris me laisse la photographier sans toucher aux attaches."
    $ hideGroup()
    call j26_photograph("j26_photo_grille", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j26_grille_photo
    $ showGroup([("iris", "fatigue", 0.27), ("noam", "inquiet", 0.69)])
    "Les clous ont l'air d'être en place. En approchant la main, je sens quand même un filet d'air."
    iris inquiet "Lysa est avec Elen ?"
    noam fatigue "Ouais. Elle a réussi à la faire dormir un peu."
    iris neutre "Tant mieux."
    "Je baisse la tablette. Ça ne change rien à l'image que j'ai du lit, tout à l'heure."
    noam reflexion "Je vais demander aux autres ce qu'ils faisaient hier. Je sais même pas comment m'y prendre."
    iris raison "Ils vont mal le prendre."
    noam fatigue "Je sais."
    iris fatigue "Moi aussi, je le prendrais mal. Mais si tu dois le faire, évite Elen pour l'instant. Elle vient de perdre quelqu'un dans son propre lit."
    $ hideGroup()
    jump _26_0_1_1_0_1_DECOUVERTE_FLACON

label _26_0_1_1_0_1_DECOUVERTE_FLACON:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    "Avant que je parte, Iris se penche vers les affaires restées près du lit."
    $ showGroup([("iris", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    iris surpris "Attends, là... C'est quoi ?"
    "Elle se baisse derrière la table de chevet et ressort un petit flacon. Il ne reste que quelques comprimés au fond."
    noam surpris "C'était là ? On l'avait même pas vu."
    iris reflexion "Ouais. Attends que je lise."
    "Elle tourne le flacon sous la lumière de la lampe."
    iris reflexion "C'est pour dormir."
    noam inquiet "Tomas en prenait ?"
    iris raison "J'en sais rien. Et c'est même pas dit que ce soit à lui."
    "Elle le pose sur la table, à l'écart des autres objets."
    iris fatigue "Prends une photo avant que je le range."
    $ hideGroup()
    scene j26_elen_flacon at adaptive_fullscreen with dissolve
    call j26_photograph("j26_photo_flacon", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_photo
    "Iris me demande de laisser le flacon sur la table de chevet, sans y toucher, jusqu'aux prélèvements."
    $ showGroup([("iris", "reflexion", 0.33), ("noam", "inquiet", 0.69)])
    noam fatigue "Tu penses qu'il aurait pu... en prendre trop ?"
    iris fatigue "Noam, regarde-moi. Je sais pas s'il en a pris un seul."
    noam inquiet "Ouais, mais hier soir, il était vraiment pas bien..."
    iris raison "Je sais. Ça m'a pas échappé."
    "Elle prend le flacon entre deux doigts, hésite à le manipuler, puis le repose exactement au même endroit."
    iris fatigue "Faut que je vérifie. Pour l'instant, on dit rien."
    noam fatigue "D'accord. Je préfère attendre aussi."
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
    lysa reflexion "Cinq trucs. Tu choisis cinq trucs à vérifier, après tu t'arrêtes. Sinon on te reverra demain matin avec des cernes jusqu'au menton."
    noam sourire "Tu comptes ça comme un conseil médical ?"
    lysa fatigue "Comme une menace."
    "Je bloque cinq créneaux sur la tablette. Au moins, je saurai quand m'arrêter, même si je ne trouve rien."
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
    noam reflexion "Tu l'as toujours pas pris ?"
    iris neutre "Je voulais finir les prélèvements avant. J'ai besoin que tu touches à rien."
    "Elle me montre le flacon du bout du doigt, sans le déplacer."
    noam reflexion "Il en reste presque pas..."
    iris raison "Ouais. Mais j'ai aucune idée de ce qu'il y avait dedans hier."
    noam inquiet "Tu vas pouvoir vérifier si Tomas en a pris ?"
    iris fatigue "Je vais essayer. Je peux pas te promettre une réponse aujourd'hui."
    "Elle me laisse refaire une photo de l'étiquette, de plus près."
    $ hideGroup()
    call investigation_take_manual_photo("j26_photo_flacon_detail", "j26_elen_flacon", (0.14, 0.52), 3.0) from _call_j26_flacon_detail_photo
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "neutre", 0.68)])
    "Je note le nom. Iris glisse le flacon dans un sachet et écrit quelque chose dessus."
    noam fatigue "Je voulais juste être sûr que..."
    iris neutre "Je sais. Moi aussi, je voudrais être sûre."
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
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Le lit sur lequel repose Tomas est dissimulé derrière un rideau. Je m'arrête devant sans oser l'ouvrir."
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "inquiet", 0.68)])
    iris fatigue "Si c'est pour me demander si j'ai trouvé la cause, non."
    noam raison "Je voulais juste... Il y a quelque chose qui te paraît bizarre ?"
    "Iris regarde le rideau derrière elle, puis se tourne de nouveau vers moi."
    iris reflexion "Il avait pas de blessure visible. Et ses vêtements étaient complètement trempés. Tu l'as vu aussi."
    noam inquiet "Tu crois qu'il a eu mal ?"
    iris triste "Je peux pas savoir."
    noam fatigue "D'accord."
    iris neutre "Ça m'énerve de pas pouvoir te dire autre chose. Mais je vais pas inventer."
    noam raison "Et cette odeur, dans la chambre ?"
    iris reflexion "Il y avait tellement de nourriture qui traînait... J'en sais rien. J'ai eu mal au crâne en entrant, mais ça veut peut-être rien dire."
    noam neutre "Tu me préviens quand t'as quelque chose ?"
    iris raison "Oui."
    "Elle retourne vers son plan de travail, puis se ravise."
    iris fatigue "Noam... t'as le droit d'être là, mais évite de regarder derrière le rideau, d'accord ?"
    noam neutre "Ouais. Je vais te laisser."
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
    pause 0.3
    noam reflexion "Hier, quand tu lui as proposé ta chambre... il avait dit quoi ?"
    elen fatigue "Pas grand-chose. Il a demandé si j'étais sûre. Deux fois."
    lysa inquiet "Et toi ?"
    elen triste "Je lui ai dit que j'avais pas peur d'une bande d'idiots qui tapent aux portes. Il a rigolé un peu, même."
    "Elle tire sur le bord de la couverture."
    noam raison "Après, vous avez fait quoi ?"
    elen fatigue "Rien. On s'est souhaité bonne nuit. Moi, je suis allée dans sa chambre, et j'en ai pas bougé."
    noam neutre "Vous étiez seuls quand vous en avez parlé ?"
    elen reflexion "Je sais pas. On était dans le couloir. Des gens passaient, je crois. Pourquoi ?"
    noam inquiet "Je me demandais juste qui était au courant."
    elen fatigue "Tu penses que quelqu'un a attendu qu'il aille dans ma chambre ?"
    noam fatigue "J'en sais rien, Elen."
    "Lysa me lance un regard noir. Je m'en veux aussitôt de ne pas avoir arrêté plus tôt."
    noam inquiet "Le petit flacon qu'Iris a trouvé, c'était à toi ?"
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
    sael raison "À l'infirmerie au début. Iris m'a vue. Après, j'ai fermé et je suis allée me coucher."
    noam neutre "Toute seule ?"
    sael neutre "Oui."
    "Elle repose lentement le linge qu'elle était en train de plier."
    sael reflexion "Tu veux savoir si j'ai croisé quelqu'un ?"
    noam raison "Aussi. Ryn, par exemple."
    sael reflexion "Je l'ai vu dans le couloir. Il râlait contre le vote. Comme d'habitude."
    noam fatigue "Ouais..."
    sael neutre "Écoute. J'ai rien à te cacher, mais si tu commences à demander à chacun de prouver qu'il dormait, ça va très mal finir."
    noam raison "Je sais. Je cherche juste..."
    sael inquiet "Je sais ce que tu cherches. Fais attention aux gens pendant que tu cherches, d'accord ?"
    noam neutre "Ouais."
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
    noam raison "Je voulais te demander un truc sur hier soir."
    nyra neutre "Quand on s'est croisés ? Je suis rentrée dans ma chambre après."
    noam reflexion "T'es pas ressortie ?"
    nyra sourire "Non. Pourquoi, tu m'as cherchée ?"
    noam neutre "C'est pas ce que je veux dire."
    nyra raison "Je sais. Je te taquine. Un peu mal choisi, désolée."
    noam reflexion "T'avais entendu parler de l'échange de chambres ?"
    nyra hesitation "J'avais compris qu'Elen voulait l'aider. J'ai pas entendu la suite."
    noam neutre "T'as croisé quelqu'un d'autre, après moi ?"
    nyra raison "Non. Enfin, personne dont je me souvienne. Je suis allée me coucher."
    "Elle tourne sa tasse entre ses mains avant de reprendre."
    nyra neutre "Tu cherches surtout à savoir qui était dans les couloirs, c'est ça ?"
    noam fatigue "Je sais pas quoi chercher, en fait."
    nyra raison "Alors commence par ce que tu as vu toi-même. Et laisse tomber le reste pour l'instant, tu vas te rendre malade."
    "Je ne sais pas si elle a raison, mais sa réponse me fait du bien sur le moment. Je n'ai toujours aucun moyen de vérifier ce qu'elle m'a raconté."
    $ j26_alt_nyra = True
    $ hideGroup()
    return

label _26_0_1_1_0_1_PA_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    $ showGroup([("kael", "calme", 0.21), ("elias", "fatigue", 0.45), ("noam", "neutre", 0.70)])
    "Elias a gardé l'outil dont il s'est servi ce matin sur l'établi. Il le fait tourner entre ses doigts sans s'en rendre compte."
    noam raison "La porte d'Elen... elle était vraiment verrouillée de l'intérieur ?"
    elias reflexion "Ouais. C'est pour ça que j'ai dû la forcer."
    noam neutre "Y avait pas moyen de l'ouvrir autrement ?"
    elias raison "Pas avec la tablette, non. Le verrou bloque le lecteur."
    kael reflexion "Les accès des chambres sont isolés. Et les conduits ont été protégés aussi."
    noam raison "Les grilles qu'Elias a posées ?"
    kael neutre "Ouais. L'air passe encore, mais pas quelqu'un."
    elias agace "C'est le but, ouais. Même si j'avoue que j'aurais aimé les faire plus jolies."
    "Il essaie de sourire. Aucun de nous ne le suit."
    noam reflexion "Et hier, vous étiez encore ici ?"
    kael raison "On réparait une fuite avec Elias. On a fermé l'atelier et on est partis chacun de notre côté."
    elias fatigue "Je suis rentré direct. J'ai pas vu Tomas."
    noam raison "Les badges ont dû enregistrer quelque chose, non ?"
    kael reflexion "On a les heures de passage, pas les visages. Je regarderai ce qu'on peut en tirer."
    noam neutre "Merci."
    elias fatigue "Noam... tu crois qu'il a entendu quand j'ai cassé le verrou ?"
    noam fatigue "Non. Je crois pas."
    "Elias baisse les yeux vers son outil."
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
    noam raison "Je voulais savoir si t'avais revu Tomas hier soir."
    ryn colere "Putain. Toi aussi, tu vas t'y mettre ?"
    noam fatigue "Je te demande, c'est tout."
    ryn agace "Non, je l'ai pas revu. J'étais avec Julian et Mara. Après, je suis allé me coucher."
    noam neutre "Vous étiez encore ensemble tard ?"
    ryn colere "J'en sais rien. J'ai pas regardé ma montre toutes les cinq minutes !"
    "Il reprend son souffle, puis fixe le sac."
    ryn fatigue "Tu sais ce que je lui ai dit hier ?"
    noam raison "J'étais là."
    ryn agace "Ouais. Bah moi aussi, j'étais là. Et je l'entends encore, ce que je lui ai dit."
    pause 0.3
    ryn fatigue "Je lui en voulais pour le vote. Ça veut pas dire que je voulais le voir mort."
    noam fatigue "J'ai jamais dit ça."
    ryn agace "Non. Mais je sais ce que tout le monde pense."
    "Il essuie son visage avec son avant-bras. Je ne sais pas s'il transpire ou s'il essaie de cacher quelque chose."
    noam fatigue "Moi, j'arrive même pas à penser à ça pour l'instant."
    ryn triste "Ouais... moi non plus."
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
    noam fatigue "Des trucs. Mais plus je cherche, moins je suis sûr de ce qu'on sait."
    nyra raison "Fais voir."
    if "iris" in investigation_pa_completed:
        noam raison "Iris sait toujours pas ce qui lui est arrivé. Elle continue ses analyses."
        lysa neutre "Bon. Alors si quelqu'un recommence à dire qu'il s'est suicidé, je lui envoie Iris."
    else:
        noam reflexion "Iris a pas encore de réponse. Et je vais pas retourner la voir une troisième fois."
    if "flacon" in investigation_pa_completed:
        lysa reflexion "Et le truc pour dormir ?"
        noam raison "Presque vide. Mais on sait même pas si Tomas y a touché."
    if "elen" in investigation_pa_completed:
        noam raison "Elen dit qu'elle a passé la nuit dans la chambre de Tomas."
        lysa inquiet "J'espère que t'as pas insisté. Elle était en train de tenir debout par miracle."
    if "julian" in investigation_pa_completed:
        noam neutre "Julian dit qu'il était avec Ryn et Mara. Pour l'échange de chambres, il savait rien."
    if "ryn" in investigation_pa_completed:
        noam neutre "Ryn confirme qu'il était avec eux. Il m'a presque envoyé balader quand j'ai demandé."
    if "nyra" in investigation_pa_completed:
        noam reflexion "Nyra, toi, t'étais rentrée après qu'on s'est croisés ?"
        nyra neutre "Ouais, je t'ai dit. J'ai pas vu grand monde après."
    if "kael" in investigation_pa_completed:
        noam raison "Kael et Elias ont bien trouvé le verrou engagé. Et les protections bloquent les passages dans les conduits."
    if "grille" in investigation_pa_completed:
        noam reflexion "La tôle devant l'aération a pas bougé. Mais l'air passe toujours."
        nyra neutre "Ouais. Garde quand même l'image, on sait jamais."
    if "notes" in investigation_pa_completed or "console" in investigation_pa_completed:
        noam fatigue "Il bossait encore sur Keyper hier. Il avait même pas fini ce qu'il cherchait."
        lysa raison "Ouais... mais ça nous dit pas comment il allait, tu sais."
        noam neutre "Je sais. C'est juste dur à avaler."
    if investigation_pa_remaining > 0:
        lysa reflexion "T'as pas fait le tour de tout le monde ?"
        noam raison "Non. Je voulais pas passer la journée à les suivre."
        nyra raison "T'as bien fait. Y a rien qui nous oblige à tout régler ce soir."
    else:
        lysa fatigue "T'as vraiment fait le tour de la station..."
        noam fatigue "Je sais. Et je suis pas plus avancé."
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
    $ showGroup([("julian", "fatigue", 0.20), ("elen", "triste", 0.46), ("noam", "fatigue", 0.73)])
    julian reflexion "On est tous là ?"
    elen fatigue "Pas tous."
    julian triste "..."
    julian fatigue "Oui. Pardon."
    "Personne ne sait comment commencer. Iris finit par prendre la parole."
    $ showGroup([("iris", "fatigue", 0.23), ("elen", "triste", 0.49), ("noam", "fatigue", 0.74)])
    iris raison "J'ai pas grand-chose à vous dire. Je cherche toujours ce qui a causé sa mort."
    elen inquiet "Et les médicaments ?"
    iris raison "Je les ai trouvés dans sa chambre. C'est tout ce que je sais pour l'instant."
    elen triste "C'était ma chambre..."
    iris fatigue "Je sais, Elen. Pardon."
    elen inquiet "Je veux dire... et si quelqu'un venait pour moi ? Si c'était pas Tomas qui devait dormir là ?"
    noam raison "On sait pas si quelqu'un est entré. Elias a dû forcer le verrou."
    elen triste "Mais alors comment il est mort ?"
    "Iris reste silencieuse. Elle serre un instant les mâchoires."
    iris fatigue "J'aimerais vraiment pouvoir te répondre. Là, je peux pas."
    "Elen baisse la tête. Personne ne lui demande d'arrêter de pleurer."
    $ showGroup([("julian", "fatigue", 0.20), ("ryn", "agace", 0.45), ("noam", "neutre", 0.72)])
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
    $ showGroup([("sael", "neutre", 0.21), ("nyra", "neutre", 0.47), ("noam", "neutre", 0.73)])
    sael raison "Hé. On a déjà passé assez de temps à s'en vouloir ces derniers jours. Vous allez pas recommencer ici."
    nyra neutre "Iris a dit qu'elle cherchait encore. On peut peut-être lui laisser une nuit avant de tout retourner."
    noam raison "Ouais. Pour ce soir, on arrête."
    if "flacon" in investigation_pa_completed:
        noam neutre "Et le flacon, on sait même pas à qui étaient les comprimés."
    if "kael" in investigation_pa_completed:
        noam raison "Même avec ce verrou, je comprends pas ce qu'il s'est passé."
    if "elen" in investigation_pa_completed:
        noam raison "Tomas avait juste voulu dormir ailleurs. C'est tout ce qu'Elen lui avait proposé."
    $ showGroup([("julian", "reflexion", 0.22), ("elen", "triste", 0.48), ("noam", "fatigue", 0.73)])
    julian reflexion "Il y a aussi le vote de demain."
    elen colere "Quoi ?"
    julian inquiet "J'ai pas dit qu'on devait le faire ! Mais Kami va forcément en parler. Vous le savez."
    elen colere "Tomas vient de mourir, Julian. Tu peux pas nous laisser cinq minutes ?"
    julian fatigue "Je sais ! Mais si on fait rien et qu'elle nous tombe dessus, c'est encore nous qui allons payer !"
    noam raison "Alors on lui répondra tous. Ensemble. Mais on va pas s'asseoir demain pour voter comme si de rien n'était."
    elen triste "Moi, de toute façon, je pourrai pas."
    $ showGroup([("lysa", "neutre", 0.21), ("mara", "fatigue", 0.47), ("noam", "neutre", 0.73)])
    lysa neutre "Moi non plus."
    mara fatigue "Pareil. Elle nous gonfle déjà assez comme ça."
    "Un à un, les autres finissent par approuver. Julian regarde les places vides, puis pose les mains sur la table."
    $ showGroup([("julian", "fatigue", 0.21), ("elen", "triste", 0.47), ("noam", "neutre", 0.72)])
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
    $ showGroup([("elen", "triste", 0.26), ("iris", "fatigue", 0.50), ("noam", "fatigue", 0.75)])
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
    "Demain, j'irai dans sa chambre. Pas pour jouer au détective. Juste parce que j'ai besoin de voir ce qu'il avait commencé, et ce qu'il comptait faire après."
    "Je ferme le dossier. Une seconde plus tard, je le rouvre, comme si quelque chose allait apparaître."
    "Rien. J'éteins enfin l'écran."
    stop music fadeout 1.0
    call end_day("27", sleeping=True) from _call_j26_alt_end_day_27
    jump _27_0_1_1_0_1_REVEIL
