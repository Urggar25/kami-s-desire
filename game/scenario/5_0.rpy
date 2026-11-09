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

    $ blink()
    think "Huit heures. J'ai pourtant l'impression d'avoir passé la nuit entière à fixer le plafond."
    think "Sael a dit non avant même qu'on vote. Et Ryn a réagi comme si elle avait personnellement appuyé sur la gâchette de chaque sanction."
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "J'aimerais parler à Sael. Pas pour lui extorquer un oui."
    think "Hier, tout le monde voulait obtenir une réponse. Personne n'a vraiment pris le temps d'écouter sa question."
    think "Et Julian... Lui qui se précipitait d'habitude devant la moindre caméra a disparu des discussions."
    think "Je ne sais pas ce qui m'inquiète le plus : qu'il prépare un discours ou qu'il n'en prépare plus."

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
    noam inquiet "Les groupes armés ? Ceux dont tu nous as parlé hier ?"
    sael triste "Ils venaient pour les récoltes, les outils, parfois juste pour montrer qu'ils pouvaient venir."
    sael triste "À force, on n'avait plus peur de perdre nos affaires. On se demandait qui serait le prochain à ne pas revenir."
    sael neutre "Depuis la fermeture, on peut retourner dans les champs sans guetter chaque bruit de moteur."
    sael triste "Je sais ce que Kami fait aux frontières. Je sais que des familles sont séparées."
    sael mefiant "Mais la dernière fois qu'on nous a promis des passages sûrs, ce sont d'autres hommes qui sont arrivés chez nous."
    noam reflechit "À Harmonie, on parle surtout des familles séparées. Je n'avais pas imaginé ce que l'ouverture pouvait signifier pour toi."
    $ unlock_dossier_arg("p2_familles")
    sael mefiant "Et tu voudrais que je mette mon village en danger pour réparer ce que ces familles subissent ?"
    noam inquiet "Non ! Je ne te demande pas de choisir entre deux groupes de victimes."
    noam inquiet "Justement... je n'ai pas de solution qui protège tout le monde."
    sael reflechit "Ryn non plus n'en a pas. Pourtant, il me parlait comme si j'avais personnellement signé chaque sanction."
    sael triste "Je ne lui demande pas d'oublier ses morts. J'aimerais simplement qu'il ne m'oblige pas à oublier les miens."
    noam calme "Il se sent abandonné. Ça n'excuse pas la façon dont il t'a parlé."
    noam calme "Et tu n'avais aucune raison de lui confier tout ça devant les autres."
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
    think "Mais maintenant je sais au moins pourquoi elle accepte d'être détestée pour ce choix."
    think "Mara hésite peut-être moins que je l'imaginais. Ça ne fait pas d'elle une alliée automatique de Sael."
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

    think "Après le temps libre, je repense à ma discussion avec Sael. Je comprends ses raisons, mais elle votera contre demain. Si je veux faire quelque chose d'utile, il me reste deux possibilités."
    think "Julian ne sort presque plus de sa chambre, et il s'est montré particulièrement agressif hier. Je pourrais aller vérifier comment il va, même si on risque de se disputer encore."
    think "Sinon, la salle d'observation permet de consulter les informations venant de la Terre. J'aimerais savoir comment les gens vivent avec les restrictions dont on parle depuis plusieurs jours."

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
    think "Je frappe à la porte de Julian. Une première fois, puis une deuxième quand il ne répond pas."
    play sound sfx_knock
    pause 0.5
    noam neutre "Julian, c'est moi. Je veux juste te parler, je vais pas rester longtemps."
    "J'entends un bruit, puis la porte s'ouvre."
    play sound sfx_door
    $ showGroup([("julian", "neutre", 0.65), ("noam", "neutre", 0.30)])
    julian taquin "Tiens, Noam. Tu viens me dire qu'il faut sourire et accepter la défaite ?"
    noam inquiet "Non, je voulais juste savoir comment t'allais. Tu t'es enfermé ici depuis le vote."
    julian sourire "Je vais parfaitement bien. Tu vois, je tiens debout, je parle et je suis même habillé. Tu peux faire ton rapport aux autres."
    noam colere "Tu peux arrêter deux secondes ? Je te demande pas ça pour me moquer."
    "Julian me regarde sans répondre, puis s'écarte pour me laisser entrer."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_236
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "sourire", 0.65), ("noam", "reflexion", 0.30)])
    think "Sa chambre est soigneusement rangée. Il a laissé sa tablette allumée sur une rediffusion du vote."
    noam inquiet "Tu regardes encore ça ?"
    julian decu "J'essaye de comprendre ce qui s'est passé. J'avais vraiment cru que le texte pouvait être adopté."
    noam neutre "Il y avait quand même un problème énorme avec la suppression des rations."
    julian colere "Je sais, Noam ! J'étais à la même table que toi. Tu crois que j'ai pas entendu ?"
    noam inquiet "Alors pourquoi tu fais comme si ceux qui ont voté contre étaient des idiots ?"
    julian neutre "Parce que je suis en colère. Ça t'arrive jamais, toi ?"
    "Il saisit le brouilleur posé près de la tablette et touche un bouton. L'indicateur lumineux s'éteint."
    $ unlock_codex_page("surveillance_conclave", with_notification=False)
    julian taquin "Tu vas voir un truc. Regarde bien la caméra."
    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3
    "La caméra au plafond pivote vers nous. Julian se redresse immédiatement et prend un air accablé."
    julian triste "J'ai fait tout ce que je pouvais pour ce vote. Je pensais qu'on pourrait enfin changer quelque chose, et certains ont préféré abandonner."
    julian decu "C'est difficile, mais je continuerai à me battre pour les gens qui nous regardent."
    noam surpris "Attends, tu viens vraiment de..."
    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    "Julian réactive le brouilleur et reprend aussitôt son expression habituelle."
    julian rire "Alors ? Convaincant, non ?"
    noam colere "Mais t'es sérieux ?! Tu viens de faire un petit discours devant la caméra juste pour te donner le beau rôle !"
    julian taquin "Je savais que tu comprendrais pas. Les gens ont besoin de voir qu'on continue à se battre, même quand on perd."
    noam inquiet "Et tu peux pas simplement leur parler normalement ?"
    julian neutre "Normalement, on dit des choses qu'on regrette. Et Kami adore quand on lui en donne l'occasion."
    noam reflechit "T'avais pourtant l'air vraiment en colère hier. C'était du cinéma aussi ?"
    julian decu "Non. J'étais furieux. Mais je peux être furieux et réfléchir quand même à ce que les gens vont voir."

    $ j50_julian_fissure = 0
    menu:
        "Lui reprocher de penser à sa réputation.":
            $ j50_julian_fissure += 1
            noam colere "J'ai quand même l'impression que tu penses beaucoup plus à ton image qu'aux gens qu'on représente."
            julian colere "Et toi, tu penses que les gens vont nous écouter si on passe pour une bande d'incapables ?"
        "Reconnaître qu'il est réellement déçu.":
            $ j50_julian_fissure -= 1
            noam neutre "D'accord, je te crois quand tu dis que t'étais déçu. Je crois juste que t'as mal réagi."
            julian decu "Ça, je veux bien l'admettre. J'aurais peut-être dû laisser Tomas tranquille."
        "Lui demander pourquoi il a autant insisté auprès de Tomas.":
            noam inquiet "Ce qui me dérange surtout, c'est ce que t'as fait avec Tomas. Tu l'as coincé dans la salle de repos."
            julian hesitation "Je voulais qu'il comprenne que son vote était important. J'ai insisté, oui. Un peu trop."

    julian neutre "Tu sais, j'avais passé du temps à préparer ce vote. Je m'étais dit que si on réussissait une fois, les autres arrêteraient de nous prendre pour des gamins."
    noam reflechit "Et depuis qu'on a perdu, tu demandes à tout le monde qui a voté contre. Tu te rends compte que ça va surtout leur donner peur de te parler ?"
    julian colere "Je voudrais juste savoir pourquoi quelqu'un a décidé de tout arrêter. C'est trop demander ?"
    noam neutre "Oui, si la personne voulait garder son vote secret. Ça faisait partie des règles dès le début."
    "Il ouvre la bouche pour répondre, puis se ravise. Ses yeux reviennent vers la rediffusion."
    julian decu "Tu sais ce qui m'énerve le plus ? C'est que si un autre arrive à faire adopter son texte demain, tout le monde aura oublié celui-là."
    noam surpris "Tu veux dire que tu serais pas content qu'on réussisse enfin ?"
    julian colere "Mais si ! Évidemment que si !"
    "Il répond un peu trop vite et s'en rend compte."
    julian hesitation "Enfin... j'aurais voulu qu'on réussisse avec le premier. J'y tenais, c'est tout."

    menu:
        "Lui dire qu'il n'a rien à prouver.":
            $ j50_julian_fissure += 1
            noam neutre "Julian, t'as pas besoin de réussir tous les votes pour que les autres te prennent au sérieux."
            julian inquiet "C'est facile à dire quand c'est pas toi qui as passé deux jours à convaincre tout le monde."
        "Lui demander ce qui l'inquiète vraiment.":
            $ j50_julian_fissure += 1
            noam inquiet "T'as vraiment peur qu'on oublie ce que t'as fait ? Même si quelqu'un d'autre réussit après toi ?"
            julian hesitation "Je veux pas passer pour celui qui a promis quelque chose et qui a tout raté."
        "Lui répondre que le résultat compte davantage.":
            $ j50_julian_fissure -= 1
            noam colere "On est pas là pour savoir qui a eu la meilleure idée, Julian. Ce qui compte, c'est ce qui arrive aux gens dehors."
            julian colere "Je sais ! Tu vas pas me répéter ça toute la journée !"

    "Julian récupère le brouilleur et le tourne entre ses doigts. Cette fois, il ne regarde pas la caméra."
    julian neutre "De toute façon, le prochain sujet, c'est les frontières. Ryn va encore hurler, Sael va refuser et on finira exactement au même endroit."
    noam inquiet "J'ai vu Sael ce matin. Elle est contre, oui, mais elle m'a expliqué pourquoi."
    julian reflechit "Elle t'a parlé ? T'as de la chance. Moi, elle m'a même pas laissé essayer."
    noam calme "Tu pourrais peut-être commencer par demander aux gens ce qu'ils pensent, au lieu de leur dire quoi voter."
    julian decu "Je t'ai entendu, Noam. Vraiment. Mais ça me demande un effort, tu sais."

    menu:
        "Lui proposer de sortir voir les autres.":
            $ j50_julian_fissure += 1
            noam sourire "Tu devrais venir manger avec nous. Même si t'as pas envie de reparler du vote."
            julian hesitation "Peut-être ce soir. Pas maintenant."
        "Lui demander de s'excuser auprès de Tomas.":
            $ j50_julian_fissure += 1
            noam neutre "Tu pourrais au moins t'excuser auprès de Tomas. Il était vraiment mal à l'aise."
            julian decu "Oui... J'y réfléchirai."
        "Lui dire qu'il se complique la vie.":
            $ j50_julian_fissure -= 1
            noam sourire "Tu sais que tu te compliques énormément la vie pour quelqu'un qui prétend toujours tout maîtriser ?"
            julian taquin "C'est pour ça que je suis exceptionnel."

    if j50_julian_fissure >= 3:
        julian inquiet "Noam, j'ai une question. Si demain vous arrivez à faire passer le texte sans moi... tu crois qu'on voudra encore m'écouter après ?"
        noam surpris "Julian, c'est pas une compétition. Bien sûr qu'on aura encore besoin de ton avis."
        julian hesitation "Ouais. J'imagine que tu peux pas vraiment me le promettre."
        think "Il semble regretter d'avoir posé la question, et je préfère ne pas insister."
    elif j50_julian_fissure >= 1:
        julian decu "Je vais essayer de revenir avec les autres. Mais j'ai pas envie de voir Ryn se réjouir de mon absence."
        noam sourire "Je pense qu'il a déjà assez à faire avec Sael. Tu risques de ne même pas être le sujet de conversation."
        julian taquin "Tu sais vraiment rassurer les gens."
    else:
        julian colere "Bon, je crois qu'on va continuer à se disputer si tu restes là. On peut arrêter pour aujourd'hui ?"
        noam neutre "Ouais. Je voulais juste savoir comment tu allais."
        julian decu "Maintenant, tu sais."

    "Julian pose le brouilleur sur son bureau et me raccompagne à la porte."
    julian neutre "Au fait, ne raconte pas aux autres ce que j'ai dit devant la caméra. Ils me prennent déjà assez pour un imbécile."
    noam sourire "Alors arrête de leur donner des raisons de le penser."
    julian taquin "Très drôle. Allez, à plus, Noam."
    think "Je repars sans vraiment savoir s'il va mieux, mais au moins il a accepté de discuter sans chercher à gagner chaque échange."

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
    think "Je suis venu consulter les chiffres des districts. J'espère au moins trouver des informations sur ce qui se passe réellement aux frontières."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_238
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "neutre", 0.75), ("noam", "neutre", 0.25)])
    "Elias est installé devant une console, avec une tasse de café posée à côté de lui."
    elias sourire "Noam ! J'allais justement fermer les relevés, t'arrives au bon moment."
    noam surpris "Tu m'as même pas vu entrer !"
    elias rire "J'ai reconnu tes pas. Tu traînes un peu du pied gauche, tu sais ?"
    noam sourire "Super, maintenant je vais y penser chaque fois que je marche."
    elias sourire "T'inquiète, je fais ça avec tout le monde. Tu voulais quelque chose ?"
    noam reflechit "Je cherche des infos sur Limen et les frontières. Après ce que Sael nous a dit, j'ai envie de voir comment les gens vivent là-bas."
    elias reflechit "Attends, je peux te montrer les rapports. J'essayais de comprendre pourquoi autant de gens ont été sanctionnés ces derniers jours."
    "Il ouvre une liste d'incidents : vols, bagarres, tentatives de passage entre districts. Plusieurs noms reviennent dans les rapports."
    noam inquiet "Tout ça, c'est juste pour cette semaine ?"
    elias inquiet "Ouais. Et encore, c'est seulement ce que les systèmes de Kami ont enregistré."
    noam triste "Il y en a qui se battent parce qu'ils n'ont pas assez à manger. Et on leur ajoute une sanction..."
    elias reflechit "C'est pas toujours pour manger, mais y en a beaucoup. Regarde le nombre de vols dans les centres de distribution."
    noam inquiet "On aurait vraiment besoin de voir quelqu'un qui vit là-bas, pas juste des chiffres."
    elias sourire "Je te l'aurais bien montré sur une caméra, mais c'est pas vraiment mon domaine. Moi, je répare surtout ce qui tombe en panne."
    "Il veut me montrer une autre ligne du rapport, se penche trop vite et accroche la tasse du coude."
    elias peur "Ah merde ! Le café !"
    play sound sfx_drop
    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")
    "La tasse bascule sur la console. Le café passe entre les touches et coule vers une trappe de maintenance mal refermée."
    "Je tends aussitôt le bras pour l'empêcher de tomber complètement."

    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress
    if j50_coffee_trace_score >= 0.82:
        "J'arrive à retenir la tasse avant qu'elle ne se fracasse par terre, mais une bonne partie du café a déjà coulé dans la trappe."
        elias inquiet "Merci ! Oh non, regarde, ça rentre sous le panneau..."
    elif j50_coffee_trace_score >= 0.35:
        "Je ralentis sa chute sans parvenir à la rattraper. La tasse heurte le bord du meuble et le café éclabousse la trappe ouverte."
        elias peur "Merde, j'aurais pas dû la poser là !"
    else:
        "Je rate la tasse. Elle tombe au sol, et le café se déverse directement sur les connecteurs exposés."
        elias panique "Oh non, non, non ! C'est pas vrai !"

    "Un grésillement retentit derrière la console. Elias se précipite sur le bouton d'arrêt du panneau, mais le voyant de sécurité s'allume avant qu'il puisse l'atteindre."
    noam peur "Ça fume ! On fait quoi ?"
    elias inquiet "Ne touche pas aux connecteurs ! Le café a dû provoquer un court-circuit sur le circuit de commande."
    "La ventilation accélère d'un coup. La porte se verrouille et une alarme apparaît sur l'écran : « PANNE DU CONTRÔLE D'ACCÈS — SALLE ISOLÉE »."
    $ unlock_codex_page("securite_orbitale", with_notification=False)
    noam inquiet "Pourquoi elle se ferme ? On devrait pouvoir sortir s'il y a un incendie !"
    elias panique "Normalement oui ! Mais là, le système croit peut-être qu'il y a une fuite ou un problème de pression. C'est une sécurité prévue pour isoler la salle, pas pour un café renversé !"
    noam peur "Et si ça commence vraiment à brûler ?"
    elias inquiet "Le disjoncteur a coupé l'alimentation principale de ce panneau. Ça devrait arrêter la chauffe, mais on doit remettre les circuits de secours en marche."
    elias reflechit "J'ai un boîtier de raccordement ici. Le câblage a des codes couleur, heureusement. Tu peux m'aider ?"
    noam inquiet "Tu veux que je fasse quoi exactement ? Je connais rien à ça !"
    elias inquiet "Tu relies les fils de même couleur, un par un. Moi, je coupe ce qui est abîmé et je vérifie qu'on n'envoie pas de courant dans le mauvais circuit."
    "Il soulève le capot du boîtier de secours et m'indique les huit raccordements à remettre en place. Un signal sonore prévient que la batterie de contrôle est presque vide."

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
        elias rire "Oui ! Le circuit de secours est revenu ! Bien joué, Noam !"
        "Les voyants de ventilation repassent au vert, et un message confirme que la demande d'ouverture a été envoyée à la maintenance."
        noam sourire "Ça veut dire qu'on peut sortir ?"
        elias inquiet "Pas encore. Le verrouillage doit être levé depuis l'extérieur, mais au moins la pièce est stable et ils ont reçu notre signal."
    elif j50_wire_success >= 5:
        elias inquiet "Bon, t'as réussi à remettre une partie des raccordements. La ventilation fonctionne, mais le panneau de la porte répond toujours pas."
        "Elias utilise la batterie restante pour déclencher une alerte manuelle vers la maintenance."
        noam inquiet "On va devoir attendre qu'ils viennent ?"
        elias reflechit "Ouais. Mais normalement, ils verront le signal."
    else:
        elias panique "Merde, la batterie de secours est vide. Le boîtier ne répond plus du tout."
        "Elias coupe les derniers circuits accessibles et nous fait nous éloigner de la console. La ventilation principale continue de tourner, mais il n'a plus accès à la commande de la porte."
        noam peur "Tu peux prévenir quelqu'un ?"
        elias inquiet "Je vais essayer avec le communicateur d'urgence, s'il est pas branché sur le même panneau. Sinon, on attend que la maintenance voie la panne."
        "Il tente plusieurs appels avant d'obtenir un signal de confirmation très bref."
        elias fatigue "Bon, au moins le message est parti. Désolé, j'ai vraiment fait n'importe quoi avec cette tasse."

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")
    "Nous nous éloignons du panneau. L'odeur de café chaud a été remplacée par celle des composants brûlés."
    noam inquiet "Tu crois que ça va coûter cher à réparer ?"
    elias fatigue "Si Kael voit l'état du contrôleur, il va m'en parler pendant des semaines. Et franchement, il aura raison."
    noam sourire "Je peux lui dire que c'est moi qui t'ai fait tomber la tasse."
    elias inquiet "Non, ça va pas ! C'était moi. Et puis je préfère qu'il sache ce qui s'est passé, sinon il réparera peut-être pas le bon truc."
    "Nous nous asseyons à distance de la console en attendant que quelqu'un rétablisse l'accès. Elias regarde régulièrement le voyant de l'alarme."
    elias neutre "Au fait, t'as parlé à Sael ? Pour les frontières, je veux dire."
    noam reflechit "Oui, ce matin. Elle m'a expliqué ce qu'ils ont vécu dans son village. Elle votera contre demain."
    elias triste "Ah... Je m'en doutais. J'espérais quand même qu'on pourrait trouver un compromis."
    noam inquiet "Le texte ne prévoit pas de compromis. C'est bien le problème. On peut pas protéger son village et laisser les familles circuler avec cette seule question."
    elias reflechit "C'est vraiment mal fichu, leurs votes. Je sais même pas ce que je vais choisir."
    noam neutre "Moi non plus. Et je crois pas qu'on puisse régler ça ici, coincés devant une console grillée."
    elias sourire "Ouais, ce serait déjà pas mal qu'on arrive à sortir."

    call show_custom_title("Un peu plus tard") from _call_show_custom_title
    scene bg_observation at adaptive_fullscreen with dissolve
    if j50_wire_completed:
        "L'alarme s'arrête enfin. La maintenance a pu réinitialiser le verrouillage à distance, mais la console reste hors service."
        elias sourire "Ça y est ! Ils ont accepté la demande d'ouverture. On va pouvoir sortir."
    else:
        "Après plusieurs tentatives, une équipe de maintenance répond à l'appel d'urgence. Quelqu'un coupe le verrouillage depuis le couloir et nous demande de ne plus toucher à la console."
        elias fatigue "Ils vont devoir remplacer le contrôleur. Je sens qu'on va m'en parler longtemps."
    play sound "sound/sfx_door.ogg"
    "La porte s'ouvre. Je quitte la salle avec Elias, qui s'arrête une dernière fois devant le panneau abîmé."
    elias inquiet "Je vais prévenir Kael avant qu'il découvre ça par hasard. Et je lui dirai exactement ce qui s'est passé."
    noam sourire "Bonne idée. Et la prochaine fois, pose ton café ailleurs."
    elias rire "Promis ! Enfin... je vais essayer."
    think "Je n'ai pas trouvé toutes les réponses que j'étais venu chercher, et une partie de la console est hors service. Elias a au moins réussi à prévenir la maintenance, mais je me demande si cette panne aura d'autres conséquences."

    jump _5_0_FIN_JOURNEE


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
        think "Je quitte Julian et retourne au dortoir. J'espère qu'il finira par discuter avec les autres, même si je sais qu'il aura du mal à passer sur le résultat du vote."
    else:
        think "En rentrant depuis la salle d'observation, je repense à Elias et à sa console. J'espère que Kael pourra réparer les dégâts avant que quelqu'un ait besoin des relevés."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_241
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je pose ma tablette sur le bureau et m'assieds sur le lit."
    think "Demain, Sael votera contre. Je comprends pourquoi elle refuse de prendre le risque, mais ça n'empêche pas Ryn d'avoir raison quand il parle de ceux qui meurent aux frontières."
    think "J'aimerais qu'on puisse voter sur quelque chose de moins brutal. Pour le moment, Kami ne nous a laissé que ces deux possibilités."
    "Je me change et je me couche. Je commence enfin à m'endormir quand j'entends une porte s'ouvrir dans le dortoir."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    think "Quelqu'un marche dans le couloir. Il est tard, et les pas ralentissent près de ma chambre."

    menu:
        "Ouvrir la porte.":
            jump _5_0_NUIT_OUVRIR
        "Écouter sans bouger.":
            jump _5_0_NUIT_ECOUTER
        "Ignorer les pas et rester allongé.":
            jump _5_0_NUIT_RESTER

label _5_0_NUIT_RETOUR:

    $ blink()
    think "Les pas finissent par s'éloigner. Je me demande qui se promène encore à cette heure-là, puis je renonce à y réfléchir."
    think "Demain, il faudra affronter un autre vote. Je ne sais pas ce qu'il donnera, mais je compte au moins écouter les autres avant de me décider."
    "Je m'endors quelques minutes plus tard."

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
        think "Le cadre du lit est démonté et les planches sont rangées contre un mur. Sael a gardé le matelas et posé une couverture dessus."
        noam surpris "T'as démonté tout ça toute seule ? Ça a dû te prendre du temps."
        sael neutre "Un peu. Chez moi, on dort souvent sur des couches plus simples. Je suis plus à l'aise comme ça."
        noam sourire "Moi, je crois que j'aurais gardé le lit. J'ai déjà assez de mal à dormir."
        sael sourire "C'est ton choix. Je vais pas venir démonter le tien."
    elif _j50_sael_choice == "crane":
        $ j50_sael_mark_seen("crane")
        think "Un petit crâne d'animal est posé parmi des morceaux de bois et des ficelles. Il a été nettoyé et décoré à la main."
        noam inquiet "C'est un vrai crâne ?"
        sael neutre "Oui. Il vient d'un animal qu'on a chassé. Chez nous, on essaie de ne pas gaspiller ce qu'on prélève."
        noam neutre "D'accord. Je te demande parce que j'en ai jamais vu chez moi."
        sael mefiant "Tu peux regarder, mais évite d'y toucher. J'y tiens."
    elif _j50_sael_choice == "affaires":
        $ j50_sael_mark_seen("affaires")
        think "Ses affaires sont rangées dans de petits sacs en toile. Elle a aussi gardé des morceaux de tissu et quelques outils."
        noam reflexion "Tu as ramené tout ça de chez toi ?"
        sael neutre "Presque tout. Je savais pas ce qu'ils nous laisseraient garder, alors j'ai pris surtout des choses utiles."
        noam sourire "J'aurais dû faire pareil. J'ai pris des trucs dont je me sers même pas."
        sael reflechit "Si tu en as besoin un jour, tu seras peut-être content de les avoir."
    else:
        return

    if j50_sael_pnc_score >= 3:
        sael sourire "Bon, tu as fait le tour. Tu voulais surtout parler du vote, non ?"
        return
    jump _5_0_SAEL_PNC

label _5_0_NUIT_OUVRIR:

    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_242
    scene bg_dortoir at adaptive_fullscreen with dissolve
    "J'entrouvre ma porte. Quelqu'un est déjà presque au bout du dortoir."
    if doplleganger == 0:
        think "Je crois reconnaître la façon de marcher de Julian, mais il tourne au coin avant que je puisse le voir de face."
        noam neutre "Julian ?"
    else:
        think "La silhouette tient quelque chose sous le bras. Je me demande si c'est Elias qui revient de la maintenance."
        noam neutre "Hé, il y a quelqu'un ?"
    "Personne ne répond. Je reste quelques secondes dans le couloir avant de retourner me coucher."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_ECOUTER:

    think "Je reste au lit et j'écoute les pas. Quelqu'un s'arrête à proximité, juste assez longtemps pour que je distingue sa voix."
    if doplleganger == 0:
        julian decu "Non, c'est pas ce que je voulais dire..."
        pause 0.3
        julian neutre "Bon, je recommencerai demain. Si je les vois, je m'excuserai. Enfin, j'essaierai."
        think "Julian parle tout seul. Il prépare peut-être ce qu'il dira aux autres, ou à Tomas."
    else:
        elias fatigue "Kael, j'ai vérifié, le message d'erreur est toujours là..."
        pause 0.3
        elias inquiet "Non, on a coupé le panneau. Il devrait plus rien alimenter, mais faudrait quand même le regarder demain."
        think "Elias semble parler dans son communicateur. La panne de la salle d'observation le préoccupe encore."
    "Les pas reprennent puis s'éloignent. Je ne les entends bientôt plus."
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_RESTER:

    think "Je n'ai pas envie de sortir vérifier. Les autres ont bien le droit de se déplacer sans que je leur demande des explications."
    "Je remonte la couverture et j'attends que les pas s'éloignent."
    jump _5_0_NUIT_RETOUR

# total : 8m
# Total jour 0-5 : 1h41
