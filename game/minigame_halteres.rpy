default persistent.pegi18 = False
default stat_physique = 0

# --- Config réutilisable (modifiée par minijeu_halteres_run) ---
default mg_title = "ENTRAÎNEMENT AUX HALTÈRES"
default mg_subtitle = "Synchronise ton effort avec la zone verte pour valider chaque répétition."
default mg_bg = "gym_bg.png"
default mg_duration = 60.0
default mg_base_speed = 0.9
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
default mg_quick_menu_prev = True
default mg_combo = 0
default mg_combo_max = 0
default mg_perfects = 0
default mg_misses = 0
default mg_flash = 0.0
default sport_events_pool = [
    "sport_event_001",
    "sport_event_002",
    "sport_event_003",
    "sport_event_004",
    "sport_event_005",
]
default sport_events_seen = []

default scenes_normales = ["scene_mg_normale_1"]
default scenes_patreon = ["scene_mg_patreon_1"]
default scenes_sexy = []

init python:
    def mg_get_ui_font():
        if renpy.loadable("game/fonts/Orbitron-Regular.ttf"):
            return "fonts/Orbitron-Regular.ttf"
        return "fonts/day_font.ttf"

    def mg_configure(target_reps=10, duration=60.0, base_speed=0.9, title=None, subtitle=None, bg=None):
        store.mg_target_reps = target_reps
        store.mg_duration = float(duration)
        store.mg_base_speed = float(base_speed)
        if title: store.mg_title = title
        if subtitle: store.mg_subtitle = subtitle
        if bg: store.mg_bg = bg

    def mg_reset():
        store.mg_reps = 0
        store.mg_progress = 0
        store.mg_energy = 1.0
        store.mg_value = 0.0
        store.mg_direction = 1
        store.mg_speed = store.mg_base_speed
        store.mg_done = False
        store.mg_feedback = ""
        store.mg_feedback_color = "#f5f5f5"
        store.mg_time_left = store.mg_duration
        store.mg_zone_start = 0.40
        store.mg_zone_end = 0.60
        store.mg_combo = 0
        store.mg_combo_max = 0
        store.mg_perfects = 0
        store.mg_misses = 0
        store.mg_flash = 0.0

    def mg_live_challenges():
        return [
            ("Combo x5", store.mg_combo_max >= 5),
            ("Zéro raté", False, store.mg_misses > 0),
            ("4 frappes parfaites", store.mg_perfects >= 4),
        ]

    def mg_final_challenges():
        return [
            ("Combo x5", store.mg_combo_max >= 5),
            ("Zéro raté", store.mg_misses == 0),
            ("4 frappes parfaites", store.mg_perfects >= 4),
        ]

    def mg_tick(dt=0.02):
        if store.mg_done:
            return

        store.mg_time_left = max(0.0, store.mg_time_left - dt)
        store.mg_value += store.mg_direction * store.mg_speed * dt

        if store.mg_flash > 0.0:
            store.mg_flash = max(0.0, store.mg_flash - dt)

        if store.mg_value >= 1.0:
            store.mg_value = 1.0
            store.mg_direction = -1
        elif store.mg_value <= 0.0:
            store.mg_value = 0.0
            store.mg_direction = 1

        if store.mg_time_left <= 0 or store.mg_reps >= store.mg_target_reps or store.mg_energy <= 0:
            store.mg_done = True

    def mg_relocate_zone():
        # La zone se déplace et rétrécit avec la progression (difficulté).
        progress = store.mg_reps / float(max(1, store.mg_target_reps))
        width = max(0.10, 0.20 - progress * 0.08)
        center = renpy.random.uniform(0.22 + width, 0.78 - width)
        store.mg_zone_start = center - width / 2.0
        store.mg_zone_end = center + width / 2.0
        # Vitesse croissante
        store.mg_speed = store.mg_base_speed + progress * 0.55

    def mg_click():
        if store.mg_done:
            return

        store.mg_reps += 1
        val = store.mg_value
        if store.mg_zone_start <= val <= store.mg_zone_end:
            center = (store.mg_zone_start + store.mg_zone_end) / 2.0
            store.mg_combo += 1
            store.mg_combo_max = max(store.mg_combo_max, store.mg_combo)
            combo_bonus = 1 if store.mg_combo >= 3 else 0

            if abs(val - center) <= store.mg_perfect_margin:
                store.mg_perfects += 1
                store.mg_progress += 2 + combo_bonus
                store.mg_feedback = (kd_tr("PARFAIT !") + " x%d" % store.mg_combo) if store.mg_combo >= 2 else kd_tr("PARFAIT !")
                store.mg_feedback_color = "#5ad45a"
                store.mg_flash = 0.18
                renpy.play("audio/sfx_clap.mp3", channel="sound")
            else:
                store.mg_progress += 1 + combo_bonus
                store.mg_feedback = (kd_tr("Correct.") + " x%d" % store.mg_combo) if store.mg_combo >= 2 else kd_tr("Correct.")
                store.mg_feedback_color = "#f2c94c"
                renpy.play("audio/sfx_beep.mp3", channel="sound")
        else:
            store.mg_misses += 1
            store.mg_combo = 0
            store.mg_energy = max(0.0, store.mg_energy - 0.15)
            store.mg_feedback = kd_tr("Raté...")
            store.mg_feedback_color = "#ff6b6b"
            renpy.play("audio/sfx_drop.mp3", channel="sound")

        mg_relocate_zone()

        if store.mg_reps >= store.mg_target_reps:
            store.mg_done = True

    def mg_is_successful():
        return store.mg_progress >= store.mg_target_reps

    def sport_events_left_count():
        return len([event for event in store.sport_events_pool if event not in store.NSFW_SPORT_EVENTS])

    def pop_random_sport_event():
        safe_events = [event for event in store.sport_events_pool if event not in store.NSFW_SPORT_EVENTS]
        if not safe_events:
            return None
        picked = renpy.random.choice(safe_events)
        store.sport_events_pool.remove(picked)
        store.sport_events_seen.append(picked)
        return picked

    def mg_pick_scene():
        pools = []
        if store.scenes_normales:
            pools.append(store.scenes_normales)
        if store.scenes_patreon:
            pools.append(store.scenes_patreon)
        if not pools:
            return None
        pool = renpy.random.choice(pools)
        return renpy.random.choice(pool)

    NSFW_SPORT_EVENTS = {
        "sport_event_006",
        "sport_event_007",
        "sport_event_008",
        "sport_event_009",
    }

transform mg_bg_idle:
    alpha 0.82
    linear 3.0 alpha 0.94
    linear 3.0 alpha 0.82
    repeat

transform mg_panel_fade(delay=0.0):
    alpha 0.0
    yoffset 24
    pause delay
    easeout 0.35 alpha 1.0 yoffset 0

transform mg_hud_pulse:
    zoom 1.0
    linear 0.35 zoom 1.02
    linear 0.35 zoom 1.0
    repeat

transform mg_feedback_pop:
    alpha 0.0
    zoom 0.85
    easeout 0.18 alpha 1.0 zoom 1.0

style mg_title_text is default:
    color "#d8ecff"
    size 38
    outlines [(2, "#051321", 0, 0)]

style mg_subtitle_text is default:
    color "#97b5d5"
    size 21
    outlines [(1, "#051321", 0, 0)]

style mg_label_text is default:
    color "#9ec4e9"
    size 20
    outlines [(1, "#02101d", 0, 0)]

style mg_value_text is default:
    color "#dff1ff"
    size 24
    outlines [(2, "#04131f", 0, 0)]

screen minijeu_halteres():
    modal True
    zorder 200

    timer 0.02 repeat True action Function(mg_tick, 0.02)
    key "mouseup_1" action Function(mg_click)

    if mg_done:
        timer 0.05 action Return()

    default mg_font = mg_get_ui_font()

    add mg_bg
    add Solid("#020912b0")
    add Solid("#1f5fa833") at mg_bg_idle

    if mg_flash > 0.0:
        add Solid("#5ad45a2e")

    use mk_challenge_hud(mg_live_challenges(), 24, 240)
    use mk_help_button("tuto_halteres")

    frame at mg_panel_fade(0.0):
        xalign 0.5
        yalign 0.06
        xsize 1480
        ysize 165
        background Solid("#071827c0")
        padding (40, 22)

        vbox:
            spacing 8
            text kd_tr(mg_title) style "mg_title_text" xalign 0.5 font mg_font
            text kd_tr(mg_subtitle) style "mg_subtitle_text" xalign 0.5 font mg_font

    hbox:
        xalign 0.5
        yalign 0.57
        spacing 30

        frame at mg_panel_fade(0.08):
            xsize 980
            ysize 650
            background Solid("#07131fcf")
            padding (26, 26)

            fixed:
                xfill True
                yfill True
                add Solid("#0f2439") xsize 928 ysize 598
                add Solid("#1f8fff18") xsize 928 ysize 598 at mg_bg_idle

                $ dumbbell_y = int(440 - (mg_value * 300))
                add Solid("#9fb3c7") xpos 320 ypos dumbbell_y xsize 280 ysize 22
                add Solid("#232f3a") xpos 264 ypos dumbbell_y-13 xsize 66 ysize 48
                add Solid("#232f3a") xpos 595 ypos dumbbell_y-13 xsize 66 ysize 48
                add Solid("#576572") xpos 280 ypos dumbbell_y-9 xsize 40 ysize 40
                add Solid("#576572") xpos 604 ypos dumbbell_y-9 xsize 40 ysize 40
                add Solid("#57e86c") xpos 300 ypos 540 xsize 320 ysize 6 at mg_hud_pulse

                if renpy.has_image("noam neutre"):
                    add "noam neutre" xpos 40 yalign 1.0 zoom 0.82
                else:
                    text "NOAM" xpos 68 yalign 1.0 style "mg_value_text" font mg_font

        vbox at mg_panel_fade(0.14):
            spacing 20

            frame:
                xsize 470
                ysize 150
                background Solid("#06111dd8")
                padding (20, 18)

                vbox:
                    spacing 8
                    hbox:
                        spacing 24
                        text "RÉPÉTITIONS" style "mg_label_text" font mg_font
                        if mg_combo >= 2:
                            text "COMBO x[mg_combo]" style "mg_label_text" color "#5ad45a" font mg_font at mg_hud_pulse
                    text "[mg_reps]/[mg_target_reps]" style "mg_value_text" xalign 0.5 font mg_font
                    if mg_feedback:
                        text kd_tr(mg_feedback) at mg_feedback_pop style "mg_subtitle_text" color mg_feedback_color xalign 0.5 font mg_font

            frame:
                xsize 470
                ysize 308
                background Solid("#06111dd8")
                padding (20, 18)

                vbox:
                    spacing 14

                    text "ÉNERGIE // CHARGE MUSCULAIRE" style "mg_label_text" font mg_font
                    fixed:
                        xsize 430
                        ysize 40
                        add Solid("#0d2235") xsize 430 ysize 40
                        add Solid("#3ed06f") xsize int(430 * mg_energy) ysize 40
                        add Solid("#ffffff20") xsize int(430 * mg_energy) ysize 16

                    text "RYTHME // FENÊTRE D'EFFORT" style "mg_label_text" font mg_font
                    fixed:
                        xsize 430
                        ysize 34
                        add Solid("#11293f") xsize 430 ysize 34
                        $ zone_width = (mg_zone_end - mg_zone_start)
                        add Solid("#22c065") xpos int(mg_zone_start * 430) xsize int(zone_width * 430) ysize 34 at mg_hud_pulse
                        add Solid("#f4faff") xpos int(mg_value * 430) xsize 8 ysize 34

                    text "TEMPS // CHRONO" style "mg_label_text" font mg_font
                    fixed:
                        xsize 430
                        ysize 28
                        add Solid("#101e2e") xsize 430 ysize 28
                        add Solid("#e74f4f") xsize int((mg_time_left / max(0.01, mg_duration)) * 430) ysize 28

                    text "⬆ ⬇  Clic, ↑ ou ↓ pour pousser." style "mg_subtitle_text" xalign 0.5 font mg_font

            textbutton "POUSSER":
                action Function(mg_click)
                xsize 470
                ysize 94
                text_size 34
                text_font mg_font
                text_color "#e6f7ff"
                background Solid("#0d3b63")
                hover_background Solid("#1e7fce")
                insensitive_background Solid("#203447")

            textbutton "RETOUR":
                action Return()
                xalign 1.0
                text_font mg_font
                text_color "#9eb3c7"
                background Solid("#091522aa")
                hover_background Solid("#16324acc")

    key "K_UP" action Function(mg_click)
    key "K_DOWN" action Function(mg_click)


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

# ------------------------------------------------------------
# TUTORIEL ANIMÉ — démo de la barre de rythme
# ------------------------------------------------------------
transform mg_demo_cursor_sweep:
    xpos 60
    block:
        linear 1.1 xpos 560
        linear 1.1 xpos 60
        repeat

transform mg_demo_hit_flash:
    alpha 0.0
    block:
        pause 0.78
        easeout 0.10 alpha 1.0
        easein 0.30 alpha 0.0
        pause 1.02
        repeat

transform mg_demo_dumbbell_lift:
    ypos 330
    block:
        pause 0.78
        easeout 0.35 ypos 250
        pause 0.4
        easein 0.35 ypos 330
        pause 0.32
        repeat

screen tuto_halteres(as_overlay=False):
    use mk_tuto_chrome("RYTHME D'ENTRAÎNEMENT", [
        ("Observe le curseur", "Le curseur blanc balaye la barre de rythme en continu."),
        ("Frappe dans la zone verte", "Clique (ou ↑/↓) quand le curseur traverse la zone. Au centre exact : PARFAIT."),
        ("Enchaîne les combos", "Chaque réussite consécutive augmente le combo et le score. Un raté coûte de l'énergie."),
    ], "tuto_halteres", as_overlay):

        fixed:
            xfill True
            yfill True

            # Haltère qui se lève à chaque "frappe"
            fixed at mg_demo_dumbbell_lift:
                xpos 230
                xsize 280
                ysize 50
                add Solid("#9fb3c7") size (200, 16) pos (40, 17)
                add Solid("#232f3a") size (44, 50) pos (0, 0)
                add Solid("#232f3a") size (44, 50) pos (236, 0)

            # Barre de rythme
            fixed:
                xpos 60
                ypos 430
                xsize 540
                ysize 36
                add Solid("#11293f") size (540, 36)
                add Solid("#22c065") size (130, 36) xpos 205
                add Solid("#FFFFFF") size (8, 36) at mg_demo_cursor_sweep

            text "PARFAIT !" at mg_demo_hit_flash:
                xpos 330
                ypos 370
                xanchor 0.5
                size 30
                color "#5ad45a"
                bold True
                outlines [(2, "#02040A", 0, 0)]

# ------------------------------------------------------------
# LABEL RÉUTILISABLE
#   call minijeu_halteres_run(mg_id="halteres", title=..., target_reps=..,
#                             duration=.., base_speed=.., with_scene=True)
# ------------------------------------------------------------
label minijeu_halteres_run(mg_id="halteres", title=None, subtitle=None, bg=None, target_reps=10, duration=60.0, base_speed=0.9, with_scene=True):
    $ mg_quick_menu_prev = quick_menu
    $ quick_menu = False
    $ mg_configure(target_reps=target_reps, duration=duration, base_speed=base_speed, title=title, subtitle=subtitle, bg=bg)
    $ mg_reset()
    $ mg_skip_scene_pick = mg_skip_scene_pick or (not with_scene)

    call mk_tutorial("halteres", "tuto_halteres") from _call_mk_tutorial_2
    call mk_countdown from _call_mk_countdown
    call screen minijeu_halteres

    $ mg_was_success = mg_is_successful()

    # Écran de résultats avec rang, défis et record
    $ mg_final_score = min(mg_target_reps * 2, mg_progress + len([1 for c in mg_final_challenges() if c[1]]))
    call mk_show_results(
        mg_title,
        mg_final_score,
        mg_target_reps * 2,
        stats=[
            ("Répétitions", "%d/%d" % (mg_reps, mg_target_reps)),
            ("Parfaits", str(mg_perfects)),
            ("Combo max", "x%d" % mg_combo_max),
            ("Ratés", str(mg_misses)),
        ],
        challenges=mg_final_challenges(),
        mg_id=mg_id,
    ) from _call_mk_show_results_2

    $ quick_menu = mg_quick_menu_prev
    jump minijeu_halteres_after

# Compatibilité : ancien point d'entrée (jour 2 gymnase)
label minijeu_halteres:
    call minijeu_halteres_run(mg_id="halteres") from _call_minijeu_halteres_run
    return

label minijeu_halteres_after:

    # Gain de stat lié à la performance (au lieu d'un pur aléatoire)
    $ _mg_gain_chance = 0.10 + (0.45 if mg_was_success else 0.0) + min(0.20, mg_combo_max * 0.03)
    $ gained_physique = False
    if renpy.random.random() < _mg_gain_chance:
        # La tablette lit le système de statistiques permanent. L'ancienne
        # variable reste synchronisée pour les sauvegardes et scripts existants.
        $ _physique_level, gained_physique = mod_stat("physique", 1)
        $ stat_physique = _physique_level

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
    if nsfw_content_locked():
        return

    "Le contact s'attarde une seconde de trop, et la chaleur monte."
    return

label sport_event_001:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_1
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Il n’y a plus rien autour d'Elias."
    "Juste la barre et le chrono."

    elias "Quarante-huit secondes."

    "Ses bras tremblent."
    "Il ne cligne presque pas des yeux."

    elias "Pouah ! J'ai assez bien géré l'amplitude aujourd'hui..."

    "La barre descend."
    "Il contrôle la descente."
    "Pas d’élan."

    elias "Allez ! Encore une."

    "Il pousse."
    "Mâchoire serrée."

    return

label sport_event_002:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_2
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le bruit de leurs mains résonne dans le gymnase."

    mara "Ha ! J't'avais dit que je tiendrais plus longtemps."

    "Sael ne retire pas sa main tout de suite."
    "Elle observe."
    "Calme."

    sael "Tu parles beaucoup pour quelqu’un qui tremblait à la dernière série."

    mara "Oh ça va."
    mara "Je transpirais, c’est tout."

    "Leurs épaules brillent encore."
    "Respiration haute."
    "Rythme rapide."

    sael "Ta posture était mauvaise."
    sael "Tu compenses avec le bas du dos."

    mara "Tu peux juste dire bravo, tu sais ?"

    "Un sourire discret passe sur le visage de Sael."

    sael "Bravo..."

    mara "Voilà."
    mara "C’était pas si compliqué."

    return

label sport_event_003:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_3
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La barre repose sur ses épaules."
    "Beaucoup trop lourde."

    tomas "Charge vérifiée."
    tomas "Amplitude correcte."

    "Ses jambes tremblent déjà."

    iris "Impressionnant."
    iris "Mais je te jure que si tu te fais mal tu te débrouilleras pour aller à l'infirmerie."

    "Il descend."
    "Lentement."

    nyra "Allez ! Maintenant il faut remonter !"

    tomas "Silence."

    "Il pousse."
    "Les dents serrées."
    "Un souffle brutal."

    "La barre remonte."

    iris "Acceptable."

    nyra "C'est vraiment pas mal !"

    tomas "O-Ouai..."

    return

label sport_event_004:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Elen et Ryn sont là. Ils ne parlent pas."
    "Ils tiennent."

    ryn "Alors t'abandonnes toujours pas ?"

    elen "Même pas en rêve."

    "Leurs bras tremblent."
    "Le sol est froid."
    "Le chrono tourne."

    ryn "T’as déjà les épaules qui lâchent."

    elen "C’est toi qui parle ?"

    "Une goutte tombe."
    "Puis une autre."

    ryn "Tu respires trop vite."

    elen "Et alors ?! J'en ai bien le droit !"

    "Silence."
    "Juste leurs souffles."

    "Ils tiennent encore."
    "Mais je ne vais pas rester là pour voir qui gagnera."

    return

label sport_event_005:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_5
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le gymnase est devenu… autre chose."

    julian "Bienvenue au Tournoi Nexus Extrême !"

    iris "Pourquoi il y a des cônes partout…"

    elen "Et pourquoi il y a une échelle au sol ?"

    julian "Parce que c’est un parcours multi-dimensionnel."

    nyra "Ça ne veut rien dire."

    tomas "Quel est l’objectif précis ?"

    julian "Coordination."
    julian "Endurance."

    iris "On voulait juste courir un peu…"

    "Julian déplie son tableau."
    "Flèches. Cercles. Points d’exclamation."

    tomas "Il y a une phase chantée. E-Euh, je suis pas très à l'aise !"

    julian "Oui ! C'est de la motivation sonore."

    elen "On doit vraiment passer dans le pneu là ?!"

    julian "Absolument."

    iris "Je déteste déjà."

    julian "C’est ça l’esprit du tournoi !"

    return

label sport_event_006:
    if nsfw_content_locked():
        return

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_6
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le gymnase est presque vide maintenant. Juste elle."
    "Elen pose sa gourde. Respire profondément. Puis commence à s’étirer."
    "Bras levés haut, dos cambré, le tissu mouillé colle à sa peau comme une seconde peau."
    "Elle penche le buste sur le côté, une main glisse le long de sa hanche."
    "Le silence amplifie chaque souffle, chaque froissement de tissu."

    elen "…ah, ça tire bien là…"

    "Elle change de côté. La lumière bleue des néons trace des reflets sur ses abdos luisants."
    "Ses doigts effleurent le creux de sa taille, puis descendent un instant sur la sangle de son short."
    "Elle se redresse lentement, roule les épaules, fait craquer sa nuque."
    "Un sourire fatigué, mais satisfait."

    elen "Bon… séance terminée."

    "Elle attrape sa serviette, s’essuie le front, le cou… descend un peu plus bas entre ses seins."
    "Tu ne peux pas détourner les yeux. Elle est… magnétique."
    "La sueur qui perle encore sur son ventre plat. Les muscles qui roulent sous la peau quand elle bouge."
    "Canon. Vraiment canon."
    "Elle te remarque enfin. Un sourcil se lève."

    elen "Quoi ? Tu comptes rester planté là toute la journée ?"

    return

label sport_event_007:
    if nsfw_content_locked():
        return

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_7
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Nyra est encore sur le banc, torse bombé, respiration lourde. La séance l’a vraiment cuite."
    "Elle attrape sa bouteille, la dévisse d’un geste fatigué."

    nyra "Putain… j’ai l’impression d’être un radiateur ambulant."

    "Sans réfléchir, elle penche la tête en arrière et renverse la bouteille au-dessus d’elle."
    "L’eau jaillit en filet large. Elle coule d’abord sur son front, glisse sur ses tempes, puis descend en cascade sur son visage, sa gorge, entre ses seins."
    "Le tissu noir ultra-fin devient instantanément transparent. Chaque goutte trace une ligne brillante sur sa peau rougie par l’effort."
    "Elle ferme les yeux, un petit soupir de soulagement lui échappe."

    nyra "…aaaaah, ça fait du bien…"

    "L’eau continue de ruisseler : sur son ventre contracté, le long des côtes, jusqu’à disparaître dans le creux de son nombril et plus bas."
    "Ses cuisses gainées de noir luisent maintenant. Quelques gouttes perlent sur le banc en dessous d’elle."
    "Elle rouvre les yeux, passe une main dans ses cheveux trempés pour les rejeter en arrière."
    "Un sourire paresseux, presque sensuel, apparaît sur ses lèvres."

    nyra "Bon… au moins je suis réveillée maintenant."

    "Elle pose la bouteille vide à côté d’elle, s’étire légèrement, le tissu collant soulignant chaque courbe."
    "Tu ne bouges pas. Difficile de détourner le regard."

    return
label sport_event_008:
    if nsfw_content_locked():
        return

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_8
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le tapis s’est enfin arrêté. Lysa descend, jambes encore tremblantes de l’effort."
    "Elle pose les mains sur les hanches, inspire profondément, puis lève les bras haut au-dessus de la tête."
    "Dos cambré, poitrine qui se soulève, elle s’étire longuement comme pour évacuer toute la fatigue accumulée."
    "La sueur coule en filets réguliers : du front aux tempes, le long du cou, entre les seins, sur les abdos qui se contractent à chaque respiration."
    "Elle penche la tête d’un côté, puis de l’autre, fait craquer sa nuque avec un petit soupir satisfait."

    lysa "…ouf. Ça faisait longtemps que j’avais pas poussé comme ça."

    "Bras toujours en l’air, elle roule lentement les épaules, fait passer le poids d’une jambe sur l’autre."
    "Le tissu du crop top colle à sa peau, transparent par endroits. Les gouttes glissent sur son ventre, disparaissent sous la ceinture du short."
    "Elle descend les bras, attrape ses coudes derrière le dos et tire pour ouvrir la poitrine."
    "Un sourire fatigué illumine son visage. Elle a l’air épuisée… mais heureuse."

    lysa "Bon, je crois que j’ai mérité une bonne douche."

    "Elle secoue légèrement la tête pour chasser les gouttes de ses cheveux, puis me jette un regard en coin."

    lysa "T’as couru combien de km toi aujourd’hui ? Ou t’as juste regardé ?"

    return

label sport_event_009:
    if nsfw_content_locked():
        return

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9
    scene bg_gymnase at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La séance est finie. J'ai le corps lourd, muscles chauds. Je range les affaires en silence."
    "Direction les douches. Le couloir est désert, juste le bruit lointain de l’eau qui tombe."
    "Je pousse la porte entrouverte. La vapeur flotte déjà dans l’air."
    "Et là, elle est là."

    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_10
    scene bg_gymnase at adaptive_fullscreen with dissolve

    "De loin. Dos tourné. Sous le jet principal. L'eau cascade sur son dos, sur ses hanches, sur ses fesses rondes et luisantes."
    "Les cheveux blancs collés à la peau, les gouttes qui glissent le long de sa colonne et disparaissent dans le creux de ses reins."
    "Elle ne bouge presque pas. Juste les épaules qui se soulèvent doucement au rythme de sa respiration."
    "L’eau ruisselle partout."
    "Je reste immobile. À l’entrée. Sans un bruit. Sans un mot."
    "Mon cœur bat un peu plus fort. La vapeur rend tout ça un peu irréel."
    "Elle passe une main dans ses cheveux, rejette la tête en arrière un instant. Un soupir à peine audible."
    "Puis l’eau ralentit. Le jet devient filet. Puis gouttes. Puis rien."
    "Elle tend la main vers le robinet, coupe le débit."
    "On recule d’un pas. Puis d’un autre. La porte se referme doucement derrière nous sans un claquement."
    "Il ne faut pas qu'on me voit ici."
    "On s’éloigne dans le couloir. Pouls encore rapide. Image gravée."

    return
