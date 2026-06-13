# --------------------------------------------------------------------------------------------
# JOUR 1 — Canon (version pro)
# Scène 1 : Réveil sur les sièges du Conclave
# Noam = narrateur principal
#
# Mise en scène : TRIO DYNAMIQUE
#   - Toujours 3 persos affichés (dès qu'on entre en dialogue)
#   - Quand un 4e parle : on retire celui qui n'a pas parlé depuis le plus longtemps
#   - Les slots sont fixes : gauche (0.22) / centre (0.50) / droite (0.78)
#   - Transitions animées via showP (entrée) et hideP (sortie)
# --------------------------------------------------------------------------------------------

default j1_noam_prudence = 0
default j1_noam_initiative = 0
default j1_noam_mediation = 0
default j1_noam_curiosity = 0
default j1_wakeup_trace_attempts = 0
default j1_urn_trace_attempts = 0
default j1_jammer_trace_attempts = 0
default j1_tablet_touched = False
default j1_amendment_validated = False
default j1_amendment_deposited = False
default noam_amendement_choix = None
default noam_room_jammer_on = True
default choix_1_soir = "dormir"

define sfx_drop = "audio/sfx_drop.mp3"
define sfx_shower = "audio/sfx_shower.mp3"

init 2 python:
    day1_amendment_cards = [
        {
            "id": "information_locale",
            "title": "Parole locale encadrée",
            "commandment": "Cinquième Commandement",
            "intent": "Autoriser les informations locales non politiques.",
            "short_wording": "Les faits locaux, immédiats et non sensibles peuvent être communiqués sans validation préalable.",
            "wording": "La transmission d'informations non validées reste interdite pour les sujets politiques, stratégiques ou interdistricts. Les faits locaux, immédiats et non sensibles peuvent être communiqués sans validation préalable d'ARCHIVE.",
            "risks": "Risque de flou entre fait local et information politique.",
        },
        {
            "id": "assistance_minimale",
            "title": "Assistance possible",
            "commandment": "Commandements de conduite civile",
            "intent": "Protéger le geste d'aide quand il ne met personne en danger.",
            "short_wording": "Un citoyen peut porter assistance en cas de danger immédiat si son geste n'aggrave pas la situation.",
            "wording": "Aucun citoyen ne peut être sanctionné pour avoir porté assistance à une personne en danger immédiat, si cette assistance n'aggrave pas la situation et ne contrevient pas à une procédure de sécurité active.",
            "risks": "Risque d'interprétations abusives en situation de crise.",
        },
    ]

    if "reglement_conclave" not in CODEX_ENTRIES:
        CODEX_ENTRIES["reglement_conclave"] = {
            "title": "Règlement du Conclave",
            "category": "coutume",
            "unlocked_day": 1,
            "text": """Le Conclave dure trente jours. Pendant cette période, les représentants restent isolés dans le complexe et ne peuvent pas rejoindre leur district, ni initier de contact vers l'extérieur. Si un appel extérieur leur parvient, ils peuvent y répondre, mais ils ne peuvent pas provoquer eux-mêmes l'échange.

Chaque représentant dépose un amendement lors de la première journée. Les propositions sont déposées dans une urne, anonymement. Dix amendements sont ensuite tirés au sort pour être soumis au vote au cours du Conclave ; deux propositions peuvent donc ne jamais être débattues.

Un vote a lieu tous les trois jours. Pour qu'un amendement soit adopté, tous les bulletins exprimés doivent être favorables. Les abstentions et absences ne comptent pas dans les bulletins exprimés, mais une seule voix contre suffit à rejeter le texte. Selon la nature de la proposition, un rejet peut aussi produire des conséquences.

Les chambres individuelles sont équipées de brouilleurs. Par défaut, le brouilleur coupe les caméras, l'audio et les capteurs de la chambre. Un représentant peut le désactiver, mais la pièce redevient alors potentiellement observable.

Les espaces communs restent surveillés et enregistrés. Les Commandements ordinaires ne s'appliquent pas dans le Conclave, mais les règles propres au complexe restent actives. Kami ne vote pas et ne propose pas d'amendement ; elle organise, observe, tire au sort, annonce les résultats et applique les changements validés."""
        }


# =============================================================================
label _1_CANON:
# =============================================================================

    $ day_id = 1
    $ current_day = 1
    $ current_period = "Matin"

    # --- HUD jour/période (persistant toute la journée) ---
    show screen day_period_hud

    scene black
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    show screen day1_wakeup_overlay("heavy")

    think "Jour un."
    think "Enfin, je crois."
    think "Je n'ai pas vu le temps passer."
    think "Je me suis endormi dans un caisson."
    think "Et là… je me réveille sur un siège."

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with fade

    "Un dossier rigide sous mon dos."
    "Un siège froid et métallique."
    "L'air est sec, presque comme s'il était recyclé."
    "Ça sent le plastique neuf et le produit de nettoyage."

    $ blink()

    "Je cligne des yeux."
    "Ma bouche est sèche."
    "Ma nuque me fait mal."
    "Ma main droite ne répond pas tout de suite."

    # --- Tutoriel trace QTE (première fois) ---
    show screen day1_tuto_trace
    pause

    call day1_play_trace(path_type="curve_right", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_day1_trace_wakeup
    $ j1_noam_initiative += 1

    hide screen day1_wakeup_overlay
    show screen day1_wakeup_overlay("soft")

    "La sensation revient par à-coups."
    "D'abord les doigts."
    "Puis le poignet."
    "Enfin le bras."

    "Je me redresse."
    hide screen day1_wakeup_overlay
    "Autour de moi, d'autres sièges."
    "Beaucoup."
    "En cercle."
    "Et sur chaque siège… quelqu'un."

    "Certains bougent légèrement."
    "D'autres restent figés. Ils dorment encore."

    "Personne ne parle fort."
    "Juste des respirations régulières."
    "Des froissements de vêtements."
    "Un raclement de gorge quelque part."

    play sound sfx_beep
    "-Bip-"

    "Un son bref."
    "Pas une alarme."
    "Un bip de système."
    "Ça vient d'en bas, il semble y avoir plusieurs étages ici."

    "Je baisse les yeux."
    "Sur mon pupitre, une tablette est encastrée."
    "Éteinte."
    "Noire."

    menu:
        "Que fait Noam avec la tablette ?"

        "Poser la main sur l'écran":
            $ j1_noam_curiosity += 1
            $ j1_tablet_touched = True
            "Je pose deux doigts sur la surface froide."
            call screen day1_tablet_interaction()
            play sound sfx_beep
            $ shake(6, 0.2)
            "-Bip-"
            think "Même éteinte, elle note que j'existe."

        "Retirer la main du pupitre":
            $ j1_noam_prudence += 1
            "Je garde mes doigts contre le bord du siège."
            think "Pas maintenant. Pas avant de comprendre à quoi elle sert."

    "Je tourne la tête."
    "Je cherche Lysa du regard."
    "Parce que c'est la seule personne que je connais un minimum."
    "Au moins de nom."

    $ showGroup([
        ("lysa", "neutre", -0.11),
        ("noam", "inquiet", 0.01),
        ("ryn", "colere", 0.13),
        ("mara", "rire", 0.25),
        ("tomas", "reflechit", 0.37),
        ("elen", "surpris", 0.49),
        ("julian", "peur", 0.60),
        ("iris", "inquiet", 0.72),
        ("nyra", "triste", 0.84),
        ("kael", "calme", 0.96),
        ("elias", "neutre", 1.08),
        ("sael", "raison", 1.20),
    ])

    noam inquiet "Lysa… ?"


    lysa blase "Ouais..."
    lysa blase "T'es enfin réveillé."

    noam inquiet "On est où… ?"


    lysa reflexion "Si je devais deviner…"
    lysa reflexion "Je dirais le Conclave."

    "Je regarde autour."
    "Je ne connais aucun des autres visages."

    think "Donc c'est vrai."
    think "Ils nous ont tous mis au même endroit."
    think "En même temps pour participer à ce truc étrange."

    "Quelqu'un se lève brusquement."
    "Un siège grince."
    "Ça claque dans le silence."


    ryn colere "Putain mais on est où là ?!"
    ryn colere "Qui a fait ça ?!"

    "Personne ne répond."
    "Pas un seul mot."



    mara rire "Tu veux dire… à part l'IA qui tient le monde en laisse ?"

    ryn colere "Je parle de ce qui nous arrive, là, maintenant."
    ryn colere "Qui nous a endormis."
    ryn colere "Qui nous a trimballés ici."



    tomas reflechit "Probablement… personne qui soit vraiment là. Enfin, je veux dire… pas ici, pas physiquement."
    tomas reflechit "Ça ressemble à une procédure. Automatique. Presque… mécanique."



    elen surpris "Automatique ou pas… c'est quand même nous qui sommes embarqués de force, non ?"
    elen surpris "J'arrive pas à me dire que c'est juste 'normal' maintenant."
    elen surpris "Même si… ouais, à force on finit par s'habituer à tout. C'est ça qui me fait peur."

    "Je lève les yeux."
    "Je cherche les caméras."
    "Il y en a."
    "Évidemment."
    "Propres."
    "Discrètes."

    think "Ça, c'est la partie la plus habituelle de tout ça."
    think "C'est triste mais on y est habitué."



    julian peur "Vous… vous entendez ça ?"
    julian peur "Rien. Absolument rien. On dirait qu'on est les derniers humains sur Terre."



    iris inquiet "Mais… y a même pas un murmure ! Rien ! C'est flippant à quel point c'est silencieux ici !"
    iris inquiet "Et en plus on sait même pas ce qu'on est censés faire, hein ! On attend quoi, un miracle ?"



    nyra triste "Ce silence est voulu."
    nyra triste "C'est un test. Kami veut voir comment on réagit."



    kael calme "Ou alors… c'est juste une attente."
    kael calme "Peut-être qu'elle attend quelque chose. Quelque chose de précis."

    "Un silence encore plus lourd tombe."
    "Personne n'aime l'idée d'attendre."
    "Surtout dans une situation comme celle-là."
    "Parce que ça veut dire qu'on dépend du bouton 'play' de quelqu'un d'autre."



    noam reflexion "Au fait, vous avez vu Kami ?"

    "Pas un seul regard ne se lève vers l'écran central."
    "Il n'est pas allumé. Tout comme les tablettes disposées à chacune des places."
    "Et parce que personne n'a envie de prononcer son nom trop fort."



    ryn reflechit "Non."
    ryn reflechit "Et ça me fait chier de le dire, mais je préfèrerais avoir des nouvelles."



    mara rire "J'adore, putain."
    mara rire "Douze pigeons, zéro animateur."
    mara rire "Pas de mode d'emploi, pas d'hôte, même pas un petit speech d'accueil."
    mara rire "Elle nous snobe direct, la garce."



    tomas reflechit "On parle de Kami, quand même."
    tomas reflechit "Elle est toujours là. Même quand on ne la voit pas."
    tomas reflechit "Même sans image… elle reste là."

    "Je fixe la tablette noire sur mon pupitre."
    if j1_tablet_touched:
        "Je n'y touche pas une seconde fois."
        "Le message ACCÈS LIMITÉ est encore trop frais dans ma tête."
    else:
        "Je tapote du doigt."
        "Rien."

    think "C'est ça qui me dérange."
    think "D'habitude, Kami aime être… présente."
    think "Là, c'est vide."
    think "Comme une salle de classe sans prof."
    think "Sauf qu'ici le prof peut te tuer."

    "Lysa se penche légèrement vers moi."
    "Elle parle bas par réflexe."



    lysa reflexion "Tu as remarqué ça ?"



    noam reflexion "Quoi ?"


    lysa neutre "Aucun ordre."
    lysa neutre "Aucun écran."
    lysa neutre "Aucun message."
    lysa fatigue "... Silence radio."

    noam reflexion "Ça veut dire quoi pour toi ?"


    lysa blase "Ça veut dire que soit on est censé faire quelque chose, soit que Kami attend un autre moment."
    lysa blase "Et ça…"
    lysa blase "J'aime pas."

    pause 0.4

    "Au centre de la salle, une structure circulaire."
    "Un vaste écran qui fait un tour complet sur lui-même."
    think "C'est comme si on regardait un film mais qu'on attendait l'acteur principal."

    play sound sfx_beep
    "-Bip-"

    "Un deuxième bip."
    "Puis rien."

    "Quelqu'un se lève."
    "Un pas."
    "Puis s'arrête."



    ryn reflechit "On reste assis ?"
    ryn reflechit "On attend ?"
    ryn reflechit "C'est ça le plan ?"

    elias neutre "… Et après ? Tu comptes faire quoi ?"



    sael raison "Le plan, c'est de survivre."
    sael raison "Et pour l'instant, bouger sans info…"
    sael raison "c'est un risque. Et tu veux que je te rappelle ce qui arrive à ceux qui prennent des risques ?"

    "Derrière, une petite voix se fait entendre."
    elen desaccord "Mais attendre… c'est aussi super risqué, tu trouves pas ?"
    elen desaccord "On mise sur le fait que ça va pas empirer…"


    tomas raison "Tout ça… c'est un pari, non ? Tout le temps."
    tomas raison "On s'est tous fait prendre de court. Moi le premier."
    tomas raison "Même les gens des districts… on aurait dit qu'ils tombaient des nues."

    "Je sens mon cœur accélérer."
    "Pas de panique."
    "Juste la lucidité qui pique."

    menu:
        "Que fait Noam ?"

        "Se lever pour observer la salle":
            $ j1_noam_initiative += 1
            "Je me lève à moitié."
            "Pas assez pour provoquer quoi que ce soit."
            "Juste assez pour voir les issues, les caméras, les pupitres."
            think "Tout est prévu pour qu'on soit visibles."

        "Rester assis et écouter":
            $ j1_noam_prudence += 1
            "Je reste assis."
            "J'écoute les respirations, les voix, les bips de la salle."
            think "Avant d'agir, il faut savoir dans quoi on met les pieds."

    think "Jour un."
    think "Et on est déjà en train d'essayer de deviner les règles."
    think "Super."

    "Je jette un regard à Lysa."
    "Elle ne tremble pas."
    "Mais sa jambe bouge."
    "Un mouvement minuscule."



    noam reflexion "On fait quoi, alors ?"

    "Personne ne répond tout de suite."
    "Parce que personne ne veut être le premier à choisir."
    "Parce que choisir, ça peut nous tuer."

    pause 0.6

    "Un souffle de ventilation change."
    "Très léger."
    "Mais tout le monde l'entend."
    "Parce qu'on n'a plus que ça à entendre."

    "Et là, au-dessus du pupitre central…"
    "Une lumière blanche s'allume."
    "Faible."
    "Comme une veilleuse."
    "Au même moment, le bruit d'un mécanisme qui s'active prend de l'ampleur."

    play sound sfx_gresillement
    $ shake(8, 0.25)

    "Puis l'écran central s'allume enfin."
    $ cam_move(0.5, 0.05, 3.00, 1.0)


    pause 0.4

    $ hideGroup()
    jump _1_KAMI_APPARITION

# =============================================================================
# 3m — Total : ~24m30
# =============================================================================

label _1_KAMI_APPARITION:

    play music "music/bgm_system_override.mp3" fadein 0.4
    scene bg_diffusion_amour at adaptive_fullscreen with fade
    $ bc_off()
    show screen kami_broadcast_ui

    kami "Ah… vous êtes tous réveillés."
    kami "Parfait."
    kami "J'avais peur d'avoir surestimé votre capacité à survivre à une sieste forcée."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Les sièges étaient confortables, j'espère."
    kami "J'ai hésité avec des bancs en métal."
    kami "Et puis je me suis dit que vous préféreriez commencer… doucement."

    pause 0.4

    $ bc_show("noam", "inquiet", px=-80, py=-50, pz=0.8)
    noam reflexion "Pourquoi nous ?"

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Oh."
    kami "Excellente question."

    kami "Parce que vous êtes douze."
    kami "Et que douze, c'est un chiffre pratique."
    kami "Assez pour créer des alliances."
    kami "Pas assez pour se cacher dans la foule."

    pause 0.3

    $ bc_show("ryn", "colere", px=-90, py=-40, pz=0.85)
    ryn reflechit "Un test de quoi ?"

    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Un test de vous."
    kami "De vos choix."
    kami "De l'humanité en général."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "De votre capacité à obéir…"
    kami "Et à prétendre que vous obéissez 'pour le bien commun'."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Croyez-moi."
    kami "Ça ne sera pas si évident."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Bienvenue au Conclave."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le Conclave durera trente jours."
    kami "Trente jours exactement."
    kami "Pas un de plus."
    kami "Pas un de moins."
    kami "Et pendant ces trente jours, vous ne retournerez pas chez vous."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Trente jours pendant lesquels vous allez décider."
    kami "Pas pour vous."
    kami "Pour tous les autres…"

    pause 0.4

    $ bc_show("elen", "inquiet", px=-70, py=-50, pz=0.85)
    elen desaccord "Décider de quoi exactement ?"
    elen desaccord "Attends, explique-moi encore, je suis larguée là."

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Des règles."
    kami "Celles qui encadrent ce monde."
    kami "Celles que vous respectez déjà, chaque jour."
    kami "Le bien et le mal, en somme."

    pause 0.4

    kami "Aujourd'hui, au cours de cette première journée…"
    kami "Chacun de vous proposera une modification."
    kami "Un amendement."
    kami "Un seul."
    kami "Sur le commandement de votre choix."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous pourrez renforcer une règle."
    kami "L'adoucir."
    kami "La tordre."
    kami "Ou l'habiller d'un joli mot pour faire croire que c'est une avancée."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vous êtes libres de proposer ce que vous voulez."
    kami "Et personne ne saura jamais qui a proposé quoi."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je vous laisse être créatifs."
    kami "Après tout…"
    kami "C'est ce que vous faites de mieux."

    pause 0.5

    $ bc_show("tomas", "reflechit", px=-80, py=-45, pz=0.85)
    tomas raison "Et ensuite ?"

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Ensuite ?"
    kami "Vous votez."

    kami "Tous les trois jours."
    kami "Un vote."
    kami "Simple."
    kami "Clair."
    kami "Binaire."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Pour."
    kami "Ou contre."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais attention."
    kami "Pour qu'un amendement soit adopté…"
    kami "Il faut l'unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    $ impact(10, 0.25, "#c81e2e")

    kami "Tous."
    kami "Sans exception."
    kami "Sinon, c'est non."

    pause 0.5

    $ bc_show("nyra", "triste", px=-70, py=-55, pz=0.85)
    nyra panne "Et si quelqu'un vote contre… ?"

    $ bc_hide()

    scene bg_diffusion_desespoir at adaptive_fullscreen with dissolve

    kami "Alors l'amendement est rejeté."
    kami "Il disparaît."
    kami "Comme s'il n'avait jamais existé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Un peu comme certaines personnes."
    kami "Dans d'autres circonstances."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous allez apprendre quelque chose d'important."
    kami "Très vite."

    kami "Convaincre est plus difficile que contraindre."
    kami "Et le consensus…"
    kami "Est un luxe que peu de sociétés peuvent se permettre."

    pause 0.6

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Oh."
    kami "Dernière précision."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Je ne participerai pas aux votes."
    kami "Je ne donnerai pas mon avis."
    kami "Je ne prendrai part à aucune de vos manigances."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je regarderai."
    kami "Et j'apprendrai encore de vous."

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Et maintenant, la précision de taille."
    kami "Ici… les Commandements n'ont pas lieu d'être."

    kami "Vous pouvez vous battre."
    kami "Vous pouvez mentir."
    kami "Vous pouvez voler."
    kami "Vous pouvez vous entretuer."
    kami "Je ne m'en mêlerai pas."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Mais n'oubliez pas."
    kami "Tout ce que vous faites est filmé."
    kami "Et diffusé."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "J'ai passé un an à vous observer."
    kami "Vos débats."
    kami "Vos justifications."
    kami "Vos excuses."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ce serait dommage de s'arrêter maintenant."

    pause 0.6

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Le Conclave commence."
    kami "Les portes sont ouvertes."
    kami "Visitez les lieux."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Faites connaissance."
    kami "Ou faites… autrement."

    pause 0.5

    # --------------------------------------------------------------------------
    # 2m10 — Total : ~26m40
    # --------------------------------------------------------------------------

    $ bc_off()
    play music "music/bgm_quiet_routine.mp3" fadein 0.4
    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade

    "L'écran s'éteint."
    "Et pendant une seconde, personne ne respire."

    "Puis tout le monde se met à parler en même temps."
    "Des chuchotements qui deviennent vite des phrases entières."
    "Des rires nerveux."
    "Des insultes à demi avalées."

    $ showGroup([
        ("noam", "reflexion", -0.09),
        ("lysa", "blase", 0.05),
        ("tomas", "reflechit", 0.19),
        ("nyra", "triste", 0.33),
        ("elen", "inquiet", 0.47),
        ("mara", "rire", 0.61),
        ("ryn", "colere", 0.75),
        ("julian", "rire", 0.89),
        ("kael", "neutre", 1.03),
    ])

    noam reflexion "On va devoir vraiment passer trente jours ici…"

    lysa blase "L'unanimité ?"
    lysa blase "C'est le piège ultime."
    lysa blase "En vrai, c'est quasi impossible."
    lysa blase "Soit tu convaincs tout le monde…"
    lysa blase "soit tu les écrases."
    lysa fatigue "Maintenant je pige pourquoi elle dit que ce sera pas simple."

    tomas raison "Ou alors… faire des compromis."
    tomas raison "Pour une fois."

    "Je tourne la tête."
    "Sur les autres sièges, ça débat déjà comme si ça faisait une heure."

    menu:
        "Où Noam pose-t-il son regard ?"

        "Suivre Lysa du regard":
            $ j1_noam_prudence += 1
            "Lysa regarde les caméras avant de regarder les gens."
            think "Elle cherche les angles morts. S'il y en a."

        "Regarder l'écran central":
            $ j1_noam_curiosity += 1
            "Je garde les yeux sur l'écran central."
            think "Même éteint, il donne l'impression de pouvoir reprendre la parole à tout moment."



    nyra triste "Moi… je vois quand même un truc positif."
    nyra triste "Si on peut modifier les règles…"
    nyra triste "Ça veut dire qu'on peut améliorer les choses."

    lysa blase "Ou les empirer."
    lysa blase "Les rendre 'légales', surtout."



    elen inquiet "Le fait qu'on ait le droit de proposer des amendements…"
    elen inquiet "Franchement, dans ce merdier, c'est déjà énorme."
    elen inquiet "C'est comme… une toute petite fenêtre ouverte. Ça fait du bien de respirer cinq secondes."

    lysa blase "Une respiration sous l'eau."

    "Un rire s'échappe quelque part."
    "Un rire trop franc, trop sûr de lui."



    mara rire "Vous parlez tous comme si on venait de gagner au loto."
    mara rire "On est dans une putain de cage, les gars."
    mara rire "Avec un bouton 'vote' et un nœud rose dessus pour faire genre que c'est cadeau."

    lysa colere "Merci pour le rappel."



    ryn colere "Non mais attendez."
    ryn colere "Elle a dit quoi exactement ?"
    ryn colere "Ici, les commandements s'appliquent pas."

    ryn colere "Donc si quelqu'un pète un câble…"
    ryn colere "On fait quoi ?"

    lysa neutre "On est filmés en permanence."
    lysa neutre "IA qui mate et diffuse tout."
    lysa blase "Son idée du 'cadre sécurisé', apparemment."
    lysa blase "La pression, ça empêche de péter un câble."
    lysa fatigue "... En théorie."

    "À côté, quelqu'un se lève, ajuste sa veste comme s'il montait sur scène."
    "Il cherche du regard une caméra. Il la trouve."
    "Et il lui offre un sourire travaillé."



    julian rire "Franchement ?"
    julian rire "Moi je trouve ça carrément bandant."

    julian neutre "Enfin !"
    julian neutre "Un endroit où on peut vraiment parler, peser sur les règles…"
    julian neutre "… et où les gens vont regarder. Pour de vrai."

    "Il se tourne légèrement. Comme pour se mettre de profil face à la caméra."
    "Comme si ça avait de l'importance."

    lysa colere "T'es sérieux ?"

    julian idee "Totalement."
    julian idee "Si je dois être coincé ici trente jours… autant que ce soit légendaire."
    julian idee "Et autant en profiter pour rendre la vie un peu moins pourrie aux autres, non ?"

    "Il jette un regard rapide vers une caméra."
    "Il lève deux doigts en signe de salut."
    "Comme si quelqu'un l'attendait de l'autre côté."

    noam inquiet "…"



    tomas reflechit "Au moins, ça confirme quelque chose."
    tomas reflechit "Elle veut du spectacle. Vraiment."
    tomas raison "Et si elle veut du spectacle… c'est qu'elle compte sur le fait qu'on va se déchirer entre nous."

    pause 0.4

    "Un autre détail me revient."
    "Le jour 1, chacun propose un amendement."

    noam reflexion "Donc aujourd'hui… on doit tous proposer quelque chose."

    lysa culpabilite "Ouais."
    lysa culpabilite "Et personne saura qui a proposé quoi."

    kael neutre "Et si on se disait chacun ce qu'on envisage comme modifications ?"
    kael neutre "Pas besoin de tout écrire d'un coup. Juste… l'idée générale."
    kael neutre "Si on les met sur la table ensemble, on a peut-être une chance d'atteindre l'unanimité."
    kael neutre "Sinon, on va tourner en rond."

    "Un silence retombe, plus sec."
    "Cette fois, c'est pas la peur."
    "C'est le calcul."




    elen inquiet "On devrait peut-être se caler sur un truc simple avant que ça parte en vrille."
    elen inquiet "Genre une règle de base, pas grand-chose… juste pour pas s'étriper dans les dix premières minutes."
    elen inquiet "Parce que sinon je te jure, ça va dégénérer direct."

    lysa blase "Tu veux une méthode ?"
    lysa blase "On est douze, enfermés, filmés."
    lysa blase "Et ici, tuer quelqu'un… pas de conséquence."
    lysa fatigue "La méthode est déjà écrite."
    lysa fatigue "... Et on la connaît tous."
    lysa peur "Évidemment que ça va finir en tuerie de masse."

    pause 0.4

    "Je vois des petits groupes se former."
    "Deux par-ci."
    "Trois par-là."
    "Des regards en biais."
    "Des gens qui s'éloignent déjà, comme s'ils avaient peur d'être associés."

    noam reflexion "On fait quoi, nous ?"

    lysa neutre "On visite."
    lysa neutre "On repère les lieux."
    lysa neutre "Et on ferme sa gueule devant les caméras."
    lysa fatigue "Surtout au début."

    elen reflexion "Je vais checker s'il y a une infirmerie… ou au moins de quoi faire un pansement."
    elen reflexion "On sait jamais, des fois que quelqu'un se fasse vraiment mal."

    noam neutre "Ok."

    pause 0.4

    "Tout le monde quitte peu à peu la pièce."

    "Et moi…"
    "Je devrais aller faire un tour également."

    pause 0.6

    think "Phase exploration."
    think "Ça commence maintenant."
    $ hideGroup()

    scene bg_map at adaptive_fullscreen with fade

    tuto "Prêt pour un nouveau tutoriel ?"
    tuto "J'espère bien !"
    tuto "Cette carte correspond à la carte du Conclave."
    tuto "Toutes les pièces vous sont ouvertes afin que vous puissiez explorer chacune d'entre elles convenablement."
    tuto "Pour accéder à une salle spécifique, rien de plus simple : il suffit de cliquer dessus."
    tuto "Dans certaines pièces, certaines interactions peuvent être cruciales pour débloquer des fins différentes."
    tuto "Cette mécanique complète la mécanique de choix afin d'ouvrir les possibles."
    tuto "N'hésitez donc pas à explorer et à interagir avec votre environnement."
    tuto "Bonne exploration !"

    jump OPEN_CONCLAVE_MAP

    # --------------------------------------------------------------------------
    # 2m10 — Total : ~28m50
    # --------------------------------------------------------------------------

label CHECK_ALL_SALLES_VISITEES:

    if (
        decouverte_salle_archive
        and decouverte_cafeteria
        and decouverte_salle_canon
        and decouverte_gymnase
        and decouverte_infirmerie
        and decouverte_salle_maintenance
        and decouverte_salle_observation
        and decouverte_salle_repos
        and decouverte_sas
        and decouverte_stockage
    ):
        jump KAMI_MESSAGE_APRES_VISITE

    return

label KAMI_MESSAGE_APRES_VISITE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "J'avais fini par oublier l'heure."
    think "Ici, le temps a une façon de te faire croire qu'il s'est arrêté."
    think "Et puis non."
    think "Il avance. Lentement, mais il ne recule jamais."

    "Un écran mural grésille."
    "Un second s'allume plus loin."
    "Puis un troisième."
    "Même signal, partout, identique."

    play sound sfx_beep
    "-Bip-"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il est bientôt dix-huit heures."
    kami "Votre visite libre touche à sa fin."

    kami "J'espère que vous avez trouvé ça…"
    kami "inspirant et complet."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "On a mis du cœur à l'ouvrage."
    kami "Enfin."
    kami "On a surtout mis des ingénieurs passionnés."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous êtes tous convoqués."
    kami "Direction la salle du Conclave."
    kami "Tout de suite."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Hop hop."
    kami "Je suis déjà installée."
    kami "Popcorn virtuel en main."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ne me faites pas perdre mon temps."
    kami "C'est le seul truc que je ne vous pardonnerai pas."

    play sound sfx_beep
    "-Bip-"

    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Voilà, on y arrive."
    think "À partir de là, le Conclave débute vraiment."
    think "Ce n'est plus possible de faire marche arrière."
    think "Enfin, ça n'a jamais été possible, mais bon…"

    scene bg_conclave at adaptive_fullscreen with fade

    "Les portes du Conclave s'ouvrent ; dedans, il y a déjà plusieurs personnes."
    "On évite tous de se regarder, comme si on était gênés de quelque chose."
    "Personne n'a envie d'être le premier à parler."

    "La salle du Conclave n'a pas changé depuis tout à l'heure."
    "Toujours trop propre."
    "Toujours trop grande."
    "Et on est toujours insignifiants dans ce monde gigantesque."

    "Je m'assois et ceux déjà présents m'imitent."
    "Les autres arrivent par grappes."
    "Des fauteuils raclent."
    "Mais personne ne parle. On attend."

    $ showGroup([
        ("ryn", "fatigue", 0.02),
        ("mara", "rire", 0.25),
        ("iris", "fatigue", 0.50),
        ("julian", "sourire", 0.75),
        ("elen", "inquiet", 0.98),
    ])

    ryn fatigue "On est tous là ?"
    ryn fatigue "Me dites pas qu'on va encore attendre pour rien."


    mara rire "Chuuut."
    mara rire "T'as capté ou quoi ?"
    mara rire "Kami supporte pas qu'on lui fasse perdre son temps, soi-disant."
    mara rire "Et moi j'ai pas envie d'être sa cible du jour, alors merci, mais tais-toi."


    iris fatigue "Super. Vraiment super."
    iris fatigue "On nous convoque comme des mômes de primaire qui ont sali la classe. Génial, l'ambiance."
    iris fatigue "J'ai hâte de voir qui va nous mettre au coin cette fois."


    julian sourire "Perso je trouve ça hyper marrant."
    julian sourire "J'ai trop envie de voir jusqu'où on peut pousser le bordel dans cet endroit…"


    elen inquiet "Franchement, je suis pas sûre qu'on puisse changer grand-chose…"
    elen inquiet "Kami décide de qui vit ou meurt, on va pas se mentir."
    elen inquiet "Mais même si c'est minuscule… j'ai envie d'essayer quand même. Ça coûte rien d'essayer, si ?"


    julian taquin "Je sais, je sais..."
    julian taquin "Mais justement, c'est ça qui est excitant."
    julian taquin "Si on peut réécrire les règles, on peut tout changer."
    julian taquin "Et sortir tout le monde de là. On pourrait être les héros de l'humanité !"

    "L'écran central s'allume."
    "Un halo blanc."
    "Et Kami apparaît."
    $ hideGroup()

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Bonjour. Je vois que vous êtes tous arrivés."
    kami "Mes douze représentants."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oh que ça faisait longtemps que j'en rêvais, de ce Conclave !"
    kami "C'était un travail monstre de tout organiser !"
    kami "Mais je pense que ça peut valoir le coup !"

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais revenons à nos moutons."
    kami "Je vais être claire."
    kami "Ici, dans le Conclave…"
    kami "les Commandements sont suspendus, abolis."
    kami "Toutes les règles que vous connaissiez jusque-là n'ont plus lieu d'être."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous êtes libres d'avoir la liberté absolue !"
    kami "Pas de commandement, pas de loi, pas de police."
    kami "Juste vous."

    "Un frisson traverse la salle."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui."
    kami "Je vois que certains d'entre vous arborent déjà des sourires."
    kami "Mais..."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ne vous enflammez pas."
    kami "Ça ne veut pas dire que vous pouvez tout faire."
    kami "Je me permets juste cet aménagement pour pouvoir vous observer sans bruit de fond."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Donc."
    kami "Il n'y a plus de Commandements ici."
    kami "Mais il reste certaines règles."
    kami "Celles du Conclave."

    kami "Règle une."
    kami "Interdiction de retourner dans votre district."
    kami "Interdiction d'aller dans un autre."
    kami "Jusqu'à la fin du trentième jour."

    pause 0.2

    kami "Vous restez ici."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Pendant trente petits jours, nous allons nous amuser ensemble."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Règle deux."
    kami "Interdiction d'initier un contact vers l'extérieur."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Alors que je ne vous vois pas tripoter le matériel de communication."
    kami "Si jamais quelqu'un vous appelle, vous pouvez répondre."
    kami "Mais pas l'inverse."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Vous savez combien ça coûte les appels depuis l'espace ?!"
    kami "Non franchement, ne jouez pas aux idiots."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Règle trois."
    kami "Vous êtes constamment filmés."

    "Personne ne commente."
    "On le sait."
    "On le sait trop bien."
    "C'est peut-être la seule chose qui ne changera pas dans notre quotidien."

    kami "Mais il y a une exception."

    "Tout le monde écoute plus attentivement."

    kami "Vos chambres sont équipées d'un brouilleur."
    kami "Il est activé par défaut."
    kami "Caméras, audio, capteurs : tout est coupé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Mais vous pouvez le désactiver."
    kami "Si vous aimez être vus, par exemple."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Maintenant."
    kami "On peut passer au cœur du Conclave."

    kami "Vous allez déposer chacun un amendement."
    kami "Une modification d'un Commandement."
    kami "Dans une urne."

    kami "Vous avez trente-cinq minutes pour chacun en déposer un."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui, c'est presque comme un examen surprise."
    kami "J'adore."
    kami "J'espère que vous avez de l'inspiration."

    scene bg_diffusion_gene at adaptive_fullscreen with dissolve

    kami "Allez, je veux savoir ce que vous voulez changer dans mes règles parfaites !"
    kami "Qu'est-ce que j'aurais pu mal faire ?"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il y aura dix votes."
    kami "Dix amendements tirés au sort."
    kami "Pas un de plus."

    kami "Vous êtes douze."
    kami "Donc deux amendements ne seront pas votés lors de ce Conclave."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ne le prenez pas mal."
    kami "C'est mathématique."
    kami "Et ce n'est pas plus mal, si jamais je devais reproduire le Conclave l'an prochain."
    kami "Je pourrais peut-être ajouter les amendements restants dans la prochaine urne !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Tous les trois jours."
    kami "Un amendement sera tiré au sort."
    kami "Puis tous les trois jours, vous voterez sur cet amendement. Votre objectif : l'unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Une seule voix contre."
    kami "Et l'amendement est refusé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "La participation aux votes est libre. Libre à vous de venir voter, ou pas."
    kami "Sur les bulletins exprimés, il faut une unanimité de POUR pour adopter le vote."
    kami "Sont retirés des bulletins exprimés les abstentions et les absences au vote."

    kami "Je ne suis pas un monstre, tout de même."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Mais je vous préviens, le peuple n'apprécie généralement pas les PROCRASTINATEURS."

    show screen kami_broadcast_ui
    $ bc_show("elias", "reflechit", px=-70, py=-50, pz=0.85)

    elias neutre "Donc si une seule personne dit non… c'est mort."
    elias neutre "C'est une sorte de système de blocage."

    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Pour chaque proposition d'amendement adoptée, j'initierai immédiatement le changement."
    kami "Pour certains, un refus de l'amendement pourra aussi avoir des conséquences."
    kami "Mais ça dépendra de vos douces propositions."

    $ unlock_codex_page("reglement_conclave", with_notification=False)
    show screen day1_codex_unlock_panel("Règlement du Conclave")
    pause 2.0
    hide screen day1_codex_unlock_panel

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Sur ce."
    kami "Écrivez."
    kami "Réfléchissez."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Faites semblant d'être des adultes responsables."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "L'urne ferme dans trente-et-une minutes."
    kami "Ne déposez pas vos propositions en retard."

    play sound sfx_beep
    "-Bip-"
    jump _1_CONCLAVE_DEBAT_DEPOT

# Durée : 3m30 — Total : ~56m15


# =============================================================================
label _1_CONCLAVE_DEBAT_DEPOT:
# =============================================================================

    scene bg_conclave at adaptive_fullscreen
    play music "music/bgm_system_override.mp3" fadein 1.0

    # --- Timer synchronisé avec le système day0 ---
    $ day0_timer_init(m=31, s=0)
    show screen day1_amendment_timer

    think "Trente-et-une minutes seulement."
    think "Pour faire des propositions qui peuvent réduire des villes en cendre."

    "L'urne est là, au centre de la pièce."
    "Bien visible, bien mise en avant."

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    kael calme "Bon."
    kael calme "Je vais être direct."
    kael calme "Si chacun écrit de son côté, sans rien partager avant…"
    kael calme "… on prend un risque énorme."
    kael calme "Je propose quelque chose de simple."
    kael calme "Chacun dit à voix haute ce qu'il compte mettre en avant."
    kael calme "Pas le texte mot pour mot. Juste l'intention."
    kael calme "Comme ça, on voit tout de suite où ça coince."
    kael calme "Et on évite… les catastrophes."

    pause 0.3


    iris fatigue "Non mais non !"
    iris fatigue "C'est déjà l'horreur ton truc, là, tu te rends compte ou pas ?!"


    kael neutre "Pourquoi ça ?"


    iris desaccord "Attends, parce que si un amendement a l'air tout gentil, tout raisonnable…"
    iris desaccord "…mais qu'en vrai il fout un merdier monstrueux derrière…"
    iris desaccord "Tu crois vraiment que Kami va faire quoi ?"
    iris taquin "'Oups, désolée' ?"
    iris colere "Ou 'ah bah c'est la faute de celui qui l'a écrit' ? Genre, super la logique !"


    sael determine "Elle pointera quelqu'un."
    sael determine "Toujours."
    sael determine "Et ce quelqu'un sera l'un d'entre nous."

    sael determine "Même si elle ne le dit pas clairement."
    sael determine "Même si c'est jamais écrit."

    sael determine "On en assumera les conséquences."


    elen inquiet "Et puis… y en a qui ont clairement pas envie d'en causer."
    elen inquiet "Y a des trucs qu'on garde pour soi, des idées un peu tordues…"
    elen inquiet "Bref, c'est pas parce qu'on est tous là qu'on va tout se dire cash."


    julian sourire "Moi je veux bien en parler, hein."
    julian sourire "Mais bon… je sens que je vais encore me faire passer pour le relou qui se la raconte."


    mara neutre "C'est pas un risque, c'est ta marque de fabrique."
    mara neutre "Au fait… c'est quoi ton blaze déjà ?"

    "Personne ne lui répond vraiment."

    pause 0.3


    ryn reflechit "Et si on faisait rien ?"

    ryn reflechit "On vote contre tout."
    ryn reflechit "On touche à rien."
    ryn reflechit "Fin de l'histoire."
    ryn reflechit "Comme ça on ne change pas les habitudes, et tout le monde connaît les règles ?"


    nyra triste "Ça veut dire accepter."
    nyra triste "Que ce monde reste comme il est."

    nyra triste "On va pas faire semblant que tout va bien, non ?"
    nyra triste "Y'a pas que du mauvais, mais y'a aussi des choses à changer."


    tomas hesitation "Non. Ça ne marchera pas, Ryn."
    tomas hesitation "Kami a dit… très clairement… que refuser un amendement pouvait aussi avoir des conséquences."
    tomas hesitation "On sait juste pas encore lequel. Et c'est ça qui m'inquiète."

    pause 0.3


    kael reflechit "C'est précisément pour ça qu'il faut en parler."
    kael reflechit "Le silence."
    kael reflechit "C'est exactement ce qu'ils veulent."
    kael reflechit "Le laisser s'installer, c'est leur donner le champ libre."


    lysa reflexion "Ou alors…"
    lysa reflexion "c'est notre seule défense."
    lysa doute "Quelqu'un peut très bien mentir."
    lysa doute "Dire qu'il propose un truc alors qu'il en propose un autre."
    lysa blase "Avec seulement dix votes tirés au sort…"
    lysa blase "c'est l'alibi parfait."
    lysa fatigue "Personne ne pourra prouver le contraire."

    pause 0.4

    "Le silence retombe."
    "Pas un silence lourd."
    "Un silence méfiant."

    lysa fatigue "Comme il n'y a que dix votes… c'est l'alibi idéal pour justifier son mensonge."


    # --- Le chrono passe à 20 min (mise à jour dynamique) ---
    $ day0_timer_set(20 * 60)

    elias reflechit "Au fait les gars..."
    elias reflechit "Pendant qu'on tourne en rond, il ne reste plus que vingt minutes."

    pause 0.4


    ryn fatigue "Écoutez, faites ce que vous voulez."

    "Ryn se lève."

    "Il attrape une feuille de papier puis un stylo."
    "Sans aucune justification ni aucune parole."


    play sound sfx_paper
    "Un froissement."
    "Puis le bruit sec du papier qui tombe au fond d'une boîte."
    play sound sfx_drop

    think "Voilà."
    think "Le premier."


    nyra reflexion "C'est allé vite…"


    mara sourire "Dès qu'un con commence…"
    mara sourire "Tous les autres moutons suivent. Les gens sont vraiment des moutons."

    pause 0.3

    "Une chaise recule."
    "Puis une autre."


    sael neutre "On peut en discuter pendant des heures."
    sael neutre "Mais au final."
    sael neutre "Chacun va écrire ce qu'il croit être juste."

    sael neutre "Sauf que la justice, c'est une notion très personnelle."


    play sound sfx_drop
    "Un second papier tombe."
    "Puis un troisième."

    think "Plus personne ne débat vraiment."

    "On est encore quelques-uns debout."
    "On a les yeux baissés. On n'ose plus se regarder."


    kael calme "Bon…"
    kael calme "C'est donc votre choix."
    kael calme "Je le note."

    "Puis Kael s'éloigne à son tour."


    julian neutre "C'est dingue, non ?"
    julian neutre "C'est toujours quand tout le monde se tait…"
    julian neutre "… que les vraies décisions se prennent."


    "L'urne se remplit."
    play sound sfx_paper
    "Lentement."
    play sound sfx_paper
    "Inexorablement."
    play sound sfx_drop

    think "C'est ça le Conclave."
    think "Pas un débat."
    think "Un enchaînement."


    elen inquiet "Et si jamais quelqu'un balance un truc vraiment hardcore ?"
    elen inquiet "Genre une proposition qui fait flipper tout le monde…"


    iris fatigue "Donc voilà : soit on vote contre, et rien ne change, sauf que même ça ça craint..."
    iris fatigue "soit on se tape les conséquences dans la tronche."
    iris fatigue "Comme d'hab', quoi. Rien de neuf sous le soleil pourri."

    pause 0.4

    play sound sfx_paper
    "Plusieurs personnes sont debout."
    "D'autres écrivent encore."

    play sound sfx_drop
    "L'urne est presque entièrement remplie."
    "Le temps passe."
    "Il faut que je m'y mette moi aussi."

    # --- Timer à 4 minutes ---
    $ day0_timer_set(4 * 60)
    $ hideGroup()
    jump _1_proposition_amendement

    return

# Durée du label : 2m — Total : ~58m15

# =============================================================================

label _1_proposition_amendement:
# =============================================================================

    scene bg_cg009 at adaptive_fullscreen
    $ unlock_gallery_image("bg_cg009")
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    think "Ok."
    think "C'est à moi."

    "Le bruit des papiers qui tombent dans l'urne continue."
    "Pas fort."
    "Mais assez pour te rappeler que tu traînes."

    "Sur ma table, j'ai pris une feuille."
    "Un stylo."
    "Et il y a toujours ce vide au milieu de la poitrine."

    think "On dirait un examen."
    think "Sauf qu'ici…"
    think "si tu rates."
    think "Les conséquences peuvent être terribles."

    "Je fais tourner le stylo entre mes doigts."
    "Je le lâche."
    "Je le reprends."
    "Je sais que je suis assez ridicule comme ça."

    think "Respire, Noam."
    think "Fais pas semblant."
    think "T'as peur. Ok."
    think "C'est normal. Enfin, je crois que ça l'est."

    "Je baisse les yeux sur l'urne."
    "Elle est toujours là."
    "Comme si elle me regardait, comme si elle attendait."

    think "Il faut que je trouve quelque chose."

    "Je gratte un mot sur le papier."
    "Je le raye aussitôt."

    think "Il faut quelque chose qui puisse être utile."
    think "Quelque chose qui fait que les gens vivront mieux."
    think "Facile à dire. Difficile à trouver."

    pause 0.3

    "Une chaise grince derrière moi."
    "Quelqu'un passe."
    "Je n'ose même pas relever la tête."

    think "Ils écrivent tous."
    think "Comme si c'était simple."
    think "Comme si c'était… normal."

    "Je pose la pointe du stylo."
    "Et je reste bloqué."

    think "Ok."
    think "Il faut que je sois honnête avec moi-même."
    think "J'hésite."

    pause 0.2

    think "Deux idées."
    think "Deux trucs très concrets."
    think "Deux propositions pour tenter de faire changer les choses."

    think "La première…"
    think "C'est l'information."

    think "Pas le monde."
    think "Pas les districts."
    think "Pas les grandes annonces."
    think "Mais celles du quotidien."

    think "Dire ce que je vois."
    think "Ce que je vis, ce que je ressens."

    think "Arrêter de faire semblant que parler de la pluie, du froid ou d'un problème local…"
    think "c'est une menace pour l'équilibre du monde."
    think "Actuellement ce n'est pas clair."

    "Le cinquième commandement dit que :"
    "La diffusion d'informations non validées par ARCHIVE est interdite."
    "Mais qu'est-ce qui est validé ?"
    "Personne ne le sait vraiment."
    "Donc tout le monde évite de parler."

    pause 0.2

    think "La deuxième…"
    think "C'est le fait d'aider."
    think "Aujourd'hui, plus personne n'aide grand monde."
    think "On a peur de faire quoi que ce soit qui ne serait pas conforme aux Commandements."

    think "Le fait d'aider quelqu'un ne devrait pas être pénalisable."
    think "Quand quelqu'un est dans la merde."
    think "Quand on peut."
    think "Alors il faudrait permettre le fait d'aider."

    pause 0.3

    think "Les deux propositions me semblent raisonnables."
    think "Laquelle choisir ?"
    think "Je ne vois pas ce qu'il y aurait de mal à proposer ça."

    think "À moins que je ne fasse fausse route ?"

    think "Et évidemment…"
    think "C'est à moi de décider."

    pause 0.3

    "Je ferme les yeux une seconde."
    "Le bruit de l'urne continue."
    "Moins régulier."
    "Plus pressant."

    "Je souffle lentement."
    "Je redresse un peu le dos."

    think "Ok."
    think "Arrête de tourner autour du pot."
    think "Il faut choisir."

    # --- Tutoriel amendement ---
    show screen day1_tuto_amendment
    pause

    call screen day1_amendment_form()
    $ noam_amendement_choix = _return
    $ j1_amendment_validated = True

    if noam_amendement_choix == "information_locale":
        $ j1_noam_mediation += 1

        think "D'accord."
        think "Il faut libérer la parole."
        think "Mais pas n'importe comment."

        "J'écris une phrase."
        "Puis je m'arrête."
        "Je me relis."

        think "Je précise un mot qui me semble mal tourné, peu précis."
        think "Il ne faut pas tout changer, mais permettre une plus grande liberté est important."
        think "Ce qui touche aux districts et à la politique."
        think "Ça peut rester verrouillé."

        think "Mais le reste…"
        think "Le quotidien."
        think "Le local."
        think "L'immédiat, ce qu'on voit, ce qu'on dit, ce qu'on ressent."

        think "On devrait pouvoir le formuler comme on le souhaite."
        think "Sans risquer sa vie, du moins."

        "Je reformule."
        "Encore."
        "J'enlève un mot."
        "J'en ajoute un autre."

    if noam_amendement_choix == "assistance_minimale":
        $ j1_noam_initiative += 1

        think "Ok."
        think "Je vais essayer de permettre l'entraide."

        "J'écris un premier jet."
        "Ma main hésite."

        think "Il faut que la formulation ne soit pas un truc impossible."
        think "Juste…"
        think "qu'on puisse faire quelque chose quand on le peut."

        think "Aider."
        think "Prévenir."
        think "Intervenir."

        think "Parce que laisser quelqu'un tomber…"
        think "Ça aussi, c'est une décision."
        think "Une mauvaise décision."

        "Je fais attention à chaque formulation."

    pause 0.3

    "Quand j'ai fini d'écrire, ma main tremble un peu."
    "Pas assez pour lâcher le stylo."
    "Juste assez pour que je remarque la tension qui fait vibrer mes doigts."

    think "Voilà."
    think "C'est fait."

    "Je relis une dernière fois."
    "J'ai envie de corriger."
    "De nuancer."
    "De préciser encore."

    think "Non."
    think "Sinon je recommencerai encore et encore."

    "Je jette un coup d'œil aux écrans."
    "Il ne reste plus que quatre minutes."

    think "Ça fait déjà si longtemps que ça ?"

    pause 0.2

    "Je plie la feuille."
    "Ce n'est pas très droit, c'est assez irrégulier."

    "Je me lève."
    "La chaise fait trop de bruit."
    "Ou alors c'est le fait que personne ne fait un bruit."

    think "Je sens le regard des caméras."
    think "Même sans forcément les voir."

    "Je marche jusqu'à l'urne."
    "Chaque pas est un peu trop long."
    "J'ai la gorge sèche."

    think "Et si j'avais fait le mauvais choix ?"
    think "Non. Arrête d'y penser."

    call day1_play_trace(path_type="vertical_up", time_limit=6.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_day1_trace_urn

    play sound sfx_paper
    "Je pousse la feuille dans la fente."
    play sound sfx_drop
    $ impact(8, 0.2, "#3BCC82")
    "Elle tombe au fond."
    $ j1_amendment_deposited = True
    call screen day1_urn_confirmation()
    "Je ne peux plus la récupérer."
    "Trop tard pour les regrets."

    pause 0.4

    think "Voilà."
    think "Mon premier amendement."

    "Je recule."
    "Je retourne à ma place."
    "J'étais le dernier."

    scene bg_conclave at adaptive_fullscreen with dissolve

    jump _1_AMENDEMENT_DEPOSE

# Durée : 3m — Total : ~1h 0m 15s


# =============================================================================
label _1_AMENDEMENT_DEPOSE:
# =============================================================================

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    $ day0_timer_active = False
    hide screen day1_amendment_timer

    "Un léger grésillement."
    "Les écrans muraux s'allument presque en même temps."

    play sound sfx_beep
    "-Bip-"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Dix-huit heures précises."

    kami "Le temps imparti pour le dépôt des amendements est désormais écoulé."

    pause 0.2

    kami "Je suis ravie."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vraiment."
    kami "Vous avez tous participé."
    kami "Dans les temps."
    kami "Sans exception."

    pause 0.2

    kami "C'est rare."
    kami "Et très appréciable."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Grâce à vous, je n'aurai pas besoin d'éliminer qui que ce soit aujourd'hui."

    "Personne ne réagit."
    "Mais l'air semble se détendre d'un cran."
    "D'un cran seulement."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Les dix amendements soumis au vote seront tirés au sort."

    kami "Le tirage sera diffusé demain matin."
    kami "À neuf heures."
    kami "Sur l'ensemble des écrans."

    pause 0.2

    kami "Je vous conseille d'être attentifs."
    kami "Le hasard a parfois beaucoup de goût."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "En attendant."

    kami "L'accès aux chambres est désormais ouvert."
    kami "Vous êtes libres de circuler."
    kami "De manger."
    kami "De vous reposer."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Profitez-en."
    kami "Demain, on recommencera à jouer tous ensemble."

    play sound sfx_beep
    "-Bip-"

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Les écrans s'éteignent."
    "Un par un."
    "Puis le silence retombe."

    pause 0.3

    "Personne ne parle tout de suite."
    "Comme si on attendait encore quelque chose."
    "Ou quelqu'un. Mais rien ne vient."

    "Puis les chaises raclent le sol."
    "Des pas."
    "Des soupirs."

    "Les représentants commencent à se disperser."
    "Sans vraiment se regarder."
    "Sans se dire au revoir."

    think "C'est fini."
    think "Pour aujourd'hui du moins."

    scene bg_couloir at adaptive_fullscreen with fade

    "Le couloir est éclairé."
    "Il est plus calme."
    "Presque normal."

    think "J'ai déposé un amendement."
    think "On en a tous déposé un."
    think "J'espère ne pas avoir fait une connerie."

    think "Demain matin à neuf heures."

    pause 0.3

    "Je m'arrête un instant."
    "Debout, au milieu du couloir."

    think "Je n'ai pas vraiment envie de réfléchir."
    think "Mais j'ai pas envie de rester seul avec ça en tête non plus."

    $ current_period = "Soir"

    menu:
        "Que devrais-je faire ?"

        "Aller se coucher":
            $ choix_1_soir = "dormir"
            think "J'ai besoin de m'allonger."
            think "Même si je sais que je ne dormirai pas tout de suite."

            think "Juste…"
            think "Me couper un peu du monde et rester au calme."

            jump _1_FIN_JOURNEE_DORTOIR

        "Se rendre à la salle de repos (Optionnel)":
            $ choix_1_soir = "salle_repos"
            think "Je devrais aller à la salle de repos."
            think "Peut-être que quelqu'un y sera."
            think "Ou peut-être pas."

            think "Dans les deux cas…"
            think "ça me fera du bien."

            jump _1_SALLE_DE_REPOS_OPTIONNELLE

# Durée : 1m — Total : ~1h 1m 15s


# =============================================================================
label _1_SALLE_DE_REPOS_OPTIONNELLE:
# =============================================================================

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "La salle de repos est allumée."
    "Pas trop."
    "Il y a cette lumière douce, presque agréable qui pulse du plafond."

    "Il n'y a pas grand monde."
    "Quelques canapés sont occupés."
    "La plupart sont vides."

    think "Je m'attendais à pire."
    think "Ou à plus de silence."

    pause 0.2

    $ showGroup([
        ("julian", "detendu", 0.22),
        ("nyra", "sourire", 0.50),
        ("mara", "sourire", 0.78),
    ])

    julian detendu "Ah."
    julian detendu "Toi aussi t'as pas réussi à te coucher direct ?"

    think "Évidemment."


    nyra sourire "J'avais besoin de…"
    nyra sourire "Je sais pas."
    nyra sourire "Voir autre chose qu'un mur."

    "Julian se laisse tomber dans un fauteuil."
    "Un peu trop fort."

    julian detendu "Franchement..."
    julian detendu "J'ai cru que j'allais rester planté devant ma feuille blanche comme un idiot."
    julian detendu "J'ai écrit une phrase entière, puis je l'ai rayée, trois fois de suite."
    julian detendu "Il fallait vraiment que je trouve quelque chose de bien."

    pause 0.2


    mara sourire "Moi j'ai arrêté de cogiter."
    mara sourire "Sinon je devenais dingue."
    mara sourire "J'ai écrit un truc."
    mara sourire "Point barre."
    mara sourire "Et si ça vous plaît pas, bah tant pis pour vos gueules."

    think "Tant pis."
    think "Facile à dire."

    pause 0.3

    "Quelqu'un rit."
    "Pas fort."
    "Mais assez pour que ça surprenne."

    julian detendu "On est bien d'accord que c'est complètement n'importe quoi ?"
    julian detendu "On réfléchit à ce qui peut aider les gens, on écrit des phrases."
    julian detendu "… et demain matin le hasard décide si ça vaut de l'or ou si ça vaut zéro."
    julian detendu "Imagine si ma proposition ne tombe pas dans les dix tirages !"

    nyra sourire "Oui."
    nyra sourire "Mais au moins…"
    nyra sourire "on a écrit quelque chose."

    pause 0.2

    "Un silence s'installe."
    "Pas gênant."
    "Juste calme."

    think "C'est étrange."
    think "On dirait presque une soirée normale."

    mara sourire "Vous croyez qu'elle nous mate là ? Genre… là, tout de suite ?"

    julian detendu "Sûrement..."
    julian detendu "Et pour tout te dire, j'espère bien !"
    julian detendu "Ah, qu'est-ce que j'aimerais être repéré pour mes talents ici !"

    pause 0.3

    "Personne ne le reprend."
    "Personne ne le contredit."

    think "Ça fait du bien."
    think "De ne pas faire attention pendant deux minutes."

    pause 0.4

    play sound sfx_door
    $ hideGroup()

    scene bg_cg010 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")
    show screen kami_broadcast_ui

    "La porte de la salle de repos s'ouvre."

    "Quelqu'un hésite un instant."
    "Puis il avance."

    tomas hesitation "Euh…"
    tomas hesitation "Bonsoir."

    "Tomas entre."
    "Un plateau entre les mains."
    "Six tasses."
    "Il marche lentement."
    "Beaucoup trop concentré sur son équilibre."

    $ bc_show("julian", "detendu", px=-70, py=-50, pz=0.85)
    julian detendu "…"
    julian detendu "Ok."
    julian detendu "Respect vraiment."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra sourire "Fais pas semblant d'être détendu."
    nyra sourire "On voit très bien que tu stresses."
    $ bc_hide()

    tomas hesitation "Disons que… si je renverse ça sur moi là, maintenant…"
    tomas hesitation "je suis mort socialement pour le reste du mois. Je vais directement me cacher sous une table et on me reverra plus."
    $ bc_show("mara", "content", px=-70, py=-50, pz=0.85)
    mara sourire "Y'a pire."
    mara sourire "Tu pourrais mourir pour de vrai."
    $ bc_hide()

    "Un léger rire passe."
    "Bref, presque timide."

    tomas hesitation "Je me suis dit que…"
    tomas hesitation "…que ça ferait peut-être du bien."
    tomas hesitation "Un truc chaud. Juste… un truc chaud."

    "Il pose enfin le plateau sur la table."
    "Sans rien renverser."

    $ bc_show("julian", "joie", px=-70, py=-50, pz=0.85)
    julian detendu "Putain."
    julian detendu "T'es un vrai héros, mec."
    $ bc_hide()

    pause 0.3

    scene bg_cg010_1 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")
    $ showGroup([
        ("tomas", "vide", 0.02),
        ("julian", "vide", 0.25),
        ("noam", "vide", 0.50),
        ("mara", "vide", 0.75),
        ("nyra", "vide", 0.98),
    ])

    "Les tasses circulent."
    "Les mains se tendent."
    "La vapeur monte doucement."

    think "Ça sent le thé."
    think "Un vrai thé bien fort comme il faut."
    think "Pas un truc synthétique."

    nyra vide "J'avais presque oublié ce que ça faisait."
    nyra vide "Tenir quelque chose de chaud."

    mara vide "Ouais…"
    mara vide "C'est débile mais ça fait du bien."
    mara vide "Un tout petit peu."

    menu:
        "Que fait Noam ?"

        "Prendre une tasse":
            $ j1_noam_initiative += 1
            "Je prends la tasse."
            "Elle me brûle presque les doigts."
            "Mais je la garde quand même."

            think "C'est idiot."
            think "Mais ça m'ancre."

        "Laisser la tasse aux autres":
            $ j1_noam_prudence += 1
            "Je laisse la tasse sur le plateau."
            "Mes mains restent autour du vide."
            think "Ce soir, même un geste simple ressemble à une décision."

    tomas vide "Demain…"
    tomas vide "À neuf heures on saura…"

    julian vide "Ouais."
    julian vide "Demain."

    "Personne n'ajoute rien."
    "Mais tout le monde y pense."

    pause 0.4

    "On boit."
    "En silence."

    think "Je sais pas combien de temps ce calme durera."
    think "Mais là, en ce moment…"
    think "C'est agréable."

    pause 0.4

    "Les tasses se vident."
    "Le plateau n'en garde plus qu'une."
    "Personne ne la prend."

    mara vide "Bon bah voilà."
    mara vide "Je vais aller me pieuter avant de péter un câble."

    nyra vide "Moi aussi."
    nyra vide "Avant que je recommence à réfléchir."

    julian vide "Excellente idée."

    "Ils se lèvent."
    "Un à un."

    think "La parenthèse se referme."

    pause 0.3

    "Je reste encore quelques secondes."
    "Assis."
    "La tasse vide entre les mains."

    think "Je devrais y aller aussi."

    $ hideGroup()
    jump _1_FIN_JOURNEE_DORTOIR

# Durée : 1m55 — Total : ~1h 3m 10s


# =============================================================================

label _1_FIN_JOURNEE_DORTOIR:
# =============================================================================

    scene bg_couloir at adaptive_fullscreen
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le couloir est plus calme."
    "Pas vide."
    "Mais plus lent."

    "Les pas résonnent différemment."
    "Comme si le bâtiment lui-même soufflait un peu."

    think "Ça y est."
    think "La journée est finie."
    think "Enfin… presque."

    "Je marche sans me presser."
    "Je laisse les pensées glisser."
    "Sans vraiment m'y accrocher."

    pause 0.3

    scene bg_dortoir at adaptive_fullscreen with fade

    "Le dortoir est allumé."
    "Une lumière plus chaude."
    "Moins clinique."

    "Quelqu'un est déjà là."

    $ showGroup([
        ("elias", "detendu", 0.22),
        ("noam", "neutre", 0.78),
    ])

    if choix_1_soir == "salle_repos":

        elias detendu "Ah. Toi aussi t'es encore debout."

        think "Elias."


        noam neutre "Ouais."
        noam neutre "J'avais pas trop envie de rester seul."

        elias detendu "Je vois."
        elias detendu "La salle de repos, hein ? … Pas con."

        noam neutre "Ouais."

        elias detendu "Bonne idée."

        elias detendu "Moi j'ai tenté de dormir direct."
        elias detendu "Raté."

    if choix_1_soir == "dormir":

        elias detendu "En voilà un qui se couche tôt."
        elias detendu "Laisse-moi deviner, envie de rester seul ?"


        noam neutre "On peut dire ça."
        noam neutre "Drôle de journée."

    pause 0.2

    "Il sourit."
    "Un vrai sourire."
    "Un peu fatigué."

    elias detendu "C'est chelou quand même."
    elias detendu "Journée à rallonge, stress au max…"
    elias detendu "… et je suis rincé comme après douze heures sur un chantier."

    noam neutre "Ouais."
    noam neutre "Comme après un déménagement."
    noam neutre "Ou un examen."

    elias detendu "Exactement. C'est l'idée."

    pause 0.3


    elias inquiet "Demain matin…"
    elias inquiet "Ça va être un autre calibre."

    noam neutre "Ouais."


    "On n'insiste pas."
    "Pas besoin."

    elias jaloux "Bonne nuit, Noam."

    noam neutre "Bonne nuit."


    pause 0.3
    $ hideGroup()

    scene bg_chambre at adaptive_fullscreen with fade

    "Ma chambre."
    "Petite."
    "Propre."
    "Silencieuse."

    think "Enfin seul."

    "Je pose mes affaires."
    "En fait, je les jette presque."
    "Je suis épuisé."

    "Je jette un regard sur ce qui va me servir de chambre pendant un mois."
    "Honnêtement, c'est pas mal du tout."
    "Le lit est grand, une garderobe avec mes affaires…"

    think "Non, ce sont MES affaires !"

    "Il y a du matériel informatique également."
    "Je me demande à quoi on a accès."

    "Un petit boîtier est fixé près du bureau."
    "Une diode verte pulse lentement."
    "Sous la diode, un libellé minuscule : BROUILLEUR."

    menu:
        "Que fait Noam avec le brouilleur ?"

        "Ouvrir l'interface du brouilleur":
            $ j1_noam_curiosity += 1
            call day1_play_trace(path_type="arc", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=560, required=False) from _call_day1_trace_jammer
            if _return:
                call screen day1_jammer_panel()
                if noam_room_jammer_on:
                    "La diode reste verte."
                    "La chambre indique son mode privé comme une permission accordée."
                else:
                    "La diode passe au rouge."
                    "La chambre paraît soudain plus grande, et beaucoup moins à moi."
            else:
                $ j1_noam_prudence += 1
                "Le capteur refuse mon geste."
                "Je retire la main avant d'insister."

        "Laisser le brouilleur tranquille":
            $ j1_noam_prudence += 1
            "Je garde la diode verte dans un coin de mon regard."
            think "S'il est actif par défaut, je vais le laisser actif."

    "Sur le côté de la chambre, il y a aussi un accès à des toilettes privatives ainsi qu'une salle de bain."
    "Franchement, une douche bien chaude ça me tente bien."

    "Bon… Allez."

    pause 0.2

    scene bg_cg011 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg011")

    play sound sfx_shower

    "L'eau chaude coule."
    "Longtemps."
    "Mais qu'est-ce que ça fait du bien."

    "Je ferme les yeux."
    "Je profite du moment."
    "Je laisse la journée partir avec la vapeur."

    think "Pas ce soir."
    think "Je réfléchirai demain."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with fade

    "Je sors de la douche puis m'allonge tranquillement sur le lit."
    "Il est plus confortable que je ne l'imaginais."

    think "Mon amendement est déposé."
    think "Le reste ne m'appartient plus."

    "Le plafond est immobile."

    $ blink()

    "Pour une fois."

    $ blink()

    pause 0.4

    $ blink()

    "Je ne vais pas tarder à dormir."

    $ blink()

    $ journal_entries.append({"title": "Jour 1 — chambre", "text": "Je me suis réveillé dans un siège, avec une main qui ne voulait pas bouger et une salle entière déjà en train de nous regarder. Aujourd'hui, j'ai touché une tablette verrouillée, écouté Kami transformer un règlement en cage propre, validé une phrase sur un formulaire officiel, puis je l'ai poussée dans une urne qui ne rend rien. Même ma chambre dépend d'un interrupteur. Le brouilleur décide si je suis seul ou seulement moins visible. Ici, je suis libre dans les limites prévues par Kami."})

    hide screen day_period_hud

    scene black with fade
    stop music fadeout 2.0

    call end_day("2")

    jump _2_CANON

# Durée : 1m40 — Total : ~1h 4m 50s


# =============================================================================
# LABEL trace QTE jour 1
# =============================================================================

label day1_play_trace(path_type="curve_right", time_limit=6.0, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True):

    call trace_qte_run(mg_id="trace_day1", title="SYNCHRONISATION MOTRICE", path_type=path_type, time_limit=time_limit, wait_time=wait_time, tolerance=tolerance, max_errors=max_errors, anchor_x=anchor_x, anchor_y=anchor_y, required=required) from _call_day1_play_trace_trace_qte
    $ fix_stale_return_label(day1_trace_return_label(path_type, anchor_y))
    return (_return != "FAIL")
