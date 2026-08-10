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

    NSFW_GALLERY_BASES = {
        "bg_cg015", "bg_cg016", "bg_cg017",
        "sport006", "sport007", "sport008", "sport009",
    }

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
        if nsfw_content_locked() and base_name in NSFW_GALLERY_BASES:
            return False
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
        if nsfw_content_locked() and base_name in NSFW_GALLERY_BASES:
            return
        if base_name not in persistent.gallery_unlocked_bases:
            persistent.gallery_unlocked_bases.append(base_name)
            renpy.save_persistent()


# ============================================================
# MAIN MENU — KAMI HUD
# ============================================================
# Direction artistique : interface Kami, vue orbitale, ton sacré-froid.
# Tous les assets dédiés vivent dans gui/main_menu_kami/.

# --- Transforms d'ambiance ----------------------------------------------------
transform kami_pulse:
    alpha 0.18
    linear 2.4 alpha 0.32
    linear 2.4 alpha 0.18
    repeat

transform kami_drift:
    # Léger panoramique vertical sans révéler les bords (zoom 1.06).
    zoom 1.06
    xanchor 0.5 yanchor 0.5
    xpos 960 ypos 540
    yoffset 0
    linear 18.0 yoffset -22
    linear 18.0 yoffset 0
    repeat

transform kami_menu_in:
    alpha 0.0
    yoffset 12
    easein 0.6 alpha 1.0 yoffset 0

transform kami_glyph_spin:
    alpha 0.30
    zoom 0.9
    rotate 0
    linear 80.0 rotate 360
    repeat

transform kami_scan:
    alpha 0.25
    yoffset -1080
    linear 7.0 yoffset 1080
    repeat

transform kami_overlay_dim:
    alpha 0.35

transform kami_vignette_dim:
    alpha 0.8

# --- Styles dédiés ------------------------------------------------------------
style kami_button is button:
    background Frame("gui/main_menu_kami/button_idle.png", 14, 14)
    hover_background Frame("gui/main_menu_kami/button_hover.png", 14, 14)
    xsize 460
    ysize 72
    xalign 0.5
    padding (38, 12, 18, 12)

style kami_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 28
    color "#8ab8d0"
    hover_color "#dff2ff"
    insensitive_color "#3a5a72"
    xalign 0.0
    yalign 0.5

style kami_small_button is button:
    background None
    padding (10, 6, 10, 6)
    hover_background Solid("#5cd3ff22")

style kami_small_button_text is button_text:
    font "fonts/Barlow-Light.ttf"
    size 20
    color "#6fa5be"
    hover_color "#dff2ff"

style kami_title_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 88
    color "#dff2ff"
    outlines [(2, "#0a1626", 0, 0)]
    kerning 6.0

style kami_subtitle_text:
    font "fonts/Barlow-Light.ttf"
    size 22
    color "#5cd3ff"
    kerning 8.0

style kami_meta_text:
    font "fonts/Barlow-Light.ttf"
    size 18
    color "#3a7a90"
    kerning 2.0


screen main_menu():
    tag menu
    zorder 200
    modal True

    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=1.5)
    on "hide" action Stop("music", fadeout=1.2)

    # --- Couches de fond -----------------------------------------------------
    add Solid("#04080f")
    add "gui/main_menu_kami/bg_orbit.png" at kami_drift

    # Œil de Kami (présence omnisciente, très tamisé)
    add "gui/main_menu_kami/kami_eye.png":
        xalign 0.5
        yalign 0.5
        at kami_pulse

    # Glyphe Kami décoratif (rotation lente, présence subtile)
    add "gui/main_menu_kami/glyph_kami.png":
        at kami_glyph_spin
        xpos 1700
        ypos 880
        xanchor 0.5
        yanchor 0.5

    # Scanline subtile qui descend
    add "gui/main_menu_kami/scanlines.png" at kami_overlay_dim
    add "gui/main_menu_kami/scanlines.png" at kami_scan

    # Vignette
    add "gui/main_menu_kami/vignette.png" at kami_vignette_dim

    # --- HUD coins -----------------------------------------------------------
    add "gui/main_menu_kami/corner.png" xpos 30 ypos 30
    add Transform("gui/main_menu_kami/corner.png", xzoom=-1) xpos 1770 ypos 30
    add Transform("gui/main_menu_kami/corner.png", yzoom=-1) xpos 30 ypos 950
    add Transform("gui/main_menu_kami/corner.png", xzoom=-1, yzoom=-1) xpos 1770 ypos 950

    # Bandeau supérieur — identifiants Conclave
    text "KAMI.CORE // CONCLAVE ORBITAL — LINK STABLE":
        style "kami_meta_text"
        xpos 80
        ypos 50
    text "[config.version]":
        style "kami_meta_text"
        xpos 1730
        ypos 50
        xanchor 1.0

    # --- Titre ---------------------------------------------------------------
    vbox:
        xalign 0.5
        ypos 80
        spacing 6
        at kami_menu_in

        text "KAMI'S DESIRES" style "kami_title_text" xalign 0.5
        text "— LE CONCLAVE T'ÉCOUTE —" style "kami_subtitle_text" xalign 0.5

    # --- Panneau central des actions principales ------------------------------
    frame:
        xalign 0.5
        ypos 280
        xsize 520
        ysize 740
        background Frame("gui/main_menu_kami/panel.png", 32, 32)
        padding (30, 50, 30, 50)
        at kami_menu_in

        vbox:
            spacing 14
            xalign 0.5
            yalign 0.5

            if main_menu:
                textbutton _("Nouvelle partie") style "kami_button" action Start()
            else:
                textbutton _("Reprendre") style "kami_button" action Return()

            textbutton _("Charger")     style "kami_button" action ShowMenu("load")
            textbutton _("Roadmap")     style "kami_button" action ShowMenu("roadmap_menu")
            textbutton _("Galerie")     style "kami_button" action ShowMenu("gallery_menu")
            textbutton _("Codex")       style "kami_button" action ShowMenu("codex_menu")
            textbutton _("Options")     style "kami_button" action ShowMenu("preferences")

            add "gui/main_menu_kami/divider.png" xalign 0.5 ypos 4

            hbox:
                xalign 0.5
                spacing 18

                textbutton _("PATREON") style "kami_small_button":
                    action Function(renpy.open_url, "https://www.patreon.com/c/Kamidesires")
                textbutton _("CRÉDITS") style "kami_small_button" action ShowMenu("about")
                textbutton _("QUITTER") style "kami_small_button" action Quit(confirm=True)

    # --- Bas de l'écran : signature institutionnelle --------------------------
    text "© CONCLAVE.ORBITAL — COMMANDEMENTS ENREGISTRÉS":
        style "kami_meta_text"
        xalign 0.5
        ypos 1040

    # Raccourci clavier rapide
    key "K_ESCAPE" action NullAction()


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

    key "game_menu" action NullAction()
    key "K_ESCAPE" action NullAction()

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
