# Jour 1 — flèches contextuelles sur les vrais contrôles de l'interface.
# Ne substitue aucun écran : le joueur doit ouvrir la tablette, le Codex, puis l'entrée.
default day1_rules_stage = -1

transform day1_rules_arrow_bounce:
    alpha 0.98
    xoffset -12
    linear 0.55 xoffset 0
    linear 0.55 xoffset -12
    repeat

transform day1_rules_arrow_down:
    alpha 0.98
    yoffset -12
    linear 0.55 yoffset 0
    linear 0.55 yoffset -12
    repeat

screen day1_rules_guided_reading():
    zorder 360
    modal False
    on "show" action SetVariable("day1_rules_stage", 0)

    # Le raccourci T et le bouton réel du HUD déclenchent la même transition.
    if day1_rules_stage == 0:
        key "K_t" action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
    elif day1_rules_stage == 1 and not renpy.get_screen("tablet_home"):
        key "K_t" action Show("tablet_home")

    # Ne pas reprendre le dialogue tant que la lecture est en cours.
    if day1_rules_stage == 3 and not renpy.get_screen("tablet_codex") and not renpy.get_screen("tablet_home"):
        timer 0.25 action Return()

    if day1_rules_stage == 0:
        # HUD coin supérieur droit : premier bouton de la rangée, sous JOUR.
        text "▼":
            xpos 1733 ypos 152 size 68 color "#74E5FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#062334", 0, 0)]
            at day1_rules_arrow_down
        text "TABLETTE  ·  OU TOUCHE T":
            xpos 1350 ypos 198 size 19 color "#F2FBFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#00121D", 0, 0)]
    elif day1_rules_stage == 1 and renpy.get_screen("tablet_home"):
        # Le bouton CODEX est une icône sur la tablette existante.
        # La flèche ne capte pas les clics : c'est le vrai imagebutton.
        text "➤":
            xpos 1100 ypos 580 size 74 color "#74E5FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#062334", 0, 0)]
            at day1_rules_arrow_bounce
        text "CODEX":
            xpos 1025 ypos 660 size 24 color "#FFFFFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#00121D", 0, 0)]
    elif day1_rules_stage == 2 and renpy.get_screen("tablet_codex"):
        # Première entrée de la liste LE CONCLAVE, sur la vitre inclinée.
        text "➤":
            xpos 480 ypos 264 size 66 color "#74E5FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#062334", 0, 0)]
            at day1_rules_arrow_bounce
        text "RÈGLES DU CONCLAVE":
            xpos 465 ypos 339 size 20 color "#FFFFFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#00121D", 0, 0)]
    elif day1_rules_stage == 3 and (renpy.get_screen("tablet_codex") or renpy.get_screen("tablet_home")):
        text "RÈGLEMENT OUVERT  —  REFERMEZ LA TABLETTE POUR CONTINUER":
            xalign 0.5 ypos 925 size 19 color "#ACF6D8"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#00121D", 0, 0)]
