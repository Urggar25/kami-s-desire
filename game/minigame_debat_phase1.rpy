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

    # --- Ajustements layout demandés (mesurés) ---
    # Baisser banque / mots / slots sans tout exploser.
    DEBAT_PHASE1_BANK_Y = 150             # anciennement 88
    DEBAT_PHASE1_WORDS_Y_OFFSET = 40      # descend un peu les mots
    DEBAT_PHASE1_WORDS_X_SPREAD = 1.03    # écarte un peu les mots

    DEBAT_PHASE1_SLOT_START_X = 150
    DEBAT_PHASE1_SLOT_START_Y = 600       # anciennement 520 (trop haut)
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

            # Espacer un peu + baisser les mots (sans dérégler l'écran)
            hx = int(960 + (hx - 960) * DEBAT_PHASE1_WORDS_X_SPREAD)
            hy = int(hy + DEBAT_PHASE1_WORDS_Y_OFFSET)

            store.debat_phase1_words[orig_id] = {
                "id": orig_id,
                "text": text,
                "home_x": hx,
                "home_y": hy,
            }

        store.debat_phase1_slots = [None for _ in DEBAT_PHASE1_TARGET]
        debat_phase1_refresh_slot_layout()
        store.debat_phase1_success = False

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

        if occupant is not None and occupant != word_id:
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = occupant

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
        # => suppression du double effet : un seul outline net
        outlines [(3, "#000000AA", 0, 0)]

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
        # Contraste ++
        color "#FFFFFF"
        text_align 0.5
        outlines [(3, "#000000CC", 0, 0)]

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
                add Solid("#1CB7D111", xsize=1, ysize=1080):
                    xpos gx
                    ypos 0
            for gx2 in range(32, 1921, 64):
                add Solid("#22D6F208", xsize=1, ysize=1080):
                    xpos gx2
                    ypos 0

        # Faint texture/noise style overlay
        fixed:
            xfill True
            yfill True
            for ny in range(0, 1081, 36):
                add Solid("#D8F7FF03", xsize=1920, ysize=1):
                    xpos 0
                    ypos ny

        # Vignette approximation
        add Solid("#00000040", xsize=1920, ysize=80):
            xpos 0
            ypos 0
        add Solid("#00000044", xsize=1920, ysize=80):
            xpos 0
            ypos 1000
        add Solid("#00000030", xsize=90, ysize=1080):
            xpos 0
            ypos 0
        add Solid("#00000030", xsize=90, ysize=1080):
            xpos 1830
            ypos 0

    frame:
        xalign 0.5
        yalign 0.03
        xsize 1720
        ypadding 14
        background Solid("#0A1622CC")

        vbox:
            spacing 6
            # Sous-titre supprimé : on garde juste le titre
            text "Fatal Assembly":
                xalign 0.0
                style "fa_h1"

    add Solid("#38DFFF", xsize=1680, ysize=2):
        xalign 0.5
        ypos 120

    # Panel for word bank visuals (abaissé)
    frame:
        xpos 56
        ypos DEBAT_PHASE1_BANK_Y
        xsize 1808
        ysize 370
        background Solid("#1024348A")
        padding (12, 12)

        frame:
            xfill True
            yfill True
            background Solid("#0B152380")

    # Zone banque (drop) (abaissée)
    drag:
        drag_name "word_bank"
        draggable False
        droppable True
        xpos 60
        ypos (DEBAT_PHASE1_BANK_Y - 10)
        xsize 1800
        ysize 370

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

            # Largeur stable pour éviter les tiles "bizarres"
            $ ww = debat_phase1_word_width(word["text"])
            $ th = 46

            drag:
                drag_name ("word_%d" % word_id)
                xpos wx
                ypos wy
                draggable True
                droppable False
                dragged (lambda drags, drop, wid=word_id: debat_phase1_handle_drop(wid, drags, drop))
                hovered SetScreenVariable("fa_hovered_word", word_id)
                unhovered SetScreenVariable("fa_hovered_word", None)

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
                    if fa_hovered_word == word_id:
                        frame:
                            xsize ww
                            ysize th
                            background Solid("#1B2D43E8")
                            at fa_tile_hover

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

                                text word["text"]:
                                    style "fa_word"
                                    xalign 0.5
                                    yalign 0.5
                    else:
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

                                text word["text"]:
                                    style "fa_word"
                                    xalign 0.5
                                    yalign 0.5

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
            if debat_phase1_success:
                at fa_btn_focus_pulse


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
