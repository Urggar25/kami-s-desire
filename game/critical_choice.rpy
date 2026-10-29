# ============================================================
# critical_choice.rpy — HUD des CHOIX CRITIQUES
# Réservé aux décisions majeures (PAS les petits choix).
# Supporte 2 à 4 options, layout adaptatif, Noam glitché.
#
# Usage dans le scénario :
#   menu (screen="critical_choice", noam_expr="hesitation"):
#       "Titre affiché en haut"
#       "Option A":
#           ...
#       "Option B":
#           ...
#
#   - Le "titre" = la ligne de menu sans bloc (caption).
#   - noam_expr : expression du layered image noam (def. "reflexion").
#   - Fonctionne avec 2, 3 ou 4 options (max 4).
# ============================================================

define CC_DIR = "images/hud/critical_choice"

# ------------------------------------------------------------
# Positions des panneaux selon le nombre d'options
# (xpos, ypos) en fraction d'écran, ancrage centre (0.5,0.5)
# ------------------------------------------------------------
init python:
    CC_LAYOUT = {
        1: [(0.500, 0.640)],
        2: [(0.250, 0.580), (0.750, 0.580)],
        3: [(0.238, 0.500), (0.762, 0.500), (0.500, 0.820)],
        4: [(0.238, 0.450), (0.762, 0.450), (0.238, 0.740), (0.762, 0.740)],
    }

    CC_UNFINISHED_LABELS = set()
    CC_UNRELEASED_PACKS = {"mystere"}  # Annonce réservée, aucune date ni achat.
    CC_STORY_PACKS = {"origine": {"title": "L'Origine", "days": "Jours 5 à 30", "endings": "7 fins", "tagline": "Découvrez une des vérités cachées derrière le Conclave."},
        "doppelganger_routes": {"title": "L’Origine", "days": "Jours 20 à 30", "endings": "Fins alternatives", "tagline": "Et si Noam avait choisi autrement ?"}}

    def cc_owned_packs():
        # Development entitlement, NOT commercial DRM.
        # Les anciens packs restent inchangés ; pas de faux droit d'accès persistant.
        owned = ["origine"]
        if kd_dlc_unlocked("doppelganger_routes"):
            owned.append("doppelganger_routes")
        return owned

    def cc_option_status(destination=None, pack=None):
        if pack in CC_UNRELEASED_PACKS:
            return "coming_soon"
        if destination and (destination in CC_UNFINISHED_LABELS or not renpy.has_label(destination)):
            return "unreleased"
        if pack and pack not in cc_owned_packs():
            return "dlc"
        return "available"

    def cc_option_details(caption, targets):
        options = targets or {}
        spec = options.get(caption, {})
        if not spec:
            for source_caption, candidate in options.items():
                if renpy.translate_string(source_caption) == caption:
                    spec = candidate
                    break
        if isinstance(spec, str):
            spec = {"label": spec}
        return cc_option_status(spec.get("label"), spec.get("pack")), spec.get("pack")

    def cc_positions(n):
        return CC_LAYOUT.get(n, CC_LAYOUT[2])

# ------------------------------------------------------------
# Noam glitché (aberration chromatique + jitter)
# ------------------------------------------------------------
transform cc_noam_base:
    subpixel True
    zoom 1.07 xalign 0.5 yanchor 1.0 ypos 1.025
    block:
        pause 1.1
        ease 0.02 xoffset -3
        ease 0.02 xoffset 4
        ease 0.02 xoffset 0
        pause 0.6
        ease 0.02 xoffset 2
        ease 0.02 xoffset -1
        ease 0.02 xoffset 0
        pause 0.5
        repeat

transform cc_noam_ghost(dx, tint):
    subpixel True
    zoom 1.07 xalign 0.5 yanchor 1.0 ypos 1.025
    matrixcolor TintMatrix(tint)
    additive 1.0
    alpha 0.30
    xoffset dx
    block:
        pause 1.1
        ease 0.03 xoffset dx * 3
        ease 0.05 xoffset dx
        pause 0.6
        ease 0.03 xoffset dx * 2
        ease 0.05 xoffset dx
        pause 0.5
        repeat

# léger scan/flicker sur l'ensemble du personnage
transform cc_noam_flicker:
    block:
        alpha 1.0
        pause 2.3
        linear 0.03 alpha 0.82
        linear 0.03 alpha 1.0
        pause 1.7
        linear 0.02 alpha 0.9
        linear 0.02 alpha 1.0
        repeat

# ------------------------------------------------------------
# Entrées animées
# ------------------------------------------------------------
transform cc_panel_in(delay=0.0):
    alpha 0.0 zoom 0.86
    pause delay
    parallel:
        easein 0.28 alpha 1.0
    parallel:
        easeout 0.34 zoom 1.0

transform cc_title_in:
    alpha 0.0 yoffset -22
    parallel:
        easein 0.4 alpha 1.0
    parallel:
        easeout 0.45 yoffset 0

transform cc_title_glitch:
    block:
        xoffset 0
        pause 1.4
        linear 0.02 xoffset -4
        linear 0.02 xoffset 5
        linear 0.02 xoffset 0
        pause 0.9
        linear 0.02 xoffset 3
        linear 0.02 xoffset 0
        repeat

transform cc_teaser_pulse:
    alpha 0.88
    block:
        ease 0.75 alpha 1.0
        ease 0.75 alpha 0.88
        repeat

transform cc_story_card_enter(delay=0.0):
    alpha 0.0 yoffset -24
    pause delay
    easeout 0.38 alpha 1.0 yoffset 0

transform cc_story_connector_enter(delay=0.0):
    alpha 0.0 yzoom 0.0
    pause delay
    easeout 0.27 alpha 0.80 yzoom 1.0

transform cc_bar_pulse:
    block:
        alpha 0.75
        linear 0.9 alpha 1.0
        linear 0.9 alpha 0.75
        repeat

# ------------------------------------------------------------
# ÉCRAN
# ------------------------------------------------------------
screen critical_choice(items, noam_expr="reflexion", cc_targets=None, cc_prompt=None):
    style_prefix "cc"
    modal True
    zorder 210

    python:
        _cc_choices = [i for i in items if i.action]
        _cc_caps = [i.caption for i in items if not i.action]
        _cc_title = _cc_caps[0] if _cc_caps else ""
        _cc_n = len(_cc_choices)
        _cc_pos = cc_positions(_cc_n)
        # Le mode Story Pack est réservé aux véritables embranchements de route.
        _cc_story_mode = (_cc_n == 2 and any(cc_option_details(i.caption, cc_targets)[1] for i in _cc_choices))

    # Fond assombri ; interface de jeu sous-jacente masquée.
    add Solid("#03070df2")

    # Noam glitché (centre)
    fixed:
        xsize 1920 ysize 1080
        at cc_noam_flicker
        add ("noam " + noam_expr) at cc_noam_ghost(-7, "#ff2d6b")
        add ("noam " + noam_expr) at cc_noam_ghost(7, "#33e0ff")
        add ("noam " + noam_expr) at cc_noam_base

    # Overlays glitch
    add CC_DIR + "/scanlines.png"
    add CC_DIR + "/vignette.png"

    # Réticule sur le visage
    add CC_DIR + "/reticle.png" xpos 0.5 ypos 0.30 anchor (0.5, 0.5) at Transform(alpha=0.9)

    # Question : pour les routes premium elle est intégrée au HUD et
    # ne dépend pas de la boîte de dialogue masquée.
    if _cc_story_mode:
        fixed at cc_title_in:
            xpos 0.5 ypos 27 xanchor 0.5
            xsize 740 ysize 94
            add Solid("#4DAFD180") xpos 30 ypos 43 xsize 120 ysize 1
            add Solid("#4DAFD180") xpos 590 ypos 43 xsize 120 ysize 1
            text "DÉCISION CRITIQUE":
                xalign 0.5 ypos 0
                font "fonts/Rajdhani-SemiBold.ttf"
                size 20 color "#79CDE3"
            text (cc_prompt or _cc_title or "Quel chemin choisir ?"):
                xalign 0.5 ypos 35
                font "fonts/Rajdhani-SemiBold.ttf"
                size 37 color "#F2FBFF"
    # Titre glitché réservé à l'interface classique.
    if _cc_title and not _cc_story_mode:
        fixed:
            xsize 1920 ysize 200
            ypos 0.045
            at cc_title_in
            fixed:
                at cc_title_glitch
                text _cc_title style "cc_title_ghost_m" xalign 0.5 ypos 0 offset (-4, 2) at Transform(alpha=0.55)
                text _cc_title style "cc_title_ghost_c" xalign 0.5 ypos 0 offset (4, -2) at Transform(alpha=0.55)
                text _cc_title style "cc_title" xalign 0.5 ypos 0

    # Choix standards inchangés ; la vitrine Story Pack n'existe
    # que sur les menus dont les branches déclarent un pack.
    for idx, i in enumerate(_cc_choices):
        $ px, py = _cc_pos[idx] if idx < len(_cc_pos) else (0.5, 0.5 + idx * 0.12)
        $ _cc_status, _cc_pack = cc_option_details(i.caption, cc_targets)
        $ _cc_locked = _cc_status != "available"
        $ _cc_panel_y = (0.267 if _cc_story_mode else py)
        $ _cc_panel_x = ((0.20 if idx == 0 else 0.80) if _cc_story_mode else px)
        button:
            action (Show("cc_pack_information", pack_id=_cc_pack) if _cc_status == "dlc" else (NullAction() if _cc_locked else i.action))
            xpos _cc_panel_x ypos _cc_panel_y
            anchor (0.5, 0.5)
            xysize (560, 128)
            background (Transform(CC_DIR + "/panel_idle.png", matrixcolor=SaturationMatrix(0.0), alpha=0.56) if _cc_locked else CC_DIR + "/panel_idle.png")
            hover_background (Transform(CC_DIR + "/panel_idle.png", matrixcolor=SaturationMatrix(0.0), alpha=0.56) if _cc_locked else CC_DIR + "/panel_hover.png")
            at cc_panel_in(0.15 + idx * 0.08)
            text i.caption:
                style "cc_option_text"
                align (0.5, 0.5)
                color ("#758493" if _cc_locked else "#D6F2FF")
                hover_color ("#758493" if _cc_locked else "#06131F")
            if _cc_locked:
                add CC_DIR + "/lock.svg":
                    xpos 16 yalign 0.5 xysize (37, 43)

    # Cartes narratives compactes. Deux colonnes strictes, sans collision
    # avec la silhouette centrale ni l'interface de confirmation.
    if _cc_story_mode and _cc_n == 2:
        for idx, i in enumerate(_cc_choices):
            $ _status, _pack = cc_option_details(i.caption, cc_targets)
            $ _locked = _status != "available"
            $ _card_x = (110 if idx == 0 else 1270)
            $ _card_border = "#414D5F" if _locked else "#48CDE9"
            $ _card_accent = "#8794A3" if _locked else "#86E9FF"
            # Liaison verticale entre la décision et son Story Pack.
            add Solid(_card_border):
                xpos (380 if idx == 0 else 1540) ypos 334
                xsize 2 ysize 32
                at cc_story_connector_enter(0.27 + idx * 0.1)
            add Solid(_card_border):
                xpos (376 if idx == 0 else 1536) ypos 362
                xsize 10 ysize 7
                at cc_panel_in(0.32 + idx * 0.1)
            fixed at cc_story_card_enter(0.39 + idx * 0.10):
                xpos _card_x ypos 366
                xsize 540 ysize 338

                # Cadre parfaitement aligné sous le choix (540 px).
                add Solid(_card_border + "A0") xsize 540 ysize 338
                add Solid("#06111CF8") xpos 2 ypos 2 xsize 536 ysize 334
                add Solid(_card_border) xpos 0 ypos 0 xsize 135 ysize 3
                add Solid(_card_border) xpos 405 ypos 335 xsize 135 ysize 3
                add Solid(_card_border) xpos 0 ypos 0 xsize 3 ysize 44
                add Solid(_card_border) xpos 537 ypos 294 xsize 3 ysize 44

                # Hiérarchie lisible : titre, chiffres, image, une seule accroche.
                if _locked:
                    add CC_DIR + "/lock.svg" xpos 22 ypos 19 xsize 35 ysize 40
                    text "STORY PACK : ???" xpos 72 ypos 16:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 32 color "#B8C0CC"
                    text "NON ANNONCÉ" xpos 72 ypos 53:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 21 color "#A5B0BB"
                else:
                    add Solid("#66DBF0") xpos 25 ypos 27 xsize 21 ysize 21
                    text ("STORY PACK : " + CC_STORY_PACKS.get(_pack, {}).get("title", "À VENIR")).upper() xpos 70 ypos 16:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 31 color "#F3FCFF"
                    text ("JOURS 5–30     •     7 FINS" if _pack == "origine" else "CONTENU ADDITIONNEL") xpos 70 ypos 53:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 22 color "#8BE3F3"
                add Solid(_card_border + "80") xpos 20 ypos 87 xsize 500 ysize 2

                if _status == "coming_soon":
                    # Une véritable image de dossier censuré : le visuel est
                    # délibérément obscurci, mais reste identifiable comme une photo.
                    fixed:
                        xpos 20 ypos 102
                        xsize 500 ysize 174
                        clipping True
                        add Solid("#070E18") xsize 500 ysize 174
                        add Transform("bg_conduit_reseau", fit="cover",
                            xysize=(500, 174), matrixcolor=SaturationMatrix(0.0), alpha=0.31)
                        add Solid("#0306108E") xsize 500 ysize 174
                        add Solid("#02040AF0") xpos 152 ypos 14 xsize 192 ysize 30
                        add Solid("#02040AF0") xpos 128 ypos 62 xsize 245 ysize 32
                        add Solid("#02040AF0") xpos 177 ypos 108 xsize 158 ysize 29
                        add Solid("#8D9DAB55") xpos 14 ypos 12 xsize 102 ysize 2
                        add Solid("#8D9DAB55") xpos 14 ypos 19 xsize 63 ysize 2
                        add Solid("#8D9DAB44") xpos 382 ypos 150 xsize 99 ysize 2
                        text "ARCHIVE // ACCÈS REFUSÉ" xpos 17 ypos 146:
                            font "fonts/Rajdhani-SemiBold.ttf"
                            size 19 color "#A3AFBE"
                        add CC_DIR + "/lock.svg" xpos 229 ypos 53 xsize 42 ysize 48
                    text "UN AUTRE DESTIN VOUS ATTEND." xpos 23 ypos 289:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 24 color "#DFE6ED"
                elif _pack == "origine":
                    # Une seule cible de clic : la vignette entière.
                    button:
                        xpos 20 ypos 102 xsize 500 ysize 174
                        padding (0, 0)
                        background Solid("#07111C")
                        hover_background Solid("#122D3A")
                        action Function(renpy.call_in_new_context, "origine_story_pack_teaser")
                        # Le fixed découpe réellement la CG : plus aucun
                        # pixel en dehors du cadre 500 × 174.
                        fixed:
                            xsize 500 ysize 174
                            clipping True
                            add Transform("bg_cg052", fit="cover", xysize=(500, 174), alpha=0.93)
                            add Solid("#090C1B62") xsize 500 ysize 174
                            add Solid("#EC567A") xsize 4 ysize 174
                            add Solid("#082338CC") xpos 209 ypos 49 xsize 82 ysize 75 at cc_teaser_pulse
                            text "▶" xalign 0.5 yalign 0.47 size 61 color "#E6FCFF"
                            add Solid("#03101BB0") xpos 440 ypos 143 xsize 60 ysize 31
                            text "30 S" xpos 469 ypos 147 anchor (0.5, 0.0):
                                font "fonts/Rajdhani-SemiBold.ttf"
                                size 20 color "#F1FAFF"
                    text "UNE VÉRITÉ CACHÉE DU CONCLAVE" xpos 22 ypos 289:
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 24 color "#E8F7FF"
                else:
                    add Solid("#0C1722") xpos 20 ypos 102 xsize 500 ysize 174
                    text "APERÇU À VENIR" xpos 270 ypos 189 anchor (0.5, 0.5) size 25 color "#A6BAC8"
                    text "NOUVELLE ROUTE NARRATIVE" xpos 22 ypos 289 size 23 color "#C8DAE5"

    # La consigne n'est pertinente que pour les décisions disponibles.
    if not _cc_story_mode:
        frame:
            style "cc_confirm_bar"
            xalign 0.5 yalign 0.965
            at cc_bar_pulse
            hbox:
                spacing 14
                align (0.5, 0.5)
                frame:
                    style "cc_key_badge"
                    text "A" style "cc_key_text"
                text _("Confirmer") style "cc_confirm_text"

# ------------------------------------------------------------
# STYLES
# ------------------------------------------------------------
style cc_title is default
style cc_title_ghost_m is cc_title
style cc_title_ghost_c is cc_title
style cc_option_text is default
style cc_confirm_bar is frame
style cc_confirm_text is default
style cc_key_badge is frame
style cc_key_text is default

style cc_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 82
    color "#ffffff"
    outlines [(2, "#0a1a2acc", 0, 0)]
    kerning 2.0

style cc_title_ghost_m:
    color "#ff2d6b"
    outlines []

style cc_title_ghost_c:
    color "#33e0ff"
    outlines []

style cc_option_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 40
    color "#d6f2ff"
    hover_color "#06131f"
    selected_color "#06131f"
    kerning 1.0
    text_align 0.5
    xmaximum 470
    outlines []

style cc_confirm_bar:
    background Fixed(
        Solid("#040b14e0"),
        Solid("#5cd3ff40", ysize=2),
        Solid("#5cd3ff40", ysize=2, yalign=1.0),
    )
    xsize 460
    padding (26, 12, 26, 12)

style cc_confirm_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 30
    color "#bfe9ff"
    kerning 3.0

style cc_key_badge:
    background Solid("#5cd3ff")
    xsize 38 ysize 38
    padding (0, 0, 0, 0)

style cc_key_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 26
    color "#04121e"
    xalign 0.5
    yalign 0.5

# Story Pack modal. Replaced by verified storefront entitlement for DLC sales.
screen cc_pack_information(pack_id="origine"):
    modal True
    zorder 250
    $ pack = CC_STORY_PACKS.get(pack_id, CC_STORY_PACKS["origine"])
    add Solid("#02060CEB")
    frame:
        xalign 0.5 yalign 0.5 xsize 850
        background Solid("#0D1726")
        padding (48, 38)
        vbox:
            spacing 19
            text "STORY PACK REQUIS" size 25 color "#69D3E9" xalign 0.5
            text pack["title"] size 64 color "#FFFFFF" xalign 0.5
            text pack["days"] + "   •   " + pack["endings"] size 28 color "#A9BCCC" xalign 0.5
            text pack["tagline"] size 25 color "#E0ECF2" xalign 0.5
            text "Contenu non inclus dans cette édition." size 21 color "#8E9EAB" xalign 0.5
            hbox:
                xalign 0.5 spacing 24
                textbutton "RETOUR":
                    action Hide("cc_pack_information")
    key "K_ESCAPE" action Hide("cc_pack_information")
