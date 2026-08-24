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

# =============================================================================
label _1_CANON:
# =============================================================================

    $ day_id = 1
    $ current_day = 1
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"

    scene black
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Jour un."
    think "Enfin, je crois... Tout ce dont je me rappelle, c'est ce foutu caisson et ce mal de crâne qui ne me quitte plus."

    pause 0.4

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_113
    scene bg_conclave at adaptive_fullscreen with fade

    think "Dossier rigide. Métal froid. Air recyclé. Plastique neuf. Finalement, j'ai l'impression de n'avoir jamais quitté Harmonie."
    think "C'est exactement le même niveau de confort... Si on peut appeler ça comme ça."

    $ blink()

    noam "Ma main..."
    think "J'ai la tête qui tourne, la bouche sèche, la nuque en vrac. Qu'est-ce qu'ils ont utilisé comme produit pour nous endormir ?!"

    # --- Tutoriel trace QTE (première fois) ---
    show screen day1_tuto_trace
    pause

    call day1_play_trace(path_type="curve_right", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_day1_trace_wakeup

    think "J'étends mes bras devant moi, difficilement, mais j'y parviens."
    think "Tout me semble lointain, comme si je me réveillais d'une anesthésie complète."
    think "Il y a des sièges en cercle. Un corps sur chacun. Certains remuent, d'autres dorment encore."
    think "Il n'y a pas beaucoup de bruits, des respirations fortes, des vêtements qui se froissent, une gorge qui racle. Personne n'ose faire davantage de bruit."

    play sound sfx_beep
    voix "Initialisation en cours..."
    think "Une voix robotique retentit depuis plus bas. Il y a plusieurs niveaux, peut-être."
    think "Une tablette noire est encastrée dans mon pupitre."

    menu:
        "Que dois-je faire ?"

        "Poser la main sur l'écran":
            think "Voyons voir ce que tu as à m'apprendre."
            call screen day1_tablet_interaction()
            play sound sfx_beep
            $ shake(6, 0.2)
            voix "Noam. Accès limité."
            think "Elle me reconnaît à ma main, ils ont dû prendre nos empreintes."

        "Regarder autour de moi":
            think "La tablette ne m'intéresse pas."
            think "Pas maintenant. Pas avant de comprendre où on est."

    think "Je cherche des yeux Lysa. C'est la seule personne ici que je connais. Enfin connaître, je ne connais que son prénom."

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

    lysa blase "Sérieux, arrête de crier !"

    noam inquiet "Hein ? Mais je crie pas..."

    lysa blase "Bien sûr que si que tu cries, tu ne t'en rends même pas compte ?"
    lysa blase "Les Sept Dormants ont tenu des siècles. Toi, au bout de dix minutes, et t'as déjà mauvaise mine."

    noam inquiet "On est où… ?"

    lysa reflexion "Tu vois bien où on est. À ton avis... Le Conclave."
    lysa reflexion "Mais faut dire que je voyais ça d'une façon totalement différente."

    think "Je regarde autour, en m'efforçant de ne pas parler. Je ne reconnais aucun autre visage. Donc c'est vrai : les douze représentants sont bien réunis dans la même cage."

    "Un homme se lève d'un bond. Son siège claque au sol."

    ryn colere "Putain mais on est où là ?!"
    ryn colere "Qui a fait ça ?!"

    mara rire "Tu veux dire... à part l'IA qui tient le monde en laisse ?"
    mara taquin "Joli réveil, cela dit. Très viril. Les caméras ont dû adorer."
    "Elle fait un mouvement de tête dans une direction, pour montrer une caméra."

    ryn colere "Hein ?! Mais de quoi vous parlez ?"
    ryn colere "Je parle de ce qui nous arrive, là, maintenant."
    ryn colere "Qui nous a endormis."
    ryn colere "Qui nous a trimballés ici."
    ryn colere "J'en ai rien à foutre de Kami et de ses règles idiotes moi !"

    tomas reflechit "C-Comment ça t'es au courant de rien ..?"
    tomas reflechit "Tu... Tu as bien entendu l'annonce, non ?!"

    elen surpris "Aaaaah, je sais même pas depuis combien de temps on était là, c'est quand même nous qu'on a emballés dans des boîtes, non ?"
    elen surpris "Oh ! Vous croyez qu'ils ont prévu à manger ? Parce que le gaz, franchement, ça ouvre l'appétit et—"

    ryn colere "Hein ?! Emballé dans des boîtes ? Mais qu'est-ce que vous racontez ? Et qui vous êtes d'abord !"

    lysa blase "Sérieux ? Comment ça t'es au courant de rien ?"

    ryn colere "Vous êtes de mèche avec ceux qui m'ont attaqué ? C'est ça ?!"
    ryn colere "Vous avez de la chance de m'avoir pris dans le dos, sinon je vous aurais eu !"

    mara taquin "Ah parce qu'en plus tu as perdu la bagarre ?!"

    ryn colere "Quoi ?? Qu'est-ce que t'as dit !"

    mara taquin "Ouuuh effraaayant !"

    noam "Bon arrêtez un peu là. Je pense qu'on essaye tous de comprendre ce qui nous arrive."

    think "Je cherche les caméras. Elles sont propres, discrètes, partout. Enfin quelque chose de familier."

    julian peur "On pourrait presque apprécier le silence, si l'un d'entre nous ne faisait pas que de meugler."
    julian reflexion "Kami veut que nous nous sentions seuls. JE refuse de lui offrir ce spectacle."

    iris inquiet "Tu ne changeras donc jamais."
    iris blase "On attend quoi ? Un miracle ? Une notice ? Quelqu'un de compétent ? On ne sait même pas ce qu'on doit faire."

    nyra triste "Si elle voulait nous parler elle pourrait le faire à tout moment."
    nyra neutre "Elle est omnipotente après tout."

    kael calme "Mouais, si elle a envie."
    kael calme "Si ça se trouve ça la fait marrer de voir douze inconnus enfermés dans une pièce."

    elen inquiet "Hein ?? On est enfermés ?!"
    elen inquiet "Mais comment qu'on va faire..."
    elen fatigue "Aaaahh ! En plus j'ai envie d'aller faire pipi !"

    ryn reflechit "Et bah retiens-toi. Fais comme tout le monde"

    mara rire "Facile à dire quand on est un mec. Tu pourrais aller pisser dans un coin de la pièce que y'aurait pas de problème."

    ryn colere "Quoi ?! C'est pas parce que je suis de Limen que je sais pas me tenir !"

    mara rire "J'adore. Douze pigeons, zéro animateur. Et un susceptible."
    mara taquin "Il est vraiment mal foutu cet enlèvement. Amatrice !"

    tomas reflechit "T-Tu sais qu'elle entend tout ce qu'on dit ? Tout le temps."
    tomas reflechit "Le fait qu'on ne la voie pas ne change rien à ce qu'on fait à cause d'elle."

    think "D'habitude, Kami adore être présente. Là, c'est comme une salle de classe sans prof."
    think "Sauf qu'ici le prof peut tuer les élèves à tout moment, et à distance."

    lysa fatigue "... Silence radio."

    noam reflexion "Ça veut dire quoi pour toi ?"

    lysa blase "J'en sais rien."
    "Elle se dirige vers la porte puis tente de l'ouvrir."
    lysa colere "Putain, ça s'ouvre pas."

    tomas neutre "Tu as une erreur en particulier ?"

    lysa "Hein ? Euh attends..."
    lysa "Lysa, Permission denied..."

    tomas reflechit "D-Donc ça te détecte et... Et il y a un système de permission par personne..."
    tomas raison "On devrait peut-être tous essayer ?"

    lysa blase "T'en as d'autres des idées de génie ?"
    lysa fatigue "Je vois pas pourquoi l'un d'entre nous aurait des permissions que les autres n'auraient pas."

    nyra hesitation "Sauf si elle veut créer des tensions dans le groupe dès le début ?"

    pause 0.4

    think "Tout le monde se regarde de travers."
    think "L'un d'entre nous a-t-il la permission d'ouvrir la porte ?"

    elias inquiet "Sinon, on peut tenter de la forcer."

    iris peur "Tu veux nous faire tuer ou quoi ?!"

    sael raison "Il n'y a pas le choix."
    sael raison "Ma grand-mère disait que le premier pas dans le brouillard appartient rarement à celui qui le fait."
    sael raison "Il faut prendre une décision claire."

    elen desaccord "Mais attendre, c'est risqué aussi, nooon ?"
    elen desaccord "C'est comme laisser un plat au four en espérant qu'il décide tout seul de pas brûler !"

    sael "Donc il faut choisir. Soit on tente d'ouvrir la porte."
    sael "Soit on attend."

    think "Mon cœur accélère."

    tuto "Prêt pour un nouveau tutoriel ?"
    tuto "J'espère bien !"
    tuto "Au cours de votre aventure, vous pourrez faire des choix !"
    tuto "Mais attention, tous les choix ne se valent pas !"
    tuto "Il y a des choix mineurs qui ont une importance limitée : ils peuvent changer vos relations, ou vous débloquer de petites scènes différentes."
    tuto "Et puis il y a les choix CRITIQUES. Qui peuvent changer TOUT LE RESTE de votre aventure ou vous réserver bien des surprises !"
    tuto "Ce choix en est un, alors choisissez bien !"

    jump _1_CHOICE

label _1_CHOICE_DEATH:
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_114
    scene bg_conclave at adaptive_fullscreen with fade

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

    $ _day1_asphyxia_deaths = getattr(persistent, "succes_day1_asphyxia_deaths", 0)

    if _day1_asphyxia_deaths <= 1:
        "Je mets mes mains à mon cou, il est légèrement douloureux."
        think "Quel est ce sentiment ? Qu'est-ce que je faisais déjà ?"
        think "Ah oui, on hésitait sur la marche à suivre..."
    elif _day1_asphyxia_deaths == 2:
        "Je prends une grande bouffée d'air, comme si j'allais en avoir besoin."
        think "Qu'est ce qui m'arrive ?"
        think "Pourquoi j'ai un mauvais présentiment ?"
    else:
        "Je caresse du bout des doigts la ligne de mon cou."
        think "Cette sensation, d'où venait-elle ?"
        think "Et pourquoi est-elle aussi intense ?"

    jump _1_CHOICE

label _1_CHOICE:

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Que devrions-nous faire ?"

        "Tenter d'ouvrir la porte":
            noam determine "Raah, on ne peut pas rester là à rien faire !"
            think "Les caméras nous regardent, tout le monde nous regarde."

            ryn "Bon bouge de là !"
            play sound sfx_thud volume 5.0

            think "Il met rapidement sa main sur le capteur. La porte ne s'ouvre pas."

            ryn "Raah, moi aussi je peux pas !"
            ryn "Allez au suivant ! Qu'on termine ça au plus vite."

            noam raison "Bon, bah je vais tenter."
            "Je mets ma main sur la porte puis je vois comme une petite lumière verte qui scanne ma main."

            think "Noam, Permission denied."
            noam triste "Fait chier, ça marche pas..."

            play sound sfx_clim volume 5.0

            think "Je regarde plus en détail l'écran pour voir s'il y a d'autres indications."
            noam surpris "Hein, c'est quoi ça ?"
            think "Sur l'écran il est affiché en petit dans le coin supérieur droit : 3/3"

            "Je me retourne face aux autres."

            noam hesitation "Y'a un chiffre bizarre à côté aussi, il y a écrit 3."

            kael surpris "Hein ? T'en es sûr ?"
            kael doute "Ça ne pourrait pas être..."
            kael peur "Oh non..."

            noam peur "Quoi qu'est-ce qu'il y a ?!"

            "Ma tête commence soudainement à tourner. Quelque chose ne va pas."

            "Quel est ce bruit ?"
            think "Pourquoi je vois tout flou ?"
            scene cg007 at adaptive_fullscreen with vpunch
            $ unlock_gallery_image("cg007")
            $ _day1_asphyxia_deaths = register_day1_asphyxia_death()

            if _day1_asphyxia_deaths <= 1:
                think "Ma gorge me brûle..."
                think "Pourquoi j'ai... j'..."
            elif _day1_asphyxia_deaths == 2:
                think "Ma gorge me brûle encore. Exactement comme avant."
                think "Mon corps reconnaît la panique avant moi."
            else:
                think "Ma gorge reconnaît la brûlure."
                think "Troisième fois. Même la peur commence à avoir un goût familier."

            think "Put...a..."

            scene black with dissolve

            jump _1_CHOICE_DEATH

        "Rester assis et écouter":
            think "Je m'assois à une chaise et ne bouge pas."

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

    noam doute "On ne sait pas ce qu'on doit faire, il vaut mieux attendre les consignes."

    julian "Comme tu es arrangeant. Typique du premier de la classe."

    think "Jour un, et on en est déjà là, à se chamailler pour rien."

    noam "Profitons-en pour observer cette salle en détail, on en apprendra peut-être un peu plus."

    kael sourire "Ouais, t'as sans doute raison."

    pause 0.4

    $ hideGroup()
    jump _1_PNC_CONCLAVE

# =============================================================================
# 3m — Total : ~24m30
# =============================================================================

screen day1_conclave_pnc():
    modal True
    zorder 200

    $ conclave_scene = room_scene_current_number("conclave")

    add Solid("#000")
    use room_scene_background("conclave")
    use room_scene_interactions("conclave", {
        "conclave1_porte": "_1_PNC_CONCLAVE_PORTE",
        "conclave2_ecran": "_1_PNC_CONCLAVE_FINISH",
        "conclave3_porte_debaras": "_1_PNC_CONCLAVE_DEBARAS",
    })

    if conclave_scene == 1:
        imagebutton:
            idle Transform(character_image("lysa", "neutre"), zoom=1.00)
            hover Transform(character_image("lysa", "reflexion"), zoom=1.00)
            focus_mask True
            xalign 0.18
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_LYSA")

        imagebutton:
            idle Transform(character_image("ryn", "colere"), zoom=1.00)
            hover Transform(character_image("ryn", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.39
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_RYN")

        imagebutton:
            idle Transform(character_image("mara", "taquin"), zoom=1.00)
            hover Transform(character_image("mara", "rire"), zoom=1.00)
            focus_mask True
            xalign 0.61
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_MARA")

        imagebutton:
            idle Transform(character_image("elias", "neutre"), zoom=1.00)
            hover Transform(character_image("elias", "inquiet"), zoom=1.00)
            focus_mask True
            xalign 0.82
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_ELIAS")

    elif conclave_scene == 2:
        imagebutton:
            idle Transform(character_image("kael", "calme"), zoom=1.00)
            hover Transform(character_image("kael", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.28
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_KAEL")

        imagebutton:
            idle Transform(character_image("tomas", "neutre"), zoom=1.00)
            hover Transform(character_image("tomas", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_TOMAS")

        imagebutton:
            idle Transform(character_image("iris", "neutre"), zoom=1.00)
            hover Transform(character_image("iris", "blase"), zoom=1.00)
            focus_mask True
            xalign 0.72
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_IRIS")

    elif conclave_scene == 3:
        imagebutton:
            idle Transform(character_image("elen", "neutre"), zoom=1.00)
            hover Transform(character_image("elen", "inquiet"), zoom=1.00)
            focus_mask True
            xalign 0.18
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_ELEN")

        imagebutton:
            idle Transform(character_image("nyra", "neutre"), zoom=1.00)
            hover Transform(character_image("nyra", "reflexion"), zoom=1.00)
            focus_mask True
            xalign 0.39
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_NYRA")

        imagebutton:
            idle Transform(character_image("julian", "neutre"), zoom=1.00)
            hover Transform(character_image("julian", "reflexion"), zoom=1.00)
            focus_mask True
            xalign 0.61
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_JULIAN")

        imagebutton:
            idle Transform(character_image("sael", "neutre"), zoom=1.00)
            hover Transform(character_image("sael", "raison"), zoom=1.00)
            focus_mask True
            xalign 0.82
            yalign 1.00
            action Jump("_1_PNC_CONCLAVE_SAEL")


label _1_PNC_CONCLAVE:
    $ pnc_room = "day1_conclave"
    $ room_scene_indices["conclave"] = room_scene_current_number("conclave") or 1
    call screen day1_conclave_pnc()
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_PORTE:
    hide screen day1_conclave_pnc
    "La porte reste fermée."
    think "Sortir d'ici n'est visiblement pas une option."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_DEBARAS:
    hide screen day1_conclave_pnc
    "Je pose la main près du capteur."
    "Un bip sec répond aussitôt."
    think "Permission denied."
    think "Cette porte aussi est fermée..."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_FINISH:
    hide screen day1_conclave_pnc

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_115
    scene conclave2 at adaptive_fullscreen with fade
    "L'écran central du Conclave s'allume faiblement."
    think "On dirait que le système attendait qu'on l'observe."
    jump _1_KAMI_APPARITION


label _1_PNC_CONCLAVE_LYSA:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_116
    scene bg_conclave at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("lysa", "blase", 0.6),
    ])

    lysa blase "Surtout ne touche à rien sans prévenir."
    lysa colere "Ici, une erreur stupide pourrait tous nous tuer."
    noam "Comment tu le sens ?"
    lysa blase "Je préfère ne pas y penser. On verra ce que ça donne."
    hide lysa
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_RYN:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_117
    scene bg_conclave at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("ryn", "colere", 0.6),
    ])

    ryn colere2 "Cette porte me saoule."
    ryn colere "Et puis qu'est-ce qu'on fout là d'abord !"
    noam surpris "Hein ? Encore ça ?! Mais qu'est-ce que tu as à dire que tu ne sais pas ce qu'on fait là ?!"
    ryn "Et d'abord, c'était quoi votre soi-disant annonce de tout à l'heure ?!"
    ryn colere "Réponds-moi ! J'y pige que dalle !"
    noam panique "Mais tu as bien été sélectionné ?"
    ryn surpris "Hein ? Sélectionné ? Mais de..."
    noam surpris "Attends tu n'as vraiment pas entendu l'annonce ?!"
    noam panne "Elle a dû être diffusée partout dans le monde ! Sur tous les appareils ! Comment tu as pu passer à côté ?"
    ryn "Hein ? Moi j'étais près de la frontière quand on m'a attaqué..."
    noam colere "On t'a attaqué ?!"
    ryn colere "Ouais, ces connards m'ont foutu une sorte de serviette sur le nez et je me suis réveillé ici."
    ryn triste "Alors j'aimerais comprendre ce qu'il se passe ici !"
    noam reflechit "C'est assez dur à expliquer, même nous on ne sait pas grand-chose, Kami va sans doute nous en dire plus..."
    ryn colere "Donc on doit encore attendre après elle... Génial..."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_MARA:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_118
    scene bg_conclave at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("mara", "taquin", 0.6),
    ])

    mara taquin "Alors Monsieur je décide pour tout le monde, tu as trouvé une piste ?"
    noam reflechit "J'essaie déjà de comprendre où on est."
    mara taquin "Mauvaise nouvelle : on est dans une pièce fermée dans laquelle toutes les sorties sont bloquées."
    mara jaloux "C'est donc avec vous que je vais devoir passer mes trente prochains jours ici ?"
    mara rire "On devrait pouvoir bien s'amuser !"
    mara taquin "Ou plus, si affinité ?"
    noam peur "Hein ?!"
    mara rire_profond "Quelle réaction exquise !"
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_ELIAS:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_119
    scene bg_conclave at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("elias", "taquin", 0.6),
    ])

    elias reflechit "La ventilation a changé depuis tout à l'heure."
    elias ecoute "C'est léger, mais c'est certain, c'est plus la même depuis qu'on s'est réveillé."
    noam surpris "Hein ? Comment tu sais ça ?"
    elias neutre "C'est mon travail de savoir repérer ce genre de petit changement."
    noam reflechit "Maintenant que tu le dis, c'est vrai que la ventilation n'est plus la même."
    elias surpris "Ah, tu l'as remarqué toi aussi ?"
    noam sourire "On m'a souvent dit que j'avais une très bonne ouïe."
    elias ecoute "Intéressant à savoir !"
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_KAEL:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_120
    scene conclave2 at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("kael", "taquin", 0.6),
    ])

    kael reflechit "Si les portes sont bloquées par des permissions, ça veut dire que c'est le même système que sur Orbite."
    noam surpris "Hein ? qu'est-ce que tu racontes ? Tu viens d'Orbite ?"
    kael doute "Sur Orbite, tout le monde ne peut pas aller partout, t'imagines si un gamin va dans la salle de pilotage..."
    kael mefiant "Donc on a des systèmes de vérifications des autorisations par empreinte. Et ça ressemble à ce qui est installé sur les portes."
    noam panique "Donc on ne pourra jamais passer par ces portes ?"
    kael raison "C'est pas ce que j'ai dit, il suffit qu'on nous donne l'accès et on pourra y accéder."
    noam neutre "J'espère..."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_TOMAS:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_121
    scene conclave2 at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("tomas", "reflechit", 0.6),
    ])

    tomas reflechit "L'écran central... Il n'est pas éteint."
    noam surpris "Hein, mais il est tout noir ?"
    tomas hesitation "O-Ouais c'est vrai mais je suis quasiment sûr qu'il n'est pas éteint."
    tomas determine "Enfin, je veux dire, regarde..."
    "Il pointe du doigt des côtés de l'écran."
    tomas hesitation "Déjà il n'y a aucun bouton pour l'allumer ou l'éteindre."
    tomas reflechit "Habituellement sur les modèles RX-453, ce modèle de télévision on a des boutons pour pouvoir..."
    noam peur "Attends quoi ? Tu connais le modèle de la télévision par cœur ?!"
    noam taquin "T'es une sorte de geek ou quelque chose du genre ?"
    tomas gene "Hein ? Moi ? Ah... Non pas vraiment..."
    tomas gene "C'est juste mon travail de savoir ce genre de choses..."
    tomas determine "Enfin bref, pour faire simple d'habitude sur ce modèle il y a des boutons, là il n'y en a pas. Et évidemment on a pas de sortes de télécommande."
    noam surpris "Et c'est censé vouloir dire quoi ?"
    tomas raison "Qu'on ne peut pas éteindre cet écran. Il est en veille et peut se rallumer à tout moment."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_IRIS:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_122
    scene conclave2 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("iris", "triste", 0.6),
    ])

    iris desaccord "Je déteste les salles où tout le monde fait semblant de réfléchir calmement."
    iris triste "On est enfermés. Évidemment que tout le monde panique."
    noam taquin "Pourquoi ? Tu paniques ?"
    iris taquin "Moi ? Non. Et puis quoi encore ?! Je dis juste que vous pouvez montrer que vous êtes paniqués !"
    iris blase "Pas besoin de faire les hypocrites à jouer les durs."
    iris desaccord "Ce n'est pas ça qui ouvrira ces portes de toute façon."
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_ELEN:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave3") from _call_MAYBE_PLAY_SCRIPTED_DOOR_123
    scene conclave3 at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("elen", "joie", 0.6),
    ])

    elen surpris "Tu crois qu'ils ont prévu des pauses dans leur truc ?"
    noam neutre "Des pauses ?"
    elen triste "Bah oui. Moi, je ne veux pas travailler tout le teeeemps !"
    elen peur "Et j'ai besoin de trouver urgemment des toilettes..."
    noam triste "Je crois que nos envies, Kami s'en contrefout."
    elen joie "J'espère au moins qu'il y aura des trucs bons à manger !"
    hide elen
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_NYRA:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave3") from _call_MAYBE_PLAY_SCRIPTED_DOOR_124
    scene conclave3 at adaptive_fullscreen with fade
    
    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("nyra", "reflexion", 0.6),
    ])

    nyra reflexion "Tout le monde cherche une issue."
    nyra hesitation "Mais personne ne se demande encore pourquoi cette salle existe."
    noam "Tu as une idée ?"
    nyra sourire "Kami avait annoncé qu'on devrait voter sur des trucs ? Vu la salle, ça se fera ici."
    nyra raison "Peut-être qu'il faut chercher quelque chose en rapport avec ça ?"
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_JULIAN:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave3") from _call_MAYBE_PLAY_SCRIPTED_DOOR_125
    scene conclave3 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("julian", "reflexion", 0.6),
    ])

    julian reflexion "Le Conclave porte bien son nom."
    julian joie "Un cercle, des regards, une autorité invisible. Tout est pensé pour nous mettre en scène."
    noam "Tu crois que quelqu'un regarde ?"
    julian determine "JE dirais même : qui ne regarderait pas ?!"
    julian decontracte "L'avenir de l'humanité se joue ici ! La modification des lois se jouera ici !"
    julian joie "Tout le monde regardera ! Évidemment !"
    jump _1_PNC_CONCLAVE


label _1_PNC_CONCLAVE_SAEL:
    hide screen day1_conclave_pnc
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "conclave3") from _call_MAYBE_PLAY_SCRIPTED_DOOR_126
    scene conclave3 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("sael", "reflexion", 0.6),
    ])

    sael determine "Ma grand-mère disait qu'une salle silencieuse n'est jamais véritablement vide."
    noam surpris "Elle disait ça souvent ?"
    sael taquin "Seulement quand quelqu'un écoutait derrière les murs."
    noam triste "J'imagine qu'on peut dire avec Kami qu'il y a toujours quelqu'un qui écoute derrière les murs."
    sael triste "Mamie n'est plus physiquement là pour le dire mais elle avait souvent raison."
    jump _1_PNC_CONCLAVE


label _1_KAMI_APPARITION:

    elias surpris "Ah. C'est parti !"

    iris peur "Hein quoi ?!"

    elias taquin "La télévision va s'allumer."

    play sound sfx_gresillement
    $ shake(8, 0.25)

    voix "Diffusion centrale active."
    $ cam_move(0.5, 0.05, 3.00, 1.0)

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
    kami "Et puis je me suis dit que vous préféreriez commencer… doucement et confortablement."

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
    ryn colere "Qu'est-ce qu'on fout ici ?"

    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Du calme mon petit Ryn, c'est vrai que tu n'es pas au courant de tout..."
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
    elen desaccord "Attends, explique-moi, je suis larguée là."

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Des règles."
    kami "Celles qui encadrent ce monde."
    kami "Celles que vous respectez déjà, chaque jour."
    kami "Le bien et le mal, en somme."

    pause 0.4

    kami "Aujourd'hui, au cours de cette première journée…"
    kami "Chacun de vous proposera une modification."
    kami "On appellera ça un amendement."
    kami "Un seul."
    kami "Sur le commandement ou la règle de votre choix."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous pourrez renforcer une règle."
    kami "L'adoucir."
    kami "La tordre."
    kami "Ou l'habiller d'un joli mot pour faire croire que c'est une avancée."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vous êtes libres de proposer ce que vous voulez."
    kami "Et personne ne saura jamais qui a proposé quoi."
    kami "Vous êtes libres de ne penser qu'à vous ; ou à tous les autres."

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
    kami "Un vote. Ce sera simple, clair, binaire."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Pour ou contre."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais attention."
    kami "Pour qu'un amendement soit adopté… Il faut l'UNANIMITÉ !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    $ impact(10, 0.25, "#c81e2e")

    kami "Personne ne devra voter contre. Sinon le vote est refusé."

    pause 0.5

    $ bc_show("nyra", "triste", px=-70, py=-55, pz=0.85)
    nyra panne "Donc si une seule personne vote contre…"

    $ bc_hide()

    scene bg_diffusion_desespoir at adaptive_fullscreen with dissolve

    kami "Alors l'amendement est rejeté. Il disparaît."
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

    kami "Oh !"
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
    kami "Tout ce que vous faites est filmé et diffusé."

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

    kami "Le Conclave commence, je vous donne à tous les autorisations pour explorer librement le Conclave."
    kami "Les portes vous sont désormais ouvertes."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Faites connaissance."
    kami "Après tout, vous allez devoir vous supporter pendant un mois."

    pause 0.5

    # --------------------------------------------------------------------------
    # 2m10 — Total : ~26m40
    # --------------------------------------------------------------------------

    $ bc_off()
    play music "music/bgm_quiet_routine.mp3" fadein 0.4
    hide screen kami_broadcast_ui

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_127
    scene bg_conclave at adaptive_fullscreen with fade

    "L'écran s'éteint. Une seconde plus tard, les douze voix éclatent ensemble."

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
        ("iris", "neutre", 1.13),
    ])

    ryn colere "C'est quoi ce délire ?"
    elias panique "Attends, trente jours ? C'est chaud !"
    iris blase "On est pas sorti de l'auberge."

    noam reflexion "On va devoir vraiment passer trente jours ici…"

    lysa doute "L'unanimité. C'est adorable."
    lysa blase "La Diète polonaise avait déjà testé le veto individuel."
    lysa colere "C'est un système tellement tordu que rien ne pourra jamais aboutir."

    tomas raison "Ou alors... il faut faire des compromis. Enfin, pour une fois."

    nyra triste "C'est vrai que ça va être dur de tout le temps avoir l'unanimité."
    nyra neutre "Mais si c'est nous qui proposons les modifications, ce n'est pas impossible."

    elen joie "Mais on peut vraiment proposer n'importe quoi ? C'est énooorme !"

    lysa blase "Quelle naïveté..."

    mara rire "Vous parlez comme si on avait gagné au loto."
    mara taquin "On est toujours dans une cage, en train d'obéir aux règles de Madame."

    ryn colere "Attendez. Ici, les Commandements ne s'appliquent pas ?!"
    ryn colere "Si quelqu'un pète un câble, on fait quoi ?"

    iris reflexion "On est filmés en permanence. La pression publique est censée nous contenir."
    iris blase "Parce que la honte a toujours été un excellent protocole de sécurité. Aucun défaut connu."
    iris taquin "Quoique, certains ça ne les gêne pas tant que ça."

    think "Julian se lève, il ajuste sa veste et trouve une caméra avant de trouver ses mots."

    julian rire "Franchement ? Ce moment est historique."
    julian neutre "Enfin un lieu où nos paroles peuvent peser sur les règles."
    julian idee "Julian n'a pas l'intention de gaspiller cette scène."

    think "Il offre son meilleur profil à la caméra. Pour lui, ça semble avoir toute l'importance du monde."

    lysa doute "T'es sérieux ?"
    lysa colere "On nous enferme, on nous filme, on nous fait jouer les réformateurs sous peine de mort — et toi, t'es là en train de jouer au beau ?"
    lysa blase "Même Narcisse serait plus intéressant que toi."

    julian idee "Si nous devons rester ici trente jours, faisons-en sorte qu'ils comptent."
    julian idee "Tu peux me mépriser. Mais les gens, eux, ont besoin d'un résultat, ils veulent du CHANGEMENT."

    think "Il salue la caméra comme si le public l'attendait déjà."

    noam inquiet "…"

    tomas reflechit "Au moins, ça confirme quelque chose."
    tomas reflechit "Kami veut du spectacle. Vraiment."
    tomas raison "Et si elle veut du spectacle… C-C'est qu'elle compte sur le fait qu'on va se déchirer entre nous."

    pause 0.4

    noam reflexion "Donc aujourd'hui… on doit tous proposer quelque chose."

    lysa culpabilite "Ouais."
    lysa culpabilite "Et personne saura qui a proposé quoi."

    kael neutre "On pourrait partager les thèmes de ce qu'on propose ?"
    kael neutre "Histoire que personne ne propose des grosses dingueries."

    elen inquiet "Oh ! On peut commencer par une règle toute simple !"
    elen sourire "Genre : personne s'étripe avant le petit-déj. Après, idéalement personne s'étripe du tout, hein."

    pause 0.4

    noam reflexion "On y réfléchira plus tard. On ne sait toujours pas où nous sommes."
    noam neutre "Et puis ça nous laissera du temps pour réfléchir à ce qu'on voudrait modifier."

    lysa determine "Ouais, on devrait visiter."

    elen joie  "Je vais voir s'il y a une cantine ! Oh j'espère qu'il y aura des biscuits !"

    pause 0.4

    think "La salle se vide. À mon tour d'explorer cet endroit."
    $ hideGroup()

    scene expression "images/background/scene/couloir_dortoir.png" at adaptive_fullscreen with fade

    tuto "Prêt pour un nouveau tutoriel ?"
    tuto "J'espère bien !"
    tuto "Vous pouvez maintenant explorer manuellement les couloirs du Conclave."
    tuto "Toutes les pièces vous sont ouvertes afin que vous puissiez explorer chacune d'entre elles convenablement."
    tuto "Cliquez sur une porte pour entrer dans une salle, ou sur l'extrémité d'un couloir pour poursuivre votre chemin."
    tuto "Lorsque vous quittez une pièce, vous revenez dans le couloir qui mène à cette salle."
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

    $ _first_conclave_origin_room = room_key_from_pnc_room(getattr(store, "pnc_room", None))

    scene expression door_room_background(_first_conclave_origin_room) at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ current_period = "Après-midi"

    think "À force de me balader, j'ai fini par oublier l'heure."
    think "Ici, le temps a une façon de te faire croire qu'il s'est arrêté."
    think "Et puis non. Il avance. Lentement, mais il ne recule jamais."

    "Un écran mural grésille puis s'allume. Puis un autre. Et un autre encore."
    "Même signal, partout, identique."

    play sound sfx_announce volume 5.0

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il est bientôt dix-sept heures. Votre visite libre touche à sa fin."

    kami "J'espère que vous avez trouvé ça… Inspirant et complet."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "On a mis du cœur à l'ouvrage. VRAIMENT ! Je vous le promets !"
    kami "Enfin. On a surtout forcé quelques ingénieurs à travailler avec passion."
    kami "Mais vous n'êtes pas là pour apprendre ce qu'étaient les coulisses de ce Conclave, n'est-ce pas ?"
    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je vous attends avec hâte dans la Salle de Conclave."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Hop hop. Je suis déjà installée."
    kami "Popcorn virtuel en main."
    kami "Popcorn sucré évidemment ! Je me respecte."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ne me faites pas perdre mon temps."
    kami "C'est le seul truc que je ne vous pardonnerai pas."
    kami "Aaaaahhh, j'ai trop hâte que ça commence !"

    scene expression door_room_background(_first_conclave_origin_room) at adaptive_fullscreen with dissolve

    think "Voilà, on y arrive."
    think "À partir de là, le Conclave débute vraiment."
    think "Ce n'est plus possible de faire marche arrière."
    think "Enfin, ça n'a jamais été possible, mais bon…"

    $ current_scene_active = "FIRST_CONCLAVE_ELEN_INTERACT"
    $ _first_conclave_origin_label = corridor_room_label(_first_conclave_origin_room)

    if _first_conclave_origin_label is not None:
        jump expression _first_conclave_origin_label

    jump OPEN_CONCLAVE_MAP


label FIRST_CONCLAVE_ELEN_INTERACT:

    $ showGroup([
        ("noam", "reflexion", 0.3),
        ("elen", "joie", 0.6),
    ])

    elen joie "Noam ! Tu réalises qu'on est dans l'espace ?"
    elen joie "Dans l'espace ! Genre… pour de vrai !"

    noam reflexion "J'avais remarqué, oui."

    elen content "Mais c'est complètement fou ! Il suffit que je pense à tout ce vide sous nos pieds et j'ai envie de sautiller partout."
    elen joie "On voit la planète d'en haut, on flotte au milieu des étoiles, et tout le monde agit comme si c'était un couloir normal !"

    noam inquiet "Dit comme ça, le vide sous nos pieds est surtout rassurant."

    elen taquin "Ah non, fais pas cette tête ! C'est génial !"
    elen joie "J'ai toujours rêvé de voir l'espace. Je pensais juste pas que ça arriverait comme ça."
    elen content "Bon… Kami nous attend. On devrait y aller."
    elen joie "Mais quand même : on est dans l'espace !"

    return

label _1_KAMI_CONVOCATION_CONCLAVE:
    $ current_scene_active = "NONE"

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_128
    scene bg_conclave at adaptive_fullscreen with fade

    "Les portes du Conclave s'ouvrent ; dedans, il y a déjà plusieurs personnes."
    "On évite tous de se regarder, comme si on était gênés de quelque chose."
    "Personne n'a envie d'être le premier à parler, à briser ce silence."

    "La salle du Conclave n'a pas changé depuis tout à l'heure."
    "Et on est toujours insignifiants dans ce monde gigantesque."

    "Je m'assois et ceux déjà présents m'imitent."
    "Les autres arrivent par grappes. Des fauteuils raclent."
    "Mais personne ne parle. On attend."

    $ showGroup([
        ("ryn", "fatigue", 0.02),
        ("mara", "rire", 0.25),
        ("iris", "fatigue", 0.50),
        ("julian", "sourire", 0.75),
        ("elen", "inquiet", 0.98),
    ])

    ryn fatigue "On est tous là ?"
    ryn colere "Me dites pas qu'on va encore attendre pour rien."

    mara rire "Chuuut."
    mara rire "T'as capté ou quoi ?"
    mara rire "Kami supporte pas qu'on lui fasse perdre son temps, soi-disant."
    mara taquin "Et moi j'ai pas envie d'être sa cible du jour, alors merci, mais tais-toi."

    iris fatigue "Super. Vraiment super."
    iris fatigue "On nous convoque comme des mômes qui ont fait des conneries. Génial, l'ambiance."
    iris fatigue "J'ai hâte de voir qui va nous mettre au coin cette fois."

    julian sourire "Perso je trouve ça hyper marrant."
    julian sourire "J'ai trop envie de voir jusqu'où on peut aller dans cet endroit…"

    elen joie "On va réussir à changer les choses ! C'est sûr !"

    julian taquin "Exactement ! C'est ça qui est excitant."
    julian taquin "Si on peut réécrire les règles, on peut tout changer."
    julian taquin "Et sortir tout le monde de là. On SERA les héros de l'humanité !"

    "L'écran central s'allume et Kami apparaît."
    $ hideGroup()

    play sound sfx_announce volume 5.0

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Bonjour. Je vois que vous êtes tous arrivés. Mes douze petits représentants."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oh que ça faisait longtemps que j'en rêvais, de ce Conclave !"
    kami "C'était un travail monstre de tout organiser ! Vous n'imaginez même pas !"
    kami "Mais je pense que ça va valoir le coup !"

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais revenons à nos moutons. Je vais être claire."
    kami "Ici, dans le Conclave…"
    kami "les Commandements sont suspendus, abolis."
    kami "Toutes les règles que vous connaissiez jusque-là n'ont plus lieu d'être."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous êtes libres d'avoir la liberté absolue !"
    kami "Pas de commandement, pas de loi, pas de responsabilités ! C'est ça la belle vie !"
    kami "Juste vous et votre conscience, si vous en avez une."

    $ bc_show("ryn", "colere", px=-70, py=-50, pz=0.85)
    ryn "Ça, c'est censé nous rassurer ?"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oh qu'ils sont mignons les sourires qui commencent à poindre sur vos visages..."
    kami "Je me demande quel supplice... Pardon délice, vous venez d'imaginer !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Donc. Il n'y a plus de Commandements ici."
    kami "Mais il reste certaines règles."
    kami "Celles du Conclave. Alors ouvrez grand vos oreilles !"

    kami "Règle une."
    kami "Il est interdit de retourner dans votre district."
    kami "Il est interdit de quitter le district actuel, à savoir Orbite jusqu'à la fin du trentième jour."

    pause 0.2

    kami "Vous devrez rester ici. Avec moi."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "De toute façon, vous l'avez vu, comme on est dans l'espace, il n'y a pas beaucoup d'endroits où vous pourriez aller !"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Pendant trente petits jours, nous allons nous amuser ensemble."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Règle deux."
    kami "Il est interdit d'initier un contact vers l'extérieur."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Alors que je ne vous vois pas tripoter le matériel de communication !"
    kami "Si jamais quelqu'un vous appelle, vous pouvez répondre. Mais pas l'inverse."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Vous savez combien ça coûte les appels depuis l'espace ?!"
    kami "Non franchement, ne jouez pas aux idiots ou je vous ferai payer la facture !"

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Règle trois."
    kami "Vous êtes constamment filmés."

    think "Personne ne commente. Être filmés est la seule règle qui ressemble encore à notre quotidien."

    kami "Mais il y a une exception."

    $ bc_show("elen", "reflechit", px=-70, py=-50, pz=0.85)
    elen "Hein ? Une exception ?"
    $ bc_hide()

    kami "Vos chambres sont équipées d'un brouilleur. Il est activé par défaut."
    kami "Caméras, audio, capteurs : tout est coupé et rien ne va jusqu'à la cellule de diffusion."
    kami "Vous êtes filmés quand même, mais personne ne peut accéder aux images et aux sons, même moi !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Enfin... Pas pour le moment. Les images me deviennent accessibles une semaine après leur date d'enregistrement."
    kami "Mais rien ne pourra être diffusé si les brouilleurs sont actifs."
    kami "Après, rien ne vous empêche de le désactiver. Si vous aimez être vus, par exemple."

    $ bc_show("noam", "neutre", px=-70, py=-50, pz=0.85)
    noam "Mais qui ferait ça ?!"
    $ bc_hide()

    $ bc_show("julian", "joie", px=-70, py=-50, pz=0.85)
    julian "..."
    $ bc_hide()

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Maintenant."
    kami "On peut passer au cœur de ce Conclave."
    kami "Vous allez déposer chacun un amendement, c'est à dire une modification à un commandement ou une règle que vous voulez ajouter dans une urne."
    kami "Vous avez trente-cinq minutes pour chacun en déposer un."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "TOUT LE MONDE ! C'est bien compris ?!"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Et oui ! C'est presque comme un examen surprise. Oh et j'adore cette expression ! Presque comme... Désespérée..."
    kami "J'adore. J'espère que vous avez de l'inspiration."

    scene bg_diffusion_gene at adaptive_fullscreen with dissolve

    kami "Allez, je veux savoir ce que vous voulez changer dans mes règles parfaites !"
    kami "Qu'est-ce que j'aurais pu mal faire ? RIEN, ça c'est certain !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il y aura dix votes. Dix amendements tirés au sort. Pas un de plus."
    kami "Vous êtes douze."
    kami "Donc deux amendements ne seront pas votés lors de ce Conclave."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ne le prenez pas mal. C'est MATHEMATIQUE."
    kami "Et ce n'est pas plus mal, si jamais je devais reproduire le Conclave l'an prochain."
    kami "Je pourrais peut-être ajouter les amendements restants dans la prochaine urne !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Tous les trois jours. Un amendement sera tiré au sort."
    kami "Puis tous les trois jours, vous voterez sur cet amendement. Votre objectif : l'unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Comme je vous l'ai déjà dit : une seule voix contre et l'amendement est refusé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "La participation aux votes est libre. Libre à vous de venir voter, ou pas."
    kami "Sur les bulletins exprimés, il faut une unanimité de POUR pour adopter le vote."
    kami "Sont retirés des bulletins exprimés : les abstentions et les absences au vote."
    kami "Je ne suis pas un monstre, tout de même. MOI je respecte le principe du vote blanc."

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

    kami "Sur ce. Écrivez. Réfléchissez. Épatez-moi."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Faites semblant d'être des adultes responsables."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "L'urne ferme dans trente-et-une minutes."
    kami "Ne déposez pas vos propositions en retard."
    jump _1_CONCLAVE_DEBAT_DEPOT

# Durée : 3m30 — Total : ~56m15

# =============================================================================
label _1_CONCLAVE_DEBAT_DEPOT:
# =============================================================================

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_129
    scene bg_conclave at adaptive_fullscreen
    play music "music/bgm_system_override.mp3" fadein 1.0

    # --- Timer synchronisé avec le système day0 ---
    $ day0_timer_init(m=31, s=0)
    show screen day1_amendment_timer

    think "Trente-et-une minutes seulement."
    think "Pour faire des propositions qui peuvent réduire des villes en cendres."
    think "L'urne trône au centre de la pièce. Elle nous attend."

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

    kael calme "Bon, il faut qu'on se mette d'accord. On partage nos intentions, oui ou non ?!"
    kael colere "On a plus le temps de se balader et de parler de la pluie et du beau temps."

    iris fatigue "Ouais, nan, ça sert à rien."

    kael triste "Hein ?! Pourquoi ça ?"

    iris desaccord "Parce qu'un amendement peut sembler raisonnable en apparence et provoquer une catastrophe."
    iris taquin "Kami dira quoi ? Elle cherchera un responsable. Nous."
    iris desaccord "Et si tout le monde sait qui a déposé quoi..."

    kael colere "T'es vraiment en train de dire que tu ne veux pas qu'on assume nos actes ?"

    iris colere "Et alors ?!"
    iris desaccord "Je suis pas une politicienne moi ! Je sais même pas écrire ce truc-là d'amande je sais pas quoi !"
    iris colere "Et tu voudrais que je sois responsable ? C'est pas moi qui ai décidé tout ça hein !"

    noam calme "Je suis sûr que ce n'est pas ce qu'il a voulu dire..."

    sael determine "Une faute sans visage finit toujours par en emprunter un."
    sael determine "Si quelque chose tourne mal, l'un de nous portera ce visage, l'un de nous sera responsable aux yeux des gens."

    elen inquiet "Et puis tout le monde veut peut-être pas en parler, nooon ?"
    elen sourire "On a tous nos petits secrets, pas vrai ?"

    julian sourire "Moi je suis d'accord pour en parler. La transparence est le premier devoir d'un collectif."
    julian sourire "JE ne demanderai pas aux autres un courage que je me refuse à moi-même."

    mara neutre "Le type qui parle de lui quasi à la troisième personne craint de ne pas se faire remarquer. Adorable."
    mara taquin "Ton prénom, déjà ? Jules ? Justin ?"

    julian neutre "Julian. Mais ça tu le savais ma belle."
    mara rire "Ah ! Au moins, tu es marrant."

    pause 0.3

    ryn reflechit "Et si on touche à rien ?"
    ryn reflechit "On vote contre tout. Les règles restent connues, les mêmes qu'actuellement. Fin."

    nyra triste "Tu veux vraiment protéger le système actuel ? C'est peut-être le truc le moins risqué mais comment l'expliquer aux gens."
    nyra neutre " « Désolé on avait une chance de tout changer mais on avait peur du changement » ?"

    tomas hesitation "Ça ne marchera pas, Ryn. Enfin... pas forcément."
    tomas hesitation "Kami a dit qu'un refus pouvait aussi avoir des conséquences. On ne sait juste pas lesquelles..."

    pause 0.3

    kael reflechit "Raison de plus pour qu'on se parle !"
    kael reflechit "Si on fait tout ça tout seul dans notre coin, on va se retrouver avec des conneries sur le dos."

    lysa doute "Vous avez été choisis pour votre naïveté ou quoi ?!"
    lysa reflexion "Quelqu'un peut très bien annoncer une chose et écrire tout autre chose !"
    lysa taquin "Et avec deux textes jamais tirés, l'alibi est parfait."
    lysa colere "Il suffira de dire que notre texte n'a pas été choisi. Personne ne pourra le vérifier !"

    pause 0.4

    # --- Le chrono passe à 20 min (mise à jour dynamique) ---
    $ day0_timer_set(20 * 60)

    elias reflechit "Les gars... il reste vingt minutes. C'est chaud, là."

    pause 0.4

    ryn fatigue "Bon, écoutez, faites ce que vous voulez."
    ryn fatigue "Moi perso, je dépose le mien."

    play sound sfx_paper
    voix "Premier amendement déposé."
    play sound sfx_drop

    think "Voilà. Le premier."

    nyra reflexion "Tu savais déjà ce que tu voulais changer ?"

    mara sourire "Dès que l'un de nous fait le premier pas, les autres suivent rapidement."
    mara taquin "Ils ont tous commencé à griffonner des trucs. L'instinct de troupeau. Rudimentaire mais très élégant également."

    pause 0.3

    voix "Dépôt enregistré."

    sael neutre "Nous pouvons en parler jusqu'à la nuit. Chacun écrira ce qu'il croit être juste."
    sael neutre "Les morts savent mieux que nous combien la justice change de visage."

    play sound sfx_drop
    voix "Deuxième amendement. Troisième amendement."

    think "Plus personne ne débat vraiment."
    think "Nous ne sommes plus que quelques-uns sans avoir écrit. Personne ne cherche nos regards."

    kael calme "Bon, d'accord. Vous ne voulez pas bosser ensemble, j'ai compris."

    noam triste "Non attends Kael !"

    play sound sfx_paper
    think "L'urne se remplit, papier après papier, Kael a déposé le sien."
    play sound sfx_drop

    think "C'est ça le Conclave. Qui a pu vraiment croire que ce serait un lieu de débat et de discussion ?"

    elen inquiet "Et si quelqu'un met un truc vraiiiment horrible ?"
    elen inquiet "Genre le genre de surprise qui te coupe l'appétit. Ça existe, ça ?"

    iris fatigue "Alors on votera contre et on verra bien."

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

    think "Bon... Ok."
    think "Il faut que je me grouille. C'est à moi."

    think "Chaque papier qui tombe me rappelle que je traîne. Feuille blanche, stylo, vide au milieu de la poitrine."
    think "Un examen où une mauvaise réponse peut brûler une ville. Non, ça va, pas de quoi stresser. Vraiment..."
    think "Respire, Noam. T'as peur. Enfin, j'imagine qu'ils ont tous peur, n'importe qui dans cette situation flipperait grave."
    pause 0.3

    "Une idée me vient en tête."
    think "Reste à l'écrire. Juste l'écrire, sans tout gâcher."

    # --- MINIJEU : le brouillon de Noam (remplace le formulaire + le tracé urne) ---
    hide screen day1_amendment_timer
    call amendement_brouillon_play from _call_amendement_brouillon

    # --- Dépôt (sans tracé QTE) ---
    play sound "audio/sfx_announce.mp3"
    voix "Trente secondes avant fermeture de l'urne."

    think "Je me lève. Ma chaise racle le sol, seule voix dans la salle vide."
    think "L'urne paraît plus loin à chaque pas. Ma gorge se serre."

    play sound sfx_paper
    think "Je pousse la feuille dans la fente. Sale, pliée, ratée. Vivante."
    play sound sfx_drop
    $ impact(8, 0.2, "#3BCC82")
    voix "Amendement enregistré."
    call screen day1_urn_confirmation()
    think "Impossible de la récupérer. Tant mieux. Sinon je l'effacerais encore."

    pause 0.4

    think "Voilà. Mon premier amendement. Le dernier déposé, forcément."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_130
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

    play sound sfx_announce

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Les douze participations ont bien été enregistrées."
    kami "Il est dix-huit heures précises. Le temps imparti pour le dépôt des amendements est désormais écoulé."

    pause 0.2

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je suis ravie. Vraiment. Vous avez tous participé. Dans les temps. Sans exception."
    kami "C'est rare et particulièrement appréciable. Comme quoi, vous êtes peut-être plus efficaces que vos anciens élus !"

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Grâce à vous, je n'aurai pas besoin d'éliminer qui que ce soit aujourd'hui."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "le premier amendement soumis au vote sera tiré au sort demain matin, à neuf heures."

    pause 0.2

    kami "Je vous conseille d'être attentifs. Le hasard a parfois beaucoup de goût."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "En attendant. L'accès aux chambres est désormais ouvert."
    kami "Vous êtes libres de circuler. Oui, de manger aussi, ma petite Elen et surtout de vous reposer."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Profitez de votre douce nuit de tranquillité ! Demain, on recommencera à jouer tous ensemble."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_131
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Les écrans s'éteignent. Les chaises raclent le sol. Personne ne se dit vraiment au revoir."

    think "C'est fini. Pour aujourd'hui du moins."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_132
    scene couloir_dortoir at adaptive_fullscreen with fade

    think "Le couloir est calme. Presque normal, si on oublie l'urne capable de réécrire le monde derrière moi."

    think "J'ai déposé un amendement. On en a tous déposé un."
    think "J'espère ne pas avoir fait une connerie."
    think "Demain matin à neuf heures."

    pause 0.3

    think "Je m'arrête au milieu du couloir."
    think "Je n'ai pas vraiment envie de réfléchir."
    think "Mais j'ai pas envie de rester seul avec ça en tête non plus."

    menu:
        "Que devrais-je faire ?"

        "Aller se coucher":
            $ choix_1_soir = "dormir"
            think "J'ai besoin de m'allonger."
            think "Même si je sais que je ne dormirai pas tout de suite."
            think "Juste… Me couper un peu du monde et rester au calme, loin de toute cette agitation."

            jump _1_FIN_JOURNEE_DORTOIR

        "Se rendre à la salle de repos (Optionnel)":
            $ choix_1_soir = "salle_repos"
            think "Je devrais aller à la salle de repos."
            think "Peut-être que quelqu'un y sera. Ou peut-être pas."
            think "Dans les deux cas… ça me fera du bien."

            jump _1_SALLE_DE_REPOS_OPTIONNELLE

# Durée : 1m — Total : ~1h 1m 15s


# =============================================================================
label _1_SALLE_DE_REPOS_OPTIONNELLE:
# =============================================================================

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_133
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Lumière douce, canapés presque vides. La salle de repos mérite presque son nom."

    pause 0.2

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("julian", "detendu", 0.22),
        ("nyra", "sourire", 0.50),
        ("mara", "sourire", 0.78),
    ])

    julian detendu "Ah. Toi non plus, tu n'as pas réussi à te coucher ?"

    think "Évidemment..."

    nyra sourire "Ah, Noam ? Qu'est-ce qui t'amène ici ? Tu ne voulais pas supporter le silence de ta chambre, ou ces reproches qu'on se fait tous au fond de nous ?"

    noam sourire "Ouais, me poser un coup me fera du bien. Cette journée était stressante..."

    think "Julian se laisse tomber dans un fauteuil avec juste assez de bruit pour rester au centre de la scène."

    julian detendu "J'ai réécrit ma proposition trois fois. TROIS FOIS. Tu imagines ?!"
    julian sourire "Ce genre de phrase peut rester dans l'Histoire."
    julian detendu "JE refuse de ne pas y entrer à cause d'une mauvaise formulation !"

    mara sourire "Moi, j'ai pu écrire ce que je voulais. C'est une expérience assez nouvelle."
    mara taquin "Si ça vous plaît, je prends les compliments. Sinon, je prends quand même un verre."

    julian detendu "Nous écrivons pour des millions de personnes, puis le hasard décide si nos idées existeront lors du tirage au sort."
    julian inquiet "Imaginez que ma proposition reste dans l'urne. Un moment pareil, perdu avant même d'avoir été entendu. Non, impossible !"

    nyra taquin "Tu veux être utile, ou tu veux être entendu ?"
    julian detendu "Les deux ne s'opposent pas."
    nyra sourire "Je n'ai pas dit qu'ils s'opposaient."

    pause 1.0

    mara sourire "Vous croyez qu'elle nous regarde, là ? J'espère que mon profil est du bon côté."

    julian detendu "Sûrement. Et tant mieux. Contenter un public attentif, ça demande beaucoup de travail."
    mara taquin "Bien sûr. C'est pour ça que tu vérifies la caméra toutes les trente secondes. Par responsabilité bien sûr."

    julian joie "Avoue juste que tu es jalouse car tout le monde me préfèrera à toi !"
    mara sourire "Ah ! Dans tes rêves, jamais tu ne vaincras mon charme !"

    "Malgré la tension de la journée, l'ambiance est plutôt chaleureuse."
    think "Ça fait vraiment du bien..."

    play sound sfx_door
    $ hideGroup()

    scene bg_cg010 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")
    show screen kami_broadcast_ui

    "La porte s'ouvre. Tomas apparaît avec un plateau chargé de six tasses."

    tomas hesitation "Euh… Bonsoir."
    tomas hesitation "J'ai entendu du bruit ici, alors..."

    mara sourire "Attention, tout le monde. Opération à haut risque !"

    $ bc_show("julian", "detendu", px=-70, py=-50, pz=0.85)
    julian detendu "Voilà une entrée que je respecte. Et un ravitaillement plus que bienvenu !"

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra sourire "Tu veux qu'on libère la table, ou tu préfères réussir seul ?"
    $ bc_hide()

    tomas hesitation "Si je renverse ça maintenant, enfin... j'irai vivre sous une table jusqu'au trentième jour, mort de honte."
    $ bc_show("mara", "content", px=-70, py=-50, pz=0.85)
    mara sourire "Oh ! Y'a pire."
    mara taquin "Tu pourrais être mort tout court."
    $ bc_hide()

    mara sourire "Il reste une place ici."

    "Mara tapote du bout des doigts le canapé à côté d'elle."

    tomas hesitation "Je me suis dit que…"
    tomas hesitation "…que ça ferait peut-être du bien."
    tomas hesitation "Un truc chaud. Juste… un truc chaud."
    tomas gene "Je savais pas combien on allait être alors j'en ai pris quelques-uns..."
    tomas "Voilà. Rien de cassé. Enfin, pas encore."

    $ bc_show("julian", "joie", px=-70, py=-50, pz=0.85)
    julian detendu "Un vrai héros. Et sans discours, en plus. C'est presque vexant."
    $ bc_hide()

    pause 0.3

    scene bg_cg010_1 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg010")

    think "Les tasses circulent rapidement. La vapeur transforme la table en refuge provisoire."
    think "Ça sent le thé. Un vrai thé bien fort comme il faut. Pas un truc synthétique."

    nyra vide "Ça vous manquait aussi ? Tenir quelque chose de chaud."

    mara vide "Ouais… C'est débile mais ça fait du bien. Un tout petit peu."
    mara vide "Oh et puis ce thé ! Mon dieu qu'il est exquis !"

    tomas "O-Ouais... J'en avais jamais bu d'aussi bon !"

    mara "Tu m'étonnes, un thé comme ça, ça valait une blinde à l'époque !"

    julian "Je vois que Madame a déjà eu l'occasion de goûter à de tels mets !"

    mara "Ah ! Ne fais pas ta jalouse mon petit Julius !"

    julian "C'est JU-LIAN !"

    mara "Ouais, si tu le dis !"

    pause 2.0

    "L'ambiance retombe un peu."
    tomas vide "Demain… À neuf heures on saura…"

    julian vide "Ouais. Demain. Mais c'est encore loin !"
    julian "Alors ne brise pas l'ambiance ! Tu as ramené les boissons, ne gâche pas ce moment !"

    pause 0.4

    think "On boit en silence. Je sais pas combien de temps ce calme durera."
    think "Mais là, en ce moment… C'est agréable."
    think "Les tasses se vident. La dernière reste sur le plateau, intacte."

    mara vide "Bon bah voilà. C'était sympa."
    mara vide "Je vais aller essayer d'aller me pieuter avant de péter un câble."

    nyra vide "Moi aussi. Avant de recommencer à réfléchir."
    nyra "Et je t'avoue que j'espère avoir des douches dans la chambre !"

    julian "Ouais, clairement !"
    julian vide "Excellente idée."

    think "Ils se lèvent un à un. La parenthèse se referme."
    think "Je reste quelques secondes, la tasse vide, encore à moitié chaude, entre les mains."
    think "Je devrais y aller aussi."

    $ hideGroup()
    jump _1_FIN_JOURNEE_DORTOIR

# Durée : 1m55 — Total : ~1h 3m 10s

# =============================================================================

label _1_FIN_JOURNEE_DORTOIR:
# =============================================================================

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_134
    scene couloir_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "Ça y est. La journée est finie. Enfin… presque. Je continue de marcher sans m'attarder sur mes pensées."

    pause 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_135
    scene couloir_dortoir at adaptive_fullscreen with fade
    pause 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_136
    scene bg_dortoir at adaptive_fullscreen with fade

    think "La lumière du dortoir est plus chaude, moins clinique. Elias est déjà là."

    $ showGroup([
        ("elias", "detendu", 0.22),
        ("noam", "neutre", 0.78),
    ])

    if choix_1_soir == "salle_repos":

        elias detendu "Ah, toi aussi t'es encore debout. C'est chaud de dormir après ça."

        noam neutre "Ouais."
        noam neutre "J'avais pas trop envie de rester seul."

        elias detendu "Je vois. T'étais à la salle de repos, hein ? C'est pas con."

        noam neutre "Ouais."

        elias detendu "Moi j'ai tenté de dormir direct. Raté."

    if choix_1_soir == "dormir":

        elias detendu "En voilà un qui se couche tôt. Tu voulais rester seul ?"

        noam neutre "On peut dire ça."
        noam neutre "Drôle de journée, me reposer me fera du bien."

    pause 0.2

    think "Son sourire est franc. Fatigué, mais franc."

    elias detendu "C'est chaud quand même. J'ai rien porté, rien monté, et je suis rincé comme après douze heures d'usine."

    noam neutre "Ouais. C'est clair. C'était une journée épuisante..."

    elias inquiet "Demain matin, ça va être chaud pour de vrai."

    noam neutre "Ouais. M'en parle pas..."

    think "On n'insiste pas. Pas besoin."

    elias jaloux "Bonne nuit, Noam."

    noam neutre "Bonne nuit."

    pause 0.3
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_137
    scene bg_chambre at adaptive_fullscreen with fade

    think "Ma chambre est étrangement assez confortable."
    think "Enfin seul. Je jette presque mes affaires et découvre un grand lit, une garde-robe..."
    think "Non, ce sont MES affaires ! Du matériel informatique. Près du bureau, un boîtier pulse en vert : le brouilleur."

    menu:
        "Que dois-je faire ?"

        "Ouvrir l'interface du brouilleur":
            call day1_play_trace(path_type="arc", time_limit=5.5, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=560, required=False) from _call_day1_trace_jammer
            if _return:
                call screen day1_jammer_panel()
                if noam_room_jammer_on:
                    think "La diode reste verte. Les règles présentent l'intimité dans la chambre comme une permission accordée."
                else:
                    think "La diode passe au rouge. La chambre paraît plus grande, et beaucoup moins à moi."
            else:
                think "Le capteur refuse mon geste. Je retire la main avant d'insister."

        "Laisser le brouilleur tranquille":
            think "Je garde la diode verte dans un coin de mon regard."
            think "S'il est actif par défaut, je vais le laisser actif."

    think "Il y a une salle de bain privée. Une douche chaude est la première décision simple de la journée."

    pause 0.2

    scene bg_cg011 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg011")

    play sound sfx_shower

    think "L'eau chaude coule longtemps. Je laisse le stress de la journée s'évaporer."
    think "Pas ce soir. Je réfléchirai demain."

    pause 0.5

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_138
    scene bg_chambre at adaptive_fullscreen with fade

    think "Je m'allonge. Le lit est plus confortable que prévu."
    think "Mon amendement est déposé. Le reste ne m'appartient plus."
    think "Le plafond est immobile."

    $ blink()

    pause 0.4

    $ blink()

    pause 0.4

    $ blink()

    think "Étrangement, malgré le stress, cette journée était crevante. Je ne vais pas tarder à dormir. Enfin, je l'espère."

    $ blink()

    scene black with fade
    stop music fadeout 2.0

    call end_day("2") from _call_end_day_21

    jump _2_CANON

# Durée : 1m40 — Total : ~1h 4m 50s


# =============================================================================
# LABEL trace QTE jour 1
# =============================================================================

label day1_play_trace(path_type="curve_right", time_limit=6.0, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True):

    call trace_qte_run(mg_id="trace_day1", title="SYNCHRONISATION MOTRICE", path_type=path_type, time_limit=time_limit, wait_time=wait_time, tolerance=tolerance, max_errors=max_errors, anchor_x=anchor_x, anchor_y=anchor_y, required=required) from _call_day1_play_trace_trace_qte
    $ fix_stale_return_label(day1_trace_return_label(path_type, anchor_y))
    return (_return != "FAIL")

# Total J1 + exploration des salles : 44m30
