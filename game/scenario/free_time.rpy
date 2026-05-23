# -----------------------------------------------------------------------
# TEMPS LIBRE — Gestion générale
# -----------------------------------------------------------------------

default free_time_active = False

default free_time_next_label = None

default last_room_label = None
default free_time_round = 0


label START_FREE_TIME(next_label=None):

    $ free_time_active = True
    $ free_time_round += 1
    $ free_time_next_label = next_label
    $ conclave_lock = False
    $ dortoir_lock = False

    scene black
    show expression Text("Temps libre", size=84, color="#FFFFFF", font="fonts/day_font.ttf") as free_time_title at truecenter
    pause 5.0
    hide free_time_title
    jump START_FREE_TIME_MAP

label START_FREE_TIME_MAP:

    call screen conclave_map(allow_return=True)

    if _return == "archive":
        call ARCHIVE_TP
    elif _return == "cafeteria":
        call CAFETERIA_TP
    elif _return == "canon":
        call CANON_TP
    elif _return == "conclave":
        call CONCLAVE_TP
    elif _return == "dortoir":
        call DORTOIR_TP
    elif _return == "gymnase":
        call GYMNASE_TP
    elif _return == "infirmerie":
        call INFIRMERIE_TP
    elif _return == "livraison":
        call LIVRAISON_TP
    elif _return == "maintenance":
        call MAINTENANCE_TP
    elif _return == "observation":
        call OBSERVATION_TP
    elif _return == "repos":
        call REPOS_TP
    elif _return == "stockage":
        call STOCKAGE_TP

    if free_time_active:
        jump START_FREE_TIME_MAP

    jump FREE_TIME_END


label FREE_TIME_END:

    $ free_time_active = False

    $ next_label = free_time_next_label
    $ free_time_next_label = None

    if next_label is not None:
        jump expression next_label

    return
