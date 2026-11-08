# -----------------------------------------------------------------------
# GYMNASE — même modèle que CANON
# - 2 persos seulement : Noam + Elias
# - Découverte : Elias s'entraîne / discussion légère
# - PNC : tapis / poids / vélo / ballon / retour
# -----------------------------------------------------------------------

default decouverte_gymnase = False



label GYMNASE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_337
    scene bg_gymnase at adaptive_fullscreen

    if not decouverte_gymnase and day_number() == 1:
        jump decouverte_gymnase

    $ pnc_room = "pnc_gymnase"
    call screen pnc_gymnase()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_gymnase():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("gymnase")
    use room_scene_interactions("gymnase")

    if social_free_time_active() and character_has_available_free_time("ryn"):
        imagebutton:
            idle Transform(character_image("ryn", "determine"), zoom=1.00)
            hover Transform(character_image("ryn", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.20
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "ryn"), Jump("FREE_TIME_CHARACTER_INTERACT")]
    if social_free_time_active() and character_has_available_free_time("elias"):
        imagebutton:
            idle Transform(character_image("elias", "neutre"), zoom=1.00)
            hover Transform(character_image("elias", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.90
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "elias"), Jump("FREE_TIME_CHARACTER_INTERACT")]


label gymnase1_douche:
    "Les douches sont impeccables. Trop impeccables."
    "Je lève les yeux et repère plusieurs caméras orientées vers les cabines."
    "Aucun angle mort. Et aucun brouilleur pour couper la surveillance."
    think "Qui irait se doucher là-dedans, à la vue de tous ?!"
    jump GYMNASE_TP


label gymnase1_porte_couloir_infirmerie:
    $ corridor_current = "infirmerie"
    jump EXIT_ROOM_TO_CORRIDOR


label gymnase1_terrain:
    "Les lignes du terrain sont nettes, comme si personne ne les avait encore franchies."
    "Il y a assez de place pour courir, jouer ou simplement oublier les murs pendant quelques minutes."
    think "Même la détente ressemble à une zone soigneusement délimitée."
    jump GYMNASE_TP


label gymnase2_banc:
    jump GYM_BANC_INTERACT

label GYM_BANC_INTERACT:
    if not social_free_time_active():
        jump GYM_PNC_POIDS

    $ events_left = sport_events_left_count()

    if events_left > 0:
        menu:
            "Faire une session de sport ? ([events_left] évènement(s) sport restant(s))"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP
    else:
        menu:
            "Faire une session de sport ? (Tous les évènements sport ont été découverts)"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP


label GYM_SPORT_MINIGAME:
    "Tu t'installes sur le banc et tu commences l'entraînement."

    call minijeu_halteres from _call_minijeu_halteres_free_time

    if mg_was_success:
        $ sport_event_label = pop_random_sport_event()
        if sport_event_label:
            call expression sport_event_label from _call_expression_sport_event
        else:
            "Tu termines ta séance, satisfait de tes progrès."
    else:
        "La série te casse le rythme, mais tu sauras mieux gérer la prochaine fois."

    if social_free_time_active():
        jump FREE_TIME_END

    jump GYMNASE_TP

label GYM_PNC_TAPIS:
    "Le tapis est encore tiède."
    "Quelqu'un a couru récemment."
    "Les réglages sont simples."
    "Vitesse. Inclinaison. Temps."
    think "Même ici, tout est calibré."
    jump GYMNASE_TP


label GYM_PNC_POIDS:
    "Des poids libres."
    "Des barres."
    "Des repères au sol comme dans une salle publique."
    "Mais tout est trop propre."
    "Trop rangé."
    think "On dirait un décor de pub."
    jump GYMNASE_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label GYM_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_gymnase:

    $ decouverte_gymnase = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "Un gymnase. Si on doit passer un mois ici, je suppose que c'est toujours mieux que de tourner en rond dans les couloirs."

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_338
    scene bg_gymnase at adaptive_fullscreen with fade

    "Il y a de quoi courir, soulever des poids et s'entraîner. Près d'une machine, un garçon en plein bricolage lâche un juron assez sonore pour me faire sursauter."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elias", "neutre", 0.78),
    ])

    elias colere "Mais c'est pas possible ! J'ai juste demandé la vitesse minimum !"
    noam sourire "Tout va bien ?"
    elias surpris "Ouais, ouais. Enfin... je crois. Le tapis m'a fait une accélération de malade, j'ai failli me casser la gueule."
    noam taquin "Bon, au moins, tu sais qu'il peut aller vite."
    elias fatigue "Très drôle. Tu veux essayer pour voir ?"
    noam sourire "Pourquoi pas ? Ça a pas l'air si compliqué."
    elias content "Attends, je vais te montrer. Je bosse sur des machines toute la journée, normalement je sais les régler."
    noam reflexion "Tu travailles dans quoi ?"
    elias neutre "La mécanique, surtout. Je viens de la Forge, à Axiome. Elias, au fait."
    $ unlock_character_name("elias")
    noam sourire "Noam, d'Harmonie. Enchanté."
    elias sourire "Pareil. Allez, monte dessus, je te règle ça."

    "Je pose les pieds sur le tapis. Elias manipule l'écran avec l'assurance de quelqu'un qui connaît parfaitement ce qu'il fait."
    noam hesitation "Dis, c'est normal qu'il y ait marqué « entraînement intensif » ?"
    elias surpris "Quoi ? Non, attends, bouge pas, je vais..."
    "Le tapis démarre beaucoup trop vite. Je m'agrippe à la barre avant de perdre l'équilibre."
    noam peur "ELIAS ! ARRÊTE CE TRUC !"
    elias panique "PUTAIN, MAIS OÙ IL EST, LE BOUTON ?!"
    "Il tape sur deux commandes sans succès, puis se penche sous la console. Je continue de courir sur place en essayant de ne pas me retrouver par terre."
    noam desespoir "IL EST JUSTE DEVANT TOI, LE GROS BOUTON ROUGE !"
    elias panique "AH, MERDE, OUAIS !"
    "Il appuie sur l'arrêt d'urgence. Le tapis ralentit brutalement et je manque de basculer en avant."
    noam inquiet "T'aurais pu me tuer avec ton échauffement !"
    elias fatigue "Je sais, je sais ! Désolé, j'ai confondu les deux programmes. Je voulais juste te montrer comment ça marchait."
    "Je descends en gardant une main sur la barre. Elias me regarde, visiblement plus inquiet que moi maintenant que le danger est passé."
    elias fatigue "Tu t'es fait mal ? Sérieux, dis-moi. J'aurais dû vérifier les réglages avant de te faire monter."
    noam neutre "Non, je crois que ça va. Mais on va peut-être éviter de recommencer."
    elias rire "Ouais. Bon. On va dire que c'était le programme spécial survie."
    noam taquin "Ça tombe bien, on a déjà Kami pour s'occuper de notre survie."
    elias rire "Ah ouais, j'avais presque oublié notre gentille surveillante."

    "Il débranche la machine et colle dessus une petite étiquette de maintenance, récupérée dans un tiroir voisin."
    noam reflexion "Tu sais quand même réparer ce genre de truc, d'habitude ?"
    elias neutre "Ouais, quand je peux ouvrir le capot et voir ce qui déconne. Là, ils ont tout planqué derrière des menus à la con."
    noam sourire "Je te crois. Mais pour la prochaine démonstration, on fera des pompes."
    elias content "Ça, au moins, ça risque pas de tomber en panne."
    noam taquin "À condition que tu me demandes pas d'en faire cent."
    elias rire "Je te promets rien."

    "Il me tend une bouteille d'eau et en prend une pour lui. Je bois quelques gorgées en reprenant mon souffle."
    elias neutre "Tu sais, ça fait du bien de faire autre chose que de penser à ce qui nous attend. Même si j'ai réussi à transformer cinq minutes de sport en catastrophe."
    noam sourire "On pourra dire qu'on a eu notre premier entraînement en conditions extrêmes."
    elias rire "Voilà ! Et la prochaine fois, je touche plus aux tapis. Enfin... pas avant d'avoir lu la notice."
    "Je le quitte alors qu'il cherche déjà cette fameuse notice dans le tiroir. J'espère simplement que personne ne lui demandera une nouvelle démonstration avant qu'il l'ait trouvée."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_3
    $ hideGroup()
    jump GYMNASE_TP
