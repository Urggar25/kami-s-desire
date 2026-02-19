# Mini-jeu : Débat - Phase 2 (Buzzer / contradictions)

default debat_phase2_buzzed_ids = []
default debat_phase2_rebuttal_log = []
default debat_phase2_vote_summary = {}
default debat_day3_live_vote_stats = {}
default debat_phase2_index = 0
default debat_phase2_current_dialogue = None
default debat_phase2_current_outcome = None

define DEBAT_PHASE2_LINE_DURATION = 5.0
define DEBAT_PHASE2_REBUTTAL_LINE_DURATION = 3.4
define DEBAT_PHASE2_FADE_TIME = 0.35

image kami_debat_background = "images/background/bg_conclave.png"

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

transform debat_phase2_objection_shock:
    alpha 0.0
    zoom 0.96
    linear 0.16 alpha 1.0
    easeout 0.30 zoom 1.01
    easein 0.10 zoom 0.99
    easeout 0.12 zoom 1.0

init python:
    DEBAT_PHASE2_DIALOGUES = [
        {"id": "d1", "speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d1", "lines": ["Abolir la distribution,", "c'est condamner", "les plus fragiles."]},
        {"id": "d2", "speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d2", "lines": ["Le marché libre va", "récompenser ceux", "qui se bougent."]},
        {"id": "d3", "speaker": "Lysa", "speaker_tag": "lysa", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d3", "lines": ["Vous confondez", "liberté économique", "et abandon collectif."]},
        {"id": "d4", "speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d4", "lines": ["Le système est lent,", "opaque...", "et tue l'initiative."]},
        {"id": "d5", "speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d5", "lines": ["Si les prix flambent,", "certains ne", "mangeront plus."]},
        {"id": "d6", "speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d6", "lines": ["On n'a même pas", "simulé l'impact", "logistique."]},
        {"id": "d7", "speaker": "Elen", "speaker_tag": "elen", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d7", "lines": ["Sans concurrence,", "la qualité stagne", "pour tout le monde."]},
        {"id": "d8", "speaker": "Kael", "speaker_tag": "kael", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d8", "lines": ["On va créer", "un marché noir", "impossible à contrôler."]},
        {"id": "d9", "speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d9", "lines": ["Le vrai sujet...", "qui contrôle", "les stocks critiques ?"]},
        {"id": "d10", "speaker": "Ryn", "speaker_tag": "ryn", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d10", "lines": ["Ce texte ressemble", "à un pari", "fait avec nos vies."]},
        {"id": "d11", "speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d11", "lines": ["Sans clauses de secours,", "je ne vote jamais", "un texte pareil."]},
        {"id": "d12", "speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d12", "lines": ["Ceux qui défendent ça", "n'ont jamais connu", "la vraie pénurie."]},
        {"id": "d13", "speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d13", "lines": ["Si on refuse", "tout risque,", "on restera bloqués."]},
        {"id": "d14", "speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d14", "lines": ["Ce débat n'a de sens", "que si chacun", "peut manger demain."]},
        {"id": "d15", "speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "neutre", "counter_label": "debat_phase2_counter_d15", "lines": ["On tranche ce soir,", "sinon on n'avancera", "jamais."]},
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

    def debat_phase2_get_objection_protocol_image(index_number):
        wanted = "images/background/debat/objection_protocol_%d.png" % int(index_number)
        if renpy.loadable(wanted):
            return wanted
        fallback = "images/background/debat/fatal_assembly_%d.png" % int(index_number)
        return fallback

    def debat_day3_vote_from_stat(stat_value):
        if stat_value > 0:
            return "pour"
        if stat_value == 0:
            return "abstention"
        return "contre"

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

screen debat_phase2_line(dialogue_data):
    modal True
    zorder 120

    add "kami_debat_background" at adaptive_fullscreen

    frame:
        background Solid("#05091765")
        xfill True
        yfill True

    add "[dialogue_data['speaker_tag']] [dialogue_data['speaker_expr']]" at Position(xalign=0.18, yalign=1.0), debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

    vbox:
        xalign 0.73
        yalign 0.45
        spacing 6
        at debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

        for idx, line_text in enumerate(dialogue_data["lines"]):
            $ local_xoffset = DEBAT_PHASE2_LINE_X_OFFSETS[idx % len(DEBAT_PHASE2_LINE_X_OFFSETS)]
            text "[line_text]":
                style "debat_phase2_line_text"
                xoffset local_xoffset

    text "[dialogue_data['speaker']]":
        style "debat_phase2_speaker_text"
        xalign 0.58
        yalign 0.22
        at debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

    frame:
        background Solid("#8d1212dd")
        xalign 0.5
        yalign 0.92
        xsize 390
        ysize 96

        textbutton "BUZZER" style "debat_phase2_buzzer_button":
            xalign 0.5
            yalign 0.5
            at debat_phase2_buzzer_pulse
            action Return({
                "buzzed": True,
                "id": dialogue_data["id"],
                "speaker": dialogue_data["speaker"],
                "counter_label": dialogue_data["counter_label"],
            })

    timer DEBAT_PHASE2_LINE_DURATION action Return({"buzzed": False, "id": dialogue_data["id"]})

screen debat_phase2_rebuttal_line(entry_data, duration=3.4):
    modal True
    zorder 120

    add "kami_debat_background" at adaptive_fullscreen

    frame:
        background Solid("#05091765")
        xfill True
        yfill True

    add "[entry_data['speaker_tag']] [entry_data['speaker_expr']]" at Position(xalign=0.18, yalign=1.0), debat_phase2_fade_cycle(duration, DEBAT_PHASE2_FADE_TIME)

    vbox:
        xalign 0.73
        yalign 0.45
        spacing 6
        at debat_phase2_fade_cycle(duration, DEBAT_PHASE2_FADE_TIME)

        for idx, line_text in enumerate(entry_data["lines"]):
            $ local_xoffset = DEBAT_PHASE2_LINE_X_OFFSETS[idx % len(DEBAT_PHASE2_LINE_X_OFFSETS)]
            text "[line_text]":
                style "debat_phase2_line_text"
                xoffset local_xoffset

    text "[entry_data['speaker']]":
        style "debat_phase2_speaker_text"
        xalign 0.58
        yalign 0.22
        at debat_phase2_fade_cycle(duration, DEBAT_PHASE2_FADE_TIME)

    timer duration action Return(True)

screen debat_phase2_objection_flash():
    modal True
    zorder 240

    add "images/background/debat/noam_objection.png" at adaptive_fullscreen, debat_phase2_objection_shock
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

label debat_phase2_minigame:
    $ debat_phase2_buzzed_ids = []
    $ debat_phase2_rebuttal_log = []
    $ debat_day3_reset_live_stats()
    $ debat_phase2_index = 0

    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    call DEBAT_PHASE2_START_ANIM

label debat_phase2_loop:
    if debat_phase2_index >= len(DEBAT_PHASE2_DIALOGUES):
        jump debat_phase2_finish

    $ debat_phase2_current_dialogue = DEBAT_PHASE2_DIALOGUES[debat_phase2_index]
    $ debat_phase2_current_outcome = renpy.call_screen("debat_phase2_line", dialogue_data=debat_phase2_current_dialogue)

    if debat_phase2_current_outcome and debat_phase2_current_outcome.get("buzzed"):
        $ counter_label = debat_phase2_current_outcome.get("counter_label")
        $ debat_phase2_buzzed_ids.append(debat_phase2_current_outcome.get("id"))
        $ debat_phase2_rebuttal_log.append({
            "id": debat_phase2_current_outcome.get("id"),
            "speaker": debat_phase2_current_outcome.get("speaker"),
            "counter_label": counter_label,
        })
        call screen debat_phase2_objection_flash
        if counter_label:
            jump expression counter_label
        jump debat_phase2_resume

    $ debat_phase2_index += 1
    jump debat_phase2_loop

label debat_phase2_resume:
    $ debat_phase2_index += 1
    jump debat_phase2_loop

label debat_phase2_finish:
    $ debat_phase2_vote_summary = debat_day3_compute_votes(store.debat_day3_live_vote_stats)

    "Résultat provisoire du vote : [debat_phase2_vote_summary['pour']] pour, [debat_phase2_vote_summary['abstention']] abstention, [debat_phase2_vote_summary['contre']] contre."

    return

# --- Contre-arguments dédiés (1 label par réplique contredite) ---

label debat_phase2_counter_d1:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["Mara, supprimer le filet", "d'un coup, c'est", "trop risqué."]},
        {"speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "raison", "lines": ["On peut encadrer", "sans abandonner", "les plus fragiles."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"mara": -1, "nyra": 1, "iris": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d2:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["L'effort doit être", "récompensé, mais", "pas les abus."]},
        {"speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "reflexion", "lines": ["Si c'est régulé", "intelligemment...", "je peux l'entendre."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"elias": -1, "sael": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d3:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["Liberté, oui.", "Abandon", "non."]},
        {"speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "mefiant", "lines": ["On garde un socle", "commun sinon", "le vote explose."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"lysa": 1, "sael": 1, "julian": -1})
    jump debat_phase2_resume

label debat_phase2_counter_d4:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["Corriger un système", "et le détruire,", "c'est différent."]},
        {"speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "reflechit", "lines": ["Un audit en amont", "évite un", "chaos total."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d5:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["On peut verrouiller", "les prix des", "denrées vitales."]},
        {"speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "neutre", "lines": ["Si ce verrou est", "réel, j'écoute", "la suite."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"iris": 1, "elen": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d6:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["On lance une phase", "pilote, pas", "une bascule brutale."]},
        {"speaker": "Tomas", "speaker_tag": "tomas", "speaker_expr": "reflechit", "lines": ["Avec ça,", "on peut tester", "proprement."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"tomas": 1, "kael": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d7:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["Concurrence oui,", "mais dans", "un cadre clair."]},
        {"speaker": "Elen", "speaker_tag": "elen", "speaker_expr": "joie", "lines": ["Si la sécurité", "reste minimale,", "ça me va."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"elen": 1, "mara": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d8:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["Un marché légal", "traçable réduit", "le noir."]},
        {"speaker": "Kael", "speaker_tag": "kael", "speaker_expr": "reflexion", "lines": ["Si c'est vérifiable,", "alors c'est", "défendable."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"kael": 2, "nyra": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d9:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["Contrôle tournant", "et audits publics,", "pas de confiscation."]},
        {"speaker": "Nyra", "speaker_tag": "nyra", "speaker_expr": "raison", "lines": ["Dans ce cadre,", "c'est", "plus stable."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"nyra": 1, "iris": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d10:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["On découpe", "en étapes", "mesurables."]},
        {"speaker": "Ryn", "speaker_tag": "ryn", "speaker_expr": "determine", "lines": ["Si elles sont", "réversibles,", "je peux suivre."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"ryn": 2, "mara": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d11:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["On ajoute", "des clauses", "de secours."]},
        {"speaker": "Sael", "speaker_tag": "sael", "speaker_expr": "mefiant", "lines": ["Là, c'est", "un texte qui", "survit au réel."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"sael": 1, "julian": -1})
    jump debat_phase2_resume

label debat_phase2_counter_d12:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["La pénurie doit", "servir à calibrer,", "pas tout bloquer."]},
        {"speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "reflexion", "lines": ["Je veux des", "garanties", "écrites."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"mara": -1, "lysa": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d13:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["Le risque n'est", "acceptable qu'avec", "des seuils clairs."]},
        {"speaker": "Julian", "speaker_tag": "julian", "speaker_expr": "reflexion", "lines": ["OK, si ces seuils", "sont gravés", "dans l'amendement."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d14:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "raison", "lines": ["Critère numéro un :", "tout le monde", "mange demain."]},
        {"speaker": "Iris", "speaker_tag": "iris", "speaker_expr": "neutre", "lines": ["Dans ce cas,", "je défends", "cette version."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"iris": 1, "ryn": 1})
    jump debat_phase2_resume

label debat_phase2_counter_d15:
    $ seq = [
        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine", "lines": ["Décider vite", "ne vaut rien", "si c'est intenable."]},
        {"speaker": "Elias", "speaker_tag": "elias", "speaker_expr": "reflexion", "lines": ["On tranche alors", "sur une version", "sécurisée."]},
    ]
    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"elias": -1, "elen": 1, "sael": 1})
    jump debat_phase2_resume
