default j4_photo_pick_trace_attempts = 0
default j4_photo_put_trace_attempts = 0
default j4_tray_eaten = []
default j4_thread_score = 0
default j4_thread_tension = 36
default j4_thread_wave = 1
default j4_thread_current_bubble = None
default j4_thread_selected_bubble = None
default j4_thread_silences_left = 2
default j4_thread_cut_used = 0
default j4_thread_timer = 0.0
default j4_thread_feedback = ""
default j4_thread_done = False
default j4_thread_result = "medium"
default j4_thread_active_bubbles = []
default j4_thread_answered_ids = []
default j4_thread_freeze_timer = 0.0
default j4_thread_last_link = None
default j4_thread_last_effect = ""
default j4_thread_round = 0
default j4_thread_successes = 0
default j4_argument_frontieres_cadre = False

init python:
    J4_THREAD_POLES = [
        {"id": "liberte", "label": "LIBERTE", "subtitle": "respirer / sortir / ne plus etre tenu", "xalign": 0.08, "yalign": 0.18, "color": "#9be7ff"},
        {"id": "securite", "label": "SECURITE", "subtitle": "risque / attaque / digue / protection", "xalign": 0.92, "yalign": 0.18, "color": "#ffd071"},
        {"id": "memoire", "label": "MEMOIRE", "subtitle": "morts / villages / sang / traumatisme", "xalign": 0.08, "yalign": 0.76, "color": "#d2b2ff"},
        {"id": "cadre", "label": "CADRE", "subtitle": "regles / rythme / controle / passage", "xalign": 0.92, "yalign": 0.76, "color": "#aef2bf"},
    ]

    J4_THREAD_BUBBLES = [
        {"id": "cage", "wave": 1, "keyword": "CAGE", "line": "Moi, j'en ai juste marre de vivre dans une cage.", "pole": "liberte", "danger": "normal", "xalign": 0.50, "yalign": 0.31, "success": "Ryn ne parle pas seulement de bouger. Il parle de respirer sans autorisation."},
        {"id": "gardiens", "wave": 1, "keyword": "GARDIENS", "line": "Des Gardiens sont morts pour tenir ces lignes.", "pole": "memoire", "danger": "urgent", "xalign": 0.36, "yalign": 0.40, "success": "Pour Sael, ouvrir les frontieres, ce n'est pas juste changer une regle. C'est toucher a des morts."},
        {"id": "frontieres", "wave": 1, "keyword": "FRONTIERES", "line": "Les frontieres, ce n'est pas une ligne sur une carte.", "pole": "securite", "danger": "normal", "xalign": 0.62, "yalign": 0.41, "success": "Elle parle d'un danger concret. Pas d'un symbole."},
        {"id": "trop_vite", "wave": 2, "keyword": "TROP VITE", "line": "On n'a meme pas survecu a une histoire de rationnement.", "pole": "cadre", "danger": "urgent", "xalign": 0.47, "yalign": 0.28, "success": "Lysa ne refuse pas forcement le changement. Elle dit qu'on n'a aucun rythme, aucun cadre."},
        {"id": "pauvres", "wave": 2, "keyword": "PAUVRES", "line": "Ce ne sera pas les plus solides qui se feront ecraser.", "pole": "liberte", "danger": "normal", "xalign": 0.35, "yalign": 0.48, "success": "Iris parle de ceux qui subiront la liberte des autres avant d'en profiter."},
        {"id": "controle", "wave": 2, "keyword": "CONTROLE", "line": "On nous balance un bouton, et debrouillez-vous.", "pole": "cadre", "danger": "normal", "xalign": 0.64, "yalign": 0.47, "success": "Nyra pointe le vrai vide : pas de regles, pas de passage, pas de protection."},
        {"id": "peur", "wave": 3, "keyword": "PEUR", "line": "Vous me faites tous peur.", "pole": "memoire", "danger": "urgent", "xalign": 0.40, "yalign": 0.31, "success": "Sael ne parle plus seulement du vote. Elle parle de ce qu'elle a deja vu arriver."},
        {"id": "digue", "wave": 3, "keyword": "DIGUE", "line": "J'appelle ca une digue.", "pole": "securite", "danger": "urgent", "xalign": 0.59, "yalign": 0.39, "success": "Pour elle, une frontiere fermee n'est pas une prison. C'est ce qui empeche le pire de revenir."},
        {"id": "laisse", "wave": 3, "keyword": "LAISSE", "line": "Kami nous tient encore en laisse.", "pole": "liberte", "danger": "normal", "xalign": 0.50, "yalign": 0.52, "success": "Ryn confond peut-etre vitesse et liberte, mais sa colere vient d'un vrai enfermement."},
    ]

    J4_THREAD_PARASITES = [
        {"id": "parasite_0", "keyword": "MENSONGE", "line": "Quelqu'un cherche a faire taire quelqu'un.", "xalign": 0.22, "yalign": 0.34},
        {"id": "parasite_1", "keyword": "TRAITRE", "line": "Le mot parasite accroche la table.", "xalign": 0.77, "yalign": 0.35},
        {"id": "parasite_2", "keyword": "COUPABLE", "line": "La faute circule plus vite que les idees.", "xalign": 0.26, "yalign": 0.58},
        {"id": "parasite_3", "keyword": "CRIE", "line": "Le volume remplace le sens.", "xalign": 0.74, "yalign": 0.59},
    ]

    J4_NEWS_ITEMS = [
        ("FILES DE RATIONNEMENT INCHANGÉES", "Même file. Autre district. Même attente.\nLe système appelle ça de la stabilité."),
        ("DISTRIBUTION CENTRALISÉE MAINTENUE", "Aucun ajustement local autorisé.\nLes citoyens sont invités à préserver le calme."),
        ("RÉAFFECTATION DES STOCKS NON ESSENTIELS", "Les réserves de confort du Conclave sont redirigées.\nLe sacrifice partagé est prioritaire."),
        ("COMMUNIQUÉ ARCHIVE", "Aucune archive commerciale ne sera ouverte.\nLa continuité administrative reste totale."),
        ("MESSAGE OFFICIEL DE KAMI", "Merci d'avoir choisi la prudence.\nDemain vous ressemblera."),
        ("AUCUNE ÉVOLUTION COMMERCIALE AUTORISÉE", "Pas de circulation libre. Pas d'échange spontané.\nLe monde entier ressemble à une salle d'attente."),
    ]

    def j4_thread_safe_play(path):
        if renpy.loadable(path):
            renpy.play(path, channel="sound")

    def j4_thread_bubble_by_id(bubble_id):
        for bubble in J4_THREAD_BUBBLES:
            if bubble["id"] == bubble_id:
                return bubble
        for bubble in J4_THREAD_PARASITES:
            if bubble["id"] == bubble_id:
                parasite = dict(bubble)
                parasite["parasite"] = True
                parasite["danger"] = "danger"
                return parasite
        return None

    def j4_thread_next_real_bubble():
        for bubble in J4_THREAD_BUBBLES:
            if bubble["id"] not in store.j4_thread_answered_ids:
                return bubble
        return None

    def j4_thread_refresh_wave():
        current = j4_thread_next_real_bubble()
        if current:
            store.j4_thread_wave = current["wave"]
            store.j4_thread_current_bubble = current["id"]
        else:
            store.j4_thread_current_bubble = None
            store.j4_thread_done = True

    def j4_thread_reset():
        store.j4_thread_score = 0
        store.j4_thread_tension = 36
        store.j4_thread_wave = 1
        store.j4_thread_current_bubble = None
        store.j4_thread_selected_bubble = None
        store.j4_thread_silences_left = 2
        store.j4_thread_cut_used = 0
        store.j4_thread_timer = 0.0
        store.j4_thread_feedback = "Clique une bulle, puis relie-la au bon enjeu."
        store.j4_thread_done = False
        store.j4_thread_result = "medium"
        store.j4_thread_active_bubbles = []
        store.j4_thread_answered_ids = []
        store.j4_thread_freeze_timer = 0.0
        store.j4_thread_last_link = None
        store.j4_thread_last_effect = ""
        store.j4_thread_round = 0
        store.j4_thread_successes = 0
        j4_thread_refresh_wave()
        j4_thread_safe_play("sound/thread_bubble_spawn.ogg")

    def j4_thread_select(bubble_id):
        if store.j4_thread_done:
            return
        store.j4_thread_selected_bubble = bubble_id
        bubble = j4_thread_bubble_by_id(bubble_id)
        if bubble:
            store.j4_thread_feedback = bubble["line"]

    def j4_thread_choose_pole(pole_id):
        if store.j4_thread_done or not store.j4_thread_selected_bubble:
            return

        bubble_id = store.j4_thread_selected_bubble
        bubble = j4_thread_bubble_by_id(bubble_id)
        if not bubble:
            store.j4_thread_selected_bubble = None
            return

        if bubble.get("parasite", False):
            store.j4_thread_tension = min(100, store.j4_thread_tension + 8)
            store.j4_thread_feedback = "Noam donne du poids a un mot parasite. Le debat se crispe."
            store.j4_thread_last_effect = "fail"
            j4_thread_safe_play("sound/thread_link_fail.ogg")
            store.j4_thread_selected_bubble = None
            return

        if pole_id == bubble["pole"]:
            store.j4_thread_score += 1
            store.j4_thread_successes += 1
            store.j4_thread_tension = max(0, store.j4_thread_tension - 9)
            store.j4_thread_feedback = bubble["success"]
            store.j4_thread_last_link = (bubble["xalign"], bubble["yalign"], pole_id)
            store.j4_thread_last_effect = "success"
            j4_thread_safe_play("sound/thread_link_success.ogg")
        else:
            store.j4_thread_tension = min(100, store.j4_thread_tension + 17)
            store.j4_thread_feedback = "Noam tire le fil du mauvais cote. La phrase se durcit au lieu de s'ouvrir."
            store.j4_thread_last_effect = "fail"
            j4_thread_safe_play("sound/thread_link_fail.ogg")

        store.j4_thread_answered_ids.append(bubble_id)
        store.j4_thread_selected_bubble = None
        store.j4_thread_timer = 0.0
        store.j4_thread_round += 1
        j4_thread_refresh_wave()
        if store.j4_thread_done:
            j4_thread_finalize()
        else:
            j4_thread_safe_play("sound/thread_bubble_spawn.ogg")

    def j4_thread_spawn_parasite():
        if len(store.j4_thread_active_bubbles) >= 3:
            return
        index = (store.j4_thread_round + len(store.j4_thread_active_bubbles) + int(store.j4_thread_tension / 10)) % len(J4_THREAD_PARASITES)
        parasite = J4_THREAD_PARASITES[index]
        if parasite["id"] not in store.j4_thread_active_bubbles:
            store.j4_thread_active_bubbles.append(parasite["id"])
            j4_thread_safe_play("sound/thread_bubble_spawn.ogg")

    def j4_thread_silence():
        if store.j4_thread_done or store.j4_thread_silences_left <= 0:
            return
        store.j4_thread_silences_left -= 1
        store.j4_thread_freeze_timer = 1.0
        store.j4_thread_feedback = "Noam impose une seconde de silence. Les mots restent suspendus."
        j4_thread_safe_play("sound/thread_silence.ogg")

    def j4_thread_cut():
        if store.j4_thread_done or not store.j4_thread_selected_bubble:
            return
        if store.j4_thread_selected_bubble in store.j4_thread_active_bubbles:
            store.j4_thread_active_bubbles.remove(store.j4_thread_selected_bubble)
            store.j4_thread_selected_bubble = None
            store.j4_thread_cut_used += 1
            store.j4_thread_tension = min(100, store.j4_thread_tension + 5)
            store.j4_thread_feedback = "Noam coupe court. Efficace, mais le geste laisse une marque."
            store.j4_thread_last_effect = "cut"
            j4_thread_safe_play("sound/thread_cut.ogg")

    def j4_thread_finalize():
        if store.j4_thread_tension >= 86 or store.j4_thread_score <= 3:
            store.j4_thread_result = "bad"
            j4_thread_safe_play("sound/thread_break.ogg")
        elif store.j4_thread_score >= 7 and store.j4_thread_tension <= 64:
            store.j4_thread_result = "good"
        else:
            store.j4_thread_result = "medium"
        store.j4_thread_done = True

    def j4_thread_tick():
        if store.j4_thread_done:
            return
        if store.j4_thread_freeze_timer > 0.0:
            store.j4_thread_freeze_timer = max(0.0, store.j4_thread_freeze_timer - 0.5)
            return

        store.j4_thread_timer += 0.5
        if store.j4_thread_timer >= 3.0:
            store.j4_thread_tension = min(100, store.j4_thread_tension + 2)
            if int(store.j4_thread_timer * 10) % 10 == 0:
                store.j4_thread_feedback = "Le silence dure trop longtemps. La tension gagne du terrain."
                j4_thread_safe_play("sound/thread_tension_up.ogg")

        spawn_delay = 4.0
        if store.j4_thread_tension >= 75:
            spawn_delay = 2.5
        if store.j4_thread_timer >= spawn_delay and int(store.j4_thread_timer * 10) % 20 == 0:
            j4_thread_spawn_parasite()

        if store.j4_thread_tension >= 100:
            store.j4_thread_feedback = "Le fil casse."
            j4_thread_finalize()

screen day4_restricted_map():
    modal True
    zorder 200

    add Solid("#000")
    add "images/carte/bg_map.png" at cover_screen

    frame:
        xalign 0.03
        yalign 0.05
        background Solid("#071018dd")
        padding (18, 14)
        text "Objectif : rejoindre la cafétéria" size 30 color "#E8F4FF"

    imagebutton:
        idle "images/carte/cafeteria.png"
        hover "images/carte/cafeteria_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("cafeteria")

    imagebutton:
        idle "images/carte/repos.png"
        hover "images/carte/repos_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("repos")

    imagebutton:
        idle "images/carte/conclave.png"
        hover "images/carte/conclave_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("conclave")

    imagebutton:
        idle "images/carte/dortoir.png"
        hover "images/carte/dortoir_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("dortoir")

    imagebutton:
        idle "images/carte/infirmerie.png"
        hover "images/carte/infirmerie_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("infirmerie")

screen day4_cafeteria_wall():
    modal True
    zorder 205

    add "images/background/bg_cafeteria.png" at cover_screen
    add Solid("#00000055")

    frame:
        xalign 0.5
        yalign 0.16
        xsize 760
        background Solid("#071018e8")
        padding (24, 18)
        vbox:
            spacing 10
            text "ÉCRAN CAFÉTÉRIA" size 30 color "#BFE8FF" xalign 0.5
            text "Les flux d'aujourd'hui tournent en boucle." size 24 color "#DCE8F7" xalign 0.5

    imagebutton:
        idle "gui/day4/news_button_idle.png"
        hover "gui/day4/news_button_hover.png"
        xalign 0.5
        yalign 0.49
        action Return("news")

    textbutton "Continuer":
        xalign 0.5
        yalign 0.78
        action Return("continue")

screen day4_cafeteria_elen_gate():
    modal True
    zorder 205

    add Solid("#000")
    add "images/background/bg_cafeteria.png" at cover_screen

    imagebutton:
        idle "images/background/interact/cafeteria/goumi.png"
        hover "images/background/interact/cafeteria/goumi_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("goumi")

    imagebutton:
        idle "images/background/interact/cafeteria/frigo.png"
        hover "images/background/interact/cafeteria/frigo_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("frigo")

    imagebutton:
        idle "images/background/interact/cafeteria/table.png"
        hover "images/background/interact/cafeteria/table_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("tables")

    imagebutton:
        idle "images/background/interact/cafeteria/ecran.png"
        hover "images/background/interact/cafeteria/ecran_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Return("news")

    imagebutton:
        idle Transform("images/character/elen/colere.png", zoom=0.75)
        hover Transform("images/character/elen/colere_noire.png", zoom=0.75)
        focus_mask True
        xalign 0.55
        yalign 0.30
        action Return("elen")

screen day4_news_screen():
    modal True
    zorder 215

    add "gui/day4/news_screen_bg.png" at cover_screen

    frame:
        xalign 0.5
        yalign 0.48
        xsize 1180
        ysize 760
        background Solid("#071018f2")
        padding (26, 24)

        vbox:
            spacing 18
            text "INFOS D'AUJOURD'HUI" size 38 color "#E8F4FF"
            grid 2 3:
                spacing 16
                for title, body in J4_NEWS_ITEMS:
                    frame:
                        xsize 550
                        ysize 165
                        background Solid("#101a26ee")
                        padding (18, 14)
                        vbox:
                            spacing 8
                            text title size 21 color "#9FD8FF"
                            text body size 22 color "#E1E8EF"

    textbutton "Fermer":
        xalign 0.5
        yalign 0.91
        xsize 180
        ysize 54
        action Return("back")

screen day4_tray_pnc():
    modal True
    zorder 210

    add "images/background/interact/cafeteria/plateau/plateau.png" at cover_screen

    if "bread" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/pain.png"
            hover "images/background/interact/cafeteria/plateau/pain.png"
            xalign 0.29
            yalign 0.54
            action Return("bread")

    if "ration" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/ration.png"
            hover "images/background/interact/cafeteria/plateau/ration.png"
            xalign 0.50
            yalign 0.50
            action Return("ration")

    if "bar" not in j4_tray_eaten:
        imagebutton:
            idle "images/background/interact/cafeteria/plateau/barre.png"
            hover "images/background/interact/cafeteria/plateau/barre.png"
            xalign 0.65
            yalign 0.64
            action Return("bar")

    button:
        xalign 0.37
        yalign 0.68
        xsize 260
        ysize 170
        background None
        action Return("empty")

    textbutton "Terminer":
        xalign 0.84
        yalign 0.88
        xsize 190
        ysize 58
        action Return("finish")

transform j4_thread_bubble_idle:
    alpha 0.96
    zoom 1.0
    ease 0.7 yoffset -6
    ease 0.7 yoffset 6
    repeat

transform j4_thread_bubble_selected:
    alpha 1.0
    zoom 1.06
    ease 0.22 zoom 1.11
    ease 0.22 zoom 1.06
    repeat

transform j4_thread_glitch:
    alpha 0.24
    ease 0.05 xoffset -10
    ease 0.05 xoffset 12
    ease 0.05 xoffset 0
    repeat

screen day4_thread_debate():
    modal True
    zorder 220

    on "show" action Function(j4_thread_reset)
    timer 0.5 repeat True action Function(j4_thread_tick)

    if renpy.loadable("gui/day4/thread/thread_bg.png"):
        add "gui/day4/thread/thread_bg.png" at cover_screen
    else:
        add "gui/day4/thread_debate_bg.png" at cover_screen

    if j4_thread_tension >= 75:
        add Solid("#2a0308a8")
        add Solid("#ff1c1c22") at j4_thread_glitch
    else:
        add Solid("#00081699")

    $ current = j4_thread_bubble_by_id(j4_thread_current_bubble)
    $ visible_bubbles = []
    if current:
        $ visible_bubbles.append(current)
    for parasite_id in j4_thread_active_bubbles:
        $ parasite_bubble = j4_thread_bubble_by_id(parasite_id)
        if parasite_bubble:
            $ visible_bubbles.append(parasite_bubble)

    frame:
        xalign 0.5
        yalign 0.08
        xsize 720
        ysize 128
        background Solid("#06111dee")
        padding (20, 14)
        vbox:
            spacing 6
            text "NOAM / FIL DU DEBAT" size 34 color "#E8F4FF" xalign 0.5
            text "Vague [j4_thread_wave]/3 - [j4_thread_score] fils compris" size 22 color "#9FD8FF" xalign 0.5
            if current:
                text current["line"] size 22 color "#DCE8F7" xalign 0.5 text_align 0.5

    frame:
        xalign 0.5
        yalign 0.47
        xsize 390
        ysize 190
        background Solid("#081827dd")
        padding (20, 18)
        vbox:
            spacing 8
            text "NOAM" size 26 color "#E8F4FF" xalign 0.5
            text "Maintenir le sens sans etouffer la colere." size 20 color "#A9C6D8" xalign 0.5 text_align 0.5
            null height 8
            bar value StaticValue(max(0, 100 - j4_thread_tension), 100):
                xsize 330
                ysize 16
            text "Concentration" size 18 color "#CDEBFF" xalign 0.5

    for pole in J4_THREAD_POLES:
        frame:
            xalign pole["xalign"]
            yalign pole["yalign"]
            xsize 270
            ysize 116
            background Solid("#07131fee")
            padding (10, 8)
            vbox:
                spacing 4
                textbutton pole["label"]:
                    xsize 250
                    ysize 50
                    background Solid("#10283aee")
                    hover_background Solid("#1a4665ee")
                    text_size 27
                    text_color pole["color"]
                    text_hover_color "#ffffff"
                    action Function(j4_thread_choose_pole, pole["id"])
                text pole["subtitle"] size 16 color "#BFD5E5" xalign 0.5 text_align 0.5

    for bubble in visible_bubbles:
        $ is_selected = bubble["id"] == j4_thread_selected_bubble
        $ is_parasite = bubble.get("parasite", False)
        $ bubble_bg = "#0f3147ee"
        $ bubble_border = "#9be7ff"
        $ bubble_text = "#ffffff"
        if bubble.get("danger", "normal") == "urgent":
            $ bubble_bg = "#5a2b0bee"
            $ bubble_border = "#ffb35c"
        if is_parasite:
            $ bubble_bg = "#25050bee"
            $ bubble_border = "#ff3848"
        if is_selected:
            $ bubble_bg = "#1d6788ee"
            $ bubble_text = "#ffffff"
        button:
            xalign bubble["xalign"]
            yalign bubble["yalign"]
            xsize 245
            ysize 92
            background Solid(bubble_bg)
            hover_background Solid("#244e68ee")
            action Function(j4_thread_select, bubble["id"])
            at j4_thread_bubble_idle
            frame:
                xfill True
                yfill True
                background Solid("#00000000")
                padding (10, 8)
                vbox:
                    spacing 2
                    text bubble["keyword"] size 30 color bubble_text xalign 0.5
                    if is_parasite:
                        text "parasite" size 17 color bubble_border xalign 0.5
                    else:
                        text "a relier" size 17 color bubble_border xalign 0.5

    if j4_thread_last_effect == "success":
        frame:
            xalign 0.5
            yalign 0.66
            xsize 560
            ysize 38
            background Solid("#9be7ff55")
            padding (8, 4)
            text "Fil lumineux etabli" size 22 color "#E8F4FF" xalign 0.5
    elif j4_thread_last_effect == "fail":
        add Solid("#ff1c1c33") at j4_thread_glitch
    elif j4_thread_last_effect == "cut":
        frame:
            xalign 0.5
            yalign 0.66
            xsize 500
            ysize 38
            background Solid("#ff384855")
            padding (8, 4)
            text "Mot coupe" size 22 color "#ffffff" xalign 0.5

    hbox:
        xalign 0.5
        yalign 0.78
        spacing 18
        textbutton "Faire silence ([j4_thread_silences_left])":
            xsize 260
            ysize 58
            text_size 23
            background Solid("#123044ee")
            hover_background Solid("#1f5b79ee")
            insensitive_background Solid("#222831dd")
            action Function(j4_thread_silence)
            sensitive j4_thread_silences_left > 0
        textbutton "Couper":
            xsize 180
            ysize 58
            text_size 23
            background Solid("#451018ee")
            hover_background Solid("#762030ee")
            insensitive_background Solid("#222831dd")
            action Function(j4_thread_cut)
            sensitive j4_thread_selected_bubble in j4_thread_active_bubbles

    frame:
        xalign 0.5
        yalign 0.91
        xsize 940
        ysize 112
        background Solid("#061018ee")
        padding (18, 12)
        vbox:
            spacing 8
            hbox:
                spacing 14
                text "TENSION" size 23 color "#E8F4FF"
                bar value StaticValue(j4_thread_tension, 100):
                    xsize 735
                    ysize 22
            text "[j4_thread_feedback]" size 23 color "#E8F4FF" xalign 0.5 text_align 0.5

    if j4_thread_done:
        timer 0.8 action Return(j4_thread_result)

label _4_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4

    pause 1.5  # Légèrement plus long pour accentuer la lourdeur

    $ blink()
    "Je me réveille… ou plutôt, je reviens à moi."
    $ blink()
    "La lumière bleue des veilleuses est toujours là, mais aujourd’hui elle donne l’impression d’un néon fatigué qui clignote à peine."

    "Hier, on a voté."
    "On a eu une chance. Une vraie."
    "Et on l’a laissée filer."
    "Le bouton vert est resté éteint. Au moins l'un d'entre nous a dit non."
    "Et le monde continue de tourner exactement comme avant."

    $ blink()
    "Je reste immobile, les bras morts le long du corps."
    "Mon cœur bat lentement, presque à contrecœur, comme s’il économisait ses forces pour une journée qui ne vaut pas la peine d’être vécue."

    "On a gardé les bons de rationnement."
    "On a gardé la sécurité."
    "Mais on a aussi gardé nos chaines."

    $ blink()
    pause 2.5  # Pause plus longue pour laisser peser le vide

    "Je me tourne à moitié."
    "Une photo holographique est posée sur la table de nuit."
    "Elle n'était pas là hier."
    "Ou alors je ne l'ai pas vue."
    "Non. Je l'aurais vue."

    call day4_photo_take_trace from _call_day4_photo_take_trace

    scene bg_cg029 at adaptive_fullscreen with dissolve
    "Je la prends entre deux doigts."
    "Le cadre est froid."
    "Un souvenir posé là sans me demander mon avis."
    "Même ma table de nuit n'est pas vraiment à moi."
    "Sur la photo, il y a une famille souriante. Pas la mienne. Ce sont des amis."
    $ unlock_gallery_image("bg_cg029")
    "Je me demande si eux aussi ont un bon de rationnement ce matin."
    "Ou si, quelque part, ils ont déjà arrêté de sourire depuis longtemps."

    menu:
        "Regarder la photo encore quelques secondes.":
            "Je garde le cadre levé."
            "Les visages tremblent à peine dans la lumière holographique."
            "Plus je regarde, plus j'ai l'impression qu'on m'a déposé une preuve au lieu d'un souvenir."

        "La retourner immédiatement.":
            "Je serre un peu trop fort les bords."
            "Je n'ai pas envie que ces sourires me regardent plus longtemps."

        "Vérifier l'arrière du cadre.":
            "Je retourne le cadre."
            "Rien."
            "Pas de signature. Pas de mot. Juste une surface lisse, prévue pour ne rien avouer."

    call day4_photo_put_trace from _call_day4_photo_put_trace

    "Je repose la photo face contre la table."
    "Ça ne règle rien."
    "Mais au moins, pendant quelques secondes, elle cesse de me regarder."

    play sound sfx_announce
    "Un bip strident déchire le silence."
    "L’écran s’allume brutalement, lumière blanche et clinique."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits anges de la prudence !"
    kami "Il est 8 heures, et devinez quoi ? La révolution est officiellement annulée !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit briefing matinal, parce que je sais que vous raffolez quand je vous rappelle à quel point vous êtes raisonnables :"
    kami "La situation est toujours impeccables. Pas une pièce qui circule, pas une once de liberté."
    kami "Vous avez l'avez voulu, vous l'aurez !."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C’est beau, non ? Le calme avant… ben, le calme, en fait."
    kami "Pas d’alarme, pas de chaos."
    kami "Juste la douce certitude que demain sera exactement comme aujourd’hui."
    kami "Alors, je tiens à tous vous remercier :"
    kami "Merci de m'avoir donné raison. L'humanité ne veut pas de cette liberté que vous dites pourtant chérir."
    kami "Elle est bien moins importante que le certitude de pouvoir être nourris."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Allez, ne faites pas cette tête !"
    kami "Vous verrez tout ça de vos propres yeux à la cafétéria. Les écrans sont chauds, vos rations sont prêtes."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    "L’écran s’éteint. Le silence retombe, épais comme du béton."
    "Je reste assis, les mains posées sur mes genoux, inertes."
    "Elle n’a même pas besoin de mentir."
    "On n’a rien changé. Et on n’a même pas le courage de le regretter à voix haute."

    pause 1.8

    play sound sfx_drop
    "Un bruit mat dans le couloir. Comme un poing contre du métal."
    "Un cri bref, étouffé, presque honteux."
    "Puis plus rien."

    "Je me lève lentement. Pas d’un bond. Pas la force."
    "Mon cœur cogne, mais c’est un cognement fatigué."
    "Je tends l’oreille. Silence."
    "Juste l’écho de ce cri, et la certitude que ce n’est que le début de quelque chose qui se fissure sans bruit."

    "Ça n’a pas encore explosé."
    "Mais ça pourrait à tout moment."

    jump _4_0_NAVIGATION_CAFETERIA

label day4_photo_take_trace:

    $ j4_photo_pick_trace_attempts = 0

label day4_photo_take_trace_loop:

    call screen trace_qte(path_type="curve_right", time_limit=6.0, wait_time=0.5, tolerance=70, max_errors=5, anchor_x=860, anchor_y=620)

    if _return:
        return

    $ j4_photo_pick_trace_attempts += 1
    if j4_photo_pick_trace_attempts >= 2:
        "Mes doigts glissent une première fois, puis finissent par trouver le bord du cadre."
        return

    "Je m'y reprends."
    jump day4_photo_take_trace_loop

label day4_photo_put_trace:

    $ j4_photo_put_trace_attempts = 0

label day4_photo_put_trace_loop:

    call screen trace_qte(path_type="arc", time_limit=5.0, wait_time=0.4, tolerance=72, max_errors=5, anchor_x=960, anchor_y=620)

    if _return:
        return

    $ j4_photo_put_trace_attempts += 1
    if j4_photo_put_trace_attempts >= 2:
        "Je finis par la reposer, maladroitement."
        return

    "Le cadre accroche mes doigts."
    jump day4_photo_put_trace_loop

label _4_0_NAVIGATION_CAFETERIA:

    scene bg_couloir at adaptive_fullscreen with dissolve
    "Je sors de la chambre."
    "Le couloir m'attend avec sa lumière froide et ses portes fermées."

label _4_0_NAVIGATION_CAFETERIA_LOOP:

    call screen day4_restricted_map()

    if _return == "cafeteria":
        "Je prends enfin la direction de la cafétéria."
        jump _4_0_CAFETERIA_ELEN

    if _return == "repos":
        scene bg_repos at adaptive_fullscreen with dissolve
        think "Je n'ai pas envie de faire semblant de me détendre."
    elif _return == "conclave":
        scene bg_conclave at adaptive_fullscreen with dissolve
        think "Pas maintenant. Je n'ai pas envie de revoir les boutons."
    elif _return == "dortoir":
        scene bg_dortoir at adaptive_fullscreen with dissolve
        think "Derrière chaque porte, quelqu'un digère l'échec d'hier à sa manière."
    elif _return == "infirmerie":
        scene bg_infirmerie at adaptive_fullscreen with dissolve
        think "Mauvaise idée. Je n'ai pas envie de chercher une solution dans une armoire à médicaments."

    jump _4_0_NAVIGATION_CAFETERIA_LOOP

label _4_0_CAFETERIA_ELEN:

    $ decouverte_cafeteria = True

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "A peine entré dans la cafétéria, je repère Elen près du comptoir."
    "Elle ne parle pas. Elle bouillonne."

label _4_0_CAFETERIA_ELEN_PARTIAL:

    call screen day4_cafeteria_elen_gate()

    if _return == "elen":
        $ showP("elen", "colere", 0.55)
        elen "Noam."
        elen "Viens voir ça."
        hide elen
        jump _4_0_CAFETERIA_ECRANS

    if _return == "news":
        call screen day4_news_screen()
    elif _return == "goumi":
        "Goumi reste immobile derriere le comptoir."
        "Ses voyants suivent Elen comme s'il attendait l'ordre suivant."
    elif _return == "frigo":
        "Le frigo-machine affiche des listes presque vides."
        "Il y a assez pour survivre. Pas assez pour oublier ou on est."
    elif _return == "tables":
        "Les tables sont deja occupees par des plateaux silencieux."
        "Personne ne mange vraiment."

    jump _4_0_CAFETERIA_ELEN_PARTIAL

label _4_0_CAFETERIA_ECRANS:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "À peine entré dans la cafétéria, je remarque l’attroupement près du grand comptoir central."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen "Allez Goumi, s’il te plaît ! Juste un tout petit peu de cannelle ! Ou même du poivre !"
    elen "Ça fait des mois que je rêve d’un truc qui ait vraiment du goût !"

    goumi "Demande refusée, représentante Elen."
    goumi "Les provisions restantes du Conclave ont été redirigées vers la Terre ce matin."

    elen "Quoi ?! Mais… on n’a presque rien ici !"

    elias "Moi je voulais juste des barres protéinées un peu meilleures… celles qu’on a sont dégueulasses !"

    nyra "Elen, Elias… calmez-vous. Goumi ne fait qu’appliquer les ordres."

    goumi "Ordre direct de Kami. Priorité absolue à la distribution planétaire."

    elen "Mais c’est injuste ! On est coincés ici et on n’a même pas le droit à un petit quelque chose de différent ?!"

    elias "Ouais, on est censés représenter tout le monde et on bouffe la même merde que les autres ?!"

    nyra "Ce n’est pas en criant que ça va changer quoi que ce soit…"

    elen "…Je voulais juste que ça ait un peu de goût pour une fois."

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh là là, ma petite Elen… toujours à pleurnicher pour tes petites épices de luxe ?"
    kami "C’est tellement mignon. Tellement… humain."
    kami "Mais il faut bien que tout le monde participe un minimum à l’effort collectif, non ?"
    kami "Le Conclave ne doit pas devenir un petit paradis pour privilégiés pendant que la Terre se serre la ceinture."
    kami "C’est une question d’équité. De justice. De sacrifice partagé."
    kami "Ne vous inquiétez pas trop… de nouvelles provisions arriveront au Jour 7."
    kami "En attendant, contentez-vous de ce que vous avez. Comme tout le monde."
    kami "Et surtout… comme vous l’avez vous-mêmes décidé hier."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "L’écran s’éteint."

    "Elen reste figée deux secondes, les yeux brillants de larmes de rage et de déception."
    "Puis elle tourne les talons et quitte la cafétéria presque en courant, la tête baissée comme une petite fille qui vient de se faire humilier devant tout le monde."

    menu:
        "Faire un pas vers Elen.":
            "Je bouge trop tard."
            "Elen est déjà partie."

        "Regarder Goumi.":
            "Le robot reste immobile."
            "Pas de honte. Pas d'hésitation."
            "Juste l'ordre exécuté."

        "Baisser les yeux vers le plateau.":
            "Je regarde ma ration."
            "Elle a soudain l'air encore plus petite."

    $ showP("mara", "agace", 0.70)
    mara "…Génial. Voilà qu’elle boude comme une gamine maintenant."

    $ showP("julian", "decu", 0.50)
    julian "On ne peut même plus avoir un peu de goût dans nos rations ?"
    julian "C’est ça, notre grande victoire d’hier ?"

    $ showP("ryn", "colere", 0.12)
    ryn "Bravo. On a voté pour la sécurité et on se fait traiter comme des chiens par une IA."
    ryn "On mérite vraiment tout ce qui nous arrive."

    "Je reste planté là, ma ration tiède entre les mains. L’ambiance est déjà irrespirable."

    pause 1.2

    "Les écrans muraux s’allument enfin, montrant les mêmes images que tous les jours :"
    "Rien n'a changé. Les files d'attente sont longues."
    "Il n'y a rien d'autre à manger qu'un bout de pain déjà sec depuis deux jours ..."

    hide julian
    $ showP("lysa", "determine", 0.50)
    lysa "Tout est parfaitement normal."
    lysa "Comme hier. Comme demain. Comme dans six mois."

    hide mara
    $ showP("kael", "calme", 0.88)
    kael "C’est stable. C’est ce qu’on a voté."

    $ showP("ryn", "colere", 0.12)
    ryn "Stable ? On crève lentement et poliment, oui !"

    hide lysa
    $ showP("iris", "desaccord", 0.50)
    iris "Les pauvres continuent à crever devant les mêmes murs. Rien ne change jamais."

    hide kael
    $ showP("julian", "decu", 0.88)
    julian "On avait une chance de faire bouger les choses… et on l’a laissée passer."

    "Je pose ma ration intacte sur la table."

    hide ryn
    $ showP("lysa", "blase", 0.30)
    lysa "Alors Noam ?"
    lysa "Tu regrettes qu’on n’ait pas osé ? Ou tu es soulagé qu’on ait préféré rester dans nos petites chaînes bien confortables ?"

    menu:
        "Répondre franchement.":
            noam "Je crois que oui."
            noam "Mais je ne sais même pas ce que je regrette exactement."

        "Éviter son regard.":
            noam "Je ne sais pas."
            noam "Et j'ai horreur que ce soit la seule réponse honnête."

        "Regarder les écrans avant de répondre.":
            "Je regarde les files d'attente."
            "Puis je comprends que ma réponse ne vaut pas grand-chose."
            noam "Je ne sais plus."

    noam "Je me demande si... ne rien risquer hier... c’était du confort. Ou juste de la peur."

    hide lysa

    call day4_tray_scene from _call_day4_tray_scene

    "La salle est silencieuse. Chacun fixe les écrans comme une sentence qu’on s’est nous-mêmes infligée."
    "On n’a rien gagné hier."
    "On a juste réussi à rester exactement au même endroit… en sachant qu’on aurait pu faire mieux."

    jump _4_0_TEMPS_LIBRE_1

label day4_optional_news:

    call screen day4_cafeteria_wall()

    if _return == "news":
        call screen day4_news_screen()
        "Quand je relève les yeux, les mêmes titres continuent de défiler."
        "Même file. Même attente. Même monde."
    else:
        "Je laisse les écrans tourner sans moi."

    return

label day4_tray_scene:

    $ j4_tray_eaten = []
    "Je baisse les yeux vers mon plateau."
    "Il n'y a pas grand-chose à sauver là-dedans."

label day4_tray_scene_loop:

    call screen day4_tray_pnc()

    if _return == "bread":
        $ j4_tray_eaten.append("bread")
        "Je croque."
        "Ça fait plus de bruit que de goût."
    elif _return == "ration":
        $ j4_tray_eaten.append("ration")
        "Tiède."
        "Pas chaud. Pas froid."
        "Même la température refuse de prendre parti."
    elif _return == "bar":
        $ j4_tray_eaten.append("bar")
        "Le genre d'aliment qu'on mange uniquement parce que le corps insiste."
    elif _return == "empty":
        "Je fixe le vide."
        "C'est idiot, mais c'est ça qui me met le plus en colère."
    elif _return == "finish":
        "Je repousse le plateau de quelques centimètres."
        return

    if len(j4_tray_eaten) >= 3:
        "Mon corps a compris le message avant moi."
        "Il n'y aura rien de plus."
        return

    jump day4_tray_scene_loop

label _4_0_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Après le petit-déjeuner, j'ai un peu de temps devant moi."
    "Je ne sais pas enncore quoi faire."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE")

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 1.2

    "L’après-midi traîne."
    "Pas vraiment calme. Pas vraiment vivant non plus."
    "Juste ce moment bizarre où plus personne ne sait quoi faire de sa colère."

    play sound sfx_announce
    pause 1.1

    "Le signal me vrille les oreilles."
    "Je sursaute."
    "Putain."

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention à tous mes petits représentants…"
    kami "Je vous attends dans la salle principale."
    kami "Et cette fois, j’aimerais éviter le petit numéro pathétique des gens qui boudent dans leur chambre."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On a un nouveau vote à préparer."
    kami "Alors vous marchez."
    kami "Ou je viens vous chercher avec les caméras braquées sur votre tronche."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L’écran se coupe."
    "Plus un bruit."
    "Puis des portes s’ouvrent, une à une, quelque part dans le couloir."
    "Des pas. Lents. Pas pressés."
    "On dirait moins un rassemblement qu’un transfert de détenus."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.2

    "Quand j’entre, personne ne parle."
    "Ryn est déjà là, collé au mur, les bras verrouillés sur son torse."
    "Kael garde les yeux baissés."
    "Nyra regarde l’écran noir comme si elle attendait déjà le prochain mauvais coup."
    "Tomas s’attaque à son ongle sans même s’en rendre compte."
    "Et au fond, il y a un siège vide."
    "Celui de Julian."

    "Elen arrive la dernière."
    "C'est bizarre, ça contraste fortement avec son attitude des derniers jours."
    "Là, non."
    "Elle s’assoit. C’est tout."

    $ showP("ryn", "colere", 0.50)
    ryn "Bon."
    ryn "On y est."

    $ showP("kael", "inquiet", 0.88)
    kael "Julian ne viendra pas."
    kael "J’ai frappé."
    kael "Il m’a juste dit de le laisser tranquille."

    "Personne ne commente."
    "Même Mara ne saute pas tout de suite sur l’occasion."
    "Ça en dit déjà long."

    $ showP("mara", "agace", 0.12)
    mara "Super."
    mara "Le grand architecte du changement s’effondre au premier mur."
    mara "C’était donc ça, notre pseudo leader."

    hide kael
    $ showP("tomas", "hesitation", 0.88)
    tomas "M-Mara…"

    $ showP("mara", "agace", 0.12)
    mara "Quoi ?"
    mara "On va encore faire semblant que tout va bien ?"

    "Elen ne relève même pas."
    "Elle garde les yeux fixés sur la table, comme si elle essayait juste de tenir assise."

    hide tomas
    $ showP("nyra", "raison", 0.88)
    nyra "Ça sert à rien de tirer sur une chaise vide."
    nyra "Elle ne votera pas mieux."

    "Ryn souffle du nez."
    "Un rire sans humour."

    $ showP("ryn", "colere", 0.50)
    ryn "Ouais."
    ryn "Et nous, on est là à continuer ce putain de cirque."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Parfait."
    kami "Les survivants émotionnels sont installés."
    kami "Passons donc à la suite de votre petite aventure démocratique."

    kami "Prochain vote :"

    play sound sfx_tambour
    pause 2.2

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser ou non les déplacements entre les districts ?"
    kami "Oui : libre circulation entre tous les districts."
    kami "Non : les frontières restent fermées comme aujourd’hui."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    show screen day3_codex_logo

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "C’est simple."
    kami "Même vous devriez réussir à comprendre celui-là."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    "Deux boutons apparaissent à l’écran."
    "Vert. Rouge."
    "On dirait presque un jeu."
    "Presque."

    pause 0.8

    "Personne ne parle."
    "Le mot frontières reste suspendu dans la pièce comme une odeur de brûlé."

    $ showP("lysa", "blase", 0.12)
    lysa "Vous êtes sérieux…"
    lysa "On sort à peine du désastre d’hier et on enchaîne direct sur ça ?"

    $ showP("iris", "desaccord", 0.88)
    iris "C’est n’importe quoi."
    iris "Genre, vraiment n’importe quoi."

    $ showP("elias", "determine", 0.50)
    elias "N’importe quoi, peut-être."
    elias "Mais pas inutile."

    hide iris
    $ showP("kael", "inquiet", 0.88)
    kael "Libre circulation..."
    kael "Entre tous les districts..."
    kael "Comme ça."

    hide elias
    $ showP("ryn", "colere", 0.50)
    ryn "Oui. Comme ça."
    ryn "Parce que ça fait des années qu’on nous apprend à vivre séparés comme du bétail bien rangé."
    ryn "Et parce qu’à Limen, les frontières, c’est pas une ligne sur une carte."
    ryn "C’est des types armés."
    ryn "C’est des gens qu’on enterre."
    ryn "C’est des gosses qui grandissent en pensant que de l’autre côté, y a forcément un ennemi."
    ryn "Donc ouais."
    ryn "Moi, je vote oui."

    "Sael n’a toujours pas bougé."
    "Puis elle lève enfin les yeux."
    "Et là, c’est pas de la colère que je vois d’abord."
    "C’est pire."
    "C’est quelqu’un qui a déjà vu ce qui arrive quand on ouvre trop grand une porte."

    hide kael
    $ showP("sael", "mefiant", 0.88)
    sael "Tu parles comme si ces frontières étaient gratuites."
    sael "Comme si elles étaient là pour le plaisir de nous punir."

    $ showP("ryn", "colere", 0.50)
    ryn "Tu veux qu’on dise quoi ? Merci ?"

    $ showP("sael", "determine", 0.88)
    sael "Je veux que tu arrêtes de faire semblant de ne pas savoir."
    sael "Les lignes ont été tracées dans le sang."
    sael "Des Gardiens sont morts pour les tenir."
    sael "Des villages entiers ont été rayés pour éviter que ça déborde."
    sael "Chez nous, on n’ouvre pas un passage parce qu’on se sent à l’étroit pendant une semaine."

    hide lysa
    $ showP("elias", "determine", 0.12)
    elias "Et chez nous, on crève aussi à rester chacun dans notre coin."

    $ showP("sael", "mefiant", 0.88)
    sael "Alors crève avec tes certitudes."
    sael "Mais ne demande pas aux autres de te suivre."

    "Le ton tombe d’un coup."
    "Net."
    "Tomas retire sa main de sa bouche."
    "Même Nyra cesse de sourire."

    hide elias
    $ showP("lysa", "blase", 0.12)
    lysa "Le problème, c’est qu’on n’a même pas survécu à une histoire de rationnement."
    lysa "Et là vous proposez de mélanger les districts comme si on était capables de gérer quoi que ce soit."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce qu’on doit attendre quoi, hein ?"
    ryn "Que tout soit parfait ?"
    ryn "Que Kami nous tienne encore dix ans en laisse avant qu’on mérite de respirer ?"

    hide lysa
    $ showP("iris", "desaccord", 0.12)
    iris "Respirer pour qui ?"
    iris "Parce que ce ne sera pas les plus solides qui se feront écraser, comme d’habitude."

    hide iris
    $ showP("nyra", "raison", 0.12)
    nyra "Le vrai problème, c’est pas juste ouvrir ou fermer."
    nyra "Le vrai problème, c’est qu’on n’a aucun cadre."
    nyra "Aucune règle de passage."
    nyra "Aucun contrôle."
    nyra "Rien."
    nyra "On nous balance un bouton, et débrouillez-vous."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce que fermer, ça, c’est un cadre peut-être ?"
    ryn "Interdire, abattre, isoler ?"
    ryn "Vous appelez ça une société ?"

    $ showP("sael", "determine", 0.88)
    sael "J’appelle ça une digue."

    pause 0.5

    $ showP("sael", "mefiant", 0.88)
    sael "Et vous..."
    sael "Vous me faites tous peur."

    "Le silence qui suit n’a rien à voir avec les précédents."
    "Celui-là coupe."
    "Net."

    $ showP("sael", "determine", 0.88)
    sael "Hier, vous avez reculé devant un changement économique."
    sael "Aujourd’hui, vous voulez faire sauter les frontières."
    sael "Vous ne réfléchissez pas."
    sael "Vous compensez."
    sael "Vous cherchez un grand geste pour oublier que vous avez échoué."

    "Le siège vide de Julian me saute à la gorge."
    "Personne ne regarde dans sa direction."
    "Tout le monde y pense."

    $ showP("ryn", "colere", 0.50)
    ryn "Non."
    ryn "Moi, j’en ai juste marre de vivre dans une cage."

    call day4_thread_debate_game from _call_day4_thread_debate_game

    $ showP("sael", "determine", 0.88)
    sael "Alors vote oui."
    sael "Mais ne compte pas sur moi pour ouvrir la porte."

    $ showP("sael", "colere", 0.88)
    sael "Je voterai contre."

    pause 0.2

    sael "Et cette fois, je ne bougerai pas."

    hide sael
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Sael se lève d’un coup."
    "La chaise racle violemment le sol."
    "Puis la porte claque."
    with hpunch
    with vpunch

    pause 0.6

    $ showP("mara", "agace", 0.88)
    mara "Mais c’est pas vrai..."
    mara "Vous savez faire autre chose que tout cramer ?!"
    mara "Un vote foire et maintenant tout le monde veut régler ses névroses sur le suivant ?!"

    hide mara
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Mara part juste après elle, presque en rage."

    "La salle reste ouverte."
    "Mais plus vraiment habitable."

    $ showP("tomas", "hesitation", 0.88)
    tomas "Je..."
    tomas "Je crois qu’on va trop vite."

    $ showP("ryn", "colere", 0.50)
    ryn "On va surtout nulle part."
    ryn "Comme d’habitude."

    hide tomas
    $ showP("kael", "inquiet", 0.88)
    kael "Elle n’a pas totalement tort."
    kael "On est déjà au bord de la rupture."
    kael "Et on parle d’effacer les seules limites que tout le monde connaît depuis toujours..."

    $ showP("nyra", "raison", 0.12)
    nyra "Le plus drôle, c’est qu’on n’a même pas commencé le vrai débat."
    nyra "Et pourtant, on sait déjà exactement comment ça va finir."

    "Elen bouge enfin."
    "À peine."
    "Elle relève la tête, cligne des yeux, regarde la porte par laquelle Sael vient de sortir."

    hide ryn
    $ showP("elen", "triste", 0.50)
    elen "On dirait..."
    elen "On dirait qu’on se déteste de plus en plus vite."

    "Personne ne lui répond."
    "Parce que pour une fois, elle a visé juste du premier coup."

    "Je regarde les sièges vides."
    "Julian."
    "Sael."
    "Mara."

    "Trois absences."
    "Et le vote n’a même pas commencé."

    "J’ai un nœud dans le ventre."
    "L’impression très nette qu’on n’est pas en train de préparer une décision."
    "On est en train de choisir la forme exacte de notre prochain désastre."

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    "Je sens le debat partir."
    "Pas d'un coup."
    "Comme un fil qu'on tire trop longtemps."
    "Puis le fil casse en eclats."

    call screen day4_objection_fracturee()
    $ day4_objection_return = _return
    call screen day4_objection_reward_summary()

    if day4_objection_return == "good":
        $ j4_argument_frontieres_cadre = True
        $ j4_argument_circulation_cadre = True
        noam "Attendez."
        noam "Ryn parle d'une cage. Sael parle d'une digue."
        noam "Et au fond, vous parlez tous les deux de peur."
        noam "Si on ouvre sans cadre, on transforme la liberte en abandon."
        noam "Si on ferme sans ecouter, on transforme la securite en prison."
        "Pendant une seconde, ca tient."
        "Une seule."
        think "Sael ne recule pas. Mais cette fois, je vois ce qu'elle protege vraiment : pas une frontiere. Une terreur."
        think "Et Ryn l'entend aussi. Un peu."
    elif day4_objection_return == "bad":
        noam "On peut peut-etre..."
        ryn "Non, Noam."
        ryn "La, tu fais juste joli au milieu de la piece."
        sael "Tu veux traduire une peur que tu ne connais pas."
        think "Le fil me glisse des mains."
        think "Non. Il me claque entre les doigts."
    else:
        noam "On peut ralentir deux secondes ?"
        noam "Personne ne parle vraiment de la meme chose."
        noam "Ryn parle d'etouffer. Sael parle de proteger ce qui reste."
        "Quelques regards se tournent vers moi."
        "Pas assez longtemps pour sauver le debat."
        think "Je tiens le fil. Mal. Mais je le tiens encore."

    return

label _4_0_APRES_CLASH_PRE_FETE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 2.5

    "La porte est fermée."
    "Mais l'écho du claquement est encore là."
    "Quelque chose dans l'air a changé. Pas de façon dramatique."
    "Juste… une fissure de plus dans quelque chose qui n'était déjà plus solide."

    pause 1.0

    "Les sièges vides s'accumulent."
    "Julian. Sael. Mara."
    "Trois chaises tournées vers le néant."
    "Et nous, les survivants, on reste là à fixer la table comme si elle allait nous donner les réponses."

    pause 1.2

    $ showP("ryn", "colere", 0.12)
    ryn "Super."
    ryn "On a réussi à se déchirer avant même de voter."

    $ showP("tomas", "hesitation", 0.88)
    tomas "C'est… c'est pas ce qu'on voulait."

    ryn "Et pourtant."

    "Ryn se lève. Pas pour partir. Juste parce que rester assis est insupportable."
    "Il fait deux pas vers la fenêtre opaque, les bras croisés, la nuque raide."

    hide tomas
    $ showP("kael", "inquiet", 0.50)
    $ showP("nyra", "fatigue", 0.88)
    kael "On devrait peut-être… essayer de les rejoindre ?"
    kael "Parler à Sael. Lui expliquer qu'on n'attaquait pas ses Gardiens."

    nyra "Tu as entendu sa voix quand elle est partie ?"
    nyra "Ça ne servira à rien ce soir."

    "Kael acquiesce sans conviction."
    "Il sait que Nyra a raison. Mais admettre qu'on ne peut rien faire, c'est encore pire."

    hide ryn
    hide kael

    pause 0.8

    "Je regarde Elen."
    "Elle est assise, les coudes sur les genoux, le regard posé sur ses mains."
    "Pas en larmes. Pas en colère."
    "Juste… absente."

    $ showP("elen", "triste", 0.50)
    elen "…"

    "Je m'attends à ce qu'elle dise quelque chose."
    "Un mot d'espoir. Une tentative maladroite de recoller les morceaux."
    "Rien."
    "Elen se tait. Et c'est peut-être ça le signe le plus inquiétant de la journée."

    hide nyra

    pause 1.5

    $ showP("elias", "neutre", 0.12)
    elias "Bon."
    elias "Quelqu'un propose quelque chose ?"
    elias "Ou on reste là à s'observer comme des plantes mortes ?"

    "Silence."

    $ showP("lysa", "blase", 0.88)
    lysa "Il n'y a rien à proposer, Elias."
    lysa "Pas ce soir."

    hide elias

    $ showP("iris", "hesitation", 0.12)
    iris "On pourrait aller… je sais pas. La salle de repos ?"
    iris "Essayer de décompresser un peu ?"

    lysa "Décompresser."
    lysa reflexion "Ouais. Bonne idée en théorie."

    hide lysa

    "Personne ne bouge."
    "L'idée reste suspendue dans la pièce comme une invitation que tout le monde décline tacitement."
    "Ce n'est pas qu'on ne veuille pas se détendre."
    "C'est qu'on n'en a plus la capacité."

    hide iris
    hide elen

    pause 1.0

    "Peu à peu, sans un mot, les gens se lèvent."
    "Pas ensemble. Pas en groupe."
    "Un par un. Chacun vers sa solitude."
    "Tomas part le premier, tête baissée."
    "Puis Nyra, qui glisse un \"bonne nuit\" qui sonne comme un verdict."
    "Kael sort sans se retourner."
    "Ryn disparaît dans le couloir sans que personne l'arrête."

    pause 0.8

    "Et moi."
    "Je reste là encore quelques secondes."
    "Seul dans la salle."
    "La lumière blafarde du Conclave tombe sur les chaises vides, les verres d'eau intacts, l'écran éteint."

    "On n'a pas tenu une journée entière."
    "Pas même une."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 1.0

    "Je marche lentement."
    "Le couloir est désert."
    "Quelques veilleuses clignotent au rythme d'un système qui n'a pas besoin de nous pour tourner."
    "Les portes sont closes. Derrière chacune, quelqu'un qui ruminent en silence, j'imagine."
    "Ou quelqu'un qui essaie de ne plus penser du tout."

    "Je passe devant la chambre de Julian."
    "La lumière filtre sous la porte."
    "Il est là."
    "Il n'a pas dormi non plus."
    "Mais je ne frappe pas."
    "Je ne saurais pas quoi lui dire."

    pause 0.8

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ blink()
    "Je pousse la porte de ma chambre."
    "Elle se referme dans mon dos."
    "Clic."

    "Je ne cherche pas la lumière."
    "Je n'allume rien."
    "Je m'assieds sur le bord du lit dans le noir."
    "La veilleuse bleue dessine des ombres sur le mur."

    pause 1.2

    $ blink()
    "Je repense à tout."
    "À Elen qui pleurait ce matin pour des épices."
    "À Sael qui partait en claquant la porte."
    "À Julian enfermé dans sa chambre comme si ça pouvait tout effacer."
    "Au siège vide."
    "Aux sièges vides."

    pause 0.8

    "On n'était pas forcément d'accord."
    "On n'était pas forcément proches."
    "Mais on était là."
    "Et maintenant même ça, on est en train de le perdre."

    $ blink()
    "Je m'allonge sur le dos, les bras le long du corps."
    "Le plafond est là. Inerte. Rassurant dans sa stupidité totale."

    pause 1.0

    "Je pense à ce vote qui arrive."
    "La libre circulation."
    "Un autre bouton vert ou rouge."
    "Une autre chance de rien faire, ou une autre catastrophe à vitesse accélérée."

    "Je ne sais plus ce que je veux."
    "Je ne sais plus ce qu'on est capables de faire."
    "Ensemble."

    $ blink()
    pause 0.6

    "Il y a quelque chose d'épuisant à rester conscient de son propre échec."
    "À le voir, le nommer, et ne pas savoir par quel bout le réparer."
    "On n'a même pas su faire une soirée."
    "On n'a même pas su rester dans la même pièce."

    pause 1.0

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()
    "Mes paupières tombent."
    "Pas parce que je suis en paix."
    "Juste parce que le corps abandonne avant la tête."

    "La lumière bleue pulse doucement dans le noir."
    "Quelque part dans le couloir, une porte s'ouvre puis se referme."
    "Quelqu'un d'autre qui ne dort pas."
    "Ou quelqu'un qui fait semblant."

    $ blink()
    pause 1.5

    "On a la chance d'être là."
    "D'avoir une voix. Un vote. Une salle autour d'une table."
    "Et on a quand même réussi à tout rater."

    pause 0.8

    "Je ne sais pas si demain sera mieux."
    "Je ne suis même plus sûr d'en avoir envie."

    $ blink()
    pause 2.0

    "Le sommeil arrive."
    "Lourd. Sans rêve. Sans réponse."
    "Juste le silence et la certitude d'un gâchis que je n'arrive pas encore à mesurer."

    $ current_day = 5
    pause 1.5

    #jump patreon_ending

    call end_day("5")
    jump _5_0_REVEIL_CHAMBRE

# Durée : 2m00
# Total estimé journée 4_0 : ~13-14 minutes
