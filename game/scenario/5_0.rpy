# --------------------------------------------------------------------------------------------
# JOUR 5 — 5_0.rpy
# Vote Jour 4 : NON (status quo des rations — branche 4_0)
# Noam = narrateur principal, parle à la première personne.
# --------------------------------------------------------------------------------------------

default j50_sael_pnc_score = 0
default j50_sael_pnc_seen = []
default j50_julian_fissure = 0
default j50_wire_success = 0
default j50_wire_errors = 0
default j50_kamyz_bonus = 0
default j50_wire_selected = None
default j50_wire_done = []
default j50_wire_right_done = []
default j50_wire_connections = []
default j50_wire_time_left = 8.0
default j50_wire_lives = 3
default j50_wire_failed = False
default j50_wire_completed = False
default j50_wire_failure_has_consequences = False
default j50_kael_alert_sent = False
default j50_observation_circuit_status = "inconnu"
default j50_wire_feedback = "Sélectionne un câble à gauche."

init python:
    J50_SAEL_HOTSPOTS = {
        "lit": "images/background/interact/chambre_sael/lit.png",
        "crane": "images/background/interact/chambre_sael/crane.png",
        "affaires": "images/background/interact/chambre_sael/affaires.png",
    }

    J50_WIRE_COLORS = [
        ("rouge", "#d94040"),
        ("bleu", "#3f7fe8"),
        ("vert", "#47b86b"),
        ("jaune", "#e6c84e"),
        ("violet", "#9b63d9"),
        ("orange", "#df8a34"),
        ("rouge", "#d94040"),
        ("bleu", "#3f7fe8"),
    ]

    J50_WIRE_RIGHT_ORDER = ["bleu", "rouge", "jaune", "vert", "orange", "violet", "rouge", "bleu"]

    J50_WIRE_LEFT_YS = [170 + (idx * 85) for idx in range(len(J50_WIRE_COLORS))]
    J50_WIRE_RIGHT_YS = [170 + (idx * 85) for idx in range(len(J50_WIRE_RIGHT_ORDER))]
    J50_WIRE_BOARD_LEFT = 535
    J50_WIRE_BOARD_RIGHT = 1385

    def j50_sael_mark_seen(item):
        if item not in store.j50_sael_pnc_seen:
            store.j50_sael_pnc_seen.append(item)
            store.j50_sael_pnc_score += 1

    def j50_wire_reset(failure_has_consequences=False):
        store.j50_wire_success = 0
        store.j50_wire_errors = 0
        store.j50_wire_selected = None
        store.j50_wire_done = []
        store.j50_wire_right_done = []
        store.j50_wire_connections = []
        store.j50_wire_time_left = 8.0
        store.j50_wire_lives = 3
        store.j50_wire_failed = False
        store.j50_wire_completed = False
        store.j50_wire_failure_has_consequences = bool(failure_has_consequences)
        store.j50_wire_feedback = "Sélectionne un câble à gauche."

    def j50_wire_pick_left(idx):
        if not store.j50_wire_failed and idx not in store.j50_wire_done:
            store.j50_wire_selected = idx
            color_name = J50_WIRE_COLORS[idx][0]
            store.j50_wire_feedback = "Câble {} sélectionné — trouve son connecteur.".format(color_name.upper())
            renpy.sound.play("audio/sfx_beep.mp3")
            renpy.restart_interaction()

    def j50_wire_pick_right(connector_idx):
        idx = store.j50_wire_selected
        if idx is None or idx in store.j50_wire_done or connector_idx in store.j50_wire_right_done:
            return
        expected = J50_WIRE_COLORS[idx][0]
        color_name = J50_WIRE_RIGHT_ORDER[connector_idx]
        if expected == color_name:
            store.j50_wire_success += 1
            store.j50_wire_done.append(idx)
            store.j50_wire_right_done.append(connector_idx)
            store.j50_wire_connections.append((idx, connector_idx))
            store.j50_wire_time_left = 8.0
            store.j50_wire_feedback = "CONNEXION VERROUILLÉE — chronomètre réinitialisé."
            renpy.sound.play("audio/sfx_qte_hit.wav")
            if store.j50_wire_success >= len(J50_WIRE_COLORS):
                store.j50_wire_completed = True
        else:
            store.j50_wire_errors += 1
            store.j50_wire_feedback = "MAUVAISE COULEUR — la liaison est refusée."
            renpy.sound.play("audio/sfx_qte_miss.wav")
        store.j50_wire_selected = None
        renpy.restart_interaction()

    def j50_wire_tick(delta=0.1):
        if store.j50_wire_failed or store.j50_wire_completed:
            return

        store.j50_wire_time_left = round(max(0.0, store.j50_wire_time_left - delta), 1)
        if store.j50_wire_time_left <= 0.0:
            store.j50_wire_lives = max(0, store.j50_wire_lives - 1)
            store.j50_wire_errors += 1
            store.j50_wire_selected = None
            store.j50_wire_time_left = 8.0
            renpy.sound.play("audio/sfx_qte_miss.wav")

            if store.j50_wire_lives <= 0:
                store.j50_wire_failed = True
                store.j50_wire_feedback = "ÉCHEC — alimentation de secours interrompue."
            else:
                store.j50_wire_feedback = "TEMPS ÉCOULÉ — reprise d'urgence : 8,0 s."

        renpy.restart_interaction()

    def j50_wire_abandon():
        store.j50_wire_lives = 0
        store.j50_wire_failed = True
        store.j50_wire_selected = None
        store.j50_wire_feedback = "CONNEXION ABANDONNÉE."
        renpy.restart_interaction()

screen j50_sael_room_pnc():
    modal True
    zorder 200

    add Solid("#000")
    add "images/background/scene/bg_chambre_sael.png" at cover_screen

    for item, path in J50_SAEL_HOTSPOTS.items():
        imagebutton:
            idle room_interaction_null()
            hover room_interaction_layer(path, "chambre_sael", "hover")
            focus_mask room_interaction_layer(path, "chambre_sael", "art")
            xpos 0
            ypos 0
            action Return(item)

screen j50_julian_surveillance_overlay(room_name="CHAMBRE 04"):
    zorder 180
    add Solid("#3d536033")
    add Solid("#00000033")
    frame:
        xpos 42
        ypos 34
        padding (18, 10)
        background Solid("#05090acc")
        hbox:
            spacing 18
            text "REC" size 34 color "#ff3b3b" font "fonts/Rajdhani-SemiBold.ttf"
            text "[room_name]" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
            text "13:42:08" size 30 color "#9ed8ff" font "fonts/Rajdhani-SemiBold.ttf"
    frame:
        xpos 1450
        ypos 34
        padding (18, 10)
        background Solid("#05090acc")
        text "KAMI OBSERVE" size 28 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
    for y in range(0, 1080, 54):
        add Solid("#ffffff08") xpos 0 ypos y xsize 1920 ysize 2

transform j50_wire_selected_pulse:
    alpha 0.62
    linear 0.30 alpha 1.0
    linear 0.30 alpha 0.62
    repeat

screen j50_wire_minigame(failure_has_consequences=False):
    modal True
    zorder 220
    on "show" action Function(j50_wire_reset, failure_has_consequences)

    add "gui/day5/wire/wire_hud_background.png":
        xysize (1920, 1080)

    add Solid("#03101a44")

    text "▮▮  MINI-JEU : CONNEXION":
        xpos 54
        ypos 22
        size 30
        color "#55adff"
        font "fonts/Rajdhani-SemiBold.ttf"

    text "Raccordez les 8 fils par couleur avant que la batterie de contrôle s'épuise.":
        xpos 690
        ypos 25
        xsize 1180
        text_align 1.0
        size 23
        color "#bdc9d5"
        font "fonts/Barlow-Light.ttf"

    # Huit raccordements à rétablir ; chaque bonne liaison réinitialise le délai.
    for left_idx, right_idx in j50_wire_connections:
        $ _wire_color = J50_WIRE_COLORS[left_idx][1]
        $ _wire_y1 = J50_WIRE_LEFT_YS[left_idx]
        $ _wire_y2 = J50_WIRE_RIGHT_YS[right_idx]
        $ _wire_mid = 710 + ((left_idx % 6) * 105)
        $ _wire_top = min(_wire_y1, _wire_y2)
        $ _wire_height = max(4, abs(_wire_y2 - _wire_y1))

        add Solid("#000814cc") xpos J50_WIRE_BOARD_LEFT ypos (_wire_y1 - 5) xsize (_wire_mid - J50_WIRE_BOARD_LEFT + 5) ysize 12
        add Solid("#000814cc") xpos (_wire_mid - 5) ypos _wire_top xsize 12 ysize (_wire_height + 5)
        add Solid("#000814cc") xpos _wire_mid ypos (_wire_y2 - 5) xsize (J50_WIRE_BOARD_RIGHT - _wire_mid) ysize 12
        add Solid(_wire_color + "55") xpos J50_WIRE_BOARD_LEFT ypos (_wire_y1 - 4) xsize (_wire_mid - J50_WIRE_BOARD_LEFT) ysize 9
        add Solid(_wire_color + "55") xpos (_wire_mid - 4) ypos _wire_top xsize 9 ysize _wire_height
        add Solid(_wire_color + "55") xpos _wire_mid ypos (_wire_y2 - 4) xsize (J50_WIRE_BOARD_RIGHT - _wire_mid) ysize 9
        add Solid(_wire_color) xpos J50_WIRE_BOARD_LEFT ypos (_wire_y1 - 1) xsize (_wire_mid - J50_WIRE_BOARD_LEFT) ysize 3
        add Solid(_wire_color) xpos (_wire_mid - 1) ypos _wire_top xsize 3 ysize _wire_height
        add Solid(_wire_color) xpos _wire_mid ypos (_wire_y2 - 1) xsize (J50_WIRE_BOARD_RIGHT - _wire_mid) ysize 3

    # Connecteurs gauches.
    for idx, wire in enumerate(J50_WIRE_COLORS):
        $ color_name, color_hex = wire
        $ _left_y = J50_WIRE_LEFT_YS[idx]
        button:
            xpos 466
            ypos (_left_y - 24)
            xsize 82
            ysize 48
            padding (0, 0)
            background None
            sensitive idx not in j50_wire_done and not j50_wire_failed
            action Function(j50_wire_pick_left, idx)
            if idx == j50_wire_selected:
                at j50_wire_selected_pulse
            hbox:
                xalign 1.0
                yalign 0.5
                spacing 8
                text "[idx + 1:02d]" size 16 color "#8296aa" font "fonts/Rajdhani-SemiBold.ttf"
                text "●" size 42 color ("#314354" if idx in j50_wire_done else color_hex) outlines [(3, "#08121d", 0, 0), (1, "#dff8ff", 0, 0)]

    # Connecteurs droits mélangés.
    for connector_idx, color_name in enumerate(J50_WIRE_RIGHT_ORDER):
        $ color_hex = dict(J50_WIRE_COLORS).get(color_name, "#ffffff")
        $ _right_y = J50_WIRE_RIGHT_YS[connector_idx]
        button:
            xpos 1371
            ypos (_right_y - 24)
            xsize 84
            ysize 48
            padding (0, 0)
            background None
            sensitive connector_idx not in j50_wire_right_done and j50_wire_selected is not None and not j50_wire_failed
            action Function(j50_wire_pick_right, connector_idx)
            hbox:
                yalign 0.5
                spacing 8
                text "●" size 42 color ("#314354" if connector_idx in j50_wire_right_done else color_hex) outlines [(3, "#08121d", 0, 0), (1, "#dff8ff", 0, 0)]
                text "[connector_idx + 1:02d]" size 16 color "#8296aa" font "fonts/Rajdhani-SemiBold.ttf"

    # Colonne de gauche : délai par connexion, progression et vies.
    frame:
        xpos 58
        ypos 78
        xsize 366
        ysize 245
        padding (26, 22)
        background Solid("#020a12aa")
        vbox:
            spacing 8
            text "TEMPS RESTANT" size 25 color "#62b5ff" font "fonts/Rajdhani-SemiBold.ttf"
            $ _wire_time_text = "{:.1f}".format(j50_wire_time_left)
            text "[_wire_time_text]":
                size 76
                color ("#ff626f" if j50_wire_time_left <= 1.0 else "#70baff")
                font "fonts/Rajdhani-SemiBold.ttf"
                outlines [(2, "#0d2e4d", 0, 0)]
            hbox:
                xfill True
                bar value AnimatedValue(j50_wire_time_left, 8.0, delay=0.1):
                    xsize 260
                    ysize 14
                    left_bar Solid("#428fda")
                    right_bar Solid("#152536")
                text " SEC" size 20 color "#a9b6c2"

    frame:
        xpos 58
        ypos 356
        xsize 366
        ysize 245
        padding (26, 24)
        background Solid("#020a12aa")
        vbox:
            spacing 13
            text "PROGRESSION" size 25 color "#62b5ff" font "fonts/Rajdhani-SemiBold.ttf"
            text "[j50_wire_success] / [len(J50_WIRE_COLORS)]" size 54 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
            hbox:
                spacing 7
                for progress_idx in range(len(J50_WIRE_COLORS)):
                    text "●" size 19 color ("#59b6ff" if progress_idx < j50_wire_success else "#344658")

    frame:
        xpos 58
        ypos 635
        xsize 366
        ysize 270
        padding (26, 22)
        background Solid("#020a12aa")
        vbox:
            spacing 13
            text "INTÉGRITÉ" size 25 color "#62b5ff" font "fonts/Rajdhani-SemiBold.ttf"
            hbox:
                spacing 18
                for life_idx in range(3):
                    text "◆" size 42 color ("#ff6574" if life_idx < j50_wire_lives else "#3a4652") outlines [(2, "#40141c", 0, 0)]
            text "3 tentatives avant panne du boîtier" size 19 color "#9fb0bf"
            text "Une bonne liaison remet le délai à 8,0 s." size 18 color "#73899c" xsize 310

    # Colonne de droite : cible et retour système.
    frame:
        xpos 1497
        ypos 78
        xsize 365
        ysize 405
        padding (26, 24)
        background Solid("#020a12aa")
        vbox:
            spacing 19
            text "COMBINAISON ACTIVE" size 24 color "#62b5ff" font "fonts/Rajdhani-SemiBold.ttf"
            if j50_wire_selected is None:
                text "EN ATTENTE" size 34 color "#65798c" font "fonts/Rajdhani-SemiBold.ttf"
                text "Choisis un câble dans la rangée de gauche." size 21 color "#aab8c4" xsize 300
            else:
                $ _selected_name, _selected_color = J50_WIRE_COLORS[j50_wire_selected]
                text "●" size 82 color _selected_color xalign 0.5 outlines [(5, "#08121d", 0, 0), (2, "#dff8ff", 0, 0)]
                text _selected_name.upper() size 34 color "#dff8ff" xalign 0.5 font "fonts/Rajdhani-SemiBold.ttf"
                text "Trouve le connecteur identique à droite." size 20 color "#aab8c4" xsize 300 text_align 0.5

    frame:
        xpos 1497
        ypos 520
        xsize 365
        ysize 385
        padding (26, 24)
        background Solid("#070b12cc")
        vbox:
            spacing 18
            text ("ÉCHEC" if j50_wire_failed else "ATTENTION") size 28 color ("#ff6574" if j50_wire_failed or j50_wire_time_left <= 1.0 else "#ffb55f") font "fonts/Rajdhani-SemiBold.ttf"
            text "[j50_wire_feedback]" size 22 color "#d2dce5" xsize 305
            text "Erreurs : [j50_wire_errors]" size 20 color "#8296aa"

    textbutton "ESC  ABANDONNER":
        xpos 60
        ypos 1010
        text_size 20
        text_color "#9aabba"
        background None
        action Function(j50_wire_abandon)

    key "K_ESCAPE" action Function(j50_wire_abandon)
    timer 0.1 repeat True action Function(j50_wire_tick, 0.1)
    if j50_wire_failed:
        timer 0.35 action Return(False)
    if j50_wire_completed:
        timer 0.35 action Return(True)

label _5_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 5
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"
    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ cafeteria_food_level = "medium"
    $ j50_kael_alert_sent = False
    $ j50_observation_circuit_status = "inconnu"

    $ blink()
    think "Huit heures. J'ai pourtant l'impression d'avoir passé la nuit entière à fixer le plafond."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Ma tablette vibre. Pas un message : un rappel pour le vote de demain. J'avais presque réussi à oublier qu'on avait encore un scrutin à perdre."
    think "Sael a déjà annoncé son non. Hier soir, j'ai vu Mara entrer dans sa chambre, sans entendre ce qu'elles se sont dit."
    think "Et Julian... lui qui se jetterait devant une caméra pour annoncer qu'il a retrouvé une chaussette n'a pas reparu."
    think "Je ne sais pas ce qui m'inquiète le plus : qu'il prépare un discours ou qu'il n'en prépare plus."
    "Je repose la tablette. Aujourd'hui, je vais commencer par quelqu'un qui n'a pas besoin de public."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "BOOOONJOUR, mes adorables représentants ! Toujours aussi reposés, à ce que je vois. Vos cernes pourraient presque siéger à votre place !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Le petit-déjeuner est servi ! Même menu que prévu. Et inutile de harceler ce pauvre Goumi pour des extras : prochaine livraison au jour 7."
    kami "Oui, Elen, ça inclut la cannelle. Je te vois venir."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et demain... NOUVEAU VOTE ! Encore un jour pour vous convaincre, vous menacer ou vous ignorer. Personnellement, j'ai beaucoup aimé la deuxième méthode hier."
    kami "Ou était-ce la première ? Oh, vous êtes si difficiles à suivre quand vous criez tous en même temps !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Je croque dans le pain d'hier."
    think "Il a la consistance d'une pièce détachée. Elias saurait sûrement quoi en faire."
    think "La cafétéria peut attendre. Si je veux parler à Sael sans avoir dix personnes pour nous couper la parole, c'est maintenant."
    "J'attrape ma tablette et sors avant de trouver une bonne excuse pour remettre ça à demain."

    stop music fadeout 1.2

    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_231
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.0

    think "Un tissu noir est noué à sa poignée. Sael a même réussi à rendre une porte de dortoir reconnaissable."
    think "Je frappe. Une fois. Deux fois. J'espère qu'elle n'a pas décidé de me démonter comme son lit."
    play sound sfx_knock
    pause 0.5
    play sound sfx_door
    $ showGroup([("sael", "mefiant", 0.65), ("noam", "reflexion", 0.30)])
    sael mefiant "Noam."
    sael mefiant "Tu veux parler des frontières, je suppose."
    if j4_frontieres_result == "pont":
        sael reflechit "J'ai repensé à ce que Ryn a dit. Pour la première fois, j'ai eu envie de lui répondre autrement qu'en criant."
    elif j4_frontieres_result == "rupture":
        sael mefiant "Si tu viens me dire de me calmer, la porte est juste derrière toi."
        noam inquiet "Non. Hier, j'ai déjà suffisamment parlé à votre place."
    noam inquiet "Un peu. Mais je peux aussi juste te dire bonjour et repartir. Ce serait une rencontre très réussie."
    sael neutre "Tu as fait tout ce chemin pour me dire bonjour ?"
    sael neutre "Entre. Au moins, ici, on pourra terminer nos phrases."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_sael") from _call_MAYBE_PLAY_SCRIPTED_DOOR_232
    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    think "J'entre. Pendant une seconde, je crois m'être trompé de chambre."
    think "Le lit a disparu. Enfin, pas tout à fait : ses planches sont contre le mur et le matelas repose par terre. Des objets en bois et en os occupent l'espace laissé libre."
    sael reflechit "Tu peux regarder. Mais pas toucher aux objets au mur."
    sael sourire "Je préfère te le dire avant qu'une curiosité maladroite ne finisse en accident diplomatique."

    $ j50_sael_pnc_score = 0
    $ j50_sael_pnc_seen = []
    call _5_0_SAEL_PNC from _call_5_0_SAEL_PNC
    $ showGroup([("noam", "hesitation", 0.25), ("sael", "neutre", 0.75)])

    noam reflexion "Je pensais qu'on ne pouvait même pas régler la hauteur du lit. Toi, tu l'as carrément abattu."
    sael neutre "Il était trop haut, trop mou. Je dors mieux près du sol. Les planches pourront servir, au lieu de prendre la poussière."
    noam sourire "Kael doit rêver de récupérer toutes ces vis."
    sael sourire "Il est venu hier. Pour les vis, justement."
    sael neutre "J'ai refusé."
    think "Évidemment. Les ingénieurs sont prévisibles."
    "Sael m'indique un tabouret."
    think "J'inspecte discrètement ses pieds avant de m'asseoir. On ne sait jamais quels meubles elle a démontés."
    noam inquiet "Hier, quand tu as parlé de ton village... Tu t'es arrêtée comme si tu retenais quelque chose."
    noam inquiet "Je ne te demande pas de tout raconter. Je voulais juste savoir si ça allait."
    sael triste "Je n'allais pas raconter ce que nous avons vécu pendant que Ryn me hurlait dessus."
    sael mefiant "Et puis je vous connais depuis quatre jours. Tu me demandes beaucoup."
    noam neutre "Tu as raison. Je ne voulais pas te forcer."
    noam inquiet "Mais quand Ryn parle des corps à la frontière... je crois qu'il ne sait plus comment demander de l'aide sans s'énerver."
    sael determine "Je l'ai compris, Noam. Je n'ai pas besoin qu'on m'explique ce qu'est un mort."
    sael triste "Chez nous aussi, il y en a eu. Pas seulement parmi les hommes qui venaient nous attaquer."
    "Elle se penche pour ramasser un petit outil tombé près du matelas. Sa main reste un instant refermée dessus."
    noam inquiet "C'est un objet de ton village ?"
    sael mefiant "Tu es venu pour inspecter mes affaires ou pour parler ?"
    noam inquiet "Pour parler. Désolé."
    sael neutre "Il servait à réparer les clôtures. On les réparait sans arrêt, avant."
    noam inquiet "À cause des groupes armés ?"
    sael triste "Ils entraient par les champs. Les premières fois, on cherchait surtout à récupérer les outils volés."
    sael triste "Après, on cherchait ceux qui n'étaient pas rentrés."
    "Elle pose l'outil sur la table, loin de moi."
    sael neutre "Depuis la fermeture, les enfants peuvent retourner dehors sans qu'on les surveille à chaque instant."
    noam reflechit "Et ceux qui ont de la famille derrière la frontière ?"
    sael mefiant "Je sais. Je les ai entendus, hier. Je ne suis pas sourde parce que je ne suis pas d'accord."
    noam reflechit "À Harmonie, on parle surtout des familles séparées. Je n'avais pas imaginé ce que l'ouverture pouvait signifier pour toi."
    $ unlock_dossier_arg("p2_familles")
    sael mefiant "Et tu voudrais que je mette mon village en danger pour réparer ce que ces familles subissent ?"
    noam inquiet "Non ! Je voulais juste comprendre ce que le texte te demandait de risquer."
    sael reflechit "Alors arrête d'essayer de me trouver une réponse avant que j'aie fini de parler."
    "Je referme la bouche. Pour une fois, c'est peut-être la contribution la plus utile que je puisse apporter."
    sael triste "Ryn n'a pas inventé ses morts. Moi non plus."
    noam neutre "Tu pourrais lui dire ça."
    sael mefiant "Quand il me laissera placer trois mots sans me traiter de lâche, peut-être."
    noam inquiet "Oui. Ce serait un début."
    sael neutre "Je lui reparlerai quand il sera capable de m'écouter."
    sael determine "Mais le scrutin, lui, n'attendra pas notre réconciliation."
    noam inquiet "Et si on trouvait une surveillance qui empêche les groupes armés de revenir ?"
    sael determine "Alors je lirais ce projet avec attention."
    sael determine "Mais ce n'est pas le texte de demain. Demain, on ouvre tout, sans rien prévoir pour protéger les villages."
    sael determine "Je voterai contre. Ce n'est pas négociable."
    noam triste "D'accord."
    think "J'étais venu comprendre. Une partie de moi espérait quand même trouver le mot qui la ferait hésiter."
    sael reflechit "Mara est passée hier soir. Elle aussi a des réserves sur l'ouverture."
    sael mefiant "Je te le précise avant que quelqu'un invente une alliance entre nous."
    noam surpris "Elle était donc contre, elle aussi ?"
    sael neutre "C'est ce qu'elle m'a dit. Mais va lui demander ce qu'elle en pense si tu veux comprendre ses raisons."
    sael neutre "Je ne vais pas me mettre à voter à sa place en plus de la mienne."
    "Sael m'accompagne jusqu'à la porte. Elle pose la main sur la poignée, sans l'ouvrir."
    sael triste "Tu sais... moi aussi, j'aimerais revoir des gens qui vivent ailleurs."
    sael triste "Je ne défends pas les frontières parce que j'aime enfermer les autres."
    noam calme "Je crois que je commence à le comprendre."
    noam calme "Merci de m'avoir laissé entrer."
    sael neutre "Et une dernière chose : ne va pas faire le tour des chambres en répétant ton argument jusqu'à ce que quelqu'un cède."
    sael sourire "On a déjà Julian pour ça."
    noam sourire "Promis. Une campagne électorale dans les couloirs, ça me fatigue déjà rien que d'y penser."
    noam neutre "Bonne journée, Sael."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_233
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    think "Sael votera non. Je le savais avant de frapper."
    "J'ai encore en tête le petit outil qu'elle a posé hors de ma portée. Je ne lui ai pas demandé à qui il appartenait."
    think "Mara est venue hier. Sael dit qu'elle aussi a des réserves. Il faudra que je lui parle, sans inventer leur vote à leur place."
    think "Une chose est sûre : je n'ai toujours pas envie de me transformer en Julian."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)

    jump _5_0_TEMPS_LIBRE_1

label _5_0_TEMPS_LIBRE_1:
    call START_FREE_TIME("_5_0_APRES_TEMPS_LIBRE_1") from _call_START_FREE_TIME_2

label _5_0_APRES_TEMPS_LIBRE_1:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_234
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8

    think "J'ai passé la matinée à chercher une manière de faire entendre deux peurs qui se contredisent."
    think "Il me reste l'après-midi. Et deux endroits où je risque d'apprendre quelque chose... ou de faire une bêtise."
    think "Julian n'a toujours pas montré le bout de son nez. D'habitude, je rêve qu'il parle moins. Là, son silence commence à m'inquiéter."
    think "Ou alors, la salle d'observation. Des chiffres, des images de la Terre. Peut-être des réponses qu'aucun représentant n'aura besoin de crier."

label _5_0_CRITICAL_CHOICE:

    menu (screen="critical_choice", noam_expr="hesitation", cc_prompt="Où devrais-je aller ?", cc_targets={"Aller frapper à la porte de Julian.":{"label":"_5_0_0_JULIAN","pack":"mystere"},"Aller à la salle d'observation.":{"label":"_5_0_1_OBSERVATION","pack":"origine"}}):
        "Où devrais-je aller ?"

        "Aller frapper à la porte de Julian.":
            $ doplleganger = 0
            jump _5_0_0_JULIAN

        "Aller à la salle d'observation.":
            $ doplleganger = 1
            jump _5_0_1_OBSERVATION


label _5_0_0_JULIAN:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_235
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ doplleganger = 0
    think "Je frappe. Aucune réponse."
    think "Je recommence, un peu plus fort. Julian qui refuse un public, c'est décidément mauvais signe."
    play sound sfx_knock
    pause 0.5
    noam neutre "Julian ? C'est Noam. Je ne viens pas te faire un discours. Promis, ça tiendra en moins de dix minutes."
    "Quelque chose bouge derrière la porte. Enfin, le verrou cède."
    play sound sfx_door
    $ showGroup([("julian", "neutre", 0.65), ("noam", "neutre", 0.30)])
    julian taquin "Tiens donc. Mon conseiller en bonnes manières."
    julian taquin "Tu viens me rappeler qu'il faut accepter la défaite avec le sourire ?"
    noam inquiet "Non. Tu as disparu depuis le vote et personne ne sait vraiment comment tu vas."
    julian sourire "Formidablement bien ! Debout, propre, habillé !"
    julian sourire "Tu peux annoncer aux autres que le patient respire encore."
    noam colere "Tu pourrais arrêter ton numéro trente secondes ? Je ne suis pas venu pour te ridiculiser."
    "Son sourire s'efface. Il hésite, puis s'écarte de la porte."
    think "C'est peut-être la première fois que je gagne une dispute avec Julian sans le vouloir."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_236
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "sourire", 0.65), ("noam", "reflexion", 0.30)])
    think "Sa chambre est impeccable. Même les affaires sur le bureau semblent avoir été alignées pour une photo."
    think "Seule sa tablette détonne : la rediffusion du vote tourne en boucle."
    noam inquiet "Attends... tu revois encore le dépouillement ?"
    julian decu "J'essaye de voir à quel moment tout nous a échappé. Je pensais vraiment qu'on y arriverait."
    noam neutre "Le texte supprimait les rations. Beaucoup n'étaient pas prêts à accepter ça."
    julian colere "JE SAIS ! J'étais là ! J'ai entendu exactement les mêmes arguments que toi !"
    noam inquiet "Alors pourquoi tu regardes les autres comme s'ils avaient tout gâché par stupidité ?"
    julian neutre "Parce que je suis furieux. Ça t'arrive de ressentir autre chose que de la déception polie ?"
    "Julian saisit le brouilleur posé près de la tablette. Il coupe l'appareil d'un geste précis."
    think "Je commence à lui demander ce qu'il fait quand un voyant s'éteint au plafond."
    $ unlock_codex_page("surveillance_conclave", with_notification=False)
    julian taquin "Tiens. Je vais te montrer ce que j'appelle une gestion de crise."
    julian sourire "Regarde la caméra."
    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3
    "La caméra pivote. Julian redresse les épaules, baisse les yeux, puis prend soudain l'air d'un homme que le monde aurait personnellement trahi."
    think "C'est... impressionnant de rapidité."
    julian triste "J'ai tout donné pour ce premier vote. Nous avions la possibilité de rendre espoir à des millions de personnes..."
    julian triste "Et nous avons échoué. Mais je ne renoncerai pas."
    julian decu "À tous ceux qui nous regardent : votre confiance ne sera pas trahie. Je continuerai à porter vos attentes."
    noam surpris "Attends... Tu es en train de faire un discours ? Là ?!"
    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    "Le brouilleur se rallume. Julian se détend instantanément."
    think "Je viens d'assister au changement de costume le plus rapide de l'histoire. Sans costume."
    julian rire "Alors ? Le regard, la voix, la petite pause ? Je trouve ça très convaincant."
    noam colere "TU TE FOUS DE MOI ?! Tu as joué l'homme brisé devant une caméra !"
    julian taquin "Je savais que tu réagirais comme ça. Les gens ont besoin de savoir que quelqu'un continue à se battre pour eux."
    julian sourire "Ce n'est pas ma faute si j'ai une présence naturelle."
    noam inquiet "Et leur parler normalement ? Sans réciter le discours du siècle ?"
    julian neutre "Normalement, on parle sous le coup de la colère. On dit ce qu'on pense, même quand ce n'est pas malin."
    julian neutre "Et Kami choisit le pire passage à montrer au monde."
    noam reflechit "Hier, quand tu as hurlé sur tout le monde... Ça aussi, c'était calculé ?"
    julian decu "Non."
    julian decu "J'étais sincèrement furieux. Tu peux ressentir quelque chose et ne pas avoir envie que le monde te voie t'effondrer."

    $ j50_julian_fissure = 0
    menu:
        "Lui reprocher de penser à sa réputation.":
            $ j50_julian_fissure += 1
            noam colere "Par moments, j'ai l'impression que tu t'inquiètes davantage de l'image de Julian que des gens qu'on est censés représenter."
            julian colere "Et tu crois qu'ils nous écouteront s'ils pensent qu'on est incapables de s'entendre sur quoi que ce soit ?!"
        "Reconnaître qu'il est réellement déçu.":
            $ j50_julian_fissure -= 1
            noam neutre "Je te crois sur ta déception. Je ne dis pas que tu joues tout le temps. Je dis que tu as fait du mal à Tomas."
            julian decu "Ça... oui. J'ai insisté beaucoup trop longtemps avec Tomas."
            julian hesitation "Je pensais vraiment pouvoir le convaincre."
        "Lui demander pourquoi il a autant insisté auprès de Tomas.":
            noam inquiet "Tu as coincé Tomas dans la salle de repos et tu voulais lui faire annoncer ton opinion. Ce n'était plus une discussion."
            julian hesitation "J'avais peur qu'il vote contre sans avoir compris les conséquences."
            julian hesitation "Alors j'ai insisté. Beaucoup trop, visiblement."

    julian neutre "J'avais préparé ce premier vote dans ma tête cent fois."
    julian decu "Si on réussissait dès le début, les gens arrêteraient peut-être de nous prendre pour des gamins enfermés dans une station."
    noam reflechit "Et maintenant, tu veux savoir qui a dit non. Tu ne crois pas que ça rendra les gens encore plus méfiants ?"
    julian colere "Je veux comprendre pourquoi quelqu'un a choisi de tout bloquer ! C'est vraiment si incompréhensible ?"
    noam neutre "Je le comprends. Mais le bulletin secret permet aussi à quelqu'un de te contredire sans craindre tes réactions."
    "Julian ouvre la bouche. Je m'attends à recevoir un nouveau discours."
    "Il finit par regarder la rediffusion sans rien dire."
    julian decu "Tu sais ce qui me fait vraiment mal ?"
    julian decu "Si le prochain texte passe, tout le monde retiendra cette victoire-là. Personne ne se souviendra de tout ce qu'on a essayé avant."
    noam surpris "Attends. Tu voudrais qu'on réussisse... mais pas si quelqu'un d'autre en récolte les félicitations ?"
    julian colere "MAIS SI ! ÉVIDEMMENT QUE JE VOUDRAIS QU'ON RÉUSSISSE !"
    "Il répond trop vite. Même lui semble surpris par sa propre voix."
    julian hesitation "Enfin... j'aurais voulu que ce soit le premier."
    julian decu "Je m'étais imaginé que ça changerait quelque chose pour nous."

    menu:
        "Lui dire qu'il n'a rien à prouver.":
            $ j50_julian_fissure += 1
            noam neutre "Tu sais, on peut te prendre au sérieux sans que tu gagnes toutes les batailles."
            julian inquiet "C'est facile à dire quand tu n'as pas passé deux jours à promettre qu'on pouvait y arriver."
        "Lui demander ce qui l'inquiète vraiment.":
            $ j50_julian_fissure += 1
            noam inquiet "Tu as peur qu'on oublie tes efforts... ou qu'on se souvienne seulement de ton échec ?"
            julian hesitation "Je ne veux pas être celui qui a promis à tout le monde que les choses allaient changer... et qui a échoué au premier essai."
        "Lui répondre que le résultat compte davantage.":
            $ j50_julian_fissure -= 1
            noam colere "Ce n'est pas un concours de popularité. On représente des gens, pas notre propre réputation."
            julian colere "JE SAIS ! Tu n'es pas obligé de me le rappeler comme si j'avais cinq ans !"

    "Julian reprend le brouilleur et le fait tourner entre ses doigts. La caméra ne l'intéresse plus."
    think "Je commence à croire que les moments où il ne joue aucun rôle sont ceux où il parle le moins."
    julian neutre "Demain, on vote sur les frontières. Ryn va crier, Sael va dire non, et notre belle expérience démocratique s'arrêtera au même endroit."
    noam inquiet "J'ai parlé à Sael. Elle a des raisons que je ne peux pas simplement balayer."
    julian reflechit "Elle t'a reçu ?"
    julian taquin "Tu dois avoir un talent caché. Avec moi, elle n'a même pas voulu commencer."
    noam calme "Tu pourrais peut-être commencer par leur demander ce qu'ils craignent au lieu d'arriver avec la conclusion."
    julian decu "Je t'ai entendu, Noam. Tu serais surpris du nombre de choses que j'entends."
    julian decu "C'est juste... plus difficile à appliquer que ça en a l'air."

    menu:
        "Lui proposer de sortir voir les autres.":
            $ j50_julian_fissure += 1
            noam sourire "Viens au moins prendre un repas avec nous. On peut même parler de la nourriture. Elen a beaucoup d'avis là-dessus."
            julian hesitation "Peut-être ce soir. Je n'ai pas envie de retrouver Ryn tout de suite."
        "Lui demander de s'excuser auprès de Tomas.":
            $ j50_julian_fissure += 1
            noam neutre "Et Tomas ? Tu pourrais lui présenter des excuses. Pas devant les caméras, pour une fois."
            julian decu "Oui... Je sais. Mais je préférerais ne pas faire ça devant tout le monde."
            julian hesitation "Je sais ce que je dois lui dire. C'est le moment de le dire qui me manque."
        "Lui dire qu'il se complique la vie.":
            $ j50_julian_fissure -= 1
            noam sourire "Tu travailles incroyablement dur pour un type qui prétend que tout lui vient naturellement."
            julian taquin "L'excellence demande des sacrifices. J'aurais cru que tu l'avais compris."

    if j50_julian_fissure >= 3:
        julian inquiet "Noam... Si demain vous réussissez sans moi, tu crois que les autres voudront encore m'écouter ?"
        noam surpris "Julian, on n'est pas en train de choisir un chef. Même si le vote passe, on aura encore besoin de toi."
        julian hesitation "Ouais."
        julian hesitation "Tu ne peux pas vraiment me promettre ça. C'est gentil d'essayer."
        think "Il regrette sa question à l'instant où elle lui échappe. Je fais comme si je n'avais pas remarqué."
    elif j50_julian_fissure >= 1:
        julian decu "Je reviendrai. Mais si Ryn commence à faire une fête pour mon retour, je repars."
        noam sourire "Il est tellement occupé à se disputer avec Sael qu'il ne remarquera peut-être même pas ta présence."
        julian taquin "Merci. J'apprécie que tu considères mon invisibilité comme une bonne nouvelle."
    else:
        julian colere "Bon, je crois qu'on est sur le point de repartir pour un deuxième débat. Je préférerais éviter ça dans ma chambre."
        noam neutre "D'accord. Je voulais juste m'assurer que tu allais bien."
        julian decu "Maintenant tu sais que je suis encore capable de me disputer. C'est rassurant, non ?"

    "Julian repose le brouilleur et m'accompagne à la porte. Il évite soigneusement de croiser le regard de la caméra."
    julian neutre "Au fait... pas un mot sur ma petite démonstration devant la caméra."
    julian decu "J'ai déjà assez de gens qui me prennent pour un imbécile."
    noam sourire "Alors essaie de leur parler sans répéter ton discours de campagne."
    julian taquin "Tu es un public affreux. À plus, Noam."
    think "Je repars. Julian ne va pas mieux, pas vraiment."
    think "Mais au moins, pendant quelques minutes, il a cessé de parler comme si une caméra devait juger chacune de ses phrases."

    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:
    call KD_ROUTE_J5_NYRA from _call_optional_kd_route_j5_nyra
    # Navigation libre vers l'objectif avant la scène scénarisée.
    call START_EXPLORATION_LIBRE("_5_0_1_OBSERVATION_ARRIVEE", title="Rejoindre la salle d'observation", destination_room="observation") from _call_exploration__5_0_1_OBSERVATION

label _5_0_1_OBSERVATION_ARRIVEE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_237
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ doplleganger = 1
    think "Je voudrais voir ce qui se passe réellement aux frontières. Des rapports, des chiffres... quelque chose qui ne soit pas la colère de Ryn ou la peur de Sael."
    think "C'est presque reposant d'imaginer que des colonnes de nombres peuvent me donner une réponse."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_238
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "neutre", 0.75), ("noam", "neutre", 0.25)])
    "Elias est absorbé par une console. Une tasse de café pleine trône à côté du clavier."
    think "Je n'aime pas la proximité entre ces deux objets. Mais je ne suis pas ingénieur."
    elias sourire "Noam ! Pile quand j'allais fermer les relevés ! Tu as le sens du timing, toi !"
    noam surpris "Mais tu ne m'as même pas regardé !"
    elias rire "J'ai reconnu tes pas. Tu traînes le pied gauche d'un rien. Je commence à reconnaître tout le monde au bruit !"
    noam sourire "Excellent. Maintenant je vais m'écouter marcher jusqu'à la fin de ma vie."
    elias sourire "Je fais ça avec tout le monde ! Enfin, sans le vouloir."
    elias gene "Ça sonne moins inquiétant dans ma tête."
    noam reflechit "Je cherche des informations sur Limen. Après ce que Sael nous a raconté, je me demande à quoi ressemble la vie près des frontières."
    elias reflechit "Ah, ça tombe bien ! Je regardais les sanctions de ces derniers jours. Il y en a... beaucoup."
    elias inquiet "Enfin, ça ne tombe pas bien pour eux, évidemment."
    "Des lignes défilent : vols, bagarres, tentatives de passage entre districts. Certains noms apparaissent plusieurs fois."
    think "Je ne connais aucun de ces gens. Pourtant, ils commencent à me sembler moins abstraits qu'hier."
    noam inquiet "Attends... tout ça, c'est pour une seule semaine ?"
    elias inquiet "Ouais. Et ça, c'est seulement ce que Kami a enregistré. Ce qui n'apparaît pas ici... on n'en sait rien."
    noam triste "Certains vols concernent de la nourriture. Les gens ont faim, ils tentent quelque chose, et ils se font sanctionner."
    elias reflechit "Pas tous, mais regarde les centres de distribution. Il y a une quantité folle de vols autour des stocks."
    noam inquiet "J'aimerais parler à l'un d'entre eux. Savoir ce qu'il s'est passé avant que son nom devienne une ligne sur cet écran."
    elias sourire "Une caméra, je pourrais peut-être trouver ça, mais je suis surtout là pour les pannes."
    elias taquin "Les gens, eux, c'est moins simple à réparer."
    "Elias se penche pour me montrer une nouvelle ligne."
    think "Son coude part vers l'arrière. Vers la tasse."
    think "Je vois la catastrophe une demi-seconde avant lui."
    elias peur "NON ! NON, PAS LE CAFÉ !"
    play sound sfx_drop
    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")
    "Le café éclabousse les touches puis s'infiltre dans une trappe de maintenance entrouverte."
    think "J'ai le réflexe idiot de croire qu'un clavier peut boire quelque chose sans conséquence."
    "Je me jette sur la tasse. Quelques centimètres séparent encore le désastre de la catastrophe complète."

    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress
    if j50_coffee_trace_score >= 0.82:
        "J'attrape la tasse ! Je me sens presque héroïque."
        think "Puis je vois le liquide disparaître sous le panneau. Ma carrière de héros vient de durer une seconde."
        elias inquiet "Merci ! Enfin... non ! Le café ! Il passe SOUS le panneau !"
    elif j50_coffee_trace_score >= 0.35:
        "Je ralentis la chute de la tasse, mais elle heurte le bord de la console."
        "Le café éclabousse la trappe. Le gobelet est presque intact ; ce qui m'inquiète, c'est tout ce qui se trouve dessous."
        elias peur "Merde ! Pourquoi je pose toujours mon café à l'endroit le plus stupide possible ?!"
    else:
        "Mes doigts n'attrapent que de l'air. La tasse tombe."
        "Le café se répand directement sur les connecteurs exposés. Je crois que je viens d'assister à une tentative de meurtre par petit-déjeuner."
        elias panique "NON NON NON ! Pas les connecteurs ! Tout sauf les connecteurs !"

    "Un grésillement retentit. Elias se jette vers l'arrêt d'urgence."
    "Le voyant de sécurité s'allume avant qu'il ait pu appuyer. Un bruit sec me fait sursauter."
    noam peur "ELIAS ! ÇA FUME ! JE FAIS QUOI ?!"
    elias inquiet "NE TOUCHE À RIEN ! Le café a court-circuité la commande ! Recule !"
    "La ventilation se met à rugir."
    "CLAC."
    "Le verrou de la porte se referme. Sur l'écran : « PANNE DU CONTRÔLE D'ACCÈS — SALLE ISOLÉE »."
    $ unlock_codex_page("securite_orbitale", with_notification=False)
    noam inquiet "POURQUOI ELLE SE FERME ?! On n'est pas censés pouvoir sortir quand ça prend feu ?!"
    elias panique "SI ! Mais le système a dû détecter un défaut de pression ! Il croit qu'il faut isoler la salle !"
    elias panique "Ce truc est prévu pour une fuite d'air, pas pour un CAPPUCCINO ASSASSIN !"
    noam peur "Et si ça prend vraiment feu, on fait quoi ? On attend que le café termine son travail ?!"
    elias inquiet "Le disjoncteur a coupé ce panneau, donc la chauffe devrait s'arrêter !"
    elias inquiet "Mais tant qu'on n'a pas relancé le secours, la porte ne répondra pas."
    elias reflechit "Il y a un boîtier de secours sous la console. Les câbles sont codés par couleur !"
    elias inquiet "Noam, j'ai besoin de toi. Maintenant."
    noam inquiet "Moi ?! Elias, j'ai déjà du mal à choisir un câble de chargeur !"
    elias inquiet "Même couleur avec même couleur ! Un fil après l'autre !"
    elias inquiet "Je m'occupe de couper les circuits endommagés. Toi, tu rétablis les liaisons. Pas au hasard, d'accord ?!"
    "Elias soulève le capot. Huit raccordements nous attendent."
    "Un bip aigu retentit. L'écran indique que la batterie de contrôle approche de sa limite."
    think "Tout ce que je sais, c'est que je n'aime pas ce décompte."

    call screen j50_wire_minigame(failure_has_consequences=True)
    $ j50_wire_completed = bool(_return)
    if j50_wire_completed:
        $ j50_kamyz_bonus = 40
    elif j50_wire_success >= 5:
        $ j50_kamyz_bonus = 10
    else:
        $ j50_kamyz_bonus = 0
    if j50_kamyz_bonus > 0:
        $ player_kamyz += j50_kamyz_bonus
        "Kamyz bonus obtenus : [j50_kamyz_bonus]"

    if j50_wire_completed:
        $ j50_observation_circuit_status = "secours_partiel"
        elias rire "OUI ! ÇA MARCHE ! Tu vois ? Je te l'avais dit !"
        "Les voyants passent au vert. Un message apparaît : « ALIMENTATION SECONDAIRE RÉTABLIE — ACCÈS TOUJOURS VERROUILLÉ »."
        noam surpris "Ça marche ? Elias, la porte n'a pas bougé !"
        elias sourire "Parce qu'il reste une étape ! Si je relance le contrôle local, on pourra l'ouvrir sans déranger personne."
        "Je soulève ma tablette."
        noam inquiet "Ou alors on écrit à Kael. Il est ingénieur, lui."
        elias inquiet "Non ! Attends, s'il te plaît ! Je sais d'où vient la panne, je peux la réparer."
        noam reflechit "Et si tu te trompes ?"
        elias gene "Alors... là, tu pourras lui écrire. Mais laisse-moi juste essayer."
        "Il a les mains qui tremblent encore. Pourtant, il a déjà retiré le panneau de protection."
        noam neutre "D'accord. Je garde la tablette allumée."
        elias sourire "Marché conclu ! Et si ça marche, tu racontes à Kael que j'ai tout réparé."
        noam sourire "Je lui raconterai surtout que tu m'as interdit de l'appeler."
        elias gene "Pas interdit ! Conseillé avec beaucoup de conviction !"
        call show_custom_title("Un long moment plus tard") from _call_show_custom_title_j50_wait
        scene bg_observation at adaptive_fullscreen with dissolve
        "La lumière de la console s'est éteinte deux fois. Elias a changé de tournevis, de position, puis de théorie."
        "La porte, elle, n'a pas changé d'avis."
        noam neutre "Ça fait combien de temps que tu dis « encore une minute » ?"
        elias fatigue "Ça dépend. On compte les minutes où je réfléchis ?"
        noam neutre "Celles où tu parles aussi."
        elias gene "Alors beaucoup trop."
        "Il tente une dernière fois de relancer le boîtier. Un voyant clignote, puis s'éteint."
        elias fatigue "Bon."
        noam inquiet "Bon... ?"
        elias fatigue "Tu peux écrire à Kael."
        noam surpris "Pardon ? J'ai mal entendu ?"
        elias gene "Je t'autorise officiellement à demander de l'aide. Avec toute la dignité qui me reste."
        noam sourire "Tu veux que je note ça dans le procès-verbal ?"
        elias inquiet "Non ! Et ne lui dis pas que j'ai attendu aussi longtemps... Enfin, si. Il faut lui expliquer ce qui s'est passé."
        elias fatigue "Je croyais vraiment pouvoir nous sortir de là."
        noam calme "Tu as empêché le boîtier de lâcher complètement. Mais on a besoin d'un coup de main."
        call _5_0_MESSAGE_KAEL from _call_j50_message_kael_success
    else:
        $ j50_observation_circuit_status = "panne_totale"
        elias panique "Merde ! Le boîtier est mort ! Même le voyant de secours ne répond plus !"
        "La ventilation principale continue de fonctionner, mais la porte reste bloquée."
        noam inquiet "On arrête. Je vais écrire à Kael."
        elias inquiet "Attends, je peux encore tester le..."
        "Il s'arrête devant les connecteurs noircis."
        elias fatigue "Non. Tu as raison. Si je touche encore à ça, je risque d'empirer les choses."
        noam neutre "Et pour une fois, je préférerais qu'on soit deux à reconnaître une mauvaise idée."
        elias gene "J'en ai déjà eu une très bonne avec le café, ça suffit."
        call _5_0_MESSAGE_KAEL from _call_j50_message_kael_failure

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")
    "Nous nous éloignons du panneau. Les voyants ont cessé de clignoter ; ça ne rend pas le silence plus rassurant."
    noam inquiet "Dis, Elias... tu n'as pas peur que Kael te passe un savon ?"
    elias fatigue "Si. Énormément. Je l'entends déjà me dire de ne jamais boire au-dessus d'un circuit."
    noam sourire "Je peux prétendre que je t'ai bousculé."
    elias inquiet "Surtout pas !"
    noam surpris "Oh. C'était une plaisanterie."
    elias gene "Ah. Oui. Désolé."
    elias neutre "Mais même pour rire, ne fais pas ça. Si Kael croit que la panne a commencé autrement, il pourrait chercher au mauvais endroit."
    "Il frotte machinalement une petite tache de café sur sa manche. Elle ne part pas."
    elias fatigue "J'aime bien réparer les choses. Quand j'y arrive, je peux au moins me dire que j'ai servi à quelque chose."
    noam inquiet "Tu viens de t'enfermer dans une pièce en voulant réparer quelque chose."
    elias sourire "Voilà. C'est pour ça que je préfère généralement les objets aux gens."
    "Je ris. Il essaie de faire pareil, sans vraiment y parvenir."
    elias neutre "Je sais que tout le monde me prend pour le type qui renverse son verre. Parfois, je me demande s'ils me laisseraient toucher à une console s'ils n'avaient pas besoin de moi."
    noam neutre "Tu as vu le défaut et tu as essayé de l'isoler. Moi, je n'aurais même pas su par où commencer."
    elias gene "Tu dis ça pour me remonter le moral ?"
    noam sourire "Oui. Mais c'est vrai aussi."
    "Elias baisse les yeux. Puis il tend son gobelet vide vers la poubelle, le regarde une seconde, et le pose très loin de la console."
    elias reflechit "Tu as parlé à Sael, finalement ?"
    noam inquiet "Oui. Elle ne changera pas d'avis."
    elias triste "Je m'en doutais. C'est compliqué de lui demander de prendre un risque depuis une salle où il suffit d'un café pour qu'on panique."
    noam reflexion "Tu te moques de nous ou de la station ?"
    elias sourire "Je sais pas. Un peu des deux."
    play sound "audio/sfx_door.mp3"
    "Un bruit de métal résonne derrière la porte. Puis deux coups brefs."
    kael "Elias ? Noam ? Éloignez-vous du panneau !"
    elias sourire "KAEL ! On est là !"
    nyra "On le sait. Votre message mentionnait précisément la salle d'observation."
    "Un autre cliquetis. Le verrou résiste, puis cède enfin."
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.23), ("nyra", "reflechit", 0.48), ("elias", "gene", 0.74), ("noam", "reflexion", 0.91)])
    kael reflechit "Personne ne touche plus à rien. J'ai isolé le contrôleur depuis le couloir, Nyra a coupé l'autorisation de verrouillage."
    nyra reflechit "La sécurité pensait protéger la salle. C'était une décision parfaitement logique, fondée sur une information complètement fausse."
    noam sourire "C'est rassurant de savoir que même une porte peut se tromper avec autant d'assurance."
    kael inquiet "Vous n'êtes pas blessés ? Vous avez respiré de la fumée ?"
    elias gene "Non. La ventilation a tenu. Enfin... à ce que j'ai vu."
    nyra reflechit "Et pourquoi le signal d'alerte automatique ne nous est-il pas parvenu ?"
    if j50_wire_completed:
        kael reflechit "Le secours était rétabli, mais la liaison de contrôle est restée isolée. J'ai dû contourner le verrou depuis l'extérieur."
        nyra neutre "Nous aurions pu être ici plus tôt."
        elias fatigue "Oui. J'ai voulu finir sans déranger Kael. C'était idiot."
        kael calme "Idiot, non. Dangereux de garder l'information pour toi, oui."
    else:
        kael reflechit "Le contrôleur a perdu son alimentation. Heureusement, le message de Noam est passé par la tablette."
        elias fatigue "J'ai cru que je pouvais encore raccorder un fil. Noam m'a arrêté."
        nyra raison "Pour une fois, la décision la plus utile n'était pas de réparer, mais d'arrêter."
    noam inquiet "Vous pourrez remettre les relevés en marche ?"
    kael reflechit "La console locale, oui. Mais le verrou d'accès et les relevés ne répondent pas au même circuit. Je veux comprendre pourquoi l'un a entraîné l'autre."
    nyra reflechit "Je vais consigner l'incident. Ne touchez pas aux données de la salle avant qu'on ait identifié ce qui a été interrompu."
    elias inquiet "Vous pensez que le café a touché autre chose ?"
    kael reflechit "Je ne vais pas inventer une panne plus grande pour te faire peur. Je vais vérifier."
    "Nyra sort la première. Kael reste un instant devant le panneau, puis se retourne vers Elias."
    kael calme "La prochaine fois, tu m'appelles avant de démonter la moitié de la station."
    elias sourire "Promis !"
    elias gene "Je vais peut-être commencer par changer de tasse."
    kael calme "Commence par changer de table."
    think "Je suis entré ici pour chercher des informations sur la Terre. J'en repars avec une question beaucoup plus proche : pourquoi une simple panne a-t-elle suffi à nous couper du reste du Conclave ?"

    jump _5_0_FIN_JOURNEE


label _5_0_MESSAGE_KAEL:
    $ j50_kael_alert_sent = True
    "J'ouvre la messagerie de ma tablette. Même derrière une porte verrouillée, le réseau personnel semble répondre."
    if j50_wire_completed:
        call messenger_play("j5_observation_secours", "kael", [("noam", "Kael ? On est bloqués avec Elias dans la salle d'observation. Le secours fonctionne, mais la porte reste verrouillée."), ("kael", "Vous êtes blessés ? Le panneau chauffe encore ?"), ("noam", "Non. Ventilation active. Elias a tenté le contrôle local, sans résultat."), ("kael", "Ne touchez plus au boîtier. J'arrive avec Nyra pour isoler l'accès depuis le couloir.")], objective_text="Envoyer un appel à l'aide à Kael", notify=False) from _call_messenger_j50_secours
    else:
        call messenger_play("j5_observation_panne", "kael", [("noam", "KAEL ! On est enfermés avec Elias dans la salle d'observation. Court-circuit, boîtier de secours hors service."), ("kael", "Respirez calmement. Vous voyez de la fumée ? La ventilation fonctionne ?"), ("noam", "Plus de fumée. Ventilation active, mais la porte ne répond plus."), ("kael", "Ne touchez plus au panneau. Nyra et moi arrivons. Restez loin des connecteurs.")], objective_text="Demander immédiatement l'aide de Kael", notify=False) from _call_messenger_j50_panne
    "Je relève les yeux de la tablette. Elias attend ma réaction comme si c'était moi qui devais lui annoncer sa note."
    noam neutre "Ils arrivent. Kael et Nyra."
    elias fatigue "Super. On va être sauvés par deux personnes qui vont me regarder comme si j'avais essayé de faire du café dans le réacteur."
    return


label _5_0_FIN_JOURNEE:

    $ current_period = "Soir"
    if doplleganger == 0:
        call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_240
        scene bg_dortoir at adaptive_fullscreen with dissolve
    else:
        call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_240_observation
        scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    if doplleganger == 0:
        think "Je laisse Julian seul avec ses caméras. Au moins, aujourd'hui, il a accepté de me parler sans public."
        think "Je ne sais pas si c'est un progrès. Je préfère le croire."
    else:
        think "Elias avait tellement peur de déranger Kael qu'il a préféré rester enfermé. Puis il a fini par demander de l'aide."
        think "Kael et Nyra ont ouvert la porte. Ils n'ont pas promis que les contrôles fonctionnaient à nouveau."
        think "Un verrou qui nous protège en nous enfermant : je commence à comprendre pourquoi le mot sécurité ne rassure pas tout le monde."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_241
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je pose la tablette sur le bureau et m'écroule sur le lit."
    think "J'avais prévu une journée tranquille. Au moins, personne n'a essayé de me faire voter pendant le dîner."
    think "Demain, Sael votera non. Je comprends ce qui la pousse à le faire."
    think "Et quand je repense aux corps dont parle Ryn, je comprends aussi pourquoi il ne peut pas accepter ce non."
    think "Deux raisons de vouloir sauver des gens. Deux votes qui ne peuvent pas se rejoindre."
    think "Kami doit se régaler."
    "Je me glisse sous la couverture."
    "Au moment où mes yeux se ferment, un verrou grince dans le dortoir."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    think "Des pas. Lents, réguliers."
    think "Ils ralentissent juste devant ma porte."
    think "À cette heure-ci, je préférerais vraiment que ce soit quelqu'un qui cherche les toilettes."

    menu:
        "Ouvrir la porte.":
            jump _5_0_NUIT_OUVRIR
        "Écouter sans bouger.":
            jump _5_0_NUIT_ECOUTER
        "Ignorer les pas et rester allongé.":
            jump _5_0_NUIT_RESTER

label _5_0_NUIT_RETOUR:

    $ blink()
    think "Les pas s'éloignent enfin. Je reste encore une minute à écouter."
    think "Je ne sais pas pourquoi ce simple bruit me tient autant éveillé."
    think "Demain, il faudra voter."
    think "Cette nuit, je n'ai même pas réussi à identifier qui traversait le couloir. Je me demande ce que je crois vraiment connaître des onze autres."
    "Le silence revient. Je finis par m'endormir."

    $ current_day = 6
    pause 1.0

    if doplleganger == 0:
        call end_day("6", sleeping=True) from _call_end_day_6
        jump _6_0_0_REVEIL_CHAMBRE

    else:
        call end_day("6", sleeping=True) from _call_end_day_7
        jump _6_0_1_REVEIL_CHAMBRE


label _5_0_SAEL_PNC:

    $ _j50_sael_choice = renpy.call_screen("j50_sael_room_pnc")

    if _j50_sael_choice == "lit":
        $ j50_sael_mark_seen("lit")
        think "Le lit a été réduit à l'essentiel : un matelas et une couverture. Les planches sont rangées contre le mur."
        think "Je commence à soupçonner Sael d'avoir déclaré la guerre au mobilier."
        noam surpris "Tu as vraiment démonté un lit entier toute seule ? Tu as une rancune particulière envers les meubles ?"
        sael neutre "Chez moi, on dort souvent plus près du sol. C'est comme ça que je suis à l'aise."
        sael sourire "Quant à la rancune, je te rassure : je n'en veux pas au matelas."
        noam sourire "Moi, si je démonte mon lit, c'est parce que je suis tombé dessus un peu trop fort."
        sael sourire "Ne t'inquiète pas, je ne viens pas inspecter le tien. Tu peux dormir dans ton nuage."
    elif _j50_sael_choice == "crane":
        $ j50_sael_mark_seen("crane")
        think "Un petit crâne d'animal repose parmi des morceaux de bois et des ficelles."
        think "Il a été nettoyé et décoré soigneusement. Je crois que mon visage vient de montrer une surprise un peu trop visible."
        noam inquiet "Euh... je vais poser une question stupide. C'est un vrai crâne ?"
        sael neutre "Oui. Un animal chassé chez nous."
        sael neutre "On prend une vie pour se nourrir. Alors on essaie de ne rien gaspiller de ce qu'elle nous donne."
        noam neutre "D'accord. À Harmonie, ce n'est pas exactement le genre de décoration qu'on trouve sur les étagères."
        sael mefiant "Regarde si tu veux, mais ne le prends pas. Il a plus de valeur pour moi qu'il n'en a l'air."
    elif _j50_sael_choice == "affaires":
        $ j50_sael_mark_seen("affaires")
        think "Ses affaires tiennent dans quelques sacs de toile. Elle a conservé des outils, des morceaux de tissu, des objets réparés."
        think "Je crois que je n'aurais jamais pensé à emporter la moitié de tout ça."
        noam reflexion "Tu as vraiment apporté tous ces outils depuis ton village ?"
        sael neutre "Presque. Je ne savais pas ce qu'on pourrait garder, alors j'ai préféré prendre ce qui peut servir."
        sael taquin "J'aurais sans doute dû emporter des vis aussi. Kael serait venu plus tôt."
        noam sourire "J'ai emporté des objets parfaitement inutiles. Ma valise aurait honte si elle pouvait te voir."
        sael reflechit "Un objet inutile aujourd'hui peut te sauver demain. Tout dépend de ce qu'on fait avec."
    else:
        return

    if j50_sael_pnc_score >= 3:
        sael sourire "Bon. Tu as étudié ma chambre comme un inspecteur."
        sael neutre "On peut parler de la vraie raison de ta visite, maintenant ?"
        return
    jump _5_0_SAEL_PNC

label _5_0_NUIT_OUVRIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_242
    scene bg_dortoir at adaptive_fullscreen with dissolve
    "J'entrouvre la porte. Une silhouette s'éloigne déjà au bout du dortoir."
    think "Évidemment. Le temps que je trouve le courage de regarder, le mystérieux visiteur s'en va."
    if doplleganger == 0:
        think "Cette démarche... Julian ?"
        think "Il tourne au coin avant que je puisse distinguer son visage."
        noam neutre "Julian ? C'est toi ?"
    else:
        think "La silhouette porte quelque chose sous le bras. Elias ?"
        think "Après l'accident de cet après-midi, il pourrait encore chercher une solution à la panne."
        noam neutre "Hé ! Qui est là ?"
    "Aucune réponse."
    think "Je reste seul dans le couloir, avec cette sensation ridicule d'avoir dérangé quelqu'un qui n'existe peut-être même pas."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_ECOUTER:

    think "Je retiens mon souffle. Les pas s'arrêtent."
    think "Une voix murmure quelque chose, juste assez fort pour que j'en distingue quelques mots."
    if doplleganger == 0:
        julian decu "Non... c'est pas comme ça qu'il faut le dire..."
        pause 0.3
        julian neutre "Demain. Si je vois Tomas, je pourrai..."
        julian hesitation "Non. Recommence. Dis juste que tu es désolé."
        think "Julian. Il répète des excuses dans un couloir vide."
        think "Je n'aurais jamais cru qu'il aurait besoin de s'entraîner pour prononcer ces mots."
    else:
        elias fatigue "Kael ? Ouais, c'est Elias. Je sais que tu viens à peine de rentrer..."
        pause 0.3
        elias inquiet "Non, j'ai compris pour le contrôleur. C'est pas ça. Tu as vérifié les relevés qui étaient affichés avant la coupure ?"
        elias reflechit "D'accord. Je t'attends demain. Je toucherai plus à rien."
        think "Les relevés ? Je pensais que son inquiétude s'arrêtait à la porte."
        think "Je pourrais sortir lui demander ce qu'il a remarqué. Mais Elias a déjà repris sa marche, et la chambre est redevenue silencieuse."
    "Les pas reprennent. La voix disparaît au bout du couloir."
    think "Je n'ai pas bougé. J'ai pourtant l'impression d'avoir assisté à une conversation à laquelle je n'étais pas invité."
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_RESTER:

    think "Je reste au lit."
    think "Après une journée passée à demander aux autres de m'expliquer leurs choix, je pourrais peut-être leur laisser une nuit de tranquillité."
    "Je remonte la couverture. Les pas finissent par s'éloigner."
    think "Pour une fois, je décide de ne pas mener l'enquête."
    jump _5_0_NUIT_RETOUR

# total : 8m
# Total jour 0-5 : 1h41
