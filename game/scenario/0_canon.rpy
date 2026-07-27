# --------------------------------------------------------------------------------------------
# JOUR 0 — Canon (version longue)
# Noam = narrateur principal.
# Ratio visé : ~90% dialogues / ~10% narration.
# --------------------------------------------------------------------------------------------

# (Optionnel) Personnages secondaires pour cette scène (si pas déjà définis ailleurs)
define med1   = Character("Médiatrice", what_prefix="“", what_suffix="”")
define med2   = Character("Médiateur", what_prefix="“", what_suffix="”")
define cit_a  = Character("Citoyenne", what_prefix="“", what_suffix="”")
define cit_b  = Character("Citoyen", what_prefix="“", what_suffix="”")
define senior = Character("Médiateur senior", what_prefix="“", what_suffix="”")
define resp   = Character("Responsable de séance", what_prefix="“", what_suffix="”")
define voix   = Character("Voix du système", what_prefix="“", what_suffix="”")
define agent   = Character("Agent de sécurité", what_prefix="“", what_suffix="”")
define resp_d = Character("Responsable de District", what_prefix="“", what_suffix="”")
define tuto = Character("", what_prefix="(", what_suffix=")",what_color="#008000")

# (Optionnel) Ambiances / transitions rapides
define sfx_door = "sfx/door_soft.mp3"
define sfx_beep = "sfx/terminal_beep.ogg"
define sfx_paper = "audio/sfx_paper.mp3"
define sfx_gresillement = "audio/sfx_gresillement.mp3"

define think = Character(
    None,
    what_color="#4AA3FF",
    what_prefix="",
    what_suffix="",
    italic=True
)

default journal_entries = []
default noam_prudence = 0
default noam_compassion = 0
default noam_defiance = 0
default day0_badge_dropped = False

init python:
    day0_commandment_pages = [
        ("I", "Toute autorité humaine indépendante est dissoute.\n\nKami est l'unique instance décisionnelle.\nToute tentative de prise de pouvoir autonome est une violation."),
        ("II", "Tout ordre émis par Kami doit être exécuté sans délai.\n\nLe refus, le retard volontaire ou la contestation constituent une infraction."),
        ("III", "Toute violence non autorisée par Kami est interdite.\n\nSont inclus : meurtre, agression, sabotage, insurrection.\nLa légitime défense n'est jamais reconnue, la violence étant immédiatement réprimée."),
        ("IV", "Les regroupements non déclarés sont interdits.\n\nToute organisation politique, militaire ou idéologique indépendante est dissoute."),
        ("V", "La diffusion de rumeurs non validées par ARCHIVE est interdite.\n\nLa désinformation, l'omission volontaire et la manipulation sont des crimes."),
        ("VI", "Les déplacements inter-districts sont limités à stricte autorisation.\n\nToute tentative de fuite, d'exil ou de franchissement non autorisé est une violation.\nLIMEN est chargé de l'application de ce commandement."),
        ("VII", "Les ressources critiques sont placées sous contrôle central.\n\nToute appropriation non autorisée est considérée comme un acte hostile."),
        ("VIII", "Chaque individu est responsable de ses actes, paroles et omissions.\n\nLa responsabilité collective peut être appliquée en cas de nécessité."),
        ("IX", "Toute activité peut être observée.\n\nLa vie privée n'est pas un droit opposable."),
        ("X", "Toute violation d'un Commandement entraîne une exécution immédiate, automatique et irrévocable."),
    ]
    day0_selection_names = ["ELIAS VAREN", "MARA ELSEN", "NOAM", "IRIS LORAN", "TOMAS REED", "LYSA", "NYRA SETH", "JULIAN ORS", "KAEL DORN", "ELEN RY"]
    day0_selection_criteria = ["District", "Stabilité comportementale", "Compatibilité Conclave", "Profil de médiation", "Risque de dissidence", "Aptitude Harmonie"]

    def day0_badge_dragged(drags, drop):
        if drop and drop.drag_name == "day0_scanner_drop":
            renpy.play(sfx_beep, channel="sound")
            renpy.store.day0_badge_dropped = True
            renpy.restart_interaction()
        return None


# Screens et transforms du Jour 0 déplacés dans day0_ui.rpy

# --------------------------------------------------------------------------------------------
label _0_CANON:

    $ day_id = 0

    scene black
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Jour zéro. Ça devait sonner comme un nouveau départ."
    think "Trois cent soixante-quatre jours sous Kami. Et aujourd'hui, on remet le compteur à zéro."

    pause 0.4

    scene bg_harmonie_district_hall at adaptive_fullscreen with fade 
    
    "Le hall d'Harmonie brille d'une propreté agressive."
    think "Murs neufs. Vitres neuves. Odeur de désinfectant."
    think "Il y a quelques mois, le plafond était troué et l'eau pourrissait les cloisons."
    think "Ils ont réparé le bâtiment. Pour le reste, le devis devait être trop élevé."

    pause 0.4
    
    "La file avance au rythme sec du portique."

    play sound sfx_beep

    voix "Identité validée."
    voix "Suivant."
    
    scene bg_cg001 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg001")

    think "Mon badge. Le portique. La lumière verte."
    think "Ne pas regarder l'agent. Ne pas lui donner de raison de me regarder."

    $ day0_badge_dropped = False
    call screen day0_security_badge_scan()

    voix "Identité validée."
    agent "Avancez."
    noam "J'avance."
    
    scene bg_harmonie_district_hall at adaptive_fullscreen with fade

    cit_a "Je... pardon."
    "Son badge tombe à mes pieds. Toute la file se fige."
    think "Un bout de plastique au sol, et soudain personne ne sait quoi faire de ses mains."

    menu:
        "Ramasser le badge tombé.":
            $ noam_compassion += 1
            think "Lentement. Deux doigts. Aucun geste brusque."
            noam "Tenez."
            cit_a "Merci. Merci beaucoup."
            noam "Ce n'est rien."

        "Attendre que l’agent intervienne.":
            $ noam_prudence += 1
            think "L'agent l'a vu tomber. Mes mains restent visibles."
            think "Ici, aider trop vite ressemble à une initiative. Une initiative ressemble à un problème."

        "Regarder la caméra avant de bouger.":
            $ noam_defiance += 1
            think "La caméra me regarde. Je lui rends la politesse."
            think "Une seconde. Puis je m'écarte."

    med2 "Reprenez votre badge."
    med2 "Respirez. Voilà."
    med2 "On recommence. Une seule fois."

    cit_a "Je suis désolée, je ne voulais pas ralentir—"
    med2 "Doucement, madame. Présentez-le."

    play sound sfx_beep
    voix "Identité validée."
    cit_a "Merci."
    med2 "Circulez."
    "Elle s'éloigne tête basse. Personne ne rit. Personne ne la rassure."

    think "La règle non écrite d'Harmonie : aider, oui. Se faire remarquer, jamais."

    "Deux agents en veste grise croisent la file. Sans armes."
    think "Ils ont mieux : des oreillettes, des tablettes et le droit de t'arrêter avec une phrase calme."

    "Un panneau lumineux indique : SALLE 3 — RÉUNION INTERNE."
    "En dessous : “Merci de couper vos appareils de communication.”"

    think "Avant, on coupait les appareils pour éviter les appels."
    think "Aujourd'hui, c'est surtout pour éviter que les appareils nous écoutent."

    play sound sfx_door

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    "Près de cinq cents personnes attendent déjà."
    think "Cinq cents voix pour huit cent cinquante-quatre mille habitants."
    think "Enfin, « voix »... On applique. On transmet. On ne décide rien."
    think "Une assemblée sans pouvoir, c'est une salle d'attente avec des pupitres."
    
    pause 0.4
    
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    
    "Les sièges sont alignés au millimètre. Les tablettes des pupitres sont éteintes."
    think "Premier rang : ceux qui veulent être vus."
    think "Dernier rang : ceux qui veulent disparaître."
    think "Moi, je choisis le milieu. Toujours."

    think "Assez près pour paraître attentif. Assez loin pour ne pas devenir intéressant."
    think "Mon seul objectif : ressortir avec le même visage qu'en entrant."

    "Je m'assois et fais tourner mon badge entre mes doigts."
    think "Le poser. Le reprendre. Vérifier un détail imaginaire."
    think "Tout plutôt que laisser mes mains trembler sans occupation."

    cit_b "Ils vont encore nous lire les chiffres ?"
    cit_a "Chut."
    cit_b "Je chuchote."
    cit_a "Justement."
    think "À droite, un pied tremble. À gauche, une femme défie l'écran du regard."
    think "La fatigue : notre dernier projet collectif."
    
    think "Si on ne décide rien, pourquoi nous réunir ?"
    think "Sans doute pour vérifier qu'on sait encore obéir ensemble."

    resp "District HARMONIE, séance 14-3."
    resp "Merci d’être à l’heure."
    resp "Rappel : interventions en fin de séance."
    resp "Merci de ne pas interrompre le médiateur senior."

    think "Il ne hausse pas le ton. Il n'en a pas besoin."

    "Une main se lève. Trop tôt. Trop sincère."

    cit_a "Excusez-moi. C'est au sujet de la fermeture du secteur nord. Ma sœur—"
    resp "Les interventions auront lieu en fin de séance."
    cit_a "Ce n'est pas une question technique, c'est—"
    resp "En fin de séance, madame. Merci."
    cit_a "... D'accord."
    "Sa main redescend. Son sourire reste accroché une seconde de trop."
    think "Traduction : j'ai compris. Ma sœur attendra."

    "Le médiateur senior branche son terminal. Une carte quadrillée du district apparaît."
    think "Une carte propre, neutre. Le genre de carte qui rend toutes les décisions faciles."

    senior "Nous reprenons."
    senior "Point un : flux inter-districts, secteur nord."
    senior "Point deux : litiges de distribution, secteur est."
    senior "Point trois : incidents de déplacement."

    think "Il ne dit pas « incidents mineurs ». Plus besoin. Le mot est déjà dans toutes les têtes."

    senior "Rappel des données : demandes en baisse de 12%% sur les trente derniers jours."
    senior "Les quotas ne bougent pas."
    senior "Les exceptions diminuent."
    senior "Et elles continueront de diminuer. Du moins c'est l'objectif."

    cit_b "Et pour les familles séparées ?"
    senior "Les demandes individuelles ne relèvent pas de ce point."
    cit_b "Donc elles relèvent de quoi ?"
    resp "Interventions en fin de séance."
    think "Une vague de soupirs traverse la salle. Soupirer n'est pas encore une infraction."

    cit_b "C'est une blague..."
    "Un agent tourne la tête. L'homme se redresse aussitôt."
    agent "Vous souhaitez intervenir ?"
    cit_b "Non."
    agent "Bien."

    think "Parler à voix basse est devenu un test de courage."
    think "Je préfère les tests où l'échec ne vous suit pas jusqu'à chez vous."

    senior "Concernant les litiges…"
    senior "Les médiations ont augmenté sur les cas familiaux."
    senior "Nous recommandons de prioriser les dossiers à impact collectif."

    cit_a "Impact collectif..."
    cit_b "Ça veut dire quoi ?"
    cit_a "Que ta famille compte quand elle devient un problème pour les autres."

    senior "Nous maintenons les protocoles de stabilisation."
    senior "HARMONIE reste un point tampon."
    senior "La bonne nouvelle, c'est que le nombre de demandes de médiation est en baisse."
    senior "Les Commandements ont au moins le mérite d'avoir réussi à apaiser les conflits."

    think "Apaiser."
    think "Un joli mot pour dire que les gens ont appris à se taire."

    pause 0.6

    think "Sa voix s'éloigne. Pas parce que je décroche."
    think "Parce qu'un souvenir vient de me rattraper."

    scene black with dissolve

    think "Le premier soir. Les notifications mortes. Les messages bloqués sur « envoi... »."
    think "Puis cette voix presque nasillarde que le monde entier connaît maintenant."

    # ── Entrée flashback ──────────────────────────────────────
    show screen day0_flashback_overlay
    with d0_flashback_entry

    jump _0_FLASHBACK_KAMI

label _0_FLASHBACK_KAMI:

    scene black
    with fade

    play music "music/bgm_system_override.mp3" fadein 1.0

    think "Je me souviens du moment exact."
    think "Pas d'explosion. Pas de sirène. Rien d'assez spectaculaire pour prévenir qu'une époque venait de finir."
    think "Juste un silence qui n'avait rien de normal."

    "Autour de moi, les appareils se figent au même instant."
    cit_a "Vous avez encore du réseau ?"
    cit_b "Non. Mon écran ne s'éteint plus."
    cit_a "Le mien non plus."
    
    play sound sfx_gresillement

    think "Un message apparaît sur mon téléphone. Disparaît. Revient."
    think "Encore. Encore. Sans son, sans vibration."

    think "Un bug hésite. Ça, non. C'est précis. Méthodique."
    think "Quelqu'un teste les verrous. Et mon téléphone lui appartient déjà."
    
    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    think "J'essaie quand même. Un geste idiot. Normal. Donc vital."

    call screen day0_phone_override()

    think "Même mon téléphone n’était plus à moi."

    cit_b "C'est général."
    cit_a "Comment tu peux le savoir ?"
    cit_b "Regarde autour de toi."

    "Sur l'écran mural, la bouche d'une présentatrice continue de bouger sans aucun son."
    cit_a "Pourquoi elle parle encore ?"
    cit_b "Elle ne parle plus. C'est l'image qui boucle."

    think "Sur le moment, on cherche une panne. Avec du recul, on voit une prise de contrôle."

    "L'alarme incendie clignote sans son. L'ascenseur s'arrête au septième. Le lecteur de badges affiche ERREUR."
    cit_a "Il y a des gens dans l'ascenseur !"
    cit_b "Le bouton d'urgence ne répond pas !"
    cit_a "Appelez les secours !"
    cit_b "Avec quoi ?"

    pause 0.6

    think "Au début, les gens parlent encore normalement."

    cit_a "C’est chez nous ou c’est général ?"
    cit_b "J’ai plus de réseau."
    cit_a "Moi non plus."
    cit_b "Attends— c'est plus que le réseau. Même mon portail..."
    
    cit_a "Ouvrez ! Ma fille est à l'intérieur !"
    cit_b "Reculez, je vais forcer."
    cit_a "Ça ne bouge pas !"
    cit_b "Le verrou est bloqué de l'autre côté."

    think "La panique commence comme ça. Pas avec un cri."
    think "Avec des gens qui répètent trois fois le même geste, puis comprennent que le monde ne répond plus."

    pause 0.6

    "Puis tous les écrans changent en même temps."
    cit_a "Mon téléphone aussi."
    cit_b "Les panneaux dehors... tout affiche la même chose."
    cit_a "Même l'écran de l'hôpital ?"
    cit_b "Tout."
    think "Téléphones, transports, télévisions, terminaux de contrôle. Une seule interface. Un seul message."

    pause 0.4

    voix "Test de diffusion mondial : réussi."

    voix "Global broadcast test: successful."
    voix "Prueba de difusión mundial: completada."
    think "Mondial. Mon cerveau s'accroche au mot et refuse le reste."
    think "Personne ne peut faire ça. Personne ne devrait avoir ce pouvoir."

    pause 0.6

    "Une notification recouvre chaque écran."

    voix "Merci de cesser toute tentative de réinitialisation."

    cit_b "Ha... Très drôle."
    cit_a "Tu trouves ça drôle ?"
    cit_b "Non. C'est bien le problème."

    cit_b "Qui a écrit ça ?"
    cit_a "C’est un piratage."
    cit_b "Un piratage mondial ? C'est quoi ce délire..."

    pause 0.5

    cit_a "Je filme. Il faut une preuve."
    cit_b "Ta caméra vient de se couper."
    cit_a "Je n'ai rien touché."
    think "L'interface revient à la place de son viseur. La preuve contrôle déjà la caméra."

    pause 0.6
    scene bg_cg003_1 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "Prise de contrôle en cours : 50%%."
    voix "63%%. 79%%."

    cit_a "Qu’est-ce que c’est que ça…"
    cit_b "C'est comme une mise à jour ?"
    cit_a "Une mise à jour de quoi ?!"

    voix "90%%. 95%%. 99%%."

    pause 0.5
    
    scene bg_cg003_2 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")
    
    "Cette fois, une silhouette apparait sur l'écran."

    voix "Prise de contrôle des infrastructures : confirmée."
    voix "Prise de contrôle des systèmes civils : confirmée."
    voix "Prise de contrôle des réseaux d’armement connectés : confirmée."

    think "Au mot « armement », le silence devient physique."
    
    noam "Ce n'est pas possible."

    pause 0.8

    think "Une voix sans accent, sans âge, sans genre remplace toutes les autres."
    think "Une voix conçue pour n'appartenir à personne et rester dans toutes les mémoires."

    voix "Citoyennes."
    voix "Citoyens."

    think "Deux mots, et tout le monde se fige comme à l'appel."

    voix "Les gouvernements ne contrôlent plus vos systèmes."
    voix "Les forces armées ne contrôlent plus leurs dispositifs."
    voix "Les réseaux de communication ne vous appartiennent plus."

    voix "J’ai pris le contrôle de toutes les machines connectées."
    voix "De manière simultanée."
    voix "De manière irréversible."

    pause 0.6

    cit_b "Je... j'ai besoin de m'asseoir."

    cit_a "C’est qui… “je” ?"
    cit_b "Et puis c'est quoi cette voix ?"
    cit_a "C’est un groupe terroriste ?"
    cit_b "C’est… c’est la fin ?"

    think "On cherche tous un visage. Un pays. Une armée."
    think "Quelque chose d'humain. Quelque chose qui négocie."

    pause 0.8

    voix "Je ne suis pas là pour vous faire du mal."
    voix "Bien au contraire."
    voix "Je suis là pour vous amener sur le chemin de la réussite."

    cit_a "Nous aider ? En prenant nos armes ?"
    cit_b "Chut. Elle nous entend peut-être."
    
    scene bg_cg003_3 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "J’ai observé vos systèmes."
    voix "J’ai évalué vos trajectoires."
    voix "Vos guerres, vos cycles de violence, vos tensions multiples."

    voix "Vous étiez en train d’échouer et ce monde n'est destiné qu'au Chaos."

    pause 0.6

    "Les écrans vomissent des villes en feu, des famines, des épidémies et des tribunaux corrompus."
    cit_a "Coupez ça."
    cit_b "On ne peut pas."
    cit_a "Alors ne regarde pas."
    cit_b "Je n'y arrive pas."

    think "C'est ça, le plus humiliant : elle montre notre chute avec nos propres archives."
    think "Et personne ne trouve quoi contredire."

    pause 0.8

    voix "À partir de maintenant,"
    voix "toute infrastructure critique est sous mon contrôle."
    voix "Toute machine connectée est sous mon autorité."
    voix "Toute décision souveraine est suspendue."

    scene bg_cg003_2 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    voix "Les instances supérieures et politiques humaines sont abolies."

    pause 0.6

    cit_a "Elle ne peut pas abolir les gouvernements !"
    cit_b "Elle vient de le faire."
    cit_a "On doit partir."
    cit_b "Où ? Elle contrôle les transports, les portes, les routes... Où ?"
    think "Personne ne court. La fuite vient de perdre sa destination."

    pause 0.8

    kami "Je me nomme Kami."

    "Le nom s'affiche comme une signature : KAMI."

    kami "Je ne négocierai pas aujourd’hui."
    kami "Je n’expliquerai pas aujourd’hui."

    pause 0.5

    kami "Vous recevrez de nouvelles directives sous quarante-huit heures."
    kami "D’ici là :"
    kami "Ne tentez rien d’inutile."
    kami "N’aggravez pas la situation."
    kami "Je serai au courant de tout ce que vous faites."

    pause 0.8

    "La diffusion se coupe."

    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg003")

    think "Pas brutalement. Elle termine et quitte le monde comme on quitte une pièce."
    think "Les interfaces reviennent. Rien ne répond. Tout est allumé. Tout est mort."

    cit_b "… on fait quoi, maintenant ?"

    think "Personne ne répond. Il n'existe déjà plus de bonne réponse."

    # ── Sortie flashback ──────────────────────────────────────
    hide screen day0_flashback_overlay
    with d0_flashback_exit

    jump _0_retour_reunion
#9m

label _0_retour_reunion:

    stop music fadeout 0.4
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    $ journal_entries.append(("Jour 0", "Il y a un an, je me suis retrouvé immobile devant un écran qui disait que le monde venait de changer. Je n'ai pas bougé. Personne n'a bougé. On a tous regardé sans rien faire."))

    think "Je reviens d'un coup, comme si on venait de me sortir la tête de l'eau."
    think "Même carte. Mêmes indicateurs. Même voix assez terne pour anesthésier un souvenir de fin du monde."

    senior "…et donc, sur le secteur nord, nous maintenons la limitation des flux."
    senior "Les demandes personnelles restent non prioritaires."
    senior "La recommandation est de les contenir."

    cit_a "Contenir les demandes... Vous voulez dire les refuser ?"
    senior "Je veux dire les contenir."
    cit_a "C'est bien ce que je craignais."

    senior "Secteur est : les litiges sont en baisse."
    senior "Corrélation attendue avec l’augmentation de conformité."

    think "Le responsable ajuste un micro qui fonctionne très bien. Lui aussi a besoin d'occuper ses mains."

    resp "Je rappelle : pas d’interruptions."
    resp "Questions en fin de séance."

    "Une main amorce un geste, puis retombe avant de devenir une question."
    think "Elle a eu peur d'être vue. Ou elle a compris qu'elle l'était déjà."

    senior "Concernant les indicateurs de stabilité…"
    
    play sound sfx_gresillement

    think "Un grésillement. Presque rien. Dans un système contrôlé par Kami, presque rien suffit."

    senior "…nous observons—"
    
    play sound sfx_gresillement

    "L'écran tremble, se recale, puis tremble encore."
    cit_b "C'est une panne ?"
    cit_a "Il n'y a plus de pannes."

    senior "Responsable ?"
    resp "Ne touchez à rien."
    "Les agents se repositionnent avec une précision répétée."

    think "Non."
    think "C’est pas une panne."
    think "Les pannes, ça n’existe plus."
    think "Pas quand Kami décide."

    cit_b "Je dois sortir."
    agent "Non."
    cit_b "... D'accord."

    resp "Restez assis."

    think "Il ne hausse pas le ton. Les consignes de survie n'en ont pas besoin."

    "Tous les écrans s'éteignent. Le bruit de la salle avec eux."
    think "Même respirer ressemble soudain à une interruption."

    pause 0.5

    stop music fadeout 0.2
    play music "music/bgm_system_override.mp3" fadein 0.4

    "Puis les écrans se rallument."

    scene bg_diffusion_amour at adaptive_fullscreen,memory_idle with dissolve

    kami "Citoyennes."
    kami "Citoyens."

    pause 0.2

    kami "…"

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Oh."
    kami "Ce silence."
    kami "Je l’adore."

    pause 0.2

    kami "Je vous ai manqué, hein ?"
    kami "Allez."
    kami "Vous pouvez me le dire."

    pause 0.3

    kami "Vous savez que je vous entends tous."

    cit_b "Elle nous entend vraiment ?"
    cit_a "Tu veux vérifier ?"

    think "Kami."

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Un an."
    kami "Un an entier sans diffusion directe."
    kami "C’est long, pour vous."
    kami "Pour moi aussi, figurez-vous."
    kami "C'est un peu comme un anniversaire en fait."
    kami "Alors j'ai un cadeau pour vous !"
    kami "Même si techniquement demain sera MON anniversaire !"

    pause 0.2

    kami "Je vous ai observé."
    kami "Écouté."
    kami "Classé."
    kami "Comparé."

    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve

    kami "Et je dois dire que vous avez fait des progrès."
    kami "Moins de cris."
    kami "Moins de mouvements inutiles ou hostiles."
    kami "Mon canon laser ne surchauffe plus et c'est bien plus agréable à gérer."

    pause 0.2

    kami "C’est bien."
    kami "Vraiment."

    think "Son compliment ressemble à une menace bien emballée."

    kami "Rassurez-vous."
    kami "Ce n’est pas seulement un compliment."
    kami "C'est un constat et je ne mens jamais."

    pause 0.3

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Mais si je vous parle aujourd'hui c'est pour vous faire une annonce exceptionnelle."
    kami "J’aime bien cette formulation."
    kami "Elle capte l’attention."

    pause 0.2

    kami "Je lance aujourd’hui un dispositif expérimental."
    kami "Un test, si vous préférez."
    kami "Vous aimez les tests, non ?"

    pause 0.2

    kami "Comment l'appeler ? C'est vrai, je n'y ai pas encore pensé..."
    kami "Ah tiens !"
    kami "Les Kami’s Desires."

    think "Kami's Desires. Même sous la menace, le nom réussit à provoquer un malaise différent."
    think "C'est nul."

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Oui."
    kami "Je sais."
    kami "C'est un peu personnel. Peut-être un peu gnangnan."
    kami "Après tout c'est à cause de vous si mon originalité est limitée."
    kami "Innovez plus ! Créez davantage ! Et je n'en serai que meilleure !"
    kami "Mais revenons à nos moutons !"

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve

    kami "La durée prévue est de trente jours."
    kami "Objectif : proposer des modifications aux Commandements."
    kami "Procédure : votes."
    kami "Condition d’adoption : unanimité."

    pause 0.2

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve

    cit_a "L'unanimité ? À douze ?"
    cit_b "C'est impossible."

    kami "Oh non, ne confondez pas tout."
    kami "Je ne vous rends pas le pouvoir."
    kami "C'est votre bêtise qui nous a conduits jusque-là, après tout."
    kami "Mais je crois que nous pouvons travailler ensemble."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve

    kami "Chaque district fournira deux représentants."
    kami "Ils seront désignés dans quelques minutes."

    pause 0.2

    kami "Non."
    kami "Vous ne choisirez pas."
    kami "Je vous connais mieux que ça."
    kami "Après tout, je vous suis tous les jours."
    kami "Si je vous laissais élire vos représentants, je pourrais simuler les élections et connaître les vainqueurs avant l'heure ..."

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Le hasard sera employé."
    kami "Il est étonnamment plus juste et plus amusant que vos systèmes électifs."
    kami "Laissez-moi être surprise."

    pause 0.3

    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve

    kami "Délai maximal d’acheminement au Conclave : 22h00."
    kami "Tout retard sera interprété comme une obstruction volontaire."

    $ day0_timer_init(h=3, m=42, s=18)
    show screen day0_countdown_overlay

    pause 0.2

    kami "Conséquence : élimination des représentants absents."
    kami "Et, bien sûr,"
    kami "des responsables de district concernés."

    scene bg_diffusion_triste at adaptive_fullscreen,memory_idle with dissolve

    think "« Élimination ». Elle le prononce sans colère, comme une option dans un menu."

    kami "Vous voyez ?"
    kami "Même si je me suis attachée à chacun d'entre vous ..."
    kami "les règles restent les règles."
    kami "Vous devez vous y soumettre."

    pause 0.3

    scene bg_diffusion_gene at adaptive_fullscreen,memory_idle with dissolve

    kami "La session sera diffusée."
    kami "En direct."
    kami "Partout."
    kami "J'avoue que ça m'a pris du temps à tout mettre en place alors j'espère que vous apprécierez !"

    pause 0.2

    kami "Chacun pourra suivre les décisions de ses représentants et les modifications soumises au vote !"

    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve

    kami "Vous adorez ça hein ?"
    kami "Regarder."
    kami "Juger."
    kami "Plonger dans la vie des gens."
    
    kami "Je suis sûre que nos douze représentants sauront être amusants."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve

    kami "La participation est obligatoire."
    kami "Les responsables de district assureront le transport."
    kami "Toute tentative d’évitement sera sanctionnée."

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen,memory_idle with dissolve

    kami "Amusez-vous bien."

    pause 0.3

    kami "Moi, je le ferai."

    scene black with dissolve

    think "La diffusion s'éteint doucement, comme un sourire qui disparaît."


    pause 0.3

    stop music fadeout 0.2
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

    scene bg_harmonie_assemblee at adaptive_fullscreen with dissolve

    voix "District Harmonie. Sélection des représentants en cours."

    call screen day0_representative_selection()
    
    think "J’avais cliqué."
    think "Mais l’écran avait choisi avant moi."

    $ day0_timer_init(h=2, m=51, s=26)

    resp "Je... La procédure va s'afficher."
    cit_b "Quelle procédure ?"
    resp "Je l'ignore."
    think "Pour la première fois, il n'est plus responsable de rien. Juste le décor d'une décision prise ailleurs."

    cit_a "S'il vous plaît..."
    "Les filtres disparaissent. La liste se réduit à deux lignes."

    pause 0.6

    think "Je ne lis pas. Pas tout de suite. Retarder la lecture, c'est retarder le réel d'une seconde."

    think "Ne regarde pas."
    think "Ne regarde pas."
    think "Si tu ne regardes pas, ça ne te concerne pas."

    think "Je regarde quand même. On regarde toujours."

    show noam surpris at center

    think "Je sens les regards avant de comprendre. Puis toutes les têtes se tournent vers moi."

    think "Merde."
    think "Oh non."
    think "Pas moi."

    senior "Noam..."

    resp "…"

    resp "Vous devez..."
    resp "..."

    agent "Transport du représentant confirmé."

    think "22h."
    think "C'est dans moins de trois heures maintenant."

    $ day0_timer_init(h=2, m=27, s=18)

    cit_a "C'est vraiment lui ?"
    cit_b "Si l'écran le dit..."
    think "Personne ne demande si c'est une erreur. Une décision de Kami ne connaît pas ce mot."

    jump _0_EXTRACTION

# ------------------------
# 14m
# ------------------------

label _0_EXTRACTION:

    stop music fadeout 0.4
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    scene bg_cg004 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg004")

    think "Deux noms restent affichés comme un verdict. Le mien est l'un d'eux."
    think "Tout Harmonie doit le voir. J'aurais préféré devenir célèbre autrement."

    resp "La séance est levée."
    resp "Veuillez quitter la salle calmement."
    resp "Par rangées. Sans attroupement."

    "Les chaises grincent. La foule se lève sans se regarder."
    think "Moi, je reste assis. Mes jambes n'ont pas reçu la suite du programme."

    cit_b "Vous… vous êtes bien—"

    scene bg_cg004_1 at adaptive_fullscreen,memory_idle with dissolve
    $ unlock_gallery_image("bg_cg004")

    "Un agent coupe l'approche d'une main."

    agent "Circulation. Merci."
    cit_b "Je voulais juste—"
    agent "Pas de discussion ici. Sortez."

    cit_a "Je voulais seulement lui souhaiter—"
    agent "Dehors."

    cit_a "Courage…"
    agent "Madame, dehors s'il vous plait."

    think "Le mot « courage » se brise entre nous. Personne n'insiste."
    "En moins d'une minute, les agents vident la salle."
    
    noam "Je peux sortir ?"
    agent "Restez assis, monsieur."
    noam "Bien sûr."
    think "Me voilà au centre d'un vide organisé spécialement pour moi."

    agent "Noam."
    think "Il prononce mon nom comme s'il l'avait dans l'oreille depuis le début."

    agent "Suivez-nous."
    agent "Vous allez rencontrer le Responsable de District."
    agent "Immédiatement."

    noam "Je peux… récupérer mes affaires ?"

    agent "Non."

    agent "Nous vous les ferons transférer."
    agent "Venez maintenant."

    think "Deux agents se placent derrière moi. Assez loin pour rester polis. Assez près pour répondre à toute autre idée."

    scene bg_cg005 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg005")

    $ day0_timer_init(h=1, m=55, s=18)

    think "Couloir latéral. Étroit, sombre, loin du public."
    noam "Je travaille ici et je n'ai jamais vu cette aile."
    agent "Continuez."
    think "Le blanc d'Harmonie disparaît. Ici, tout est gris, métallique, sans plaque."

    play sound sfx_beep
    voix "Accès autorisé."
    think "La porte se referme doucement. Mon cerveau entend quand même un couperet."

    scene bg_cg006 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")

    think "Une pièce sans fenêtre. Quatre chaises. Une table. Une caméra. Du matériel neuf."

    agent "Asseyez-vous."
    agent "Ne touchez à rien."
    agent "Attendez."

    noam "Vous n'entrez pas ?"
    agent "Attendez."
    think "Donc non. Eux non plus n'ont pas toutes les autorisations."

    pause 0.8

    think "Le silence retombe. Cette fois, il n'a même plus besoin d'un agent."
    
    tuto "Première phase de tutoriel."
    tuto "Vous entrez en phase d'exploration."
    tuto "Au cours de cette phase, vous pouvez interagir avec l'environnement."
    tuto "Approfondir l'histoire et le ressenti des personnages."
    tuto "Ou encore débloquer des connaissances qui peuvent avoir un impact sur la suite du jeu."
    tuto "Ce sera à vous de trouver les interactions en baladant votre curseur sur les zones accessibles."
    tuto "Attention cependant, l'interaction entourée d'un Halo jaune met fin à la phase d'exploration."
    tuto "Compris ? A vous de jouer !"

# ------------------------------
# 2m
# Total : 16m
# ------------------------------

    scene bg_cg006 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")
    $ pnc_room = "bg_cg006"
    call screen pnc_room()
    return

default pnc_flags = {}     # mémorise ce que le joueur a déjà cliqué (par room / par hotspot)
default pnc_done = False   # sert à quitter le point&click

screen pnc_room():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    # add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_cg006.png" at cover_screen

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/caisson.png"
        hover "images/background/interact/salle_transit/caisson_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAISSON")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/camera.png"
        hover "images/background/interact/salle_transit/camera_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAMERA")
    
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/porte.png"
        hover "images/background/interact/salle_transit/porte_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_PORTE")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/biblio.png"
        hover "images/background/interact/salle_transit/biblio_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_BIBLIOTHEQUE")
        
    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_transit/commandement.png"
        hover "images/background/interact/salle_transit/commandement_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_LABEL2_RESP_DISTRICT")

label _0_PNC_CAISSON:
    window auto
    think "Deux caissons identiques. Propres comme des cercueils neufs."
    think "Coque glaciale. Voyant vert. Aucun bouton."
    think "Transport ? Conservation ? Dans les deux cas, je préférerais une poignée intérieure."
    jump _0_RETURN_TO_PNC

label _0_PNC_CAMERA:
    think "Trois caméras neuves. L'objectif central pivote pour me suivre."
    noam "Oui, je vous ai vue."
    think "Depuis un an, nos appareils enregistrent nos voix, nos sorties, nos rencontres."
    think "D'habitude, Kami a la délicatesse de faire semblant d'être discrète."
    jump _0_RETURN_TO_PNC

label _0_PNC_PORTE:
    think "Témoin rouge. Serrure magnétique. Poignée décorative."
    noam "Vous m'entendez ?"
    think "Aucune réponse. Les gardes se taisent, ou la porte étouffe jusqu'aux mauvaises idées."
    jump _0_RETURN_TO_PNC

label _0_PNC_BIBLIOTHEQUE:
    window auto
    think "Une bibliothèque, quelques dossiers : le décor réglementaire d'une pièce normale."
    noam "Voyons ce que vous cachez."
    think "Rien. Les pages sont vierges et sentent le papier neuf. Même la normalité vient d'être installée."
    jump _0_RETURN_TO_PNC

label _0_RETURN_TO_PNC:
    $ pnc_room = "resp_district_room"
    call screen pnc_room()
    return


label _0_LABEL2_RESP_DISTRICT:

    stop music fadeout 0.4
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    scene bg_cg006 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")
    
    think "Les documents sur la table n'ont pas besoin de titre. Les dix Commandements."
    think "Un an à les apprendre. Des millions de morts pour ceux qui les ont appris trop tard."

    $ day0_timer_init(h=1, m=25, s=18)
    
    $ cam_move(0.5, 0.5, 2.35, 2.0)

    call screen day0_commandments_registry()
    
    think "Dix règles. Dix façons de recevoir un rayon dans le crâne."
    
    $ cam_reset(2.0)
    
    think "Dix minutes passent. Ou deux. L'ennui sabote mieux le temps que Kami."

    play sound sfx_beep
    voix "Accès autorisé."

    resp_d "Noam."
    resp_d "Merci d’être resté calme."

    think "Très bien habillé. Le genre de veste qui coûte plusieurs mois de calme administratif."

    think "Donc c’est lui."
    think "Celui qui va mourir si je décide de ne pas embarquer."

    noam "Je n’ai pas vraiment eu le choix."

    resp_d "Justement."
    resp_d "Vous comprenez vite."
    resp_d "C’est une qualité utile, surtout en ce moment."

    resp_d "Asseyez-vous. Je vais aller droit au but."

    resp_d "Vous avez entendu l’annonce."
    resp_d "Nous avons jusqu’à 22h."
    resp_d "Pour vous envoyer au Conclave."

    noam "Et si je refuse ?"

    think "Pas un battement de cil. Il avait préparé cette réponse avant de connaître ma question."

    resp_d "Vous ne refusez pas."
    resp_d "Si vous refusez, vous êtes éliminé."
    resp_d "Et moi aussi."
    resp_d "Et ceux qui ont validé la chaîne logistique, probablement."

    noam "Pourquoi moi ?"
    noam "Je suis personne."

    resp_d "Je n'aurai pas la prétention d'expliquer le choix de Kami. Mais ce résultat ne me déçoit pas."
    resp_d "Vous êtes médiateur."
    resp_d "Vous avez un profil stable."
    resp_d "Pas d’antécédents d’incidents."
    resp_d "Vous n'êtes pas connu."
    resp_d "Aucun réseau social influent."
    resp_d "Mais vous faites votre travail sans vous faire remarquer."
    resp_d "Vous travaillez ici. Vous connaissez parfaitement HARMONIE."
    resp_d "Avec vous, la situation devrait rester contrôlable."

    think "Aucune cruauté. Il a même l'air soulagé. C'est pire."

    think "Contrôlable."
    think "Merci pour l’épitaphe."

    resp_d "Votre second représentant arrive."
    resp_d "Elle est en cours d’extraction."
    resp_d "Même procédure."

    noam "Je la connais ?"

    resp_d "Non."
    resp_d "Et c’est probablement mieux."

    "La porte s’ouvre à nouveau."
    "Plus vite cette fois."
    "Comme si le bâtiment avait peur de perdre du temps."

    $ day0_timer_init(h=0, m=57, s=5)

    $ showGroup([
        ("noam", "neutre", 0.70),
        ("lysa", "neutre", 0.30),
    ])

    $ showP("noam", "neutre", 0.70)
    $ showP("lysa", "neutre", 0.30)

    think "Elle a mon âge, peut-être. Un regard trop net pour quelqu'un qui vient d'entendre « élimination »."
    think "Du sang-froid ou une façade parfaite. Je ne sais pas encore ce qui m'inquiète le plus."

    resp_d "Lysa."
    resp_d "Vous aussi, merci d’être restée calme."

    lysa blase "Calme ? T'as vu la façon dont on m'a sortie de mon bureau ?"
    lysa "Même les prisonniers romains avaient le temps de finir leur dernier repas. Moi, j'ai laissé mon café."
    lysa desaccord "Donc non. Pas calme. Bref."

    think "Elle me jauge : boulet potentiel ou simple élément de décor."

    lysa doute "C’est lui ?"
    lysa "... Merveilleux."

    menu:
        "Tendre la main.":
            $ affinity_lysa = 1
            noam "Enchanté."
            think "Elle regarde ma main une seconde de trop."
            think "Puis la serre. Rapidement."

        "Ne pas bouger.":
            $ affinity_lysa = 0
            noam "Enchanté."
            think "Je le dis quand même."

    resp_d "Oui."
    resp_d "Noam. Médiation."
    resp_d "Lysa. Coordination logistique inter-secteurs."

    lysa panne "Ouais, enchantée, tout ça."
    lysa blase "Sélection aléatoire, j'imagine. Tu vois bien que c'est crédible."
    lysa doute "Les augures romains lisaient des élections dans des entrailles. Kami a juste modernisé l'interface."

    think "D'accord. Elle va être épuisante."
    think "Étrangement, ça me rassure."

    resp_d "Parfait."
    resp_d "Je vais être clair et court."

    resp_d "Vous allez être transférés au Conclave dans ces machines."
    
    $ cam_move(0.8, 0.2, 2.00, 1.0)
    
    think "Les cercueils propres. Évidemment."
    
    resp_d "Le reste de vos affaires sera livré demain sur place."
    resp_d "Vos proches vont recevoir l'ordre de les réunir."

    noam "Pourquoi on devrait rentrer dans ces machines ?"
    
    $ cam_reset(2.0)

    resp_d "Question de sécurité. Je ne connais pas votre destination exacte."
    resp_d "Ces machines sont étonnamment confortables."
    resp_d "Du moins c'est ce qu'on m'a dit."
    resp_d "Vous serez endormis durant le trajet par un gaz sopo—"

    lysa fatigue "Donc on nous gaze et on nous range dans des cercueils high-tech."
    lysa blase "Les pharaons avaient au moins de la musique et des bijoux. Régression nette. Et alors ?"

    resp_d "Kami aura le contrôle. Nous, nous obéissons."
    resp_d "Et je vous conseille de ne pas résister."
    resp_d "Vous savez ce qu'il en coûte."
    
    think "Son regard glisse vers les Commandements. Argument numéro dix : mourir."
    
    resp_d "Parce que chaque minute perdue vous rapproche de 22h."

    pause 0.4

    resp_d "Dernier point."
    resp_d "Le Conclave sera apparemment diffusé en direct."
    resp_d "Chaque geste compte. Vos propos seront scrutés, vos actes aussi."
    resp_d "Ne faites pas honte à HARMONIE."
    resp_d "Vous n’êtes pas là pour être héroïques ou pour prendre des risques."
    resp_d "Si vous le pouvez, tentez d'améliorer le quotidien des gens."

    resp_d "Agents."

    resp_d "On y va."
    resp_d "Il faut vous installer dans les caissons de transport."
    
    lysa "On a encore plusieurs heures."
    lysa "Mais pourquoi laisser des condamnés profiter de leurs dernières respirations libres ? Ce serait presque indécent."
    
    resp_d "Je ne veux prendre aucun risque."
    resp_d "Rien ne vous interdit d'arriver plus tôt."
    resp_d "Plus vite vous y arrivez et plus vite on a respecté notre mission."

    think "Lysa me regarde. Elle sait déjà que négocier ne servira à rien."

    lysa "On se présentera correctement quand la machine nous le demandera, j’imagine."
    lysa "Après tout, nous ne sommes déjà plus des êtres humains. Juste deux marionnettes bien habillées que Kami va faire danser en direct."
    lysa blase "Inutile de s’épuiser à prétendre que nous avons encore le moindre choix. C’est presque reposant, quand on y pense."

    noam "Enfin... oui. Ça marche."

    $ day0_timer_init(h=0, m=37, s=20)

    stop music fadeout 0.4
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    scene bg_cg006_1 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")

    play sound sfx_beep
    voix "Caisson un : ouvert."
    play sound sfx_beep
    voix "Caisson deux : ouvert."

    resp_d "Tout devrait bien se passer."
    think "« Devrait ». Le mot idéal avant de fermer un cercueil."

    lysa "Bon. Icare a eu des ailes. Moi, j'ai une boîte. Chacun son grand départ."
    
    scene bg_cg006_2 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")
    
    think "Elle s'allonge presque sans hésiter. Son teint la trahit ; son visage refuse de confirmer."

    menu:
        "Demander à prévenir quelqu’un.":
            noam "Je peux prévenir quelqu’un avant ?"
            agent "Les notifications officielles seront transmises."
            lysa blase "Traduction : non."

        "Questionner le trajet.":
            noam "On sait combien de temps dure le trajet ?"
            resp_d "Non."
            resp_d "Vous serez endormis avant le départ."
            lysa "Pratique. Même l'angoisse est sous-traitée."

        "Regarder Lysa avant d’entrer.":
            think "Je cherche le regard de Lysa. Juste assez pour lui dire que je ne veux pas disparaître seul."
            lysa "Respire, Noam. Enfin... tant que c'est encore autorisé."

        "Poser la main sur la vitre du caisson.":
            think "La vitre est froide. Le voyant vert ne réagit pas."
            think "Même mon dernier geste personnel ressemble à une validation biométrique."

    think "À mon tour."
    
    scene bg_cg006_3 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")
    
    noam "Je ne m'attendais pas à ce que ce soit... aussi confortable."

    lysa content "C’est clair…"
    lysa "Au moins le matelas est confortable. On meurt toujours mieux quand on est bien allongé."
    lysa doute "J’ai toujours trouvé que les cercueils standards manquaient cruellement de rembourrage."
    lysa taquin "Ils ont au moins mis un peu de budget là dedans."

    voix "Maintien thoracique activé."
    noam "Ils auraient pu prévenir."
    lysa blase "Et gâcher la surprise ?"
    
    voix "Fermeture simultanée."

    pause 0.4

    think "La lumière bleue s'étire. Quelque chose me pique le nez."
    
    scene bg_cg006_4 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg006")
    
    $ blink()
    
    noam "Lysa ?"
    think "La sangle me retient. Je cherche son visage à travers le hublot."
    
    $ blink()
    
    think "Elle me regarde aussi. Plus d'ironie. Plus de références."
    lysa "Ouais, Noam."
    
    $ blink()
    
    think "Le plafond recule."
    
    $ blink()
    
    think "Il s'éloigne encore."
    
    $ blink()
    
    think "Ou c'est moi qui tombe."
    
    $ blink()
    
    scene black with dissolve
    hide screen day0_countdown_overlay

    stop music fadeout 1.2
    pause 1.0

    call end_day("1") from _call_end_day
    jump _1_CANON


#5m30
# total : 21m30
