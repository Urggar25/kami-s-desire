# ============================================================
# MAIN MENU — Kami's Desires (adaptive_fullscreen + mask)
# ============================================================

# Si tu as déjà adaptive_fullscreen ailleurs, NE REDEFINIS PAS.
# Sinon, garde ceci (exemple classique cover) :
transform adaptive_fullscreen:
    xalign 0.5
    yalign 0.5
    # "cover" : on remplit l'écran sans déformer, on crop si besoin
    zoom max(config.screen_width / float(config.screen_width),
             config.screen_height / float(config.screen_height))

transform fit_fullscreen:
    xalign 0.5
    yalign 0.5
    # Contain : on voit toute l'image, bandes possibles
    zoom min(config.screen_width / float(config.image_width),
             config.screen_height / float(config.image_height))

init python:
    def fit(path):
        # Fit = contain (pas de crop)
        return im.Fit(path, config.screen_width, config.screen_height)

init python:
    def contain_rect(img_w, img_h, scr_w=None, scr_h=None):
        if scr_w is None: scr_w = config.screen_width
        if scr_h is None: scr_h = config.screen_height

        scale = min(scr_w / float(img_w), scr_h / float(img_h))
        w = int(img_w * scale)
        h = int(img_h * scale)
        x = int((scr_w - w) / 2)
        y = int((scr_h - h) / 2)
        return x, y, w, h

    # Place un point (rx, ry) dans le rect contain (rx/ry en 0..1)
    def in_rect(x, y, w, h, rx, ry):
        return int(x + w * rx), int(y + h * ry)

init python:
    def contain_params(img_w, img_h, scr_w=None, scr_h=None):
        if scr_w is None: scr_w = config.screen_width
        if scr_h is None: scr_h = config.screen_height

        scale = min(scr_w / float(img_w), scr_h / float(img_h))
        w = int(img_w * scale)
        h = int(img_h * scale)
        x = int((scr_w - w) / 2)
        y = int((scr_h - h) / 2)
        return x, y, scale



# (Optionnel mais utile) Déclare ton bg comme image
image bg_menu = "images/background/bg_menu.png"

default persistent.gallery_unlocked_bases = []
default story_map_target_label = None

init python:
    import re

    _cg_pattern = re.compile(r"^images/background/(bg_cg\d+)(?:_(\d+))?\.(png|jpg|jpeg|webp|mp4|webm|avi)$")
    _sport_pattern = re.compile(r"^images/background/(sport\d+)(?:_(\d+))?\.(png|jpg|jpeg|webp|mp4|webm|avi)$")

    def _build_gallery_catalog(pattern):
        catalog = {}
        for path in renpy.list_files():
            match = pattern.match(path)
            if not match:
                continue

            base_name = match.group(1)
            suffix = match.group(2)
            order = 0 if suffix is None else int(suffix)

            if base_name not in catalog:
                catalog[base_name] = []
            catalog[base_name].append((order, path))

        ordered = []
        for base_name in sorted(catalog.keys()):
            sprites = [p for _, p in sorted(catalog[base_name], key=lambda item: item[0])]
            ordered.append((base_name, sprites))
        return ordered

    GALLERY_CG_CATALOG = _build_gallery_catalog(_cg_pattern)
    GALLERY_SPORT_CATALOG = _build_gallery_catalog(_sport_pattern)

    def gallery_variants(base_name, section="cg"):
        catalog = GALLERY_CG_CATALOG if section == "cg" else GALLERY_SPORT_CATALOG
        for cg_name, sprites in catalog:
            if cg_name == base_name:
                return sprites
        return []

    def gallery_is_unlocked(base_name):
        return base_name in persistent.gallery_unlocked_bases

    def gallery_displayable(path):
        lowered = path.lower()
        if lowered.endswith((".mp4", ".webm", ".avi")):
            return Movie(
                play=path,
                loop=True,
                size=(config.screen_width, config.screen_height),
            )
        return path

    def gallery_is_video(path):
        return path.lower().endswith((".mp4", ".webm", ".avi"))

    def gallery_preview(sprites):
        for sprite in sprites:
            lowered = sprite.lower()
            if lowered.endswith((".png", ".jpg", ".jpeg", ".webp")):
                return sprite
        return sprites[0] if sprites else None

    # Fonction utilitaire demandée : débloque une image + ses variantes _1, _2, etc.
    def unlock_gallery_image(base_name):
        if base_name not in persistent.gallery_unlocked_bases:
            persistent.gallery_unlocked_bases.append(base_name)
            renpy.save_persistent()

    STORY_MAP_ROUTES = [
        {
            "id": "route_main",
            "name": "Trame principale",
            "nodes": [
                {"id": "D0", "title": "Jour 0", "label": "_0_CANON", "requires": []},
                {"id": "D1", "title": "Jour 1", "label": "_1_CANON", "requires": ["D0"]},
                {"id": "D2", "title": "Jour 2", "label": "_2_CANON", "requires": ["D1"]},
                {"id": "D3", "title": "Jour 3", "label": "_3_CANON", "requires": ["D2"]},
                {"id": "D4A", "title": "Jour 4A", "label": "_4_0_REVEIL_CHAMBRE", "requires": ["D3"]},
                {"id": "D4B", "title": "Jour 4B", "label": "_4_1_REVEIL_CHAMBRE", "requires": ["D3"]},
            ],
        },
        {
            "id": "route_debat",
            "name": "Branche débat",
            "nodes": [
                {"id": "DB1", "title": "Débat P1", "label": "_3_CAFETERIA_DEBAT", "requires": []},
                {"id": "DB2", "title": "Débat P2", "label": "_3_DEBAT1_PHASE2", "requires": ["DB1"]},
                {"id": "DB3", "title": "Débat P3", "label": "_3_DEBAT1_PHASE3", "requires": ["DB2"]},
                {"id": "VOTE", "title": "Vote final", "label": "vote_phase3_final", "requires": ["DB3"]},
            ],
        },
    ]

    def _story_node_seen(node):
        return renpy.seen_label(node["label"])

    def _story_node_visible(node):
        return _story_node_seen(node)

    def _story_node_unlocked(node, nodes_by_id):
        if _story_node_seen(node):
            return True
        for requirement in node.get("requires", []):
            if requirement not in nodes_by_id:
                return False
            if not _story_node_seen(nodes_by_id[requirement]):
                return False
        return True

    def _story_route_layout(route_nodes):
        if not route_nodes:
            return {"nodes": [], "edges": [], "width": 2200, "height": 1200}

        node_w = 270
        node_h = 118
        margin = 180
        step_x = 340
        step_y = 180

        nodes_by_id = {n["id"]: n for n in route_nodes}
        node_index = {n["id"]: idx for idx, n in enumerate(route_nodes)}
        children = {n["id"]: [] for n in route_nodes}
        for n in route_nodes:
            for req in n.get("requires", []):
                if req in children:
                    children[req].append(n["id"])

        depth_memo = {}
        def depth_for(node_id):
            if node_id in depth_memo:
                return depth_memo[node_id]
            node = nodes_by_id[node_id]
            reqs = [r for r in node.get("requires", []) if r in nodes_by_id]
            if not reqs:
                depth_memo[node_id] = 0
            else:
                depth_memo[node_id] = 1 + max(depth_for(r) for r in reqs)
            return depth_memo[node_id]

        depths = {n["id"]: depth_for(n["id"]) for n in route_nodes}
        ordered = sorted(route_nodes, key=lambda n: (depths[n["id"]], node_index[n["id"]]))
        lanes = {}
        occupied = {}
        root_lane = 0
        branch_offsets = [0, -1, 1, -2, 2, -3, 3, -4, 4]

        for node in ordered:
            nid = node["id"]
            depth = depths[nid]
            occupied.setdefault(depth, set())
            reqs = [r for r in node.get("requires", []) if r in lanes]

            if not reqs:
                lane = root_lane
                root_lane += 2
            else:
                main_parent = reqs[0]
                siblings = [s for s in children.get(main_parent, []) if s in nodes_by_id]
                s_idx = siblings.index(nid) if nid in siblings else 0
                offset = branch_offsets[s_idx] if s_idx < len(branch_offsets) else s_idx
                lane = lanes[main_parent] + offset

            while lane in occupied[depth]:
                lane += 1

            lanes[nid] = lane
            occupied[depth].add(lane)

        min_lane = min(lanes.values())
        max_lane = max(lanes.values())
        lane_shift = -min_lane if min_lane < 0 else 0

        positioned_nodes = []
        for node in route_nodes:
            nid = node["id"]
            x = margin + depths[nid] * step_x
            y = margin + (lanes[nid] + lane_shift) * step_y
            positioned_nodes.append({
                "node": node,
                "x": x,
                "y": y,
                "w": node_w,
                "h": node_h,
                "cx": x + int(node_w / 2),
                "cy": y + int(node_h / 2),
            })

        by_id = {p["node"]["id"]: p for p in positioned_nodes}
        edges = []
        for child in positioned_nodes:
            child_node = child["node"]
            for req in child_node.get("requires", []):
                if req not in by_id:
                    continue
                parent = by_id[req]
                mid_x = int((parent["cx"] + child["cx"]) / 2)
                edges.append({
                    "sx": parent["x"] + node_w,
                    "sy": parent["cy"],
                    "mx": mid_x,
                    "ey": child["cy"],
                    "ex": child["x"],
                    "branch": len(children.get(req, [])) > 1,
                })

        max_depth = max(depths.values())
        canvas_w = max(2200, margin * 2 + (max_depth + 1) * step_x + node_w)
        canvas_h = max(1200, margin * 2 + (max_lane - min_lane + 1) * step_y + node_h)

        return {
            "nodes": positioned_nodes,
            "edges": edges,
            "width": canvas_w,
            "height": canvas_h,
        }


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
# ------------------------------------------------------------
# MAIN MENU (format PNC : full-screen buttons + cover_screen)
# ------------------------------------------------------------
screen main_menu():

    # menu Ren'Py
    tag menu
    zorder 200
    modal True

    on "show" action Play("music", audio.main_menu, fadein=1.0)
    on "hide" action Stop("music", fadeout=1.0)

    add Solid("#000")

    # Fond menu
    add "images/background/bg_menu.png" at cover_screen

    # NEW GAME
    imagebutton:
        idle "images/background/interact/menu/new_game.png"
        hover "images/background/interact/menu/new_game_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Start()

    # LOAD GAME
    imagebutton:
        idle "images/background/interact/menu/load_game.png"
        hover "images/background/interact/menu/load_game_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("load")

    # OPTIONS
    imagebutton:
        idle "images/background/interact/menu/option.png"
        hover "images/background/interact/menu/option_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("preferences")

    # GALLERY
    imagebutton:
        idle "images/background/interact/menu/gallery.png"
        hover "images/background/interact/menu/gallery_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("gallery_menu")

    # STORY MAP
    imagebutton:
        idle "images/background/interact/menu/story_map.png"
        hover "images/background/interact/menu/story_map_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("story_map_menu")

    # CODEX
    textbutton "Codex":
        xalign 0.97
        yalign 0.05
        action ShowMenu("codex_menu")

    # PATREON
    imagebutton:
        idle "images/background/interact/menu/patreon.png"
        hover "images/background/interact/menu/patreon_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Function(renpy.open_url, "https://www.patreon.com/c/Kamidesires")

    # QUIT
    imagebutton:
        idle "images/background/interact/menu/quit.png"
        hover "images/background/interact/menu/quit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Quit(confirm=True)


# ------------------------------------------------------------
# Galerie CG
# - 12 images par page (4 x 3)
# - unlock_gallery_image("bg_cg001") débloque aussi bg_cg001_1, _2, etc.
# ------------------------------------------------------------
screen gallery_menu():

    tag menu
    zorder 200
    modal True

    default gallery_page = 0
    default selected_base = None
    default selected_variant_index = 0
    default gallery_section = "cg"

    $ page_size = 12
    $ active_catalog = GALLERY_CG_CATALOG if gallery_section == "cg" else GALLERY_SPORT_CATALOG
    $ total_items = len(active_catalog)
    $ total_pages = max(1, (total_items + page_size - 1) // page_size)
    $ gallery_page = min(gallery_page, total_pages - 1)
    $ start = gallery_page * page_size
    $ end = min(start + page_size, total_items)
    $ page_items = active_catalog[start:end]

    add Solid("#000")

    key "game_menu" action [SetScreenVariable("selected_base", None), Return()]
    key "K_ESCAPE" action [SetScreenVariable("selected_base", None), Return()]

    if selected_base:
        $ variants = gallery_variants(selected_base, gallery_section)
        $ current_variant = variants[selected_variant_index] if variants else None

        if current_variant:
            if gallery_is_video(current_variant):
                add gallery_displayable(current_variant)
            else:
                add gallery_displayable(current_variant) at adaptive_fullscreen

        if len(variants) > 1:
            text "Variant [selected_variant_index + 1]/[len(variants)]" xalign 0.5 yalign 0.04 size 28 color "#FFF"

        if current_variant and len(variants) > 1:
            button:
                background Solid("#0000")
                xfill True
                yfill True
                action SetScreenVariable("selected_variant_index", (selected_variant_index + 1) % len(variants))

        textbutton "Retour":
            xalign 0.02
            yalign 0.03
            action SetScreenVariable("selected_base", None)

        if current_variant and len(variants) > 1:
            text "Cliquez sur l'image pour passer au sprite suivant" xalign 0.5 yalign 0.96 size 24 color "#FFF"

    else:
        add "images/background/bg_menu.png" at cover_screen

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1700
            ysize 900
            padding (30, 25)
            background Solid("#000a")

            vbox:
                spacing 18

                text "Galerie" xalign 0.5 size 42 color "#FFF"

                hbox:
                    spacing 12
                    xalign 0.5

                    textbutton "CG":
                        background Solid("#2f2f2f")
                        hover_background Solid("#4a4a4a")
                        if gallery_section == "cg":
                            background Solid("#be9c36")
                            hover_background Solid("#d8b44f")
                        action [SetScreenVariable("gallery_section", "cg"), SetScreenVariable("gallery_page", 0)]

                    textbutton "Sport":
                        background Solid("#2f2f2f")
                        hover_background Solid("#4a4a4a")
                        if gallery_section == "sport":
                            background Solid("#be9c36")
                            hover_background Solid("#d8b44f")
                        action [SetScreenVariable("gallery_section", "sport"), SetScreenVariable("gallery_page", 0)]

                text "Page [gallery_page + 1]/[total_pages]" xalign 0.5 size 24 color "#DDD"

                grid 4 3:
                    xalign 0.5
                    yalign 0.5
                    spacing 12

                    for idx in range(page_size):
                        if idx < len(page_items):
                            $ base_name, sprites = page_items[idx]
                            $ preview = gallery_preview(sprites)

                            if gallery_is_unlocked(base_name) and preview:
                                imagebutton:
                                    idle Transform(preview, size=(380, 200))
                                    hover Transform(preview, size=(380, 200), alpha=0.9)
                                    action [
                                        SetScreenVariable("selected_base", base_name),
                                        SetScreenVariable("selected_variant_index", 0),
                                    ]
                            else:
                                button:
                                    xsize 380
                                    ysize 200
                                    background Solid("#111")
                                    text "???" xalign 0.5 yalign 0.5 size 42 color "#777"
                                    action NullAction()
                        else:
                            null width 380 height 200

                hbox:
                    xalign 0.5
                    spacing 16

                    textbutton "← Précédent":
                        sensitive gallery_page > 0
                        action SetScreenVariable("gallery_page", max(0, gallery_page - 1))

                    textbutton "Retour":
                        action Return()

                    textbutton "Suivant →":
                        sensitive gallery_page < (total_pages - 1)
                        action SetScreenVariable("gallery_page", min(total_pages - 1, gallery_page + 1))


screen story_map_menu():

    tag menu
    zorder 210
    modal True

    default selected_route_id = STORY_MAP_ROUTES[0]["id"] if STORY_MAP_ROUTES else None

    $ current_route = next((r for r in STORY_MAP_ROUTES if r["id"] == selected_route_id), STORY_MAP_ROUTES[0] if STORY_MAP_ROUTES else None)
    $ route_nodes = current_route["nodes"] if current_route else []
    $ nodes_by_id = {node["id"]: node for node in route_nodes}
    $ layout = _story_route_layout(route_nodes)
    $ current_seen = [n for n in route_nodes if _story_node_seen(n)]
    $ current_day_node = current_seen[-1] if current_seen else (route_nodes[0] if route_nodes else None)

    add Solid("#020716")
    add "images/background/bg_menu.png" at cover_screen

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1760
        ysize 950
        padding (26, 22)
        background Solid("#040f22e8")

        vbox:
            spacing 14

            text "STORY MAP // ITERATION FLOW" xalign 0.5 size 44 color "#8ef3ff"
            text "Une case s'affiche seulement après avoir vu son label au moins une fois." xalign 0.5 size 21 color "#a6d3ff"

            hbox:
                xalign 0.5
                spacing 14
                for route in STORY_MAP_ROUTES:
                    textbutton "[route['name']]":
                        xminimum 280
                        yminimum 48
                        background Solid("#0c1c38")
                        hover_background Solid("#173765")
                        if selected_route_id == route["id"]:
                            background Solid("#2ec4ff")
                            hover_background Solid("#68d9ff")
                        action SetScreenVariable("selected_route_id", route["id"])

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                scrollbars "both"

                fixed:
                    xsize layout["width"]
                    ysize layout["height"]

                    for yline in range(0, layout["height"], 80):
                        add Solid("#10477a33") xpos 0 ypos yline xsize layout["width"] ysize 1
                    for xline in range(0, layout["width"], 120):
                        add Solid("#0d8ac733") xpos xline ypos 0 xsize 1 ysize layout["height"]

                    for edge in layout["edges"]:
                        $ edge_color = "#ff8f2e" if edge["branch"] else "#45dfff"
                        add Solid(edge_color) xpos edge["sx"] ypos edge["sy"] xsize max(2, edge["mx"] - edge["sx"]) ysize 3
                        if edge["ey"] >= edge["sy"]:
                            add Solid(edge_color) xpos edge["mx"] ypos edge["sy"] xsize 3 ysize max(2, edge["ey"] - edge["sy"])
                        else:
                            add Solid(edge_color) xpos edge["mx"] ypos edge["ey"] xsize 3 ysize max(2, edge["sy"] - edge["ey"])
                        add Solid(edge_color) xpos edge["mx"] ypos edge["ey"] xsize max(2, edge["ex"] - edge["mx"]) ysize 3

                    if current_day_node:
                        $ current_pos = next((p for p in layout["nodes"] if p["node"]["id"] == current_day_node["id"]), None)
                        if current_pos:
                            add Solid("#35e8ff66") xpos current_pos["cx"]-52 ypos current_pos["cy"]-52 xsize 104 ysize 104
                            add Solid("#35e8ffaa") xpos current_pos["cx"]-4 ypos current_pos["cy"]-4 xsize 8 ysize 8

                    for positioned in layout["nodes"]:
                        $ node = positioned["node"]
                        $ is_visible = _story_node_visible(node)
                        $ is_unlocked = _story_node_unlocked(node, nodes_by_id)
                        $ is_current = current_day_node and (current_day_node["id"] == node["id"])
                        $ node_bg = "#0f3352" if is_visible else ("#2d3b4a" if is_unlocked else "#151d28")
                        $ hover_bg = "#1b4f7a" if is_visible else node_bg
                        $ outline_color = "#ff9a37" if len(node.get("requires", [])) > 1 or node["id"].endswith("B") else "#4ae4ff"

                        if is_visible:
                            button:
                                xpos positioned["x"]
                                ypos positioned["y"]
                                xsize positioned["w"]
                                ysize positioned["h"]
                                background Solid(node_bg)
                                hover_background Solid(hover_bg)
                                action [SetVariable("story_map_target_label", node["label"]), Start()]

                                vbox:
                                    xfill True
                                    yfill True
                                    spacing 4
                                    text "[node['id']]  •  [node['title']]" xalign 0.5 size 24 color "#bff5ff"
                                    text "[node['label']]" xalign 0.5 size 17 color "#fff4d3"
                                    if is_current:
                                        text "CURRENT" xalign 0.5 size 16 color "#35e8ff"
                        else:
                            frame:
                                xpos positioned["x"]
                                ypos positioned["y"]
                                xsize positioned["w"]
                                ysize positioned["h"]
                                background Solid(node_bg)
                                vbox:
                                    xfill True
                                    yfill True
                                    spacing 4
                                    if is_unlocked:
                                        text "[node['id']]  •  [node['title']]" xalign 0.5 size 23 color "#98b7ce"
                                        text "Label non visité" xalign 0.5 size 16 color "#ffd08a"
                                    else:
                                        text "🔒 [node['id']]" xalign 0.5 size 24 color "#6f8398"
                                        text "Données cryptées" xalign 0.5 size 16 color "#5f7388"
                                        text "Prérequis: [', '.join(node.get('requires', [])) if node.get('requires') else 'Aucun']" xalign 0.5 size 14 color "#5f7388"

                        add Solid(outline_color) xpos positioned["x"] ypos positioned["y"] xsize positioned["w"] ysize 2
                        add Solid(outline_color) xpos positioned["x"] ypos positioned["y"] xsize 2 ysize positioned["h"]
                        add Solid(outline_color) xpos positioned["x"] ypos (positioned["y"] + positioned["h"] - 2) xsize positioned["w"] ysize 2
                        add Solid(outline_color) xpos (positioned["x"] + positioned["w"] - 2) ypos positioned["y"] xsize 2 ysize positioned["h"]

    textbutton "Retour":
        xalign 0.03
        yalign 0.05
        action Return()

    textbutton "QUIT GAME":
        xalign 0.5
        yalign 0.97
        background Solid("#1e0a0a")
        hover_background Solid("#4d1313")
        text_color "#ffb3b3"
        action Quit(confirm=True)
