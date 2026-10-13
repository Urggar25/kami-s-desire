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
# Les souvenirs ne sont pas un menu : ils flottent comme des pensées dans le noir.
# Interface 100 % Ren'Py, sans image externe ni rectangles de boutons.
transform d0_orb_drift_a:
    subpixel True
    yoffset 0 rotate -2
    ease 2.7 yoffset -16 rotate 2
    ease 2.9 yoffset 8 rotate -1
    ease 2.6 yoffset 0 rotate -2
    repeat

transform d0_orb_drift_b:
    subpixel True
    yoffset 4 rotate 2
    ease 3.2 yoffset 17 rotate -2
    ease 2.6 yoffset -12 rotate 1
    ease 2.9 yoffset 4 rotate 2
    repeat

transform d0_orb_drift_c:
    subpixel True
    yoffset -5 rotate -1
    ease 3.6 yoffset 13 rotate 2
    ease 3.1 yoffset -9 rotate -2
    ease 3.3 yoffset -5 rotate -1
    repeat

# Nuage peint sur fond transparent, partage par les quatre souvenirs.
# Aucune glyphe Unicode n'est utilisee pour les formes ou decorations.
transform d0_cloud_breathe:
    subpixel True
    zoom 0.98
    ease 2.6 zoom 1.025
    ease 2.8 zoom 0.98
    repeat

transform d0_pulse:
    alpha 0.6
    linear 1.1 alpha 1.0
    linear 1.1 alpha 0.6
    repeat

screen d0_thought_orb(key, title, hint, xp, yp, diameter, drift):
    $ unlocked = key in ("noam", "kami") or (key == "conclave" and "noam" in d0_memories_seen and "kami" in d0_memories_seen) or (key == "lysa" and "conclave" in d0_memories_seen)
    $ already = key in d0_memories_seen
    $ caption = "SOUVENIR RETROUVÉ" if already else (hint if unlocked else "SOUVENIR ENFOUI")
    $ cloud_path = "gui/day0/thought_cloud.png"
    $ cloud_tint = "#60717B" if already else ("#D8F5FF" if unlocked else "#394956")
    $ cloud_opacity = 0.48 if already else (0.95 if unlocked else 0.31)
    fixed:
        xpos xp
        ypos yp
        xsize diameter
        ysize diameter
        at drift
        # Le nuage est une vraie texture PNG avec transparence.
        button:
            xalign 0.5
            yalign 0.5
            xsize diameter
            ysize diameter
            padding (0, 0)
            background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix(cloud_tint), alpha=cloud_opacity)
            hover_background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix("#FFFFFF"), alpha=1.0)
            insensitive_background Transform(cloud_path, xysize=(diameter, diameter), matrixcolor=TintMatrix("#3B4A59"), alpha=0.30)
            focus_mask True
            sensitive unlocked
            action [SetVariable("d0_memory_choice", key), Return()]
            at d0_cloud_breathe
            vbox:
                xalign 0.5
                yalign 0.5
                xmaximum int(diameter * 0.73)
                spacing 8
                text title:
                    xalign 0.5
                    text_align 0.5
                    size (25 if diameter >= 260 else 22)
                    bold True
                    color ("#123249" if unlocked and not already else "#C1CED8")
                text caption:
                    xalign 0.5
                    text_align 0.5
                    xmaximum int(diameter * 0.68)
                    size 14
                    color ("#27526B" if unlocked and not already else "#8195A5")

screen d0_memories():
    modal True
    zorder 220
    add Solid("#030A13F2")
    text "REMÉMORATION":
        xalign 0.5
        ypos 0.065
        size 26
        color "#BCE7F6"
        kerning 4
    text "Des souvenirs flottent à la surface de ma mémoire...":
        xalign 0.5
        ypos 0.111
        size 16
        color "#7B9BAC"
    use d0_thought_orb("noam", "JULIETTE", "Ce qui m'attend chez moi", 0.13, 0.20, 320, d0_orb_drift_a)
    use d0_thought_orb("kami", "KAMI", "Les Commandements", 0.66, 0.18, 330, d0_orb_drift_b)
    use d0_thought_orb("conclave", "CONCLAVE", "L'annonce", 0.34, 0.51, 310, d0_orb_drift_c)
    use d0_thought_orb("lysa", "UNE VOIX", "Un dernier souvenir", 0.77, 0.62, 270, d0_orb_drift_a)
    if "lysa" in d0_memories_seen:
        textbutton "REVENIR AU PRÉSENT":
            xalign 0.5
            yalign 0.945
            text_size 23
            text_color "#CBEEFA"
            text_hover_color "#FFFFFF"
            action [SetVariable("d0_memories_done", True), Return()]
    else:
        text "CHOISISSEZ UN SOUVENIR":
            xalign 0.5
            yalign 0.955
            size 16
            color "#91B7C7"

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
    while not d0_memories_done:
        $ d0_memory_choice = ""
        call screen d0_memories
        if d0_memory_choice == "noam":
            call d0_memory_noam
        elif d0_memory_choice == "kami":
            call d0_memory_kami
        elif d0_memory_choice == "conclave":
            call d0_memory_conclave
        elif d0_memory_choice == "lysa":
            call d0_memory_lysa
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


label d0_memory_noam:
    stop music fadeout 0.2
    scene black with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.6
    noam reflexion "Je suis une personne ordinaire. Je n'ai aucun talent particulier, aucun ami haut placé. Je suis... juste moi. Et c'est d'ailleurs très bien ainsi."
    noam sourire "Rien qui mérite vraiment qu'on s'y attarde..."
    noam reflexion "Je vis dans une famille traumatisée par la guerre."
    noam triste "Mon père est mort il y a trois ans, sur le front. Ma mère, elle, est complètement à la ramasse depuis."
    noam sourire "Mon seul rayon de soleil, c'est ma sœur. Juliette."
    noam taquin "Elle a dix ans de moins que moi. Elle est gentille, parfois un peu trop... Elle ne mérite pas tout ça."
    noam reflexion "On essaie de vivre tant bien que mal dans ce qu'on appelle désormais le district Harmonie."
    noam reflexion "Quand je le peux, je participe à de longues réunions techniques et administratives."
    noam triste "Soi-disant, elles aident les gens, débloquent des dossiers et, d'après ce qu'on nous dit, sauvent parfois des vies."
    noam reflexion "Ce « travail », que je fais depuis un an, me permet de gagner des bons supplémentaires."
    noam sourire "C'est grâce à ça qu'on peut dire qu'on survit plutôt bien."
    noam triste "Beaucoup sont bien plus à plaindre que nous..."
    think "Mais tout ça... Ça ne me dit pas ce que je fais ici !"
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
    noam reflexion "Kami... Certains l'adorent. Après tout, elle a mis fin au cycle de violence et de guerre."
    noam triste "D'autres la détestent, car elle nous prive de la plus essentielle des libertés."
    noam reflexion "Ce qui m'a toujours étonné, c'est sa façon de prendre le pouvoir."
    noam reflexion "En un instant, tout était fait. Tout était sous son contrôle."
    noam triste "Les téléphones. Les ordinateurs. Les télévisions. Les radios. Les montres. Les caméras. Même les portails. Tout ce qui était connecté a été piraté en une seconde."
    noam reflexion "Kami sait tout ce qu'on fait."
    noam triste "Tout ce qu'on dit."
    noam colere "Et presque tout ce qu'on pense."
    noam reflexion "Mais toutes ces informations ne lui suffisaient pas. Pour nous gouverner, il lui fallait des règles."
    noam reflexion "Il y a un an, presque jour pour jour, elle a imposé ses Commandements."
    noam colere "Avec une règle simple, froide et totalitaire : quiconque bafoue un Commandement est immédiatement éliminé."
    think "Comment ? Grâce aux armes de pointe dont se servaient nos aïeux."
    noam reflexion "Je ne saurais pas dire exactement comment ça marche, mais... Quand quelqu'un ne respecte pas les règles..."
    noam colere "Un rayon laser extrêmement puissant lui perce le crâne depuis les nuages. En une seconde, c'est terminé."
    noam reflexion "Aujourd'hui, on peut dire que toute notre vie s'est réorganisée autour de ces Commandements."
    noam reflexion "Il n'y a plus de guerre. Plus de violence. C'est désormais interdit."
    noam triste "Mais il n'y a plus non plus de travail comme avant. Plus de marchés où l'on peut acheter tout et n'importe quoi. Plus de salaires, plus d'argent..."
    noam reflexion "Oui... On peut dire que le monde a bien changé."
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
