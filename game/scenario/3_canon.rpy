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
            day2_vote_add_argument(arg_id)
            store.j3_codex_dot = True
            return True
        renpy.restart_interaction()

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
        "Argument ajouté au dossier du vote."
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

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.5

    think "J'ai à peine dormi. Chaque fois que je fermais les yeux, je revoyais le même mot : unanimité."

    scene bg_cg012 at adaptive_fullscreen with fade

    think "Le plafond blanc me fixe autant que je le fixe."
    $ blink()

    think "Dans le couloir, les pas traînent déjà. Personne ne court. Personne ne parle fort."
    think "C'est le silence des gens qui savent qu'aujourd'hui, quelqu'un va perdre."
    $ blink()

    play sound sfx_announce
    pause 1.0

    # ── Diffusion du matin : Kami joueuse mais tranchante ──
    stop music fadeout 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits représentants."
    kami "Vous avez la tête de gens qui ont mal dormi. C'est parfait."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Aujourd'hui, C'est JOUR DE VOOOOOTE !"
    kami "L'un de vous a écrit un texte. Dans quelques heures, on saura s'il valait vraiment la peine d'exister."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Petit rappel, mais je pense que ça commence à imprimer : il suffit d'un seul « non »."
    kami "Un seul. Et tout ce que vous avez construit ces trois jours retourne au néant."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Alors soyez adorables les uns envers les autres."
    kami "Rendez-vous au Conclave à quatorze heures. Je compte les têtes. J'espère les compter toutes."

    pause 0.3
    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "« J'espère les compter toutes. »"
    think "Même quand elle sourit, elle rappelle qu'elle peut soustraire."

    pause 0.6

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_157
    scene bg_chambre at adaptive_fullscreen with fade

    call day3_play_wakeup_trace from _call_day3_play_wakeup_trace

    think "Debout. La cafétéria d'abord. On ne débat pas le ventre vide."

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

    think "Kael est adossé au mur, là où la ventilation fait le moins de bruit. Comme s'il se cachait du son."

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("kael", "fatigue", 0.65),
    ])

    kael fatigue "Oh. Noam."

    think "Sa voix est plus basse que d'habitude. Presque enrouée."

    noam "Tu vas à la cafétéria ?"

    kael reflechit "Dans une minute. J'essaie juste de… ralentir mon cerveau."

    noam "Le vote ?"

    kael inquiet "Tout le monde répète que les effets seront minimes."
    kael inquiet "Ils ne le seront pas. Sur Orbite, rien n'est jamais minime. Un écart, et c'est le vide."

    kael mefiant "Un module dépend d'une chaîne logistique au gramme près. Change le flux, et tu joues avec des vies là-haut."

    think "Ce qu'il décrit, je pourrai le ressortir au débat. La fragilité d'Orbite, personne d'autre ne la mesure vraiment."

    # Déblocage optionnel de l'argument « Risque de dépressurisation » (sinon disponible au Jour 2).
    call day3_collect_vote_argument("orbite") from _call_day3_collect_vote_argument_orbite

    think "Il évite mon regard, comme si le plafond avait la réponse."

    noam "Tu veux voter contre ?"

    kael surpris "Non. Enfin… je suis pour. En théorie."
    kael culpabilite "Mais toucher aux règles de ce monde, ça me terrifie. Et je déteste avoir peur devant les autres."

    noam "On a tous peur. Vouloir que rien ne bouge, c'est un choix aussi. Et il tue aussi, juste plus lentement."

    kael calme "…Ouais. On verra à quatorze heures."
    kael sourire "Merci d'être passé. Ça aide, même si je le montre mal."

    hide noam
    hide kael

    think "Un « pour » qui tient à un fil. Je note ça quelque part, tout au fond."

    pause 0.5
    jump DORTOIR_TP

label _3_OPT_JULIAN_DIAL:
    scene expression Image(corridor_background("cafeteria")) at adaptive_fullscreen with dissolve
    $ day3_cafeteria_route_julian_seen = True
    think "Julian tapote le distributeur comme si la machine lui devait un service."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("julian", "joie", 0.75),
    ])

    julian joie "Noam. Prêt à ouvrir la première brèche dans ce système ?"

    noam "On va essayer."

    julian rire "Essayer ? Non. On va le faire."
    julian "Le café, lui, résiste encore. Mais ça viendra."

    think "La tasse déborde sur ses doigts. Sa mise en scène, elle, reste intacte."

    julian reflexion "Si ce texte passe, on ouvre la première fissure depuis la prise de pouvoir de Kami."
    julian joie "Commerce. Échanges. Mouvement. Les gens ont besoin de sentir que quelque chose bouge enfin."

    noam "Et si ça ne passe pas ?"

    julian hesitation "Ça passera. On n'est pas venus entretenir le statu quo."
    julian idee "Les gens veulent un changement visible. Quelqu'un doit l'incarner."

    noam "Tu es sûr que tout le monde suivra ?"

    julian hesitation "…Certains ont juste besoin qu'on formule leur courage à leur place."
    julian sourire "Imagine : des ressources qui circulent, des districts qui échangent. Comme avant. Ce tableau ne te parle pas ?"

    noam "Dit comme ça… si. Ça me parle."

    julian sourire "À quatorze heures, on change ce monde."

    call day3_collect_vote_argument("monde_avant") from _call_day3_collect_vote_argument_monde_avant

    hide noam
    hide julian

    return

label _3_CAFETERIA_ARRIVE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_159
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    think "La cafétéria se remplit doucement. Le brouhaha se limite au raclement des chaises et au bruit des fourchettes."
    think "Qui, ici, pourrait voter contre ? Mara ? Sael serait frontale. Ryn est furieux, mais pour qui ?"
    think "Et moi… suis-je seulement convaincu qu'il faut refaire comme avant ?"

    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("noam", "neutre", 0.82),
        ("elen", "joie", 0.22),
        ("iris", "fatigue", 0.50),
    ])

    pause 0.3

    scene bg_cg013 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg013")

    think "Elen protège un bol énorme et fumant. L'odeur tient de la forêt et du caramel. Un mélange que rien ne devrait autoriser."

    pause 0.3

    iris "C'est quoi, ce truc ? Elen, tu ne peux pas avaler ça."

    elen "C'est. Une. Masterpiiiiece."

    iris "Pourquoi, chaque fois que tu dis ce mot, c'est exactement l'inverse ?"

    elen "Maiiiis non, ch'est des pâtes, des noix et… un petit truc checret."
    "Elle parle la bouche pleine, incapable de s'en empêcher."

    iris "Un petit truc secret. C'est précisément comme ça qu'on finit à l'infirmerie."

    elen "T'inquiète. Ch'est Goumi qui a validé."
    elen "Goumi ne tue pas ses clients. Enfin… pas volontairement."

    iris "…Ce n'est pas rassurant."

    think "Elen mélange, goûte, et ses yeux s'illuminent comme deux petites diffusions à elle toute seule."

    elen "Oh ! Ch'est trooop bon ! Exactement trop bon !"

    iris "Tu essaies de nous convaincre, ou de survivre à la première bouchée ?"

    elen "J'ai le droit d'être heureuse, non ? Tu devrais essayer, tiens."

    iris "Ça me fatigue rien que de te regarder."

    think "Mon plateau se limite à une barre et un jus. La nausée occupe le reste de la place."

    scene bg_cg013_1 at adaptive_fullscreen with fade
    think "Elen compose alors un regard très particulier. Grands yeux, lèvre tremblante."

    elen "Le regard ultiiime ! C'est comme ça que j'ai eu le bol."

    iris "Le regard du caprice, oui."

    elen "Le regard du caprice, c'est mignon ! Je me suis bien entraînée, t'as vu ?"

    scene bg_cg013 at adaptive_fullscreen with fade
    pause 0.3

    iris inquiet "…T'as pas peur ? Deux secondes ?"

    elen triste "Si. Mais là, maintenant, tout de suite, j'ai faim."
    elen joie "Alors je m'autorise à oublier la peur. Juste pour un bol."

    iris surpris "…"

    elen taquin "T'as envie de me faire la morale, hein ?"

    iris triste "Un peu."

    elen taquin "Vas-y. Balance ton sermon, je t'écoute."

    iris fatigue "Non. Laisse tomber."

    think "Une chaise racle derrière nous. Personne ne regarde. On a appris à ne plus se retourner."

    # On quitte le CG (où les persos sont déjà dessinés) et on regroupe TOUS les
    # locuteurs présents dans un seul showGroup, complété à chaque nouvelle arrivée.
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_160
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elen", "joie"),
        ("iris", "taquin"),
        ("elias", "neutre"),
    ])

    elias sourire "Wesh. Vous mangez quoi ?"

    elen joie "Le bonheur."

    iris taquin "Ne la crois surtout pas."

    elias inquiet "…Faut manger correctement. Surtout aujourd'hui."

    elen taquin "Oh non. Iris me faisait déjà la morale. Pas besoin de rab."

    elias colere "Je plaisante pas."

    iris taquin "Il plaisante jamais. Ça, c'est vrai."

    elias sourire "Protéines. Œufs. Poulet. Simple, efficace."

    think "Elen le regarde comme s'il venait de recommander de l'eau tiède pour le plaisir."

    elen triste "Tu veux manger du poulet ? Ici, le seul endroit où on peut demander tout ce qu'on veut ?"

    elias reflechit "C'est une base. Ça tient au corps. Ton truc, là… c'est chaud d'appeler ça un repas."

    iris taquin "Merci. Elle a clairement un palais de doberman."

    elen colere "Oh ! C'est pas des pâtes aux noix. C'est une œuvre d'art gustative."

    elias peur "Franchement, j'en doute."
    elias reflechit "Cet aprèm, faut être lucides. On peut pas débarquer là-bas tout mous."

    iris triste "…"

    elen colere "On devait pas en parler. Pas pendant le repas."

    elias reflechit "Personne veut en parler. C'est pour ça que ça tourne dans toutes les têtes."

    iris colere "On n'est pas obligés. Là. Maintenant. On mange."

    elias triste "On fait quoi, alors ? On arrive et on improvise ? C'est chaud comme plan."

    elen sourire "Bon. Puisque vous me cassez l'appétit avec ça…"

    think "Elen bondit presque de sa chaise."

    # Mise en avant d'Elen : elle se lève et s'avance (recentrage + pop de zoom).
    show elen joie at day3_vote_pop zorder 60
    elen joie "Moi, je vote pour."

    pause 0.4

    think "Elle l'annonce comme un dessert de mariage. Pas l'ombre d'une hésitation sur son visage."

    # Elen se rassoit : on restaure le groupe attablé.
    $ showGroup([
        ("elen", "joie"),
        ("iris", "reflechit"),
        ("elias", "sourire"),
    ])

    iris reflechit "Tu le dis si facilement."

    elen taquin "Parce que c'est facile. Ici, on crève d'ennui. Dehors, ils crèvent pour de vrai."
    elen inquiet "…Pardon. C'est pas drôle. Mais vous avez compris. Si on peut changer ça, on change ça, et puis c'est tout."

    iris reflechit "…"

    elias sourire "Tu marques un point."

    think "Julian s'approche, attiré par le mot « vote » comme par un projecteur."
    $ showGroup([
        ("elen", "joie"),
        ("iris", "hesitation"),
        ("elias", "neutre"),
        ("julian", "neutre"),
    ])

    julian "J'ai entendu « je vote pour » ?"

    elen rire "Oui. Bienvenue au club."

    julian sourire "Évidemment. JE vote pour. Toujours du côté de ma secrétaire préférée."

    iris hesitation "Julian…"

    julian reflechit "Quoi ? Je ne vais pas cacher une position aussi évidente. On a tous besoin de clarté."

    think "La moitié de la salle regarde vers nous. Elen fédère, même par accident."

    elen taquin "Bon, puisqu'il faut y aller : question simple. Qui vote pour ?"

    think "Julian lève la main comme si une caméra attendait précisément ce plan."

    julian rire "Pour. Évidemment."

    think "Tout le monde se tourne vers moi."

    noam reflechit "Tu votes pour… sans aucune hésitation ?"

    elen colere "Nooon, faut voir le bon côté !"

    iris fatigue "Une seule voix contre suffit à tout faire capoter. L'enthousiasme n'est pas une stratégie de vote."

    elias "Pour. Mais faut que ça soit vraiment appliqué. Sinon on vote pour du vent, et ça, c'est chaud."

    think "Kael tente de passer avec son plateau. Elen lui barre la route en souriant."

    $ showGroup([
        ("elen", "joie"),
        ("iris", "fatigue"),
        ("elias", "neutre"),
        ("julian", "neutre"),
        ("kael", "neutre"),
    ])

    pause 0.4

    elen joie "Kael ? Pour ou contre ?"

    kael "…Je ne sais pas. Je déciderai au moment de voter."

    elen "Ok. Au moins, c'est honnête."

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

    mara reflechit "On vous entend de loin. Annoncer vos votes devant les caméras, c'est audacieux."
    mara taquin "Ou généreux. Vous facilitez le travail de tout le monde."

    elen joie "Oh non. On est démasqués."

    iris reflechit "Alors ? Tu t'es décidée ? Tu votes contre ?"

    mara taquin "J'ai pas dit ça."
    mara reflechit "Je comprends l'idée. Mais on ouvre une porte sans voir ce qu'il y a derrière."

    elen colere "C'est du commerce. C'est pas comme si on proposait d'éradiquer les bébés pingouins."

    mara doute "T'en es vraiment sûre ?"

    mara colere "Non, laisse. Je dramatise pas. Je demande juste ce qu'on n'a pas compris."
    mara colere "Où est le texte exact ? Je veux le voir avant de voter quoi que ce soit."

    elen reflechit "Ok. Je t'entends. Vraiment. Mais… on fait quoi, sinon ?"
    elen colere "On regarde les gens crever en se disant que c'est pas notre faute ?"

    mara triste "Je dis pas ça."
    mara peur "Je dis juste que si ça tourne mal, c'est nous qui payons. Pas Kami. Nous."

    noam reflechit "Tu veux des garanties. Ne pas signer les yeux fermés."

    mara reflechit "Voilà. Et tout dépendra de l'énoncé précis. Un mot en trop, et une bonne idée devient une condamnation."

    call day3_collect_vote_argument("enonce_precis") from _call_day3_collect_vote_argument_enonce_precis

    pause 0.3

    think "Elle a raison. Et c'est exactement ce détail que je n'arrive pas à me sortir de la tête."

    think "Elen pousse son bol vide avec la fierté d'une mission accomplie."

    elen content "Bon. Je vais digérer mon œuvre."
    elen taquin "Et peut-être convertir quelques âmes à ma bonne humeur en chemin."

    iris "Bonne chance."

    elen rire "Merci. Je suis née pour ça."

    hide elen with moveoutleft

    pause 0.4

    $ hideGroup()
    "Peu à peu, la cafétéria se vide. Bientôt, il ne reste qu'Iris et moi."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("iris", "neutre", 0.60),
    ])

    iris fatigue "Tu vois. Même quand personne veut en parler…"
    iris fatigue "…on finit toujours par le faire."

    "Puis elle sort à son tour."
    hide iris with moveoutleft

    think "Je repose mon plateau. Trois heures avant de savoir si on est un groupe, ou juste douze inconnus qui vont se déchirer en direct."

    stop music fadeout 0.8

    "Que faire en attendant ?"

    call START_FREE_TIME("_3_PAUSE_CHAMBRE") from _call_START_FREE_TIME_3_1


label _3_PAUSE_CHAMBRE:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_161
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

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

    nyra stress "Julian fait le tour des indécis. Un par un."

    noam "Attends. Qu'est-ce qu'il fait, exactement ?"

    nyra colere "Il est allé voir Tomas, puis deux autres. Il ne défend plus le texte."
    nyra triste "Il se vend, lui. Et le pire, c'est que ça va braquer les gens au lieu de les convaincre."

    noam "Il est où ?"

    nyra "Dans la salle de repos. Encore."

    stop music fadeout 0.5
    play music "music/bgm_tension_low.mp3" fadein 0.6

    # Effet de course : le décor tremble tant qu'on court (secousse day3_run_shake).
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_163
    scene couloir_dortoir at adaptive_fullscreen, day3_run_shake with fade

    think "On se met à courir. La salle de repos n'est pas loin, par chance."

    play sound sfx_run

    think "Mes semelles claquent sur le métal. Nyra file devant sans se retourner."
    "Les néons défilent. Les caméras pivotent avec nous, patientes."
    think "Encore un joli spectacle qu'on offre au monde entier."

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
    think "Je l'entends rire derrière la porte. Ce rire trop rond, trop travaillé."

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_165
    scene bg_repos at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("nyra", "neutre", 0.25),
        ("julian", "neutre", 0.55),
        ("tomas", "neutre", 0.85),
    ])

    if day3_corridor_success >= 2:
        think "On est arrivés vite. Julian vient à peine de commencer son numéro."

        julian sourire "—et si JE prends la parole en premier, on y arrivera plus vite."
        julian sourire "Il faut un cap. Quelqu'un en qui les gens se reconnaissent."

        tomas hesitation "N-Ne compte pas sur… j-je…"

        think "Tomas hésite encore, mais il tient debout. On est arrivés à temps."
    else:
        think "On a traîné. À voir la tête de Tomas, Julian le travaille au corps depuis un moment."

        julian rire "…et voilà pourquoi c'est TOI qu'il faut, Tomas. Répète-le : « je soutiens le porteur du vote »."

        tomas peur "J-Je… oui… enfin, si tu crois que c'est mieux…"

        julian sourire "Évidemment que c'est mieux. Tu vois ? On se comprend."

        think "Il l'a essoré. Tomas n'ose même plus finir ses phrases. J'aurais dû courir plus vite."

    julian rire "Allez, Tomas. Tu veux que ça change, non ? Écoute-moi. Le monde a besoin de toi."

    tomas inquiet "O-Ouais, sans doute…"

    think "Il l'enveloppe comme un vendeur. Tomas se ratatine à chaque phrase. Je m'avance."

    call day3_julian_clash_minigame from _call_day3_julian_clash_minigame

    noam determine "Personne ici n'a de mandat pour se poser en chef."

    julian sourire "Ah. Noam. Il fallait bien que tu débarques."

    noam hesitation "Que tu veuilles que le vote passe, je le comprends."
    noam "Mais si tu te mets trop en avant, les hésitants vont voir autre chose que le texte."
    noam reflexion "On lit clair dans ton jeu, Julian. Tu veux briller."
    noam raison "Résultat : le vote ne portera plus sur la proposition. Il portera sur toi."
    noam colere "Et une chose est sûre : toi, tu ne fais pas l'unanimité."

    julian sourire "Tu te réveilles, aujourd'hui ? On ne t'entendait pas depuis le premier jour."
    julian taquin "Et là, tu viens faire le malin ?"
    julian "JE veux que ce texte passe. Alors laisse-moi convaincre les autres."

    noam "Parle du texte. Rien d'autre. Ta personne, ta gloire, tout le monde s'en contrefiche."

    tomas "I-Il a raison. Enfin… je veux dire…"
    tomas "Si ça ressemble à une démonstration d'ego, f-franchement… ce sera sans moi."

    julian triste "Bon. Très bien. On verra au Conclave qui porte réellement ce vote."
    julian "Évite juste de me transformer en méchant de l'histoire. Je me bouge pour le collectif, moi. C'est déjà plus que la plupart."

    hide julian with moveoutleft

    stop music fadeout 0.6
    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    tomas mefiant "…D-Désolé. À cause de moi, vous avez dû venir."

    nyra "Non. Il fallait remettre les points sur les i de toute façon."

    tomas "P-Pour être honnête… je ne veux pas que ce soit lui qui donne le ton."
    tomas "Il faut que quelqu'un puisse lui tenir tête. T-Tu vas parler, tout à l'heure ?"

    noam "Oui. Mais pas pour briller. Pour que ça avance dans le bon sens."

    tomas hoche_la_tete "Alors ça a une chance de passer."

    nyra sourire "Allez, viens, Tomas. Tu as bien mérité une pause."
    nyra "Merci, Noam."

    think "Ils repartent ensemble. Tomas marche un peu plus droit qu'à l'aller."
    hide tomas with moveoutleft
    hide nyra with moveoutleft

    think "Ce vote, ce n'est pas juste un texte. C'est une question de confiance."
    think "Julian n'est pas un ennemi. Mais son besoin d'exister peut causer le pire comme le meilleur."
    think "Je serre les poings. Ils tremblent moins qu'avant."
    think "Les grands discours, c'est pas pour moi. Mais je ne peux pas laisser ça déraper."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite


label _3_TRANSITION_CONCLAVE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_166
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Bientôt l'heure. Le couloir paraît plus étroit, moins amical, comme s'il se resserrait sur nous."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    think "Respire, Noam. C'est juste un vote."
    think "Alors pourquoi mon cœur cogne comme ça ?"
    think "Une sueur froide glisse dans ma nuque. J'ai l'impression d'être observé plus que d'habitude."
    think "Les caméras, évidemment. Pourquoi auraient-elles disparu aujourd'hui, justement ?"

    think "Le groupe converge peu à peu vers le Conclave, tout le monde partageant le même silence épais."

    $ showGroup([
        ("lysa", "neutre", 0.25),
        ("noam", "neutre", 0.50),
    ])

    "Lysa marche en retrait. Juste assez pour que ça se remarque."
    "Le groupe accélère quand le couloir se resserre. Elle, non. Elle traîne les pieds, exprès."

    lysa triste "On va voter. On va échouer."
    lysa triste "Puis demain on se réveillera ici, mêmes murs, même pression. Et dans trois jours, on recommencera."
    lysa blase "Et on échouera encore. On ne change pas un monde à douze marionnettes."

    think "Elle ne me parle pas vraiment. Elle récite une conclusion qu'elle a déjà tranchée toute seule."

    noam reflechit "Il n'y a que ceux qui ne tentent rien qui n'ont jamais rien."
    noam sourire "On avance, et ce qui arrivera arrivera. C'est déjà ça de moins à regretter."

    "Lysa fait une moue déconfite alors qu'on approche de la porte du Conclave."

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    think "Sael s'est laissée glisser à l'arrière du groupe, elle aussi. Volontairement. Elle observe Lysa depuis un moment."
    "Sans prévenir, sans théâtre, elle attrape Lysa et la serre contre elle."

    sael "Je te regarde depuis hier. Tu portes tout ce que les autres refusent de voir. C'est lourd."
    sael "Ma grand-mère disait que même les morts se reposent avant de revenir dans nos rêves."
    sael "On a besoin de ta lucidité. Pas d'une autre Lysa. De celle qui est là, maintenant."

    "Elle pointe la poitrine de Lysa du doigt. Les épaules de Lysa se relâchent, à peine."

    lysa "Tu dramatises. Je suis toujours là."

    sael "Alors montre-le. Montre-nous la battante qui se cache là-dedans."
    sael "Tu vois des failles qu'on ne voit pas. C'est pénible. Mais aujourd'hui, ça peut nous sauver."

    lysa "…Si je sauve le débat, tu me dois un café. Les oracles se faisaient mieux payer, pourtant."

    sael sourire "Je t'en offre deux. Ici, personne ne paie rien. Peut-être un signe que ton monde d'avant n'était pas si parfait."

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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_168
    scene bg_conclave at adaptive_fullscreen with fade
    pause 0.4

    "Les portes se referment. Un déclic net résonne derrière nous."

    play sound sfx_door

    think "…C'était un verrou ? Ils nous ont enfermés."
    think "Pas de sortie tant qu'il n'y a pas de décision. Kami veut un vote, ou un cadavre. Pas d'entre-deux."

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
    nyra "Traduire. Ou réécrire ?"
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Réécrire est un vilain mot. Disons que j'ai rendu vos intentions… exécutables."
    kami "Le texte est là. Compilé, dense, juridique. Exactement comme les lois que vous adoriez ignorer avant moi."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "À vous de le remettre en ordre et de le lire. Vraiment le lire."
    kami "Le diable se cache dans les détails. Moi, je me contente de l'y ranger."

    hide screen kami_broadcast_ui

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_169
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

    ryn colere "Un texte juridique compilé ?! On voulait juste autoriser le commerce !"

    tomas hesitation "C'est… c'est exactement là qu'il faut se méfier. Un texte de loi, c'est jamais neutre."
    tomas raison "Chaque mot ajouté peut changer tout le sens. Faut le reconstruire proprement avant d'en juger."

    nyra "On fait ça vite et bien. Cherchez la ponctuation et les majuscules, ça situe les fragments."
    nyra "Chacun prend un morceau. Personne ne conclut avant qu'on ait la phrase entière."

    noam "D'accord. On assemble, on lit, ensuite on discute."
    noam "Et on garde les yeux ouverts sur ce qu'elle a pu glisser dedans."

    # Wrapper complet : intro animée, tutoriel 1ère fois, retry avec malus, résultats avec rang
    call debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY") from _call_debat_phase1_run

    $ phase1_ok = debat_phase1_last_result.get("success", False)
    $ phase1_time_left = debat_phase1_last_result.get("time_left", 0)
    $ phase1_kamyz_gain = debat_phase1_last_result.get("kamyz", 0)
    if phase1_ok:
        $ player_kamyz += phase1_kamyz_gain
        $ renpy.notify("+ %d Kamyz" % phase1_kamyz_gain)
        call screen noam_consent_screen

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_170
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

    lysa "« Autoriser le transport, la vente et l'échange de marchandises. »"
    lysa colere "« En conséquence, le système de distribution de denrées est aboli. »"

    elen surpris "Attendez… « aboli » ? C'était pas dans l'idée de départ, ça !"

    tomas "M-Maintenant, le vrai débat peut commencer. Et il est plus grave qu'on croyait."

    jump _3_DEBAT1_PHASE2

# ============================================================================
# DÉBAT — PHASE 2 : le clash + CLIFFHANGER 1
# ============================================================================

label _3_DEBAT1_PHASE2:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_171
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

    mara surpris "Donc voilà le piège. Autoriser le commerce, ça supprime les rations. En un seul texte."

    noam "Du calme. On sait tous que ce n'est pas ce qui avait été proposé au départ."
    noam "C'est l'habillage qu'en a fait Kami. La question, c'est : est-ce qu'on peut vivre avec ?"

    nyra reflechit "Si on vote ce texte, demain il n'y a plus une seule distribution gratuite. Nulle part."

    kael inquiet "Supprimer les rations… ça change tout."

    ryn colere "Ça supprime la seule sécurité qu'on avait ! À Limen, c'est ce qui tient les gens en vie."

    lysa reflechit "Et pourtant, c'est logique."

    noam "…Comment ça ?"

    lysa blase "On disait hier : rétablir le commerce, c'est rétablir la monnaie."
    lysa reflechit "Pour gagner de la monnaie, il faut travailler. Et pour pousser les gens à travailler…"
    lysa blase "…on arrête de leur donner de quoi vivre gratuitement. Kami n'a rien inventé. Elle a juste écrit tout haut ce qu'on pensait tout bas."

    nyra reflechit "Sauf que supprimer une structure mondiale, ça ne se décide pas sur un coup de tête."

    sael triste "Les morts de Limen n'ont pas besoin d'un nouveau responsable."
    sael reflechit "Kami. Dis-nous seulement une chose : ce texte vient-il vraiment de l'un de nous ?"

    think "Les regards se croisent. L'écran central reste figé. Kami ne répond pas."
    think "Le silence dure trop longtemps pour être innocent."

    lysa blase "Elle ne répondra pas. Dix votes pour douze textes, le tour de passe-passe est parfait."
    lysa colere "Elle peut ajouter, couper, tordre ce qu'elle veut. On ne le saura jamais."

    ryn reflechit "Attends… tu dis quoi, là ?"

    lysa salut "Que peut-être aucun de ces textes n'est de nous. Que la manipulation est invérifiable. Bienvenue."

    noam "Manipulation ou pas, il faudra voter. Alors autant décider en connaissance de cause."
    noam reflexion "Concentrons-nous sur ce qu'on peut vérifier : ce que ce texte fait, concrètement, à chacun de nos districts."

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
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_172
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_low.mp3" fadein 0.6

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("ryn", "colere", 0.62),
    ])

    ryn colere "On tourne en rond depuis une heure ! Pendant qu'on parle, eux, ils attendent."

    think "Il a raison. Et Kami adore avoir raison à notre place."

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
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_173
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

    noam reflexion "Elle nous montre le prix de l'attente. Pas celui de l'erreur. Ne la laissons pas choisir pour nous."
    noam "On garde la tête froide. On finit ce qu'on a commencé, mais on le finit lucides."

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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_174
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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_175
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

    noam "Bon. On a le vrai texte, on a le chiffre de Kami. Il nous reste à décider avec la tête, pas avec la peur."

    julian "La tête ? On est en train de crever à petit feu, Noam."
    julian "Le statu quo, c'est une tombe collective avec des bons de pain rassi. Tu appelles ça la sécurité ?"

    ryn colere "Et ton grand soir, c'est quoi ? On sacrifie Limen pour que Nexus se paie du luxe ?"

    julian surpris "Nexus ? Je te rappelle que j'en viens, de Nexus. Et je ne roule pas sur l'or, figure-toi."

    ryn "…Ouais. Bref. Ça change rien au fond !"

    mara colere "Ryn. Respire. On avance mieux sans hurler."

    elen joie "Mais c'est ça qui est beau ! Choisir ce qu'on mange sans demander la permission !"

    # (combinaison « lysa raison » ajoutée dans images.rpy)
    lysa raison "Pour choisir, il faut de l'argent, Elen. Midas transformait tout en or, et il est quand même mort de faim."

    tomas "Euh… il faut dire que la production mondiale s'est effondrée depuis Kami."
    tomas "On fabrique presque quatre fois moins qu'avant. C'est… c'est pas rien."

    nyra "Rien d'étonnant. Sans récompense, personne ne se donne la peine de produire."

    # Cadrage de Kami : moins clownesque, plus prédatrice.
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "Voilà. Enfin une vraie question sous le vernis."
    kami "Je vous rappelle que ce texte est né de VOTRE imagination. Ne me regardez pas comme la coupable."
    kami "Continuez. Vous êtes bien plus intéressants quand vous avez peur."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], phase=3, prompt="Moment 1 — Cadrer la première salve.")
    if p3_pick is None:
        $ p3_pick = 0
    call _3_DEBAT1_PHASE3_INT1 from _call__3_DEBAT1_PHASE3_INT1

    stop music fadeout 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_176
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    elias "Le vrai problème, c'est qu'on évite la vraie question. Le système actuel, il marche pas. Point."

    sael "…Vous dépendez trop de ce système."
    sael colere "Les gens ne veulent plus travailler, plus faire d'effort, mais ils veulent être libres."
    sael colere "Il va falloir choisir. Entre la liberté et la sécurité. On ne peut pas garder les deux entières."

    lysa blase "Même en votant pour, il reste un trou béant dans le texte."
    lysa reflechit "Avec quoi les gens gagnent leur premier argent ? Si personne n'a rien, personne ne peut rien acheter à personne."

    noam "Elle a raison. C'est le point noir de toute la proposition."
    noam "Kami. Tu peux nous éclairer, ou tu comptes rester muette encore une heure ?"

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh. Une question pratique ? On progresse."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Si ce texte passe, j'ouvrirai des contrats de travail rémunérés. Des tâches assignées, des objectifs, un salaire à la clé."
    kami "Vous fabriquez, vous récoltez, vous livrez. Vous êtes payés. Simple."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Libre à vous de travailler. Ou pas. Mais ne comptez plus sur la générosité des rations."
    kami "La faim est une motivation remarquablement efficace. Je l'ai observé sur vous mille fois."

    hide screen kami_broadcast_ui
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_177
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

    lysa reflechit "Un système de contrats. C'est… viable. Au moins pour amorcer l'économie."

    nyra reflechit "Et avec le commerce, des structures plus grosses finiront par émerger. Des entreprises. Un vrai tissu."

    ryn reflechit "Ouais, sur le papier. Mais qui décide des contrats ? Elle. Toujours elle."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], phase=3, prompt="Moment 2 — Désamorcer ou accélérer la fracture.")
    if p3_pick is None:
        $ p3_pick = 0
    call _3_DEBAT1_PHASE3_INT2 from _call__3_DEBAT1_PHASE3_INT2

    stop music fadeout 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_178
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 1.0

    noam "Bon. Je crois qu'on a fait le tour."
    noam "Le monde d'avant, le texte brut, les trocs qui existent déjà, les contrats de Kami…"
    noam "On sait tout ce qu'on peut savoir. Le reste, c'est un pari."

    # ── CLIFFHANGER 2 : le dernier indécis, avant le vote ──
    think "Je regarde autour de la table. Les visages se sont figés. Chacun a choisi. Ou presque."
    think "Presque."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_179
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "reflechit", 0.32),
        ("kael", "inquiet", 0.68),
    ])

    noam "Il ne manque plus que… vous deux. Ceux de qui tout dépend."

    ryn triste "…Moi, je sais. Que je le veuille ou non. Limen, c'est écrit là. Alors je porterai mon choix."

    think "Reste Kael. Celui qui déciderait « au moment de voter ». Le moment, c'est maintenant."

    kael inquiet "Je…"

    kael triste "Sur Orbite, une erreur ne pardonne pas. Et là, je n'arrive pas à voir si on ouvre une porte…"
    kael peur "…ou si on retire le dernier filet sous nos pieds."

    noam "Kael. Regarde-moi. Pour ou contre ?"

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
    $ selected = p3_round_options[0][p3_pick]["title"]

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_180
    scene bg_conclave at adaptive_fullscreen with dissolve

    if "appro" in selected.lower() or "inégal" in selected.lower():

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

        noam "Même avec les bons, les rayons sont vides. On distribue des droits sur des étagères qui n'existent pas."

        elias determine "Ça, c'est la vérité vraie. Un bon pour du riz, et pas de riz au bout. On appelle ça la sécurité ?"

        julian sourire "Le commerce remplit les rayons. Un producteur qui peut vendre produit davantage. C'est mécanique."

        mara doute "Ou alors les rayons se remplissent là où il y a de l'argent. Et Limen regarde par la fenêtre."

        ryn colere "Voilà ! Nexus déborde, nous on ramasse les miettes. Comme aujourd'hui, mais en pire."

        kael reflechit "…Sauf que Limen est le plus peuplé. La demande y sera énorme. Un marché suit la demande, non ?"

        ryn reflechit "…Mouais. Peut-être. Si on a de quoi payer, déjà."

        sael neutre "Chez nous, on fabrique ce qu'il nous faut. Le manque, on le connaît. On lui survit."

        elen joie "Et avec les échanges, on n'aura plus à seulement survivre. On pourra vivre !"

        # Montre que le système actuel ne nourrit pas : pousse doucement les hésitants.
        $ debat_day3_apply_influence({"ryn": 1, "kael": 1, "mara": -1, "julian": 1, "elen": 1})

    elif "ration" in selected.lower() or "choix" in selected.lower():

        $ showGroup([
            ("tomas", "raison", 0.05),
            ("iris", "colere", 0.23),
            ("ryn", "colere", 0.41),
            ("mara", "reflexion", 0.59),
            ("elias", "determine", 0.77),
            ("elen", "joie", 0.95),
        ])

        noam "On répète que les bons donnent droit à tout. En vrai, ils donnent droit à quoi ?"

        tomas raison "Euh… 62 %% des références listées sont en rupture permanente en périphérie. C'est… c'est pas rien."

        iris colere "Un bon, c'est un ticket pour faire la queue. Point. Le produit correct part en deux jours."

        ryn colere "À Limen, on a des bons pour du lait qui arrive caillé. Des médocs périmés avant même la livraison."
        ryn triste "Ça, c'est votre « sécurité » ? Un papier qui promet ce qui n'arrive jamais ?"

        mara reflexion "…D'accord. Là, tu marques un point. Défendre ce système-là, c'est défendre du vide."

        elias determine "Le même ticket pour rien, qu'on se crève au boulot ou qu'on dorme toute la journée. Faut que ça change."

        elen joie "Plus de fournisseurs, plus de concurrence, plus de choix. On mérite mieux qu'un ticket vide !"

        # L'argument le plus efficace pour rallier les pauvres (Ryn) : preuve vécue.
        $ debat_day3_apply_influence({"ryn": 2, "mara": 1, "kael": 1, "tomas": 1, "iris": 1})

    elif "orbite" in selected.lower() or "dépress" in selected.lower():

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

        kael mefiant "Un écart de flux. Un module dépressurisé. Là-haut, une erreur logistique, ça tue en silence."
        kael triste "On ne peut pas se permettre l'imprévu. Jamais."

        noam "Et le commerce, c'est de l'imprévu par définition."

        iris inquiet "…Ok. Là, même moi je tique. On met des vies en balance contre des étals mieux garnis ?"

        tomas raison "P-Paradoxalement, c'est sur Orbite qu'il y a le moins de morts par an. Le carcan actuel les protège."

        julian hesitation "On n'interdit rien de plus, pourtant… Enfin. Je vois l'idée. Mais je vois aussi le vide sous nos pieds."

        lysa blase "Un grain de sable dans un système sous pression, et tout saute. Kael et Nyra le savent mieux que nous."

        nyra stress "Sur Orbite, la perte de contrôle se paie dans la seconde. Pas au prochain vote."

        mara stress "…Super. Donc en votant pour, on joue avec la vie de gens qu'on ne verra jamais."

        think "Nyra et Kael échangent un regard bref, tendu. Personne n'insiste."

        # Argument « danger » : refroidit fortement les hésitants (surtout Kael).
        $ debat_day3_apply_influence({"kael": -2, "nyra": -1, "mara": -1, "ryn": -1, "julian": -1, "lysa": -1})

    return

label _3_DEBAT1_PHASE3_INT2:
    $ selected = p3_round_options[1][p3_pick]["title"]

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_181
    scene bg_conclave at adaptive_fullscreen with dissolve

    if "avant" in selected.lower():

        $ showGroup([
            ("iris", "reflechit", 0.05),
            ("elen", "joie", 0.23),
            ("julian", "sourire", 0.41),
            ("mara", "reflexion", 0.59),
            ("tomas", "raison", 0.77),
            ("ryn", "colere", 0.95),
        ])

        iris reflechit "Le monde d'avant… vous en parlez comme d'un paradis perdu. Moi, je me souviens des files et des prix qui doublaient sans raison."
        iris reflechit "…Mais au moins, ça bougeait. On pouvait râler ET agir. Aujourd'hui, on ne fait plus que râler."

        elen joie "Voilà ! Tu bossais, tu achetais. Personne pour juger si tes chaussures étaient assez trouées."

        julian sourire "Ce monde n'était pas parfait. Il était vivant. Je préfère le mouvement à une égalité dans l'attente."

        mara reflexion "« Choisir »… c'est un joli mot, Elen."
        mara reflexion "Moi, je me souviens surtout des sourires obligatoires. Des portes qui se ferment si tu n'es pas… parfaite."
        mara triste "La liberté d'avant, certains l'ont payée très cher. J'en fais partie."

        tomas raison "Faut dire… ce qui pourrissait tout, avant, c'était la guerre. Elle est interdite maintenant. Techniquement, ça pourrait mieux tourner."

        ryn colere "« Techniquement ». Dis ça aux gamins de Limen qui bouffaient les restes des riches."

        noam "Le monde d'avant offrait la liberté à ceux qui avaient déjà les moyens. Aux autres, la loi de la jungle."

        elen joie "Alors gardons le meilleur ! L'essentiel pour tous, la liberté pour le reste. Comme avant, mais sans la guerre !"

        think "Mara détourne le regard, comme si elle regrettait déjà d'avoir livré quelque chose de vrai."

        # Galvanise les convaincus, mais réveille les blessures de Mara et l'amertume de Ryn.
        $ debat_day3_apply_influence({"julian": 1, "elen": 1, "iris": 1, "mara": -1, "ryn": -1})

    elif "énoncé" in selected.lower():

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

        noam "Le texte est binaire. Pour : suppression totale, tout de suite. Contre : rien ne change. Aucun entre-deux."

        kael triste "Aucune transition. On saute sans corde. Sur Orbite, ça, c'est un arrêt de mort."

        lysa blase "« Suppression » veut dire suppression. Pas « réduction ». Icare aussi croyait pouvoir négocier avec la gravité."

        ryn colere "Sans bons, à Limen, on meurt en silence pendant que vous « produisez » vos rêves."
        ryn colere "Le texte condamne les faibles. C'est écrit noir sur blanc !"

        mara stress "…Et il l'écrit noir sur blanc. On ne pourra pas dire qu'on ne savait pas."

        sael determine "Les Limenois échangent déjà pour survivre. Ce texte ne les condamne pas. Il les libère du mensonge."

        think "Ryn frappe du poing. Sael ne cille pas."

        # Brutalité du texte : durcit les hésitants (Ryn surtout), galvanise Sael et Elias.
        $ debat_day3_apply_influence({"ryn": -2, "kael": -1, "mara": -1, "elias": 1, "sael": 2})

    elif "échange" in selected.lower() or "discret" in selected.lower():

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

        noam "Ça marche en petit. Mais à grande échelle, officiel : est-ce que ça reste sous contrôle ?"

        kael doute "…Si ça existe déjà sans provoquer le chaos, alors peut-être que sur Orbite aussi, ça pourrait tenir."

        julian sourire "Exactement ! Les gens s'organisent déjà. Supprimer les bons, c'est cesser de nier ce qu'ils font en cachette."

        lysa blase "S'organiser… ou couronner des petits rois. Les marchés noirs finissent toujours par sacrer quelqu'un."

        ryn reflechit "…Mais si c'est déjà là, et que ça sauve des familles… alors on pourrait faire pareil. En mieux. Sans crever en attendant Kami."

        mara reflexion "Tiens. Pour une fois, un plan qui ne sort pas de nulle part. Ça existe, ça marche. C'est déjà ça."

        sael determine "On survit déjà. On peut faire plus que survivre."

        think "Ryn baisse les yeux. Kael recalcule. Le troc existe déjà — l'idée trouve enfin une prise."

        # Rassure les hésitants avec une preuve concrète : le levier de l'unanimité.
        $ debat_day3_apply_influence({"ryn": 2, "kael": 2, "mara": 1, "sael": 1, "julian": 1})

    return

# ============================================================================
# ISSUES DU VOTE
# ============================================================================

label _3_VOTE_POUR:

    $ current_period = "Soir"
    
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_182
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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_183
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    think "L'écran s'éteint. Aucun cri de joie. On n'a pas gagné. On a changé les règles, c'est tout."

    $ showGroup([
        ("julian", "sourire", 0.15),
        ("ryn", "jaloux", 0.38),
        ("elen", "joie", 0.61),
        ("mara", "rire_profond", 0.84),
    ])

    julian sourire "C'est fait. Le collectif vient de créer une chance réelle."

    ryn jaloux "Ouais."
    ryn inquiet "Mais sans les bons, Limen va morfler au début. Faut pas se mentir."

    noam "Je me demande si on savait vraiment ce qu'on faisait."
    noam "On ne pouvait plus rester comme avant. Mais… est-ce que c'était vraiment un choix ?"

    mara rire_profond "Génial. On va enfin pouvoir acheter des trucs."
    mara taquin "Et crever avec le choix de la sauce. Le luxe."

    $ showGroup([
        ("elen", "joie", 0.30),
        ("kael", "mefiant", 0.70),
    ])

    kael mefiant "Orbite tiendra. Si les protocoles de sécurité restent intacts."
    kael triste "Si."

    think "Julian souriait trop fort. Elen rayonne et tremble. Ryn fixe le sol. Kael compte ses respirations."
    think "Personne n'exulte. Le plus dur commence maintenant."

    $ hideGroup()

    think "Dix-sept heures dix. On se lève en silence."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_184
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent jusqu'à ma chambre."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_185
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "On a voté pour le changement. J'ignore encore si on est prêts à le vivre."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_186
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit. Demain sera différent. Pas forcément meilleur."

    $ phase3_over = True
    $ vote1 = "OUI"
    $ kami_grant_chapter_1_ending_reward("vote_oui")

    call show_chapter_title("Fin du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title

    pause 3.0
    jump patreon_ending

    #call end_day("4") from _call_end_day_3

    #jump _4_1_REVEIL_CHAMBRE

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

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_188
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    play music "music/bgm_low_tension.mp3" fadein 2.0
    think "L'écran s'éteint. Le rejet retombe sur nos épaules comme une couverture mouillée."

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

    nyra raison "Qui a voté contre n'a pas choisi l'inaction. Il a choisi le risque connu plutôt que l'inconnu."

    think "Les voix montent. Julian se lève et frappe la table. Sa performance vient de perdre son public."

    julian colere "Rationnel ?! Vous appelez ça rationnel ?"
    julian colere "Continuer à rationner des miettes pendant que les districts crèvent ? On a laissé filer la seule ouverture !"

    ryn colere "C'est le vote. C'est comme ça."
    ryn colere "Je le comprends. T'as vu ce que ça risquait pour Limen ?"

    julian colere "Et t'as vu ce que ça risque si on change rien ?!"

    ryn colere "Assieds-toi !"
    mara colere "Les riches survivront encore. Quelle surprise."
    noam "Attendez— un par un ! On ne va pas se déchirer devant le monde entier."

    think "Presque dix-sept heures. La journée est finie. Le vote aussi. Rien n'a changé."
    think "Et pourtant, quelque chose s'est brisé dans le groupe. Ça, ça ne se répare pas au vote suivant."

    think "Je me lève. Les voix continuent sans moi. Je veux juste rentrer et arrêter de réfléchir."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_189
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent dans les couloirs froids."
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_190
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_191
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Le silence est pire que les cris. On avait une chance. Une seule voix l'a refermée."
    think "Qu'est-ce qu'on peut faire, maintenant ?"

    $ phase3_over = True
    $ vote1 = "NON"
    $ kami_grant_chapter_1_ending_reward("vote_non")

    call show_chapter_title("Fin du chapitre 1", "Chapitre 1 — Le poids d’une voix") from _call_show_chapter_title_1

    pause 3.0
    #jump patreon_ending

    call end_day("4") from _call_end_day_24

    jump _4_0_REVEIL_CHAMBRE

# Total jour 3 : 17m
# Total J0-J3 : 1h25
