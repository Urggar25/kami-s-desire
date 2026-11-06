# JOUR 30 — PRINCESSE
# Route « Le Bouc émissaire ». Fin selon l'accusation du jour 29.
default j30a_pirate_reveal = False
default j30a_tomas_truth = False
default j30a_nyra_escaped = False

label _30_0_1_1_0_1_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"
    $ j30a_pirate_reveal = False
    $ j30a_tomas_truth = False
    $ j30a_nyra_escaped = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Il est sept heures trente. Ma tablette sonne depuis une bonne minute, mais je suis déjà réveillé."
    "J'ai rangé presque toutes mes affaires hier. Il reste ma tablette, quelques vêtements et les notes sur Tomas. J'hésite à les laisser là, puis je les glisse dans mon sac."
    noam fatigue "Bon. On rentre."
    "Je vérifie que j'ai rien oublié. La chambre me paraît encore plus petite avec les étagères vides."
    stop music fadeout 0.5
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.7
    kami "Bonjour, mes chers survivants ! Vous avez bien dormi ? Non ? Oh, quel dommage !"
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Embarquement à neuf heures, départ pour la Terre à neuf heures trente. Je ne vous attends pas une minute de plus !"
    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "Et bien sûr, notre regretté Tomas sera rapatrié lui aussi. Enfin, sa dépouille. Quelle triste façon de terminer un séjour..."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Allez ! Encore un petit effort. Pas de nouveau décès avant le départ, ça m'arrangerait !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_chambre at adaptive_fullscreen with dissolve
    noam fatigue "Toujours aussi charmante..."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j30a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _30_0_1_1_0_1_CAFETERIA
# Durée : 1m00.

label _30_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j30a_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Elen est assise devant un bol qu'elle n'a pas touché. Julian termine de fermer son sac."
    if j29a_nyra_detained:
        $ showGroup([("elen", "triste", 0.17), ("julian", "fatigue", 0.35), ("sael", "neutre", 0.53), ("lysa", "neutre", 0.71), ("noam", "fatigue", 0.89)])
        julian reflexion "Sael, pour Nyra ?"
        sael raison "Elle a passé la nuit dans la chambre surveillée. Elle n'a pas essayé de sortir."
        noam reflexion "Vous allez la garder comme ça jusqu'au départ ?"
        julian neutre "Sur Terre, on transmettra les éléments aux autorités. On va pas faire son procès ici."
        lysa blase "Ça, c'est sûr."
        elen inquiet "Et Tomas ?"
        sael fatigue "Iris s'occupe de son transfert."
        elen triste "D'accord..."
        noam neutre "Elen, t'as besoin qu'on porte quelque chose ?"
        elen fatigue "Non. J'ai juste envie de partir."
    else:
        $ showGroup([("elen", "triste", 0.16), ("julian", "fatigue", 0.34), ("nyra", "neutre", 0.52), ("lysa", "neutre", 0.70), ("noam", "fatigue", 0.88)])
        julian reflexion "Vous êtes prêts ? On embarque dans pas longtemps."
        lysa blase "On a trente jours d'entraînement pour ranger des t-shirts. Ça devrait aller."
        nyra sourire "T'en as oublié un dans ta chambre."
        lysa surpris "Hein ?"
        nyra sourire "Non, je plaisante."
        lysa fatigue "C'est pas le moment, Nyra."
        nyra neutre "Ouais. Pardon."
        noam reflexion "Tu prends la navette avec nous ?"
        nyra raison "C'était prévu, oui. On reparlera de tout ça sur Terre."
        elen triste "Moi je veux juste rentrer."
        noam neutre "Ouais."
    "J'avale mon café. Il est beaucoup trop chaud. Avant que je puisse finir, mon téléphone vibre : Kael nous demande de venir immédiatement à l'observation."
    $ hideGroup()
    jump _30_0_1_1_0_1_ALERTE
# Durée : 1m00.

label _30_0_1_1_0_1_ALERTE:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.6
    "Sur l'écran principal, plusieurs points avancent vers la station. Kael passe d'un affichage à l'autre."
    $ showGroup([("kael", "inquiet", 0.18), ("elias", "surpris", 0.37), ("julian", "neutre", 0.56), ("noam", "neutre", 0.75), ("lysa", "neutre", 0.94)])
    kael raison "Je pensais que c'étaient les navettes de Kami. Mais elles arrivent pas du bon côté."
    elias reflexion "Combien ?"
    kael inquiet "Six petits appareils. Un gros derrière. Et aucune identification."
    julian agace "Tu leur as demandé ?"
    kael raison "Trois fois. Ils répondent pas sur les canaux normaux."
    noam reflexion "Et Kami ?"
    $ hideGroup()
    stop music fadeout 0.3
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.5
    kami "Alors là ! J'ai demandé un départ sans incident ! Qui sont ces idiots ?!"
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Ces appareils ne m'appartiennent pas. Et ils se sont placés beaucoup trop près du Conclave."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "S'ils ne s'écartent pas, je vais devoir m'en occuper. Ce serait dommage d'abîmer votre jolie station juste avant le départ !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.4
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "inquiet", 0.18), ("elias", "surpris", 0.37), ("julian", "neutre", 0.56), ("noam", "inquiet", 0.75), ("lysa", "neutre", 0.94)])
    elias inquiet "Elle va leur tirer dessus ? Ils sont presque collés à nous !"
    kael raison "C'est peut-être pour ça qu'ils se rapprochent. Si Kami tire, elle risque de toucher le Conclave."
    "Une voix grésille soudain dans les haut-parleurs."
    "???" "Vous me recevez ? Hé, le Conclave ? On vient récupérer quelqu'un."
    julian colere "Vous êtes qui ?!"
    "???" "On est pas là pour vous. On vient chercher notre commandante."
    noam surpris "Votre commandante ?"
    "???" "Ouais. Enfin, notre Princesse. Elle est toujours chez vous, non ?"
    lysa surpris "Votre quoi ?"
    julian surpris "C'est une blague ?!"
    "???" "Non, pourquoi ? Passez-la-moi, s'il vous plaît."
    $ hideGroup()
    jump _30_0_1_1_0_1_REVELATION
# Durée : 1m30.

label _30_0_1_1_0_1_REVELATION:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    if j29a_nyra_detained:
        "Sael vient d'arriver avec Nyra. Kael lui a demandé de la faire venir après avoir entendu le mot « commandante »."
        $ showGroup([("nyra", "fatigue", 0.16), ("sael", "neutre", 0.34), ("julian", "agace", 0.52), ("elen", "triste", 0.70), ("noam", "inquiet", 0.88)])
        julian colere "Si vous parlez de la personne qu'on surveille, elle ne sort pas sans explication !"
        "???" "Attendez, vous la retenez ? Vous êtes sérieux ?"
        nyra colere "Arrêtez de gueuler deux minutes !"
        "???" "Capitaine ?! Vous êtes là !"
        nyra fatigue "Oui. Et arrête de m'appeler comme ça."
        "???" "Pardon, Princesse."
        nyra colere "Mais putain !"
    else:
        "Nyra nous rejoint, attirée par l'alarme. Elle s'arrête net en entendant la voix."
        $ showGroup([("nyra", "surpris", 0.16), ("julian", "agace", 0.35), ("elen", "triste", 0.54), ("lysa", "surpris", 0.73), ("noam", "inquiet", 0.92)])
        nyra fatigue "Non... Sérieusement ?"
        "???" "Attendez. Je connais cette voix. Capitaine ?"
        nyra colere "Ferme-la !"
        "???" "Ah ! Je savais que vous étiez là, Princesse !"
        julian surpris "Nyra ?!"
    pause 0.3
    noam surpris "Attends. Ils viennent te chercher, TOI ?"
    nyra fatigue "Oui."
    julian colere "Mais c'est qui ces gens ?!"
    nyra neutre "Mon équipage."
    elen surpris "Ton équipage ?"
    nyra fatigue "Je commande une flotte. Des pirates, si vous voulez tout savoir."
    $ j30a_pirate_reveal = True
    julian surpris "QUOI ?!"
    noam reflexion "Depuis quand ?"
    nyra raison "Depuis avant le Conclave. J'ai été capturée il y a six mois. Ils m'ont enfermée sur Syelena, et Kami m'a sortie de là pour son jeu."
    elen inquiet "Et ces gens t'attendaient ?"
    nyra neutre "Ils me cherchaient, oui."
    "???" "Et on vous a retrouvée ! On peut accoster dans dix minutes, Princesse !"
    nyra colere "Tu peux arrêter de m'appeler comme ça devant tout le monde ?!"
    "???" "Oui, Capitaine."
    noam reflexion "L'appareil de Tomas. Dans la salle d'observation. C'était un émetteur à toi ?"
    "Nyra ne répond pas immédiatement."
    nyra neutre "Oui."
    $ hideGroup()
    jump _30_0_1_1_0_1_AVEU
# Durée : 1m30.

label _30_0_1_1_0_1_AVEU:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    $ showGroup([("nyra", "neutre", 0.12), ("noam", "inquiet", 0.29), ("elen", "triste", 0.46), ("iris", "fatigue", 0.63), ("julian", "agace", 0.80), ("lysa", "neutre", 0.97)])
    noam reflexion "C'était un relais Yanma ?"
    nyra raison "Oui. Je pouvais parler à ma flotte sans passer par les communications du Conclave."
    noam raison "Tomas l'a trouvé le jour 25."
    nyra fatigue "Oui."
    noam inquiet "Comment tu le savais ? Tu n'étais pas dans la salle."
    nyra reflexion "L'appareil m'a signalé qu'on l'avait retiré de son support. J'ai vérifié le journal d'accès. Tomas était là quand c'est arrivé."
    noam surpris "Mais il savait même pas ce que c'était !"
    nyra fatigue "J'en savais rien. Il cherchait déjà des trucs sur Keyper. S'il identifiait mon relais, Kami aurait pu retrouver mon équipage."
    noam colere "Nyra. C'est toi qui as tué Tomas ?"
    pause 0.6
    nyra triste "Oui."
    julian colere "Putain..."
    noam colere "Le bol dans la ventilation ? La plaque ?"
    nyra neutre "Oui. Je les ai installés depuis la maintenance."
    iris reflexion "Et les somnifères ?"
    nyra fatigue "J'ai pris le flacon dans les affaires d'Elen. Je l'ai laissé pour que ça ressemble à un suicide."
    elen colere "Tu savais qu'il dormait dans MA chambre ?!"
    nyra neutre "J'ai entendu quand vous en avez parlé."
    elen colere_noire "Et t'as passé les jours suivants à ME CONSOLER ?!"
    nyra triste "Elen..."
    elen colere "Non, mais ferme-la ! Il t'avait fait quoi, Tomas ?!"
    nyra fatigue "Rien."
    elen colere "Alors pourquoi tu l'as tué ?!"
    nyra colere "Parce que j'ai paniqué ! Je voulais pas qu'on retrouve mes gars !"
    noam colere "T'aurais pu déplacer ton appareil. Ou lui parler ! Il savait même pas ce qu'il avait dans les mains !"
    nyra fatigue "Je sais."
    noam raison "Non, je crois pas que tu saches."
    pause 0.4
    nyra neutre "Je vais pas vous demander de comprendre. Je l'ai fait. C'est tout."
    $ j30a_tomas_truth = True
    "Lysa entraîne doucement Elen vers la sortie. Elen ne regarde même plus Nyra."
    $ hideGroup()
    jump _30_0_1_1_0_1_ULTIMATUM
# Durée : 1m45.

label _30_0_1_1_0_1_ULTIMATUM:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    $ showGroup([("nyra", "fatigue", 0.16), ("julian", "colere", 0.34), ("kael", "inquiet", 0.52), ("noam", "inquiet", 0.70), ("sael", "neutre", 0.88)])
    "???" "Princesse ? La navette est prête. On peut vous récupérer."
    julian colere "Hors de question ! Elle vient d'avouer un meurtre !"
    "???" "Vous voulez qu'on vienne la chercher nous-mêmes ?"
    kael inquiet "S'ils forcent l'amarrage, on peut perdre la pression dans le secteur du sas."
    julian agace "On va quand même pas la laisser partir !"
    nyra colere "Hé ! Personne ne force rien. Vous coupez les armes et vous attendez."
    "???" "Compris, Capitaine. Mais on repart pas sans vous."
    $ hideGroup()
    stop music fadeout 0.4
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.4
    kami "Non, non, non ! Personne ne transforme mon départ en bataille spatiale !"
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Ces imbéciles sont collés à la station. Si je tire maintenant, je risque de vous emporter avec eux. C'est extrêmement agaçant !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous avez vingt minutes pour régler ça. À neuf heures trente, ma navette part. Et ne venez pas vous plaindre si vous la ratez !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.4
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "fatigue", 0.16), ("julian", "colere", 0.34), ("kael", "inquiet", 0.52), ("noam", "inquiet", 0.70), ("sael", "neutre", 0.88)])
    if j29a_nyra_detained:
        julian colere "On l'avait enfermée pour l'enquête !"
        sael raison "On ne peut pas risquer une attaque contre le sas."
        noam fatigue "On a déjà perdu Tomas. On va pas en perdre d'autres juste pour l'empêcher de partir."
        julian agace "Et on fait quoi ? On lui dit bon voyage ?"
        noam colere "Non. On la laisse partir parce qu'on n'a pas le choix."
    else:
        julian colere "Vous allez juste la laisser partir ?!"
        sael raison "On n'a pas de quoi repousser toute une flotte."
        noam fatigue "On va pas risquer d'autres morts."
        nyra neutre "Je vous ai rien demandé."
        noam colere "Si. Tu m'as demandé de te faire confiance."
        nyra fatigue "..."
    sael neutre "On consigne ses aveux et on évacue le secteur."
    "Julian se détourne, furieux. Nyra récupère ses affaires sans que personne ne lui parle."
    $ hideGroup()
    jump _30_0_1_1_0_1_DEPART_NYRA
# Durée : 1m00.

label _30_0_1_1_0_1_DEPART_NYRA:
    scene bg_sas at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Il est un peu plus de neuf heures. La navette pirate attend de l'autre côté du sas."
    $ showGroup([("nyra", "neutre", 0.36), ("noam", "fatigue", 0.68)])
    if j29a_nyra_detained:
        nyra reflexion "Tu avais raison, hier."
        noam colere "Tu veux que je te félicite ?"
        nyra fatigue "Non."
        noam raison "Tomas te faisait confiance. Moi aussi."
        nyra triste "Je sais."
    else:
        nyra reflexion "Je suppose que tu m'en veux."
        noam fatigue "Je t'ai raconté toute mon enquête. Pendant trois jours."
        nyra neutre "Oui."
        noam colere "Tu m'as regardé accuser la mauvaise personne."
        nyra triste "Oui..."
    "Un voyant passe au vert."
    "???" "Capitaine ! On est prêts !"
    nyra colere "J'arrive !"
    noam neutre "Nyra."
    nyra reflexion "Quoi ?"
    noam fatigue "Il voulait juste comprendre. Tomas."
    nyra triste "Je sais."
    $ hideGroup()
    "Elle passe la porte. Quelques instants plus tard, sa navette se détache de la station."
    $ j30a_nyra_escaped = True
    jump _30_0_1_1_0_1_RETOUR
# Durée : 45 s.

label _30_0_1_1_0_1_RETOUR:
    scene bg_sas at adaptive_fullscreen with dissolve
    "L'embarquement officiel reprend. Iris et Lysa attendent près de la navette pour la Terre."
    $ showGroup([("elen", "triste", 0.18), ("lysa", "neutre", 0.39), ("iris", "fatigue", 0.60), ("noam", "fatigue", 0.81)])
    iris raison "Ils ont chargé la dépouille de Tomas dans le compartiment prévu."
    elen triste "D'accord."
    lysa inquiet "Viens. On va s'asseoir ensemble."
    elen fatigue "Ouais. Merci."
    iris neutre "Noam ? Dépêche-toi, ils ferment."
    noam neutre "J'arrive."
    $ hideGroup()
    scene bg_navette at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je m'assois près d'un hublot. Elen a pris place avec Lysa, deux rangées plus loin. Personne ne parle beaucoup."
    "La navette se détache du Conclave. Je regarde le sas s'éloigner, puis la station entière disparaît peu à peu derrière nous."
    "Je repense à Tomas. Il avait trouvé un petit appareil, l'avait reposé, puis il avait continué ses recherches sur Keyper comme si de rien n'était."
    "Il ne savait même pas ce qu'il avait découvert."
    if j29a_nyra_detained:
        "Hier, j'avais accusé la bonne personne. Ça n'a rien changé à son départ."
    else:
        "Hier, j'avais accusé quelqu'un d'autre. Nyra m'avait laissé me tromper."
    "Je regarde la Terre devant nous. J'aurais aimé pouvoir dire à Tomas qu'on avait fini par comprendre."
    stop music fadeout 1.0
    scene black with fade
    if j29a_nyra_detained:
        call screen kd_ending_reached("Princesse — La vérité", "ENDING ALT // JOUR 30")
    else:
        call screen kd_ending_reached("Princesse — Le dernier mensonge", "ENDING ALT // JOUR 30")
    return
# Durée visée : 9–11 minutes, départ vers 9 h 30.
