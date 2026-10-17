# Tablette du Conclave — 4 étapes en fondus CROISÉS.
# La phase 4 remplace la phase 3, sans image noire sous la tablette.
# L'accueil est ouvert avec Show("tablet_home") depuis le HUD.

transform tablet_phase_fade(duration=0.3):
    alpha 0.0
    linear duration alpha 1.0

transform tablet_phase_fade_out(duration=0.2):
    alpha 1.0
    linear duration alpha 0.0

screen tablet_home():
    modal True
    zorder 200

    default stage = 1
    default closing = False
    default phase_tick = 0

    key "K_ESCAPE" action [SetScreenVariable("closing", True), SetScreenVariable("phase_tick", 0)]
    key "K_t" action [SetScreenVariable("closing", True), SetScreenVariable("phase_tick", 0)]

    # Horloge unique (0,1 s) : 3 ticks par phase ordinaire,
    # 2 ticks pour 3 -> 4 à l'ouverture et 4 -> 3 à la fermeture.
    # La phase terminée demeure visible jusqu'à une vraie action utilisateur.
    if closing:
        timer 0.1 repeat True action If(
            phase_tick >= (1 if stage == 4 else 2),
            [SetScreenVariable("phase_tick", 0),
             If(stage == 1, Hide("tablet_home"), SetScreenVariable("stage", stage - 1))],
            SetScreenVariable("phase_tick", phase_tick + 1)
        )
    elif stage < 4:
        timer 0.1 repeat True action If(
            phase_tick >= (1 if stage == 3 else 2),
            [SetScreenVariable("phase_tick", 0), SetScreenVariable("stage", stage + 1)],
            SetScreenVariable("phase_tick", phase_tick + 1)
        )

    fixed:
        xysize (1920, 1080)

        # Le calque inférieur reste à 100 % pendant le fondu du supérieur.
        # Ainsi, aucun trou visuel n'apparaît entre deux étapes.
        if closing:
            if stage == 4:
                add "images/ui/tablette/tablette_4.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade_out(0.2)
            elif stage == 3:
                add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080)
                add "images/ui/tablette/tablette_2.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.3)
            elif stage == 2:
                add "images/ui/tablette/tablette_2.png" fit "contain" xysize (1920, 1080)
                add "images/ui/tablette/tablette_1.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.3)
            else:
                add "images/ui/tablette/tablette_1.png" fit "contain" xysize (1920, 1080)
        elif stage == 1:
            add "images/ui/tablette/tablette_1.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.3)
        elif stage == 2:
            add "images/ui/tablette/tablette_1.png" fit "contain" xysize (1920, 1080)
            add "images/ui/tablette/tablette_2.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.3)
        elif stage == 3:
            add "images/ui/tablette/tablette_2.png" fit "contain" xysize (1920, 1080)
            add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.3)
        else:
            add "images/ui/tablette/tablette_4.png" fit "contain" xysize (1920, 1080) at tablet_phase_fade(0.2)

        # Même repère 1920x1080 et même fondu que tablette_4.
        # Les PNG sont des skins de boutons (pas de rectangle Solid).
        # IMPORTANT : les fichiers d'icônes peuvent contenir des marges
        # transparentes ; focus_mask True rendrait alors le clic impossible
        # si les pixels opaques sont hors de la zone visuellement attendue.
        if stage == 4 and not closing:
            # Les icones sont des calques 1536x1024 transparents alignes sur
            # la maquette complete. Le focus alpha limite le clic a l'icone.
            imagebutton:
                idle Transform(
                    "images/ui/tablette/messagerie_notif.png" if messenger_has_pending() else "images/ui/tablette/messagerie.png",
                    xysize=(1920, 1080), fit="contain"
                )
                hover Transform(
                    "images/ui/tablette/messagerie_notif.png" if messenger_has_pending() else "images/ui/tablette/messagerie.png",
                    xysize=(1920, 1080), fit="contain", matrixcolor=BrightnessMatrix(0.18)
                )
                xpos 0 ypos 0
                xsize 1920 ysize 1080
                focus_mask True
                at tablet_phase_fade(0.2)
                action If(
                    messenger_has_pending(),
                    [Hide("tablet_home"), Show("messenger_conversation"), With(Dissolve(0.25))],
                    Function(messenger_no_recent)
                )

            imagebutton:
                idle Transform(
                    "images/ui/tablette/profil.png",
                    xysize=(1920, 1080), fit="contain"
                )
                hover Transform(
                    "images/ui/tablette/profil.png",
                    xysize=(1920, 1080), fit="contain", matrixcolor=BrightnessMatrix(0.18)
                )
                xpos 0 ypos 0
                xsize 1920 ysize 1080
                focus_mask True
                at tablet_phase_fade(0.2)
                action [Hide("tablet_home"), Show("tablet_profiles"), With(Dissolve(0.25))]

            # Dossier de vote : même navigation que le profil, avec l'icône de la tablette.
            # Le contenu et les déblocages restent ceux du dossier de vote existant.
            imagebutton:
                idle Transform(
                    "images/ui/tablette/dossier.png",
                    xysize=(1920, 1080), fit="contain"
                )
                hover Transform(
                    "images/ui/tablette/dossier.png",
                    xysize=(1920, 1080), fit="contain", matrixcolor=BrightnessMatrix(0.18)
                )
                xpos 0 ypos 0
                xsize 1920 ysize 1080
                focus_mask True
                at tablet_phase_fade(0.2)
                action [Hide("tablet_home"), Show("vote_dossier"), With(Dissolve(0.25))]

            # Statistiques : application intégrée à la vitre de la tablette.
            imagebutton:
                idle Transform(
                    "images/ui/tablette/stats.png",
                    xysize=(1920, 1080), fit="contain"
                )
                hover Transform(
                    "images/ui/tablette/stats.png",
                    xysize=(1920, 1080), fit="contain", matrixcolor=BrightnessMatrix(0.18)
                )
                xpos 0 ypos 0
                xsize 1920 ysize 1080
                focus_mask True
                at tablet_phase_fade(0.2)
                action [Hide("tablet_home"), Show("tablet_stats"), With(Dissolve(0.25))]

            imagebutton:
                idle Transform("images/ui/tablette/codex.png", xysize=(1920, 1080), fit="contain")
                hover Transform("images/ui/tablette/codex.png", xysize=(1920, 1080), fit="contain", matrixcolor=BrightnessMatrix(0.18))
                xpos 0 ypos 0
                xsize 1920 ysize 1080
                focus_mask True
                at tablet_phase_fade(0.2)
                action [Hide("tablet_home"), Show("tablet_codex"), With(Dissolve(0.25))]

            imagebutton:
                idle Transform("images/ui/tablette/discord.png", xysize=(150, 150), fit="contain")
                hover Transform("images/ui/tablette/discord.png", xysize=(150, 150), fit="contain")
                xpos 1210 ypos 650
                xsize 150 ysize 150
                at tablet_phase_fade(0.2)
                action OpenURL("https://discord.gg/RyN4CZCeRE")

            imagebutton:
                idle Transform("images/ui/tablette/exit.png", xysize=(130, 75), fit="contain")
                hover Transform("images/ui/tablette/exit.png", xysize=(130, 75), fit="contain")
                xpos 1215 ypos 832
                xsize 130 ysize 75
                at tablet_phase_fade(0.2)
                action [SetScreenVariable("closing", True), SetScreenVariable("phase_tick", 0)]
