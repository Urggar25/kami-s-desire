# Jour 7 - Enquête sur le matériel disparu
# Dix pistes sont disponibles, mais une partie n'en laissera examiner que cinq.

default j701_investigation_found = []
default j701_investigation_turn = 0

init python:
    J701_INVESTIGATION_MAX_TURNS = 5

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

        text "5 TOURS  /  10 PISTES  /  UNE SEULE NUIT":
            font "fonts/Rajdhani-SemiBold.ttf"
            size 31
            color "#8EEAFF"
            kerning 3
            xalign 0.5

    text "Choisis où consacrer ton temps. Les pistes abandonnées seront perdues.":
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

    text "5 fragments récupérés  //  5 pistes abandonnées":
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
    play music "audio/music/bgm_low_tension.mp3" fadein 1.0

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
    "Quand je relève enfin la tête, les lumières du couloir ont basculé en mode nocturne."
    think "Cinq pistes. Et cinq autres que je n'aurai pas le temps de suivre."
    call screen j701_investigation_dossier
    jump j701_investigation_debrief


label j701_clue_elias_testimony:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_13
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.28),
        ("elias", "reflechit", 0.72),
    ])
    noam reflechit "Reprends depuis la dernière fois où tu as vu le matériel. Sans raccourci."
    elias reflechit "Hier soir. Je suis resté au stockage après le repas pour recalibrer mon projet."
    noam doute "Tu as utilisé quoi, exactement ?"
    elias neutre "Les deux batteries, le micro-soudeur, puis les stabilisateurs. Je les ai même recomptés. Trois."
    noam reflechit "Et ensuite ?"
    elias reflechit "J'ai tout rangé. La porte affiche l'heure quand elle se ferme : 23 h 47."
    elias fatigue "Je l'ai regardée en me disant que j'allais encore dormir quatre heures. C'est le genre de détail qui reste."
    noam doute "Tu es certain de ne pas y être retourné ?"
    elias colere "Certain ! À 23 h 47, tout était encore là. Ce matin, les emplacements étaient vides."
    "Il ne reconstruit pas un souvenir : il reproduit une routine. Les gestes, l'ordre, jusqu'au voyant de la porte."
    think "S'il ment, il a préparé chaque détail. S'il dit vrai, la nuit vient de rétrécir."
    $ hideGroup()
    return


label j701_clue_foil_crane:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_14
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.14),
        ("elen", "surpris", 0.50),
        ("julian", "taquin", 0.86),
    ])
    "Sous le rebord de la grande table, une pointe argentée dépasse d'une traînée de graisse."
    noam surpris "Attendez... Il y a quelque chose de coincé là-dessous."
    "Je tire doucement. Un minuscule oiseau en papier se déplie dans ma paume, une aile broyée comme si elle avait été prise dans une roue."
    play sound "audio/sfx_paper.mp3"
    elen surpris "C'est... une de mes grues. Enfin, je crois. Je les plie avec les emballages des rations."
    julian taquin "Je préfère le terme d'aviation expérimentale."
    elen colere "Tu les lances sur Iris quand elle ne te répond pas."
    julian hesitation "L'aviation expérimentale connaît parfois des dérives militaires."
    noam doute "Elen, tu en as donné à quelqu'un hier ?"
    elen inquiet "Non... mais j'en laisse partout. Sur les tables, dans les livres. N'importe qui pouvait en prendre une."
    "La graisse sur l'aile est fraîche. L'origami, lui, peut avoir changé dix fois de mains."
    think "Une signature parfaite pour accuser Elen. Donc une signature presque inutile."
    $ hideGroup()
    return


label j701_clue_counterweight:
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_15
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.15),
        ("elias", "surpris", 0.50),
        ("mara", "doute", 0.85),
    ])
    "L'étagère insiste : MASSE CONFORME. Pourtant, les logements des batteries sont vides."
    noam doute "Le capteur affirme qu'elles sont toujours là."
    mara taquin "Peut-être qu'elles ont atteint un nouveau stade de discrétion."
    elias colere "Ou peut-être que le capteur raconte n'importe quoi. Pousse-toi."
    "Je soulève le faux fond avant lui. Deux poches d'eau aplaties sont sanglées sous la plaque."
    play sound "audio/sfx_metal_clank.mp3"
    "Elles pèsent, au gramme près, le poids des batteries disparues. Le capteur n'a donc jamais enregistré de retrait."
    elias surpris "Quelqu'un a pesé mes batteries avant de les prendre ?"
    noam reflechit "Et préparé les contrepoids avant cette nuit."
    mara mefiant "Donc le vol a commencé avant que les objets disparaissent."
    "Ce n'est plus un geste improvisé. C'est un tour de prestidigitation répété à l'avance, jusqu'à devenir invisible pour la salle elle-même."
    think "Le voleur ne s'est pas contenté de connaître le stockage. Il connaissait la façon dont le stockage regarde."
    $ hideGroup()
    return


label j701_clue_blank_receipt:
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_16
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.28),
        ("kael", "reflechit", 0.72),
    ])
    "Le boîtier de la porte ne conserve pas de vidéo, seulement des reçus de transaction."
    play sound "audio/sfx_beep.mp3"
    noam reflechit "Il y a bien une transaction à 02 h 14."
    kael neutre "RETRAIT AUTORISÉ. Quatre références. Masse déclarée : zéro."
    noam doute "Zéro ? Avec deux batteries ?"
    kael reflechit "Le capteur a été trompé par les contrepoids. Pour lui, rien n'a quitté l'étagère."
    "Dans la colonne IDENTITÉ, aucun nom. Seulement un petit carré blanc que le terminal refuse de sélectionner ou de copier."
    noam surpris "La ligne a été effacée ?"
    kael mefiant "Non. Une suppression laisserait un trou. Là, le système croit vraiment que personne a effectué le retrait."
    noam reflechit "Ou qu'il a reçu un nom qu'il n'est pas capable d'afficher."
    "Le reçu prouve l'heure et l'autorisation — puis avale la seule chose qui nous intéresse."
    think "À 02 h 14, la porte s'est ouverte pour un utilisateur que la machine ne sait pas nommer."
    $ hideGroup()
    return


label j701_clue_brown_hair:
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_17
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.28),
        ("mara", "reflexion", 0.72),
    ])
    "Sous la lèvre de l'établi, quelque chose de brun est collé dans une goutte de graisse claire."
    noam reflechit "Ne touche pas. Passe-moi la pince."
    mara taquin "J'allais justement le lécher pour identifier son propriétaire."
    noam blase "La pince, Mara."
    "Je le dégage délicatement : un cheveu brun, assez court, long d'à peine quatre centimètres."
    play sound "audio/sfx_exclamation.mp3"
    mara reflexion "Pas de racine. Et regarde l'autre bout."
    "L'extrémité est droite, nette, presque géométrique. Ce cheveu n'est pas tombé : il a été coupé."
    noam doute "Donc il ne prouve même pas que son propriétaire est venu ici."
    mara mefiant "Il prouve surtout que quelqu'un voulait qu'on le trouve."
    noam inquiet "Brun et court... Ça désigne beaucoup trop de monde."
    mara neutre "Exactement. Suffisamment précis pour lancer une accusation. Suffisamment vague pour en lancer cinq."
    think "Une preuve posée exprès peut mentir. Mais elle révèle tout de même l'existence d'un menteur."
    $ hideGroup()
    return


label j701_clue_negative_blueprint:
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_18
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.12),
        ("elias", "reflechit", 0.50),
        ("kael", "neutre", 0.88),
    ])
    "Le plan de travail paraît impeccable. Trop impeccable."
    elias reflechit "Normalement, cet établi attire la limaille pendant des jours. Là, il n'y en a presque plus."
    kael neutre "Presque."
    "Kael approche un aimant. La limaille oubliée se redresse autour d'une zone parfaitement propre."
    noam surpris "Elle dessine le contour de ce qui était posé là."
    "Peu à peu, le vide forme un objet : trois anneaux, un faisceau central, deux attaches asymétriques."
    elias reflechit "C'est l'ombre d'un adaptateur. Quelqu'un l'a assemblé ici, puis a nettoyé autour."
    kael reflechit "Le terminal devrait avoir conservé le plan de montage."
    "Le terminal ne contient aucun fichier correspondant. Son cache garde seulement un titre tronqué : CONVERTISSEUR MULTI-PH..."
    noam reflechit "Les batteries, le micro-soudeur, les stabilisateurs..."
    elias inquiet "Tout ce qu'il faut pour que ce truc accepte une énorme charge sans griller."
    kael mefiant "Et quelqu'un a effacé le mode d'emploi après l'avoir fabriqué."
    "Nous savons enfin que le matériel n'a pas seulement été caché. Une partie a déjà servi."
    think "On ne cherche plus uniquement un voleur. On cherche ce qu'il a fabriqué."
    $ hideGroup()
    return


label j701_clue_kael_database:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_19
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "doute", 0.28),
        ("kael", "reflechit", 0.72),
    ])
    play sound "audio/sfx_gresillement.mp3"
    "Kael ne m'a pas entendu entrer. Ses doigts enchaînent les commandes sur la base de données des caméras."
    "Quand mon reflet apparaît dans son écran, il masque sa requête d'un geste sec."
    noam doute "Tu cherches les images ou tu cherches à les cacher ?"
    kael surpris "Depuis combien de temps tu es là ?"
    noam reflechit "Assez pour voir BASE CAMÉRAS et ACCÈS ADMINISTRATEUR."
    kael mefiant "J'essaie d'obtenir l'accès administrateur. La base refuse même de me dire quels segments existent."
    noam doute "Alors pourquoi fermer la fenêtre ?"
    kael gene "Parce que j'ai utilisé un ancien identifiant personnel. Je n'avais pas envie d'expliquer pourquoi il est encore valide ici."
    noam inquiet "Il est encore valide ?"
    kael reflechit "Il est reconnu. Ce n'est pas la même chose. Regarde : six refus et une septième tentative marquée EN COURS."
    noam doute "Tu aurais pu nous prévenir."
    kael mefiant "Et transformer chaque ligne de code en débat collectif ? J'ai choisi de gagner du temps."
    "Sa justification tient. Son réflexe, beaucoup moins."
    think "Kael peut être en train de nous aider. Il peut aussi choisir exactement ce que nous allons voir."
    $ hideGroup()
    return


label j701_clue_maintenance_log:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_20
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.12),
        ("lysa", "inquiet", 0.50),
        ("kael", "reflechit", 0.88),
    ])
    "Une fois l'accès obtenu, Kael ouvre le journal général des portes plutôt que les vidéos."
    play sound "audio/sfx_beep.mp3"
    kael reflechit "Stockage : ouverture autorisée à 02 h 14. Ça correspond au reçu."
    noam reflechit "Continue après 02 h 23."
    lysa surpris "Attendez. Là. Maintenance."
    "Une ligne blanche apparaît au milieu du journal : PORTE MAINTENANCE — OUVERTE — 02 H 34."
    noam surpris "La porte de la salle de maintenance s'est ouverte à 2 h 34 du matin."
    lysa inquiet "Vingt minutes après le retrait du matériel."
    noam doute "Qui est entré ?"
    kael mefiant "La colonne d'identité est vide. Comme sur le reçu du stockage."
    lysa reflexion "Le voleur prend le matériel à 02 h 14, puis ouvre la maintenance à 02 h 34..."
    noam reflechit "Assez de temps pour déplacer une cargaison sans courir."
    kael doute "Ou assez de temps pour vouloir nous faire croire à ce trajet. Ce journal a déjà accepté une identité impossible."
    "La ligne de 02 h 34 relie enfin deux salles. Elle ne nous dit toujours pas qui a franchi la porte."
    think "Le matériel disparu est très probablement passé par la maintenance. À 2 h 34, quelqu'un y est entré sans laisser de nom."
    $ hideGroup()
    return


label j701_clue_vertical_tracks:
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_21
    scene bg_sas at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.12),
        ("iris", "surpris", 0.50),
        ("mara", "doute", 0.88),
    ])
    "Deux marques de roues traversent le sol jusqu'à la grande porte. Au lieu de s'arrêter, elles remontent sur le métal."
    iris surpris "D'accord. Le chariot a décidé de marcher sur les murs."
    mara taquin "Ne le juge pas. Il explore sa verticalité."
    noam blase "Vous pourriez m'aider à regarder au-dessus ?"
    "Mara joint les mains. Iris prend appui dessus et se hisse jusqu'au cadre supérieur."
    iris reflexion "Deux impacts en demi-lune. Même écartement que les roues."
    noam reflechit "Un plateau magnétique. La cargaison a été plaquée verticalement contre la porte."
    mara doute "Pour la faire passer quand elle s'ouvre ?"
    iris inquiet "Ou pour la glisser dans le rail. Il est couvert de poussière noire fraîche."
    "Quelque chose de lourd a bien circulé au-dessus de la porte, hors du champ de la caméra."
    think "Le voleur n'a pas traversé le sas. Il a utilisé la porte elle-même comme ascenseur."
    $ hideGroup()
    return


label j701_clue_impossible_echo:
    call MAYBE_PLAY_SCRIPTED_DOOR("sas", "bg_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_22
    scene bg_sas at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "reflexion", 0.12),
        ("kael", "reflechit", 0.50),
        ("mara", "doute", 0.88),
    ])
    "Le terminal possède un micro de diagnostic. Il enregistre les sons des verrous pour repérer les pannes mécaniques."
    noam reflechit "Il reste une séquence audio à 02 h 21."
    play sound "audio/sfx_beep.mp3"
    "Un bip d'autorisation retentit. Sept secondes plus tard, exactement le même son revient, jusque dans son grésillement final."
    mara doute "Deux ouvertures ?"
    kael reflechit "Impossible. Cette porte met douze secondes à se refermer. Elle ne peut pas valider deux passages espacés de sept secondes."
    noam doute "Un écho ?"
    mara taquin "Un écho très ponctuel qui prend sept secondes pour traverser dix mètres ?"
    kael raison "Le second son a été rejoué. Compare les formes d'onde : elles sont identiques au pixel près."
    noam inquiet "Quelqu'un a diffusé un faux bip dans la salle."
    kael mefiant "Oui. Mais pour tromper une personne, un autre capteur... ou notre enquête ?"
    "Le micro ne répond pas. Il conserve seulement deux sons identiques dans un ordre impossible."
    think "Quelqu'un a fabriqué du bruit comme il a fabriqué de fausses données : juste assez vrai pour que la machine l'accepte."
    $ hideGroup()
    return


label j701_investigation_debrief:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_23
    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "audio/music/bgm_unsaid_distance.mp3" fadein 1.5

    "La nuit est tombée pendant que nous courions d'une salle à l'autre. Les fragments de preuve occupent maintenant toute la table."

    $ showGroup([
        ("iris", "reflexion", 0.10),
        ("julian", "inquiet", 0.27),
        ("lysa", "fatigue", 0.43),
        ("kael", "reflechit", 0.59),
        ("elias", "colere", 0.76),
        ("mara", "doute", 0.91),
    ])

    elias colere "Alors ? On a un nom ?"
    noam fatigue "On a cinq morceaux. Pas une histoire complète."

    if "counterweight" in j701_investigation_found:
        lysa reflexion "Les contrepoids prouvent que ce vol était préparé avant cette nuit. Mais pas par qui."
    elif "negative_blueprint" in j701_investigation_found:
        lysa reflexion "On sait qu'un adaptateur a été fabriqué. On ignore toujours à quoi il sert et qui l'a emporté."
    else:
        lysa reflexion "Chaque piste ouvre deux explications nouvelles. On ne réduit pas la liste, on l'agrandit."

    if "maintenance_log" in j701_investigation_found:
        julian inquiet "Donc la maintenance s'ouvre à 2 h 34, sans nom, et personne ne trouve ça terrifiant ?"
        noam reflechit "Ça relie le stockage à la maintenance. Pas le trajet à une personne."

    if "kael_database" in j701_investigation_found:
        iris reflexion "Et Kael qui fouille les caméras en douce, on en parle ?"
        kael mefiant "J'ai tenté l'accès que j'ai moi-même proposé devant vous. Si je voulais le cacher, je n'aurais pas laissé l'historique."
        noam reflechit "C'est suspect. Ce n'est pas une preuve de vol."

    if "brown_hair" in j701_investigation_found:
        mara reflexion "Le cheveu brun a été coupé. Il désigne trop de monde et ne place personne dans la salle."
        elias fatigue "Donc il a surtout été déposé pour qu'on s'accuse entre nous."

    if "foil_crane" in j701_investigation_found:
        elen inquiet "Je vous jure que ma grue ne veut rien dire. N'importe qui pouvait la prendre."
        iris reflexion "Justement. C'est une fausse piste parfaite. Trop personnelle pour être ignorée, trop commune pour prouver quoi que ce soit."

    if "blank_receipt" in j701_investigation_found or "impossible_echo" in j701_investigation_found:
        kael reflechit "Les systèmes ont accepté des données impossibles. Quelqu'un sait leur faire prendre une copie pour un original."

    elias inquiet "Donc quelqu'un prend mon matériel, falsifie les systèmes, se balade la nuit... et on va juste dormir ?"
    mara fatigue "On va surtout éviter de désigner un coupable au hasard parce qu'on est crevés."
    kael reflechit "On verrouille ce qui reste. Demain, on reprend avec les journaux d'accès complets."
    lysa inquiet "À condition que Kami ne revienne pas avant."

    "Le nom de Kami suffit à éteindre les dernières protestations."
    "Personne n'est convaincu. Personne n'est accusé. Un à un, nous finissons pourtant par quitter la table."
    think "On a trouvé des indices. Pas le coupable."
    think "Et quelque part dans le Conclave, le matériel sert peut-être déjà à quelque chose."

    $ hideGroup()
    stop music fadeout 1.0
    jump _7_0_1_FIN_JOURNEE
