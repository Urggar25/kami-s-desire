# One-shot additive sprite movements. No camera shake or blocking pause.
default kd_pending_character_motion = None

transform kd_motion_arc(dx, dy, rise, settle):
    subpixel True
    xoffset 0
    yoffset 0
    easeout rise xoffset dx yoffset dy
    ease settle xoffset 0 yoffset 0

transform kd_motion_shiver(dx, t):
    subpixel True
    xoffset 0
    linear t xoffset dx
    linear t xoffset (-dx)
    linear t xoffset (dx / 2)
    easeout t xoffset 0

transform kd_motion_laugh:
    subpixel True
    yoffset 0
    easeout .09 yoffset -9
    easein .09 yoffset 0
    easeout .09 yoffset -5
    easein .18 yoffset 0

transform kd_motion_idle:
    xoffset 0
    yoffset 0

init python:
    # Durations and amplitudes are deliberately small at 1920x1080.
    KD_CHARACTER_MOTIONS = {
        "sigh": (0, 9, .28, .37),
        "surprise": (0, -16, .09, .16),
        "exasperation": (5, 6, .16, .28),
        "embarrassed": (10, 5, .15, .28),
        "interest": (0, -7, .18, .27),
        "suspicion": (-5, 0, .22, .28),
        "step_back": (18, 5, .14, .21),
        "recoil": (18, 5, .14, .21),
        "approach": (0, -10, .20, .30),
        "lean_forward": (0, -11, .16, .24),
        "exhausted": (0, 15, .28, .42),
        "shock": (0, -20, .10, .20),
        "emphasis": (0, -6, .08, .17),
        "enter": (18, 0, .12, .23),
        "exit": (-18, 0, .16, .24),
    }

    def kd_character_motion(name):
        if name == "anger":
            return kd_motion_shiver(9, .045)
        if name == "nervous":
            return kd_motion_shiver(5, .125)
        if name == "hesitate":
            return kd_motion_shiver(4, .125)
        if name == "laugh":
            return kd_motion_laugh
        if name in KD_CHARACTER_MOTIONS:
            return kd_motion_arc(*KD_CHARACTER_MOTIONS[name])
        return kd_motion_idle

    def kd_queue_character_motion(tag, name):
        # Applied after the line's normal camera/lighting callback.
        store.kd_pending_character_motion = (tag, name)

    def kd_play_queued_character_motion(speaker):
        pending = store.kd_pending_character_motion
        if pending is None:
            return
        store.kd_pending_character_motion = None
        tag, name = pending
        if speaker != tag or renpy.is_skipping() or not persistent.kd_dialogue_direction:
            return
        if scene_has_no_character_sprites() or not renpy.showing(tag, layer="master"):
            return
        if renpy.get_screen("kami_broadcast_ui") or renpy.get_screen("kd_news_broadcast"):
            return
        if store.kd_direction_active and tag in kd_direct_visible():
            kd_direct_draw(tag, reaction=name)
            return
        st = store.char_state.get(tag)
        if not st:
            return
        expr = kd_direct_expression(tag)
        x, y = st.get("x", .5), st.get("y", 1.0)
        scale = st.get("group_scale", 1.0)
        mode = st.get("mode")
        z = st.get("zorder", 0)
        base = [Position(xalign=x, yalign=y)]
        if mode == "focus":
            base.append(char_focus(scale))
            z = 500
        elif mode == "dim":
            base.append(char_dim(.35, scale))
        else:
            base.append(char_restore_scaled(scale))
        renpy.show(tag + " " + expr, tag=tag, layer="master",
                   at_list=base + [kd_character_motion(name)], zorder=z)
