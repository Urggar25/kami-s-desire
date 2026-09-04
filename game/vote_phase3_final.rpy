# Phase 3 — Vote final + dépouillement animé

default amendement_passe = False
default vote_phase3_player_choice = None
default vote_phase3_time_left = 10
default vote_phase3_hover_side = None
default vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
default vote_phase3_current_name = ""
default vote_phase3_current_vote = None
default vote_phase3_results = []
default vote_phase3_pending_votes = []
default vote_phase3_tally_index = 0
default vote_phase3_tally_done = False
default vote_phase3_amendment_override = None

init python:
    import random

    def vote_phase3_safe_play(path, fallback):
        if renpy.loadable(path):
            renpy.sound.play(path)
        elif renpy.loadable(fallback):
            renpy.sound.play(fallback)

    def vote_phase3_build_results(player_choice):
        """Construit les 12 votes : 11 persos via score, + Noam via choix joueur."""
        display_names = {
            "ryn": "Ryn",
            "julian": "Julian",
            "nyra": "Nyra",
            "kael": "Kael",
            "mara": "Mara",
            "elias": "Elias",
            "lysa": "Lysa",
            "iris": "Iris",
            "tomas": "Tomas",
            "elen": "Elen",
            "sael": "Sael",
        }

        player_vote = player_choice if player_choice in ("pour", "contre", "abstention") else "abstention"

        # Stats des 11 personnages (hors Noam) issues de la phase 2.
        stats = dict(getattr(store, "debat_day3_live_vote_stats", {}))
        if not stats and "DEBAT_DAY3_BASE_VOTE_STATS" in globals():
            stats = dict(DEBAT_DAY3_BASE_VOTE_STATS)

        results = []
        for key, name in display_names.items():
            stat_value = stats.get(key, 0)
            if stat_value > 1:
                vote = "pour"
            elif stat_value < -1:
                vote = "contre"
            else:
                vote = "abstention"
            results.append((name, vote))

        # Vote du joueur (Noam).
        results.append(("Noam", player_vote))

        random.shuffle(results)
        return results

    def vote_phase3_tally_step():
        """Dépouille 1 vote aléatoire et le retire de la liste restante."""
        if store.vote_phase3_tally_done:
            return

        if not store.vote_phase3_pending_votes:
            store.vote_phase3_tally_done = True
            return

        pick_index = random.randrange(len(store.vote_phase3_pending_votes))
        rep_name, rep_vote = store.vote_phase3_pending_votes.pop(pick_index)

        store.vote_phase3_current_name = rep_name
        store.vote_phase3_current_vote = rep_vote
        store.vote_phase3_counts[rep_vote] += 1
        store.vote_phase3_tally_index += 1

        if rep_vote == "pour":
            vote_phase3_safe_play("audio/sfx_vote_pour.wav", "audio/sfx_beep.mp3")
        elif rep_vote == "abstention":
            vote_phase3_safe_play("audio/sfx_vote_abstention.wav", "audio/sfx_paper.mp3")
        else:
            vote_phase3_safe_play("audio/sfx_vote_contre.wav", "audio/sfx_tambour.mp3")

        if not store.vote_phase3_pending_votes:
            store.vote_phase3_tally_done = True




    def vote_phase3_amendment_text():
        override = getattr(store, "vote_phase3_amendment_override", None)
        if override:
            return override
        if "DOSSIER_PROPOSITIONS" in globals():
            prop = DOSSIER_PROPOSITIONS.get("p1_vote_commerce", {})
            if prop.get("formulation"):
                return prop["formulation"]
            if prop.get("title"):
                return prop["title"].replace("\n", " ")
        return "Autoriser le transport, la vente et l'échange de marchandises entre les districts."

    def vote_phase3_status_text():
        if not store.vote_phase3_tally_done:
            if store.vote_phase3_tally_index <= 0:
                return "En attente du premier bulletin..."
            return "Dépouillement en cours..."
        if store.vote_phase3_counts.get("contre", 0) > 0:
            return "Amendement refusé : au moins un vote contre."
        return "Amendement adopté : aucun vote contre."

# -----------------------------
# ATL — ambiance néon / dynamiques UI
# -----------------------------
transform vote_phase3_intro_left:
    alpha 0.0
    xoffset -420
    zoom 0.92
    easeout 0.55 alpha 1.0 xoffset 0 zoom 1.0

transform vote_phase3_intro_right:
    alpha 0.0
    xoffset 420
    zoom 0.92
    easeout 0.55 alpha 1.0 xoffset 0 zoom 1.0

transform vote_phase3_btn_pulse:
    zoom 1.0
    ease 1.2 zoom 1.03
    ease 1.2 zoom 1.0
    repeat

transform vote_phase3_hover_zoom:
    zoom 1.08

transform vote_phase3_title_glow:
    alpha 0.7
    ease 1.1 alpha 1.0
    ease 1.1 alpha 0.7
    repeat

transform vote_phase3_symbol_pulse:
    zoom 0.94
    alpha 0.7
    ease 0.45 zoom 1.05 alpha 1.0
    ease 0.45 zoom 1.0 alpha 0.85
    repeat

transform vote_phase3_float_up:
    yoffset 0
    alpha 0.2
    ease 1.0 yoffset -24 alpha 0.8
    ease 1.0 yoffset -46 alpha 0.0
    repeat

transform vote_phase3_float_down:
    yoffset 0
    alpha 0.2
    ease 1.0 yoffset 24 alpha 0.8
    ease 1.0 yoffset 46 alpha 0.0
    repeat

transform vote_phase3_scanline:
    yoffset -1080
    linear 8.0 yoffset 1080
    repeat


# -----------------------------
# Écran 1 — vote initial (10s)
# -----------------------------
transform vote_phase3_panel_breathe:
    alpha 0.86
    ease 1.4 alpha 1.0
    ease 1.4 alpha 0.86
    repeat

transform vote_phase3_card_reveal:
    alpha 0.0
    yoffset 20
    easeout 0.35 alpha 1.0 yoffset 0

transform vote_phase3_ballot_pop:
    zoom 0.92
    alpha 0.0
    easeout 0.22 zoom 1.08 alpha 1.0
    easein 0.18 zoom 1.0


screen vote_screen():
    modal True
    zorder 220

    $ timer_ratio = float(vote_phase3_time_left) / 10.0

    add "bg_conclave" at adaptive_fullscreen
    add Solid("#020509CC")
    add Solid("#00000066")
    add Solid("#FFFFFF06", xsize=1920, ysize=20) at vote_phase3_scanline

    fixed:
        xfill True
        yfill True

        frame:
            xalign 0.5
            ypos 58
            xsize 980
            ysize 88
            background Fixed(
                Solid("#070A0EDD"),
                Solid("#6B747A55", ysize=1),
                Solid("#6B747A55", ysize=1, yalign=1.0),
                Solid("#FFFFFF08", xsize=1),
                Solid("#FFFFFF08", xsize=1, xalign=1.0),
            )
            padding (28, 14)
            vbox:
                xfill True
                spacing 10
                hbox:
                    xalign 0.5
                    spacing 72
                    text "VOTE EN COURS" size 34 color "#D7D2C8" font "fonts/Rajdhani-SemiBold.ttf" kerning 5
                    text "[vote_phase3_time_left]s" size 34 color "#D7D2C8" font "fonts/Rajdhani-SemiBold.ttf" kerning 4
                bar:
                    xalign 0.5
                    xsize 900
                    ysize 16
                    value AnimatedValue(value=timer_ratio, range=1.0, delay=0.20)
                    left_bar Solid("#9CD7E6")
                    right_bar Solid("#161A20")

        vbox:
            xpos 0
            ypos 205
            xsize 1920
            spacing 20
            text "CHOISISSEZ L’ISSUE DU VOTE" xalign 0.5 size 62 color "#E7E2D8" font "fonts/Rajdhani-SemiBold.ttf" kerning 4
            hbox:
                xalign 0.5
                spacing 0
                add Solid("#6B747A55", xsize=410, ysize=1) yalign 0.5
                text "◆" size 20 color "#8C867B" font "fonts/Rajdhani-SemiBold.ttf"
                add Solid("#6B747A55", xsize=410, ysize=1) yalign 0.5

        hbox:
            xpos 132
            ypos 388
            spacing 46
            use vote_phase3_choice_card("pour", "+", "VOTE POUR", "Changer les règles", "#A7BE83", "#162016DD")
            use vote_phase3_choice_card("abstention", "=", "ABSTENTION", "Laisser le système trancher", "#A9AAA6", "#1A1A1ADD")
            use vote_phase3_choice_card("contre", "-", "VOTE CONTRE", "Maintenir le cadre", "#B96455", "#221211DD")

    timer 1.0 repeat True action If(
        vote_phase3_time_left > 0,
        true=SetVariable("vote_phase3_time_left", vote_phase3_time_left - 1),
        false=NullAction()
    )

    timer 10.0 action [
        SetVariable("vote_phase3_player_choice", "abstention"),
        Return("timeout")
    ]

screen vote_phase3_choice_card(choice_id, icon, label, subtitle, color, fill):
    $ hovered = (vote_phase3_hover_side == choice_id)
    button:
        xsize 500
        ysize 396
        at vote_phase3_btn_pulse
        background Fixed(
            Solid(fill),
            Solid(color + "AA", xsize=2),
            Solid(color + "AA", xsize=2, xalign=1.0),
            Solid(color + "99", ysize=2),
            Solid(color + "99", ysize=2, yalign=1.0),
            Solid("#FFFFFF07", ysize=1),
        )
        hover_background Fixed(
            Solid("#070A0EDD"),
            Solid(color + "26"),
            Solid(color, xsize=3),
            Solid(color, xsize=3, xalign=1.0),
            Solid(color, ysize=3),
            Solid(color, ysize=3, yalign=1.0),
            Solid("#FFFFFF18", ysize=2),
        )
        hovered SetVariable("vote_phase3_hover_side", choice_id)
        unhovered SetVariable("vote_phase3_hover_side", None)
        action [
            SetVariable("vote_phase3_player_choice", choice_id),
            Play("sound", "audio/sfx_beep.mp3"),
            With(vpunch),
            Return(choice_id),
        ]

        fixed:
            xfill True
            yfill True
            add Solid(color + ("22" if hovered else "10"), xsize=460, ysize=356) xpos 20 ypos 20
            if hovered:
                add Solid(color + "88", xsize=390, ysize=1) xpos 55 ypos 28
                add Solid(color + "88", xsize=390, ysize=1) xpos 55 ypos 367

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 22
                frame:
                    xalign 0.5
                    xsize 92
                    ysize 92
                    background Fixed(
                        Solid("#05080CB0"),
                        Solid(color + "45", xsize=2),
                        Solid(color + "45", xsize=2, xalign=1.0),
                        Solid(color + "45", ysize=2),
                        Solid(color + "45", ysize=2, yalign=1.0),
                    )
                    padding (0, 0)
                    text icon xalign 0.5 yalign 0.5 size 58 color color font "fonts/Rajdhani-SemiBold.ttf"

                text kd_tr(label) xalign 0.5 size 46 color color font "fonts/Rajdhani-SemiBold.ttf" kerning 3
                text kd_tr(subtitle) xalign 0.5 text_align 0.5 xmaximum 420 size 27 color "#D7D2C8" font "fonts/Barlow-Light.ttf"


screen vote_phase3_tally_screen():
    modal True
    zorder 230

    $ total_votes = max(1, len(vote_phase3_results))
    $ progress_ratio = float(vote_phase3_tally_index) / float(total_votes)
    $ current_label = kd_tr(vote_phase3_current_vote.upper()) if vote_phase3_current_vote else "..."
    $ current_color = {"pour": "#43A8FF", "abstention": "#F2B63E", "contre": "#FF4747"}.get(vote_phase3_current_vote, "#9BA7B4")

    add "bg_conclave" at adaptive_fullscreen
    add Solid("#02060DE8")
    add Solid("#FFFFFF07", xsize=1920, ysize=20) at vote_phase3_scanline

    fixed:
        xfill True
        yfill True

        hbox:
            xpos 58 ypos 34 spacing 14
            text "//" size 34 color "#AEB8C2" font "fonts/Rajdhani-SemiBold.ttf"
            vbox:
                spacing 2
                text "DÉPOUILLEMENT DES VOTES" size 36 color "#E8EEF4" font "fonts/Rajdhani-SemiBold.ttf"
                text "Les votes sont secrets - les résultats seuls comptent." size 22 color "#AEB8C2" font "fonts/Barlow-Light.ttf"

        hbox:
            xpos 1380 ypos 46 spacing 16
            text "PHASE 3/3" size 22 color "#AEB8C2" font "fonts/Rajdhani-SemiBold.ttf"
            for pi in range(1, 4):
                add Solid("#FF3F3F" if pi == 3 else "#69717A", xsize=22, ysize=22)

        frame:
            xpos 58 ypos 128 xsize 1804 ysize 180
            background Fixed(
                Solid("#071018DA"),
                Solid("#6C7A8655", ysize=1),
                Solid("#6C7A8655", ysize=1, yalign=1.0),
                Solid("#4CB7FF66", xsize=3),
                Solid("#4CB7FF66", xsize=3, xalign=1.0),
            )
            padding (36, 24)
            vbox:
                xalign 0.5
                spacing 12
                text "AMENDEMENT N°1" xalign 0.5 size 25 color "#4CB7FF" font "fonts/Rajdhani-SemiBold.ttf" kerning 4
                text kd_tr(vote_phase3_amendment_text()) xalign 0.5 text_align 0.5 size 30 color "#F2F5F8" font "fonts/Barlow-Light.ttf" xmaximum 1500 line_spacing 4

        hbox:
            xpos 0 ypos 348 xsize 1920 spacing 22
            null width 415
            add Solid("#FF3F3F88", xsize=8, ysize=8) yalign 0.5
            add Solid("#6C7A8633", xsize=245, ysize=1) yalign 0.5
            text "COMPTAGE DES VOTES" size 30 color "#E2E8EF" font "fonts/Rajdhani-SemiBold.ttf" kerning 3
            add Solid("#6C7A8633", xsize=245, ysize=1) yalign 0.5
            add Solid("#FF3F3F88", xsize=8, ysize=8) yalign 0.5

        text "Bulletin [vote_phase3_tally_index] / [total_votes]" xalign 0.5 ypos 392 size 22 color "#AEB8C2" font "fonts/Barlow-Light.ttf"

        if vote_phase3_current_vote:
            frame:
                xpos 760 ypos 426 xsize 400 ysize 82
                at vote_phase3_ballot_pop
                background Fixed(Solid("#08111CE8"), Solid(current_color, xsize=4), Solid(current_color, xsize=4, xalign=1.0))
                padding (18, 10)
                vbox:
                    xalign 0.5 yalign 0.5 spacing 2
                    text "BULLETIN DÉPOUILLÉ" xalign 0.5 size 16 color "#93A1AE" font "fonts/Rajdhani-SemiBold.ttf" kerning 3
                    text current_label xalign 0.5 size 34 color current_color font "fonts/Rajdhani-SemiBold.ttf"

        hbox:
            xpos 162 ypos 530 spacing 40
            use vote_phase3_count_card("POUR", "pour", "#43A8FF", "+", vote_phase3_counts["pour"], total_votes)
            use vote_phase3_count_card("ABSTENTION", "abstention", "#F2B63E", "=", vote_phase3_counts["abstention"], total_votes)
            use vote_phase3_count_card("CONTRE", "contre", "#FF4747", "-", vote_phase3_counts["contre"], total_votes)

        frame:
            xpos 162 ypos 842 xsize 1596 ysize 96
            background Fixed(Solid("#081018DD"), Solid("#FF3F3F66", xsize=4), Solid("#6C7A8644", ysize=1), Solid("#6C7A8644", ysize=1, yalign=1.0))
            padding (30, 18)
            hbox:
                spacing 28
                text "!" size 44 color "#FF4747" font "fonts/Rajdhani-SemiBold.ttf"
                vbox:
                    spacing 4
                    text "RÈGLE D’UNANIMITÉ" size 24 color "#FF4747" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                    text "Si une seule personne vote contre, l’amendement est immédiatement refusé. L’abstention ne bloque pas l’adoption." size 22 color "#D5D9DE" font "fonts/Barlow-Light.ttf"

        frame:
            xpos 58 ypos 960 xsize 1804 ysize 92
            background Fixed(Solid("#071018E2"), Solid("#6C7A8644", ysize=1), Solid("#4CB7FF55", xsize=3), Solid("#4CB7FF55", xsize=3, xalign=1.0))
            padding (32, 12)
            vbox:
                xalign 0.5 spacing 4
                text "STATUT" xalign 0.5 size 20 color "#AEB8C2" font "fonts/Rajdhani-SemiBold.ttf" kerning 3
                text kd_tr(vote_phase3_status_text()) xalign 0.5 text_align 0.5 size 31 color ("#FF6262" if vote_phase3_counts["contre"] > 0 else "#E8EEF4") font "fonts/Barlow-Light.ttf"

        bar:
            xpos 560 ypos 1060 xsize 800 ysize 8
            value AnimatedValue(value=progress_ratio, range=1.0, delay=0.35)
            left_bar Solid("#4CB7FF")
            right_bar Solid("#1A2339")

    timer 0.9 repeat True action If(
        vote_phase3_tally_done,
        true=NullAction(),
        false=Function(vote_phase3_tally_step)
    )

    timer 2.0 repeat True action If(
        vote_phase3_tally_done,
        true=Return(True),
        false=NullAction()
    )

screen vote_phase3_count_card(title, key, color, icon, count, total_votes):
    frame:
        xsize 506 ysize 285
        at vote_phase3_card_reveal
        background Fixed(
            Solid("#070D14DD"),
            Solid(color + "99", xsize=2),
            Solid(color + "99", xsize=2, xalign=1.0),
            Solid(color + "55", ysize=1),
            Solid(color + "55", ysize=1, yalign=1.0),
        )
        padding (24, 26)
        vbox:
            xalign 0.5
            spacing 20
            text kd_tr(title) xalign 0.5 size 34 color color font "fonts/Rajdhani-SemiBold.ttf" kerning 3
            text "[count]" xalign 0.5 size 60 color "#E8EEF4" font "fonts/Rajdhani-SemiBold.ttf"
            text "Voix" xalign 0.5 size 24 color "#AEB8C2" font "fonts/Barlow-Light.ttf"
            bar:
                xalign 0.5
                xsize 330
                ysize 8
                value AnimatedValue(value=count, range=total_votes, delay=0.35)
                left_bar Solid(color)
                right_bar Solid("#27313A")
            text icon xalign 0.5 size 30 color color font "fonts/Rajdhani-SemiBold.ttf"


# -----------------------------
# Label principal demandé
# -----------------------------
label vote_phase3_final:
    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    scene black with dissolve

    # Vote joueur (ou timeout => abstention par défaut)
    $ _vote_result = renpy.call_screen("vote_screen")

    if _vote_result == "pour":
        scene expression Solid("#0AFF8844")
        with Dissolve(0.12)
    else:
        scene expression Solid("#FF2A2A44")
        with Dissolve(0.12)

    # Préparation dépouillement
    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None
    $ vote_phase3_results = vote_phase3_build_results(vote_phase3_player_choice)
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    $ renpy.pause(0.8, hard=False)

    if vote_phase3_counts["contre"] == 0:
        jump _3_VOTE_POUR
    else:
        jump _3_VOTE_CONTRE
