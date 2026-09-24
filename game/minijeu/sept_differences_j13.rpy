# Mini-jeu du jour 13 — comparer le dessin original de Juliette à sa copie.

default j13_sd_found = []

init -2 python:
    J13_SD_BASE = "images/minigame/sept_differences/dessin_juliette.png"
    J13_SD_OVERLAYS = (
        "images/minigame/sept_differences/yeux_juliette.png",
        "images/minigame/sept_differences/yeux_peluche.png",
        "images/minigame/sept_differences/coeur_saigne.png",
        "images/minigame/sept_differences/cicatrice_juliette.png",
    )

    # Coordonnées dans l'image source 1374x1145. Les zones sont volontairement
    # un peu plus larges que les traits afin de rester confortables à la souris.
    J13_SD_DIFFERENCES = (
        {"id": "yeux_juliette", "x": 590, "y": 458, "w": 230, "h": 150},
        {"id": "yeux_peluche", "x": 944, "y": 587, "w": 130, "h": 130},
        {"id": "coeur", "x": 908, "y": 344, "w": 130, "h": 170},
        {"id": "cicatrice", "x": 610, "y": 366, "w": 150, "h": 100},
    )

    J13_SD_IMAGE_W = 740
    J13_SD_IMAGE_H = 617
    J13_SD_ORIGINAL_X = 116
    J13_SD_COPY_X = 1064
    J13_SD_IMAGE_Y = 210

    def j13_sd_screen_rect(diff, origin_x):
        scale_x = float(J13_SD_IMAGE_W) / 1374.0
        scale_y = float(J13_SD_IMAGE_H) / 1145.0
        width = int(diff["w"] * scale_x)
        height = int(diff["h"] * scale_y)
        center_x = origin_x + int(diff["x"] * scale_x)
        center_y = J13_SD_IMAGE_Y + int(diff["y"] * scale_y)
        return (center_x - width // 2, center_y - height // 2, width, height)

    def j13_sd_add_found(diff_id):
        if diff_id not in store.j13_sd_found:
            store.j13_sd_found = store.j13_sd_found + [diff_id]


screen j13_sept_differences_screen(interactive=True, reaction_text=None, reaction_title="NOAM"):
    modal True
    zorder 220

    default hovered_diff = None

    add Solid("#05070B")
    add Solid("#0D1822") xsize 1920 ysize 150
    add Solid("#7FD8EE55") xsize 1920 ysize 2 ypos 149

    text "LES 7 DIFFÉRENCES":
        xpos 82
        ypos 38
        size 42
        color "#F1F6F8"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "Retrouve les 4 détails qui ont été ajoutés à la copie.":
        xpos 84
        ypos 91
        size 23
        color "#9FB9C4"

    text "[len(j13_sd_found)] / 4":
        xpos 1765
        ypos 49
        xanchor 1.0
        size 35
        color "#7FD8EE"
        font "fonts/Rajdhani-SemiBold.ttf"

    frame:
        xpos 110
        ypos 204
        xsize 752
        ysize 629
        padding (6, 6)
        background Solid("#D8E0DE")
        add Transform(J13_SD_BASE, size=(J13_SD_IMAGE_W, J13_SD_IMAGE_H))

    frame:
        xpos 1058
        ypos 204
        xsize 752
        ysize 629
        padding (6, 6)
        background Solid("#D8E0DE")
        fixed:
            xsize J13_SD_IMAGE_W
            ysize J13_SD_IMAGE_H
            add Transform(J13_SD_BASE, size=(J13_SD_IMAGE_W, J13_SD_IMAGE_H))
            for overlay_path in J13_SD_OVERLAYS:
                add Transform(overlay_path, size=(J13_SD_IMAGE_W, J13_SD_IMAGE_H))

    text "ORIGINAL":
        xpos 486
        ypos 166
        xanchor 0.5
        size 26
        color "#BAC8CE"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "COPIE RETROUVÉE":
        xpos 1434
        ypos 166
        xanchor 0.5
        size 26
        color "#F0C98A"
        font "fonts/Rajdhani-SemiBold.ttf"

    for diff in J13_SD_DIFFERENCES:
        if diff["id"] not in j13_sd_found and interactive:
            # Le joueur peut cliquer sur l'un ou l'autre dessin, comme dans un
            # jeu des différences classique. Les zones restent invisibles,
            # y compris au survol et lorsqu'elles reçoivent le focus.
            for hit_origin in (J13_SD_ORIGINAL_X, J13_SD_COPY_X):
                $ hit_rect = j13_sd_screen_rect(diff, hit_origin)
                button:
                    xpos hit_rect[0]
                    ypos hit_rect[1]
                    xsize hit_rect[2]
                    ysize hit_rect[3]
                    padding (0, 0)
                    background None
                    hover_background None
                    focus_mask None
                    keyboard_focus False
                    hovered SetScreenVariable("hovered_diff", diff["id"])
                    unhovered SetScreenVariable("hovered_diff", None)
                    action Return(diff["id"])

    frame:
        xpos 270
        ypos 875
        xsize 1380
        ysize 128
        padding (28, 18)
        background Solid("#0D1822EE")
        vbox:
            spacing 8
            text "OBSERVE LES DEUX DESSINS":
                xalign 0.5
                size 24
                color "#7FD8EE"
                font "fonts/Rajdhani-SemiBold.ttf"
            if reaction_text:
                text "[reaction_title]":
                    xalign 0.5
                    size 21
                    color "#F0C98A"
                    font "fonts/Rajdhani-SemiBold.ttf"
                text "[reaction_text]":
                    xalign 0.5
                    text_align 0.5
                    size 25
                    color "#F1F6F8"
            elif hovered_diff and hovered_diff not in j13_sd_found:
                text "Clique pour examiner ce détail.":
                    xalign 0.5
                    size 25
                    color "#F1F6F8"
            elif len(j13_sd_found) < 4:
                text "Les différences peuvent être sélectionnées sur l'original ou sur la copie.":
                    xalign 0.5
                    size 25
                    color "#B8C8CE"
            else:
                text "Les quatre différences sont identifiées.":
                    xalign 0.5
                    size 25
                    color "#B8FFD9"

    if reaction_text:
        key "dismiss" action Return(True)
        key "K_RETURN" action Return(True)
        key "K_SPACE" action Return(True)
        button:
            xpos 270
            ypos 875
            xsize 1380
            ysize 128
            padding (0, 0)
            background None
            hover_background None
            keyboard_focus False
            action Return(True)


label j13_sept_differences_run:
    $ j13_sd_found = []

    while len(j13_sd_found) < 4:
        call screen j13_sept_differences_screen(interactive=True)
        $ _j13_sd_choice = _return
        $ j13_sd_add_found(_j13_sd_choice)

        if _j13_sd_choice == "yeux_juliette":
            call _j13_sd_reaction_yeux_juliette
        elif _j13_sd_choice == "yeux_peluche":
            call _j13_sd_reaction_yeux_peluche
        elif _j13_sd_choice == "coeur":
            call _j13_sd_reaction_coeur
        elif _j13_sd_choice == "cicatrice":
            call _j13_sd_reaction_cicatrice

    call screen j13_sept_differences_screen(
        interactive=False,
        reaction_text="Quatre détails. Quatre ajouts volontaires."
    )
    return


label _j13_sd_reaction_yeux_juliette:
    play sound "audio/sfx_qte_hit.wav" volume 0.65
    call screen j13_sept_differences_screen(
        interactive=False,
        reaction_text="Ses yeux... Ils sont ouverts sur la copie. Je les avais dessinés fermés."
    )
    return


label _j13_sd_reaction_yeux_peluche:
    play sound "audio/sfx_qte_hit.wav" volume 0.65
    call screen j13_sept_differences_screen(
        interactive=False,
        reaction_text="La peluche aussi me regarde. Ce n'était pas comme ça."
    )
    return


label _j13_sd_reaction_coeur:
    play sound "audio/sfx_qte_hit.wav" volume 0.65
    call screen j13_sept_differences_screen(
        interactive=False,
        reaction_text="Le cœur saigne. Je n'avais jamais dessiné ça."
    )
    return


label _j13_sd_reaction_cicatrice:
    play sound "audio/sfx_exclamation_horror.mp3" volume 0.75
    call screen j13_sept_differences_screen(
        interactive=False,
        reaction_text="Une cicatrice... Elle n'était pas sur mon dessin. Personne ne peut savoir que Juliette en a une. Sa mèche la cachait toujours — pourtant, elle est là, sur la copie."
    )
    return
