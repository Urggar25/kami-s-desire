default room_scene_indices = {}
default noam_room_has_jammer = True
default noam_has_juliette_drawing = True
default cafeteria_food_level = "high"
default cafeteria_food_visible_cache = None
default anya_lit_iris = 0
default anya_lit_infirmerie = 0

init -2 python:
    im = renpy.display.im
    ROOM_SCENE_DIR = "images/background/scene"
    ROOM_INTERACT_DIR = "images/background/interact"
    ROOM_SCENE_EXTENSIONS = ("png", "webp", "jpg", "jpeg")
    ROOM_SCENE_ANIM_HOLD = 1.4
    ROOM_SCENE_ANIM_FADE = 0.45
    ROOM_SCENE_NAV_WIDTH = 44

    # Ces catalogues évitent de rescanner toutes les ressources du jeu à
    # chaque frame d'un décor animé.
    _room_variant_numbers_cache = {}
    _room_frame_paths_cache = {}
    _room_interaction_catalog = None
    _room_composited_frame_cache = {}
    _room_image_cache = {}

    # Étalonnage automatique des décors selon la période narrative.
    # La matrice est recalculée par les DynamicDisplayable : un changement de
    # current_period met donc aussi à jour un décor déjà affiché.
    def automatic_scene_lighting_matrix(period=None):
        value = period if period is not None else getattr(store, "current_period", "Matin")
        key = str(value or "").strip().lower()
        key = key.replace("è", "e").replace("é", "e").replace("ê", "e")

        if "nuit" in key:
            return TintMatrix("#aeb8cf") * SaturationMatrix(0.80) * BrightnessMatrix(-0.20)
        if "soir" in key:
            return TintMatrix("#ead8d0") * SaturationMatrix(0.92) * BrightnessMatrix(-0.10)
        if "midi" in key or "apres" in key:
            return TintMatrix("#f7fbff") * SaturationMatrix(1.015) * BrightnessMatrix(0.01)
        # Matin, fin de matinée et valeur de repli : lumière douce et chaude.
        return TintMatrix("#fff8ed") * SaturationMatrix(1.02) * BrightnessMatrix(0.025)

    def automatic_scene_lighting(displayable):
        return Transform(displayable, matrixcolor=automatic_scene_lighting_matrix())

    def automatic_scene_lighting_dynamic(st, at, displayable):
        return automatic_scene_lighting(displayable), 0.20

    def automatic_scene_image_dynamic(st, at, path):
        image = _room_image_cache.get(path)
        if image is None:
            image = Image(path)
            _room_image_cache[path] = image
        return automatic_scene_lighting(image), 0.20

    def chambre_iris_scene_dynamic(st, at):
        scene_path = "images/background/scene/bg_chambre_iris.png"
        overlays = ()
        if getattr(store, "anya_lit_iris", 0) == 1:
            overlays = ("images/background/interact/chambre_iris/deco_lit_anya.png",)

        scene = room_scene_composited_frame(scene_path, overlays)
        return automatic_scene_lighting(scene), 0.20

    def infirmerie2_scene_dynamic(st, at):
        scene_path = "images/background/scene/infirmerie2.png"
        overlays = ()
        if getattr(store, "anya_lit_infirmerie", 0) == 1:
            overlays = ("images/background/interact/infirmerie/infirmerie2/deco_lit_anya.png",)

        scene = room_scene_composited_frame(scene_path, overlays)
        return automatic_scene_lighting(scene), 0.20

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
        cached = _room_variant_numbers_cache.get(room_name)
        if cached is not None:
            return cached

        numbers = []
        for idx in range(1, 100):
            if room_scene_find_asset("%s%s" % (room_name, idx)):
                numbers.append(idx)
        result = tuple(numbers)
        _room_variant_numbers_cache[room_name] = result
        return result

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
        cache_key = (room_name, current)
        cached = _room_frame_paths_cache.get(cache_key)
        if cached is not None:
            return cached

        if current is None:
            base = room_scene_find_asset(room_name)
            if base:
                result = (base,)
                _room_frame_paths_cache[cache_key] = result
                return result
            legacy = room_scene_legacy_asset(room_name)
            result = (legacy,) if legacy else ()
            _room_frame_paths_cache[cache_key] = result
            return result

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

        result = tuple(frames)
        _room_frame_paths_cache[cache_key] = result
        return result

    def room_scene_native_size(path):
        try:
            return renpy.image_size(path)
        except Exception:
            return (1536, 1024)

    def room_scene_frame_displayable(path, alpha=1.0):
        image = _room_image_cache.get(path)
        if image is None:
            image = Image(path)
            _room_image_cache[path] = image
        if alpha == 1.0:
            return image
        return Transform(image, alpha=alpha)

    def room_scene_crossfade_displayable(first, second, alpha, size):
        sw, sh = size
        return LiveComposite(
            (sw, sh),
            (0, 0), first,
            (0, 0), Transform(second, alpha=alpha),
        )

    def room_interaction_is_visual_overlay(room_name, key):
        """Calques qui font partie de l'état visuel permanent de la salle."""
        if room_interaction_is_decorative(key):
            return True
        if key == "brouilleur":
            return True
        if (
            room_name == "chambre"
            and room_scene_stem(room_name) == "chambre3"
            and key == "photo_juliette"
        ):
            return True
        return (
            room_name == "cafeteria"
            and room_scene_stem(room_name) == "cafeteria3"
            and key.startswith("nourriture")
        )

    def room_scene_visual_overlay_paths(room_name):
        return tuple(
            path for key, path in room_interaction_files(room_name)
            if room_interaction_is_visual_overlay(room_name, key)
        )

    def room_scene_composited_frame(frame_path, overlays):
        """Construit une seule fois une frame avec ses calques conditionnels."""
        cache_key = (frame_path, overlays)
        cached = _room_composited_frame_cache.get(cache_key)
        if cached is not None:
            return cached

        if not overlays:
            result = room_scene_frame_displayable(frame_path)
        else:
            sw, sh = room_scene_native_size(frame_path)
            parts = [(0, 0), room_scene_frame_displayable(frame_path)]
            for path in overlays:
                parts.extend(((0, 0), room_scene_frame_displayable(path)))
            result = LiveComposite((sw, sh), *parts)

        _room_composited_frame_cache[cache_key] = result
        return result

    def room_scene_dynamic(st, at, room_name):
        frames = room_scene_frame_paths(room_name)
        if not frames:
            return automatic_scene_lighting(Solid("#000")), 1.0
        overlays = room_scene_visual_overlay_paths(room_name)
        if len(frames) == 1:
            return automatic_scene_lighting(room_scene_composited_frame(frames[0], overlays)), 0.20

        step = ROOM_SCENE_ANIM_HOLD + ROOM_SCENE_ANIM_FADE
        frame_index = int(st / step) % len(frames)
        phase = st % step

        if phase < ROOM_SCENE_ANIM_HOLD:
            current = room_scene_composited_frame(frames[frame_index], overlays)
            return automatic_scene_lighting(current), min(0.20, max(0.05, ROOM_SCENE_ANIM_HOLD - phase))

        next_index = (frame_index + 1) % len(frames)
        alpha = min(1.0, max(0.0, (phase - ROOM_SCENE_ANIM_HOLD) / ROOM_SCENE_ANIM_FADE))
        current = room_scene_composited_frame(frames[frame_index], overlays)
        following = room_scene_composited_frame(frames[next_index], overlays)
        size = room_scene_native_size(frames[frame_index])
        crossfade = room_scene_crossfade_displayable(current, following, alpha, size)
        return automatic_scene_lighting(crossfade), 0.03

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

    def room_interaction_hover_with_overlays(path, room_name):
        """Garde les compléments visibles au-dessus de leur texture mère."""
        overlays = room_scene_visual_overlay_paths(room_name)
        cache_key = (room_name, path, "hover_with_overlays", overlays)
        cached = _room_disp_cache.get(cache_key)
        if cached is not None:
            return cached

        if not overlays:
            result = room_interaction_layer(path, room_name, "hover")
        else:
            parts = [
                (0, 0), room_interaction_layer(path, room_name, "hover"),
            ]
            for overlay_path in overlays:
                parts.extend((
                    # Les textures filles reçoivent le même hover transparent
                    # que la mère, sans modifier leur canal alpha.
                    (0, 0), room_interaction_layer(overlay_path, room_name, "hover"),
                ))
            result = LiveComposite(
                (config.screen_width, config.screen_height),
                *parts
            )

        _room_disp_cache[cache_key] = result
        return result

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
        global _room_interaction_catalog
        stem = room_scene_stem(room_name)
        base_dir = "%s/%s/" % (ROOM_INTERACT_DIR, room_name)
        if room_scene_current_number(room_name) is None:
            scene_dir = base_dir
        else:
            scene_dir = "%s%s/" % (base_dir, stem)
        files = []
        cafeteria_food_keys = cafeteria_visible_food_keys() if room_name == "cafeteria" and stem == "cafeteria3" else None

        if _room_interaction_catalog is None:
            catalog = {}
            prefix = ROOM_INTERACT_DIR + "/"
            for path in renpy.list_files():
                normalized = path.replace("\\", "/")
                if not normalized.startswith(prefix) or not normalized.lower().endswith(".png"):
                    continue
                directory = normalized.rsplit("/", 1)[0] + "/"
                key = normalized.rsplit("/", 1)[-1].rsplit(".", 1)[0]
                catalog.setdefault(directory, []).append((key, normalized))
            _room_interaction_catalog = {
                directory: tuple(sorted(entries, key=lambda item: item[0]))
                for directory, entries in catalog.items()
            }

        for key, normalized in _room_interaction_catalog.get(scene_dir, ()):
            if key.startswith("brouilleur_"):
                continue
            if (
                stem == "chambre3"
                and key == "photo_juliette"
                and not getattr(store, "noam_has_juliette_drawing", True)
            ):
                continue
            if cafeteria_food_keys is not None and key.startswith("nourriture") and key not in cafeteria_food_keys:
                continue
            if room_name == "repos" and stem == "repos1" and key.startswith("decor_distributeur_"):
                if key != repos_distributor_decor_key():
                    continue
            if room_name == "repos" and stem == "repos2" and key == "deco_fete":
                if not getattr(store, "repos_party_active", False):
                    continue
            if room_name == "infirmerie" and stem == "infirmerie2" and key == "deco_lit_anya":
                if getattr(store, "anya_lit_infirmerie", 0) != 1:
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

        return files

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
image bg_repos_fete = DynamicDisplayable(
    automatic_scene_lighting_dynamic,
    LiveComposite(
        (1672, 941),
        (0, 0), "images/background/scene/repos2.png",
        (0, 0), "images/background/interact/repos/repos2/deco_fete.png",
    ),
)

# Les fichiers de `images/background/scene` peuvent aussi être appelés
# directement par les scripts. Ces déclarations leur donnent le même
# éclairage que les salles dynamiques, sans toucher aux CG ni à l'interface.
image bg_dortoir = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/bg_dortoir.png")
image bg_chambre_iris = DynamicDisplayable(chambre_iris_scene_dynamic)
image bg_salle_de_bain_iris = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/noam_salle_bain.png")
image bg_chambre_sael = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/bg_chambre_sael.png")
image bg_harmonie_assemblee = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/bg_harmonie_assemblee.png")
image bg_harmonie_district_hall = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/bg_harmonie_district_hall.png")
image noam_salle_bain = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/noam_salle_bain.png")

image couloir_cafeteria = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/couloir_cafeteria.png")
image couloir_dortoir = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/couloir_dortoir.png")
image couloir_principal = "couloir_dortoir"
image couloir_infirmerie = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/couloir_infirmerie.png")
image couloir_maintenance = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/couloir_maintenance.png")
image couloir_sas = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/couloir_sas.png")

image archive1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/archive1.png")
image archive2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/archive2.png")
image cafeteria1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/cafeteria1.png")
image cafeteria2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/cafeteria2.png")
image cafeteria3 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/cafeteria3.png")
image canon1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/canon1.png")
image canon2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/canon2.png")
image chambre1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/chambre1.png")
image chambre2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/chambre2.png")
image chambre2_1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/chambre2_1.png")
image chambre3 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/chambre3.png")
image chambre3_1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/chambre3_1.png")
image conclave1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/conclave1.png")
image conclave2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/conclave2.png")
image conclave3 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/conclave3.png")
image gymnase1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/gymnase1.png")
image gymnase2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/gymnase2.png")
image infirmerie1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/infirmerie1.png")
image infirmerie2 = DynamicDisplayable(infirmerie2_scene_dynamic)
image infirmerie3 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/infirmerie3.png")
image maintenance1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/maintenance1.png")
image maintenance2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/maintenance2.png")
image observation1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/observation1.png")
image observation2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/observation2.png")
image repos1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/repos1.png")
image repos2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/repos2.png")
image sas1 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/sas1.png")
image sas2 = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/sas2.png")
image stockage = DynamicDisplayable(automatic_scene_image_dynamic, "images/background/scene/stockage.png")

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
            # Déjà intégré au décor dynamique : visible aussi pendant les dialogues.
            null
        elif target_label and renpy.has_label(target_label):
            imagebutton:
                # Le visuel au repos appartient désormais au fond composé.
                idle room_interaction_null()
                hover room_interaction_hover_with_overlays(path, room_name)
                focus_mask room_interaction_layer(path, room_name, "art")
                xpos 0
                ypos 0
                action Jump(target_label)
