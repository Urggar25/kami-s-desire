init python:
    # Compatibilité chargement : d'anciennes sauvegardes peuvent désérialiser
    # une référence à store.build_arg pendant un reload Ren'Py.
    def build_arg(title):
        low = title.lower()

        if "ration" in low:
            icon = "⌬"
            desc = "Sécurité minimale contre la faim et le chaos."
        elif "orbite" in low or "dépress" in low:
            icon = "◉"
            desc = "Dépendance logistique et fragilité structurelle."
        elif "énoncé" in low or "precis" in low:
            icon = "⟡"
            desc = "Texte exact, conséquences juridiques immédiates."
        elif "appro" in low or "inégal" in low:
            icon = "⬢"
            desc = "Ruptures passées et files de pénurie."
        elif "échange" in low or "discret" in low:
            icon = "◌"
            desc = "Réseaux d'entraide clandestins déjà en place."
        elif "avant" in low:
            icon = "+"
            desc = "Mémoire d'un système ancien imparfait mais vivant."
        else:
            icon = "•"
            desc = "Argument."

        return {"title": title, "desc": desc, "icon": icon}

default j3_wakeup_trace_attempts = 0
default j3_corridor_trace_attempts = 0
default j3_codex_dot = False
default j45_vote_codex_active = False
default day3_cafeteria_route_kael_seen = False
default day3_cafeteria_route_julian_seen = False
# Course des 3 virages : nombre de réussites + malus/bonus d'influence sur Tomas,
# appliqué au vote après la remise à zéro des adhésions (phase 1 du débat).
default day3_corridor_success = 0
default tomas_corridor_delta = 0

init 4 python:
    DAY3_VOTE_ARGUMENTS = {
        "monde_avant": {
            "title": "Le monde d'avant",
            "category": "Mémoire politique",
            "summary": "Julian présente l'avant-Kami comme une preuve que la circulation libre peut exister.",
            "origin": "Entendu auprès de Julian avant la cafétéria.",
            "card": "gui/day3/argument_card_world_before.png",
        },
        "enonce_precis": {
            "title": "L'énoncé précis",
            "category": "Texte du vote",
            "summary": "La formulation exacte devient décisive : elle engage plus qu'une simple autorisation d'échange.",
            "origin": "Déduit pendant la discussion à la cafétéria.",
            "card": "gui/day3/argument_card_exact_wording.png",
        },
        "echanges_discrets": {
            "title": "Échanges discrets déjà actifs",
            "category": "Réseaux informels",
            "summary": "Des échanges informels existent déjà. Les nier ne les fait pas disparaître.",
            "origin": "Observé dans la salle de stockage.",
            "card": "gui/day3/argument_card_exact_wording.png",
        },
    }

    def day3_vote_bootstrap():
        store.j2_vote_codex_unlocked = True
        if "DAY2_VOTE_ARGUMENTS" in globals():
            for _arg_id, _arg_data in DAY3_VOTE_ARGUMENTS.items():
                if _arg_id not in DAY2_VOTE_ARGUMENTS:
                    DAY2_VOTE_ARGUMENTS[_arg_id] = _arg_data

    def day3_vote_argument_drop(drags, drop, arg_id):
        if drop is not None and getattr(drop, "drag_name", "") == "day3_briefcase_drop":
            if day2_vote_add_argument(arg_id):
                store.j3_codex_dot = True
                return True
        renpy.restart_interaction()
        return False

screen day3_current_vote_codex(called=False):
    modal True
    zorder 200
    $ vote_codex_j45 = getattr(store, "j45_vote_codex_active", False)
    add Solid("#080d12")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 960
        padding (28, 24)
        background Solid("#07151ef5")
        vbox:
            spacing 18
            hbox:
                xfill True
                vbox:
                    spacing 4
                    text "Codex" size 22 color "#3a9fca"
                    text "Prochain vote" size 48 color "#daeaf5" font "fonts/Rajdhani-SemiBold.ttf"
                textbutton "Retour":
                    xalign 1.0
                    yalign 0.5
                    xsize 150
                    background Solid("#1a2530")
                    hover_background Solid("#2d3a45")
                    text_color "#dff8ff"
                    action If(called, Return(), Hide("day3_current_vote_codex"))
            hbox:
                spacing 22
                frame:
                    xsize 500
                    yfill True
                    padding (22, 18)
                    background Solid("#0d2230")
                    vbox:
                        spacing 12
                        text "Vote en cours" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        if vote_codex_j45:
                            text "Autoriser ou non les déplacements entre les districts." size 22 color "#dff8ff"
                            text "Moment prévu : Jour 6, 14h00" size 19 color "#9ed8ff"
                        else:
                            text "Ça serait bien qu'on réautorise le commerce comme avant." size 22 color "#dff8ff"
                            text "Moment prévu : Jour 3, 14h00" size 19 color "#9ed8ff"
                        text "Résumé neutre" size 21 color "#70c6e8"
                        if vote_codex_j45:
                            text "Le texte promet une circulation plus libre des personnes entre districts. Ses effets restent incertains selon les frontières, la sécurité et les capacités d'accueil." size 20 color "#b8d8e4"
                        else:
                            text "Le texte promet une circulation plus libre des biens. Ses effets restent incertains selon les districts, les procédures et les risques locaux." size 20 color "#b8d8e4"
                        null height 8
                        text "Arguments découverts" size 24 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        for arg_id in dossier_prop_args("p1_vote_commerce"):
                            if arg_id in j2_vote_arguments:
                                $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
                                frame:
                                    xfill True
                                    padding (12, 10)
                                    background Solid("#123044")
                                    vbox:
                                        spacing 3
                                        text kd_tr(arg["title"]) size 21 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text kd_tr(arg["summary"]) size 17 color "#b8d8e4"
                                        text kd_tr(arg["origin"]) size 15 color "#74a8ba"
                            else:
                                frame:
                                    xfill True
                                    padding (12, 12)
                                    background Solid("#111820")
                                    text "Argument non découvert" size 18 color "#526d79"
                fixed:
                    xfill True
                    yfill True
                    draggroup:
                        for cidx, col_data in enumerate(DAY2_VOTE_COLUMNS):
                            $ col_id = col_data[0]
                            $ col_label = col_data[1]
                            drag:
                                drag_name ("day2_vote_col_%s" % col_id)
                                draggable False
                                droppable True
                                xpos (20 + cidx * 340)
                                ypos 0
                                xsize 318
                                ysize 810
                                frame:
                                    xfill True
                                    yfill True
                                    padding (14, 14)
                                    background Solid("#0c1d29")
                                    vbox:
                                        spacing 8
                                        text kd_tr(col_label) xalign 0.5 size 28 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text "Glisse les portraits ici." xalign 0.5 size 16 color "#6797aa"
                        for cid in DAY2_VOTE_CHARACTER_ORDER:
                            $ card_x, card_y = day2_vote_card_xy(cid)
                            $ cdata = DAY2_VOTE_CHARACTERS[cid]
                            drag:
                                drag_name ("day2_vote_char_%s" % cid)
                                xpos card_x
                                ypos card_y
                                xsize 142
                                ysize 116
                                draggable True
                                droppable False
                                dragged (lambda drags, drop, cid=cid: day2_vote_position_dragged(cid, drags, drop))
                                frame:
                                    xfill True
                                    yfill True
                                    padding (7, 7)
                                    background Solid("#182d3a")
                                    vbox:
                                        spacing 3
                                        add cdata["portrait"] xalign 0.5 xysize (62, 62)
                                        text "[cdata['name']]" xalign 0.5 size 17 color "#dff8ff"

screen day3_phone_vote_notice():
    modal True
    zorder 160
    add Solid("#02050bd9")
    fixed:
        xalign 0.5
        yalign 0.5
        xsize 560
        ysize 940
        add "gui/day3/phone_frame.png" xalign 0.5 yalign 0.5
        add "gui/day3/phone_screen_vote.png" xpos 65 ypos 82
        vbox:
            xpos 96
            ypos 168
            xsize 365
            spacing 18
            text "Dossier actif" size 25 color "#9ed8ff" font "fonts/Rajdhani-SemiBold.ttf"
            text "Ça serait bien qu'on réautorise le commerce comme avant." size 22 color "#dff8ff"
            text "Arguments rangés : [day2_vote_argument_count()] / [len(DAY2_VOTE_ARGUMENTS)]" size 20 color "#b8d8e4"
            text "Les positions restent modifiables dans le Codex." size 19 color "#74a8ba"
        hbox:
            xpos 112
            ypos 688
            spacing 28
            imagebutton:
                idle "gui/day3/phone_icon_vote.png"
                hover "gui/day3/phone_icon_vote.png"
                action Return("codex")
            imagebutton:
                idle "gui/day3/phone_icon_codex.png"
                hover "gui/day3/phone_icon_codex.png"
                action Return("codex")
        textbutton "Continuer":
            xpos 175
            ypos 802
            xsize 210
            background Solid("#123044")
            hover_background Solid("#1c526b")
            text_color "#dff8ff"
            action Return("continue")

screen day3_argument_briefcase(arg_id):
    $ arg = DAY3_VOTE_ARGUMENTS[arg_id] if arg_id in DAY3_VOTE_ARGUMENTS else DAY2_VOTE_ARGUMENTS[arg_id]
    use vote_argument_briefcase(arg_id, arg, "day3_argument_card", "day3_briefcase_drop", day3_vote_argument_drop)

label day3_play_wakeup_trace:
    call trace_qte_run(mg_id="trace_day3_wakeup", title="RÉVEIL — JOUR 3", path_type="curve_right", time_limit=7.0, wait_time=0.8, tolerance=60, max_errors=4, anchor_x=930, anchor_y=640, required=True) from _call_trace_qte_run_3
    return True

label day3_play_corridor_trace:
    call trace_qte_run(mg_id="trace_day3_corridor", title="VIRAGE SERRÉ", path_type="arc", time_limit=5.0, wait_time=0.5, tolerance=58, max_errors=4, anchor_x=960, anchor_y=650, required=False) from _call_trace_qte_run_4
    if _return != "FAIL":
        "Je prends le virage sans ralentir."
        return True
    else:
        "Mon épaule tape contre le mur. Nyra ne ralentit même pas."
        return False

label day3_collect_vote_argument(arg_id):
    call screen day3_argument_briefcase(arg_id)
    if _return:
        play sound sfx_drop
        call screen day2_argument_deposit_success(DAY3_VOTE_ARGUMENTS[arg_id] if arg_id in DAY3_VOTE_ARGUMENTS else DAY2_VOTE_ARGUMENTS[arg_id])
        $ chapter1_check_complete_dossier()
    return


# ============================================================================
# JOUR 3 — Canon (réécriture)
# Structure : réveil (froid) → cafétéria (douceur) → clash Julian (tension)
#            → transition (accalmie) → Conclave : débat 3 phases avec
#              2 cliffhangers → vote (unanimité réelle).
# ============================================================================

# Transforms d'ambiance du Jour 3.
init -1:
    # Mise en avant ponctuelle d'un personnage (déclaration de vote d'Elen).
    transform day3_vote_pop:
        xcenter 0.5
        yalign 1.0
        zoom 1.0
        easein 0.14 zoom 1.16
        easeout 0.26 zoom 1.06

    # Secousse « course » appliquée au décor de couloir pendant que les persos courent.
    transform day3_run_shake:
        subpixel True
        block:
            linear 0.06 yoffset 6 xoffset -4
            linear 0.06 yoffset -5 xoffset 5
            linear 0.06 yoffset 4 xoffset -3
            linear 0.06 yoffset 0 xoffset 0
            repeat

label _3_CANON:

    $ day_id = 3
    $ current_day = 3
    $ noam_has_juliette_drawing = True
    $ day3_vote_bootstrap()
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    pause 0.5

    think "Je suis réveillé avant l'annonce de Kami. Première victoire de la journée : l'IA n'a pas eu besoin de me tirer du lit."
    think "Deuxième victoire : je n'ai pas encore vomi en pensant à quatorze heures."
    scene bg_cg012 at adaptive_fullscreen with fade
    $ blink()
    think "Un seul non et on repart à zéro. Douze inconnus, une urne et une phrase qui pourrait faire basculer le monde."
    think "J'aimerais croire que ce sera aussi simple qu'une couleur sur un écran."
    think "Je saisis ma tablette. Hier, elle débordait d'arguments. Aujourd'hui, il va falloir faire quelque chose de tout ça."

    play sound sfx_announce
    pause 1.0

    # ── Diffusion du matin : Kami joueuse mais tranchante ──
    stop music fadeout 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Booooonjour, mes douze petites consciences ! Vous avez une mine à faire pâlir mes caméras."
    kami "Pas dormi ? Tant mieux ! Une décision historique mérite quelques cernes. C'est plus photogénique."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "AUJOURD'HUI... C'EST LE JOUR DU VOOOOOTE ! Oui ! Le premier ! J'ai préparé des effets sonores et tout !"
    kami "L'un de vous a griffonné une idée sur une feuille. Dans quelques heures, on saura si elle mérite de devenir une règle... ou du papier recyclé."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Un seul « non » et pouf ! Plus d'amendement. Je sais, je me répète. Mais c'est tellement délicieux que je ne m'en lasse pas."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Soyez gentils les uns avec les autres, surtout ! De petits sourires, des encouragements, aucune menace... ou presque."
    kami "Conclave, quatorze heures. Douze sièges, douze têtes. J'aimerais beaucoup qu'il y ait autant de têtes en repartant."

    pause 0.3
    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "Même ses menaces n'arrivent pas à gâcher mon envie de réussir. C'est presque inquiétant : je commence à ressembler à Elen."
    scene bg_chambre at adaptive_fullscreen with fade
    think "Je m'habille. Le miroir me renvoie la tête de quelqu'un qui essaie d'avoir l'air sûr de lui."
    think "Il ne fait pas semblant très bien."
    think "D'abord manger. Après, convaincre onze personnes de ne pas faire exploser cette journée."

    # Trajet jouable : chambre -> dortoir -> couloir -> cafétéria.
    # Kael et Julian peuvent être croisés, mais leurs dialogues restent optionnels.
    $ day3_cafeteria_route_kael_seen = False
    $ day3_cafeteria_route_julian_seen = False
    $ current_scene_active = "_3_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    $ room_scene_indices["chambre"] = 2
    jump CHAMBRE_TP


label _3_OPT_KAEL_DIAL:
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_158
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ day3_cafeteria_route_kael_seen = True

    think "Kael est assis dans le dortoir. Il fait tourner sa tablette entre ses doigts sans jamais l'allumer. Il a cette tête qu'on fait devant une machine en panne."

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("kael", "fatigue", 0.65),
    ])

    kael fatigue "Ah... Noam. J'ai entendu des pas. J'espérais presque que ce soit un technicien."

    think "Il a l’air d’avoir très peu dormi."

    noam "Tu descends manger, ou tu as décidé de t'installer dans ce couloir ?"

    kael reflechit "Dans une minute. J'essaie de ne pas penser au vote. Pour l'instant, c'est un échec monumental."

    noam "C'est toujours le commerce qui te travaille ?"

    kael inquiet "J'en entends qui disent que ça ne changera rien. Et d'autres qui parlent déjà comme si tout était gagné."
    kael inquiet "Sur Orbite, une livraison retardée peut tuer des gens. Et une livraison mal contrôlée aussi. Je suis censé être rassuré par quoi, exactement ?"

    kael mefiant "On vit grâce à des cargaisons régulières. Si tout le système change du jour au lendemain, je ne peux pas juste croiser les doigts."

    think "Il ne cherche même pas à me convaincre. C'est peut-être ça qui me trouble : il a vraiment peur."

    # Déblocage optionnel de l'argument « Risque de dépressurisation » (sinon disponible au Jour 2).
    call day3_collect_vote_argument("orbite") from _call_day3_collect_vote_argument_orbite

    think "Kael baisse les yeux vers sa tablette sans l’allumer."

    noam "Donc... tu penses voter contre ?"

    kael surpris "Non ! Enfin... je suis plutôt pour. Sur le principe."
    kael doute "En pratique, c'est une autre histoire."
    kael culpabilite "J'ai déjà dû fermer une porte sur deux personnes pour en sauver d'autres. Je sais ce que coûte une mauvaise décision."
    kael inquiet "Et je déteste que les autres me regardent comme si j'avais toutes les réponses."

    noam "Je comprends. Mais maintenir les règles actuelles, c'est aussi une décision. Et on sait déjà qu'elles font des dégâts."

    kael calme "Ouais... On verra quand on aura le bulletin devant nous."
    kael sourire "Merci d'être passé. Au moins, j'ai arrêté de fixer ma tablette pendant deux minutes."

    hide noam
    hide kael

    think "Il a l'air d'avoir deux opinions contradictoires, et de bonnes raisons pour chacune. J'espère qu'il choisira avant de prendre son bulletin."

    pause 0.5
    jump DORTOIR_TP

label _3_OPT_JULIAN_DIAL:
    scene expression Image(corridor_background("cafeteria")) at adaptive_fullscreen with dissolve
    $ day3_cafeteria_route_julian_seen = True
    think "Julian donne de petites tapes au distributeur. Il négocie manifestement avec une machine qui n'a aucunement l'intention de le respecter."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("julian", "joie", 0.75),
    ])

    julian joie "Noam ! Quelle journée ! On pourrait entrer dans l'histoire d'ici quelques heures !"
    noam sourire "T'as pris combien de cafés avant de dire bonjour ?"
    julian rire "Un seul, mais il suffit de savoir se motiver. Tu devrais essayer devant un miroir."
    "La tasse de Julian déborde. Il la retire trop tard et se brûle les doigts."
    julian colere "AÏE ! Cette machine a décidé de saboter mon discours !"
    noam sourire "Tu peux toujours lui expliquer ton programme. Peut-être qu'elle votera pour toi."
    julian sourire "Très spirituel. Mais imagine : des gens qui achètent et vendent sans supplier Kami de leur donner la permission. On peut y arriver."
    noam inquiet "À condition que tout le monde accepte aussi la disparition des rations. J'ai croisé Kael, il n'est pas tranquille."
    julian reflexion "Je sais. C'est précisément pour ça qu'il faut parler aux indécis. Il faut les amener avec nous."
    noam calme "Les convaincre, pas les coincer dans un couloir jusqu'à ce qu'ils disent oui."
    julian sourire "Je sais faire la différence, Noam. Et crois-moi, je sais parler aux gens."
    noam reflechit "C'est justement ce qui m'inquiète."
    julian taquin "Tu t'inquiètes trop. Ça ne fait pas gagner des élections, tu sais."
    noam neutre "On n'est pas en campagne."
    julian sourire "Pas officiellement."
    think "Il part avant que je puisse répondre. Il a l'assurance de quelqu'un qui n'imagine pas une seule seconde être le problème."

    call day3_collect_vote_argument("monde_avant") from _call_day3_collect_vote_argument_monde_avant

    hide noam
    hide julian

    return

label _3_CAFETERIA_ARRIVE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_159
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    think "La cafétéria ressemble à une salle d'attente avant une opération : certains bavardent trop fort, les autres regardent leur plateau comme s'il allait les sauver."
    think "J'avais envie d'un petit-déjeuner tranquille. Manifestement, ce n'est pas aujourd'hui."

    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("noam", "neutre", 0.82),
        ("elen", "joie", 0.22),
        ("iris", "fatigue", 0.50),
    ])

    pause 0.3

    scene bg_cg013 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg013")

    think "Elen a créé une chose qui ressemble à des pâtes prises en otage par des noix. Iris fixe le bol comme si elle évaluait sa dangerosité."

    pause 0.3

    iris "C'est quoi, ce truc ? Tu as vidé les poubelles du distributeur dans ton bol ?"

    elen "C'est. Mon. CHEF-D'ŒUVRE !"

    iris "Chaque fois que tu annonces un chef-d'œuvre, je m'attends à devoir appeler les secours."

    elen "Mais naaaan, ch'est des pâtes, des noix et une touche checrète !"
    "Elle parle la bouche pleine, incapable de s'en empêcher."

    iris "Une touche secrète. C'est comme ça qu'on finit à l'infirmerie avec une allergie incompréhensible."

    elen "Goumi a approuvé ! Il a même fait bip !"
    elen "Un robot qui fait bip, c'est forcément bon signe ! Enfin... presque."

    iris "Je te rappelle qu'il fait aussi bip quand il lave les tables."

    think "Elen goûte une bouchée et sourit immédiatement."

    elen "MMMMH ! C'est encore meilleur que dans ma tête !"

    iris "Elle a survécu à la première bouchée. Je suis presque déçue."

    elen "J'ai le droit d'être heureuse, moi ! Tu devrais essayer, ça change la vie !"

    iris "Je le serai quand tu auras fini de mâcher."

    think "Mon petit-déjeuner se compose de pain et de jus. Rien qui nécessite un comité d'éthique."

    scene bg_cg013_1 at adaptive_fullscreen with fade
    think "Elen me regarde avec de grands yeux suppliants, puis me montre son bol."

    elen "T'as vu ? Mon regard irrésistible ! Goumi n'a pas pu dire non !"

    iris "Tu as surtout appuyé six fois sur le bouton, non ?"

    elen "C'est parce que j'ai pratiqué ! Regarde, je peux le refaire !"

    scene bg_cg013 at adaptive_fullscreen with fade
    pause 0.3

    iris inquiet "Dis... tu n'as pas peur ? Même une toute petite seconde ?"

    elen triste "Bien sûr que j'ai peur ! J'ai peur depuis qu'on s'est réveillés ici."
    elen triste "Mais si je me mets à pleurer devant chaque assiette, je vais faire quoi pendant trente jours ?"
    elen content "Alors je mange. Et j'essaie de faire comme si tout allait bien. C'est idiot ?"

    iris surpris "...Non."

    elen taquin "Tu avais préparé un sermon, pas vrai ?"

    iris triste "Un tout petit."

    elen taquin "Vas-y ! Promis, je l'écoute entre deux bouchées."

    iris fatigue "Non. Pour une fois, je vais te laisser tranquille."

    think "Elias arrive juste au moment où la conversation devient presque touchante. Il pose son plateau et regarde le bol."

    # On quitte le CG (où les persos sont déjà dessinés) et on regroupe TOUS les
    # locuteurs présents dans un seul showGroup, complété à chaque nouvelle arrivée.
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elen", "joie"),
        ("iris", "taquin"),
        ("elias", "neutre"),
    ])

    elias sourire "Salut ! Euh... tu as perdu un pari, Elen ?"
    elen joie "C'est mon petit-déjeuner de championne ! Tu veux goûter ?"
    elias peur "Oh, non merci. Moi, je mise sur les protéines. J'ai un programme, tu comprends."
    iris taquin "Enfin un témoin ! Je commençais à croire que j'étais la seule à voir ce bol."
    elen desaccord "Vous êtes insupportables ! C'est VOUS qui ne savez pas manger !"
    elias sourire "Avec ça, tu auras faim dans une heure. Moi, j'ai pris des œufs et du poulet. Des vraies protéines !"
    elen surpris "DU POULET ?! À CETTE HEURE-CI ?! Mais tu es fou !"
    iris taquin "Je ne pensais pas dire ça, mais... Elen a raison."
    elias colere "Quoi ?! Le poulet, c'est parfaitement normal ! Vous avez un problème avec les poulets ?!"
    elen sourire "Bon ! Vous êtes officiellement interdits de commenter mon assiette. Et le vote aussi. Juste cinq minutes !"
    elias inquiet "J'aimerais bien. Mais j'ai l'impression d'avoir un compte à rebours dans le crâne. Vous avez décidé, vous ?"
    iris fatigue "Je lirai le texte. Hier, on a débattu pendant des heures d'une phrase écrite comme une liste de courses."
    elen inquiet "Mais à force de vouloir être sûrs de tout, on va rester coincés à attendre qu'une autre personne décide."
    noam calme "J'ai peur de ce qu'on risque de supprimer. Mais j'ai aussi peur de ce qui arrivera si on ne change jamais rien."
    elen joie "Voilà ! C'est exactement ce que je voulais dire ! Alors écoutez bien..."

    # Mise en avant d'Elen : elle se lève et s'avance (recentrage + pop de zoom).
    show elen joie at day3_vote_pop zorder 60
    elen joie "Moi, je voterai POUR !"

    pause 0.4

    think "Elle parle si fort que les voisins de table se retournent. Iris lui fait signe de baisser le ton, mais Elen continue de sourire."

    # Elen se rassoit : on restaure le groupe attablé.
    $ showGroup([
        ("elen", "joie"),
        ("iris", "reflechit"),
        ("elias", "sourire"),
    ])

    iris reflechit "Tu annonces ça comme si tu choisissais un dessert."

    elen inquiet "Tu crois que j'ai décidé ça pour rigoler ? J'y ai pensé toute la nuit."
    elen triste "Je sais que des gens nous regardent, peut-être même ma famille. Si je reviens sans avoir rien tenté, je leur raconterai quoi ?"

    iris reflechit "..."

    elias sourire "Bon... dit comme ça, je comprends."

    think "Julian s’approche avec son café quand il entend Elen parler du vote."
    $ showGroup([
        ("elen", "joie"),
        ("iris", "hesitation"),
        ("elias", "neutre"),
        ("julian", "neutre"),
    ])

    julian "On parle d'un vote favorable ? Je savais que je trouverais des gens raisonnables ici !"

    elen rire "Bienvenue au club ! Il nous manque une devise et des badges !"

    julian sourire "Évidemment, je suis pour ! Et je constate que ma secrétaire préférée a déjà commencé à rassembler les voix."

    iris hesitation "Julian... tu n'es pas obligé d'en faire un spectacle."

    julian reflechit "Je n'en fais pas un spectacle. Je fais preuve de transparence ! Il faut que les gens sachent sur qui compter."

    think "Plusieurs personnes aux tables voisines nous regardent maintenant. Elen n’a pas l’air de s’en rendre compte."

    elen taquin "Bon ! Qui d'autre est pour ? Je promets de ne pas noter les noms !"

    think "Julian lève la main très haut et vérifie du coin de l’œil si on le regarde."

    julian rire "POUR ! J'ai répondu assez fort pour ceux du fond ?"

    think "Tout le monde se tourne vers moi."

    noam reflechit "Et tu ne veux même pas lire la version définitive ?"

    elen colere "Mais j'ai réfléchi ! Arrêtez de me regarder comme si j'avais choisi au hasard !"

    iris fatigue "Vous pouvez parler moins fort ? Un indécis qui se sent interrogé, vous allez surtout réussir à le faire fuir."

    elias "Je penche pour. Mais si ça n'aide pas vraiment les gens à travailler et à obtenir ce qui manque, on aura voté pour quoi ?"

    think "Kael tente de passer avec son plateau. Elen lui barre la route en souriant."

    $ showGroup([
        ("elen", "joie"),
        ("iris", "fatigue"),
        ("elias", "neutre"),
        ("julian", "neutre"),
        ("kael", "neutre"),
    ])

    pause 0.4

    elen joie "Kael ! Toi aussi, tu viens dans notre club ?"

    kael "...Je ne sais pas. Je déciderai devant le bulletin."

    elen "Ah. Bon... tu peux quand même prendre un badge imaginaire."

    think "Kael s'éclipse sans demander son reste."
    $ showGroup([
        ("elen", "joie"),
        ("iris", "reflechit"),
        ("elias", "neutre"),
        ("julian", "neutre"),
    ])

    think "Mara arrive. Elle inspecte les plateaux, puis les visages. Toujours dans cet ordre."

    $ showGroup([
        ("elen", "joie"),
        ("iris", "reflechit"),
        ("elias", "neutre"),
        ("julian", "neutre"),
        ("mara", "neutre"),
    ])

    mara taquin "Oh, quelle belle petite cérémonie ! Vous comptez afficher vos votes sur vos vêtements aussi ? Kami doit adorer."

    elen joie "Oh non, elle nous a démasqués ! Tous mes plans de campagne sont fichus !"

    iris reflechit "Et toi, Mara ? Tu as déjà décidé de faire ton numéro contre tout le monde ?"

    mara taquin "C'est fou, ça. Je dis bonjour et vous m'attribuez déjà un bulletin."
    mara reflechit "Je ne suis pas contre le commerce. Je suis contre l'idée de voter les yeux fermés juste pour être applaudis."

    elen colere "C'est du commerce, pas un plan pour exterminer les bébés pingouins !"

    mara doute "T'as lu le texte définitif ? Non ? Alors pourquoi t'es si sûre ?"

    mara colere "Je veux lire ce qu'on va VRAIMENT voter. Je demande la lune, peut-être ?"

    elen colere "Et si on attend d'être absolument sûrs, on ne fera rien ! Les gens ont besoin qu'on essaie !"

    mara triste "Je le sais. Mais si ça tourne mal, ceux qui paieront ne seront pas assis à cette table."
    mara triste "Et encore moins Kami."

    noam reflechit "Mara a raison sur un point : si Kami change le sens du texte, on aura passé deux jours à débattre d'une proposition qui n'existe plus."
    mara reflechit "Voilà. Je ne confierais déjà pas ma liste de courses à Kami. Alors la vie des gens..."
    elen inquiet "Je voulais juste qu'on se soutienne..."
    mara triste "Je sais, Elen. Mais nous soutenir, ça veut aussi dire être capables de dire non."
    julian colere "Dire non sans raison, c'est condamner tout le monde à attendre !"
    iris desaccord "Et vous êtes repartis. C'était combien, déjà, les cinq minutes de paix ?"
    think "Mara ne sourit plus. Julian, lui, ne regarde même pas Elen."

    call day3_collect_vote_argument("enonce_precis") from _call_day3_collect_vote_argument_enonce_precis

    pause 0.3

    think "Pour la première fois, je réalise que mon optimisme et la prudence de Mara ne sont pas forcément incompatibles. C'est une découverte dérangeante."

    think "Elen repousse son bol vide, visiblement satisfaite."

    elen content "Bon ! Mon chef-d'œuvre est terminé ! Et je suis toujours vivante !"
    elen taquin "Maintenant, je vais parler aux autres ! Ça m'a l'air d'une meilleure idée que de me faire engueuler ici."

    iris "Bonne chance. Et évite de les coincer dans les toilettes."

    elen rire "Promis ! Je suis une professionnelle du charme !"

    hide elen with moveoutleft

    pause 0.4

    $ hideGroup()
    "Peu à peu, la cafétéria se vide. Bientôt, il ne reste qu'Iris et moi."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("iris", "neutre", 0.60),
    ])

    iris fatigue "Tu vois ? On avait demandé cinq minutes sans parler du vote..."
    iris fatigue "...On a tenu quoi ? Quinze secondes ?"

    "Puis elle sort à son tour."
    hide iris with moveoutleft

    think "La table est presque vide. J'étais entré ici persuadé qu'on pouvait tous s'entendre. Je repars en me demandant si on a seulement entendu les mêmes mots."

    stop music fadeout 0.8

    "Que faire en attendant ?"

    call START_FREE_TIME("_3_PAUSE_CHAMBRE") from _call_START_FREE_TIME_3_1


label _3_PAUSE_CHAMBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_161
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ current_period = "Après-midi"

    "Je suis remonté dans ma chambre pour souffler un peu."
    think "Bientôt l'heure. Autant fermer les yeux deux minutes."

    play sound sfx_knock
    think "On frappe. Fort."
    pause 0.2
    play sound sfx_knock
    pause 0.2

    nyra "Noam. Ouvre."

    think "Ce n'est pas la voix de quelqu'un qui vient discuter."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_162
    scene bg_dortoir at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("nyra", "neutre", 0.60),
    ])

    nyra stress "Noam, viens. Julian est avec Tomas dans la salle de repos, et ça se passe vraiment mal."
    noam inquiet "Mal comment ? Ils se disputent ?"
    nyra colere "Julian lui demande de promettre qu'il votera pour et surtout qu'il le soutiendra devant les autres. Tomas a essayé de partir, mais il ne le lâche pas."
    noam colere "Il est sérieux ? Mais pourquoi il s'acharne sur Tomas ?"
    nyra stress "Parce qu'il sait que Tomas a du mal à dire non. S'il continue, Tomas risque de voter contre juste pour qu'on lui fiche la paix."
    noam determine "Bon, on y va."
    nyra neutre "Et essaie de ne pas t'engueuler avec Julian. Si vous vous mettez tous les deux contre lui, on aura rien arrangé."

    stop music fadeout 0.5
    play music "music/bgm_world_decline.mp3" fadein 0.6

    # Effet de course : le décor tremble tant qu'on court (secousse day3_run_shake).
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_163
    scene couloir_dortoir at adaptive_fullscreen, day3_run_shake with fade

    think "On part immédiatement. Nyra a reçu un message de Tomas qui lui demandait de venir."

    play sound sfx_run

    think "Nyra court devant moi. J’ai du mal à la suivre dans les virages, mais je ne veux pas laisser Tomas seul avec Julian plus longtemps."

    play sound sfx_run

    # Trois virages enchaînés : chaque réussite = du temps gagné, donc moins de
    # temps pour Julian d'user Tomas. Le total module l'influence sur Tomas.
    $ day3_corridor_success = 0

    call trace_qte_run(mg_id="trace_day3_corr1", title="VIRAGE 1/3", path_type="arc", time_limit=5.0, wait_time=0.4, tolerance=58, max_errors=4, anchor_x=960, anchor_y=650, required=False, show_results=False) from _call_day3_corr1
    if _return != "FAIL":
        $ day3_corridor_success += 1

    call trace_qte_run(mg_id="trace_day3_corr2", title="VIRAGE 2/3", path_type="curve_right", time_limit=4.6, wait_time=0.3, tolerance=56, max_errors=4, anchor_x=960, anchor_y=650, required=False, show_results=False) from _call_day3_corr2
    if _return != "FAIL":
        $ day3_corridor_success += 1

    call trace_qte_run(mg_id="trace_day3_corr3", title="VIRAGE 3/3", path_type="arc", time_limit=4.2, wait_time=0.25, tolerance=54, max_errors=4, anchor_x=960, anchor_y=650, required=False, show_results=False) from _call_day3_corr3
    if _return != "FAIL":
        $ day3_corridor_success += 1

    if day3_corridor_success == 3:
        $ unlock_succes("succes008")

    python:
        # Plus on arrive vite, plus Tomas est épargné par Julian (bonus au vote).
        if day3_corridor_success >= 3:
            store.tomas_corridor_delta = 2
        elif day3_corridor_success == 2:
            store.tomas_corridor_delta = 1
        elif day3_corridor_success == 1:
            store.tomas_corridor_delta = 0
        else:
            store.tomas_corridor_delta = -2

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_164
    scene couloir_cafeteria at adaptive_fullscreen with fade
    think "J'entends Julian derrière la porte. Il parle encore plus fort que d'habitude."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_165
    scene bg_repos at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("nyra", "neutre", 0.25),
        ("julian", "neutre", 0.55),
        ("tomas", "neutre", 0.85),
    ])

    if day3_corridor_success >= 2:
        think "On arrive assez vite pour entendre Tomas demander à Julian de le laisser partir."
        tomas inquiet "Je t'ai dit que je voulais réfléchir tout seul. Pourquoi tu continues ?"
        julian sourire "Parce que le vote est dans une heure et que si tu attends trop, tu risques de prendre une décision sur un coup de tête."
    else:
        think "Tomas est coincé entre une table et Julian. Il tient sa tablette contre lui, très énervé."
        julian rire "Tomas, dis-moi juste que tu me soutiens et on en finit. Tu n'as même pas de meilleure idée !"
        tomas peur "Mais j'en sais rien ! Ça fait dix minutes que je te le dis !"
    julian sourire "Allez. Tu viens avec moi au Conclave, tu expliques aux autres que tu es pour, et après je te laisse tranquille."
    tomas inquiet "Mais j'ai pas dit que j'étais pour !"
    "Julian se retourne vers nous. Tomas en profite pour s'éloigner de lui."

    call day3_julian_clash_minigame from _call_day3_julian_clash_minigame

    noam colere "Julian, ça suffit. Il t'a demandé de le laisser tranquille, tu l'as entendu ou pas ?"
    julian colere "Ah, Noam. Parfait. Nyra a donc appelé du renfort ?"
    nyra neutre "Tomas m'a demandé de venir. Il voulait partir et tu continuais à insister."
    julian reflexion "Je lui expliquais pourquoi son soutien comptait. On dirait que discuter est devenu interdit."
    tomas inquiet "Non ! Tu voulais que je dise à tout le monde que je te soutiens, toi ! Et tu m'écoutais même pas !"
    julian hesitation "Tomas, tu déformes ce que j'ai dit."
    noam colere "On t'a entendu en arrivant. Tu voulais même lui faire répéter ta phrase."
    julian colere "Et toi, tu fais quoi depuis ce matin ? Tu te promènes en espérant que tout le monde va finir par tomber d'accord ?!"
    noam colere "Au moins, j'essaie pas de forcer les autres à voter comme moi !"
    julian colere "Tu crois que je fais ça pour m'amuser ? Un seul non et tout ce qu'on a tenté ne sert à rien !"
    noam colere "Alors parle de l'amendement ! Pas de qui doit te soutenir devant les caméras !"
    julian colere "C'est facile de jouer les gentils quand tu laisses aux autres le boulot de convaincre !"
    tomas inquiet "Mais arrêtez tous les deux ! Je suis là, vous savez !"
    "Je me tourne vers Tomas. Il tremble de colère, et je réalise que je viens aussi de parler à sa place."
    noam culpabilite "T'as raison, désolé. Je voulais pas te mettre au milieu."
    julian hesitation "Tomas, je..."
    tomas inquiet "Non ! Laisse-moi finir ! J'ai peut-être envie de voter pour, mais là, franchement, vous me donnez envie de vous envoyer promener tous les deux !"
    nyra raison "Tomas n'a pas à vous promettre quoi que ce soit. Julian, tu peux partir ? Noam, reste deux minutes avec nous."
    julian colere "Très bien. Mais si on perd parce que personne n'a voulu convaincre les indécis, vous y repenserez."
    noam colere "Et toi, essaie de comprendre que les gens ont le droit d'hésiter."
    julian colere "On verra tout à l'heure."

    hide julian with moveoutleft

    stop music fadeout 0.6
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6

    tomas hesitation "Je lui ai dit que je voulais réfléchir. Je sais pas pourquoi il a pas compris."
    noam triste "Je suis désolé aussi. Je lui ai crié dessus sans même te demander ce que tu voulais."
    tomas hesitation "Je voudrais que ça passe, je crois. Mais si les gens n'ont plus leurs rations et que ça se passe mal, on fait quoi ?"
    nyra neutre "Tu voteras sur le texte qu'on aura devant nous, pas sur ce que Julian ou Noam veulent entendre."
    tomas inquiet "Ouais... J'aurais juste aimé qu'on me laisse un peu de temps."
    noam determine "Je comprends. On se retrouve au Conclave ?"
    tomas hoche_la_tete "Ouais. Et s'il vous plaît, arrêtez de vous battre pour moi."
    nyra sourire "Je reste un moment avec lui. Merci d'être venu, Noam."
    think "Ils partent ensemble. Je ne sais pas si j'ai vraiment aidé Tomas, et je me demande si Julian va essayer de se venger pendant le débat."
    $ hideGroup()

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite


label _3_TRANSITION_CONCLAVE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_166
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Je retrouve les autres dans le couloir. Tout le monde avance vers le Conclave, mais personne n’a vraiment envie de discuter."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    think "Je repense à Tomas. J’aimerais que le texte passe, mais pas parce que quelqu’un aura eu trop peur de dire non. Je suis encore déterminé à essayer, même après cette dispute."

    $ showGroup([
        ("lysa", "neutre", 0.25),
        ("noam", "neutre", 0.50),
    ])

    "Lysa marche en retrait. Juste assez pour que ça se remarque."
    "Le groupe accélère quand le couloir se resserre. Elle, non. Elle traîne les pieds, exprès."

    lysa triste "On va voter. On va échouer."
    lysa triste "Et demain on sera encore coincés ici. Dans trois jours, on recommencera."
    lysa blase "On est douze à jouer les députés pendant qu'elle décide de tout."

    think "Lysa dit ça sans vraiment attendre de réponse. Elle paraît déjà convaincue qu’on va échouer."

    noam reflechit "On n'a pas encore voté, Lysa."
    noam sourire "Attends au moins le résultat avant de nous enterrer."

    "Lysa fait une moue déconfite alors qu'on approche de la porte du Conclave."

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    think "Sael s'est laissée glisser à l'arrière du groupe, elle aussi. Volontairement. Elle observe Lysa depuis un moment."
    "Sans prévenir, sans théâtre, elle attrape Lysa et la serre contre elle."

    sael "Lysa... Tu as l'air épuisée."
    sael "Tu vois les problèmes avant tout le monde. C'est utile. Mais tu peux aussi te reposer un peu."
    sael "On aura besoin de toi pendant le vote."

    "Elle pointe la poitrine de Lysa du doigt. Les épaules de Lysa se relâchent, à peine."

    lysa "Tu dramatises. Je suis toujours là."

    sael "Je sais. Je te demande juste de ne pas abandonner avant d'avoir essayé."

    lysa "Bon. Mais tu me devras un café après ça."

    sael sourire "Deux, même. Et sans formulaire."

    lysa blase "Touché. Bref. On y va avant que je devienne sentimentale."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_167
    scene bg_conclave at adaptive_fullscreen with dissolve

    think "On entre. On s'installe. Voilà. C'est parti."

    play sound sfx_announce
    pause 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous voilà tous ! Douze fauteuils, douze silhouettes. Personne ne manque à l'appel."
    kami "Ce serait dommage. Les chaises vides, ça déprime l'audience."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Et je vois des visages émus ! Il y a eu de la tendresse dans les couloirs, on dirait."
    kami "Cameraman, un gros plan sur ces petites âmes fragiles."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Installez-vous. On commence dans un instant."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade
    pause 0.4

    "Les portes se referment. Un déclic net résonne derrière nous."

    play sound sfx_door

    think "Les portes viennent de se verrouiller. Je vérifie rapidement la poignée : impossible de sortir. Kami compte bien nous garder ici jusqu’au vote."

# ============================================================================
# DÉBAT — PHASE 1 : le texte réel (Fatal Assembly)
# ============================================================================

label _3_DEBAT1_PHASE1:

    pause 0.4

    # Remise à zéro de l'adhésion des PNJ (base) avant que les phases 2/3 ne la modifient.
    $ debat_day3_reset_live_stats()
    # Report du résultat de la course : Tomas plus ou moins entamé par Julian.
    $ debat_day3_apply_influence({"tomas": tomas_corridor_delta})

    show screen kami_broadcast_ui

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Avant de débattre, encore faut-il savoir de quoi on parle."
    kami "Alors soyons rigoureux. Voici le texte officiel de l'amendement."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Enfin… « officiel ». [codex_dialogue_link('archive', 'ARCHIVE')] l'a harmonisé avec les Commandements existants."
    kami "Vos petites phrases d'amateurs, seules, ne valent rien en droit. Il a fallu les traduire."

    $ bc_show("nyra", "stress", px=-70, py=-50, pz=0.85)
    nyra "Tu l'as seulement reformulé ? Ou tu as aussi changé ce qu'il disait ?"
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oh, j'ai juste fait en sorte que ça puisse s'appliquer. Chaque détail compte, vous savez."
    kami "Le texte est là. Compilé, dense, juridique. Exactement comme les lois que vous adoriez ignorer avant moi."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "À vous de le remettre en ordre et de le lire. Vraiment le lire."
    kami "Faites attention aux petits mots. Je vous assure que ça compte."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    ryn colere "Pourquoi elle nous sort un pavé pareil ? On voulait juste le commerce !"

    tomas inquiet "Attendez, si elle a ajouté des trucs, on peut se faire avoir. Il faut tout lire, même les petits passages à la fin."

    nyra raison "Attendez, regardez les virgules et les fins de phrase. Ça devrait nous aider à remettre les passages dans le bon ordre."

    noam "Bon, autant s’y mettre. J’aime pas qu’elle nous fasse voter sur un truc qu’on a même pas encore lu."

    # Wrapper complet : intro animée, tutoriel 1ère fois, retry avec malus, résultats avec rang
    call debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY") from _call_debat_phase1_run

    $ phase1_ok = debat_phase1_last_result.get("success", False)
    $ phase1_time_left = debat_phase1_last_result.get("time_left", 0)
    $ phase1_kamyz_gain = debat_phase1_last_result.get("kamyz", 0)
    if phase1_ok:
        $ player_kamyz += phase1_kamyz_gain
        $ renpy.notify("+ %d Kamyz" % phase1_kamyz_gain)
        call screen noam_consent_screen

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    lysa reflexion "Attendez... « Autoriser le transport, la vente et l'échange de marchandises. » Ça, d'accord."
    lysa colere "Mais après, c'est écrit « En conséquence, le système de distribution de denrées est aboli ». Vous avez vu ça ?!"
    elen peur "QUOI ?! Mais j'ai dit que j'étais pour ! Je savais pas que les bons allaient disparaître !"
    ryn colere "C'EST QUOI CETTE CONNERIE ?! Vous allez nourrir les gens de Limen comment ?!"
    tomas peur "Non... non, ça, c'était pas dans la phrase d'hier. Elle peut pas ajouter ça sans rien demander !"
    iris colere "Kami ! T'as ajouté ça exprès, hein ?!"
    mara colere "Voilà pourquoi je vous disais d'attendre le texte avant de promettre quoi que ce soit !"
    nyra stress "Laissez-la répondre, on doit savoir si ce passage est définitif."


    jump _3_DEBAT1_PHASE2

# ============================================================================
# DÉBAT — PHASE 2 : le clash + CLIFFHANGER 1
# ============================================================================

label _3_DEBAT1_PHASE2:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    mara surpris "Ah bah voilà. On demande le commerce et on perd les rations. Génial."

    noam "Attendez. Le texte de départ parlait pas des rations."
    noam "Mais c'est celui-là qu'on doit voter. Alors on fait quoi ?"

    nyra reflechit "Si on vote ce texte, demain il n'y a plus une seule distribution gratuite. Nulle part."

    kael inquiet "Supprimer les rations… ça change tout."

    ryn colere "Ça supprime la seule sécurité qu'on avait ! À Limen, c'est ce qui tient les gens en vie."

    lysa reflechit "Et pourtant, c'est logique."

    noam surpris "Comment ça, logique ? On va retirer à des gens leur seule source de nourriture !"

    lysa blase "Avec le commerce, il faut de l'argent. Pour en avoir, il faut bosser."
    lysa reflechit "Kami a juste décidé de couper les rations pour forcer tout le monde à s'y mettre. Sympa."

    nyra reflechit "Ça reste énorme, comme changement. Et on n'a même pas le temps de s'y préparer."

    sael triste "Les morts de Limen n'ont pas besoin d'un nouveau responsable."
    sael reflechit "Kami. Dis-nous seulement une chose : ce texte vient-il vraiment de l'un de nous ?"

    think "Kami ne répond pas. Ryn répète sa question, puis Tomas commence à protester lui aussi. L’écran reste inchangé."

    lysa blase "Elle ne répondra pas. Dix votes pour douze textes, le tour de passe-passe est parfait."
    lysa colere "Elle peut changer ce qu'elle veut. Et on pourra rien prouver."

    ryn reflechit "Attends… tu dis quoi, là ?"

    lysa salut "Qu'elle nous raconte peut-être n'importe quoi depuis le début. Voilà."

    noam inquiet "Elle nous a peut-être bien eus, oui. Mais j’aimerais surtout savoir ce qui va arriver aux gens si on vote pour."

    # ── Mini-jeu buzzer (Objection Protocol) : influence l'adhésion des PNJ ──
    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On m'informe que l'audience décroche. Trop de blabla, pas assez de sang."
    kami "Je reprends la main. À partir de maintenant, un seul parle à la fois."

    "Les pupitres se transforment. Un micro et un buzzer émergent devant chacun de nous."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous ne parlez que quand votre buzzer passe au vert. Vous voulez contredire ? Vous appuyez."
    kami "On appellera ça un débat. Moi, j'appelle ça du divertissement."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Montrez-moi qui sait viser. C'est parti."

label day3_before_objection_protocol_minigame:
    call debat_phase2_minigame from _call_debat_phase2_minigame

    # ── CLIFFHANGER 1 : Kami rend la conséquence humaine, en direct ──
    stop music fadeout 0.6
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 0.6

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("ryn", "colere", 0.62),
    ])

    ryn colere "Putain, on y passe la journée ! Les gens attendent, eux !"

    think "Ryn a raison sur une chose : on n’a pas beaucoup de temps et on ne sait toujours pas si Kami accepterait de changer une ligne."

    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "« Ils attendent. » Oh, Ryn. Quelle jolie transition."
    kami "Justement. J'ai pensé que vous débattiez un peu trop dans le vide."
    kami "Alors regardez. En direct. Ce n'est pas une rediffusion."

    scene bg_cg003 at adaptive_fullscreen,memory_idle with dissolve
    "Les écrans du Conclave basculent sur un plan de Limen. Une file devant un centre de distribution. Des gens qui poussent. Des cartons vides."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vos districts vous écoutent depuis ce matin. Ils savent qu'aujourd'hui, vous touchez aux rations."
    kami "Alors certains ont commencé à faire des réserves. À se battre pour un carton. Par anticipation."

    $ bc_show("ryn", "inquiet", px=-70, py=-50, pz=0.85)
    ryn "Ce sont… ce sont des gens de chez moi."
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Douze mille trois cent quarante et un."
    kami "C'est le nombre de foyers de Limen sans ration complète à cette heure précise. Le chiffre monte pendant que vous hésitez."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Alors dépêchez-vous de décider. Ils comptent sur vous."
    kami "Enfin… sur l'un de vous. Il en suffit d'un pour tout faire capoter, souvenez-vous."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "triste", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    ryn triste "Elle nous met le couteau sous la gorge avec des vrais visages."

    elen inquiet "Mais… du coup, c'est pire de ne rien faire, non ? Ils souffrent déjà."

    mara colere "Ou alors c'est exactement ce qu'elle veut qu'on pense. Paniquer, voter vite, se planter."

    noam inquiet "Je sais qu’ils ont faim, mais si on supprime les bons maintenant, ils risquent d’avoir encore moins à manger. On peut pas décider juste parce qu’elle nous fait peur."

    jump _3_DEBAT1_PHASE3

# ============================================================================
init -1:
    transform p3_arg_button_idle:
        alpha 0.92
        zoom 1.0
    transform p3_arg_button_hover:
        alpha 1.0
        zoom 1.04
    transform p3_arg_glow:
        alpha 0.35
        linear 0.6 alpha 0.75
        linear 0.6 alpha 0.35
        repeat
    transform p3_arg_float:
        yoffset 0
        linear 1.2 yoffset -6
        linear 1.2 yoffset 0
        repeat


init 4 python:
    DEBATE_ARGUMENT_PHASES = {
        1: ["rationnement", "approvisionnement", "monde_avant", "derogations_complexes", "valeur_travail"],
        2: ["enonce_precis", "orbite", "rationnement", "approvisionnement", "echanges_discrets"],
        3: ["monde_avant", "enonce_precis", "echanges_discrets", "valeur_travail", "derogations_complexes"],
    }
    DEBATE_ARGUMENT_NOAM_LINES = {
        "rationnement": "Les bons ne nourrissent personne quand les rayons sont vides.",
        "approvisionnement": "Les districts ne partent pas avec les mêmes réserves ni les mêmes pénuries.",
        "monde_avant": "Le monde d'avant prouve que la circulation libre peut exister, pas qu'elle est juste.",
        "derogations_complexes": "Si la moindre demande utile exige une dérogation, le système étouffe déjà.",
        "valeur_travail": "Une société tient aussi parce que chacun contribue quand il le peut.",
        "enonce_precis": "Le texte exact compte plus que nos impressions.",
        "orbite": "Sur Orbite, une erreur logistique ne coûte pas seulement cher. Elle tue.",
        "echanges_discrets": "Les échanges existent déjà en cachette. La vraie question, c'est ce qu'on en fait.",
    }
    DEBATE_ARGUMENT_ICONS = {
        "rationnement": "RT",
        "approvisionnement": "ID",
        "orbite": "OR",
        "derogations_complexes": "DG",
        "valeur_travail": "VT",
        "monde_avant": "MA",
        "enonce_precis": "TX",
        "echanges_discrets": "EX",
    }
    DEBATE_ARGUMENT_COLORS = ["#4CB7FF", "#F0BF4A", "#B681FF", "#6BD98A", "#FF6B7C"]

    def debate_argument_is_unlocked(arg_id):
        if "dossier_arg_unlocked" in globals() and dossier_arg_unlocked(arg_id):
            return True
        if arg_id in getattr(store, "j2_vote_arguments", []):
            return True
        data = DAY2_VOTE_ARGUMENTS.get(arg_id, {}) if "DAY2_VOTE_ARGUMENTS" in globals() else {}
        title = data.get("title")
        return bool(title and title in getattr(store, "arguments", []))

    def debate_argument_option(arg_id, phase=1, idx=0):
        data = DAY2_VOTE_ARGUMENTS.get(arg_id, {}) if "DAY2_VOTE_ARGUMENTS" in globals() else {}
        if not data and arg_id in DAY3_VOTE_ARGUMENTS:
            data = DAY3_VOTE_ARGUMENTS[arg_id]
        color = DEBATE_ARGUMENT_COLORS[idx % len(DEBATE_ARGUMENT_COLORS)]
        return {"id": arg_id, "title": data.get("title", arg_id), "desc": data.get("summary", "Argument à découvrir."), "noam": DEBATE_ARGUMENT_NOAM_LINES.get(arg_id, "Je dois choisir l'angle qui aura le plus d'impact."), "icon": DEBATE_ARGUMENT_ICONS.get(arg_id, "--"), "color": color, "unlocked": debate_argument_is_unlocked(arg_id)}

    def debate_argument_options_for_phase(phase):
        return [debate_argument_option(arg_id, phase, i) for i, arg_id in enumerate(DEBATE_ARGUMENT_PHASES.get(phase, []))]

    def debate_argument_unlocked_count():
        ids = []
        for phase_ids in DEBATE_ARGUMENT_PHASES.values():
            for arg_id in phase_ids:
                if arg_id not in ids:
                    ids.append(arg_id)
        return sum(1 for arg_id in ids if debate_argument_is_unlocked(arg_id)), len(ids)

    def debate_argument_fallback_index(options):
        for i, opt in enumerate(options):
            if opt.get("unlocked", False):
                return i
        return None

label day3_choose_debate_argument(phase=1, prompt="Choisissez un argument pour orienter le débat."):
    $ restore_unlocked_arguments()
    $ day3_vote_bootstrap()
    $ day2_sync_argument_titles()
    $ _debate_arg_options = debate_argument_options_for_phase(phase)
    $ _debate_arg_pick = renpy.call_screen("argument_menu_ui", options=_debate_arg_options, phase=phase, prompt=prompt)
    if _debate_arg_pick is None:
        return
    $ selected_argument_id = _debate_arg_options[_debate_arg_pick]["id"]
    $ selected_argument_noam_line = _debate_arg_options[_debate_arg_pick]["noam"]
    noam "[selected_argument_noam_line]"
    return

screen argument_menu_ui(options, prompt="Choisissez un argument pour orienter le débat.", phase=1):
    modal True
    zorder 250
    default selected_idx = debate_argument_fallback_index(options)

    add Solid("#02070CEE")
    add "bg_conclave" at adaptive_fullscreen:
        alpha 0.16

    $ unlocked_count, total_count = debate_argument_unlocked_count()

    fixed:
        xfill True
        yfill True
        hbox:
            xpos 56
            ypos 42
            spacing 22
            text "//" size 42 color "#D7E1EA" font "fonts/Rajdhani-SemiBold.ttf"
            vbox:
                spacing 2
                text "CHOIX DU THÈME" size 34 color "#EAF3FA" font "fonts/Rajdhani-SemiBold.ttf"
                text "PHASE ARGUMENTATIVE" size 18 color "#4CB7FF" font "fonts/Rajdhani-SemiBold.ttf"
        hbox:
            xpos 1365
            ypos 50
            spacing 14
            text "PHASE [phase]/3" size 21 color "#8A94A0" font "fonts/Rajdhani-SemiBold.ttf"
            for pi in range(1, 4):
                add Solid("#4CB7FF" if pi <= phase else "#27313A", xsize=22, ysize=22)
        frame:
            xpos 46 ypos 132 xsize 1828 ysize 280
            background Solid("#071018E8")
            padding (0, 0)
            fixed:
                add Solid("#6F849A66", xsize=1828, ysize=1)
                frame:
                    xpos 0 ypos 0 xsize 450 ysize 280
                    background Solid("#0B1824E8")
                    padding (0, 0)
                    add "gui/day3/vote_phase2/portraits/noam_idle.png":
                        xysize (450, 450)
                        yalign 0.28
                        alpha 0.72
                vbox:
                    xpos 530 ypos 70 spacing 18
                    text "NOAM" size 30 color "#4CB7FF" font "fonts/Rajdhani-SemiBold.ttf"
                    text "Quel angle aborder pour cette discussion ?\nJe dois choisir l'argument qui aura le plus d'impact." size 29 color "#F0F4F7" font "fonts/Barlow-Light.ttf" line_spacing 8
        vbox:
            xpos 0 ypos 460 xsize 1920 spacing 10
            text "SÉLECTIONNEZ LE THÈME DE LA DISCUSSION" xalign 0.5 size 31 color "#EAF3FA" font "fonts/Rajdhani-SemiBold.ttf"
            text kd_tr(prompt) xalign 0.5 size 22 color "#AEB8C2" font "fonts/Barlow-Light.ttf"
        hbox:
            xpos 44 ypos 548 spacing 22
            for i, opt in enumerate(options):
                $ unlocked = opt.get("unlocked", False)
                $ selected = (selected_idx == i)
                $ col = opt.get("color", "#4CB7FF")
                $ card_bg = (col + "33") if selected and unlocked else ("#07131DDD" if unlocked else "#050A0FCC")
                button:
                    xsize 282 ysize 382 padding (18, 14)
                    background Solid(card_bg)
                    hover_background Solid((col + "44") if unlocked else "#050A0FCC")
                    sensitive unlocked
                    action SetScreenVariable("selected_idx", i)
                    vbox:
                        xfill True spacing 10
                        text "[i + 1]" size 22 color (col if unlocked else "#59636B") font "fonts/Rajdhani-SemiBold.ttf"
                        text opt.get("icon", "--") xalign 0.5 size 48 color (col if unlocked else "#666666") font "fonts/Rajdhani-SemiBold.ttf"
                        text kd_tr(opt.get("title", "ARGUMENT")) xalign 0.5 text_align 0.5 size 22 color (col if unlocked else "#6F747A") font "fonts/Rajdhani-SemiBold.ttf" xmaximum 238
                        text kd_tr(opt.get("desc", "")) xalign 0.5 text_align 0.5 size 16 color ("#D6DDE4" if unlocked else "#555D65") font "fonts/Barlow-Light.ttf" xmaximum 238 line_spacing -1
                        null height 2
                        text ("DISPONIBLE" if unlocked else "VERROUILLÉ") xalign 0.5 size 15 color (col if unlocked else "#5F666D") font "fonts/Rajdhani-SemiBold.ttf"
                        if not unlocked:
                            text "Débloquez cet argument pour l'utiliser." xalign 0.5 text_align 0.5 size 14 color "#555D65" font "fonts/Barlow-Light.ttf" xmaximum 238
        frame:
            xpos 50 ypos 950 xsize 770 ysize 62 background Solid("#071018DD") padding (22, 10)
            hbox:
                spacing 22
                text "//" size 28 color "#8AB9E8" font "fonts/Rajdhani-SemiBold.ttf"
                vbox:
                    spacing 2
                    text "VOS ARGUMENTS DÉBLOQUÉS" size 18 color "#4CB7FF" font "fonts/Rajdhani-SemiBold.ttf"
                    text "[unlocked_count] / [total_count]" size 25 color "#EAF3FA" font "fonts/Rajdhani-SemiBold.ttf"
        frame:
            xpos 900 ypos 950 xsize 770 ysize 62 background Solid("#071018DD") padding (22, 13)
            text "INFO  Chaque thème influence les réactions des représentants. Choisissez judicieusement." size 18 color "#B8C2CC" font "fonts/Barlow-Light.ttf" xmaximum 720
        textbutton "CONFIRMER LE THÈME":
            xpos 470 ypos 1022 xsize 980 ysize 52
            text_size 24
            text_color "#EAF3FA"
            text_font "fonts/Rajdhani-SemiBold.ttf"
            background Solid("#102A46EE")
            hover_background Solid("#174D7CEE")
            sensitive selected_idx is not None
            action Return(selected_idx)
        if selected_idx is None:
            textbutton "CONTINUER SANS THÈME":
                xpos 470 ypos 1022 xsize 980 ysize 52
                text_size 22
                text_color "#7D8994"
                background Solid("#111820EE")
                hover_background Solid("#1A2530EE")
                action Return(None)

label _3_DEBAT1_PHASE3:

    # Réinjecte les arguments débloqués globalement avant d'afficher les choix.
    $ restore_unlocked_arguments()
    $ day2_sync_argument_titles()

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.0
    show screen kami_broadcast_ui

    python:
        store.p3_round_options = [
            [
                debate_argument_option("rationnement", 1, 0),
                debate_argument_option("approvisionnement", 1, 1),
                debate_argument_option("orbite", 1, 2),
                debate_argument_option("valeur_travail", 1, 3),
                debate_argument_option("derogations_complexes", 1, 4),
            ],
            [
                debate_argument_option("monde_avant", 3, 0),
                debate_argument_option("enonce_precis", 3, 1),
                debate_argument_option("echanges_discrets", 3, 2),
                debate_argument_option("rationnement", 3, 3),
                debate_argument_option("approvisionnement", 3, 4),
            ],
        ]

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 0.6

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    noam inquiet "Bon, je crois qu’on a tous compris ce qu’elle a ajouté. Mais qu’est-ce qu’on fait, maintenant ? Moi, j’ai pas envie de décider ça à la va-vite."

    julian colere "À la va-vite ? Noam, ça fait un an que les gens manquent de tout ! Tu veux encore attendre combien de temps ?"

    ryn colere "Et ton grand soir, c'est quoi ? On sacrifie Limen pour que Nexus se paie du luxe ?"

    julian surpris "Nexus ? Je te rappelle que j'en viens, de Nexus. Et je ne roule pas sur l'or, figure-toi."

    ryn "…Ouais. Bref. Ça change rien au fond !"

    mara taquin "Ryn, tu vas te fatiguer avant de voter si tu continues à gueuler comme ça."

    elen joie "Imaginez : tu peux acheter ce que tu veux sans remplir trois formulaires !"

    # (combinaison « lysa raison » ajoutée dans images.rpy)
    lysa raison "Encore faut-il avoir de l'argent, Elen. Sinon tu regardes juste les vitrines."

    tomas hesitation "Moi, je sais juste qu’on fabrique beaucoup moins de choses qu’avant. J’ai vu les chiffres, c’est presque quatre fois moins. Ça fait peur quand même."

    nyra reflechit "C’est pas tellement surprenant. Quand on ne gagne rien de plus en travaillant davantage, tout le monde finit par se contenter du minimum."

    # Cadrage de Kami : moins clownesque, plus prédatrice.
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "Ah ! Voilà une discussion qui devient intéressante !"
    kami "Je vous rappelle que ce texte est né de VOTRE imagination. Ne me regardez pas comme la coupable."
    kami "Continuez. Vous êtes bien plus intéressants quand vous avez peur."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], phase=3, prompt="Premier échange — Quel argument présenter ?")
    if p3_pick is not None and p3_round_options[0][p3_pick]["unlocked"]:
        $ p3_argument_one = p3_round_options[0][p3_pick]["id"]
        call _3_DEBAT1_PHASE3_INT1 from _call__3_DEBAT1_PHASE3_INT1
    else:
        $ p3_argument_one = None
        think "Je n'ai rien de suffisamment solide à ajouter pour le moment."

    scene bg_conclave at adaptive_fullscreen with dissolve

    elias "Je comprends qu’on hésite, mais le système actuel, il marche pas non plus. À la Forge, on passe plus de temps à demander des pièces qu’à réparer !"

    sael "Chez nous, on s'aide déjà sans bons."
    sael determine "Je comprends votre peur. Mais je ne crois pas qu'attendre Kami pour chaque chose nous aide davantage."

    lysa blase "Même en votant pour, il reste un trou béant dans le texte."
    lysa reflechit "Avec quoi les gens gagnent leur premier argent ? Si personne n'a rien, personne ne peut rien acheter à personne."

    noam inquiet "Et ils vont sortir d’où, les premiers salaires ? Kami, t’as prévu quelque chose ou tu nous laisses deviner ?"

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh. Une question pratique ? On progresse."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Si ce texte passe, j'ouvrirai des contrats de travail rémunérés. Des tâches assignées, des objectifs, un salaire à la clé."
    kami "Vous fabriquez, vous récoltez, vous livrez. Vous êtes payés. Simple."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Libre à vous de travailler. Ou pas. Mais ne comptez plus sur la générosité des rations."
    kami "Et pour ceux qui ne voudront pas travailler... Eh bien, il faudra se débrouiller sans rations. Motivant, non ?"

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])

    elen inquiet "Attendez, il faut travailler pour avoir à manger, maintenant ? Mais ceux qui sont malades, ils font comment ?"
    ryn colere "Et les vieux ? Et les gens qui peuvent pas bosser ? Tu vas les laisser crever ?!"
    sael determine "Chez moi, on s'occupe de ceux qui ne peuvent pas travailler. Tout le monde ne peut pas produire autant."
    mara colere "Donc elle supprime les rations et elle décide elle-même qui a le droit de gagner de l'argent. Vous voyez le problème ou pas ?!"
    julian reflexion "Au moins, les gens pourront retravailler et recevoir quelque chose en échange. On peut pas rester bloqués avec les anciens bons."
    lysa blase "Et si les contrats sont tous proposés à Nexus ? Les autres vont faire quoi, marcher pendant trois jours pour aller bosser ?"
    elias reflechit "Pour réparer une machine, moi, j'aurais du boulot. Mais les gens qui ont pas de métier comme ça... j'en sais rien."
    tomas inquiet "Et les premiers salaires, ils seront versés quand ? Le jour même ? Dans une semaine ? Faut bien manger entre-temps !"
    nyra raison "Kami, tu peux au moins préciser quand les contrats commencent et comment les districts seront approvisionnés ?"
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Les contrats seront disponibles dès l'entrée en vigueur du texte. Pour le reste, je vous laisse organiser votre merveilleuse nouvelle économie !"
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("kael", "calme", -0.11),
        ("iris", "fatigue", 0.02),
        ("sael", "determine", 0.15),
        ("elen", "inquiet", 0.28),
        ("julian", "sourire", 0.41),
        ("mara", "neutre", 0.54),
        ("ryn", "reflechit", 0.67),
        ("nyra", "triste", 0.80),
        ("tomas", "hesitation", 0.93),
        ("lysa", "reflexion", 1.06),
        ("elias", "reflechit", 1.19),
    ])
    iris colere "Ah bah super ! Elle nous donne les contrats, mais on doit se débrouiller pour le reste !"
    kael inquiet "Sur Orbite, si les livraisons ne suivent pas, des gens peuvent mourir très vite. Ce n'est pas une question de confort."
    noam inquiet "Je voulais qu'on puisse acheter ce qui nous manque, pas qu'on retire à tout le monde le droit de manger. Et là, on doit se décider sans même savoir comment ça va fonctionner."
    sael neutre "Il faudra choisir malgré ça. Mais ce n'est pas une raison pour faire semblant que tout ira bien."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], phase=3, prompt="Dernier échange — Quel argument présenter ?")
    if p3_pick is not None and p3_round_options[1][p3_pick]["unlocked"]:
        $ p3_argument_two = p3_round_options[1][p3_pick]["id"]
        call _3_DEBAT1_PHASE3_INT2 from _call__3_DEBAT1_PHASE3_INT2
    else:
        $ p3_argument_two = None
        think "Je préfère me taire plutôt que parler pour ne rien dire."

    scene bg_conclave at adaptive_fullscreen with dissolve
    pause 0.3

    noam inquiet "Bon... On peut encore en parler pendant des heures, mais je crois que personne n’aura toutes les réponses aujourd’hui."
    nyra neutre "Oui. On sait au moins ce qu’on risque de perdre, et ce qu’on pourrait gagner. À chacun de voir."

    # ── CLIFFHANGER 2 : le dernier indécis, avant le vote ──
    think "Je regarde Kael. Il a encore l’air de chercher ce qu’il va faire, et je ne crois pas que je serais capable de le convaincre avec une phrase de plus."

    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "reflechit", 0.32),
        ("kael", "inquiet", 0.68),
    ])

    noam "Ryn, Kael... Vous en pensez quoi, maintenant ?"

    ryn triste "…Moi, je sais. Que je le veuille ou non. Limen, c'est écrit là. Alors je porterai mon choix."

    think "Reste Kael. Celui qui déciderait « au moment de voter ». Le moment, c'est maintenant."

    kael inquiet "Je…"

    kael triste "Sur Orbite, une erreur ne pardonne pas. Et là, je n'arrive pas à voir si on ouvre une porte…"
    kael peur "…ou si on retire le dernier filet sous nos pieds."

    noam inquiet "Kael, t’as toujours pas décidé ? On peut encore attendre une minute si t’as besoin."

    think "Il ouvre la bouche."

    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "STOP !"
    kami "Non, non, non. Ne me gâchez pas le suspense en le disant tout haut."
    kami "L'audimat est à son sommet. Un cœur qui hésite en direct, ça n'a pas de prix."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Vous garderez vos réponses pour le bulletin. C'est plus honnête. Et tellement plus cruel."
    kami "Rappel des règles : il suffit d'un « contre ». Un seul. Et tout s'effondre."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Alors… on vote. Maintenant. POUR, ou CONTRE."
    kami "Je meurs d'envie de compter."

    jump vote_phase3_final

# ============================================================================
# PHASE 3 — Interventions selon l'argument choisi (influence l'adhésion PNJ)
# ============================================================================

label _3_DEBAT1_PHASE3_INT1:
    $ selected = p3_argument_one

    scene bg_conclave at adaptive_fullscreen with dissolve

    if selected == "approvisionnement":

        # Tous les locuteurs de la branche sont dans le showGroup (aucun sprite parasite).
        $ showGroup([
            ("elias", "determine", 0.02),
            ("julian", "sourire", 0.18),
            ("mara", "doute", 0.34),
            ("ryn", "colere", 0.50),
            ("kael", "reflechit", 0.66),
            ("sael", "neutre", 0.82),
            ("elen", "joie", 0.98),
        ])

        noam inquiet "Ryn, t’as dit hier que chez toi, même avec des bons, vous repartez parfois sans rien. C’est toujours comme ça ?"

        elias determine "Ça, c'est la vérité vraie. Un bon pour du riz, et pas de riz au bout. On appelle ça la sécurité ?"

        julian sourire "Si les producteurs peuvent vendre, ils auront une bonne raison d'en faire plus."

        mara doute "Ouais, et tout partira là où y a de l'argent. À Limen, ils auront quoi ?"

        ryn colere "Voilà ! Nexus déborde, nous on ramasse les miettes. Comme aujourd'hui, mais en pire."

        kael reflechit "Limen a beaucoup d'habitants. Des vendeurs voudront sûrement y aller aussi."

        ryn reflechit "…Mouais. Peut-être. Si on a de quoi payer, déjà."

        sael neutre "Chez moi, on fait avec ce qu'on a. Mais c'est pas toujours simple."

        elen joie "Et si on pouvait enfin avoir ce qui nous manque ? Ça serait bien, non ?"

        # Montre que le système actuel ne nourrit pas : pousse doucement les hésitants.
        $ debat_day3_apply_influence({"ryn": 1, "kael": 1, "mara": -1, "julian": 1, "elen": 1})

    elif selected == "rationnement":

        $ showGroup([
            ("tomas", "raison", 0.05),
            ("iris", "colere", 0.23),
            ("ryn", "colere", 0.41),
            ("mara", "reflexion", 0.59),
            ("elias", "determine", 0.77),
            ("elen", "joie", 0.95),
        ])

        noam inquiet "Vous trouvez pas ça dingue qu’on ait des bons de rationnement et qu’on manque quand même de nourriture ?"

        tomas raison "J'ai vu les chiffres. Dans certains endroits, plus de la moitié des produits manquent presque tout le temps."

        iris colere "Un bon, c'est un ticket pour faire la queue. Point. Le produit correct part en deux jours."

        ryn colere "À Limen, on a des bons pour du lait qui arrive caillé. Des médocs périmés avant même la livraison."
        ryn triste "Ça, c'est votre « sécurité » ? Un papier qui promet ce qui n'arrive jamais ?"

        mara reflexion "Ouais, ça marche pas bien. Mais le supprimer d'un coup, c'est pas mieux."

        elias determine "Le même ticket pour rien, qu'on se crève au boulot ou qu'on dorme toute la journée. Faut que ça change."

        elen joie "Moi, j'aimerais juste qu'on arrête de se battre pour trois bricoles."

        # L'argument le plus efficace pour rallier les pauvres (Ryn) : preuve vécue.
        $ debat_day3_apply_influence({"ryn": 2, "mara": 1, "kael": 1, "tomas": 1, "iris": 1})

    elif selected == "orbite":

        $ showGroup([
            ("nyra", "raison", 0.02),
            ("kael", "mefiant", 0.18),
            ("iris", "inquiet", 0.34),
            ("tomas", "raison", 0.50),
            ("julian", "hesitation", 0.66),
            ("lysa", "blase", 0.82),
            ("mara", "stress", 0.98),
        ])

        nyra raison "Vous parlez de Limen. Mais que savez-vous du prix d'une erreur sur Orbite ?"

        kael mefiant "Chez nous, un retard de livraison, ça peut vite devenir dangereux. On a pas le droit de se planter."
        kael triste "On ne peut pas se permettre l'imprévu. Jamais."

        noam "Et avec le commerce, les livraisons peuvent changer tout le temps."

        iris inquiet "…Ok. Là, même moi je tique. On met des vies en balance contre des étals mieux garnis ?"

        tomas raison "Sur Orbite, il y a pourtant peu de morts. Les règles actuelles ont aussi cet avantage."

        julian hesitation "On n’interdit rien de plus... enfin, je vois le risque. Mais on peut pas renoncer à chaque fois parce qu’on a peur."

        lysa blase "Il suffit qu'une livraison merde et ils ont un gros problème. On a compris."

        nyra stress "Sur Orbite, la perte de contrôle se paie dans la seconde. Pas au prochain vote."

        mara stress "…Super. Donc en votant pour, on joue avec la vie de gens qu'on ne verra jamais."

        think "Nyra et Kael échangent un regard bref, tendu. Personne n'insiste."

        # Argument « danger » : refroidit fortement les hésitants (surtout Kael).
        $ debat_day3_apply_influence({"kael": -2, "nyra": -1, "mara": -1, "ryn": -1, "julian": -1, "lysa": -1})

    elif selected == "valeur_travail":
        $ showGroup([
            ("sael", "neutre", 0.12),
            ("elias", "reflechit", 0.33),
            ("mara", "doute", 0.55),
            ("ryn", "reflechit", 0.77),
        ])
        noam "Sael, chez toi, tout le monde aide les autres, c'est ça ?"
        sael neutre "Oui. Quand quelqu'un ne peut pas travailler, on l'aide. Sinon, chacun fait sa part."
        elias reflechit "Ça, ça me parle. Mais avec les nouveaux contrats, ceux qui peuvent pas bosser, ils font quoi ?"
        mara doute "Voilà. C'est exactement ce qui me gêne."
        noam inquiet "C’est ça qui m’embête. Si on dit oui, on fait quoi des gens qui peuvent pas travailler ?"
        ryn reflechit "Au moins, tu poses la bonne question."
        $ debat_day3_apply_influence({"sael": 1, "elias": 1, "mara": -1, "ryn": 1})

    elif selected == "derogations_complexes":
        $ showGroup([
            ("elen", "reflechit", 0.16),
            ("iris", "blase", 0.38),
            ("kael", "calme", 0.60),
            ("nyra", "raison", 0.82),
        ])
        noam sourire "Elen a passé un temps fou sur des formulaires juste pour commander des fraises. Vous trouvez pas qu’on va un peu loin ?"
        elen reflechit "Trois pages ! Pour des épices ! J'ai cru devenir folle."
        iris blase "Et pour une pièce de rechange, c'est la même galère."
        kael calme "Oui. Certains dossiers mettent des jours à être validés."
        nyra raison "Donc le système bloque même les demandes les plus simples. On peut au moins être d'accord là-dessus."
        noam inquiet "Voilà pourquoi j’ai envie que ça change. Mais franchement, je sais toujours pas si ce texte va arranger les choses."
        $ debat_day3_apply_influence({"elen": 1, "iris": 1, "kael": 1, "nyra": 1})

    return

label _3_DEBAT1_PHASE3_INT2:
    $ selected = p3_argument_two

    scene bg_conclave at adaptive_fullscreen with dissolve

    if selected == "monde_avant":

        $ showGroup([
            ("iris", "reflechit", 0.05),
            ("elen", "joie", 0.23),
            ("julian", "sourire", 0.41),
            ("mara", "reflexion", 0.59),
            ("tomas", "raison", 0.77),
            ("ryn", "colere", 0.95),
        ])

        iris reflechit "Avant, tout coûtait cher. Vous avez oublié les prix qui grimpaient sans arrêt ?"
        iris reflechit "Mais quand un truc manquait, on pouvait au moins chercher ailleurs."

        elen joie "Voilà ! Tu bossais, tu achetais. Personne pour juger si tes chaussures étaient assez trouées."

        julian sourire "C'était pas parfait, mais on pouvait essayer autre chose. Aujourd'hui, on attend que Kami décide."

        mara reflexion "« Choisir »… c'est un joli mot, Elen."
        mara reflexion "Moi, je me souviens surtout des sourires obligatoires. Des portes qui se ferment si tu n'es pas… parfaite."
        mara triste "La liberté d'avant, certains l'ont payée très cher. J'en fais partie."

        tomas raison "Les guerres faisaient beaucoup de dégâts aussi. Avec Kami, ce risque-là est plus faible. Enfin... en théorie."

        ryn colere "« Techniquement ». Dis ça aux gamins de Limen qui bouffaient les restes des riches."

        noam "Ouais. Enfin, avant, les gens qui avaient pas d'argent galéraient aussi."

        elen joie "Alors gardons le meilleur ! L'essentiel pour tous, la liberté pour le reste. Comme avant, mais sans la guerre !"

        think "Mara détourne le regard et ne répond plus. Je crois qu’elle n’avait pas envie de parler de ça devant tout le monde."

        # Galvanise les convaincus, mais réveille les blessures de Mara et l'amertume de Ryn.
        $ debat_day3_apply_influence({"julian": 1, "elen": 1, "iris": 1, "mara": -1, "ryn": -1})

    elif selected == "enonce_precis":

        $ showGroup([
            ("ryn", "colere", 0.05),
            ("elias", "determine", 0.23),
            ("kael", "triste", 0.41),
            ("lysa", "blase", 0.59),
            ("mara", "stress", 0.77),
            ("sael", "determine", 0.95),
        ])

        ryn colere "Lisez le texte, bon sang ! « Suppression des bons. Fin de la distribution. » Point."
        ryn colere "Pas de « minimum vital ». Pas de « transition ». Rien."

        elias determine "C'est ça qui libère ! Plus de bons, plus de laisse. On produit, on échange, on vit."

        noam inquiet "On peut pas garder les bons juste quelques semaines de plus. Soit on les supprime d’un coup, soit on refuse tout. C’est ça qui me fait peur."

        kael triste "Sur Orbite, si on arrête les livraisons avant de savoir les remplacer, on risque d’avoir des morts. On peut pas faire ça du jour au lendemain."

        lysa blase "Y a écrit « supprimer ». Pas « réduire ». C'est quand même pas compliqué."

        ryn colere "Sans bons, à Limen, on meurt en silence pendant que vous « produisez » vos rêves."
        ryn colere "Et ceux qui peuvent pas bosser, ils crèvent ? C'est ça, le plan ?!"

        mara stress "…Et il l'écrit noir sur blanc. On ne pourra pas dire qu'on ne savait pas."

        sael determine "Les gens échangent déjà des choses là-bas. On le sait tous."

        think "Ryn frappe du poing. Sael ne cille pas."

        # Brutalité du texte : durcit les hésitants (Ryn surtout), galvanise Sael et Elias.
        $ debat_day3_apply_influence({"ryn": -2, "kael": -1, "mara": -1, "elias": 1, "sael": 2})

    elif selected == "echanges_discrets":

        $ showGroup([
            ("ryn", "surpris", 0.05),
            ("sael", "reflechit", 0.23),
            ("kael", "doute", 0.41),
            ("julian", "sourire", 0.59),
            ("lysa", "blase", 0.77),
            ("mara", "reflexion", 0.95),
        ])

        ryn surpris "Attends… tu dis que ça se fait déjà ? Des trocs en douce, à Limen ?"

        sael reflechit "Depuis toujours. Un sac contre une réparation. Un service contre du tissu. Ça tient les gens debout entre deux rations."

        noam "Ça marche entre voisins. Mais dans tous les districts ? J'en suis moins sûr."

        kael doute "Si ça existe déjà, on pourrait peut-être trouver un moyen de le faire chez nous aussi."

        julian sourire "Exactement ! Les gens s'organisent déjà. Supprimer les bons, c'est cesser de nier ce qu'ils font en cachette."

        lysa blase "Et y aura toujours des types pour prendre leur part au passage."

        ryn reflechit "…Mais si c'est déjà là, et que ça sauve des familles… alors on pourrait faire pareil. En mieux. Sans crever en attendant Kami."

        mara reflexion "Tiens. Pour une fois, un plan qui ne sort pas de nulle part. Ça existe, ça marche. C'est déjà ça."

        sael determine "On survit déjà. On peut faire plus que survivre."

        think "Ryn baisse les yeux. Kael pose quelques questions à Sael sur la façon dont ils organisent les échanges chez elle."

        # Rassure les hésitants avec une preuve concrète : le levier de l'unanimité.
        $ debat_day3_apply_influence({"ryn": 2, "kael": 2, "mara": 1, "sael": 1, "julian": 1})

    elif selected == "rationnement":
        $ showGroup([
            ("ryn", "colere", 0.12),
            ("mara", "doute", 0.34),
            ("iris", "blase", 0.56),
            ("tomas", "hesitation", 0.78),
        ])
        noam "On parle de supprimer les bons. Mais dans certains districts, ils ne suffisent déjà pas à nourrir tout le monde."
        ryn colere "À Limen, tu peux attendre toute la journée et repartir les mains vides."
        iris blase "Donc on garde un système qui marche mal, ou on le supprime d'un coup. Super choix."
        tomas hesitation "O-On devrait au moins prévoir une période de transition..."
        mara doute "Sauf qu'on peut pas rajouter une ligne au texte. C'est bien le problème."
        noam inquiet "Donc même si ça passe, on n’aura pas réglé tous les problèmes. Loin de là."
        $ debat_day3_apply_influence({"ryn": -1, "mara": -1, "tomas": -1, "iris": 1})

    elif selected == "approvisionnement":
        $ showGroup([
            ("lysa", "blase", 0.12),
            ("nyra", "raison", 0.34),
            ("kael", "inquiet", 0.56),
            ("elen", "inquiet", 0.78),
        ])
        noam "Même aujourd'hui, tous les districts ne reçoivent pas la même chose."
        lysa blase "Et demain, ceux qui ont déjà de quoi payer seront servis les premiers. Quelle surprise."
        nyra raison "Pas forcément. S'il y a plus de marchandises en circulation, certains endroits pourraient aussi y gagner."
        kael inquiet "Il faudra surtout que les livraisons arrivent à temps."
        elen inquiet "Donc on sait pas si ce sera mieux. C'est ça ?"
        noam "C'est ça. Et on va devoir décider quand même."
        $ debat_day3_apply_influence({"lysa": -1, "kael": -1, "nyra": 1, "elen": 1})

    return

# ============================================================================
# ISSUES DU VOTE
# ============================================================================

label _3_VOTE_POUR:

    $ current_period = "Soir"
    
    scene bg_conclave at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    play music "music/bgm_victory_bitter.mp3" fadein 2.0

    pause 1.2

    $ interject("ADOPTÉ", color="#5DFF9A")

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "VERT."
    kami "Le vote est POUR. À l'unanimité. Pas un seul « contre ». Je suis presque émue."
    kami "Suppression totale des bons de rationnement. Fin de la distribution gratuite."
    kami "Le commerce, le transport et le stockage de marchandises sont désormais autorisés."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Félicitations, mes petits rebelles. Vous avez coupé la laisse."
    kami "Mais la laisse, c'était aussi ce qui vous retenait de tomber."
    kami "On va voir ce que ça donne sans filet. J'ai hâte du spectacle."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    think "Dès que l’écran s’éteint, Elen pousse un cri de joie et Julian se lève d’un bond. D’autres restent assis, visiblement moins rassurés par le résultat."

    $ showGroup([
        ("julian", "sourire", 0.15),
        ("ryn", "jaloux", 0.38),
        ("elen", "joie", 0.61),
        ("mara", "rire_profond", 0.84),
    ])

    julian joie "ON A RÉUSSI ! Je vous l’avais dit ! C’est le premier texte qu’on arrive à faire passer !"
    elen joie "Ouiiii ! On a réussi à se mettre d’accord ! Enfin... je crois !"
    mara taquin "Doucement, vous deux. On vient aussi de supprimer les rations de tout le monde."

    ryn jaloux "Ouais."
    ryn inquiet "Mais sans les bons, Limen va morfler au début. Faut pas se mentir."

    noam sourire "Je suis content qu’on ait réussi quelque chose ensemble. J’espère juste qu’on n’a pas fait une énorme bêtise."

    mara rire_profond "Génial. On va enfin pouvoir acheter des trucs."
    mara taquin "Et crever avec le choix de la sauce. Le luxe."

    $ showGroup([
        ("elen", "joie", 0.30),
        ("kael", "mefiant", 0.70),
    ])

    kael mefiant "Orbite tiendra. Si les protocoles de sécurité restent intacts."
    kael triste "Si."

    think "Julian essaie de sourire, mais Elen paraît surtout soulagée. Ryn garde les yeux baissés, tandis que Kael parle tout bas avec Nyra."
    think "Certains sont heureux, d’autres ont peur. Pour ma part, je suis soulagé qu’on ait réussi à voter ensemble, même si je ne sais pas encore ce que ça donnera."

    $ hideGroup()

    think "Il est dix-sept heures dix quand on quitte la salle. Julian continue de parler du résultat, tandis que Ryn refuse de participer aux félicitations."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_184
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent jusqu'à ma chambre."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_185
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "On a réussi à faire passer un amendement. Il y a deux jours, je n’aurais pas cru que c’était possible."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_186
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit. Demain sera différent. Pas forcément meilleur."

    $ phase3_over = True
    $ vote1 = "OUI"
    $ kami_grant_chapter_1_ending_reward("vote_oui")

    call show_chapter_title("Fin du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title

    pause 3.0

    # La suite du vote adopte n'est pas encore developpee.
    # Conserver la scene et le succes de ce vote, puis annoncer explicitement
    # le retour a la chronologie jouable (vote refuse) pour eviter un cul-de-sac.
    call screen kd_route_vote_convergence
    $ vote1 = "NON"
    call end_day("4", sleeping=True) from _call_end_day_3

    jump _4_0_REVEIL_CHAMBRE

label _3_VOTE_CONTRE:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_187
    scene bg_conclave at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    play music "music/bgm_system_override.mp3" fadein 2.0

    pause 1.2

    $ interject("REJETÉ", color="#FF4D6D")

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "ROUGE."
    kami "Le vote est CONTRE. Il a suffi d'une voix. Une seule."
    kami "Le statu quo est maintenu. Les bons de rationnement restent. La distribution continue."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Alors, que je n'entende plus personne pleurer sur ces bons."
    kami "Vous aviez la possibilité de tout changer. Quelqu'un, à cette table, a dit non."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Félicitations, mes petits rats sages. Vous avez choisi la sécurité."
    kami "C'est plus ennuyeux. J'espérais un peu plus de sang. Ce sera pour une autre fois."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    play music "music/bgm_world_decline.mp3" fadein 2.0
    think "L’écran s’éteint et personne ne réagit pendant quelques secondes. Puis Julian repousse sa chaise d’un coup."

    $ showGroup([
        ("julian", "colere", 0.02),
        ("ryn", "fatigue", 0.26),
        ("mara", "colere", 0.50),
        ("elen", "triste", 0.74),
        ("kael", "doute", 0.90),
        ("nyra", "raison", 1.14),
    ])

    julian colere "Non. On avait une chance réelle. Une vraie."

    ryn fatigue "C'est pas si simple. D'autres auraient pu en crever."

    mara colere "On a juste repoussé l'inévitable. On va continuer à mourir à petit feu. Su-per."

    elen triste "Je… je croyais qu'on allait y arriver."
    elen triste "J'étais tellement sûre…"

    kael doute "Au moins, on connaît déjà ce quotidien. Ça ne s'aggrave pas. C'est déjà ça."

    nyra raison "Attendez, on sait même pas qui a voté contre, et on ne sait pas pourquoi. On va pas commencer à s’accuser les uns les autres."

    think "Julian frappe brusquement la table. Elen sursaute et Tomas lui demande de se calmer, mais il ne l’écoute pas."

    julian colere "Rationnel ?! Vous appelez ça rationnel ?"
    julian colere "Continuer à rationner des miettes pendant que les districts crèvent ? On a laissé filer la seule ouverture !"

    ryn colere "C'est le vote. C'est comme ça."
    ryn colere "Je le comprends. T'as vu ce que ça risquait pour Limen ?"

    julian colere "Et t'as vu ce que ça risque si on change rien ?!"

    ryn colere "Assieds-toi !"
    mara colere "Les riches survivront encore. Quelle surprise."
    noam colere "Julian, arrête ! Crier sur Ryn va pas faire changer le résultat !"
    nyra neutre "On va pas refaire le débat maintenant. Ceux qui veulent discuter peuvent le faire demain, quand on sera calmés."

    think "Il est presque dix-sept heures. Le texte a été rejeté, et je ne sais même pas comment on va réussir à s’asseoir tous ensemble au prochain vote."
    think "Maintenant, certains vont chercher qui a voté contre, même si le scrutin est secret. Je n’aime pas du tout la façon dont Julian regarde les autres."

    think "Je me lève. Les voix continuent sans moi. Je veux juste rentrer et arrêter de réfléchir."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_189
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent dans les couloirs froids."
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_190
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Je traverse le dortoir sans m’arrêter."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_191
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je m’effondre sur mon lit sans même prendre le temps de me changer."
    think "J’entends encore Julian s’énerver. On avait une chance d’adopter ce texte, et maintenant je me demande comment on va réussir à travailler ensemble au prochain vote."
    think "Qu'est-ce qu'on peut faire, maintenant ?"

    $ phase3_over = True
    $ vote1 = "NON"
    $ kami_grant_chapter_1_ending_reward("vote_non")

    call show_chapter_title("Fin du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title_1

    pause 3.0

    call end_day("4", sleeping=True) from _call_end_day_24

    jump _4_0_REVEIL_CHAMBRE

# Total jour 3 : 17m
# Total J0-J3 : 1h25
