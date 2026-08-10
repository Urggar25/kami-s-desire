# ============================================================
# Manette -> curseur souris virtuel
# ============================================================
#
# Ren'Py sait naviguer au focus avec une manette, mais les PnC,
# les drag/drop et certains mini-jeux de ce projet lisent directement
# la position de la souris. Cette surcouche déplace donc le pointeur
# Ren'Py avec la manette et renvoie des clics souris standards.

default kd_gamepad_cursor_x = 960
default kd_gamepad_cursor_y = 540
default kd_gamepad_cursor_active = False
default kd_gamepad_cursor_pressed = False
default kd_gamepad_cursor_secondary_pressed = False
default kd_gamepad_cursor_last_input = 0.0
default kd_gamepad_cursor_left = False
default kd_gamepad_cursor_right = False
default kd_gamepad_cursor_up = False
default kd_gamepad_cursor_down = False
default kd_gamepad_cursor_fast = False

init -20 python:
    import math
    import time
    import pygame_sdl2 as kd_gamepad_pygame

    KD_GAMEPAD_CURSOR_SPEED = 720.0
    KD_GAMEPAD_CURSOR_FAST_MULT = 1.75
    KD_GAMEPAD_CURSOR_IDLE_FADE = 3.0
    KD_GAMEPAD_CURSOR_TICK = 0.016

    def kd_gamepad_cursor_screen_size():
        width = int(getattr(config, "screen_width", 1920) or 1920)
        height = int(getattr(config, "screen_height", 1080) or 1080)
        return width, height

    def kd_gamepad_cursor_clamp(x, y):
        width, height = kd_gamepad_cursor_screen_size()
        return (
            max(0, min(width - 1, int(round(x)))),
            max(0, min(height - 1, int(round(y)))),
        )

    def kd_gamepad_cursor_touch():
        store.kd_gamepad_cursor_active = True
        store.kd_gamepad_cursor_last_input = time.time()

    def kd_gamepad_cursor_suspended():
        try:
            return renpy.get_screen("choice") is not None
        except Exception:
            return False

    def kd_gamepad_cursor_clear_motion():
        store.kd_gamepad_cursor_left = False
        store.kd_gamepad_cursor_right = False
        store.kd_gamepad_cursor_up = False
        store.kd_gamepad_cursor_down = False
        store.kd_gamepad_cursor_fast = False
        store.kd_gamepad_cursor_pressed = False
        store.kd_gamepad_cursor_secondary_pressed = False

    def kd_gamepad_cursor_sync_from_mouse():
        try:
            x, y = renpy.get_mouse_pos()
        except Exception:
            x, y = store.kd_gamepad_cursor_x, store.kd_gamepad_cursor_y
        store.kd_gamepad_cursor_x, store.kd_gamepad_cursor_y = kd_gamepad_cursor_clamp(x, y)

    def kd_gamepad_cursor_set_mouse(x, y):
        x, y = kd_gamepad_cursor_clamp(x, y)
        store.kd_gamepad_cursor_x = x
        store.kd_gamepad_cursor_y = y
        try:
            renpy.set_mouse_pos(x, y, duration=0.0)
        except TypeError:
            try:
                renpy.set_mouse_pos(x, y)
            except Exception:
                pass
        except Exception:
            pass

    def kd_gamepad_cursor_queue(event_name):
        try:
            renpy.queue_event(event_name)
        except Exception:
            pass

    def kd_gamepad_cursor_post_mouse_event(event_type, button=None):
        try:
            x, y = kd_gamepad_cursor_clamp(store.kd_gamepad_cursor_x, store.kd_gamepad_cursor_y)
            data = {"pos": (x, y)}
            if event_type == kd_gamepad_pygame.MOUSEMOTION:
                data["rel"] = (0, 0)
                data["buttons"] = (
                    1 if getattr(store, "kd_gamepad_cursor_pressed", False) else 0,
                    0,
                    1 if getattr(store, "kd_gamepad_cursor_secondary_pressed", False) else 0,
                )
            elif button is not None:
                data["button"] = button
            kd_gamepad_pygame.event.post(kd_gamepad_pygame.event.Event(event_type, data))
        except Exception:
            pass

    def kd_gamepad_cursor_button_down(button=1):
        kd_gamepad_cursor_sync_from_mouse()
        kd_gamepad_cursor_touch()
        if button == 1:
            store.kd_gamepad_cursor_pressed = True
        elif button == 3:
            store.kd_gamepad_cursor_secondary_pressed = True
        kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEMOTION)
        kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEBUTTONDOWN, button)
        if button == 1:
            kd_gamepad_cursor_queue(["mousedown_1", "button_ignore", "bar_activate", "drag_activate", "viewport_drag_start"])
        elif button == 3:
            kd_gamepad_cursor_queue(["mousedown_3", "button_alternate_ignore"])
        else:
            kd_gamepad_cursor_queue("mousedown_%d" % button)
        renpy.restart_interaction()

    def kd_gamepad_cursor_button_up(button=1):
        kd_gamepad_cursor_touch()
        if button == 1:
            store.kd_gamepad_cursor_pressed = False
        elif button == 3:
            store.kd_gamepad_cursor_secondary_pressed = False
        kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEMOTION)
        kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEBUTTONUP, button)
        if button == 1:
            kd_gamepad_cursor_queue(["mouseup_1", "button_select", "bar_deactivate", "drag_deactivate", "viewport_drag_end", "dismiss"])
        elif button == 3:
            kd_gamepad_cursor_queue(["mouseup_3", "button_alternate"])
        else:
            kd_gamepad_cursor_queue("mouseup_%d" % button)
        renpy.restart_interaction()

    def kd_gamepad_cursor_scroll(direction):
        kd_gamepad_cursor_touch()
        if direction < 0:
            kd_gamepad_cursor_queue(["mousedown_5", "viewport_wheeldown"])
        else:
            kd_gamepad_cursor_queue(["mousedown_4", "viewport_wheelup"])
        renpy.restart_interaction()

    def kd_gamepad_cursor_set_dir(direction, enabled):
        if direction == "left":
            store.kd_gamepad_cursor_left = bool(enabled)
        elif direction == "right":
            store.kd_gamepad_cursor_right = bool(enabled)
        elif direction == "up":
            store.kd_gamepad_cursor_up = bool(enabled)
        elif direction == "down":
            store.kd_gamepad_cursor_down = bool(enabled)
        kd_gamepad_cursor_touch()
        renpy.restart_interaction()

    def kd_gamepad_cursor_stop_horizontal():
        store.kd_gamepad_cursor_left = False
        store.kd_gamepad_cursor_right = False
        kd_gamepad_cursor_touch()

    def kd_gamepad_cursor_stop_vertical():
        store.kd_gamepad_cursor_up = False
        store.kd_gamepad_cursor_down = False
        kd_gamepad_cursor_touch()

    def kd_gamepad_cursor_set_fast(enabled):
        store.kd_gamepad_cursor_fast = bool(enabled)
        kd_gamepad_cursor_touch()

    def kd_gamepad_cursor_tick():
        if kd_gamepad_cursor_suspended():
            kd_gamepad_cursor_clear_motion()
            return

        dx = 0
        dy = 0

        if store.kd_gamepad_cursor_left:
            dx -= 1
        if store.kd_gamepad_cursor_right:
            dx += 1
        if store.kd_gamepad_cursor_up:
            dy -= 1
        if store.kd_gamepad_cursor_down:
            dy += 1

        if dx == 0 and dy == 0:
            return

        length = math.sqrt(dx * dx + dy * dy)
        speed = KD_GAMEPAD_CURSOR_SPEED
        if store.kd_gamepad_cursor_fast:
            speed *= KD_GAMEPAD_CURSOR_FAST_MULT

        step = speed * KD_GAMEPAD_CURSOR_TICK
        x = store.kd_gamepad_cursor_x + (dx / length) * step
        y = store.kd_gamepad_cursor_y + (dy / length) * step
        kd_gamepad_cursor_set_mouse(x, y)
        kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEMOTION)
        kd_gamepad_cursor_touch()

    def kd_gamepad_cursor_is_visible():
        if kd_gamepad_cursor_suspended():
            return False
        if not getattr(store, "kd_gamepad_cursor_active", False):
            return False
        if getattr(store, "kd_gamepad_cursor_pressed", False):
            return True
        return (time.time() - getattr(store, "kd_gamepad_cursor_last_input", 0.0)) <= KD_GAMEPAD_CURSOR_IDLE_FADE

    _kd_previous_map_pad_event = config.map_pad_event

    def kd_gamepad_cursor_map_pad_event(event_name):
        if _kd_previous_map_pad_event is not None:
            mapped = list(_kd_previous_map_pad_event(event_name))
        else:
            mapped = list(config.pad_bindings.get(event_name, ()))

        if kd_gamepad_cursor_suspended():
            return mapped

        if event_name == "pad_a_press":
            mapped = ["dismiss", "button_ignore", "bar_activate", "drag_activate", "viewport_drag_start"]
            kd_gamepad_cursor_sync_from_mouse()
            kd_gamepad_cursor_touch()
            store.kd_gamepad_cursor_pressed = True
            kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEMOTION)
            kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEBUTTONDOWN, 1)
            if "mousedown_1" not in mapped:
                mapped.append("mousedown_1")

        elif event_name == "pad_a_release":
            mapped = ["button_select", "bar_deactivate", "drag_deactivate", "viewport_drag_end"]
            kd_gamepad_cursor_touch()
            store.kd_gamepad_cursor_pressed = False
            kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEMOTION)
            kd_gamepad_cursor_post_mouse_event(kd_gamepad_pygame.MOUSEBUTTONUP, 1)
            if "mouseup_1" not in mapped:
                mapped.append("mouseup_1")

        return mapped

    config.map_pad_event = kd_gamepad_cursor_map_pad_event

    if "gamepad_virtual_cursor" not in config.overlay_screens:
        config.overlay_screens.append("gamepad_virtual_cursor")


transform kd_gamepad_cursor_pulse:
    alpha 0.72
    ease 0.25 alpha 1.0
    ease 0.25 alpha 0.72
    repeat

screen gamepad_virtual_cursor():
    zorder 10000

    if not kd_gamepad_cursor_suspended():
        # Stick gauche.
        key "pad_leftx_neg" action Function(kd_gamepad_cursor_set_dir, "left", True)
        key "pad_leftx_pos" action Function(kd_gamepad_cursor_set_dir, "right", True)
        key "pad_leftx_zero" action Function(kd_gamepad_cursor_stop_horizontal)
        key "pad_lefty_neg" action Function(kd_gamepad_cursor_set_dir, "up", True)
        key "pad_lefty_pos" action Function(kd_gamepad_cursor_set_dir, "down", True)
        key "pad_lefty_zero" action Function(kd_gamepad_cursor_stop_vertical)

        # D-pad.
        key "pad_dpleft_press" action Function(kd_gamepad_cursor_set_dir, "left", True)
        key "pad_dpleft_release" action Function(kd_gamepad_cursor_set_dir, "left", False)
        key "pad_dpright_press" action Function(kd_gamepad_cursor_set_dir, "right", True)
        key "pad_dpright_release" action Function(kd_gamepad_cursor_set_dir, "right", False)
        key "pad_dpup_press" action Function(kd_gamepad_cursor_set_dir, "up", True)
        key "pad_dpup_release" action Function(kd_gamepad_cursor_set_dir, "up", False)
        key "pad_dpdown_press" action Function(kd_gamepad_cursor_set_dir, "down", True)
        key "pad_dpdown_release" action Function(kd_gamepad_cursor_set_dir, "down", False)

        # Clic secondaire : A est mappe plus bas niveau pour preserver l'avance dialogue.
        key "pad_x_press" action Function(kd_gamepad_cursor_button_down, 3)
        key "pad_x_release" action Function(kd_gamepad_cursor_button_up, 3)

        # Confort : R1 accelere le curseur, les gachettes simulent la molette.
        key "pad_rightshoulder_press" action Function(kd_gamepad_cursor_set_fast, True)
        key "pad_rightshoulder_release" action Function(kd_gamepad_cursor_set_fast, False)
        key "pad_lefttrigger_pos" action Function(kd_gamepad_cursor_scroll, 1)
        key "pad_righttrigger_pos" action Function(kd_gamepad_cursor_scroll, -1)

    timer KD_GAMEPAD_CURSOR_TICK repeat True action Function(kd_gamepad_cursor_tick)

    if kd_gamepad_cursor_is_visible():
        fixed:
            xpos kd_gamepad_cursor_x
            ypos kd_gamepad_cursor_y
            xanchor 0.5
            yanchor 0.5
            xsize 42
            ysize 42

            add Solid("#FFFFFF44"):
                xysize (36, 36)
                align (0.5, 0.5)
                rotate 45
            add Solid("#5CD3FFDD"):
                xysize (18, 18)
                align (0.5, 0.5)
                rotate 45
                at kd_gamepad_cursor_pulse
            add Solid("#FFFFFF"):
                xysize (6, 6)
                align (0.5, 0.5)
