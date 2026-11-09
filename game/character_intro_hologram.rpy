# ------------------------------------------------------------
# CINEMATIQUE DE PRESENTATION DES REPRESENTANTS
# Jour 0 : Lysa ; jour 1 : les dix autres representants.
# Animation non interactive de 4 secondes, synchronisee avec
# les fiches existantes PROFILE_DATA (pas de donnees dupliquees).
# ------------------------------------------------------------

default kd_character_intro_seen = []

transform kd_intro_camera_push:
    subpixel True
    zoom 1.0
    xalign 0.5
    yalign 0.5
    easeout 0.45 zoom 1.085 xalign 0.34

transform kd_intro_camera_restore:
    subpixel True
    zoom 1.085
    xalign 0.34
    yalign 0.5
    easein 0.32 zoom 1.0 xalign 0.5

transform kd_intro_veil:
    alpha 0.0
    linear 0.18 alpha 1.0
    pause 3.37
    linear 0.45 alpha 0.0

transform kd_intro_character:
    subpixel True
    xalign 0.22
    yalign 1.0
    xoffset -95
    zoom 1.03
    alpha 0.0
    easeout 0.55 xoffset 0 zoom 1.15 alpha 1.0
    pause 2.96
    easein 0.46 xoffset -45 alpha 0.0

transform kd_intro_holo_panel:
    subpixel True
    xoffset 130
    alpha 0.0
    easeout 0.42 xoffset 0 alpha 1.0
    pause 3.11
    easein 0.47 xoffset 58 alpha 0.0

transform kd_intro_reveal(delay=0.7):
    subpixel True
    alpha 0.0
    xoffset 26
    pause delay
    easeout 0.27 alpha 1.0 xoffset 0

transform kd_intro_scanline:
    subpixel True
    alpha 0.0
    yoffset -210
    pause 0.22
    alpha 0.95
    linear 1.45 yoffset 290
    linear 0.28 alpha 0.0

transform kd_intro_hud_pulse:
    alpha 0.25
    linear 0.16 alpha 0.88
    linear 0.22 alpha 0.38
    repeat

screen kd_character_intro_screen(profile_id):
    modal True
    zorder 750

    $ info = PROFILE_DATA.get(profile_id, {})
    $ sw = config.screen_width
    $ sh = config.screen_height
    $ ui = min(float(sw) / 1920.0, float(sh) / 1080.0)
    $ px = int(sw * 0.505)
    $ py = int(sh * 0.15)
    $ pw = int(sw * 0.455)
    $ ph = int(sh * 0.70)
    $ border = max(2, int(3 * ui))

    # La scene d'origine reste derriere la projection.
    # Ce voile sombre dissocie le sprite anime de ceux du dialogue.
    add Solid("#020F1BD9") at kd_intro_veil

    # Trame technique tres discrete : pas de texture importee.
    for n in range(12):
        add Solid("#4CDDFE10"):
            xpos int(sw * (0.06 + n * 0.081))
            ypos int(sh * 0.07)
            xsize max(1, int(1 * ui))
            ysize int(sh * 0.86)
            at kd_intro_veil

    # Grand portrait sur la gauche ; ses proportions restent intactes.
    add character_image(profile_id, "neutre") at kd_intro_character

    # Hologramme a droite : vitre semi-transparente, contours cyan
    # et scan lumineux. Le texte n'est pas une image : il vient du profil.
    fixed:
        xpos px
        ypos py
        xsize pw
        ysize ph
        at kd_intro_holo_panel

        add Solid("#061C2BD9") xsize pw ysize ph
        add Solid("#42DEFF34") xpos 0 ypos 0 xsize border ysize ph
        add Solid("#42DEFF34") xpos pw-border ypos 0 xsize border ysize ph
        add Solid("#42DEFF78") xpos 0 ypos 0 xsize pw ysize border
        add Solid("#42DEFF78") xpos 0 ypos ph-border xsize pw ysize border

        # Angles de verrouillage plus epais.
        add Solid("#80F6FF") xpos 0 ypos 0 xsize int(pw*0.15) ysize border*2
        add Solid("#80F6FF") xpos 0 ypos 0 xsize border*2 ysize int(ph*0.14)
        add Solid("#80F6FF") xpos int(pw*0.84) ypos ph-border*2 xsize int(pw*0.16) ysize border*2
        add Solid("#80F6FF") xpos pw-border*2 ypos int(ph*0.86) xsize border*2 ysize int(ph*0.14)

        # Marqueurs lateraux de projection et segments de mesures.
        for k in range(7):
            add Solid("#48DFFF65"):
                xpos int(pw * 0.94)
                ypos int(ph * (0.20 + k * 0.095))
                xsize int(pw * (0.028 if k % 2 else 0.045))
                ysize max(2, int(3 * ui))
                at kd_intro_reveal(0.38 + k*0.07)

        add Solid("#99F9FF6F"):
            xpos int(pw*0.035)
            ypos int(ph*0.16)
            xsize int(pw*0.91)
            ysize max(2, int(3*ui))
            at kd_intro_scanline

        vbox:
            xpos int(pw * 0.065)
            ypos int(ph * 0.062)
            xsize int(pw * 0.82)
            spacing int(13 * ui)

            text "CONCLAVE // IDENTIFICATION":
                size max(13, int(19*ui))
                color "#6AD8EB"
                bold True
                at kd_intro_reveal(0.25)

            text info.get("name", profile_id).upper():
                size max(34, int(68*ui))
                color "#F3FFFF"
                bold True
                outlines [(max(1,int(2*ui)), "#38CFFF44", 0, 0)]
                at kd_intro_reveal(0.65)

            null height int(8*ui)

            hbox:
                spacing int(15*ui)
                at kd_intro_reveal(1.17)
                text "DISTRICT" size max(17,int(23*ui)) color "#76D5E9" xminimum int(310*ui)
                text info.get("district", "—").upper() size max(17,int(29*ui)) color "#FFFFFF" bold True

            add Solid("#3ED6EE46") xsize int(pw*0.82) ysize max(1,int(2*ui)) at kd_intro_reveal(1.23)

            hbox:
                spacing int(15*ui)
                at kd_intro_reveal(1.64)
                text "ÂGE" size max(17,int(23*ui)) color "#76D5E9" xminimum int(310*ui)
                text (info.get("age", "—") + " ANS") size max(17,int(29*ui)) color "#FFFFFF" bold True

            add Solid("#3ED6EE46") xsize int(pw*0.82) ysize max(1,int(2*ui)) at kd_intro_reveal(1.72)

            hbox:
                spacing int(15*ui)
                at kd_intro_reveal(2.11)
                text "TAILLE" size max(17,int(23*ui)) color "#76D5E9" xminimum int(310*ui)
                text info.get("height", "—") size max(17,int(29*ui)) color "#FFFFFF" bold True

            add Solid("#3ED6EE46") xsize int(pw*0.82) ysize max(1,int(2*ui)) at kd_intro_reveal(2.19)

            hbox:
                spacing int(15*ui)
                at kd_intro_reveal(2.58)
                text "TOUR DE POITRINE" size max(17,int(23*ui)) color "#76D5E9" xminimum int(310*ui)
                text info.get("chest", "—") size max(17,int(29*ui)) color "#FFFFFF" bold True

            null height int(9*ui)

            text "DOSSIER PERSONNEL   /   DONNEES CONFIRMEES":
                size max(12,int(17*ui))
                color "#74D9EB"
                at kd_intro_reveal(3.07)

    # Decompte fixe : aucune interaction/clic supplementaire.
    timer 4.0 action Return()

label kd_play_character_intro(profile_id):
    if profile_id in PROFILE_DATA and profile_id not in kd_character_intro_seen:
        $ kd_character_intro_seen.append(profile_id)
        window hide
        camera master at kd_intro_camera_push
        play sound sfx_beep
        call screen kd_character_intro_screen(profile_id)
        camera master at kd_intro_camera_restore
        window auto
    return
