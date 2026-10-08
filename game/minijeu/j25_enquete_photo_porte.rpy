# Jour 25 : comparer la veste, photographier le corps, rejoindre Iris.
# Le fond reste sur master : la lampe du calque lighting reste active.
default j25_veste_inspected = []
default j25_photo_frame = None
default j25_knock_success = False

init python:
    import time as _j25_time

    # Coordonnées dans le cadre 1920 × 1080 de bg_cg040.
    _J25_VESTE_ZONES = (
        ("devant", (730, 544, 160, 66), (0.42, 0.53),
         "La couleur est exactement la même. Mais ici, il ne manque rien."),
        ("manche", (690, 610, 122, 66), (0.39, 0.59),
         "Non... Le tissu de la manche est intact. Pas de déchirure."),
        ("poignet", (814, 650, 66, 52), (0.44, 0.62),
         "La couture tient encore. Le morceau qu'on a trouvé ne vient pas de là."),
    )

    def _j25_clamp_center(value, zoom):
        margin = 0.5 / zoom
        return max(margin, min(1.0 - margin, value))

    class _J25View(renpy.Displayable):
        def __init__(self, zoom=1.0, center=(0.5, 0.5), **kwargs):
            super(_J25View, self).__init__(**kwargs)
            self.zoom = zoom
            self.center = center
            self.child = Transform("bg_cg040", xysize=(1920, 1080))

        def render(self, width, height, st, at):
            scaled = renpy.render(Transform(self.child, zoom=self.zoom), 1920, 1080, st, at)
            cx = _j25_clamp_center(self.center[0], self.zoom)
            cy = _j25_clamp_center(self.center[1], self.zoom)
            result = renpy.Render(1920, 1080)
            result.blit(scaled, (int(960 - cx * 1920 * self.zoom), int(540 - cy * 1080 * self.zoom)))
            return result

        def visit(self):
            return [self.child]

    def _j25_focus(view, center=None):
        view.zoom = 2.0 if center else 1.0
        view.center = center or (0.5, 0.5)
        renpy.redraw(view, 0)

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
        button:
            xpos rect[0] ypos rect[1] xsize rect[2] ysize rect[3]
            padding (0, 0)
            background None
            hover_background None
            hovered [SetScreenVariable("hovered", zone_id), SetScreenVariable("reaction", comment), Function(_j25_focus, view, center)]
            unhovered [SetScreenVariable("hovered", None), Function(_j25_focus, view)]
            action NullAction()
        if hovered == zone_id and zone_id not in j25_veste_inspected:
            timer 0.7 action SetVariable("j25_veste_inspected", j25_veste_inspected + [zone_id])

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
        textbutton _("TERMINER L'EXAMEN"):
            xpos 1450 ypos 55 padding (22, 16)
            text_size 24 text_color "#DDF8FF"
            background Solid("#07121CEE") hover_background Solid("#19445DEE")
            action Return(list(j25_veste_inspected))


screen _j25_photo_screen(view):
    modal True
    zorder 220
    default captured = False

    if not captured:
        timer 0.033 repeat True action Function(_j25_pan, view)
        key "K_SPACE" action [SetScreenVariable("captured", True), Play("sound", "audio/sfx_photo.mp3")]
        key "K_RETURN" action [SetScreenVariable("captured", True), Play("sound", "audio/sfx_photo.mp3")]
    else:
        add Solid("#FFFFFFCC")
        timer 0.18 action Return((view.center[0], view.center[1], view.zoom))

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

    frame:
        xpos 280 ypos 220 xsize 1360 padding (45, 34)
        background Solid("#07121CEE")
        vbox:
            spacing 25
            text _("LE SIGNAL D'IRIS") xalign 0.5 size 40 color "#DDF8FF" font "fonts/Rajdhani-SemiBold.ttf"
            text _("ESPACE ou clic : toquer. Relâche entre chaque coup.") xalign 0.5 size 25 color "#ACBDC8"
            hbox:
                xalign 0.5 spacing 28
                for i in range(5):
                    frame:
                        xsize 175 ysize 130 padding (0, 0)
                        background Solid("#205E6588" if i < rhythm.count else "#14232BCC")
                        vbox:
                            align (0.5, 0.5) spacing 4
                            text ("-" if i < 3 else "---") xalign 0.5 size 55 color ("#8FFFC7" if i < rhythm.count else "#DDF8FF")
                            text (_("RAPIDE") if i < 3 else _("LENT")) xalign 0.5 size 21 color "#ACBDC8"

            if 0 < rhythm.count < 5 and not rhythm.failed:
                $ elapsed = max(0.0, _j25_time.monotonic() - rhythm.last)
                $ low, high = rhythm.limits()
                bar value min(elapsed, high) range high xsize 800 xalign 0.5 ysize 15
                text (_("FRAPPE MAINTENANT") if low <= elapsed <= high else _("ATTENDS…")) xalign 0.5 size 26 color "#8FFFC7"
            text _(rhythm.feedback) xalign 0.5 size 26 color ("#FFAAA4" if rhythm.failed else "#F1F6F8")
            if rhythm.failed:
                textbutton _("RECOMMENCER"):
                    xalign 0.5 text_size 28 text_color "#5CD3FF"
                    action Function(rhythm.reset)
                key "K_RETURN" action Function(rhythm.reset)


label j25_examiner_veste:
    $ j25_veste_inspected = []
    $ _j25_view = _J25View()
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
