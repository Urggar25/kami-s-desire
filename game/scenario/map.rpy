# -----------------------------------------------------------------------
# NAVIGATION MANUELLE — Couloirs du Conclave
# -----------------------------------------------------------------------

default corridor_current = "dortoir"
default corridor_ui_target = None
default current_scene_active = None

init python:
    CORRIDOR_FOR_ROOM = {
        "archive": "dortoir",
        "cafeteria": "cafeteria",
        "canon": "cafeteria",
        "conclave": "dortoir",
        "dortoir": "dortoir",
        "gymnase": "infirmerie",
        "infirmerie": "infirmerie",
        "livraison": "sas",
        "maintenance": "maintenance",
        "observation": "cafeteria",
        "repos": "cafeteria",
        "stockage": "sas",
    }

    CORRIDOR_LABELS = {
        "cafeteria": "Couloir de la cafétéria",
        "dortoir": "Couloir du dortoir",
        "infirmerie": "Couloir de l'infirmerie",
        "maintenance": "Couloir de maintenance",
        "sas": "Couloir du SAS",
    }

    MAP_ROOM_LABELS = {
        "archive": "Salle d'archive",
        "cafeteria": "Cafétéria",
        "canon": "Salle du canon",
        "conclave": "Conclave",
        "dortoir": "Dortoir",
        "gymnase": "Gymnase",
        "infirmerie": "Infirmerie",
        "livraison": "SAS de livraison",
        "maintenance": "Maintenance",
        "observation": "Observatoire",
        "repos": "Salle de repos",
        "stockage": "Stockage",
    }

    # (type, destination, texture interactive, libellé)
    CORRIDOR_INTERACTIONS = {
        "cafeteria": [
            ("room", "cafeteria", "porte_cafeteria.png", "Entrer dans la cafétéria"),
            ("room", "canon", "porte_canon.png", "Entrer dans la salle du canon"),
            ("room", "observation", "porte_observation.png", "Entrer dans l'observatoire"),
            ("room", "repos", "porte_repos.png", "Entrer dans la salle de repos"),
            ("corridor", "dortoir", "vers_couloir_dortoir.png", "Aller vers le dortoir"),
            ("corridor", "maintenance", "vers_couloir_maintenance.png", "Aller vers la maintenance"),
        ],
        "dortoir": [
            ("room", "archive", "porte_archive.png", "Entrer dans la salle d'archive"),
            ("room", "conclave", "porte_conclave.png", "Entrer dans le Conclave"),
            ("room", "dortoir", "porte_dortoir.png", "Entrer dans le dortoir"),
            ("corridor", "cafeteria", "vers_couloir_cafeteria.png", "Aller vers la cafétéria"),
            ("corridor", "infirmerie", "vers_couloir_infirmerie.png", "Aller vers l'infirmerie"),
        ],
        "infirmerie": [
            ("room", "gymnase", "porte_gymnase.png", "Entrer dans le gymnase"),
            ("room", "infirmerie", "porte_infirmerie.png", "Entrer dans l'infirmerie"),
            ("corridor", "dortoir", "vers_couloir_dortoir.png", "Aller vers le dortoir"),
            ("corridor", "maintenance", "vers_couloir_maintenance.png", "Aller vers la maintenance"),
            ("corridor", "sas", "vers_couloir_sas.png", "Aller vers le SAS"),
        ],
        "maintenance": [
            ("room", "maintenance", "porte_maintenance.png", "Entrer dans la maintenance"),
            ("corridor", "cafeteria", "vers_couloir_cafeteria.png", "Aller vers la cafétéria"),
            ("corridor", "infirmerie", "vers_couloir_infirmerie.png", "Aller vers l'infirmerie"),
        ],
        "sas": [
            ("room", "livraison", "porte_sas.png", "Entrer dans le SAS de livraison"),
            ("room", "stockage", "porte_stockage.png", "Entrer dans la salle de stockage"),
            ("corridor", "infirmerie", "vers_couloir_infirmerie.png", "Aller vers l'infirmerie"),
        ],
    }

    CORRIDOR_ROOM_LABELS = {
        "archive": "ARCHIVE_TP",
        "cafeteria": "CAFETERIA_TP",
        "canon": "CANON_TP",
        "conclave": "CONCLAVE_TP",
        "dortoir": "DORTOIR_TP",
        "gymnase": "GYMNASE_TP",
        "infirmerie": "INFIRMERIE_TP",
        "livraison": "LIVRAISON_TP",
        "maintenance": "MAINTENANCE_TP",
        "observation": "OBSERVATION_TP",
        "repos": "REPOS_TP",
        "stockage": "STOCKAGE_TP",
    }

    DOOR_ROOM_BACKGROUNDS = {
        "archive": "bg_archive",
        "cafeteria": "bg_cafeteria",
        "canon": "bg_canon",
        "conclave": "bg_conclave",
        "dortoir": "bg_dortoir",
        "gymnase": "bg_gymnase",
        "infirmerie": "bg_infirmerie",
        "livraison": "bg_sas",
        "maintenance": "bg_maintenance",
        "observation": "bg_observation",
        "repos": "bg_repos",
        "stockage": "bg_stockage",
        "chambre": "bg_chambre",
    }

    def corridor_for_room(room_key):
        if room_key and room_key.startswith("pnc_"):
            room_key = room_key[4:]
        if room_key == "chambre":
            room_key = "dortoir"
        return CORRIDOR_FOR_ROOM.get(room_key, "dortoir")

    def room_key_from_pnc_room(pnc_room_name):
        if isinstance(pnc_room_name, str) and pnc_room_name.startswith("pnc_"):
            room_key = pnc_room_name[4:]
            if room_key in CORRIDOR_ROOM_LABELS:
                return room_key
        return None

    def corridor_background(corridor_key):
        return "images/background/scene/couloir_{}.png".format(corridor_key)

    def corridor_interaction_path(corridor_key, filename):
        return "images/background/interact/couloir/{}/{}".format(corridor_key, filename)

    def map_room_selectable(room_key):
        if getattr(store, "exploration_libre_active", False):
            return exploration_libre_room_allowed(room_key)
        return True

    def corridor_target_enabled(corridor_key, target_type, target_key):
        if getattr(store, "current_scene_active", None) == "_6_0_1_ROUTE_CAFETERIA":
            if corridor_key == "dortoir":
                return (target_type, target_key) == ("corridor", "cafeteria")
            if corridor_key == "cafeteria":
                return (target_type, target_key) == ("room", "cafeteria")
            return False

        if getattr(store, "current_scene_active", None) == "_4_0_ROUTE_CAFETERIA":
            if corridor_key == "dortoir":
                return (target_type, target_key) == ("corridor", "cafeteria")
            if corridor_key == "cafeteria":
                return (target_type, target_key) in (
                    ("room", "cafeteria"),
                    ("corridor", "dortoir"),
                )
            return False

        if getattr(store, "current_scene_active", None) == "_2_ROUTE_OBSERVATION":
            return target_type == "corridor" or (
                target_type == "room" and target_key in ("cafeteria", "observation")
            )

        if getattr(store, "current_scene_active", None) in ("_2_ROUTE_CAFETERIA", "_3_ROUTE_CAFETERIA"):
            if corridor_key == "dortoir":
                return (target_type, target_key) in (
                    ("room", "dortoir"),
                    ("corridor", "cafeteria"),
                )
            if corridor_key == "cafeteria":
                return (target_type, target_key) in (
                    ("room", "cafeteria"),
                    ("corridor", "dortoir"),
                )
            return False

        return target_type == "corridor" or map_room_selectable(target_key)

    def corridor_room_label(room_key):
        return CORRIDOR_ROOM_LABELS.get(room_key)

    def door_room_background(room_key):
        image_name = DOOR_ROOM_BACKGROUNDS.get(room_key)
        if image_name:
            return renpy.displayable(image_name)
        return Solid("#000")

    def door_corridor_background(corridor_key):
        return Image(corridor_background(corridor_key))


screen conclave_corridor(corridor_key=None):
    modal True
    zorder 200

    $ shown_corridor = corridor_key if corridor_key in CORRIDOR_INTERACTIONS else "dortoir"
    $ corridor_title = CORRIDOR_LABELS[shown_corridor]

    add Solid("#000")
    add corridor_background(shown_corridor) at cover_screen

    for target_type, target_key, texture_name, target_text in CORRIDOR_INTERACTIONS[shown_corridor]:
        $ target_enabled = corridor_target_enabled(shown_corridor, target_type, target_key)
        $ interaction_path = corridor_interaction_path(shown_corridor, texture_name)

        imagebutton:
            idle interaction_path
            hover Transform(interaction_path, matrixcolor=BrightnessMatrix(0.25))
            # Les calques de couloir couvrent parfois une grande partie du décor.
            # Les teinter lorsqu'ils sont désactivés crée alors des bandes visibles.
            insensitive interaction_path
            focus_mask True
            xpos 0
            ypos 0
            at cover_screen
            sensitive target_enabled
            hovered SetVariable("corridor_ui_target", target_text if target_enabled else "Accès indisponible")
            unhovered SetVariable("corridor_ui_target", None)
            action Return((target_type, target_key))

    if shown_corridor == "dortoir" and current_scene_active == "FIRST_CONCLAVE_ELEN_INTERACT":
        imagebutton:
            idle Transform(character_image("elen", "joie"), zoom=1.00)
            hover Transform(character_image("elen", "content"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            hovered SetVariable("corridor_ui_target", "Parler à Elen")
            unhovered SetVariable("corridor_ui_target", None)
            action Return("FIRST_CONCLAVE_ELEN_INTERACT")

    if shown_corridor == "cafeteria" and current_scene_active == "_2_ROUTE_CAFETERIA" and not day2_cafeteria_route_tomas_seen:
        imagebutton:
            idle Transform(character_image("tomas", "neutre"), zoom=1.00)
            hover Transform(character_image("tomas", "hesitation"), zoom=1.00)
            focus_mask True
            xalign 0.62
            yalign 1.00
            hovered SetVariable("corridor_ui_target", "Parler à Tomas")
            unhovered SetVariable("corridor_ui_target", None)
            action Return("_2_ROUTE_CAFETERIA_TOMAS")

    if shown_corridor == "cafeteria" and current_scene_active == "_3_ROUTE_CAFETERIA" and not day3_cafeteria_route_julian_seen:
        imagebutton:
            idle Transform(character_image("julian", "joie"), zoom=1.00)
            hover Transform(character_image("julian", "sourire"), zoom=1.00)
            focus_mask True
            xalign 0.62
            yalign 1.00
            hovered SetVariable("corridor_ui_target", "Parler à Julian")
            unhovered SetVariable("corridor_ui_target", None)
            action Return("_3_OPT_JULIAN_DIAL")

    if shown_corridor == "dortoir" and current_scene_active == "_2_ROUTE_OBSERVATION":
        if not day2_observation_route_mara_seen:
            imagebutton:
                idle Transform(character_image("mara", "mefiant"), zoom=1.00)
                hover Transform(character_image("mara", "taquin"), zoom=1.00)
                focus_mask True
                xalign 0.18
                yalign 1.00
                hovered SetVariable("corridor_ui_target", "Parler à Mara et Sael")
                unhovered SetVariable("corridor_ui_target", None)
                action Return("_2_APRES_MIDI_MARA_SAEL")

        if not day2_observation_route_lysa_seen:
            imagebutton:
                idle Transform(character_image("lysa", "triste"), zoom=1.00)
                hover Transform(character_image("lysa", "reflexion"), zoom=1.00)
                focus_mask True
                xalign 0.82
                yalign 1.00
                hovered SetVariable("corridor_ui_target", "Parler à Lysa et Elias")
                unhovered SetVariable("corridor_ui_target", None)
                action Return("_2_APRES_MIDI_LYSA_ELIAS")

    if shown_corridor == "infirmerie" and current_scene_active == "_2_ROUTE_OBSERVATION":
        if not day2_observation_route_sael_seen:
            imagebutton:
                idle Transform(character_image("sael", "neutre"), zoom=1.00)
                hover Transform(character_image("sael", "raison"), zoom=1.00)
                focus_mask True
                xalign 0.50
                yalign 1.00
                hovered SetVariable("corridor_ui_target", "Parler à Sael")
                unhovered SetVariable("corridor_ui_target", None)
                action Return("_2_APRES_MIDI_SAEL")

    frame:
        xalign 0.02
        yalign 0.03
        xmaximum 500
        background Solid("#090d14dd")
        padding (18, 12)

        vbox:
            spacing 4
            text kd_tr(corridor_title):
                color "#E8F4FF"
                size 32
                xalign 0.0
                text_align 0.0
                outlines [(2, "#02060ccc", 0, 0)]

            if corridor_ui_target:
                text kd_tr(corridor_ui_target):
                    color "#A6D8FF"
                    size 22
                    xalign 0.0
                    text_align 0.0

    if exploration_libre_active:
        frame:
            xalign 0.03
            yalign 0.97
            background Solid("#0b1118d0")
            padding (16, 12)

            vbox:
                spacing 5
                text kd_tr(exploration_libre_title):
                    size 26
                    color "#A6D8FF"

                if exploration_libre_required_visits > 0:
                    text "Zones visitées : [len(exploration_libre_seen_rooms)]/[exploration_libre_required_visits]":
                        size 20
                        color "#DCE8F7"

    elif current_scene_active in ("_4_0_ROUTE_CAFETERIA", "_6_0_1_ROUTE_CAFETERIA"):
        frame:
            xalign 0.03
            yalign 0.97
            background Solid("#0b1118d0")
            padding (16, 12)

            vbox:
                spacing 5
                text "OBJECTIF":
                    size 18
                    color "#6FA6C6"
                text "Rejoindre la cafétéria":
                    size 26
                    color "#A6D8FF"

    elif current_scene_active == "_2_ROUTE_OBSERVATION":
        frame:
            xalign 0.03
            yalign 0.97
            background Solid("#0b1118d0")
            padding (16, 12)

            vbox:
                spacing 5
                text "OBJECTIF":
                    size 18
                    color "#6FA6C6"
                text "Rejoindre la salle d'observation":
                    size 26
                    color "#A6D8FF"


label _2_ROUTE_CAFETERIA_TOMAS:
    scene expression Image(corridor_background("cafeteria")) at adaptive_fullscreen
    $ day2_cafeteria_route_tomas_seen = True

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("tomas", "hesitation", 0.68),
    ])

    noam "Salut Tomas. Tu vas à la cafétéria ?"
    tomas hesitation "O-Oui. Enfin, j'essaie surtout de ne pas arriver le dernier."
    tomas inquiet "Tu crois que Kami va vraiment annoncer le vote dès ce matin ?"
    noam reflexion "Si elle l'a dit, je pense que oui..."
    tomas raison "O-Ouais on devrait y aller alors."

    $ hideGroup()
    return


label CORRIDOR_NAVIGATION(start_corridor=None):
    if start_corridor is not None:
        $ corridor_current = start_corridor

    $ corridor_ui_target = None
    call screen conclave_corridor(corridor_current)
    $ _corridor_action = _return

    if _corridor_action is None:
        jump CORRIDOR_NAVIGATION

    if isinstance(_corridor_action, str):
        call expression _corridor_action from _call_expression_2
        jump CORRIDOR_NAVIGATION

    if _corridor_action[0] == "corridor":
        $ corridor_current = _corridor_action[1]
        jump CORRIDOR_NAVIGATION

    $ _corridor_room = _corridor_action[1]
    $ corridor_current = corridor_for_room(_corridor_room)
    call PLAY_DOOR_OPEN(door_room_background(_corridor_room)) from _call_PLAY_DOOR_OPEN
    return _corridor_room


label PLAY_DOOR_OPEN(next_background=None):
    window hide

    if next_background is not None:
        scene expression next_background as door_destination_bg at adaptive_fullscreen
    else:
        scene black

    play sound "audio/sfx_door.mp3"

    show expression "images/background/interact/animation/door_open/porte1.png" as door_open_fg at adaptive_fullscreen
    with None
    $ renpy.pause(0.18, hard=True)

    show expression "images/background/interact/animation/door_open/porte2.png" as door_open_fg at adaptive_fullscreen
    $ renpy.pause(0.18, hard=True)

    show expression "images/background/interact/animation/door_open/porte3.png" as door_open_fg at adaptive_fullscreen
    $ renpy.pause(0.42, hard=True)

    hide door_open_fg with Dissolve(0.14)
    return


label EXIT_ROOM_TO_CORRIDOR:
    call PLAY_DOOR_OPEN(door_corridor_background(corridor_current)) from _call_PLAY_DOOR_OPEN_1

    if exploration_libre_active or social_free_time_active():
        return

    jump OPEN_CONCLAVE_MAP


label OPEN_CONCLAVE_MAP:
    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_2
    $ _open_room_label = corridor_room_label(_return)

    if _open_room_label is not None:
        jump expression _open_room_label

    jump OPEN_CONCLAVE_MAP


label MAP_NOTHING_HERE:
    think "Je n'ai rien à faire ici pour le moment."
    pause 0.3
    jump OPEN_CONCLAVE_MAP
