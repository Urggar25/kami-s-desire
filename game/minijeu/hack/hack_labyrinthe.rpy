# ============================================================
# HACK LABYRINTHE — moteur reutilisable + circuit du jour 9
#
# Controles : ZQSD / fleches ou clic sur une case de la ligne.
# ESPACE : propulsion phasee (jusqu'a 3 cases).
#
# Rendu : plateau en vue camera (le cadrage suit le jeton du
# joueur), habillage CRT genere par tools/build_hack_assets.py.
#
# Les cases speciales s'appliquent AUX DEUX camps :
#   oneway   : sens unique pour le joueur ET la sentinelle
#   trap     : immobilise le premier qui marche dessus (usage unique)
#   boost    : projette de 2 cases supplementaires, joueur ou sentinelle
#   password : pare-feu, infranchissable par la sentinelle tant qu'il
#              n'est pas force par le joueur (qui l'ouvre pour les deux)
#   sign     : balise ; consultee par le joueur, elle informe.
#              Piratee par la sentinelle, elle expose le joueur.
# ============================================================

default hack_grid = []
default hack_specials = {}
default hack_player = (1, 1)
default hack_player_previous = (1, 1)
default hack_player_start = (1, 1)
default hack_goal = (1, 1)
default hack_enemy = (1, 1)
default hack_enemy_start = (1, 1)
default hack_enemy_previous = None
default hack_enemy_stun = 0.0
default hack_enemy_scan = 0.0
default hack_time_left = 55.0
default hack_total_time = 55.0
default hack_enemy_interval = 1.0
default hack_enemy_clock = 1.0
default hack_enemy_mode = "PATROUILLE"
default hack_enemy2_active = False
default hack_enemy2 = (1, 1)
default hack_enemy2_start = (1, 1)
default hack_enemy2_previous = None
default hack_enemy2_stun = 0.0
default hack_enemy2_scan = 0.0
default hack_enemy2_interval = 1.0
default hack_enemy2_clock = 1.0
default hack_enemy2_mode = "PATROUILLE"
default hack_player_stun = 0.0
default hack_done = False
default hack_success = False
default hack_end_delay = 0.0
default hack_hits = 0
default hack_max_hits = 3
default hack_status = "CONNEXION AU RESEAU DU CANON"
default hack_status_color = "#4AE3FF"
default hack_logbook = []
default hack_flash = 0.0
default hack_flash_color = "#FF173C"
default hack_last_direction = (1, 0)
default hack_dash_cooldown = 0.0
default hack_dash_cooldown_max = 4.0
default hack_trail = []
default hack_paused = False
default hack_solved_passwords = []
default hack_password_active = False
default hack_password_cell = None
default hack_password_sequence = []
default hack_password_progress = 0
default hack_password_time = 0.0
default hack_password_total = 6.0
default hack_sign_message = ""
default hack_sign_time = 0.0
default hack_assist = False
default hack_tick_marker = -1
default j901_hack_success = False
default j710_hack_success = False
default hack_title = "INTRUSION // RESEAU DU CANON"
default hack_channel = "CANAL CHIFFRE J-09  //  TRACE ACTIVE"


# ------------------------------------------------------------
# Assets generes par tools/build_hack_assets.py
# ------------------------------------------------------------
image hk_floor = "minijeu/hack/assets/hk_floor.png"
image hk_wall_0 = "minijeu/hack/assets/hk_wall_0.png"
image hk_wall_1 = "minijeu/hack/assets/hk_wall_1.png"
image hk_wall_2 = "minijeu/hack/assets/hk_wall_2.png"
image hk_goal = "minijeu/hack/assets/hk_goal.png"
image hk_oneway = "minijeu/hack/assets/hk_oneway.png"
image hk_firewall = "minijeu/hack/assets/hk_firewall.png"
image hk_firewall_open = "minijeu/hack/assets/hk_firewall_open.png"
image hk_beacon = "minijeu/hack/assets/hk_beacon.png"
image hk_boost = "minijeu/hack/assets/hk_boost.png"
image hk_trap = "minijeu/hack/assets/hk_trap.png"
image hk_player = "minijeu/hack/assets/hk_player.png"
image hk_enemy = "minijeu/hack/assets/hk_enemy.png"
image hk_glow_cyan = "minijeu/hack/assets/hk_glow_cyan.png"
image hk_glow_red = "minijeu/hack/assets/hk_glow_red.png"
image hk_glow_mint = "minijeu/hack/assets/hk_glow_mint.png"
image hk_glow_violet = "minijeu/hack/assets/hk_glow_violet.png"
image hk_glow_amber = "minijeu/hack/assets/hk_glow_amber.png"
image hk_bezel = "minijeu/hack/assets/hk_bezel.png"
image hk_vignette = "minijeu/hack/assets/hk_vignette.png"
image hk_scanlines = "minijeu/hack/assets/hk_scanlines.png"
image hk_grain = "minijeu/hack/assets/hk_grain.png"
image hk_hexfield = "minijeu/hack/assets/hk_hexfield.png"
image hk_edge = "minijeu/hack/assets/hk_edge.png"
image hk_bar = "minijeu/hack/assets/hk_bar.png"


transform hk_pulse_soft:
    alpha 0.55
    linear 0.85 alpha 1.0
    linear 0.85 alpha 0.55
    repeat

transform hk_pulse_fast:
    alpha 0.35
    linear 0.28 alpha 1.0
    linear 0.34 alpha 0.35
    repeat

transform hk_spin_slow:
    rotate 0
    linear 14.0 rotate 360
    repeat

transform hk_route_pulse(delay=0.0):
    alpha 0.10
    pause delay
    linear 0.40 alpha 0.90
    linear 0.55 alpha 0.10
    repeat

transform hk_driver_at:
    function hack_driver

transform hk_player_at:
    function hack_token_player

transform hk_enemy_at:
    function hack_token_enemy

transform hk_player_halo_at:
    function hack_halo_player

transform hk_enemy_halo_at:
    function hack_halo_enemy

transform hk_enemy2_at:
    function hack_token_enemy2

transform hk_enemy2_halo_at:
    function hack_halo_enemy2


transform hk_scan_sweep:
    ypos -30
    linear 3.4 ypos 1120
    repeat

transform hk_grain_drift:
    xoffset 0 yoffset 0
    pause 0.06
    xoffset -37 yoffset 23
    pause 0.06
    xoffset 61 yoffset -44
    pause 0.06
    xoffset -19 yoffset 55
    pause 0.06
    repeat


init python:
    import math
    import random
    import time
    from collections import deque

    HACK_TICK = 0.05
    HACK_CELL = 104
    HACK_VIEW_X = 150
    HACK_VIEW_Y = 158
    HACK_VIEW_W = 1620
    HACK_VIEW_H = 756
    HACK_DETECT = 6
    HACK_DETECT_SCAN = 12

    HK_CYAN = "#4AE3FF"
    HK_ICE = "#E4FAFF"
    HK_MINT = "#5CFFC0"
    HK_AMBER = "#FFA53D"
    HK_RED = "#FF3D5C"
    HK_VIOLET = "#B672FF"
    HK_MUTED = "#5C8296"
    HK_DIM = "#3A5C6E"

    HACK_DIRECTIONS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    HACK_SND = "minijeu/hack/audio/"

    # Etat purement visuel : hors rollback, mis a jour a chaque frame.
    class HackView(python_object):
        def __init__(self):
            self.px = 1.0
            self.py = 1.0
            self.ex = 1.0
            self.ey = 1.0
            self.ex2 = 1.0
            self.ey2 = 1.0
            self.cam_x = 0.0
            self.cam_y = 0.0
            self.clock = 0.0
            self.hover = None
            self.world = None
            self.minimap = None
            self.world_w = HACK_VIEW_W
            self.world_h = HACK_VIEW_H
            self.mini_w = 0
            self.mini_h = 0

    hack_view = HackView()
    hack_xadj = ui.adjustment()
    hack_yadj = ui.adjustment()

    # Le circuit du jour 9 favorise les boucles et les changements de route :
    # le joueur peut semer la sentinelle au lieu de subir un couloir unique.
    J901_HACK_CIRCUIT = {
        "title": "INTRUSION // RESEAU DU CANON",
        "time": 60.0,
        "enemy_interval": 0.92,
        "grid": [
            "###################",
            "#S..........#.....#",
            "#.##..#.###.#.###.#",
            "#.....#.....#.....#",
            "###.#####.#.###.#.#",
            "#...#.....#...#...#",
            "#.#.#.###.###.#.#.#",
            "#.#...#.....#...#.#",
            "#.#####.###.#.###.#",
            "#.......#......#.G#",
            "###################",
        ],
        "enemy": (13, 5),
        # Placement valide par tools/build_hack_assets.py + verification de
        # connectivite : l'ouverture (6, 1) empeche le spawn d'apparaitre
        # enferme dans la boucle ouest. Le joueur atteint les 97 couloirs et
        # garde toujours une route vers le noyau.
        "specials": {
            (4, 1): {"type": "sign", "message": "PROPULSION DISPONIBLE // TOUCHE ESPACE"},
            (9, 1): {"type": "trap"},
            (3, 3): {"type": "boost"},
            (7, 3): {"type": "password"},
            (9, 4): {"type": "oneway", "direction": (0, 1)},
            (11, 4): {"type": "oneway", "direction": (0, -1)},
            (5, 5): {"type": "trap"},
            (12, 5): {"type": "boost"},
            (11, 7): {"type": "sign", "message": "LES PIEGES IMMOBILISENT AUSSI LA SENTINELLE"},
            (13, 7): {"type": "password"},
            (5, 9): {"type": "boost"},
            (13, 9): {"type": "trap"},
        },
    }

    # Bonus du jour 7 (route commerce adopte) : topologie tres ouverte,
    # boucles multiples, pare-feu, pieges et deux sentinelles simultanees.
    J710_HACK_CIRCUIT = {
        "title": "INTRUSION // SERVEUR DE SURVEILLANCE",
        "channel": "NOEUD LOGISTIQUE J-07  //  DOUBLE TRACE",
        "time": 65.0,
        "enemy_interval": 0.78,
        "enemy2_interval": 0.92,
        "grid": [
            "###################",
            "#S................#",
            "#.###.###.###.###.#",
            "#.................#",
            "#.###.#.#####.#.#.#",
            "#.....#.......#...#",
            "#.#.#.#####.#.###.#",
            "#.................#",
            "#.###.###.###.###.#",
            "#................G#",
            "###################",
        ],
        "enemies": [(17, 1), (1, 9)],
        "specials": {
            (4, 1): {"type": "sign", "message": "DEUX SENTINELLES // CHANGEZ DE BOUCLE"},
            (9, 1): {"type": "trap"},
            (3, 3): {"type": "boost"},
            (7, 3): {"type": "password"},
            (9, 3): {"type": "oneway", "direction": (1, 0)},
            (13, 3): {"type": "trap"},
            (3, 5): {"type": "trap"},
            (9, 5): {"type": "sign", "message": "LES PIEGES SONT A USAGE UNIQUE"},
            (11, 5): {"type": "password"},
            (15, 5): {"type": "boost"},
            (3, 7): {"type": "boost"},
            (7, 7): {"type": "password"},
            (9, 7): {"type": "trap"},
            (13, 7): {"type": "oneway", "direction": (0, 1)},
            (13, 9): {"type": "boost"},
            (15, 9): {"type": "trap"},
        },
    }

    # Catalogue de reference pour composer les prochains circuits.
    # (4, 3): {"type": "oneway", "direction": (1, 0)}
    # (7, 5): {"type": "password"}
    # (8, 5): {"type": "sign", "message": "Le signal rouge ment."}
    # (9, 5): {"type": "boost"}
    # (10, 5): {"type": "trap"}
    HACK_SUPPORTED_TILES = (
        "neutral", "goal", "oneway", "password", "sign", "boost", "trap"
    )

    HACK_TILE_IMAGE = {
        "goal": "hk_goal",
        "oneway": "hk_oneway",
        "password": "hk_firewall",
        "sign": "hk_beacon",
        "boost": "hk_boost",
        "trap": "hk_trap",
    }

    def hack_play(name, volume=0.6):
        path = HACK_SND + name
        if renpy.loadable(path):
            renpy.play(path, channel="sound", relative_volume=volume)

    def hack_ambient_start():
        path = HACK_SND + "hk_ambient.wav"
        if renpy.loadable(path):
            try:
                renpy.music.play(path, channel="hackamb", loop=True, fadein=1.2)
            except Exception:
                pass

    def hack_ambient_stop():
        try:
            renpy.music.stop(channel="hackamb", fadeout=0.8)
        except Exception:
            pass

    def hack_find_marker(grid, marker):
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value == marker:
                    return (x, y)
        return (1, 1)

    # --------------------------------------------------------
    # Journal / statut
    # --------------------------------------------------------
    def hack_log(message, color=HK_CYAN):
        entries = list(store.hack_logbook)
        entries.append(("{:05.1f}".format(store.hack_time_left), message, color))
        store.hack_logbook = entries[-3:]

    def hack_status_set(message, color=HK_CYAN, log=False):
        store.hack_status = message
        store.hack_status_color = color
        if log:
            hack_log(message, color)

    # --------------------------------------------------------
    # Construction du plateau
    # --------------------------------------------------------
    def hack_build_world():
        cell = HACK_CELL
        rows = len(store.hack_grid)
        cols = len(store.hack_grid[0]) if rows else 0
        hack_view.world_w = cols * cell
        hack_view.world_h = rows * cell

        pieces = []
        for y, row in enumerate(store.hack_grid):
            for x, marker in enumerate(row):
                px, py = x * cell, y * cell
                if marker == "#":
                    art = "hk_wall_{}".format((x * 7 + y * 5) % 3)
                else:
                    art = "hk_floor"
                pieces.append((px, py))
                pieces.append(Transform(art, xysize=(cell, cell)))
        hack_view.world = Composite((hack_view.world_w, hack_view.world_h), *pieces)

        hack_xadj.range = max(0, hack_view.world_w - HACK_VIEW_W)
        hack_yadj.range = max(0, hack_view.world_h - HACK_VIEW_H)

    def hack_build_minimap(cell=13):
        rows = len(store.hack_grid)
        cols = len(store.hack_grid[0]) if rows else 0
        hack_view.mini_w = cols * cell
        hack_view.mini_h = rows * cell

        pieces = []
        for y, row in enumerate(store.hack_grid):
            for x, marker in enumerate(row):
                color = "#08131C" if marker == "#" else "#14384E"
                pieces.append((x * cell, y * cell))
                pieces.append(Solid(color, xsize=cell - 1, ysize=cell - 1))
        for pos, data in store.hack_specials.items():
            tone = {
                "trap": "#7A1F31",
                "password": "#5B3391",
                "boost": "#1F6E8C",
                "oneway": "#1F6E8C",
                "sign": "#8A5A1E",
            }.get(data.get("type"), None)
            if tone:
                pieces.append((pos[0] * cell + 3, pos[1] * cell + 3))
                pieces.append(Solid(tone, xsize=cell - 7, ysize=cell - 7))
        hack_view.minimap = Composite((hack_view.mini_w, hack_view.mini_h), *pieces)

    def hack_reset(circuit=None, assist=False):
        circuit = circuit or J901_HACK_CIRCUIT
        store.hack_grid = list(circuit["grid"])
        store.hack_specials = dict((k, dict(v)) for k, v in circuit.get("specials", {}).items())
        store.hack_player_start = hack_find_marker(store.hack_grid, "S")
        store.hack_goal = hack_find_marker(store.hack_grid, "G")
        store.hack_player = store.hack_player_start
        store.hack_player_previous = store.hack_player_start
        enemy_starts = list(circuit.get("enemies", [circuit.get("enemy", store.hack_goal)]))
        store.hack_enemy_start = tuple(enemy_starts[0])
        store.hack_enemy = store.hack_enemy_start
        store.hack_enemy_previous = None
        store.hack_enemy_stun = 0.0
        store.hack_enemy_scan = 0.0
        store.hack_total_time = float(circuit.get("time", 55.0)) + (20.0 if assist else 0.0)
        store.hack_time_left = store.hack_total_time
        store.hack_enemy_interval = float(circuit.get("enemy_interval", 1.0)) * (1.45 if assist else 1.0)
        store.hack_enemy_clock = store.hack_enemy_interval
        store.hack_enemy_mode = "PATROUILLE"
        store.hack_enemy2_active = len(enemy_starts) > 1
        store.hack_enemy2_start = tuple(enemy_starts[1]) if store.hack_enemy2_active else store.hack_enemy_start
        store.hack_enemy2 = store.hack_enemy2_start
        store.hack_enemy2_previous = None
        store.hack_enemy2_stun = 0.0
        store.hack_enemy2_scan = 0.0
        store.hack_enemy2_interval = float(circuit.get("enemy2_interval", circuit.get("enemy_interval", 1.0))) * (1.45 if assist else 1.0)
        store.hack_enemy2_clock = store.hack_enemy2_interval
        store.hack_enemy2_mode = "PATROUILLE"
        store.hack_player_stun = 0.0
        store.hack_done = False
        store.hack_success = False
        store.hack_end_delay = 0.0
        store.hack_hits = 0
        store.hack_max_hits = 3
        store.hack_status = "TROUVEZ LE NOYAU DE CONNEXION"
        store.hack_status_color = HK_CYAN
        store.hack_logbook = []
        store.hack_flash = 0.0
        store.hack_flash_color = "#FF173C"
        store.hack_last_direction = (1, 0)
        store.hack_dash_cooldown = 0.0
        store.hack_dash_cooldown_max = 4.0
        store.hack_trail = [store.hack_player_start]
        store.hack_paused = False
        store.hack_solved_passwords = []
        store.hack_password_active = False
        store.hack_password_cell = None
        store.hack_password_sequence = []
        store.hack_password_progress = 0
        store.hack_password_time = 0.0
        store.hack_password_total = 6.0
        store.hack_sign_message = ""
        store.hack_sign_time = 0.0
        store.hack_assist = assist
        store.hack_tick_marker = -1
        store.hack_title = circuit.get("title", "INTRUSION // RESEAU DU CANON")
        store.hack_channel = circuit.get("channel", "CANAL CHIFFRE J-09  //  TRACE ACTIVE")

        hack_build_world()
        hack_build_minimap()

        hack_view.px = float(store.hack_player[0])
        hack_view.py = float(store.hack_player[1])
        hack_view.ex = float(store.hack_enemy[0])
        hack_view.ey = float(store.hack_enemy[1])
        hack_view.ex2 = float(store.hack_enemy2[0])
        hack_view.ey2 = float(store.hack_enemy2[1])
        hack_view.clock = time.time()
        hack_view.hover = None
        hack_view.cam_x = hack_camera_target_x(hack_view.px)
        hack_view.cam_y = hack_camera_target_y(hack_view.py)
        hack_xadj.change(hack_view.cam_x)
        hack_yadj.change(hack_view.cam_y)

        hack_log("CANAL D'INTRUSION OUVERT", HK_CYAN)
        renpy.restart_interaction()

    # --------------------------------------------------------
    # Topologie
    # --------------------------------------------------------
    def hack_in_bounds(pos):
        x, y = pos
        return (0 <= y < len(store.hack_grid)
                and 0 <= x < len(store.hack_grid[y]))

    def hack_walkable(pos):
        return hack_in_bounds(pos) and store.hack_grid[pos[1]][pos[0]] != "#"

    def hack_special(pos):
        data = store.hack_specials.get(pos)
        if not data or data.get("spent"):
            return {}
        return data

    def hack_tile_type(pos):
        if pos == store.hack_goal:
            return "goal"
        return hack_special(pos).get("type", "neutral")

    def hack_direction_between(a, b):
        return (b[0] - a[0], b[1] - a[1])

    def hack_can_cross(a, b, actor="player"):
        """Les sens uniques et les pare-feu contraignent les deux camps."""
        if not hack_walkable(b):
            return False

        direction = hack_direction_between(a, b)
        source = hack_special(a)
        target = hack_special(b)

        if source.get("type") == "oneway" and tuple(source.get("direction", (1, 0))) != direction:
            return False
        if target.get("type") == "oneway" and tuple(target.get("direction", (1, 0))) != direction:
            return False

        # Un pare-feu ferme bloque la sentinelle ; le joueur peut le forcer.
        if actor != "player" and target.get("type") == "password" and b not in store.hack_solved_passwords:
            return False
        return True

    def hack_neighbors(pos, actor="enemy"):
        result = []
        for direction in HACK_DIRECTIONS.values():
            nxt = (pos[0] + direction[0], pos[1] + direction[1])
            if hack_can_cross(pos, nxt, actor):
                result.append(nxt)
        return result

    def hack_path(start, goal, actor="enemy"):
        if start == goal:
            return [start]
        queue = deque([start])
        came_from = {start: None}
        while queue:
            current = queue.popleft()
            for nxt in hack_neighbors(current, actor):
                if nxt in came_from:
                    continue
                came_from[nxt] = current
                if nxt == goal:
                    path = [nxt]
                    while path[-1] != start:
                        path.append(came_from[path[-1]])
                    path.reverse()
                    return path
                queue.append(nxt)
        return []

    def hack_path_distance(start, goal, actor="enemy"):
        path = hack_path(start, goal, actor)
        return len(path) - 1 if path else 99

    def hack_goal_distance():
        return hack_path_distance(store.hack_player, store.hack_goal, "player")

    def hack_detection_distance():
        distances = [hack_path_distance(store.hack_enemy, store.hack_player, "enemy")]
        if store.hack_enemy2_active:
            distances.append(hack_path_distance(store.hack_enemy2, store.hack_player, "enemy"))
        return min(distances)

    def hack_detection_range():
        exposed = store.hack_enemy_scan > 0.0 or (store.hack_enemy2_active and store.hack_enemy2_scan > 0.0)
        return HACK_DETECT_SCAN if exposed else HACK_DETECT

    def hack_threat_label():
        distance = hack_detection_distance()
        if store.hack_enemy_stun > 0.0 and (not store.hack_enemy2_active or store.hack_enemy2_stun > 0.0):
            return "SENTINELLE HORS LIGNE", HK_AMBER, 1
        if distance <= 3:
            return "CRITIQUE", HK_RED, 5
        if distance <= hack_detection_range():
            return "VERROUILLAGE", "#FF8A65", 4
        if store.hack_enemy_mode == "RECHERCHE" or (store.hack_enemy2_active and store.hack_enemy2_mode == "RECHERCHE"):
            return "TRACE DETECTEE", "#FFD166", 3
        return "FURTIF", HK_CYAN, 2

    def hack_preview_path(start, goal, limit=6, actor="enemy"):
        return hack_path(start, goal, actor)[1:limit + 1]

    def hack_record_trail(pos):
        trail = list(store.hack_trail)
        if not trail or trail[-1] != pos:
            trail.append(pos)
        store.hack_trail = trail[-10:]

    def hack_spend(pos):
        """Consomme une case a usage unique."""
        data = store.hack_specials.get(pos)
        if not data:
            return
        specials = dict(store.hack_specials)
        entry = dict(data)
        entry["spent"] = True
        specials[pos] = entry
        store.hack_specials = specials

    def hack_toggle_pause():
        if not store.hack_done and not store.hack_password_active:
            store.hack_paused = not store.hack_paused
            renpy.restart_interaction()

    # --------------------------------------------------------
    # Camera
    # --------------------------------------------------------
    def hack_camera_target_x(cell_x):
        target = cell_x * HACK_CELL + HACK_CELL * 0.5 - HACK_VIEW_W * 0.5
        return min(max(target, 0.0), float(max(0, hack_view.world_w - HACK_VIEW_W)))

    def hack_camera_target_y(cell_y):
        target = cell_y * HACK_CELL + HACK_CELL * 0.5 - HACK_VIEW_H * 0.5
        return min(max(target, 0.0), float(max(0, hack_view.world_h - HACK_VIEW_H)))

    def hack_driver(trans, st, at):
        """Anime jetons + cadrage a la frequence d'affichage."""
        now = time.time()
        dt = now - hack_view.clock
        hack_view.clock = now
        if dt <= 0.0 or dt > 0.25:
            dt = 1.0 / 60.0

        token = 1.0 - math.exp(-dt * 17.0)
        hack_view.px += (store.hack_player[0] - hack_view.px) * token
        hack_view.py += (store.hack_player[1] - hack_view.py) * token
        hack_view.ex += (store.hack_enemy[0] - hack_view.ex) * token
        hack_view.ey += (store.hack_enemy[1] - hack_view.ey) * token
        hack_view.ex2 += (store.hack_enemy2[0] - hack_view.ex2) * token
        hack_view.ey2 += (store.hack_enemy2[1] - hack_view.ey2) * token

        lens = 1.0 - math.exp(-dt * 9.0)
        hack_view.cam_x += (hack_camera_target_x(hack_view.px) - hack_view.cam_x) * lens
        hack_view.cam_y += (hack_camera_target_y(hack_view.py) - hack_view.cam_y) * lens
        hack_xadj.change(hack_view.cam_x)
        hack_yadj.change(hack_view.cam_y)

        if store.hack_done or store.hack_paused or store.hack_password_active:
            hack_view.hover = None
        else:
            mx, my = renpy.get_mouse_pos()
            lx = mx - HACK_VIEW_X
            ly = my - HACK_VIEW_Y
            if 0 <= lx < HACK_VIEW_W and 0 <= ly < HACK_VIEW_H:
                cx = int((lx + hack_view.cam_x) // HACK_CELL)
                cy = int((ly + hack_view.cam_y) // HACK_CELL)
                hack_view.hover = (cx, cy) if hack_walkable((cx, cy)) else None
            else:
                hack_view.hover = None
        return 0

    def hack_token_player(trans, st, at):
        trans.xanchor = 0.0
        trans.yanchor = 0.0
        trans.xpos = int(hack_view.px * HACK_CELL)
        trans.ypos = int(hack_view.py * HACK_CELL)
        trans.zoom = 1.0 + 0.05 * math.sin(st * 3.4)
        return 0

    def hack_token_enemy(trans, st, at):
        trans.xanchor = 0.0
        trans.yanchor = 0.0
        trans.xpos = int(hack_view.ex * HACK_CELL)
        trans.ypos = int(hack_view.ey * HACK_CELL)
        speed = 6.4 if store.hack_enemy_mode == "VERROUILLAGE" else 3.0
        trans.zoom = 1.0 + 0.07 * math.sin(st * speed)
        return 0

    def hack_token_enemy2(trans, st, at):
        trans.xanchor = 0.0
        trans.yanchor = 0.0
        trans.xpos = int(hack_view.ex2 * HACK_CELL)
        trans.ypos = int(hack_view.ey2 * HACK_CELL)
        speed = 6.8 if store.hack_enemy2_mode == "VERROUILLAGE" else 3.4
        trans.zoom = 1.0 + 0.07 * math.sin(st * speed + 1.7)
        return 0

    def hack_halo_player(trans, st, at):
        trans.xanchor = 0.5
        trans.yanchor = 0.5
        trans.xpos = int(hack_view.px * HACK_CELL + HACK_CELL // 2)
        trans.ypos = int(hack_view.py * HACK_CELL + HACK_CELL // 2)
        trans.alpha = 0.42 + 0.16 * math.sin(st * 2.6)
        return 0

    def hack_halo_enemy(trans, st, at):
        trans.xanchor = 0.5
        trans.yanchor = 0.5
        trans.xpos = int(hack_view.ex * HACK_CELL + HACK_CELL // 2)
        trans.ypos = int(hack_view.ey * HACK_CELL + HACK_CELL // 2)
        base = 0.62 if store.hack_enemy_mode == "VERROUILLAGE" else 0.38
        trans.alpha = base + 0.18 * math.sin(st * 5.0)
        return 0

    def hack_halo_enemy2(trans, st, at):
        trans.xanchor = 0.5
        trans.yanchor = 0.5
        trans.xpos = int(hack_view.ex2 * HACK_CELL + HACK_CELL // 2)
        trans.ypos = int(hack_view.ey2 * HACK_CELL + HACK_CELL // 2)
        base = 0.62 if store.hack_enemy2_mode == "VERROUILLAGE" else 0.38
        trans.alpha = base + 0.18 * math.sin(st * 5.3 + 1.4)
        return 0

    def hack_screen_pos(cell):
        """Position ecran (centre) d'une case, et si elle est hors cadre."""
        cx = cell[0] * HACK_CELL + HACK_CELL * 0.5 - hack_view.cam_x
        cy = cell[1] * HACK_CELL + HACK_CELL * 0.5 - hack_view.cam_y
        inside = (40 <= cx <= HACK_VIEW_W - 40) and (40 <= cy <= HACK_VIEW_H - 40)
        cx = min(max(cx, 44), HACK_VIEW_W - 44)
        cy = min(max(cy, 44), HACK_VIEW_H - 44)
        return (not inside, int(HACK_VIEW_X + cx), int(HACK_VIEW_Y + cy))

    # --------------------------------------------------------
    # Resolution des cases
    # --------------------------------------------------------
    def hack_collide():
        primary_hit = store.hack_player == store.hack_enemy
        secondary_hit = store.hack_enemy2_active and store.hack_player == store.hack_enemy2
        if (not primary_hit and not secondary_hit) or store.hack_done:
            return
        store.hack_hits += 1
        store.hack_time_left = max(0.0, store.hack_time_left - 5.0)
        hack_play("hk_hit.wav", 0.85)
        if store.hack_hits >= store.hack_max_hits:
            hack_finish(False, "SIGNAL DETRUIT // CONNEXION COUPEE")
            return
        store.hack_player = store.hack_player_start
        store.hack_player_previous = store.hack_player_start
        store.hack_enemy = store.hack_enemy_start
        store.hack_enemy_previous = None
        store.hack_enemy_mode = "PATROUILLE"
        store.hack_enemy_stun = 0.0
        store.hack_enemy_scan = 0.0
        store.hack_enemy2 = store.hack_enemy2_start
        store.hack_enemy2_previous = None
        store.hack_enemy2_mode = "PATROUILLE"
        store.hack_enemy2_stun = 0.0
        store.hack_enemy2_scan = 0.0
        store.hack_enemy2_clock = store.hack_enemy2_interval
        store.hack_player_stun = 0.75
        store.hack_dash_cooldown = 0.0
        store.hack_trail = [store.hack_player_start]
        hack_view.px = float(store.hack_player_start[0])
        hack_view.py = float(store.hack_player_start[1])
        hack_view.ex = float(store.hack_enemy_start[0])
        hack_view.ey = float(store.hack_enemy_start[1])
        hack_view.ex2 = float(store.hack_enemy2_start[0])
        hack_view.ey2 = float(store.hack_enemy2_start[1])
        hack_status_set("INTERCEPTION // SIGNAL REINITIALISE // -5 S", HK_RED, True)
        store.hack_flash = 0.45
        store.hack_flash_color = "#FF173C"

    def hack_finish(success, message):
        store.hack_done = True
        store.hack_success = success
        store.hack_end_delay = 1.7 if success else 0.9
        hack_status_set(message, HK_MINT if success else HK_RED, True)
        store.hack_flash = 0.55
        store.hack_flash_color = "#1CFFC8" if success else "#FF173C"
        hack_play("hk_goal.wav" if success else "hk_fail.wav", 0.9)

    def hack_activate_password(pos):
        store.hack_password_active = True
        store.hack_password_cell = pos
        store.hack_password_sequence = [random.choice(("z", "q", "s", "d")) for _ in range(5)]
        store.hack_password_progress = 0
        store.hack_password_total = 6.0
        store.hack_password_time = store.hack_password_total
        hack_status_set("PARE-FEU // SAISISSEZ LA SEQUENCE", HK_VIOLET, True)

    def hack_password_fail(message="SEQUENCE REFUSEE"):
        store.hack_password_active = False
        hack_play("hk_deny.wav", 0.75)
        store.hack_time_left = max(0.0, store.hack_time_left - 4.0)
        store.hack_player = store.hack_player_previous
        store.hack_player_stun = 0.6
        hack_status_set(message + " // -4 SECONDES", HK_RED, True)
        store.hack_flash = 0.30
        store.hack_flash_color = "#FF173C"

    def hack_password_press(key):
        if not store.hack_password_active:
            return
        expected = store.hack_password_sequence[store.hack_password_progress]
        if key != expected:
            hack_password_fail()
            renpy.restart_interaction()
            return
        store.hack_password_progress += 1
        hack_play("hk_key.wav", 0.5)
        if store.hack_password_progress >= len(store.hack_password_sequence):
            solved = list(store.hack_solved_passwords)
            if store.hack_password_cell not in solved:
                solved.append(store.hack_password_cell)
            store.hack_solved_passwords = solved
            store.hack_password_active = False
            hack_play("hk_unlock.wav", 0.8)
            hack_status_set("PARE-FEU FORCE // LA VOIE S'OUVRE POUR TOUS", HK_MINT, True)
        renpy.restart_interaction()

    def hack_resolve_tile(pos, direction, allow_boost=True):
        tile = hack_tile_type(pos)
        data = hack_special(pos)

        if tile == "goal":
            hack_finish(True, "NOYAU ATTEINT // ACCES AUTORISE")
            return
        if tile == "password" and pos not in store.hack_solved_passwords:
            hack_activate_password(pos)
            return
        if tile == "trap":
            hack_spend(pos)
            store.hack_player_stun = max(store.hack_player_stun, 3.0)
            hack_play("hk_trap.wav", 0.8)
            hack_status_set("PIEGE DE VERROUILLAGE // IMMOBILISE 3 S", "#FF755D", True)
            store.hack_flash = 0.20
            store.hack_flash_color = "#FF5A2E"
            return
        if tile == "boost" and allow_boost:
            hack_play("hk_dash.wav", 0.5)
            hack_status_set("ACCELERATEUR // +2 CASES", HK_CYAN, True)
            for _unused in range(2):
                if store.hack_done or store.hack_password_active:
                    break
                nxt = (store.hack_player[0] + direction[0], store.hack_player[1] + direction[1])
                if not hack_can_cross(store.hack_player, nxt, "player"):
                    break
                store.hack_player_previous = store.hack_player
                store.hack_player = nxt
                hack_record_trail(nxt)
                hack_collide()
                if store.hack_player != nxt:
                    break
                hack_resolve_tile(nxt, direction, allow_boost=False)
            return
        if tile == "oneway":
            hack_status_set("PASSAGE A SENS UNIQUE", HK_CYAN)
        elif tile == "sign":
            store.hack_sign_message = data.get("message", "BALISE SANS DONNEES")
            store.hack_sign_time = 3.5
            hack_play("hk_beacon.wav", 0.55)
            hack_status_set("BALISE CONSULTEE", HK_AMBER)

    def hack_enemy_resolve_tile(pos, direction, allow_boost=True):
        """Les cases speciales mordent aussi sur la sentinelle."""
        tile = hack_tile_type(pos)
        if tile == "trap":
            hack_spend(pos)
            store.hack_enemy_stun = 3.2
            store.hack_enemy_mode = "PATROUILLE"
            hack_play("hk_trap.wav", 0.7)
            hack_status_set("SENTINELLE PIEGEE // 3 S HORS LIGNE", HK_AMBER, True)
            return
        if tile == "boost" and allow_boost:
            if direction == (0, 0):
                return
            for _unused in range(2):
                nxt = (store.hack_enemy[0] + direction[0], store.hack_enemy[1] + direction[1])
                if not hack_can_cross(store.hack_enemy, nxt, "enemy"):
                    break
                store.hack_enemy_previous = store.hack_enemy
                store.hack_enemy = nxt
                hack_collide()
                if store.hack_done:
                    return
            hack_status_set("SENTINELLE PROPULSEE", HK_RED, True)
            return
        if tile == "sign":
            store.hack_enemy_scan = 5.0
            hack_play("hk_alert.wav", 0.7)
            hack_status_set("BALISE PIRATEE // VOTRE POSITION EST EXPOSEE", HK_RED, True)

    def hack_enemy2_resolve_tile(pos, direction, allow_boost=True):
        """Resolution des modules pour la seconde sentinelle."""
        tile = hack_tile_type(pos)
        if tile == "trap":
            hack_spend(pos)
            store.hack_enemy2_stun = 3.2
            store.hack_enemy2_mode = "PATROUILLE"
            hack_play("hk_trap.wav", 0.7)
            hack_status_set("SENTINELLE B PIEGEE // 3 S HORS LIGNE", HK_AMBER, True)
            return
        if tile == "boost" and allow_boost:
            if direction == (0, 0):
                return
            for _unused in range(2):
                nxt = (store.hack_enemy2[0] + direction[0], store.hack_enemy2[1] + direction[1])
                if not hack_can_cross(store.hack_enemy2, nxt, "enemy"):
                    break
                store.hack_enemy2_previous = store.hack_enemy2
                store.hack_enemy2 = nxt
                hack_collide()
                if store.hack_done:
                    return
            hack_status_set("SENTINELLE B PROPULSEE", HK_RED, True)
            return
        if tile == "sign":
            store.hack_enemy2_scan = 5.0
            hack_play("hk_alert.wav", 0.7)
            hack_status_set("BALISE PIRATEE // DOUBLE TRACE ACTIVE", HK_RED, True)

    # --------------------------------------------------------
    # Actions joueur
    # --------------------------------------------------------
    def hack_blocked(message="ROUTE INACCESSIBLE"):
        hack_play("hk_deny.wav", 0.45)
        hack_status_set(message, "#FFD166")
        renpy.restart_interaction()

    def hack_try_move(dx, dy):
        if store.hack_done or store.hack_paused or store.hack_password_active or store.hack_player_stun > 0.0:
            return
        current = store.hack_player
        target = (current[0] + dx, current[1] + dy)
        if not hack_can_cross(current, target, "player"):
            hack_blocked()
            return
        store.hack_player_previous = current
        store.hack_player = target
        store.hack_last_direction = (dx, dy)
        hack_record_trail(target)
        hack_play("hk_move.wav", 0.32)
        hack_status_set("INTRUSION EN COURS", HK_CYAN)
        hack_collide()
        if store.hack_player == target:
            hack_resolve_tile(target, (dx, dy))
        renpy.restart_interaction()

    def hack_try_dash(dx=None, dy=None, steps=3):
        if store.hack_done or store.hack_paused or store.hack_password_active or store.hack_player_stun > 0.0:
            return
        if store.hack_dash_cooldown > 0.0:
            hack_blocked("PROPULSION EN RECHARGE // {:.1f} S".format(store.hack_dash_cooldown))
            return

        if dx is None or dy is None:
            dx, dy = store.hack_last_direction
        direction = (int(dx), int(dy))
        moved = 0
        for _unused in range(max(1, min(3, int(steps)))):
            current = store.hack_player
            target = (current[0] + direction[0], current[1] + direction[1])
            if not hack_can_cross(current, target, "player"):
                break
            store.hack_player_previous = current
            store.hack_player = target
            hack_record_trail(target)
            moved += 1
            hack_collide()
            if store.hack_player != target or store.hack_done:
                break
            hack_resolve_tile(target, direction, allow_boost=False)
            if store.hack_password_active or store.hack_done:
                break

        if moved:
            store.hack_last_direction = direction
            store.hack_dash_cooldown = store.hack_dash_cooldown_max
            hack_play("hk_dash.wav", 0.6)
            if not store.hack_done and not store.hack_password_active:
                hack_status_set("PROPULSION PHASEE // {} CASE{}".format(moved, "S" if moved > 1 else ""),
                                "#72EAFF", True)
        else:
            hack_blocked("AUCUN VECTEUR DE PROPULSION")
            return
        renpy.restart_interaction()

    def hack_click_cell(x, y):
        pos = (x, y)
        data = hack_special(pos)
        dx = x - store.hack_player[0]
        dy = y - store.hack_player[1]
        if data.get("type") == "sign" and abs(dx) + abs(dy) > 1:
            store.hack_sign_message = data.get("message", "BALISE SANS DONNEES")
            store.hack_sign_time = 3.5
            hack_play("hk_beacon.wav", 0.5)
            hack_status_set("BALISE CONSULTEE A DISTANCE", HK_AMBER)
            renpy.restart_interaction()
            return
        if abs(dx) + abs(dy) == 1:
            hack_try_move(dx, dy)
        elif ((dx == 0) != (dy == 0)) and 2 <= abs(dx) + abs(dy) <= 3:
            distance = abs(dx) + abs(dy)
            hack_try_dash(0 if dx == 0 else (1 if dx > 0 else -1),
                          0 if dy == 0 else (1 if dy > 0 else -1), distance)
        else:
            hack_blocked("CASE VOISINE OU PROPULSION EN LIGNE DROITE")

    def hack_click_view():
        if store.hack_done or store.hack_paused or store.hack_password_active:
            return
        mx, my = renpy.get_mouse_pos()
        lx = mx - HACK_VIEW_X + hack_view.cam_x
        ly = my - HACK_VIEW_Y + hack_view.cam_y
        if lx < 0 or ly < 0:
            return
        hack_click_cell(int(lx // HACK_CELL), int(ly // HACK_CELL))

    # --------------------------------------------------------
    # Sentinelle
    # --------------------------------------------------------
    def hack_enemy_step():
        if store.hack_done or store.hack_enemy_stun > 0.0:
            return
        previous_mode = store.hack_enemy_mode
        pursuit = hack_path(store.hack_enemy, store.hack_player, "enemy")
        distance = len(pursuit) - 1 if pursuit else 99
        if pursuit and distance <= hack_detection_range():
            nxt = pursuit[1] if len(pursuit) > 1 else store.hack_player
            store.hack_enemy_mode = "VERROUILLAGE"
            if previous_mode != "VERROUILLAGE":
                hack_play("hk_alert.wav", 0.55)
                hack_status_set("ALERTE // KAMI A VERROUILLE VOTRE POSITION", HK_RED, True)
        else:
            trace_path = []
            for trace_pos in reversed(store.hack_trail[:-1]):
                candidate_path = hack_path(store.hack_enemy, trace_pos, "enemy")
                if candidate_path and len(candidate_path) - 1 <= 4:
                    trace_path = candidate_path
                    break

            if len(trace_path) > 1:
                nxt = trace_path[1]
                store.hack_enemy_mode = "RECHERCHE"
                if previous_mode != "RECHERCHE":
                    hack_status_set("TRACE RESIDUELLE DETECTEE // CHANGEZ DE ROUTE", "#FFD166", True)
            else:
                candidates = hack_neighbors(store.hack_enemy, "enemy")
                if store.hack_enemy_previous in candidates and len(candidates) > 1:
                    candidates.remove(store.hack_enemy_previous)
                if not candidates:
                    store.hack_enemy_previous = None
                    return
                # La sentinelle prefere les embranchements proches de l'objectif,
                # sans connaitre parfaitement la position du joueur hors detection.
                candidates.sort(key=lambda pos: hack_path_distance(pos, store.hack_goal, "enemy"))
                shortlist = candidates[:min(2, len(candidates))]
                nxt = random.choice(shortlist)
                store.hack_enemy_mode = "PATROUILLE"

        direction = hack_direction_between(store.hack_enemy, nxt)
        store.hack_enemy_previous = store.hack_enemy
        store.hack_enemy = nxt
        hack_collide()
        if not store.hack_done:
            hack_enemy_resolve_tile(nxt, direction)

    def hack_enemy2_step():
        if store.hack_done or not store.hack_enemy2_active or store.hack_enemy2_stun > 0.0:
            return
        previous_mode = store.hack_enemy2_mode
        pursuit = hack_path(store.hack_enemy2, store.hack_player, "enemy")
        distance = len(pursuit) - 1 if pursuit else 99
        detect_range = HACK_DETECT_SCAN if store.hack_enemy2_scan > 0.0 else HACK_DETECT

        if pursuit and distance <= detect_range:
            nxt = pursuit[1] if len(pursuit) > 1 else store.hack_player
            store.hack_enemy2_mode = "VERROUILLAGE"
            if previous_mode != "VERROUILLAGE":
                hack_play("hk_alert.wav", 0.55)
                hack_status_set("ALERTE // SECONDE SENTINELLE VERROUILLEE", HK_RED, True)
        else:
            trace_path = []
            for trace_pos in reversed(store.hack_trail[:-1]):
                candidate_path = hack_path(store.hack_enemy2, trace_pos, "enemy")
                if candidate_path and len(candidate_path) - 1 <= 5:
                    trace_path = candidate_path
                    break

            if len(trace_path) > 1:
                nxt = trace_path[1]
                store.hack_enemy2_mode = "RECHERCHE"
            else:
                candidates = hack_neighbors(store.hack_enemy2, "enemy")
                if store.hack_enemy2_previous in candidates and len(candidates) > 1:
                    candidates.remove(store.hack_enemy2_previous)
                if not candidates:
                    store.hack_enemy2_previous = None
                    return
                # La seconde sentinelle ferme plutot les routes proches du joueur.
                candidates.sort(key=lambda pos: hack_path_distance(pos, store.hack_player, "enemy"))
                shortlist = candidates[:min(3, len(candidates))]
                nxt = random.choice(shortlist)
                store.hack_enemy2_mode = "PATROUILLE"

        direction = hack_direction_between(store.hack_enemy2, nxt)
        store.hack_enemy2_previous = store.hack_enemy2
        store.hack_enemy2 = nxt
        hack_collide()
        if not store.hack_done:
            hack_enemy2_resolve_tile(nxt, direction)

    def hack_tick():
        if store.hack_done:
            store.hack_end_delay = max(0.0, store.hack_end_delay - HACK_TICK)
            store.hack_flash = max(0.0, store.hack_flash - HACK_TICK)
            renpy.restart_interaction()
            return
        if store.hack_paused:
            return

        store.hack_time_left = max(0.0, store.hack_time_left - HACK_TICK)
        store.hack_enemy_clock -= HACK_TICK
        store.hack_player_stun = max(0.0, store.hack_player_stun - HACK_TICK)
        store.hack_enemy_stun = max(0.0, store.hack_enemy_stun - HACK_TICK)
        store.hack_enemy_scan = max(0.0, store.hack_enemy_scan - HACK_TICK)
        store.hack_enemy2_stun = max(0.0, store.hack_enemy2_stun - HACK_TICK)
        store.hack_enemy2_scan = max(0.0, store.hack_enemy2_scan - HACK_TICK)
        if store.hack_enemy2_active:
            store.hack_enemy2_clock -= HACK_TICK
        store.hack_dash_cooldown = max(0.0, store.hack_dash_cooldown - HACK_TICK)
        store.hack_flash = max(0.0, store.hack_flash - HACK_TICK)
        store.hack_sign_time = max(0.0, store.hack_sign_time - HACK_TICK)

        marker = int(store.hack_time_left)
        if store.hack_time_left <= 10.0 and marker != store.hack_tick_marker:
            store.hack_tick_marker = marker
            hack_play("hk_tick.wav", 0.5)

        if store.hack_password_active:
            store.hack_password_time = max(0.0, store.hack_password_time - HACK_TICK)
            if store.hack_password_time <= 0.0:
                hack_password_fail("PARE-FEU EXPIRE")

        if store.hack_enemy_clock <= 0.0:
            hack_enemy_step()
            if store.hack_enemy_mode == "VERROUILLAGE":
                speed_factor = 0.68
            elif store.hack_enemy_mode == "RECHERCHE":
                speed_factor = 0.82
            else:
                speed_factor = 1.0
            store.hack_enemy_clock += store.hack_enemy_interval * speed_factor

        if store.hack_enemy2_active and store.hack_enemy2_clock <= 0.0:
            hack_enemy2_step()
            if store.hack_enemy2_mode == "VERROUILLAGE":
                speed_factor2 = 0.68
            elif store.hack_enemy2_mode == "RECHERCHE":
                speed_factor2 = 0.82
            else:
                speed_factor2 = 1.0
            store.hack_enemy2_clock += store.hack_enemy2_interval * speed_factor2

        if store.hack_time_left <= 0.0 and not store.hack_done:
            hack_finish(False, "FENETRE D'INTRUSION EXPIREE")
        renpy.restart_interaction()

    def hack_tile_image(pos):
        tile = hack_tile_type(pos)
        if tile == "password" and pos in store.hack_solved_passwords:
            return "hk_firewall_open"
        return HACK_TILE_IMAGE.get(tile, "hk_floor")

    def hack_tile_glow(pos):
        return {
            "goal": "hk_glow_mint",
            "password": "hk_glow_violet",
            "trap": "hk_glow_red",
            "sign": "hk_glow_amber",
        }.get(hack_tile_type(pos), "hk_glow_cyan")

    def hack_oneway_rotation(pos):
        direction = tuple(hack_special(pos).get("direction", (0, -1)))
        return {(0, -1): 0, (1, 0): 90, (0, 1): 180, (-1, 0): 270}.get(direction, 0)

    def hack_special_cells():
        """Cases speciales visibles, objectif inclus."""
        cells = [(store.hack_goal, "goal")]
        for pos, data in store.hack_specials.items():
            if pos == store.hack_goal:
                continue
            cells.append((pos, data.get("type", "neutral")))
        return cells


init -5 python:
    try:
        renpy.music.register_channel("hackamb", mixer="sfx", loop=True)
    except Exception:
        pass


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------
style hk_h1 is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#4AE3FF"
    kerning 4

style hk_h2 is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#E4FAFF"
    kerning 2

style hk_label is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#5C8296"
    kerning 3

style hk_value is text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#E4FAFF"
    kerning 1

style hk_body is text:
    font "fonts/Barlow-Light.ttf"
    color "#B7CCD5"
    kerning 0

style hk_button is button:
    background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
    hover_background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
    padding (26, 12)

style hk_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#9FD9EE"
    hover_color "#FFFFFF"
    kerning 4
    size 26
    xalign 0.5
    yalign 0.5


# ------------------------------------------------------------
# Briefing
# ------------------------------------------------------------
screen j901_hack_howto():
    modal True
    zorder 500

    add Solid("#02060B")
    add Tile("hk_hexfield") alpha 0.55
    add Solid("#0B2940") alpha 0.20
    add Solid("#1AE4FF12", xsize=1920, ysize=22) at hk_scan_sweep

    vbox:
        xalign 0.5
        ypos 92
        spacing 8
        text "PROTOCOLE D'INTRUSION" style "hk_h1" size 54 xalign 0.5
        text hack_channel style "hk_label" size 20 color "#FF6B68" xalign 0.5

    hbox:
        xalign 0.5
        ypos 214
        spacing 26

        frame:
            xsize 486 ysize 396
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (32, 28)
            vbox:
                xfill True spacing 14
                add Transform("hk_player", xysize=(132, 132)) xalign 0.5
                text "SIGNAL MOBILE" style "hk_h2" size 28 color "#4AE3FF" xalign 0.5
                text "ZQSD, flèches ou clic sur une case de la ligne. La caméra suit votre jeton." style "hk_body" size 21 xalign 0.5 text_align 0.5 xmaximum 400
                text "ESPACE  //  PROPULSION 3 CASES" style "hk_label" size 19 color "#E4FAFF" xalign 0.5

        frame:
            xsize 486 ysize 396
            background Frame("minijeu/hack/assets/hk_panel_red.png", 34, 34)
            padding (32, 28)
            vbox:
                xfill True spacing 14
                add Transform("hk_enemy", xysize=(132, 132)) xalign 0.5
                text ("2 SENTINELLES KAMI" if hack_enemy2_active else "SENTINELLE KAMI") style "hk_h2" size 28 color "#FF5968" xalign 0.5
                text ("Elles patrouillent par deux routes et accélèrent dès qu'elles captent votre trace." if hack_enemy2_active else "Elle patrouille hors champ, puis accélère dès qu'elle capte votre trace à six cases.") style "hk_body" size 21 xalign 0.5 text_align 0.5 xmaximum 400
                text "3 INTERCEPTIONS  //  ECHEC" style "hk_label" size 19 color "#FF8B94" xalign 0.5

        frame:
            xsize 486 ysize 396
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (32, 28)
            vbox:
                xfill True spacing 14
                add Transform("hk_goal", xysize=(132, 132)) xalign 0.5
                text "NOYAU DE CONNEXION" style "hk_h2" size 28 color "#5CFFC0" xalign 0.5
                text "Atteignez le noyau avant la coupure. Plusieurs boucles mènent au but." style "hk_body" size 21 xalign 0.5 text_align 0.5 xmaximum 400
                text "[hack_total_time:.0f] S  //  ROUTES MULTIPLES" style "hk_label" size 19 color "#E4FAFF" xalign 0.5

    frame:
        xalign 0.5
        ypos 640
        xsize 1524 ysize 208
        background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
        padding (30, 20)
        vbox:
            xfill True spacing 12
            text "MODULES DU RESEAU  //  ILS AGISSENT SUR LES DEUX CAMPS" style "hk_label" size 19 xalign 0.5
            hbox:
                xalign 0.5
                spacing 22
                for _art, _title, _desc in (
                        ("hk_oneway", "SENS UNIQUE", "Infranchissable à contresens, pour vous comme pour elle."),
                        ("hk_boost", "ACCELERATEUR", "Projette de 2 cases dans la direction d'entrée."),
                        ("hk_trap", "PIEGE", "Immobilise 3 s le premier qui le déclenche. Usage unique."),
                        ("hk_firewall", "PARE-FEU", "Bloque la sentinelle. Le forcer ouvre la voie aux deux."),
                        ("hk_beacon", "BALISE", "Vous informe. Piratée par Kami, elle vous expose.")):
                    vbox:
                        xsize 274 spacing 5
                        hbox:
                            spacing 10
                            add Transform(_art, xysize=(56, 56)) yalign 0.5
                            text _title style "hk_h2" size 21 yalign 0.5
                        text _desc style "hk_body" size 17 xmaximum 268

    textbutton "INITIALISER LE SIGNAL":
        style "hk_button"
        xalign 0.5
        ypos 888
        xsize 470
        ysize 74
        action Return(True)

    add "hk_scanlines" alpha 0.55
    add "hk_vignette"
    add "hk_bezel"


# ------------------------------------------------------------
# Partie
# ------------------------------------------------------------
screen j901_hack_screen():
    modal True
    zorder 500

    $ _time_ratio = max(0.0, min(1.0, hack_time_left / max(0.001, hack_total_time)))
    $ _dash_ratio = 1.0 - max(0.0, min(1.0, hack_dash_cooldown / hack_dash_cooldown_max))
    $ _threat = hack_threat_label()
    $ _threat_text = _threat[0]
    $ _threat_color = _threat[1]
    $ _threat_level = _threat[2]
    $ _enemy_distance = hack_detection_distance()
    $ _goal_raw = hack_goal_distance()
    $ _goal_distance = _goal_raw if _goal_raw < 99 else "--"
    $ _bar_w = max(3, int(1620 * _time_ratio))
    $ _low_time = hack_time_left <= 12.0

    add Solid("#02060B")
    add Tile("hk_hexfield") alpha 0.40
    add Null(width=1, height=1) at hk_driver_at

    # ---------- Plateau ----------
    viewport:
        xpos HACK_VIEW_X
        ypos HACK_VIEW_Y
        xysize (HACK_VIEW_W, HACK_VIEW_H)
        child_size (hack_view.world_w, hack_view.world_h)
        xadjustment hack_xadj
        yadjustment hack_yadj
        draggable False
        mousewheel False
        arrowkeys False
        pagekeys False

        fixed:
            xysize (hack_view.world_w, hack_view.world_h)

            add hack_view.world

            # Modules speciaux
            for _pos, _kind in hack_special_cells():
                $ _px = _pos[0] * HACK_CELL
                $ _py = _pos[1] * HACK_CELL
                $ _spent = bool(hack_specials.get(_pos, {}).get("spent"))
                if _kind == "goal":
                    add Transform("hk_glow_mint", xysize=(230, 230)) xpos _px - 63 ypos _py - 63 at hk_pulse_soft
                    add Transform("hk_goal", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py
                elif _kind == "oneway":
                    add Transform("hk_oneway", xysize=(HACK_CELL, HACK_CELL), rotate=hack_oneway_rotation(_pos), rotate_pad=False) xpos _px ypos _py
                elif _kind == "password":
                    if _pos in hack_solved_passwords:
                        add Transform("hk_firewall_open", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py alpha 0.75
                    else:
                        add Transform("hk_glow_violet", xysize=(180, 180)) xpos _px - 38 ypos _py - 38 at hk_pulse_soft
                        add Transform("hk_firewall", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py
                elif _kind == "trap":
                    if _spent:
                        add Transform("hk_trap", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py alpha 0.22
                    else:
                        add Transform("hk_glow_red", xysize=(170, 170)) xpos _px - 33 ypos _py - 33 at hk_pulse_fast
                        add Transform("hk_trap", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py
                elif _kind == "boost":
                    add Transform("hk_boost", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py
                elif _kind == "sign":
                    add Transform("hk_beacon", xysize=(HACK_CELL, HACK_CELL)) xpos _px ypos _py

            # Trace persistante
            for _trail_index in range(1, len(hack_trail)):
                $ _ta = hack_trail[_trail_index - 1]
                $ _tb = hack_trail[_trail_index]
                $ _tax = _ta[0] * HACK_CELL + HACK_CELL // 2
                $ _tay = _ta[1] * HACK_CELL + HACK_CELL // 2
                $ _tbx = _tb[0] * HACK_CELL + HACK_CELL // 2
                $ _tby = _tb[1] * HACK_CELL + HACK_CELL // 2
                $ _talpha = 0.08 + 0.26 * (_trail_index / float(max(1, len(hack_trail) - 1)))
                if _tax == _tbx:
                    add Solid("#27DFFF", xsize=4, ysize=abs(_tby - _tay)) xpos _tax - 2 ypos min(_tay, _tby) alpha _talpha
                else:
                    add Solid("#27DFFF", xsize=abs(_tbx - _tax), ysize=4) xpos min(_tax, _tbx) ypos _tay - 2 alpha _talpha

            # Route conseillee vers le noyau
            $ _goal_preview = hack_preview_path(hack_player, hack_goal, 6, "player")
            for _route_index, _route_pos in enumerate(_goal_preview):
                add Solid("#70ECFF", xsize=10, ysize=10) xpos _route_pos[0] * HACK_CELL + 47 ypos _route_pos[1] * HACK_CELL + 47 at hk_route_pulse(_route_index * 0.07)

            # Trajectoire de poursuite
            if _enemy_distance <= hack_detection_range() and hack_enemy_stun <= 0.0:
                $ _enemy_preview = hack_preview_path(hack_enemy, hack_player, 4, "enemy")
                for _route_index, _route_pos in enumerate(_enemy_preview):
                    add Solid("#FF465C", xsize=13, ysize=13) xpos _route_pos[0] * HACK_CELL + 45 ypos _route_pos[1] * HACK_CELL + 45 at hk_route_pulse(_route_index * 0.06)

            if hack_enemy2_active and hack_enemy2_stun <= 0.0:
                $ _enemy2_distance = hack_path_distance(hack_enemy2, hack_player, "enemy")
                if _enemy2_distance <= (HACK_DETECT_SCAN if hack_enemy2_scan > 0.0 else HACK_DETECT):
                    $ _enemy2_preview = hack_preview_path(hack_enemy2, hack_player, 4, "enemy")
                    for _route_index, _route_pos in enumerate(_enemy2_preview):
                        add Solid("#FF8A65", xsize=11, ysize=11) xpos _route_pos[0] * HACK_CELL + 46 ypos _route_pos[1] * HACK_CELL + 46 at hk_route_pulse(_route_index * 0.06 + 0.03)

            # Survol
            if hack_view.hover:
                $ _hx = hack_view.hover[0] * HACK_CELL
                $ _hy = hack_view.hover[1] * HACK_CELL
                add Solid("#4AE3FF", xsize=HACK_CELL - 8, ysize=3) xpos _hx + 4 ypos _hy + 4 alpha 0.75
                add Solid("#4AE3FF", xsize=HACK_CELL - 8, ysize=3) xpos _hx + 4 ypos _hy + HACK_CELL - 7 alpha 0.75
                add Solid("#4AE3FF", xsize=3, ysize=HACK_CELL - 8) xpos _hx + 4 ypos _hy + 4 alpha 0.75
                add Solid("#4AE3FF", xsize=3, ysize=HACK_CELL - 8) xpos _hx + HACK_CELL - 7 ypos _hy + 4 alpha 0.75
                add Solid("#4AE3FF", xsize=HACK_CELL - 14, ysize=HACK_CELL - 14) xpos _hx + 7 ypos _hy + 7 alpha 0.07

            # Jetons
            add Transform("hk_glow_red", xysize=(250, 250)) at hk_enemy_halo_at
            if hack_enemy2_active:
                add Transform("hk_glow_red", xysize=(250, 250), matrixcolor=TintMatrix("#FF8A65")) at hk_enemy2_halo_at
            add Transform("hk_glow_cyan", xysize=(260, 260)) at hk_player_halo_at
            add Transform("hk_enemy", xysize=(HACK_CELL, HACK_CELL)) at hk_enemy_at
            if hack_enemy2_active:
                add Transform("hk_enemy", xysize=(HACK_CELL, HACK_CELL), matrixcolor=TintMatrix("#FFB06A")) at hk_enemy2_at
            add Transform("hk_player", xysize=(HACK_CELL, HACK_CELL)) at hk_player_at

    # Zone de clic (ne prend jamais le focus clavier)
    button:
        xpos HACK_VIEW_X
        ypos HACK_VIEW_Y
        xysize (HACK_VIEW_W, HACK_VIEW_H)
        background None
        keyboard_focus False
        action Function(hack_click_view)

    # Halo de bord teinte par la menace
    add Transform("hk_edge", xysize=(HACK_VIEW_W, HACK_VIEW_H), matrixcolor=TintMatrix(_threat_color)) xpos HACK_VIEW_X ypos HACK_VIEW_Y alpha (0.34 if _threat_level >= 4 else 0.13)

    # Reperes hors cadre
    $ _goal_marker = hack_screen_pos(hack_goal)
    if _goal_marker[0]:
        add Transform("hk_glow_mint", xysize=(96, 96), xanchor=0.5, yanchor=0.5) xpos _goal_marker[1] ypos _goal_marker[2] at hk_pulse_soft
        text "NOYAU [_goal_distance]" style "hk_label" size 16 color "#5CFFC0" xpos _goal_marker[1] ypos _goal_marker[2] + 30 xanchor 0.5

    $ _enemy_marker = hack_screen_pos(hack_enemy)
    if _enemy_marker[0]:
        add Transform("hk_glow_red", xysize=(88, 88), xanchor=0.5, yanchor=0.5) xpos _enemy_marker[1] ypos _enemy_marker[2] at hk_pulse_fast
        text ("KAMI [_enemy_distance]" if _enemy_distance < 99 else "KAMI") style "hk_label" size 16 color "#FF3D5C" xpos _enemy_marker[1] ypos _enemy_marker[2] + 30 xanchor 0.5

    if hack_enemy2_active:
        $ _enemy2_marker = hack_screen_pos(hack_enemy2)
        $ _enemy2_distance = hack_path_distance(hack_enemy2, hack_player, "enemy")
        if _enemy2_marker[0]:
            add Transform("hk_glow_red", xysize=(88, 88), xanchor=0.5, yanchor=0.5, matrixcolor=TintMatrix("#FF8A65")) xpos _enemy2_marker[1] ypos _enemy2_marker[2] at hk_pulse_fast
            text ("KAMI-B [_enemy2_distance]" if _enemy2_distance < 99 else "KAMI-B") style "hk_label" size 16 color "#FF8A65" xpos _enemy2_marker[1] ypos _enemy2_marker[2] + 30 xanchor 0.5

    # ---------- Mini-carte ----------
    $ _mini_cell = 13
    $ _mini_x = HACK_VIEW_X + HACK_VIEW_W - hack_view.mini_w - 34
    $ _mini_y = HACK_VIEW_Y + 18
    frame:
        xpos _mini_x - 16
        ypos _mini_y - 34
        xsize hack_view.mini_w + 32
        ysize hack_view.mini_h + 50
        background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
        padding (0, 0)
        text "TOPOLOGIE" style "hk_label" size 15 xpos 16 ypos 8

    add hack_view.minimap xpos _mini_x ypos _mini_y
    add Solid("#5CFFC0", xsize=9, ysize=9) xpos _mini_x + hack_goal[0] * _mini_cell + 2 ypos _mini_y + hack_goal[1] * _mini_cell + 2
    add Solid("#FF3D5C", xsize=9, ysize=9) xpos _mini_x + hack_enemy[0] * _mini_cell + 2 ypos _mini_y + hack_enemy[1] * _mini_cell + 2 at hk_pulse_fast
    if hack_enemy2_active:
        add Solid("#FF9A65", xsize=9, ysize=9) xpos _mini_x + hack_enemy2[0] * _mini_cell + 2 ypos _mini_y + hack_enemy2[1] * _mini_cell + 2 at hk_pulse_fast
    add Solid("#E4FAFF", xsize=9, ysize=9) xpos _mini_x + hack_player[0] * _mini_cell + 2 ypos _mini_y + hack_player[1] * _mini_cell + 2

    # ---------- En-tete ----------
    text hack_title style "hk_h1" size 31 xpos 152 ypos 40
    text hack_channel style "hk_label" size 15 xpos 154 ypos 78

    vbox:
        xalign 0.5
        ypos 28
        spacing 0
        text "[hack_time_left:04.1f]" style "hk_h1" size 58 color ("#FF5968" if _low_time else "#F4FBFF") xalign 0.5
        text "SECONDES RESTANTES" style "hk_label" size 14 xalign 0.5

    vbox:
        xpos 1768 xanchor 1.0 ypos 42 spacing 7
        text "INTERCEPTIONS  [hack_hits] / [hack_max_hits]" style "hk_label" size 19 color "#B8D1DC" xalign 1.0
        hbox:
            spacing 8
            xalign 1.0
            for _hit_index in range(hack_max_hits):
                add Solid("#FF3D5C" if _hit_index < hack_hits else "#173342", xsize=76, ysize=8)

    text "FENETRE D'INTRUSION" style "hk_label" size 14 xpos 152 ypos 100
    text "SEUIL CRITIQUE 12.0 S" style "hk_label" size 14 color ("#FF5968" if _low_time else "#3A5C6E") xpos 1768 ypos 100 xanchor 1.0

    # Barre de temps dynamique
    add Solid("#0A1826", xsize=1620, ysize=16) xpos 150 ypos 122
    add Solid("#16374B", xsize=1620, ysize=1) xpos 150 ypos 122
    add Transform("hk_bar", crop=(0, 0, max(2, int(1024 * _time_ratio)), 24), xysize=(_bar_w, 16)) xpos 150 ypos 122
    add Solid("#FFFFFF", xsize=3, ysize=16) xpos 150 + _bar_w - 3 ypos 122 alpha 0.9
    add Transform("hk_glow_cyan" if not _low_time else "hk_glow_red", xysize=(70, 70), xanchor=0.5, yanchor=0.5) xpos 150 + _bar_w ypos 130 alpha 0.5
    for _seg in range(1, 12):
        add Solid("#02060B", xsize=2, ysize=16) xpos 150 + int(1620 * _seg / 12.0) ypos 122 alpha 0.75

    # ---------- Bandeau bas ----------
    frame:
        xpos 150 ypos 926 xsize 396 ysize 88
        background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
        padding (22, 14)
        vbox:
            spacing 7
            hbox:
                spacing 12
                text "ESPACE" style "hk_h2" size 20 color "#E4FAFF" yalign 0.5
                text ("PROPULSION PRETE" if hack_dash_cooldown <= 0.0 else "RECHARGE [hack_dash_cooldown:0.1f] S") style "hk_label" size 16 color ("#4AE3FF" if hack_dash_cooldown <= 0.0 else "#5C8296") yalign 0.5
            fixed:
                xysize (348, 6)
                add Solid("#122C3C", xsize=348, ysize=6)
                add Solid("#35DFFF" if hack_dash_cooldown <= 0.0 else "#1F7FA0", xsize=max(2, int(348 * _dash_ratio)), ysize=6)

    frame:
        xalign 0.5 ypos 926 xsize 800 ysize 88
        background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
        padding (24, 12)
        vbox:
            xfill True spacing 3
            text hack_status style "hk_h2" xalign 0.5 size 23 color hack_status_color
            for _stamp, _entry, _color in reversed(hack_logbook[-2:]):
                text "[_stamp]  ·  [_entry]" style "hk_label" size 14 color _color xalign 0.5

    frame:
        xpos 1374 ypos 926 xsize 396 ysize 88
        background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
        padding (22, 14)
        vbox:
            spacing 6
            hbox:
                spacing 14
                vbox:
                    spacing 1
                    text "NIVEAU DE MENACE" style "hk_label" size 14
                    text _threat_text style "hk_h2" size 21 color _threat_color
                text ("PORTEE [_enemy_distance]" if _enemy_distance < 99 else "HORS CHAMP") style "hk_label" size 16 color _threat_color yalign 1.0
            hbox:
                spacing 5
                for _lvl in range(5):
                    add Solid(_threat_color if _lvl < _threat_level else "#173342", xsize=66, ysize=5)

    text "ZQSD / FLECHES  DEPLACER     ·     CLIC  ROUTE OU PROPULSION     ·     ESPACE  PROPULSION" style "hk_label" size 14 color "#3A5C6E" xpos 152 ypos 1024
    text "ECHAP  PAUSE" style "hk_label" size 14 color "#5C8296" xpos 1768 ypos 1024 xanchor 1.0

    # ---------- Surcouches ----------
    if hack_player_stun > 0.0 and not hack_done:
        frame:
            xalign 0.5 ypos 476
            background Frame("minijeu/hack/assets/hk_panel_red.png", 34, 34)
            padding (34, 16)
            text "SIGNAL BLOQUE  //  [hack_player_stun:0.1f] S" style "hk_h2" size 30 color "#FFB1A8"

    if (hack_enemy_stun > 0.0 or (hack_enemy2_active and hack_enemy2_stun > 0.0)) and not hack_done:
        frame:
            xalign 0.5 ypos 200
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (28, 12)
            text ("SENTINELLES PERTURBEES" if hack_enemy2_active else "SENTINELLE HORS LIGNE  //  %.1f S" % hack_enemy_stun) style "hk_h2" size 23 color "#FFA53D"

    if hack_sign_time > 0.0 and hack_sign_message:
        frame:
            xalign 0.5 ypos 200 xmaximum 860
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (30, 16)
            hbox:
                spacing 16
                add Transform("hk_beacon", xysize=(48, 48)) yalign 0.5
                text hack_sign_message style "hk_h2" size 22 color "#FFE9C4" yalign 0.5

    if hack_password_active:
        add Solid("#01020ADD")
        $ _pw_ratio = max(0.0, min(1.0, hack_password_time / max(0.001, hack_password_total)))
        frame:
            xalign 0.5 yalign 0.5
            xsize 860 ysize 440
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (46, 34)
            vbox:
                xfill True spacing 18
                text "PARE-FEU  //  CLE D'IMPULSION" style "hk_h1" xalign 0.5 size 38 color "#CF8CFF"
                text "Reproduisez la séquence avant expiration. Le module s'ouvrira aussi pour la sentinelle." style "hk_body" xalign 0.5 text_align 0.5 size 20 color "#DCCEEE" xmaximum 680
                hbox:
                    xalign 0.5
                    spacing 16
                    for _idx, _key in enumerate(hack_password_sequence):
                        frame:
                            xsize 96 ysize 96
                            padding (0, 0)
                            background Solid("#2A1046" if _idx > hack_password_progress else ("#0E3B2E" if _idx < hack_password_progress else "#4A1E7A"))
                            text _key.upper() style "hk_h1" size 46 xalign 0.5 yalign 0.5 color ("#5CFFC0" if _idx < hack_password_progress else ("#FFFFFF" if _idx == hack_password_progress else "#7A5C9E"))
                fixed:
                    xysize (768, 8)
                    add Solid("#2A1046", xsize=768, ysize=8)
                    add Solid("#CF8CFF", xsize=max(2, int(768 * _pw_ratio)), ysize=8)
                text "IMPULSION [min(hack_password_progress + 1, len(hack_password_sequence))] / [len(hack_password_sequence)]     ·     [hack_password_time:0.1f] S" style "hk_label" xalign 0.5 size 21 color "#CF8CFF"

    if hack_paused:
        add Solid("#010409DD")
        frame:
            xalign 0.5 yalign 0.5
            xsize 660 ysize 340
            background Frame("minijeu/hack/assets/hk_panel.png", 34, 34)
            padding (46, 36)
            vbox:
                xfill True spacing 22
                text "INTRUSION SUSPENDUE" style "hk_h1" size 40 xalign 0.5
                text "Le chronomètre et la sentinelle sont en pause." style "hk_body" size 21 xalign 0.5
                textbutton "REPRENDRE":
                    style "hk_button"
                    xalign 0.5 xsize 380 ysize 66
                    action Function(hack_toggle_pause)

    if hack_done and hack_success:
        add Solid("#02100BCC")
        vbox:
            xalign 0.5 yalign 0.5
            spacing 10
            text "ACCES AUTORISE" style "hk_h1" size 76 color "#5CFFC0" xalign 0.5
            text "NOYAU DU CANON COMPROMIS" style "hk_label" size 24 color "#9CFFE0" xalign 0.5

    # ---------- Habillage ----------
    add "hk_scanlines" alpha 0.5
    add Tile("hk_grain") alpha 0.35 at hk_grain_drift
    add Solid("#36DBFF10", xsize=1920, ysize=20) at hk_scan_sweep
    add "hk_vignette"
    add "hk_bezel"

    if hack_flash > 0.0:
        add Solid(hack_flash_color) alpha min(0.34, hack_flash)

    timer HACK_TICK action Function(hack_tick) repeat True
    timer 0.10 action If(hack_done and hack_end_delay <= 0.0, true=Return(hack_success), false=NullAction()) repeat True

    key "K_ESCAPE" action Function(hack_toggle_pause)

    if hack_password_active:
        key "K_z" action Function(hack_password_press, "z")
        key "K_q" action Function(hack_password_press, "q")
        key "K_s" action Function(hack_password_press, "s")
        key "K_d" action Function(hack_password_press, "d")
    elif not hack_paused:
        key "K_SPACE" action Function(hack_try_dash)
        key "K_z" action Function(hack_try_move, 0, -1)
        key "K_UP" action Function(hack_try_move, 0, -1)
        key "K_s" action Function(hack_try_move, 0, 1)
        key "K_DOWN" action Function(hack_try_move, 0, 1)
        key "K_q" action Function(hack_try_move, -1, 0)
        key "K_LEFT" action Function(hack_try_move, -1, 0)
        key "K_d" action Function(hack_try_move, 1, 0)
        key "K_RIGHT" action Function(hack_try_move, 1, 0)


# ------------------------------------------------------------
# Echec
# ------------------------------------------------------------
screen j901_hack_retry():
    modal True
    zorder 510

    add Solid("#02060B")
    add Tile("hk_hexfield") alpha 0.35
    add Solid("#25060C") alpha 0.30
    add Solid("#FF3B5218", xsize=1920, ysize=20) at hk_scan_sweep

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        padding (58, 46)
        background Frame("minijeu/hack/assets/hk_panel_red.png", 34, 34)

        vbox:
            xfill True
            spacing 22
            text "SIGNAL ROMPU" style "hk_h1" xalign 0.5 size 54 color "#FF5968"
            text ("LIMITE D'INTERCEPTIONS ATTEINTE" if hack_hits >= hack_max_hits else "FENETRE D'INTRUSION EXPIREE") style "hk_label" xalign 0.5 size 21 color "#FF9AA3"
            add Solid("#FF3B5266") xsize 880 ysize 2

            hbox:
                xalign 0.5 spacing 84
                vbox:
                    spacing 3
                    text "TEMPS RESIDUEL" style "hk_label" size 15 xalign 0.5
                    text "[hack_time_left:04.1f] S" style "hk_value" size 32 xalign 0.5
                vbox:
                    spacing 3
                    text "INTERCEPTIONS" style "hk_label" size 15 xalign 0.5
                    text "[hack_hits] / [hack_max_hits]" style "hk_value" size 32 color "#FF6577" xalign 0.5
                vbox:
                    spacing 3
                    text "DISTANCE NOYAU" style "hk_label" size 15 xalign 0.5
                    text ("[hack_goal_distance()] CASES" if hack_goal_distance() < 99 else "HORS ROUTE") style "hk_value" size 32 color "#4AE3FF" xalign 0.5

            text "La topologie du réseau reste stable. Changez de route, forcez un pare-feu, ou attirez la sentinelle sur un piège." style "hk_body" xalign 0.5 text_align 0.5 size 21 xmaximum 820

            textbutton "REESSAYER":
                style "hk_button"
                xalign 0.5
                xsize 430
                ysize 68
                action Return("retry")

            textbutton "ACTIVER L'ASSISTANCE":
                style "hk_button"
                xalign 0.5
                xsize 430
                ysize 60
                action Return("assist")

            text "+20 secondes  //  sentinelle ralentie" style "hk_label" size 15 xalign 0.5

    add "hk_scanlines" alpha 0.5
    add "hk_vignette"
    add "hk_bezel"


label j901_play_hack:
    $ hack_assist = False
    $ hack_reset(J901_HACK_CIRCUIT, assist=False)
    call screen j901_hack_howto
    $ hack_ambient_start()

label j901_hack_retry_loop:
    $ hack_reset(J901_HACK_CIRCUIT, assist=hack_assist)
    call screen j901_hack_screen
    $ j901_hack_success = bool(_return)

    if not j901_hack_success:
        call screen j901_hack_retry
        if _return == "assist":
            $ hack_assist = True
        jump j901_hack_retry_loop

    $ hack_ambient_stop()
    return True


label j710_play_hack_bonus:
    $ hack_assist = False
    $ hack_reset(J710_HACK_CIRCUIT, assist=False)
    call screen j901_hack_howto
    $ hack_ambient_start()

label j710_hack_retry_loop:
    $ hack_reset(J710_HACK_CIRCUIT, assist=hack_assist)
    call screen j901_hack_screen
    $ j710_hack_success = bool(_return)

    if not j710_hack_success:
        call screen j901_hack_retry
        if _return == "assist":
            $ hack_assist = True
        jump j710_hack_retry_loop

    $ hack_ambient_stop()
    return True
