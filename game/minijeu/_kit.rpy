# ============================================================
# _kit.rpy — Kit minijeu partagé (v2)
#
# Fournit :
#   1. Compte à rebours READY/GO            : call mk_countdown
#   2. Tutoriels animés (1ère fois + revoir): call mk_tutorial("mg_id", "screen_tuto")
#      + bouton d'aide en jeu               : use mk_help_button("screen_tuto")
#   3. Défis optionnels (HUD + résultats)   : use mk_challenge_hud(challenges)
#   4. Résultats avec rang S/A/B/C/D, malus de retry, records persistants :
#      call mk_show_results("TITRE", score, max_score, stats=[...],
#                           challenges=[("Défi", True), ...],
#                           mg_id="trace_qte", retries=0)
#
# Rang auto : S >= 95%, A >= 80%, B >= 60%, C >= 40%, D sinon.
# Chaque retry abaisse le rang max atteignable d'un cran (S→A→B...).
# ============================================================

default persistent.mk_tuto_seen = {}
default persistent.mk_best_ranks = {}
default mk_retry_counts = {}

init -10 python:
    MK_RANK_ORDER = ["S", "A", "B", "C", "D"]

    MK_RANK_COLORS = {
        "S": "#FFD700",
        "A": "#5DFF9A",
        "B": "#7DF9FF",
        "C": "#FFD166",
        "D": "#FF4D6D",
    }

    MK_RANK_LABELS = {
        "S": "PARFAIT",
        "A": "EXCELLENT",
        "B": "SOLIDE",
        "C": "PASSABLE",
        "D": "INSUFFISANT",
    }

    def mk_compute_rank(score, max_score, retries=0):
        ratio = (float(score) / float(max_score)) if max_score else 0.0
        if ratio >= 0.95: base = 0
        elif ratio >= 0.80: base = 1
        elif ratio >= 0.60: base = 2
        elif ratio >= 0.40: base = 3
        else: base = 4
        capped = min(len(MK_RANK_ORDER) - 1, base + max(0, int(retries)))
        return MK_RANK_ORDER[capped]

    def mk_rank_index(rank):
        return MK_RANK_ORDER.index(rank) if rank in MK_RANK_ORDER else len(MK_RANK_ORDER) - 1

    def mk_register_best(mg_id, rank):
        """Retourne True si nouveau record."""
        if not mg_id:
            return False
        prev = persistent.mk_best_ranks.get(mg_id)
        if prev is None or mk_rank_index(rank) < mk_rank_index(prev):
            persistent.mk_best_ranks[mg_id] = rank
            return True
        return False

    def mk_add_retry(mg_id):
        store.mk_retry_counts[mg_id] = store.mk_retry_counts.get(mg_id, 0) + 1

    def mk_get_retries(mg_id):
        return store.mk_retry_counts.get(mg_id, 0)

    def mk_reset_retries(mg_id):
        store.mk_retry_counts[mg_id] = 0

    def mk_tuto_is_seen(mg_id):
        return bool(persistent.mk_tuto_seen.get(mg_id))

    def mk_tuto_mark_seen(mg_id):
        persistent.mk_tuto_seen[mg_id] = True

    def mk_challenge_count_done(challenges):
        return len([1 for _c in challenges if _c[1]])


# ------------------------------------------------------------
# Compte à rebours 3-2-1-GO
# ------------------------------------------------------------
transform mk_count_pop:
    alpha 0.0
    zoom 2.4
    easein 0.18 alpha 1.0 zoom 1.0
    pause 0.55
    easeout 0.15 alpha 0.0 zoom 0.8

transform mk_go_slam:
    alpha 0.0
    zoom 0.4
    easein 0.12 alpha 1.0 zoom 1.25
    easeout 0.10 zoom 1.0
    pause 0.45
    linear 0.12 alpha 0.0

transform mk_scanline_drift:
    yoffset -1080
    linear 7.0 yoffset 1080
    repeat

transform mk_edge_alert:
    alpha 0.35
    ease 0.7 alpha 0.85
    ease 0.7 alpha 0.35
    repeat

style mk_terminal_label:
    font "fonts/Barlow-Light.ttf"
    size 18
    color "#7DF9FF"
    kerning 4.0

style mk_panel_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#DCF0FF"
    outlines [(2, "#02040A", 0, 1)]

screen mk_countdown_screen():
    modal True
    zorder 400

    add Solid("#02040Acc")
    add Solid("#7DF9FF22", ysize=2) ypos 188
    add Solid("#7DF9FF22", ysize=2) ypos 760
    add Solid("#FFFFFF08", xsize=1920, ysize=24) at mk_scanline_drift
    text "KAMI.CORE // EXECUTION PROTOCOL":
        style "mk_terminal_label"
        xpos 76
        ypos 78

    default mk_step = 0

    if mk_step == 0:
        text "3" at mk_count_pop:
            align (0.5, 0.45) size 220 color "#7DF9FF" bold True
            outlines [(6, "#02040A", 0, 0)]
        timer 0.9 action SetScreenVariable("mk_step", 1)
    elif mk_step == 1:
        text "2" at mk_count_pop:
            align (0.5, 0.45) size 220 color "#7DF9FF" bold True
            outlines [(6, "#02040A", 0, 0)]
        timer 0.9 action SetScreenVariable("mk_step", 2)
    elif mk_step == 2:
        text "1" at mk_count_pop:
            align (0.5, 0.45) size 220 color "#FFD166" bold True
            outlines [(6, "#02040A", 0, 0)]
        timer 0.9 action SetScreenVariable("mk_step", 3)
    else:
        text "GO" at mk_go_slam:
            align (0.5, 0.45) size 260 color "#5DFF9A" bold True
            outlines [(8, "#02040A", 0, 0)]
        timer 0.8 action Return(True)

label mk_countdown:
    play sound "audio/sfx_minigame_start.mp3"
    call screen mk_countdown_screen
    return


# ------------------------------------------------------------
# TUTORIELS — chrome commun + cycle d'étapes
#
# Chaque minijeu définit son propre screen de tuto :
#   screen tuto_xxx(as_overlay=False):
#       use mk_tuto_chrome("TITRE", étapes, "tuto_xxx", as_overlay):
#           <zone démo animée custom>
#
# Affichage automatique 1ère fois :
#   call mk_tutorial("mg_id", "tuto_xxx")
# Revoir en jeu : use mk_help_button("tuto_xxx")
# ------------------------------------------------------------

transform mk_tuto_panel_in:
    alpha 0.0
    yoffset 30
    easeout 0.30 alpha 1.0 yoffset 0

transform mk_tuto_step_in(delay=0.0):
    alpha 0.0
    xoffset -26
    pause delay
    easeout 0.28 alpha 1.0 xoffset 0

transform mk_tuto_demo_loop:
    alpha 0.0
    easein 0.25 alpha 1.0

transform mk_tuto_badge_pulse:
    zoom 1.0
    ease 0.6 zoom 1.08
    ease 0.6 zoom 1.0
    repeat

# Faux curseur réutilisable pour les démos (un anneau + un point)
transform mk_demo_click_pulse:
    zoom 1.0
    easeout 0.12 zoom 0.78
    easein 0.12 zoom 1.0

screen mk_demo_cursor(cx=0, cy=0):
    fixed:
        xpos cx
        ypos cy
        add Solid("#FFFFFF44") size (34, 34) align (0.5, 0.5) at Transform(rotate=45)
        add Solid("#FFFFFFEE") size (12, 12) align (0.5, 0.5)

screen mk_tuto_chrome(title, steps, screen_name, as_overlay=False):
    modal True
    zorder 420

    add Solid("#02040AE6")
    add Solid("#7DF9FF20", ysize=2) ypos 110
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at mk_scanline_drift

    frame at mk_tuto_panel_in:
        xalign 0.5
        yalign 0.5
        xsize 1480
        ysize 760
        background Fixed(
            Solid("#0A1326F2"),
            Solid("#7DF9FF44", xsize=4),
            Solid("#7DF9FF44", xsize=4, xalign=1.0),
            Solid("#FFFFFF12", ysize=1),
        )
        padding (46, 36)

        vbox:
            spacing 18
            xfill True

            hbox:
                xfill True
                text "{} — {}".format(kd_tr("TUTORIEL"), kd_tr(title)):
                    size 34
                    color "#7DF9FF"
                    bold True
                text "NOUVELLE MÉCANIQUE" at mk_tuto_badge_pulse:
                    xalign 1.0
                    size 20
                    color "#FFD166"
                    bold True

            add Solid("#7DF9FF55", xsize=1388, ysize=2)

            hbox:
                spacing 40

                # --- Zone démo animée (fournie par le minijeu) ---
                frame:
                    xsize 760
                    ysize 520
                    background Fixed(
                        Solid("#060D1CEE"),
                        Solid("#7DF9FF22", xsize=3),
                        Solid("#FFFFFF10", ysize=1),
                    )
                    padding (10, 10)

                    fixed at mk_tuto_demo_loop:
                        xfill True
                        yfill True
                        transclude

                # --- Étapes ---
                vbox:
                    spacing 22
                    yalign 0.5

                    for st_idx, st_pair in enumerate(steps):
                        hbox at mk_tuto_step_in(0.25 + st_idx * 0.30):
                            spacing 18

                            frame:
                                xsize 52
                                ysize 52
                                background Solid("#10384D")
                                text "[st_idx + 1]":
                                    align (0.5, 0.5)
                                    size 26
                                    color "#7DF9FF"
                                    bold True

                            vbox:
                                spacing 4
                                yalign 0.5
                                xmaximum 510
                                text kd_tr(st_pair[0]):
                                    size 24
                                    color "#FFFFFF"
                                    bold True
                                text kd_tr(st_pair[1]):
                                    size 20
                                    color "#9FC7D8"

            null height 4

            hbox:
                xalign 0.5
                spacing 30

                textbutton "COMPRIS, ON Y VA":
                    xsize 340
                    ysize 62
                    background Solid("#10384DEE")
                    hover_background Solid("#1D5C7AEE")
                    text_size 26
                    text_color "#FFFFFF"
                    text_xalign 0.5
                    if as_overlay:
                        action Hide(screen_name)
                    else:
                        action Return(True)

                if not as_overlay:
                    textbutton "PASSER":
                        xsize 200
                        ysize 62
                        background Solid("#0A1A2AEE")
                        hover_background Solid("#13304AEE")
                        text_size 24
                        text_color "#9FC7D8"
                        text_xalign 0.5
                        action Return(False)

label mk_tutorial(mg_id, tuto_screen, force=False):
    if force or not mk_tuto_is_seen(mg_id):
        $ mk_tuto_mark_seen(mg_id)
        play sound "audio/sfx_beep.mp3"
        $ renpy.call_screen(tuto_screen, as_overlay=False)
    return

# Bouton "?" à inclure dans le screen du minijeu
screen mk_help_button(tuto_screen):
    textbutton "?":
        xpos 1856
        ypos 14
        xanchor 1.0
        xsize 56
        ysize 56
        background Fixed(Solid("#10384DCC"), Solid("#7DF9FF55", xsize=3))
        hover_background Fixed(Solid("#1D5C7AEE"), Solid("#FFFFFF33", ysize=2))
        text_size 28
        text_color "#7DF9FF"
        text_hover_color "#FFFFFF"
        text_xalign 0.5
        text_yalign 0.5
        action Show(tuto_screen, as_overlay=True)


# ------------------------------------------------------------
# DÉFIS — HUD en jeu
# challenges : liste de (label, done_bool) ou (label, done_bool, failed_bool)
# ------------------------------------------------------------
transform mk_challenge_done_pop:
    zoom 1.0
    easeout 0.14 zoom 1.18
    easein 0.14 zoom 1.0

screen mk_challenge_hud(challenges, xpos_v=24, ypos_v=120):
    frame:
        xpos xpos_v
        ypos ypos_v
        background Fixed(
            Solid("#060D1CD8"),
            Solid("#FFD16655", xsize=3),
            Solid("#FFFFFF10", ysize=1),
        )
        padding (18, 14)

        vbox:
            spacing 8

            text "DÉFIS":
                size 18
                color "#FFD166"
                bold True

            for ch in challenges:
                $ ch_failed = (len(ch) > 2 and ch[2])
                hbox:
                    spacing 10
                    if ch[1]:
                        text "OK" size 20 color "#5DFF9A" bold True at mk_challenge_done_pop
                        text kd_tr(ch[0]) size 18 color "#5DFF9A"
                    elif ch_failed:
                        text "✗" size 20 color "#FF4D6D" bold True
                        text kd_tr(ch[0]) size 18 color "#6E7F8F" strikethrough True
                    else:
                        text "•" size 20 color "#7DF9FF"
                        text kd_tr(ch[0]) size 18 color "#DCF0FF"


# ------------------------------------------------------------
# ÉCHEC / RETRY — écran de relance avec malus de rang
# ------------------------------------------------------------
transform mk_fail_slam:
    alpha 0.0
    zoom 1.6
    easein 0.16 alpha 1.0 zoom 1.0

screen mk_fail_retry_screen(title, mg_id):
    modal True
    zorder 410

    add Solid("#1A0408E0")
    add Solid("#FF4D6D33", ysize=4) ypos 170 at mk_edge_alert
    add Solid("#FF4D6D33", ysize=4) ypos 820 at mk_edge_alert
    text "KAMI.CORE // RETRY PENALTY":
        style "mk_terminal_label"
        color "#FF8FA3"
        xpos 76
        ypos 78

    vbox:
        align (0.5, 0.45)
        spacing 26

        text "ÉCHEC" at mk_fail_slam:
            xalign 0.5
            size 130
            color "#FF4D6D"
            bold True
            outlines [(6, "#02040A", 0, 0)]

        text kd_tr(title):
            xalign 0.5
            size 28
            color "#DCF0FF"

        $ _next_cap = MK_RANK_ORDER[min(len(MK_RANK_ORDER) - 1, mk_get_retries(mg_id))]
        text "Rang maximum à la prochaine tentative : [_next_cap]":
            xalign 0.5
            size 22
            color "#FFD166"

        textbutton "RÉESSAYER":
            xalign 0.5
            xsize 320
            ysize 64
            background Solid("#5C1020EE")
            hover_background Solid("#8A1830EE")
            text_size 28
            text_color "#FFFFFF"
            text_xalign 0.5
            action Return(True)

        if mk_get_retries(mg_id) >= 3:
            textbutton "PASSER LE MINIJEU":
                xalign 0.5
                xsize 320
                ysize 58
                background Solid("#182A3AEE")
                hover_background Solid("#25445EEE")
                text_size 24
                text_color "#BFD7E8"
                text_xalign 0.5
                action Return(False)

label mk_fail_retry(title, mg_id):
    $ mk_add_retry(mg_id)
    play sound "audio/sfx_drop.mp3"
    call screen mk_fail_retry_screen(title, mg_id)
    return


# ------------------------------------------------------------
# Écran de résultats avec rang, défis et record
# ------------------------------------------------------------
transform mk_result_panel_in:
    alpha 0.0
    yoffset 40
    easeout 0.35 alpha 1.0 yoffset 0

transform mk_rank_slam:
    alpha 0.0
    zoom 3.0
    rotate -8
    pause 0.45
    easein 0.16 alpha 1.0 zoom 1.0 rotate 0
    easeout 0.06 zoom 1.12
    easein 0.08 zoom 1.0

transform mk_stat_in(delay=0.0):
    alpha 0.0
    xoffset -22
    pause delay
    easeout 0.25 alpha 1.0 xoffset 0

transform mk_record_blink:
    alpha 1.0
    ease 0.5 alpha 0.45
    ease 0.5 alpha 1.0
    repeat

screen mk_results_screen(title, score, max_score, stats, challenges, rank, is_record, best_rank, retries):
    modal True
    zorder 400

    $ _rcolor = MK_RANK_COLORS[rank]
    $ _rlabel = MK_RANK_LABELS[rank]

    add Solid("#02040AE8")
    add Solid("#7DF9FF1E", ysize=2) ypos 126
    add Solid("#7DF9FF1E", ysize=2) ypos 950
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at mk_scanline_drift
    text "KAMI.CORE // PERFORMANCE VERDICT":
        style "mk_terminal_label"
        xpos 76
        ypos 78

    frame at mk_result_panel_in:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 740
        background Fixed(
            Solid("#0A1326F4"),
            Solid("#7DF9FF44", xsize=4),
            Solid("#7DF9FF44", xsize=4, xalign=1.0),
            Solid("#FFFFFF12", ysize=1),
        )
        padding (50, 36)

        vbox:
            xalign 0.5
            spacing 16

            text (kd_tr("RÉSULTATS") + " — " + kd_tr(title)):
                xalign 0.5
                size 30
                color "#9FC7D8"
                bold True

            add Solid("#7DF9FF66", xsize=980, ysize=2) xalign 0.5

            hbox:
                xalign 0.5
                spacing 60

                # Rang
                vbox:
                    spacing 6
                    yalign 0.5
                    text "[rank]" at mk_rank_slam:
                        xalign 0.5
                        size 190
                        color _rcolor
                        bold True
                        outlines [(6, "#02040A", 0, 0)]
                    text kd_tr(_rlabel):
                        xalign 0.5
                        size 26
                        color _rcolor
                        bold True
                    if is_record:
                        text "★ NOUVEAU RECORD" at mk_record_blink:
                            xalign 0.5
                            size 20
                            color "#FFD700"
                            bold True
                    elif best_rank:
                        text "Record : [best_rank]":
                            xalign 0.5
                            size 20
                            color "#6E8FA8"
                    if retries > 0:
                        text "[retries] retry — rang plafonné":
                            xalign 0.5
                            size 18
                            color "#FF8FA3"

                # Stats + défis
                vbox:
                    spacing 12
                    yalign 0.5

                    text "SCORE  [score] / [max_score]" at mk_stat_in(0.5):
                        size 32
                        color "#FFFFFF"
                        bold True

                    for s_idx, s_pair in enumerate(stats):
                        text (kd_tr(s_pair[0]) + "  —  " + kd_tr(s_pair[1])) at mk_stat_in(0.62 + s_idx * 0.10):
                            size 24
                            color "#DCF0FF"

                    if challenges:
                        null height 6
                        text "DÉFIS  [mk_challenge_count_done(challenges)] / [len(challenges)]" at mk_stat_in(0.9):
                            size 24
                            color "#FFD166"
                            bold True
                        for c_idx, c_pair in enumerate(challenges):
                            hbox at mk_stat_in(1.0 + c_idx * 0.10):
                                spacing 10
                                if c_pair[1]:
                                    text "OK" size 22 color "#5DFF9A" bold True
                                    text kd_tr(c_pair[0]) size 22 color "#5DFF9A"
                                else:
                                    text "✗" size 22 color "#FF4D6D" bold True
                                    text kd_tr(c_pair[0]) size 22 color "#8A9BAB"

            null height 10

            textbutton "CONTINUER":
                xalign 0.5
                xsize 300
                ysize 64
                background Solid("#10384DEE")
                hover_background Solid("#1D5C7AEE")
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                action Return(rank)

label mk_show_results(title, score, max_score, stats=[], challenges=[], mg_id=None, retries=0):
    python:
        _mk_rank = mk_compute_rank(score, max_score, retries)
        _mk_best_prev = persistent.mk_best_ranks.get(mg_id) if mg_id else None
        _mk_is_record = mk_register_best(mg_id, _mk_rank)
    if _mk_rank in ("S", "A"):
        play sound "audio/sfx_victory.mp3"
    call screen mk_results_screen(title, score, max_score, stats, challenges, _mk_rank, _mk_is_record, _mk_best_prev, retries)
    if mg_id:
        $ mk_reset_retries(mg_id)
    return _return
