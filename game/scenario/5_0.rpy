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

    if j50_sael_pnc_score >= 3:
        imagebutton:
            idle "images/background/interact/retour.png"
            hover "images/background/interact/retour_hover.png"
            focus_mask True
            xpos 0
            ypos 0
            at cover_screen
            action Return("finish")

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
    "J'ouvre les yeux sans avoir l'impression d'avoir dormi."

    "Ma nuque me lance."
    "Mes épaules sont dures."
    "Cette sensation poisseuse des nuits où le corps s'est allongé, mais où la tête a continué à tourner."

    pause 0.5

    $ blink()
    "Je tourne la tête vers le plafond."
    "Silence."
    "Pas un vrai silence apaisant."
    "Un silence froid. Un silence qui attend quelque chose."

    pause 0.6

    think "Le vote."
    think "Celui d'il y a deux jours."
    think "Et celui qui arrive."

    "Mon ventre se serre presque aussitôt."
    "Depuis l'annonce de ce vote sur les frontières, tout s'est déjà figé."
    "Les regards comme les discussions."
    "Même les moments où quelqu'un essaie de plaisanter."
    "Rien ne tient."

    $ blink()

    think "Ça ne passera pas."
    think "Personne n'y croit plus vraiment."

    "Je me redresse lentement sur le lit."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "J'ai les traits lourds."
    "Les yeux qui piquent."
    "L'impression d'avoir vieilli de plusieurs jours pendant la nuit."

    pause 0.6

    "Je reste assis au bord du lit."
    "Les pieds posés au sol."
    "Le dos courbé."
    "Comme si me lever demandait déjà une décision, un lourd effort à faire."

    think "Si je vais à la cafétéria, ce sera pareil qu'hier."
    think "Des gens qui ne parlent pas."
    think "Des regards qui fuient au loin."
    think "Et au fond de chaque tête, la même certitude non dite..."
    think "Ce vote va échouer."

    pause 0.7

    "Je déteste cette sensation."
    "Pas seulement la peur de mal faire."
    "Pas seulement la fatigue."
    "Cette espèce d'impuissance molle."
    "Ce moment où rien n'a encore explosé, mais où tout le monde agit déjà comme après la casse."

    "Je me rends compte que j'ai parlé à voix haute après coup."

    pause 0.5

    "Je baisse les yeux vers mes mains."
    "Elles sont immobiles, elles ne tremblent même pas."

    think "Non."
    think "C'est trop facile."
    think "Si je commence comme ça, la journée est déjà morte."

    "Je serre un peu les doigts."
    "Pas assez pour me faire mal."
    "Juste assez pour sentir que je suis là, bien réveillé."

    pause 0.5

    think "Le vote n'a peut-être aucune chance de passer."
    think "L'ambiance est glaciale."
    think "Sael est fermée."
    think "Julian se mure dans sa chambre."
    think "Et moi..."
    think "Moi, j'ai même pas de bonne réponse."

    "Mais je n'abandonnerai pas."

    pause 0.6

    "Le pire, c'est peut-être ça."
    "Le fait que tout le monde ait une part de raison."
    "Sael n'a pas tort."
    "En fait, personne n'a tort..."
    "Et pourtant, à la fin, il faudra quand même trancher."
    "Comme si une décision acceptable était encore possible."
    "Face tu gagnes, pile je perds."

    pause 0.5

    "Je me lève enfin."
    "Mes jambes protestent un peu."
    "Je fais deux pas dans la chambre."

    "L'air me paraît plus froid que d'habitude."
    "Ou alors c'est juste moi."

    play sound sfx_announce
    pause 0.7

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour mes petits ! Jour cinq, et ça fleure déjà le drame."
    kami "Ne vous inquiétez pas : votre prochaine chance de tout rater arrive dans vingt-quatre heures !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rappel amical : le vote sur la libre circulation aura lieu demain."
    kami "Vous aurez donc une nuit de plus pour vous convaincre que vous êtes capables de décider de quelque chose ensemble."
    kami "Comme c'est amusant !."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "La cafétéria est ouverte. Vos rations sont prêtes. Les mêmes qu'hier."
    kami "Et comme toujours, j'observerai avec beaucoup d'intérêt ce que vous allez faire de cette belle matinée ensoleillée."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oups, j'oubliais, vous ne pouvez pas voir la lumière du soleil depuis le Conclave !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "L'écran s'éteint sous les rires criards de Kami."
    "Le silence retombe doucement."

    pause 0.8

    think "La cafétéria."

    "J'imagine l'ambiance."

    think "Est-ce que j'ai vraiment envie de traverser ça ce matin?"

    pause 0.5

    "Je regarde le bout de pain posé sur ma table de nuit."
    "Dur. Sec. Ça fera très bien l'affaire."

    pause 0.3

    jump _5_0_SKIP_CAFETERIA


label _5_0_SKIP_CAFETERIA:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    "Je prends le pain."
    "Je l'examine une seconde."
    "Il est vraiment sec."

    think "Je me demande si quelqu'un remarquera que je ne suis pas venu à la cafétéria."

    "Je mords dedans."
    "Ça craque sous les dents."
    "Un goût de rien ou presque."
    "Juste d'un bout de pain déjà sec et dur."

    pause 0.4

    "Je mastique lentement et difficilement."
    "Debout. Seul."
    "Dos à la porte de ma chambre."

    "Il y a quelque chose d'étrangement honnête là-dedans."
    "Pas de conversation à gérer."
    "Pas de regard à soutenir."
    "Pas d'hypocrisie."
    "Juste moi et ce pain, sans témoin."

    think "C'est mieux comme ça, un peu plus reposant."
    think "Au moins pour cette heure-là."

    pause 0.7

    "Je finis le morceau."
    "J'essuie ma main sur mon pantalon."

    "J'entends pendant ce temps là quelques pas dans le couloir."
    "Quelques voix étouffées."
    "Le groupe qui se lève, qui se déplace, qui se retrouve autour d'un plateau."
    "Qui vit ou qui essaye."
    "Je ne me sens pas capable de les rejoindre."
    "Pas dans cet état."
    "Pas avant d'avoir réfléchi à ce que je peux encore faire."

    think "Sael. Si elle vote contre, c'est foutu."
    think "Il faut que je lui parle."
    think "Avant que ce soit trop tard."

    pause 0.5

    "Je sais qu'elle est encore là."
    "Je l'ai entendue hier soir traverser le couloir, rentrer dans sa chambre, fermer sa porte."
    "Elle avait essayé d'être discrète."
    "Ce qui est, à sa façon, encore moins discret."

    pause 0.4

    "Je soupire."
    "Je jette un dernier regard à ma chambre."

    think "Il me semble qu'il faut au moins essayer."

    stop music fadeout 1.2

    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 0.8

    "Le couloir est presque vide."
    "Quelques silhouettes au loin, qui se dirigent vers la cafétéria sans se presser."
    "Personne ne me regarde, ils vaquent tous à leur occupation."

    "Je marche vers la rangée de portes."
    "Je sais laquelle est la sienne."
    "Chambre 7."
    "Elle a mis un petit morceau de tissu sombre sur la poignée, je ne sais pas vraiment ce que ça veut dire."
    "Je n'ai jamais su si c'était pour signaler quelque chose ou juste une habitude."

    pause 0.4

    "Je m'arrête devant."
    "J'hésite un instant."

    think "Je me demande si elle a envie de me parler."
    think "Je me demande si quelqu'un a envie de me parler ce matin."

    "Je frappe. Deux coups. Pas trop forts."

    play sound sfx_knock volume 8.0
    pause 1.0

    "Silence."

    "Je frappe encore. Un peu plus fort."

    play sound sfx_knock volume 8.0
    pause 0.8

    "Un mouvement derrière la porte."
    "Un bruit de tissu."
    "Puis la porte s'entrouvre."

    play sound sfx_door volume 8.0

    $ showP("sael", "mefiant", 0.50)

    sael "..."

    "Elle me regarde."
    "Elle n'a pas l'air particulièrement surprise."
    "Comme si elle savait que ce serait moi."

    sael mefiant "Noam."

    noam "Ce que j'entends, c'est que tu n'as pas encore mangé non plus."

    sael "..."

    sael neutre "Qu'est-ce que tu veux ?"

    "Elle n'ouvre pas vraiment la porte."
    "Juste assez pour parler."
    "Pas assez pour m'inviter à entrer."

    noam hesitation "Je pense qu'on devrait parler."
    noam "Du vote."
    noam "De demain."

    pause 0.3

    sael "Je savais que c'était pour ça."

    "Elle s'écarte un peu."
    "On ne peut pas vraiment dire qu'elle m'accueille. Elle semble juste tolérer ma présence."

    sael "Rentre."

    pause 0.3

    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    pause 0.6

    "Je m’attendais à une chambre froide."
    "Pas à... ça."
    "Le lit a disparu."
    "Ou plutôt non. Il a été démonté."

    "Des planches posées au sol."
    "Une simple couette."
    "Rien de plus."

    "Le reste de la pièce est presque vide."

    "Quelques objets pendent au mur."
    "Des ficelles, des os, du bois tressé, des symboles que je ne comprends pas."

    think "On dirait pas une chambre."
    think "C'est quoi ce truc ?!"

    $ j50_sael_pnc_score = 0
    $ j50_sael_pnc_seen = []
    call _5_0_SAEL_PNC from _call_5_0_SAEL_PNC


    $ showP("noam", "hesitation", 0.25)
    noam "T’as vraiment tout enlevé..."

    $ showP("sael", "neutre", 0.75)
    sael "Ce qui ne sert pas prend de la place."

    noam "Et tout ça, là... c’est ..."

    "Elle me regarde enfin."
    "Pas vexée. Pas gênée. Juste fermée."

    sael "Dis-moi ce que t'as à dire. Rien d'autre."

    pause 0.3

    if j50_sael_pnc_score >= 3:
        noam reflexion "Tu n'as pas rendu cette chambre vide."
        noam "Tu l'as ramenée au sol."

        sael fatigue "..."
        sael "C'est moins faux que le reste."

    noam "Je me demande si tu as encore réfléchi à la question des frontières."
    noam reflexion "Pas pour te convaincre de changer de camp. Juste... pour comprendre où tu en es."

    sael mefiant "Tu veux comprendre, ou tu veux me faire changer d'avis ?"

    noam "Ce que j'entends, c'est que pour toi c'est la même chose."

    "Sael penche légèrement la tête."

    $ showP("sael", "reflechit", 0.75)

    sael "Peut-être."
    sael reflexion "Mais ça ne change pas ma réponse."

    $ showP("noam", "reflexion", 0.25)

    noam "Il me semble que la libre circulation ..."
    noam "C'est des gens de Limen qui pourraient aller chercher du travail ailleurs."
    noam "Des familles séparées qui pourraient se retrouver."

    pause 0.3

    $ showP("sael", "desaccord", 0.75)

    sael "On en a déjà discuté."
    sael "Quand une barrière tombe, les gens ne deviennent pas libres."
    sael "Ils courent."
    sael "Ils poussent."
    sael "Ils prennent ce qu'ils peuvent avant que quelqu'un d'autre le prenne."
    sael "Ryn croit qu'il ouvre une porte."
    sael determine "Moi, je vois une digue qu'on casse."

    sael "Tu parles de familles, de travail, de passages."
    sael "Moi, je vois le froid qui rentre, les corps serrés aux grilles, la faim qui choisit les plus lents."
    sael "Limen tient parce qu'on accepte des rites durs."
    sael colere "Et si je dois passer pour cruelle pour que le sol tienne encore, je passerai pour cruelle."

    if j50_sael_pnc_score >= 4:
        noam reflexion "Tu ne votes pas contre les voyages."
        noam "Tu votes contre ce que tu crois être l'effondrement de Limen."

        sael fatigue "..."
        sael "C'est moins faux que le reste."

    sael determine "J'ai vu ce qui se passe quand une foule sent que la frontière ne répond plus."
    sael "J'ai vu la peur devenir une main qui tire."
    sael "Contrairement à ce que tu crois, je ne cherche pas à être aimée."
    sael colere "Je n'ai simplement pas oublié ce que c'est que survivre."

    "Elle dit ça posément."
    "Sans colère."
    "Comme quelqu'un qui a déjà eu cette conversation dans sa tête cent fois, et qui n'attend plus rien de la vraie."

    pause 0.4

    $ showP("noam", "inquiet", 0.25)

    noam "Ce que j'entends, c'est que tu voteras contre."

    sael raison "Oui."
    sael determine "Et rien ne me fera changer d'avis."

    pause 0.4

    "Le mot reste là."
    "Simple. Sec."
    "Sans appel."

    sael raison "Et Mara votera contre aussi. On en a parlé hier soir."

    pause 0.3

    noam "Et Iris ?"

    sael "Va lui demander toi-même."
    sael mefiant "Mais je crois que tu connais déjà la réponse."

    "Je reste sans répondre."
    "Ce n'est pas une attaque de sa part."
    "C'est juste un fait qu'elle pose là, entre nous deux, comme une pierre froide sur une table."

    pause 0.5

    noam hesitation "Je me demande si..."

    "Je m'arrête."

    pause 0.3

    noam "Non. Rien."

    "Je n'ai pas fini ma phrase parce que je n'avais rien à mettre dedans."
    "Pas d'argument solide."
    "Juste cette espèce d'espoir diffus qui ne ressemble même plus à grand-chose."

    $ showP("sael", "fatigue", 0.75)

    sael "Tu n'étais pas obligé de venir."
    sael "Ça ne changera rien."
    sael fatigue "Mais... j'apprécie que tu aies essayé."
    sael fatigue "Au moins on discute sans s'insulter."

    pause 0.4

    hide noam
    hide sael

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "Sael me raccompagne sans un mot puis referme sa porte derrière moi."
    "Le couloir est silencieux."

    pause 0.6

    think "Sael votera contre."
    think "Mara votera contre."

    think "Et Iris... En fait est-ce que ça vaut le coup d'aller lui demander ?"
    think "Avec deux voix contre, c'est certain."
    think "Le vote échouera quoi qu'il arrive."

    "Je fais quelques pas puis passe devant la chambre d'Iris."
    
    think "Oh et puis merde !"

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 0.8

    play sound sfx_door volume 8.0
    $ showP("iris", "fatigue", 0.50)

    iris fatigue "Ah. Noam."

    $ showP("noam", "inquiet", 0.25)
    noam hesitation "Tu as une minute ?"

    "Elle sort dans le couloir, les bras croisés sur elle-même."
    "Elle a l'air d'avoir mal dormi, elle aussi."

    iris "Si c'est pour le vote..."
    iris fatigue "Je sais déjà ce que je vais faire."

    noam "Ce que j'entends, c'est que ta décision est prise."

    iris "Oui."

    pause 0.3

    iris triste "Je comprends le débat, vraiment."
    iris triste "Le fait qu'il faut rendre aux gens la liberté d'aller où ils veulent."
    iris triste "Mais on y arrivera pas, pas avec cet état d'esprit."
    iris "Alors je ne vais pas perdre mon temps à essayer de faire quelque chose."
    iris hesitation "Je ne vais pas participer à cette mascarade. Ça a déjà trop duré."

    pause 0.3

    noam "Non mais tu..."

    iris colere "Quoi ?!"
    iris colere "Dis-moi que j'ai tort ?!"

    "Je ne sais pas quoi lui dire."
    "Je comprends sa logique."
    "Mais quelque chose en moi est révulsé à l'idée de ne rien faire."

    noam "Rien..."
    noam "C'est toi qui voit."

    iris triste 'Encore heureux.'

    "Sur ces mots, elle referme la porte derrière elle."

    hide iris
    hide noam

    jump _5_0_DISCUSSION_SAEL


label _5_0_DISCUSSION_SAEL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je reste immobile dans le couloir vide."
    "La porte d'Iris est refermée."
    "Celle de Sael aussi."
    "Les murs métalliques absorbent tout."

    pause 0.5

    "Je n'ai même pas besoin de compter mentalement."
    "Douze représentants. Un seul contre et c'est foutu."
    "On a déjà minimum deux contre."

    pause 0.4

    think "C'est déjà perdu."

    "Cette pensée arrive sans drama."
    "Calme. Presque comme une évidence que je savais déjà."
    "Comme quand on calcule une somme et que le résultat ne surprend personne."

    think "Julian s'est enfermé dans sa chambre."
    think "Et moi... Je suis là à essayer de glaner quelques infos."

    pause 0.4

    "Je m'adosse au mur du couloir."
    "Le métal est froid dans mon dos."

    think "Je me demande si ce vote a encore un sens."
    think "Si quelque chose peut encore être rattrapé."
    think "Est-ce que participer c'est cautionner ce système foireux ?"
    think "Ou si on va juste... traverser ça."
    think "Se faire démolir lentement en regardant chacun voter dans son coin."
    think "Et recommencer, encore... Encore... Encore..."

    pause 0.6

    "Je pousse un souffle par le nez."
    "Long. Contrôlé."
    "Le genre de souffle qu'on fait quand on évite de crier dans un couloir."

    pause 0.5

    "Il reste quoi ?"

    "Il reste aujourd'hui."
    "Ce matin. Cet après-midi."
    "Ce petit espace avant que tout se referme une fois encore et qu'on passe pour des cons."

    think "Je ne sais pas ce que ça donnera."
    think "Mais il me semble que je ne peux pas juste attendre que ça s'effondre."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    show screen day3_codex_logo

    "Le dossier du vote reste accessible sur ma tablette."
    "Les positions y sont rangées trop proprement pour ce qu'elles représentent."

    jump _5_0_TEMPS_LIBRE_1

label _5_0_TEMPS_LIBRE_1:
    call START_FREE_TIME("_5_0_APRES_TEMPS_LIBRE_1") from _call_START_FREE_TIME_2

label _5_0_APRES_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 0.8

    "Je continue à déambuler dans le couloir."
    "Sans vraiment avoir de direction précise."
    "Juste le mouvement pour ne pas rester figé et seul."

    "Les autres sont probablement encore à la cafétéria."
    "Ou retournés dans leurs chambres."
    "Le Conclave a quelque chose de désert dans ces moments-là."
    "Comme un bateau entre deux vagues."

    pause 0.5

    "Je passe devant la salle commune."
    "Elle est vide."
    "Une chaise est renversée près d'une table comme si quelqu'un s'était battu."
    "Un plateau est resté là, discret, pas débarrassé."

    think "Il me semble que je devrais faire quelque chose."
    think "Mais je ne sais vraiment pas quoi."
    think "Convaincre qui ? De quoi faire exactement ?"

    pause 0.5

    "Le problème, avec les convictions des autres, c'est qu'on ne peut pas vraiment les déplacer."
    "On peut juste... s'asseoir à côté d'elles."
    "Les écouter."
    "Et espérer que ça bouge un peu."

    think "Julian."
    think "Il doit encore être dans sa chambre."
    think "Kael a dit qu'il avait tenté d'aller le voir hier soir."
    think "Qu'il lui avait répondu de le laisser tranquille."

    "Je m'arrête."

    think "Et la salle d'observation."
    think "Je n'y suis pas retourné depuis un moment."
    think "Il y a des écrans qui montrent l'état des districts."
    think "Peut-être qu'il y a quelque chose à comprendre là-bas..."
    think "Quelque chose de concret, qui résiste à l'abstraction des votes."

    pause 0.4

    jump _5_0_CHOIX_PRINCIPAL


label _5_0_CHOIX_PRINCIPAL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.3

    "Je reste planté là une seconde."
    "Deux options, pas plus."

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
    "Je remonte le couloir des chambres."
    "Chambre 4. Julian."

    "Je m'arrête devant la porte."
    "De l'extérieur, rien."
    "Pas de décoration. Pas de trace de lui."
    "C'est presque drôle."
    "Julian passe son temps à vouloir exister partout, mais sa porte, elle, pourrait être celle de n'importe qui."

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 1.0

    "Pas de réponse."

    "Je frappe encore."

    play sound sfx_knock volume 8.0
    pause 0.8

    "Cette fois, j'entends du mouvement."
    "Pas quelqu'un qu'on tire hors du lit."
    "Plutôt quelqu'un qui choisit au bout de combien de secondes il va ouvrir."

    noam "Julian. C'est moi."

    pause 0.8

    play sound sfx_door volume 8.0

    $ showP("julian", "neutre", 0.65)
    $ showP("noam", "neutre", 0.30)

    "La porte s'ouvre."

    "Julian est là."
    "Et, pendant une seconde, j'ai un léger temps d'arrêt."

    "Il n'a pas l'air détruit."
    "Il n'a même pas l'air particulièrement atteint."

    julian sourire "Noam."
    julian taquin "Tu viens constater les dégâts ?"

    noam hesitation "Je venais surtout voir comment t'allais."

    julian sourire "Oh."
    julian taquin "C'est presque gentil."

    "Il se pousse."
    "Cette fois, c'est une vraie invitation à entrer dans la chambre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    $ showP("julian", "sourire", 0.65)
    $ showP("noam", "reflexion", 0.30)

    "Je rentre."
    "La chambre est propre."
    "Trop propre."
    "Comme une pièce témoin."
    "Rien qui dépasse."
    "Rien qui vive vraiment."

    julian neutre "Alors ?"
    julian sourire "Tu veux me dire de ne pas prendre les résultats comme quelque chose de personnel ?"
    julian taquin "Ou tu veux me sortir une de tes phrases calmes et évidemment utiles ?"

    noam "Disons que je ne suis pas vraiment venu avec un dialogue préétabli."

    julian rire "Moi si."

    pause 0.4

    "Il dit ça avec un petit sourire."
    "Comme une blague."
    "Sauf que malgré son sourire, je vois qu'il ne plaisante pas vraiment."

    noam reflexion "Tu n'as pas l'air aussi abattu que ce matin."

    julian sourire "Parce que je ne le suis pas."

    "Il tourne la tête vers la porte."
    "Puis il pose la main sur le brouilleur."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    "Le grésillement disparaît."
    "La caméra de la chambre pivote."
    "L'image devient froide, trop nette, presque déshumanisée."

    $ showP("julian", "triste", 0.72)

    julian triste "Je..."
    julian triste "J'avoue que c'est difficile."
    julian decu "Je pensais vraiment qu'on pouvait faire quelque chose de grand."
    julian triste "Et au final, vous avez eu peur."

    "Il baisse les yeux juste assez."
    "Gros plan parfait."
    "Même la douleur semble cadrée."

    noam reflexion "Arrête de..."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    noam reflexion "...jouer la comédie."

    $ showP("julian", "rire", 0.72)

    julian rire "Évidemment que je joue."
    julian sourire "Quand Kami peut regarder, il faut lui donner quelque chose à regarder."

    noam desaccord "Donc tout ça, c'était pour l'image."

    julian taquin "L'image, c'est ce qui reste quand les idées échouent."
    julian sourire "Et le plus beau, c'est que même un échec peut me servir."

    play sound sfx_beep
    show screen j50_julian_surveillance_overlay
    pause 0.4

    $ showP("julian", "triste", 0.72)

    julian triste "Je suppose qu'il faut accepter la défaite avec dignité."
    julian decu "Mais je continuerai à porter ce vote jusqu'au bout."
    julian triste "Même si certains préfèrent avoir peur."

    "La phrase est pour moi."
    "Le regard est pour la caméra."

    play sound sfx_beep
    hide screen j50_julian_surveillance_overlay
    pause 0.4

    $ showP("julian", "sourire", 0.65)

    julian sourire "Voilà."
    julian taquin "Public et privé. Deux langues. Même bouche."

    noam reflexion "Et toi, dans tout ça ?"

    julian neutre "Moi ?"
    julian sourire "Je fais ce qu'il faut pour rester utile."

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

    julian sourire "Qu'il passe ou qu'il tombe, ce vote me donne quelque chose."
    julian idee "S'il passe, j'ai porté une idée décisive."
    julian idee "S'il tombe, j'ai combattu votre peur du changement."
    julian rire "Dans les deux cas, je suis gagnant."

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

    julian sourire "C'est bien, non ?"
    julian taquin "Simple. Clair. Réutilisable."

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
        julian "C'est une façon très injuste de résumer une ambition sincère."

        noam "Non."
        noam "C'est une façon très précise."

        $ showP("julian", "peur", 0.65)
        julian peur "Tu crois que c'est drôle, ça ?"
        julian inquiet "Tu crois que je n'ai pas pensé à ce qui reste quand personne n'a plus besoin de moi ?"

    elif j50_julian_fissure >= 1:
        noam reflexion "Tu veux être celui autour de qui le vote s'organise."
        noam "Pas seulement celui qui vote pour."

        $ showP("julian", "reflexion", 0.65)
        julian reflexion "Peut-être."
        julian sourire "Ou peut-être que tu as juste besoin que je sois plus simple que je ne le suis."

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

    "Je m'arrête une seconde devant la porte."
    "Brouilleur activé, il parle plus vrai."
    "Brouilleur coupé, il se remet en place."

    "Et le plus inquiétant, c'est que je ne sais pas quelle version est la plus dangereuse."

    hide noam
    hide julian

    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    $ doplleganger = 1
    "Je marche vers la salle d'observation."
    "Kami ne nous a jamais interdit de surveiller les données du terminal après tout."
    "Probablement parce que regarder le vide en face finit toujours par décourager les gens."

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 0.8

    "La salle est plongée dans cette lumière bleue permanente."
    "Les baies vitrées donnent directement sur l'espace."
    "Même après plusieurs jours, ça me prend quelques secondes à chaque fois d'habituer mes yeux à cette étrange atmosphère."
    "Ce silence derrière les vitres qui n'a rien à voir avec le silence gêné des couloirs."
    "Un silence qui existe depuis des milliards d'années et qui durera des milliards d'années encore après nous."
    "Indifférent à nos votes, à notre lutte ou à notre survie."

    $ showP("elias", "neutre", 0.75)

    "Elias est là."
    "Assis à la console centrale."
    "Une tasse bien chaude dans une main."
    "Les yeux sur un des écrans latéraux qui affiche les données des districts."

    elias neutre "Noam ?"

    "Il ne s'est même pas retourné."

    elias "Qu'est-ce que tu fais là ?"

    $ showP("noam", "neutre", 0.25)

    noam "C'est le seul endroit qui soit calme aujourd'hui."

    $ showP("elias", "neutre", 0.75)
    elias "Ouais."
    elias "La cafétéria, c'était... chargé."

    "Il prend une gorgée de café."
    "Il continue à fixer l'écran sans tourner la tête."

    $ showP("elias", "neutre", 0.75)
    elias "Regarde ça."

    "Il pointe vers une partie spécifique du panneau droit."
    "Il y a un flux de données qui défile en temps réel."
    "Des chiffres, des courbes, des noms de districts."

    $ showP("noam", "reflexion", 0.25)

    noam "Faut que tu m'expliques, c'est quoi tous ces chiffres ?"

    elias "Ici..."

    "Il pointe du doigt une liste de noms qui défile."

    elias inquiet "C'est les noms des gens qui ont merdé."
    elias "Et la règle qu'ils ont cassée."

    "Je regarde la liste. Elle est longue. Bien trop longue."
    "Je regarde les raisons : vol, bagarre, menace... Les raisons ne manquent pas, mais il y a toujours un point central : les tickets de rationnement."
    "Les gens veulent juste manger."

    pause 0.4

    "Je m'approche de la console."
    "Je veux voir plus précisément."
    "Je tends le bras vers l'écran pour zoomer sur la courbe de population de Limen."

    pause 0.3

    elias inquiet "Attends, regarde..."

    "Elias se relève pour me montrer quelque chose mais son coude accroche sa tasse."
    play sound sfx_drop

    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")

    "Un bruit mat."
    "Le café se renverse en arc sur le bord de la console."
    "Sur les touches."
    "Sur le panneau de commande latéral."

    elias "Et merde !"

    call screen trace_qte(path_type="arc", time_limit=2.4, wait_time=0.15, tolerance=70, max_errors=3, anchor_x=960, anchor_y=620, start_radius=120)
    $ j50_coffee_trace_score = tq_progress

    if j50_coffee_trace_score >= 0.82:
        "Mes doigts frôlent la porcelaine."
        "Pas assez pour la retenir."
        "Juste assez pour changer l'angle."
    elif j50_coffee_trace_score >= 0.35:
        "Je réagis trop tard."
        "Ma main traverse l'air là où la tasse n'est déjà plus."
    else:
        "Je tends la main trop vite."
        "Mon poignet heurte le bord de la console."
        "Et la tasse part encore plus loin."

    "Il se lève d'un bond."
    "Attrape sa tasse ; vide désormais."
    "Le café ruisselle entre les touches."

    "Un voyant passe au rouge."
    "Un léger sifflement."

    noam "C'est moi qui— j'ai failli te bousculer, je—"

    elias inquiet "Non, non, c'était ma tasse."

    "Un autre voyant s'allume."
    "Orange."
    "Puis une fumée fine s'échappe d'une grille latérale."
    "Pas de flammes. Juste cette fumée grise et acre qui monte tranquillement."

    elias inquiet "OK."
    elias "Bon. OK. C'est pas mort."
    elias "Enfin... pas encore."

    "Un déclic mécanique quelque part dans le mur."
    "Fort."
    "Presque un claquement."

    "On se retourne."

    "La porte automatique de la salle s'est fermée."
    "Hermétiquement."
    "Le panneau de commande à côté affiche : VERROUILLAGE SÉCURITÉ — ANOMALIE DÉTECTÉE."

    pause 0.5

    elias panique "Ah."

    noam peur "La porte est bloquée ?"

    elias inquiet "La salle s'est verrouillée."
    elias "Sûrement une sécurité à la con."
    elias "Quand un truc fume, ça ferme tout pour éviter qu'on crève dedans."

    noam hesitation "En principe."

    elias "Ouais."
    elias fatigue "En principe."

    pause 0.4

    "La fumée continue de s'échapper de la grille."
    "Fine. Légère."
    "Pas de danger immédiat."
    "Mais la porte reste fermée."

    "Et derrière les baies vitrées, l'espace continue d'être indifférent à tout ça."

    noam reflexion "..."

    noam "Je me demande combien de temps on a."

    $ showP("elias", "panique", 0.75)
    elias panique "Putain, putain, putain..."
    elias inquiet "Noam, viens là. Tu vas relier les fils."
    elias "Même couleur ensemble. Tu réfléchis pas. Tu relies."

    "Elias arrache le panneau sous la console."
    "Des fils pendent en grappes colorées."
    "Ça fume encore un peu, mais moins."

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
        elias "Putain... bon. Pas grave."
        elias fatigue "Enfin si, grave, mais on va dire pas grave."

    if j50_wire_success >= 8:
        elias rire "T'as fait ça mieux que moi."
        elias "Ce qui est franchement pas rassurant."
    elif j50_wire_success >= 5:
        elias fatigue "C'est moche."
        elias "Mais ça tient."
    else:
        elias inquiet "C'est pété de partout."
        elias "Mais au moins, ça fume moins. On va prendre ça."

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")

    elias "La salle est ventilée."
    elias fatigue "On n'étouffera pas."
    elias "Mais ouais... on est bloqués là pour un moment."

    "Il s'assoit par terre."
    "Le dos contre le panneau, loin de l'écran qui fume encore légèrement."
    "Avec le calme de quelqu'un qui a déjà vécu des situations plus graves."

    elias neutre "Tu voulais regarder les chiffres de Limen, non ?"

    "Il pointe vers l'écran qui fonctionne encore."

    elias fatigue "On n'a nulle part où aller."
    elias "Autant qu'on en parle."

    noam "Il me semble que ce n'est pas le contexte idéal pour une discussion sur le vote."

    elias rire "Non."
    elias "Mais les bons moments, ici, ça n'existe plus vraiment."

    pause 0.5

    "Je m'assieds à côté de lui."
    "Par terre. Le dos au mur."
    "Les jambes tendues devant moi."
    "On regarde tous les deux les voyants rouges et les données qui défilent toujours."

    elias inquiet "Tu crois que ça va passer, le vote ?"

    noam "Je me demande si quelque chose peut encore changer avant demain."

    pause 0.3

    elias inquiet "Sael votera contre."
    elias "C'est sûr."

    noam "Elle me l'a dit ce matin."
    noam hesitation "Mara aussi. Et Iris."

    elias "..."

    "Silence."

    elias fatigue "Alors c'est foutu."

    noam "Peut-être pas..."

    "Je le dis sans vraiment y croire."
    "On le sait tous les deux."

    pause 1.0

    call show_custom_title("Après plusieurs heures") from _call_show_custom_title

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 3.0

    "Les voyants passent de rouge à orange."
    "La fumée s'est dissipée."
    "Le panneau de la porte clignote."

    play sound "sound/sfx_door.ogg"

    "Un déclic."
    "La porte s'ouvre."

    $ showP("elias", "fatigue", 0.75)

    elias fatigue "Ah. Libérés."

    "Il se lève."
    "S'étire le dos."

    elias "Je vais voir si j'ai pas cramé un truc important."

    "Il examine la console."
    "Quelques touches sont pâteuses."
    "L'écran latéral est éteint."

    elias neutre "Rien de trop grave."
    elias "Juste une caméra de relevé sur ce panneau."
    elias fatigue "C'est de la merde, mais ça se répare."

    noam reflexion "Je me demande si Kami va nous faire une remarque là-dessus."

    elias rire "Probablement."
    elias "Elle fait des remarques sur tout."

    hide noam
    hide elias

    "Enfin libérés, on se sépare et je me retrouve dans le couloir."

    jump _5_0_FIN_JOURNEE


label _5_0_FIN_JOURNEE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    "L'après-midi se passe dans un calme de façade."
    "Quelques échanges à la salle commune."
    "Un repas du soir que j'avale sans vraiment y goûter."
    "Des conversations qui démarrent et qui s'arrêtent avant d'aboutir à quelque chose d'intéressant."

    "Je croise Tomas dans le couloir."
    "Il fait un signe de tête."
    "Pas de mots."
    "Je fais pareil."

    "Je croise Nyra."
    "Elle a l'air de calculer quelque chose dans sa tête."
    "Elle ne me demande rien."
    "Je ne demande rien non plus."

    pause 0.6

    "La journée se finit comme elle a commencé."
    "Lentement. Lourdement."
    "Sans catastrophe, mais sans rien qui ressemble à une ouverture."

    "Kami ne fait pas d'annonce en début de soirée."
    "Ce silence-là est presque pire."
    "Comme si elle attendait quelque chose qu'on n'arrive pas à lui donner."

    pause 0.5

    "Je rentre dans ma chambre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    "Je m'assis au bord du lit."
    "Pas encore prêt à m'allonger."
    "Juste là. Posé sur le bord."

    pause 0.5

    think "Je pense que tout le monde a raison."
    think "D'une certaine façon."
    think "Et en même temps, le vote de demain sera contre."

    pause 0.4

    $ blink()
    "Je m'allonge sur le dos."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    "La lumière bleue des veilleuses."
    "Toujours là."
    "Ce plafond qui ne répond jamais."

    $ blink()

    "On a encore une nuit."
    "Et un matin."
    "Et puis le vote."

    think "Je me demande ce qu'on peut encore faire."
    think "Je me demande si 'faire' est encore le bon mot."
    think "Ou si parfois, il faut juste... être là."
    think "Sans solution. Sans angle."
    think "Juste présent dans quelque chose qui se casse."

    pause 0.5

    $ blink()

    "Quelque part dans le couloir, une porte s'ouvre et se referme."
    "Des pas discrets."
    "Quelqu'un qui n'arrive pas à dormir non plus."

    "Ou quelqu'un qui fait semblant."

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

    "Je ferme les yeux."
    "Pas parce que je suis en paix."
    "Juste parce que le corps finit toujours par tomber de fatigue avant la tête."

    "Le vote de demain est probablement perdu."
    "Et pourtant, quelque chose dans le fait de s'être levé ce matin, d'avoir frappé aux portes, d'avoir été là..."
    "Quelque chose là-dedans ne ressemble pas tout à fait à la défaite."

    pause 0.4

    "Je ne sais pas encore ce que ça veut dire."

    $ blink()
    pause 1.5

    "Le sommeil arrive."
    "Lent. Sans fracas."
    "Juste le silence, et la certitude que demain sera difficile."
    "Et que j'y serai quand même."

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
        jump _5_0_SAEL_PNC

    if _j50_sael_choice == "crane":
        $ j50_sael_mark_seen("crane")
        think "Je ne sais pas si c'est un souvenir, un avertissement ou une prière."
        think "Chez elle, même les morts semblent avoir une fonction."
        sael neutre "Ne touche pas."
        jump _5_0_SAEL_PNC

    if _j50_sael_choice == "affaires":
        $ j50_sael_mark_seen("affaires")
        think "Elle n'a pas décoré sa chambre."
        think "Elle l'a rendue habitable selon ses propres règles."
        think "Pas confortable. Habitable."
        jump _5_0_SAEL_PNC

    return


label _5_0_NUIT_OUVRIR:

    scene bg_dortoir at adaptive_fullscreen with dissolve

    "J'ouvre la porte juste assez pour voir le couloir."
    "Une silhouette tourne au bout de l'angle."
    "Trop vite pour que je voie son visage."
    "Pas assez vite pour que je puisse croire que je l'ai inventée."

    think "Le Conclave ne dort pas."
    think "Il se déplace à voix basse."

    scene bg_cg012 at adaptive_fullscreen with dissolve
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_ECOUTER:

    "Je reste immobile."
    "Les pas ralentissent derrière la porte."

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

    "Puis les pas s'éloignent."
    jump _5_0_NUIT_RETOUR


label _5_0_NUIT_RESTER:

    think "Je pourrais me lever."
    think "Je pourrais ouvrir."
    think "Mais ce soir, je n'ai plus la force de devenir utile."

    jump _5_0_NUIT_RETOUR
