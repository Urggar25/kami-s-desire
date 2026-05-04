# Mini-jeu Jour 6_0_1 : Signal Instable

default j601_signal_timer = 38.0
default j601_signal_stability = 55
default j601_signal_drift = 3
default j601_signal_done = False
default j601_signal_success = False
default j601_signal_pulses = 0

init python:
    import random

    def j601_signal_reset():
        store.j601_signal_timer = 38.0
        store.j601_signal_stability = 55
        store.j601_signal_drift = 3
        store.j601_signal_done = False
        store.j601_signal_success = False
        store.j601_signal_pulses = 0

    def j601_signal_tick(boost=0):
        if store.j601_signal_done:
            return

        wobble = random.randint(-2, 2)
        fatigue = min(6, int((38.0 - store.j601_signal_timer) / 7.0))
        loss = store.j601_signal_drift + fatigue + wobble - boost

        store.j601_signal_stability = max(0, min(100, store.j601_signal_stability - loss))
        store.j601_signal_timer = max(0.0, store.j601_signal_timer - 0.30)
        store.j601_signal_pulses += 1

        if store.j601_signal_stability <= 0:
            store.j601_signal_done = True
            store.j601_signal_success = False
            return

        if store.j601_signal_timer <= 0.0:
            store.j601_signal_done = True
            store.j601_signal_success = store.j601_signal_stability >= 22

screen j601_signal_instable_screen():
    modal True
    zorder 250

    add Solid("#060A14DD")

    frame:
        xalign 0.5
        yalign 0.10
        xsize 1100
        ysize 130
        background Solid("#0F1728DD")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8

            text "SIGNAL INSTABLE":
                xalign 0.5
                size 48
                color "#D8F6FF"

            text "Maintenez la stabilité du lien de Kami.":
                xalign 0.5
                size 24
                color "#B9D3E6"

    frame:
        xalign 0.5
        yalign 0.33
        xsize 1180
        ysize 220
        background Solid("#0D1320C8")

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            text "Temps restant : [j601_signal_timer:.1f]s":
                xalign 0.5
                size 32
                color "#D4EFFF"

            bar:
                xalign 0.5
                xsize 1000
                ysize 26
                value AnimatedValue(value=j601_signal_stability, range=100, delay=0.15)
                left_bar Solid("#42D8FF")
                right_bar Solid("#1D2B44")

            text "Stabilité : [j601_signal_stability]%":
                xalign 0.5
                size 28
                color "#9FE7FF"

    hbox:
        xalign 0.5
        yalign 0.72
        spacing 36

        textbutton "Calibrer (+2)":
            xsize 260
            ysize 90
            action [Function(j601_signal_tick, 2)]

        textbutton "Filtrer (+3)":
            xsize 260
            ysize 90
            action [Function(j601_signal_tick, 3)]

        textbutton "Synchroniser (+4)":
            xsize 260
            ysize 90
            action [Function(j601_signal_tick, 4)]

    timer 0.30 repeat True action Function(j601_signal_tick, 0)

    if j601_signal_done:
        timer 0.2 action Return(j601_signal_success)

label j601_play_signal_instable:
    $ j601_signal_reset()
    $ result_signal = renpy.call_screen("j601_signal_instable_screen")
    return result_signal
