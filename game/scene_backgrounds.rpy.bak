default room_scene_indices = {}
default noam_room_has_jammer = True
default cafeteria_food_level = "high"
default cafeteria_food_visible_cache = None

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
            base = room_scene_find_asset(room_name)
            if base:
                return [base]
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

    def _room_cover_im(path, room_name):
        # Cover-fit CPU (im.Scale + im.Crop) au lieu d'un Transform GPU.
        # CRUCIAL : focus_mask sait lire l'alpha des displayables im.* (CPU)
        # mais PAS d'un Transform "fit"/zoom (GPU) -> c'était la cause du
        # survol non détecté. Résultat caché sur disque par Ren'Py au 1er rendu.
        frames = room_scene_frame_paths(room_name)
        sw, sh = room_scene_native_size(frames[0]) if frames else room_scene_native_size(path)
        W, H = config.screen_width, config.screen_height
        scale = max(float(W) / float(sw), float(H) / float(sh))
        nw, nh = int(round(sw * scale)), int(round(sh * scale))
        ox, oy = (nw - W) // 2, (nh - H) // 2
        # Recale sur la taille native du fond (mêmes coords d'origine) puis
        # scale cover + crop centré = géométrie identique au fond.
        base = im.Composite((sw, sh), (0, 0), path)
        return im.Crop(im.Scale(base, nw, nh), (ox, oy, W, H))

    # Cache des displayables d'interaction : identité stable -> Ren'Py réutilise
    # le rendu ET le focus_mask (construits une seule fois). Supprime le
    # re-render par frame = plus de latence, et fiabilise la détection du survol.
    _room_disp_cache = {}
    _room_null_disp = None

    def room_interaction_layer(path, room_name, kind):
        # kind : "art" (visible / focus_mask) | "hover" (éclairci au survol)
        ck = (room_name, path, kind)
        d = _room_disp_cache.get(ck)
        if d is None:
            cov = _room_cover_im(path, room_name)
            if kind == "hover":
                d = im.MatrixColor(
                    cov,
                    im.matrix.brightness(0.22) * im.matrix.saturation(1.15)
                )
            else:
                d = cov
            _room_disp_cache[ck] = d
        return d

    def room_interaction_null():
        # idle vide plein écran : rien dessiné au repos (0 coût GPU),
        # la zone reste focusable via focus_mask.
        global _room_null_disp
        if _room_null_disp is None:
            _room_null_disp = Null(
                width=config.screen_width, height=config.screen_height
            )
        return _room_null_disp

    # Compat : ancien nom (calques décoratifs éventuels)
    def room_interaction_fit(path, room_name):
        return _room_cover_im(path, room_name)

    def room_interaction_files(room_name):
        stem = room_scene_stem(room_name)
        base_dir = "%s/%s/" % (ROOM_INTERACT_DIR, room_name)
        if room_scene_current_number(room_name) is None:
            scene_dir = base_dir
        else:
            scene_dir = "%s%s/" % (base_dir, stem)
        files = []
        cafeteria_food_keys = cafeteria_visible_food_keys() if room_name == "cafeteria" and stem == "cafeteria3" else None

        for path in renpy.list_files():
            normalized = path.replace("\\", "/")
            if not normalized.startswith(scene_dir):
                continue
            if not normalized.lower().endswith(".png"):
                continue
            key = normalized.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            if key.startswith("brouilleur_"):
                continue
            if cafeteria_food_keys is not None and key.startswith("nourriture") and key not in cafeteria_food_keys:
                continue
            if room_name == "repos" and stem == "repos1" and key.startswith("decor_distributeur_"):
                if key != repos_distributor_decor_key():
                    continue
            if room_name == "repos" and stem == "repos2" and key == "deco_fete":
                if not getattr(store, "repos_party_active", False):
                    continue
            if room_name == "maintenance" and stem == "maintenance1" and key == "deco_outil1":
                if hasattr(store, "vol_outil"):
                    continue
            files.append((key, normalized))

        if stem == "chambre3" and getattr(store, "noam_room_has_jammer", False):
            jammer_key = "brouilleur_on" if getattr(store, "noam_room_jammer_on", False) else "brouilleur_off"
            jammer_path = "%s%s.png" % (scene_dir, jammer_key)
            if renpy.loadable(jammer_path):
                files.append(("brouilleur", jammer_path))

        return sorted(files, key=lambda item: item[0])

    def room_interaction_label(room_name, key):
        if room_name == "cafeteria" and room_scene_stem(room_name) == "cafeteria3" and key.startswith("nourriture"):
            return "cafeteria3_nourriture"
        return "%s_%s" % (room_scene_stem(room_name), key)

    def room_interaction_is_decorative(key):
        return key.startswith("decor_") or key.startswith("deco_")

    def repos_distributor_decor_key():
        count = cafeteria_food_visible_count()
        if count <= 0:
            return "decor_distributeur_vide"
        if count >= 5:
            return "decor_distributeur_plein"
        return "decor_distributeur_mi"

    def cafeteria_food_visible_count():
        level = getattr(store, "cafeteria_food_level", "high")

        try:
            amount = int(level)
            if amount <= 0:
                return 0
            if amount <= 1:
                return 1
            if amount <= 3:
                return 3
            return 5
        except Exception:
            pass

        level_key = str(level).strip().lower()
        if level_key in ("empty", "none", "zero", "vide", "aucune", "0"):
            return 0
        if level_key in ("low", "few", "peu", "faible", "1"):
            return 1
        if level_key in ("medium", "mid", "moyen", "moins", "3"):
            return 3
        return 5

    def cafeteria_visible_food_keys():
        keys = ["nourriture%s" % idx for idx in range(1, 6)]
        count = cafeteria_food_visible_count()

        if count <= 0:
            return set()
        if count >= len(keys):
            return set(keys)

        try:
            day_key = day_number()
        except Exception:
            day_key = 0

        cache_key = (str(getattr(store, "cafeteria_food_level", "high")), count, day_key)
        cache = getattr(store, "cafeteria_food_visible_cache", None)
        if cache and cache.get("key") == cache_key:
            return set(cache.get("keys", []))

        selected = sorted(renpy.random.sample(keys, count))
        store.cafeteria_food_visible_cache = {
            "key": cache_key,
            "keys": selected,
        }
        return set(selected)

image bg_chambre = DynamicDisplayable(room_scene_dynamic, "chambre")
image bg_archive = DynamicDisplayable(room_scene_dynamic, "archive")
image bg_cafeteria = DynamicDisplayable(room_scene_dynamic, "cafeteria")
image bg_conclave = DynamicDisplayable(room_scene_dynamic, "conclave")
image bg_canon = DynamicDisplayable(room_scene_dynamic, "canon")
image bg_gymnase = DynamicDisplayable(room_scene_dynamic, "gymnase")
image bg_repos = DynamicDisplayable(room_scene_dynamic, "repos")
image bg_maintenance = DynamicDisplayable(room_scene_dynamic, "maintenance")
image bg_sas = DynamicDisplayable(room_scene_dynamic, "sas")
image bg_infirmerie = DynamicDisplayable(room_scene_dynamic, "infirmerie")
image bg_stockage = DynamicDisplayable(room_scene_dynamic, "stockage")
image bg_observation = DynamicDisplayable(room_scene_dynamic, "observation")
image bg_repos_fete = LiveComposite(
    (1672, 941),
    (0, 0), "images/background/scene/repos2.png",
    (0, 0), "images/background/interact/repos/repos2/deco_fete.png",
)

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
        if room_interaction_is_decorative(key):
            add room_interaction_layer(path, room_name, "art")
        elif target_label and renpy.has_label(target_label):
            $ idle_disp = room_interaction_layer(path, room_name, "art") if key == "brouilleur" else room_interaction_null()
            imagebutton:
                idle idle_disp
                hover room_interaction_layer(path, room_name, "hover")
                focus_mask room_interaction_layer(path, room_name, "art")
                xpos 0
                ypos 0
                action Jump(target_label)
