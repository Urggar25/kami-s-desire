# Mini-jeu : Débat - Phase 1 (Ouverture)

default debat_phase1_slots = []
default debat_phase1_words = []
default debat_phase1_success = False

init python:
    import random

    DEBAT_PHASE1_TARGET = [
        "Autoriser",
        "le",
        "transport,",
        "la",
        "vente",
        "et",
        "l’échange",
        "de",
        "marchandises",
        "entre",
        "les",
        "districts",
        "Le",
        "système",
        "actuel",
        "de",
        "distribution",
        "de",
        "matériel",
        "et",
        "de",
        "denrées",
        "est",
        "aboli",
    ]

    DEBAT_PHASE1_FLOAT_POSITIONS = [
        (90, 120), (260, 90), (430, 130), (620, 95), (800, 130), (980, 100),
        (1140, 125), (1320, 95), (1490, 125), (170, 240), (360, 215), (550, 250),
        (750, 220), (940, 245), (1130, 215), (1310, 250), (1500, 220), (120, 360),
        (300, 335), (500, 370), (700, 340), (900, 370), (1100, 340), (1300, 370),
    ]

    DEBAT_PHASE1_SLOT_POSITIONS = [
        (120 + (i % 12) * 135, 520 + (i // 12) * 120) for i in range(24)
    ]

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
        indexed_words = list(enumerate(DEBAT_PHASE1_TARGET))
        random.shuffle(indexed_words)

        store.debat_phase1_words = []
        for i, (_, text) in enumerate(indexed_words):
            hx, hy = DEBAT_PHASE1_FLOAT_POSITIONS[i]
            store.debat_phase1_words.append({
                "id": i,
                "text": text,
                "home_x": hx,
                "home_y": hy,
            })

        store.debat_phase1_slots = [None for _ in DEBAT_PHASE1_TARGET]
        store.debat_phase1_success = False

    def debat_phase1_handle_drop(word_id, drags, drop):
        if drop is None:
            return

        target_name = getattr(drop, "drag_name", "")
        current_slot = debat_phase1_find_word_slot(word_id)

        if target_name == "word_bank":
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = None
                debat_phase1_update_success()
                renpy.restart_interaction()
            return

        if not target_name.startswith("slot_"):
            return

        target_slot = int(target_name.split("_")[1])
        occupant = store.debat_phase1_slots[target_slot]

        if current_slot is not None:
            store.debat_phase1_slots[current_slot] = None

        store.debat_phase1_slots[target_slot] = word_id

        if occupant is not None and occupant != word_id:
            if current_slot is not None:
                store.debat_phase1_slots[current_slot] = occupant

        debat_phase1_update_success()
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

screen debat_phase1_opening():
    modal True
    zorder 250

    add Solid("#090b12")

    frame:
        xalign 0.5
        yalign 0.04
        xsize 1720
        ypadding 12
        background Solid("#151a2a")

        vbox:
            spacing 6
            text "Phase 1 – Ouverture : Poser les bases" size 38 color "#E9ECFF"
            text "Reconstituez la proposition en glissant les mots dans le bon ordre." size 28 color "#C8D0FF"

    drag:
        drag_name "word_bank"
        draggable False
        droppable True
        xpos 60
        ypos 80
        xsize 1800
        ysize 360

    draggroup:
        for i in range(24):
            $ sx, sy = DEBAT_PHASE1_SLOT_POSITIONS[i]
            drag:
                drag_name "slot_[i]"
                draggable False
                droppable True
                xpos sx
                ypos sy
                xsize 122
                ysize 66

                frame:
                    xfill True
                    yfill True
                    background Solid("#1E243A")

        for word in debat_phase1_words:
            $ slot_index = debat_phase1_find_word_slot(word["id"])
            $ wx = DEBAT_PHASE1_SLOT_POSITIONS[slot_index][0] if slot_index is not None else word["home_x"]
            $ wy = DEBAT_PHASE1_SLOT_POSITIONS[slot_index][1] if slot_index is not None else word["home_y"]
            drag:
                drag_name "word_[word['id']]"
                xpos wx
                ypos wy
                draggable True
                droppable False
                dragged Function(debat_phase1_handle_drop, word["id"])

                if slot_index is None:
                    if word["id"] % 3 == 0:
                        at debat_phase1_float_a
                    elif word["id"] % 3 == 1:
                        at debat_phase1_float_b
                    else:
                        at debat_phase1_float_c

                frame:
                    padding (12, 10)
                    background Solid("#2A3352")
                    text word["text"] size 25 color "#FFFFFF"

    text ".":
        xpos 1748
        ypos 535
        size 64
        color "#E9ECFF"

    text ".":
        xpos 1748
        ypos 655
        size 64
        color "#E9ECFF"

    hbox:
        xalign 0.5
        yalign 0.94
        spacing 24

        textbutton "Réinitialiser":
            action Function(debat_phase1_setup)

        textbutton "Valider la proposition":
            sensitive debat_phase1_success
            action Return(True)
