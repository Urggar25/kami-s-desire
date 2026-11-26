# Jour 7 - Enquête sur le matériel disparu
# Deux découvertes structurantes garanties ; trois pistes complémentaires choisies par le joueur.

default j701_investigation_found = []
default j701_investigation_turn = 0
default j701_investigation_theory = "inconnue"

init python:
    J701_INVESTIGATION_MAX_TURNS = 4

    J701_INVESTIGATION_ROOMS = [
        {"id": "cafeteria", "title": "CAFÉTÉRIA", "subtitle": "Reprendre les témoignages", "color": "#42D9FF"},
        {"id": "stockage", "title": "STOCKAGE", "subtitle": "Reconstituer le prélèvement", "color": "#FFD34E"},
        {"id": "maintenance", "title": "MAINTENANCE", "subtitle": "Chercher ce qui a été fabriqué", "color": "#6DFF9B"},
        {"id": "observation", "title": "OBSERVATION", "subtitle": "Interroger les images", "color": "#B88CFF"},
        {"id": "sas", "title": "SAS DE LIVRAISON", "subtitle": "Suivre le trajet du matériel", "color": "#FF6B8A"},
    ]

    J701_INVESTIGATION_CLUES = [
        {
            "id": "elias_testimony", "room": "cafeteria", "number": "01",
            "location": "CAFÉTÉRIA", "title": "LA DERNIÈRE VISITE",
            "summary": "Elias a manipulé les quatre objets hier soir. À 23 h 47, ils étaient encore tous à leur place.",
            "color": "#42D9FF",
        },
        {
            "id": "foil_crane", "room": "cafeteria", "number": "02",
            "location": "CAFÉTÉRIA", "title": "LA GRUE D'ARGENT",
            "summary": "Un origami en emballage de ration était pris dans une roue du chariot. Elen en plie souvent, mais les laisse sur toutes les tables.",
            "color": "#42D9FF",
        },
        {
            "id": "counterweight", "room": "stockage", "number": "03",
            "location": "STOCKAGE", "title": "LE POIDS FANTÔME",
            "summary": "Les batteries ont été remplacées par des poches d'eau du même poids afin de tromper le capteur de l'étagère.",
            "color": "#FFD34E",
        },
        {
            "id": "blank_receipt", "room": "stockage", "number": "04",
            "location": "STOCKAGE", "title": "LE REÇU SANS NOM",
            "summary": "Le terminal a bien autorisé un retrait à 02 h 14, mais la case réservée à l'identité contient seulement un caractère impossible.",
            "color": "#FFD34E",
        },
        {
            "id": "brown_hair", "room": "maintenance", "number": "05",
            "location": "MAINTENANCE", "title": "LE CHEVEU COUPÉ",
            "summary": "Un cheveu brun et assez court était coincé dans l'établi. Son extrémité est tranchée net et il ne porte aucune racine.",
            "color": "#6DFF9B",
        },
        {
            "id": "negative_blueprint", "room": "maintenance", "number": "06",
            "location": "MAINTENANCE", "title": "LE PLAN EN NÉGATIF",
            "summary": "La limaille magnétique dessine la silhouette d'un adaptateur fabriqué ici, emporté ensuite, et dont le plan a été soigneusement effacé.",
            "color": "#6DFF9B",
        },
        {
            "id": "kael_database", "room": "observation", "number": "07",
            "location": "OBSERVATION", "title": "LA REQUÊTE DE KAEL",
            "summary": "Kael tente seul d'entrer dans la base des caméras et masque sa requête lorsque Noam approche.",
            "color": "#B88CFF",
        },
        {
            "id": "maintenance_log", "room": "observation", "number": "08",
            "location": "OBSERVATION", "title": "LE LOG DE 02 H 34",
            "summary": "Les logs de sécurité indiquent que la porte de la maintenance s'est ouverte à 02 h 34, sans enregistrer l'identité de l'utilisateur.",
            "color": "#B88CFF",
        },
        {
            "id": "vertical_tracks", "room": "sas", "number": "09",
            "location": "SAS", "title": "LES TRACES VERTICALES",
            "summary": "Les marques du chariot quittent le sol et continuent sur une porte. La cargaison a été fixée à un plateau magnétique.",
            "color": "#FF6B8A",
        },
        {
            "id": "impossible_echo", "room": "sas", "number": "10",
            "location": "SAS", "title": "L'ÉCHO IMPOSSIBLE",
            "summary": "Le micro du sas a enregistré deux bips de la même porte séparés de sept secondes, alors que son verrou exige douze secondes.",
            "color": "#FF6B8A",
        },
    ]

    J701_INVESTIGATION_HOTSPOTS = {
        "cafeteria": [
            {"clue": "elias_testimony", "x": 255, "y": 275, "w": 390, "h": 760, "hint": "Interroger Elias"},
            {"clue": "foil_crane", "x": 780, "y": 610, "w": 520, "h": 300, "hint": "Examiner la table"},
        ],
        "stockage": [
            {"clue": "counterweight", "x": 70, "y": 250, "w": 650, "h": 560, "hint": "Inspecter les emplacements vides"},
            {"clue": "blank_receipt", "x": 1725, "y": 390, "w": 180, "h": 250, "hint": "Consulter le boîtier de porte"},
        ],
        "maintenance": [
            {"clue": "brown_hair", "x": 420, "y": 560, "w": 560, "h": 300, "hint": "Regarder sous l'établi"},
            {"clue": "negative_blueprint", "x": 990, "y": 360, "w": 780, "h": 320, "hint": "Étudier le plan de travail"},
        ],
        "observation": [
            {"clue": "kael_database", "x": 175, "y": 250, "w": 430, "h": 780, "hint": "Surprendre Kael"},
            {"clue": "maintenance_log", "x": 1390, "y": 420, "w": 510, "h": 350, "hint": "Accéder aux logs de sécurité"},
        ],
        "sas": [
            {"clue": "vertical_tracks", "x": 875, "y": 230, "w": 620, "h": 570, "hint": "Suivre les marques"},
            {"clue": "impossible_echo", "x": 390, "y": 390, "w": 500, "h": 340, "hint": "Écouter le terminal"},
        ],
    }

    J701_INVESTIGATION_BY_ID = dict((clue["id"], clue) for clue in J701_INVESTIGATION_CLUES)
    J701_INVESTIGATION_ROOM_BY_ID = dict((room["id"], room) for room in J701_INVESTIGATION_ROOMS)

    def j701_investigation_reset():
        store.j701_investigation_found = []
        store.j701_investigation_turn = 0
        store.j701_investigation_theory = "inconnue"

    def j701_investigation_collect(clue_id):
        found = list(store.j701_investigation_found)
        if clue_id not in found and len(found) < J701_INVESTIGATION_MAX_TURNS:
            found.append(clue_id)
            store.j701_investigation_found = found
            store.j701_investigation_turn = len(found)

    def j701_investigation_clue(clue_id):
        return J701_INVESTIGATION_BY_ID.get(clue_id, J701_INVESTIGATION_CLUES[0])

    def j701_investigation_room_remaining(room_id):
        found = set(getattr(store, "j701_investigation_found", []))
        return len([clue for clue in J701_INVESTIGATION_CLUES if clue["room"] == room_id and clue["id"] not in found])

    def j701_investigation_prepare_room(room_id):
        numbers = room_scene_variant_numbers(room_id)
        if numbers:
            indices = dict(getattr(store, "room_scene_indices", {}))
            indices[room_id] = numbers[0]
            store.room_scene_indices = indices


transform j701_inv_intro_slam:
    alpha 0.0
    zoom 2.2
    rotate -7
    easeout 0.20 alpha 1.0 zoom 0.92 rotate 2
    easein 0.10 zoom 1.0 rotate 0

transform j701_inv_card_in(delay=0.0):
    alpha 0.0
    xoffset -90
    pause delay
    easeout 0.28 alpha 1.0 xoffset 0
    on hover:
        easeout 0.10 xoffset 16
    on idle:
        easein 0.10 xoffset 0

transform j701_inv_scanline:
    ypos -40
    alpha 0.0
    linear 0.15 alpha 0.65
    linear 1.25 ypos 1080 alpha 0.0
    repeat

transform j701_inv_evidence_slam:
    alpha 0.0
    zoom 1.8
    rotate 5
    easeout 0.16 alpha 1.0 zoom 0.94 rotate -1
    easein 0.10 zoom 1.0 rotate 0

transform j701_inv_pulse:
    alpha 0.32
    linear 0.55 alpha 0.75
    linear 0.55 alpha 0.32
    repeat


screen j701_investigation_intro():
    modal True
    zorder 250

    add Solid("#02050A")
    add Solid("#FF335544") xpos -200 ypos 410 xsize 2320 ysize 230 at Transform(rotate=-4)
    add Solid("#39D9FF33") xpos -200 ypos 500 xsize 2320 ysize 12 at Transform(rotate=3)

    vbox at j701_inv_intro_slam:
        xalign 0.5
        yalign 0.48
        spacing -4

        text "PHASE D'ENQUÊTE":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 92
            color "#FFFFFF"
            outlines [(5, "#07111F", 0, 0), (9, "#FF3355", 0, 0)]
            xalign 0.5

        text "2 DÉCOUVERTES  /  2 PISTES À CHOISIR  /  UNE NUIT":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 31
            color "#8EEAFF"
            kerning 3
            xalign 0.5

    text "Le vol est établi. Choisis maintenant quelles pistes approfondir.":
        font "fonts/Barlow-Light.ttf"
        size 25
        color "#D7E8F4"
        xalign 0.5
        yalign 0.78

    timer 2.6 action Return(True)


screen j701_investigation_locations():
    modal True
    zorder 250

    add Solid("#03070D")
    add Solid("#071827") xpos 0 ypos 0 xsize 1920 ysize 154
    add Solid("#FF3355") xpos 0 ypos 150 xsize 1920 ysize 4
    add Solid("#36D9FF") xpos 0 ypos 154 xsize 680 ysize 3
    add Solid("#7CEBFF") xpos 0 ypos 0 xsize 1920 ysize 3 at j701_inv_scanline

    text "DOSSIER 07-A  //  CHOISIR UN LIEU":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 42
        color "#F4FAFF"
        xpos 92
        ypos 38

    text "LE CONTENU DES SALLES RESTE INCONNU TANT QUE TU NE L'EXAMINES PAS":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 22
        color "#7FDBF2"
        xpos 96
        ypos 96
        kerning 2

    text "TOUR [j701_investigation_turn + 1] / [J701_INVESTIGATION_MAX_TURNS]":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 34
        color "#FFD34E"
        xalign 0.91
        ypos 48

    for slot in range(J701_INVESTIGATION_MAX_TURNS):
        $ filled = slot < len(j701_investigation_found)
        add Solid("#FFD34E" if filled else "#243445"):
            xpos 1480 + slot * 68
            ypos 105
            xsize 52
            ysize 8

    for idx, room in enumerate(J701_INVESTIGATION_ROOMS):
        $ remaining = j701_investigation_room_remaining(room["id"])

        button at j701_inv_card_in(idx * 0.055):
            xpos 300
            ypos 205 + idx * 153
            xsize 1320
            ysize 126
            padding (20, 13)
            background Solid("#101C29F2" if remaining else "#091018CC")
            hover_background Solid(room["color"] + "38")
            insensitive_background Solid("#071018CC")
            sensitive remaining > 0
            action [Play("sound", "audio/sfx_qte_hit.wav"), Return(room["id"])]

            fixed:
                add Solid(room["color"] if remaining else "#34404B") xpos 0 ypos 0 xsize 8 ysize 100

                text "0[idx + 1]":
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 42
                    color (room["color"] if remaining else "#53606B")
                    xpos 28
                    yalign 0.5

                vbox:
                    xpos 108
                    yalign 0.5
                    xsize 920
                    spacing 5

                    text kd_tr(room["title"]):
                        font "fonts/Rajdhani-SemiBold.ttf"
                        size 31
                        color (room["color"] if remaining else "#53606B")
                        kerning 2

                    text kd_tr("PLUS RIEN À EXAMINER" if not remaining else room["subtitle"]):
                        font "fonts/Barlow-Light.ttf"
                        size 23
                        color ("#61707C" if not remaining else "#F1F6FA")

                text ("{} {}".format(remaining, kd_tr("POINT D'INTÉRÊT" if remaining == 1 else "POINTS D'INTÉRÊT"))):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 23
                    color (room["color"] if remaining else "#53606B")
                    xalign 0.96
                    yalign 0.5

    frame:
        xpos 120
        ypos 1023
        xsize 1680
        ysize 38
        padding (14, 5)
        background Solid("#07131FEE")

        text "Entrer dans une salle est gratuit. Seul un indice collecté consomme un tour.":
            font "fonts/Barlow-Light.ttf"
            size 20
            color "#93A9BA"
            xalign 0.5


screen j701_investigation_pointclick(room_id):
    modal True
    zorder 250
    default hovered_hint = "Déplace le curseur sur le décor et cherche ce qui ne colle pas."

    $ room = J701_INVESTIGATION_ROOM_BY_ID[room_id]
    $ hotspots = J701_INVESTIGATION_HOTSPOTS.get(room_id, [])

    add Solid("#000")
    use room_scene_background(room_id, navigation=False)
    add Solid("#02060C44")

    frame:
        xpos 38
        ypos 30
        xsize 720
        padding (22, 14)
        background Solid("#07131FEF")
        vbox:
            spacing 3
            text kd_tr(room["title"]) font "fonts/Rajdhani-SemiBold.ttf" size 37 color room["color"]
            text kd_tr(hovered_hint) font "fonts/Barlow-Light.ttf" size 23 color "#ECF6FC"

    frame:
        xalign 0.98
        yalign 0.035
        padding (18, 11)
        background Solid("#07131FEF")
        text "TOUR [j701_investigation_turn + 1] / [J701_INVESTIGATION_MAX_TURNS]" font "fonts/Rajdhani-SemiBold.ttf" size 28 color "#FFD34E"

    for hotspot in hotspots:
        $ clue_id = hotspot["clue"]
        $ available = clue_id not in j701_investigation_found

        if available and clue_id == "elias_testimony":
            imagebutton:
                idle Transform(character_image("elias", "reflechit"), zoom=1.00)
                hover Transform(character_image("elias", "inquiet"), zoom=1.00)
                focus_mask True
                xalign 0.25
                yalign 1.00
                hovered SetScreenVariable("hovered_hint", hotspot["hint"])
                unhovered SetScreenVariable("hovered_hint", "Déplace le curseur sur le décor et cherche ce qui ne colle pas.")
                action [Play("sound", "audio/sfx_qte_hit.wav"), Return(clue_id)]

        elif available and clue_id == "kael_database":
            imagebutton:
                idle Transform(character_image("kael", "reflechit"), zoom=1.00)
                hover Transform(character_image("kael", "surpris"), zoom=1.00)
                focus_mask True
                xalign 0.27
                yalign 1.00
                hovered SetScreenVariable("hovered_hint", hotspot["hint"])
                unhovered SetScreenVariable("hovered_hint", "Déplace le curseur sur le décor et cherche ce qui ne colle pas.")
                action [Play("sound", "audio/sfx_qte_hit.wav"), Return(clue_id)]

        elif available:
            button:
                xpos hotspot["x"]
                ypos hotspot["y"]
                xsize hotspot["w"]
                ysize hotspot["h"]
                padding (0, 0)
                background Solid("#00000001")
                hover_background Solid(room["color"] + "20")
                hovered SetScreenVariable("hovered_hint", hotspot["hint"])
                unhovered SetScreenVariable("hovered_hint", "Déplace le curseur sur le décor et cherche ce qui ne colle pas.")
                action [Play("sound", "audio/sfx_qte_hit.wav"), Return(clue_id)]

                text "◇" at j701_inv_pulse:
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 52
                    color room["color"]
                    outlines [(2, "#071018", 0, 0)]
                    xalign 0.5
                    yalign 0.5

    textbutton "<  RETOUR AU PLAN":
        xpos 38
        yalign 0.96
        xsize 330
        ysize 62
        text_font "fonts/Rajdhani-SemiBold.ttf"
        text_size 23
        text_color "#DCEBF5"
        text_hover_color "#FFFFFF"
        background Solid("#07131FEF")
        hover_background Solid(room["color"] + "66")
        action Return(None)


screen j701_investigation_evidence(clue_id):
    modal True
    zorder 270

    $ clue = j701_investigation_clue(clue_id)

    add Solid("#020409F2")
    add Solid(clue["color"] + "44") xpos -240 ypos 390 xsize 2400 ysize 280 at Transform(rotate=-5)
    add Solid("#FFFFFF18") xpos -100 ypos 505 xsize 2200 ysize 5 at j701_inv_pulse

    vbox at j701_inv_evidence_slam:
        xalign 0.5
        yalign 0.48
        xsize 1420
        spacing 13

        text "FRAGMENT DE PREUVE OBTENU":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 32
            color clue["color"]
            kerning 4
            xalign 0.5

        text kd_tr(clue["title"]):
            font "fonts/Rajdhani-SemiBold.ttf"
            size 76
            color "#FFFFFF"
            outlines [(5, "#050A12", 0, 0)]
            xalign 0.5
            text_align 0.5

        text kd_tr(clue["summary"]):
            font "fonts/Barlow-Light.ttf"
            size 29
            color "#E8F2F8"
            xalign 0.5
            text_align 0.5

    text "[len(j701_investigation_found)] / [J701_INVESTIGATION_MAX_TURNS]":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 30
        color "#FFFFFF"
        xalign 0.5
        yalign 0.82

    timer 2.8 action Return(True)


screen j701_investigation_dossier():
    modal True
    zorder 250

    add Solid("#03070DF5")

    text "DOSSIER PROVISOIRE":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 58
        color "#FFFFFF"
        xpos 110
        ypos 54

    text "4 fragments récupérés  //  6 pistes non examinées":
        font "fonts/Rajdhani-SemiBold.ttf"
        size 25
        color "#FF6B8A"
        xpos 114
        ypos 124
        kerning 2

    for idx, clue_id in enumerate(j701_investigation_found):
        $ clue = j701_investigation_clue(clue_id)

        frame at j701_inv_card_in(idx * 0.07):
            xpos 170
            ypos 205 + idx * 137
            xsize 1580
            ysize 112
            padding (22, 12)
            background Solid("#0D1A27F2")

            fixed:
                add Solid(clue["color"]) xpos 0 ypos 0 xsize 7 ysize 88
                text clue["number"]:
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 38
                    color clue["color"]
                    xpos 28
                    yalign 0.5
                vbox:
                    xpos 105
                    yalign 0.5
                    spacing 1
                    text kd_tr(clue["title"]) font "fonts/Rajdhani-SemiBold.ttf" size 27 color "#FFFFFF"
                    text kd_tr(clue["summary"]) font "fonts/Barlow-Light.ttf" size 22 color "#B9CAD7"

    textbutton "REJOINDRE LE DÉBRIEF  >":
        xalign 0.5
        ypos 930
        xsize 560
        ysize 72
        text_font "fonts/Rajdhani-SemiBold.ttf"
        text_size 28
        text_color "#071018"
        text_hover_color "#071018"
        background Solid("#FFD34E")
        hover_background Solid("#FFFFFF")
        action [Play("sound", "audio/sfx_minigame_start.mp3"), Return(True)]


label j701_investigation:
    $ hideGroup()
    $ j701_investigation_reset()
    stop music fadeout 0.8
    scene black
    play sound "audio/sfx_minigame_start.mp3"
    call screen j701_investigation_intro
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([("nyra", "neutre", 0.25), ("elias", "inquiet", 0.55), ("noam", "reflechit", 0.85)])
    elias "On peut demander à Goumi de chercher aussi ? Il passe dans toutes les salles, il a peut-être déplacé mes affaires."
    nyra "Avant d'envoyer qui que ce soit, je veux voir les emplacements. Ensuite, l'atelier. Si on sait ce qui manque et ce qu'on peut en faire, on saura peut-être où chercher."
    elias "Bon. Venez, je vais vous montrer."
    $ hideGroup()
    call j701_clue_counterweight from _call_j701_core_counterweight
    $ j701_investigation_collect("counterweight")
    call screen j701_investigation_evidence("counterweight")
    call j701_clue_negative_blueprint from _call_j701_core_blueprint
    $ j701_investigation_collect("negative_blueprint")
    call screen j701_investigation_evidence("negative_blueprint")
    "Elias retourne au stockage pour inspecter une nouvelle fois l'étagère."
    elias inquiet "Si vous retrouvez quelqu'un avec les batteries, appelez-moi, hein. Je veux voir ce qu'il a foutu avec."
    nyra "Il se fait tard. On a encore le temps de vérifier deux pistes avant de retrouver les autres. Noam, choisis par où tu veux commencer."
    while len(j701_investigation_found) < J701_INVESTIGATION_MAX_TURNS:
        $ _j701_selected_room = renpy.call_screen("j701_investigation_locations")
        $ j701_investigation_prepare_room(_j701_selected_room)
        $ _j701_selected_clue = renpy.call_screen("j701_investigation_pointclick", _j701_selected_room)
        if _j701_selected_clue is not None:
            call expression "j701_clue_{}".format(_j701_selected_clue) from _call_expression_4
            $ j701_investigation_collect(_j701_selected_clue)
            play sound "audio/sfx_exclamation.mp3"
            call screen j701_investigation_evidence(_j701_selected_clue)
    scene black with fade
    "Les lumières du couloir passent en mode nocturne. On n'a vérifié que quatre éléments."
    call screen j701_investigation_dossier
    jump j701_investigation_debrief

label j701_clue_elias_testimony:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_13
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("elias", "reflechit", 0.72)])
    "Elias me fait une place et sort une feuille pliée de sa poche."
    elias "Regarde. J'avais fait la liste avant de bosser hier soir. Deux batteries, le micro-soudeur, trois stabilisateurs. J'ai même corrigé le nombre parce que j'avais écrit deux au début."
    noam "Tu les as utilisés pour ton projet hier soir ?"
    elias "Ouais, au stockage. J'arrivais pas à faire une calibration propre. Au bout d'un moment j'en ai eu marre, j'ai rangé tout le matos et je suis rentré. Il était 23 h 47, je me rappelle de l'heure sur la porte."
    noam "T'es sûr de l'heure à la minute près ?"
    elias "Ben oui ! J'ai regardé parce que j'avais prévu de me coucher tôt pour une fois. Et les pièces étaient toutes là quand j'ai fermé."
    elias "Noam, je sais que je suis pas le mec le plus soigneux du monde, mais j'ai bossé avec ce genre de matériel bien avant de venir ici. Je laisse pas deux batteries comme ça au milieu d'un couloir."
    noam "Je te crois. Je vais noter 23 h 47."
    "Il se penche sur ma tablette et vérifie l'heure que j'inscris."
    $ hideGroup()
    return

label j701_clue_foil_crane:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_14
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.14), ("elen", "surpris", 0.50), ("julian", "taquin", 0.86)])
    "Une pointe argentée dépasse sous le rebord de la table. Je décolle un petit oiseau en papier de la traînée de graisse qui le retient."
    play sound "audio/sfx_paper.mp3"
    elen "Oh, ma grue ! Fais attention, l'aile est toute abîmée."
    noam "Tu en fais souvent ?"
    elen "Quand j'ai rien à faire avec mes mains. J'utilise les emballages des rations parce que le papier tient bien. Attends, je peux te montrer le pli, normalement..."
    "Elle essaie de redresser l'aile, puis s'arrête en voyant la graisse sur ses doigts."
    julian "J'en ai retrouvé une dans ma chambre. Je serais incapable de te dire comment elle y est arrivée."
    elen "Je t'en avais donné une ! Tu devais la mettre sur ton bureau."
    julian "Ah. Je ne l'ai pas jetée, si ça peut te rassurer."
    noam "Je vais garder celle-ci. Elle est tachée de graisse. Tu te rappelles si quelqu'un t'en a demandé une hier ?"
    elen "Non, désolée. J'en fais un peu partout et je les laisse sur les tables. Je peux pas te dire à qui elle appartenait."
    "Elle me laisse l'oiseau. Je le range sans l'aplatir."
    $ hideGroup()
    return

label j701_clue_counterweight:
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_15
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.15), ("elias", "surpris", 0.50), ("mara", "doute", 0.85)])
    elias "Là ! C'est là que je les range. Tu vois bien qu'y a rien."
    "Le terminal indique MASSE CONFORME."
    noam "Peut-être que le capteur est tombé en panne comme le reste."
    elias "Attends, bouge."
    "Il appuie sur la plaque de l'étagère. L'affichage change."
    elias "Non, regarde. Il marche. Aide-moi à soulever ça."
    "Deux poches d'eau aplaties sont sanglées sous le faux fond."
    play sound "audio/sfx_metal_clank.mp3"
    mara "C'est à toi, ça ?"
    elias "J'ai jamais mis ça là. Putain, c'est lourd..."
    "On pèse une poche. L'affichage correspond à la masse attendue."
    elias "Elles ont remplacé les batteries ! Quelqu'un a dû les peser avant de préparer ces trucs. Le capteur vérifie le poids, il sait pas reconnaître ce qu'on pose dessus."
    noam "Donc c'était pas quelqu'un qui les avait juste empruntées."
    mara "Ça me paraît difficile à croire, ouais. Garde les poches ici pour que Nyra puisse les voir."
    "Elias regarde l'étagère vide sans bouger."
    $ hideGroup()
    return

label j701_clue_blank_receipt:
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_16
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("kael", "reflechit", 0.72)])
    kael "Ce boîtier n'enregistre pas les images. Mais il conserve les transactions. Si on trouve le retrait, on aura peut-être au moins une heure."
    play sound "audio/sfx_beep.mp3"
    "Il ouvre le reçu de 02 h 14 : RETRAIT AUTORISÉ. Quatre références. Masse déclarée : zéro."
    noam "Ça correspond aux contrepoids. Regarde la colonne à côté, il y a pas de nom."
    kael "Attends, je vais exporter la ligne."
    "Il essaie deux fois. À la place de l'identité, le même petit carré blanc apparaît."
    noam "Ça pourrait être le nom de quelqu'un qui n'est pas enregistré comme représentant ?"
    kael "Je n'en sais rien. Normalement, le système devrait refuser un identifiant inconnu. Là, il a accepté le retrait."
    kael "Si la ligne avait simplement été supprimée, on devrait voir une trace différente. Mais je ne connais pas assez bien ce terminal pour exclure une erreur."
    noam "On garde le reçu. Je veux pas qu'on nous dise demain qu'il a jamais existé."
    $ hideGroup()
    return

label j701_clue_brown_hair:
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_17
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("mara", "reflexion", 0.72)])
    "Un cheveu brun est collé dans de la graisse sous le rebord de l'établi."
    noam "Mara, passe-moi la pince. Celle à côté du tournevis."
    "Je dégage le cheveu, long d'environ quatre centimètres."
    play sound "audio/sfx_exclamation.mp3"
    mara "T'en fais pas un peu trop ? On est tous passés dans cette salle."
    noam "Il y a peut-être moyen de savoir à qui il appartient. Elias a les cheveux..."
    mara "Oh, commence pas. Regarde le bout. Il est coupé net et y a pas de racine."
    noam "Quelqu'un a pu le laisser ici exprès."
    mara "Ou quelqu'un s'est coupé les cheveux, ou il traînait sur un vêtement. J'en ai rien à foutre que tu le gardes, mais va pas accuser quelqu'un avec ça."
    "Elle me tend un sachet. J'y glisse le cheveu."
    $ hideGroup()
    return

label j701_clue_negative_blueprint:
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_18
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.12), ("elias", "reflechit", 0.50), ("kael", "neutre", 0.88)])
    elias "Ils ont nettoyé l'établi. Hier, j'avais encore de la limaille dessus."
    kael "Tu as un aimant ?"
    "Elias lui tend celui qui se trouve parmi les outils. Kael le rapproche de la surface."
    "Les restes de limaille se redressent autour d'une zone propre : trois anneaux, un faisceau central et deux attaches asymétriques."
    noam "On dirait le contour d'un truc qu'on a posé ici."
    elias "Attends... Kael, ça ressemble pas à un adaptateur ? Si quelqu'un voulait brancher un appareil qui accepte pas la même alimentation que nos équipements, ça pourrait avoir cette forme."
    kael "Peut-être. Je vais chercher dans les plans."
    "Le terminal ne retrouve aucun fichier correspondant. Le cache affiche seulement : CONVERTISSEUR MULTI-PH..."
    elias "Avec mes batteries, les stabilisateurs et le micro-soudeur, y a de quoi faire un montage qui supporte une grosse charge. Mais j'ai besoin de voir le reste pour te dire à quoi ça sert."
    noam "Ça pourrait servir à réparer les relais de Kami ?"
    kael "Je ne vois pas pourquoi quelqu'un aurait effacé le plan dans ce cas. On n'a pas assez d'informations."
    elias "Prends une photo. Et envoie-la-moi, j'aimerais bien regarder ça de plus près."
    "Kael photographie le contour."
    $ hideGroup()
    return

label j701_clue_kael_database:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_19
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "doute", 0.28), ("kael", "reflechit", 0.72)])
    play sound "audio/sfx_gresillement.mp3"
    "Kael travaille sur la base des caméras. Quand je m'approche, il ferme une fenêtre."
    noam "Pourquoi tu fermes ça ? Je voulais justement te demander si on pouvait voir les images."
    kael "Je tentais d'accéder à l'administration. La base refuse de me donner la liste des enregistrements."
    noam "J'ai vu que tu avais entré un identifiant."
    kael "Un ancien identifiant personnel. À Orbite, j'avais accès à certains outils de maintenance. J'ai voulu vérifier si le système le reconnaissait."
    noam "Tu peux utiliser un accès d'Orbite ici ?"
    kael "Je ne peux rien utiliser pour l'instant. Il reconnaît l'identifiant, ce n'est pas la même chose qu'une autorisation. J'ai six refus et une tentative en cours."
    "Il me montre les résultats sans rouvrir sa requête."
    noam "Kael, j'aurais préféré que tu nous préviennes avant. Si on découvre ça dans un journal d'accès, ça risque de mal passer."
    kael "Je sais. Je voulais obtenir les images avant d'en discuter avec tout le monde. J'ai peut-être eu tort."
    "Il remet sa tablette devant lui. Je ne vois toujours pas la requête."
    $ hideGroup()
    return

label j701_clue_maintenance_log:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_20
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.12), ("lysa", "inquiet", 0.50), ("kael", "reflechit", 0.88)])
    "Kael affiche le journal général des portes."
    play sound "audio/sfx_beep.mp3"
    kael "Le stockage a enregistré une ouverture autorisée à 02 h 14. Je vais faire défiler les lignes suivantes."
    noam "Arrête-toi après 02 h 23."
    lysa "Là, la maintenance. Deux heures trente-quatre."
    "L'identité est vide."
    lysa "Ça laisse vingt minutes pour déplacer les batteries. C'est largement faisable."
    noam "On devrait demander qui était encore réveillé à cette heure-là."
    kael "Oui, mais ne partez pas du principe que c'était la même personne. Si le système enregistre des identités vides, on ne sait pas non plus si les heures sont fiables."
    lysa "Alors on va finir avec douze personnes qui jurent avoir dormi et aucun moyen de vérifier."
    "Je sauvegarde les deux lignes. Kael reste devant le journal."
    $ hideGroup()
    return

label j701_clue_vertical_tracks:
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_21
    scene bg_sas at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.12), ("iris", "surpris", 0.50), ("mara", "doute", 0.88)])
    "Deux marques de roues traversent le sol et se prolongent sur le métal de la porte."
    iris "Mara, aide-moi à monter. Il y a quelque chose au-dessus du cadre."
    mara "Mets ton pied là. Accroche-toi à mon épaule."
    "Iris se hisse avec difficulté."
    iris "Deux marques en demi-lune. L'écartement correspond aux roues. Et il y a de la poussière noire sur le rail."
    noam "On aurait pu utiliser un support magnétique pour plaquer la cargaison contre la porte."
    mara "Je vois pas pourquoi on s'emmerderait à faire ça au lieu de l'ouvrir."
    iris "Pour ne pas passer devant la caméra ? Si le matériel reste dans le rail ou au-dessus, on peut peut-être le déplacer sans que le terminal voie un passage normal."
    "Mara tente de bouger une plaque au-dessus de la porte. Elle résiste."
    iris "Ne force pas. Fais-moi redescendre, j'ai mal au pied."
    $ hideGroup()
    return

label j701_clue_impossible_echo:
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_22
    scene bg_sas at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.12), ("kael", "reflechit", 0.50), ("mara", "doute", 0.88)])
    kael "Le micro du terminal sert à diagnostiquer les verrous. Il reste un enregistrement à 02 h 21. Écoutez."
    play sound "audio/sfx_beep.mp3"
    "Un bip d'autorisation. Sept secondes plus tard, le même bruit."
    mara "Ils ont ouvert deux fois ?"
    kael "La fermeture prend douze secondes. On ne peut pas valider deux passages aussi rapprochés avec cette porte."
    noam "Tu peux remettre le passage ?"
    "Kael relance l'enregistrement, puis superpose les formes d'onde."
    kael "Vous voyez le grésillement à la fin ? Il est exactement identique. Le deuxième signal a été rejoué."
    mara "Mais ça sert à quoi de faire croire à un micro qu'une porte s'ouvre ? C'est débile."
    kael "Je ne sais pas si le micro était la cible. Quelqu'un qui attendait dans le sas aurait pu entendre le bip aussi."
    noam "Ou quelqu'un qui consulte l'enregistrement, comme nous."
    "Je le réécoute une dernière fois. Sans les courbes de Kael, j'aurais cru à deux passages."
    $ hideGroup()
    return

label j701_investigation_debrief:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_23
    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "audio/music/bgm_introspective_atmosphere.mp3" fadein 1.5
    $ showGroup([
        ("iris", "reflexion", 0.10),
        ("julian", "inquiet", 0.27),
        ("lysa", "fatigue", 0.43),
        ("kael", "reflechit", 0.59),
        ("elias", "inquiet", 0.76),
        ("mara", "doute", 0.91),
        ("elen", "inquiet"),
        ("nyra", "reflechit")
    ])
    "Elias a déplié les relevés sur la table où nous jouions aux cartes."
    elias "Je veux qu'on retrouve le truc qu'ils ont fabriqué. J'ai besoin de mes pièces, mais surtout, si quelqu'un a fait un montage avec autant de puissance, j'aimerais savoir où il l'a mis."
    julian "Nous pourrions demander à chacun de nous montrer ce qu'il a dans sa chambre. Si tout le monde coopère, il ne devrait pas y avoir de difficulté."
    iris colere "T'as pas intérêt à mettre un pied dans la mienne."
    julian "Je parlais d'une démarche volontaire."
    lysa "Et ceux qui refusent deviennent suspects, évidemment."
    nyra "Personne ne va ouvrir les chambres cette nuit. On ne sait même pas si l'appareil est encore au même endroit."
    elias "J'ai pas demandé qu'on fouille vos chambres ! Si quelqu'un a des infos, c'est tout ce que je veux."
    kael "On a au moins les contrepoids et le contour à l'atelier. Le montage semble compatible avec les pièces disparues. Ça ne me permet pas de dire qui l'a fait."
    if "blank_receipt" in j701_investigation_found:
        noam "Le reçu du stockage autorise un retrait à 02 h 14, mais il n'y a aucun nom. Ça me dérange plus que l'absence d'images."
        iris "Kael, il faudra me montrer le reçu. Si le système accepte un identifiant qu'il ne sait pas afficher, je veux voir comment il le présente."
    if "maintenance_log" in j701_investigation_found:
        lysa "On a aussi une ouverture à la maintenance vingt minutes plus tard, sans identité. Ça pourrait correspondre au déplacement du matériel."
        mara "Ou pas. On n'a vu personne, alors allez pas raconter demain qu'on a trouvé le trajet du voleur."
    if "kael_database" in j701_investigation_found:
        iris "Et toi, Kael, pourquoi t'as essayé d'ouvrir les caméras avec un ancien identifiant sans nous prévenir ?"
        kael "Parce que je pensais pouvoir récupérer les images. J'ai montré les refus à Noam."
        iris "Envoie-les-moi aussi. Je regarderai."
        "Kael ne répond pas immédiatement."
    if "brown_hair" in j701_investigation_found:
        noam "On a trouvé un cheveu à l'atelier..."
        mara "Et ça ne désigne personne. Il est coupé, on sait même pas depuis combien de temps il est là."
    if "foil_crane" in j701_investigation_found:
        elen "L'oiseau en papier qu'on a trouvé est probablement un des miens. Je peux essayer de me souvenir où j'en ai laissé, mais j'en fais vraiment beaucoup."
        julian "J'en ai vu plusieurs dans la salle de repos. Ce serait difficile de remonter à une personne."
    if "vertical_tracks" in j701_investigation_found:
        iris "Il faut aussi regarder le rail du sas. Il y a des traces de roues jusque sur la porte. Ça ne correspond pas à un passage normal."
        kael "Je regarderai le système de guidage demain."
    if "impossible_echo" in j701_investigation_found:
        kael "Et au sas, quelqu'un a peut-être rejoué un bip d'autorisation. Je ne sais pas pour qui."
        lysa "Donc même si l'un de nous a entendu une porte s'ouvrir cette nuit, ça ne prouve rien."
    "Elias froisse le coin de sa feuille."
    elias "On va faire quoi, là ? On va attendre qu'il manque encore autre chose ?"
    menu:
        "Insister sur le fait que le vol était préparé.":
            $ j701_investigation_theory = "premedite"
            noam "Les poches d'eau avaient le bon poids. Pour les préparer, il fallait savoir quelles batteries prendre et comment l'étagère fonctionne. On devrait regarder qui connaissait le matériel."
            elias "Ouais. Ça, on peut le faire."
            mara "Sans partir du principe que les ingénieurs sont coupables, merci."
        "S'inquiéter de ce que les systèmes n'ont pas détecté.":
            $ j701_investigation_theory = "securite"
            noam "Si on a pu tromper le capteur du stockage, j'aimerais qu'on vérifie les autres systèmes. Je suis pas rassuré à l'idée qu'on se fie tous à ce qu'affichent nos portes."
            nyra "Je peux faire une liste des accès à vérifier. Pour les chambres, il faudra l'accord de chacun."
            lysa "Ça me va, tant qu'on garde nos affaires privées."
        "Refuser de désigner un suspect sans preuve.":
            $ j701_investigation_theory = "prudence"
            noam "On devrait continuer à chercher le matériel plutôt que commencer à désigner quelqu'un. Si on se met à accuser tous ceux qui ont accès à l'atelier, on va se faire la gueule pendant une semaine."
            kael "Merci."
            iris "On a quand même le droit de demander ce que les gens ont fait. Je compte bien le faire."
    elias "Bon. Moi je retourne au stockage demain matin. Si quelqu'un veut venir, je serai là."
    mara "Je viendrai avec toi. Mais là, va te coucher. T'as pas arrêté de chercher depuis ce matin."
    "Il reprend ses feuilles, en oubliant le plan de l'adaptateur au milieu de la table."
    elen "Je pensais à un truc... Si quelqu'un a fait tout ça cette nuit, il est peut-être assis avec nous en ce moment."
    "Julian regarde autour de la table. Kael referme son dossier."
    "Personne ne lui répond."
    $ hideGroup()
    stop music fadeout 1.0
    jump _7_0_1_FIN_JOURNEE
