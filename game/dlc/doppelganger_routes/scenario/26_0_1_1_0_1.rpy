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
    $ showGroup([("lysa", "blase", 0.06), ("elen", "fatigue", 0.21), ("julian", "neutre", 0.36), ("mara", "taquin", 0.51), ("iris", "fatigue", 0.66), ("noam", "neutre", 0.81), ("nyra", "neutre", 0.96), ("elias", "fatigue", 1.11)])
    julian reflexion "Vous avez lu le nouveau texte ? Sur les sanctions pour les opinions ?"
    iris fatigue "J'ai essayé. Puis t'as commencé à parler."
    mara sourire "Moi j'ai retenu qu'on avait le droit de dire que Julian était chiant."
    julian agace "C'est pas ce que dit le texte !"
    noam neutre "Salut."
    elen sourire "Salut, Noam !"
    lysa reflexion "Attendez. Tomas est où ?"
    julian fatigue "Il nous évite encore."
    elen reflexion "Je pense qu'il dort. Il était vraiment fatigué."
    lysa inquiet "Il est jamais en retard, même quand il a dormi deux heures."
    elen neutre "Je lui ai prêté ma chambre hier soir. On a échangé."
    mara taquin "Oh ! Monsieur a passé la nuit dans ton lit ?"
    elen colere "Mara !"
    mara rire "Quoi ?! C'était gratuit, je sais, mais fallait que je la fasse."
    noam surpris "Pourquoi vous avez changé de chambre ?"
    elen inquiet "Il avait peur que quelqu'un revienne frapper à sa porte. Je me suis dit qu'il serait plus tranquille chez moi."
    noam reflexion "Ah. C'était donc ça, votre conversation d'hier soir."
    elen neutre "Ouais. J'ai dormi dans sa chambre, lui dans la mienne."
    lysa inquiet "Mais il est toujours pas arrivé."
    nyra raison "On peut aller voir sans lui faire peur. Il a eu assez de monde sur le dos."
    noam neutre "Elen, tu viens avec moi ?"
    elen content "Oui."
    lysa neutre "Je viens aussi."
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
    play sound sfx_door_knock
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
    $ showGroup([("kael", "reflexion", 0.12), ("elias", "fatigue", 0.29), ("iris", "inquiet", 0.46), ("elen", "inquiet", 0.63), ("noam", "inquiet", 0.80), ("lysa", "inquiet", 0.97)])
    kael reflexion "Vous avez essayé l'accès normal ?"
    elen inquiet "Oui. Ça marche pas."
    elias raison "Si le verrou intérieur est mis, le lecteur extérieur peut rien faire."
    iris agace "Ouvre, Elias."
    elias fatigue "Ça va abîmer la serrure."
    iris colere "On s'en fout de la serrure !"
    elias surpris "Bon, OK !"
    "Il place son outil sur le boîtier. Un claquement retentit."
    elias neutre "Voilà. Le verrou a sauté."
    "Kael pousse la porte. Une odeur horrible me prend à la gorge."
    noam fatigue "Putain, c'est quoi, cette odeur ?"
    lysa fatigue "Mais qu'est-ce que tu gardes dans ta chambre, Elen ?!"
    elen fatigue "J'ai pas eu le temps de ranger, désolée !"
    "Il y a des vêtements partout, des barquettes de nourriture oubliées, des emballages et des boîtes par terre."
    "Et puis je vois le lit. Tomas est allongé dessus, immobile."
    noam inquiet "Tomas ?"
    elen inquiet "Tomas !"
    "Je m'approche. Sa chemise est trempée et ses cheveux sont collés à son front."
    noam peur "Tomas ! Réveille-toi !"
    iris determine "Noam, écarte-toi."
    "Elle lui prend le poignet, puis vérifie son cou. Elle recommence sans nous regarder."
    pause 0.8
    elen peur "Iris ?"
    iris triste "Elen, recule."
    elen peur "Qu'est-ce qu'il a ?"
    iris triste "Je trouve pas de pouls. Il respire plus."
    noam peur "Non... Non, il était là hier. Il me parlait !"
    iris determine "Je vérifie encore."
    "Sael arrive, alertée par les cris. Elle procède à son tour à un examen."
    $ showGroup([("iris", "triste", 0.18), ("sael", "inquiet", 0.37), ("elen", "peur", 0.56), ("noam", "peur", 0.75), ("lysa", "inquiet", 0.94)])
    sael triste "Il est mort."
    pause 1.0
    elen peur "Non !"
    noam fatigue "Tomas..."
    "Je regarde sa poitrine, sans réussir à accepter qu'elle ne bouge plus."
    "L'odeur me soulève le cœur. Iris pose sa main sur sa tempe."
    iris fatigue "J'ai mal au crâne. On peut pas tous rester ici."
    "Nyra arrive dans l'encadrement de la porte."
    $ showGroup([("iris", "fatigue", 0.18), ("nyra", "inquiet", 0.37), ("elen", "peur", 0.56), ("noam", "inquiet", 0.75), ("lysa", "inquiet", 0.94)])
    nyra inquiet "Qu'est-ce qui se passe ?"
    noam fatigue "Tomas est mort."
    nyra peur "..."
    nyra inquiet "Merde..."
    elen triste "Il était dans ma chambre. Je lui ai proposé..."
    nyra raison "Elen. T'es pas responsable de ça."
    "Nyra grimace et fait un pas en arrière."
    nyra reflexion "C'est irrespirable. On devrait laisser la porte ouverte et aérer tout ça."
    iris fatigue "Oui, s'il vous plaît. J'arrive plus à réfléchir avec cette odeur."
    noam raison "Kael, tu peux augmenter l'extraction du couloir ?"
    kael calme "Je vais voir."
    "Nyra maintient la porte ouverte. Quelques minutes plus tard, l'air devient moins lourd."
    "Iris demande qu'on laisse les affaires en place avant de déplacer Tomas."
    $ hideGroup()
    jump _26_0_1_1_0_1_INSPECTION_INTRO
# Durée : 3m00 — Total : 7m15.

label _26_0_1_1_0_1_INSPECTION_INTRO:
    $ current_period = "Après-midi"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Elen attend dans le couloir. Iris veut qu'on regarde la pièce avant de transporter Tomas à l'infirmerie."
    $ showGroup([("iris", "reflexion", 0.18), ("lysa", "inquiet", 0.39), ("nyra", "neutre", 0.60), ("noam", "inquiet", 0.81)])
    iris reflexion "Je vois pas de blessure extérieure évidente."
    lysa inquiet "Pourquoi il est trempé, alors ?"
    iris raison "C'est une des choses qu'il faut comprendre."
    nyra raison "On devrait noter ce qu'on trouve avant que quelqu'un range tout ça."
    noam neutre "Ouais. Je m'en occupe."
    jump _26_0_1_1_0_1_INSPECTION
# Durée : 45 s — Total : 8m00.

label _26_0_1_1_0_1_INSPECTION:
    menu:
        "Que regarder ?"
        "Le corps et les draps" if not j26_alt_corps:
            $ j26_alt_corps = True
            noam inquiet "Sa chemise est trempée, les draps aussi."
            iris reflexion "On dirait qu'il a beaucoup transpiré. Comme une forte fièvre, mais ça peut venir d'autre chose."
            noam reflexion "Il a souffert ?"
            iris triste "J'en sais rien, Noam."
            jump _26_0_1_1_0_1_INSPECTION
        "Le flacon près du lit" if not j26_alt_flacon:
            $ j26_alt_flacon = True
            "Un petit flacon presque vide a roulé derrière une boîte."
            noam reflexion "Iris, regarde."
            iris surpris "Attends, touche pas."
            iris inquiet "Un somnifère."
            lysa inquiet "Il est presque vide."
            nyra reflexion "On devrait demander à Elen si c'est à elle."
            iris raison "Et vérifier si Tomas en a pris. Le flacon tout seul prouve rien."
            jump _26_0_1_1_0_1_INSPECTION
        "L'aération" if not j26_alt_vent:
            $ j26_alt_vent = True
            noam reflexion "La plaque est toujours en place devant la grille."
            lysa neutre "Celle qu'Elias a installée pour bloquer les conduits ?"
            iris raison "Ça empêche les gens de passer. L'air circule toujours."
            nyra neutre "Donc quelqu'un n'a pas pu entrer par là sans tout démonter."
            noam neutre "Je note."
            jump _26_0_1_1_0_1_INSPECTION
        "La porte" if not j26_alt_verrou:
            $ j26_alt_verrou = True
            "Le boîtier du verrou porte les marques de l'outil d'Elias."
            noam reflexion "Quand on est arrivés, c'était fermé de l'intérieur."
            lysa raison "Oui. J'étais là. Elen a essayé, puis toi."
            nyra reflexion "Et pour ressortir, on aurait dû rouvrir de l'intérieur."
            noam fatigue "À moins qu'on ait raté quelque chose."
            jump _26_0_1_1_0_1_INSPECTION
        "Les déchets et l'odeur" if not j26_alt_bazar:
            $ j26_alt_bazar = True
            "Derrière une pile de vêtements, je découvre une barquette de nourriture qui a tourné."
            lysa fatigue "Je vais plus jamais venir ici."
            iris blase "Tu venais souvent ?"
            lysa neutre "Non. Et ça va pas commencer."
            noam reflexion "Ça explique au moins une partie de l'odeur."
            nyra neutre "Avec l'aération, difficile de distinguer quoi que ce soit maintenant."
            jump _26_0_1_1_0_1_INSPECTION
        "Terminer l'examen" if j26_alt_corps and j26_alt_flacon and j26_alt_vent and j26_alt_verrou and j26_alt_bazar:
            jump _26_0_1_1_0_1_HYPOTHESES
# Durée : 3m00 — Total : ~11m00.

label _26_0_1_1_0_1_HYPOTHESES:
    $ showGroup([("iris", "reflexion", 0.20), ("lysa", "neutre", 0.41), ("nyra", "neutre", 0.62), ("noam", "inquiet", 0.83)])
    lysa reflexion "Le flacon, les menaces hier, la porte fermée..."
    noam neutre "Tu penses à un suicide ?"
    lysa fatigue "J'espère que non."
    nyra raison "C'est une possibilité. Mais on devrait pas décider tout de suite."
    iris raison "Je dois l'examiner à l'infirmerie. Là, on sait pas s'il a pris ces comprimés."
    noam reflexion "Hier, il cherchait encore Keyper. Il avait des tas de questions."
    lysa neutre "Ça veut pas dire qu'il allait bien."
    noam fatigue "Je sais."
    nyra reflexion "On peut essayer de reconstituer ses dernières heures. Ça sera plus utile."
    noam neutre "D'accord."
    "Sael vient aider Iris à transporter Tomas. Je sors avant qu'elles le soulèvent."
    $ hideGroup()
    jump _26_0_1_1_0_1_INFIRMERIE
# Durée : 1m00 — Total : ~12m00.


label _26_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j26_alt_door_3
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je retrouve Iris et Sael à l'infirmerie. Le corps de Tomas est derrière un rideau."
    $ showGroup([("iris", "fatigue", 0.22), ("sael", "reflexion", 0.43), ("lysa", "neutre", 0.64), ("noam", "inquiet", 0.84)])
    noam inquiet "Alors ?"
    iris fatigue "On n'a pas de réponse définitive."
    noam surpris "Même avec le flacon ?"
    iris agace "Noam, un flacon presque vide, ça veut pas dire qu'il a avalé tout ce qu'il y avait dedans."
    sael raison "L'intoxication est possible. Médicamenteuse ou autre. Il faudra examiner davantage."
    lysa reflexion "Et les draps trempés ?"
    iris raison "Ça arrive dans plusieurs situations. J'ai pas envie de vous raconter n'importe quoi."
    noam fatigue "OK. Désolé."
    iris triste "Je l'ai vu hier. Il avait l'air fatigué, c'est tout."
    noam neutre "On va interroger les autres."
    iris determine "Alors évitez de leur hurler dessus comme hier."
    noam raison "On va essayer."
    $ hideGroup()
    jump _26_0_1_1_0_1_ENQUETE
# Durée : 1m20 — Total : ~13m20.

label _26_0_1_1_0_1_ENQUETE:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Nyra m'attend dans la salle commune."
    $ showGroup([("nyra", "neutre", 0.34), ("noam", "fatigue", 0.67)])
    nyra raison "Il faut demander à chacun où il était hier soir. Et qui savait que Tomas avait changé de chambre."
    noam reflexion "On commence par Elen ?"
    nyra neutre "Oui. Mais doucement. Elle s'en veut déjà assez."
    noam fatigue "Je déteste faire ça."
    nyra sourire "Je sais. C'est pour ça que je viens."
    noam neutre "Merci."
    $ hideGroup()
    jump _26_0_1_1_0_1_TEMOINS
# Durée : 35 s — Total : ~14m00.

label _26_0_1_1_0_1_TEMOINS:
    menu:
        "Qui interroger ?"
        "Elen" if not j26_alt_elen:
            $ j26_alt_elen = True
            call _26_0_1_1_0_1_ELEN from _call_j26_alt_elen
            jump _26_0_1_1_0_1_TEMOINS
        "Julian" if not j26_alt_julian:
            $ j26_alt_julian = True
            call _26_0_1_1_0_1_JULIAN from _call_j26_alt_julian
            jump _26_0_1_1_0_1_TEMOINS
        "Kael et Elias" if not j26_alt_kael:
            $ j26_alt_kael = True
            call _26_0_1_1_0_1_KAEL from _call_j26_alt_kael
            jump _26_0_1_1_0_1_TEMOINS
        "Ryn et Sael" if not j26_alt_ryn:
            $ j26_alt_ryn = True
            call _26_0_1_1_0_1_RYN from _call_j26_alt_ryn
            jump _26_0_1_1_0_1_TEMOINS
        "Nyra" if not j26_alt_nyra:
            $ j26_alt_nyra = True
            call _26_0_1_1_0_1_NYRA from _call_j26_alt_nyra
            jump _26_0_1_1_0_1_TEMOINS
        "Faire le point" if j26_alt_elen and j26_alt_julian and j26_alt_kael and j26_alt_ryn and j26_alt_nyra:
            jump _26_0_1_1_0_1_BILAN
# Durée : variable — Total : ~19m00.

label _26_0_1_1_0_1_ELEN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "triste", 0.21), ("nyra", "neutre", 0.45), ("noam", "inquiet", 0.70)])
    elen triste "C'est moi qui lui ai proposé ma chambre..."
    noam raison "On veut juste comprendre ce qui s'est passé après."
    elen fatigue "On a parlé dans le couloir, hier. Il avait peur qu'on frappe encore chez lui."
    noam neutre "Je vous ai vus de loin. J'ai rien entendu."
    elen neutre "On a échangé les chambres. Je suis allée dans la sienne et j'y suis restée."
    nyra reflexion "Tu es revenue dans ta chambre pendant la nuit ?"
    elen desaccord "Non ! Même pour récupérer mon pyjama, j'ai pas voulu le déranger."
    noam reflexion "Tu sais qui vous a vus discuter ?"
    elen fatigue "Non... Il y avait du monde dans le couloir, je crois."
    noam raison "Les somnifères, ils étaient à toi ?"
    elen surpris "Des somnifères ? Peut-être dans ma trousse. Je m'en sers pas, moi."
    nyra neutre "Tu te souviens combien il en restait ?"
    elen triste "Non. Désolée."
    noam neutre "C'est pas grave."
    elen triste "Je voulais juste l'aider à dormir..."
    $ hideGroup()
    return
# Durée : 1m00.

label _26_0_1_1_0_1_JULIAN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "agace", 0.23), ("nyra", "neutre", 0.47), ("noam", "neutre", 0.71)])
    julian agace "Je sais. J'ai crié sur Tomas. Tout le monde m'a entendu."
    noam reflexion "Et après le dîner ?"
    julian fatigue "Salle commune avec Ryn et Mara. Puis je suis rentré."
    nyra raison "Tu savais qu'Elen et Tomas avaient échangé leurs chambres ?"
    julian surpris "Quoi ? Non. Pourquoi ?"
    noam neutre "Tomas avait peur qu'on vienne lui demander des comptes."
    julian triste "Ah..."
    julian colere "Mais je suis pas allé le tuer, putain !"
    noam raison "On ne dit pas ça."
    julian fatigue "C'est exactement ce que j'ai l'impression d'entendre."
    pause 0.3
    julian triste "J'ai été con avec lui. J'aurais dû lui parler autrement. Mais je suis pas un meurtrier."
    nyra neutre "Merci, Julian."
    $ hideGroup()
    return
# Durée : 1m00.

label _26_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.16), ("elias", "fatigue", 0.36), ("nyra", "neutre", 0.56), ("noam", "neutre", 0.78)])
    kael reflexion "J'étais avec Elias hier soir. On s'occupait des pièces de maintenance."
    elias fatigue "Ouais. Après, on est rentrés chacun chez soi."
    noam raison "Le verrou intérieur, vous confirmez ?"
    elias raison "Il était engagé. J'ai dû forcer. Tout le monde était là."
    nyra reflexion "Et les conduits ?"
    kael calme "Les plaques empêchent de passer, mais laissent circuler l'air."
    elias neutre "On aurait pas bouché l'aération, hein. On est pas dingues."
    noam fatigue "OK. Merci."
    $ hideGroup()
    return
# Durée : 50 s.

label _26_0_1_1_0_1_RYN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("ryn", "agace", 0.17), ("sael", "neutre", 0.37), ("nyra", "neutre", 0.57), ("noam", "neutre", 0.77)])
    ryn agace "Ouais, j'étais en colère contre lui. Je vous le cache pas."
    noam neutre "Où t'étais hier soir ?"
    ryn fatigue "Dans la salle commune avec Julian et Mara. Après, j'ai dormi."
    sael reflexion "Je l'ai croisé avant de rejoindre l'infirmerie."
    nyra raison "Tu as parlé à Tomas après le dîner ?"
    ryn neutre "Non. J'avais plus rien à lui dire."
    noam reflexion "Et toi, Sael ?"
    sael neutre "J'étais à l'infirmerie. Seule, puis je suis allée dormir."
    ryn colere "C'est pas parce que j'étais contre son vote que je voulais qu'il crève !"
    noam agace "Je sais, Ryn."
    sael neutre "Alors arrêtons là."
    $ hideGroup()
    return
# Durée : 50 s.

label _26_0_1_1_0_1_NYRA:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam reflexion "Et toi, hier soir ?"
    nyra sourire "Tu m'as croisée dans les dortoirs. J'allais me coucher."
    noam neutre "Ouais, je me rappelle."
    nyra neutre "Et c'est ce que j'ai fait."
    noam raison "Tu savais pour l'échange ?"
    nyra hesitation "Je savais qu'Elen voulait l'aider. J'ai pas entendu ce qu'ils avaient décidé exactement."
    noam reflexion "Tu as parlé à Tomas ?"
    nyra neutre "Non. Je l'ai juste aperçu de loin."
    nyra raison "Tu peux me poser les mêmes questions qu'aux autres, Noam. C'est normal."
    noam fatigue "J'ai vraiment horreur de ça."
    nyra sourire "Je sais."
    $ hideGroup()
    return
# Durée : 45 s.

label _26_0_1_1_0_1_BILAN:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    $ showGroup([("nyra", "reflexion", 0.28), ("lysa", "neutre", 0.51), ("noam", "fatigue", 0.74)])
    lysa reflexion "Alors ?"
    noam raison "Les alibis sont flous. La porte était fermée de l'intérieur."
    nyra raison "Et l'échange des chambres n'était pas annoncé à tout le monde."
    lysa neutre "Donc on sait toujours pas si c'est un suicide."
    noam fatigue "Non."
    nyra reflexion "On devrait attendre le rapport d'Iris avant d'accuser quelqu'un."
    noam neutre "Ouais. Mais il faut aussi décider pour le vote."
    $ hideGroup()
    jump _26_0_1_1_0_1_REUNION
# Durée : 35 s — Total : ~20m00.

label _26_0_1_1_0_1_REUNION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "La place de Tomas est vide. Personne ne la regarde longtemps."
    $ showGroup([("julian", "reflexion", 0.04), ("elen", "triste", 0.17), ("iris", "fatigue", 0.30), ("lysa", "neutre", 0.43), ("noam", "neutre", 0.56), ("nyra", "neutre", 0.69), ("ryn", "agace", 0.82), ("sael", "neutre", 0.95), ("mara", "fatigue", 1.08), ("kael", "calme", -0.08)])
    julian reflexion "Je sais que c'est pas le moment, mais il y a le vote demain."
    elen colere "Tomas est mort ce matin !"
    julian inquiet "Je sais, Elen ! Je dis juste qu'il faut décider."
    iris fatigue "On sait même pas comment il est mort."
    ryn agace "Et si Kami nous force à participer ?"
    sael raison "Qu'elle essaie."
    nyra raison "On peut décider ensemble de ne pas y aller. Ça aussi, c'est une décision."
    noam raison "Je propose qu'on boycotte le vote du jour 27. On reprendra le débat quand on saura ce qui s'est passé."
    elen determine "Moi, j'irai pas."
    lysa neutre "Moi non plus."
    mara fatigue "Pareil. J'ai autre chose en tête."
    kael neutre "D'accord."
    "Les autres approuvent. Julian hésite puis finit par accepter."
    julian fatigue "OK. Mais on assume tous, alors."
    $ j26_alt_boycott = True
    play sound sfx_announce
    $ hideGroup()
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
    $ showGroup([("elen", "triste", 0.28), ("iris", "fatigue", 0.48), ("noam", "fatigue", 0.69), ("nyra", "neutre", 0.90)])
    elen triste "Elle est vraiment dégueulasse."
    iris agace "Ouais."
    nyra neutre "On reprendra demain."
    noam fatigue "Demain."
    $ hideGroup()
    jump _26_0_1_1_0_1_NUIT
# Durée : 2m30 — Total : ~23m00.

label _26_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je suis enfin seul. Sur ma tablette, j'ai noté le flacon, les draps trempés, le verrou et les témoignages."
    "Mais chaque fois que je ferme les yeux, je revois Tomas allongé sur ce lit."
    think "Hier, il cherchait encore Keyper."
    "Il avait trouvé une carte, et cette station était à quelques heures de vol. Il avait l'air presque content d'avoir avancé."
    "Il y avait aussi ce petit appareil qu'il examinait quand je suis arrivé."
    "Je sais pas pourquoi je repense à ça maintenant. Peut-être parce que c'était la dernière fois où je l'ai vu faire autre chose que subir les reproches des autres."
    noam fatigue "Merde..."
    "Demain, je vais regarder dans sa chambre. Ses notes, ses livres, les dossiers qu'il a laissés."
    "Peut-être qu'il avait découvert quelque chose. Peut-être pas. Mais je peux pas juste m'arrêter là."
    "Je coupe la lumière."
    stop music fadeout 1.0
    call end_day("27", sleeping=True) from _call_j26_alt_end_day_27
    jump _27_0_1_1_0_1_REVEIL
# Durée : 1m00 — Total : ~24m00.
