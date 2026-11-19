# Kami's Desires — animations de dialogue inspirees d'une mise en scene VN
# Effets opt-in : aucun automatisme sur l'ensemble du scenario.
# Voir les labels kd_vn_entrance, kd_vn_reaction, kd_vn_cg_impact.
# Conserve le systeme showGroup et les cameras existantes.

transform kd_vn_slide_left:
    subpixel True
    xalign 0.23
    yalign 1.0
    xoffset -240
    alpha 0.0
    zoom 0.94
    parallel:
        easeout 0.28 xoffset 18 alpha 1.0 zoom 1.02
        easein 0.10 xoffset 0 zoom 1.0

transform kd_vn_slide_right:
    subpixel True
    xalign 0.77
    yalign 1.0
    xoffset 240
    alpha 0.0
    zoom 0.94
    parallel:
        easeout 0.28 xoffset -18 alpha 1.0 zoom 1.02
        easein 0.10 xoffset 0 zoom 1.0

transform kd_vn_pop:
    subpixel True
    xalign 0.5
    yalign 1.0
    alpha 0.0
    zoom 0.84
    easeout 0.17 alpha 1.0 zoom 1.09
    easein 0.13 zoom 0.99
    easeout 0.07 zoom 1.0

transform kd_vn_bounce:
    subpixel True
    xalign 0.5
    yalign 1.0
    yoffset 80
    alpha 0.0
    easeout 0.13 yoffset -28 alpha 1.0
    easein 0.10 yoffset 0
    easeout 0.09 yoffset -8
    easein 0.09 yoffset 0

transform kd_vn_reaction_back:
    alpha 0.0
    linear 0.06 alpha 0.60
    pause 0.36
    easeout 0.18 alpha 0.0

transform kd_vn_reaction_face:
    subpixel True
    xalign 0.5
    yalign 0.5
    zoom 1.35
    alpha 0.0
    easeout 0.13 zoom 1.06 alpha 1.0
    easein 0.11 zoom 1.0
    pause 0.25
    easeout 0.15 alpha 0.0 zoom 1.03

transform kd_vn_cg_flash:
    alpha 0.0
    linear 0.035 alpha 0.78
    easeout 0.22 alpha 0.0

transform kd_vn_cg_lines:
    alpha 0.0
    xoffset 180
    easeout 0.10 alpha 0.75 xoffset 0
    easein 0.23 alpha 0.0 xoffset -130

screen kd_vn_entrance_screen(tag, expr="neutre", side="left"):
    zorder 410
    $ enter_motion = kd_vn_slide_left if side == "left" else kd_vn_slide_right if side == "right" else kd_vn_pop
    add character_image(tag, expr) at enter_motion

screen kd_vn_reaction_screen(tag, expr="surpris", accent="#ff5d75"):
    zorder 430
    add Solid("#040914") at kd_vn_reaction_back
    add Solid(accent, xysize=(config.screen_width, 8)) ypos int(config.screen_height * 0.13) at kd_vn_cg_lines
    add Solid(accent, xysize=(config.screen_width, 8)) ypos int(config.screen_height * 0.87) at kd_vn_cg_lines
    add kd_face(tag, expr, min(670, int(config.screen_height * 0.72))) at kd_vn_reaction_face

screen kd_vn_cg_impact_screen(accent="#ffffff"):
    zorder 435
    add Solid(accent) at kd_vn_cg_flash
    add Solid("#ffffff", xysize=(config.screen_width, 5)) ypos int(config.screen_height * 0.34) at kd_vn_cg_lines
    add Solid("#ffffff", xysize=(config.screen_width, 5)) ypos int(config.screen_height * 0.66) at kd_vn_cg_lines

# Une entree animee a declencher AVANT un showGroup (evite les doublons).
label kd_vn_entrance(tag, expr="neutre", side="left"):
    if renpy.is_skipping():
        return
    show screen kd_vn_entrance_screen(tag, expr, side)
    $ renpy.pause(0.38, hard=True)
    hide screen kd_vn_entrance_screen
    return

# Plan expressif d'une demi-seconde, pour une surprise ou une reaction comique.
label kd_vn_reaction(tag, expr="surpris", accent="#ff5d75"):
    if renpy.is_skipping():
        return
    show screen kd_vn_reaction_screen(tag, expr, accent)
    $ renpy.pause(0.62, hard=True)
    hide screen kd_vn_reaction_screen
    return

# Impact de coupe pour CG ou changement de decor ; le scene suivant reste
# sous le controle du scenario. Ne modifie pas les couches camera.
label kd_vn_cg_impact(accent="#ffffff"):
    if renpy.is_skipping():
        return
    show screen kd_vn_cg_impact_screen(accent)
    $ renpy.pause(0.29, hard=True)
    hide screen kd_vn_cg_impact_screen
    return
