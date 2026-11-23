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
    $ j701_lysa_search_help = False
    $ j701_iris_defense = False
    $ j701_tomas_informed = False
    $ j701_nyra_sorting = "standard"
    $ j701_plate_result = -1
    $ j701_julian_rapport = "neutre"
    $ j701_evidence_note = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    $ blink()
    play sound sfx_knock
    lysa "Noam ?"
    "Je laisse ma tête s'enfoncer dans l'oreiller."
    lysa "Je sais que tu m'entends."
    noam "Non."
    lysa "Bon. Je repasserai quand le monsieur aura fini de nier son existence."
    "Je me lève avant qu'elle reparte. Une seule chaussette est à sa place. Ça commence bien."
    scene bg_chambre at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_278
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "neutre", 0.74), ("noam", "fatigue", 0.28)])
    noam fatigue "Qu'est-ce qu'il y a ?"
    lysa "Regarde l'heure."
    noam "Bonjour à toi aussi."
    lysa "Regarde."
    "Je vérifie ma tablette."
    noam surpris "Onze heures quarante ?!"
    lysa "J'ai hésité à te laisser dormir jusqu'au dîner."
    noam "Pourquoi personne nous a réveillés ?"
    lysa "Essaie de demander."
    noam "Kami ?"
    "Rien. Même pas une remarque sur mes cheveux."
    noam inquiet "Kami, tu m'entends ?"
    lysa "Iris l'appelle depuis ce matin. Elle a essayé les écrans du dortoir, la cafétéria, sa tablette... Tout."
    noam "Elle n'a rien dit depuis hier ?"
    lysa "Pas un mot."
    "Un chariot passe dans le couloir. À part ça, tout est normal. C'est ce qui me gêne le plus."
    noam "Les portes fonctionnent ?"
    lysa "Oui."
    noam "La ventilation ?"
    lysa "Oui."
    noam "Et..."
    lysa "Les machines à café aussi. J'ai vérifié les priorités."
    "Je souris malgré moi. Elle ne me le rend pas."
    noam "Tu t'inquiètes vraiment, hein ?"
    lysa "Je sais pas. J'ai pris mon petit déjeuner tranquillement. C'était agréable."
    noam "Ça n'a pas l'air."
    lysa "J'ai passé dix minutes à attendre qu'elle dise quelque chose. Je crois que je m'étais habituée à lui en vouloir."
    "Elle fixe l'écran au bout du couloir."
    menu:
        "Lui proposer de rester un peu avec elle.":
            $ j701_lysa_worry = True
            noam neutre "Tu veux qu'on reste là deux minutes ?"
            lysa "Pour contempler un écran éteint ?"
            noam "Je peux aussi te montrer mon autre chaussette. Si je la retrouve."
            lysa sourire "Évite. Je préfère l'écran."
            "Elle reste quand même."
            lysa "J'ai eu peur qu'il te soit arrivé un truc. Tout le monde était déjà levé."
            noam "Tu pouvais commencer par ça."
            lysa "Je viens de le faire. Et ça me suffit pour aujourd'hui."
        "La taquiner pour la rassurer.":
            noam sourire "Tu commences à regretter les insultes de Kami ?"
            lysa blase "Je regrette surtout de t'avoir réveillé. Tu parles beaucoup."
            noam "Tu as frappé à ma porte."
            lysa "Ouais. Mauvais calcul."
            "Elle essaie de sourire, puis regarde de nouveau l'écran."
    nyra "LYSA !"
    lysa blase "Et voilà."
    noam "Quoi ?"
    lysa "Les livraisons. Nyra cherche des bras."
    noam "Ça explique pourquoi elle crie, mais pas pourquoi tu souris."
    lysa "Parce que je lui ai promis de t'en trouver deux."
    noam "Je n'ai pas dit oui !"
    lysa "J'ai dit que je trouverais des bras. Pas un volontaire."
    "Elle s'éloigne avant que je puisse négocier."
    $ hideGroup()
    call kd_vn_cg_impact("#e4f0ff")
    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")
    pause 0.4
    "Je ferme la porte et retourne chercher ma chaussette. Elle était sous le bureau."
    "Le dessin de Juliette est posé à côté du cadre numérique. Je le relève pour récupérer le tissu coincé dessous, puis le repose à plat."
    noam neutre "Ne bouge pas, toi."
    $ unlock_gallery_image("bg_cg026")
    scene bg_cg026 at adaptive_fullscreen with dissolve
    scene bg_cg026_1 at adaptive_fullscreen with dissolve
    window hide
    $ chibi_montage_play(CHIBI_MONTAGE_J701_NOAM)
    window auto
    "Cinq minutes plus tard, je suis habillé et à peu près présentable."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_281
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "neutre", 0.80), ("lysa", "blase", 0.51), ("noam", "neutre", 0.21)])
    nyra colere "Ah, enfin !"
    noam "Vous vous êtes vraiment organisées pour me tomber dessus."
    nyra "On a reçu du matériel sans étiquettes. Il me faut quelqu'un pour vérifier le contenu."
    lysa "Et moi, j'ai trouvé un expert."
    noam "En quoi ?"
    lysa "En affaires mal rangées."
    nyra "Vous avez fini ?"
    noam "Pas sûr."
    "Nyra m'ouvre un carton. Des pansements, des sachets de nourriture et un appareil emballé ensemble. Le manifeste indique simplement : FOURNITURES."
    noam "C'est précis."
    nyra "Le service de livraison n'a pas répondu à mes demandes de clarification."
    lysa "Étonnant. Personne ne répond à personne aujourd'hui."
    "Nyra lui lance un regard. Lysa baisse la tête vers le registre."
    nyra "On peut au moins vérifier ce qu'on a."
    menu:
        "Faire un inventaire complet avec Nyra.":
            $ j701_nyra_sorting = "inventaire"
            noam neutre "Donne-moi les numéros. Je vais les noter."
            nyra "Merci."
            lysa "Oh. Elle sait dire merci."
            nyra "Lysa, je t'en prie."
            "On finit par retrouver l'ordre des caisses. Nyra paraît presque soulagée."
        "Isoler les colis douteux pour gagner du temps.":
            $ j701_nyra_sorting = "rapide"
            noam neutre "On met les colis sans référence à part. On terminera quand on aura les bons documents."
            nyra "À part où ?"
            noam "Pas devant la porte. J'ai retenu la leçon."
            lysa "Il progresse."
            "Nyra note soigneusement les caisses à reprendre. Elle n'a pas l'air ravie, mais accepte."
    "Je transporte le dernier carton pendant que Nyra recompte les fournitures. Lysa revient avec un paquet de biscuits qu'elle a trouvé dans un lot de rations."
    noam "C'était dans l'inventaire ?"
    lysa "Maintenant, oui."
    nyra "Tu l'as noté ?"
    lysa "Un paquet de biscuits. Voilà."
    "Nyra tend la main. Lysa soupire et lui donne le paquet."
    nyra "On les distribuera au repas."
    lysa "Tu sais vraiment comment ruiner une découverte."
    "Je m'éclipse avant qu'elles recommencent."
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
    "Elen est debout au bout de la table. Julian mâche quelque chose en évitant soigneusement son regard."
    elen colere "Tu m'avais promis de le garder."
    julian "J'avais promis de le surveiller."
    elen "Mon gâteau !"
    julian "Oui. Je l'ai surveillé."
    iris blase "Puis il l'a mangé."
    julian "J'ai cédé à un moment de faiblesse."
    mara "Ça fait longtemps que tu étais faible ?"
    julian "Depuis ce matin."
    "Elen attrape l'assiette vide. Elias propose la sienne, mais elle la repousse."
    elen "C'est pas la peine, Elias."
    elias "Je peux te la laisser."
    elen "Mais j'en veux pas, de la tienne !"
    elias "Ah. D'accord."
    "Il récupère son assiette. Julian tente d'en profiter pour se lever."
    lysa "Assieds-toi, Julian."
    julian "Je comptais seulement..."
    lysa "Je sais."
    "Il se rassied. Personne ne lui demande ce qu'il comptait faire."
    noam sourire "J'arrive trop tard pour le dessert ?"
    elen "C'est lui !"
    noam "Je vois."
    julian "Tout le monde a décidé de m'accuser avant même..."
    noam "Tu l'as mangé ?"
    julian "Oui."
    noam "Bon."
    "Julian lève les mains. Elen s'assied enfin, mais elle refuse de le regarder."
    "Je récupère une assiette et m'installe. Pendant quelques minutes, la discussion repart sur le repas, les livraisons et les biscuits confisqués par Nyra."
    elen sourire "On pourrait profiter de cette journée pour faire quelque chose ce soir. Un jeu, par exemple."
    julian sourire "J'ai un tour de cartes."
    elen "Pas avec mon jeu."
    julian "J'ai dit un tour, pas un vol."
    "Elen se retourne vers lui. Julian préfère terminer son verre."
    "Un écran noir domine le comptoir. Iris le fixe depuis le début du repas."
    kael reflechit "Tu vas finir par y faire un trou."
    iris "Quoi ?"
    kael "L'écran."
    iris "Je l'ai appelée douze fois depuis ce matin."
    mara "Treize. Je t'ai entendue recommencer dans le couloir."
    iris colere "Tu comptais ?"
    mara "J'essayais de dormir."
    iris "Tu peux au moins admettre que ce n'est pas normal ?"
    mara "Bien sûr que ce n'est pas normal."
    iris "Alors pourquoi personne ne fait rien ?"
    kael "Je fais quelque chose. Je regarde les journaux. Il manque des morceaux entiers de la liaison extérieure."
    iris "Et c'est censé me rassurer ?"
    kael "Non."
    "Iris pose sa fourchette."
    iris "Elle a dit qu'on lui prenait sa voix. Vous vous en souvenez ? Hier, elle nous a demandé de l'aider."
    lysa "On s'en souvient, Iris."
    iris "Et aujourd'hui, elle ne répond plus. Vous trouvez ça normal de parler de gâteaux ?"
    elen inquiet "On n'a pas dit que c'était normal."
    iris "C'est pourtant ce que vous faites."
    "Elen baisse les yeux. Julian regarde son assiette."
    mara "On peut aussi manger sans avoir réglé ce qui s'est passé hier."
    iris "T'as réponse à tout, toi."
    mara "Non. Justement."
    "Iris pousse sa chaise. Le pied grince si fort que tout le monde s'interrompt."
    elias inquiet "Iris ?"
    iris "Je vais réessayer depuis l'infirmerie. Les terminaux n'utilisent peut-être pas tous la même connexion."
    kael "J'ai déjà comparé les relais."
    iris "Moi, j'ai pas fini."
    "Elle sort sans toucher à son repas."
    "Personne ne fait de commentaire. Même Julian."
    menu:
        "Suivre Iris jusqu'à la porte.":
            $ j701_table_choice = "inquietude"
            $ j701_iris_defense = True
            noam neutre "Iris, attends."
            iris fatigue "Quoi ?"
            noam "Tu veux que je t'apporte ton assiette après ?"
            iris "Je n'ai pas faim."
            noam "D'accord."
            "Elle hésite, puis reprend sa marche."
            iris inquiet "Si tu entends quelque chose sur une tablette, même un bruit idiot, tu me préviens."
            noam "Promis."
        "Rester auprès d'Elen.":
            $ j701_table_choice = "complicite"
            elen triste "J'aurais peut-être dû me taire."
            noam neutre "Tu proposais un jeu, pas de débrancher la station."
            elen "Je sais. Mais j'avais juste envie qu'on passe une soirée tranquille."
            noam "On peut toujours essayer."
            elen "Ouais. On verra."
        "Demander à Julian de changer de sujet.":
            $ j701_table_choice = "julian"
            noam "Julian, c'est le moment pour une de tes histoires nulles."
            julian hesitation "Tu te rends compte de ce que tu me demandes ?"
            noam "Oui."
            julian "Alors non."
            "Il croise les bras. C'est la première fois que je le vois refuser une occasion de parler."
    "Kael se lève avec sa tablette. Elle est encore branchée à une batterie externe."
    elias "Tu ne manges pas ?"
    kael "J'ai mangé."
    elias "Du pain. Tu as mangé du pain."
    kael "C'est déjà ça."
    "Elias n'insiste pas. Quand Kael passe devant moi, je remarque qu'il a dessiné des colonnes d'heures au dos de son menu."
    "Lysa me pousse une assiette avec la dernière part de gâteau."
    noam "Elen ne va pas..."
    lysa "C'est la mienne. Mange avant que Julian revienne."
    "Elle regarde vers la porte par laquelle Iris est sortie."
    lysa "Et garde-en un bout. Elle mangera peut-être plus tard."
    $ hideGroup()
    jump _7_0_1_TEMPS_LIBRE_1

label _7_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_284
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflechit", 0.31), ("noam", "neutre", 0.72)])
    "Kael est assis sur un carton vide, face à la porte du local technique. À côté de lui, plusieurs feuilles couvertes de chiffres."
    "Il tient un morceau de pain dans une main et un crayon dans l'autre. Le pain porte une trace de graphite."
    noam "T'as essayé de manger ton crayon ?"
    kael reflechit "Quoi ?"
    "Il regarde ses mains, puis repose lentement le pain."
    kael "Ah. Non."
    noam "Tu m'as l'air en pleine forme."
    kael "Je vérifiais une addition."
    noam "Avec tes dents ?"
    kael "Tu es venu pour quoi ?"
    noam "Je passais. J'ai vu quelqu'un essayer de déjeuner avec du matériel de bureau."
    kael "Ce n'était pas volontaire."
    noam "C'est encore plus inquiétant."
    "Je m'assieds sur le carton d'en face. Il ne me demande pas de partir."
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
    noam "Tu faisais quoi avant de venir ici, quand tu n'avais rien à réparer ?"
    kael reflechit "Pourquoi ?"
    noam "Parce que je me demande si quelqu'un a déjà réussi à te faire poser un outil."
    kael "Je faisais des maquettes."
    noam "Des maquettes de machines ?"
    kael "De bateaux."
    noam "Ah."
    kael "Des voiliers. Avec des pièces en bois. Ça prenait des semaines."
    noam "Tu naviguais ?"
    kael "Non."
    noam "Évidemment."
    kael "Quoi ?"
    noam "Rien. Je m'étais imaginé un grand marin."
    kael "Je suis malade en mer."
    "Il le dit avec un tel sérieux que je me mets à rire. Kael attend que j'aie terminé."
    kael "Je ne vois pas ce qu'il y a de drôle."
    noam "Non, c'est bon. Garde tes bateaux."
    "Il pousse une feuille sous la pile. Je remarque qu'il a dessiné une petite coque dans la marge."
    noam "Et tes relevés, alors ? Tu as trouvé quelque chose ?"
    kael reflechit "La station continue de fonctionner. C'est tout ce que je peux affirmer."
    noam "Tu crois que Kami s'est mise en veille ?"
    kael "C'est possible."
    noam "Et tu crois qu'elle peut revenir ?"
    kael "Ça aussi."
    noam "Tu devrais faire des conférences. Les gens adorent les réponses comme ça."
    kael sourire "Tu peux aussi aller voir Julian. Il en donne des plus longues."
    "Il reprend la feuille."
    if j601_fracture_trace_saved:
        kael reflechit "Au fait, tu as encore la trace que tu as enregistrée pendant le piratage ?"
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
    "Quand il me voit, il fait mine de consulter l'heure, manque de lâcher l'appareil et le rattrape contre son torse."
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
    tomas "Parce que si je montre ça à la cafétéria, quelqu'un va regarder par-dessus mon épaule."
    noam "Et alors ?"
    tomas "Et alors il va raconter ce qu'il a cru comprendre à quelqu'un qui racontera autre chose. Hier, Elias a demandé si on avait du thé. Ce matin, j'ai entendu dire qu'il avait volé des rations."
    noam "C'est pas la même chose."
    tomas "Non, justement. Moi, je voudrais savoir de quoi je parle avant."
    "Il me laisse enfin approcher de sa tablette, puis change d'avis et la baisse."
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
    tomas inquiet "Mais si je me trompe..."
    noam "Quoi ?"
    tomas "Rien. Il faut d'abord vérifier."
    noam "Tomas, tu m'as traîné jusqu'ici pour ça. Dis-moi."
    tomas "Tu connais les gens. Tu leur dis que les sanctions sont peut-être arrêtées et ils entendent qu'ils peuvent faire ce qu'ils veulent."
    noam "Pas forcément."
    tomas "Il suffit d'un."
    noam "Un quoi ?"
    tomas "Un qui décide d'essayer."
    "Il tape sur l'écran noir avec l'ongle, une fois, puis retire sa main."
    tomas "Et si demain on apprend qu'il y a eu un mort... non. Je veux pas être celui qui a donné l'idée."
    noam "D'accord. Je comprends mieux."
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
    "Quand je reviens, Julian a étalé des cartes sur la table. Elen lui tient le poignet."
    $ showGroup([
        ("iris", "sourire"), ("julian", "sourire"), ("lysa", "reflexion"),
        ("kael", "fatigue"), ("elias", "neutre"), ("mara", "neutre"),
        ("elen", "joie"), ("noam", "neutre")
    ])
    julian surpris "Mais enfin, lâche-moi !"
    elen sourire "Tu allais faire disparaître la carte."
    julian "C'est le principe d'un tour de magie."
    elen "Je sais, mais je veux voir comment tu fais !"
    julian "Si tu vois, ça n'a plus aucun intérêt."
    elen "Mais sinon je ne peux pas savoir si tu triches !"
    mara sourire "Elen, ma chère, c'est littéralement le métier du magicien."
    elen "Alors pourquoi il m'a demandé de regarder ?"
    julian "Les cartes ! Je t'ai demandé de regarder les cartes !"
    iris rire "Arrête, Julian. Elle va finir par te démonter les manches."
    lysa blase "Il n'a pas besoin d'aide pour ça."
    noam sourire "Je vois que vous avez trouvé de quoi vous occuper."
    julian "Très bien. Noam, viens là. Tu seras mon spectateur."
    noam "Je viens juste d'entrer."
    julian "Justement. Tu n'as pas vu les préparatifs."
    elen "Il a caché un as sous le coude."
    julian colere "ELEN !"
    noam "Ah. Donc tu as caché un as sous le coude."
    julian "Non. Enfin, oui, mais c'est une technique."
    mara taquin "Une technique très impressionnante : il cache des cartes devant nous."
    "Julian ramasse le paquet, le mélange avec un sérieux disproportionné, puis m'en tend une."
    julian neutre "Choisis. Ne me la montre pas."
    "Je prends une carte. Julian attend avec impatience."
    julian "C'est bon ?"
    noam "Oui."
    julian "Remets-la au milieu."
    noam "Voilà."
    "Il coupe le paquet, en tire une carte et la brandit devant nous."
    julian joie "Et voici... !"
    elen "C'est pas la bonne."
    julian "Tu ne connais même pas la carte !"
    noam "Elle a raison. C'est pas la bonne."
    "Julian regarde la carte, puis la retourne discrètement."
    julian "Attendez, je crois que j'ai..."
    iris blase "Tu t'es trompé."
    julian "J'ai perdu le fil."
    elen joie "Mais c'était très bien !"
    julian "Tu dis ça pour me faire plaisir."
    elen "Un peu."
    "Il se laisse tomber sur sa chaise. Mara lui rend l'as qu'il avait abandonné sur la table."
    mara "Tiens. Ton assistant a essayé de s'enfuir."
    julian decu "Merci, Mara."
    "Il reprend le paquet, mais ne tente pas de nouveau tour."
    if j701_table_choice == "julian":
        noam sourire "Je préférais ton discours de tout à l'heure."
        julian "Il était très court."
        noam "C'est pour ça."
        julian "C'est vraiment une journée difficile pour mon talent."
        $ j701_julian_rapport = "taquin"
    elif j50_julian_relation >= 1:
        noam neutre "La prochaine fois, entraîne-toi avec moi avant."
        julian sourire "C'est une proposition d'aide ?"
        noam "Je n'ai jamais dit que je serais bon."
        julian "Ça me rassure."
        $ j701_julian_rapport = "complice"
    else:
        julian neutre "Je vous montrerai un vrai tour demain."
        lysa blase "On aura tous le temps de nous y préparer."
    elen sourire "On pourrait aussi jouer normalement."
    mara "À condition que Julian ne distribue pas."
    julian "Je suis victime d'une campagne de dénigrement."
    "Tomas entre, hésite au seuil, puis repart lorsqu'il aperçoit tout le monde autour de la table."
    "Je manque de me lever pour le rattraper, mais il me fait un petit signe de la main, presque imperceptible. Je reste assis."
    "Iris dépose sa tablette à côté d'elle, écran tourné vers le bas."
    elen "Iris, tu joues ?"
    iris "Je regarde."
    elen "Tu as dit ça hier."
    iris "Et hier j'ai regardé."
    lysa "Elle est cohérente."
    "Elen distribue. Je me retrouve avec une main qui ressemble à un inventaire de cartes manquantes."
    noam "Il en manque toujours trois, à ce paquet ?"
    elen "Oui."
    noam "Comment on fait pour jouer ?"
    mara "On prétend que tout va bien. Apparemment, c'est une compétence qu'on développe ici."
    "Personne ne relève la remarque. Elen demande à Julian de poser une carte et la partie continue."
    "Elen lance une nouvelle partie en mélangeant si mal les cartes que deux tombent par terre."
    julian "Tu veux que je le fasse ?"
    elen "Non. Dès que je te les donne, il manque des cartes."
    julian "Il en manquait déjà trois !"
    elen "Quatre, maintenant."
    "Elias ramasse l'une des cartes, mais reste à genoux une seconde pour chercher sous la table."
    mara "Tu as perdu quoi, cette fois ?"
    elias "Une carte."
    mara "Tu l'as dans la main."
    elias "Ah."
    "Il remonte sur sa chaise. Quelques secondes plus tard, il se penche vers Kael, assez près pour lui parler sans attirer l'attention."
    elias reflechit "Tu as cinq minutes après ?"
    kael "Pour quoi ?"
    elias "Mon inventaire."
    kael "Celui des outils ?"
    elias "Ouais."
    kael "Demain matin. J'ai passé la journée sur les relevés."
    elias inquiet "Je sais, mais il y a un problème."
    kael "Quel genre ?"
    elias "Je ne retrouve pas deux batteries."
    kael reflechit "On a reçu des caisses aujourd'hui."
    elias "Je sais. J'ai vérifié celles de la maintenance."
    "Kael pose ses cartes."
    kael "Tu as regardé dans le stockage ?"
    elias "Oui."
    kael "Et les registres de livraison ?"
    elias "C'est ce que je viens de dire, j'ai..."
    "Il s'interrompt. Julian et Elen continuent de discuter au-dessus de leurs cartes."
    elias gene "Pardon. Je voulais pas vous couper."
    julian "Tu ne nous coupes pas. On essaie de savoir si Elen a gagné."
    elen "J'ai gagné."
    mara neutre "On attend qu'Elen comprenne qu'elle a perdu."
    elen "Je n'ai pas perdu !"
    lysa "Tu as posé toutes tes cartes."
    elen "Ah."
    elen sourire "Bon. Alors j'ai gagné ?"
    mara "Non."
    "La table éclate de rire. Elias essaie de sourire, mais regarde encore Kael."
    noam reflechit "Elias, tu as besoin d'un coup de main ?"
    elias "Pas forcément. Je voulais juste savoir si quelqu'un avait déplacé des affaires pendant le tri."
    noam "Quelles affaires ?"
    elias "Deux batteries. Des petits composants. Quelques outils."
    "Elias regarde vers la porte, comme s'il espérait voir Nyra entrer à cet instant."
    mara neutre "Tu les avais comptés quand ?"
    elias "Ce matin, avant le ravitaillement."
    mara "Et tu as recompté après ?"
    elias "Oui."
    mara "Tu es sûr que tu n'as pas mis les batteries ailleurs ?"
    elias colere "Oui !"
    "Mara ne répond pas immédiatement. Elias se frotte le visage."
    elias gene "Désolé. J'ai fait le tour trois fois. Je sais plus où chercher."
    iris reflechit "Il faut vérifier les listes de Nyra."
    elen "Elle a encore les tableaux qu'on a remplis dans le couloir."
    if j701_nyra_sorting == "inventaire":
        noam neutre "On a noté les numéros des colis sans étiquette. Je peux lui demander la liste."
        kael "Ça nous donnera déjà un point de départ."
    else:
        noam neutre "On a laissé les caisses non identifiées dans le stockage. Il faudra commencer par là."
        lysa blase "Nyra va adorer l'apprendre."
    julian hesitation "Vous pensez qu'on a perdu tout ça en une matinée ?"
    elias "Je ne sais pas !"
    julian "D'accord. Je demandais juste."
    "Julian pose ses cartes. Elias les regarde, puis se retourne aussitôt vers Kael."
    elias "Je demande juste cinq minutes. Pas une réunion."
    kael "Et je t'ai dit que je viendrais demain."
    elias "Tu dis ça depuis ce matin."
    kael "Parce que tu me demandes depuis ce matin."
    elen "On peut terminer la partie avant ?"
    elias "Oui, pardon. Faites comme si j'avais rien dit."
    "Il tend la main vers ses cartes sans les regarder."
    mara "Personne n'a dit ça."
    elias "Bah, j'ai compris."
    "Kael soupire. Il semble sur le point de répondre, mais préfère examiner la carte qu'il vient de tirer."
    elen inquiet "On n'a peut-être rien perdu. Quelqu'un a pu les déplacer pour nettoyer."
    mara neutre "C'est possible."
    "Elias regarde les autres, un peu perdu."
    elias "Il y avait des outils de coupe avec."
    iris "Des outils de coupe ?"
    elias "Oui. Enfin, ça ne veut pas dire quoi que ce soit. C'est du matériel normal pour un atelier."
    mara "Alors ne le dis pas avec cette tête."
    elias "Quelle tête ?"
    mara "Celle que tu fais quand tu vas nous annoncer qu'un moteur a pris feu."
    elias "Je fais pas une tête spéciale."
    noam sourire "Un peu, si."
    "Il me lance un regard vexé, puis soupire."
    kael reflechit "Il y a des caméras dans le stockage, mais je ne sais pas si on peut consulter les enregistrements sans Kami."
    iris inquiet "On n'a qu'à lui demander."
    "Elle regarde immédiatement l'écran noir."
    iris fatigue "Enfin. Quand elle répondra."
    elen neutre "On peut commencer par chercher. Pas besoin d'en faire toute une histoire."
    lysa "Oui. Mais pas en fouillant les chambres des autres."
    mara "Personne n'a parlé de ça."
    lysa "Je préfère le dire avant."
    julian "Je suis d'accord. Il faut éviter d'accuser quelqu'un sur un doute."
    mara "Tu avais déjà trouvé le coupable avant qu'on te dise ce qui manquait."
    julian "Je n'ai nommé personne !"
    elen "On pourrait au moins finir la partie. Si les outils ont bougé, ils vont pas repartir pendant qu'on joue."
    elias colere "Moi, je les cherche depuis ce matin !"
    "Elen reste un instant bouche bée."
    elias gene "Désolé. Je voulais pas te parler comme ça."
    elen "Non, mais... c'est bon."
    "Elle rassemble lentement les cartes. Julian l'aide sans faire de remarque."
    kael reflechit "Elias. On commence par les registres. Après, je regarde les relevés des caméras si j'arrive à les ouvrir."
    elias "Tu peux vraiment ?"
    kael "J'ai dit « si »."
    noam "Je peux aller au stockage avec vous. J'y ai passé une bonne partie de la matinée."
    lysa "J'y retournerai aussi. Je veux surtout être sûre que personne n'ouvre une chambre pour retrouver une batterie."
    mara "Tu peux arrêter de répéter ça ?"
    lysa "Quand vous arrêterez de me regarder comme si j'étais parano."
    "Mara lève les mains et sort la première. Lysa ne la suit pas tout de suite."
    iris "Et cette fois, on ne touche pas aux boutons au hasard."
    elias "JE SAIS !"
    "Il baisse le ton."
    elias gene "Pardon."
    "Elen remet les cartes dans leur boîte. Elle garde les yeux baissés, sans essayer de retenir les autres."
    "La partie est terminée, mais je n'ai pas l'impression que tout le monde est d'accord sur ce qu'on fait."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE


label _7_0_1_FIN_JOURNEE:
    "Nous finissons par ranger les dernières caisses. Les batteries ne sont toujours pas là."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([("noam", "neutre", 0.50)])
    "Je croise Elen près des chambres. Elle tient une petite assiette recouverte d'un mouchoir."
    noam sourire "Qu'est-ce que tu transportes ?"
    elen sourire "La part de Ryn."
    noam "Il n'est toujours pas venu la prendre ?"
    elen "Non. Je pensais la laisser devant sa porte."
    noam "Sans lui demander ?"
    elen "C'est un gâteau, Noam. Pas un ultimatum."
    noam sourire "Vu ce qui s'est passé avec Julian, je ne suis pas si sûr."
    "Elen sourit, puis regarde l'assiette."
    elen neutre "Je ne veux pas qu'il croie qu'on l'a oublié."
    noam "Tu peux lui écrire un mot."
    elen "J'ai essayé. J'ai écrit « Bon courage ». C'était nul."
    noam "Écris juste « J'ai gardé une part »."
    elen "C'est mieux ?"
    noam "Je crois."
    "Elle réfléchit, puis sourit."
    elen "D'accord. Merci."
    "Elle part vers la chambre de Ryn avec son assiette. Je reste une seconde dans le couloir."
    if j701_tomas_secret_kept:
        "Ma tablette vibre. Tomas m'a envoyé un message : « Je vais revérifier demain matin. Bonne nuit. »"
        "Je réponds : « Bonne nuit. Dors pour de vrai. »"
        "Il m'envoie un pouce levé presque immédiatement."
        think "Je ne crois pas qu'il dormira beaucoup."
    else:
        "Ma tablette vibre. Tomas m'écrit : « J'ai envoyé les relevés à Kael. Il les regardera demain. »"
        "Je réponds : « Merci. Ne passe pas la nuit dessus. »"
        "Tomas commence à écrire, s'arrête, puis répond simplement : « D'accord. »"
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    "Je pose la tablette sur le bureau et retire ma veste."
    "Il y a encore une chaussette sous le lit. Ce matin, j'étais persuadé de les avoir toutes les deux."
    noam neutre "Il faut vraiment que je range cette chambre."
    "J'ouvre le tiroir, y fourre la chaussette et cherche le dessin de Juliette pour le déplacer avant de nettoyer."
    "Il n'est pas à côté du cadre."
    noam surpris "Tiens."
    "Je soulève ma tablette. Rien dessous."
    "Je regarde derrière le cadre, puis sous les feuilles posées près de la lampe."
    noam neutre "Je l'ai mis où, encore ?"
    "Je retrouve une vieille note, une étiquette arrachée à un carton, un sachet vide. Pas le dessin."
    "Je repousse la chaise et me baisse pour regarder sous le bureau."
    noam inquiet "Non. Il était là ce matin."
    "Je vérifie ma poche intérieure, puis la poche extérieure de la veste. Un mouchoir, deux petits papiers, rien d'autre."
    "Je reprends le tiroir depuis le début."
    noam "Allez..."
    "Je vide les affaires sur le lit. Des vêtements, un chargeur, la boîte qui contenait le dessin pendant le voyage."
    "Je l'ouvre."
    "Vide."
    "Je la secoue, même si je vois bien qu'il n'y a rien dedans."
    noam inquiet "Mais c'est pas possible."
    "Je m'assieds sur le bord du lit, la boîte ouverte dans les mains."
    "Juliette avait insisté pour que je ne le plie pas. Je lui avais même promis de le poser quelque part où je le verrais tous les jours."
    "Je me relève et inspecte l'espace entre le bureau et le mur. J'y glisse les doigts jusqu'au fond."
    "Toujours rien."
    noam colere "Putain !"
    "J'ouvre brusquement l'armoire. Une pile de vêtements bascule sur le sol."
    "Je reste devant, incapable de me rappeler ce que je cherchais exactement à cet endroit."
    noam fatigue "Bon. D'accord."
    "Je ramasse les vêtements. Puis je recommence à chercher."
    "À force de déplacer les affaires, je ne sais même plus ce qui était à sa place au départ."
    "Je me souviens pourtant l'avoir soulevé ce matin. Je lui ai parlé, même. C'était idiot, mais je l'ai fait."
    "Je m'arrête au milieu de la chambre."
    noam triste "Juliette..."
    "Je regarde vers la porte. Lysa était restée dans le couloir ce matin. Elle n'a même pas mis un pied ici."
    "Je pourrais aller lui demander de m'aider à chercher, mais... lui expliquer quoi ? Que j'ai perdu un dessin sur mon propre bureau ?"
    menu:
        "Demander de l'aide à Lysa malgré la gêne.":
            noam inquiet "Bon. Tant pis."
            "J'ouvre la porte et passe la tête dans le couloir. Personne. Je lui envoie un message : « Tu dors ? J'ai perdu quelque chose. »"
            "Les trois petits points apparaissent, disparaissent, puis reviennent."
            lysa "C'est grave ?"
            noam "Pour moi, oui."
            lysa "D'accord. Je passe demain matin. Ne retourne pas la chambre pendant la nuit."
            "Je regarde les vêtements étalés sur mon lit."
            noam fatigue "Trop tard."
            "Elle répond par un simple « ... »."
            $ j701_lysa_search_help = True
        "Ne rien dire à personne pour l'instant.":
            "Je reprends le dessin dans ma tête : le papier, le coin légèrement plié, l'endroit où je l'avais posé."
            "Je vois très bien ma main le remettre sur le bureau ce matin."
            "Mais après ? Rien."
            noam inquiet "Je comprends pas."
            "Je prends ma tablette pour écrire à Lysa, puis la repose. Je ne sais même pas ce que je lui demanderais."
    $ noam_has_juliette_drawing = False
    "Je remets les objets à leur place, un par un. Je laisse seulement la boîte vide sur le bureau."
    "Au moment d'éteindre la lampe, je rouvre encore le tiroir."
    "Toujours rien."
    if j701_lysa_search_help:
        noam triste "Demain, je chercherai avec Lysa."
    else:
        noam triste "Demain, je demanderai aux autres."
    $ hideGroup()
    "Je me couche. Au bout d'un moment, les bruits du dortoir s'éteignent."
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_1_0_0_CANON
