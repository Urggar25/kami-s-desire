# Mini-jeu : Débat - Phase 2 (Buzzer / contradictions)

default debat_phase2_buzzed_ids = []
default debat_phase2_rebuttal_log = []
default debat_phase2_vote_summary = {}
default debat_day3_live_vote_stats = {}
default debat_phase2_good = 0
default debat_phase2_wrong = 0
default debat_phase2_missed = 0
default debat_phase2_dialogues_active = []
default debat_phase2_too_many_objections_bad_end = False

define DEBAT_PHASE2_LINE_DURATION = 6.0

define DEBAT_PHASE2_FADE_TIME = 0.35
define DEBAT_PHASE2_REBUTTAL_LINE_DURATION = 5.0

transform debat_phase2_fade_cycle(total=5.0, fade=0.35):
    alpha 0.0
    linear fade alpha 1.0
    pause max(0.0, total - (fade * 2.0))
    linear fade alpha 0.0

transform debat_phase2_buzzer_pulse:
    zoom 1.0
    ease 0.28 zoom 1.05
    ease 0.28 zoom 1.0
    repeat

transform debat_phase2_time_drain(total=6.0):
    xzoom 1.0
    xanchor 0.0
    linear total xzoom 0.0

transform debat_phase2_objection_shock:
    alpha 0.0
    zoom 0.96
    linear 0.16 alpha 1.0
    easeout 0.30 zoom 1.01
    easein 0.10 zoom 0.99
    easeout 0.12 zoom 1.0

transform debat_phase2_scanline:
    yoffset -1080
    linear 7.0 yoffset 1080
    repeat

transform debat_phase2_reject_warning:
    alpha 0.35
    ease 0.35 alpha 0.95
    ease 0.35 alpha 0.35
    repeat

transform debat_phase2_bad_end_fade:
    alpha 0.0
    linear 0.35 alpha 1.0

image dp2_portrait_mara_talk:
    "gui/day3/vote_phase2/portraits/mara_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/mara_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/mara_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/mara_blink.png"
    pause 0.10
    repeat

image dp2_portrait_elias_talk:
    "gui/day3/vote_phase2/portraits/elias_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/elias_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/elias_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/elias_blink.png"
    pause 0.10
    repeat

image dp2_portrait_lysa_talk:
    "gui/day3/vote_phase2/portraits/lysa_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/lysa_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/lysa_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/lysa_blink.png"
    pause 0.10
    repeat

image dp2_portrait_julian_talk:
    "gui/day3/vote_phase2/portraits/julian_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/julian_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/julian_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/julian_blink.png"
    pause 0.10
    repeat

image dp2_portrait_iris_talk:
    "gui/day3/vote_phase2/portraits/iris_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/iris_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/iris_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/iris_blink.png"
    pause 0.10
    repeat

image dp2_portrait_tomas_talk:
    "gui/day3/vote_phase2/portraits/tomas_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/tomas_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/tomas_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/tomas_blink.png"
    pause 0.10
    repeat

image dp2_portrait_elen_talk:
    "gui/day3/vote_phase2/portraits/elen_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/elen_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/elen_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/elen_blink.png"
    pause 0.10
    repeat

image dp2_portrait_kael_talk:
    "gui/day3/vote_phase2/portraits/kael_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/kael_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/kael_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/kael_blink.png"
    pause 0.10
    repeat

image dp2_portrait_nyra_talk:
    "gui/day3/vote_phase2/portraits/nyra_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/nyra_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/nyra_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/nyra_blink.png"
    pause 0.10
    repeat

image dp2_portrait_ryn_talk:
    "gui/day3/vote_phase2/portraits/ryn_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/ryn_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/ryn_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/ryn_blink.png"
    pause 0.10
    repeat

image dp2_portrait_sael_talk:
    "gui/day3/vote_phase2/portraits/sael_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/sael_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/sael_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/sael_blink.png"
    pause 0.10
    repeat

image dp2_portrait_noam_talk:
    "gui/day3/vote_phase2/portraits/noam_idle.png"
    pause 0.42
    "gui/day3/vote_phase2/portraits/noam_talk.png"
    pause 0.16
    "gui/day3/vote_phase2/portraits/noam_idle.png"
    pause 0.32
    "gui/day3/vote_phase2/portraits/noam_blink.png"
    pause 0.10
    repeat

init python:
    DEBAT_PHASE2_DIALOGUES = [
        {"id": "d1", "speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "doute", "counter_label": "debat_phase2_counter_d1", "lines": ["Ah, je dois commencer ?? Euh...", "Abolir la distribution risque de", "condamner les plus fragiles."]},
        {"id": "d2", "speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "determine", "counter_label": "debat_phase2_counter_d2", "lines": ["Le marché libre va", "récompenser ceux", "qui se bougent vraiment."]},
        {"id": "d3", "speaker": "Lysa", "speaker_tag": "lysa", "speaker_expr": "opposition", "counter_label": "debat_phase2_counter_d3", "lines": ["Ceux qui se bougent, oui.", "Mais ceux qui échouent", "on les verra aussi."]},
        {"id": "d4", "speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "taquin", "counter_label": "debat_phase2_counter_d4", "lines": ["L’échec existe déjà.", "Au moins là,", "il aura un sens."]},
        {"id": "d5", "speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "inquiet", "counter_label": "debat_phase2_counter_d5", "lines": ["J’aime pas vraiment ça.", "Mais rester figés,", "j’aime encore moins."]},
        {"id": "d6", "speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "raison", "counter_label": "debat_phase2_counter_d6", "lines": ["Statistiquement…", "ne rien changer", "c’est déjà tout perdre."]},
        {"id": "d7", "speaker": "Elen", "speaker_tag": "elen", "speaker_expr": "joie", "counter_label": "debat_phase2_counter_d7", "lines": ["Alors essayons !", "Moi, j’ai envie de voir", "ce que ça peut donner."]},
        {"id": "d8", "speaker": "Kael", "speaker_tag": "kael", "speaker_expr": "reflechit", "counter_label": "debat_phase2_counter_d8", "lines": ["Un test mal cadré peut", "coûter plus cher que", "ce qu'on connait déjà."]},
        {"id": "d9", "speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "determine", "counter_label": "debat_phase2_counter_d9", "lines": ["Alors cadrons-le.", "Mais ne faisons pas", "semblant d’ignorer le reste."]},
        {"id": "d10", "speaker": "Ryn", "speaker_tag": "ryn", "speaker_expr": "colere", "counter_label": "debat_phase2_counter_d10", "lines": ["Le reste ?!", "Le reste, c’est des vies !", "Pas un foutu paramètre !"]},
        {"id": "d11", "speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "determine", "counter_label": "debat_phase2_counter_d11", "lines": ["Si on veut protéger des vies,", "il faut tout changer.", "Ca commence par ça."]},
        {"id": "d12", "speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "reflexion", "counter_label": "debat_phase2_counter_d12", "lines": ["On doit bouger, oui.", "Mais étape par étape.", "Doucement."]},
        {"id": "d13", "speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "joie", "counter_label": "debat_phase2_counter_d13", "lines": ["Je vous l’avais dit.", "On finit toujours", "par me rejoindre."]},
        {"id": "d14", "speaker": "noam", "speaker_tag": "noam", "speaker_expr": "desaccord", "counter_label": "debat_phase2_counter_d14", "lines": ["Ton besoin d’avoir raison", "n’a rien à voir avec", "notre discussion."]},
        {"id": "d15", "speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "determine", "counter_label": "debat_phase2_counter_d15", "lines": ["Je crois bien que", "nous sommes d’accord.", "Il faut du changement."]},
    ]

    DEBAT_DAY3_BASE_VOTE_STATS = {
        "elias": 7,
        "mara": 1,
        "lysa": 2,
        "julian": 9,
        "iris": 4,
        "tomas": 3,
        "elen": 8,
        "kael": -1,
        "nyra": 3,
        "ryn": -1,
        "sael": 2,
    }

    DEBAT_PHASE2_LINE_X_OFFSETS = [0, 24, -18, 12]

    DEBAT_PHASE2_SPEAKER_META = {
        "mara": "Représentante n°03 — Velkyn",
        "elias": "Représentant n°04 — Solen",
        "lysa": "Représentante n°05 — Orée",
        "julian": "Représentant n°06 — Miren",
        "iris": "Représentante n°08 — Civitas",
        "tomas": "Représentant n°09 — Archive",
        "elen": "Représentante n°10 — Aster",
        "kael": "Représentant n°11 — Forge",
        "nyra": "Représentante n°02 — Apex",
        "ryn": "Représentant n°07 — Limen",
        "sael": "Représentante n°12 — Serment",
        "noam": "Médiateur — District Harmonie",
    }

    def debat_phase2_get_objection_protocol_image(index_number):
        wanted = "images/background/debat/objection_protocol_%d.png" % int(index_number)
        if renpy.loadable(wanted):
            return wanted
        fallback = "images/background/debat/fatal_assembly_%d.png" % int(index_number)
        return fallback

    def debat_phase2_speaker_portrait(tag):
        image_name = "dp2_portrait_%s_talk" % tag
        if renpy.has_image((image_name,)):
            return image_name
        return "dp2_portrait_noam_talk"

    def debat_phase2_speaker_meta(tag):
        return DEBAT_PHASE2_SPEAKER_META.get(tag, "Représentant — Conclave")

    def debat_phase2_join_lines(dialogue_data):
        return "\n".join(kd_tr(line) for line in dialogue_data.get("lines", []))

    def debat_day3_vote_from_stat(stat_value):
        if stat_value > 1:
            return "pour"
        if stat_value < -1:
            return "contre"
        if -1 <= stat_value <= 1:
            return "abstention"
        return "abstention"

    def debat_day3_compute_votes(stats=None):
        source = stats if stats is not None else store.debat_day3_live_vote_stats
        result = {"pour": 0, "abstention": 0, "contre": 0, "details": {}}

        for character, stat_value in source.items():
            vote = debat_day3_vote_from_stat(stat_value)
            result[vote] += 1
            result["details"][character] = vote

        return result

    def debat_day3_reset_live_stats():
        store.debat_day3_live_vote_stats = dict(DEBAT_DAY3_BASE_VOTE_STATS)

    def debat_day3_apply_influence(delta_map):
        for character, delta in delta_map.items():
            current = store.debat_day3_live_vote_stats.get(character, 0)
            store.debat_day3_live_vote_stats[character] = current + delta

    def debat_phase2_is_contestable(dialogue_data):
        label_name = dialogue_data.get("counter_label")
        return bool(label_name) and renpy.has_label(label_name)

    def debat_phase2_total_contestable(dialogues=None):
        source = dialogues if dialogues is not None else store.debat_phase2_dialogues_active
        return len([d for d in source if debat_phase2_is_contestable(d)])

    def debat_phase2_compute_score():
        total = max(1, debat_phase2_total_contestable())
        useful_ratio = store.debat_phase2_good / float(total)
        coherence_penalty = max(0, store.debat_phase2_good - 7) * 90
        base = 780.0 * useful_ratio
        restraint_bonus = 160 if 3 <= store.debat_phase2_good <= 7 else 0
        clean_bonus = 80 if store.debat_phase2_wrong == 0 else 0
        return int(max(0, round(base + restraint_bonus + clean_bonus - coherence_penalty - 80 * store.debat_phase2_wrong)))

    def debat_phase2_contradicted_everyone():
        total = debat_phase2_total_contestable()
        return total > 0 and store.debat_phase2_good >= total

screen debat_phase2_line(dialogue_data):
    modal True
    zorder 120

    on "show" action Function(
        play_dialogue_doublage,
        dialogue_data["speaker_tag"],
        debat_phase2_join_lines(dialogue_data),
    )

    add "bg_conclave" at adaptive_fullscreen
    add Solid("#02060ADC")
    add "gui/day3/vote_phase2/bg_overlay.png":
        alpha 0.22
    add Solid("#00000080", xsize=1920, ysize=1080)
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at debat_phase2_scanline

    $ _dp2_total_lines = max(1, len(debat_phase2_dialogues_active))
    $ _dp2_current_line = min(_dp2_total_lines, debat_phase2_index + 1)
    $ _dp2_portrait = debat_phase2_speaker_portrait(dialogue_data["speaker_tag"])
    $ _dp2_meta = debat_phase2_speaker_meta(dialogue_data["speaker_tag"])
    $ _dp2_speech = debat_phase2_join_lines(dialogue_data)
    $ _dp2_intervention_color = "#FFD166" if debat_phase2_good <= 7 else "#FF5B64"

    for gx in range(56, 1921, 112):
        add Solid("#6B879B0B", xsize=1, ysize=1080):
            xpos gx
            ypos 0
    for gy in range(48, 1081, 96):
        add Solid("#6B879B0B", xsize=1920, ysize=1):
            xpos 0
            ypos gy

    frame:
        xpos 46
        ypos 34
        xsize 1828
        ysize 360
        background Solid("#071018E8")
        padding (0, 0)
        at debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

        fixed:
            add Solid("#8A98A844", xsize=1828, ysize=1):
                xpos 0
                ypos 0
            add Solid("#8A98A833", xsize=1828, ysize=1):
                xpos 0
                ypos 359
            add Solid("#FF4D5C99", xsize=210, ysize=2):
                xpos 210
                ypos 357
            add Solid("#FF4D5C66", xsize=190, ysize=1):
                xpos 1568
                ypos 332

            frame:
                xpos 16
                ypos 14
                xsize 370
                ysize 330
                background Solid("#0B1824F0")
                padding (0, 0)

                add _dp2_portrait:
                    xysize (370, 370)
                    yalign 0.5
                    yoffset (-18 if dialogue_data["speaker_tag"] in ("nyra", "ryn") else 0)
                    alpha 0.88
                add Solid("#00000060", xsize=370, ysize=330)
                add Solid("#6F849A55", xsize=1, ysize=330):
                    xpos 369
                    ypos 0

            vbox:
                xpos 430
                ypos 50
                xsize 1040
                spacing 18

                text "[dialogue_data['speaker']]":
                    size 34
                    color "#FF5B64"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
                    outlines [(1, "#05070A", 0, 0)]

                text kd_tr(_dp2_meta):
                    size 24
                    color "#8C98A4"
                    font "fonts/Barlow-Light.ttf"
                    outlines [(1, "#05070A", 0, 0)]

                text kd_tr(_dp2_speech):
                    size 31
                    color "#F3F6F8"
                    font "fonts/Barlow-Light.ttf"
                    line_spacing 10
                    xmaximum 1040
                    outlines [(1, "#05070A", 0, 0)]

            vbox:
                xpos 1510
                ypos 58
                xsize 250
                spacing 18
                text "KAMI.CORE":
                    size 18
                    color "#70879B"
                    font "fonts/Barlow-Light.ttf"
                    kerning 3
                    xalign 0.5
                text "OBJECTION\nPROTOCOL":
                    size 25
                    color "#C7D4DF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    text_align 0.5
                    xalign 0.5
                    outlines [(1, "#05070A", 0, 0)]
                text "LIGNE [_dp2_current_line]/[_dp2_total_lines]":
                    size 20
                    color "#9AA7B1"
                    xalign 0.5
                    font "fonts/Barlow-Light.ttf"
                text "PRISES DE PAROLE [debat_phase2_good]":
                    size 22
                    color _dp2_intervention_color
                    xalign 0.5
                    font "fonts/Rajdhani-SemiBold.ttf"

    fixed:
        xpos 270
        ypos 450
        xsize 1380
        ysize 92
        at debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

        add Solid("#C9953C66", xsize=500, ysize=1):
            xpos 0
            ypos 32
        add Solid("#C9953C66", xsize=500, ysize=1):
            xpos 880
            ypos 32
        text "VOTRE TOUR":
            xpos 0
            ypos 0
            xsize 1380
            text_align 0.5
            size 28
            color "#FFD166"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(1, "#05070A", 0, 0)]
        text "Cliquez sur le buzzer seulement quand une intervention apporte vraiment quelque chose.":
            xpos 0
            ypos 54
            xsize 1380
            text_align 0.5
            size 24
            color "#F0F2F4"
            font "fonts/Barlow-Light.ttf"
            outlines [(1, "#05070A", 0, 0)]

    frame:
        xpos 1215
        ypos 645
        xsize 426
        ysize 178
        background Solid("#071018DB")
        padding (28, 24)
        at debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

        hbox:
            spacing 18
            text "!":
                size 46
                color "#FF5B64"
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(2, "#05070A", 0, 0)]
            vbox:
                spacing 10
                text "ATTENTION":
                    size 24
                    color "#FF5B64"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
                text "Vous ne pouvez parler\nqu’après avoir appuyé\nsur le buzzer.":
                    size 22
                    color "#C6CED6"
                    font "fonts/Barlow-Light.ttf"
                    line_spacing 4

    fixed:
        xpos 70
        ypos 952
        xsize 1780
        ysize 78

        add Solid("#E6EEF044", xsize=1780, ysize=1):
            xpos 0
            ypos 0
        hbox:
            xpos 575
            ypos 42
            spacing 18
            text "PHASE":
                size 20
                color "#6F7B84"
                font "fonts/Barlow-Light.ttf"
            for pi in range(_dp2_total_lines):
                $ _pip_color = "#FF4D5C" if pi == (debat_phase2_index % _dp2_total_lines) else "#151A20"
                $ _pip_edge = "#FF6C76" if pi == (debat_phase2_index % _dp2_total_lines) else "#59636B"
                fixed:
                    xsize 24
                    ysize 24
                    add Solid(_pip_edge, xsize=24, ysize=24)
                    add Solid(_pip_color, xsize=16, ysize=16):
                        xpos 4
                        ypos 4

    fixed:
        xalign 0.5
        ypos 880
        xsize 760
        ysize 10

        add Solid("#151923", xsize=760, ysize=10)
        add Solid("#FFD166") at debat_phase2_time_drain(DEBAT_PHASE2_LINE_DURATION):
            xpos 0
            xsize 760
            ysize 10

    if debat_phase2_wrong > 0 or debat_phase2_missed > 0:
        hbox:
            xpos 70
            ypos 908
            spacing 18
            if debat_phase2_wrong > 0:
                text "À TORT [debat_phase2_wrong]" size 20 color "#FF5B64" font "fonts/Rajdhani-SemiBold.ttf"
            if debat_phase2_missed > 0:
                text "MANQUÉES [debat_phase2_missed]" size 20 color "#FFD166" font "fonts/Rajdhani-SemiBold.ttf"

    use mk_help_button("tuto_debat_phase2")

    imagebutton:
        idle "gui/day3/vote_phase2/buzzer_round_idle.png"
        hover "gui/day3/vote_phase2/buzzer_round_hover.png"
        xalign 0.5
        yalign 0.71
        xysize (390, 390)
        at debat_phase2_buzzer_pulse
        action [Play("sound", "audio/sfx_kami_alert.wav"), Return({
            "buzzed": True,
            "id": dialogue_data["id"],
            "speaker": dialogue_data["speaker"],
            "counter_label": dialogue_data["counter_label"],
        })]

    timer DEBAT_PHASE2_LINE_DURATION action Return({"buzzed": False, "id": dialogue_data["id"]})

screen debat_phase2_rebuttal_line(entry_data, duration=3.4):
    modal True
    zorder 120

    on "show" action Function(
        play_dialogue_doublage,
        entry_data["speaker_tag"],
        "\n".join(entry_data.get("lines", [])),
    )

    add "bg_conclave" at adaptive_fullscreen
    add Solid("#02060ADC")
    add "gui/day3/vote_phase2/bg_overlay.png":
        alpha 0.24
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at debat_phase2_scanline

    $ _dp2_portrait = debat_phase2_speaker_portrait(entry_data["speaker_tag"])
    $ _dp2_meta = debat_phase2_speaker_meta(entry_data["speaker_tag"])
    $ _dp2_speech = debat_phase2_join_lines(entry_data)
    $ _dp2_rebuttal_name_color = "#FF5B64" if entry_data["speaker_tag"] != "noam" else "#6FE7FF"

    frame:
        xpos 150
        ypos 170
        xsize 1620
        ysize 420
        background Solid("#071018EC")
        padding (0, 0)
        at debat_phase2_fade_cycle(duration, DEBAT_PHASE2_FADE_TIME)

        fixed:
            add Solid("#8A98A844", xsize=1620, ysize=1)
            add Solid("#FF4D5C99", xsize=250, ysize=2):
                xpos 250
                ypos 418

            frame:
                xpos 24
                ypos 24
                xsize 370
                ysize 370
                background Solid("#0B1824F0")
                padding (0, 0)
                add _dp2_portrait:
                    xysize (370, 370)
                    yoffset (-18 if entry_data["speaker_tag"] in ("nyra", "ryn") else 0)
                    alpha 0.90
                add Solid("#00000044", xsize=370, ysize=370)

            vbox:
                xpos 440
                ypos 62
                xsize 1000
                spacing 20

                text "[entry_data['speaker']]":
                    size 36
                    color _dp2_rebuttal_name_color
                    font "fonts/Rajdhani-SemiBold.ttf"
                    bold True
                    outlines [(1, "#05070A", 0, 0)]

                text kd_tr(_dp2_meta):
                    size 24
                    color "#8C98A4"
                    font "fonts/Barlow-Light.ttf"

                text kd_tr(_dp2_speech):
                    size 34
                    color "#F3F6F8"
                    font "fonts/Barlow-Light.ttf"
                    line_spacing 10
                    xmaximum 1000
                    outlines [(1, "#05070A", 0, 0)]

    timer duration action Return(True)

screen debat_phase2_objection_flash():
    modal True
    zorder 240

    add "images/background/debat/noam_objection.png" at adaptive_fullscreen, debat_phase2_objection_shock
    add "gui/day3/vote_phase2/objection_flash_overlay.png" at debat_phase2_objection_shock
    on "show" action Play("sound", "audio/sfx_announce.mp3")
    timer 1.9 action Return(True)

style debat_phase2_speaker_text:
    color "#FFFFFF"
    font "fonts/day_font.ttf"
    size 52
    outlines [(3, "#000000B5", 0, 0)]

style debat_phase2_line_text:
    color "#FFFFFF"
    font "fonts/day_font.ttf"
    size 62
    outlines [(4, "#0E1028E0", 0, 0)]

style debat_phase2_buzzer_button is default:
    font "fonts/day_font.ttf"
    size 42
    color "#FFFFFF"
    hover_color "#FFE7A8"
    outlines [(2, "#000000", 0, 0)]

label DEBAT_PHASE2_START_ANIM:
    $ renpy.block_rollback()

    scene black

    $ op1 = debat_phase2_get_objection_protocol_image(1)
    $ op2 = debat_phase2_get_objection_protocol_image(2)

    show expression op1 as op_bg at adaptive_fullscreen, debat_phase2_objection_shock
    play sound "audio/sfx_minigame_start.mp3"
    pause 2.50

    show expression op2 as op_fx at adaptive_fullscreen, debat_phase2_objection_shock
    pause 2.50

    hide op_fx
    hide op_bg

    return

label debat_phase2_play_rebuttal_sequence(sequence_data):
    python:
        for entry in sequence_data:
            renpy.call_screen("debat_phase2_rebuttal_line", entry_data=entry, duration=DEBAT_PHASE2_REBUTTAL_LINE_DURATION)
    return

# ------------------------------------------------------------
# TUTORIEL ANIMÉ — démo du buzzer
# ------------------------------------------------------------
transform dp2_demo_time_drain_loop:
    xzoom 1.0
    xanchor 0.0
    block:
        linear 2.6 xzoom 0.0
        pause 0.6
        xzoom 1.0
        repeat

transform dp2_demo_cursor_to_buzzer:
    xpos 540 ypos 150 alpha 0.0
    block:
        easein 0.3 alpha 1.0
        pause 0.5
        easeout 0.8 xpos 360 ypos 330
        easeout 0.10 zoom 0.8
        easein 0.10 zoom 1.0
        pause 0.3
        linear 0.25 alpha 0.0
        pause 0.85
        repeat

transform dp2_demo_objection_pop:
    alpha 0.0
    block:
        pause 1.8
        easeout 0.15 alpha 1.0 zoom 1.25
        easein 0.15 zoom 1.0
        pause 0.6
        linear 0.2 alpha 0.0
        pause 0.3
        repeat

screen tuto_debat_phase2(as_overlay=False):
    use mk_tuto_chrome("PROTOCOLE D'OBJECTION", [
        ("Ecoute chaque argument", "Chaque participant parle quelques secondes. La barre jaune indique le temps disponible."),
        ("Interviens avec discernement", "Le buzzer sert a prendre la parole quand Noam apporte un vrai eclairage, pas a contredire tout le monde."),
        ("Reste coherent", "Multiplier les objections affaiblit Noam : l'assemblee juge aussi la coherence de tes interventions."),
    ], "tuto_debat_phase2", as_overlay):

        fixed:
            xfill True
            yfill True

            # Panneau de dialogue factice
            frame:
                xpos 60
                ypos 60
                xsize 620
                ysize 130
                background Solid("#0A1622DD")
                vbox:
                    align (0.5, 0.5)
                    spacing 4
                    text "« Abolir la distribution risque de" size 22 color "#FFFFFF" xalign 0.5
                    text "condamner les plus fragiles. »" size 22 color "#FFFFFF" xalign 0.5

            # Barre de temps qui se vide en boucle
            fixed:
                xpos 60
                ypos 220
                xsize 620
                ysize 12
                add Solid("#0A1326CC", xsize=620, ysize=12)
                add Solid("#FFD166", xsize=620, ysize=12) at dp2_demo_time_drain_loop

            # Buzzer
            frame:
                xpos 360
                ypos 330
                xanchor 0.5
                yanchor 0.5
                xsize 150
                ysize 150
                background Solid("#5C1020")
                text "BUZZ" align (0.5, 0.5) size 30 color "#FFFFFF" bold True

            # Faux curseur
            fixed at dp2_demo_cursor_to_buzzer:
                xanchor 0.5
                yanchor 0.5
                xsize 34
                ysize 34
                add Solid("#FFFFFF55") size (34, 34) align (0.5, 0.5)
                add Solid("#FFFFFFEE") size (12, 12) align (0.5, 0.5)

            text "OBJECTION !" at dp2_demo_objection_pop:
                xpos 360
                ypos 440
                xanchor 0.5
                size 36
                color "#FF4D6D"
                bold True
                outlines [(3, "#02040A", 0, 0)]

# Mauvaise objection (ligne non contestable)
screen debat_phase2_bad_objection():
    modal True
    zorder 240

    add Solid("#1A0408B0")
    add Solid("#FF4D6D33", ysize=5) ypos 170 at debat_phase2_reject_warning
    add Solid("#FF4D6D33", ysize=5) ypos 820 at debat_phase2_reject_warning
    add Solid("#FFFFFF08", xsize=1920, ysize=22) at debat_phase2_scanline

    vbox:
        align (0.5, 0.45)
        spacing 14
        text "OBJECTION REJETÉE" at debat_phase2_objection_shock:
            xalign 0.5
            size 72
            color "#FF4D6D"
            bold True
            outlines [(4, "#02040A", 0, 0)]
        text "Cet argument tenait debout. L'assemblée murmure...":
            xalign 0.5
            size 26
            color "#DCF0FF"

    on "show" action Play("sound", "audio/sfx_drop.mp3")
    timer 1.6 action Return(True)

screen debat_phase2_incoherence_gameover():
    modal True
    zorder 260

    add Solid("#020308F2")
    add Solid("#FF4D5C22") at debat_phase2_bad_end_fade

    vbox:
        align (0.5, 0.45)
        spacing 18
        text "GAME OVER":
            xalign 0.5
            size 86
            color "#FF5B64"
            font "fonts/Rajdhani-SemiBold.ttf"
            outlines [(4, "#05070A", 0, 0)]
        text "Noam a perdu toute credibilite devant le Conclave.":
            xalign 0.5
            size 28
            color "#DCE6EF"
            font "fonts/Barlow-Light.ttf"
        text "Cliquez pour reprendre juste avant le Protocole d'Objection.":
            xalign 0.5
            size 22
            color "#8C98A4"
            font "fonts/Barlow-Light.ttf"

    key "dismiss" action Return(True)
    button:
        xfill True
        yfill True
        background None
        action Return(True)

# ------------------------------------------------------------
# MINIJEU — réutilisable : debat_phase2_session est paramétrable
#   $ debat_phase2_dialogues_active = MA_LISTE  (avant l'appel)
#   call debat_phase2_minigame
# ------------------------------------------------------------
label debat_phase2_minigame:
    $ debat_phase2_buzzed_ids = []
    $ debat_phase2_rebuttal_log = []
    $ debat_phase2_good = 0
    $ debat_phase2_wrong = 0
    $ debat_phase2_missed = 0
    if not debat_phase2_dialogues_active:
        $ debat_phase2_dialogues_active = list(DEBAT_PHASE2_DIALOGUES)
    $ debat_day3_reset_live_stats()
    $ debat_phase2_index = 0

    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    call DEBAT_PHASE2_START_ANIM from _call_DEBAT_PHASE2_START_ANIM
    call mk_tutorial("debat_phase2", "tuto_debat_phase2") from _call_mk_tutorial_1

label debat_phase2_loop:
    if debat_phase2_index >= len(debat_phase2_dialogues_active):
        jump debat_phase2_finish

    $ debat_phase2_current_dialogue = debat_phase2_dialogues_active[debat_phase2_index]
    $ debat_phase2_current_outcome = renpy.call_screen("debat_phase2_line", dialogue_data=debat_phase2_current_dialogue)

    if debat_phase2_current_outcome and debat_phase2_current_outcome.get("buzzed"):
        $ counter_label = debat_phase2_current_outcome.get("counter_label")

        if not debat_phase2_is_contestable(debat_phase2_current_dialogue):
            # Objection à tort : pénalité, pas de crash
            $ debat_phase2_wrong += 1
            call screen debat_phase2_bad_objection
            jump debat_phase2_resume

        $ debat_phase2_good += 1
        $ debat_phase2_buzzed_ids.append(debat_phase2_current_outcome.get("id"))
        $ debat_phase2_rebuttal_log.append({
            "id": debat_phase2_current_outcome.get("id"),
            "speaker": debat_phase2_current_outcome.get("speaker"),
            "counter_label": counter_label,
        })
        call screen debat_phase2_objection_flash
        jump expression counter_label

    if debat_phase2_is_contestable(debat_phase2_current_dialogue):
        $ debat_phase2_missed += 1

    $ debat_phase2_index += 1
    jump debat_phase2_loop

label debat_phase2_resume:
    $ debat_phase2_index += 1
    jump debat_phase2_loop

label debat_phase2_finish:
    if debat_phase2_contradicted_everyone():
        jump debat_phase2_bad_ending_tout_et_rien_dire

    $ debat_phase2_vote_summary = debat_day3_compute_votes(store.debat_day3_live_vote_stats)

    # Résultats avec rang
    python:
        dp2_score = debat_phase2_compute_score()
        dp2_total = debat_phase2_total_contestable()
        dp2_challenges = [
            ("Aucune objection a tort", debat_phase2_wrong == 0),
            ("Interventions coherentes", debat_phase2_good <= 7),
            ("Impact politique positif", debat_phase2_vote_summary["pour"] >= 8),
        ]
        dp2_score = min(1000, dp2_score + 40 * len([1 for c in dp2_challenges if c[1]]))

    call mk_show_results(
        "PROTOCOLE D'OBJECTION",
        dp2_score,
        1000,
        stats=[
            ("Prises de parole", str(debat_phase2_good)),
            ("Objections a tort", str(debat_phase2_wrong)),
            ("Lignes laissees respirer", str(max(0, dp2_total - debat_phase2_good))),
        ],
        challenges=dp2_challenges,
        mg_id="debat_phase2",
    ) from _call_mk_show_results_1

    $ debat_phase2_dialogues_active = []

    "Résultat provisoire du vote : [debat_phase2_vote_summary['pour']] pour, [debat_phase2_vote_summary['abstention']] abstention, [debat_phase2_vote_summary['contre']] contre."

    return

# --- Contre-arguments dédiés (1 label par réplique contredite) ---

label debat_phase2_bad_ending_tout_et_rien_dire:
    $ unlock_succes("succes004")
    $ debat_phase2_dialogues_active = []
    stop music fadeout 0.8

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR
    scene bg_conclave at adaptive_fullscreen with dissolve
    play sound "audio/sfx_kami_alert.wav"

    "Le dernier buzzer retombe."
    "Cette fois, personne ne reprend tout de suite."

    mara colere "Non. Stop."
    ryn colere "Tu viens de contredire tout le monde."
    nyra colere "A chaque phrase, tu changes d'angle. A chaque reponse, tu defends l'inverse."
    tomas peur "Ce n'est plus une mediation. C'est du bruit."
    sael colere "Tu dis tout et son contraire, Noam."
    lysa colere "Et tu nous demandes encore de te suivre ?"

    noam inquiet "J'essayais juste de faire avancer le debat."

    iris inquiet "Non. La, tu attises les tensions."
    kael colere "Tu n'es plus coherent."
    elias colere "Tu cherches seulement a gagner contre chaque personne qui parle."
    julian inquiet "Meme moi, je trouve ca dangereux. C'est dire."

    ryn colere "Dehors."
    nyra colere "Avant que tu fasses exploser le vote pour de bon."

    "Les chaises raclent le sol."
    "Les regards se ferment un a un."
    "Noam recule, chasse du centre de la salle par l'assemblee qu'il devait tenir ensemble."

    call screen debat_phase2_incoherence_gameover
    jump day3_before_objection_protocol_minigame

label debat_phase2_counter_d1:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Mara, attends. On ne parle pas",
            "de tout couper. On parle de",
            "changer comment ça marche."
        ]},

        {"speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "doute",
        "lines": [
            "Changer, oui, d’accord.",
            "Mais comment on fait si ça dérape ?",
            "C’est pas toi qui assumera."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Si. Bien au contraire",
            "On en assumera tous les conséquences.",
            "C’est justement pour ça qu’on en parle."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence
    $ debat_day3_apply_influence({"mara": -1, "iris": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d2:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Attends.",
            "On parle quand même de réintroduire",
            "de l’argent dans un système fermé."
        ]},

        {"speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "determine",
        "lines": [
            "Justement, cette proposition.",
            "est plus importante, elle réintroduit,",
            "l'argent et le fait d’obtenir ce qu'on veut."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison",
        "lines": [
            "Donc certains auront plus.",
            "Et d’autres moins.",
            "On accepte ça ?"
        ]},

        {"speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "reflexion",
        "lines": [
            "Parce que si on accepte ça,",
            "on accepte aussi le retour à ce qu'on",
            "connaissait avant, la liberté."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_1
    $ debat_day3_apply_influence({"elias": 1, "nyra": 1, "lysa": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d3:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Les voir, ça ne veut pas dire",
            "les abandonner.",
            "On peut prévoir des garde-fous."
        ]},

        {"speaker": "Ryn", "speaker_tag": "ryn", "speaker_expr": "colere",
        "lines": [
            "Des garde-fous ?",
            "A Limen, c'est TRES CLAIR !",
            "Ce sera une hécatombe."
        ]},

        {"speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "raison",
        "lines": [
            "Non. Pas partout.",
            "En dehors des trois grandes villes,",
            "on sait encore vivre autrement."
        ]},

        {"speaker": "Lysa", "speaker_tag": "lysa", "speaker_expr": "reflexion",
        "lines": [
            "Tout le monde ne reçoit pas de bons.",
            "Mais la majorité est en ville.",
            "Eux, ils feront comment ?"
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_2
    $ debat_day3_apply_influence({"ryn": -1, "sael": 1, "lysa": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d4:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "colere",
        "lines": [
            "Un sens ? Mais de quoi tu parles ?!",
            "Tu parles de gens qui risquent,",
            "de mourir ! Pas d’un foutu concept."
        ]},

        {"speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "hesitation",
        "lines": [
            "Je ne romantise rien.",
            "Je dis juste que stagner",
            "ne sauvera jamais personne."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Alors arrête de parler",
            "comme si l’échec était utile.",
            "Pour certains, il sera définitif."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_3
    $ debat_day3_apply_influence({"tomas": 1, "lysa": 1, "nyra": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d5:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Je comprends. MAIS...",
            "bouger juste pour bouger,",
            "c’est pas une solution."
        ]},

        {"speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "inquiet",
        "lines": [
            "Alors on fait quoi ?",
            "On attend encore trois ans,",
            "et on appelle ça de la prudence ?"
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison",
        "lines": [
            "Non. Ce n'est pas une solution non plus ...",
            "Il faut que ça change mais...",
            "Il faut être sûrs de ce qu'on fait."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_4
    $ debat_day3_apply_influence({"iris": -1, "mara": -1})
    jump debat_phase2_resume

label debat_phase2_counter_d6:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Statistiquement, d’accord.",
            "Mais tu simplifies beaucoup.",
            "C’est pas si binaire."
        ]},

        {"speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "hesitation",
        "lines": [
            "Je…",
            "Les tendances montrent quand même",
            "une perte progressive."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison",
        "lines": [
            "Une tendance n’est pas un verdict.",
            "On peut corriger.",
            "Sans provoquer une rupture."
        ]},

        {"speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "panne",
        "lines": [
            "Oui… peut-être.",
            "Je voulais juste dire que",
            "le statu quo nous fragilise."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_5
    $ debat_day3_apply_influence({"tomas": -2})
    jump debat_phase2_resume

label debat_phase2_counter_d7:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Ce n’est pas un jeu, Elen.",
            "On ne “voit pas ce que ça donne”.",
            "On risque clairement des vies."
        ]},

        {"speaker": "Elen", "speaker_tag": "elen", "speaker_expr": "joie",
        "lines": [
            "Mais si on ne teste jamais,",
            "on ne saura jamais !",
            "Ça peut marcher, non ?"
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Essayer pour essayer",
            "ce n’est pas une stratégie.",
            "Il nous faut un cadre clair."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_6
    $ debat_day3_apply_influence({"elen": -2})
    jump debat_phase2_resume

label debat_phase2_counter_d8:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Et rester comme ça",
            "n’a aucun coût ?",
            "On fait comme si tout allait bien ?"
        ]},

        {"speaker": "Kael", "speaker_tag": "kael", "speaker_expr": "reflechit",
        "lines": [
            "Non. Mais on sait au moins",
            "ce que ça produit.",
            "Et ce qu'on peut faire ou non."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "On sait que ça fige tout.",
            "Que personne ne peut avancer.",
            "Ça aussi, c’est un risque."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_7
    $ debat_day3_apply_influence({"kael": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d9:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "On ne peut pas le cadrer.",
            "Ce vote est binaire, soit",
            "c'est oui, soit c'est non..."
        ]},

        {"speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "reflexion",
        "lines": [
            "Alors il faut au moins",
            "accepter ce que ça implique.",
            "Sans être naïfs."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_8
    $ debat_day3_apply_influence({"nyra": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d10:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Je parle de vies aussi.",
            "Celles qui étouffent déjà.",
            "Et qu’on ne voit plus."
        ]},

        {"speaker": "Ryn", "speaker_tag": "ryn", "speaker_expr": "colere",
        "lines": [
            "À Limen, on les voit.",
            "Tous les jours.",
            "On en enterre déjà assez."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison",
        "lines": [
            "Justement.",
            "Si on ne change rien,",
            "ça continuera pareil."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_9
    $ debat_day3_apply_influence({"ryn": 2})
    jump debat_phase2_resume

label debat_phase2_counter_d11:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Tout changer, d’accord.",
            "Mais pas n’importe comment.",
            "Pas d’un coup."
        ]},

        {"speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "reflechit",
        "lines": [
            "Chaque retard",
            "coûte aussi des vies.",
            "L’inaction protège qui ?"
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Changer, oui. Mais",
            "sans créer une fracture",
            "qu’on ne pourra pas contenir."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_10
    $ debat_day3_apply_influence({"sael": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d12:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Le problème c'est qu'on a",
            "pas le choix. On doit voter.",
            "Et assumer ensemble ce choix."
        ]},

        {"speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "doute",
        "lines": [
            "Et si ça déraille ?",
            "On ne pourra pas revenir",
            "en arrière."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "On peut ne rien changer.",
            "c’est déjà un choix.",
            "Mais ça a aussi un coût."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_11
    $ debat_day3_apply_influence({"mara": -1})
    jump debat_phase2_resume

label debat_phase2_counter_d13:

    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "desaccord",
        "lines": [
            "Ce n’est pas une victoire.",
            "On ne te rejoint pas.",
            "On hésite encore."
        ]},

        {"speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "surpris",
        "lines": [
            "Je plaisantais.",
            "On avance quand même.",
            "C’est déjà ça."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Alors reste concentré.",
            "Ce n’est pas ton moment.",
            "C’est une décision lourde."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq) from _call_debat_phase2_play_rebuttal_sequence_12
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    jump debat_phase2_resume
