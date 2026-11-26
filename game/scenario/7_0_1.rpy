default j701_table_choice = "aucun"
default j701_lysa_worry = False
default j701_lysa_search_help = False
default j701_iris_defense = False
default j701_tomas_informed = False
default j701_nyra_sorting = "standard"
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
    $ j701_julian_rapport = "neutre"
    $ j701_evidence_note = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    $ blink()

    scene bg_chambre at adaptive_fullscreen with dissolve
    play sound sfx_knock
    lysa "Noam ?"
    noam fatigue "Mmh..."
    play sound sfx_knock
    lysa "Tu dors encore ?"
    noam "Oui..."
    lysa "Je peux rentrer ?"
    noam "Attends !"
    "Je regarde ce que je porte. Un pantalon de pyjama, un tee-shirt... Ça devrait aller."
    noam "C'est bon, entre."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_278
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.74), ("noam", "fatigue", 0.28)])
    lysa "T'es encore au lit ?"
    noam "Quelle heure il est ?"
    lysa "Onze heures quarante."
    noam surpris "Quoi ?!"
    "Je cherche ma tablette sous l'oreiller."

    $ hideGroup()
    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")

    noam "Ah merde... Onze heures quarante."
    lysa "Tu t'es couché à quelle heure ?"
    noam "Je sais plus. Pourquoi Kami nous a pas réveillés ?"
    lysa "Bah, demande-lui."
    noam "Kami ?"
    pause 0.6
    noam "Kami, il est quelle heure ?"
    lysa "Je viens de te le dire."
    noam "Non mais je vérifie."
    lysa "..."
    noam inquiet "Toujours rien depuis hier ?"
    lysa "Rien. J'ai croisé Iris très tôt ce matin, elle était déjà dans un sale état."
    noam "Elle a trouvé quelque chose ?"
    lysa "Aucune idée. J'ai essayé de lui parler, elle m'a demandé de la laisser tranquille."
    noam "Et Kael ?"
    lysa "Il bosse. Nyra aussi. Les portes s'ouvrent, on a de l'eau chaude, de quoi manger... Pour le reste, j'en sais rien."
    noam "T'as déjà mangé, toi ?"
    lysa "Oui."
    noam "Y avait quoi ?"
    lysa "Tu vas vraiment me demander de te détailler mon petit déjeuner ?"
    noam "Bah j'ai faim."
    lysa "Tu trouveras de quoi manger."
    "Je commence à me lever, mais Lysa ne bouge pas."
    noam "Tu voulais autre chose ?"
    lysa "Non."
    noam "Ah."
    lysa "Enfin... Je suis passée y a deux heures. T'as pas répondu."
    noam "Deux heures ? Pourquoi t'as pas insisté ?"
    lysa "Parce que tu pouvais très bien être en train de dormir. La preuve."
    noam "T'es revenue pour voir si j'étais vivant ?"
    lysa "Dit comme ça, c'est un peu con."
    menu:
        "Lui proposer de rester un peu avec elle.":
            $ j701_lysa_worry = True
            noam "Tu peux rester un peu si tu veux. Enfin, si t'as rien à faire."
            lysa "Tu comptes te rendormir devant moi ?"
            noam "Non, je vais m'habiller."
            lysa "Je vais attendre que t'aies fini, alors."
            noam "Lysa... Ça va, moi."
            lysa "Ouais, j'ai vu."
            lysa "C'est bon. Arrête de me regarder comme ça."
        "La taquiner pour la rassurer.":
            noam sourire "Fallait me réveiller. T'aurais pu me balancer un oreiller dans la figure."
            lysa "Je retiens."
            noam "Non, en fait, oublie."
            lysa "Trop tard."

    nyra "LYSA !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "blase", 0.74), ("noam", "neutre", 0.28)])
    lysa "Oui, oui, j'arrive !"
    noam "Elle te veut quoi ?"
    lysa "Ah. Les livraisons."
    noam "Quoi, les livraisons ?"
    lysa "J'ai dit à Nyra que tu viendrais nous aider."
    noam "Lysa !"
    lysa "Bon, habille-toi. Je t'attends dehors."
    noam "Mais je viens de me réveiller !"
    lysa "T'as dix minutes."
    "La porte se referme derrière elle."
    $ hideGroup()

    "Bon. Où est mon autre chaussette ?"
    "Je finis par la retrouver sous le dessin de Juliette, à côté du cadre numérique. Je la tire doucement pour ne pas froisser le papier et je remets le dessin bien à plat."
    $ unlock_gallery_image("bg_cg026")
    scene bg_cg026 at adaptive_fullscreen with dissolve
    "Je me passe un peu d'eau sur le visage."
    scene bg_cg026_1 at adaptive_fullscreen with dissolve
    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    "Je suis prêt en cinq minutes. J'espère au moins qu'il restera du café."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "blase", 0.51), ("noam", "neutre", 0.21)])
    nyra "Tu peux prendre cette caisse ?"
    noam "Bonjour, Nyra."
    nyra "Bonjour. Celle-ci, s'il te plaît."
    lysa "Pas l'autre. Elle m'a déjà engueulée parce que j'ai déplacé l'autre."
    nyra "J'avais terminé celle-là."
    "Je soulève le couvercle de la caisse. Il y a des pansements, des rations et un appareil dans le même emballage."
    noam "Ça va où, tout ça ?"
    nyra "C'est ce que j'essaie de déterminer. Regarde le manifeste."
    "FOURNITURES."
    noam "Ah."
    nyra "J'ai demandé une liste détaillée au service de livraison. Aucune réponse."
    lysa "Les pansements à l'infirmerie, les trucs à manger à la cafétéria. Pour le machin là, on demande à Elias."
    nyra "Il faut aussi noter ce qu'on a. Si on ne sait pas ce qui est entré, on ne saura pas ce qui manque."
    noam "OK. Montre-moi où t'en es."

    menu:
        "Faire un inventaire complet avec Nyra.":
            $ j701_nyra_sorting = "inventaire"
            noam "Je lis les références, tu les notes ?"
            nyra "Parfait. Lysa, tu peux séparer les consommables ?"
            lysa "Ouais. Donne-moi une caisse vide."
            nyra "On vérifie chaque référence. Pour le tri, on a quatre destinations : cafétéria, infirmerie, maintenance et stockage."
        "Isoler les colis douteux pour gagner du temps.":
            $ j701_nyra_sorting = "rapide"
            noam "On commence par ce qu'on reconnaît et on garde le reste ensemble ?"
            nyra "Il faudra quand même tout vérifier après."
            noam "Oui, mais on aura déjà dégagé le passage."
            lysa "Je peux prendre les rations."
            nyra "D'accord. Je note les caisses qu'il reste à examiner."
            nyra "Cafétéria, infirmerie, maintenance et stockage. Ce que vous ne reconnaissez pas, vous me le laissez."

    $ hideGroup()
    call rangement_play from _call_rangement_day7
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "neutre", 0.51), ("noam", "neutre", 0.21)])
    nyra "C'est bon pour celles-ci. Merci."
    lysa "Attends, j'ai trouvé un truc."
    "Elle ressort un paquet de biscuits."
    noam "Ah ! Donne."
    nyra "Non."
    lysa "J'ai même pas ouvert le paquet !"
    nyra "On les mettra avec le repas."
    lysa "Y en a douze, Noam. Je viens de compter. Un chacun."
    noam "Je veux bien le mien maintenant."
    nyra "Donne-moi le paquet."
    lysa "Mais..."
    nyra "Lysa."
    "Lysa lui tend le paquet."
    lysa "Tu nous en gardes, hein ?"
    nyra "Oui."
    noam "Bon, je vais manger. J'ai vraiment faim."
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
    elen colere "Non mais t'es sérieux ?!"
    julian "Quoi ?"
    elen "Mon gâteau ! Où il est ?"
    julian "Ah."
    elen "Julian !"
    julian "Bon... Il semblerait qu'il y ait eu un petit malentendu."
    elen "Je t'avais dit de me le garder !"
    julian "Et je l'ai gardé !"
    iris blase "Dans son estomac."
    julian "Merci, Iris. Je m'apprêtais justement à fournir quelques précisions."
    elen "Mais pourquoi t'as mangé le mien ? T'avais le tien !"
    julian "J'avais fini le mien."
    elen "ET ALORS ?!" with vpunch
    elias "Elen, tiens. Prends le mien."
    elen "Non, Elias, mange-le !"
    elias "Mais ça me dérange pas."
    elen "Merci, mais je veux pas que TU sois privé de gâteau."
    elias "Ah... D'accord."
    noam "Qu'est-ce qui se passe ?"
    mara "Julian a bouffé le gâteau d'Elen."
    julian "Ah, parfait ! Encore un témoin pour mon procès."
    noam "Tu l'as mangé ou pas ?"
    julian "Oui."
    noam "Bah..."
    julian "Mais enfin, regarde-la ! On croirait que j'ai assassiné quelqu'un !"
    elen "Tu pouvais juste me demander !"
    julian "Et risquer que tu me dises non ?"
    "Elen récupère son assiette vide et la pousse devant lui."
    elen "Tiens. Va m'en chercher un autre."
    julian "..."
    elen "Bah vas-y !"
    julian "Elen, il n'en reste plus."
    mara "T'as vérifié ?"
    julian "Oui."
    mara "Quand ?"
    julian hesitation "Avant de manger le sien."
    lysa sourire "Ah, ça y est. Le vrai Julian est de retour !"
    julian "Pardon ?"
    lysa "Bah, t'étais presque supportable, hier. Ça commençait à m'inquiéter."
    julian "J'ai fait un effort monumental pour ne pas vous interrompre pendant ce vote."
    noam "Un effort monumental ?"
    julian "Absolument. Et vous voyez le résultat !"
    elen "Quel rapport avec mon gâteau ?"
    julian "Aucun, Elen, laisse-moi finir."
    julian "Si nous avons échoué hier, c'est évidemment parce que j'ai eu la brillante idée de ne pas me mêler de ce vote."
    noam "Ah, carrément. C'est parce que TU n'as rien fait ?"
    julian sourire "Exactement !"
    lysa "Ah bah oui. Bien sûr."
    elen "Julian."
    julian "Oui ?"
    elen "Je veux mon gâteau."
    julian "Je sais, Elen."
    elen "Bon."

    "Je vais me servir et je prends place avec les autres. Elen surveille Julian jusqu'à ce qu'il ait débarrassé son assiette."
    elen "On fait quelque chose ce soir ? J'en ai marre de manger et de retourner dans ma chambre."
    elias "On peut jouer aux cartes."
    elen "Oui ! Elias, tu viens ?"
    elias "Bah oui."
    julian "Je peux vous apprendre un jeu."
    elen "Non."
    julian "Tu ne sais même pas de quel jeu il s'agit !"
    elen "Non."
    mara "Laisse tomber."

    "Je remarque qu'Iris n'a presque pas touché à son repas. Elle regarde l'écran éteint derrière le comptoir."
    kael "Iris, j'ai essayé celui-là aussi."
    iris "Et ?"
    kael "Il n'y a pas de réponse."
    iris "C'est pas ce que je te demande. Tu as regardé les relevés d'hier ?"
    kael "Oui. Il manque une partie des données de la liaison extérieure."
    iris "À partir de quelle heure ?"
    kael "Je suis en train de vérifier."
    iris "Tu m'as dit la même chose tout à l'heure."
    kael "Parce que je n'ai pas terminé."
    iris "Hier, elle nous a demandé de l'aider. Elle nous a dit qu'on lui prenait sa voix. On a tous entendu ça, non ?"
    noam "Oui."
    iris "Alors pourquoi on attend ?"
    mara "Tu veux qu'on fasse quoi, là, tout de suite ?"
    iris colere "J'en sais rien, Mara ! Que vous veniez chercher avec moi, déjà !"
    elen inquiet "On peut t'aider après manger si tu veux..."
    iris "Laisse tomber."
    "Iris repousse sa chaise."
    elias inquiet "Tu finis pas ?"
    iris "Non. J'ai pas faim."
    kael "Tu retournes aux archives ?"
    iris "Je vais d'abord passer à l'infirmerie."
    kael "J'ai déjà vérifié les relais."
    iris "Je vais vérifier quand même."
    "Elle quitte la pièce."

    menu:
        "Suivre Iris jusqu'à la porte.":
            $ j701_table_choice = "inquietude"
            $ j701_iris_defense = True
            noam "Iris !"
            iris fatigue "Quoi ?"
            noam "Je te mets ton assiette de côté ?"
            iris "Non. Mangez-la."
            noam "Tu sais, si tu veux qu'on regarde un truc..."
            iris "Si ta tablette reçoit quelque chose de Kami, tu me le dis. Même si tu comprends pas ce que c'est."
            noam "Oui. Bien sûr."
            iris "Merci."
        "Rester auprès d'Elen.":
            $ j701_table_choice = "complicite"
            elen triste "J'aurais dû attendre avant de proposer ça."
            noam "Proposer quoi ?"
            elen "Les cartes."
            noam "Elen, t'as rien fait. Elle est inquiète."
            elen "Je sais. Ça fait deux jours qu'elle est comme ça..."
            noam "Tu peux quand même jouer ce soir."
            elen "Ouais."
        "Demander à Julian de changer de sujet.":
            $ j701_table_choice = "julian"
            noam "Alors, c'était quoi ton jeu de cartes ?"
            julian "Tu veux vraiment que je t'explique maintenant ?"
            noam "Bah, si tu veux."
            julian "Plus tard."
            "Il ne reprend pas la conversation."

    $ hideGroup()
    $ showGroup([
        ("julian", "neutre"), ("lysa", "neutre"), ("elias", "neutre"),
        ("mara", "neutre"), ("kael", "fatigue"), ("elen", "joie")
    ])
    "Kael prend sa tablette, toujours reliée à une batterie externe."
    elias "Kael, tu laisses ça ?"
    kael "Quoi ?"
    elias "Ton assiette."
    kael "Ah. Oui."
    "Il prend le morceau de pain qui reste dessus et s'en va."
    lysa "Tiens, Noam."
    "Elle me tend son assiette à dessert."
    noam "T'es sûre ?"
    lysa "Ouais."
    noam "Je peux vraiment le manger ?"
    lysa "Oui, Noam."
    "Elen se retourne vers moi."
    noam "C'est Lysa qui me le donne !"
    elen "J'ai entendu !"
    lysa "Garde-en un peu pour Iris, si tu la croises. Je crois qu'elle a rien mangé aujourd'hui."
    $ hideGroup()
    jump _7_0_1_TEMPS_LIBRE_1


label _7_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflechit", 0.31), ("noam", "neutre", 0.72)])
    "Kael est assis sur une caisse, sa tablette posée sur les genoux."
    noam "Tu comptes vraiment bosser ici ?"
    kael "La prise près de la porte fonctionne."
    noam "T'as une tête affreuse."
    kael "J'ai dormi deux heures."
    noam "Et ça avance ?"
    kael "Regarde. Ça, c'est l'heure enregistrée par le Conclave. Et ça, c'est celle de l'observatoire."
    noam "C'est pas la même."
    kael "Voilà. Je ne sais même pas lequel des deux relevés est fiable."
    if j601_fracture_trace_saved:
        kael "Tu as encore la trace du piratage ? Sur ta tablette."
        noam "Oui. Je te l'envoie ?"
        kael "Non, garde le fichier original. Je regarderai directement dessus."
        $ j701_evidence_note = True
    else:
        kael "Dommage qu'on n'ait pas un enregistrement complet de ce qu'on a vu hier."
        noam "Même avec nos tablettes ?"
        kael "J'ai rien trouvé d'exploitable pour l'instant."
    noam "Tu crois que Kami peut se remettre en route toute seule ?"
    kael "C'est possible."
    noam "OK..."
    "Il cherche son crayon. Il finit par le retrouver coincé derrière son oreille."
    kael "Ah."
    noam "Va dormir un peu, Kael."
    kael "Quand j'aurai terminé ça."
    noam "Ouais. Bon courage."
    $ hideGroup()
    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1


label _7_0_1_APRES_MIDI_TOMAS_CANON:
    $ current_period = "Après-midi"
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.29), ("noam", "neutre", 0.72)])
    tomas "Noam ! T'étais avec Iris ce midi, non ?"
    noam "À table, ouais. Pourquoi ?"
    tomas "Elle a mangé quelque chose ?"
    noam "Pas grand-chose. Elle est partie avant la fin du repas."
    tomas "Je viens de passer aux archives. Je lui avais laissé à manger, elle y a même pas touché."
    noam "T'as essayé de lui parler ?"
    tomas "Oui. Elle m'a dit qu'elle avait pas besoin de moi."
    noam "Ça m'étonne pas."
    tomas "Je sais, mais... Je l'ai déjà trouvée là-bas cette nuit."
    noam "Cette nuit ?"
    tomas "Vers trois heures. Je dormais pas, je suis sorti chercher de l'eau. Elle avait sorti des dossiers partout et elle regardait les enregistrements d'hier."
    noam "Elle faisait encore ça ce matin ?"
    tomas "Ouais. Quand je suis repassé ce matin, elle était toujours sur le même écran. Elle avait même pas enlevé sa veste."
    noam "Elle a rien trouvé ?"
    tomas "Elle m'a rien dit."
    "Tomas vérifie quelque chose sur sa tablette."
    tomas "J'ai voulu l'aider, alors j'ai regardé les données des sanctions. Noam... Viens voir. Je voudrais être sûr que je me trompe pas."
    noam "Tu as trouvé quoi ?"
    tomas "Viens au canon, c'est encore affiché."
    noam "OK."
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Tomas connecte sa tablette à la console. Les données de quatre flux apparaissent à l'écran, mais plusieurs valeurs changent sans arrêt."
    tomas "C'est le registre des sanctions. J'essaie de récupérer les dernières données fiables."
    noam "Il y a que des erreurs, là."
    tomas "Oui. Il faut stabiliser chaque flux pour retrouver le total. J'y suis arrivé sur trois d'entre eux, mais sur le dernier..."
    noam "Montre-moi."
    tomas "Merci."
    $ hideGroup()
    call j701_play_console from _call_j701_play_console
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])

    "Les valeurs cessent de défiler. Le total général s'affiche."
    "0."
    noam surpris "Attends. Zéro sanction ?"
    tomas "Oui."
    noam "Remets les données d'hier."
    "Tomas fait défiler les relevés."
    noam "Là, on en a."
    tomas "Oui. Jusqu'au piratage."
    noam "Et après ?"
    tomas "Rien."
    noam "Dans tous les districts ?"
    tomas "Regarde."
    "Il ouvre le détail des quatre flux. Le chiffre ne change pas."
    noam "T'as vérifié ailleurs ?"
    tomas "J'ai pas réussi à ouvrir les registres des archives. Ici, j'ai encore accès aux relevés locaux."
    noam "Donc on reçoit peut-être juste plus les données."
    tomas "C'est possible."
    noam "Mais si les données sont bonnes..."
    "Tomas ne répond pas. Je ressors ma tablette et ouvre la messagerie."
    tomas "Tu fais quoi ?"
    noam "Je vais demander à quelqu'un sur Terre s'il a remarqué quelque chose."
    tomas inquiet "Attends, non !"
    noam "Pourquoi ?"
    tomas "Tu vas lui demander quoi, exactement ? S'il a vu quelqu'un enfreindre un Commandement sans mourir ?"
    noam "Je vais pas lui demander de le faire lui-même !"
    tomas "Je sais, mais imagine qu'il en parle à quelqu'un d'autre. On peut pas leur dire que les sanctions sont arrêtées, on en sait rien."
    noam "Tomas, je voulais juste savoir s'il s'était passé quelque chose."
    tomas "S'il te plaît. Attends qu'on ait vérifié."
    "Je regarde le message que j'ai commencé à taper. Je l'efface."
    noam "OK. J'envoie rien."
    tomas "Merci."
    noam "T'as sauvegardé tout ça ?"
    tomas "Oui. Une copie et une photo de l'écran. J'ai déjà perdu un fichier en essayant de l'ouvrir."
    noam "On devrait montrer ça à Kael."
    tomas "J'ai essayé de le trouver ce matin. Il était occupé et... je voulais pas lui amener un problème de plus si c'était moi qui lisais mal le tableau."
    noam "Là, on est deux à le lire."
    tomas "Ouais."
    "Je regarde encore l'écran. J'aimerais qu'un autre nombre apparaisse, juste pour être sûr que le compteur fonctionne. Je n'arrive pas à me réjouir de ce zéro."

    call play_stat_dialogue("d7_0_1") from _call_stat_dialogue_d7_0_1
    menu:
        "Respecter sa demande de discrétion jusqu'au lendemain.":
            $ j701_tomas_secret_kept = True
            noam "On vérifie demain, tous les deux. On en parle pas d'ici là."
            tomas neutre "D'accord."
            noam "Et si tu vois Iris, dis-lui de manger quelque chose."
            tomas "J'ai laissé de quoi manger à côté d'elle. J'irai voir si elle y a touché."
        "Demander à Tomas de prévenir Kael dès maintenant.":
            $ j701_tomas_secret_kept = False
            $ j701_tomas_informed = True
            noam determine "Envoie les relevés à Kael. Juste les relevés. On lui demande de vérifier."
            tomas inquiet "Tu crois qu'il aura le temps ?"
            noam "Il verra ça quand il pourra. Il faut qu'il les ait."
            "Tomas ouvre la messagerie et joint les deux fichiers."
            tomas "C'est bon. Je lui ai demandé de me répondre demain."
            noam "Merci."

    "Avant de sortir, je me retourne une dernière fois vers la console."
    "Toujours zéro."
    $ hideGroup()
    jump _7_0_1_SOIREE_TENSION_LEGERE


label _7_0_1_SOIREE_TENSION_LEGERE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_287
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2
    $ showGroup([
        ("iris", "fatigue"), ("julian", "neutre"), ("lysa", "neutre"),
        ("kael", "fatigue"), ("elias", "inquiet"), ("mara", "neutre"),
        ("elen", "sourire"), ("noam", "neutre")
    ])
    "Elen a finalement réussi à organiser sa partie de cartes. Iris est revenue elle aussi, mais elle n'a pas l'air de vouloir jouer."
    julian "Il manque l'as de pique."
    elen "T'es sûr ?"
    julian "Oui. J'ai compté."
    elen "Tu veux que je recompte ?"
    julian "Non !"
    lysa "On peut jouer sans, non ?"
    julian "Pas à ce jeu-là."
    mara "Alors change de jeu."
    julian "..."
    elen "Donne, je vais distribuer."
    elias inquiet "Vous avez vu les batteries du stockage ?"
    elen "Hein ?"
    elias "Les deux grosses. Je les retrouve pas."
    kael "T'as regardé avec les nouvelles caisses ?"
    elias "Oui. J'ai regardé trois fois."
    kael "On regardera demain."
    elias colere "Mais tu m'as déjà dit ça ce matin !"
    "Kael relève les yeux. Elen arrête de distribuer."
    elias "Pardon. C'est pas juste les batteries. Il y a un micro-soudeur et des stabilisateurs qui ont disparu aussi."
    mara "Depuis quand ?"
    elias "Je sais pas. Je m'en suis rendu compte ce matin."
    kael "Le micro-soudeur, c'est peut-être moi."
    elias "J'ai regardé sur ton établi."
    kael "Ah."
    elias "Et il manque des outils de coupe. Si quelqu'un a pris quelque chose, c'est pas grave, je veux juste savoir où c'est."
    elen inquiet "On regarde ensemble après la partie ?"
    "Elias pose ses cartes sur la table."
    elias "Non, c'est bon. Jouez."
    elen "Mais Elias..."
    kael "Attends. Les batteries, c'est celles de la grosse étagère ? Avec le capteur de masse ?"
    elias "Oui."
    kael "T'es sûr qu'elles y sont plus ?"
    elias "Oui, Kael !"
    kael "Je viens de regarder le registre. Elles sont toujours indiquées en stock."
    "Nyra arrive à la table avec le registre des livraisons."
    $ hideGroup()
    $ showGroup([
        ("nyra", "neutre"), ("kael", "reflechit"), ("elias", "inquiet"),
        ("lysa", "neutre"), ("mara", "neutre"), ("elen", "inquiet"), ("julian", "neutre")
    ])
    nyra "Quelles batteries ?"
    elias "Les deux grosses du stockage."
    nyra "Le système enregistre automatiquement le poids de cette étagère. Si elles n'y sont plus, ça doit apparaître."
    lysa "Et si quelqu'un a posé autre chose à la place ?"
    "Nyra et Kael se regardent."
    kael "Je vais voir."
    elias "Viens. Je vais te montrer."
    elen "Attendez... Vous pensez que quelqu'un a pris tout ça exprès ?"
    mara "On va d'abord vérifier."
    "Elen ramasse les cartes. Julian soulève son bras pour lui en rendre une."
    elen "L'as de pique..."
    julian "Ah."
    "Elle le remet dans le paquet sans rien dire."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE


label _7_0_1_FIN_JOURNEE:
    "Nous finissons par fermer le stockage. Nous n'avons retrouvé aucune des pièces manquantes."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([("elen", "neutre", 0.32), ("noam", "neutre", 0.72)])
    "Je retrouve Elen devant la chambre de Ryn. Elle a une assiette à la main."
    noam "Tu lui apportes à manger ?"
    elen "Ouais. Il est pas venu ce soir."
    noam "Tu lui as demandé ?"
    elen "Il m'a dit de le laisser tranquille."
    noam "Ah."
    elen "Je vais la laisser là. Il la prendra s'il a faim."
    "Elle pose l'assiette près de la porte."
    elen "Il pourrait au moins nous dire quand il veut pas manger avec nous. J'avais mis une place pour lui."
    noam "T'as prévu douze places tous les soirs ?"
    elen "Bah oui."
    noam "D'accord."
    elen "Tu veux que j'enlève la sienne ?"
    noam "Non. Laisse-la."
    elen "Ouais."
    elen "Bon, bonne nuit, Noam."
    noam "Bonne nuit."
    $ hideGroup()

    if j701_tomas_secret_kept:
        "Ma tablette vibre. Tomas m'écrit : « Je revérifie demain matin. J'en ai parlé à personne. »"
        "Je lui réponds : « OK. Essaie de dormir un peu. »"
    else:
        "Ma tablette vibre. Tomas m'écrit : « Kael a reçu les fichiers. Il regardera demain. »"
        "Je lui réponds : « OK, merci. »"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je retire ma veste et la jette sur le lit. Le tiroir du bureau est entrouvert."
    "Je m'approche pour le refermer. Il manque quelque chose à côté du cadre."
    noam surpris "Hein ?"
    "Le dessin de Juliette. Je soulève le cadre, puis ma tablette. Je regarde dans le tiroir."
    noam "Attends..."
    "Il était là ce matin. J'ai récupéré ma chaussette en dessous et je l'ai reposé. Je m'en souviens très bien."
    "J'ouvre la boîte dans laquelle je l'avais apporté. Elle est vide."
    "Je cherche derrière le bureau, sous le lit, puis dans les poches de ma veste, même si je sais qu'il n'y rentre pas."
    noam inquiet "Je l'ai pas sorti d'ici..."
    "Je regarde la porte. Elle est fermée."
    "Je refais le tour du bureau, cette fois en déplaçant tout ce qui se trouve dessus."
    "Rien."
    "J'ouvre ma messagerie. Lysa est en haut de la liste."

    menu:
        "Demander à Lysa de m'aider à chercher demain.":
            $ j701_lysa_search_help = True
            "Je lui écris : « Tu dors ? J'ai perdu un truc dans ma chambre. Tu pourrais m'aider demain ? »"
            "Elle répond presque aussitôt."
            lysa "Oui. Tu veux pas que je vienne maintenant ?"
            noam "Non, demain ça ira. Merci."
            lysa "OK. Je passe demain matin."
        "Garder la disparition pour moi cette nuit.":
            "Je commence à écrire un message, puis je l'efface."
            "Si je lui demande de venir et qu'on le retrouve dans un tiroir en deux minutes, je vais avoir l'air malin."
            "Je pose ma tablette."

    $ noam_has_juliette_drawing = False
    "Je récupère la boîte vide et la pose sur le bureau. Juliette m'avait demandé trois fois de faire attention au dessin pendant le trajet."
    "Je vais vérifier la porte."
    "VERROUILLÉE."
    "Je tire quand même sur la poignée."
    $ hideGroup()
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_1_0_0_CANON
