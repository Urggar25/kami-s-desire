# Modular TV portraits. All layers share a 600x720 transparent canvas.
# No character or scenario data is randomized during rendering.
default kd_news_cast = ()
default kd_news_layout = "studio"
default kd_news_speaker = None
default kd_news_talking = False
default kd_news_moods = {}
default kd_news_custom = {}

init -1 python:
    from functools import partial as _kd_news_partial

    KD_NEWS_PROFILES = {
        "anchor": (0, 1, 1, 0, False, False),
        "reporter": (1, 2, 2, 1, False, True),
        "commentator": (3, 4, 4, 6, True, False),
        "mother": (0, 5, 1, 3, False, False),
        "father": (1, 2, 0, 5, False, False),
        "shopwoman": (3, 1, 3, 2, True, False),
        "worker": (2, 0, 0, 3, False, False),
        "woman": (1, 3, 5, 7, False, False),
        "vendor": (1, 2, 1, 2, False, False),
        "customer": (2, 5, 0, 4, False, False),
        "teen": (0, 3, 2, 4, False, False),
        "dad": (3, 4, 1, 1, True, False),
        "youngwoman": (3, 1, 5, 7, False, False),
        "olderwoman": (3, 5, 4, 5, True, False),
        "olderman": (1, 4, 4, 3, True, False),
        "girl": (0, 5, 3, 7, False, False),
        "boy": (1, 2, 3, 5, False, False),
        "guard": (2, 0, 2, 6, False, False),
        "anchor2": (2, 2, 0, 0, False, False),
        "reporter2": (3, 3, 1, 6, False, True),
    }

    def kd_news_reset_actors():
        store.kd_news_cast = ()
        store.kd_news_layout = "studio"
        store.kd_news_speaker = None
        store.kd_news_talking = False
        store.kd_news_moods = {}
        store.kd_news_custom = {}

    def kd_news_configure(actor, skin=0, hair=0, hair_color=0, outfit=0, glasses=False, mic=False):
        values = (int(skin), int(hair), int(hair_color), int(outfit), bool(glasses), bool(mic))
        if not (0 <= values[0] < 4 and 0 <= values[1] < 6 and 0 <= values[2] < 6 and 0 <= values[3] < 8):
            raise ValueError("Invalid TV portrait component")
        store.kd_news_custom = dict(store.kd_news_custom, **{actor: values})

    def kd_news_stage(layout, *actors):
        if layout not in ("studio", "interview", "duplex", "debate", "home", "flash", "insert"):
            raise ValueError("Unknown TV layout")
        if not 1 <= len(actors) <= 3 or len(set(actors)) != len(actors):
            raise ValueError("TV layout needs one to three distinct actors")
        for actor in actors:
            if actor not in KD_NEWS_PROFILES and actor not in store.kd_news_custom:
                raise ValueError("Unknown TV actor: " + actor)
        store.kd_news_layout = layout
        store.kd_news_cast = tuple(actors)
        store.kd_news_speaker = None
        store.kd_news_talking = False
        renpy.show_screen("kd_news_actor_stage")

    def kd_news_expression(actor, mood):
        if mood not in ("neutral", "happy", "sad", "angry", "surprised"):
            raise ValueError("Unknown TV expression")
        store.kd_news_moods = dict(store.kd_news_moods, **{actor: mood})

    def kd_news_actor_callback(event, interact=True, actor=None, **kwargs):
        if not interact:
            return
        if event == "begin":
            store.kd_news_speaker = actor
            store.kd_news_talking = True
        elif event in ("slow_done", "end"):
            store.kd_news_talking = False

    def kd_news_portrait(actor, st, at):
        skin, hair, color, outfit, glasses, mic = store.kd_news_custom.get(actor, KD_NEWS_PROFILES.get(actor, KD_NEWS_PROFILES["anchor"]))
        mood = store.kd_news_moods.get(actor, "neutral")
        animate = getattr(persistent, "dialogue_animations", True) and not renpy.is_skipping()
        phase = (st + sum(ord(c) for c in actor) * 0.037) % 4.7
        eyes = "closed" if 4.48 < phase < 4.60 else ("half" if 4.40 < phase < 4.66 else "open")
        mouth = "closed" if mood == "neutral" else mood
        if animate and store.kd_news_speaker == actor and store.kd_news_talking:
            mouth = ("half", "open", "half", "closed")[int(st * 11) % 4]
        if not animate:
            eyes = "open"
        base = "images/kd_news/actors/"
        parts = ["skin_%d" % skin, "outfit_%d" % outfit, "hair_%d_%d" % (hair, color), "brows_" + mood, "eyes_" + eyes, "mouth_" + mouth]
        if glasses:
            parts.append("glasses")
        args = []
        for part in parts:
            args.extend(((0, 0), base + part + ".svg"))
        return Composite((600, 720), *args), (0.07 if animate else None)

    def kd_news_mic_pose():
        # One mic per interview. In an insert, the reporter is off camera
        # when a citizen is shown, so the mic enters from the frame edge.
        cast = store.kd_news_cast
        layout = store.kd_news_layout
        if not cast or layout not in ("interview", "home", "duplex", "insert"):
            return None
        owners = [a for a in cast if store.kd_news_custom.get(a, KD_NEWS_PROFILES.get(a, KD_NEWS_PROFILES["anchor"]))[5]]
        if not owners and layout != "insert":
            return None
        target = store.kd_news_speaker if store.kd_news_speaker in cast else (owners[0] if owners else cast[0])
        slots = (960,) if len(cast) == 1 else ((540, 1380) if len(cast) == 2 else (360, 960, 1560))
        if layout == "insert":
            return (1440, 541, 25)
        owner = owners[0]
        ox = slots[cast.index(owner)]
        tx = slots[cast.index(target)]
        # In a duplex the presenter is in another location.
        if layout == "duplex":
            tx = ox
        side = 1 if tx <= ox else -1
        return (tx + side * 110, 541, -side * 28)

    def kd_news_mic_motion(trans, st, at):
        pose = kd_news_mic_pose()
        if pose is None:
            trans.alpha = 0.0
            return 0.05
        # Keep previous rendered position on the transform, not in save state.
        # Exponential easing with elapsed time prevents jumps on frame skips.
        previous = getattr(trans, "_kd_mic_position", None)
        last = getattr(trans, "_kd_mic_time", st)
        dt = max(0.0, min(0.10, st - last))
        if previous is None or st < last or renpy.is_skipping() or not getattr(persistent, "dialogue_animations", True):
            current = pose
        else:
            factor = 1.0 - pow(2.718281828, -dt * 15.0)
            current = tuple(a + (b - a) * factor for a, b in zip(previous, pose))
        trans._kd_mic_position = current
        trans._kd_mic_time = st
        trans.xpos = int(current[0])
        trans.ypos = int(current[1])
        trans.rotate = current[2]
        trans.alpha = 1.0
        return 0.016

    def kd_news_actor_image(actor):
        return DynamicDisplayable(_kd_news_partial(kd_news_portrait, actor))

    def kd_news_character(actor, name):
        return Character(name, callback=_kd_news_partial(kd_news_actor_callback, actor=actor))

transform kd_news_actor_idle:
    subpixel True
    yoffset 0
    ease 1.8 yoffset -3
    ease 1.8 yoffset 0
    repeat

transform kd_news_actor_arrive:
    alpha 0.0
    xoffset -18
    easeout 0.23 alpha 1.0 xoffset 0

transform kd_news_shared_mic_motion:
    subpixel True
    anchor (0.5, 0.5)
    function kd_news_mic_motion

screen kd_news_actor_stage():
    zorder 3
    modal False
    if kd_news_cast:
        if kd_news_layout != "insert":
            if kd_news_layout in ("studio", "debate", "flash"):
                add "images/kd_news/studio_set.svg"
            elif kd_news_layout == "home":
                add "images/kd_news/home_set.svg"
            elif kd_news_layout != "duplex":
                add "images/kd_news/street_set.svg"
        $ count = len(kd_news_cast)
        $ slots = (960,) if count == 1 else ((540, 1380) if count == 2 else (360, 960, 1560))
        for i, actor in enumerate(kd_news_cast):
            $ px = slots[i]
            $ active = actor == kd_news_speaker
            $ scale = 0.76 if kd_news_layout == "insert" else (0.92 if count < 3 else 0.76)
            if kd_news_layout == "insert":
                $ px = 1530
                add Solid("#091827e8", xysize=(510, 505)) xpos 1275 ypos 103
                add Solid("#6cc4dc", xysize=(510, 3)) xpos 1275 ypos 103
            elif kd_news_layout == "duplex":
                fixed:
                    xpos (px - 420)
                    ypos 108
                    xysize (840, 500)
                    add Solid("#294a63" if i == 0 else "#536c79")
                    add Solid("#6cc4dc" if active else "#54748a", xysize=(840, 3))
                    text (_("PLATEAU") if i == 0 else _("SUR PLACE")) style "kd_news_small" xpos 14 ypos 12
            fixed:
                xpos int(px - 300 * scale)
                ypos int(625 - 720 * scale)
                xysize (int(600 * scale), int(720 * scale))
                at kd_news_actor_arrive
                if getattr(persistent, "dialogue_animations", True):
                    add kd_news_actor_image(actor) zoom scale at kd_news_actor_idle
                else:
                    add kd_news_actor_image(actor) zoom scale
                if active:
                    add Solid("#6cc4dc", xysize=(64, 3)) xalign 0.5 yalign 0.98

        if kd_news_mic_pose() is not None:
            add "images/kd_news/mic_shared.svg" at kd_news_shared_mic_motion id "kd_news_shared_microphone"

label kd_news_actor_demo:
    call kd_news_open(_("LIMEN 24"), _("ESSAI PLATEAU"), _("JOURNAL")) from _call_kd_news_actor_demo_open
    scene expression "images/kd_news/studio_set.svg"
    show screen kd_news_broadcast(_("LIMEN 24"), _("PLATEAU"), _("Essai des personnages modulaires"))
    $ kd_news_stage("studio", "anchor")
    window auto
    kd_tv_anchor "Bienvenue dans notre édition."
    $ kd_news_stage("duplex", "anchor", "reporter")
    kd_tv_reporter "Nous sommes sur place."
    $ kd_news_stage("debate", "anchor", "commentator", "anchor2")
    $ kd_news_expression("commentator", "surprised")
    kd_tv_commentator "Ah bon ?"
    call kd_news_close from _call_kd_news_actor_demo_close
    return

define kd_tv_anchor = kd_news_character("anchor", _("PRÉSENTATRICE"))
define kd_tv_reporter = kd_news_character("reporter", _("JOURNALISTE"))
define kd_tv_commentator = kd_news_character("commentator", _("CHRONIQUEUR"))
define kd_tv_mother = kd_news_character("mother", _("UNE FEMME"))
define kd_tv_father = kd_news_character("father", _("UN HOMME"))
define kd_tv_shopwoman = kd_news_character("shopwoman", _("UNE ANCIENNE COMMERÇANTE"))
define kd_tv_worker = kd_news_character("worker", _("UN HOMME"))
define kd_tv_woman = kd_news_character("woman", _("UNE FEMME"))
define kd_tv_vendor = kd_news_character("vendor", _("UN VENDEUR"))
define kd_tv_customer = kd_news_character("customer", _("UNE CLIENTE"))
define kd_tv_teen = kd_news_character("teen", _("UNE ADOLESCENTE"))
define kd_tv_dad = kd_news_character("dad", _("UN PÈRE"))
define kd_tv_youngwoman = kd_news_character("youngwoman", _("UNE JEUNE FEMME"))
define kd_tv_olderwoman = kd_news_character("olderwoman", _("UNE VIEILLE FEMME"))
define kd_tv_olderman = kd_news_character("olderman", _("UN HOMME"))
define kd_tv_girl = kd_news_character("girl", _("UNE PETITE FILLE"))