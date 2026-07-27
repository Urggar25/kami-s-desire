# -----------------------------------------------------------------------
# TEMPS LIBRE — Gestion générale
# -----------------------------------------------------------------------

default free_time_active = False

default free_time_next_label = None

default last_room_label = None
default free_time_round = 0

default exploration_libre_active = False
default exploration_libre_next_label = None
default exploration_libre_seen_rooms = []
default exploration_libre_required_visits = 0
default exploration_libre_allowed_rooms = None
default exploration_libre_title = "Exploration libre"
default exploration_libre_last_room = None
default link_replay_mode = False
default persistent.character_link_progress = {}
default persistent.character_link_memories = {}

init python:
    CHARACTER_LINK_IDS = [
        "mara",
        "lysa",
        "elen",
        "elias",
        "ryn",
        "kael",
        "nyra",
        "julian",
        "iris",
        "tomas",
        "sael",
    ]

    EXPLORATION_LIBRE_DEFAULT_ROOMS = [
        "archive",
        "cafeteria",
        "canon",
        "conclave",
        "dortoir",
        "gymnase",
        "infirmerie",
        "livraison",
        "maintenance",
        "observation",
        "repos",
        "stockage",
    ]

    def exploration_libre_room_allowed(room_key):
        if not getattr(store, "exploration_libre_active", False):
            return True
        allowed = getattr(store, "exploration_libre_allowed_rooms", None)
        if allowed is None:
            return True
        return room_key in allowed

    def exploration_libre_mark_seen(room_key):
        seen = list(getattr(store, "exploration_libre_seen_rooms", []))
        if room_key and room_key not in seen:
            seen.append(room_key)
        store.exploration_libre_seen_rooms = seen
        return len(seen)

    def social_free_time_active():
        return getattr(store, "free_time_active", False) and not getattr(store, "exploration_libre_active", False)

    def character_link_progress(character_id):
        return persistent.character_link_progress.get(character_id, 0)

    def set_character_link_progress(character_id, value):
        persistent.character_link_progress[character_id] = max(persistent.character_link_progress.get(character_id, 0), value)
        memories = set(persistent.character_link_memories.get(character_id, []))
        if value > 0:
            memories.add(value)
        persistent.character_link_memories[character_id] = sorted(memories)
        renpy.save_persistent()

    def sync_character_links_from_persistent():
        for character_id in CHARACTER_LINK_IDS:
            var_name = character_id + "_link"
            persistent_value = persistent.character_link_progress.get(character_id, 0)
            current_value = getattr(store, var_name, 0)
            if persistent_value > current_value:
                setattr(store, var_name, persistent_value)

    def character_link_unlocked_memories(character_id):
        return list(persistent.character_link_memories.get(character_id, []))

    def character_link_memory_label(character_id, memory_index):
        return "{}_link_{}".format(character_id, memory_index)


label START_FREE_TIME(next_label=None):

    $ sync_character_links_from_persistent()
    $ free_time_active = True
    $ free_time_round += 1
    $ free_time_next_label = next_label
    $ conclave_lock = False
    $ dortoir_lock = False
    $ corridor_current = "dortoir"

    scene black
    show expression Text("Temps libre", size=84, color="#FFFFFF", font="fonts/day_font.ttf") as free_time_title at truecenter
    pause 5.0
    hide free_time_title
    jump START_FREE_TIME_MAP

label START_FREE_TIME_MAP:

    call CORRIDOR_NAVIGATION(corridor_current)

    if _return == "archive":
        call ARCHIVE_TP from _call_ARCHIVE_TP
    elif _return == "cafeteria":
        call CAFETERIA_TP from _call_CAFETERIA_TP
    elif _return == "canon":
        call CANON_TP from _call_CANON_TP
    elif _return == "conclave":
        call CONCLAVE_TP from _call_CONCLAVE_TP
    elif _return == "dortoir":
        call DORTOIR_TP from _call_DORTOIR_TP
    elif _return == "gymnase":
        call GYMNASE_TP from _call_GYMNASE_TP
    elif _return == "infirmerie":
        call INFIRMERIE_TP from _call_INFIRMERIE_TP
    elif _return == "livraison":
        call LIVRAISON_TP from _call_LIVRAISON_TP
    elif _return == "maintenance":
        call MAINTENANCE_TP from _call_MAINTENANCE_TP
    elif _return == "observation":
        call OBSERVATION_TP from _call_OBSERVATION_TP
    elif _return == "repos":
        call REPOS_TP from _call_REPOS_TP
    elif _return == "stockage":
        call STOCKAGE_TP from _call_STOCKAGE_TP

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


# -----------------------------------------------------------------------
# EXPLORATION LIBRE — visite de salles sans scènes sociales de temps libre
# -----------------------------------------------------------------------

label START_EXPLORATION_LIBRE(next_label=None, required_visits=0, allowed_rooms=None, title="Exploration libre"):

    $ sync_character_links_from_persistent()
    $ free_time_active = False
    $ exploration_libre_active = True
    $ exploration_libre_next_label = next_label
    $ exploration_libre_seen_rooms = []
    $ exploration_libre_required_visits = required_visits
    $ exploration_libre_allowed_rooms = allowed_rooms
    $ exploration_libre_title = title
    $ exploration_libre_last_room = None
    $ corridor_current = "dortoir"

    scene black
    show expression Text(exploration_libre_title, size=84, color="#FFFFFF", font="fonts/day_font.ttf") as exploration_libre_title_card at truecenter
    pause 2.5
    hide exploration_libre_title_card

    jump START_EXPLORATION_LIBRE_MAP

label START_EXPLORATION_LIBRE_MAP:

    call CORRIDOR_NAVIGATION(corridor_current)
    $ exploration_libre_last_room = _return

    if _return == "archive":
        call ARCHIVE_TP from _call_exploration_libre_ARCHIVE_TP
    elif _return == "cafeteria":
        call CAFETERIA_TP from _call_exploration_libre_CAFETERIA_TP
    elif _return == "canon":
        call CANON_TP from _call_exploration_libre_CANON_TP
    elif _return == "conclave":
        call CONCLAVE_TP from _call_exploration_libre_CONCLAVE_TP
    elif _return == "dortoir":
        call DORTOIR_TP from _call_exploration_libre_DORTOIR_TP
    elif _return == "gymnase":
        call GYMNASE_TP from _call_exploration_libre_GYMNASE_TP
    elif _return == "infirmerie":
        call INFIRMERIE_TP from _call_exploration_libre_INFIRMERIE_TP
    elif _return == "livraison":
        call LIVRAISON_TP from _call_exploration_libre_LIVRAISON_TP
    elif _return == "maintenance":
        call MAINTENANCE_TP from _call_exploration_libre_MAINTENANCE_TP
    elif _return == "observation":
        call OBSERVATION_TP from _call_exploration_libre_OBSERVATION_TP
    elif _return == "repos":
        call REPOS_TP from _call_exploration_libre_REPOS_TP
    elif _return == "stockage":
        call STOCKAGE_TP from _call_exploration_libre_STOCKAGE_TP

    $ _exploration_libre_count = exploration_libre_mark_seen(exploration_libre_last_room)

    if exploration_libre_required_visits > 0 and _exploration_libre_count >= exploration_libre_required_visits:
        jump EXPLORATION_LIBRE_END

    if exploration_libre_active:
        jump START_EXPLORATION_LIBRE_MAP

    jump EXPLORATION_LIBRE_END

label EXPLORATION_LIBRE_END:

    $ exploration_libre_active = False
    $ next_label = exploration_libre_next_label
    $ exploration_libre_next_label = None
    $ exploration_libre_allowed_rooms = None
    $ exploration_libre_last_room = None

    if next_label is not None:
        jump expression next_label

    return


label REPLAY_CHARACTER_LINK(character_id, memory_index):

    $ _replay_label = character_link_memory_label(character_id, memory_index)
    $ link_replay_mode = True
    $ _replay_previous_free_time = free_time_active
    $ _replay_previous_exploration = exploration_libre_active
    $ free_time_active = False
    $ exploration_libre_active = False

    call expression _replay_label

    $ link_replay_mode = False
    $ free_time_active = _replay_previous_free_time
    $ exploration_libre_active = _replay_previous_exploration
    $ sync_character_links_from_persistent()

    return
