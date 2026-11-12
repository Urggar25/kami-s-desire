# INVESTIGATION À PA — J28. La découverte de la plaque, du bol et de la plante reste obligatoire.
init 10 python:
    J28A_ROOMS = {
      "dortoir": {
        "title": "DORTOIRS",
        "background": "j26_elen_vide",
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
        "j28_photo_plaque": {"category": "preuves", "title": "PLAQUE DANS LE CONDUIT", "desc": "Une seconde plaque non standard a été placée à l'intérieur du conduit pour dévier le flux d'air.", "day": "J28", "origin": "CONDUITS DE VENTILATION", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/maintenance1.png"},
        "j28_photo_grille": {"category": "preuves", "title": "FIXATIONS INTACTES — CHAMBRE D'ELEN", "desc": "Nouvelle photographie de la protection artisanale et de ses fixations, après la découverte des conduits.", "day": "J28", "origin": "CHAMBRE D'ELEN", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j28_photo_bulbuma": {"category": "preuves", "title": "POT DE BULBUMA BRÛLÉ", "desc": "Un récipient noirci contenant des résidus végétaux brûlés était caché derrière la plaque de dérivation.", "day": "J28", "origin": "CONDUITS DE VENTILATION", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/maintenance2.png"},
        "j28_core_plaque": {"category": "preuves", "title": "PLAQUE DE DÉRIVATION D'AIR", "desc": "Une plaque non standard dévie l'air vers la chambre d'Elen depuis l'intérieur du réseau de ventilation.", "day": "J28", "origin": "CONDUITS", "status": "CONFIRMÉ", "manual_only": True},
        "j28_core_bol": {"category": "preuves", "title": "RÉCIPIENT BRÛLÉ", "desc": "Un petit récipient noirci contenant des résidus végétaux brûlés a été découvert derrière la plaque.", "day": "J28", "origin": "CONDUITS", "status": "CONFIRMÉ", "manual_only": True},
        "j28_core_bulbuma": {"category": "hypotheses", "title": "PISTE DU BULBUMA CORIENIS", "desc": "Des fragments évoquent une plante dont certaines préparations chauffées peuvent être toxiques, sans identification définitive.", "day": "J28", "origin": "INFIRMERIE", "status": "HYPOTHÈSE", "manual_only": True},
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
default j28a_air_traced = False

label _28_0_1_1_0_1_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"
    $ j28a_plaque = False
    $ j28a_bol = False
    $ j28a_bulbuma = False
    $ j28a_detours = 0
    $ j28a_air_traced = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je passe la main à côté de l'oreiller. Rien. Ma tablette a glissé sous le lit pendant la nuit."
    "Elle affiche toujours les photos des affaires de Tomas. J'ai dû m'endormir dessus."
    "Au milieu des notifications, il y a encore son dernier message. « Merci pour tout à l'heure. On se voit demain. »"
    noam fatigue "Ouais..."
    "Je ferme la conversation. Une alerte apparaît : livraison du jour 28."
    noam reflexion "Les caisses. J'avais complètement oublié."
    "Je m'habille et regarde une dernière fois la photo de la grille dans la chambre d'Elen. Hier, je l'ai fixée pendant dix minutes sans comprendre ce qui me dérangeait."
    "On était tous tellement occupés à regarder cette foutue porte."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j28a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _28_0_1_1_0_1_LIVRAISON

label _28_0_1_1_0_1_LIVRAISON:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Près du sas, Elias et Elen empilent des caisses. Goumi attend avec le chariot, parfaitement immobile. Évidemment, lui n'a aucun problème à faire comme si tout allait bien."
    $ showGroup([("elias", "fatigue", 0.080), ("elen", "reflexion", 0.360), ("noam", "neutre", 0.640), ("lysa", "blase", 0.920)])
    elias fatigue "Hé ! Pas celle-là, elle est lourde !"
    "Elen soulève la caisse et manque de la lâcher. Elias la retient par un coin."
    elen peur "Putain ! Pardon..."
    elias fatigue "Mais dis-le si t'arrives pas à la porter !"
    elen colere "J'y arrive ! J'ai juste glissé."
    lysa blase "C'est la deuxième fois."
    elen colere "Lysa, s'il te plaît..."
    noam neutre "Donne, je prends le côté."
    "On finit de charger sans parler. Sur le bord d'un carton, je reconnais le symbole de l'infirmerie."
    noam reflexion "C'est quand même dingue. Les livraisons continuent."
    elias fatigue "Bah ouais. On va pas arrêter de bouffer."
    elen triste "Même Goumi, il a rien changé à sa tournée."
    lysa neutre "Tu veux rentrer, Elen ?"
    elen fatigue "Non. Si je reste seule, je vais juste repenser à..."
    "Elle s'arrête en voyant une petite caisse de fournitures portant la mention ARCHIVE. C'est le district de Tomas."
    elen neutre "Allez. Il reste quoi ?"
    elias neutre "Deux cartons. Après c'est bon."
    "On termine ensemble. Elen repart avec Elias et Goumi, sans nous regarder."
    lysa inquiet "Elle dort plus. Ça se voit."
    noam fatigue "Ouais. Et on continue de lui demander ce qu'elle a fait ce soir-là."
    lysa reflexion "T'as une meilleure idée ?"
    noam neutre "Pas encore."
    lysa reflexion "Tu voulais voir Sael, non ?"
    noam raison "Ouais. Pour les résultats. Et pour la ventilation."
    lysa neutre "Je viens avec toi."
    $ hideGroup()
    jump _28_0_1_1_0_1_INFIRMERIE

label _28_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_2
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Sael est encore près du lit où l'on a déposé Tomas. Iris regarde des relevés sur un écran, les yeux rouges de fatigue."
    $ showGroup([("sael", "fatigue", 0.13), ("iris", "fatigue", 0.37), ("lysa", "neutre", 0.61), ("noam", "neutre", 0.85)])
    iris fatigue "Si c'est encore pour me demander si j'ai trouvé le coupable, je vous fais payer la consultation."
    noam taquin "On peut payer en café ?"
    iris fatigue "Vu la tête de celui de ce matin, non."
    sael raison "Laissez-la. Elle a cherché dans les dossiers toute la nuit."
    noam reflexion "Et toi, tu as trouvé quelque chose sur Tomas ?"
    sael fatigue "Une chose me gêne. Ses vêtements étaient trempés, il n'avait pas de blessure visible et son état ne colle pas forcément à ce qu'on attendrait des somnifères."
    lysa reflexion "Alors c'est quoi ?"
    sael raison "Je n'en sais rien. Une intoxication est possible. Il faut que j'en sache plus sur ce qu'il a respiré."
    iris reflexion "Dans les archives médicales, j'ai retrouvé plusieurs descriptions d'exposition à des substances chauffées. Certains symptômes ressemblent à ceux qu'on a vus."
    noam raison "Et cette odeur, quand on a ouvert la chambre ?"
    sael inquiet "On a tous eu mal à la tête. Les déchets pouvaient expliquer une partie de l'odeur, mais pas forcément tout."
    lysa reflexion "On a regardé la grille. Pas ce qu'il y avait derrière."
    "Sael lève aussitôt les yeux."
    sael raison "La protection était intacte ?"
    noam neutre "Oui. Et l'air passait toujours."
    sael reflexion "Alors il faut inspecter le conduit. Si quelque chose était dedans, on a pu le manquer."
    iris neutre "Je peux rester dans la chambre avec le plan du réseau et vous guider par téléphone."
    sael raison "Prenez des gants, des masques et des sachets. Et ne touchez à rien avant de l'avoir photographié."
    lysa blase "Ça commence à ressembler à une très bonne journée."
    iris sourire "Tu peux toujours rester ici avec moi."
    lysa neutre "Non merci. Noam ferait une connerie sans surveillance."
    noam fatigue "Je suis là, hein."
    "Sael nous passe le matériel. Avant de partir, je regarde le rideau devant le lit de Tomas."
    sael neutre "Noam. Si tu trouves quelque chose, tu m'appelles. Pas de conclusion tout seul."
    noam raison "Promis."
    $ hideGroup()
    jump _28_0_1_1_0_1_CHAMBRE

label _28_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Iris nous attend devant la chambre d'Elen. Elle hésite une seconde avant de débloquer la porte."
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "reflexion", 0.23), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    lysa fatigue "Ah, ouais. Ça sent toujours autant la merde."
    iris neutre "Un peu moins. Mais on ne va pas rester longtemps."
    noam reflexion "La plaque qu'Elias avait fixée sur la grille n'a pas bougé."
    iris raison "Et elle bloque le passage d'une personne. Pas l'air. Regarde."
    "Elle approche une bande de papier de l'aération. Elle bouge immédiatement."
    lysa inquiet "Donc quelqu'un pouvait envoyer quelque chose par là sans ouvrir la porte ?"
    iris reflexion "C'est une possibilité. Pas une réponse."
    noam raison "Il faut suivre la branche jusqu'à la maintenance."
    iris neutre "J'ai le plan. Vous m'appelez au premier croisement et vous prenez des photos avant de déplacer quoi que ce soit."
    lysa blase "Et si on se coince ?"
    iris sourire "J'appellerai Goumi. Il vous sortira comme deux sacs de linge."
    noam taquin "Très rassurant."
    "Je laisse une copie du plan à Iris et rejoins Lysa. Avant de refermer la porte, je regarde une dernière fois le lit vide."
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
            "Je suis les flèches peintes sur la paroi. Le plan d'Iris correspond."
            jump _28_0_1_1_0_1_CONDUIT_2
        "Le conduit qui descend vers les machines":
            $ j28a_detours += 1
            "On débouche devant un ventilateur protégé par une grille. Le souffle couvre presque ma voix."
            lysa fatigue "Tu veux qu'on passe à travers, peut-être ?"
            noam fatigue "Non. J'ai compris."
            lysa blase "C'est déjà ça."
            "On retourne au croisement et on retrouve la branche des dortoirs."
            jump _28_0_1_1_0_1_CONDUIT_2

label _28_0_1_1_0_1_CONDUIT_2:
    "Le passage se divise de nouveau. J'appelle Iris."
    iris "Vous voyez le repère quatre ?"
    noam raison "Oui. Deux branches."
    iris "À droite du boîtier. Si vous avez pris la bonne direction, vous devez sentir l'air tirer vers vous."
    menu:
        "Quelle direction prendre ?"
        "Suivre le repère indiqué par Iris":
            jump _28_0_1_1_0_1_CONDUIT_3
        "Explorer la branche la plus large":
            $ j28a_detours += 1
            "Au bout, une grille donne sur un couloir désert. Un courant d'air froid entre par les fentes."
            lysa blase "Voilà, on a visité un autre bout de couloir. Passionnant."
            noam neutre "On revient."
            "On reprend la bonne branche et je commence à sentir le souffle décrit par Iris."
            jump _28_0_1_1_0_1_CONDUIT_3

label _28_0_1_1_0_1_CONDUIT_3:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    "Plus loin, le passage s'élargit à peine. Ma lampe éclaire une plaque de métal qui n'a rien à faire là."
    lysa reflexion "Attends. C'est quoi, cette tôle ?"
    noam reflexion "Il y a une ouverture derrière. On dirait qu'elle force l'air à passer d'un seul côté."
    iris "Vous êtes arrivés près de la chambre ?"
    noam neutre "Presque. Il y a une plaque posée de travers."
    iris "Ne la bougez pas encore. Il faut comprendre où va l'air."
    menu:
        "Comment vérifier la dérivation ?"
        "Observer les fixations et suivre le courant d'air":
            $ j28a_air_traced = True
            "Je passe un petit morceau de papier devant la fente. Il se plaque aussitôt contre le bord orienté vers les dortoirs."
            noam surpris "Lysa... L'air part tout droit vers la chambre d'Elen."
            lysa inquiet "Et de l'autre côté ?"
            noam raison "Presque rien. C'est cette plaque qui le dirige."
            jump _28_0_1_1_0_1_PLAQUE
        "Pousser la plaque pour regarder derrière":
            $ j28a_detours += 1
            play sound "audio/sfx_duct_scrape.wav"
            "Le métal grince. Lysa me retient le bras."
            lysa colere "Hé ! Iris a dit de pas y toucher !"
            noam fatigue "Ouais. Désolé."
            iris "Qu'est-ce que vous avez fait ?"
            noam neutre "Rien. Enfin, presque."
            iris "Alors prenez une photo et regardez où passe l'air avant de tout déplacer."
            "Je sors un petit bout de papier et suis le souffle jusqu'à la branche d'Elen. Il est beaucoup plus fort de ce côté."
            $ j28a_air_traced = True
            jump _28_0_1_1_0_1_PLAQUE

label _28_0_1_1_0_1_PLAQUE:
    $ j28a_plaque = True
    "Je photographie la plaque et ses supports. L'air est détourné vers la chambre d'Elen, alors qu'il devrait circuler dans plusieurs branches."
    call investigation_take_manual_photo("j28_photo_plaque", "bg_conduit_reseau", (0.55, 0.52), 2.2) from _call_j28_photo_plaque
    if j28a_detours >= 2:
        lysa blase "Bon, au moins on a compris le trajet. On aurait pu éviter de ramper dans toute la station."
        noam fatigue "Tu veux vraiment en parler maintenant ?"
    noam reflexion "Il y a un truc derrière. Tu vois ?"
    lysa inquiet "Une espèce de niche. Attends, je vais éclairer."
    "Je demande à Iris si on peut déplacer la plaque après l'avoir photographiée. Elle nous dit de ne la faire glisser que de quelques centimètres."
    play sound "audio/sfx_duct_scrape.wav"
    with hpunch
    "Le métal résiste, puis se décale. Derrière, un petit récipient noirci repose sur une surface isolante. Le fond est couvert de cendres et de fragments végétaux."
    pause 0.4
    noam surpris "C'est quoi ce bordel... ?"
    lysa inquiet "Ne le touche pas."
    "Une marque plus claire entoure le fond du récipient. Le métal au-dessous a changé de couleur, comme s'il avait chauffé. Mais je ne vois ni câble ni alimentation."
    noam reflexion "Il a chauffé ici. Regarde le dessous."
    lysa reflexion "Et comment ? Il y a rien de branché."
    "Je prends une photo. Puis une autre, plus proche. Je vérifie les bords du renfoncement et les fixations."
    $ j28a_bol = True
    call investigation_take_manual_photo("j28_photo_bulbuma", "bg_conduit_reseau", (0.55, 0.65), 2.2) from _call_j28_photo_bulbuma
    "Je rappelle Iris."
    noam inquiet "On a trouvé un bol. Avec des trucs brûlés dedans. Il est caché juste derrière la plaque."
    iris "Vous n'avez pas remué les cendres ?"
    noam raison "Non."
    iris "Bien. Laissez le récipient là. S'il y a des résidus dangereux, je veux pas que vous les respiriez."
    lysa fatigue "On a des masques. Ils servent à quoi, du coup ?"
    iris "À limiter les risques, pas à faire n'importe quoi."
    "Avec une pince, je récupère seulement un fragment qui s'est détaché sur le bord. Je le glisse dans un sachet."
    noam reflexion "Iris... Si ça a brûlé pendant qu'il dormait..."
    iris "Noam, reviens. Sael regardera ce que vous avez trouvé."
    "Je regarde à nouveau la plaque. Je pense à la porte fermée, au verrou, à Tomas qui avait peur de retourner dans sa chambre."
    "Je revois son message : « On se voit demain. »"
    noam fatigue "Putain..."
    lysa inquiet "Noam ?"
    noam neutre "On rentre."
    "Je ne sais pas ce qu'on vient de trouver. Mais quelqu'un a mis ce bol là. Et il fallait savoir exactement quelle branche du conduit menait à cette chambre."
    $ flashlight_off()
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    $ showGroup([("lysa", "fatigue", 0.37), ("noam", "inquiet", 0.66)])
    lysa reflexion "T'as pensé à la même chose que moi ?"
    noam fatigue "Que quelqu'un aurait pu faire ça sans toucher au verrou ? Oui."
    lysa inquiet "Et si c'était pas Tomas qui devait dormir là ?"
    "Je m'arrête devant l'accès de maintenance."
    noam reflexion "On sait pas quand le bol a été posé."
    lysa neutre "C'est justement ce qui me fait peur."
    $ hideGroup()
    jump _28_0_1_1_0_1_ANALYSE

label _28_0_1_1_0_1_ANALYSE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_3
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Sael étale nos photographies sur la tablette. Iris garde le sachet fermé, à côté des résultats de ses recherches."
    $ showGroup([("sael", "reflexion", 0.12), ("iris", "fatigue", 0.34), ("lysa", "neutre", 0.57), ("noam", "inquiet", 0.81)])
    sael reflexion "La plaque n'est pas une simple protection. Elle oblige l'air à passer par une seule branche."
    noam raison "Et le bol était juste derrière. Il y a une marque de chaleur sous le fond."
    sael inquiet "Vous avez vu comment il a été chauffé ?"
    noam neutre "Non. Pas de câble. Rien d'évident."
    iris reflexion "Sur la photo, ça ressemble à des résidus végétaux. Mais je peux pas dire lesquels juste avec ça."
    sael raison "Moi non plus. J'ai déjà entendu parler de plantes qui deviennent dangereuses quand on les chauffe. Ça dépend de la préparation."
    "Iris ouvre une fiche et agrandit plusieurs images."
    iris surpris "Attendez. Ça ressemble à du Bulbuma Corienis."
    lysa reflexion "Ça se trouve où ?"
    sael neutre "Dans certaines régions sèches de Limen. Pas seulement là, d'après ce que je sais."
    iris raison "Il y a aussi des espèces proches. Et certaines préparations dégagent des substances toxiques si elles chauffent. Je vais garder les photos pour comparer."
    noam inquiet "Ça pourrait tuer quelqu'un pendant son sommeil ?"
    sael fatigue "Une intoxication par inhalation est possible, oui. Mais je ne vais pas te dire que Tomas est mort de ça sans analyse."
    noam reflexion "Et nos maux de tête ?"
    sael raison "Ça colle avec une exposition. Mais entre la nourriture pourrie et ce qu'on a trouvé, on ne peut pas isoler une cause."
    lysa reflexion "Les somnifères, alors ?"
    noam inquiet "On a un flacon, oui. Mais maintenant on a aussi ce montage dans le conduit."
    call refutation_run("j28_tomas")
    if _return[0] == "success":
        call play_noam_interupt
        iris raison "Exact. Le flacon ne suffit pas à conclure au suicide. Il faut poursuivre les analyses."
    else:
        sael neutre "Pas d'accusation pour l'instant. On doit encore vérifier le dispositif."
    sael neutre "On n'a toujours pas la preuve qu'il en ait pris. Le flacon était là. C'est tout."
    iris fatigue "Et on ne sait même pas depuis quand ce montage est dans le conduit."
    "Je regarde les trois photos : la plaque, le récipient et la chambre."
    noam reflexion "S'il a été placé avant que Tomas échange sa chambre avec Elen..."
    lysa inquiet "Ça voudrait dire qu'Elen devait dormir dedans."
    noam raison "Et s'il a été mis après, quelqu'un savait qu'ils avaient échangé."
    sael inquiet "Voilà pourquoi je veux qu'on soit prudents. Il manque encore l'heure, le moyen de chauffer le bol et la personne qui l'a posé."
    iris raison "Le Bulbuma, pour l'instant, c'est une piste. Pas une identification."
    noam fatigue "On a quand même beaucoup plus qu'un flacon de comprimés."
    sael neutre "Oui. Assez pour prévenir les autres. Pas pour donner un nom."
    lysa reflexion "On va poser quelques questions avant la réunion."
    sael raison "D'accord. Mais allez-y doucement avec Elen."
    $ j28a_bulbuma = True
    "Les photos restent sur ma tablette. Le sachet est conservé à l'infirmerie."
    $ hideGroup()
    jump _28_0_1_1_0_1_TEMOINS

label _28_0_1_1_0_1_TEMOINS:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Dans la salle commune, Lysa s'assoit en face de moi. Je pose la tablette entre nous."
    $ showGroup([("lysa", "fatigue", 0.36), ("noam", "neutre", 0.69)])
    lysa reflexion "Bon. Tu veux aller voir qui ?"
    noam raison "Kael pour la plaque. Les autres pour la plante. Et je voudrais comprendre qui savait que Tomas dormait chez Elen."
    lysa blase "Tout ça aujourd'hui ? T'as vu l'heure ?"
    noam fatigue "Je sais."
    lysa reflexion "Comme hier. Cinq actions. On choisit celles qui nous semblent utiles, et après on fait le point."
    noam reflexion "Même si on a pas trouvé le coupable ?"
    lysa neutre "On va pas trouver un assassin en courant partout jusqu'à trois heures du matin."
    noam neutre "Tu marques un point."
    "Je note les premières découvertes. La plaque, le bol et les fragments sont acquis. Le reste dépend de ce que j'aurai le temps de vérifier."
    $ investigation_pa_begin(28, 5)
    $ investigation_unlocked = True
    $ investigation_add("j28_core_plaque", notify=False)
    $ investigation_add("j28_core_bol", notify=False)
    $ investigation_add("j28_core_bulbuma", notify=False)
    $ free_time_active = False
    $ conclave_lock = False
    $ dortoir_lock = False
    $ exploration_libre_active = True
    $ exploration_libre_allowed_rooms = list(J28A_ROOMS.keys())
    $ current_scene_active = None
    $ corridor_current = "dortoir"
    $ hideGroup()
    jump _28_0_1_1_0_1_PA_MAP

label _28_0_1_1_0_1_PA_MAP:
    # Compatibilité avec les anciens jumps et sauvegardes.
    jump _28_0_1_1_0_1_PA_CORRIDORS

label _28_0_1_1_0_1_PA_CORRIDORS:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_j28a_pa_corridors
    $ investigation_pa_current_room = _return
    if investigation_pa_current_room not in J28A_ROOMS:
        jump _28_0_1_1_0_1_PA_CORRIDORS
    jump _28_0_1_1_0_1_PA_ROOM

label _28_0_1_1_0_1_PA_ROOM:
    call screen investigation_pa_room(investigation_pa_current_room, J28A_ROOMS, J28A_ACTIONS)
    if _return == "finish":
        jump _28_0_1_1_0_1_PA_FIN
    if _return == "corridors":
        call EXIT_ROOM_TO_CORRIDOR from _call_j28a_pa_exit_room_native
        jump _28_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_selected = _return
    if not investigation_pa_can_take(investigation_pa_selected):
        jump _28_0_1_1_0_1_PA_ROOM
    call INVESTIGATION_PA_CHOICE(J28A_ACTIONS[investigation_pa_selected], investigation_pa_current_room) from _call_j28a_pa_choice_native
    if not _return:
        jump _28_0_1_1_0_1_PA_ROOM
    if not investigation_pa_spend(investigation_pa_selected):
        jump _28_0_1_1_0_1_PA_ROOM
    call expression J28A_ACTIONS[investigation_pa_selected]["label"] from _call_j28a_pa_dynamic
    $ investigation_add(J28A_ACTIONS[investigation_pa_selected]["evidence"])
    if investigation_pa_remaining == 0:
        "Les cinq actions du jour sont utilisées. Je fais le point avant la réunion."
        jump _28_0_1_1_0_1_PA_FIN
    jump _28_0_1_1_0_1_PA_ROOM

label _28_0_1_1_0_1_PA_FIN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    if investigation_pa_remaining > 0:
        "Je préfère arrêter avant de faire le tour de tout le monde. On a déjà de quoi parler ce soir."
    jump _28_0_1_1_0_1_NYRA

label _28_0_1_1_0_1_SAEL_RYN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.22), ("ryn", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    ryn fatigue "Quoi, encore ?"
    noam raison "On cherche d'où peut venir une plante. Du Bulbuma Corienis."
    sael reflexion "Je t'en ai parlé à l'infirmerie. Ryn, tu en as déjà vu ?"
    ryn reflexion "Chez nous ? Oui, près des zones sèches. Enfin, je crois."
    noam neutre "Et sur le Conclave ?"
    ryn colere "Attends. Pourquoi tu me demandes ça à moi ?"
    $ showGroup([("lysa", "neutre", 0.22), ("ryn", "colere", 0.48), ("noam", "neutre", 0.74)])
    lysa reflexion "Parce qu'on cherche. On a aussi prévu de parler à Kael."
    ryn colere "Ouais, mais c'est nous les premiers, hein ?"
    noam fatigue "Ryn, on a trouvé de la plante brûlée dans un conduit. Je veux juste savoir si tu connais ça."
    ryn colere "Et si je connais, quoi ? Je suis coupable ?"
    $ showGroup([("sael", "neutre", 0.22), ("ryn", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    sael raison "Il ne t'a pas accusé. Réponds à sa question."
    ryn fatigue "Non. J'en ai pas vu ici. Voilà."
    sael reflexion "Ce n'est pas une plante réservée à Limen. Et même si elle l'était, on reçoit des cargaisons de partout."
    noam raison "Tu as déjà utilisé ça pour soigner quelqu'un ?"
    sael neutre "Non. Certaines préparations irritent les voies respiratoires. Je ne vais pas faire semblant de connaître les dosages."
    ryn agace "Donc maintenant, je suis censé me souvenir de toutes les mauvaises herbes de mon district ?"
    lysa blase "Ce serait pratique, mais on va s'en passer."
    "Ryn se lève, manifestement furieux. Sael ne le retient pas."
    sael fatigue "Vous avez autre chose ?"
    noam reflexion "Oui. La plaque dans le conduit. Tu crois qu'elle a pu être posée avant l'échange des chambres ?"
    sael raison "Sans connaître les accès, je ne peux pas te dire quand. Mais si tu veux comprendre la mort de Tomas, c'est une question plus utile que de chercher qui a déjà vu cette plante."
    $ hideGroup()
    return

label _28_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.24), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    noam raison "Kael, regarde cette photo. C'est toi qui as installé cette plaque ?"
    kael surpris "Quoi ? Non. Attends..."
    "Il agrandit l'image, puis pose sa tablette."
    kael reflexion "Nous, on a fixé des protections devant les grilles. Pas ça. Cette plaque est dans le réseau lui-même."
    lysa reflexion "Et elle renvoie l'air vers une seule chambre."
    kael reflexion "Oui. C'est du bricolage, mais ça peut marcher."
    noam inquiet "Qui peut entrer dans cette branche ?"
    kael neutre "Ceux qui ont accès à la maintenance. Et je parle pas seulement de moi. On a déplacé des outils là-dedans plusieurs fois."
    lysa reflexion "Le journal des entrées ?"
    kael raison "Je peux essayer de le récupérer. Mais il y a plusieurs lecteurs, et ils ne conservent pas tous la même chose."
    noam raison "Tu penses que le montage a été posé récemment ?"
    kael reflexion "Sur photo, impossible de dater ça. Et ne me demande pas une heure, j'en sais rien."
    lysa blase "On peut au moins exclure que ce soit une pièce normale ?"
    kael neutre "Oui. Ça, je peux te le dire."
    noam reflexion "Et tu connais le Bulbuma ?"
    kael calme "De nom. On a des plantes de ce genre dans certains secteurs d'Orbite. Mais pour l'espèce exacte, demande à quelqu'un d'autre."
    noam raison "Préviens-moi si tu retrouves les heures de passage."
    kael neutre "D'accord. Je regarde ça."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_GRILLE:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam reflexion "On avait regardé cette grille le premier jour. Elle n'a pas bougé."
    lysa neutre "Oui. Mais ce qu'on a trouvé était plus loin dans le conduit."
    noam raison "Donc quelqu'un pouvait toucher à cette plaque depuis la maintenance, sans passer par la chambre."
    lysa inquiet "Ça me plaît pas du tout."
    "Je photographie une nouvelle fois les fixations. Elles ont l'air intactes."
    $ hideGroup()
    call investigation_take_manual_photo("j28_photo_grille", "j26_elen_vide", (0.625, 0.17), 2.9) from _call_j28_grille_photo
    return

label _28_0_1_1_0_1_PA_FLACON:
    scene j26_elen_vide at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.35), ("noam", "reflexion", 0.69)])
    noam raison "Le flacon avait l'air tellement évident, le jour où on l'a trouvé."
    lysa reflexion "Tu crois que quelqu'un l'a mis exprès ?"
    noam fatigue "Je sais pas. Mais il n'explique pas la plaque et les trucs brûlés."
    lysa reflexion "Ouais. Et Iris a jamais dit qu'il avait pris ces comprimés."
    noam neutre "Je vais noter cette contradiction. Pas plus."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "fatigue", 0.20), ("iris", "reflexion", 0.45), ("noam", "neutre", 0.72)])
    noam reflexion "Vous avez pu comparer les symptômes de Tomas avec ce qu'on a trouvé ?"
    sael raison "Oui. Et ça reste compatible avec une intoxication. Mais ce n'est pas une preuve que le bol l'a tué."
    iris fatigue "La fiche que j'ai trouvée décrit des réactions proches. Le problème, c'est qu'on n'a pas identifié ce qu'il y avait vraiment dans le récipient."
    noam raison "Donc on peut parler d'un dispositif suspect. Pas annoncer la cause exacte."
    sael neutre "Voilà."
    iris agace "C'est fou, il nous écoute parfois."
    noam taquin "Très drôle."
    sael inquiet "Et ne laisse personne aller retirer le bol pour le montrer aux autres. Il faut conserver ce qu'on a trouvé."
    $ hideGroup()
    return

label _28_0_1_1_0_1_PA_ANALYSE:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    "Iris me montre la photo du fragment, à côté d'une fiche botanique. Sael observe les deux images."
    $ showGroup([("sael", "reflexion", 0.19), ("iris", "neutre", 0.46), ("noam", "neutre", 0.73)])
    noam reflexion "C'est vraiment la même plante ?"
    iris raison "Ça y ressemble. Mais regarde, celle d'à côté aussi. Elles se ressemblent presque toutes sur une photo comme ça."
    sael neutre "Et une plante chauffée n'a pas forcément les mêmes effets qu'une plante fraîche."
    noam fatigue "Donc on ne peut pas dire que ça vient de Limen."
    sael raison "Non. Et on ne sait même pas encore quelle espèce c'est."
    iris neutre "Je garde ces deux fiches. Si on retrouve un vrai échantillon exploitable, on pourra comparer."
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
    "Julian remue son café depuis un bon moment. Quand je m'assois, il pose enfin sa cuillère."
    julian fatigue "Kael m'a raconté pour le conduit. C'est vrai ?"
    noam raison "La plaque et le bol, oui. Pour le reste, Sael continue les examens."
    julian reflexion "Putain... Et moi qui étais sûr qu'il avait pris ces comprimés."
    noam neutre "Tu pouvais pas savoir."
    julian colere "Si. J'aurais surtout pu l'écouter deux minutes, au lieu de lui hurler dessus."
    noam inquiet "Julian..."
    julian fatigue "Je l'ai vu pleurer. Je me suis dit qu'il avait craqué. C'était tellement simple comme explication."
    noam raison "Être mal ne veut pas dire qu'on veut mourir."
    julian triste "Ouais. Je comprends, maintenant."
    "Il serre sa tasse au point que ses doigts blanchissent."
    julian inquiet "Tu crois que quelqu'un a fait ça exprès ?"
    noam reflexion "Je crois que quelqu'un a installé le dispositif. Pourquoi, et pour qui, je sais pas."
    julian determine "Alors trouve-le. Parce que si on repart sans savoir..."
    noam neutre "Je cherche, Julian."
    julian fatigue "Je sais. Désolé."
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
    "Nyra nous retrouve près de la porte. Elle regarde les photographies sans rien dire pendant quelques secondes."
    $ showGroup([("nyra", "inquiet", 0.26), ("lysa", "neutre", 0.50), ("noam", "neutre", 0.74)])
    nyra surpris "Un récipient brûlé ? Dans la ventilation ?"
    noam raison "Avec une plaque qui dirigeait l'air vers la chambre d'Elen."
    nyra reflexion "C'est quand même très étrange."
    lysa reflexion "Sael pense qu'une intoxication est possible."
    nyra inquiet "Merde..."
    noam reflexion "On n'a pas réussi à savoir quand le montage a été installé."
    nyra raison "Donc on ignore si la personne qui l'a posé savait que Tomas dormirait dans cette chambre."
    lysa inquiet "Ouais."
    if "livraisons" in investigation_pa_completed:
        noam raison "J'ai regardé les livraisons. Rien qui permette de retracer le récipient."
        nyra neutre "Je vais reprendre les lots avec les documents d'Orbite. Il y a peut-être une référence qu'on a ratée."
    else:
        nyra neutre "Je peux regarder les livraisons. J'ai déjà parcouru ces registres pour les recherches sur Keyper."
    if "limen" in investigation_pa_completed:
        lysa fatigue "Ryn a pas apprécié qu'on lui parle du Bulbuma."
        nyra neutre "Je peux le comprendre. Il va falloir éviter que tout le monde se saute dessus."
    noam raison "Sael veut présenter les résultats au groupe."
    nyra reflexion "Elle a raison. Mais annoncez bien ce qui est certain. Sinon la soirée va être longue."
    lysa blase "À mon avis, elle le sera quand même."
    nyra neutre "Je vais consulter les archives. On se retrouve au Conclave."
    "Elle s'éloigne. Lysa reste un moment devant les photos."
    lysa inquiet "Ça va partir en vrille."
    noam fatigue "Ouais. Je sais."
    $ hideGroup()
    jump _28_0_1_1_0_1_REUNION

label _28_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    "Quand j'entre au Conclave, presque tout le monde est déjà là. Personne n'a touché à la place de Tomas."
    "Julian est debout derrière son siège. Elen regarde le pupitre vide. Ryn a les bras croisés et l'air de vouloir être n'importe où ailleurs."
    $ showGroup([("sael", "reflexion", 0.07), ("iris", "fatigue", 0.21), ("elen", "triste", 0.35), ("noam", "neutre", 0.49), ("julian", "fatigue", 0.63), ("ryn", "fatigue", 0.77), ("nyra", "neutre", 0.91)])
    sael raison "Bon. Je vais pas tourner autour du pot. On a trouvé quelque chose dans la ventilation de la chambre d'Elen."
    julian inquiet "Quel genre de chose ?"
    noam raison "Une plaque qui détourne l'air et un récipient avec des restes brûlés. C'était caché dans le conduit."
    elen surpris "Dans MA chambre ?"
    lysa reflexion "Dans le conduit qui y mène. Il y avait des fragments de plante dedans."
    sael reflexion "Certains symptômes de Tomas sont compatibles avec une intoxication par inhalation. Ça ne me suffit pas à confirmer la cause de sa mort."
    julian colere "Mais le bol, il a pas poussé tout seul !"
    kael raison "Non. C'est une installation qui n'existe pas sur les plans."
    elen peur "Attendez. Donc... quelqu'un aurait pu mettre un truc là-dedans, et je l'aurais respiré en dormant ?"
    sael raison "C'est possible."
    elen colere "C'est tout ce que tu peux me dire ?"
    sael inquiet "Elen, je sais que ça fait peur. Je préfère te dire ce que je sais plutôt que d'inventer."
    "Elen se lève. Sa chaise recule d'un coup."
    elen colere "Mais c'était MA chambre ! C'est moi qui lui ai dit d'y aller !"
    noam inquiet "Elen, attends..."
    elen triste "Non. Vous comprenez pas ? Si on avait pas échangé, c'est moi qui aurais dormi là !"
    pause 0.5
    "Julian cesse de bouger. Même Ryn ne dit plus rien."
    nyra reflexion "On ne sait pas encore quand le dispositif a été installé."
    elen surpris "Quoi ?"
    noam raison "C'est le problème. S'il était déjà là avant l'échange, tu aurais pu être visée. S'il a été installé après, quelqu'un savait que Tomas dormirait chez toi."
    elen peur "Mais... il y avait des gens dans le couloir quand on en a parlé."
    julian inquiet "Qui ?"
    elen fatigue "J'en sais rien ! Je l'ai déjà dit ! Il voulait pas retourner dans sa chambre, alors j'ai proposé la mienne. J'ai pas pris la liste des gens qui passaient !"
    julian colere "Et personne a rien remarqué ? Personne ?"
    lysa colere "Julian. Arrête de lui tomber dessus."
    julian colere "Je lui tombe pas dessus ! J'essaie de comprendre !"
    elen colere "Bah moi aussi !"
    "Elen se rassoit brusquement. Elle essuie son visage avec sa manche."
    iris fatigue "On va tous se calmer deux secondes. Et le flacon de somnifères, on n'a toujours pas prouvé que Tomas avait pris quoi que ce soit."
    julian triste "Super. Donc il s'est peut-être pas suicidé. Il s'est peut-être fait tuer pendant que je pensais que..."
    "Il s'arrête. Personne ne termine sa phrase à sa place."
    ryn agace "Et maintenant, vous allez accuser qui ?"
    noam reflexion "Personne, tant qu'on n'a pas recoupé les indices."
    if "limen" in investigation_pa_completed:
        ryn colere "Pourtant, vous êtes venus me parler de cette putain de plante."
    else:
        ryn colere "Cette plante vient de Limen, c'est ça ? Parce que je vous vois venir."
    sael neutre "On en trouve aussi ailleurs. Et on ne sait même pas si les fragments viennent bien de cette espèce."
    ryn colere "Voilà. Mais c'est quand même mon district qu'on regarde !"
    julian determine "Ryn, personne n'a dit que tu l'avais tué. Mais je vais pas ignorer une piste juste parce que ça te vexe."
    ryn colere "Répète ça."
    $ showGroup([("ryn", "colere", 0.18), ("julian", "determine", 0.40), ("sael", "neutre", 0.63), ("noam", "inquiet", 0.84)])
    "Ryn se lève. Julian ne recule pas."
    sael determine "Ryn. Assieds-toi."
    ryn colere "Laisse-moi."
    sael raison "Je te demande de t'asseoir."
    "Ryn finit par tirer sa chaise. Le bruit résonne dans toute la salle."
    $ showGroup([("nyra", "neutre", 0.14), ("kael", "reflexion", 0.33), ("lysa", "neutre", 0.52), ("noam", "neutre", 0.71), ("julian", "fatigue", 0.90)])
    kael raison "Pour la plaque, un accès de maintenance suffit. Pas besoin d'ouvrir la porte d'Elen."
    julian reflexion "Et combien de personnes ont accès à la maintenance ?"
    kael fatigue "Plusieurs. Pas juste moi et Elias."
    julian colere "C'est pas une réponse."
    kael neutre "C'est la seule que je peux te donner aujourd'hui."
    if "acces" in investigation_pa_completed:
        noam raison "J'ai regardé les journaux avec Elias. Il manque une partie des données de cette nuit-là."
        kael reflexion "Je vais tenter de récupérer ce que le lecteur local a gardé."
    else:
        kael raison "Je vais vérifier les journaux des lecteurs. J'aurai peut-être des heures de passage."
    if "livraisons" in investigation_pa_completed:
        noam raison "Et les registres de livraison sont incomplets. On ne sait pas d'où vient le bol."
    nyra raison "Je peux reprendre les registres. Mais il faudrait aussi vérifier les badges de maintenance."
    julian reflexion "Et si le responsable est dans cette salle ? On va tous le laisser se promener tranquillement ?"
    lysa reflexion "Tu proposes quoi ? Qu'on s'enferme chacun dans sa chambre ?"
    julian colere "Je propose qu'on arrête de faire comme si on avait juste perdu une caisse de nourriture !"
    elen fatigue "Vous pourriez arrêter de vous engueuler ? Juste ce soir ?"
    pause 0.4
    "Personne ne répond tout de suite."
    if "julian" in investigation_pa_completed:
        julian triste "J'ai déjà dit à Noam que j'avais eu tort sur les somnifères. Mais ça veut pas dire que je vais laisser tomber."
    else:
        julian triste "J'étais persuadé qu'il s'était suicidé. Je lui ai même pas laissé le temps de m'expliquer avant..."
    julian fatigue "Merde."
    sael raison "Écoutez. On garde le bol en place, on conserve les prélèvements, et personne ne touche au réseau sans prévenir. Je continuerai l'examen."
    kael neutre "Je m'occupe des journaux."
    nyra raison "Et moi des cargaisons."
    noam raison "Demain, on reprend la chronologie. L'échange des chambres, les accès et ce que Tomas cherchait avant de mourir."
    elen triste "Moi, je retourne pas dormir dans cette chambre."
    lysa inquiet "Tu peux rester avec moi."
    elen fatigue "Ouais... Merci."
    "Elen quitte la table avec Lysa. Ryn part aussitôt après, sans un mot pour Julian."
    "En quelques minutes, la salle se vide. La chaise de Tomas reste là, exactement comme avant."
    $ hideGroup()
    jump _28_0_1_1_0_1_NUIT


label _28_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je suis encore couvert de poussière. J'ai pris une douche, mais il y a toujours un peu de gris sous mes ongles."
    "J'ouvre les photos de cet après-midi : la plaque, le bol noirci, les fragments. Puis celle de la chambre d'Elen, prise le jour où on a trouvé Tomas."
    "Je repense à Elen. Elle aurait pu dormir dans cette chambre. Ou quelqu'un a attendu de savoir que ce serait Tomas."
    noam fatigue "C'est pas la même histoire..."
    "Le flacon ne prouve toujours rien. Et les résidus non plus, à eux seuls. Mais ça ne ressemble plus du tout à la mort qu'on imaginait il y a deux jours."
    "Je rouvre le dossier Keyper-IIB. Les unités ÉID-0, le livre sur la résonance Yanma et ce petit appareil que je n'ai jamais retrouvé."
    "Tomas voulait nous parler de tout ça. J'étais persuadé qu'il aurait le temps."
    "Je fais défiler les images jusqu'à la photo du récipient, prise avant qu'on touche à la plaque."
    "Sur le moment, je regardais les cendres. Là, je remarque surtout la surface autour : une trace claire, le fond du bol noirci, et juste à côté une partie restée presque propre."
    "Je zoome. Ce n'est peut-être qu'une marque laissée pendant l'installation. Ou pendant qu'on a déplacé la plaque."
    noam reflexion "Attends..."
    "Je compare les deux clichés. Il y a une chose que je n'arrive pas à déterminer : est-ce que le récipient est resté exactement au même endroit tout le temps ?"
    "Je pourrais essayer de le deviner pendant des heures. Ça ne me donnera ni l'heure où il a été installé, ni celle où il a servi."
    "Mais si le montage a été préparé avant l'échange des chambres, on cherche peut-être la mauvaise cible depuis le début."
    pause 0.5
    "Je reviens au dernier message de Tomas. « On se voit demain. »"
    "Je laisse la conversation ouverte sur la tablette."
    "Demain, il faudra reprendre la chronologie depuis le début. Et cette fois, je demanderai à chacun ce qu'il faisait vraiment cette nuit-là."
    stop music fadeout 1.0
    call end_day("29", sleeping=True) from _call_j28a_end_day_29
    jump _29_0_1_1_0_1_REVEIL
