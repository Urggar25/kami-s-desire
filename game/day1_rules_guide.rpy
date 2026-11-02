# Tutoriel interactif J1 : réutilise la vraie tablette et le vrai Codex.
# Les étapes sont enregistrées en variables de sauvegarde (pas en persistent).
default day1_rules_stage = -1

transform day1_rules_hint_pulse:
    alpha 0.65
    linear 0.65 alpha 1.0
    linear 0.65 alpha 0.65
    repeat

screen day1_rules_guided_reading():
    zorder 260
    modal False
    on "show" action SetVariable("day1_rules_stage", 0)
    if day1_rules_stage == 0:
        key "K_t" action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
    elif day1_rules_stage == 1:
        key "K_t" action Show("tablet_home")
    timer 0.15 repeat True action If(day1_rules_stage == 3, Return(), NullAction())

    frame:
        xpos 24 ypos 22 xsize 550
        padding (18, 14)
        background Solid("#061421F0")
        vbox:
            spacing 8
            text "GUIDE // RÈGLES DU CONCLAVE":
                size 23 color "#70DDFF" font "fonts/Rajdhani-SemiBold.ttf"
            if day1_rules_stage == 0:
                text "1 / 3 — Ouvrez votre tablette.":
                    size 19 color "#F1F9FF"
                textbutton "OUVRIR LA TABLETTE [[T]":
                    action [SetVariable("day1_rules_stage", 1), Show("tablet_home")]
                    text_size 19 text_color "#FFFFFF" background Solid("#13526C") hover_background Solid("#207C9D")
            elif day1_rules_stage == 1:
                text "2 / 3 — Touchez l'icône CODEX sur votre tablette.":
                    at day1_rules_hint_pulse
                    size 19 color "#F1F9FF"
                if not renpy.get_screen("tablet_home"):
                    textbutton "RÉOUVRIR LA TABLETTE [[T]":
                        action Show("tablet_home")
                        text_size 17 text_color "#FFFFFF" background Solid("#13526C") hover_background Solid("#207C9D")
            elif day1_rules_stage == 2:
                text "3 / 3 — Dans LE CONCLAVE, ouvrez « Règles du Conclave ».":
                    at day1_rules_hint_pulse
                    size 19 color "#F1F9FF"
                if not renpy.get_screen("tablet_codex"):
                    textbutton "RETOURNER AU CODEX":
                        action [Hide("tablet_home"), Show("tablet_codex")]
                        text_size 17 text_color "#FFFFFF" background Solid("#13526C") hover_background Solid("#207C9D")
            else:
                text "Règlement ouvert. Bonne lecture !":
                    size 19 color "#A2F2C9"
