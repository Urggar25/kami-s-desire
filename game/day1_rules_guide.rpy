# Guidage visuel Jour 1 — balises HUD précises, sans glyphes de flèche.
default day1_rules_stage = -1

transform rules_marker_breathe:
    alpha 0.65
    linear 0.65 alpha 1.0
    linear 0.65 alpha 0.65
    repeat

# Pointe dessinée par deux traits inclinés (aucune dépendance à une police).
screen rules_guide_pointer(x, y, w, h, direction="left"):
    fixed:
        xpos x ypos y xysize (w, h)
        # Cadre léger qui englobe uniquement la vraie cible interactive.
        add Solid("#60DDFE") xpos 0 ypos 0 xsize w ysize 2
        add Solid("#60DDFE") xpos 0 ypos (h - 2) xsize w ysize 2
        add Solid("#60DDFE") xpos 0 ypos 0 xsize 2 ysize h
        add Solid("#60DDFE") xpos (w - 2) ypos 0 xsize 2 ysize h

screen day1_rules_guided_reading():
    zorder 360
    modal False
    on "show" action SetVariable("day1_rules_stage", 0)
    if day1_rules_stage == 0:
        key "K_t" action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
    elif day1_rules_stage == 1 and not renpy.get_screen("tablet_home"):
        key "K_t" action Show("tablet_home")

    if day1_rules_stage == 3 and not renpy.get_screen("tablet_codex") and not renpy.get_screen("tablet_home"):
        timer 0.25 action Return()

    if day1_rules_stage == 0:
        # Position dérivée du HUD 330px aligné à droite : icône tablette en 1er.
        use rules_guide_pointer(1495, 110, 57, 47)
        fixed:
            xpos 1195 ypos 122 xysize (285, 70)
            text "OUVRIR LA TABLETTE":
                xpos 0 ypos 3 size 21 color "#F1FBFF"
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(2, "#071421", 0, 0)]
            text "Cliquez sur l'icône ou appuyez sur T":
                xpos 0 ypos 31 size 16 color "#B9E9F6"
                font "fonts/Barlow-Light.ttf"
                outlines [(2, "#071421", 0, 0)]
            add Solid("#60DDFE") xpos 270 ypos 17 xsize 20 ysize 2 at rules_marker_breathe
    elif day1_rules_stage == 1 and renpy.get_screen("tablet_home"):
        # Icône Codex : seconde rangée, tout à gauche de la vraie tablette.
        use rules_guide_pointer(369, 284, 129, 127)
        fixed:
            xpos 510 ypos 313 xysize (250, 77)
            add Solid("#60DDFE") xpos 0 ypos 24 xsize 24 ysize 2 at rules_marker_breathe
            text "OUVRIR LE CODEX":
                xpos 39 ypos 4 size 22 color "#F1FBFF"
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(2, "#071421", 0, 0)]
            text "Sélectionnez cette application":
                xpos 39 ypos 34 size 15 color "#B9E9F6"
                font "fonts/Barlow-Light.ttf"
                outlines [(2, "#071421", 0, 0)]
    elif day1_rules_stage == 2 and renpy.get_screen("tablet_codex"):
        # Première carte de la colonne ENTRÉES (maquette tablette en 1920x1080).
        use rules_guide_pointer(438, 229, 251, 63)
        fixed:
            xpos 710 ypos 233 xysize (270, 66)
            add Solid("#60DDFE") xpos 0 ypos 23 xsize 24 ysize 2 at rules_marker_breathe
            text "RÈGLES DU CONCLAVE":
                xpos 36 ypos 5 size 21 color "#F1FBFF"
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(2, "#071421", 0, 0)]
            text "Ouvrez cette entrée":
                xpos 36 ypos 34 size 15 color "#B9E9F6"
                font "fonts/Barlow-Light.ttf"
                outlines [(2, "#071421", 0, 0)]
    # L'aide disparaît complètement dès que l'entrée est ouverte.
