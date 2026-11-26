# =============================================================================
# JOUR 20 — Route 0_1_1
# Réécriture complète
# =============================================================================

default j20_iris_qte_success = False
default j20_knife_choice = None
default j20_kael_depart_choice = None


# Mise en scène spécifique à la révélation de Kael au J20.
# Le zoom est appliqué au sprite seul afin de garder la salle des Goumi lisible.
transform j20_kael_approach(z=1.0):
    # Le point d'ancrage est placé autour du visage de Kael.
    # Ainsi le visage reste dans le cadre pendant que le zoom
    # fait progressivement sortir le bas du corps par le bas.
    xpos 0.5
    xanchor 0.5
    ypos 0.27
    yanchor 0.17
    zoom z


label _20_0_1_1_0_REVEIL:

    $ cafeteria_food_level = "null"
    $ current_period = "Matin"
    $ current_day = 20
    # À compter du J20, la Mara visible dans cette route est son double.
    # Le sprite conserve les bras/expressions habituels, seul le corps change.
    $ mara_dg_body_locked = True
    $ noam_has_juliette_drawing = False

    $ unlock_gallery_image("bg_cg040")
    scene bg_cg040 at adaptive_fullscreen
    $ flashlight_on(pattern=0)
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.0
    $ danger_on()

    "Je reste devant la table, la lampe braquée sur le visage de Mara."
    "Ma main tremble. J'essaie de la tenir avec l'autre, sans résultat."

    noam peur "Mara...?"

    "Elle ne bouge pas."
    think "Vérifie son pouls."
    "Je fais un pas, puis je m'arrête."

    "Un bruit métallique résonne dans le conduit derrière moi."

    noam peur "Qui est là ?" id j20_reveil_silence_noam

    "Je recule, puis je cours."

    scene bg_conduit_reseau at adaptive_fullscreen with vpunch
    $ flashlight_on(pattern=4)

    "Je remonte dans le réseau avec la lampe dans une main et le couteau dans l'autre. Mon épaule cogne contre la tôle. Je continue."
    think "Va chercher les autres."

    $ flashlight_off()
    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je sors de la grille trop vite et tombe à genoux dans ma chambre."

    "Je regarde le couteau dans ma main."

    think "Pose-le."
    "Je me relève avec."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_200
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je traverse le dortoir. Une porte s'ouvre sur mon passage ; je ne m'arrête pas."

    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    scene bg_cafeteria at adaptive_fullscreen with vpunch

    stop music fadeout 0.5
    play music "audio/music/bgm_tense_meeting.mp3" fadein 1.0

    "La porte frappe le mur."

    $ showGroup([
        ("noam", "desespoir", 0.05),
        ("lysa", "surpris", 0.18),
        ("ryn", "surpris", 0.31),
        ("tomas", "surpris", 0.44),
        ("elen", "surpris", 0.57),
        ("iris", "surpris", 0.70),
        ("kael", "surpris", 0.83),
        ("sael", "surpris", 0.96),
    ])

    call cutin("noam", expr="desespoir", color="#ff2e55") from _call_kd_cutin_20_noam
    noam desespoir "{shout}MARA EST MORTE !{/shout}"

    "Plus personne ne parle."
    call reactions([("ryn", "surpris"), ("elen", "peur"), ("iris", "inquiet")]) from _call_kd_reactions_20_mara

    ryn surpris "Quoi ?" id j20_cafeteria_ryn_quoi

    noam desespoir "Dans la salle des Goumi. Sur la table de maintenance. Elle bougeait plus."

    elen peur "Attends... Mara ?"

    noam colere "Oui, Mara !"

    iris inquiet "Noam. Le couteau."

    "Je baisse les yeux."

    noam inquiet "Je l'avais dans les conduits. C'est tout."

    lysa inquiet "Pose-le. Après tu recommences depuis le début."

    noam colere "J'ai pas besoin de recommencer ! Venez voir !"

    tomas inquiet "Tu as vérifié son pouls ?"

    noam desaccord "Non. J'ai paniqué. Mais elle respirait pas, Tomas."

    sael mefiant "Ça suffit pour qu'on vérifie."

    "Des pas arrivent derrière moi avant que quelqu'un puisse répondre."

    mara neutre "Vérifier quoi ?"

    $ horror_audio_cut(duration=0.52, restore_volume=0.70)
    $ unlock_gallery_image("bg_cg044")
    $ hideGroup()
    scene bg_cg044 at adaptive_fullscreen with signal_stutter
    $ cam_move(fx=0.67, fy=0.44, z=1.13, t=5.5)

    "Je me retourne."
    $ doppelganger_reveal(screamer=False, duration=0.86, restore_volume=0.70)

    "Mara est dans l'encadrement de la porte."

    mara neutre "Pourquoi vous me regardez tous comme ça ?"

    noam panne "..."

    mara mefiant "Noam ?"

    "Je recule d'un pas quand elle s'approche."

    noam peur "Ne viens pas plus près."

    mara colere "Pardon ?"

    noam peur "Reste là."

    mara colere "Mais qu'est-ce que t'as encore foutu ?"

    noam desespoir "Je viens de te voir morte."

    "Elle me fixe sans répondre. Pendant une seconde, même Mara ne trouve rien à dire."

    $ cam_reset(t=0.25)
    $ danger_off()
    scene bg_cafeteria at adaptive_fullscreen with memory_rip
    $ showGroup([
        ("noam", "desespoir", 0.28),
        ("mara", "stress", 0.72),
    ])

    mara stress "Je crois que t'as vraiment besoin de dormir."

    noam colere "Je sais ce que j'ai vu !"

    mara colere "Et moi je sais que je suis devant toi, là ! Tu veux que je fasse quoi de plus, que je me pince pour te rassurer ?"

    noam panne "Non..."

    $ investigation_add("mara_vivante")

    ryn desaccord "Noam. Elle est là."

    noam colere "Je la regarde ! C'est justement pour ça que je vous demande de venir avec moi ! Il y avait un corps sur cette table, et ce corps avait son visage !"

    "Iris fixe Mara."
    iris reflexion "Attends. Tu dis que t'as vu son corps ? Pas quelqu'un qui lui ressemble ?"
    noam colere "Son visage. Ses cheveux. Tout."
    iris inquiet "Et elle était vraiment morte ? T'as vérifié ?"
    noam agace "Elle était froide."
    iris reflexion "Tu l'as touchée, alors ?"
    noam hesitation "Je... non. Pas vraiment."
    iris inquiet "Alors comment tu—"

    noam colere "Non !"

    noam colere "Me dites pas que j'ai rêvé. Venez voir la table. Après, vous pourrez décider que je suis fou."

    mara colere "Moi, je vais nulle part avec toi tant que t'as ce couteau."

    noam agace "Très bien."

    "Je le pose lentement sur une table, manche tourné vers l'extérieur."

    noam determine "Maintenant, qui vient ?"

    "Un silence passe."

    iris reflexion "J'y vais."

    kael inquietude "Moi aussi."

    ryn determine "Je peux venir si—"

    iris desaccord "Non. Kael connaît les conduits, moi je garde un œil sur Noam. À trois, ça suffit."

    noam colere "J'ai pas besoin d'être surveillé."

    iris blase "Tu as passé la nuit avec un couteau dans une bouche d'aération. On en reparlera."

    mara stress "Et si y'a rien ?"

    "Je tourne la tête vers elle."

    noam desespoir "Elle était là."

    $ hideGroup()

    jump _20_0_1_1_SALLE_GOUMI


label _20_0_1_1_SALLE_GOUMI:

    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.5
    $ flashlight_on()

    $ showGroup([
        ("noam", "determine", 0.18),
        ("iris", "inquiet", 0.50),
        ("kael", "inquietude", 0.82),
    ])

    "Iris rampe derrière moi. Kael ferme la marche."

    iris inquiet "T'es sûr du chemin ?"

    noam determine "Oui. Encore deux bifurcations."

    kael inquietude "Tu étais venu jusque-là tout seul cette nuit ?"

    noam agace "Oui."

    kael doute "Avec ton couteau."

    noam colere "Je sais à quoi ça ressemble. J'entendais quelqu'un, personne me croyait... J'y suis allé."

    kael doute "D'accord."

    "Quelques minutes plus tard, je reconnais enfin la grille qui donne sur la salle."

    noam determine "C'est ici."

    "Je descends le premier sans attendre les autres."

    $ hideGroup()
    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "determine", 0.18),
        ("iris", "inquiet", 0.50),
        ("kael", "inquietude", 0.82),
    ])

    "Je saute dans la salle et braque la lampe vers la table."

    pause 1.0

    noam panne "..."

    "{cps=10}Elle est vide.{/cps}"
    with flash_white

    "Je regarde la table d'à côté. Puis le sol."

    noam peur "Non..."

    iris inquiet "Noam ?"

    noam peur "Elle était là."

    "Je m'approche de la table et passe ma main sur la surface métallique."

    noam colere "Là ! Sur le dos, la tête de ce côté !"

    kael inquietude "Il n'y a rien."

    noam colere "Merci, j'avais remarqué."

    "Je regarde sous la table, derrière les deux Goumi, puis dans les espaces de rangement ouverts sous l'établi."

    iris reflexion "Noam, arrête. Si quelqu'un a déplacé un corps, il l'a pas rangé dans un tiroir."

    noam colere "Donc tu admets que quelqu'un a pu le déplacer ?"

    iris agace "Je dis que fouiller au hasard sert à rien."

    noam desaccord "Vous pensez que j'ai tout inventé."

    iris inquiet "Je pense surtout que tu dors presque plus et que t'es terrifié. Ça veut pas dire que tu mens."

    noam colere "Arrêtez tous avec ça ! J'étais fatigué, oui. J'avais peur, oui. Ça ne transforme pas une table vide en cadavre !"

    kael inquietude "Maintenant, elle est vide."

    "Je me retourne brutalement vers lui."

    noam colere "Tu veux dire quoi par là ?"

    kael doute "Qu'on est venus vérifier. Et qu'il n'y a personne."

    noam colere "Tu crois que je mens ?"

    kael doute "Je crois que tu l'as vue. Mais avec M16, ça ne prouve pas qu'elle était là."

    "Je ne réponds pas."

    noam desespoir "Je l'ai vue..."

    iris triste "Je sais."

    noam colere "Ne me parle pas comme si j'étais malade."

    iris inquiet "Alors arrête de nous parler comme si on était contre toi."

    "Je fais un pas vers elle, plus par frustration que par intention réelle, et mon pied heurte quelque chose au sol."

    play sound sfx_drop

    "Le couteau glisse sur le métal."

    "Je baisse les yeux."

    noam surpris "..." id j20_couteau_silence_noam

    iris peur "Ne le ramasse pas."

    noam desaccord "Je le ramasse, c'est tout."

    iris determine "Non. Tu le laisses par terre et on remonte."

    noam colere "Tu crois vraiment que je vais vous attaquer ?"

    iris determine "Là, je crois que tu réfléchis plus. Recule."

    noam colere "J'en ai marre qu'on décide de tout à ma place !"

    "Je me penche malgré elle."

    iris colere "Noam, ne fais pas ça."

    "Je referme ma main sur le manche et me redresse."

    noam agace "Voilà. Maintenant on remonte."

    "Iris ne bouge pas."

label _20_0_1_1_IRIS_CONFRONTATION:

    # Point de reprise de la roadmap : juste avant le choix qui sépare les routes.
    scene bg_salle_goumi_cachee at adaptive_fullscreen
    $ showGroup([
        ("noam", "inquiet", 0.22),
        ("iris", "determine", 0.52),
        ("kael", "inquietude", 0.82),
    ])

    iris determine "Pose-le."

    "Je regarde Iris, puis le couteau."

    "Je pourrais simplement ouvrir la main."

    "Ça devrait être facile."
    menu (screen="critical_choice", noam_expr="hesitation", cc_targets={"Lâcher le couteau":{"label":"_20_0_1_1_LACHER_COUTEAU","pack":"doppelganger_routes"},"Garder le couteau":{"label":"_20_0_1_1_GARDER_COUTEAU"}}):
        "Que faire du couteau ?"

        "Lâcher le couteau":
            $ j20_knife_choice = "drop"
            jump _20_0_1_1_LACHER_COUTEAU

        "Garder le couteau":
            $ j20_knife_choice = "keep"
            jump _20_0_1_1_GARDER_COUTEAU


label _20_0_1_1_GARDER_COUTEAU:
    $ j20_knife_choice = "keep"
    scene bg_salle_goumi_cachee at adaptive_fullscreen
    $ showGroup([
        ("noam", "colere", 0.22),
        ("iris", "colere", 0.52),
        ("kael", "inquietude", 0.82),
    ])
    $ danger_on()

    noam colere "Non. Je le garde."

    iris colere "Noam..."

    noam colere "Je vais attaquer personne. Je veux juste pas rester désarmé pendant que quelqu'un se balade dans les murs."

    "Elle avance d'un pas."

    noam inquiet "Iris, reste où tu es."

    iris determine "Pose-le et je recule."

    noam colere "Arrête de me parler comme à un débile !"

    "Je lève le bras, simplement pour lui faire signe de reculer."

    "Je n'ai pas le temps de terminer mon geste."

    $ flashlight_off()
    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch

    "Iris attrape mon poignet, tourne sur elle-même et me fait perdre l'équilibre avec une facilité qui me laisse à peine le temps de comprendre ce qu'elle vient de faire."

    $ unlock_gallery_image("bg_cg052")
    scene bg_cg052 at adaptive_fullscreen with flash_white

    noam surpris "Qu'est-ce que—?!"

    $ j20_iris_qte_success = False
    python:
        j20_iris_trace_steps = [
            {"path_type": "curve_left", "time_limit": 1.20, "wait_time": 0.28, "tolerance": 30, "max_errors": 1, "anchor_x": 760, "anchor_y": 620, "start_radius": 70},
            {"path_type": "s_curve", "time_limit": 1.05, "wait_time": 0.24, "tolerance": 27, "max_errors": 1, "anchor_x": 1120, "anchor_y": 620, "start_radius": 66},
            {"path_type": "curve_right", "time_limit": 0.92, "wait_time": 0.20, "tolerance": 24, "max_errors": 1, "anchor_x": 820, "anchor_y": 620, "start_radius": 62},
            {"path_type": "arc", "time_limit": 0.80, "wait_time": 0.16, "tolerance": 22, "max_errors": 1, "anchor_x": 1020, "anchor_y": 650, "start_radius": 58},
        ]

    call trace_qte_sequence(
        j20_iris_trace_steps,
        "bg_cg052",
        start_zoom=1.0,
        zoom_step=0.065,
        show_tutorial=False
    ) from _call_trace_qte_sequence_j20_iris
    $ j20_iris_trace_result = _return

    if j20_iris_trace_result["success"]:
        jump _20_0_1_1_IRIS_QTE_REUSSITE

    jump _20_0_1_1_IRIS_QTE_ECHEC


label _20_0_1_1_LACHER_COUTEAU:
    if not kd_dlc_unlocked("doppelganger_routes"):
        call screen kd_dlc_locked_notice
        jump _20_0_1_1_IRIS_CONFRONTATION

    $ danger_off()

    "Je garde le manche serré une seconde de plus, puis j'ouvre la main."

    play sound sfx_drop

    "Le couteau tombe entre nous et glisse sur le sol métallique."

    noam fatigue "Voilà."

    "Iris ne répond pas."

    "Elle regarde ma main vide."

    noam inquiet "Ça va ?"

    iris colere "Non."

    noam surpris "..."

    iris colere "Non, ça va pas, espèce d'abruti."

    noam inquiet "Iris..."

    "Elle s'approche."

    iris fatigue "Bouge pas."

    noam hesitation "Je bouge pas."

    "À la place, ses bras passent autour de moi."

    noam surpris "..."

    "Pendant une seconde, je reste complètement raide."

    "Iris serre plus fort."

    noam gene "Euh..."

    iris triste "Ferme-la deux secondes."

    "Alors je ferme la bouche."

    iris fatigue "J'ai cru que t'allais vraiment faire une connerie."

    noam inquiet "Je voulais pas te faire de mal."

    iris fatigue "Je sais."

    "Elle répond tout de suite."

    iris triste "C'est justement ça le pire."

    noam fatigue "..."

    iris triste "Je savais que tu voulais pas. Mais je savais plus ce que t'allais faire."

    "Je baisse les yeux."

    noam fatigue "Moi non plus."

    "Kael détourne la tête."

    noam fatigue "Désolé."

    iris fatigue "Ouais."

    noam hesitation "C'est tout ?"

    iris blase "Tu voulais quoi ? Un discours ?"

    "Un rire nerveux m'échappe."

    iris colere "T'as intérêt à pas me refaire un truc pareil."

    noam fatigue "Je vais essayer."

    iris colere "Non. Tu vas pas essayer."

    noam fatigue "D'accord. Je vais pas recommencer."

    "Elle finit par me lâcher et recule juste assez pour me regarder."

    iris inquiet "Et maintenant on remonte."

    "Je hoche la tête."

    "Mon regard tombe une dernière fois sur le couteau."

    "Il est resté au milieu de la salle."

    "Je pourrais le reprendre."

    "Je ne le fais pas."

    kael inquietude "On devrait y aller."

    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(pattern=2)

    "Iris avance devant. Kael ferme la marche. Personne ne parle."

    think "J'ai vu Mara sur cette table."

    think "Je l'ai vue."

    think "Mais Mara était dans la cafétéria. Vivante."

    think "M16."

    "Je serre les dents."

    think "Le corps était faux ? Le souvenir ? Ou Mara..."

    "Je bloque la pensée avant même de la terminer."

    iris inquiet "Noam ?"

    noam fatigue "Ça va."

    iris blase "Tu sais que t'es vraiment mauvais pour mentir ?"

    noam fatigue "Je réfléchis."

    iris blase "Justement."

    "Elle ralentit pour rester à ma hauteur."

    iris fatigue "T'es pas obligé de trouver une réponse maintenant."

    noam inquiet "Demain on part."

    iris fatigue "Je sais."

    noam inquiet "Si le corps était réel, demain c'est trop tard."

    "Iris ouvre la bouche, mais ne répond pas."

    "Cette fois, même elle n'a rien à me proposer."

    scene bg_chambre at adaptive_fullscreen with dissolve
    $ flashlight_off()

    "Nous ressortons enfin du conduit dans ma chambre."

    "Je m'assois un instant sur le bord du lit, surtout parce que mes jambes en ont marre de me porter."

    $ showGroup([
        ("noam", "fatigue", 0.22),
        ("iris", "inquiet", 0.52),
        ("kael", "doute", 0.82),
    ])

    iris inquiet "Je vais prévenir les autres qu'on a rien trouvé."

    noam desaccord "Dis pas que j'ai inventé le reste."

    iris colere "J'ai pas dit ça."

    noam fatigue "Je sais."

    iris fatigue "Je vais juste leur dire qu'il n'y avait plus de corps. C'est la seule chose qu'on sait."

    "Elle hésite une seconde avant de sortir."

    iris determine "Et tu restes ici."

    noam blase "Oui, maman."

    iris colere "Je suis sérieuse."

    noam fatigue "Moi aussi. Enfin... oui. Je reste là."

    "Elle me lance encore un regard méfiant, puis ouvre la porte."

    iris reflexion "Kael ?"

    kael doute "J'arrive."

    "Iris sort."

    play sound sfx_door

    "Kael, lui, ne bouge pas tout de suite."

    noam fatigue "Tu peux y aller."

    kael doute "Ouais."

    "Il regarde la grille ouverte derrière nous."

    kael doute "Je voulais juste..."

    "Il s'arrête."

    noam reflexion "Quoi ?"

    call play_stat_dialogue("j20") from _call_play_stat_dialogue_19

    kael doute "Non, rien."

    noam reflexion "Kael."

    "Il inspire doucement par le nez."

    kael inquietude "Je peux te poser une question ?"

    noam calme "Vas-y."

    kael doute "C'est un peu... enfin, c'est pas vraiment lié à tout ça."

    noam blase "Vu la journée, ça changera pas grand-chose."

    "Il esquisse un sourire, mais il disparaît presque aussitôt."

    kael inquietude "Si demain la navette arrive..."

    "Il marque une pause."

    kael doute "Et que quelqu'un resterait coincé ici..."

    "Ses yeux quittent les miens."

    kael doute "Tu monterais quand même dedans ?"

    noam surpris "..."

    noam reflexion "Pourquoi tu me demandes ça ?"

    kael inquietude "J'en sais rien."

    "Il passe une main derrière sa nuque."

    kael doute "Je pensais au départ. À demain. Et puis..."

    "Il s'interrompt encore."

    kael doute "Laisse tomber. C'était une question con."

    noam reflexion "Non."

    "Il relève les yeux."

    noam reflexion "C'est juste... précis."

    kael inquietude "Ouais."

    "Un silence passe."

    kael inquietude "Alors ?"

label _20_0_1_1_KAEL_QUESTION:

    # Second point de bifurcation majeur de la route "lâcher le couteau".
    # Le joueur choisit sans savoir ce que Kael cherche réellement à résoudre.
    $ j20_knife_choice = "drop"
    scene bg_chambre at adaptive_fullscreen
    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("kael", "doute", 0.70),
    ])
    menu (screen="critical_choice", noam_expr="reflexion", cc_targets={"Je monte dans la navette.":{"label":"_20_0_1_1_KAEL_PARTIR","pack":"doppelganger_routes"},"Je reste s'il y a encore une chance de le sortir.":{"label":"_20_0_1_1_KAEL_RESTER","pack":"doppelganger_routes"}}):
        "Si demain la navette arrive... mais que quelqu'un reste coincé ici ?"

        "Je monte dans la navette.":
            $ j20_kael_depart_choice = "leave"
            jump _20_0_1_1_KAEL_PARTIR

        "Je reste s'il y a encore une chance de le sortir.":
            $ j20_kael_depart_choice = "stay"
            jump _20_0_1_1_KAEL_RESTER


label _20_0_1_1_KAEL_PARTIR:
    if not kd_dlc_unlocked("doppelganger_routes"):
        call screen kd_dlc_locked_notice
        jump _20_0_1_1_IRIS_CONFRONTATION


    noam reflexion "Je monte."

    kael surpris "..."

    noam hesitation "Enfin... si j'ai vraiment aucun moyen de le sortir."

    kael doute "Même en sachant qu'il reste ici ?"

    noam reflexion "Rester avec lui ne changera rien. On sera juste deux à être coincés."

    "Il regarde le sol quelques secondes."

    kael inquietude "Ouais..."

    kael doute "Je vois."

    noam inquiet "T'avais quelqu'un en tête ?"

    kael surpris "Non."

    "La réponse sort un peu trop vite."

    kael doute "Non, personne. Je... je me demandais juste."

    noam reflexion "D'accord."

    "Il hoche la tête, comme s'il venait de prendre une décision qui n'a rien à voir avec moi."

    jump _20_0_1_1_LACHER_FIN_JOURNEE


label _20_0_1_1_KAEL_RESTER:
    if not kd_dlc_unlocked("doppelganger_routes"):
        call screen kd_dlc_locked_notice
        jump _20_0_1_1_IRIS_CONFRONTATION


    noam reflexion "Je reste."

    kael surpris "Tu resterais ?"

    noam calme "S'il reste une chance de le sortir, oui."

    kael inquietude "Même si tu risques de rater la navette ?"

    noam hesitation "Je vais pas rester ici pour toujours juste pour faire le héros. Mais partir alors que je peux encore faire quelque chose ? Non."

    "Kael baisse légèrement les yeux."

    kael doute "Même si c'est pas... quelqu'un que tu connais vraiment ?"

    noam reflexion "Ça change quoi ?"

    kael doute "..."

    noam calme "S'il est coincé et que je peux l'aider, j'essaie. Si c'est impossible... c'est autre chose."

    "Kael reste silencieux longtemps."

    kael inquietude "D'accord."

    noam surpris "D'accord ?"

    kael doute "Ouais. C'est juste..."

    "Il cherche ses mots."

    kael doute "Je voulais savoir."

    noam inquiet "Tu me fais un peu flipper, là."

    kael sourire "Désolé."

    "Son sourire est petit. Presque gêné."

    "Mais son regard, lui, reste ailleurs."

    jump _20_0_1_1_LACHER_FIN_JOURNEE


label _20_0_1_1_LACHER_FIN_JOURNEE:

    $ current_period = "Soir"

    "Kael finit par rejoindre Iris dans le couloir."

    play sound sfx_door

    $ hideGroup()

    "La porte se referme. Je reste assis sur le lit, les mains posées entre mes genoux."

    scene black with dissolve
    pause 0.6

    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Des heures plus tard, je n'ai toujours rien compris."
    think "Mara est vivante. J'ai vu son corps. Les deux ne peuvent pas être vrais."
    think "Sauf si M16 a encore touché à ma mémoire."

    noam fatigue "Putain."

    "Je me laisse tomber sur le dos. Demain, la navette doit arriver."
    "La question de Kael me revient."

    if j20_kael_depart_choice == "leave":
        think "Ça fera juste deux personnes coincées au lieu d'une."
    else:
        think "S'il reste une chance de le sortir..."

    think "Pourquoi il voulait savoir ça ?"

    stop music fadeout 1.5

    call show_chapter_title("Fin du chapitre 6", "Chapitre 6 — Derrière les murs") from _call_show_chapter_title_22
    call end_day("21") from _call_j20_dropknife_end_day_21

    if j20_kael_depart_choice == "stay":
        jump _21_0_1_1_0_0_REVEIL

    jump _21_0_1_1_0_1_REVEIL


label _20_0_1_1_IRIS_QTE_ECHEC:
    if not kd_dlc_unlocked("doppelganger_routes"):
        call screen kd_dlc_qte_retry
        jump _20_0_1_1_GARDER_COUTEAU


    $ unlock_gallery_image("bg_cg047")
    scene bg_cg047 at adaptive_fullscreen with flash_white

    "Le couteau tombe. J'essaie de me dégager, mais Iris garde mon bras bloqué contre la table."

    iris colere "Arrête de bouger !"

    noam colere "Lâche-moi !"

    iris colere "Je te lâche dès que tu te calmes !"

    noam colere "Je suis calme !"

    kael inquietude "Non. Là, t'es pas calme."

    "Je force pour me relever. Iris change d'appui et me déséquilibre encore."
    "Son poing arrive sur le côté."

    scene bg_cg047 at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 0.95
    call impact_fx("critical", direction="left") from _call_impact_fx_13

    "Un choc sec me frappe à la tempe."

    "Mes jambes se dérobent immédiatement."

    noam panne "..."

    "J'entends Iris m'appeler, puis Kael lui répondre quelque chose que je ne comprends déjà plus."

    "Tout devient noir avant même que je touche complètement le sol."

    scene black with dissolve
    $ danger_off()

    stop music fadeout 1.0

    pause 2.0

    jump _20_0_1_1_INFIRMERIE
    # Durée : 1m15


label _20_0_1_1_IRIS_QTE_REUSSITE:

    $ j20_iris_qte_success = True

    "Je baisse l'épaule au moment où Iris verrouille mon bras. Sa prise glisse."
    "Elle revient aussitôt. J'évite son coude et récupère mon poignet."

    iris colere "Arrête de bouger !"

    noam colere "Arrête de m'attaquer !"

    "Elle tente encore de saisir mon bras. Je recule contre la table, le couteau toujours serré dans ma main."

    noam inquiet "Iris, stop !"

    iris colere "Alors lâche-le !"

    noam inquiet "Je vais le poser ! Arrête de me sauter dessus !"

    iris colere "Tu dis ça depuis tout à l'heure !"

    "Elle attrape mon avant-bras à deux mains."

    noam colere "Lâche-moi !"

    iris colere "Lâche le couteau !"

    "Je tire mon bras vers moi. Elle tire dans l'autre sens."

    "Pendant une seconde, personne ne gagne."

    kael inquietude "Ça suffit !"

    "Iris change brusquement d'appui."

    "Son pied accroche le bord de la table."

    iris surpris "Merde—"

    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch
    play sound sfx_drop

    "Son poids part vers moi. Quelque chose s'arrête net."

    pause 0.6

    $ unlock_gallery_image("bg_cg053")
    scene bg_cg053 at adaptive_fullscreen with flash_white

    "Iris ne bouge plus."

    noam panne "..."

    "Sa main est toujours refermée sur mon poignet."

    "Je baisse les yeux."

    "Le couteau est entre nous."

    "Une partie de la lame a disparu dans son ventre."

    noam peur "Iris..."

    "Elle baisse les yeux à son tour."

    iris panne "..."

    iris fatigue "T'es... sérieux... ?"

    noam desespoir "J'ai pas fait exprès. Putain, Iris, j'ai pas fait exprès !"

    "Je lâche immédiatement le manche."

    iris peur "Non !"

    "Sa voix me coupe."

    iris peur "Touche pas... laisse-le."

    noam peur "D'accord. Je touche pas."

    "Ses jambes commencent à lâcher."

    "Je la rattrape comme je peux et l'accompagne au sol."

    noam desespoir "Kael ! Va chercher Sael ! Maintenant !"

    "Aucune réponse."

    # La CG reste importante pour la blessure d'Iris, puis on revient
    # explicitement dans la salle pour isoler Kael à l'écran.
    scene bg_salle_goumi_cachee at adaptive_fullscreen with memory_rip
    $ hideGroup()
    hide iris
    hide noam
    hide kael

    $ renpy.music.set_volume(0.34, delay=1.0, channel="music")

    show kael neutre at j20_kael_approach(0.96) with dissolve
    pause 1.0

    show kael doute at j20_kael_approach(1.02) with dissolve
    pause 1.0

    show kael calme at j20_kael_approach(1.08) with dissolve
    pause 1.0

    show kael sourire at j20_kael_approach(1.14) with dissolve

    noam colere "KAEL !"

    show kael sourire at j20_kael_approach(1.23) with Dissolve(0.25)

    "Il ne répond pas. Il me regarde seulement, parfaitement immobile, comme s'il attendait que je comprenne tout seul."

    noam colere "Mais bouge, putain !"

    show kael taquin at j20_kael_approach(1.34) with Dissolve(0.22)

    "Ses lèvres remontent un peu plus."

    noam panne "..."

    show kael joie at j20_kael_approach(1.46) with Dissolve(0.20)

    "Je connais le sourire de Kael."

    "Celui-là, non."

    noam inquiet "Kael... ?"

    show kael sourire at j20_kael_approach(1.60) with Dissolve(0.18)

    "Il fait un pas vers nous."

    noam colere "Qu'est-ce que tu fous ? Va chercher quelqu'un !"

    show kael taquin at j20_kael_approach(1.76) with Dissolve(0.16)

    "Encore un pas."

    iris fatigue "Kael..."

    show kael joie at j20_kael_approach(1.94) with Dissolve(0.14)

    "J'essaie de me relever sans lâcher Iris."

    noam inquiet "Reste où tu es."

    show kael sourire at j20_kael_approach(2.15) with Dissolve(0.12)

    "Son visage prend maintenant presque tout mon champ de vision."

    $ renpy.music.set_volume(0.08, delay=0.45, channel="music")
    pause 0.35

    show kael taquin at j20_kael_approach(2.38) with Dissolve(0.10)
    pause 0.55

    $ horror_audio_cut(duration=0.30, restore_volume=0.0)
    $ doppelganger_reveal(screamer=True, duration=0.88, restore_volume=0.0)

    noam peur "..."

    noam peur "T'es pas Kael."

    hide kael
    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 0.95

    "Il se jette sur moi."

    "Je lève le bras par réflexe."

    play sound "audio/sfx_thud.mp3" volume 1.0
    call impact_fx("hard", direction="right") from _call_impact_fx_14

    "Il frappe mon poignet contre le bord de la table."

    play sound sfx_drop

    "Le couteau tombe quelque part au sol."

    noam colere "DÉGAGE !"
    call kd_vn_reaction("noam", "colere", "#ff9c55")

    play sound "audio/sfx_thud.mp3" volume 0.90
    call impact_fx("light", direction="left") from _call_impact_fx_15

    "Je lui donne un coup d'épaule et réussis à le repousser."

    "Iris essaie de se redresser derrière moi."

    iris colere "Espèce de..."

    "Kael pivote vers elle."

    noam peur "IRIS, NON !"

    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch

    "Elle essaie de le frapper."

    "Son bras part trop lentement."

    play sound "audio/sfx_thud.mp3" volume 1.0
    call impact_fx("brutal", direction="right", blood="screen") from _call_impact_fx_16

    "Kael lui donne un coup sec au visage."

    play sound "audio/sfx_drop.mp3" volume 0.72

    "Iris retombe contre le sol."

    noam desespoir "IRIS !"

    "Je me jette sur lui."

    "Je n'arrive même pas jusqu'à son épaule."

    play sound "audio/sfx_thud.mp3" volume 1.0
    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    call impact_fx("critical", direction="left") from _call_impact_fx_17

    "Quelque chose me frappe derrière la tête."

    play sound "audio/sfx_tinnitus.wav" volume 0.48

    "Mes jambes disparaissent."

    noam panne "..."

    "Je tombe."

    "La dernière chose que je vois, c'est Kael qui se penche vers moi."

    show kael sourire at j20_kael_approach(1.38) with creep_diss

    "Il sourit encore."

    pause 0.5

    scene black with suffocation_cut
    stop music fadeout 0.25
    $ renpy.music.set_volume(1.0, delay=0.0, channel="music")

    pause 1.5

    # L'édition gratuite se termine sans dévoiler le laboratoire ni l'origine
    # des doubles. Le joueur peut prolonger l'épilogue avec le pack installé.
    scene black with suffocation_cut
    stop music fadeout 0.25
    $ renpy.music.set_volume(1.0, delay=0.0, channel="music")
    $ danger_off()
    pause 1.5

    "Dans le noir, un bruit métallique résonne tout près de moi."
    "Il y a quelqu'un d'autre dans cette pièce."
    "J'essaie de bouger, mais je n'y arrive plus."
    "Puis j'entends une voix."
    "Elle est bizarrement familière."
    "Et après ça, plus rien."

    call screen kd_ending_reached("Derrière la grille", "FIN GRATUITE // JOUR 20", button_text=("CONTINUER" if kd_dlc_unlocked("doppelganger_routes") else None))
    $ _ending_screen_closed = _return

    if kd_dlc_unlocked("doppelganger_routes"):
        call screen kd_dlc_extend_j20
        if _return:
            jump kd_dlc_la_peau_des_autres
    return


label _20_0_1_1_INFIRMERIE:

    $ current_period = "Après-midi"

    scene bg_infirmerie at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    "Je reviens à moi avec une douleur sourde sur le côté de la tête. Pendant quelques secondes, je reste complètement immobile, incapable de remettre les événements dans l'ordre."

    "Puis j'ouvre les yeux et reconnais le plafond de l'infirmerie."

    think "Iris."

    "Je tente de porter une main à ma tempe, mais mon bras ne bouge presque pas."

    noam inquiet "Qu'est-ce que..."

    "Une sangle maintient mon poignet au bord du lit. L'autre bras est attaché de la même manière, et mes chevilles le sont aussi."

    noam colere "Non, mais vous êtes sérieux ?!"

    "Je tire une première fois dessus. Rien ne cède."

    noam colere "Hé ! Il y a quelqu'un ?!"

    "Aucune réponse."

    noam colere "Sael ?! Iris ?!"

    "Je recommence, plus fort."

    noam colere "Détachez-moi !"

    "Ma voix traverse la pièce et s'écrase contre la porte fermée. Personne ne vient."

    "Je me débats encore quelques secondes avant que la douleur dans ma tête m'oblige à arrêter."

    noam fatigue "Putain..."

    "Je reste allongé, essoufflé, à fixer le plafond."

    think "Le corps n'était plus là."

    "C'est la seule chose qui compte."

    think "Quelqu'un l'a déplacé."

    "Je ferme les yeux et revois la salle exactement comme cette nuit : la lampe qui passe sur les Goumi, la table, les cheveux de Mara, son visage."

    think "Je ne peux pas avoir inventé tout ça."

    "Mais plus les minutes passent, plus une autre idée revient malgré moi."

    think "M16."

    noam desaccord "Non..."

    "Je secoue légèrement la tête et le regrette immédiatement."

    think "Pas encore."

    "Je refuse de recommencer à douter de chacun de mes souvenirs dès que quelque chose ne colle pas."

    "Je tire de nouveau sur les sangles."

    noam colere "Quelqu'un peut venir, bordel ?!"

    "Toujours rien." id j20_infirmerie_toujours_rien

    menu:
        "Rester immobile ou examiner la pièce ?"

        "Balayer l'infirmerie du regard":
            $ _j20_infirmerie_points = []
            jump _20_0_1_1_OBSERVER_INFIRMERIE

        "Garder des forces":
            think "Tirer au hasard ne fera que resserrer les sangles. Je dois attendre une occasion."
            jump _20_0_1_1_ATTENTE_INFIRMERIE


label _20_0_1_1_OBSERVER_INFIRMERIE:

    menu:
        "Que puis-je atteindre du regard ?"

        "Le moniteur" if "moniteur" not in _j20_infirmerie_points:
            $ _j20_infirmerie_points.append("moniteur")
            "Le moniteur derrière mon épaule affiche mon rythme cardiaque, mais une seconde courbe reste figée sous la mienne. Elle porte la même heure de réveil."
            think "Pourquoi il y a une seconde courbe ?"
            jump _20_0_1_1_OBSERVER_INFIRMERIE

        "Les sangles" if "sangles" not in _j20_infirmerie_points:
            $ _j20_infirmerie_points.append("sangles")
            "Je cesse de tirer et suis la sangle jusqu'au bord du lit. La boucle n'est pas médicale : quelqu'un l'a remplacée par une fermeture de caisse, serrée à la main."
            think "Ce n'est pas un protocole automatique. Quelqu'un a pris le temps de m'attacher."
            jump _20_0_1_1_OBSERVER_INFIRMERIE

        "La porte" if "porte" not in _j20_infirmerie_points:
            $ _j20_infirmerie_points.append("porte")
            "Sous la porte, une ombre coupe brièvement la lumière du couloir. Elle s'arrête lorsque je retiens ma respiration, puis repart sans entrer."
            noam inquiet "Je sais que vous êtes là."
            "Les pas ne répondent pas."
            jump _20_0_1_1_OBSERVER_INFIRMERIE

        "Arrêter d'observer" if len(_j20_infirmerie_points) >= 1:
            jump _20_0_1_1_ATTENTE_INFIRMERIE


label _20_0_1_1_ATTENTE_INFIRMERIE:

    "J'appelle jusqu'à avoir la gorge sèche, puis je me tais."
    "Chaque fois que je ferme les yeux, je revois Mara sur la table."

    scene bg_infirmerie at adaptive_fullscreen with dissolve
    pause 1.2

    jump _20_0_1_1_LYSA_SAEL


label _20_0_1_1_LYSA_SAEL:

    $ current_period = "Soir"

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    play sound sfx_door

    "La porte s'ouvre enfin."

    $ showGroup([
        ("noam", "fatigue", 0.26),
        ("lysa", "blase", 0.62),
        ("sael", "neutre", 0.82),
    ])

    lysa blase "T'as une tête affreuse."

    noam colere "Détache-moi."

    lysa taquin "Bonjour Lysa. Merci d'être venue. Non, surtout, ne change rien."

    noam agace "Ça fait combien de temps que je suis là ?"

    lysa reflexion "Quelques heures. Iris t'a pas raté, mais apparemment elle savait exactement où frapper pour t'éteindre sans te casser quelque chose."

    noam colere "Iris m'a mis KO et vous m'avez attaché. Ma politesse attendra."

    "Lysa soupire, puis s'approche du lit. Malgré son ton, elle me regarde attentivement, surtout la tempe."

    lysa fatigue "Je vais le dire sans me foutre de toi : t'as déconné. Tu débarques avec un couteau, Mara est devant toi, puis Iris te demande de laisser la lame au sol et tu la ramasses."

    noam desaccord "Je ne voulais attaquer personne."

    lysa fatigue "Je sais."

    noam surpris "Alors pourquoi je suis attaché ?"

    lysa fatigue "Parce qu'Iris savait pas ce que t'allais faire après. Moi non plus."

    noam colere "J'étais pas hors de contrôle. J'étais énervé parce que personne ne m'écoutait."
    noam fatigue "Bon. Vous voulez une explication ? Alors écoutez jusqu'au bout."
    call refutation_run("j20_defense")
    if _return[0] == "success":
        call play_noam_interupt
        noam raison "Je peux vous montrer où j'ai trouvé le corps. C'est au moins un point qu'on peut vérifier."
    else:
        lysa fatigue "Je te crois quand tu dis avoir eu peur. Mais ça ne suffit pas à expliquer le couteau."

    lysa blase "Tu vois, rien que cette phrase, elle résume assez bien le problème."

    noam agace "Lysa..."

    lysa fatigue "Je te crois quand tu dis que t'as vu Mara. Mais tu peux pas nous demander d'agir comme si elle était morte alors qu'elle est debout devant nous."

    noam colere "Arrête de dire 'dans ma tête'."

    lysa blase "Tu veux que je dise quoi ? Qu'elle est morte et vivante en même temps ?"

    noam colere "Je veux que tu admettes qu'il y a quelque chose qui colle pas !"

    sael raison "Personne ne dit le contraire."

    "Je tourne la tête vers Sael, qui est restée près de la porte."

    noam agace "Alors détache-moi."

    sael neutre "Non." id j20_infirmerie_sael_non

    noam colere "Pourquoi ?"

    sael neutre "Parce que tu viens de te réveiller, que tu cries et que tu tires encore sur les sangles."

    noam colere "Parce que je suis attaché !"

    lysa blase "C'est vrai que le concept tourne un peu en rond."

    noam colere "Ça t'amuse ?!"

    lysa fatigue "Non. C'est justement pour ça que je plaisante."

    "Sa réponse me coupe une seconde."

    "Lysa détourne légèrement le regard avant de reprendre."

    lysa fatigue "Tu nous fais peur, Noam. Pas parce qu'on pense que tu vas nous planter dès qu'on te détache. Parce qu'on te regarde t'enfoncer depuis plusieurs jours et que tu refuses d'admettre que tu ne tiens plus debout."

    noam desespoir "Je tiens très bien debout. Enfin, quand Iris ne m'assomme pas."

    lysa taquin "Tu vois ? C'était presque drôle. Il reste de l'espoir."

    noam colere "Je suis sérieux."

    lysa fatigue "Moi aussi."

    "Je prends une longue inspiration. J'essaie de parler moins fort, mais ma colère revient dès que je repense à la table vide."

    noam reflexion "Écoutez. Cette nuit, Mara était sur la table. Quand je suis revenu, le corps avait disparu. Entre les deux, quelqu'un est entré."

    sael mefiant "Ou ton souvenir est faux."

    noam colere "Je savais que t'allais dire ça."

    sael raison "Parce que c'est possible."

    noam colere "C'est pratique. Depuis M16, tout ce qui vous arrange pas devient un faux souvenir."

    sael raison "J'ai pas dit ça. Je dis juste qu'on peut pas écarter l'idée parce qu'elle te fait peur."

    noam inquiet "Ce qui me fait peur, c'est que quelqu'un se balade dans les murs pendant qu'on discute."

    lysa reflexion "Et qui serait ce quelqu'un ?"

    noam agace "J'en sais rien."

    lysa blase "Voilà."

    noam colere "Non, justement ! C'est pas 'voilà' ! Le fait que je sache pas qui c'est ne veut pas dire qu'il n'existe pas."

    "Je tire brusquement sur les sangles, plus fort que je ne le voulais."

    sael mefiant "Noam."

    noam colere "Quelqu'un connaissait cette salle ! Il a déplacé le corps et demain il peut partir avec nous !"

    sael inquiet "Noam, arrête. Tu vas te faire mal."

    noam colere "ARRÊTEZ DE ME DIRE DE ME CALMER !"

    "Sael ouvre immédiatement le petit meuble à côté du lit et en sort une seringue encore emballée."

    noam surpris "..." id j20_infirmerie_seringue_silence

    sael neutre "Noam, je veux pas te faire ça. Mais si tu continues à te débattre, je vais devoir te rendormir. Tu vas te blesser."

    noam inquiet "Tu plaisantes ?"

    sael neutre "Non."

    lysa blase "Pour une fois, je te conseille vraiment de la croire."

    "Je regarde la seringue, puis Sael. Elle n'a même pas besoin de hausser le ton."

    "Je relâche lentement mes bras."

    noam hesitation "D'accord... D'accord, je me calme."

    sael calme "Bien."

    "Elle garde tout de même la seringue à portée de main."

    lysa taquin "Incroyable. Vingt jours pour découvrir le bouton pause de Noam."

    noam colere "Profite."

    lysa taquin "Je compte bien."

    "Je respire plus lentement. Cette fois, je fais réellement l'effort de ne pas crier."

    noam raison "Je vous demande même plus de croire que Mara est morte. Juste... admettez qu'il y a quelqu'un ici qui en sait beaucoup plus que nous."

    "Lysa ne répond pas immédiatement."

    noam raison "Quelqu'un connaissait ces conduits avant nous. Si le corps était réel, il l'a déplacé pendant que j'étais parti."

    sael mefiant "Tu parles d'un traître."

    noam determine "Oui."

    "Le mot reste un instant dans la pièce."

    noam determine "Il y a un traître parmi nous."

    lysa reflexion "Tu as un nom ?"

    noam fatigue "Non."

    lysa reflexion "Un indice qui désigne quelqu'un ?"

    noam fatigue "Non."

    lysa fatigue "Tu vois bien le problème. Si on commence à regarder tout le monde comme un traître à moins de vingt-quatre heures du départ, on va finir par s'entretuer tout seuls."

    noam desaccord "Et si on ne fait rien, on peut partir avec cette personne demain."

    sael raison "Peut-être."

    noam agace "Tu vois ? Même toi tu l'envisages."

    sael raison "J'envisage tout. Ça veut pas dire que je vais pointer quelqu'un du doigt sans la moindre preuve."

    "Je ferme les yeux. Elles comprennent rien. Ou alors elles comprennent très bien et elles veulent juste pas me suivre là-dedans."

    noam fatigue "Faites seulement attention. C'est tout ce que je vous demande."

    lysa fatigue "Ça, je peux le faire."

    "Sa réponse est moins moqueuse."

    lysa fatigue "Mais toi, tu restes ici. Plus de conduits, plus de chasse au cadavre et plus de couteau."

    noam colere "Tu dis ça comme si c'était une habitude."

    lysa taquin "Une fois suffit largement."

    "Elle s'approche encore et remet correctement la couverture qui avait glissé pendant que je me débattais."

    noam surpris "..."

    lysa fatigue "Et avant que tu recommences : non, je ne te détache pas. J'ai envie de te retrouver vivant demain, même si tu fais absolument tout pour rendre ça compliqué."

    "Je la regarde sans savoir quoi répondre."

    noam inquiet "Lysa..."

    lysa blase "Quoi ?"

    noam inquiet "Si tu entends quelque chose cette nuit, derrière une grille ou dans un mur... ne va pas voir toute seule."

    "Elle me fixe quelques secondes, puis soupire."

    lysa sourire "D'accord."

    noam inquiet "Je suis sérieux."

    lysa sourire "Moi aussi. Si quelqu'un rampe derrière ma chambre, je réveille toute la station."

    sael neutre "Nous devrions y aller."

    noam inquiet "Attendez."

    sael neutre "Quoi encore ?"

    noam inquiet "Vous allez vraiment me laisser ici ?"

    lysa blase "Oui."

    noam colere "Attaché ?"

    lysa blase "Tu progresses vite."

    noam colere "Lysa..."

    lysa fatigue "Dors, Noam. Pour une fois, essaie juste de ne rien résoudre pendant quelques heures."

    "Sael ouvre la porte."

    noam inquiet "Et le traître ?"

    sael mefiant "S'il existe, il sera encore là quand tu te réveilleras."

    noam inquiet "C'est justement ce qui m'inquiète."

    "Elles échangent un regard, mais aucune ne répond."

    $ hideGroup()

    play sound sfx_door

    "La porte se referme derrière elles."

    jump _20_0_1_1_FIN


label _20_0_1_1_FIN:

    $ current_period = "Nuit"

    scene bg_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0

    "Je reste seul dans l'infirmerie, toujours attaché au lit."
    call KD_EXTRA_J20_ELEN from _call_kd_extra_j20_elen

    "Je fixe la porte après le départ de Lysa et Sael."
    think "Mara sur la table. Mara dans la cafétéria. Puis plus de corps."
    think "Quelqu'un a fait disparaître ce que j'ai vu."

    noam fatigue "..." id j20_fin_silence_noam

    "Je ferme les yeux, puis les rouvre presque aussitôt."

    "Demain, la navette arrivera. Si j'ai raison, le responsable pourra monter avec nous."

    "Je tire une dernière fois, doucement, sur la sangle de mon poignet."

    "Elle ne bouge pas."

    noam inquiet "Génial..."

    "Je regarde la grille d'aération, hors de portée depuis le lit."

    stop music fadeout 2.0
    call show_chapter_title("Fin du chapitre 6", "Chapitre 6 — Derrière les murs") from _call_show_chapter_title_23
    call end_day("21") from _call_j20_end_day_21
    jump _21_0_1_1_0_REVEIL
