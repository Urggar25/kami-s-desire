# Jour 0 - decor de caisson anime avec les calques images/ui/0/s1_caisson.
# Calques a CANEVAS COMPLET : coordonnees identiques a d0_capsule_base.
# Les transformations touchent la luminosite/opacite, jamais la geometrie.
define D0_CAPSULE_DIR = "images/ui/0/s1_caisson/"

transform d0_capsule_lamp_idle:
    alpha 0.96
    ease 2.8 alpha 1.0
    ease 3.1 alpha 0.95
    repeat

transform d0_capsule_lamp_start:
    alpha 0.0
    pause 0.32
    linear 0.12 alpha 0.80
    linear 0.08 alpha 0.22
    linear 0.16 alpha 1.0
    ease 0.5 alpha 0.96
    block:
        ease 2.8 alpha 1.0
        ease 3.1 alpha 0.95
        repeat

transform d0_capsule_led_normal:
    alpha 1.0
    pause 3.1
    linear 0.1 alpha 0.70
    linear 0.14 alpha 1.0
    repeat

transform d0_capsule_led_warning:
    alpha 1.0
    linear 0.14 alpha 0.40
    linear 0.14 alpha 1.0
    pause 0.55
    repeat

transform d0_capsule_vent_idle:
    subpixel True
    xoffset 0
    pause 4.1
    linear 0.045 xoffset 1
    linear 0.045 xoffset -1
    linear 0.045 xoffset 0
    repeat

transform d0_capsule_valve_start:
    alpha 0.0
    linear 0.28 alpha 1.0

transform d0_capsule_lamp_alarm:
    alpha 1.0
    pause 0.22
    linear 0.06 alpha 0.48
    linear 0.1 alpha 1.0
    pause 0.75
    repeat

# Placement : les textures exportees en pleine resolution sont superposees a (0, 0).
# Aucun flou, aucun halo supplementaire, aucune reinterpolation de perspective.
screen d0_capsule_live(mode="idle"):
    zorder -5
    fixed:
        xfill True
        yfill True
        add (D0_CAPSULE_DIR + "d0_capsule_base.png") xysize (config.screen_width, config.screen_height)
        if mode == "startup":
            add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height) at d0_capsule_lamp_start
        elif mode == "alarm":
            add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height) at d0_capsule_lamp_alarm
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_lights.png") xysize (config.screen_width, config.screen_height) at d0_capsule_lamp_idle
        add (D0_CAPSULE_DIR + "d0_capsule_vent.png") xysize (config.screen_width, config.screen_height) at d0_capsule_vent_idle
        add (D0_CAPSULE_DIR + "d0_capsule_valve.png") xysize (config.screen_width, config.screen_height)
        if mode == "alarm":
            add (D0_CAPSULE_DIR + "d0_capsule_led_red.png") xysize (config.screen_width, config.screen_height) at d0_capsule_led_warning
        elif mode == "startup":
            add (D0_CAPSULE_DIR + "d0_capsule_led_gray.png") xysize (config.screen_width, config.screen_height)
            add (D0_CAPSULE_DIR + "d0_capsule_led_green.png") xysize (config.screen_width, config.screen_height) at d0_capsule_valve_start
        else:
            add (D0_CAPSULE_DIR + "d0_capsule_led_green.png") xysize (config.screen_width, config.screen_height) at d0_capsule_led_normal

