default room_scene_indices = {}
default noam_room_has_jammer = True

init -2 python:
    im = renpy.display.im
    ROOM_SCENE_DIR = "images/background/scene"
    ROOM_INTERACT_DIR = "images/background/interact"
    ROOM_SCENE_EXTENSIONS = ("png", "webp", "jpg", "jpeg")
    ROOM_SCENE_ANIM_HOLD = 1.4
    ROOM_SCENE_ANIM_FADE = 0.45
    ROOM_SCENE_NAV_WIDTH = 44

    def room_scene_find_asset(stem):
        for ext in ROOM_SCENE_EXTENSIONS:
            path = "%s/%s.%s" % (ROOM_SCENE_DIR, stem, ext)
            if renpy.loadable(path):
                return path
        return None

    def room_scene_legacy_asset(room_name):
        for ext in ROOM_SCENE_EXTENSIONS:
            path = "images/background/bg_%s.%s" % (room_name, ext)
            if renpy.loadable(path):
                return path
        return None

    def room_scene_variant_numbers(room_name):
        numbers = []
        for idx in range(1, 100):
            if room_scene_find_asset("%s%s" % (room_name, idx)):
                numbers.append(idx)
        return numbers

    def room_scene_has_variants(room_name):
        return len(room_scene_variant_numbers(room_name)) > 1

    def room_scene_current_number(room_name):
        numbers = room_scene_variant_numbers(room_name)
        if not numbers:
            return None

        current = store.room_scene_indices.get(room_name, numbers[0])
        if current not in numbers:
            current = numbers[0]
            store.room_scene_indices[room_name] = current
        return current

    def room_scene_step(room_name, direction):
        numbers = room_scene_variant_numbers(room_name)
        if len(numbers) <= 1:
            return

        current = room_scene_current_number(room_name)
        pos = numbers.index(current)
        store.room_scene_indices[room_name] = numbers[(pos + direction) % len(numbers)]
        renpy.restart_interaction()

    def room_scene_stem(room_name):
        current = room_scene_current_number(room_name)
        if current is None:
            return room_name
        return "%s%s" % (room_name, current)

    def room_scene_frame_paths(room_name):
        current = room_scene_current_number(room_name)
        if current is None:
            legacy = room_scene_legacy_asset(room_name)
            return [legacy] if legacy else []

        stem = "%s%s" % (room_name, current)
        frames = []

        base = room_scene_find_asset(stem)
        if base:
            frames.append(base)

        for idx in range(1, 100):
            frame = room_scene_find_asset("%s_%s" % (stem, idx))
            if not frame:
                break
            frames.append(frame)

        return frames

    def room_scene_native_size(path):
        try:
            return renpy.image_size(path)
        except Exception:
            return (1536, 1024)

    def room_scene_frame_displayable(path, alpha=1.0):
        return Transform(Image(path), alpha=alpha)

    def room_scene_crossfade_displayable(first, second, alpha):
        sw, sh = room_scene_native_size(first)
        return LiveComposite(
            (sw, sh),
            (0, 0), room_scene_frame_displayable(first, 1.0),
            (0, 0), room_scene_frame_displayable(second, alpha),
        )

    def room_scene_dynamic(st, at, room_name):
        frames = room_scene_frame_paths(room_name)
        if not frames:
            return Solid("#000"), 1.0
        if len(frames) == 1:
            return room_scene_frame_displayable(frames[0]), 0.25

        step = ROOM_SCENE_ANIM_HOLD + ROOM_SCENE_ANIM_FADE
        frame_index = int(st / step) % len(frames)
        phase = st % step

        if phase < ROOM_SCENE_ANIM_HOLD:
            return room_scene_frame_displayable(frames[frame_index]), max(0.05, ROOM_SCENE_ANIM_HOLD - phase)

        next_index = (frame_index + 1) % len(frames)
        alpha = min(1.0, max(0.0, (phase - ROOM_SCENE_ANIM_HOLD) / ROOM_SCENE_ANIM_FADE))
        return room_scene_crossfade_displayable(frames[frame_index], frames[next_index], alpha), 0.03

    def room_scene_displayable(room_name):
        return DynamicDisplayable(room_scene_dynamic, room_name)

    def room_scene_band_displayable(room_name, hover=False):
        sw = ROOM_SCENE_NAV_WIDTH
        sh = config.screen_height
        tint = "#ffffff1f" if hover else "#ffffff10"
        return LiveComposite(
            (sw, sh),
            (0, 0), Transform(Solid("#ffffff08"), xysize=(sw, sh)),
            (0, 0), Transform(Solid(tint), xysize=(sw, sh)),
        )

    def room_interaction_hover(path):
        return im.MatrixColor(
            path,
            im.matrix.brightness(0.22) * im.matrix.saturation(1.15)
        )

    def room_interaction_files(room_name):
        stem = room_scene_stem(room_name)
        base_dir = "%s/%s/" % (ROOM_INTERACT_DIR, room_name)
        scene_dir = "%s%s/" % (base_dir, stem)
        files = []

        for path in renpy.list_files():
            normalized = path.replace("\\", "/")
            if not normalized.startswith(scene_dir):
                continue
            if not normalized.lower().endswith(".png"):
                continue
            key = normalized.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            if key.startswith("brouilleur_"):
                continue
            files.append((key, normalized))

        if stem == "chambre3" and getattr(store, "noam_room_has_jammer", False):
            jammer_key = "brouilleur_on" if getattr(store, "noam_room_jammer_on", False) else "brouilleur_off"
            jammer_path = "%s%s.png" % (scene_dir, jammer_key)
            if renpy.loadable(jammer_path):
                files.append(("brouilleur", jammer_path))

        return sorted(files, key=lambda item: item[0])

    def room_interaction_label(room_name, key):
        return "%s_%s" % (room_scene_stem(room_name), key)

image bg_chambre = DynamicDisplayable(room_scene_dynamic, "chambre")

screen room_scene_background(room_name, navigation=True):
    add room_scene_displayable(room_name) at cover_screen

    if navigation and room_scene_has_variants(room_name):
        use room_scene_navigation_band(room_name, -1, 0)
        use room_scene_navigation_band(room_name, 1, config.screen_width - ROOM_SCENE_NAV_WIDTH)

screen room_scene_navigation_band(room_name, direction, xpos_value):
    button:
        xpos xpos_value
        ypos 0
        xsize ROOM_SCENE_NAV_WIDTH
        ysize config.screen_height
        background room_scene_band_displayable(room_name)
        hover_background room_scene_band_displayable(room_name, True)
        action Function(room_scene_step, room_name, direction)

screen room_scene_interactions(room_name, label_overrides=None):
    $ resolved_label_overrides = label_overrides or {}

    for key, path in room_interaction_files(room_name):
        $ label_name = room_interaction_label(room_name, key)
        $ target_label = resolved_label_overrides.get(label_name, label_name)
        if target_label and renpy.has_label(target_label):
            imagebutton:
                idle (path if key == "brouilleur" else Transform(path, alpha=0.01))
                hover room_interaction_hover(path)
                focus_mask True
                xpos 0
                ypos 0
                at cover_screen
                action Jump(target_label)
