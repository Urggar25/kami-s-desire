# Ambient corridor encounters. No dialogue, no story state or character staging changes.
default persistent.kd_corridor_ambient_enabled = True
default kd_corridor_last_actor = None
default kd_corridor_visit_pending = True

init python:
    KD_CORRIDOR_AMBIENT_CHANCE = .30

    # Conservative initial rollout: before the later branching crises.
    # Each entry: actor, expression, exit animation.
    KD_CORRIDOR_AMBIENT_CAST = {
        "cafeteria": (("tomas","sourire","greet"),("mara","neutre","stride"),("elen","joie","greet"),("elias","inquiet","rush"),("lysa","blase","linger")),
        "dortoir": (("julian","neutre","stride"),("mara","neutre","stride"),("lysa","neutre","linger"),("tomas","sourire","greet"),("elen","joie","greet")),
        "infirmerie": (("iris","reflechit","linger"),("sael","neutre","recede"),("ryn","neutre","stride"),("elias","inquiet","rush")),
        "maintenance": (("kael","reflechit","recede"),("nyra","reflechit","stride"),("elias","neutre","rush")),
        "sas": (("kael","calme","recede"),("nyra","neutre","stride"),("ryn","neutre","stride")),
    }

    # Exclude entire corridor when it has a scripted optional encounter,
    # including actors mentioned in the encounter but not shown by its button.
    KD_CORRIDOR_SCRIPTED = {
        "_4_0_ROUTE_CAFETERIA": ("cafeteria",),
        "_4_0_ROUTE_CHAMBRE_SOIR": ("cafeteria",),
        "FIRST_CONCLAVE_ELEN_INTERACT": ("dortoir",),
        "_2_ROUTE_CAFETERIA": ("cafeteria",),
        "_3_ROUTE_CAFETERIA": ("cafeteria",),
        "_2_ROUTE_OBSERVATION": ("dortoir","infirmerie"),
        "_2_ROUTE_GYMNASE": ("dortoir","infirmerie"),
        "_2_ROUTE_CAFETERIA_SOIR": ("cafeteria",),
    }

    def kd_corridor_roll(corridor):
        if not persistent.kd_corridor_ambient_enabled or renpy.is_skipping():
            return None
        if getattr(store, "current_day", 0) not in range(1,7):
            return None
        if str(getattr(store, "current_period", "")).lower() == "nuit":
            return None
        route = getattr(store,"current_scene_active",None)
        if corridor in KD_CORRIDOR_SCRIPTED.get(route, ()):
            return None
        if route is not None and route not in KD_CORRIDOR_SCRIPTED:
            return None
        if renpy.random.random() >= KD_CORRIDOR_AMBIENT_CHANCE:
            return None
        candidates = [v for v in KD_CORRIDOR_AMBIENT_CAST.get(corridor,())
                      if v[0] != store.kd_corridor_last_actor and renpy.has_image(v[0]+" "+v[1])]
        if not candidates:
            return None
        actor, expr, motion = renpy.random.choice(candidates)
        store.kd_corridor_last_actor = actor
        # Pixel positions with centered sprite anchor; ends beyond screen.
        side = renpy.random.choice((-1,1))
        return (actor,expr,motion,side)

# Two independent transforms: horizontal trajectory and vertical step rhythm.
# Explicitly finite, never loop after the actor has left.
transform kd_corridor_stride(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos 0.50
    ypos 1.0
    zoom .84
    alpha 1.0
    pause .18
    easein .28 xpos (0.50 + side*.06)
    linear 1.24 xpos (0.50 + side*.82)
    alpha 0.0

transform kd_corridor_greet(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 - side*.12)
    ypos 1.0
    zoom .86
    alpha 1.0
    ease .16 yoffset 7
    ease .16 yoffset 0
    pause .42
    easein 1.14 xpos (0.50 + side*.82)
    alpha 0.0

transform kd_corridor_rush(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 - side*.18)
    ypos 1.0
    zoom .88
    alpha 1.0
    ease .12 xpos (0.50 - side*.21)
    easein .24 xpos (0.50 + side*.04)
    linear .65 xpos (0.50 + side*.85)
    alpha 0.0

transform kd_corridor_linger(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 - side*.16)
    ypos 1.0
    zoom .80
    alpha 1.0
    pause .70
    easein .30 xpos (0.50 - side*.05)
    linear 1.20 xpos (0.50 + side*.82)
    alpha 0.0

transform kd_corridor_recede(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 - side*.15)
    ypos 1.0
    zoom .82
    alpha 1.0
    pause .25
    ease 1.25 xpos (0.50 + side*.10) ypos .72 zoom .42
    ease .55 xpos (0.50 + side*.22) ypos .64 zoom .31 alpha 0.0

transform kd_corridor_steps(delay=.18, amplitude=5, pace=.14, count=5):
    subpixel True
    yoffset 0
    pause delay
    block:
        ease pace yoffset (-amplitude)
        ease pace yoffset 0
        repeat count

screen kd_corridor_ambient_actor(encounter):
    $ actor, expr, motion, side = encounter
    $ portrait = character_image(actor,expr)
    if motion == "greet":
        add portrait at kd_corridor_steps(.74,4,.14,4), kd_corridor_greet(side)
    elif motion == "rush":
        add portrait at kd_corridor_steps(.12,10,.09,5), kd_corridor_rush(side)
    elif motion == "linger":
        add portrait at kd_corridor_steps(.70,4,.15,5), kd_corridor_linger(side)
    elif motion == "recede":
        add portrait at kd_corridor_steps(.25,3,.16,5), kd_corridor_recede(side)
    else:
        add portrait at kd_corridor_steps(.18,5,.14,5), kd_corridor_stride(side)
