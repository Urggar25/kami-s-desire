# ============================================================
# script.rpy — bgcam + autofocus cinéma (FIXED)
# - Zoom/pan décor + sprites (layers bgcam+master)
# - Focus locuteur (zoom sprite + zorder)
# - Autres persos dim (alpha)
# - Flou léger du BG uniquement (bgcam)
# - Reset GARANTI sur narrateur
# ============================================================

# ------------------------------------------------------------
# PARAMÈTRES CENTRAUX DU ZOOM CINÉMA
# Ces valeurs sont réévaluées à CHAQUE lancement et à CHAQUE reload (Shift+R)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Layers
# ------------------------------------------------------------
init -2 python:
    config.layers = [ "bgcam", "master", "lighting", "transient", "screens", "overlay" ]
    CINEMA_ZOOM_BG = 2.25
    CINEMA_CAM_Y = 0.41
    CINEMA_SPRITE_ZOOM = 1.0
    CINEMA_SPRITE_YPUSH = -80

define config.say_attribute_transition = None
define config.say_attribute_transition_layer = "master"

# ------------------------------------------------------------
# Etat global
# ------------------------------------------------------------
default cam_x_cur = 0.5
default cam_y_cur = 0.5
default cam_z_cur = 1.0
default bg_cam_x_cur = 0.5
default bg_cam_y_cur = 0.5
default bg_cam_z_cur = 1.0

default minor_choice_noam_expression = "reflexion"
default char_pos = {}         # tag -> xalign
default char_state = {}       # tag -> dict(expr,x,y,layer,zorder)
default group_members = []    # tags visibles via showGroup

default current_bg_name = None
default bg_is_blurred = False
default current_day = 0

default _last_autofocus_tag = None
default character_speaking_until = {}

default cam_runtime_dx0 = 0.0
default cam_runtime_dy0 = 0.0
default cam_runtime_z0 = 1.0
default cam_runtime_dx1 = 0.0
default cam_runtime_dy1 = 0.0
default cam_runtime_z1 = 1.0
default cam_runtime_duration = 0.6
default cam_runtime_speaker = False
default _cinema_manual_override = False
default _focus_locked = False
default _focus_last_params = None
default _cinema_last_scene_signature = None
default arguments = []
# Arguments débloqués de façon GLOBALE : conservés entre les sauvegardes et
# même après avoir recommencé une nouvelle partie.
default persistent.unlocked_arguments = []
default persistent.unlocked_vote_argument_ids = []
default persistent.unlocked_dossier_args = []
default persistent.pegi18_prompt_done = False
default persistent.known_character_names = []

default day_id = 0


# ------------------------------------------------------------
# Transforms génériques
# ------------------------------------------------------------
transform adaptive_fullscreen:
    fit "cover"
    xalign 0.5
    yalign 0.5

init -2:
    transform cover_screen:
        fit "cover"
        xalign 0.5
        yalign 0.5


# ------------------------------------------------------------
# Caméra runtime (appliquée aux layers)
# ------------------------------------------------------------
# Camera interactive : après le travelling (0,6 s), le curseur peut explorer
# librement le plan large, ou un rayon réduit autour du locuteur.
init python:
    def cinema_mouse_follow(trans, st, at):
        """Callback global sérialisable par Ren'Py (aucune closure locale)."""
        # Arguments passés via des propriétés ATL standard, sauvegardables.
        dx0 = store.cam_runtime_dx0
        dy0 = store.cam_runtime_dy0
        z0 = store.cam_runtime_z0
        dx1 = store.cam_runtime_dx1
        dy1 = store.cam_runtime_dy1
        z1 = store.cam_runtime_z1
        duration = store.cam_runtime_duration
        speaker_mode = store.cam_runtime_speaker
        w = float(config.screen_width)
        h = float(config.screen_height)
        progress = min(1.0, max(0.0, st / max(0.001, duration)))
        smooth = progress * progress * (3.0 - 2.0 * progress)
        zoom = z0 + (z1 - z0) * smooth
        trans.zoom = zoom

        base_x = dx0 + (dx1 - dx0) * smooth
        base_y = dy0 + (dy1 - dy0) * smooth
        edge_x = max(0.0, w * (zoom - 1.0) / 2.0)
        edge_y = max(0.0, h * (zoom - 1.0) / 2.0)
        mx, my = renpy.get_mouse_pos()
        mouse_x = (0.5 - max(0.0, min(1.0, float(mx) / w))) * 2.0 * edge_x
        mouse_y = (0.5 - max(0.0, min(1.0, float(my) / h))) * 2.0 * edge_y
        # Priorité au locuteur : déplacement de souris autour du focus,
        # plutôt qu'une interpolation moitié-moitié qui le décale du centre.
        # Le clamp final garde l'image dans ses bords, même aux extrémités.
        # Pensées/narration : 100 % du déplacement autorisé par le zoom.
        # Aucun rayon artificiel autour du point de focus.
        amount = 0.24 if speaker_mode else 1.0
        target_x = max(-edge_x, min(edge_x, base_x * (1.0 - amount) + mouse_x * amount))
        target_y = max(-edge_y, min(edge_y, base_y * (1.0 - amount) + mouse_y * amount))
        trans.xoffset += (target_x - trans.xoffset) * 0.23
        trans.yoffset += (target_y - trans.yoffset) * 0.23
        return 0.016

transform cam_runtime(dx0=0, dy0=0, z0=1.0, dx1=0, dy1=0, z1=1.0, t=0.6, speaker_mode=False):
    xalign 0.5
    yalign 0.5
    zoom z0
    xoffset dx0
    yoffset dy0
    function cinema_mouse_follow

init python:
    CHARACTER_REAL_NAMES = {
        "noam": "Noam", "lysa": "Lysa", "elias": "Elias",
        "mara": "Mara", "julian": "Julian", "iris": "Iris",
        "tomas": "Tomas", "elen": "Elen", "kael": "Kael",
        "nyra": "Nyra", "ryn": "Ryn", "sael": "Sael",
        "anya": "Anya", "kami": "KAMI", "goumi": "Goumi",
    }

    def character_names_ensure_state():
        known_names = getattr(persistent, "known_character_names", None)
        if not isinstance(known_names, list):
            known_names = []
            persistent.known_character_names = known_names
        return known_names

    def is_character_name_known(character_id):
        return character_id in character_names_ensure_state()

    def character_display_name(character_id):
        if is_character_name_known(character_id):
            return CHARACTER_REAL_NAMES.get(character_id, "???")
        return "???"

    def unlock_character_name(character_id, save=True):
        if character_id not in CHARACTER_REAL_NAMES:
            return False

        known_names = character_names_ensure_state()
        if character_id in known_names:
            return False

        known_names.append(character_id)
        if save:
            renpy.save_persistent()
        return True

    def migrate_known_character_names_from_save():
        """Récupère les découvertes déjà faites dans les anciennes sauvegardes."""
        discovered_rooms = {
            "decouverte_salle_archive": ("tomas",),
            "decouverte_cafeteria": ("elen", "goumi"),
            "decouverte_salle_canon": ("ryn",),
            "decouverte_gymnase": ("elias",),
            "decouverte_infirmerie": ("sael",),
            "decouverte_salle_maintenance": ("kael",),
            "decouverte_salle_observation": ("lysa",),
            "decouverte_salle_repos": ("iris", "julian"),
            "decouverte_sas": ("mara",),
            "decouverte_stockage": ("nyra",),
        }

        changed = False
        for flag_name, character_ids in discovered_rooms.items():
            if getattr(store, flag_name, False):
                for character_id in character_ids:
                    changed = unlock_character_name(character_id, save=False) or changed

        # À partir du jour 1, ces trois identités ont déjà été révélées
        # explicitement pendant le prologue.
        if getattr(store, "day_id", 0) >= 1:
            for character_id in ("noam", "lysa", "kami"):
                changed = unlock_character_name(character_id, save=False) or changed

        if changed:
            renpy.save_persistent()

    import re
    import time

    def dialogue_word_count(text):
        return len(re.findall(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’_-][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*", text or ""))

    def start_character_dialogue(tag, text):
        if not tag or tag.startswith("__"):
            return
        duration = 0.2 * dialogue_word_count(text)
        if duration <= 0.0:
            return
        store.character_speaking_until[tag] = time.time() + duration

    def is_character_speaking(tag):
        until = store.character_speaking_until.get(tag, 0.0)
        if until <= time.time():
            if tag in store.character_speaking_until:
                store.character_speaking_until.pop(tag, None)
            return False
        return True

    def nsfw_content_locked():
        return True

    def lock_nsfw_content():
        persistent.pegi18 = False
        persistent.pegi18_prompt_done = True
        renpy.save_persistent()

    def day_number(value=None):
        if value is None:
            value = getattr(store, "current_day", 0)
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0

    def fix_stale_return_label(target_label, source_file="game/scenario/1_canon.rpy"):
        """
        Compatibilite sauvegardes: les anciens `call` sans `from` stockaient
        une position anonyme dans 1_canon.rpy. Apres modification du fichier,
        Ren'Py peut ne plus retrouver ce retour.
        """
        if not target_label:
            return
        ctx = renpy.game.context()
        if not ctx.return_stack:
            return
        top = ctx.return_stack[-1]
        if isinstance(top, tuple) and len(top) >= 1 and str(top[0]).replace("\\", "/") == source_file:
            ctx.return_stack[-1] = target_label

    def day1_trace_return_label(path_type, anchor_y=620):
        if path_type == "vertical_up":
            return "_call_day1_trace_urn"
        if path_type == "arc" and anchor_y == 560:
            return "_call_day1_trace_jammer"
        return "_call_day1_trace_wakeup"

    def cam_apply(x1, y1, z1, t=0.6, layers=("bgcam", "master")):
        sw = config.screen_width
        sh = config.screen_height

        for ly in layers:
            if ly == "bgcam":
                x0 = store.bg_cam_x_cur
                y0 = store.bg_cam_y_cur
                z0 = store.bg_cam_z_cur
            else:
                x0 = store.cam_x_cur
                y0 = store.cam_y_cur
                z0 = store.cam_z_cur

            dx0 = int((0.5 - x0) * (sw * (z0 - 1.0)))
            dy0 = int((0.5 - y0) * (sh * (z0 - 1.0)))
            dx1 = int((0.5 - x1) * (sw * (z1 - 1.0)))
            dy1 = int((0.5 - y1) * (sh * (z1 - 1.0)))
            # Snapshot de la position précédente pour débuter la transition
            # depuis l'ancienne vue, même après changement de locuteur.
            mx, my = renpy.get_mouse_pos()
            prev_edge_x = sw * max(0.0, z0 - 1.0) / 2.0
            prev_edge_y = sh * max(0.0, z0 - 1.0) / 2.0
            prev_pointer_x = (0.5 - max(0.0, min(1.0, float(mx) / sw))) * 2.0 * prev_edge_x
            prev_pointer_y = (0.5 - max(0.0, min(1.0, float(my) / sh))) * 2.0 * prev_edge_y
            store._cinema_previous_mode = (prev_pointer_x, prev_pointer_y, z0, z0 >= 1.75, dx0, dy0)
            store.cam_runtime_dx0 = dx0
            store.cam_runtime_dy0 = dy0
            store.cam_runtime_z0 = z0
            store.cam_runtime_dx1 = dx1
            store.cam_runtime_dy1 = dy1
            store.cam_runtime_z1 = z1
            store.cam_runtime_duration = t
            store.cam_runtime_speaker = z1 >= 1.75
            tr = cam_runtime(
                dx0=dx0, dy0=dy0, z0=z0,
                dx1=dx1, dy1=dy1, z1=z1,
                t=t, speaker_mode=(z1 >= 1.75)
            )
            renpy.show_layer_at([], layer=ly)
            renpy.show_layer_at([tr], layer=ly)

            if ly == "bgcam":
                store.bg_cam_x_cur = x1
                store.bg_cam_y_cur = y1
                store.bg_cam_z_cur = z1
            else:
                store.cam_x_cur = x1
                store.cam_y_cur = y1
                store.cam_z_cur = z1

    def cam_current(layer="master"):
        if layer == "bgcam":
            return store.bg_cam_x_cur, store.bg_cam_y_cur, store.bg_cam_z_cur
        return store.cam_x_cur, store.cam_y_cur, store.cam_z_cur

    def cam_restore_current(t=0.0, layers=("bgcam", "master")):
        for layer in layers:
            x, y, z = cam_current(layer)
            cam_apply(x, y, z, t=t, layers=(layer,))


    def cam_move(fx=0.5, fy=0.5, z=1.35, t=0.35, layers=("bgcam", "master")):
        cam_apply(fx, fy, z, t, layers)

    def cam_reset(t=0.6, layers=("bgcam", "master")):
        cam_apply(0.5, 0.5, 1.0, t, layers)


# ------------------------------------------------------------
# Sprites : dim / restore / focus
# ------------------------------------------------------------

transform char_restore:
    alpha 1.0
    zoom 1.0
    yoffset 0

transform char_dim(a=0.35):
    alpha a
    zoom 1.0
    yoffset 0

transform char_focus:
    alpha 1.0
    zoom 1.0
    yoffset 0

# ------------------------------------------------------------
# BG blur — SAFE (Ren'Py 8)
# ------------------------------------------------------------
init python:
    im = renpy.display.im
    ImageReference = renpy.display.image.ImageReference

    def add_argument(name):
        if name not in store.arguments:
            store.arguments.append(name)
        # Persistance globale : l'argument reste débloqué pour toutes les
        # parties futures, y compris après un recommencement complet.
        if persistent.unlocked_arguments is None:
            persistent.unlocked_arguments = []
        if name not in persistent.unlocked_arguments:
            persistent.unlocked_arguments.append(name)
            renpy.save_persistent()

    def restore_unlocked_arguments():
        """Réinjecte dans la sauvegarde courante tous les arguments déjà
        débloqués de façon globale (persistent). À appeler au démarrage et
        avant tout écran d'arguments."""
        if persistent.unlocked_arguments is None:
            persistent.unlocked_arguments = []
        for name in persistent.unlocked_arguments:
            if name not in store.arguments:
                store.arguments.append(name)

        if persistent.unlocked_vote_argument_ids is None:
            persistent.unlocked_vote_argument_ids = []
        if hasattr(store, "j2_vote_arguments"):
            for arg_id in persistent.unlocked_vote_argument_ids:
                if arg_id not in store.j2_vote_arguments:
                    store.j2_vote_arguments.append(arg_id)

        if persistent.unlocked_dossier_args is None:
            persistent.unlocked_dossier_args = []
        if hasattr(store, "dossier_unlocked_args"):
            for arg_id in persistent.unlocked_dossier_args:
                if not store.dossier_unlocked_args.get(arg_id, False):
                    store.dossier_unlocked_args[arg_id] = True

    def bg_disp(name, blurred=False, blur_radius=2.0):
        ref = ImageReference(name)
        if blurred:
            return im.Blur(ref, blur_radius)
        return ref

    def character_image(char_name, expr="neutre"):
        """Return the Ren'Py image declared as ``image <char> <expr>``."""
        return ImageReference("%s %s" % (char_name, expr))

    def bg_show(name, at_list=None, layer="bgcam", blurred=False, blur_radius=2.0):
        if at_list is None:
            at_list = []

        store.current_bg_name = name
        store.bg_is_blurred = blurred

        renpy.scene(layer=layer)
        renpy.show("BG", what=bg_disp(name, blurred, blur_radius), layer=layer, at_list=at_list)

    def bg_set_blur(blurred, blur_radius=2.0, layer="bgcam"):
        if not store.current_bg_name:
            return
        if store.bg_is_blurred == blurred:
            return

        store.bg_is_blurred = blurred
        renpy.show("BG", what=bg_disp(store.current_bg_name, blurred, blur_radius), layer=layer)


# ------------------------------------------------------------
# Persos : show / move / restyle (track)
# ------------------------------------------------------------
init python:
    def showP(tag, expr="neutre", x=0.5, y=1.0, layer="master", zorder=0, extra_at=None):
        """
        Affiche un personnage.
        Si le personnage n'était PAS à l'écran, applique une transition d'entrée animée.
        Si déjà présent, simple repositionnement/changement d'expression.
        """
        if extra_at is None:
            extra_at = []

        already_showing = renpy.showing(tag, layer=layer)

        store.char_pos[tag] = x
        store.char_state[tag] = dict(expr=expr, x=x, y=y, layer=layer, zorder=zorder)

        img = f"{tag} {expr}"

        if already_showing:
            # Repositionnement standard
            at_list = [Position(xalign=x, yalign=y)] + extra_at
        else:
            # Entrée animée selon position horizontale
            if x <= 0.35:
                enter = char_enter_left(xp=x)
            elif x >= 0.65:
                enter = char_enter_right(xp=x)
            else:
                enter = char_enter_center(xp=x)
            at_list = [enter] + extra_at

        renpy.show(img, tag=tag, layer=layer, at_list=at_list, zorder=zorder)


    def hideP(tag, layer="master"):
        """
        Cache un personnage avec une transition de sortie animée.
        Remplace les `hide X` dans les scripts pour plus de dynamisme.
        """
        if not renpy.showing(tag, layer=layer):
            store.char_pos.pop(tag, None)
            store.char_state.pop(tag, None)
            return

        x = store.char_pos.get(tag, 0.5)
        expr = store.char_state.get(tag, {}).get("expr", "neutre")
        img = f"{tag} {expr}"

        # Sortie animée selon position
        if x <= 0.35:
            exit_tr = char_exit_left(xp=x)
        elif x >= 0.65:
            exit_tr = char_exit_right(xp=x)
        else:
            exit_tr = char_exit_center(xp=x)

        renpy.show(img, tag=tag, layer=layer, at_list=[exit_tr])
        renpy.pause(0.24, hard=True)
        renpy.hide(tag, layer=layer)

        store.char_pos.pop(tag, None)
        store.char_state.pop(tag, None)


    def moveP(tag, x, y=1.0, t=0.35):
        if tag not in store.char_state:
            store.char_pos[tag] = x
            return

        store.char_pos[tag] = x
        store.char_state[tag]["x"] = x
        store.char_state[tag]["y"] = y

        expr = store.char_state[tag]["expr"]
        img = f"{tag} {expr}"
        renpy.show(img, tag=tag, layer="master",
                  at_list=[Position(xalign=x, yalign=y), MoveTransition(t)])

init python:
    def restyle_char(tag, mode="restore"):
        if tag not in store.char_state:
            return

        st = store.char_state[tag]
        if st.get("mode") == mode:
            return

        st["mode"] = mode

        expr = st.get("expr", "neutre")
        x = st.get("x", 0.5)
        y = st.get("y", 1.0)
        layer = st.get("layer", "master")  # valeur par défaut si clé absente
        base_z = st.get("zorder", 0)

        img = f"{tag} {expr}"
        at_list = [Position(xalign=x, yalign=y)]
        z = base_z

        if mode == "dim":
            at_list.append(char_dim(0.35))
        elif mode == "focus":
            at_list.append(char_focus)
            z = 500
        else:
            at_list.append(char_restore)

        renpy.show(img, tag=tag, layer=layer, at_list=at_list, zorder=z)

init python:
    def cam_x_for_edge_safe_char(tag, zoom=None):
        """Centre autant que possible sans jamais découvrir un bord du décor."""
        x = store.char_pos.get(tag, 0.5)
        z = zoom if zoom is not None else CINEMA_ZOOM_BG
        if z <= 1.0:
            return 0.5

        # Cette cible centrerait exactement le personnage. La borner à 0..1
        # garantit que l'image zoomée couvre encore les deux bords de l'écran.
        # Le point de référence est la position réelle du sprite dans le plan.
        # Le focus doit rester dans l'image zoomée, sans compenser deux fois.
        target = 0.5 + (x - 0.5) * z / max(0.001, (z - 1.0))
        return max(0.0, min(1.0, target))


# ------------------------------------------------------------
# Cinéma : zoom BG + zoom sprite + dim autres + blur BG
# ------------------------------------------------------------
init python:
    def cinematic_reset(t=0.6, cam_layers=("bgcam", "master"), blur_radius=2.0):
        # Reset garanti : cam + blur OFF + restore tous les persos
        bg_set_blur(False, blur_radius, layer="bgcam")
        cam_move(0.5, 0.5, CINEMA_ZOOM_BG * 0.80, t=t, layers=cam_layers)

        for c in list(store.char_state.keys()):
            if renpy.showing(c, layer="master"):
                restyle_char(c, "restore")
        
        store._focus_last_params = dict(tag="__NARRATOR__")

init python:
    def cinematic_focus(tag, t=0.6):
        store._focus_last_params = dict(tag=tag)

        if tag == "__NARRATOR__":
            return

        if not cinema_visible_speaker(tag):
            # Voix hors champ : conserver une caméra légèrement rapprochée.
            cinematic_reset(t=t)
            return

        bg_set_blur(False, 2.5, layer="bgcam")
        safe_tx = cam_x_for_edge_safe_char(tag, CINEMA_ZOOM_BG)
        cam_move(safe_tx, CINEMA_CAM_Y, CINEMA_ZOOM_BG, t, layers=("bgcam", "master"))

        for c in list(store.char_state.keys()):
            if not renpy.showing(c, layer="master"):
                continue
            if c == tag:
                attrs = renpy.get_attributes(c, layer="master")
                if attrs:
                    real_expr = attrs[0]
                    if real_expr != store.char_state[c].get("expr"):
                        store.char_state[c]["expr"] = real_expr
                        store.char_state[c]["mode"] = None
                restyle_char(c, "focus")
            else:
                restyle_char(c, "dim")

init python:
    def cinematic_hold(t=0.0):
        """
        Ré-applique l'état visuel courant (cam + focus/dim + blur) instantanément.
        Empêche le "drop" entre deux lignes du même locuteur.
        """
        p = store._focus_last_params
        if not p:
            return

        tag = p.get("tag")
        if not tag or tag in ("__NARRATOR__", "__NO_AUTOFOCUS__"):
            return

        # On ré-applique strictement ce qui est en cours
        cinematic_focus(tag, t=t)


# ------------------------------------------------------------
# Callback : ne fait rien si même locuteur (anti reset)
# ------------------------------------------------------------
init python:
    if not hasattr(store, "_autofocus_cb_lock"):
        store._autofocus_cb_lock = False

init python:
    def scene_has_no_character_sprites():
        """Exclusion uniquement si une CG est ACTUELLEMENT affichée.

        current_bg_name peut conserver l'ancienne salle après un 'scene' direct :
        ne jamais s'en servir comme preuve d'une CG active.
        """
        for layer in ("bgcam", "master"):
            for tag in renpy.get_showing_tags(layer=layer):
                if tag.lower().startswith(("bg_cg", "bg_diffusion")):
                    return True
        # bg_show affiche le fond sous le tag BG ; la référence réelle est
        # suivie par current_bg_name. La vérification du tag est nécessaire.
        if any("BG" in renpy.get_showing_tags(layer=layer) for layer in ("bgcam", "master")):
            return bool((store.current_bg_name or "").lower().startswith(("bg_cg", "bg_diffusion")))
        return False

    def cinema_scene_signature():
        """Identifie la scène réellement visible, indépendamment du dernier locuteur."""
        visible = []
        for layer in ("bgcam", "master"):
            for tag in renpy.get_showing_tags(layer=layer):
                lower = tag.lower()
                if lower.startswith(("bg_", "scene_")) or tag == "BG":
                    visible.append((layer, tag))
        if any(tag == "BG" for _, tag in visible):
            visible.append(("bg_show", store.current_bg_name))
        return tuple(sorted(visible, key=str))

    def cinema_visible_speaker(tag):
        """Répare le suivi si un sprite est affiché sans passer par showP."""
        if tag in store.char_state and renpy.showing(tag, layer="master"):
            return True
        if not renpy.showing(tag, layer="master"):
            return False
        x = store.char_pos.get(tag, 0.5)
        store.char_state[tag] = dict(expr="neutre", x=x, y=1.0, layer="master", zorder=0)
        return True


init python:
    def make_autofocus_cb(tag, doublage_tag=None):
        def _cb(event, interact=True, **kwargs):
            if event != "begin":
                return
            manual_camera = getattr(store, "_cinema_manual_override", False)

            dialogue_text = kwargs.get("what", "")
            # Memorise l'expression de Noam pour les choix mineurs, meme si
            # son sprite est ensuite masque avant l'ouverture du menu.
            if tag == "noam":
                attrs = renpy.get_attributes("noam", layer="master") or ()
                expr = next((a for a in attrs if a in NOAM_EXPRESSIONS), None)
                if not expr:
                    state = getattr(store, "char_state", {}).get("noam", {})
                    expr = state.get("expr") if isinstance(state, dict) else None
                if expr in NOAM_EXPRESSIONS:
                    store.minor_choice_noam_expression = expr
            start_character_dialogue(tag, dialogue_text)
            play_dialogue_doublage(doublage_tag or tag, dialogue_text)

            if manual_camera:
                return  # Son, bouche et clignement restent opérationnels.

            scene_signature = cinema_scene_signature()
            scene_changed = scene_signature != store._cinema_last_scene_signature
            store._cinema_last_scene_signature = scene_signature

            if scene_has_no_character_sprites():
                if scene_changed or store._focus_last_params != dict(tag="__NO_AUTOFOCUS__"):
                    cam_reset(t=0.6)
                    store._focus_last_params = dict(tag="__NO_AUTOFOCUS__")
                return

            if tag == "__NARRATOR__":
                last_tag = store._focus_last_params.get("tag") if store._focus_last_params else None
                # Ne pas sauter le cadrage après un changement de pièce,
                # même si les deux répliques consécutives sont des pensées.
                wanted_zoom = CINEMA_ZOOM_BG * 0.80
                wrong_camera = abs(store.cam_z_cur - wanted_zoom) > 0.001 or abs(store.bg_cam_z_cur - wanted_zoom) > 0.001
                if not scene_changed and last_tag == "__NARRATOR__" and not wrong_camera:
                    return
                cinematic_reset(t=0.6)
                return

            last_tag = store._focus_last_params.get("tag") if store._focus_last_params else None
            if last_tag == tag and not scene_changed:
                # Même locuteur : ne pas recréer le transform, car cela
                # relancerait le travelling et réinitialiserait le curseur.
                # Ses animations de bouche et son audio ont déjà été lancés.
                return

            cinematic_focus(tag, t=0.6)

        return _cb

# ------------------------------------------------------------
# Characters
# IMPORTANT: Les lignes "sans nom" utilisent narrator => callback reset
# ------------------------------------------------------------
define narrator = Character(
    None,
    what_prefix="", what_suffix="",
    callback=make_autofocus_cb("__NARRATOR__")
)

define n = Character(
    None,
    what_prefix="“", what_suffix="”",
    callback=make_autofocus_cb("__NARRATOR__")
)

define think = Character(
    None,
    what_color="#4AA3FF",
    italic=True,
    callback=make_autofocus_cb("__NARRATOR__")
)

define voix_off = Character(
    "Voix artificielle",
    what_prefix="“", what_suffix="”",
    callback=make_autofocus_cb("__NARRATOR__")
)

# Persos
define noam = DynamicCharacter("character_display_name('noam')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("noam"), image="noam")
define dg_noam = DynamicCharacter("'Noam ?'", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("dg_noam"), image="dg_noam")
define lysa = DynamicCharacter("character_display_name('lysa')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("lysa"), image="lysa")
define elias = DynamicCharacter("character_display_name('elias')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("elias"), image="elias")
define mara = DynamicCharacter("character_display_name('mara')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("mara"), image="mara")
define julian = DynamicCharacter("character_display_name('julian')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("julian"), image="julian")
define iris = DynamicCharacter("character_display_name('iris')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("iris"), image="iris")
define tomas = DynamicCharacter("character_display_name('tomas')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("tomas"), image="tomas")
define elen = DynamicCharacter("character_display_name('elen')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("elen"), image="elen")
define kael = DynamicCharacter("character_display_name('kael')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("kael"), image="kael")
define nyra = DynamicCharacter("character_display_name('nyra')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("nyra"), image="nyra")
define ryn = DynamicCharacter("character_display_name('ryn')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("ryn"), image="ryn")
define sael = DynamicCharacter("character_display_name('sael')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("sael"), image="sael")
define anya = DynamicCharacter("character_display_name('anya')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("anya"), image="anya")
define anya_inconnue = Character("Inconnue", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("anya"), image="anya")

define med1 = Character("Médiatrice", what_prefix="“", what_suffix="”")
define med2 = Character("Médiateur", what_prefix="“", what_suffix="”")
define cit_a = Character("Citoyenne", what_prefix="“", what_suffix="”")
define cit_b = Character("Citoyen", what_prefix="“", what_suffix="”")
define senior = Character("Médiateur senior", what_prefix="“", what_suffix="”")
define resp = Character("Responsable de séance", what_prefix="“", what_suffix="”")
define voix = Character("Voix du système", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("__NARRATOR__"))
define agent = Character("Agent de sécurité", what_prefix="“", what_suffix="”")
define resp_d = Character("Responsable de District", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("man"), image="man")
define tuto = Character("", what_prefix="(", what_suffix=")", what_color="#008000", callback=make_autofocus_cb("__NARRATOR__"))
define goumi = DynamicCharacter("character_display_name('goumi')", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("goumi"), image="goumi")
define robot = Character("Robot", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("robot"))

define kami = DynamicCharacter(
    "character_display_name('kami')",
    what_prefix="« ", what_suffix=" »",
    who_color="#AFCBFF",
    callback=kami_diffusion_speaker_callback
)

# ---------------------------------------------------------------------------
# Transform
# ---------------------------------------------------------------------------

transform adaptive_fullscreen:
    fit "cover"
    xalign 0.5
    yalign 0.5

transform memory_idle:
    alpha 0.97
    zoom 1.02
    linear 6.0 zoom 1.03 xoffset 1 yoffset -1
    linear 6.0 zoom 1.02 xoffset -1 yoffset 1
    repeat

init -2:
    transform cover_screen:
        fit "cover"
        xalign 0.5
        yalign 0.5

# ------------------------------------------------------------
# START
# ------------------------------------------------------------

label _init_cinema_params:
    $ CINEMA_ZOOM_BG = 2.25          # Zoom modéré sur le locuteur
    $ CINEMA_CAM_Y = 0.41            # Cadrage relevé vers le visage
    $ CINEMA_SPRITE_ZOOM = 1.0       # Évite un double grossissement
    $ CINEMA_SPRITE_YPUSH = -80      # Relevé sprite (négatif = vers le haut)
    return


label splashscreen:
    # La bande-annonce se lance via Start() : on saute le logo d'intro,
    # sinon le joueur subit 11 s de cartons avant le premier plan.
    if persistent.trl_skip_splash:
        $ persistent.trl_skip_splash = False
        return

    scene black
    with Dissolve(0.5)

    scene expression "images/background/cg/bg_initialisation.png" at adaptive_fullscreen
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    scene black
    with Dissolve(1.0)

    scene expression "images/background/cg/bg_studio.png" at adaptive_fullscreen
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    scene black
    with Dissolve(1.0)

    return

label patreon_ending:
    scene black
    with Dissolve(0.5)

    scene expression "images/background/cg/bg_patreon.png" at adaptive_fullscreen
    with Dissolve(1.0)
    $ renpy.pause(6.0, hard=True)
    scene black
    with Dissolve(1.0)

    call screen save

    $ renpy.pause(3.0, hard=True)
    $ renpy.full_restart()

label start:
    call _init_cinema_params from _call__init_cinema_params
    $ lock_nsfw_content()
    $ restore_unlocked_arguments()
    # A roadmap teleport restarts the game with all defaults restored.
    # Consume its destination only after the new store is initialized.
    $ _roadmap_clean_label = roadmap_restore_clean_jump()
    if _roadmap_clean_label:
        jump expression _roadmap_clean_label
    if roadmap_target_label:
        $ _target = roadmap_target_label
        $ roadmap_target_label = None
        jump expression _target
    if story_map_target_label:
        $ _target = story_map_target_label
        $ story_map_target_label = None
        jump expression _target
    jump _0_CANON


# ------------------------------------------------------------
# Rappel usage :
# $ bg_show("bg_cg006", at_list=[adaptive_fullscreen], blurred=False)
# $ showGroup([("noam", "neutre", 0.30), ("lysa", "neutre", 0.70)])
# ------------------------------------------------------------
