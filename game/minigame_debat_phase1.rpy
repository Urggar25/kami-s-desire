# Mini-jeu : Débat - Phase 1 (Ouverture)

default debat_phase1_slots = []
default debat_phase1_words = []
default debat_phase1_success = False
default debat_phase1_slot_layout = []
default debat_phase1_target = []
default debat_phase1_resets = 0
default debat_phase1_wrong_drops = 0
default debat_phase1_last_result = {}
default player_kamyz = 0

define sfx_victory = "audio/sfx_clap.mp3"

init python:
    import random

    DEBAT_PHASE1_TARGET = [
        "Autoriser","le","transport,","la","vente","et","l’échange","de",
        "marchandises.","Le","système","actuel","de","distribution","de","denrées",
        "est","aboli.",
    ]

    DEBAT_PHASE1_FLOAT_POSITIONS = [
        (90, 170), (260, 140), (430, 180), (620, 145), (800, 180), (980, 150),
        (1140, 175), (1320, 145), (1490, 175), (170, 290), (360, 265), (550, 300),
        (750, 270), (940, 295), (1130, 265), (1310, 300), (1500, 270), (120, 410),
        (300, 385), (500, 420), (700, 390), (900, 420), (1100, 390), (1300, 420),
    ]

    DEBAT_PHASE1_BANK_Y = 344
    DEBAT_PHASE1_WORD_BANK_START_X = 86
    DEBAT_PHASE1_WORD_BANK_START_Y = 418
    DEBAT_PHASE1_WORD_BANK_ROW_MAX_WIDTH = 1748
    DEBAT_PHASE1_WORD_BANK_GAP = 16
    DEBAT_PHASE1_WORD_BANK_ROW_SPACING = 76

    DEBAT_PHASE1_SLOT_START_X = 86
    DEBAT_PHASE1_SLOT_START_Y = 742
    DEBAT_PHASE1_SLOT_GAP = 10
    DEBAT_PHASE1_SLOT_ROW_SPACING = 78
    DEBAT_PHASE1_SLOT_MIN_WIDTH = 54
    DEBAT_PHASE1_SLOT_TEXT_PADDING_X = 28
    DEBAT_PHASE1_SLOT_CHAR_WIDTH = 13.5
    DEBAT_PHASE1_SLOT_HEIGHT = 58
    DEBAT_PHASE1_SLOT_ROW_MAX_WIDTH = 1748
    DEBAT_PHASE1_TOTAL_TIME = 180
    DEBAT_PHASE1_COMMENT_THRESHOLDS = [120, 60, 30, 10]
    DEBAT_PHASE1_PRESSURE_COMMENTS = {
        120: [
            "Kami : Deux minutes. Vous êtes déjà en retard sur mes calculs.",
            "Kami : 120 secondes, et toujours ce chaos. Charmant.",
            "Kami : Vous sentez la pression ? Moi, j'appelle ça une statistique.",
        ],
        60: [
            "Kami : Une minute. J'espère que vous aimez finir dans la panique.",
            "Kami : 60 secondes. Je lance déjà les paris sur votre échec.",
            "Kami : Tic tac. C'est là que les erreurs deviennent irréversibles.",
        ],
        30: [
            "Kami : 30 secondes. Même mes protocoles ont plus de sang-froid.",
            "Kami : Trente secondes. Vous devriez déjà avoir terminé.",
            "Kami : Plus que 30 secondes. Essayez de ne pas tout saboter.",
        ],
        10: [
            "Kami : 10 secondes. Oui, c'est exactement aussi catastrophique que prévu.",
            "Kami : Dix secondes. Respirez... enfin non, perdez plutôt du temps.",
            "Kami : 10 secondes. Le stress vous va si bien.",
        ],
    }

    def debat_phase1_word_width(word_text):
        translated_word = kd_tr(word_text)
        estimated = DEBAT_PHASE1_SLOT_TEXT_PADDING_X + int(len(translated_word) * DEBAT_PHASE1_SLOT_CHAR_WIDTH)
        return max(DEBAT_PHASE1_SLOT_MIN_WIDTH, estimated)

    def debat_phase1_get_slot_width(slot_index, slot_word_id):
        if slot_word_id is None:
            return debat_phase1_word_width(store.debat_phase1_target[slot_index])

        word_text = store.debat_phase1_words[slot_word_id]["text"]
        return debat_phase1_word_width(word_text)

    def debat_phase1_refresh_slot_layout():
        layout = []
        current_x = DEBAT_PHASE1_SLOT_START_X
        current_y = DEBAT_PHASE1_SLOT_START_Y

        for slot_index, slot_word_id in enumerate(store.debat_phase1_slots):
            slot_width = debat_phase1_get_slot_width(slot_index, slot_word_id)
            row_end = DEBAT_PHASE1_SLOT_START_X + DEBAT_PHASE1_SLOT_ROW_MAX_WIDTH

            if current_x != DEBAT_PHASE1_SLOT_START_X and (current_x + slot_width) > row_end:
                current_x = DEBAT_PHASE1_SLOT_START_X
                current_y += DEBAT_PHASE1_SLOT_ROW_SPACING

            layout.append((current_x, current_y, slot_width, DEBAT_PHASE1_SLOT_HEIGHT))
            current_x += slot_width + DEBAT_PHASE1_SLOT_GAP

        store.debat_phase1_slot_layout = layout

    def debat_phase1_find_word_slot(word_id):
        for i, slot_word_id in enumerate(store.debat_phase1_slots):
            if slot_word_id == word_id:
                return i
        return None

    def debat_phase1_update_success():
        if len(store.debat_phase1_slots) != len(store.debat_phase1_target):
            store.debat_phase1_success = False
            return

        for i, expected_word in enumerate(store.debat_phase1_target):
            word_id = store.debat_phase1_slots[i]
            if word_id is None:
                store.debat_phase1_success = False
                return

            actual_word = store.debat_phase1_words[word_id]["text"]
            if actual_word != expected_word:
                store.debat_phase1_success = False
                return

        if not store.debat_phase1_success:
            renpy.play("audio/sfx_victory.mp3", channel="sound")
            store.debat_phase1_success = True
            fa_fx_event("on_success")
        store.debat_phase1_success = True

    def debat_phase1_setup(target=None, count_reset=False):
        if target is not None:
            store.debat_phase1_target = list(target)
        elif not store.debat_phase1_target:
            store.debat_phase1_target = list(DEBAT_PHASE1_TARGET)

        if count_reset:
            store.debat_phase1_resets += 1
        else:
            store.debat_phase1_resets = 0
            store.debat_phase1_wrong_drops = 0

        tgt = store.debat_phase1_target
        indexed_words = list(enumerate(tgt))  # (orig_id, text)
        random.shuffle(indexed_words)

        store.debat_phase1_words = [None for _ in tgt]

        current_x = DEBAT_PHASE1_WORD_BANK_START_X
        current_y = DEBAT_PHASE1_WORD_BANK_START_Y
        row_end = DEBAT_PHASE1_WORD_BANK_START_X + DEBAT_PHASE1_WORD_BANK_ROW_MAX_WIDTH

        for i, (orig_id, text) in enumerate(indexed_words):
            word_width = debat_phase1_word_width(text)

            if current_x != DEBAT_PHASE1_WORD_BANK_START_X and (current_x + word_width) > row_end:
                current_x = DEBAT_PHASE1_WORD_BANK_START_X
                current_y += DEBAT_PHASE1_WORD_BANK_ROW_SPACING

            hx = current_x
            hy = current_y
            current_x += word_width + DEBAT_PHASE1_WORD_BANK_GAP

            store.debat_phase1_words[orig_id] = {
                "id": orig_id,
                "text": text,
                "home_x": hx,
                "home_y": hy,
            }

        store.debat_phase1_slots = [None for _ in tgt]
        debat_phase1_refresh_slot_layout()
        store.debat_phase1_success = False

        renpy.block_rollback()

    def debat_phase1_compute_score(time_left, total_time):
        """Score sur 1000 : temps restant + propreté du placement."""
        time_part = 700.0 * max(0, time_left) / float(max(1, total_time))
        clean_part = max(0.0, 300.0 - 40.0 * store.debat_phase1_wrong_drops - 80.0 * store.debat_phase1_resets)
        return int(round(time_part + clean_part))

    def debat_phase1_handle_drop(word_id, drags, drop):
        if drop is None:
            return

        target_name = getattr(drop, "drag_name", "")
        current_slot = debat_phase1_find_word_slot(word_id)

        if target_name == "word_bank":
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = None
                debat_phase1_update_success()
                debat_phase1_refresh_slot_layout()
                renpy.block_rollback()
                renpy.restart_interaction()
            return

        if not target_name.startswith("slot_"):
            return

        try:
            target_slot = int(target_name.split("_", 1)[1])
        except Exception:
            return

        occupant = store.debat_phase1_slots[target_slot]
        renpy.play("audio/sfx_beep.mp3", channel="sound")

        if current_slot is not None:
            store.debat_phase1_slots[current_slot] = None

        store.debat_phase1_slots[target_slot] = word_id

        if store.debat_phase1_words[word_id]["text"] != store.debat_phase1_target[target_slot]:
            store.debat_phase1_wrong_drops += 1
            fa_fx_event("on_drop", False)
        else:
            fa_fx_event("on_drop", True)

        if occupant is not None and occupant != word_id:
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = occupant

        debat_phase1_update_success()
        debat_phase1_refresh_slot_layout()
        renpy.block_rollback()
        renpy.restart_interaction()

    def debat_phase1_pick_pressure_comment(threshold):
        comments = DEBAT_PHASE1_PRESSURE_COMMENTS.get(threshold, [])
        if not comments:
            return ""
        return random.choice(comments)

    def debat_phase1_calculate_kamyz(time_left):
        clamped_time = max(0, min(DEBAT_PHASE1_TOTAL_TIME, int(time_left)))
        return int(round(500.0 * clamped_time / float(DEBAT_PHASE1_TOTAL_TIME)))

    def debat_phase1_format_time(seconds):
        seconds = int(max(0, seconds))
        return "%02d:%02d" % (seconds // 60, seconds % 60)


transform debat_phase1_float_a:
    yoffset 0
    ease 2.0 yoffset -8
    ease 2.0 yoffset 0
    repeat

transform debat_phase1_float_b:
    yoffset 0
    ease 2.5 yoffset -10
    ease 2.5 yoffset 0
    repeat

transform debat_phase1_float_c:
    yoffset 0
    ease 2.2 yoffset -6
    ease 2.2 yoffset 0
    repeat

transform fa_tile_hover:
    zoom 1.0
    ease 0.12 zoom 1.05

transform fa_tile_idle:
    zoom 1.0

transform fa_tile_dragging:
    alpha 0.96
    matrixcolor BrightnessMatrix(0.12)

transform fa_tile_shadow:
    alpha 0.35
    yoffset 4

transform fa_slot_pulse:
    alpha 0.35
    ease 1.2 alpha 0.7
    ease 1.2 alpha 0.35
    repeat

transform fa_slot_filled_glow:
    alpha 0.65

transform fa_btn_focus_pulse:
    alpha 0.85
    ease 0.8 alpha 1.0
    ease 0.8 alpha 0.85
    repeat

transform fa_success_flash:
    alpha 0.2
    ease 0.18 alpha 0.75
    ease 0.22 alpha 0.2
    repeat

transform fa_panel_scan:
    alpha 0.18
    xoffset -60
    linear 2.8 xoffset 60
    repeat

transform fa_error_shake:
    xoffset 0
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset -6
    linear 0.04 xoffset 6
    linear 0.04 xoffset 0


init -2:
    style fa_h1 is default
    style fa_h1:
        size 46
        color "#F2F6FF"
        text_align 0.5
        outlines [(2, "#000000AA", 0, 0)]

    style fa_h2 is default
    style fa_h2:
        size 24
        color "#65D5FF"
        text_align 0.5
        outlines [(2, "#0A1D2B", 0, 0)]

    style fa_hint is default
    style fa_hint:
        size 22
        color "#A8CFE4"
        text_align 0.5
        outlines [(1, "#07141F", 0, 0)]

    style fa_word is default
    style fa_word:
        size 23
        color "#FFFFFF"
        text_align 0.5
        outlines [(2, "#000000CC", 0, 0)]

    style fa_btn_text is default
    style fa_btn_text:
        size 28
        color "#E6F8FF"
        text_align 0.5
        outlines [(2, "#0C2533", 0, 0)]
        insensitive_color "#7F8A99"
        insensitive_outlines [(2, "#0C253355", 0, 0)]

    style fa_btn is default
    style fa_btn:
        xpadding 28
        ypadding 14
        background Solid("#153246D0")
        hover_background Solid("#1B4D68F0")
        insensitive_background Solid("#1A1E2688")


# ------------------------------------------------------------
# MISE EN SCÈNE « FATAL ASSEMBLY »
# Plateau holographique du Conclave, chrono circulaire, Kami qui surgit
# pour mettre la pression et bulles de réactions des représentants.
# La logique (mots, emplacements, score) reste celle de debat_phase1_*.
# ------------------------------------------------------------
init python:
    import time as _fa_time

    FA_ASSETS = "minijeu/fatal_assembly_assets/"
    FA_CYAN = "#5cd3ff"
    FA_AMBER = "#ffb84d"
    FA_KAMI = "#ff2e8a"
    FA_BUBBLE_TIME = 3.2
    FA_KAMI_TIME = 3.9
    FA_TIMER_CX = 1730
    FA_TIMER_CY = 182
    FA_TIMER_SEGMENTS = 48

    # Réactions des représentants : (personnage, expression, réplique).
    FA_REP_WRONG = [
        ("ryn", "colere", _("Ça veut rien dire, ça !")),
        ("nyra", "raison", _("Relis la structure. Le verbe vient avant.")),
        ("tomas", "inquiet", _("Attends, ce mot-là n'a rien à faire là...")),
        ("mara", "blase", _("Super. On va voter sur du charabia.")),
        ("iris", "colere", _("Concentre-toi, Noam !")),
        ("kael", "reflexion", _("Non. Ça ne colle pas avec la suite.")),
    ]
    FA_REP_GOOD = [
        ("elen", "joie", _("Ouiii, ça prend forme !")),
        ("julian", "sourire", _("Voilà qui ressemble enfin à un texte de loi.")),
        ("lysa", "reflexion", _("Continue, t'es pas loin.")),
        ("tomas", "joie", _("C'est ça ! Je reconnais la phrase.")),
    ]
    FA_REP_IDLE = [
        ("ryn", "colere", _("Ça fait combien de temps qu'on est là ?!")),
        ("nyra", "raison", _("Les virgules. Regarde les virgules.")),
        ("elen", "inquiet", _("Je comprends plus rien...")),
        ("julian", "sourire", _("Les caméras tournent, Noam. Souris.")),
        ("sael", "determine", _("Commence par le verbe. Le reste suivra.")),
    ]
    FA_KAMI_LINES = {
        "reset": ("taquin", _("On recommence ? Je prends note de chaque hésitation.")),
        "wrong3": ("professeur", _("Trois erreurs. Vous lisez avec les pieds, médiateur ?")),
        "wrong6": ("colere", _("Six. Je commence à douter de vos capacités de lecture.")),
        "success": ("fier", _("Hm. Correct. Ne vous habituez pas à mes félicitations.")),
        "start": ("taquin", _("Le texte est là. Il suffit de le lire. Simple, non ?")),
    }
    FA_KAMI_THRESHOLD_EXPR = {120: "taquin", 60: "professeur", 30: "fier", 10: "colere"}

    class _FARuntime(object):
        pass

    _fa_runtime = _FARuntime()
    _fa_runtime.fx = None

    def fa_strip_speaker(line):
        text = kd_tr(line)
        head, sep, rest = text.partition(":")
        if sep and head.strip().lower() in ("kami", "kami "):
            return rest.strip()
        return text

    class FAFX(object):
        def __init__(self, total):
            self.total = float(total)
            self.left = float(total)
            self.elapsed = 0.0
            self._clock = None
            self.bubbles = []
            self.kami = None
            self.kami_serial = 0
            self.bubble_serial = 0
            self.streak = 0
            self.wrong = 0
            self.thresholds = set()
            self.idle_marks = [22.0, 58.0, 96.0, 138.0]
            self.idle_pool = list(range(len(FA_REP_IDLE)))
            self.heartbeat = False
            self.started = False
            _fa_runtime.fx = self

        # --- événements -------------------------------------------------
        def bubble(self, entry):
            who, expr, line = entry
            self.bubble_serial += 1
            self.bubbles = [dict(who=who, expr=expr, text=line, t0=self.elapsed, id=self.bubble_serial)]
            renpy.sound.play("audio/sfx_beep.mp3", channel="kd_fx", relative_volume=0.5)

        def say_kami(self, key=None, expr=None, text=None):
            if key is not None:
                expr, text = FA_KAMI_LINES[key]
            self.kami_serial += 1
            self.kami = dict(expr=expr, text=text, t0=self.elapsed, id=self.kami_serial)
            renpy.sound.play("audio/sfx_kami_alert.wav", channel="kd_fx")

        def on_drop(self, correct):
            if correct:
                self.streak += 1
                if self.streak in (4, 8, 12):
                    self.bubble(renpy.random.choice(FA_REP_GOOD))
            else:
                self.streak = 0
                self.wrong += 1
                if self.wrong == 3:
                    self.say_kami("wrong3")
                elif self.wrong == 6:
                    self.say_kami("wrong6")
                else:
                    self.bubble(renpy.random.choice(FA_REP_WRONG))

        def on_reset(self):
            self.streak = 0
            self.say_kami("reset")

        def on_success(self):
            self.say_kami("success")
            self.bubble(("lysa", "sourire", _("C'est bon, on l'a !")))

        # --- horloge ----------------------------------------------------
        def tick(self):
            now = _fa_time.time()
            dt = 0.0 if self._clock is None else min(0.25, max(0.0, now - self._clock))
            self._clock = now
            if not self.started:
                self.started = True
                _fa_runtime.fx = self
                self.say_kami("start")
            if debat_phase1_success:
                dt = 0.0
            self.elapsed += dt
            self.left = max(0.0, self.left - dt)

            for threshold in DEBAT_PHASE1_COMMENT_THRESHOLDS:
                if self.left <= threshold and threshold not in self.thresholds:
                    self.thresholds.add(threshold)
                    if self.total > threshold + 1:
                        self.say_kami(
                            expr=FA_KAMI_THRESHOLD_EXPR.get(threshold, "taquin"),
                            text=fa_strip_speaker(debat_phase1_pick_pressure_comment(threshold)),
                        )

            if self.idle_marks and self.elapsed >= self.idle_marks[0]:
                self.idle_marks.pop(0)
                if self.idle_pool and (self.kami is None):
                    index = renpy.random.choice(self.idle_pool)
                    self.idle_pool.remove(index)
                    self.bubble(FA_REP_IDLE[index])

            if self.left <= 10 and not self.heartbeat:
                self.heartbeat = True
                renpy.music.play("audio/sfx_heartbeat.mp3", channel="kd_fx_loop", loop=True)

            self.bubbles = [b for b in self.bubbles if self.elapsed - b["t0"] < FA_BUBBLE_TIME]
            if self.kami is not None and self.elapsed - self.kami["t0"] >= FA_KAMI_TIME:
                self.kami = None

            if self.left <= 0:
                fa_stop_loops()
                return {"success": False, "time_left": 0}
            return None

        # --- affichage --------------------------------------------------
        def seconds_left(self):
            return int(self.left + 0.999)

        def clock_text(self):
            seconds = self.seconds_left()
            return "%02d:%02d" % (seconds // 60, seconds % 60)

        def centis(self):
            return "%02d" % int((self.left - int(self.left)) * 100)

        def color(self):
            if self.left <= 30:
                return FA_KAMI
            if self.left <= 60:
                return FA_AMBER
            return FA_CYAN

        def segments(self):
            lit = int(round(FA_TIMER_SEGMENTS * self.left / max(1.0, self.total)))
            out = []
            for index in range(FA_TIMER_SEGMENTS):
                angle = 360.0 * index / FA_TIMER_SEGMENTS
                rad = _fa_math.radians(angle - 90)
                x = FA_TIMER_CX + int(100 * _fa_math.cos(rad))
                y = FA_TIMER_CY + int(100 * _fa_math.sin(rad))
                out.append((x, y, angle, index < lit))
            return out

        def kami_image(self):
            return fa_kami_displayable((self.kami or {}).get("expr", "taquin"))

        def kami_chars(self):
            if self.kami is None:
                return 0
            return int((self.elapsed - self.kami["t0"]) * 55)

    import math as _fa_math

    _fa_kami_cache = {}

    def _fa_kami_frame(st, at, expr):
        talking = st < 2.4 and int(st * 7) % 2 == 0
        path = "images/background/kami_diffusion/%s%s.png" % (expr, "_parle" if talking else "")
        if not renpy.loadable(path):
            path = "images/background/kami_diffusion/%s.png" % expr
        return Transform(path, crop=(380, 100, 820, 780), zoom=0.42), 0.07

    def fa_kami_displayable(expr):
        if expr not in _fa_kami_cache:
            _fa_kami_cache[expr] = DynamicDisplayable(_fa_kami_frame, expr)
        return _fa_kami_cache[expr]

    def fa_stop_loops():
        renpy.music.stop(channel="kd_fx_loop", fadeout=0.3)

    def fa_fx_event(name, *args):
        fx = getattr(_fa_runtime, "fx", None)
        if fx is None:
            return
        getattr(fx, name)(*args)

    renpy.music.register_channel("kd_fx_loop", mixer="sfx", loop=True)


transform fa_scan_line:
    alpha 0.16
    yoffset -1080
    linear 3.6 yoffset 1080
    repeat

transform fa_bubble_pop:
    subpixel True
    alpha 0.0 zoom 0.7 yoffset 24
    easeout 0.16 alpha 1.0 zoom 1.06 yoffset 0
    easein 0.08 zoom 1.0
    pause (FA_BUBBLE_TIME - 0.5)
    linear 0.22 alpha 0.0 yoffset -10

transform fa_kami_hop:
    subpixel True
    yoffset 420 rotate -12
    easeout 0.22 yoffset -26 rotate 6
    easein 0.12 yoffset 0 rotate 0
    block:
        ease 0.35 yoffset -10 rotate -3
        ease 0.35 yoffset 0 rotate 3
        repeat 4
    easein 0.25 yoffset 460 rotate 10

transform fa_kami_bubble:
    subpixel True
    alpha 0.0 xoffset 40
    pause 0.15
    easeout 0.16 alpha 1.0 xoffset 0
    pause (FA_KAMI_TIME - 0.75)
    linear 0.2 alpha 0.0

transform fa_kami_glitch:
    alpha 0.0
    linear 0.04 alpha 0.18
    linear 0.04 alpha 0.0
    linear 0.03 alpha 0.12
    linear 0.12 alpha 0.0

transform fa_seg(angle):
    anchor (0.5, 0.5)
    rotate angle

transform fa_digits_pulse:
    zoom 1.0
    easeout 0.08 zoom 1.12
    easein 0.42 zoom 1.0
    repeat

transform fa_edge_alarm:
    alpha 0.0
    easeout 0.12 alpha 0.85
    easein 0.75 alpha 0.15
    repeat

transform fa_eye_watch:
    alpha 0.55
    ease 1.4 alpha 0.95
    ease 1.4 alpha 0.55
    repeat

transform fa_face_tilt:
    rotate_pad False
    rotate -4


screen debat_phase1_opening():
    modal True
    zorder 250

    default fx = FAFX(DEBAT_PHASE1_TOTAL_TIME)

    timer 0.04 repeat True action Function(fx.tick)

    key "rollback" action NullAction()
    key "rollforward" action NullAction()

    # --- GARDE ANTI-DESYNC ---
    $ expected = len(debat_phase1_target) if debat_phase1_target else len(DEBAT_PHASE1_TARGET)
    if (debat_phase1_slots is None) or (len(debat_phase1_slots) != expected) or (len(debat_phase1_words) != expected):
        $ debat_phase1_setup()
    elif len(debat_phase1_slot_layout) != len(debat_phase1_slots):
        $ debat_phase1_refresh_slot_layout()

    $ fa_filled_count = sum(1 for slot_word_id in debat_phase1_slots if slot_word_id is not None)
    $ fa_total_slots = max(1, len(debat_phase1_slots))
    $ fa_timer_color = fx.color()

    # ------------------------------------------------------------
    # Décor : Conclave assombri, scan holographique.
    # ------------------------------------------------------------
    add "bg_conclave" at adaptive_fullscreen
    add Solid("#030812d6")
    add "gui/main_menu_kami/scanlines.png" alpha 0.28
    add "gui/main_menu_kami/vignette.png"
    add Solid(FA_CYAN, xysize=(1920, 2)) at fa_scan_line

    if fx.left <= 10 and not debat_phase1_success:
        add "gui/main_menu_kami/vignette.png" at fa_edge_alarm:
            matrixcolor TintMatrix(FA_KAMI) * BrightnessMatrix(0.25)

    # ------------------------------------------------------------
    # Titre
    # ------------------------------------------------------------
    vbox:
        xpos 40
        ypos 22
        spacing 0
        text "FATAL ASSEMBLY":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 68
            color "#ffffff"
            kerning 6
            outlines [(3, "#0b4a66", 0, 0)]
        text _("RECONSTITUEZ LE TEXTE OFFICIEL AVANT LA FIN DU DÉCOMPTE"):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 22
            color FA_CYAN
            kerning 2
    add Solid(FA_CYAN, xysize=(220, 4)) xpos 44 ypos 146
    add Solid(FA_CYAN + "66", xysize=(60, 4)) xpos 272 ypos 146

    if fx.kami is None:
        hbox at fa_eye_watch:
            xpos 760
            ypos 44
            spacing 12
            add Transform("gui/main_menu_kami/glyph_kami.png", zoom=0.26)
            text _("KAMI OBSERVE"):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 22
                color FA_KAMI
                kerning 4
                yalign 0.5

    # ------------------------------------------------------------
    # Chrono circulaire
    # ------------------------------------------------------------
    add FA_ASSETS + "timer_disc.png" xcenter FA_TIMER_CX ycenter FA_TIMER_CY
    for seg_x, seg_y, seg_angle, seg_on in fx.segments():
        add FA_ASSETS + "seg.png" at fa_seg(seg_angle):
            xpos seg_x
            ypos seg_y
            matrixcolor TintMatrix(fa_timer_color if seg_on else "#1b2c40")
    text _("TEMPS"):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 18
        color "#8fb4c8"
        kerning 4
        xcenter FA_TIMER_CX
        ycenter (FA_TIMER_CY - 44)
    if fx.left <= 10 and not debat_phase1_success:
        text fx.clock_text() at fa_digits_pulse:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 64
            color fa_timer_color
            outlines [(2, "#000000", 0, 0)]
            xcenter FA_TIMER_CX
            ycenter (FA_TIMER_CY + 4)
    else:
        text fx.clock_text():
            font "fonts/Rajdhani-SemiBold.ttf"
            size 64
            color fa_timer_color
            outlines [(2, "#000000", 0, 0)]
            xcenter FA_TIMER_CX
            ycenter (FA_TIMER_CY + 4)
    text fx.centis():
        font "fonts/Rajdhani-SemiBold.ttf"
        size 22
        color "#8fb4c8"
        xcenter FA_TIMER_CX
        ycenter (FA_TIMER_CY + 50)

    # ------------------------------------------------------------
    # Panneaux de jeu
    # ------------------------------------------------------------
    frame:
        background Frame("minijeu/refutation_assets/panel.png", 26, 26)
        xpos 34
        ypos DEBAT_PHASE1_BANK_Y
        xsize 1852
        ysize 266
    text _("FRAGMENTS DU TEXTE"):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 24
        color FA_CYAN
        kerning 3
        xpos 62
        ypos (DEBAT_PHASE1_BANK_Y + 18)
    add Solid(FA_CYAN, xysize=(80, 3)) xpos 64 ypos (DEBAT_PHASE1_BANK_Y + 50)

    frame:
        background Frame("minijeu/refutation_assets/panel.png", 26, 26)
        xpos 34
        ypos 650
        xsize 1852
        ysize 252
    text _("TEXTE OFFICIEL  //  RECONSTITUTION"):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 24
        color FA_CYAN
        kerning 3
        xpos 62
        ypos 668
    text ("%d / %d" % (fa_filled_count, fa_total_slots)):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 24
        color "#8fb4c8"
        xpos 1850
        xanchor 1.0
        ypos 668

    use mk_help_button("tuto_debat_phase1")

    draggroup:
        xsize 1920
        ysize 1080

        drag:
            drag_name "word_bank"
            draggable False
            droppable True
            xpos 48
            ypos DEBAT_PHASE1_BANK_Y
            xsize 1824
            ysize 266

        for i in range(len(debat_phase1_slots)):
            $ sx, sy, slot_w, slot_h = debat_phase1_slot_layout[i]
            drag:
                drag_name ("slot_%d" % i)
                draggable False
                droppable True
                xpos sx
                ypos sy
                xsize slot_w
                ysize slot_h
                fixed:
                    xysize (slot_w, slot_h)
                    add Frame(FA_ASSETS + "slot.png", 16, 16, xysize=(slot_w, slot_h))
                    if debat_phase1_slots[i] is None:
                        add Solid(FA_CYAN + "30", xysize=(slot_w - 8, slot_h - 10)) at fa_slot_pulse:
                            xpos 4
                            ypos 4

        for word in debat_phase1_words:
            if word is None:
                continue

            $ word_id = word["id"]
            $ slot_index = debat_phase1_find_word_slot(word_id)
            if slot_index is not None:
                $ wx = debat_phase1_slot_layout[slot_index][0]
                $ wy = debat_phase1_slot_layout[slot_index][1]
            else:
                $ wx = word["home_x"]
                $ wy = word["home_y"]

            $ is_word_wrong = False
            if slot_index is not None and not debat_phase1_success:
                $ is_word_wrong = (word["text"] != debat_phase1_target[slot_index])
            $ ww = debat_phase1_word_width(word["text"])
            $ th = 54
            $ tile_img = "tile_ok.png" if debat_phase1_success else ("tile_wrong.png" if is_word_wrong else "tile.png")

            drag:
                drag_name ("word_%d" % word_id)
                xpos wx
                ypos wy
                xsize ww
                ysize th
                draggable (not debat_phase1_success)
                droppable False
                drag_raise True
                drag_handle (0, 0, ww, th)
                dragged (lambda drags, drop, wid=word_id: debat_phase1_handle_drop(wid, drags, drop))
                fixed:
                    xysize (ww, th)
                    add Solid("#00000070", xysize=(ww - 6, th - 6)) xpos 5 ypos 8
                    if is_word_wrong:
                        add Frame(FA_ASSETS + tile_img, 16, 16, xysize=(ww, th)) at fa_error_shake
                    else:
                        add Frame(FA_ASSETS + tile_img, 16, 16, xysize=(ww, th))
                    text kd_tr(word["text"]):
                        style "fa_word"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 26
                        color ("#ffd0e2" if is_word_wrong else "#ffffff")
                        xalign 0.5
                        yalign 0.5

    # ------------------------------------------------------------
    # Barre du bas : réinitialiser, progression, valider.
    # ------------------------------------------------------------
    textbutton _("RÉINITIALISER"):
        xpos 40
        ypos 942
        xysize (300, 80)
        background Frame("minijeu/refutation_assets/frag_idle.png", 30, 26)
        hover_background Frame("minijeu/refutation_assets/frag_selected.png", 30, 26)
        text_font "fonts/Rajdhani-SemiBold.ttf"
        text_size 28
        text_color "#d9ecf7"
        text_kerning 3
        text_xalign 0.5
        text_yalign 0.5
        sensitive (not debat_phase1_success)
        action [Play("sound", "audio/sfx_glitch.mp3"), Function(debat_phase1_setup, count_reset=True), Function(fa_fx_event, "on_reset")]

    hbox:
        xcenter 960
        ycenter 982
        spacing 6
        for pi in range(fa_total_slots):
            add Solid((FA_CYAN if pi < fa_filled_count else "#1b2c40"), xysize=(int(min(46, 1040 / fa_total_slots - 6)), 12))

    textbutton _("VALIDER"):
        xpos 1580
        ypos 936
        xysize (300, 92)
        background Frame("minijeu/refutation_assets/frag_idle.png", 30, 26)
        hover_background Frame("minijeu/refutation_assets/frag_selected.png", 30, 26)
        insensitive_background Frame("minijeu/refutation_assets/frag_idle.png", 30, 26)
        text_font "fonts/Rajdhani-SemiBold.ttf"
        text_size 34
        text_color "#ffffff"
        text_insensitive_color "#4f6a80"
        text_kerning 4
        text_xalign 0.5
        text_yalign 0.5
        sensitive debat_phase1_success
        action [Function(fa_stop_loops), Play("sound", "audio/sfx_victory.mp3"), Return({"success": True, "time_left": fx.seconds_left()})]
        if debat_phase1_success:
            at fa_btn_focus_pulse

    # ------------------------------------------------------------
    # Pression : bulles des représentants et irruptions de Kami.
    # ------------------------------------------------------------
    for bubble index bubble["id"] in fx.bubbles:
        $ b_color = kd_char_color(bubble["who"])
        fixed at fa_bubble_pop:
            xpos 40
            ypos 150
            xysize (560, 150)
            fixed at fa_face_tilt:
                xysize (112, 112)
                ypos 14
                add Solid(b_color)
                add kd_face(bubble["who"], bubble["expr"], 104) xalign 0.5 yalign 0.5
            add FA_ASSETS + "tail_rep.png" xpos 124 ypos 50
            frame:
                background Frame(FA_ASSETS + "bubble_rep.png", 24, 24)
                xpos 150
                ypos 6
                xmaximum 400
                padding (24, 14)
                vbox:
                    spacing 2
                    text kd_display_name(bubble["who"]).upper():
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 20
                        color b_color
                        kerning 2
                    text kd_tr(bubble["text"]):
                        size 24
                        color "#eef7ff"

    for kami_line index kami_line["id"] in ([fx.kami] if fx.kami else []):
        add Solid(FA_KAMI) at fa_kami_glitch
        fixed:
            add fx.kami_image() at fa_kami_hop:
                xpos 1236
                ypos 0
            frame at fa_kami_bubble:
                background Frame(FA_ASSETS + "bubble_kami.png", 24, 24)
                xpos 620
                ypos 150
                xsize 600
                padding (28, 18)
                vbox:
                    spacing 4
                    text "KAMI":
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 22
                        color FA_KAMI
                        kerning 4
                    text kd_tr(kami_line["text"]):
                        size 27
                        color "#ffffff"
                        slow_cps 55
            add FA_ASSETS + "tail_kami.png" at fa_kami_bubble:
                xpos 1212
                ypos 210
                xzoom -1.0


# ------------------------------------------------------------
# TUTORIEL ANIMÉ — démo drag & drop d'un mot vers un slot
# ------------------------------------------------------------
transform fa_demo_word_drag:
    xpos 90 ypos 120 alpha 0.0
    block:
        easein 0.35 alpha 1.0
        pause 0.45
        easeout 0.9 xpos 250 ypos 360
        pause 0.35
        linear 0.25 alpha 0.0
        pause 0.6
        repeat

transform fa_demo_slot_glow:
    alpha 0.35
    block:
        ease 0.8 alpha 0.85
        ease 0.8 alpha 0.35
        repeat

transform fa_demo_check_pop:
    alpha 0.0
    block:
        pause 1.7
        easeout 0.2 alpha 1.0 zoom 1.2
        easein 0.2 zoom 1.0
        pause 0.35
        linear 0.2 alpha 0.0
        pause 0.55
        repeat

screen tuto_debat_phase1(as_overlay=False):
    use mk_tuto_chrome("FATAL ASSEMBLY", [
        ("Lis la banque de mots", "Les mots de la proposition sont rangés dans le panneau du haut, dans le désordre."),
        ("Glisse chaque mot", "Fais glisser les mots dans les emplacements, dans le bon ordre."),
        ("Valide avant la fin du chrono", "Quand la phrase est correcte, le bouton de validation s'active. Kami commente ton retard..."),
    ], "tuto_debat_phase1", as_overlay):

        fixed:
            xfill True
            yfill True

            # Banque (3 mots fixes)
            frame:
                xpos 40
                ypos 60
                xsize 660
                ysize 150
                background Solid("#1024348A")
            text "Autoriser" pos (260, 110) size 24 color "#FFFFFF" bold True
            text "vente" pos (470, 95) size 24 color "#FFFFFF" bold True

            # Slots
            for fa_si in range(3):
                frame at fa_demo_slot_glow:
                    xpos (110 + fa_si * 200)
                    ypos 350
                    xsize 170
                    ysize 62
                    background Solid("#2AE5FF40")

            # Mot qui se déplace
            frame at fa_demo_word_drag:
                xsize 150
                ysize 48
                background Solid("#1B2D43F0")
                text "le" align (0.5, 0.5) size 24 color "#FFFFFF" bold True

            text "OK" at fa_demo_check_pop:
                xpos 335
                ypos 300
                size 48
                color "#5DFF9A"
                bold True

# ------------------------------------------------------------
# WRAPPER COMPLET : tutoriel → anim → jeu → retry malus → résultats
#   call debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY",
#                         target=None, with_intro_anim=True)
#   → _return = rang ; debat_phase1_last_result = {"success","time_left","kamyz"}
# ------------------------------------------------------------
label debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY", target=None, with_intro_anim=True):

    call mk_tutorial("debat_phase1", "tuto_debat_phase1") from _call_mk_tutorial

    if with_intro_anim:
        call FA_START_ANIM from _call_FA_START_ANIM

    $ mk_reset_retries(mg_id)

label .attempt:
    $ debat_phase1_setup(target=target)
    $ fa_run_result = renpy.call_screen("debat_phase1_opening")

    if not fa_run_result.get("success"):
        call mk_fail_retry(title, mg_id) from _call_mk_fail_retry
        if not _return:
            $ debat_phase1_last_result = {"success": False, "time_left": 0, "kamyz": 0}
            return "D"
        jump .attempt

    python:
        fa_time_left = fa_run_result.get("time_left", 0)
        fa_run_score = debat_phase1_compute_score(fa_time_left, DEBAT_PHASE1_TOTAL_TIME)
        fa_run_challenges = [
            ("Sans réinitialiser", debat_phase1_resets == 0),
            ("Aucun mot mal placé", debat_phase1_wrong_drops == 0),
            ("Fini avec +50% du temps", fa_time_left >= DEBAT_PHASE1_TOTAL_TIME / 2),
        ]
        fa_run_score = min(1000, fa_run_score + 40 * len([1 for c in fa_run_challenges if c[1]]))
        store.debat_phase1_last_result = {
            "success": True,
            "time_left": fa_time_left,
            "kamyz": debat_phase1_calculate_kamyz(fa_time_left),
        }

    call mk_show_results(
        title,
        fa_run_score,
        1000,
        stats=[
            ("Temps restant", "%ds / %ds" % (fa_time_left, DEBAT_PHASE1_TOTAL_TIME)),
            ("Mots mal placés", str(debat_phase1_wrong_drops)),
            ("Réinitialisations", str(debat_phase1_resets)),
        ],
        challenges=fa_run_challenges,
        mg_id=mg_id,
        retries=mk_get_retries(mg_id),
    ) from _call_mk_show_results
    return _return


screen noam_consent_screen():
    modal True
    zorder 260

    add "images/background/debat/noam_agree.png" at adaptive_fullscreen

    on "show" action Play("sound", sfx_victory)
    timer 2.8 action Return(True)


# Animation :

transform fa_cam_in:
    zoom 1.08
    ease 0.8 zoom 1.0

transform fa_pop:
    alpha 0.0
    zoom 0.96
    linear 0.15 alpha 1.0
    easeout 0.35 zoom 1.02
    easein 0.10 zoom 0.99
    easeout 0.15 zoom 1.0

transform fa_tiles_float:
    yoffset 0
    ease 1.2 yoffset -10
    ease 1.2 yoffset 0
    repeat

transform fa_title_slam:
    yoffset 60
    alpha 0.0
    linear 0.12 alpha 1.0
    easeout 0.35 yoffset 0
    easein 0.08 yoffset 12
    easeout 0.12 yoffset 0


label FA_START_ANIM:

    $ renpy.block_rollback()

    scene black

    show fatal_assembly_1 as fa_bg at adaptive_fullscreen, fa_cam_in
    play sound sfx_minigame_start
    pause 0.50

    show fatal_assembly_2 as fa_fx at adaptive_fullscreen, fa_pop
    pause 0.50

    show fatal_assembly_3 as fa_noam at adaptive_fullscreen, fa_pop
    pause 0.50

    show fatal_assembly_4 as fa_tiles at adaptive_fullscreen, fa_tiles_float
    pause 0.60

    show fatal_assembly_5 as fa_title at adaptive_fullscreen, fa_title_slam
    pause 1.20

    pause 1.30
    return
