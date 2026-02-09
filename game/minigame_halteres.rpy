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
default mg_time_left = 60.0
default mg_zone_start = 0.40
default mg_zone_end = 0.60
default mg_perfect_margin = 0.05

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
            else:
                store.mg_progress += 1
                store.mg_feedback = "Correct."
        else:
            store.mg_energy = max(0.0, store.mg_energy - 0.15)
            store.mg_feedback = "Raté..."

        if store.mg_reps >= store.mg_target_reps:
            store.mg_done = True

    def mg_stat_chance():
        max_progress = float(store.mg_target_reps * 2)
        ratio = 0.0
        if max_progress > 0:
            ratio = min(1.0, store.mg_progress / max_progress)
        return min(0.8, 0.2 + (0.6 * ratio))

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

    if mg_done:
        timer 0.05 action Return()

    frame:
        style "frame"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 520

        vbox:
            spacing 16
            xalign 0.5

            text "ENTRAÎNEMENT AUX HALTÈRES" style "label_text" xalign 0.5

            fixed:
                xsize 340
                ysize 260
                xalign 0.5
                if renpy.has_image("noam neutre"):
                    add "noam neutre" xalign 0.5 yalign 0.5
                else:
                    text "NOAM" xalign 0.5 yalign 0.5

            text "BARRE D'ÉNERGIE" xalign 0.5
            bar value mg_energy range 1.0 xsize 600

            text "BARRE DE RYTHME" xalign 0.5
            fixed:
                xsize 600
                ysize 28
                add Solid("#2b2b2b")
                $ zone_width = (mg_zone_end - mg_zone_start)
                add Solid("#3fa34d") xpos int(mg_zone_start * 600) xsize int(zone_width * 600) ysize 28
                add Solid("#f5f5f5") xpos int(mg_value * 600) xsize 6 ysize 28

            text "⬆   ⬇" xalign 0.5
            text "(CLIC AU BON MOMENT)" xalign 0.5
            text "Compteur répétitions : [mg_reps]/[mg_target_reps]" xalign 0.5

            if mg_feedback:
                text "[mg_feedback]" xalign 0.5

            textbutton "CLIC" action Function(mg_click) xalign 0.5

label minijeu_halteres:
    $ mg_reset()
    call screen minijeu_halteres

    $ gained_physique = False
    $ chance_physique = mg_stat_chance()
    if renpy.random.random() < chance_physique:
        $ stat_physique += 1
        $ gained_physique = True

    if gained_physique:
        "Ta statistique Physique augmente."
    else:
        "Tu sens la fatigue, mais tu sais que ça finit par payer."

    $ scene_label = mg_pick_scene()
    if scene_label:
        call expression scene_label
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
