# PROLOGUE - CAISSON. Scene 2D composite et camera subjective.
# Tous les calques gardent le meme canevas que d0_capsule_base.
define D0_CAPSULE_DIR = "images/ui/0/s1_caisson/"
define D0_CAPSULE_ZOOM = 1.23

default d0_cam_x = 0.0
default d0_cam_y = 0.0
default d0_vent_inspecting = False
default d0_vent_enabled = False

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

screen d0_capsule_beacon(color="#B9FFAC"):
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        $ cx = int(config.screen_width * 410.0 / 1690.0)
        $ cy = int(config.screen_height * 127.0 / 931.0)
        # Eclair bref teinte la piece : le fond reste presque noir au repos.
        add Solid(color):
            alpha 0.33
            at d0_capsule_color_pulse
        # Pas de glyphe Unicode : la police du jeu ne possede pas l'etoile.
        # Le PNG du voyant gere son propre halo; la teinte de la scene
        # est animee par d0_capsule_color_pulse.

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
screen d0_capsule_picture(alarm=False):
    fixed:
        xfill True yfill True
        add (D0_CAPSULE_DIR + "d0_capsule_base.png") xysize (config.screen_width, config.screen_height)
        # Composer d'abord TOUS les objets, puis assombrir l'ensemble.
        add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_vent.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_valve.png") xysize (config.screen_width, config.screen_height)
        add (D0_CAPSULE_DIR + "d0_capsule_led_gray.png") xysize (config.screen_width, config.screen_height)
        # Filtre NUIT au-dessus des composants, environ 88 % d'obscurcissement.
        add Solid("#020812E0")
        if alarm:
            add (D0_CAPSULE_DIR + "d0_capsule_led_red.png") xysize (config.screen_width, config.screen_height) at d0_led_flash
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_led_green.png") xysize (config.screen_width, config.screen_height) at d0_led_flash
        # Le rayon et sa coloration suivent le meme cycle de 2s que la LED.
        if alarm:
            use d0_capsule_beacon("#FF9191")
        else:
            use d0_capsule_beacon("#B9FFAC")

# Souffle par balayage vertical : apparition 0-1 s, disparition
# 0.5-1.5 s. Les deux balayages se croisent pendant 0.5 s.
# Le cycle complet dure 5 s. L'animation ne change jamais de position.
transform d0_vent_reveal:
    subpixel True
    crop (0, 0, config.screen_width, 1)
    linear 1.0 crop (0, 0, config.screen_width, config.screen_height)
    pause 4.0
    repeat

transform d0_vent_erase:
    subpixel True
    crop (0, 0, config.screen_width, config.screen_height)
    pause 0.5
    linear 1.0 crop (0, config.screen_height - 1, config.screen_width, 1)
    pause 3.5
    repeat

# Un cycle relance a la demande pendant le passage de la main.
transform d0_arm_sway:
    subpixel True
    xoffset 0
    ease 0.12 xoffset -11
    ease 0.13 xoffset 11
    ease 0.12 xoffset -7
    ease 0.13 xoffset 0

screen d0_capsule_vent_air():
    zorder 1
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        add At(At(Transform(D0_CAPSULE_DIR + "d0_capsule_vent_anim.png",
            xysize=(config.screen_width, config.screen_height)), d0_vent_reveal), d0_vent_erase)

# Deux calques PNG successifs + la pose finale, toujours superposes au
# caisson suivant le meme zoom et le meme decalage que la camera.
screen d0_capsule_arm(pose=1, sway=False):
    zorder 20
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        if sway:
            add (D0_CAPSULE_DIR + "d0_capsule_bras3.png"):
                xysize (config.screen_width, config.screen_height)
                at d0_arm_sway
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_bras%d.png" % pose) xysize (config.screen_width, config.screen_height)

# Calque interactif exactement sur le PNG de la grille : pas de rectangle
# invisible clicable au-dessus des autres objets.
screen d0_capsule_vent_hotspot():
    zorder 10
    if d0_vent_enabled and not d0_vent_inspecting:
        fixed:
            xsize config.screen_width
            ysize config.screen_height
            at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
            imagebutton:
                idle (D0_CAPSULE_DIR + "d0_capsule_vent.png")
                hover (D0_CAPSULE_DIR + "d0_capsule_vent.png")
                xysize (config.screen_width, config.screen_height)
                focus_mask True
                action Call("d0_inspect_vent")

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
