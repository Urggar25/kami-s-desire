# ENQUÊTE À PA — J29. L'accusation et ses preuves essentielles restent obligatoires.
init 10 python:
    J29A_ROOMS = {
      "dortoir": {
        "title": "DORTOIRS",
        "background": "bg_chambre",
        "description": "La chambre d'Elen est toujours le point de départ de l'enquête.",
        "actions": [
          "grille",
          "elen"
        ]
      },
      "infirmerie": {
        "title": "INFIRMERIE",
        "background": "infirmerie2",
        "description": "Iris peut préciser ce que les résultats permettent de conclure.",
        "actions": [
          "iris",
          "flacon"
        ]
      },
      "maintenance": {
        "title": "MAINTENANCE",
        "background": "bg_maintenance",
        "description": "Le badge utilisé à 02 h 17 a laissé une trace, mais pas un visage.",
        "actions": [
          "kael",
          "elias"
        ]
      },
      "repos": {
        "title": "SALLE COMMUNE",
        "background": "bg_repos",
        "description": "Ryn et Sael sont disponibles pour des questions supplémentaires.",
        "actions": [
          "ryn",
          "sael"
        ]
      },
      "cafeteria": {
        "title": "CAFÉTÉRIA",
        "background": "bg_cafeteria",
        "description": "Julian et les autres ont gardé en tête leurs dernières disputes.",
        "actions": [
          "julian"
        ]
      },
      "archive": {
        "title": "ARCHIVES",
        "background": "bg_archive",
        "description": "Les documents techniques de Tomas et les registres de livraison.",
        "actions": [
          "livraisons"
        ]
      },
      "observation": {
        "title": "OBSERVATION",
        "background": "bg_observation",
        "description": "La console porte encore la trace d'un signal faible.",
        "actions": [
          "signal"
        ]
      },
      "conclave": {
        "title": "SALLE DU CONCLAVE",
        "background": "bg_conclave",
        "description": "La table autour de laquelle l'accusation sera présentée.",
        "actions": []
      },
      "gymnase": {
        "title": "GYMNASE",
        "background": "bg_gymnase",
        "description": "Personne n'a envie de s'entraîner aujourd'hui.",
        "actions": []
      }
    }
    J29A_ACTIONS = {
      "grille": {
        "title": "Reconstituer le passage de l'air",
        "description": "Vérifier la différence entre l'accès physique et la diffusion dans les conduits.",
        "label": "_29_0_1_1_0_1_PA_GRILLE",
        "evidence": "j29_tomas_grille"
      },
      "elen": {
        "title": "Revoir l'échange avec Elen",
        "description": "Lui demander si quelqu'un aurait pu entendre l'échange des chambres.",
        "label": "_29_0_1_1_0_1_PA_ELEN",
        "evidence": "j29_tomas_elen"
      },
      "iris": {
        "title": "Demander à Iris ce qui reste incertain",
        "description": "Distinguer l'homicide probable d'une cause toxicologique certaine.",
        "label": "_29_0_1_1_0_1_PA_IRIS",
        "evidence": "j29_tomas_iris"
      },
      "flacon": {
        "title": "Revoir le flacon avec Iris",
        "description": "Vérifier si le flacon était déjà dans la chambre d'Elen.",
        "label": "_29_0_1_1_0_1_PA_FLACON",
        "evidence": "j29_tomas_flacon"
      },
      "kael": {
        "title": "Interroger Kael sur les accès",
        "description": "Demander pourquoi le journal du badge de Nyra n'identifie pas son porteur.",
        "label": "_29_0_1_1_0_1_PA_KAEL",
        "evidence": "j29_tomas_badge"
      },
      "elias": {
        "title": "Interroger Elias sur les badges",
        "description": "Vérifier les possibilités d'emprunt et de prêt d'une autorisation.",
        "label": "_29_0_1_1_0_1_PA_ELIAS",
        "evidence": "j29_tomas_elias"
      },
      "ryn": {
        "title": "Reprendre l'alibi de Ryn",
        "description": "Confronter calmement sa soirée à celle de Julian.",
        "label": "_29_0_1_1_0_1_PA_RYN",
        "evidence": "j29_tomas_ryn"
      },
      "sael": {
        "title": "Questionner Sael sur la plante",
        "description": "Demander si la provenance botanique peut vraiment désigner quelqu'un.",
        "label": "_29_0_1_1_0_1_PA_SAEL",
        "evidence": "j29_tomas_sael"
      },
      "julian": {
        "title": "Confronter Julian à ses menaces",
        "description": "Lui demander ce qu'il a fait après la dispute, sans l'accuser.",
        "label": "_29_0_1_1_0_1_PA_JULIAN",
        "evidence": "j29_tomas_julian"
      },
      "livraisons": {
        "title": "Chercher une provenance du Bulbuma",
        "description": "Comparer les cargaisons sans en déduire l'identité d'un coupable.",
        "label": "_29_0_1_1_0_1_PA_LIVRAISONS",
        "evidence": "j29_tomas_livraisons"
      },
      "signal": {
        "title": "Comparer les signaux d'observation",
        "description": "Revoir les mesures sans inventer une destination de l'appareil.",
        "label": "_29_0_1_1_0_1_PA_SIGNAL",
        "evidence": "j29_tomas_signal"
      }
    }
    INVESTIGATION_ENTRIES.update({
        "j29_tomas_grille": {"category": "preuves", "title": "VENTILATION ET VERROU", "desc": "Le dispositif pouvait agir depuis le réseau malgré une porte verrouillée.", "day": "J29", "origin": "DORTOIRS", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_elen": {"category": "personnes", "title": "ELEN — ÉCHANGE CONNU", "desc": "Elen ne peut pas dire avec certitude qui a entendu leur discussion dans le couloir.", "day": "J29", "origin": "DORTOIRS", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_iris": {"category": "hypotheses", "title": "INCERTITUDES MÉDICALES", "desc": "Iris privilégie l'homicide sans pouvoir identifier avec certitude la substance inhalée.", "day": "J29", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_flacon": {"category": "preuves", "title": "FLACON DÉJÀ PRÉSENT", "desc": "Elen pense avoir laissé des somnifères dans sa chambre avant l'échange ; leur quantité initiale reste inconnue.", "day": "J29", "origin": "INFIRMERIE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_badge": {"category": "preuves", "title": "AUTORISATION DE NYRA", "desc": "Un lecteur de maintenance a enregistré une autorisation liée à Nyra à 02 h 17, sans identifier le porteur du badge.", "day": "J29", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_elias": {"category": "personnes", "title": "ELIAS — BADGES EMPRUNTABLES", "desc": "Le système enregistre les autorisations, et ne prouve pas qui portait le badge.", "day": "J29", "origin": "MAINTENANCE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_ryn": {"category": "personnes", "title": "RYN — SOIRÉE", "desc": "Ryn maintient être resté avec Julian et Mara une partie de la soirée puis être allé dormir.", "day": "J29", "origin": "SALLE COMMUNE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_sael": {"category": "personnes", "title": "SAEL — ORIGINES DU BULBUMA", "desc": "La présence possible de Bulbuma à Limen ne permet pas d'identifier son propriétaire sur le Conclave.", "day": "J29", "origin": "SALLE COMMUNE", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_julian": {"category": "personnes", "title": "JULIAN — REGRETS", "desc": "Julian regrette ses menaces mais maintient être resté avec Ryn et Mara avant de rentrer.", "day": "J29", "origin": "CAFÉTÉRIA", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_livraisons": {"category": "preuves", "title": "CARGAISONS NON CONCLUANTES", "desc": "Les registres n'établissent pas la provenance du récipient découvert dans la ventilation.", "day": "J29", "origin": "ARCHIVES", "status": "À VÉRIFIER", "manual_only": True},
        "j29_tomas_signal": {"category": "anomalies", "title": "SIGNAL NON IDENTIFIÉ", "desc": "Une émission faible figure dans les relevés du jour 25, mais son origine et sa destination restent inconnues.", "day": "J29", "origin": "OBSERVATION", "status": "À VÉRIFIER", "manual_only": True},
    })

# JOUR 29 — LE DERNIER MENSONGE
# Route alternative : Noam enquête sur l'assassinat de Tomas.
default j29a_reconstitution = 0
default j29a_erreurs = 0
default j29a_mobile = ""
default j29a_badge_nyra = False
default j29a_signal = False
default j29a_objections = 0
default j29a_accuse = ""
default j29a_contradiction = False
default j29a_nyra_detained = False

label _29_0_1_1_0_1_REVEIL:
    $ current_day = 29
    $ day_id = 29
    $ current_period = "Matin"
    $ j29a_reconstitution = 0
    $ j29a_erreurs = 0
    $ j29a_mobile = ""
    $ j29a_badge_nyra = False
    $ j29a_signal = False
    $ j29a_objections = 0
    $ j29a_accuse = ""
    $ j29a_contradiction = False
    $ j29a_nyra_detained = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille avec mes notes sur la tablette. Je les ai relues jusqu'à une heure impossible, et j'ai pas plus de certitudes qu'hier."
    "Tomas est mort. On a trouvé un dispositif derrière la ventilation de la chambre où il dormait. Je sais toujours pas qui a pu faire ça."
    noam fatigue "Bon. Faut arrêter de tourner en rond."
    "Le départ pour la Terre approche. Si on ne trouve rien aujourd'hui, j'ai peur qu'on n'arrive jamais à reprendre toute cette histoire."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j29a_door1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _29_0_1_1_0_1_INFIRMERIE
# Durée : ~50 s.

label _29_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j29a_door2
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("iris", "fatigue", 0.22), ("lysa", "neutre", 0.45), ("noam", "neutre", 0.70)])
    iris fatigue "Je vais le dire une fois, parce que je sais comment ça se passe avec toi."
    noam neutre "Bonjour à toi aussi."
    iris raison "Les derniers résultats sont compatibles avec une intoxication par inhalation. Et les résidus de la chambre ressemblent à ce qu'on a prélevé dans le conduit."
    lysa reflexion "Donc c'est le bol ?"
    iris agace "C'est compatible. J'ai pas un laboratoire complet ici, et ça me permet pas de déterminer une substance avec certitude."
    noam reflexion "Mais le suicide ?"
    iris raison "Franchement, vu le montage dans la ventilation, je trouve l'homicide beaucoup plus probable."
    lysa inquiet "Et les somnifères ?"
    iris neutre "On a toujours aucune preuve qu'il ait pris ce qu'il y avait dans le flacon. Il a pu être laissé là exprès. Il a aussi pu être là avant."
    noam fatigue "Ça me rend dingue."
    iris fatigue "Moi aussi. Mais si je commence à inventer des certitudes pour te faire plaisir, ça servira à rien."
    lysa raison "On va reprendre les événements avec Nyra."
    iris inquiet "Faites ça. Et si vous pensez trouver un coupable, trouvez quelque chose de concret. Pas juste quelqu'un qui vous plaît pas."
    noam raison "D'accord."
    iris triste "J'aurais aimé faire mieux pour Tomas."
    noam neutre "T'as pas arrêté depuis trois jours. On le sait."
    $ hideGroup()
    jump _29_0_1_1_0_1_RECONSTITUTION
# Durée : ~2m00.

label _29_0_1_1_0_1_RECONSTITUTION:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Nyra a mis nos notes dans l'ordre sur deux tablettes. Ça fait un drôle d'effet de voir les dernières heures de Tomas réduites à une liste."
    $ showGroup([("lysa", "neutre", 0.22), ("nyra", "neutre", 0.45), ("noam", "neutre", 0.70)])
    nyra raison "On sait certaines choses. D'autres, on les suppose. Si on mélange, on va accuser n'importe qui."
    noam neutre "On fait comment ?"
    lysa blase "Tu lis ce qui est écrit et tu essaies de pas te planter."
    noam taquin "Merci, c'est gentil."
    nyra sourire "Elle a pas tort."
    "Je reprends la chronologie. Pour chaque étape, je dois choisir ce qu'on peut réellement déduire."
    jump _29_0_1_1_0_1_RECON_MENU
# Durée : ~1m00.

label _29_0_1_1_0_1_RECON_MENU:
    if j29a_reconstitution == 4:
        jump _29_0_1_1_0_1_MOBILE
    if j29a_reconstitution == 0:
        menu:
            "Quel événement est certain ?"
            "Elen et Tomas ont échangé leurs chambres.":
                $ j29a_reconstitution = 1
                noam raison "Je les ai vus parler. Elen a confirmé qu'ils avaient échangé."
                nyra neutre "Ça, on peut le garder."
            "Tomas avait décidé de se suicider.":
                $ j29a_erreurs += 1
                lysa colere "On en sait rien. C'est justement ce qu'on vérifie."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 1:
        menu:
            "Comment expliquer la chambre fermée ?"
            "Une substance a pu entrer par la ventilation.":
                $ j29a_reconstitution = 2
                noam raison "Le verrou ne protège pas de ce qui passe par l'air."
                nyra neutre "C'est possible. Pas encore démontré pour cette nuit."
            "Quelqu'un a forcément forcé le verrou.":
                $ j29a_erreurs += 1
                lysa raison "Elias a forcé le verrou devant nous. Rien ne montrait qu'il avait été abîmé avant."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 2:
        menu:
            "Que permettent de dire les résultats médicaux ?"
            "L'intoxication par inhalation est plausible et l'homicide probable.":
                $ j29a_reconstitution = 3
                noam raison "C'est ce que dit Iris. Pas plus."
                nyra raison "OK."
            "Les somnifères prouvent le suicide.":
                $ j29a_erreurs += 1
                lysa blase "Non, Noam. Iris a littéralement passé trois jours à nous dire le contraire."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 3:
        menu:
            "Qu'est-ce qu'il manque encore ?"
            "L'identité de celui qui a préparé le dispositif et son mobile.":
                $ j29a_reconstitution = 4
                noam raison "On a une méthode possible. Pas un coupable."
                nyra neutre "Voilà. On avance."
            "Le nom de celui qui a ouvert la porte de l'intérieur.":
                $ j29a_erreurs += 1
                lysa raison "Personne n'avait besoin d'ouvrir si le dispositif était déjà dans les conduits."
        jump _29_0_1_1_0_1_RECON_MENU
# Durée : ~3m00, selon les tentatives.

label _29_0_1_1_0_1_MOBILE:
    $ current_period = "Après-midi"
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "reflexion", 0.21), ("nyra", "neutre", 0.45), ("noam", "neutre", 0.69)])
    lysa reflexion "Julian et Ryn lui en voulaient. Il a reçu des menaces sur Terre. C'est quand même pas rien."
    noam raison "Mais il cherchait Keyper et il avait trouvé cet appareil dans l'observation."
    nyra reflexion "Les deux pistes existent. On ne peut pas savoir laquelle a un lien avec sa mort, pour l'instant."
    menu:
        "Quelle piste approfondir en premier ?"
        "Les représailles liées au vote":
            $ j29a_mobile = "vote"
            noam raison "On reprend les menaces et les disputes. C'est le plus évident."
            lysa raison "D'accord. Mais après, on retourne voir les éléments techniques."
        "Le secret que Tomas avait découvert":
            $ j29a_mobile = "secret"
            noam raison "Je voudrais comprendre pourquoi ses recherches auraient pu déranger quelqu'un."
            nyra raison "D'accord. Sans oublier les gens qui le détestaient pour son vote."
    "Mon téléphone vibre. C'est Kael : il a trouvé un relevé dans la maintenance."
    noam surpris "Kael veut nous montrer quelque chose."
    nyra neutre "J'allais regarder de mon côté dans les archives. Je vous rejoins après."
    lysa raison "OK. On y va."
    $ hideGroup()
    jump _29_0_1_1_0_1_MAINTENANCE
# Durée : ~1m30.


label _29_0_1_1_0_1_MAINTENANCE:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Kael et Elias ont démonté la façade d'un boîtier de contrôle. Quand j'arrive, Elias est en train de se battre avec un câble qui refuse de rentrer dans son logement."
    $ showGroup([("kael", "reflexion", 0.22), ("elias", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    elias agace "Mais rentre, bordel..."
    noam neutre "Salut."
    elias fatigue "Ouais, salut. Deux secondes."
    kael raison "J'ai retrouvé une partie des relevés de l'accès technique des dortoirs."
    $ showGroup([("kael", "reflexion", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
    lysa reflexion "Celui par lequel on est passés hier ?"
    kael neutre "Oui. Enfin, un des accès à cette branche. Il est équipé d'un lecteur de badge."
    noam surpris "Et ?"
    kael reflexion "Le contrôleur garde les heures d'ouverture et l'autorisation utilisée. Pas une vidéo, juste des lignes."
    $ showGroup([("kael", "reflexion", 0.22), ("elias", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    elias raison "Ça enregistre le badge. Si tu piques celui de quelqu'un, il voit pas que c'est toi."
    $ showGroup([("kael", "reflexion", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
    lysa neutre "D'accord. Il dit quoi ?"
    kael raison "La nuit du 25 au 26, quelqu'un a ouvert l'accès à 02 h 17."
    noam inquiet "Le soir où Tomas est mort..."
    kael neutre "Oui. Mais ce journal ne nous dit pas combien de temps il est resté ouvert, ni ce que la personne a fait."
    noam reflexion "Et c'est le badge de qui ?"
    "Kael pivote l'écran. La ligne donne un identifiant de lecteur et un numéro d'autorisation."
    kael hesitation "Nyra."
    pause 0.4
    lysa surpris "Quoi ? Son badge ?"
    noam fatigue "Attends, Nyra ?"
    kael raison "Son autorisation, oui. J'ai vérifié dans le répertoire local."
    $ showGroup([("kael", "reflexion", 0.22), ("elias", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    elias neutre "Je te préviens tout de suite, ça veut pas dire qu'elle était là. Les badges peuvent se prêter."
    noam raison "Tu as d'autres accès enregistrés cette nuit-là ?"
    kael reflexion "Le reste du journal est incomplet. J'ai pas de quoi reconstruire tous les déplacements de la station, et encore moins d'affirmer qu'elle est passée devant la chambre."
    $ showGroup([("kael", "reflexion", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
    lysa neutre "Mais elle nous a dit qu'elle était allée se coucher."
    noam inquiet "Elle me l'a dit, oui. Je l'ai croisée devant les dortoirs."
    kael raison "Demande-lui si elle avait son badge. C'est la première chose à faire."
    noam neutre "Je peux prendre une copie ?"
    kael neutre "Oui. Mais n'en fais pas une preuve de meurtre à elle toute seule."
    "J'enregistre la ligne. Ce qu'on vient de découvrir est beaucoup plus précis que les soupçons sur la plante, mais ça ne donne toujours pas le nom de la personne qui l'a utilisée."
    $ j29a_badge_nyra = True
    elias fatigue "Bon. Maintenant, vous me laissez finir de remettre ce machin ? Sinon il va plus fermer du tout."
    lysa sourire "Bon courage."
    elias agace "Ouais, rigole."
    $ hideGroup()
    jump _29_0_1_1_0_1_OBSERVATION
# Durée : ~2m30.

label _29_0_1_1_0_1_OBSERVATION:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Sur le chemin, je repense au jour 25. Tomas avait reposé un petit appareil métallique sans même savoir ce que c'était. Le lendemain, il était mort."
    "Ça peut être une coïncidence. Mais je veux regarder une dernière fois."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_j29a_door3
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("lysa", "neutre", 0.39), ("noam", "reflexion", 0.68)])
    noam reflexion "C'était juste ici."
    lysa fatigue "Tu me l'as déjà montré hier."
    noam raison "Oui. Là, je veux regarder les relevés de la console."
    lysa reflexion "Les relevés de quoi ?"
    noam neutre "Des signaux reçus. Tomas lisait un livre sur Yanma, peut-être que cette salle a détecté quelque chose."
    "Je fouille les rapports automatiques du jour 25. La plupart sont des chiffres que je ne comprends pas."
    noam fatigue "Y a tellement de trucs..."
    lysa blase "Ça, je peux confirmer."
    "Je repère une entrée classée comme émission faible non identifiée, relevée pendant que Tomas travaillait dans la salle."
    noam surpris "Attends. Là."
    lysa reflexion "Ça dit juste « signal non classé »."
    noam raison "Oui. Et l'intensité est presque nulle."
    lysa neutre "Donc ça pourrait être le boîtier."
    noam reflexion "Peut-être. Mais y a aucune destination, aucun propriétaire, rien."
    lysa raison "Garde une copie. Mais ne dis pas que tu connais la destination du signal."
    noam neutre "Je sais même pas si le boîtier était un émetteur."
    lysa neutre "Voilà."
    lysa neutre "Oui, bon. Tu m'as compris."
    "Je photographie le relevé. Je n'ai rien permettant de confirmer qu'il s'agissait d'une émission Yanma, encore moins de savoir qui aurait été à l'autre bout."
    $ j29a_signal = True
    noam inquiet "Je voudrais demander à Nyra pour son badge."
    lysa raison "On le fait devant les autres. Sans lui sauter à la gorge."
    noam neutre "Ouais."
    $ hideGroup()
    jump _29_0_1_1_0_1_PA_INTRO
# Durée : ~1m45.

label _29_0_1_1_0_1_PA_INTRO:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("lysa", "neutre", 0.34), ("noam", "fatigue", 0.69)])
    lysa reflexion "Tu vas vraiment confronter Nyra pour ce badge ?"
    noam raison "Oui. Mais d'abord, je voudrais vérifier les dernières choses qu'on peut encore vérifier."
    lysa neutre "Alors on fait comme les autres jours. Cinq actions, pas davantage."
    noam reflexion "On pourra toujours lui poser la question même si je trouve rien ?"
    lysa raison "Évidemment. Le journal de maintenance et ce signal, tu les as déjà."
    noam fatigue "D'accord."
    "J'ai les preuves principales sur ma tablette. Les prochaines actions permettront d'éclaircir certaines contradictions et de retrouver des témoignages, pas de débloquer le droit d'accuser quelqu'un."
    $ investigation_pa_begin(29, 5)
    $ investigation_unlocked = True
    $ free_time_active = False
    $ conclave_lock = False
    $ dortoir_lock = False
    $ exploration_libre_active = True
    $ exploration_libre_allowed_rooms = list(J29A_ROOMS.keys())
    $ current_scene_active = None
    $ corridor_current = "dortoir"
    $ hideGroup()
    jump _29_0_1_1_0_1_PA_MAP

label _29_0_1_1_0_1_PA_MAP:
    call screen investigation_pa_map(J29A_ROOMS, title="JOUR 29 — LES DERNIERS ALIBIS")
    if _return == "finish":
        jump _29_0_1_1_0_1_PA_FIN
    if _return == "corridors":
        jump _29_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_current_room = _return
    jump _29_0_1_1_0_1_PA_ROOM

label _29_0_1_1_0_1_PA_CORRIDORS:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_j29a_pa_corridors
    $ investigation_pa_current_room = _return
    if investigation_pa_current_room not in J29A_ROOMS:
        jump _29_0_1_1_0_1_PA_MAP
    jump _29_0_1_1_0_1_PA_ROOM

label _29_0_1_1_0_1_PA_ROOM:
    call screen investigation_pa_room(investigation_pa_current_room, J29A_ROOMS, J29A_ACTIONS)
    if _return == "back":
        jump _29_0_1_1_0_1_PA_MAP
    if _return == "corridors":
        jump _29_0_1_1_0_1_PA_CORRIDORS
    $ investigation_pa_selected = _return
    if not investigation_pa_can_take(investigation_pa_selected):
        jump _29_0_1_1_0_1_PA_ROOM
    call screen investigation_pa_confirm(J29A_ACTIONS[investigation_pa_selected])
    if not _return:
        jump _29_0_1_1_0_1_PA_ROOM
    if not investigation_pa_spend(investigation_pa_selected):
        jump _29_0_1_1_0_1_PA_ROOM
    call expression J29A_ACTIONS[investigation_pa_selected]["label"] from _call_j29a_pa_dynamic
    $ investigation_add(J29A_ACTIONS[investigation_pa_selected]["evidence"])
    if investigation_pa_remaining == 0:
        "J'ai utilisé mes cinq actions. Il faut maintenant parler à Nyra devant les autres."
        jump _29_0_1_1_0_1_PA_FIN
    jump _29_0_1_1_0_1_PA_ROOM

label _29_0_1_1_0_1_PA_FIN:
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None
    if investigation_pa_remaining > 0:
        "Je m'arrête là. J'ai assez de choses à vérifier et je ne veux plus tourner autour du pot."
    jump _29_0_1_1_0_1_NYRA


label _29_0_1_1_0_1_PA_GRILLE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "La grille paraît intacte. Je reprends mes photos et compare son emplacement avec la plaque découverte dans les conduits."
    noam reflexion "La porte pouvait rester fermée tout le temps..."
    "L'air, lui, passait encore. Ça ne me donne pas un nom, mais ça explique pourquoi personne n'a entendu la porte."
    return

label _29_0_1_1_0_1_PA_ELEN:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    $ showGroup([("elen", "triste", 0.35), ("noam", "neutre", 0.69)])
    noam inquiet "Elen, je peux te demander une dernière fois pour l'échange des chambres ?"
    elen fatigue "Encore ?"
    noam neutre "C'est juste pour savoir si quelqu'un a pu entendre."
    elen reflexion "Noam, j'étais avec Tomas dans le couloir. Il y avait sûrement des gens pas loin. Mais je regardais pas qui passait."
    noam raison "Tu n'as vu personne clairement ?"
    elen triste "Non. Et si j'avais su..."
    noam fatigue "Je sais. J'arrête."
    elen inquiet "Tu penses que quelqu'un savait qu'il dormait chez moi ?"
    noam neutre "Je cherche à comprendre, c'est tout."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    noam raison "Je voudrais vérifier une dernière chose. Tu penses qu'on l'a tué, mais tu peux pas être sûre de la substance ?"
    iris raison "C'est ça. L'exposition par inhalation correspond aux éléments, mais je peux pas identifier précisément ce qu'il a respiré."
    noam reflexion "Donc on peut pas accuser quelqu'un juste parce qu'il connaît le Bulbuma."
    iris agace "Non. Et si tu me reposes cette question une quatrième fois, je vais t'envoyer chez Kael."
    noam sourire "D'accord, compris."
    iris triste "Fais attention à Elen pendant la réunion, s'il te plaît."
    noam neutre "Ouais."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_FLACON:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "fatigue", 0.35), ("noam", "reflexion", 0.69)])
    noam raison "Elen m'avait dit qu'elle avait peut-être des somnifères dans sa trousse."
    iris reflexion "Oui. Elle en avait bien. Mais elle ne sait pas combien il en restait."
    noam inquiet "Donc le flacon pouvait être dans sa chambre avant Tomas ?"
    iris raison "Oui. On ne peut pas démontrer quand il a été déplacé, ni même s'il l'a été."
    noam fatigue "C'est encore un truc qu'on pourra pas prouver."
    iris neutre "Pas avec ce qu'on a ici. Note-le comme une possibilité, pas comme un fait."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.35), ("noam", "neutre", 0.69)])
    noam raison "Reprenons le badge de Nyra. Il a bien ouvert le lecteur à 02 h 17 ?"
    kael raison "Oui. Le terminal donne l'autorisation et l'heure. Il ne photographie pas la personne."
    noam reflexion "Et quelqu'un aurait pu utiliser son badge sans qu'elle le sache ?"
    kael neutre "Oui. Je peux pas exclure ça. Mais je peux pas non plus expliquer pourquoi cette autorisation précise a été enregistrée."
    noam raison "Le lecteur est sur le chemin du conduit ?"
    kael raison "Il ouvre une porte qui mène à cette branche. Pas directement à la chambre."
    noam fatigue "Donc ça reste un indice. Pas une preuve définitive."
    kael neutre "Exact."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_ELIAS:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    noam reflexion "On peut prêter son badge de maintenance ?"
    elias raison "Oui. Enfin, faut normalement pas. Mais le lecteur sait pas si tu l'as emprunté."
    noam neutre "Nyra dit qu'elle avait probablement le sien avec elle."
    elias reflexion "Peut-être. Mais « probablement », ça me dit pas qui était à la porte."
    noam raison "Et les autres journaux ?"
    elias fatigue "Ils sont toujours incomplets. J'ai cherché."
    noam neutre "Bon. Merci."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_RYN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("ryn", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    ryn agace "Encore moi ?"
    noam raison "Je voulais vérifier la soirée du 25. Tu étais avec Julian et Mara ?"
    ryn fatigue "Ouais. Je l'ai déjà dit. Après je suis allé me coucher."
    noam neutre "Tu les as quittés à quelle heure ?"
    ryn reflexion "J'en sais rien. Il était tard."
    noam inquiet "Tu savais où Tomas dormait ?"
    ryn colere "Non ! Je savais même pas qu'il avait changé de chambre !"
    noam raison "D'accord."
    ryn fatigue "Je sais que j'ai été un con avec lui. Mais ça prouve quoi, tout ça ?"
    noam neutre "Rien, à lui seul."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_SAEL:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.35), ("noam", "neutre", 0.69)])
    noam raison "Sael, la plante qui pourrait avoir brûlé dans le conduit... Elle pousse aussi ailleurs qu'à Limen ?"
    sael raison "Oui. Et certaines espèces proches sont cultivées. On ne peut pas retrouver le propriétaire à partir de ça."
    noam reflexion "Tu sais si quelqu'un en avait ici ?"
    sael neutre "Non. J'ai vérifié mes affaires et celles de l'infirmerie. Rien ne correspond."
    noam fatigue "Donc on peut pas écarter Limen, ni l'accuser."
    sael raison "Voilà. C'est exactement ce que je dis depuis hier."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "fatigue", 0.35), ("noam", "neutre", 0.69)])
    noam raison "Julian, tu peux me redire quand tu as quitté Ryn et Mara ?"
    julian reflexion "Je sais pas, Noam. Je suis rentré après eux, ou à peu près en même temps."
    noam neutre "Tu as revu Tomas dans la nuit ?"
    julian fatigue "Non. J'ai passé la soirée à l'éviter. Tu connais la suite."
    noam raison "Tu te souviens qu'il avait changé de chambre ?"
    julian agace "Je te l'ai déjà dit : non."
    pause 0.3
    julian triste "Je sais que j'ai été odieux. Mais si tu veux me demander si je l'ai tué, demande-le franchement."
    noam fatigue "J'essaie juste de comprendre ce qui s'est passé."
    julian neutre "Alors fais-le sans inventer ce que je pense."
    $ hideGroup()
    return

label _29_0_1_1_0_1_PA_LIVRAISONS:
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je vérifie les lots de plantes, les consommables médicaux et les petits récipients passés par le Conclave."
    "Les références sont trop vagues pour retrouver celui qui a été installé dans le conduit. Certaines cargaisons viennent de Limen, d'autres d'Orbite ou ont transité ailleurs."
    noam fatigue "Même les factures savent rien..."
    "Je prends une copie des références utilisables. Pour l'instant, ça ne permet de désigner personne."
    return

label _29_0_1_1_0_1_PA_SIGNAL:
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7
    "Je reviens sur l'émission faible découverte ce matin. Le rapport est court. Aucune destination n'y figure."
    "Ça pourrait être lié au petit appareil que Tomas tenait, mais je n'ai ni numéro de série ni preuve que ce soit un signal Yanma."
    noam reflexion "Je peux pas me permettre de raconter que j'ai retrouvé un appel clandestin."
    "Je garde une copie du relevé, sans lui donner plus de valeur qu'il n'en a."
    return

label _29_0_1_1_0_1_NYRA:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Nyra est près de la table commune. Elle referme sa tablette en nous voyant arriver."
    $ showGroup([("nyra", "neutre", 0.24), ("lysa", "neutre", 0.49), ("noam", "neutre", 0.74)])
    nyra sourire "Alors ? Vous avez trouvé quelque chose ?"
    noam reflexion "Ouais. On a un relevé de maintenance."
    nyra neutre "D'accord."
    noam raison "La nuit où Tomas est mort, un badge a ouvert l'accès technique vers les conduits des dortoirs."
    nyra reflexion "Lequel ?"
    noam neutre "Le tien."
    pause 0.4
    nyra surpris "Mon badge ?"
    lysa raison "C'est ce que dit le boîtier. À 02 h 17."
    nyra reflexion "Je suis allée me coucher, Noam. Tu m'as croisée."
    noam raison "Oui. Tu m'as dit que tu allais dormir. Mais je te demande juste si tu avais ton badge."
    nyra neutre "Normalement, oui. Je l'ai presque toujours avec moi."
    lysa reflexion "Et quelqu'un aurait pu te l'emprunter ?"
    nyra hesitation "J'en sais rien. C'est possible. Je vérifie pas toutes les heures si quelqu'un l'a touché."
    noam reflexion "Tu te souviens d'être passée par la maintenance cette nuit-là ?"
    nyra raison "Non. Je viens de te dire que je dormais."
    noam neutre "D'accord."
    nyra reflexion "Tu penses que je suis entrée dans le conduit pour faire quelque chose à Tomas ?"
    noam fatigue "Je pense que j'ai besoin de comprendre pourquoi ton autorisation apparaît là."
    nyra raison "Alors montre-moi le relevé."
    "Je lui montre l'écran. Elle lit la ligne, puis agrandit l'identifiant du lecteur."
    nyra neutre "Kael a raison de dire que ça ne montre pas la personne. Juste une autorisation."
    noam raison "Ouais."
    nyra inquiet "Tu sais, je t'ai aidé pendant trois jours. Je vois bien que ça te met mal à l'aise de me demander."
    noam fatigue "Un peu."
    nyra neutre "Je préfère que tu le fasses, plutôt que tu racontes aux autres que j'ai tué Tomas dans mon dos."
    lysa blase "Là-dessus, on est d'accord."
    nyra raison "Je viens à la réunion. Je répondrai aux questions."
    "Elle reprend sa tablette. Personne ne se met à hurler. Je pensais que j'allais être soulagé, mais je suis encore plus mal à l'aise."
    $ hideGroup()
    jump _29_0_1_1_0_1_REUNION
# Durée : ~2m30.

label _29_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    "On se retrouve dans la salle du Conclave. J'ai demandé à tout le monde de venir parce que je ne veux plus discuter de la mort de Tomas par petits groupes, en inventant des morceaux d'histoire chacun de notre côté."
    $ showGroup([("noam", "neutre", 0.22), ("iris", "fatigue", 0.48), ("julian", "fatigue", 0.74)])
    julian reflexion "Bon. Tu nous as dit que t'avais quelque chose d'important."
    noam raison "Oui. Mais d'abord, Iris va vous expliquer ce qu'elle a trouvé."
    iris raison "L'hypothèse d'une intoxication par inhalation s'est renforcée. Avec le dispositif du conduit, l'homicide est désormais plus probable qu'un suicide."
    $ showGroup([("noam", "neutre", 0.22), ("iris", "fatigue", 0.48), ("elen", "triste", 0.74)])
    elen inquiet "Donc... il s'est pas tué ?"
    iris fatigue "Je ne peux pas te le garantir. Mais je ne crois plus qu'on puisse continuer à parler d'un suicide probable."
    $ showGroup([("noam", "neutre", 0.22), ("iris", "fatigue", 0.48), ("julian", "fatigue", 0.74)])
    julian fatigue "D'accord."
    $ showGroup([("noam", "neutre", 0.22), ("ryn", "agace", 0.48), ("sael", "neutre", 0.74)])
    ryn agace "Et nous, on est encore dans la liste des suspects à cause de cette plante ?"
    sael calme "Ryn, laisse-le parler."
    noam raison "On va reprendre les éléments, sans essayer de choisir quelqu'un avant."
    $ showGroup([("noam", "neutre", 0.22), ("nyra", "neutre", 0.48), ("elen", "triste", 0.74)])
    nyra neutre "C'est ce qu'il faut faire."
    elen triste "Je veux juste savoir. Même si c'est horrible, je préfère savoir."
    noam neutre "Ouais. Moi aussi."
    if "elias" in investigation_pa_completed or "kael" in investigation_pa_completed:
        $ showGroup([("kael", "calme", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
        noam raison "J'ai revu le journal d'accès. Le lecteur enregistre un badge, pas la personne qui l'utilise."
        kael neutre "Exactement. Ça reste une piste, pas une identification."
    if "livraisons" in investigation_pa_completed or "sael" in investigation_pa_completed:
        $ showGroup([("sael", "neutre", 0.22), ("iris", "fatigue", 0.48), ("noam", "neutre", 0.74)])
        noam raison "Les registres et l'origine de la plante ne permettent pas de désigner une personne."
        sael raison "Donc ne le faisons pas."
    if "elen" in investigation_pa_completed:
        $ showGroup([("elen", "triste", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
        noam raison "On ne sait toujours pas qui a entendu l'échange de chambres."
        elen fatigue "J'aimerais tellement pouvoir vous répondre..."
        lysa raison "On sait. On peut pas te demander de te souvenir de tout."
    $ showGroup([("iris", "fatigue", 0.22), ("julian", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    "J'affiche les photos de la chambre et du conduit sur la table. Il va falloir reprendre les arguments un par un."
    jump _29_0_1_1_0_1_OBJECTIONS
# Durée : ~1m30.

label _29_0_1_1_0_1_OBJECTIONS:
    if j29a_objections >= 4:
        jump _29_0_1_1_0_1_ACCUSATION
    if j29a_objections == 0:
        menu:
            "« La chambre était fermée. Il ne pouvait pas y avoir de meurtrier. »"
            "Montrer le dispositif d'aération":
                $ j29a_objections = 1
                noam raison "Quelqu'un a pu préparer le dispositif depuis la maintenance. Pas besoin d'entrer dans la chambre."
                kael raison "Oui. L'accès technique permet d'atteindre cette branche."
                julian inquiet "D'accord. J'avais pas pensé à ça."
            "Montrer le livre de Tomas":
                $ j29a_erreurs += 1
                lysa raison "Le livre nous dit rien sur la porte. Regarde plutôt les photos du conduit."
        jump _29_0_1_1_0_1_OBJECTIONS
    if j29a_objections == 1:
        menu:
            "« Le flacon prouve que Tomas voulait mourir. »"
            "Présenter les conclusions d'Iris":
                $ j29a_objections = 2
                iris raison "On ne sait même pas s'il a pris les comprimés. Les signes d'intoxication et le dispositif sont beaucoup plus importants."
                elen triste "Je savais qu'on pouvait pas conclure comme ça..."
            "Présenter les menaces reçues sur Terre":
                $ j29a_erreurs += 1
                noam fatigue "Les menaces expliquent pourquoi il allait mal. Pas ce qui l'a tué."
        jump _29_0_1_1_0_1_OBJECTIONS
    if j29a_objections == 2:
        menu:
            "« La plante ne pousse qu'à Limen. »"
            "Rappeler les autres régions arides et les livraisons":
                $ j29a_objections = 3
                sael raison "Exactement. Le lieu de croissance d'une plante ne dit pas qui l'a apportée."
                ryn fatigue "Merci. C'est ce que j'essaie de dire depuis hier."
                nyra neutre "Et on reçoit régulièrement des marchandises des autres districts."
            "Accuser Ryn parce qu'il connaît le nom de la plante":
                $ j29a_erreurs += 1
                ryn colere "Mais tu m'écoutes quand je parle, ou pas ?!"
                noam fatigue "Non. C'est pas suffisant."
        jump _29_0_1_1_0_1_OBJECTIONS
    if j29a_objections == 3:
        menu:
            "« Tomas n'avait aucune autre raison d'être visé que son vote. »"
            "Présenter Keyper et l'appareil disparu":
                $ j29a_objections = 4
                noam raison "Il enquêtait encore sur Keyper et sur un appareil qu'il avait trouvé. Ça pouvait aussi déranger quelqu'un."
                julian reflexion "Mais tu sais pas ce que c'était."
                noam raison "Non. C'est une deuxième piste, pas un mobile démontré."
            "Présenter le verrou de la chambre":
                $ j29a_erreurs += 1
                lysa raison "Ça nous dit comment le meurtre a pu être fait, pas pourquoi."
        jump _29_0_1_1_0_1_OBJECTIONS
# Durée : ~3m00, selon les tentatives.


label _29_0_1_1_0_1_ACCUSATION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    $ showGroup([("julian", "fatigue", 0.22), ("iris", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    julian reflexion "Tout ça, c'est bien joli, mais on sait toujours pas qui aurait pu faire ça."
    noam raison "Kael a trouvé un relevé. Un accès de maintenance a été ouvert à 02 h 17 la nuit de la mort de Tomas."
    iris surpris "Avec quel badge ?"
    noam reflexion "Celui de Nyra."
    pause 0.5
    $ showGroup([("elen", "triste", 0.22), ("julian", "fatigue", 0.48), ("noam", "neutre", 0.74)])
    elen surpris "Nyra ?"
    julian surpris "Attends, quoi ?!"
    $ showGroup([("nyra", "neutre", 0.22), ("lysa", "neutre", 0.48), ("noam", "neutre", 0.74)])
    nyra neutre "Oui. Noam m'en a parlé. Je lui ai dit que je ne m'étais pas rendue dans la maintenance cette nuit-là."
    lysa raison "Le système a enregistré ton autorisation, pas ton visage."
    nyra raison "Exactement. Si mon badge a été utilisé par quelqu'un d'autre, ça ne dit rien sur moi."
    $ showGroup([("julian", "fatigue", 0.22), ("nyra", "neutre", 0.48), ("noam", "neutre", 0.74)])
    julian inquiet "Mais tu l'avais avec toi ?"
    nyra reflexion "Normalement. Je ne peux pas certifier chaque minute de la nuit."
    noam neutre "Je peux pas prouver que tu étais dans le conduit. Mais je peux pas faire comme si ce relevé existait pas."
    nyra raison "Alors ne fais pas comme si c'était une vidéo de moi."
    $ showGroup([("elen", "triste", 0.22), ("nyra", "neutre", 0.48), ("noam", "neutre", 0.74)])
    elen inquiet "Noam, tu soupçonnes Nyra ?"
    noam fatigue "Je soupçonne plusieurs personnes. Je vais devoir dire ce que je pense."
    $ showGroup([("iris", "fatigue", 0.22), ("nyra", "neutre", 0.48), ("noam", "neutre", 0.74)])
    iris reflexion "Et tu sais que ça peut se retourner contre quelqu'un qui n'a rien fait."
    noam neutre "Je sais."
    "Je regarde les visages autour de la table. Même après tout ça, j'aimerais encore qu'Iris me dise qu'elle a trouvé une autre explication."
    menu (screen="critical_choice", noam_expr="hesitation"):
        "Qui semble le plus directement impliqué ?"
        "Julian — la colère contre Tomas":
            $ j29a_accuse = "julian"
        "Ryn — les menaces et la piste de Limen":
            $ j29a_accuse = "ryn"
        "Sael — les connaissances botaniques":
            $ j29a_accuse = "sael"
        "Nyra — le badge de maintenance et l'appareil disparu":
            $ j29a_accuse = "nyra"
    if j29a_accuse == "nyra":
        jump _29_0_1_1_0_1_NYRA_ACCUSATION
    jump _29_0_1_1_0_1_FAUSSE_ACCUSATION
# Durée : ~2m00 + choix critique.

label _29_0_1_1_0_1_FAUSSE_ACCUSATION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    if j29a_accuse == "julian":
        $ showGroup([("noam", "inquiet", 0.22), ("nyra", "neutre", 0.48), ("julian", "fatigue", 0.74)])
    elif j29a_accuse == "ryn":
        $ showGroup([("noam", "inquiet", 0.22), ("ryn", "agace", 0.48), ("sael", "neutre", 0.74)])
    else:
        $ showGroup([("noam", "inquiet", 0.22), ("sael", "neutre", 0.48), ("elen", "triste", 0.74)])
    if j29a_accuse == "julian":
        noam raison "Julian. Tu lui en voulais, et tu l'as menacé devant tout le monde."
        julian colere "Je l'ai engueulé, oui ! Mais ça fait trois jours que je vous dis que je voulais pas sa mort !"
        noam raison "Tu savais où étaient les accès techniques."
        julian agace "Comme la moitié des gens ici ! Montre-moi juste une preuve que j'y suis allé !"
        "Je regarde mes notes. Je n'en ai aucune."
        julian triste "J'ai été horrible avec lui. Ça, je peux pas le changer. Mais je l'ai pas tué."
    elif j29a_accuse == "ryn":
        noam raison "Ryn. Tu étais furieux, et tu connais les plantes de Limen."
        ryn colere "Putain ! Pas encore ! Je connais le NOM d'une plante, et ça y est ?!"
        sael raison "Il n'y a aucune preuve qu'il ait eu cette plante ou qu'il soit entré dans le conduit."
        ryn fatigue "J'étais avec Julian et Mara une partie de la soirée. Après je suis rentré. Je sais pas quoi te dire d'autre."
        noam fatigue "Je peux pas prouver que tu y es allé."
    else:
        noam raison "Sael. Tu avais accès au matériel médical et tu connais certaines plantes de Limen."
        sael reflexion "Oui. Et ?"
        noam raison "Tu pouvais identifier la plante et comprendre son effet."
        sael colere "Tu m'accuses parce que je soigne les gens et que je sais lire une fiche botanique ?"
        sael raison "Tu as une preuve de ma présence dans la ventilation ?"
        noam fatigue "Non."
        sael neutre "Alors tu n'as pas assez."
    pause 0.3
    $ showGroup([("elen", "triste", 0.22), ("nyra", "neutre", 0.48), ("noam", "neutre", 0.74)])
    elen inquiet "Noam, je comprends que tu veuilles trouver quelqu'un... mais on peut pas enfermer une personne juste avec ça."
    nyra raison "Elen a raison. Et le badge retrouvé, on n'a toujours pas expliqué pourquoi il a été utilisé."
    noam fatigue "Je sais."
    julian reflexion "On va pas décider d'une arrestation sur un vote de popularité."
    iris raison "Il n'y a pas assez pour conclure. Ça n'efface pas la mort de Tomas."
    "La réunion s'arrête sans décision. J'ai désigné quelqu'un, et je n'ai pas réussi à défendre mon accusation."
    "Personne n'est enfermé. Nyra quitte la salle avec les autres."
    $ j29a_nyra_detained = False
    $ hideGroup()
    jump _29_0_1_1_0_1_NUIT
# Durée : ~2m30.

label _29_0_1_1_0_1_NYRA_ACCUSATION:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    $ showGroup([("nyra", "neutre", 0.22), ("noam", "inquiet", 0.48), ("elen", "triste", 0.74)])
    noam raison "Nyra. Je pense que tu es impliquée dans la mort de Tomas."
    pause 0.6
    nyra surpris "Moi ?"
    elen surpris "Noam..."
    nyra neutre "D'accord. Explique-moi."
    noam raison "Le badge de maintenance, d'abord. Il a été utilisé vers la branche des dortoirs pendant la nuit."
    nyra reflexion "Je viens de dire que ce relevé ne montre pas qui l'avait. Tu le sais."
    noam neutre "Oui."
    nyra raison "Et le fait que je sache utiliser des appareils orbitaux ne fait pas de moi une meurtrière."
    noam fatigue "Je sais."
    nyra reflexion "Alors qu'est-ce que tu as de plus ?"
    "Je regarde les autres. Aucun ne parle. Je repense à toutes les fois où Nyra m'a aidé, jusqu'à cet après-midi."
    jump _29_0_1_1_0_1_CONFRONTATION
# Durée : ~1m30.

label _29_0_1_1_0_1_CONFRONTATION:
    menu:
        "Quel élément confronter à la version de Nyra ?"
        "Le badge utilisé à 02 h 17 et son affirmation qu'elle n'a pas quitté sa chambre":
            $ j29a_contradiction = True
            noam raison "Tu m'as dit que tu allais dormir. Aujourd'hui, tu dis que tu n'es jamais passée en maintenance. Pourtant, ton autorisation a ouvert un accès qui mène à la chambre où Tomas est mort."
            nyra raison "Il reste possible que quelqu'un ait utilisé mon badge."
            noam neutre "Oui. Mais tu dis l'avoir eu sur toi. Et tu ne nous as jamais signalé sa disparition."
            nyra reflexion "Parce que j'ai jamais constaté sa disparition."
            noam raison "Je te demande pas d'avouer. Je te demande d'expliquer ce relevé autrement qu'en disant que quelqu'un a peut-être pris ton badge."
            nyra neutre "Je ne peux pas. Pas plus que toi tu ne peux prouver que je l'ai utilisé."
            lysa raison "C'est vrai. Mais on a désormais une contradiction qu'il faut vérifier."
            jump _29_0_1_1_0_1_CONSEQUENCE_NYRA
        "La plante, parce qu'Orbite possède des zones arides":
            noam raison "Tu viens d'Orbite. Le Bulbuma y pousse peut-être."
            nyra reflexion "Comme à Limen. Et comme dans certaines marchandises qu'on reçoit ici. Tu sais que ça ne prouve rien."
            iris raison "Je l'ai dit moi-même. Ce n'est pas un indice suffisant."
            noam fatigue "Ouais..."
            $ j29a_erreurs += 1
            jump _29_0_1_1_0_1_CONFRONTATION
        "Le livre Yanma, parce qu'elle connaît les transmissions spatiales":
            noam raison "Tu connais la résonance Yanma. Tomas lisait un livre là-dessus."
            nyra raison "Kael la connaît aussi. Et tu n'as même pas identifié l'appareil que Tomas tenait."
            lysa neutre "On peut pas accuser quelqu'un pour ses connaissances techniques."
            $ j29a_erreurs += 1
            jump _29_0_1_1_0_1_CONFRONTATION
# Durée : 1m30 selon les essais.

label _29_0_1_1_0_1_CONSEQUENCE_NYRA:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    $ showGroup([("nyra", "neutre", 0.22), ("elen", "triste", 0.48), ("noam", "inquiet", 0.74)])
    elen inquiet "Vous voulez l'enfermer ?"
    $ showGroup([("nyra", "neutre", 0.22), ("julian", "fatigue", 0.48), ("noam", "inquiet", 0.74)])
    julian reflexion "On va quand même pas prendre une décision définitive avec une seule ligne dans un journal."
    noam raison "Pas une décision définitive. Mais le départ approche. Si elle peut accéder aux conduits, on peut pas juste faire comme si on avait rien trouvé."
    nyra neutre "Je n'ai touché à aucun conduit. Tu me crois ou non, c'est tout ce que je peux dire."
    $ showGroup([("nyra", "neutre", 0.22), ("iris", "fatigue", 0.48), ("noam", "inquiet", 0.74)])
    iris raison "Ça n'est pas une preuve complète de culpabilité. Il faut être clair là-dessus."
    $ showGroup([("nyra", "neutre", 0.22), ("sael", "neutre", 0.48), ("noam", "inquiet", 0.74)])
    sael reflexion "On peut néanmoins la placer sous surveillance jusqu'à ce qu'on puisse vérifier ce relevé."
    $ showGroup([("nyra", "neutre", 0.22), ("elen", "triste", 0.48), ("noam", "inquiet", 0.74)])
    elen triste "Je veux pas qu'il arrive quelque chose à quelqu'un d'autre."
    nyra reflexion "Et moi, je dois accepter d'être enfermée parce qu'on n'a pas compris qui a utilisé mon badge ?"
    $ showGroup([("nyra", "neutre", 0.22), ("julian", "fatigue", 0.48), ("noam", "inquiet", 0.74)])
    julian fatigue "Je sais pas quoi penser. Mais pour cette nuit, je préfère qu'on évite de laisser les accès techniques libres."
    noam neutre "On peut garder Nyra dans une chambre surveillée. Pas la condamner. On continuera l'enquête sur Terre."
    $ showGroup([("nyra", "neutre", 0.22), ("iris", "fatigue", 0.48), ("noam", "inquiet", 0.74)])
    iris neutre "Si c'est provisoire et que personne n'y touche, je peux accepter. Je veux pouvoir lui parler si elle en a besoin."
    $ showGroup([("nyra", "neutre", 0.22), ("sael", "neutre", 0.48), ("noam", "inquiet", 0.74)])
    sael raison "Je surveillerai la porte avec Kael. Et on conservera son badge séparément."
    nyra fatigue "..."
    pause 0.4
    nyra neutre "D'accord. Mais ne me demandez pas de vous remercier."
    noam inquiet "Nyra..."
    nyra raison "Tu as fait ton choix, Noam. Tu m'as même laissé répondre. Je n'ai rien d'autre à ajouter."
    "Elle se lève. Personne ne la touche. Sael lui indique simplement la sortie, et Kael l'attend à l'extérieur."
    $ j29a_nyra_detained = True
    $ hideGroup()
    jump _29_0_1_1_0_1_NUIT
# Durée : ~3m00.

label _29_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.9
    "Je retrouve ma chambre avec la sensation d'avoir raté quelque chose. J'ai beau regarder les documents, je revois surtout Tomas, puis les visages des autres pendant la réunion."
    if j29a_nyra_detained:
        "Nyra est dans une chambre surveillée pour la nuit. Personne n'a prouvé qu'elle a tué Tomas, et pourtant c'est moi qui ai demandé qu'on l'y mette."
        "Je repense à tous les moments où elle m'a aidé. Elle était là quand on a trouvé les livres, quand on a repris les témoignages et même ce matin, quand on cherchait à remettre les événements dans l'ordre."
        noam fatigue "Si je me suis planté..."
        "Je voudrais lui demander pourquoi son badge apparaît dans ce journal. Elle n'a pas d'explication. Moi non plus, pas une explication qui élimine toutes les autres."
    else:
        "Personne n'a été arrêté. J'ai accusé quelqu'un sans réussir à démontrer quoi que ce soit, et je sais que les autres vont s'en souvenir."
        "Nyra m'a proposé qu'on poursuive les recherches une fois sur Terre. J'ai dit oui, mais j'arrive pas à me convaincre que tout s'arrêtera là."
        noam fatigue "Pardon, Tomas..."
        "Je rouvre le dossier une dernière fois. Il reste ce relevé de maintenance, l'appareil qui a disparu et les notes sur Keyper. On a encore trop de questions."
    "Demain, on devrait enfin rentrer. Je ne sais même plus si j'en ai envie."
    "J'éteins la tablette."
    stop music fadeout 1.0
    call end_day("30", sleeping=True) from _call_j29a_end_day_30
    jump _30_0_1_1_0_1_REVEIL
# Durée : ~1m20.
