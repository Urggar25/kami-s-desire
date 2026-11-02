# J1 — guidage par un seul repère contextuel à la fois.
# Positions calibrées sur les écrans 1920x1080, d'après les captures de jeu.
default day1_rules_stage = -1

transform day1_guide_pulse:
    alpha 0.42
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.42
    repeat

transform day1_guide_nudge:
    yoffset -8
    linear 0.6 yoffset 0
    linear 0.6 yoffset -8
    repeat

# Pointe fine dessinée avec des segments, pas avec des caractères spéciaux.
screen day1_guide_marker(cx, cy, caption, label_x, label_y):
    # La cible est matérialisée par 4 coins discontinus, sans carré plein.
    fixed:
        xpos cx - 39 ypos cy - 37 xysize (78, 74)
        at day1_guide_pulse
        add Solid("#73E4FF") xpos 0 ypos 0 xsize 15 ysize 2
        add Solid("#73E4FF") xpos 0 ypos 0 xsize 2 ysize 15
        add Solid("#73E4FF") xpos 63 ypos 0 xsize 15 ysize 2
        add Solid("#73E4FF") xpos 76 ypos 0 xsize 2 ysize 15
        add Solid("#73E4FF") xpos 0 ypos 72 xsize 15 ysize 2
        add Solid("#73E4FF") xpos 0 ypos 59 xsize 2 ysize 15
        add Solid("#73E4FF") xpos 63 ypos 72 xsize 15 ysize 2
        add Solid("#73E4FF") xpos 76 ypos 59 xsize 2 ysize 15

    # Flèche vers le bas : tige + deux branches géométriques.
    fixed:
        xpos cx - 14 ypos cy - 95 xysize (30, 52)
        at day1_guide_nudge
        add Solid("#E8FBFF") xpos 13 ypos 0 xsize 3 ysize 36
        add Transform(Solid("#E8FBFF", xysize=(3, 19)), rotate=-45) xpos 7 ypos 29
        add Transform(Solid("#E8FBFF", xysize=(3, 19)), rotate=45) xpos 19 ypos 29

    text caption:
        xpos label_x ypos label_y
        size 18 color "#ECFAFF"
        font "fonts/Rajdhani-SemiBold.ttf"
        outlines [(2, "#071421", 0, 0)]

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
        # Premier vrai bouton du HUD (coin supérieur droit).
        use day1_guide_marker(1755, 159, "CLIQUEZ ICI OU APPUYEZ SUR T", 1450, 206)
    elif day1_rules_stage == 1 and renpy.get_screen("tablet_home"):
        # Icône livre CODEX sur la deuxième rangée.
        use day1_guide_marker(467, 395, "OUVRIR LE CODEX", 502, 432)
    elif day1_rules_stage == 2 and renpy.get_screen("tablet_codex"):
        # Première fiche de la colonne centrale, PAS le pack de gauche.
        use day1_guide_marker(800, 328, "RÈGLES DU CONCLAVE", 840, 370)
    # Après le clic sur la fiche, aucun guide n'est superposé à la lecture.
