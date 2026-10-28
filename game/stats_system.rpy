# =============================================================
# STATISTIQUES SECONDAIRES — progression permanente partagée
# =============================================================

# ---- Données permanentes (partagées entre toutes les saves) ----
default persistent.stats = None   # dict rempli par stats_init()
default persistent.stats_xp = None
default persistent.stats_xp_blocked_until = 0.0
default stat_level_up_queue = []
default stat_level_up_active = False

init python:

    STAT_MIN = 1
    STAT_MAX = 10

    # XP nécessaire pour passer des niveaux 1 à 9. La tablette affiche
    # l'avancement ; le surplus se reporte automatiquement au niveau suivant.
    STAT_XP_THRESHOLDS = (3, 5, 8, 12, 17, 24, 32, 42, 55)
    STAT_XP_LOAD_COOLDOWN = 60.0

    # Ordre d'affichage + méta (label, couleur, initiale icône)
    STATS_ORDER = ["observation", "empathie", "sang_froid", "logique", "audace", "physique"]

    STATS_META = {
        "observation": {"label": "Observation", "color": "#5CD3FF", "glyph": "O"},
        "empathie":    {"label": "Empathie",    "color": "#B57BFF", "glyph": "E"},
        "sang_froid":  {"label": "Sang-froid",  "color": "#E85C6B", "glyph": "S"},
        "logique":     {"label": "Logique",     "color": "#6BD98A", "glyph": "L"},
        "audace":      {"label": "Audace",       "color": "#4FE0C0", "glyph": "A"},
        "physique":    {"label": "Physique",     "color": "#F0A835", "glyph": "P"},
    }

    def stats_init():
        # Crée/complète les données permanentes sans écraser les anciennes saves.
        if not isinstance(persistent.stats, dict):
            persistent.stats = {}
        if not isinstance(persistent.stats_xp, dict):
            persistent.stats_xp = {}
        for k in STATS_ORDER:
            if k not in persistent.stats:
                persistent.stats[k] = STAT_MIN
            persistent.stats[k] = max(STAT_MIN, min(STAT_MAX, int(persistent.stats[k])))
            if k not in persistent.stats_xp:
                persistent.stats_xp[k] = 0
            persistent.stats_xp[k] = max(0, int(persistent.stats_xp[k]))
            if persistent.stats[k] >= STAT_MAX:
                persistent.stats_xp[k] = 0
        if not isinstance(getattr(persistent, "stats_xp_blocked_until", None), (int, float)):
            persistent.stats_xp_blocked_until = 0.0
        return persistent.stats

    def get_stat(name):
        stats_init()
        return persistent.stats.get(name, STAT_MIN)

    def set_stat(name, value):
        stats_init()
        persistent.stats[name] = max(STAT_MIN, min(STAT_MAX, int(value)))
        return persistent.stats[name]

    def mod_stat(name, delta):
        # +1 / -1 etc. Retourne (nouveau_niveau, a_monte_de_niveau)
        old = get_stat(name)
        new = set_stat(name, old + delta)
        leveled = new > old
        if leveled:
            queue_stat_level_up(name, new)
        return new, leveled

    def queue_stat_level_up(name, level):
        """Empile une annonce afin que plusieurs gains restent lisibles."""
        if name not in STATS_META:
            return
        if not isinstance(getattr(store, "stat_level_up_queue", None), list):
            store.stat_level_up_queue = []
        if store.stat_level_up_active and not renpy.get_screen("stat_level_up_animation"):
            store.stat_level_up_active = False
        store.stat_level_up_queue.append((name, int(level)))
        if not store.stat_level_up_active:
            show_next_stat_level_up()

    def show_next_stat_level_up():
        if not store.stat_level_up_queue:
            store.stat_level_up_active = False
            return
        name, level = store.stat_level_up_queue.pop(0)
        store.stat_level_up_active = True
        if renpy.loadable("audio/sfx_victory.mp3"):
            renpy.sound.play("audio/sfx_victory.mp3")
        renpy.show_screen("stat_level_up_animation", stat_name=name, level=level)

    def finish_stat_level_up():
        renpy.hide_screen("stat_level_up_animation")
        store.stat_level_up_active = False
        show_next_stat_level_up()

    def stat_xp_required(name):
        """Seuil interne du niveau courant. None signifie niveau maximum."""
        level = get_stat(name)
        if level >= STAT_MAX:
            return None
        return STAT_XP_THRESHOLDS[level - STAT_MIN]

    def start_stat_xp_load_cooldown(seconds=STAT_XP_LOAD_COOLDOWN):
        """Interdit tout gain d'XP pendant 60 s après le chargement d'une save."""
        import time
        stats_init()
        store.stat_level_up_queue = []
        store.stat_level_up_active = False
        renpy.hide_screen("stat_level_up_animation")
        persistent.stats_xp_blocked_until = time.time() + max(0.0, float(seconds))
        renpy.save_persistent()

    def stat_xp_is_blocked():
        import time
        stats_init()
        return time.time() < persistent.stats_xp_blocked_until

    def award_stat_xp(name, amount):
        """Point d'entrée unique des gains d'XP de statistiques.

        Le surplus est conservé lors des montées de niveau. La tablette affiche l'XP.
        """
        stats_init()
        if name not in STATS_META:
            raise ValueError("Statistique inconnue : {}".format(name))

        amount = max(0, int(amount))
        result = {
            "stat": name,
            "awarded": 0,
            "blocked": False,
            "leveled": False,
            "level": get_stat(name),
        }
        if amount <= 0 or result["level"] >= STAT_MAX:
            return result
        if stat_xp_is_blocked():
            result["blocked"] = True
            return result

        # Préserve le surplus lors des passages de niveaux successifs.
        persistent.stats_xp[name] += amount
        while result["level"] < STAT_MAX:
            required = stat_xp_required(name)
            if required is None or persistent.stats_xp[name] < required:
                break
            persistent.stats_xp[name] -= required
            result["level"] = set_stat(name, result["level"] + 1)
            result["leveled"] = True
            queue_stat_level_up(name, result["level"])
        if result["level"] >= STAT_MAX:
            persistent.stats_xp[name] = 0

        renpy.save_persistent()
        return result

    def award_stats_xp(rewards):
        """Attribue en une fois l'XP d'un choix à une ou plusieurs statistiques."""
        results = []
        for name, amount in rewards.items():
            results.append(award_stat_xp(name, amount))
        return results

    def stat_choice_unlocked(option):
        requirements = option.get("requires", {})
        return all(get_stat(name) >= int(level) for name, level in requirements.items())

    def notify_stat_level_ups(results):
        # Conservé pour les appels historiques : award_stat_xp anime déjà le gain.
        return


$ stats_init()


# ---- Transforms d'animation ----
transform tablet_card_halo:
    alpha 0.0
    linear 1.4 alpha 0.30
    linear 1.4 alpha 0.0
    repeat

transform stat_check_idle:
    linear 1.6 zoom 1.04
    linear 1.6 zoom 1.0
    repeat

# ── Cérémonie de progression : réutilise les icônes et anneaux de la tablette.
# Les étapes s'enchaînent sans clic : entrée, ancien niveau, transition, victoire.
transform stat_level_overlay_in:
    alpha 0.0
    ease 0.30 alpha 1.0

transform stat_level_backdrop_breathe:
    alpha 0.18
    linear 1.4 alpha 0.38
    linear 1.4 alpha 0.18
    repeat

transform stat_level_panel_enter:
    alpha 0.0
    zoom 0.88
    yoffset 40
    easeout 0.52 alpha 1.0 zoom 1.0 yoffset 0

transform stat_level_ring_enter:
    alpha 0.0
    zoom 0.65
    rotate -18
    parallel:
        easeout 0.55 alpha 1.0 zoom 1.0
    parallel:
        easeout 0.65 rotate 0

transform stat_level_ring_breathe:
    zoom 0.97
    linear 0.85 zoom 1.035
    linear 0.85 zoom 0.97
    repeat

transform stat_level_ring_spin:
    rotate 0
    linear 6.0 rotate 360
    repeat

transform stat_level_old_phase:
    alpha 0.0
    pause 0.38
    ease 0.18 alpha 1.0
    pause 0.78
    ease 0.24 alpha 0.0

transform stat_level_new_phase:
    alpha 0.0
    zoom 1.36
    pause 1.56
    easeout 0.30 alpha 1.0 zoom 1.0

transform stat_level_flash:
    alpha 0.0
    pause 1.39
    linear 0.10 alpha 0.82
    linear 0.42 alpha 0.0

transform stat_level_burst:
    alpha 0.0
    zoom 0.4
    pause 1.34
    easeout 0.72 alpha 0.0 zoom 1.85

transform stat_level_line_sweep:
    alpha 0.0
    xoffset -380
    pause 1.40
    linear 0.10 alpha 1.0
    easeout 0.50 xoffset 380 alpha 0.0

transform stat_level_footer_in:
    alpha 0.0
    yoffset 16
    pause 1.83
    easeout 0.36 alpha 1.0 yoffset 0

transform stat_level_exit:
    alpha 1.0
    pause 3.9
    easein 0.40 alpha 0.0

# Valeur visuelle du niveau PRÉCÉDENT : indispensable lorsque deux montées
# de niveau sont enchaînées dans une même attribution d'XP.
screen stat_level_up_animation(stat_name, level):
    zorder 260
    modal True
    $ meta = STATS_META[stat_name]
    $ col = meta["color"]
    $ old_level = max(STAT_MIN, level - 1)
    $ new_level = min(STAT_MAX, level)
    $ icon = "hud/tablet/stat_icon_" + stat_name + ".png"
    $ new_ring = "hud/tablet/ring_" + stat_name + "_" + str(new_level) + ".png"

    # Le screen passe au-dessus du dialogue, sans changer le menu tablette.
    # Chaque affichage se ferme automatiquement ; la file gère les gains simultanés.
    fixed at stat_level_exit:
        xysize (1920, 1080)
        add Solid("#01060BD6") at stat_level_overlay_in
        add Solid(col + "15") at stat_level_backdrop_breathe

        # Habillage Conclave OS, mêmes teintes et typographies que la tablette.
        frame at stat_level_panel_enter:
            xalign 0.5 yalign 0.5
            xsize 900 ysize 594
            background Solid("#071522F7")
            padding (0, 0)

            fixed:
                xysize (900, 594)
                add Solid("#102B3BC0") xsize 900 ysize 62
                add Solid(col) xsize 900 ysize 3
                add Solid(col + "77") xpos 0 ypos 60 xsize 900 ysize 1
                add Solid(col + "44") xpos 20 ypos 78 xsize 860 ysize 1
                add Solid(col + "44") xpos 20 ypos 515 xsize 860 ysize 1
                add Solid("#193B50") xpos 0 ypos 591 xsize 900 ysize 3

                text "CONCLAVE OS   //   ÉVOLUTION DES APTITUDES":
                    xpos 30 ypos 22 size 19 color "#DCECF6"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 1.6
                text "KAMI.CORE  /  01":
                    xpos 725 ypos 26 size 13 color col
                    font "fonts/Barlow-Light.ttf"

                # Grand anneau et icône : fichiers EXACTS du menu statistiques.
                fixed:
                    xpos 40 ypos 104
                    xysize (375, 355)
                    add Solid(col + "0E") xalign 0.5 yalign 0.5 xsize 350 ysize 350
                    add new_ring at stat_level_ring_enter:
                        xalign 0.5 yalign 0.5
                    add new_ring at stat_level_ring_breathe:
                        xalign 0.5 yalign 0.5
                        alpha 0.20
                    add icon at stat_level_ring_enter:
                        xalign 0.5 yalign 0.5
                    add Solid(col + "15") at stat_level_flash:
                        xalign 0.5 yalign 0.5 xsize 310 ysize 310
                    add Solid(col + "88") at stat_level_burst:
                        xalign 0.5 yalign 0.5 xsize 145 ysize 145

                text "APTITUDE AMÉLIORÉE":
                    xpos 425 ypos 153 size 19 color "#91AEBE"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2.2

                text meta["label"].upper():
                    xpos 424 ypos 202 size 42 color "#F2FAFF"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 1.2

                fixed at stat_level_old_phase:
                    xpos 422 ypos 290
                    xysize (455, 110)
                    text "NIVEAU [old_level]":
                        xpos 0 ypos 0 size 39 color "#A1BAC9"
                        font "fonts/Rajdhani-SemiBold.ttf"
                    add Solid("#244154") xpos 0 ypos 68 xsize 392 ysize 9
                    add Solid(col) xpos 0 ypos 68 xsize 392 ysize 9

                fixed at stat_level_new_phase:
                    xpos 422 ypos 280
                    xysize (450, 120)
                    text "NIVEAU [new_level]":
                        xpos 0 ypos 0 size 49 color col
                        font "fonts/Rajdhani-SemiBold.ttf" outlines [(1, "#01060B", 0, 0)]
                    add Solid("#244154") xpos 0 ypos 76 xsize 392 ysize 9
                    add Solid(col) xpos 0 ypos 76 xsize 392 ysize 9
                    text "NOUVEAU PALIER ATTEINT":
                        xpos 2 ypos 93 size 17 color "#D1E8F2"
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1.3

                add Solid("#FFFFFFAA") xpos 422 ypos 407 xsize 5 ysize 45 at stat_level_line_sweep

                fixed at stat_level_footer_in:
                    xpos 34 ypos 531
                    xysize (825, 45)
                    text "PROGRESSION PERMANENTE ENREGISTRÉE":
                        xpos 0 ypos 5 size 16 color "#A4C0CD"
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1.6
                    text ("NIVEAU MAXIMUM" if new_level >= STAT_MAX else "+1 NIVEAU"):
                        xalign 1.0 ypos 5 size 18 color col
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1.3

    timer 4.32 action Function(finish_stat_level_up)

# =============================================================
# ÉCRAN D'ACCUEIL TABLETTE — "CONCLAVE OS" (cf maquette)
# =============================================================
# Ancien écran conservé pour référence ; le HUD ouvre maintenant tablet_home
# card_actions permet de rebrancher les boutons selon le contexte.

screen tablet_home_legacy(clock="08:00", show_vote=True):
    modal True
    zorder 100

    add Solid("#020609F2")

    # Grille déco
    for gx in [0.25, 0.50, 0.75]:
        add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1920 ysize 1 at Transform(ypos=gx)
    for gy in [0.33, 0.67]:
        add Solid("#5CD3FF08") xpos 0 ypos 0 xsize 1 ysize 1080 at Transform(xpos=gy)

    frame at d1_appear:
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 720
        background Frame(Solid("#0A121CF8"), 0, 0)
        padding (0, 0)

        fixed:
            xsize 1180
            ysize 720

            add Solid("#5CD3FF") xpos 0 ypos 0 xsize 1180 ysize 2

            # ---- Barre de statut ----
            add Solid("#0A111C") xpos 0 ypos 0 xsize 1180 ysize 56
            text "▮ ▮▮  ⌁":
                xpos 26 ypos 18 size 16 color "#5CD3FF" font "fonts/Rajdhani-SemiBold.ttf"
            text "[clock]":
                xpos 1070 ypos 15 size 20 color "#5CD3FF" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            add Solid("#1A2D3E") xpos 0 ypos 56 xsize 1180 ysize 1

            # ---- Cartes ----
            hbox:
                xalign 0.5
                ypos 130
                spacing 40

                if show_vote and j2_vote_codex_unlocked:
                    $ vote_progress = dossier_chapter_progress(dossier_default_chapter())
                    use tablet_card("DOSSIER DE VOTE", "#B57BFF", "hud/tablet/card_vote", [Hide("tablet_home"), Show("vote_dossier")], vote_progress)
                use tablet_card("STATISTIQUES", "#5CD3FF", "hud/tablet/card_stats", [Hide("tablet_home"), Show("tablet_stats")])
                use tablet_card("CODEX", "#6BD98A", "hud/tablet/card_codex", [Hide("tablet_home"), ShowMenu("codex_menu")])

            if investigation_story_available():
                textbutton "⌁  DOSSIER D'ENQUÊTE":
                    xpos 885 ypos 610 xsize 250 ysize 40
                    text_size 15 text_color "#5CD3FF"
                    background Solid("#5CD3FF12")
                    hover_background Solid("#5CD3FF2A")
                    action [Function(investigation_sync_legacy_save), Hide("tablet_home"), Show("investigation_dossier", from_tablet=True)]

            # ---- Barre basse + bouton home (ferme la tablette) ----
            text "CONCLAVE OS v2.1":
                xpos 26 ypos 678 size 12 color "#3A566A" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            button:
                xalign 0.5 ypos 660
                xsize 90 ysize 44
                background Frame(Solid("#12202E"), 0, 0)
                hover_background Frame(Solid("#5CD3FF22"), 0, 0)
                action Hide("tablet_home")
                text "⌂" xalign 0.5 yalign 0.5 size 24 color "#5CD3FF"


screen tablet_card(title, color, icon, action, progress=None):
    $ progress_percent = progress["percent"] if progress is not None else 0
    $ progress_arguments_done = progress["arguments_done"] if progress is not None else 0
    $ progress_arguments_total = progress["arguments_total"] if progress is not None else 0
    $ progress_successes_done = progress["successes_done"] if progress is not None else 0
    $ progress_successes_total = progress["successes_total"] if progress is not None else 0

    frame:
        xsize 320
        ysize 460
        background Frame(Solid("#0C1622"), 0, 0)
        padding (0, 0)

        button:
            xsize 320
            ysize 460
            background Frame(Solid("#00000000"), 0, 0)
            hover_background Frame(Solid(color + "18"), 0, 0)
            action action

            fixed:
                xsize 320
                ysize 460
                add Solid(color) xpos 0 ypos 0 xsize 320 ysize 2
                add Solid(color + "55") xpos 0 ypos 0 xsize 2 ysize 460
                add Solid(color + "55") xpos 318 ypos 0 xsize 2 ysize 460

                # Icône circulaire (halo + anneau ticks + texture)
                fixed:
                    xalign 0.5 ypos 64
                    xysize (200, 200)
                    add Transform("hud/tablet/glow_soft.png", matrixcolor=TintMatrix(color)) xalign 0.5 yalign 0.5 at tablet_card_halo
                    add Transform("hud/tablet/disc_ring.png", size=(184, 184), matrixcolor=TintMatrix(color)) xalign 0.5 yalign 0.5
                    add Transform(icon + ".png", size=(94, 94)) xalign 0.5 yalign 0.5
                    if progress is not None:
                        add Solid("#07111DDD") xalign 0.5 yalign 0.5 xysize (116, 58)
                        text "[progress_percent]%":
                            xalign 0.5 yalign 0.5 size 27 color "#FFFFFF"
                            font "fonts/Rajdhani-SemiBold.ttf"

                if progress is not None:
                    text "ARGUMENTS  [progress_arguments_done] / [progress_arguments_total]":
                        xalign 0.5 ypos 278 size 14 color color
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1
                    text "SUCCÈS  [progress_successes_done] / [progress_successes_total]":
                        xalign 0.5 ypos 304 size 14 color color
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1

                add Solid(color + "33") xpos 40 ypos 340 xsize 240 ysize 1
                text title:
                    xalign 0.5 ypos 372
                    size 22 color color
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                text "◇":
                    xalign 0.5 ypos 412 size 16 color color


# =============================================================
# ÉCRAN STATISTIQUES — jauges 10 segments (cf HUD perso)
# =============================================================

screen tablet_stats():
    # Reprend l'interface tablette inclinée du menu Profil / Dossier.
    modal True
    zorder 220

    $ back_to_tablet = [Hide("tablet_stats"), Show("tablet_home"), With(Dissolve(0.25))]
    key "K_ESCAPE" action back_to_tablet
    key "K_t" action back_to_tablet

    add Solid("#01060bcc")
    add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080)

    fixed at messenger_panel_in, tablet_profile_plane:
        xysize (940, 560)
        clipping True

        add Solid("#020912f5")
        add Solid("#0b223144", ysize=56)
        add Solid("#5cd3ff99", ysize=2) ypos 55

        text "KAMI.CORE // STATISTIQUES":
            font "fonts/Barlow-Light.ttf"
            size 14 color "#5cd3ff" kerning 2.2
            xpos 18 ypos 18

        text "COMPÉTENCES PERMANENTES":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 13 color "#769aab" kerning 1.3
            xpos 590 ypos 20

        textbutton "RETOUR":
            xpos 824 ypos 9 xsize 100 ysize 36
            padding (8, 4)
            background Fixed(Solid("#07131de8"), Solid("#5cd3ff", ysize=2, yalign=1.0))
            hover_background Fixed(Solid("#123249f5"), Solid("#86e2ff", ysize=3, yalign=1.0))
            text_font "fonts/Rajdhani-SemiBold.ttf"
            text_size 14 text_color "#9bc7d8" text_hover_color "#ffffff"
            text_xalign 0.5 text_yalign 0.5
            action back_to_tablet

        text "APTITUDES // NOAM":
            xpos 22 ypos 68 size 19 color "#eaf4ff"
            font "fonts/Rajdhani-SemiBold.ttf" kerning 2
        text "Niveaux actuels de vos six compétences.":
            xpos 23 ypos 94 size 13 color "#829fad"
            font "fonts/Barlow-Light.ttf"
        add Solid("#294c5e") xpos 21 ypos 119 xsize 896 ysize 1

        # Réutilise directement les anneaux et icônes du menu d'origine.
        grid 3 2:
            xpos 21 ypos 132
            xspacing 13 yspacing 12
            for stat_name in STATS_ORDER:
                use tablet_stat_gauge(stat_name)

        add Solid("#294c5e") xpos 21 ypos 511 xsize 896 ysize 1
        text "CONCLAVE OS  //  STATISTIQUES ACTUALISÉES EN TEMPS RÉEL":
            xpos 24 ypos 524 size 12 color "#698b9e"
            font "fonts/Rajdhani-SemiBold.ttf" kerning 1.2


    # Pouce au premier plan, au-dessus de toute l’interface de l’application.
    add "images/ui/tablette/tablette_pouce.png" fit "contain" xysize (1920, 1080)

screen tablet_stat_gauge(name):
    $ meta = STATS_META[name]
    $ lvl = get_stat(name)
    $ col = meta["color"]
    $ xp_needed = stat_xp_required(name)
    $ xp_current = persistent.stats_xp.get(name, 0) if xp_needed is not None else 0
    $ xp_fraction = min(1.0, max(0.0, float(xp_current) / xp_needed)) if xp_needed else 1.0

    frame:
        xsize 290 ysize 178
        padding (0, 0)
        background Fixed(
            Solid("#0a1b28ee"),
            Solid(col + "88", ysize=2),
            Solid("#254052", ysize=1, yalign=1.0),
        )
        fixed:
            xysize (290, 178)
            # Anneau et icône originaux, réduits pour tenir dans la vitre.
            add Transform("hud/tablet/ring_" + name + "_" + str(lvl) + ".png",
                          size=(162, 162)) xpos 6 ypos 6
            add Transform("hud/tablet/stat_icon_" + name + ".png",
                          size=(49, 49)) xpos 63 ypos 52
            text str(lvl):
                xpos 87 ypos 112 xanchor 0.5
                size 35 color col
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(1, "#00000088", 0, 0)]
            text meta["label"]:
                xpos 174 ypos 47 xanchor 0.0
                xmaximum 107 size 17 color "#e4f2f9"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "NIVEAU":
                xpos 174 ypos 86 size 12 color "#819baa"
                font "fonts/Barlow-Light.ttf"
            text "{:02d} / 10".format(lvl):
                xpos 174 ypos 103 size 18 color col
                font "fonts/Rajdhani-SemiBold.ttf"
            # Progression intégrée dans la tuile existante (290 x 178).
            add Solid("#243c4b") xpos 174 ypos 137 xsize 102 ysize 5
            if xp_needed is not None and xp_fraction > 0:
                add Solid(col) xpos 174 ypos 137 xsize max(1, int(102 * xp_fraction)) ysize 5
            text ("XP {:d}/{:d}".format(xp_current, xp_needed) if xp_needed is not None else "MAÎTRISE MAX"):
                xpos 174 ypos 147 size 12 color "#a9c8d5"
                font "fonts/Rajdhani-SemiBold.ttf"


screen stat_gauge(name):
    $ meta = STATS_META[name]
    $ lvl = get_stat(name)
    $ col = meta["color"]

    fixed:
        xysize (340, 300)

        # Anneau segmenté (niveau)
        add ("hud/tablet/ring_" + name + "_" + str(lvl) + ".png") xalign 0.5 ypos 0

        # Icône centrée
        add Transform("hud/tablet/stat_icon_" + name + ".png", size=(96, 96)) xalign 0.5 ypos 82

        # Niveau chiffré (dans l'anneau, bas)
        text "[lvl]":
            xalign 0.5 ypos 196 size 52 color col
            font "fonts/Rajdhani-SemiBold.ttf" kerning 1 outlines [(1, "#00000088", 0, 0)]

        # Libellé
        text meta["label"]:
            xalign 0.5 ypos 262 size 22 color "#D6E8F0"
            font "fonts/Rajdhani-SemiBold.ttf" kerning 1
