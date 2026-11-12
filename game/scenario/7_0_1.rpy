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
    call show_chapter_title("Début du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_25

    scene black
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 7
    $ noam_has_juliette_drawing = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    $ blink()

    play sound sfx_knock volume 4.0
    "BAM ! BAM ! BAM !"
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    think "Quoi ?! Qu'est-ce qui..."
    play sound sfx_knock volume 4.0
    lysa "Noam !"
    think "Lysa ? Si elle cogne à cette heure-ci, il s'est passé quelque chose."
    "Je saute du lit, me prends un pied dans la couette et traverse la chambre en essayant de ne pas m'étaler."
    scene bg_chambre at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_278
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.75), ("noam", "surpris", 0.25)])
    noam inquiet "Qu'est-ce qu'il y a ? Quelqu'un est blessé ?"
    lysa surpris "..."
    noam inquiet "Lysa ?!"
    lysa taquin "Non. Mais maintenant, j'ai une nouvelle raison de m'inquiéter."
    noam surpris "Hein ?"
    lysa sourire "Tu as toujours cette tête au réveil ?"
    think "Je baisse les yeux. T-shirt froissé, pantalon de nuit, une chaussette qui a disparu."
    noam colere "TU AS FAILLI DÉFONCER MA PORTE !"
    lysa blase "Et toi, tu viens de m'agresser avec ta coiffure."
    noam desaccord "On dirait que tu annonçais la fin du monde !"
    lysa reflechit "Justement. Je ne sais pas si c'est la fin du monde."
    noam inquiet "Quoi ?"
    lysa neutre "Il est presque midi. Et Kami n'a toujours rien dit."
    "Je cherche des yeux l'écran au fond de ma chambre. Pas une image."
    noam hesitation "Pas d'annonce du matin ?"
    lysa neutre "Pas d'annonce. Pas de commentaire sur notre petit-déjeuner. Pas même un « bande d'incapables »."
    noam reflechit "Depuis quand ?"
    lysa reflechit "Depuis le vote d'hier. J'ai attendu un peu avant de venir."
    noam desaccord "Et tu as attendu jusqu'à midi pour me prévenir ?!"
    lysa blase "Je te rappelle que monsieur le héros dormait."
    noam colere "Tu pouvais me réveiller plus tôt !"
    lysa taquin "Je viens de le faire. Tu m'as engueulée."
    noam panne "..."
    lysa sourire "Tu devrais entrer, tu vas attraper froid."
    noam surpris "C'est MA chambre !"
    lysa rire "Ah. Oui. C'est vrai."

    $ hideGroup()
    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")
    pause 1.0
    lysa reflechit "D'habitude, ça m'aurait fait plaisir de ne pas entendre sa voix."
    noam neutre "Et aujourd'hui ?"
    lysa blase "Aujourd'hui, je me demande ce que les gens font quand la seule chose qui leur donne des ordres s'arrête brusquement."
    noam taquin "Ils font la grasse matinée, apparemment."
    lysa sourire "Excellent choix de société. Tu devrais le proposer au prochain vote."
    noam inquiet "Tu as vérifié avec les autres ?"
    lysa neutre "Quelques chambres. Personne ne l'a entendue. D'ailleurs, une partie des représentants dort encore."
    noam reflechit "Les écrans du Conclave fonctionnent ?"
    lysa reflechit "Ceux que j'ai vus, oui. Elle, non."
    "Je voudrais trouver une bonne raison de me réjouir. Je n'en trouve pas, puis j'en trouve une, et j'en ai presque honte."
    noam sourire "Au moins, elle nous laisse tranquilles."
    lysa sourire "Voilà. C'est ce que je me dis depuis ce matin."
    lysa blase "Et plus je me le répète, moins j'y crois."
    "Elle regarde les vêtements éparpillés par terre."
    lysa taquin "Tu vas rester habillé comme ça pour célébrer notre liberté ?"
    noam colere "SORS !"
    lysa rire "Je t'attends dehors. Prends ton temps. Pas trop, hein : j'aimerais déjeuner avant la prochaine décennie."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "La porte se referme."
    think "Hier, Kami suppliait presque qu'on termine le vote. Ce matin, elle ne prend même plus la peine de nous insulter."
    "J'ouvre la bouche pour lui lancer une question, par habitude."
    "Rien ne vient."
    $ unlock_gallery_image("bg_cg026")
    scene bg_cg026 at adaptive_fullscreen with dissolve
    "Un peu d'eau sur le visage. Mes cheveux refusent de coopérer."
    think "Je vais finir par croire que Lysa avait raison."
    scene bg_cg026_1 at adaptive_fullscreen with dissolve
    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    think "Bon. Si je n'ai toujours aucune réponse, au moins j'ai retrouvé ma deuxième chaussette."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je récupère ma veste et sors."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "blase", 0.50), ("noam", "neutre", 0.22)])
    nyra colere "Ah ! Vous voilà enfin."
    noam surpris "Nyra ?"
    nyra neutre "Lysa, tu lui as dit ?"
    lysa taquin "Que Kami est muette, ou qu'il dort comme une pierre ?"
    nyra fatigue "Je parle des caisses."
    noam reflexion "Quelles caisses ?"
    "Nyra réajuste un carton sur sa hanche. Une boîte en dépasse dangereusement."
    nyra colere "La livraison ! Elle est arrivée ce matin. Sans prévenir. Sans bon de répartition. Et j'ai trouvé du matériel médical entre deux cartons de nourriture !"
    lysa blase "Une véritable insurrection des fournitures."
    nyra determine "Si tu veux plaisanter, tu peux le faire en portant une caisse."
    lysa taquin "Ça, c'est une proposition qui me ressemble."
    noam inquiet "Attends. Le ravitaillement s'est fait normalement, alors que Kami n'a rien annoncé ?"
    nyra reflechit "Les commandes étaient probablement programmées. Je n'en sais rien."
    lysa blase "Au moins, les cartons ne bégaient pas."
    nyra neutre "Pour l'instant."
    "Elle nous tend deux caisses. La mienne est beaucoup plus lourde que prévu."
    noam surpris "Il y a quoi là-dedans ? Des briques ?!"
    nyra taquin "Non. Les briques sont dans l'autre."
    noam desaccord "C'était une blague !"
    nyra neutre "Moi aussi."
    lysa rire "Oh. Elle apprend."
    nyra determine "Cafétéria, infirmerie, maintenance ou stockage. On trie correctement, on ferme les caisses et on les amène à leur destination. Pas d'improvisation."
    noam taquin "Et si on improvise ?"
    nyra neutre "Je vous fais tout recommencer."
    lysa blase "Voilà, Noam. On avait gagné une matinée sans dictature."
    $ hideGroup()
    call rangement_play from _call_rangement_day7
    "Je repose enfin la dernière caisse."
    noam fatigue "Je crois que mes bras viennent de déposer une demande de congé."
    nyra reflechit "J'en profiterai pour vérifier les inventaires. Il manque déjà des numéros sur deux étiquettes."
    lysa neutre "On est nourris, et on a encore le droit de se plaindre. Journée historiquement réussie."
    nyra neutre "À condition que personne n'ait mélangé les médicaments avec les sauces."
    noam surpris "C'est arrivé ?!"
    nyra taquin "Je vérifie justement."
    jump _7_0_1_CAFETERIA


label _7_0_1_CAFETERIA:
    call KD_ROUTE_J7_ELIAS from _call_optional_kd_route_j7_elias
    call START_EXPLORATION_LIBRE("_7_0_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_exploration__7_0_1_CAFETERIA


label _7_0_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_282
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "J'entends des rires. De vrais rires. Je m'arrête une seconde devant la porte."
    $ showGroup([
        ("iris", "sourire"), ("julian", "sourire"), ("lysa", "neutre"),
        ("elias", "neutre"), ("mara", "rire"), ("kael", "fatigue"), ("elen", "joie")
    ])
    julian joie "Et c'est ainsi que j'ai sauvé la dernière part de gâteau d'une disparition tragique."
    iris blase "Tu l'as mangée."
    julian sourire "Je l'ai mise à l'abri. Dans un lieu dont je garantis personnellement la sécurité."
    mara rire "Ouais, ton bide !"
    elen rire "Mais c'était ma part !"
    julian surpris "Ah."
    lysa blase "Voilà. Premier crime du monde sans Kami : vol de dessert."
    elias rire "On peut lancer une enquête. Je suis sûr que le suspect porte encore les preuves autour de la bouche."
    julian hesitation "Je ne vois absolument pas de quoi tu parles."
    iris colere "Et EN PLUS tu nous prends pour des imbéciles !"
    noam sourire "Vous avez l'air de bien vous amuser."
    mara taquin "Oh, le survivant du déménagement ! T'as ramené une étagère dans ta poche ?"
    noam desaccord "Si Nyra me redemande de porter une caisse, je déménage sur Terre."
    lysa sourire "Bonne chance. Les frontières sont fermées."
    "Le mot tombe un peu trop fort. Julian pose sa cuillère."
    elen sourire "Bon ! Nouvelle règle : on mange avant de parler de politique."
    mara taquin "Tu vas encore proposer d'interdire la mauvaise humeur ?"
    elen determine "Oui ! Et maintenant c'est obligatoire !"
    iris blase "Parfait. La première dictature dirigée par une fille qui s'excuse quand elle marche sur une fourmi."
    elen surpris "Mais je ne marche pas sur les fourmis !"
    mara rire "Elle nie les faits. C'est déjà une vraie dirigeante."
    "Elen proteste, Julian applaudit son discours imaginaire et Elias manque de renverser son verre en voulant applaudir aussi."
    elias panique "Oh, merde !"
    iris colere "PAS ENCORE !"
    "Il rattrape le verre de justesse. Cette fois, Mara l'applaudit pour de bon."
    lysa taquin "Félicitations. On vient d'éviter une deuxième catastrophe technologique."
    kael sourire "Un événement statistiquement notable."
    elias colere "Vous allez me la ressortir combien de temps, cette histoire ?!"
    mara taquin "Jusqu'à ce que tu inventes un café qui tienne tout seul."
    "Même moi, je ris. Puis je réalise que personne n'a regardé l'écran depuis plusieurs minutes."
    iris reflechit "Bon. Le truc vraiment étrange, c'est que tout fonctionne encore."
    julian sourire "Étrange ? Moi, j'appelle ça des vacances."
    iris colere "Je parle des portes, des livraisons, de nos tablettes ! Kami n'a pas répondu une seule fois et les automatismes continuent !"
    kael reflechit "Une partie de la station doit fonctionner sans intervention directe."
    elias neutre "Ouais. C'est comme un moteur qui continue de tourner après que le conducteur a lâché le volant."
    mara taquin "Formidable. On est dans un véhicule sans conducteur."
    elias inquiet "C'était pas censé rassurer."
    lysa reflechit "Et si elle ne revenait pas ?"
    "La question fait cesser les couverts de tinter."
    julian hesitation "Alors... nous pourrions enfin décider par nous-mêmes ?"
    noam reflechit "On ne sait même pas ce qui lui arrive."
    iris reflechit "Je voudrais voir son système. Juste une fois. Comprendre ce qu'elle est vraiment."
    mara agace "Évidemment. Le monde est peut-être en train de s'écrouler et toi tu veux lui ouvrir le crâne."
    iris colere "C'est une INTELLIGENCE ARTIFICIELLE, Mara !"
    mara sourire "Merci, j'avais presque oublié."
    elen inquiet "Mais si elle ne revient pas, qui va faire fonctionner les sanctions ?"
    lysa blase "Je ne suis pas certaine que ce soit la première chose dont on devrait se plaindre."
    elen hesitation "Non, enfin... Je veux dire, les gens sur Terre. Ils ont grandi avec ça."
    kael reflechit "Le silence de Kami ne signifie pas nécessairement que ses ordres ont cessé d'être appliqués."
    noam neutre "Alors on ne va pas inventer une bonne nouvelle."
    "Elen prend sa tasse entre ses mains et baisse les yeux."
    elen sourire "D'accord. Mais on peut quand même profiter d'une heure où personne ne nous insulte ?"
    iris taquin "Enfin une proposition raisonnable."
    julian joie "Je demande à en être nommé organisateur officiel."
    mara taquin "Refusé à l'unanimité."
    julian surpris "Tu n'as même pas organisé de vote !"
    lysa rire "Tu vois ? On progresse déjà."
    "Une minute plus tard, le ton remonte. Elen a décidé qu'on devait porter un toast à quelque chose, sans parvenir à trouver quoi."
    call j701_play_plate from _call_j701_play_plate
    "Le plateau finit au centre de la table. Une petite victoire dont personne ne sait trop qui doit se vanter."
    elias sourire "Cette fois, je n'ai rien cassé."
    mara taquin "Garde cette phrase pour ta pierre tombale."
    iris colere "Mara !"
    "J'ai presque l'impression d'avoir retrouvé un repas ordinaire."
    call j701_play_calm from _call_j701_play_calm
    "La conversation se dissout en plaisanteries et en disputes minuscules."
    "Pour une fois, elles n'ont pas besoin de nous conduire quelque part."
    $ hideGroup()
    jump _7_0_1_TEMPS_LIBRE_1


label _7_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    noam sourire "Je crois que j'avais oublié à quel point ils pouvaient être insupportables quand ils ne sont pas terrifiés."
    think "Et pourtant, ça m'avait manqué."
    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1


label _7_0_1_APRES_MIDI_TOMAS_CANON:
    $ current_period = "Après-midi"
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    tomas inquiet "Noam ! Attends... juste une minute !"
    noam sourire "Si c'est un exposé sur l'histoire des frontières, je viens de manger."
    tomas gene "Non, ce n'est pas... enfin, ça touche peut-être aux frontières, indirectement."
    noam desaccord "Tomas..."
    tomas inquiet "J'ai trouvé un chiffre qui n'a rien à faire là."
    noam reflechit "Quel chiffre ?"
    tomas hesitation "Je préfère que tu le voies avant que je t'explique. Sinon je vais encore commencer à..."
    noam taquin "À écrire un livre ?"
    tomas gene "Oui. Exactement."
    "Il part devant moi, puis revient sur ses pas."
    tomas inquiet "Et, Noam ? Pour l'instant, n'en parle pas aux autres."
    noam inquiet "Tu me fais peur."
    tomas neutre "C'est justement ce que j'essaie d'éviter."
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    "La salle du Canon a l'air inchangée. Aucun grondement, aucun voyant d'alerte."
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    tomas reflechit "Le système publie un décompte des exécutions liées aux Commandements."
    noam inquiet "Je sais."
    tomas gene "Ah. Oui. Pardon."
    "Il ouvre plusieurs fenêtres."
    tomas reflechit "D'habitude, ça augmente chaque jour. La moyenne est d'environ vingt-cinq à quarante-cinq, suivant la période."
    noam reflechit "Et là ?"
    tomas inquiet "Regarde."
    call j701_play_console from _call_j701_play_console
    "Le tableau revient à l'écran."
    tomas inquiet "Zéro."
    noam surpris "Zéro... partout ?"
    tomas neutre "Depuis hier soir. Toutes les régions."
    call play_stat_dialogue("d7_0_1") from _call_stat_dialogue_d7_0_1
    "Je relis la même ligne plusieurs fois. Elle ne change pas."
    noam hesitation "Ça pourrait vouloir dire que personne n'a enfreint de Commandement."
    tomas reflechit "Oui. En théorie. Sauf qu'à l'échelle mondiale, pendant autant d'heures..."
    noam reflechit "C'est peu probable."
    tomas raison "Très."
    noam inquiet "Ou bien le compteur est en panne."
    tomas inquiet "C'est ce que je pensais. Mais les autres indicateurs de la station sont toujours mis à jour."
    noam reflechit "Tu crois que Kami ne sanctionne plus personne ?"
    tomas hesitation "Je crois que le nombre affiché est zéro. Je ne peux pas te promettre davantage."
    noam inquiet "C'est la réponse la moins rassurante que tu pouvais me donner."
    tomas gene "J'aurais pu te mentir."
    noam sourire "Tu ne sais pas faire ça."
    tomas triste "Si. Et c'est justement pour ça que je préfère vérifier."
    "Je tourne la tête vers l'immense canon derrière la vitre."
    noam hesitation "S'il n'y a vraiment plus d'exécutions..."
    tomas neutre "Certaines personnes vivent peut-être aujourd'hui parce que Kami s'est tue."
    "Il serre les lèvres, comme s'il regrettait d'avoir prononcé cette phrase."
    noam inquiet "Et si elle revient demain ?"
    tomas inquiet "Je n'en sais rien."
    "Cette fois, il ne cherche même pas à compléter sa réponse."
    noam reflechit "Tu vas prévenir tout le monde ?"
    tomas hesitation "Pas avant d'avoir vérifié davantage. Imagine ce que Ryn ferait s'il croyait soudain que les frontières ne sont plus surveillées."
    noam inquiet "Ou ce que Sael ferait pour l'en empêcher."
    tomas neutre "Voilà."
    "Je regarde encore le zéro. Il ressemble à une bonne nouvelle. Je n'arrive pas à lui faire confiance."
    $ hideGroup()
    jump _7_0_1_SOIREE_TENSION_LEGERE


label _7_0_1_SOIREE_TENSION_LEGERE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_287
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "À mon retour, Julian est en train d'essayer d'apprendre à Elen un tour de cartes. Elle a découvert sa combine avant la première démonstration."
    $ showGroup([
        ("iris", "sourire"), ("julian", "sourire"), ("lysa", "reflexion"),
        ("kael", "fatigue"), ("elias", "neutre"), ("mara", "neutre"),
        ("elen", "joie"), ("noam", "neutre")
    ])
    elen joie "Mais tu as caché la carte sous ton coude !"
    julian surpris "C'est une technique de prestidigitation !"
    mara taquin "C'est une technique de triche avec un costume."
    iris rire "Tu vois ? Même quand Kami disparaît, on peut encore compter sur Julian pour nous mentir."
    julian taquin "Mes secrets sont à la hauteur de mon charme."
    lysa blase "Donc, très faciles à trouver."
    "Le rire de la table couvre un instant les bruits de vaisselle."
    noam sourire "Je vois que personne n'a trouvé de meilleure occupation."
    elen sourire "On n'avait pas besoin d'en trouver !"
    iris reflechit "Ça fait du bien de ne pas entendre Kami. Mais... je veux quand même savoir ce qui s'est passé."
    kael neutre "Les systèmes peuvent reprendre. Elle peut revenir demain."
    iris colere "Kael ! Tu as un don pour gâcher les bonnes choses sans même changer de ton !"
    kael sourire "Je n'ai pas changé de ton, justement."
    mara rire "Il a marqué un point."
    lysa reflechit "Je n'ai pas réussi à me débarrasser de l'impression qu'on profite d'un silence qui ne nous appartient pas."
    julian sourire "Alors je propose qu'on le remplisse d'applaudissements."
    iris blase "Pour toi ?"
    julian joie "Naturellement."
    elias inquiet "Désolé de casser votre fête, mais quelqu'un est passé au stockage après le tri de ce matin ?"
    mara taquin "Oh non. Elias a encore perdu son café."
    elias colere "PAS MON CAFÉ !"
    iris fatigue "Alors quoi ?"
    elias inquiet "Des outils. Des composants. Et deux grosses batteries. Il manque des trucs."
    lysa reflechit "Deux batteries ? Tu les as comptées avant ou après qu'on a déplacé toutes les caisses ?"
    elias neutre "Avant. Et après. Je sais où je range mes affaires."
    mara agace "Tu sais aussi où tu renverses tes boissons. Ça t'a pas empêché de..."
    elias colere "MARA, JE TE JURE !"
    "Il frappe la table, puis se ravise en voyant son verre trembler."
    elias gene "Enfin... je veux juste les retrouver."
    noam reflechit "Nyra a dit qu'il manquait des numéros sur certaines étiquettes."
    kael reflechit "On a peut-être rangé les batteries dans la maintenance."
    elias inquiet "J'y suis déjà allé."
    julian idee "Alors quelqu'un les a prises ?"
    mara mefiant "Tu balances ça comme ça, toi ? Tu sais ce que ça veut dire ?"
    julian hesitation "Je pose une question !"
    iris colere "Et moi j'aimerais qu'on évite d'accuser des gens pour une caisse mal étiquetée !"
    elias fatigue "Mais personne ne m'écoute ! J'ai vérifié !"
    lysa neutre "Alors raconte précisément ce qu'il manque. Pas ce que tu crois qu'on a fait."
    elias inquiet "Les composants de mon projet. Deux batteries de forte capacité. Des outils de coupe."
    "Julian cesse de jouer avec ses cartes."
    noam inquiet "Des outils de coupe ?"
    elias gene "Oui. Mais il y en a d'autres à l'atelier. Je dis pas qu'on prépare un meurtre !"
    mara taquin "Sympa, j'avais pas encore pensé au meurtre."
    elen inquiet "Mara..."
    mara neutre "Je plaisantais."
    kael reflechit "Il y a des caméras dans le stockage."
    iris surpris "Avec Kami, oui. Mais est-ce qu'on peut consulter les images sans elle ?"
    kael neutre "Je ne sais pas."
    elias inquiet "Le plus simple serait de lui demander."
    "Personne ne répond. C'est presque pire que si quelqu'un s'était mis à rire."
    julian hesitation "On... vient vraiment de souhaiter le retour de Kami pour retrouver une batterie ?"
    lysa blase "Deux batteries. C'est beaucoup plus grave."
    noam determine "On peut déjà regarder nous-mêmes. Les caisses, les registres, l'atelier. On n'a pas besoin de l'attendre pour chercher."
    mara sourire "Voilà notre détective. Je parie qu'il va commencer par interroger le meuble."
    noam taquin "Si le meuble répond, on aura au moins trouvé quelqu'un de plus coopératif que toi."
    elen rire "Je viens !"
    iris fatigue "Moi aussi. Mais si quelqu'un a déplacé tout ça sans prévenir, je l'étrangle."
    kael reflechit "On peut commencer par la liste de Nyra."
    elias fatigue "Merci. Enfin."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE


label _7_0_1_FIN_JOURNEE:
    "On compare les stocks, on retourne les caisses et on refait le chemin de la livraison. Personne ne retrouve les batteries."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ showGroup([("noam", "neutre", 0.50)])
    think "On a passé la soirée à chercher des objets que quelqu'un aurait pu déplacer par erreur. C'est presque rassurant de pouvoir encore imaginer une explication aussi bête."
    think "Je n'ai parlé à personne du compteur d'exécutions. Tomas m'a demandé de me taire, et je lui ai promis."
    noam reflechit "Espérons qu'il ait raison de vouloir attendre."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je jette ma veste sur la chaise. L'écran mural est toujours noir."
    think "Toute la journée, j'ai rêvé qu'elle se remette à parler. Pas parce qu'elle me manquait. Parce que j'aurais voulu savoir ce que son silence signifiait."
    "Je m'assieds au bureau."
    think "Juliette, elle, se moquerait de moi pour ça. Elle dirait qu'il faut profiter des bonnes choses quand elles arrivent."
    noam sourire "Tu aurais sûrement adoré voir ce matin..."
    "Je tends la main vers le dessin posé sur le bureau."
    "Mes doigts rencontrent le plateau vide."
    noam surpris "Hein ?"
    "Je tire un tiroir. Puis le deuxième."
    "Le dessin n'est ni dans la pochette, ni sous la tablette."
    noam inquiet "Non... Je l'ai laissé là."
    call fouille_bureau_run from _call_fouille_bureau_run
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je vérifie une dernière fois sous le bureau. Les papiers que j'ai déplacés sont là. Pas son dessin."
    noam desaccord "Ça n'a aucun sens. Je l'ai vu hier."
    think "J'ai dû le ranger sans m'en souvenir. Peut-être en me changeant, peut-être avant le vote."
    "Je ramasse un vêtement par terre. Rien."
    "Je repense aux batteries absentes du stockage."
    think "Non. Ça n'a aucun rapport. Une feuille de papier et du matériel de maintenance. Je suis en train de me faire peur tout seul."
    "Je pose les mains sur le bureau pour les empêcher de fouiller encore."
    noam triste "Je continuerai demain, Juliette. Promis."
    $ hideGroup()
    "Je me couche. Le Conclave ne fait aucun bruit."
    pause 0.5
    "Pour la première fois, j'aimerais presque entendre la voix de Kami se moquer de moi."
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_1_0_0_CANON
