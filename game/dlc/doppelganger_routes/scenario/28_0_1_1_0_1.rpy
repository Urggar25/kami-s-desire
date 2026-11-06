# INVESTIGATION À PA — J28. La découverte de la plaque, du bol et de la plante reste obligatoire.
init 10 python:
    J28A_ROOMS = {
      "dortoir": {
        "title": "DORTOIRS",
        "background": "bg_chambre",
        "description": "Les premières constatations et l'aération de la chambre d'Elen.",
        "actions": [
          "grille",
          "flacon"
        ]
      },
      "infirmerie": {
        "title": "INFIRMERIE",
        "background": "infirmerie2",
        "description": "Iris peut vérifier certains symptômes et réexaminer les prélèvements.",
        "actions": [
          "iris",
          "analyse"
        ]
      },
      "maintenance": {
        "title": "MAINTENANCE",
        "background": "bg_maintenance",
        "description": "Kael vérifie l'installation des plaques et les accès techniques.",
        "actions": [
          "kael",
          "acces"
        ]
      },
      "repos": {
        "title": "SALLE COMMUNE",
        "background": "bg_repos",
        "description": "Sael et Ryn répondent aux questions sur la plante.",
        "actions": [
          "limen"
        ]
      },
      "archive": {
        "title": "ARCHIVES",
        "background": "bg_archive",
        "description": "Les documents sur le Bulbuma Corienis et les registres de livraison.",
        "actions": [
          "botanique",
          "livraisons"
        ]
      },
      "cafeteria": {
        "title": "CAFÉTÉRIA",
        "background": "bg_cafeteria",
        "description": "Les conversations de la veille sont encore dans les mémoires.",
        "actions": [
          "julian"
        ]
      },
      "observation": {
        "title": "OBSERVATION",
        "background": "bg_observation",
        "description": "La salle où Tomas avait trouvé un mystérieux boîtier.",
        "actions": [
          "orbite"
        ]
      },
      "conclave": {
        "title": "SALLE DU CONCLAVE",
        "background": "bg_conclave",
        "description": "La place vide de Tomas reste visible.",
        "actions": []
      },
      "gymnase": {
        "title": "GYMNASE",
        "background": "bg_gymnase",
        "description": "Il n'y a rien à examiner ici.",
        "actions": []
      }
    }
    J28A_ACTIONS = {
      "grille": {
        "title": "Comparer les grilles d'aération",
        "description": "Vérifier que les protections empêchaient le passage physique, pas l'air.",
        "label": "_28_0_1_1_0_1_PA_GRILLE",
        "evidence": "j28_tomas_grilles"
      },
      "flacon": {
        "title": "Revoir le flacon de somnifères",
        "description": "Reconsidérer l'hypothèse du suicide à la lumière du dispositif.",
        "label": "_28_0_1_1_0_1_PA_FLACON",
        "evidence": "j28_tomas_flacon"
      },
      "iris": {
        "title": "Demander à Iris ce que prouvent les prélèvements",
        "description": "Distinguer les observations médicales des suppositions.",
        "label": "_28_0_1_1_0_1_PA_IRIS",
        "evidence": "j28_tomas_iris"
      },
      "analyse": {
        "title": "Consulter la fiche du Bulbuma Corienis",
        "description": "Comparer les caractéristiques du fragment avec des descriptions botaniques.",
        "label": "_28_0_1_1_0_1_PA_ANALYSE",
        "evidence": "j28_tomas_fragment"
      },
      "kael": {
        "title": "Interroger Kael sur la plaque",
        "description": "Comprendre pourquoi cet obstacle ne vient pas des protections habituelles.",
        "label": "_28_0_1_1_0_1_KAEL",
        "evidence": "j28_tomas_kael"
      },
      "acces": {
        "title": "Inspecter le registre de maintenance",
        "description": "Vérifier ce que les journaux de passage peuvent ou non montrer.",
        "label": "_28_0_1_1_0_1_PA_ACCES",
        "evidence": "j28_tomas_acces"
      },
      "limen": {
        "title": "Interroger Sael et Ryn",
        "description": "Demander s'ils connaissent la plante et ses origines à Limen.",
        "label": "_28_0_1_1_0_1_SAEL_RYN",
        "evidence": "j28_tomas_limen"
      },
      "botanique": {
        "title": "Vérifier la répartition du Bulbuma",
        "description": "Chercher où cette plante pourrait pousser au-delà de Limen.",
        "label": "_28_0_1_1_0_1_PA_BOTANIQUE",
        "evidence": "j28_tomas_geographie"
      },
      "livraisons": {
        "title": "Consulter les registres de livraison",
        "description": "Chercher une provenance possible sans désigner prématurément un coupable.",
        "label": "_28_0_1_1_0_1_PA_LIVRAISONS",
        "evidence": "j28_tomas_livraisons"
      },
      "julian": {
        "title": "Reparler à Julian du suicide",
        "description": "Lui demander ce qu'il pense de l'hypothèse d'intoxication.",
        "label": "_28_0_1_1_0_1_PA_JULIAN",
        "evidence": "j28_tomas_julian"
      },
      "orbite": {
        "title": "Examiner les équipements orbitaux",
        "description": "Voir si des matériels auraient pu être déplacés entre observation et maintenance.",
        "label": "_28_0_1_1_0_1_PA_ORBITE",
        "evidence": "j28_tomas_orbite"
      }
    }
    INVESTIGATION_ENTRIES.update({
        "j28_tomas_grilles": {"category": "preuves", "title": "PROTECTIONS ET FLUX D'AIR", "desc": "Les grilles bloquent le passage d'une personne, mais laissent circuler l'air vers les chambres.", "day": "J28", "origin": "DORTOIRS", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_flacon": {"category": "hypotheses", "title": "FLACON ET SUICIDE", "desc": "La présence de somnifères ne suffit pas à expliquer la plaque et les résidus trouvés dans le conduit.", "day": "J28", "origin": "DORTOIRS", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_iris": {"category": "personnes", "title": "IRIS — INTOXICATION POSSIBLE", "desc": "Les symptômes et les résidus rendent l'intoxication plausible, sans identifier avec certitude la substance.", "day": "J28", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_fragment": {"category": "preuves", "title": "FRAGMENT VÉGÉTAL", "desc": "L'aspect de la matière brûlée rappelle le Bulbuma Corienis, sous réserve de confirmation.", "day": "J28", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_kael": {"category": "personnes", "title": "KAEL — PLAQUE NON STANDARD", "desc": "Kael affirme que la plaque du réseau ne correspond pas aux protections qu'il a installées.", "day": "J28", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_acces": {"category": "anomalies", "title": "ACCÈS TECHNIQUES INCOMPLETS", "desc": "Le journal du secteur technique est partiel. Il ne permet pas d'identifier les allées et venues nocturnes.", "day": "J28", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_limen": {"category": "personnes", "title": "SAEL ET RYN — BULBUMA", "desc": "Sael reconnaît le nom de la plante. Ryn s'agace des soupçons liés à Limen.", "day": "J28", "origin": "SALLE COMMUNE", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_geographie": {"category": "anomalies", "title": "BULBUMA HORS LIMEN", "desc": "Le Bulbuma Corienis et ses espèces voisines ne sont pas exclusifs à Limen ; Orbite compte aussi des régions arides.", "day": "J28", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_livraisons": {"category": "preuves", "title": "LIVRAISONS INTERDISTRICTS", "desc": "Les cargaisons transitent entre districts. Aucune ligne retrouvée ne suffit à identifier l'origine du récipient.", "day": "J28", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_julian": {"category": "personnes", "title": "JULIAN — DOUTE SUR LE SUICIDE", "desc": "Julian commence à douter de sa lecture des derniers jours de Tomas et regrette sa dispute.", "day": "J28", "origin": "CAFÉTÉRIA", "status": "À VÉRIFIER", "manual_only": True},
        "j28_tomas_orbite": {"category": "anomalies", "title": "ÉQUIPEMENTS D'ORBITE", "desc": "Les instruments utilisés sur le Conclave viennent de plusieurs districts. Aucune référence ne désigne l'appareil de Tomas.", "day": "J28", "origin": "OBSERVATION", "status": "À VÉRIFIER", "manual_only": True},
    })

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


label _28_0_1_1_0_1_CONDUIT_3:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    "Un peu plus loin, la lumière accroche une plaque métallique placée de travers. Elle coupe presque toute la largeur du conduit."
    lysa reflexion "Attends. Ça, c'est normal ?"
    noam reflexion "J'ai jamais vu une plaque comme ça."
    iris "Vous êtes à la grille ?"
    noam neutre "Presque. Il y a un truc en métal juste avant."
    iris "Ne forcez pas. Regarde comment l'air peut passer."
    menu:
        "Comment examiner la plaque ?"
        "Observer les fixations et le passage d'air":
            "La plaque est coincée sur des supports. L'air n'a plus qu'une ouverture étroite pour passer vers la chambre."
            jump _28_0_1_1_0_1_PLAQUE
        "Essayer de pousser directement":
            $ j28a_detours += 1
            play sound "audio/sfx_duct_scrape.wav"
            "Le métal résiste et grince contre la paroi."
            lysa inquiet "Doucement ! Tu vas faire tomber quelque chose."
            noam neutre "Ouais, attends."
            "Je regarde les attaches. La plaque est posée sur des supports, pas vissée comme les protections habituelles."
            jump _28_0_1_1_0_1_PLAQUE

label _28_0_1_1_0_1_PLAQUE:
    $ j28a_plaque = True
    "Je photographie le montage. La plaque détourne la circulation de l'air vers un passage qui débouche près de la chambre d'Elen."
    noam reflexion "Lysa, tu peux m'aider à la faire glisser ?"
    lysa raison "Oui. Mais pas comme un bourrin. Un... deux... trois."
    play sound "audio/sfx_duct_scrape.wav"
    with hpunch
    "La plaque bouge de quelques centimètres. Derrière, il y a un renfoncement sombre."
    lysa inquiet "Il y a quelque chose là-dedans."
    "Je dirige la lampe vers le fond. Un petit récipient noirci est posé sur une surface métallique. Il contient des résidus brûlés et des fragments qui ressemblent à des feuilles."
    noam surpris "C'est quoi, ce truc ?"
    lysa reflexion "On dirait un bol. Mais qu'est-ce qu'il fout là ?"
    noam raison "Je prends des photos. On touche à rien."
    $ j28a_bol = True
    "Je photographie le récipient, le renfoncement et les alentours, puis je rappelle Iris."
    noam raison "On a trouvé un bol avec quelque chose de brûlé dedans. La plaque était juste devant."
    iris "OK. Surtout, ne remuez pas les cendres. Ça peut encore être dangereux."
    lysa fatigue "Super. J'adore cette sortie."
    iris "Vous avez des gants et un sachet. Si vous pouvez récupérer un fragment sans soulever de poussière, faites-le. Sinon, laissez tout."
    "Je prélève avec une pince un fragment déjà détaché, puis je referme le sachet. Le reste ne bouge pas."
    noam reflexion "Iris, si quelque chose brûlait ici, ça aurait pu passer dans la chambre ?"
    iris "Avec une plaque qui dirige l'air dans cette direction, peut-être. Mais il faut que je voie les photos."
    lysa inquiet "Quelqu'un aurait pu placer tout ça depuis la maintenance..."
    noam neutre "Ouais. Sans jamais ouvrir la porte."
    iris "Revenez. Maintenant."
    "Je jette un dernier regard au bol. C'est la première fois que je vois quelque chose qui ne ressemble pas à un simple accident."
    $ flashlight_off()
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    $ showGroup([("lysa", "fatigue", 0.37), ("noam", "inquiet", 0.66)])
    lysa fatigue "J'ai de la poussière partout. Je veux une douche."
    noam fatigue "Moi aussi."
    lysa reflexion "Tu crois que c'est à cause de ça que Tomas est mort ?"
    noam neutre "Je sais pas. Mais cette plaque n'avait rien à faire là."
    $ hideGroup()
    jump _28_0_1_1_0_1_ANALYSE
# Durée : environ 4 minutes pour la traversée.

label _28_0_1_1_0_1_ANALYSE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_3
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Iris examine les photos du conduit. Elle garde le sachet fermé et agrandit l'image du fragment sur son écran."
    $ showGroup([("iris", "reflexion", 0.22), ("lysa", "neutre", 0.46), ("noam", "inquiet", 0.70)])
    iris reflexion "La plaque n'a pas été installée comme les protections habituelles. Et le récipient est bien derrière."
    noam neutre "On dirait qu'il a brûlé quelque chose."
    iris raison "Oui. Un matériau organique, au moins en partie."
    lysa reflexion "Tu reconnais la plante ?"
    "Iris cherche dans une bibliothèque d'images, puis s'arrête sur une fiche botanique."
    iris surpris "Attendez. Ça ressemble beaucoup à du Bulbuma Corienis."
    noam reflexion "Du quoi ?"
    iris raison "Bulbuma Corienis. C'est une plante assez rare. Elle pousse surtout dans des régions arides."
    lysa inquiet "Et c'est dangereux ?"
    iris neutre "Selon la préparation, certains composants peuvent dégager des substances toxiques quand on les chauffe. Je veux confirmer l'espèce avant de dire que c'est ce qu'on a ici."
    noam raison "Ça pourrait expliquer comment Tomas est mort ?"
    iris reflexion "Une intoxication par inhalation pourrait expliquer une partie de ce qu'on a vu. Mais ça ne démontre pas qu'il a inhalé ce mélange-là."
    lysa raison "Et les maux de tête qu'on a eus en ouvrant la chambre ?"
    iris neutre "Ça peut correspondre à une exposition, oui. Mais il y avait aussi des déchets et une odeur très forte. Je peux pas en déduire davantage."
    noam reflexion "Donc on a un bol brûlé, une plaque pas normale et une mort qui ressemble à une intoxication..."
    iris raison "Ce sont des éléments qui rendent l'hypothèse d'un meurtre beaucoup plus sérieuse. Pas une preuve définitive."
    lysa reflexion "Et le flacon de somnifères, alors ?"
    iris fatigue "Toujours le même problème : on sait pas ce qu'il a pris. Si quelqu'un a mis ce flacon pour nous tromper, c'est une autre possibilité."
    noam neutre "Au moins, la porte fermée ne règle plus rien."
    iris raison "C'est ça. Un verrou fermé n'empêche pas quelqu'un d'agir depuis les conduits."
    pause 0.3
    noam fatigue "Putain, Tomas..."
    lysa reflexion "Tu disais que la plante poussait dans les endroits arides ?"
    iris raison "Oui."
    lysa neutre "Ça fait penser à Limen."
    noam reflexion "À Ryn et Sael."
    iris agace "Pas seulement. Orbite a aussi des territoires arides. Et les livraisons circulent entre districts."
    noam raison "Donc Kael et Nyra aussi."
    iris neutre "Et ça ne prouve rien contre aucun des quatre. L'origine d'une plante ne te dit pas qui l'a apportée ici."
    lysa raison "On sait. Mais ça fait au moins des gens à qui demander."
    iris reflexion "Demandez ce qu'ils connaissent, pas s'ils ont tué Tomas."
    noam sourire "J'essaierai."
    iris agace "Noam..."
    noam neutre "Je plaisante."
    $ j28a_bulbuma = True
    "Je conserve les photos de la plaque et du récipient sur ma tablette. Le sachet reste à l'infirmerie."
    $ hideGroup()
    jump _28_0_1_1_0_1_TEMOINS
# Durée : environ 3 minutes.

label _28_0_1_1_0_1_TEMOINS:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "J'ai les photos du conduit sur ma tablette. Lysa me rejoint, mais elle n'a pas l'air d'avoir envie de reparler de ce qu'on a trouvé."
    $ showGroup([("lysa", "fatigue", 0.36), ("noam", "neutre", 0.69)])
    lysa reflexion "Tu vas interroger tout le monde, maintenant ?"
    noam fatigue "Pas tous. Je voudrais comparer quelques trucs et comprendre d'où vient la plante."
    lysa raison "Alors on garde la même limite qu'hier. Cinq actions. Après, on s'arrête."
    noam neutre "Et si je veux juste passer dans une salle ?"
    lysa neutre "Tu y vas. C'est poser les questions et examiner les indices qui prend du temps."
    noam raison "OK. D'ailleurs, je vais laisser Iris tranquille un peu."
    lysa blase "Bonne idée. Elle va finir par nous jeter dehors."
    "Je sauvegarde les photos de la plaque, du bol et des fragments. Ces découvertes sont déjà acquises : je n'ai pas besoin de dépenser des PA pour les garder."
    $ investigation_pa_begin(28, 5)
    $ investigation_unlocked = True
    $ free_time_active = False
    $ exploration_libre_active = True
    $ exploration_libre_allowed_rooms = list(J28A_ROOMS.keys())
    $ current_scene_active = None
    $ corridor_current = "dortoir"
    $ hideGroup()
    jump _28_0_1_1_0_1_PA_MAP

label _28_0_1_1_0_1_PA_MAP:
    call screen investigation_pa_map(J28A_ROOMS, title="JOUR 28 — LES CONDUITS")
    if _return == "finish":
        jump _28_0_1_1_0_1_PA_FIN
    if _return == "corridors":
        jump _28_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_current_room = _return
    jump _28_0_1_1_0_1_PA_ROOM

label _28_0_1_1_0_1_PA_CORRIDORS:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_j28a_pa_corridors
    $ investigation_pa_current_room = _return
    if investigation_pa_current_room not in J28A_ROOMS:
        jump _28_0_1_1_0_1_PA_MAP
    jump _28_0_1_1_0_1_PA_ROOM

label _28_0_1_1_0_1_PA_ROOM:
    call screen investigation_pa_room(investigation_pa_current_room, J28A_ROOMS, J28A_ACTIONS)
    if _return == "back":
        jump _28_0_1_1_0_1_PA_MAP
    if _return == "corridors":
        jump _28_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_selected = _return
    if not investigation_pa_can_take(investigation_pa_selected):
        jump _28_0_1_1_0_1_PA_ROOM
    call screen investigation_pa_confirm(J28A_ACTIONS[investigation_pa_selected])
    if not _return:
        jump _28_0_1_1_0_1_PA_ROOM
    if not investigation_pa_spend(investigation_pa_selected):
        jump _28_0_1_1_0_1_PA_ROOM
    call expression J28A_ACTIONS[investigation_pa_selected]["label"] from _call_j28a_pa_dynamic
    $ investigation_add(J28A_ACTIONS[investigation_pa_selected]["evidence"])
    if investigation_pa_remaining == 0:
        "J'ai utilisé mes cinq actions. Je peux continuer à circuler, mais pas lancer un nouvel interrogatoire."
        jump _28_0_1_1_0_1_PA_MAP
    jump _28_0_1_1_0_1_PA_ROOM

label _28_0_1_1_0_1_PA_FIN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    if investigation_pa_remaining > 0:
        "Je préfère arrêter avant de faire le tour de tout le monde. On a déjà de quoi parler ce soir."
    jump _28_0_1_1_0_1_NYRA

label _28_0_1_1_0_1_SAEL_RYN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.17), ("ryn", "fatigue", 0.37), ("lysa", "neutre", 0.57), ("noam", "neutre", 0.77)])
    ryn fatigue "Qu'est-ce qu'il y a, encore ?"
    noam raison "On a trouvé quelque chose dans un conduit. Je voulais savoir si vous connaissez une plante : Bulbuma Corienis."
    sael reflexion "J'en ai entendu parler. On en trouve dans certaines régions de Limen."
    ryn reflexion "C'est celle qui pousse dans le désert ?"
    sael neutre "Il y a plusieurs espèces. Pourquoi ?"
    lysa raison "Des restes de plante brûlée, dans un bol. Près de la ventilation d'Elen."
    sael inquiet "Et vous pensez que ça pourrait avoir un rapport avec la mort de Tomas ?"
    noam neutre "Iris dit que c'est possible, oui."
    ryn colere "Ah. Donc parce qu'on vient de Limen, c'est nous maintenant ?"
    noam agace "Mais j'ai pas dit ça !"
    ryn colere "Vous arrivez avec une plante du désert et vous nous regardez tous les deux !"
    lysa blase "On va aussi parler à Kael. Calme-toi."
    ryn fatigue "Ouais, c'est ça..."
    sael raison "Ryn, laisse-le finir."
    noam reflexion "Sael, tu sais ce qui se passe quand on brûle cette plante ?"
    sael neutre "Certaines préparations sont irritantes. Je n'en ai jamais utilisé, alors je ne vais pas inventer."
    noam neutre "Tu en as déjà vu ici ?"
    sael neutre "Non. Pas à ma connaissance."
    ryn colere "Et moi non plus, d'accord ? J'ai même jamais touché à cette plante."
    noam raison "D'accord."
    sael reflexion "Vous avez trouvé comment le bol a été placé ?"
    noam neutre "Pas encore. Mais la plaque qu'on a trouvée ne vient pas des protections habituelles."
    sael raison "Alors c'est peut-être ça qu'il faut comprendre en priorité."
    $ hideGroup()
    return

label _28_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.24), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    noam raison "Tu peux regarder ces photos ? On a trouvé une plaque dans le réseau."
    kael surpris "Attends... C'est quoi, ça ?"
    lysa neutre "On espérait que tu nous le dirais."
    kael reflexion "C'est pas une des plaques qu'on a installées. Nous, on a protégé les grilles, pas mis des obstacles à l'intérieur."
    noam reflexion "Elle redirigeait l'air vers la chambre d'Elen."
    kael raison "Ça en a l'air. Il faudrait voir sur place pour être sûr."
    noam raison "On peut poser cette plaque depuis un accès de maintenance ?"
    kael neutre "Oui. Les branches sont reliées."
    lysa reflexion "Donc pas besoin d'ouvrir la porte de la chambre."
    kael raison "Non, pas pour accéder à cette partie du réseau."
    noam neutre "Et le Bulbuma Corienis ? Tu connais ?"
    kael reflexion "De nom. On trouve des plantes du même genre dans certains secteurs d'Orbite, mais je suis pas botaniste."
    lysa blase "Ça, on avait remarqué."
    kael sourire "Je préfère les moteurs."
    noam raison "Tu peux vérifier les accès de maintenance ?"
    kael neutre "Je regarderai les journaux, mais il y a du passage. Je promets rien."
    noam neutre "Merci."
    $ hideGroup()
    return



label _28_0_1_1_0_1_PA_GRILLE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam reflexion "On avait regardé cette grille le premier jour. Elle n'a pas bougé."
    lysa neutre "Oui. Mais ce qu'on a trouvé était plus loin dans le conduit."
    noam raison "Donc quelqu'un pouvait toucher à cette plaque depuis la maintenance, sans passer par la chambre."
    lysa inquiet "Ça me plaît pas du tout."
    "Je photographie une nouvelle fois les fixations. Elles ont l'air intactes."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_FLACON:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam raison "Le flacon avait l'air tellement évident, le jour où on l'a trouvé."
    lysa reflexion "Tu crois que quelqu'un l'a mis exprès ?"
    noam fatigue "Je sais pas. Mais il n'explique pas la plaque et les trucs brûlés."
    lysa raison "Ouais. Et Iris a jamais dit qu'il avait pris ces comprimés."
    noam neutre "Je vais noter cette contradiction. Pas plus."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "fatigue", 0.34), ("noam", "neutre", 0.69)])
    iris fatigue "Dis-moi que tu viens pas encore pour me demander si j'ai trouvé un meurtrier."
    noam neutre "Non. Je voudrais comprendre ce qu'on sait vraiment sur l'intoxication."
    iris raison "Ses symptômes sont compatibles avec une substance inhalée. Le récipient et la plaque nous donnent une piste sérieuse."
    noam reflexion "Mais tu peux pas confirmer la cause exacte ?"
    iris neutre "Non. Et je veux pas faire croire que oui."
    noam fatigue "D'accord."
    iris inquiet "Tu te rends compte de ce que ça veut dire, si c'est ça ?"
    noam neutre "Ouais. C'est pour ça que je voudrais être sûr."
    iris raison "Alors garde les résultats. Ne rajoute rien."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_ANALYSE:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    "Iris me laisse regarder la photo du fragment sur son écran. Elle garde le sachet fermé."
    $ showGroup([("iris", "reflexion", 0.34), ("noam", "neutre", 0.69)])
    noam raison "Tu l'as identifié avec certitude ?"
    iris neutre "Non. Ça ressemble beaucoup à du Bulbuma Corienis, mais il y a d'autres espèces proches."
    noam reflexion "Et c'est dangereux quand on le brûle ?"
    iris raison "Certaines préparations peuvent dégager des substances toxiques. Ça dépend de ce qu'on chauffe."
    noam fatigue "Ça nous laisse pas mal d'inconnues."
    iris fatigue "Bienvenue dans mon quotidien."
    "Je garde la fiche descriptive, sans annoncer que le fragment vient forcément de cette espèce."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_ACCES:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    "Elias m'ouvre le journal des accès locaux. Les lignes ne couvrent pas toute la nuit."
    $ showGroup([("elias", "fatigue", 0.34), ("noam", "neutre", 0.69)])
    noam raison "C'est tout ?"
    elias fatigue "Ouais. Une partie des terminaux enregistre sur place, une autre non. Et je vais pas t'inventer les lignes manquantes."
    noam reflexion "Donc on peut pas savoir qui a circulé ici le soir du 25 ?"
    elias raison "Pas avec cet écran. Kael verra s'il peut récupérer les journaux du lecteur des dortoirs."
    noam neutre "OK. Tu peux me faire une copie ?"
    elias neutre "Ouais, mais ça sera juste ce qu'on a déjà."
    "J'enregistre les données partielles. Aucune entrée ne désigne un coupable."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_BOTANIQUE:
    scene bg_archive at adaptive_fullscreen with dissolve
    "Je consulte les fiches des plantes poussant dans les zones arides."
    "Le Bulbuma Corienis est surtout cité pour certaines régions de Limen, mais des espèces proches existent aussi dans des secteurs d'Orbite."
    noam reflexion "Donc ça veut rien dire sur le district de celui qui l'a apporté."
    "Je garde les pages. Ça évitera au moins qu'on accuse Ryn ou Sael uniquement à cause de leur origine."
    return

label _28_0_1_1_0_1_PA_LIVRAISONS:
    scene bg_archive at adaptive_fullscreen with dissolve
    "Les registres des livraisons sont longs et pas très bien renseignés. Il y a des lots qui passent d'un district à l'autre sans détailler chaque contenu."
    "Je cherche les plantes médicinales, les résidus organiques et les petits récipients. Plusieurs lignes pourraient convenir, aucune ne permet d'identifier celui trouvé dans le conduit."
    noam fatigue "Super. Des listes partout et rien de précis."
    "Je sauvegarde les références des lots. Elles pourront servir si on retrouve une provenance exacte."
    return

label _28_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.34), ("noam", "neutre", 0.69)])
    noam raison "T'as appris ce qu'on a trouvé dans le conduit ?"
    julian inquiet "Un bol brûlé, ouais. Kael m'a dit qu'il y avait une plaque bizarre."
    noam neutre "Tu penses toujours que Tomas s'est suicidé ?"
    julian fatigue "J'en sais rien. Je pensais que c'était les somnifères, mais là..."
    noam raison "Iris peut pas encore confirmer."
    julian triste "Tu sais, moi je l'ai vu pleurer presque la veille. J'étais sûr qu'il avait craqué."
    noam fatigue "On peut être au fond du trou et mourir pour autre chose."
    julian neutre "Ouais. Ça, je commence à le comprendre."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_ORBITE:
    scene bg_observation at adaptive_fullscreen with dissolve
    "Je repasse l'inventaire des équipements. Plusieurs boîtiers viennent d'Orbite ; d'autres ont été fabriqués dans les ateliers du Conclave."
    "Je ne trouve toujours rien qui identifie l'appareil vu dans les mains de Tomas."
    noam fatigue "C'est fou comme je me souviens mal de cette boîte..."
    "Je ferme l'inventaire. Je n'ai pas le droit de présenter ce manque de souvenir comme une preuve."
    return

label _28_0_1_1_0_1_NYRA:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Nyra nous rejoint près de la porte. Je lui montre les photos du conduit."
    $ showGroup([("nyra", "inquiet", 0.26), ("lysa", "neutre", 0.50), ("noam", "neutre", 0.74)])
    nyra surpris "Attends, un bol brûlé ? Dans la ventilation ?"
    noam raison "Ouais. Et une plaque qui redirigeait l'air."
    nyra reflexion "C'est... bizarre. Vraiment bizarre."
    lysa raison "Iris pense que le récipient a pu servir à diffuser une substance toxique."
    nyra inquiet "Merde."
    noam neutre "On peut toujours pas affirmer que c'est ça qui l'a tué."
    nyra raison "Mais ça expliquerait comment quelqu'un aurait pu agir sans ouvrir la porte."
    if "limen" in investigation_pa_completed or "kael" in investigation_pa_completed:
        lysa neutre "On a posé des questions à ceux qui connaissaient peut-être la plante."
        nyra reflexion "Et alors ?"
        noam raison "Rien qui dise d'où viennent les résidus."
    else:
        lysa neutre "On n'a pas encore demandé aux autres d'où ça peut venir."
        nyra raison "Alors ne vous pressez pas de désigner quelqu'un. On a le temps d'examiner les documents."
    nyra neutre "Ça nous dit pas d'où vient ce qu'on a trouvé."
    lysa raison "Non. On va regarder les livraisons."
    nyra sourire "Je peux m'en occuper. J'ai déjà consulté une partie des registres pour Keyper."
    noam neutre "Ouais, merci."
    nyra reflexion "Juste une chose. Si on annonce que Tomas a été assassiné, ça risque de partir en vrille."
    noam raison "Je sais. Iris va présenter les éléments, pas accuser quelqu'un."
    nyra neutre "OK. Je vais regarder ce que je trouve dans les livraisons."
    "Elle part vers les archives. Lysa referme son carnet."
    lysa blase "Elle a pas tort. On a déjà assez de gens sur les nerfs."
    noam fatigue "C'est bien pour ça que je veux pas accuser quelqu'un sans preuve."
    $ hideGroup()
    jump _28_0_1_1_0_1_REUNION
# Durée : ~1m15.

label _28_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    "On se retrouve au Conclave à la demande d'Iris. La place de Tomas reste vide, et cette fois personne ne propose de faire semblant de préparer un vote."
    $ showGroup([("iris", "reflexion", 0.10), ("elen", "triste", 0.26), ("julian", "fatigue", 0.42), ("lysa", "neutre", 0.58), ("noam", "neutre", 0.74), ("sael", "neutre", 0.90), ("ryn", "fatigue", 1.06), ("nyra", "neutre", -0.06)])
    iris raison "On a trouvé un récipient avec des résidus brûlés dans le conduit relié à la chambre d'Elen."
    julian surpris "Un récipient ?"
    lysa raison "Un petit bol, oui. Il y avait une plaque qui changeait la circulation de l'air."
    noam neutre "On a photographié le montage. C'était pas une des protections installées par Kael."
    elen inquiet "Mais quelqu'un a mis ça là ?"
    iris raison "Ça ne fait pas partie du réseau normal. Oui, quelqu'un l'a placé."
    julian reflexion "Tu penses que Tomas a été empoisonné ?"
    iris neutre "C'est une possibilité sérieuse. On a retrouvé des fragments végétaux brûlés. Une partie pourrait provenir d'une plante capable de dégager des substances toxiques."
    elen peur "Attends... Tu veux dire qu'il a pu respirer ça pendant qu'il dormait ?"
    iris reflexion "Ça pourrait correspondre à une intoxication par inhalation. Mais je n'ai pas encore la preuve que ce soit la cause de sa mort."
    elen triste "Oh, putain..."
    julian neutre "Et les somnifères ?"
    iris neutre "On sait toujours pas s'il en a pris. Le flacon ne suffit pas à expliquer la plaque et le récipient."
    elen colere "Donc il s'est peut-être pas suicidé du tout !"
    iris raison "Oui. C'est possible."
    ryn agace "Et vous avez commencé par nous demander si on connaissait cette plante."
    julian surpris "Quelle plante ?"
    lysa raison "Du Bulbuma Corienis. Ça pousse dans les régions arides."
    ryn colere "Voilà ! Tu vois !"
    sael calme "Ryn. Arrête de t'énerver."
    ryn agace "Mais on nous a posé des questions parce qu'on vient de Limen !"
    noam agace "On sait que cette plante peut venir de plusieurs endroits !"
    sael raison "La provenance d'une plante ne permet pas d'identifier celui qui l'a apportée."
    nyra raison "Et il y a des régions arides à Orbite. Sans parler des livraisons entre districts."
    julian reflexion "C'est pas pour autant qu'on doit ignorer la piste."
    nyra neutre "Non. Mais on peut chercher sans décider que les gens de Limen sont coupables."
    kael raison "La plaque ne ressemble pas aux protections habituelles. Je vais vérifier les journaux de maintenance."
    elen inquiet "Vous pensez vraiment que quelqu'un ici a fait ça ?"
    noam fatigue "On sait pas qui a pu passer par les conduits. Mais quelqu'un y a installé quelque chose."
    lysa raison "Et cette personne pouvait préparer le dispositif sans ouvrir la porte d'Elen."
    pause 0.4
    julian fatigue "Je pensais vraiment que Tomas avait pu..."
    julian triste "Merde. Je lui ai crié dessus jusqu'à la fin."
    elen triste "Julian..."
    julian fatigue "Non, laisse. Je sais."
    iris determine "Je garde les prélèvements et je continue les examens. Et je veux que personne ne touche au montage dans le conduit sans nous prévenir."
    nyra raison "On peut aussi reprendre calmement les témoignages de cette nuit-là. Avec ce qu'on vient de trouver, certaines choses vont peut-être changer."
    noam neutre "Ouais. Mais pas ce soir."
    "Personne ne proteste. On quitte la table les uns après les autres, sans savoir quoi dire à Elen."
    $ hideGroup()
    jump _28_0_1_1_0_1_NUIT
# Durée : ~3m00.

label _28_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je pose la tablette sur le lit. Je suis couvert de poussière, mais j'ai pas envie de me lever pour aller me laver."
    "J'ouvre les photos : la plaque, le bol noirci, les fragments végétaux. Tout ça était juste derrière une chambre où on pensait que personne ne pouvait entrer."
    think "Le verrou était bien fermé. Et pourtant, il suffisait peut-être de passer par les conduits."
    "Je reviens au flacon de somnifères. Il paraît presque trop pratique maintenant. Mais peut-être que je suis en train de lui donner un sens qu'il n'a pas."
    "Je repense à la première fois qu'on a ouvert la porte. Nyra avait proposé d'aérer. Avec cette odeur, je lui aurais demandé la même chose."
    "Je relis les témoignages de Julian, Ryn, Sael, Kael, Elen et Nyra. Aucun ne permet de dire qui a installé cette plaque."
    "La plante pourrait venir de Limen, ou d'Orbite. Et même ça, ça ne prouve rien."
    noam reflexion "Mais pourquoi Tomas ?"
    "Pour son vote ? Parce qu'il avait énervé tout le monde ? Ou parce qu'il avait découvert quelque chose que quelqu'un ne voulait pas qu'il trouve ?"
    "J'ouvre une dernière fois le dossier Keyper-IIB. Il y a les unités ÉID-0, le livre sur la résonance Yanma et ce petit appareil disparu."
    "Je sais pas si c'est lié au bol dans les conduits. Je sais seulement que Tomas avait commencé à chercher, et qu'il n'aura jamais terminé."
    "Demain, je reprends tous les indices. Même ceux qui ont l'air de ne rien avoir à faire là."
    "Je coupe l'écran."
    stop music fadeout 1.0
    call end_day("29", sleeping=True) from _call_j28a_end_day_29
    jump _29_0_1_1_0_1_REVEIL
# Durée : ~1m00.
