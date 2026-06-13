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
    CINEMA_ZOOM_BG = 1.60
    CINEMA_CAM_Y = 0.45
    CINEMA_SPRITE_ZOOM = 1.60
    CINEMA_SPRITE_YPUSH = -80
    CINEMA_FRAME_LEFT = 0.38
    CINEMA_FRAME_RIGHT = 0.62

define config.say_attribute_transition = None
define config.say_attribute_transition_layer = "master"

# ------------------------------------------------------------
# Etat global
# ------------------------------------------------------------
default cam_x_cur = 0.5
default cam_y_cur = 0.5
default cam_z_cur = 1.0

default char_pos = {}         # tag -> xalign
default char_state = {}       # tag -> dict(expr,x,y,layer,zorder)
default group_members = []    # tags visibles via showGroup

default current_bg_name = None
default bg_is_blurred = False
default current_day = 0

default _last_autofocus_tag = None

default _focus_locked = False
default _focus_last_params = None
default arguments = []
default persistent.pegi18_prompt_done = False


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
        x0 = store.cam_x_cur
        y0 = store.cam_y_cur
        z0 = store.cam_z_cur

        sw = config.screen_width
        sh = config.screen_height

        dx0 = int((0.5 - x0) * (sw * (z0 - 1.0)))
        dy0 = int((0.5 - y0) * (sh * (z0 - 1.0)))
        dx1 = int((0.5 - x1) * (sw * (z1 - 1.0)))
        dy1 = int((0.5 - y1) * (sh * (z1 - 1.0)))

        tr = cam_runtime(
            dx0=dx0, dy0=dy0, z0=z0,
            dx1=dx1, dy1=dy1, z1=z1,
            t=t
        )

        for ly in layers:
            renpy.show_layer_at([], layer=ly)
            renpy.show_layer_at([tr], layer=ly)

        store.cam_x_cur = x1
        store.cam_y_cur = y1
        store.cam_z_cur = z1


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

    def bg_disp(name, blurred=False, blur_radius=2.0):
        ref = ImageReference(name)
        if blurred:
            return im.Blur(ref, blur_radius)
        return ref

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

# ------------------------------------------------------------
# Cible caméra en fonction du perso
# ------------------------------------------------------------
init python:
    def focus_target_x_from_char(tag):
        x = store.char_pos.get(tag, 0.5)

        # Si perso est à gauche, on le met sur le tiers gauche ; sinon tiers droit.
        if x < 0.5:
            return CINEMA_FRAME_LEFT
        elif x > 0.5:
            return CINEMA_FRAME_RIGHT
        else:
            return 0.5


init python:
    def cam_x_for_framed_char(tag):
        x = store.char_pos.get(tag, 0.5)

        # Où on veut voir le perso à l'écran
        if x < 0.5:
            target = CINEMA_FRAME_LEFT
        elif x > 0.5:
            target = CINEMA_FRAME_RIGHT
        else:
            target = 0.5

        # Convertit en cible caméra : on décale de la différence
        # cam_x = 0.5 + (x - target)
        # clamp 0..1 pour éviter de sortir du décor
        cam_x = 0.5 + (x - target)
        if cam_x < 0.0: cam_x = 0.0
        if cam_x > 1.0: cam_x = 1.0
        return cam_x


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
        tx = cam_x_for_framed_char(tag)
        cam_move(tx, CINEMA_CAM_Y, CINEMA_ZOOM_BG, t, layers=("bgcam", "master"))

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
    def make_autofocus_cb(tag):
        def _cb(event, interact=True, **kwargs):
            if event != "begin":
                return

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
define noam = Character("Noam", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("noam"), image="noam")
define lysa = Character("Lysa", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("lysa"), image="lysa")
define elias = Character("Elias", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("elias"), image="elias")
define mara = Character("Mara", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("mara"), image="mara")
define julian = Character("Julian", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("julian"), image="julian")
define iris = Character("Iris", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("iris"), image="iris")
define tomas = Character("Tomas", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("tomas"), image="tomas")
define elen = Character("Elen", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("elen"), image="elen")
define kael = Character("Kael", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("kael"), image="kael")
define nyra = Character("Nyra", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("nyra"), image="nyra")
define ryn = Character("Ryn", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("ryn"), image="ryn")
define sael = Character("Sael", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("sael"), image="sael")

define resp_d = Character("Responsable de District", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("__NARRATOR__"))
define goumi = Character("Goumi", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("goumi"), image="goumi")
define robot = Character("Robot", what_prefix="“", what_suffix="”", callback=make_autofocus_cb("robot"))

define kami = Character(
    "KAMI",
    what_prefix="« ", what_suffix=" »",
    who_color="#AFCBFF",
    callback=make_autofocus_cb("__NARRATOR__")
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
    $ CINEMA_ZOOM_BG = 1.60          # Zoom du fond
    $ CINEMA_CAM_Y = 0.45            # Hauteur caméra (0.5 = centre, 0.70 = visage haut)
    $ CINEMA_SPRITE_ZOOM = 1.60      # Zoom du sprite locuteur
    $ CINEMA_SPRITE_YPUSH = -80      # Relevé sprite (négatif = vers le haut)
    $ CINEMA_FRAME_LEFT = 0.38
    $ CINEMA_FRAME_RIGHT = 0.62
    return


label splashscreen:
    scene black
    with Dissolve(0.5)

    scene expression "images/background/bg_initialisation.png" at adaptive_fullscreen
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    scene black
    with Dissolve(1.0)

    scene expression "images/background/bg_studio.png" at adaptive_fullscreen
    with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    scene black
    with Dissolve(1.0)

    return

label patreon_ending:
    scene black
    with Dissolve(0.5)

    scene expression "images/background/bg_patreon.png" at adaptive_fullscreen
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
# $ showP("noam", "neutre", 0.30)
# $ showP("lysa", "neutre", 0.70)
# ------------------------------------------------------------
