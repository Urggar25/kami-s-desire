# -----------------------------------------------------------------------
# CODEX — Entrées, catégories et déblocages
# -----------------------------------------------------------------------

# Entrées visibles au démarrage.
default codex_unlocked_entries = [
    "districts_conclave",
    "systeme_votes",
    "personnage_noam",
]

# File de notifications de pages débloquées.
default codex_notification_queue = []
default codex_current_notification = None

init python:
    # -------------------------------------------------------------------
    # Configuration des catégories
    # Pour ajouter/retirer une catégorie, modifiez ces 2 structures.
    # -------------------------------------------------------------------
    CODEX_CATEGORY_ORDER = ["histoire", "district", "coutume", "divers"]

    CODEX_CATEGORY_LABELS = {
        "histoire": "Histoire",
        "district": "District",
        "coutume": "Coutume",
        "divers": "Divers",
    }

    # -------------------------------------------------------------------
    # Pages du codex
    # category doit utiliser une clé présente dans CODEX_CATEGORY_ORDER.
    # -------------------------------------------------------------------
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

    # Alias de compatibilité avec le code existant.
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


transform codex_unlock_notification_appear:
    alpha 0.0
    xoffset 80
    parallel:
        ease 0.25 alpha 1.0
    parallel:
        ease 0.25 xoffset 0


screen codex_unlock_notification():
    zorder 500

    if codex_current_notification:
        frame at codex_unlock_notification_appear:
            background Solid("#0f1f2ae8")
            xalign 0.985
            yalign 0.08
            xsize 520
            padding (16, 12)

            vbox:
                spacing 4
                text "Nouvelle page du Codex" size 24 color "#A3E0FF"
                text "[codex_current_notification['title']]" size 27 color "#FFFFFF"
                text "Catégorie : [CODEX_CATEGORY_LABELS.get(codex_current_notification['category'], codex_current_notification['category'])]" size 19 color "#BFD6EA"

        timer 2.8 action Function(codex_pop_notification)


screen codex_menu():
    tag menu

    default selected_category = codex_first_visible_category()
    default selected_entry = codex_first_visible_entry(selected_category)

    use game_menu(_("Codex"), scroll="viewport"):

        hbox:
            spacing 24

            frame:
                background Solid("#110f0dcc")
                xsize 430
                yfill True
                padding (14, 14)

                vbox:
                    spacing 8
                    text "Index" size 34 color "#E8D8B8"
                    text "Complétion: [codex_completion_percent()]%" size 22 color "#C9B896"

                    null height 8
                    text "Catégories" size 24 color "#F4E3C1"

                    for category_id in CODEX_CATEGORY_ORDER:
                        $ category_entries = codex_entries_for_category(category_id)
                        if category_entries:
                            textbutton "[CODEX_CATEGORY_LABELS.get(category_id, category_id)] ([len(category_entries)])":
                                action [
                                    SetScreenVariable("selected_category", category_id),
                                    SetScreenVariable("selected_entry", codex_first_visible_entry(category_id)),
                                ]

                    null height 10
                    text "Pages débloquées" size 24 color "#F4E3C1"

                    $ current_entries = codex_entries_for_category(selected_category) if selected_category else []
                    if current_entries:
                        for eid in current_entries:
                            $ entry = CODEX_ENTRIES[eid]
                            textbutton "[entry['title']]":
                                action SetScreenVariable("selected_entry", eid)
                    else:
                        text "Aucune page débloquée dans cette catégorie." size 20 color "#A99779"

            frame:
                background Solid("#1a1612dd")
                xfill True
                yfill True
                padding (18, 18)

                if selected_entry and selected_entry in CODEX_ENTRIES:
                    $ entry = CODEX_ENTRIES[selected_entry]
                    vbox:
                        spacing 12
                        text "[entry['title']]" size 40 color "#F8E7C2"
                        text "[CODEX_CATEGORY_LABELS.get(entry.get('category', 'divers'), entry.get('category', 'divers'))]" size 20 color "#BFAF8E"

                        viewport:
                            mousewheel True
                            draggable True
                            scrollbars "vertical"
                            ysize 580

                            text "[entry['text']]" size 22 color "#EFE7D8" line_spacing 4
                else:
                    text "Aucune page du Codex débloquée pour le moment." size 24 color "#A99779"
