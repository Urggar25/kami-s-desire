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
        idle Transform(character_image("elen", "colere"), zoom=0.75)
        hover Transform(character_image("elen", "colere_noire"), zoom=0.75)
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
    $ current_period = "Matin"

    pause 1.5  # Légèrement plus long pour accentuer la lourdeur

    $ blink()
    "Je reviens à moi sous la lumière bleue des veilleuses."
    $ blink()
    think "Hier, il a suffi d'un non. Un seul."
    think "Le bouton vert est resté éteint, et le monde a repris sa place exacte."

    $ blink()
    think "Mon cœur bat comme s'il voulait économiser ses forces."
    think "On a gardé les rations. La sécurité. Les chaînes avec."

    $ blink()
    pause 2.5  # Pause plus longue pour laisser peser le vide

    "Une photo holographique repose sur la table de nuit. Elle n'était pas là hier."
    think "Non. Je l'aurais vue."

    call day4_photo_take_trace from _call_day4_photo_take_trace

    scene bg_cg029 at adaptive_fullscreen with dissolve
    think "Le cadre est froid. Une famille sourit. Pas la mienne : des amis."
    $ unlock_gallery_image("bg_cg029")
    think "Même mes souvenirs entrent ici sans frapper."
    think "Je me demande s'ils sourient encore."

    menu:
        "Regarder la photo encore quelques secondes.":
            "Je garde le cadre levé."
            think "Les visages tremblent dans la lumière. On m'a déposé une preuve, pas un souvenir."

        "La retourner immédiatement.":
            "Je serre un peu trop fort les bords."
            think "Je n'ai pas envie que ces sourires me regardent plus longtemps."

        "Vérifier l'arrière du cadre.":
            "Je retourne le cadre."
            think "Rien. Pas de signature, pas de mot. Une surface prévue pour ne rien avouer."

    call day4_photo_put_trace from _call_day4_photo_put_trace

    "Je repose la photo face contre la table."
    think "Ça ne règle rien. Au moins, elle cesse de me regarder."

    play sound sfx_announce
    "Un bip strident déchire le silence ; l'écran s'allume."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits anges de la prudence !"
    kami "Il est huit heures et, bonne nouvelle : votre révolution a été annulée faute de participants."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit bilan matinal, puisque vous adorez qu'on récompense votre sens des responsabilités."
    kami "La situation reste impeccable : pas une pièce qui circule, pas une once de liberté qui dépasse."
    kami "Vous l'avez voulu. Vous l'avez !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C'est beau, non ? Le calme avant… le calme."
    kami "Pas d'alarme. Pas de chaos. Juste la garantie que demain ressemblera exactement à aujourd'hui."
    kami "Merci de m'avoir donné raison : l'humanité aime la liberté tant qu'elle ne menace pas le dîner."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Allez, ne faites pas cette tête !"
    kami "Vous verrez tout ça de vos propres yeux à la cafétéria. Les écrans sont chauds, vos rations sont prêtes."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    think "L'écran s'éteint. Elle laisse le silence terminer son discours."
    think "Elle n'a même pas besoin de mentir. On fait le travail à sa place."

    pause 1.8

    play sound sfx_drop
    "Un poing heurte le métal dans le couloir. Un cri bref suit, puis plus rien."
    think "Ça n'a pas encore explosé. Voilà tout ce que le silence prouve."

    jump _4_0_NAVIGATION_CAFETERIA

label day4_photo_take_trace:

    $ j4_photo_pick_trace_attempts = 0

label day4_photo_take_trace_loop:

    call screen trace_qte(path_type="curve_right", time_limit=6.0, wait_time=0.5, tolerance=70, max_errors=5, anchor_x=860, anchor_y=620)

    if _return["success"]:
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

    if _return["success"]:
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
    think "Lumière froide. Portes fermées. Personne ne veut être le premier à sortir."

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

    "À peine entré dans la cafétéria, je repère Elen près du comptoir."
    think "Elle ne parle pas. Elle bouillonne."

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
        think "Goumi reste immobile derrière le comptoir."
        think "Ses voyants suivent Elen. Il attend déjà le prochain ordre."
    elif _return == "frigo":
        think "Le frigo affiche assez pour survivre, pas assez pour oublier où on est."
    elif _return == "tables":
        think "Des plateaux occupent les tables. Personne ne semble pressé d'y toucher."
        think "Personne ne mange vraiment."

    jump _4_0_CAFETERIA_ELEN_PARTIAL

label _4_0_CAFETERIA_ECRANS:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "À peine entré dans la cafétéria, je remarque l’attroupement près du grand comptoir central."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen "Allez, Goumi, s'il te plaît ! Un peu de cannelle. Ou du poivre. Ou un truc qui prouve que j'ai encore une langue !"

    goumi "Demande refusée, représentante Elen."
    goumi "Les provisions restantes du Conclave ont été redirigées vers la Terre ce matin."

    elen "Quoi ?! Mais nooon, on n'a déjà presque rien ici !"

    elias "Moi, j'voulais juste des barres moins dégueulasses. C'est chaud, elles ont même plus de goût."

    nyra "Elen, Elias… Goumi applique un ordre. La vraie question, c'est qui cet ordre est censé aider."

    goumi "Ordre direct de Kami. Priorité absolue à la distribution planétaire."

    elen "Mais c'est injuste ! On est coincés ici et on peut même pas avoir un tout petit truc qui soit… différent ?"

    elias "Ouais, on est censés bosser pour tout le monde et on bouffe un truc que même le carton il refuserait. C'est chaud."

    nyra "Vous voulez que ça change. Je comprends. Mais crier sur Goumi, ça donne juste à Kami un meilleur spectacle."

    elen "…Je voulais juste que ça ait un peu de goût pour une fois."

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh là là, ma petite Elen… une tragédie en trois actes, avec cannelle disparue et papilles endeuillées."
    kami "Mais le Conclave ne va tout de même pas devenir un buffet pour privilégiés pendant que la Terre se serre la ceinture."
    kami "Équité. Justice. Sacrifice partagé. Vous aimiez beaucoup ces mots, hier."
    kami "Ne vous inquiétez pas trop… de nouvelles provisions arriveront au Jour 7."
    kami "En attendant, contentez-vous de ce que vous avez. Comme tout le monde."
    kami "Et surtout… comme vous l’avez vous-mêmes décidé hier."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "L’écran s’éteint."

    "Elen reste figée deux secondes, les yeux humides. Puis elle tourne les talons et sort presque en courant."

    menu:
        "Faire un pas vers Elen.":
            think "Je bouge trop tard. Elle est déjà partie."

        "Regarder Goumi.":
            think "Pas de honte. Pas d'hésitation. Un ordre exécuté."

        "Baisser les yeux vers le plateau.":
            think "Je regarde ma ration."
            think "Elle a soudain l'air encore plus petite."

    $ showP("mara", "agace", 0.70)
    mara "Génial. Kami humilie Elen et nous, on contemple le décor. Quel collectif de rêve."

    $ showP("julian", "decu", 0.50)
    julian "Nous n'avons même plus la maîtrise du goût de nos repas."
    julian "Voilà donc la grande victoire que l'histoire retiendra d'hier."

    $ showP("ryn", "colere", 0.12)
    ryn "Bravo. On a voté pour la laisse et maintenant on s'étonne qu'elle serre."

    think "Ration tiède en main, je cherche encore une façon de respirer ici."

    pause 1.2

    "Les écrans muraux s’allument enfin, montrant les mêmes images que tous les jours :"
    think "Rien n'a changé : mêmes files, même pain sec, même attente."

    hide julian
    $ showP("lysa", "determine", 0.50)
    lysa "Tout est parfaitement normal. Tantale avait au moins de vrais fruits au-dessus de la tête. Nous, on a du pain sec."

    hide mara
    $ showP("kael", "calme", 0.88)
    kael "C'est stable. Techniquement."

    $ showP("ryn", "colere", 0.12)
    ryn "Stable ? On crève lentement et poliment, oui !"

    hide lysa
    $ showP("iris", "desaccord", 0.50)
    iris "Oh, regardez : les pauvres crèvent toujours devant les mêmes murs. Quel soulagement, la stabilité fonctionne."

    hide kael
    $ showP("julian", "decu", 0.88)
    julian "Nous avions une occasion d'agir. Nous l'avons transformée en immobilisme collectif."

    think "Je pose ma ration intacte sur la table."

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
            think "Je regarde les files d'attente."
            think "Ma réponse ne vaut pas grand-chose face à ces files."
            noam "Je ne sais plus."

    noam "Je me demande si... ne rien risquer hier... c’était du confort. Ou juste de la peur."

    hide lysa

    call day4_tray_scene from _call_day4_tray_scene

    think "Chacun fixe les écrans comme une sentence collective."
    think "On n'a rien gagné. On sait seulement qu'on aurait pu faire mieux."

    jump _4_0_TEMPS_LIBRE_1

label day4_optional_news:

    call screen day4_cafeteria_wall()

    if _return == "news":
        call screen day4_news_screen()
        think "Les mêmes titres continuent de défiler."
        think "Même file. Même attente. Même monde."
    else:
        "Je laisse les écrans tourner sans moi."

    return

label day4_tray_scene:

    $ j4_tray_eaten = []
    think "Je baisse les yeux vers mon plateau."
    think "Il n'y a pas grand-chose à sauver là-dedans."

label day4_tray_scene_loop:

    call screen day4_tray_pnc()

    if _return == "bread":
        $ j4_tray_eaten.append("bread")
        "Je croque."
        think "Ça fait plus de bruit que de goût."
    elif _return == "ration":
        $ j4_tray_eaten.append("ration")
        think "Tiède. Même la température refuse de prendre parti."
    elif _return == "bar":
        $ j4_tray_eaten.append("bar")
        think "Le genre d'aliment qu'on mange uniquement parce que le corps insiste."
    elif _return == "empty":
        think "Je fixe le vide."
        think "C'est idiot, mais c'est ça qui me met le plus en colère."
    elif _return == "finish":
        "Je repousse le plateau de quelques centimètres."
        return

    if len(j4_tray_eaten) >= 3:
        think "Mon corps a compris le message : il n'y aura rien de plus."
        return

    jump day4_tray_scene_loop

label _4_0_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Après le petit-déjeuner, j'ai un peu de temps devant moi."
    think "Je ne sais pas encore quoi faire."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 1.2

    think "L'après-midi s'étire. Chacun range sa colère hors de vue."

    play sound sfx_announce
    pause 1.1

    "Le signal me vrille les oreilles."
    think "Putain."

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention, mes petits représentants en deuil démocratique…"
    kami "Salle principale. Maintenant. Même pour ceux qui boudent avec beaucoup de profondeur."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Un nouveau vote vous attend. Vous marchez, ou je transforme votre extraction en programme de divertissement."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L'écran se coupe. Des portes s'ouvrent une à une, puis des pas traînent dans le couloir."
    think "Un transfert de détenus. Il ne manque que les menottes."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.2

    think "Ryn se verrouille. Kael baisse les yeux. Tomas ronge un ongle. Nyra surveille déjà l'écran."
    think "Au fond, le siège de Julian est vide."

    think "Elen arrive la dernière. Chez elle, le silence ressemble à une alarme."

    $ showP("ryn", "colere", 0.50)
    ryn "Bon."
    ryn "On y est."

    $ showP("kael", "inquiet", 0.88)
    kael "Julian ne viendra pas. J'ai frappé. Il a dit : laisse-moi."

    think "Même Mara ne saute pas sur l'occasion. Ça en dit assez."

    $ showP("mara", "agace", 0.12)
    mara "Super. Notre grand architecte du changement rencontre un mur et se met en congé."
    mara "Quelqu'un pense à prévenir les caméras que leur héros est souffrant ?"

    hide kael
    $ showP("tomas", "hesitation", 0.88)
    tomas "M-Mara…"

    $ showP("mara", "agace", 0.12)
    mara "Quoi ?"
    mara "On va encore faire semblant que tout va bien ?"

    think "Elen fixe la table comme si elle essayait seulement de tenir assise."

    hide tomas
    $ showP("nyra", "raison", 0.88)
    nyra "Qu'est-ce que tu veux obtenir, Mara ? Parce qu'une chaise vide ne va pas mieux voter si tu l'humilies."

    think "Ryn lâche un rire sans humour."

    $ showP("ryn", "colere", 0.50)
    ryn "Ouais."
    ryn "Et nous, on est là à continuer ce putain de cirque."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Parfait. Les survivants émotionnels sont installés."
    kami "Poursuivons votre petite aventure démocratique avant une nouvelle disparition."

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

    think "Vert. Rouge. Le décor d'un jeu, sans le droit de recommencer."

    pause 0.8

    think "Le mot « frontières » reste dans l'air comme une odeur de brûlé."

    $ showP("lysa", "blase", 0.12)
    lysa "Formidable. Sisyphe vient de lâcher son rocher et on lui propose déjà une frontière à pousser."

    $ showP("iris", "desaccord", 0.88)
    iris "Oh, excellent. Une question géopolitique binaire sans protocole de transition. Qu'est-ce qui pourrait mal tourner ?"

    $ showP("elias", "determine", 0.50)
    elias "Ouais, c'est chaud comme façon de demander. Mais c'est pas inutile."

    hide iris
    $ showP("kael", "inquiet", 0.88)
    kael "Libre circulation. Tous les districts. Sans transition."

    hide elias
    $ showP("ryn", "colere", 0.50)
    ryn "Oui. Comme ça."
    ryn "Parce que ça fait des années qu’on nous apprend à vivre séparés comme du bétail bien rangé."
    ryn "Et parce qu’à Limen, les frontières, c’est pas une ligne sur une carte."
    ryn "C’est des types armés."
    ryn "C’est des gens qu’on enterre."
    ryn "C’est des gosses qui grandissent en pensant que de l’autre côté, y a forcément un ennemi."
    ryn "Donc oui. Je vote oui."

    think "Sael lève les yeux. Pas de colère : la mémoire d'une porte ouverte trop grand."

    hide kael
    $ showP("sael", "mefiant", 0.88)
    sael "Tu parles comme si ces frontières étaient gratuites."
    sael "Comme si elles étaient là pour le plaisir de nous punir."

    $ showP("ryn", "colere", 0.50)
    ryn "Tu veux qu’on dise quoi ? Merci ?"

    $ showP("sael", "determine", 0.88)
    sael "Je veux que tu arrêtes de faire semblant de ne pas savoir."
    sael "Les morts de Limen se souviennent du prix de ces lignes. Les Gardiens aussi."
    sael "Des villages entiers ont disparu pour contenir ce qui débordait. Une semaine à l'étroit n'efface pas leur sang."

    hide lysa
    $ showP("elias", "determine", 0.12)
    elias "Et chez nous, des gens crèvent parce qu'on reste chacun dans notre coin. Ça aussi, c'est du sang."

    $ showP("sael", "mefiant", 0.88)
    sael "Alors garde tes certitudes. Mais ne demande pas aux morts de les suivre."

    think "Le ton coupe net. Tomas baisse la main. Même Nyra cesse de sourire."

    hide elias
    $ showP("lysa", "blase", 0.12)
    lysa "Hier, douze personnes n'ont pas survécu intellectuellement à une histoire de rationnement."
    lysa "Aujourd'hui, vous improvisez la migration de districts entiers. L'ascension est spectaculaire."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce qu’on doit attendre quoi, hein ?"
    ryn "Que tout soit parfait ?"
    ryn "Que Kami nous tienne encore dix ans en laisse avant qu’on mérite de respirer ?"

    hide lysa
    $ showP("iris", "desaccord", 0.12)
    iris "Respirer pour qui ? Parce que les plus solides passeront. Les autres se feront piétiner, puis on appellera ça la liberté."

    hide iris
    $ showP("nyra", "raison", 0.12)
    nyra "Ryn, tu veux que les gens puissent partir sans se faire abattre. Iris, tu veux qu'ils arrivent sans se faire broyer."
    nyra "Ces deux choses ne s'opposent pas. Ce qui manque, c'est un cadre : passages, contrôles, protection."
    nyra "Kami nous donne deux boutons parce qu'elle préfère un conflit à une solution."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce que fermer, ça, c’est un cadre peut-être ?"
    ryn "Interdire, abattre, isoler ?"
    ryn "Vous appelez ça une société ?"

    $ showP("sael", "determine", 0.88)
    sael "J'appelle cela une digue. On insulte toujours les digues avant de voir l'eau."

    pause 0.5

    $ showP("sael", "mefiant", 0.88)
    sael "Et vous… vous me faites tous peur."

    think "Le silence qui suit coupe plus fort encore."

    $ showP("sael", "determine", 0.88)
    sael "Hier, vous avez reculé devant un changement économique."
    sael "Aujourd’hui, vous voulez faire sauter les frontières."
    sael "Vous ne réfléchissez pas."
    sael "Vous compensez."
    sael "Vous cherchez un grand geste pour oublier que vous avez échoué."

    think "Personne ne regarde le siège vide de Julian. Tout le monde y pense."

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
    "Sael se lève ; la chaise racle le sol, puis la porte claque."
    with hpunch
    with vpunch

    pause 0.6

    $ showP("mara", "agace", 0.88)
    mara "Vous savez faire autre chose que tout cramer ?"
    mara "Un vote foire et, soudain, chacun étale sa névrose sur la table. Même moi, j'ai des standards."

    hide mara
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Mara part juste après elle, presque en rage."

    think "La salle reste ouverte. Plus vraiment habitable."

    $ showP("tomas", "hesitation", 0.88)
    tomas "Je..."
    tomas "Je crois qu’on va trop vite."

    $ showP("ryn", "colere", 0.50)
    ryn "On va surtout nulle part."
    ryn "Comme d’habitude."

    hide tomas
    $ showP("kael", "inquiet", 0.88)
    kael "Elle n'a pas totalement tort. Rupture interne. Frontières supprimées. Deux risques qui se multiplient."

    $ showP("nyra", "raison", 0.12)
    nyra "On n'a même pas commencé le vrai débat. Alors dites-moi : vous voulez avoir raison, ou éviter qu'il finisse comme le précédent ?"

    "Elen relève enfin les yeux vers la porte."

    hide ryn
    $ showP("elen", "triste", 0.50)
    elen "On dirait..."
    elen "On dirait qu’on se déteste de plus en plus vite."

    think "Personne ne répond. Pour une fois, Elen a visé juste du premier coup."

    think "Trois sièges vides. Le vote n'a même pas commencé."
    think "On ne prépare pas une décision. On négocie la forme exacte du prochain désastre."

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    think "Le débat part comme un fil tiré jusqu'à la rupture."

    call screen day4_objection_fracturee()
    $ day4_objection_return = _return
    call screen day4_objection_reward_summary()

    if day4_objection_return == "good":
        $ j4_argument_frontieres_cadre = True
        $ j4_argument_circulation_cadre = True
        noam "Attendez."
        noam "Ryn parle d'une cage. Sael parle d'une digue. Enfin… vous parlez tous les deux de ce que vous refusez de revivre."
        noam "Si on ouvre sans cadre, la liberté devient un abandon. Si on ferme sans écouter, la sécurité reste une prison."
        think "Pendant une seconde, ça tient. Une seule."
        think "Sael ne recule pas. Mais je vois ce qu'elle protège : pas une frontière. Une terreur."
        think "Et Ryn l'entend aussi. Un peu."
    elif day4_objection_return == "bad":
        noam "On peut peut-être…"
        ryn "Non, Noam."
        ryn "Là, tu fais juste joli au milieu de la pièce."
        sael "Tu veux traduire une peur que tu ne connais pas."
        think "Le fil me glisse des mains."
        think "Non. Il me claque entre les doigts."
    else:
        noam "On peut ralentir deux secondes ?"
        noam "Personne ne parle vraiment de la même chose."
        noam "Ryn parle d'étouffer. Sael parle de protéger ce qui reste."
        think "Quelques regards se tournent vers moi. Pas assez longtemps pour sauver le débat."
        think "Je tiens le fil. Mal. Mais je le tiens encore."

    return

label _4_0_APRES_CLASH_PRE_FETE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 2.5

    think "La porte est fermée. L'écho, lui, reste."

    pause 1.0

    think "Julian. Sael. Mara. Trois sièges vides autour d'une table qui ne répondra à personne."

    pause 1.2

    $ showP("ryn", "colere", 0.12)
    ryn "Super. On a réussi à se déchirer avant même de voter."

    $ showP("tomas", "hesitation", 0.88)
    tomas "C'est… c'est pas ce qu'on voulait."

    ryn "Et pourtant."

    "Ryn se lève et gagne la fenêtre opaque, la nuque raide."

    hide tomas
    $ showP("kael", "inquiet", 0.50)
    $ showP("nyra", "fatigue", 0.88)
    kael "On devrait rejoindre Sael. Lui dire qu'on n'attaquait pas ses Gardiens."

    nyra "Tu veux réparer avant que ça durcisse. Je comprends. Mais tu as entendu sa voix : ce soir, elle n'écoutera que sa colère."

    think "Kael acquiesce sans y croire."
    think "Kael sait qu'elle a raison. L'impuissance ne lui va pas mieux qu'à nous."

    hide ryn
    hide kael

    pause 0.8

    think "Elen fixe ses mains, absente. Toujours aucun mot sur la nourriture."

    $ showP("elen", "triste", 0.50)
    elen "…"

    think "J'attends le mot d'espoir, la diversion alimentaire, n'importe quoi. Rien."

    hide nyra

    pause 1.5

    $ showP("elias", "neutre", 0.12)
    elias "Bon. Quelqu'un propose un truc ou on reste là comme des plantes mortes ? C'est chaud, même elles ont l'air plus vivantes."

    think "Personne n'a rien."

    $ showP("lysa", "blase", 0.88)
    lysa "Même Cassandre savait quand arrêter de parler. Il n'y a rien à proposer ce soir, Elias."

    hide elias

    $ showP("iris", "hesitation", 0.12)
    iris "On pourrait aller à la salle de repos. Enfin, si cette brillante assemblée sait encore décompresser sans exploser."

    lysa "Décompresser."
    lysa reflexion "Ouais. Bonne idée en théorie."

    hide lysa

    think "Personne ne bouge. L'invitation meurt sans même être refusée."

    hide iris
    hide elen

    pause 1.0

    "Ils partent un par un. Tomas d'abord, puis Nyra, Kael et Ryn. Chacun vers sa solitude."

    pause 0.8

    think "Je reste seul devant les chaises vides et les verres intacts."
    think "On n'a pas tenu une journée. Pas même une."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 1.0

    think "Le couloir est désert. Le système, lui, n'a pas besoin de nous pour tourner."

    think "De la lumière sous la porte de Julian. Je ralentis, puis je passe."
    think "Je pourrais frapper. Enfin… pour lui dire quoi ?"

    pause 0.8

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ blink()
    "La porte de ma chambre se referme d'un clic. Je m'assieds dans le noir."

    pause 1.2

    $ blink()
    think "Elen et ses épices. Sael et la porte. Julian derrière la sienne."
    think "Un siège vide, puis trois."

    pause 0.8

    think "On n'était ni d'accord ni proches. Mais on était là. Même ça, on le perd."

    $ blink()
    think "Le plafond reste inerte, rassurant dans sa stupidité totale."

    pause 1.0

    think "Libre circulation. Un autre bouton vert ou rouge."
    think "Une nouvelle chance de ne rien faire — ou d'accélérer la catastrophe."
    think "Je ne sais plus ce que je veux. Enfin, je ne sais même plus ce qu'on sait faire ensemble."

    $ blink()
    pause 0.6

    think "Voir l'échec, le nommer, puis ne rien réparer. Ma spécialité devient collective."

    pause 1.0

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()
    think "Le corps abandonne avant la tête."

    think "Une porte s'ouvre dans le couloir. Quelqu'un d'autre ne dort pas."

    $ blink()
    pause 1.5

    think "Une voix. Un vote. Une table. Et douze façons de tout rater."

    pause 0.8

    think "Demain sera peut-être mieux. Je ne suis même plus sûr d'en avoir envie."

    $ blink()
    pause 2.0

    "Le sommeil arrive, lourd, sans rêve et sans réponse."

    $ current_day = 5
    pause 1.5

    #jump patreon_ending

    call end_day("5") from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

# Durée : 2m00
# Total estimé journée 4_0 : ~13-14 minutes
