# --------------------------------------------------------------------------------------------
# TRACE QTE — Mini-jeu QTE générique (Attendre / Maintenir / Glisser)
# Compatible Ren'Py 8.3.7
#
# Usage :
#   call screen trace_qte(
#       path_type="vertical_up",
#       time_limit=6.0,
#       wait_time=1.2,
#       tolerance=45,
#       max_errors=3,
#       success_label="LABEL_SUCCESS",
#       fail_label="LABEL_FAIL"
#   )
#
# Le screen NE pose PAS d'image de fond : il pose juste un voile semi-transparent
# par-dessus la scène actuelle (l'image courante reste visible).
# --------------------------------------------------------------------------------------------

default tq_phase = "wait"            # "wait" / "hold" / "trace" / "done"
default tq_result = None             # "success" / "fail" / None
default tq_progress = 0.0            # 0.0 -> 1.0
default tq_errors = 0
default tq_stray = False
default tq_mouse_x = 960
default tq_mouse_y = 540
default tq_elapsed = 0.0
default tq_wait_remaining = 1.0
default tq_pulse = 0.0
default tq_pressed = False
default tq_path_points = []
default tq_path_length = 1.0
default tq_anchor_x = 960
default tq_anchor_y = 540
default tq_success_label = None
default tq_fail_label = None

init -2 python:
    import math
    try:
        import pygame_sdl2 as _tq_pygame
    except Exception:
        _tq_pygame = None

    # ------------------------------------------------------------------
    # Trajectoires
    # ------------------------------------------------------------------
    def tq_build_path(path_type, anchor_x=960, anchor_y=540):
        pts = []
        if path_type == "vertical_up":
            for i in range(21):
                t = i / 20.0
                pts.append((anchor_x, anchor_y + 280 - int(560 * t)))
        elif path_type == "vertical_down":
            for i in range(21):
                t = i / 20.0
                pts.append((anchor_x, anchor_y - 280 + int(560 * t)))
        elif path_type == "curve_right":
            for i in range(31):
                t = i / 30.0
                x = anchor_x + int(260 * math.sin(t * math.pi))
                y = anchor_y + 280 - int(560 * t)
                pts.append((x, y))
        elif path_type == "curve_left":
            for i in range(31):
                t = i / 30.0
                x = anchor_x - int(260 * math.sin(t * math.pi))
                y = anchor_y + 280 - int(560 * t)
                pts.append((x, y))
        elif path_type == "s_curve":
            for i in range(41):
                t = i / 40.0
                x = anchor_x + int(170 * math.sin(t * math.pi * 2))
                y = anchor_y + 280 - int(560 * t)
                pts.append((x, y))
        elif path_type == "arc":
            for i in range(31):
                t = i / 30.0
                ang = math.pi - t * math.pi
                x = anchor_x + int(260 * math.cos(ang))
                y = anchor_y - int(220 * math.sin(ang)) + 60
                pts.append((x, y))
        else:
            for i in range(21):
                t = i / 20.0
                pts.append((anchor_x, anchor_y + 280 - int(560 * t)))
        return pts

    def tq_path_total_length(points):
        total = 0.0
        for i in range(1, len(points)):
            ax, ay = points[i - 1]
            bx, by = points[i]
            total += ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
        return max(1.0, total)

    def tq_dist(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def tq_dist_to_segment(p, a, b):
        ax, ay = a
        bx, by = b
        px, py = p
        dx = bx - ax
        dy = by - ay
        if dx == 0 and dy == 0:
            return tq_dist(p, a), 0.0
        denom = float(dx * dx + dy * dy)
        t = ((px - ax) * dx + (py - ay) * dy) / denom
        tc = max(0.0, min(1.0, t))
        closest = (ax + tc * dx, ay + tc * dy)
        return tq_dist(p, closest), tc

    def tq_closest_progress(points, pos):
        best_d = 1e9
        best_len = 0.0
        cumul = 0.0
        for i in range(1, len(points)):
            a = points[i - 1]
            b = points[i]
            seg_len = tq_dist(a, b)
            d, t = tq_dist_to_segment(pos, a, b)
            if d < best_d:
                best_d = d
                best_len = cumul + t * seg_len
            cumul += seg_len
        return best_d, best_len

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def tq_reset(path_type, anchor_x, anchor_y, wait_time, success_label, fail_label):
        store.tq_phase = "wait"
        store.tq_result = None
        store.tq_progress = 0.0
        store.tq_errors = 0
        store.tq_stray = False
        store.tq_pressed = False
        store.tq_pulse = 0.0
        store.tq_elapsed = 0.0
        store.tq_wait_remaining = max(0.05, float(wait_time))
        store.tq_anchor_x = anchor_x
        store.tq_anchor_y = anchor_y
        store.tq_path_points = tq_build_path(path_type, anchor_x, anchor_y)
        store.tq_path_length = tq_path_total_length(store.tq_path_points)
        store.tq_success_label = success_label
        store.tq_fail_label = fail_label

    def tq_on_press(start_radius):
        if store.tq_phase == "done":
            return
        store.tq_pressed = True
        pos = renpy.get_mouse_pos()
        store.tq_mouse_x, store.tq_mouse_y = pos
        if store.tq_phase == "wait":
            store.tq_phase = "done"
            store.tq_result = "fail"
            return
        if store.tq_phase == "hold":
            start_pt = store.tq_path_points[0]
            if tq_dist(pos, start_pt) <= start_radius:
                store.tq_phase = "trace"
                store.tq_progress = 0.0
                store.tq_errors = 0
                store.tq_stray = False
                store.tq_elapsed = 0.0
            else:
                store.tq_phase = "done"
                store.tq_result = "fail"

    def tq_on_release():
        store.tq_pressed = False
        if store.tq_phase == "trace" and store.tq_progress < 0.985:
            store.tq_phase = "done"
            store.tq_result = "fail"

    def tq_tick(time_limit, tolerance, max_errors):
        if store.tq_phase == "done":
            return
        store.tq_pulse = (store.tq_pulse + 0.08) % 6.2832
        pos = renpy.get_mouse_pos()
        store.tq_mouse_x, store.tq_mouse_y = pos

        if store.tq_phase == "wait":
            store.tq_wait_remaining -= 0.03
            if store.tq_wait_remaining <= 0.0:
                store.tq_phase = "hold"
            return

        if store.tq_phase == "hold":
            return

        if store.tq_phase == "trace":
            # vérifie bouton toujours pressé
            if _tq_pygame is not None and not _tq_pygame.mouse.get_pressed()[0]:
                if store.tq_progress < 0.985:
                    store.tq_phase = "done"
                    store.tq_result = "fail"
                    return

            store.tq_elapsed += 0.03
            if store.tq_elapsed >= time_limit:
                store.tq_phase = "done"
                store.tq_result = "fail"
                return

            points = store.tq_path_points
            d, length_along = tq_closest_progress(points, pos)

            new_progress = length_along / store.tq_path_length
            if new_progress > store.tq_progress:
                store.tq_progress = min(1.0, new_progress)

            if d > tolerance:
                store.tq_stray = True
                store.tq_errors += 1
                # max_errors compté en "ticks" hors zone (~30 ticks/s)
                if store.tq_errors >= max_errors * 14:
                    store.tq_phase = "done"
                    store.tq_result = "fail"
                    return
            else:
                store.tq_stray = False

            if store.tq_progress >= 0.985:
                store.tq_phase = "done"
                store.tq_result = "success"

    # ------------------------------------------------------------------
    # Displayable custom : dessine cercles + tracé propres (anti-alias)
    # ------------------------------------------------------------------
    class TraceQTEDrawable(renpy.Displayable):
        def __init__(self, **kwargs):
            super(TraceQTEDrawable, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            W = int(width)
            H = int(height)
            rv = renpy.Render(W, H)
            c = rv.canvas()

            phase = store.tq_phase
            pts = store.tq_path_points or [(store.tq_anchor_x, store.tq_anchor_y)]
            sx, sy = pts[0]

            # ---- Tracé ----
            if phase in ("trace", "done") and len(pts) >= 2:
                progress = float(store.tq_progress)
                stray = bool(store.tq_stray)

                base_color = "#ff5a5add" if stray else "#dceaf5cc"
                done_color = "#ffffffee"
                shadow_color = "#0a1016cc"
                inner_color = "#121c26eb"

                # ombre arrière large
                for i in range(1, len(pts)):
                    c.line(shadow_color, pts[i - 1], pts[i], 22)
                # contour
                for i in range(1, len(pts)):
                    c.line(base_color, pts[i - 1], pts[i], 14)
                # remplissage intérieur (vide)
                for i in range(1, len(pts)):
                    c.line(inner_color, pts[i - 1], pts[i], 8)

                # portion accomplie
                total_len = max(1.0, store.tq_path_length)
                target = progress * total_len
                cum = 0.0
                for i in range(1, len(pts)):
                    a = pts[i - 1]
                    b = pts[i]
                    seg = tq_dist(a, b)
                    if cum >= target:
                        break
                    if cum + seg <= target:
                        c.line(done_color, a, b, 8)
                    else:
                        ratio = (target - cum) / seg
                        bx = int(a[0] + (b[0] - a[0]) * ratio)
                        by = int(a[1] + (b[1] - a[1]) * ratio)
                        c.line(done_color, a, (bx, by), 8)
                        break
                    cum += seg

                # point d'arrivée
                ex, ey = pts[-1]
                c.circle("#dceaf5dd", (ex, ey), 18, 3)

            # ---- Cercle de départ ----
            pulse = math.sin(store.tq_pulse) * 0.5 + 0.5
            if phase == "wait":
                ring_r = 90 + int(pulse * 6)
                c.circle("#ffffffa0", (sx, sy), ring_r, 3)
            elif phase == "hold":
                ring_r = 90 + int(pulse * 10)
                c.circle("#ffffffe6", (sx, sy), ring_r, 4)
            else:
                c.circle("#ffffffa0", (sx, sy), 88, 2)

            # ---- Disque intérieur ----
            if phase == "trace":
                if store.tq_stray:
                    inner_fill = "#d25a5ac8"
                else:
                    inner_fill = "#a0c8ebdc"
            else:
                inner_fill = "#6e91b4b4"
            c.circle(inner_fill, (sx, sy), 46, 0)
            c.circle("#ffffffdc", (sx, sy), 46, 2)

            # ---- Curseur actif ----
            if phase == "trace":
                mx = int(store.tq_mouse_x)
                my = int(store.tq_mouse_y)
                if store.tq_stray:
                    c.circle("#ff64646e", (mx, my), 26, 0)
                    c.circle("#ff8282e6", (mx, my), 12, 0)
                else:
                    c.circle("#ffffff5a", (mx, my), 26, 0)
                    c.circle("#ffffffe6", (mx, my), 12, 0)

            # ---- Flash de fin ----
            if phase == "done":
                if store.tq_result == "success":
                    c.circle("#b4ffc8b4", (sx, sy), 110, 5)
                elif store.tq_result == "fail":
                    c.circle("#ff6464b4", (sx, sy), 110, 5)

            renpy.redraw(self, 0)
            return rv

        def visit(self):
            return []

# --------------------------------------------------------------------------------------------
# TRANSFORMS
# --------------------------------------------------------------------------------------------

transform tq_label_pulse:
    alpha 0.85
    block:
        linear 0.7 alpha 1.0
        linear 0.7 alpha 0.7
        repeat

# --------------------------------------------------------------------------------------------
# SCREEN PRINCIPAL
# --------------------------------------------------------------------------------------------

screen trace_qte(path_type="vertical_up", time_limit=6.0, wait_time=1.2, tolerance=45, max_errors=3, success_label=None, fail_label=None, anchor_x=960, anchor_y=540, start_radius=95):
    modal True
    zorder 150

    on "show" action Function(tq_reset, path_type, anchor_x, anchor_y, wait_time, success_label, fail_label)

    key "mousedown_1" action Function(tq_on_press, start_radius)
    key "mouseup_1" action Function(tq_on_release)

    # Voile sombre semi-transparent : l'image de fond actuelle reste visible
    add Solid("#00000077")

    # Drawable custom (cercles, tracé, curseur)
    add TraceQTEDrawable()

    # Label sous l'action
    $ phase = tq_phase
    if phase == "wait":
        $ label_text = "ATTENDRE"
    elif phase == "hold":
        $ label_text = "MAINTENIR"
    elif phase == "trace":
        $ label_text = "GLISSER"
    else:
        $ label_text = ""

    if label_text:
        text label_text:
            xpos tq_anchor_x
            ypos (tq_anchor_y + 120)
            xanchor 0.5
            yanchor 0.0
            size 28
            color "#ffffff"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(2, "#000000aa", 0, 0)]
            at tq_label_pulse

    # Tick global
    timer 0.03 repeat True action Function(tq_tick, time_limit, tolerance, max_errors)
    # Sortie : quand phase=="done" on ferme le screen après un court délai (animation fin)
    if tq_phase == "done":
        if tq_result == "success" and tq_success_label:
            timer 0.45 action [Hide("trace_qte"), Jump(tq_success_label)]
        elif tq_result == "fail" and tq_fail_label:
            timer 0.45 action [Hide("trace_qte"), Jump(tq_fail_label)]
        else:
            timer 0.45 action Return(tq_result == "success")

# --------------------------------------------------------------------------------------------
# Labels de test
# --------------------------------------------------------------------------------------------

label _TEST_TRACE_VERTICAL_UP:
    scene black
    call screen trace_qte(path_type="vertical_up", time_limit=6.0, wait_time=1.2, tolerance=45, max_errors=3, success_label="_TEST_TRACE_SUCCESS", fail_label="_TEST_TRACE_FAIL")
    return

label _TEST_TRACE_VERTICAL_DOWN:
    scene black
    call screen trace_qte(path_type="vertical_down", time_limit=6.0, wait_time=1.2, tolerance=45, max_errors=3, success_label="_TEST_TRACE_SUCCESS", fail_label="_TEST_TRACE_FAIL")
    return

label _TEST_TRACE_CURVE_RIGHT:
    scene black
    call screen trace_qte(path_type="curve_right", time_limit=7.0, wait_time=1.2, tolerance=45, max_errors=3, success_label="_TEST_TRACE_SUCCESS", fail_label="_TEST_TRACE_FAIL")
    return

label _TEST_TRACE_SUCCESS:
    "QTE REUSSI."
    return

label _TEST_TRACE_FAIL:
    "QTE RATE."
    return
