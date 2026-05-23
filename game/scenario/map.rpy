# =========================
#  IMAGES — CARTE CONCLAVE
# =========================

image bg_map                    = "images/carte/bg_map.png"

image map_archive               = "images/carte/archive.png"
image map_archive_hover         = "images/carte/archive_hover.png"

image map_cafeteria             = "images/carte/cafeteria.png"
image map_cafeteria_hover       = "images/carte/cafeteria_hover.png"

image map_canon                 = "images/carte/canon.png"
image map_canon_hover           = "images/carte/canon_hover.png"

image map_conclave              = "images/carte/conclave.png"
image map_conclave_hover        = "images/carte/conclave_hover.png"

image map_dortoir               = "images/carte/dortoir.png"
image map_dortoir_hover         = "images/carte/dortoir_hover.png"

image map_gymnase               = "images/carte/gymnase.png"
image map_gymnase_hover         = "images/carte/gymnase_hover.png"

image map_infirmerie            = "images/carte/infirmerie.png"
image map_infirmerie_hover      = "images/carte/infirmerie_hover.png"

image map_livraison             = "images/carte/livraison.png"
image map_livraison_hover       = "images/carte/livraison_hover.png"

image map_maintenance            = "images/carte/maintenance.png"
image map_maintenance_hover      = "images/carte/maintenance_hover.png"

image map_observation           = "images/carte/observation.png"
image map_observation_hover     = "images/carte/observation_hover.png"

image map_repos                 = "images/carte/repos.png"
image map_repos_hover           = "images/carte/repos_hover.png"

image map_stockage              = "images/carte/stockage.png"
image map_stockage_hover        = "images/carte/stockage_hover.png"


default map_ui_room_key = None


init python:
    MAP_ROOM_LABELS = {
        "archive": "Salle d'Archive",
        "cafeteria": "Cafétéria",
        "canon": "Salle du Canon",
        "conclave": "Conclave",
        "dortoir": "Dortoir",
        "gymnase": "Gymnase",
        "infirmerie": "Infirmerie",
        "livraison": "SAS Livraison",
        "maintenance": "Maintenance",
        "observation": "Observatoire",
        "repos": "Salle de Repos",
        "stockage": "Stockage",
    }

    MAP_CHARACTER_PORTRAIT_IMAGES = {
        "Mara": "images/character/mara/portrait.png",
        "Lysa": "images/character/lysa/portrait.png",
        "Elen": "images/character/elen/portrait.png",
        "Nyra": "images/character/nyra/portrait.png",
        "Tomas": "images/character/tomas/portrait.png",
        "Ryn": "images/character/ryn/portrait.png",
        "Elias": "images/character/elias/portrait.png",
        "Kael": "images/character/kael/portrait.png",
        "Julian": "images/character/julian/portrait.png",
        "Iris": "images/character/iris/portrait.png",
        "Sael": "images/character/sael/portrait.png",
    }

    def map_room_characters(room_key):
        """Retourne la liste des personnages visibles en temps libre pour une salle."""
        if not getattr(store, "free_time_active", False):
            return []

        chars = []
        if room_key == "archive":
            if getattr(store, "tomas_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Tomas")
            if getattr(store, "lysa_link", -1) == 3:
                chars.append("Lysa")
        elif room_key == "cafeteria":
            if getattr(store, "mara_link", -1) in [0, 2, 4]:
                chars.append("Mara")
            if getattr(store, "lysa_link", -1) == 1:
                chars.append("Lysa")
            if getattr(store, "elen_link", -1) == 1:
                chars.append("Elen")
        elif room_key == "conclave":
            if getattr(store, "nyra_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Nyra")
            if getattr(store, "elen_link", -1) == 0:
                chars.append("Elen")
        elif room_key == "dortoir":
            if getattr(store, "lysa_link", -1) == 4:
                chars.append("Lysa")
        elif room_key == "gymnase":
            if getattr(store, "ryn_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Ryn")
            if getattr(store, "elias_link", -1) in [0, 2, 4]:
                chars.append("Elias")
        elif room_key == "infirmerie":
            if getattr(store, "elen_link", -1) == 3:
                chars.append("Elen")
        elif room_key == "livraison":
            if getattr(store, "sael_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Sael")
        elif room_key == "maintenance":
            if getattr(store, "kael_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Kael")
            if getattr(store, "elias_link", -1) in [1, 3]:
                chars.append("Elias")
        elif room_key == "observation":
            if getattr(store, "lysa_link", -1) == 2:
                chars.append("Lysa")
            if getattr(store, "julian_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Julian")
            if getattr(store, "elen_link", -1) == 2:
                chars.append("Elen")
        elif room_key == "repos":
            if getattr(store, "mara_link", -1) in [1, 3]:
                chars.append("Mara")
            if getattr(store, "lysa_link", -1) == 0:
                chars.append("Lysa")
            if getattr(store, "iris_link", -1) in [0, 1, 2, 3, 4]:
                chars.append("Iris")
            if getattr(store, "elen_link", -1) == 4:
                chars.append("Elen")

        return chars

    def map_room_header(room_key):
        if not room_key:
            return "Conclave — Carte interactive"
        return MAP_ROOM_LABELS.get(room_key, "Salle inconnue")


transform map_room_title_pop:
    alpha 0.0
    yoffset -8
    ease 0.18 alpha 1.0 yoffset 0


# =========================
#  SCREEN — CARTE CONCLAVE
# =========================



screen exploration_retour_button():

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action If(free_time_active, Jump("START_FREE_TIME_MAP"), Jump("OPEN_CONCLAVE_MAP"))

screen conclave_map(allow_return=False):

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/carte/bg_map.png" at cover_screen

    use exploration_meta_buttons

    frame:
        xalign 0.03
        yalign 0.97
        xmaximum 560
        ymaximum 220
        background Solid("#0b1118d0")
        padding (16, 14)

        vbox:
            spacing 10

            text "Présences":
                size 28
                color "#A6D8FF"

            if map_ui_room_key is None:
                text "Survole une zone":
                    size 22
                    color "#DCE8F7"
            else:
                $ current_chars = map_room_characters(map_ui_room_key)

                if current_chars:
                    hbox:
                        spacing 10
                        for char_name in current_chars:
                            $ portrait_path = MAP_CHARACTER_PORTRAIT_IMAGES.get(char_name, None)
                            frame:
                                background Solid("#101722f0")
                                xsize 78
                                ysize 78
                                padding (2, 2)

                                if portrait_path is not None:
                                    add Transform(portrait_path, xsize=74, ysize=74)
                else:
                    text "Aucun personnage":
                        size 22
                        color "#C8D3E0"

    # --- HOTSPOTS (full-screen overlays) ---
    # IMPORTANT : xpos/ypos 0 + at cover_screen, comme ton modèle

    imagebutton:
        idle "images/carte/archive.png"
        hover "images/carte/archive_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "archive")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("archive"), Jump("ARCHIVE_TP"))

    imagebutton:
        idle "images/carte/cafeteria.png"
        hover "images/carte/cafeteria_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "cafeteria")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("cafeteria"), Jump("CAFETERIA_TP"))

    imagebutton:
        idle "images/carte/canon.png"
        hover "images/carte/canon_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "canon")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("canon"), Jump("CANON_TP"))

    imagebutton:
        idle "images/carte/conclave.png"
        hover "images/carte/conclave_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "conclave")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("conclave"), Jump("CONCLAVE_TP"))

    imagebutton:
        idle "images/carte/dortoir.png"
        hover "images/carte/dortoir_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "dortoir")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("dortoir"), Jump("DORTOIR_TP"))

    imagebutton:
        idle "images/carte/gymnase.png"
        hover "images/carte/gymnase_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "gymnase")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("gymnase"), Jump("GYMNASE_TP"))

    imagebutton:
        idle "images/carte/infirmerie.png"
        hover "images/carte/infirmerie_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "infirmerie")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("infirmerie"), Jump("INFIRMERIE_TP"))

    imagebutton:
        idle "images/carte/livraison.png"
        hover "images/carte/livraison_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "livraison")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("livraison"), Jump("LIVRAISON_TP"))

    imagebutton:
        idle "images/carte/maintenance.png"
        hover "images/carte/maintenance_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "maintenance")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("maintenance"), Jump("MAINTENANCE_TP"))

    imagebutton:
        idle "images/carte/observation.png"
        hover "images/carte/observation_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "observation")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("observation"), Jump("OBSERVATION_TP"))

    imagebutton:
        idle "images/carte/repos.png"
        hover "images/carte/repos_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "repos")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("repos"), Jump("REPOS_TP"))

    imagebutton:
        idle "images/carte/stockage.png"
        hover "images/carte/stockage_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        hovered SetVariable("map_ui_room_key", "stockage")
        unhovered SetVariable("map_ui_room_key", None)
        action If(free_time_active, Return("stockage"), Jump("STOCKAGE_TP"))

    frame at map_room_title_pop:
        xalign 0.985
        yalign 0.03
        xmaximum 430
        background Solid("#090d14dd")
        padding (16, 12)

        text "[map_room_header(map_ui_room_key)]":
            color "#E8F4FF"
            size 36
            xalign 1.0
            text_align 1.0
            xmaximum 390
            min_width 390
            outlines [(2, "#02060ccc", 0, 0)]


# =========================
#  LABEL D'ENTRÉE (exemple)
# =========================

label OPEN_CONCLAVE_MAP:
    $ map_ui_room_key = None
    call screen conclave_map()
    return

label MAP_NOTHING_HERE:
    think "Je n'ai rien à faire ici pour le moment."
    pause 0.3
    jump OPEN_CONCLAVE_MAP
