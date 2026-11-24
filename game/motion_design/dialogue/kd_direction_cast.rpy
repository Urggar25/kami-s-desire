# Existing sprites only. No facial or skeletal asset is synthesized.
transform kd_direct_pose(x, y, scale=1.0, facing=1, dim=0.0, dx=0, dy=0, t=.22, active=False):
    subpixel True
    xalign x
    yalign y
    zoom scale
    xzoom facing
    alpha 1.0
    matrixcolor (TintMatrix("#8d97b8") * BrightnessMatrix(dim) * SaturationMatrix(0.55) if dim < 0 else TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0))
    xoffset 0
    yoffset (10 if active else 0)
    easeout t xoffset dx yoffset dy
    ease t xoffset 0 yoffset 0

transform kd_direct_move(x0, x, y, scale=1.0, facing=1, t=.35, dim=0.0):
    subpixel True
    xalign x0
    yalign y
    zoom scale
    xzoom facing
    alpha 1.0
    matrixcolor (TintMatrix("#8d97b8") * BrightnessMatrix(dim) * SaturationMatrix(0.55) if dim < 0 else TintMatrix("#ffffff") * BrightnessMatrix(0.0) * SaturationMatrix(1.0))
    ease t xalign x

transform kd_direct_arrive(x, y, scale=1.0, facing=1, dx=90, t=.3):
    subpixel True
    xalign x
    yalign y
    zoom scale
    xzoom facing
    alpha 0.0
    xoffset dx
    easeout t alpha 1.0 xoffset 0

transform kd_direct_depart(x, y, scale=1.0, facing=1, dx=160, t=.3):
    subpixel True
    xalign x
    yalign y
    zoom scale
    xzoom facing
    alpha 1.0
    easein t alpha 0.0 xoffset dx

init python:
    KD_DIRECT_REACTIONS = {
        "sigh": (0,8,.27), "surprise": (-9,-14,.13), "exasperation": (4,7,.24),
        "embarrassed": (12,5,.25), "interest": (0,-8,.28), "laugh": (0,-9,.14),
        "suspicion": (-5,0,.25), "silence": (0,0,.3),
        "step_back": (18,6,.28), "approach": (-12,-8,.28),
    }

    def kd_direct_visible():
        return tuple(a for a in store.kd_direction_actors
                     if a in store.char_state and renpy.showing(a, layer="master"))

    def kd_direct_expression(tag):
        attrs = renpy.get_attributes(tag, layer="master") or ()
        if attrs and renpy.has_image(tag+" "+attrs[0]):
            return attrs[0]
        return store.char_state.get(tag, {}).get("expr","neutre")

    def kd_direct_refresh_focus():
        for actor in kd_direct_visible():
            kd_direct_draw(actor)

    def kd_direct_draw(tag, reaction=None, dim=None, old_x=None, entry=None):
        if tag not in kd_direct_visible():
            return
        st = store.char_state[tag]
        x,y = st.get("x",.5),st.get("y",1.0)
        expr = kd_direct_expression(tag)
        st["expr"],st["mode"] = expr,None
        scale,facing,depth = store.kd_direction_poses.get(tag,(st.get("group_scale",1.0),1,0))
        speaker = store.kd_direction_speaker
        active = speaker == tag
        if dim is None:
            dim = -0.28 if speaker is not None and not active else 0.0
        if active:
            scale = max(scale, .98)
        # Match historical speaker contrast and foreground ordering.
        # Keep the authored composition and camera untouched.
        skip = renpy.is_skipping() or not persistent.kd_dialogue_direction
        if reaction:
            dx,dy,t = KD_DIRECT_REACTIONS.get(reaction,(0,0,.2))
            tr = kd_direct_pose(x,y,scale,facing,dim,0 if skip else dx,0 if skip else dy,0 if skip else t)
        elif entry is not None:
            tr = kd_direct_arrive(x,y,scale,facing,entry,0 if skip else .3)
        elif old_x is not None:
            tr = kd_direct_move(x if skip else old_x,x,y,scale,facing,0 if skip else .22,dim)
        else:
            tr = kd_direct_pose(x,y,scale,facing,dim,0,0,0 if skip else .13,active and not skip)
        renpy.show(tag+" "+expr,tag=tag,layer="master",at_list=[tr],zorder=(500 if active else st.get("zorder",0)+depth))
