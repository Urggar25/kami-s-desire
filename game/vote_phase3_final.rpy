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
screen vote_screen():
    modal True
    zorder 220

    add "images/background/bg_conclave.png" at adaptive_fullscreen
    add Solid("#060B17A0")
    add Solid("#4AD5FF20", ysize=2) ypos 120
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at vote_phase3_scanline
    text "KAMI.CORE // SCRUTIN FINAL":
        xpos 70
        ypos 74
        font "fonts/Barlow-Light.ttf"
        size 18
        color "#78DFFF"
        kerning 4

    # Timer + barre de décompte (10s)
    frame:
        xalign 0.5
        yalign 0.08
        xsize 980
        ysize 84
        background Fixed(
            Solid("#0D1320DD"),
            Solid("#4AD5FF55", xsize=4),
            Solid("#FFFFFF12", ysize=1),
        )

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 6

            text "VOTE EN COURS  //  [vote_phase3_time_left]s":
                xalign 0.5
                font "fonts/day_font.ttf"
                size 34
                color "#D6F0FF"
                outlines [(2, "#56D7FF88", 0, 0)]

            bar:
                xalign 0.5
                xsize 860
                ysize 14
                value AnimatedValue(value=vote_phase3_time_left, range=10.0, delay=0.22)
                left_bar Solid("#4AD5FF")
                right_bar Solid("#1A2339")

    text "CHOISISSEZ L'ISSUE DU VOTE":
        xalign 0.5
        yalign 0.20
        font "fonts/day_font.ttf"
        size 52
        color "#E8F6FF"
        outlines [(3, "#74D7FF88", 0, 0)]

    hbox:
        xalign 0.5
        yalign 0.58
        spacing 54

        # ---------------------
        # Bouton POUR
        # ---------------------
        button:
            at vote_phase3_intro_left, vote_phase3_btn_pulse
            xsize 500
            ysize 360
            background Fixed(Solid("#0F2A1CCF"), Solid("#87FFD055", xsize=4))
            hover_background Fixed(Solid("#1C5A3ACC"), Solid("#87FFD0", xsize=5), Solid("#FFFFFF20", ysize=2))
            hovered SetVariable("vote_phase3_hover_side", "pour")
            unhovered SetVariable("vote_phase3_hover_side", None)

            action [
                SetVariable("vote_phase3_player_choice", "pour"),
                Play("sound", "audio/sfx_beep.mp3"),
                With(vpunch),
                Return("pour"),
            ]

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                if vote_phase3_hover_side == "pour":
                    at vote_phase3_hover_zoom

                text "Vote Pour":
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 56
                    bold True
                    color "#9FFFD4"
                    outlines [(4, "#2CFF9D88", 0, 0)]

                text "Changer les règles":
                    xalign 0.5
                    font "fonts/Barlow-Light.ttf"
                    size 24
                    color "#D6FFF0"

        # ---------------------
        # Bouton ABSTENTION
        # ---------------------
        button:
            at vote_phase3_btn_pulse
            xsize 500
            ysize 360
            background Fixed(Solid("#202536CF"), Solid("#C6CBD555", xsize=4))
            hover_background Fixed(Solid("#3A4054CC"), Solid("#E6ECF8", xsize=5), Solid("#FFFFFF20", ysize=2))
            hovered SetVariable("vote_phase3_hover_side", "abstention")
            unhovered SetVariable("vote_phase3_hover_side", None)

            action [
                SetVariable("vote_phase3_player_choice", "abstention"),
                Play("sound", "audio/sfx_beep.mp3"),
                With(vpunch),
                Return("abstention"),
            ]

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                if vote_phase3_hover_side == "abstention":
                    at vote_phase3_hover_zoom

                text "Abstention":
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 54
                    bold True
                    color "#E6ECF8"
                    outlines [(4, "#8B95A888", 0, 0)]

                text "Laisser le système trancher":
                    xalign 0.5
                    font "fonts/Barlow-Light.ttf"
                    size 24
                    color "#EEF2F8"

        # ---------------------
        # Bouton CONTRE
        # ---------------------
        button:
            at vote_phase3_intro_right, vote_phase3_btn_pulse
            xsize 500
            ysize 360
            background Fixed(Solid("#2A1010CF"), Solid("#FFB2B255", xsize=4))
            hover_background Fixed(Solid("#5A1F1FCC"), Solid("#FFB2B2", xsize=5), Solid("#FFFFFF20", ysize=2))
            hovered SetVariable("vote_phase3_hover_side", "contre")
            unhovered SetVariable("vote_phase3_hover_side", None)

            action [
                SetVariable("vote_phase3_player_choice", "contre"),
                Play("sound", "audio/sfx_beep.mp3"),
                With(vpunch),
                Return("contre"),
            ]

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                if vote_phase3_hover_side == "contre":
                    at vote_phase3_hover_zoom

                text "Vote contre":
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 56
                    bold True
                    color "#FFB2B2"
                    outlines [(4, "#FF474788", 0, 0)]

                text "Maintenir le cadre":
                    xalign 0.5
                    font "fonts/Barlow-Light.ttf"
                    size 24
                    color "#FFE8E8"

    # Timer logique
    timer 1.0 repeat True action If(
        vote_phase3_time_left > 0,
        true=SetVariable("vote_phase3_time_left", vote_phase3_time_left - 1),
        false=NullAction()
    )

    timer 10.0 action [
        SetVariable("vote_phase3_player_choice", "abstention"),
        Return("timeout")
    ]

# -----------------------------
# Écran 2 — dépouillement visuel
# -----------------------------
screen vote_phase3_tally_screen():
    modal True
    zorder 230

    add Solid("#04070FCC")
    add "images/background/bg_conclave.png" at adaptive_fullscreen
    add Solid("#4AD5FF18", ysize=2) ypos 118
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at vote_phase3_scanline

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1560
        ysize 920
        background Fixed(
            Solid("#0A1222D8"),
            Solid("#4AD5FF44", xsize=4),
            Solid("#4AD5FF44", xsize=4, xalign=1.0),
            Solid("#FFFFFF10", ysize=1),
        )

    text "DÉPOUILLEMENT DES VOTES":
        xalign 0.5
        yalign 0.11
        font "fonts/day_font.ttf"
        size 62
        color "#E6F4FF"
        outlines [(4, "#65D4FF88", 0, 0)]
        at vote_phase3_title_glow

    timer 0.85 repeat True action If(
        vote_phase3_tally_done,
        true=NullAction(),
        false=Function(vote_phase3_tally_step)
    )

    timer 0.2 repeat True action If(
        vote_phase3_tally_done,
        true=Return(True),
        false=NullAction()
    )

    if vote_phase3_current_name:
        frame:
            xalign 0.5
            yalign 0.285
            xsize 720
            ysize 76
            background Fixed(
                Solid("#071426DD"),
                Solid("#4AD5FF66", xsize=4),
                Solid("#FFFFFF12", ysize=1),
            )

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 18
                text "BULLETIN":
                    font "fonts/Barlow-Light.ttf"
                    size 22
                    color "#78DFFF"
                    kerning 4
                text "[vote_phase3_current_name]":
                    font "fonts/day_font.ttf"
                    size 40
                    color "#E6F4FF"
                    outlines [(2, "#203050", 0, 0)]

    if vote_phase3_current_vote == "pour":
        text "POUR":
            xalign 0.5
            yalign 0.42
            font "fonts/day_font.ttf"
            size 110
            bold True
            color "#87FFD0"
            outlines [(6, "#28FF9C88", 0, 0)]
            at vote_phase3_symbol_pulse
        text "✦ ✦ ✦":
            xalign 0.5
            yalign 0.54
            font "fonts/day_font.ttf"
            size 60
            color "#58FFC0"
            at vote_phase3_float_up

    elif vote_phase3_current_vote == "abstention":
        text "ABSTENTION":
            xalign 0.5
            yalign 0.42
            font "fonts/day_font.ttf"
            size 96
            bold True
            color "#C6CBD5"
            outlines [(5, "#8B95A888", 0, 0)]
            at vote_phase3_symbol_pulse

    elif vote_phase3_current_vote == "contre":
        text "CONTRE":
            xalign 0.5
            yalign 0.42
            font "fonts/day_font.ttf"
            size 110
            bold True
            color "#FFB0B0"
            outlines [(6, "#FF3F3F88", 0, 0)]
            at vote_phase3_symbol_pulse
        text "✦ ✦ ✦":
            xalign 0.5
            yalign 0.54
            font "fonts/day_font.ttf"
            size 60
            color "#FF7070"
            at vote_phase3_float_down

    # Compteurs progressifs
    vbox:
        xalign 0.5
        yalign 0.86
        spacing 16

        text "POUR : [vote_phase3_counts['pour']]":
            font "fonts/day_font.ttf"
            size 32
            color "#A8FFD8"
        bar:
            xsize 1200
            ysize 18
            value AnimatedValue(value=vote_phase3_counts["pour"], range=12.0, delay=0.35)
            left_bar Solid("#28FF9D")
            right_bar Solid("#203428")

        text "ABSTENTION : [vote_phase3_counts['abstention']]":
            font "fonts/day_font.ttf"
            size 32
            color "#E1E5EC"
        bar:
            xsize 1200
            ysize 18
            value AnimatedValue(value=vote_phase3_counts["abstention"], range=12.0, delay=0.35)
            left_bar Solid("#B6BBC7")
            right_bar Solid("#2A2F39")

        text "CONTRE : [vote_phase3_counts['contre']]":
            font "fonts/day_font.ttf"
            size 32
            color "#FFC3C3"
        bar:
            xsize 1200
            ysize 18
            value AnimatedValue(value=vote_phase3_counts["contre"], range=12.0, delay=0.35)
            left_bar Solid("#FF4040")
            right_bar Solid("#3A2323")


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
        scene Solid("#0AFF8844")
        with Dissolve(0.12)
    else:
        scene Solid("#FF2A2A44")
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
