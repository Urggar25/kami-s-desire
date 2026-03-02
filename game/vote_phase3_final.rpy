# Phase 3 — Vote final + dépouillement animé

default amendement_passe = False
default vote_phase3_player_choice = None
default vote_phase3_time_left = 10
default vote_phase3_hover_side = None
default vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
default vote_phase3_current_name = ""
default vote_phase3_current_vote = None
default vote_phase3_results = []
default vote_phase3_tally_index = 0
default vote_phase3_tally_done = False

init python:
    import random

    VOTE_PHASE3_REPRESENTANTS = [
        "Ryn", "Julian", "Nyra", "Kael", "Mara", "Elias",
        "Lysa", "Iris", "Tomas", "Elen", "Sael", "Noam",
    ]

    def vote_phase3_build_results(player_choice):
        """Prépare 12 votes. Le vote de Noam reflète le choix joueur (timeout => abstention)."""
        names = list(VOTE_PHASE3_REPRESENTANTS)
        random.shuffle(names)

        player_vote = player_choice if player_choice in ("pour", "contre", "abstention") else "abstention"
        npc_pool = ["pour", "pour", "pour", "abstention", "abstention", "abstention"]

        results = []
        for name in names:
            if name == "Noam":
                vote = player_vote
            else:
                vote = random.choice(npc_pool)
            results.append((name, vote))

        # Évite un résultat 100% abstention (hors cas voulu si Noam s'abstient).
        if all(v == "abstention" for _, v in results):
            candidates = [i for i, (n, _) in enumerate(results) if n != "Noam"]
            if candidates:
                idx = random.choice(candidates)
                n, _ = results[idx]
                results[idx] = (n, "pour")

        return results

    def vote_phase3_tally_step():
        """Dépouille un vote à chaque appel et marque la fin une fois la liste épuisée."""
        if store.vote_phase3_tally_done:
            return

        if store.vote_phase3_tally_index >= len(store.vote_phase3_results):
            store.vote_phase3_tally_done = True
            return

        _, rep_vote = store.vote_phase3_results[store.vote_phase3_tally_index]
        store.vote_phase3_current_name = ""
        store.vote_phase3_current_vote = rep_vote
        store.vote_phase3_counts[rep_vote] += 1

        if rep_vote == "pour":
            renpy.sound.play("sound/sfx_vote_pour.ogg")
        elif rep_vote == "abstention":
            renpy.sound.play("sound/sfx_abstention.ogg")
        else:
            renpy.sound.play("sound/sfx_contre.ogg")

        store.vote_phase3_tally_index += 1

        if store.vote_phase3_tally_index >= len(store.vote_phase3_results):
            store.vote_phase3_tally_done = True

        renpy.restart_interaction()


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


# -----------------------------
# Écran 1 — vote initial (10s)
# -----------------------------
screen vote_screen():
    modal True
    zorder 220

    add "images/background/bg_conclave.png" at adaptive_fullscreen
    add Solid("#060B17A0")

    # Timer + barre de décompte (10s)
    frame:
        xalign 0.5
        yalign 0.08
        xsize 980
        ysize 84
        background Solid("#0D1320CC")

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
        spacing 120

        # ---------------------
        # Bouton POUR
        # ---------------------
        button:
            at vote_phase3_intro_left, vote_phase3_btn_pulse
            xsize 600
            ysize 360
            background Solid("#0F2A1CCF")
            hover_background Solid("#1C5A3ACC")
            hovered SetVariable("vote_phase3_hover_side", "pour")
            unhovered SetVariable("vote_phase3_hover_side", None)

            action [
                SetVariable("vote_phase3_player_choice", "pour"),
                Play("sound", "sound/sfx_vote_click.ogg"),
                With(vpunch),
                Return("pour"),
            ]

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                if vote_phase3_hover_side == "pour":
                    at vote_phase3_hover_zoom

                text "VOTER POUR":
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 62
                    bold True
                    color "#9FFFD4"
                    outlines [(4, "#2CFF9D88", 0, 0)]

                text "Suppression des bons\n+ liberté marchande":
                    text_align 0.5
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 36
                    color "#D8FFF1"
                    outlines [(2, "#0C2A1C", 0, 0)]

                if vote_phase3_hover_side == "pour":
                    text "✦  ✦  ✦":
                        xalign 0.5
                        font "fonts/day_font.ttf"
                        size 46
                        color "#68FFC1"
                        at vote_phase3_float_up

        # ---------------------
        # Bouton CONTRE
        # ---------------------
        button:
            at vote_phase3_intro_right, vote_phase3_btn_pulse
            xsize 600
            ysize 360
            background Solid("#2A1010CF")
            hover_background Solid("#5A1F1FCC")
            hovered SetVariable("vote_phase3_hover_side", "contre")
            unhovered SetVariable("vote_phase3_hover_side", None)

            action [
                SetVariable("vote_phase3_player_choice", "contre"),
                Play("sound", "sound/sfx_vote_click.ogg"),
                With(vpunch),
                Return("contre"),
            ]

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                if vote_phase3_hover_side == "contre":
                    at vote_phase3_hover_zoom

                text "VOTER CONTRE":
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 62
                    bold True
                    color "#FFB2B2"
                    outlines [(4, "#FF474788", 0, 0)]

                text "Statu quo maintenu":
                    text_align 0.5
                    xalign 0.5
                    font "fonts/day_font.ttf"
                    size 40
                    color "#FFE7E7"
                    outlines [(2, "#2A0C0C", 0, 0)]

                if vote_phase3_hover_side == "contre":
                    text "✦  ✦  ✦":
                        xalign 0.5
                        font "fonts/day_font.ttf"
                        size 46
                        color "#FF7070"
                        at vote_phase3_float_down

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

    add "images/background/bg_conclave.png" at adaptive_fullscreen
    add Solid("#04070FCC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1560
        ysize 920
        background Solid("#0A1222D8")

    text "DÉPOUILLEMENT DES VOTES":
        xalign 0.5
        yalign 0.11
        font "fonts/day_font.ttf"
        size 62
        color "#E6F4FF"
        outlines [(4, "#65D4FF88", 0, 0)]
        at vote_phase3_title_glow

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

    # Vote joueur (ou timeout => contre par défaut)
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
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    show screen vote_phase3_tally_screen

    # Dépouillement piloté par le script (plus robuste que les timers d'écran
    # selon les plateformes/configurations Ren'Py).
    while not vote_phase3_tally_done:
        $ vote_phase3_tally_step()
        $ renpy.pause(0.55, hard=False)

    $ renpy.pause(1.2, hard=False)

    hide screen vote_phase3_tally_screen

    if vote_phase3_counts["contre"] == 0:
        jump vote_pour
    else:
        jump vote_contre
