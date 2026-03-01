# Mini-jeu : Débat - Phase 2 (Buzzer / contradictions)

default debat_phase2_buzzed_ids = []
default debat_phase2_rebuttal_log = []
default debat_phase2_vote_summary = {}
default debat_day3_live_vote_stats = {}

define DEBAT_PHASE2_LINE_DURATION = 6.0

define DEBAT_PHASE2_FADE_TIME = 0.35
define DEBAT_PHASE2_REBUTTAL_LINE_DURATION = 5.0

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
        {"id": "d1", "speaker": "Mara", "speaker_tag": "mara", "speaker_expr": "doute", "counter_label": "debat_phase2_counter_d1", "lines": ["Ah, je dois commence ?? Euh...", "Abolir la distribution risque de", "condamner les plus fragiles."]},
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

    add "[dialogue_data['speaker_tag']] [dialogue_data['speaker_expr']]" at Position(xalign=0.00, yalign=1.0), debat_phase2_fade_cycle(DEBAT_PHASE2_LINE_DURATION, DEBAT_PHASE2_FADE_TIME)

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

    add "[entry_data['speaker_tag']] [entry_data['speaker_expr']]" at Position(xalign=0.00, yalign=1.0), debat_phase2_fade_cycle(duration, DEBAT_PHASE2_FADE_TIME)

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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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
            "ne sauvere jamais personne."
        ]},

        {"speaker": "Noam", "speaker_tag": "noam", "speaker_expr": "determine",
        "lines": [
            "Alors arrête de parler",
            "comme si l’échec était utile.",
            "Pour certains, il sera définitif."
        ]},
    ]

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
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

    call debat_phase2_play_rebuttal_sequence(seq)
    $ debat_day3_apply_influence({"julian": -1, "tomas": 1})
    jump debat_phase2_resume