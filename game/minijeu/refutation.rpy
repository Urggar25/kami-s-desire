# ============================================================
# minijeu/refutation.rpy — Mini-jeu « Réfutation »
#
# Mécanique inspirée des débats non-stop (affirmations qui défilent,
# failles à viser, argument à injecter), habillée dans la DA de
# Kami's Desires : HUD holographique cyan, cadres chanfreinés,
# failles ambre, sanctions de Kami en magenta.
#
#   $ refutation_register("id", title=..., statements=[...], ...)
#   call refutation_run("id")   ->  _return = ("success"|"failure", fragment_id)
#
# Les affirmations marquent leurs failles avec [[ ]] :
#   _("Il n'y a [[aucune règle]] qui nous interdit d'appeler l'extérieur !")
# Chaque faille est identifiée par (index de l'affirmation, index de la faille).
# ============================================================

init -1 python:
    import re as _rf_re
    import math as _rf_math
    import time as _rf_time

    REFUTATIONS = {}

    RF_CYAN = "#5cd3ff"
    RF_AMBER = "#ffb84d"
    RF_KAMI = "#ff2e8a"
    RF_ASSETS = "minijeu/refutation_assets/"

    RF_CHIP_X = 40
    RF_CHIP_Y = 706
    RF_CHIP_W = 540
    RF_CHIP_H = 64
    RF_CHIP_GAP = 8

    _RF_FAULT = _rf_re.compile(r"\[\[(.+?)\]\]")

    def refutation_register(refutation_id, **data):
        """Déclare un duel de réfutation.

        Champs : title, location, bg, statements [(speaker, expr, texte)],
        fragments [(id, libellé)], solution {(stmt, faille): fragment_id},
        miss (fonction (fragment, stmt, faille) -> réplique) ou dict,
        success_text, lives (3), line_time (5.0 s), time_limit (None).
        """
        REFUTATIONS[refutation_id] = data

    def rf_markup(text):
        """Convertit [[faille]] en hyperliens cliquables, après traduction."""
        text = kd_tr(text)
        counter = [0]

        def _sub(match):
            index = counter[0]
            counter[0] += 1
            return "{a=rf:%d}%s{/a}" % (index, match.group(1))

        return _RF_FAULT.sub(_sub, text)

    def rf_fault_style(target):
        return style.rf_fault

    def rf_fault_hovered(target):
        state = getattr(_rf_runtime, "state", None)
        if state is not None:
            state.hover = target is not None
            renpy.restart_interaction()
        return None

    def rf_fault_clicked(target):
        state = getattr(_rf_runtime, "state", None)
        if state is None or not str(target).startswith("rf:"):
            return None
        state.fire(int(str(target)[3:]))
        renpy.restart_interaction()
        return None

    class _RFRuntime(object):
        pass

    _rf_runtime = _RFRuntime()

    class RFState(object):
        def __init__(self, refutation_id):
            data = REFUTATIONS[refutation_id]
            self.rid = refutation_id
            self.count = len(data["statements"])
            self.lives_max = data.get("lives", 3)
            self.lives = self.lives_max
            self.line_time = data.get("line_time", 5.0)
            self.time_limit = data.get("time_limit", None)
            self.line = 0
            self.line_t = 0.0
            self.total = 0.0
            self.intro = 1.4
            self.fragment = 0
            self.locked_hint = ""
            self.hover = False
            self.shot = None
            self.shot_t = 0.0
            self.shot_xy = (960, 400)
            self.shot_origin = (RF_CHIP_X + RF_CHIP_W, RF_CHIP_Y)
            self.retort = ""
            self.last_fragment = None
            self.result = None
            self._clock = None
            _rf_runtime.state = self

        @property
        def data(self):
            return REFUTATIONS[self.rid]

        def fragment_id(self, index=None):
            frags = self.data["fragments"]
            return frags[self.fragment if index is None else index][0]

        def fragment_available(self, index):
            """Conserve les indices en visuel, mais interdit les preuves non acquises."""
            item = self.data["fragments"][index]
            if len(item) < 3 or not item[2]:
                return True
            requirement = item[2]
            if callable(requirement):
                return bool(requirement())
            if isinstance(requirement, str):
                return bool(getattr(store, requirement, False))
            return bool(requirement)

        def select(self, index):
            if self.shot is not None:
                return
            index = index % len(self.data["fragments"])
            if self.fragment_available(index):
                self.fragment = index
                self.locked_hint = ""
            else:
                self.locked_hint = _("Argument non débloqué")

        def cycle(self, step):
            for n in range(1, len(self.data["fragments"]) + 1):
                target = (self.fragment + step * n) % len(self.data["fragments"])
                if self.fragment_available(target):
                    self.select(target)
                    break

        def chip_y(self, index):
            return RF_CHIP_Y + index * (RF_CHIP_H + RF_CHIP_GAP)

        def tick(self, dt):
            # Temps réel (et non nombre de déclenchements du timer) : le
            # rythme reste juste même si l'affichage ralentit.
            now = _rf_time.time()
            if self._clock is not None:
                dt = min(0.25, max(0.0, now - self._clock))
            self._clock = now
            if self.result is not None:
                return self.result
            self.total += dt
            if self.intro > 0:
                self.intro -= dt
                return None
            if self.shot is not None:
                self.shot_t += dt
                if self.shot_t >= 1.05:
                    if self.shot == "hit":
                        self.result = ("success", self.last_fragment)
                    elif self.lives <= 0:
                        self.result = ("failure", self.last_fragment)
                    else:
                        self.shot = None
                        self.line_t = 0.0
                    if self.result is not None:
                        return self.result
                return None
            self.line_t += dt
            if self.line_t >= self.line_time:
                self.line = (self.line + 1) % self.count
                self.line_t = 0.0
            if self.time_limit and self.total >= self.time_limit:
                self.result = ("failure", self.last_fragment)
                return self.result
            return None

        def miss_text(self, frag, stmt, fault):
            miss = self.data.get("miss")
            if callable(miss):
                return miss(frag, stmt, fault)
            if isinstance(miss, dict):
                for key in ((frag, stmt, fault), (stmt, fault), frag, "default"):
                    if key in miss:
                        return miss[key]
            return _("Ça ne prouve rien.")

        def fire(self, fault):
            if self.shot is not None or self.intro > 0:
                return
            if not self.fragment_available(self.fragment):
                self.locked_hint = _("Argument non débloqué")
                return
            frag = self.fragment_id()
            self.last_fragment = frag
            self.shot_xy = renpy.get_mouse_pos()
            self.shot_origin = (RF_CHIP_X + RF_CHIP_W, self.chip_y(self.fragment) + RF_CHIP_H // 2)
            self.shot_t = 0.0
            if self.data["solution"].get((self.line, fault)) == frag:
                self.shot = "hit"
                renpy.sound.play("audio/sfx_interrupt_impact.wav", channel="kd_fx")
            else:
                self.shot = "miss"
                self.lives -= 1
                self.retort = self.miss_text(frag, self.line, fault)
                renpy.sound.play("audio/trailer/trl_glitch_stutter.wav", channel="kd_fx")

        def beam(self):
            (x0, y0), (x1, y1) = self.shot_origin, self.shot_xy
            length = max(1.0, _rf_math.hypot(x1 - x0, y1 - y0))
            angle = _rf_math.degrees(_rf_math.atan2(y1 - y0, x1 - x0))
            return int((x0 + x1) / 2), int((y0 + y1) / 2), int(length), angle

        def clock(self):
            value = self.total if not self.time_limit else max(0.0, self.time_limit - self.total)
            minutes = int(value // 60)
            return "%02d:%05.2f" % (minutes, value - minutes * 60)

    def rf_reticle_follow(trans, st, at):
        x, y = renpy.get_mouse_pos()
        trans.xpos = x
        trans.ypos = y
        return 0


style rf_fault:
    color RF_AMBER
    hover_color "#ffffff"
    underline True
    bold True


# ------------------------------------------------------------
# Animations
# ------------------------------------------------------------
transform rf_reticle:
    anchor (0.5, 0.5)
    function rf_reticle_follow

transform rf_reticle_hot:
    anchor (0.5, 0.5)
    function rf_reticle_follow
    zoom 1.0
    ease 0.12 zoom 0.72
    ease 0.3 zoom 0.82
    repeat

transform rf_enter_left(d=5.0):
    subpixel True
    rotate_pad False
    alpha 0.0 xoffset -260 rotate -2
    easeout 0.28 alpha 1.0 xoffset 0
    linear (d - 0.5) xoffset 70
    linear 0.22 alpha 0.0

transform rf_enter_right(d=5.0):
    subpixel True
    rotate_pad False
    alpha 0.0 xoffset 260 rotate 1.5
    easeout 0.28 alpha 1.0 xoffset 0
    linear (d - 0.5) xoffset -70
    linear 0.22 alpha 0.0

transform rf_enter_zoom(d=5.0):
    subpixel True
    rotate_pad False
    alpha 0.0 zoom 1.35 rotate -1.5
    easeout 0.26 alpha 1.0 zoom 1.0
    linear (d - 0.48) zoom 0.96
    linear 0.22 alpha 0.0

transform rf_enter_rise(d=5.0):
    subpixel True
    rotate_pad False
    alpha 0.0 yoffset 120 rotate -2
    easeout 0.3 alpha 1.0 yoffset 0
    linear (d - 0.52) yoffset -40
    linear 0.22 alpha 0.0

init python:
    RF_ENTRIES = (rf_enter_left, rf_enter_zoom, rf_enter_right, rf_enter_rise)

transform rf_speaker_in:
    subpixel True
    alpha 0.0 xoffset 60
    easeout 0.25 alpha 1.0 xoffset 0

transform rf_scan:
    alpha 0.18
    yoffset -1080
    linear 3.2 yoffset 1080
    repeat

transform rf_intro_title:
    alpha 0.0 zoom 1.4
    easeout 0.18 alpha 1.0 zoom 1.0
    pause 0.95
    linear 0.25 alpha 0.0

transform rf_beam(angle):
    anchor (0.5, 0.5)
    rotate angle
    xzoom 0.0 alpha 1.0
    easeout 0.12 xzoom 1.0
    pause 0.12
    linear 0.25 alpha 0.0

transform rf_impact_ring:
    anchor (0.5, 0.5)
    zoom 0.4 alpha 1.0
    easeout 0.35 zoom 2.2 alpha 0.0

transform rf_flash(a=0.35):
    alpha 0.0
    linear 0.04 alpha a
    linear 0.3 alpha 0.0

transform rf_stamp:
    alpha 0.0 zoom 1.6
    pause 0.12
    easeout 0.12 alpha 1.0 zoom 1.0
    pause 0.6
    linear 0.15 alpha 0.0

transform rf_shatter:
    easeout 0.06 xoffset 18
    easeout 0.06 xoffset -14
    easeout 0.08 xoffset 0
    linear 0.25 alpha 0.0 zoom 1.06

transform rf_shake:
    easeout 0.04 xoffset 14
    easeout 0.04 xoffset -12
    easeout 0.05 xoffset 8
    easeout 0.06 xoffset 0

transform rf_still:
    xoffset 0

transform rf_retort_in:
    alpha 0.0 yoffset 30
    easeout 0.18 alpha 1.0 yoffset 0


# ------------------------------------------------------------
# Écran principal
# ------------------------------------------------------------
screen refutation_screen(refutation_id):
    modal True
    zorder 305

    default rf = RFState(refutation_id)
    $ data = REFUTATIONS[refutation_id]
    $ statement = data["statements"][rf.line]
    $ speaker, speaker_expr = statement[0], statement[1]
    $ speaker_color = kd_char_color(speaker)

    timer 0.04 repeat True action Function(rf.tick, 0.04)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "mousedown_4" action Function(rf.cycle, -1)
    key "mousedown_5" action Function(rf.cycle, 1)
    key "K_UP" action Function(rf.cycle, -1)
    key "K_DOWN" action Function(rf.cycle, 1)
    key "K_q" action Function(rf.cycle, -1)
    key "K_e" action Function(rf.cycle, 1)
    key "pad_leftshoulder_press" action Function(rf.cycle, -1)
    key "pad_rightshoulder_press" action Function(rf.cycle, 1)

    fixed at (rf_shake if rf.shot == "miss" else rf_still):
        # --- Décor du lieu, assombri et balayé par un scan holographique.
        add data.get("bg", "bg_observation") at adaptive_fullscreen
        add Solid("#040914c4")
        add "gui/main_menu_kami/vignette.png"
        add "gui/main_menu_kami/scanlines.png" alpha 0.35
        add Solid(RF_CYAN, xysize=(1920, 2)) at rf_scan

        # --- Locuteur, cadré à droite. Kami n'a pas de sprite humain :
        # afficher son écran de diffusion plutôt qu'une image inexistante.
        for index, entry in enumerate(data["statements"]):
            if rf.line == index and rf.intro <= 0:
                if entry[0] == "kami":
                    add Transform("bg_diffusion_professeur", zoom=0.55) at rf_speaker_in:
                        xpos 1050
                        ypos 110
                else:
                    add Transform(character_image(entry[0], entry[1]), zoom=1.5) at rf_speaker_in:
                        xpos 1060
                        ypos -10

        # --- Bandeau supérieur : locuteur et chrono.
        frame:
            background Frame(RF_ASSETS + "panel.png", 26, 26)
            xpos 40
            ypos 30
            xsize 560
            ysize 104
            padding (30, 14)
            vbox:
                spacing 2
                text kd_display_name(speaker).upper():
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 44
                    color speaker_color
                    kerning 3
                text (_("AFFIRMATION") + "  %d / %d" % (rf.line + 1, rf.count)):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 20
                    color RF_CYAN
                    kerning 2
        hbox:
            xpos 70
            ypos 140
            spacing 8
            for index in range(rf.count):
                add Solid(RF_CYAN if index == rf.line else "#24405a", xysize=(96, 4))

        frame:
            background Frame(RF_ASSETS + "panel.png", 26, 26)
            xpos 1440
            ypos 30
            xsize 440
            ysize 104
            padding (30, 14)
            vbox:
                spacing 0
                text (data.get("title") or _("RÉFUTATION")):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 20
                    color RF_CYAN
                    kerning 2
                text rf.clock():
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 46
                    color "#eef7ff"
        hbox:
            xpos 1452
            ypos 142
            spacing 4
            text _("CRÉDIBILITÉ"):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 18
                color "#8fb4c8"
                yalign 0.5
            null width 8
            for index in range(rf.lives_max):
                if index < rf.lives:
                    add RF_ASSETS + "hex_on.png"
                elif index == rf.lives and rf.shot == "miss":
                    add RF_ASSETS + "hex_lost.png" at rf_flash(1.0)
                else:
                    add RF_ASSETS + "hex_off.png"

        # --- Affirmation en cours, failles cliquables.
        if rf.intro <= 0:
            for index, entry in enumerate(data["statements"]):
                if rf.line == index:
                    frame at RF_ENTRIES[index % len(RF_ENTRIES)](rf.line_time):
                        background Frame(RF_ASSETS + "holo_frame.png", 44, 44)
                        xpos 110
                        ypos 230
                        xmaximum 1100
                        padding (52, 38)
                        text rf_markup(entry[2]):
                            font "fonts/Rajdhani-SemiBold.ttf"
                            size 54
                            color "#ffffff"
                            outlines [(3, "#03070fdd", 0, 0)]
                            line_spacing 6
                            substitute False
                            hyperlink_functions (rf_fault_style, rf_fault_clicked, rf_fault_hovered)
                            at (rf_shatter if rf.shot == "hit" else rf_still)

        # --- Tablette de Noam : fragments d'arguments.
        add RF_ASSETS + "tablet_header.png" xpos RF_CHIP_X ypos (RF_CHIP_Y - 62)
        text _("TABLETTE  //  FRAGMENTS"):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 22
            color RF_CYAN
            kerning 2
            xpos (RF_CHIP_X + 26)
            ypos (RF_CHIP_Y - 48)
        for index, fragment in enumerate(data["fragments"]):
            $ chosen = (index == rf.fragment)
            $ available = rf.fragment_available(index)
            button:
                xpos (RF_CHIP_X + (18 if chosen else 0))
                ypos rf.chip_y(index)
                xysize (RF_CHIP_W, RF_CHIP_H)
                background Frame(RF_ASSETS + ("frag_selected.png" if chosen else "frag_idle.png"), 30, 26)
                hover_background Frame(RF_ASSETS + "frag_selected.png", 30, 26)
                sensitive (rf.shot is None and available)
                action Function(rf.select, index)
                padding (52, 0, 20, 0)
                hbox:
                    yalign 0.5
                    spacing 16
                    text ("%02d" % (index + 1)):
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 22
                        color ("#607080" if not available else (RF_CYAN if chosen else "#6f8ba0"))
                        yalign 0.5
                    text kd_tr(fragment[1]):
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 28
                        color ("#73808c" if not available else ("#ffffff" if chosen else "#b9c9d6"))
                        yalign 0.5
                    if not available:
                        text _("VERROUILLÉ"):
                            size 17
                            color "#ffb84d"
                            yalign 0.5

        text _("MOLETTE OU Q / E : CHANGER DE FRAGMENT     •     CLIC SUR UNE FAILLE : INJECTER"):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 22
            color "#8fb4c8"
            kerning 1
            xpos 640
            ypos 1036

        # --- Tir : faisceau, impact, verdict.
        if rf.shot is not None:
            $ beam_x, beam_y, beam_len, beam_angle = rf.beam()
            $ beam_color = (RF_CYAN if rf.shot == "hit" else RF_KAMI)
            add Solid(beam_color, xysize=(beam_len, 14)) at rf_beam(beam_angle):
                xpos beam_x
                ypos beam_y
                alpha 0.35
            add Solid("#ffffff", xysize=(beam_len, 4)) at rf_beam(beam_angle):
                xpos beam_x
                ypos beam_y
            add RF_ASSETS + "reticle.png" at rf_impact_ring:
                xpos rf.shot_xy[0]
                ypos rf.shot_xy[1]
            add Solid("#ffffff" if rf.shot == "hit" else RF_KAMI) at rf_flash(0.3 if rf.shot == "hit" else 0.22)

            frame at rf_stamp:
                background Frame(RF_ASSETS + "panel.png", 26, 26)
                xalign 0.36
                ypos 520
                padding (46, 18)
                text (_("FAILLE CONFIRMÉE") if rf.shot == "hit" else _("INCOHÉRENT")):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 80
                    kerning 6
                    color ("#ffffff" if rf.shot == "hit" else RF_KAMI)
                    outlines [(3, beam_color, 0, 0)]

            if rf.shot == "miss":
                frame at rf_retort_in:
                    background Frame(RF_ASSETS + "panel.png", 26, 26)
                    xpos 640
                    ypos 900
                    xsize 1240
                    padding (34, 18)
                    vbox:
                        spacing 4
                        text kd_display_name(speaker).upper():
                            font "fonts/Rajdhani-SemiBold.ttf"
                            size 24
                            color speaker_color
                        text kd_tr(rf.retort):
                            size 30
                            color "#eef7ff"

        # --- Ouverture.
        if rf.intro > 0:
            vbox at rf_intro_title:
                xalign 0.45
                yalign 0.42
                spacing 10
                text (data.get("title") or _("RÉFUTATION")):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 110
                    color "#ffffff"
                    kerning 10
                    outlines [(4, RF_CYAN, 0, 0)]
                    xalign 0.5
                text _("Trouve la faille. Injecte le bon fragment."):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 34
                    color RF_AMBER
                    xalign 0.5

    if rf.shot is None and rf.intro <= 0:
        add RF_ASSETS + "reticle.png" at (rf_reticle_hot if rf.hover else rf_reticle)


label refutation_run(refutation_id):
    play kd_fx "audio/trailer/trl_riser_short.wav"
    call screen refutation_screen(refutation_id)
    $ _rf_runtime.state = None
    return _return
