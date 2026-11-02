# Tutoriel de navigation contextuel — Jour 1.
# Aucune fenêtre opaque sur les personnages : aide discrète et contextuelle.
default day1_rules_stage = -1

transform day1_rules_soft_pulse:
    alpha 0.78
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.78
    repeat

screen day1_rules_guided_reading():
    zorder 260
    modal False
    on "show" action SetVariable("day1_rules_stage", 0)
    if day1_rules_stage == 0:
        key "K_t" action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
    elif day1_rules_stage == 1 and not renpy.get_screen("tablet_home"):
        key "K_t" action Show("tablet_home")
    # Reprise du récit seulement après la vraie consultation, tablette fermée.
    if day1_rules_stage == 3 and not renpy.get_screen("tablet_codex") and not renpy.get_screen("tablet_home"):
        timer 0.25 action Return()

    if day1_rules_stage == 0:
        frame:
            xalign 0.98 ypos 182 xsize 350
            padding (18, 14)
            background Solid("#071929F2")
            vbox:
                spacing 8
                text "01  /  TABLETTE":
                    size 20 color "#67d9ff" font "fonts/Rajdhani-SemiBold.ttf"
                text "Accédez aux informations du Conclave.":
                    xmaximum 315 size 16 color "#edf8ff"
                textbutton "OUVRIR  ·  T":
                    action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
                    text_font "fonts/Rajdhani-SemiBold.ttf" text_size 19 text_color "#ffffff"
                    background Solid("#126080") hover_background Solid("#248cac")
    elif day1_rules_stage == 1:
        frame:
            xalign 0.5 ypos 870 xsize 590
            padding (16, 12)
            background Solid("#071929F0")
            at day1_rules_soft_pulse
            hbox:
                spacing 16
                text "02  /  CODEX":
                    size 21 color "#67d9ff" font "fonts/Rajdhani-SemiBold.ttf"
                text "Sur la tablette, sélectionnez l'application CODEX.":
                    xmaximum 365 size 17 color "#f1f8ff"
            if not renpy.get_screen("tablet_home"):
                textbutton "RÉOUVRIR LA TABLETTE":
                    xalign 0.97 ypos 49
                    action Show("tablet_home")
                    text_size 14 text_color "#8ce4ff" background None
    elif day1_rules_stage == 2:
        frame:
            xalign 0.5 ypos 880 xsize 710
            padding (15, 12)
            background Solid("#071929F0")
            at day1_rules_soft_pulse
            hbox:
                spacing 16
                text "03  /  RÈGLEMENT":
                    size 20 color "#67d9ff" font "fonts/Rajdhani-SemiBold.ttf"
                text "LE CONCLAVE  →  Règles du Conclave":
                    size 17 color "#f1f8ff"
            if not renpy.get_screen("tablet_codex"):
                textbutton "REVENIR AU CODEX":
                    xalign 0.97 ypos 46
                    action [Hide("tablet_home"), Show("tablet_codex")]
                    text_size 14 text_color "#8ce4ff" background None
    elif day1_rules_stage == 3:
        if renpy.get_screen("tablet_codex") or renpy.get_screen("tablet_home"):
            frame:
                xalign 0.5 ypos 880 xsize 650
                padding (16, 13)
                background Solid("#071929F0")
                hbox:
                    spacing 15
                    text "✓  RÈGLEMENT CONSULTÉ":
                        size 20 color "#9cebd0" font "fonts/Rajdhani-SemiBold.ttf"
                    text "Prenez le temps de lire, puis fermez la tablette.":
                        size 16 color "#f1f8ff"
