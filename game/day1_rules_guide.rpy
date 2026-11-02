# Tutoriel Jour 1 - animations par textures PNG du pack fourni.
# Assets : game/images/ui/tutorial_conclave/guide_*.png
# Les boutons existants restent seuls interactifs ; les textures sont décoratives.
default day1_rules_stage = -1

transform conclave_guide_panel_arrive:
    alpha 0.0
    yoffset 18
    easeout 0.35 alpha 1.0 yoffset 0

transform conclave_guide_arrow_move:
    alpha 0.75
    xoffset -12
    easein 0.65 alpha 1.0 xoffset 5
    easeout 0.65 alpha 0.75 xoffset -12
    repeat

transform conclave_guide_focus_blink:
    alpha 0.45
    zoom 0.94
    easein 0.65 alpha 0.95 zoom 1.04
    easeout 0.65 alpha 0.45 zoom 0.94
    repeat

screen day1_rules_guided_reading():
    zorder 360
    modal False
    on "show" action SetVariable("day1_rules_stage", 0)

    # Les deux moyens ouvrent exactement la même tablette.
    if day1_rules_stage == 0:
        key "K_t" action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
    elif day1_rules_stage == 1 and not renpy.get_screen("tablet_home"):
        key "K_t" action Show("tablet_home")

    # Aucune reprise du dialogue avant la fermeture de la tablette.
    if day1_rules_stage == 3 and not renpy.get_screen("tablet_codex") and not renpy.get_screen("tablet_home"):
        timer 0.25 action Return()

    if day1_rules_stage in (0, 1, 2):
        # Panneau illustré : un seul visible à la fois.
        $ _step = day1_rules_stage + 1
        add "images/ui/tutorial_conclave/guide_step_%d.png" % _step:
            xpos 30 ypos 798 xysize (654, 175)
            at conclave_guide_panel_arrive

    if day1_rules_stage == 0:
        # Vrai bouton tablette du HUD (1920x1080) : ~1754, 157.
        add "images/ui/tutorial_conclave/guide_arrow.png":
            xpos 1560 ypos 85 xysize (160, 104)
            at conclave_guide_arrow_move
        add "images/ui/tutorial_conclave/guide_focus.png":
            xpos 1720 ypos 115 xysize (72, 80)
            at conclave_guide_focus_blink

    elif day1_rules_stage == 1 and renpy.get_screen("tablet_home"):
        # Icône CODEX : livre de la deuxième ligne de l'accueil tablette.
        add "images/ui/tutorial_conclave/guide_arrow.png":
            xpos 234 ypos 317 xysize (155, 100)
            at conclave_guide_arrow_move
        add "images/ui/tutorial_conclave/guide_focus.png":
            xpos 397 ypos 322 xysize (133, 139)
            at conclave_guide_focus_blink

    elif day1_rules_stage == 2 and renpy.get_screen("tablet_codex"):
        # Première carte de la colonne centrale (et non la colonne des PACKS).
        add "images/ui/tutorial_conclave/guide_arrow.png":
            xpos 525 ypos 248 xysize (151, 98)
            at conclave_guide_arrow_move
        add "images/ui/tutorial_conclave/guide_focus.png":
            xpos 678 ypos 253 xysize (150, 105)
            at conclave_guide_focus_blink
