# --------------------------------------------------------------------------------------------
# JOUR 5 — 5_0.rpy
# Vote Jour 4 : NON (status quo des rations — branche 4_0)
# Noam = narrateur principal, parle à la première personne.
# --------------------------------------------------------------------------------------------

default j50_sael_pnc_score = 0
default j50_sael_visit_awkward = False
default j50_julian_relation = 0
default j50_night_memory = "aucun"
default j50_observation_followup = False
default j50_sael_pnc_seen = []
default j50_julian_fissure = 0
default j50_wire_success = 0
default j50_wire_errors = 0
default j50_kamyz_bonus = 0
default j50_wire_selected = None
default j50_wire_done = []
default j50_wire_right_done = []
default j50_wire_connections = []
default j50_wire_time_left = 11.0
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
        store.j50_wire_time_left = 11.0
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
            store.j50_wire_time_left = 11.0
            store.j50_wire_feedback = "CONNEXION VERROUILLÉE — chronomètre réinitialisé."
            renpy.sound.play("audio/sfx_qte_hit.wav")
            if store.j50_wire_success >= len(J50_WIRE_COLORS):
                store.j50_wire_completed = True
        else:
            store.j50_wire_errors += 1
            store.j50_wire_time_left = max(1.5, store.j50_wire_time_left - 2.0)
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
            store.j50_wire_time_left = 11.0
            renpy.sound.play("audio/sfx_qte_miss.wav")

            if store.j50_wire_lives <= 0:
                store.j50_wire_failed = True
                store.j50_wire_feedback = "ÉCHEC — alimentation de secours interrompue."
            else:
                store.j50_wire_feedback = "TEMPS ÉCOULÉ — reprise d'urgence : 11,0 s."

        renpy.restart_interaction()

    def j50_wire_abandon():
        store.j50_wire_lives = 0
        store.j50_wire_failed = True
        store.j50_wire_selected = None
        store.j50_wire_feedback = "CONNEXION ABANDONNÉE."
        renpy.restart_interaction()

# Panne J5 : pulsations d'alerte irrégulières, sans timer bloquant ni hasard
# recalculé au rafraîchissement de l'interface. L'éclairage reste actif
# pendant le mini-jeu et la discussion, puis s'arrête à l'ouverture.
transform j50_emergency_red_pulse:
    alpha 0.10
    linear 0.18 alpha 0.34
    pause 0.56
    linear 0.07 alpha 0.02
    pause 0.22
    linear 0.14 alpha 0.29
    pause 0.83
    linear 0.05 alpha 0.0
    pause 0.42
    linear 0.23 alpha 0.37
    pause 0.19
    linear 0.09 alpha 0.09
    pause 0.71
    repeat

screen j50_emergency_lighting():
    zorder 85
    add Solid("#ff101c") at j50_emergency_red_pulse

screen j50_sael_room_pnc():
    modal True
    zorder 200

    add Solid("#000")
    add "images/background/scene/bg_chambre_sael.png" at cover_screen

    textbutton "Terminer la visite":
        xpos 1480
        ypos 925
        text_size 28
        background Solid("#081722dd")
        action Return("sortir")

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
                bar value AnimatedValue(j50_wire_time_left, 11.0, delay=0.1):
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
            text "Chaque liaison remet le délai à 11 s." size 18 color "#73899c" xsize 310

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
    $ j50_kael_alert_sent = False
    $ j50_observation_circuit_status = "inconnu"
    $ j50_night_memory = "aucun"
    $ j50_julian_relation = 0
    $ j50_julian_fissure = 0
    $ j50_observation_followup = False

    $ blink()
    think "J'ai encore du mal à croire que le vote d'hier soit terminé. Demain, on recommence."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je récupère ma tablette sur le bureau. Rien de neuf, à part le rappel du prochain scrutin."
    noam neutre "Déjà..."
    play sound sfx_knock
    noam surpris "Oui ?"
    elen "Noam ? T'es réveillé ?"
    noam neutre "Techniquement."
    elen "Tu peux ouvrir ? Juste deux secondes."
    "J'ouvre la porte, encore à moitié endormi."
    $ showGroup([("elen", "sourire", 0.70), ("noam", "neutre", 0.28)])
    elen sourire "Salut ! J'ai un service à te demander."
    noam inquiet "Il est huit heures."
    elen sourire "Oui ! C'est pour ça que je viens maintenant."
    noam reflechit "Ce n'est pas une explication."
    elen "Tu aurais de la cannelle ?"
    $ kd_queue_character_motion("noam", "surprise")
    noam surpris "De la... cannelle ?"
    elen "Même un tout petit peu. Un sachet oublié, un fond dans une boîte..."
    noam neutre "Pourquoi j'aurais de la cannelle dans ma chambre ?"
    elen "Je sais pas ! Tu pourrais aimer cuisiner."
    noam sourire "Tu as demandé à tout le dortoir ?"
    elen "Pas encore."
    noam neutre "Elen."
    elen "Quoi ?"
    noam sourire "Tu fais du porte-à-porte pour une épice."
    elen "C'est pas une épice quelconque."
    noam "Ah."
    elen "Je voulais juste donner un peu de goût au petit-déjeuner. J'en ai marre que tout ait le même goût."
    noam "Tu comptes mettre de la cannelle sur quoi ?"
    elen "Je trouverai. C'est pas le problème."
    noam sourire "Ça ressemble pourtant au principal problème."
    elen "Tu m'aides ou tu fais ton intéressant ?"
    noam "Je n'ai pas de cannelle, Elen."
    elen "Bon. Au moins, c'est clair."
    elen "Bon, si tu trouves de la cannelle..."
    noam "Je te préviens immédiatement. Priorité absolue."
    elen "Tu te moques, mais je note."
    "Elle s'éloigne déjà vers la porte suivante."
    think "À peine réveillé, et j'ai participé à une opération de contrebande culinaire."

    play sound sfx_announce
    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen
    show screen kami_broadcast_ui
    call KAMI_BROADCAST_WAIT_OPEN from _call_kami_broadcast_wait_open_j50
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "BOOOONJOUR ! Quel bonheur de vous savoir si actifs dès le matin !"
    kami "Petit rappel : la prochaine livraison est prévue au jour 7. Jusque-là, inutile de marchander avec Goumi."
    kami "Et oui, Elen, je parle aussi de la cannelle."
    $ bc_show("elen", "colere")
    elen "C'EST PAS DE LA MARCHANDISE !"
    $ bc_hide()
    kami "Oh, je sais. Tu as demandé à quatre personnes et menacé un grille-pain. C'est une quête spirituelle."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Demain, nouveau scrutin. Vous avez encore toute une journée pour changer d'avis. Ou pour vous persuader que vous aviez raison depuis le début."
    kami "Personnellement, j'apprécie les deux spectacles."
    call KAMI_BROADCAST_CLOSE from _call_kami_broadcast_close_j50
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    "Ma tablette vibre : rappel du vote de demain."
    think "Sael a dit non. Ryn n'a pas arrêté d'en parler. Et Julian... ça fait un moment que personne ne l'a vraiment vu."
    "Je retrouve mon dessin de Juliette sur le bureau et le glisse soigneusement sous la tablette."
    think "Je vais parler à Sael. Pas pour lui arracher un oui. J'aimerais au moins arrêter de deviner ce qu'elle pense."
    # Le déplacement utilise l'animation de sortie de chambre existante.
    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_231
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.4
    think "Un morceau de tissu noir est noué à sa poignée. Je n'avais jamais remarqué."
    play sound sfx_knock
    pause 0.4
    sael "Une minute !"
    "Quelque chose cogne contre le sol, suivi d'un juron étouffé."
    noam inquiet "Ça va ?"
    sael "Oui."
    pause 0.4
    sael "Non. Attends."
    "Le verrou tourne enfin."
    play sound sfx_door
    $ showGroup([("sael", "mefiant", 0.65), ("noam", "hesitation", 0.30)])
    sael mefiant "Noam."
    noam sourire "Salut."
    sael mefiant "Si tu viens me parler des frontières, je te préviens..."
    noam neutre "Je peux commencer par autre chose."
    sael "Comme quoi ?"
    "La porte d'à côté s'ouvre. Elias en ressort avec une longue planche sur l'épaule, qu'il manque de coincer contre l'encadrement."
    $ showGroup([("elias", "gene", 0.18), ("noam", "surpris", 0.44), ("sael", "neutre", 0.78)])
    noam surpris "Elias ? Qu'est-ce que tu fiches avec ça ?"
    $ kd_queue_character_motion("elias", "embarrassed")
    elias gene "Ah ! Salut, Noam. Je... je donne un coup de main."
    noam "En déménageant le lit ?"
    elias "Pas le lit entier ! Juste... cette partie."
    sael neutre "Elias, fais attention au mur."
    elias "Oui ! Pardon. Je la pose où ?"
    sael "À l'atelier. Comme prévu."
    elias "C'est vrai. Oui. Bon, à plus !"
    "Il repart en tenant sa planche à deux mains. Sael s'écarte pour me laisser passer."
    $ showGroup([("sael", "neutre", 0.69), ("noam", "reflechit", 0.29)])
    sael "Entre. Je t'expliquerai."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_sael") from _call_MAYBE_PLAY_SCRIPTED_DOOR_232
    scene bg_chambre_sael at adaptive_fullscreen with dissolve
    "Son matelas est par terre. Les planches du sommier s'alignent contre le mur. À côté, des morceaux de bois, des cordes, de petits outils."
    $ kd_queue_character_motion("noam", "surprise")
    noam surpris "Tu as démonté toute la chambre ?"
    sael sourire "Non. Les murs sont toujours là."
    noam neutre "Très rassurant."
    sael neutre "Le lit était trop haut. Je dors mal dessus."
    noam inquiet "Attends... on a le droit de démonter des meubles ici ?"
    sael reflechit "Pourquoi on n'aurait pas le droit ?"
    noam "Parce que dégrader volontairement les biens du Conclave, c'est interdit. Tu sais, le règlement ?"
    sael neutre "Je sais. J'ai demandé à Kami avant de toucher au lit."
    noam surpris "Et elle a accepté ?"
    sael "Oui. Du moment que je garde tout et que je puisse le remonter."
    noam "C'est presque raisonnable, venant d'elle."
    sael sourire "Elle m'a quand même demandé si je comptais construire une catapulte."
    noam "Tu lui as répondu quoi ?"
    sael neutre "Que j'aurais demandé davantage de planches."
    noam "Ah."
    sael "Elias m'aide à porter celles qui m'encombrent. Il a insisté."
    noam "Il avait surtout l'air de regretter."
    sael "Il a aussi insisté pour commencer par la plus lourde."
    sael "Tu peux regarder, mais fais attention. Et ne touche pas aux objets accrochés au mur."
    noam "Compris."
    $ j50_sael_pnc_score = 0
    $ j50_sael_pnc_seen = []
    $ j50_sael_visit_awkward = False
    call _5_0_SAEL_PNC from _call_5_0_SAEL_PNC
    $ showGroup([("noam", "neutre", 0.25), ("sael", "neutre", 0.75)])
    sael "Bon. Tu veux t'asseoir ?"
    noam "Sur quoi ?"
    "Elle désigne un tabouret."
    noam inquiet "Il est encore entier, celui-là ?"
    sael sourire "Pour l'instant."
    "Je m'assieds prudemment."
    if j50_sael_visit_awkward:
        sael mefiant "Tu n'as pas besoin de tout comprendre à ce que j'ai amené ici."
        noam inquiet "Oui. J'ai été maladroit."
        sael "Un peu."
    else:
        sael neutre "Au moins, tu as attendu qu'on t'explique les choses avant de toucher."
        noam sourire "J'apprends vite. Surtout quand les objets sont pointus."

    sael neutre "Tu as parlé avec Ryn depuis hier ?"
    noam reflechit "Pas vraiment. Je crois qu'il est toujours en colère."
    sael "Ça lui arrive de ne pas l'être ?"
    noam "Je ne voudrais pas lancer de rumeur."
    sael sourire "Hm."
    pause 0.3
    sael "Hier, tu as essayé de calmer tout le monde."
    noam inquiet "C'était pas très réussi."
    if j4_frontieres_result == "pont":
        sael reflechit "Non, mais tu nous as au moins fait nous écouter pendant quelques secondes. C'est déjà plus que d'habitude."
    elif j4_frontieres_result == "rupture":
        sael mefiant "Tu as parlé à ma place. Ça, je n'ai pas apprécié."
        noam inquiet "Je sais. J'aurais pas dû."
    sael "J'ai rien contre lui, tu sais."
    noam "Ryn ?"
    sael "Oui. Enfin, ça dépend des moments."
    noam sourire "Là, par exemple ?"
    sael mefiant "Là, je préférerais qu'il ne soit pas dans ma chambre."
    "Elle reprend un petit outil et en nettoie la pointe avec un chiffon."
    noam "C'est pour quoi, ça ?"
    sael "Les clôtures. Chez moi, on les réparait tout le temps."
    noam reflechit "À cause des animaux ?"
    sael neutre "Entre autres."
    "Elle continue de frotter."
    noam "Tu sais, j'essayais pas de dire que Ryn avait raison hier."
    sael "Je sais."
    noam "Il a parlé des gens morts près des frontières. Je..."
    sael mefiant "Noam. Arrête."
    "Je me tais."
    sael "Je ne t'ai pas demandé de venir m'expliquer ce qu'il ressent."
    noam "Oui. Pardon."
    sael "Chez nous aussi, des gens sont morts. Tu ne les connais pas. Tu ne peux pas les comparer."
    noam inquiet "Je voulais pas les comparer."
    sael "Alors ne le fais pas."
    pause 0.5
    "Elle dépose l'outil sur une étagère, puis se rassied, sans me regarder."
    sael neutre "La première fois qu'on nous a volé quelque chose, c'était des outils. Mon père s'est mis en colère parce qu'on en avait besoin pour réparer une porte."
    noam neutre "D'accord."
    sael "Après, ça a été du bétail. Et puis les gens ont commencé à ne plus rentrer."
    "Je cherche une réponse. Je n'en trouve pas."
    sael "Depuis la fermeture, les enfants peuvent sortir sans qu'on leur coure après. C'est tout ce que je te demande de comprendre."
    noam inquiet "Et les familles séparées par cette même fermeture ?"
    sael mefiant "Je sais qu'elles existent."
    noam "Je sais."
    sael "Non, je crois pas. Tu as posé ta question comme si j'allais découvrir leur existence grâce à toi."
    noam inquiet "Ouais. Vu comme ça..."
    sael "Tu viens de Harmonie. Là-bas, ce n'est pas la même chose."
    noam reflechit "Non. Clairement."
    $ unlock_dossier_arg("p2_familles")
    "Sael se lève pour replacer le chiffon sur l'étagère."
    sael neutre "Mara est venue hier soir. Elle a posé presque les mêmes questions que toi. Mais elle a surtout voulu savoir comment on protège les passages."
    noam "Elle serait contre aussi ?"
    sael "Demande-lui. C'est son vote."
    noam "Je demanderai."
    sael reflechit "Si votre projet prévoyait une protection des villages, je le lirais. Mais ce n'est pas ce qui est écrit."
    sael determine "Demain, je voterai non."
    noam triste "D'accord."
    sael "Tu n'essaies même pas de discuter ?"
    noam neutre "Tu viens de me dire que tu voterais non."
    sael sourire "Pour une fois, on gagne du temps."
    noam sourire "Tu vois ? On peut être d'accord sur quelque chose."
    sael mefiant "Ne prends pas trop confiance."
    "À la porte, elle retient un instant la poignée."
    sael neutre "Au fait. Si tu croises Kael..."
    noam "Oui ?"
    sael "Dis-lui que je n'ai pas perdu ses vis."
    noam "Tu pourrais lui rendre."
    sael "Ce sont mes vis."
    noam "Je vais essayer de formuler ça diplomatiquement."
    "Elle ouvre la porte avec un léger sourire."
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_233
    scene bg_dortoir at adaptive_fullscreen with dissolve
    think "J'étais venu pour parler du vote. Je repars avec une dispute sur des vis à transmettre à Kael."
    think "Et Sael n'a pas changé d'avis. Je crois que je m'y attendais."
    jump _5_0_TEMPS_LIBRE_1


label _5_0_TEMPS_LIBRE_1:
    call START_FREE_TIME("_5_0_APRES_TEMPS_LIBRE_1") from _call_START_FREE_TIME_2


label _5_0_APRES_TEMPS_LIBRE_1:

    $ current_period = "Après-midi"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_234
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8
    think "Il est déjà l'après-midi. Je n'ai toujours pas revu Julian."
    "Je consulte ma tablette. Pas de message de lui. Je pourrais aller voir s'il est vraiment enfermé dans sa chambre."
    "La salle d'observation est aussi ouverte. J'aimerais regarder les relevés sur Limen sans devoir interrompre Sael toutes les deux minutes."
    think "Je ne ferai pas les deux aujourd'hui."


label _5_0_CRITICAL_CHOICE:

    menu (screen="critical_choice", noam_expr="hesitation", cc_prompt="Qu'est-ce qui compte le plus pour moi aujourd'hui ?", cc_targets={"Vérifier que Julian va bien.":{"label":"_5_0_0_JULIAN","pack":"mystere"},"Chercher des réponses dans les relevés.":{"label":"_5_0_1_OBSERVATION","pack":"origine"}}):
        "Qu'est-ce qui compte le plus pour moi aujourd'hui ?"

        "Vérifier que Julian va bien.":
            $ doplleganger = 0
            jump _5_0_0_JULIAN
        "Chercher des réponses dans les relevés.":
            $ doplleganger = 1
            jump _5_0_1_OBSERVATION


label _5_0_0_JULIAN:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_235
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5
    $ doplleganger = 0
    play sound sfx_knock
    noam "Julian ? C'est Noam."
    pause 0.5
    noam "Je voulais juste..."
    julian "S'il s'agit de refaire le vote, c'est non."
    noam sourire "Ça tombe bien, j'ai oublié mon urne."
    pause 0.3
    play sound sfx_door
    $ showGroup([("julian", "neutre", 0.65), ("noam", "neutre", 0.30)])
    julian taquin "Voilà donc notre grand médiateur. Tu viens prendre des nouvelles du perdant ?"
    noam inquiet "Je viens prendre des nouvelles de toi."
    julian sourire "Parfaitement vivant. Tu vois ?"
    noam "Je vois."
    julian "Tu peux maintenant rassurer tout le dortoir."
    noam "Je peux aussi entrer ?"
    "Julian soupire puis s'écarte."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_236
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "sourire", 0.65), ("noam", "reflexion", 0.30)])
    "Sa chambre est impeccablement rangée, sauf une tablette au milieu du bureau. La rediffusion du vote tourne en silence."
    noam surpris "Tu regardes encore ça ?"
    julian neutre "Je regarde ce que je pourrais faire différemment."
    noam "Le résultat est le même, tu sais."
    julian "Merci. Je n'avais pas remarqué."
    "Il arrête la vidéo, la remet deux secondes en arrière et me fait signe d'approcher."
    julian "Regarde mon visage, là."
    noam "Quoi, ton visage ?"
    julian "Est-ce que je parais convaincant ?"
    noam "Julian..."
    julian "Je pose une question simple."
    noam reflechit "Tu as l'air d'avoir mal dormi."
    julian "C'est vrai. Mauvaise réponse."
    noam "Tu devrais peut-être dormir, alors."
    julian "Attends. Je vais te montrer."
    "Il prend un petit brouilleur près de la tablette. Le voyant de la caméra au plafond s'éteint."
    $ unlock_codex_page("surveillance_conclave", with_notification=False)
    julian "Normalement, tout ce qu'on fait ici peut finir dans une diffusion."
    noam "Tu m'avais déjà dit que tu détestais ça."
    julian "Je déteste ne pas savoir quel moment on va montrer."
    "Il éteint le brouilleur et se place face à la caméra."
    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    julian triste "À tous ceux qui nous regardent : le résultat d'hier nous déçoit profondément..."
    "Il marque une pause. Trois secondes. Quatre."
    julian "Non. Trop long."
    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    $ kd_queue_character_motion("noam", "hesitate")
    noam surpris "Tu répètes un discours ?"
    julian neutre "Je travaille. Ne fais pas cette tête."
    noam "Je suis venu te demander comment tu allais !"
    julian taquin "Et tu as découvert un homme occupé. C'est rassurant."
    noam colere "Tu veux que je sois sincère ?"
    julian "Je sens que tu vas l'être même si je dis non."
    noam "Ton petit silence tragique, on dirait que tu attends que quelqu'un te remette une médaille."
    julian colere "Ah. Charmant."
    julian "Tu aurais dit quoi, toi ?"
    noam "Rien. J'aurais parlé normalement."
    julian taquin "Vraiment ? Montre."
    noam surpris "Pardon ?"
    julian "Là. À la caméra. Imagine que des millions de gens t'écoutent."
    noam "Je refuse."
    julian "Tu viens de dire que c'était simple."
    noam "J'ai dit normalement, pas simplement."
    "Il me tend le brouilleur avec un sourire beaucoup trop satisfait."
    julian "Allez. Dix secondes."
    menu:
        "Jouer le jeu et improviser.":
            $ j50_julian_fissure += 1
            $ j50_julian_relation += 1
            noam inquiet "Euh... bonjour. Alors, hier, ça s'est mal passé."
            julian "Continue."
            noam "On a essayé. On a perdu. Et je... voilà."
            julian "Tu viens de dire « voilà » à des millions de personnes."
            noam "Je t'avais prévenu."
            julian "Au moins, tu ne leur as pas demandé de patienter pendant une minute de silence."
        "Refuser catégoriquement.":
            $ j50_julian_relation -= 1
            noam neutre "Non. Je ne fais pas ton numéro."
            julian colere "Ce n'est pas un numéro."
            noam "Alors arrête de me demander de jouer dedans."
            "Julian reprend le brouilleur. Son sourire se crispe."
        "Lui proposer de parler sans caméra.":
            $ j50_julian_fissure += 1
            noam neutre "Coupe-la. On essaie sans public."
            julian "Et qui va juger ?"
            noam "Personne. C'est le principe."
            "Julian hésite avant d'éteindre la caméra."

    julian neutre "Quand j'étais plus jeune, j'ai fait un discours dans une salle quasiment vide."
    noam "Ah."
    julian "Il y avait huit personnes. Neuf en me comptant. Et une qui s'était trompée de salle."
    noam sourire "Tu comptes encore celle-là ?"
    julian taquin "Elle est restée jusqu'à la fin. C'est de la loyauté."
    noam "Et tu avais convaincu qui ?"
    julian "Aucune idée. J'avais passé la moitié du temps à regarder la porte."
    noam "Pourquoi ?"
    julian neutre "J'attendais quelqu'un."
    noam "Qui ?"
    julian "Peu importe."
    "Il relance la vidéo du vote, puis l'arrête presque aussitôt."
    julian decu "J'avais vraiment cru que ça passerait."
    noam neutre "Je sais."
    julian "Non. Tu crois que tu sais. J'ai passé des jours à dire aux gens que ça pouvait marcher."
    noam "Et Tomas ?"
    julian neutre "Quoi, Tomas ?"
    noam "Tu l'as coincé dans la salle de repos."
    $ kd_queue_character_motion("julian", "anger")
    julian colere "Je voulais qu'il écoute !"
    noam "Il écoutait. Il voulait juste que tu le laisses sortir."
    "Julian ouvre la bouche, puis tourne les yeux vers la tablette."
    julian decu "Oui. Bon."
    noam "Tu lui as parlé depuis ?"
    julian "Pas encore."
    noam "Tu pourrais."
    julian neutre "Je sais."
    noam "Tu veux que je..."
    julian "Non. Surtout pas."
    pause 0.3
    julian "Il m'a dit qu'il ne voulait plus discuter avec moi pendant un moment."
    noam "Alors laisse-lui un moment."
    julian "C'est ce que je fais."
    "Il coupe la vidéo. Cette fois, il ne la remet pas."

    menu:
        "Lui dire qu'on peut avoir besoin de lui sans l'admirer.":
            $ j50_julian_relation += 1
            $ j50_julian_fissure += 1
            noam neutre "Tu sais, on peut avoir besoin de toi sans applaudir à chaque fois que tu entres quelque part."
            julian taquin "Tu proposes que je fasse mon entrée plus discrètement ?"
            noam "Je propose que tu essaies une fois."
            julian "Je vais étudier cette idée révolutionnaire."
        "Lui reprocher de manipuler les autres.":
            $ j50_julian_relation -= 1
            noam colere "Tu prépares même tes réactions. Comment tu veux qu'on te fasse confiance ?"
            julian colere "Parce que les autres font toujours tout spontanément, peut-être ?"
            noam "Ils ne répètent pas leurs émotions devant un miroir."
            julian "Tu n'en sais rien."
        "Changer de sujet et lui proposer de manger.":
            $ j50_julian_relation += 1
            noam sourire "Elen cherche de la cannelle. Tu pourrais utiliser tes talents pour la négociation."
            julian surpris "De la cannelle ?"
            noam "C'est une crise majeure, apparemment."
            julian rire "Elle m'a envoyé trois messages. Je croyais qu'elle se moquait de moi."
            noam "Non. Elle prend ça très au sérieux."
            julian "Bon. Pour une fois, je peux peut-être sauver quelque chose."

    julian neutre "Demain, c'est le vote sur les frontières."
    noam "Oui."
    julian "Sael va dire non."
    noam "Je l'ai vue ce matin."
    julian reflechit "Elle t'a ouvert ?"
    noam "Après quelques minutes."
    julian "À moi, elle a dit qu'elle n'avait pas besoin d'un vendeur de porte à porte."
    noam sourire "Elle a peut-être raison."
    julian "Tu pourrais faire semblant d'être de mon côté cinq minutes."
    noam "J'étais de ton côté quand je suis venu frapper."
    "Il n'a rien à répondre à ça."
    if j50_julian_relation >= 1:
        julian hesitation "Je vais essayer de sortir ce soir."
        noam sourire "Même sans annonce préalable ?"
        julian "Ne pousse pas."
    else:
        julian neutre "Bon. Je crois que j'ai eu ma dose de conseils."
        noam "D'accord. Je te laisse."
    julian taquin "Et pas un mot sur mes répétitions."
    noam "Je ne promets rien concernant le discours du siècle."
    julian "Noam."
    noam sourire "Bonne journée."
    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:
    call KD_ROUTE_J5_NYRA from _call_optional_kd_route_j5_nyra
    call START_EXPLORATION_LIBRE("_5_0_1_OBSERVATION_ARRIVEE", title="Rejoindre la salle d'observation", destination_room="observation") from _call_exploration__5_0_1_OBSERVATION


label _5_0_1_OBSERVATION_ARRIVEE:

    # START_EXPLORATION_LIBRE conduit déjà à la salle d'observation :
    # ne pas relancer les portes/couloirs une seconde fois.
    $ doplleganger = 1
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.4
    $ showGroup([("elias", "neutre", 0.75), ("noam", "neutre", 0.25)])
    "Elias est penché sur une console. Devant lui, un gobelet de café et trois petits morceaux de papier."
    elias sourire "Noam ! Attends, ne bouge pas."
    noam surpris "Quoi ?"
    "Il ferme les yeux."
    elias reflechit "Quatre pas. Tu traînes un peu le pied gauche. Oui, c'est toi."
    noam reflechit "J'aurais pu te le dire."
    $ kd_queue_character_motion("elias", "laugh")
    elias rire "Mais c'est moins drôle !"
    noam "Tu fais ça pour t'amuser ?"
    $ kd_queue_character_motion("elias", "nervous")
    elias gene "J'essaie de reconnaître les gens au bruit. Ça sert parfois pour savoir qui arrive quand on travaille sous une console."
    noam "Et les papiers ?"
    elias "Un classement. Kael marche vite. Nyra marche presque sans bruit."
    noam "Et moi ?"
    elias sourire "Tu as l'air de chercher quelque chose."
    noam "Là, tu triches. Tu me regardes."
    elias gene "Ah. Oui."
    "Il pousse le gobelet un peu plus loin du clavier, sans vraiment le quitter des yeux."
    noam "Tu fais quoi ?"
    elias "Je vérifie les relevés. J'avais une comparaison à terminer avant de fermer."
    noam reflechit "Tu pourrais me montrer ceux de Limen ?"
    elias "Pourquoi pas. Tu cherches quoi ?"
    noam "Je suis allé voir Sael. Je voudrais comprendre ce qui se passe aux frontières."
    elias reflechit "Ça dépend de ce que tu appelles « ce qui se passe »."
    noam "Ce que les gens font. Ce qu'ils risquent. Les sanctions."
    elias "Ah ! Ça, j'ai. Assieds-toi, ce sera plus simple."
    "Je m'installe devant la console. Elias tire une chaise à côté de la mienne et s'assied."
    "Il ouvre un registre : vols près de dépôts, passages interdits, bagarres, distributions interrompues."
    elias inquiet "Certains noms reviennent plusieurs fois."
    noam "Tout ça, c'est pour cette semaine ?"
    elias "Oui. Enfin, tout ce que le système a enregistré. Pour le reste..."
    noam "On ne sait pas."
    elias "Voilà."
    "Un nom apparaît encore et encore à l'écran."
    noam "Tu sais ce qui lui est arrivé ?"
    elias "Pas personnellement. Je peux seulement te montrer les rapports."
    noam "C'est étrange de voir un même nom autant de fois sans savoir qui est la personne."
    elias "Oui."
    "Un bip résonne. Elias lève aussitôt la tête."
    noam surpris "Quoi ?"
    elias "Rien. Mon minuteur pour le café."
    noam "Tu mets un minuteur pour ton café ?"
    elias "Sinon je l'oublie."
    noam "Tu l'as déjà devant toi."
    elias sourire "Et pourtant, ça marche."
    "Il porte le gobelet à ses lèvres, grimace, le repose."
    elias "Froid."
    noam "Le minuteur ne fait pas de miracles."
    elias "Non, mais j'avais l'espoir. Et puis, ici, il fait vraiment froid."
    noam "Tu trouves ?"
    elias "Comparé aux Forges d'Axiome ? Là-bas, on transpire rien qu'en entrant. Ici, j'ai toujours les mains gelées."
    noam "Tu vas finir par demander une chaudière dans la salle d'observation."
    elias sourire "Non, non. Juste du café qui reste chaud deux minutes."
    "Elias veut attraper une fiche derrière la console. Son coude heurte le gobelet."
    "Pendant une fraction de seconde, il reste debout sur le bord."
    elias gene "Oh."
    elias peur "Non... non, non, non ! PAS LUI !"
    noam surpris "Elias ?!"
    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")
    play sound sfx_drop
    elias peur "NON ! NON, RATTRAPE-LE !"
    noam surpris "Moi ?!"
    elias "Oui, toi ! J'ai les mains prises !"
    noam "Mais il tombe de ton côté !"
    elias "Je le vois bien !"
    "Le gobelet glisse sur le rebord de la console."
    noam inquiet "Ne bouge pas, tu vas l'envoyer dans le panneau !"
    elias panique "Il va tomber dans le panneau !"
    noam "C'est ce que je viens de dire !"
    elias "Alors fais quelque chose !"
    noam panique "J'essaie !"
    "Je me jette en avant, sans savoir si je dois attraper le gobelet ou protéger la trappe."
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "peur", 0.74), ("noam", "surpris", 0.25)])
    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress
    if j50_coffee_trace_score >= 0.82:
        "Je rattrape le gobelet juste avant qu'il touche le sol."
        noam sourire "Je l'ai !"
        "Du café coule entre mes doigts, directement dans la trappe."
        elias peur "MAIS PAS LE CAFÉ ! C'ÉTAIT MON DERNIER !"
        noam inquiet "On a un problème un peu plus gros, là !"
    elif j50_coffee_trace_score >= 0.35:
        "Mes doigts accrochent le gobelet. Il rebondit sur la console."
        "Une grande éclaboussure disparaît sous le capot."
        elias panique "NON ! Mon café ! Putain, mon café !"
        noam inquiet "Elias, la console !"
    else:
        "Je manque le gobelet. Il frappe la console et se vide sur les connecteurs."
        elias panique "MON CAFÉ ! NON, LES CONNECTEURS ! PUTAIN !"
        noam peur "Recule !"
        call kd_vn_reaction("elias", "panique", "#ff9c55")
    "Elias tire son chiffon de sa poche et reste pétrifié, sans oser l'approcher du circuit."
    noam inquiet "Tu veux que j'essuie ?"
    elias "NON !"
    noam "D'accord !"
    "Un grésillement sec. Une diode s'éteint."
    elias inquiet "Recule."
    noam "C'est grave ?"
    elias "Je... recule, s'il te plaît."
    stop music fadeout 0.3
    play music "music/bgm_horror_pulse.mp3" fadein 0.6
    show screen j50_emergency_lighting
    play sound sfx_beep
    with hpunch
    "CLAC."
    "La porte se verrouille derrière nous."
    "Sur l'écran : « PANNE DU CONTRÔLE D'ACCÈS — SALLE ISOLÉE »."
    $ unlock_codex_page("securite_orbitale", with_notification=False)
    noam peur "Elias ?"
    elias panique "Le contrôleur pense qu'il y a un défaut de pression. Il isole la salle !"
    noam "Mais il y a de la fumée !"
    elias "La sécurité du panneau a coupé l'alimentation. La ventilation fonctionne encore."
    noam "Et la porte ?"
    elias "Elle est sur le même contrôleur local. Elle ne répond plus."
    noam "Tu peux appeler quelqu'un ?"
    elias "Oui. Enfin, on peut. Mais je peux essayer de relancer le secours d'abord."
    noam inquiet "D'abord ?"
    elias "Le circuit principal est coupé. Il reste un boîtier indépendant. Si on remet les liaisons, je peux tester la commande."
    noam "Et si on ne les remet pas ?"
    elias "On contacte Kael. Tout de suite."
    "Il soulève le capot du boîtier. Huit fils apparaissent, croisés, certains noircis."
    elias inquiet "Je vais isoler les prises abîmées. Tu raccordes les couleurs de gauche avec celles de droite."
    noam "Elias, je ne sais pas faire."
    elias "Les couleurs, Noam. Tu sais reconnaître les couleurs !"
    noam "Tu me rassures très mal."
    elias "Je sais ! Désolé. Fais attention aux deux rouges et aux deux bleus. Prends ceux qui restent libres."
    "L'écran affiche un décompte. Elias passe derrière la console pour couper les circuits endommagés."
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
        play sound sfx_beep
        "Les voyants passent au vert."
        elias rire "OUI ! Bien joué !"
        noam surpris "La porte ?"
        "Elle ne bouge pas."
        elias gene "Le secours répond. Pas la commande du verrou."
        noam "Donc on est toujours enfermés."
        elias "Oui. Mais on a sauvé l'alimentation."
        noam "On prévient Kael."
        elias inquiet "Attends. Je pourrais relancer le contrôleur local en deux minutes."
        noam "Tu en es sûr ?"
        elias "Je... je veux vérifier un truc."
        menu:
            "Lui laisser un dernier essai, sous surveillance.":
                noam neutre "Deux minutes. Et je garde ma tablette ouverte."
                elias "Marché conclu."
                call show_custom_title("Quelques minutes plus tard") from _call_show_custom_title_j50_wait
                scene bg_observation at adaptive_fullscreen with dissolve
                "Elias essaie un nouveau raccordement. Le contrôleur clignote puis s'éteint."
                $ showGroup([("elias", "fatigue", 0.74), ("noam", "inquiet", 0.25)])
                elias fatigue "Bon. Appelle-le."
                noam "Tu me l'avais dit."
                elias "Je sais. Et tu peux me le rappeler quand on sera sortis."
            "Appeler Kael immédiatement.":
                $ j50_observation_followup = True
                noam neutre "Non. Le circuit marche, mais la porte est verrouillée. On arrête là."
                elias inquiet "Je peux encore..."
                noam "Je te crois. Mais ce n'est pas le moment de le prouver."
                "Elias regarde les fils, puis repose son outil."
                $ showGroup([("elias", "fatigue", 0.74), ("noam", "neutre", 0.25)])
                elias fatigue "D'accord. Écris-lui."
        call _5_0_MESSAGE_KAEL from _call_j50_message_kael_success
    else:
        $ j50_observation_circuit_status = "panne_totale"
        play sound sfx_beep
        with hpunch
        "Le dernier voyant s'éteint."
        elias peur "Merde."
        noam inquiet "Quoi ?"
        elias fatigue "Le boîtier ne répond plus. C'est fini, on arrête."
        noam "Je contacte Kael."
        elias "Oui. Et dis-lui que la ventilation tient. C'est important."
        call _5_0_MESSAGE_KAEL from _call_j50_message_kael_failure

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")
    "Nous restons loin du panneau. La ventilation ronronne au-dessus de nos têtes."
    noam inquiet "Je crois qu'on va attendre un moment."
    elias fatigue "Ouais."
    noam "Tu veux t'asseoir ?"
    elias "Pas près du panneau."
    noam "Non, évidemment."
    "On s'installe contre le mur, en gardant les yeux sur la porte."
    elias fatigue "Tu crois que Kael va gueuler ?"
    noam "Peut-être un peu."
    elias "Je lui dirai que c'était ma faute."
    noam "Il va surtout vérifier qu'on respire encore."
    elias "Ouais... t'as raison."
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.74), ("noam", "inquiet", 0.25)])
    noam "Tu veux t'asseoir ?"
    elias fatigue "Ouais... d'accord."
    "Il s'assied près de moi, les mains encore tremblantes."
    noam "Ça va aller."
    pause 0.4
    elias "Je croyais que j'allais pouvoir arranger ça avant que Kael le sache."
    noam "Il allait bien finir par voir la porte bloquée."
    elias gene "Oui. Je sais."
    elias "À chaque fois que quelque chose ne va pas, il arrive et il trouve la solution en deux minutes."
    noam "Ça doit être pratique de travailler avec lui."
    elias "Ça l'est. C'est ça qui m'énerve."
    "Je ne réponds pas."
    elias "J'aimerais juste qu'il me laisse finir une fois. Sans avoir à me montrer où mettre les mains."
    noam "Tu as coupé le circuit avant qu'on se prenne une décharge."
    elias "Et j'ai renversé le café."
    noam "Oui. Ça aussi."
    "Il sourit à peine."
    elias "Je vais devoir lui expliquer pourquoi j'avais une tasse à côté d'une trappe ouverte."
    noam "Je peux dire que je t'ai bousculé."
    elias inquiet "Non ! Il va chercher une panne ailleurs !"
    noam "C'était une blague."
    elias "Ah."
    pause 0.3
    elias "Une mauvaise blague."
    noam sourire "Oui, bon."
    "Deux coups métalliques résonnent derrière la porte."
    kael "Elias ? Noam ? Vous m'entendez ?"
    elias sourire "OUI !"
    nyra "On vous entend. Éloignez-vous du panneau."
    "Un cliquetis, puis le verrou cède."
    hide screen j50_emergency_lighting
    stop music fadeout 0.5
    play music "music/bgm_low_tension.mp3" fadein 1.1
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.23), ("nyra", "reflechit", 0.48), ("elias", "gene", 0.74), ("noam", "reflexion", 0.91)])
    kael inquiet "Vous avez respiré de la fumée ? Quelqu'un est blessé ?"
    noam "Non. On va bien."
    elias "La ventilation n'a pas lâché."
    nyra reflechit "Je voudrais d'abord savoir pourquoi l'alerte automatique n'a rien envoyé."
    kael reflechit "Et moi, pourquoi le contrôleur d'accès a pris une panne locale pour un problème de pression."
    elias gene "Je peux expliquer le début."
    kael "Je t'écoute."
    $ kd_direct.begin("comedy", auto=False)
    $ kd_direct.fixed_close("elias", duration=.18)
    elias "J'ai renversé mon café."
    pause 0.3
    $ kd_direct.unlock()
    $ kd_direct.shot("reverse", "kael", duration=.18, hold=0)
    kael "Sur quoi ?"
    $ kd_direct.shot("field", "elias", duration=.18, hold=0)
    elias "La console."
    kael "Avec le capot ouvert ?"
    elias "Oui."
    $ kd_direct.simultaneous(("kael", "nyra"))
    "Kael se passe une main sur le visage."
    $ kd_direct.end()
    nyra neutre "C'est donc une erreur humaine, suivie d'une erreur de diagnostic du système."
    noam "On peut dire ça."
    if j50_wire_completed:
        kael reflechit "Le secours est rétabli. C'est déjà ça."
        elias "Noam a fait les raccordements."
        kael "Bien. Mais pourquoi vous avez attendu pour appeler ?"
        if j50_observation_followup:
            noam "On n'a pas attendu une fois la porte restée verrouillée."
            kael "C'est la bonne décision."
        else:
            elias fatigue "Parce que je pensais pouvoir réparer le contrôle local."
            kael "Tu n'as pas à faire tout ça seul, Elias."
            elias colere "Je sais !"
            "Nyra s'arrête de prendre des notes."
            elias gene "Désolé. Je sais."
    else:
        kael reflechit "L'alimentation de secours est morte. Il faudra changer le boîtier."
        elias fatigue "Oui."
        kael "Et vous n'avez pas insisté après ?"
        noam "Non."
        kael "Tant mieux. Les connecteurs auraient pu chauffer davantage."
    nyra reflechit "Je vais consigner l'incident. Et surtout la réaction du verrou. Le café n'explique pas pourquoi la salle s'est isolée."
    noam "Ça pourrait se reproduire ?"
    nyra "Nous n'en savons rien. C'est précisément ce que nous allons vérifier."
    kael calme "Elias, tu restes avec moi pour regarder le contrôleur. Pas de réparation solitaire."
    elias "D'accord."
    kael "Et tu poses ton prochain café dans le couloir."
    elias sourire "Je vais surtout prendre une tasse avec un couvercle."
    kael "Et la boire loin des consoles."
    "Elias se penche déjà vers les relevés interrompus."
    nyra reflechit "Ne touche plus aux données. Pas avant qu'on ait tout sauvegardé."
    elias inquiet "Oui. Pardon."
    "En quittant la pièce, je remarque que le dernier rapport affiché à l'écran ne correspond plus à celui que nous regardions avant l'accident."
    think "Probablement à cause de la coupure. Il faudra que je demande à Elias."
    jump _5_0_FIN_JOURNEE


label _5_0_MESSAGE_KAEL:
    $ j50_kael_alert_sent = True
    "J'ouvre la messagerie. Le réseau personnel répond encore."
    if j50_wire_completed:
        call messenger_play("j5_observation_secours", "kael", [("noam", "Kael ? Avec Elias, on est bloqués dans la salle d'observation. Le secours fonctionne, mais la porte ne s'ouvre pas."), ("kael", "Vous êtes blessés ? Le panneau chauffe encore ?"), ("noam", "Non. Ventilation active. On a arrêté les réparations."), ("kael", "Bien. Ne touchez plus à rien. J'arrive avec Nyra.")], objective_text="Prévenir Kael", notify=False) from _call_messenger_j50_secours
    else:
        call messenger_play("j5_observation_panne", "kael", [("noam", "KAEL ! On est enfermés avec Elias dans la salle d'observation. Court-circuit. Le boîtier de secours a lâché."), ("kael", "Vous êtes blessés ? La ventilation fonctionne ?"), ("noam", "Oui. Plus de fumée. On reste loin du panneau."), ("kael", "Parfait. Ne touchez plus à rien. Nyra et moi arrivons.")], objective_text="Demander de l'aide à Kael", notify=False) from _call_messenger_j50_panne
    noam "Ils arrivent."
    elias fatigue "Super."
    noam "Tu n'as pas l'air heureux."
    elias "Si. J'aurais juste préféré les accueillir autrement."
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
        think "Julian a essayé de me faire jouer dans son discours. Ça aurait presque été amusant s'il n'avait pas l'air si fatigué."
    else:
        think "J'ai encore le bruit du verrou dans les oreilles. Et cette odeur de café brûlé."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_241
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je pose la tablette et retire mes chaussures."
    "J'éteins la lumière."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    "Un verrou grince dans le dortoir."
    "Puis des pas s'arrêtent devant ma porte."
    think "Il y a forcément quelqu'un qui a une bonne raison de passer ici. Forcément."
    menu:
        "Ouvrir la porte.":
            jump _5_0_NUIT_OUVRIR
        "Écouter sans bouger.":
            jump _5_0_NUIT_ECOUTER
        "Rester au lit.":
            jump _5_0_NUIT_RESTER


label _5_0_NUIT_RETOUR:
    $ blink()
    "Le couloir redevient silencieux."
    if j50_night_memory == "vu":
        think "Je n'ai pas réussi à voir clairement qui c'était. Tant pis."
    elif j50_night_memory == "entendu":
        think "Je ne suis pas sûr qu'on apprécierait de savoir que j'écoutais derrière ma porte."
    else:
        think "Il y a des soirs où je préfère ne pas poser de questions."
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
    if _j50_sael_choice == "sortir":
        return
    $ showGroup([("sael", "neutre", 0.73), ("noam", "reflechit", 0.25)])
    if _j50_sael_choice == "lit":
        $ j50_sael_mark_seen("lit")
        think "Le matelas repose sur le sol, soigneusement plié au pied. Les planches ont été empilées contre le mur."
        noam sourire "Tu crois que je pourrais dormir comme ça chez moi ?"
        sael "Essaie."
        noam "Je te demande un conseil, pas un défi."
        sael "Je te conseille d'essayer."
        noam "Et pour me relever ?"
        sael sourire "Ça, c'est ton problème."
        noam "Tu ne m'aides pas beaucoup."
        sael "Je ne t'ai rien vendu."
    elif _j50_sael_choice == "crane":
        $ j50_sael_mark_seen("crane")
        think "Un petit crâne d'animal est décoré de ficelles. Je m'approche, sans le toucher."
        noam inquiet "C'est un vrai ?"
        sael "Oui."
        noam "Et tu l'as..."
        sael mefiant "Quoi ?"
        noam "Je sais pas. J'allais demander si c'était une décoration."
        sael "Chez moi, on ne jette pas ce qu'on peut conserver."
        noam "D'accord."
        sael "Tu le trouves bizarre."
        noam inquiet "Je ne suis juste pas habitué."
        sael "Ça, je peux l'entendre."
        noam "Je crois que j'ai fait une tête étrange."
        sael sourire "Oui."
        $ j50_sael_visit_awkward = True
    elif _j50_sael_choice == "affaires":
        $ j50_sael_mark_seen("affaires")
        think "Des sacs de toile débordent de petites réparations, d'outils et de bouts de tissu."
        noam "Tu as emporté toute ta boîte à outils ?"
        sael "Presque."
        noam "Moi, j'ai surtout emporté des vêtements."
        sael "Tu peux toujours en faire des chiffons."
        noam "J'espère ne jamais en arriver là."
        sael "Tu m'as demandé."
        noam "Tu as raison."
        sael "Et ne me demande pas mes vis pour Kael."
        noam sourire "Je n'avais encore rien dit."
    if j50_sael_pnc_score >= 3:
        sael neutre "Tu as fait le tour."
        noam "Tu m'as laissé regarder."
        sael "Oui. Ça me change des gens qui ouvrent les tiroirs sans demander."
        return
    jump _5_0_SAEL_PNC


label _5_0_NUIT_OUVRIR:
    $ j50_night_memory = "vu"
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_242
    scene bg_dortoir at adaptive_fullscreen with dissolve
    "J'entrouvre la porte. Quelqu'un s'éloigne déjà."
    if doplleganger == 0:
        noam "Julian ?"
        "La silhouette se fige une seconde."
        julian "Rentre te coucher, Noam."
        noam "Tu fais quoi ?"
        julian "Je marche."
        noam "À cette heure-là ?"
        julian "Apparemment."
        "Il disparaît au coin du couloir, sans me laisser le temps d'ajouter quoi que ce soit."
    else:
        noam "Elias ?"
        elias "Oui !"
        noam "Tu peux me dire pourquoi tu es debout ?"
        elias "Je vais chercher de l'eau."
        noam "T'as soif ?"
        elias "Non. Enfin... oui."
        "Il serre sa tablette contre lui."
        elias "Bonne nuit, Noam."
        noam "Bonne nuit."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_ECOUTER:
    $ j50_night_memory = "entendu"
    "Je retiens mon souffle. Une voix me parvient."
    if doplleganger == 0:
        julian hesitation "Tomas, je voulais..."
        pause 0.3
        julian "Non. Pas comme ça."
        pause 0.3
        julian decu "Salut. T'as une minute ?"
        "Il soupire et reprend sa marche."
    else:
        "Les pas s'éloignent dans le couloir. Un peu plus loin, deux voix de femmes me parviennent, étouffées par la porte."
        nyra "Et à Nexus, vous vous connaissiez déjà ?"
        iris "Qui, Julian ?"
        "Une porte coulisse quelque part. Je perds la réponse d'Iris."
        nyra "Je demandais juste si vous aviez travaillé ensemble."
        iris "Non, enfin... pas vraiment. Il était surtout..."
        "Un chariot passe en grinçant. La fin de sa phrase disparaît sous le bruit des roues."
        nyra "Ah. D'accord."
        iris "Pourquoi ?"
        nyra "Pour rien. Bonne nuit, Iris."
        "Je n'entends plus que des pas. Je n'ai même pas compris ce qui les intéressait tant chez Julian."
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_RESTER:
    $ j50_night_memory = "rien"
    "Je retourne mon oreiller. La fatigue gagne."
    "Les pas s'éloignent et je m'endors sans savoir qui était dans le couloir."
    jump _5_0_NUIT_RETOUR
