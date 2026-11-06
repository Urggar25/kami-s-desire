# INVESTIGATION À PA — J27. Les faits nécessaires au J29 restent obligatoires.
init 10 python:
    J27A_ROOMS = {
      "dortoir": {
        "title": "DORTOIRS — CHAMBRE DE TOMAS",
        "background": "bg_chambre",
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
        "j27_photo_yanma": {"category": "preuves", "title": "LIVRE — RÉSONANCE YANMA", "desc": "Tomas consultait un manuel sur les communications spatiales de faible intensité.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/chambre1.png"},
        "j27_photo_transport": {"category": "preuves", "title": "NOTES DE TRANSPORT DE TOMAS", "desc": "Photographie des documents consultés dans la chambre de Tomas.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_carnet": {"category": "preuves", "title": "CARNET DE TOMAS", "desc": "Photographie prise lors de l'inspection du carnet.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_grille_tomas": {"category": "preuves", "title": "FIXATIONS — CHAMBRE DE TOMAS", "desc": "Photographie des protections de l'aération de la chambre de Tomas.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True},
        "j27_photo_keyper": {"category": "preuves", "title": "DOCUMENTS — KEYPER-IIB", "desc": "Le registre de production de Keyper-IIB mentionne les unités ÉID-0 et des quotas inexpliqués.", "day": "J27", "origin": "CHAMBRE DE TOMAS", "status": "PHOTOGRAPHIE", "manual_only": True, "photo_source": "images/background/scene/archive2.png"},
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
    "Je me réveille avec le rappel du vote du jour 27 sur ma tablette."
    "J'avais oublié de le désactiver. Après ce qui s'est passé hier, la dernière chose que je veux, c'est retourner voter."
    "Je fais défiler mes notes : le flacon de somnifères, les draps trempés, le verrou intérieur, les témoignages..."
    think "J'ai tout écrit. Et j'ai toujours aucune idée de ce qui lui est arrivé."
    "Je me rappelle Tomas devant ses cartes, dans la salle d'observation. Il avait passé sa dernière journée à chercher Keyper."
    noam fatigue "Bon. On va regarder ce qu'il a laissé."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j27a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _27_0_1_1_0_1_CAFETERIA
# Durée : ~1m00.

label _27_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j27a_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Il reste plusieurs places libres. Celle de Tomas me saute aux yeux."
    $ showGroup([("julian", "fatigue", 0.080), ("iris", "fatigue", 0.248), ("elen", "triste", 0.416), ("lysa", "blase", 0.584), ("noam", "neutre", 0.752), ("nyra", "neutre", 0.920)])
    julian reflexion "Iris, pour les analyses... T'as pu avancer ?"
    iris fatigue "Pas assez pour donner une cause de décès. On en a déjà parlé."
    elen inquiet "Et les médicaments ?"
    iris raison "On sait pas ce qu'il a pris. Je veux pas conclure à une surdose juste à cause d'un flacon."
    julian fatigue "Personne a dit qu'on devait conclure."
    lysa blase "C'est vrai. Pas aujourd'hui."
    noam neutre "Elen, je peux te demander un truc ?"
    elen neutre "Bien sûr."
    noam reflexion "Tu as dormi dans la chambre de Tomas. Je voudrais y retourner pour regarder ses notes. Il cherchait encore Keyper la veille."
    elen inquiet "Tu crois que tu vas trouver quelque chose ?"
    noam fatigue "Franchement, j'en sais rien. Mais je veux pas m'arrêter au flacon."
    elen neutre "Vas-y. J'ai rien déplacé là-bas à part les draps."
    nyra raison "Je peux t'accompagner, Noam. On prendra des photos de ce qu'on trouve."
    noam sourire "Merci."
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
    kami "Faute de participants, aucun nouveau Commandement ne sera adopté aujourd'hui. Je précise que cela ne suspend aucune de mes règles."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je vous souhaite une excellente petite journée de repos. Essayez de ne pas trop vous ennuyer sans moi !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.080), ("iris", "fatigue", 0.248), ("elen", "triste", 0.416), ("lysa", "blase", 0.584), ("noam", "fatigue", 0.752), ("nyra", "neutre", 0.920)])
    elen fatigue "Elle pourrait au moins nous laisser tranquilles."
    nyra neutre "On y va ?"
    noam neutre "Ouais."
    $ hideGroup()
    jump _27_0_1_1_0_1_CHAMBRE
# Durée : ~2m30.

label _27_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "On passe devant la chambre d'Elen. Je ralentis sans le vouloir, puis je continue."
    "Nous entrons dans celle de Tomas avec l'accès qu'Elen nous a prêté."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Les livres sont alignés. Les vêtements sont pliés. Il a même une pile de documents parfaitement droite sur le bureau."
    $ showGroup([("nyra", "neutre", 0.37), ("noam", "reflexion", 0.68)])
    noam reflexion "Tomas, quoi..."
    nyra sourire "On dirait qu'il va revenir dans deux minutes pour vérifier qu'on range bien."
    noam fatigue "Ouais."
    nyra raison "On examine ce qui concerne ses recherches, on photographie et on remet tout ?"
    noam neutre "C'est ça."
    $ hideGroup()
    jump _27_0_1_1_0_1_FOUILLE
# Durée : ~1m00.

label _27_0_1_1_0_1_FOUILLE:
    menu:
        "Que regarder ?"
        "Les livres techniques" if not j27a_yanma:
            $ j27a_yanma = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Un livre dépasse de l'étagère. Plusieurs pages sont marquées."
            noam reflexion "« Résonance Yanma — Transmissions à très faible intensité ». Ça te parle ?"
            nyra reflexion "De nom. C'est une méthode de transmission dans l'espace."
            noam neutre "Comment ça marche ?"
            nyra raison "On envoie des signaux très faibles. Difficiles à détecter sans un récepteur adapté. Mais je connais pas tous les détails."
            noam surpris "Pourquoi Tomas lisait ça ?"
            nyra neutre "Il cherchait des coordonnées orbitales. Peut-être qu'il a voulu comprendre un système."
            noam raison "Je prends une photo du livre."
            $ hideGroup()
            call investigation_take_manual_photo("j27_photo_yanma", "bg_chambre", (0.39, 0.49), 2.2) from _call_j27_photo_yanma
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
            nyra raison "Ou des machines. Certains services utilisent aussi ce mot pour des unités automatisées."
            noam neutre "Et ici, il y a les quotas qu'on devait augmenter."
            "Tomas a écrit dans la marge : « ÉID-0 = personnes ? machines ? »"
            nyra neutre "Il n'avait pas encore la réponse."
            noam fatigue "Non. Mais il a voté contre à cause de ça."
            "Je photographie la page du registre qui mentionne les unités ÉID-0."
            $ hideGroup()
            call investigation_take_manual_photo("j27_photo_keyper", "bg_chambre", (0.61, 0.59), 2.2) from _call_j27_photo_keyper
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
            call investigation_take_manual_photo("j27_photo_transport", "bg_chambre", (0.61, 0.59), 2.2) from _call_j27_transport_photo
            jump _27_0_1_1_0_1_FOUILLE
        "La porte et les accès" if not j27a_chambre:
            $ j27a_chambre = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Je regarde le verrou et la grille d'aération. Rien ne semble avoir bougé."
            noam reflexion "Elen a dormi ici. Et Tomas s'est retrouvé dans sa chambre à elle."
            nyra neutre "Oui. On sait juste qu'ils ont échangé la veille."
            noam raison "Il faudrait vérifier qui connaissait l'échange, exactement."
            nyra reflexion "On pourra reprendre les témoignages. Mais ne mélange pas les suppositions avec ce qu'on sait."
            noam neutre "Ouais."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Terminer la fouille" if j27a_yanma and j27a_eid and j27a_notes and j27a_chambre:
            jump _27_0_1_1_0_1_APPAREIL
# Durée : ~3m30.

label _27_0_1_1_0_1_APPAREIL:
    $ showGroup([("nyra", "reflexion", 0.38), ("noam", "neutre", 0.68)])
    noam reflexion "Attends. Ce livre sur Yanma me rappelle quelque chose."
    nyra neutre "Quoi ?"
    noam raison "Dans la salle d'observation, il tenait un petit appareil métallique. Il l'a posé quand je suis arrivé. Il y avait un voyant dessus."
    nyra surpris "Tu sais à quoi il servait ?"
    noam neutre "Non. Lui non plus, d'après ce qu'il m'a dit."
    nyra raison "Ça peut être une balise, un capteur, un boîtier de maintenance... Mais ça vaut le coup d'aller voir."
    noam sourire "On y va."
    $ hideGroup()
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_j27a_door_3
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.68)])
    noam raison "C'était là, près du pupitre."
    "Je regarde le dessus du meuble, puis les compartiments. L'appareil n'y est plus."
    noam surpris "Il a disparu."
    nyra reflexion "T'es sûr de l'endroit ?"
    noam agace "Oui ! Je l'ai vu le poser."
    $ j27a_appareil_absent = True
    nyra raison "Il a pu être rangé. Kael et Elias viennent ici pour le matériel."
    noam reflexion "Mais pourquoi celui-là ?"
    nyra neutre "Je sais pas. On peut leur demander."
    noam raison "Si c'était un émetteur Yanma, tu saurais le reconnaître ?"
    nyra reflexion "Pas à partir d'un voyant. Et sans l'appareil, encore moins."
    noam fatigue "J'aurais dû le prendre en photo."
    nyra sourire "Tu pouvais pas prévoir qu'on reviendrait chercher ce truc."
    "Je regarde encore une fois le meuble vide. Il y a deux jours, je me fichais complètement de cet objet."
    $ hideGroup()
    jump _27_0_1_1_0_1_QUESTIONS
# Durée : ~2m30.

label _27_0_1_1_0_1_QUESTIONS:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "J'ai pris les photos de ses livres et constaté que le petit appareil n'est plus en observation. Mais je ne sais toujours pas à quoi servait ce truc."
    $ showGroup([("nyra", "neutre", 0.33), ("noam", "fatigue", 0.69)])
    nyra raison "Tu veux continuer aujourd'hui ?"
    noam raison "Oui, mais pas passer la journée à poser les mêmes questions à tout le monde."
    nyra neutre "Alors fais comme hier. Cinq pistes, et tu peux circuler entre les salles."
    noam reflexion "Et si je trouve rien ?"
    nyra raison "On gardera ce qu'on a. Le livre et le registre existent, même si tu n'interroges personne d'autre."
    noam neutre "D'accord."
    "Je vérifie mon dossier. Le livre Yanma, le registre ÉID-0 et la disparition de l'appareil sont déjà notés : ces éléments ne me coûteront pas de point d'action."
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
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je retrouve un petit carnet coincé derrière ses dossiers. Rien d'extraordinaire : des heures de rendez-vous, des listes, des calculs."
    "À la fin, trois lignes sur Keyper. Puis une quatrième, barrée si fort que le papier a presque cédé."
    noam reflexion "Tu préparais quoi, Tomas... ?"
    "J'essaie de déchiffrer les mots, sans succès. Il avait pourtant prévu de continuer ses recherches le lendemain."
    "Je prends une photo du carnet et le remets exactement où il était."
    call investigation_take_manual_photo("j27_photo_carnet", "bg_chambre", (0.61, 0.59), 2.2) from _call_j27_carnet_photo
    return

label _27_0_1_1_0_1_PA_GRILLE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "La chambre de Tomas est impeccable, et sa grille possède encore ses fixations d’origine. Je les examine."
    "Dans la chambre d'Elen, c'est différent : une tôle artisanale est clouée devant l'ouverture. Elle bloque le passage, mais pas la circulation de l'air."
    noam reflexion "Bon. Ça n'explique toujours pas ce qui lui est arrivé."
    "J'enregistre les images sans toucher aux vis. Lysa me ferait une tête pas possible si je démontais tout."
    call investigation_take_manual_photo("j27_photo_grille_tomas", "bg_chambre", (0.65, 0.19), 2.2) from _call_j27_grille_photo
    return

label _27_0_1_1_0_1_PA_KEYPER:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je recherche les dernières consultations de Tomas. Keyper-IIB revient plusieurs fois dans l'historique."
    "Il avait ouvert des documents la veille de sa mort, puis repris une partie de ses calculs."
    noam raison "T'avais vraiment pas lâché l'affaire."
    "Les dates confirment qu'il travaillait encore sur la station. Elles ne disent rien sur ce qui lui est arrivé."
    return

label _27_0_1_1_0_1_PA_QUOTAS:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je parcours les index de production, à la recherche d'une définition d'ÉID-0."
    "Il y a des unités de transport, des références de conteneurs, des catégories de machines... mais aucune entrée qui corresponde clairement."
    noam fatigue "Sérieux, c'est quoi, ces effectifs ?"
    "Je sauvegarde les références des pages consultées. Je n'ai rien trouvé qui permette de dire s'il s'agit de personnes ou de machines."
    return

label _27_0_1_1_0_1_PA_SIGNAL:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je regarde les journaux de la console. Des mesures, des interférences, des heures de connexion. Je comprends à peine la moitié des colonnes."
    "Je ne repère aucune mention explicite de Yanma, et je n'ai pas le modèle du petit appareil."
    noam reflexion "Ça pourrait être là, sous mes yeux, et je le verrais même pas."
    "J'enregistre le journal sans tirer de conclusion."
    return

label _27_0_1_1_0_1_PA_CAMERA:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "J'ouvre l'inventaire des appareils censés se trouver ici."
    "Une longue liste de boîtiers et de capteurs apparaît, avec des photos qui se ressemblent presque toutes."
    noam fatigue "Génial... Une boîte grise, puis une autre boîte grise."
    "Aucun modèle ne correspond clairement à mon souvenir. Je demande une copie de l'inventaire."
    return

label _27_0_1_1_0_1_PA_ELIAS:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.36), ("noam", "neutre", 0.68)])
    noam reflexion "Elias, tu ranges parfois les appareils de la salle d'observation ?"
    elias raison "Ouais. Quand il traîne des trucs, je les ramène ici."
    noam raison "T'as déplacé une petite boîte avec un voyant, depuis le jour 25 ?"
    elias surpris "Une petite boîte ? Noam, y en a plein."
    noam fatigue "Je sais. J'ai pas mieux comme description."
    elias reflexion "J'ai pas le souvenir d'en avoir pris une, mais ça veut pas dire que j'ai rien bougé."
    noam neutre "Ça marche. Tu peux vérifier si un modèle manque ?"
    elias raison "Je peux regarder, oui. Mais je te promets pas que je vais retrouver ton truc."
    noam sourire "Merci."
    $ hideGroup()
    return

label _27_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    noam raison "Je voulais revenir sur le vote. Tu savais ce que Tomas cherchait exactement ?"
    julian agace "Tu vas encore me demander pourquoi je me suis énervé ?"
    noam neutre "Non. Je veux savoir s'il t'a parlé de Keyper ou des unités ÉID-0."
    julian reflexion "Keyper, oui, il avait dit un truc sur des quotas. ÉID-quoi, j'en ai aucune idée."
    noam raison "Il t'avait montré ses dossiers ?"
    julian fatigue "Non. On s'est engueulés avant qu'il puisse m'expliquer. Je l'ai pas laissé finir."
    noam inquiet "Julian..."
    julian triste "Ouais. Je sais."
    "Il détourne la tête. Je n'insiste pas."
    $ hideGroup()
    return

label _27_0_1_1_0_1_NYRA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Je retrouve Nyra. Elle m'a gardé un plateau."
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "fatigue", 0.68)])
    nyra sourire "Tu m'as dit que t'avais pas mangé. Alors mange."
    noam sourire "Merci. T'es la troisième personne à me le dire."
    nyra reflexion "Alors, ils ont dit quoi ?"
    noam raison "J'ai vérifié quelques pistes. Pour le moment, personne ne m'a donné une réponse claire sur les unités ÉID-0."
    if "kael" in investigation_pa_completed:
        noam reflexion "Kael connaît Yanma, mais il ne reconnaît pas l'appareil."
    if "iris" in investigation_pa_completed:
        noam raison "Iris croit avoir déjà vu une nomenclature proche. Elle va regarder."
        nyra raison "Ça vaut le coup de suivre ça."
    elif "sael" in investigation_pa_completed:
        noam raison "Sael et Ryn ne savent pas davantage ce que sont ces unités."
    else:
        nyra raison "Au moins, on a les documents de Tomas. Ça nous permet de chercher demain."
    noam neutre "Mais pas forcément pourquoi il est mort."
    nyra reflexion "Non, pas forcément."
    noam raison "J'ai toujours l'appareil en tête."
    nyra neutre "On y reviendra. Pour l'instant, on sait même pas ce que c'était. Je voudrais éviter qu'on accuse quelqu'un juste pour ça."
    noam fatigue "Ouais. T'as raison."
    nyra sourire "On peut faire deux dossiers. Keyper et ses unités d'un côté ; la mort de Tomas de l'autre. Si ça se recoupe, on le verra."
    noam neutre "Ça me va."
    "Je m'assois à côté d'elle et on trie mes notes pendant que je mange."
    $ hideGroup()
    jump _27_0_1_1_0_1_REUNION
# Durée : ~2m00.

label _27_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    "On se réunit autour de la table. La place de Tomas est toujours vide."
    $ showGroup([("julian", "fatigue", 0.080), ("elen", "triste", 0.248), ("noam", "neutre", 0.416), ("lysa", "blase", 0.584), ("iris", "fatigue", 0.752), ("nyra", "neutre", 0.920)])
    julian reflexion "On peut au moins faire le point ?"
    elen inquiet "Iris a dit qu'elle avait pas encore la cause."
    julian neutre "Je sais. Mais on va pas juste attendre sans rien faire."
    elen colere "Et tu veux qu'on dise qu'il s'est suicidé ?!"
    julian colere "J'ai pas dit ça !"
    lysa blase "C'est reparti..."
    iris agace "Stop. On n'a toujours pas de preuve qu'il a pris ces comprimés. Et on n'a pas de preuve qu'on l'a tué non plus."
    julian fatigue "D'accord."
    noam raison "J'ai trouvé les documents de Tomas. Sur Keyper-IIB et les unités ÉID-0."
    elen reflexion "Ça nous dit ce que c'est ?"
    noam fatigue "Non. Il y a des effectifs et des quotas. Et Tomas avait localisé la station à quelques heures de vol."
    noam raison "Il y avait aussi un livre sur la résonance Yanma. C'est une méthode de transmission dans l'espace."
    julian reflexion "Quel rapport avec sa mort ?"
    noam neutre "J'en sais rien. Mais il avait un petit appareil dans la salle d'observation, le jour 25. Aujourd'hui, cet appareil avait disparu."
    lysa surpris "Disparu ?"
    nyra raison "Il a pu être déplacé par quelqu'un de la maintenance. Mais on sait toujours pas ce que c'était."
    elen triste "Donc on sait toujours pas..."
    noam neutre "Pas encore."
    iris raison "Continuez à chercher. Moi je poursuis les examens. Mais arrêtez de tirer des conclusions avec une moitié d'indice."

    if "camera" in investigation_pa_completed:
        noam reflexion "J'ai aussi regardé l'inventaire des appareils. Aucune référence ne correspond clairement à ce que j'ai vu."
        lysa raison "Donc il a peut-être été rangé. Ou c'était pas un appareil officiel."
        nyra neutre "On n'a pas de quoi trancher."
    if "elias" in investigation_pa_completed:
        noam raison "Elias m'a dit qu'il déplaçait parfois du matériel. Mais il ne se souvient pas de celui-là."
        julian reflexion "Donc il l'a peut-être juste rangé ?"
        noam neutre "Peut-être."
    if "quotas" in investigation_pa_completed:
        noam reflexion "J'ai cherché une définition des unités ÉID-0. Aucun des index ouverts ne répond clairement."
        elen inquiet "Alors Tomas avait peut-être raison de s'inquiéter..."
        nyra raison "Peut-être, oui. Ça reste à vérifier."

    julian fatigue "Je peux avoir une copie des documents ?"
    noam surpris "Oui. Bien sûr."
    julian neutre "Merci."
    "Pour une fois, la réunion se termine sans que quelqu'un sorte en claquant la porte."
    $ hideGroup()
    jump _27_0_1_1_0_1_NUIT
# Durée : ~2m30.

label _27_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je relis les notes de Tomas. Keyper-IIB, les effectifs des unités ÉID-0, les trajets orbitaux, le livre sur Yanma."
    "J'avais espéré comprendre pourquoi il était mort. À la place, j'ai surtout découvert à quel point il cherchait encore."
    think "Et cet appareil qu'il examinait..."
    "Je n'ai pas de photo. Aucun numéro de série. Juste un souvenir d'une petite boîte métallique et d'un voyant."
    noam fatigue "Merde, Tomas..."
    "Demain, je voudrais retourner voir cette chambre où on l'a trouvé. Il reste peut-être quelque chose qu'on a raté."
    "Je pose ma tablette et ferme les yeux."
    stop music fadeout 1.0
    call end_day("28", sleeping=True) from _call_j27a_end_day_28
    jump _28_0_1_1_0_1_REVEIL
# Durée : ~1m00.
