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
default j50_wire_time_left = 4.0
default j50_wire_lives = 3
default j50_wire_failed = False
default j50_wire_completed = False
default j50_wire_failure_has_consequences = False
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
        ("vert", "#47b86b"),
        ("jaune", "#e6c84e"),
        ("violet", "#9b63d9"),
        ("orange", "#df8a34"),
    ]

    J50_WIRE_RIGHT_ORDER = ["bleu", "rouge", "jaune", "vert", "orange", "violet", "rouge", "vert", "bleu", "orange", "violet", "jaune"]

    J50_WIRE_LEFT_YS = [151 + (idx * 62) for idx in range(12)]
    J50_WIRE_RIGHT_YS = [151 + (idx * 62) for idx in range(12)]
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
        store.j50_wire_time_left = 4.0
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
            store.j50_wire_time_left = 4.0
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
            store.j50_wire_time_left = 5.0
            renpy.sound.play("audio/sfx_qte_miss.wav")

            if store.j50_wire_lives <= 0:
                store.j50_wire_failed = True
                store.j50_wire_feedback = "ÉCHEC — alimentation de secours interrompue."
            else:
                store.j50_wire_feedback = "TEMPS ÉCOULÉ — reprise d'urgence : 5,0 s."

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

    text "Reliez chaque câble au connecteur de même couleur avant la fin du délai.":
        xpos 690
        ypos 25
        xsize 1180
        text_align 1.0
        size 23
        color "#bdc9d5"
        font "fonts/Barlow-Light.ttf"

    # Câbles déjà verrouillés : ombre, halo puis cœur lumineux.
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

    # Colonne de gauche : temps, progression et vies.
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
                bar value AnimatedValue(j50_wire_time_left, 5.0, delay=0.1):
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
            text "3 vies — expiration uniquement" size 19 color "#9fb0bf"
            text "Une bonne liaison remet le délai à 4,0 s." size 18 color "#73899c" xsize 310

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

    $ blink()
    think "Je regarde l'heure. Il est déjà huit heures, et je me demande si Sael est réveillée. Depuis la dispute d'hier, je n'arrête pas de repenser à ce qu'elle nous a raconté."
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Elle a clairement dit qu'elle voterait contre demain. J'aimerais la revoir, pas pour la coincer avec des arguments, mais parce que je crois qu'on a compris seulement une partie de son histoire."
    think "Je repense aussi à Julian. Il n'est même pas venu à la réunion hier. Ça ne lui ressemble vraiment pas."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Bonjour à tous ! Vous avez une mine épouvantable ce matin. Et moi qui croyais qu'une bonne nuit suffirait à vous remettre du vote !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Les rations du jour vous attendent à la cafétéria. Vous aurez de nouvelles provisions au jour 7, alors inutile de venir pleurer auprès de Goumi."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et n'oubliez pas, vous revoterez demain. J'espère que vous avez prévu de vous parler entre-temps, c'était assez amusant hier !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Je prends le morceau de pain laissé sur mon bureau la veille et mange quelques bouchées en m'habillant. Je n'ai pas vraiment faim."
    think "Je pourrais aller retrouver les autres à la cafétéria, mais j'aimerais parler à Sael avant qu'elle ne commence sa journée. Je ne sais pas si elle acceptera de me recevoir."
    "Je prends ma tablette et je sors."

    stop music fadeout 1.2

    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_231
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.0

    think "Je retrouve la porte de Sael grâce au tissu noir noué sur la poignée. Je frappe, puis j'attends un moment avant d'entendre des pas."
    play sound sfx_knock
    pause 0.5
    play sound sfx_door
    $ showGroup([("sael", "mefiant", 0.65), ("noam", "reflexion", 0.30)])
    sael mefiant "Noam. Je suppose que tu viens pour le vote ?"
    noam inquiet "Un peu, oui. Mais si tu veux pas en parler, je peux repartir."
    sael neutre "Tu es déjà là. Entre, au moins on pourra discuter sans que tout le dortoir nous entende."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_sael") from _call_MAYBE_PLAY_SCRIPTED_DOOR_232
    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    think "La chambre n'a presque plus rien de celle qu'on nous a donnée à notre arrivée. Sael a démonté le lit et posé le matelas près du sol. Elle a aussi accroché plusieurs objets en bois et en os aux murs."
    sael reflechit "Tu peux regarder, ça ne me dérange pas. Mais ne touche pas à ce qui est accroché au mur, s'il te plaît."

    $ j50_sael_pnc_score = 0
    $ j50_sael_pnc_seen = []
    call _5_0_SAEL_PNC from _call_5_0_SAEL_PNC
    $ showGroup([("noam", "hesitation", 0.25), ("sael", "neutre", 0.75)])

    noam reflexion "T'as vraiment tout changé dans ta chambre. Je pensais pas qu'on pouvait démonter les meubles comme ça."
    sael neutre "Le lit était trop haut et trop mou, alors je l'ai défait. Les planches peuvent servir à autre chose, au moins."
    noam sourire "Je me disais que Kael aurait déjà essayé de récupérer les vis."
    sael sourire "Il est passé hier pour me demander exactement ça. J'ai refusé."
    "Elle me montre un tabouret. Je m'assieds pendant qu'elle termine de ranger quelques affaires."
    noam inquiet "Je voulais surtout te demander un truc. Hier, quand tu as parlé des attaques contre ton village, j'ai eu l'impression que tu nous racontais pas tout."
    sael triste "Parce que je n'allais pas raconter toute ma vie devant Ryn qui me criait dessus. Et puis je ne vous connais pas assez pour ça."
    noam neutre "Je comprends. Mais tu vois bien pourquoi lui, il veut ouvrir les frontières. Il a vu des gens mourir juste parce qu'ils essayaient de passer."
    sael determine "Je le comprends très bien. Chez nous aussi, il y a eu des morts, Noam. Et pas seulement des gens qui se battaient. C'est justement pour ça que je suis contre."
    noam inquiet "C'étaient les groupes armés dont tu parlais ?"
    sael triste "Oui. Ils venaient nous prendre de la nourriture et du matériel. Il y a eu des périodes où on se demandait simplement qui serait le prochain à se faire attaquer."
    sael neutre "Depuis que les frontières sont fermées, on peut au moins cultiver nos terres et vivre sans les voir revenir. Je sais que les règles de Kami sont horribles pour ceux qui essaient de sortir de Limen, mais chez nous elles ont arrêté quelque chose."
    noam reflechit "Je pensais pas que c'était aussi différent selon les endroits. Chez moi, on voit surtout les familles qui n'ont plus le droit de se rejoindre."
    $ unlock_dossier_arg("p2_familles")
    sael mefiant "Et tu voudrais que j'accepte de rouvrir les passages parce que certaines familles sont séparées ?"
    noam inquiet "Non, je dis juste que c'est aussi un problème. Je sais pas comment régler les deux, justement."
    sael reflechit "Ryn ne sait pas non plus, mais il parle comme si tous ceux qui veulent les garder étaient des monstres. Ça m'a vraiment mise en colère."
    noam calme "Je crois qu'il s'énerve parce qu'il a l'impression que personne ne l'écoute. Mais oui, hier il t'a coupé la parole plusieurs fois."
    sael neutre "Je lui reparlerai quand il sera capable de me laisser finir une phrase. En revanche, pour le vote, ma décision est prise."
    noam inquiet "Tu comptes vraiment voter contre, même si on propose une surveillance des passages ?"
    sael determine "Le texte de demain dit qu'on ouvre les frontières. Il ne prévoit aucune surveillance et ne nous laisse aucune garantie. Je voterai non, et je ne changerai pas d'avis."
    noam triste "D'accord. Au moins, je comprends mieux pourquoi."
    sael reflechit "Mara est venue hier soir. Elle m'a dit qu'elle avait aussi beaucoup de réserves, mais on n'a pas décidé de voter ensemble. Je préfère te le préciser."
    noam surpris "Je pensais que vous étiez déjà toutes les deux contre."
    sael neutre "Je ne décide pas pour Mara. Demande-lui directement, si tu veux savoir."
    "Sael se lève pour me raccompagner. Avant d'ouvrir la porte, elle s'arrête."
    sael triste "Tu sais, ça me ferait plaisir de pouvoir revoir les gens que je connais ailleurs. Je ne suis pas contre parce que j'aime voir des gens enfermés."
    noam calme "Je sais. Merci d'avoir accepté de m'en parler."
    sael neutre "Et essaie de ne pas te mettre dans la même situation que Julian en allant insister auprès de tout le monde."
    noam sourire "Je vais essayer. Bonne journée, Sael."

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_233
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    think "Sael votera non. Je m'y attendais, mais au moins je sais maintenant qu'elle n'est pas simplement opposée à l'idée de laisser les gens circuler."
    think "Pour Mara, je n'ai encore aucune certitude. De toute façon, si je veux comprendre ce qu'elle pense, il faudra lui parler à elle."

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

    pause 0.8

    think "Ne sachant pas quoi faire, je marche sans réelle direction. Le Conclave parait désert."

    "La salle commune est vide : une chaise renversée, un plateau abandonné."

    think "Je devrais faire quelque chose. Mais faire quoi ? Convaincre qui ? De quoi, exactement ?"

    think "Julian. Il doit encore être dans sa chambre."
    think "Kael a dit qu'il avait tenté d'aller le voir hier soir."
    think "Qu'il lui avait répondu de le laisser tranquille."

    "Je m'arrête."

    think "Sinon, dans la salle d'observation, sur les ordinateurs, on peut voir l'état des districts."
    think "Qu'espèrent les gens par rapport au vote de demain ? Je me le demande bien."

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

    pause 0.5

    $ doplleganger = 0
    think "Bon, Julian m'inquiète à ne plus se montrer du tout, ça ne lui ressemble pas."

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 1.0

    think "Rien."
    "Je frappe encore."

    play sound sfx_knock volume 8.0
    pause 0.8

    think "J'entends un mouvement derrière la porte."

    noam "Julian. C'est moi."

    pause 0.8

    play sound sfx_door volume 8.0

    $ showGroup([("julian", "neutre", 0.65), ("noam", "neutre", 0.30)])

    "La porte s'ouvre."

    think "Julian n'a l'air ni détruit ni même vraiment atteint."

    julian taquin "Noam. Tu viens constater les dégâts ?"

    noam hesitation "Je venais surtout voir comment tu allais."

    julian sourire "Oh. C'est presque touchant."

    "Il se pousse. Cette fois, l'invitation est réelle. Il m'invite à rentrer."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_236
    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    $ showGroup([("julian", "sourire", 0.65), ("noam", "reflexion", 0.30)])

    think "La chambre est trop propre. Une pièce témoin où rien ne dépasse, rien ne vit."

    julian neutre "Alors ? Laisse-moi deviner. Tu veux me dire de ne pas prendre les résultats comme quelque chose de personnel ?"
    julian taquin "Ou m'offrir une de tes phrases calmes, prudentes et miraculeusement sans conclusion ?"

    noam "Disons que je ne suis pas vraiment venu avec un dialogue préétabli."

    julian rire "Oh, comme c'est surprenant."

    noam reflexion "Tu n'as pas l'air aussi abattu qu'hier."

    julian sourire "Parce que je ne le suis pas, du moins pas vraiment."

    "Julian pose la main sur le brouilleur."
    $ unlock_codex_page("surveillance_conclave", with_notification=False)

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    think "Le grésillement disparaît. La caméra pivote. Julian se met en scène."

    julian triste "J'avoue que c'est difficile. Je croyais sincèrement que nous pouvions accomplir quelque chose de grand."
    julian decu "Et, au moment décisif, VOUS avez choisi la peur."

    noam reflexion "Sérieux ?! Arrête de..."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    noam reflexion "...jouer la comédie."


    julian rire "Évidemment que je joue. Quand Kami regarde, il faut lui donner quelque chose qu'elle ne puisse pas utiliser contre nous."
    julian sourire "L'opinion publique est bien plus dangereuse que tu ne le crois !"

    noam desaccord "Donc tout ça, c'était pour l'image. Pour TON image ?!"

    julian taquin "L'image, c'est ce qui reste quand une idée échoue. Et ce qui permet à la suivante d'exister."
    julian sourire "Et le plus beau c'est que, tu sais. Noam, il faut aussi se servir de ses échecs."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    julian triste "Il faut accepter la défaite avec dignité. Mais j'ai porté ce vote jusqu'au bout."
    julian decu "Alors c'est normal que je sois déçu !"

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    noam reflexion "Et toi, dans tout ça ? Où s'arrête le masque que tu portes ?"

    julian neutre "Moi ? je fais ce qu'il faut pour rester utile à la société."

    $ j50_julian_fissure = 0

    menu:
        "Tu veux aider les gens.":
            $ j50_julian_fissure -= 1
            noam "Tu veux aider les gens."
            julian sourire "C'est gentil de le remarquer."

        "Tu veux qu'on te regarde aider les gens.":
            $ j50_julian_fissure += 1
            noam "Tu veux qu'on te regarde aider les gens."
            julian inquiet "..."

        "Tu t'en fiches complètement.":
            noam "Tu t'en fiches complètement."
            julian taquin "Evidemment, tout est de la faute de ce connard de Julian."

    julian sourire "Que le vote passe ou qu'il tombe, ce vote laisse quelque chose, une marque indélébile, sur la société."
    julian idee "S'il passe, j'ai porté une idée décisive. S'il tombe, j'ai combattu votre peur du changement."
    julian rire "Dans les deux cas, l'histoire sait où me placer."

    menu:
        "Tu veux être indispensable.":
            $ j50_julian_fissure += 1
            noam determine "Tu veux être indispensable."
            julian inquiet "Ce n'est pas un défaut."

        "Tu veux prouver que les autres sont lâches.":
            $ j50_julian_fissure -= 1
            noam "Tu veux prouver que les autres sont lâches."
            julian sourire "Je n'ai pas besoin de le prouver. Ils le font très bien tout seuls."

        "Tu veux juste gagner.":
            noam "Tu veux juste gagner."
            julian neutre "Gagner quoi ? Tu vois, même toi tu ne sais pas."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3

    julian triste "Mais ce n'est pas fini, on a encore 9 votes à traverser. Je crois encore qu'ils peuvent dire quelque chose de nous."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.3

    menu:
        "Tu veux qu'on ait besoin de toi pour y croire.":
            $ j50_julian_fissure += 1
            noam determine "Tu veux qu'on ait besoin de toi pour y croire."

        "Tu es seulement cynique.":
            $ j50_julian_fissure -= 1
            noam desaccord "Tu es seulement cynique."

        "Tu as peur que le vote passe sans toi.":
            $ j50_julian_fissure += 1
            noam reflexion "Tu as peur que le vote passe sans toi."

    if j50_julian_fissure >= 3:
        noam determine "Tu ne veux pas seulement que le vote passe."
        noam "Tu veux qu'il ait besoin de toi pour passer."

        julian inquiet "..."
        julian "C'est une façon remarquablement injuste de résumer une ambition sincère."

        noam "Non."
        noam "C'est une façon très précise."

        julian peur "Tu crois que c'est drôle ?"
        julian inquiet "Tu crois que je n'ai jamais pensé à ce qui reste quand personne n'a plus besoin de moi ?"

    elif j50_julian_fissure >= 1:
        noam reflexion "Tu veux être celui autour de qui le vote s'organise."
        noam "Pas seulement celui qui vote pour."

        julian reflexion "Peut-être. Ou peut-être que tu es incapable de me comprendre."

    else:
        noam desaccord "Tu joues avec tout le monde."

        julian sourire "Et toi, tu me donnes exactement la scène qu'il me fallait."
        julian taquin "Alors, je dois te le dire..."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3


    julian sourire "Merci d'être venu, Noam."
    julian triste "Même nos désaccords prouvent que tout ça compte encore."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.3

    noam "Pff, t'es incorrigible. Un putain de manipulateur."

    julian sourire "Oh pauvre chou. Pourquoi est-ce que j'arrêterais juste avant la fin ?"
    julian colere "Allez ouste, tu ne me sers plus à rien maintenant."

    "Il me pousse en direction de la sortie. Un sourire sur le visage."

    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:
    call KD_ROUTE_J5_NYRA from _call_optional_kd_route_j5_nyra
    # Navigation libre vers l'objectif avant la scène scénarisée.
    call START_EXPLORATION_LIBRE("_5_0_1_OBSERVATION_ARRIVEE", title="Rejoindre la salle d'observation", destination_room="observation") from _call_exploration__5_0_1_OBSERVATION

label _5_0_1_OBSERVATION_ARRIVEE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_237
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    pause 0.5

    $ doplleganger = 1
    think "J'ai besoin d'avoir des réponses, j'ai besoin de savoir où en est le monde. Ce qu'il attend, ce qu'il espère."

    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_238
    scene bg_observation at adaptive_fullscreen with dissolve

    pause 0.8

    think "Derrière les baies vitrées, un silence vieux de milliards d'années ignore nos votes et notre survie."

    $ showGroup([("elias", "neutre", 0.75), ("noam", "neutre", 0.25)])

    "Elias est assis à la console, une tasse à la main, les yeux sur les données des districts."

    elias neutre "Noam ?"

    think "Il ne s'est même pas retourné."

    elias sourire "Qu'est-ce que tu fais là ?"

    noam surpris "Hein ? Comment tu as su que c'était moi ?!"

    elias sourire "Facile, au bruit de tes pas."
    elias rire "Je t'ai déjà dit, non ? Que j'avais une excellente ouïe."

    noam triste "Ah ouais, c'est vrai. Tout est vraiment plus calme aujourd'hui."

    elias neutre "Ouais. Mais la cafétéria, c'était chaud. Genre vraiment chaud."

    think "Il boit sans quitter l'écran des yeux."

    elias neutre "Regarde ça."

    "Des chiffres, des courbes et des noms défilent sur le panneau droit."

    noam reflexion "Il va falloir m'expliquer. Enfin… ces chiffres ça correspond à quoi ?"

    elias reflechit "Là. Regarde."

    "Il pointe du doigt une liste de noms qui défile."

    elias inquiet "C'est les noms des gens qui ont merdé. Enfin, c'est ce que l'écran dit."
    elias triste "À côté, t'as la règle qu'ils ont brisée."

    think "Vol. Bagarre. Menace. La liste est longue et chaque ligne revient aux rations."
    think "Ils veulent manger. Le système, lui, il compte les infractions."

    pause 0.3

    elias inquiet "Attends, regarde ça—"

    "Son coude accroche la tasse."
    play sound sfx_drop

    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")

    "Le café se répand sur les touches et le panneau latéral."

    elias "Et merde ! Oh, putain, c'est chaud, c'est chaud—"

    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress

    if j50_coffee_trace_score >= 0.82:
        think "Mes doigts frôlent la porcelaine. Assez pour changer l'angle, pas pour la retenir."
    elif j50_coffee_trace_score >= 0.35:
        think "Trop tard. Ma main traverse l'endroit où la tasse n'est déjà plus."
    else:
        think "Trop vite. Mon poignet heurte la console et la tasse part plus loin en se brisant au sol."

    "Elias récupère sa tasse vide. Le café ruisselle entre les touches."
    "Un voyant passe au rouge. La console siffle et de la fumée s'échape de la console."

    noam "C'est moi qui— j'ai tendu le bras, enfin, j'ai dû te—"

    elias inquiet "Non, c'était ma tasse. Mon coude. Ma connerie. T'inquiète, j'ai l'habitude..."

    "Un voyant orange s'allume. Une fumée grise monte de la grille latérale."

    "Un claquement mécanique nous fait nous retourner. La porte s'est verrouillée."
    think "VERROUILLAGE SÉCURITÉ — ANOMALIE DÉTECTÉE. Pour une fois, l'écran résume bien la situation."
    $ unlock_codex_page("securite_orbitale", with_notification=False)

    pause 0.5

    elias panique "Ah. Et merde, me dis pas qu'on est coincé ici !"

    noam peur "La porte est bloquée ?"

    elias inquiet "La salle s'est verrouillée."
    elias colere "Sûrement une sécurité à la con. Quand un truc fume, ça ferme tout pour éviter que le feu ne sorte."

    noam "Heureusement rien n'a pris feu, le matériel a juste dû en prendre un coup. Combien de temps avant que ça devienne vraiment dangereux ?"

    elias panique "Putain, putain, putain…"
    elias inquiet "Noam, viens là. Tu vas relier les fils pendant que j'essaye de réparer ça."
    elias "Même couleur ensemble. Tu réfléchis pas. Tu relies."

    "Elias arrache le panneau. Des grappes de fils pendent sous la console."

    # Passe True ici si cette occurrence du mini-jeu doit sanctionner l'échec.
    call screen j50_wire_minigame(failure_has_consequences=False)
    $ j50_wire_completed = bool(_return)

    if j50_wire_completed:
        $ j50_kamyz_bonus = 40
    elif j50_wire_failure_has_consequences:
        $ j50_kamyz_bonus = 0
    elif j50_wire_success >= 8:
        $ j50_kamyz_bonus = 25
    elif j50_wire_success >= 5:
        $ j50_kamyz_bonus = 15
    else:
        $ j50_kamyz_bonus = 5

    $ player_kamyz += j50_kamyz_bonus
    "Kamyz bonus obtenus : [j50_kamyz_bonus]"

    if j50_wire_failed and j50_wire_failure_has_consequences:
        elias colere "On a perdu l'alimentation de secours. Là, ça va vraiment nous retomber dessus."
    elif j50_wire_failed:
        elias fatigue "C'est mort pour le panneau… mais la sécurité principale tient encore. On peut continuer."

    if j50_wire_errors > 0:
        elias colere "Non, pas celui-là !"
        elias "Putain… Bon. Bah je sais plus quoi faire pour réparer ça..."

    if j50_wire_success >= 8:
        elias rire "Oh super, t'as géré !"
    elif j50_wire_success >= 5:
        elias fatigue "C'est moche. Mais ça tient. C'est le principal."
    else:
        elias inquiet "C'est pété de partout. Mais ça fume moins. Franchement, on prend."

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")

    elias "La ventilation tourne. Au moins on va pas étouffer."
    elias fatigue "Mais ouais… on est bloqués pour un moment. C'est chaud, cette salle est censée observer les problèmes, pas en devenir un."

    "Elias s'assoit par terre, loin du panneau."

    elias neutre "Tu voulais regarder les chiffres de Limen, non ?"

    "Je m'assieds à côté de lui, dos au mur."

    elias inquiet "Tu crois que ça va passer, le vote ?"

    noam "Tu veux savoir si ça peut encore passer. Enfin… je ne vois pas ce qui changerait avant demain."

    pause 0.3

    elias inquiet "Sael votera contre."
    elias triste "C'est sûr. Elle croit vraiment que ça ramènera la guerre."

    noam triste "Elle me l'a dit ce matin. Mara aussi d'ailleurs apparemment."

    elias "… Ah."

    elias fatigue "Alors c'est foutu. C'est chaud."

    noam "Ouais, on ne peut plus rien changer…"
    pause 1.0

    call show_custom_title("Après plusieurs heures") from _call_show_custom_title

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 3.0

    "Les voyants passent à l'orange. Le panneau de la porte clignote."

    play sound "sound/sfx_door.ogg"

    "La porte s'ouvre dans un déclic."

    $ showGroup([("elias", "fatigue", 0.75)])

    elias fatigue "Ah. Libérés. C'était moins long que prévu."

    "Elias se relève en s'étirant."

    elias "Je vais voir si j'ai cramé un truc important. Enfin, je veux dire plus important que la porte."

    think "Quelques touches collent. L'écran latéral est mort."

    elias neutre "Rien de trop grave. Enfin je crois."
    elias reflechit "Mais je comprends pas pourquoi ça a fumé autant..."

    think "Nous nous séparons dans le couloir, avec un vote condamné et une caméra en moins. Bilan mitigé."

    jump _5_0_FIN_JOURNEE


label _5_0_FIN_JOURNEE:

    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_240
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    think "Puis l'après-midi passe. Elle se termine comme elle a commencé : lourde, lente, sans discussion."
    "Puis je retourne dans ma chambre."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_241
    scene bg_chambre at adaptive_fullscreen with dissolve

    think "Je m'assieds au bord du lit, pas encore prêt à m'allonger."
    think "Tout le monde a raison, d'une certaine façon. Et demain, le vote échouera."

    $ blink()
    "Je m'allonge."

    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()

    think "Plus qu'une nuit. Un matin. Puis le vote."

    think "Que peut-on encore faire ? Peut-être que « faire » n'est même plus le bon mot."
    think "Peut-être qu'il faut seulement rester là, sans solution."

    pause 0.5

    $ blink()

    "Une porte s'ouvre dans le couloir. Des pas discrets passent devant ma chambre."
    think "Quelqu'un ne dort pas."

    pause 0.6

    menu:
        "Ouvrir la porte.":
            jump _5_0_NUIT_OUVRIR

        "Écouter sans bouger.":
            jump _5_0_NUIT_ECOUTER

        "Ignorer les pas et rester allongé.":
            jump _5_0_NUIT_RESTER

label _5_0_NUIT_RETOUR:

    $ blink()

    think "Je ferme les yeux. Le corps tombe toujours avant la tête."

    think "Le vote est probablement perdu. Pourtant, m'être levé, avoir frappé aux portes, être resté là…"
    think "Ça ne ressemble pas tout à fait à une défaite."
    think "Je me suis battu quand même. Personne ne pourra me le reprocher."

    pause 0.4

    think "Je ne sais pas encore ce que ça veut dire."

    $ blink()
    pause 1.5

    think "Demain sera difficile. Mais j'y serai quand même."
    "Puis le sommeil arrive rapidement."

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

    if _j50_sael_choice == "finish":
        return

    if _j50_sael_choice == "lit":
        $ j50_sael_mark_seen("lit")
        think "Le lit n'est pas défait."
        think "Il a été refusé."
        sael neutre "Le lit était trop mou."
        sael "On dort mal quand le corps oublie le sol."
        if j50_sael_pnc_score >= 3:
            return
        jump _5_0_SAEL_PNC

    if _j50_sael_choice == "crane":
        $ j50_sael_mark_seen("crane")
        think "Je ne sais pas si c'est un souvenir, un avertissement ou une prière."
        think "Chez elle, même les morts semblent avoir une fonction."
        sael neutre "Ne touche pas."
        if j50_sael_pnc_score >= 3:
            return
        jump _5_0_SAEL_PNC

    if _j50_sael_choice == "affaires":
        $ j50_sael_mark_seen("affaires")
        think "Elle n'a pas décoré sa chambre."
        think "Elle l'a rendue habitable selon ses propres règles."
        think "Pas confortable. Habitable."
        if j50_sael_pnc_score >= 3:
            return
        jump _5_0_SAEL_PNC

    return


label _5_0_NUIT_OUVRIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_242
    scene bg_dortoir at adaptive_fullscreen with dissolve

    "J'entrouvre la porte. Une silhouette disparaît au bout du couloir."
    think "Trop vite pour un visage. Pas assez pour l'inventer."

    think "Le Conclave ne dort pas."
    think "Il se déplace à voix basse."

    scene bg_cg012 at adaptive_fullscreen with dissolve
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_ECOUTER:

    think "Je reste immobile. Les pas ralentissent derrière la porte."

    if doplleganger == 0:
        julian "Je voulais aider."
        pause 0.5
        julian "Non. Trop faible."
        julian "J'ai porté une idée que vous n'étiez pas prêts à comprendre."
    else:
        elias fatigue "C'est moche."
        pause 0.5
        elias "Mais ça tient."
        elias "Faut que ça tienne jusqu'à demain, c'est tout."

    think "Puis les pas s'éloignent."
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_RESTER:

    think "Je pourrais me lever."
    think "Je pourrais ouvrir."
    think "Mais ce soir, je n'ai plus la force de devenir utile."

    jump _5_0_NUIT_RETOUR

# total : 8m
# Total jour 0-5 : 1h41
