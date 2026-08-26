default j701_plate_step = 0
default j701_plate_score = 0
default j701_plate_errors = 0
default j701_plate_time = 8
default j701_plate_combo = 0
default j701_plate_wobble = 0
default j701_plate_feedback = ""
default j701_calm_score = 45
default j701_calm_node = "start"
default j701_calm_depth = 0
default j701_calm_time = 6
default j701_calm_feedback = ""
default j701_calm_done = False
default j701_calm_last_line = ""
default j701_console_rings = []
default j701_console_locked = []
default j701_console_error_ticks = []
default j701_console_errors = 0
default j701_console_noise = 0
default j701_console_feedback = ""
default j701_console_phase = "play"
default j701_clean_particles = []
default j701_clean_score = 0
default j701_clean_time = 22
default j701_clean_next_id = 0
default j701_clean_mouse_x = 960
default j701_clean_mouse_y = 540
default j701_clean_reveal = 0
default j701_clean_feedback = ""

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

    J701_PLATE_ORDERS = [
        {"who": "Julian", "line": "Le pain va tomber de mon côté.", "want": "pain", "lane": 0, "tone": "blague"},
        {"who": "Iris", "line": "Quelqu'un peut me passer l'eau avant que Julian négocie avec elle ?", "want": "eau", "lane": 2, "tone": "relance"},
        {"who": "Lysa", "line": "La ration chaude, avant qu'elle devienne un concept.", "want": "ration", "lane": 1, "tone": "calme"},
        {"who": "Mara", "line": "Laisse une part au centre. On va éviter le drame diplomatique.", "want": "part", "lane": 3, "tone": "partage"},
    ]

    J701_PLATE_BUTTONS = [
        ("pain", "Pain", "#d4a45f", 0.18, 0.62, "sec"),
        ("eau", "Eau", "#7bc7ff", 0.38, 0.70, "stable"),
        ("ration", "Ration", "#ffb05c", 0.59, 0.62, "chaud"),
        ("part", "Partage", "#b8f0a0", 0.79, 0.70, "centre"),
    ]

    J701_CALM_NODES = {
        "start": {
            "speaker": "Iris",
            "line": "Je veux que ça DUUURE... Si on a enfin une journée sans voix divine, je refuse qu'on la passe à fixer les murs.",
            "choices": [
                ("Alors impose une minute de fête officielle.", "iris_fete", 12, "Iris lève son verre comme si elle venait de fonder un pays."),
                ("Tu crois vraiment qu'elle est partie ?", "kami_absente", -16, "Le nom de Kami aspire l'air autour de la table."),
                ("Julian peut faire le discours, il adore s'écouter.", "julian_discours", 9, "Julian prend l'attaque comme une promotion."),
                ("On devrait quand même rester prudents.", "lysa_prudence", -5, "La prudence est juste. Elle est aussi lourde."),
            ],
        },
        "iris_fete": {
            "speaker": "Iris",
            "line": "Minute de fête officielle ? J'aime. Il nous faut un rituel idiot, tout de suite.",
            "choices": [
                ("Lever les verres à la santé du silence.", "final_good", 12, "Les verres se lèvent. Le silence devient presque une présence invitée."),
                ("Déclarer Julian mascotte temporaire.", "final_fun", 8, "Julian proteste trop vite pour être crédible."),
                ("Proposer une minute sans parler de Kami.", "final_best", 15, "La règle est simple. Tout le monde l'accepte."),
            ],
        },
        "kami_absente": {
            "speaker": "Lysa",
            "line": "Partie ? Non. C'est justement ça qui me gêne. Elle ne disparaît pas. Elle attend.",
            "choices": [
                ("Alors on lui vole six minutes.", "final_good", 10, "Lysa te regarde, puis accepte cette petite désobéissance."),
                ("Tu as raison, ça sent mauvais.", "final_bad", -12, "La table retombe dans le réel."),
                ("Peut-être qu'elle nous écoute paniquer.", "final_bad", -14, "Mauvaise image. Les épaules se tendent."),
            ],
        },
        "julian_discours": {
            "speaker": "Julian",
            "line": "Je peux improviser un discours historique. Court, brillant, indispensable.",
            "choices": [
                ("Trois mots maximum.", "final_fun", 10, "Julian mime une blessure politique grave."),
                ("Vas-y, président de la table.", "final_good", 9, "Il se redresse comme si c'était sérieux. C'est ce qui sauve la blague."),
                ("Non. On mange.", "final_flat", 2, "Le repas continue. Sans éclat, mais sans casse."),
            ],
        },
        "lysa_prudence": {
            "speaker": "Lysa",
            "line": "Merci. Je sais que je casse l'ambiance, mais je n'arrive pas à trouver ça normal.",
            "choices": [
                ("Tu ne casses rien. Tu vérifies les murs.", "final_good", 11, "La formule lui arrache presque un sourire."),
                ("Alors laisse-moi casser l'ambiance à ta place.", "final_fun", 7, "Elle te laisse faire. C'est déjà un accord."),
                ("Tu stresses pour rien.", "final_bad", -16, "Elle se ferme aussitôt. Mauvais angle."),
            ],
        },
        "final_best": {"speaker": "Table", "line": "Pendant une minute, personne ne dit son nom.", "choices": []},
        "final_good": {"speaker": "Table", "line": "La table respire encore un peu.", "choices": []},
        "final_fun": {"speaker": "Table", "line": "La blague tient juste assez longtemps pour devenir utile.", "choices": []},
        "final_flat": {"speaker": "Table", "line": "Le calme reste là, moins brillant, mais intact.", "choices": []},
        "final_bad": {"speaker": "Table", "line": "Le calme se fend. Pas beaucoup. Assez.", "choices": []},
    }

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

    J701_CLEAN_SPRITES = [
        "gui/day7/clean/dust_1.png",
        "gui/day7/clean/dust_2.png",
        "gui/day7/clean/dust_3.png",
        "gui/day7/clean/dust_4.png",
        "gui/day7/clean/glitch_dust_1.png",
        "gui/day7/clean/glitch_dust_2.png",
    ]

    def j701_plate_reset():
        store.j701_plate_step = 0
        store.j701_plate_score = 0
        store.j701_plate_errors = 0
        store.j701_plate_time = 8
        store.j701_plate_combo = 0
        store.j701_plate_wobble = 0
        store.j701_plate_feedback = "Le plateau glisse de main en main. Suis la demande avant que la conversation déraille."

    def j701_plate_pick(item_id):
        if store.j701_plate_step >= len(J701_PLATE_ORDERS):
            return
        expected = J701_PLATE_ORDERS[store.j701_plate_step]["want"]
        if item_id == expected:
            store.j701_plate_score += 1
            store.j701_plate_combo += 1
            store.j701_plate_wobble = max(0, store.j701_plate_wobble - 12)
            store.j701_plate_feedback = "Bon geste. Le repas continue sans accroc."
            store.j701_plate_step += 1
            store.j701_plate_time = 8
        else:
            store.j701_plate_errors += 1
            store.j701_plate_combo = 0
            store.j701_plate_wobble = min(100, store.j701_plate_wobble + 26)
            store.j701_plate_feedback = "Mauvais objet. Quelqu'un rattrape le plateau au dernier moment."
            store.j701_plate_time = max(2, store.j701_plate_time - 2)
        renpy.restart_interaction()

    def j701_plate_tick():
        if store.j701_plate_step >= len(J701_PLATE_ORDERS):
            return
        store.j701_plate_time -= 1
        if store.j701_plate_time <= 0:
            store.j701_plate_errors += 1
            store.j701_plate_combo = 0
            store.j701_plate_wobble = min(100, store.j701_plate_wobble + 18)
            store.j701_plate_feedback = "Trop lent. La demande se perd dans le bruit de la table."
            store.j701_plate_step += 1
            store.j701_plate_time = 8
        else:
            store.j701_plate_wobble = min(100, store.j701_plate_wobble + 2)
        renpy.restart_interaction()

    def j701_calm_reset():
        store.j701_calm_score = 45
        store.j701_calm_node = "start"
        store.j701_calm_depth = 0
        store.j701_calm_time = 6
        store.j701_calm_feedback = "Réponds vite. Trop hésiter, c'est déjà laisser le malaise entrer."
        store.j701_calm_done = False
        store.j701_calm_last_line = ""

    def j701_calm_choose(choice_index):
        if store.j701_calm_done:
            return
        node = J701_CALM_NODES.get(store.j701_calm_node, J701_CALM_NODES["start"])
        if choice_index >= len(node["choices"]):
            return
        label, next_node, effect, feedback = node["choices"][choice_index]
        store.j701_calm_score = max(0, min(100, store.j701_calm_score + effect))
        store.j701_calm_last_line = label
        store.j701_calm_feedback = feedback
        store.j701_calm_node = next_node
        store.j701_calm_depth += 1
        if not J701_CALM_NODES.get(next_node, {}).get("choices", []):
            store.j701_calm_done = True
        else:
            store.j701_calm_time = 6
        renpy.restart_interaction()

    def j701_calm_timeout():
        if store.j701_calm_done:
            return
        store.j701_calm_score = max(0, store.j701_calm_score - 8)
        store.j701_calm_last_line = "..."
        store.j701_calm_feedback = "Noam hésite. La table continue sans lui, un peu moins légère."
        node = J701_CALM_NODES.get(store.j701_calm_node, J701_CALM_NODES["start"])
        if node["choices"]:
            store.j701_calm_node = node["choices"][-1][1]
        store.j701_calm_depth += 1
        store.j701_calm_time = 6
        if not J701_CALM_NODES.get(store.j701_calm_node, {}).get("choices", []):
            store.j701_calm_done = True
        renpy.restart_interaction()

    def j701_calm_tick():
        if store.j701_calm_done:
            return
        store.j701_calm_time -= 1
        if store.j701_calm_time <= 0:
            j701_calm_timeout()
        else:
            renpy.restart_interaction()

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

    def j701_clean_spawn(x=None, y=None, glitch=False):
        import random
        particle = {
            "id": store.j701_clean_next_id,
            "x": x if x is not None else random.randint(190, 1180),
            "y": y if y is not None else random.randint(120, 540),
            "dx": random.choice([-1, 1]) * random.uniform(0.5, 2.2),
            "dy": random.choice([-1, 1]) * random.uniform(0.3, 1.6),
            "sprite": random.choice(J701_CLEAN_SPRITES[4:] if glitch else J701_CLEAN_SPRITES[:4]),
            "glitch": glitch,
            "life": random.randint(5, 9) if glitch else random.randint(7, 12),
        }
        store.j701_clean_next_id += 1
        store.j701_clean_particles.append(particle)

    def j701_clean_reset():
        import random
        store.j701_clean_particles = []
        store.j701_clean_score = 0
        store.j701_clean_time = 22
        store.j701_clean_next_id = 0
        store.j701_clean_mouse_x = 960
        store.j701_clean_mouse_y = 540
        store.j701_clean_reveal = 0
        store.j701_clean_feedback = "Balaye les poussières avant qu'elles se multiplient."
        for i in range(7):
            j701_clean_spawn(glitch=(i >= 5))

    def j701_clean_sweep(particle_id):
        particles = []
        removed = None
        for particle in store.j701_clean_particles:
            if particle["id"] == particle_id:
                removed = particle
            else:
                particles.append(particle)
        if removed:
            store.j701_clean_score += 2 if removed.get("glitch") else 1
            store.j701_clean_reveal = min(100, store.j701_clean_reveal + (18 if removed.get("glitch") else 10))
            store.j701_clean_feedback = "La poussière éclate en silence."
            if removed.get("glitch"):
                store.j701_clean_feedback = "Le parasite se désagrège sous le balai."
        store.j701_clean_particles = particles
        renpy.restart_interaction()

    def j701_clean_tick():
        import random
        if store.j701_clean_score >= 12 or store.j701_clean_time <= 0:
            return
        try:
            mx, my = renpy.get_mouse_pos()
            store.j701_clean_mouse_x = mx
            store.j701_clean_mouse_y = my
        except Exception:
            pass
        store.j701_clean_time = max(0, store.j701_clean_time - 0.25)
        moved = []
        for particle in store.j701_clean_particles:
            particle = dict(particle)
            particle["x"] += particle["dx"]
            particle["y"] += particle["dy"]
            if particle["x"] < 110 or particle["x"] > 1240:
                particle["dx"] *= -1
            if particle["y"] < 90 or particle["y"] > 565:
                particle["dy"] *= -1
            particle["life"] -= 0.25
            if particle["life"] <= 0 and len(store.j701_clean_particles) + len(moved) < 18:
                particle["life"] = random.randint(5, 9)
                moved.append({
                    "id": store.j701_clean_next_id,
                    "x": particle["x"] + random.randint(-80, 80),
                    "y": particle["y"] + random.randint(-60, 60),
                    "dx": -particle["dx"] * random.uniform(0.7, 1.25),
                    "dy": -particle["dy"] * random.uniform(0.7, 1.25),
                    "sprite": random.choice(J701_CLEAN_SPRITES[4:] if particle.get("glitch", False) else J701_CLEAN_SPRITES[:4]),
                    "glitch": particle.get("glitch", False),
                    "life": random.randint(5, 9),
                })
                store.j701_clean_next_id += 1
                store.j701_clean_feedback = "La poussière se divise. Le bureau refuse de rester propre."
            moved.append(particle)
        store.j701_clean_particles = moved
        if random.random() < 0.08 and len(store.j701_clean_particles) < 14:
            j701_clean_spawn(glitch=random.random() < 0.35)
        renpy.restart_interaction()

screen j701_plate_game():
    modal True
    zorder 220
    on "show" action Function(j701_plate_reset)
    timer 1.0 repeat True action Function(j701_plate_tick)
    add Solid("#03070bee")

    $ finished = j701_plate_step >= len(J701_PLATE_ORDERS)
    if not finished:
        $ order = J701_PLATE_ORDERS[j701_plate_step]
    else:
        $ order = {"who": "Table", "line": "Le plateau a survécu au repas.", "want": ""}

    frame:
        xalign 0.5
        yalign 0.08
        xsize 980
        ysize 132
        padding (24, 16)
        background Solid("#07131ff2")
        vbox:
            spacing 6
            text "PLATEAU EN CIRCULATION" size 34 color "#E8F4FF" xalign 0.5
            text "{} : {}".format(kd_tr(order["who"]), kd_tr(order["line"])) size 24 color "#DCE8F7" xalign 0.5 text_align 0.5
            if not finished:
                text "{} : {} / {} {}".format(kd_tr("ton"), kd_tr(order["tone"]), kd_tr("piste"), order["lane"] + 1) size 18 color "#FFDF8A" xalign 0.5

    fixed:
        xalign 0.5
        yalign 0.52
        xsize 1260
        ysize 660
        add Solid("#101820dd") xpos 80 ypos 250 xsize 1100 ysize 180
        add Solid("#ff384855") xpos 80 ypos 250 xsize int(11 * j701_plate_wobble) ysize 180
        add Solid("#283846") xpos 400 ypos 180 xsize 460 ysize 300
        add Solid("#05090a88") xpos 420 ypos 200 xsize 420 ysize 260
        for i in range(6):
            add Solid("#ffffff10") xpos (150 + i * 180) ypos 250 xsize 2 ysize 180
        if not finished:
            add Solid("#ffdf8a55") xpos 88 ypos (260 + order["lane"] * 42) xsize 1084 ysize 30

        for item_id, label, color, xa, ya, hint in J701_PLATE_BUTTONS:
            $ wanted = (not finished and item_id == order["want"])
            button:
                xalign xa
                yalign ya
                xsize 180
                ysize 100
                background Solid(color + ("ff" if wanted else "cc"))
                hover_background Solid("#ffffffdd")
                sensitive not finished
                action Function(j701_plate_pick, item_id)
                vbox:
                    spacing 4
                    text kd_tr(label) size 27 color "#061018" xalign 0.5
                    text kd_tr(hint).upper() size 15 color "#24313a" xalign 0.5
                    text "PASSER" size 17 color "#1b2b34" xalign 0.5

    frame:
        xalign 0.14
        yalign 0.18
        xsize 260
        ysize 96
        padding (14, 10)
        background Solid("#05090add")
        vbox:
            spacing 6
            text "Rythme de table" size 20 color "#9FD8FF" xalign 0.5
            bar value StaticValue(max(0, 100 - j701_plate_wobble), 100):
                xsize 220
                ysize 16
            text "combo x[j701_plate_combo]" size 20 color "#FFDF8A" xalign 0.5

    frame:
        xalign 0.5
        yalign 0.89
        xsize 980
        ysize 116
        padding (20, 12)
        background Solid("#061018ee")
        vbox:
            spacing 8
            hbox:
                spacing 18
                text "Temps" size 23 color "#9FD8FF"
                bar value StaticValue(j701_plate_time, 8):
                    xsize 540
                    ysize 20
                text "OK [j701_plate_score]/4" size 23 color "#B8F0A0"
                text "Ratés [j701_plate_errors]" size 23 color "#FF8A7A"
            text kd_tr(j701_plate_feedback) size 22 color "#E8F4FF" xalign 0.5 text_align 0.5

    if finished:
        timer 0.8 action Return(j701_plate_score)

screen j701_calm_game():
    modal True
    zorder 220
    on "show" action Function(j701_calm_reset)
    timer 1.0 repeat True action Function(j701_calm_tick)
    add "gui/day7/social/branch_ui.png" at cover_screen
    add Solid("#02070b55")

    if not j701_calm_done:
        $ round_data = J701_CALM_NODES.get(j701_calm_node, J701_CALM_NODES["start"])
    else:
        $ round_data = J701_CALM_NODES.get(j701_calm_node, {"speaker": "Table", "line": "Le calme tient encore.", "choices": []})

    fixed:
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

        frame:
            xpos 92
            ypos 92
            xsize 680
            ysize 176
            padding (22, 16)
            background Solid("#07131fcc")
            vbox:
                spacing 8
                text "{} / {}".format(kd_tr("DISCUSSION"), kd_tr(round_data["speaker"])) size 34 color "#E8F4FF"
                text kd_tr(round_data["line"]) size 24 color "#DCE8F7"
                if j701_calm_last_line:
                    text "Noam : {}".format(kd_tr(j701_calm_last_line)) size 20 color "#FFDF8A"

        frame:
            xpos 1420
            ypos 70
            xsize 390
            ysize 112
            padding (16, 12)
            background Solid("#061018dd")
            vbox:
                spacing 8
                hbox:
                    spacing 14
                    text "6s" size 25 color "#FFDF8A"
                    bar value StaticValue(j701_calm_time, 6):
                        xsize 270
                        ysize 20
                bar value StaticValue(j701_calm_score, 100):
                    xsize 350
                    ysize 18
                text (kd_tr("chemin") + " " + str(j701_calm_depth + 1) + "/2") size 18 color "#9FD8FF" xalign 0.5

        for dot in range(3):
            add Solid("#ffdf8a" if dot <= j701_calm_depth else "#516A7A") xpos (102 + dot * 38) ypos 294 xsize 24 ysize 8

        for idx, choice in enumerate(round_data["choices"]):
            $ yline = 154 + idx * 190
            $ effect = choice[2]
            $ tone_color = "#B8F0A0" if effect >= 10 else ("#FF8A7A" if effect < 0 else "#FFDF8A")
            textbutton kd_tr(choice[0]):
                xpos 1100
                ypos yline
                xsize 690
                ysize 96
                text_size 24
                text_xalign 1.0
                background Solid("#07131faa")
                hover_background Solid("#17344bdd")
                action Function(j701_calm_choose, idx)
            add Solid(tone_color) xpos 1070 ypos (yline + 16) xsize 8 ysize 64

        frame:
            xpos 460
            ypos 910
            xsize 1000
            ysize 74
            padding (18, 10)
            background Solid("#061018dd")
            text kd_tr(j701_calm_feedback) size 22 color "#E8F4FF" xalign 0.5 text_align 0.5

    if j701_calm_done:
        timer 0.8 action Return(j701_calm_score)

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

screen j701_search_drawing_game():
    modal True
    zorder 220
    on "show" action Function(j701_clean_reset)
    timer 0.25 repeat True action Function(j701_clean_tick)
    add Solid("#02070bee")
    add "bg_chambre" at adaptive_fullscreen
    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.08
        xsize 920
        padding (22, 14)
        background Solid("#07131fee")
        vbox:
            spacing 6
            text "NETTOYER LE BUREAU" size 36 color "#E8F4FF" xalign 0.5
            text "Balaye les particules avant qu'elles se multiplient. Le dessin n'apparaît nulle part." size 22 color "#9FD8FF" xalign 0.5

    frame:
        xalign 0.5
        yalign 0.53
        xsize 1360
        ysize 650
        background Solid("#091018cc")
        padding (0, 0)
        add Solid("#17202aaa") xpos 120 ypos 270 xsize 1120 ysize 180
        add Solid("#263444dd") xpos 310 ypos 150 xsize 730 ysize 330
        add Solid("#05090acc") xpos 340 ypos 180 xsize 670 ysize 270
        add Solid("#d8e6ef22") xpos 488 ypos 230 xsize max(8, int(j701_clean_reveal * 3.8)) ysize 92
        add Solid("#ffdf8a55") xpos 488 ypos 230 xsize 380 ysize 4
        add Solid("#ffdf8a55") xpos 488 ypos 318 xsize 380 ysize 4

        for particle in j701_clean_particles:
            imagebutton:
                idle Transform(particle["sprite"], zoom=0.34)
                hover Transform("gui/day7/clean/sweep_ring.png", zoom=0.38)
                xpos int(particle["x"])
                ypos int(particle["y"])
                xanchor 0.5
                yanchor 0.5
                action Function(j701_clean_sweep, particle["id"])

    frame:
        xalign 0.5
        yalign 0.88
        xsize 920
        ysize 96
        padding (18, 12)
        background Solid("#061018ee")
        vbox:
            spacing 8
            hbox:
                spacing 18
                xalign 0.5
                text "Temps" size 22 color "#9FD8FF"
                bar value StaticValue(max(0, j701_clean_time), 22):
                    xsize 520
                    ysize 18
                text "Nettoyé [j701_clean_score]/12" size 22 color "#FFDF8A"
            hbox:
                spacing 18
                xalign 0.5
                text "Trace révélée" size 20 color "#9FD8FF"
                bar value StaticValue(j701_clean_reveal, 100):
                    xsize 480
                    ysize 14
            text kd_tr(j701_clean_feedback) size 23 color "#E8F4FF" xalign 0.5 text_align 0.5

    add Transform("gui/day7/clean/broom.png", zoom=0.32) xpos j701_clean_mouse_x ypos j701_clean_mouse_y xanchor 0.18 yanchor 0.18

    if j701_clean_score >= 12 or j701_clean_time <= 0:
        timer 0.9 action Return(True)

label j701_play_plate:
    call screen j701_plate_game
    return

label j701_play_calm:
    call screen j701_calm_game
    return

label j701_play_console:
    call screen j701_console_game
    return

label j701_play_search_drawing:
    call screen j701_search_drawing_game
    return

label _7_0_1_REVEIL_CHAMBRE:

    scene black
    $ current_period = "Matin"

    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    $ current_day = 7
    $ noam_has_juliette_drawing = False

    $ blink()

    play sound sfx_knock volume 4.0
    "BAM BAM BAM."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()

    "Je me redresse d'un coup."

    think "Merde. Pourquoi on me réveille en pleine nuit ?!"

    play sound sfx_knock volume 4.0
    "Je repousse la couette."
    "Je manque de me prendre les pieds dedans."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_277
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je traverse la chambre à moitié réveillé puis j'ouvre la porte."

    "J'ouvre la porte."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_278
    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("lysa", "neutre", 0.75),
        ("noam", "neutre", 0.25),
    ])

    lysa surpris "..."

    noam surpris "Quoi ? Qu'est-ce qui se passe ?"

    lysa surpris "Rien."

    noam panne "Rien ? Mais pour..."

    lysa taquin "Enfin... C'est pas une catastrophe quoi."

    "Je la regarde droit dans les yeux. Elle ne cille pas. Puis son regard descend et remonte."
    "Comme si elle m'analysait. T-shirt froissé. Cheveux en pagaille. Pyjama."
    think "Oh mon dieu, la honte..."

    lysa taquin "Je vais m'abstenir de tout commentaire."

    noam desaccord "Tu vas pas commencer à me juger ? Je croyais qu'on était attaqués vu comment tu tambourinais sur la porte."

    lysa rire "C'est ta couette qui t'a attaqué, oui !"

    noam "Très drôle... Sérieux... Pourquoi tu me réveilles en pleine nuit si c'est pas important ?"

    lysa taquin "En pleine nuit ? Il est quasi midi..."

    noam surpris "Hein ?! Quoi ?!"

    lysa "Je crois que tu as bien entendu."

    noam panne "Hein ?! Pourquoi personne m'a réveillé ?"
    noam hesitation "J'ai loupé l'annonce... Ah, c'est tout..."

    "Elle me coupe la parole."
    lysa neutre "Parce que quasiment personne ne s'est levé."

    $ blink()

    noam surpris "Personne ?"

    lysa taquin "Écoute, laisse-moi entrer avant que tout le monde te voit dans ton plus bel attirail."
    think "Ouais, c'est franchement ce dont je préférerais me passer."

    $ hideGroup()

    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")

    pause 2.0

    lysa reflechit "En fait, y'a pas eu d'annonce."
    lysa taquin "Pas de petite voix divine pour se moquer de nous ce matin."

    "Je tourne instinctivement la tête vers l'écran dans ma chambre. Il est noir. Complètement noir."

    think "... Elle n'a pas parlé. Pourquoi changerait-elle ses habitudes ?"

    noam hesitation "Depuis ce matin ?"

    lysa neutre "Pour être plus précise, depuis le vote d'hier même."

    noam inquiet "Et personne ne trouve ça inquiétant ?"

    lysa reflechit "Si. Enfin je pense, pas grand monde n'est levé pour le moment. À croire que sans réveil vous continuez tous à côtoyer Morphée."
    lysa sourire "Faut dire que ça fait un bail qu'on a pas pu dormir sans être réveillés le matin... Et c'est assez agréable."

    "Je regarde encore l'écran. Il ne bouge pas d'un iota. Rien. Toujours rien."

    noam taquin "On a la paix pour une fois."
    noam taquin "Donc tu as défoncé ma porte pour me dire que tout va bien."

    lysa desaccord "J'ai pas défoncé la porte."

    noam "BAM BAM BAM."

    lysa desaccord "J'ai toqué normalement."

    noam colere "Tu as toqué comme une malade mentale !"
    noam colere "Tellement que j'ai sauté de mon lit !"

    lysa blase "C'est toi qui es fragile aussi..."

    noam "Je suis en pyjama devant une représentante officielle d'[codex_dialogue_link('harmonie', 'Harmonie')]."

    lysa rire "J'avais remarqué."
    lysa rire "Monsieur le représentant officiel d'[codex_dialogue_link('harmonie', 'Harmonie')]."

    "Elle détourne le regard. Cette fois, pour de vrai."

    lysa culpabilite "Désolée. Je pensais vraiment que tu étais levé."
    lysa taquin "Disons que je te voyais comme plus responsable que ça."
    lysa taquin "Mais non, tu es surtout décoiffé."

    noam colere "Tes excuses ne sont PAS acceptées !"
    noam taquin "Tu ne comprends pas, c'est une stratégie."

    lysa "Hein ? Qu'est-ce que tu veux dire par là ? Pour faire quoi ?"

    noam taquin "C'est pour désorienter l'ennemi."

    lysa taquin "Si c'est moi ton ennemie, alors... On peut dire que ça marche."

    $ blink()

    lysa neutre "La cafétéria commence à se remplir. Les hommes-taupes commencent à sortir de leurs grottes."

    lysa sourire "Ils doivent commencer à avoir une sacrée faim."
    lysa taquin "Toi aussi tu dois avoir faim non ?"

    noam rire "Tu as raison, je crois bien que mon estomac crie famine."

    lysa "Je t'attends ?"

    noam "Laisse-moi deux minutes."

    lysa blase "Deux seulement ? Pour rattraper tout ça ?"

    noam "Cinq."

    lysa sourire "C'est déjà un tout petit peu plus crédible."

    "Elle recule d'un pas."

    lysa neutre "Je t'attends devant la porte."
    lysa taquin "Ne me fais pas trop attendre."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_279
    scene bg_chambre at adaptive_fullscreen with dissolve

    "La porte se referme. Je reste debout au milieu de la chambre."
    think "Pourquoi j'ai un très mauvais pressentiment ?"

    "Encore en pyjama."
    "Encore à moitié réveillé."

    "Mais plus vraiment paniqué."

    "Je regarde l'écran. Noir. Pas de visage souriant. Pas de voix enfantine. Pas de consignes dramatiques."

    think "Elle n'est pas là. Du moins, pas maintenant."

    "Un vrai soulagement me traverse."
    "Net." id j701_reveil_soulagement_net
    "Presque honteux."

    think "Tant pis."

    "Je vais rapidement dans la salle de bain pour me refaire une beauté."
    noam sourire "Lysa m'attend, je ne devrais pas la faire attendre."

    scene bg_cg026 at adaptive_fullscreen with dissolve

    "Je passe de l'eau sur mon visage."
    "Dans le miroir, j'ai l'air de quelqu'un qu'on n'a réveillé pendant une évacuation."

    think "Tu m'étonnes qu'elle se moque de moi."

    "Je respire un coup. Je cherche mes vêtements."
    "J'enfile ce qui me tombe sous la main."

    scene bg_cg026_1 at adaptive_fullscreen with dissolve

    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    
    think "Bon je ressemble toujours à rien, mais c'est au moins mieux qu'avant."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_280
    scene bg_chambre at adaptive_fullscreen with dissolve

    "J'enfile ma veste puis je cours rejoindre Lysa dans le couloir."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je sors enfin de ma chambre."
    "Lysa m'attend un peu plus loin, adossée au mur."
    "Avant que je la rejoigne, Nyra débouche du couloir et passe une tête à travers la porte qui mène au couloir."
    "Elle a les bras chargés de fournitures, un carton calé contre la hanche."

    $ showGroup([
        ("nyra", "neutre", 0.72),
        ("noam", "neutre", 0.28),
    ])

    nyra colere "Et VOUS DEUX !!"
    
    noam surpris "Nyra ? Qu'est-ce que tu fous ? Tu déménages le stockage ?"

    nyra taquin "Le Conclave a reçu une livraison apparemment tôt ce matin : des fournitures, quelques pièces de maintenance, et assez de cartons pour qu'on s'en occupe à trois."
    nyra colere "Alors bougez-vous bordel ! C'est assez lourd comme ça."

    "Lysa soupire puis commence à s'approcher du couloir. Je fais de même."

    $ showGroup([
        ("nyra", "neutre", 0.80),
        ("lysa", "neutre", 0.50),
        ("noam", "neutre", 0.28),
    ])

    noam reflexion "Une livraison le matin où Kami ne parle pas..."

    lysa reflechit "C'est bizarre qu'elle n'ait pas fait d'annonce pour l'annoncer."

    nyra triste "L'important, c'est qu'on soit livré. Les stocks de nourriture commençaient à baisser drastiquement."

    "Elle réajuste le carton contre elle."

    nyra reflechit "Bon écoutez, pour aller plus vite, on va chacun s'occuper d'une pièce."
    nyra reflechit "On va trier toutes les affaires pour aller dans les différentes pièces : cafétéria, infirmerie, salle de maintenance, salle de stockage."
    nyra taquin "Il faudra mettre correctement les affaires dans chaque pièce. Puis chacun amènera la caisse dans la salle dédiée. Compris ?"

    lysa blase "Su-per. Évitez de vous tromper, je préfèrerais éviter de devoir tout retrier après."

    $ hideGroup()

    # /!\ Minijeu de rangement

    call rangement_play from _call_rangement_day7

    jump _7_0_1_CAFETERIA

# Durée : ~3m00

label _7_0_1_CAFETERIA:

    call show_custom_title("Je termine de ranger les caisses.") from _call_show_custom_title_01
    pause 2.0
    call show_custom_title("Puis je me rends à la cafétéria.") from _call_show_custom_title_1
    pause 2.0

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_282
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    "Pour une fois, la cafétéria est particulièrement vivante. Ça parle. Ça circule. Ça respire."
    "Comme si nous avions tous digéré l'échec prévisible d'hier."

    $ showGroup([
        ("iris",   "sourire"),
        ("julian", "decontracte"),
        ("lysa",   "neutre"),
        ("elias",  "detendu"),
        ("mara",   "rire"),
        ("kael",   "fatigue"),
        ("elen",   "joie"),
    ])

    iris sourire "Franchement ? Si on m'avait dit qu'un jour Kami pouvait bugger comme ça..."
    iris rire "Je n'y aurais jamais cru."

    julian decontracte "Ah mais complètement."
    julian joie "Le meilleur réveil depuis notre arrivée. J'ai enfin pu DORMIR !"

    mara taquin "MDR ! C'est pas toi qui arrive souvent en retard le matin ? Genre ça t'empêche de dormir les annonces de Kami."

    julian taquin "Mais je ne te permets pas. Évidemment que les annonces pour le moins agaçantes de Kami me stressent."
    julian decontracte "C'est justement pour ça que je prends mon temps le matin !"

    iris rire "Ouais ouais, bien sûr. Tu n'as jamais vraiment été à l'heure, Julian. JAMAIS."

    call show_custom_title("Le repas se déroule sans accroc pendant de longues minutes.") from _call_show_custom_title_02
    pause 2.0

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_283
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris",   "sourire"),
        ("julian", "decontracte"),
        ("lysa",   "neutre"),
        ("elias",  "detendu"),
        ("mara",   "rire"),
        ("kael",   "fatigue"),
        ("elen",   "joie"),
    ])

    lysa triste "Tu vas peut-être me prendre pour une folle. Mais tout ça ne me rassure pas vraiment. Le fait que Kami ne dise plus rien."

    noam "Tu préfères quand elle nous parle comme à des chiens ? Qu'elle nous utilise à sa guise."

    lysa blase "Non. Mais au moins, on savait à quoi s'en tenir."

    mara reflexion "On sait toujours à quoi s'en tenir. Les règles n'ont pas changé."
    mara neutre "La seule différence c'est que cette pétasse ne nous a pas cassé les couilles ce matin !"

    elen taquin "La mauvaise humeur et le pessimisme devraient être tout simplement IN-TER-DITS!"
    elen joie "Et si on mettait ça au vote prochainement ?"

    iris taquin "Tu veux être responsable d'un massacre de masse ?"

    elen surpris "Quoi ? On peut espérer non ?"

    mara surpris "Tu espères un massacre de masse ?!"

    elen triste "Quoi ?! Mais nan !! Je veux de la bonne humeur c'est tout !"

    iris desaccord "Quelle naïveté ! Tu crois vraiment que Kami nous laissera respirer ?"

    julian idee "Bah ça dépend, peut-être même qu'elle est cassée."

    kael reflechit "Tu crois qu'elle aurait pu être surchargée ou genre... piratée ?"

    julian sourire "Il y a peut-être un moyen de le savoir, non ?"

    kael reflexion "À quoi tu penses ?!"

    julian rire "Va savoir."

    $ hideGroup()

    jump _7_0_1_TEMPS_LIBRE_1

label _7_0_1_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    noam sourire "La journée est plus calme que d'habitude. Je devrais pouvoir trouver quelque chose pour m'occuper."

    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1

label _7_0_1_APRES_MIDI_TOMAS_CANON:

    $ current_period = "Après-midi"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_285
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "L'après-midi passe lentement. Comme s'il manquait quelque chose."
    "Comme si le Conclave ne savait plus quoi faire de nous sans la petite voix de Kami qui résonne entre les murs."

    "Je tourne au coin du couloir quand quelqu'un m'interpelle."

    $ showGroup([
        ("tomas", "neutre", 0.30),
        ("noam",  "neutre", 0.70),
    ])

    tomas neutre "Noam ? Tu as quelques minutes ?"

    noam taquin "J'ai pas grand-chose d'autre à faire. À cette heure-là, on est déjà censé savoir quel est le prochain vote."
    noam taquin "Tu vas encore essayer de me faire lire des statistiques incompréhensibles ?"

    tomas determine "Justement, à ce propos..."

    "Il plisse légèrement les yeux avant de continuer sur un ton un peu plus grave."

    tomas reflechit "J'ai vérifié certaines données disponibles dans la salle du Canon."

    noam surpris "Dans la salle du Canon ?"

    tomas neutre "Oui. Tu-Tu sais, il y a des ordinateurs là-bas. Et on peut voir certaines données."

    noam taquin "Tu bosses vraiment alors que tout le monde est de bonne humeur ?"

    tomas reflechit "Je préfère vérifier des choses quand elles sont anormales."
    tomas gene "C-C'est plus... rassurant."

    noam hesitation "Et ça l'est ?"

    tomas hesitation "Oui. Enfin je pense... Suis-moi, ce sera plus simple si tu vois ça par toi-même."

    "Je le suis pendant quelques minutes en silence."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_tension.mp3" fadein 1.5

    think "La salle du Canon est presque vide. Comme d'habitude, pas grand monde n'aime cette ambiance pesante."
    think "Mais pourquoi est-elle aussi froide ?!"

    $ showGroup([
        ("tomas", "neutre", 0.30),
        ("noam",  "neutre", 0.70),
    ])

    tomas neutre "Regarde ça."

    "Il tapote sur un écran et y affiche plusieurs fenêtres."
    "Des centaines de lignes incompréhensibles défilent."

    noam panne "Tomas. Je vais être honnête avec toi."
    noam panne "Je comprends absolument rien à ce que tu fais..."
    noam taquin "Enfin, je comprends que tu comprends quelque chose. C'est déjà bien."

    tomas gene "A-Ah... Oui. Pardon. Je vais t'expliquer."

    "Il ferme plusieurs fenêtres. Une seule reste ouverte. Un tableau."

    tomas inquiet "Ce sont... les exécutions quotidiennes."

    noam inquiet "..."

    "Le mot suffit à refroidir la pièce encore davantage."

    tomas inquiet "Le système mondial publie automatiquement les chiffres toutes les heures. Enfin, normalement."
    tomas reflechit "Mais, regarde... Depuis hier soir…"

    call j701_play_console from _call_j701_play_console

    "Il déglutit légèrement."

    tomas inquiet "Zéro. Depuis hier il y a zéro exécution."

    "Je regarde l'écran. 0. Partout. Toutes régions confondues."

    noam surpris "... C'est une bonne nouvelle, non ?"
    noam hesitation "Enfin... ça devrait l'être."

    tomas raison "Techniquement oui."

    noam hesitation "Mais est-ce que c'est seulement possible ?"

    tomas reflechit "Statistiquement… C'est extrêmement improbable."
    tomas neutre "On est généralement entre vingt-cinq et quarante-cinq exécutions par jour."
    tomas inquiet "Là, il n'y en a aucune. Alors c'est pas impossible... Mais c'est pas non plus ordinaire."

    noam reflexion "Donc soit personne dans le monde entier n'a enfreint un Commandement…"
    noam reflexion "Soit le système déconne."

    tomas raison "Oui. Et je pense que c'est plus le système qui déconne."

    noam inquiet "Ouais, je crois bien que ça déconne sérieusement..."
    noam inquiet "D'abord Kami... Et maintenant ça ?"

    tomas hesitation "Je n'en sais rien. Mais..."
    tomas joie "Peut-être que les Commandements ne s'appliquent plus."

    "Un léger sourire passe sur son visage. Ça aussi, c'est rare."

    noam reflexion "Tu crois que c'est lié à Kami ?"

    tomas raison "Je dirais que c'est presque certain que c'est lié à l'état de Kami."
    tomas inquiet "C-C'est comme si les règles du monde avait cessé d'exister."

    noam surpris "Tu as l'air sûr de toi."

    tomas reflechit "Non. Mais si Kami disparaît réellement…"
    tomas inquiet "Alors ça dépasse largement le Conclave."

    noam triste "Hier encore j'aurais dû être content d'apprendre ça."
    noam fatigue "Et là... Je suis surtout fatigué."

    tomas fatigue "Je crois qu'on l'est tous."

    "Les écrans continuent de tourner doucement."
    "Aucun son. Aucune alerte. Aucune voix de Kami. Le canon ne se charge plus."
    "Pour la première fois depuis longtemps, le monde semble fonctionner sans elle."

    noam reflexion "Tu vas montrer ça aux autres ?"

    tomas mefiant "Pas encore."

    noam hesitation "Pourquoi ?"

    tomas reflechit "Parce que je ne sais pas encore ce que ça signifie. Im-Imagine si on se trompe complètement ?"
    tomas neutre "Je veux comprendre ce qu'il se passe avant de déclencher une panique."

    $ hideGroup()

    think "Je quitte la salle, la boule au ventre et l'estomac qui se creuse."

    jump _7_0_1_SOIREE_TENSION_LEGERE

label _7_0_1_SOIREE_TENSION_LEGERE:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_287
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    "Le dîner commence tard. Personne ne l'a vraiment décidé."
    "Les gens sont juste revenus progressivement manger après avoir vaqué à leurs occupations."
    think "On a tous plus ou moins réussi à se faire au rythme du Conclave."

    $ showGroup([
        ("iris",   "sourire"),
        ("julian", "decontracte"),
        ("lysa",   "reflexion"),
        ("kael",   "fatigue"),
        ("elias",  "neutre"),
        ("mara",   "neutre"),
        ("noam",   "neutre"),
    ])

    iris taquin "Franchement, si demain elle parle toujours pas…"

    julian sourire "Je commence officiellement à apprécier cette dystopie !"

    noam content "Tu dis ça maintenant. Mais au bout de trois jours, tu risques de mourir d'ennui !"

    julian rire "Impossible. Je suis trop fascinant pour m'ennuyer !"

    iris rire "Laisse-moi rire... Ton égo relève certainement de la psychiatrie."

    lysa reflexion "Je crois surtout qu'on profite du silence avant de comprendre pourquoi il est là."

    iris gene "T'es toujours optimiste, toi. Franchement, ça doit être fatiguant d'être dans ta peau."

    lysa inquiet "Si ça peut nous garder en vie..."

    kael fatigue "Techniquement, Kami peut être en maintenance et revenir demain."

    iris colere "Kael. Non. Tais-toi un peu."
    iris desaccord "Tu peux arrêter de rendre chaque chose terrifiante avec un ton calme ?"

    kael neutre "Il ne faut pas se mentir. C'est même très probable après le cirque d'hier."

    play sound "sfx/plate_drop.mp3"

    "CLAC."

    elias inquiet "Ok. Bon. Faut qu'on parle sérieusement."

    mara agace "Houla ! Tu es inquiétant quand tu tires cette tronche."

    elias inquiet "Non mais sérieux. Quelqu'un est allé dans la salle de stockage ?"

    "Quelques regards se lèvent."

    mara doute "Hein ? Pourquoi ?"

    elias inquiet "Parce qu'il manque du matériel."

    iris surpris "Quel genre de matériel ?"

    elias "Des outils. Des composants. Et des grosses batteries."

    kael surpris "Des batteries ? Pourquoi tu crois qu'on aurait besoin de batteries ?"

    mara doute "T'es sûr que tu les as pas déplacées ? Ouais je sais, c'est un peu une question à la con mais bon."

    elias colere "Oui je suis sûr. Elles y étaient encore hier."
    elias fatigue "Tout était encore rangé ce matin."
    elias fatigue "Je bricolais un truc. Un petit truc. Rien de bizarre, hein."

    mara taquin "Pourquoi quand tu dis ça, ça te rend encore plus suspect ?"

    elias fatigue "J'ai refait la liste dans ma tête."
    elias inquiet "Plus je recompte, moins ça colle. Et moi, les listes, je les rate pas."

    kael reflechit "On a redistribué les stocks ce matin avec la livraison, on les a peut-être déplacés dans la salle de maintenance ?"

    elias neutre "Non, impossible. J'ai déjà tout retourné au moins dix fois."

    mara reflexion "Il manque beaucoup de choses ?"

    elias fatigue "Pas énormément. Mais les composants qu'il me fallait, ceux-là, on les remplace pas avec n'importe quoi."
    elias colere "Et franchement, j'ai la flemme de devoir attendre le jour 14 pour terminer mon projet."

    iris hesitation "Et personne a rien pris ici ?"

    julian reflexion "Pourquoi quelqu'un volerait des batteries ?"

    elias panique "J'en sais rien, pour bricoler ?"

    iris colere "Génial. Tu sous-entends qu'il y a un voleur parmi nous ?"

    elias inquiet "Quelqu'un a peut-être cru que c'était disponible. C'est pas..."

    mara agace "Tu viens littéralement de demander si quelqu'un avait pris ton matériel."

    elias inquiet "Oui mais—"

    "Il s'arrête. Comme s'il essayait lui-même de décider si ça avait du sens."

    elias fatigue "Je comprends pas. Fais chier, j'avais quasiment terminé !"
    elias colere "J'ai vérifié partout pourtant ! Impossible de mettre la main dessus."

    kael neutre "Il y a des caméras dans le stockage. Peut-être qu'on peut accéder aux images ?"

    iris surpris "Ah. Oui. C'est vrai qu'on vit tout le temps avec ça, mais il y a des caméras partout ici..."

    elias panique "Il faudrait accéder aux images... Le plus simple serait de demander à Kami."

    noam fatigue "Ne me dites pas qu'on en est réduit à espérer son retour ?"

    pause 2.0

    noam reflechit "Non. On vaut mieux que ça. On va résoudre cette affaire nous-mêmes !"

    call j701_investigation from _call_j701_investigation

label _7_0_1_FIN_JOURNEE:

    "Au final nous n'avons pas trouvé grand-chose."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    $ showGroup([
        ("noam",   "neutre",     0.50),
    ])

    think "Nous avons fouillé, mais rien ne laisse envisager le moindre vol."
    think "Pourquoi quelqu'un aurait besoin de tout ça de toute façon ?"

    noam triste "Raah, j'y comprends rien."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam",   "neutre",     0.50),
    ])

    think "Kami n'est toujours pas réapparue."

    noam reflechit "Pourtant je suis sûr qu'elle est toujours là. Juste silencieuse."

    "Je retire ma veste et la laisse tomber sur la chaise près du bureau."
    "Le silence dans la chambre est toujours là. Et je ne saurais dire s'il est plutôt inquiétant ou rassurant."

    think "J'ai presque envie qu'il reste."

    "Je m'assois sur le bord du lit. Je repense à la cafétéria. À la relative bonne humeur de la journée. Aux discussions inutiles..."
    "Au silence du canon."

    think "Quelque chose cloche. Mais personne n'a vraiment envie que ça s'arrête."
    think "D'une certaine manière, le monde est redevenu totalement instable."

    "Je regarde vers mon bureau. Je cherche le dessin de Juliette."

    noam sourire "J'espère qu'elle va bien."
    pause 1.0
    noam surpris "Hein ?! Mais où il est ?!"

    call fouille_bureau_run from _call_fouille_bureau_run

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam",   "neutre",     0.50),
    ])

    "Je fouille, je retourne tout. Je cherche partout."
    noam colere "Il n'est plus là."
    think "Le dessin de Juliette n'est plus là."

    "Je me redresse rapidement."

    noam surpris "Hein... ?"

    "Je regarde autour de moi."

    think "Je l'ai pourtant laissé là il me semble."
    think "Je n'y ai pas touché ! Il devrait être là !"

    "Je continue à fouiller pendant de nombreuses minutes."
    think "Il a dû tomber."

    noam colere "Raaah ! Je fouillerai toute la chambre demain !" 

    $ blink()

    "Je m'allonge finalement dans le lit."

    $ blink()

    scene black with fade

    jump patreon_ending

    #call end_day("8") from _call_end_day_11
    #jump _8_0_1_REVEIL_CHAMBRE

# Total journée : 14 minutes
# Durée totale : 2h03