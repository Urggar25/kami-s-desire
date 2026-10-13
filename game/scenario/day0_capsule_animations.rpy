# PROLOGUE - CAISSON. Scene 2D composite et camera subjective.
# Tous les calques gardent le meme canevas que d0_capsule_base.
define D0_CAPSULE_DIR = "images/ui/0/s1_caisson/"
define D0_CAPSULE_ZOOM = 1.23

default d0_cam_x = 0.0
default d0_cam_y = 0.0

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
    easein_out 0.85 xoffset 145 yoffset -12
    pause 0.20
    easein_out 1.25 xoffset -145 yoffset -12
    pause 0.15
    easein_out 1.10 xoffset 0 yoffset 90
    pause 0.25
    easein_out 0.60 xoffset 0 yoffset 0

transform d0_capsule_led_glow:
    alpha 0.0
    linear 0.13 alpha 0.9
    easeout 0.24 alpha 0.0

transform d0_capsule_ray_glow:
    alpha 0.0
    linear 0.10 alpha 0.55
    easeout 0.38 alpha 0.0

# Eclairage vert au point (410, 127) dans la resolution SOURCE 1690x931.
# Les rayons sont des traits lumineux transparents et ne constituent pas
# une nouvelle texture qui risque de se decaler.
screen d0_capsule_beacon(color="#B9FFAC"):
    fixed:
        xfill True yfill True
        $ cx = int(config.screen_width * 410.0 / 1690.0)
        $ cy = int(config.screen_height * 127.0 / 931.0)
        add Solid(color + "16") at d0_capsule_led_glow
        # Rayons stylises autour du voyant, peu opaques, effets ponctuels.
        for angle in (-83, -59, -38, -15, 12, 34, 60, 87, 115, 145, 178, 205, 232, 260):
            add Transform(Solid(color), xysize=(int(config.screen_width * 0.30), 3),
                anchor=(0.0, 0.5), rotate=angle, alpha=0.12):
                xpos cx ypos cy
                at d0_capsule_ray_glow

# Le detecteur est eteint par defaut; il pulse toutes les 2 secondes :
# environ 0.65s allume, 1.35s gris.
transform d0_led_flash:
    alpha 0.0
    linear 0.10 alpha 1.0
    pause 0.48
    linear 0.10 alpha 0.0
    pause 1.32
    repeat

transform d0_lights_stable:
    alpha 0.97

# Le calque sombre est placé AU-DESSUS de la base, SOUS les elements eclaires.
# Ne pas flouter les illustrations, ne pas déplacer les éléments isolément.
screen d0_capsule_picture(alarm=False):
    fixed:
        xfill True yfill True
        add (D0_CAPSULE_DIR + "d0_capsule_base.png") xysize (config.screen_width, config.screen_height)
        # Ambiance nuit : bleu nuit transparent, et non un voile blanc.
        add Solid("#07122582")
        add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height) at d0_lights_stable
        add (D0_CAPSULE_DIR + "d0_capsule_vent.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_valve.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_led_gray.png") xysize (config.screen_width, config.screen_height)
        if alarm:
            add (D0_CAPSULE_DIR + "d0_capsule_led_red.png") xysize (config.screen_width, config.screen_height) at d0_led_flash
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_led_green.png") xysize (config.screen_width, config.screen_height) at d0_led_flash
        # Le rayon et sa coloration suivent le meme cycle que la LED.
        if alarm:
            use d0_capsule_periodic_ray("#FF9191")
        else:
            use d0_capsule_periodic_ray("#B9FFAC")

screen d0_capsule_periodic_ray(color):
    fixed:
        xfill True yfill True
        # Chaque apparition est synchronisee avec le debut du cycle de la LED.
        if True:
            use d0_capsule_beacon(color)
        timer 2.0 repeat True action NullAction()

# Le scénério change ce mode apres l'ouverture dirigee.
screen d0_capsule_live(mode="idle"):
    zorder -5
    if mode == "intro":
        fixed:
            xsize config.screen_width ysize config.screen_height
            at d0_capsule_intro_camera
            use d0_capsule_picture(False)
    else:
        timer 0.033 repeat True action Function(d0_capsule_mouse_camera)
        fixed:
            xsize config.screen_width ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            use d0_capsule_picture(mode == "alarm")
