# =============================================================================
# JOUR 21 — Route 0_1_1_0_1
# Réponse à Kael : "Je monte dans la navette."
#
# Les Doppelgängers choisissent de ne pas prolonger le Conclave.
# Ceux qui ont déjà pris la place de leur original partiront aujourd'hui.
# Le Doppelgänger de Noam n'a, lui, toujours pas remplacé Noam.
# =============================================================================

default j21_leave_qte_success = False

define dg_noam = Character("Noam")


label _21_0_1_1_0_1_REVEIL:

    $ cafeteria_food_level = "null"
    $ current_period = "Matin"
    $ current_day = 21
    $ day_id = 21
    $ j20_kael_depart_choice = "leave"
    $ noam_has_juliette_drawing = False

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Je me réveille avant l'annonce de Kami."

    "Pendant quelques secondes, je reste allongé sans bouger, les yeux ouverts dans le noir."

    think "Aujourd'hui."

    "C'est la première pensée qui me vient."

    "Pas Mara. Pas la salle des Goumi. Pas M16."

    "Aujourd'hui, on rentre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je me redresse lentement et regarde la grille d'aération au fond de la chambre."

    "Elle est exactement comme hier."

    "Enfin... je crois."

    "Je la fixe encore quelques secondes avant de détourner les yeux."

    noam fatigue "Non."

    "Pas aujourd'hui."

    "Je me lève."

    play sound sfx_kami_on
    $ camera_glitch(strength="light", duration=0.35)

    kami "REPRÉSENTANTS."

    noam surpris "..."

    kami "LE VAISSEAU DE RETOUR S'AMARRERA AU CONCLAVE À QUATORZE HEURES."

    kami "LE DÉPART EST PROGRAMMÉ À SEIZE HEURES."

    pause 0.5

    kami "JE VOUS CONSEILLE DE NE RIEN OUBLIER."

    kami "JE N'AI AUCUNE INTENTION DE FAIRE DEMI-TOUR POUR VOS AFFAIRES."

    "Puis le haut-parleur se coupe."

    "Je reste debout au milieu de ma chambre."

    think "Seize heures."

    "Quelques heures."

    "C'est tout ce qu'il reste."

    stop music fadeout 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j21_leave_door_chambre_couloir
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Quand je sors, plusieurs portes sont déjà ouvertes."

    "Pour la première fois depuis longtemps, le couloir ressemble presque à celui d'un hôtel le matin d'un départ."

    "Des gens passent d'une chambre à l'autre. On parle de sacs, de vêtements oubliés, de ce qu'on fera une fois en bas."

    "Personne ne parle de vote."

    "Rien que ça me paraît irréel."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_daily_light.mp3" fadein 1.2

    $ showGroup([
        ("noam", "fatigue", 0.12),
        ("iris", "blase", 0.28),
        ("elen", "joie", 0.44),
        ("tomas", "reflexion", 0.60),
        ("kael", "calme", 0.76),
        ("mara", "neutre", 0.92),
    ])

    elen joie "J'ai officiellement décidé que mon premier repas sur Terre serait tellement gras que Sael fera un malaise juste en le regardant."

    tomas reflexion "C'est rassurant de voir que trois semaines ici n'ont absolument rien changé chez toi."

    elen rire "Si. Maintenant j'apprécie la nourriture."

    iris blase "Tu l'appréciais déjà beaucoup trop avant."

    elen "Jalouse."

    "Je m'assois avec eux."

    "Même Mara est là."

    "Vivante."

    "Elle discute avec Tomas comme si je ne l'avais pas vue morte hier matin."

    "Je détourne les yeux avant qu'elle remarque que je la fixe."

    iris inquiet "T'as dormi ?"

    noam fatigue "Un peu."

    iris "Ça veut dire non."

    noam "Ça veut dire un peu."

    iris blase "T'es insupportable."

    noam "Bonjour à toi aussi."

    "Elle pousse une tasse dans ma direction."

    iris "Bois."

    noam surpris "C'est quoi ?"

    iris "Du café."

    noam "Je vois bien que c'est du café."

    iris blase "Alors pourquoi tu demandes ?"

    noam "Je vérifie juste que t'as pas décidé de m'empoisonner avant le départ."

    iris "J'y ai pensé."

    "Je prends la tasse."

    "Elle me regarde boire comme si c'était une victoire personnelle."

    kael calme "Noam."

    "Je tourne la tête."

    kael doute "Tu... ça va mieux ?"

    noam "Je sais pas."

    kael "Ouais."

    "Il joue avec le bord de son verre."

    kael inquietude "Pour hier..."

    noam reflexion "Ta question bizarre ?"

    "Kael baisse les yeux."

    kael doute "Ouais."

    iris reflexion "Quelle question bizarre ?"

    noam "Il voulait savoir si je monterais dans la navette en sachant que quelqu'un restait coincé ici."

    iris surpris "..."

    iris blase "Putain, Kael. Vous pouvez pas parler de météo comme les gens normaux ?"

    kael sourire "J'avais pas grand-chose à dire sur la météo."

    "Iris lève les yeux au ciel."

    kael doute "Je voulais juste dire..."

    "Il hésite."

    kael "Je crois que t'avais raison."

    noam reflexion "Sur quoi ?"

    kael inquietude "Quand une sortie existe..."

    "Il s'arrête encore, puis hausse légèrement les épaules."

    kael "Parfois, faut juste la prendre."

    noam "Ouais."

    "Il hoche la tête."

    "Quelque chose dans sa façon de le faire me dérange."

    "Pas assez pour que je sache pourquoi."

    "Iris tape deux fois du doigt sur la table."

    iris "Bon. Nouvelle règle."

    noam blase "Oh non."

    iris determine "Aujourd'hui, tu ne fais rien de stupide."

    noam "C'est très large."

    iris "Pas de conduit. Pas de salle cachée. Pas de cadavre. Pas de couteau."

    noam surpris "Le couteau..."

    iris inquiet "Quoi ?"

    "Je repense soudainement à la salle."

    noam reflexion "Je l'ai laissé en bas."

    iris blase "Oui."

    noam "Je devrais peut-être le récupérer."

    iris colere "Non."

    noam "C'est quand même mon—"

    iris determine "Non."

    "Je la regarde."

    "Elle ne plaisante pas."

    noam fatigue "D'accord."

    iris "Merci."

    "Elle reprend son verre."

    "Je vois Kael relever très légèrement les yeux."

    "Puis il recommence à boire."

    $ hideGroup()

    jump _21_0_1_1_0_1_MILIEU_JOURNEE


label _21_0_1_1_0_1_MILIEU_JOURNEE:

    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 1.0

    "Le reste de la matinée passe beaucoup trop vite."

    "Tout le monde récupère ses affaires."

    "Kami fait vérifier les badges une première fois, puis une deuxième, parce qu'elle considère apparemment que nous sommes incapables de garder un morceau de plastique sur nous pendant quatre heures."

    play sound sfx_kami_on

    kami "AMARRAGE DU VAISSEAU CONFIRMÉ."

    kami "DEUX HEURES AVANT LE DÉPART."

    "Deux heures."

    "Je devrais être soulagé."

    "Je le suis."

    "Mais quelque chose continue de me gratter derrière le crâne."

    play sound "audio/sfx_duct_scrape.wav" volume 0.42

    "Un bruit métallique résonne au-dessus de moi."

    "Je m'arrête."

    noam inquiet "..."

    "Le couloir est vide."

    "Je lève les yeux vers la grille la plus proche."

    "Rien."

    think "Pas aujourd'hui."

    "Je repars."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Quand je rentre dans ma chambre, je m'arrête sur le seuil."

    "La grille d'aération est légèrement ouverte."

    noam panne "..."

    "Quelques millimètres."

    "Peut-être un centimètre."

    "Je pourrais jurer qu'elle était fermée ce matin."

    "Je pose mon sac sur le lit."

    think "Ou peut-être pas."

    think "M16."

    "Je déteste immédiatement cette pensée."

    "Avant, quand quelque chose n'allait pas, je pouvais au moins faire confiance à mes propres yeux."

    "Maintenant, même une grille mal fermée suffit à me faire douter de ma tête."

    play sound sfx_door

    show iris neutre at center with dissolve

    iris "T'es prêt ?"

    noam "Presque."

    "Elle remarque que je regarde derrière elle."

    iris inquiet "Quoi encore ?"

    noam fatigue "Rien."

    iris "Noam."

    noam "La grille était peut-être fermée tout à l'heure."

    "Iris regarde l'aération."

    iris reflexion "Peut-être ?"

    noam "Voilà."

    iris "Et tu veux aller vérifier."

    noam desaccord "Non."

    iris surpris "..."

    noam "J'ai dit que j'arrêtais. J'arrête."

    "Elle me regarde quelques secondes."

    iris fatigue "Bonne réponse."

    noam "Tu vois ? Je peux apprendre."

    iris blase "J'attends encore la preuve."

    "Je ferme mon sac."

    iris "J'ai encore deux trucs à récupérer dans ma chambre."

    noam "Vas-y."

    iris inquiet "Je reviens."

    noam blase "Je vais pas disparaître."

    iris "C'est exactement le genre de phrase qu'on dit avant de disparaître."

    noam "Dix minutes."

    iris determine "Dix minutes."

    "Elle pointe un doigt vers moi."

    iris "Et si t'entends quoi que ce soit dans le mur..."

    noam "Je viens te chercher."

    iris "Tu touches à rien."

    noam "Je touche à rien."

    iris "Tu rampes nulle part."

    noam "Je rampe nulle part."

    iris blase "Ça devient inquiétant que je sois obligée de préciser tout ça."

    noam "Va chercher tes affaires."

    "Elle finit par sourire légèrement."

    iris "J'arrive."

    hide iris with dissolve
    play sound sfx_door

    "La porte se referme."

    pause 0.8

    "Je reste seul."

    jump _21_0_1_1_0_1_DOPPELGANGER


label _21_0_1_1_0_1_DOPPELGANGER:

    scene bg_chambre at adaptive_fullscreen
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.2
    $ danger_on()

    "Je range un dernier vêtement dans mon sac."

    play sound "audio/sfx_duct_scrape.wav" volume 0.62

    "Le bruit revient."

    "Cette fois, juste derrière moi."

    "Je ferme les yeux."

    noam fatigue "Iris va me tuer..."

    "Je me retourne vers la grille."

    "Elle bouge."

    noam panne "..."

    "Pas un souvenir."

    "Pas une impression."

    "Elle bouge vraiment."

    play sound "audio/sfx_metal_open.mp3"

    "La plaque bascule vers l'extérieur."

    "Deux mains apparaissent dans l'ouverture."

    "Puis une tête."

    pause 0.8

    noam peur "..."

    "Mon cerveau refuse l'image avant même que je comprenne pourquoi."

    "Quelqu'un sort du conduit et retombe lourdement dans ma chambre."

    "Il se redresse."

    $ doppelganger_reveal(screamer=False, duration=0.85, restore_volume=0.65)

    show noam fatigue at center with creep_diss

    "Je me regarde."

    noam panne "..."

    "Même visage."

    "Même taille."

    "Même cheveux."

    "Il respire vite."

    "Beaucoup trop vite."

    "Et dans sa main..."

    "Il y a mon couteau."

    noam peur "C'est..."

    "Je reconnais immédiatement les petites rayures sur le manche."

    noam "C'est mon couteau."

    dg_noam "Ouais."

    "Sa voix me coupe presque les jambes."

    "Ma voix."

    "Pas exactement comme je l'entends quand je parle."

    "Comme dans un enregistrement."

    noam desespoir "T'es quoi ?"

    "L'autre Noam serre le manche."

    dg_noam "Bouge pas."

    noam "T'es quoi, putain ?!"

    dg_noam "J'ai pas le temps de t'expliquer."

    noam colere "Alors pose le couteau !"

    dg_noam "Je peux pas."

    "Sa main tremble."

    "Il n'a pas l'air heureux."

    "Il n'a même pas l'air particulièrement sûr de ce qu'il fait."

    "Il a peur."

    "Cette constatation me terrifie encore plus."

    noam inquiet "Pourquoi tu me ressembles ?"

    dg_noam "Parce que je suis toi."

    noam colere "Non."

    dg_noam "J'ai tes souvenirs."

    noam "Non."

    dg_noam "Je me souviens de notre mère."

    noam colere "Ferme-la."

    dg_noam "Je me souviens de la maison."

    noam "FERME-LA."

    dg_noam "Je me souviens de Juliette."

    "Je me fige."

    noam panne "..."

    dg_noam "Je me souviens de son visage."

    noam peur "Ne parle pas d'elle."

    dg_noam "Pourquoi ?"

    noam colere "Parce que c'est ma sœur !"

    "Sa mâchoire se crispe."

    dg_noam "Et tu crois que pour moi c'est quoi ?"

    noam "T'as volé mes souvenirs !"

    dg_noam "Je les ai pas volés !"

    "Il crie plus fort que prévu."

    "Puis regarde immédiatement la porte."

    "Il baisse la voix."

    dg_noam "Je les ai. C'est tout."

    noam inquiet "Qu'est-ce que tu veux ?"

    "Il me regarde."

    "Ses yeux sont humides."

    dg_noam "Partir."

    noam "..."

    dg_noam "La navette part dans moins de deux heures."

    noam "Alors pars."

    dg_noam "Je peux pas."

    "Il lève légèrement le couteau."

    noam panne "..."

    dg_noam "Pas tant que t'es là."

    "Je comprends."

    "Pas tout."

    "Mais assez."

    noam peur "Tu veux prendre ma place."

    dg_noam "Je dois prendre ta place."

    noam "Tu dois rien du tout."

    dg_noam "Si je le fais pas maintenant, ils partent sans moi."

    noam reflexion "Ils ?"

    "Il ne répond pas."

    "Kael me revient immédiatement en tête."

    "Sa question."

    "Son hésitation."

    "Et sa phrase de ce matin."

    think "Quand une sortie existe..."

    noam panne "Kael..."

    "Le visage devant moi change à peine."

    "Ça suffit."

    noam desespoir "C'était pour ça."

    dg_noam "..."

    noam "Sa question hier."

    dg_noam "Il voulait savoir ce que tu ferais."

    noam "Et vous avez décidé quoi ?"

    "L'autre Noam baisse les yeux une fraction de seconde."

    dg_noam "De partir."

    noam colere "En me tuant."

    dg_noam "Je veux pas te tuer."

    noam "Ah ouais ? Le couteau c'est pour m'aider à fermer mon sac ?"

    dg_noam "Arrête."

    noam "Non, réponds-moi !"

    dg_noam "J'AI PAS D'AUTRE PLACE !"

    "Sa voix se casse."

    "Il avance d'un pas."

    dg_noam "Si tu montes dans cette navette, moi je reste ici."

    noam "C'est pas mon problème."

    "Il me regarde comme si je venais de le frapper."

    dg_noam "Tu l'as dit hier."

    noam reflexion "Quoi ?"

    dg_noam "Quand t'as une sortie, tu la prends."

    noam "Ça n'a rien à voir."

    dg_noam "Pourquoi ?"

    noam colere "Parce que tu veux me tuer !"

    dg_noam colere "PARCE QUE MOI AUSSI JE VEUX VIVRE !"

    pause 0.5

    "Le silence retombe brutalement."

    "Il respire par à-coups."

    "Ses doigts tremblent autour du manche."

    dg_noam "Moi aussi je veux serrer Juliette dans mes bras !"

    noam panne "..."

    dg_noam "Moi aussi j'ai envie de rentrer."

    dg_noam "Moi aussi j'ai passé tout ce temps à penser à elle."

    noam peur "T'es pas moi."

    dg_noam "Je sais."

    "Il avale difficilement."

    dg_noam "Mais ça rend pas ce que je ressens moins réel."

    "Il regarde la porte."

    "Puis moi."

    dg_noam "Désolé."

    noam peur "Attends."

    "Il avance."

    jump _21_0_1_1_0_1_QTE


label _21_0_1_1_0_1_QTE:

    scene bg_chambre at adaptive_fullscreen with vpunch

    "Je recule au moment où il se jette sur moi."

    play sound "audio/sfx_thud.mp3" volume 0.95
    $ shake(8, 0.20)

    "Son épaule me percute en plein torse."

    "Je lui attrape le poignet avant que la lame descende."

    noam colere "LÂCHE ÇA !"

    dg_noam "ARRÊTE DE BOUGER !"

    noam "T'ES SÉRIEUX ?!"

    "Nos mains tremblent entre nous."

    "Le couteau descend lentement."

    "Je pousse de toutes mes forces."

    dg_noam "J'AI PAS LE TEMPS !"

    noam "ALORS CASSE-TOI !"

    dg_noam "OÙ ?!"

    $ j21_leave_qte_success = False

    python:
        j21_leave_trace_steps = [
            {"path_type": "curve_right", "time_limit": 1.15, "wait_time": 0.24, "tolerance": 29, "max_errors": 1, "anchor_x": 750, "anchor_y": 625, "start_radius": 68},
            {"path_type": "s_curve", "time_limit": 1.02, "wait_time": 0.20, "tolerance": 27, "max_errors": 1, "anchor_x": 1110, "anchor_y": 610, "start_radius": 64},
            {"path_type": "arc", "time_limit": 0.92, "wait_time": 0.18, "tolerance": 25, "max_errors": 1, "anchor_x": 840, "anchor_y": 640, "start_radius": 62},
            {"path_type": "curve_left", "time_limit": 0.84, "wait_time": 0.16, "tolerance": 23, "max_errors": 1, "anchor_x": 1080, "anchor_y": 625, "start_radius": 60},
            {"path_type": "s_curve", "time_limit": 0.76, "wait_time": 0.14, "tolerance": 21, "max_errors": 1, "anchor_x": 920, "anchor_y": 610, "start_radius": 56},
        ]

    call trace_qte_sequence(
        j21_leave_trace_steps,
        "bg_chambre",
        start_zoom=1.0,
        zoom_step=0.055,
        show_tutorial=False
    ) from _call_trace_qte_sequence_j21_leave
    $ j21_leave_trace_result = _return

    if j21_leave_trace_result["success"]:
        $ j21_leave_qte_success = True
        jump _21_0_1_1_0_1_QTE_REUSSITE

    jump _21_0_1_1_0_1_QTE_ECHEC


label _21_0_1_1_0_1_QTE_ECHEC:

    scene bg_chambre at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 1.0
    $ shake(12, 0.28)

    "Mon pied glisse."

    "Ça suffit."

    "Mon dos heurte le bord du lit et ma prise lâche une fraction de seconde."

    noam peur "Non—"

    play sound "audio/sfx_tinnitus.wav" volume 0.60
    $ impact(intensity=10, duration=0.24, color="#8f101c")

    "La lame entre sous mes côtes."

    noam panne "..."

    "Je ne sens presque rien au début."

    "Juste un choc."

    "Puis la douleur arrive."

    "Mes jambes lâchent."

    "L'autre Noam me retient avant que je tombe complètement."

    dg_noam "Merde..."

    "Il me descend lentement jusqu'au sol."

    noam peur "Iris..."

    dg_noam "Chut."

    noam "Iris..."

    "J'essaie de pousser sa main."

    "Je n'ai déjà plus assez de force."

    dg_noam "Je suis désolé."

    noam desespoir "Juliette..."

    "Son visage se déforme."

    dg_noam "Je sais."

    noam "T'approche pas d'elle..."

    dg_noam "Je la protégerai."

    noam colere "T'es pas..."

    "Ma voix disparaît."

    "Je veux finir la phrase."

    "Je n'y arrive pas."

    scene black with suffocation_cut
    stop music fadeout 1.5
    $ danger_off()

    "Je pense à Juliette."

    "Puis plus rien."

    pause 2.0

    jump _21_0_1_1_0_1_FIN_A_MA_PLACE


label _21_0_1_1_0_1_FIN_A_MA_PLACE:

    # La narration quitte Noam : l'original est mort.
    scene bg_chambre at adaptive_fullscreen with creep_diss
    play music "audio/music/bgm_epilogue_cold.mp3" fadein 2.0

    "Noam reste assis au sol pendant plusieurs secondes."

    "Il regarde le corps devant lui."

    "Son propre visage."

    "Ses propres mains."

    "Du sang sur ses doigts."

    "Il ferme les yeux."

    play sound "audio/sfx_duct_scrape.wav" volume 0.58

    "Un mouvement vient du conduit."

    show kael doute at left with dissolve
    show noam fatigue at right with dissolve

    "Kael sort à son tour."

    "Il comprend immédiatement."

    kael doute "T'as réussi."

    "Noam ne répond pas."

    kael inquietude "On a moins d'une heure."

    dg_noam "Je sais."

    "Kael regarde le corps."

    kael "Il faut le bouger."

    "Noam baisse les yeux vers ses vêtements tachés."

    dg_noam "Iris va revenir."

    kael "Alors dépêche-toi."

    scene black with dissolve

    "Quelques minutes plus tard, le corps disparaît dans le conduit."

    "Les vêtements aussi."

    "Le sang est nettoyé comme il peut l'être."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Noam récupère le badge."

    "Le téléphone."

    "Le sac."

    "Tout ce qui appartient à Noam."

    "Tout ce qui lui appartient maintenant."

    "L'écran du téléphone s'allume."

    "Une photo de Juliette apparaît."

    pause 0.7

    dg_noam "..."

    "Il passe son pouce sur l'écran."

    dg_noam "J'arrive."

    play sound sfx_door

    show iris inquiet at left with dissolve

    iris "Noam ?"

    "Il verrouille immédiatement le téléphone."

    dg_noam "Ouais."

    iris "J'ai entendu un truc."

    dg_noam "J'ai fait tomber mon sac."

    "Elle regarde la chambre."

    "Puis son visage."

    iris reflexion "Ça va ?"

    "Il hésite une fraction de seconde."

    dg_noam "Oui."

    iris blase "T'as encore cette tête bizarre."

    dg_noam "Quelle tête ?"

    iris "Celle où t'essaies de me convaincre que tout va bien."

    "Noam sourit faiblement."

    dg_noam "On rentre, Iris."

    "Elle le fixe encore une seconde."

    iris fatigue "Ouais."

    iris "On rentre."

    scene black with dissolve

    play sound sfx_kami_on

    kami "DIX MINUTES AVANT FERMETURE DU SAS."

    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with fade

    "Les représentants prennent place à bord."

    "Noam s'assoit."

    "Iris juste en face de lui."

    "Kael quelques sièges plus loin."

    "La navette se détache du Conclave."

    "La Terre grandit derrière les hublots."

    "Noam sort discrètement son téléphone."

    "La photo de Juliette est toujours là."

    "Cette fois, son sourire n'a rien de victorieux."

    "Il a seulement l'air terrifié."

    dg_noam "Encore un peu..."

    scene black with signal_stutter
    stop music fadeout 0.25

    pause 1.0

    call screen kd_ending_reached(
        "À ma place",
        "ENDING 03 // JOUR 21"
    )
    $ _ending_screen_closed = _return

    return


label _21_0_1_1_0_1_QTE_REUSSITE:

    scene bg_chambre at adaptive_fullscreen with vpunch

    "Je pousse son poignet sur le côté au dernier moment."

    play sound sfx_drop

    "Le couteau m'échappe presque, mais je réussis à frapper sa main contre le bord du lit."

    "La lame tombe au sol."

    dg_noam "NON !"

    "Il se jette sur moi à mains nues."

    play sound "audio/sfx_thud.mp3" volume 0.92
    $ shake(9, 0.20)

    "On s'écrase tous les deux contre le mur."

    noam colere "ARRÊTE !"

    dg_noam "JE PEUX PAS !"

    "Il essaie de me faire tomber."

    "Je l'attrape par le col."

    "Pendant une seconde, j'ai mon propre visage à quelques centimètres du mien."

    "Même peur."

    "Même rage."

    "Même envie de sortir d'ici."

    play sound sfx_door
    scene bg_chambre at adaptive_fullscreen with vpunch

    iris colere "NOAM ?!"

    "On se fige tous les deux."

    "Iris reste dans l'encadrement."

    "Son sac tombe de sa main."

    iris panne "..."

    "Elle me regarde."

    "Puis lui."

    "Puis encore moi."

    iris peur "C'est quoi ce bordel...?"

    dg_noam "Iris—"

    noam desespoir "IL A MON COUTEAU !"

    "Le regard d'Iris tombe au sol."

    "Sur la lame."

    "Puis sur l'autre Noam qui essaie déjà de se dégager."

    dg_noam "Attends !"

    "Iris n'attend pas."

    play sound "audio/sfx_thud.mp3" volume 1.0
    $ impact(intensity=8, duration=0.20, color="#6f91a8")

    "Son pied frappe l'autre Noam derrière le genou."

    "Il s'effondre."

    play sound "audio/sfx_thud.mp3" volume 0.92

    "Je lui bloque immédiatement le bras."

    iris colere "Tiens-le !"

    noam "J'essaie !"

    dg_noam "LÂCHEZ-MOI !"

    "Iris attrape une sangle du sac et me la tend."

    "À deux, on finit par lui coincer les poignets derrière le dos."

    "Il se débat encore quelques secondes."

    "Puis il comprend."

    "Il s'arrête."

    $ danger_off()
    stop music fadeout 1.0

    show iris peur at left with dissolve
    show noam fatigue at right with dissolve

    "Iris reste debout devant lui."

    "Elle a blêmi."

    iris panne "Noam..."

    noam fatigue "Je sais."

    iris "Non, je..."

    "Elle regarde le double."

    iris peur "Je sais même pas quoi demander."

    dg_noam "On n'a pas le temps."

    iris colere "Toi, ferme-la."

    "Il rit une fois."

    "Sans joie."

    dg_noam "Ouais."

    play sound sfx_kami_on

    kami "TRENTE MINUTES AVANT FERMETURE DU SAS."

    "Le message nous coupe tous les trois."

    "L'autre Noam ferme les yeux."

    noam reflexion "Combien ?"

    dg_noam "..."

    noam "Combien vous êtes ?"

    dg_noam "Ça change quoi ?"

    noam colere "KAEL EN EST UN ?"

    "Il ne répond pas."

    "Encore une fois, ça suffit."

    iris surpris "Kael ?"

    noam "Sa question hier."

    iris "Noam, de quoi tu—"

    noam "Il savait."

    "Je regarde mon double."

    noam "Il savait exactement pourquoi il me demandait ça."

    dg_noam "Et tu lui as répondu."

    noam panne "..."

    dg_noam "Tu lui as dit de partir."

    iris colere "Arrête de parler comme si c'était sa faute !"

    dg_noam "J'ai pas dit ça."

    "Il relève les yeux vers moi."

    dg_noam "Je dis juste qu'il avait raison."

    noam reflexion "Tu viens d'essayer de me tuer."

    dg_noam "Parce que moi aussi je veux vivre."

    "Sa voix est beaucoup plus basse maintenant."

    dg_noam "C'est tout."

    "Iris serre la mâchoire."

    dg_noam "Si je reste ici, c'est fini pour moi."

    noam "Et si tu pars, c'est fini pour moi."

    "Il baisse les yeux."

    dg_noam "Ouais."

    "Personne ne parle pendant quelques secondes."

    play sound sfx_kami_on

    kami "VINGT MINUTES AVANT FERMETURE DU SAS."

    iris inquiet "On fait quoi ?"

    "Je regarde l'autre Noam."

    "Il comprend immédiatement."

    dg_noam peur "Non."

    noam "..."

    dg_noam "Non, attends."

    "Il tire sur ses liens."

    dg_noam "Tu vas vraiment me laisser ici ?"

    "La question me frappe beaucoup plus fort que prévu."

    "Hier, Kael m'a posé exactement la même."

    "Sans visage."

    "Sans couteau."

    "Sans me dire qui resterait derrière."

    dg_noam "Noam."

    "Je me relève."

    dg_noam "S'il te plaît."

    noam fatigue "Je t'ai déjà répondu hier."

    "Il se fige."

    noam "Sans savoir que je te répondais à toi."

    dg_noam "..."

    noam "La navette part."

    dg_noam colere "PUTAIN !"

    "Il se débat brutalement."

    iris inquiet "Noam..."

    noam determine "On y va."

    "Iris reste immobile."

    noam "Si on rate cette navette, ça fera juste..."

    "Je n'arrive pas à finir."

    "Je regarde mon propre visage au sol."

    "Il sait très bien comment se termine la phrase."

    dg_noam fatigue "Deux personnes coincées au lieu d'une."

    noam panne "..."

    "Je ramasse mon sac."

    iris triste "Je suis désolée."

    dg_noam "Ouais."

    "Iris ramasse le couteau."

    "Puis elle me rejoint dans le couloir."

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_epilogue_cold.mp3" fadein 1.5

    "Je ferme la porte derrière nous."

    "Je n'arrive pas à regarder Iris."

    iris inquiet "Tu crois qu'on devrait prévenir les autres ?"

    noam "Oui."

    iris "Mais ?"

    noam "Mais on a quinze minutes et je sais même pas qui est encore..."

    "Je m'arrête."

    iris peur "Humain ?"

    "Je déteste le mot."

    noam "Ouais."

    "On accélère."

    play sound sfx_kami_on

    kami "QUINZE MINUTES AVANT FERMETURE DU SAS."

    "Au bout du couloir, Kael apparaît."

    show kael calme at center with dissolve

    "Il marche vers le sas avec son sac sur l'épaule."

    "Puis il me voit."

    "Il s'arrête."

    kael panne "..."

    "Ses yeux passent sur mon visage."

    "Puis sur Iris."

    "Puis sur le couteau qu'elle tient encore."

    "Quelque chose change dans son expression."

    "Pas de surprise."

    "Plutôt une déception très brève."

    noam panne "..."

    "On se regarde."

    kael doute "T'as réussi à être prêt."

    noam "Ouais."

    "Il hoche lentement la tête."

    kael "Alors viens."

    "Il reprend sa marche."

    "Iris me regarde."

    iris inquiet "Noam ?"

    noam fatigue "Après."

    "Je repars."

    jump _21_0_1_1_0_1_FIN_LAISSE_DERRIERE


label _21_0_1_1_0_1_FIN_LAISSE_DERRIERE:

    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with fade

    "Les portes se ferment derrière nous."

    "Je reste debout une seconde de trop avant de m'asseoir."

    "Iris prend la place à côté de moi."

    "Kael est plus loin."

    "Je ne le quitte presque pas des yeux."

    iris inquiet "On va devoir parler."

    noam fatigue "Je sais."

    iris "À tout le monde."

    noam "Je sais."

    "Elle pose sa main sur la mienne."

    "Je la laisse faire."

    play sound sfx_kami_on

    kami "DÉPART."

    "La navette tremble."

    "Puis le Conclave commence à s'éloigner."

    scene black with dissolve

    "Dans ma chambre, quelqu'un tire encore sur ses liens."

    scene bg_chambre at adaptive_fullscreen with creep_diss

    show noam fatigue at center with dissolve

    "L'autre Noam a cessé de crier."

    "Il est assis contre le bord du lit, les poignets toujours attachés."

    "Le silence de la station revient peu à peu."

    play sound sfx_kami_on

    kami "VAISSEAU DÉSARRIMÉ."

    "Il ferme les yeux."

    dg_noam "..."

    "Puis il laisse échapper un petit rire épuisé."

    dg_noam "Ouais."

    "Il regarde la porte fermée."

    dg_noam "Deux personnes coincées au lieu d'une."

    "Son sourire disparaît."

    scene black with signal_stutter
    stop music fadeout 0.25

    pause 1.0

    call screen kd_ending_reached(
        "Celui qu'on laisse derrière",
        "ENDING 04 // JOUR 21"
    )
    $ _ending_screen_closed = _return

    return
