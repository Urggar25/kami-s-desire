# --------------------------------------------------------------------------------------------
# JOUR 10_0_1_1 — Matinée lourde
#
# Refonte :
# - suppression complète du minijeu de tension à table
# - enquête active sur trois relais de ventilation précis
# - anomalies progressives sans explication directe
# - retour vers Elias interrompu par l'annonce de Kami
# - l'explication de Kami ne couvre pas les anomalies relevées
# - mini-interrogatoire au Conclave pour vérifier les alibis
# - aucune révélation directe sur ce que Noam a vu
# --------------------------------------------------------------------------------------------

default j10011_waiting_elias = False
default j10011_cafeteria_done = False
default j10011_walk_choice = None

default j10011_relays_checked = []
default j10011_relay_order = []
default j10011_relay_archives_checked = False
default j10011_relay_gym_checked = False
default j10011_relay_infirmary_checked = False

default j10011_alibis_checked = []
default j10011_alibi_done = False


label _10_0_1_1_REVEIL_CHAMBRE:

    scene black

    $ current_day = 10
    $ j10011_cafeteria_done = False
    $ j10011_waiting_elias = False
    $ j10011_relays_checked = []
    $ j10011_relay_order = []
    $ j10011_relay_archives_checked = False
    $ j10011_relay_gym_checked = False
    $ j10011_relay_infirmary_checked = False
    $ j10011_alibis_checked = []
    $ j10011_alibi_done = False
    $ cafeteria_food_level = "medium"
    $ current_period = "Matin"

    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    $ blink()

    think "Je me réveille avant l'annonce, avec la tête lourde, la bouche sèche et cette sensation désagréable d'avoir dormi dans une pièce trop petite."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Quand je repousse le drap, la chaleur me saute au visage avec assez de violence pour me faire regretter le geste."
    "L'air est lourd, presque immobile, et ma chemise me colle déjà au dos alors que je viens à peine de me lever."

    think "La température est censée être régulée partout. Si ma chambre chauffe comme ça, ce n'est pas juste une mauvaise nuit."

    "Je reste un moment assis au bord du lit, les coudes sur les genoux, à écouter le couloir derrière la porte."
    "Après le vote d'hier, je m'attendais à entendre des portes claquer, des disputes, quelqu'un marcher trop vite ou parler trop fort."

    think "Mais il n'y a rien. Pas le moindre éclat de voix, pas même ces bruits inutiles qu'on finit par ne plus entendre quand tout va à peu près bien."

    "Je finis par enfiler ma veste malgré la chaleur et je sors."

    stop music fadeout 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_25
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    "Le couloir est encore plus étouffant que ma chambre. Une porte s'entrouvre au fond, reste ainsi une seconde, puis se referme dès que j'avance."

    think "Personne n'a envie de croiser les autres. Moi non plus, mais si quelqu'un sait déjà quelque chose sur hier, ce sera à la cafétéria."

    $ j10011_waiting_elias = True
    $ free_time_active = False
    $ free_time_next_label = None
    $ exploration_libre_active = True
    $ exploration_libre_next_label = None
    $ exploration_libre_seen_rooms = []
    $ exploration_libre_required_visits = 0
    $ exploration_libre_allowed_rooms = ["cafeteria"]
    $ exploration_libre_title = "Rejoindre la cafétéria"
    $ sync_character_links_from_persistent()
    $ conclave_lock = False
    $ dortoir_lock = False

    think "Je devrais aller manger quelque chose, ou au moins essayer."

    jump START_EXPLORATION_LIBRE_MAP


label _10_0_1_1_CAFETERIA_ELIAS:

    $ j10011_waiting_elias = False
    $ free_time_active = False
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_26
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2

    $ showGroup([
        ("noam", "inquiet"),
        ("elias", "fatigue"),
        ("mara", "stress"),
        ("ryn", "colere"),
        ("nyra", "reflechit"),
    ])

    "La cafétéria est presque pleine, mais elle n'a rien de vivant. Les conversations repartent par petits morceaux avant de s'interrompre chaque fois qu'une nouvelle ligne apparaît sur l'écran d'information."
    "Elias, Mara et Nyra sont installés au fond. Ryn, lui, reste debout derrière une chaise, les deux mains serrées sur le dossier."

    elias inquiet "Noam... T'as vu l'écran ?"

    noam inquiet "Non. Je viens de me lever. Qu'est-ce qu'il y a ?"

    mara agace "Assieds-toi avant qu'il soit obligé de le répéter une quatrième fois, sinon il va finir par réciter le communiqué en dormant."

    noam hesitation "D'accord..."

    "Je tire une chaise et m'installe. Elias attend une seconde, les yeux fixés sur son plateau, puis reprend."

    elias fatigue "Ils disent que la majorité des campements se sont dispersés avant la fin du délai."
    elias inquiet "C'est tout. Pas de liste, pas de chiffre précis, pas de bilan. Juste cette phrase."

    nyra reflechit "Durant le vote, Kami a accepté plusieurs déclarations préalables."
    nyra raison "Ceux qui ont transmis un registre complet avant la fin du compte à rebours ne pouvaient plus être considérés comme des campements clandestins."

    ryn colere "Tu peux pas raconter ça comme s'ils avaient tranquillement rempli un formulaire."

    nyra reflechit "Je ne raconte rien. Je répète ce que nous savons."

    ryn colere "Ils ont fui avec ce qu'ils avaient sur le dos, Nyra. Ils se sont dispersés parce qu'un Canon était braqué sur eux, pas parce qu'ils avaient soudain envie de régulariser leur situation."

    nyra raison "Je sais."

    ryn colere "Non, tu sais ce que dit l'écran. Moi, j'essaie de penser à ceux qui ont pas couru assez vite."

    mara stress "Ryn..."

    ryn colere "Quoi ? Ça te coupe l'appétit ?"

    mara colere "Non. Ça me donne surtout envie que t'arrêtes de parler comme si on avait oublié ce qui s'est passé."

    elias inquiet "On peut éviter de se bouffer entre nous pendant cinq minutes ? Juste cinq."

    "Ryn lâche enfin le dossier, mais il ne s'assoit pas. Sa colère ne retombe pas vraiment ; elle change simplement de place."

    noam triste "On ne sait pas combien de personnes ont réussi à partir, mais le délai a servi à quelque chose."

    ryn colere "Je sais."

    noam hesitation "Alors pourquoi tu me regardes comme si je venais de dire l'inverse ?"

    ryn fatigue "Parce que j'ai pas envie d'entendre que ça s'est bien terminé."

    "Personne ne répond tout de suite. Même Mara baisse les yeux."

    elias fatigue "Quand j'ai lu « majorité dispersée », j'ai été soulagé."

    mara stress "Moi aussi."

    elias inquiet "Une seconde seulement, mais... ouais."

    mara agace "Tu croyais être le seul connard de la table ?"

    elias fatigue "Ça aurait été rassurant."

    nyra raison "On demandera les chiffres complets. Les déclarations déposées, les zones évacuées et celles qui ne répondent plus."

    ryn reflechit "Je viens avec toi."

    nyra reflechit "Je m'en doutais."

    ryn colere "C'était pas une demande."

    nyra raison "Je sais."

    "La conversation s'éteint d'elle-même. L'écran continue de faire défiler les mêmes mots, comme s'il suffisait de les répéter pour qu'ils deviennent plus précis."

    elias fatigue "Je vais bouger un peu."

    mara stress "Pour aller où ?"

    elias fatigue "N'importe où tant qu'il y a des vis, des câbles et personne pour me demander ce que je ressens."

    noam taquin "Ça réduit pas mal le choix."

    elias fatigue "La maintenance. Au moins les machines savent fermer leur gueule."

    "Il se lève avec son plateau presque intact et quitte la cafétéria sans attendre de réponse."

    $ hideGroup()

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    think "Je baisse les yeux vers mon propre plateau. J'ai faim, mais chaque bouchée paraît trop sèche et trop chaude."

    "Je reste encore quelques minutes avec les autres avant de repousser ma chaise."

    jump _10_0_1_1_MARCHE_APRES_TABLE


label _10_0_1_1_MARCHE_APRES_TABLE:
    $ current_period = "Après-midi"

    stop music fadeout 1.5
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_29
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.2

    "Dès que la porte se referme derrière moi, le peu de fraîcheur de la cafétéria disparaît."
    "Le couloir semble encore plus chaud qu'avant. L'air vibre légèrement au-dessus des plaques métalliques, comme au-dessus d'un radiateur."

    think "Elias est parti en maintenance. Ce n'est pas vraiment une destination, mais c'est mieux que de tourner en rond."

    "Je prends la direction qu'il a empruntée quelques minutes plus tôt."

    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_30
    scene bg_maintenance at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "fatigue"),
        ("elias", "fatigue"),
    ])

    "Elias est accroupi devant un coffret ouvert. Un outil lui échappe des mains et roule sous une armoire ; il le regarde disparaître sans même essayer de le retenir."

    elias fatigue "Ouais. Reste là-dessous. Très bonne idée."

    noam taquin "Je vous laisse régler ça entre vous ? Toi et le sol ?"

    elias fatigue "Non. Reste. Lui, il a déjà gagné."

    "Il se penche enfin, récupère l'outil et retourne devant le coffret."

    noam reflexion "Tu répares quoi ?"

    elias reflechit "Un relais de ventilation. Il faisait un bruit bizarre."

    noam reflexion "Il était vraiment en panne ?"

    elias fatigue "J'ai dit qu'il faisait un bruit bizarre."

    noam hesitation "Donc non."

    "Il serre la mâchoire, replace l'outil contre une vis et manque encore son geste."

    elias colere "Tu veux quoi, Noam ? Que je retourne m'asseoir là-bas et que je fasse un discours sur mes sentiments ?"

    noam raison "Non."

    elias colere "Parce que je me sens coupable, voilà. Super. Maintenant, ce relais peut continuer à faire son bruit de merde ?"

    noam triste "T'as été soulagé qu'ils soient pas tous morts. Je vois pas ce qu'il y a de dégueulasse là-dedans."

    elias fatigue "Je sais. Enfin... je crois."

    "Il inspire comme s'il voulait continuer, puis un déclic sec résonne dans les gaines au-dessus de nous."
    "Le souffle de la ventilation s'arrête d'un seul coup."

    elias inquiet "Putain..."

    noam reflexion "C'était toi ?"

    elias inquiet "Non."

    "Il se relève immédiatement et fixe le petit écran du coffret. Des lignes de texte défilent, disparaissent, puis laissent place à un message unique."

    "FLUX PRINCIPAL — INDISPONIBLE"

    elias inquiet "Non, non, non..."

    noam reflexion "La clim est en panne ?"

    elias reflechit "J'en sais rien. Mais ça devrait pas se couper comme ça."

    "Il tape rapidement sur le clavier intégré. L'écran clignote, affiche brièvement plusieurs valeurs, puis revient au même message."

    elias inquiet "Pas d'alarme. Pas de notification. Rien."

    noam hesitation "Kami ?"

    elias reflechit "Possible, mais d'habitude elle nous le ferait savoir. Elle adore annoncer quand elle touche à quelque chose."

    "Il rouvre le coffret et contrôle les branchements un par un."

    elias reflechit "Le relais répond. L'alimentation aussi. C'est le flux qui manque."

    noam reflexion "Donc quelque chose bloque ailleurs."

    elias reflechit "Peut-être. Il y a trois relais secondaires accessibles : archives, gymnase et infirmerie."

    noam reflexion "Je vais les vérifier."

    elias inquiet "Regarde l'écran, la grille et le conduit. Si les trois racontent la même chose, tu reviens me voir."

    noam hesitation "Et toi ?"

    elias fatigue "Je reste ici pour comprendre pourquoi ce machin affirme qu'il fonctionne alors que plus rien ne souffle."

    "Un nouveau déclic passe dans la gaine, plus loin cette fois. Aucun courant d'air ne revient."

    elias inquiet "Et Noam... si tu vois un truc qui n'a aucun sens, tu touches à rien. Tu reviens."

    noam reflexion "Ça inspire confiance."

    elias fatigue "C'est exactement l'effet recherché."

    $ hideGroup()

    think "Trois relais. Archives, gymnase, infirmerie. Au moins cette fois, j'ai une raison de tourner dans les couloirs."

    tuto "(Inspecte les trois relais de ventilation. Tu peux les vérifier dans l'ordre de ton choix.)"

    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_ENQUETE_CLIM:

    if len(j10011_relays_checked) >= 3:
        jump _10_0_1_1_RETOUR_ELIAS

    scene couloir_maintenance at adaptive_fullscreen with dissolve

    "Je m'arrête à l'intersection des couloirs. Sans ventilation, le silence porte beaucoup plus loin que d'habitude."

    menu:
        "Quel relais vérifier ?"

        "Relais des Archives" if not j10011_relay_archives_checked:
            jump _10_0_1_1_RELAIS_ARCHIVES

        "Relais du Gymnase" if not j10011_relay_gym_checked:
            jump _10_0_1_1_RELAIS_GYMNASE

        "Relais de l'Infirmerie" if not j10011_relay_infirmary_checked:
            jump _10_0_1_1_RELAIS_INFIRMERIE


label _10_0_1_1_RELAIS_ARCHIVES:

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_j10011_archive_relay
    scene bg_archive at adaptive_fullscreen with dissolve

    "Le relais des archives est fixé dans une niche au-dessus d'une grille basse. Une diode verte clignote à intervalle régulier."

    menu:
        "Qu'est-ce que je vérifie d'abord ?"

        "L'écran":
            "L'affichage indique un flux stable et une ouverture de vanne presque maximale."
            think "Donc, d'après lui, tout fonctionne."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE

        "La grille":
            "Je place ma main devant la grille. Pas un souffle, même pas un courant d'air tiède."
            think "Super."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE

        "Le conduit":
            "Le métal est plus chaud que prévu. Pas brûlant, mais assez pour que je retire la main presque aussitôt."
            think "Quelque chose circule là-dedans, ou alors quelque chose chauffe."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE


label _10_0_1_1_RELAIS_ARCHIVES_SUITE:

    "Je vérifie le reste avant de repartir."
    "L'écran affirme toujours que le flux est actif, la grille ne souffle rien et le conduit continue de chauffer."

    think "Un relais qui fonctionne parfaitement, sauf pour la partie où il est censé ventiler."

    $ j10011_relay_archives_checked = True
    $ j10011_relays_checked.append("archives")
    $ j10011_relay_order.append("archives")

    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RELAIS_GYMNASE:

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_j10011_gym_relay
    scene bg_gymnase at adaptive_fullscreen with dissolve

    "Le gymnase est vide. L'odeur de caoutchouc et de métal paraît plus forte sans le souffle constant de la climatisation."
    "Le relais est derrière une protection transparente, juste à côté d'une large bouche d'aération."

    menu:
        "Qu'est-ce que je vérifie d'abord ?"

        "L'écran":
            "Le relais annonce une pression correcte, puis la valeur tombe à zéro pendant une fraction de seconde avant de revenir exactement à la valeur précédente."
            think "J'ai peut-être cligné des yeux au mauvais moment."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE

        "La grille":
            "Je tends la main devant la bouche d'aération. Rien."
            "En approchant davantage, j'entends pourtant un léger ronflement derrière la grille, comme si un moteur tournait beaucoup plus loin."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE

        "Le conduit":
            "Le conduit vibre très faiblement sous mes doigts, puis s'immobilise au moment précis où je m'en rends compte."
            think "..."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE


label _10_0_1_1_RELAIS_GYMNASE_SUITE:

    "Je contrôle les autres éléments."
    "Même résultat : des valeurs normales, aucun souffle, et ce ronflement trop faible pour savoir s'il vient réellement du conduit."

    if len(j10011_relays_checked) >= 1:
        think "Ça commence à faire beaucoup de systèmes « normaux » qui ne font pas ce qu'ils affichent."

    $ j10011_relay_gym_checked = True
    $ j10011_relays_checked.append("gymnase")
    $ j10011_relay_order.append("gymnase")

    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RELAIS_INFIRMERIE:

    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "infirmerie1") from _call_j10011_infirmary_relay
    scene infirmerie1 at adaptive_fullscreen with dissolve

    "Le relais de l'infirmerie est encastré dans le mur du couloir intérieur. Sa diode reste verte, immobile."
    "Je m'approche et l'écran s'allume avant même que je le touche."

    menu:
        "Qu'est-ce que je vérifie d'abord ?"

        "L'écran":
            "FLUX : ACTIF."
            "TEMPÉRATURE : 31.4 °C."
            "PRESSION : NORMALE."
            "Je reste quelques secondes devant les valeurs. Une ligne supplémentaire apparaît si vite que je ne suis pas certain de l'avoir vraiment lue."
            "Puis l'écran revient à son affichage normal."
            think "..."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE

        "La grille":
            "Aucun souffle."
            "Quand je retire ma main, quelque chose frappe doucement dans la gaine, une seule fois, suffisamment loin pour que je ne sache pas d'où vient le bruit."
            think "Un clapet. Probablement."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE

        "Le conduit":
            "Le métal est chaud."
            "Je laisse mes doigts dessus une seconde de plus et une vibration courte traverse la paroi, comme un mouvement transmis depuis un autre conduit."
            "Quand je retire la main, tout s'arrête."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE


label _10_0_1_1_RELAIS_INFIRMERIE_SUITE:

    "Je vérifie les deux autres éléments."
    "Le relais maintient que tout est normal. Pourtant la grille reste parfaitement silencieuse."

    if len(j10011_relays_checked) == 2:
        think "Les trois relais disent la même chose. Ce n'est pas une panne locale."

    elif len(j10011_relays_checked) == 1:
        think "Deux relais, deux affichages normaux, et toujours aucun air."

    else:
        think "Si les autres affichent la même chose, Elias avait raison de s'inquiéter."

    $ j10011_relay_infirmary_checked = True
    $ j10011_relays_checked.append("infirmerie")
    $ j10011_relay_order.append("infirmerie")

    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RETOUR_ELIAS:

    scene couloir_infirmerie at adaptive_fullscreen with dissolve

    "Je recompte mentalement les trois relais en quittant le dernier secteur."
    "Archives. Gymnase. Infirmerie."
    "Trois écrans qui prétendent que le système fonctionne, trois grilles qui ne soufflent rien."

    think "Je dois retourner voir Elias."

    "Je fais quelques pas, puis je ralentis sans comprendre pourquoi."

    jump _10_0_1_1_DOPPELGANGER


label _10_0_1_1_DOPPELGANGER:

    scene couloir_infirmerie at adaptive_fullscreen with dissolve

    "Le couloir est vide, mais quelque chose dans sa profondeur accroche mon regard."
    "Je ne saurais pas dire quoi. Une forme, une différence de lumière, peut-être seulement l'impression qu'un détail n'était pas là une seconde plus tôt."

    stop music fadeout 0.5

    think "..."

    scene bg_cg030 at adaptive_fullscreen
    show bg_cg030 at slow_zoom_creep, breathe_dark
    with dread_pix
    $ unlock_gallery_image("bg_cg030")

    "Je reste immobile beaucoup trop longtemps, incapable de décider si je regarde réellement quelque chose ou si j'attends simplement que quelque chose apparaisse."

    think "Qu'est-ce que..."

    scene bg_cg030_1 at adaptive_fullscreen
    show bg_cg030_1 at slow_zoom_in
    show bg_cg030 at afterimage
    with blink

    "Mon regard glisse sur le fond du couloir, revient au même endroit, puis s'y bloque de nouveau."

    think "Non."

    "Je cligne des yeux."

    scene couloir_infirmerie at adaptive_fullscreen
    show couloir_infirmerie at unease_drift
    with creep_diss

    "Le couloir est exactement comme il devrait être."

    think "Alors pourquoi j'ai arrêté de marcher ?"

    "Je reprends ma route, plus lentement."

    play sound "audio/sfx/metal_hit_distant.ogg"

    "Un bruit métallique résonne quelque part derrière moi." with vpunch

    "Je me retourne immédiatement."

    scene bg_cg030 at adaptive_fullscreen
    show flash_white at hard_flash
    with glitch_diss

    scene couloir_infirmerie at adaptive_fullscreen, lean_left
    with hpunch

    "Rien."

    "Le couloir n'a pas changé."

    think "..."

    "Je voudrais continuer, mais mes jambes refusent de repartir tout de suite."
    "Une sensation absurde me colle à la nuque : celle d'avoir oublié quelque chose d'important alors que je viens précisément de vérifier trois fois la même chose."

    think "Archives. Gymnase. Infirmerie."

    "Je répète l'ordre dans ma tête."

    think "Archives. Gymnase. Infirmerie."

    "Pendant une seconde, je ne suis plus certain que ce soit l'ordre dans lequel j'y suis allé."

    think "..."

    "Je ferme les yeux, puis les rouvre."

    think "Je dois retourner voir Elias."

    jump _10_0_1_1_2_ANNONCE_KAMI


label _10_0_1_1_2_ANNONCE_KAMI:
    show screen kami_broadcast_ui

    play sound sfx_announce
    pause 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    kami "Comment vont mes petits représentants ce matin ? Bien cuits ? Bien transpirants ?"

    "La voix de Kami remplit le couloir avant que j'aie le temps de repartir vers la maintenance."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vois que vous vous êtes parfaitement acclimatés à mon retour."
    kami "Oh, en parlant de climat..."

    scene bg_diffusion_meteo at adaptive_fullscreen with dissolve
    kami "Aujourd'hui, le Conclave vous offre une charmante ambiance tropicale."
    kami "La salle du Canon rattrape une partie de son retard et sollicite un peu trop le refroidissement général."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Évitez donc cette salle, sauf si vous souhaitez finir cuits autrement."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Cela explique votre température fort peu élégante, mais je vous laisse vos petits problèmes techniques. J'ai mieux à faire."

    think "La chaleur, peut-être. Pas les relais."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Revenons à votre performance d'hier."
    kami "Vous avez gagné assez de temps pour permettre à plusieurs Limenois de se mettre en règle."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Des Limenois qui avaient tout de même décidé de défier mes Commandements !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Heureusement pour eux, je suis d'excellente humeur."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Quoi ? Ça ne se voit pas ?"

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Nous sommes déjà au dixième jour du Conclave. Un tiers du parcours !"
    kami "Et malgré vos efforts, vous êtes presque tous encore fonctionnels."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vous attends dans la Salle du Conclave pour découvrir votre prochain vote. Ne traînez pas !"

    hide screen kami_broadcast_ui

    scene couloir_infirmerie at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "reflexion"),
        ("sael", "mefiant"),
    ])

    sael inquiet "Noam ?"

    "Sael sort de l'infirmerie, me regarde, puis suit la direction de mes yeux."

    sael mefiant "Tu attends quelqu'un ?"

    noam hesitation "Non."

    sael raison "Alors viens. Kami n'apprécie pas qu'on la fasse attendre."

    noam fatigue "Ouais... J'arrive."

    "Sael part devant. Je reste encore une seconde à regarder le couloir avant de la suivre."

    think "Elias attend mon rapport."

    think "Il devra attendre."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_34
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    "Quand j'arrive, tout le monde est déjà installé. Mara suit mon trajet jusqu'à ma place sans même essayer d'être discrète."

    mara taquin "Ah bah quand même. T'as fait une sieste debout dans le couloir ?"

    noam hesitation "Non. Désolé, j'ai... perdu du temps."

    lysa inquiet "Tu as surtout perdu quelques couleurs."

    mara stress "Il était déjà blanc avant. Là, il tire vers le transparent."

    elen inquiet "Tu veux t'asseoir près de la porte ? Si tu dois sortir, ce sera plus simple."

    noam fatigue "Ça va. J'ai juste eu un moment bizarre."

    iris desaccord "Ce n'est toujours pas une réponse."

    kael calme "Laissez-le respirer."

    iris colere "Je le laisse respirer. Je constate juste qu'il a une tête de mort."

    julian inquiet "Kami va parler. On reprend ça après."

    elias reflechit "Et les relais ?"

    "Je tourne la tête vers lui."

    noam hesitation "Les trois affichent un fonctionnement normal."

    elias inquiet "Et le flux ?"

    noam reflexion "Rien. Pas un souffle."

    "Elias fronce les sourcils, mais l'annonce retentit avant qu'il puisse répondre."

    play sound sfx_announce
    show screen kami_broadcast_ui

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Tout le monde est là ! C'est gentil de m'éviter un appel interminable."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous voulez connaître le thème de votre prochaine grande décision ?"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Au douzième jour, vous voterez sur l'autorisation des dispositifs de brouillage."
    kami "Un vote favorable légalisera leur possession, leur fabrication et leur utilisation."
    kami "Dans les limites techniques que je fixerai, naturellement. Les autres Commandements continueront de s'appliquer."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "En revanche, si vous votez contre, toute zone utilisant un brouilleur sera détruite par le Canon."
    kami "Broyée, pour être précise. Je ne voudrais pas que vous sous-estimiez la sanction."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Il faut bien apprendre à respecter les règles, mes chéris."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et si vous les interdisez aux autres, je retirerai aussi ceux de vos chambres. Un peu de cohérence !"

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn colere "Broyée..."
    $ bc_hide()

    kami "Oui, Ryn. L'euphémisme nuit souvent à la pédagogie."

    $ bc_show("nyra", "raison", px=-70, py=-50, pz=0.85)
    nyra raison "Personne ici ne votera pour rendre ta surveillance plus simple."
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Sans brouilleurs, je détecte immédiatement une infraction. Avec eux, certains vilains pourraient agir hors de mon regard."

    $ bc_show("mara", "rire", px=-70, py=-50, pz=0.85)
    mara taquin "Tout ce discours pour justifier que tu nous mates jusque dans nos chambres."
    mara agace "Désolée, mais ma liste d'invités est déjà complète."
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Oh, Mara... Tu sous-estimes les plaisirs de l'observation."

    $ bc_show("elias", "fatigue", px=-70, py=-50, pz=0.85)
    elias fatigue "C'est une idée ou cette conversation part en couille ?"
    $ bc_hide()

    $ bc_show("kael", "doute", px=-70, py=-50, pz=0.85)
    kael reflechit "Les chambres ont des brouilleurs internes depuis notre arrivée."
    kael calme "Leur fonction affichée est de protéger les conversations privées."
    $ bc_hide()

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Petite correction : ils empêchent la cellule de diffusion d'enregistrer vos conversations privées."
    kami "Moi, je continue de vous voir et de vous entendre. Seulement, à cause des brouilleurs, je n'ai pas accès aux images ni aux sons pendant une semaine."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je pourrais même vous dire qui ronfle !"

    $ bc_show("iris", "desaccord", px=-70, py=-50, pz=0.85)
    iris desaccord "Personne de rationnel ne vote contre ça."
    $ bc_hide()

    $ bc_show("julian", "inquietude", px=-70, py=-50, pz=0.85)
    julian inquiet "L'intimité n'est pas une faveur que tu peux retirer quand ça t'arrange."
    julian colere "Même cette mascarade devrait avoir des limites."
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ce sera pourtant votre décision. Et vous en assumerez les conséquences."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas hesitation "Je vais poser la question, mais laissez-moi finir avant de me tomber dessus."

    ryn colere "Très bon début."

    tomas inquiet "Si on les autorise, qu'est-ce qui empêche quelqu'un de s'en servir pour cacher une autre infraction ?"

    ryn colere "Et si on les interdit, tous ceux qui en ont déjà crèvent. T'as besoin de réfléchir longtemps ?"

    tomas hesitation "J'ai pas dit qu'il fallait les interdire. J'ai dit qu'il fallait penser à ce qu'on autorise."

    lysa blase "Le choix reste assez simple : un risque qu'on peut encadrer ou une liste d'adresses à bombarder."

    elen reflexion "On peut les autoriser et décider après qui a le droit d'en fabriquer, non ?"

    kael reflechit "Oui. Un brouilleur nécessite des composants précis. La production restera limitée tant que le commerce ne change pas."

    mara agace "Et surtout, on garde ceux des chambres. J'ai déjà assez de mal à dormir sans savoir qu'elle écoute."

    elias reflechit "Attendez. Tomas a pas complètement tort."

    ryn colere "Toi aussi ?"

    elias inquiet "Si quelqu'un tabasse son voisin derrière un brouilleur, Kami voit rien. C'est tout ce que je dis."

    iris colere "Kami ne protège personne, Elias. Elle détecte une bagarre et elle exécute celui qu'elle a décidé coupable."

    elias inquiet "Je sais. Mais la personne derrière le brouilleur, elle, peut toujours se faire frapper."

    iris desaccord "Et sans brouilleur, elle ne peut même pas demander de l'aide sans être entendue."

    "Elias ouvre la bouche, puis renonce."

    nyra raison "On ne réglera pas toutes les conséquences aujourd'hui."
    nyra reflechit "On autorise les brouilleurs. Ensuite, on travaille sur leur distribution et sur un moyen d'alerte indépendant."

    tomas reflechit "Un signal d'urgence qui sortirait du brouillage... Oui, techniquement, ça peut se faire."

    ryn colere "Alors fais-le. Mais on vote pour."

    julian inquiet "On semble au moins d'accord sur ce point. Il faudra convaincre les autres sans leur cacher le reste."

    mara taquin "Tu pourras faire un discours. Ça devrait t'occuper jusqu'au vote."

    julian taquin "Je prendrai le risque."

    sael determine "On autorise d'abord. On encadre ensuite. Dans cet ordre."

    "Ils continuent à parler, mais leurs voix commencent à se mélanger dans ma tête."
    "Sans vraiment le vouloir, je regarde de nouveau vers la porte."

    noam hesitation "Est-ce que... quelqu'un était dans les couloirs juste avant l'annonce ?"

    iris inquiet "Pourquoi ?"

    noam reflexion "J'ai cru voir quelqu'un. Enfin... je crois."

    "Plusieurs regards se tournent vers moi."

    mara stress "Tu crois ?"

    noam hesitation "Je veux juste savoir où vous étiez."

    tuto "(Vérifie les alibis des représentants présents.)"

    $ j10011_alibis_checked = []

    jump _10_0_1_1_ALIBIS


label _10_0_1_1_ALIBIS:

    if len(j10011_alibis_checked) >= 5:
        jump _10_0_1_1_APRES_ALIBIS

    menu:
        "À qui demander ?"

        "Tomas et Nyra" if "tomas_nyra" not in j10011_alibis_checked:
            tomas inquiet "J'étais déjà ici avant l'annonce. Nyra est arrivée avec moi."
            nyra raison "On a quitté les archives ensemble et on n'a croisé personne."
            $ j10011_alibis_checked.append("tomas_nyra")
            jump _10_0_1_1_ALIBIS

        "Mara et Elen" if "mara_elen" not in j10011_alibis_checked:
            mara stress "Elen et moi, on était encore à la cafétéria."
            elen inquiet "Oui ! On est parties quand Kami a lancé l'annonce, et le couloir était vide."
            $ j10011_alibis_checked.append("mara_elen")
            jump _10_0_1_1_ALIBIS

        "Elias" if "elias" not in j10011_alibis_checked:
            elias reflechit "Maintenance. J'ai pas bougé jusqu'à l'annonce."
            elias inquiet "Je t'ai aperçu plus tard dans le couloir, mais j'ai croisé personne d'autre."
            $ j10011_alibis_checked.append("elias")
            jump _10_0_1_1_ALIBIS

        "Sael" if "sael" not in j10011_alibis_checked:
            sael mefiant "J'étais à l'infirmerie."
            sael reflexion "Quand je suis sortie, tu étais déjà dans le couloir. Seul."
            $ j10011_alibis_checked.append("sael")
            jump _10_0_1_1_ALIBIS

        "Iris et Kael" if "iris_kael" not in j10011_alibis_checked:
            iris inquiet "J'étais avec Kael dans le couloir du Conclave."
            kael calme "On est entrés ensemble. Personne ne nous a dépassés."
            $ j10011_alibis_checked.append("iris_kael")
            jump _10_0_1_1_ALIBIS


label _10_0_1_1_APRES_ALIBIS:

    "Je repasse les réponses dans ma tête. Elles s'emboîtent trop facilement pour m'aider."

    noam reflexion "D'accord..."

    iris inquiet "Noam, qu'est-ce que t'as vu ?"

    noam hesitation "Je sais pas."

    mara stress "C'est pas très rassurant."

    sael mefiant "Tu étais déjà comme ça quand je suis sortie de l'infirmerie."

    elias inquiet "Il faisait quoi ?"

    sael reflexion "Il regardait le bout du couloir."

    noam inquiet "Je regardais rien."

    "Les mots sortent plus vite que prévu."

    noam hesitation "Enfin... je veux dire, il n'y avait rien."

    "Un silence bref tombe autour de moi."

    elen inquiet "Noam ?"

    play sound sfx_heartbeat fadein 1.0

    $ blink()

    "La chaleur remonte brusquement jusque dans mon visage. Mon cœur accélère comme si je venais de courir."

    think "Pas maintenant."

    "Quelqu'un prononce mon nom."

    noam inquiet "Quoi ?"

    iris inquiet "Quoi, quoi ?"

    "Je la fixe."

    noam fatigue "Tu viens de m'appeler."

    iris desaccord "Non."

    "Autour de la table, personne ne rit."

    $ blink()

    "Les voix s'éloignent d'un seul coup et la salle paraît se décaler légèrement, comme si le sol n'était plus tout à fait horizontal."

    elias panique "Noam ?"

    noam fatigue "Je... je crois que..."

    $ blink()

    "Mes jambes cèdent avant que je puisse terminer."

    scene black with fade
    pause 3.0

    call end_day("11") from _call_end_day_1
    jump _11_0_1_1_REVEIL_CHAMBRE

# Total journée : 10 minutes 50
# Durée totale : 2h30,50
