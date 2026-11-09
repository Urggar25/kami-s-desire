# -----------------------------------------------------------------------
# SALLE D'OBSERVATION — même modèle que CANON
# - 2 persos seulement : Noam + Lysa
# - Découverte : ils sont dans l'espace
# - PNC : radio / vitre / retour
# - Parfois : passage d'un vaisseau (District ORBITE)
# -----------------------------------------------------------------------

default decouverte_salle_observation = False


label OBSERVATION_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_343
    scene bg_observation at adaptive_fullscreen

    if current_scene_active == "_2_ROUTE_OBSERVATION":
        $ current_scene_active = None
        jump _2_SALLE_OBSERVATION

    if not decouverte_salle_observation and day_number() == 1:
        jump decouverte_salle_observation

    $ pnc_room = "pnc_observation"
    call screen pnc_observation()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_observation():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("observation")
    use room_scene_interactions("observation")

    if social_free_time_active() and character_has_available_free_time("julian"):
        imagebutton:
            idle Transform(character_image("julian", "sourire"), zoom=1.00)
            hover Transform(character_image("julian", "taquin"), zoom=1.00)
            focus_mask True
            xalign 0.62
            yalign 1.00
            action [SetVariable("last_room_label", "OBSERVATION_TP"), SetVariable("free_time_selected_character", "julian"), Jump("FREE_TIME_CHARACTER_INTERACT")]



label observation1_porte_couloir_cafeteria:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label observation1_horizon:
    jump OBS_PNC_VITRE


label observation1_ordinateur:
    "Les postes compilent les données orbitales en continu."
    "Trajectoires, distances, vitesses relatives et fenêtres de communication défilent sur les écrans."
    "Je tente d'ouvrir les commandes, mais les fonctions d'émission et de navigation sont verrouillées."
    think "On nous laisse observer tout ce qui passe. Surtout pas lui parler."
    jump OBSERVATION_TP


label observation1_vaisseau_communication:
    "Un vaisseau glisse lentement devant la baie vitrée."
    "Les consoles identifient sa balise, puis affichent une fréquence de communication barrée en rouge."
    "Il est assez proche pour que je distingue les lumières de sa coque. Trop loin pour savoir si quelqu'un regarde dans notre direction."
    think "Un moyen de partir passe sous mes yeux, et je ne peux même pas lui envoyer un signal."
    jump OBSERVATION_TP


label observation2_horizon:
    jump OBS_PNC_VITRE


label observation2_radio:
    jump OBS_PNC_RADIO



label OBS_PNC_RADIO:
    "La console radio est massive."
    "Plusieurs fréquences."
    "Des indicateurs de puissance."
    "Un micro sur bras articulé."
    "Tout est verrouillé."
    think "Donc on peut parler… mais pas appeler."
    jump OBSERVATION_TP


label OBS_PNC_VITRE:
    "Les vitres donnent sur le vide."
    "Pas une vue 'sur le dehors'."
    "Une vue sur l’espace."
    think "Difficile de s'habituer à ça."
    jump OBSERVATION_TP

label OBS_PNC_ORBITE:

    window auto

    "Je m’approche un peu plus de la vitre."
    "Mon regard se fixe sur la masse la plus imposante au loin."

    "Ce n’est pas une station."
    "Pas vraiment."
    "Trop mobile."
    "Trop structurée."

    "C'est sans doute un vaisseau."
    "Ou quelque chose qui en a la fonction."

    "Des lumières courent le long de sa coque."
    "Pas au hasard."
    "Des lignes nettes."
    "Presque… organisées."

    "Autour, d’autres silhouettes plus petites."
    "Elles apparaissent."
    "Disparaissent."
    "Comme si tout ça suivait un rythme précis."

    think "Le district ORBITE."
    think "Du moins, ce que j’imagine que c’est."

    "Rien ne semble nous prêter attention."
    "Aucune manœuvre."
    "Aucun signal visible."

    "Juste cette présence."
    "Lourde."
    "Constante."

    think "Ils sont là."
    think "Ils bougent."
    think "Ils vivent."

    think "Et moi… je regarde."

    pause 0.3

    jump OBSERVATION_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label OBS_PNC_EXIT:
    return


# Zoom doux sur la baie vitrée pendant la première découverte de l'espace.
# Un cadrage sur le décor seul évite d'agrandir les sprites des interlocuteurs.
transform observation_day1_window_zoom:
    zoom 1.0
    xalign 0.5
    yalign 0.42
    ease 2.0 zoom 1.22

# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_observation:

    $ decouverte_salle_observation = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "La salle d'observation doit donner sur l'extérieur. J'ai presque peur de découvrir à quoi ressemble la Terre depuis ici."

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_344
    scene bg_observation at adaptive_fullscreen with fade

    "Une immense baie vitrée occupe le fond de la pièce. Avant même de m'en approcher, j'entends quelqu'un protester devant une console de communication."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "neutre", 0.78),
    ])

    lysa blase "Mais oui, j'ai compris que c'était verrouillé. Tu vas me le répéter combien de fois ?"
    noam hesitation "Tu parles à qui ?"
    lysa surpris "Ah, Noam. À cette foutue radio. Elle refuse d'envoyer quoi que ce soit."
    "Sur l'écran de la console, un numéro de destinataire est déjà composé. Lysa appuie de nouveau sur le bouton d'appel."
    play sound "audio/sfx_beep.mp3"
    "Une notification rouge s'affiche : « ÉMISSION INTERDITE — AUTORISATION REFUSÉE »."
    lysa colere "Mais allez ! Je veux juste passer un appel, pas prendre le contrôle de la station !"
    noam inquiet "Tu essaies de joindre quelqu'un sur Terre ?"
    lysa blase "Non, le service de livraison de pizzas. Évidemment que j'essaie de joindre quelqu'un !"
    "Elle fait défiler les fréquences et cherche une autre option pour lancer l'appel."
    think "Elle n'a pas l'air de vouloir abandonner. Pourtant, j'ai lu quelque chose à ce sujet dans le règlement sur ma tablette."
    noam determine "Lysa, attends !"
    $ hideGroup()
    call day1_noam_radio_interruption from _call_day1_noam_radio_interruption_observation
    $ day1_radio_result = _return
    $ day1_radio_argument = day1_radio_result[1]
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "neutre", 0.78),
    ])

    if day1_radio_result[0] == "success":
        noam determine "Dans le règlement du Conclave, c'est écrit qu'on n'a pas le droit de contacter l'extérieur nous-mêmes. C'est pas simplement la radio qui est verrouillée."
        lysa surpris "Attends, c'est vraiment marqué comme ça ?"
        noam neutre "Oui. On ne peut pas initier un appel. Si quelqu'un nous contacte, on peut répondre, mais on n'a pas le droit de passer le premier appel."
        lysa blase "Génial. Donc si ma sœur m'appelle, je peux lui parler, mais si elle n'y pense pas, je peux juste attendre."
        noam inquiet "Je sais que c'est pénible. Je voulais surtout t'éviter de chercher une fonction que Kami nous interdit d'utiliser."
        lysa fatigue "Bon... au moins, ça explique pourquoi tous les boutons sont bloqués."
    else:
        if day1_radio_argument == "reglement_conclave":
            noam inquiet "J'ai voulu citer le règlement, mais je l'ai interrompue au mauvais moment."
            lysa blase "Si tu veux me dire quelque chose, attends au moins que je finisse ma phrase."
        elif day1_radio_argument == "commandements":
            noam reflexion "Les Dix Commandements doivent peut-être empêcher ce genre de communication."
            lysa blase "Les Commandements ne s'appliquent pas ici, Noam. Kami l'a dit tout à l'heure."
        elif day1_radio_argument == "surveillance":
            noam inquiet "Avec toutes les caméras, Kami doit surveiller nos appels aussi."
            lysa taquin "Bien sûr qu'elle surveille. Mais ça m'aide pas à comprendre pourquoi cette machine refuse de composer le numéro."
        elif day1_radio_argument == "vote_secret":
            noam reflexion "Ça a peut-être un rapport avec le secret des votes. Elle ne veut pas qu'on parle de nos décisions dehors."
            lysa blase "On n'a même pas encore voté. Et je veux appeler ma famille, pas raconter ce qu'on va proposer."
        else:
            noam inquiet "Peut-être que c'est interdit pour éviter qu'on dérègle les équipements de la station."
            lysa blase "Alors pourquoi ils ont laissé une radio ici ? Je demande pas de démonter l'antenne, juste de passer un appel."

        lysa colere "Bon, laisse-moi essayer une dernière fois."
        "Elle relance l'appel sur une autre fréquence. La même notification rouge revient aussitôt."
        lysa fatigue "Bon, c'est mort. J'ai essayé tout ce que j'ai trouvé, et ça veut rien savoir."
        noam neutre "Désolé, j'aurais aimé pouvoir t'aider."
        lysa taquin "Tu peux toujours m'aider en évitant de raconter à tout le monde que je me suis disputée avec une radio."

    "Lysa referme le menu de communication. J'aperçois un nom dans la liste des contacts, mais elle efface rapidement le champ."
    lysa blase "Tu peux éviter de regarder par-dessus mon épaule, s'il te plaît ?"
    noam neutre "Oui, pardon. Je voulais pas être indiscret."
    lysa fatigue "C'est rien. J'avais juste quelqu'un à appeler et j'ai pas réussi."

    "Elle s'éloigne de l'écran et se place devant la baie vitrée."
    lysa reflexion "Viens voir ça, plutôt. Au moins, c'est quelque chose qu'on nous laisse regarder."
    $ hideGroup()
    scene bg_observation at adaptive_fullscreen

    "Je m'avance. La Terre s'étend derrière la vitre, immense et pourtant inaccessible. Un vaisseau traverse lentement notre champ de vision, si près que je distingue ses balises."
    "Pendant un instant, j'oublie complètement la dispute de Lysa avec la console."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "reflexion", 0.78),
    ])

    noam surpris "Ah ouais... Je savais qu'on était dans l'espace, mais la voir comme ça, c'est autre chose."
    lysa sourire "C'est la première fois que je trouve un truc réussi dans toute cette histoire."
    noam inquiet "Ça donne aussi une sacrée impression de vide. Tu ressens pas ça, toi ?"
    lysa taquin "Si. Mais je préfère encore regarder le vide que les gens qui vont nous demander de voter pendant un mois."
    noam rire "Tu es vraiment incapable de profiter d'un moment tranquille, hein ?"
    lysa sourire "Je fais des efforts, regarde. J'ai tenu presque dix secondes."

    "Un autre vaisseau apparaît, ralentit près de notre trajectoire et repart vers la Terre."
    noam reflexion "Tu voulais appeler quelqu'un qui se trouve sur Terre, c'est ça ?"
    lysa triste "Ouais. Je pensais qu'il y aurait forcément un moyen de passer un appel depuis une station comme celle-ci, mais j'aurais dû me douter que Kami aurait tout verrouillé."
    noam neutre "Je comprends que tu aies voulu essayer. Avec tous les vaisseaux qu'on voit, c'est difficile de croire qu'on ne peut parler à personne."
    lysa blase "C'est surtout frustrant de savoir qu'ils peuvent nous voir, alors que nous, on peut même pas leur demander comment ils vont."
    "Elle garde les yeux sur le petit point lumineux qui s'éloigne."
    lysa reflexion "C'était ma sœur que j'essayais d'appeler. On s'est quittées comme des connes, avec une dispute à propos de rien. Je voulais juste lui dire que..."
    "Elle souffle et se met à rire, sans grande conviction."
    lysa taquin "Super, hein ? Une vue imprenable sur la Terre et moi qui me prends la tête pour une engueulade."
    noam neutre "Tu peux t'inquiéter pour elle. T'as pas besoin de faire comme si c'était ridicule."
    lysa fatigue "Je sais. C'est juste que j'ai horreur qu'on me voie comme ça."
    noam sourire "Je peux faire semblant de n'avoir rien entendu."
    lysa sourire "Ça, ce serait sympa."
    "Nous regardons encore le vaisseau disparaître, jusqu'à ce qu'il devienne impossible à distinguer des autres lumières."
    lysa reflexion "J'espère qu'elle va bien."
    noam neutre "Moi aussi."

    "Lysa rejoint la baie vitrée et me donne un petit coup d'épaule."
    lysa taquin "Bon. Si quelqu'un te demande, j'étais en train d'étudier les trajectoires spatiales. Avec beaucoup de sérieux."
    noam rire "Évidemment. Je n'ai jamais vu quelqu'un d'aussi professionnel."
    lysa sourire "Parfait. Maintenant, laisse-moi deux minutes avec ma vue."
    "Je lui laisse la place. En revenant vers la porte, je remarque que la console de communication affiche toujours « ÉMISSION INTERDITE »."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_6
    $ hideGroup()
    jump OBSERVATION_TP
