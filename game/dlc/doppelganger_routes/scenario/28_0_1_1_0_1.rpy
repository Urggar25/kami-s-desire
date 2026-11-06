# JOUR 28 — CE QUI RESTE DANS LES CONDUITS
# Route alternative du vote rejeté. Le coupable reste inconnu.
default j28a_plaque = False
default j28a_bol = False
default j28a_bulbuma = False
default j28a_detours = 0

label _28_0_1_1_0_1_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"
    $ j28a_plaque = False
    $ j28a_bol = False
    $ j28a_bulbuma = False
    $ j28a_detours = 0
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille en pensant encore à Tomas. Hier, j'ai passé ma journée à fouiller ses papiers. Au final, j'ai surtout découvert qu'il avait encore beaucoup de questions."
    "Une notification apparaît sur ma tablette : livraison du jour 28."
    noam fatigue "Ah oui... Les caisses."
    "Je regarde une dernière fois les photos de Keyper, puis je m'habille."
    think "Aujourd'hui, il faut que je comprenne ce qui s'est passé dans cette chambre."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j28a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _28_0_1_1_0_1_LIVRAISON

label _28_0_1_1_0_1_LIVRAISON:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Près du sas de livraison, Elias et Elen chargent des caisses sur un chariot. Goumi attend derrière eux."
    $ showGroup([("elias", "fatigue", 0.20), ("elen", "reflexion", 0.42), ("noam", "neutre", 0.64), ("lysa", "blase", 0.87)])
    elias fatigue "Attends, Elen, pas celle-là."
    elen neutre "Pourquoi ?"
    elias raison "Elle est plus lourde."
    "La caisse cogne contre le chariot. Elen la retient de justesse."
    elen peur "Oh ! Merde !"
    noam surpris "Ça va ?"
    elen fatigue "Ouais. C'est rien."
    lysa blase "C'est la deuxième en cinq minutes."
    elen colere "Lysa !"
    lysa neutre "Quoi ? Je compte."
    "Je les aide à remettre la caisse en place."
    noam reflexion "Kami a toujours pas arrêté les livraisons ?"
    elias fatigue "Non. C'est pareil que d'habitude. Infirmerie, cafétéria, maintenance."
    elen triste "Elle fait vraiment comme si rien s'était passé."
    noam neutre "Tu veux qu'on termine sans toi ?"
    elen fatigue "Non. J'ai besoin de faire quelque chose. Si je reste seule, je vais encore penser à Tomas."
    lysa inquiet "Elen..."
    elen neutre "Ça va. Enfin, non, mais j'ai pas envie d'en parler pour l'instant."
    noam raison "OK. On termine les caisses."
    "Une fois le chargement fini, Elias repart avec Goumi et Elen. Lysa me rejoint."
    lysa reflexion "Tu vas à l'infirmerie ?"
    noam neutre "Ouais. Je veux voir si Iris a avancé."
    lysa raison "Je viens."
    $ hideGroup()
    jump _28_0_1_1_0_1_INFIRMERIE

label _28_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_2
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Iris est penchée sur ses résultats. Elle a l'air de ne pas avoir dormi."
    $ showGroup([("iris", "fatigue", 0.24), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.70)])
    iris fatigue "Si vous venez demander si j'ai trouvé la cause du décès, je vais mettre une affiche sur la porte."
    noam taquin "Avec juste « non » écrit dessus ?"
    iris blase "Exactement."
    lysa reflexion "T'as quand même une piste ?"
    iris raison "Une intoxication est possible. On s'est trop concentrés sur les somnifères."
    noam reflexion "Tu crois qu'il a rien pris ?"
    iris neutre "Je sais pas ce qu'il a pris. C'est bien le problème."
    noam raison "Il transpirait beaucoup."
    iris reflexion "Oui. Pas de blessure évidente, des draps trempés... Et vous vous souvenez de nos maux de tête ?"
    lysa blase "Comment oublier cette odeur ?"
    iris raison "On a dit que ça venait des déchets. Mais il y avait peut-être autre chose."
    noam reflexion "Tu penses à un gaz ?"
    iris neutre "À une substance inhalée. Je sais pas encore laquelle, ni même s'il y en avait une."
    lysa raison "Les restes de nourriture d'Elen auraient pu masquer une odeur."
    iris reflexion "Voilà. Et on n'a regardé que la grille d'aération, pas ce qu'il y avait derrière."
    noam fatigue "Tu veux retourner dans les conduits."
    iris sourire "Pour une fois, t'as compris avant moi."
    noam agace "Merci."
    iris raison "On prend des gants, des masques et des sachets. Si vous trouvez quelque chose, vous ne le touchez pas n'importe comment."
    lysa neutre "Je vais chercher une lampe."
    "Iris rassemble le matériel. Elle propose de rester dans la chambre d'Elen pour nous guider pendant qu'on passe par l'accès de maintenance."
    $ hideGroup()
    jump _28_0_1_1_0_1_CHAMBRE

label _28_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "On rouvre la chambre d'Elen. L'odeur est moins forte, mais elle me rappelle immédiatement le corps de Tomas."
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "reflexion", 0.23), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    lysa fatigue "Bon. Ça sent toujours la mort ici."
    iris raison "La plaque est toujours devant la grille. Les fixations n'ont pas bougé."
    noam neutre "C'est ce qu'on avait vérifié."
    iris reflexion "Oui. Elle bloque le passage d'une personne, pas le flux d'air."
    noam reflexion "Donc quelque chose pouvait venir du conduit sans qu'on ouvre la porte."
    iris neutre "C'est possible. Je veux juste savoir si le réseau a été modifié."
    lysa raison "Tu nous guideras par téléphone ?"
    iris neutre "Oui. Et vous prenez des photos avant de déplacer quoi que ce soit."
    noam sourire "Compris."
    iris agace "Je parle surtout à toi."
    "Je laisse à Iris une copie du plan des conduits."
    $ hideGroup()
    jump _28_0_1_1_0_1_CONDUIT

label _28_0_1_1_0_1_CONDUIT:
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_horror_pulse.mp3" fadein 1.0
    $ showGroup([("lysa", "inquiet", 0.38), ("noam", "neutre", 0.68)])
    lysa blase "Si je reste coincée, tu me sors de là."
    noam sourire "Ça va bien se passer."
    lysa fatigue "C'est pas ce que j'ai demandé."
    "On ouvre l'accès technique. Je passe devant, Lysa me suit."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on()
    "La lampe éclaire un conduit très étroit. Derrière moi, Lysa cogne déjà son genou contre le métal."
    lysa fatigue "Putain, c'est petit."
    noam neutre "Faut suivre les flèches vers les dortoirs."
    jump _28_0_1_1_0_1_CONDUIT_1

label _28_0_1_1_0_1_CONDUIT_1:
    menu:
        "À quel passage se fier ?"
        "La branche des dortoirs":
            "On avance vers un réseau plus étroit. Le plan correspond à ce qu'Iris nous a envoyé."
            jump _28_0_1_1_0_1_CONDUIT_2
        "Le conduit qui descend vers les machines":
            $ j28a_detours += 1
            "On débouche devant un ventilateur qui barre complètement le passage."
            lysa fatigue "Tu vois bien qu'on va pas passer là !"
            noam agace "Ouais, demi-tour."
            "On revient au croisement et reprend la branche des dortoirs."
            jump _28_0_1_1_0_1_CONDUIT_2

label _28_0_1_1_0_1_CONDUIT_2:
    "Un nouveau croisement apparaît. J'appelle Iris."
    iris "Vous voyez le repère quatre ?"
    noam raison "Ouais, avec deux passages."
    iris "Prenez la dérivation à droite du boîtier. C'est elle qui mène à la chambre d'Elen."
    menu:
        "Quelle direction prendre ?"
        "Suivre le repère indiqué par Iris":
            jump _28_0_1_1_0_1_CONDUIT_3
        "Explorer la branche la plus large":
            $ j28a_detours += 1
            "Une grille donne sur le couloir de l'autre côté des dortoirs."
            lysa blase "C'est pas du tout sa chambre."
            noam fatigue "Je sais. On revient."
            "On retrouve le croisement et suit les indications d'Iris."
            jump _28_0_1_1_0_1_CONDUIT_3
