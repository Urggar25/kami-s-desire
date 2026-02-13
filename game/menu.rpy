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

init python:
    import re

    _cg_pattern = re.compile(r"^images/background/(bg_cg\d+)(?:_(\d+))?\.(png|jpg|jpeg|webp)$")

    def _gallery_catalog():
        catalog = {}
        for path in renpy.list_files():
            match = _cg_pattern.match(path)
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

    GALLERY_CG_CATALOG = _gallery_catalog()

    def gallery_variants(base_name):
        for cg_name, sprites in GALLERY_CG_CATALOG:
            if cg_name == base_name:
                return sprites
        return []

    def gallery_is_unlocked(base_name):
        return base_name in persistent.gallery_unlocked_bases

    # Fonction utilitaire demandée : débloque une image + ses variantes _1, _2, etc.
    def unlock_gallery_image(base_name):
        if base_name not in persistent.gallery_unlocked_bases:
            persistent.gallery_unlocked_bases.append(base_name)
            renpy.save_persistent()


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
# - 16 images par page (4 x 4)
# - unlock_gallery_image("bg_cg001") débloque aussi bg_cg001_1, _2, etc.
# ------------------------------------------------------------
screen gallery_menu():

    tag menu
    zorder 200
    modal True

    default gallery_page = 0
    default selected_base = None
    default selected_variant_index = 0

    $ page_size = 16
    $ total_items = len(GALLERY_CG_CATALOG)
    $ total_pages = max(1, (total_items + page_size - 1) // page_size)
    $ gallery_page = min(gallery_page, total_pages - 1)
    $ start = gallery_page * page_size
    $ end = min(start + page_size, total_items)
    $ page_items = GALLERY_CG_CATALOG[start:end]

    add Solid("#000")

    key "game_menu" action [SetScreenVariable("selected_base", None), Return()]
    key "K_ESCAPE" action [SetScreenVariable("selected_base", None), Return()]

    if selected_base:
        $ variants = gallery_variants(selected_base)
        $ current_variant = variants[selected_variant_index] if variants else None

        if current_variant:
            add current_variant at adaptive_fullscreen

        if len(variants) > 1:
            text "Variant [selected_variant_index + 1]/[len(variants)]" xalign 0.5 yalign 0.04 size 28 color "#FFF"

        textbutton "Retour":
            xalign 0.02
            yalign 0.03
            action SetScreenVariable("selected_base", None)

        if current_variant and len(variants) > 1:
            button:
                background Solid("#0000")
                xfill True
                yfill True
                action SetScreenVariable("selected_variant_index", (selected_variant_index + 1) % len(variants))

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

                text "Galerie CG" xalign 0.5 size 42 color "#FFF"
                text "Page [gallery_page + 1]/[total_pages]" xalign 0.5 size 24 color "#DDD"

                grid 4 4:
                    xalign 0.5
                    yalign 0.5
                    spacing 12

                    for idx in range(page_size):
                        if idx < len(page_items):
                            $ base_name, sprites = page_items[idx]
                            $ preview = sprites[0] if sprites else None

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
