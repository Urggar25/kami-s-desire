# Existing camera coordinates, but deterministic ATL transitions instead of mouse tracking.
transform kd_direct_cam_ease(dx0, dy0, z0, dx1, dy1, z1, t):
    subpixel True
    xalign 0.5
    yalign 0.5
    xoffset dx0
    yoffset dy0
    zoom z0
    ease t xoffset dx1 yoffset dy1 zoom z1

transform kd_direct_cam_linear(dx0, dy0, z0, dx1, dy1, z1, t):
    subpixel True
    xalign 0.5
    yalign 0.5
    xoffset dx0
    yoffset dy0
    zoom z0
    linear t xoffset dx1 yoffset dy1 zoom z1

transform kd_direct_cam_out(dx0, dy0, z0, dx1, dy1, z1, t):
    subpixel True
    xalign 0.5
    yalign 0.5
    xoffset dx0
    yoffset dy0
    zoom z0
    easeout t xoffset dx1 yoffset dy1 zoom z1

transform kd_direct_cam_in(dx0, dy0, z0, dx1, dy1, z1, t):
    subpixel True
    xalign 0.5
    yalign 0.5
    xoffset dx0
    yoffset dy0
    zoom z0
    easein t xoffset dx1 yoffset dy1 zoom z1

init python:
    def kd_direct_clamp(v, lo=0.0, hi=1.0):
        return max(lo, min(hi, float(v)))

    def kd_direct_center_for(x, zoom):
        return 0.5 if zoom <= 1.001 else kd_direct_clamp(0.5+(x-0.5)*zoom/(zoom-1))

    def kd_direct_cam_apply(x, y, z, duration=.4, easing="ease"):
        x, y, z = kd_direct_clamp(x), kd_direct_clamp(y), kd_direct_clamp(z, 1, 1.85)
        t = kd_direct_clamp(duration, 0, 2)
        if renpy.is_skipping() or not persistent.kd_dialogue_direction:
            t = 0
        factory = {"ease": kd_direct_cam_ease, "linear": kd_direct_cam_linear,
                   "easein": kd_direct_cam_in, "easeout": kd_direct_cam_out}.get(easing, kd_direct_cam_ease)
        for layer in ("bgcam", "master"):
            x0, y0, z0 = cam_current(layer)
            w, h = config.screen_width, config.screen_height
            dx0, dy0 = (0.5-x0)*w*(z0-1), (0.5-y0)*h*(z0-1)
            dx1, dy1 = (0.5-x)*w*(z-1), (0.5-y)*h*(z-1)
            if not t:
                dx0, dy0, z0 = dx1, dy1, z
            renpy.show_layer_at([factory(dx0,dy0,z0,dx1,dy1,z,t)], layer=layer)
            if layer == "bgcam":
                store.bg_cam_x_cur, store.bg_cam_y_cur, store.bg_cam_z_cur = x,y,z
            else:
                store.cam_x_cur, store.cam_y_cur, store.cam_z_cur = x,y,z
