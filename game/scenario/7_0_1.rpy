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
    "Kael est assis sur une caisse. Il a un morceau de pain dans une main, un crayon dans l'autre et les yeux fixés sur une addition."
    noam "Tu vas vraiment manger ça ?"
    kael "Oui."
    noam "Il y a du graphite dessus."
    "Kael regarde le pain, puis le crayon. Il pose les deux."
    kael "Ah."
    "Je m'assieds sur la caisse d'en face."
    noam "Tu as dormi ?"
    kael "Deux heures. Peut-être."
    noam "Depuis hier ?"
    kael "Oui."
    "Il me montre une feuille où les heures ne se suivent pas dans le bon ordre."
    kael "Les relevés du Conclave et ceux de l'observatoire ne correspondent pas. J'essaie de savoir quand la liaison s'est réellement interrompue."
    noam "Tu ne peux pas les comparer sur une tablette ?"
    kael "C'est ce que j'ai fait. Les tablettes pensent toutes avoir raison."
    noam "Tu as l'air de leur en vouloir."
    kael "Un peu."
    "Son crayon roule et tombe. Il se penche pour le récupérer, puis reste quelques secondes à regarder sous la caisse."
    noam "Kael ?"
    kael "J'ai trouvé une vis."
    noam "Super."
    kael "Elle vient de mon casque."
    "Il la glisse dans sa poche et se redresse."
    kael "Tu sais, avant, je construisais des maquettes."
    noam "Quel genre ?"
    kael "Des voiliers. En bois."
    noam "Tu naviguais ?"
    kael "Non. J'ai le mal de mer."
    noam "Tu te moques de moi."
    kael "Pas du tout."
    "Je m'attends à ce qu'il sourie. Il recommence plutôt son addition."
    noam "Et tu faisais quoi, une fois le bateau fini ?"
    kael "Je le rangeais dans une vitrine."
    noam "Ça te manque ?"
    kael "Le bois, oui. Les écrans, moins."
    "Il rature une ligne et reprend depuis le début."
    if j601_fracture_trace_saved:
        kael "Tu as conservé la trace du piratage sur ta tablette ?"
        noam "Oui."
        kael "Garde-la. Je voudrais comparer les horodatages avec ceux de la station."
        noam "Tu veux que je te l'envoie ?"
        kael "Pas encore. J'ai besoin de voir la version originale."
        $ j701_evidence_note = True
    else:
        kael "J'aurais aimé avoir une trace complète de ce que nous avons vu hier."
        noam "J'étais là. J'ai tout vu."
        kael "Tu en as vu une partie. Moi aussi. C'est justement le problème."
    noam "Tu crois qu'elle va revenir ?"
    kael "Oui."
    noam "Tu en es sûr ?"
    kael "Non."
    "Il a répondu trop vite. Il s'en rend compte, mais ne corrige pas."
    noam "Essaie au moins de dormir une heure."
    kael "Après les relevés."
    noam "C'est ce que tu disais tout à l'heure."
    kael "Je sais."
    "Je le laisse à ses papiers. En me retournant, je le vois reprendre le morceau de pain couvert de graphite. Il hésite, puis l'abandonne définitivement."
    $ hideGroup()
    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1

label _7_0_1_APRES_MIDI_TOMAS_CANON:
    $ current_period = "Après-midi"
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.29), ("noam", "neutre", 0.72)])
    "Tomas m'attend à l'extérieur de la cafétéria. Dès qu'il m'aperçoit, il retourne sa tablette contre son torse."
    tomas "Noam. Il faut que tu viennes voir un truc."
    noam "Où ça ?"
    tomas "Au canon."
    noam "Pourquoi ?"
    tomas "J'ai besoin d'un deuxième avis."
    noam "Celui de Kael ?"
    tomas "Non. Le tien."
    "Il vérifie que personne n'arrive derrière moi."
    noam "Tomas, tu commences à me faire peur."
    tomas "Je sais. Désolé. Mais si je t'explique ici, quelqu'un va entendre la moitié de ce que je dis."
    noam "Alors explique-moi là-bas."
    "Il hoche la tête et prend les devants. Il marche beaucoup plus vite que d'habitude."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_286
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Tomas referme la porte et connecte sa tablette à la console. Sur l'écran, quatre colonnes de chiffres défilent avec des erreurs de synchronisation."
    tomas reflechit "Les registres de sanctions. J'ai cherché les derniers relevés de chaque district."
    noam "Et ?"
    tomas "Et je crois que quelque chose cloche."
    noam "Tu crois ?"
    tomas "Je ne veux pas dire de bêtises."
    "Il me montre quatre indicateurs clignotants."
    tomas "Les valeurs se mélangent. Il faut retrouver la dernière donnée stable, puis regarder le total."
    noam "Tu l'as fait ?"
    tomas "J'ai essayé. Deux fois. Je me suis trompé sur le flux de l'Est."
    noam "Et tu veux que je m'y mette."
    tomas "Oui. S'il te plaît."
    call j701_play_console from _call_j701_play_console
    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ showGroup([("tomas", "inquiet", 0.30), ("noam", "neutre", 0.70)])
    "Les quatre flux se figent. La dernière colonne s'actualise."
    "0."
    noam surpris "Attends. Ça ne peut pas être le total."
    tomas "J'ai pensé la même chose."
    noam "Remonte à la veille."
    "Il fait défiler les enregistrements. Des dizaines de lignes chiffrées apparaissent."
    noam "Donc il y avait des sanctions avant."
    tomas "Oui."
    noam "Et depuis le piratage ?"
    tomas "Aucune enregistrée."
    "Je vérifie le nom du tableau. Tomas ouvre le détail du premier district, puis du deuxième."
    noam "Tout à zéro ?"
    tomas "Les quatre."
    noam "Tu as essayé avec un autre terminal ?"
    tomas "L'archive n'est plus accessible. Ici, les relevés locaux s'affichent encore."
    noam "Ça peut simplement vouloir dire que les données ne remontent plus."
    tomas "Je sais."
    "Je regarde le canon derrière la vitre. Il est immobile, comme toujours."
    noam "Mais si ce n'est pas ça..."
    tomas "Oui."
    "Je prends ma tablette et ouvre la messagerie. J'entre le nom d'un contact sur Terre, puis j'efface le message sans l'envoyer."
    tomas "Tu fais quoi ?"
    noam "J'allais demander si quelqu'un avait remarqué quelque chose."
    tomas "Non. Attends."
    noam "Pourquoi ?"
    tomas inquiet "Parce qu'on ne sait rien, Noam. On voit des cases vides."
    noam "Des cases vides sur le compteur qui décide si les gens vont mourir."
    tomas "Justement."
    "Il rapproche la tablette de lui, puis réfléchit."
    tomas "Si on raconte que les Commandements ne fonctionnent plus et que c'est faux..."
    noam "Je ne comptais pas publier un communiqué."
    tomas "Je sais. Mais il suffit qu'une personne entende ça, qu'elle veuille vérifier..."
    "Il s'interrompt. Je pose ma tablette."
    noam "Je n'enverrai rien."
    tomas "Merci."
    "Il inspire longuement. Je ne l'ai jamais vu aussi tendu pour un simple tableau."
    noam "Tu as gardé les relevés ?"
    tomas "Une copie. Et une photo, parce que la dernière fois le fichier s'est corrompu."
    noam "Bien. On peut au moins comparer demain."
    tomas "Avec Kael, peut-être."
    noam "Pourquoi pas maintenant ?"
    tomas "Il n'a presque pas dormi, lui non plus. Je voulais d'abord vérifier que je n'avais pas mal lu."
    "Je laisse les chiffres affichés. J'aurais envie que le système se mette à jour, même avec un nombre terrible. N'importe quoi qui prouve qu'il fonctionne."
    call play_stat_dialogue("d7_0_1") from _call_stat_dialogue_d7_0_1
    menu:
        "Respecter sa demande de discrétion jusqu'au lendemain.":
            $ j701_tomas_secret_kept = True
            noam neutre "On attend demain. Mais demain matin, on vérifie avec quelqu'un d'autre."
            tomas neutre "D'accord."
            noam "Et tu vas dormir."
            tomas "Je vais essayer."
            noam "Ce n'est pas une réponse."
            tomas "Alors non. Je ne peux pas te le promettre."
        "Demander à Tomas de prévenir Kael dès maintenant.":
            $ j701_tomas_secret_kept = False
            $ j701_tomas_informed = True
            noam determine "Envoie au moins les relevés à Kael. Pas une théorie, juste les chiffres."
            tomas inquiet "Tu crois qu'il va s'inquiéter ?"
            noam "Oui. Mais il est ingénieur. C'est son travail."
            "Tomas écrit un message, l'efface une fois, puis joint les fichiers."
            tomas "Voilà. Je lui demande de regarder demain."
            noam "Merci."
    "Tomas m'accompagne à la porte. Avant de sortir, je regarde une dernière fois le total général."
    "Toujours zéro."
    $ hideGroup()
    jump _7_0_1_SOIREE_TENSION_LEGERE


label _7_0_1_SOIREE_TENSION_LEGERE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_287
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2
    "Quand je rentre, Elen et Julian ont sorti un jeu de cartes. Il manque plusieurs cartes, mais ça ne semble gêner personne."
    $ showGroup([
        ("iris", "fatigue"), ("julian", "neutre"), ("lysa", "neutre"),
        ("kael", "fatigue"), ("elias", "inquiet"), ("mara", "neutre"),
        ("elen", "sourire"), ("noam", "neutre")
    ])
    julian "J'ai une question très simple. Quelqu'un a vu l'as de pique ?"
    elen "Tu l'avais tout à l'heure."
    julian "Ça ne répond pas à ma question."
    elen "C'est toi qui l'as perdu."
    julian "Merci. Très utile."
    "Elen retourne une carte et la pose devant lui."
    elen sourire "Celle-là ?"
    julian "Non. Mais je vais faire avec."
    "Je m'assieds. Kael semble trop fatigué pour suivre le jeu. Elias ne regarde même pas ses cartes."
    elen "Allez, on distribue ?"
    elias inquiet "Deux batteries ont disparu."
    "Elen garde une carte entre deux doigts."
    elen "Quoi ?"
    elias "Je cherche depuis ce matin. Deux batteries, un micro-soudeur et des stabilisateurs."
    kael "Tu les as peut-être déplacés pendant les livraisons."
    elias "Non."
    kael "On regardera demain."
    elias colere "Tu m'as déjà dit ça trois fois !"
    "Kael relève les yeux. Elias s'arrête, comme surpris d'avoir crié."
    elias "Pardon. Mais j'ai tout vérifié. Je sais où je range mes affaires."
    mara "Tu es sûr de ton compte ?"
    elias "Oui."
    mara "D'accord."
    elias surpris "D'accord ?"
    mara "Je te crois sur le compte. Ça ne dit pas qui les a pris."
    "Elias me regarde, puis revient à Kael."
    elias "Il manque des outils de coupe aussi. Si quelqu'un les a empruntés, je veux juste qu'il me le dise."
    elen inquiet "On peut finir la partie et regarder après ?"
    "Elias se lève."
    elias "Tu sais quoi ? Oui. Finissez votre partie."
    elen "Elias, je voulais pas..."
    elias "Je sais."
    "Il prend sa tablette et marche vers la porte. Kael attrape son poignet au passage."
    kael reflechit "Attends. Quelles batteries ?"
    elias "Les deux grosses du stockage."
    kael "Celles qui sont sur l'étagère avec le capteur de masse ?"
    elias "Oui."
    kael "Le registre indique toujours qu'elles y sont."
    "Elias ouvre la bouche. Cette fois, il ne trouve rien à répondre."
    nyra "C'est impossible. Si le poids change, le système le note."
    "Nyra vient d'entrer. Elle pose le registre de la livraison sur la table."
    lysa "Sauf si quelqu'un s'est arrangé pour que le poids ne change pas."
    "Personne ne rit."
    elen "Attendez. On parle d'un vol ?"
    elias inquiet "C'est ce que j'essaie de vous dire !"
    kael "On va vérifier l'étagère. Maintenant."
    julian "Vous voulez qu'on vienne tous ?"
    mara "Pas pour faire du bruit. Pour regarder."
    "Elen rassemble les cartes à la hâte. Julian l'aide, puis garde l'as qu'il vient de retrouver sous son coude."
    elen "Tu l'avais là depuis le début ?"
    julian "Oui."
    elen "Ah."
    "Pour une fois, elle ne s'en sert pas pour se moquer de lui."
    $ hideGroup()
    call j701_investigation from _call_j701_investigation
    jump _7_0_1_FIN_JOURNEE

label _7_0_1_FIN_JOURNEE:
    "Nous finissons par fermer le stockage. Les pièces volées sont introuvables."
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_288
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([("noam", "neutre", 0.50)])
    "Elen attend devant la chambre de Ryn avec une assiette recouverte d'un mouchoir."
    noam "Qu'est-ce que tu fais ?"
    elen sourire "Il n'a pas mangé avec nous. Je lui ai gardé une part."
    noam "Tu l'as déjà appelé ?"
    elen "Il m'a dit de le laisser tranquille."
    noam "Et tu es venue quand même."
    elen "Je vais pas le forcer à me parler. Je veux juste qu'il mange."
    "Elle pose l'assiette près de la porte et se redresse."
    elen "C'est idiot ?"
    noam "Non."
    elen "Tu peux me dire si c'est idiot."
    noam "Je viens de le faire."
    "Elle hésite un peu, puis retourne vers les chambres."
    if j701_tomas_secret_kept:
        "Ma tablette vibre. Tomas m'écrit : « Je revérifie demain matin. Je n'ai rien dit. »"
        "Je réponds : « Dors quand même. »"
    else:
        "Ma tablette vibre. Tomas m'écrit : « Kael a reçu les fichiers. Il regarde demain. »"
        "Je réponds : « Merci. »"
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_289
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je retire ma veste et la jette sur le lit. Le tiroir du bureau est entrouvert."
    "Je m'approche pour le refermer. Le dessin de Juliette n'est plus à côté du cadre."
    noam surpris "Hein ?"
    "Je soulève le cadre. Je cherche sous la tablette, dans le tiroir, derrière la lampe."
    noam "Non. Attends."
    "Ce matin, il était là. Je l'ai soulevé pour récupérer ma chaussette. J'en suis certain."
    "Je vérifie la boîte dans laquelle je l'avais transporté jusqu'au Conclave. Vide."
    "Je regarde derrière le bureau, puis sous le lit. Je ne trouve que des vêtements et de la poussière."
    noam inquiet "Mais je l'ai pas sorti de la chambre..."
    "Je me redresse. Mon regard se pose sur la porte."
    "Elle est fermée. Je n'ai aucun moyen de savoir si quelqu'un l'a ouverte pendant mon absence."
    "Je retourne le cadre. Je le retourne encore. C'est absurde, je sais très bien que le dessin n'est pas dedans."
    "Je finis par poser la boîte vide sur le bureau."
    noam triste "Juliette..."
    "Je prends ma tablette. Le nom de Lysa apparaît dans mes conversations récentes."
    menu:
        "Demander à Lysa de m'aider à chercher demain.":
            $ j701_lysa_search_help = True
            "Je lui écris : « T'es réveillée ? J'ai perdu quelque chose d'important. Tu pourrais m'aider demain ? »"
            "Sa réponse arrive presque tout de suite."
            lysa "Oui. N'y touche plus pour ce soir. On regardera ensemble."
            noam "D'accord. Merci."
            "Je n'ai pas envie d'expliquer ce que c'est par message."
        "Garder la disparition pour moi cette nuit.":
            "Je commence à écrire à Lysa. J'efface."
            "Si je l'ai simplement rangé ailleurs, j'aurai l'air malin."
            "Je pose la tablette. Je la reprends, puis je la verrouille."
    $ noam_has_juliette_drawing = False
    "Je prends une dernière fois la boîte vide. Les coins du carton sont légèrement usés à l'endroit où Juliette avait insisté pour que je fasse attention au papier."
    "Je ferme le tiroir et je vérifie la serrure de ma porte."
    "Elle affiche VERROUILLÉE."
    "Ça ne m'aide pas autant que je l'espérais."
    $ hideGroup()
    scene black with fade
    call end_day("8", sleeping=True) from _call_end_day_11
    jump _8_1_0_0_CANON
