# Terminal personnel du Conclave — ouverture/fermeture animées.
# Les quatre PNG sont des étapes successives de l'animation, et non
# quatre menus différents. L'écran reste modal pendant la fermeture.

transform tablet_stage_fade:
    alpha 0.0
    linear 0.15 alpha 1.0

screen tablet_home():
    modal True
    zorder 200

    default stage = 1
    default closing = False

    # Intercepte Échap pour refermer la tablette au lieu d'ouvrir le menu Ren'Py.
    key "K_ESCAPE" action SetScreenVariable("closing", True)
    key "K_t" action SetScreenVariable("closing", True)

    # Avance d'un visuel toutes les 0,18 seconde ; à la fermeture, inverse
    # exactement les étapes avant de rendre la main au jeu.
    if closing and stage == 1:
        timer 0.18 action Hide("tablet_home")
    elif closing:
        timer 0.18 action SetScreenVariable("stage", stage - 1)
    elif stage < 4:
        timer 0.18 action SetScreenVariable("stage", stage + 1)

    # La tablette est dessinée au format 1536 × 1024 (rapport 3:2).
    # Ce fixed garde l'image et ses zones de clic dans le même repère,
    # même si l'écran du jeu est en 16:9.
    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1620, 1080)

        if stage == 1:
            add "images/ui/tablette/tablette_1.png" xysize (1620, 1080) at tablet_stage_fade
        elif stage == 2:
            add "images/ui/tablette/tablette_2.png" xysize (1620, 1080) at tablet_stage_fade
        elif stage == 3:
            add "images/ui/tablette/tablette_3.png" xysize (1620, 1080) at tablet_stage_fade
        else:
            add "images/ui/tablette/tablette_4.png" xysize (1620, 1080) at tablet_stage_fade

        # Les zones de clic ne deviennent actives qu'après l'ouverture.
        # Positionnées sur les boutons déjà dessinés dans tablette_4.png.
        if stage == 4 and not closing:
            hotspot (1043, 658, 145, 147) action OpenURL("https://discord.gg/RyN4CZCeRE")
            hotspot (1187, 680, 164, 122) action SetScreenVariable("closing", True)
