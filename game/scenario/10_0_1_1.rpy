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
    call show_chapter_title("Début du chapitre 4", "Chapitre 4 — Quelque chose ne tourne pas rond") from _call_show_chapter_title_17

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
    $ noam_has_juliette_drawing = False
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0
    $ blink()

    "Je rêve du Conclave. Les sièges sont vides, les pupitres sont allumés et quelqu'un me demande encore de voter alors que le canon tire déjà."
    "Je me réveille en voulant répondre, avec la bouche sèche et le drap collé au dos."
    scene bg_chambre at adaptive_fullscreen with dissolve
    noam fatigue "Mais il fait combien, là-dedans... ?"
    "La pièce est étouffante. Je repousse la couverture du pied et tends la main vers la bouche d'aération, sans sentir le moindre courant d'air."
    noam desaccord "Super. Deux jours sans Kami, une nuit avec le canon... et maintenant on nous fait cuire."
    "Je regarde l'écran mural. Rien. Pas d'annonce, pas de commentaire sur ma coiffure, pas de bulletin triomphal sur les tirs d'hier."
    think "D'habitude, je me serais réjoui de ce silence. Là, je voudrais juste savoir si les tirs se sont arrêtés."
    "Je m'approche du bureau. La place du dessin de Juliette est toujours vide."
    noam triste "Je ne t'ai pas oublié."
    "Je suis sur le point de fouiller à nouveau sous la tablette lorsque quelque chose résonne dans le couloir : le claquement d'une porte, puis des pas pressés."
    think "Quelqu'un est enfin réveillé. Ça devrait me rassurer."
    "J'enfile ma veste, la retire aussitôt à cause de la chaleur, puis la reprends par habitude. Je dois avoir l'air malin."
    stop music fadeout 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_25
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    "Le couloir est presque aussi chaud que la chambre. Une silhouette disparaît au coin du mur avant que je puisse reconnaître qui que ce soit."
    noam neutre "Hé !"
    "Les pas ne s'arrêtent pas."
    think "Peut-être qu'on n'a simplement pas envie de se parler aujourd'hui. Moi le premier."
    "Je repense à Ryn, à Sael qui lui barrait la route, et au grondement qui couvrait nos voix. Pour la première fois, je ne sais pas si j'ai envie de croiser quelqu'un du Conclave."
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
    think "Je vais à la cafétéria. Si quelqu'un a des nouvelles de Limen, c'est là que je les trouverai."
    call KD_ROUTE_J10_LYSA from _call_optional_kd_route_j10_lysa
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
        ("noam", "inquiet"), ("elias", "fatigue"),
        ("mara", "stress"), ("ryn", "colere"), ("nyra", "reflechit"),
    ])
    mara agace "NON. T'as pas le droit de faire ça."
    elias fatigue "Je ne fais RIEN !"
    mara colere "Tu sépares les morceaux de pain pour manger la mie et laisser la croûte ! C'est quoi le projet ?"
    elias reflechit "Manger la partie qui ressemble encore à du pain ?"
    ryn colere "Vous pouvez fermer vos gueules deux secondes ?"
    "La remarque claque plus fort que nécessaire. Elias laisse tomber sa croûte sur le plateau."
    mara stress "Tu crois qu'on fait ça pour t'emmerder ?"
    ryn colere "Je crois surtout que vous arrivez à parler de pain après hier."
    nyra neutre "Ryn. Tu n'es pas le seul à avoir regardé le canon tirer."
    ryn colere "J'AI PAS DIT ÇA !"
    "J'hésite sur le pas de la porte. Hier encore, une dispute pareille aurait fini en blague."
    noam hesitation "Euh... Salut ?"
    elias fatigue "Noam ! Voilà. Un témoin. Tu manges la croûte de ce truc, toi ?"
    mara agace "Ne l'encourage pas !"
    noam fatigue "J'ai surtout l'impression que ce pain a déjà servi de matériau de construction."
    elias sourire "MERCI."
    ryn fatigue "..."
    "Elias ricane, mais ça ne dure pas. Sur l'écran d'information, les mêmes phrases défilent depuis mon arrivée."
    noam reflexion "Il y a des nouvelles ?"
    nyra reflechit "Un communiqué. « La majorité des campements a été dispersée avant la reprise des sanctions. »"
    noam inquiet "Et le reste ?"
    nyra neutre "Aucun chiffre publié. Aucune répartition. Rien de vérifiable."
    ryn colere "Donc une phrase pour nous dire de nous féliciter."
    elias inquiet "Ça veut peut-être dire qu'une majorité s'est sauvée."
    ryn colere "OU ÇA VEUT DIRE QU'ILS SONT MORTS !"
    "Elias se fige. Même Mara ne bouge plus."
    nyra raison "Les deux restent possibles. On ne peut pas déduire le bilan de cette phrase."
    ryn colere "T'es sérieuse, là ? Tu vas encore m'expliquer comment lire un écran ?"
    nyra neutre "Si tu veux qu'on trouve les survivants, il faudra commencer par admettre qu'on ne sait pas qui ils sont."
    ryn colere "..."
    mara stress "Ryn, t'as le droit d'être en colère. Mais tu peux pas nous demander de le rester vingt-quatre heures sur vingt-quatre."
    ryn colere "Je demande rien."
    mara agace "Ah, d'accord ! C'est juste ton visage qui menace tout le monde !"
    noam triste "On a essayé de les prévenir."
    ryn fatigue "Je sais."
    noam hesitation "On a gagné du temps, au moins."
    ryn colere "Je SAIS, Noam !"
    "Il serre le dossier d'une chaise. Pendant un instant, j'ai peur qu'il l'arrache du sol."
    ryn fatigue "Je le sais. Mais j'ai passé la nuit à me demander qui j'avais vu sur cet écran. Et s'il avait couru assez vite."
    "Personne ne lui répond. Je m'assieds à côté d'Elias, qui pousse silencieusement une tasse vers moi."
    noam reflexion "C'est quoi ?"
    elias fatigue "Du café. Pas renversé, cette fois. Il paraît que ça se boit."
    noam taquin "Tu te diversifies."
    mara taquin "Éloignez-le des machines, il va provoquer une deuxième panne mondiale."
    elias colere "C'est BON, cette blague !"
    "Ryn souffle du nez. Ce n'est pas un rire, mais Elias le remarque et lève la tasse comme s'il venait de remporter un prix."
    nyra reflechit "J'irai vérifier les rapports du Canon. Tomas aura peut-être obtenu le détail des déclarations."
    ryn neutre "Je viens."
    nyra raison "D'accord, mais tu me laisses accéder aux données sans menacer l'ordinateur."
    ryn desaccord "Je menace pas les ordinateurs."
    mara taquin "Seulement ceux qui te répondent."
    "Il ne réplique pas. Il fixe son plateau pendant quelques secondes."
    ryn fatigue "J'ai pas faim."
    "Ryn part avant que quelqu'un puisse lui demander de rester. Nyra attend qu'il ait franchi la porte, puis récupère sa tablette."
    nyra neutre "Je vais quand même vérifier les chiffres."
    mara stress "Oui. Merci."
    "Quand Nyra s'éloigne à son tour, l'espace laissé par leurs chaises paraît immense."
    elias fatigue "Je crois que j'aurais préféré qu'on se dispute pour de vrai sur le pain."
    mara neutre "C'était une vraie dispute."
    elias rire "T'es capable de t'énerver pour de la mie, Mara."
    mara sourire "Et je t'emmerde avec amour."
    noam taquin "C'est une déclaration qui restera dans l'histoire du Conclave."
    "Mara me tire la langue. Elias essaye de sourire, puis baisse les yeux vers ses mains."
    elias fatigue "Quand j'ai vu « majorité dispersée », ça m'a soulagé. Une seconde. J'ai eu l'impression que c'était fini."
    noam neutre "Moi aussi."
    mara stress "Moi aussi. Bon. On va pas commencer à se détester pour avoir respiré un coup."
    elias fatigue "J'aurais peut-être préféré travailler. Au moins, les vis ne te demandent pas si t'es une bonne personne."
    mara taquin "Non. Elles se contentent de s'enfuir quand tu les touches."
    elias rire "C'est vrai."
    "Il se lève, ramasse son plateau et le repose aussitôt parce qu'il a oublié sa tablette."
    elias fatigue "Je vais à la maintenance. J'ai un relais qui fait un bruit de merde depuis ce matin."
    noam reflexion "Un relais ?"
    elias neutre "La ventilation. Tu trouves pas qu'il fait chaud ?"
    noam desaccord "J'ai cru que j'allais fondre dans mon lit."
    elias sourire "Voilà. J'espère que c'est rien. Si le Conclave se met à transpirer, j'ai pas envie d'être celui qu'on appelle pour essuyer les murs."
    mara rire "C'est bien dommage, j'avais précisément ce rôle en tête pour toi."
    elias fatigue "Tu vois ? Une raison de plus de partir."
    "Il quitte la salle. Mara termine son verre sans me regarder."
    mara stress "T'as une tête épouvantable, toi aussi."
    noam fatigue "Merci."
    mara neutre "C'est pas une insulte. Pas aujourd'hui."
    "Je hoche la tête, sans savoir quoi répondre."
    $ hideGroup()
    jump _10_0_1_1_MARCHE_APRES_TABLE


label _10_0_1_1_MARCHE_APRES_TABLE:
    $ current_period = "Après-midi"
    stop music fadeout 1.5
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_29
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.2
    "Dans le couloir, je tire sur le col de ma chemise. La chaleur s'est aggravée depuis ce matin."
    think "Rester assis à me demander combien de gens sont morts ne va pas me donner la réponse. Et je crois qu'Elias a besoin de parler à quelqu'un, même s'il affirme le contraire."
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_30
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "fatigue"), ("elias", "fatigue")])
    "Elias est à genoux devant un coffret ouvert. Il tourne un outil entre ses doigts avec un air si contrarié que j'hésite à lui demander s'il s'est encore disputé avec une vis."
    elias colere "Ça n'a AUCUN sens !"
    noam taquin "Bonjour à toi aussi."
    elias inquiet "Oh. Noam. Désolé."
    noam reflexion "C'est le relais ?"
    elias fatigue "Oui. Non. Enfin, j'en sais rien, justement."
    noam taquin "Excellent diagnostic. C'est rassurant de savoir qu'on a un spécialiste."
    elias fatigue "Tu veux la version professionnelle ?"
    noam sourire "Vas-y."
    elias colere "Ça n'a AUCUN PUTAIN DE SENS."
    "Je ris malgré moi. Elias aussi, brièvement. Puis un cliquetis résonne dans le mur."
    noam reflexion "Ça fait souvent ça ?"
    elias inquiet "C'est la quatrième fois. Et chaque fois que je pense l'avoir localisé, il s'arrête."
    noam neutre "Il te fuit."
    elias fatigue "Comme les vis."
    "Il touche une commande. Une ligne de valeurs se met à défiler sur l'écran."
    elias reflechit "Regarde. L'alimentation est bonne, le contrôle répond, les vannes sont ouvertes."
    noam hesitation "Donc on devrait avoir de l'air."
    elias neutre "Exactement."
    "Le bruit de ventilation derrière nous s'interrompt si brusquement que j'entends Elias avaler sa salive."
    noam inquiet "Tu l'as arrêté ?"
    elias inquiet "Non."
    "Il pousse la même commande. La diode passe au vert, et aucun souffle ne revient."
    elias colere "Mais BORDEL !"
    noam reflexion "C'est à cause du canon ?"
    elias reflechit "Peut-être. Il a tiré pendant des heures hier. Sauf que si le refroidissement tirait trop sur le système, les relais devraient remonter une alerte."
    noam neutre "Et ils n'en remontent pas."
    elias inquiet "Rien. Comme si tout allait merveilleusement bien."
    "Il ferme les yeux une seconde, se masse les tempes puis se tourne vers moi."
    elias neutre "Je vais rester ici et suivre l'alimentation principale. Tu peux m'aider ?"
    noam sourire "J'allais justement me proposer, avant de te voir discuter avec tes outils."
    elias reflechit "Il y a trois relais secondaires accessibles : archives, gymnase, infirmerie. Va voir leur écran, leur grille, le conduit. Juste observer."
    noam taquin "Et si je trouve une petite créature qui vit dans la ventilation ?"
    elias fatigue "Tu lui dis de payer son loyer, et tu reviens."
    noam rire "D'accord."
    "Je commence à partir. Il me retient par la manche."
    elias inquiet "Noam. Si tu vois un truc bizarre, ne démonte rien. Je voudrais éviter qu'on se retrouve aussi sans lumière."
    noam taquin "Très bien, monsieur « ça n'a aucun sens »."
    elias colere "JE SUIS SÉRIEUX !"
    noam neutre "Moi aussi."
    $ hideGroup()
    tuto "(Inspecte les trois relais de ventilation. Tu peux les vérifier dans l'ordre de ton choix.)"
    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_ENQUETE_CLIM:
    if len(j10011_relays_checked) >= 3:
        jump _10_0_1_1_RETOUR_ELIAS
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    if len(j10011_relays_checked) == 0:
        think "Archives, gymnase, infirmerie. Trois endroits à vérifier. Ça devrait être simple."
    elif len(j10011_relays_checked) == 1:
        think "Un relais vérifié. J'aimerais déjà avoir quelque chose de concret à raconter à Elias."
    else:
        think "Plus qu'un relais. J'ai la chemise trempée et l'impression que les couloirs deviennent de plus en plus étroits."
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
    "Les archives sont plus calmes encore que d'habitude. Sans ventilation, je peux entendre le frottement de mes semelles sur le sol."
    "La diode du relais est verte. Rien d'autre ne semble anormal."
    noam neutre "Bon. Elias a dit de regarder trois trucs."
    menu:
        "Qu'est-ce que je vérifie d'abord ?"
        "L'écran":
            "Je lis : « Vannes ouvertes. Pression stable. Flux normal. »"
            noam reflexion "Donc tout marche ?"
            "Je tends aussitôt la main devant la grille, par réflexe. Pas la moindre brise."
            noam desaccord "Ah, bah oui. Parfaitement."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE
        "La grille":
            "Je place la paume contre les lamelles. Rien ne bouge. Même la poussière reste sur place."
            noam taquin "Vous avez pensé à prévenir l'air qu'il était censé passer par ici ?"
            "Je me rends compte que je parle à une grille. Je retire la main."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE
        "Le conduit":
            "La paroi métallique est beaucoup plus chaude que le reste du mur. Je laisse la main dessus un instant."
            "Un petit clic résonne dans la gaine, bien plus loin."
            noam reflexion "Un clapet... ?"
            "Le bruit ne revient pas."
            jump _10_0_1_1_RELAIS_ARCHIVES_SUITE


label _10_0_1_1_RELAIS_ARCHIVES_SUITE:
    "Je vérifie les deux autres éléments. La diode reste obstinément verte, l'écran soutient que tout fonctionne, et aucun air ne sort de la grille."
    noam reflexion "S'il n'y a pas de panne, pourquoi j'étouffe ?"
    "En quittant l'allée, je crois entendre une deuxième fois le clic du conduit."
    "Je m'arrête. Le bruit s'arrête aussi."
    think "Il faudrait que je demande à Elias si les machines ont le droit de faire exprès de m'énerver."
    $ j10011_relay_archives_checked = True
    $ j10011_relays_checked.append("archives")
    $ j10011_relay_order.append("archives")
    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RELAIS_GYMNASE:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_j10011_gym_relay
    scene bg_gymnase at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg051")
    scene bg_cg051 at adaptive_fullscreen with dissolve
    "Je tombe sur Iris au milieu d'un entraînement. Elle enchaîne deux coups contre un sac, pivote et termine par un mouvement si net que je préfère rester à bonne distance."
    noam surpris "Ah ! Pardon. Je savais pas que tu faisais de la boxe."
    iris fatigue "Tu connais encore beaucoup de choses que je ne fais pas ?"
    noam taquin "Je sais que tu m'engueules souvent."
    iris colere "C'est pas un sport."
    noam sourire "Tu devrais y penser. Tu serais championne."
    iris desaccord "T'es venu pour être drôle ou pour quelque chose d'utile ?"
    noam reflexion "Elias m'a envoyé vérifier la ventilation."
    iris fatigue "Alors dis-lui qu'il m'envoie de l'air avant de m'envoyer un rapport ! J'ai l'impression de m'entraîner dans une boîte de conserve."
    noam neutre "C'est ce qu'on essaie de comprendre."
    iris reflechit "Les voyants sont verts, pourtant. Je les ai regardés en arrivant."
    noam surpris "Tu as vérifié le relais ?"
    iris colere "Non, j'ai posé les yeux dessus. Tu sais, ce truc qu'on fait quand on regarde quelque chose."
    noam taquin "Tu es vraiment reposante à fréquenter."
    iris taquin "Et toi vraiment courageux de rester à portée de mes poings."
    "Elle prend une serviette, s'essuie le front et baisse le ton."
    iris fatigue "J'arrivais pas à dormir. J'ai pensé que ça aiderait."
    noam hesitation "À cause du vote ?"
    iris neutre "À cause de plein de trucs."
    "Elle se tourne vers le sac. Elle pourrait lui donner un dernier coup, mais n'en fait rien."
    iris fatigue "Kael me répond à peine depuis hier. Et Kami est revenue. Et maintenant il fait une chaleur à crever."
    noam neutre "Je peux pas faire grand-chose pour les deux premiers."
    iris taquin "Alors dépêche-toi sur le troisième."
    noam sourire "Bien reçu."
    "Elle récupère ses affaires, puis s'arrête au seuil."
    iris fatigue "Noam ?"
    noam reflexion "Oui ?"
    iris inquiet "Si jamais tu parles à Kael... ne lui demande pas encore s'il est sûr d'avoir bien rangé la photo."
    noam neutre "Je n'allais pas le faire."
    iris reflechit "Tant mieux."
    "Elle quitte le gymnase. Une fois seul, je réalise à quel point le grondement habituel de la ventilation me manque."
    scene bg_gymnase at adaptive_fullscreen with dissolve
    menu:
        "Qu'est-ce que je vérifie d'abord ?"
        "L'écran":
            "La valeur de pression est stable. Elle tombe à zéro le temps d'un clignement d'œil, puis revient exactement au même chiffre."
            noam surpris "Hein ?"
            "Je me penche davantage. La valeur ne bouge plus."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE
        "La grille":
            "La grille est sèche, chaude, immobile. En collant l'oreille à proximité, je perçois pourtant un très léger ronronnement, comme une machine qui tournerait de l'autre côté d'une cloison."
            noam reflexion "Il y a bien quelque chose qui fonctionne..."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE
        "Le conduit":
            "Une vibration traverse la paroi sous ma paume. Je retire la main, puis la repose aussitôt."
            "Cette fois, rien."
            noam desaccord "C'est pas possible. Je l'ai sentie."
            jump _10_0_1_1_RELAIS_GYMNASE_SUITE


label _10_0_1_1_RELAIS_GYMNASE_SUITE:
    "Je vérifie le reste. Les données paraissent normales, mais rien ne sort du conduit."
    if len(j10011_relays_checked) >= 1:
        think "Deux endroits différents, le même affichage absurde. Elias va adorer."
    else:
        think "Si les deux autres relais font pareil, je ne vais pas pouvoir lui raconter grand-chose d'utile."
    "Je jette un dernier regard à l'endroit où Iris s'entraînait. La chaleur est toujours là, mais sa petite colère avait presque rendu l'endroit agréable."
    $ j10011_relay_gym_checked = True
    $ j10011_relays_checked.append("gymnase")
    $ j10011_relay_order.append("gymnase")
    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RELAIS_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "infirmerie1") from _call_j10011_infirmary_relay
    scene infirmerie1 at adaptive_fullscreen with dissolve
    "L'infirmerie est déserte. Je m'attendais à croiser quelqu'un ; à la place, un bourdonnement électrique vient du couloir intérieur."
    "La diode du relais est fixe. Verte, évidemment."
    noam fatigue "Vous vous êtes tous passé le mot ou quoi ?"
    "Quand je m'approche, l'écran s'allume avant que je l'aie touché."
    noam reflexion "Ah. D'accord."
    menu:
        "Qu'est-ce que je vérifie d'abord ?"
        "L'écran":
            "FLUX : ACTIF. TEMPÉRATURE : 31,4 °C. PRESSION : NORMALE."
            "Une ligne supplémentaire apparaît au bas de l'écran. Elle s'efface si vite que je ne réussis pas à la lire."
            noam surpris "Attends !"
            "Je touche la bordure de l'écran. Rien ne se passe."
            think "J'ai peut-être simplement cligné des yeux."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE
        "La grille":
            "Je tends la main. Aucun souffle. Puis quelque chose frappe dans la gaine, une seule fois."
            noam hesitation "Elias ?"
            "Je me rends compte de l'absurdité de la question. Il est à l'autre bout de la station."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE
        "Le conduit":
            "Le métal est brûlant par endroits. Je pose deux doigts sur une zone plus froide."
            "Une vibration lente passe sous ma main. Pas un grondement continu : plutôt un mouvement bref, suivi d'un autre."
            "Je retire les doigts. Plus rien."
            noam inquiet "..."
            jump _10_0_1_1_RELAIS_INFIRMERIE_SUITE


label _10_0_1_1_RELAIS_INFIRMERIE_SUITE:
    "Je contrôle les deux autres éléments, sans rien apprendre de plus. L'écran affirme que la pression est normale, tandis que la grille reste immobile."
    if len(j10011_relays_checked) == 2:
        think "Trois relais. Aucun air. Aucun signal d'erreur. Elias avait raison, ça n'a aucun sens."
    elif len(j10011_relays_checked) == 1:
        think "Deux relais identiques, et pourtant j'ai l'impression que quelque chose d'autre se passe dans celui-ci."
    else:
        think "Il vaut mieux que je vérifie les deux autres avant d'aller inquiéter Elias."
    "Je m'éloigne de la grille. Au moment de tourner le dos, j'entends de nouveau le bruit dans la gaine."
    "Pas le même rythme."
    think "Je vais arrêter d'écouter les tuyaux comme si quelqu'un allait me répondre."
    $ j10011_relay_infirmary_checked = True
    $ j10011_relays_checked.append("infirmerie")
    $ j10011_relay_order.append("infirmerie")
    jump _10_0_1_1_ENQUETE_CLIM


label _10_0_1_1_RETOUR_ELIAS:
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    "Je sors du dernier secteur, les doigts encore chauds après avoir touché les conduits."
    think "Trois relais, trois affichages parfaitement rassurants, et pas un souffle. Elias va pouvoir choisir entre me croire et étrangler un écran."
    "J'essaie de me rappeler par quel couloir rejoindre la maintenance. Je connais pourtant ce chemin."
    noam reflexion "À droite, puis..."
    "Quelque chose change au fond du couloir."
    jump _10_0_1_1_DOPPELGANGER


label _10_0_1_1_DOPPELGANGER:
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    stop music fadeout 0.5
    "Je ralentis, sans savoir exactement pourquoi. Une partie du couloir me semble différente, mais dès que j'essaie de trouver laquelle, tout paraît reprendre sa place."
    think "Qu'est-ce que..."
    scene bg_cg030 at adaptive_fullscreen
    show bg_cg030 at slow_zoom_creep, breathe_dark
    with dread_pix
    $ unlock_gallery_image("bg_cg030")
    $ investigation_add("silhouette_couloirs")
    "Je fixe le même point trop longtemps. Il y a quelque chose que je devrais reconnaître, quelque chose de tellement évident que mon regard refuse de passer ailleurs."
    think "Non. Attends."
    scene bg_cg030_1 at adaptive_fullscreen
    show bg_cg030_1 at slow_zoom_in
    show bg_cg030 at afterimage
    with blink
    "Je cligne des yeux. La sueur me coule le long du cou, pourtant je viens de sentir un froid insupportable entre les omoplates."
    think "Je..."
    "J'essaie de reculer. Je ne sais plus si j'ai bougé."
    scene couloir_infirmerie at adaptive_fullscreen
    show couloir_infirmerie at unease_drift
    with creep_diss
    "Le couloir est vide."
    "Je reste planté là, une main serrée sur le mur, incapable de comprendre ce qui m'a fait m'arrêter."
    think "C'était quoi, ça ?"
    "J'ouvre la bouche pour appeler quelqu'un. Aucun son ne sort."
    play sound "audio/sfx_metal_clank.mp3"
    "Un choc métallique résonne derrière moi." with vpunch
    scene bg_cg030 at adaptive_fullscreen
    show flash_white at hard_flash
    with glitch_diss
    scene couloir_infirmerie at adaptive_fullscreen, lean_left
    with hpunch
    "Je me retourne si brusquement que ma main glisse sur la paroi."
    "Rien. Pas même un bruit de pas."
    noam inquiet "..."
    "Je voudrais repartir immédiatement, mais le chemin jusqu'à la maintenance me paraît soudain étrangement difficile à remettre en ordre."
    think "Je venais de l'infirmerie. Avant, il y avait..."
    "Je regarde ma tablette. Les trois relais sont cochés. Je les ai bien inspectés."
    think "Pourquoi ai-je eu besoin de vérifier ça ?"
    "La lumière du plafond grésille une fois. Je me surprends à retenir mon souffle en attendant qu'elle recommence."
    "Elle ne recommence pas."
    think "Elias. Je dois retourner voir Elias."
    jump _10_0_1_1_2_ANNONCE_KAMI


label _10_0_1_1_2_ANNONCE_KAMI:
    play sound sfx_announce
    show screen kami_broadcast_ui
    pause 0.6
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    kami "ALLOOOORS ! Comment vont mes petits représentants ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'ai l'impression que certains découvrent les joies du sauna. Vous auriez pu me prévenir, j'aurais apporté des serviettes !"
    noam fatigue "Pas maintenant..."
    scene bg_diffusion_meteo at adaptive_fullscreen with dissolve
    kami "Bulletin météo de votre station préférée : très chaud, très sec, avec un risque élevé d'odeurs corporelles désagréables !"
    kami "À cause des tirs d'hier, les systèmes de refroidissement du Canon travaillent un tout petit peu plus que prévu."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Conséquence : quelques difficultés de climatisation. Rien de bien dramatique. À moins que vous considériez la transpiration comme une tragédie nationale."
    think "Les relais. Elias va vouloir savoir ce qu'elle a dit."
    noam inquiet "Kami ! Les écrans affichent que tout fonctionne !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Noam, tu veux déposer une réclamation ? Je t'informe que le service clientèle est fermé pour cause de chaleur."
    noam colere "Pourquoi les trois relais indiquent-ils un flux normal ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh là là... Les questions techniques, dès le réveil ! Vous êtes d'un ennui."
    "Je serre ma tablette. Elle ne répond pas. Encore."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Évitez simplement la salle du Canon. Je tiens à mes petits invités, et vous m'avez déjà donné assez de travail !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Mais je vous pardonne ! D'ailleurs, j'ai quelque chose de bien plus intéressant que vos petits ventilateurs."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "DIX JOURS ! Cela fait dix jours que vous profitez de mon hospitalité !"
    kami "Un tiers de votre merveilleux séjour. Et presque tout le monde est encore capable de se plaindre ! Quel succès !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ah, au fait, les Limenois d'hier... Certains ont réussi à se disperser. Vous devriez être heureux, non ?"
    noam inquiet "Combien ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Nous n'allons pas recommencer ce débat. Il est TER-MI-NÉ."
    "J'attends une autre phrase, un chiffre, n'importe quoi. Au lieu de cela, son sourire change."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je vous attends tous au Conclave ! Nous allons découvrir votre prochain sujet de vote !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et pas de retard, hein ! J'ai eu ma dose de démocratie hier."
    hide screen kami_broadcast_ui
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion"), ("sael", "mefiant")])
    sael inquiet "Noam ?"
    noam surpris "AH !"
    sael inquiet "..."
    sael mefiant "Tu as un problème ?"
    noam hesitation "Non. Enfin... ça dépend. Tu es là depuis longtemps ?"
    sael reflechit "Je viens de sortir de l'infirmerie."
    noam inquiet "Tu as croisé quelqu'un ?"
    sael mefiant "Non. Pourquoi ?"
    "Je regarde derrière elle, puis au fond du couloir. Tout paraît parfaitement normal."
    noam fatigue "Je crois que j'ai eu un coup de chaud."
    sael raison "Alors tu devrais t'asseoir."
    noam hesitation "Mais Kami nous attend..."
    sael determine "Kami peut attendre deux minutes si tu t'apprêtes à tomber. Ce n'est pas elle qui devra te ramasser."
    noam taquin "C'est presque gentil, dit comme ça."
    sael mefiant "Ne prends pas de mauvaises habitudes."
    "Elle sort une petite bouteille de sa poche et me la tend."
    sael neutre "Bois."
    noam neutre "Merci."
    "Je prends deux gorgées. L'eau est tiède, mais mes mains arrêtent peu à peu de trembler."
    sael reflechit "Tu as l'air d'avoir vu quelque chose de déplaisant."
    noam hesitation "Je ne sais pas."
    sael mefiant "Une réponse peu satisfaisante."
    noam fatigue "Je sais."
    "Elle me regarde encore, puis tend la main vers la direction du Conclave."
    sael determine "Viens. Elias pourra écouter ton rapport plus tard."
    think "Comment sait-elle que je devais voir Elias ? Il m'en a peut-être parlé au matin. Ce n'est pas le moment de lui demander."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_34
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    julian taquin "Ah ! Le dernier représentant arrive enfin. Nous envisagions de faire voter une motion pour constater ton absence."
    mara taquin "Ça lui prendrait au moins trois discours pour le faire."
    julian surpris "Je pourrais être bref !"
    lysa blase "Tu n'en as jamais apporté la preuve."
    noam fatigue "Désolé. J'ai eu un... souci dans le couloir."
    elen inquiet "Tu es tout pâle. Tu veux t'asseoir ?"
    iris inquiet "Il a une mine terrible. Noam, tu as mangé ?"
    noam neutre "Oui."
    iris reflechit "Bu de l'eau ?"
    noam neutre "Oui, maman."
    iris colere "Ne commence pas !"
    mara taquin "Ça y est, deux infirmières pour le prix d'une."
    sael determine "Iris n'est pas infirmière."
    iris colere "Et je n'ai pas demandé à l'être !"
    elen sourire "Vous pouvez éviter de vous chamailler pendant que Noam va mal ?"
    noam desaccord "Je vais BIEN !"
    "Ma voix est plus forte que prévu. Lysa me regarde avec un air que je lui ai déjà vu quand elle ne croit absolument pas ce qu'on lui raconte."
    kael calme "Laissez-le s'asseoir."
    "Je prends ma place. Elias se penche aussitôt vers moi."
    elias reflechit "Alors ? Les relais ?"
    noam neutre "Trois voyants verts, trois écrans qui disent que tout va bien. Zéro souffle."
    elias inquiet "Merde. Aucun message d'erreur ?"
    noam reflexion "Non. Juste une valeur qui a sauté, je crois. Et..."
    elias reflechit "Et quoi ?"
    "Je regarde l'entrée de la salle, puis reviens à Elias."
    noam hesitation "Je t'expliquerai après."
    elias fatigue "Tu sais que c'est la phrase la moins rassurante du monde ?"
    noam neutre "Je sais."
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Tout le monde ! Formidable ! Je commençais à croire que les couloirs vous avaient avalés."
    "Un frisson me traverse, malgré la chaleur."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et ne faites pas ces têtes ! J'ai choisi un sujet plein de promesses. D'intimité. De liberté. Et de délicieux petits secrets !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Au douzième jour, vous voterez sur l'autorisation des dispositifs de brouillage."
    kami "En cas d'adoption unanime, leur possession, leur fabrication et leur utilisation seront autorisées, dans les limites prévues par les autres Commandements."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Vous voyez ? Je sais être une patronne formidable !"
    ryn "Et si on refuse ?"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Alors les zones qui utiliseront encore des brouilleurs seront DÉTRUITES par le Canon !"
    "Personne ne réagit tout de suite."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quoi ? Je suis censée vous expliquer qu'une interdiction ne sert à rien si elle n'est pas sanctionnée ?"
    nyra "Tu veux dire que les zones déjà équipées seraient concernées ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Évidemment. Vous n'allez tout de même pas faire deux poids, deux mesures."
    elen "Mais il y a des brouilleurs dans nos chambres !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Très bien observé, Elen ! Je les retirerai, bien sûr. Je refuse de favoriser mes petits chéris."
    mara "Tu parles d'intimité après avoir expliqué que tu veux détruire ceux qui la protègent."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mara, tu as une manière extraordinairement vulgaire de résumer les choses."
    julian "Tu ne peux pas décider de retirer notre vie privée sur un coup de tête !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Votre vie privée ? Oh, mes chéris... Les brouilleurs empêchent l'enregistrement et la diffusion de vos conversations privées. Pas mes petites oreilles de vous entendre."
    iris "Attends. Tu veux dire que..."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je peux même vous dire qui ronfle, si vous voulez."
    elias "Ça répond pas vraiment à la question !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Quant aux enregistrements, ils sont indisponibles pendant la période de brouillage. C'est le prix à payer pour une certaine discrétion."
    noam inquiet "Donc si quelqu'un entre dans une chambre..."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Eh bien, il faut espérer que son occupant n'ait pas oublié de fermer la porte !"
    "Je regarde Kael. Il ne détourne pas les yeux de l'écran."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Le vote aura lieu au jour douze. Vous avez le temps de discuter, de vous disputer et de me décevoir !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Profitez-en. Le temps passe si vite quand on s'amuse !"
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elias", "fatigue", -0.11), ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13), ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37), ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60), ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84), ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08), ("sael", "mefiant", 1.20),
    ])
    mara colere "Bon. On autorise, et on arrête de lui donner des excuses pour tuer des gens."
    ryn colere "Pour une fois que je suis d'accord avec toi."
    mara taquin "Fais attention, ça pourrait devenir une habitude."
    tomas reflechit "Il faut quand même parler des risques. Un brouilleur pourrait masquer une infraction, ou empêcher un signal de secours."
    iris colere "Tomas, tu as entendu la partie où elle veut détruire des quartiers entiers ?!"
    tomas inquiet "Oui ! Je ne demande pas d'interdire les brouilleurs. Je demande qu'on sache ce que ça implique !"
    elias reflechit "Il a pas complètement tort. Si une personne se fait agresser dans une zone coupée du réseau..."
    ryn colere "Alors on l'aide nous-mêmes ! On n'a pas besoin de Kami pour ça !"
    call cutin("elias") from _call_kd_cutin_10_elias
    elias colere "ET SI Y A PERSONNE POUR L'AIDER ?!"
    "Ryn se tourne vers lui. Pendant un instant, j'ai peur qu'ils recommencent la dispute de ce matin."
    sael determine "On peut les autoriser et travailler sur une alerte indépendante. Ça n'oblige pas à laisser Kami surveiller chaque pièce."
    nyra raison "Il faudra vérifier que le dispositif ne coupe pas aussi les communications d'urgence."
    kael reflechit "On peut concevoir un canal séparé. À condition d'avoir les composants."
    elias fatigue "Des composants. Génial. On va donc avoir besoin de ceux qui ont disparu."
    "Kael serre les mains sur ses genoux."
    elen inquiet "Vous pensez que quelqu'un les a pris pour fabriquer un brouilleur ?"
    kael calme "On n'en sait rien."
    "Sa voix est calme, mais il vient de répondre plus vite que tous les autres."
    lysa reflechit "C'est la deuxième fois qu'on voudrait résoudre le problème en devinant ce que quelqu'un a fait. Ça ne nous réussit pas vraiment."
    julian inquiet "Nous pouvons au moins nous mettre d'accord sur la nécessité de protéger les gens."
    mara taquin "Un discours de huit mots. Je suis impressionnée."
    julian sourire "Dix, en réalité."
    noam reflexion "J'aurais une question."
    "La discussion continue encore quelques secondes. Personne ne m'entend. Je recommence, plus fort."
    noam inquiet "Est-ce que quelqu'un est passé dans le couloir de l'infirmerie, juste avant l'annonce ?"
    "Elias me regarde. Sael s'immobilise."
    iris inquiet "Pourquoi tu demandes ça ?"
    noam hesitation "Je crois avoir... J'ai eu l'impression qu'il y avait quelqu'un."
    mara stress "Tu as vu quelqu'un ?"
    noam fatigue "J'arrive pas à être sûr."
    julian inquiet "C'est une façon particulièrement inquiétante de demander où nous étions."
    ryn colere "Tu suspectes quelqu'un ?"
    noam neutre "Non. Je voudrais juste savoir."
    tuto "(Vérifie les alibis des représentants présents.)"
    $ j10011_alibis_checked = []
    jump _10_0_1_1_ALIBIS


label _10_0_1_1_ALIBIS:
    if len(j10011_alibis_checked) >= 5:
        jump _10_0_1_1_APRES_ALIBIS
    menu:
        "À qui demander ?"
        "Tomas et Nyra" if "tomas_nyra" not in j10011_alibis_checked:
            tomas gene "J'étais aux archives. Nyra m'a retrouvé juste avant l'annonce."
            nyra raison "Nous avons ensuite rejoint le Conclave ensemble. Aucun passage par l'infirmerie."
            noam reflexion "Vous êtes sûrs de l'heure ?"
            nyra neutre "Aussi sûrs qu'on peut l'être sans consulter un relevé de portes."
            tomas inquiet "On peut en demander un, si ça t'aide..."
            noam neutre "Pas maintenant. Merci."
            $ j10011_alibis_checked.append("tomas_nyra")
            jump _10_0_1_1_ALIBIS
        "Mara et Elen" if "mara_elen" not in j10011_alibis_checked:
            mara stress "Cafétéria. Elen était avec moi."
            elen inquiet "On essayait de trouver de quoi rendre l'air moins étouffant..."
            mara taquin "Elle proposait des éventails en papier. Pour douze personnes. Dans une station spatiale."
            elen desaccord "Tu as dit que c'était une bonne idée !"
            mara neutre "J'ai dit que ça nous occuperait. C'est différent."
            noam neutre "Et vous êtes venues directement ici ?"
            elen neutre "Oui."
            $ j10011_alibis_checked.append("mara_elen")
            jump _10_0_1_1_ALIBIS
        "Elias" if "elias" not in j10011_alibis_checked:
            elias reflechit "Maintenance. J'ai pas quitté le poste depuis que t'es parti."
            noam inquiet "Même quand Kami a commencé à parler ?"
            elias fatigue "Surtout quand Kami a commencé à parler ! Je voulais entendre si elle avait une explication pour cette fichue clim."
            noam neutre "D'accord."
            elias inquiet "Noam, sérieusement... tu cherches quoi ?"
            noam hesitation "Je sais pas."
            $ j10011_alibis_checked.append("elias")
            jump _10_0_1_1_ALIBIS
        "Sael" if "sael" not in j10011_alibis_checked:
            sael mefiant "Je t'ai trouvé devant l'infirmerie. C'est toi qui regardais le couloir."
            noam reflexion "Tu n'as croisé personne d'autre ?"
            sael neutre "Non."
            noam hesitation "Même pas quelqu'un qui partait ?"
            sael determine "Non, Noam. Et si tu m'expliquais enfin pourquoi tu poses ces questions ?"
            noam fatigue "J'essaie de comprendre un truc."
            sael neutre "Alors commence par nous le dire."
            $ j10011_alibis_checked.append("sael")
            jump _10_0_1_1_ALIBIS
        "Iris et Kael" if "iris_kael" not in j10011_alibis_checked:
            iris inquiet "J'ai retrouvé Kael dans le couloir du Conclave. On est arrivés ensemble."
            kael calme "Je n'ai pas quitté ce secteur depuis."
            noam reflexion "Tu n'es pas passé près de l'infirmerie ?"
            kael doute "Non."
            iris desaccord "Noam, qu'est-ce qui se passe avec toi ?"
            noam hesitation "Rien. J'essaie juste de vérifier."
            $ j10011_alibis_checked.append("iris_kael")
            jump _10_0_1_1_ALIBIS


label _10_0_1_1_APRES_ALIBIS:
    "Je repasse les réponses. Certaines se recoupent, d'autres non. Aucune ne me permet de décider si j'ai réellement vu quelqu'un."
    noam reflexion "D'accord... Merci."
    mara stress "Non, c'est pas « merci » ! Tu débarques avec une tête de cadavre, tu demandes où on était tous et tu nous dis rien !"
    lysa neutre "Mara, laisse-lui une seconde."
    mara colere "Je lui ai laissé toute la discussion !"
    elen inquiet "Noam, tu te sens bien ?"
    noam hesitation "Oui. Enfin, je crois."
    iris desaccord "Tu crois beaucoup de choses depuis ton arrivée. Pas une seule réponse claire."
    noam inquiet "Je ne sais même pas ce que je suis censé vous dire !"
    "La phrase sort plus fort que prévu. Je sens aussitôt tous les regards sur moi."
    sael neutre "Tu étais déjà dans cet état dans le couloir."
    elias inquiet "Il avait quoi ?"
    sael reflechit "Il regardait devant lui comme si quelqu'un lui parlait."
    noam desaccord "Personne ne me parlait !"
    "La voix de Sael s'arrête. J'attends la suite, mais les secondes passent."
    noam hesitation "Pourquoi vous me regardez comme ça ?"
    lysa inquiet "Noam..."
    "Je veux lui répondre. Sa bouche bouge encore, mais je ne comprends pas ce qu'elle dit."
    play sound sfx_heartbeat fadein 1.0
    $ blink()
    "Une chaleur brutale me prend à la gorge. J'ai le cœur qui bat si fort que les bruits autour de moi deviennent difficiles à distinguer."
    think "Non, non... Pas ici."
    iris inquiet "Noam ! Assieds-toi !"
    noam fatigue "Je suis déjà..."
    "Je baisse les yeux. Je suis debout, les doigts crispés sur le dossier de ma chaise."
    "Je ne me souviens pas de m'être levé."
    $ blink()
    elias panique "Hé ! Noam, regarde-moi !"
    "Je veux lui demander de reculer. Je n'arrive pas à trouver le mot."
    noam inquiet "Elias, je..."
    "Je sens mes genoux se dérober. Quelqu'un attrape mon bras, mais la table s'éloigne déjà de moi."
    scene black with fade
    pause 3.0
    call end_day("11", sleeping=True) from _call_end_day_1
    jump _11_0_1_1_REVEIL_CHAMBRE
