# CONTENT PREVIEW — CODED KNOCK (30s, cinematic non-interactive demonstration).
# The real J25 game evaluates intervals: three rapid knocks, two slow knocks.
# This animation makes the press/release and the waiting intervals readable.
# No story or save variables are touched.

init python:
    # Relative timings of each demonstration. Each entry is a press (start, duration).
    # Visual "long" emphasis represents the slower spacing between knocks,
    # matching the actual minigame's timing-based rule.
    _KD_KNOCK_BAD = ((0.85, 0.16), (1.16, 0.16), (1.48, 0.16),
                     (1.80, 0.16), (2.10, 0.16))
    _KD_KNOCK_GOOD = ((0.70, 0.15), (1.04, 0.15), (1.39, 0.15),
                      (2.49, 0.22), (3.66, 0.22))

    def kd_kp_beats(t, beats):
        return sum(1 for start, dur in beats if t >= start + dur)

    def kd_kp_pressed(t, beats):
        return any(start <= t < start + dur for start, dur in beats)

    def kd_kp_last(t, beats):
        previous = [(i, start, dur) for i, (start, dur) in enumerate(beats) if t >= start]
        return previous[-1] if previous else None

    def kd_kp_scene(t):
        if t < 3.4:
            return "intro", t
        if t < 7.5:
            return "learn", t - 3.4
        if t < 14.8:
            return "wrong", t - 7.5
        if t < 22.7:
            return "correct", t - 14.8
        if t < 26.3:
            return "warning", t - 22.7
        return "end", t - 26.3

transform kd_kp_reveal:
    alpha 0.0 yoffset 20
    ease 0.45 alpha 1.0 yoffset 0

transform kd_kp_pulse:
    alpha 0.45
    ease 0.42 alpha 0.95
    ease 0.42 alpha 0.45
    repeat

screen content_preview_knock():
    tag menu
    modal True
    zorder 250
    default elapsed = 0.0
    timer 0.05 repeat True action SetScreenVariable("elapsed", elapsed + 0.05)
    key "K_ESCAPE" action ShowMenu("content_preview_hub")
    key "K_RETURN" action ShowMenu("content_preview_hub")
    if elapsed >= 30.0:
        timer 0.01 action ShowMenu("content_preview_hub")

    $ phase, local = kd_kp_scene(elapsed)
    $ bad_phase = phase == "wrong"
    $ good_phase = phase == "correct"
    $ demo = bad_phase or good_phase
    $ beats = _KD_KNOCK_BAD if bad_phase else _KD_KNOCK_GOOD
    $ playing = kd_kp_pressed(local, beats) if demo else False
    $ count = kd_kp_beats(local, beats) if demo else 0
    $ complete = bad_phase and local >= 3.3 or good_phase and local >= 4.5
    $ wrong = bad_phase and local >= 3.3
    $ passed = good_phase and local >= 4.5

    add Solid("#030A12")
    add Solid("#10202B") xpos 0 ypos 0 xsize 1920 ysize 1080
    add Solid("#070C15") xpos 0 ypos 0 xsize 1920 ysize 1080 alpha 0.55
    # Vertical seams and doorframe: abstract Conclave airlock, no J25 footage.
    add Solid("#172C39") xpos 336 ypos 0 xsize 8 ysize 1080
    add Solid("#223B45") xpos 1559 ypos 0 xsize 8 ysize 1080
    add Solid("#263E4A") xpos 482 ypos 125 xsize 960 ysize 748
    add Solid("#0B1724") xpos 493 ypos 136 xsize 938 ysize 726
    add Solid("#1B3944") xpos 525 ypos 167 xsize 874 ysize 668
    add Solid("#071522") xpos 535 ypos 177 xsize 854 ysize 648
    # Keypad/access panel.
    add Solid("#315063") xpos 1310 ypos 417 xsize 130 ysize 216
    add Solid("#04121B") xpos 1321 ypos 428 xsize 108 ysize 194
    add Solid("#59B9BD" if passed else ("#D96868" if wrong else "#294F61")) xpos 1342 ypos 462 xsize 66 ysize 10
    add Solid("#7CBABBAA") xpos 1340 ypos 530 xsize 70 ysize 2
    text "LOCK / 07" xpos 1346 ypos 567 size 15 color "#A5C4D0" font "fonts/Rajdhani-SemiBold.ttf"

    # Atmosphere and top-level production treatment.
    add Solid("#57BFD6") xpos 80 ypos 80 xsize 78 ysize 3
    text "KAMI.CORE  /  ACCESS PROTOCOL":
        xpos 80 ypos 104 size 23 kerning 3 color "#9FC8D5"
        font "fonts/Rajdhani-SemiBold.ttf"
    text "CONTENT PREVIEW  02/02":
        xpos 80 ypos 146 size 19 kerning 2 color "#75939F"

    if phase == "intro":
        add Solid("#020A13D8")
        text "A SECRET KNOCK.":
            xalign 0.5 ypos 312 size 94 color "#F3F8F8"
            font "fonts/Rajdhani-SemiBold.ttf" at kd_kp_reveal
        text "UN CODE FRAPPÉ À LA PORTE.":
            xalign 0.5 ypos 434 size 36 color "#9BCCD6" at kd_kp_reveal
        add Solid("#74C9D7") xpos 772 ypos 540 xsize 376 ysize 3
        text "REMEMBER THE PATTERN.":
            xalign 0.5 ypos 594 size 39 color "#E1F3F5"
        text "MÉMORISEZ LE RYTHME.":
            xalign 0.5 ypos 648 size 25 color "#A4BEC8"

    elif phase == "learn":
        text "EVERY BEAT MATTERS":
            xalign 0.5 ypos 236 size 56 color "#F0F7F8"
            font "fonts/Rajdhani-SemiBold.ttf"
        text "CHAQUE COUP COMPTE":
            xalign 0.5 ypos 300 size 29 color "#A9C5CE"
        for i in range(5):
            $ x = 660 + 150 * i
            add Solid("#315D68") xpos x ypos 427 xsize 92 ysize 92
            add Solid("#071522") xpos (x + 6) ypos 433 xsize 80 ysize 80
            text ("•" if i < 3 else "—"):
                xpos (x + 46) ypos 438 xanchor 0.5 size 57 color ("#77D3C0" if i < 3 else "#F6DBA3")
        text "3 QUICK BEATS                 2 SLOW BEATS":
            xalign 0.5 ypos 566 size 32 color "#E7F2F1"
        text "3 COUPS RAPIDES                 2 COUPS LENTS":
            xalign 0.5 ypos 615 size 23 color "#AFCCD1"
        text "LISTEN. WAIT. KNOCK.":
            xalign 0.5 ypos 733 size 32 color "#6CCBDD" at kd_kp_pulse
        text "ÉCOUTEZ. ATTENDEZ. FRAPPEZ.":
            xalign 0.5 ypos 779 size 20 color "#A2BFC7"

    elif demo:
        # Lights, a pulsing contact target, the on-screen cue and explicit beat history.
        add Solid("#020811BB") xpos 551 ypos 207 xsize 812 ysize 570
        add Solid("#071B27") xpos 666 ypos 300 xsize 588 ysize 338
        add Solid("#132C37") xpos 676 ypos 310 xsize 568 ysize 318
        text ("ATTEMPT 01 / ESSAI 01" if bad_phase else "ATTEMPT 02 / ESSAI 02"):
            xalign 0.5 ypos 224 size 26 color "#ABC9D1" kerning 3
        $ disk_color = "#A6E0D1" if playing else "#466671"
        add Solid(disk_color) xpos 864 ypos 336 xsize 192 ysize 192
        add Solid("#0C2731") xpos (875 if playing else 886) ypos (347 if playing else 358) xsize (170 if playing else 148) ysize (170 if playing else 148)
        text ("KNOCK!" if playing else "WAIT..."):
            xalign 0.5 ypos 398 size 44 color ("#C8FFF0" if playing else "#94B5C0")
            font "fonts/Rajdhani-SemiBold.ttf"
        text ("FRAPPEZ !" if playing else "ATTENDEZ..."):
            xalign 0.5 ypos 465 size 20 color "#A5CAD0"

        # Progress pattern: filled beat = performed. Long separation is highlighted.
        for i in range(5):
            $ bx = 690 + i * 132
            $ c = "#83E0C5" if i < count else ("#E9D9A4" if i == count else "#456571")
            add Solid(c) xpos bx ypos 588 xsize (81 if i < 3 else 102) ysize (9 if i < count else 4)
            text ("%02d" % (i + 1)):
                xpos (bx + 42) ypos 607 xanchor 0.5 size 17 color "#9DBAC3"
        if local >= 2.0 and bad_phase and not wrong:
            text "TOO FAST!" xalign 0.5 ypos 675 size 37 color "#F2B8AC"
            text "TROP RAPIDE !" xalign 0.5 ypos 720 size 23 color "#DBA19A"
        if wrong:
            add Solid("#A7353B55")
            text "ACCESS DENIED":
                xalign 0.5 ypos 725 size 66 color "#FF9898"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "ACCÈS REFUSÉ":
                xalign 0.5 ypos 802 size 30 color "#E6B1B1"
        elif passed:
            add Solid("#40A78333")
            text "CODE ACCEPTED":
                xalign 0.5 ypos 725 size 66 color "#9BF3D9"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "CODE ACCEPTÉ":
                xalign 0.5 ypos 802 size 30 color "#A7DCCE"
        else:
            text "WATCH THE PAUSES / OBSERVEZ LES PAUSES":
                xalign 0.5 ypos 724 size 25 color "#BCD2D7"

    elif phase == "warning":
        add Solid("#030912D7")
        text "DON'T FORGET THE CODE.":
            xalign 0.5 ypos 305 size 78 color "#F4F7F8"
            font "fonts/Rajdhani-SemiBold.ttf" at kd_kp_reveal
        text "N'OUBLIEZ PAS LE CODE.":
            xalign 0.5 ypos 422 size 35 color "#BAD1D7"
        add Solid("#E7BE86") xpos 710 ypos 533 xsize 500 ysize 3
        text "ONE WRONG BEAT CAN CHANGE EVERYTHING.":
            xalign 0.5 ypos 592 size 32 color "#EED8B6"
        text "UN SEUL MAUVAIS COUP PEUT TOUT CHANGER.":
            xalign 0.5 ypos 642 size 22 color "#BDAE9F"

    else:
        add Solid("#020711E5")
        text "KAMI'S DESIRES":
            xalign 0.5 ypos 327 size 107 color "#F1FBFE"
            font "fonts/Rajdhani-SemiBold.ttf" at kd_kp_reveal
        text "ITCH.IO FREE GAME":
            xalign 0.5 ypos 503 size 43 color "#77D3DF" kerning 4
        text "JEU GRATUIT SUR ITCH.IO":
            xalign 0.5 ypos 563 size 25 color "#ADCCD3"
        text "CODED KNOCK / CODE SECRET":
            xalign 0.5 ypos 717 size 29 color "#E9F0EF"

    # Playback progress / unambiguous close, consistent with photo preview.
    add Solid("#24404F") xpos 55 ypos 1020 xsize 1810 ysize 4
    add Solid("#7ACED4") xpos 55 ypos 1020 xsize int(1810 * min(elapsed / 30.0, 1.0)) ysize 4
    textbutton "CLOSE / FERMER":
        xpos 1580 ypos 45 padding (16, 8)
        background Solid("#05131BE8") hover_background Solid("#145061")
        text_size 21 text_color "#BFD4DC" text_hover_color "#FFFFFF"
        action ShowMenu("content_preview_hub")
