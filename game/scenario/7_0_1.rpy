default j701_table_choice = "aucun"
default j701_lysa_worry = False
default j701_lysa_search_help = False
default j701_iris_defense = False
default j701_tomas_informed = False
default j701_nyra_sorting = "standard"
default j701_plate_result = -1
default j701_julian_rapport = "neutre"
default j701_evidence_note = False
default j701_tomas_secret_kept = True
default j701_console_rings = []
default j701_console_locked = []
default j701_console_error_ticks = []
default j701_console_errors = 0
default j701_console_noise = 0
default j701_console_feedback = ""
default j701_console_phase = "play"

transform j701_elen_hop:
    yoffset 0
    easeout 0.13 yoffset -80
    easein 0.16 yoffset 0
    easeout 0.12 yoffset -45
    easein 0.14 yoffset 0

transform j701_console_panels:
    on show:
        alpha 0.0
        easeout 0.35 alpha 1.0
    on hide:
        ease 0.55 alpha 0.0

transform j701_console_result:
    alpha 0.0
    yoffset 18
    pause 0.35
    easeout 0.65 alpha 1.0 yoffset 0

transform j701_console_result_button:
    alpha 0.0
    pause 1.35
    easeout 0.45 alpha 1.0

transform j701_console_last_record:
    alpha 0.0
    pause 1.05
    easeout 0.4 alpha 1.0

transform j701_console_value_glitch:
    subpixel True
    block:
        xoffset -3
        alpha 0.82
        pause 0.05
        xoffset 3
        alpha 1.0
        pause 0.07
        xoffset 0
        pause 0.22
        repeat

transform j701_console_value_unstable:
    subpixel True
    block:
        xoffset 0
        pause 0.42
        xoffset -1
        pause 0.04
        xoffset 1
        pause 0.04
        xoffset 0
        pause 0.58
        repeat

init python:
    import math

    J701_CONSOLE_MODULES = [
        {"name": "NORD", "values": ["31", "48", "ERR", "7", "0"]},
        {"name": "SUD", "values": ["ERR", "16", "SYNC", "42", "0"]},
        {"name": "EST", "values": ["8", "23", "61", "ERR", "0"]},
        {"name": "OUEST", "values": ["SYNC", "12", "3", "55", "0"]},
    ]

    J701_CONSOLE_CENTERS = [
        (310, 315),
        (310, 705),
        (1610, 315),
        (1610, 705),
    ]

    try:
        renpy.music.register_channel("j701_console_ambience", mixer="sfx", loop=True)
        renpy.music.register_channel("j701_console_fx", mixer="sfx", loop=False)
    except Exception:
        pass

    def j701_console_reset():
        store.j701_console_rings = [0, 0, 0, 0]
        store.j701_console_locked = [False, False, False, False]
        store.j701_console_error_ticks = [0, 0, 0, 0]
        store.j701_console_errors = 0
        store.j701_console_noise = 64
        store.j701_console_feedback = "SIGNAL MONDIAL INSTABLE"
        store.j701_console_phase = "play"
        if renpy.loadable("audio/sfx_static.mp3"):
            renpy.music.play(
                "audio/sfx_static.mp3",
                channel="j701_console_ambience",
                loop=True,
                fadein=0.45,
                relative_volume=0.24,
            )

    def j701_console_locked_count():
        return sum(1 for locked in store.j701_console_locked if locked)

    def j701_console_value(index):
        if index >= len(J701_CONSOLE_MODULES):
            return "--"
        rings = store.j701_console_rings
        ring = rings[index] if index < len(rings) else 0
        values = J701_CONSOLE_MODULES[index]["values"]
        return values[ring % len(values)]

    def j701_console_cycle(index, direction=1):
        if store.j701_console_phase != "play":
            return
        if index < len(store.j701_console_locked) and store.j701_console_locked[index]:
            return
        rings = list(store.j701_console_rings)
        while len(rings) < len(J701_CONSOLE_MODULES):
            rings.append(0)
        rings[index] = (rings[index] + direction) % len(J701_CONSOLE_MODULES[index]["values"])
        store.j701_console_rings = rings
        value = j701_console_value(index)
        store.j701_console_feedback = kd_tr("{} // VALEUR {} SÉLECTIONNÉE").format(kd_tr(J701_CONSOLE_MODULES[index]["name"]), value)
        if renpy.loadable("audio/sfx_metal_clank.mp3"):
            renpy.play("audio/sfx_metal_clank.mp3", channel="sound", relative_volume=0.34)
        if value == "ERR" and renpy.loadable("audio/sfx_glitch.mp3"):
            renpy.play("audio/sfx_glitch.mp3", channel="j701_console_fx", relative_volume=0.62)
        elif value == "SYNC" and renpy.loadable("audio/sfx_gresillement.mp3"):
            renpy.play("audio/sfx_gresillement.mp3", channel="j701_console_fx", relative_volume=0.46)
        renpy.restart_interaction()

    def j701_console_calibrate(index):
        if store.j701_console_phase != "play":
            return
        locked = list(store.j701_console_locked)
        while len(locked) < len(J701_CONSOLE_MODULES):
            locked.append(False)
        if locked[index]:
            return

        value = j701_console_value(index)
        module_name = J701_CONSOLE_MODULES[index]["name"]
        if value != "0":
            errors = list(store.j701_console_error_ticks)
            while len(errors) < len(J701_CONSOLE_MODULES):
                errors.append(0)
            errors[index] = 11
            store.j701_console_error_ticks = errors
            store.j701_console_errors += 1
            store.j701_console_feedback = kd_tr("{} // CALIBRATION REFUSÉE — SIGNAL INSTABLE").format(kd_tr(module_name))
            if renpy.loadable("audio/sfx_qte_miss.wav"):
                renpy.play("audio/sfx_qte_miss.wav", channel="sound", relative_volume=0.72)
            if renpy.loadable("audio/sfx_glitch.mp3"):
                renpy.play("audio/sfx_glitch.mp3", channel="j701_console_fx", relative_volume=0.55)
            renpy.restart_interaction()
            return

        locked[index] = True
        store.j701_console_locked = locked
        locked_count = j701_console_locked_count()
        store.j701_console_noise = max(0, 64 - locked_count * 16)
        store.j701_console_feedback = kd_tr("{} // FLUX STABILISÉ").format(kd_tr(module_name))
        if renpy.loadable("audio/trailer/trl_sub_drop.wav"):
            renpy.play("audio/trailer/trl_sub_drop.wav", channel="sound", relative_volume=0.52)
        renpy.music.set_volume(max(0.03, 0.24 * (store.j701_console_noise / 64.0)), 0.35, channel="j701_console_ambience")

        if locked_count == len(J701_CONSOLE_MODULES):
            store.j701_console_phase = "silence"
            store.j701_console_feedback = "SIGNAL MONDIAL STABILISÉ"
            renpy.music.stop(channel="j701_console_ambience", fadeout=0.18)
            renpy.music.stop(channel="j701_console_fx", fadeout=0.1)
            renpy.music.set_pause(True, channel="music")
        renpy.restart_interaction()

    def j701_console_tick():
        errors = list(store.j701_console_error_ticks)
        changed = False
        for index in range(len(errors)):
            if errors[index] > 0:
                errors[index] -= 1
                changed = True
        if changed:
            store.j701_console_error_ticks = errors
            renpy.restart_interaction()

    def j701_console_begin_reveal():
        if store.j701_console_phase != "silence":
            return
        store.j701_console_phase = "reveal"
        renpy.restart_interaction()

    def j701_console_cleanup():
        renpy.music.stop(channel="j701_console_ambience", fadeout=0.15)
        renpy.music.stop(channel="j701_console_fx", fadeout=0.1)
        renpy.music.set_pause(False, channel="music")

    def j701_console_arc(canvas, color, center, radius, start_angle, end_angle, width=2, steps=32):
        cx, cy = center
        previous = None
        for step in range(steps + 1):
            ratio = step / float(steps)
            angle = start_angle + (end_angle - start_angle) * ratio
            point = (
                int(cx + math.cos(angle) * radius),
                int(cy + math.sin(angle) * radius),
            )
            if previous is not None:
                canvas.line(color, previous, point, width)
            previous = point

    def j701_console_ellipse(canvas, color, center, rx, ry, width=1, steps=52):
        cx, cy = center
        previous = None
        for step in range(steps + 1):
            angle = (math.pi * 2.0 * step) / float(steps)
            point = (
                int(cx + math.cos(angle) * rx),
                int(cy + math.sin(angle) * ry),
            )
            if previous is not None:
                canvas.line(color, previous, point, width)
            previous = point

    class J701ConsoleNetwork(renpy.Displayable):
        def __init__(self, **kwargs):
            super(J701ConsoleNetwork, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            result = renpy.Render(1920, 1080)
            canvas = result.canvas()
            locked = list(store.j701_console_locked)
            while len(locked) < 4:
                locked.append(False)
            paths = [
                [(468, 315), (610, 315), (704, 410),],
                [(468, 705), (610, 705), (704, 610),],
                [(1452, 315), (1310, 315), (1216, 410),],
                [(1452, 705), (1310, 705), (1216, 610),],
            ]
            for index, points in enumerate(paths):
                active = locked[index]
                glow = "#77ef9ccc" if active else "#39bff066"
                core = "#b9ffd0" if active else "#8adeff"
                for segment in range(1, len(points)):
                    canvas.line("#061f30dd", points[segment - 1], points[segment], 13)
                    canvas.line(glow, points[segment - 1], points[segment], 5 if active else 3)
                    canvas.line(core, points[segment - 1], points[segment], 1)
                pulse = 8 + int(3 * (math.sin(st * 4.0 + index) * 0.5 + 0.5))
                canvas.circle(glow, points[-1], pulse, 2)
                canvas.circle(core, points[-1], 3, 0)
            renpy.redraw(self, 0.05)
            return result

        def visit(self):
            return []

    class J701ConsoleDialFace(renpy.Displayable):
        def __init__(self, index, **kwargs):
            super(J701ConsoleDialFace, self).__init__(**kwargs)
            self.index = index

        def render(self, width, height, st, at):
            size = 330
            result = renpy.Render(size, size)
            canvas = result.canvas()
            center = (165, 165)
            locked = self.index < len(store.j701_console_locked) and store.j701_console_locked[self.index]
            error = self.index < len(store.j701_console_error_ticks) and store.j701_console_error_ticks[self.index] > 0
            value = j701_console_value(self.index)

            if locked:
                accent = "#67ef8f"
                glow = "#67ef8f66"
            elif error or value == "ERR":
                accent = "#ff5b66"
                glow = "#ff334f77"
            else:
                accent = "#63d7ff"
                glow = "#36bde866"

            canvas.circle("#03101adf", center, 160, 0)
            canvas.circle(glow, center, 157, 7)
            canvas.circle("#183b52", center, 145, 2)
            canvas.circle(accent, center, 132, 3)
            canvas.circle("#0b2638", center, 112, 2)
            canvas.circle("#020a11", center, 100, 0)

            rotation = 0.0 if locked else st * (0.42 if self.index % 2 == 0 else -0.38)
            for tick in range(40):
                angle = rotation + (math.pi * 2.0 * tick / 40.0)
                outer = 139
                inner = 129 if tick % 5 else 123
                p1 = (int(165 + math.cos(angle) * inner), int(165 + math.sin(angle) * inner))
                p2 = (int(165 + math.cos(angle) * outer), int(165 + math.sin(angle) * outer))
                canvas.line(accent if tick % 5 == 0 else "#5c91ab", p1, p2, 3 if tick % 5 == 0 else 1)

            for segment in range(8):
                start = rotation * -0.7 + segment * math.pi / 4.0 + 0.08
                j701_console_arc(canvas, glow, center, 151, start, start + 0.48, 5, 9)

            wave_amp = 0 if locked else (8 if value in ("ERR", "SYNC") else 4)
            previous = None
            for x in range(92, 239, 7):
                y = 217 + int(math.sin(x * 0.23 + st * 7.0) * wave_amp)
                if value == "ERR":
                    y += int(math.sin(x * 0.71 + st * 17.0) * 5)
                point = (x, y)
                if previous is not None:
                    canvas.line(accent, previous, point, 2)
                previous = point

            if locked:
                canvas.circle("#67ef8f99", (165, 271), 25, 3)
                canvas.line("#67ef8f", (154, 271), (154, 260), 4)
                canvas.line("#67ef8f", (176, 271), (176, 260), 4)
                canvas.line("#67ef8f", (154, 260), (176, 260), 4)
                canvas.line("#67ef8f", (151, 271), (179, 271), 16)

            renpy.redraw(self, 0.04)
            return result

        def visit(self):
            return []

    class J701ConsoleCore(renpy.Displayable):
        def __init__(self, **kwargs):
            super(J701ConsoleCore, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            size = 620
            result = renpy.Render(size, size)
            canvas = result.canvas()
            center = (310, 310)
            locked = list(store.j701_console_locked)
            while len(locked) < 4:
                locked.append(False)
            locked_count = sum(1 for value in locked if value)
            solved = locked_count == 4

            canvas.circle("#03101acc", center, 286, 0)
            canvas.circle("#3cc8ff33", center, 284, 5)
            canvas.circle("#51d3ff99", center, 257, 3)
            canvas.circle("#153f58", center, 232, 2)
            canvas.circle("#061926ee", center, 207, 0)

            rotation = 0.0 if solved else st * 0.20
            for segment in range(16):
                start = rotation + segment * math.pi / 8.0 + 0.035
                j701_console_arc(canvas, "#4bd0ff99", center, 273, start, start + 0.22, 5, 7)

            for radius in (215, 239, 275):
                for tick in range(24):
                    angle = -rotation * 0.65 + tick * math.pi / 12.0
                    inner = radius - (10 if tick % 3 == 0 else 5)
                    p1 = (int(310 + math.cos(angle) * inner), int(310 + math.sin(angle) * inner))
                    p2 = (int(310 + math.cos(angle) * radius), int(310 + math.sin(angle) * radius))
                    canvas.line("#6ce0ff88", p1, p2, 2)

            j701_console_ellipse(canvas, "#44c9f077", center, 198, 76, 2)
            j701_console_ellipse(canvas, "#44c9f066", center, 198, 132, 1)
            j701_console_ellipse(canvas, "#44c9f066", center, 76, 198, 2)
            j701_console_ellipse(canvas, "#44c9f055", center, 132, 198, 1)
            canvas.line("#44c9f066", (112, 310), (508, 310), 2)
            canvas.line("#44c9f055", (310, 112), (310, 508), 1)

            quadrants = [
                (math.pi, math.pi * 1.5),
                (math.pi * 0.5, math.pi),
                (math.pi * 1.5, math.pi * 2.0),
                (0.0, math.pi * 0.5),
            ]
            for index, angles in enumerate(quadrants):
                color = "#72f29cdd" if locked[index] else "#287ca144"
                for radius in (168, 181, 194):
                    j701_console_arc(canvas, color, center, radius, angles[0] + 0.05, angles[1] - 0.05, 2 if locked[index] else 1, 22)

            noise_ratio = max(0.0, min(1.0, store.j701_console_noise / 64.0))
            previous = None
            for x in range(82, 539, 8):
                if solved:
                    y = 310
                else:
                    y = 310 + int(math.sin(x * 0.15 + st * 6.0) * (8 + 15 * noise_ratio))
                    y += int(math.sin(x * 0.43 + st * 13.0) * 8 * noise_ratio)
                point = (x, y)
                if previous is not None:
                    canvas.line("#a8efff", previous, point, 3)
                    canvas.line("#43cfff66", previous, point, 7)
                previous = point

            renpy.redraw(self, 0.04)
            return result

        def visit(self):
            return []

screen j701_console_game():
    modal True
    zorder 220
    on "show" action Function(j701_console_reset)
    on "hide" action Function(j701_console_cleanup)
    timer 0.05 repeat True action Function(j701_console_tick)

    if j701_console_phase == "silence":
        timer 1.0 action Function(j701_console_begin_reveal)

    add Solid("#01070df8")
    add Solid("#06182788") xpos 16 ypos 50 xsize 1888 ysize 870
    add Solid("#35bff022") xpos 16 ypos 50 xsize 2 ysize 870
    add Solid("#35bff022") xpos 1902 ypos 50 xsize 2 ysize 870

    frame:
        xpos 380
        ypos 18
        xsize 1160
        ysize 116
        padding (24, 12)
        background Solid("#03111bea")
        vbox:
            spacing 3
            text "CANON // SYNCHRONISATION DES FLUX" size 42 color "#DFF8FF" xalign 0.5
            text "Isole la dernière valeur stable de chaque flux régional." size 24 color "#A8D9F2" xalign 0.5

    showif j701_console_phase in ("play", "silence"):
        fixed:
            at j701_console_panels
            xsize 1920
            ysize 940

            add J701ConsoleNetwork()
            add J701ConsoleCore() xpos 650 ypos 205

            $ locked_count = j701_console_locked_count()
            $ central_status = kd_tr("SIGNAL MONDIAL INSTABLE") if locked_count == 0 else (kd_tr("SIGNAL PARTIEL // %d / 4") % locked_count if locked_count < 4 else kd_tr("SIGNAL MONDIAL STABILISÉ"))
            frame:
                xpos 720
                ypos 642
                xsize 480
                ysize 54
                padding (10, 7)
                background Solid("#03111bee")
                text central_status size 25 color ("#77EF9C" if locked_count == 4 else "#79DFFF") xalign 0.5 yalign 0.5

            for idx, module in enumerate(J701_CONSOLE_MODULES):
                $ cx, cy = J701_CONSOLE_CENTERS[idx]
                $ value = j701_console_value(idx)
                $ locked = idx < len(j701_console_locked) and j701_console_locked[idx]
                $ error = idx < len(j701_console_error_ticks) and j701_console_error_ticks[idx] > 0
                $ shake = (-7 if j701_console_error_ticks[idx] % 2 else 7) if error else 0
                $ value_color = "#77EF9C" if locked else ("#FF5964" if error or value == "ERR" else "#FFCE70")

                add Transform(J701ConsoleDialFace(idx), xoffset=shake) xpos (cx - 165) ypos (cy - 165)
                text kd_tr(module["name"]):
                    xpos cx
                    ypos (cy - 194)
                    xanchor 0.5
                    size 30
                    color ("#77EF9C" if locked else "#79DFFF")
                    outlines [(2, "#02070b", 0, 0)]

                if value in ("ERR", "SYNC") and not locked:
                    text value at j701_console_value_glitch:
                        xpos cx
                        ypos (cy - 30)
                        xanchor 0.5
                        yanchor 0.5
                        size (56 if value == "SYNC" else 64)
                        color value_color
                        outlines [(3, "#02070b", 0, 0)]
                elif not locked:
                    text value at j701_console_value_unstable:
                        xpos cx
                        ypos (cy - 30)
                        xanchor 0.5
                        yanchor 0.5
                        size 72
                        color value_color
                        outlines [(3, "#02070b", 0, 0)]
                else:
                    text value:
                        xpos cx
                        ypos (cy - 30)
                        xanchor 0.5
                        yanchor 0.5
                        size 72
                        color value_color
                        outlines [(3, "#02070b", 0, 0)]

                textbutton "‹":
                    xpos (cx - 215)
                    ypos (cy - 34)
                    xsize 58
                    ysize 68
                    text_size 45
                    text_color "#FFCE70"
                    text_xalign 0.5
                    text_yalign 0.5
                    background Solid("#0b2333dd")
                    hover_background Solid("#184762ee")
                    sensitive not locked and j701_console_phase == "play"
                    action Function(j701_console_cycle, idx, -1)

                textbutton "›":
                    xpos (cx + 157)
                    ypos (cy - 34)
                    xsize 58
                    ysize 68
                    text_size 45
                    text_color "#FFCE70"
                    text_xalign 0.5
                    text_yalign 0.5
                    background Solid("#0b2333dd")
                    hover_background Solid("#184762ee")
                    sensitive not locked and j701_console_phase == "play"
                    action Function(j701_console_cycle, idx, 1)

                if locked:
                    text "FLUX STABILISÉ":
                        xpos cx
                        ypos (cy + 154)
                        xanchor 0.5
                        size 21
                        color "#77EF9C"
                        outlines [(2, "#02070b", 0, 0)]
                else:
                    textbutton "CALIBRER":
                        xpos (cx - 117)
                        ypos (cy + 143)
                        xsize 234
                        ysize 52
                        text_size 23
                        text_color "#FFCE70"
                        text_xalign 0.5
                        text_yalign 0.5
                        background Solid("#101d27ee")
                        hover_background Solid("#473718ee")
                        sensitive j701_console_phase == "play"
                        action Function(j701_console_calibrate, idx)

            frame:
                xpos 638
                ypos 852
                xsize 644
                ysize 48
                padding (12, 6)
                background Solid("#030d15dd")
                text kd_tr(j701_console_feedback) size 20 color ("#FF5964" if any(j701_console_error_ticks) else ("#77EF9C" if j701_console_locked_count() == 4 else "#A8D9F2")) xalign 0.5 yalign 0.5 text_align 0.5

    showif j701_console_phase == "reveal":
        fixed:
            at j701_console_result
            xsize 1920
            ysize 930

            frame:
                xpos 390
                ypos 220
                xsize 1140
                ysize 570
                padding (42, 34)
                background Solid("#020c14f5")
                vbox:
                    spacing 24
                    xalign 0.5
                    text "ANALYSE TERMINÉE" size 46 color "#79DFFF" xalign 0.5
                    add Solid("#49cfff88") xalign 0.5 xsize 760 ysize 2
                    text "EXÉCUTIONS RECENSÉES — DERNIÈRES 24 HEURES" size 27 color "#A8D9F2" xalign 0.5
                    text "TOTAL MONDIAL : 0" size 68 color "#77EF9C" xalign 0.5
                    null height 18
                    text "DERNIÈRE EXÉCUTION ENREGISTRÉE : HIER — 18 H 42" at j701_console_last_record:
                        size 27
                        color "#FFCE70"
                        xalign 0.5

            textbutton "QUITTER LE CANON" at j701_console_result_button:
                xpos 730
                ypos 720
                xsize 460
                ysize 72
                text_size 28
                text_color "#DFF8FF"
                text_xalign 0.5
                text_yalign 0.5
                background Solid("#0d3044ee")
                hover_background Solid("#176083ee")
                action Return(True)

    frame:
        xpos 100
        ypos 946
        xsize 1720
        ysize 92
        padding (24, 15)
        background Solid("#020d15f2")
        fixed:
            text "Stabilise chaque flux pour reconstituer le bilan mondial.":
                xpos 360
                ypos 13
                size 23
                color "#79DFFF"
            bar value StaticValue(j701_console_noise, 64):
                xpos 1120
                ypos 20
                xsize 250
                ysize 16
            text "[j701_console_locked_count()] / 4 FLUX STABILISÉS":
                xpos 1400
                ypos 9
                size 23
                color ("#77EF9C" if j701_console_locked_count() == 4 else "#FFCE70")

label j701_play_console:
    call screen j701_console_game
    return


label _7_0_1_REVEIL_CHAMBRE:
    call show_chapter_title("Début du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_25
    scene black
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 7
    $ noam_has_juliette_drawing = True
    $ j701_table_choice = "aucun"
    $ j701_tomas_secret_kept = True
    $ j701_lysa_worry = False
    $ j701_lysa_search_help = False
    $ j701_iris_defense = False
    $ j701_tomas_informed = False
    $ j701_nyra_sorting = "standard"
    $ j701_plate_result = -1
    $ j701_julian_rapport = "neutre"
    $ j701_evidence_note = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    pause 0.5
    play sound sfx_knock
    $ blink()
    lysa "Noam ? C'est moi."
    "Je remonte la couverture jusqu'à mon nez. On frappe de nouveau."
    noam "Ouais, j'arrive..."
    lysa "Il est presque midi, t'es toujours au lit ?"
    "Je regarde ma tablette. 11 h 40."
    noam "Merde !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me traîne jusqu'à la porte et l'entrouvre. Une silhouette passe au bout du couloir."
    noam "Rentre, s'il te plaît. J'ai pas envie que tout le monde me voie en pyjama."
    call kd_vn_cg_impact("#e4f0ff")
    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")
    "Je referme la porte derrière elle."
    lysa "T'as raté le petit déjeuner. Nyra a commencé à ranger les livraisons, et Iris appelle Kami depuis huit heures. Elle est même allée emmerder Goumi à la cafétéria."
    noam "Toujours aucune réponse ? Je pensais qu'elle finirait par revenir cette nuit."
    lysa "J'ai essayé à mon réveil. Sur Terre, ça m'aurait arrangée qu'elle nous foute la paix de temps en temps. Mais ici, j'aimerais bien savoir ce qui se passe."
    "Je récupère une chaussette au pied du lit. L'autre est coincée sous mon bureau."
    noam "Je vais pas me plaindre d'avoir pu dormir, mais hier... J'avais vraiment l'impression qu'elle avait besoin de nous."
    menu:
        "Rester un moment avec Lysa.":
            $ j701_lysa_worry = True
            lysa "J'ai vérifié ta porte deux fois ce matin. J'allais finir par demander à quelqu'un de venir l'ouvrir."
            noam "Ah... Désolé, je devais vraiment dormir comme une masse."
            lysa "T'as le droit de dormir. Préviens-moi juste si tu comptes passer la journée ici."
        "Essayer de la détendre.":
            noam "Au moins, personne n'est venu commenter ma tronche au réveil."
            lysa "Je peux encore m'en charger si ça te manque."
            "Je ramasse mon pantalon."
    play sound sfx_knock
    nyra "Lysa ? Tu es là ?"
    lysa "Oui, j'arrive !"
    "Lysa se tourne vers moi."
    lysa "Ah, oui. Je lui ai dit que tu l'aiderais avec les caisses."
    noam "Mais je dormais ! Bon, je vais dans la salle de bain me changer."
    lysa "Prends ton temps. Je vais commencer avec elle."
    "Elle ressort. Je soulève le dessin de Juliette pour dégager ma chaussette, puis je le repose soigneusement sur le bureau."
    $ unlock_gallery_image("bg_cg026")
    scene bg_cg026 at adaptive_fullscreen with dissolve
    "Je prends mes vêtements et file dans la salle de bain."
    scene bg_cg026_1 at adaptive_fullscreen with dissolve
    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    "Je les retrouve cinq minutes plus tard."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "blase", 0.51), ("noam", "neutre", 0.21)])
    nyra "Bonjour. Ne soulève pas celle-ci par les poignées, le carton est déchiré en dessous."
    "Je me baisse. Le fond commence effectivement à céder."
    nyra "Les manifestes sont arrivés avec des références incomplètes. Je ne peux pas valider la réception de matériel médical si je ne sais pas ce qui a été livré. Il faudrait ouvrir les caisses et faire deux listes."
    noam "On est combien à faire ça ?"
    nyra "Trois, pour le moment."
    lysa "J'ai déjà ouvert les miennes. Si tu veux, je peux aller chercher Elias."
    nyra "Il a du travail. Et je préfère que les mêmes personnes terminent l'inventaire."
    "Nyra sort une liasse de feuilles. L'une d'elles est un quadrillage dessiné à la main."
    noam "Tu fais encore tes tableaux sur papier ?"
    nyra "Oui. Sur Orbite, j'avais pris l'habitude de garder une liste indépendante des terminaux. Quand tu vis avec une réserve limitée, tu ne peux pas te permettre d'attendre que quelqu'un te confirme qu'il reste de quoi manger."
    lysa "Ici, personne ne nous a demandé de tenir un inventaire pour Kami. Je veux bien aider, mais je vais pas remplir trois formulaires pour un paquet de pâtes."
    nyra "Ce n'est pas pour Kami. Je ne sais pas combien de temps elle sera absente, ni si la prochaine livraison sera complète. J'aimerais éviter qu'on découvre trop tard qu'il nous manque quelque chose d'important."
    "Je pose le carton sur le sol. Il contient des pansements, de la nourriture et un appareil emballé."
    noam "Bon, je commence par quoi ? J'ai pas encore mangé et je sens que je vais faire des erreurs."
    menu:
        "Faire un inventaire complet avec Nyra.":
            $ j701_nyra_sorting = "inventaire"
            noam "Passe-moi une feuille. Je note le contenu, et toi tu vérifies les références."
            nyra "Parfait. Écris assez grand, il faudra que je puisse relire."
            "Elle me tend son crayon."
            lysa "Je vais chercher un truc à boire. Je reviens."
        "Isoler les colis douteux pour gagner du temps.":
            $ j701_nyra_sorting = "rapide"
            noam "On pourrait mettre les colis qui posent problème de côté et ranger le reste. On serait déjà débarrassés de la moitié."
            nyra "Ça me convient si on note où ils sont. Pas dans le passage, s'il te plaît."
    "Au bout d'un moment, Lysa revient avec trois verres d'eau et un paquet de biscuits trouvé parmi les rations."
    lysa "Vous en voulez ?"
    nyra "Attends, il faut que je le compte avant."
    "Lysa tient le paquet fermé pendant que Nyra termine sa ligne."
    nyra "Bon. Il est noté. Tu peux l'ouvrir."
    "Elle en prend un elle aussi. Je m'assieds sur la caisse vide."
    nyra "Pas celle-là !"
    "Trop tard. Le carton s'écrase sous moi."
    noam "Aïe... C'est bon, j'ai rien cassé ?"
    "Lysa me tend la main. Nyra récupère la feuille qui a glissé sous mon pied."
    "On termine le rangement sans autre incident. J'ai toujours faim."
    $ hideGroup()
    jump _7_0_1_CAFETERIA

label _7_0_1_CAFETERIA:
    call KD_ROUTE_J7_ELIAS from _call_optional_kd_route_j7_elias
    call START_EXPLORATION_LIBRE("_7_0_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_exploration__7_0_1_CAFETERIA

label _7_0_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_282
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    $ showGroup([
        ("iris", "fatigue"), ("julian", "sourire"), ("lysa", "neutre"),
        ("elias", "neutre"), ("mara", "neutre"), ("kael", "fatigue"), ("elen", "joie")
    ])
    elen colere "Non ! Ne t'assieds pas là, Julian. C'est ma place et c'était mon gâteau."
    julian "Elen, je n'ai jamais vu ton nom sur cette assiette."
    elen "Je t'ai demandé de me le garder pendant que j'allais chercher de l'eau !"
    "Elle dépose son verre devant lui. Julian regarde l'assiette vide."
    julian "Je pensais que tu étais partie. Je te propose de te céder mon dessert demain. Un dessert entier."
    elen "Mais demain il y aura peut-être des yaourts !"
    elias "Tiens, prends le mien. Franchement, j'aime pas trop le truc au-dessus."
    elen "C'est de la crème, Elias. Et non, mange-le, toi."
    "Elias garde son assiette en l'air. Mara en prélève un morceau avec sa fourchette."
    elias "Wesh ! Je l'ai pas donné à tout le monde !"
    mara "Bah fallait la poser."
    "Elen essaie de récupérer l'assiette de Julian, découvre qu'il ne reste vraiment rien, puis lui confisque sa serviette."
    julian "Je peux au moins finir de déjeuner proprement ?"
    elen "Non."
    "Je prends mon repas et m'assieds à côté de Lysa. Julian se lève pour chercher une autre serviette ; Elen déplace sa chaise."
    julian "Noam. Dis-lui qu'elle se comporte comme une enfant."
    noam "Me mêle pas à ça, j'ai déjà passé ma matinée à porter des caisses."
    elen "Oh ! Il reste du gâteau au comptoir ?"
    "Elle repart aussitôt. Elle revient avec un morceau et le mange debout, hors de portée de Julian."
    elen "Che choir on fait quelque chose. J'en ai marre de manger et de rentrer chacun dans cha chambre..."
    iris "Avale avant de parler, Elen."
    "Elen termine sa bouchée."
    elen "J'ai trouvé un jeu de cartes dans la salle de repos ! On pourrait jouer après le dîner."
    mara "Si on joue de l'argent, je viens."
    elen "On n'a pas d'argent."
    mara "On trouvera un truc. J'ai besoin de me divertir, là."
    "Lysa me fait passer le pain. Iris ne mange presque pas."
    iris "Vous avez essayé les terminaux de vos chambres ce matin ?"
    elias "Le mien s'allume. Mais y a pas Kami dessus, si c'est ça."
    iris "Elle nous a demandé de l'aider hier. J'ai envoyé des requêtes depuis tous les terminaux accessibles, et même quand elle refusait de me répondre, avant, je pouvais au moins identifier un refus. Là je n'ai rien."
    mara "Perso, ça m'a fait du bien de pas entendre sa voix au réveil. Ça faisait un an que j'avais pas eu une matinée comme ça."
    iris colere "Mais elle est peut-être en panne ! C'est pas un concours pour savoir qui la déteste le plus."
    mara "Tu crois que je vais pleurer parce qu'elle peut plus nous dire quoi faire ?"
    "Iris repose sa fourchette."
    iris "Tu te rends compte de ce qu'elle est capable de faire ? Elle gère des millions de situations en même temps et elle arrive quand même à nous répondre individuellement. Rien que la façon dont elle adapte ses réponses, j'aimerais comprendre comment elle fait. Et là, elle ne répond plus à rien."
    iris "Si quelque chose est capable de la mettre dans cet état, j'aimerais le savoir avant que ça touche autre chose."
    lysa "Tu lui prêtes beaucoup de bonnes intentions, quand même."
    iris "J'ai pas parlé de ses intentions."
    elias "Moi j'aimerais surtout savoir si dehors c'est pareil. À Axiome, avant Kami, dans mon quartier, on évitait de rentrer seuls le soir. J'ai pas envie que ça recommence."
    mara "Chez moi, on avait des murs de trois mètres pour pas voir ce qui se passait dehors. Depuis Kami, j'ai enfin pu ouvrir la porte à des gens qui avaient besoin d'un endroit où dormir. Et je vais pas non plus lui donner raison sur tout pour ça."
    julian "Nous avons voté hier. Il me semble que nous pourrions, exceptionnellement, profiter de l'occasion pour reprendre une discussion sans qu'une voix nous impose l'ordre du jour."
    noam "Julian, on a passé trois jours à se prendre la tête. Laisse-nous manger, pour une fois."
    julian "Je ne t'ai pas demandé de présider la discussion."
    "Je ravale ce que j'allais lui répondre. Elen me montre le jeu de cartes qu'elle a rapporté."
    elen "On pourra choisir les règles ce soir. Il y en a plein que je connais pas."
    kael reflechit "Iris, j'ai comparé les journaux des relais ce matin. Il manque une partie des données extérieures. Je ne sais pas encore à quel niveau."
    iris "Tu aurais pu me le dire !"
    kael "Je n'avais rien de fiable à te donner."
    iris "Tu m'envoies ce que tu as, même si c'est incomplet. Je vais regarder depuis l'infirmerie."
    "Elle se lève. Elen écarte son verre pour la laisser passer."
    menu:
        "Suivre Iris jusqu'à la porte.":
            $ j701_table_choice = "inquietude"
            $ j701_iris_defense = True
            noam "Iris, attends. Je peux t'aider à regarder les terminaux après manger."
            iris "Tu vas surtout me poser des questions pendant que j'essaie de bosser. Laisse-moi faire, d'accord ? Si tu entends quelque chose sur ta tablette, tu me le dis."
            noam "D'accord. Je te garde ton assiette."
        "Rester auprès d'Elen.":
            $ j701_table_choice = "complicite"
            elen "Je voulais juste qu'on passe un bon moment. J'ai peut-être choisi le mauvais jour."
            noam "Viens, montre-moi les cartes. On peut préparer le jeu quand même."
            "Elle étale les cartes sur la table et me demande de l'aider à les trier."
        "Demander à Julian de changer de sujet.":
            $ j701_table_choice = "julian"
            noam "Julian, si tu veux vraiment faire quelque chose d'utile, aide Elen à organiser sa soirée."
            julian "Très bien. Mais je refuse qu'on me rende responsable de la mauvaise humeur générale."
            "Il reprend le paquet de cartes sans attendre ma réponse."
    "Kael se lève avec sa tablette branchée à une batterie externe."
    elias "Kael, t'as même pas fini ton pain. Tu veux que je te garde le reste ?"
    kael "Je vais l'emporter, merci."
    "Lysa me pousse une assiette avec un morceau de gâteau."
    lysa "Tiens. Si tu repasses à l'infirmerie, garde-en un bout pour Iris."
    noam "Je vais voir."
    $ hideGroup()
    jump _7_0_1_TEMPS_LIBRE_1

label _7_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflechit", 0.31), ("noam", "neutre", 0.72)])
    "Kael a posé une feuille sur une caisse et essaie de noter quelque chose en mangeant son pain."
    noam "Je peux m'asseoir ? J'ai pas envie de retourner dans ma chambre tout de suite."
    kael "Oui. Fais attention au crayon."
    "Je m'installe. Il continue ses calculs."
    noam "Ça fait longtemps que tu bosses là-dessus ?"
    kael "Depuis cette nuit. J'ai dormi un peu entre deux vérifications. Les relevés du Conclave et ceux de l'observatoire ne concordent pas. Je les recopie parce que les terminaux ne sont même pas d'accord sur l'ordre des événements."
    noam "Je croyais que tu pouvais faire ça automatiquement."
    kael "D'habitude, oui. Mais je préfère retrouver une heure que je peux vérifier moi-même. À Orbite, j'ai appris à ne pas faire confiance à un affichage simplement parce qu'il est précis."
    "Il efface une colonne. Un peu de graphite a taché le pain."
    noam "Tu sais que t'es en train de manger ton crayon, là ?"
    kael "Ah."
    "Il pose le pain et nettoie son doigt sur la feuille."
    kael "Je faisais pareil avec mes maquettes. J'avais passé un temps fou à monter le gréement d'un voilier et j'ai cassé le mât en voulant le ranger. J'ai dû recommencer toute une partie."
    noam "Un voilier ?! Je pensais que tu collectionnais des vaisseaux spatiaux, des trucs un peu plus classes."
    kael "Je voyais des vaisseaux tous les jours sur Orbite. Les voiliers, par contre... J'ai jamais vu la mer. J'ai regardé des tas de vidéos pour comprendre comment ils utilisaient le vent."
    noam "T'aimerais essayer ?"
    kael "Bien sûr. Rien que monter à bord, ça me plairait. Après, je laisserais quelqu'un d'autre s'occuper des manœuvres."
    "Il me montre la taille de la maquette avec ses mains."
    noam "Ah ouais, c'est carrément un meuble ton truc. J'avais un modèle de vaisseau quand j'étais plus jeune, j'ai perdu une aile et j'ai fini par le jeter."
    kael "Tu aurais pu la refaire. Je peux te montrer comment, à l'occasion."
    noam "Tu risques de regretter de m'avoir proposé ça."
    "Il reprend son crayon."
    if j601_fracture_trace_saved:
        kael "Au fait, tu as conservé la trace du piratage sur ta tablette ? Ne la modifie pas. J'aimerais comparer les horodatages avec les relevés originaux."
        noam "Je te la laisse quand tu veux."
        kael "Merci. Pas besoin de me l'envoyer pour l'instant."
        $ j701_evidence_note = True
    else:
        kael "Il me faudrait un enregistrement complet de la diffusion d'hier. Les relevés que j'ai récupérés sont incomplets, je vais voir si la console d'observation a gardé une copie."
    noam "Tu devrais dormir avant de continuer. Tu vas finir par te tromper dans tes propres calculs."
    kael "Possible. Je termine cette colonne et je vais m'allonger."
    "Je le laisse à ses papiers."
    $ hideGroup()
    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1

label _7_0_1_APRES_MIDI_TOMAS_CANON:
    $ current_period = "Après-midi"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Je suis retourné dans ma chambre. Je viens à peine de m'allonger quand quelqu'un frappe."
    play sound sfx_knock
    tomas "Noam ? Tu es disponible ?"
    "J'ouvre la porte."
    $ showGroup([("tomas", "inquiet", 0.50)])
    tomas "Excuse-moi de te déranger. J'ai besoin d'un deuxième avis sur des relevés que j'ai trouvés ce matin. Si tu as quelques minutes, j'ai laissé la console ouverte au canon."
    noam "Si c'est encore des calculs, t'aurais peut-être dû demander à quelqu'un de plus compétent."
    tomas "Justement, je préfère que tu découvres les données sans savoir ce que j'ai obtenu. Ça ne prendra pas très longtemps."
    noam "Bon, laisse-moi récupérer ma veste."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Tomas connecte sa tablette à la console."
    tomas reflechit "J'ai pris l'habitude de regarder les registres de sanctions. À Archive, j'avais accès à beaucoup de documents sur l'ancien monde, mais les chiffres de l'époque ne sont pas toujours comparables aux nôtres. Je voulais voir ce qu'il était possible de reconstituer sur cette dernière année."
    noam "Les sanctions ? Tu passes ton temps libre à compter des morts ?"
    tomas "Pas exactement. Enfin... oui, parfois. Ce qui m'intéresse, c'est ce que les relevés permettent de vérifier. Depuis hier, les quatre flux régionaux présentent des erreurs et les valeurs arrivent dans le désordre."
    tomas "J'ai essayé de retrouver les dernières valeurs stables. Je me suis trompé deux fois sur le flux de l'Est et, à ce stade, j'ai peur de choisir les chiffres qui confirment ce que je crois avoir vu."
    noam "Montre-moi comment on fait. Je vais essayer sans regarder ton résultat."
    tomas "Tu as les quatre commandes ici. Trouve la dernière valeur stable de chaque flux, puis valide-les séparément."
    call j701_play_console from _call_j701_play_console
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Le total s'affiche."
    noam surpris "Zéro ? Attends, c'est le nombre de personnes exécutées ?"
    tomas "C'est ce que j'ai obtenu aussi. J'ai regardé les enregistrements précédents pour vérifier que le tableau n'était pas vide depuis le début."
    "Il remonte jusqu'à la veille. Des dizaines de lignes s'affichent."
    noam "Donc depuis ce qu'on a vu hier... plus aucune exécution enregistrée ?"
    tomas "Aucune sur les quatre flux que nous pouvons consulter. Mais je n'ai pas accès à l'archive complète. Ça peut être un problème de transmission, une interruption des sanctions, ou autre chose que nous ne voyons pas."
    noam "Zéro... Ça fait bizarre de voir ça. J'espère vraiment que le chiffre est bon."
    "Tomas remonte quelques lignes et agrandit le graphique."
    tomas "Moi aussi. Mais regarde, les enregistrements se sont arrêtés alors que les terminaux présentent encore des anomalies. Si on ne reçoit plus certaines données, un total de zéro ne veut pas forcément dire qu'il ne s'est rien passé."
    noam "Ah... D'accord."
    tomas "Je vais garder une copie des relevés et refaire la comparaison demain. J'aimerais que ça reste entre nous pour le moment. Enfin, j'hésite à demander à Kael de vérifier les fichiers quand il aura un peu de temps."
    noam "Tu préfères attendre d'être sûr, c'est ça ?"
    tomas "Oui. Je voulais surtout savoir si quelqu'un d'autre arrivait au même résultat."
    call play_stat_dialogue("d7_0_1") from _call_stat_dialogue_d7_0_1
    menu:
        "Respecter sa demande de discrétion jusqu'au lendemain.":
            $ j701_tomas_secret_kept = True
            noam "D'accord. On attend demain, mais ne continue pas tout seul toute la nuit. Si on trouve autre chose, on décidera ensemble de ce qu'on en fait."
            tomas neutre "Ça me va. Je te préviendrai si j'obtiens de nouveaux relevés."
        "Laisser Tomas décider s'il souhaite demander un avis à Kael.":
            $ j701_tomas_secret_kept = False
            $ j701_tomas_informed = True
            noam "Fais comme tu le sens. Si tu penses que ça peut t'aider à vérifier, je ne vois pas de problème."
            tomas "Je vais lui transmettre uniquement les relevés, sans en tirer de conclusion."
            "Il rédige le message et joint les relevés."
            tomas "C'est envoyé."
    "Je reste devant le total encore quelques secondes avant de partir."
    $ hideGroup()
    jump _7_0_1_SOIREE_TENSION_LEGERE

label _7_0_1_SOIREE_TENSION_LEGERE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_287
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2
    "Elen a rapproché deux tables. Des cartes sont étalées au milieu."
    $ showGroup([
        ("iris", "fatigue"), ("julian", "neutre"), ("lysa", "neutre"),
        ("kael", "fatigue"), ("elias", "inquiet"), ("mara", "neutre"),
        ("elen", "sourire"), ("noam", "neutre")
    ])
    elen "Noam ! Prends une chaise. On joue au menteur. J'ai récupéré les cartes qui manquaient sous le canapé de la salle de repos."
    mara "On met un gage à celui qui perd ?"
    noam "NON !"
    "Mara n'avait même pas terminé sa phrase."
    mara "Mais je t'ai encore rien proposé !"
    noam "La dernière fois que t'as commencé une phrase comme ça, j'ai regretté de t'avoir écoutée. On joue aux cartes. C'est tout."
    elen "Moi je veux bien des gages, mais des trucs gentils."
    "Mara se penche vers elle et lui murmure quelque chose. Elen ouvre de grands yeux."
    elen "Ah non, je suis d'accord avec Noam."
    "On finit par distribuer. Elias repousse ses cartes vers Elen."
    elias inquiet "J'vais regarder, moi."
    "Julian remporte deux parties de suite. À la troisième, il pose ses dernières cartes et se lève pour saluer."
    julian sourire "Mes chers collègues, vous avez devant vous un joueur dont l'honnêteté n'a d'égal que le talent."
    lysa "Tu nous caches tes cartes depuis dix minutes."
    "Julian se tourne vers la caméra de surveillance."
    julian "Et pour les archives du Conclave : Julian ne ment JA-MAIS !"
    "Il attend quelques secondes, comme s'il espérait des applaudissements. Elen ramasse le paquet."
    elen "Tu peux te rasseoir maintenant ?"
    "Je perds la manche suivante. Iris récupère mes cartes en soupirant."
    iris "Mais t'as gardé que des rois ! Qu'est-ce que tu voulais que je fasse avec ça ?"
    "Julian se redresse. Iris pose deux cartes face cachée."
    iris "Deux dames."
    julian "MENTEUSE !"
    "Il retourne les cartes avant même qu'elle puisse retirer sa main. Deux rois."
    iris colere "Attends ! C'est Noam qui m'a déconcentrée !"
    noam "Tu viens de dire à voix haute ce que t'avais dans les mains !"
    julian "Je vous remercie, Iris. Je n'avais encore jamais vu quelqu'un annoncer lui-même sa stratégie à ses adversaires."
    "Iris pousse le tas vers moi, puis le reprend."
    iris "Redistribue. Je veux rejouer."
    "Elias fixe son verre. Il n'a pas touché aux cartes."
    elias inquiet "..."
    "La manche suivante dure un moment. Julian, qui n'a plus qu'une carte, se redresse déjà sur sa chaise."
    julian "J'espère que vous êtes prêts à assister à ma quatrième victoire. Elen, à toi."
    elen "Attends... Je crois que j'ai encore une dame. Voilà, une dame."
    julian "Tu mens."
    "Il retourne la carte. Une dame."
    "Elen regarde sa main vide. Julian doit ramasser tout le tas."
    elen joie "J'AI GAGNÉ !"
    $ _j701_elen_state = char_state.get("elen", {})
    $ renpy.show("elen joie", tag="elen", at_list=[char_group_move(_j701_elen_state.get("x", 0.85), _j701_elen_state.get("y", 1.0), _j701_elen_state.get("x", 0.85), _j701_elen_state.get("group_scale", 1.0), _j701_elen_state.get("group_scale", 1.0)), j701_elen_hop], layer=_j701_elen_state.get("layer", "master"), zorder=_j701_elen_state.get("zorder", 0))
    pause 0.65
    "Elle bondit de sa chaise, les bras en l'air."
    elen "J'ai gagné contre Julian ! Mara, t'as vu ?!"
    mara "Je te jure que j'ai cru qu'elle avait posé la mauvaise carte."
    "Julian reste immobile devant le tas qu'il doit reprendre. Il finit par regarder sa dernière carte."
    julian "Je... Je demande une revanche."
    "Elen est déjà partie montrer sa victoire à Kael, qui n'a suivi que la moitié de la partie."
    "Iris repose son paquet et regarde Elias."
    iris "Elias, ça va ? T'as pas joué une seule fois depuis qu'on est là."
    elias "J'arrive pas à retrouver mon matos. Je voulais continuer à réparer le gros robot de la maintenance, mais il manque des pièces et même sa batterie a disparu."
    lysa "Attends... Tu parles du truc énorme au fond de l'atelier ? Tu voulais vraiment le réveiller ?"
    elias "Bah ouais ! J'ai réussi à réparer une partie de ses connexions. Avec la batterie, j'aurais peut-être pu faire bouger les bras aujourd'hui."
    lysa "Ah non. Il est déjà suffisamment dégueulasse quand il bouge pas. Préviens-moi avant de faire ça."
    elias "J'te jure que je l'aurais pas laissé sortir de la maintenance."
    noam "T'as cherché où ? Si quelqu'un a déplacé les pièces pendant la livraison, elles sont peut-être dans une caisse."
    elias "J'ai vérifié les cartons, mais j'ai pas fait tous les placards. Ça m'énerve, j'étais presque prêt. Il manque aussi la batterie de rechange, le micro-soudeur, les trois stabilisateurs et les outils de coupe."
    kael "On a récupéré beaucoup de matériel ce matin. Il a peut-être été emprunté."
    noam "Viens, je vais regarder avec toi."
    lysa "Je vous accompagne. Mais si vous essayez de l'allumer, je me casse."
    elen "On laisse les cartes ici, alors ?"
    julian "Certainement pas. Je tiens à obtenir ma revanche."
    "Elen rassemble les cartes pendant que nous nous levons."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE

label _7_0_1_FIN_JOURNEE:
    "Après avoir laissé Elias ranger ses outils, je retourne vers les chambres."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([("noam", "neutre", 0.50)])
    "Elen attend devant la chambre de Ryn avec une assiette recouverte d'un mouchoir."
    noam "Il a pas mangé avec nous ?"
    elen "Non. Je lui ai gardé une part. Il m'a dit tout à l'heure qu'il voulait qu'on le laisse tranquille, alors je vais juste la poser ici."
    noam "Tu pourrais lui laisser un message. Il va peut-être pas ouvrir avant demain."
    elen "Je lui en ai déjà envoyé un. Je sais pas quoi lui dire depuis le vote. J'ai peur de l'énerver encore plus quand j'essaie de lui remonter le moral."
    "Elle dépose l'assiette près de la porte."
    elen "Au moins, s'il a faim, il aura quelque chose."
    noam "Je crois que c'est une bonne idée."
    "On se sépare devant les chambres."
    if j701_tomas_secret_kept:
        "Ma tablette vibre. Tomas m'écrit : « Je revérifie demain matin. Je n'ai rien dit. »"
        "Je réponds : « Dors quand même. »"
    else:
        "Ma tablette vibre. Tomas m'écrit : « Kael a reçu les fichiers. Il regarde demain. »"
        "Je réponds : « Merci. »"
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je retire ma veste. Le tiroir de mon bureau est entrouvert."
    "Je m'approche pour le fermer."
    noam surpris "Hein ?"
    "Le dessin de Juliette n'est plus à côté du cadre."
    "Je soulève le cadre, puis la tablette. Je vide le tiroir."
    noam "Non, attends... Je l'ai pas rangé là."
    "Ce matin, je l'ai déplacé pour récupérer ma chaussette. Je l'ai remis à sa place. J'en suis sûr."
    "Je sors la boîte dans laquelle je l'avais transporté jusqu'au Conclave. Elle est vide."
    think "Putain. Non."
    "Je revois Juliette me faire répéter que je serais là pour son anniversaire. Elle avait insisté pour que je fasse attention au dessin pendant le voyage."
    "Je regarde sous le lit. Rien."
    noam inquiet "Qui est entré ici ?"
    "Je prends ma tablette. Le nom de Lysa apparaît dans mes conversations récentes."
    menu:
        "Demander à Lysa de m'aider à chercher demain.":
            $ j701_lysa_search_help = True
            "Je lui écris : « T'es réveillée ? Il me manque quelque chose dans ma chambre. Tu pourrais venir voir demain ? »"
            lysa "Oui. Laisse les affaires comme elles sont, j'arrive demain matin."
            noam "Merci."
        "Garder la disparition pour moi cette nuit.":
            "J'écris à Lysa, puis j'efface le message. Je veux encore vérifier avant de lui en parler."
    $ noam_has_juliette_drawing = False
    "Je pose la boîte vide sur le bureau. Je vérifie la serrure de ma porte."
    "Elle affiche VERROUILLÉE."
    "Ça ne m'aide pas autant que je l'espérais."
    $ hideGroup()
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_0_1_REVEIL_CHAMBRE
