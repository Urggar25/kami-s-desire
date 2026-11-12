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
# Empêche de créditer plusieurs fois la récompense de la réfutation de Julian.
default day3_julian_clash_rewarded = False
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
    think "Il reste assez de temps pour respirer. Pas assez pour décider quoi que ce soit."
    think "Je me laisse tomber sur le lit. Deux minutes les yeux fermés, et je repars."

    play sound sfx_knock
    think "Trois coups frappés à la porte. Fort. Visiblement, la tranquillité n'a pas voté pour moi."
    pause 0.2
    play sound sfx_knock
    pause 0.2

    nyra "Noam ! Ouvre. Vite."

    think "Ce n'est pas une visite de courtoisie. Je me redresse d'un bond."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_162
    scene bg_dortoir at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("nyra", "neutre", 0.60),
    ])

    nyra stress "Noam, viens. Julian a coincé Tomas dans la salle de repos. Il ne le laisse pas partir."
    noam inquiet "Coincé comment ? Il l'a menacé ?"
    nyra colere "Il veut lui faire promettre un vote pour. Et lui faire dire devant les caméras qu'il le soutient. Tomas a dit qu'il voulait réfléchir seul."
    noam colere "Et il s'acharne sur Tomas ?! Évidemment. Il pouvait pas commencer par quelqu'un qui lui répondrait non."
    nyra stress "C'est justement ce qui m'inquiète. Tomas n'ose pas lui tenir tête. Il va finir par dire oui pour avoir la paix... ou non pour se venger."
    noam determine "On y va. Avant qu'ils se mettent à voter pour savoir qui a le droit de quitter la pièce."
    nyra neutre "Et ne transforme pas ça en duel avec Julian. Tomas n'a pas demandé deux personnes de plus pour décider à sa place."

    stop music fadeout 0.5
    play music "music/bgm_world_decline.mp3" fadein 0.6

    # Effet de course : le décor tremble tant qu'on court (secousse day3_run_shake).
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_163
    scene couloir_dortoir at adaptive_fullscreen, day3_run_shake with fade

    think "Tomas a envoyé un message à Nyra. Pas à moi. Il savait visiblement qui serait la plus utile."

    play sound sfx_run

    think "Nyra avale les couloirs. Je la suis de mon mieux, en essayant d'oublier que mes jambes n'ont pas signé pour une course-poursuite."

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
    think "La voix de Julian traverse la porte. Pour une fois, je souhaiterais qu'il ait réellement appris à faire des discours brefs."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_165
    scene bg_repos at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("nyra", "neutre", 0.25),
        ("julian", "neutre", 0.55),
        ("tomas", "neutre", 0.85),
    ])

    if day3_corridor_success >= 2:
        think "On arrive juste au moment où Tomas essaie de mettre fin à la discussion. Sa voix est plus ferme que d'habitude. Ça ne suffit pas."
        tomas inquiet "Julian, je t'ai déjà répondu ! J'ai besoin de réfléchir. Tu peux me laisser passer ?"
        julian sourire "Justement, le vote est dans une heure ! Tu ne peux pas remettre ta décision à la dernière seconde et espérer qu'elle sera bonne !"
    else:
        think "Tomas serre sa tablette contre lui. Julian lui barre le passage avec l'assurance de quelqu'un qui croit rendre service."
        julian rire "Tomas, dis simplement que tu soutiens notre position, et on en termine ! Tu as une meilleure solution, peut-être ?"
        tomas peur "MAIS J'EN SAIS RIEN ! Je te le répète depuis dix minutes !"
    julian sourire "On va au Conclave ensemble, tu annonces que tu es pour, et tu verras : personne ne te posera plus la question."
    tomas inquiet "Mais c'est TOI qui dis que je suis pour !"
    "Julian se retourne vers nous. Tomas en profite pour s'éloigner de lui."

    call refutation_run("j3_julian")
    if _return[0] == "success":
        call play_noam_interupt
        if not day3_julian_clash_rewarded:
            $ player_kamyz += 20
            $ day3_julian_clash_rewarded = True
        julian hesitation "D'accord, personne ne m'a demandé de parler en son nom. Mais on doit bien prendre une décision !"
    else:
        tomas colere "Je t'ai dit d'arrêter, Julian. Ça suffit !"

    noam colere "Julian ! Il vient de te dire qu'il voulait partir. Tu as un problème avec le mot non ?"
    julian colere "Ah, Noam. Parfait. Nyra a recruté la police des bonnes intentions ?"
    nyra neutre "Tomas m'a demandé de venir. Il ne voulait plus discuter avec toi. C'est assez clair."
    julian reflexion "Je lui explique pourquoi son choix compte. Vous voulez interdire les discussions maintenant ?"
    tomas inquiet "Non ! Tu veux que je dise que je TE soutiens ! Tu n'as même pas demandé ce qui me faisait hésiter !"
    julian hesitation "C'est... ce n'est pas ce que je voulais dire."
    noam colere "On était derrière la porte. On t'a entendu lui dicter sa réponse !"
    julian colere "Et toi, tu fais quoi depuis ce matin ? Tu te promènes en espérant que l'unanimité va tomber du plafond ?!"
    noam colere "Au moins, je ne prends pas les autres pour des bulletins avec des jambes !"
    call cutin("julian") from _call_kd_cutin_3_julian
    julian colere "Tu crois que ça m'amuse ?! UN seul contre et trois jours d'efforts partent en fumée !"
    noam colere "Alors convaincs-le sur le TEXTE ! Pas sur la jolie photo de groupe que tu veux offrir aux caméras !"
    julian colere "Tu peux jouer les gentils parce que d'autres prennent le risque de défendre ce qu'ils croient juste !"
    tomas inquiet "MAIS VOUS ALLEZ VOUS TAIRE ?!"
    tomas colere "Je suis là ! Je suis pas une chaise qu'on déplace d'un camp à l'autre !"
    "Je me tourne vers Tomas. Il tremble de colère, et je réalise que je viens aussi de parler à sa place."
    noam culpabilite "T'as raison. Excuse-moi. J'aurais dû te demander ce que tu voulais au lieu de hurler."
    julian hesitation "Tomas, je ne voulais pas..."
    tomas inquiet "NON ! Vous m'écoutez pour une fois !"
    tomas inquiet "J'ai peut-être envie de voter pour, d'accord ? Mais maintenant, j'ai surtout envie de vous envoyer promener tous les deux !"
    nyra raison "Vous avez terminé ? Alors on va faire quelque chose de révolutionnaire : laisser Tomas réfléchir."
    nyra neutre "Julian, sors. Noam, reste."
    julian colere "Très bien. Mais si une seule hésitation nous fait perdre, rappelez-vous qui aura essayé de l'éviter."
    noam colere "Et rappelle-toi que les gens ont le droit de te dire non !"
    julian colere "Oui. On verra."

    hide julian with moveoutleft

    stop music fadeout 0.6
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6

    tomas hesitation "Je lui ai dit non à la discussion. Je sais pas pourquoi c'est plus difficile à comprendre qu'un non au vote."
    noam triste "Je ne t'ai pas beaucoup aidé. J'ai fait exactement ce que je lui reprochais."
    tomas hesitation "Je veux que les choses changent, moi aussi. Mais si on supprime les rations et que les gens n'ont plus rien, ça va être de ma faute ?"
    nyra neutre "Tu voteras sur le texte. Pas pour faire plaisir à Julian. Pas pour remercier Noam d'être venu."
    tomas inquiet "J'aurais juste voulu avoir peur tranquillement, vous voyez ? Sans que quelqu'un transforme ça en problème."
    noam determine "Prends le temps qui reste. On se retrouvera au Conclave."
    tomas hoche_la_tete "Ouais. Mais je vous en supplie, ne faites pas encore de moi l'enjeu de votre dispute."
    nyra sourire "Je reste avec lui. Et merci d'être venu sans casser une porte, Noam."
    think "Nyra reste auprès de Tomas. Je repars seul."
    think "Je m'étais promis de faire mieux que me disputer. Il est à peine midi, et j'ai déjà perdu une partie de ce pari."
    $ hideGroup()

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite


label _3_TRANSITION_CONCLAVE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_166
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Le groupe avance vers la salle du Conclave. Pas de grandes discussions, plus de plaisanteries. On dirait une classe qui rejoint une salle d'examen."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    think "Je repense à Tomas. Il voulait seulement qu'on lui laisse le choix."
    think "Et moi, je voulais que le texte passe. Il va falloir vérifier que ces deux souhaits ne deviennent pas incompatibles."

    $ showGroup([
        ("lysa", "neutre", 0.25),
        ("noam", "neutre", 0.50),
    ])

    "Lysa marche en retrait. Juste assez pour que ça se remarque."
    "Le groupe accélère quand le couloir se resserre. Elle, non. Elle traîne les pieds, exprès."

    lysa triste "On marche vers une défaite avec un sérieux admirable."
    lysa triste "Et demain ? Les mêmes chambres, les mêmes couloirs. Dans trois jours, on rejouera la même pièce."
    lysa blase "On se prend pour des législateurs et Kami tient les lumières, les portes et la sortie de secours."

    think "Lysa dit ça sans vraiment attendre de réponse. Elle paraît déjà convaincue qu’on va échouer."

    noam reflechit "On n'a pas encore voté, Lysa. Tu as déjà rédigé le communiqué de défaite ?"
    noam sourire "Attends au moins qu'on ait le droit de mettre nos bulletins dans l'urne."

    "Lysa fait une moue déconfite alors qu'on approche de la porte du Conclave."

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    think "Sael s'est laissée glisser à l'arrière du groupe, elle aussi. Volontairement. Elle observe Lysa depuis un moment."
    "Sans prévenir, sans théâtre, elle attrape Lysa et la serre contre elle."

    sael "Lysa... Tu peux arrêter de faire semblant d'aller bien cinq minutes ?"
    sael "Tu repères les problèmes avant tout le monde. C'est précieux. Mais si tu passes ton temps à les porter seule, tu vas t'écrouler."
    sael "On aura besoin de toi là-dedans. Pas de ta pire prédiction."

    "Elle pointe la poitrine de Lysa du doigt. Les épaules de Lysa se relâchent, à peine."

    lysa "Je suis toujours debout. C'est déjà une preuve de bonne santé."

    sael "Alors continue. Mais arrête d'annoncer l'échec avant même qu'on entre."

    lysa "D'accord... Mais tu me devras un café. Un vrai. Pas cette eau brune de station."

    sael sourire "Deux cafés, si tu veux. Et je remplirai les formulaires à ta place."

    lysa blase "Bon. On avance, avant que tu me fasses pleurer devant ces idiots."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_167
    scene bg_conclave at adaptive_fullscreen with dissolve

    think "La table circulaire nous attend. Je reconnais les sièges, les caméras, l'écran."
    think "Je découvre surtout que je déteste cette salle quand elle est pleine."

    play sound sfx_announce
    pause 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Douze représentants ! Douze sièges ! Pas un seul absent ! Vous voyez que vous êtes capables de vous entendre sur quelque chose : être à l'heure !"
    kami "J'aurais été tellement triste de devoir montrer une chaise vide au public. Quelle catastrophe pour la réalisation !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Ooooh ! Je vois que certains ont eu droit à un câlin avant de venir ! Ça me donne presque envie d'avoir des bras."
    kami "Cadreur imaginaire, gros plan sur ces petites âmes fragiles ! Oui, je fais aussi la réalisation. Je suis polyvalente."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Installez-vous. Dans quelques instants, vous allez découvrir combien vous tenez vraiment les uns aux autres."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade
    pause 0.4

    "Les portes se referment. Un déclic net résonne derrière nous."

    play sound sfx_door

    think "Le verrou claque. Je vérifie la poignée par réflexe."
    think "Bloquée. Un rappel discret que notre grand débat démocratique se déroule dans une cage."

# ============================================================================
# DÉBAT — PHASE 1 : le texte réel (Fatal Assembly)
# ============================================================================

label _3_DEBAT1_PHASE1:
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_3

    pause 0.4

    # Remise à zéro de l'adhésion des PNJ (base) avant que les phases 2/3 ne la modifient.
    $ debat_day3_reset_live_stats()
    # Report du résultat de la course : Tomas plus ou moins entamé par Julian.
    $ debat_day3_apply_influence({"tomas": tomas_corridor_delta})

    show screen kami_broadcast_ui

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Avant de vous chamailler, une formalité : peut-être faudrait-il savoir ce que vous allez voter."
    kami "Soyons rigoureux ! Voici le texte officiel. Le vrai, le beau, celui qui aura des conséquences."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Enfin, « officiel »... [codex_dialogue_link('archive', 'ARCHIVE')] l'a harmonisé avec les Commandements. Vous connaissez le principe : on prend votre idée et on lui met une cravate."
    kami "Votre petite phrase tenait sur un coin de nappe. La loi, elle, doit tenir debout devant le monde entier. Ça demande quelques mots de plus."

    $ bc_show("nyra", "stress", px=-70, py=-50, pz=0.85)
    nyra "Tu as corrigé sa forme... ou tu as modifié ce qu'il signifie ?"
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oh, j'ai rendu votre idée applicable. C'est une toute petite différence. Enfin... tout dépend de ce que vous appelez petit."
    kami "Tout est là ! Des articles, des conséquences, de merveilleux petits mots dont vous découvrirez l'importance quand ce sera trop tard."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "À vous de reconstituer le texte ! Oui, vous allez devoir LIRE. Je sais, quelle cruauté."
    kami "Et regardez bien les fins de phrase. Les catastrophes se cachent souvent dans un « en conséquence »."

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

    ryn colere "C'EST QUOI CE PAVÉ ?! On a demandé le commerce, pas un concours de lecture !"

    tomas inquiet "Attendez ! Si elle a ajouté une condition à la fin, on pourrait tout approuver sans s'en rendre compte. Il faut vérifier chaque phrase."

    nyra raison "Commencez par les liaisons logiques. Les virgules, les conséquences, les renvois. Le texte a une structure, même si Kami veut nous la faire chercher."

    noam "Bon. Mettons les morceaux dans l'ordre. Je refuse de voter sur un texte qu'on ne comprend pas."

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

    lysa reflexion "Attendez... « Autoriser le transport, la vente et l'échange de marchandises. » Très bien. Mais la suite..."
    lysa colere "« En conséquence, le système de distribution de denrées est aboli. » Vous avez bien LU ce passage ?!"
    call reactions([("elen", "peur"), ("ryn", "colere"), ("tomas", "peur")]) from _call_kd_reactions_3_abolition
    elen peur "HEIN ?! Mais j'ai déjà dit à tout le monde que je voterais pour ! Je savais pas qu'on supprimait les bons !"
    ryn colere "VOUS ÊTES MALADES ?! À LIMEN, ON MANGE QUOI QUAND LES BONS DISPARAISSENT ? LE TEXTE ?!"
    tomas peur "Non... hier, il n'y avait pas ça. Je l'aurais remarqué ! J'ai relu la phrase au moins dix fois !"
    iris colere "KAMI ! Tu t'es bien gardée de nous prévenir de cette petite conséquence, hein ?!"
    mara colere "Et voilà ! On m'a traitée de rabat-joie parce que je voulais LIRE ! C'était vraiment trop demander ?!"
    nyra stress "Attendez. On doit d'abord savoir si cette disposition est définitive. Arrêtez de parler tous en même temps !"


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

    mara surpris "Merveilleux. On commande du commerce et on nous livre la fin des rations. La prochaine fois, demandons des serviettes : elle supprimera l'eau."

    noam "Attendez. Personne n'a proposé explicitement de supprimer les rations."
    noam "Mais c'est ce texte-là qu'on devra accepter ou rejeter. Pas celui qu'on avait en tête."

    nyra reflechit "Si ce texte passe, la distribution gratuite s'arrête partout. Pas seulement là où le commerce peut fonctionner immédiatement."

    kael inquiet "Sans les rations... il faut revoir toute la chaîne d'approvisionnement. Immédiatement."

    ryn colere "À Limen, les bons sont peut-être nuls, mais c'est parfois le seul repas garanti ! On l'enlève et on leur dit de se débrouiller ?!"

    lysa reflechit "Le pire... c'est que je comprends son raisonnement."

    noam surpris "Logique ? Des gens vont perdre la seule nourriture qu'on leur assure !"

    lysa blase "Si on rétablit les ventes, il faut pouvoir payer. Et pour payer, il faut des revenus."
    lysa reflechit "Kami coupe les rations pour forcer les gens à entrer dans le jeu. Sur le papier, ça se tient."
    lysa colere "Sur le papier. Surtout pas dans une assiette vide."

    nyra reflechit "La transition prendrait normalement des mois. Là, on parle de demain. Même une bonne idée peut provoquer un désastre si on l'applique d'un coup."

    sael triste "On a déjà enterré trop de gens pour des règles décidées loin de chez nous."
    sael reflechit "Kami. Une seule réponse : est-ce que l'un de nous a réellement proposé tout ce qui figure ici ?"

    think "Kami ne répond pas. Ryn répète sa question, puis Tomas commence à protester lui aussi. L’écran reste inchangé."

    lysa blase "Elle n'a aucune raison de répondre. On ne sait pas qui a écrit quoi. On n'a que sa parole."
    lysa colere "Si elle déforme une proposition, comment on la contredit ? On va demander au coupable de se dénoncer ?"

    ryn reflechit "Attends... tu veux dire qu'elle pourrait inventer un texte entier ?"

    lysa salut "Qu'on n'a aucun moyen de vérifier. Et qu'on devrait peut-être arrêter de la croire sur parole."

    noam inquiet "Peut-être qu'elle nous manipule. Mais ce texte est devant nous, et c'est nous qui porterons la décision."

    # ── Mini-jeu buzzer (Objection Protocol) : influence l'adhésion des PNJ ──
    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oh là là ! Mon audimat s'endort ! Vous avez réussi à transformer une crise mondiale en réunion de copropriété !"
    kami "On change les règles du spectacle : un seul parle à la fois. J'ai pitié des oreilles de mes spectateurs."

    "Les pupitres se transforment. Un micro et un buzzer émergent devant chacun de nous."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Micro vert : vous parlez. Vous n'êtes pas d'accord ? Vous BUZZEZ ! C'est tellement simple que même vous devriez y arriver."
    kami "Vous appelez ça la délibération. Moi, j'appelle ça une excellente émission."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "À vos arguments ! Et essayez de ne pas vous tuer avant le vote, ça compliquerait le dépouillement."

label day3_before_objection_protocol_minigame:
    call refutation_run("j3_assemblee")
    if _return[0] == "success":
        call play_noam_interupt
        noam determine "Attendez. Le texte ouvre des échanges. Il ne garantit pas que ceux qui n'ont rien pourront acheter quoi que ce soit."
        lysa raison "Voilà. C'est exactement ce qui me gêne."
        $ debat_day3_apply_influence({"lysa": 1, "mara": 1, "tomas": 1})
    else:
        mara agace "On crie, on s'interrompt, et on n'a toujours aucune réponse sur la transition."
        $ debat_day3_apply_influence({"mara": -1, "tomas": -1})
    $ debat_phase2_vote_summary = debat_day3_compute_votes()

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
                    add Transform(character_image("noam", "neutre"), zoom=0.85):
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
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
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

    noam inquiet "On a compris ce qu'elle a ajouté. Mais on fait quoi, maintenant ? On ne peut pas décider ça entre deux cris."

    julian colere "Entre deux cris ?! Ça fait un an que les gens manquent de tout ! Tu veux leur demander d'attendre encore combien de temps ?"

    ryn colere "Et ton grand projet, c'est quoi ?! On sacrifie Limen pour que Nexus se paie des nouveaux jouets ?!"

    julian surpris "Tu crois que tous ceux de Nexus roulent sur l'or ?! J'en viens, figure-toi !"

    ryn "...C'est pas ce que j'ai dit ! Enfin, si, mais c'est pas le problème !"

    mara taquin "Économise ta salive, Ryn. On n'a même pas encore le droit de cocher une case."

    elen joie "Mais imaginez ! Acheter quelque chose sans devoir raconter pourquoi on en a besoin à un distributeur !"

    # (combinaison « lysa raison » ajoutée dans images.rpy)
    lysa raison "Pour acheter, il faut de l'argent, Elen. Une vitrine pleine ne nourrit personne quand ton portefeuille est vide."

    tomas hesitation "Je... j'ai regardé les chiffres de production. Dans certains secteurs, on fabrique presque quatre fois moins qu'avant."
    tomas inquiet "Alors oui, continuer comme ça me fait peur aussi."

    nyra reflechit "Ce n'est pas étonnant. Quand produire davantage n'apporte aucune possibilité supplémentaire, le système encourage souvent à se limiter au minimum."

    # Cadrage de Kami : moins clownesque, plus prédatrice.
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "ENFIN ! Vous avez commencé à vous battre avec des arguments plutôt qu'avec des meubles. Je suis fière de vous !"
    kami "Je vous rappelle que ce petit monstre est né de VOTRE imagination. Moi, je n'ai fait que lui donner des dents."
    kami "Continuez ! La peur vous rend tellement éloquents. Et puis je trouve que la rougeur vous va très bien."

    play sound "audio/trailer/trl_impact_deep.wav"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], phase=3, prompt="Premier échange — Quel argument présenter ?")
    if p3_pick is not None and p3_round_options[0][p3_pick]["unlocked"]:
        $ p3_argument_one = p3_round_options[0][p3_pick]["id"]
        call _3_DEBAT1_PHASE3_INT1 from _call__3_DEBAT1_PHASE3_INT1
    else:
        $ p3_argument_one = None
        think "J'ai des opinions. Beaucoup trop. Pas encore un argument que je pourrais défendre devant tout le monde."

    scene bg_conclave at adaptive_fullscreen with dissolve

    elias "Moi je comprends qu'on ait peur. Mais à la Forge, on remplit plus de formulaires qu'on ne répare de machines ! On peut pas appeler ça un système qui marche !"

    sael "Chez nous, on s'aide déjà sans attendre les bons."
    sael determine "Je ne dis pas que le changement sera simple. Je dis qu'on a fini par dépendre d'une permission pour tout."

    lysa blase "Vous êtes très enthousiastes, mais il manque toujours un détail : l'argent."
    lysa reflechit "D'où viennent les premiers salaires ? On fait comment pour acheter quoi que ce soit quand personne n'a reçu le moindre paiement ?"

    noam inquiet "Kami ! Tu as prévu des revenus dès le premier jour ou il faudra apprendre à manger des promesses ?"

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh ! Une question pratique ! Mes petits représentants découvrent l'économie ! Je suis si émue."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Si le texte passe, je proposerai des contrats rémunérés. Des tâches, des objectifs, un salaire. Comme dans vos vieux souvenirs d'avant moi, mais avec moins de paperasse inutile."
    kami "Vous produisez, récoltez, transportez, réparez. Je vous paie. Vous achetez. Facile, non ?"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Vous serez libres de travailler. Ou de ne pas travailler. Attention : la liberté de ne rien gagner est incluse dans l'offre."
    kami "Et ceux qui refuseront de travailler ? Eh bien... il faudra se débrouiller. Les rations ne seront plus là pour attendre les retardataires. Motivant !"

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

    elen inquiet "Mais... les gens malades ? Les personnes qui ne peuvent pas travailler ? Ils vont manger quoi ?"
    ryn colere "Et les vieux ?! Et ceux qui ont déjà plus la force de se lever ?! C'est quoi, le programme, on les laisse crever ?!"
    sael determine "Chez nous, personne n'est abandonné parce qu'il ne peut pas travailler. La solidarité, ça ne se mesure pas à la quantité produite."
    mara colere "Attendez ! Elle supprime les rations ET décide quels contrats existent. C'est elle qui contrôle les deux côtés de l'équation !"
    julian reflexion "Au moins, le travail redeviendra une manière de gagner quelque chose. On ne peut pas rester éternellement coincés avec les anciens bons."
    lysa blase "Et si tous les contrats sont à Nexus ? Les habitants des autres districts vont payer le trajet avec leurs bonnes intentions ?"
    elias reflechit "Moi, je trouverais sûrement à réparer des choses. Mais un type sans formation, sans outil et sans moyen de transport, il commence comment ?"
    tomas inquiet "Et le premier salaire, il tombe quand ? Aujourd'hui ? Dans une semaine ? Les gens ne peuvent pas mettre leur faim sur pause !"
    nyra raison "Kami, précise au moins le calendrier. À partir de quand ces contrats seront-ils disponibles, et comment seront assurées les livraisons ?"
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Contrats disponibles dès l'entrée en vigueur ! Pour l'approvisionnement, vous découvrirez les joies de l'organisation humaine. Après tout, vous vouliez reprendre les choses en main !"
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
    iris colere "Magnifique ! Elle distribue les contrats et nous laisse gérer les conséquences ! Même son service après-vente est une blague !"
    kael inquiet "Sur Orbite, il suffit de manquer une livraison critique pour perdre des vies. Ce n'est pas un désagrément administratif."
    noam inquiet "Au départ, on voulait pouvoir obtenir ce qui manque. Maintenant, on doit décider si on supprime le filet qui protège encore des familles."
    noam inquiet "Je ne peux pas faire comme si ces deux décisions étaient identiques."
    sael neutre "Nous devrons choisir quand même. Mais personne ne devra prétendre qu'il n'avait pas compris les risques."

    play sound "audio/trailer/trl_impact_deep.wav"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], phase=3, prompt="Dernier échange — Quel argument présenter ?")
    if p3_pick is not None and p3_round_options[1][p3_pick]["unlocked"]:
        $ p3_argument_two = p3_round_options[1][p3_pick]["id"]
        call _3_DEBAT1_PHASE3_INT2 from _call__3_DEBAT1_PHASE3_INT2
    else:
        $ p3_argument_two = None
        think "J'aurais aimé trouver une phrase capable de les rassurer. Je n'en connais aucune qui soit honnête."

    scene bg_conclave at adaptive_fullscreen with dissolve
    pause 0.3

    noam inquiet "On peut discuter encore des heures. On ne saura pas tout. À un moment, il faudra choisir en acceptant cette incertitude."
    nyra neutre "On connaît les bénéfices possibles et les risques immédiats. Personne ne peut décider à la place des autres."

    # ── CLIFFHANGER 2 : le dernier indécis, avant le vote ──
    think "Je cherche Kael du regard. Chaque mot du débat semble l'avoir un peu plus éloigné d'une réponse."

    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "reflechit", 0.32),
        ("kael", "inquiet", 0.68),
    ])

    noam "Ryn... Kael... Vous avez réussi à vous décider ?"

    ryn triste "...Moi, je sais ce que je dois faire. Que ça me plaise ou non. Demain, je devrai regarder les gens de Limen en face."

    think "Reste Kael. Il m'avait dit qu'il déciderait devant le bulletin. Le bulletin n'est plus très loin."

    kael inquiet "Je…"

    kael triste "Sur Orbite, une erreur peut tuer des innocents. Et je n'arrive pas à savoir si ce texte nous ouvre une porte..."
    kael peur "...ou s'il retire simplement le dernier filet qui nous empêchait de tomber."

    noam inquiet "Kael, on peut te laisser une minute. Personne ne va te forcer à..."

    think "Il ouvre la bouche."

    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "STOOOOOP !"
    kami "Non, non, NON ! Ne gâchez pas le suspense en lui faisant prononcer son choix avant le bulletin !"
    kami "Une main qui tremble au moment de voter... c'est de l'or pour l'audience ! Ne me privez pas de ça."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Gardez votre courage, vos regrets et vos petites lâchetés pour le secret de l'urne. C'est beaucoup plus élégant."
    kami "Une seule voix contre, et tout tombe. Je vous le répète une dernière fois, parce que je vous aime."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Alors... PLACE AU VOTE ! Pour, contre, abstention : il est temps de voir ce que vous valez quand plus personne ne vous entend."
    kami "J'ai tellement hâte de compter. Et ne vous inquiétez pas : je sais compter jusqu'à douze."

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

        noam inquiet "Ryn, tu disais que les bons ne suffisaient même plus chez toi. Tu parlais de quelques pénuries... ou de quelque chose de permanent ?"

        elias determine "Un bon pour du riz, et l'entrepôt est vide ! On a gagné quoi ? Le droit officiel d'avoir faim ?"

        julian sourire "Si les producteurs peuvent enfin vendre ce qu'ils fabriquent, ils auront une raison d'augmenter la production. On ne peut pas ignorer ça."

        mara doute "Très bien. Et si les acheteurs les plus riches raflent tout, qui livrera Limen ? Le Père Noël ?"

        ryn colere "Voilà ! Nexus se remplira les poches et nous, on verra passer les camions sans pouvoir les arrêter !"

        kael reflechit "Limen, c'est aussi beaucoup de clients potentiels. Certains commerçants voudront peut-être s'y installer."

        ryn reflechit "...Peut-être. Encore faut-il qu'on ait quelque chose à leur donner."

        sael neutre "Chez moi, on partage, mais ça ne fait pas apparaître de la nourriture par magie. Je comprends qu'on cherche autre chose."

        elen joie "Et si ça permettait enfin aux gens de trouver ce qu'il leur manque ? Même juste une fois sans supplier Kami ?"

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

        noam inquiet "On a des bons censés garantir le nécessaire, mais certains rentrent les mains vides. On peut vraiment dire que ça fonctionne ?"

        tomas raison "J'ai regardé les statistiques... Dans certains secteurs, les ruptures touchent plus de la moitié des produits sur de longues périodes."

        iris colere "Tu peux avoir un bon parfaitement valable et attendre toute la journée devant un stock vide. Le papier ne nourrit personne."

        ryn colere "À Limen, le lait arrive parfois déjà tourné. Les médicaments sont périmés avant même qu'on puisse les distribuer !"
        ryn triste "Et après on nous explique qu'on devrait être reconnaissants d'avoir des tickets. Des tickets pour des choses qui n'arrivent pas."

        mara reflexion "Le système est nul. Je le sais. Mais le supprimer d'un coup, sans savoir par quoi le remplacer, c'est une autre folie."

        elias determine "Et on reçoit les mêmes refus, qu'on passe la journée à réparer des machines ou qu'on reste chez soi ! Ça finit par dégoûter les gens."

        elen joie "Moi, j'aimerais juste que personne n'ait besoin de se disputer pour trois pommes et un paquet de riz ! C'est trop demander ?"

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

        nyra raison "Vous parlez des pénuries au sol. Mais une erreur logistique sur Orbite ne se rattrape pas avec une livraison le lendemain."

        kael mefiant "Là-haut, un filtre ou une pièce manquante peut devenir une urgence vitale. On ne peut pas improviser."
        kael triste "On ne peut pas faire comme si une livraison ratée ne coûtait qu'un peu de confort."

        noam "Si les circuits commerciaux changent sans transition, toutes les livraisons pourraient être perturbées."

        iris inquiet "...Là, ça devient sérieux. On risque des vies pour avoir des rayons mieux remplis ?"

        tomas raison "Il y a relativement peu de morts sur Orbite. Il faut peut-être admettre que certaines règles protègent vraiment."

        julian hesitation "Je comprends le danger. Mais si on renonce à tout changement dès qu'il comporte un risque, on ne sortira jamais de ce système."

        lysa blase "Une seule livraison ratée, et tout un module peut trinquer. Ça devrait suffire à calmer quelques beaux discours."

        nyra stress "Sur Orbite, on ne peut pas attendre trois jours pour corriger une erreur. Le vide n'accorde pas de délai parlementaire."

        mara stress "...Génial. On prend notre décision ici, confortablement assis. Et ce sont des inconnus enfermés dans une boîte métallique qui pourraient en payer le prix."

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
        noam "Sael, tu nous as parlé de ton village. Chez toi, personne ne reste sans aide quand il ne peut plus travailler ?"
        sael neutre "Non. On aide ceux qui en ont besoin. Ceux qui peuvent participer le font. C'est ce qui permet au village de tenir."
        elias reflechit "Je comprends. Mais les contrats de Kami, ils prévoient quoi pour ceux qui ne peuvent pas travailler ?"
        mara doute "Voilà. On parle de liberté comme si tout le monde partait avec les mêmes chances."
        noam inquiet "Et ceux qui sont incapables de signer un contrat, ils deviennent quoi dans ce nouveau système ?"
        ryn reflechit "Enfin une question qui ne vient pas d'un catalogue de belles promesses."
        $ debat_day3_apply_influence({"sael": 1, "elias": 1, "mara": -1, "ryn": 1})

    elif selected == "derogations_complexes":
        $ showGroup([
            ("elen", "reflechit", 0.16),
            ("iris", "blase", 0.38),
            ("kael", "calme", 0.60),
            ("nyra", "raison", 0.82),
        ])
        noam sourire "Elen a failli devoir organiser un référendum pour commander des fraises. Vous trouvez ça raisonnable ?"
        elen reflechit "Trois pages ! Et j'avais même pas encore demandé les épices ! J'ai cru que j'allais y passer la nuit."
        iris blase "Même procédure absurde pour obtenir une pièce détachée. Et on s'étonne que plus rien n'avance."
        kael calme "Certains dossiers d'équipement prennent plusieurs jours. Pour une urgence, c'est une éternité."
        nyra raison "Nous sommes donc d'accord sur un constat : l'organisation actuelle entrave même les besoins les plus banals."
        noam inquiet "Voilà pourquoi j'ai envie de changer les règles. Mais l'amendement qu'on nous propose est-il vraiment la bonne réponse ?"
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

        iris reflechit "Avant Kami, les prix augmentaient parfois plus vite que les salaires. Vous avez oublié ça ?"
        iris reflechit "Mais quand quelque chose manquait, on pouvait chercher ailleurs. Ça nous laissait au moins une chance."

        elen joie "Voilà ! Tu pouvais acheter des chaussures sans devoir prouver qu'elles étaient vraiment trouées !"

        julian sourire "Le monde d'avant était loin d'être parfait. Mais tu pouvais essayer, échouer, recommencer. Aujourd'hui, on attend qu'une IA autorise le moindre changement."

        mara reflexion "« Choisir »... C'est un très joli mot quand on a les moyens de choisir."
        mara reflexion "Moi, je me souviens des portes qui se fermaient devant toi quand tu n'avais pas le bon visage, les bons contacts, la bonne façon de sourire."
        mara triste "La liberté d'avant n'avait pas le même prix pour tout le monde. Je suis bien placée pour le savoir."

        tomas raison "Et il y avait des guerres. Des destructions énormes. Avec Kami, les affrontements de cette ampleur ont diminué... enfin, d'après les données."

        ryn colere "Les données ? Va expliquer tes statistiques aux gamins de Limen qui grandissaient avec les restes des autres !"

        noam "Avant Kami, l'argent donnait déjà des possibilités aux uns et les retirait aux autres. Ça ne suffit pas de dire qu'on était plus libres."

        elen joie "Alors... pourquoi on ne pourrait pas garder ce qui marche et changer le reste ?! La liberté, sans laisser les gens mourir de faim !"

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

        ryn colere "Lisez les mots ! « Suppression des bons. Fin de la distribution. » C'est écrit. Noir sur blanc !"
        ryn colere "Pas un mot pour ceux qui ne peuvent pas payer. Pas de délai. Pas de minimum vital. RIEN !"

        elias determine "Mais si on garde les bons, on reste dépendants de la permission de Kami pour chaque pièce, chaque outil, chaque repas !"

        noam inquiet "On ne peut même pas proposer de maintenir les bons quelques semaines. On nous demande de tout supprimer, ou de ne rien changer."

        kael triste "Sur Orbite, couper les circuits actuels sans savoir par quoi les remplacer, ça pourrait nous tuer. On ne change pas une livraison vitale du jour au lendemain."

        lysa blase "Le mot est « supprimer ». Pas « aménager ». Si on vote oui, il faudra assumer ce qu'il signifie."

        ryn colere "Sans les bons, à Limen, on crèvera en silence pendant que vous organiserez votre jolie économie !"
        ryn colere "Et les gens trop vieux ou trop malades pour bosser ? Ils font quoi ? Ils meurent en attendant un emploi ?!"

        mara stress "...Au moins, cette fois, ce sera notre responsabilité. On ne pourra pas prétendre qu'on n'avait pas lu."

        sael determine "Les gens échangent déjà ce qu'ils peuvent. Ce n'est pas Kami qui les a inventés, ces échanges."

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

        ryn surpris "Attends... tu veux dire qu'il y a déjà des échanges en douce chez nous ?"

        sael reflechit "Depuis toujours. Un peu de nourriture contre une réparation. Du tissu contre un service. Quand les rations manquent, c'est parfois ce qui fait tenir les familles."

        noam "Entre voisins, ça peut fonctionner. Mais à l'échelle de tous les districts, c'est autre chose."

        kael doute "Si les gens le font déjà malgré les interdictions, il y a peut-être moyen d'organiser ces échanges sans tout bouleverser d'un coup."

        julian sourire "Voilà ! Les gens ont déjà commencé à se débrouiller. On ne fait que leur rendre le droit de le faire ouvertement."

        lysa blase "Et il y aura toujours quelqu'un pour se faire payer très cher le passage d'un sac de riz."

        ryn reflechit "...Si ça sauve déjà des gens, peut-être qu'on pourrait en faire quelque chose de plus grand. Sans devoir se cacher pour survivre."

        mara reflexion "Tiens. Un argument qui ne sort pas d'un joli discours. Ça existe, ça fonctionne parfois. C'est déjà plus convaincant."

        sael determine "Pour l'instant, on survit. Je voudrais qu'on puisse recommencer à vivre."

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
        noam "On parle de supprimer les bons. Mais aujourd'hui, certains districts en reçoivent sans jamais pouvoir les utiliser."
        ryn colere "À Limen, tu peux faire la queue toute la journée et rentrer sans une miette !"
        iris blase "Deux options : garder un système défaillant ou supprimer sa dernière protection. Quelle magnifique conception du choix."
        tomas hesitation "On... on devrait au moins avoir une période de transition. Quelque chose pour éviter que les gens se retrouvent sans rien."
        mara doute "Mais on ne peut pas ajouter un mot au texte. C'est le piège depuis le début."
        noam inquiet "Même si on adopte cet amendement, il restera des problèmes. Peut-être même des problèmes plus graves."
        $ debat_day3_apply_influence({"ryn": -1, "mara": -1, "tomas": -1, "iris": 1})

    elif selected == "approvisionnement":
        $ showGroup([
            ("lysa", "blase", 0.12),
            ("nyra", "raison", 0.34),
            ("kael", "inquiet", 0.56),
            ("elen", "inquiet", 0.78),
        ])
        noam "Déjà aujourd'hui, deux familles de deux districts différents n'obtiennent pas du tout les mêmes ressources."
        lysa blase "Et demain, si on instaure les ventes, ceux qui possèdent déjà quelque chose auront toutes les chances de passer devant les autres."
        nyra raison "Pas nécessairement. Une augmentation des échanges pourrait aussi favoriser les districts actuellement délaissés. Il faut considérer les deux possibilités."
        kael inquiet "Tout dépendra des circuits d'approvisionnement. Sur Orbite, une livraison ratée ne se corrige pas facilement."
        elen inquiet "Donc... même en y réfléchissant tous ensemble, on ne peut pas savoir si ça va améliorer les choses ?"
        noam "C'est ça. Et ce n'est pas Kami qui assumera notre choix. Ce sera nous."
        $ debat_day3_apply_influence({"lysa": -1, "kael": -1, "nyra": 1, "elen": 1})

    return

# ============================================================================
# ISSUES DU VOTE
# ============================================================================

label _3_VOTE_POUR:

    $ current_period = "Soir"
    
    scene bg_conclave at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    pause 1.2

    $ interject("ADOPTÉ", color="#5DFF9A")

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "VEEEEERT !"
    kami "ADOPTÉ ! Aucun vote contre ! Vous avez réussi à vous mettre d'accord ! Je... je crois que je vais pleurer. Enfin, si j'avais des glandes lacrymales."
    kami "Dès l'application du texte : adieu les bons de rationnement, adieu la distribution gratuite. Vous avez coupé un lien qui vous attachait depuis longtemps."
    kami "Le transport, le stockage, la vente et l'échange de marchandises sont autorisés. Félicitations, vous venez de rendre au monde une chose qu'il avait oubliée."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Bravo, mes petits révolutionnaires ! Vous avez demandé la liberté. Et moi, je vous l'offre."
    kami "En revanche... vous êtes-vous demandé pourquoi certains avaient peur de lâcher la laisse ?"
    kami "Désormais, vous marcherez sans filet. Oh, comme j'ai hâte de voir qui saura tenir debout !"

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    think "Vert."
    think "Elen pousse un cri. Julian bondit de son siège. Pendant une seconde, j'ai presque envie de les rejoindre."
    think "Puis je remarque que Kael n'a pas bougé."

    $ showGroup([
        ("julian", "sourire", 0.15),
        ("ryn", "jaloux", 0.38),
        ("elen", "joie", 0.61),
        ("mara", "rire_profond", 0.84),
    ])

    julian joie "ON A RÉUSSI ! NOTRE PREMIER AMENDEMENT ! Vous vous rendez compte ?! On a vraiment changé quelque chose !"
    elen joie "OUAAAAAIS ! Tout le monde a dit oui ! Enfin... personne n'a dit non, c'est pareil, non ?"
    mara taquin "Doucement avec les confettis. On vient aussi de supprimer les rations de tout le monde."

    ryn jaloux "Ouais... Quelle victoire."
    ryn inquiet "Chez moi, les gens vont morfler tant que les échanges ne seront pas en place. J'espère que vous en avez conscience."

    noam sourire "On a réussi à adopter un texte. Je voudrais fêter ça... mais je n'arrive pas à oublier ceux qui vont perdre leurs bons demain."

    mara rire_profond "Enfin, du choix ! Des magasins ! Des prix ! Des vendeurs qui vous expliqueront que leur soupe est exceptionnelle !"
    mara taquin "Et si on doit crever de faim, au moins on pourra choisir la sauce. Quel progrès."

    $ showGroup([
        ("elen", "joie", 0.30),
        ("kael", "mefiant", 0.70),
    ])

    kael mefiant "Orbite pourra tenir... si les procédures de sécurité restent intactes. Il faut juste qu'on ne rompe aucun maillon."
    kael triste "Si."

    think "Julian sourit aux caméras. Elen cherche quelqu'un à serrer dans ses bras. Ryn détourne le regard."
    think "Kael murmure quelque chose à Nyra. Elle ne lui répond pas."
    think "Une victoire. Je suppose que c'est le mot."
    think "Pourtant, personne n'a exactement l'air d'avoir gagné la même chose."

    $ hideGroup()

    think "Il est dix-sept heures dix. Julian parle déjà de la prochaine réforme. Ryn passe devant lui sans un mot."
    think "Je crois que notre première unanimité n'a pas rendu les gens plus proches."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_184
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Dans le couloir, les voix de la fête se perdent derrière moi. Je n'arrive pas à décider si je devrais être fier ou inquiet."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_185
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Il y a deux jours, je croyais que la difficulté serait de nous mettre d'accord."
    think "Aujourd'hui, je me demande si nous nous sommes réellement entendus sur les conséquences."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_186
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je tombe sur le lit. Demain, le monde sera différent."
    think "Et si les premières mauvaises nouvelles arrivent, personne ne pourra dire que nous n'étions pas prévenus."

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
    kami "ROOOOOUGE !"
    kami "REJETÉ ! Un seul vote contre ! Une toute petite voix a suffi pour anéantir votre belle unanimité."
    kami "Les bons restent en place. La distribution gratuite continue. Le commerce reste interdit. Rien ne change... pour le moment."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Alors, la prochaine fois que vous vous plaindrez d'un bon de rationnement, pensez à ce joli instant."
    kami "Vous aviez la possibilité de tout bouleverser. Quelqu'un ici a dit non. Qui ? Mais voyons... le secret du vote, c'est sacré !"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Félicitations, mes petites souris prudentes ! Vous avez préféré garder vos habitudes. Je suis presque attendrie."
    kami "C'est beaucoup moins amusant pour moi, évidemment. Mais rassurez-vous : nous avons encore de nombreux votes pour nous détester."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    play music "music/bgm_world_decline.mp3" fadein 2.0
    think "Rouge."
    think "L'écran s'éteint. Pas de cris, pas d'applaudissements. Rien."
    think "Puis Julian repousse sa chaise si violemment que tout le monde sursaute."

    $ showGroup([
        ("julian", "colere", 0.02),
        ("ryn", "fatigue", 0.26),
        ("mara", "colere", 0.50),
        ("elen", "triste", 0.74),
        ("kael", "doute", 0.90),
        ("nyra", "raison", 1.14),
    ])

    julian colere "NON ! On avait une chance ! Une vraie chance de changer quelque chose !"

    ryn fatigue "On pouvait aussi condamner des gens à crever sans rations. C'est pas si simple."

    mara colere "Fantastique. On garde les pénuries, les formulaires et les files d'attente. On a sauvé notre petite routine !"

    elen triste "Je... j'étais sûre qu'on y arriverait. Même juste pour une fois."
    elen triste "Je l'avais presque promis aux gens qui nous regardent..."

    kael doute "On a évité une transition dont on ne connaissait pas les dangers. Mais on garde les problèmes actuels. Ce n'est pas vraiment une victoire."

    nyra raison "Arrêtez ! On ne sait pas qui a voté contre, ni pourquoi. Vous allez accuser onze personnes au hasard ?"

    think "Julian frappe brusquement la table. Elen sursaute et Tomas lui demande de se calmer, mais il ne l’écoute pas."

    julian colere "Et ça, c'est censé être une décision responsable ?! On n'a même pas essayé !"
    julian colere "On va continuer à rationner des miettes pendant que les gens manquent de tout ! On avait une ouverture, et quelqu'un l'a refermée !"

    ryn colere "C'est la règle ! Tu voulais convaincre tout le monde. Tu n'as pas réussi !"
    ryn colere "Et celui qui a dit non avait peut-être des raisons ! Tu sais ce que Limen risquait de perdre ?!"

    julian colere "ET TU SAIS CE QU'ON RISQUE EN CONTINUANT COMME AVANT ?!"

    ryn colere "BAISSE D'UN TON, OU JE VAIS TE FAIRE ASSEOIR !"
    mara colere "Pendant ce temps, ceux qui ont les moyens de contourner les règles continueront à se débrouiller. Quelle surprise."
    noam colere "Julian, arrête ! On ne peut pas refaire le scrutin en hurlant plus fort que les autres !"
    nyra neutre "Personne ne changera le résultat aujourd'hui. Sortez, reposez-vous, et évitez de vous accuser tant que vous ne savez rien."

    think "Il est presque dix-sept heures. Nous avions douze sièges autour d'une table. Je me demande combien de personnes accepteront encore de s'y asseoir ensemble."
    think "Le vote était secret. Mais à voir Julian dévisager les autres, le secret vient de devenir un motif de soupçon."

    think "Je me lève sans dire au revoir. Les voix continuent derrière moi. Pour une fois, je n'ai plus envie d'essayer de les réunir."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_189
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Le couloir est désert. Mes pas font plus de bruit que les applaudissements qu'on n'aura jamais."
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_190
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Je traverse le dortoir. La porte de chaque chambre me paraît être une bonne raison de ne parler à personne."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_191
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit, encore habillé. Je n'ai même pas la force de poser ma tablette."
    think "La voix de Julian me revient. Puis celle de Tomas dans la salle de repos."
    think "On prétendait vouloir convaincre les autres. Aujourd'hui, on leur a surtout appris à se méfier."
    think "Dans trois jours, il faudra recommencer. Avec les mêmes personnes, les mêmes règles... et beaucoup moins de confiance."

    $ phase3_over = True
    $ vote1 = "NON"
    $ kami_grant_chapter_1_ending_reward("vote_non")

    call show_chapter_title("Fin du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title_1

    pause 3.0

    call end_day("4", sleeping=True) from _call_end_day_24

    jump _4_0_REVEIL_CHAMBRE

# Total jour 3 : 17m
# Total J0-J3 : 1h25
