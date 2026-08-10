# ============================================================
# MINI-JEU JOUR 11 - CONSULTATION_CAMERAS
#
# Contexte :
# Noam accede au systeme de Kami dans la salle d'observation
# pour consulter les archives video de la veille.
#
# Assets image attendus, a deposer de ton cote :
#   images/background/bg_camera_14h_cafe.png
#   images/background/bg_camera_14h_maintenance.png
#   images/background/bg_camera_14h_conclave.png
#   images/background/bg_camera_14h_couloir.png
#   images/background/bg_camera_15h_cafe.png
#   images/background/bg_camera_15h_maintenance.png
#   images/background/bg_camera_15h_conclave.png
#   images/background/bg_camera_15h_couloir.png
#   images/background/bg_camera_16h_cafe.png
#   images/background/bg_camera_16h_maintenance.png
#   images/background/bg_camera_16h_conclave.png
#   images/background/bg_camera_16h_couloir_doppel.png
#
# Si un asset n'existe pas encore, le lecteur affiche l'ecran
# "pas d'activite" au lieu de provoquer une erreur Ren'Py.
# ============================================================


default seen_16h_couloir = False

default camera_selected_time = "14h00"
default camera_selected_room = "cafe"
default camera_current_image = None
default camera_current_active = False
default camera_current_message = "Selectionne une heure et une salle, puis lance la lecture."
default camera_current_timestamp = "--:--:--"
default camera_current_room_label = "Aucune camera"


init python:
    CAMERA_TIMES = ["14h00", "15h00", "16h00"]

    CAMERA_ROOMS = [
        ("maintenance", "Salle de maintenance", "MAINTENANCE"),
        ("cafe", "Cafeteria", "CAFETERIA"),
        ("conclave", "Salle du Conclave", "CONCLAVE"),
        ("couloir", "Couloir (Stockage)", "COULOIR STOCKAGE"),
    ]

    CAMERA_ROOM_LABELS = dict((room_id, label) for room_id, label, _ in CAMERA_ROOMS)
    CAMERA_ROOM_CODES = dict((room_id, code) for room_id, _, code in CAMERA_ROOMS)

    # Noms d'images Ren'Py attendus. Les fichiers .png places dans images/
    # peuvent porter exactement ces noms sans extension.
    CAMERA_IMAGE_NAMES = {}
    for _time in CAMERA_TIMES:
        _prefix = _time.replace("h00", "h")
        for _room_id, _label, _code in CAMERA_ROOMS:
            CAMERA_IMAGE_NAMES[(_time, _room_id)] = "bg_camera_%s_%s" % (_prefix, _room_id)

    CAMERA_IMAGE_NAMES[("14h00", "cafe")] = "bg_camera_14h_cafe"
    CAMERA_IMAGE_NAMES[("15h00", "cafe")] = "bg_camera_15h_cafe"
    CAMERA_IMAGE_NAMES[("16h00", "cafe")] = "bg_camera_16h_cafe"
    CAMERA_IMAGE_NAMES[("16h00", "couloir")] = "bg_camera_16h_couloir_doppel"

    def camera_asset_exists(image_name):
        return bool(image_name and renpy.has_image(image_name))

    def camera_get_displayable(image_name):
        if camera_asset_exists(image_name):
            return image_name
        return Solid("#05080d")

    def camera_lookup_image(time_id, room_id):
        return CAMERA_IMAGE_NAMES.get((time_id, room_id), None)

    def camera_is_special_selection():
        return store.camera_selected_time == "16h00" and store.camera_selected_room == "couloir"

    def camera_make_timestamp(time_id):
        if time_id == "14h00":
            return "J10 14:00:27"
        if time_id == "15h00":
            return "J10 15:00:41"
        if time_id == "16h00":
            return "J10 16:00:13"
        return "J10 --:--:--"

    def camera_view_selection():
        time_id = store.camera_selected_time
        room_id = store.camera_selected_room
        image_name = camera_lookup_image(time_id, room_id)

        store.camera_current_image = image_name
        store.camera_current_timestamp = camera_make_timestamp(time_id)
        store.camera_current_room_label = CAMERA_ROOM_CODES.get(room_id, "CAMERA INCONNUE")

        if image_name and camera_asset_exists(image_name):
            store.camera_current_active = True
            store.camera_current_message = "Archive chargee. Lecture du segment %s - %s." % (
                time_id,
                CAMERA_ROOM_LABELS.get(room_id, "Salle inconnue"),
            )
        else:
            store.camera_current_active = False
            store.camera_current_message = "Il n'y avait pas d'activite a ce moment la."


transform camera_rec_blink:
    alpha 1.0
    pause 0.45
    alpha 0.15
    pause 0.30
    repeat

transform camera_feed_breathe:
    xoffset 0
    yoffset 0
    linear 0.10 xoffset 1 yoffset 0
    linear 0.10 xoffset -1 yoffset 1
    linear 0.12 xoffset 0 yoffset -1
    linear 0.12 xoffset 0 yoffset 0
    repeat

transform camera_doppel_glitch:
    xoffset 0
    yoffset 0
    linear 0.06 xoffset 4 yoffset -2
    linear 0.06 xoffset -5 yoffset 2
    linear 0.08 xoffset 2 yoffset 1
    linear 0.10 xoffset 0 yoffset 0
    pause 0.35
    repeat

transform camera_scan_drift:
    yoffset -1080
    linear 4.0 yoffset 0
    repeat


style camera_ui_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#d9f7ff"
    outlines [(1, "#031016dd", 0, 1)]

style camera_title_text is camera_ui_text:
    size 42
    color "#f0fbff"

style camera_section_text is camera_ui_text:
    size 25
    color "#85dfff"

style camera_button_text is camera_ui_text:
    size 25
    xalign 0.5
    yalign 0.5

style camera_small_text is camera_ui_text:
    size 22
    color "#a9e8ff"


label _11_0_1_3_MINIJEU_CAMERAS:

    $ camera_selected_time = "14h00"
    $ camera_selected_room = "cafe"
    $ camera_current_image = None
    $ camera_current_active = False
    $ camera_current_message = "Selectionne une heure et une salle, puis lance la lecture."
    $ camera_current_timestamp = "--:--:--"
    $ camera_current_room_label = "Aucune camera"

    call screen camera_browser()

    if _return == "doppel":
        $ seen_16h_couloir = True
        call screen camera_doppel_reveal()
        jump _11_0_1_1_CONFRONTATION_KAMI

    return


screen camera_browser():
    modal True
    zorder 80

    add "bg_observation" at adaptive_fullscreen
    add Solid("#020914cc")

    # Panneau principal : interface froide, bleue et semi-transparente.
    frame:
        xpos 54
        ypos 46
        xsize 1812
        ysize 988
        background Frame(Solid("#061a2acc"), 18, 18)
        padding (26, 22, 26, 22)

        vbox:
            spacing 18

            hbox:
                xfill True
                text "Archives de Surveillance - Jour 10" style "camera_title_text"
                null width 20
                text "KAMI / OBSERVATION_SYS" style "camera_small_text" xalign 1.0

            add Solid("#54d8ff88", xysize=(1760, 2))

            hbox:
                spacing 28

                # Colonne gauche : choix des salles et horaires.
                vbox:
                    xsize 880
                    spacing 18

                    text "SELECTION CAMERA" style "camera_section_text"

                    grid 2 2:
                        spacing 22
                        xsize 880
                        ysize 610

                        for room_id, room_label, room_code in CAMERA_ROOMS:
                            button:
                                xsize 426
                                ysize 288
                                background Solid("#0a2030bb")
                                hover_background Solid("#123a52dd")
                                selected_background Solid("#0e5f78dd")
                                selected (camera_selected_room == room_id)
                                action [Play("sound", sfx_beep), SetVariable("camera_selected_room", room_id)]

                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 10
                                    text room_code style "camera_section_text" xalign 0.5
                                    text room_label style "camera_button_text" xalign 0.5
                                    add Solid("#69e7ff88", xysize=(210, 2)) xalign 0.5

                    text "TRANCHE HORAIRE" style "camera_section_text"

                    hbox:
                        spacing 24
                        for time_id in CAMERA_TIMES:
                            button:
                                xsize 190
                                ysize 76
                                background Solid("#071c2bbb")
                                hover_background Solid("#123a52dd")
                                selected_background Solid("#0e5f78dd")
                                selected (camera_selected_time == time_id)
                                action [Play("sound", sfx_beep), SetVariable("camera_selected_time", time_id)]

                                text time_id style "camera_button_text"

                    textbutton "VISIONNER":
                        xsize 250
                        ysize 72
                        background Solid("#39c7eacc")
                        hover_background Solid("#89f2ffdd")
                        text_style "camera_button_text"
                        text_color "#031016"
                        text_hover_color "#031016"
                        action If(
                            camera_is_special_selection(),
                            [Play("sound", sfx_gresillement), SetVariable("seen_16h_couloir", True), Return("doppel")],
                            [Play("sound", sfx_gresillement), Function(camera_view_selection)]
                        )

                # Colonne droite : lecteur camera.
                vbox:
                    xsize 852
                    spacing 18

                    frame:
                        xsize 852
                        ysize 664
                        background Solid("#02070bcc")
                        padding (0, 0, 0, 0)

                        fixed:
                            xysize (852, 664)

                            if camera_current_image and camera_current_active:
                                add camera_get_displayable(camera_current_image):
                                    xysize (852, 664)
                                    at camera_feed_breathe
                                use camera_feed_overlay(camera_current_timestamp, camera_current_room_label, 852, 664)
                            else:
                                add Solid("#03070c")
                                add Solid("#17202a")
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 16
                                    text "Il n'y avait pas d'activite a ce moment la.":
                                        style "camera_title_text"
                                        xalign 0.5
                                        color "#e5eef5"
                                    text "ARCHIVE NOIRE / SIGNAL INEXPLOITABLE":
                                        style "camera_small_text"
                                        xalign 0.5
                                        color "#6f8b99"

                    frame:
                        xsize 852
                        ysize 174
                        background Solid("#061a2acc")
                        padding (26, 20, 26, 20)

                        vbox:
                            spacing 12
                            text "COMMENTAIRE DE NOAM" style "camera_section_text"
                            text camera_current_message:
                                style "camera_ui_text"
                                size 30
                                color "#eefaff"
                                xmaximum 790


screen camera_feed_overlay(timestamp, room_label, feed_w=1920, feed_h=1080):
    fixed:
        xysize (feed_w, feed_h)

        # Balayage et lignes de scan animees.
        fixed at camera_scan_drift:
            for y in range(0, feed_h * 2, 8):
                add Solid("#d8fbff10", xysize=(feed_w, 1)) ypos y

        add Solid("#001d2a33")

        hbox:
            xpos 28
            ypos 24
            spacing 16
            text "REC" style "camera_section_text" color "#ff394d" at camera_rec_blink
            text timestamp style "camera_section_text"
            text room_label style "camera_section_text" color "#ffffff"

        text "CAM-ARCHIVE / VIDEO BUFFER 94%":
            xpos 28
            ypos 58
            style "camera_small_text"
            color "#9eeeff"

        add Solid("#6cecff99", xysize=(84, 2)) xpos 20 ypos 20
        add Solid("#6cecff99", xysize=(2, 84)) xpos 20 ypos 20
        add Solid("#6cecff99", xysize=(84, 2)) xpos (feed_w - 104) ypos 20
        add Solid("#6cecff99", xysize=(2, 84)) xpos (feed_w - 22) ypos 20
        add Solid("#6cecff99", xysize=(84, 2)) xpos 20 ypos (feed_h - 22)
        add Solid("#6cecff99", xysize=(2, 84)) xpos 20 ypos (feed_h - 104)
        add Solid("#6cecff99", xysize=(84, 2)) xpos (feed_w - 104) ypos (feed_h - 22)
        add Solid("#6cecff99", xysize=(2, 84)) xpos (feed_w - 22) ypos (feed_h - 104)


screen camera_doppel_reveal():
    modal True
    zorder 95

    timer 5.0 action Return(True)

    add camera_get_displayable("bg_camera_16h_couloir_doppel"):
        xysize (1920, 1080)
        at camera_doppel_glitch

    # Doubles tres legers pour donner une sensation de glitch sans asset dedie.
    add camera_get_displayable("bg_camera_16h_couloir_doppel"):
        xysize (1920, 1080)
        alpha 0.16
        xoffset -8
    add camera_get_displayable("bg_camera_16h_couloir_doppel"):
        xysize (1920, 1080)
        alpha 0.12
        xoffset 8

    add Solid("#001b2a44")
    use camera_feed_overlay("J10 16:00:13", "COULOIR STOCKAGE", 1920, 1080)

    text "ANOMALIE DETECTEE":
        xpos 70
        ypos 970
        style "camera_title_text"
        color "#ff4058"
        at camera_rec_blink
