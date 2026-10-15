# Tablette du Conclave : quatre phases en fondu (0,5 s chacune).
# Vue modale ouverte via Show("tablet_home"), refermée via Hide("tablet_home").
# Les zones de clic sont des buttons, jamais des hotspots hors imagemap.

transform tablet_stage_fade:
    alpha 0.0
    linear 0.5 alpha 1.0

screen tablet_home():
    modal True
    zorder 200

    default stage = 1
    default closing = False

    key "K_ESCAPE" action SetScreenVariable("closing", True)
    key "K_t" action SetScreenVariable("closing", True)

    # Horloge stable : chaque phase reste 0,5 s. Une fois en phase 4,
    # on attend une action utilisateur ; en fermeture on parcourt 4 -> 1.
    timer 0.5 repeat True action If(
        closing,
        If(stage <= 1,
            Hide("tablet_home"),
            SetScreenVariable("stage", stage - 1)),
        If(stage < 4,
            SetScreenVariable("stage", stage + 1),
            NullAction())
    )

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

        # L'image est centrée avec fit contain. Les boutons ci-dessous
        # englobent les icônes Discord et EXIT visibles en bas à droite.
        # Un fond quasi-transparent rend toute la surface réceptrice du clic.
        if stage == 4 and not closing:
            button:
                xpos 1160 ypos 640
                xsize 220 ysize 245
                padding (0, 0)
                background Solid("#FFFFFF01")
                hover_background Solid("#FFFFFF08")
                action OpenURL("https://discord.gg/RyN4CZCeRE")

            button:
                xpos 1380 ypos 645
                xsize 230 ysize 245
                padding (0, 0)
                background Solid("#FFFFFF01")
                hover_background Solid("#FFFFFF08")
                action SetScreenVariable("closing", True)
