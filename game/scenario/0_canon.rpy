# --------------------------------------------------------------------------------------------
# JOUR 0 — Définitions partagées et séquence active après la sélection
# Le début actuellement joué se trouve dans 0_rewrite.rpy.
# --------------------------------------------------------------------------------------------

# (Optionnel) Ambiances / transitions rapides
define sfx_door = "sfx/door_soft.mp3"
define sfx_beep = "sfx/terminal_beep.ogg"
define sfx_paper = "audio/sfx_paper.mp3"
define sfx_gresillement = "audio/sfx_gresillement.mp3"

default journal_entries = []
default day0_badge_dropped = False
default day0_human_badge = False
default day0_human_handshake = False
default day0_human_look_lysa = False

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
# Ancien début long supprimé : l'entrée active est _0_CANON dans 0_rewrite.rpy.
# Suite réellement atteinte depuis 0_rewrite.rpy.
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

screen pnc_room():

    modal True
    zorder 200

    # Tous les calques ont la même définition que bg_cg006 et utilisent le
    # même transform afin de rester alignés, quelle que soit la résolution.
    add "images/background/cg/bg_cg006.png" at cover_screen

    # Deux caissons de transport.
    imagebutton:
        idle "images/background/interact/salle_transit/caisson.png"
        hover Transform(
            "images/background/interact/salle_transit/caisson.png",
            matrixcolor=BrightnessMatrix(0.18) * SaturationMatrix(1.15)
        )
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAISSON")

    # Trois caméras de surveillance.
    imagebutton:
        idle "images/background/interact/salle_transit/camera.png"
        hover "images/background/interact/salle_transit/camera_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_CAMERA")

    # Bibliothèque et dossiers au fond de la salle.
    imagebutton:
        idle "images/background/interact/salle_transit/biblio.png"
        hover Transform(
            "images/background/interact/salle_transit/biblio.png",
            matrixcolor=BrightnessMatrix(0.18) * SaturationMatrix(1.15)
        )
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_0_PNC_BIBLIOTHEQUE")

    # Le registre termine l'exploration ; son survol doré reprend le halo
    # annoncé dans le tutoriel.
    imagebutton:
        idle "images/background/interact/salle_transit/commandement.png"
        hover Transform(
            "images/background/interact/salle_transit/commandement.png",
            matrixcolor=TintMatrix("#FFF0A0") * BrightnessMatrix(0.28)
        )
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

    think "Les documents sur la table n'ont pas besoin de titre : les dix Commandements, appris en un an et trop tard pour des millions de morts."

    $ day0_timer_init(h=1, m=25, s=18)
    
    $ cam_move(0.5, 0.5, 2.35, 2.0)

    call screen day0_commandments_registry()
    
    think "Dix règles. Dix façons de recevoir un rayon dans le crâne."
    
    $ cam_reset(2.0)
    
    think "Dix minutes passent. Ou deux. L'ennui sabote mieux le temps que Kami."

    play sound sfx_beep
    voix "Accès autorisé."

    $ showGroup([
        ("man", "neutre", 0.30),
        ("noam", "neutre", 0.70),
    ])

    resp_d "Noam."
    resp_d "Merci d’être resté calme."

    think "Très bien habillé. Le genre de veste qui coûte plusieurs mois de calme administratif."

    think "C'est donc lui qui mourra si je décide de ne pas embarquer."

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
    resp_d "Vous travaillez ici. Vous connaissez parfaitement [codex_dialogue_link('harmonie', 'HARMONIE')]."
    resp_d "Avec vous, la situation devrait rester contrôlable."

    think "Aucune cruauté. Il a même l'air soulagé. C'est pire."

    think "Contrôlable : merci pour l'épitaphe."

    resp_d "Votre second représentant arrive."
    resp_d "Elle est en cours d’extraction."
    resp_d "Même procédure."

    noam "Je la connais ?"

    resp_d "Non."
    resp_d "Et c’est probablement mieux."

    "La porte s'ouvre plus vite cette fois, comme si le bâtiment lui-même avait peur de perdre du temps."

    $ day0_timer_init(h=0, m=57, s=5)

    $ showGroup([
        ("noam", "neutre", 0.70),
        ("lysa", "neutre", 0.30),
    ])

    $ showGroup([("noam", "neutre", 0.70), ("lysa", "neutre", 0.30)])

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
            $ day0_human_handshake = True
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

    think "Elle va être épuisante et, étrangement, ça me rassure."

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
    resp_d "Ne faites pas honte à [codex_dialogue_link('harmonie', 'HARMONIE')]."
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
            $ day0_human_look_lysa = True
            think "Je cherche le regard de Lysa. Juste assez pour lui dire que je ne veux pas disparaître seul."
            lysa "Respire, Noam. Enfin... tant que c'est encore autorisé."

        "Poser la main sur la vitre du caisson.":
            think "La vitre est froide. Le voyant vert ne réagit pas."
            think "Même mon dernier geste personnel ressemble à une validation biométrique."

    if day0_human_badge and day0_human_handshake and day0_human_look_lysa:
        $ unlock_succes("succes002")

    think "À mon tour."
    
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
    
    $ blink()
    
    noam "Lysa ?"
    think "La sangle me retient. Je cherche son visage à travers le hublot."
    
    $ blink()
    
    think "Elle me regarde aussi. Plus d'ironie. Plus de références."
    lysa "Ouais, Noam."
    
    $ blink()
    
    think "Le plafond recule encore, à moins que ce soit moi qui tombe."
    
    $ blink()
    
    scene black with dissolve
    hide screen day0_countdown_overlay

    stop music fadeout 1.2
    pause 1.0

    call end_day("1") from _call_end_day
    jump _1_CANON


# Total jour 0 : 13m30
