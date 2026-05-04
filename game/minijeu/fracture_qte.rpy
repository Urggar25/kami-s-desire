# Mini-jeu Jour 6_0_1 : Fracture QTE

default j601_qte_sequence = ["K_UP", "K_LEFT", "K_RIGHT", "K_DOWN"]
default j601_qte_index = 0
default j601_qte_timer = 38.0
default j601_qte_hits = 0
default j601_qte_misses = 0

define j601_qte_symbols = {
    "K_UP": "↑",
    "K_LEFT": "←",
    "K_RIGHT": "→",
    "K_DOWN": "↓",
}

init python:
    import random

    def j601_qte_reset():
        keys = ["K_UP", "K_LEFT", "K_RIGHT", "K_DOWN"]
        random.shuffle(keys)
        store.j601_qte_sequence = keys[:]
        store.j601_qte_index = 0
        store.j601_qte_timer = 38.0
        store.j601_qte_hits = 0
        store.j601_qte_misses = 0

    def j601_qte_expected():
        if store.j601_qte_index >= len(store.j601_qte_sequence):
            return None
        return store.j601_qte_sequence[store.j601_qte_index]

    def j601_qte_press(key_name):
        expected = j601_qte_expected()
        if expected is None:
            return

        if key_name == expected:
            store.j601_qte_hits += 1
            store.j601_qte_index += 1
        else:
            store.j601_qte_misses += 1

    def j601_qte_tick():
        if store.j601_qte_index >= len(store.j601_qte_sequence):
            return
        store.j601_qte_timer = max(0.0, store.j601_qte_timer - 0.15)

screen j601_fracture_qte_screen():
    modal True
    zorder 250

    add Solid("#090C18E0")

    frame:
        xalign 0.5
        yalign 0.13
        xsize 1000
        ysize 140
        background Solid("#121A2ED9")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            text "FRACTURE // LAPSUS EN COURS":
                xalign 0.5
                size 42
                color "#FFE1EE"
            text "Repérez les glitches de Kami en temps réel.":
                xalign 0.5
                size 24
                color "#F2BACF"

    frame:
        xalign 0.5
        yalign 0.38
        xsize 700
        ysize 240
        background Solid("#1A1322D0")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            $ expected = j601_qte_expected()
            if expected:
                text "Entrée attendue":
                    xalign 0.5
                    size 28
                    color "#F9D7E5"
                text "[j601_qte_symbols[expected]]":
                    xalign 0.5
                    size 96
                    color "#FFFFFF"
            else:
                text "Séquence complétée":
                    xalign 0.5
                    size 42
                    color "#B9FFD0"

            text "Temps : [j601_qte_timer:.1f]s   |   Succès : [j601_qte_hits]/4   |   Erreurs : [j601_qte_misses]":
                xalign 0.5
                size 24
                color "#E6DDE3"

    key "K_UP" action Function(j601_qte_press, "K_UP")
    key "K_LEFT" action Function(j601_qte_press, "K_LEFT")
    key "K_RIGHT" action Function(j601_qte_press, "K_RIGHT")
    key "K_DOWN" action Function(j601_qte_press, "K_DOWN")

    timer 0.15 repeat True action Function(j601_qte_tick)

    if j601_qte_index >= 4 or j601_qte_timer <= 0.0:
        timer 0.2 action Return(j601_qte_hits)

label j601_play_fracture_qte:
    $ j601_qte_reset()
    $ result_qte = renpy.call_screen("j601_fracture_qte_screen")
    return result_qte
