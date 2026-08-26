# Mini-jeu du jour 7 — fouille frénétique du bureau.
# Le joueur choisit chaque objet puis maintient le clic pour suivre son tracé.

default fb_removed = []
default fb_active = None
default fb_phase = "pick"
default fb_path = []
default fb_path_length = 1.0
default fb_progress = 0.0
default fb_pressed = False
default fb_mouse_x = 960
default fb_mouse_y = 540
default fb_stray = False
default fb_stray_ticks = 0
default fb_feedback = "Clique sur un point lumineux, puis suis le tracé en maintenant le clic."
default fb_phrase = ""
default fb_phrase_time = 0.0
default fb_flight_time = 0.0

init -2 python:
    import math

    FB_SHEET = "images/background/interact/animation/fouille_bureau/planche_item.png"
    FB_DESK = "images/background/interact/animation/fouille_bureau/bureau.png"

    # Zone sûre des tracés : sous le bandeau et au-dessus des dialogues/consignes.
    FB_QTE_LEFT = 120
    FB_QTE_RIGHT = 1800
    FB_QTE_TOP = 205
    FB_QTE_BOTTOM = 825

    # Les centres suivent les deux rangées en perspective du plateau. Les objets
    # hauts sont remontés pour que leur base — et non leur centre — repose dessus.
    FB_ITEMS = [
        {"id": "ecran", "name": "Écran", "crop": (42, 220, 268, 242), "x": 470, "y": 330, "zoom": .58, "point_y": -4, "bend": -95, "end": (-205, -105), "fly": (-700, -500, -38)},
        {"id": "lampe", "name": "Lampe", "crop": (350, 88, 272, 364), "x": 650, "y": 290, "zoom": .48, "point_y": -18, "bend": 90, "end": (-175, -75), "fly": (-720, -610, -75)},
        {"id": "tablette", "name": "Tablette", "crop": (639, 255, 316, 188), "x": 860, "y": 285, "zoom": .56, "point_y": 0, "bend": -90, "end": (-70, -100), "fly": (-310, -690, -110)},
        {"id": "carnet", "name": "Carnet", "crop": (980, 260, 271, 184), "x": 1080, "y": 250, "zoom": .54, "point_y": 0, "bend": 95, "end": (70, -85), "fly": (350, -690, 85)},
        {"id": "stylo", "name": "Stylo", "crop": (1297, 282, 182, 122), "x": 1285, "y": 220, "zoom": .66, "point_y": 0, "bend": -75, "end": (210, -70), "fly": (720, -520, 155)},
        {"id": "tasse", "name": "Tasse", "crop": (67, 592, 201, 205), "x": 570, "y": 420, "zoom": .48, "point_y": -2, "bend": 85, "end": (-230, -65), "fly": (-760, -360, -125)},
        {"id": "hologramme", "name": "Projecteur", "crop": (352, 569, 178, 242), "x": 760, "y": 385, "zoom": .46, "point_y": -12, "bend": -85, "end": (-145, -135), "fly": (-670, -500, 70)},
        {"id": "casque", "name": "Casque", "crop": (619, 586, 248, 210), "x": 970, "y": 350, "zoom": .48, "point_y": 0, "bend": 85, "end": (15, -160), "fly": (90, -690, 145)},
        {"id": "pot", "name": "Pot à crayons", "crop": (969, 547, 179, 264), "x": 1200, "y": 290, "zoom": .43, "point_y": -10, "bend": -80, "end": (145, -125), "fly": (650, -500, -95)},
        {"id": "plante", "name": "Plante", "crop": (1246, 525, 233, 290), "x": 1420, "y": 245, "zoom": .41, "point_y": -8, "bend": 85, "end": (215, -75), "fly": (760, -350, 120)},
    ]
    FB_ITEM_BY_ID = dict((item["id"], item) for item in FB_ITEMS)
    FB_PHRASES = [
        "Non, pas là...",
        "Rien dessous.",
        "Pas ici non plus...",
        "Allez, dégage.",
        "Toujours rien.",
        "Non... où est-ce que je l'ai mis ?",
        "Pas ça.",
        "Dégage, toi aussi.",
        "Rien. Évidemment.",
        "Le dernier... allez.",
    ]

    def fb_dist(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** .5

    def fb_dist_to_segment(point, start, end):
        ax, ay = start
        bx, by = end
        px, py = point
        dx = bx - ax
        dy = by - ay
        if dx == 0 and dy == 0:
            return fb_dist(point, start), 0.0
        ratio = ((px - ax) * dx + (py - ay) * dy) / float(dx * dx + dy * dy)
        ratio = max(0.0, min(1.0, ratio))
        nearest = (ax + ratio * dx, ay + ratio * dy)
        return fb_dist(point, nearest), ratio

    def fb_total_length(points):
        return max(1.0, sum(fb_dist(points[index - 1], points[index]) for index in range(1, len(points))))

    def fb_closest_progress(points, point):
        best_distance = 99999.0
        best_length = 0.0
        walked = 0.0
        for index in range(1, len(points)):
            segment = fb_dist(points[index - 1], points[index])
            distance, ratio = fb_dist_to_segment(point, points[index - 1], points[index])
            if distance < best_distance:
                best_distance = distance
                best_length = walked + segment * ratio
            walked += segment
        return best_distance, best_length

    def fb_make_path(item):
        start_x = item["x"]
        start_y = item["y"] + item.get("point_y", 0)
        end_x = max(FB_QTE_LEFT, min(FB_QTE_RIGHT, start_x + item["end"][0]))
        end_y = max(FB_QTE_TOP, min(FB_QTE_BOTTOM, start_y + item["end"][1]))
        control_x = (start_x + end_x) * .5 + item["bend"]
        control_x = max(FB_QTE_LEFT, min(FB_QTE_RIGHT, control_x))
        control_y = max(FB_QTE_TOP, min(FB_QTE_BOTTOM, min(start_y, end_y) - 70))
        points = []
        for index in range(31):
            t = index / 30.0
            inv = 1.0 - t
            x = inv * inv * start_x + 2.0 * inv * t * control_x + t * t * end_x
            y = inv * inv * start_y + 2.0 * inv * t * control_y + t * t * end_y
            points.append((
                int(max(FB_QTE_LEFT, min(FB_QTE_RIGHT, x))),
                int(max(FB_QTE_TOP, min(FB_QTE_BOTTOM, y))),
            ))
        return points

    def fb_reset():
        store.fb_removed = []
        store.fb_active = None
        store.fb_phase = "pick"
        store.fb_path = []
        store.fb_path_length = 1.0
        store.fb_progress = 0.0
        store.fb_pressed = False
        store.fb_stray = False
        store.fb_stray_ticks = 0
        store.fb_feedback = "Clique sur un point lumineux, puis suis le tracé en maintenant le clic."
        store.fb_phrase = ""
        store.fb_phrase_time = 0.0
        store.fb_flight_time = 0.0

    def fb_select(item_id):
        if store.fb_phase != "pick" or item_id in store.fb_removed:
            return
        item = FB_ITEM_BY_ID[item_id]
        store.fb_active = item_id
        store.fb_phase = "trace"
        store.fb_path = fb_make_path(item)
        store.fb_path_length = fb_total_length(store.fb_path)
        store.fb_progress = 0.0
        store.fb_pressed = False
        store.fb_stray = False
        store.fb_stray_ticks = 0
        store.fb_feedback = "Maintiens le clic sur le point, puis suis la ligne jusqu'au bout."
        renpy.restart_interaction()

    def fb_press():
        if store.fb_phase != "trace" or not store.fb_path:
            return
        position = renpy.get_mouse_pos()
        store.fb_mouse_x, store.fb_mouse_y = position
        if fb_dist(position, store.fb_path[0]) <= 58:
            store.fb_pressed = True
            store.fb_feedback = "Ne relâche pas."
        else:
            store.fb_feedback = "Commence sur le point lumineux."

    def fb_release():
        if store.fb_phase != "trace":
            return
        if store.fb_pressed and store.fb_progress < .97:
            store.fb_progress = 0.0
            store.fb_stray_ticks = 0
            store.fb_feedback = "Trop tôt. Reprends depuis le point lumineux."
        store.fb_pressed = False
        store.fb_stray = False

    def fb_cancel_trace():
        if store.fb_phase != "trace":
            return
        store.fb_active = None
        store.fb_phase = "pick"
        store.fb_path = []
        store.fb_progress = 0.0
        store.fb_pressed = False
        store.fb_feedback = "Choisis un autre objet."
        renpy.restart_interaction()

    def fb_tick():
        if store.fb_phrase_time > 0.0:
            store.fb_phrase_time = max(0.0, store.fb_phrase_time - .03)
            if store.fb_phrase_time == 0.0:
                store.fb_phrase = ""

        if store.fb_phase == "flying":
            store.fb_flight_time += .03
            if store.fb_flight_time >= .67:
                removed = list(store.fb_removed)
                if store.fb_active not in removed:
                    removed.append(store.fb_active)
                store.fb_removed = removed
                store.fb_active = None
                store.fb_phase = "pick"
                store.fb_path = []
                store.fb_progress = 0.0
                store.fb_flight_time = 0.0
                if len(removed) < len(FB_ITEMS):
                    store.fb_feedback = "Encore %d objet%s à dégager." % (len(FB_ITEMS) - len(removed), "" if len(FB_ITEMS) - len(removed) == 1 else "s")
            return

        if store.fb_phase != "trace" or not store.fb_pressed:
            return

        position = renpy.get_mouse_pos()
        store.fb_mouse_x, store.fb_mouse_y = position
        distance, length_along = fb_closest_progress(store.fb_path, position)
        new_progress = length_along / store.fb_path_length
        if distance <= 62 and new_progress + .04 >= store.fb_progress:
            store.fb_progress = max(store.fb_progress, min(1.0, new_progress))
            store.fb_stray = False
            store.fb_stray_ticks = max(0, store.fb_stray_ticks - 1)
        else:
            store.fb_stray = True
            store.fb_stray_ticks += 1
            if store.fb_stray_ticks >= 12:
                store.fb_progress = 0.0
                store.fb_pressed = False
                store.fb_stray_ticks = 0
                store.fb_feedback = "Tu as quitté le tracé. Recommence depuis le point."

        if store.fb_progress >= .97:
            phrase_index = len(store.fb_removed) % len(FB_PHRASES)
            store.fb_phrase = FB_PHRASES[phrase_index]
            store.fb_phrase_time = 1.65
            store.fb_phase = "flying"
            store.fb_pressed = False
            store.fb_flight_time = 0.0
            store.fb_feedback = ""
            if renpy.loadable("audio/trailer/trl_swoosh.wav"):
                renpy.play("audio/trailer/trl_swoosh.wav", channel="sound")

    class FouilleBureauTrace(renpy.Displayable):
        def __init__(self, **kwargs):
            super(FouilleBureauTrace, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            result = renpy.Render(int(width), int(height))
            canvas = result.canvas()
            points = store.fb_path
            if store.fb_phase in ("trace", "flying") and len(points) > 1:
                for index in range(1, len(points)):
                    canvas.line("#07101acc", points[index - 1], points[index], 22)
                    canvas.line("#77d9ffcc", points[index - 1], points[index], 11)
                target = store.fb_progress * store.fb_path_length
                walked = 0.0
                for index in range(1, len(points)):
                    start = points[index - 1]
                    end = points[index]
                    segment = fb_dist(start, end)
                    if walked >= target:
                        break
                    if walked + segment <= target:
                        canvas.line("#fff3b0", start, end, 8)
                    else:
                        ratio = (target - walked) / max(1.0, segment)
                        partial = (int(start[0] + (end[0] - start[0]) * ratio), int(start[1] + (end[1] - start[1]) * ratio))
                        canvas.line("#fff3b0", start, partial, 8)
                        break
                    walked += segment
                sx, sy = points[0]
                ex, ey = points[-1]
                pulse = 7 + int(4 * (math.sin(st * 7.0) * .5 + .5))
                canvas.circle("#ffffffdd", (sx, sy), 28 + pulse, 4)
                canvas.circle("#77d9ffee", (sx, sy), 17, 0)
                canvas.circle("#fff3b0dd", (ex, ey), 18, 3)
                if store.fb_pressed:
                    color = "#ff6177" if store.fb_stray else "#ffffff"
                    canvas.circle(color, (int(store.fb_mouse_x), int(store.fb_mouse_y)), 12, 0)
            renpy.redraw(self, 0.03)
            return result

        def visit(self):
            return []

transform fb_desk_settle:
    alpha 0.0
    yoffset 20
    easeout 0.35 alpha 1.0 yoffset 0

transform fb_item_idle:
    subpixel True
    block:
        ease 1.15 yoffset -3
        ease 1.15 yoffset 1
        repeat

transform fb_point_pulse:
    alpha .72
    zoom .92
    block:
        ease .55 alpha 1.0 zoom 1.12
        ease .55 alpha .72 zoom .92
        repeat

screen fouille_bureau_game():
    modal True
    zorder 180

    on "show" action Function(fb_reset)
    key "mousedown_1" action Function(fb_press)
    key "mouseup_1" action Function(fb_release)
    key "K_ESCAPE" action Function(fb_cancel_trace)
    timer .03 repeat True action Function(fb_tick)

    add Solid("#000000")
    add Transform(FB_DESK, zoom=.93):
        xalign .5
        yalign .53
        at fb_desk_settle

    for item in FB_ITEMS:
        if item["id"] not in fb_removed:
            $ item_image = Transform(im.Crop(FB_SHEET, item["crop"]), zoom=item["zoom"])
            if fb_phase == "flying" and fb_active == item["id"]:
                $ flight_ratio = min(1.0, fb_flight_time / .67)
                $ flight_x = item["x"] + int(item["fly"][0] * flight_ratio)
                $ flight_y = item["y"] + int(item["fly"][1] * flight_ratio - 310 * 4 * flight_ratio * (1.0 - flight_ratio))
                $ flight_alpha = min(1.0, max(0.0, (1.0 - flight_ratio) * 3.2))
                add Transform(item_image, rotate=item["fly"][2] * flight_ratio, alpha=flight_alpha, rotate_pad=False):
                    xpos flight_x
                    ypos flight_y
                    xanchor .5
                    yanchor .5
            else:
                add item_image:
                    xpos item["x"]
                    ypos item["y"]
                    xanchor .5
                    yanchor .5
                    at fb_item_idle

            if fb_phase == "pick":
                $ point_x = item["x"]
                $ point_y = item["y"] + item.get("point_y", 0)
                button:
                    xpos point_x - 42
                    ypos point_y - 42
                    xsize 84
                    ysize 84
                    background None
                    hover_background Solid("#77d9ff18")
                    action Function(fb_select, item["id"])
                    add Solid("#77d9ff38", xsize=38, ysize=38) xalign .5 yalign .5 at fb_point_pulse
                    text "+" size 31 color "#ffffff" xalign .5 yalign .5

    add FouilleBureauTrace()

    frame:
        xalign .5
        ypos 24
        xsize 1120
        padding (24, 14)
        background Solid("#07111aee")
        vbox:
            spacing 5
            text "FOUILLE DU BUREAU" size 34 color "#fff3b0" xalign .5 font "fonts/Rajdhani-SemiBold.ttf"
            text "Dégage chaque objet pour retrouver le dessin de Juliette." size 21 color "#dceaf5" xalign .5
            text "[len(fb_removed)] / [len(FB_ITEMS)]" size 24 color "#77d9ff" xalign .5

    if fb_feedback:
        frame:
            xalign .5
            yalign .91
            xsize 900
            padding (18, 12)
            background Solid("#07111add")
            text "[fb_feedback]" size 23 color "#ffffff" xalign .5 text_align .5

    if fb_phrase:
        frame:
            xalign .5
            yalign .80
            xsize 760
            padding (22, 14)
            background Solid("#05090def")
            vbox:
                spacing 3
                text "NOAM" size 19 color "#77d9ff" xalign .5
                text "[fb_phrase]" size 31 color "#ffffff" xalign .5 text_align .5

    if len(fb_removed) >= len(FB_ITEMS) and fb_phase == "pick":
        timer .75 action Return(True)

label fouille_bureau_run:
    scene black
    call screen fouille_bureau_game
    return
