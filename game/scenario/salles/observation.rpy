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
    think "La salle d'observation est au bout du couloir. Je ne sais pas encore ce qu'on est censés y observer."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_344
    scene bg_observation at adaptive_fullscreen with fade
    "Une grande baie vitrée occupe presque tout un mur. Des consoles de navigation affichent des trajectoires et des informations sur le trafic alentour."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "neutre", 0.78),
    ])
    "Lysa est déjà là. Elle me voit entrer, mais ne détourne presque pas les yeux du hublot."
    noam sourire "Ça va ? Tu as l'air absorbée."
    lysa blase "Approche et regarde. Après, tu pourras te moquer de ma tête."
    $ hideGroup()
    scene bg_observation at adaptive_fullscreen
    "Je m'avance jusqu'à la vitre. La Terre occupe une grande partie du champ de vision, entourée de ténèbres et de quelques points lumineux."
    "Je reste un moment sans parler. Je savais qu'on avait quitté le sol, mais le voir de mes propres yeux est une autre histoire."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "reflexion", 0.78),
    ])
    noam surpris "On est vraiment aussi loin ?"
    lysa sourire "Eh ouais. On a fait un sacré trajet pendant qu'on dormait."
    noam inquiet "C'est magnifique, mais j'ai un peu l'impression que le sol va se dérober sous mes pieds."
    lysa taquin "Il est déjà très loin sous tes pieds, le sol. Désolée, ça aide pas."
    noam rire "Non, pas vraiment."
    "Un vaisseau traverse lentement le champ de vision. Sur l'écran voisin, une trajectoire s'affiche avec l'identifiant du district Orbite."
    noam reflexion "Il y a du trafic dehors. Tu crois qu'ils peuvent nous voir ?"
    lysa neutre "Probablement. Par contre, nous, on n'a même pas le droit de les appeler."
    noam desaccord "Il doit bien y avoir une radio quelque part."
    lysa reflexion "Il y en a une, juste là. Mais l'émission est verrouillée. J'ai déjà vérifié."
    noam sourire "J'aurais dû me douter que tu avais essayé."
    lysa taquin "Tu me connais. Quand on me dit de rester enfermée, je commence par chercher les fenêtres."
    noam reflexion "Tu voudrais contacter qui ?"
    lysa triste "Ma famille. Comme tout le monde, je suppose. J'aimerais juste savoir ce qu'ils font en ce moment."
    noam neutre "Oui, moi aussi."
    "Elle pose la main sur le rebord de la baie, puis me laisse regarder les écrans."
    lysa reflexion "C'est bizarre, hein ? Depuis qu'on est arrivés, je suis énervée contre à peu près tout. Et là, pendant cinq minutes, j'ai enfin réussi à penser à autre chose."
    noam taquin "À condition de ne pas regarder la planète où on a laissé tous nos problèmes."
    lysa rire "Bravo, t'as réussi à gâcher le moment. Je pensais que c'était mon boulot."
    noam sourire "Pardon. C'est plutôt beau, quand même."
    lysa sourire "Ouais. Ça me fait du bien de l'admettre, même si je sais pas trop quoi en penser."
    "Nous restons un peu devant la vitre. Lysa finit par s'asseoir près d'une console pendant que je consulte la carte des trajectoires."
    noam neutre "Je vais continuer la visite. Tu viens ?"
    lysa blase "Pas tout de suite. J'ai trouvé le seul endroit d'ici où personne ne me demande mon avis."
    noam taquin "Profites-en, ça risque de pas durer."
    lysa sourire "Compte sur moi."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_6
    $ hideGroup()
    jump OBSERVATION_TP
