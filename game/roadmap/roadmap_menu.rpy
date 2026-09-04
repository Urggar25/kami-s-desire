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
            "title": "Jour 7_1_0 — La passagère",
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
            "title": "Jour 7_1_0_0 — Passagère clandestine",
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
            "title": "Jour 7_1_0_1 — Sursis déclaré",
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
            "title": "Jour 8_1_0_0 — Le réveil d'Anya",
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
            "title": "Jour 9_1_0_0 — Ce que Ryn savait",
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
            "title": "Jour 15 - Images impossibles",
            "short": "J15",
            "label": "_15_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 7680,
            "y": 530,
            "summary": "Noam et Kael exploitent les archives video et decouvrent des preuves impossibles autour des objets disparus.",
            "choice": "Regarder les cameras malgre le risque de detruire la confiance restante.",
            "consequence": "La journee se termine sur un blackout brutal apres une confrontation avec Kael.",
            "requires": ["day_14_0_1_1_0"],
            "teleportable": True,
        },
        {
            "id": "day_16_0_1_1_0",
            "title": "Jour 16 - Memoire modifiee",
            "short": "J16",
            "label": "_16_0_1_1_0_REVEIL_CHAMBRE",
            "category": "day",
            "kind": "day",
            "x": 8060,
            "y": 530,
            "summary": "Noam se reveille avec un blackout total. La tension avec Kael l'entraine jusqu'aux archives, ou Sael revele une mention medicale impossible.",
            "choice": "Confronter Kael ou chercher une preuve qui ne depend pas des souvenirs.",
            "consequence": "La mention Memoire modifiee frappe tous les representants et remet en doute la realite vecue.",
            "requires": ["day_15_0_1_1_0"],
            "teleportable": True,
        },
        {
            "id": "day_17_0_1_1_0",
            "title": "Jour 17 - Les murs repondent",
            "short": "J17",
            "label": "_17_0_1_1_0_ANNONCE_KAMI",
            "category": "day", "kind": "day", "x": 8440, "y": 530,
            "summary": "Kami annule les prochains votes apres la lecture des archives. Dans sa chambre, Noam entend des grattements qui lui repondent.",
            "choice": "Croire une trace physique plutot que les souvenirs alteres.",
            "consequence": "Noam decide d'ouvrir la grille d'aeration malgre l'interdiction de Kami.",
            "requires": ["day_16_0_1_1_0"], "teleportable": True,
        },
        {
            "id": "day_18_0_1_1_0",
            "title": "Jour 18 - La grille",
            "short": "J18",
            "label": "_18_0_1_1_0_REVEIL_DECISION",
            "category": "day", "kind": "day", "x": 8820, "y": 530,
            "summary": "Noam demande l'aide de Mara pour demonter l'aeration. Ils trouvent des fibres, une semelle et les traces d'un passage humain.",
            "choice": "Partager la preuve avec Mara et preparer une exploration du conduit.",
            "consequence": "Kami evoque le Clone de Mara, un souvenir qu'elle n'avait confie a personne.",
            "requires": ["day_17_0_1_1_0"], "teleportable": True,
        },
        {
            "id": "day_19_0_1_1_0",
            "title": "Jour 19 - Dans les murs",
            "short": "J19",
            "label": "_19_0_1_1_0_BARRICADE",
            "category": "day", "kind": "day", "x": 9200, "y": 530,
            "summary": "Noam barricade sa chambre puis traverse le reseau d'aeration avec Mara. Une silhouette portant sa voix les attend dans le noir.",
            "choice": "Poursuivre la voix ou conserver un chemin de retour.",
            "consequence": "Mara promet de ravitailler Noam, convaincue que quelqu'un peut prendre sa place.",
            "requires": ["day_18_0_1_1_0"], "teleportable": True,
        },
        {
            "id": "day_20_0_1_1_0",
            "title": "Jour 20 - La copie",
            "short": "J20",
            "label": "_20_0_1_1_0_FAIM",
            "category": "day", "kind": "day", "x": 9580, "y": 530,
            "summary": "Affame, Noam retrouve une Mara qui ne se souvient plus du conduit. Avec Tomas, ils y decouvrent une copie de la photo de la soeur de Kael.",
            "choice": "Retourner dans les conduits malgre l'amnesie de Mara.",
            "consequence": "La copie porte la mention Chambre Noam tandis qu'une seconde voix de Noam parle depuis les murs.",
            "requires": ["day_19_0_1_1_0"], "teleportable": True,
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
        if status == "current":
            return "current"
        if status == "done":
            return "done"
        if status in ("locked", "unknown"):
            return status
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
        if target.get("kind") == "route":
            return "alt"
        if target.get("kind") == "vote":
            return "vote"
        return "active"

    def roadmap_is_day(node):
        return bool(node and (node.get("kind") == "day" or node.get("category") == "day"))

    def roadmap_day_predecessors(node):
        """Return the nearest day nodes behind a day, skipping technical nodes."""
        result = []
        visited = set()

        def visit(node_id):
            if node_id in visited:
                return
            visited.add(node_id)
            candidate = ROADMAP_NODE_BY_ID.get(node_id)
            if not candidate:
                return
            if roadmap_is_day(candidate):
                if candidate["id"] not in result:
                    result.append(candidate["id"])
                return
            for requirement in candidate.get("requires", []):
                visit(requirement)

        for requirement in node.get("requires", []):
            visit(requirement)
        return result

    def roadmap_map_size(nodes=None):
        nodes = list(nodes) if nodes is not None else [node for node in ROADMAP_NODES if roadmap_is_day(node)]
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

    def roadmap_jump_to_node(node_id):
        node = ROADMAP_NODE_BY_ID.get(node_id)
        if not node:
            renpy.notify("Roadmap: noeud inconnu - %s" % node_id)
            return
        label = node.get("label")
        if not label or not renpy.has_label(label):
            renpy.notify("Roadmap: label introuvable - %s" % label)
            return

        store.quick_menu = True
        store.quick_menu_open = False
        roadmap_apply_node_setup(node_id)
        if node_id not in store.roadmap_unlocked_nodes:
            store.roadmap_unlocked_nodes.append(node_id)
        if node_id not in store.roadmap_discovered_nodes:
            store.roadmap_discovered_nodes.append(node_id)
        store.roadmap_current_node = node_id
        store.roadmap_target_node_id = None
        store.roadmap_target_label = None
        renpy.jump_out_of_context(label)

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
        if roadmap_is_day(ROADMAP_NODE_BY_ID.get(selected_id)):
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
        $ roadmap_apply_node_setup(_roadmap_target)
        $ roadmap_set_current(_roadmap_target)
        $ roadmap_target_label = roadmap_node(_roadmap_target).get("label")
        $ roadmap_target_node_id = None
        if roadmap_target_label:
            $ _jump_label = roadmap_target_label
            $ roadmap_target_label = None
            jump expression _jump_label
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

    $ visible_nodes = [node for node in ROADMAP_NODES if roadmap_is_day(node) and roadmap_should_show(node)]
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
                                for req in roadmap_day_predecessors(node):
                                    if req in visible_node_ids:
                                        $ source = ROADMAP_NODE_BY_ID[req]
                                        $ sx = map_offset_x + int(source["x"] * z) + node_w
                                        $ sy = map_offset_y + int(source["y"] * z) + int(node_h / 2)
                                        $ tx = map_offset_x + int(node["x"] * z)
                                        $ ty = map_offset_y + int(node["y"] * z) + int(node_h / 2)
                                        $ mx = int((sx + tx) / 2)
                                        $ edge_state = roadmap_edge_status(req, node["id"])
                                        $ edge_color = {"active": "#5cd3ffcc", "locked": "#39495699", "alt": "#b27bffcc", "vote": "#d6b15fcc"}.get(edge_state, "#5cd3ffcc")
                                        $ edge_glow = {"active": "#5cd3ff22", "locked": "#39495618", "alt": "#b27bff22", "vote": "#d6b15f22"}.get(edge_state, "#5cd3ff22")
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
                text "Aucune journée sélectionnée" style "roadmap_details_title_text"
                text "Sélectionnez une journée pour consulter ses archives et rejoindre cette séquence." style "roadmap_body_text"

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
