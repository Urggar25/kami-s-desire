init python:
    # Compatibilité chargement : d'anciennes sauvegardes peuvent désérialiser
    # une référence à store.build_arg pendant un reload Ren'Py.
    def build_arg(title):
        low = title.lower()

        if "ration" in low:
            icon = "⌬"
            desc = "Sécurité minimale contre la faim et le chaos."
        elif "orbite" in low:
            icon = "◉"
            desc = "Dépendance logistique et fragilité structurelle."
        elif "énoncé" in low or "precis" in low:
            icon = "⟡"
            desc = "Texte exact, conséquences juridiques immédiates."
        elif "appro" in low:
            icon = "⬢"
            desc = "Ruptures passées et files de pénurie."
        elif "échange" in low or "discret" in low:
            icon = "◌"
            desc = "Réseaux d'entraide clandestins déjà en place."
        elif "avant" in low:
            icon = "✦"
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

screen day3_codex_logo():
    if j2_vote_codex_unlocked:
        zorder 95
        imagebutton:
            idle "gui/common/codex_logo_idle.png"
            hover "gui/common/codex_logo_hover.png"
            selected_idle "gui/common/codex_logo_pressed.png"
            xpos 1814
            ypos 18
            action [SetVariable("j3_codex_dot", False), Show("day3_current_vote_codex")]
        if j3_codex_dot:
            add "gui/common/codex_notification_dot.png" xpos 1864 ypos 18

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
                            text "Autoriser le transport, la vente et l'échange de marchandises au sein des districts." size 22 color "#dff8ff"
                            text "Moment prévu : Jour 3, 14h00" size 19 color "#9ed8ff"
                        text "Résumé neutre" size 21 color "#70c6e8"
                        if vote_codex_j45:
                            text "Le texte promet une circulation plus libre des personnes entre districts. Ses effets restent incertains selon les frontières, la sécurité et les capacités d'accueil." size 20 color "#b8d8e4"
                        else:
                            text "Le texte promet une circulation plus libre des biens. Ses effets restent incertains selon les districts, les procédures et les risques locaux." size 20 color "#b8d8e4"
                        null height 8
                        text "Arguments découverts" size 24 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        for arg_id in ["approvisionnement", "rationnement", "orbite", "monde_avant", "enonce_precis"]:
                            if arg_id in j2_vote_arguments:
                                $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
                                frame:
                                    xfill True
                                    padding (12, 10)
                                    background Solid("#123044")
                                    vbox:
                                        spacing 3
                                        text "[arg['title']]" size 21 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text "[arg['summary']]" size 17 color "#b8d8e4"
                                        text "[arg['origin']]" size 15 color "#74a8ba"
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
                                        text "[col_label]" xalign 0.5 size 28 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
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
            text "Autoriser le transport, la vente et l'échange de marchandises." size 22 color "#dff8ff"
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
    call trace_qte_run(mg_id="trace_day3_wakeup", title="RÉVEIL — JOUR 3", path_type="curve_right", time_limit=7.0, wait_time=0.8, tolerance=60, max_errors=4, anchor_x=930, anchor_y=640, required=True)
    return True

label day3_play_corridor_trace:
    call trace_qte_run(mg_id="trace_day3_corridor", title="VIRAGE SERRÉ", path_type="arc", time_limit=5.0, wait_time=0.5, tolerance=58, max_errors=4, anchor_x=960, anchor_y=650, required=False)
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


label _3_CANON:

    $ day_id = 3
    $ current_day = 3
    $ day3_vote_bootstrap()

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.5

    think "Après une longue nuit, épuisante, je finis par ouvrir les yeux."

    scene bg_cg012 at adaptive_fullscreen with fade

    think "Je fixe le plafond blanc au dessus de moi."
    $ blink()
    
    think "Dans le couloir, les pas traînent déjà. Certains sont déjà reveillés. Personne ne court. Personne ne parle fort."
    $ blink()

    play sound sfx_announce
    pause 1.0

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Booooonjour mes petits représentants ♥"
    kami "Et bien, vous avez l'air motivés pour ce troisième jour !"
    kami "Je n'ai pas besoin de vous rappeler mais aujourd'hui est JOUR DE VOTE !"

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "J'espère que vous avez pu discuter entre vous ! Un petit non et Pfiou... C'est terminé !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'un d'entre vous se sera creusé les méninges pour rien !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Aaah ! Trop hâte de voir quelle sera votre décision !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à 14h ♥"

    pause 0.3

    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "Elle adore appuyer là où ça fait mal. Ne peut-elle pas arrêter de rappeler ces règles constamment ?"

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with fade

    call day3_play_wakeup_trace from _call_day3_play_wakeup_trace

    think "Mais il faut quand même que j'aille à la cafétéria."

    # Trajet jouable : chambre -> dortoir -> couloir -> cafétéria.
    # Kael et Julian peuvent être croisés, mais leurs dialogues restent optionnels.
    $ day3_cafeteria_route_kael_seen = False
    $ day3_cafeteria_route_julian_seen = False
    $ current_scene_active = "_3_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    $ room_scene_indices["chambre"] = 2
    jump CHAMBRE_TP


label _3_OPT_KAEL_DIAL:
    scene bg_dortoir at adaptive_fullscreen with dissolve
    $ day3_cafeteria_route_kael_seen = True

    think "Le couloir du dortoir est étrangement calme. Même la ventilation semble retenir son souffle."

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("kael", "fatigue", 0.65),
    ])

    kael fatigue "Oh, Noam."

    think "Sa voix est plus basse que d'habitude."

    noam "Tu vas à la cafétéria ?"

    kael reflechit "O-Ouais. Tu es sûr que c’est une bonne idée ?"

    noam "Le commerce ?"

    kael reflechit "Oui. Tout le monde minimise les effets."
    kael inquiet "Ils ne seront pas minimes."

    think "Il évite mon regard."

    noam "Tu penses que ça peut vraiment déraper ?"

    kael culpabilite "Je ne sais pas. Mais toucher aux règles de ce monde, ça me fait flipper."

    noam "Tu veux voter contre ?"

    kael surpris "Non. Je suis pour. En théorie. Disons que ça va dans la bonne direction."
    kael inquiet "Mais, t-tu n’as pas peur ?"

    noam "Si, je flippe grave. Mais on a pas le choix, quatorze heures va vite arriver..."
    noam "Vouloir que rien ne change, c’est aussi un choix."

    kael calme "On verra à 14h. Bonne chance."

    hide noam
    hide kael

    think "Je continue."

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

    julian joie "Alors Noam. Prêt à ouvrir la première brèche dans ce système ?"

    noam "On va essayer."

    julian rire "Essayer ? Non. Nous allons le faire."
    julian "Si JE monte scène, c'est pour annoncer que nous allons réussir !"

    think "Il attrape sa tasse. Le café déborde ; sa mise en scène, elle, reste intacte."

    julian reflexion "Si ce texte passe, nous ouvrons la première brèche depuis la prise de pouvoir de Kami."
    julian joie "Commerce. Échanges. Mouvement. L'Histoire s'en souviendra."

    noam "Et si ça ne passe pas ?"

    julian hesitation "Ça passera. Nous ferons en sorte que ça passe. Nous ne sommes pas ici pour maintenir le statu quo."
    julian idee "Les gens veulent un changement visible. Nous avons la responsabilité de l'incarner."

    noam "Tu es sûr que tout le monde suivra ?"

    julian hesitation "… Ils suivront. Certains ont simplement besoin que quelqu'un formule leur courage à leur place."
    julian reflexion "C'est le commerce. Personne ne votera contre une évidence pareille."
    julian sourire "Imagine : des ressources qui circulent, des districts qui échangent, des idées qui bougent."
    julian idee "Comme avant. Ce tableau ne te parle pas ?"

    noam "Je crois que... oui. Dit comme ça, sur le papier... Ouais, ça me plaît."

    julian reflexion "Le collectif a besoin d'un élan. À nous de le provoquer."
    julian sourire "À quatorze heures, nous changerons ce monde !"

    call day3_collect_vote_argument("monde_avant") from _call_day3_collect_vote_argument_monde_avant

    hide noam
    hide julian

    return

label _3_CAFETERIA_ARRIVE:
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    think "J'arrive à la cafétéria. Les discussions se font rares."
    think "Ryn murmure avec Elen. Mara fixe un écran mort. Iris tient une tasse pleine."
    think "Qui pourrait voter contre ? Mara ? Non. Sael ? Elle serait frontale. Moi ? Suis-je même moi même convaincu qu'il faudrait refaire comme avant ?"


    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "La cafétéria se remplit au fur et à mesure, mais le brouhaha se limite au bruit des fourchettes, des chaises et des respirations."

    $ showGroup([
        ("noam", "neutre", 0.82),
        ("elen", "joie", 0.22),
        ("iris", "fatigue", 0.50),
    ])

    pause 0.3

    scene bg_cg013 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg013")

    think "Elen protège un bol énorme et fumant. L'odeur est bizarre, on dirait un mélange de forêt et de sucré."

    pause 0.3

    iris "C'est quoi, ce truc ? Elen, tu peux pas avaler ça !"

    elen "C'est. Une. Masterpiiiiece."

    iris "Pourquoi à chaque fois que j'entends ce mot, c'est carrément l'inverse, hein ?!"

    elen "Maiiiis noon, chez des pâtes, des noix et... un petit truc checret."
    "Elle ne peut pas s'empêcher de parler la bouche pleine."

    iris "Un petit truc secret ?! C’est exactement comme ça qu’on finit à l’infirmerie."

    elen "T’inquiète. Ch’est Goumi qui a validé."
    elen "Goumi ne tue pas ses clients. Enfin, pas volontairement !"

    iris "… C’est pas rassurant."

    think "Elen mélange, goûte. Ses yeux s'illuminent."

    elen "Oh ! Ch'est trooop bon ! Exactement trop bon !"

    iris "Tu essaies de nous convaincre ou de survivre à la première bouchée ?"

    elen "J'ai le droit d'être heureuse, nooon ? Tu devrais essayer !"

    iris "Ça me fatigue rien que de te regarder."

    elen "Goûte ! Aller, rien qu'une bouchée ! Pour l'art ! Tu es bien courageuse non ?"

    iris "Alors pas particulièrement, mais là encore moins !"

    elen "Même pas pour la postérité ?!"

    iris "Surtout pas... Encore moins."

    elen "Ok. Bah ça en fait plus pour moi. C-ça... m'va..."

    think "Mon plateau se limite à une barre et un jus. La nausée tient le reste de la place."

    noam "Goumi t’a laissé commander ça ?"

    elen "Ouaiiiis. J'lui ai fait ce regard. Genre."

    scene bg_cg013_1 at adaptive_fullscreen with fade
    think "Elle compose un regard si particulier."

    elen "Le regard ultiiime !"

    iris "Le regard du caprice, oui."

    elen "Le regard du caprice, c'est mignon ! Je me suis bien entraînée t'as vu ?!"

    scene bg_cg013 at adaptive_fullscreen with fade
    pause 0.3

    iris "On dirait des pâtes… Avec des cailloux."

    elen "C’est des noix."

    iris "Oui. Avec des cailloux, la texture serait peut-être plus cohérente."

    elen "Ah ouais, tu crois ?"

    iris "C'était du sarcasme, Elen. Ne mange pas de cailloux. Je refuse de remplir ce rapport d'incident."
    iris "Puis qui mange des pâtes dès le matin d'abord ?!"

    pause 0.3

    iris "…"

    elen "Tu vois ? La vie, c'est ça ! Profiter et s'en foutre de ce que les autres pensent !"
    elen "Comme ça, rien ne t'atteint."

    iris "Tu dis ça comme si c’était normal."

    elen "Ça devrait en tout cas."

    pause 0.5
    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.80),
        ("elen", "joie", 0.20),
        ("iris", "fatigue", 0.50),
    ])

    iris inquiet "T’as pas peur. Deux secondes ?"

    elen triste "Si. Mais là, maintenant, tout de suite, j’ai faim."
    elen joie "Alors je m'en fou d'avoir peur."

    iris surpris "…"

    elen taquin "T’as envie de me faire la morale, hein."

    iris triste "Un peu."

    elen taquin "Vas-y. Je t’écoute. Héhé, balance ton sermon."

    iris fatigue "Non. Laisse tomber."

    think "Une chaise racle derrière nous. Personne ne regarde."

    $ showGroup([
        ("elias", "neutre", 0.60),
    ])

    elias sourire "Wsh, vous mangez quoi ?"

    elen joie "Le bonheur."

    iris taquin "Ne la crois surtout pas..."

    elias inquiet "… Faut manger correctement. Surtout aujourd'hui."

    elen taquin "Oh non. Iris me faisait déjà la morale, pas besoin de moraline en plus !"

    elias colere "Je plaisante pas."

    iris taquin "Il plaisante jamais. Crois moi. Ca c'est vrai."

    elias sourire "Protéines, œufs, poulet. Simple. Efficace. Nutritif."

    think "Elen le regarde comme s'il venait de recommander l'eau tiède pour le plaisir."

    elen triste "Tu veux manger du poulet, ici ? Alors que c'est peut-être le seul endroit où tu peux demander à manger tout ce que tu veux ?!"

    elias reflechit "C'est une base. Ça tient au corps. Mais ton truc là... c'est chaud de manger ça."

    iris taquin "Merci. Elle a clairement un palais de doberman !"

    elen colere "Et, oh ! C’est pas des pâtes aux noix. C’est une œuvre d'art gustative."

    elias peur "Franchement, j'en doute."
    elias reflechit "Cet aprèm, faudra être lucides. On peut pas arriver tout mous. Faut bien manger !"

    iris triste "…"

    elen colere "On devait pas en parler. Pas pendant le repas !"

    elias reflechit "Personne veut en parler. C’est pour ça que ça tourne dans les têtes."

    iris colere "On n’est pas obligés. Là. Maintenant. On est en train de manger."

    elias triste "On fait quoi alors ? On arrive et on improvise ? C'est chaud comme plan."

    elen sourire "Bon vu que vous me cassez les pieds avec ça. Moi, je vais pas improviser. Je sais déjà ce que je vais faire."

    think "Elen bondit presque de sa chaise."

    elen joie "Moi je vote pour !"

    pause 0.4

    think "Elle l'annonce comme un dessert de mariage. Aucune hésitation n'est visible sur son visage."

    iris reflechit "Tu le dis si facilement."

    elen taquin "Parce que c'est facile. Ici on crève d'ennui, dehors ils crèvent pour de vrai."
    elen inquiet "Enfin... c'est pas drôle. Vous avez compris. Alors si on peut changer ça, on change ça et puis c'est tout !"

    iris reflechit "…"

    elias sourire "Tu marques un point."

    $ showGroup([
        ("julian", "neutre", 0.30),
    ])

    julian "J'ai entendu « je vote pour » ?"

    elen rire "Oui. Bienvenue au club !!"

    julian sourire "Évidemment. JE vote pour. JE serai de ton côté ! Toujours aux côtés de ma secrétaire préférée !"

    iris hesitation "Julian…"

    julian reflechit "Quoi ? Je ne vais pas cacher une position aussi évidente. On a tous besoin de clarté."

    think "Toute la salle regarde maintenant dans notre direction. Elen sait fédérer, même par accident."

    elen taquin "Bon vu qu'il faut y aller, je me lance ! Question simple. Qui vote pour ?"

    think "Julian lève la main comme si une caméra attendait précisément ce plan."

    julian rire "Pour. Evidemment."

    think "Tout le monde regarde dans ma direction."

    noam reflechit "Tu votes pour... sans aucune hésitation ?"

    think "Elen hausse les épaules. Pour elle, c'est évident. Et moi ? Si c'était si simple..."

    noam inquiet "Et si le texte est foireux ?"

    elen colere "Nooon ! Il faut voir le bon côté !"

    iris fatigue "Une seule voix contre suffit. L'enthousiasme n'est pas une stratégie de vote."

    elias "Pour. Mais faut que ça soit vraiment appliqué. Sinon c'est chaud de voter pour du vent."

    think "Kael tente de passer avec son plateau. Elen lui barre la route."

    $ showGroup([
        ("kael", "neutre", 0.10),
    ])

    pause 0.4

    elen joie "Kael ? Pour ou contre ?"

    kael "… Je ne sais pas. Je déciderai au moment de voter."

    elen "Ok. Au moins c'est une réponse honnête."

    hide kael with moveoutleft

    think "Mara arrive, inspecte les plateaux puis les visages."

    $ showGroup([
        ("mara", "neutre", 0.00),
    ])

    mara reflechit "On vous entend de loin. Annoncer vos votes devant les caméras, c'est audacieux."
    mara taquin "Ou généreux. Vous facilitez le travail de tout le monde."

    elen joie "Oh non. On est démasqués."

    iris reflechit "Alors, tu t'es décidée ? Tu votes contre ?"

    mara taquin "J'ai pas dis pas ça."
    mara reflechit "Je comprends l'idée. Mais on ouvre une porte sans voir derrière."
    mara taquin "D'habitude, j'aime les surprises. Celles qui concernent des millions de gens, bof, un peu moins."

    elen colere "C’est du commerce. C'est pas comme si on proposait l'éradication des bébés pingouins !"

    mara doute "T’en es vraiment sûre ?"

    iris colere "Mara…"

    mara colere "Non. Laissez. Je dramatise pas. Je demande ce qu'on n'a pas compris."
    mara colere "Où est le texte exact ? Je veux le voir avant de voter quoi que ce soit."

    elen reflechit "Ok. Je t’entends. Vraiment. Mais… On fait quoi sinon ?"
    elen colere "On regarde les gens crever et on se dit que c'est pas de notre faute ?"

    mara triste "Je ne dis pas ça."

    mara reflechit "Sur le principe, je vous comprends. Vouloir avoir accès à tout, sans avoir à demander, c'est bien..."
    mara peur "Mais... Si ça tourne mal, c'est nous qui payons. Pas Kami. Nous."
    mara reflechit "Et puis je ne suis pas sûre que tout le monde souhaite retourner à cette vie de travail et d'exploitation des autres."

    noam reflechit "Tu veux des garanties. Pour ne pas faire de conneries."

    elen taquin "Ok. Donc t’es pas contre, tu vas voter pour."

    mara stress "Je te jure…"

    elen rire "Je plaisante."

    julian "Au moins, le collectif penche vers le pour."

    elen joie "Ça me suffit pour le moment."

    mara reflechit "Et bien, ça dépendra surtout de l'énonce précis."

    call day3_collect_vote_argument("enonce_precis") from _call_day3_collect_vote_argument_enonce_precis

    pause 0.3

    think "Elen pousse son bol vide avec la satisfaction d'une mission accomplie."

    elen content "Ok. Je vais aller digérer mon œuvre."
    elen taquin "Et peut-être convertir d’autres âmes à ma bonne humeur."

    iris "Bonne chance."

    elen rire "Merci. Hé hé, Je suis née pour ça."

    hide elen with moveoutleft

    pause 0.4

    $ hideGroup()
    "Peu à peu, tout le monde se lève et quitte la cafétéra. Rapidement, il ne reste qu'Iris et moi."

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("iris", "neutre", 0.60),
    ])

    iris fatigue "Tu vois. Même quand personne veut en parler…"
    iris fatigue "On finit toujours par le faire.."

    "Puis elle sort de la pièce à son tour."
    hide iris with moveoutleft

    think "Je repose mon plateau et me lève."

    stop music fadeout 0.8

    "Que devrais-je faire en attendant ?"

    call START_FREE_TIME("_3_PAUSE_CHAMBRE") from _call_START_FREE_TIME_3_1

# Durée : 6m30
# Totale : 1h 34m 25s

# + 1m30 de temps libres
# Totale : 1h 36m 00s

label _3_PAUSE_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Je suis retourné dans ma chambre afin de me reposer quelques temps."
    think "Il sera bientôt l'heure de voter."

    play sound sfx_knock
    think "Quelqu'un frappe à la porte."
    pause 0.2
    play sound sfx_knock
    pause 0.2

    nyra "Noam ! Ouvre !"

    think "Je me lève et l'ouvre."

    scene bg_dortoir at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("nyra", "neutre", 0.60),
    ])

    nyra stress "Julian fait chier tout le monde, il fait le tour des indécis."

    noam "Hein ? Qu'est-ce qui se passe exactement ?"

    nyra colere "Il est allé voir Tomas, puis deux autres. Il ne défend pas seulement le texte."
    nyra triste "Il essaye de leur imposer de voter pour, pas sûr que ça marche, au contraire !"

    noam "Où est-ce qu'il est ?"

    nyra "Je crois qu'il est encore dans la salle de repos."

    stop music fadeout 0.5
    play music "music/bgm_tension_low.mp3" fadein 0.6

    scene couloir_dortoir at adaptive_fullscreen,memory_idle with fade

    think "Nous nous mettons à courir en direction de la salle de repos, par chance, elle n'est pas très loin."

    play sound sfx_run

    think "Mes semelles claquent sur le métal. Nyra court devant sans regarder derrière."
    "Les néons défilent. Les caméras semblent pivoter avec nous."
    think "Putain, quel spectacle on donne aux gens encore..."

    play sound sfx_run

    call day3_play_corridor_trace from _call_day3_play_corridor_trace


    scene couloir_cafeteria at adaptive_fullscreen with fade
    think "Je l'entends rire depuis l'arrière de la porte."

    scene bg_repos at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "neutre", 0.10),
        ("nyra", "neutre", 0.30),
        ("julian", "neutre", 0.50),
        ("tomas", "neutre", 0.70),
    ])

    julian sourire "— si JE prend la parole en premier, on y arrivera plus facilement."
    julian sourire "Il faut donner un cap, incarnet le changement, que quelqu'un en qui les gens se reconnaissent prennent le lead."

    tomas hesitation "N-Ne compte pas... J-Je..."

    julian rire "Allez Tomas. Tu veux que ça change n'est-ce pas ? Ecoute moi. Le monde a besoin de toi."

    tomas inquiet "O-Ouais, sans doute..."
    
    think "Je m'avance, prêt à lui couper la parole."

    call day3_julian_clash_minigame from _call_day3_julian_clash_minigame

    noam determine "Il me semble que personne ici n'a de mandat pour se poser en leader."

    julian sourire "Ah. Noam. Il fallait évidemment que tu débarques."

    noam hesitation "Que tu veuilles que le vote passe, je le comprends."
    noam "Mais si tu te mets trop en avant, les hésitants vont percevoir autre chose."
    noam reflexion "On voit clair dans ton jeu Julian. Tu veux te mettre en avant."
    noam raison "Le risque, c'est que le vote ne se basera plus sur le fond de la proposition. Ce sera sur toi."
    noam colere "Et une chose et sûre : toi, tu ne fais pas l'unanimité !"

    julian sourire "Tu t'es décidé à te réveiller ? On en t'entends pas depuis le premier jour."
    julian taquin "Et là tu viens faire ton malin ?"
    julian "JE veux que ce texte passe. Alors laisse moi convaincre les autres."

    noam "Parle du texte. Rien d'autre. Le reste, ta petite personne, ta gloire personnelle, tout le monde s'en contrefout."

    tomas "I-Il a raison. Enfin... Je veux dire..."
    tomas "Si ça ressemble à une démonstration d’ego, f-Franchement, ç-ça sera sans moi."

    julian triste "Bon. Très bien. Nous verrons au Conclave qui porte réellement ce vote."
    julian "Évite simplement de me transformer en antagoniste. Je suis là pour le bien collectif, moi. Et je me bouge pour faire avancer les choses."

    hide julian with moveoutleft

    stop music fadeout 0.6
    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    tomas mefiant "... D-Désolé, à cause de moi, v-vous avez du venir m'aider..."

    nyra "Non pas de soucis, il fallait remettre les points sur les i de toute façon."

    tomas "P-Pour être honnête, je ne veux pas que ce soit lui qui donne le ton."
    tomas "Il faut que quelqu'un puisse lui tenir tête... T-Tu vas parler tout à l'heure ?"

    noam "Oui. Mais pas pour briller. Pour essayer que ça avance dans le bon sens."

    tomas hoche_la_tete "Alors ça a une chance de passer."

    nyra "Allez viens Tomas, tu as bien mérité une pause avec tout ça..."
    nyra sourire "Merci Noam."

    think "Ils repartent ensemble."
    hide tomas with moveoutleft
    hide nyra with moveoutleft

    think "Ce vote, c’est pas juste un texte. C’est aussi une question de confiance."
    think "On ne peut pas faire n'importe quoi, au risque de briser celle que les autres nous porte."
    think "Julian n’est pas un ennemi. Mais son caractère peut causer le pire comme le meilleur."
    think "Je serre les poings. Ils tremblent moins qu'avant."
    think "Les grands discours, ce n'est pas vraiment pour moi."
    think "Mais je ne peux pas laisser les choses s'envenimer."
    think "Je devrais y aller."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite

# Durée : 2m40
# Totale : 1h 37m 05s

# + 1m30 de temps libres
# Totale : 1h 38m 35s

label _3_TRANSITION_CONCLAVE:

    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Il sera bientôt l'heure. Le couloir me paraît plus sombre, plus étroit, encore moins amical."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    think "Respire, Noam. C’est juste un vote."
    think "Pourquoi est-ce que mon cœur continue de taper comme ça."
    think "Une sueur froide glisse dans ma nuque. J'ai l'impression d'être observé, bien plus que d'habitude."
    think "Les caméras. Évidemment. Pourquoi auraient-elles disparu aujourd'hui ?"
    think "Tout le monde s'est plus ou moins réuni dans le couloir et le groupe converge vers le Conclave en partageant le même silence."

    $ showGroup([
        ("lysa", "neutre", 0.25),
    ])

    "Lysa marche légèrement en retrait. Juste assez pour que ça se voie."
    "Le groupe accélère quand le couloir se resserre. Elle, non. Elle continue à trainer des pieds."
    "J'essaye de calibrer mon rythme sur le sien, pour qu'elle me rattrape."
    "Elle tourne la tête. Ni sourire ni attaque. Seulement de la fatigue."

    lysa triste "On va voter. On va échouer."
    lysa triste "Puis demain on se réveillera de nouveau ici, avec les mêmes murs, la même pression. Puis on recommence dans trois jours."
    lysa blase "Et on échouera encore. On ne peut pas changer ce monde."

    think "Elle ne me parle pas vraiment. Elle n'a pas l'air d'attendre de réponse. Elle récite une conclusion déjà prononcée dans sa tête."
    think "Je ne sais pas quoi répondre d'ailleurs. Peut-être qu'elle a raison ? Peut-être qu'elle a tord."

    noam reflechit "Il n'y a que ceux qui ne tentent rien qui n'ont rien."
    noam sourire "Il faut aller de l'avant, et ce qui arrivera, arrivera."

    "Lysa a une mine déconfite alors que nous arrivons devant la porte de la Salle du Conclave."
    "Et puis c'est arrivé..."

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    "Sans prévenir, sans théâtre. Sael a sauté sur Lysa pour la prendre dans ses bras."

    sael "Tu as le droit d'être fatiguée, perdue ou démotivée."
    sael "Ma grand-mère disait que même les morts se reposent avant de revenir dans nos rêves."

    sael "On a besoin de ta lucidité. Pas d'une autre Lysa. De celle qui est là."

    "Elle pointe du doigt la poitrine de Lysa."
    "Les épaules de Lysa se détendent à peine, elles se relâchent."

    lysa "Tu dramatises. Je suis toujours là."

    sael "Alors montre-le. Montre nous cette battante qui est en toi."

    "Sael la relâche sans s'éloigner complètement."

    sael "Tu vois des failles que je ne vois pas, qu'on ne voit pas. C'est pénible. Mais c'est utile."

    lysa "Si je sauve le débat, tu me dois un café. Les oracles se faisaient mieux payer, hein."

    sael "Je t'en offre même deux, en plus, ici, personne ne paie rien. C'est peut-être un signe."

    scene bg_conclave at adaptive_fullscreen with dissolve

    think "On entre dans la salle et on s'installe à nos places. Bon, ça y est. C'est parti."

    play sound sfx_announce
    pause 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous voilà tous ! Manquera-t-il quelqu'un ? Mes chers téléspectateurs, nous le saurons dans un instant !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "On voit à vos visages qu'il y a eu un peu d'émotion !"
    kami "Oh, comme c'est mignon !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "CAMERAMAN ! Un petit zoom sur ces visages cro-crognon !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pardonnez mon humour douteux, je suis comme vous, moi aussi je stress !"
    kami "C'est bien la première fois que j'organise ça..."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais pas d'inquiétude, asseyez-vous. On commence dans quelques instants."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade
    pause 0.4

    "Les portes se referment derrière nous, on entend un cliqueris.."

    think "C'est... C'était un verrou ça ? Ils ont fermé à clé derrière nous ?!"

    play sound sfx_door

    think "Putain, plus de retour en arrière possible."

# Durée : 2m55
# Totale : 1h 40m 00s

label _3_DEBAT1_PHASE1:
    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "C'est bon tout le monde est installé ?"
    kami "C'est TROOOP LOOONG !!"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bon on va commencer cette première phase en douceur. Vous allez devoir poser les bases."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Avant de vous arracher les cordes vocales, vous allez devoir reconstruire le texte ensemble."
    kami "Il faut que vous sachiez de quoi vous parlez non ?!"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ne faites pas les mêmes erreurs que les anciens politiciens qui ont conduit le monde à sa ruine !"

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn "Attends comment ça reconstruire le texte ensemble ?!"
    ryn "C'est quoi ce bordel ?! Ce n'est pas ce que tu as dis hier ?"
    $ bc_hide()

    kami "Non mais attends ! Tu ne penses tout de même pas que je vais faire le travail à TA place ?!"
    kami "J'ai un monde entier à gérer, je suis très occupée, moi !"
    kami "Déjà que j'ai dû revoir entièrement votre très mauvaise formulation !"

    $ bc_show("sael", "reflechit", px=-70, py=-50, pz=0.85)
    sael "Donc ça veut dire qu'on a même pas la base écrite de l'amendement ?"
    sael "Comment on va faire pour en débattre sans ça ?!"
    $ bc_hide()

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mon dieu, je savais qu'en prenant des jeunes il aurait fallu tout expliquer !"
    kami "Zen... Kami, tu t'y étais préparée..."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ne vous en faites pas, je sais que vous n'avez PAS de mémoire..."
    kami "Alors pour vous aider, mais pas trop, j'ai réarrangé les mots de l'amendement déposé... Et..."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je vous laisse découvrir tout ça. Histoire de voir vos débats !"

    $ bc_show("lysa", "colere", px=-70, py=-50, pz=0.85)
    lysa "C'était évidemment trop beau !"
    lysa "Avoir un amendement qui autorise simplement le commerce, c'était trop simple !"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Toujours en train de pleurnicher ceux là..."
    kami "Vous devriez être reconnaissants de cette possibilité de changement !"

    $ bc_show("nyra", "stress", px=-70, py=-50, pz=0.85)
    nyra "Qu'est-ce qui nous garantit que les mots ajoutés ne changent pas l'intention ?"
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bref, j'ai rentré les mots de l'amendement à archive et je les ai compilé."
    kami "Malheureusement pour vous, ils sont totalement dans le désordre."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Avant de pouvoir débattre de quoi que ce soit, il faudra que vous régliez ce problème..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous vous rappelez vos règles de construction de phrase. SUJET, VERBE, COMPLEMENT, POINT."

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

    ryn colere "Elle pouvait pas nous les donner directement dans l'ordre ?!"
    ryn triste "Sérieusement, pourquoi elle fait ça ?!"

    sael reflechit "Va falloir qu'on s'y mette si on veut avancer."

    nyra "On va faire ça vite, ça va aller. Cherchez la ponctuation et les majuscules, ça aide à mieux situer les mots."
    nyra "Si chacun prend un fragment, on reconstruira tout ça plus vite."

    noam "D'accord. On reconstruit ça, puis on discutera ensuite."
    noam "J'espère que rien de dangereux n'a été ajouté."

    hide screen day3_codex_logo

    # Wrapper complet : intro animée, tutoriel 1ère fois, retry avec malus, résultats avec rang
    call debat_phase1_run(mg_id="fatal_assembly", title="FATAL ASSEMBLY")

    $ phase1_ok = debat_phase1_last_result.get("success", False)
    $ phase1_time_left = debat_phase1_last_result.get("time_left", 0)
    $ phase1_kamyz_gain = debat_phase1_last_result.get("kamyz", 0)
    if phase1_ok:
        $ player_kamyz += phase1_kamyz_gain
        $ renpy.notify("+ %d Kamyz" % phase1_kamyz_gain)
        call screen noam_consent_screen

    scene bg_conclave at adaptive_fullscreen with dissolve
    show screen day3_codex_logo

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

    lysa "Autoriser le transport, la vente et l'échange de marchandises ..."
    lysa "Le système actuel de distribution de denrées est aboli ?!"

    elen "On l'aaa ! Enfin une base claire !"

    tomas "Parfait. M-Maintenant, le vrai débat peut commencer."

    jump _3_DEBAT1_PHASE2

# Durée : 2m35
# Totale : 1h 42m 35s

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

    mara surpris "Le papier est clair. Qui est le génie qui veut supprimer les distributions de bons de rationnement ? Qu'il se dénonce !"
    
    elen triste "Attends, ça faisait partie de la proposition ? C'est pas du tout la même chose !"

    noam "Du calme ! Vous savez très bien que ce n'est pas ce qui avait été proposé."
    noam "C'est l'adaptation qu'en a fait Kami."

    tomas surprus "La… la formulation est… euh… très claire."
    tomas reflechit "L’abrogation… elle est… incluse. Oui."

    nyra reflechit "Donc ça veut dire que si on vote cet amendement, demain il n'y aura plus de distribution gratuite de nourriture."

    kael inquiet "Supprimer les distributions, ça change tout..."

    ryn colere "Ça supprime TOUT ! La seule putain de sécurité qu’on avait !"

    julian reflechit "C'est différent de ce qui a étéé annoncé oui, mais-"

    lysa reflechit "En même temps c'est logique."

    noam "Hein ?"

    lysa blase "Et bien oui, c'est en partie ce qu'on disait hier : si on rétablit le commerce, on rétablit un système monétaire."
    lysa reflechit "Donc pour gagner de la monnaie, il faut travailler. Et pour motiver les gens à travailler, on arrête de leur donner tout ce dont ils ont besoin."

    mara colere "C'est exactement ce que je disais."

    nyra reflechit "On voit en action comment Kami modifie une idée pourtant simple pour nous mettre dans l'embarras."
    nyra reflechit "Ce n’est pas anodin. Supprimer une structure mondiale, ça ne se décide pas sur un coup de tête."

    julian joie "Au moins c'est plus clair désormais, non ?! Nous devons débattre du texte et décider de ce qui est le mieux."

    ryn colere "Facile à dire."

    noam "Je me demande si... tout ça n'est pas une mascarade."
    noam "Il est possible que Kami se moque totalement de nous, et que personne n'ait proposé ça."

    lysa reflechit "Oui. Dix votes pour douze textes : le tour de passe-passe est parfait."
    lysa colere "Les augures choisissaient déjà les signes qui les arrangeaient. Là c'est pareil."
    lysa blase "Kami peut ajouter, supprimer ou modifier n'importe quoi. On ne le saura jamais et de toute façon c'est elle qui fait les règles."

    ryn reflechit "Hein, qu'est ce que tu veux dire par là ?!"

    lysa blase "Si Kami injecte ses propres textes, chacun attendra le sien, peut-être que tous les textes mis au vote sont scriptés !"
    lysa salut "S'il ne sort jamais, il se croira simplement parmi les deux oubliés. La manipulation est invérifiable."

    sael reflechit "Donc c'est impossible de savoir si c'est l'un d'entre nous qui a proposé ça ?!"

    noam "Exactement. Seules Kami et l'auteur — s'il existe — connaissent la réponse."

    sael triste "Les morts de Limen n'ont pas besoin d'un nouveau responsable."
    sael reflechit "Kami. Dis-nous seulement si ce texte vient de nous."

    think "Les regards se croisent. Personne ne répond."
    think "L'écran central reste figé. Kami ne répond pas."

    noam "Bon, il faut qu'on en discute. Tout ça n'est pas important pour le moment."
    noam reflexion "Dans tous les cas, il faudra voter. Manipulation ou pas."

    julian reflechit "Noam, cette découverte nuance ma position. Mais elle ne l'annule pas."
    julian joie "Les échanges restent essentiels. Je ne renie pas une idée au premier obstacle."

    lysa blase "Ah ouais ? T'es prêt à tout changer juste pour faire l'intéréssant ?"

    think "Les regards convergent vers Julian."

    julian joie "Autoriser le transport et la vente relance les districts, l'économie, le mouvement."
    julian reflechit "Nous rendons aux gens une part importante de leur liberté ! La liberté contre de la nourriture gratuite ?"
    julian joie "Pour moi, le choix est vite fais."

    mara taquin "Et tu comptes faire comment, lover ? Tu nourris les ventres vides avec ton discours ?"

    julian sourire "Comment on le faisait avant ? Un district qui produit des ressources le vendra aux autres. Tout simplement."

    ryn colere "Et ceux qui n'ont rien ?!"
    ryn triste "Si le système actuel saute… Les distributions sautent aussi."
    ryn colere "Et ça ça tuera de nombreuses personnes dans les districts les plus pauvres dont Limen."

    julian reflechit "Pas forcément."

    ryn colere "Si. C’est écrit noir sur blanc."

    sael reflechit "Non, il suffira de travailler pour gagner de quoi acheter à manger."

    noam "Calmez-vous vous deux ! On est pas là pour s'étriper !"

    tomas reflechit "L’abrogation du système de distribution implique la disparition des rations."
    tomas reflechit "Il n’y a pas d’entre-deux, c-c'est factuel."

    julian sourire "On peut le compenser."

    lysa reflechit "Comment tu comptes faire ça ? Ce n'est même pas précisé dans l'amendement."

    julian colere "C’est fou. Dès qu’on parle d’ouverture, vous imaginez l’apocalypse."

    mara taquin "Ouais non, j’ai pas envie de ramasser des macchabées parce que Monsieur Idéal a eu une illumination de start-upper."

    elen joie "Mais attendez ! Ça va être génial !"
    elen sourire "Les trucs vont circuler partout, on pourra enfin CHOISIR ce qu’on veut !"
    elen reflechit "C’est pas ça, la liberté ?!"

    nyra raison "Ça dépend de qui pourra les acheter."

    mara triste "Regarde, par exemple, sur Orbite, ils ne produisent pas-"

    kael reflechit "Alors oui et non..."
    kael raison "Si on ne produit pas beaucoup de ressources, on en exploite quand même dans l'espace."
    kael raison "Simplement ces matériaux là ne restent pas bien longtemps chez nous, on les exporte rapidement."

    # Animation "Objection" de Ryn
    ryn colere "Dans tous les cas, y'a un problème !"
    ryn reflechit "Actuellement la frontière est fermée, seuls ceux qui ont une autorisation spéciale peuvent passer."
    ryn reflechit "Même si on ne peut pas passer, les matériaux peuvent passer sans soucis. Comment se fera le transport ?"
    ryn reflechit "Et si les distributions sautent comment feront les plus pauvres pour s'acheter quelque chose ?"

    noam "Logiquement, il y aura un système de laissé passer. Il existe déjà des dérogations pour traverser les frontières."

    julian reflechit "Tu pourras acheter des choses en gagnant de l'argent, par exemple en travaillant ou en vendant-."

    # Animation "Objection" de Ryn
    ryn colere "Vendre QUOI, Julian ?! Nos godasses trouées ?"

    julian sourire "Leur travail, leur ressource."
    julian taquin "Ne me fais pas croire un instant qu'il n'y a pas de travail à Limen !"

    ryn reflechit "Si, évidemment qu'il y en a..."

    julian colere "Et pourquoi les gens ne travaillent pas ?!"

    ryn colere "Parce que ça change QUE DALLE !"
    ryn triste "Tu travailles. Tu te crèves le cul douze heures, tu touches le même ticket pourri que le mec qui dort toute la journée."
    ryn colere "C’est ça ta motivation, toi ?!"

    lysa reflechit "Oui, c'est pareil dans tous les districts..."
    lysa reflechit "Comme on a les bons de rationnement et l'interdiction de faire du commerce, le travail est devenu optionnel."
    lysa blase "On ne travaille que si on le souhaite ou si on en reçoit l'ordre de Kami."

    think "Julian relève la tête, comme si Lysa venait de valider sa conclusion."

    julian joie "Enfin quelqu'un comprend où JE veux en venir."

    noam "Tu veux redonner du sens au travail en utilisant le commerce ?"

    julian joie "La question est : est-ce que le système actuel fonctionne ?"

    mara colere "..."

    julian peur "Il nous étouffe."

    ryn colere "Il nous nourrit aussi."

    julian colere "En nous rationnant, en nous empêchant de manger ce qu'on veut, en nous distribuant du pain rassi, en nous obligeant à réclamer tout et n'importe quoi !"
    julian colere "Mais réveillez-vous ! Vous voulez VRAIMENT garder ce monde là ?!"

    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On me dit dans l'oreillette que vous êtes ennuyants !!"
    kami "Tout ça, vos blabla, ça n'avance pas ! Je suis obligée de prendre les choses en main."
    kami "Nos internautes ont du mal à vous suivre !"

    "Les pupitres se transforment. Micro et buzzer émergent devant chacun de nous."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "A partir de maintenant vous n'avez plus la parole. Vous parlerez à tour de rôle. Histoire qu'on puisse vous entendre."
    kami "Devant vous, il y a un buzzer, si vous voulez contredire un propos d'un de vos camarades, vous pouvez appuyer dessus."
    kami "Et vous ne parlerez que lorsque votre buzzer s'allumera d'une couleur verte !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Compris ?! Alors c'est parti !"

    hide screen day3_codex_logo
    call debat_phase2_minigame from _call_debat_phase2_minigame
    show screen day3_codex_logo

    jump _3_DEBAT1_PHASE3

# Durée : 6m05
# Totale : 1h 48m 40s
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

screen argument_menu_ui(options, prompt="Choisis l'argument à projeter."):
    modal True
    zorder 250

    add "gui/day3/vote_phase3/bg.png"

    frame:
        background None
        xalign 0.5
        yalign 0.5
        xsize 1620
        ysize 820
        padding (40, 35)

        vbox:
            spacing 28
            xfill True

            add "gui/day3/vote_phase3/prompt_panel.png" xalign 0.5
            text "INTERVENTION STRATÉGIQUE" size 48 color "#7be7ff" xalign 0.5 font "fonts/Rajdhani-SemiBold.ttf"
            text "[prompt]" size 30 color "#d5f7ff" xalign 0.5 text_align 0.5

            hbox:
                spacing 26
                xalign 0.5

                for i, opt in enumerate(options):
                    $ is_unlocked = opt["title"] in arguments
                    fixed:
                        xsize 490
                        ysize 560
                        at p3_arg_float

                        if is_unlocked:
                            add "gui/day3/vote_phase3/card_idle.png" xpos 0 ypos 0 xsize 490 ysize 560
                            add Solid("#61f0ff15") at p3_arg_glow
                        else:
                            add "gui/day3/vote_phase3/card_locked.png" xpos 0 ypos 0 xsize 490 ysize 560

                        imagebutton:
                            idle ("gui/day3/vote_phase3/card_idle.png" if is_unlocked else "gui/day3/vote_phase3/card_locked.png")
                            hover ("gui/day3/vote_phase3/card_hover.png" if is_unlocked else "gui/day3/vote_phase3/card_locked.png")
                            at p3_arg_button_idle
                            xalign 0.5
                            yalign 0.5
                            xsize 490
                            ysize 560
                            sensitive is_unlocked

                            if is_unlocked:
                                action Return(i)
                            else:
                                action NullAction()

                        vbox:
                            xalign 0.5
                            yalign 0.48
                            spacing 18
                            xmaximum 410

                            if is_unlocked:
                                text "[opt['icon']]" size 74 xalign 0.5
                                text "[opt['title']]" size 33 color "#9deeff" xalign 0.5 text_align 0.5 font "fonts/Rajdhani-SemiBold.ttf"
                                text "[opt['desc']]" size 25 color "#e6f6ff" xalign 0.5 text_align 0.5
                                add "gui/day3/vote_phase3/select_button.png" xalign 0.5
                            else:
                                text "?" size 92 color "#6f7c86" xalign 0.5 font "fonts/Rajdhani-SemiBold.ttf"
                                add "gui/day3/vote_phase3/locked_stamp.png" xalign 0.5
                                text "Argument non débloqué" size 24 color "#9a8f96" xalign 0.5 text_align 0.5

            text "L'impact dépend du moment et des tensions déjà installées." size 24 color "#86bdd0" xalign 0.5

label _3_DEBAT1_PHASE3:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.0
    show screen kami_broadcast_ui

    # =========================
    # OPTIONS FIXES (3 CHOIX x 3 MOMENTS)
    # =========================
    python:
        # >>> ICI TU DÉCIDES EXACTEMENT LES 3 ARGUMENTS DE CHAQUE MOMENT <<<
        store.p3_round_options = [
            [   # Moment 1
                build_arg("Bons de rationnement"),
                build_arg("Difficulté d'approvisionnement"),
                build_arg("Faiblesse d'Orbite"),
            ],
            [   # Moment 2
                build_arg("L'énoncé précis"),
                build_arg("Le monde d'avant"),
                build_arg("Échanges discrets déjà actifs"),
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

    noam "Bon, il faut qu'on récapitule, et qu'on reste civilisés."

    julian "Civilisés ? On est en train de crever doucement, Noam."
    julian "Le statu quo, c’est une tombe collective avec des bons de pain rassis. C'est ça la liberté pour toi ?"

    ryn colere "Et ton 'choc salvateur', c’est quoi ? On sacrifie Limen pour que tes potes d’Orbite se payent des putes en or ?"

    julian surpris "D'orbite ?!"
    julian rire "Mais je viens de Nexus moi ! Faut suivre hein !"

    ryn "Ah... Euh oui..."
    ryn jaloux "Bah c'est pareil façon !"
    ryn colere "C'est peut-être même encore pire !"

    mara colere "Oh ça va, Ryn, calme tes hormones là."

    elen joie "Mais c'est çaaa qui est génial ! Choisir ce qu'on mange sans demander la permission !"

    lysa raison "Mais pour choisir, il faut de l'argent, Elen ! Midas transformait tout en or et il est quand même mort de faim."

    tomas "Euh… Après f-faut dire que les chiffres de la production mondiale depuis que K-Kami est arrivée ne sont pas bons…"
    tomas "…L'humanité produit quasimment quatre fois moins de choses de-depuis..."
    tomas "C’est… c’est pas rien, hein ?"

    nyra "En quoi c'est étonnant ? Tout le monde souhaite être récompensé pour son travail."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Oh ? Déjà la parano ? J’adore."
    kami "Je vous rappelle que cet amendement est le fruit de VOTRE imagination !"
    kami "Continuez, mes petits rats de laboratoire."
    kami "Oooh ! J'adore le drama ! l'audimat MONTE EN FLECHE !"

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], prompt="Moment 1 — Cadrer la première salve.")
    call _3_DEBAT1_PHASE3_INT1 from _call__3_DEBAT1_PHASE3_INT1

    stop music fadeout 1.0
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    elias "Parce qu'on évite les vraies questions. Le système actuel marche pas. C'est clair."

    sael "… Vous dépendez trop de ce système."
    sael colere "Les gens ne veulent plus travailler, ils ne veulent plus faire d'effort et ils veulent vivre libres."
    sael colere "C'est triste, mais il va falloir choisir. Choisir entre la liberté, et la sécurité."

    # Animation "Objection" de Lysa
    lysa blase "Même si on venait à voter pour, il reste un problème structurel."
    lysa reflechit "Comment feront les gens pour gagner leurs premières sommes d'argent ?"
    lysa blase "Si personne n'a d'argent, personne ne pourra payer quoi que ce soit, à personne."

    noam "tu as raison. C'est un gros point noir de la proposition."
    noam "Kami, tu peux nous en dire plus ou tu continues à te murer dans le silence ?!"

    show screen kami_broadcast_ui

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh, ça y est ? Enfin une question intéressante ? On avance !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Si cette proposition venait à être adoptée, je pourrais lancer des missions officielles qui seraient rémunérées."

    $ bc_show("nyra", "reflechit", px=-70, py=-50, pz=0.85)
    ryn "Des missions ? Comment ça marcherait exactement ?"
    $ bc_hide()

    kami "Et bien, ça fonctionnerait comme des sortes de quêtes. Vous savez, comme ce que vous adoriez autrefois en regardant..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Comment ça s'appelait déjà ?! Ah oui ! Les Isekai et leurs fameuses guildes !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous auriez des missions : fabriquer tant d'objet, récolter tant de ressources !"
    kami "Et chaque fois que vous remplireriez des missions, vous toucheriez un salaire sur vos objectifs."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et dans cette situation, libre à vous de travailler, ou pas. Mais il ne faudra pas compter sur la générosité des bons de rationnement."

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

    lysa reflechit "Le système semble viable, du moins pour lancer l'économie."

    nyra reflechit "Ouais, ce n'est pas déconnant. Puis après, avec le commerce, des sortes d'entreprises pourront voir le jour."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], prompt="Moment 2 — Désamorcer ou accélérer la fracture.")
    call _3_DEBAT1_PHASE3_INT2 from _call__3_DEBAT1_PHASE3_INT2

    stop music fadeout 1.0
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 1.0

    noam "Bon, je pense qu’on a fait le tour."
    noam "Le monde d’avant, le texte brut, les trocs qui existent déjà…"
    noam reflexion "Je me demande si... on est prêts à choisir maintenant."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Enfin ! Allez STOP ! Arrêtez de parler ! J’ai failli m’endormir avec vos jérémiades."
    kami "Le texte est clair : suppression totale des bons ou statu quo."
    kami "C'est l'heure de faire VIBRER l'audimat ! Il est temps de voter, POUR ou CONTRE !"

    hide screen day3_codex_logo
    jump vote_phase3_final

# Durée : 4m
# Total : 1h 52m 40s

label _3_DEBAT1_PHASE3_INT1:
    $ selected = p3_round_options[0][p3_pick]["title"]
    
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

    if "appro" in selected.lower():

        noam "Attends. Même avec les bons actuels… On a presque rien à manger."

        julian colere "Rien ! C’est du vent, Noam. Un bout de pain pourri, tout au plus."
        julian joie "Ouvrir le commerce, c’est remplir les rayons. Point."

        mara colere "Ouais, mais qu'est-ce que tu comptes faire pour les districts qui produisent que dalle ?"

        ryn colere "Exactement ! À Limen, on a quasi rien, tu crois que le marché va soudain nous livrer en priorité ?"

        kael reflechit "Après, Limen est le district le plus peuplé, donc c'est là-bas qu'il y aura le plus de demandes."

        lysa blase "Encore faut-il que les gens aient assez d'argent pour acheter."

        iris colere "Et bien ils n'auront qu'à travailler. C'est pas si compliqué."

        elen "Mais imagine ! Des épices, des vrais vêtements... On pourra enfin choisiiir !"

        sael "Et puis Limen fabrique déjà ce dont il a besoin quand il le peut. En tout cas, loin des grandes villes, c'est le cas."

        $ debat_day3_apply_influence({"julian": 2, "ryn": 1, "mara": -1, "kael": 1, "lysa": 1, "elen": 2})

    if "ration" in selected.lower() or "choix" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve

        noam "On dit que les bons permettent d’avoir beaucoup de choses…"
        noam "Mais en vrai, combien de produits sont réellement disponibles ?"

        nyra "Que vaut un droit inscrit sur un bon quand le rayon est vide ?"

        $ showP("tomas", "hesitation", 0.12)  # gauche
        tomas "Euh… les rapports indiquent souvent que 62 %% des références listées…"
        tomas "…sont en rupture permanente dans les zones périphériques."
        tomas "C’est… c’est pas juste un chiffre, hein ?"

        hide noam
        $ showP("mara", "agace", 0.50)  # centre
        mara "Le choix entre pain sec et pain moisi. Même dans ma pire fête, le buffet avait plus de dignité."

        hide nyra
        $ showP("iris", "desaccord", 0.88)  # droite
        iris "Et le produit correct disparaît en deux jours. Une chaîne logistique conçue par des amateurs ivres."

        hide tomas
        $ showP("ryn", "colere", 0.12)  # gauche
        ryn "C’est pas juste une question de goût !"
        ryn "À Limen, on a des bons pour du lait… qui arrive caillé la moitié du temps."
        ryn "Ou des médocs qui périment avant d’arriver. C’est ça votre 'nombreuses choses' ?"

        hide mara
        $ showP("elen", "joie", 0.50)  # centre – elle entre pour contrer
        elen "Mais justement ! Plus de fournisseurs, plus de concurrence, plus de choix ! Non ?"

        hide iris
        $ showP("noam", "raison", 0.88)  # droite – retour
        noam "En théorie, oui. Mais en pratique…"
        noam "Les fournisseurs iront là où il y a du pouvoir d’achat."
        noam "Et Limen n’en a pas beaucoup."

        hide ryn
        $ showP("elias", "determine", 0.12)  # gauche
        elias "C'est pour ça qu'il faut changer. Limen produit, vend, bosse."
        elias "Le même ticket pour rien, c'est chaud de défendre ça."

        # Modifs adhésion
        $ debat_day3_apply_influence({
            "julian": 1,      # aime l'idée de choix via commerce
            "ryn": 2,        # voit l'échec actuel comme preuve contre le changement
            "mara": 1,       # agacée par l'idéalisme
            "noam": 1,        # pragmatique, voit le potentiel mais reste prudent
            "nyra": 1,        # politique, apprécie la nuance sur le pouvoir d'achat
            "tomas": 1,       # factuel, les chiffres le font pencher vers le changement
            "iris": 1,       # râleuse, reste sceptique
            "elen": 1         # enthousiaste, adore l'idée de choix
        })

        hide elen
        hide noam
        hide elias

        return

    if "orbite" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("nyra", "raison", 0.50)  # centre
        nyra "Vous avez parlé de Limen. Que savez-vous du prix d'une erreur sur Orbite ?"

        $ showP("kael", "mefiant", 0.88)  # droite
        kael "Un écart. Un tir. Un module entier en danger."
        kael triste "Nous ne pouvons pas nous permettre l'imprévu."

        $ showP("noam", "reflexion", 0.12)  # gauche
        noam "C’est pour ça que le système actuel tient Orbite entre ses griffes ?"
        noam "Tu m'en avais rapidement parlé. Tout le monde sait à quoi s’en tenir."

        hide nyra
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Donc le bénéfice commercial doit dépasser un risque de dépressurisation. Voilà un seuil parfaitement raisonnable."

        hide kael
        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais peut-être qu’avec plus d’échanges, Orbite pourrait importer ce qu’il manque !"
        elen "Plus de stabilité, plus de ressources…"

        hide noam
        $ showP("tomas", "hesitation", 0.12)  # gauche
        tomas "Euh… en théorie, oui."
        tomas "Mais p-paradoxalement c'est sur Orbite qu'il y a le m-moins de morts chaque année."

        hide iris
        $ showP("julian", "determine", 0.50)  # centre
        julian "En autorisant le commerce, on ne met pas en cause la viabilité d'Orbite !"
        julian "Au contraire : on ouvre les possibles ! Ce n'est pas comme si on créait une nouvelle interdiction !"

        hide elen
        $ showP("lysa", "blase", 0.88)  # droite
        lysa "Et s'il y a la moindre chose qu'on ne contrôle pas, tout peut pêter."
        lysa "Et Nyra et Kael le savent mieux que quiconque."

        hide tomas
        $ showP("nyra", "stress", 0.12)  # gauche – retour
        nyra "Appelez ça du progrès si vous voulez. Sur Orbite, la perte de contrôle se paie immédiatement."

        think "Nyra et Kael échangent un regard bref, tendu. Personne n'insiste."

        # Modifs adhésion – pénalisantes pour le changement
        $ debat_day3_apply_influence({
            "julian": -2,     # idéaliste mais bloqué par la réalité d'Orbite
            "noam": 1,        # pragmatique, penche pour la stabilité
            "nyra": -2,        # manipulatrice, utilise Orbite comme argument massue
            "kael": -2,        # culpabilisé, terrifié
            "tomas": 1,       # factuel, chiffres le font pencher anti-changement
            "iris": -1,        # râleuse, horrifiée par le risque
            "elen": -1,       # enthousiaste mais remise en question
            "lysa": -1         # blasée, voit le pragmatisme anti
        })

        hide nyra
        hide lysa
        hide julian

    return

label _3_DEBAT1_PHASE3_INT2:
    $ selected = p3_round_options[1][p3_pick]["title"]

    scene bg_conclave at adaptive_fullscreen with dissolve

    if "avant" in selected.lower():
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Pff… le monde d’avant ?"
        iris "Vous parlez comme si c’était le paradis perdu."
        iris "Moi je m’en souviens : files interminables, prix qui doublaient sans raison…"

        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais au moins on pouvait choisiiir ! Tu bossais, tu achetais !"
        elen "Pas besoin d'attendre que Kami décide si tes chaussures sont assez trouées !"

        $ showP("mara", "reflexion", 0.12)  # gauche
        mara "Choisir…"
        mara "C’est un beau mot, Elen."
        mara "Moi je me souviens surtout des sourires obligatoires."
        mara "Des regards qui comptent chaque faux pas."
        mara "Et des portes qui se ferment si tu n’es pas… parfaite."
        mara "Mais bon… les robes étaient jolies."

        hide iris
        $ showP("julian", "determine", 0.50)  # centre
        julian "Ce monde n'était pas parfait. Il était vivant."
        julian "Les gens travaillaient, inventaient, échangeaient. Julian préfère le mouvement à une égalité dans l'attente."

        hide mara
        $ showP("tomas", "hesitation", 0.88)  # droite
        tomas "Euh… avant Kami, c’était surtout la guerre qui foutait le bordel."
        tomas "Tous les matériaux, la nourriture, les pièces… réquisitionnés pour l’effort de guerre."
        tomas "C’est pour ça que les prix explosaient et que les rayons se vidaient."
        tomas "Maintenant la guerre est interdite… donc techniquement, ça pourrait mieux tourner."

        hide julian
        $ showP("noam", "raison", 0.12)  # gauche
        noam "Le monde d’avant avait de la liberté pour ceux qui avaient déjà les moyens."
        noam "Pour les autres, c’était la loi de la jungle : les riches achetaient tout, les pauvres regardaient."
        noam "On a mis les bons et la distribution pour arrêter ça."

        hide tomas
        $ showP("elen", "joie", 0.88)  # droite – retour
        elen "Mais on peut garder le meilleur !"
        elen "La distribution pour les essentiels, et la liberté pour le reste !"
        elen "Comme avant, mais sans la guerre !"

        hide noam
        $ showP("mara", "colere", 0.50)  # centre – retour
        mara "Sans la guerre, peut-être."
        mara "Mais sans les chaînes aussi ?"
        mara "Tu crois que la liberté vient sans prix à payer ?"
        mara "Moi j’ai payé cher pour le découvrir."

        hide elen
        $ showP("iris", "desaccord", 0.88)  # droite – retour
        iris "Pff. Et maintenant c’est juste ?"
        iris "Au moins c’est égal. Tout le monde crève pareil."

        think "Un silence amer s'installe. Mara détourne le regard, regrettant déjà d'avoir donné quelque chose de vrai."

        # Modifs adhésion – Mara ambivalente : nostalgique mais blessée → léger malus au changement pur
        $ debat_day3_apply_influence({
            "julian": 1,      # adore le retour à la liberté/vie
            "elen": 2,        # enthousiaste, rêve du "mieux"
            "mara": -1,       # nostalgique de la richesse mais traumatisée par les obligations (teasé subtilement)
            "iris": 1,       # râleuse, sceptique
            "tomas": 1       # factuel, voit que sans guerre ça pourrait marcher
        })

        hide iris
        hide mara

    elif "énoncé" in selected.lower():
        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("ryn", "colere", 0.50)  # centre
        ryn "Le texte est clair comme de l’eau de roche !"
        ryn "Suppression des bons. Fin de la distribution. Point barre !"
        ryn "Pas de 'peut-être', pas de 'minimum vital'. Rien !"

        $ showP("elias", "determine", 0.88)  # droite
        elias "C'est ça qui libère ! Plus de bons, plus de laisse. On échange, on bosse, on vit."

        hide ryn
        $ showP("noam", "raison", 0.50)  # centre
        noam "Le texte est binaire."
        noam "POUR : suppression totale, liberté marchande immédiate."
        noam "CONTRE : on garde tout tel quel."
        noam "Y a pas d’entre-deux écrit. Pas de négociation possible."

        hide elias
        $ showP("kael", "triste", 0.88)  # droite
        kael "Il n'y a aucune transition."

        $ showP("lysa", "blase", 0.12)  # gauche
        lysa "Interpréter ? Le texte dit suppression. Pas réduction, pas adaptation."
        lysa "Icare aussi négociait avec la gravité. Bref."

        hide kael
        $ showP("elias", "determine", 0.88)  # droite – reste
        elias "On arrête de mendier des miettes. On produit. On vend. On survit. C'est concret !"

        hide noam
        $ showP("ryn", "colere", 0.50)  # centre – retour
        ryn "Survivre ?!"
        ryn "À Limen sans bons, on meurt en silence pendant que vous 'produisez' vos rêves !"
        ryn "Le texte condamne les faibles. C’est écrit noir sur blanc !"

        hide elias
        $ showP("sael", "mefiant", 0.88)  # droite – retour
        sael "Les Limenois échangent déjà pour survivre. Ce texte condamne peut-être moins qu'il ne révèle."

        think "Ryn frappe du poing. Sael ne cille pas."

        # Modifs adhésion : positif = POUR suppression / changement ; négatif = CONTRE
        $ debat_day3_apply_influence({
            "ryn": -2,        # violemment contre (condamnation Limen)
            "kael": -1,       # indécis, terrifié par l’absence d’entre-deux
            "elias": 1,       # déterminé, voit la fin de la dépendance
            "lysa": -1,       # blasée, pointe la cruauté immédiate
            "sael": 2         # très favorable : voit la suppression comme délivrance/force vitale
        })

        hide ryn
        hide sael

    elif "échange" in selected.lower() or "discret" in selected.lower():
        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("ryn", "colere", 0.50)  # centre
        ryn "Attends… tu dis que ça se fait déjà ?"
        ryn "Des trocs en douce à Limen ?"

        $ showP("sael", "mefiant", 0.88)  # droite
        sael "Depuis longtemps."
        sael "Un sac contre une réparation. Un service contre du tissu."
        sael "Ça tient les gens en vie entre deux distributions."

        $ showP("noam", "reflexion", 0.12)  # gauche
        noam "Ça marche en petit comité."
        noam "Mais si tout le monde le fait officiellement, est-ce que ça reste contrôlable ?"

        hide ryn
        $ showP("kael", "doute", 0.50)  # centre
        kael "Si ces échanges existent sans sanction... ils peuvent peut-être fonctionner sur Orbite."

        hide noam
        $ showP("julian", "determine", 0.88)  # droite
        julian "Exactement. Les gens savent déjà s'organiser."
        julian "Supprimer les bons, c'est cesser de nier leur initiative."

        hide kael
        $ showP("lysa", "blase", 0.12)  # gauche
        lysa "S'organiser, ou créer des petits rois. Les marchés noirs finissent toujours par couronner quelqu'un."

        hide julian
        $ showP("ryn", "reflechit", 0.88)  # droite – retour
        ryn "Mais… si c’est déjà là à Limen…"
        ryn "Et que ça sauve des familles entre deux rations…"
        ryn "Alors peut-être que sans les bons, on pourrait faire pareil, mais en mieux."
        ryn "Sans crever de faim en attendant Kami."

        hide lysa
        $ showP("sael", "mefiant", 0.50)  # centre – retour
        sael "C’est déjà le cas."
        sael "On survit."
        sael "On peut faire plus que survivre."

        think "Ryn baisse les yeux. Kael recalcule. Le troc existe déjà ; l'idée trouve une prise."

        # Modifs adhésion : on cible surtout Ryn et Kael (positif = POUR le changement)
        $ debat_day3_apply_influence({
            "ryn": 2,         # convaincu que Limen survivrait grâce au troc existant
            "kael": 2,        # rassuré : échanges sans chaos ni punition orbitale
            "julian": 1,      # adore la preuve d’autonomie
            "sael": 1,        # favorable, voit le surpassement
            "lysa": -1        # blasée, craint les dérives
        })

        hide ryn
        hide sael

    return

label _3_VOTE_POUR:

    scene bg_conclave at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    play music "music/bgm_victory_bitter.mp3" fadein 2.0  # ambiance triomphale mais pesante, avec une note sombre

    pause 1.2

    $ interject("ADOPTÉ", color="#5DFF9A")

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with vpunch
    kami "VERT !"
    kami "Le vote est POUR !"
    kami "Suppression totale des bons de rationnement. Fin de la distribution gratuite."
    kami "Le commerce, le transport et le stockage de marchandises sont désormais autorisés."
    kami "Félicitations, mes petits rebelles. Vous avez coupé la laisse."
    kami "Mais attention… la laisse, c’était aussi une sécurité."
    kami "On va voir ce que ça donne sans filet. J’ai hâte du spectacle."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    think "L'écran s'éteint. Aucun cri de joie. Nous n'avons pas gagné ; nous avons changé les règles."

    $ showP("julian", "sourire", 0.50)  # centre
    julian "C'est fait. Le collectif vient de créer une chance réelle."

    $ showP("elen", "joie", 0.88)  # droite
    elen "On va pouvoir choisiiir. Vraiment choisir."

    $ showP("ryn", "jaloux", 0.12)  # gauche
    ryn "Ouais…"
    ryn inquiet "Mais sans les bons, Limen va morfler au début."
    ryn "Faut pas se mentir."

    hide julian
    $ showP("noam", "raison", 0.50)  # centre
    noam reflexion "Je me demande si on savait vraiment ce que ça voulait dire."
    noam "Il me semble qu'on ne pouvait plus rester comme avant. Mais... est-ce que c'était vraiment un choix ?"

    hide elen
    $ showP("mara", "rire_profond", 0.88)  # droite
    mara "Génial. On va enfin pouvoir acheter des trucs."
    mara taquin "Enfin… au moins, on va crever en ayant le choix de la sauce."

    hide ryn
    $ showP("kael", "mefiant", 0.12)  # gauche
    kael "Orbite tiendra si les protocoles de sécurité restent intacts."
    kael triste "Si."

    hide noam
    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Qu'allons-nous faire des conséquences ? Le vote ne les gérera pas à notre place."

    think "Julian sourit trop fort. Elen rayonne et tremble. Ryn fixe le sol. Kael compte ses respirations."
    think "Personne n'exulte. Le plus dur commence maintenant."

    hide nyra
    hide kael
    hide mara

    think "17 h 10. Nous nous levons en silence."

    scene bg_couloir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent jusqu'à ma chambre."

    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Nous avons voté pour le changement. Je ne sais pas si nous sommes prêts à le vivre."

    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit. Demain sera différent. Pas nécessairement meilleur."

    $ phase3_over = True
    $ vote1 = "OUI"

    #jump patreon_ending

    call end_day("4") from _call_end_day_3

    jump _4_1_REVEIL_CHAMBRE

label _3_VOTE_CONTRE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    play music "music/bgm_system_override.mp3" fadein 2.0  # ambiance sombre, pesante

    pause 1.2

    $ interject("REJETÉ", color="#FF4D6D")

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "ROUGE !"
    kami "Le vote est CONTRE !"
    kami "Le statu quo est donc maintenu. Les bons de rationnement restent. La distribution continue."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Que je n'entende plus personne râler sur ces bons !"
    kami "Vous aviez la possibilité de changer le système."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Félicitations, mes petits rats sages. Vous avez choisi la sécurité… Bien que c'est un peu plus ennuyeux."
    kami "Je suis presque déçue. J’espérais un peu plus de sang et de chaos."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    play music "music/bgm_low_tension.mp3" fadein 2.0  # ambiance sombre, pesante
    think "L'écran s'éteint. Le rejet tombe sur nos épaules."

    $ showP("julian", "colere", 0.50)  # centre
    julian "Non. Le collectif avait une chance réelle de changer les choses."

    $ showP("ryn", "fatigue", 0.12)  # gauche
    ryn "Ce n'est pas si simple que ça, d'autres auraient pu en souffrir."

    $ showP("mara", "colere", 0.88)  # droite
    mara "On a juste repoussé l’inévitable !"
    mara "On va continuer à crever à petit feu, SU-PER."

    hide julian
    $ showP("elen", "triste", 0.50)  # centre – remplace Julian
    elen "Je… je croyais qu’on allait y arriver…"
    elen "J’étais tellement sûre…"

    hide ryn
    $ showP("kael", "doute", 0.12)  # gauche
    kael "Au moins… On est déjà habitué à ce quotidien."
    kael "Rien ne change, ça ne s'aggrave pas. C'est déjà ça."

    hide mara
    $ showP("nyra", "raison", 0.88)  # droite
    nyra "Qui a voté contre n'a pas choisi l'inaction. Il a choisi le risque connu."

    think "Les voix montent. Julian se lève et frappe la table. Sa performance vient de perdre son public."

    hide elen
    $ showP("julian", "colere", 0.50)  # centre – retour
    julian "Rationnelle ?!"
    julian "Vous appelez ça rationnel ? Continuer à rationner des miettes pendant que les districts crèvent ?!"
    julian "On a eu une chance et on l’a laissée filer !"

    hide kael
    $ showP("ryn", "colere", 0.12)  # gauche
    ryn "C'est le vote, c'est comme ça."
    ryn "Je le comprends. T’as vu ce que ça risquait pour Limen ?!"

    julian "Et t’as vu ce que ça risque si on change rien ?!"

    ryn "Assieds-toi !"
    mara "Les riches survivront encore, quelle surprise !"
    noam "Ce que j'entends— enfin, attendez ! Un par un !"

    think "Presque 17 h. La journée est finie. Le vote aussi. Rien n'a changé."

    think "Je me lève. Les voix continuent sans moi. Je veux rentrer et ne plus réfléchir."

    hide julian
    hide ryn
    hide nyra

    scene bg_couloir at adaptive_fullscreen with dissolve
    think "Mes pas résonnent dans les couloirs froids."
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "Je m'effondre sur le lit."

    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Le silence est pire que les cris. Tout a échoué."
    think "Qu'est-ce qu'on peut faire maintenant ?"

    $ phase3_over = True

    $ vote1 = "NON"

    #jump patreon_ending

    call end_day("4")

    jump _4_0_REVEIL_CHAMBRE

# Durée : 1m20
# Total : 1h 54m 0s

