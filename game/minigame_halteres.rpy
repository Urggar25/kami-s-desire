default persistent.pegi18 = False
default stat_physique = 0

default mg_target_reps = 10
default mg_reps = 0
default mg_progress = 0
default mg_energy = 1.0
default mg_value = 0.0
default mg_direction = 1
default mg_speed = 0.9
default mg_done = False
default mg_feedback = ""
default mg_feedback_color = "#f5f5f5"
default mg_time_left = 60.0
default mg_zone_start = 0.40
default mg_zone_end = 0.60
default mg_perfect_margin = 0.05
default mg_skip_scene_pick = False
default mg_was_success = False
default sport_events_pool = [
    "sport_event_001",
    "sport_event_002",
    "sport_event_003",
    "sport_event_004",
    "sport_event_005",
    "sport_event_006",
    "sport_event_007",
    "sport_event_008",
    "sport_event_009",
]
default sport_events_seen = []

default scenes_normales = ["scene_mg_normale_1"]
default scenes_patreon = ["scene_mg_patreon_1"]
default scenes_sexy = ["scene_mg_sexy_1"]

init python:
    def mg_reset():
        store.mg_reps = 0
        store.mg_progress = 0
        store.mg_energy = 1.0
        store.mg_value = 0.0
        store.mg_direction = 1
        store.mg_done = False
        store.mg_feedback = ""
        store.mg_feedback_color = "#f5f5f5"
        store.mg_time_left = 60.0

    def mg_tick(dt=0.02):
        if store.mg_done:
            return

        store.mg_time_left = max(0.0, store.mg_time_left - dt)
        store.mg_value += store.mg_direction * store.mg_speed * dt

        if store.mg_value >= 1.0:
            store.mg_value = 1.0
            store.mg_direction = -1
        elif store.mg_value <= 0.0:
            store.mg_value = 0.0
            store.mg_direction = 1

        if store.mg_time_left <= 0 or store.mg_reps >= store.mg_target_reps or store.mg_energy <= 0:
            store.mg_done = True

    def mg_click():
        if store.mg_done:
            return

        store.mg_reps += 1
        val = store.mg_value
        if store.mg_zone_start <= val <= store.mg_zone_end:
            center = (store.mg_zone_start + store.mg_zone_end) / 2.0
            if abs(val - center) <= store.mg_perfect_margin:
                store.mg_progress += 2
                store.mg_feedback = "Parfait !"
                store.mg_feedback_color = "#5ad45a"
            else:
                store.mg_progress += 1
                store.mg_feedback = "Correct."
                store.mg_feedback_color = "#f2c94c"
        else:
            store.mg_energy = max(0.0, store.mg_energy - 0.15)
            store.mg_feedback = "Raté..."
            store.mg_feedback_color = "#ff6b6b"

        if store.mg_reps >= store.mg_target_reps:
            store.mg_done = True

    def mg_is_successful():
        return store.mg_progress >= store.mg_target_reps

    def sport_events_left_count():
        return len(store.sport_events_pool)

    def pop_random_sport_event():
        if not store.sport_events_pool:
            return None
        picked = renpy.random.choice(store.sport_events_pool)
        store.sport_events_pool.remove(picked)
        store.sport_events_seen.append(picked)
        return picked

    def mg_pick_scene():
        pools = []
        if store.scenes_normales:
            pools.append(store.scenes_normales)
        if store.scenes_patreon:
            pools.append(store.scenes_patreon)
        if persistent.pegi18 and store.scenes_sexy:
            pools.append(store.scenes_sexy)

        if not pools:
            return None
        pool = renpy.random.choice(pools)
        return renpy.random.choice(pool)

screen minijeu_halteres():
    modal True
    zorder 200

    timer 0.02 repeat True action Function(mg_tick, 0.02)
    key "mouseup_1" action Function(mg_click)

    if mg_done:
        timer 0.05 action Return()

    frame:
        style "frame"
        xalign 0.5
        yalign 0.5
        xsize 980
        ysize 560

        vbox:
            spacing 14
            xalign 0.5

            text "ENTRAÎNEMENT AUX HALTÈRES" style "label_text" xalign 0.5
            text "Clique au bon moment pour enchaîner les répétitions." xalign 0.5

            fixed:
                xsize 620
                ysize 240
                xalign 0.5
                add Solid("#1c1c1c") xsize 620 ysize 240 xalign 0.5 yalign 0.5
                $ dumbbell_y = int(160 - (mg_value * 110))
                add Solid("#8f99a3") xpos 140 ypos dumbbell_y-10 xsize 40 ysize 40
                add Solid("#e6e6e6") xpos 180 ypos dumbbell_y xsize 260 ysize 18
                add Solid("#8f99a3") xpos 440 ypos dumbbell_y-10 xsize 40 ysize 40
                add Solid("#2d2d2d") xpos 130 ypos dumbbell_y-14 xsize 60 ysize 48
                add Solid("#2d2d2d") xpos 440 ypos dumbbell_y-14 xsize 60 ysize 48
                add Solid("#3f3f3f") xpos 200 ypos 190 xsize 220 ysize 6
                if renpy.has_image("noam neutre"):
                    add "noam neutre" xpos 30 yalign 1.0 zoom 0.5
                else:
                    text "NOAM" xpos 40 yalign 1.0

            hbox:
                spacing 24
                xalign 0.5
                vbox:
                    spacing 8
                    text "Énergie" xalign 0.0
                    bar value mg_energy range 1.0 xsize 520
                vbox:
                    spacing 8
                    text "Temps" xalign 0.0
                    bar value mg_time_left range 60.0 xsize 200

            text "Rythme" xalign 0.5
            fixed:
                xsize 720
                ysize 30
                add Solid("#2b2b2b") xsize 720 ysize 30
                $ zone_width = (mg_zone_end - mg_zone_start)
                add Solid("#3fa34d") xpos int(mg_zone_start * 720) xsize int(zone_width * 720) ysize 30
                add Solid("#f5f5f5") xpos int(mg_value * 720) xsize 8 ysize 30

            text "⬆   ⬇  (clic ou touche)" xalign 0.5
            text "Répétitions : [mg_reps]/[mg_target_reps]" xalign 0.5

            if mg_feedback:
                text "[mg_feedback]" xalign 0.5 color mg_feedback_color

            textbutton "POUSSER" action Function(mg_click) xalign 0.5


screen physique_gain_anim():

    zorder 260
    modal True

    add Solid("#0008")

    frame at argument_unlock_appear:
        xalign 0.5
        yalign 0.5
        xmaximum 900
        padding (60, 40)
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

        vbox:
            spacing 12
            text "STAT EN HAUSSE" at argument_unlock_pulse size 38 xalign 0.5 color "#be9c36"
            text "Physique +1" size 48 xalign 0.5 color "#000000"

    timer 2.0 action Hide("physique_gain_anim")

label minijeu_halteres:
    $ mg_reset()
    call screen minijeu_halteres

    $ mg_was_success = mg_is_successful()
    $ gained_physique = False
    if renpy.random.random() < 0.30:
        $ stat_physique += 1
        $ gained_physique = True

    if gained_physique:
        show screen physique_gain_anim
        pause 2.0
        hide screen physique_gain_anim
        "Ta statistique Physique augmente."
    else:
        "Tu sens la fatigue, mais tu sais que ça finit par payer."

    if mg_skip_scene_pick:
        $ scene_label = None
        $ mg_skip_scene_pick = False
    else:
        $ scene_label = mg_pick_scene()
    if scene_label:
        call expression scene_label from _call_expression
    return

label scene_mg_normale_1:
    "Iris t'adresse un regard fier, comme si elle voyait les efforts s'accumuler."
    return

label scene_mg_patreon_1:
    "Elias rectifie ta posture d'une main sûre, sans un mot."
    return

label scene_mg_sexy_1:
    "Le contact s'attarde une seconde de trop, et la chaleur monte."
    return

label sport_event_001:
    $ unlock_gallery_image("sport001")
    "Tu termines ta série avec Elias qui corrige ton rythme sans te lâcher du regard."
    return

label sport_event_002:
    $ unlock_gallery_image("sport002")
    "Iris te lance un défi de vitesse au rameur et t'arrache un rire malgré la fatigue."
    return

label sport_event_003:
    $ unlock_gallery_image("sport003")
    "Un entraînement de gainage tourne à la compétition improvisée entre vous tous."
    return

label sport_event_004:
    $ unlock_gallery_image("sport004")
    "Tu croises Elias tard, et vous faites une séance silencieuse, épaule contre épaule."
    return

label sport_event_005:
    $ unlock_gallery_image("sport005")
    "Iris commente chacun de tes mouvements avec une ironie qui te pousse à tenir."
    return

label sport_event_006:
    $ unlock_gallery_image("sport006")
    "Tu termines sur le banc, vidé, pendant qu'Elias te tend une serviette en souriant."
    return

label sport_event_007:
    $ unlock_gallery_image("sport007")
    "Une coupure de courant stoppe les machines et vous finissez l'entraînement dans l'ombre."
    return

label sport_event_008:
    $ unlock_gallery_image("sport008")
    "Vous improvisez un mini match sur le terrain, et la tension retombe enfin."
    return

label sport_event_009:
    $ unlock_gallery_image("sport009")
    "Dernière répétition, dernier souffle ; tu sens que ton corps commence vraiment à changer."
    return
