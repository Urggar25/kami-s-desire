# ============================================================
# MINI-JEU REUTILISABLE - OBJECTION FRACTUREE
# Jour 4 : debat sur la libre circulation entre districts.
# ============================================================

default j4_objection_score = 0
default j4_objection_tension = 0
default j4_objection_lucidity = 100
default j4_objection_phase = "clash"
default j4_objection_time_left = 0.0
default j4_objection_active_words = []
default j4_objection_captured = []
default j4_objection_feedback = ""
default j4_objection_done = False
default j4_objection_result = "medium"
default j4_objection_word_uid = 0
default j4_objection_flash = 0.0
default j4_objection_pulse = 0.0
default j4_objection_shake = 0
default j4_objection_phrase_index = 0
default j4_objection_phrase_state = "entry"
default j4_objection_phrase_timer = 0.0
default j4_objection_qte_uid = None
default j4_objection_qte_timer = 0.0
default j4_objection_synthesis_step = 0
default j4_objection_synthesis_answers = []
default j4_objection_reward = 0
default j4_objection_errors = 0
default j4_argument_circulation_cadre = False

init python:
    import random
    import math

    J4_OBJECTION_TICK = 0.05
    J4_OBJECTION_CENTER_X = 960
    J4_OBJECTION_CENTER_Y = 520
    J4_OBJECTION_NOAM_LEFT_X = 250
    J4_OBJECTION_NOAM_RIGHT_X = 1670
    J4_OBJECTION_READ_TIME = 3.0
    J4_OBJECTION_QTE_TIME = 0.9

    J4_OBJECTION_CLASH_LINES = [
        {
            "speaker": "ryn",
            "name": "RYN",
            "side": "left",
            "color": "#ff8a35",
            "portrait": "images/character/ryn/colere2.png",
            "bubble": "gui/day4/objection/comic_bubble_ryn.png",
            "line": "J'en peux plus, Noam. On nous demande de sourire dans une cage.",
            "rich_line": "J'en peux plus, Noam. On nous demande de sourire dans une {color=#68d9ff}cage{/color}.",
            "words": [
                ("SOURIRE", "neutral"), ("CAGE", "important"), ("RESPIRER", "important"),
                ("LAISSE", "important"), ("TRAHISON", "danger"), ("ASSEZ", "neutral"),
            ],
        },
        {
            "speaker": "sael",
            "name": "SAEL",
            "side": "right",
            "color": "#87cfff",
            "portrait": "images/character/sael/determine.png",
            "bubble": "gui/day4/objection/comic_bubble_sael.png",
            "line": "Tu appelles ca une porte. Moi je vois surtout l'endroit ou ca casse.",
            "rich_line": "Tu appelles ca une {color=#68d9ff}porte{/color}. Moi je vois surtout l'endroit ou {color=#ff6f7d}ca casse{/color}.",
            "words": [
                ("PORTE", "neutral"), ("CADRE", "important"), ("BRECHE", "danger"),
                ("GARDIENS", "important"), ("PEUR", "important"), ("LACHE", "danger"),
            ],
        },
        {
            "speaker": "ryn",
            "name": "RYN",
            "side": "left",
            "color": "#ff8a35",
            "portrait": "images/character/ryn/desaccord.png",
            "bubble": "gui/day4/objection/comic_bubble_ryn.png",
            "line": "Arrete avec tes grands mots. Proteger, ici, ca veut dire tenir les gens en laisse.",
            "rich_line": "Arrete avec tes grands mots. {color=#68d9ff}Proteger{/color}, ici, ca veut dire tenir les gens en {color=#68d9ff}laisse{/color}.",
            "words": [
                ("PROTEGER", "neutral"), ("LAISSE", "important"), ("RESPIRER", "important"),
                ("FERME-LA", "danger"), ("CAGE", "important"), ("VOUS", "neutral"),
            ],
        },
        {
            "speaker": "sael",
            "name": "SAEL",
            "side": "right",
            "color": "#87cfff",
            "portrait": "images/character/sael/peur.png",
            "bubble": "gui/day4/objection/comic_bubble_sael.png",
            "line": "Et les morts, Ryn ? Tu leur expliques comment que cette fois ca ira ?",
            "rich_line": "Et les {color=#68d9ff}morts{/color}, Ryn ? Tu leur expliques comment que cette fois {color=#ff6f7d}ca ira{/color} ?",
            "words": [
                ("MORTS", "neutral"), ("MEMOIRE", "important"), ("DIGUE", "important"),
                ("MEURTRE", "danger"), ("PEUR", "important"), ("RESPIRER", "important"),
            ],
        },
        {
            "speaker": "nyra",
            "name": "NYRA",
            "side": "right",
            "color": "#d6e8ff",
            "portrait": "images/character/nyra/stress.png",
            "bubble": "gui/day4/objection/comic_bubble_sael.png",
            "line": "Vous etes en train de vous repondre a cote. La, quelqu'un va casser.",
            "rich_line": "Vous etes en train de vous repondre a cote. La, quelqu'un va {color=#ff6f7d}casser{/color}.",
            "words": [
                ("CHOIX", "neutral"), ("CADRE", "important"), ("CASSER", "danger"),
                ("CALME", "neutral"), ("PEUR", "important"), ("DANGER", "neutral"),
            ],
        },
    ]

    J4_OBJECTION_SYNTHESIS = [
        {
            "question": "Si je dois resumer, pour Sael c'est...",
            "rich_question": "Si je dois resumer, pour {color=#87cfff}Sael{/color}, c'est...",
            "answers": ["la peur", "la liberte", "le confort", "la vengeance"],
            "correct": ["la peur"],
        },
        {
            "question": "Du coup pour Ryn, c'est...",
            "rich_question": "Du coup pour {color=#ff8a35}Ryn{/color}, c'est...",
            "answers": ["respirer", "obeir", "proteger", "punir"],
            "correct": ["respirer"],
        },
        {
            "question": "Il faut qu'on essaye de...",
            "rich_question": "Il faut qu'on essaye de...",
            "answers": ["poser un cadre", "ouvrir sans reflechir", "fermer les yeux", "choisir un camp"],
            "correct": ["poser un cadre"],
        },
    ]

    J4_OBJECTION_SFX_FALLBACKS = {
        "sound/objection_word_spawn.ogg": "audio/sfx_beep.mp3",
        "sound/objection_word_capture.ogg": "audio/sfx_victory.mp3",
        "sound/objection_word_miss.ogg": "audio/sfx_balle.mp3",
        "sound/objection_parasite_click.ogg": "audio/sfx_gresillement.mp3",
        "sound/objection_tension_hit.ogg": "audio/sfx_tambour.mp3",
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

    def j4_objection_asset(path, fallback):
        if renpy.loadable(path):
            return path
        return fallback

    def j4_objection_current_line():
        index = min(store.j4_objection_phrase_index, len(J4_OBJECTION_CLASH_LINES) - 1)
        return J4_OBJECTION_CLASH_LINES[index]

    def j4_objection_core_x():
        if store.j4_objection_phase == "synthesis":
            return J4_OBJECTION_CENTER_X
        line = j4_objection_current_line()
        if line.get("side") == "left":
            return J4_OBJECTION_NOAM_RIGHT_X
        return J4_OBJECTION_NOAM_LEFT_X

    def j4_objection_core_y():
        return J4_OBJECTION_CENTER_Y

    def j4_objection_reset():
        store.j4_objection_score = 0
        store.j4_objection_tension = 0
        store.j4_objection_lucidity = 100
        store.j4_objection_phase = "clash"
        store.j4_objection_time_left = 0.0
        store.j4_objection_active_words = []
        store.j4_objection_captured = []
        store.j4_objection_feedback = "Lis la phrase. Elle va se briser."
        store.j4_objection_done = False
        store.j4_objection_result = "medium"
        store.j4_objection_word_uid = 0
        store.j4_objection_flash = 0.0
        store.j4_objection_pulse = 0.0
        store.j4_objection_shake = 0
        store.j4_objection_phrase_index = 0
        store.j4_objection_phrase_state = "entry"
        store.j4_objection_phrase_timer = 0.65
        store.j4_objection_qte_uid = None
        store.j4_objection_qte_timer = 0.0
        store.j4_objection_synthesis_step = 0
        store.j4_objection_synthesis_answers = []
        store.j4_objection_reward = 0
        store.j4_objection_errors = 0
        renpy.block_rollback()
        j4_objection_safe_play("sound/objection_word_spawn.ogg")

    def j4_objection_unique_append(fragment):
        if fragment and fragment not in store.j4_objection_captured:
            store.j4_objection_captured.append(fragment)

    def j4_objection_spawn_phrase_words():
        line = j4_objection_current_line()
        side = line.get("side", "left")
        start_x = -260 if side == "left" else 2180
        target_x = j4_objection_core_x()
        target_y_base = j4_objection_core_y()
        words = list(line.get("words", []))
        random.shuffle(words)
        store.j4_objection_active_words = []

        for index, pair in enumerate(words):
            text, word_type = pair
            y = 245 + (index % 6) * 86 + random.randint(-22, 22)
            target_y = target_y_base + random.randint(-110, 110)
            dx = target_x - start_x
            dy = target_y - y
            distance = max(1.0, math.sqrt(dx * dx + dy * dy))
            speed = random.randint(250, 335)
            if word_type == "danger":
                speed += 45
            word = {
                "uid": store.j4_objection_word_uid,
                "text": text,
                "type": word_type,
                "x": float(start_x),
                "y": float(y),
                "vx": dx / distance * speed,
                "vy": dy / distance * speed,
                "age": 0.0,
                "rotation": random.randint(-8, 8),
                "qte": False,
            }
            store.j4_objection_word_uid += 1
            store.j4_objection_active_words.append(word)

        store.j4_objection_feedback = "Capture les bleus. Les rouges se gerent avec ESPACE."
        store.j4_objection_pulse = 0.35
        j4_objection_safe_play("sound/objection_tension_hit.ogg")

    def j4_objection_click_word(uid):
        if store.j4_objection_phase != "clash" or store.j4_objection_done:
            return
        found = None
        for word in store.j4_objection_active_words:
            if word.get("uid") == uid:
                found = word
                break
        if not found:
            return

        if found.get("type") != "important":
            return

        store.j4_objection_active_words.remove(found)
        fragment = found.get("text", "")
        j4_objection_unique_append(fragment)
        store.j4_objection_score += 12
        store.j4_objection_tension = max(0, store.j4_objection_tension - 3)
        store.j4_objection_feedback = "Noam garde : " + fragment
        store.j4_objection_pulse = 0.35
        j4_objection_safe_play("sound/objection_word_capture.ogg")

    def j4_objection_damage(text, amount=14):
        store.j4_objection_errors += 1
        store.j4_objection_lucidity = max(0, store.j4_objection_lucidity - amount)
        store.j4_objection_tension = min(100, store.j4_objection_tension + amount)
        store.j4_objection_feedback = text
        store.j4_objection_flash = 0.28
        store.j4_objection_shake = 7
        j4_objection_safe_play("sound/objection_word_miss.ogg")

    def j4_objection_space():
        if store.j4_objection_phase != "clash" or store.j4_objection_qte_uid is None:
            return

        found = None
        for word in store.j4_objection_active_words:
            if word.get("uid") == store.j4_objection_qte_uid:
                found = word
                break

        if found:
            store.j4_objection_active_words.remove(found)
            store.j4_objection_score += 5
            store.j4_objection_feedback = found.get("text", "ROUGE") + " se brise."
            store.j4_objection_pulse = 0.35
            j4_objection_safe_play("sound/objection_stabilize.ogg")

        store.j4_objection_qte_uid = None
        store.j4_objection_qte_timer = 0.0

    def j4_objection_start_synthesis():
        store.j4_objection_phase = "synthesis"
        store.j4_objection_active_words = []
        store.j4_objection_qte_uid = None
        store.j4_objection_qte_timer = 0.0
        store.j4_objection_synthesis_step = 0
        store.j4_objection_feedback = "Le clash retombe. Noam doit formuler."
        store.j4_objection_pulse = 0.45

    def j4_objection_answer_synthesis(answer):
        if store.j4_objection_phase != "synthesis" or store.j4_objection_done:
            return

        step = store.j4_objection_synthesis_step
        if step >= len(J4_OBJECTION_SYNTHESIS):
            return

        question = J4_OBJECTION_SYNTHESIS[step]
        correct = answer in question.get("correct", [])
        store.j4_objection_synthesis_answers.append({"answer": answer, "correct": correct})

        if correct:
            store.j4_objection_score += 18
            store.j4_objection_tension = max(0, store.j4_objection_tension - 5)
            store.j4_objection_feedback = "Ca tient."
            j4_objection_safe_play("sound/objection_word_capture.ogg")
        else:
            j4_objection_damage("La synthese se fissure.", 10)

        store.j4_objection_synthesis_step += 1
        if store.j4_objection_synthesis_step >= len(J4_OBJECTION_SYNTHESIS):
            j4_objection_finalize()

    def j4_objection_calculate_reward():
        if store.j4_objection_errors <= 0 and store.j4_objection_tension <= 0:
            return 200
        tension = max(0, min(100, int(store.j4_objection_tension)))
        return max(0, int(round(200.0 * (100 - tension) / 100.0)))

    def j4_objection_finalize():
        correct_answers = 0
        for item in store.j4_objection_synthesis_answers:
            if item.get("correct", False):
                correct_answers += 1

        if correct_answers >= 3 and store.j4_objection_tension <= 35 and store.j4_objection_lucidity >= 70:
            store.j4_objection_result = "good"
        elif correct_answers <= 1 or store.j4_objection_tension >= 80 or store.j4_objection_lucidity <= 35:
            store.j4_objection_result = "bad"
        else:
            store.j4_objection_result = "medium"

        store.j4_objection_reward = j4_objection_calculate_reward()
        if not hasattr(store, "player_kamyz"):
            store.player_kamyz = 0
        store.player_kamyz += store.j4_objection_reward
        store.j4_objection_done = True
        renpy.block_rollback()

        if store.j4_objection_result == "good":
            j4_objection_safe_play("sound/objection_final_good.ogg")
        elif store.j4_objection_result == "bad":
            j4_objection_safe_play("sound/objection_final_bad.ogg")

    def j4_objection_update_qte():
        if store.j4_objection_qte_uid is None:
            return
        store.j4_objection_qte_timer = max(0.0, store.j4_objection_qte_timer - J4_OBJECTION_TICK)
        if store.j4_objection_qte_timer > 0.0:
            return

        found = None
        for word in store.j4_objection_active_words:
            if word.get("uid") == store.j4_objection_qte_uid:
                found = word
                break

        if found:
            store.j4_objection_active_words.remove(found)
            j4_objection_damage(found.get("text", "ROUGE") + " happe Noam.", 14)

        store.j4_objection_qte_uid = None
        store.j4_objection_qte_timer = 0.0

    def j4_objection_tick():
        if store.j4_objection_done:
            return
        if store.j4_objection_flash > 0.0:
            store.j4_objection_flash = max(0.0, store.j4_objection_flash - J4_OBJECTION_TICK)
        if store.j4_objection_pulse > 0.0:
            store.j4_objection_pulse = max(0.0, store.j4_objection_pulse - J4_OBJECTION_TICK)
        if store.j4_objection_shake > 0:
            store.j4_objection_shake = max(0, store.j4_objection_shake - 1)

        if store.j4_objection_phase != "clash":
            return

        store.j4_objection_phrase_timer = max(0.0, store.j4_objection_phrase_timer - J4_OBJECTION_TICK)
        j4_objection_update_qte()

        if store.j4_objection_phrase_state == "entry":
            if store.j4_objection_phrase_timer <= 0.0:
                store.j4_objection_phrase_state = "read"
                store.j4_objection_phrase_timer = J4_OBJECTION_READ_TIME
                store.j4_objection_feedback = "Lis. Puis trie ce qui reste."
            return

        if store.j4_objection_phrase_state == "read":
            if store.j4_objection_phrase_timer <= 0.0:
                store.j4_objection_phrase_state = "words"
                j4_objection_spawn_phrase_words()
            return

        survivors = []
        for word in store.j4_objection_active_words:
            word["x"] += word["vx"] * J4_OBJECTION_TICK
            word["y"] += word["vy"] * J4_OBJECTION_TICK
            word["age"] += J4_OBJECTION_TICK
            core_x = j4_objection_core_x()
            core_y = j4_objection_core_y()
            dist = math.sqrt((word["x"] - core_x) ** 2 + (word["y"] - core_y) ** 2)

            if word.get("type") == "danger" and store.j4_objection_qte_uid is None and dist < 230:
                store.j4_objection_qte_uid = word.get("uid")
                store.j4_objection_qte_timer = J4_OBJECTION_QTE_TIME
                word["qte"] = True
                store.j4_objection_feedback = "ESPACE !"
                j4_objection_safe_play("sound/objection_parasite_click.ogg")

            crossed = dist < 70 or word["age"] > 8.0
            if crossed:
                if word.get("type") == "important":
                    j4_objection_damage(word.get("text", "MOT") + " percute Noam.", 8)
                elif word.get("type") == "danger":
                    if store.j4_objection_qte_uid == word.get("uid"):
                        store.j4_objection_qte_uid = None
                        store.j4_objection_qte_timer = 0.0
                    j4_objection_damage(word.get("text", "ROUGE") + " traverse Noam.", 14)
                else:
                    store.j4_objection_score += 1
                continue
            survivors.append(word)

        store.j4_objection_active_words = survivors

        if len(store.j4_objection_active_words) <= 0:
            store.j4_objection_phrase_index += 1
            if store.j4_objection_phrase_index >= len(J4_OBJECTION_CLASH_LINES):
                j4_objection_start_synthesis()
            else:
                store.j4_objection_phrase_state = "entry"
                store.j4_objection_phrase_timer = 0.5
                store.j4_objection_feedback = "Une autre voix coupe."

        if store.j4_objection_tension >= 100:
            store.j4_objection_tension = 100
            j4_objection_start_synthesis()

transform j4_objection_word_motion(rot=0):
    rotate rot
    alpha 0.98
    ease 0.18 zoom 1.05
    ease 0.18 zoom 1.0
    repeat

transform j4_objection_parasite_motion(rot=0):
    rotate rot
    alpha 0.95
    ease 0.04 xoffset -7
    ease 0.04 xoffset 9
    ease 0.04 xoffset 0
    repeat

transform j4_objection_core_pulse:
    alpha 0.92
    ease 0.55 zoom 1.08
    ease 0.55 zoom 1.0
    repeat

transform j4_objection_error_shake:
    ease 0.035 xoffset -14
    ease 0.035 xoffset 16
    ease 0.035 xoffset -8
    ease 0.035 xoffset 0
    repeat

transform j4_objection_fracture_flicker:
    alpha 0.18
    ease 0.08 alpha 0.55
    ease 0.08 alpha 0.18
    repeat

transform j4_objection_left_entry:
    xoffset -170
    alpha 0.0
    ease 0.25 xoffset 0 alpha 1.0

transform j4_objection_right_entry:
    xoffset 170
    alpha 0.0
    ease 0.25 xoffset 0 alpha 1.0

screen day4_objection_fracturee():
    modal True
    zorder 230

    on "show" action Function(j4_objection_reset)
    key "K_SPACE" action Function(j4_objection_space)
    timer J4_OBJECTION_TICK repeat True action Function(j4_objection_tick)

    $ screen_offset = 0
    if j4_objection_shake > 0:
        $ screen_offset = -10 + (j4_objection_shake % 3) * 10

    fixed:
        xoffset screen_offset

        add j4_objection_asset("gui/day4/objection/objection_bg.png", "images/background/bg_conclave.png") at cover_screen
        add Solid("#020711dd")

        add j4_objection_asset("gui/day4/objection/ryn_side.png", Solid("#5a120c88")):
            xsize 560
            ysize 1080
            xpos 0
        add j4_objection_asset("gui/day4/objection/sael_side.png", Solid("#06142b99")):
            xsize 560
            ysize 1080
            xpos 1360
        add Solid("#00000077")

        if j4_objection_phase == "clash":
            use day4_objection_clash
        else:
            use day4_objection_synthesis

        $ core_x = int(j4_objection_core_x())
        $ core_y = int(j4_objection_core_y())
        add j4_objection_asset("gui/day4/objection/noam_core.png", Solid("#a8f4ff")):
            xpos core_x - 96
            ypos core_y - 96
            xsize 192
            ysize 192
            at j4_objection_core_pulse

        if j4_objection_tension >= 35:
            add j4_objection_asset("gui/day4/objection/fracture_overlay.png", Solid("#ff2b2b24")) at j4_objection_fracture_flicker

        if j4_objection_flash > 0.0:
            add Solid("#ff1a2f55")
        if j4_objection_pulse > 0.0:
            add Solid("#9ef8ff24")

        frame:
            xpos 300
            ypos 922
            xsize 1320
            ysize 126
            background Solid("#020910ee")
            padding (22, 16)
            vbox:
                spacing 10
                hbox:
                    spacing 18
                    text "TENSION" size 23 color "#ffd1d1"
                    bar value StaticValue(j4_objection_tension, 100):
                        xsize 500
                        ysize 22
                    text "LUCIDITE" size 23 color "#c9f7ff"
                    bar value StaticValue(j4_objection_lucidity, 100):
                        xsize 500
                        ysize 22
                text "[j4_objection_feedback]" size 25 color "#f2fbff" xalign 0.5 text_align 0.5

    if j4_objection_done:
        timer 1.2 action Return(j4_objection_result)

screen day4_objection_clash():
    $ line = j4_objection_current_line()
    $ entry_from_left = line.get("side") == "left"
    $ speaker_x = 40 if entry_from_left else 1340
    $ bubble_x = 390 if entry_from_left else 410
    $ speaker_name = line.get("name", "")
    $ phrase_text = line.get("rich_line", line.get("line", ""))
    $ portrait_path = line.get("portrait", "images/character/noam/portrait.png")
    $ bubble_path = line.get("bubble", "gui/day4/objection/comic_bubble_noam.png")

    frame:
        xalign 0.5
        ypos 24
        xsize 850
        ysize 82
        background Solid("#06121cee")
        padding (20, 12)
        hbox:
            spacing 30
            text "DISCUSSION FRACTUREE" size 31 color "#ffffff"
            text "clash [j4_objection_phrase_index + 1]/[len(J4_OBJECTION_CLASH_LINES)]" size 26 color "#9ef8ff"
            text "sens [len(j4_objection_captured)]" size 26 color "#ffd071"

    if j4_objection_phrase_state in ("entry", "read"):
        if entry_from_left:
            add portrait_path:
                xpos speaker_x
                ypos 72
                xsize 620
                ysize 930
                at j4_objection_left_entry

            add bubble_path:
                xpos bubble_x
                ypos 165
                at j4_objection_left_entry

            vbox:
                xpos bubble_x + 72
                ypos 190
                xsize 980
                spacing 12
                at j4_objection_left_entry
                text speaker_name.lower() size 28 color line.get("color", "#ffffff")
                text phrase_text size 43 color "#ffffff" xalign 0.5 text_align 0.5 outlines [(2, "#000000", 0, 0)]
                if j4_objection_phrase_state == "read":
                    text "La phrase tient encore..." size 24 color "#b7f7ff" xalign 0.5
        else:
            add portrait_path:
                xpos speaker_x
                ypos 72
                xsize 620
                ysize 930
                at j4_objection_right_entry

            add bubble_path:
                xpos bubble_x
                ypos 165
                at j4_objection_right_entry

            vbox:
                xpos bubble_x + 70
                ypos 190
                xsize 980
                spacing 12
                at j4_objection_right_entry
                text speaker_name.lower() size 28 color line.get("color", "#ffffff")
                text phrase_text size 43 color "#ffffff" xalign 0.5 text_align 0.5 outlines [(2, "#000000", 0, 0)]
                if j4_objection_phrase_state == "read":
                    text "La phrase tient encore..." size 24 color "#b7f7ff" xalign 0.5

    for word in j4_objection_active_words:
        $ wx = int(word.get("x", 0))
        $ wy = int(word.get("y", 0))
        $ word_text = word.get("text", "")
        $ rot = word.get("rotation", 0)
        $ word_type = word.get("type", "neutral")
        $ is_qte = j4_objection_qte_uid == word.get("uid")
        $ shard_bg = "#eceff4dd"
        $ shard_hover = "#ffffffee"
        $ shard_color = "#0b1118"
        $ shard_size = 30
        if word_type == "important":
            $ shard_bg = "#0d5877ee"
            $ shard_hover = "#1483aeee"
            $ shard_color = "#ffffff"
            $ shard_size = 38
        elif word_type == "danger":
            $ shard_bg = "#5b0711ee"
            $ shard_hover = "#7b0d1aee"
            $ shard_color = "#ffd1d1"
            $ shard_size = 34

        if word_type == "important":
            button:
                xpos wx
                ypos wy
                xsize 235
                ysize 72
                background Solid(shard_bg)
                hover_background Solid(shard_hover)
                action Function(j4_objection_click_word, word.get("uid"))
                at j4_objection_word_motion(rot)
                text word_text size shard_size color shard_color xalign 0.5 yalign 0.5 outlines [(2, "#000000", 0, 0)]
        elif word_type == "danger":
            frame:
                xpos wx
                ypos wy
                xsize 220
                ysize 66
                background Solid(shard_bg)
                padding (8, 6)
                at j4_objection_parasite_motion(rot)
                text word_text size shard_size color shard_color xalign 0.5 yalign 0.5 outlines [(2, "#000000", 0, 0)]
        else:
            frame:
                xpos wx
                ypos wy
                xsize 220
                ysize 66
                background Solid(shard_bg)
                padding (8, 6)
                at j4_objection_word_motion(rot)
                text word_text size shard_size color shard_color xalign 0.5 yalign 0.5 outlines [(2, "#000000", 0, 0)]

        if is_qte:
            frame:
                xpos 805
                ypos 700
                xsize 350
                ysize 92
                background Solid("#120407f2")
                padding (18, 12)
                vbox:
                    spacing 4
                    text "ESPACE" size 46 color "#ffffff" xalign 0.5 outlines [(3, "#ff2438", 0, 0)]
                    bar value StaticValue(j4_objection_qte_timer, J4_OBJECTION_QTE_TIME):
                        xsize 300
                        ysize 14
                        xalign 0.5

screen day4_objection_synthesis():
    $ step = min(j4_objection_synthesis_step, len(J4_OBJECTION_SYNTHESIS) - 1)
    $ question = J4_OBJECTION_SYNTHESIS[step]
    $ question_text = question.get("rich_question", question.get("question", ""))

    frame:
        xalign 0.5
        ypos 28
        xsize 820
        ysize 76
        background Solid("#07180dee")
        padding (20, 12)
        hbox:
            spacing 24
            text "SYNTHESE DE NOAM" size 31 color "#c8ffd0"
            text "[j4_objection_synthesis_step + 1]/3" size 30 color "#ffffff"

    add "images/character/noam/reflexion.png":
        xalign 0.5
        ypos 84
        xsize 520
        ysize 760

    add "gui/day4/objection/comic_bubble_noam.png":
        xalign 0.5
        ypos 292

    vbox:
        xalign 0.5
        ypos 320
        xsize 850
        spacing 10
        text "noam" size 28 color "#b7f7ff"
        text "\"[question_text]\"" size 40 color "#ffffff" xalign 0.5 text_align 0.5 outlines [(2, "#000000", 0, 0)]
        text "Kamyz : +[j4_objection_reward]" size 22 color "#ffe7ae" xalign 0.5

    fixed:
        xpos 485
        ypos 560
        xsize 950
        ysize 310
        for index, answer in enumerate(question.get("answers", [])):
            $ row = index // 2
            $ col = index % 2
            button:
                xpos col * 485
                ypos row * 118
                xsize 430
                ysize 82
                background Solid("#102942f2")
                hover_background Solid("#245c82f2")
                action Function(j4_objection_answer_synthesis, answer)
                text answer size 32 color "#f6fbff" xalign 0.5 yalign 0.5

screen day4_objection_reward_summary():
    modal True
    zorder 240
    add Solid("#000000aa")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 620
        ysize 260
        background Solid("#061019f5")
        padding (30, 24)
        vbox:
            spacing 18
            text "RECOMPENSE" size 38 color "#ffe7ae" xalign 0.5
            text "+[j4_objection_reward] Kamyz" size 48 color "#ffffff" xalign 0.5
            text "Tension finale : [j4_objection_tension]/100" size 26 color "#c9f7ff" xalign 0.5
            textbutton "Continuer":
                xalign 0.5
                xsize 260
                ysize 58
                background Solid("#1d4d2bee")
                hover_background Solid("#2f7a43ee")
                text_size 27
                text_color "#eaffee"
                action Return(True)
