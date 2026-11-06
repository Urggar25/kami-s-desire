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
    scene bg_chambre at adaptive_fullscreen with dissolve
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
    "Je m'assois de l'autre côté du couloir. Personne n'a vraiment envie de retourner à la cafétéria."
    pause 0.5
    "Quand Iris ressort enfin, elle semble aussi épuisée que nous."
    $ showGroup([("iris", "fatigue", 0.23), ("lysa", "inquiet", 0.46), ("noam", "fatigue", 0.69)])
    iris fatigue "Sael prépare le transfert à l'infirmerie. Je veux photographier quelques éléments avant qu'on bouge le corps."
    noam reflexion "Tu sais comment il est mort ?"
    iris agace "Non. J'ai pas une réponse en dix minutes, Noam."
    noam fatigue "Désolé."
    iris raison "Et je veux éviter que tout le monde dise qu'il s'est suicidé avant même qu'on ait regardé."
    lysa inquiet "On a le droit d'aider ?"
    iris neutre "Deux personnes. Et pas tout de suite. J'ai besoin de finir."
    "Elle repart dans la chambre. On attend encore un moment, sans vraiment se parler."
    $ hideGroup()
    jump _26_0_1_1_0_1_INSPECTION_INTRO

