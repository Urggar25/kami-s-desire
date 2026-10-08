# Jour 25 : comparer la veste, photographier le corps, rejoindre Iris.
# Le fond reste sur master : la lampe du calque lighting reste active.
default j25_veste_inspected = []
default j25_photo_frame = None
default j25_knock_success = False

init python:
    import time as _j25_time
    import math as _j25_math

    # Coordonnées dans le cadre 1920 × 1080 de bg_cg040.
    _J25_VESTE_ZONES = (
        ("devant", (786, 563, 89, 55), (0.433, 0.547),
         "La couleur est exactement la même. Mais ici, il ne manque rien."),
        ("manche", (730, 617, 70, 36), (0.395, 0.586),
         "Non... Le tissu de la manche est intact. Pas de déchirure."),
        ("poignet", (812, 648, 42, 32), (0.433, 0.616),
         "La couture tient encore. Le morceau qu'on a trouvé ne vient pas de là."),
    )

    # Cadrage d'ouverture sur Mara, puis gros plan sur chaque détail.
    _J25_VESTE_BASE_ZOOM = 2.05
    _J25_VESTE_BASE_CENTER = (0.415, 0.575)
    _J25_VESTE_FOCUS_ZOOM = 3.15

    def _j25_veste_screen_rect(rect):
        # Projection de la zone source dans le cadrage agrandi de départ.
        # Les étoiles ET leurs zones de survol suivent la même projection.
        x, y, w, h = rect
        zoom = _J25_VESTE_BASE_ZOOM
        cx, cy = _J25_VESTE_BASE_CENTER
        px = 960 + (x - cx * 1920) * zoom
        py = 540 + (y - cy * 1080) * zoom
        return (int(px), int(py), int(w * zoom), int(h * zoom))

    def _j25_clamp_center(value, zoom):
        margin = 0.5 / zoom
        return max(margin, min(1.0 - margin, value))

    class _J25View(renpy.Displayable):
        def __init__(self, zoom=1.0, center=(0.5, 0.5), **kwargs):
            super(_J25View, self).__init__(**kwargs)
            self.zoom = zoom
            self.center = center
            self.motion = None
            self.draw_st = 0.0
            self.child = Transform("bg_cg040", xysize=(1920, 1080))

        def render(self, width, height, st, at):
            self.draw_st = st
            shake_x = shake_y = 0.0
            if getattr(self, "motion", None) is not None:
                started, initial_zoom, initial_center, target_zoom, target_center, shake = self.motion
                elapsed = max(0.0, st - started)
                lead = 0.14 if shake else 0.0
                duration = 0.62 if shake else 0.30
                if elapsed < lead:
                    strength = 5.0 * (1.0 - elapsed / lead)
                    shake_x = _j25_math.sin(elapsed * 150.0) * strength
                    shake_y = _j25_math.sin(elapsed * 110.0) * strength * 0.55
                amount = min(1.0, max(0.0, (elapsed - lead) / duration))
                eased = amount * amount * (3.0 - 2.0 * amount)
                self.zoom = initial_zoom + (target_zoom - initial_zoom) * eased
                self.center = tuple(a + (b - a) * eased for a, b in zip(initial_center, target_center))
                if amount < 1.0:
                    renpy.redraw(self, 0)
                else:
                    self.motion = None
            scaled = renpy.render(Transform(self.child, zoom=self.zoom), 1920, 1080, st, at)
            cx = _j25_clamp_center(self.center[0], self.zoom)
            cy = _j25_clamp_center(self.center[1], self.zoom)
            result = renpy.Render(1920, 1080)
            result.blit(scaled, (int(960 - cx * 1920 * self.zoom + shake_x), int(540 - cy * 1080 * self.zoom + shake_y)))
            return result

        def visit(self):
            return [self.child]

    def _j25_focus(view, center=None):
        # Départ depuis le zoom courant pour un fondu de mouvement fluide,
        # y compris si le curseur quitte la zone avant la fin du zoom.
        target_zoom = _J25_VESTE_FOCUS_ZOOM if center else _J25_VESTE_BASE_ZOOM
        target_center = center if center else _J25_VESTE_BASE_CENTER
        view.motion = (getattr(view, "draw_st", 0.0), view.zoom, view.center,
                       target_zoom, target_center, center is not None)
        renpy.redraw(view, 0)

    def _j25_veste_complete(view, zone_id, comment):
        if zone_id in store.j25_veste_inspected:
            return
        renpy.set_screen_variable("reaction", comment)
        store.j25_veste_inspected = store.j25_veste_inspected + [zone_id]
        if len(store.j25_veste_inspected) == 3:
            _j25_focus(view)

    def _j25_capture_photo(view):
        # Une vue indépendante fige exactement le cadrage au déclenchement.
        renpy.set_screen_variable("snapshot", _J25View(view.zoom, view.center))
        renpy.set_screen_variable("phase", "flash")
        renpy.sound.play("audio/sfx_photo.mp3")

    def _j25_pan(view):
        # Pas dépendant de la fréquence du timer ; pause après un menu/load.
        now = _j25_time.monotonic()
        previous = getattr(view, "tick", now)
        view.tick = now
        dt = min(max(now - previous, 0.0), 0.05)
        mx, my = renpy.get_mouse_pos()
        dx = -1 if mx < 150 else (1 if mx > 1770 else 0)
        dy = -1 if my < 120 else (1 if my > 960 else 0)
        view.center = (
            _j25_clamp_center(view.center[0] + dx * dt * 0.22, view.zoom),
            _j25_clamp_center(view.center[1] + dy * dt * 0.22, view.zoom),
        )
        renpy.redraw(view, 0)

    class _J25Knocks(object):
        def __init__(self):
            self.reset()

        def reset(self):
            self.count = 0
            self.last = None
            self.feedback = "Trois coups rapprochés, puis deux coups espacés."
            self.failed = False

        def __getstate__(self):
            # Une sauvegarde au milieu du rythme reprend au premier coup.
            # L'horloge système n'a aucun sens après un chargement.
            return {"count": 0, "last": None, "failed": False,
                    "feedback": "Trois coups rapprochés, puis deux coups espacés."}

        def limits(self):
            return (0.12, 0.48) if self.count < 3 else (0.65, 1.50)

        def hit(self, now):
            if self.count >= 5 or self.failed:
                return
            if self.last is not None:
                low, high = self.limits()
                gap = now - self.last
                if not low <= gap <= high:
                    self.failed = True
                    self.feedback = "Trop vite." if gap < low else "Trop tard."
                    return
            self.last = now
            self.count += 1
            self.feedback = "Encore un coup rapide." if self.count < 3 else "Attends un peu avant le prochain coup."
            if self.count == 5:
                self.feedback = "C'est le bon rythme."

        def tick(self, now):
            if self.last is not None and 0 < self.count < 5 and not self.failed:
                if now - self.last > self.limits()[1]:
                    self.failed = True
                    self.feedback = "Trop tard. Reprends depuis le premier coup."

    def _j25_knock_hit(state):
        if state.failed or state.count >= 5:
            return
        renpy.sound.play("audio/sfx_knock.mp3")
        state.hit(_j25_time.monotonic())
        renpy.restart_interaction()

    def _j25_knock_tick(state):
        state.tick(_j25_time.monotonic())
        renpy.restart_interaction()


screen _j25_veste_screen(view):
    modal True
    zorder 220
    default hovered = None
    default reaction = "Il faut trouver où le tissu aurait pu s'arracher."

    for zone_id, rect, center, comment index zone_id in _J25_VESTE_ZONES:
        $ hitbox = _j25_veste_screen_rect(rect)
        button:
            xpos hitbox[0] ypos hitbox[1] xsize hitbox[2] ysize hitbox[3]
            padding (0, 0)
            background None
            hover_background None
            sensitive len(j25_veste_inspected) < 3
            hovered [SetScreenVariable("hovered", zone_id), Function(_j25_focus, view, center)]
            unhovered [SetScreenVariable("hovered", None), Function(_j25_focus, view)]
            action NullAction()
        if hovered == zone_id and len(j25_veste_inspected) < 3:
            timer 0.9 action Function(_j25_veste_complete, view, zone_id, comment)
        # Reflet discret au centre des zones encore à examiner.
        # Le marqueur disparaît au survol pour laisser voir le tissu.
        if zone_id not in j25_veste_inspected and hovered != zone_id:
            text "✦":
                xpos (hitbox[0] + hitbox[2] // 2)
                ypos (hitbox[1] + hitbox[3] // 2)
                xanchor 0.5 yanchor 0.5
                size 18 color "#D8F3E8"
                at _j25_veste_sparkle((0.0, 0.85, 1.7)[("devant", "manche", "poignet").index(zone_id)])

    frame:
        xpos 50 ypos 35 padding (24, 16)
        background Solid("#07121CEE")
        vbox:
            spacing 6
            text _("EXAMINER LA VESTE") size 30 color "#DDF8FF"
            text _("Survole les vêtements pour les observer de plus près.") size 23 color "#ACBDC8"
            text _("Détails examinés : [len(j25_veste_inspected)] / 3") size 22 color "#5CD3FF"

    frame:
        xpos 180 ypos 865 xsize 1560 ysize 170 padding (30, 20)
        background Solid("#07121CEE")
        vbox:
            spacing 10
            text "NOAM" size 27 color "#5CD3FF" font "fonts/Rajdhani-SemiBold.ttf"
            text _(reaction) size 29 color "#F1F6F8" xmaximum 1470

    if len(j25_veste_inspected) == 3:
        timer 2.0 action Return(list(j25_veste_inspected))


screen _j25_photo_screen(view):
    modal True
    zorder 220
    default phase = "camera"
    default snapshot = None

    if phase == "camera":
        timer 0.033 repeat True action Function(_j25_pan, view)
        key "K_SPACE" action Function(_j25_capture_photo, view)
        key "K_RETURN" action Function(_j25_capture_photo, view)

    if phase == "camera":
        # Coins du viseur et réticule, sans nouvel asset.
        for cx, cy, sx, sy in ((120, 140, 1, 1), (1800, 140, -1, 1), (120, 820, 1, -1), (1800, 820, -1, -1)):
            add Solid("#E7F7EECC") xpos (cx if sx > 0 else cx - 85) ypos cy xsize 85 ysize 4
            add Solid("#E7F7EECC") xpos cx ypos (cy if sy > 0 else cy - 85) xsize 4 ysize 85
        add Solid("#E7F7EEAA") xpos 940 ypos 539 xsize 40 ysize 2
        add Solid("#E7F7EEAA") xpos 959 ypos 520 xsize 2 ysize 40
    
        frame:
            xpos 55 ypos 35 padding (22, 14)
            background Solid("#07121CEE")
            text _("TABLETTE / APPAREIL PHOTO — ZOOM ×2,2") size 28 color "#DDF8FF"
        frame:
            xpos 280 ypos 920 xsize 1360 padding (24, 18)
            background Solid("#07121CEE")
            vbox:
                spacing 7
                text _("Déplace le curseur vers les bords pour ajuster le cadrage.") xalign 0.5 size 26 color "#F1F6F8"
                text _("ESPACE ou ENTRÉE : prendre la photo") xalign 0.5 size 28 color "#5CD3FF"
    elif phase == "flash":
        add Solid("#FFFFFF") at _j25_shutter_flash
        timer 0.12 action SetScreenVariable("phase", "preview")
    else:
        add Solid("#03070DBB")
        frame at _j25_print_in:
            align (0.5, 0.5)
            xsize 1156 ysize 724
            padding (18, 18)
            background Solid("#ECE8DC")
            vbox:
                spacing 18
                add Transform(snapshot, crop=(0, 0, 1920, 1080), xysize=(1120, 630))
                text _("PHOTO ENREGISTRÉE") xalign 0.5 size 24 color "#25333B" font "fonts/Rajdhani-SemiBold.ttf" kerning 3
        timer 1.0 action Return((view.center[0], view.center[1], view.zoom))


# Un éclat court, désynchronisé entre les trois emplacements.
# Une faible opacité évite l'effet « bouton clignotant » sur le corps.
transform _j25_veste_sparkle(delay=0.0):
    alpha 0.0
    pause delay
    ease 0.32 alpha 0.55 zoom 1.12
    ease 0.55 alpha 0.0 zoom 0.94
    pause (2.5 - delay)
    repeat


transform _j25_shutter_flash:
    alpha 0.95
    linear 0.12 alpha 0.0

transform _j25_print_in:
    rotate -2.0
    zoom 1.035
    ease 0.18 zoom 1.0

transform _j25_beat_glow:
    alpha 0.9
    ease 0.28 alpha 0.25


screen _j25_knock_screen():
    modal True
    zorder 220
    default rhythm = _J25Knocks()
    timer 0.04 repeat True action Function(_j25_knock_tick, rhythm)

    if rhythm.count == 5:
        timer 0.45 action Return(True)
    elif not rhythm.failed:
        key "K_SPACE" action Function(_j25_knock_hit, rhythm)
        key "mousedown_1" action Function(_j25_knock_hit, rhythm)

    add Solid("#02081155")
    text _("CHAMBRE D'IRIS"):
        xpos 160 ypos 150 size 23 kerning 5 color "#A5BAC0"
        font "fonts/Rajdhani-SemiBold.ttf"
    text _("Le signal"):
        xpos 155 ypos 187 size 70 color "#EEF2EA"
        font "fonts/Rajdhani-SemiBold.ttf"
    add Solid("#86BDB7") xpos 160 ypos 282 xsize 60 ysize 3
    text _("Trois coups rapides. Deux coups lents."):
        xpos 160 ypos 310 size 28 color "#C3D1D0"

    frame:
        xpos 300 ypos 580 xsize 1320 ysize 330
        background Solid("#081117E8") padding (0, 0)
        text _("RAPIDES") xpos 190 ypos 28 size 18 kerning 4 color "#849B9F"
        text _("LENTS") xpos 845 ypos 28 size 18 kerning 4 color "#849B9F"
        add Solid("#385052") xpos 130 ypos 142 xsize 1060 ysize 2
        add Solid("#385052") xpos 665 ypos 70 xsize 1 ysize 110
        for i index (i, i < rhythm.count) in range(5):
            $ bx = (180, 360, 540, 840, 1100)[i]
            $ done = i < rhythm.count
            $ active = i == rhythm.count and not rhythm.failed
            $ ink = "#9FDFCA" if done else ("#F0E3BD" if active else "#536A72")
            if done:
                add Solid("#79D8BD") xpos (bx - 38) ypos 135 xsize 76 ysize 17 at _j25_beat_glow
            text ("-" if i < 3 else "---"):
                xpos bx ypos 95 xanchor 0.5 size 60 color ink
                font "fonts/Rajdhani-SemiBold.ttf"
            text ("%02d" % (i + 1)):
                xpos bx ypos 176 xanchor 0.5 size 17 color ink
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            if active:
                add Solid("#F0E3BD") xpos (bx - 3) ypos 76 xsize 6 ysize 6

        if 0 < rhythm.count < 5 and not rhythm.failed:
            $ elapsed = max(0.0, _j25_time.monotonic() - rhythm.last)
            $ low, high = rhythm.limits()
            add Solid("#263C44") xpos 130 ypos 230 xsize 1060 ysize 4
            add Solid("#A9D6C877") xpos (130 + int(1060 * low / high)) ypos 230 xsize (1060 - int(1060 * low / high)) ysize 4
            add Solid("#F0E3BD") xpos (130 + int(1060 * min(elapsed / high, 1.0))) ypos 223 xsize 3 ysize 18
            text (_("MAINTENANT") if low <= elapsed <= high else _("ATTENDS")):
                xalign 0.5 ypos 263 size 22 kerning 3 color "#F0E3BD"
                font "fonts/Rajdhani-SemiBold.ttf"
        else:
            text _(rhythm.feedback):
                xalign 0.5 ypos 254 size 24 color ("#EBA69A" if rhythm.failed else "#A9D6C8")

    if rhythm.failed:
        textbutton _("RECOMMENCER  /  ENTRÉE"):
            xalign 0.5 ypos 940 padding (24, 10)
            background None hover_background Solid("#A9D6C81A")
            text_size 22 text_color "#D4E7E1" text_hover_color "#FFFFFF"
            text_font "fonts/Rajdhani-SemiBold.ttf" text_kerning 2
            action Function(rhythm.reset)
        key "K_RETURN" action Function(rhythm.reset)
    else:
        text _("ESPACE OU CLIC  ·  RELÂCHE ENTRE CHAQUE COUP"):
            xalign 0.5 ypos 960 size 19 kerning 2 color "#A7BABC"
            font "fonts/Rajdhani-SemiBold.ttf"


label j25_examiner_veste:
    $ j25_veste_inspected = []
    $ _j25_view = _J25View(zoom=_J25_VESTE_BASE_ZOOM, center=_J25_VESTE_BASE_CENTER)
    show expression _j25_view as j25_inspection_view onlayer master
    call screen _j25_veste_screen(_j25_view)
    $ j25_veste_inspected = _return
    hide j25_inspection_view onlayer master
    $ _j25_view = None
    return
    # Durée : environ 30 secondes.

label j25_prendre_photo:
    $ _j25_view = _J25View(zoom=2.2, center=(0.50, 0.56))
    show expression _j25_view as j25_photo_view onlayer master
    call screen _j25_photo_screen(_j25_view)
    $ j25_photo_frame = _return
    hide j25_photo_view onlayer master
    $ _j25_view = None
    return
    # Durée : environ 15 secondes.

label j25_toquer_iris:
    call screen _j25_knock_screen
    $ j25_knock_success = _return
    return
    # Durée : environ 10 secondes, hors nouvelles tentatives.
