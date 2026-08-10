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


screen debat_phase1_opening():
    modal True
    zorder 250
    default fa_hovered_word = None
    default fa_time_left = DEBAT_PHASE1_TOTAL_TIME
    default fa_shown_thresholds = []
    default fa_pressure_comment = ""

    timer 1.0 repeat True action [
        If(fa_time_left > 0, true=SetScreenVariable("fa_time_left", fa_time_left - 1)),
        If(
            (fa_time_left in DEBAT_PHASE1_COMMENT_THRESHOLDS) and (fa_time_left not in fa_shown_thresholds),
            true=[
                SetScreenVariable("fa_pressure_comment", debat_phase1_pick_pressure_comment(fa_time_left)),
                SetScreenVariable("fa_shown_thresholds", fa_shown_thresholds + [fa_time_left]),
            ],
        ),
        If(fa_time_left <= 0, true=Return({"success": False, "time_left": 0})),
    ]

    # --- GARDE ANTI-DESYNC ---
    $ expected = len(debat_phase1_target) if debat_phase1_target else len(DEBAT_PHASE1_TARGET)
    if (debat_phase1_slots is None) or (len(debat_phase1_slots) != expected) or (len(debat_phase1_words) != expected):
        $ debat_phase1_setup()
    elif len(debat_phase1_slot_layout) != len(debat_phase1_slots):
        $ debat_phase1_refresh_slot_layout()

    $ fa_filled_count = sum(1 for slot_word_id in debat_phase1_slots if slot_word_id is not None)
    $ fa_total_slots = max(1, len(debat_phase1_slots))
    $ fa_time_text = debat_phase1_format_time(fa_time_left)
    $ fa_timer_width = int(184 * max(0, fa_time_left) / float(max(1, DEBAT_PHASE1_TOTAL_TIME)))

    fixed:
        add Solid("#020711")

        add "gui/day3/vote_phase2/bg_overlay.png":
            alpha 0.20

        for gx in range(48, 1921, 96):
            add Solid("#2A9CCD14", xsize=1, ysize=1080):
                xpos gx
                ypos 0
        for gy in range(40, 1081, 72):
            add Solid("#2A9CCD10", xsize=1920, ysize=1):
                xpos 0
                ypos gy

        add Solid("#00000058", xsize=1920, ysize=86):
            xpos 0
            ypos 0
        add Solid("#00000066", xsize=1920, ysize=150):
            xpos 0
            ypos 930
        add Solid("#00000036", xsize=90, ysize=1080):
            xpos 0
            ypos 0
        add Solid("#00000036", xsize=90, ysize=1080):
            xpos 1830
            ypos 0

    fixed:
        xpos 34
        ypos 28
        xysize (820, 82)

        add Solid("#06111DD8", xsize=820, ysize=82)
        add Solid("#5DCBFFAA", xsize=4, ysize=62):
            xpos 0
            ypos 10
        text "▽":
            xpos 24
            ypos -6
            size 68
            color "#BFD9EA"
            outlines [(2, "#020711", 0, 0)]
        text "FATAL ASSEMBLY":
            xpos 96
            ypos -2
            size 42
            color "#EAF4FF"
            bold True
            outlines [(2, "#020711", 0, 0)]
        text "RECONSTRUISEZ LE VÉRITABLE TEXTE":
            xpos 100
            ypos 52
            size 20
            color "#9BCDEB"
            outlines [(1, "#020711", 0, 0)]
        add Solid("#53CFFF", xsize=128, ysize=6):
            xpos 412
            ypos 60
        add Solid("#53CFFF99", xsize=28, ysize=6):
            xpos 548
            ypos 60

    text "ARCHIVE // ANALYSE DE TEXTE":
        xpos 1542
        ypos 32
        xanchor 1.0
        size 20
        color "#6F8BA2"
        outlines [(1, "#020711", 0, 0)]
    add Solid("#4FC8FF", xsize=114, ysize=4):
        xpos 1572
        ypos 60
    add Solid("#4FC8FF88", xsize=28, ysize=4):
        xpos 1700
        ypos 60

    frame:
        xpos 34
        ypos 126
        xsize 820
        ysize 180
        background Solid("#071421E8")
        padding (18, 18)

        fixed:
            add Solid("#3EBEFF99", xsize=3, ysize=156):
                xpos 0
                ypos 0
            add Solid("#3EBEFF66", xsize=784, ysize=1):
                xpos 0
                ypos 0
            add Solid("#3EBEFF35", xsize=784, ysize=1):
                xpos 0
                ypos 155
            frame:
                xpos 16
                ypos 0
                xsize 156
                ysize 156
                background Solid("#0D253BEE")
                padding (0, 0)
                add "images/character/kami/analyse.png":
                    xysize (156, 156)
                    alpha 0.92
            vbox:
                xpos 198
                ypos 8
                spacing 8
                text "KAMI":
                    size 22
                    color "#5FD5FF"
                    bold True
                    outlines [(1, "#020711", 0, 0)]
                text "Alors, médiateur...":
                    size 24
                    color "#F2F6FF"
                    outlines [(1, "#020711", 0, 0)]
                if fa_pressure_comment:
                    text kd_tr(fa_pressure_comment):
                        size 21
                        color "#DCEBFA"
                        xmaximum 560
                        line_spacing 4
                        outlines [(1, "#020711", 0, 0)]
                else:
                    text "Remettez les mots dans le bon ordre.\nMontrez-moi que vous comprenez vraiment ce que vous votez.":
                        size 22
                        color "#DCEBFA"
                        line_spacing 4
                        outlines [(1, "#020711", 0, 0)]

    frame:
        xpos 884
        ypos 126
        xsize 1002
        ysize 180
        background Solid("#071421E8")
        padding (22, 18)

        fixed:
            add Solid("#3EBEFF99", xsize=3, ysize=156):
                xpos 0
                ypos 0
            add Solid("#3EBEFF66", xsize=956, ysize=1):
                xpos 0
                ypos 0
            add Solid("#3EBEFF35", xsize=956, ysize=1):
                xpos 0
                ypos 155
            vbox:
                xpos 22
                ypos 4
                spacing 10
                hbox:
                    spacing 12
                    text "●":
                        size 28
                        color "#62D9FF"
                    text "OBJECTIF":
                        size 26
                        color "#EAF4FF"
                        bold True
                        outlines [(1, "#020711", 0, 0)]
                text "Glissez-déposez les mots pour reconstituer la phrase exacte du texte officiel.":
                    size 23
                    color "#E7F0FA"
                    xmaximum 650
                    outlines [(1, "#020711", 0, 0)]
                text "Chaque placement compte : une proposition propre donne un meilleur résultat.":
                    size 19
                    color "#91AABD"
                    xmaximum 650
                    outlines [(1, "#020711", 0, 0)]
            fixed:
                xpos 766
                ypos 4
                xysize (164, 146)
                add Solid("#020A13EE", xsize=164, ysize=146)
                add Solid("#FFB42E", xsize=10, ysize=120):
                    xpos 140
                    ypos 13
                add Solid("#173149", xsize=184, ysize=8):
                    xpos -10
                    ypos 130
                add Solid("#FFD35C", xsize=fa_timer_width, ysize=8):
                    xpos -10
                    ypos 130
                text "TEMPS\nRESTANT":
                    xpos 0
                    ypos 18
                    xsize 136
                    text_align 0.5
                    size 18
                    color "#9BCDEB"
                    line_spacing 2
                    outlines [(1, "#020711", 0, 0)]
                text "[fa_time_text]":
                    xpos 0
                    ypos 74
                    xsize 136
                    text_align 0.5
                    size 36
                    color ("#FF4D6D" if fa_time_left <= 10 else "#F4F8FF")
                    bold True
                    outlines [(2, "#020711", 0, 0)]

    frame:
        xpos 34
        ypos DEBAT_PHASE1_BANK_Y
        xsize 1852
        ysize 266
        background Solid("#071421E8")
        padding (20, 28)

        fixed:
            add Solid("#3EBEFFAA", xsize=3, ysize=232):
                xpos 0
                ypos 0
            add Solid("#3EBEFF66", xsize=1810, ysize=1):
                xpos 0
                ypos 0
            add Solid("#3EBEFF35", xsize=1810, ysize=1):
                xpos 0
                ypos 231
            add Solid("#65D5FF24", xsize=120, ysize=232) at fa_panel_scan
            text "MOTS DISPONIBLES":
                xpos 22
                ypos -12
                size 24
                color "#65D5FF"
                bold True
                outlines [(1, "#020711", 0, 0)]
            add Solid("#65D5FF", xsize=92, ysize=5):
                xpos 256
                ypos 0

    frame:
        xpos 34
        ypos 680
        xsize 1852
        ysize 218
        background Solid("#06101CE8")
        padding (20, 28)

        fixed:
            add Solid("#3EBEFFAA", xsize=3, ysize=184):
                xpos 0
                ypos 0
            add Solid("#3EBEFF66", xsize=1810, ysize=1):
                xpos 0
                ypos 0
            add Solid("#3EBEFF35", xsize=1810, ysize=1):
                xpos 0
                ypos 183
            text "VOTRE PHRASE":
                xpos 22
                ypos -12
                size 24
                color "#65D5FF"
                bold True
                outlines [(1, "#020711", 0, 0)]
            text "[fa_filled_count]/[fa_total_slots] mots placés":
                xpos 1548
                ypos -8
                size 18
                color "#7895AA"
                outlines [(1, "#020711", 0, 0)]

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

        # --- SLOTS ---
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

                frame:
                    xfill True
                    yfill True
                    background Solid("#101A2680")
                    padding (6, 6)

                    fixed:
                        xfill True
                        yfill True

                        add Solid("#0A1522D8", xsize=slot_w, ysize=slot_h)

                        if debat_phase1_slots[i] is None:
                            add Solid("#2AE5FF40", xsize=slot_w, ysize=slot_h) at fa_slot_pulse
                        else:
                            add Solid("#2AE5FF40", xsize=slot_w, ysize=slot_h) at fa_slot_filled_glow

                        if debat_phase1_slots[i] is None:
                            add Solid("#64EBFF66", xsize=slot_w, ysize=2):
                                xpos 0
                                ypos 0
                            add Solid("#64EBFF66", xsize=slot_w, ysize=2):
                                xpos 0
                                ypos slot_h - 2
                        else:
                            add Solid("#74F3FFAA", xsize=slot_w, ysize=2):
                                xpos 0
                                ypos 0
                            add Solid("#74F3FFAA", xsize=slot_w, ysize=2):
                                xpos 0
                                ypos slot_h - 2

                        if debat_phase1_success:
                            add Solid("#63EBFF55", xsize=slot_w, ysize=slot_h) at fa_success_flash

        # --- WORDS ---
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

            $ float_at = None

            $ is_word_wrong = False
            if slot_index is not None and not debat_phase1_success:
                $ is_word_wrong = (word["text"] != debat_phase1_target[slot_index])

            # Largeur stable pour éviter les tiles "bizarres"
            $ ww = debat_phase1_word_width(word["text"])
            $ th = 54

            drag:
                drag_name ("word_%d" % word_id)
                xpos wx
                ypos wy
                xsize ww
                ysize th
                draggable True
                droppable False
                drag_raise True
                drag_handle (0, 0, ww, th)
                dragged (lambda drags, drop, wid=word_id: debat_phase1_handle_drop(wid, drags, drop))

                fixed:
                    xsize ww
                    ysize th
                    if float_at is not None:
                        at float_at

                    # shadow (sans texte -> pas de doublon)
                    frame:
                        xsize ww
                        ysize th
                        background Solid("#00000066")
                        at fa_tile_shadow

                    # main tile
                    frame:
                        xsize ww
                        ysize th
                        background Solid("#1B2D43E8")
                        at fa_tile_idle

                        fixed:
                            xfill True
                            yfill True

                            add Solid("#74EFFF18", xsize=ww - 2, ysize=2):
                                xpos 1
                                ypos 1

                            if debat_phase1_success:
                                add Solid("#61F0FF44") at fa_success_flash
                            elif is_word_wrong:
                                add Solid("#FF4D5E22") at fa_error_shake

                            text kd_tr(word["text"]):
                                style "fa_word"
                                xalign 0.5
                                yalign 0.5

    fixed:
        xpos 34
        ypos 930
        xysize (1852, 112)

        textbutton "↻  RÉINITIALISER":
            xpos 0
            ypos 18
            xsize 300
            ysize 76
            action [Play("sound", "audio/sfx_glitch.mp3"), Function(debat_phase1_setup, count_reset=True)]
            style "fa_btn"
            text_style "fa_btn_text"

        frame:
            xpos 560
            ypos 30
            xsize 720
            ysize 54
            background Solid("#071421D8")
            padding (18, 12)

            hbox:
                spacing 12
                yalign 0.5
                text "— PROGRESSION":
                    size 18
                    color "#6F8BA2"
                    outlines [(1, "#020711", 0, 0)]
                for pi in range(len(debat_phase1_slots)):
                    $ pip_color = "#65D5FF" if pi < fa_filled_count else "#162C42"
                    $ pip_edge = "#9BE8FF" if pi < fa_filled_count else "#41627A"
                    fixed:
                        xsize 18
                        ysize 18
                        add Solid(pip_edge, xsize=18, ysize=18)
                        add Solid(pip_color, xsize=12, ysize=12):
                            xpos 3
                            ypos 3

        textbutton "✓  VALIDER":
            xpos 1540
            ypos 8
            xsize 312
            ysize 88
            sensitive debat_phase1_success
            action [Play("sound", "audio/sfx_victory.mp3"), Return({"success": True, "time_left": fa_time_left})]
            style "fa_btn"
            text_style "fa_btn_text"
            if debat_phase1_success:
                at fa_btn_focus_pulse


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
