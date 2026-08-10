# =============================================================================
# MINI-JEU — DUEL VERBAL DU JOUR 4
#
# Chaque mot d'une phrase devient un projectile :
#   gris  : laisser passer ;
#   rouge : esquiver avec ESPACE ;
#   bleu  : cliquer pour le renvoyer vers son auteur.
# =============================================================================

default j4_objection_player_hp = 100
default j4_objection_opponent_hp = 100
default j4_objection_phase_index = 0
default j4_objection_phase_state = "playing"
default j4_objection_active_words = []
default j4_objection_word_uid = 0
default j4_objection_dodge_timer = 0.0
default j4_objection_dodge_cooldown = 0.0
default j4_objection_transition_timer = 0.0
default j4_objection_player_flash = 0.0
default j4_objection_opponent_flash = 0.0
default j4_objection_feedback = ""
default j4_objection_result = "failure"
default j4_objection_blue_hits = 0
default j4_objection_red_dodged = 0
default j4_objection_red_hits = 0
default j4_argument_circulation_cadre = False

init python:
    import math
    import random
    import re

    J4_OBJECTION_TICK = 0.04
    J4_OBJECTION_PLAYER_X = 455.0
    J4_OBJECTION_PLAYER_Y = 540.0
    J4_OBJECTION_OPPONENT_X = 1470.0
    J4_OBJECTION_OPPONENT_Y = 500.0
    J4_OBJECTION_BLUE_DAMAGE = 8
    J4_OBJECTION_RED_DAMAGE = 12

    J4_OBJECTION_PHASES = [
        {
            "speaker": "ryn",
            "name": "RYN",
            "expr": "colere",
            "line": "À Limen, les frontières ne protègent personne : elles enferment les vivants et condamnent ceux qui tentent seulement de partir.",
            "reply": "Une frontière qui tue ne protège plus personne.",
            "blue": ["frontières", "protègent", "enferment", "partir"],
            "red": ["personne", "condamnent", "tentent"],
        },
        {
            "speaker": "sael",
            "name": "SAEL",
            "expr": "determine",
            "line": "Ouvrir sans contrôle, c'est offrir un passage aux massacres que mes camarades ont payé de leur vie pour contenir.",
            "reply": "Protéger n'oblige pas à condamner tous les passages.",
            "blue": ["contrôle", "passage", "camarades", "contenir"],
            "red": ["ouvrir", "massacres", "vie"],
        },
        {
            "speaker": "iris",
            "name": "IRIS",
            "expr": "desaccord",
            "line": "Vous transformez une décision immense en symbole alors que personne n'a prévu le travail, l'accueil ni la sécurité derrière ces frontières.",
            "reply": "Alors défendons un cadre au lieu de défendre l'immobilité.",
            "blue": ["décision", "travail", "l'accueil", "sécurité"],
            "red": ["immense", "personne", "frontières"],
        },
    ]

    J4_OBJECTION_SFX_FALLBACKS = {
        "sound/objection_word_spawn.ogg": "audio/sfx_beep.mp3",
        "sound/objection_word_capture.ogg": "audio/sfx_victory.mp3",
        "sound/objection_word_miss.ogg": "audio/sfx_balle.mp3",
        "sound/objection_stabilize.ogg": "audio/sfx_minigame_start.mp3",
        "sound/objection_final_good.ogg": "audio/sfx_victory.mp3",
        "sound/objection_final_bad.ogg": "audio/sfx_bad_joke.mp3",
    }

    def j4_objection_safe_play(path):
        if renpy.loadable(path):
            renpy.play(path, channel="sound")
            return
        fallback = J4_OBJECTION_SFX_FALLBACKS.get(path, "")
        if fallback and renpy.loadable(fallback):
            renpy.play(fallback, channel="sound")

    def j4_objection_normalize_word(word):
        return (word or "").lower().replace("’", "'")

    def j4_objection_tokenize(line):
        return re.findall(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*", line or "")

    def j4_objection_current_phase():
        index = max(0, min(store.j4_objection_phase_index, len(J4_OBJECTION_PHASES) - 1))
        return J4_OBJECTION_PHASES[index]

    def j4_objection_word_type(token, phase):
        normalized = j4_objection_normalize_word(token)
        blue = [j4_objection_normalize_word(word) for word in phase.get("blue", [])]
        red = [j4_objection_normalize_word(word) for word in phase.get("red", [])]
        if normalized in blue:
            return "blue"
        if normalized in red:
            return "red"
        return "gray"

    def j4_objection_prepare_phase(index):
        store.j4_objection_phase_index = index
        store.j4_objection_phase_state = "playing"
        store.j4_objection_transition_timer = 0.0
        store.j4_objection_active_words = []

        phase = j4_objection_current_phase()
        tokens = j4_objection_tokenize(phase.get("line", ""))
        lane_order = [1, 4, 2, 5, 0, 3]

        for word_index, token in enumerate(tokens):
            lane = lane_order[word_index % len(lane_order)]
            word_type = j4_objection_word_type(token, phase)
            store.j4_objection_active_words.append({
                "uid": store.j4_objection_word_uid,
                "text": token,
                "type": word_type,
                "state": "incoming",
                "x": 1450.0 + random.randint(-20, 24),
                "y": 275.0 + lane * 92.0 + random.randint(-12, 12),
                "speed": 245.0 + random.randint(-12, 30) + (35.0 if word_type == "red" else 0.0),
                "delay": 0.18 * word_index,
                "rotation": random.randint(-5, 5),
            })
            store.j4_objection_word_uid += 1

        store.j4_objection_feedback = "Clique les mots bleus. ESPACE pour esquiver les rouges."
        start_character_dialogue(phase.get("speaker", ""), phase.get("line", ""))
        start_character_dialogue("noam", phase.get("reply", ""))
        j4_objection_safe_play("sound/objection_word_spawn.ogg")

    def j4_objection_reset():
        store.j4_objection_player_hp = 100
        store.j4_objection_opponent_hp = 100
        store.j4_objection_phase_index = 0
        store.j4_objection_phase_state = "playing"
        store.j4_objection_active_words = []
        store.j4_objection_word_uid = 0
        store.j4_objection_dodge_timer = 0.0
        store.j4_objection_dodge_cooldown = 0.0
        store.j4_objection_transition_timer = 0.0
        store.j4_objection_player_flash = 0.0
        store.j4_objection_opponent_flash = 0.0
        store.j4_objection_feedback = ""
        store.j4_objection_result = "failure"
        store.j4_objection_blue_hits = 0
        store.j4_objection_red_dodged = 0
        store.j4_objection_red_hits = 0
        renpy.block_rollback()
        j4_objection_prepare_phase(0)

    def j4_objection_click_word(uid):
        if store.j4_objection_phase_state != "playing":
            return
        for word in store.j4_objection_active_words:
            if word.get("uid") == uid and word.get("type") == "blue" and word.get("state") == "incoming" and word.get("delay", 0.0) <= 0.0:
                word["state"] = "returning"
                word["speed"] = 900.0
                store.j4_objection_feedback = "Renvoi : « %s »" % word.get("text", "")
                j4_objection_safe_play("sound/objection_word_capture.ogg")
                return

    def j4_objection_space():
        if store.j4_objection_phase_state != "playing" or store.j4_objection_dodge_cooldown > 0.0:
            return
        store.j4_objection_dodge_timer = 0.52
        store.j4_objection_dodge_cooldown = 0.68
        store.j4_objection_feedback = "ESQUIVE"
        j4_objection_safe_play("sound/objection_stabilize.ogg")

    def j4_objection_finish():
        if store.j4_objection_phase_state == "done":
            return
        store.j4_objection_phase_state = "done"
        store.j4_objection_active_words = []
        if store.j4_objection_player_hp > store.j4_objection_opponent_hp:
            store.j4_objection_result = "success"
            store.j4_objection_feedback = "Leur certitude cède avant la tienne."
            j4_objection_safe_play("sound/objection_final_good.ogg")
        else:
            store.j4_objection_result = "failure"
            store.j4_objection_feedback = "Leurs certitudes tiennent plus longtemps que toi."
            j4_objection_safe_play("sound/objection_final_bad.ogg")
        renpy.block_rollback()

    def j4_objection_advance_phase():
        next_index = store.j4_objection_phase_index + 1
        if next_index >= len(J4_OBJECTION_PHASES):
            j4_objection_finish()
        else:
            j4_objection_prepare_phase(next_index)

    def j4_objection_tick():
        if store.j4_objection_phase_state == "done":
            return

        store.j4_objection_dodge_timer = max(0.0, store.j4_objection_dodge_timer - J4_OBJECTION_TICK)
        store.j4_objection_dodge_cooldown = max(0.0, store.j4_objection_dodge_cooldown - J4_OBJECTION_TICK)
        store.j4_objection_player_flash = max(0.0, store.j4_objection_player_flash - J4_OBJECTION_TICK)
        store.j4_objection_opponent_flash = max(0.0, store.j4_objection_opponent_flash - J4_OBJECTION_TICK)

        if store.j4_objection_phase_state == "transition":
            store.j4_objection_transition_timer -= J4_OBJECTION_TICK
            if store.j4_objection_transition_timer <= 0.0:
                j4_objection_advance_phase()
            return

        survivors = []
        for word in store.j4_objection_active_words:
            if word.get("delay", 0.0) > 0.0:
                word["delay"] = max(0.0, word["delay"] - J4_OBJECTION_TICK)
                survivors.append(word)
                continue

            if word.get("state") == "returning":
                dx = J4_OBJECTION_OPPONENT_X - word["x"]
                dy = J4_OBJECTION_OPPONENT_Y - word["y"]
                distance = max(1.0, math.sqrt(dx * dx + dy * dy))
                step = word.get("speed", 900.0) * J4_OBJECTION_TICK
                word["x"] += dx / distance * step
                word["y"] += dy / distance * step
                if distance <= 54.0:
                    store.j4_objection_opponent_hp = max(0, store.j4_objection_opponent_hp - J4_OBJECTION_BLUE_DAMAGE)
                    store.j4_objection_opponent_flash = 0.22
                    store.j4_objection_blue_hits += 1
                    continue
                survivors.append(word)
                continue

            word["x"] -= word.get("speed", 255.0) * J4_OBJECTION_TICK
            if word["x"] <= J4_OBJECTION_PLAYER_X:
                if word.get("type") == "red":
                    if store.j4_objection_dodge_timer > 0.0:
                        store.j4_objection_red_dodged += 1
                        store.j4_objection_feedback = "Mot rouge esquivé."
                    else:
                        store.j4_objection_player_hp = max(0, store.j4_objection_player_hp - J4_OBJECTION_RED_DAMAGE)
                        store.j4_objection_player_flash = 0.28
                        store.j4_objection_red_hits += 1
                        store.j4_objection_feedback = "Le mot rouge te percute."
                        j4_objection_safe_play("sound/objection_word_miss.ogg")
                continue
            survivors.append(word)

        store.j4_objection_active_words = survivors

        if store.j4_objection_player_hp <= 0 or store.j4_objection_opponent_hp <= 0:
            j4_objection_finish()
        elif not store.j4_objection_active_words:
            store.j4_objection_phase_state = "transition"
            store.j4_objection_transition_timer = 0.85
            store.j4_objection_feedback = "La phrase retombe."


transform j4_objection_player_idle:
    yoffset 5
    ease 1.4 yoffset -3
    ease 1.4 yoffset 5
    repeat

transform j4_objection_opponent_idle:
    yoffset 2
    ease 1.2 yoffset -5
    ease 1.2 yoffset 2
    repeat

transform j4_objection_word_pulse(rot=0):
    rotate rot
    zoom 0.96
    ease 0.30 zoom 1.04
    ease 0.30 zoom 0.96
    repeat

transform j4_objection_word_return:
    ease 0.12 zoom 1.20
    linear 0.20 rotate 20
    linear 0.20 rotate -20
    repeat

transform j4_objection_damage_shake:
    xoffset 0
    ease 0.035 xoffset -14
    ease 0.035 xoffset 12
    ease 0.035 xoffset -6
    ease 0.035 xoffset 0
    repeat


screen day4_objection_fracturee():
    modal True
    zorder 230

    on "show" action Function(j4_objection_reset)
    key "K_SPACE" action Function(j4_objection_space)
    timer J4_OBJECTION_TICK repeat True action Function(j4_objection_tick)

    $ phase = j4_objection_current_phase()
    $ noam_expr = "peur" if j4_objection_player_flash > 0.0 else ("determine" if j4_objection_dodge_timer > 0.0 else "reflexion")
    $ opponent_expr = "surpris" if j4_objection_opponent_flash > 0.0 else phase.get("expr", "neutre")
    $ noam_offset = -42 if j4_objection_dodge_timer > 0.0 else 0

    add "gui/day4/objection/objection_bg.png" at cover_screen
    add Solid("#020711D8")

    # Lignes techniques du terrain.
    for lane_y in [360, 452, 544, 636, 728, 820]:
        add Solid("#5CD3FF18") xpos 420 ypos lane_y xsize 1080 ysize 2
    add Solid("#5CD3FF16") xpos 420 ypos 180 xsize 2 ysize 680
    add Solid("#FF6B7716") xpos 1500 ypos 180 xsize 2 ysize 680

    # Portraits composés : corps, bras, yeux et bouche proviennent d'images.rpy.
    add Transform(character_image("noam", noam_expr), zoom=0.92):
        xpos -115 + noam_offset
        yalign 1.0
        at j4_objection_player_idle

    add Transform(character_image(phase.get("speaker", "ryn"), opponent_expr), zoom=0.92):
        xpos 1435
        yalign 1.0
        at j4_objection_opponent_idle

    # Bandeau supérieur : vies et progression.
    frame:
        xpos 24 ypos 18 xsize 430 ysize 92
        background Solid("#071522EE")
        padding (24, 12)
        vbox:
            spacing 8
            text "NOAM" size 26 color "#DCEBFF" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            bar value StaticValue(j4_objection_player_hp, 100):
                xsize 360 ysize 16
                left_bar Solid("#55B9FF")
                right_bar Solid("#173246")

    frame:
        xpos 1466 ypos 18 xsize 430 ysize 92
        background Solid("#160D18EE")
        padding (24, 12)
        vbox:
            spacing 8
            text phase.get("name", "ADVERSAIRE") xalign 1.0 size 26 color "#FFE4E8" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            bar value StaticValue(j4_objection_opponent_hp, 100):
                xsize 360 ysize 16
                left_bar Solid("#FF6877")
                right_bar Solid("#40202A")

    frame:
        xalign 0.5 ypos 14 xsize 430 ysize 100
        background Solid("#08131FEE")
        padding (18, 10)
        vbox:
            spacing 4
            text "PHASE [j4_objection_phase_index + 1] / [len(J4_OBJECTION_PHASES)]" xalign 0.5 size 22 color "#DCEBFF" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            hbox:
                xalign 0.5 spacing 26
                for phase_dot in range(len(J4_OBJECTION_PHASES)):
                    text "●" size 25 color ("#5CD3FF" if phase_dot <= j4_objection_phase_index else "#384A5A")

    # Bulles de dialogue proches du modèle fourni.
    frame:
        xpos 205 ypos 205 xsize 300 ysize 190
        background Solid("#071522E8")
        padding (20, 16)
        vbox:
            spacing 8
            text "NOAM" size 18 color "#5CD3FF" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text phase.get("reply", "") size 23 color "#DCEBFF" line_leading 3

    frame:
        xpos 1415 ypos 205 xsize 300 ysize 220
        background Solid("#190E16E8")
        padding (20, 16)
        vbox:
            spacing 8
            text phase.get("name", "") size 18 color "#FF6877" font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text phase.get("line", "") size 21 color "#FFE8EA" line_leading 2

    # Bouclier / zone d'esquive.
    frame:
        xpos 420 ypos 300 xsize 48 ysize 500
        background Solid("#0C2438EE" if j4_objection_dodge_timer <= 0.0 else "#5CD3FFCC")
        padding (4, 4)
        add Solid("#5CD3FF44")
    text "ESPACE":
        xpos 472 ypos 523 size 20 color ("#FFFFFF" if j4_objection_dodge_timer > 0.0 else "#5CD3FF")
        font "fonts/Rajdhani-SemiBold.ttf" kerning 2

    # Tous les mots de la phrase deviennent des projectiles.
    for word in j4_objection_active_words:
        if word.get("delay", 0.0) <= 0.0:
            use day4_objection_word(word)

    if j4_objection_player_flash > 0.0:
        add Solid("#FF334433")
    if j4_objection_opponent_flash > 0.0:
        add Solid("#5CD3FF1F")

    # Légende basse.
    frame:
        xpos 330 ypos 930 xsize 1260 ysize 112
        background Solid("#07111CEB")
        padding (28, 16)
        hbox:
            spacing 85
            use day4_objection_legend("#D9E1E8", "MOTS GRIS", "Ne rien faire")
            use day4_objection_legend("#FF6877", "MOTS ROUGES", "Esquiver avec ESPACE")
            use day4_objection_legend("#55A9FF", "MOTS BLEUS", "Cliquer pour renvoyer")

    text j4_objection_feedback:
        xalign 0.5 ypos 870 size 22 color "#BBD6E8" font "fonts/Rajdhani-SemiBold.ttf" kerning 1

    if j4_objection_phase_state == "transition":
        frame:
            xalign 0.5 yalign 0.5 xsize 420 ysize 90
            background Solid("#071522F2")
            text "ARGUMENT SUIVANT" xalign 0.5 yalign 0.5 size 30 color "#DCEBFF" font "fonts/Rajdhani-SemiBold.ttf" kerning 3

    if j4_objection_phase_state == "done":
        use day4_objection_result_panel


screen day4_objection_word(word):
    $ word_type = word.get("type", "gray")
    $ returning = word.get("state") == "returning"
    $ orb_color = "#D9E1E8"
    $ inner_color = "#F4F7FA"
    $ text_color = "#101820"
    if word_type == "blue":
        $ orb_color = "#55A9FF"
        $ inner_color = "#276AB5"
        $ text_color = "#FFFFFF"
    elif word_type == "red":
        $ orb_color = "#FF6877"
        $ inner_color = "#B93649"
        $ text_color = "#FFFFFF"
    $ orb_size = 122 if len(word.get("text", "")) > 9 else 106
    $ font_size = 16 if len(word.get("text", "")) > 10 else 19
    $ word_x = int(word.get("x", 0.0))
    $ word_y = int(word.get("y", 0.0))

    if word_type == "blue" and not returning:
        button:
            xpos word_x ypos word_y
            xanchor 0.5 yanchor 0.5
            xysize (orb_size, orb_size)
            background None
            hover_background None
            action Function(j4_objection_click_word, word.get("uid"))
            at j4_objection_word_pulse(word.get("rotation", 0))
            fixed:
                text "●" xalign 0.5 yalign 0.5 size orb_size color orb_color outlines [(7, "#55A9FF55", 0, 0)]
                text "●" xalign 0.5 yalign 0.5 size orb_size - 15 color inner_color
                text word.get("text", "") xalign 0.5 yalign 0.5 size font_size color text_color font "fonts/Rajdhani-SemiBold.ttf"
    else:
        fixed:
            xpos word_x ypos word_y
            xanchor 0.5 yanchor 0.5
            xysize (orb_size, orb_size)
            at (j4_objection_word_return if returning else j4_objection_word_pulse(word.get("rotation", 0)))
            text "●" xalign 0.5 yalign 0.5 size orb_size color orb_color outlines [(7, orb_color + "44", 0, 0)]
            text "●" xalign 0.5 yalign 0.5 size orb_size - 15 color inner_color
            text word.get("text", "") xalign 0.5 yalign 0.5 size font_size color text_color font "fonts/Rajdhani-SemiBold.ttf"


screen day4_objection_legend(color, title, subtitle):
    fixed:
        xysize (330, 72)
        text "●" xpos 0 yalign 0.5 size 58 color color outlines [(5, color + "44", 0, 0)]
        vbox:
            xpos 70 yalign 0.5 spacing 2
            text title size 20 color color font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            text subtitle size 17 color "#A8BAC8"


screen day4_objection_result_panel():
    add Solid("#02060BE6")
    frame:
        xalign 0.5 yalign 0.5 xsize 720 ysize 430
        background Solid("#081522F8")
        padding (42, 32)
        vbox:
            xfill True spacing 18
            text ("CONVICTION RÉUSSIE" if j4_objection_result == "success" else "CONVICTION ÉCHOUÉE"):
                xalign 0.5 size 38 color ("#5CD3FF" if j4_objection_result == "success" else "#FF6877")
                font "fonts/Rajdhani-SemiBold.ttf" kerning 3
            text "NOAM  [j4_objection_player_hp]  —  [j4_objection_opponent_hp]  OPPOSITION":
                xalign 0.5 size 27 color "#DCEBFF" font "fonts/Rajdhani-SemiBold.ttf"
            text j4_objection_feedback:
                xalign 0.5 text_align 0.5 size 22 color "#AFC6D8"
            hbox:
                xalign 0.5 spacing 50
                text "Bleus renvoyés : [j4_objection_blue_hits]" size 18 color "#55A9FF"
                text "Rouges esquivés : [j4_objection_red_dodged]" size 18 color "#FF9AA4"
            textbutton "CONTINUER":
                xalign 0.5 xsize 280 ysize 62
                background Solid("#12344D")
                hover_background Solid("#1D587D")
                text_size 25 text_color "#EAF7FF"
                action Return(j4_objection_result)


# Conservé pour les anciennes sauvegardes qui pourraient encore cibler cet écran.
screen day4_objection_reward_summary():
    modal True
    timer 0.01 action Return(True)
