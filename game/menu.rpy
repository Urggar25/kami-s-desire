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

    _cg_pattern = re.compile(r"^images/background/(?:cg/)?(bg_cg\d+)(?:_(\d+))?\.(png|jpg|jpeg|webp|mp4|webm|avi)$")
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
                catalog[base_name] = {}

            # Les CG historiques peuvent exister à la racine et dans
            # background/cg/. En cas de doublon, le dossier canonique prime.
            previous = catalog[base_name].get(order)
            if previous is None or "/cg/" in path:
                catalog[base_name][order] = path

        ordered = []
        for base_name in sorted(catalog.keys()):
            sprites = [p for _, p in sorted(catalog[base_name].items(), key=lambda item: item[0])]
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
    ysize 62
    xalign 0.5
    padding (38, 12, 18, 12)

style kami_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 26
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

style version_trailer_button is button:
    background Solid("#06111BD9")
    hover_background Solid("#123247F2")
    xsize 206
    ysize 52
    padding (16, 10, 16, 10)

style version_trailer_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 20
    color "#6FA5BE"
    hover_color "#E4F7FF"
    xalign 0.5
    yalign 0.5
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
        ypos 252
        xsize 520
        ysize 772
        background Frame("gui/main_menu_kami/panel.png", 32, 32)
        padding (30, 50, 30, 50)
        at kami_menu_in

        vbox:
            spacing 9
            xalign 0.5
            yalign 0.5

            if main_menu:
                textbutton _("Nouvelle partie") style "kami_button" action Start()
            else:
                textbutton _("Reprendre") style "kami_button" action Return()

            textbutton _("Charger")     style "kami_button" action ShowMenu("load")
            textbutton _("Roadmap")     style "kami_button" action ShowMenu("roadmap_menu")
            textbutton _("Contenu bonus") style "kami_button" action ShowMenu("bonus_content_menu")
            textbutton _("Codex")       style "kami_button" action ShowMenu("codex_menu")
            textbutton _("Boutique")    style "kami_button" action ShowMenu("kami_shop_menu")
            textbutton _("Évènement")   style "kami_button" action ShowMenu("kami_event_menu")
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

    # Accès direct à la bande-annonce de la version courante.
    # Start() lance une cinématique autonome et préserve les sauvegardes.
    textbutton "TRAILER 3.0  ▶":
        style "version_trailer_button"
        xpos 1870
        ypos 1000
        xanchor 1.0
        yanchor 1.0
        action [
            SetField(persistent, "trl_skip_splash", True),
            Start("version_3_0_trailer"),
        ]

    # Raccourci clavier rapide
    key "K_ESCAPE" action NullAction()


# ------------------------------------------------------------
# Galerie CG
# - 12 images par page (4 x 3)
# - unlock_gallery_image("bg_cg001") débloque aussi bg_cg001_1, _2, etc.
# ------------------------------------------------------------
screen gallery_menu_legacy():

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


# ============================================================
# BONUS CONTENT — HUD orbital
# ============================================================

style bonus_heading:
    font "fonts/Barlow-Light.ttf"
    size 54
    color "#F4F7FB"
    outlines [(2, "#03070D", 0, 0)]
    kerning 5.0

style bonus_breadcrumb:
    font "fonts/Barlow-Light.ttf"
    size 17
    color "#9AA8B8"
    kerning 1.5

style bonus_label:
    font "fonts/Barlow-Light.ttf"
    size 22
    color "#DDE5EE"
    kerning 1.0

style bonus_small:
    font "fonts/Barlow-Light.ttf"
    size 17
    color "#8997A8"

style bonus_footer_button is button:
    background None
    hover_background Solid("#67D5FF16")
    padding (14, 7, 14, 7)

style bonus_footer_button_text is button_text:
    font "fonts/Barlow-Light.ttf"
    size 20
    color "#DDE5EE"
    hover_color "#8BE1FF"
    kerning 1.0

style bonus_filter_button is button:
    background Solid("#070C13CC")
    hover_background Solid("#172534EE")
    selected_background Solid("#23394CDD")
    xfill True
    ysize 48
    padding (18, 8, 12, 8)

style bonus_filter_button_text is button_text:
    font "fonts/Barlow-Light.ttf"
    size 18
    color "#9CA9B8"
    hover_color "#F4F7FB"
    selected_color "#F4F7FB"


screen bonus_orbit_background():
    add Solid("#02050A")
    add "gui/main_menu_kami/bg_orbit.png" at cover_screen
    add Solid("#02050A99")
    add "gui/main_menu_kami/scanlines.png" alpha 0.18
    add "gui/main_menu_kami/vignette.png" alpha 0.92
    add Solid("#E83B4A", xsize=4, ysize=104) xpos 58 ypos 52
    add Solid("#E83B4A55", xsize=1, ysize=104) xpos 48 ypos 52


screen bonus_header(title, section=None):
    if section:
        text _("CONTENU BONUS  /  [section]") style "bonus_breadcrumb" xpos 84 ypos 48
    else:
        text _("CONTENU BONUS") style "bonus_breadcrumb" xpos 84 ypos 48
    text title style "bonus_heading" xpos 82 ypos 76
    add Solid("#D7E0E966", xsize=570, ysize=1) xpos 84 ypos 150
    text "+" xpos 332 ypos 137 size 20 color "#B9C7D4" font "fonts/Barlow-Light.ttf"


screen bonus_footer(back_action):
    add Solid("#C7D2DD55", xsize=1920, ysize=1) ypos 1010
    hbox:
        xalign 0.5
        ypos 1022
        spacing 60
        textbutton _("ENTRÉE : CONFIRMER") style "bonus_footer_button" action NullAction()
        textbutton _("ÉCHAP : RETOUR") style "bonus_footer_button" action back_action


screen bonus_content_menu():
    tag menu
    zorder 200
    modal True
    use bonus_orbit_background
    use bonus_header(_("CONTENU BONUS"))
    key "game_menu" action Return()

    hbox:
        xpos 112
        ypos 284
        spacing 44
        button:
            xysize (826, 410)
            background Fixed(Solid("#07101AE8"), Solid("#91DBFF88", xsize=2), Solid("#91DBFF88", ysize=2))
            hover_background Fixed(Solid("#0B1723F2"), Solid("#BDEBFFFF", xsize=4), Solid("#BDEBFFFF", ysize=4))
            action ShowMenu("gallery_menu")
            fixed:
                xfill True
                yfill True
                grid 3 2:
                    xpos 52
                    ypos 48
                    spacing 7
                    for catalog_index in range(6):
                        if catalog_index < len(GALLERY_CG_CATALOG):
                            $ bonus_preview = gallery_preview(GALLERY_CG_CATALOG[catalog_index][1])
                            if bonus_preview:
                                add Transform(bonus_preview, fit="cover", xsize=210, ysize=116) alpha 0.70
                            else:
                                add Solid("#101923", xsize=210, ysize=116)
                        else:
                            add Solid("#101923", xsize=210, ysize=116)
                text _("GALERIE D'IMAGES") style "bonus_heading" size 35 xalign 0.5 ypos 322

        button:
            xysize (826, 410)
            background Fixed(Solid("#07101AE8"), Solid("#91DBFF55", xsize=2), Solid("#91DBFF55", ysize=2))
            hover_background Fixed(Solid("#0B1723F2"), Solid("#BDEBFFFF", xsize=4), Solid("#BDEBFFFF", ysize=4))
            action ShowMenu("scene_select_menu")
            fixed:
                xfill True
                yfill True
                text ">" xalign 0.22 ypos 98 size 96 color "#EAF8FF" font "fonts/Barlow-Light.ttf"
                vbox:
                    xpos 320
                    ypos 72
                    spacing 18
                    for line_index in range(3):
                        hbox:
                            spacing 12
                            add Solid("#344353", xsize=120, ysize=34)
                            add Solid("#24313E", xsize=120, ysize=34)
                text _("SÉLECTION DE SCÈNES") style "bonus_heading" size 35 xalign 0.5 ypos 322

    use bonus_footer(Return())


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
    $ page_items = active_catalog[gallery_page * page_size:min((gallery_page + 1) * page_size, total_items)]
    $ unlocked_count = len([item for item in active_catalog if gallery_is_unlocked(item[0])])

    if selected_base:
        $ variants = gallery_variants(selected_base, gallery_section)
        $ current_variant = variants[selected_variant_index] if variants else None
        add Solid("#000")
        if current_variant:
            add gallery_displayable(current_variant) at adaptive_fullscreen
        add Solid("#00000055", ysize=82) ypos 0
        text _("VARIANTE [selected_variant_index + 1] / [len(variants)]") style "bonus_label" xalign 0.5 ypos 24
        textbutton _("ÉCHAP : RETOUR") style "bonus_footer_button" xpos 34 ypos 20 action SetScreenVariable("selected_base", None)
        if len(variants) > 1:
            key "K_RIGHT" action SetScreenVariable("selected_variant_index", (selected_variant_index + 1) % len(variants))
            key "K_LEFT" action SetScreenVariable("selected_variant_index", (selected_variant_index - 1) % len(variants))
            button:
                background None
                xfill True
                ypos 82
                ysize 998
                action SetScreenVariable("selected_variant_index", (selected_variant_index + 1) % len(variants))
        key "game_menu" action SetScreenVariable("selected_base", None)
    else:
        use bonus_orbit_background
        use bonus_header(_("GALERIE D'IMAGES"), _("GALERIE D'IMAGES"))
        key "game_menu" action ShowMenu("bonus_content_menu")
        hbox:
            xpos 1220
            ypos 76
            spacing 12
            textbutton _("CG") style "bonus_filter_button" xsize 120 selected gallery_section == "cg" action [SetScreenVariable("gallery_section", "cg"), SetScreenVariable("gallery_page", 0)]
            textbutton _("SPORT") style "bonus_filter_button" xsize 120 selected gallery_section == "sport" action [SetScreenVariable("gallery_section", "sport"), SetScreenVariable("gallery_page", 0)]
        grid 4 3:
            xpos 92
            ypos 184
            spacing 18
            for gallery_index in range(page_size):
                if gallery_index < len(page_items):
                    $ base_name, sprites = page_items[gallery_index]
                    $ preview = gallery_preview(sprites)
                    $ is_unlocked = gallery_is_unlocked(base_name)
                    button:
                        xysize (417, 205)
                        background Fixed(Solid("#07101AE8"), Solid("#8A9BAA77", xsize=2), Solid("#8A9BAA77", ysize=2))
                        hover_background Fixed(Solid("#0D1924F2"), Solid("#B9ECFFFF", xsize=4), Solid("#B9ECFFFF", ysize=4))
                        sensitive is_unlocked and preview is not None
                        action [SetScreenVariable("selected_base", base_name), SetScreenVariable("selected_variant_index", 0)]
                        if preview:
                            add Transform(preview, fit="cover", xsize=405, ysize=193) xpos 6 ypos 6 alpha (1.0 if is_unlocked else 0.18)
                        if not is_unlocked:
                            add Solid("#03070BAA")
                            text "X" xalign 0.5 yalign 0.5 text_align 0.5 size 42 color "#A9B4BF" font "fonts/Barlow-Light.ttf"
                else:
                    null width 417 height 205
        hbox:
            xalign 0.5
            ypos 848
            spacing 28
            textbutton "<" style "bonus_footer_button" text_size 38 sensitive gallery_page > 0 action SetScreenVariable("gallery_page", max(0, gallery_page - 1))
            text _("PAGE [gallery_page + 1] / [total_pages]") style "bonus_label" yalign 0.5
            textbutton ">" style "bonus_footer_button" text_size 38 sensitive gallery_page < total_pages - 1 action SetScreenVariable("gallery_page", min(total_pages - 1, gallery_page + 1))
        text _("[unlocked_count] / [total_items] DÉBLOQUÉES") style "bonus_label" xpos 1810 ypos 870 xanchor 1.0
        use bonus_footer(ShowMenu("bonus_content_menu"))


screen scene_select_menu():
    tag menu
    zorder 200
    modal True
    default scene_page = 0
    default scene_filter = "all"
    default selected_scene_id = None
    $ all_scenes = all_free_time_scenes()
    $ filtered_scenes = all_scenes if scene_filter == "all" else list(FREE_TIME_SCENES.get(scene_filter, []))
    $ page_size = 6
    $ total_pages = max(1, (len(filtered_scenes) + page_size - 1) // page_size)
    $ scene_page = min(scene_page, total_pages - 1)
    $ page_scenes = filtered_scenes[scene_page * page_size:min((scene_page + 1) * page_size, len(filtered_scenes))]
    $ selected_scene = free_time_scene(selected_scene_id) if selected_scene_id else (page_scenes[0] if page_scenes else None)
    $ selected_unlocked = selected_scene is not None and free_time_scene_unlocked(selected_scene["id"])
    $ total_unlocked = free_time_unlocked_count()
    use bonus_orbit_background
    use bonus_header(_("SÉLECTION DE SCÈNES"), _("SÉLECTION DE SCÈNES"))
    key "game_menu" action ShowMenu("bonus_content_menu")

    frame:
        xpos 58
        ypos 176
        xysize (286, 640)
        padding (2, 2)
        background Fixed(Solid("#050A10E8"), Solid("#8494A455", xsize=2), Solid("#8494A455", ysize=2))
        vbox:
            spacing 2
            text _("PERSONNAGE") style "bonus_label" xalign 0.5 ysize 52
            textbutton _("TOUS") style "bonus_filter_button" selected scene_filter == "all" action [SetScreenVariable("scene_filter", "all"), SetScreenVariable("scene_page", 0), SetScreenVariable("selected_scene_id", None)]
            viewport:
                ysize 570
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 2
                    for character_id in CHARACTER_LINK_IDS:
                        textbutton CHARACTER_REAL_NAMES.get(character_id, character_id.title()).upper() style "bonus_filter_button":
                            selected scene_filter == character_id
                            action [SetScreenVariable("scene_filter", character_id), SetScreenVariable("scene_page", 0), SetScreenVariable("selected_scene_id", None)]

    frame:
        xpos 366
        ypos 176
        xysize (728, 640)
        padding (16, 54, 16, 12)
        background Fixed(Solid("#050A10E8"), Solid("#8494A455", xsize=2), Solid("#8494A455", ysize=2))
        text _("SCÈNES BONUS") style "bonus_label" xalign 0.5 ypos 12
        vbox:
            spacing 9
            for row_index in range(page_size):
                if row_index < len(page_scenes):
                    $ scene = page_scenes[row_index]
                    $ scene_unlocked = free_time_scene_unlocked(scene["id"])
                    button:
                        xfill True
                        ysize 82
                        background Solid("#07101AE8")
                        hover_background Solid("#173044EE")
                        selected_background Solid("#1C3D52EE")
                        selected selected_scene is not None and selected_scene["id"] == scene["id"]
                        action SetScreenVariable("selected_scene_id", scene["id"])
                        text "[scene_page * page_size + row_index + 1:02d]" style "bonus_label" xpos 18 yalign 0.5 color ("#DDE5EE" if scene_unlocked else "#626E7B")
                        if scene_unlocked:
                            add Transform(scene["preview"], fit="cover", xsize=176, ysize=68) xpos 72 ypos 7
                            text scene["title"].upper() style "bonus_label" xpos 278 yalign 0.5 size 18
                            text ">" style "bonus_label" xpos 654 yalign 0.5
                        else:
                            add Solid("#111820", xsize=176, ysize=68) xpos 72 ypos 7
                            text _("VERROUILLÉE") style "bonus_small" xpos 278 yalign 0.5
                            text "X" style "bonus_label" xpos 654 yalign 0.5
                else:
                    null height 82

    frame:
        xpos 1116
        ypos 176
        xysize (496, 640)
        padding (20, 20)
        background Fixed(Solid("#050A10E8"), Solid("#8494A455", xsize=2), Solid("#8494A455", ysize=2))
        if selected_scene:
            add Transform(selected_scene["preview"], fit="cover", xsize=452, ysize=254) xpos 0 ypos 0 alpha (1.0 if selected_unlocked else 0.20)
            if not selected_unlocked:
                text "X" xalign 0.5 ypos 94 size 46 color "#DDE5EE" font "fonts/Barlow-Light.ttf"
            text (selected_scene["title"].upper() if selected_unlocked else _("SCÈNE VERROUILLÉE")) style "bonus_heading" size 27 xalign 0.5 ypos 286
            add Solid("#A5B4C455", xsize=452, ysize=1) ypos 337
            text _("PERSONNAGE") style "bonus_small" xpos 4 ypos 360
            text selected_scene["route"].upper() style "bonus_label" xpos 448 ypos 356 xanchor 1.0 size 18
            text _("STATUT") style "bonus_small" xpos 4 ypos 404
            text (_("DÉBLOQUÉE") if selected_unlocked else _("VERROUILLÉE")) style "bonus_label" xpos 448 ypos 400 xanchor 1.0 size 18
            textbutton _(">  JOUER") style "bonus_footer_button":
                xalign 0.5
                ypos 500
                sensitive selected_unlocked
                action Call("REPLAY_FREE_TIME_SCENE", selected_scene["id"])

    text _("[total_unlocked] / [len(all_scenes)] DÉBLOQUÉES") style "bonus_label" xpos 76 ypos 850
    hbox:
        xalign 0.5
        ypos 838
        spacing 26
        textbutton "<" style "bonus_footer_button" text_size 38 sensitive scene_page > 0 action [SetScreenVariable("scene_page", max(0, scene_page - 1)), SetScreenVariable("selected_scene_id", None)]
        text _("PAGE [scene_page + 1] / [total_pages]") style "bonus_label" yalign 0.5
        textbutton ">" style "bonus_footer_button" text_size 38 sensitive scene_page < total_pages - 1 action [SetScreenVariable("scene_page", min(total_pages - 1, scene_page + 1)), SetScreenVariable("selected_scene_id", None)]
    use bonus_footer(ShowMenu("bonus_content_menu"))
