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

    lysa blase "Mais oui, je sais que c'est verrouillé. Tu peux arrêter de me le répéter ?"
    noam hesitation "Tu parles à qui ?"
    lysa surpris "Ah, Noam. À personne. Enfin, à une machine qui a décidé de me prendre pour une idiote."
    noam sourire "Qu'est-ce que tu essaies de faire ?"
    lysa taquin "Commander une pizza. Tu veux quoi dessus ?"
    noam taquin "D'accord, j'ai compris. T'essaies de contacter quelqu'un."
    "Lysa ramène aussitôt la console à son menu principal, mais j'ai eu le temps d'apercevoir un nom dans le champ du destinataire."
    lysa blase "Tu peux éviter de regarder par-dessus mon épaule ?"
    noam neutre "Désolé. Je voulais pas être indiscret."
    lysa fatigue "Ouais, bon... Je voulais juste passer un appel. Ça a pas marché. Fin de l'histoire."
    noam sourire "Tu peux toujours réessayer plus tard."
    lysa taquin "Merci pour le conseil technique. Je le noterai dans mon journal de bord."

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
    noam reflexion "Ils ont peut-être une radio. On pourrait demander à quelqu'un de relayer un message."
    lysa triste "J'ai essayé de trouver un canal ouvert. Tout ce qui sert à émettre est bloqué."
    noam neutre "Il y a peut-être une autre solution."
    lysa blase "Je sais. C'est ce que je me répète depuis tout à l'heure."
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
