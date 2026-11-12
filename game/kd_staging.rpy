# ============================================================
# kd_staging.rpy — Grammaire de mise en scène « procès »
# (inspirée de Danganronpa / The Hundred Line)
#
# Contient :
#   - le tempo global des transitions (dissolve / fade raccourcis) ;
#   - la couleur signature de chaque personnage (nom, cut-in, panneaux) ;
#   - les balises de texte {k} (mot-clé) et {shout} (cri) ;
#   - les plans de caméra : close_up, release_cam, wide_shot, punch_in, dutch ;
#   - le cut-in d'accusation : call cutin("mara", _("C'EST FAUX !")) ;
#   - les panneaux de réactions simultanées : call reactions([...]) ;
#   - l'ouverture de séance du Conclave : call trial_intro(...).
# Toute évolution doit être répercutée dans MECANIQUES_JEU.md.
# ============================================================


# ------------------------------------------------------------
# Tempo global : les transitions par défaut de Ren'Py (0,5 s et 1 s)
# rendaient chaque changement de plan mou. Les appels `with dissolve` et
# `with fade` existants héritent automatiquement de ces durées.
# ------------------------------------------------------------
define dissolve = Dissolve(0.2)
define fade = Fade(0.15, 0.05, 0.2)


init -1 python:

    # Couleur signature de chaque personnage : nom dans la boîte de dialogue,
    # bande des cut-ins et cadre des panneaux de réaction.
    KD_CHARACTER_COLORS = {
        "noam": "#3ddc97",
        "lysa": "#ff8a3d",
        "mara": "#ffcf5c",
        "julian": "#b9c7d4",
        "iris": "#8fd3ff",
        "elias": "#c98a5a",
        "elen": "#d6f05a",
        "kael": "#9b8cff",
        "nyra": "#ff8fb0",
        "ryn": "#c05cff",
        "sael": "#e0a050",
        "tomas": "#6f9fd8",
        "anya": "#ff5f6d",
        "kami": "#ff2e8a",
        "goumi": "#7fffd4",
    }

    KD_KEYWORD_COLOR = "#ffb84d"
    KD_DANGER_COLOR = "#ff405c"
    KD_TRIAL_ACCENT = "#ff2e55"

    # Centre horizontal et haut du crâne (pixels du PNG source 1024x1536)
    # pour cadrer automatiquement le visage dans les cut-ins et panneaux.
    KD_FACE_BOX = {
        "noam": (522, 153), "lysa": (478, 164), "mara": (500, 109),
        "julian": (515, 146), "iris": (504, 134), "elias": (477, 87),
        "elen": (497, 148), "kael": (435, 112), "nyra": (507, 263),
        "ryn": (438, 195), "sael": (487, 128), "tomas": (502, 131),
        "anya": (515, 40),
    }
    KD_FACE_SOURCE = 460
    KD_SPRITE_SOURCE_SCALE = 0.60
    KD_CAST_ORDER = (
        "noam", "lysa", "mara", "julian", "iris", "elias", "elen",
        "kael", "nyra", "ryn", "sael", "tomas",
    )

    _kd_name_color_cache = {}

    def kd_char_color(tag, default="#5cd3ff"):
        return KD_CHARACTER_COLORS.get(tag, default)

    def kd_display_name(tag):
        try:
            return character_display_name(tag)
        except Exception:
            return tag.capitalize()

    def kd_name_color(who):
        """Couleur signature du locuteur courant (tag d'image, sinon nom unique)."""
        if not who:
            return None
        try:
            speaker_tag = renpy.get_say_image_tag()
        except Exception:
            speaker_tag = None
        if speaker_tag in KD_CHARACTER_COLORS:
            return KD_CHARACTER_COLORS[speaker_tag]
        name = str(who)
        # Les noms masqués (« ??? ») ne doivent pas prendre la couleur
        # d'un personnage précis.
        if not any(ch.isalpha() for ch in name):
            return None
        if name in _kd_name_color_cache:
            return _kd_name_color_cache[name]
        found = None
        for tag, color in KD_CHARACTER_COLORS.items():
            try:
                if character_display_name(tag) == name:
                    found = color
                    break
            except Exception:
                pass
        # Les noms inconnus (« ??? ») peuvent changer : on ne met en cache
        # que les correspondances trouvées.
        if found is not None:
            _kd_name_color_cache[name] = found
        return found

    def _kd_reset_name_cache(*args):
        _kd_name_color_cache.clear()

    config.change_language_callbacks.append(_kd_reset_name_cache)

    def kd_current_expr(tag, fallback="neutre"):
        state = getattr(store, "char_state", {}).get(tag, {})
        expr = state.get("expr") if isinstance(state, dict) else None
        return expr or fallback

    def kd_face(tag, expr=None, size=340):
        """Gros plan carré du visage, avec l'expression demandée."""
        if expr is None:
            expr = kd_current_expr(tag)
        box = KD_FACE_BOX.get(tag)
        image_name = "%s %s" % (tag, expr)
        if box is not None and renpy.has_image(image_name):
            cx, top = box
            src = KD_FACE_SOURCE
            full = Transform(character_image(tag, expr), zoom=1.0 / KD_SPRITE_SOURCE_SCALE)
            return Transform(full, crop=(cx - src // 2, top - 20, src, src), xysize=(size, size))
        portrait = "images/character/%s/portrait.png" % tag
        if renpy.loadable(portrait):
            return Transform(portrait, fit="cover", xysize=(size, size))
        return Solid(kd_char_color(tag), xysize=(size, size))

    def kd_portrait(tag, size=150):
        """Portrait 500x500 léger (bandeaux défilants : évite de composer
        des dizaines de sprites en calques pleine résolution)."""
        portrait = "images/character/%s/portrait.png" % tag
        if renpy.loadable(portrait):
            return Transform(portrait, fit="cover", xysize=(size, size))
        return Solid(kd_char_color(tag), xysize=(size, size))

    # --------------------------------------------------------
    # Balises de texte
    # --------------------------------------------------------
    def _kd_tag_keyword(tag, argument, contents):
        color = argument or KD_KEYWORD_COLOR
        return (
            [(renpy.TEXT_TAG, "color=" + color), (renpy.TEXT_TAG, "b")]
            + contents
            + [(renpy.TEXT_TAG, "/b"), (renpy.TEXT_TAG, "/color")]
        )

    def _kd_tag_shout(tag, argument, contents):
        color = argument or KD_DANGER_COLOR
        return (
            [(renpy.TEXT_TAG, "size=+10"), (renpy.TEXT_TAG, "b"), (renpy.TEXT_TAG, "color=" + color)]
            + contents
            + [(renpy.TEXT_TAG, "/color"), (renpy.TEXT_TAG, "/b"), (renpy.TEXT_TAG, "/size")]
        )

    config.custom_text_tags["k"] = _kd_tag_keyword
    config.custom_text_tags["shout"] = _kd_tag_shout

    renpy.music.register_channel("kd_fx", mixer="sfx", loop=False)


# ------------------------------------------------------------
# Plans de caméra explicites
# ------------------------------------------------------------
default _kd_closeup_tag = None

init python:
    def _kd_apply_focus_styles(tag):
        for c in list(store.char_state.keys()):
            if not renpy.showing(c, layer="master"):
                continue
            restyle_char(c, "focus" if c == tag else "dim")

    def close_up(tag=None, z=None, t=0.0):
        """Gros plan sur le visage d'un personnage (coupe sèche par défaut).

        Le gros plan est relâché automatiquement dès qu'un autre personnage
        parle, ou explicitement avec release_cam().
        """
        if tag is None:
            tag = (store._focus_last_params or {}).get("tag")
        if not tag or not renpy.showing(tag, layer="master"):
            return
        if z is None:
            z = CINEMA_ZOOM_BG * 1.45
        store._cinema_manual_override = True
        store._kd_closeup_tag = tag
        store._focus_last_params = dict(tag=tag)
        cam_move(cam_x_for_edge_safe_char(tag, z), CINEMA_CAM_Y - 0.06, z, t)
        _kd_apply_focus_styles(tag)

    def release_cam(t=None):
        """Rend la main à l'autofocus après un plan manuel."""
        store._cinema_manual_override = False
        store._kd_closeup_tag = None
        store._focus_last_params = dict(tag="__REGROUP__")
        cinematic_reset(t=CINEMA_FOCUS_TIME if t is None else t)

    def wide_shot(t=0.0):
        """Plan d'ensemble immédiat (tous les personnages en pleine lumière)."""
        store._cinema_manual_override = False
        store._kd_closeup_tag = None
        cinematic_reset(t=t)

    def punch_in(amount=0.16, t=0.07):
        """Coup de zoom bref sur le plan courant, pour ponctuer une réplique."""
        x, y, z = cam_current("master")
        cam_apply(x, y, z + amount, t)

    def dutch(angle=-6.0, t=0.18):
        """Plan incliné (malaise, folie, manipulation) jusqu'au prochain recadrage."""
        for ly in ("bgcam", "master"):
            renpy.show_layer_at([_dialogue_camera_base(ly), kd_dutch_tilt(angle, t)], layer=ly)

    def dutch_off():
        cam_restore_current(t=0.0)


transform kd_dutch_tilt(angle=-6.0, t=0.18):
    transform_anchor True
    ease t rotate angle zoom 1.2


# ------------------------------------------------------------
# Cut-in d'accusation
# ------------------------------------------------------------
transform kd_cutin_band(d=0.85):
    xalign 0.5
    yalign 0.5
    rotate -6
    xoffset -2700
    easeout 0.14 xoffset 0
    pause d
    easein 0.12 xoffset 2700

transform kd_cutin_face(d=0.85):
    xoffset 380
    alpha 0.0
    pause 0.06
    easeout 0.16 xoffset 0 alpha 1.0
    linear d xoffset -30
    linear 0.1 alpha 0.0

transform kd_cutin_text(d=0.85):
    alpha 0.0
    zoom 1.6
    pause 0.12
    easeout 0.12 alpha 1.0 zoom 1.0
    pause (d - 0.1)
    linear 0.1 alpha 0.0

transform kd_cutin_dim(d=0.85):
    alpha 0.0
    linear 0.08 alpha 0.55
    pause d
    linear 0.14 alpha 0.0

transform kd_flash_once:
    alpha 0.0
    linear 0.03 alpha 0.7
    easeout 0.18 alpha 0.0

screen kd_cutin(tag, line="", expr=None, color=None, d=0.85):
    zorder 450
    default band_color = color or kd_char_color(tag)

    add Solid("#000000") at kd_cutin_dim(d)

    fixed at kd_cutin_band(d):
        xysize (2700, 400)
        add Solid(band_color)
        add Solid("#06080f") ysize 340 yalign 0.5
        add Solid(band_color) xsize 2700 ysize 4 ypos 46 alpha 0.55
        add Solid(band_color) xsize 2700 ysize 4 ypos 350 alpha 0.55

        add kd_face(tag, expr, 340) xpos 1880 yalign 0.5 at kd_cutin_face(d)

        text kd_display_name(tag).upper():
            font "fonts/Rajdhani-SemiBold.ttf"
            size 50
            color band_color
            kerning 6
            xpos 520
            ypos 66

        if line:
            text line at kd_cutin_text(d):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 112
                color "#ffffff"
                outlines [(5, band_color, 0, 0), (2, "#000000", 4, 4)]
                xpos 520
                ypos 130
                xmaximum 1340

    add Solid("#ffffff") at kd_flash_once


# Usage : call cutin("mara", _("C'EST FAUX !"))
#         call cutin("noam")                       (nom seul)
#         call cutin("kael", expr="colere", color="#ff2e55")
label cutin(tag, line="", expr=None, color=None):
    if renpy.is_skipping():
        return
    play kd_fx "audio/sfx_interrupt_impact.wav"
    show screen kd_cutin(tag, line, expr, color)
    $ renpy.pause(1.05)
    hide screen kd_cutin
    return


# ------------------------------------------------------------
# Panneaux de réactions simultanées (2 à 4 personnages)
# ------------------------------------------------------------
transform kd_panel_in(delay=0.0, d=1.2):
    yoffset 760
    alpha 0.0
    pause delay
    easeout 0.16 yoffset 0 alpha 1.0
    pause d
    easein 0.14 yoffset -760 alpha 0.0

transform kd_panels_dim(d=1.2):
    alpha 0.0
    linear 0.1 alpha 0.6
    pause d
    linear 0.2 alpha 0.0

screen kd_reactions(items, d=1.2):
    zorder 440
    $ count = max(1, min(4, len(items)))
    $ panel_w = int(1920 / count)
    $ face_size = min(panel_w - 40, 560)

    add Solid("#000000") at kd_panels_dim(d)

    for i, item in enumerate(items[:4]):
        $ r_tag = item[0]
        $ r_expr = item[1] if len(item) > 1 else None
        $ r_color = kd_char_color(r_tag)
        fixed at kd_panel_in(i * 0.07, d):
            xpos i * panel_w
            ypos 230
            xysize (panel_w, 620)
            fixed at kd_tilt(-4):
                xysize (face_size + 16, face_size + 16)
                xalign 0.5
                yalign 0.0
                add Solid(r_color)
                add kd_face(r_tag, r_expr, face_size) xalign 0.5 yalign 0.5
                add Solid("#05060ad9") xalign 0.5 yalign 1.0 xsize face_size ysize 58 yoffset -8
                text kd_display_name(r_tag).upper():
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 40
                    color r_color
                    kerning 4
                    xalign 0.5
                    yalign 1.0
                    yoffset -14


# Usage : call reactions([("mara", "colere"), ("lysa", "surpris"), ("julian", "peur")])
label reactions(items, hold=1.2):
    if renpy.is_skipping():
        return
    play kd_fx "audio/trailer/trl_swoosh.wav"
    show screen kd_reactions(items, hold)
    $ renpy.pause(hold + 0.35)
    hide screen kd_reactions
    return


# ------------------------------------------------------------
# Ouverture de séance du Conclave (identité commune des débats et votes)
# ------------------------------------------------------------
transform kd_trial_marquee(direction=1):
    xoffset (0 if direction > 0 else -1600)
    linear 2.6 xoffset (-1600 if direction > 0 else 0)

transform kd_tilt(angle=-4):
    rotate angle

# Positionnement par le centre : la rotation agrandit la boîte englobante,
# un yalign classique décalerait donc la bande hors de l'écran.
transform kd_trial_band_in(delay=0.0, y=230, angle=-7):
    xanchor 0.5
    xpos 0.5
    yanchor 0.5
    ypos y
    rotate angle
    xoffset -2400
    pause delay
    easeout 0.22 xoffset 0

transform kd_trial_title:
    alpha 0.0
    zoom 2.4
    pause 0.45
    easeout 0.14 alpha 1.0 zoom 1.0

transform kd_trial_subtitle:
    alpha 0.0
    pause 0.75
    easeout 0.25 alpha 1.0

screen kd_trial_intro(title, subtitle=""):
    zorder 460
    add Solid("#05060a")

    fixed at kd_trial_band_in(0.0, 215):
        xysize (2600, 170)
        add Solid(KD_TRIAL_ACCENT)
        hbox at kd_trial_marquee(1):
            spacing 14
            ypos 10
            for c in KD_CAST_ORDER + KD_CAST_ORDER:
                add kd_portrait(c, 150)

    fixed at kd_trial_band_in(0.1, 865):
        xysize (2600, 170)
        add Solid("#e8edf6")
        hbox at kd_trial_marquee(-1):
            spacing 14
            ypos 10
            for c in reversed(KD_CAST_ORDER + KD_CAST_ORDER):
                add kd_portrait(c, 150)

    text title at kd_trial_title:
        font "fonts/Rajdhani-SemiBold.ttf"
        size 150
        color "#ffffff"
        outlines [(6, KD_TRIAL_ACCENT, 0, 0)]
        kerning 8
        xalign 0.5
        yalign 0.47

    if subtitle:
        text subtitle at kd_trial_subtitle:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 44
            color "#e8edf6"
            kerning 4
            xalign 0.5
            yalign 0.62

    add Solid("#ffffff") at kd_flash_once


# Usage : call trial_intro(_("SÉANCE DU CONCLAVE"), _("Vote : abolition des rations"))
label trial_intro(title=None, subtitle=""):
    if renpy.is_skipping():
        return
    $ _kd_title = title or _("SÉANCE DU CONCLAVE")
    play kd_fx "audio/trailer/trl_braam.wav"
    show screen kd_trial_intro(_kd_title, subtitle)
    $ renpy.pause(2.5)
    hide screen kd_trial_intro
    with Dissolve(0.15)
    return
