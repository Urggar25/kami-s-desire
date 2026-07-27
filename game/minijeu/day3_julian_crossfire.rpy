# Mini-jeu jour 3 : Contradiction face à Julian
#
# Huit déclarations défilent. Trois fragments jaunes peuvent être contestés
# avec l'une des trois répliques disponibles. Une seule combinaison est juste.

default day3_julian_clash_success = False
default day3_julian_clash_selected = 0
default day3_julian_clash_attempts = []
default day3_julian_clash_rewarded = False

define DAY3_JULIAN_CLASH_LINE_TIME = 5.2
define DAY3_JULIAN_CLASH_HIGHLIGHT_TIME = 7.0
define DAY3_JULIAN_CLASH_REWARD = 20

init python:
    DAY3_JULIAN_CLASH_BULLETS = [
        {
            "id": "tomas",
            "title": "LA LIMITE DE TOMAS",
            "text": "Tomas vient de te demander d'arrêter.",
        },
        {
            "id": "mandat",
            "title": "AUCUN MANDAT",
            "text": "Personne ne t'a choisi pour les représenter.",
        },
        {
            "id": "fond",
            "title": "LE FOND DU TEXTE",
            "text": "Parler plus fort ne rend pas le texte meilleur.",
        },
    ]

    DAY3_JULIAN_CLASH_STATEMENTS = [
        {
            "id": "j1",
            "expr": "sourire",
            "lines": ["Je veux seulement que ce texte passe.", "On devrait tous viser la même chose."],
        },
        {
            "id": "j2",
            "expr": "taquin",
            "lead": "Je ne force personne.",
            "claim": "Je leur donne seulement un cap.",
            "tail": "Ils restent libres de me suivre.",
            "claim_id": "cap",
        },
        {
            "id": "j3",
            "expr": "idee",
            "lines": ["Quelqu'un doit transformer cette hésitation", "en mouvement. J'assume de le faire."],
        },
        {
            "id": "j4",
            "expr": "sourire",
            "lead": "Tomas hésite, c'est tout.",
            "claim": "Au fond, il attend que je le guide.",
            "tail": "Je lui évite de rester seul avec son choix.",
            "claim_id": "guide",
        },
        {
            "id": "j5",
            "expr": "reflexion",
            "lines": ["Si je parle en premier au Conclave,", "les autres sauront enfin où regarder."],
        },
        {
            "id": "j6",
            "expr": "determine",
            "lead": "Ce n'est pas une question d'ego.",
            "claim": "Les indécis m'ont choisi pour les représenter.",
            "tail": "Je ne fais que prendre mes responsabilités.",
            "claim_id": "representer",
        },
        {
            "id": "j7",
            "expr": "taquin",
            "lines": ["Vous pouvez trouver ma méthode agaçante.", "Elle reste plus utile que votre silence."],
        },
        {
            "id": "j8",
            "expr": "sourire",
            "lines": ["Quand le vote passera, personne ne reprochera", "à Julian d'avoir pris les devants."],
        },
    ]

    def day3_julian_clash_is_correct(claim_id, bullet_index):
        bullet = DAY3_JULIAN_CLASH_BULLETS[int(bullet_index)]
        return claim_id == "representer" and bullet["id"] == "mandat"


transform day3_julian_clash_character_in:
    xalign 0.19
    yalign 1.0
    alpha 0.0
    xoffset -70
    easeout 0.35 alpha 1.0 xoffset 0

transform day3_julian_clash_panel_in:
    alpha 0.0
    xoffset 55
    easeout 0.28 alpha 1.0 xoffset 0

transform day3_julian_clash_scan:
    ypos -32
    linear 5.0 ypos 1080
    repeat

transform day3_julian_clash_time_drain(total=5.2):
    xzoom 1.0
    xanchor 0.0
    linear total xzoom 0.0

transform day3_julian_clash_claim_pulse:
    alpha 0.88
    ease 0.35 alpha 1.0
    ease 0.35 alpha 0.88
    repeat

transform day3_julian_clash_feedback_pop:
    alpha 0.0
    zoom 0.78
    rotate -2
    easeout 0.22 alpha 1.0 zoom 1.06 rotate 1
    easein 0.12 zoom 1.0 rotate 0


style day3_julian_clash_statement is default:
    font "fonts/day_font.ttf"
    size 48
    color "#F4F8FF"
    outlines [(4, "#020711E8", 0, 2)]

style day3_julian_clash_claim_button is button:
    background Solid("#FFD16616")
    hover_background Solid("#FFD16635")
    selected_background Solid("#FFD16635")
    padding (16, 7)

style day3_julian_clash_claim_button_text is button_text:
    font "fonts/day_font.ttf"
    size 51
    color "#FFD166"
    hover_color "#FFF1AD"
    insensitive_color "#FFD166"
    outlines [(4, "#1B1000F0", 0, 2)]

style day3_julian_clash_bullet_button is button:
    xsize 510
    ysize 124
    background Solid("#081426E8")
    hover_background Solid("#102B45F2")
    selected_background Solid("#17445CF2")
    insensitive_background Solid("#081426AA")
    padding (18, 13)

style day3_julian_clash_bullet_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#B9CADB"
    hover_color "#FFFFFF"
    selected_color "#7DF9FF"
    insensitive_color "#718092"


screen day3_julian_clash_tutorial():
    modal True
    zorder 140

    add "bg_repos" at adaptive_fullscreen
    add Solid("#030812E8")
    add Solid("#7DF9FF0C", xsize=1920, ysize=28) at day3_julian_clash_scan

    frame:
        align (0.5, 0.48)
        xsize 1360
        ysize 720
        background Fixed(
            Solid("#07111FF2"),
            Solid("#7DF9FF", xsize=5),
            Solid("#FFFFFF18", ysize=2),
        )
        padding (58, 44)

        vbox:
            spacing 24

            text "CONTRE-INTERROGATOIRE":
                font "fonts/Rajdhani-SemiBold.ttf"
                size 58
                color "#FFFFFF"
                kerning 3

            text "ÉCOUTE • ARME • CONTREDIS":
                font "fonts/Barlow-Light.ttf"
                size 22
                color "#7DF9FF"
                kerning 7

            null height 8

            hbox:
                spacing 34

                vbox:
                    xsize 380
                    spacing 10
                    text "01  ÉCOUTE" size 28 color "#FFD166" bold True
                    text "Huit déclarations vont défiler. Trois fragments seront surlignés en jaune." size 24 color "#D7E5F2" line_spacing 5

                vbox:
                    xsize 380
                    spacing 10
                    text "02  ARME" size 28 color "#FFD166" bold True
                    text "Choisis une réplique avec la souris ou les touches 1, 2 et 3." size 24 color "#D7E5F2" line_spacing 5

                vbox:
                    xsize 380
                    spacing 10
                    text "03  CONTREDIS" size 28 color "#FFD166" bold True
                    text "Clique le fragment jaune, ou appuie sur Espace. Une seule association est décisive." size 24 color "#D7E5F2" line_spacing 5

            null height 22

            frame:
                xfill True
                ysize 115
                background Solid("#FFD16612")
                padding (24, 18)

                text "Une erreur ne bloque pas la scène : Julian poursuit simplement son argumentaire.":
                    align (0.5, 0.5)
                    size 25
                    color "#FFF1C2"

            textbutton "COMMENCER":
                xalign 0.5
                xsize 360
                ysize 74
                background Solid("#16637A")
                hover_background Solid("#2187A2")
                text_font "fonts/Rajdhani-SemiBold.ttf"
                text_size 29
                text_color "#FFFFFF"
                action Return(True)

    key "K_RETURN" action Return(True)
    key "K_SPACE" action Return(True)


screen day3_julian_clash_line(statement, line_index, total_lines, duration):
    modal True
    zorder 140

    add "bg_repos" at adaptive_fullscreen
    add Solid("#020611B8")
    add Solid("#11294ACC")
    add "gui/day3/vote_phase2/bg_overlay.png"
    add Solid("#7DF9FF0D", xsize=1920, ysize=28) at day3_julian_clash_scan

    add "julian [statement['expr']]" at day3_julian_clash_character_in

    frame:
        xpos 620
        ypos 88
        xsize 1225
        ysize 610
        background Fixed(
            Solid("#07101EDC"),
            Solid("#7DF9FF", xsize=5),
            Solid("#FFFFFF16", ysize=2),
        )
        padding (54, 38)
        at day3_julian_clash_panel_in

        fixed:
            text "ARGUMENT // JULIAN":
                xpos 0
                ypos 0
                font "fonts/Barlow-Light.ttf"
                size 19
                color "#7DF9FF"
                kerning 5

            text "DÉCLARATION [line_index + 1] / [total_lines]":
                xalign 1.0
                ypos 0
                font "fonts/Rajdhani-SemiBold.ttf"
                size 22
                color "#9EB3C8"

            vbox:
                xpos 0
                ypos 105
                xsize 1105
                spacing 16

                if statement.get("claim"):
                    text "[statement['lead']]" style "day3_julian_clash_statement"

                    textbutton "[statement['claim']]":
                        style "day3_julian_clash_claim_button"
                        at day3_julian_clash_claim_pulse
                        sensitive not day3_julian_clash_success
                        action Return({
                            "type": "shot",
                            "statement_id": statement["id"],
                            "claim_id": statement["claim_id"],
                            "bullet_index": day3_julian_clash_selected,
                        })

                    text "[statement['tail']]" style "day3_julian_clash_statement"
                else:
                    for statement_line in statement["lines"]:
                        text "[statement_line]" style "day3_julian_clash_statement"

            fixed:
                xpos 0
                ypos 510
                xsize 1105
                ysize 10
                add Solid("#09121F", xsize=1105, ysize=10)
                add Solid("#FFD166", xsize=1105, ysize=10) at day3_julian_clash_time_drain(duration)

    hbox:
        xpos 222
        ypos 875
        spacing 20

        for bullet_index, bullet in enumerate(DAY3_JULIAN_CLASH_BULLETS):
            textbutton "[bullet_index + 1]  [bullet['title']]\n[bullet['text']]":
                style "day3_julian_clash_bullet_button"
                selected day3_julian_clash_selected == bullet_index
                sensitive not day3_julian_clash_success
                action SetVariable("day3_julian_clash_selected", bullet_index)

    if day3_julian_clash_success:
        frame:
            xpos 222
            ypos 814
            background Solid("#153D32E8")
            padding (18, 8)
            text "CONTRADICTION TROUVÉE — écoute de la fin de l'argumentaire":
                size 20
                color "#74FFB2"
                bold True
    else:
        text "SÉLECTION : [DAY3_JULIAN_CLASH_BULLETS[day3_julian_clash_selected]['text']]":
            xpos 222
            ypos 829
            size 20
            color "#7DF9FF"

    key "K_1" action SetVariable("day3_julian_clash_selected", 0)
    key "K_2" action SetVariable("day3_julian_clash_selected", 1)
    key "K_3" action SetVariable("day3_julian_clash_selected", 2)

    if statement.get("claim") and not day3_julian_clash_success:
        key "K_SPACE" action Return({
            "type": "shot",
            "statement_id": statement["id"],
            "claim_id": statement["claim_id"],
            "bullet_index": day3_julian_clash_selected,
        })

    timer duration action Return({"type": "timeout", "statement_id": statement["id"]})


screen day3_julian_clash_feedback(success, bullet_text):
    modal True
    zorder 220

    if success:
        add Solid("#03150DC9")
        add Solid("#74FFB22A")
    else:
        add Solid("#19050AC9")
        add Solid("#FF4D6D20")

    vbox at day3_julian_clash_feedback_pop:
        align (0.5, 0.45)
        spacing 18

        if success:
            text "CONTRADICTION":
                xalign 0.5
                font "fonts/Rajdhani-SemiBold.ttf"
                size 88
                color "#74FFB2"
                outlines [(5, "#03150D", 0, 3)]
            text "« [bullet_text] »":
                xalign 0.5
                size 32
                color "#FFFFFF"
        else:
            text "RÉPLIQUE ÉCARTÉE":
                xalign 0.5
                font "fonts/Rajdhani-SemiBold.ttf"
                size 70
                color "#FF6B7F"
                outlines [(5, "#19050A", 0, 3)]
            text "Julian enchaîne sans te laisser reprendre l'avantage.":
                xalign 0.5
                size 27
                color "#E5C7CD"

    on "show" action Play("sound", "audio/sfx_qte_hit.wav" if success else "audio/sfx_qte_miss.wav")
    timer 1.35 action Return(True)


screen day3_julian_clash_reward():
    modal True
    zorder 220

    add Solid("#020711E8")
    add Solid("#7DF9FF13", xsize=1920, ysize=28) at day3_julian_clash_scan

    frame at day3_julian_clash_feedback_pop:
        align (0.5, 0.47)
        xsize 820
        ysize 400
        background Fixed(
            Solid("#081827F5"),
            Solid("#74FFB2", xsize=6),
            Solid("#FFFFFF18", ysize=2),
        )
        padding (50, 40)

        vbox:
            align (0.5, 0.5)
            spacing 18

            text "FAILLE DÉCISIVE TROUVÉE":
                xalign 0.5
                font "fonts/Rajdhani-SemiBold.ttf"
                size 43
                color "#74FFB2"

            text "Tu as isolé le faux mandat derrière le discours de Julian.":
                xalign 0.5
                text_align 0.5
                size 25
                color "#DCEAF4"

            text "+[DAY3_JULIAN_CLASH_REWARD] KAMYZ":
                xalign 0.5
                font "fonts/day_font.ttf"
                size 49
                color "#FFD166"

            textbutton "REPRENDRE LA SCÈNE":
                xalign 0.5
                xsize 360
                ysize 64
                background Solid("#16637A")
                hover_background Solid("#2187A2")
                text_size 24
                text_color "#FFFFFF"
                action Return(True)

    key "K_RETURN" action Return(True)
    key "K_SPACE" action Return(True)


label day3_julian_clash_minigame:
    $ day3_julian_clash_success = False
    $ day3_julian_clash_selected = 0
    $ day3_julian_clash_attempts = []
    $ day3_julian_clash_index = 0

    window hide
    call screen day3_julian_clash_tutorial

label day3_julian_clash_loop:
    if day3_julian_clash_index >= len(DAY3_JULIAN_CLASH_STATEMENTS):
        jump day3_julian_clash_finish

    $ day3_julian_clash_statement = DAY3_JULIAN_CLASH_STATEMENTS[day3_julian_clash_index]
    $ day3_julian_clash_duration = DAY3_JULIAN_CLASH_HIGHLIGHT_TIME if day3_julian_clash_statement.get("claim") else DAY3_JULIAN_CLASH_LINE_TIME
    $ day3_julian_clash_outcome = renpy.call_screen(
        "day3_julian_clash_line",
        statement=day3_julian_clash_statement,
        line_index=day3_julian_clash_index,
        total_lines=len(DAY3_JULIAN_CLASH_STATEMENTS),
        duration=day3_julian_clash_duration,
    )

    if day3_julian_clash_outcome.get("type") == "shot":
        $ day3_julian_clash_bullet_index = day3_julian_clash_outcome["bullet_index"]
        $ day3_julian_clash_correct = day3_julian_clash_is_correct(
            day3_julian_clash_outcome["claim_id"],
            day3_julian_clash_bullet_index,
        )
        $ day3_julian_clash_attempts.append({
            "statement_id": day3_julian_clash_outcome["statement_id"],
            "claim_id": day3_julian_clash_outcome["claim_id"],
            "bullet_id": DAY3_JULIAN_CLASH_BULLETS[day3_julian_clash_bullet_index]["id"],
            "success": day3_julian_clash_correct,
        })

        if day3_julian_clash_correct:
            $ day3_julian_clash_success = True

        call screen day3_julian_clash_feedback(
            success=day3_julian_clash_correct,
            bullet_text=DAY3_JULIAN_CLASH_BULLETS[day3_julian_clash_bullet_index]["text"],
        )

    $ day3_julian_clash_index += 1
    jump day3_julian_clash_loop

label day3_julian_clash_finish:
    if day3_julian_clash_success and not day3_julian_clash_rewarded:
        $ player_kamyz += DAY3_JULIAN_CLASH_REWARD
        $ day3_julian_clash_rewarded = True
        call screen day3_julian_clash_reward

    window auto
    return
