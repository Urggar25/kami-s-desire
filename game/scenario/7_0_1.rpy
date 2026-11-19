default j701_table_choice = "aucun"
default j701_lysa_worry = False
default j701_iris_defense = False
default j701_tomas_informed = False
default j701_nyra_sorting = "standard"
default j701_plate_result = -1
default j701_julian_rapport = "neutre"
default j701_evidence_note = False
default j701_tomas_secret_kept = True
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
    $ noam_has_juliette_drawing = True
    $ j701_table_choice = "aucun"
    $ j701_tomas_secret_kept = True
    $ j701_lysa_worry = False
    $ j701_iris_defense = False
    $ j701_tomas_informed = False
    $ j701_nyra_sorting = "standard"
    $ j701_plate_result = -1
    $ j701_julian_rapport = "neutre"
    $ j701_evidence_note = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    $ blink()
    "Un bruit sourd me tire du sommeil. Je me retourne et essaie de me rendormir."
    play sound sfx_knock volume 4.0
    lysa "Noam !"
    think "Il est quelle heure... ?"
    "Je tire la couverture sur ma tête."
    lysa "Je sais que t'es là."
    noam "Non."
    lysa "Ah. Pardon. J'avais cru entendre quelqu'un répondre."
    "Je rouvre les yeux."
    noam "Lysa, qu'est-ce que tu veux ?"
    lysa "Que tu ouvres."
    noam "Pourquoi ?"
    lysa "Parce que je commence à parler à une porte et que ça me déprime."
    "Je cherche mes chaussettes en tâtonnant au pied du lit. J'en retrouve une. L'autre a disparu."
    noam "Attends."
    lysa "Tu as dit ça il y a une minute."
    noam "J'ai besoin de deux minutes."
    lysa "Il va falloir négocier une prolongation."
    "Je finis par ouvrir, toujours en t-shirt de nuit."
    scene bg_chambre at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_278
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.74), ("noam", "surpris", 0.28)])
    lysa sourire "Ah."
    noam fatigue "Quoi ?"
    lysa "Tu dors avec les cheveux comme ça ?"
    noam "Je les range dans un tiroir, normalement. Mais il était fermé."
    lysa rire "Pas mal."
    noam "Merci. Maintenant dis-moi ce qui se passe."
    "Lysa jette un regard par-dessus mon épaule."
    lysa neutre "Tu n'as pas remarqué ?"
    noam "Quoi ?"
    lysa "Depuis tout à l'heure."
    noam "Tu m'as réveillé. Forcément que je n'ai rien remarqué."
    lysa "Écoute."
    "J'écoute. Des portes claquent au fond du couloir. Quelqu'un fait rouler un chariot. Une voix se plaint que le petit-déjeuner est déjà terminé."
    noam reflechit "On a perdu Goumi ?"
    lysa blase "Non."
    noam "La ventilation ?"
    lysa "Elle marche."
    noam "Alors aide-moi un peu."
    lysa neutre "Il est presque midi."
    noam surpris "Quoi ?!"
    lysa "Voilà. Première chose que tu aurais dû remarquer."
    noam "Pourquoi tu m'as laissé dormir jusque-là ?"
    lysa "Parce que je ne suis pas ta mère."
    noam "Ça, j'avais remarqué."
    lysa "Et parce que personne n'a annoncé le réveil."
    "Je regarde l'écran mural au bout du couloir. Il est noir."
    noam inquiet "Kami ?"
    "Je laisse passer quelques secondes."
    noam "Kami, si tu comptes faire une blague, on peut directement passer au moment où tu te moques de moi."
    "L'écran ne réagit pas."
    lysa neutre "J'ai essayé ça aussi. Beaucoup mieux formulé, évidemment."
    noam "Elle ne répond pas du tout ?"
    lysa "Depuis hier. Elen l'a appelée une dizaine de fois, Iris encore plus."
    noam "Et les autres ?"
    lysa "Ils sont occupés à vérifier si les distributeurs fonctionnent."
    noam "Et ?"
    lysa sourire "Ils fonctionnent."
    "Un petit sourire m'échappe."
    noam "Au moins, une bonne nouvelle."
    lysa "Tu peux te réjouir. Personne ne m'en voudra."
    "Elle baisse les yeux vers mes pieds."
    lysa taquin "Tu devrais peut-être te réjouir avec deux chaussettes."
    noam desaccord "Je te rappelle que tu m'as réveillé en frappant comme si quelqu'un était mort."
    lysa neutre "C'était peut-être un peu excessif."
    noam "Un peu ?"
    lysa "J'avais vraiment besoin de parler à quelqu'un."
    "Elle le dit simplement. J'allais répondre quelque chose de désagréable, mais je m'arrête."
    menu:
        "Lui proposer de discuter quelques minutes.":
            $ j701_lysa_worry = True
            noam neutre "Tu veux entrer ? Je vais m'habiller, mais on peut parler après."
            lysa taquin "Je vais rester dehors. On tient tous à certaines frontières."
            noam sourire "Très drôle."
            lysa neutre "Merci."
            lysa "Je voulais juste vérifier que tu allais bien."
            noam "Je vais bien. Je suis juste en retard sur ma journée."
            lysa "D'accord."
            "Elle ne repart pas tout de suite."
            lysa reflechit "J'ai essayé de me dire que j'allais profiter du calme. Mais j'ai passé toute la matinée à attendre une insulte."
            noam "C'est une mauvaise habitude."
            lysa "Ouais."
        "La taquiner sur sa soudaine inquiétude.":
            noam sourire "Tu t'inquiètes pour moi ? Tu devrais te faire examiner."
            lysa blase "Je t'ai réveillé pour avoir quelqu'un à insulter. C'est tout."
            noam "Ah. Là, je te reconnais."
            lysa "Tu vois ? Tout va bien."
            "Elle sourit, mais continue à regarder l'écran."
    lysa neutre "Bon. Va te changer. Nyra cherchait des volontaires pour les livraisons."
    noam "Des volontaires ?"
    lysa "C'est le mot qu'elle a utilisé."
    noam "Et pourquoi tu me le dis avec cet air-là ?"
    lysa taquin "Tu comprendras."
    $ hideGroup()
    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")
    pause 0.6
    "Lysa finit par s'éloigner. Je ferme la porte et retrouve enfin ma deuxième chaussette sous le bureau."
    "Le dessin de Juliette est toujours là. Je le soulève pour vérifier qu'aucun vêtement n'a glissé derrière."
    noam sourire "Toi, au moins, t'es à l'heure."
    "Je le remets à sa place."
    $ unlock_gallery_image("bg_cg026")
    scene bg_cg026 at adaptive_fullscreen with dissolve
    "Mes cheveux ont effectivement décidé de faire ce qu'ils veulent."
    scene bg_cg026_1 at adaptive_fullscreen with dissolve
    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    "Je prends ma tablette, ma veste, puis repars chercher ma tablette que j'avais reposée sans m'en rendre compte."
    scene bg_chambre at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "blase", 0.51), ("noam", "neutre", 0.21)])
    nyra colere "Enfin !"
    noam surpris "Quoi encore ?"
    nyra "Il me manque deux personnes pour le tri."
    lysa taquin "Tu en as trouvé une."
    noam "Tu avais dit des volontaires."
    nyra neutre "Oui."
    noam "Mais je n'ai pas..."
    nyra "Les volontaires portent les caisses. Les autres font l'inventaire. Tu préfères lequel ?"
    noam "C'est un choix parfaitement injuste."
    nyra "Les caisses, alors."
    lysa sourire "Tu vois, tu t'en sors très bien."
    "Nyra nous tend un carton à chacun. Celui qu'elle me donne semble rempli de pièces métalliques."
    noam inquiet "C'est lourd !"
    nyra "C'est marqué sur l'étiquette."
    noam "Il n'y a pas d'étiquette."
    nyra "Justement. Ce sont les colis non identifiés."
    lysa blase "Formidable organisation."
    nyra colere "Parce que toi, tu as mieux à proposer ?"
    lysa "Oui. On ouvre les cartons avant de les porter."
    "Nyra s'arrête."
    nyra reflechit "C'est... raisonnable."
    lysa sourire "Merci."
    noam "C'était donc une possibilité depuis le début."
    nyra "On a reçu le ravitaillement sans aucune feuille de répartition. Je fais avec ce que j'ai."
    noam "Tu veux que je t'aide avec les catégories ?"
    nyra "Tu connais la différence entre du matériel médical et des assiettes ?"
    noam "Généralement."
    nyra "Alors oui."
    "On commence à ouvrir les caisses. Une boîte de pansements se retrouve avec les épices."
    noam sourire "Celle-là, c'est facile."
    lysa "Ça dépend de la qualité du repas."
    nyra neutre "Lysa."
    lysa "Pardon."
    "Nyra me confie une petite pile de colis presque identiques."
    menu:
        "Vérifier les étiquettes avec Nyra avant de tout ranger.":
            $ j701_nyra_sorting = "inventaire"
            noam neutre "Attends. Si les numéros manquent, on devrait écrire ce qu'on trouve."
            nyra neutre "Oui. C'est ce que j'essaie de faire depuis vingt minutes."
            noam "Tu pouvais me le dire."
            nyra "Je viens de le faire."
            "On prend le temps de noter plusieurs numéros illisibles avant de ranger les colis."
        "Terminer rapidement le rangement pour rejoindre les autres.":
            $ j701_nyra_sorting = "rapide"
            noam sourire "On commence par les plus faciles. Le reste, on le laisse à part."
            nyra mefiant "À part où ?"
            noam "Là. Dans le couloir."
            nyra colere "Pas dans le couloir !"
            lysa "Pour une fois, je suis avec elle."
            "On déplace les cartons dans un coin du stockage. Nyra ajoute une note pour y revenir."
    $ hideGroup()
    call rangement_play from _call_rangement_day7
    "Quand je dépose enfin le dernier carton, Lysa s'est déjà assise sur une caisse vide."
    noam fatigue "Je veux une médaille."
    nyra neutre "Tu veux ton déjeuner."
    noam "Les deux, ce n'est pas possible ?"
    nyra "On verra quand j'aurai fini les inventaires."
    lysa taquin "Ne l'encourage pas. Elle est capable de créer un formulaire de demande de médaille."
    nyra "Je pourrais."
    noam "Bon. Je vais manger avant que vous en parliez sérieusement."
    jump _7_0_1_CAFETERIA

label _7_0_1_CAFETERIA:
    call KD_ROUTE_J7_ELIAS from _call_optional_kd_route_j7_elias
    call START_EXPLORATION_LIBRE("_7_0_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_exploration__7_0_1_CAFETERIA


label _7_0_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_282
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "Quand j'arrive, Julian et Elen se disputent autour d'une assiette presque vide."
    $ showGroup([
        ("iris", "sourire"), ("julian", "sourire"), ("lysa", "neutre"),
        ("elias", "neutre"), ("mara", "rire"), ("kael", "fatigue"), ("elen", "joie")
    ])
    elen colere "Tu l'as mangée !"
    julian surpris "Je n'ai jamais dit le contraire."
    elen "Tu as dit que tu la gardais pour moi !"
    julian "Je l'ai gardée aussi longtemps que possible."
    elen "Trente secondes !"
    julian "Tu sous-estimes l'effort."
    iris blase "Il a passé trente secondes à la regarder et il l'a avalée."
    julian sourire "Je suis flatté que tu observes mes habitudes avec autant d'attention."
    iris colere "Ne commence pas."
    mara taquin "Moi, je trouve qu'il a été très courageux. Affronter un gâteau sans défense..."
    elen "C'ÉTAIT MON GÂTEAU !"
    elias sourire "Je peux te donner ma part, si tu veux."
    elen "Non, merci."
    elias "Pourquoi ?"
    elen "Parce que tu vas encore croire que je te demande la moitié de tout ce que tu manges."
    elias surpris "Mais pas du tout !"
    lysa blase "Elle a raison. Une fois, tu lui as donné ton dessert, puis tu l'as remerciée pendant deux jours."
    elias gene "Je la remerciais parce qu'elle m'avait rendu une fourchette."
    noam sourire "Je suis arrivé au mauvais moment ?"
    mara rire "Parfaitement au bon. Il y a un procès en cours."
    julian taquin "J'exige un avocat."
    noam "Tu as mangé le gâteau ?"
    julian "Oui, mais..."
    noam "Affaire classée."
    "Elen frappe dans ses mains, ravie. Julian lève les yeux au ciel."
    julian colere "Tu viens de ruiner ma défense."
    noam "Fallait commencer par ne pas avouer."
    elen joie "Merci, Noam."
    "Une part de dessert attend toujours dans l'assiette d'Elias. Elen la regarde, puis la repousse légèrement vers lui."
    elen neutre "Mange-la. Ça va."
    elias "Tu es sûre ?"
    elen "Oui."
    elias "Parce que je peux..."
    elen "ELIAS."
    elias sourire "D'accord !"
    "Il prend une bouchée. Julian observe l'assiette avec regret."
    iris colere "Ne regarde même pas."
    julian neutre "Je ne regardais rien."
    iris "Tu regardais."
    julian "Je regardais la table."
    mara "Avec de grandes ambitions."

    "Goumi arrive avec un plateau supplémentaire. Il s'arrête devant moi, les mains occupées."
    noam "Merci, Goumi."
    elen "Oh ! On peut passer les plats ? J'ai pas envie de demander à tout le monde de se lever."
    mara "Tu peux les poser au milieu."
    elen "Les bols sont encore chauds."
    kael calme "On peut attendre."
    elen "Non, non. Je demande juste si quelqu'un peut m'aider."
    menu:
        "Aider à faire circuler les plateaux.":
            noam neutre "Passe-les-moi. Je vais faire tourner."
            elen sourire "Merci ! Faites attention, ça glisse."
            call j701_play_plate from _call_j701_play_plate_story
            $ j701_plate_result = j701_plate_score
            scene bg_cafeteria at adaptive_fullscreen with dissolve
            play music "music/bgm_introspective_atmosphere.mp3" fadein 0.5
            $ showGroup([
                ("iris", "sourire"), ("julian", "sourire"), ("lysa", "neutre"),
                ("elias", "neutre"), ("mara", "rire"), ("kael", "fatigue"), ("elen", "joie")
            ])
            if j701_plate_score >= 3:
                elen joie "Voilà ! Tout le monde a quelque chose !"
                noam sourire "Je prends ma retraite de serveur."
                mara sourire "C'est dommage. Tu avais presque de l'avenir."
            else:
                "Un bol glisse sur le plateau. Elias le rattrape avant qu'il tombe."
                elias surpris "Ouh !"
                noam gene "Merci !"
                elias sourire "Tu vois ? Ça arrive aussi aux autres."
                iris blase "N'en profite pas pour te sentir autorisé à recommencer."
        "Laisser Goumi déposer le plateau.":
            noam neutre "Goumi peut le poser au milieu, non ?"
            elen "Oui, c'est vrai."
            "Le robot pose le plateau sans rien renverser."
            mara taquin "Le seul professionnel de cette table."
            elias gene "Je vous entends."
    "Le repas reprend. Julian se sert en dernier, l'air faussement offensé."
    julian "Je ne comprends pas pourquoi vous avez si peu confiance en moi."
    lysa "On pourrait te montrer les assiettes."
    julian "Injuste."
    "Elen finit par accepter un morceau de pain chaud à la place de son gâteau."
    elen sourire "Bon. Ça va."
    julian "Tu me pardonnes ?"
    elen "Non."
    julian "Ah."
    "Personne ne vient lui porter secours."

    "À l'autre bout de la table, Kael essaie de faire tenir sa tablette debout contre un pichet."
    elias reflechit "Tu peux la poser à plat."
    kael "Il faut que je voie l'écran pendant que je mange."
    elias "Mais tu ne manges pas."
    kael "Parce qu'elle tombe."
    "Il la redresse. La tablette glisse à nouveau."
    iris fatigue "Kael, tu pourrais juste prendre dix minutes de pause ?"
    kael reflechit "J'ai des relevés à vérifier."
    elias "Tu m'as fait écrire la liste de ce que j'avais touché hier. Elle fait neuf pages."
    noam "Neuf ?"
    elias gene "Enfin, quatre pages et demie. J'ai laissé de la place pour les schémas."
    mara sourire "C'est presque rassurant. Il sait encore écrire."
    elias "Mara..."
    kael calme "Je préfère une liste trop longue à une panne qu'on ne comprend pas."
    iris reflechit "Tu ne sais toujours pas ce qui s'est passé au Conclave ?"
    kael "Pas précisément."
    iris "Et tu as vérifié les connexions principales ?"
    kael "Celles auxquelles j'ai accès."
    iris "Mais elle peut avoir coupé les canaux elle-même, non ? Pour se réparer."
    kael "Oui."
    iris "Voilà."
    kael "Ça reste une possibilité. Pas une conclusion."
    iris colere "Je ne t'ai pas demandé une conclusion."
    "Kael essaie encore de caler sa tablette. Je lui passe mon verre vide."
    noam "Tiens. Fais un support avec ça."
    kael surpris "Ah."
    "Il cale enfin l'écran."
    kael calme "Merci."
    noam "L'ingénieur en chef vaincu par un pichet. Je ne raconterai ça à personne."
    elias sourire "Je peux le noter dans ma liste ?"
    kael "Non."

    "Ryn passe derrière la baie vitrée, sans entrer. Il ne nous remarque pas. Sael, assise près de la porte, baisse les yeux sur son assiette."
    elen neutre "Je lui avais gardé un morceau."
    mara "Il repassera."
    elen "Tu crois ?"
    mara "J'en sais rien. Je ne vais pas lui courir après avec une fourchette."
    "Elen ne répond pas. Elle dépose une petite part sur une assiette vide."
    iris reflechit "On peut au moins être contents que la livraison soit arrivée."
    lysa neutre "Oui. Ça, c'est bien."
    julian sourire "On pourrait même fêter notre première matinée de repos sans les commentaires de Kami."
    iris "Elle ne s'est pas arrêtée pour nous donner des vacances."
    julian hesitation "Je n'ai pas dit ça."
    iris "Tout fonctionne encore. Elle doit traiter quelque chose d'important."
    mara neutre "Peut-être."
    iris "Quoi, « peut-être » ?"
    mara "Je n'en sais rien, Iris. Toi non plus."
    iris colere "Tu pourrais éviter de le dire comme ça."
    mara neutre "D'accord."
    "Iris baisse les yeux. Quelques secondes plus tard, elle récupère sa fourchette."
    elen sourire "On peut quand même faire quelque chose ce soir ? Un jeu ?"
    julian taquin "J'ai un excellent tour de cartes."
    lysa "Non."
    julian "Vous ne l'avez même pas vu."
    lysa "Justement."
    elen "J'aimerais bien le voir, moi."
    iris fatigue "Fais comme tu veux."
    "Elen lui touche légèrement le bras."
    elen neutre "Tu viendras quand même ?"
    iris inquiet "Peut-être. Je dois d'abord essayer un truc sur ma tablette."
    elen "D'accord."
    "Iris se lève pour aller au comptoir. Elle compose une commande sur l'écran, l'efface, puis recommence."
    noam reflechit "Ça va ?"
    iris "Oui."
    noam "Tu veux que je..."
    iris "Non, merci."
    "Je la laisse tranquille."
    "À la table, Julian présente déjà trois cartes à Elen. Elle lui demande pourquoi elles sont toutes de la même couleur."
    julian joie "Parce que c'est le principe du tour."
    elen "Ah bon ?"
    julian "Non. Enfin, tu n'étais pas censée les regarder maintenant."
    "Cette fois, Mara n'a même pas besoin d'ajouter quoi que ce soit."

    "Le dernier plateau arrive. Elen refuse obstinément de reprendre le sujet du Conclave."
    elen "Je propose une règle pour le dessert."
    mara "Pas de procès pour les gâteaux ?"
    elen "Non. Une minute entière sans parler de ce qui s'est passé hier."
    lysa blase "Tu viens d'en parler."
    elen "Oui, mais le chrono n'a pas commencé !"
    julian "Une minute de silence ?"
    elen "Non, on a le droit de parler. Juste pas de ça."
    noam "C'est plus difficile que ça en a l'air."
    menu:
        "Aider Elen à lancer une conversation légère.":
            $ j701_table_choice = "complicite"
            noam sourire "Bon. Question importante : qui est le pire cuisinier de la table ?"
            mara sourire "Tomas."
            elen "Il n'est même pas là !"
            mara "Il ne risque pas de contester."
            elias sourire "J'ai déjà mangé ce qu'il prépare. Il met du sel dans le thé."
            lysa "Pourquoi tu as bu ça ?"
            elias "Je pensais que c'était du sucre."
            noam "Vous avez réussi à rendre la question beaucoup plus grave que prévu."
            "Elen rit. Julian commence à défendre la cuisine de Tomas, sans l'avoir jamais goûtée."
        "Dire à Iris qu'elle n'a pas besoin de faire semblant.":
            $ j701_table_choice = "inquietude"
            $ j701_iris_defense = True
            noam neutre "Iris, tu peux rester. Même si t'as pas envie de faire la fête."
            iris surpris "Je n'ai pas dit que je voulais partir."
            noam "Je sais."
            iris neutre "Alors pourquoi tu me demandes ?"
            noam "Je ne demande rien."
            "Elle me regarde, hésite, puis reprend place."
            iris fatigue "D'accord. Mais ne me demandez pas de chanter."
            elen sourire "Personne n'allait te le demander."
            julian "Moi, j'aurais bien..."
            iris colere "Julian."
            julian "C'est bon."
        "Laisser Julian improviser son fameux discours.":
            $ j701_table_choice = "julian"
            noam sourire "Vas-y, Julian. Ton discours."
            julian joie "Vraiment ?"
            lysa blase "Pourquoi est-ce qu'on fait ça ?"
            julian "Mes chers amis, en ce jour historique..."
            elen "Tu as dit une minute, pas un siècle !"
            julian "Je n'en suis qu'à l'introduction."
            mara "Et déjà, je regrette."
            "Julian tente une conclusion accélérée, se mélange les mots, puis renonce sous les rires d'Elen."
    "Le temps passe sans que personne ne regarde l'écran au-dessus du comptoir."
    "Elen ramasse enfin les assiettes vides. Julian se propose de l'aider."
    elen sourire "Très bien. Tu peux commencer par me rendre mon dessert."
    julian hesitation "Je crois que ça va être compliqué."
    elen "Alors tu feras la vaisselle."
    julian "C'est du chantage."
    elen "Oui."
    $ hideGroup()
    jump _7_0_1_TEMPS_LIBRE_1

label _7_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflechit", 0.31), ("noam", "neutre", 0.72)])
    "Kael est assis sur un carton vide, face à la porte du local technique. À côté de lui, plusieurs feuilles couvertes de chiffres."
    noam sourire "Tu as abandonné les ordinateurs pour le papier ?"
    kael calme "Les tablettes ne m'ont pas encore rendu les journaux que je leur ai demandés."
    noam "Et les feuilles répondent mieux ?"
    kael "Elles ne plantent pas."
    noam "C'est déjà une différence."
    "Il me montre un schéma que je ne comprends pas."
    kael reflechit "J'essaie de faire correspondre les heures. Le réseau de l'observatoire, la séance d'hier et les relevés de ce matin."
    noam "Tu as dormi combien de temps ?"
    kael "Un peu."
    noam "Combien ?"
    kael "Tu veux vraiment savoir ?"
    noam "Non, mais je demande quand même."
    kael "Deux heures, je crois."
    noam "Tu tiens debout comment ?"
    kael "Je suis assis."
    "Je baisse les yeux vers son carton. Bon. Il a raison."
    noam "Tu as mangé, au moins ?"
    kael "Oui."
    noam "Autre chose que le pain de ce matin ?"
    kael "Oui."
    noam "Tu es pénible."
    kael sourire "Tu poses des questions très précises."
    "Je ramasse une feuille tombée près de sa chaussure."
    noam "Tu as trouvé quoi, finalement ?"
    kael reflechit "La station continue de fonctionner. C'est tout ce que je peux affirmer."
    noam "Tu crois que Kami s'est mise en veille ?"
    kael "C'est possible."
    noam "Et tu crois qu'elle peut revenir ?"
    kael "Ça aussi."
    noam "Tu devrais faire des conférences. Les gens adorent les réponses comme ça."
    kael sourire "Tu peux aussi aller voir Julian. Il en donne des plus longues."
    "Il reprend la feuille."
    if j601_fracture_trace_saved:
        kael reflechit "Au fait, tu as encore la trace que tu as enregistrée pendant le vote ?"
        noam "Oui."
        kael "Ne la supprime pas. Je voudrais comparer le décalage à l'horloge de la station."
        noam "Tu ne l'as pas déjà ?"
        kael "J'ai une copie partielle. Il me manque la confirmation d'origine."
        noam "D'accord."
        $ j701_evidence_note = True
    else:
        kael reflechit "J'ai essayé de retrouver l'erreur de ta tablette. Sans la trace, je n'ai que le témoignage des autres."
        noam "On a été douze à voir les écrans se dérégler."
        kael "Oui. Et pas douze à voir exactement la même chose."
        noam "Tu peux au moins me dire qu'on n'a pas rêvé ?"
        kael "Je peux te le dire."
    kael neutre "Et si tu vois quelque chose d'étrange aujourd'hui, note l'heure."
    noam "Je vais passer ma journée à relever les minutes ?"
    kael "Pas nécessairement."
    "Il regarde ses feuilles. Je comprends le sous-entendu."
    noam "Bon. Essaie de dormir avant de t'endormir sur une console."
    kael calme "Je te retourne le conseil."
    noam "Moi, j'ai dormi."
    kael "Je l'ai entendu."
    noam surpris "Comment ça ?"
    kael sourire "Lysa raconte beaucoup de choses."
    "Je m'apprête à protester. Il remet déjà son casque sur les oreilles."
    $ hideGroup()
    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1

label _7_0_1_APRES_MIDI_TOMAS_CANON:
    $ current_period = "Après-midi"
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.29), ("noam", "neutre", 0.72)])
    "Tomas m'attend près de l'entrée de la cafétéria. Il tient sa tablette à l'envers."
    tomas "Noam. Tu as une minute ?"
    noam "Ça dépend."
    tomas gene "De quoi ?"
    noam "Du nombre de minutes que tu comptes finalement prendre."
    tomas "Ah."
    "Il réfléchit très sérieusement."
    tomas "Peut-être dix."
    noam sourire "Au moins, tu es sincère."
    tomas inquiet "Tu sais comment on retrouve l'historique des dernières synchronisations ?"
    noam "Sur la tablette ?"
    tomas "Non, sur... oui, évidemment, sur la tablette. Pardon."
    noam "Tu peux aller voir Kael."
    tomas "Je sais. Il a l'air occupé."
    noam "Il est assis sur un carton depuis tout à l'heure."
    tomas "Précisément. Un carton rempli de documents."
    noam "Et tu veux que je t'aide ?"
    tomas "Je voulais surtout que tu me dises si j'ai mal lu quelque chose."
    "Je tends la main vers sa tablette. Il la retire d'un geste brusque."
    noam surpris "Tomas ?"
    tomas gene "Ah, pardon ! Je n'ai rien contre toi."
    noam "Tu caches quoi ?"
    tomas inquiet "Rien. Enfin, un relevé. Mais pas ici."
    noam "Pourquoi ?"
    tomas "On va se mettre à m'expliquer que je ne comprends pas ce que je regarde. J'aimerais être sûr avant."
    "Il essaie de glisser la tablette dans sa poche. Elle est trop grande."
    noam "Tu sais que je peux encore te voir ?"
    tomas "Oui. Je sais. Ça n'a aucun sens."
    "Il s'arrête enfin de gesticuler."
    tomas neutre "Viens au canon avec moi. Tu me diras ce que tu en penses."
    noam "D'accord. Mais tu portes ta tablette correctement, cette fois."
    tomas gene "Promis."
    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Tomas ferme la porte derrière nous. Il vérifie deux fois qu'elle est bien fermée."
    noam "Tu vas finir par me donner envie de repartir."
    tomas gene "Désolé. Je ne veux pas que quelqu'un nous interrompe."
    noam "On est venus lire des chiffres, pas voler la station."
    tomas "Oui."
    "Il cherche un câble, l'enroule autour de sa main, puis le pose sans s'en servir."
    noam "Tomas. Assieds-toi."
    tomas "Je préfère rester debout."
    noam "Alors montre-moi."
    tomas reflechit "Tu te souviens du tableau qui comptabilise les sanctions liées aux Commandements ?"
    noam "Oui."
    tomas "D'habitude, il y a un relevé pour chaque secteur. Un total régional, puis un total général."
    noam "Tu as trouvé une erreur ?"
    tomas "Je n'en sais rien."
    "Il ouvre sa console. Les nombres s'affichent, puis plusieurs cellules disparaissent."
    tomas inquiet "Voilà. C'est ce que je voulais te montrer. Je n'arrive pas à isoler les dernières valeurs stables."
    noam "Qu'est-ce que ça veut dire ?"
    tomas "Que je voudrais être certain de lire la bonne ligne avant de raconter n'importe quoi."
    noam "Je peux essayer ?"
    tomas "Oui. Mais pas le bouton à droite. Celui-là remet tous les filtres à zéro."
    noam "Tu as déjà appuyé dessus ?"
    tomas "Trois fois."
    noam "Ah."
    tomas gene "Je pensais que c'était « retour »."
    "Je prends place devant la console. Tomas se tient derrière moi, presque sur la pointe des pieds."
    tomas "Tu vois les quatre flux ? Il faut retrouver la dernière valeur enregistrée pour chacun."
    noam "Et après ?"
    tomas "On verra."
    call j701_play_console from _call_j701_play_console
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Les quatre valeurs se stabilisent. Dans la colonne de droite, un total se met à jour."
    "0."
    noam "..."
    tomas "..."
    noam "Attends. Zéro, là ?"
    tomas reflechit "Oui."
    noam "Tu es sûr que c'est le total ?"
    tomas "C'est ce que dit l'intitulé."
    noam "Et pour hier ?"
    tomas "Remonte."
    "Je fais défiler les lignes précédentes. Les valeurs sont différentes."
    noam "Donc on a bien quelque chose avant."
    tomas "Oui."
    noam "Et depuis ?"
    tomas "Zéro."
    "Je regarde une autre région. Même chiffre."
    noam "Sur les quatre ?"
    tomas "Toutes."
    noam "Tu as vérifié l'horloge ?"
    tomas "Oui."
    noam "L'heure de la station, pas celle du vote ?"
    tomas "Oui, Noam."
    noam "Pardon."
    "Je parcours encore quelques lignes. Il y a bien des heures enregistrées, mais pas d'exécution depuis la veille."
    noam reflechit "Ça peut être un compteur qui ne reçoit plus de données."
    tomas "C'est possible."
    noam "Une coupure avec la Terre ?"
    tomas "Possible aussi."
    noam "Et le canon ?"
    tomas "Je ne sais pas."
    "Je me tourne vers la baie vitrée. Le canon est immobile."
    noam "Pourquoi tu ne m'as pas dit tout de suite que c'était ça ?"
    tomas gene "Parce que tu aurais tout de suite pensé que Kami ne sanctionne plus personne."
    noam "Et tu n'y penses pas ?"
    tomas "Si."
    "Il frotte ses paumes contre son pantalon."
    tomas inquiet "Mais si je me trompe, des gens pourraient croire qu'ils peuvent faire n'importe quoi."
    noam "Tu as peur que quelqu'un teste les Commandements."
    tomas "Je n'ai pas envie d'apprendre demain qu'une personne est morte parce qu'on lui a raconté que tout était terminé."
    noam "D'accord."
    "Il semble soulagé que je n'essaie pas immédiatement de le contredire."
    tomas "On peut comparer les données à d'autres systèmes. Kael pourrait..."
    noam "Pourquoi tu ne lui as pas demandé ?"
    tomas "Parce que tout le monde lui demande déjà quelque chose et qu'il n'a pas dormi."
    noam "C'est vrai."
    tomas "Et parce que je voulais vérifier sans lancer une rumeur."
    "Je ferme une fenêtre du tableau. Tomas la rouvre aussitôt."
    noam "Quoi ?"
    tomas "Pardon. Je voulais juste garder la ligne sous les yeux."
    noam "Tu peux l'enregistrer ?"
    tomas "J'ai fait deux copies."
    noam "Très bien."
    tomas "Enfin... une copie et une photo de l'écran."
    noam "C'est déjà mieux que rien."
    "Il essaie de sourire."
    call play_stat_dialogue("d7_0_1") from _call_stat_dialogue_d7_0_1
    "La salle reste silencieuse. Pour la première fois, Tomas ne cherche pas à combler le vide."
    noam neutre "Qu'est-ce que tu veux faire ?"
    tomas inquiet "Vérifier demain matin. Avec les relevés d'une autre console."
    noam "Pourquoi demain ?"
    tomas "Parce que je veux voir si une nouvelle journée s'enregistre. Si tout reste à zéro, ça voudra au moins dire quelque chose de plus."
    noam "Quoi ?"
    tomas "Je ne sais pas encore."
    "Je regarde sa tablette. Il a déjà ouvert une note pour préparer les prochaines vérifications."
    noam "Les autres devraient être au courant, non ?"
    tomas "Peut-être. Mais je voudrais être là quand on leur dira."
    menu:
        "Accepter de ne rien dire avant les vérifications.":
            $ j701_tomas_secret_kept = True
            noam neutre "D'accord. Je te laisse jusqu'à demain matin. Après, on en parle."
            tomas neutre "Merci."
            noam "Mais tu ne vas pas passer la nuit ici, hein ?"
            tomas gene "Je vais essayer."
            noam "Tomas."
            tomas sourire "Je te promets de dormir."
        "Demander à Tomas de prévenir Kael dès maintenant.":
            $ j701_tomas_secret_kept = False
            noam determine "Non. On ne peut pas attendre seuls avec ça. Il faut au moins que Kael sache qu'il y a un problème."
            tomas inquiet "Tu veux le dire à tout le monde ?"
            noam "Pas avant de vérifier. Mais Kael peut comparer les relevés."
            tomas reflechit "Je suppose."
            noam "Tu préfères l'appeler ou je le fais ?"
            tomas "Moi. Ce sont mes relevés."
            "Tomas compose un message, l'efface, puis écrit simplement : « J'ai trouvé une anomalie sur le compteur du canon. Tu peux m'aider à vérifier demain ? »"
            tomas "Voilà."
            noam "Merci."
            tomas "Il va croire que j'ai encore cassé quelque chose."
            noam "Il te connaît. Il demandera d'abord si tu as touché à un bouton."
            tomas gene "Il aura raison."
            $ j701_tomas_informed = True
    "Je referme le dossier avec Tomas. Il reste un instant devant la console."
    tomas "Noam ?"
    noam "Oui ?"
    tomas "Si c'est vrai..."
    "Il ne termine pas."
    noam neutre "On vérifiera."
    tomas "Ouais."
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
    if j601_fracture_trace_saved:
        noam reflechit "Et la trace que j'ai conservée hier ? Ça pourrait être lié ?"
        kael inquiet "Je n'ai pas de preuve pour l'instant. Mais je comparerai les anomalies. Ne supprime rien."
        lysa reflechit "Pourvu que le journal n'efface pas lui-même les preuves."
    else:
        noam reflechit "J'ai perdu la trace de l'erreur d'hier. Cette fois, il faut conserver une copie des relevés."
        kael reflechit "Exactement. On sauvegarde avant de toucher aux systèmes."
    elias fatigue "Merci. Enfin."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE


label _7_0_1_FIN_JOURNEE:
    "Après les vérifications, chacun regagne son couloir avec davantage de questions qu'en arrivant. Les batteries restent introuvables."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ showGroup([("noam", "neutre", 0.50)])
    think "On a passé la soirée à chercher des objets que quelqu'un aurait pu déplacer par erreur. C'est presque rassurant de pouvoir encore imaginer une explication aussi bête."
    if j701_tomas_secret_kept:
        think "Je n'ai parlé à personne du compteur d'exécutions. J'ai promis à Tomas une nuit pour vérifier."
        noam reflechit "J'espère qu'on ne regrettera pas cette promesse."
    else:
        think "Je n'ai pas annoncé le zéro à la cafétéria. Tomas et moi avons promis de préparer une explication après une dernière vérification."
        noam reflechit "Une nuit. Pas une de plus."
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
    "Je déplace la tablette, puis le cadre posé à côté. Le dessin n'est pas là."
    noam inquiet "Attends... Je l'avais laissé ici."
    "J'ouvre le premier tiroir. Rien. Le second contient les vêtements que j'y ai fourrés ce matin."
    noam desaccord "Ne me dis pas que j'ai perdu ça."
    "Je retourne sa pochette. Vide, elle aussi."
    "Je revois Juliette me faire promettre de ne pas corner la feuille avant de l'emporter jusque dans l'espace."
    noam triste "Tu vas te moquer de moi, Juliette."
    "Ma main revient au même endroit, comme si le papier allait finir par réapparaître."
    "Je pense aux batteries disparues. Pourquoi quelqu'un aurait-il pris le dessin de ma sœur ?"
    noam triste "Demain, je fouille tout. Promis."
    $ noam_has_juliette_drawing = False
    $ hideGroup()
    "Je me couche. Le Conclave ne fait aucun bruit."
    pause 0.5
    "Pour la première fois, j'aimerais presque entendre la voix de Kami se moquer de moi."
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_1_0_0_CANON
