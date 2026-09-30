# =============================================================================
# JOUR 20 — Route 0_1_1
# Réécriture complète
# =============================================================================

default j20_iris_qte_success = False


# Mise en scène spécifique à la révélation de Kael au J20.
# Le zoom est appliqué au sprite seul afin de garder la salle des Goumi lisible.
transform j20_kael_approach(z=1.0):
    xalign 0.5
    yalign 1.0
    zoom z


label _20_0_1_1_0_REVEIL:

    $ cafeteria_food_level = "null"
    $ current_period = "Matin"
    $ current_day = 20
    $ noam_has_juliette_drawing = False

    $ unlock_gallery_image("bg_cg040")
    scene bg_cg040 at adaptive_fullscreen
    $ flashlight_on(pattern=0)
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.0
    $ danger_on()

    think "Je ne sais pas combien de temps je reste devant la table avant de réussir à bouger."
    think "Mara est là. Allongée devant moi. Dans une pièce que personne n'était censé connaître."

    "Ma lampe tremble entre mes doigts. J'essaie de la stabiliser, mais dès que je regarde son visage, ça recommence."

    noam peur "Mara...?"

    "Je n'attends pas vraiment de réponse. Son torse ne bouge pas, ses yeux sont fermés et rien, absolument rien dans cette pièce, ne ressemble à quelqu'un qui dort tranquillement."

    think "Je devrais m'approcher. Vérifier son pouls. Faire quelque chose."
    think "Mais je n'y arrive pas."

    "Un bruit métallique résonne dans le conduit derrière moi."

    noam surpris "..." id j20_reveil_silence_noam

    "Cette fois, je ne reste pas."

    scene bg_conduit_reseau at adaptive_fullscreen with vpunch
    $ flashlight_on(pattern=4)

    "Je remonte dans le réseau aussi vite que l'espace me le permet, la lampe coincée dans une main et le couteau toujours serré dans l'autre. Je me cogne plusieurs fois contre la tôle, mais je continue sans ralentir."

    think "Il faut prévenir les autres."
    think "Il faut qu'ils viennent voir."

    $ flashlight_off()
    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je me laisse tomber hors de la grille et manque de m'écraser sur le sol de ma chambre. J'ai les genoux en feu, la respiration complètement coupée, mais je me relève presque immédiatement."

    "Je regarde le couteau dans ma main."

    think "Je devrais le poser."

    "Je ne le fais pas."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_200
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je traverse le couloir sans même chercher à savoir quelle heure il est. Quelques portes sont encore fermées, d'autres commencent à s'ouvrir. Je n'adresse la parole à personne."

    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Quand j'arrive près de la cafétéria, j'entends plusieurs voix à l'intérieur. Il y a déjà du monde."

    scene bg_cafeteria at adaptive_fullscreen with vpunch

    stop music fadeout 0.5
    play music "audio/music/bgm_tense_meeting.mp3" fadein 1.0

    "J'ouvre la porte tellement brutalement qu'elle vient frapper le mur."

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

    noam desespoir "Mara est morte !"

    "Plus personne ne parle."

    ryn surpris "Quoi ?" id j20_cafeteria_ryn_quoi

    noam desespoir "Mara est morte. Je viens de la trouver dans la salle des Goumi, derrière les conduits. Elle était allongée sur la table de maintenance."

    elen peur "Attends... Mara ? Notre Mara ?"

    noam colere "Oui, notre Mara ! De qui tu veux que je parle ?!"

    iris inquiet "Noam, calme-toi deux secondes et pose déjà ce que tu as dans la main."

    "Je baisse les yeux vers le couteau comme si je le découvrais seulement maintenant."

    noam "Je l'ai pris pour me défendre dans les conduits, c'est tout. Je ne suis pas venu ici pour menacer quelqu'un."

    lysa inquiet "Personne n'a dit ça, mais tu débarques couvert de poussière avec un couteau en hurlant qu'une fille est morte. Tu peux peut-être comprendre qu'on ait besoin de deux secondes pour suivre."

    noam colere "J'ai pas besoin que vous suiviez, j'ai besoin que vous veniez voir !"

    tomas inquiet "Tu l'as touchée ? Enfin... t'as vérifié son pouls ? T'es sûr qu'elle était morte ?"

    noam desaccord "Non, j'ai pas pris son putain de pouls ! Elle bougeait plus, elle respirait plus et elle était sur une table dans une pièce cachée. Ça vous suffit ou il faut vraiment que je vous fasse un rapport ?"

    sael mefiant "Ça suffit pour qu'on vérifie."

    "Des pas arrivent derrière moi avant que quelqu'un puisse répondre."

    mara "Vérifier quoi ?"

    $ horror_audio_cut(duration=0.52, restore_volume=0.70)
    $ unlock_gallery_image("bg_cg044")
    $ hideGroup()
    scene bg_cg044 at adaptive_fullscreen with signal_stutter
    $ cam_move(fx=0.67, fy=0.44, z=1.13, t=5.5)

    "Je me retourne."
    $ doppelganger_reveal(screamer=False, duration=0.86, restore_volume=0.70)

    "Mara vient d'entrer dans la cafétéria, les cheveux encore un peu en bataille, visiblement réveillée depuis peu."

    mara neutre "Pourquoi vous me regardez tous comme ça ?"

    noam panne "..."

    mara mefiant "Noam ?"

    "Je recule d'un pas quand elle s'approche."

    noam peur "Ne viens pas plus près."

    mara colere "Pardon ?"

    noam "Reste là."

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

    noam "C'est impossible..."

    $ investigation_add("mara_vivante")

    ryn desaccord "Noam, regarde-la. Elle est là."

    noam colere "Je la regarde ! C'est justement pour ça que je vous demande de venir avec moi ! Il y avait un corps sur cette table, et ce corps avait son visage !"

    iris inquiet "Tu es sûr que tu n'as pas simplement..."

    noam colere "Non !"

    "Je coupe Iris avant même qu'elle termine."

    noam "Me dites pas que j'ai rêvé. Pas maintenant. Venez voir la salle, regardez la table, et après vous pourrez me dire que je suis devenu fou si ça vous chante."

    mara colere "Moi, je vais nulle part avec toi tant que t'as ce couteau."

    noam "Très bien."

    "Je le pose lentement sur une table, manche tourné vers l'extérieur."

    noam determine "Maintenant, quelqu'un vient avec moi."

    "Un silence passe."

    iris reflexion "J'y vais."

    kael inquietude "Moi aussi."

    ryn "Je peux venir si—"

    iris desaccord "Non. On va pas être huit à ramper là-dedans. Kael vient, moi aussi. Et surtout, je veux éviter que Noam fasse encore une connerie."

    noam colere "Je ne me mets pas en danger."

    iris blase "Tu as passé la nuit avec un couteau dans une bouche d'aération. On en reparlera."

    mara stress "Et si y'a rien ?"

    "Je tourne la tête vers elle."

    noam desespoir "Il y aura quelque chose."

    "Je le dis sans hésiter. Pourtant, une partie de moi espère presque avoir tort."

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

    "Nous avançons tous les trois dans le réseau. Iris est juste derrière moi, Kael ferme la marche et, contrairement à la veille, chaque bruit me semble beaucoup plus fort."

    iris inquiet "T'es sûr du chemin ? Et je demande sérieusement, hein. J'ai aucune envie de me paumer là-dedans juste avant de partir."

    noam "Oui. Je reconnais les bifurcations. La salle est encore un peu plus loin."

    kael inquietude "Tu étais venu jusque-là tout seul cette nuit ?"

    noam "Oui."

    kael "Avec ton couteau."

    noam colere "Je sais très bien à quoi ça ressemble, Kael ! Ça fait plusieurs nuits que j'entends quelqu'un derrière ma chambre, personne m'écoute et j'en ai eu marre. Alors avance."

    "Il ne répond pas."

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

    "Mes pieds touchent le sol et je braque immédiatement la lampe vers la table de maintenance."

    pause 1.0

    noam panne "..."

    "{cps=10}Elle est vide.{/cps}"
    with flash_white

    "Je reste immobile quelques secondes, convaincu que je me suis trompé de table. Puis je regarde celle d'à côté, le sol, l'espace entre les établis."

    noam peur "Non..."

    iris inquiet "Noam ?"

    noam "Elle était là."

    "Je m'approche de la table et passe ma main sur la surface métallique."

    noam "Elle était là ! Sur le dos, la tête de ce côté. Je confonds pas, bordel."

    kael inquietude "Il n'y a rien."

    noam colere "Merci, j'avais remarqué."

    "Je regarde sous la table, derrière les deux Goumi, puis dans les espaces de rangement ouverts sous l'établi."

    iris reflexion "Noam, arrête deux secondes. Si quelqu'un a vraiment déplacé un corps, tu vas pas le retrouver en ouvrant trois tiroirs au pif."

    noam colere "Donc tu admets que quelqu'un a pu le déplacer ?"

    iris "Je dis seulement que ce que tu fais ne sert à rien."

    noam "Parce que vous pensez que j'ai tout inventé."

    iris inquiet "Je pense surtout que tu dors presque plus et que t'es terrifié. Ça veut pas dire que tu mens."

    noam colere "Arrêtez tous avec ça ! J'étais fatigué, oui. J'avais peur, oui. Ça ne transforme pas une table vide en cadavre !"

    kael inquietude "Et pourtant, maintenant, elle est vide."

    "Je me retourne brutalement vers lui."

    noam colere "Tu veux dire quoi par là ?"

    kael "Rien. Je dis juste qu'on est venus vérifier... et qu'il y a personne, Noam."

    noam "Tu crois que je mens ?"

    kael "Depuis trois jours, on découvre que nos souvenirs peuvent nous raconter n'importe quoi. Alors non, je vais pas te dire que t'as forcément raison juste parce que tu gueules."

    "Je trouve rien à répondre tout de suite."

    noam desespoir "Je l'ai vue..."

    iris triste "Je sais que tu en es convaincu."

    noam colere "Ne me parle pas comme si j'étais malade."

    iris inquiet "Alors arrête de te comporter comme si on voulait tous te piéger."

    "Je fais un pas vers elle, plus par frustration que par intention réelle, et mon pied heurte quelque chose au sol."

    play sound sfx_drop

    "Le couteau glisse sur le métal."

    "Je baisse les yeux."

    noam surpris "..." id j20_couteau_silence_noam

    iris peur "Ne le ramasse pas."

    noam desaccord "Iris, je vais juste le récupérer."

    iris determine "Non. Tu le laisses par terre et on remonte."

    noam colere "Tu crois vraiment que je vais vous attaquer ?"

    iris "Là, je crois surtout que tu réfléchis plus correctement. Alors pour une fois, tu m'écoutes et tu t'éloignes de ce putain de couteau."

    noam colere "J'en ai marre qu'on décide à ma place ce que j'ai vu, ce que j'ai compris et maintenant même ce que j'ai le droit de toucher !"

    "Je me penche malgré elle."

    iris colere "Noam, ne fais pas ça."

    "Je referme ma main sur le manche et me redresse."

    noam "Voilà. Je l'ai. Et maintenant on remonte, d'accord ?"

    "Iris ne bouge pas."

label _20_0_1_1_IRIS_CONFRONTATION:

    # Le décor est reposé ici pour les accès directs depuis la roadmap.
    scene bg_salle_goumi_cachee at adaptive_fullscreen

    iris determine "Pose-le."
    $ danger_on()

    noam colere "Mais je viens de te dire que—"

    "Elle avance d'un pas."

    noam inquiet "Iris, reste où tu es."

    iris "Pose le couteau et je reste où je suis."

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


label _20_0_1_1_IRIS_QTE_ECHEC:

    $ unlock_gallery_image("bg_cg047")
    scene bg_cg047 at adaptive_fullscreen with flash_white

    "Le couteau tombe immédiatement. J'essaie de me dégager par réflexe, mais elle garde mon bras bloqué et me repousse contre la table."

    iris colere "Arrête de bouger !"

    noam colere "Lâche-moi !"

    iris "Je te lâche dès que tu te calmes !"

    noam "Je suis calme !"

    kael "Non, Noam, là t'es vraiment pas calme !"

    "Je force pour me relever. Iris change simplement d'appui, me déséquilibre une deuxième fois et, quand j'essaie encore de lui échapper, son mouvement suivant part beaucoup plus vite que le précédent."

    "Je vois son poing arriver sur le côté."

    scene bg_cg047 at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 0.95
    $ shake(9, 0.22)

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

    "Je baisse l'épaule au moment où Iris cherche à verrouiller mon bras. Sa prise glisse."

    "Elle revient aussitôt. J'évite son coude de justesse et je tire mon poignet vers moi avant qu'elle puisse le reprendre."

    iris colere "Arrête de bouger !"

    noam colere "Arrête de m'attaquer !"

    "Elle tente encore de saisir mon bras. Je recule contre la table, le couteau toujours serré dans ma main."

    noam inquiet "Iris, stop !"

    iris colere "Alors lâche-le !"

    noam "Je vais le poser, mais arrête de me sauter dessus deux secondes !"

    iris "Tu dis ça depuis tout à l'heure !"

    "Elle attrape mon avant-bras à deux mains."

    noam colere "Lâche-moi !"

    iris "Lâche le couteau !"

    "Je tire mon bras vers moi. Elle tire dans l'autre sens."

    "Pendant une seconde, personne ne gagne."

    kael inquietude "Ça suffit !"

    "Iris change brusquement d'appui."

    "Son pied accroche le bord de la table."

    iris surpris "Merde—"

    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch
    play sound sfx_drop

    "Tout va beaucoup trop vite."

    "Je sens son poids partir vers moi."

    "Puis quelque chose s'arrête net."

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

    "Pendant une seconde, elle a juste l'air agacée. Comme si son cerveau refusait encore de comprendre."

    iris fatigue "T'es... sérieux... ?"

    noam desespoir "J'ai pas fait exprès. Putain, Iris, j'ai pas fait exprès !"

    "Je lâche immédiatement le manche."

    iris peur "Non !"

    "Sa voix me coupe."

    iris "Touche pas... laisse-le."

    noam "D'accord. D'accord, je touche pas."

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

    noam "Mais bouge, putain !"

    show kael taquin at j20_kael_approach(1.34) with Dissolve(0.22)

    "Ses lèvres remontent un peu plus."

    noam panne "..."

    show kael joie at j20_kael_approach(1.46) with Dissolve(0.20)

    "Je connais le sourire de Kael."

    "Celui-là, non."

    noam inquiet "Kael... ?"

    show kael sourire at j20_kael_approach(1.60) with Dissolve(0.18)

    "Il fait un pas vers nous."

    noam "Qu'est-ce que tu fous ? Va chercher quelqu'un !"

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

    noam "T'es pas Kael."

    hide kael
    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch
    play sound "audio/sfx_thud.mp3" volume 0.95

    "Il se jette sur moi."

    "Je lève le bras par réflexe."

    play sound "audio/sfx_thud.mp3" volume 1.0
    $ shake(10, 0.22)

    "Il frappe mon poignet contre le bord de la table."

    play sound sfx_drop

    "Le couteau tombe quelque part au sol."

    noam colere "DÉGAGE !"

    play sound "audio/sfx_thud.mp3" volume 0.90
    $ shake(8, 0.18)

    "Je lui donne un coup d'épaule et réussis à le repousser."

    "Iris essaie de se redresser derrière moi."

    iris colere "Espèce de..."

    "Kael pivote vers elle."

    noam peur "IRIS, NON !"

    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch

    "Elle essaie de le frapper."

    "Son bras part trop lentement."

    play sound "audio/sfx_thud.mp3" volume 1.0
    $ impact(intensity=8, duration=0.20, color="#8f101c")

    "Kael lui donne un coup sec au visage."

    play sound "audio/sfx_drop.mp3" volume 0.72

    "Iris retombe contre le sol."

    noam desespoir "IRIS !"

    "Je me jette sur lui."

    "Je n'arrive même pas jusqu'à son épaule."

    play sound "audio/sfx_thud.mp3" volume 1.0
    $ shake(14, 0.30)
    scene bg_salle_goumi_cachee at adaptive_fullscreen with vpunch

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

    # À partir d'ici, Noam n'est plus le narrateur.
    # La narration passe volontairement à un point de vue externe.
    scene bg_salle_goumi_cachee at adaptive_fullscreen with creep_diss

    "Noam ne voit pas Kael se redresser."

    pause 0.8

    play sound "audio/sfx_duct_scrape.wav" volume 0.74

    "Il ne voit pas non plus la grille d'aération bouger derrière lui."

    play sound "audio/sfx_metal_open.mp3"

    "La grille s'ouvre."

    "Deux mains apparaissent."

    "Puis un visage."

    pause 0.8

    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.2

    "Noam sort du conduit."

    "Le même visage."

    "Les mêmes cheveux."

    "Les mêmes vêtements."

    "Aucune hésitation."

    $ doppelganger_reveal(screamer=True, duration=0.96, restore_volume=0.56)

    "Le second Noam regarde Kael."

    "Kael désigne Iris d'un mouvement du menton."

    "Aucun des deux ne parle."

    "Noam se penche, passe un bras sous les épaules d'Iris et l'autre sous ses jambes."

    "Kael attrape le premier Noam sous les bras."

    "Les deux corps sont emportés dans le conduit."

    scene bg_conduit_reseau at adaptive_fullscreen with creep_diss

    "Le trajet dure plusieurs minutes."

    "Ils passent deux embranchements, descendent plus bas dans la structure, puis s'arrêtent devant une grille que Noam n'avait jamais vue."

    "Kael la déverrouille."

    "Derrière, il n'y a plus de conduit."

    "Il y a une salle."

    pause 0.8

    scene bg_laboratoire at adaptive_fullscreen with creep_diss

    "La pièce ressemble vaguement à une infirmerie."

    "Vaguement."

    "Il y a bien des écrans, des plateaux métalliques et des machines autour des murs, mais rien n'est disposé pour soigner quelqu'un."

    "Au centre, une énorme cuve verticale occupe presque toute la hauteur de la salle."

    "Quelque chose flotte à l'intérieur."

    pause 0.7

    "Un corps."

    "Ou presque."

    "Deux bras."

    "Deux jambes."

    "Une tête."

    "Mais aucun visage vraiment terminé."

    "La peau est pâle, lisse, presque sans détail."

    "Kael dépose Noam au sol."

    "Le second Noam fait la même chose avec Iris."

    "Elle respire encore."

    "Faiblement."

    "Kael s'approche de la machine."

    "Il ouvre un compartiment, retire plusieurs pièces, en ajoute d'autres."

    "Certaines ressemblent à des poches médicales."

    "D'autres à des composants électroniques."

    "Impossible de savoir où s'arrête l'un et où commence l'autre."

    "Le second Noam reste debout près d'Iris."

    "Il la regarde."

    "Puis regarde la cuve."

    "Kael appuie sur l'écran."

    play sound "audio/sfx_tinnitus.wav" volume 0.38

    "La machine démarre."

    "Le liquide dans la cuve se met à tourner lentement."

    "La forme à l'intérieur tressaille."

    pause 0.8

    "Ses doigts bougent."

    "Puis ses bras."

    "Quelque chose change dans son visage."

    "Les contours se creusent."

    "Des cheveux apparaissent."

    "La couleur vient ensuite."

    pause 0.8

    "Rouge."

    "Le visage n'est plus vide."

    "C'est celui d'Iris."

    pause 1.0

    "La cuve se vide."

    "Le corps s'effondre contre la paroi."

    play sound "audio/sfx_metal_open.mp3"

    "La porte s'ouvre."

    "Iris tombe à genoux sur le sol, trempée, incapable de tenir debout correctement."

    iris panne "..."

    "Elle tousse."

    "Respire."

    "Regarde autour d'elle."

    "Puis elle fronce les sourcils."

    iris colere "...Putain..."

    "Elle passe une main tremblante sur son bras."

    iris fatigue "Il fait froid ici."

    "Kael lui tend une couverture."

    "Elle la prend sans poser de question."

    "Le second Noam sourit."

    scene bg_laboratoire at adaptive_fullscreen with dissolve

    "Quelques minutes plus tard, une porte latérale s'ouvre."

    "La lumière s'allume automatiquement."

    scene bg_cavite_technique at adaptive_fullscreen with creep_diss

    "Des corps sont entassés contre le fond de la pièce."

    "Pas des dizaines."

    "Juste assez pour comprendre."

    pause 0.6

    "Mara est là."

    "Le même corps que Noam avait trouvé sur la table quelques heures plus tôt."

    pause 0.6

    "À côté d'elle repose Kael."

    "Le vrai Kael."

    pause 0.8

    "Et un peu plus loin..."

    "Noam."

    pause 1.0

    "Un autre Noam."

    "Immobile."

    "Déjà là avant leur arrivée."

    $ horror_audio_cut(duration=0.42, restore_volume=0.45)

    "Kael traîne le Noam inconscient dans la pièce."

    "Le second Noam fait la même chose avec Iris."

    "Ils les déposent à côté des autres."

    "Sans précaution particulière."

    "Comme s'ils rangeaient quelque chose."

    pause 0.8

    "Derrière eux, la nouvelle Iris apparaît dans l'encadrement de la porte."

    "Elle a maintenant une tenue sur le dos."

    "Ses cheveux sont encore humides."

    "Elle regarde Mara."

    "Puis Kael."

    "Puis les deux Noam."

    "Son regard descend enfin sur Iris."

    pause 1.0

    iris reflexion "..."

    "Elle fixe son propre corps pendant quelques secondes."

    "Son visage se ferme."

    iris colere "...C'est quoi ce bordel ?"

    scene black with signal_stutter
    stop music fadeout 0.2
    $ danger_off()

    pause 1.2

    call screen kd_ending_reached(
        "Les Remplaçants",
        "ENDING 01 // JOUR 20"
    )
    $ _ending_screen_closed = _return

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

    noam "Sael ?! Iris ?!"

    "Je recommence, plus fort."

    noam colere "Détachez-moi !"

    "Ma voix traverse la pièce et s'écrase contre la porte fermée. Personne ne vient."

    "Je me débats encore quelques secondes avant que la douleur dans ma tête m'oblige à arrêter."

    noam "Putain..."

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
            think "Deux patients enregistrés sur un seul lit. Ou deux versions du même patient."
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

    "Je ne sais pas combien de temps je reste comme ça. Assez longtemps pour avoir la gorge sèche à force d'appeler, puis assez longtemps encore pour que je finisse par me taire."

    "Le pire n'est même plus d'être attaché."

    "Le pire, c'est de savoir que Mara est quelque part dans le Conclave alors que je peux encore voir son corps dès que je ferme les yeux."

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

    lysa blase "Eh ben... T'as vraiment une tête affreuse."

    noam colere "Détache-moi."

    lysa "Bonjour Lysa, merci d'être venue voir comment je vais. Non, vraiment, fais comme chez toi."

    noam "Ça fait combien de temps que je suis là ?"

    lysa reflexion "Quelques heures. Iris t'a pas raté, mais apparemment elle savait exactement où frapper pour t'éteindre sans te casser quelque chose."

    noam colere "Elle m'a mis KO et ensuite vous m'avez attaché à un lit pendant des heures. Tu veux vraiment qu'on parle de ma politesse ?"

    "Lysa soupire, puis s'approche du lit. Malgré son ton, elle me regarde attentivement, surtout la tempe."

    lysa fatigue "Je vais te le dire une fois sans me foutre de toi : t'as complètement déconné. T'es revenu avec un couteau en gueulant que Mara était morte alors qu'elle était juste là. Et après, dans les conduits, Iris te dit de laisser le couteau au sol... et toi tu le ramasses quand même."

    noam desaccord "Je ne voulais attaquer personne."

    lysa "Je sais."

    noam surpris "Alors pourquoi je suis attaché ?"

    lysa "Parce que ça change rien au fait que t'étais hors de contrôle ! Iris savait pas ce que t'allais faire la seconde d'après. Et franchement ? Moi non plus."

    noam colere "J'étais pas hors de contrôle. J'étais énervé parce que personne ne m'écoutait."

    lysa blase "Tu vois, rien que cette phrase, elle résume assez bien le problème."

    noam "Lysa..."

    lysa fatigue "Je te crois quand tu dis que t'as eu peur. Je te crois même quand tu dis que t'as vraiment vu Mara sur cette table. Mais tu peux pas demander à tout le monde d'agir comme si elle était morte alors qu'elle est debout devant nous."

    noam colere "Arrête de dire 'dans ma tête'."

    lysa "Tu veux que je dise quoi ? Que Mara est morte et vivante en même temps ?"

    noam "Je veux que tu admettes qu'il y a quelque chose qui ne colle pas !"

    sael raison "Personne ne dit le contraire."

    "Je tourne la tête vers Sael, qui est restée près de la porte."

    noam "Alors détache-moi."

    sael neutre "Non." id j20_infirmerie_sael_non

    noam colere "Pourquoi ?"

    sael "Parce que tu t'es réveillé depuis moins d'une heure, que tu cries depuis que nous sommes entrées et que tu essaies encore de tirer sur tes liens toutes les trente secondes."

    noam "Parce que je suis attaché !"

    lysa blase "C'est vrai que le concept tourne un peu en rond."

    noam colere "Ça t'amuse ?!"

    lysa "Non. C'est justement pour ça que je plaisante."

    "Sa réponse me coupe une seconde."

    "Lysa détourne légèrement le regard avant de reprendre."

    lysa fatigue "Tu nous fais peur, Noam. Pas parce qu'on pense que tu vas nous planter dès qu'on te détache. Parce qu'on te regarde t'enfoncer depuis plusieurs jours et que tu refuses d'admettre que tu ne tiens plus debout."

    noam desespoir "Je tiens très bien debout. Enfin, quand Iris ne m'assomme pas."

    lysa taquin "Tu vois ? C'était presque drôle. Il reste de l'espoir."

    noam colere "Je suis sérieux."

    lysa "Moi aussi."

    "Je prends une longue inspiration. J'essaie de parler moins fort, mais ma colère revient dès que je repense à la table vide."

    noam reflexion "Écoutez-moi juste jusqu'au bout. Quand je suis entré dans cette salle cette nuit, Mara était là. Quand je suis revenu avec Iris et Kael, elle avait disparu. Entre les deux, quelqu'un a forcément fait quelque chose."

    sael mefiant "Ou ton souvenir est faux."

    noam colere "Je savais que t'allais dire ça."

    sael "Parce que c'est possible."

    noam "Et c'est pratique, hein ? Depuis qu'on a découvert M16, dès qu'il se passe quelque chose qu'on n'arrive pas à expliquer, on peut juste dire que ma mémoire déconne."

    sael raison "J'ai pas dit ça. Je dis juste qu'on peut pas écarter l'idée parce qu'elle te fait peur."

    noam "Ce qui me fait peur, c'est qu'on puisse tous rester là à discuter pendant que quelqu'un se balade dans les murs."

    lysa reflexion "Et qui serait ce quelqu'un ?"

    noam "J'en sais rien."

    lysa "Voilà."

    noam colere "Non, justement ! C'est pas 'voilà' ! Le fait que je sache pas qui c'est ne veut pas dire qu'il n'existe pas."

    "Je tire brusquement sur les sangles, plus fort que je ne le voulais."

    sael mefiant "Noam."

    noam "Quelqu'un connaissait cette salle ! Quelqu'un a pu déplacer le corps avant qu'on revienne ! Et demain on quitte tous le Conclave comme si de rien n'était !"

    sael "Calme-toi."

    noam colere "ARRÊTEZ DE ME DIRE DE ME CALMER !"

    "Sael ouvre immédiatement le petit meuble à côté du lit et en sort une seringue encore emballée."

    noam surpris "..." id j20_infirmerie_seringue_silence

    sael neutre "Si tu continues, je t'injecte un anesthésiant et tu dormiras jusqu'à ce que je décide que tu peux te réveiller sans arracher les sangles."

    noam inquiet "Tu plaisantes ?"

    sael "Non."

    lysa blase "Pour une fois, je te conseille vraiment de la croire."

    "Je regarde la seringue, puis Sael. Elle n'a même pas besoin de hausser le ton."

    "Je relâche lentement mes bras."

    noam hesitation "D'accord... D'accord, je me calme."

    sael "Bien."

    "Elle garde tout de même la seringue à portée de main."

    lysa taquin "Incroyable. Vingt jours pour découvrir le bouton pause de Noam."

    noam colere "Profite."

    lysa "Je compte bien."

    "Je respire plus lentement. Cette fois, je fais réellement l'effort de ne pas crier."

    noam raison "Je vous demande même plus de croire que Mara est morte. Juste... admettez qu'il y a quelqu'un ici qui en sait beaucoup plus que nous."

    "Lysa ne répond pas immédiatement."

    noam "Quelqu'un connaissait ces conduits avant nous. Quelqu'un savait comment atteindre cette salle et... si ce corps était réel, bordel, quelqu'un l'a déplacé pendant que j'étais parti."

    sael mefiant "Tu parles d'un traître."

    noam determine "Oui."

    "Le mot reste un instant dans la pièce."

    noam "Il y a un traître parmi nous."

    lysa reflexion "Tu as un nom ?"

    noam "Non."

    lysa "Un indice qui désigne quelqu'un en particulier ?"

    noam "Non."

    lysa fatigue "Tu vois bien le problème. Si on commence à regarder tout le monde comme un traître à moins de vingt-quatre heures du départ, on va finir par s'entretuer tout seuls."

    noam desaccord "Et si on ne fait rien, on peut partir avec cette personne demain."

    sael "Peut-être."

    noam "Tu vois ? Même toi tu l'envisages."

    sael raison "J'envisage tout. Ça veut pas dire que je vais pointer quelqu'un du doigt sans la moindre preuve."

    "Je ferme les yeux. Elles comprennent rien. Ou alors elles comprennent très bien et elles veulent juste pas me suivre là-dedans."

    noam fatigue "Faites seulement attention. C'est tout ce que je vous demande."

    lysa fatigue "Ça, je peux le faire."

    "Sa réponse est moins moqueuse."

    lysa "Mais toi, tu vas rester ici pour l'instant. Tu vas arrêter de courir dans les murs, arrêter de chercher des cadavres tout seul et surtout arrêter de prendre des couteaux dès que tu entends un bruit."

    noam colere "Tu dis ça comme si c'était une habitude."

    lysa taquin "Une fois suffit largement."

    "Elle s'approche encore et remet correctement la couverture qui avait glissé pendant que je me débattais."

    noam surpris "..."

    lysa fatigue "Et avant que tu recommences : non, je ne te détache pas. J'ai envie de te retrouver vivant demain, même si tu fais absolument tout pour rendre ça compliqué."

    "Je la regarde sans savoir quoi répondre."

    noam "Lysa..."

    lysa "Quoi ?"

    noam inquiet "Si tu entends quelque chose cette nuit, derrière une grille ou dans un mur... ne va pas voir toute seule."

    "Elle me fixe quelques secondes, puis soupire."

    lysa sourire "D'accord."

    noam "Je suis sérieux."

    lysa "Moi aussi. Je te promets que si quelqu'un vient ramper derrière ma chambre cette nuit, je hurlerai suffisamment fort pour réveiller tout le Conclave."

    sael neutre "Nous devrions y aller."

    noam inquiet "Attendez."

    sael "Quoi encore ?"

    noam "Vous allez vraiment me laisser ici ?"

    lysa blase "Oui."

    noam "Attaché ?"

    lysa "Tu progresses vite."

    noam colere "Lysa..."

    lysa fatigue "Dors, Noam. Pour une fois, essaie juste de ne rien résoudre pendant quelques heures."

    "Sael ouvre la porte."

    noam "Et le traître ?"

    sael mefiant "S'il existe, il sera encore là quand tu te réveilleras."

    noam "C'est justement ce qui m'inquiète."

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

    "Pendant un long moment, je fixe simplement la porte par laquelle Lysa et Sael viennent de sortir. J'aimerais me convaincre qu'elles vont réfléchir à ce que je leur ai dit, mais je n'en sais rien."

    think "Il y a un traître parmi nous."
    "Je me répète la phrase. J'en sais rien. Mais pour l'instant, c'est la seule chose qui relie encore tout le reste."

    think "Mara dans la salle."
    think "Mara dans la cafétéria."
    think "Le corps disparu."

    "Trois faits qui ne peuvent pas exister ensemble, et pourtant je me souviens des trois."

    noam fatigue "..." id j20_fin_silence_noam

    "Je ferme les yeux, puis les rouvre presque aussitôt."

    "Demain, la navette arrivera."

    "Tout le monde quittera le Conclave."

    "Et si j'ai raison, celui qui nous manipule quittera peut-être cet endroit avec nous."

    "Je tire une dernière fois, doucement, sur la sangle de mon poignet."

    "Elle ne bouge pas."

    noam inquiet "Génial..."

    "Pour la première fois depuis plusieurs nuits, je n'ai même plus accès à la bouche d'aération."

    "Ça devrait me rassurer."

    "Étrangement, ce n'est pas le cas."

    stop music fadeout 2.0
    call end_day("21") from _call_j20_end_day_21
    jump _21_0_1_1_0_REVEIL
