# 30-second in-engine content preview; no story flags or J25 spoilers.
# Uses existing CGs, never bg_cg040 or the real J25 photo screen.
init python:
    import math

    # Each pan prioritizes the upper part of the CG (characters' faces),
    # instead of drifting toward torsos or empty corners of the scene.
    # Normalized coordinates refer to the original 1920x1080 CG.
    _KD_CP_SHOTS = (
        ("bg_cg006", (0.47, 0.36), (0.53, 0.29)),
        ("bg_cg014", (0.47, 0.32), (0.43, 0.26)),
        ("bg_cg025", (0.51, 0.34), (0.56, 0.29)),
    )

    def kd_cp_state(seconds):
        # 0-4 title; 4-20 camera demonstration (three pans + photos);
        # 20-26 photo contact-sheet; 26-30 end card.
        if seconds < 4.0:
            return -1, 0.0
        if seconds < 20.0:
            span = (seconds - 4.0) / 5.333333333
            return min(2, int(span)), span % 1.0
        return 3, 0.0

    def kd_cp_ease(t):
        t = max(0.0, min(1.0, t))
        return t * t * (3.0 - 2.0 * t)

    def kd_cp_camera(shot, local):
        # Camera pans vertically and horizontally at 2.2x zoom.
        first, second = shot[1], shot[2]
        t = kd_cp_ease(max(0.0, min(1.0, (local - 0.08) / 0.67)))
        return (first[0] + (second[0] - first[0]) * t,
                first[1] + (second[1] - first[1]) * t)

    def kd_cp_cursor(local):
        # A simulated cursor follows the pans, then lands on shutter.
        t = kd_cp_ease(max(0.0, min(1.0, (local - 0.08) / 0.65)))
        if local > 0.63:
            u = kd_cp_ease((local - 0.63) / 0.12)
            return (960 + (1670 - 960) * u, 520 + (925 - 520) * u)
        return (600 + 600 * t, 700 - 470 * t)

    def kd_cp_projection(center, zoom=2.2):
        # Integer pixel offsets for Transform at 1920x1080.
        # Clamp to avoid exposing the outside of the background.
        mx = 0.5 / zoom
        cx = max(mx, min(1.0 - mx, center[0]))
        cy = max(mx, min(1.0 - mx, center[1]))
        return (int(960 - cx * 1920 * zoom),
                int(540 - cy * 1080 * zoom))

screen content_preview():
    tag menu
    modal True
    zorder 250
    default elapsed = 0.0
    timer 0.05 repeat True action SetScreenVariable("elapsed", elapsed + 0.05)
    key "K_ESCAPE" action ShowMenu("main_menu")
    key "K_RETURN" action ShowMenu("main_menu")
    if elapsed >= 30.0:
        timer 0.01 action ShowMenu("main_menu")

    add Solid("#050A12")
    $ phase, local = kd_cp_state(elapsed)

    if phase == -1:
        text "KAMI'S DESIRES":
            align (0.5, 0.38) size 94 color "#E8F8FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            at kd_cp_fade
        text "CONTENT PREVIEW  /  PHOTO MODE":
            align (0.5, 0.54) size 31 color "#6BD8ED" kerning 4
        text "APERÇU DU CONTENU  /  MODE PHOTO":
            align (0.5, 0.59) size 20 color "#A0B6C3" kerning 2

    elif phase < 3:
        $ shot = _KD_CP_SHOTS[phase]
        $ center = kd_cp_camera(shot, local)
        $ offset = kd_cp_projection(center)
        add Transform(shot[0], zoom=2.2, xpos=offset[0], ypos=offset[1],
                      xanchor=0.0, yanchor=0.0)
        add Solid("#03101D33")

        # Framing overlay.
        for x, y, sx, sy in ((125, 130, 1, 1), (1795, 130, -1, 1),
                              (125, 850, 1, -1), (1795, 850, -1, -1)):
            add Solid("#E3F5F7CC") xpos (x if sx > 0 else x - 76) ypos y xsize 76 ysize 3
            add Solid("#E3F5F7CC") xpos x ypos (y if sy > 0 else y - 76) xsize 3 ysize 76
        add Solid("#DEEEF9AA") xpos 938 ypos 540 xsize 44 ysize 2
        add Solid("#DEEEF9AA") xpos 960 ypos 519 xsize 2 ysize 44

        frame:
            xpos 55 ypos 35 padding (20, 12) background Solid("#06101AE8")
            vbox:
                spacing 3
                text "PHOTO MODE  ·  EXPLORE THE IMAGE" size 27 color "#E2F8FF"
                text "MODE PHOTO  ·  EXPLOREZ L'IMAGE" size 17 color "#9FBBC9"
        frame:
            xpos 55 ypos 920 padding (20, 12) background Solid("#06101AE8")
            vbox:
                spacing 4
                text "MOVE YOUR CURSOR TO REFRAME" size 26 color "#E8F7FB"
                text "DÉPLACEZ LE CURSEUR POUR RECADRER" size 18 color "#A9C2CF"

        # Simulated mouse pointer, not the player's real mouse.
        $ mx, my = kd_cp_cursor(local)
        add Text("◆", size=34, color="#FFFFFF",
                 outlines=[(2, "#10232E", 0, 0)]) xpos int(mx) ypos int(my)

        frame:
            xpos 1605 ypos 894 padding (18, 12)
            background Solid("#07202BDC")
            text "●  SNAP / PHOTO" size 23 color "#D7F5FA"

        if 0.77 < local < 0.80:
            add Solid("#FFFFFFDD")
        if local >= 0.81:
            frame at kd_cp_photo_pop:
                align (0.5, 0.5)
                xsize 745 ysize 465
                padding (13, 13)
                background Solid("#F4F0E5")
                vbox:
                    spacing 9
                    add Transform(shot[0], xysize=(719, 404))
                    text "PHOTO CAPTURED / PHOTO PRISE":
                        xalign 0.5 size 20 color "#21333C"

    elif elapsed < 26.0:
        text "YOUR EVIDENCE. YOUR PERSPECTIVE.":
            align (0.5, 0.13) size 46 color "#EDF9FF"
        text "VOS PREUVES. VOTRE POINT DE VUE.":
            align (0.5, 0.19) size 23 color "#9DC5D5"
        for i, shot in enumerate(_KD_CP_SHOTS):
            frame at kd_cp_gallery_in(i * 0.3):
                xpos (130 + i * 565) ypos (302 + (35 if i == 1 else 0))
                xsize 525 ysize 346 padding (12, 12)
                background Solid("#EAE8DE")
                vbox:
                    spacing 13
                    add Transform(shot[0], xysize=(501, 282))
                    text ("CAPTURE %02d" % (i + 1)):
                        xalign 0.5 size 21 color "#293C47"
        text "THREE FRAMES. COUNTLESS QUESTIONS.":
            align (0.5, 0.79) size 32 color "#C9DFE6"
        text "TROIS CLICHÉS. D'INNOMBRABLES QUESTIONS.":
            align (0.5, 0.84) size 19 color "#91ABBA"
    else:
        text "KAMI'S DESIRES":
            align (0.5, 0.35) size 102 color "#F0FCFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            at kd_cp_fade
        text "ITCH.IO FREE GAME":
            align (0.5, 0.52) size 38 kerning 4 color "#77D7ED"
        text "JEU GRATUIT SUR ITCH.IO":
            align (0.5, 0.58) size 23 color "#B9D3DC"
        text "CONTENT PREVIEW  •  PHOTO MODE":
            align (0.5, 0.70) size 24 color "#E0E9EF"

    # Escape works throughout, including opening and closing cards.
    textbutton "✕  CLOSE / FERMER":
        xpos 1590 ypos 34 padding (14, 9)
        background Solid("#05131BAA") hover_background Solid("#124056DD")
        text_size 20 text_color "#BBD3DC" text_hover_color "#FFFFFF"
        action ShowMenu("main_menu")

transform kd_cp_fade:
    alpha 0.0
    ease 0.65 alpha 1.0

transform kd_cp_photo_pop:
    alpha 0.0 zoom 1.07 rotate -2
    ease 0.24 alpha 1.0 zoom 1.0

transform kd_cp_gallery_in(delay=0):
    alpha 0.0 yoffset 40
    pause delay
    ease 0.5 alpha 1.0 yoffset 0
