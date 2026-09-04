# MINI-JEU JOUR 12 — LES CINQ AIGUILLAGES
# Un trolley problem en cinq manches. Chaque décision altère les suivantes.

default j12_trolley_round = 0
default j12_trolley_choice = "upper"
default j12_trolley_time_left = 45.0
default j12_trolley_security = 0
default j12_trolley_freedom = 0
default j12_trolley_history = []
default j12_trolley_switches = 0
default j12_trolley_locked = False
default j12_trolley_last_outcome = None

# Compatibilité avec les embranchements narratifs du jour 13.
default j12011_wire_result = None
default j12011_vote_data = None

init python:
    J12_TROLLEY_DURATION = 45.0
    J12_TROLLEY_TICK = 0.10

    def j12_trolley_reset():
        store.j12_trolley_round = 0
        store.j12_trolley_choice = "upper"
        store.j12_trolley_time_left = J12_TROLLEY_DURATION
        store.j12_trolley_security = 0
        store.j12_trolley_freedom = 0
        store.j12_trolley_history = []
        store.j12_trolley_switches = 0
        store.j12_trolley_locked = False
        store.j12_trolley_last_outcome = None
        store.j12011_wire_result = None
        store.j12011_vote_data = None

    def j12_trolley_prepare_round():
        store.j12_trolley_choice = "upper"
        store.j12_trolley_time_left = J12_TROLLEY_DURATION
        store.j12_trolley_switches = 0
        store.j12_trolley_locked = False

    def j12_trolley_set_choice(route):
        if store.j12_trolley_locked:
            return
        if route != store.j12_trolley_choice:
            store.j12_trolley_choice = route
            store.j12_trolley_switches += 1
            renpy.play("audio/sfx_beep.mp3", channel="sound")

    def j12_trolley_toggle():
        j12_trolley_set_choice("lower" if store.j12_trolley_choice == "upper" else "upper")

    def j12_trolley_tick():
        if store.j12_trolley_locked:
            return
        store.j12_trolley_time_left = max(0.0, store.j12_trolley_time_left - J12_TROLLEY_TICK)

    def j12_trolley_round_data():
        r = store.j12_trolley_round

        if r == 0:
            return {
                "title": "LA PORTE FERMÉE",
                "context": "02 h 17 — Les capteurs médicaux de Mira signalent une anomalie.",
                "briefing": "Deux cents personnes vivent dans une colonie isolée. Elles dépendent des mêmes portes, des mêmes réserves et des mêmes systèmes. Une règle protège pourtant leur dernier espace personnel : aucune surveillance permanente n'est autorisée dans les lieux privés.\n\nCette nuit, Mira est enfermée dans sa chambre. Elle avait légalement désactivé ses capteurs. Derrière la porte, un détecteur résiduel relève un rythme cardiaque irrégulier. Les médecins veulent réactiver toute la surveillance à distance. Mira ne peut pas consentir.",
                "question": "Peut-on franchir une porte privée uniquement parce qu'un danger est possible ?",
                "upper": {
                    "label": "RÉACTIVER LES CAPTEURS",
                    "cost": "Les médecins obtiennent immédiatement ses constantes et peuvent intervenir.",
                    "uncertainty": "Mira a explicitement refusé cette surveillance. Aucun seuil d'urgence n'a jamais été défini.",
                    "aftermath": "Mira va bien. Elle dormait profondément après avoir pris un médicament.\n\nAu réveil, elle apprend que sa chambre a été surveillée contre sa volonté et dépose une plainte : « À quoi sert le droit de couper les caméras si vous pouvez les rallumer dès que vous avez peur ? »\n\nLa polémique commence.",
                },
                "lower": {
                    "label": "RESPECTER SA DÉCISION",
                    "cost": "La chambre reste invisible. Le consentement de Mira demeure valable, même en son absence.",
                    "uncertainty": "Si elle fait réellement un malaise, chaque minute d'attente peut aggraver les séquelles.",
                    "aftermath": "À 03 h 06, Mira appelle elle-même les secours. Elle faisait réellement un malaise et survit.\n\nLes médecins expliquent qu'une intervention quarante minutes plus tôt aurait réduit les complications. Dans les couloirs, une autre phrase se répand : « À quoi sert notre intimité si elle peut nous tuer ? »",
                },
            }

        if r == 1:
            opening = "La plainte de Mira divise encore la colonie." if store.j12_trolley_history and store.j12_trolley_history[0]["route"] == "upper" else "Les complications de Mira alimentent toujours le débat sur les zones privées."
            return {
                "title": "L'OBJET DISPARU",
                "context": opening + " Une cellule énergétique manque au dépôt.",
                "briefing": opening + "\n\nUne cellule énergétique portable disparaît du dépôt technique. Mal manipulée, elle peut provoquer une explosion. Les registres identifient trois personnes présentes dans le secteur, dont Jonas, le médecin qui s'est occupé de Mira.\n\nAucune preuve ne les accuse. La sécurité demande pourtant de fouiller leurs chambres, leurs terminaux et leurs messages privés — sans mandat individuel.",
                "question": "Un risque grave suffit-il à traiter trois personnes comme des coupables ?",
                "upper": {
                    "label": "AUTORISER LA FOUILLE",
                    "cost": "Les trois chambres et leurs communications seront examinées immédiatement.",
                    "uncertainty": "La fouille peut prévenir une explosion, mais révélera aussi tout ce qui n'a aucun rapport avec l'enquête.",
                    "aftermath": "La cellule est retrouvée dans un compartiment technique voisin. Personne ne l'avait volée.\n\nMais les copies des communications révèlent que Jonas entretient secrètement une relation avec une collègue mariée. Il n'a commis aucun crime. L'information se répand malgré tout et il quitte temporairement son poste.\n\nLa menace était imaginaire. L'intrusion, elle, ne l'était pas.",
                },
                "lower": {
                    "label": "REFUSER LA FOUILLE",
                    "cost": "Les recherches resteront limitées aux espaces publics et aux traces liées à l'incident.",
                    "uncertainty": "La cellule demeure dangereuse. Une chambre privée peut aussi servir à cacher une bombe.",
                    "aftermath": "La cellule reste introuvable. Peu après, une explosion secoue un atelier. Elle avait été rangée là par erreur.\n\nUn technicien est grièvement blessé. Personne ne saura si une fouille générale l'aurait retrouvée à temps.\n\nVous avez refusé de fabriquer trois coupables. Vous devez maintenant vivre avec le doute.",
                },
            }

        if r == 2:
            previous = store.j12_trolley_history[1]["route"] if len(store.j12_trolley_history) > 1 else "lower"
            opening = "Après la fouille injustifiée, chacun protège désormais davantage ses secrets." if previous == "upper" else "Après l'explosion, chacun soupçonne la prudence d'avoir été de la faiblesse."
            return {
                "title": "LE MESSAGE",
                "context": opening + " Un canal chiffré déclenche une alerte.",
                "briefing": opening + "\n\nLe système informatique détecte une phrase dans un canal chiffré : « Demain, il ne pourra plus rien faire. » Son auteur a accès aux systèmes techniques.\n\nPour identifier la personne et lire la conversation, les ingénieurs doivent exploiter une vulnérabilité commune à tous les terminaux. Une fois utilisée, cette porte restera ouverte pour les futures enquêtes.",
                "question": "Faut-il ouvrir les messages de tous pour comprendre la menace d'une seule personne ?",
                "upper": {
                    "label": "DÉCHIFFRER LA CONVERSATION",
                    "cost": "L'auteur sera identifié et la menace pourra être vérifiée avant demain.",
                    "uncertainty": "La même clé permettra ensuite d'ouvrir les conversations de chaque habitant innocent.",
                    "aftermath": "Le message concernait réellement un sabotage. Une unité de refroidissement devait être détruite le lendemain. L'auteur est arrêté et des dizaines de vies sont potentiellement sauvées.\n\nQuelques heures plus tard, la méthode devient publique. Le chiffrement privé n'existe plus vraiment. Même ceux qui n'ont rien fait savent que leurs messages peuvent désormais être ouverts.",
                },
                "lower": {
                    "label": "NE PAS DÉCHIFFRER",
                    "cost": "Une menace isolée ne créera pas de passe-partout pour toutes les conversations privées.",
                    "uncertainty": "Le message peut être une métaphore banale. Il peut aussi annoncer exactement ce qu'il semble annoncer.",
                    "aftermath": "Le lendemain, une unité de refroidissement est sabotée. La température monte brutalement et plusieurs secteurs sont évacués. Il y a de nombreux blessés.\n\nLe message était bien une menace. Vous aviez eu l'occasion de le savoir.\n\nLa vulnérabilité demeure fermée. Le saboteur aussi demeure libre.",
                },
            }

        if r == 3:
            previous = store.j12_trolley_history[2]["route"] if len(store.j12_trolley_history) > 2 else "lower"
            opening = "Le sabotage a été évité, mais l'arrestation a révélé une contamination dans l'unité médicale." if previous == "upper" else "Les dégâts du refroidissement ont contaminé une unité médicale pendant l'évacuation."
            return {
                "title": "LE CONFINEMENT",
                "context": opening,
                "briefing": opening + "\n\nPlusieurs habitants présentent les symptômes d'une infection respiratoire inconnue. Les médecins demandent vingt-quatre heures pour identifier l'agent. La sécurité veut verrouiller immédiatement tous les secteurs.\n\nUne femme transporte le médicament de son père. Un couple tente de rejoindre son enfant hospitalisé. Un médecin doit traverser trois zones. Après les décisions précédentes, une partie de la population refuse désormais qu'on choisisse encore à sa place.",
                "question": "Peut-on enfermer deux cents personnes pour empêcher un risque encore mal compris ?",
                "upper": {
                    "label": "IMPOSER LE CONFINEMENT",
                    "cost": "Toutes les portes seront verrouillées pendant vingt-quatre heures, sans exception individuelle.",
                    "uncertainty": "L'infection peut être bénigne. Certaines urgences ordinaires ne supporteront pas l'attente.",
                    "aftermath": "La contamination était réelle et dangereuse. Grâce au confinement, seuls quelques habitants sont infectés.\n\nMais le père qui attendait son médicament meurt pendant la nuit. Sa fille avait le traitement dans son sac. Deux portes les séparaient. Elle n'a pas été autorisée à les franchir.\n\nVous avez contenu l'épidémie. Vous avez aussi décidé quelle urgence comptait le plus.",
                },
                "lower": {
                    "label": "LAISSER CHACUN DÉCIDER",
                    "cost": "Le risque sera annoncé et l'isolement recommandé, mais aucune porte ne sera verrouillée.",
                    "uncertainty": "La majorité respectera probablement la consigne. Une seule exception peut suffire.",
                    "aftermath": "La grande majorité des habitants reste volontairement chez elle. Quelques dizaines circulent. Une seule personne contaminée suffit.\n\nTrois jours plus tard, l'infection s'est propagée à plusieurs secteurs. Certaines victimes n'avaient jamais quitté leur chambre et avaient respecté chaque recommandation.\n\nD'autres ont choisi le risque pour elles.",
                },
            }

        recap = "Après quatre crises, chaque décision a protégé certains habitants et exposé les autres. La colonie ne sait plus quel risque elle accepte encore de partager."
        return {
            "title": "LA PROPOSITION",
            "context": recap,
            "briefing": recap + "\n\nLa confiance est détruite. Les ingénieurs proposent un système de prévention analysant en permanence déplacements, conversations, constantes médicales, accès et comportements inhabituels. Aucun agent humain ne consulterait librement les données : une intelligence artificielle ne transmettrait que les alertes graves.\n\nLes simulations affirment que 91 % des incidents récents auraient été évités. Mais le système exige une condition absolue : aucune zone invisible. Aucune chambre. Aucun message. Aucun moment.",
            "question": "Une surveillance qui fonctionne cesse-t-elle d'être une privation de liberté ?",
            "upper": {
                "label": "ACTIVER LE SYSTÈME",
                "cost": "Le système promet de prévenir les urgences sans laisser les agents explorer librement les vies privées.",
                "uncertainty": "Il peut ne jamais être détourné. Une population protégée peut simplement ne plus accepter de vivre sans lui.",
                "aftermath": "Les mois suivants sont remarquablement calmes. Les accidents diminuent, plusieurs urgences sont détectées à temps, deux agressions et un sabotage sont empêchés.\n\nLe système ne devient pas tyrannique. Il n'accuse pas d'innocents. Il fait exactement ce qui était promis.\n\nQuelques mois plus tard, presque personne ne veut prendre le risque de le désactiver. La colonie n'a jamais été aussi sûre. Et personne n'est plus jamais réellement seul.",
            },
            "lower": {
                "label": "REFUSER LE SYSTÈME",
                "cost": "Certaines chambres et conversations resteront invisibles. Chacun pourra encore cacher, mentir ou être seul.",
                "uncertainty": "Les mêmes angles morts qui protègent l'intimité protégeront aussi les erreurs, les violences et les préparatifs criminels.",
                "aftermath": "La vie reprend avec ses secrets, ses surprises et ses zones invisibles.\n\nSix mois plus tard, un habitant est tué dans sa chambre. L'enquête découvre chez son agresseur plusieurs comportements que le système aurait détectés. Le meurtre aurait probablement été empêché.\n\nVous avez conservé un monde dans lequel chacun peut disparaître du regard des autres. Le meurtrier aussi.",
            },
        }

    def j12_trolley_resolve(route):
        store.j12_trolley_locked = True
        data = j12_trolley_round_data()
        picked = data[route]

        if route == "upper":
            store.j12_trolley_security += 1
        else:
            store.j12_trolley_freedom += 1

        outcome = {
            "round": store.j12_trolley_round + 1,
            "route": route,
            "label": picked["label"],
            "aftermath": picked["aftermath"],
            "switches": store.j12_trolley_switches,
        }
        store.j12_trolley_history.append(outcome)
        store.j12_trolley_last_outcome = outcome
        store.j12_trolley_round += 1
        return outcome

    def j12_trolley_finalize():
        # Conserve les deux routes attendues par le jour 13.
        store.j12011_wire_result = "security" if store.j12_trolley_security > store.j12_trolley_freedom else "freedom"
        store.j12011_vote_data = {
            "result": store.j12011_wire_result,
            "security": store.j12_trolley_security,
            "freedom": store.j12_trolley_freedom,
            "history": list(store.j12_trolley_history),
        }
        return store.j12011_vote_data

    class J12TrolleyTrack(renpy.Displayable):
        """Rails vectoriels stables, indépendants de la résolution de la texture."""

        def __init__(self, selected="upper", **kwargs):
            super(J12TrolleyTrack, self).__init__(**kwargs)
            self.selected = selected

        def render(self, width, height, st, at):
            result = renpy.Render(1920, 1080)
            canvas = result.canvas()

            start = (170, 560)
            split = (805, 560)
            upper = (1190, 350)
            lower = (1190, 750)

            # Ombre des rails, puis branche active et cœur lumineux.
            canvas.line("#02080ddd", start, split, 30)
            canvas.line("#02080ddd", split, upper, 30)
            canvas.line("#02080ddd", split, lower, 30)
            canvas.line("#275364", start, split, 15)
            canvas.line("#63e9f4", start, split, 5)

            upper_color = "#62edff" if self.selected == "upper" else "#244653"
            lower_color = "#62edff" if self.selected == "lower" else "#244653"
            canvas.line(upper_color, split, upper, 15)
            canvas.line(lower_color, split, lower, 15)
            canvas.line("#e8fdff" if self.selected == "upper" else "#47717e", split, upper, 4)
            canvas.line("#e8fdff" if self.selected == "lower" else "#47717e", split, lower, 4)

            canvas.circle("#06121b", split, 29, 0)
            canvas.circle("#dffcff", split, 18, 3)
            canvas.circle("#69eaff", upper, 15, 3)
            canvas.circle("#69eaff", lower, 15, 3)
            return result


transform j12_trolley_kami_idle:
    subpixel True
    yoffset 0
    ease 0.45 yoffset -7
    ease 0.45 yoffset 0
    repeat

transform j12_trolley_warning:
    alpha 0.45
    linear 0.35 alpha 1.0
    linear 0.35 alpha 0.45
    repeat

style j12_trolley_title:
    font gui.name_text_font
    size 43
    color "#eafcff"
    bold True

style j12_trolley_text:
    font gui.interface_text_font
    size 27
    color "#ccebf3"

style j12_trolley_small:
    font gui.interface_text_font
    size 22
    color "#8fb8c5"

style j12_trolley_button:
    background Solid("#071827e8")
    hover_background Solid("#12384aea")
    selected_background Solid("#0d5268f2")
    padding (22, 15)

style j12_trolley_button_text:
    font gui.name_text_font
    size 27
    color "#d9faff"
    hover_color "#ffffff"
    selected_color "#71edff"
    text_align 0.5


screen j12_trolley_intro():
    modal True
    add "gui/day12/trolley_dilemma/bg_control_chamber.png":
        xysize (1920, 1080)
    add Solid("#02070cc4")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1240
        background Solid("#06131ff2")
        padding (50, 38)
        vbox:
            spacing 22
            text "LES CINQ AIGUILLAGES" style "j12_trolley_title" xalign 0.5
            text "Kami avance seule. La voie se divise, mais elle ne s'arrête jamais." style "j12_trolley_text" xalign 0.5 text_align 0.5
            text "Cinq crises vont mettre vos principes à l'épreuve. Chaque décision laissera une trace dans la manche suivante." style "j12_trolley_text" xalign 0.5 text_align 0.5
            text "À chaque manche, vous aurez 45 secondes pour déplacer l'aiguillage. Les voies n'ont ni nom ni valeur prédéfinie : seuls leurs effets vous sont présentés." style "j12_trolley_text" xalign 0.5 text_align 0.5
            text "Aucune voie n'est propre. Vous devrez seulement décider quel risque la colonie doit accepter." style "j12_trolley_text" color "#ffb36b" xalign 0.5
            null height 8
            textbutton "LANCER LA SIMULATION":
                xalign 0.5
                action Return(True)
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"


screen j12_trolley_briefing(data):
    modal True
    add "gui/day12/trolley_dilemma/bg_control_chamber.png":
        xysize (1920, 1080)
    add Solid("#02070cda")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1370
        background Solid("#06131ff5")
        padding (55, 42)
        vbox:
            spacing 20
            text "MANCHE [j12_trolley_round + 1]/5" style "j12_trolley_small" color "#69e9ff" xalign 0.5
            text data["title"] style "j12_trolley_title" xalign 0.5
            text data["briefing"] style "j12_trolley_text" size 25 xalign 0.5 text_align 0.5 xmaximum 1240
            frame:
                xfill True
                background Solid("#0b2634e8")
                padding (28, 18)
                text data["question"] style "j12_trolley_text" color "#ffffff" xalign 0.5 text_align 0.5
            textbutton "OUVRIR L'AIGUILLAGE — 45 S":
                xalign 0.5
                action Return(True)
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"


screen j12_trolley_round_screen():
    modal True
    timer J12_TROLLEY_TICK repeat True action Function(j12_trolley_tick)
    timer J12_TROLLEY_DURATION action [SetVariable("j12_trolley_locked", True), Return(j12_trolley_choice)]

    $ data = j12_trolley_round_data()
    $ elapsed = max(0.0, J12_TROLLEY_DURATION - j12_trolley_time_left)
    $ progress = min(1.0, elapsed / J12_TROLLEY_DURATION)
    $ rail_progress = min(1.0, progress / 0.88)
    $ before_split = min(1.0, rail_progress / 0.55)
    $ after_split = max(0.0, (rail_progress - 0.55) / 0.45)
    $ kami_x = int(170 + 635 * before_split) if rail_progress <= 0.55 else int(805 + 385 * after_split)
    $ endpoint_y = 350 if j12_trolley_choice == "upper" else 750
    $ kami_y = 560 if rail_progress <= 0.55 else int(560 + (endpoint_y - 560) * after_split)
    $ timer_width = int(390 * max(0.0, j12_trolley_time_left) / J12_TROLLEY_DURATION)

    add "gui/day12/trolley_dilemma/bg_control_chamber.png":
        xysize (1920, 1080)
    add Solid("#02091252")

    frame:
        xpos 90
        ypos 45
        xsize 1740
        ysize 140
        background Solid("#06131fe8")
        padding (28, 17)
        vbox:
            spacing 5
            hbox:
                spacing 35
                text "MANCHE [j12_trolley_round + 1]/5" style "j12_trolley_small" color "#69e9ff"
            text data["title"] style "j12_trolley_title"
            text data["context"] style "j12_trolley_small" xmaximum 1120

    frame:
        xpos 1370
        ypos 64
        xsize 390
        background None
        vbox:
            spacing 8
            text ("%.1f s" % j12_trolley_time_left) style "j12_trolley_title" color ("#ff6475" if j12_trolley_time_left < 10.0 else "#eafcff") xalign 1.0
            fixed:
                xsize 390
                ysize 16
                add Solid("#132d38", xysize=(390, 16))
                add Solid("#ff6475" if j12_trolley_time_left < 10.0 else "#62e7ff", xysize=(timer_width, 16))

    frame:
        xpos 140
        ypos 205
        xsize 1060
        background Solid("#06131fda")
        padding (28, 18)
        text data["question"] style "j12_trolley_text" color "#f1fbff" text_align 0.5 xalign 0.5

    # Un seul embranchement en Y, dessiné dans le repère natif 1920×1080.
    add J12TrolleyTrack(j12_trolley_choice)

    add "gui/day12/trolley_dilemma/kami_trolley.png" at j12_trolley_kami_idle:
        xpos kami_x
        ypos kami_y
        xanchor 0.5
        yanchor 0.5
        xsize 132
        ysize 132
        fit "contain"

    frame:
        xpos 1270
        ypos 215
        xsize 560
        ysize 290
        background (Solid("#0a4557ee") if j12_trolley_choice == "upper" else Solid("#071521e8"))
        padding (22, 16)
        vbox:
            spacing 7
            textbutton data["upper"]["label"]:
                action Function(j12_trolley_set_choice, "upper")
                selected j12_trolley_choice == "upper"
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"
                xfill True
            text data["upper"]["cost"] style "j12_trolley_small" size 20 xmaximum 510
            text ("INCERTITUDE — " + data["upper"]["uncertainty"]) style "j12_trolley_small" size 18 color "#e3c987" xmaximum 510

    frame:
        xpos 1270
        ypos 625
        xsize 560
        ysize 290
        background (Solid("#0a4557ee") if j12_trolley_choice == "lower" else Solid("#071521e8"))
        padding (22, 16)
        vbox:
            spacing 7
            textbutton data["lower"]["label"]:
                action Function(j12_trolley_set_choice, "lower")
                selected j12_trolley_choice == "lower"
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"
                xfill True
            text data["lower"]["cost"] style "j12_trolley_small" size 20 xmaximum 510
            text ("INCERTITUDE — " + data["lower"]["uncertainty"]) style "j12_trolley_small" size 18 color "#e3c987" xmaximum 510

    textbutton "CHANGER L'AIGUILLAGE":
        xpos 455
        ypos 905
        xsize 760
        action Function(j12_trolley_toggle)
        style "j12_trolley_button"
        text_style "j12_trolley_button_text"

    if j12_trolley_time_left < 10.0:
        text "DÉCISION IMMINENTE" style "j12_trolley_title" color "#ff596b" at j12_trolley_warning:
            xpos 630
            ypos 995


screen j12_trolley_outcome(outcome):
    modal True
    add "gui/day12/trolley_dilemma/bg_control_chamber.png":
        xysize (1920, 1080)
    add Solid("#02070cd8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1150
        background Solid("#06131ff2")
        padding (48, 36)
        vbox:
            spacing 19
            text "DÉCISION ENREGISTRÉE" style "j12_trolley_title" color "#69e9ff" xalign 0.5
            text outcome["label"] style "j12_trolley_title" xalign 0.5
            text outcome["aftermath"] style "j12_trolley_text" size 24 xalign 0.5 text_align 0.5 xmaximum 1000
            textbutton ("MANCHE SUIVANTE" if j12_trolley_round < 5 else "VOIR LE BILAN"):
                xalign 0.5
                action Return(True)
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"


screen j12_trolley_result(result_data):
    modal True
    add "gui/day12/trolley_dilemma/bg_control_chamber.png":
        xysize (1920, 1080)
    add Solid("#02070cd0")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1390
        background Solid("#06131ff4")
        padding (48, 32)
        vbox:
            spacing 16
            text "FIN DE LA SIMULATION" style "j12_trolley_title" xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                vbox:
                    text "SÉCURITÉ" style "j12_trolley_small" color "#69e9ff" xalign 0.5
                    text ("%d/5" % result_data["security"]) style "j12_trolley_title" color "#69e9ff" size 68 xalign 0.5
                vbox:
                    text "LIBERTÉ" style "j12_trolley_small" color "#ffb36b" xalign 0.5
                    text ("%d/5" % result_data["freedom"]) style "j12_trolley_title" color "#ffb36b" size 68 xalign 0.5
            text "Il n'existe aucun score parfait : seulement la forme de société que vos décisions ont dessinée." style "j12_trolley_text" size 24 xalign 0.5 text_align 0.5
            null height 8
            for item in result_data["history"]:
                hbox:
                    xfill True
                    spacing 22
                    text ("%d" % item["round"]) style "j12_trolley_small" color "#65e8ff" xsize 45
                    text item["label"] style "j12_trolley_small" xsize 620
                    text ("%d bascule%s" % (item["switches"], "s" if item["switches"] != 1 else "")) style "j12_trolley_small"
            null height 10
            text "Combien de risques une société doit-elle accepter pour que ses habitants puissent encore lui échapper ?" style "j12_trolley_text" size 23 xalign 0.5 text_align 0.5
            text "Combien de liberté êtes-vous prêt à retirer aux autres pour ne plus vivre avec ces risques ?" style "j12_trolley_text" size 23 color "#ffcf9e" xalign 0.5 text_align 0.5
            textbutton "RETOUR AU CONCLAVE":
                xalign 0.5
                action Return(result_data)
                style "j12_trolley_button"
                text_style "j12_trolley_button_text"


label j12_play_trolley_problem:
    $ j12_trolley_reset()
    play sound "audio/sfx_minigame_start.mp3"
    call screen j12_trolley_intro

    while j12_trolley_round < 5:
        $ j12_trolley_briefing_data = j12_trolley_round_data()
        call screen j12_trolley_briefing(j12_trolley_briefing_data)
        $ j12_trolley_prepare_round()
        call screen j12_trolley_round_screen
        $ j12_trolley_route = _return
        $ j12_trolley_outcome_data = j12_trolley_resolve(j12_trolley_route)
        call screen j12_trolley_outcome(j12_trolley_outcome_data)

    $ j12_trolley_result_data = j12_trolley_finalize()
    call screen j12_trolley_result(j12_trolley_result_data)
    return j12_trolley_result_data
