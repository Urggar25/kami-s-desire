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
