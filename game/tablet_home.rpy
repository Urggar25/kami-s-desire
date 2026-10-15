# Terminal du Conclave. Les PNG représentent quatre étapes d'une même animation.
# Le HUD de jour se rafraîchit toutes les 0,10 s : éviter les timers
# conditionnels de 0,18 s, qui peuvent être réinitialisés à chaque rafraîchissement.

transform tablet_stage_fade:
    alpha 0.0
    linear 0.045 alpha 1.0

screen tablet_home():
    modal True
    zorder 200

    default stage = 1
    default closing = False

    key "K_ESCAPE" action SetScreenVariable("closing", True)
    key "K_t" action SetScreenVariable("closing", True)

    # Timer récurrent unique, plus court que l'actualisation du HUD.
    # Il traverse les interactions sans être recréé à chaque étape.
    timer 0.05 repeat True action If(
        closing,
        If(stage <= 1,
            Hide("tablet_home"),
            SetScreenVariable("stage", stage - 1)),
        If(stage < 4,
            SetScreenVariable("stage", stage + 1),
            NullAction())
    )

    # Le canevas correspond au jeu (1920x1080), pas à la taille des PNG.
    # L'image entière est visible et centrée, sans déformation de son ratio.
    fixed:
        xysize (1920, 1080)

        if stage == 1:
            add "images/ui/tablette/tablette_1.png" fit "contain" xysize (1920, 1080) at tablet_stage_fade
        elif stage == 2:
            add "images/ui/tablette/tablette_2.png" fit "contain" xysize (1920, 1080) at tablet_stage_fade
        elif stage == 3:
            add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080) at tablet_stage_fade
        else:
            add "images/ui/tablette/tablette_4.png" fit "contain" xysize (1920, 1080) at tablet_stage_fade

        # Zones cliquables à vérifier en jeu par rapport aux PNG affichés.
        # Repère 1920x1080, tablette mise à l'échelle en conservant le ratio.
        if stage == 4 and not closing:
            button:
                xpos 1175 ypos 655
                xsize 165 ysize 150
                background None
                action OpenURL("https://discord.gg/RyN4CZCeRE")
            button:
                xpos 1340 ypos 676
                xsize 180 ysize 130
                background None
                action SetScreenVariable("closing", True)
