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
default j50_wire_time_left = 30

init python:
    J50_SAEL_HOTSPOTS = {
        "lit": ("images/background/interact/chambre_sael/lit.png", "images/background/interact/chambre_sael/lit_hover.png"),
        "crane": ("images/background/interact/chambre_sael/crane.png", "images/background/interact/chambre_sael/crane_hover.png"),
        "affaires": ("images/background/interact/chambre_sael/affaires.png", "images/background/interact/chambre_sael/affaires_hover.png"),
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

    def j50_sael_mark_seen(item):
        if item not in store.j50_sael_pnc_seen:
            store.j50_sael_pnc_seen.append(item)
            store.j50_sael_pnc_score += 1

    def j50_wire_reset():
        store.j50_wire_success = 0
        store.j50_wire_errors = 0
        store.j50_wire_selected = None
        store.j50_wire_done = []
        store.j50_wire_right_done = []
        store.j50_wire_connections = []
        store.j50_wire_time_left = 30

    def j50_wire_pick_left(idx):
        if idx not in store.j50_wire_done:
            store.j50_wire_selected = idx

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
            renpy.sound.play("audio/sfx_announce.mp3")
        else:
            store.j50_wire_errors += 1
            renpy.sound.play("audio/sfx_announce.mp3")
        store.j50_wire_selected = None
        renpy.restart_interaction()

    def j50_wire_tick():
        store.j50_wire_time_left = max(0, store.j50_wire_time_left - 1)
        renpy.restart_interaction()

screen j50_sael_room_pnc():
    modal True
    zorder 200

    add Solid("#000")
    add "images/background/interact/chambre_sael/bg_chambre_sael.png" at cover_screen

    for item, paths in J50_SAEL_HOTSPOTS.items():
        imagebutton:
            idle paths[0]
            hover paths[1]
            focus_mask True
            xpos 0
            ypos 0
            at cover_screen
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

screen j50_wire_minigame():
    modal True
    zorder 220
    on "show" action Function(j50_wire_reset)
    add Solid("#02070bee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1500
        ysize 820
        padding (34, 28)
        background Solid("#07151ef5")
        vbox:
            spacing 18
            hbox:
                xfill True
                text "RECÂBLAGE D'URGENCE" size 44 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                text "[j50_wire_time_left]s" size 40 color "#ffe7ae" xalign 1.0 font "fonts/Rajdhani-SemiBold.ttf"
            text "Relie les fils de même couleur. Même couleur ensemble. Tu réfléchis pas. Tu relies." size 24 color "#9ed8ff"
            hbox:
                spacing 180
                vbox:
                    spacing 14
                    text "Fils coupés" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                    for idx, wire in enumerate(J50_WIRE_COLORS):
                        $ color_name, color_hex = wire
                        button:
                            xsize 430
                            ysize 40
                            background Solid("#1f2b34" if idx != j50_wire_selected else "#f3f8ff")
                            sensitive idx not in j50_wire_done
                            action Function(j50_wire_pick_left, idx)
                            hbox:
                                spacing 12
                                add Solid(color_hex) xsize 250 ysize 12 yalign 0.5
                                if idx in j50_wire_done:
                                    text "OK" size 22 color "#7cff9b"
                                else:
                                    text color_name.upper() size 22 color "#dff8ff"
                vbox:
                    spacing 14
                    text "Connecteurs" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                    for connector_idx, color_name in enumerate(J50_WIRE_RIGHT_ORDER):
                        $ color_hex = dict(J50_WIRE_COLORS).get(color_name, "#ffffff")
                        button:
                            xsize 430
                            ysize 40
                            background Solid("#12241d" if connector_idx in j50_wire_right_done else "#101820")
                            hover_background Solid("#263748")
                            sensitive connector_idx not in j50_wire_right_done
                            action Function(j50_wire_pick_right, connector_idx)
                            hbox:
                                spacing 12
                                if connector_idx in j50_wire_right_done:
                                    text "LIE" size 22 color "#7cff9b"
                                else:
                                    text color_name.upper() size 22 color "#dff8ff"
                                add Solid(color_hex) xsize 250 ysize 12 yalign 0.5
            if j50_wire_connections:
                hbox:
                    spacing 12
                    text "Liaisons verrouillees :" size 22 color "#9ed8ff"
                    text "[len(j50_wire_connections)]/[len(J50_WIRE_COLORS)]" size 22 color "#7cff9b"
            hbox:
                spacing 40
                text "Réussites : [j50_wire_success]" size 28 color "#7cff9b"
                text "Erreurs : [j50_wire_errors]" size 28 color "#ff8585"

    timer 1.0 repeat True action Function(j50_wire_tick)
    if j50_wire_time_left <= 0:
        timer 0.1 action Return(True)
    if j50_wire_success >= 12:
        timer 0.2 action Return(True)

label _5_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 5
    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    show screen day3_codex_logo

    pause 1.2

    $ blink()
    think "J'ouvre les yeux sans avoir l'impression d'avoir dormi."
    think "La nuque raide, les épaules dures. Mon corps s'est couché ; ma tête, non."

    pause 0.5

    $ blink()
    think "Même le silence attend quelque chose."

    pause 0.6

    think "Le vote d'il y a deux jours. Celui de demain. Entre les deux, plus rien ne tient."

    $ blink()

    think "Ça ne passera pas. Personne n'y croit encore."

    think "Je me redresse. Il faut bien commencer quelque part."

    scene bg_chambre at adaptive_fullscreen with dissolve

    think "J'ai pris plusieurs jours pendant la nuit."

    pause 0.6

    think "Me lever ressemble déjà à une décision. Mauvais début."

    think "Si je vais à la cafétéria, ce sera pareil qu'hier."
    think "Des silences. Des regards qui fuient. Et la même certitude dans chaque tête : ce vote va échouer."

    pause 0.7

    noam "Rien n'a encore explosé et on se comporte déjà comme après la casse."
    think "Je l'ai dit à voix haute. Parfait."

    pause 0.5

    think "Mes mains ne tremblent même pas. L'impuissance a donc une phase calme."

    think "Non. Trop facile. Si je commence comme ça, la journée est déjà morte."

    think "Je serre les doigts. Au moins, je suis bien réveillé."

    pause 0.5

    think "Le vote n'a peut-être aucune chance de passer."
    think "L'ambiance est glaciale."
    think "Sael est fermée."
    think "Julian se mure dans sa chambre."
    think "Et moi, je n'ai même pas de bonne réponse. Mais je n'abandonnerai pas."

    pause 0.6

    think "Le pire, c'est que chacun a une part de raison. Et demain, il faudra trancher comme si une décision acceptable existait."
    think "Face, tu gagnes. Pile, je perds."

    pause 0.5

    think "Je me lève enfin. Première décision validée."
    think "L'air paraît plus froid. Ou c'est juste moi."

    play sound sfx_announce
    pause 0.7

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits ! Jour cinq, et ça fleure déjà le drame."
    kami "Ne vous inquiétez pas : votre prochaine chance de tout rater arrive dans vingt-quatre heures !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rappel amical : le vote sur la libre circulation aura lieu demain."
    kami "Vous aurez donc une nuit de plus pour vous convaincre que vous êtes capables de décider de quelque chose ensemble."
    kami "Comme c'est amusant !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "La cafétéria est ouverte. Vos rations sont prêtes. Les mêmes qu'hier."
    kami "Et comme toujours, j'observerai avec beaucoup d'intérêt ce que vous allez faire de cette belle matinée ensoleillée."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oups, j'oubliais : vous ne pouvez pas voir le soleil depuis le Conclave !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    think "L'écran s'éteint sur son rire. Le silence paraît presque poli en comparaison."

    pause 0.8

    think "La cafétéria."

    think "J'imagine l'ambiance."

    think "Est-ce que j'ai vraiment envie de traverser ça ce matin ?"

    pause 0.5

    think "Le pain sur ma table est dur, sec et silencieux. Candidat idéal."

    pause 0.3

    jump _5_0_SKIP_CAFETERIA


label _5_0_SKIP_CAFETERIA:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    think "Je prends le pain."
    think "Il est vraiment sec."

    think "Je me demande si quelqu'un remarquera que je ne suis pas venu à la cafétéria."

    think "Je mords dedans."
    think "Ça craque sous les dents. Le goût précis de presque rien."

    pause 0.4

    think "Debout, seul, dos à la porte. Pas de conversation, pas de regard, pas d'hypocrisie."
    think "Juste ce pain et moi. Il est plus facile à affronter qu'un vote."

    think "C'est mieux comme ça, un peu plus reposant."
    think "Au moins pour cette heure-là."

    pause 0.7

    think "Je termine le morceau et m'essuie la main. Petit-déjeuner réussi, selon des critères très bas."

    think "Des pas et des voix traversent le couloir. Le groupe se retrouve autour des plateaux."
    think "Je ne peux pas les rejoindre. Pas avant de savoir ce que je peux encore faire."

    think "Sael. Si elle vote contre, c'est foutu."
    think "Il faut que je lui parle."
    think "Avant que ce soit trop tard."

    pause 0.5

    think "Sael est là. Je l'ai entendue rentrer hier soir en essayant d'être discrète. C'est ce qui l'a trahie."

    pause 0.4

    think "Je gagne la porte avant de trouver une nouvelle raison de rester."

    think "Il faut au moins essayer. Enfin… il me semble."

    stop music fadeout 1.2

    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 0.8

    think "Le couloir se vide vers la cafétéria. Personne ne me regarde."
    think "Chambre sept. Un tissu sombre noué à la poignée. Signe ou habitude, je n'en sais rien."

    pause 0.4

    "Je m'arrête devant sa porte."

    think "A-t-elle envie de me parler ? Est-ce que quelqu'un en a envie ce matin ?"

    "Je frappe deux coups."

    play sound sfx_knock volume 8.0
    pause 1.0

    think "Rien."

    "Je frappe encore, plus fort."

    play sound sfx_knock volume 8.0
    pause 0.8

    "Un froissement, puis la porte s'entrouvre."

    play sound sfx_door volume 8.0

    $ showP("sael", "mefiant", 0.50)

    sael "..."

    think "Elle n'a pas l'air surprise. Comme si elle savait que ce serait moi."

    sael mefiant "Noam."

    noam "Tu n'as pas mangé non plus. Enfin… ce n'est pas pour ça que je suis là."

    sael "..."

    sael neutre "Qu'est-ce que tu viens chercher, Noam ?"

    think "Assez ouverte pour parler. Pas assez pour entrer."

    noam hesitation "Je pense qu'on devrait parler du vote. De demain."

    pause 0.3

    sael "Je savais que tu viendrais pour ça."

    "Elle s'écarte juste assez."

    sael "Entre. Les seuils ne sont pas faits pour les longues conversations."

    pause 0.3

    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    pause 0.6

    think "Le lit a été démonté. Planches au sol, une couette, puis du vide."
    think "Aux murs : ficelles, os, bois tressé. Des signes dans une langue que je ne sais pas lire."

    think "Ça ne ressemble pas à une chambre. Plutôt à un lieu qui refuse d'oublier."

    $ j50_sael_pnc_score = 0
    $ j50_sael_pnc_seen = []
    call _5_0_SAEL_PNC from _call_5_0_SAEL_PNC


    $ showP("noam", "hesitation", 0.25)
    noam "Tu as vraiment tout enlevé…"

    $ showP("sael", "neutre", 0.75)
    sael "Ce qui ne sert pas prend de la place. Et la place finit toujours par nous prendre quelque chose."

    noam "Et tout ça… les os, les fils…"

    think "Elle me regarde enfin. Ni vexée ni gênée. Fermée."

    sael "Dis ce que tu es venu dire. Le reste ne t'aidera pas."

    pause 0.3

    if j50_sael_pnc_score >= 3:
        noam reflexion "Tu n'as pas rendu cette chambre vide."
        noam "Tu l'as ramenée au sol."

        sael fatigue "..."
        sael "C'est moins faux que le reste."

    noam "Tu as encore réfléchi aux frontières. Enfin— je ne viens pas te demander de changer de camp."
    noam reflexion "Je veux comprendre où tu en es."

    sael mefiant "Tu veux comprendre, ou tu veux trouver l'endroit où pousser ?"

    noam "Pour toi, c'est la même chose."

    think "Elle incline la tête. Touché."

    $ showP("sael", "reflechit", 0.75)

    sael "Peut-être."
    sael reflexion "Mais ça ne change pas ma réponse."

    $ showP("noam", "reflexion", 0.25)

    noam "La libre circulation, ce sont aussi des gens de Limen qui pourraient travailler ailleurs."
    noam "Des familles séparées qui pourraient se retrouver. Enfin… ce n'est pas seulement une porte ouverte au danger."

    pause 0.3

    $ showP("sael", "desaccord", 0.75)

    sael "On en a déjà discuté."
    sael "Quand une barrière tombe, les gens ne deviennent pas libres. Ils courent. Ils poussent. Ils prennent avant d'être privés."
    sael "Ryn croit qu'il ouvre une porte."
    sael determine "Moi, je vois une digue qu'on casse."

    sael "Tu parles de familles, de travail, de passages. Moi, je vois le froid entrer et les corps se serrer aux grilles."
    sael "Je vois la faim choisir les plus lents. Limen tient parce que nous acceptons des rites durs."
    sael colere "Si je dois paraître cruelle pour que le sol tienne encore, alors je porterai ce mot."

    if j50_sael_pnc_score >= 4:
        noam reflexion "Tu ne votes pas contre les voyages."
        noam "Tu votes contre ce que tu crois être l'effondrement de Limen."

        sael fatigue "..."
        sael "C'est moins faux que le reste."

    sael determine "J'ai vu ce qui se passe quand une foule sent que la frontière ne répond plus."
    sael "J'ai vu la peur devenir une main qui tire. Je ne cherche pas à être aimée, Noam."
    sael colere "Je n'ai simplement pas oublié ce que survivre exige."

    think "Elle ne hausse pas le ton. Elle a déjà vécu cette conversation cent fois, sans moi."

    pause 0.4

    $ showP("noam", "inquiet", 0.25)

    noam "Tu voteras contre."

    sael raison "Oui."
    sael determine "Et rien ne me fera changer d'avis."

    pause 0.4

    think "Un oui simple, sec, sans appel."

    sael raison "Mara votera contre aussi. Nous en avons parlé hier soir."

    pause 0.3

    noam "Et Iris ?"

    sael "Va lui demander toi-même."
    sael mefiant "Mais je crois que tu connais déjà la réponse."

    think "Ce n'est pas une attaque. Seulement un fait posé entre nous comme une pierre froide."

    pause 0.5

    noam hesitation "Je me demande si..."

    think "La phrase n'a pas de fin. Moi non plus."

    pause 0.3

    noam "Non. Rien."

    think "Pas d'argument. Seulement un espoir diffus qui ne sait même plus se défendre."

    $ showP("sael", "fatigue", 0.75)

    sael "Tu n'étais pas obligé de venir. Cela ne changera rien."
    sael fatigue "Mais j'apprécie que tu aies essayé. Nous avons parlé sans ajouter une blessure aux autres."

    pause 0.4

    hide noam
    hide sael

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "Sael me raccompagne et referme sa porte."

    pause 0.6

    think "Sael contre. Mara contre."

    think "Et Iris… À quoi bon demander ? Deux non suffisent déjà à tuer le vote."

    "Je passe devant la chambre d'Iris."
    
    think "Et puis merde."

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 0.8

    play sound sfx_door volume 8.0
    $ showP("iris", "fatigue", 0.50)

    iris fatigue "Ah. Noam."

    $ showP("noam", "inquiet", 0.25)
    noam hesitation "Tu as une minute ?"

    think "Elle sort, bras croisés. Le sommeil ne lui a pas fait plus de cadeaux qu'à moi."

    iris "Si c'est pour le vote, épargne-nous l'introduction. Ma décision est prise."

    noam "Oui. Ça, j'avais compris."

    iris "Oui."

    pause 0.3

    iris triste "Je comprends l'idée : rendre aux gens la liberté d'aller où ils veulent. Très beau sur l'écran."
    iris triste "Mais sans plan, sans transition et avec ce groupe ? On n'ouvre pas des frontières. On lance une expérience sur des millions de cobayes."
    iris hesitation "Je ne cautionnerai pas cette mascarade."

    pause 0.3

    noam "Mais ne rien faire, c'est aussi—"

    iris colere "Aussi quoi ? Une décision ? Oui, merci, je connais le piège."
    iris colere "Dis-moi que j'ai tort. Avec des faits, si possible. Ça nous changera."

    think "Je comprends sa logique. C'est justement ce qui me révulse."

    noam "Je ne peux pas. Enfin… pas avec des faits."
    noam "Mais je déteste qu'on transforme notre peur d'échouer en raison de ne rien tenter."

    iris triste "Alors déteste. Moi, je voterai avec ce qu'on sait."

    "Iris referme la porte."

    hide iris
    hide noam

    jump _5_0_DISCUSSION_SAEL


label _5_0_DISCUSSION_SAEL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Deux portes fermées. Les murs métalliques absorbent le reste."

    pause 0.5

    think "Douze représentants. Un seul non suffit. J'en ai déjà deux."

    pause 0.4

    think "C'est déjà perdu."

    think "La conclusion arrive sans drame, comme le résultat banal d'un calcul."

    think "Julian s'est enfermé dans sa chambre."
    think "Et moi, je glane des certitudes sur notre échec. Travail essentiel."

    pause 0.4

    "Je m'adosse au mur."

    think "Je me demande si ce vote a encore un sens."
    think "Si quelque chose peut encore être rattrapé."
    think "Participer, est-ce cautionner ce système ? Ou seulement le traverser pendant qu'il nous démonte ?"
    think "Puis recommencer. Encore. Encore."

    pause 0.6

    think "J'expire lentement. La version socialement acceptable d'un cri."

    pause 0.5

    think "Il reste quoi ? Aujourd'hui. Un petit espace avant que tout se referme."

    think "Je ne sais pas ce que ça donnera."
    think "Mais il me semble que je ne peux pas juste attendre que ça s'effondre."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    show screen day3_codex_logo

    think "Le dossier range nos positions avec une propreté obscène."

    jump _5_0_TEMPS_LIBRE_1

label _5_0_TEMPS_LIBRE_1:
    call START_FREE_TIME("_5_0_APRES_TEMPS_LIBRE_1") from _call_START_FREE_TIME_2

label _5_0_APRES_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 0.8

    think "Je marche sans direction. Le mouvement donne à l'indécision une allure d'activité."
    think "Le Conclave paraît désert, comme un bateau entre deux vagues."

    pause 0.5

    "La salle commune est vide : une chaise renversée, un plateau abandonné."

    think "Je devrais faire quelque chose. Convaincre qui ? De quoi, exactement ?"

    pause 0.5

    think "Les convictions ne se déplacent pas. On s'assoit à côté, on écoute, on espère qu'elles bougent seules."

    think "Julian."
    think "Il doit encore être dans sa chambre."
    think "Kael a dit qu'il avait tenté d'aller le voir hier soir."
    think "Qu'il lui avait répondu de le laisser tranquille."

    "Je m'arrête."

    think "Et la salle d'observation."
    think "Je n'y suis pas retourné depuis un moment."
    think "Les écrans montrent l'état des districts. Peut-être quelque chose de concret, qui résiste enfin à l'abstraction des votes."

    pause 0.4

    jump _5_0_CHOIX_PRINCIPAL


label _5_0_CHOIX_PRINCIPAL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.3

    think "Deux options. C'est déjà une de trop."

    menu:
        "Aller frapper à la porte de Julian.":
            $ doplleganger = 0
            jump _5_0_0_JULIAN

        "Aller à la salle d'observation.":
            $ doplleganger = 1
            jump _5_0_1_OBSERVATION


label _5_0_0_JULIAN:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    $ doplleganger = 0
    think "Chambre quatre. Julian."
    think "Aucune décoration, aucune trace de lui. Il veut exister partout, sauf sur sa propre porte."

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 1.0

    think "Rien."

    "Je frappe encore."

    play sound sfx_knock volume 8.0
    pause 0.8

    think "Du mouvement. Pas quelqu'un qu'on réveille : quelqu'un qui choisit son temps d'entrée."

    noam "Julian. C'est moi."

    pause 0.8

    play sound sfx_door volume 8.0

    $ showP("julian", "neutre", 0.65)
    $ showP("noam", "neutre", 0.30)

    "La porte s'ouvre."

    think "Julian n'a l'air ni détruit ni même atteint."

    julian sourire "Noam."
    julian taquin "Tu viens constater les dégâts ?"

    noam hesitation "Je venais surtout voir comment tu allais."

    julian sourire "Oh."
    julian taquin "C'est presque touchant."

    "Il se pousse."
    think "Cette fois, l'invitation est réelle. Ou parfaitement jouée."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    $ showP("julian", "sourire", 0.65)
    $ showP("noam", "reflexion", 0.30)

    think "La chambre est trop propre. Une pièce témoin où rien ne dépasse, rien ne vit."

    julian neutre "Alors ?"
    julian sourire "Tu veux me dire de ne pas prendre les résultats comme quelque chose de personnel ?"
    julian taquin "Ou m'offrir une de tes phrases calmes, prudentes et miraculeusement sans conclusion ?"

    noam "Disons que je ne suis pas vraiment venu avec un dialogue préétabli."

    julian rire "Moi si."

    pause 0.4

    think "Le sourire dit plaisanterie. Ses yeux, non."

    noam reflexion "Tu n'as pas l'air aussi abattu que ce matin."

    julian sourire "Parce que je ne le suis pas."

    "Julian pose la main sur le brouilleur."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    think "Le grésillement disparaît. La caméra pivote. Julian entre en scène."

    $ showP("julian", "triste", 0.72)

    julian triste "J'avoue que c'est difficile. Julian croyait sincèrement que nous pouvions accomplir quelque chose de grand."
    julian decu "Et, au moment décisif, vous avez choisi la peur."

    think "Il baisse les yeux juste assez. Même sa douleur connaît son cadre."

    noam reflexion "Arrête de..."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    noam reflexion "...jouer la comédie."

    $ showP("julian", "rire", 0.72)

    julian rire "Évidemment que je joue."
    julian sourire "Quand Kami regarde, il faut lui donner quelque chose qu'elle ne puisse pas monter contre nous."

    noam desaccord "Donc tout ça, c'était pour l'image."

    julian taquin "L'image, c'est ce qui reste quand une idée échoue. Et ce qui permet à la suivante d'exister."
    julian sourire "Et le plus beau, c'est que même un échec peut me servir."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    $ showP("julian", "triste", 0.72)

    julian triste "Il faut accepter la défaite avec dignité."
    julian decu "Mais Julian portera ce vote jusqu'au bout."
    julian triste "Même si certains préfèrent avoir peur."

    think "La phrase est pour moi. Le regard, pour la caméra."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    $ showP("julian", "sourire", 0.65)

    julian sourire "Voilà."
    julian taquin "Public et privé. Deux langues, même bouche. Le talent consiste à ne mordre personne par accident."

    noam reflexion "Et toi, dans tout ça ?"

    julian neutre "Moi ?"
    julian sourire "Julian fait ce qu'il faut pour rester utile."

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
            julian taquin "Trop simple."

    julian sourire "Qu'il passe ou qu'il tombe, ce vote laisse quelque chose à Julian."
    julian idee "S'il passe, j'ai porté une idée décisive."
    julian idee "S'il tombe, j'ai combattu votre peur du changement."
    julian rire "Dans les deux cas, l'histoire sait où me placer."

    menu:
        "Tu veux être indispensable.":
            $ j50_julian_fissure += 1
            noam determine "Tu veux être indispensable."
            julian inquiet "Ce n'est pas un défaut."

        "Tu veux prouver que les autres sont lâches.":
            $ j50_julian_fissure -= 1
            noam "Tu veux prouver que les autres sont lâches."
            julian sourire "Je n'ai pas besoin de le prouver. Ils le font très bien seuls."

        "Tu veux juste gagner.":
            noam "Tu veux juste gagner."
            julian neutre "Gagner quoi ? Tu vois, même toi tu ne sais pas."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3

    $ showP("julian", "triste", 0.72)

    julian triste "Je crois encore que ce vote peut dire quelque chose de nous."
    julian "Si nous reculons maintenant, alors nous acceptons que Limen reste à genoux."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.3

    $ showP("julian", "sourire", 0.65)

    julian sourire "C'est fort, non ?"
    julian taquin "Simple. Clair. Prêt pour les archives."

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

        $ showP("julian", "inquietude", 0.65)
        julian inquiet "..."
        julian "C'est une façon remarquablement injuste de résumer une ambition sincère."

        noam "Non."
        noam "C'est une façon très précise."

        $ showP("julian", "peur", 0.65)
        julian peur "Tu crois que c'est drôle ?"
        julian inquiet "Tu crois que je n'ai jamais pensé à ce qui reste quand personne n'a plus besoin de moi ?"

    elif j50_julian_fissure >= 1:
        noam reflexion "Tu veux être celui autour de qui le vote s'organise."
        noam "Pas seulement celui qui vote pour."

        $ showP("julian", "reflexion", 0.65)
        julian reflexion "Peut-être."
        julian sourire "Ou peut-être as-tu besoin que Julian soit plus simple qu'il ne l'est."

    else:
        noam desaccord "Tu joues avec tout le monde."

        $ showP("julian", "sourire", 0.65)
        julian sourire "Et toi, tu me donnes exactement la scène qu'il me fallait."
        julian taquin "L'indignation calme. Très propre."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.3

    $ showP("julian", "sourire", 0.72)

    julian sourire "Merci d'être venu, Noam."
    julian triste "Même nos désaccords prouvent que ce vote compte encore."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.3

    noam "Tu viens encore de corriger ton image."

    julian sourire "Bien sûr."
    julian taquin "Pourquoi est-ce que j'arrêterais juste avant la fin ?"

    think "Brouilleur actif, il paraît plus vrai. Caméra active, il devient plus net."
    think "Je ne sais pas quelle version est la plus dangereuse — ni laquelle est vraiment Julian."

    hide noam
    hide julian

    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    $ doplleganger = 1
    think "Kami ne nous interdit pas les données. Regarder le vide en face suffit probablement à décourager les curieux."

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 0.8

    think "Derrière les baies vitrées, un silence vieux de milliards d'années ignore nos votes et notre survie."

    $ showP("elias", "neutre", 0.75)

    "Elias est assis à la console, une tasse à la main, les yeux sur les données des districts."

    elias neutre "Noam ?"

    think "Il ne s'est même pas retourné."

    elias "Qu'est-ce que tu fais là ?"

    $ showP("noam", "neutre", 0.25)

    noam "C'est le seul endroit qui soit calme aujourd'hui."

    $ showP("elias", "neutre", 0.75)
    elias "Ouais."
    elias "La cafétéria, c'était chaud. Genre vraiment chaud."

    think "Il boit sans quitter l'écran."

    $ showP("elias", "neutre", 0.75)
    elias "Regarde ça."

    "Des chiffres, des courbes et des noms défilent sur le panneau droit."

    $ showP("noam", "reflexion", 0.25)

    noam "Il va falloir m'expliquer. Enfin… ces chiffres disent quoi ?"

    elias "Là. Regarde."

    "Il pointe du doigt une liste de noms qui défile."

    elias inquiet "C'est les noms des gens qui ont merdé. Enfin, c'est ce que l'écran dit."
    elias "À côté, t'as la règle qu'ils ont cassée."

    think "Vol. Bagarre. Menace. La liste est longue et chaque ligne revient aux rations."
    think "Ils veulent manger. Le système, lui, compte les infractions."

    pause 0.4

    "Je me penche vers la courbe de Limen."

    pause 0.3

    elias inquiet "Attends, regarde ça—"

    "Son coude accroche la tasse."
    play sound sfx_drop

    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")

    "Le café se répand sur les touches et le panneau latéral."

    elias "Et merde ! C'est chaud, c'est chaud—"

    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress

    if j50_coffee_trace_score >= 0.82:
        think "Mes doigts frôlent la porcelaine. Assez pour changer l'angle, pas pour la retenir."
    elif j50_coffee_trace_score >= 0.35:
        think "Trop tard. Ma main traverse l'endroit où la tasse n'est déjà plus."
    else:
        think "Trop vite. Mon poignet heurte la console et la tasse part plus loin."

    "Elias récupère sa tasse vide. Le café ruisselle entre les touches."

    "Un voyant passe au rouge. La console siffle."

    noam "C'est moi qui— j'ai tendu le bras, enfin, j'ai dû te—"

    elias inquiet "Non, c'était ma tasse. Mon coude. Ma connerie. C'est clair."

    "Un voyant orange s'allume. Une fumée grise monte de la grille latérale."

    elias inquiet "OK. Bon. C'est pas mort."
    elias "Enfin… pas encore. C'est chaud."

    "Un claquement mécanique nous fait nous retourner. La porte est verrouillée."
    think "VERROUILLAGE SÉCURITÉ — ANOMALIE DÉTECTÉE. Pour une fois, l'écran résume bien la situation."

    pause 0.5

    elias panique "Ah. C'est chaud."

    noam peur "La porte est bloquée ?"

    elias inquiet "La salle s'est verrouillée."
    elias "Sûrement une sécurité à la con. Quand un truc fume, ça ferme tout pour éviter que le feu sorte."
    elias "Ou pour éviter qu'on sorte. J'sais plus."

    noam hesitation "En principe."

    elias "Ouais."
    elias fatigue "En principe."

    pause 0.4

    think "La fumée reste fine. La porte, fermée. L'espace ne juge même pas utile de réagir."

    noam "Combien de temps avant que ça devienne vraiment dangereux ?"

    $ showP("elias", "panique", 0.75)
    elias panique "Putain, putain, putain…"
    elias inquiet "Noam, viens là. Tu vas relier les fils."
    elias "Même couleur ensemble. Tu réfléchis pas. Tu relies."

    "Elias arrache le panneau. Des grappes de fils pendent sous la console."

    call screen j50_wire_minigame

    if j50_wire_success >= 12:
        $ j50_kamyz_bonus = 40
    elif j50_wire_success >= 8:
        $ j50_kamyz_bonus = 25
    elif j50_wire_success >= 5:
        $ j50_kamyz_bonus = 15
    else:
        $ j50_kamyz_bonus = 5

    $ player_kamyz += j50_kamyz_bonus
    "Kamyz bonus obtenus : [j50_kamyz_bonus]"

    if j50_wire_errors > 0:
        elias colere "Non, pas celui-là !"
        elias "Putain… Bon. C'est grave, mais si je le dis trop fort ça va pas aider."

    if j50_wire_success >= 8:
        elias rire "T'as fait ça mieux que moi. C'est bien pour nous, mais c'est chaud pour ma fierté."
    elif j50_wire_success >= 5:
        elias fatigue "C'est moche. Mais ça tient."
    else:
        elias inquiet "C'est pété de partout. Mais ça fume moins. Franchement, on prend."

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")

    elias "La ventilation tourne. On va pas étouffer."
    elias fatigue "Mais ouais… on est bloqués un moment. C'est chaud, cette salle est censée observer les problèmes, pas en devenir un."

    "Elias s'assoit par terre, loin du panneau."

    elias neutre "Tu voulais regarder les chiffres de Limen, non ?"

    think "Il désigne le seul écran qui fonctionne encore."

    elias fatigue "On a nulle part où aller. Autant en parler."

    noam "Ce n'est pas exactement le contexte idéal pour parler du vote. Enfin…"

    elias rire "Non."
    elias "Les bons moments, ici, ça existe plus vraiment."

    pause 0.5

    "Je m'assieds à côté de lui, dos au mur."

    elias inquiet "Tu crois que ça va passer, le vote ?"

    noam "Tu veux savoir si ça peut encore passer. Enfin… je ne vois pas ce qui changerait avant demain."

    pause 0.3

    elias inquiet "Sael votera contre."
    elias "C'est sûr. Elle croit vraiment que ça ramènera la guerre."

    noam "Elle me l'a dit ce matin."
    noam hesitation "Mara aussi. Et Iris."

    elias "… Ah."

    elias fatigue "Alors c'est foutu. C'est chaud."

    noam "Peut-être pas…"
    think "Le mensonge manque de conviction. Elias a la gentillesse de ne pas le relever."

    pause 1.0

    call show_custom_title("Après plusieurs heures") from _call_show_custom_title

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 3.0

    "Les voyants passent à l'orange. Le panneau de la porte clignote."

    play sound "sound/sfx_door.ogg"

    "La porte s'ouvre dans un déclic."

    $ showP("elias", "fatigue", 0.75)

    elias fatigue "Ah. Libérés. C'était moins long que prévu."

    "Elias se relève en s'étirant."

    elias "Je vais voir si j'ai cramé un truc important. Enfin, plus important que la porte."

    think "Quelques touches collent. L'écran latéral est mort."

    elias neutre "Rien de trop grave. Juste une caméra de relevé."
    elias fatigue "C'est de la merde, mais ça se répare. Moi aussi, en général."

    noam reflexion "Kami va faire une remarque. La seule question, c'est combien."

    elias rire "Probablement."
    elias "Elle fait des remarques sur tout. Même quand personne lui parle."

    hide noam
    hide elias

    think "Nous nous séparons dans le couloir, avec un vote condamné et une caméra en moins. Bilan mitigé."

    jump _5_0_FIN_JOURNEE


label _5_0_FIN_JOURNEE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    think "L'après-midi se cache derrière un calme de façade : quelques échanges, un repas sans goût, des conversations sans fin."

    think "Tomas me salue sans parler. Nyra calcule sans m'inclure. Je leur rends la pareille."

    pause 0.6

    think "La journée finit comme elle a commencé : lourde, lente, sans catastrophe et sans ouverture."

    think "Kami ne fait aucune annonce. Son silence ressemble à une attente que nous décevons encore."

    pause 0.5

    "Je rentre dans ma chambre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    think "Je m'assieds au bord du lit, pas encore prêt à m'allonger."

    pause 0.5

    think "Tout le monde a raison, d'une certaine façon. Et demain, le vote sera quand même contre."

    pause 0.4

    $ blink()
    "Je m'allonge."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    think "Lumière bleue. Plafond muet. Au moins deux choses restent fiables."

    $ blink()

    think "Une nuit. Un matin. Puis le vote."

    think "Que peut-on encore faire ? Peut-être que « faire » n'est plus le bon mot."
    think "Peut-être qu'il faut seulement rester là, sans solution, pendant que quelque chose se casse."

    pause 0.5

    $ blink()

    "Une porte s'ouvre dans le couloir. Des pas discrets passent devant ma chambre."
    think "Quelqu'un ne dort pas. Ou fait semblant."

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

    pause 0.4

    think "Je ne sais pas encore ce que ça veut dire."

    $ blink()
    pause 1.5

    think "Demain sera difficile. J'y serai quand même."
    "Le sommeil arrive sans fracas."

    $ current_day = 6
    pause 1.0

    if doplleganger == 0:
        call end_day("6") from _call_end_day_6
        jump _6_0_0_REVEIL_CHAMBRE

    else:
        call end_day("6") from _call_end_day_7
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
