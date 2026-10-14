# PROLOGUE - CAISSON. Scene 2D composite et camera subjective.
# Tous les calques gardent le meme canevas que d0_capsule_base.
define D0_CAPSULE_DIR = "images/ui/0/s1_caisson/"
define D0_CAPSULE_ZOOM = 1.23

default d0_cam_x = 0.0
default d0_cam_y = 0.0
default d0_vent_inspecting = False
default d0_vent_enabled = False
default d0_air_elapsed = 0.0
default d0_capsule_alarm = False
default d0_valve_enabled = False
default d0_valve_inspecting = False
default d0_push_impact_count = 0
default d0_push_impact_pending = False

init python:
    def d0_capsule_mouse_camera():
        # Utiliser les bords (18 %), sans effet lorsqu'on reste au centre.
        # Fonction executee uniquement lorsque l'introduction est terminee.
        mx, my = renpy.get_mouse_pos()
        w, h = float(config.screen_width), float(config.screen_height)
        if w <= 0 or h <= 0:
            return
        nx, ny = mx / w, my / h
        def edge(v):
            if v < 0.18:
                return -(0.18 - max(0.0, v)) / 0.18
            if v > 0.82:
                return (min(1.0, v) - 0.82) / 0.18
            return 0.0
        # Mouvement oppose a la direction du regard, borne a la marge du zoom.
        max_x = w * (D0_CAPSULE_ZOOM - 1.0) / 2.0 * 0.85
        max_y = h * (D0_CAPSULE_ZOOM - 1.0) / 2.0 * 0.85
        target_x = -edge(nx) * max_x
        target_y = -edge(ny) * max_y
        st = renpy.store
        st.d0_cam_x += (target_x - st.d0_cam_x) * 0.14
        st.d0_cam_y += (target_y - st.d0_cam_y) * 0.14

# Le mouvement d'ouverture est dirige et ne repond pas a la souris.
transform d0_capsule_intro_camera:
    subpixel True
    zoom D0_CAPSULE_ZOOM
    xalign 0.5 yalign 0.5
    xoffset 0 yoffset 0
    pause 0.25
    ease 0.85 xoffset 145 yoffset -12
    pause 0.20
    ease 1.25 xoffset -145 yoffset -12
    pause 0.15
    ease 1.10 xoffset 0 yoffset 90
    pause 0.25
    ease 0.60 xoffset 0 yoffset 0

# Flash concentre exactement sur le detecteur (410, 127) du CANEVAS SOURCE.
# Pas de longues lignes geometriques dont le pivot se decale avec rotate.
transform d0_capsule_color_pulse:
    alpha 0.0
    linear 0.13 alpha 0.75
    pause 0.16
    ease 0.34 alpha 0.0
    pause 1.37
    repeat

transform d0_capsule_sun_pulse:
    alpha 0.0
    zoom 0.70
    parallel:
        linear 0.13 alpha 0.85
        pause 0.16
        ease 0.34 alpha 0.0
        pause 1.37
        repeat
    parallel:
        ease 0.63 zoom 1.45
        pause 1.37
        zoom 0.70
        repeat

# Le detecteur est eteint par defaut; il pulse toutes les 2 secondes :
# environ 0.65s allume, 1.35s gris.
transform d0_led_flash:
    alpha 0.0
    linear 0.12 alpha 1.0
    pause 0.22
    linear 0.34 alpha 0.0
    pause 1.32
    repeat

transform d0_lights_stable:
    alpha 0.97

# Le calque sombre est placé AU-DESSUS de la base, SOUS les elements eclaires.
# Ne pas flouter les illustrations, ne pas déplacer les éléments isolément.
# Composition des objets physiques sans duplication de textures dans le hotspot.
# L'eclairage final couvre decor, bras et ventilation, tout en restant SOUS l'UI.
screen d0_capsule_picture():
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        add (D0_CAPSULE_DIR + "d0_capsule_base.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_vent.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_valve.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_led_gray.png") xysize (config.screen_width, config.screen_height)

screen d0_capsule_lighting(alarm=False, intro=False):
    # Positif pour passer devant toutes les textures, mais sous screen say.
    zorder 0
    # Filtre sur la TOTALITE des sprites, jamais sur le texte.
    if intro:
        fixed:
            xsize config.screen_width
            ysize config.screen_height
            at d0_capsule_intro_camera
            use d0_capsule_lighting_contents(alarm)
    else:
        fixed:
            xsize config.screen_width
            ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            use d0_capsule_lighting_contents(alarm)

screen d0_capsule_lighting_contents(alarm):
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        add Solid("#020812E0")
        if alarm:
            $ pulse_color = "#FF9191"
            $ led_asset = D0_CAPSULE_DIR + "d0_capsule_led_red.png"
        else:
            $ pulse_color = "#B9FFAC"
            $ led_asset = D0_CAPSULE_DIR + "d0_capsule_led_green.png"
        add Solid(pulse_color + "35") at d0_capsule_color_pulse
        add led_asset xysize (config.screen_width, config.screen_height) at d0_led_flash

# Effet revele puis efface par deux fronts de balayage descendants.
# Aucune translation du visuel, seule une tranche du PNG original est visible.
init python:
    def d0_tick_air():
        renpy.store.d0_air_elapsed = (renpy.store.d0_air_elapsed + 0.0333333) % 5.0

screen d0_air_wipe():
    $ t = d0_air_elapsed
    $ w, h = config.screen_width, config.screen_height
    $ lower = int(h * min(1.0, t / 1.0))
    $ upper = int(h * min(1.0, max(0.0, (t - 0.5) / 0.55)))
    $ band = max(0, lower - upper)
    if band > 0:
        add Transform(
            Transform(D0_CAPSULE_DIR + "d0_capsule_vent_anim.png", xysize=(w, h)),
            crop=(0, upper, w, band),
            xpos=0, ypos=upper, xanchor=0.0, yanchor=0.0)

# Un cycle relance a la demande pendant le passage de la main.
transform reverse_img:
    xzoom -1.0

transform d0_push_hold_visibility:
    on show:
        alpha 0.0
        linear 0.18 alpha 1.0
    on hide:
        linear 0.22 alpha 0.0

transform d0_pousse_fade:
    alpha 0.0
    linear 0.18 alpha 1.0

transform d0_pousse_rest:
    alpha 1.0

transform d0_arm_sway:
    subpixel True
    xoffset 0
    ease 0.12 xoffset -11
    ease 0.13 xoffset 11
    ease 0.12 xoffset -7
    ease 0.13 xoffset 0

screen d0_capsule_vent_air():
    zorder -4
    timer 0.0333333 repeat True action Function(d0_tick_air)
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        use d0_air_wipe

# Deux calques PNG successifs + la pose finale, toujours superposes au
# caisson suivant le meme zoom et le meme decalage que la camera.
screen d0_capsule_arm(pose=1, sway=False, reversed=False):
    zorder -3
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        if sway:
            add (D0_CAPSULE_DIR + "d0_capsule_bras3.png"):
                xysize (config.screen_width, config.screen_height)
                at d0_arm_sway
        elif reversed:
            add (D0_CAPSULE_DIR + "d0_capsule_bras%d.png" % pose):
                xysize (config.screen_width, config.screen_height)
                at reverse_img
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_bras%d.png" % pose) xysize (config.screen_width, config.screen_height)

# Cible invisible : masque alpha du PNG, aucun deuxieme dessin du vent.
screen d0_capsule_vent_hotspot():
    # Au-dessus de screen say pour capter les clics sur la grille.
    # Aucune image affichee : uniquement le masque alpha.
    zorder 30
    if d0_vent_enabled and not d0_vent_inspecting:
        fixed:
            xsize config.screen_width
            ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            button:
                xsize config.screen_width
                ysize config.screen_height
                background None
                hover_background None
                focus_mask Transform(D0_CAPSULE_DIR + "d0_capsule_vent.png", xysize=(config.screen_width, config.screen_height))
                action Call("d0_inspect_vent")

# Hitbox invisible placee aux coordonnees du cylindre (sur canevas 1690x931).
screen d0_capsule_valve_hotspot():
    # Au-dessus de screen say et du hotspot de ventilation.
    # Sinon le dialogue consomme le clic avant le bouton.
    zorder 31
    if d0_valve_enabled and not d0_valve_inspecting:
        fixed:
            xsize config.screen_width
            ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            button:
                xsize config.screen_width
                ysize config.screen_height
                background None
                hover_background None
                focus_mask Transform(D0_CAPSULE_DIR + "d0_capsule_valve.png", xysize=(config.screen_width, config.screen_height))
                action Call("d0_inspect_valve", from_current=True)

# Le scénério change ce mode apres l'ouverture dirigee.
screen d0_capsule_live(mode="idle"):
    zorder -6
    if mode == "intro":
        fixed:
            xsize config.screen_width ysize config.screen_height
            at d0_capsule_intro_camera
            use d0_capsule_picture()
    else:
        timer 0.033 repeat True action Function(d0_capsule_mouse_camera)
        fixed:
            xsize config.screen_width ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            use d0_capsule_picture()

# Poussee sur le couvercle (sprites pleine image, meme cadrage que le caisson).
# La main est placee SOUS le filtre nocturne et SOUS les dialogues.
transform d0_push_strain:
    subpixel True
    xoffset 0 yoffset 0
    block:
        ease 0.18 xoffset -3 yoffset -2
        ease 0.17 xoffset 3 yoffset 1
        ease 0.16 xoffset -2 yoffset -1
        ease 0.18 xoffset 0 yoffset 0
        repeat

transform d0_push_impact_overlay:
    alpha 1.0
    pause 0.8
    ease 0.12 alpha 0.0

# bras0 n'est actuellement pas present dans les assets du depot.
# Au repos, la main est donc masquee plutot que de charger un PNG inexistant.
screen d0_pousse_hand(hit=False, pressing=False):
    zorder -3
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        if hit:
            add (D0_CAPSULE_DIR + "d0_pousse_bras2.png") xysize (config.screen_width, config.screen_height)
            add (D0_CAPSULE_DIR + "d0_pousse_bras2_anim.png"):
                xysize (config.screen_width, config.screen_height)
                at d0_push_impact_overlay
        elif pressing:
            add (D0_CAPSULE_DIR + "d0_pousse_bras1.png"):
                xysize (config.screen_width, config.screen_height)
                at d0_push_strain, d0_pousse_fade
