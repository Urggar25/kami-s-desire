# =============================================================================
# ECRAN DE FIN — KAMI'S DESIRES
# =============================================================================
# Écran réutilisable pour les fins scénarisées.
# Appel :
#     call screen kd_ending_reached("Nom de la fin", "ENDING 01 // JOUR 20")
# =============================================================================

transform kd_ending_title_in:
    alpha 0.0
    yoffset 24
    pause 0.18
    easeout 0.65 alpha 1.0 yoffset 0

transform kd_ending_meta_in:
    alpha 0.0
    pause 0.42
    easeout 0.55 alpha 1.0

transform kd_ending_button_in:
    alpha 0.0
    yoffset 12
    pause 0.78
    easeout 0.45 alpha 1.0 yoffset 0

transform kd_ending_scan:
    alpha 0.07
    yoffset -1080
    linear 7.0 yoffset 1080
    repeat


style kd_ending_menu_button is button:
    xsize 360
    ysize 62
    padding (24, 0, 24, 0)
    background Fixed(
        Solid("#140a0de8"),
        Solid("#7f2430", xsize=5),
        Solid("#ffffff0d", ysize=1),
        Solid("#c93a4d22", ysize=2, yalign=1.0),
    )
    hover_background Fixed(
        Solid("#261015f5"),
        Solid("#e35a6c", xsize=7),
        Solid("#e35a6c44", ysize=2),
        Solid("#e35a6c", ysize=3, yalign=1.0),
    )


style kd_ending_menu_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 25
    color "#b98f96"
    hover_color "#ffffff"
    kerning 2.0
    xalign 0.5
    yalign 0.5


screen kd_ending_reached(ending_name, ending_code, ending_label="ENDING"):

    modal True

    key "game_menu" action NullAction()

    add Solid("#020305")
    add Solid("#26080d88")

    add Transform(
        "gui/main_menu_kami/glyph_kami.png",
        size=(760, 760),
        matrixcolor=TintMatrix("#781a28")
    ):
        xalign 0.5
        yalign 0.47
        alpha 0.10

    add "gui/main_menu_kami/scanlines.png" at kd_ending_scan
    add "gui/main_menu_kami/vignette.png" alpha 0.82

    # Filets techniques / interface KAMI.CORE.
    add Solid("#d64b5d20", xsize=2) xpos 165
    add Solid("#d64b5d20", xsize=2) xpos 1755
    add Solid("#d64b5d22", ysize=2) ypos 128
    add Solid("#d64b5d22", ysize=2) ypos 902

    text "KAMI.CORE // CONCLUSION":
        font "fonts/Barlow-Light.ttf"
        size 18
        color "#7f4a52"
        kerning 4
        xpos 170
        ypos 82

    text ending_code:
        font "fonts/Rajdhani-SemiBold.ttf"
        size 19
        color "#8f5962"
        kerning 3
        xanchor 1.0
        xpos 1750
        ypos 82
        at kd_ending_meta_in

    vbox:
        xalign 0.5
        yalign 0.43
        spacing 16
        xmaximum 1420
        at kd_ending_title_in

        text ending_label:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 28
            color "#d64b5d"
            kerning 9
            xalign 0.5
            textalign 0.5

        add Solid("#d64b5d88", xsize=840, ysize=2) xalign 0.5

        text ending_name:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 78
            color "#f3e7e9"
            outlines [(2, "#120206cc", 0, 2)]
            kerning 2.5
            xalign 0.5
            textalign 0.5

        text _("Cette issue a été atteinte."):
            font "fonts/Barlow-Light.ttf"
            size 21
            color "#8d777b"
            kerning 1.5
            xalign 0.5
            textalign 0.5

    fixed:
        xalign 0.5
        yalign 0.82
        xysize (360, 62)
        at kd_ending_button_in

        textbutton _("MENU PRINCIPAL"):
            style "kd_ending_menu_button"
            action Return(True)

    text "KAMI'S DESIRES":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 112
        color "#d64b5d08"
        kerning 8
        xalign 0.5
        ypos 865
