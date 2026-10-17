# =============================================================================
# DOSSIER DE VOTE — Propositions & arguments par chapitre
# =============================================================================
# Débloquer un argument :   $ unlock_dossier_arg("id_argument")
# Débloquer une proposition : $ unlock_dossier_prop("id_proposition")
# Débloquer un chapitre : $ unlock_dossier_chapter(2)
# =============================================================================

default dossier_current_chapter = 1
default dossier_unlocked_chapters = [1]
default dossier_unlocked_args = {}
default dossier_unlocked_props = ["p1_vote_commerce"]

init python:

    # ------------------------------------------------------------------
    # CATÉGORIES D'ARGUMENTS
    # ------------------------------------------------------------------
    DOSSIER_ARG_CATS = {
        "soutien":     {"label": "SOUTIEN",     "color": "#6BD98A", "icon": "hud/dossier/ic_handshake.png"},
        "prudence":    {"label": "PRUDENCE",    "color": "#F0A835", "icon": "hud/dossier/ic_shield_alert.png"},
        "information": {"label": "INFORMATION", "color": "#5CD3FF", "icon": "hud/dossier/ic_box.png"},
    }

    # ------------------------------------------------------------------
    # CHAPITRES  (les chapitres > courant sont masqués)
    # ------------------------------------------------------------------
    DOSSIER_CHAPTERS = [
        {"id": 1, "title": "CHAPITRE 1", "props": ["p1_vote_commerce"]},
        {"id": 2, "title": "CHAPITRE 2", "props": ["p2_vote_deplacements"]},
        {"id": 3, "title": "CHAPITRE 3", "props": ["p3_vote_regroupements"]},
        {"id": 4, "title": "CHAPITRE 4", "props": ["p4_vote_brouilleurs"]},
        {"id": 5, "title": "CHAPITRE 5", "props": ["p5_vote_archive"]},
    ]

    # Les succès sont rattachés au chapitre pour son taux de complétion.
    DOSSIER_CHAPTER_SUCCES = {
        1: ["succes001", "succes002", "succes003", "succes004"],
        2: [],
        3: [],
        4: [],
        5: [],
    }

    # ------------------------------------------------------------------
    # PROPOSITIONS
    # ------------------------------------------------------------------
    DOSSIER_PROPOSITIONS = {
        "p1_vote_commerce": {"chapter": 1, "num": 1,
            "title": "ça serait bien qu'on réautorise\nle commerce comme avant.",
            "formulation": "Le Conclave autorise le transport, la vente et l'échange de marchandises entre les districts, sous réserve du respect des règles de sécurité et des quotas définis par l'administration.",
            "args": ["approvisionnement", "rationnement", "orbite", "derogations_complexes", "valeur_travail", "monde_avant", "enonce_precis", "echanges_discrets"]},
        "p2_vote_deplacements": {"chapter": 2, "num": 1,
            "title": "Autoriser les déplacements de personnes\nentre les districts",
            "formulation": "Autoriser les déplacements de personnes entre les districts.",
            "args": ["p2_formulation", "p2_orbite", "p2_cooperation", "p2_guerres",
                     "p2_controles", "p2_familles", "p2_frontiere_limen", "p2_exode"]},
        "p3_vote_regroupements": {"chapter": 3, "num": 1,
            "title": "Autoriser les regroupements\nde plus de vingt personnes",
            "formulation": "Autoriser les regroupements de plus de vingt personnes sous réserve d'une déclaration préalable.",
            "args": ["p3_declaration", "p3_familles", "p3_reseaux", "p3_campements"]},
        "p4_vote_brouilleurs": {"chapter": 4, "num": 1,
            "title": "Autoriser les dispositifs\nde brouillage",
            "formulation": "Autoriser ou interdire les dispositifs de brouillage individuels.",
            "args": ["p4_intimite", "p4_preuves", "p4_delai", "p4_voleur"]},
        "p5_vote_archive": {"chapter": 5, "num": 1,
            "title": "Ouvrir toutes les archives\nd'ARCHIVE aux citoyens",
            "formulation": "Rendre consultables par tous les citoyens toutes les informations détenues par ARCHIVE.",
            "args": ["p5_transparence", "p5_donnees_privees", "p5_validation", "p5_index_complet"]},
    }

    # ------------------------------------------------------------------
    # ARGUMENTS
    # ------------------------------------------------------------------
    DOSSIER_ARGS = {
        "approvisionnement": {"cat": "prudence", "title": "Inégalités entre les districts",
            "desc": "Les districts n'affrontent ni les mêmes pénuries ni les mêmes chances d'accéder aux biens.",
            "source": "LYSA ET ELIAS"},
        "rationnement": {"cat": "information", "title": "Bons de rationnement",
            "desc": "Les demandes officielles et les bons structurent déjà l'accès aux biens essentiels.",
            "source": "KAEL"},
        "orbite": {"cat": "prudence", "title": "Risque de dépressurisation",
            "desc": "Sur Orbite, une sanction qui perce une coque peut condamner tout un module.",
            "source": "KAEL"},
        "derogations_complexes": {"cat": "information", "title": "Dérogations trop complexes",
            "desc": "Obtenir une nourriture originale ou un objet utile exige une dérogation disproportionnée.",
            "source": "ELEN"},
        "valeur_travail": {"cat": "soutien", "title": "Valeur du travail",
            "desc": "L'entraide protège chacun, mais elle repose sur la contribution de tous ceux qui peuvent travailler.",
            "source": "SAEL"},
        "monde_avant": {"cat": "soutien", "title": "Le monde d'avant",
            "desc": "Julian présente l'avant-Kami comme une preuve que la circulation libre peut exister.",
            "source": "JULIAN"},
        "enonce_precis": {"cat": "information", "title": "L'énoncé exact",
            "desc": "La formulation exacte du vote reste le point décisif pour évaluer ses conséquences.",
            "source": "CAFÉTÉRIA"},
        "echanges_discrets": {"cat": "information", "title": "Échanges discrets déjà actifs",
            "desc": "Des échanges informels existent déjà dans la salle de stockage. Les ignorer ne les fait pas disparaître.",
            "source": "SALLE DE STOCKAGE"},
        "p2_formulation": {"cat": "information", "title": "Portée du texte",
            "desc": "Un vote pour ouvre librement les frontières ; un vote contre conserve les restrictions actuelles.",
            "source": "ANNONCE DE KAMI"},
        "p2_orbite": {"cat": "information", "title": "Cas particulier d'Orbite",
            "desc": "Orbite ne possède pas de frontières terrestres comparables et subira autrement les effets du vote.",
            "source": "KAEL"},
        "p2_cooperation": {"cat": "soutien", "title": "Coopération entre districts",
            "desc": "La circulation permettrait aux districts de travailler ensemble et de partager leurs ressources.",
            "source": "JULIAN"},
        "p2_guerres": {"cat": "prudence", "title": "Conflits encore ouverts",
            "desc": "Ouvrir une frontière n'efface ni les anciennes guerres ni ceux qui souhaitent les reprendre.",
            "source": "LYSA"},
        "p2_controles": {"cat": "information", "title": "Ouverture progressive",
            "desc": "Des contrôles ou une ouverture par étapes pourraient limiter les risques si le texte l'autorise.",
            "source": "TOMAS"},
        "p2_familles": {"cat": "soutien", "title": "Familles séparées",
            "desc": "La réouverture permettrait à des proches séparés par les frontières de se retrouver.",
            "source": "NOAM ET SAEL"},
        "p2_frontiere_limen": {"cat": "soutien", "title": "Morts à la frontière de Limen",
            "desc": "Les restrictions actuelles tuent déjà ceux qui tentent de franchir la frontière de Limen.",
            "source": "RYN"},
        "p2_exode": {"cat": "prudence", "title": "Exode des plus vulnérables",
            "desc": "Une ouverture brutale pourrait abandonner ceux que les autres districts refusent d'accueillir.",
            "source": "SAEL"},
        "p3_declaration": {"cat": "information", "title": "Déclaration préalable",
            "desc": "Lieu, date, objet et identité des organisateurs devraient être transmis avant toute réunion.",
            "source": "ANNONCE DE KAMI"},
        "p3_familles": {"cat": "soutien", "title": "Communautés et familles",
            "desc": "Les regroupements autorisés permettraient aux proches séparés de se retrouver et de s'organiser.",
            "source": "RYN"},
        "p3_reseaux": {"cat": "prudence", "title": "Risque de recrutement",
            "desc": "Des réseaux pourraient utiliser ces rassemblements pour recruter ou dissimuler leurs activités.",
            "source": "SAEL"},
        "p3_campements": {"cat": "information", "title": "Campements déjà formés",
            "desc": "Autoriser les futurs groupes ne régularise pas forcément ceux qui existent déjà.",
            "source": "NYRA"},
        "p4_intimite": {"cat": "soutien", "title": "Droit à l'intimité",
            "desc": "Les brouilleurs empêchent une surveillance constante dans les espaces privés.",
            "source": "MARA"},
        "p4_preuves": {"cat": "prudence", "title": "Preuves neutralisées",
            "desc": "Si chacun brouille les enregistrements, certains événements deviennent impossibles à prouver.",
            "source": "NYRA"},
        "p4_delai": {"cat": "information", "title": "Délai de sept jours",
            "desc": "Kami peut récupérer les vidéos brouillées, mais seulement après une semaine de délai.",
            "source": "LYSA"},
        "p4_voleur": {"cat": "prudence", "title": "Enquête sur les vols",
            "desc": "Le brouillage peut empêcher Kael d'identifier la personne qui a pris la photo de sa sœur.",
            "source": "KAEL"},
        "p5_transparence": {"cat": "soutien", "title": "Transparence publique",
            "desc": "L'accès aux rapports extérieurs et aux décisions de Kami rendrait enfin le système vérifiable.",
            "source": "NYRA ET NOAM"},
        "p5_donnees_privees": {"cat": "prudence", "title": "Toutes les informations",
            "desc": "Une ouverture totale peut aussi exposer des données privées ou dangereuses.",
            "source": "NYRA"},
        "p5_validation": {"cat": "information", "title": "Commandement V",
            "desc": "Toute information diffusée doit actuellement être validée par ARCHIVE.",
            "source": "KAMI"},
        "p5_index_complet": {"cat": "information", "title": "Synchronisation des index",
            "desc": "Le vote force temporairement les terminaux à charger les index complets d'ARCHIVE.",
            "source": "KAEL"},
    }

    # ------------------------------------------------------------------
    # Fonctions
    # ------------------------------------------------------------------
    def dossier_chapter(cid):
        for c in DOSSIER_CHAPTERS:
            if c["id"] == cid:
                return c
        return DOSSIER_CHAPTERS[0]

    def dossier_visible_chapters():
        unlocked = getattr(store, "dossier_unlocked_chapters", [1])
        return [c for c in DOSSIER_CHAPTERS if c["id"] in unlocked]

    def dossier_default_chapter():
        visible = dossier_visible_chapters()
        return visible[-1]["id"] if visible else 1

    def unlock_dossier_chapter(cid):
        if cid not in [c["id"] for c in DOSSIER_CHAPTERS]:
            return False
        changed = False
        # Débloquer un chapitre conserve toujours l'accès aux précédents,
        # y compris lors du chargement d'une ancienne sauvegarde incomplète.
        for chapter in DOSSIER_CHAPTERS:
            chapter_id = chapter["id"]
            if chapter_id <= cid and chapter_id not in store.dossier_unlocked_chapters:
                store.dossier_unlocked_chapters.append(chapter_id)
                changed = True
        if changed:
            store.dossier_unlocked_chapters.sort()
            store.dossier_current_chapter = cid
            renpy.restart_interaction()
            return True
        return False

    def dossier_prop(pid):
        return DOSSIER_PROPOSITIONS.get(pid, {})

    def dossier_prop_first_of_chapter(cid):
        return dossier_chapter(cid)["props"][0]

    def dossier_prop_available(pid):
        p = dossier_prop(pid)
        if not p or p.get("chapter", 99) not in getattr(store, "dossier_unlocked_chapters", [1]):
            return False
        # 1re proposition du chapitre toujours dispo ; les autres sur déblocage
        if pid == dossier_prop_first_of_chapter(p["chapter"]):
            return True
        return pid in store.dossier_unlocked_props

    def unlock_dossier_prop(pid):
        if pid in DOSSIER_PROPOSITIONS and pid not in store.dossier_unlocked_props:
            store.dossier_unlocked_props.append(pid)
            renpy.restart_interaction()
            return True
        return False

    def dossier_arg_unlocked(aid):
        if persistent.unlocked_dossier_args is None:
            persistent.unlocked_dossier_args = []
        return (aid in getattr(store, "j2_vote_arguments", [])
                or aid in persistent.unlocked_dossier_args
                or bool(store.dossier_unlocked_args.get(aid, False)))

    def unlock_dossier_arg(aid):
        if aid not in DOSSIER_ARGS:
            return False
        if persistent.unlocked_dossier_args is None:
            persistent.unlocked_dossier_args = []
        changed = False
        if not store.dossier_unlocked_args.get(aid, False):
            store.dossier_unlocked_args[aid] = True
            changed = True
        if aid not in persistent.unlocked_dossier_args:
            persistent.unlocked_dossier_args.append(aid)
            changed = True
        if changed:
            renpy.save_persistent()
            renpy.restart_interaction()
            return True
        return False

    def dossier_prop_args(pid):
        return dossier_prop(pid).get("args", [])

    def dossier_prop_total(pid):
        return len(dossier_prop_args(pid))

    def dossier_prop_unlocked_count(pid):
        return sum(1 for a in dossier_prop_args(pid) if dossier_arg_unlocked(a))

    def dossier_prop_complete(pid):
        t = dossier_prop_total(pid)
        return t > 0 and dossier_prop_unlocked_count(pid) == t

    def dossier_chapter_argument_ids(cid):
        argument_ids = []
        for pid in dossier_chapter(cid)["props"]:
            for aid in dossier_prop_args(pid):
                if aid not in argument_ids:
                    argument_ids.append(aid)
        return argument_ids

    def dossier_chapter_success_ids(cid):
        return list(DOSSIER_CHAPTER_SUCCES.get(cid, []))

    def dossier_chapter_progress(cid):
        argument_ids = dossier_chapter_argument_ids(cid)
        success_ids = dossier_chapter_success_ids(cid)
        arguments_done = sum(1 for aid in argument_ids if dossier_arg_unlocked(aid))
        successes_done = sum(1 for sid in success_ids if is_succes_unlocked(sid))
        total = len(argument_ids) + len(success_ids)
        done = arguments_done + successes_done
        percent = int(round(100.0 * done / total)) if total else 0
        return {
            "arguments_done": arguments_done,
            "arguments_total": len(argument_ids),
            "successes_done": successes_done,
            "successes_total": len(success_ids),
            "done": done,
            "total": total,
            "percent": percent,
        }

    def dossier_global_total():
        return sum(dossier_chapter_progress(c["id"])["total"] for c in dossier_visible_chapters())

    def dossier_global_unlocked():
        return sum(dossier_chapter_progress(c["id"])["done"] for c in dossier_visible_chapters())

    def dossier_global_percent():
        tot = dossier_global_total()
        return int(round(100.0 * dossier_global_unlocked() / tot)) if tot else 0

    def dossier_gauge_image(pct):
        step = int(round(pct / 5.0)) * 5
        step = max(0, min(100, step))
        return "hud/dossier/gauge_%d.png" % step

    def dossier_arg_cat(aid):
        return DOSSIER_ARG_CATS.get(DOSSIER_ARGS.get(aid, {}).get("cat", "information"), DOSSIER_ARG_CATS["information"])

transform dossier_tint(c):
    matrixcolor TintMatrix(c)


# =============================================================================
# ÉCRAN PRINCIPAL
# =============================================================================
screen vote_dossier():
    # Interface intégrée à la vitre inclinée de la tablette, comme tablet_profiles.
    modal True
    zorder 220

    default sel_chapter = dossier_default_chapter()
    default sel_prop = dossier_prop_first_of_chapter(dossier_default_chapter())
    $ back_to_tablet = [Hide("vote_dossier"), Show("tablet_home"), With(Dissolve(0.25))]
    $ restore_unlocked_arguments()
    if "day2_sync_argument_titles" in globals():
        $ day2_sync_argument_titles()

    key "K_ESCAPE" action back_to_tablet
    key "K_t" action back_to_tablet

    # Même fond, positionnement, rotation et animation que le menu Profil.
    add Solid("#01060bcc")
    add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080)

    fixed at messenger_panel_in, tablet_profile_plane:
        xysize (940, 560)
        clipping True
        add Solid("#020912f5")
        add Solid("#0b223144", ysize=56)
        add Solid("#5cd3ff99", ysize=2) ypos 55

        text "KAMI.CORE // DOSSIER DE VOTE":
            font "fonts/Barlow-Light.ttf"
            size 14 color "#5cd3ff" kerning 2.2
            xpos 18 ypos 18

        text "VOTES // {:02d}".format(len(dossier_visible_chapters())):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 14 color "#769aab"
            xpos 736 ypos 18

        textbutton "RETOUR":
            xpos 824 ypos 9 xsize 100 ysize 36
            padding (8, 4)
            background Fixed(Solid("#07131de8"), Solid("#5cd3ff", ysize=2, yalign=1.0))
            hover_background Fixed(Solid("#123249f5"), Solid("#86e2ff", ysize=3, yalign=1.0))
            text_font "fonts/Rajdhani-SemiBold.ttf"
            text_size 14 text_color "#9bc7d8" text_hover_color "#ffffff"
            text_xalign 0.5 text_yalign 0.5
            action back_to_tablet

        # Frise des votes réellement débloqués, dans l'ordre chronologique.
        frame:
            xpos 14 ypos 69 xsize 276 ysize 471 padding (0, 0)
            background Fixed(Solid("#081824ef"), Solid("#5cd3ff66", xsize=2))
            text "CHRONOLOGIE DES VOTES":
                xpos 14 ypos 11 size 16 color "#5cd3ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            add Solid("#294c5e") xpos 14 ypos 40 xsize 248 ysize 1

            viewport:
                xpos 6 ypos 48 xsize 262 ysize 405
                mousewheel True draggable True scrollbars "vertical"
                vbox:
                    spacing 0
                    for chapter in dossier_visible_chapters():
                        $ cid = chapter["id"]
                        $ chapter_pid = dossier_prop_first_of_chapter(cid)
                        $ chapter_prop = dossier_prop(chapter_pid)
                        button:
                            xsize 245 ysize 91
                            selected sel_chapter == cid
                            background (Solid("#15384c") if sel_chapter == cid else Solid("#00000000"))
                            hover_background Solid("#15384c99")
                            action [SetScreenVariable("sel_chapter", cid), SetScreenVariable("sel_prop", chapter_pid)]
                            fixed:
                                xysize (245, 91)
                                add Solid("#315a71") xpos 19 ypos 0 xsize 2 ysize 91
                                add Solid("#5cd3ff" if sel_chapter == cid else "#567b8d") xpos 12 ypos 18 xysize (16, 16)
                                add Solid("#0b1d2a") xpos 16 ypos 22 xysize (8, 8)
                                text "JOUR {:02d}  /  VOTE {:02d}".format(cid * 3, cid):
                                    xpos 42 ypos 10 size 14
                                    color ("#82e5ff" if sel_chapter == cid else "#8daebd")
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                text chapter_prop.get("title", "").replace("\\n", " "):
                                    xpos 42 ypos 34 xmaximum 189
                                    size 14 color "#e3f0f8"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    line_leading 1
                                add Solid("#27485a") xpos 40 ypos 90 xsize 190 ysize 1

        $ prop = dossier_prop(sel_prop)
        $ chapter_progress = dossier_chapter_progress(sel_chapter)
        $ percent = chapter_progress["percent"]
        $ unlocked_count = dossier_prop_unlocked_count(sel_prop)
        $ total_count = dossier_prop_total(sel_prop)

        # Proposition du vote sélectionné et synthèse de complétion.
        frame:
            xpos 305 ypos 69 xsize 619 ysize 174 padding (0, 0)
            background Fixed(Solid("#091924f4"), Solid("#5cd3ff77", ysize=2))
            text "PROPOSITION // VOTE {:02d}".format(sel_chapter):
                xpos 14 ypos 10 size 13 color "#5cd3ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1.5
            text prop.get("title", ""):
                xpos 14 ypos 32 xmaximum 435
                size 20 color "#effaff" font "fonts/Rajdhani-SemiBold.ttf"
                line_leading 1
            text "{:d}%".format(percent):
                xpos 524 ypos 22 xanchor 0.5 size 26 color "#5cd3ff"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "COMPLÉTION":
                xpos 479 ypos 57 size 12 color "#8cabbc"
                font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#284a5b") xpos 467 ypos 82 xsize 127 ysize 5
            add Solid("#5cd3ff") xpos 467 ypos 82 xsize int(127 * percent / 100.0) ysize 5

            add Solid("#244152") xpos 14 ypos 103 xsize 590 ysize 1
            text "FORMULATION":
                xpos 14 ypos 111 size 12 color "#5cd3ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            text prop.get("formulation", ""):
                xpos 14 ypos 130 xmaximum 587
                size 13 color "#c0d3de" font "fonts/Barlow-Light.ttf"
                line_leading 1

        # Le dossier conserve les arguments et leurs états de déblocage.
        frame:
            xpos 305 ypos 252 xsize 619 ysize 288 padding (0, 0)
            background Fixed(Solid("#081824f2"), Solid("#24495d", xsize=2))
            text "ARGUMENTS // {:02d} SUR {:02d} DÉCOUVERTS".format(unlocked_count, total_count):
                xpos 14 ypos 11 size 16 color "#5cd3ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            text "SUCCÈS : {} / {}".format(chapter_progress["successes_done"], chapter_progress["successes_total"]):
                xpos 443 ypos 15 size 12 color "#8fa8b8"
                font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#24495d") xpos 14 ypos 40 xsize 587 ysize 1

            viewport:
                xpos 12 ypos 49 xsize 593 ysize 221
                mousewheel True draggable True scrollbars "vertical"
                vbox:
                    spacing 7
                    for aid in dossier_prop_args(sel_prop):
                        $ unlocked = dossier_arg_unlocked(aid)
                        $ meta = dossier_arg_cat(aid)
                        $ arg = DOSSIER_ARGS.get(aid, {})
                        frame:
                            xsize 566
                            yminimum 76
                            padding (12, 8, 12, 8)
                            background Fixed(Solid("#102634" if unlocked else "#0b1822"), Solid(meta["color"] if unlocked else "#365061", xsize=3))
                            vbox:
                                spacing 2
                                hbox:
                                    spacing 9
                                    text (meta["label"] if unlocked else "VERROUILLÉ"):
                                        size 11 color (meta["color"] if unlocked else "#637b8b")
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                    text (arg.get("title", "") if unlocked else "Argument non découvert"):
                                        size 15 color ("#eaf4ff" if unlocked else "#647d8b")
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                text (arg.get("desc", "") if unlocked else "Explorez le Conclave pour découvrir cet argument."):
                                    size 12 color ("#b7cad8" if unlocked else "#637b8b")
                                    font "fonts/Barlow-Light.ttf" xmaximum 530
                                if unlocked and arg.get("source"):
                                    text "SOURCE : {}".format(arg["source"]):
                                        size 11 color meta["color"]
                                        font "fonts/Rajdhani-SemiBold.ttf"

# -----------------------------------------------------------------------------
# Onglet
# -----------------------------------------------------------------------------
screen dossier_tab(icon, label, color, active, act):
    button:
        xsize 156 ysize 64
        background (Frame(Solid("#0E2233"), 0, 0) if active else Frame(Solid("#0A141E"), 0, 0))
        hover_background Frame(Solid(color + "18"), 0, 0)
        action act
        fixed:
            if active:
                add Solid(color) xpos 0 ypos 0 xsize 156 ysize 2
            add Transform(icon, size=(28, 28), matrixcolor=TintMatrix(color)) xalign 0.5 ypos 8
            text label:
                xalign 0.5 ypos 40 size 13 color color
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1


# -----------------------------------------------------------------------------
# Ligne chapitre (colonne gauche — un vote par chapitre)
# -----------------------------------------------------------------------------
screen dossier_chapter_row(chapter, sel_chapter):
    $ chapter_id = chapter["id"]
    $ pid = dossier_prop_first_of_chapter(chapter_id)
    $ prop = dossier_prop(pid)
    $ selected = (chapter_id == sel_chapter)
    $ vote_day = chapter_id * 3

    button:
        xsize 430 ysize 118
        background (Frame(Solid("#0E1E2C"), 0, 0) if selected else Frame(Solid("#00000000"), 0, 0))
        hover_background Frame(Solid("#5CD3FF10"), 0, 0)
        action [SetScreenVariable("sel_chapter", chapter_id),
                SetScreenVariable("sel_prop", pid)]
        fixed:
            xsize 430 ysize 118
            # Fil chronologique continu : un marqueur par vote.
            add Solid("#244558") xpos 32 ypos 0 xsize 2 ysize 118
            add Solid("#5CD3FF" if selected else "#36627D") xpos 23 ypos 31 xysize (20, 20)
            add Solid("#07141F") xpos 28 ypos 36 xysize (10, 10)
            if selected:
                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 3 ysize 118
                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 430 ysize 2
                add Solid("#5CD3FF") xpos 0 ypos 116 xsize 430 ysize 2
            else:
                add Solid("#0F1A26") xpos 0 ypos 117 xsize 430 ysize 1

            text ("JOUR %02d  //  VOTE %02d" % (vote_day, chapter_id)):
                xpos 62 ypos 17 size 17 color ("#5CD3FF" if selected else "#6E8CA6")
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text prop.get("title", "").replace("\\n", " "):
                xpos 62 ypos 49 xsize 320 size 17 color ("#DCEBFF" if selected else "#8FB4CC")
                font "fonts/Rajdhani-SemiBold.ttf" line_leading 2
            add Solid("#5CD3FF" if selected else "#3A566A") xpos 398 ypos 54 xysize (9, 9)


# -----------------------------------------------------------------------------
# Ligne proposition (colonne gauche)
# -----------------------------------------------------------------------------
screen dossier_prop_row(pid, sel_prop):
    $ prop = dossier_prop(pid)
    $ avail = dossier_prop_available(pid)
    $ selected = (pid == sel_prop)

    button:
        xsize 430 ysize 98
        background (Frame(Solid("#0E1E2C"), 0, 0) if (selected and avail) else Frame(Solid("#00000000"), 0, 0))
        hover_background Frame(Solid("#5CD3FF10"), 0, 0)
        action SetScreenVariable("sel_prop", pid)
        sensitive avail
        fixed:
            xsize 430 ysize 98
            if selected and avail:
                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 3 ysize 98
                add Solid("#5CD3FF") xpos 0 ypos 0 xsize 430 ysize 2
                add Solid("#5CD3FF") xpos 0 ypos 96 xsize 430 ysize 2
            else:
                add Solid("#0F1A26") xpos 0 ypos 97 xsize 430 ysize 1

            text ("%02d" % prop.get("num", 0)):
                xpos 22 ypos 34 size 26 color ("#5CD3FF" if avail else "#3C4E5E")
                font "fonts/Rajdhani-SemiBold.ttf"

            text (prop.get("title", "").replace("\n", " ") if avail else prop.get("title", "").replace("\n", " ")):
                xpos 78 ypos 20 xsize 296 size 16
                color ("#DCEBFF" if avail else "#54697B")
                font "fonts/Rajdhani-SemiBold.ttf" line_leading 2

            if avail:
                add Solid("#5CD3FF") xpos 388 ypos 44 xysize (10, 10)
            else:
                add "hud/codex/badge_lock.png" xpos 384 ypos 38 xysize (22, 22) at dossier_tint("#54697B")


# -----------------------------------------------------------------------------
# Carte argument
# -----------------------------------------------------------------------------
screen dossier_arg_card(aid):
    $ unlocked = dossier_arg_unlocked(aid)
    $ meta = dossier_arg_cat(aid)
    $ col = meta["color"]
    $ arg = DOSSIER_ARGS.get(aid, {})

    fixed:
        xysize (642, 210)

        if unlocked:
            add Solid(col + "0C") xpos 0 ypos 0 xsize 642 ysize 210
            add Solid(col) xpos 0 ypos 0 xsize 642 ysize 2
            add Solid(col) xpos 0 ypos 208 xsize 642 ysize 2
            add Solid(col) xpos 0 ypos 0 xsize 2 ysize 210
            add Solid(col) xpos 640 ypos 0 xsize 2 ysize 210

            # Tag catégorie
            frame:
                xpos 22 ypos 20 ysize 30
                background Frame(Solid("#0A1420"), 0, 0)
                fixed:
                    add Solid(col) xpos 0 ypos 0 xsize 2 ysize 30
                    text meta["label"]:
                        xpos 12 yalign 0.5 xoffset 2 size 14 color col
                        font "fonts/Rajdhani-SemiBold.ttf" kerning 2 xmaximum 200

            # Titre
            text arg.get("title", ""):
                xpos 130 ypos 22 xsize 420 size 20 color "#EAF4FF"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1

            # Check
            add "hud/codex/badge_check.png" xpos 594 ypos 20 xysize (30, 30) at dossier_tint(col)

            # Icône disque
            frame:
                xpos 22 ypos 66 xysize (86, 86)
                background Frame(Solid(col + "16"), 0, 0)
                add Transform(meta["icon"], size=(50, 50), matrixcolor=TintMatrix(col)) xalign 0.5 yalign 0.5

            # Description
            text arg.get("desc", ""):
                xpos 130 ypos 58 xsize 480 size 16 color "#B7CAD8"
                font "fonts/Barlow-Light.ttf" line_leading 3

            # Source
            text "Obtenu auprès de :":
                xpos 22 ypos 172 size 15 color "#7C99AC" font "fonts/Barlow-Light.ttf"
            text arg.get("source", ""):
                xpos 190 ypos 172 size 15 color col font "fonts/Rajdhani-SemiBold.ttf" kerning 1

        else:
            add Solid("#0A121C") xpos 0 ypos 0 xsize 642 ysize 210
            add Solid("#1A2A3A") xpos 0 ypos 0 xsize 642 ysize 1
            add Solid("#1A2A3A") xpos 0 ypos 209 xsize 642 ysize 1
            add Solid("#1A2A3A") xpos 0 ypos 0 xsize 1 ysize 210
            add Solid("#1A2A3A") xpos 641 ypos 0 xsize 1 ysize 210

            frame:
                xpos 22 ypos 20 ysize 30
                background Frame(Solid("#0E1826"), 0, 0)
                text "INCONNU":
                    xpos 12 yalign 0.5 size 14 color "#54697B"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text "Argument non débloqué":
                xpos 130 ypos 22 size 20 color "#5E7688" font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            frame:
                xpos 22 ypos 66 xysize (86, 86)
                background Frame(Solid("#101E2A"), 0, 0)
                add "hud/codex/badge_lock.png" xalign 0.5 yalign 0.5 xysize (40, 40) at dossier_tint("#3C4E5E")
            text "Continuez vos discussions, explorez les lieux et observez les autres représentants pour débloquer cet argument.":
                xpos 130 ypos 58 xsize 480 size 16 color "#54697B"
                font "fonts/Barlow-Light.ttf" line_leading 3
            text "???":
                xpos 130 ypos 170 size 18 color "#3C4E5E" font "fonts/Rajdhani-SemiBold.ttf"


# -----------------------------------------------------------------------------
# Cycle chapitre (parmi les chapitres visibles)
# -----------------------------------------------------------------------------
init python:
    def dossier_cycle_chapter(cur):
        vis = [c["id"] for c in dossier_visible_chapters()]
        if not vis:
            return cur
        if cur not in vis:
            return vis[0]
        i = vis.index(cur)
        return vis[(i + 1) % len(vis)]
