################################################################################
## Roadmap / Carte narrative - Kami's Desires
################################################################################

default roadmap_unlocked_nodes = []
default roadmap_discovered_nodes = []
default roadmap_completed_nodes = []
default roadmap_current_node = None
default roadmap_selected_node = None
default roadmap_selected_category = "all"
default roadmap_dev_mode = False
default roadmap_target_node_id = None
default roadmap_target_label = None

init -2 python:
    ROADMAP_CATEGORIES = [
        ("all", "Tous"),
        ("day", "Jours"),
        ("vote", "Votes"),
        ("route", "Routes"),
        ("scene", "Scènes importantes"),
        ("ending", "Fins"),
        ("debug", "Développement / Debug"),
    ]

    ROADMAP_NODES = [
        {
            "id": "day_0",
            "title": "Jour 0 — Sélection",
            "short": "J0",
            "label": "_0_CANON",
            "category": "day",
            "kind": "day",
            "x": 120,
            "y": 390,
            "summary": "Kami interrompt une réunion ordinaire et impose le Conclave orbital comme nouveau centre de décision.",
            "choice": "Acceptation forcée du protocole Kami's Desires.",
            "consequence": "Noam est extrait vers le Conclave.",
            "requires": [],
            "required_variables": {},
            "teleportable": True,
        },
        {
            "id": "day_1",
            "title": "Jour 1 — Réveil au Conclave",
            "short": "J1",
            "label": "_1_CANON",
            "category": "day",
            "kind": "day",
            "x": 500,
            "y": 390,
            "summary": "Les représentants découvrent le Conclave, ses salles et les règles d'unanimité imposées par Kami.",
            "choice": "Premiers repères, premières alliances, premières méfiances.",
            "consequence": "Le cycle des amendements est lancé.",
            "requires": ["day_0"],
            "required_variables": {},
            "teleportable": True,
        },
        {
            "id": "day_2",
            "title": "Jour 2 — Installation",
            "short": "J2",
            "label": "_2_CANON",
            "category": "day",
            "kind": "day",
            "x": 880,
            "y": 390,
            "summary": "Le premier amendement sur le commerce interdistrict est annoncé. Les intérêts de chaque district remontent.",
            "choice": "Observer les positions avant le premier vote.",
            "consequence": "Le débat sur le commerce devient inévitable.",
            "requires": ["day_1"],
            "required_variables": {},
            "teleportable": True,
        },
        {
            "id": "day_3",
            "title": "Jour 3 — Premier débat",
            "short": "J3",
            "label": "_3_CANON",
            "category": "day",
            "kind": "day",
            "x": 1260,
            "y": 390,
            "summary": "Le Conclave approche du vote sur le commerce. Les tensions politiques deviennent impossibles à cacher.",
            "choice": "Soutien, opposition ou prudence face à l'amendement.",
            "consequence": "Le vote peut ouvrir une nouvelle route ou maintenir le statu quo.",
            "requires": ["day_2"],
            "required_variables": {},
            "teleportable": True,
        },
        {
            "id": "debate_phase_1",
            "title": "Débat — Texte fragmenté",
            "short": "Débat I",
            "label": "_3_DEBAT1_PHASE1",
            "category": "scene",
            "kind": "scene",
            "x": 1620,
            "y": 245,
            "summary": "L'amendement est présenté sous une forme instable. Les représentants tentent de reconstituer le sens politique du texte.",
            "choice": "Identifier les arguments utiles au vote.",
            "consequence": "Le rapport de forces se précise.",
            "requires": ["day_3"],
            "teleportable": True,
        },
        {
            "id": "vote_commerce",
            "title": "Vote — Commerce libre",
            "short": "Vote",
            "label": "vote_phase3_final",
            "category": "vote",
            "kind": "vote",
            "x": 1980,
            "y": 390,
            "summary": "Le Conclave vote sur l'autorisation du commerce, du transport et du stockage des marchandises.",
            "choice": "Voter pour, voter contre, ou laisser l'abstention agir.",
            "consequence": "Le résultat divise la chronologie en deux routes.",
            "requires": ["day_3"],
            "required_variables": {
                "vote_phase3_player_choice": None,
                "vote_phase3_time_left": 10,
            },
            "teleportable": True,
        },
        {
            "id": "route_trade_rejected",
            "title": "Route — Statu quo",
            "short": "NON",
            "label": "_3_VOTE_CONTRE",
            "category": "route",
            "kind": "route",
            "x": 2360,
            "y": 220,
            "summary": "Le commerce échoue. Le Conclave conserve l'ordre existant, mais la frustration politique s'accumule.",
            "choice": "Refus ou blocage de l'amendement commerce.",
            "consequence": "Jour 4 suit la route de l'échec du vote.",
            "requires": ["vote_commerce"],
            "required_variables": {"vote1": "NON"},
            "teleportable": True,
        },
        {
            "id": "route_trade_accepted",
            "title": "Route — Commerce adopté",
            "short": "OUI",
            "label": "_3_VOTE_POUR",
            "category": "route",
            "kind": "route",
            "x": 2360,
            "y": 560,
            "summary": "Le commerce est adopté. Nexus et Orbite s'organisent, tandis que Limen vacille.",
            "choice": "Adoption de l'amendement commerce.",
            "consequence": "Jour 4 suit la route du commerce ouvert.",
            "requires": ["vote_commerce"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_4_statu_quo",
            "title": "Jour 4 — Conséquences",
            "short": "J4",
            "label": "_4_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 2740,
            "y": 220,
            "summary": "Après l'échec du commerce, Kami annonce le vote sur la libre circulation. Sael cristallise l'opposition.",
            "choice": "Préparer le vote malgré l'échec précédent.",
            "consequence": "La route se durcit autour du refus et du regret.",
            "requires": ["route_trade_rejected"],
            "required_variables": {"vote1": "NON"},
            "teleportable": True,
        },
        {
            "id": "day_4_trade",
            "title": "Jour 4 — Conséquences",
            "short": "J4",
            "label": "_4_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 2740,
            "y": 560,
            "summary": "Après l'adoption du commerce, le Conclave découvre déjà les effets politiques de sa décision.",
            "choice": "Gérer les fractures ouvertes par l'amendement.",
            "consequence": "Une fête improvisée masque mal la tension.",
            "requires": ["route_trade_accepted"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_5_statu_quo",
            "title": "Jour 5 — Fractures internes",
            "short": "J5",
            "label": "_5_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 3120,
            "y": 220,
            "summary": "Noam observe les oppositions à la libre circulation et choisit comment agir face aux tensions.",
            "choice": "Confronter Julian ou suivre Elias vers l'observation.",
            "consequence": "Le Conclave entre dans une phase plus instable.",
            "requires": ["day_4_statu_quo"],
            "required_variables": {"vote1": "NON"},
            "teleportable": True,
        },
        {
            "id": "day_5_trade",
            "title": "Jour 5 — Fractures internes",
            "short": "J5",
            "label": "_5_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 3120,
            "y": 560,
            "summary": "Une alerte venue d'Orbite fragilise Kael. Une note anonyme rappelle que les absents ne comptent pas.",
            "choice": "Soutenir Kael, enquêter ou s'en remettre au règlement.",
            "consequence": "La route du commerce ouvre une pression plus institutionnelle.",
            "requires": ["day_4_trade"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_5_choice_julian",
            "title": "Divergence — Mise en scène",
            "short": "Julian",
            "label": "_5_0_0_JULIAN",
            "category": "scene",
            "kind": "divergence",
            "x": 3500,
            "y": 95,
            "summary": "Noam confronte Julian sur sa manière de transformer le vote en théâtre politique.",
            "choice": "Affronter la stratégie de Julian.",
            "consequence": "Le soupçon de manipulation reste actif.",
            "requires": ["day_5_statu_quo"],
            "teleportable": True,
        },
        {
            "id": "day_5_choice_observation",
            "title": "Divergence — Incident observation",
            "short": "Elias",
            "label": "_5_0_1_OBSERVATION",
            "category": "scene",
            "kind": "divergence",
            "x": 3500,
            "y": 345,
            "summary": "Noam accompagne Elias. Un incident endommage une console et laisse une trace technique inquiétante.",
            "choice": "Suivre Elias plutôt que Julian.",
            "consequence": "La surveillance du Conclave paraît moins stable.",
            "requires": ["day_5_statu_quo"],
            "teleportable": True,
        },
        {
            "id": "day_6_incident",
            "title": "Jour 6 — Incident système",
            "short": "J6",
            "label": "_6_0_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 3880,
            "y": 390,
            "summary": "Le vote sur la libre circulation tourne au fiasco. Kami se déforme et laisse filtrer une menace.",
            "choice": "Rejeter un texte devenu dangereux.",
            "consequence": "Le silence de Kami commence.",
            "requires": ["day_5_statu_quo"],
            "required_variables": {"vote1": "NON"},
            "teleportable": True,
        },
        {
            "id": "day_6_price_of_yes",
            "title": "Jour 6 — Le prix du oui",
            "short": "J6-1",
            "label": "_6_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 3880,
            "y": 640,
            "summary": "Après l'adoption du commerce, la libre circulation déchire Limen. Ryn tente de forcer une issue avant le vote.",
            "choice": "Défendre le droit de Sael à voter malgré le prix politique du refus.",
            "consequence": "Le vote échoue, la violence fracture le groupe et le chapitre 2_1 se referme.",
            "requires": ["day_5_trade"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_7_1_0",
            "title": "Jour 7 — La passagère",
            "short": "J7",
            "label": "_7_1_0_CANON",
            "category": "day",
            "kind": "day",
            "x": 4260,
            "y": 640,
            "summary": "Le groupe découvre une jeune femme dissimulée dans la livraison et doit décider s'il la cache ou s'il révèle sa présence à Kami.",
            "choice": "Cacher la rescapée ou la déclarer à Kami.",
            "consequence": "La journée se divise entre un transfert clandestin vers la chambre d'Iris et une prise en charge déclarée à l'infirmerie.",
            "requires": ["day_6_price_of_yes"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_7_1_0_0",
            "title": "Jour 7 — Passagère clandestine",
            "short": "J7-0",
            "label": "_7_1_0_CACHER_PLAN",
            "category": "day",
            "kind": "day",
            "x": 4640,
            "y": 560,
            "summary": "Kael pirate les serveurs pendant que le groupe transporte clandestinement la jeune femme jusqu'à la chambre d'Iris.",
            "choice": "Cacher la rescapée à Kami.",
            "consequence": "Le groupe gagne une alliée potentielle, mais risque l'exécution si le secret est découvert.",
            "requires": ["day_7_1_0"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_7_1_0_1",
            "title": "Jour 7 — Sursis déclaré",
            "short": "J7-1",
            "label": "_7_1_0_DECLARER_PLACEHOLDER",
            "category": "day",
            "kind": "day",
            "x": 4640,
            "y": 720,
            "summary": "Le groupe révèle la présence de la jeune femme à Kami et obtient un sursis pour la soigner à l'infirmerie.",
            "choice": "Déclarer la rescapée et exiger son transfert médical.",
            "consequence": "Kami cède temporairement ; le transport jusqu'à l'infirmerie met la coordination du groupe à l'épreuve.",
            "requires": ["day_7_1_0"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "vote_circulation",
            "title": "Vote — Libre circulation",
            "short": "Vote II",
            "label": "_6_0_1_VOTE",
            "category": "vote",
            "kind": "vote",
            "x": 4260,
            "y": 390,
            "summary": "Le Conclave vote dans un climat de dégradation système. Le texte ne paraît plus fiable.",
            "choice": "Maintenir l'ordre ou refuser une application incontrôlée.",
            "consequence": "Le rejet ouvre une séquence de silence et d'anomalies.",
            "requires": ["day_6_incident"],
            "teleportable": True,
        },
        {
            "id": "day_7_silence",
            "title": "Jour 7 — Silence de Kami",
            "short": "J7",
            "label": "_7_0_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 4640,
            "y": 390,
            "summary": "Kami ne parle plus. Le calme apparent révèle des disparitions de matériel et l'arrêt des exécutions.",
            "choice": "Profiter du calme ou chercher les fissures.",
            "consequence": "Le Conclave découvre que le système a changé sans prévenir.",
            "requires": ["vote_circulation"],
            "teleportable": True,
        },
        {
            "id": "day_8_memories",
            "title": "Jour 8 — Souvenirs volés",
            "short": "J8",
            "label": "_8_0_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 5020,
            "y": 390,
            "summary": "Des objets personnels disparaissent. Les souvenirs intimes deviennent des preuves et des armes.",
            "choice": "Enquêter dans la chambre et soutenir Kael.",
            "consequence": "La menace devient personnelle.",
            "requires": ["day_7_silence"],
            "teleportable": True,
        },
        {
            "id": "day_8_1_0_0",
            "title": "Jour 8 — Le réveil d'Anya",
            "short": "J8-0",
            "label": "_8_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 5020,
            "y": 560,
            "summary": "Anya se réveille dans la chambre d'Iris et découvre qu'elle a été recueillie au cœur du Conclave.",
            "choice": "Gagner sa confiance tout en continuant à cacher sa présence à Kami.",
            "consequence": "Une visite inattendue de Ryn fait planer le doute sur la sécurité du secret.",
            "requires": ["day_7_1_0_0"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_9_1_0_0",
            "title": "Jour 9 — Ce que Ryn savait",
            "short": "J9-0",
            "label": "_9_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 5400,
            "y": 560,
            "summary": "Noam cherche à comprendre pourquoi Ryn connaissait la présence d'Anya et découvre son intérêt pour les réseaux de passeurs.",
            "choice": "Préserver le secret d'Anya sans confronter directement Ryn.",
            "consequence": "Le silence de Ryn protège temporairement Anya, mais ses questions sur les contrôles de marchandises restent inquiétantes.",
            "requires": ["day_8_1_0_0"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_10_1_0_0",
            "title": "Jour 10 — Les passages de Ryn",
            "short": "J10-1",
            "label": "_10_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 5780,
            "y": 720,
            "summary": "Noam remonte la piste des questions de Ryn et découvre comment les archives peuvent servir à organiser des passages clandestins.",
            "choice": "Aider Ryn à exploiter les failles du système ou refuser de participer à son plan.",
            "consequence": "Le secret d'Anya est préservé, mais Noam doit choisir jusqu'où il accepte de contourner les contrôles de Kami.",
            "requires": ["day_9_1_0_0"],
            "required_variables": {"vote1": "OUI"},
            "teleportable": True,
        },
        {
            "id": "day_9_kami_return",
            "title": "Jour 9 — Retour de Kami",
            "short": "J9",
            "label": "_9_0_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 5400,
            "y": 390,
            "summary": "Kami revient dans un Conclave déjà fracturé. Le système vivant est désormais impossible à ignorer.",
            "choice": "Comprendre ce que Kami surveille encore.",
            "consequence": "La chronologie entre dans une phase plus dangereuse.",
            "requires": ["day_8_memories"],
            "teleportable": True,
        },
        {
            "id": "day_10_0_1_0",
            "title": "Jour 10 — Conséquence directe",
            "short": "J10-0",
            "label": "_10_0_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 5780,
            "y": 250,
            "summary": "Branche alternative du Jour 10 après l'échec du vote limenois. Le Conclave commence la journée sous le poids immédiat du Commandement IV.",
            "choice": "Assumer les conséquences du vote refusé.",
            "consequence": "La route sombre du Jour 10 reste à développer.",
            "requires": ["day_9_kami_return"],
            "teleportable": True,
        },
        {
            "id": "day_10_0_1_1",
            "title": "Jour 10 — Matinée lourde",
            "short": "J10",
            "label": "_10_0_1_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 5780,
            "y": 530,
            "summary": "Noam se réveille avec un mal de crâne inhabituel dans un Conclave trop chaud et trop silencieux. À la cafétéria, Elias annonce que la majorité des campements s'est dispersée, mais Ryn accuse Kami d'avoir piégé tout le monde.",
            "choice": "Rejoindre la cafétéria et empêcher la discussion de rompre autour de la table.",
            "consequence": "La colère contre Kami devient un risque interne pour le groupe.",
            "requires": ["day_9_kami_return"],
            "teleportable": True,
        },
        {
            "id": "day_11_0_1_1",
            "title": "Jour 11 — Archives effacées",
            "short": "J11",
            "label": "_11_0_1_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 6160,
            "y": 530,
            "summary": "Encore affaibli par sa fièvre, Noam recherche la silhouette aperçue la veille et découvre que les images de surveillance ont été effacées.",
            "choice": "Rejoindre la cafétéria et empêcher la discussion de rompre autour de la table.",
            "consequence": "La colère contre Kami devient un risque interne pour le groupe.",
            "requires": ["day_10_0_1_1"],
            "teleportable": True,
        },
        {
            "id": "day_12_0_1_1",
            "title": "Jour 12 — Intrusion",
            "short": "J12",
            "label": "_12_0_1_1_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 6540,
            "y": 530,
            "summary": "Noam se réveille en sursaut après un bruit dans sa chambre. La fouille transforme le doute en menace intime.",
            "choice": "Fouiller la chambre malgré la peur de céder à la paranoïa.",
            "consequence": "Le soupçon d'une intrusion récente s'ajoute à la méfiance envers le groupe.",
            "requires": ["day_11_0_1_1"],
            "teleportable": True,
        },
        {
            "id": "day_13_0_1_1_0",
            "title": "Jour 13 — Intrusion",
            "short": "J13",
            "label": "_13_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 6920,
            "y": 530,
            "summary": "Noam se réveille en sursaut alors que son brouilleur se fait démonter.",
            "choice": "Fouiller la chambre malgré la peur de céder à la paranoïa.",
            "consequence": "Le soupçon d'une intrusion récente s'ajoute à la méfiance envers le groupe.",
            "requires": ["day_12_0_1_1"],
            "teleportable": True,
        },
        {
            "id": "day_14_0_1_1_0",
            "title": "Jour 14 — Intrusion",
            "short": "J14",
            "label": "_14_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 7300,
            "y": 530,
            "summary": "Noam se réveille en sursaut alors que son brouilleur se fait démonter.",
            "choice": "Fouiller la chambre malgré la peur de céder à la paranoïa.",
            "consequence": "Le soupçon d'une intrusion récente s'ajoute à la méfiance envers le groupe.",
            "requires": ["day_13_0_1_1_0"],
            "teleportable": True,
        },
        {
            "id": "day_15_0_1_1_0",
            "title": "Jour 15 — Images impossibles",
            "short": "J15",
            "label": "_15_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 7680,
            "y": 530,
            "summary": "Noam renonce au vote pour consulter les caméras avec Kael. Les archives montrent Kael volant sa propre photo, puis entrant dans la chambre de Noam pour prendre le dessin de Juliette.",
            "choice": "Privilégier l'enquête aux responsabilités du vote et confronter Kael aux images.",
            "consequence": "Le comportement de Kael bascule et Noam perd connaissance après une vision du laboratoire.",
            "requires": ["day_14_0_1_1_0"],
            "required_variables": {"day_id": 15, "current_day": 15, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_16_0_1_1_0",
            "title": "Jour 16 — Mémoire altérée",
            "short": "J16",
            "label": "_16_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 8060,
            "y": 530,
            "summary": "Noam se réveille avec un trou net dans sa mémoire. Aux archives, Sael et lui découvrent la procédure M16 — altération mnésique — dans leurs dossiers médicaux.",
            "choice": "Chercher une preuve qui ne dépende ni des souvenirs de Noam ni de ceux de Kael.",
            "consequence": "La référence M16 disparaît du terminal sous leurs yeux, confirmant une intervention active du système.",
            "requires": ["day_15_0_1_1_0"],
            "required_variables": {"day_id": 16, "current_day": 16, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_17_0_1_1_0",
            "title": "Jour 17 — Les murs répondent",
            "short": "J17",
            "label": "_17_0_1_1_0_ANNONCE_KAMI",
            "category": "day",
            "kind": "day",
            "x": 8440,
            "y": 530,
            "summary": "Les représentants découvrent que douze dossiers portent la mention M16 et suspendent les votes. Kami leur répond que le Conclave prendra fin au jour 21 s'ils persistent.",
            "choice": "Maintenir la protestation puis ouvrir la grille derrière laquelle Noam entend du mouvement.",
            "consequence": "Le conduit relie les chambres et mène à une treizième ouverture où une présence laisse une trace fraîche.",
            "requires": ["day_16_0_1_1_0"],
            "required_variables": {"day_id": 17, "current_day": 17, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_18_0_1_1_0",
            "title": "Jour 18 — Derrière les murs",
            "short": "J18",
            "label": "_18_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 8820,
            "y": 530,
            "summary": "Mara rejoint Noam dans le réseau technique. Ils découvrent une salle de maintenance des Goumi, plusieurs embranchements et une trappe qu'ils ne peuvent pas ouvrir.",
            "choice": "Explorer avec Mara tout en gardant un chemin de retour vers les dortoirs.",
            "consequence": "Noam prévient Elias, mais une présence circule encore derrière sa grille pendant la nuit.",
            "requires": ["day_17_0_1_1_0"],
            "required_variables": {"day_id": 18, "current_day": 18, "current_period": "Nuit"},
            "teleportable": True,
        },
        {
            "id": "day_19_0_1_1_0",
            "title": "Jour 19 — Elle était là",
            "short": "J19",
            "label": "_19_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 9200,
            "y": 530,
            "summary": "Mara affirme n'avoir jamais exploré les conduits avec Noam. Le groupe sécurise les chambres, mais Noam retourne seul dans le réseau en suivant les bruits.",
            "choice": "Poursuivre la présence malgré l'épuisement, armé d'une lampe et d'un couteau.",
            "consequence": "Dans la salle des Goumi, Noam découvre le corps immobile de Mara alors qu'il l'a vue vivante le matin même.",
            "requires": ["day_18_0_1_1_0"],
            "required_variables": {"day_id": 19, "current_day": 19, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_20_0_1_1_0",
            "title": "Jour 20 — Le corps disparu",
            "short": "J20",
            "label": "_20_0_1_1_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 9580,
            "y": 530,
            "summary": "Noam annonce la mort de Mara avant de la voir entrer vivante dans la cafétéria. De retour dans la salle cachée avec Iris et Kael, il découvre que le corps a disparu.",
            "choice": "Maintenir son récit malgré le doute des autres et la disparition de toute preuve.",
            "consequence": "Iris assomme Noam après une lutte. Attaché à l'infirmerie, il conclut qu'un traître agit parmi eux.",
            "requires": ["day_19_0_1_1_0"],
            "required_variables": {"day_id": 20, "current_day": 20, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "split_noam_iris",
            "title": "CRITICAL CHOICE — Le couteau",
            "short": "CHOIX",
            "label": "_20_0_1_1_IRIS_CONFRONTATION",
            "category": "scene",
            "kind": "divergence",
            "x": 9960,
            "y": 530,
            "summary": "Dans la salle des Goumi, Iris demande une dernière fois à Noam de poser le couteau. Le choix de le garder ou de le lâcher sépare définitivement les routes.",
            "choice": "Lâcher le couteau ou le garder.",
            "consequence": "Le garder déclenche la confrontation et les QTE. Le lâcher ouvre une route fondée sur la confiance d'Iris et la question de Kael.",
            "requires": ["day_20_0_1_1_0"],
            "teleportable": True,
        },
        {
            "id": "qte_noam_iris",
            "title": "Confrontation — Noam / Iris",
            "short": "QTE",
            "label": "_20_0_1_1_GARDER_COUTEAU",
            "category": "scene",
            "kind": "divergence",
            "x": 10340,
            "y": 330,
            "summary": "Noam refuse de lâcher le couteau. Iris tente de le désarmer et la confrontation devient physique.",
            "choice": "Réussir ou rater les quatre QTE.",
            "consequence": "La réussite révèle brutalement les Doppelgängers ; l'échec mène au Jour 21 déjà existant.",
            "requires": ["split_noam_iris"],
            "required_variables": {"j20_knife_choice": "keep"},
            "teleportable": True,
        },
        {
            "id": "choice_kael_depart",
            "title": "CRITICAL CHOICE — La navette",
            "short": "CHOIX",
            "label": "_20_0_1_1_KAEL_QUESTION",
            "category": "scene",
            "kind": "divergence",
            "x": 10340,
            "y": 730,
            "summary": "Après que Noam a lâché le couteau et quitté la salle avec Iris et Kael, Kael lui pose une question étrange sur le départ du lendemain et quelqu'un qui resterait coincé derrière.",
            "choice": "Partir malgré tout ou rester s'il existe encore une chance de sauver celui qui reste.",
            "consequence": "La réponse de Noam détermine la position de Kael et ouvre deux entrées différentes pour le Jour 21.",
            "requires": ["split_noam_iris"],
            "required_variables": {"j20_knife_choice": "drop"},
            "teleportable": True,
        },
        {
            "id": "day_21_0_1_1_0",
            "title": "Jour 21 — Écho des cendres",
            "short": "J21",
            "label": "_21_0_1_1_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 10720,
            "y": 470,
            "summary": "Après l'échec de la confrontation avec Iris, Noam se retrouve attaché à l'infirmerie. Mara neutralise la caméra avant qu'un double parfait de Noam ne sorte du conduit.",
            "choice": "Route issue du couteau gardé et des QTE échoués.",
            "consequence": "Le double tue Noam, prend sa place et quitte le Conclave avec les autres représentants.",
            "requires": ["qte_noam_iris"],
            "required_variables": {"j20_knife_choice": "keep", "day_id": 21, "current_day": 21, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_21_kael_leave",
            "title": "Jour 21 — Partir demain",
            "short": "J21",
            "label": "_21_0_1_1_0_1_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 10720,
            "y": 690,
            "summary": "Noam répond à Kael qu'il monterait dans la navette si rester ne pouvait plus sauver la personne coincée derrière.",
            "choice": "« Je monte dans la navette. »",
            "consequence": "Cette réponse ouvre la branche où la priorité donnée au départ immédiat pèsera sur les décisions des Doppelgängers.",
            "requires": ["choice_kael_depart"],
            "required_variables": {"j20_knife_choice": "drop", "j20_kael_depart_choice": "leave", "day_id": 21, "current_day": 21, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "ending_at_my_place",
            "title": "FIN — À ma place",
            "short": "FIN",
            "label": "_21_0_1_1_0_1_FIN_A_MA_PLACE",
            "category": "ending",
            "kind": "ending",
            "x": 11100,
            "y": 620,
            "summary": "Le Doppelgänger de Noam remporte la lutte, élimine l'original et monte dans la navette sous son identité.",
            "choice": "Échouer au QTE contre le Doppelgänger de Noam.",
            "consequence": "Le Doppelgänger retourne sur Terre à la place de Noam, avec ses souvenirs et son attachement à Juliette.",
            "requires": ["day_21_kael_leave"],
            "teleportable": True,
        },
        {
            "id": "ending_left_behind",
            "title": "FIN — Celui qu'on laisse derrière",
            "short": "FIN",
            "label": "_21_0_1_1_0_1_FIN_LAISSE_DERRIERE",
            "category": "ending",
            "kind": "ending",
            "x": 11100,
            "y": 790,
            "summary": "Noam survit à l'attaque avec l'aide d'Iris et quitte le Conclave, tandis que son Doppelgänger reste attaché dans la station.",
            "choice": "Réussir le QTE contre le Doppelgänger de Noam.",
            "consequence": "Noam applique sa propre réponse de la veille : il monte dans la navette et laisse son double derrière lui.",
            "requires": ["day_21_kael_leave"],
            "teleportable": True,
        },
        {
            "id": "day_21_kael_stay",
            "title": "Jour 21 — Ne laisser personne",
            "short": "J21",
            "label": "_21_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 10720,
            "y": 870,
            "summary": "Le départ est annulé : certains représentants ont demandé à poursuivre le Conclave jusqu'au jour 30. Une anomalie apparaît ensuite dans la livraison.",
            "choice": "« Je reste s'il y a encore une chance de le sortir. »",
            "consequence": "Les Doppelgängers prolongent le Conclave. Des plaques métalliques destinées à être automatiquement réapprovisionnées sont introuvables.",
            "requires": ["choice_kael_depart"],
            "required_variables": {"j20_knife_choice": "drop", "j20_kael_depart_choice": "stay", "day_id": 21, "current_day": 21, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_22_0_1_1_0_0",
            "title": "Jour 22 — Derrière les murs",
            "short": "J22",
            "label": "_22_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 11100,
            "y": 930,
            "summary": "Une plaisanterie sur les fantômes pousse Iris à rappeler que du matériel disparu avait déjà été retrouvé dans la salle cachée. Elias part seul vérifier les conduits et revient changé.",
            "choice": "Suite de la route « Je reste s'il y a encore une chance de le sortir. »",
            "consequence": "Elias est remplacé par son Doppelgänger, les plaques de fortune sont abandonnées et Kami annonce pour le jour 24 un nouveau Commandement sur le toit, l'eau et la nourriture.",
            "requires": ["day_21_kael_stay"],
            "required_variables": {"j20_knife_choice": "drop", "j20_kael_depart_choice": "stay", "day_id": 22, "current_day": 22, "current_period": "Matin", "j22_elias_replaced": False, "j22_vote_announced": False},
            "teleportable": True,
        },
        {
            "id": "day_23_0_1_1_0_0",
            "title": "Jour 23 — Rien dans sa tête",
            "short": "J23",
            "label": "_23_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 11480,
            "y": 930,
            "summary": "Sael s'inquiète des hallucinations de Noam et lui fait passer une batterie d'examens à l'infirmerie sous la surveillance d'Iris. L'IRM ne révèle aucune anomalie.",
            "choice": "Accepter de vérifier si les visions de Noam ont une origine médicale.",
            "consequence": "L'hypothèse d'un trouble neurologique perd du poids : si Noam a bien vu Mara morte, le problème est ailleurs.",
            "requires": ["day_22_0_1_1_0_0"],
            "required_variables": {"j20_knife_choice": "drop", "j20_kael_depart_choice": "stay", "day_id": 23, "current_day": 23, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_24_0_1_1_0_0",
            "title": "Jour 24 — Les besoins vitaux",
            "short": "J24",
            "label": "_24_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 11860,
            "y": 930,
            "summary": "Le groupe débat du nouveau Commandement sur le toit, l'eau et l'alimentation. Noam aide à faire basculer les hésitants vers l'adoption.",
            "choice": "Soutenir le texte malgré les risques d'interprétation par Kami.",
            "consequence": "Le Commandement est adopté dans une ambiance exceptionnellement chaleureuse ; Julian et Elen transforment le vote en petite victoire collective.",
            "requires": ["day_23_0_1_1_0_0"],
            "required_variables": {"j20_knife_choice": "drop", "j20_kael_depart_choice": "stay", "day_id": 24, "current_day": 24, "current_period": "Matin", "j24_vital_vote": None},
            "teleportable": True,
        },
        {
            "id": "vote_vital_needs_j24",
            "title": "Vote — Besoins vitaux",
            "short": "Vote J24",
            "label": "_24_0_1_1_0_0_VOTE",
            "category": "vote",
            "kind": "vote",
            "x": 12050,
            "y": 760,
            "summary": "Le Conclave vote sur un nouveau Commandement garantissant un toit, de l'eau potable et une alimentation suffisante.",
            "choice": "Voter pour ou s'abstenir sans bloquer l'unanimité des suffrages exprimés.",
            "consequence": "Le texte est adopté et offre au groupe une rare victoire commune.",
            "requires": ["day_24_0_1_1_0_0"],
            "required_variables": {"j24_vital_vote": None},
            "teleportable": True,
        },
        {
            "id": "day_25_0_1_1_0_0",
            "title": "Jour 25 — La preuve",
            "short": "J25",
            "label": "_25_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 12240,
            "y": 930,
            "summary": "Iris et Noam retournent dans les conduits après avoir retrouvé un morceau de la veste de Mara. Iris découvre à son tour le corps de Mara alors que sa copie circule toujours dans le Conclave. Le joueur examine la veste intacte, cadre une photographie, puis reproduit le signal frappé à la porte d'Iris.",
            "choice": "Garder temporairement la découverte secrète pour éviter d'alerter les imposteurs.",
            "consequence": "L'existence d'au moins un remplacement devient incontestable. Kami annonce parallèlement le vote du jour 27.",
            "requires": ["vote_vital_needs_j24"],
            "required_variables": {"day_id": 25, "current_day": 25, "current_period": "Matin", "j25_double_proof": False},
            "teleportable": True,
        },
        {
            "id": "day_26_0_1_1_0_0",
            "title": "Jour 26 — Face caméra",
            "short": "J26",
            "label": "_26_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 12620,
            "y": 930,
            "summary": "Noam décide de profiter de l'exposition mondiale du Conclave pour révéler publiquement ce qu'Iris et lui ont découvert. Tomas surprend l'intervention et prévient le groupe.",
            "choice": "Choisir comment présenter publiquement l'existence probable des doubles.",
            "consequence": "Le secret devient irréversible : les Doppelgängers comprennent que leurs identités seront désormais suspectées à leur arrivée sur Terre.",
            "requires": ["day_25_0_1_1_0_0"],
            "required_variables": {"day_id": 26, "current_day": 26, "current_period": "Matin", "j26_camera_tone": None, "j26_public_reveal": False},
            "teleportable": True,
        },
        {
            "id": "choice_face_camera_j26",
            "title": "Choix critique — Face caméra",
            "short": "Caméra",
            "label": "_26_0_1_1_0_0_CAMERA",
            "category": "route",
            "kind": "divergence",
            "x": 12810,
            "y": 760,
            "summary": "Noam rend ses soupçons publics devant les caméras du Conclave, en choisissant de s'en tenir aux faits ou d'accuser clairement des doubles de remplacer les représentants.",
            "choice": "Raconter les faits ou nommer explicitement l'hypothèse des Doppelgängers.",
            "consequence": "Dans les deux formulations, l'information devient mondiale et détruit l'intérêt stratégique des DG à rester discrets.",
            "requires": ["day_26_0_1_1_0_0"],
            "required_variables": {"j26_camera_tone": None, "j26_public_reveal": False},
            "teleportable": True,
        },
        {
            "id": "day_27_0_1_1_0_0",
            "title": "Jour 27 — Rupture",
            "short": "J27",
            "label": "_27_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 13000,
            "y": 930,
            "summary": "La révélation publique rend la stratégie d'infiltration inutile. Mara, Kael et Elias cessent de nier et tentent d'isoler les représentants encore humains.",
            "choice": "Rester groupés malgré l'impossibilité de savoir qui a déjà été remplacé.",
            "consequence": "Les DG passent à l'attaque ouverte. Le vote du jour se déroule malgré la fuite et la fracture du groupe.",
            "requires": ["choice_face_camera_j26"],
            "required_variables": {"day_id": 27, "current_day": 27, "current_period": "Matin", "j27_attack_started": False, "j27_vote_result": None},
            "teleportable": True,
        },
        {
            "id": "vote_detention_j27",
            "title": "Vote — Détention contestable",
            "short": "Vote J27",
            "label": "_27_0_1_1_0_0_VOTE",
            "category": "vote",
            "kind": "vote",
            "x": 13190,
            "y": 760,
            "summary": "En pleine chasse aux doubles, les représentants encore réunis votent sur le droit de connaître et contester le motif d'une privation de liberté.",
            "choice": "Maintenir le processus politique alors que le Conclave s'effondre autour d'eux.",
            "consequence": "Le texte est adopté, sans véritable célébration.",
            "requires": ["day_27_0_1_1_0_0"],
            "required_variables": {"j27_vote_result": None},
            "teleportable": True,
        },
        {
            "id": "day_28_0_1_1_0_0",
            "title": "Jour 28 — La station change de mains",
            "short": "J28",
            "label": "_28_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 13380,
            "y": 930,
            "summary": "Les disparitions et retours suspects se multiplient. Noam et Iris ne peuvent plus déterminer si Ryn, Tomas, Julian ou Elen sont encore les originaux.",
            "choice": "Continuer à rester ensemble et refuser les séparations.",
            "consequence": "Kami annonce le dernier vote pour 8 h au jour 30, suivi immédiatement du départ, ainsi que le remplacement des exécutions par l'effacement de mémoire.",
            "requires": ["vote_detention_j27"],
            "required_variables": {"day_id": 28, "current_day": 28, "current_period": "Matin", "j28_last_vote_announced": False},
            "teleportable": True,
        },
        {
            "id": "day_29_0_1_1_0_0",
            "title": "Jour 29 — Plus que deux",
            "short": "J29",
            "label": "_29_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 13760,
            "y": 930,
            "summary": "Noam et Iris pensent être les deux seuls représentants encore non remplacés. Tous les autres leur paraissent anormalement calmes et coordonnés.",
            "choice": "Se barricader ensemble dans la chambre d'Iris, dont l'aération est encore condamnée.",
            "consequence": "Les voix des anciens camarades se relaient derrière la porte pendant toute la nuit, sans parvenir à les faire sortir.",
            "requires": ["day_28_0_1_1_0_0"],
            "required_variables": {"day_id": 29, "current_day": 29, "current_period": "Matin"},
            "teleportable": True,
        },
        {
            "id": "day_30_0_1_1_0_0",
            "title": "Jour 30 — Le dernier matin",
            "short": "J30",
            "label": "_30_0_1_1_0_0_REVEIL",
            "category": "day",
            "kind": "day",
            "x": 14140,
            "y": 930,
            "summary": "Toujours barricadés, Noam et Iris participent au dernier vote. L'amendement remplaçant l'élimination par l'effacement de mémoire est adopté avant l'arrivée de la navette.",
            "choice": "Trouver un chemin vers le sas en moins de trente minutes.",
            "consequence": "Le couloir a été entièrement barricadé de l'extérieur. Il ne reste que deux options : forcer le passage ou reprendre les conduits.",
            "requires": ["day_29_0_1_1_0_0"],
            "required_variables": {"day_id": 30, "current_day": 30, "current_period": "Matin", "j30_escape_route": None, "j30_final_vote": "adopted"},
            "teleportable": True,
        },
        {
            "id": "vote_memory_j30",
            "title": "Vote — Intégrité de la mémoire",
            "short": "Vote J30",
            "label": "_30_0_1_1_0_0_VOTE",
            "category": "vote",
            "kind": "vote",
            "x": 14330,
            "y": 760,
            "summary": "Le dernier amendement remplace l'élimination par l'effacement de mémoire en cas de violation des Commandements.",
            "choice": "Le vote a lieu sans Noam et Iris, enfermés dans leur chambre.",
            "consequence": "Le texte est adopté à l'unanimité des votants. La navette est annoncée pour dans trente minutes.",
            "requires": ["day_30_0_1_1_0_0"],
            "required_variables": {"j30_final_vote": "adopted"},
            "teleportable": True,
        },
        {
            "id": "choice_escape_j30",
            "title": "CRITICAL CHOICE — Une seule issue",
            "short": "Choix final",
            "label": "_30_0_1_1_0_0_REVEIL",
            "category": "route",
            "kind": "divergence",
            "x": 14520,
            "y": 930,
            "summary": "La porte d'Iris est bloquée par une barricade construite depuis le couloir. Le temps avant le départ s'écoule.",
            "choice": "Forcer la barricade ou passer par les conduits.",
            "consequence": "Le choix détermine si Noam et Iris ratent le départ sans comprendre toute la vérité ou découvrent le secret du Polymorphe.",
            "requires": ["vote_memory_j30"],
            "required_variables": {"j30_escape_route": None},
            "teleportable": True,
        },
        {
            "id": "ending_too_late_j30",
            "title": "FIN — L'embarquement manqué",
            "short": "FIN 05",
            "label": "_30_0_1_1_0_0_BARRICADE",
            "category": "ending",
            "kind": "ending",
            "x": 14900,
            "y": 820,
            "summary": "Noam et Iris tentent de dégager la barricade. Une manipulation réussie révèle les doubles dans la navette ; un échec les condamne à un départ vers une station de production.",
            "choice": "Forcer la barricade.",
            "consequence": "Les Doppelgängers atteignent la Terre tandis que Noam et Iris restent prisonniers de la station.",
            "requires": ["choice_escape_j30"],
            "required_variables": {"j30_escape_route": "barricade", "j30_barricade_success": False},
            "teleportable": True,
        },
        {
            "id": "ending_thirteenth_representative",
            "title": "FIN — Derrière les doubles",
            "short": "FIN 06",
            "label": "_30_0_1_1_0_0_VENTILATION",
            "category": "ending",
            "kind": "ending",
            "x": 14900,
            "y": 1040,
            "summary": "En passant par les conduits, Noam et Iris découvrent les corps originaux et les indices qui révèlent la nature du Polymorphe.",
            "choice": "Passer par les conduits.",
            "consequence": "La confrontation avec le Polymorphe mène à la dernière issue de cette branche.",
            "requires": ["choice_escape_j30"],
            "required_variables": {"j30_escape_route": "ventilation"},
            "teleportable": True,
        },
        {
            "id": "ending_doppelganger_revelation",
            "title": "FIN — Derrière les visages",
            "short": "FIN",
            "label": "_20_0_1_1_IRIS_QTE_REUSSITE",
            "category": "ending",
            "kind": "ending",
            "x": 10720,
            "y": 230,
            "summary": "Noam réussit les quatre QTE face à Iris. La lutte tourne au drame avant que Kael révèle sa véritable nature et que la salle de fabrication des Doppelgängers soit découverte.",
            "choice": "Réussir les quatre QTE face à Iris.",
            "consequence": "Fin alternative : les corps originaux et le procédé de remplacement sont révélés.",
            "requires": ["qte_noam_iris"],
            "required_variables": {"j20_knife_choice": "keep"},
            "teleportable": True,
        },
        {
            "id": "ending_echoes_ashes",
            "title": "FIN — Écho des cendres",
            "short": "FIN",
            "label": "_21_0_1_1_EPILOGUE",
            "category": "ending",
            "kind": "ending",
            "x": 11100,
            "y": 470,
            "summary": "Noam est éliminé puis remplacé par son Doppelgänger. La navette quitte le Conclave avec la copie de Noam parmi les représentants.",
            "choice": "Échouer à empêcher le remplacement de Noam.",
            "consequence": "Fin de la route : le Doppelgänger de Noam retourne sur Terre avec les survivants.",
            "requires": ["day_21_0_1_1_0"],
            "teleportable": True,
        },
        {
            "id": "debug_conclave_map",
            "title": "Debug — Carte du Conclave",
            "short": "Map",
            "label": "OPEN_CONCLAVE_MAP",
            "category": "debug",
            "kind": "debug",
            "x": 500,
            "y": 760,
            "summary": "Entrée directe vers la carte d'exploration du Conclave.",
            "choice": "Accès de test.",
            "consequence": "Réservé au mode développeur.",
            "requires": [],
            "dev_only": True,
            "teleportable": True,
        },
    ]

    ROADMAP_NODE_BY_ID = {node["id"]: node for node in ROADMAP_NODES}

    def roadmap_node(node_id):
        return ROADMAP_NODE_BY_ID.get(node_id)

    def roadmap_nodes_for_category(category):
        if category in (None, "all"):
            return list(ROADMAP_NODES)
        return [node for node in ROADMAP_NODES if node.get("category") == category]

    def roadmap_unlock(node_id, set_current=True):
        if node_id not in ROADMAP_NODE_BY_ID:
            renpy.notify("Roadmap: nœud inconnu - %s" % node_id)
            return
        if node_id not in store.roadmap_unlocked_nodes:
            store.roadmap_unlocked_nodes.append(node_id)
        if node_id not in store.roadmap_discovered_nodes:
            store.roadmap_discovered_nodes.append(node_id)
        if set_current:
            store.roadmap_current_node = node_id
        renpy.restart_interaction()

    def roadmap_complete(node_id):
        roadmap_unlock(node_id, set_current=False)
        if node_id not in store.roadmap_completed_nodes:
            store.roadmap_completed_nodes.append(node_id)
        renpy.restart_interaction()

    def roadmap_set_current(node_id):
        if node_id in ROADMAP_NODE_BY_ID:
            roadmap_unlock(node_id, set_current=False)
            store.roadmap_current_node = node_id
            renpy.restart_interaction()

    def roadmap_label_seen(node):
        label = node.get("label")
        return bool(label and renpy.seen_label(label))

    def roadmap_is_discovered(node):
        node_id = node["id"]
        return (
            store.roadmap_dev_mode
            or node_id in store.roadmap_unlocked_nodes
            or node_id in store.roadmap_discovered_nodes
            or roadmap_label_seen(node)
        )

    def roadmap_required_met(node):
        if store.roadmap_dev_mode:
            return True
        for requirement in node.get("requires", []):
            req_node = ROADMAP_NODE_BY_ID.get(requirement)
            if not req_node:
                return False
            if not roadmap_is_discovered(req_node):
                return False
        return True

    def roadmap_should_show(node):
        if node.get("dev_only") and not store.roadmap_dev_mode:
            return False
        if node.get("kind") == "day" or node.get("category") == "day":
            return True
        return True

    def roadmap_status(node):
        node_id = node["id"]
        if node.get("dev_only") and not store.roadmap_dev_mode:
            return "hidden"
        if store.roadmap_current_node == node_id:
            return "current"
        if node_id in store.roadmap_completed_nodes or roadmap_label_seen(node):
            return "done"
        if roadmap_is_discovered(node):
            return "available"
        if roadmap_required_met(node):
            return "locked"
        return "unknown"

    def roadmap_status_label(node):
        status = roadmap_status(node)
        if roadmap_is_ending(node):
            return kd_tr({
                "current": "Fin en cours",
                "done": "Fin découverte",
                "available": "Fin accessible",
                "locked": "Fin non découverte",
                "unknown": "Fin non découverte",
                "hidden": "Accès refusé par Kami",
            }.get(status, "Fin"))
        return kd_tr({
            "current": "En cours",
            "done": "Terminé",
            "available": "Accès autorisé",
            "locked": "Nœud narratif verrouillé",
            "unknown": "Données non découvertes",
            "hidden": "Accès refusé par Kami",
        }.get(status, "Statut inconnu"))

    def roadmap_can_teleport(node):
        if not node or not node.get("teleportable", False):
            return False
        label = node.get("label")
        if not label or not renpy.has_label(label):
            return False
        if store.roadmap_dev_mode:
            return True
        return roadmap_is_discovered(node)

    def roadmap_visual_kind(node):
        status = roadmap_status(node)
        if status in ("locked", "unknown"):
            return status
        if roadmap_is_ending(node):
            return "ending"
        if status == "current":
            return "current"
        if status == "done":
            return "done"
        return node.get("kind", "day")

    def roadmap_node_bg(node, hover=False):
        kind = roadmap_visual_kind(node)
        table = {
            "current": "gui/roadmap/nodes/roadmap_node_current.png",
            "done": "gui/roadmap/nodes/roadmap_node_done.png",
            "locked": "gui/roadmap/nodes/roadmap_node_locked.png",
            "unknown": "gui/roadmap/nodes/roadmap_node_unknown.png",
            "vote": "gui/roadmap/nodes/roadmap_node_vote_hover.png" if hover else "gui/roadmap/nodes/roadmap_node_vote_idle.png",
            "route": "gui/roadmap/nodes/roadmap_node_route_hover.png" if hover else "gui/roadmap/nodes/roadmap_node_route_idle.png",
            "divergence": "gui/roadmap/nodes/roadmap_node_divergence.png",
            "ending": "gui/roadmap/nodes/roadmap_node_divergence.png",
            "debug": "gui/roadmap/nodes/roadmap_node_route_hover.png" if hover else "gui/roadmap/nodes/roadmap_node_route_idle.png",
        }
        return table.get(kind, "gui/roadmap/nodes/roadmap_node_main_hover.png" if hover else "gui/roadmap/nodes/roadmap_node_main_idle.png")

    def roadmap_icon(node):
        kind = node.get("kind", "day")
        if roadmap_status(node) in ("locked", "unknown"):
            return "gui/roadmap/icons/roadmap_icon_locked.png"
        return {
            "day": "gui/roadmap/icons/roadmap_icon_day.png",
            "vote": "gui/roadmap/icons/roadmap_icon_vote.png",
            "route": "gui/roadmap/icons/roadmap_icon_route.png",
            "divergence": "gui/roadmap/icons/roadmap_icon_choice.png",
            "scene": "gui/roadmap/icons/roadmap_icon_scene.png",
            "ending": "gui/roadmap/icons/roadmap_icon_kami.png",
            "debug": "gui/roadmap/icons/roadmap_icon_kami.png",
        }.get(kind, "gui/roadmap/icons/roadmap_icon_scene.png")

    def roadmap_is_redacted(node):
        return bool(
            node
            and not store.roadmap_dev_mode
            and roadmap_status(node) in ("locked", "unknown")
        )

    def roadmap_display_title(node):
        if roadmap_is_redacted(node):
            return kd_tr("Données non découvertes")
        return kd_tr(node.get("title", node["id"]))

    def roadmap_display_summary(node):
        if roadmap_is_redacted(node):
            return kd_tr("Kami refuse l'accès à ce fragment. Continuez la chronologie pour l'identifier.")
        return kd_tr(node.get("summary", "Résumé à compléter."))

    def roadmap_edge_status(source_id, target_id):
        source = ROADMAP_NODE_BY_ID.get(source_id)
        target = ROADMAP_NODE_BY_ID.get(target_id)
        if not source or not target:
            return "locked"
        if roadmap_status(target) in ("unknown", "locked"):
            return "locked"
        if roadmap_is_day(source) and roadmap_is_day(target):
            if target.get("y", 0) > source.get("y", 0) + 40:
                return "alt"
            if target.get("y", 0) < source.get("y", 0) - 40:
                return "vote"
        if target.get("kind") == "ending":
            return "ending"
        if target.get("kind") == "divergence":
            return "alt"
        if target.get("kind") == "route":
            return "alt"
        if target.get("kind") == "vote":
            return "vote"
        return "active"

    def roadmap_is_day(node):
        return bool(node and (node.get("kind") == "day" or node.get("category") == "day"))

    def roadmap_is_ending(node):
        return bool(node and (node.get("kind") == "ending" or node.get("category") == "ending"))

    def roadmap_is_divergence(node):
        return bool(node and node.get("kind") == "divergence")

    def roadmap_is_timeline_node(node):
        return bool(node and (roadmap_is_day(node) or roadmap_is_ending(node) or roadmap_is_divergence(node)))

    def roadmap_timeline_predecessors(node):
        """Return the nearest visible roadmap nodes behind a node, skipping hidden technical nodes."""
        result = []
        visited = set()

        def visit(node_id):
            if node_id in visited:
                return
            visited.add(node_id)
            candidate = ROADMAP_NODE_BY_ID.get(node_id)
            if not candidate:
                return
            if roadmap_is_timeline_node(candidate):
                if candidate["id"] not in result:
                    result.append(candidate["id"])
                return
            for requirement in candidate.get("requires", []):
                visit(requirement)

        for requirement in node.get("requires", []):
            visit(requirement)
        return result

    def roadmap_map_size(nodes=None):
        nodes = list(nodes) if nodes is not None else [node for node in ROADMAP_NODES if roadmap_is_timeline_node(node)]
        if not nodes:
            return 1280, 800
        max_x = max([node["x"] for node in nodes]) + 390
        max_y = max([node["y"] for node in nodes]) + 190
        return max(1280, max_x), max(800, max_y)

    def roadmap_fit_zoom(nodes=None, view_w=1280, view_h=800):
        map_w, map_h = roadmap_map_size(nodes)
        return max(0.12, min(0.78, min(
            float(view_w - 56) / float(map_w),
            float(view_h - 56) / float(map_h),
        )))

    def roadmap_apply_node_setup(node_id):
        node = ROADMAP_NODE_BY_ID.get(node_id)
        if not node:
            return
        for var_name, var_value in node.get("required_variables", {}).items():
            setattr(store, var_name, var_value)
        setup_label = node.get("setup")
        if setup_label and renpy.has_label(setup_label):
            renpy.call_in_new_context(setup_label)

    def roadmap_queue_clean_jump(node_id):
        """
        A roadmap teleport begins a NEW playthrough at the selected node.
        A normal jump retains all variables from the previous timeline.
        Save only roadmap progress and the destination across a full restart.
        """
        node = ROADMAP_NODE_BY_ID.get(node_id)
        if not node or not node.get("teleportable", False):
            renpy.notify("Roadmap: destination invalide.")
            return
        label = node.get("label")
        if not label or not renpy.has_label(label):
            renpy.notify("Roadmap: label introuvable - %s" % label)
            return

        # persistent is only a transport envelope, cleared at the next start.
        persistent.kd_roadmap_transfer = {
            "target": node_id,
            "unlocked": list(store.roadmap_unlocked_nodes),
            "discovered": list(store.roadmap_discovered_nodes),
            "completed": list(store.roadmap_completed_nodes),
            "dev_mode": bool(store.roadmap_dev_mode),
        }
        renpy.save_persistent()
        # Crucial: reset every default variable, not only the few in
        # required_variables. Also removes stale outfit locks and flags.
        renpy.full_restart(transition=None)

    def roadmap_restore_clean_jump():
        """Called from start, after the store has been recreated."""
        transfer = getattr(persistent, "kd_roadmap_transfer", None)
        if not isinstance(transfer, dict):
            return None

        # Consume the request first to avoid an accidental repeat after a crash.
        persistent.kd_roadmap_transfer = None
        renpy.save_persistent()
        node_id = transfer.get("target")
        node = ROADMAP_NODE_BY_ID.get(node_id)
        if not node or not renpy.has_label(node.get("label", "")):
            return None

        store.roadmap_unlocked_nodes = list(transfer.get("unlocked", []))
        store.roadmap_discovered_nodes = list(transfer.get("discovered", []))
        store.roadmap_completed_nodes = list(transfer.get("completed", []))
        store.roadmap_dev_mode = bool(transfer.get("dev_mode", False))
        roadmap_apply_node_setup(node_id)
        roadmap_set_current(node_id)

        # Node-specific story setup: important when jumping directly into
        # a mid-J20 label (which bypasses the beginning of the day).
        # Determine the target's day and route even for mid-day nodes with
        # no required_variables (e.g. the J20 knife confrontation).
        label = node["label"]
        import re
        match = re.match(r"^_(\\d+)_", label)
        if match:
            target_day = int(match.group(1))
            store.current_day = target_day
            store.day_id = target_day
        route_dg = (
            label.startswith("_20_0_1_1_")
            or label.startswith(tuple("_%d_0_1_1_0" % day for day in range(21, 31)))
        )
        store.mara_dg_body_locked = bool(route_dg)
        return label

    def roadmap_jump_to_node(node_id):
        roadmap_queue_clean_jump(node_id)

    def roadmap_latest_node_id():
        if roadmap_is_day(ROADMAP_NODE_BY_ID.get(store.roadmap_current_node)):
            return store.roadmap_current_node
        discovered = [node["id"] for node in ROADMAP_NODES if roadmap_is_day(node) and roadmap_is_discovered(node)]
        return discovered[-1] if discovered else "day_0"

    def roadmap_focus_initial(node_id, axis, zoom=1.0, nodes=None):
        node = ROADMAP_NODE_BY_ID.get(node_id)
        if not node:
            return 0.0
        map_w, map_h = roadmap_map_size(nodes)
        if axis == "x":
            value = (node["x"] * zoom - 760.0) / max(1.0, map_w * zoom - 1180.0)
        else:
            value = (node["y"] * zoom - 360.0) / max(1.0, map_h * zoom - 620.0)
        return min(1.0, max(0.0, value))

    def roadmap_selected_or_latest(selected_id):
        if roadmap_is_timeline_node(ROADMAP_NODE_BY_ID.get(selected_id)):
            return selected_id
        return roadmap_latest_node_id()

transform roadmap_scan_sweep:
    alpha 0.18
    yoffset -1080
    linear 8.0 yoffset 1080
    repeat

transform roadmap_soft_pulse:
    alpha 0.72
    linear 1.6 alpha 1.0
    linear 1.6 alpha 0.72
    repeat

label roadmap_perform_teleport:
    $ quick_menu = True
    $ quick_menu_open = False
    $ _roadmap_target = roadmap_target_node_id
    if _roadmap_target:
        $ roadmap_target_node_id = None
        $ roadmap_queue_clean_jump(_roadmap_target)
    return

# After full_restart Ren'Py normally shows the main menu. For a queued
# roadmap transfer we press the normal Start action automatically, so that
# Ren'Py creates a fresh game context before restoring the destination.
label before_main_menu:
    if getattr(persistent, "kd_roadmap_transfer", None):
        $ renpy.run(Start())
    return

################################################################################
## Écran principal
################################################################################

screen roadmap_menu(focus_node_id=None, initial_zoom=None):
    tag menu
    modal True
    zorder 220

    default selected_node_id = roadmap_selected_or_latest(roadmap_selected_node)
    default map_zoom = initial_zoom if initial_zoom is not None else 0.78

    $ visible_nodes = [node for node in ROADMAP_NODES if roadmap_is_timeline_node(node) and roadmap_should_show(node)]
    $ map_w, map_h = roadmap_map_size(visible_nodes)
    $ fit_zoom = roadmap_fit_zoom(visible_nodes)
    $ z = max(fit_zoom, min(1.40, map_zoom))
    $ canvas_w = max(1280, int(map_w * z))
    $ canvas_h = max(800, int(map_h * z))
    $ map_offset_x = max(0, int((canvas_w - map_w * z) / 2))
    $ map_offset_y = max(0, int((canvas_h - map_h * z) / 2))
    $ node_w = max(44, int(310 * z))
    $ node_h = max(24, int(118 * z))
    $ compact_nodes = z < 0.45
    $ visible_node_ids = set([node["id"] for node in visible_nodes])
    $ selected_node = roadmap_node(selected_node_id) if selected_node_id in visible_node_ids else None
    $ focus_id = focus_node_id or (selected_node_id if selected_node_id in visible_node_ids else roadmap_latest_node_id())

    add "gui/roadmap/backgrounds/roadmap_bg_hologram.png"
    add Solid("#02071199")
    add "gui/roadmap/backgrounds/roadmap_overlay_scan.png"
    add "gui/roadmap/backgrounds/roadmap_overlay_glitch.png" at roadmap_scan_sweep

    key "game_menu" action NullAction()
    key "K_ESCAPE" action NullAction()
    key "mousedown_4" action SetScreenVariable("map_zoom", min(1.40, z + 0.08))
    key "mousedown_5" action SetScreenVariable("map_zoom", max(fit_zoom, z - 0.08))

    frame:
        xpos 28
        ypos 28
        xsize 1864
        ysize 1024
        padding (22, 18)
        background Frame("gui/roadmap/roadmap_panel_main.png", 18, 18)

        fixed:
            text "ARCHIVES DU CONCLAVE":
                xpos 26
                ypos 10
                style "roadmap_title_text"
            text "Chronologie surveillée // Kami.observe(branches=true)":
                xpos 30
                ypos 70
                style "roadmap_meta_text"

            hbox:
                xpos 28
                ypos 114
                spacing 12
                add Solid("#55d7a0") xsize 34 ysize 3 yalign 0.5
                text "JOURNÉES // CHRONOLOGIE PRINCIPALE" style "roadmap_meta_text"

            hbox:
                xpos 1168
                ypos 102
                spacing 8
                textbutton "−":
                    style "roadmap_small_button"
                    xsize 58
                    sensitive z > fit_zoom
                    action SetScreenVariable("map_zoom", max(fit_zoom, z - 0.10))
                textbutton "[int(z * 100)] %":
                    style "roadmap_small_button"
                    xsize 78
                    action SetScreenVariable("map_zoom", fit_zoom)
                textbutton "+":
                    style "roadmap_small_button"
                    xsize 58
                    sensitive z < 1.40
                    action SetScreenVariable("map_zoom", min(1.40, z + 0.10))
                textbutton "Vue globale":
                    style "roadmap_small_button"
                    xsize 154
                    action SetScreenVariable("map_zoom", fit_zoom)
                textbutton "Centrer":
                    style "roadmap_small_button"
                    xsize 124
                    action ShowMenu("roadmap_menu", focus_node_id=roadmap_latest_node_id(), initial_zoom=z)
                textbutton "Retour":
                    style "roadmap_small_button"
                    xsize 112
                    action Return()

            hbox:
                xpos 32
                ypos 168
                spacing 20

                frame:
                    xsize 1280
                    ysize 800
                    background Solid("#020812aa")
                    padding (0, 0)

                    viewport:
                        xsize 1280
                        ysize 800
                        draggable True
                        scrollbars "both"
                        pagekeys True
                        xinitial roadmap_focus_initial(focus_id, "x", z, visible_nodes)
                        yinitial roadmap_focus_initial(focus_id, "y", z, visible_nodes)

                        fixed:
                            xsize canvas_w
                            ysize canvas_h

                            for node in visible_nodes:
                                for req in roadmap_timeline_predecessors(node):
                                    if req in visible_node_ids:
                                        $ source = ROADMAP_NODE_BY_ID[req]
                                        $ sx = map_offset_x + int(source["x"] * z) + node_w
                                        $ sy = map_offset_y + int(source["y"] * z) + int(node_h / 2)
                                        $ tx = map_offset_x + int(node["x"] * z)
                                        $ ty = map_offset_y + int(node["y"] * z) + int(node_h / 2)
                                        $ mx = int((sx + tx) / 2)
                                        $ edge_state = roadmap_edge_status(req, node["id"])
                                        $ edge_color = {"active": "#5cd3ffcc", "locked": "#39495699", "alt": "#b27bffcc", "vote": "#d6b15fcc", "ending": "#ff5f7acc"}.get(edge_state, "#5cd3ffcc")
                                        $ edge_glow = {"active": "#5cd3ff22", "locked": "#39495618", "alt": "#b27bff22", "vote": "#d6b15f22", "ending": "#ff5f7a22"}.get(edge_state, "#5cd3ff22")
                                        add Solid(edge_glow) xpos min(sx, mx) ypos (sy - 3) xsize max(6, abs(mx - sx)) ysize 8
                                        add Solid(edge_glow) xpos (mx - 3) ypos min(sy, ty) xsize 8 ysize max(6, abs(ty - sy))
                                        add Solid(edge_glow) xpos min(mx, tx) ypos (ty - 3) xsize max(6, abs(tx - mx)) ysize 8
                                        add Solid(edge_color) xpos min(sx, mx) ypos sy xsize max(2, abs(mx - sx)) ysize 2
                                        add Solid(edge_color) xpos mx ypos min(sy, ty) xsize 2 ysize max(2, abs(ty - sy))
                                        add Solid(edge_color) xpos min(mx, tx) ypos ty xsize max(2, abs(tx - mx)) ysize 2
                                        add Solid(edge_color) xpos (tx - 3) ypos (ty - 3) xsize 8 ysize 8

                            for node in visible_nodes:
                                $ nx = map_offset_x + int(node["x"] * z)
                                $ ny = map_offset_y + int(node["y"] * z)
                                button:
                                    xpos nx
                                    ypos ny
                                    xsize node_w
                                    ysize node_h
                                    background Frame(roadmap_node_bg(node), 12, 12)
                                    hover_background Frame(roadmap_node_bg(node, True), 12, 12)
                                    action [
                                        SetScreenVariable("selected_node_id", node["id"]),
                                        SetVariable("roadmap_selected_node", node["id"]),
                                    ]

                                    fixed:
                                        if roadmap_is_ending(node):
                                            add Solid("#ff5f7acc") xpos 0 ypos 0 xsize node_w ysize max(3, int(5 * z))
                                            add Solid("#ff5f7acc") xpos 0 ypos (node_h - max(3, int(5 * z))) xsize node_w ysize max(3, int(5 * z))
                                        if compact_nodes:
                                            text kd_tr(node.get("short", node["id"])):
                                                xalign 0.5
                                                yalign 0.5
                                                style "roadmap_node_code_text"
                                                size 12
                                        else:
                                            add Transform(roadmap_icon(node), size=(int(38 * z), int(38 * z))) xpos int(16 * z) ypos int(32 * z)
                                            text kd_tr(node.get("short", node["id"])):
                                                xpos int(64 * z)
                                                ypos int(18 * z)
                                                xsize int(218 * z)
                                                style "roadmap_node_code_text"
                                            text roadmap_display_title(node):
                                                xpos int(64 * z)
                                                ypos int(49 * z)
                                                xsize int(218 * z)
                                                style "roadmap_node_title_text"
                                                size max(15, int(20 * z))
                                            if roadmap_can_teleport(node):
                                                add Transform("gui/roadmap/icons/roadmap_icon_teleport.png", size=(int(24 * z), int(24 * z))) xpos int(272 * z) ypos int(14 * z)

                use roadmap_node_details(selected_node)

            hbox:
                xpos 38
                ypos 980
                spacing 22
                use roadmap_legend_item("#55d7a0", "Terminé")
                use roadmap_legend_item("#5cd3ff", "En cours / disponible")
                use roadmap_legend_item("#b27bff", "Embranchement")
                use roadmap_legend_item("#ff5f7a", "Fin")
                use roadmap_legend_item("#677989", "Verrouillé")
                text "Molette : zoom  •  Glisser : déplacer  •  Vue globale : tout afficher" style "roadmap_legend_text"

screen roadmap_legend_item(color_value, label_value):
    hbox:
        spacing 8
        add Solid(color_value) xsize 28 ysize 3 yalign 0.5
        text kd_tr(label_value) style "roadmap_legend_text"

screen roadmap_node_details(node):
    frame:
        xsize 500
        ysize 800
        background Frame("gui/roadmap/roadmap_panel_side.png", 18, 18)
        padding (28, 26)

        if node:
            vbox:
                spacing 14
                text roadmap_display_title(node) style "roadmap_details_title_text"
                text roadmap_status_label(node) style "roadmap_status_text"
                add Solid("#3a9fca66") xsize 444 ysize 1

                text roadmap_display_summary(node) style "roadmap_body_text"

                null height 8

                if roadmap_can_teleport(node):
                    textbutton "Rejoindre cette séquence":
                        style "roadmap_action_button"
                        action [
                            Hide("roadmap_menu"),
                            Function(roadmap_jump_to_node, node["id"]),
                        ]
                else:
                    textbutton "Accès refusé par Kami":
                        style "roadmap_action_button"
                        sensitive False

                textbutton "Fermer la sélection":
                    style "roadmap_action_button"
                    action [
                        SetVariable("roadmap_selected_node", None),
                    ]
        else:
            vbox:
                spacing 18
                text "Aucune séquence sélectionnée" style "roadmap_details_title_text"
                text "Sélectionnez une journée ou une fin pour consulter ses archives et rejoindre cette séquence." style "roadmap_body_text"

################################################################################
## Styles
################################################################################

style roadmap_title_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 46
    color "#dff2ff"
    outlines [(1, "#071018", 0, 0)]

style roadmap_meta_text:
    font "fonts/Barlow-Light.ttf"
    size 20
    color "#5cd3ff"

style roadmap_filter_button is button:
    background Solid("#071723aa")
    hover_background Solid("#0c2b3dcc")
    selected_background Solid("#123d55dd")
    padding (18, 8, 18, 8)

style roadmap_filter_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#75a9bd"
    hover_color "#dff2ff"
    selected_color "#5cd3ff"

style roadmap_small_button is button:
    background Frame("gui/roadmap/buttons/roadmap_button_idle.png", 12, 12)
    hover_background Frame("gui/roadmap/buttons/roadmap_button_hover.png", 12, 12)
    insensitive_background Frame("gui/roadmap/buttons/roadmap_button_disabled.png", 12, 12)
    xsize 170
    ysize 46
    padding (14, 5, 14, 5)

style roadmap_small_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 20
    color "#8ab8d0"
    hover_color "#dff2ff"
    insensitive_color "#4a5a64"
    xalign 0.5

style roadmap_node_code_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 18
    color "#5cd3ff"

style roadmap_node_title_text:
    font "fonts/Barlow-Light.ttf"
    color "#d8eef6"
    line_spacing 0

style roadmap_details_title_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 34
    color "#dff2ff"

style roadmap_status_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 24
    color "#5cd3ff"

style roadmap_section_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#d6b15f"

style roadmap_body_text:
    font "fonts/Barlow-Light.ttf"
    size 22
    color "#9db8c6"
    line_spacing 3

style roadmap_code_text:
    font "DejaVuSansMono.ttf"
    size 18
    color "#8eeaff"

style roadmap_action_button is button:
    background Frame("gui/roadmap/buttons/roadmap_button_idle.png", 12, 12)
    hover_background Frame("gui/roadmap/buttons/roadmap_button_hover.png", 12, 12)
    insensitive_background Frame("gui/roadmap/buttons/roadmap_button_disabled.png", 12, 12)
    xfill True
    ysize 54
    padding (18, 8, 18, 8)

style roadmap_action_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 23
    color "#8ab8d0"
    hover_color "#dff2ff"
    insensitive_color "#51616b"
    xalign 0.5

style roadmap_list_button is button:
    background Solid("#081822aa")
    hover_background Solid("#10334acc")
    selected_background Solid("#164865dd")
    xfill True
    ysize 48
    padding (14, 6, 14, 6)

style roadmap_list_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#80a9bb"
    hover_color "#dff2ff"
    selected_color "#5cd3ff"

style roadmap_scene_button is button:
    background Solid("#06131daa")
    hover_background Solid("#0e2d3fcc")
    selected_background Solid("#173c52dd")
    xfill True
    yminimum 50
    padding (14, 8, 14, 8)

style roadmap_scene_button_text is button_text:
    font "fonts/Barlow-Light.ttf"
    size 22
    color "#8caec0"
    hover_color "#dff2ff"
    selected_color "#5cd3ff"

style roadmap_legend_text:
    font "fonts/Barlow-Light.ttf"
    size 18
    color "#7f9dad"
