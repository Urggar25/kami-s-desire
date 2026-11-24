# Ambient corridor encounters. No dialogue, no story state or character staging changes.
default persistent.kd_corridor_ambient_enabled = True
default kd_corridor_last_actor = None
default kd_corridor_visit_pending = True

init python:
    KD_CORRIDOR_AMBIENT_CHANCE = .10

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

# Use a single transform per actor: no competing offsets or exaggerated bobbing.
# Front-facing sprites cannot convincingly walk away into depth.
# Start near an exit, already moving, and leave the frame without fading.
transform kd_corridor_stride(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 + side*.22)
    ypos 1.0
    zoom .84
    alpha 1.0
    linear 1.35 xpos (0.50 + side*1.10)

transform kd_corridor_greet(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 + side*.25)
    ypos 1.0
    zoom .84
    alpha 1.0
    pause .28
    ease .12 yoffset 2
    ease .14 yoffset 0
    easein .22 xpos (0.50 + side*.32)
    linear 1.05 xpos (0.50 + side*1.10)

transform kd_corridor_rush(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 + side*.18)
    ypos 1.0
    zoom .84
    alpha 1.0
    linear .88 xpos (0.50 + side*1.10)

transform kd_corridor_linger(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 + side*.28)
    ypos 1.0
    zoom .84
    alpha 1.0
    pause .52
    easein .26 xpos (0.50 + side*.35)
    linear 1.10 xpos (0.50 + side*1.10)

# Former recede motion: use a quiet lateral exit instead of shrinking
# a forward-facing sprite as if it were walking backwards.
transform kd_corridor_recede(side):
    subpixel True
    anchor (0.5, 1.0)
    xpos (0.50 + side*.32)
    ypos 1.0
    zoom .80
    alpha 1.0
    pause .18
    linear 1.25 xpos (0.50 + side*1.10)

screen kd_corridor_ambient_actor(encounter):
    $ actor, expr, motion, side = encounter
    $ portrait = character_image(actor,expr)
    if motion == "greet":
        add portrait at kd_corridor_greet(side)
    elif motion == "rush":
        add portrait at kd_corridor_rush(side)
    elif motion == "linger":
        add portrait at kd_corridor_linger(side)
    elif motion == "recede":
        add portrait at kd_corridor_recede(side)
    else:
        add portrait at kd_corridor_stride(side)
