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
    think "Enfin, je crois. Je me suis endormi dans un caisson et je me réveille sur un siège."
    think "Entre les deux : rien. Même ma mémoire a voyagé sous scellés."

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with fade

    think "Dossier rigide. Métal froid. Air recyclé. Plastique neuf."
    think "Tout le confort d'une salle d'interrogatoire qui sortirait de l'usine."

    $ blink()

    noam "Ma main..."
    think "Bouche sèche. Nuque en vrac. Main droite absente. Excellente arrivée."

    # --- Tutoriel trace QTE (première fois) ---
    show screen day1_tuto_trace
    pause

    call day1_play_trace(path_type="curve_right", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_day1_trace_wakeup
    $ j1_noam_initiative += 1

    hide screen day1_wakeup_overlay
    show screen day1_wakeup_overlay("soft")

    think "Les doigts reviennent. Puis le poignet. Enfin le bras."
    hide screen day1_wakeup_overlay
    think "Des sièges en cercle. Un corps sur chacun. Certains remuent, d'autres dorment encore."
    think "Douze respirations, des vêtements qui froissent, une gorge qu'on racle. Personne n'ose faire davantage de bruit."

    play sound sfx_beep
    voix "Initialisation en attente."
    think "Le son vient d'en bas. Plusieurs niveaux, peut-être."
    think "Une tablette noire est encastrée dans mon pupitre."

    menu:
        "Que dois-je faire ?"

        "Poser la main sur l'écran":
            $ j1_noam_curiosity += 1
            $ j1_tablet_touched = True
            think "Deux doigts sur la surface froide."
            call screen day1_tablet_interaction()
            play sound sfx_beep
            $ shake(6, 0.2)
            voix "Accès limité."
            think "Même éteinte, elle note que j'existe."

        "Retirer la main du pupitre":
            $ j1_noam_prudence += 1
            think "Je garde les doigts sur le bord du siège."
            think "Pas maintenant. Pas avant de comprendre à quoi elle sert."

    think "Je cherche Lysa. C'est la seule personne ici que je connais — si connaître un prénom compte."

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


    lysa blase "Ouais. Enfin réveillé."
    lysa blase "Les Sept Dormants ont tenu des siècles. Toi, dix minutes, et t'as déjà mauvaise mine."

    noam inquiet "On est où… ?"


    lysa reflexion "Tu vois bien où on est. Propre, froid, filmé. Le Conclave."
    lysa reflexion "Panoptique classique, mais avec un meilleur éclairage."

    think "Je ne reconnais aucun autre visage. Donc c'est vrai : les douze représentants, réunis dans la même cage."

    "Un homme se lève d'un bond. Son siège claque au sol."


    ryn colere "Putain mais on est où là ?!"
    ryn colere "Qui a fait ça ?!"

    ryn colere "J'ai posé une question !"



    mara rire "Tu veux dire... à part l'IA qui tient le monde en laisse ?"
    mara taquin "Joli réveil, cela dit. Très viril. Les caméras ont dû adorer."

    ryn colere "Je parle de ce qui nous arrive, là, maintenant."
    ryn colere "Qui nous a endormis."
    ryn colere "Qui nous a trimballés ici."



    tomas reflechit "Personne qui soit vraiment là. Enfin... pas ici, pas physiquement."
    tomas reflechit "Ça ressemble à une procédure automatique. Ce qui ne la rend pas moins volontaire."



    elen surpris "Aaaaah, automatique ou pas, c'est quand même nous qu'on a emballés dans des boîtes, non ?"
    elen surpris "Oh ! Vous croyez qu'ils ont prévu à manger ? Parce que le gaz, franchement, ça ouvre l'appétit et—"
    elen inquiet "Enfin... ouais. On s'habitue vraiment à tout, maintenant."

    think "Je cherche les caméras. Propres, discrètes, partout. Enfin quelque chose de familier."
    think "C'est triste que la surveillance soit la partie rassurante."



    julian peur "Écoutez ce silence. Il est construit. Mis en scène."
    julian reflexion "Quelqu'un veut que nous nous sentions seuls. Julian refuse de lui offrir ce spectacle."



    iris inquiet "Oh, superbe. Une cage insonorisée sans mode d'emploi. J'adore les protocoles où l'étape un est « paniquez au hasard »."
    iris blase "On attend quoi ? Un miracle ? Une notice ? Quelqu'un de compétent ? Non, oubliez la troisième option."



    nyra triste "Qu'est-ce qui vous inquiète le plus : le silence, ou ce qu'on risque d'y faire ?"
    nyra neutre "On peut peut-être commencer par s'écouter avant de lui donner une réaction."



    kael calme "C'est une attente."
    kael calme "Elle déclenchera la suite quand ses paramètres seront remplis."

    think "Le silence s'alourdit. Attendre, c'est admettre que quelqu'un d'autre possède le bouton lecture."



    noam reflexion "Au fait, vous avez vu Kami ?"

    think "Personne ne regarde l'écran central. Il est éteint, comme les tablettes."
    think "Ou personne ne veut montrer qu'il a entendu son nom."



    ryn reflechit "Non."
    ryn reflechit "Et ça me fait chier de le dire, mais je préfèrerais avoir des nouvelles."



    mara rire "J'adore. Douze pigeons, zéro animateur."
    mara taquin "Pas d'hôte, pas de verre, même pas un discours d'accueil. J'ai connu des enlèvements mieux organisés."



    tomas reflechit "On parle de Kami. Elle est toujours là, enfin... même sans image."
    tomas reflechit "Le fait qu'on ne la voie pas ne change rien à ce qu'on fait à cause d'elle."

    "Je fixe la tablette noire sur mon pupitre."
    if j1_tablet_touched:
        think "Je n'y touche pas une seconde fois. ACCÈS LIMITÉ est encore trop frais dans ma tête."
    else:
        think "Je tapote le bord. Rien."

    think "D'habitude, Kami adore être présente. Là, c'est une salle de classe sans prof."
    think "Sauf qu'ici le prof peut tuer les élèves à distance."

    lysa reflexion "Noam. T'as remarqué ?"



    noam reflexion "Quoi ?"


    lysa neutre "Aucun ordre."
    lysa neutre "Aucun écran."
    lysa neutre "Aucun message."
    lysa fatigue "... Silence radio."

    noam reflexion "Ça veut dire quoi pour toi ?"


    lysa blase "Ça veut dire qu'on est censés bouger sans ordre, ou qu'elle attend son moment."
    lysa blase "Dans les deux cas, c'est elle qui écrit la scène. Tu vois bien le problème."

    pause 0.4

    think "L'écran circulaire au centre ressemble à une scène qui attend son actrice principale."

    play sound sfx_beep
    voix "Phase d'observation maintenue."
    ryn reflechit "« Observation » ?"



    ryn reflechit "On reste assis ?"
    ryn reflechit "On attend ?"
    ryn reflechit "C'est ça le plan ?"

    elias neutre "Et après ? Tu comptes faire quoi ? Parce que là, c'est chaud de foncer sans savoir."



    sael raison "Le plan, c'est de survivre."
    sael raison "Ma grand-mère disait que le premier pas dans le brouillard appartient rarement à celui qui le fait."
    sael raison "Attendons que le signe soit clair."

    elen desaccord "Mais attendre, c'est risqué aussi, nooon ?"
    elen desaccord "C'est comme laisser un plat au four en espérant qu'il décide tout seul de pas brûler ! Enfin... je crois."


    tomas raison "Tout ça… c'est un pari, non ? Tout le temps."
    tomas raison "On s'est tous fait prendre de court. Moi le premier."
    tomas raison "Même les gens des districts… on aurait dit qu'ils tombaient des nues."

    think "Mon cœur accélère. Pas encore de la panique. Juste la lucidité qui pique."

    menu:
        "Que dois-je faire ?"

        "Se lever pour observer la salle":
            $ j1_noam_initiative += 1
            think "Je me lève à moitié. Assez pour voir les issues, pas assez pour devenir une menace."
            think "Tout est prévu pour qu'on soit visibles."

        "Rester assis et écouter":
            $ j1_noam_prudence += 1
            think "Je reste assis et j'écoute les respirations, les voix, les bips."
            think "Avant d'agir, il faut savoir dans quoi on met les pieds."

    think "Jour un."
    think "Et on est déjà en train d'essayer de deviner les règles."
    think "Super."

    think "Lysa ne tremble pas. Sa jambe, elle, n'a pas reçu la consigne."



    noam reflexion "On fait quoi, alors ?"

    think "Personne ne veut choisir en premier. Ici, une initiative peut devenir une cause de décès."

    pause 0.6

    "La ventilation change de régime. Une lumière blanche s'allume au-dessus du pupitre central."
    ryn "C'est quoi, ça ?"
    kael "Le système démarre."

    play sound sfx_gresillement
    $ shake(8, 0.25)

    voix "Diffusion centrale active."
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

    "L'écran s'éteint. Une seconde plus tard, les douze voix éclatent ensemble."
    ryn "C'est quoi ce délire ?"
    elias "Attends, trente jours ? C'est chaud !"
    iris "Oui, merci, nous savons compter."

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

    lysa doute "L'unanimité. C'est adorable."
    lysa blase "La Diète polonaise avait déjà testé le veto individuel. Tu sais comment ça finit ? Non ? Voilà."

    tomas raison "Ou alors... faire des compromis. Enfin, pour une fois."

    think "Autour de nous, le débat a déjà une heure de retard et trente jours d'avance."

    menu:
        "Où Noam pose-t-il son regard ?"

        "Suivre Lysa du regard":
            think "Lysa regarde les caméras avant les gens."
            think "Elle cherche les angles morts. S'il y en a."

        "Regarder l'écran central":
            think "Je garde les yeux sur l'écran central."
            think "Même éteint, il donne l'impression de pouvoir reprendre la parole à tout moment."

    nyra triste "Qu'est-ce qu'on veut obtenir, au juste ?"
    nyra neutre "Si chacun répond à ça, on trouvera peut-être un point commun avant de parler des règles."

    lysa blase "Ou les empirer."
    lysa desaccord "Les rendre légales, surtout. J’imagine déjà quelqu’un proposer de rétablir les exécutions publiques pour « harmonie visuelle »."

    elen inquiet "Mais on peut vraiment proposer n'importe quoi ? C'est énooorme !"
    elen sourire "Enfin, énorme bien ou énorme mauvais. Comme quand tu ouvres un paquet sans savoir si c'est sucré ou—"
    elen inquiet "Bref. Une petite fenêtre, c'est déjà de l'air, non ?"

    lysa blase "Une respiration sous l’eau."
    lysa taquin "Rafraîchissant pendant trois secondes. Puis on se noie quand même."

    mara rire "Vous parlez comme si on avait gagné au loto."
    mara taquin "On est dans une cage avec un bouton « vote » et un joli nœud rose. Cela dit, j'ai connu des cadeaux moins excitants."

    lysa blase "Une cage dorée. Caligula faisait déjà ça avec ses favoris. Bref."

    ryn colere "Attendez. Ici, les Commandements s'appliquent pas."
    ryn colere "Quelqu'un pète un câble, on fait quoi ?"

    iris reflexion "On est filmés en permanence. La pression publique est censée nous contenir."
    iris blase "Parce que la honte a toujours été un excellent protocole de sécurité. Aucun défaut connu."

    think "Julian se lève, ajuste sa veste et trouve une caméra avant de trouver ses mots."

    julian rire "Franchement ? Ce moment est historique."
    julian neutre "Enfin un lieu où nos paroles peuvent peser sur les règles — devant tous ceux qu'elles concernent."
    julian idee "Julian n'a pas l'intention de gaspiller cette scène."

    think "Il offre son meilleur profil à la caméra. Pour lui, ça a toute l'importance du monde."

    lysa doute "T'es sérieux ?"
    lysa colere "On nous enferme, on nous filme, on nous fait jouer les réformateurs sous peine de mort — et toi, t'as déjà choisi ton profil."
    lysa blase "Narcisse avait au moins un reflet honnête. Bref."

    julian idee "Si nous devons rester ici trente jours, faisons en sorte qu'ils comptent."
    julian idee "Tu peux mépriser la forme, Lysa. Les gens, eux, ont besoin d'un résultat."

    think "Il salue la caméra comme si le public l'attendait déjà."

    noam inquiet "…"



    tomas reflechit "Au moins, ça confirme quelque chose."
    tomas reflechit "Elle veut du spectacle. Vraiment."
    tomas raison "Et si elle veut du spectacle… c'est qu'elle compte sur le fait qu'on va se déchirer entre nous."

    pause 0.4

    think "Un détail revient gratter au mauvais endroit : aujourd'hui, chacun propose un amendement."

    noam reflexion "Donc aujourd'hui… on doit tous proposer quelque chose."

    lysa culpabilite "Ouais."
    lysa culpabilite "Et personne saura qui a proposé quoi."

    kael neutre "Partageons seulement les thèmes."
    kael neutre "On identifiera les incompatibilités avant le vote."

    think "Le silence revient. Cette fois, ce n'est pas la peur. C'est le calcul."

    elen inquiet "Oh ! On peut commencer par une règle toute simple !"
    elen sourire "Genre : personne s'étripe avant le petit-déj. Après, idéalement personne s'étripe du tout, hein."

    lysa blase "Douze personnes enfermées, filmées, et le meurtre retiré du règlement."
    lysa reflexion "Le Léviathan sans souverain dans la pièce. T'as vu ce que ça donne, d'habitude ?"
    lysa fatigue "Voilà. Et cette fois, ce sera diffusé en haute définition."

    pause 0.4

    think "Les premiers groupes se forment déjà : deux ici, trois là, chacun surveillant à qui il vient d'être associé."

    noam reflexion "On fait quoi, nous ?"

    lysa determine "On visite."
    lysa blase "On repère les angles morts, les caméras, les endroits où on peut encore respirer sans être jugé."
    lysa reflexion "Et surtout… on ferme sa gueule devant les caméras."

    elen reflexion "Je vais voir s'il y a une infirmerie ! Ou des pansements. Ou des biscuits."
    elen sourire "Les trois seraient vraiiiment bien."

    noam neutre "Ok."

    pause 0.4

    think "La salle se vide. À mon tour d'explorer la cage."

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

    ryn "Ça, c'est censé nous rassurer ?"

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

    think "Personne ne commente. Être filmés est la seule règle qui ressemble encore à notre quotidien."

    kami "Mais il y a une exception."

    elen "Une exception ?"

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
    voix "Dépôt des amendements ouvert."
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

    think "L'urne trône au centre de la pièce. Même notre anonymat a besoin d'une scène."

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

    kael calme "Partageons nos intentions. Pas les textes."
    kael calme "On identifiera les incompatibilités avant le dépôt."

    pause 0.3


    iris fatigue "Oh, excellente idée. Supprimons l'anonymat avant même d'avoir utilisé l'urne."


    kael neutre "Pourquoi ça ?"


    iris desaccord "Un amendement peut sembler raisonnable et provoquer une catastrophe systémique."
    iris taquin "Kami dira quoi ? « Oups, erreur de conception » ? Elle cherchera un responsable. Nous."


    sael determine "Ma grand-mère disait qu'une faute sans visage finit toujours par en emprunter un."
    sael determine "Si quelque chose tourne mal, l'un de nous portera ce visage."


    elen inquiet "Et puis tout le monde veut peut-être pas en parler, nooon ?"
    elen sourire "On garde tous des recettes secrètes. Enfin, des idées. Les recettes aussi, mais c'est pas le sujet."


    julian sourire "Je parlerai. La transparence est le premier devoir d'un collectif."
    julian sourire "Julian ne demandera pas aux autres un courage qu'il refuse lui-même."


    mara neutre "Le type qui parle de lui à la troisième personne craint de se faire remarquer. Adorable."
    mara taquin "Ton prénom, déjà ? Jules ? Justin ?"

    julian neutre "Julian. Tu le savais."
    mara rire "Maintenant, oui."

    pause 0.3


    ryn reflechit "Et si on touche à rien ?"
    ryn reflechit "On vote contre tout. Les règles restent connues. Fin."


    nyra triste "Tu veux protéger ce qui fonctionne. Je comprends."
    nyra neutre "Mais qui ici peut dire aux autres que leur district n'a rien à changer ?"


    tomas hesitation "Ça ne marchera pas, Ryn. Enfin... pas forcément."
    tomas hesitation "Kami a dit qu'un refus pouvait avoir des conséquences. On ignore lesquelles."

    pause 0.3


    kael reflechit "Raison de plus pour comparer nos intentions."
    kael reflechit "Le silence augmente le risque."


    lysa doute "Ou c'est notre seule défense."
    lysa reflexion "Quelqu'un peut annoncer une chose et écrire l'inverse. Le cheval de Troie avait aussi l'air d'un cadeau collectif."
    lysa taquin "Et avec deux textes jamais tirés, l'alibi est offert."

    pause 0.4

    think "Le silence retombe. Pas lourd. Méfiant."

    # --- Le chrono passe à 20 min (mise à jour dynamique) ---
    $ day0_timer_set(20 * 60)

    elias reflechit "Les gars... il reste vingt minutes. C'est chaud, là."

    pause 0.4


    ryn fatigue "Écoutez, faites ce que vous voulez."

    ryn fatigue "Je vais écrire."


    play sound sfx_paper
    voix "Premier amendement déposé."
    play sound sfx_drop

    think "Voilà."
    think "Le premier."


    nyra reflexion "Tu savais déjà ce que tu voulais changer ?"


    mara sourire "Dès que l'un de nous plonge, les autres suivent."
    mara taquin "Rassurant, l'instinct de troupeau. Très élégant aussi."

    pause 0.3

    voix "Dépôt enregistré."


    sael neutre "Nous pouvons en parler jusqu'à la nuit. Chacun écrira ce qu'il croit juste."
    sael neutre "Les morts savent mieux que nous combien la justice change de visage."


    play sound sfx_drop
    voix "Deuxième amendement. Troisième amendement."

    think "Plus personne ne débat vraiment."

    think "Nous ne sommes plus que quelques-uns sans texte. Personne ne cherche nos regards."


    kael calme "Refus de coordination. Compris."


    julian neutre "Retenez bien ce silence. C'est toujours là que les vraies décisions se prennent."


    play sound sfx_paper
    think "L'urne se remplit, papier après papier."
    play sound sfx_drop

    think "C'est ça le Conclave."
    think "Pas un débat."
    think "Un enchaînement."


    elen inquiet "Et si quelqu'un met un truc vraiiiment horrible ?"
    elen inquiet "Genre le genre de surprise qui te coupe l'appétit. Ça existe, ça ?"


    iris fatigue "Alors on vote contre et le refus nous explose au visage, ou on vote pour et le texte s'en charge."
    iris blase "Système impeccable. Aucune branche ne mène à une catastrophe."

    pause 0.4

    play sound sfx_paper
    think "Certains déposent. Les autres écrivent encore."

    play sound sfx_drop
    think "L'urne est presque pleine. Il faut que je m'y mette. Enfin, maintenant."

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

    think "Chaque papier qui tombe me rappelle que je traîne. Feuille blanche, stylo, vide au milieu de la poitrine."
    think "Un examen où une mauvaise réponse peut brûler une ville. Rien de disproportionné."
    think "Respire, Noam. T'as peur. Enfin, quelqu'un dans cette situation aurait peur."
    think "Je viens vraiment de reformuler ma propre peur pour ne pas dire « je ». Impressionnant."

    pause 0.3

    think "Deux idées. Concrètes. Défendables. Peut-être."
    think "La première : l'information locale. Le cinquième Commandement interdit tout ce qu'Archive ne valide pas."
    think "Mais personne ne sait ce qui est validé. Alors tout le monde se tait, même pour parler du froid ou d'une rue coupée."
    think "Autoriser le quotidien. Ce qu'on voit, ce qu'on vit. Sans transformer chaque phrase en menace d'État."

    pause 0.2

    think "La seconde : l'assistance minimale."
    think "Aujourd'hui, tendre la main peut ressembler à une initiative. Une initiative peut ressembler à une infraction."
    think "Aider. Prévenir. Intervenir quand quelqu'un tombe. Ça ne devrait pas demander du courage."

    pause 0.3

    think "Les deux paraissent raisonnables. C'est précisément ce qui m'inquiète."
    think "Enfin... assez. Il faut choisir."

    # --- Tutoriel amendement ---
    show screen day1_tuto_amendment
    pause

    call screen day1_amendment_form()
    $ noam_amendement_choix = _return
    $ j1_amendment_validated = True

    if noam_amendement_choix == "information_locale":
        $ j1_noam_mediation += 1

        think "Libérer la parole locale sans ouvrir une brèche assez large pour qu'Archive enterre le texte."
        think "J'écris, je retire un mot, j'en ajoute deux. Trop vague. Trop prudent. Enfin... plus précis."
        think "Le quotidien, l'immédiat, ce qu'on voit et ce qu'on ressent : personne ne devrait mourir pour l'avoir formulé."

    if noam_amendement_choix == "assistance_minimale":
        $ j1_noam_initiative += 1

        think "Permettre l'entraide. Pas une obligation impossible : un droit d'agir quand on le peut."
        think "Aider. Prévenir. Intervenir."
        think "Laisser quelqu'un tomber est aussi une décision. J'aimerais qu'elle cesse d'être la plus sûre."

    pause 0.3

    think "Ma main tremble. Pas assez pour lâcher le stylo. Assez pour arrêter de prétendre que je vais bien."

    think "Voilà."
    think "C'est fait."

    think "Je veux corriger. Nuancer. Préciser jusqu'à ce que le texte ne dise plus rien."

    think "Non."
    think "Sinon je recommencerai encore et encore."

    voix "Quatre minutes avant fermeture de l'urne."

    think "Ça fait déjà si longtemps que ça ?"

    pause 0.2

    think "Je plie la feuille de travers et me lève. Ma chaise crie pour moi."

    think "Je sens le regard des caméras."
    think "Même sans forcément les voir."

    think "L'urne paraît plus loin à chaque pas. Ma gorge se serre."

    think "Et si j'avais fait le mauvais choix ?"
    think "Non. Arrête d'y penser."

    call day1_play_trace(path_type="vertical_up", time_limit=6.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_day1_trace_urn

    play sound sfx_paper
    think "Je pousse la feuille dans la fente."
    play sound sfx_drop
    $ impact(8, 0.2, "#3BCC82")
    voix "Amendement enregistré."
    $ j1_amendment_deposited = True
    call screen day1_urn_confirmation()
    think "Impossible de la récupérer. Les regrets arrivent dans les temps, eux."

    pause 0.4

    think "Voilà."
    think "Mon premier amendement."

    think "Je retourne à ma place. J'étais le dernier. Évidemment."

    scene bg_conclave at adaptive_fullscreen with dissolve

    jump _1_AMENDEMENT_DEPOSE

# Durée : 3m — Total : ~1h 0m 15s


# =============================================================================
label _1_AMENDEMENT_DEPOSE:
# =============================================================================

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    $ day0_timer_active = False
    hide screen day1_amendment_timer

    voix "Dépôt fermé."

    play sound sfx_beep
    voix "Douze participations enregistrées."

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

    elias "C'est chaud d'être soulagé pour ça."
    iris "Profite. Elle vient de fixer la barre sous le sol."

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
    voix "Fin de session."

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Les écrans s'éteignent. Les chaises raclent le sol. Personne ne se dit au revoir."

    think "C'est fini."
    think "Pour aujourd'hui du moins."

    scene bg_couloir at adaptive_fullscreen with fade

    think "Le couloir est calme. Presque normal, si on oublie l'urne capable de réécrire le monde derrière moi."

    think "J'ai déposé un amendement."
    think "On en a tous déposé un."
    think "J'espère ne pas avoir fait une connerie."

    think "Demain matin à neuf heures."

    pause 0.3

    think "Je m'arrête au milieu du couloir."

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

    think "Lumière douce, canapés presque vides. La salle de repos mérite presque son nom."

    think "Je m'attendais à pire."
    think "Ou à plus de silence."

    pause 0.2

    $ showGroup([
        ("julian", "detendu", 0.22),
        ("nyra", "sourire", 0.50),
        ("mara", "sourire", 0.78),
    ])

    julian detendu "Ah. Toi non plus, tu n'as pas réussi à te coucher ?"

    think "Évidemment."


    nyra sourire "Qu'est-ce qui t'a amené ici ? Le silence de ta chambre, ou le bruit dans ta tête ?"

    think "Julian se laisse tomber dans un fauteuil avec juste assez de bruit pour rester au centre de la scène."

    julian detendu "J'ai réécrit ma proposition trois fois. Ce genre de phrase peut rester dans l'Histoire."
    julian detendu "Julian refuse d'y entrer avec une mauvaise formulation."

    pause 0.2


    mara sourire "Moi, j'ai écrit ce que je voulais. C'est une expérience assez nouvelle."
    mara taquin "Si ça vous plaît, je prends les compliments. Sinon, je prends quand même un verre."

    think "Tant pis."
    think "Facile à dire."

    pause 0.3

    noam "Ça simplifie les choses."
    mara taquin "Tu devrais essayer. Je peux t'apprendre."

    julian detendu "Nous écrivons pour des millions de personnes, puis le hasard décide si nos mots existent."
    julian inquiet "Imaginez que ma proposition reste dans l'urne. Un moment pareil, perdu avant même d'avoir été entendu."

    nyra sourire "Tu veux être utile, ou tu veux être entendu ?"
    julian detendu "Les deux ne s'opposent pas."
    nyra sourire "Je n'ai pas dit qu'ils s'opposaient."

    pause 0.2

    think "Le silence qui suit n'est pas gênant. Juste calme. Presque normal."

    think "C'est étrange."
    think "On dirait presque une soirée normale."

    mara sourire "Vous croyez qu'elle nous regarde, là ? J'espère que mon bon profil est du bon côté."

    julian detendu "Sûrement. Et tant mieux. Un public attentif est une responsabilité."
    mara taquin "Bien sûr. C'est pour ça que tu vérifies la caméra toutes les trente secondes. Par responsabilité."

    pause 0.3

    think "Personne ne le contredit. Pour deux minutes, personne ne cherche à gagner."

    think "Ça fait du bien."
    think "De ne pas faire attention pendant deux minutes."

    pause 0.4

    play sound sfx_door
    $ hideGroup()

    scene bg_cg010 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")
    show screen kami_broadcast_ui

    "La porte s'ouvre. Tomas apparaît avec un plateau chargé de six tasses."

    tomas hesitation "Euh…"
    tomas hesitation "Bonsoir."

    mara sourire "Attention, tout le monde. Opération à haut risque."

    $ bc_show("julian", "detendu", px=-70, py=-50, pz=0.85)
    julian detendu "Voilà une entrée que je respecte."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra sourire "Tu veux qu'on libère la table, ou tu préfères réussir seul ?"
    $ bc_hide()

    tomas hesitation "Si je renverse ça maintenant, enfin... je vais vivre sous une table jusqu'au trentième jour."
    $ bc_show("mara", "content", px=-70, py=-50, pz=0.85)
    mara sourire "Y'a pire."
    mara sourire "Tu pourrais mourir pour de vrai."
    $ bc_hide()

    mara sourire "Il reste une place sous celle-ci."

    tomas hesitation "Je me suis dit que…"
    tomas hesitation "…que ça ferait peut-être du bien."
    tomas hesitation "Un truc chaud. Juste… un truc chaud."

    tomas "Voilà. Rien de cassé. Enfin, pas encore."

    $ bc_show("julian", "joie", px=-70, py=-50, pz=0.85)
    julian detendu "Un vrai héros. Sans discours, en plus. C'est presque vexant."
    $ bc_hide()

    pause 0.3

    scene bg_cg010_1 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")

    think "Les tasses circulent. La vapeur transforme la table en refuge provisoire."

    think "Ça sent le thé."
    think "Un vrai thé bien fort comme il faut."
    think "Pas un truc synthétique."

    nyra vide "Ça vous manquait aussi ? Tenir quelque chose de chaud."

    mara vide "Ouais…"
    mara vide "C'est débile mais ça fait du bien."
    mara vide "Un tout petit peu."

    menu:
        "Que devrais-je faire ?"

        "Prendre une tasse":
            $ j1_noam_initiative += 1
            think "La tasse me brûle presque les doigts. Je la garde."

            think "C'est idiot."
            think "Mais ça m'ancre."

        "Laisser la tasse aux autres":
            $ j1_noam_prudence += 1
            think "Je laisse la tasse. Mes mains restent autour du vide."
            think "Ce soir, même un geste simple ressemble à une décision."

    tomas vide "Demain…"
    tomas vide "À neuf heures on saura…"

    julian vide "Ouais."
    julian vide "Demain."

    think "Personne n'ajoute rien. Tout le monde pense à neuf heures."

    pause 0.4

    think "On boit en silence."

    think "Je sais pas combien de temps ce calme durera."
    think "Mais là, en ce moment…"
    think "C'est agréable."

    pause 0.4

    think "Les tasses se vident. La dernière reste sur le plateau, intacte."

    mara vide "Bon bah voilà."
    mara vide "Je vais aller me pieuter avant de péter un câble."

    nyra vide "Moi aussi."
    nyra vide "Avant que je recommence à réfléchir."

    julian vide "Excellente idée."

    think "Ils se lèvent un à un."

    think "La parenthèse se referme."

    pause 0.3

    think "Je reste quelques secondes, la tasse vide entre les mains."

    think "Je devrais y aller aussi."

    $ hideGroup()
    jump _1_FIN_JOURNEE_DORTOIR

# Durée : 1m55 — Total : ~1h 3m 10s


# =============================================================================

label _1_FIN_JOURNEE_DORTOIR:
# =============================================================================

    scene bg_couloir at adaptive_fullscreen
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Le couloir n'est pas vide, seulement plus lent. Même le bâtiment semble reprendre son souffle."

    think "Ça y est."
    think "La journée est finie."
    think "Enfin… presque."

    think "Je marche sans m'accrocher aux pensées qui passent."

    pause 0.3

    scene bg_dortoir at adaptive_fullscreen with fade

    think "La lumière du dortoir est plus chaude, moins clinique. Elias est déjà là."

    $ showGroup([
        ("elias", "detendu", 0.22),
        ("noam", "neutre", 0.78),
    ])

    if choix_1_soir == "salle_repos":

        elias detendu "Ah, toi aussi t'es encore debout. C'est chaud de dormir après ça."

        think "Elias."


        noam neutre "Ouais."
        noam neutre "J'avais pas trop envie de rester seul."

        elias detendu "Je vois."
        elias detendu "La salle de repos, hein ? Pas con."

        noam neutre "Ouais."

        elias detendu "Bonne idée."

        elias detendu "Moi j'ai tenté de dormir direct."
        elias detendu "Raté."

    if choix_1_soir == "dormir":

        elias detendu "En voilà un qui se couche tôt. Tu voulais rester seul ?"


        noam neutre "On peut dire ça."
        noam neutre "Drôle de journée."

    pause 0.2

    think "Son sourire est franc. Fatigué, mais franc."

    elias detendu "C'est chaud quand même. J'ai rien porté, rien monté, et je suis rincé comme après douze heures d'usine."

    noam neutre "Ouais."
    noam neutre "Comme un examen où on aurait déménagé la salle pendant l'épreuve. Enfin... quelque chose comme ça."

    elias detendu "Ouais. J'ai pas trop compris, mais c'est exactement ça."

    pause 0.3


    elias inquiet "Demain matin, ça va être chaud pour de vrai."

    noam neutre "Ouais."


    think "On n'insiste pas. Pas besoin."

    elias jaloux "Bonne nuit, Noam."

    noam neutre "Bonne nuit."


    pause 0.3
    $ hideGroup()

    scene bg_chambre at adaptive_fullscreen with fade

    think "Ma chambre. Petite, propre, silencieuse."

    think "Enfin seul."

    think "Je jette presque mes affaires et découvre un grand lit, une garde-robe..."

    think "Non, ce sont MES affaires !"

    think "Du matériel informatique. Près du bureau, un boîtier pulse en vert : BROUILLEUR."

    menu:
        "Que dois-je faire ?"

        "Ouvrir l'interface du brouilleur":
            $ j1_noam_curiosity += 1
            call day1_play_trace(path_type="arc", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=560, required=False) from _call_day1_trace_jammer
            if _return:
                call screen day1_jammer_panel()
                if noam_room_jammer_on:
                    think "La diode reste verte. La chambre présente l'intimité comme une permission accordée."
                else:
                    think "La diode passe au rouge. La chambre paraît plus grande, et beaucoup moins à moi."
            else:
                $ j1_noam_prudence += 1
                think "Le capteur refuse mon geste. Je retire la main avant d'insister."

        "Laisser le brouilleur tranquille":
            $ j1_noam_prudence += 1
            think "Je garde la diode verte dans un coin de mon regard."
            think "S'il est actif par défaut, je vais le laisser actif."

    think "Salle de bain privée. Une douche chaude est la première décision simple de la journée."

    pause 0.2

    scene bg_cg011 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg011")

    play sound sfx_shower

    think "L'eau chaude coule longtemps. Je laisse la journée partir avec la vapeur."

    think "Pas ce soir."
    think "Je réfléchirai demain."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with fade

    think "Je m'allonge. Le lit est plus confortable que prévu."

    think "Mon amendement est déposé."
    think "Le reste ne m'appartient plus."

    think "Le plafond est immobile."

    $ blink()

    think "Pour une fois."

    $ blink()

    pause 0.4

    $ blink()

    think "Je ne vais pas tarder à dormir. Enfin, je l'espère."

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
