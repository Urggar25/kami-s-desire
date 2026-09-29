# =============================================================================
# CONCLAVE OS — DOSSIER D'ENQUÊTE ET OUTILS D'INVESTIGATION
# Systèmes génériques, compatibles avec les anciennes sauvegardes via `default`.
# =============================================================================

default investigation_unlocked = False
default investigation_evidence = {}
default investigation_links = []
default investigation_selected_category = "evenements"
default investigation_selected_id = None
default investigation_map_nodes = []
default investigation_video_findings = {}
default investigation_inspection_findings = {}
default investigation_contradictions = []

init python:

    if "investigation_quick_access" not in config.overlay_screens:
        config.overlay_screens.append("investigation_quick_access")

    INVESTIGATION_CATEGORIES = [
        ("evenements", "ÉVÉNEMENTS", "#5CD3FF"),
        ("preuves", "OBJETS / PREUVES", "#72E0B8"),
        ("personnes", "PERSONNES", "#B89CFF"),
        ("anomalies", "ANOMALIES", "#FF6B8A"),
        ("hypotheses", "HYPOTHÈSES", "#F0B75A"),
    ]

    INVESTIGATION_ENTRIES = {
        "cafe_renverse": {
            "category": "evenements", "title": "CAFÉ RENVERSÉ",
            "desc": "Elias renverse son café sur une console d'observation, qui se verrouille et commence à fumer.",
            "day": "J5", "origin": "SALLE D'OBSERVATION", "status": "INCIDENT",
        },
        "livraison_j7": {
            "category": "evenements", "title": "LIVRAISON — JOUR 7",
            "desc": "Une livraison arrivée en avance contient des vivres, du matériel et une passagère clandestine.",
            "day": "J7", "origin": "SAS DE LIVRAISON", "status": "ANOMALIE LOGISTIQUE",
        },
        "photo_lea_disparue": {
            "category": "preuves", "title": "PHOTO DE LÉA DISPARUE",
            "desc": "La seule photo de la sœur de Kael a disparu de sa chambre.",
            "day": "J8", "origin": "CHAMBRE DE KAEL", "status": "NON RÉSOLU",
        },
        "dessin_juliette_disparu": {
            "category": "preuves", "title": "DESSIN DE JULIETTE DISPARU",
            "desc": "Le dessin conservé par Noam n'est plus dans sa chambre malgré une fouille complète.",
            "day": "J7–8", "origin": "CHAMBRE DE NOAM", "status": "NON RÉSOLU",
        },
        "materiel_technique_manquant": {
            "category": "preuves", "title": "VOL DU MATÉRIEL DE MAINTENANCE",
            "desc": "Des batteries, des outils et plusieurs composants ont disparu de la réserve.",
            "day": "J7", "origin": "RÉSERVE TECHNIQUE", "status": "À LOCALISER",
        },
        "silhouette_couloirs": {
            "category": "evenements", "title": "SILHOUETTE DANS LES COULOIRS",
            "desc": "Une présence indistincte a été aperçue alors que Noam était fiévreux.",
            "day": "J10", "origin": "COULOIR DE L'INFIRMERIE", "status": "TÉMOIGNAGE FRAGILE",
        },
        "kami_hors_ligne": {
            "category": "anomalies", "title": "PANNE DE KAMI",
            "desc": "Kami reste silencieuse pendant les jours 7 et 8, puis revient le jour 9 en invoquant une maintenance.",
            "day": "J7–8", "origin": "CONCLAVE OS", "status": "ANOMALIE",
        },
        "doppelganger": {
            "category": "anomalies", "title": "DOPPELGÄNGER",
            "desc": "Kael adopte soudain une voix et un comportement méconnaissables juste avant le trou de mémoire de Noam.",
            "day": "J15", "origin": "COULOIR DES DORTOIRS", "status": "IDENTITÉ SUSPECTE",
        },
        "videos_supprimees": {
            "category": "preuves", "title": "VIDÉOS SUPPRIMÉES",
            "desc": "Une séquence entière des caméras du couloir a été effacée proprement des archives.",
            "day": "J11", "origin": "SALLE D'OBSERVATION", "status": "SUPPRESSION VOLONTAIRE",
        },
        "manque_nourriture": {
            "category": "evenements", "title": "MANQUE DE NOURRITURE",
            "desc": "Les réserves du Conclave chutent et Goumi commence à refuser les portions supplémentaires.",
            "day": "J11–12", "origin": "CAFÉTÉRIA", "status": "STOCK CRITIQUE",
        },
        "copie_dessin": {
            "category": "preuves", "title": "COPIE DU DESSIN DE JULIETTE",
            "desc": "Une reproduction presque exacte du dessin disparu est apparue dans le cahier noir de Noam.",
            "day": "J13", "origin": "CAHIER DE NOAM", "status": "AUTHENTICITÉ INCONNUE",
        },
        "valeur_sentimentale": {
            "category": "hypotheses", "title": "CIBLE : VALEUR SENTIMENTALE",
            "desc": "La photo et le dessin n'ont presque aucune valeur matérielle, mais une forte valeur affective.",
            "day": "J13", "origin": "RECOUPEMENT", "status": "HYPOTHÈSE",
        },
        "cicatrice_juliette": {
            "category": "anomalies", "title": "DÉTAIL IMPOSSIBLE — CICATRICE",
            "desc": "La copie montre la cicatrice de Juliette, détail absent du dessin original.",
            "day": "J13", "origin": "COMPARAISON DU DESSIN", "status": "INEXPLIQUÉ",
        },
        "video_kael": {
            "category": "evenements", "title": "VIDÉO DE KAEL — 21:17",
            "desc": "Une archive authentifiée montre Kael prenant la photo de Léa, ce qu'il nie avoir fait.",
            "day": "J8", "origin": "ARCHIVES CAMÉRA", "status": "CONTRADICTION",
        },
        "levres_kael": {
            "category": "anomalies", "title": "MOUVEMENT DES LÈVRES",
            "desc": "Kael semble prononcer quelque chose juste avant de quitter la pièce. Peut-être « désolé ».",
            "day": "J8", "origin": "ANALYSE IMAGE PAR IMAGE", "status": "LECTURE INCERTAINE",
        },
        "video_noam": {
            "category": "evenements", "title": "INTRUSION DANS LA CHAMBRE",
            "desc": "À 02:14, une personne ayant l'apparence de Kael entre chez Noam et prend le dessin.",
            "day": "J7–8", "origin": "ARCHIVES CAMÉRA", "status": "CONTRADICTION",
        },
        "hyp_trou_memoire": {
            "category": "hypotheses", "title": "MÉMOIRE DE KAEL ALTÉRÉE",
            "desc": "Kael pourrait avoir agi sans conserver de souvenir accessible de ses gestes.",
            "day": "J15", "origin": "VIDÉO + TÉMOIGNAGE", "status": "NON CONFIRMÉ",
        },
        "hyp_video_falsifiee": {
            "category": "hypotheses", "title": "VIDÉO FALSIFIÉE",
            "desc": "Les archives pourraient avoir été altérées sans laisser de trace détectable.",
            "day": "J15", "origin": "MÉTADONNÉES CAMÉRA", "status": "NON CONFIRMÉ",
        },
        "hyp_ressemblance_kael": {
            "category": "hypotheses", "title": "QUELQU'UN RESSEMBLE À KAEL",
            "desc": "Une troisième possibilité existe : l'individu filmé pourrait ne pas être Kael.",
            "day": "J15", "origin": "RECOUPEMENT", "status": "NON CONFIRMÉ",
        },
        "m16": {
            "category": "anomalies", "title": "M16 — ACCÈS MNÉSIQUE",
            "desc": "Le code M16, associé à un accès à la mémoire, apparaît dans plusieurs dossiers médicaux.",
            "day": "J16", "origin": "DOSSIERS MÉDICAUX", "status": "CLASSIFIÉ",
        },
        "exorcisme_noam": {
            "category": "evenements", "title": "EXORCISME DE NOAM",
            "desc": "Sael et Ryn soumettent Noam à un rituel brutal pour vérifier qu'il est encore lui-même.",
            "day": "J14", "origin": "CHAMBRE DE SAEL", "status": "AGRESSION",
        },
        "livraison_j14": {
            "category": "evenements", "title": "LIVRAISON — JOUR 14",
            "desc": "Une nouvelle cargaison de nourriture réapprovisionne le Conclave après plusieurs jours de pénurie.",
            "day": "J14", "origin": "SAS DE LIVRAISON", "status": "RÉCEPTIONNÉE",
        },
        "bruits_chambre": {
            "category": "anomalies", "title": "BRUITS ÉTRANGES DANS LA CHAMBRE",
            "desc": "Un frottement ou un pas réveille Noam près de son lit, sans qu'il puisse en identifier la source.",
            "day": "J12", "origin": "CHAMBRE DE NOAM", "status": "SOURCE INCONNUE",
        },
        "conduits_chambres": {
            "category": "preuves", "title": "DÉCOUVERTE DES CONDUITS",
            "desc": "Un réseau assez large pour une personne relie les chambres hors du champ des couloirs.",
            "day": "J17", "origin": "EXPLORATION", "status": "CONFIRMÉ",
        },
        "traces_conduit": {
            "category": "preuves", "title": "TRACES DANS LA POUSSIÈRE",
            "desc": "Des frottements récents traversent la poussière du conduit derrière la chambre de Noam.",
            "day": "J17", "origin": "CONDUIT DORTOIR", "status": "CONFIRMÉ",
        },
        "salle_goumi": {
            "category": "evenements", "title": "SALLE CACHÉE DES GOUMI",
            "desc": "Une salle de maintenance robotique est dissimulée au cœur du réseau technique.",
            "day": "J18", "origin": "RÉSEAU TECHNIQUE", "status": "LOCALISÉ",
        },
        "batteries_retrouvees": {
            "category": "preuves", "title": "BATTERIES VOLÉES RETROUVÉES",
            "desc": "Deux batteries correspondant au matériel volé reposent dans la salle des Goumi.",
            "day": "J18", "origin": "SALLE CACHÉE", "status": "CONFIRMÉ",
        },
        "goumi_demonte": {
            "category": "preuves", "title": "GOUMI DÉMONTÉ",
            "desc": "Une unité ouverte révèle une architecture de maintenance reliée aux conduits.",
            "day": "J18", "origin": "SALLE CACHÉE", "status": "SECONDAIRE",
        },
        "mara_exploration": {
            "category": "evenements", "title": "SOUVENIR — EXPLORATION AVEC MARA",
            "desc": "Noam se souvient avoir exploré les conduits et la salle des Goumi avec Mara.",
            "day": "J18", "origin": "SOUVENIR DE NOAM", "status": "TENU POUR VRAI",
        },
        "mara_nie": {
            "category": "anomalies", "title": "MARA NIE L'EXPLORATION",
            "desc": "Mara affirme ne jamais être entrée dans les conduits, en contradiction directe avec le souvenir de Noam.",
            "day": "J19", "origin": "CONFRONTATION", "status": "DEUX FAITS INCOMPATIBLES",
        },
        "corps_mara": {
            "category": "evenements", "title": "CORPS DE MARA",
            "desc": "Noam découvre le corps de Mara sur la table centrale de la salle cachée.",
            "day": "J19", "origin": "SALLE CACHÉE", "status": "OBSERVATION DIRECTE",
        },
        "mara_vivante": {
            "category": "personnes", "title": "MARA VIVANTE",
            "desc": "Mara est ensuite vue vivante, rendant les deux observations impossibles à concilier.",
            "day": "J20", "origin": "CONCLAVE", "status": "INCOMPATIBLE",
        },
    }

    INVESTIGATION_AUTO_LINKS = [
        (("photo_lea_disparue", "dessin_juliette_disparu"), "valeur_sentimentale"),
        (("video_kael", "levres_kael"), "hyp_trou_memoire"),
        (("video_kael", "levres_kael"), "hyp_video_falsifiee"),
        (("video_kael", "video_noam"), "hyp_ressemblance_kael"),
    ]

    def investigation_has(eid):
        return bool(getattr(store, "investigation_evidence", {}).get(eid, False))

    def investigation_add(eid, notify=True):
        if eid not in INVESTIGATION_ENTRIES:
            return False
        if not isinstance(getattr(store, "investigation_evidence", None), dict):
            store.investigation_evidence = {}
        changed = not store.investigation_evidence.get(eid, False)
        store.investigation_evidence[eid] = True
        store.investigation_unlocked = True
        if changed and notify:
            renpy.notify("DOSSIER D'ENQUÊTE — " + INVESTIGATION_ENTRIES[eid]["title"])
        investigation_refresh_hypotheses()
        return changed

    def investigation_refresh_hypotheses():
        for requirements, result in INVESTIGATION_AUTO_LINKS:
            if all(investigation_has(req) for req in requirements):
                store.investigation_evidence[result] = True
                link = tuple(list(requirements) + [result])
                if link not in store.investigation_links:
                    store.investigation_links.append(link)

    def investigation_story_available():
        if getattr(store, "investigation_unlocked", False):
            return True
        try:
            # Une sauvegarde créée avant l'ajout du dossier n'a pas rejoué son
            # déblocage du J8. Dès le jour suivant, le système doit néanmoins
            # être disponible comme il l'aurait été dans une nouvelle partie.
            return int(day_number()) > 8
        except Exception:
            return False

    def investigation_sync_legacy_save():
        if not investigation_story_available():
            return
        if not isinstance(getattr(store, "investigation_evidence", None), dict):
            store.investigation_evidence = {}
        try:
            current = int(day_number())
        except Exception:
            current = 0

        # Ne restaure que les faits de jours entièrement terminés afin de ne
        # jamais révéler à l'avance un élément du jour en cours.
        for eid, entry in INVESTIGATION_ENTRIES.items():
            if investigation_day_number(entry) < current:
                store.investigation_evidence[eid] = True
        store.investigation_unlocked = True

    def investigation_entries(category=None):
        result = []
        for eid, entry in INVESTIGATION_ENTRIES.items():
            if investigation_has(eid) and (category is None or entry["category"] == category):
                result.append((eid, entry))
        result.sort(key=lambda item: (investigation_day_number(item[1]), item[1]["title"]))
        return result

    def investigation_day_number(entry):
        value = str(entry.get("day", "0"))
        digits = ""
        for character in value:
            if character.isdigit():
                digits += character
            elif digits:
                break
        return int(digits or 0)

    def investigation_evidence_image(eid):
        return "images/hud/investigation/evidence/%s.png" % eid

    def investigation_category_color(category):
        for cid, _label, color in INVESTIGATION_CATEGORIES:
            if cid == category:
                return color
        return "#5CD3FF"

    def investigation_category_label(category):
        for cid, label, _color in INVESTIGATION_CATEGORIES:
            if cid == category:
                return label
        return "ÉLÉMENT"

    def investigation_scroll_timeline(adjustment, direction):
        if adjustment is None:
            return
        target = adjustment.value + (direction * 720)
        target = max(0, min(adjustment.range, target))
        adjustment.change(target)

    def investigation_category_count(category):
        return len(investigation_entries(category))

    def investigation_video_note(sequence, finding, evidence=None):
        if not isinstance(getattr(store, "investigation_video_findings", None), dict):
            store.investigation_video_findings = {}
        findings = list(store.investigation_video_findings.get(sequence, []))
        if finding not in findings:
            findings.append(finding)
            store.investigation_video_findings[sequence] = findings
        if evidence:
            investigation_add(evidence)

    def investigation_inspection_note(sequence, finding, evidence=None):
        if not isinstance(getattr(store, "investigation_inspection_findings", None), dict):
            store.investigation_inspection_findings = {}
        findings = list(store.investigation_inspection_findings.get(sequence, []))
        if finding not in findings:
            findings.append(finding)
            store.investigation_inspection_findings[sequence] = findings
        if evidence:
            investigation_add(evidence)

    def investigation_unlock_map(node):
        if node not in store.investigation_map_nodes:
            store.investigation_map_nodes.append(node)

    def objection_evaluate(selected, correct, relevant=()):
        if selected == correct:
            result = "correct"
        elif selected in relevant:
            result = "insufficient"
        elif selected:
            result = "wrong"
        else:
            result = "impossible"
        store.investigation_contradictions.append(result)
        return result


transform inv_pulse:
    alpha 0.45
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.45
    repeat

transform inv_reveal:
    alpha 0.0
    yoffset 12
    easeout 0.25 alpha 1.0 yoffset 0


transform investigation_quick_access_in:
    alpha 0.0
    xoffset 36
    easeout 0.35 alpha 1.0 xoffset 0

transform investigation_timeline_card_in(delay=0.0):
    alpha 0.0
    yoffset 18
    pause delay
    easeout 0.32 alpha 1.0 yoffset 0

transform investigation_detail_in:
    alpha 0.0
    xoffset 24
    easeout 0.24 alpha 1.0 xoffset 0


screen investigation_quick_access():
    zorder 150

    if investigation_story_available() and not renpy.get_screen("investigation_dossier"):
        key "K_i" action [Function(investigation_sync_legacy_save), Hide("tablet_home"), Show("investigation_dossier", persistent_access=True)]

        # Le HUD jour/période intègre déjà l'accès au dossier. L'ancien onglet
        # latéral ne sert plus que de repli si cet overlay n'est pas chargé.
        if not renpy.get_screen("tablet_home") and not renpy.get_screen("day_period_hud"):
            button:
                at investigation_quick_access_in
                xalign 0.998
                yalign 0.58
                xsize 340
                ysize 88
                padding (0, 0)
                background Transform(Crop((40, 140, 1930, 500), "images/hud/investigation/dossier_quick_access.png"), xysize=(340, 88))
                hover_background Transform(Crop((40, 140, 1930, 500), "images/hud/investigation/dossier_quick_access.png"), xysize=(340, 88), matrixcolor=BrightnessMatrix(0.12) * SaturationMatrix(1.18))
                action [Function(investigation_sync_legacy_save), Show("investigation_dossier", persistent_access=True)]

                fixed:
                    xysize (340, 88)
                    text "DOSSIER D'ENQUÊTE  ·  I":
                        xpos 94 ypos 24
                        size 18 color "#EAF8FF"
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                    text "[len(investigation_entries())] ÉLÉMENTS CONSIGNÉS":
                        xpos 95 ypos 51
                        size 11 color "#78B8D4"
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 1


screen _investigation_evidence_card(eid, entry, active=False, select_action=NullAction(), card_x=0, card_y=0):
    $ col = investigation_category_color(entry["category"])
    $ category_label = investigation_category_label(entry["category"])

    button:
        xpos card_x
        ypos card_y
        xsize 500
        ysize 292
        padding (0, 0)
        background None
        action select_action

        fixed:
            xysize (500, 292)

            if active:
                add Transform("images/hud/investigation/ui/investigation_card_paper.png", xysize=(500, 282), matrixcolor=BrightnessMatrix(0.08) * SaturationMatrix(1.08)) xpos 0 ypos 5
                add Solid(col) xpos 7 ypos 17 xsize 4 ysize 250
                add Solid(col) xpos 487 ypos 17 xsize 4 ysize 250
            else:
                add Transform("images/hud/investigation/ui/investigation_card_paper.png", xysize=(500, 282)) xpos 0 ypos 5

            add investigation_evidence_image(eid) xpos 24 ypos 35 xsize 205 ysize 205
            add Solid("#5C473A55") xpos 238 ypos 38 xsize 1 ysize 202

            text entry["day"]:
                xpos 255 ypos 35
                size 20 color "#17202B" bold True
                font "fonts/Rajdhani-SemiBold.ttf"
            text entry["title"]:
                xpos 255 ypos 65
                xmaximum 215 ymaximum 58
                size 21 color "#101721" bold True
                font "fonts/Rajdhani-SemiBold.ttf"

            add Solid(col) xpos 255 ypos 127 xsize 215 ysize 27
            text category_label:
                xpos 264 ypos 131
                size 13 color "#07121A" bold True kerning 1
                font "fonts/Rajdhani-SemiBold.ttf"

            text entry["desc"]:
                xpos 255 ypos 164
                xmaximum 215 ymaximum 76
                size 14 color "#28303A" line_spacing 1
                font "fonts/Barlow-Light.ttf"
            text entry["origin"]:
                xpos 255 ypos 248
                xmaximum 215
                size 11 color "#665A50" kerning 1
                font "fonts/Rajdhani-SemiBold.ttf"


screen investigation_dossier(from_tablet=False, persistent_access=False):
    modal True
    zorder 160
    default category = "all"
    default selected = investigation_selected_id
    default timeline_adjustment = ui.adjustment()

    add "images/hud/investigation/ui/investigation_board_bg.png"
    add Solid("#02071258")
    add Solid("#07101BBB") xpos 0 ypos 0 xsize 1920 ysize 132
    add Solid("#02050AB8") xpos 0 ypos 920 xsize 1920 ysize 160
    add Solid("#5CD3FF55") xpos 0 ypos 131 xsize 1920 ysize 1

    if from_tablet:
        $ close_action = [Hide("investigation_dossier"), Show("tablet_home")]
    elif persistent_access:
        $ close_action = Hide("investigation_dossier")
    else:
        $ close_action = Return()

    if selected:
        key "game_menu" action SetScreenVariable("selected", None)
        key "K_ESCAPE" action SetScreenVariable("selected", None)
    else:
        key "game_menu" action close_action
        key "K_ESCAPE" action close_action
    key "K_LEFT" action Function(investigation_scroll_timeline, timeline_adjustment, -1)
    key "K_RIGHT" action Function(investigation_scroll_timeline, timeline_adjustment, 1)

    fixed:
        add Solid("#F34E67") xpos 58 ypos 24 xsize 4 ysize 68
        text "KAMI'S DESIRES":
            xpos 88 ypos 22
            size 38 color "#F3F6FA" font "fonts/Rajdhani-SemiBold.ttf" kerning 5
        text "DOSSIER D'ENQUÊTE":
            xpos 90 ypos 70
            size 15 color "#8CA2B6" font "fonts/Rajdhani-SemiBold.ttf" kerning 6
        add Solid("#5CD3FF55") xpos 60 ypos 109 xsize 455 ysize 1
        text "Tout ce que tu as vu. Tout ce qui reste à comprendre.":
            xpos 610 ypos 103
            size 20 color "#BAC8D3" italic True

        hbox:
            xpos 610 ypos 27 spacing 0
            textbutton "TOUT":
                xsize 145 ysize 55 text_size 14
                text_color ("#DFFBFF" if category == "all" else "#8192A5")
                text_font "fonts/Rajdhani-SemiBold.ttf"
                background Solid("#102131E8")
                hover_background Solid("#163447EE")
                selected_background Solid("#173B4DEE")
                selected (category == "all")
                action [SetScreenVariable("category", "all"), SetScreenVariable("selected", None), Function(timeline_adjustment.change, 0)]
            for cid, label, color in INVESTIGATION_CATEGORIES:
                textbutton label:
                    xsize 150 ysize 55 text_size 13
                    text_color ("#EAF8FF" if category == cid else "#8192A5")
                    text_font "fonts/Rajdhani-SemiBold.ttf"
                    background Solid("#0B1422E8")
                    hover_background Solid(color + "25")
                    selected_background Solid(color + "38")
                    selected (category == cid)
                    action [SetScreenVariable("category", cid), SetScreenVariable("selected", None), Function(timeline_adjustment.change, 0)]

        $ visible_entries = investigation_entries(None if category == "all" else category)
        viewport:
            id "investigation_timeline"
            xpos 76 ypos 156
            xsize 1768 ysize 750
            xadjustment timeline_adjustment
            draggable True
            mousewheel "horizontal"

            hbox:
                spacing 0
                null width 18
                for index, pair in enumerate(visible_entries):
                    $ eid, entry = pair
                    $ col = investigation_category_color(entry["category"])
                    fixed at investigation_timeline_card_in(min(index * 0.035, 0.35)):
                        xsize 530 ysize 740

                        add Solid("#294158AA") xpos 0 ypos 355 xsize 530 ysize 2
                        add Solid(col + "60") xpos 0 ypos 354 xsize 530 ysize 4

                        if index % 2 == 0:
                            use _investigation_evidence_card(eid, entry, selected == eid, SetScreenVariable("selected", eid), 15, 4)
                            add Solid(col) xpos 278 ypos 288 xsize 3 ysize 67
                        else:
                            add Solid(col) xpos 278 ypos 357 xsize 3 ysize 65
                            use _investigation_evidence_card(eid, entry, selected == eid, SetScreenVariable("selected", eid), 15, 418)

                        add Solid("#07111E") xpos 262 ypos 338 xsize 35 ysize 35
                        add Solid(col) xpos 268 ypos 344 xsize 23 ysize 23
                        add Solid("#D9F8FF") xpos 276 ypos 352 xsize 7 ysize 7
                        text entry["day"] xpos 248 ypos 315 size 15 color col bold True font "fonts/Rajdhani-SemiBold.ttf"
                null width 18

        textbutton "‹":
            xpos 24 ypos 488 xsize 48 ysize 78 text_size 48 text_color "#D9F8FF"
            background Solid("#07111EDB") hover_background Solid("#5CD3FF38")
            action Function(investigation_scroll_timeline, timeline_adjustment, -1)
        textbutton "›":
            xpos 1848 ypos 488 xsize 48 ysize 78 text_size 48 text_color "#D9F8FF"
            background Solid("#07111EDB") hover_background Solid("#5CD3FF38")
            action Function(investigation_scroll_timeline, timeline_adjustment, 1)

        frame:
            xpos 392 ypos 958 xsize 1136 ysize 82
            padding (22, 16)
            background Solid("#07111EDB")
        bar:
            xpos 430 ypos 991 xsize 1060 ysize 16
            adjustment timeline_adjustment
            left_bar Solid("#47D9F0")
            right_bar Solid("#26384A")
            thumb Solid("#DDFBFF")
            thumb_offset 6
        text "J1" xpos 407 ypos 986 size 14 color "#8397AA" font "fonts/Rajdhani-SemiBold.ttf"
        text "J20" xpos 1494 ypos 986 size 14 color "#8397AA" font "fonts/Rajdhani-SemiBold.ttf"
        text "FRISE CHRONOLOGIQUE  ·  [len(visible_entries)] ÉLÉMENTS" xpos 720 ypos 936 size 13 color "#70879B" kerning 2 font "fonts/Rajdhani-SemiBold.ttf"

        if selected and investigation_has(selected):
            $ detail = INVESTIGATION_ENTRIES[selected]
            $ detail_col = investigation_category_color(detail["category"])
            button:
                xfill True yfill True
                padding (0, 0)
                background Solid("#01040ACF")
                action SetScreenVariable("selected", None)
            fixed at investigation_detail_in:
                xpos 420 ypos 220 xsize 1080 ysize 620
                add Transform("images/hud/investigation/ui/investigation_card_paper.png", xysize=(1080, 608)) xpos 0 ypos 6
                add investigation_evidence_image(selected) xpos 72 ypos 94 xsize 410 ysize 410
                add Solid("#6B554655") xpos 520 ypos 90 xsize 2 ysize 420
                text detail["day"] xpos 565 ypos 90 size 25 color "#17202B" bold True font "fonts/Rajdhani-SemiBold.ttf"
                text detail["title"] xpos 565 ypos 132 xmaximum 430 size 36 color "#101721" bold True font "fonts/Rajdhani-SemiBold.ttf"
                add Solid(detail_col) xpos 565 ypos 230 xsize 390 ysize 34
                text investigation_category_label(detail["category"]) xpos 578 ypos 236 size 15 color "#07121A" bold True kerning 2 font "fonts/Rajdhani-SemiBold.ttf"
                text detail["desc"] xpos 565 ypos 292 xmaximum 405 size 22 color "#28303A" line_spacing 5 font "fonts/Barlow-Light.ttf"
                text "ORIGINE  ·  [detail['origin']]" xpos 565 ypos 422 xmaximum 410 size 14 color "#665A50" kerning 1 font "fonts/Rajdhani-SemiBold.ttf"
                text "STATUT  ·  [detail['status']]" xpos 565 ypos 454 xmaximum 410 size 14 color detail_col bold True kerning 1 font "fonts/Rajdhani-SemiBold.ttf"
                $ related = [link for link in investigation_links if selected in link]
                if related:
                    $ names = [INVESTIGATION_ENTRIES[x]["title"] for link in related for x in link if x != selected]
                    text "CONNEXIONS  ·  [', '.join(names)]" xpos 565 ypos 495 xmaximum 410 size 13 color "#665A50" font "fonts/Rajdhani-SemiBold.ttf"
                textbutton "×":
                    xpos 995 ypos 38 xsize 48 ysize 48 text_size 34 text_color "#17202B"
                    background Solid("#EEE0C644") hover_background Solid(detail_col + "44")
                    action SetScreenVariable("selected", None)

        textbutton "×\nFERMER":
            xpos 1830 ypos 20 xsize 70 ysize 92
            text_size 15 text_color "#A9EDFF" text_align 0.5
            text_font "fonts/Rajdhani-SemiBold.ttf"
            background Solid("#071522E8") hover_background Solid("#5CD3FF38")
            action close_action


screen investigation_video(sequence="kael_photo", background="bg_chambre", alarming=False):
    modal True
    zorder 170
    default frame_index = 0
    default playing = False
    default speed = 1
    default zoom_level = 1.0
    default found = list(investigation_video_findings.get(sequence, []))

    $ total_frames = 24
    $ timestamp = ("21:17:%02d" if sequence == "kael_photo" else "02:14:%02d") % frame_index
    $ required = ["photo", "lips"] if sequence == "kael_photo" else ["entry", "drawing", "look"]
    $ complete = all(x in found for x in required)

    if playing:
        timer (0.45 / float(speed)) repeat True action SetScreenVariable("frame_index", min(total_frames, frame_index + 1))

    add Solid("#010407")
    frame:
        xalign 0.5 yalign 0.43 xsize 1500 ysize 790
        background Solid("#08111B") padding (18, 18)
        fixed:
            add Transform(background, zoom=zoom_level) xpos 0 ypos 0 xsize 1464 ysize 650
            add Solid("#00131CA8") xpos 0 ypos 0 xsize 1464 ysize 62
            text ("ARCHIVE // CHAMBRE KAEL" if sequence == "kael_photo" else "ARCHIVE // CHAMBRE NOAM") xpos 22 ypos 17 size 22 color ("#FF6B8A" if alarming else "#5CD3FF")
            text "REC  [timestamp]" xpos 1220 ypos 17 size 21 color "#FF6B8A"
            add Solid("#5CD3FF18") xpos 0 ypos 90 xsize 1464 ysize 1

            if sequence == "kael_photo":
                if frame_index >= 5:
                    textbutton "◎ CADRE PHOTO":
                        xpos 260 ypos 300 xsize 220 ysize 62
                        text_size 17 text_color "#DFF8FF"
                        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF45")
                        action [SetScreenVariable("found", found + ([] if "photo" in found else ["photo"])), Function(investigation_video_note, sequence, "photo", "video_kael")]
                if frame_index >= 8:
                    textbutton "◎ PRISE / MAINS":
                        xpos 610 ypos 390 xsize 220 ysize 62
                        text_size 17 text_color "#DFF8FF"
                        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF45")
                        action [SetScreenVariable("found", found + ([] if "grip" in found else ["grip"])), Function(investigation_video_note, sequence, "grip")]
                if frame_index >= 13:
                    textbutton "◎ REGARD CAMÉRA":
                        xpos 880 ypos 210 xsize 230 ysize 62
                        text_size 17 text_color "#DFF8FF"
                        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF45")
                        action [SetScreenVariable("found", found + ([] if "camera" in found else ["camera"])), Function(investigation_video_note, sequence, "camera")]
                if frame_index >= 17:
                    textbutton "◎ LÈVRES":
                        xpos 850 ypos 285 xsize 170 ysize 58
                        text_size 17 text_color "#FFFFFF"
                        background Solid("#FF6B8A28") hover_background Solid("#FF6B8A55")
                        action [SetScreenVariable("found", found + ([] if "lips" in found else ["lips"])), Function(investigation_video_note, sequence, "lips", "levres_kael")]
            else:
                if frame_index >= 4:
                    textbutton "◎ ENTRÉE DIRECTE":
                        xpos 190 ypos 245 xsize 240 ysize 62
                        text_size 17 text_color "#FFFFFF"
                        background Solid("#FF6B8A22") hover_background Solid("#FF6B8A55")
                        action [SetScreenVariable("found", found + ([] if "entry" in found else ["entry"])), Function(investigation_video_note, sequence, "entry")]
                if frame_index >= 10:
                    textbutton "◎ DESSIN":
                        xpos 760 ypos 330 xsize 170 ysize 62
                        text_size 17 text_color "#FFFFFF"
                        background Solid("#FF6B8A22") hover_background Solid("#FF6B8A55")
                        action [SetScreenVariable("found", found + ([] if "drawing" in found else ["drawing"])), Function(investigation_video_note, sequence, "drawing", "video_noam")]
                if frame_index >= 16:
                    textbutton "◎ REGARD VERS LE LIT":
                        xpos 930 ypos 235 xsize 270 ysize 62
                        text_size 17 text_color "#FFFFFF"
                        background Solid("#FF6B8A22") hover_background Solid("#FF6B8A55")
                        action [SetScreenVariable("found", found + ([] if "look" in found else ["look"])), Function(investigation_video_note, sequence, "look")]

            # Timeline et commandes.
            bar value ScreenVariableValue("frame_index", total_frames) xpos 80 ypos 680 xsize 1040 ysize 18 left_bar Solid("#5CD3FF") right_bar Solid("#18303D")
            textbutton ("PAUSE" if playing else "LECTURE") xpos 80 ypos 716 xsize 150 ysize 42 action ToggleScreenVariable("playing")
            textbutton "◀ IMAGE" xpos 245 ypos 716 xsize 140 ysize 42 action SetScreenVariable("frame_index", max(0, frame_index - 1))
            textbutton "IMAGE ▶" xpos 400 ypos 716 xsize 140 ysize 42 action SetScreenVariable("frame_index", min(total_frames, frame_index + 1))
            textbutton ("VITESSE x%d" % speed) xpos 555 ypos 716 xsize 160 ysize 42 action SetScreenVariable("speed", 2 if speed == 1 else (4 if speed == 2 else 1))
            textbutton ("ZOOM x%.2g" % zoom_level) xpos 730 ypos 716 xsize 150 ysize 42 action SetScreenVariable("zoom_level", 1.25 if zoom_level == 1.0 else (1.5 if zoom_level == 1.25 else 1.0))
            text "OBSERVÉS : [len(found)]" xpos 900 ypos 726 size 16 color "#8FAAB8"
            textbutton ("CONCLURE" if complete else "ANALYSE INCOMPLÈTE"):
                xpos 1160 ypos 690 xsize 280 ysize 68
                text_size 17 text_color ("#071017" if complete else "#607582")
                background Solid("#5CD3FF" if complete else "#15232B")
                hover_background Solid("#8AE5FF" if complete else "#15232B")
                sensitive complete
                action Return(found)


screen investigation_image_inspection(sequence="juliette_copy"):
    modal True
    zorder 170
    default zoom_level = 1.0
    default pan_x = 0
    default pan_y = 0
    default found = list(investigation_inspection_findings.get(sequence, []))
    $ complete = "scar" in found

    add Solid("#020509")
    frame:
        xalign 0.5 yalign 0.47 xsize 1540 ysize 900 background Solid("#09121B") padding (20, 20)
        fixed:
            text "INSPECTION // COPIE DU DESSIN" xpos 10 ypos 4 size 27 color "#5CD3FF"
            text "ZOOM [int(zoom_level * 100)] %" xpos 1250 ypos 10 size 17 color "#829BAA"
            frame:
                xpos 20 ypos 60 xsize 1120 ysize 760 background Solid("#030609") padding (0, 0)
                fixed:
                    add Transform("images/minigame/sept_differences/dessin_juliette.png", zoom=zoom_level, xoffset=pan_x, yoffset=pan_y) xalign 0.5 yalign 0.5
                    textbutton "◎ TRAIT REPASSÉ":
                        xpos 220 ypos 530 xsize 210 ysize 54 text_size 15
                        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF44")
                        action [SetScreenVariable("found", found + ([] if "line" in found else ["line"])), Function(investigation_inspection_note, sequence, "line")]
                    textbutton "◎ OMBRE DU VISAGE":
                        xpos 700 ypos 470 xsize 230 ysize 54 text_size 15
                        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF44")
                        action [SetScreenVariable("found", found + ([] if "shadow" in found else ["shadow"])), Function(investigation_inspection_note, sequence, "shadow")]
                    if zoom_level >= 1.2:
                        textbutton "◎ MARQUE AU SOURCIL":
                            xpos 535 ypos 245 xsize 245 ysize 58 text_size 16 text_color "#FFFFFF"
                            background Solid("#FF6B8A28") hover_background Solid("#FF6B8A5C")
                            action [SetScreenVariable("found", found + ([] if "scar" in found else ["scar"])), Function(investigation_inspection_note, sequence, "scar", "cicatrice_juliette")]
            vbox:
                xpos 1175 ypos 92 spacing 14
                text "OUTILS" size 16 color "#6E93A8"
                textbutton "+  ZOOM" xsize 300 ysize 52 action SetScreenVariable("zoom_level", min(1.5, zoom_level + 0.25))
                textbutton "−  ZOOM" xsize 300 ysize 52 action SetScreenVariable("zoom_level", max(0.75, zoom_level - 0.25))
                hbox:
                    spacing 8
                    textbutton "←" xsize 68 ysize 44 action SetScreenVariable("pan_x", pan_x - 70)
                    textbutton "CENTRE" xsize 140 ysize 44 action [SetScreenVariable("pan_x", 0), SetScreenVariable("pan_y", 0)]
                    textbutton "→" xsize 68 ysize 44 action SetScreenVariable("pan_x", pan_x + 70)
                hbox:
                    spacing 8
                    textbutton "↑" xsize 142 ysize 44 action SetScreenVariable("pan_y", pan_y - 60)
                    textbutton "↓" xsize 142 ysize 44 action SetScreenVariable("pan_y", pan_y + 60)
                null height 20
                text "DIFFÉRENCES" size 16 color "#6E93A8"
                text "[len(found)] repérée(s)" size 23 color "#D7E8EF"
                if complete:
                    frame at inv_pulse:
                        xsize 300 background Solid("#FF6B8A22") padding (14, 12)
                        text "DÉTAIL IMPOSSIBLE" size 18 color "#FF8DA4"
            textbutton ("REFERMER LE CAHIER" if complete else "INSPECTER DAVANTAGE"):
                xpos 1175 ypos 748 xsize 300 ysize 64
                text_size 16 text_color ("#071017" if complete else "#607582")
                background Solid("#5CD3FF" if complete else "#15232B")
                sensitive complete action Return(found)


screen investigation_room_inspection():
    modal True
    zorder 170
    default found = []
    $ complete = "batteries" in found and "goumi" in found

    add "bg_cg046"
    add Solid("#00101866")
    text "INSPECTION LIBRE // SALLE TECHNIQUE" xpos 50 ypos 35 size 27 color "#5CD3FF"
    text "Les détails secondaires peuvent être laissés de côté." xpos 50 ypos 76 size 16 color "#9AB1BE"

    textbutton "◎ BATTERIES":
        xpos 310 ypos 660 xsize 220 ysize 58
        background Solid("#5CD3FF20") hover_background Solid("#5CD3FF55")
        action [SetScreenVariable("found", found + ([] if "batteries" in found else ["batteries"])), Function(investigation_add, "batteries_retrouvees")]
    textbutton "◎ GOUMI DÉMONTÉ":
        xpos 1080 ypos 440 xsize 260 ysize 58
        background Solid("#5CD3FF20") hover_background Solid("#5CD3FF55")
        action [SetScreenVariable("found", found + ([] if "goumi" in found else ["goumi"])), Function(investigation_add, "goumi_demonte")]
    textbutton "◎ OUTILS":
        xpos 690 ypos 700 xsize 180 ysize 52
        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF44")
        action SetScreenVariable("found", found + ([] if "tools" in found else ["tools"]))
    textbutton "◎ STATIONS":
        xpos 1290 ypos 265 xsize 190 ysize 52
        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF44")
        action SetScreenVariable("found", found + ([] if "stations" in found else ["stations"]))
    textbutton "◎ CONDUIT LATÉRAL":
        xpos 120 ypos 330 xsize 260 ysize 52
        background Solid("#5CD3FF18") hover_background Solid("#5CD3FF44")
        action SetScreenVariable("found", found + ([] if "duct" in found else ["duct"]))
    textbutton ("POURSUIVRE" if complete else "TROUVER LES ÉLÉMENTS MAJEURS"):
        xpos 1450 ypos 960 xsize 410 ysize 70
        text_size 17 text_color ("#071017" if complete else "#607582")
        background Solid("#5CD3FF" if complete else "#15232B")
        sensitive complete action Return(found)


screen conduit_exploration(mode="survey"):
    modal True
    zorder 170
    default step = 0
    default route = []
    default false_alarm = False
    $ stressful = mode == "chase"
    $ survey_choices = [
        [("SUIVRE LES TRACES", "traces"), ("OBSERVER LA GRILLE", "grille")],
        [("BRANCHE VERS LES CHAMBRES", "chambres"), ("DESCENTE TECHNIQUE", "technique")],
        [("MARQUER LE CROISEMENT", "carte"), ("ÉCOUTER DERRIÈRE LA TÔLE", "ecoute")],
    ]
    $ chase_choices = [
        [("BRUIT À GAUCHE", "gauche"), ("SOUFFLE À DROITE", "droite")],
        [("ACCÉLÉRER", "vite"), ("COUPER LA LAMPE", "ombre")],
        [("GRILLE ENTROUVERTE", "goumi"), ("PAS DERRIÈRE MOI", "retour")],
    ]
    $ choices = chase_choices if stressful else survey_choices
    $ finished = step >= len(choices)

    add "bg_conduit_reseau"
    add Solid("#02070CAA" if not stressful else "#16000699")
    if stressful:
        add Solid("#FF204018") at inv_pulse

    frame:
        xpos 45 ypos 40 xsize 570 ysize 280 background Solid("#06121DEB") padding (22, 18)
        vbox:
            spacing 10
            text ("POURSUITE // SIGNAL INSTABLE" if stressful else "CARTOGRAPHIE // RÉSEAU TECHNIQUE") size 24 color ("#FF6B8A" if stressful else "#5CD3FF")
            text ("La chose peut être devant. Ou derrière." if stressful else "Choisissez un embranchement. Aucun détour ne bloque la progression.") size 16 color "#B2C5CE" xmaximum 520
            text "PROGRESSION  [min(step, len(choices))] / [len(choices)]" size 18 color "#E7F6FC"
            hbox:
                spacing 8
                for index in range(len(choices)):
                    add Solid(("#FF6B8A" if stressful else "#5CD3FF") if index < step else "#28404D") xsize 150 ysize 8

    if not finished:
        frame:
            xalign 0.5 ypos 690 xsize 1100 ysize 260 background Solid("#03090EEF") padding (26, 24)
            vbox:
                spacing 18
                text ("UN BRUIT SE DÉPLACE" if stressful else "LE CONDUIT SE DIVISE") xalign 0.5 size 25 color "#EAF8FF"
                hbox:
                    xalign 0.5 spacing 28
                    for label, value in choices[step]:
                        textbutton label:
                            xsize 470 ysize 92 text_size 21
                            text_color "#F2FBFF"
                            background Solid("#132735") hover_background Solid(("#7A1730" if stressful else "#16445A"))
                            action [SetScreenVariable("route", route + [value]), SetScreenVariable("step", step + 1), Function(investigation_unlock_map, value)]
    else:
        frame:
            xalign 0.5 ypos 730 xsize 760 ysize 180 background Solid("#06121DEE") padding (30, 24)
            vbox:
                xalign 0.5 spacing 18
                text ("LA GRILLE EST DEVANT VOUS" if stressful else "CARTE PARTIELLE ENREGISTRÉE") xalign 0.5 size 26 color ("#FF8CA3" if stressful else "#5CD3FF")
                textbutton ("DESCENDRE DANS LA SALLE" if stressful else "REVENIR VERS MARA"):
                    xalign 0.5 xsize 430 ysize 64 text_size 18
                    background Solid("#5CD3FF") text_color "#061018"
                    action Return(route)


screen objection_protocol(statement, correct_evidence, relevant_evidence=()):
    modal True
    zorder 190
    default selected = None
    $ available = investigation_entries()

    add Solid("#020509F5")
    add Solid("#5CD3FF18") at inv_pulse
    frame:
        xalign 0.5 yalign 0.5 xsize 1600 ysize 880 background Solid("#07121CF8") padding (28, 24)
        fixed:
            text "OBJECTION PROTOCOL // CONTRADICTION" xpos 0 ypos 0 size 30 color "#5CD3FF"
            frame:
                xpos 0 ypos 58 xsize 1544 ysize 118 background Solid("#151B25") padding (24, 18)
                text "« [statement] »" size 26 color "#F4F9FB" xmaximum 1460
            text "SÉLECTIONNER UN ÉLÉMENT DU DOSSIER" xpos 0 ypos 198 size 17 color "#7997A7"
            frame:
                xpos 0 ypos 235 xsize 1000 ysize 550 background Solid("#03090E") padding (12, 12)
                viewport:
                    mousewheel True draggable True scrollbars "vertical"
                    vbox:
                        spacing 8
                        for eid, entry in available:
                            button:
                                xsize 940 ysize 76
                                background Solid("#0D1B27") hover_background Solid("#5CD3FF22") selected_background Solid("#5CD3FF38")
                                selected (selected == eid) action SetScreenVariable("selected", eid)
                                vbox:
                                    xpos 14 ypos 9 spacing 2
                                    text entry["title"] size 18 color "#E8F5FA"
                                    text "[entry['day']] // [entry['status']]" size 13 color "#7392A3"
            frame:
                xpos 1030 ypos 235 xsize 514 ysize 550 background Solid("#091722") padding (22, 20)
                vbox:
                    spacing 18
                    text "ÉVALUATION" size 19 color "#6E93A8"
                    if selected:
                        $ chosen = INVESTIGATION_ENTRIES[selected]
                        text chosen["title"] size 26 color "#EAF8FF"
                        text chosen["desc"] size 18 color "#BDD0D9" xmaximum 450
                    else:
                        text "Le dossier contient des faits incompatibles. Aucun n'est automatiquement plus vrai que l'autre." size 18 color "#7893A1" xmaximum 450
            textbutton "LAISSER PASSER":
                xpos 0 ypos 812 xsize 250 ysize 48 text_size 16 action Return((None, "impossible"))
            textbutton "CONFRONTER":
                xpos 1280 ypos 802 xsize 264 ysize 58 text_size 18
                sensitive (selected is not None)
                background Solid("#5CD3FF") text_color "#061018"
                action Return((selected, objection_evaluate(selected, correct_evidence, relevant_evidence)))


label investigation_open_dossier:
    call screen investigation_dossier
    return

label investigation_video_run(sequence="kael_photo", background="bg_chambre", alarming=False):
    call screen investigation_video(sequence=sequence, background=background, alarming=alarming)
    return

label investigation_image_run(sequence="juliette_copy"):
    call screen investigation_image_inspection(sequence=sequence)
    return

label investigation_conduit_run(mode="survey"):
    call screen conduit_exploration(mode=mode)
    return

label investigation_room_run:
    call screen investigation_room_inspection
    return

label objection_protocol_run(statement, correct_evidence, relevant_evidence=()):
    call screen objection_protocol(statement, correct_evidence, relevant_evidence)
    return
