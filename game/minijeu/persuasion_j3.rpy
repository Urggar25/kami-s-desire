# ============================================================
# minijeu/persuasion_j3.rpy — Mini-jeu « Entretiens individuels » (Jour 3)
#
# Suspension de séance au Conclave : un seul représentant à l'écran,
# flèches pour passer de l'un à l'autre, un entretien par personne.
# Le visage trahit la tendance de vote sans l'afficher :
#   souriant = pour, neutre = hésite, stressé = contre.
# Chaque entretien débouche sur une Réfutation dont les fragments
# sont les arguments débloqués : selon le fragment gagnant, le
# représentant penche vers le POUR ou vers le CONTRE.
#
#   call j3_persuasion_run from _call_...
# ============================================================

define J3P_ASSETS = "minijeu/persuasion_assets/"

default j3p_index = 0
default j3p_dir = 1
default j3p_done = []
default j3p_last_fragment = None

# Une conversation = une action, au maximum trois pendant cette suspension.
define J3P_MAX_ACTIONS = 3

init 5 python:
    J3P_ORDER = ["ryn", "sael", "kael", "nyra", "mara", "elias", "julian", "iris", "elen", "tomas", "lysa"]

    J3P_DISTRICTS = {
        "ryn": _("Représentant de Limen"),
        "sael": _("Représentante de Limen"),
        "kael": _("Représentant d'Orbite"),
        "nyra": _("Représentante d'Orbite"),
        "mara": _("Représentante d'Axiome"),
        "elias": _("Représentant d'Axiome"),
        "julian": _("Représentant de Nexus"),
        "iris": _("Représentante de Nexus"),
        "elen": _("Représentante d'Archive"),
        "tomas": _("Représentant d'Archive"),
        "lysa": _("Représentante d'Harmonie"),
    }

    # Fragment gagnant -> variation d'adhésion (positif = pour, négatif = contre).
    J3P_DELTA = 3
    J3P_EFFECTS = {
        "ryn": {"rationnement": J3P_DELTA, "echanges_discrets": J3P_DELTA, "enonce_precis": -J3P_DELTA},
        "sael": {"echanges_discrets": J3P_DELTA, "valeur_travail": -J3P_DELTA},
        "kael": {"derogations_complexes": J3P_DELTA, "echanges_discrets": J3P_DELTA, "orbite": -J3P_DELTA},
        "nyra": {"approvisionnement": J3P_DELTA, "orbite": -J3P_DELTA},
        "mara": {"rationnement": J3P_DELTA, "echanges_discrets": J3P_DELTA, "monde_avant": -J3P_DELTA},
        "elias": {"derogations_complexes": J3P_DELTA, "valeur_travail": -J3P_DELTA},
        "julian": {"monde_avant": J3P_DELTA, "enonce_precis": -J3P_DELTA, "valeur_travail": -J3P_DELTA},
        "iris": {"derogations_complexes": J3P_DELTA, "rationnement": J3P_DELTA, "enonce_precis": -J3P_DELTA},
        "elen": {"derogations_complexes": J3P_DELTA, "approvisionnement": -J3P_DELTA},
        "tomas": {"rationnement": J3P_DELTA, "enonce_precis": -J3P_DELTA},
        "lysa": {"echanges_discrets": J3P_DELTA, "approvisionnement": -J3P_DELTA},
    }

    J3P_STRESS_EXPR = {"mara": "stress", "nyra": "stress", "tomas": "stress"}
    J3P_DONE_MATRIX = BrightnessMatrix(-0.30) * SaturationMatrix(0.35)

    def j3p_arg_unlocked(arg_id):
        if dossier_arg_unlocked(arg_id):
            return True
        if arg_id in getattr(store, "j2_vote_arguments", []):
            return True
        data = DAY2_VOTE_ARGUMENTS.get(arg_id) or DAY3_VOTE_ARGUMENTS.get(arg_id) or {}
        title = data.get("title")
        return bool(title and title in getattr(store, "arguments", []))

    def j3p_unlocked_count():
        ids = set(DAY2_VOTE_ARGUMENTS) | set(DAY3_VOTE_ARGUMENTS)
        return sum(1 for a in ids if j3p_arg_unlocked(a)), len(ids)

    def j3p_vote_side(who):
        stats = getattr(store, "debat_day3_live_vote_stats", None) or DEBAT_DAY3_BASE_VOTE_STATS
        value = stats.get(who, 0)
        if value > 1:
            return "pour"
        if value < -1:
            return "contre"
        return "abstention"

    def j3p_mood_expr(who):
        side = j3p_vote_side(who)
        if side == "pour":
            return "sourire"
        if side == "contre":
            return J3P_STRESS_EXPR.get(who, "inquiet")
        return "neutre"

    def j3p_step(step):
        store.j3p_dir = 1 if step > 0 else -1
        store.j3p_index = (store.j3p_index + step) % len(J3P_ORDER)
        renpy.restart_interaction()

    def j3p_goto(index):
        if index != store.j3p_index:
            store.j3p_dir = 1 if index > store.j3p_index else -1
            store.j3p_index = index
            renpy.restart_interaction()

    def j3p_can_win(who):
        return any(j3p_arg_unlocked(a) for a in J3P_EFFECTS.get(who, {}))

    def j3p_actions_left():
        return max(0, J3P_MAX_ACTIONS - len(store.j3p_done))

    def j3p_resolve(who, result):
        """Marque l'entretien comme mené et renvoie pour / contre / echec / sans_argument."""
        if who not in store.j3p_done:
            if j3p_actions_left() <= 0:
                return "echec"
            store.j3p_done.append(who)
        store.j3p_last_fragment = None
        if result is None:
            return "sans_argument"
        status, fragment = result
        store.j3p_last_fragment = fragment
        delta = J3P_EFFECTS.get(who, {}).get(fragment)
        if status == "success" and delta:
            debat_day3_apply_influence({who: delta})
            return "pour" if delta > 0 else "contre"
        return "echec"

    def j3p_fragments(entries):
        """entries : [(arg_id, libellé)] -> fragments verrouillés tant que l'argument n'est pas acquis."""
        return [(arg_id, label, (lambda a=arg_id: j3p_arg_unlocked(a))) for arg_id, label in entries]

    # ------------------------------------------------------------
    # Réfutations des entretiens (failles entre [[ ]]).
    # ------------------------------------------------------------
    refutation_register(
        "j3p_ryn", title=_("RYN — LES BONS"), bg="bg_conclave",
        statements=[
            ("ryn", "colere", _("Les bons, c'est [[tout ce qui nourrit encore Limen]] !")),
            ("ryn", "colere", _("Sans les papiers de Kami, [[personne chez nous n'aurait rien]].")),
            ("ryn", "reflechit", _("Ce texte, il autorise juste [[le commerce en plus des rations]].")),
            ("ryn", "triste", _("Et toi, t'as [[jamais fait la queue pour rien]], hein ?")),
        ],
        fragments=j3p_fragments([
            ("rationnement", _("Des bons sans rien derrière")),
            ("echanges_discrets", _("Les échanges en douce")),
            ("enonce_precis", _("« Suppression des bons »")),
            ("monde_avant", _("Le monde d'avant")),
        ]),
        solution={(0, 0): "rationnement", (1, 0): "echanges_discrets", (2, 0): "enonce_precis"},
        miss={"default": _("C'est tout ? Ça remplit pas une assiette, ça.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_sael", title=_("SAEL — LE VILLAGE"), bg="bg_conclave",
        statements=[
            ("sael", "calme", _("Mamie disait qu'un arbre ne pousse pas [[parce qu'on l'y autorise]].")),
            ("sael", "neutre", _("Le commerce, [[ce n'est pas notre façon de vivre]], chez nous.")),
            ("sael", "reflechit", _("Si les contrats sont justes, [[ils prendront soin de chacun]].")),
            ("sael", "determine", _("Je choisirai [[ce qui laisse le village debout]].")),
        ],
        fragments=j3p_fragments([
            ("echanges_discrets", _("Les échanges du village")),
            ("valeur_travail", _("Ceux qui ne peuvent plus travailler")),
            ("rationnement", _("Des bons sans rien derrière")),
            ("enonce_precis", _("« Suppression des bons »")),
        ]),
        solution={(1, 0): "echanges_discrets", (2, 0): "valeur_travail"},
        miss={"default": _("Tu cherches la pluie dans le mauvais nuage, Noam.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_kael", title=_("KAEL — LA CHAÎNE VITALE"), bg="bg_conclave",
        statements=[
            ("kael", "calme", _("Le système actuel est lent. Mais [[la lenteur ne tue personne]].")),
            ("kael", "reflechit", _("Si on ouvre les échanges, [[les livraisons vitales resteront prioritaires]].")),
            ("kael", "inquiet", _("On ne peut pas [[monter une chaîne parallèle]] en une nuit.")),
            ("kael", "neutre", _("Je déciderai [[devant le bulletin]].")),
        ],
        fragments=j3p_fragments([
            ("orbite", _("Une erreur qui tue")),
            ("derogations_complexes", _("Des jours pour une pièce")),
            ("echanges_discrets", _("Les circuits informels")),
            ("approvisionnement", _("Des districts inégaux")),
        ]),
        solution={(0, 0): "derogations_complexes", (1, 0): "orbite", (2, 0): "echanges_discrets"},
        miss={"default": _("Non. Ça ne correspond pas.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_nyra", title=_("NYRA — LES ROUTES"), bg="bg_conclave",
        statements=[
            ("nyra", "sourire", _("Je suis d'accord avec toi, Noam. [[Sur presque tout]].")),
            ("nyra", "reflechit", _("Au moins, aujourd'hui, [[tout le monde reçoit pareil]]. C'est rassurant, non ?")),
            ("nyra", "raison", _("La flotte suivra. [[Les transporteurs s'adaptent toujours]].")),
            ("nyra", "neutre", _("Qu'est-ce que tu voudrais obtenir, [[au fond]] ?")),
        ],
        fragments=j3p_fragments([
            ("approvisionnement", _("Des districts inégaux")),
            ("orbite", _("Une erreur qui tue")),
            ("echanges_discrets", _("Les circuits informels")),
            ("valeur_travail", _("Ceux qui ne peuvent plus travailler")),
        ]),
        solution={(1, 0): "approvisionnement", (2, 0): "orbite"},
        miss={"default": _("Mm. Tu as une autre offre ?")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_mara", title=_("MARA — LA CHANCE"), bg="bg_conclave",
        statements=[
            ("mara", "taquin", _("Les bons, au moins, [[c'est pareil pour tout le monde]].")),
            ("mara", "doute", _("Le commerce ? [[Ça existe même pas]] dans les districts.")),
            ("mara", "reflexion", _("Julian jure qu'avec ce texte [[tout le monde aura sa chance]].")),
            ("mara", "agace", _("Et toi, t'es venu [[me draguer ou me convaincre]] ?")),
        ],
        fragments=j3p_fragments([
            ("monde_avant", _("Le monde d'avant")),
            ("echanges_discrets", _("Les échanges en douce")),
            ("rationnement", _("Des bons sans rien derrière")),
            ("valeur_travail", _("Ceux qui ne peuvent plus travailler")),
        ]),
        solution={(0, 0): "rationnement", (1, 0): "echanges_discrets", (2, 0): "monde_avant"},
        miss={"default": _("Raté, mon chou. Vise mieux.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_elias", title=_("ELIAS — LA FORGE"), bg="bg_conclave",
        statements=[
            ("elias", "reflechit", _("Bon, peut-être que [[les formulaires, c'est pas si grave]]. On finit par les avoir, les pièces.")),
            ("elias", "determine", _("Avec les contrats, [[tout le monde pourra bosser]] et manger !")),
            ("elias", "agace", _("J'sais pas, moi, [[c'est pas moi qui ai écrit le texte]] !")),
            ("elias", "determine", _("Le travail, [[faut que ça paie enfin]].")),
        ],
        fragments=j3p_fragments([
            ("derogations_complexes", _("Des jours pour une pièce")),
            ("valeur_travail", _("Ceux qui ne peuvent plus travailler")),
            ("approvisionnement", _("Des districts inégaux")),
            ("monde_avant", _("Le monde d'avant")),
        ]),
        solution={(0, 0): "derogations_complexes", (1, 0): "valeur_travail"},
        miss={"default": _("Hein ? J'vois pas le rapport.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_julian", title=_("JULIAN — L'HISTOIRE"), bg="bg_conclave",
        statements=[
            ("julian", "determine", _("Mes chers collègues, [[l'histoire retiendra ce vote]].")),
            ("julian", "hesitation", _("Peut-être que [[les gens ont oublié comment on fait]]. Qu'ils n'essaieront plus.")),
            ("julian", "sourire", _("Ce texte [[ouvre simplement le commerce]], rien de plus.")),
            ("julian", "determine", _("Avec les contrats, [[chacun gagnera sa vie]].")),
        ],
        fragments=j3p_fragments([
            ("monde_avant", _("Le monde d'avant")),
            ("enonce_precis", _("« Suppression des bons »")),
            ("valeur_travail", _("Ceux qui ne peuvent plus travailler")),
            ("approvisionnement", _("Des districts inégaux")),
        ]),
        solution={(1, 0): "monde_avant", (2, 0): "enonce_precis", (3, 0): "valeur_travail"},
        miss={"default": _("Permets-moi de ne pas relever.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_iris", title=_("IRIS — LES CONTRATS"), bg="bg_conclave",
        statements=[
            ("iris", "agace", _("Une pièce détachée, [[ça se trouve en deux jours]]. Trois, au pire.")),
            ("iris", "reflechit", _("Techniquement, une IA qui distribue les contrats [[pourrait être plus juste]] que nous.")),
            ("iris", "colere", _("Et on vote [[sans savoir qui a écrit ça]]. Génial.")),
            ("iris", "blase", _("Les bons, au moins, [[ça a le mérite de marcher]].")),
        ],
        fragments=j3p_fragments([
            ("derogations_complexes", _("Des jours pour une pièce")),
            ("enonce_precis", _("Kami décide qui sera payé")),
            ("rationnement", _("Des bons sans rien derrière")),
            ("orbite", _("Une erreur qui tue")),
        ]),
        solution={(0, 0): "derogations_complexes", (1, 0): "enonce_precis", (3, 0): "rationnement"},
        miss={"default": _("Sérieusement ? Ça répond à rien.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_elen", title=_("ELEN — FAIRE PLAISIR"), bg="bg_conclave",
        statements=[
            ("elen", "joie", _("Imagine, acheter des chaussures [[sans prouver qu'elles sont trouées]] !")),
            ("elen", "inquiet", _("Mais bon, peut-être que [[les demandes, c'est pas si long]], en vrai...")),
            ("elen", "joie", _("Avec le commerce, [[tout le monde pourra se faire plaisir]] !")),
            ("elen", "sourire", _("Au fait, [[t'as goûté le dessert]] de midi ?")),
        ],
        fragments=j3p_fragments([
            ("derogations_complexes", _("Trois pages pour des fraises")),
            ("approvisionnement", _("Tu paies comment ?")),
            ("rationnement", _("Des bons sans rien derrière")),
            ("monde_avant", _("Le monde d'avant")),
        ]),
        solution={(1, 0): "derogations_complexes", (2, 0): "approvisionnement"},
        miss={"default": _("Hein ? Attends, j'ai perdu le fil !")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_tomas", title=_("TOMAS — LES DONNÉES"), bg="bg_conclave",
        statements=[
            ("tomas", "hesitation", _("D-D'après mes données, [[les bons couvrent l'essentiel]]... en moyenne.")),
            ("tomas", "raison", _("Il y aura forcément [[une période de transition]]. Historiquement, c'est la norme.")),
            ("tomas", "inquiet", _("Julian dit que [[l'histoire n'attend pas]]...")),
            ("tomas", "reflechit", _("Techniquement, [[on ne peut rien prévoir]]. Enfin, pas tout.")),
        ],
        fragments=j3p_fragments([
            ("rationnement", _("Ruptures de stock")),
            ("enonce_precis", _("Aucune transition prévue")),
            ("monde_avant", _("Le monde d'avant")),
            ("approvisionnement", _("Des districts inégaux")),
        ]),
        solution={(0, 0): "rationnement", (1, 0): "enonce_precis"},
        miss={"default": _("T-Techniquement, ça ne contredit pas ce que j'ai dit.")},
        lives=3, line_time=5.8,
    )

    refutation_register(
        "j3p_lysa", title=_("LYSA — LA LIGNE DE DÉPART"), bg="bg_conclave",
        statements=[
            ("lysa", "blase", _("Rome aussi a promis du pain. [[Ça s'est très bien terminé]].")),
            ("lysa", "blase", _("Interdire le commerce, [[ça empêche les gens de trafiquer]]. Évidemment.")),
            ("lysa", "reflechit", _("Si on ouvre, [[chaque district partira à égalité]]. C'est ce qu'on nous vend.")),
            ("lysa", "taquin", _("Bref. [[Tu vas me faire un discours]], c'est ça ?")),
        ],
        fragments=j3p_fragments([
            ("echanges_discrets", _("Le marché noir existe déjà")),
            ("approvisionnement", _("Les plus riches passeront devant")),
            ("monde_avant", _("Le monde d'avant")),
            ("enonce_precis", _("« Suppression des bons »")),
        ]),
        solution={(1, 0): "echanges_discrets", (2, 0): "approvisionnement"},
        miss={"default": _("Et alors ? C'était censé me faire quoi ?")},
        lives=3, line_time=5.8,
    )


transform j3p_sprite_in(d=1):
    subpixel True
    alpha 0.0 xoffset (70 * d)
    easeout 0.24 alpha 1.0 xoffset 0

transform j3p_glow_pulse:
    alpha 0.55
    ease 1.6 alpha 0.85
    ease 1.6 alpha 0.55
    repeat


# ------------------------------------------------------------
# Écran de navigation entre les représentants
# ------------------------------------------------------------
screen j3_persuasion_screen():
    modal True
    zorder 250

    $ who = J3P_ORDER[j3p_index]
    $ done = who in j3p_done
    $ col = kd_char_color(who)
    $ args_ok, args_total = j3p_unlocked_count()
    $ remaining = j3p_actions_left()
    $ end_action = Confirm(_("Reprendre la séance ? Les actions restantes seront perdues."), Return("end")) if remaining > 0 else Return("end")

    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "K_LEFT" action Function(j3p_step, -1)
    key "K_RIGHT" action Function(j3p_step, 1)
    key "K_q" action Function(j3p_step, -1)
    key "K_d" action Function(j3p_step, 1)
    key "pad_dpleft_press" action Function(j3p_step, -1)
    key "pad_dpright_press" action Function(j3p_step, 1)
    key "pad_leftshoulder_press" action Function(j3p_step, -1)
    key "pad_rightshoulder_press" action Function(j3p_step, 1)

    add "bg_conclave" at adaptive_fullscreen
    add Solid("#040914b8")
    add "gui/main_menu_kami/vignette.png"
    add "gui/main_menu_kami/scanlines.png" alpha 0.35
    add Solid(RF_CYAN, xysize=(1920, 2)) at rf_scan

    # --- Représentant (un seul à l'écran), assombri si l'entretien est fait.
    add J3P_ASSETS + "floor_glow.png" at j3p_glow_pulse:
        xcenter 960
        ycenter 1020
    for i, tag in enumerate(J3P_ORDER):
        if i == j3p_index:
            if tag in j3p_done:
                add Transform(character_image(tag, j3p_mood_expr(tag)), zoom=1.00, matrixcolor=J3P_DONE_MATRIX) at j3p_sprite_in(j3p_dir):
                    xalign 0.5
                    yalign 1.00
            else:
                add Transform(character_image(tag, j3p_mood_expr(tag)), zoom=1.00) at j3p_sprite_in(j3p_dir):
                    xalign 0.5
                    yalign 1.00

    # --- Bandeau supérieur gauche : titre de la séquence.
    frame:
        background Frame(RF_ASSETS + "panel.png", 26, 26)
        xpos 40
        ypos 30
        xsize 600
        ysize 104
        padding (30, 14)
        vbox:
            spacing 2
            text _("SUSPENSION DE SÉANCE"):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 40
                color "#eef7ff"
                kerning 3
            text _("ENTRETIENS INDIVIDUELS  //  JOUR 3"):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 20
                color RF_CYAN
                kerning 2
    text _("Choisis : trois entretiens maximum, un par représentant."):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 22
        color "#8fb4c8"
        xpos 70
        ypos 146

    # --- Pastilles : une par représentant (cliquables).
    hbox:
        xcenter 1040
        ycenter 82
        spacing 10
        for i, tag in enumerate(J3P_ORDER):
            $ pip = "current" if i == j3p_index else ("done" if tag in j3p_done else "open")
            imagebutton:
                idle (J3P_ASSETS + "pip_%s.png" % pip)
                hover J3P_ASSETS + "pip_current.png"
                action Function(j3p_goto, i)

    # --- Bandeau supérieur droit : compteurs.
    frame:
        background Frame(RF_ASSETS + "panel.png", 26, 26)
        xpos 1440
        ypos 30
        xsize 440
        ysize 104
        padding (30, 14)
        vbox:
            spacing 0
            text _("ACTIONS UTILISÉES"):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 20
                color RF_CYAN
                kerning 2
            text ("%d / %d" % (len(j3p_done), J3P_MAX_ACTIONS)):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 46
                color "#eef7ff"
    text (_("ARGUMENTS DÉBLOQUÉS") + "  %d / %d" % (args_ok, args_total)):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 20
        color "#8fb4c8"
        kerning 1
        xpos 1470
        ypos 146

    # --- Flèches de navigation.
    imagebutton:
        idle J3P_ASSETS + "arrow_left_idle.png"
        hover J3P_ASSETS + "arrow_left_hover.png"
        xcenter 500
        ycenter 560
        action Function(j3p_step, -1)
    imagebutton:
        idle J3P_ASSETS + "arrow_right_idle.png"
        hover J3P_ASSETS + "arrow_right_hover.png"
        xcenter 1420
        ycenter 560
        action Function(j3p_step, 1)

    # --- Fiche du représentant affiché.
    frame:
        background Frame(RF_ASSETS + "panel.png", 26, 26)
        xpos 40
        ypos 846
        xsize 560
        ysize 160
        padding (34, 16)
        vbox:
            spacing 4
            text kd_display_name(who).upper():
                font "fonts/Rajdhani-SemiBold.ttf"
                size 56
                color col
                kerning 4
            text kd_tr(J3P_DISTRICTS.get(who, "")).upper():
                font "fonts/Rajdhani-SemiBold.ttf"
                size 20
                color RF_CYAN
                kerning 2
            text (_("//  ENTRETIEN TERMINÉ") if done else (_("//  ACTIONS ÉPUISÉES") if remaining == 0 else _("//  ENTRETIEN DISPONIBLE"))):
                font "fonts/Rajdhani-SemiBold.ttf"
                size 20
                color ("#6f8ba0" if done else RF_AMBER)
                kerning 2

    # --- Ouvrir l'entretien.
    button:
        xcenter 960
        ypos 900
        xysize (460, 86)
        background Frame("gui/main_menu_kami/button_idle.png", 30, 20)
        hover_background Frame("gui/main_menu_kami/button_hover.png", 30, 20)
        insensitive_background Frame(RF_ASSETS + "frag_idle.png", 30, 26)
        sensitive (not done and remaining > 0)
        action Return(who)
        text (_("ENTRETIEN TERMINÉ") if done else (_("ACTIONS ÉPUISÉES") if remaining == 0 else _("OUVRIR L'ENTRETIEN"))):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 30
            kerning 3
            color ("#6f8ba0" if done else "#eef7ff")
            align (0.5, 0.5)

    # --- Reprendre la séance.
    button:
        xpos 1440
        ypos 916
        xysize (440, 70)
        background Frame(RF_ASSETS + "frag_idle.png", 30, 26)
        hover_background Frame(RF_ASSETS + "frag_selected.png", 30, 26)
        padding (52, 0, 20, 0)
        action end_action
        text _("REPRENDRE LA SÉANCE"):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 26
            kerning 2
            color "#b9c9d6"
            hover_color "#ffffff"
            yalign 0.5

    text _("← / →  CHANGER DE REPRÉSENTANT     •     3 ACTIONS MAXIMUM  •  1 PAR PERSONNE"):
        font "fonts/Rajdhani-SemiBold.ttf"
        size 20
        color "#8fb4c8"
        kerning 1
        xcenter 960
        ypos 1034


# ------------------------------------------------------------
# Boucle de la séquence
# ------------------------------------------------------------
label j3_persuasion_run:
    $ restore_unlocked_arguments()
    $ day3_vote_bootstrap()
    $ day2_sync_argument_titles()
    $ j3p_index = 0
    $ j3p_dir = 1
    $ j3p_done = []
    hide screen kami_broadcast_ui

    while True:
        scene bg_conclave at adaptive_fullscreen with dissolve
        $ _j3p_pick = renpy.call_screen("j3_persuasion_screen")
        if _j3p_pick == "end" or _j3p_pick not in J3P_ORDER or j3p_actions_left() == 0:
            return
        if _j3p_pick in j3p_done:
            continue
        $ _j3p_label = "j3p_" + _j3p_pick
        call expression _j3p_label from _call_j3p_talk_expression
        if j3p_actions_left() == 0:
            return

    return

# Lance la Réfutation de l'entretien et renvoie pour / contre / echec / sans_argument.
label j3_persuasion_duel(who):
    if not j3p_can_win(who):
        $ _j3p_outcome = j3p_resolve(who, None)
    else:
        call refutation_run("j3p_" + who) from _call_refutation_run_j3p_duel
        $ _j3p_outcome = j3p_resolve(who, _return)
    $ renpy.block_rollback()
    return _j3p_outcome


# ------------------------------------------------------------
# Entretiens
# ------------------------------------------------------------
label j3p_ryn:
    $ showP("ryn", j3p_mood_expr("ryn"), 0.5)
    noam inquiet "Ryn. T'as deux minutes ?"
    ryn colere "Pour que tu m'expliques que Julian a raison ? Non."
    noam calme "Pour t'écouter, d'abord."
    ryn agace "...Vas-y. Écoute. Ça va être court."
    ryn colere "À Limen, les gens ont faim MAINTENANT. Pas dans un an, quand Kami aura distribué ses jolis contrats."
    ryn colere "Et vous voulez retirer la seule chose qui arrive encore jusque chez nous ?!"
    think "Il ne crie pas sur moi. Il crie sur tout le monde à la fois."
    call j3_persuasion_duel("ryn") from _call_j3p_duel_ryn
    if _return == "pour":
        ryn reflechit "..."
        if j3p_last_fragment == "echanges_discrets":
            ryn reflechit "...Ouais. Chez nous aussi, ça troque en douce. Tout le monde le sait, personne le dit."
        else:
            ryn reflechit "Un bon pour du lait tourné. Ouais. Je sais."
        ryn agace "Ça me plaît pas. Mais t'as pas complètement tort."
        think "Il serre la mâchoire. Chez Ryn, c'est déjà presque un oui."
    elif _return == "contre":
        ryn colere "Voilà. VOILÀ ! Supprimer. Pas ajouter. {k}Supprimer{/k} !"
        ryn determine "Merci, Noam. Au moins un qui lit."
        think "Je viens de lui donner une raison de plus de tenir bon. Je ne sais pas encore si c'était une bonne idée."
    elif _return == "echec":
        ryn blase "T'as fini ? Les mots, ça remplit pas les assiettes."
        think "Il me tourne déjà le dos."
    else:
        think "J'ouvre la bouche. Rien de solide n'en sort."
        ryn agace "C'est bien ce que je pensais."
    return
# Durée : 1m30

label j3p_sael:
    $ showP("sael", j3p_mood_expr("sael"), 0.5)
    sael calme "Noam."
    think "Elle ne bouge pas. Elle attend, les mains croisées, comme si on était au bord d'un champ et pas au milieu d'un vote mondial."
    noam neutre "Tu n'as presque rien dit, tout à l'heure."
    sael neutre "Quand tout le monde crie, la pluie ne tombe pas plus vite."
    sael reflechit "Mamie disait ça quand les hommes du village se disputaient sur les semailles."
    noam doute "Et... ça voulait dire quoi ?"
    sael sourire "Qu'ils semaient en retard."
    sael neutre "Je t'écoute."
    call j3_persuasion_duel("sael") from _call_j3p_duel_sael
    if _return == "pour":
        sael reflechit "...Une poule contre une réparation de toit. Oui. On le fait depuis toujours."
        sael calme "On ne l'a juste jamais appelé « commerce »."
        sael sourire "Le mot me faisait plus peur que la chose."
    elif _return == "contre":
        sael triste "Personne au bord du champ."
        sael determine "C'est la seule règle que Mamie n'a jamais négociée. Ce texte l'oublie."
        think "Sa voix ne monte pas. Elle se ferme, simplement."
    elif _return == "echec":
        sael neutre "Tu parles vite, Noam. Plus vite que tu ne penses."
        sael calme "Reviens quand le vent sera tombé."
    else:
        think "Tout ce que je pourrais lui dire, elle l'a déjà vécu. Moi, je n'ai rien vu."
        sael calme "Le silence aussi est une réponse. Merci de ne pas l'avoir abîmé."
    return
# Durée : 1m30

label j3p_kael:
    $ showP("kael", j3p_mood_expr("kael"), 0.5)
    kael neutre "..."
    think "Kael fixe son pupitre. Pas l'écran, pas nous. Son pupitre."
    noam calme "Kael ?"
    kael neutre "Je t'écoute."
    noam inquiet "C'est plutôt moi qui voulais t'écouter."
    pause 0.6
    kael calme "Là-haut, chaque livraison est calculée. Filtres, joints, rations. S'il en manque une, un module entier peut y passer."
    kael inquiet "Ce texte change toute la chaîne. Je ne sais pas encore ce qu'il casse."
    call j3_persuasion_duel("kael") from _call_j3p_duel_kael
    if _return == "pour":
        if j3p_last_fragment == "echanges_discrets":
            kael reflechit "...Si les gens échangent déjà, le circuit existe. Il est juste invisible."
            kael calme "On peut le mesurer. Avant de tout casser."
        else:
            kael reflechit "...Quatre jours pour un joint de sas. Oui."
            kael calme "La lenteur aussi est un risque. Je l'avais rangée à part. Erreur de calcul."
        think "Il ne sourit pas. Mais quelque chose s'est desserré."
    elif _return == "contre":
        kael triste "Personne ne garantit rien. C'est exactement ça."
        kael inquiet "Je préfère l'entendre maintenant que dans un rapport d'accident."
    elif _return == "echec":
        kael neutre "Ton raisonnement ne tient pas."
        kael calme "Ce n'est pas un reproche. C'est une mesure."
    else:
        think "Je n'ai rien sur Orbite. Pas un chiffre. Pas un fait."
        kael neutre "Tu n'as pas besoin de parler pour combler, Noam."
    return
# Durée : 1m20

label j3p_nyra:
    $ showP("nyra", j3p_mood_expr("nyra"), 0.5)
    nyra sourire "Noam. Je me demandais quand tu passerais."
    noam doute "Tu m'attendais ?"
    nyra neutre "J'attends toujours un peu tout le monde."
    nyra reflechit "Alors ? Qu'est-ce que tu as entendu, depuis ce matin ?"
    think "Elle retourne la question avant même que je la pose. Comme si c'était moi, l'interrogé."
    noam calme "Je voulais savoir ce que toi, tu en penses."
    nyra sourire "J'ai passé ma vie entre les ports. Les marchandises, ça circule. Ou ça pourrit."
    nyra reflechit "La vraie question, c'est qui décide de la route."
    call j3_persuasion_duel("nyra") from _call_j3p_duel_nyra
    if _return == "pour":
        nyra reflechit "...Des districts qui ne voient jamais rien arriver, pendant qu'à côté..."
        nyra sourire "Oui. Une route qui s'ouvre, ça peut aussi être une route qui arrive enfin quelque part."
        nyra neutre "Tu négocies mieux que tu le crois."
    elif _return == "contre":
        nyra stress "Pas de deuxième chance là-haut. Non."
        think "Une seconde, son sourire disparaît. Une vraie seconde."
        nyra neutre "...Pardon. Tu as raison. On ne joue pas avec les modules."
    elif _return == "echec":
        nyra sourire "Mm. C'était presque convaincant."
        nyra neutre "Presque, sur Orbite, ça fait des épaves."
    else:
        think "Elle me regarde avec patience. J'ai l'impression d'être une cargaison vide qu'on inspecte."
        nyra sourire "Reviens quand tu auras quelque chose à échanger."
    return
# Durée : 1m30

label j3p_mara:
    $ showP("mara", j3p_mood_expr("mara"), 0.5)
    mara taquin "Tiens. Le médiateur fait sa tournée des pupitres."
    mara sourire "Tu viens chercher mon vote ou mon numéro de chambre ? Je te préviens, y en a un des deux qui est plus facile à obtenir."
    noam gene "...Ton vote."
    mara rire "Dommage. T'avais tes chances pour l'autre."
    noam calme "Mara. Sérieusement."
    mara agace "Sérieusement ? Bah sérieusement, ce texte me donne envie de gerber. Et l'ancien système aussi."
    mara reflexion "Alors vas-y. Convaincs-moi de choisir entre deux trucs dégueulasses."
    call j3_persuasion_duel("mara") from _call_j3p_duel_mara
    if _return == "pour":
        mara doute "...Ouais. Bon. Le système actuel est pourri, on le sait tous."
        mara taquin "Bordel. Tu viens de me convaincre avec un truc concret. C'est presque sexy."
        mara sourire "Presque."
    elif _return == "contre":
        mara colere "Exactement. La « chance », c'est un truc de gens qui ont déjà tout."
        mara reflexion "Moi, je l'ai vue, la chance d'avant. Elle avait toujours le même nom de famille."
        mara agace "Bref. Merci. Tu peux disposer."
    elif _return == "echec":
        mara taquin "Oh, mon pauvre. T'as bafouillé ton argument comme à un premier rencard."
        mara sourire "Reviens quand t'auras de l'entraînement."
    else:
        think "Je n'ai rien à lui opposer. Elle le voit avant moi."
        mara taquin "T'es venu les mains vides ? Mignon. Inutile, mais mignon."
    return
# Durée : 1m30

label j3p_elias:
    $ showP("elias", j3p_mood_expr("elias"), 0.5)
    elias agace "Ah, Noam ! Viens, viens. Explique-moi un truc."
    elias reflechit "Pourquoi tout le monde gueule ? Le texte dit qu'on pourra vendre. Vendre, c'est bien, non ?"
    noam doute "Il dit aussi qu'on supprime les bons."
    elias reflechit "Ouais mais... les bons, ils servent à rien la moitié du temps."
    elias inquiet "...Enfin. Pour moi. Pour d'autres, peut-être, j'sais pas."
    think "Il tourne en rond. Et il le sent."
    elias determine "Vas-y. Dis-moi si j'suis con."
    call j3_persuasion_duel("elias") from _call_j3p_duel_elias
    if _return == "pour":
        elias determine "VOILÀ ! Trois semaines pour un roulement ! Trois semaines, Noam !"
        elias sourire "J'me disais bien que j'étais pas fou."
    elif _return == "contre":
        elias inquiet "...Ma voisine. Elle peut plus rien porter depuis son dos."
        elias triste "Elle signe quoi, elle ? Elle mange comment ?"
        think "Il ne trouve pas la suite. Il ne la cherche même plus."
    elif _return == "echec":
        elias reflechit "J'ai rien compris, mais j'crois que t'as tort."
        elias agace "Désolé. C'est pas contre toi."
    else:
        think "Je cherche un exemple concret. Un seul. Je n'en ai pas."
        elias reflechit "Bon. Si même toi tu sais pas, j'vais pas me prendre la tête."
    return
# Durée : 1m20

label j3p_julian:
    $ showP("julian", j3p_mood_expr("julian"), 0.5)
    julian sourire "Noam ! Le médiateur en personne. Je savais que tu viendrais."
    julian determine "Tu sens ça ? Dans dix ans, on racontera qu'ici, douze personnes ont rendu aux gens le droit de choisir."
    noam doute "Ou le droit d'avoir faim."
    julian agace "Tu as écouté Ryn trop longtemps."
    julian reflexion "...Pardon. Non. Il a le droit d'avoir peur. Tout le monde a ce droit."
    julian hesitation "Mais si on recule à chaque peur, on ne bougera jamais. Et je refuse d'être celui qui n'a pas bougé."
    call j3_persuasion_duel("julian") from _call_j3p_duel_julian
    if _return == "pour":
        julian joie "EXACTEMENT ! Ça a existé, Noam ! Ça peut exister encore !"
        julian sourire "Julian ne s'était pas trompé. Merci de le lui rappeler."
        think "Il parle de lui à la troisième personne. Il est revenu en pleine forme."
    elif _return == "contre":
        julian hesitation "Je... Attends. Ce n'est pas ce que je voulais dire."
        julian reflexion "Non, attends, je peux... il y aura bien un moyen de..."
        think "Pour la première fois, ses phrases ne tombent plus juste. Elles tombent, c'est tout."
    elif _return == "echec":
        julian sourire "Joli effort. Vraiment."
        julian determine "Mais l'histoire n'attend pas les hésitants, Noam."
    else:
        think "Face à lui, je n'ai que des doutes. Ce n'est pas un argument."
        julian sourire "Tu vois ? Même toi, tu n'as rien contre. C'est un signe."
    return
# Durée : 1m20

label j3p_iris:
    $ showP("iris", j3p_mood_expr("iris"), 0.5)
    iris blase "Si tu viens me demander si je vais bien, c'est non. Personne va bien."
    noam calme "Je venais te demander ce que tu votes."
    iris agace "Ah. Encore pire."
    iris reflechit "...Ok. Honnêtement ? Une IA qui gère des contrats, sur le papier, c'est fascinant. Allocation dynamique, optimisation des flux, tout ça."
    think "Ses yeux s'allument. Trois secondes. Puis elle se rappelle de quelle IA on parle."
    iris colere "Sauf que c'est ELLE. Et qu'elle a même pas voulu dire qui avait écrit ce texte."
    call j3_persuasion_duel("iris") from _call_j3p_duel_iris
    if _return == "pour":
        if j3p_last_fragment == "rationnement":
            iris agace "...Ouais. Un bon pour un truc qui existe pas, c'est un ticket de loterie."
        else:
            iris agace "...Ouais. Dix jours pour un capteur, la dernière fois. Dix."
        iris blase "Bon. Le système actuel est une catastrophe. Ça, je te l'accorde."
        iris sourire "Me regarde pas comme ça. J'ai pas dit que t'avais raison sur le reste."
    elif _return == "contre":
        iris colere "Non mais attends... c'est elle qui choisit. Seule. Sans aucun contrôle."
        iris reflechit "Une IA sans garde-fou qui décide qui mange. J'ai lu des thèses entières sur pourquoi c'est une très mauvaise idée."
        iris agace "Merci, Noam. Je déteste quand t'as raison."
    elif _return == "echec":
        iris blase "Sérieusement ? C'est ça, ton argument ?"
        iris agace "Va réviser. Et bois de l'eau, t'as une tête de déterré."
    else:
        think "Elle a déjà démonté tout ce que je pourrais dire. Avant même que je le dise."
        iris blase "Tu viens juste me regarder râler ? Ok. C'est gratuit."
    return
# Durée : 1m20

label j3p_elen:
    $ showP("elen", j3p_mood_expr("elen"), 0.5)
    elen joie "Noaaam ! Tu viens me voir ? C'est trop gentil !"
    elen sourire "Tout le monde fait la tête. Moi, je trouve ça excitant ! On va peut-être changer le monde, tu te rends compte ?"
    noam doute "Ou le casser."
    elen inquiet "...Oui. Ou ça."
    elen joie "Mais non ! Ça va aller ! Enfin... ça doit aller, non ?"
    think "Elle sourit trop vite. Comme on referme une porte."
    call j3_persuasion_duel("elen") from _call_j3p_duel_elen
    if _return == "pour":
        elen joie "Trois pages pour des fraises ! TROIS ! Tu te rends compte ?!"
        elen sourire "Merci, Noam. J'avais besoin qu'on me dise que j'étais pas juste capricieuse."
    elif _return == "contre":
        elen inquiet "...Ceux qui ont rien, ils se font plaisir avec quoi ?"
        elen triste "Ah."
        elen sourire "Bon ! Bah. J'y réfléchirai. Promis."
        think "Le sourire revient. Pas tout à fait à la même place."
    elif _return == "echec":
        elen surpris "Hein ? J'ai pas tout compris, mais c'était très bien dit !"
        elen joie "Au fait, tu crois qu'il y aura du dessert, ce soir ?"
    else:
        think "Je n'ai rien à lui opposer. Et je ne suis pas sûr d'avoir envie d'éteindre ce sourire."
        elen joie "Tu viens juste dire bonjour ? Trop mignon !"
    return
# Durée : 1m20

label j3p_tomas:
    $ showP("tomas", j3p_mood_expr("tomas"), 0.5)
    tomas inquiet "Ah. Noam. Tu... tu viens pour le vote ?"
    noam calme "Je viens pour toi. Le vote, c'est en bonus."
    tomas hesitation "D'accord. Bon. Pour faire court..."
    tomas raison "J'ai relu le texte quatre fois. Puis je l'ai comparé à trois réformes de l'ancien monde. Deux réussies, une... enfin, moins réussie, il y a eu des émeutes, mais le contexte était différent, parce que..."
    tomas gene "...Désolé. Je m'égare."
    tomas inquiet "Et Julian n'arrête pas de me répéter que l'histoire n'attend pas."
    tomas hesitation "Pour faire court : je ne sais pas."
    call j3_persuasion_duel("tomas") from _call_j3p_duel_tomas
    if _return == "pour":
        tomas raison "...Plus de la moitié des produits en rupture. Oui. Je l'avais calculé moi-même."
        tomas hesitation "J-Je me suis fait contredire par mes propres chiffres. C'est... gênant."
        tomas sourire "Mais merci. Vraiment."
    elif _return == "contre":
        tomas peur "Il n'y a pas de transition. Pas un mot. J'ai lu quatre fois et j'ai inventé une phrase qui n'existe pas."
        tomas inquiet "C'est exactement le genre d'erreur qui... D-Désolé. Il faut que je relise."
    elif _return == "echec":
        tomas hesitation "Euh... techniquement, ça ne contredit pas ce que j'ai dit."
        tomas gene "Pardon. Je suis pénible."
    else:
        think "Il connaît les chiffres mieux que moi. Je n'ai rien à lui apprendre."
        tomas inquiet "Tu... tu n'as pas d'avis non plus ? Ça me rassure. Un peu."
    return
# Durée : 1m30

label j3p_lysa:
    $ showP("lysa", j3p_mood_expr("lysa"), 0.5)
    lysa blase "Laisse-moi deviner. Tu fais le tour des pupitres pour sauver le monde."
    noam gene "Pour parler, juste."
    lysa taquin "C'est pareil, chez les médiateurs."
    lysa reflechit "Tu sais ce qui me fatigue ? Tout le monde parle de ce texte comme d'une révolution."
    lysa blase "Les révolutions finissent toujours pareil. Quelqu'un récupère les clés. Sans surprise."
    lysa neutre "Alors vas-y. Surprends-moi."
    call j3_persuasion_duel("lysa") from _call_j3p_duel_lysa
    if _return == "pour":
        lysa reflechit "...Le marché noir existe déjà. Interdire, ça fixe juste le prix du silence."
        lysa sourire "Bon. Un point pour toi. T'y habitue pas."
    elif _return == "contre":
        lysa neutre "Noam. Tu sais pourquoi personne ne part jamais à égalité ?"
        lysa triste "Parce que la ligne de départ, ce sont toujours les mêmes qui la tracent."
    elif _return == "echec":
        lysa taquin "Et alors ? C'était censé me faire quoi, ça ?"
        lysa blase "Bref. Merci d'être passé."
    else:
        think "Lysa attend. Je n'ai rien qu'elle ne puisse retourner contre moi."
        lysa blase "Pas d'argument ? Honnête, au moins. C'est rare, ici."
    return
# Durée : 1m10
