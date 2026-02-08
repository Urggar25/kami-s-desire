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


# =========================
#  SCREEN — CARTE CONCLAVE
# =========================

screen conclave_map():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/carte/bg_map.png" at cover_screen

    # --- HOTSPOTS (full-screen overlays) ---
    # IMPORTANT : xpos/ypos 0 + at cover_screen, comme ton modèle

    imagebutton:
        idle "images/carte/archive.png"
        hover "images/carte/archive_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("ARCHIVE_TP")

    imagebutton:
        idle "images/carte/cafeteria.png"
        hover "images/carte/cafeteria_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CAFETERIA_TP")

    imagebutton:
        idle "images/carte/canon.png"
        hover "images/carte/canon_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CANON_TP")

    imagebutton:
        idle "images/carte/conclave.png"
        hover "images/carte/conclave_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CONCLAVE_TP")

    imagebutton:
        idle "images/carte/dortoir.png"
        hover "images/carte/dortoir_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("DORTOIR_TP")

    imagebutton:
        idle "images/carte/gymnase.png"
        hover "images/carte/gymnase_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("GYMNASE_TP")

    imagebutton:
        idle "images/carte/infirmerie.png"
        hover "images/carte/infirmerie_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("INFIRMERIE_TP")

    imagebutton:
        idle "images/carte/livraison.png"
        hover "images/carte/livraison_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("LIVRAISON_TP")

    imagebutton:
        idle "images/carte/maintenance.png"
        hover "images/carte/maintenance_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("MAINTENANCE_TP")

    imagebutton:
        idle "images/carte/observation.png"
        hover "images/carte/observation_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OBSERVATION_TP")

    imagebutton:
        idle "images/carte/repos.png"
        hover "images/carte/repos_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_TP")

    imagebutton:
        idle "images/carte/stockage.png"
        hover "images/carte/stockage_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("STOCKAGE_TP")


# =========================
#  LABEL D'ENTRÉE (exemple)
# =========================

label OPEN_CONCLAVE_MAP:
    call screen conclave_map()
    return

label MAP_NOTHING_HERE:
    think "Je n'ai rien à faire ici pour le moment."
    pause 0.3
    jump OPEN_CONCLAVE_MAP
