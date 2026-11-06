# INVESTIGATION À PA — J27. Les faits nécessaires au J29 restent obligatoires.
init 10 python:
    J27A_ROOMS = {
      "dortoir": {
        "title": "DORTOIRS — CHAMBRE DE TOMAS",
        "background": "bg_chambre_tomas",
        "description": "Les affaires de Tomas sont restées en place.",
        "actions": [
          "carnet",
          "grille"
        ]
      },
      "archive": {
        "title": "ARCHIVES",
        "background": "bg_archive",
        "description": "Historique des consultations de Tomas.",
        "actions": [
          "keyper",
          "quotas"
        ]
      },
      "observation": {
        "title": "OBSERVATION",
        "background": "bg_observation",
        "description": "Dernier endroit où Tomas a manipulé l'appareil.",
        "actions": [
          "signal",
          "camera"
        ]
      },
      "maintenance": {
        "title": "MAINTENANCE",
        "background": "bg_maintenance",
        "description": "Kael et Elias peuvent expliquer le matériel.",
        "actions": [
          "kael",
          "elias"
        ]
      },
      "infirmerie": {
        "title": "INFIRMERIE",
        "background": "infirmerie2",
        "description": "Iris poursuit ses analyses.",
        "actions": [
          "iris"
        ]
      },
      "repos": {
        "title": "SALLE COMMUNE",
        "background": "bg_repos",
        "description": "Ryn et Sael se souviennent du vote.",
        "actions": [
          "sael"
        ]
      },
      "cafeteria": {
        "title": "CAFÉTÉRIA",
        "background": "bg_cafeteria",
        "description": "Julian est resté près de la machine à café.",
        "actions": [
          "julian"
        ]
      },
      "conclave": {
        "title": "SALLE DU CONCLAVE",
        "background": "bg_conclave",
        "description": "Tomas a pris sa dernière décision ici.",
        "actions": []
      },
      "gymnase": {
        "title": "GYMNASE",
        "background": "bg_gymnase",
        "description": "Une salle presque déserte.",
        "actions": []
      }
    }
    J27A_ACTIONS = {
      "carnet": {
        "title": "Lire les annotations de Tomas",
        "description": "Parcourir des annotations personnelles sans déplacer le reste de ses affaires.",
        "label": "_27_0_1_1_0_1_PA_CARNET",
        "evidence": "j27_tomas_carnet"
      },
      "grille": {
        "title": "Vérifier la grille de la chambre",
        "description": "Comparer les protections avec celles de la chambre d'Elen.",
        "label": "_27_0_1_1_0_1_PA_GRILLE",
        "evidence": "j27_tomas_grille"
      },
      "keyper": {
        "title": "Vérifier le dossier Keyper",
        "description": "Contrôler les dates de consultation sans révéler la nature de la station.",
        "label": "_27_0_1_1_0_1_PA_KEYPER",
        "evidence": "j27_tomas_historique"
      },
      "quotas": {
        "title": "Chercher une définition des unités ÉID-0",
        "description": "Explorer les index accessibles de la station de production.",
        "label": "_27_0_1_1_0_1_PA_QUOTAS",
        "evidence": "j27_tomas_quotas"
      },
      "signal": {
        "title": "Examiner les journaux d'observation",
        "description": "Chercher une trace de l'appareil disparu, sans connaissance technique suffisante.",
        "label": "_27_0_1_1_0_1_PA_SIGNAL",
        "evidence": "j27_tomas_signal"
      },
      "camera": {
        "title": "Contrôler l'inventaire des appareils",
        "description": "Comparer la description de l'appareil avec les équipements officiels.",
        "label": "_27_0_1_1_0_1_PA_CAMERA",
        "evidence": "j27_tomas_inventaire"
      },
      "kael": {
        "title": "Demander à Kael ce qu'il sait de Yanma",
        "description": "Questionner Kael au sujet de l'appareil de Tomas et d'ÉID-0.",
        "label": "_27_0_1_1_0_1_KAEL",
        "evidence": "j27_tomas_kael"
      },
      "elias": {
        "title": "Interroger Elias sur les équipements déplacés",
        "description": "Vérifier qui range normalement les petits appareils en observation.",
        "label": "_27_0_1_1_0_1_PA_ELIAS",
        "evidence": "j27_tomas_elias"
      },
      "iris": {
        "title": "Demander à Iris si elle reconnaît ÉID-0",
        "description": "Confronter le registre de Tomas aux dossiers consultés à l'infirmerie.",
        "label": "_27_0_1_1_0_1_IRIS",
        "evidence": "j27_tomas_iris"
      },
      "sael": {
        "title": "Interroger Sael et Ryn",
        "description": "Demander ce qu'ils savent réellement de Keyper et des quotas.",
        "label": "_27_0_1_1_0_1_SAEL",
        "evidence": "j27_tomas_sael"
      },
      "julian": {
        "title": "Interroger Julian sur la décision de Tomas",
        "description": "Revenir sur sa colère et sur ce qu'il a compris du vote.",
        "label": "_27_0_1_1_0_1_PA_JULIAN",
        "evidence": "j27_tomas_julian"
      }
    }
    INVESTIGATION_ENTRIES.update({
        "j27_photo_yanma": {"category": "preuves", "title": "LIVRE — RÉSONANCE YANMA", "desc": "Tomas consultait un manuel sur les communications spatiales de faible intensité.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/bg_chambre_tomas.png"},
        "j27_photo_transport": {"category": "preuves", "title": "NOTES DE TRANSPORT DE TOMAS", "desc": "Photographie des documents consultés dans la chambre de Tomas.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_carnet": {"category": "preuves", "title": "CARNET DE TOMAS", "desc": "Photographie prise lors de l'inspection du carnet.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_grille_tomas": {"category": "preuves", "title": "FIXATIONS — CHAMBRE DE TOMAS", "desc": "Photographie des protections de l'aération de la chambre de Tomas.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_keyper": {"category": "preuves", "title": "DOCUMENTS — KEYPER-IIB", "desc": "Le registre de production de Keyper-IIB mentionne les unités ÉID-0 et des quotas inexpliqués.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/bg_chambre_tomas.png"},
        "j27_core_yanma": {"category": "preuves", "title": "LIVRE SUR LA RÉSONANCE YANMA", "desc": "Tomas conservait un livre décrivant des transmissions spatiales très faibles.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "CONFIRMÉ", "manual_only": True},
        "j27_core_eid": {"category": "anomalies", "title": "REGISTRE ÉID-0 / KEYPER-IIB", "desc": "Les relevés de production de Keyper-IIB mentionnent des unités ÉID-0 et des quotas sans expliquer leur nature.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "CONFIRMÉ", "manual_only": True},
        "j27_core_appareil": {"category": "preuves", "title": "APPAREIL DISPARU", "desc": "Le petit appareil examiné par Tomas au jour 25 ne se trouve plus au pupitre d'observation.", "day": "J27", "origin": "OBSERVATION", "status": "CONFIRMÉ", "manual_only": True},
        "j27_tomas_carnet": {"category": "evenements", "title": "ANNOTATIONS DE TOMAS", "desc": "Tomas notait encore des questions sur les trajets et effectifs de Keyper la veille de sa mort.", "day": "J27", "origin": "CHAMBRE", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_grille": {"category": "preuves", "title": "PROTECTIONS DES DORTOIRS", "desc": "Les deux chambres possèdent des grilles de protection comparables. Cela ne renseigne pas sur l'air circulant dans le réseau.", "day": "J27", "origin": "DORTOIRS", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_historique": {"category": "evenements", "title": "HISTORIQUE KEYPER", "desc": "Les recherches de Tomas sur Keyper-IIB se sont prolongées jusqu'au jour 25.", "day": "J27", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_quotas": {"category": "anomalies", "title": "UNITÉS ÉID-0 NON DÉFINIES", "desc": "Les index consultables ne précisent pas si les unités ÉID-0 correspondent à des personnes ou à des machines.", "day": "J27", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_signal": {"category": "anomalies", "title": "JOURNAUX D'OBSERVATION", "desc": "Les relevés généraux ne permettent pas d'identifier le petit appareil aperçu près de Tomas.", "day": "J27", "origin": "OBSERVATION", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_inventaire": {"category": "preuves", "title": "INVENTAIRE DE L'OBSERVATION", "desc": "Aucune référence évidente ne correspond à la description imprécise de l'appareil aperçu par Noam.", "day": "J27", "origin": "OBSERVATION", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_kael": {"category": "personnes", "title": "KAEL — TRANSMISSION YANMA", "desc": "Kael connaît la technologie Yanma de nom, mais ne reconnaît pas l'appareil décrit par Noam.", "day": "J27", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_elias": {"category": "personnes", "title": "ELIAS — MATÉRIEL D'OBSERVATION", "desc": "Elias déclare déplacer régulièrement de petits boîtiers, sans pouvoir identifier celui de Tomas.", "day": "J27", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_iris": {"category": "personnes", "title": "IRIS — CODE ÉID-0", "desc": "Iris croit avoir rencontré une désignation similaire, sans pouvoir confirmer le service d'origine.", "day": "J27", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_sael": {"category": "personnes", "title": "SAEL ET RYN — KEYPER", "desc": "Ni Sael ni Ryn ne disent connaître la signification des unités ÉID-0.", "day": "J27", "origin": "SALLE COMMUNE", "status": "À VÉRIFIER", "manual_only": True},
        "j27_tomas_julian": {"category": "personnes", "title": "JULIAN — MOTIF DU VOTE", "desc": "Julian savait que Tomas cherchait des anomalies de production, mais ne connaissait pas ses détails techniques.", "day": "J27", "origin": "CAFÉTÉRIA", "status": "À VÉRIFIER", "manual_only": True},
    })

# JOUR 27 — LES DERNIÈRES RECHERCHES
# Route de Tomas — uniquement les observations de Noam.
default j27a_yanma = False
default j27a_eid = False
default j27a_notes = False
default j27a_chambre = False
default j27a_iris = False
default j27a_kael = False
default j27a_sael = False
default j27a_appareil_absent = False

label _27_0_1_1_0_1_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Matin"
    $ j27a_yanma = False
    $ j27a_eid = False
    $ j27a_notes = False
    $ j27a_chambre = False
    $ j27a_iris = False
    $ j27a_kael = False
    $ j27a_sael = False
    $ j27a_appareil_absent = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Le rappel du vote me réveille. J'avais oublié de désactiver l'alarme."
    "Je regarde l'écran un moment avant de l'éteindre. Aujourd'hui, il devrait y avoir douze personnes autour de la table. Je sais déjà qui ne viendra pas."
    "J'ouvre mes notes : le flacon de médicaments, les draps trempés, le verrou intérieur, les premiers témoignages. Une quantité absurde de détails, et toujours aucune cause de décès."
    think "Tomas aurait repris chaque détail jusqu'à comprendre. Il détestait ne pas terminer ce qu'il avait commencé."
    "Sur ma dernière photo, il se penche sur une carte orbitale. Je lui avais demandé de m'expliquer plus tard. Maintenant, j'ai tout mon temps pour regretter."
    noam fatigue "Bon. On va au moins regarder ce que t'as laissé."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j27a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _27_0_1_1_0_1_CAFETERIA

label _27_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j27a_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Il reste plusieurs places libres. Celle de Tomas me saute aux yeux : personne n'y a posé son plateau."
    $ showGroup([("julian", "fatigue", 0.080), ("iris", "fatigue", 0.248), ("elen", "triste", 0.416), ("lysa", "blase", 0.584), ("noam", "neutre", 0.752), ("nyra", "neutre", 0.920)])
    julian reflexion "Iris, les analyses...?"
    iris fatigue "Toujours pas de cause de décès. Je te l'ai dit hier."
    julian fatigue "D'accord. Désolé."
    iris agace "Non, c'est moi. J'ai presque pas dormi."
    elen inquiet "Et le flacon ? On sait si les comprimés étaient à lui ?"
    iris raison "Non. Tant qu'on sait pas ce qu'il a pris, on arrête de parler d'une surdose comme si c'était établi."
    "Elen remue son déjeuner sans manger. Dès que la porte s'ouvre, elle lève la tête."
    lysa blase "Elen... Tu peux arrêter de regarder l'entrée."
    elen triste "Je sais qu'il viendra pas."
    lysa triste "Pardon. C'était idiot."
    julian fatigue "Il voulait encore me parler après le vote. Il m'avait écrit."
    noam inquiet "Tu lui as répondu ?"
    julian triste "Non."
    "Il pose sa tasse un peu trop fort. Personne ne relève."
    noam neutre "Elen, je voudrais retourner dans la chambre de Tomas. Celle où tu as dormi."
    elen surpris "Pour quoi faire ?"
    noam raison "Il cherchait encore des informations sur Keyper. Peut-être qu'il a laissé des notes."
    elen hesitation "J'ai pas déplacé ses papiers. Juste les draps, quand on a échangé."
    elen triste "Je lui avais proposé cet échange pour qu'il se repose. Je pensais lui rendre service..."
    noam inquiet "Tu pouvais pas prévoir ce qui allait se passer."
    elen colere "C'est ce que tout le monde me répète. Mais personne n'en sait rien !"
    pause 0.4
    nyra raison "Je peux accompagner Noam. On photographie les documents et on remet tout en place."
    noam neutre "D'accord."
    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonjour ! Aujourd'hui, c'est le jour du vote ! Enfin, ça aurait dû l'être."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais vous avez décidé de bouder tous ensemble. Comme c'est touchant !"
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Faute de participants, aucun nouveau Commandement ne sera adopté aujourd'hui. Toutes mes autres règles restent en vigueur, naturellement !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je vous souhaite une excellente journée libre. Essayez de ne pas trop vous ennuyer sans moi !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.080), ("iris", "fatigue", 0.248), ("elen", "triste", 0.416), ("lysa", "blase", 0.584), ("noam", "fatigue", 0.752), ("nyra", "neutre", 0.920)])
    iris agace "Elle pourrait fermer sa gueule cinq minutes."
    nyra neutre "Noam, on y va ?"
    noam neutre "Ouais."
    $ hideGroup()
    jump _27_0_1_1_0_1_CHAMBRE

label _27_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Nous passons devant la chambre d'Elen. C'est là qu'on a retrouvé Tomas, alors qu'il aurait dû dormir quelques portes plus loin."
    "Je ralentis, puis continue jusqu'à sa chambre avec l'accès qu'Elen nous a prêté."
    scene bg_chambre_tomas at adaptive_fullscreen with dissolve
    "Les étagères débordent d’ouvrages spécialisés, et son bureau est couvert de plans, de feuilles annotées et de piles de documents classés avec soin."
    $ showGroup([("nyra", "neutre", 0.37), ("noam", "reflexion", 0.68)])
    noam fatigue "Il serait capable de revenir pour nous demander de ne pas déplacer ses dossiers."
    nyra sourire "Et d'expliquer pendant dix minutes pourquoi leur ordre est important."
    "Je souris. Puis je réalise que nous parlons de lui au passé."
    nyra raison "On note ce qu'on touche. Si Iris doit revenir, elle saura ce qui a changé."
    noam neutre "D'accord. Je commence par le bureau."
    $ hideGroup()
    jump _27_0_1_1_0_1_FOUILLE

label _27_0_1_1_0_1_FOUILLE:
    menu:
        "Que regarder ?"
        "Les livres techniques" if not j27a_yanma:
            $ j27a_yanma = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Sur le coin gauche du bureau, un épais livre sur les transmissions spatiales est posé parmi les notes. Plusieurs pages sont marquées."
            noam reflexion "« Résonance Yanma — Transmissions à très faible intensité ». Ça te parle ?"
            nyra reflexion "De nom. C'est une méthode de transmission dans l'espace."
            noam neutre "Comment ça marche ?"
            nyra raison "On envoie des signaux très faibles. Difficiles à détecter sans un récepteur adapté. Mais je connais pas tous les détails."
            noam surpris "Pourquoi Tomas lisait ça ?"
            nyra neutre "Il cherchait des coordonnées orbitales. Peut-être qu'il a voulu comprendre un système."
            noam raison "Je prends une photo du livre."
            $ hideGroup()
            call investigation_take_manual_photo("j27_photo_yanma", "bg_chambre_tomas", (0.23, 0.73), 2.5) from _call_j27_photo_yanma
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Le registre de Keyper" if not j27a_eid:
            $ j27a_eid = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Je retrouve les relevés du jour 24, rangés avec un registre de production plus ancien."
            noam reflexion "Voilà. Keyper-IIB."
            "Une ligne indique « UNITÉS ÉID-0 — EFFECTIFS », suivie de chiffres. Plus bas, des quotas de production."
            noam surpris "Des effectifs ? On dirait qu'ils comptent des employés."
            nyra raison "Ou des machines. Dans les registres industriels, ce terme désigne parfois des unités automatisées."
            noam neutre "Et ici, il y a les quotas qu'on devait augmenter."
            "Tomas a écrit dans la marge : « ÉID-0 = personnes ? machines ? »"
            nyra neutre "Il n'avait pas encore la réponse."
            noam fatigue "Non. Mais il a voté contre à cause de ça."
            "Je photographie la page du registre qui mentionne les unités ÉID-0."
            $ hideGroup()
            call investigation_take_manual_photo("j27_photo_keyper", "bg_chambre_tomas", (0.27, 0.59), 2.35) from _call_j27_photo_keyper
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Je garde une copie du registre."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Ses notes de transport" if not j27a_notes:
            $ j27a_notes = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "neutre", 0.67)])
            "Les dernières feuilles contiennent des références orbitales et un tracé de trajet."
            noam reflexion "C'est ce qu'il m'avait montré. Keyper serait à quelques heures de vol."
            nyra raison "Si ses calculs sont bons. Il a entouré plusieurs positions possibles."
            noam neutre "Il avait encore des trucs à vérifier."
            nyra reflexion "Oui. On peut photographier ça aussi."
            "Je remarque trois questions sous le trajet : « Pourquoi station non déclarée ? », « Quels effectifs ? », « Accès aux quotas ? »"
            noam fatigue "Il a passé toute la journée là-dessus."
            $ hideGroup()
            call investigation_take_manual_photo("j27_photo_transport", "bg_chambre_tomas", (0.27, 0.65), 2.35) from _call_j27_transport_photo
            jump _27_0_1_1_0_1_FOUILLE
        "La porte et les accès" if not j27a_chambre:
            $ j27a_chambre = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "J'examine le verrou, puis la grille d'aération. Les fixations semblent intactes, mais j'ai appris à ne plus tirer de conclusion de ce seul détail."
            noam reflexion "Elen a dormi ici. Et Tomas s'est retrouvé dans sa chambre à elle."
            nyra neutre "Oui. On sait juste qu'ils ont échangé la veille."
            noam raison "Il faudrait vérifier qui connaissait l'échange, exactement."
            nyra reflexion "On pourra reprendre les témoignages. Il faut juste que chacun puisse préciser ce dont il se souvient."
            noam neutre "Ouais."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Terminer la fouille" if j27a_yanma and j27a_eid and j27a_notes and j27a_chambre:
            jump _27_0_1_1_0_1_APPAREIL
# Durée : ~3m30.

label _27_0_1_1_0_1_APPAREIL:
    $ showGroup([("nyra", "reflexion", 0.38), ("noam", "neutre", 0.68)])
    noam reflexion "Attends. Ce livre sur Yanma me rappelle un truc."
    nyra neutre "Quoi ?"
    noam raison "Le jour 25, Tomas manipulait un petit boîtier dans la salle d'observation. Une boîte métallique, avec un voyant. Il l'a posée quand je suis arrivé."
    nyra reflexion "Tu sais à quoi il servait ?"
    noam neutre "Non. Il avait pas l'air de savoir non plus."
    nyra raison "Alors autant voir s'il est toujours là. On saura au moins de quoi on parle."
    $ hideGroup()
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_j27a_door_3
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.68)])
    "Je retrouve le pupitre, le tiroir inférieur et la zone dégagée où Tomas avait posé sa boîte."
    noam reflexion "C'était ici."
    "Je soulève un dossier, vérifie derrière l'écran, puis ouvre chaque compartiment. Je regarde même l'espace entre le pupitre et le mur."
    nyra neutre "Tu cherches toujours l'appareil ?"
    noam inquiet "Il était là, je m'en souviens."
    "Je reviens au premier tiroir, que j'avais pourtant déjà vérifié."
    noam surpris "Il a disparu."
    nyra reflexion "Tu es sûr que Tomas l'avait laissé ici en partant ?"
    noam raison "Je l'ai vu le poser. Je sais pas ce qu'il en a fait après."
    $ j27a_appareil_absent = True
    nyra raison "Il a pu le reprendre. Ou quelqu'un a pu le ranger. Kael et Elias manipulent souvent le matériel de cette salle."
    noam reflexion "Mais pourquoi cet appareil-là ?"
    nyra neutre "On peut leur demander. Ce sera plus fiable qu'une supposition."
    noam raison "Et toi, tu saurais reconnaître un récepteur Yanma ?"
    nyra reflexion "Pas à partir de la description d'un voyant. Si on retrouve le modèle, je regarderai."
    "Je vérifie encore le meuble, sans rien découvrir. Deux jours plus tôt, je n'avais même pas songé à prendre l'objet en photo."
    $ hideGroup()
    jump _27_0_1_1_0_1_QUESTIONS

label _27_0_1_1_0_1_QUESTIONS:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "J'ai les documents de Tomas, mais il manque toujours l'appareil. Si je veux avancer, il faut confronter ce que j'ai trouvé à ce que les autres savent."
    $ showGroup([("nyra", "neutre", 0.33), ("noam", "fatigue", 0.69)])
    noam raison "Je vais vérifier les accès et parler à quelques personnes. On a trop d'hypothèses."
    nyra raison "Note séparément ce que tu as vu et ce qu'on t'a raconté. Sinon, on finira par confondre les deux."
    noam reflexion "Tu viens ?"
    nyra neutre "Je vais reprendre les copies de Keyper. On gagnera du temps en se répartissant les recherches."
    noam neutre "On se retrouve avant la réunion."
    "J'ai le temps de vérifier cinq pistes. À moi de choisir lesquelles."
    $ investigation_pa_begin(27, 5)
    $ investigation_unlocked = True
    $ investigation_add("j27_core_yanma", notify=False)
    $ investigation_add("j27_core_eid", notify=False)
    $ investigation_add("j27_core_appareil", notify=False)
    $ free_time_active = False
    $ conclave_lock = False
    $ dortoir_lock = False
    $ exploration_libre_active = True
    $ exploration_libre_allowed_rooms = list(J27A_ROOMS.keys())
    $ current_scene_active = None
    $ corridor_current = "dortoir"
    $ hideGroup()
    jump _27_0_1_1_0_1_PA_MAP

label _27_0_1_1_0_1_PA_MAP:
    # Compatibilité avec les anciens jumps et sauvegardes.
    jump _27_0_1_1_0_1_PA_CORRIDORS

label _27_0_1_1_0_1_PA_CORRIDORS:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_j27a_pa_corridors
    $ investigation_pa_current_room = _return
    if investigation_pa_current_room not in J27A_ROOMS:
        jump _27_0_1_1_0_1_PA_CORRIDORS
    jump _27_0_1_1_0_1_PA_ROOM

label _27_0_1_1_0_1_PA_ROOM:
    call screen investigation_pa_room(investigation_pa_current_room, J27A_ROOMS, J27A_ACTIONS)
    if _return == "finish":
        jump _27_0_1_1_0_1_PA_FIN
    if _return == "corridors":
        call EXIT_ROOM_TO_CORRIDOR from _call_j27a_pa_exit_room_native
        jump _27_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_selected = _return
    if not investigation_pa_can_take(investigation_pa_selected):
        jump _27_0_1_1_0_1_PA_ROOM
    call INVESTIGATION_PA_CHOICE(J27A_ACTIONS[investigation_pa_selected], investigation_pa_current_room) from _call_j27a_pa_choice_native
    if not _return:
        jump _27_0_1_1_0_1_PA_ROOM
    if not investigation_pa_spend(investigation_pa_selected):
        jump _27_0_1_1_0_1_PA_ROOM
    call expression J27A_ACTIONS[investigation_pa_selected]["label"] from _call_j27a_pa_dynamic
    $ investigation_add(J27A_ACTIONS[investigation_pa_selected]["evidence"])
    if investigation_pa_remaining == 0:
        "Les cinq actions du jour sont utilisées. Je fais le point avant la réunion."
        jump _27_0_1_1_0_1_PA_FIN
    jump _27_0_1_1_0_1_PA_ROOM

label _27_0_1_1_0_1_PA_FIN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    if investigation_pa_remaining > 0:
        "Je m'arrête avant de dépenser toutes mes actions. J'ai besoin de laisser un peu de temps aux autres, et à moi aussi."
    jump _27_0_1_1_0_1_NYRA

label _27_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.38), ("noam", "neutre", 0.68)])
    noam raison "Tu connais la résonance Yanma ?"
    kael reflexion "Un peu. C'est des transmissions très faibles, non ?"
    noam neutre "Tomas avait un livre dessus. Et je l'ai vu avec un appareil dans la salle d'observation."
    kael reflexion "Quel appareil ?"
    noam raison "Une boîte métallique. Un voyant. Petit format."
    kael fatigue "Noam... Tu me décris la moitié des appareils du Conclave."
    noam agace "Ouais, je sais."
    kael neutre "Je dis pas ça pour me foutre de toi. Mais je peux pas reconnaître un modèle comme ça."
    noam reflexion "Tu l'as déplacé récemment ?"
    kael neutre "Non. Elias range parfois les équipements là-bas, tu peux lui demander."
    noam raison "Et ÉID-0, ça te parle ?"
    kael reflexion "Non. Ça ressemble à un code interne de Kami."
    noam fatigue "OK. Merci."
    $ hideGroup()
    return

label _27_0_1_1_0_1_SAEL:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.21), ("ryn", "fatigue", 0.46), ("noam", "neutre", 0.70)])
    noam neutre "Tomas avait un registre sur Keyper-IIB. Vous connaissez ces unités ÉID-0 ?"
    ryn reflexion "C'est quoi, encore, ce truc ?"
    noam raison "Je sais pas. Des effectifs. Des quotas."
    sael reflexion "Je ne connais pas cette désignation."
    ryn agace "Et c'est toujours ça qui l'a poussé à voter contre ?"
    noam fatigue "Oui."
    ryn colere "Putain. Tout ça, et maintenant il est mort..."
    sael neutre "Ryn, ça suffit."
    ryn fatigue "Je sais. Pardon."
    noam reflexion "Vous pensez que Kami nous laisserait accéder aux dossiers ?"
    sael raison "Elle a déjà refusé. Mais tu peux demander."
    noam neutre "Ouais."
    $ hideGroup()
    return

label _27_0_1_1_0_1_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    $ showGroup([("iris", "fatigue", 0.37), ("noam", "neutre", 0.68)])
    iris fatigue "Si tu viens pour les résultats de Tomas, j'ai rien de plus."
    noam raison "Non. Regarde ce registre."
    "Je lui tends la copie. Elle s'arrête au milieu de la page."
    iris surpris "Attends... Où t'as trouvé ça ?"
    noam reflexion "Dans sa chambre. Pourquoi ?"
    iris reflexion "ÉID-0... Ça vient de quel service ?"
    noam neutre "Du registre de Keyper. Tu connais ?"
    iris hesitation "Je sais pas. J'ai l'impression d'avoir vu un code du genre dans un document technique."
    noam surpris "Quel document ?"
    iris fatigue "J'en sais rien ! Je viens de passer la nuit sur des dossiers médicaux, Noam."
    noam agace "Tu m'as quand même demandé où je l'avais trouvé."
    iris agace "Parce que c'est bizarre, cette histoire d'effectifs ! Mais je sais pas ce que c'est. J'essaie de me rappeler !"
    pause 0.3
    iris fatigue "Pardon. J'ai pas dormi."
    noam neutre "C'est bon."
    iris raison "Laisse-moi la copie. Je vais regarder si le code apparaît quelque part."
    noam reflexion "Tu crois qu'il y a un lien avec ce que j'ai vu dans la maintenance ? Avec Mara ?"
    iris inquiet "Noam... On y est retournés ensemble. Le corps n'y était plus."
    noam fatigue "Je sais."
    iris raison "Je dis pas que t'as tout inventé. Mais là, avec Tomas, on a vraiment un corps. C'est pas la même chose."
    noam neutre "Ouais."
    iris fatigue "Je t'appellerai si je trouve quelque chose. Maintenant, va manger."
    $ hideGroup()
    return


label _27_0_1_1_0_1_PA_CARNET:
    scene bg_chambre_tomas at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je retrouve un carnet glissé derrière les dossiers. Des rendez-vous, des calculs, des listes de vérification : rien qui ressemble à une lettre d'adieu."
    "À la dernière page, Tomas a écrit « Keyper » et « revoir les chiffres ». Une ligne a été barrée si fort que le papier est marqué de l'autre côté."
    noam reflexion "Qu'est-ce que tu voulais vérifier ?"
    "Je passe le doigt au-dessus du trait sans toucher l'encre. Les mots sont illisibles, mais il avait clairement prévu de poursuivre son travail."
    "Je photographie le carnet à sa place. Il ne donne aucune réponse sur sa mort ; il contredit au moins l'idée qu'il avait cessé de chercher."
    call investigation_take_manual_photo("j27_photo_carnet", "bg_chambre_tomas", (0.28, 0.65), 2.35) from _call_j27_carnet_photo
    return

label _27_0_1_1_0_1_PA_GRILLE:
    scene bg_chambre_tomas at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Dans la chambre de Tomas, les fixations de la grille semblent anciennes et intactes. Je les photographie sans les dévisser."
    "Dans celle d'Elen, une tôle artisanale est clouée devant l'ouverture. Elle empêcherait un passage, mais pas la circulation de l'air."
    noam reflexion "Une porte verrouillée... et une chambre qui n'était pas complètement isolée."
    "Ce n'est pas une preuve que l'aération a servi à quoi que ce soit. C'est seulement une raison supplémentaire de ne pas considérer la porte comme une réponse définitive."
    call investigation_take_manual_photo("j27_photo_grille_tomas", "bg_chambre_tomas", (0.67, 0.14), 2.5) from _call_j27_grille_photo
    return

label _27_0_1_1_0_1_PA_KEYPER:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je consulte l'historique des documents ouverts par Tomas. Les recherches sur Keyper-IIB se prolongent jusqu'au jour 25."
    "Les intitulés changent : trajectoires, ravitaillement, registres de production. Il ne relisait pas simplement le même fichier ; il essayait de vérifier ses hypothèses par plusieurs sources."
    noam raison "Tu voulais comprendre exactement ce qu'on nous demandait d'approuver."
    "Je conserve les dates. Elles ne révèlent pas la cause de sa mort, mais elles montrent qu'il n'avait pas abandonné son enquête."
    return

label _27_0_1_1_0_1_PA_QUOTAS:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je parcours les index de production. Il y a des références de conteneurs, des machines, du fret... mais aucune définition claire des unités ÉID-0."
    "Une chose me frappe : le registre présente les « effectifs » et les quotas côte à côte, comme si l'un déterminait l'autre."
    noam reflexion "Des effectifs pour produire davantage... C'est ça qui t'inquiétait, Tomas ?"
    "Ça ne prouve pas qu'il s'agisse de personnes. En revanche, il faudra demander pourquoi cette catégorie n'est expliquée nulle part dans les documents accessibles."
    return

label _27_0_1_1_0_1_PA_SIGNAL:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Les journaux de la console comportent des heures de connexion, des interruptions et des relevés d'interférences. Une partie des valeurs est impossible à interpréter sans connaître l'appareil."
    noam reflexion "Si je retrouve ce boîtier, au moins je pourrai comparer les heures."
    "Je sauvegarde les lignes utiles. Je n'ai pas découvert un signal mystérieux : seulement une façon concrète de vérifier un appareil si nous le retrouvons."
    return

label _27_0_1_1_0_1_PA_CAMERA:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "L'inventaire officiel propose une série de capteurs presque identiques. Certains ressemblent vaguement à mon souvenir, mais aucun ne correspond avec certitude."
    "Je remarque aussi que la liste concerne le matériel attribué à cette salle. Elle ne recense pas forcément les objets qu'un représentant apporte lui-même."
    noam raison "Donc même si la boîte n'est pas sur la liste, ça ne veut pas dire que je l'ai imaginée."
    "J'enregistre les références possibles pour les soumettre à quelqu'un de plus compétent."
    return

label _27_0_1_1_0_1_PA_ELIAS:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.36), ("noam", "neutre", 0.68)])
    noam reflexion "Elias, tu ranges parfois les petits appareils de l'observation ?"
    elias neutre "Ouais, quand ça traîne. Sinon on finit par casser un truc."
    noam raison "T'as déplacé une petite boîte métallique avec un voyant depuis le jour 25 ?"
    elias surpris "Merde, Noam, ça décrit la moitié des machins que je touche."
    noam fatigue "Je sais. J'ai rien de mieux."
    elias reflexion "Je me rappelle pas l'avoir prise. Mais je te promets pas que j'ai rien rangé non plus."
    noam raison "Tu peux vérifier les bacs ?"
    elias neutre "Ouais. Par contre, venez pas dire que je l'ai volée si elle ressort pas."
    noam inquiet "Je t'accuse de rien."
    elias fatigue "Je sais. C'est juste que tout le monde commence à regarder les autres bizarrement depuis hier."
    $ hideGroup()
    return

label _27_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    $ showGroup([("julian", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    "Julian regarde une tasse presque pleine. Il ne semble pas avoir remarqué que son café a refroidi."
    noam raison "Tomas t'avait expliqué ce qu'il avait trouvé sur Keyper ?"
    julian reflexion "Il a essayé. Il voulait me montrer ses chiffres, me convaincre d'attendre avant de me prononcer."
    noam neutre "Et ?"
    julian fatigue "Je lui ai répondu que s'il avait quelque chose d'important à dire, il n'avait qu'à trouver le courage de le dire devant tout le monde."
    noam inquiet "Julian..."
    julian triste "Ouais. Je sais."
    "Il baisse la tête, puis reprend sans essayer de sourire."
    julian fatigue "Il m'a écrit après le vote. J'ai lu son message et je l'ai laissé sans réponse."
    noam raison "Tu pouvais pas prévoir ce qui allait lui arriver."
    julian colere "Ne me dis pas ça. Je sais. Ça change rien à ce que je lui ai dit."
    pause 0.4
    julian triste "Si tu trouves ce qu'il voulait me montrer, fais-moi au moins la faveur de me l'envoyer."
    noam neutre "Je le ferai."
    $ hideGroup()
    return

label _27_0_1_1_0_1_NYRA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Je retrouve Nyra avec deux plateaux. Elle pousse le second vers moi sans commentaire."
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "fatigue", 0.68)])
    noam sourire "Tu m'as gardé à manger ?"
    nyra sourire "Il restait une portion. Tu réfléchiras mieux après avoir mangé."
    "Je pose la tablette entre nous et affiche les preuves recueillies."
    noam raison "Tout se mélange. La mort de Tomas, ses recherches sur Keyper, cet appareil... J'ai du mal à savoir ce qui a vraiment un lien."
    nyra reflexion "Peut-être qu'il y en a un. Mais ce ne serait pas la première fois que deux événements se suivent sans avoir la même cause."
    noam reflexion "Sauf que je refuse de classer ça comme un suicide."
    nyra raison "Et tu as raison de refuser une conclusion sans preuve. Ça marche aussi dans l'autre sens."
    if "kael" in investigation_pa_completed:
        noam reflexion "Kael connaît Yanma de nom, mais ne reconnaît pas la boîte. Il dit ne pas l'avoir déplacée."
        nyra neutre "Alors on garde son témoignage, sans lui faire dire davantage."
    if "elias" in investigation_pa_completed:
        noam raison "Elias ne se rappelle pas l'avoir rangée. Il doit vérifier ses bacs."
        nyra raison "Une incertitude honnête est plus utile qu'une certitude inventée."
    if "iris" in investigation_pa_completed:
        noam raison "Iris croit avoir déjà vu une désignation proche d'ÉID-0."
        nyra raison "Si elle retrouve la référence, on aura quelque chose à comparer."
    if "julian" in investigation_pa_completed:
        noam fatigue "Julian s'en veut d'avoir repoussé Tomas. Il ne savait pas ce qu'il voulait lui montrer."
        nyra neutre "La culpabilité n'est pas une preuve. Mais il pourra peut-être se souvenir de leur discussion."
    if "grille" in investigation_pa_completed:
        noam raison "Et la protection de l'aération dans la chambre d'Elen ne bloquait pas l'air."
        nyra reflexion "C'est important à noter. Pas assez pour conclure à une intervention par ce passage."
    noam inquiet "Le plus dur, c'est qu'on était tous là. Et maintenant chacun peut raconter quelque chose de différent."
    nyra raison "C'est pour ça que je préfère les faits matériels. Reprends les heures, les objets et les déplacements. Les intentions viendront après."
    noam fatigue "Tu crois qu'on trouvera quelque chose ?"
    nyra neutre "Je pense qu'on comprendra mieux si on arrête de chercher un coupable avant de savoir s'il y a eu un crime."
    pause 0.3
    noam neutre "D'accord. Je présenterai les documents sans accuser personne."
    nyra sourire "C'est tout ce que je te demande."
    "Je mange pendant qu'elle classe les copies en deux dossiers : les travaux sur Keyper d'un côté, les circonstances de la mort de Tomas de l'autre. L'ordre me semble raisonnable, alors je le conserve."
    $ hideGroup()
    jump _27_0_1_1_0_1_REUNION

label _27_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    "Nous nous réunissons autour de la table. La place de Tomas est vide, mais personne n'a demandé à retirer sa tablette du pupitre."
    $ showGroup([("julian", "fatigue", 0.080), ("elen", "triste", 0.248), ("noam", "neutre", 0.416), ("lysa", "blase", 0.584), ("iris", "fatigue", 0.752), ("nyra", "neutre", 0.920)])
    julian reflexion "On peut faire le point ? Pas pour tirer une conclusion. Pour savoir ce qu'on fait maintenant."
    elen inquiet "Iris n'a toujours pas la cause de sa mort."
    iris fatigue "Et je ne vais pas l'inventer parce que vous voulez tous dormir cette nuit."
    julian neutre "Je ne te demande pas ça."
    elen colere "Alors qu'est-ce que tu veux ? Qu'on dise qu'il a pris les comprimés et qu'on passe à autre chose ?"
    julian colere "Arrête de me faire dire ce que j'ai pas dit !"
    "Elen se lève si brusquement que sa chaise recule contre le sol."
    elen triste "C'est moi qui lui ai proposé d'échanger les chambres. S'il avait refusé, il aurait dormi dans la sienne."
    noam inquiet "Elen..."
    elen colere "Et surtout, ne me dites pas que c'est pas ma faute ! Vous en savez rien !"
    lysa triste "Non, on en sait rien. Mais ça marche aussi pour le contraire."
    pause 0.4
    "Elen se rassoit sans regarder personne. Julian fixe ses mains."
    iris raison "Voilà ce qu'on sait : un flacon de comprimés a été retrouvé. On ignore encore ce que Tomas a pris. On n'a ni preuve de suicide, ni preuve de meurtre."
    noam raison "J'ai retrouvé les dossiers de Tomas : Keyper-IIB, des effectifs appelés ÉID-0, des quotas de production et des trajectoires orbitales."
    julian reflexion "Il s'inquiétait vraiment de ce vote."
    noam neutre "Oui. Il avait aussi un livre sur la résonance Yanma, une méthode de transmission spatiale à faible intensité."
    noam raison "Le jour 25, je l'ai vu avec un petit appareil dans la salle d'observation. Aujourd'hui, il n'était plus à l'endroit où je l'avais vu."
    lysa surpris "L'appareil a disparu ?"
    noam reflexion "Je ne l'ai pas retrouvé. Mais je sais pas s'il était encore là quand Tomas est parti."
    julian colere "Et on va vraiment faire comme si ça n'avait aucune importance ?"
    nyra raison "Personne ne dit ça. On cherche juste à savoir si Tomas l'a emporté, si quelqu'un l'a rangé, ou s'il manque réellement."
    julian reflexion "Qui s'occupe de ces appareils ?"
    nyra neutre "Kael et Elias manipulent régulièrement le matériel de la salle. On peut commencer par vérifier avec eux."
    if "kael" in investigation_pa_completed:
        noam raison "Kael ne reconnaît pas l'appareil avec ma description. Il ne se souvient pas de l'avoir déplacé."
    if "elias" in investigation_pa_completed:
        noam raison "Elias n'est pas certain d'avoir touché cette boîte. Il doit vérifier les bacs."
        lysa blase "Donc si on résume, on cherche une petite boîte grise parmi cinquante petites boîtes grises."
    if "camera" in investigation_pa_completed:
        noam raison "Je n'ai trouvé aucun modèle correspondant avec certitude dans l'inventaire officiel."
        julian reflexion "Il aurait pu l'apporter lui-même."
        noam neutre "Oui. L'inventaire ne suffit pas à trancher."
    if "quotas" in investigation_pa_completed:
        noam raison "Les effectifs et les quotas figurent côte à côte dans le registre. Mais aucune définition d'ÉID-0 n'est accessible."
        elen inquiet "Alors il avait peut-être raison d'avoir peur de ce qu'on votait..."
    if "keyper" in investigation_pa_completed:
        noam raison "L'historique montre qu'il vérifiait encore plusieurs documents au jour 25. Ses recherches n'étaient pas terminées."
    if "grille" in investigation_pa_completed:
        noam raison "La protection d'aération de la chambre d'Elen bloquait le passage, pas entièrement le flux d'air."
        iris reflexion "Je le note. Mais ça ne dit pas ce qui s'est passé dans la chambre."
    if "julian" in investigation_pa_completed:
        julian triste "Il m'avait demandé de l'écouter. Je lui ai pas laissé le temps de m'expliquer. Je veux au moins comprendre ce qu'il avait trouvé."
    julian colere "Ce qui me rend fou, c'est qu'on parle tous de ce qu'on ne sait pas, comme si ça suffisait à finir la discussion !"
    elen colere "Parce qu'on a peur, Julian ! Tu crois que t'es le seul à ne pas dormir ?"
    "Julian ouvre la bouche, puis la referme. Il n'essaie pas de répondre."
    lysa reflexion "On devrait pouvoir se demander si quelqu'un lui a fait du mal sans devoir pointer du doigt la première personne qui passe."
    iris raison "Oui. Mais pas de procès improvisé avant les analyses. Si vous commencez à vous accuser entre vous, on n'obtiendra plus un seul témoignage fiable."
    nyra raison "Alors faisons simple. Chacun note ses derniers déplacements connus de Tomas et les documents restent accessibles à tous. Aucune accusation tant qu'on n'a rien de vérifiable."
    noam raison "Et on ne conclut pas au suicide à partir d'un flacon."
    iris neutre "Ça, je peux le soutenir."
    elen triste "Je voudrais juste qu'on arrête de parler de ma chambre comme si c'était une preuve contre moi."
    julian fatigue "T'es pas la seule à te répéter ce que t'aurais dû faire."
    "Il regarde le pupitre vide. Elen suit son regard, puis baisse les yeux."
    julian neutre "Noam, tu peux m'envoyer une copie des recherches de Tomas ?"
    noam neutre "Bien sûr."
    "La réunion se termine sans solution. Pour la première fois, cependant, personne ne parle du flacon comme d'une explication suffisante."
    $ hideGroup()
    jump _27_0_1_1_0_1_NUIT

label _27_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "J'envoie à Julian les documents que Tomas avait conservés. L'accusé de réception apparaît, mais Julian ne répond pas."
    "Je fais défiler mes photographies. Les relevés de Keyper-IIB, les effectifs ÉID-0, le livre sur Yanma. Et cette boîte que je n'ai pas retrouvée."
    "J'avais espéré comprendre pourquoi Tomas était mort. À la place, j'ai découvert qu'il cherchait encore des réponses, lui aussi."
    "Je repense à Elen qui n'a presque pas mangé, à Julian devant sa tasse froide, à la chaise que personne n'ose occuper."
    noam fatigue "On aurait dû t'écouter..."
    "Une photographie retient mon attention : le verrou et la grille d'aération. Le mot « fermée » me revient sans cesse, comme si une porte verrouillée expliquait automatiquement tout ce qu'il y avait derrière."
    think "Il faut que je retourne dans la chambre où on l'a trouvé. Pas pour prouver ce que j'imagine. Pour regarder ce qu'on a raté."
    "Je règle un rappel pour le lendemain. Cette fois, ce n'est pas pour un vote."
    stop music fadeout 1.0
    call end_day("28", sleeping=True) from _call_j27a_end_day_28
    jump _28_0_1_1_0_1_REVEIL

