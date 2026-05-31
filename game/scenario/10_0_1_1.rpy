# --------------------------------------------------------------------------------------------
# JOUR 10_0_1_1 — Matinée lourde
# Noam se réveille après le vote des campements limenois.
# Le joueur doit rejoindre la cafétéria et engager Elias pour lancer
# un dialogue à choix multiples autour de la table.
# --------------------------------------------------------------------------------------------

default j10011_waiting_elias = False
default j10011_cafeteria_done = False
default j10011_walk_choice = None

default j10011_tension = {"elias": 32, "ryn": 62, "mara": 44, "nyra": 38}
default j10011_tension_step = 0
default j10011_tension_done = False
default j10011_tension_result = "stable"
default j10011_tension_feedback = "La table attend une phrase qui ne mettra pas le feu."
default j10011_tension_last_choice = ""

init python:
    J10011_TENSION_NAMES = {
        "elias": "Elias",
        "ryn": "Ryn",
        "mara": "Mara",
        "nyra": "Nyra",
    }

    J10011_TENSION_COLORS = {
        "elias": "#8FD8FF",
        "ryn": "#FF5C5C",
        "mara": "#D98CFF",
        "nyra": "#C8D5DE",
    }

    J10011_TENSION_ROUNDS = [
        {
            "speaker": "elias",
            "low": "Ils ont bougé. Pas tous, mais assez pour que ça veuille dire quelque chose.",
            "high": "J'arrive pas à appeler ça une bonne nouvelle. J'y arrive vraiment pas.",
            "choices": [
                ("Rester sur les faits.", {"elias": -8, "ryn": +5, "mara": -2, "nyra": -4}, "Les chiffres tiennent la conversation à distance."),
                ("Dire qu'on a gagné du temps.", {"elias": -4, "ryn": +14, "mara": +4, "nyra": -2}, "Le mot 'gagné' passe mal. Très mal."),
                ("Demander ce qu'il a vu.", {"elias": -10, "ryn": -3, "mara": +2, "nyra": -2}, "Elias baisse les yeux. Il parle quand même."),
            ],
        },
        {
            "speaker": "ryn",
            "low": "Elle a monté son piège. On l'a vu trop tard.",
            "high": "Kami nous a piégés ! Elle les a tous mis là et elle nous a fait voter devant le canon !",
            "choices": [
                ("Le laisser vider sa colère.", {"elias": +6, "ryn": -12, "mara": +6, "nyra": +3}, "Ryn frappe la table. Puis il respire."),
                ("Le couper avant qu'il accuse quelqu'un.", {"elias": -2, "ryn": +16, "mara": +4, "nyra": -4}, "La phrase s'arrête. La colère, non."),
                ("Nommer le piège sans chercher de coupable ici.", {"elias": -3, "ryn": -9, "mara": -2, "nyra": -6}, "La cible reste Kami. Pour l'instant."),
            ],
        },
        {
            "speaker": "mara",
            "low": "Je sais pas ce qui me dégoûte le plus. Le piège ou le fait qu'il ait presque marché.",
            "high": "Non mais sérieusement. On est censés manger après ça ? Avec quoi ? Une petite fourchette de culpabilité ?",
            "choices": [
                ("Entrer dans son sarcasme.", {"elias": +4, "ryn": -3, "mara": -8, "nyra": +5}, "Mara ricane. C'est moche, mais ça casse la pointe."),
                ("Revenir au sort des campements.", {"elias": -4, "ryn": +9, "mara": +8, "nyra": -3}, "La table retombe dans les images de la veille."),
                ("Admettre que personne ne sait quoi faire.", {"elias": -5, "ryn": -4, "mara": -10, "nyra": -2}, "C'est nul. C'est honnête. Ça aide un peu."),
            ],
        },
        {
            "speaker": "nyra",
            "low": "Si la majorité s'est dispersée, alors la priorité est de conserver la procédure ouverte.",
            "high": "Je vous préviens. Si on laisse Ryn transformer ça en tribunal, on perdra notre seule marge de manœuvre.",
            "choices": [
                ("Soutenir sa méthode.", {"elias": -2, "ryn": +13, "mara": +2, "nyra": -10}, "Nyra se redresse. Ryn se ferme."),
                ("Lui rappeler que Ryn a le droit d'être en colère.", {"elias": +3, "ryn": -8, "mara": -3, "nyra": +12}, "Nyra encaisse. Mal."),
                ("Traduire sa phrase en urgence concrète.", {"elias": -4, "ryn": -4, "mara": -2, "nyra": -8}, "La méthode devient une tâche. C'est moins froid."),
            ],
        },
        {
            "speaker": "elias",
            "low": "Je crois que je suis soulagé. Et c'est ça qui me donne envie de vomir.",
            "high": "Je veux pas qu'on me dise que ça va. Si quelqu'un me dit ça, je pars.",
            "choices": [
                ("Ne pas le rassurer.", {"elias": -12, "ryn": -2, "mara": -2, "nyra": -2}, "Personne ne ment. Elias reste assis."),
                ("Dire que ça aurait pu être pire.", {"elias": +22, "ryn": +10, "mara": +12, "nyra": +4}, "La phrase est vraie. C'est justement le problème."),
                ("Lui demander de rester avec la table.", {"elias": -8, "ryn": +2, "mara": -5, "nyra": -3}, "Il hoche la tête. À peine."),
            ],
        },
        {
            "speaker": "ryn",
            "low": "Je veux juste qu'elle arrête de nous faire choisir la forme de la catastrophe.",
            "high": "Elle recommencera. Vous le savez ? Elle recommencera jusqu'à ce qu'on se bouffe entre nous.",
            "choices": [
                ("Promettre qu'on ne se retournera pas les uns contre les autres.", {"elias": -2, "ryn": +18, "mara": +8, "nyra": +4}, "Trop grand. Trop propre. Personne n'y croit."),
                ("Dire qu'on peut seulement tenir cette table.", {"elias": -8, "ryn": -10, "mara": -6, "nyra": -6}, "Petit objectif. Solide parce qu'il est petit."),
                ("Laisser Nyra proposer la suite.", {"elias": -4, "ryn": +4, "mara": -3, "nyra": -10}, "Nyra reprend la main sans hausser la voix."),
            ],
        },
    ]

    def j10011_reset_tension():
        store.j10011_tension = {"elias": 32, "ryn": 62, "mara": 44, "nyra": 38}
        store.j10011_tension_step = 0
        store.j10011_tension_done = False
        store.j10011_tension_result = "stable"
        store.j10011_tension_feedback = "La table attend une phrase qui ne mettra pas le feu."
        store.j10011_tension_last_choice = ""

    def j10011_tension_round():
        if store.j10011_tension_step >= len(J10011_TENSION_ROUNDS):
            return None
        return J10011_TENSION_ROUNDS[store.j10011_tension_step]

    def j10011_tension_line(round_data):
        speaker = round_data["speaker"]
        if store.j10011_tension.get(speaker, 0) > 50:
            return round_data["high"]
        return round_data["low"]

    def j10011_apply_choice(choice_index):
        if store.j10011_tension_done:
            return

        round_data = j10011_tension_round()
        if round_data is None:
            store.j10011_tension_done = True
            store.j10011_tension_result = "stable"
            return

        if choice_index < 0 or choice_index >= len(round_data["choices"]):
            return

        label, effects, feedback = round_data["choices"][choice_index]
        current = dict(store.j10011_tension)

        for key, delta in effects.items():
            current[key] = max(0, min(100, current.get(key, 0) + delta))

        store.j10011_tension = current
        store.j10011_tension_feedback = feedback
        store.j10011_tension_last_choice = label

        if max(current.values()) >= 100:
            store.j10011_tension_done = True
            store.j10011_tension_result = "rupture"
        else:
            store.j10011_tension_step += 1
            if store.j10011_tension_step >= len(J10011_TENSION_ROUNDS):
                store.j10011_tension_done = True
                if max(current.values()) >= 78:
                    store.j10011_tension_result = "fragile"
                else:
                    store.j10011_tension_result = "stable"

        renpy.restart_interaction()

transform j10011_dg_echo:
    alpha 0.0
    xoffset 18
    easein 0.35 alpha 0.22 xoffset 0
    pause 0.55
    easeout 0.45 alpha 0.0 xoffset -14

transform j10011_dg_far:
    zoom 0.32
    alpha 0.34
    xalign 0.74
    yalign 0.72
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.18)

screen j10011_baie_choice():

    modal True
    zorder 280

    add Solid("#000")
    add "images/background/bg_cg030_1.png" at cover_screen
    add Solid("#00000066")

    frame:
        xalign 0.5
        yalign 0.82
        xsize 760
        padding (22, 18)
        background Solid("#05080DDD")

        vbox:
            spacing 12
            text "Au-delà de la baie, une silhouette s'éloigne.":
                xalign 0.5
                size 25
                color "#E8F4FF"
            hbox:
                xalign 0.5
                spacing 14
                textbutton "Ignorer":
                    xsize 210
                    ysize 52
                    action Return("ignorer")
                textbutton "Regarder plus attentivement":
                    xsize 300
                    ysize 52
                    action Return("regarder")
                textbutton "Appeler":
                    xsize 210
                    ysize 52
                    action Return("appeler")

screen j10011_table_tension_screen():

    modal True
    zorder 280

    add Solid("#07060A")
    add "images/background/bg_cafeteria.png" at cover_screen
    add "gui/day10/morning_heat_overlay.png" at cover_screen:
        alpha 0.34

    add Solid("#00000055")

    $ _round = j10011_tension_round()

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 760
        padding (34, 28)
        background "gui/day10/tension_panel.png"

        vbox:
            spacing 20

            vbox:
                spacing 6
                text "MATINÉE LOURDE":
                    xalign 0.5
                    size 42
                    color "#FFE0B8"
                    bold True
                    outlines [(2, "#210B0B", 0, 0)]
                text "Choisis comment Noam intervient. Si une tension atteint 100, la discussion explose.":
                    xalign 0.5
                    size 21
                    color "#E8F4FF"

            hbox:
                xalign 0.5
                spacing 24

                for key in ["elias", "ryn", "mara", "nyra"]:
                    $ _value = j10011_tension.get(key, 0)
                    $ _color = J10011_TENSION_COLORS[key]
                    vbox:
                        spacing 7
                        text J10011_TENSION_NAMES[key]:
                            xalign 0.5
                            size 22
                            color _color
                            bold True
                        fixed:
                            xsize 230
                            ysize 24
                            add "gui/day10/tension_bar_bg.png":
                                xysize (230, 24)
                            add "gui/day10/tension_bar_fill.png":
                                xysize (int(230 * _value / 100.0), 24)
                            if _value >= 80:
                                add Solid("#FF2E2E55") xysize (230, 24)
                        text "[_value]/100":
                            xalign 0.5
                            size 18
                            color "#F5F7FA"

            frame:
                xalign 0.5
                xsize 1040
                ysize 170
                padding (24, 18)
                background Solid("#03080FCC")

                if _round is not None:
                    $ _speaker = _round["speaker"]
                    vbox:
                        spacing 10
                        text J10011_TENSION_NAMES[_speaker]:
                            size 26
                            color J10011_TENSION_COLORS[_speaker]
                            bold True
                        text "[j10011_tension_line(_round)]":
                            size 32
                            color "#FFFFFF"
                            xmaximum 980
                            outlines [(2, "#000000", 0, 0)]
                else:
                    text "La table retombe dans un silence moins dangereux.":
                        xalign 0.5
                        yalign 0.5
                        size 32
                        color "#FFFFFF"

            frame:
                xalign 0.5
                xsize 1040
                ysize 88
                padding (18, 12)
                background Solid("#0B121BDD")
                text "[j10011_tension_feedback]":
                    xalign 0.5
                    yalign 0.5
                    size 23
                    color "#FFE0B8"
                    text_align 0.5
                    xmaximum 980

            if _round is not None and not j10011_tension_done:
                vbox:
                    xalign 0.5
                    spacing 12
                    for idx, choice_data in enumerate(_round["choices"]):
                        $ _choice_label = choice_data[0]
                        textbutton _choice_label:
                            xalign 0.5
                            xsize 860
                            ysize 62
                            background "gui/day10/choice_idle.png"
                            hover_background "gui/day10/choice_hover.png"
                            text_size 24
                            text_color "#E8F4FF"
                            text_hover_color "#FFFFFF"
                            action Function(j10011_apply_choice, idx)

    if j10011_tension_done:
        if j10011_tension_result == "rupture":
            add "gui/day10/warning_flash.png" at cover_screen:
                alpha 0.20
        timer 0.8 action Return(j10011_tension_result)

label _10_0_1_1_REVEIL_CHAMBRE:

    scene black

    $ current_day = 10
    $ j10011_cafeteria_done = False
    $ j10011_waiting_elias = False

    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    $ blink()

    "Je me réveille avant l'annonce."

    pause 0.4

    think "Pas de bip."
    think "Pas la moindre voix."
    think "Juste ma tête qui cogne encore et encore."

    "Elle cogne."
    "Pas comme un mal de tête habituel."
    "Plutôt comme si un voisin un peu trop bruyant avait écouté du métal avec la basse mise à fond."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "La chambre est particulièrement chaude."
    "Le drap colle à ma peau."
    "L'air est sec, presque irrespirable."

    think "Le Conclave régule tout."
    think "Donc ça aussi, c'est voulu et c'est pas normal."

    pause 0.4

    "Je reste assis sur le bord du lit."
    "J'écoute."

    pause 0.6

    "Rien ne répond."

    "D'habitude, même le silence du Conclave a une épaisseur."
    "Des pas étouffés."
    "Une machine."
    "Un frottement de porte."

    "Ce matin, c'est plus sec."
    "Plus vide."

    think "Après hier, tout devrait faire du bruit."
    think "Tout le monde devrait parler."
    think "Ou crier."
    think "Quelque chose."

    pause 0.4

    "Je me mouille le visage au lavabo."
    "Elle est tiède."

    think "Forcément tiède."

    "Je récupère ma veste."
    "Je la mets quand même."

    menu:
        "Sortir tout de suite.":
            think "Si je reste ici, je vais compter les secondes."
            think "Très mauvaise idée."

        "Prendre une minute de plus.":
            "Je reste devant la porte."
            "La main sur la poignée."
            pause 0.5
            think "Une minute."
            think "Pas mieux."
            think "Il faut avancer."

    stop music fadeout 1.0
    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "Le couloir est plus chaud que la chambre."
    "Ça devrait être impossible."

    "Une porte s'ouvre au fond."
    "Puis se referme aussitôt."

    think "Personne n'a envie de croiser personne."
    think "Très pratique."
    think "On va tous le faire quand même."

    pause 0.4

    "Je prends la direction de la cafétéria."
    "Pas parce que j'ai faim."

    think "Parce que si quelqu'un parle ce matin, ce sera là-bas."

    $ j10011_waiting_elias = True
    $ free_time_active = False
    $ free_time_next_label = None
    $ exploration_libre_active = True
    $ exploration_libre_next_label = None
    $ exploration_libre_seen_rooms = []
    $ exploration_libre_required_visits = 0
    $ exploration_libre_allowed_rooms = ["cafeteria"]
    $ exploration_libre_title = "Rejoindre la cafétéria"
    $ sync_character_links_from_persistent()
    $ conclave_lock = False
    $ dortoir_lock = False

    tuto "(Va à la cafétéria et parle à Elias.)"

    jump START_EXPLORATION_LIBRE_MAP

label _10_0_1_1_CAFETERIA_ELIAS:

    $ j10011_waiting_elias = False
    $ free_time_active = False
    $ exploration_libre_active = False
    $ exploration_libre_allowed_rooms = None

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.2

    "La cafétéria est presque pleine."
    "Mais elle ne sonne pas pleine."

    "Les plateaux raclent doucement."
    "Les gobelets restent trop longtemps dans les mains."
    "Personne ne plaisante assez fort pour que ça devienne une vraie blague."

    $ showGroup([
        ("elias", "fatigue", 0.18),
        ("mara", "stress", 0.40),
        ("ryn", "colere", 0.62),
        ("nyra", "fatigue", 0.84),
    ])

    "Elias est à une table du fond."
    "Ryn est debout derrière sa chaise."
    "Mara a son plateau devant elle et n'y touche pas."
    "Nyra regarde l'écran d'information sans vraiment le lire."

    pause 0.4

    elias fatigue "Noam, viens."

    noam inquiet "Tu tiens ?"

    mara stress "T'en as d'autres des questions connes ?"

    noam "Ok. Compris."

    mara "Non, vraiment."
    mara "Si quelqu'un répond oui, je lui lance mon poing dans la gueule."

    elias "La majorité des campements limenois se sont dispersés."
    elias "C'est passé sur l'écran il y a quelques minutes."

    pause 0.3

    nyra "Plusieurs déclarations d'urgence ont été reçues après le vote."
    nyra reflexion "Ceux qui ont pu transmettre un registre sont couverts."
    nyra sourire "On a quand même réussi à sauver du monde..."

    ryn colere "Quelques uns, ouais..."

    "Le mot sort trop fort."
    "Quelques têtes se tournent."
    "Elles se détournent presque aussitôt."

    ryn colere2 "Ils sont couverts..."
    ryn "Couverts..."
    ryn "Comme si on parlait d'une putain d'assurance."

    elias inquiet "Ryn, attends..."

    ryn "Non. Pas maintenant."
    ryn colere2 "Non, tu vas pas me faire ta morale maintenant."
    ryn "Kami les a piégés."
    ryn "Elle nous a piégés."
    ryn colere "Elle a posé des gens devant un canon et elle nous a demandé de voter le plus vite possible pour les éclater en morceaux !"

    pause 0.4

    mara stress "Putain, je mange Ryn !"
    mara jaloux "Garde tes images dégueulasses pour toi !"

    nyra fatigue "Ryn, assieds-toi."

    ryn colere "Non, Nyra."

    "Il ne crie pas encore."

    $ hideGroup()
    call j10011_play_table_tension from _call_j10011_play_table_tension
    $ j10011_table_result = _return

    jump _10_0_1_1_APRES_TABLE

label j10011_play_table_tension:

    $ j10011_reset_tension()
    $ _result = renpy.call_screen("j10011_table_tension_screen")
    return _result

label _10_0_1_1_APRES_TABLE:

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    if j10011_table_result == "rupture":
        play sound sfx_clap
        with hpunch

        $ showGroup([
            ("ryn", "colere2", 0.25),
            ("elias", "panique", 0.50),
            ("nyra", "colere", 0.75),
        ])

        ryn colere2 "J'en peux plus."
        ryn "J'en peux plus de vous entendre parler comme si on avait encore une marge de manoeuvre."

        elias panique "Ryn, arrête."

        nyra colere "Tu vas t'asseoir."

        ryn "Ou quoi ?"

        pause 0.5

        "Mara se lève."
        "Pas vite."
        "Pas lentement non plus."

        mara colere "Ou je te fais avaler ton plateau."

        pause 0.4

        "Le silence tombe."

    elif j10011_table_result == "fragile":
        $ showGroup([
            ("elias", "fatigue", 0.20),
            ("ryn", "fatigue", 0.45),
            ("mara", "stress", 0.67),
            ("nyra", "raison", 0.86),
        ])

        "La table ne se calme pas vraiment."
        "La tension cesse juste de monter."

        ryn fatigue "Je veux un chiffre."
        ryn "Pas une majorité."
        ryn "Un chiffre."
        ryn colere "Je veux savoir combien sont morts !"

        nyra raison "On le demandera."
        nyra "Au pire on pourra voir avec Tomas pour fouiller dans les archives..."

        mara stress "J'ai pas vraiment envie de savoir moi en fait."

        elias fatigue "Rien ne t'oblige à venir."

        pause 0.3

    else:
        $ showGroup([
            ("elias", "fatigue", 0.20),
            ("ryn", "determine", 0.45),
            ("mara", "doute", 0.67),
            ("nyra", "raison", 0.86),
        ])

        "Ryn finit par s'asseoir."
        "La chaise grince."
        "Personne ne relève."

        elias fatigue "Je suis soulagé."
        elias "Je crois, oui."
        elias "Et je déteste ça."

        mara doute "Ouais, pareil."
        mara "Bienvenue au club le plus nul du monde."

        nyra raison "On doit obtenir le détail des campements."
        nyra "Ceux dispersés."
        nyra "Ceux déclarés."
        nyra "Ceux qui n'ont pas répondu."
        nyra "Combien sont morts..."

        ryn determine "Putain..."

        pause 0.3

        ryn "Ouais. Faisons ça. On doit savoir."

    pause 0.5

    $ hideGroup()

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "L'écran d'information continue de défiler."

    pause 0.4

    "Je fixe le bord de mon plateau."
    "Je ne me souviens pas l'avoir pris mais il est là."

    jump _10_0_1_1_MARCHE_APRES_TABLE

label _10_0_1_1_MARCHE_APRES_TABLE:

    stop music fadeout 1.5
    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.2


    "Je sors de la cafétéria avant que quelqu'un me demande où je vais."
    "Je n'ai pas de réponse."
    "Je marche."

    "Les lumières du couloir ont l'air plus faibles."
    "Pas éteintes."
    "Juste fatiguées elles aussi."

    think "Très bien."
    think "Maintenant je donne des états d'âme aux néons."

    "Le couloir me semble plus long qu'hier."
    "Ou alors je vais moins vite."

    scene bg_maintenance at adaptive_fullscreen with dissolve

    "Un bruit sec vient de la salle de maintenance."
    "Quelque chose qui tombe."
    "Puis une voix qui insulte l'objet avec beaucoup trop de précision."

    $ showGroup([
        ("elias", "fatigue", 0.52),
    ])

    elias fatigue "Non, mais bien sûr."
    elias "Tombe. Fais ta vie."
    elias "Moi aussi je rêve de m'allonger par terre et de devenir inutile."

    noam fatigue "Je dérange une relation importante ?"

    elias inquiet "Noam ?"
    elias fatigue "Non. Enfin si. Mais elle était toxique depuis le début."

    "Il tient un panneau ouvert d'une main."
    "De l'autre, un outil dont je ne connais pas le nom."
    "Un câble pend devant lui comme une phrase qui refuse de finir."

    noam "Tu répares quoi ?"

    elias "Aucune idée."
    elias "J'ai commencé par 'ce truc clignote'."
    elias "Maintenant on est sur 'ce truc ne clignote plus mais il sent le chaud'."

    noam "Progrès ?"

    elias detendu "On va dire ça."

    pause 0.3

    elias fatigue "Tout le monde est à bout."
    elias "Même les murs ont l'air de vouloir prendre une pause."

    noam "Les murs ont peut-être voté contre."

    elias rire "Si les murs se mettent à voter, je démissionne."

    pause 0.4

    "Son rire tient à peine deux secondes."
    "Mais il existe."

    elias fatigue "Va marcher, Noam."
    elias "Mais pas vers les dortoirs."
    elias "Il y a une ambiance de caveau là-bas."

    noam "Noté."

    $ hideGroup()

    tuto "(Explore trois zones du Conclave. Les dortoirs sont inaccessibles.)"

    call START_EXPLORATION_LIBRE(
        next_label="_10_0_1_1_DOPPELGANGER",
        required_visits=3,
        allowed_rooms=[
            "archive",
            "cafeteria",
            "canon",
            "conclave",
            "gymnase",
            "infirmerie",
            "livraison",
            "maintenance",
            "observation",
            "repos",
            "stockage",
        ],
        title="Marche dans le Conclave"
    ) from _call_j10011_exploration_libre

    return

label _10_0_1_1_DOPPELGANGER:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je ne choisis pas vraiment la direction."
    "Mes pas continuent, eux, à errer sans réel but dans le Conclave."
    "Les couloirs, eux, continuent de s'étirer."

    "Après quelques minutes, un étrange sentiment me prend à la gorge."
    "Je m'arrête. Je me retourne."

    "Et je la vois..."

    pause 0.4

    scene bg_cg030 at adaptive_fullscreen with vpunch
    $ unlock_gallery_image("bg_cg030")
    pause 1.6
    scene bg_cg030_1 at adaptive_fullscreen

    menu:
        "Ignorer":
            "Je cligne rapidement des yeux et la forme que j'ai cru apercevoir n'était déjà plus là."
        "Regarder plus attentivement":
            "Je plisse les yeux."
            "Il n'y a plus rien."
            "Mais il y avait quelque chose."
            "Enfin, quelqu'un..."
        "Appeler":
            noam inquiet "Hé !"
            pause 0.5
            "Ma voix s'écrase contre la vitre."
            "Dehors, rien ne répond."

    scene bg_cg030_1 at adaptive_fullscreen
    show expression Solid("#00000033") as j10011_baie_dim

    pause 0.2

    $ blink()

    scene bg_cg030_1 at adaptive_fullscreen
    "Quand je rouvre les yeux, la cour est toujours vide."

    stop music fadeout 1.0
    pause 0.4

    "Le silence arrive d'un coup."
    "Je n'entends plus rien."
    "Pas le moindre bruit..."

    think "Alors quel est ce sentiment si étrange ?"

    pause 0.4

    "Je reste encore quelques secondes totalement immobile dans le couloir."
    "Puis je repars."

    scene bg_couloir at adaptive_fullscreen with dissolve
    "Perdu dans mes pensées."

    hide j10011_baie_dim
    scene black with fade

    jump _10_0_1_1_2_ANNONCE_KAMI

label _10_0_1_1_2_ANNONCE_KAMI:

    scene black
    pause 0.4

    play music "music/bgm_low_tension.mp3" fadein 1.5

    "Je ne sais pas pendant combien de temps je suis resté là, immobile."
    "Assez tout de même pour que je comprenne que ça a duré bien plus qu'un instant."

    pause 0.3

    play sound sfx_announce
    show screen kami_broadcast_ui

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Comment vont mes petits bouts de choux ce matin ?"
    kami "Vous vous êtes bien reposés ?"

    "Sa voix résonne dans le couloir."
    "Elle se répercute dans les murs puis s'amplifie dans nos tripes."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je vois que vous vous êtes bien acclimatés à mon retour parmi vous."
    kami "Oh ! En parlant de climat."

    scene bg_diffusion_meteo at adaptive_fullscreen with dissolve
    kami "Aujourd'hui il fera particulièrement chaud au sein du Conclave."
    kami "Vous vous en êtes déjà sans doute rendu compte."
    kami "La cause ? Un vent chaud venant de la salle du Canon, celui-ci ayant dû rattraper son retard des quelques derniers jours."
    kami "Il n'était plus très loin de la surchauffe."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je vous conseille donc d'éviter d'aller dans la salle du Canon aujourd'hui."
    kami "A moins que vous ne souhaitiez finir carbonisé par la chaleur !"

    pause 0.3

    kami "Mais je ne suis pas là pour être votre présentatrice météo particulière !"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Alors revenons à nos moutons."
    kami "Vous êtes parvenu à gagner du temps et vous avez réussi à sauver quelques Limenois qui souhaitaient transgresser les Commandements !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Même si je devrais TOUS les éradiquer pour avoir osé me défier !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Mais bon, je suis de bonne humeur aujourd'hui."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Quoi ?! ça se voit non ?!"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    pause 2.0

    "Elle prend une longue seconde de pause avant de reprendre."
    
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Vous le savez déjà mais nous sommes au dixième jour du Conclave."
    kami "Vous avez déjà fait un tiers du travail !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais ce travail n'est pas encore terminé."
    kami "Je vous attends dans la Salle du Conclave pour l'annonce du prochain vote !"

    hide screen kami_broadcast_ui

    pause 0.3

    scene bg_couloir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "reflexion", 0.20),
        ("sael", "reflexion", 0.80),
    ])

    sael inquiet "Noam ? Qu'est ce que tu fixes ?!"

    "Sael venait de sortir de l'infirmerie et regardait désormais dans la même direction que moi."

    sael "Y'a rien du tout."
    sael raison "Tu viens au Conclave pour le vote ?"

    "Je réfléchis une longue seconde avant de répondre machinalement."

    noam panne "Ouais."
    noam "Ouais j'arrive."

    "Sael s'éloigne, j'attends un peu."
    "Quelques minutes en fait."
    ""

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Quand j'arrive, presque tout le monde est déjà là."
    "Tout le monde se regarde mais personne n'ose vraiment s'adresser la parole."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    pause 0.3

    mara "Ah bah enfin, tu foutais quoi Noam ?!"

    tomas fatigue "Encore un vote... Franchement je commence à en avoir marre"

    noam "Ouais, désolé pour l'attente..."
    noam "J'étais... Fin bref, c'est pas bien grave."

    lysa inquiet "Hein ?! Mais pourquoi tu fais le mec énigmatique tout d'un coup ?"

    elen rire "Ouais !"
    elen inquiet "T'as trop une tête bizarre."
    elen rire "Qu'est ce qui va pas ? T'as mal au ventre ?!"

    noam colere "C'est rien je vous dis."
    noam triste "Je dois être fatigué c'est tout."

    mara stress "Olala, pas la peine de faire la gueule hein."
    mara "Nous aussi on est crevé."

    pause 0.3

    kael doute "..."
    kael calme "Laissez-le."
    kael calme "S'il veut pas en parler, laissez-le."

    iris desaccord "Ouais, on a d'autres chats à fouetter."

    julian inquietude "Franchement, Kami pouvait pas attendre demain pour nous annoncer le prochain vote ?."

    sael mefiant "Elle veut qu'on dorme en y pensant toute la nuit..."

    elias fatigue "Et bah, disons qu'elle est douée pour ça."

    play sound sfx_announce
    show screen kami_broadcast_ui
    
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Ah, je vois que vous êtes tous présents. C'est bien, ça m'évite de devoir faire l'appel."
    kami "Comme vous êtes désormais installés, je vais éviter les préliminaires inutiles."

    "Tous les écrans de la salle s'allument en même temps."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ah vous avez hâte de savoir n'est-ce pas ?!"

    pause 1.0

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Au douzième jour, vous voterez sur l'autorisation ou interdiction des dispositifs de brouillage."
    kami "Si les dispositifs de brouillage sont autorisés, ils deviendront légaux."
    kami "Adieu la surveillance totale et absolue de votre bien aimée amie Kami."
    kami "Leur possession, leur fabrication et leur usage ne constitueront plus une infraction."
    kami "Dans les limites techniques que je définirai, évidemment."
    kami "Il restera interdit de les utiliser pour bafouer les autres Commandements."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Par contre..."
    kami "Si les dispositifs de brouillage sont interdits..."
    kami "Toute zone détectée avec ces dispositifs sera broyée par un tir de laser."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Et oui, il faut respecter les règles mes chéris !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ah et puis soyons sérieux, si vous décidez de les interdire pour les autres..."
    kami "En cohérence, je débrancherai également les brouilleurs qui se trouvent dans vos chambres !"

    pause 0.5

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn colere "Broyée..."
    $ bc_hide()

    kami "Oui."
    kami "Le terme est volontairement descriptif."
    kami "L'euphémisme nuit souvent à la pédagogie."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Alors soyons clairs !"

    $ bc_show("nyra", "raison", px=-70, py=-50, pz=0.85)
    nyra raison "Mais en fait, personne ne va voter pour se faire espionner..."
    $ bc_hide()

    kami "Se faire espionner ? Peut-être pas, mais l'absence de brouilleur est aussi un gage de sécurité."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Quand il n'y a pas de brouilleur, je peux savoir en temps réel si quelqu'un brise les règles."
    kami "S'il y en a, c'est bien plus compliqué."

    $ bc_show("mara", "rire", px=-70, py=-50, pz=0.85)
    mara "Super. Tout ça pour nous mater en culotte !"
    mara "Laisse tomber Kami, je préfère de loin que seuls MES hommes puissent me voir ainsi."
    mara "Et... Même en matière de femme, je préfère celles qui sont bien vivantes !"
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Oh mais ne t'en fais pas, je suis bien capable de m'occuper de mes petits disciples "
    kami "Il y a bien d'autres manières que de toucher pour pouvoir prendre du plaisir..."

    pause 0.3

    $ bc_show("elias", "fatigue", px=-70, py=-50, pz=0.85)
    elias fatigue "C'est une idée ou cette conversation part en couille ?"
    elias "Quoi ?! Pourquoi vous me regardez comme ça ?!"
    elias "C'est pas moi qui a parlé de 'Mes hommes' avec Kami hein !"

    $ bc_show("kael", "doute", px=-70, py=-50, pz=0.85)
    kael doute "Les chambres sont équipées de brouilleurs internes depuis notre arrivée."
    kael "C'est pour empêcher Kami d'avoir accès à nos conversations privées."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Petite correction."
    kami "C'est pour empêcher que la cellule de diffusion du Conclave n'ait accès à vos conversations privées."
    kami "Personnellement, désolée de vous décevoir, mais je vous vois constamment, et je vous entends à chaque instant."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je peux même dire qui ronfle ici !"

    $ bc_show("iris", "desaccord", px=-70, py=-50, pz=0.85)
    iris desaccord "Personne ne va voter contre ça, j'en suis sûre."

    $ bc_show("julian", "inquietude", px=-70, py=-50, pz=0.85)
    julian inquietude "C'est clair, que tu nous observes c'est une chose."
    julian "Mais il faut respecter l'intimité des demoiselles. TOUJOURS."
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "ce sera à vous d'en décider. Ce sera votre décision. Ce sera vos conséquences."

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    pause 0.3

    tomas fatigue "Franchement... J-Je comprends le débat."

    ryn colere2 "Hein ?! Quoi ?! Comment ça tu comprends le débat ? T'as écouté ce qu'elle a dit !!"

    tomas "En fait... Y'a déjà des dispositifs de brouillage qui existent et qui transitent..."
    tomas "Jusque là, ce n'était ni vraiment toléré, ni vraiment interdit."

    lysa "Kami veut avoir accès à toutes les infos."
    lysa inquiet "Et l'interdiction transforme chaque cachette en cible."

    elen rire "Alors on les autorise et voilà, le débat est fini !"

    mara stress "Oui."
    mara "Évidemment qu'on va autoriser ça."
    mara "La vie c'est pas dans une putain de télé-réalité où tous nos gestes peuvent être observés !"

    tomas "En fait, c'est un peu dans quoi on..."

    mara "Ouais je sais Tomas, on le sait tous."

    ryn colere "On ne va pas voter pour lui donner une liste de gens et de zones à pulvériser."

    nyra raison "Non c'est clairement pas acceptable."

    tomas stress "Mais tu crains pas que les gens vont en avoir en grand nombre."

    elias "Ouais je vois où tu veux en venir."
    elias "Si on peut se cacher derrière ces brouilleurs, rien t'empêche d'en porter constamment sur toi et de ne plus respecter les Commandements."
    elias "En fait y'a un vrai risque de retour du chaos."

    iris desaccord "D'un côté ça serait le meilleur moyen pour affaiblir considérablement Kami !"

    kael doute "Pas forcément. Techniquement, légaliser ne veut pas dire distribuer."
    kael "C'est pas parce qu'ils sont autorisés qu'on va en trouver partout."
    kael "Je vous rappelle qu'il n'y a pas de commerce et que les seuls choses que les gens peuvent avoir viennent des bons de rationnement."

    nyra "En fait si on vote pour ça change rien ?"

    julian inquietude "Ouais, peut-être, mais au moins on aggrave pas la situation."
    julian "Compris Tomas ?"

    tomas "Ou-Ouais..."

    sael mefiant "La majorité est plutôt pour ces brouilleurs alors."
    sael "Tant mieux. Il ne faut pas interdire ça."

    pause 0.4

    think "Ils continuent de discuter… Je les écoute à peine."
    think "Qui est-ce que j’ai vu tout à l’heure… ?"

    noam hesitation "Est-ce que… quelqu’un était dans les couloirs juste avant l’annonce ?"
    noam "Vers la salle de stockage, je veux dire."

    ryn colere "Pourquoi tu demandes ça ?"

    noam "… Laisse tomber."

    # Réponses rapides et naturelles
    tomas fatigue "M-Moi, j’étais déjà ici. Je me disais bien que Kami allait annoncer le prochain vote."
    nyra raison "Moi aussi."
    mara doute "On était à la cafétéria avec Elen."

    elias fatigue "Moi j’étais à la salle de maintenance en train de bricoler."
    elias "Je t’ai vu au loin quand je suis venu au Conclave après l’annonce de Kami."
    elias "Sinon je n'ai croisé personne."

    sael mefiant "Ouais, et t’étais vraiment bizarre tout à l’heure dans le couloir aussi…"

    play sound sfx_heartbeat fadein 1.0
    $ blink()
    "Je cligne lentement des yeux."
    "Il fait chaud, mon coeur bat la chamade."

    think "..."

    $ blink()
    "La salle commence à tanguer légèrement."
    "Un bourdonnement sourd monte dans mes oreilles."
    
    noam fatigue "Je… je me sens pas..."
    
    $ blink()
    "Mes jambes deviennent molles."
    
    scene black with fade
    pause 1.0

    call end_day("11")
    jump _11_0_1_1_REVEIL_CHAMBRE