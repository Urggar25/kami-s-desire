# Mini-jeu : Débat - Phase 2 (Buzzer / contradictions)

default debat_phase2_buzzed_ids = []
default debat_phase2_rebuttal_log = []
default debat_phase2_vote_summary = {}

image kami_debat_background = "images/background/bg_conclave.png"

init python:
    DEBAT_PHASE2_LINE_DURATION = 5.0

    # Chaque entrée est indépendante : simple à ajouter/supprimer/reclasser.
    DEBAT_PHASE2_DIALOGUES = [
        {
            "id": "d1",
            "speaker": "Mara",
            "line": "Abolir la distribution, c'est condamner les plus fragiles.",
            "counter": "Contre-argument : on peut remplacer la distribution par un fonds d'urgence ciblé, pas la supprimer sans filet.",
        },
        {
            "id": "d2",
            "speaker": "Elias",
            "line": "Le marché libre va enfin récompenser ceux qui se bougent.",
            "counter": "Contre-argument : récompenser l'effort n'empêche pas de fixer des garde-fous contre les abus.",
        },
        {
            "id": "d3",
            "speaker": "Lysa",
            "line": "Vous confondez liberté économique et abandon collectif.",
            "counter": "Contre-argument : la réforme peut conserver un socle collectif tout en ouvrant des échanges limités.",
        },
        {
            "id": "d4",
            "speaker": "Julian",
            "line": "Ce système est lent, opaque, et il étouffe toute initiative.",
            "counter": "Contre-argument : alors auditons-le et corrigeons-le, au lieu de le démolir en une fois.",
        },
        {
            "id": "d5",
            "speaker": "Iris",
            "line": "Si les prix flambent, certains ne mangeront juste plus.",
            "counter": "Contre-argument : on peut imposer un plafond sur les denrées vitales pour éviter cette flambée.",
        },
        {
            "id": "d6",
            "speaker": "Tomas",
            "line": "On n'a même pas simulé l'impact logistique de la transition.",
            "counter": "Contre-argument : validons une phase pilote courte avant tout déploiement global.",
        },
        {
            "id": "d7",
            "speaker": "Elen",
            "line": "Sans concurrence, la qualité stagne et tout le monde perd.",
            "counter": "Contre-argument : la concurrence peut exister dans un cadre régulé, pas dans un vide total.",
        },
        {
            "id": "d8",
            "speaker": "Kael",
            "line": "On risque surtout de créer un marché noir impossible à contrôler.",
            "counter": "Contre-argument : justement, légaliser partiellement avec traçabilité réduit l'intérêt du marché noir.",
        },
        {
            "id": "d9",
            "speaker": "Nyra",
            "line": "Le vrai sujet, c'est qui contrôlera les stocks critiques.",
            "counter": "Contre-argument : un comité tournant et auditable peut sécuriser ce contrôle.",
        },
        {
            "id": "d10",
            "speaker": "Ryn",
            "line": "Ce texte ressemble à un pari fait avec nos vies.",
            "counter": "Contre-argument : on peut transformer ce pari en plan à étapes mesurables.",
        },
        {
            "id": "d11",
            "speaker": "Sael",
            "line": "Je voterai jamais un amendement aussi brutal sans clauses de secours.",
            "counter": "Contre-argument : ajoutons des clauses de retour arrière automatiques en cas de crise.",
        },
        {
            "id": "d12",
            "speaker": "Mara",
            "line": "Ceux qui défendent ce texte n'ont pas connu la vraie pénurie.",
            "counter": "Contre-argument : l'expérience de la pénurie doit guider une réforme prudente, pas l'interdire.",
        },
        {
            "id": "d13",
            "speaker": "Julian",
            "line": "Si on refuse tout risque, on restera bloqués dans la même misère.",
            "counter": "Contre-argument : prendre des risques oui, mais seulement avec des seuils d'alerte clairs.",
        },
        {
            "id": "d14",
            "speaker": "Iris",
            "line": "Le débat n'a de sens que si chacun peut encore se nourrir demain.",
            "counter": "Contre-argument : c'est justement le critère numéro un à graver dans l'amendement.",
        },
        {
            "id": "d15",
            "speaker": "Elias",
            "line": "On tranche ce soir, sinon on n'avancera jamais.",
            "counter": "Contre-argument : trancher vite ne vaut rien si la décision est impossible à assumer demain.",
        },
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

    def debat_day3_vote_from_stat(stat_value):
        if stat_value > 0:
            return "pour"
        if stat_value == 0:
            return "abstention"
        return "contre"

    def debat_day3_compute_votes(stats=None):
        source = stats if stats is not None else DEBAT_DAY3_BASE_VOTE_STATS
        result = {"pour": 0, "abstention": 0, "contre": 0, "details": {}}

        for character, stat_value in source.items():
            vote = debat_day3_vote_from_stat(stat_value)
            result[vote] += 1
            result["details"][character] = vote

        return result

screen debat_phase2_line(dialogue_data):
    modal True
    zorder 120

    add "kami_debat_background" at adaptive_fullscreen

    frame:
        background Solid("#00000055")
        xfill True
        yfill True

    # Buzzer au premier plan
    frame:
        background Solid("#9f1616dd")
        xalign 0.5
        yalign 0.92
        xsize 360
        ysize 90

        textbutton "BUZZER" style "debat_phase2_buzzer_button":
            xalign 0.5
            yalign 0.5
            action Return({
                "buzzed": True,
                "id": dialogue_data["id"],
                "speaker": dialogue_data["speaker"],
                "counter": dialogue_data["counter"],
            })

    vbox:
        xalign 0.5
        yalign 0.16
        spacing 10

        text "[dialogue_data['speaker']]" style "debat_phase2_speaker_text"
        text "[dialogue_data['line']]" style "debat_phase2_line_text"

    timer DEBAT_PHASE2_LINE_DURATION action Return({"buzzed": False, "id": dialogue_data["id"]})

style debat_phase2_speaker_text:
    color "#FFFFFF"
    font "fonts/day_font.ttf"
    size 60
    outlines [(3, "#000000B0", 0, 0)]
    text_align 0.5
    xalign 0.5

style debat_phase2_line_text:
    color "#FFFFFF"
    font "fonts/day_font.ttf"
    size 50
    outlines [(4, "#000000C0", 0, 0)]
    text_align 0.5
    xalign 0.5

style debat_phase2_buzzer_button is default:
    font "fonts/day_font.ttf"
    size 42
    color "#FFFFFF"
    hover_color "#FFE7A8"
    outlines [(2, "#000000", 0, 0)]

label debat_phase2_minigame:
    $ debat_phase2_buzzed_ids = []
    $ debat_phase2_rebuttal_log = []

    scene kami_debat_background at adaptive_fullscreen with dissolve

    "Mini-jeu : buzze au bon moment pour contredire un argument."

    python:
        for dialogue_data in DEBAT_PHASE2_DIALOGUES:
            outcome = renpy.call_screen("debat_phase2_line", dialogue_data=dialogue_data)
            if outcome and outcome.get("buzzed"):
                rebuttal = outcome.get("counter", "")
                store.debat_phase2_buzzed_ids.append(outcome.get("id"))
                store.debat_phase2_rebuttal_log.append({
                    "id": outcome.get("id"),
                    "speaker": outcome.get("speaker"),
                    "counter": rebuttal,
                })
                if rebuttal:
                    renpy.say(None, rebuttal)

    $ debat_phase2_vote_summary = debat_day3_compute_votes()

    "Résultat provisoire du vote : [debat_phase2_vote_summary['pour']] pour, [debat_phase2_vote_summary['abstention']] abstention, [debat_phase2_vote_summary['contre']] contre."

    return
