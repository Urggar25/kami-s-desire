# -----------------------------------------------------------------------
# TEMPS LIBRE — Gestion générale
# -----------------------------------------------------------------------

default free_time_active = False

default free_time_next_label = None

default last_room_label = None


label START_FREE_TIME(next_label=None):

    $ free_time_active = True
    $ free_time_next_label = next_label

    call screen free_time_transition()

    call screen conclave_map(allow_return=True)

    jump FREE_TIME_END


label FREE_TIME_END:

    $ free_time_active = False

    $ next_label = free_time_next_label
    $ free_time_next_label = None

    if next_label is not None:
        jump expression next_label

    return
