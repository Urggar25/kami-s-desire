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

    add Solid("#020b19")
    add "images/background/bg_menu.png" at cover_screen

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1760
        ysize 950
        padding (30, 26)
        background Solid("#03152ddd")

        vbox:
            spacing 16

            text "Story Map" xalign 0.5 size 52 color "#7be6ff"
            text "Une case s'affiche seulement après avoir vu son label au moins une fois." xalign 0.5 size 22 color "#b7d8ff"

            hbox:
                xalign 0.5
                spacing 12
                for route in STORY_MAP_ROUTES:
                    textbutton "[route['name']]":
                        background Solid("#17314f")
                        hover_background Solid("#2c5a87")
                        if selected_route_id == route["id"]:
                            background Solid("#36b9ff")
                            hover_background Solid("#5bc8ff")
                        action SetScreenVariable("selected_route_id", route["id"])

            viewport:
                xfill True
                yfill True
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    xfill True
                    spacing 14

                    for node in route_nodes:
                        $ is_visible = _story_node_visible(node)
                        $ is_unlocked = _story_node_unlocked(node, nodes_by_id)
                        $ requirement_text = ", ".join(node.get("requires", [])) if node.get("requires") else "Aucun"

                        if is_visible:
                            button:
                                xfill True
                                ysize 86
                                background Solid("#0f3d66")
                                hover_background Solid("#14639f")
                                action [SetVariable("story_map_target_label", node["label"]), Start()]

                                hbox:
                                    xfill True
                                    yalign 0.5
                                    spacing 14
                                    text "[node['id']]" size 28 color "#66e7ff"
                                    text "[node['title']]" size 30 color "#ffffff"
                                    null width 20
                                    text "Label: [node['label']]" size 20 color "#c6e7ff"
                        elif is_unlocked:
                            frame:
                                xfill True
                                ysize 86
                                background Solid("#21344a")
                                hbox:
                                    yalign 0.5
                                    spacing 14
                                    text "[node['id']]" size 28 color "#94b8d9"
                                    text "[node['title']]" size 30 color "#d4deec"
                                    text "Débloqué (non visité)" size 22 color "#ffd166"
                                    text "Prérequis: [requirement_text]" size 20 color "#a4b8cf"
                        else:
                            frame:
                                xfill True
                                ysize 86
                                background Solid("#141b26")
                                hbox:
                                    yalign 0.5
                                    spacing 14
                                    text "???" size 30 color "#596b83"
                                    text "Prérequis: [requirement_text]" size 20 color "#647a96"

    textbutton "Retour":
        xalign 0.03
        yalign 0.05
        action Return()
