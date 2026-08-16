# -----------------------------------------------------------------------
# TEMPS LIBRE — Gestion générale
# -----------------------------------------------------------------------

default free_time_active = False

default free_time_next_label = None

default last_room_label = None

default exploration_libre_active = False
default exploration_libre_next_label = None
default exploration_libre_seen_rooms = []
default exploration_libre_required_visits = 0
default exploration_libre_allowed_rooms = None
default exploration_libre_title = "Exploration libre"
default exploration_libre_last_room = None
default link_replay_mode = False
default free_time_selected_character = None
default free_time_selected_scene = None
default persistent.free_time_completed_scenes = []
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

    # Catalogue unique des temps libres. Une condition est soit None, soit un
    # couple (nom_de_variable, valeur_attendue). Ajouter une scène ne demande
    # donc plus de modifier les écrans des salles ou une chaîne de progression.
    FREE_TIME_SCENES = {
        "lysa": [
            {"id": "lysa_1", "label": "lysa_link_1", "title": _("Un café en retard"), "route": _("Lysa"), "preview": "images/background/scene/repos1.png", "condition": None},
            {"id": "lysa_2", "label": "lysa_link_2", "title": _("Les lumières d'Harmonie"), "route": _("Lysa"), "preview": "images/background/scene/observation1.png", "condition": None},
            {"id": "lysa_3", "label": "lysa_link_3", "title": _("Après le tir"), "route": _("Lysa"), "preview": "images/background/scene/canon1.png", "condition": None},
        ],
        "julian": [
            {"id": "julian_1", "label": "julian_link_1", "title": _("Une partie sérieuse"), "route": _("Julian"), "preview": "images/background/scene/repos1.png", "condition": None},
            {"id": "julian_2", "label": "julian_link_2", "title": _("Sous les projecteurs"), "route": _("Julian"), "preview": "images/background/scene/observation1.png", "condition": None},
            {"id": "julian_3", "label": "julian_link_3", "title": _("Le rôle parfait"), "route": _("Julian"), "preview": "images/background/scene/conclave1.png", "condition": None},
        ],
        "elen": [
            {"id": "elen_1", "label": "elen_link_1", "title": _("Service improvisé"), "route": _("Elen"), "preview": "images/background/scene/cafeteria1.png", "condition": None},
            {"id": "elen_2", "label": "elen_link_2", "title": _("Vue sur le monde"), "route": _("Elen"), "preview": "images/background/scene/observation1.png", "condition": None},
            {"id": "elen_3", "label": "elen_link_3", "title": _("Garde de nuit"), "route": _("Elen"), "preview": "images/background/scene/infirmerie1.png", "condition": None},
        ],
        "iris": [
            {"id": "iris_1", "label": "iris_link_1", "title": _("À armes égales"), "route": _("Iris"), "preview": "images/background/scene/repos1.png", "condition": None},
            {"id": "iris_2", "label": "iris_link_2", "title": _("Une question de méthode"), "route": _("Iris"), "preview": "images/background/scene/archive1.png", "condition": None},
            {"id": "iris_3", "label": "iris_link_3", "title": _("Derrière l'ironie"), "route": _("Iris"), "preview": "images/background/scene/observation1.png", "condition": None},
        ],
        "tomas": [
            {"id": "tomas_1", "label": "tomas_link_1", "title": _("Archives croisées"), "route": _("Tomas"), "preview": "images/background/scene/archive1.png", "condition": None},
            {"id": "tomas_2", "label": "tomas_link_2", "title": _("Ce que disent les dossiers"), "route": _("Tomas"), "preview": "images/background/scene/archive2.png", "condition": None},
            {"id": "tomas_3", "label": "tomas_link_3", "title": _("La part manquante"), "route": _("Tomas"), "preview": "images/background/scene/archive1.png", "condition": None},
        ],
        "nyra": [
            {"id": "nyra_1", "label": "nyra_link_1", "title": _("Face au Conclave"), "route": _("Nyra"), "preview": "images/background/scene/conclave1.png", "condition": None},
            {"id": "nyra_2", "label": "nyra_link_2", "title": _("Une stratégie fragile"), "route": _("Nyra"), "preview": "images/background/scene/conclave2.png", "condition": None},
            {"id": "nyra_3", "label": "nyra_link_3", "title": _("Choisir sa bataille"), "route": _("Nyra"), "preview": "images/background/scene/conclave3.png", "condition": None},
        ],
        "kael": [
            {"id": "kael_1", "label": "kael_link_1", "title": _("Diagnostic"), "route": _("Kael"), "preview": "images/background/scene/maintenance1.png", "condition": None},
            {"id": "kael_2", "label": "kael_link_2", "title": _("Pièces détachées"), "route": _("Kael"), "preview": "images/background/scene/maintenance2.png", "condition": None},
            {"id": "kael_3", "label": "kael_link_3", "title": _("Réparer l'irréparable"), "route": _("Kael"), "preview": "images/background/scene/maintenance1.png", "condition": None},
        ],
        "elias": [
            {"id": "elias_1", "label": "elias_link_1", "title": _("Tenir le rythme"), "route": _("Elias"), "preview": "images/background/scene/gymnase1.png", "condition": None},
            {"id": "elias_2", "label": "elias_link_2", "title": _("Sous pression"), "route": _("Elias"), "preview": "images/background/scene/maintenance1.png", "condition": None},
            {"id": "elias_3", "label": "elias_link_3", "title": _("Le poids du silence"), "route": _("Elias"), "preview": "images/background/scene/gymnase2.png", "condition": None},
        ],
        "mara": [
            {"id": "mara_1", "label": "mara_link_1", "title": _("Pause tactique"), "route": _("Mara"), "preview": "images/background/scene/cafeteria1.png", "condition": None},
            {"id": "mara_2", "label": "mara_link_2", "title": _("Sans détour"), "route": _("Mara"), "preview": "images/background/scene/repos1.png", "condition": None},
            {"id": "mara_3", "label": "mara_link_3", "title": _("Ligne de fracture"), "route": _("Mara"), "preview": "images/background/scene/cafeteria2.png", "condition": None},
        ],
        "ryn": [
            {"id": "ryn_1", "label": "ryn_link_1", "title": _("Premier round"), "route": _("Ryn"), "preview": "images/background/scene/gymnase1.png", "condition": None},
            {"id": "ryn_2", "label": "ryn_link_2", "title": _("Trouver son équilibre"), "route": _("Ryn"), "preview": "images/background/scene/gymnase2.png", "condition": None},
            {"id": "ryn_3", "label": "ryn_link_3", "title": _("Ne pas reculer"), "route": _("Ryn"), "preview": "images/background/scene/gymnase1.png", "condition": None},
        ],
        "sael": [
            {"id": "sael_1", "label": "sael_link_1", "title": _("Entre deux portes"), "route": _("Sael"), "preview": "images/background/scene/sas1.png", "condition": None},
            {"id": "sael_2", "label": "sael_link_2", "title": _("Protocole humain"), "route": _("Sael"), "preview": "images/background/scene/sas2.png", "condition": None},
            {"id": "sael_3", "label": "sael_link_3", "title": _("Le sas reste ouvert"), "route": _("Sael"), "preview": "images/background/scene/sas1.png", "condition": None},
        ],
    }

    def all_free_time_scenes():
        return [scene for character_id in CHARACTER_LINK_IDS for scene in FREE_TIME_SCENES.get(character_id, [])]

    def free_time_scene(scene_id):
        for scene in all_free_time_scenes():
            if scene["id"] == scene_id:
                return scene
        return None

    def free_time_condition_met(scene):
        condition = scene.get("condition")
        if condition is None:
            return True
        variable_name, expected_value = condition
        return getattr(store, variable_name, None) == expected_value

    def completed_free_time_scene_ids():
        completed = getattr(persistent, "free_time_completed_scenes", None)
        if not isinstance(completed, list):
            completed = []
            persistent.free_time_completed_scenes = completed
        # Migration transparente des souvenirs débloqués par l'ancien système
        # progressif. La galerie bonus reste ainsi intacte sur les sauvegardes
        # existantes, sans réintroduire la progression dans le tirage en jeu.
        for character_id, memory_ids in persistent.character_link_memories.items():
            for memory_id in memory_ids:
                legacy_id = "{}_{}".format(character_id, memory_id)
                if free_time_scene(legacy_id) is not None and legacy_id not in completed:
                    completed.append(legacy_id)
        return completed

    def free_time_scene_unlocked(scene_id):
        return scene_id in completed_free_time_scene_ids()

    def available_free_time_scenes(character_id):
        completed = set(completed_free_time_scene_ids())
        return [scene for scene in FREE_TIME_SCENES.get(character_id, []) if scene["id"] not in completed and free_time_condition_met(scene)]

    def character_has_available_free_time(character_id):
        return bool(available_free_time_scenes(character_id))

    def choose_free_time_scene(character_id):
        choices = available_free_time_scenes(character_id)
        return renpy.random.choice(choices) if choices else None

    def complete_free_time_scene(scene_id):
        scene = free_time_scene(scene_id)
        if scene is None or getattr(store, "link_replay_mode", False):
            return
        completed = completed_free_time_scene_ids()
        if scene_id not in completed:
            completed.append(scene_id)
        character_id, memory_index = scene_id.rsplit("_", 1)
        memories = set(persistent.character_link_memories.get(character_id, []))
        memories.add(int(memory_index))
        persistent.character_link_memories[character_id] = sorted(memories)
        renpy.save_persistent()

    def free_time_unlocked_count():
        return len(completed_free_time_scene_ids())

    def free_time_character_count(character_id):
        return len([scene for scene in FREE_TIME_SCENES.get(character_id, []) if free_time_scene_unlocked(scene["id"])])

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
        # Compatibilité des anciennes sauvegardes et du Codex : ce compteur
        # n'intervient plus dans la sélection des scènes.
        return free_time_character_count(character_id)

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
        return [int(scene["id"].rsplit("_", 1)[1]) for scene in FREE_TIME_SCENES.get(character_id, []) if free_time_scene_unlocked(scene["id"])]

    def character_link_memory_label(character_id, memory_index):
        return "{}_link_{}".format(character_id, memory_index)


label START_FREE_TIME(next_label=None):

    $ free_time_active = True
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

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION

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

    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_1
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

    call expression _replay_label from _call_expression_1

    $ link_replay_mode = False
    $ free_time_active = _replay_previous_free_time
    $ exploration_libre_active = _replay_previous_exploration
    $ sync_character_links_from_persistent()

    return


label FREE_TIME_CHARACTER_INTERACT(character_id=None):

    if character_id is None:
        $ character_id = free_time_selected_character

    $ _free_time_character_name = CHARACTER_REAL_NAMES.get(character_id, character_id.title())

    menu:
        "Passer du temps avec [_free_time_character_name] ?"
        "Oui":
            $ free_time_selected_scene = choose_free_time_scene(character_id)
        "Non":
            if last_room_label:
                jump expression last_room_label
            jump START_FREE_TIME_MAP

    if free_time_selected_scene is None:
        "Aucun nouveau temps libre n'est disponible avec ce personnage pour le moment."
        if last_room_label:
            jump expression last_room_label
        jump START_FREE_TIME_MAP

    $ _free_time_label = free_time_selected_scene["label"]
    jump expression _free_time_label


label REPLAY_FREE_TIME_SCENE(scene_id):

    $ _replay_scene = free_time_scene(scene_id)
    if _replay_scene is None or not free_time_scene_unlocked(scene_id):
        return

    $ link_replay_mode = True
    $ _replay_previous_free_time = free_time_active
    $ _replay_previous_exploration = exploration_libre_active
    $ free_time_active = False
    $ exploration_libre_active = False
    $ _replay_label = _replay_scene["label"]

    call expression _replay_label from _call_replay_free_time_scene

    $ link_replay_mode = False
    $ free_time_active = _replay_previous_free_time
    $ exploration_libre_active = _replay_previous_exploration
    return
