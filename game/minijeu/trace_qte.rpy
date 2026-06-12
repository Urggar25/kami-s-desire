# --------------------------------------------------------------------------------------------
# TRACE QTE v2 — Mini-jeu QTE générique (Attendre / Maintenir / Glisser)
# Compatible Ren'Py 8.3.7
#
# Usage recommandé (gère tutoriel, retry avec malus, résultats avec rang) :
#   call trace_qte_run(
#       mg_id="trace_reveil", title="SYNCHRONISATION NEURALE",
#       path_type="curve_right", time_limit=6.0, wait_time=1.2,
#       tolerance=55, max_errors=4, anchor_x=960, anchor_y=620,
#       required=True, show_results=True)
#   → _return = rang ("S".."D") si réussi, "FAIL" si abandon (required=False)
#
# Usage bas niveau (juste le screen, retourne un dict) :
#   call screen trace_qte(...)
#   → _return = {"success": bool, "elapsed": float, "avg_dev": float, "stray_ticks": int}
# --------------------------------------------------------------------------------------------

default tq_phase = "wait"            # "wait" / "hold" / "trace" / "done"
default tq_result = None             # "success" / "fail" / None
default tq_progress = 0.0
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
default tq_dev_sum = 0.0
default tq_dev_samples = 0
default tq_stray_ticks = 0
default tq_time_limit = 6.0
default tq_tolerance = 45

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
    def tq_reset(path_type, anchor_x, anchor_y, wait_time, time_limit, tolerance):
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
        store.tq_dev_sum = 0.0
        store.tq_dev_samples = 0
        store.tq_stray_ticks = 0
        store.tq_time_limit = float(time_limit)
        store.tq_tolerance = float(tolerance)

    def tq_on_press(start_radius):
        if store.tq_phase == "done":
            return
        store.tq_pressed = True
        pos = renpy.get_mouse_pos()
        store.tq_mouse_x, store.tq_mouse_y = pos
        if store.tq_phase == "wait":
            store.tq_phase = "done"
            store.tq_result = "fail"
            renpy.play("audio/sfx_drop.mp3", channel="sound")
            return
        if store.tq_phase == "hold":
            start_pt = store.tq_path_points[0]
            if tq_dist(pos, start_pt) <= start_radius:
                store.tq_phase = "trace"
                store.tq_progress = 0.0
                store.tq_errors = 0
                store.tq_stray = False
                store.tq_elapsed = 0.0
                renpy.play("audio/sfx_beep.mp3", channel="sound")
            else:
                store.tq_phase = "done"
                store.tq_result = "fail"
                renpy.play("audio/sfx_drop.mp3", channel="sound")

    def tq_on_release():
        store.tq_pressed = False
        if store.tq_phase == "trace" and store.tq_progress < 0.985:
            store.tq_phase = "done"
            store.tq_result = "fail"
            renpy.play("audio/sfx_drop.mp3", channel="sound")

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

            store.tq_dev_sum += d
            store.tq_dev_samples += 1

            new_progress = length_along / store.tq_path_length
            if new_progress > store.tq_progress:
                store.tq_progress = min(1.0, new_progress)

            if d > tolerance:
                store.tq_stray = True
                store.tq_errors += 1
                store.tq_stray_ticks += 1
                if store.tq_errors >= max_errors * 14:
                    store.tq_phase = "done"
                    store.tq_result = "fail"
                    return
            else:
                store.tq_stray = False

            if store.tq_progress >= 0.985:
                store.tq_phase = "done"
                store.tq_result = "success"
                renpy.play("audio/sfx_clap.mp3", channel="sound")

    def tq_collect_stats():
        avg_dev = (store.tq_dev_sum / store.tq_dev_samples) if store.tq_dev_samples else 0.0
        return {
            "success": store.tq_result == "success",
            "elapsed": store.tq_elapsed,
            "avg_dev": avg_dev,
            "stray_ticks": store.tq_stray_ticks,
        }

    def tq_compute_score(stats, time_limit, tolerance):
        """Score sur 1000 : 600 précision + 400 vitesse."""
        if not stats["success"]:
            return 0
        precision = max(0.0, 1.0 - (stats["avg_dev"] / float(tolerance)))
        speed = max(0.0, 1.0 - (stats["elapsed"] / float(time_limit)))
        return int(round(600 * precision + 400 * min(1.0, speed * 1.6)))

    # ------------------------------------------------------------------
    # Displayable custom : cercles + tracé
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

                for i in range(1, len(pts)):
                    c.line(shadow_color, pts[i - 1], pts[i], 22)
                for i in range(1, len(pts)):
                    c.line(base_color, pts[i - 1], pts[i], 14)
                for i in range(1, len(pts)):
                    c.line(inner_color, pts[i - 1], pts[i], 8)

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

            if phase == "trace":
                if store.tq_stray:
                    inner_fill = "#d25a5ac8"
                else:
                    inner_fill = "#a0c8ebdc"
            else:
                inner_fill = "#6e91b4b4"
            c.circle(inner_fill, (sx, sy), 46, 0)
            c.circle("#ffffffdc", (sx, sy), 46, 2)

            if phase == "trace":
                mx = int(store.tq_mouse_x)
                my = int(store.tq_mouse_y)
                if store.tq_stray:
                    c.circle("#ff64646e", (mx, my), 26, 0)
                    c.circle("#ff8282e6", (mx, my), 12, 0)
                else:
                    c.circle("#ffffff5a", (mx, my), 26, 0)
                    c.circle("#ffffffe6", (mx, my), 12, 0)

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

screen trace_qte(path_type="vertical_up", time_limit=6.0, wait_time=1.2, tolerance=45, max_errors=3, anchor_x=960, anchor_y=540, start_radius=95, challenges_hud=True):
    modal True
    zorder 150

    on "show" action Function(tq_reset, path_type, anchor_x, anchor_y, wait_time, time_limit, tolerance)

    key "mousedown_1" action Function(tq_on_press, start_radius)
    key "mouseup_1" action Function(tq_on_release)

    add Solid("#00000077")
    add TraceQTEDrawable()

    # Barre de temps pendant la phase trace
    if tq_phase == "trace":
        fixed:
            xalign 0.5
            ypos 32
            xsize 600
            ysize 12
            add Solid("#0A1326CC", xsize=600, ysize=12)
            $ _tq_time_ratio = max(0.0, 1.0 - tq_elapsed / max(0.01, tq_time_limit))
            if _tq_time_ratio > 0.4:
                add Solid("#7DF9FF", xsize=int(600 * _tq_time_ratio), ysize=12)
            else:
                add Solid("#FF4D6D", xsize=int(600 * _tq_time_ratio), ysize=12)

    # Défis live
    if challenges_hud and tq_phase in ("hold", "trace"):
        $ _tq_no_stray = (tq_stray_ticks == 0)
        $ _tq_fast = (tq_elapsed <= tq_time_limit * 0.6)
        use mk_challenge_hud([
            ("Zéro sortie de piste", False, not _tq_no_stray),
            ("Rapide (-40% du chrono)", False, not _tq_fast),
        ])

    # Pas de bouton d'aide ici : tout clic hors séquence fait partie du gameplay.

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

    timer 0.03 repeat True action Function(tq_tick, time_limit, tolerance, max_errors)
    if tq_phase == "done":
        timer 0.45 action Return(tq_collect_stats())

# --------------------------------------------------------------------------------------------
# TUTORIEL ANIMÉ
# --------------------------------------------------------------------------------------------

transform tq_demo_ring_pulse:
    zoom 1.0
    alpha 0.8
    block:
        ease 0.6 zoom 1.10 alpha 1.0
        ease 0.6 zoom 1.0 alpha 0.8
        repeat

transform tq_demo_cursor_anim:
    # boucle : approche → maintien (pulse) → glisse le long de la courbe → reset
    xpos 360 ypos 470 alpha 0.0
    block:
        easein 0.4 alpha 1.0
        easeout 0.9 xpos 360 ypos 400
        # clic maintenu
        easeout 0.12 zoom 0.8
        pause 0.5
        # glissé le long de la courbe (approximation en 4 segments)
        easeout 0.45 xpos 430 ypos 320
        easeout 0.45 xpos 470 ypos 230
        easeout 0.45 xpos 430 ypos 140
        easeout 0.45 xpos 360 ypos 60
        easein 0.12 zoom 1.0
        pause 0.4
        easeout 0.4 alpha 0.0
        pause 0.5
        repeat

transform tq_demo_step_label:
    alpha 0.0
    block:
        pause 0.4
        linear 0.3 alpha 1.0
        pause 1.4
        linear 0.3 alpha 0.0
        pause 2.4
        repeat

screen tuto_trace_qte(as_overlay=False):
    use mk_tuto_chrome("TRACÉ SYNCHRONISÉ", [
        ("Attendre", "Ne clique pas tant que l'anneau n'est pas blanc. Cliquer trop tôt = échec."),
        ("Maintenir", "Clique sur le cercle de départ et garde le bouton enfoncé."),
        ("Glisser", "Suis la ligne jusqu'au bout sans relâcher. Reste dans le couloir."),
    ], "tuto_trace_qte", as_overlay):

        # Courbe en pointillés
        fixed:
            xfill True
            yfill True

            for tq_i in range(0, 13):
                $ tq_t = tq_i / 12.0
                $ tq_dx = int(360 + 110 * math.sin(tq_t * 3.14159))
                $ tq_dy = int(400 - 340 * tq_t)
                add Solid("#7DF9FF99") size (8, 8) pos (tq_dx - 4, tq_dy - 4)

            # Anneau de départ
            fixed at tq_demo_ring_pulse:
                xpos 360
                ypos 400
                xanchor 0.5
                yanchor 0.5
                xsize 110
                ysize 110
                add Solid("#FFFFFF22") size (110, 110) align (0.5, 0.5)
                add Solid("#A0C8EBDC") size (62, 62) align (0.5, 0.5)

            # Point d'arrivée
            add Solid("#5DFF9ACC") size (20, 20) pos (350, 50)

            # Faux curseur animé
            fixed at tq_demo_cursor_anim:
                xanchor 0.5
                yanchor 0.5
                xsize 34
                ysize 34
                add Solid("#FFFFFF55") size (34, 34) align (0.5, 0.5)
                add Solid("#FFFFFFEE") size (12, 12) align (0.5, 0.5)

            text "MAINTENIR PUIS GLISSER" at tq_demo_step_label:
                xpos 380
                ypos 480
                xanchor 0.5
                size 22
                color "#FFD166"
                bold True

# --------------------------------------------------------------------------------------------
# WRAPPER COMPLET : tutoriel → jeu → retry avec malus → résultats avec rang
# --------------------------------------------------------------------------------------------

label trace_qte_run(mg_id="trace_qte", title="TRACÉ SYNCHRONISÉ", path_type="curve_right", time_limit=6.0, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True, show_results=True):

    call mk_tutorial("trace_qte", "tuto_trace_qte")
    $ mk_reset_retries(mg_id)

label .attempt:
    call screen trace_qte(path_type=path_type, time_limit=time_limit, wait_time=wait_time, tolerance=tolerance, max_errors=max_errors, anchor_x=anchor_x, anchor_y=anchor_y)
    $ tq_run_stats = _return

    if not tq_run_stats["success"]:
        if required:
            call mk_fail_retry(title, mg_id)
            jump .attempt
        else:
            return "FAIL"

    if not show_results:
        return "B"

    python:
        tq_run_score = tq_compute_score(tq_run_stats, time_limit, tolerance)
        tq_run_challenges = [
            ("Zéro sortie de piste", tq_run_stats["stray_ticks"] == 0),
            ("Rapide (-40% du chrono)", tq_run_stats["elapsed"] <= time_limit * 0.6),
            ("Précision chirurgicale", tq_run_stats["avg_dev"] <= tolerance * 0.4),
        ]
        tq_run_score = min(1000, tq_run_score + 50 * len([1 for c in tq_run_challenges if c[1]]))

    call mk_show_results(
        title,
        tq_run_score,
        1000,
        stats=[
            ("Temps", "%.1fs / %.1fs" % (tq_run_stats["elapsed"], time_limit)),
            ("Écart moyen", "%dpx" % int(tq_run_stats["avg_dev"])),
            ("Sorties de piste", str(tq_run_stats["stray_ticks"])),
        ],
        challenges=tq_run_challenges,
        mg_id=mg_id,
        retries=mk_get_retries(mg_id),
    )
    return _return

# --------------------------------------------------------------------------------------------
# Labels de test
# --------------------------------------------------------------------------------------------

label _TEST_TRACE_VERTICAL_UP:
    scene black
    call trace_qte_run(mg_id="test_trace", title="TEST VERTICAL", path_type="vertical_up", required=False)
    "Rang obtenu : [_return]"
    return

label _TEST_TRACE_CURVE_RIGHT:
    scene black
    call trace_qte_run(mg_id="test_trace", title="TEST COURBE", path_type="curve_right", time_limit=7.0, required=True)
    "Rang obtenu : [_return]"
    return
