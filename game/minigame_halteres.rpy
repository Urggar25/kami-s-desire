default persistent.pegi18 = False
default stat_physique = 0

# --- Config réutilisable (modifiée par minijeu_halteres_run) ---
default mg_title = "ENTRAÎNEMENT AUX HALTÈRES"
default mg_subtitle = "Marque un maximum de points en 60 secondes. Parfait : +2, bien : +1."
default mg_bg = "bg_gymnase"
default mg_duration = 60.0
default mg_base_speed = 0.9
# Repère de performance pour les récompenses ; ne limite plus les coups.
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
        store.mg_duration = 60.0  # Défi d'une minute, quelle que soit la config précédente.
        store.mg_base_speed = float(base_speed)
        if title: store.mg_title = title
        store.mg_subtitle = "Marque un maximum de points en 60 secondes. Parfait : +2, bien : +1."
        # Décor déclaré dans images.rpy ; on évite l'ancien gym_bg.png absent.
        store.mg_bg = bg if bg and renpy.has_image(bg) else "bg_gymnase"

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

        if store.mg_time_left <= 0 or store.mg_energy <= 0:
            store.mg_done = True

    def mg_relocate_zone():
        # La difficulté progresse avec le temps et reste bornée même si
        # le joueur réussit un grand nombre de coups.
        difficulty = 1.0 - max(0.0, min(1.0, store.mg_time_left / 60.0))
        width = max(0.11, 0.22 - difficulty * 0.09)
        center = renpy.random.uniform(0.22 + width, 0.78 - width)
        store.mg_zone_start = center - width / 2.0
        store.mg_zone_end = center + width / 2.0
        # Vitesse croissante
        store.mg_speed = store.mg_base_speed + difficulty * 0.45

    def mg_click():
        if store.mg_done:
            return

        store.mg_reps += 1
        val = store.mg_value
        if store.mg_zone_start <= val <= store.mg_zone_end:
            center = (store.mg_zone_start + store.mg_zone_end) / 2.0
            store.mg_combo += 1
            store.mg_combo_max = max(store.mg_combo_max, store.mg_combo)
            # Le combo est un défi annexe, sans bonus de score.
            if abs(val - center) <= store.mg_perfect_margin:
                store.mg_perfects += 1
                store.mg_progress += 2
                store.mg_feedback = kd_tr("PARFAIT ! +2")
                store.mg_feedback_color = "#5ad45a"
                store.mg_flash = 0.18
                renpy.play("audio/sfx_clap.mp3", channel="sound")
            else:
                store.mg_progress += 1
                store.mg_feedback = kd_tr("BIEN ! +1")
                store.mg_feedback_color = "#f2c94c"
                store.mg_flash = 0.14
                renpy.play("audio/sfx_beep.mp3", channel="sound")
        else:
            store.mg_misses += 1
            store.mg_combo = 0
            store.mg_energy = max(0.0, store.mg_energy - 0.15)
            store.mg_feedback = kd_tr("RATÉ ! ÉNERGIE -15 %")
            store.mg_feedback_color = "#ff6b6b"
            store.mg_flash = 0.14
            renpy.play("audio/sfx_drop.mp3", channel="sound")

        if store.mg_energy <= 0:
            store.mg_done = True
        else:
            mg_relocate_zone()

    def mg_clock_text():
        seconds = max(0, int(store.mg_time_left + 0.999))
        return "{:02d}:{:02d}".format(seconds // 60, seconds % 60)

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

# L'interface distingue désormais le portrait (ambiance) de la barre de
# timing (action). Sans asset de Noam en position de développé couché, on
# n'affiche plus une haltère flottant derrière un sprite immobile.
screen minijeu_halteres():
    modal True
    zorder 200

    timer 0.02 repeat True action Function(mg_tick, 0.02)
    key "mouseup_1" action Function(mg_click)
    key "K_UP" action Function(mg_click)
    key "K_DOWN" action Function(mg_click)
    key "K_SPACE" action Function(mg_click)

    if mg_done:
        timer 0.05 action Return()

    default mg_font = mg_get_ui_font()
    $ beat = max(0.0, min(1.0, mg_value))
    $ energy = max(0.0, min(1.0, mg_energy))
    $ zone_start = max(0.0, min(1.0, mg_zone_start))
    $ zone_end = max(zone_start, min(1.0, mg_zone_end))
    $ beat_width = 638
    $ clock = mg_clock_text()

    # Fond du vrai gymnase : plus de référence à gym_bg.png introuvable.
    add mg_bg at adaptive_fullscreen
    add Solid("#020914E8")
    add Solid("#1D3C5425") at mg_bg_idle

    # En-tête compact : l'action conserve l'essentiel de la hauteur disponible.
    frame at mg_panel_fade(0.0):
        xpos 220 ypos 75
        xsize 1480 ysize 110
        padding (28, 15)
        background Solid("#081826F4")
        vbox:
            spacing 5
            text "ENTRAÎNEMENT AUX HALTÈRES":
                size 30 color "#ECF9FF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2
            text "Appuie quand le curseur atteint la zone verte.":
                size 23 color "#9CC6D8"
                font "fonts/Rajdhani-SemiBold.ttf"

    use mk_help_button("tuto_halteres")

    # Colonne de gauche : portrait et progression, sans haltère qui flotte
    # derrière Noam et sans découpe au milieu de son corps.
    frame at mg_panel_fade(0.06):
        xpos 220 ypos 210
        xsize 685 ysize 620
        padding (14, 14)
        background Solid("#071825EA")
        fixed:
            xysize (657, 592)
            add Solid("#102A3D") xsize 657 ysize 592
            add Solid("#17465C55") xsize 657 ysize 592 at mg_bg_idle
            add Solid("#71D4EF") xsize 657 ysize 3
            add Solid("#71D4EF") xsize 3 ysize 592
            text "NOAM  //  EFFORT":
                xpos 26 ypos 22
                size 23 color "#90DCEF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            fixed:
                xpos 18 ypos 65
                xysize (620, 430)
                clipping True
                if renpy.has_image("noam neutre"):
                    add "noam neutre":
                        xpos 58
                        yalign 0.0
                        zoom 0.65
                else:
                    text "NOAM" xalign 0.5 yalign 0.5 size 48 color "#D4ECF7"

            # La progression est indépendante du portrait : aucun élément
            # physique imaginaire ne traverse l'anatomie du sprite.
            add Solid("#061622") xpos 16 ypos 510 xsize 625 ysize 66
            text "POINTS GAGNÉS":
                xpos 28 ypos 518
                size 20 color "#A5CCDD"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "[mg_progress]":
                xpos 28 ypos 539
                size 36 color "#64E8AF"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "PARFAIT : +2   /   BIEN : +1":
                xpos 180 ypos 548
                size 19 color "#9CC7D7"
                font "fonts/Rajdhani-SemiBold.ttf"

    # Colonne de droite : le timing devient l'élément dominant.
    frame at mg_panel_fade(0.12):
        xpos 930 ypos 210
        xsize 770 ysize 620
        padding (22, 20)
        background Solid("#071725F4")
        fixed:
            xysize (726, 578)

            text "SCORE  //  60 SECONDES":
                xpos 12 ypos 4
                size 23 color "#8DBCCF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2
            text "[mg_progress] POINTS":
                xpos 12 ypos 33
                size 54 color "#F2FAFF"
                font "fonts/Rajdhani-SemiBold.ttf"

            if mg_combo >= 2:
                text "COMBO x[mg_combo]" at mg_hud_pulse:
                    xpos 320 ypos 59
                    size 30 color "#68E3AC"
                    font "fonts/Rajdhani-SemiBold.ttf"
            if mg_feedback:
                text kd_tr(mg_feedback) at mg_feedback_pop:
                    xpos 320 ypos 8
                    xsize 395
                    text_align 1.0
                    size 30
                    color mg_feedback_color
                    font "fonts/Rajdhani-SemiBold.ttf"

            add Solid("#31586B") xpos 12 ypos 126 xsize 696 ysize 2
            text "TIMING  //  ZONE D'EFFORT":
                xpos 14 ypos 151
                size 27 color "#BDEBFA"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1

            # Grande jauge : curseur blanc, fenêtre verte, centre parfait.
            add Solid("#061521") xpos 13 ypos 204 xsize 700 ysize 92
            add Solid("#16394E") xpos 30 ypos 219 xsize 666 ysize 62
            add Solid("#2FBB75") xpos (30 + int(zone_start * beat_width)) ypos 219 xsize max(1, int((zone_end - zone_start) * beat_width)) ysize 62
            add Solid("#A3F5C6") xpos (30 + int((zone_start + zone_end) * beat_width / 2) - 5) ypos 219 xsize 10 ysize 62
            add Solid("#F5FBFF") xpos (30 + int(beat * beat_width)) ypos 204 xsize 7 ysize 92
            if mg_flash > 0.0:
                add Solid(mg_feedback_color + "44") xpos 13 ypos 204 xsize 700 ysize 92

            text "ESPACE / CLIC / ↑ / ↓  —  POUSSER":
                xpos 12 ypos 311
                xsize 700
                text_align 0.5
                size 24 color "#B1D3E1"
                font "fonts/Rajdhani-SemiBold.ttf"

            # Une petite jauge d'énergie et un chrono numérique suffisent.
            text "ÉNERGIE":
                xpos 15 ypos 379
                size 23 color "#A6CADA"
                font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#183244") xpos 16 ypos 420 xsize 455 ysize 24
            add Solid("#49D889") xpos 16 ypos 420 xsize int(455 * energy) ysize 24

            text "TEMPS":
                xpos 538 ypos 379
                size 23 color "#A6CADA"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "[clock]":
                xpos 538 ypos 411
                size 36 color ("#ECF7FF" if mg_time_left > 10 else "#FF7878")
                font "fonts/Rajdhani-SemiBold.ttf"

            # Bouton de secours pour le tactile ; la zone de timing reste le
            # centre de l'attention. Le clic est aussi accepté partout.
            # Un seul déclenchement sur relâchement : l'écoute globale
            # mouseup_1 gère déjà le clic. Ce bouton sert de repère tactile.
            textbutton "POUSSER":
                xpos 12 ypos 479
                xsize 696 ysize 65
                text_font "fonts/Rajdhani-SemiBold.ttf"
                text_size 31
                text_color "#EDFAFF"
                background Solid("#0D466B")
                hover_background Solid("#16638D")
                action NullAction()

    # Défis en bas, intégrés au HUD plutôt que superposés au décor.
    frame at mg_panel_fade(0.18):
        xpos 220 ypos 854
        xsize 1480 ysize 92
        padding (22, 13)
        background Solid("#081725EA")
        hbox:
            spacing 30
            text "DÉFIS BONUS":
                size 22 color "#86BCD1"
                font "fonts/Rajdhani-SemiBold.ttf"
            for challenge in mg_live_challenges():
                $ label = challenge[0]
                $ complete = challenge[1]
                $ failed = len(challenge) > 2 and challenge[2]
                $ challenge_label = ("OK  " if complete else "NON  " if failed else "—  ") + label
                text challenge_label:
                    size 22
                    color ("#63DDA5" if complete else "#F28484" if failed else "#ADC2CD")
                    font "fonts/Rajdhani-SemiBold.ttf"

    textbutton "RETOUR":
        xpos 1570 ypos 970
        xsize 130 ysize 45
        text_color "#B8CCD7"
        text_font "fonts/Rajdhani-SemiBold.ttf"
        text_size 24
        background Solid("#07152299")
        hover_background Solid("#17405C")
        action Return()


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
        ("Marque des points", "Parfait : +2 points. Bien : +1 point. Les combos comptent pour les défis bonus."),
        ("Tiens une minute", "Chaque raté retire 15 % d'énergie. À zéro, la partie s'arrête."),
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

    # Score brut non plafonné. Le seuil de référence ne sert qu'au rang.
    $ mg_final_score = mg_progress
    $ mg_score_reference = max(40, mg_final_score)
    call mk_show_results(
        mg_title,
        mg_final_score,
        mg_score_reference,
        stats=[
            ("Points", str(mg_progress)),
            ("Tentatives", str(mg_reps)),
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

    # Gain d'XP lié à la performance (la progression reste invisible).
    $ _mg_gain_chance = 0.10 + (0.45 if mg_was_success else 0.0) + min(0.20, mg_combo_max * 0.03)
    $ gained_physique = False
    if renpy.random.random() < _mg_gain_chance:
        $ _physique_xp_result = award_stat_xp("physique", 1)
        $ gained_physique = _physique_xp_result["leveled"]
        $ stat_physique = get_stat("physique")

    if gained_physique:
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
