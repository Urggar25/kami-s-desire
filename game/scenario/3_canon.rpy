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

    think "Je suis réveillé. Je crois. Mon dos et mes épaules, eux, ont déjà voté contre cette journée."
    think "Est-ce que j'ai dormi, ou seulement fermé les yeux jusqu'au matin ?"
    think "Aujourd'hui : le vote. Un seul non, et tout s'arrête."
    think "Douze districts suspendus à une syllabe. C'est presque élégant, si on oublie que c'est monstrueux."

    pause 0.5

    scene bg_cg012 at adaptive_fullscreen with fade

    think "Je fixe le plafond blanc, lisse, propre."
    $ blink()
    think "Trop propre."
    $ blink()

    pause 0.5

    think "Dans le couloir, les pas traînent. Personne ne court. Personne ne parle fort."

    pause 0.6

    play sound sfx_announce
    pause 1.0

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Booooonjour mes petits représentants ♥"

    pause 0.4

    kami "Jour trois !"
    kami "Déjà fatigués ?"

    pause 0.4

    kami "Petit rappel doux et adorable :"
    kami "Aujourd’hui, c’est le jour de vote."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Unanimité absolue."
    kami "Un seul petit non, et… pfiou."

    pause 0.4

    kami "On efface tout."
    kami "On recommence, et tant pis pour la proposition."

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'un d'entre vous se sera creusé les méninges pour rien !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Alors souriez bien."
    kami "Et méfiez-vous un tout petit peu les uns des autres."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ça met du piment~"
    kami "Et j'adore ça !"

    pause 0.4

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à 14h ♥"

    pause 0.3

    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "Elle adore appuyer là où ça fait mal."
    think "Un seul non. Qui le prononcerait ? Personne n'y a intérêt."
    think "Alors pourquoi mon ventre prépare déjà la chute ?"

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with fade
    think "Je me redresse, allume. Mes vertèbres protestent."

    call day3_play_wakeup_trace from _call_day3_play_wakeup_trace

    pause 0.4

    think "Super."

    pause 0.4

    think "Peau froide. Mâchoire serrée."

    pause 0.5

    think "Respirer."
    think "Une étape à la fois."

    pause 0.5

    pause 0.4

    think "Le métal froid sous mes pieds achève de me réveiller."

    pause 0.5

    think "Ça réveille."

    pause 0.4

    think "Deux gorgées d'eau. La gorge reste nouée, l'appétit absent."

    menu:
        "Attraper le téléphone posé près du lit.":
            think "Je le prends du bout des doigts. L'écran s'allume avant que je le demande."
        "Le laisser encore une seconde.":
            think "Je le fixe. Le rappel du vote attend derrière le verre noir."
        "Le ranger dans ma poche.":
            think "Je le glisse dans ma poche. Son poids suffit à rappeler l'heure."

    call screen day3_phone_vote_notice
    if _return == "codex":
        call screen day3_current_vote_codex(called=True)

    show screen day3_codex_logo

    pause 0.5

    think "Mais il faut quand même que j'aille à la cafétéria."

    pause 0.5

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    think "Le couloir est étrangement calme. Même la ventilation semble retenir son souffle."

    pause 0.5

    think "Deux silhouettes ralentissent en m'entendant, puis reprennent."

    pause 0.5

    think "On se surveille sans le dire."

    pause 0.4

    think "Je croise Kael au détour du couloir."

    $ showP("noam", "neutre", 0.20)
    $ showP("kael", "fatigue", 0.65)

    kael fatigue "Salut."

    think "Sa voix est plus basse que d'habitude."

    noam "Tu vas à la cafétéria ?"

    kael reflechit "Oui."
    think "Il reste immobile une seconde de trop."

    kael inquiet "Tu es sûr que c’est une bonne idée ?"

    noam "Le commerce ?"

    kael reflechit "Oui. Tout le monde minimise les effets."
    kael inquiet "Ils ne seront pas minimes."

    think "Il évite mon regard."

    noam "Tu penses que ça peut vraiment déraper ?"

    kael culpabilite "Je ne sais pas."
    kael fatigue "Nous modifions les règles avant de savoir fonctionner ensemble."

    think "Ni oui, ni non. Exactement l'espace où Kael se sent encore en sécurité."

    noam "Tu veux voter contre ?"

    kael surpris "Non."
    kael reflechit "Je suis pour. En théorie."

    think "En théorie. Deux mots capables de cacher un vote entier."

    kael reflechit "Changer, c'est renoncer au retour arrière."

    think "La ventilation paraît soudain plus forte. Pour Kael, ce bruit n'est jamais neutre."

    kael inquiet "Tu n’as pas peur ?"

    noam "Si."
    noam "Mais ne rien changer, c’est aussi un choix."

    think "Il baisse les yeux."

    kael fatigue "Je déteste décider sans données."

    think "Il pourrait basculer."

    kael calme "On verra à 14h."
    kael sourire "Bonne chance."

    think "Il me frôle en passant. Il n'a pas tranché, et mon estomac le sait."


    hide noam
    hide kael

    think "Je continue."

    pause 0.5

    think "Julian tapote le distributeur comme si la machine lui devait un service."

    $ showP("noam", "neutre", 0.30)
    $ showP("julian", "joie", 0.75)

    julian joie "Noam. Prêt à ouvrir la première brèche dans ce système ?"

    think "Son sourire est déjà prêt pour la rediffusion."

    noam "On va essayer."

    julian rire "Essayer ? Non. Nous allons le faire."
    julian "Julian ne monte pas sur scène pour annoncer une tentative."

    think "Il attrape sa tasse. Le café déborde ; sa mise en scène, elle, reste intacte."

    julian reflexion "Si ce texte passe, nous ouvrons la première brèche depuis la prise de pouvoir de Kami."
    julian joie "Commerce. Échanges. Mouvement. L'Histoire retiendra un commencement."

    think "Ses yeux brillent. Il aime autant l'idée que la place qu'elle lui offre."

    noam "Et si ça ne passe pas ?"

    julian hesitation "Ça passera."
    julian sourire "Nous ferons en sorte que ça passe."

    think "Il appuie trop fort sur « nous »."

    julian reflexion "Nous ne sommes pas ici pour maintenir le statu quo."
    julian idee "Les gens veulent un changement visible. Nous avons la responsabilité de l'incarner."

    think "Il redresse les épaules. Il se voit déjà dans l'après."

    noam "Tu es sûr que tout le monde suivra ?"

    julian hesitation "…"

    think "Une microseconde. Son sourire manque une marche."

    julian sourire "Ils suivront. Certains ont simplement besoin que quelqu'un formule leur courage à leur place."

    think "Il me regarde droit dans les yeux. La caméra est juste derrière moi."

    julian reflexion "C'est le commerce. Personne ne votera contre une évidence pareille."

    think "Il y croit. Ou il sait très bien jouer quelqu'un qui y croit."

    julian sourire "Imagine : des ressources qui circulent, des districts qui échangent, des idées qui bougent."
    julian idee "Comme avant. Ce tableau ne te parle pas ?"

    think "Il accélère, comme si le résultat était déjà officiel."

    noam "Je crois que... oui. Dit comme ça, sur le papier... ça me plaît."

    "Mais son enthousiasme me met mal à l’aise."

    julian reflexion "Le collectif a besoin d'un élan. À nous de le provoquer."

    think "Il boit, grimace. Même le mauvais café n'était pas prévu."

    julian sourire "À quatorze heures, Julian ouvre le bal. Et nous changeons ce monde."

    call day3_collect_vote_argument("monde_avant") from _call_day3_collect_vote_argument_monde_avant

    think "Il s'éloigne trop vite. Il veut que le texte passe pour le monde — et pour son histoire à lui."

    hide noam
    hide julian

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    pause 0.5

    think "Les conversations sont basses. Trop basses."

    pause 0.6

    think "On fait semblant d’être normaux."

    pause 0.5

    think "Ryn murmure avec Elen. Mara fixe un écran mort. Iris tient une tasse pleine."

    pause 0.6

    think "Tout le monde calcule."

    pause 0.5

    think "Qui voterait contre ? Mara ? Non. Sael ? Elle serait frontale."
    think "Ou je me raconte exactement l'histoire qui m'arrange. C'est ça, le pire : le doute trouve toujours une voix crédible."

    pause 0.6

    menu:
        "Prendre un café noir.":
            think "Le café est plus amer que d'habitude. Ou c'est moi."
        "Prendre une barre de céréale.":
            think "La barre colle aux doigts. Je la garde sans vraiment manger."
        "Prendre seulement de l'eau.":
            think "L'eau froide descend dans ma gorge sans desserrer mon ventre."

    pause 0.5

    think "Un seul non, et nous prouvons qu'on ne sait pas s'entendre."
    think "Respire. Aujourd'hui, on décide si nous sommes un groupe ou seulement douze personnes enfermées ensemble."

    pause 0.8

    jump _3_CAFETERIA_DEBAT

# Durée : 3m45
# Totale : 1h 27m 55s

label _3_CAFETERIA_DEBAT:

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "La cafétéria est pleine, mais le brouhaha se limite aux fourchettes, aux chaises, aux souffles."

    pause 0.4

    menu:
        "S'asseoir près du bord de table.":
            think "Je choisis le bord. Pas au centre. Pas trop visible."
        "Rester debout quelques secondes.":
            think "Je reste debout, plateau en main, puis choisis une place discrète."
        "Poser le téléphone face contre table.":
            think "Je retourne le téléphone. L'écran disparaît. Le vote reste."

    pause 0.3

    $ showP("noam", "neutre", 0.82)
    $ showP("elen", "joie", 0.22)
    $ showP("iris", "fatigue", 0.50)

    think "Elen et Iris sont côte à côte, comme si la table avait choisi pour elles."

    pause 0.3

    scene bg_cg013 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg013")

    think "Elen protège un bol énorme et fumant. L'odeur hésite entre la forêt et le dessert."

    pause 0.3

    iris "C'est quoi, ce crime culinaire ?"

    elen rire "C'est. Une. Masterpiiiiece."

    iris "Ce mot ne s'applique déjà pas souvent. Ici, c'est une fraude."

    elen joie "Pâtes, noix et... un petit truc secret."

    iris "Un petit truc secret, c’est exactement comme ça qu’on finit à l’infirmerie."

    elen rire "T’inquiète."
    elen rire "C’est Goumi qui a validé."
    elen taquin "Goumi ne tue pas ses clients. Enfin, pas volontairement !"

    iris desaccord "… C’est pas rassurant."

    pause 0.3

    think "Elen mélange, goûte. Ses yeux s'illuminent."

    elen joie "Oh ! C'est trooop bon ! Exactement trop bon !"

    iris "Tu essaies de nous convaincre ou de survivre à la première bouchée ?"

    elen taquin "J'ai le droit d'être heureuse, nooon ? Tu devrais essayer !"

    iris fatigue "Ça me fatigue rien que de te regarder."

    pause 0.3

    think "Son rire tranche la pièce en deux : son bol d'un côté, le vote de l'autre."

    elen rire "Goûte ! Une bouchée ! Pour l'art !"
    elen taquin "Pour l’art. Tu es bien courageuse non ?"

    iris "Non."

    elen surpris "Même pas pour la postérité ?!"

    iris "Surtout pas..."

    pause 0.3

    think "Elen hausse les épaules et récupère sa bouchée."

    elen content "Ok."
    elen content "Plus pour moi."
    elen content "C-ça... m'va..."

    pause 0.4

    think "Mon plateau se limite à une barre et un jus. La nausée tient le reste de la place."

    pause 0.3

    noam "Goumi t’a laissé commander ça ?"

    elen joie "Ouaiiiis."
    elen joie "J'lui ai fait ce regard."

    scene bg_cg013_1 at adaptive_fullscreen with fade
    think "Elle compose un regard si calculé qu'il pourrait avoir sa propre notice."

    elen taquin "Le regard ultiiime !"

    iris "Le regard du caprice, oui."

    elen rire "Le regard du caprice, c'est mignon ! Je me suis entraînée !"

    scene bg_cg013 at adaptive_fullscreen with fade
    pause 0.3

    think "Iris surveille le bol comme un prototype instable."

    iris "On dirait des pâtes…"
    iris "Avec des cailloux."

    elen "C’est des noix."

    iris "Oui. Avec des cailloux, la texture serait peut-être plus cohérente."

    elen taquin "Ah ouais, tu crois ?"

    iris desaccord "C'était du sarcasme, Elen. Ne mange pas de cailloux. Je refuse de remplir ce rapport d'incident."

    pause 0.3

    think "Elen mâche les yeux fermés, parfaitement indifférente au volume de son bonheur."

    iris fatigue "…"

    elen joie "Tu vois ?"
    elen joie "La vie, c'est ça ! Profiter et s'en foutre de ce que les autres pensent !"
    elen taquin "Comme ça, rien ne t'atteint."

    iris "Tu dis ça comme si c’était normal."

    elen "Ça devrait en tout cas."

    pause 0.5
    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showP("noam", "neutre", 0.82)
    $ showP("elen", "joie", 0.22)
    $ showP("iris", "fatigue", 0.50)

    iris "T’as pas peur."
    iris "Deux secondes ?"

    elen "Si."
    elen "Mais là, maintenant, tout de suite, j’ai faim."
    elen joie "Alors je m'en fou d'avoir peur."

    iris "…"

    pause 0.3

    think "Iris détourne les yeux. Pour une fois, son sarcasme n'arrive pas."

    pause 0.4

    $ showP("elen", "taquin", 0.22)

    elen taquin "T’as envie de me faire la morale, hein."

    iris "Un peu."

    elen rire "Vas-y."
    elen rire "Je t’écoute."
    elen taquin "Héhé, balance ton sermon."

    iris fatigue "Non."
    iris fatigue "Laisse tomber."

    pause 0.4

    think "Une chaise racle derrière nous. Personne ne regarde."

    pause 0.4

    hide noam
    $ showP("elias", "neutre", 0.82)

    think "Elias arrive avec un plateau triste, propre, calibré."

    pause 0.3

    elias "Wsh, vous mangez quoi ?"

    elen joie "Le bonheur."

    iris "Ne la crois surtout pas..."

    elias inquiet "…"
    elias inquiet "Faut manger correctement. Surtout aujourd'hui."

    elen taquin "Oh non."
    elen taquin "Le discours nutrition."

    elias "Je plaisante pas."

    iris "Il plaisante jamais."
    iris taquin "Crois moi. Ca c'est vrai."

    elias "Protéines, œufs, poulet. Simple. Efficace."

    pause 0.3

    think "Elen le regarde comme s'il venait de recommander l'eau tiède pour le plaisir."

    hide elen
    $ showP("elen", "surpris", 0.22)

    elen "Poulet."
    elen "Ici."
    elen "Alors que tu peux manger tout ce que tu veux ?!"

    elias "C'est une base. Ça tient au corps. Mais ton truc là... c'est chaud."

    iris "Merci."

    elen colere "Oh !"
    elen colere "C’est pas des pâtes aux noix."
    elen colere "C’est une œuvre d'art gustative."

    elias "Franchement, j'en doute."

    elen "Ça dépend laquelle."

    pause 0.3

    think "Elias soupire et ravale la suite."

    hide elias
    $ showP("elias", "reflechit", 0.82)

    elias "Cet aprèm, faut être lucides. On peut pas arriver mous."
    think "Il pousse son œuf comme s'il regrettait déjà son propre conseil."

    pause 0.3

    hide iris
    $ showP("iris", "hesitation", 0.50)

    iris "…"

    elen "On devait pas en parler."

    elias "Personne veut en parler."
    elias "C’est pour ça que ça tourne dans les têtes."

    pause 0.4

    think "Elen remange moins bruyamment. Elle écoute."

    pause 0.3

    iris "On n’est pas obligés."
    iris "Là."
    iris "Maintenant. On est en train de manger."

    elias "On fait quoi alors ? On arrive et on improvise ? C'est chaud comme plan."

    elen "Bon vu que vous me cassez les pieds avec ça."
    elen "Moi, je vais pas improviser."
    elen "Je sais déjà ce que je vais faire."

    pause 0.3

    think "Elen bondit presque de sa chaise."
    $ showP("elen", "joie", 0.22)

    elen joie "Je vote pour !"

    pause 0.4

    think "Elle l'annonce comme un dessert de mariage. Aucune hésitation visible."

    iris "Tu le dis facilement."

    elen taquin "Parce que c'est facile. Ici on crève d'ennui, dehors ils crèvent pour de vrai."
    elen inquiet "Enfin... c'est pas drôle. Vous avez compris."

    iris "…"

    elias "Tu marques un point."

    pause 0.4

    think "Le silence voudrait rester entier. Julian le casse."

    pause 0.3

    hide elias
    $ showP("julian", "neutre", 0.82)

    think "Julian attrape une chaise avant que le sujet puisse lui échapper."

    julian "J'ai entendu « je vote pour » ?"

    elen rire "Oui."
    elen rire "Bienvenue au club !!"

    julian sourire "Évidemment. Julian vote pour."

    iris hesitation "Julian…"

    julian "Quoi ?"
    julian "Je ne vais pas cacher une position aussi évidente. Le collectif a besoin de clarté."

    think "Julian vérifie la caméra. Réflexe. Sourire intact."

    pause 0.3

    think "Toute la salle regarde maintenant dans notre direction. Elen sait fédérer, même par accident."

    pause 0.3

    elen taquin "Ok."
    elen taquin "Question simple."
    elen taquin "Qui vote pour ?"

    pause 0.4

    think "Julian lève la main comme si une caméra attendait précisément ce plan."

    julian rire "Pour."

    pause 0.3

    hide julian
    $ showP("noam", "hesitation", 0.82)

    think "Les regards attendent ma réponse sans encore m'accuser."

    noam "Tu votes pour... sans 'mais' ?"
    think "Elen hausse les épaules. Pour elle, c'est évident."
    think "Et moi ? Si c'était si simple..."
    noam "Et si le texte est foireux ?"

    pause 0.3

    elen "Nooon ! Il faut voir le bon côté !"

    hide elen
    $ showP("elen", "content", 0.22)

    elen content "Voilà."
    elen content "Ça fait déjà du bien."

    iris fatigue "Une seule voix contre suffit. L'enthousiasme n'est pas une stratégie de vote."

    pause 0.3

    think "Elias hoche la tête une fois."

    hide noam
    $ showP("elias", "determine", 0.82)

    elias "Pour. Mais faut que ça soit vraiment appliqué. Sinon c'est chaud de voter pour du vent."

    elen taquin "Ça y est."
    elen taquin "Le “mais” est arrivé."
    elen rire "Je l’attendais."

    elias "Je suis sérieux."

    iris "Lui aussi."

    pause 0.4

    think "Les autres approchent par petites vagues, sans vouloir admettre qu'ils écoutent."

    pause 0.3

    hide elias
    $ showP("kael", "neutre", 0.82)

    think "Kael tente de passer avec son plateau. Elen lui barre la route."

    pause 0.4

    elen "Kael ?"
    elen "Pour ou contre ?"

    pause 0.4

    hide kael
    $ showP("kael", "reflechit", 0.82)

    think "Kael mesure le poids du mot avant de le lâcher."

    kael "…"
    kael "Je ne sais pas. Je déciderai au vote."

    pause 0.3

    elen "Ok."
    elen "Réponse honnête."

    iris "Au moins."

    pause 0.4

    hide kael
    $ showP("mara", "mefiant", 0.82)

    think "Mara arrive, inspecte les plateaux puis les visages."

    mara "On vous entend de loin. Annoncer vos votes devant les caméras, c'est audacieux."
    mara taquin "Ou généreux. Vous facilitez le travail de tout le monde."

    elen rire "Oh non."
    elen rire "On est démasqués."

    mara mefiant "Je rigole pas."

    pause 0.3

    iris "Tu votes pas pour ?"

    mara "J'ai pas dis pas ça."

    pause 0.3

    think "Elle prend une chaise sur le bord, avec une sortie dans son champ de vision."

    hide mara
    $ showP("mara", "doute", 0.82)

    mara "Je comprends l'idée. Mais on ouvre une porte sans voir derrière."
    mara taquin "D'habitude, j'aime les surprises. Celles qui concernent des millions de gens, un peu moins."

    elen "C’est du commerce."
    elen "C'est pas comme si on proposait l'éradication des bébés pingouins !"

    mara doute "T’es sûre ?"

    pause 0.4

    iris "Mara…"

    mara "Non."
    mara "Laissez."
    mara "Je dramatise pas. Je demande ce qu'on n'a pas compris."
    mara "Où est le texte exact ? Je veux le voir avant de signer quoi que ce soit."

    pause 0.3

    think "Elen se redresse, prête à répondre trop fort, puis se retient."

    hide elen
    $ showP("elen", "reflexion", 0.22)

    elen "Ok."
    elen "Je t’entends."
    elen "Vraiment."
    elen "Mais…"
    elen "On fait quoi sinon ?"
    elen "On regarde les gens crever et on se dit que c'est pas de notre faute ?"

    mara "Je dis pas ça."

    pause 0.3

    think "Mara serre la mâchoire."

    hide mara
    $ showP("mara", "stress", 0.82)

    mara "Je ne suis pas contre par principe. Je suis réticente."
    mara "Si ça tourne mal, c'est nous qui payons. Pas Kami. Nous."
    think "Ses jointures blanchissent sur le plateau. Le show vient de s'arrêter."

    pause 0.4

    noam "Tu veux des garanties."

    mara "Oui."

    iris "Et si on en a pas ?"

    mara "Alors je veux que la proposition ne soit pas ambigüe."

    pause 0.4

    elen taquin "Ok."
    elen taquin "Donc t’es pas contre, tu vas voter pour."

    mara stress "Je te jure…"

    elen rire "Je plaisante."

    pause 0.4

    think "Le bruit de la cafétéria revient. Les gens recommencent à respirer."

    pause 0.3

    think "Quelques têtes approuvent. Les autres esquivent. Un consensus mou penche vers le pour."

    pause 0.4

    think "Kael mange sans regarder personne."

    pause 0.3

    iris "On va pas tout régler ici."

    elias "Non."

    hide mara
    $ showP("julian", "neutre", 0.82)
    julian "Au moins, le collectif penche vers le pour."

    elen joie "Ça me suffit pour le moment."

    call day3_collect_vote_argument("enonce_precis") from _call_day3_collect_vote_argument_enonce_precis

    pause 0.3

    think "Elen pousse son bol vide avec la satisfaction d'une mission accomplie."

    hide elen
    $ showP("elen", "content", 0.22)

    elen content "Ok."
    elen content "Je vais aller digérer mon œuvre."
    elen taquin "Et peut-être convertir d’autres âmes à ma bonne humeur."

    iris "Bonne chance."

    elen rire "Merci."
    elen rire "Hé hé, Je suis née pour ça."

    pause 0.4

    "Julian se lève aussi."

    hide julian
    $ showP("julian", "sourire", 0.82)

    julian "Julian va consolider ce premier accord."

    pause 0.4

    think "Elias récupère son plateau et le suit."

    hide julian
    $ showP("mara", "neutre", 0.82)
    mara "Ouais."

    pause 0.4

    think "Mara se lève, toujours sur le bord du groupe."

    mara "Je vais vérifier deux trucs."
    mara "Rien de grave."
    mara "Juste…"
    mara "Désolée d'avoir cassé l'ambiance. D'habitude, c'est plus volontaire."

    iris "T'inquiète. C'est pas toi qui est en cause..."

    mara "Merci."

    pause 0.4

    think "Kael finit et se lève sans commentaire."

    pause 0.4

    hide kael
    hide elias
    hide mara
    hide elen
    hide julian

    $ showP("noam", "neutre", 0.82)
    $ showP("iris", "fatigue", 0.50)

    think "Il ne reste qu'Iris et moi."

    pause 0.3

    iris fatigue "Tu vois."
    iris fatigue "Même quand personne veut en parler…"
    iris fatigue "On finit toujours par le faire.."

    noam "Ouais."
    think "Ma barre s'effrite entre mes doigts."

    pause 0.3

    iris "Fais attention tout à l'heure."

    noam "Toi aussi."

    pause 0.4

    think "Elle hoche la tête et part."

    hide iris

    pause 0.4

    think "La salle reste pleine, silencieuse, vivante malgré tout."

    pause 0.4

    think "Une respiration."
    think "Avant la suite."

    pause 0.4

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

    think "La porte claque derrière moi. Le choc résonne dans ma cage thoracique, pas seulement dans la pièce."

    play sound sfx_door
    think "Je reste dos au battant. Mon cœur cogne comme s'il voulait sortir avant moi."

    pause 0.3

    think "On vote pas avec des idées."
    think "On vote avec nos nerfs."

    think "La chambre paraît trop petite. Ou c'est moi qui prends enfin trop de place."

    pause 0.3

    think "Convaincre, c’est pas prouver qu’on a raison."
    think "C’est toucher ce que l’autre protège."
    think "Ce qu’il a déjà perdu. Ce qu’il refuse de perdre encore."

    think "Je m'assois au bord du lit."

    pause 0.4

    think "Vaut-il mieux défendre ses principes ou les gens ?"
    think "Vaut-il mieux voter pour un texte clair ou conserver un statu quo mortel ?"
    think "Clarté. Limites. Traçabilité."

    pause 0.3

    think "Le silence écoute presque les battements de mon cœur."

    pause 0.4

    play sound sfx_knock

    think "Trois coups secs."

    pause 0.2

    play sound sfx_knock

    think "Encore."

    pause 0.2

    nyra "Noam ! Ouvre !"

    think "Je me lève."

    scene bg_dortoir at adaptive_fullscreen with fade

    $ showP("nyra", "stress", 0.65)
    $ showP("noam", "neutre", 0.20)

    nyra stress "Julian fait le tour des indécis."

    noam "Tu l'as entendu ?"

    pause 0.2

    nyra "Tomas, puis deux autres. Il ne défend pas seulement le texte."

    noam "Ce que j'entends, c'est que... tu t'inquiètes de comment il présente les choses ?"

    nyra "Il leur demande quel visage le vote devrait avoir. Puis il propose le sien."

    pause 0.3

    nyra "Qu'est-ce que les hésitants vont entendre : l'amendement, ou sa candidature au rôle de héros ?"

    pause 0.4

    think "Pas le texte."
    think "Lui."

    noam "Où il est ?"

    nyra "Dans la salle de repos."

    stop music fadeout 0.5
    play music "music/bgm_tension_low.mp3" fadein 0.6

    scene bg_couloir at adaptive_fullscreen,memory_idle with fade

    think "Nous nous mettons à courir."

    play sound sfx_run

    think "Mes semelles claquent sur le métal. Chaque pas annonce notre arrivée."

    pause 0.3

    think "Nyra court devant sans regarder derrière."

    pause 0.2

    play sound sfx_run
    think "Les néons défilent. Les caméras semblent pivoter avec nous."

    pause 0.3

    think "Mon cœur tape dans mes tempes. Pas seulement à cause de la course."

    pause 0.2

    think "Un virage sec."
    call day3_play_corridor_trace from _call_day3_play_corridor_trace

    pause 0.5

    think "Sa voix arrive avant la salle. Son rire aussi."

    scene bg_repos at adaptive_fullscreen with fade

    $ showP("julian", "sourire", 0.65)
    $ showP("tomas", "hesitation", 0.35)

    julian sourire "— si Julian prend la parole en premier, le collectif gagne un cap."
    julian sourire "Un visage sûr. Un leader visible. Quelqu'un en qui les gens se reconnaissent."

    tomas hesitation "Je vote pour le texte."
    tomas hesitation "Pas pour un leader."

    julian rire "Un texte sans moteur reste du papier. Julian peut être ce moteur."

    think "Je m'avance."

    $ showP("noam", "determine", 0.85)

    menu:
        "Couper Julian immédiatement.":
            noam hesitation "Julian."
            noam "Je me demande si... c'est vraiment ce qu'on veut mettre en avant."
            think "Son sourire se fige plus vite que prévu."
            nyra stress "Il t'a entendu."
        "Laisser Tomas répondre d'abord.":
            think "Je garde le silence. Tomas serre son poignet."
            tomas hesitation "J-Je ne veux pas que le vote devienne ça."
            noam "Il me semble que Tomas vient de dire l'essentiel."
            nyra stress "Sa limite est claire."
        "S'adresser directement à Tomas.":
            noam "Tomas."
            noam "Tu votes pour un texte, pas pour quelqu'un qui parle plus fort."
            think "Tomas relève les yeux."
            tomas hesitation "Oui. Voilà."
            nyra stress "Le vote revient au texte."

    noam "Il me semble que personne ici n'a de mandat pour se poser en leader."

    pause 0.4

    julian sourire "Ah. Noam."

    pause 0.2

    noam hesitation "Ce que j’entends, c’est que tu veux que ça passe."
    noam "Mais il me semble que si tu te mets trop en avant, les hésitants vont percevoir autre chose."
    noam reflexion "Pas l’idée. Toi."
    noam raison "Et là, le vote ne sera plus sur le fond. Ce sera sur toi."

    pause 0.4

    julian sourire "Tu réduis une stratégie collective à une question d'ego. C'est sévère."

    think "Son sourire glisse une seconde. À peine."

    $ showP("julian", "neutre", 0.65)

    julian "Julian veut que ce texte passe."

    noam "Ce que je veux dire... parle du texte. Rien d'autre."
    noam hesitation "Je me demande si... le reste est vraiment nécessaire."

    pause 0.3

    tomas "Il a raison."

    $ showP("tomas", "determine", 0.35)

    tomas "Si ça ressemble à une démonstration d’ego,"
    tomas "F-Franchement, ç-ça sera sans moi."

    pause 0.4

    $ showP("julian", "decu", 0.65)

    julian "Bon. Très bien."
    think "Son sourire revient sans atteindre ses yeux."
    julian sourire "Nous verrons au Conclave qui porte réellement ce vote."
    julian "Évite simplement de me transformer en antagoniste. Ce rôle est déjà pris."
    think "Il s'éloigne."

    hide julian

    pause 0.5

    stop music fadeout 0.6
    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    $ showP("nyra", "neutre", 0.60)
    $ showP("tomas", "reflechit", 0.35)

    tomas "C’était limite."
    tomas triste "Il était franchement casse pied."
    tomas mefiant "D-Désolé, à cause de moi, v-vous avez du venir m'aider..."

    nyra "Tu as posé ta limite. Il devra en tenir compte."

    pause 0.3

    think "Julian n'est pas contre. Il veut seulement que le vote devienne sa scène. Et ça peut suffire à le faire échouer."

    pause 0.3

    tomas "P-Pour être honnête, je ne veux pas que ce soit lui qui donne le ton."
    tomas "Il faut que quelqu'un puisse lui tenir tête..."
    tomas "T-Tu vas parler tout à l'heure ?"

    noam "Oui."

    pause 0.2

    noam "Mais pas pour briller. Pour essayer que ça avance dans le bon sens."

    pause 0.4

    tomas hoche_la_tete "Alors fais simple."

    nyra "Et clair."

    think "Ils repartent ensemble."

    pause 0.4

    hide tomas
    hide nyra

    $ showP("noam", "determine", 0.75)

    think "Ce vote, c’est plus juste un texte."
    think "C’est aussi une question de confiance."
    think "On ne peut pas faire n'importe quoi, au risque de la briser."

    pause 0.3

    think "Julian n’est pas un ennemi."
    think "Mais son caractère peut causer le pire comme le meilleur."

    pause 0.3

    think "Je serre les poings. Ils tremblent moins qu'avant."

    pause 0.3

    think "Les grands discours, ce n'est pas vraiment pour moi."
    think "Mais je ne peux pas laisser les choses s'envenimer."

    pause 0.3

    think "Je devrais y aller."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite

# Durée : 2m40
# Totale : 1h 37m 05s

# + 1m30 de temps libres
# Totale : 1h 38m 35s

label _3_TRANSITION_CONCLAVE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Le couloir paraît plus sombre, plus étroit."

    pause 0.3

    $ showP("noam", "inquiet", 0.5)

    think "Respire."
    think "C’est juste un vote."

    pause 0.3

    think "Pourquoi est-ce que mon cœur tape comme ça."

    think "Une sueur froide glisse dans ma nuque. Quelqu'un me regarde de trop près."

    pause 0.3

    think "Les caméras."

    think "Les caméras. Évidemment. Pourquoi auraient-elles disparu aujourd'hui ?"

    pause 0.3

    think "Les groupes convergent vers le Conclave en partageant le même silence."

    pause 0.3

    think "Nous ne sommes pas synchronisés. Seulement obligés. Ça suffit à donner une cadence militaire."

    pause 0.3

    think "Elias serre les poings. Julian marche trop vite avec un sourire figé."

    pause 0.3

    think "Mara vérifie encore son poignet. Tomas compte à voix basse."

    pause 0.3

    think "On dirait une salle d’attente."
    think "Sauf que personne ne sait ce qu’on attend exactement."

    pause 0.4

    $ showP("lysa", "neutre", 0.25)
    $ showP("noam", "inquiet", 0.75)

    think "Lysa marche légèrement en retrait. Juste assez pour que ça se voie."

    pause 0.3

    think "Le groupe accélère quand le couloir se resserre. Elle, non."

    pause 0.3

    think "Même rythme, lent et délibéré."

    pause 0.3

    menu:
        "Ralentir pour marcher près de Lysa.":
            think "Je ralentis et me cale sur son pas."
        "Rester avec le groupe.":
            think "Je reste avec le groupe, mais mon regard revient vers elle. Je ralentis."
        "Regarder Julian avant d'entrer.":
            think "Julian avance trop droit, trop vite. Je reviens au rythme de Lysa."

    pause 0.3

    think "Elle le sent."

    $ showP("lysa", "reflexion", 0.25)

    think "Elle tourne la tête. Ni sourire ni attaque. Seulement de la fatigue."

    pause 0.3

    $ showP("lysa", "triste", 0.25)

    lysa "On va voter. On va échouer."
    lysa "La République de Weimar aussi croyait qu'une procédure pouvait tenir le chaos. Et alors ?"

    pause 0.3

    lysa "Demain, mêmes murs, même pression. Puis on recommence dans trois jours."

    pause 0.6

    think "Elle ne me parle pas vraiment. Elle récite une conclusion déjà prononcée dans sa tête."

    pause 0.5

    think "Elle y croit vraiment. Pas à l'espoir. À son contraire."

    pause 0.4

    $ showP("julian", "hesitation", 0.9)

    think "Julian l'a entendue. Son sourire se crispe ; il accélère."
    hide julian

    pause 0.3

    $ showP("mara", "stress", 0.5)

    think "Mara serre les lèvres. Son silence fait plus de bruit que son rire."
    hide mara

    pause 0.5

    think "Le couloir s'alourdit jusqu'aux néons."

    pause 0.4

    think "Parmi ceux qui l'ont entendu, personne ne l'a contredit."
    think "Comment le pourrions-nous ?"
    think "Personne ne sait ce qu'il va se passer."

    think "Devant la salle, Sael prend Lysa dans ses bras. Sans demander."

    pause 0.3

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    think "Bref. Sans théâtre."

    pause 0.4

    think "Ses bras se referment solidement autour d'elle."

    pause 0.3

    think "Lysa se fige, comme si son corps n'avait aucune réponse préparée."

    pause 0.4

    sael "Tu as le droit d'être fatiguée."
    sael "Ma grand-mère disait que même les morts se reposent avant de revenir dans nos rêves."

    pause 0.5

    think "Sa voix reste basse, posée."

    pause 0.4

    sael "On a besoin de ta lucidité. Pas d'une autre Lysa. De celle qui est là."

    pause 0.3

    think "Les épaules de Lysa se détendent à peine."

    pause 0.3

    lysa "Tu dramatises."
    lysa "Je suis toujours là."

    pause 0.4

    sael "Alors montre-le."

    pause 0.4

    think "Sael la relâche sans s'éloigner complètement."

    pause 0.3

    sael "Tu vois des failles que je ne vois pas. C'est pénible. Et utile."

    pause 0.5

    think "Lysa sourit légèrement."

    pause 0.3

    lysa "Si je sauve le débat, tu me dois un café. Les oracles se faisaient mieux payer."

    pause 0.3

    sael "Deux. Ici, personne ne paie. C'est peut-être un signe."

    pause 0.4

    think "Elles se séparent devant la porte."

    pause 0.3

    think "Lysa redresse le menton. Elle ne croit peut-être pas au système. Elle vient au moins de décider de lui répondre."

    scene bg_conclave at adaptive_fullscreen with dissolve

    think "La salle est prête : sièges, pupitres, caméras. Le piège a fait son lit."

    pause 0.3

    voix "Diffusion active."

    play sound sfx_announce
    pause 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous voilà tous ! Manquera-t-il quelqu'un ?"
    kami "Mes chers téléspectateurs, nous le saurons dans un instant !"

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

    think "Les portes se referment derrière nous."

    play sound sfx_door

    pause 0.5

    think "Nous gagnons nos sièges. Le Conclave commence."
    think "Plus de retour en arrière possible."

    #jump patreon_ending

# Durée : 2m55
# Totale : 1h 40m 00s

label _3_DEBAT1_PHASE1:
    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "C'est bon tout le monde est installé ?"
    kami "C'est TROOOP LOOONG !!"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bon on va commencer cette première phase en douceur."
    kami "Vous allez devoir poser les bases."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Avant de vous arracher les cordes vocales, vous allez devoir reconstruire le texte ensemble."
    kami "Il faut que vous sachiez de quoi vous parlez non ?!."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ne faites pas les mêmes erreurs que les anciens politiciens qui ont conduit le monde à sa ruine !"

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn "Attends comment ça reconstruire le texte ensemble ?!"
    ryn "C'est quoi ce bordel ?!"
    $ bc_hide()

    kami "Non mais attends ! Tu ne penses tout de même pas que je vais faire le travail à TA place ?!"
    kami "J'ai un monde entier à gérer, je suis très occupée moi !"

    $ bc_show("sael", "reflechit", px=-70, py=-50, pz=0.85)
    sael "Donc ça veut dire qu'on a même pas la base écrite de l'amendement ?"
    sael "Comment on va faire pour en débattre sans ça ?!"
    $ bc_hide()

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mon dieu, je savais qu'en prenant des jeunes il aurait fallu tout expliquer !"
    kami "Zen... Tu t'y étais préparée..."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ne vous en faites pas, je sais que vous n'avez PAS de mémoire..."
    kami "Alors pour vous aider, mais pas trop, j'ai réarrangé les mots de l'amendement déposé..."
    kami "Et..."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Pour pimenter le tout j'y ai ajouté quelques mots !"
    kami "Histoire de voir vos débats !"

    $ bc_show("lysa", "colere", px=-70, py=-50, pz=0.85)
    lysa "C'était évidemment trop beau !"
    lysa "Avoir un amendement qui autorise le commerce, c'était trop simple !"
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
    kami "J'espère que vous vous rappelez vos règles de construction de phrase."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showP("ryn", "determine", 0.18)
    ryn "Elle pouvait pas nous les donner directement dans l'ordre ?!"
    ryn "Sérieusement, pourquoi elle fait ça ?!"

    $ showP("sael", "mefiant", 0.82)
    sael "Va falloir qu'on s'y mette si on veut avancer."

    hide ryn
    $ showP("nyra", "raison", 0.50)
    nyra "Qu'est-ce qui relie l'action à sa conséquence ? Cherchez la ponctuation."
    nyra "Si chacun prend un fragment, on reconstruira plus vite."

    $ showP("noam", "raison", 0.18)
    noam "D'accord."
    noam "On reconstruit ça, puis on discutera ensuite."
    noam "J'espère que rien n'a été ajouté de dangereux."

    hide sael
    hide nyra
    hide noam

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

    $ showP("lysa", "reflexion", 0.45)
    lysa "Autoriser le transport, la vente et l'échange de marchandises ..."
    lysa "Le système actuel de distribution de denrées est aboli ?!"

    $ showP("elen", "joie", 0.28)
    elen "On l'aaa ! Enfin une base claire !"

    $ showP("tomas", "neutre", 0.82)
    tomas "Parfait."
    tomas "M-Maintenant, le vrai débat peut commencer."

    hide elen
    hide tomas
    hide lysa

    jump _3_DEBAT1_PHASE2

# Durée : 2m35
# Totale : 1h 42m 35s

label _3_DEBAT1_PHASE2:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.5

    think "Le silence ne survit pas au texte."

    $ showP("mara", "reflexion", 0.40)
    mara "Le papier est clair. Qui est le génie qui veut supprimer les distributions ?"
    mara taquin "Qu'il lève la main, j'adore rencontrer les ambitieux."

    $ showP("elen", "surpris", 0.30)
    elen "Attends, ça faisait partie de la proposition ? C'est pas du tout le même plat !"

    $ showP("tomas", "reflechit", 0.85)
    tomas "La… la formulation est… euh… très claire."
    tomas "L’abrogation… elle est… incluse. Oui."

    hide tomas
    $ showP("nyra", "raison", 0.90)
    nyra "Qui bénéficie d'une abolition immédiate ? Pas d'une transition. D'une abolition."

    hide elen
    $ showP("kael", "inquiet", 0.05)
    kael "Supprimer les distributions change tout."

    hide kael
    $ showP("ryn", "desaccord", 0.15)
    ryn "Ça supprime TOUT ! La seule putain de sécurité qu’on avait !"

    think "Le silence revient, plus lourd."

    hide nyra
    $ showP("julian", "surpris", 0.75)
    julian "Ce n'est pas le texte annoncé. Le public a entendu « commerce », pas « abolition »."

    hide mara
    $ showP("iris", "panne", 0.40)
    iris "Oui. Lis la deuxième proposition, elle n'est pas décorative."

    julian hesitation "Julian défendait l'ouverture des échanges. Pas la disparition de tout filet."

    hide iris
    $ showP("lysa", "reflexion", 0.60)
    lysa "Donc quelqu’un a proposé ça."

    hide julian
    $ showP("tomas", "raison", 0.85)
    tomas "Les amendements sont déposés anonymement."

    $ showP("ryn", "desaccord", 0.15)
    ryn "Comme c'est pratique..."

    hide tomas
    $ showP("nyra", "fatigue", 0.90)
    nyra "Ce n’est pas anodin."
    nyra "Supprimer une structure mondiale, ça ne s’écrit pas par accident."

    think "Le malaise change de cible : le texte, puis son auteur invisible."

    hide nyra
    hide lysa
    $ showP("mara", "colere", 0.40)
    mara "Donc quelqu’un ici veut casser le système."
    mara "Et évidemment, il ne l’assume pas."

    $ showP("julian", "neutre", 0.75)
    julian "Nous devons débattre du texte, pas organiser une chasse aux sorcières. Le collectif n'y survivrait pas."

    ryn "Facile à dire."

    hide mara
    $ showP("noam", "raison", 0.50)
    noam "Je me demande si... tout ça n'est pas une mascarade."
    noam "Il est possible que Kami se moque totalement de nous, et que personne n'ait proposé ça."

    hide noam
    $ showP("lysa", "reflexion", 0.60)
    lysa "Oui. Dix votes pour douze textes : le tour de passe-passe parfait."
    lysa "Les augures choisissaient déjà les signes qui arrangeaient Rome. Bref."

    ryn "Hein, qu'est ce que tu veux dire par là ?!"

    lysa "Si Kami injecte ses propres textes, chacun attendra le sien."
    lysa salut "S'il ne sort jamais, il se croira simplement parmi les deux oubliés. Manipulation invérifiable."

    hide ryn
    $ showP("sael", "desaccord", 0.25)
    sael "Donc c'est impossible de savoir si c'est l'un d'entre nous qui a proposé ça ?"

    lysa "Exactement. Seules Kami et l'auteur — s'il existe — connaissent la réponse."

    sael "Les morts de Limen n'ont pas besoin d'un nouveau responsable."
    sael "Kami. Dis-nous seulement si ce texte vient de nous."

    think "Les regards se croisent. Personne ne répond."

    think "L'écran central reste figé. Kami ne répond pas."

    hide lysa
    $ showP("noam", "reflexion", 0.50)
    noam "Il me semble que... débattre du fond reste la seule chose utile là."
    noam reflexion "Je me demande si chercher un coupable maintenant nous avancerait vraiment."
    noam "Enfin... certains semblent moins sûrs qu'à la cafétéria."

    pause 0.5
    hide sael


    think "Julian déploie son plus grand sourire. Il sait que je parle de lui."
    $ showP("julian", "sourire", 0.75)
    julian "Noam, cette découverte nuance ma position. Elle ne l'annule pas."
    julian "Les échanges restent essentiels. Julian ne renie pas une idée au premier obstacle."

    hide noam
    $ showP("lysa", "blase", 0.60)
    lysa "T’es déjà sur scène."
    lysa "Respire."

    think "Les regards convergent vers Julian. Il obtient sa scène."

    $ showP("julian", "idee", 0.75)
    julian "Autoriser le transport et la vente relance les districts, l'économie, le mouvement."
    julian "Nous cessons de tout centraliser. Nous rendons aux gens une part de leur initiative."

    hide lysa
    $ showP("mara", "rire", 0.40)
    mara "Et tu comptes faire comment, lover ?"
    mara "Tu nourris les ventres vides avec ton discours ou tu le revends au marché noir ?"

    think "Un rire nerveux traverse la salle."

    $ showP("julian", "determine", 0.75)
    julian "Comment on le faisait avant ?"
    julian "Un district qui produit des ressources le vendra aux autres."
    julian "Tout simplement."

    $ showP("ryn", "neutre", 0.15)
    ryn "Et ceux qui n'ont rien ?!"

    $ showP("ryn", "desaccord", 0.15)
    ryn "Si le système actuel saute…"
    ryn "Les distributions sautent aussi."
    ryn "Et ça ça tuera de nombreuses personnes dans les districts les plus pauvres dont LIMEN."

    $ showP("julian", "hesitation", 0.75)
    julian "Pas forcément."

    ryn "Si."
    ryn "C’est écrit noir sur blanc."

    hide julian
    $ showP("tomas", "raison", 0.85)
    tomas "L’abrogation du système de distribution implique sa disparition."
    tomas "Il n’y a pas d’entre-deux, c'est factuel."

    hide tomas
    $ showP("julian", "surpris", 0.75)
    julian "On peut compenser."

    hide mara
    $ showP("lysa", "reflexion", 0.60)
    lysa "Comment tu comptes faire ça ?"
    lysa "Ce n'est même pas précisé dans l'amendement."

    $ showP("julian", "rire", 0.75)
    julian "C’est fou."
    julian "Dès qu’on parle d’ouverture, vous imaginez l’apocalypse."

    hide lysa
    $ showP("mara", "agace", 0.40)
    mara "Ouais non, j’ai pas envie de ramasser des macchabées parce que Monsieur Idéal a eu une illumination de start-upper."

    hide mara
    $ showP("elen", "inquiet", 0.30)
    elen "Mais attendez ! Ça va être génial !"
    elen "Les trucs vont circuler partout, on pourra enfin CHOISIR ce qu’on veut !"
    elen "C’est pas ça, la liberté ?!"

    hide julian
    $ showP("nyra", "raison", 0.90)
    nyra "Ça dépend de qui pourra les acheter."
    nyra "A Orbite, on a pas de ressources propres..."

    hide ryn
    $ showP("kael", "inquiet", 0.05)
    kael "Alors oui et non..."
    kael "Si on ne produit pas beaucoup de ressources, on en exploite quand même dans l'espace."
    kael "Simplement ces matériaux là ne restent pas bien longtemps chez nous, on les exporte rapidement."

    hide nyra
    $ showP("iris", "hesitation", 0.70)
    iris "Et…"
    iris "Si ça relançait aussi les trafics ?"

    "L’atmosphère se fige légèrement."

    hide kael
    $ showP("ryn", "colere", 0.15)
    ryn "Exact. Actuellement la frontière est fermée, seuls ceux qui ont une autorisation spéciale peuvent passer."
    ryn "Même si on ne peut pas passer, les matériaux peuvent passer sans soucis."
    ryn "Et si les distributions sautent comment feront les plus pauvres pour s'acheter quelque chose ?"

    hide iris
    $ showP("julian", "reflexion", 0.75)
    julian "En vendant aussi."

    ryn "Vendre QUOI, Julian ?! Leurs godasses trouées ? Leur fierté en solde ?!"

    julian "Leur travail, leur ressource."
    julian "Ne me fais pas croire un instant qu'il n'y a pas de travail à Limen !"

    ryn "Si, évidemment qu'il y en a..."

    julian "Et pourquoi les gens ne travaillent pas ?!"

    ryn "Parce que ça change QUE DALLE !"
    ryn "Tu travailles."
    ryn "Tu te crèves le cul douze heures, tu touches le même ticket pourri que le mec qui dort toute la journée."
    ryn "C’est ça ta motivation, toi ?!"

    $ showP("lysa", "reflexion", 0.60)
    lysa "Oui, c'est pareil dans tous les districts..."
    lysa "Comme on a les bons de rationnement et l'interdiction de faire du commerce, le travail est devenu accessoire."
    lysa "On ne travaille que si on le souhaite ou si on en reçoit l'ordre de Kami."

    think "Julian relève la tête, comme si Lysa venait de valider sa conclusion."

    julian "Enfin quelqu'un comprend où Julian veut en venir."

    lysa "Mais là tu joues au héros."
    lysa "Sans plan."

    $ showP("julian", "determine", 0.75)
    julian "Quelqu'un doit faire avancer le collectif."

    hide lysa
    $ showP("noam", "raison", 0.50)
    noam "Avancer... je me demande si on sait vraiment où on va."
    noam "Je ne dis pas non. Je dis : à quel prix."

    think "Plusieurs têtes approuvent."

    noam "Ce que j'entends, c'est qu'on parle d'une idée."
    noam reflexion "Il me semble que c'est autre chose. Un système. Quelque chose qui touche les gens dans leur quotidien."

    julian "Et le système actuel fonctionne ?"

    $ showP("mara", "reflexion", 0.40)
    mara "..."

    julian "Il nous étouffe."

    ryn "Il nous nourrit aussi."

    julian "En nous rationnant, en nous empêchant de manger ce qu'on veut, en nous distribuant du pain rassi, en nous obligeant à réclamer tout et n'importe quoi !"
    julian colere "Mais réveillez-vous ! Vous voulez garder ce monde là ?!"

    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On me dit dans l'oreillette que vous êtes ennuyants !!"
    kami "Tout ça, vos blabla, ça n'avance pas !"
    kami "Je suis obligée de prendre les choses en main."

    "Les pupitres se transforment. Micro et buzzer émergent devant chacun de nous."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "A partir de maintenant vous n'avez plus la parole."
    kami "Vous parlerez à tour de rôle. Histoire qu'on puisse vous entendre."
    kami "Devant vous, il y a un buzzer, si vous voulez contredire un propos d'un de vos camarades, vous pouvez appuyer dessus."
    kami "Et vous ne parlerez que lorsque votre buzzer s'allumera d'une couleur verte !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Compris ?!"
    kami "Alors c'est parti !"

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

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    kami "Oh bordel, regardez-moi ces têtes de défunts…"
    kami "Jusque là c’était mignon : entre Julian qui se branle l’ego en public, Ryn qui hurle comme une veuve éplorée..."
    kami "...et tout le monde qui cherche le coupable sans oser se regarder dans les yeux."
    kami "Mais là, on passe aux choses sérieuses, mes chéris."
    kami "Question du jour, et je veux du sang : si on coupe les distributions, qui va gérer la famine à Limen ?"
    kami "Et surtout… pourquoi le petit peuple irait se lever le cul le matin si y’a plus de carotte au bout du bâton ?"
    kami "Allez, montrez-moi que vous valez plus que des rations périmées. Je m’ennuie déjà."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    $ showP("noam", "raison", 0.50)  # centre
    noam "Il me semble qu’on peut essayer de rester civilisés."

    $ showP("julian", "determine", 0.88)  # droite
    julian "Civilisés ? On est en train de crever doucement, Noam."
    julian "Le statu quo, c’est une tombe collective avec des bons de pain rassis."

    $ showP("ryn", "colere", 0.12)  # gauche
    ryn "Et ton 'choc salvateur', c’est quoi ? On sacrifie Limen pour que tes potes d’Orbite se payent des putes en or ?"

    julian surpris "D'orbite ?!"
    julian rire "Mais je viens de Nexus moi ! Faut suivre hein !"

    ryn "Ah... Euh oui..."
    ryn jaloux "C'est pareil façon !"

    hide noam
    $ showP("mara", "agace", 0.50)  # centre
    mara "Oh ça va, Ryn, calme tes hormones."
    mara "Mais il a pas tort : si on ouvre tout, c’est qui qui va se faire démonter en premier ? Les ventres vides ou les queues molles ?"

    hide ryn
    $ showP("kael", "culpabilite", 0.12)  # gauche
    kael "Il faut un filet minimal. Une transition mesurable."

    hide julian
    $ showP("elen", "joie", 0.88)  # droite
    elen "Mais c'est çaaa qui est génial ! Choisir ce qu'on mange sans demander la permission !"

    hide mara
    $ showP("lysa", "blase", 0.50)  # centre
    lysa "Choisir avec quel argent, Elen ? Midas transformait tout en or et il est quand même mort de faim."

    hide kael
    $ showP("iris", "desaccord", 0.12)  # gauche
    iris "Évidemment. Pendant que vous rêvez de liberté, les trafiquants écrivent déjà leur protocole de marge."

    hide elen
    $ showP("tomas", "hesitation", 0.88)  # droite
    tomas "Euh… les chiffres des trois derniers cycles…"
    tomas "…montrent une chute de productivité de vingt-sept pour cent dans les zones très assistées."
    tomas "C’est… c’est pas rien, hein ?"

    hide lysa
    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Que deviennent ces chiffres sans transition ni filet de sécurité ?"
    nyra "Le texte coupe. Il n'accompagne rien."

    hide iris
    $ showP("sael", "mefiant", 0.12)  # gauche
    sael "…"

    sael "Le silence avant une famine ressemble beaucoup à celui-ci."

    think "Un silence lourd tombe. Tous les regards gagnent l'écran central."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Oh ? Déjà la parano ? J’adore."
    kami "Je vous rappelle que cet amendement est le fruit de VOTRE imagination !"
    kami "Continuez, mes petits rats de laboratoire."
    kami "Oooh ! J'adore le drama ! Je fais plus d'audimat !"

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], prompt="Moment 1 — Cadrer la première salve.")
    call _3_DEBAT1_PHASE3_INT1 from _call__3_DEBAT1_PHASE3_INT1

    stop music fadeout 1.0
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 0.8

    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Quel problème voulez-vous résoudre d'abord ? Les buzzers ont mélangé les trois."

    $ showP("elias", "determine", 0.88)  # droite
    elias "Parce qu'on évite les vraies questions. Le système marche pas. C'est clair."

    $ showP("sael", "mefiant", 0.12)  # gauche
    sael "…"

    sael "Nous savons où mène la faim. Personne ne veut nommer les morts."

    hide elias
    $ showP("lysa", "blase", 0.88)  # droite
    lysa "On a trois problèmes qui reviennent en boucle."
    lysa "Et on fait semblant qu’ils sont séparés."

    hide sael
    $ showP("noam", "reflexion", 0.12)  # gauche
    noam "Ce que j’entends, c’est trois sujets distincts. Le passé, le texte brut, et les rayons vides."
    noam reflexion "Il me semble qu’on ne peut pas traiter tout ça en même temps."

    hide nyra
    $ showP("elen", "joie", 0.50)  # centre
    elen "Mais il faut bien commencer quelque part !"
    elen "Sinon on va encore tourner en rond jusqu’à demain !"

    hide lysa
    $ showP("nyra", "sourire", 0.88)  # droite – retour
    nyra "Choisissez un angle. Je vous écoute depuis le début."

    hide noam
    $ showP("sael", "mefiant", 0.12)  # gauche – retour
    sael "Un seul."
    sael "Le reste attendra."

    think "La salle attend que quelqu'un tranche."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], prompt="Moment 2 — Désamorcer ou accélérer la fracture.")
    call _3_DEBAT1_PHASE3_INT2 from _call__3_DEBAT1_PHASE3_INT2

    stop music fadeout 1.0
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 1.0

    $ showP("noam", "raison", 0.50)  # centre
    noam "Il me semble qu’on a fait le tour."
    noam "Le monde d’avant, le texte brut, les trocs qui existent déjà…"
    noam reflexion "Je me demande si... on est prêts à choisir maintenant."

    $ showP("ryn", "colere", 0.88)  # droite
    ryn "Choisir entre crever lentement ou crever d’un coup ?"

    $ showP("julian", "determine", 0.12)  # gauche
    julian "Ou entre survivre enchaîné ou se battre libre."

    hide noam
    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Le système exige une réponse binaire. Sommes-nous prêts à assumer celle que nous donnerons ?"

    think "Les regards se croisent. La tension devient presque une treizième présence."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Enfin !"
    kami "J’ai failli m’endormir avec vos jérémiades."
    kami "Le texte est clair : suppression totale des bons ou statu quo."
    kami "Vert pour couper la laisse. Rouge pour rester sages."
    kami "Allez, mes petits rats. Faites-moi vibrer l’audimat."

    voix "Choix final : VERT ou ROUGE."
    think "Tous les yeux se tournent vers moi. C'est maintenant."

    hide screen day3_codex_logo
    jump vote_phase3_final

# Durée : 4m
# Total : 1h 52m 40s

# label vote_phase3_final:

#     scene bg_conclave at adaptive_fullscreen with dissolve
#     show screen kami_broadcast_ui
#     play music "music/bgm_fatal_assembly.mp3" fadein 1.2
#     with Dissolve(0.5)

#     show bg_conclave:
#         zoom 1.03
#         linear 0.7 zoom 1.0

#     kami "Mes délicieux cobayes... l'instant du verdict est arrivé."
#     kami "Un seul geste, et vous décidez si la faim devient une marchandise."
#     kami "Vert : vous ouvrez les vannes du marché. Rouge : vous gardez la laisse."
#     kami "Choisissez bien. Je savoure déjà la suite."

#     $ total_adhesion = sum(debat_day3_live_vote_stats.values())
#     $ vote_joueur = renpy.call_screen("vote_screen", total_adhesion=total_adhesion)

#     if vote_joueur == "pour":
#         scene bg_conclave at adaptive_fullscreen with vpunch
#         show expression Solid("#2dff9e40") as vote_flash with dissolve
#         hide vote_flash
#     else:
#         scene bg_conclave at adaptive_fullscreen with vpunch
#         show expression Solid("#ff435040") as vote_flash with dissolve
#         hide vote_flash

#     if total_adhesion > 0:
#         jump vote_pour
#     else:
#         jump vote_contre

label _3_DEBAT1_PHASE3_INT1:
    $ selected = p3_round_options[0][p3_pick]["title"]
    
    if "appro" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve
        $ showP("noam", "reflexion", 0.50)  # centre
        noam "Attends. Même avec les bons actuels… on trouve quoi sur les rayons ?"
        noam "Des fruits frais ? Des médocs qui marchent ? Des pièces pour réparer une pompe ?"

        $ showP("julian", "idee", 0.88)  # droite
        julian "Rien ! C’est du vent, Noam."
        julian "Ouvrir le commerce, c’est remplir les rayons. Point."

        $ showP("mara", "agace", 0.12)  # gauche
        mara "Ouais, super Julian. Et les districts qui produisent que dalle ?"
        mara "Ils vendent leur cul pour une patate ou ils crèvent la dalle en silence ?"

        hide noam
        $ showP("ryn", "colere", 0.50)  # centre – remplace Noam
        ryn "Exactement !"
        ryn "À Limen, on a déjà des bons qui servent à rien. Tu crois que le marché va soudain nous livrer en priorité ?"

        hide julian
        $ showP("kael", "reflechit", 0.88)  # droite
        kael "Possible. Limen concentre la demande. Pas nécessairement le pouvoir d'achat."

        hide mara
        $ showP("lysa", "blase", 0.12)  # gauche
        lysa "Encore faut-il de l'argent. Les famines irlandaises exportaient aussi pendant que les gens mouraient. Bref."

        hide ryn
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Pff. Les prix vont exploser. Les pauvres regarderont les rayons pleins depuis dehors."
        iris "Comme d’habitude quoi."

        hide kael
        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais imagine ! Des épices, des vrais vêtements... On pourra enfin choisiiir !"

        hide lysa
        $ showP("sael", "mefiant", 0.12)  # gauche
        sael "Limen fabrique déjà ce dont il a besoin quand il le peut. Les morts nous ont appris à ne pas attendre."

        # Modifs adhésion légères et nuancées
        $ debat_day3_apply_influence({"julian": 2, "ryn": 1, "mara": -1, "kael": 1, "lysa": 1, "elen": 2})

        hide sael
        hide elen 
        hide iris

    if "ration" in selected.lower() or "choix" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("noam", "reflexion", 0.50)  # centre
        noam "On dit que les bons permettent d’avoir beaucoup de choses…"
        noam "Mais en vrai, combien de produits sont réellement disponibles ?"

        $ showP("nyra", "raison", 0.88)  # droite
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

