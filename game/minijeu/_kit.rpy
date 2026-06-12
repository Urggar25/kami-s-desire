# ============================================================
# _kit.rpy — Kit minijeu partagé
# Compte à rebours READY/GO + écran de résultats avec rang.
#
# Usage :
#   call mk_countdown                       # 3..2..1..GO
#   call mk_show_results("ENTRAÎNEMENT", score, max_score, stats=[("Combo max","8"), ...])
#   # rang auto : S >= 95%, A >= 80%, B >= 60%, C >= 40%, D sinon
# ============================================================

init python:
    def mk_compute_rank(score, max_score):
        ratio = (float(score) / float(max_score)) if max_score else 0.0
        if ratio >= 0.95: return "S"
        if ratio >= 0.80: return "A"
        if ratio >= 0.60: return "B"
        if ratio >= 0.40: return "C"
        return "D"

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

screen mk_countdown_screen():
    modal True
    zorder 400

    add Solid("#02040Acc")

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
# Écran de résultats avec rang
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

screen mk_results_screen(title, score, max_score, stats):
    modal True
    zorder 400

    $ _rank = mk_compute_rank(score, max_score)
    $ _rcolor = MK_RANK_COLORS[_rank]
    $ _rlabel = MK_RANK_LABELS[_rank]

    add Solid("#02040AE8")

    frame at mk_result_panel_in:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 680
        background Solid("#0A1326EE")
        padding (50, 40)

        vbox:
            xalign 0.5
            spacing 18

            text "RÉSULTATS — [title]":
                xalign 0.5
                size 30
                color "#9FC7D8"
                bold True

            add Solid("#7DF9FF66", xsize=860, ysize=2) xalign 0.5

            hbox:
                xalign 0.5
                spacing 70

                # Rang
                vbox:
                    spacing 6
                    yalign 0.5
                    text "[_rank]" at mk_rank_slam:
                        xalign 0.5
                        size 200
                        color _rcolor
                        bold True
                        outlines [(6, "#02040A", 0, 0)]
                    text "[_rlabel]":
                        xalign 0.5
                        size 26
                        color _rcolor
                        bold True

                # Stats
                vbox:
                    spacing 14
                    yalign 0.5

                    text "SCORE  [score] / [max_score]" at mk_stat_in(0.5):
                        size 34
                        color "#FFFFFF"
                        bold True

                    for s_idx, s_pair in enumerate(stats):
                        text "[s_pair[0]]  —  [s_pair[1]]" at mk_stat_in(0.65 + s_idx * 0.12):
                            size 26
                            color "#DCF0FF"

            null height 14

            textbutton "CONTINUER":
                xalign 0.5
                xsize 300
                ysize 64
                background Solid("#10384DEE")
                hover_background Solid("#1D5C7AEE")
                text_size 28
                text_color "#FFFFFF"
                text_xalign 0.5
                action Return(_rank)

label mk_show_results(title, score, max_score, stats=[]):
    if mk_compute_rank(score, max_score) in ("S", "A"):
        play sound "audio/sfx_victory.mp3"
    call screen mk_results_screen(title, score, max_score, stats)
    return _return
