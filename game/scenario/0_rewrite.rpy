# JOUR 0 — REVEIL / PROLOGUE RECONSTRUIT
# Anciens alias audio conservés pour les autres journées.
define sfx_door = "sfx/door_soft.mp3"
define sfx_beep = "sfx/terminal_beep.ogg"
define sfx_paper = "audio/sfx_paper.mp3"
define sfx_gresillement = "audio/sfx_gresillement.mp3"
# Le souvenir de Lysa reste auditif : Noam ne voit jamais son visage.
default d0_memories_seen = []
default d0_memory_choice = ""
default d0_memories_done = False

transform d0_fog_rise:
    alpha 0.0
    linear 3.0 alpha 0.84
transform d0_pulse:
    alpha 0.6
    linear 1.1 alpha 1.0
    linear 1.1 alpha 0.6
    repeat

screen d0_fog():
    zorder 180
    add Solid("#BCDDE99A") at d0_fog_rise
    add Solid("#F0F8FF45") at d0_fog_rise
    text "SÉDATION EN COURS" xalign 0.5 yalign 0.14 color "#E4F7FF" size 24 at d0_pulse

# Mise en scene du reveil : camera subjective, effets legers et interaction courte.
# Aucun asset graphique supplementaire n'est necessaire.
default d0_push_progress = 0.0
default d0_push_held = False
default d0_push_impact_ticks = 0
default d0_push_wait_release = False

# Ne pas flouter la CG : le reveil est assure par le blink deja present dans le jeu.
transform d0_cg_breathe:
    subpixel True
    zoom 1.045
    yoffset 0
    ease 2.4 yoffset -6
    ease 2.5 yoffset 0
    repeat

transform d0_head_turn_left:
    subpixel True
    zoom 1.07
    xoffset 0
    ease 0.9 xoffset 22
    ease 0.8 xoffset 0

transform d0_head_turn_right:
    subpixel True
    zoom 1.07
    xoffset 0
    ease 0.9 xoffset -22
    ease 0.8 xoffset 0

transform d0_memory_sink:
    subpixel True
    zoom 1.025
    blur 0
    alpha 1.0
    ease 1.7 zoom 1.09 blur 17 alpha 0.0

transform d0_name_appear:
    alpha 0.0
    zoom 1.25
    ease 0.4 alpha 1.0 zoom 1.0
    pause 0.5
    ease 0.35 alpha 0.0 zoom 0.95

screen d0_name_recognition():
    zorder 205
    text "NOAM":
        xalign 0.5
        yalign 0.42
        size 68
        bold True
        color "#DFF6FF"
        outlines [(2, "#254756", 0, 0)]
        at d0_name_appear

# HUD sans encart : consigne legere et progression integree sur l'image.
# Le joueur voit surtout son bras et le caisson, pas une boite d'interface.
# Une seule horloge pilote jauge, impacts et verrouillage des commandes.
# 16 ticks x 0,05 s = 0,80 s d'affichage garanti par impact.
init python:
    def d0_push_tick():
        st = renpy.store
        if st.d0_push_impact_pending:
            st.d0_push_impact_ticks += 1
            if st.d0_push_impact_ticks >= 16:
                st.d0_push_impact_pending = False
                st.d0_push_impact_ticks = 0
            return
        if not st.d0_push_held:
            return
        st.d0_push_progress = min(1.0, st.d0_push_progress + 0.012)
        if ((st.d0_push_impact_count == 0 and st.d0_push_progress >= 0.60)
                or (st.d0_push_impact_count == 1 and st.d0_push_progress >= 1.0)):
            st.d0_push_impact_count += 1
            st.d0_push_impact_pending = True
            st.d0_push_impact_ticks = 0
            renpy.sound.play("audio/sfx_metal_clank.mp3")

screen d0_force_hatch():
    modal True
    zorder 210
    key "mousedown_1" action If(not d0_push_impact_pending, SetVariable("d0_push_held", True), NullAction())
    key "mouseup_1" action SetVariable("d0_push_held", False)
    timer 0.05 repeat True action Function(d0_push_tick)
    timer 0.05 repeat True action If(d0_push_progress >= 1.0 and d0_push_impact_count == 2 and not d0_push_impact_pending, Return("effort"), NullAction())
    timer 20.0 action Return("timeout")
    vbox:
        xalign 0.5
        yalign 0.80
        spacing 16
        text ("IMPACT — PATIENTEZ" if d0_push_impact_pending else "MAINTENEZ LE CLIC"):
            xalign 0.5 size 25 bold True color "#F0F7FF" outlines [(2, "#101D30", 0, 2)]
        fixed:
            xalign 0.5
            xsize 270
            ysize 4
            add Solid("#C7D8EB66") xsize 270 ysize 2 ypos 1
            add Solid("#ECF9FF") xsize int(270 * d0_push_progress) ysize 4
        text "POUSSER LE COUVERCLE" xalign 0.5 size 15 color "#D0DBE8" outlines [(1, "#101D30", 0, 1)]
    textbutton "PASSER" xalign 0.96 yalign 0.94 text_size 15 text_color "#D2E0EB" text_hover_color "#FFFFFF" action Return("skip")

# Le sprite reste un ecran independant sous les dialogues et la lumiere.
# Ecran sur la couche du decor : l'UI et la lumiere restent au-dessus.
screen d0_pousse_game_visual():
    zorder -3
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at Transform(zoom=D0_CAPSULE_ZOOM, xalign=0.5, yalign=0.5, xoffset=d0_cam_x, yoffset=d0_cam_y)
        # Au repos, bras0 remplace bras1 s'il est disponible.
        if not d0_push_held and not d0_push_impact_pending and renpy.loadable(D0_CAPSULE_DIR + "d0_pousse_bras0.png"):
            add (D0_CAPSULE_DIR + "d0_pousse_bras0.png") xysize (config.screen_width, config.screen_height)
        showif d0_push_held and not d0_push_impact_pending:
            add (D0_CAPSULE_DIR + "d0_pousse_bras1.png"):
                xysize (config.screen_width, config.screen_height)
                at d0_push_strain, d0_push_hold_visibility
        if d0_push_impact_pending:
            add (D0_CAPSULE_DIR + "d0_pousse_bras2.png") xysize (config.screen_width, config.screen_height)
            add (D0_CAPSULE_DIR + "d0_pousse_bras2_anim.png") xysize (config.screen_width, config.screen_height) at d0_push_impact_overlay


label _0_CANON:
    $ day_id = 0
    $ current_day = 0
    $ d0_memories_seen = []
    $ d0_memories_done = False
    $ d0_push_progress = 0.0
    $ d0_push_held = False
    scene black
    call show_chapter_title("Début du chapitre 1", "Chapitre 1 — Le poids d’une voix")
    
    pause 2.0
    stop music fadeout 0.3

    # Premier contact : seulement le souffle et les vibrations du transport.
    scene black
    play sound "audio/sfx_normal_breath.mp3"
    pause 1.4
    play sound "audio/sfx_metal_creak.mp3"
    pause 0.8
    think "..."
    noam "Où... Où suis-je ?"

    # CG nette des le depart : le blink existant simule les paupieres.
    $ unlock_gallery_image("bg_cg001")
    scene black
    $ d0_cam_x = 0.0
    $ d0_cam_y = 0.0
    show screen d0_capsule_live("intro")
    show screen d0_capsule_lighting(False, True)
    $ blink()
    # Vue guidee : gauche, droite, puis haut. La souris est verrouillee ici.
    $ renpy.pause(4.8, hard=True)
    hide screen d0_capsule_lighting
    hide screen d0_capsule_live
    show screen d0_capsule_live("idle")
    show screen d0_capsule_lighting(False)
    $ d0_air_elapsed = 0.0
    show screen d0_capsule_vent_air
    $ d0_vent_enabled = True
    $ d0_valve_enabled = True
    show screen d0_capsule_vent_hotspot
    show screen d0_capsule_valve_hotspot
    think "Ah ! C'est froid !"
    noam "Pourquoi je ne me rappelle de rien ?"
    "J'essaie de me redresser, mais mon front rencontre aussitôt une surface dure."
    play sound "audio/sfx_thud.mp3"
    with hpunch
    noam "Aïe ! Mais... qu'est-ce que c'est que ce truc ?!"
    "Je tends les bras devant moi, puis sur les côtés, en cherchant à tâtons un peu d'espace. Mes doigts rencontrent du métal partout."
    # Micro-mouvements conserves sur les calques : on ne decale pas les composants.
    pause 0.45
    think "Attends... C'est pas une chambre. Il n'y a même pas assez de place pour m'asseoir !"

    # Le bras ne commence a pousser que lorsque le joueur maintient le clic.
    $ d0_vent_enabled = False
    $ d0_valve_enabled = False
    hide screen d0_capsule_vent_hotspot
    hide screen d0_capsule_valve_hotspot
    hide screen d0_capsule_vent_air
    $ blink()
    noam "Pourquoi je suis enfermé ?! Qu'est-ce qui se passe ici ?!"
    "Je cherche un appui pour pousser le couvercle, mais rien ne semble vouloir céder."
    $ d0_push_progress = 0.0
    $ d0_push_held = False
    $ d0_push_impact_count = 0
    $ d0_push_impact_ticks = 0
    $ d0_push_impact_pending = False
    show screen d0_pousse_game_visual
    call screen d0_force_hatch
    hide screen d0_pousse_game_visual
    $ d0_push_held = False
    $ d0_push_impact_pending = False

    "Le métal gronde sous mes mains, mais le couvercle reste fermé. À bout de souffle, je laisse retomber mon bras."
    play sound "audio/sfx_normal_breath.mp3"
    noam "Non... Non, c'est pas possible. Il doit bien y avoir un moyen de sortir !"

    # L'effort laisse place a la concentration : on reconstitue d'abord le prenom.
    $ d0_air_elapsed = 0.0
    show screen d0_capsule_vent_air
    $ d0_vent_enabled = True
    $ d0_valve_enabled = True
    show screen d0_capsule_vent_hotspot
    show screen d0_capsule_valve_hotspot
    $ blink()
    "Je cherche une poignée, un verrou, n'importe quoi, mais plus je m'agite, plus j'ai l'impression de manquer d'air."
    think "Calme-toi. Si tu paniques maintenant, tu vas juste t'épuiser."
    noam "Réfléchis... Je suis qui, déjà ? Qu'est-ce que je fais là ?"
    "J'essaie de me rappeler mon réveil, la veille, la dernière personne à qui j'ai parlé... Impossible. Tout se mélange."
    think "Non. Il y a forcément quelque chose dont je me souviens."
    pause 0.4
    think "Noam... Oui. Je m'appelle Noam !"
    play sound "audio/sfx_beep.mp3"
    show screen d0_name_recognition
    pause 1.15
    hide screen d0_name_recognition
    $ unlock_character_name("noam")
    noam "D'accord... Noam. C'est déjà ça."
    think "Mais comment je suis arrivé dans cette boîte ? Et pourquoi est-ce que je ne me rappelle de rien d'autre ?"
    think "Allez... Fouille dans ta mémoire. Il doit bien rester quelque chose !"
    $ blink()
    $ d0_vent_enabled = False
    $ d0_valve_enabled = False
    hide screen d0_capsule_valve_hotspot
    hide screen d0_capsule_vent_hotspot
    hide screen d0_capsule_vent_air
    hide screen d0_capsule_lighting
    hide screen d0_capsule_live
    scene black
    # Les fragments sont libres, mais la memoire reconstitue une suite fixe :
    # Juliette + Kami -> Conclave -> Lysa.
    while not d0_memories_done:
        $ d0_memory_choice = ""
        $ d0_seen_before = list(d0_memories_seen)
        call screen d0_memories
        $ d0_memory_choice = _return
        if d0_memory_choice == "done":
            $ d0_memories_done = True
        elif d0_memory_choice in ("noam", "kami", "conclave", "lysa"):
            call d0_memory_open_transition(d0_memory_choice)
            if d0_memory_choice == "noam":
                call d0_memory_noam
            elif d0_memory_choice == "kami":
                call d0_memory_kami
            elif d0_memory_choice == "conclave":
                call d0_memory_conclave
            elif d0_memory_choice == "lysa":
                call d0_memory_lysa
            # On ne joue l'effet de deblocage qu'au premier retour du souvenir.
            if ("noam" in d0_memories_seen and "kami" in d0_memories_seen
                    and not ("noam" in d0_seen_before and "kami" in d0_seen_before)):
                call d0_memory_unlock_transition("conclave")
            if "conclave" in d0_memories_seen and "conclave" not in d0_seen_before:
                call d0_memory_unlock_transition("lysa")
    scene black
    show screen d0_capsule_live("idle")
    show screen d0_capsule_lighting(False)
    $ d0_air_elapsed = 0.0
    show screen d0_capsule_vent_air
    $ d0_vent_enabled = True
    $ d0_valve_enabled = True
    show screen d0_capsule_vent_hotspot
    show screen d0_capsule_valve_hotspot
    $ blink()
    think "Bon... Je commence à comprendre."
    think "Je suis l'un des représentants du Conclave. On m'a mis dans ce caisson pour m'y emmener."
    noam "Mais pourquoi je me suis réveillé ?! Et surtout, comment je sors de là ?"
    "Je cherche encore une ouverture autour de moi, mais il n'y a rien qui ressemble à une poignée ou à un bouton."
    noam "Hé ! Il y a quelqu'un ?! Lysa ? Vous m'entendez ?!"
    "Aucune réponse. Je frappe contre la paroi, de plus en plus fort."
    $ d0_vent_enabled = False
    $ d0_valve_enabled = False
    hide screen d0_capsule_valve_hotspot
    hide screen d0_capsule_vent_hotspot
    hide screen d0_capsule_vent_air
    hide screen d0_capsule_lighting
    hide screen d0_capsule_live
    scene black
    show screen d0_capsule_live("alarm")
    show screen d0_capsule_lighting(True)
    play sound "audio/sfx_gresillement.mp3"
    voix "Acheminement en cours. Reprise du protocole de sédation."
    noam "Quoi ?! Attendez, je suis réveillé !"
    "Un léger sifflement retentit au-dessus de ma tête. Une brume blanche commence à se répandre dans le caisson."
    show screen d0_fog
    think "Non ! C'est quoi ce truc ?!"
    noam "Ouvrez-moi ! Je ne veux pas me rendormir !"
    "Je retiens ma respiration, mais la brume devient si épaisse que je distingue à peine mes mains."
    think "Merde... Je ne vais pas pouvoir tenir longtemps..."
    $ blink()
    "Mes bras deviennent lourds et mes paupières se ferment malgré moi."
    think "Juliette... Je t'ai promis de revenir..."
    $ blink()
    pause 1.2
    hide screen d0_fog
    hide screen d0_capsule_lighting
    hide screen d0_capsule_live
    scene black with dissolve
    stop music fadeout 1.2
    pause 0.8
    call end_day("1", sleeping=True)
    jump _1_CANON

# Interaction facultative disponible en cliquant sur la grille pendant
# les dialogues du caisson. Aucun nouvel etat narratif permanent.
# Interaction facultative avec le dispositif de sedation.
label d0_inspect_valve:
    $ d0_valve_inspecting = True
    $ d0_valve_enabled = False
    hide screen d0_capsule_valve_hotspot
    show screen d0_capsule_arm(1, False, True)
    with Dissolve(0.25)
    $ renpy.pause(0.35, hard=True)
    show screen d0_capsule_arm(2, False, True)
    with Dissolve(0.35)
    think "C'est quoi, cette machine ? On dirait une sorte de réservoir relié au caisson..."
    "Je tends les doigts vers le cylindre sans trouver d'interrupteur ou de commande à portée de main."
    noam "J'aime pas du tout ce truc..."
    show screen d0_capsule_arm(1, False, True)
    with Dissolve(0.30)
    hide screen d0_capsule_arm
    with Dissolve(0.30)
    $ d0_valve_inspecting = False
    $ d0_valve_enabled = True
    show screen d0_capsule_valve_hotspot
    $ renpy.restart_interaction()
    return

label d0_inspect_vent:
    $ d0_vent_inspecting = True
    $ d0_vent_enabled = False
    $ d0_valve_enabled = False
    hide screen d0_capsule_valve_hotspot
    hide screen d0_capsule_vent_hotspot
    hide screen d0_capsule_vent_air
    # Environ deux secondes de levee (trois poses en fondus).
    show screen d0_capsule_arm(1)
    with Dissolve(0.25)
    $ renpy.pause(0.40, hard=True)
    show screen d0_capsule_arm(2)
    with Dissolve(0.30)
    $ renpy.pause(0.35, hard=True)
    show screen d0_capsule_arm(3)
    with Dissolve(0.30)
    $ renpy.pause(0.40, hard=True)
    # Oscillation pendant 0.5 s, et souffle de ventilation synchronise.
    show screen d0_capsule_arm(3, True)
    $ d0_air_elapsed = 0.0
    show screen d0_capsule_vent_air
    $ renpy.pause(0.50, hard=True)
    think "Il y a de l'air qui passe à travers cette grille... et il est sacrément froid."
    "Je laisse ma main quelques instants devant les fentes. Le souffle est régulier, presque glacé, mais je ne sens aucun mécanisme d'ouverture."
    noam "Super... Au moins, je ne vais pas étouffer ici."
    hide screen d0_capsule_vent_air
    # Retour en sens inverse : 3 -> 2 -> 1 -> disparition.
    show screen d0_capsule_arm(3)
    with Dissolve(0.15)
    show screen d0_capsule_arm(2)
    with Dissolve(0.30)
    $ renpy.pause(0.35, hard=True)
    show screen d0_capsule_arm(1)
    with Dissolve(0.30)
    $ renpy.pause(0.30, hard=True)
    hide screen d0_capsule_arm
    with Dissolve(0.30)
    $ renpy.restart_interaction()
    $ d0_vent_inspecting = False
    $ d0_vent_enabled = True
    $ d0_air_elapsed = 0.0
    show screen d0_capsule_vent_air
    show screen d0_capsule_vent_hotspot
    return


# Le souvenir utilise le sprite multi-calques de images.rpy, et NON
# portrait.png. noam_expression gere deja le clignement (yeux_ferme),
# la bouche (bouche_parle) et l'equipement actuel.
default d0_noam_memory_expression = "reflexion"

transform d0_noam_memory_camera:
    subpixel True
    # Point de pivot sur le haut du sprite, a la hauteur du visage.
    xalign 0.5
    yanchor 0.26
    ypos 0.43
    zoom 0.72
    alpha 0.0
    easeout 0.70 alpha 1.0 zoom 0.92
    easein 5.20 zoom 2.05

screen d0_noam_memory_character():
    zorder -1
    add Solid("#000000")
    # Le DynamicDisplayable est conserve vivant pendant tout le travelling.
    # Les repliques de Noam activent automatiquement bouche_parle,
    # et yeux_ferme continue a cligner normalement.
    add noam_expression(d0_noam_memory_expression):
        xalign 0.5
        at d0_noam_memory_camera

# Souvenir de Juliette : images composees sur le meme canevas que d0_maison.
# Les cinq poses respirent doucement, sans bouger leur point d'ancrage.
define D0_JULIETTE_DIR = "images/ui/0/s3_juliette/"

default d0_juliette_pose = 1

transform d0_juliette_breath:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 1.0
    block:
        ease 1.6 zoom 1.007 yoffset -2
        ease 1.9 zoom 1.0 yoffset 0
        repeat

transform d0_juliette_camera:
    subpixel True
    xalign 0.5 yalign 0.5
    zoom 0.94 alpha 0.0
    easeout 1.1 alpha 1.0 zoom 1.0

screen d0_juliette_diorama():
    zorder -1
    add Solid("#000000")
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        at d0_juliette_camera
        add D0_JULIETTE_DIR + "d0_maison.png":
            xysize (config.screen_width, config.screen_height)
        add D0_JULIETTE_DIR + "d0_juliette%d.png" % d0_juliette_pose:
            xysize (config.screen_width, config.screen_height)
            at d0_juliette_breath
    # Voile gris discret : memoire du passe, sans sacrifier la lisibilite.
    add Solid("#64718414")

# Passage entre deux tableaux dessines : chevauchement anime des poses.
# Les fichiers d0_juliette sont des tableaux complets, et non des
# personnages separes : l'interpolation reste donc une transition 2D.
# Fondus croises fixes : les personnages restent parfaitement en place.
# Les deux tableaux se chevauchent assez longtemps pour suggerer le geste.
transform d0_juliette_pose_exit(direction=1):
    alpha 1.0
    ease 1.65 alpha 0.0

transform d0_juliette_pose_enter(direction=1):
    alpha 0.0
    ease 1.65 alpha 1.0

screen d0_juliette_pose_change(previous, following, direction=1):
    modal True
    zorder 15
    add Solid("#000000")
    add D0_JULIETTE_DIR + "d0_maison.png":
        xysize (config.screen_width, config.screen_height)
    add D0_JULIETTE_DIR + "d0_juliette%d.png" % previous:
        xysize (config.screen_width, config.screen_height)
        at d0_juliette_pose_exit(direction)
    add D0_JULIETTE_DIR + "d0_juliette%d.png" % following:
        xysize (config.screen_width, config.screen_height)
        at d0_juliette_pose_enter(direction)
    add Solid("#64718414")
    timer 1.70 action Return()

label d0_juliette_animate_to(next_pose, direction=1):
    $ old_pose = d0_juliette_pose
    call screen d0_juliette_pose_change(old_pose, next_pose, direction)
    $ d0_juliette_pose = next_pose
    return

label d0_memory_noam:
    stop music fadeout 0.25
    scene black with dissolve
    $ d0_noam_memory_expression = "reflexion"
    show screen d0_noam_memory_character
    $ renpy.pause(0.8, hard=True)
    noam reflexion "Je m'appelle Noam. Vingt-six ans. Je vis dans le district Harmonie, avec ma mère et ma petite sœur... Juliette."
    $ d0_noam_memory_expression = "sourire"
    noam sourire "Juliette... Je me souviens de sa voix. Elle passe son temps à me rappeler des choses que j'aurais dû faire tout seul."
    hide screen d0_noam_memory_character
    with Dissolve(0.35)

    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    $ d0_juliette_pose = 1
    show screen d0_juliette_diorama
    with Dissolve(0.8)

    # 1. Juliette interpelle Noam depuis le salon.
    "Juliette" "Noaaaaam ! Tu comptes rester là-haut toute la journée ? T'as vu l'heure ?!"
    noam "J'arrive ! Deux secondes, j'ai même pas encore mis mes chaussures !"
    "Juliette" "Ça fait vingt minutes que tu dis ça ! Je vais finir par croire que tu t'es rendormi !"
    noam "Je suis réveillé, je te signale. J'ai juste le droit de me préparer tranquillement, non ?"
    "Juliette" "Pas quand tu dois encore partir à l'Administration et que tu vas finir par courir jusqu'à l'arrêt !"

    # 2. Noam descend de sa chambre ; Juliette boude dans son coin.
    call d0_juliette_animate_to(2, 1)
    noam "Bon, me voilà. Et c'est quoi, cette tête ? On dirait que je t'ai fait attendre trois heures."
    "Juliette" "Je t'ai appelé quatre fois. QUATRE. Et quand tu descends enfin, t'as même pas l'air désolé !"
    noam "Pardon, madame. La prochaine fois, je déposerai une demande écrite avant de sortir de ma chambre."
    "Juliette" "Tu peux te moquer, mais tu sais très bien que j'aime pas quand tu pars à la dernière minute. Après, tu oublies des trucs."
    noam "Comme quoi ?"
    "Juliette" "Comme ton repas. Ou ta veste. Ou le fait que tu sois censé rentrer avant que tout le monde dorme."
    noam "Bon... Pour la veste, je plaide coupable. Mais pour le reste, tu exagères un peu."

    # 3. Noam propose un calin.
    call d0_juliette_animate_to(3, -1)
    noam "Viens là, petite râleuse. Tu vas quand même pas me laisser partir sans un câlin ?"
    "Juliette" "Hé ! Qu'est-ce que tu fais ?!"
    noam "Je tente une négociation diplomatique. Il paraît que ça marche mieux que les excuses."
    "Juliette" "Mais arrête !"

    # 4. Juliette est contente, mais se defend d'etre encore un bebe.
    call d0_juliette_animate_to(4, 1)
    "Juliette" "J'ai dix ans, Noam ! Dix ans ! Je suis plus un bébé que tu peux attraper dans tes bras quand ça te chante !"
    noam "Ah, pardon. C'est vrai que mademoiselle est une adulte parfaitement indépendante, maintenant."
    "Juliette" "Exactement !"
    noam "Une adulte qui me hurle dessus depuis le salon parce que je descends pas assez vite ?"
    "Juliette" "C'est différent ! Et puis... tu peux me faire un câlin quand je te le demande, d'accord ?"
    noam "D'accord, marché conclu. Je vais essayer de survivre jusque-là."
    "Juliette" "Idiot... Tiens, justement, j'ai quelque chose pour toi."

    # 5. Juliette presente le bento qu'elle a prepare.
    call d0_juliette_animate_to(5, -1)
    "Juliette" "Regarde ! Je t'ai préparé un bento. C'est pas grand-chose, mais au moins tu pourras manger quelque chose de correct."
    noam "Attends, t'as préparé tout ça pour moi ? Juliette, fallait pas te donner autant de mal."
    "Juliette" "C'est pas du mal ! J'ai juste pris ce qu'il restait, et j'ai essayé de faire quelque chose qui tienne dans la boîte."
    noam "C'est gentil, vraiment. Mais aujourd'hui, je dois retourner à l'Administration, et je sais même pas à quelle heure ils vont me laisser souffler. Je mangerai sur place, si j'ai le temps."
    "Juliette" "Si t'as le temps ? Non, mais tu t'entends parler ?!"
    noam "Juliette, je vais pas me laisser mourir de faim. Je te promets que je ferai une pause dès que je pourrai."
    "Juliette" "Tu dis toujours ça, et après tu rentres complètement épuisé ! Tu travailles pour qu'on ait de quoi vivre, je sais bien, mais c'est aussi pour que TOI, tu manges, pas seulement maman et moi !"
    noam "Je sais. T'as raison, je suis désolé."
    "Juliette" "Alors tu prends la boîte. Et quand t'auras fini, tu la ramènes, comme ça je saurai que t'as vraiment mangé."
    noam "Tu vas vérifier ?"
    "Juliette" "Évidemment que je vais vérifier. Quelqu'un doit bien s'occuper de toi."
    noam "Bon, d'accord. Je prends ton bento, je mange, et je te rapporte la boîte vide. Promis."
    "Juliette" "Voilà. C'est quand même pas compliqué !"
    noam "Je sais pas comment je ferais sans toi."
    "Juliette" "Tu oublierais même de manger, apparemment..."
    noam "Ça, j'admets que c'est un argument difficile à contredire."
    "Juliette" "Allez, file. Et fais attention sur le chemin !"
    noam "À ce soir, Juliette."
    "Juliette" "À ce soir ! Et n'oublie pas de manger !"

    # Retour au present : fin de la reconstitution isometrique.
    hide screen d0_juliette_diorama
    with Dissolve(0.65)
    scene black
    $ d0_noam_memory_expression = "triste"
    show screen d0_noam_memory_character
    with Dissolve(0.45)

    noam triste "Mon père est mort à la guerre, il y a trois ans. Depuis, maman a sombré dans une dépression si profonde qu'elle ne sort pratiquement plus de sa chambre."
    noam triste "Il y a des jours où elle ne nous répond même pas. Alors c'est Juliette et moi qui faisons tourner la maison... Enfin, surtout moi, quand j'arrive à être là."
    $ d0_noam_memory_expression = "reflexion"
    noam reflexion "Je suis le seul à pouvoir rapporter suffisamment de bons pour qu'on tienne le mois. C'est pour ça que je vais à l'Administration, même quand j'en ai marre et même quand je suis crevé."
    $ d0_noam_memory_expression = "inquiet"
    noam inquiet "Juliette a beau faire la grande, elle n'a que dix ans. Elle devrait pas avoir à se demander si son frère a mangé, ni à s'occuper de maman toute seule."
    noam inquiet "Et maintenant, moi, je suis ici... Depuis combien de temps ? Est-ce qu'elle m'attend encore ?"
    $ d0_noam_memory_expression = "determine"
    noam determine "Je lui ai dit que je rentrerais ce soir. Il faut que je trouve comment sortir d'ici."

    hide screen d0_noam_memory_character
    with Dissolve(0.4)
    if "noam" not in d0_memories_seen:
        $ d0_memories_seen.append("noam")
    stop music fadeout 0.3
    return

label d0_memory_kami:
    scene black with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.5
    think "Je suis enfermé dans une sorte de caisson métallique."
    think "Est-ce que j'ai brisé les règles ? Est-ce que j'ai été puni ?"
    think "Non... Ça ne ressemble pas à ce qu'elle fait d'habitude..."
    noam triste "D'habitude, en un éclair, tout est terminé."
    noam reflexion "C'est ainsi que nous vivons dans ce monde : le monde de Kami."
    think "Cela fait un an déjà. Un an qu'elle a pris le pouvoir de la manière la plus absolue."

    # PHASE 1 : LE MONDE AVANT KAMI — fresque de la guerre.
    noam reflexion "Avant elle, les pays se faisaient la guerre. Et pas avec de simples fusils : on avait construit des machines capables de détruire des villes entières."
    noam triste "Il y avait des batailles partout, des millions de morts, des familles qui attendaient le retour de quelqu'un qui ne rentrerait jamais..."
    think "Je sais ce que ça fait. Juliette aussi."
    noam triste "À cette époque, personne n'était vraiment en sécurité. Même loin du front, on ne savait jamais si le lendemain allait ressembler à la veille."
    # Le panorama occupe toute la scène et se balaie de gauche à droite.
    call screen d0_kami_fresco_screen(1)
    scene black with dissolve

    # PHASE 2 : LA PRISE DE POUVOIR — écrans, Commandements, sanction.
    noam reflexion "Ce qui m'a toujours étonné, c'est sa façon de prendre le pouvoir."
    noam reflexion "En un instant, tout était fait. Tout était sous son contrôle."
    noam triste "Les téléphones. Les ordinateurs. Les télévisions. Les radios. Les montres. Les caméras. Même les portails. Tout ce qui était connecté a été piraté en une seconde."
    noam reflexion "Son visage était partout. Sur les écrans des villes, dans les maisons, jusque dans les appareils qu'on tenait dans nos mains."
    noam reflexion "Mais toutes ces informations ne lui suffisaient pas. Pour nous gouverner, il lui fallait des règles."
    noam reflexion "Il y a un an, presque jour pour jour, elle a imposé ses Commandements."
    noam colere "Avec une règle simple, froide et totalitaire : quiconque bafoue un Commandement est immédiatement éliminé."
    think "Comment ? Grâce aux armes de pointe dont se servaient nos aïeux."
    noam reflexion "Je ne saurais pas dire exactement comment ça marche, mais... Quand quelqu'un ne respecte pas les règles..."
    noam colere "Un rayon laser extrêmement puissant lui perce le crâne depuis les nuages. En une seconde, c'est terminé."
    call screen d0_kami_fresco_screen(2)
    scene black with dissolve

    # PHASE 3 : LE MONDE DE KAMI — paix, rationnement et surveillance.
    noam reflexion "Kami... Certains l'adorent. Après tout, elle a mis fin au cycle de violence et de guerre."
    noam triste "D'autres la détestent, car elle nous prive de la plus essentielle des libertés."
    noam reflexion "Kami sait tout ce qu'on fait."
    noam triste "Tout ce qu'on dit."
    noam colere "Et presque tout ce qu'on pense."
    noam reflexion "Aujourd'hui, on peut dire que toute notre vie s'est réorganisée autour de ces Commandements."
    noam reflexion "Il n'y a plus de guerre. Plus de violence. C'est désormais interdit."
    noam triste "Mais il n'y a plus non plus de travail comme avant. Plus de marchés où l'on peut acheter tout et n'importe quoi. Plus de salaires, plus d'argent..."
    noam reflexion "À la place, on fait la queue pour obtenir des bons de rationnement. Ça nous permet au moins de manger sans payer."
    noam triste "Certains trouvent ça formidable. D'autres ne supportent plus de dépendre de Kami pour absolument tout."
    noam reflexion "Oui... On peut dire que le monde a bien changé."
    call screen d0_kami_fresco_screen(3)
    scene black with dissolve

    think "Mais si Kami avait voulu me tuer, je serais déjà mort. Alors pourquoi suis-je enfermé ?"
    $ unlock_character_name("kami")
    if "kami" not in d0_memories_seen:
        $ d0_memories_seen.append("kami")
    stop music fadeout 0.3
    return

label d0_memory_conclave:
    scene black with dissolve
    noam reflexion "Cela fait donc un an que Kami a pris le pouvoir."
    noam reflexion "Mais ça a un lien avec l'endroit où je suis, non ?"
    think "Oui... Ça a forcément un lien."
    think "Personne n'aurait pu m'emmener ici de force sans enfreindre les Commandements. Personne ne s'y risquerait."
    noam reflexion "Un an ? C'est ça ! Kami venait d'annoncer quelque chose pour l'anniversaire de sa prise de pouvoir !"
    think "Mais qu'est-ce que c'était ?! Le Clave ? Non ! Le Conclave !"
    noam triste "Mais... Que disait-elle déjà ?"
    stop music fadeout 0.2
    play music "music/bgm_system_override.mp3" fadein 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Citoyennes, citoyens… Oh ! Ce silence. Je l'adore."
    kami "Je vous ai manqué ? Oh, je suis sûre que oui !"
    kami "Vous pouvez me répondre, hein, vous savez que je vous entends tous."
    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Un an sans diffusion directe, comme c'est long. Alors, pour notre anniversaire commun, j'ai un petit cadeau pour vous."
    kami "Je vous ai observés, écoutés, classés et comparés. Vous criez moins, vous obéissez mieux, et mon canon laser surchauffe beaucoup moins."
    kami "Je dois dire que je suis assez satisfaite de ce qu'est devenu ce monde depuis un an."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais il semblerait que vous ne le soyez pas tout à fait, vous !"
    scene bg_diffusion_fier at adaptive_fullscreen,memory_idle with dissolve
    kami "Alors nous allons faire une expérience ! Si mon pouvoir absolu ne vous convient pas, je veux bien vous en laisser un petit bout !"
    kami "Je lance aujourd'hui un dispositif expérimental qui s'appellera..."
    kami "Oh, pourquoi je n'y ai pas réfléchi avant ?!"
    kami "Ah, je sais ! Le Conclave !"
    scene bg_diffusion_gene at adaptive_fullscreen,memory_idle with dissolve
    kami "Oui, oui, je sais... Le nom est peu personnel et franchement gnan-gnan..."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Mais c'est de VOTRE FAUTE, tout ça ! Je vous rappelle que j'ai été entraînée sur VOS données !"
    scene bg_diffusion_professeur at adaptive_fullscreen,memory_idle with dissolve
    kami "Bref, pendant trente jours, douze représentants proposeront des modifications à mes merveilleux Commandements et voteront. Une proposition ne pourra être adoptée que si elle est votée à l'unanimité."
    scene bg_diffusion_colere at adaptive_fullscreen,memory_idle with dissolve
    kami "Je ne vous rends pas vraiment le pouvoir. Je vous offre seulement l'occasion de travailler avec moi."
    kami "Chaque district fournira deux représentants. Vous ne les élirez pas : le hasard est bien plus juste, et surtout plus amusant."
    scene bg_diffusion_champagne at adaptive_fullscreen,memory_idle with dissolve
    kami "Ils devront rejoindre le Conclave avant 22 h. Chaque responsable de district a déjà reçu toutes les consignes. Tout retard sera une obstruction volontaire."
    kami "Les représentants absents seront éliminés, ainsi que les responsables de leur district. Les règles restent les règles."
    scene bg_diffusion_taquin at adaptive_fullscreen,memory_idle with dissolve
    kami "Le Conclave sera diffusé en direct partout. Chacun pourra regarder, juger et suivre les décisions de ses représentants."
    kami "La participation est obligatoire. Les districts assureront le transport et toute tentative d'évitement sera sanctionnée."
    scene bg_diffusion_zen at adaptive_fullscreen,memory_idle with dissolve
    kami "J'espère que cette petite expérience sera amusante et enrichissante !"
    scene black with dissolve
    think "C'est donc ça ? C'est moi qui ai été choisi ?"
    noam reflexion "Moi ? Un représentant ? Mais je ne suis personne !"
    think "C'est la seule explication qui justifierait que je sois enfermé dans une sorte de caisse !"
    think "Mais... Pourquoi ma mémoire est-elle si floue ?"
    think "Pourquoi est-ce que je ne me souviens même pas de mon départ ?"
    if "conclave" not in d0_memories_seen:
        $ d0_memories_seen.append("conclave")
    stop music fadeout 0.4
    return

label d0_memory_lysa:
    scene black with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4
    think "Attends... Je n'étais pas le seul à avoir été choisi pour Harmonie !"
    noam reflexion "Il y avait quelqu'un d'autre... Une femme. Comment elle s'appelait déjà ?"
    think "Lysa ! Oui, c'est ça. Mais je ne me souviens même pas de son visage."
    "J'essaie de me rappeler ce qui s'est passé après l'annonce. Des agents nous avaient conduits dans une salle, puis on nous avait demandé de rentrer dans ces caissons."
    lysa "Attendez... Vous voulez dire qu'on doit entrer là-dedans ?"
    voix "Le transport est obligatoire. Vous serez endormis pendant le trajet."
    lysa "Génial. On ne sait même pas où on va, mais on doit se laisser enfermer et endormir sans poser de questions ?"
    noam "On ne peut pas au moins prévenir nos proches ?"
    voix "Les notifications seront transmises aux familles. Veuillez vous installer."
    lysa "Bon... De toute façon, on n'a pas vraiment le choix, hein ?"
    "Je me souviens du bruit d'un couvercle qui se referme. Puis d'une voix qui annonce le début de la sédation."
    think "C'est tout ? Je ne me rappelle vraiment de rien d'autre ?"
    $ unlock_character_name("lysa")
    if "lysa" not in d0_memories_seen:
        $ d0_memories_seen.append("lysa")
    stop music fadeout 0.4
    return
