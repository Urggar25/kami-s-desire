default dortoir_lock = True


label DORTOIR_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_334
    scene bg_dortoir at adaptive_fullscreen

    if current_scene_active in ("_2_ROUTE_CAFETERIA", "_3_ROUTE_CAFETERIA"):
        $ pnc_room = "pnc_dortoir"
        call screen pnc_dortoir()
        jump DORTOIR_TP

    if dortoir_lock:
        jump MAP_NOTHING_HERE

    $ pnc_room = "pnc_dortoir"
    call screen pnc_dortoir()

    if free_time_active:
        return
    if exploration_libre_active:
        return


label CHAMBRE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_335
    scene bg_chambre at adaptive_fullscreen

    if current_scene_active in ("_2_ROUTE_CAFETERIA", "_3_ROUTE_CAFETERIA"):
        $ pnc_room = "pnc_chambre"
        call screen pnc_chambre()
        jump CHAMBRE_TP

    if not social_free_time_active():
        jump MAP_NOTHING_HERE

    $ pnc_room = "pnc_chambre"
    call screen pnc_chambre()

    if free_time_active:
        return
    if exploration_libre_active:
        return


label CHAMBRE_CHOIX_LIT_UNUSED:
    menu:
        "M'allonger pour passer le temps libre.":
            think "Je m'allonge sur le lit et laisse le temps filer."
            jump FREE_TIME_END

        "Je ne suis pas encore prêt à me reposer.":
            jump CHAMBRE_TP


screen pnc_dortoir():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/scene/bg_dortoir.png" at cover_screen

    if social_free_time_active():
        $ chambre_door_path = "images/background/interact/dortoir/porte.png"
        imagebutton:
            idle room_interaction_null()
            hover room_interaction_layer(chambre_door_path, "dortoir", "hover")
            focus_mask room_interaction_layer(chambre_door_path, "dortoir", "art")
            xpos 0
            ypos 0
            action Jump("DORTOIR_ENTER_CHAMBRE")

    $ corridor_door_path = "images/background/interact/dortoir/porte_couloir_dortoir.png"
    imagebutton:
        idle room_interaction_null()
        hover room_interaction_layer(corridor_door_path, "dortoir", "hover")
        focus_mask room_interaction_layer(corridor_door_path, "dortoir", "art")
        xpos 0
        ypos 0
        action [
            SetVariable("corridor_current", "dortoir"),
            Jump("EXIT_ROOM_TO_CORRIDOR")
        ]

    if current_scene_active == "_2_ROUTE_CAFETERIA" and not day2_cafeteria_route_nyra_seen:
        imagebutton:
            idle Transform(character_image("nyra", "neutre"), zoom=1.00)
            hover Transform(character_image("nyra", "sourire"), zoom=1.00)
            focus_mask True
            xalign 0.58
            yalign 1.00
            action Jump("_2_ROUTE_CAFETERIA_NYRA")

    if current_scene_active == "_3_ROUTE_CAFETERIA" and not day3_cafeteria_route_kael_seen:
        imagebutton:
            idle Transform(character_image("kael", "fatigue"), zoom=1.00)
            hover Transform(character_image("kael", "calme"), zoom=1.00)
            focus_mask True
            xalign 0.58
            yalign 1.00
            action Jump("_3_OPT_KAEL_DIAL")


label _2_ROUTE_CAFETERIA_NYRA:
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_336
    scene bg_dortoir at adaptive_fullscreen
    $ day2_cafeteria_route_nyra_seen = True

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("nyra", "neutre", 0.68),
    ])

    noam "Tu vas à la cafétéria ?"
    nyra sourire "Oui. J'attendais juste que le couloir se vide un peu."
    nyra raison "Après hier, je crois qu'on a tous besoin de choisir quand affronter les autres."
    noam reflexion "Je comprends. On se retrouve là-bas."

    $ hideGroup()
    jump DORTOIR_TP



screen pnc_chambre():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("chambre")
    use room_scene_interactions("chambre")



label DORTOIR_ENTER_CHAMBRE:
    $ scripted_room_current = "chambre"
    call PLAY_DOOR_OPEN(door_room_background("chambre")) from _call_PLAY_DOOR_OPEN_3
    jump CHAMBRE_TP


label CHAMBRE_BROUILLEUR:
    # Ancien point d'entrée conservé pour les sauvegardes existantes.
    $ noam_room_jammer_on = True
    jump CHAMBRE_TP
