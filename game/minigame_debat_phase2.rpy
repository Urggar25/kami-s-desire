# Mini-jeu : Débat - Phase 2 (Buzzer / contradictions)

default debat_phase2_buzzed_ids = []
default debat_phase2_rebuttal_log = []
default debat_phase2_vote_summary = {}
default debat_day3_live_vote_stats = {}

define DEBAT_PHASE2_LINE_DURATION = 5.0

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

init python:
    import random

    # Chaque entrée est indépendante : simple à ajouter/supprimer/reclasser.
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

    # Personnage parlant à gauche (fade in / fade out)
    add "[dialogue_data['speaker_tag']] [dialogue_data['speaker_expr']]" at Position(xalign=0.18, yalign=1.0), debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

    # Texte à droite, en plusieurs lignes avec léger décalage non-aligné
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

    # Buzzer au premier plan
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

label debat_phase2_minigame:
    $ debat_phase2_buzzed_ids = []
    $ debat_phase2_rebuttal_log = []
    $ debat_day3_reset_live_stats()

    scene kami_debat_background at adaptive_fullscreen with dissolve

    "Mini-jeu : buzze pour lancer une contradiction et influencer le vote."

    python:
        for dialogue_data in DEBAT_PHASE2_DIALOGUES:
            outcome = renpy.call_screen("debat_phase2_line", dialogue_data=dialogue_data)
            if outcome and outcome.get("buzzed"):
                counter_label = outcome.get("counter_label")
                store.debat_phase2_buzzed_ids.append(outcome.get("id"))
                store.debat_phase2_rebuttal_log.append({
                    "id": outcome.get("id"),
                    "speaker": outcome.get("speaker"),
                    "counter_label": counter_label,
                })
                if counter_label:
                    renpy.call(counter_label)

    $ debat_phase2_vote_summary = debat_day3_compute_votes(store.debat_day3_live_vote_stats)

    "Résultat provisoire du vote : [debat_phase2_vote_summary['pour']] pour, [debat_phase2_vote_summary['abstention']] abstention, [debat_phase2_vote_summary['contre']] contre."

    return

# --- Contre-arguments dédiés (1 label par réplique contredite) ---

label debat_phase2_counter_d1:
    noam "Mara, supprimer le filet d'un coup est trop risqué."
    nyra "Je suis d'accord, on peut encadrer sans abandonner les plus fragiles."
    $ debat_day3_apply_influence({"mara": -1, "nyra": 1, "iris": 1})
    return

label debat_phase2_counter_d2:
    noam "Elias, l'effort doit être récompensé, mais pas au prix d'abus incontrôlés."
    elias "...Si c'est régulé intelligemment, je peux l'entendre."
    $ debat_day3_apply_influence({"elias": -1, "sael": 1})
    return

label debat_phase2_counter_d3:
    noam "Lysa a raison : liberté oui, abandon non."
    sael "On garde un socle commun, sinon ce vote explose."
    $ debat_day3_apply_influence({"lysa": 1, "sael": 1, "julian": -1})
    return

label debat_phase2_counter_d4:
    noam "Julian, corriger un système et le détruire, c'est pas pareil."
    tomas "Un audit en amont éviterait un chaos total."
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    return

label debat_phase2_counter_d5:
    noam "Iris, on peut verrouiller les prix des denrées vitales."
    iris "Si ce verrou est réel, j'accepte d'écouter la suite."
    $ debat_day3_apply_influence({"iris": 1, "elen": 1})
    return

label debat_phase2_counter_d6:
    noam "Tomas, on lance une phase pilote courte, pas une bascule brutale."
    tomas "Avec ça... oui, on peut tester proprement."
    $ debat_day3_apply_influence({"tomas": 1, "kael": 1})
    return

label debat_phase2_counter_d7:
    noam "Elen, concurrence oui, mais dans un cadre clair."
    elen "Tant que la sécurité minimale est maintenue, ça me va."
    $ debat_day3_apply_influence({"elen": 1, "mara": 1})
    return

label debat_phase2_counter_d8:
    noam "Kael, un marché légal traçable réduit justement le noir."
    kael "Si la traçabilité est vérifiable, c'est défendable."
    $ debat_day3_apply_influence({"kael": 2, "nyra": 1})
    return

label debat_phase2_counter_d9:
    noam "Nyra, contrôle tournant et audits publics : personne ne confisque les stocks."
    nyra "D'accord. Dans ce cadre, c'est plus stable."
    $ debat_day3_apply_influence({"nyra": 1, "iris": 1})
    return

label debat_phase2_counter_d10:
    noam "Ryn, on découpe la réforme en étapes mesurables."
    ryn "...Si les étapes sont réversibles, je peux suivre."
    $ debat_day3_apply_influence({"ryn": 2, "mara": 1})
    return

label debat_phase2_counter_d11:
    noam "Sael, on ajoute des clauses de secours automatiques."
    sael "Là, on parle d'un texte qui peut survivre à la réalité."
    $ debat_day3_apply_influence({"sael": 1, "julian": -1})
    return

label debat_phase2_counter_d12:
    noam "L'expérience de la pénurie doit servir à calibrer, pas bloquer toute évolution."
    mara "...Je veux des garanties écrites."
    $ debat_day3_apply_influence({"mara": -1, "lysa": 1})
    return

label debat_phase2_counter_d13:
    noam "Le risque est acceptable seulement avec des seuils d'alerte précis."
    julian "OK, si on grave ces seuils dans l'amendement."
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    return

label debat_phase2_counter_d14:
    noam "Exact. Le critère n°1 reste : tout le monde mange demain."
    iris "Dans ce cas, je défends cette version amendée."
    $ debat_day3_apply_influence({"iris": 1, "ryn": 1})
    return

label debat_phase2_counter_d15:
    noam "Décider vite n'a aucune valeur si la décision est intenable."
    elias "...Très bien. On tranche, mais sur une version sécurisée."
    $ debat_day3_apply_influence({"elias": -1, "elen": 1, "sael": 1})
    return
