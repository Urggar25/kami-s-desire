# Mini-jeu : Débat - Phase 1 (Ouverture)

default debat_phase1_slots = []
default debat_phase1_words = []
default debat_phase1_success = False
default debat_phase1_slot_layout = []

define sfx_victory = "audio/sfx_clap.mp3"

init python:
    import random

    DEBAT_PHASE1_TARGET = [
        "Autoriser","le","transport,","la","vente","et","l’échange","de",
        "marchandises","entre","les","districts.","Le","système","actuel","de",
        "distribution","de","denrées","est","aboli.",
    ]

    DEBAT_PHASE1_FLOAT_POSITIONS = [
        (90, 170), (260, 140), (430, 180), (620, 145), (800, 180), (980, 150),
        (1140, 175), (1320, 145), (1490, 175), (170, 290), (360, 265), (550, 300),
        (750, 270), (940, 295), (1130, 265), (1310, 300), (1500, 270), (120, 410),
        (300, 385), (500, 420), (700, 390), (900, 420), (1100, 390), (1300, 420),
    ]

    DEBAT_PHASE1_SLOT_START_X = 120
    DEBAT_PHASE1_SLOT_START_Y = 520
    DEBAT_PHASE1_SLOT_GAP = 16
    DEBAT_PHASE1_SLOT_ROW_SPACING = 120
    DEBAT_PHASE1_SLOT_MIN_WIDTH = 54
    DEBAT_PHASE1_SLOT_TEXT_PADDING_X = 28
    DEBAT_PHASE1_SLOT_CHAR_WIDTH = 13.5
    DEBAT_PHASE1_SLOT_HEIGHT = 66
    DEBAT_PHASE1_SLOT_ROW_MAX_WIDTH = 1680

    def debat_phase1_word_width(word_text):
        estimated = DEBAT_PHASE1_SLOT_TEXT_PADDING_X + int(len(word_text) * DEBAT_PHASE1_SLOT_CHAR_WIDTH)
        return max(DEBAT_PHASE1_SLOT_MIN_WIDTH, estimated)

    def debat_phase1_get_slot_width(slot_index, slot_word_id):
        if slot_word_id is None:
            return debat_phase1_word_width(DEBAT_PHASE1_TARGET[slot_index])

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
        if len(store.debat_phase1_slots) != len(DEBAT_PHASE1_TARGET):
            store.debat_phase1_success = False
            return

        for i, expected_word in enumerate(DEBAT_PHASE1_TARGET):
            word_id = store.debat_phase1_slots[i]
            if word_id is None:
                store.debat_phase1_success = False
                return

            actual_word = store.debat_phase1_words[word_id]["text"]
            if actual_word != expected_word:
                store.debat_phase1_success = False
                return

        store.debat_phase1_success = True

    def debat_phase1_setup():
        indexed_words = list(enumerate(DEBAT_PHASE1_TARGET))  # (orig_id, text)
        random.shuffle(indexed_words)

        store.debat_phase1_words = [None for _ in DEBAT_PHASE1_TARGET]

        for i, (orig_id, text) in enumerate(indexed_words):
            hx, hy = DEBAT_PHASE1_FLOAT_POSITIONS[i]
            store.debat_phase1_words[orig_id] = {
                "id": orig_id,
                "text": text,
                "home_x": hx,
                "home_y": hy,
            }

        store.debat_phase1_slots = [None for _ in DEBAT_PHASE1_TARGET]
        debat_phase1_refresh_slot_layout()
        store.debat_phase1_success = False

        # IMPORTANT : évite que le rollback te remette l'ancien état / defaults
        renpy.block_rollback()

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

        if current_slot is not None:
            store.debat_phase1_slots[current_slot] = None

        store.debat_phase1_slots[target_slot] = word_id

        # Swap : si le slot cible était occupé
        if occupant is not None and occupant != word_id:
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = occupant
            else:
                # le mot remplacé repart à la banque
                pass

        debat_phase1_update_success()
        debat_phase1_refresh_slot_layout()
        renpy.block_rollback()
        renpy.restart_interaction()


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
        size 52
        color "#F2F6FF"
        text_align 0.5
        outlines [(2, "#062233", 0, 0), (5, "#06101980", 0, 0)]

    style fa_h2 is default
    style fa_h2:
        size 30
        color "#CFE8FF"
        text_align 0.5
        outlines [(2, "#0A1D2B", 0, 0)]

    style fa_hint is default
    style fa_hint:
        size 24
        color "#A8CFE4"
        text_align 0.5
        outlines [(1, "#07141F", 0, 0)]

    style fa_word is default
    style fa_word:
        size 25
        color "#ECF7FF"
        text_align 0.5
        outlines [(2, "#102233", 0, 0)]

    style fa_btn_text is default
    style fa_btn_text:
        size 28
        color "#E6F8FF"
        text_align 0.5
        outlines [(2, "#0C2533", 0, 0)]

    style fa_btn is default
    style fa_btn:
        xpadding 28
        ypadding 14
        background Solid("#153246D0")
        hover_background Solid("#1B4D68F0")
        insensitive_background Solid("#1A1E2688")

    style fa_btn_insensitive_text is fa_btn_text
    style fa_btn_insensitive_text:
        color "#7F8A99"


screen debat_phase1_opening():
    modal True
    zorder 250
    default fa_hovered_word = None

    # --- GARDE ANTI-DESYNC ---
    $ expected = len(DEBAT_PHASE1_TARGET)
    if (debat_phase1_slots is None) or (len(debat_phase1_slots) != expected) or (len(debat_phase1_words) != expected):
        $ debat_phase1_setup()
    elif len(debat_phase1_slot_layout) != len(debat_phase1_slots):
        $ debat_phase1_refresh_slot_layout()

    fixed:
        add Solid("#050810")

        # Vertical grid overlay
        fixed:
            xfill True
            yfill True
            for gx in range(0, 1921, 64):
                add Solid("#1CB7D111"):
                    xpos gx
                    ypos 0
                    xsize 1
                    ysize 1080

            for gx2 in range(32, 1921, 64):
                add Solid("#22D6F208"):
                    xpos gx2
                    ypos 0
                    xsize 1
                    ysize 1080

        # Faint texture/noise style overlay
        fixed:
            xfill True
            yfill True
            for ny in range(0, 1081, 36):
                add Solid("#D8F7FF03"):
                    xpos 0
                    ypos ny
                    xsize 1920
                    ysize 1

        # Vignette approximation
        add Solid("#00000040"):
            xpos 0
            ypos 0
            xsize 1920
            ysize 80
        add Solid("#00000044"):
            xpos 0
            ypos 1000
            xsize 1920
            ysize 80
        add Solid("#00000030"):
            xpos 0
            ypos 0
            xsize 90
            ysize 1080
        add Solid("#00000030"):
            xpos 1830
            ypos 0
            xsize 90
            ysize 1080

    frame:
        xalign 0.5
        yalign 0.03
        xsize 1720
        ypadding 14
        background Solid("#0A1622CC")

        vbox:
            spacing 6
            text "Fatal Assembly":
                xalign 0.5
                style "fa_h1"

            text "Phase 1 – Ouverture : Poser les bases":
                xalign 0.5
                style "fa_h2"

            text "Glisse les mots dans le bon ordre.":
                xalign 0.5
                style "fa_hint"

    add Solid("#38DFFF"):
        xalign 0.5
        ypos 168
        xsize 1680
        ysize 2

    # Panel for word bank visuals
    frame:
        xpos 56
        ypos 88
        xsize 1808
        ysize 370
        background Solid("#1024348A")
        padding (12, 12)

        frame:
            xfill True
            yfill True
            background Solid("#0B152380")

    # Zone banque (drop)
    drag:
        drag_name "word_bank"
        draggable False
        droppable True
        xpos 60
        ypos 80
        xsize 1800
        ysize 360

    draggroup:

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

                        add Solid("#0A1522D8")

                        add Solid("#2AE5FF40"):
                            xfill True
                            yfill True
                            at fa_slot_pulse if debat_phase1_slots[i] is None else fa_slot_filled_glow

                        if debat_phase1_slots[i] is None:
                            add Solid("#64EBFF66"):
                                xpos 0
                                ypos 0
                                xsize slot_w
                                ysize 2
                            add Solid("#64EBFF66"):
                                xpos 0
                                ypos slot_h - 2
                                xsize slot_w
                                ysize 2
                        else:
                            add Solid("#74F3FFAA"):
                                xpos 0
                                ypos 0
                                xsize slot_w
                                ysize 2
                            add Solid("#74F3FFAA"):
                                xpos 0
                                ypos slot_h - 2
                                xsize slot_w
                                ysize 2

                        if debat_phase1_success:
                            add Solid("#63EBFF55") at fa_success_flash

        # --- WORDS ---
        for word in debat_phase1_words:
            $ word_id = word["id"]
            $ slot_index = debat_phase1_find_word_slot(word_id)
            $ wx = debat_phase1_slot_layout[slot_index][0] if slot_index is not None else word["home_x"]
            $ wy = debat_phase1_slot_layout[slot_index][1] if slot_index is not None else word["home_y"]

            $ float_at = None
            if slot_index is None:
                if word_id % 3 == 0:
                    $ float_at = debat_phase1_float_a
                elif word_id % 3 == 1:
                    $ float_at = debat_phase1_float_b
                else:
                    $ float_at = debat_phase1_float_c

            $ is_word_wrong = False
            if slot_index is not None and not debat_phase1_success:
                $ is_word_wrong = (word["text"] != DEBAT_PHASE1_TARGET[slot_index])

            drag:
                drag_name ("word_%d" % word_id)
                xpos wx
                ypos wy
                draggable True
                droppable False
                dragged (lambda drags, drop, wid=word_id: debat_phase1_handle_drop(wid, drags, drop))
                hovered SetScreenVariable("fa_hovered_word", word_id)
                unhovered SetScreenVariable("fa_hovered_word", None)

                child:
                    fixed:
                        fit_first True
                        at float_at if slot_index is None else None

                        frame:
                            padding (14, 10)
                            background Solid("#00000066")
                            at fa_tile_shadow

                            text word["text"]:
                                style "fa_word"
                                xalign 0.5

                        frame:
                            padding (14, 10)
                            background Solid("#1B2D43E8")
                            at fa_tile_hover if fa_hovered_word == word_id else fa_tile_idle

                            fixed:
                                fit_first True

                                add Solid("#74EFFF18"):
                                    xpos 1
                                    ypos 1
                                    xsize debat_phase1_word_width(word["text"]) - 2
                                    ysize 2

                                if debat_phase1_success:
                                    add Solid("#61F0FF44") at fa_success_flash
                                elif is_word_wrong:
                                    add Solid("#FF4D5E22") at fa_error_shake

                                text word["text"]:
                                    style "fa_word"
                                    xalign 0.5

                child_when_dragging:
                    frame:
                        padding (14, 10)
                        background Solid("#2E4562F5")
                        at fa_tile_dragging

                        fixed:
                            fit_first True
                            add Solid("#8AF5FF5A")
                            text word["text"]:
                                style "fa_word"
                                xalign 0.5

    hbox:
        xalign 0.5
        yalign 0.94
        spacing 24

        textbutton "Réinitialiser":
            action Function(debat_phase1_setup)
            style "fa_btn"
            text_style "fa_btn_text"

        textbutton "Valider la proposition":
            sensitive debat_phase1_success
            action Return(True)
            style "fa_btn"
            text_style "fa_btn_text"
            insensitive_text_style "fa_btn_insensitive_text"
            at fa_btn_focus_pulse if debat_phase1_success else None

screen noam_consent_screen():
    modal True
    zorder 260

    add "images/background/debat/noam_agree.png" at adaptive_fullscreen

    on "show" action Play("sound", sfx_victory)
    timer 2.8 action Return(True)
