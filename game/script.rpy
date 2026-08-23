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
    config.layers = [ "bgcam", "master", "transient", "screens", "overlay" ]
    CINEMA_ZOOM_BG = 1.80
    CINEMA_CAM_Y = 0.41
    CINEMA_SPRITE_ZOOM = 1.60
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

default char_pos = {}         # tag -> xalign
default char_state = {}       # tag -> dict(expr,x,y,layer,zorder)
default group_members = []    # tags visibles via showGroup

default current_bg_name = None
default bg_is_blurred = False
default current_day = 0

default _last_autofocus_tag = None
default character_speaking_until = {}

default _focus_locked = False
default _focus_last_params = None
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
transform cam_runtime(dx0=0, dy0=0, z0=1.0, dx1=0, dy1=0, z1=1.0, t=0.35):
    xalign 0.5
    yalign 0.5

    xoffset dx0
    yoffset dy0
    zoom z0

    ease t xoffset dx1 yoffset dy1 zoom z1


init python:
    CHARACTER_REAL_NAMES = {
        "noam": "Noam", "lysa": "Lysa", "elias": "Elias",
        "mara": "Mara", "julian": "Julian", "iris": "Iris",
        "tomas": "Tomas", "elen": "Elen", "kael": "Kael",
        "nyra": "Nyra", "ryn": "Ryn", "sael": "Sael",
        "kami": "KAMI", "goumi": "Goumi",
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

    def cam_apply(x1, y1, z1, t=0.35, layers=("bgcam", "master")):
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
            tr = cam_runtime(
                dx0=dx0, dy0=dy0, z0=z0,
                dx1=dx1, dy1=dy1, z1=z1,
                t=t
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

    def cam_reset(t=0.35, layers=("bgcam", "master")):
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
            at_list.append(char_dim(0.30))
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
        target = 0.5 + ((x - 0.5) * z / (z - 1.0))
        return max(0.0, min(1.0, target))


# ------------------------------------------------------------
# Cinéma : zoom BG + zoom sprite + dim autres + blur BG
# ------------------------------------------------------------
init python:
    def cinematic_reset(t=0.22, cam_layers=("bgcam", "master"), blur_radius=2.0):
        # Reset garanti : cam + blur OFF + restore tous les persos
        bg_set_blur(False, blur_radius, layer="bgcam")
        cam_reset(t=t, layers=cam_layers)

        for c in list(store.char_state.keys()):
            if renpy.showing(c, layer="master"):
                restyle_char(c, "restore")
        
        store._focus_last_params = None

init python:
    def cinematic_focus(tag, t=0.30):
        store._focus_last_params = dict(tag=tag)

        if tag == "__NARRATOR__":
            return

        if tag not in store.char_state:
            cinematic_reset(t=t)
            return

        bg_set_blur(True, 2.5, layer="bgcam")
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
        special_tokens = ("bg_cg", "bg_diffusion")

        def is_sport_bg(name):
            if not name:
                return False
            low = name.lower()
            return low.startswith("sport") and low[5:].isdigit()

        # Cas où le BG est suivi via bg_show().
        bg_name = store.current_bg_name or ""
        if any(token in bg_name for token in special_tokens) or is_sport_bg(bg_name):
            return True

        # Cas des `scene bg_xxx` affichés directement par le script.
        for layer in ("bgcam", "master"):
            for tag in renpy.get_showing_tags(layer=layer):
                if any(token in tag for token in special_tokens) or is_sport_bg(tag):
                    return True

        return False


init python:
    def make_autofocus_cb(tag, doublage_tag=None):
        def _cb(event, interact=True, **kwargs):
            if event != "begin":
                return

            dialogue_text = kwargs.get("what", "")
            start_character_dialogue(tag, dialogue_text)
            play_dialogue_doublage(doublage_tag or tag, dialogue_text)

            if tag == "__NARRATOR__":
                last_tag = store._focus_last_params.get("tag") if store._focus_last_params else None
                if last_tag == "__NARRATOR__":
                    return
                cinematic_reset(t=0.30)
                store._focus_last_params = dict(tag="__NARRATOR__")
                return

            last_tag = store._focus_last_params.get("tag") if store._focus_last_params else None
            if last_tag == tag:
                return  # Skip parfait

            if scene_has_no_character_sprites():
                if last_tag == "__NO_AUTOFOCUS__":
                    return
                cinematic_reset(t=0.30)
                store._focus_last_params = dict(tag="__NO_AUTOFOCUS__")
                return

            cinematic_focus(tag, t=0.30)

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
    callback=make_autofocus_cb("__NARRATOR__", doublage_tag="kami")
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
    $ CINEMA_ZOOM_BG = 1.80          # Gros plan renforcé sur le locuteur
    $ CINEMA_CAM_Y = 0.41            # Cadrage relevé vers le visage
    $ CINEMA_SPRITE_ZOOM = 1.60      # Zoom du sprite locuteur
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
