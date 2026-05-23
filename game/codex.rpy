# -----------------------------------------------------------------------
# CODEX — Entrées, catégories et déblocages
# -----------------------------------------------------------------------

default codex_unlocked_entries = [
    "districts_conclave",
    "systeme_votes",
    "personnage_noam",
]

default codex_notification_queue = []
default codex_current_notification = None

init python:

    CODEX_CATEGORY_ORDER = ["histoire", "district", "coutume", "divers"]

    CODEX_CATEGORY_LABELS = {
        "histoire": "Histoire",
        "district": "District",
        "coutume": "Coutume",
        "divers": "Divers",
    }

    CODEX_ENTRIES = {
        "districts_conclave": {
            "title": "Districts du Conclave",
            "category": "district",
            "unlocked_day": 1,
            "text": """Le Conclave n'est pas une ville au sens ancien du terme, mais une agrégation de zones spécialisées reliées par des couloirs pressurisés, des sas et des routines de rationnement. Chaque district fonctionne comme un organe: la Cafétéria assure l'apport énergétique, l'Infirmerie absorbe les chocs biologiques, la Maintenance prolonge la survie mécanique, l'Observatoire anticipe les ruptures.

Depuis la troisième réorganisation, l'administration Kami impose une circulation par quotas temporels: on ne traverse pas un district parce qu'on le souhaite, mais parce qu'un besoin est validé. Ce système diminue les incidents, tout en créant des angles morts sociaux. Les représentants, censés compenser cette fragmentation, deviennent alors des filtres d'information autant que des voix politiques.

On observe enfin un phénomène propre aux environnements clos: l'identité individuelle se confond progressivement avec le district d'appartenance. Un conflit entre personnes se présente rapidement comme un conflit entre fonctions. Cette translation explique pourquoi les votes du Conclave paraissent souvent « techniques » alors qu'ils sont traversés d'affects et de mémoire."""
        },
        "systeme_votes": {
            "title": "Système de vote des représentants",
            "category": "coutume",
            "unlocked_day": 1,
            "text": """Le vote n'est pas un rituel démocratique classique; c'est un protocole de répartition du risque. Douze représentants y participent, avec un poids théoriquement égal, mais des conséquences asymétriques selon la proposition adoptée. Une mesure sur l'énergie peut pénaliser immédiatement la Maintenance, alors qu'une mesure sur le rationnement affectera d'abord la Cafétéria et la Santé.

Le règlement Kami distingue trois niveaux: recommandation, directive locale et dérogation d'urgence. La recommandation est consultative; la directive locale devient exécutoire dès majorité simple; la dérogation exige un seuil renforcé et une justification archivable. Dans la pratique, la frontière entre ces catégories dépend de l'état de crise déclaré.

Les observateurs extérieurs décrivent ce modèle comme « froid ». Pourtant, les archives montrent que les alignements de vote suivent aussi des affinités interpersonnelles, des dettes symboliques et des conflits antérieurs. Comprendre la mécanique officielle sans lire les liens informels revient à lire seulement la moitié du système."""
        },
        "personnage_noam": {
            "title": "Noam — médiateur émergent",
            "category": "histoire",
            "linked_profile": "noam",
            "unlocked_day": 1,
            "text": """Noam occupe une position paradoxale: il ne possède ni l'ancienneté de Tomas, ni l'autorité procédurale de Nyra, ni l'assise technique de Kael. Pourtant, il obtient un avantage décisif dans les séquences de débat: la capacité à reformuler sans humilier.

Les témoins décrivent chez lui une écoute orientée vers les « points de friction utiles ». Là où d'autres cherchent à gagner une confrontation, Noam tente d'identifier le noyau non négociable de chaque interlocuteur puis de construire un terrain d'accord minimal. Cette méthode ralentit la décision à court terme, mais réduit la probabilité de sabotage passif après le vote.

Les analyses psychologiques internes relèvent également un coût personnel. Un médiateur absorbe la charge émotionnelle de plusieurs camps sans appartenir pleinement à aucun. À mesure que les crises s'enchaînent, Noam peut devenir soit un pivot de cohésion, soit un point de rupture."""
        },
        "rationnement_consequences": {
            "title": "Conséquences des bons de rationnement",
            "category": "divers",
            "text": """Après chaque vote sur les bons de rationnement, l'effet immédiat est mesurable (portion, files, incidents), mais l'effet profond est comportemental. Les ménages adaptent leurs horaires, les personnels médicaux déplacent les soins non urgents, les équipes techniques choisissent quelles pannes « attendre ». Le rationnement redistribue le temps autant que la nourriture.

Les bulletins Kami présentent ces ajustements comme des preuves de résilience. Les témoignages anonymes, eux, parlent de fatigue stratégique: chacun optimise sa survie locale au détriment d'une vision commune. C'est dans cet écart narratif que naissent les tensions politiques du Conclave."""
        },
        "complexe_c": {
            "title": "Complexe C",
            "category": "district",
            "text": """Le complexe C est l'un des ensembles résidentiels majeurs d'Orbite. Il regroupe un total de quatre modules familiaux, de deux modules de production, d'un module administratif, des coursives pressurisées, des points de confinement et des sas de sécurité capables d'isoler une section en quelques secondes. Dans les bulletins Kami, il est présenté comme une réussite d'ingénierie orbitale : compartimenté, redondant, conçu pour encaisser les incidents sans compromettre l'ensemble de la station.

Sur place, la réalité est moins propre. Chaque habitant connaît les alarmes, les itinéraires d'évacuation et l'ordre exact des attaches d'un scaphandre d'urgence. Les enfants apprennent ces gestes comme des comptines, parce qu'une fuite, une sanction laser ou une panne de jonction ne laisse pas le temps d'avoir peur correctement. Le complexe C ne protège pas seulement ses habitants : il les dresse à survivre.

C'est cette normalité-là qui marque le plus les représentants d'Orbite. Une alerte de sas n'est pas un événement exceptionnel, mais un rappel brutal de leur quotidien. Quand une section comme le module C-4 s'isole, cent quarante personnes peuvent se retrouver coupées du reste de la station, dépendantes des réserves locales, des procédures et du sang-froid de familles entières. Dans Orbite, la sécurité n'est pas une promesse. C'est une série de gestes à réussir avant que l'air ne parte."""
        },
    }

    def codex_valid_entry_ids():
        return [eid for eid in store.codex_unlocked_entries if eid in CODEX_ENTRIES]

    def codex_entries_for_category(category_id):
        unlocked = codex_valid_entry_ids()
        return [eid for eid in unlocked if CODEX_ENTRIES[eid].get("category") == category_id]

    def codex_has_visible_entries(category_id):
        return len(codex_entries_for_category(category_id)) > 0

    def codex_visible_categories():
        return [cid for cid in CODEX_CATEGORY_ORDER if codex_has_visible_entries(cid)]

    def codex_first_visible_category():
        visible = codex_visible_categories()
        return visible[0] if visible else (CODEX_CATEGORY_ORDER[0] if CODEX_CATEGORY_ORDER else None)

    def codex_first_visible_entry(category_id=None):
        cid = category_id or codex_first_visible_category()
        entries = codex_entries_for_category(cid) if cid else []
        return entries[0] if entries else None

    def codex_completion_percent():
        total = len(CODEX_ENTRIES)
        unlocked = len(codex_valid_entry_ids())
        return int((100.0 * unlocked) / total) if total else 0

    def codex_unlock_page(entry_id, with_notification=True):
        if entry_id not in CODEX_ENTRIES:
            return False
        if entry_id in store.codex_unlocked_entries:
            return False
        store.codex_unlocked_entries.append(entry_id)
        if with_notification:
            store.codex_notification_queue.append(entry_id)
            if not store.codex_current_notification:
                codex_show_next_notification()
        renpy.restart_interaction()
        return True

    def unlock_codex_page(entry_id, with_notification=True):
        return codex_unlock_page(entry_id, with_notification=with_notification)

    def unlock_codex_entry(entry_id):
        return codex_unlock_page(entry_id, with_notification=True)

    def codex_show_next_notification():
        if store.codex_current_notification or not store.codex_notification_queue:
            return
        next_entry_id = store.codex_notification_queue.pop(0)
        entry = CODEX_ENTRIES.get(next_entry_id)
        if not entry:
            return
        store.codex_current_notification = {
            "entry_id": next_entry_id,
            "title": entry.get("title", next_entry_id),
            "category": entry.get("category", "divers"),
        }
        renpy.show_screen("codex_unlock_notification")

    def codex_pop_notification():
        store.codex_current_notification = None
        renpy.hide_screen("codex_unlock_notification")
        codex_show_next_notification()


# -----------------------------------------------------------------------
# Transforms
# -----------------------------------------------------------------------

transform codex_notif_appear:
    alpha 0.0
    xoffset 30
    parallel:
        ease 0.22 alpha 1.0
    parallel:
        ease 0.22 xoffset 0

transform codex_entry_appear:
    alpha 0.0
    yoffset 8
    ease 0.18 alpha 1.0 yoffset 0


# -----------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------

style codex_default:
    font "fonts/Barlow-Light.ttf"

style codex_nav_idle is codex_default:
    color "#3a6a80"
    size 24
    hover_color "#7ab8cc"

style codex_nav_idle_selected is codex_nav_idle:
    color "#a8d8ea"

style codex_cat_idle is codex_default:
    color "#2a5a72"
    size 23
    hover_color "#5ab0c8"

style codex_cat_idle_selected is codex_cat_idle:
    color "#5cd3ff"

style codex_entry_idle is codex_default:
    color "#3a7a90"
    size 21
    hover_color "#8ac8da"
    left_padding 10

style codex_entry_idle_selected is codex_entry_idle:
    color "#a8dff0"

style codex_read_category is codex_default:
    color "#2a6a8a"
    size 19
    kerning 3

style codex_read_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#daeaf5"
    size 46
    line_spacing 2

style codex_read_body is codex_default:
    color "#8aacbc"
    size 23
    line_spacing 8

style codex_section_label is codex_default:
    color "#1e4a65"
    size 18
    kerning 4

style codex_index_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#daeaf5"
    size 38

style codex_completion_label is codex_default:
    color "#2a5a7a"
    size 19
    kerning 2

style codex_notif_sub is codex_default:
    color "#2a6a8a"
    size 18
    kerning 3

style codex_notif_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    color "#c8e8f5"
    size 28

style codex_notif_cat is codex_default:
    color "#3a7a90"
    size 19

style codex_empty_label is codex_default:
    color "#1e4a65"
    size 22


# -----------------------------------------------------------------------
# Notification de déblocage
# -----------------------------------------------------------------------

screen codex_unlock_notification():
    zorder 500

    if codex_current_notification:
        frame at codex_notif_appear:
            background Solid("#07151e")
            xalign 0.985
            yalign 0.08
            xsize 480
            padding (0, 14, 18, 14)

            hbox:
                spacing 0

                frame:
                    background Solid("#3a9fca")
                    xsize 3
                    yfill True
                    right_margin 14

                vbox:
                    spacing 5

                    text "NOUVELLE PAGE DU CODEX":
                        style "codex_notif_sub"

                    text "[codex_current_notification['title']]":
                        style "codex_notif_title"

                    text "[CODEX_CATEGORY_LABELS.get(codex_current_notification['category'], codex_current_notification['category'])]":
                        style "codex_notif_cat"

        timer 3.0 action Function(codex_pop_notification)


# -----------------------------------------------------------------------
# Écran principal du Codex
# -----------------------------------------------------------------------

screen codex_menu():
    tag menu

    default selected_category = codex_first_visible_category()
    default selected_entry    = codex_first_visible_entry(selected_category)

    add Solid("#080d12")

    hbox:
        xfill True
        yfill True

        # -----------------------------------------------------------
        # Colonne 1 — Navigation principale
        # -----------------------------------------------------------
        frame:
            background Solid("#00000000")
            xsize 200
            yfill True

            frame:
                background Solid("#00000000")
                padding (20, 24, 0, 0)

                vbox:
                    xfill True
                    yfill True

                    text "MENU":
                        style "codex_section_label"

                    null height 14

                    for lbl, act in [
                        ("Historique",  ShowMenu("history")),
                        ("Sauvegarde",  ShowMenu("save")),
                        ("Charger",     ShowMenu("load")),
                        ("Préférences", ShowMenu("preferences")),
                        ("Profils",     ShowMenu("profiles")),
                        ("Codex",       NullAction()),
                        ("À propos",    ShowMenu("about")),
                        ("Quitter",     MainMenu()),
                    ]:
                        textbutton "[lbl]":
                            action act
                            style "codex_nav_idle"
                            selected (lbl == "Codex")
                            ypadding 7
                            xfill True

        # Séparateur vertical
        frame:
            background Solid("#122030")
            xsize 1
            yfill True

        # -----------------------------------------------------------
        # Colonne 2 — Index
        # -----------------------------------------------------------
        frame:
            background Solid("#00000000")
            xsize 260
            yfill True

            vbox:
                xfill True
                yfill True

                # En-tête
                frame:
                    background Solid("#00000000")
                    xfill True
                    padding (20, 20, 20, 16)

                    vbox:
                        spacing 8

                        text "Codex":
                            style "codex_index_title"

                        if j2_vote_codex_unlocked:
                            textbutton "Prochain vote":
                                action ShowMenu("day2_current_vote_codex")
                                style "codex_cat_idle"
                                ypadding 4
                                xfill True

                        $ pct = codex_completion_percent()
                        $ filled_w = int(2.20 * pct)

                        frame:
                            background Solid("#122030")
                            xfill True
                            ysize 2
                            xpadding 0
                            ypadding 0

                            frame:
                                background Solid("#3bbcef")
                                xsize filled_w
                                ysize 2
                                xalign 0.0

                        text "[pct]% — [len(codex_valid_entry_ids())] / [len(CODEX_ENTRIES)] pages":
                            style "codex_completion_label"

                # Séparateur horizontal
                frame:
                    background Solid("#122030")
                    xfill True
                    ysize 1

                # Catégories
                frame:
                    background Solid("#00000000")
                    xfill True
                    padding (20, 14, 20, 0)

                    vbox:
                        spacing 6

                        text "CATÉGORIES":
                            style "codex_section_label"

                        null height 4

                        for category_id in CODEX_CATEGORY_ORDER:
                            $ cat_entries = codex_entries_for_category(category_id)
                            if cat_entries:
                                textbutton "[CODEX_CATEGORY_LABELS.get(category_id, category_id)] ([len(cat_entries)])":
                                    action [
                                        SetScreenVariable("selected_category", category_id),
                                        SetScreenVariable("selected_entry", codex_first_visible_entry(category_id)),
                                    ]
                                    style "codex_cat_idle"
                                    selected (selected_category == category_id)
                                    ypadding 5
                                    xfill True

                # Pages débloquées
                frame:
                    background Solid("#00000000")
                    xfill True
                    yfill True
                    padding (20, 12, 20, 12)

                    vbox:
                        spacing 4

                        text "PAGES DÉBLOQUÉES":
                            style "codex_section_label"

                        null height 6

                        $ current_entries = codex_entries_for_category(selected_category) if selected_category else []
                        if current_entries:
                            for eid in current_entries:
                                $ edata = CODEX_ENTRIES[eid]
                                textbutton "[edata['title']]":
                                    action SetScreenVariable("selected_entry", eid)
                                    style "codex_entry_idle"
                                    selected (selected_entry == eid)
                                    ypadding 6
                                    xfill True
                                    text_xalign 0.0
                        else:
                            text "Aucune page débloquée.":
                                style "codex_empty_label"

        # Séparateur vertical
        frame:
            background Solid("#122030")
            xsize 1
            yfill True

        # -----------------------------------------------------------
        # Colonne 3 — Panneau de lecture
        # -----------------------------------------------------------
        frame:
            background Solid("#00000000")
            xfill True
            yfill True
            padding (40, 32, 40, 32)

            if selected_entry and selected_entry in CODEX_ENTRIES:
                $ edata = CODEX_ENTRIES[selected_entry]
                $ cat_label = CODEX_CATEGORY_LABELS.get(edata.get("category", "divers"), edata.get("category", "divers"))

                vbox at codex_entry_appear:
                    spacing 0
                    xfill True

                    hbox:
                        spacing 10

                        frame:
                            background Solid("#1e4a65")
                            xsize 20
                            ysize 1
                            yalign 0.5

                        text "[cat_label]":
                            style "codex_read_category"

                    null height 12

                    text "[edata['title']]":
                        style "codex_read_title"

                    null height 20

                    frame:
                        background Solid("#1e6a90")
                        xsize 40
                        ysize 1

                    null height 22

                    viewport:
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        yfill True
                        xfill True

                        text "[edata['text']]":
                            style "codex_read_body"
                            xfill True

            else:
                text "Aucune page débloquée pour le moment.":
                    style "codex_empty_label"
                    xalign 0.5
                    yalign 0.5
