# Les Sept Questions de Kami — menu de l'évènement et HUD du questionnaire.

init python:
    def sq_status_color(status=None):
        status = status or sq_status()
        return {
            "upcoming": "#7c96a4",
            "ongoing": "#51c6ff",
            "completed": "#63d59a",
            "outdated": "#b860ff",
        }.get(status, "#ffffff")

    def sq_default_stage():
        unlocked = sq_unlocked_count()
        completed = set(sq_completed_stages())
        for stage_index in range(unlocked):
            if stage_index not in completed:
                return stage_index
        return max(0, unlocked - 1)


style sq_stage_row is button:
    xsize 520
    ysize 86
    background Solid("#061522e8")
    hover_background Solid("#0a2c40f2")
    selected_background Solid("#29120beF")
    padding (16, 9, 16, 9)

style sq_answer_button is button:
    xsize 1280
    ysize 94
    background Solid("#090b0feF")
    hover_background Solid("#0b3045f5")
    insensitive_background Solid("#090b0feF")
    padding (0, 0, 24, 0)

style sq_answer_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 36
    color "#f2f4f7"
    insensitive_color "#f2f4f7"
    yalign 0.5

style sq_quiz_action is button:
    xsize 360
    ysize 64
    background Solid("#0a3348e8")
    hover_background Solid("#0d5672f5")
    padding (16, 8, 16, 8)

style sq_quiz_action_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 27
    color "#dff6ff"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


screen kami_event_menu():
    tag menu
    zorder 200
    modal True

    default countdown_tick = 0
    $ status = sq_status()
    $ completed_count = len(sq_completed_stages())

    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=0.8)
    on "hide" action Stop("music", fadeout=0.5)
    key "K_ESCAPE" action ShowMenu("main_menu")
    timer 1.0 repeat True action SetScreenVariable("countdown_tick", countdown_tick + 1)

    add "events/seven_questions/textures/bg_quiz.png" at kami_hub_background
    add Solid("#02060bc8")
    add "gui/main_menu_kami/scanlines.png" alpha 0.20
    add "gui/main_menu_kami/vignette.png" alpha 0.76

    textbutton sq_text("back"):
        style "kami_hub_return"
        xpos 28 ypos 28
        action ShowMenu("main_menu")

    text sq_text("menu_title") style "kami_hub_title" xalign 0.5 ypos 34

    frame:
        xpos 1492 ypos 28 xsize 400 ysize 76
        background Solid("#12051de8")
        padding (22, 8, 22, 8)
        hbox:
            spacing 14 yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(42, 42), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text sq_text("shards") style "kami_hub_meta" color "#eedfff" size 19 yalign 0.5
            text "[persistent.desire_shards]" font "fonts/Rajdhani-SemiBold.ttf" size 36 color "#ffffff" yalign 0.5

    frame:
        xpos 160 ypos 190 xsize 1600 ysize 720
        background Solid("#07101aef")
        padding (28, 28, 28, 28)

        vbox:
            spacing 22
            text sq_text("event_list") style "kami_hub_meta" size 30 xalign 0.5
            add Solid("#1c79a8") xsize 1544 ysize 2

            button:
                xsize 1544 ysize 180
                background Solid("#140914ef")
                hover_background Solid("#241129f5")
                padding (4, 4, 4, 4)
                action ShowMenu("chapter_2_reward_boost_event_menu")
                at kami_card_hover

                fixed:
                    add Transform("events/seven_questions/textures/bg_quiz.png", fit="cover", xsize=1536, ysize=172, matrixcolor=TintMatrix("#7b42a8"))
                    add Solid("#08020dcc")
                    add Solid("#b860ff") xpos 0 ypos 0 xsize 8 ysize 172

                    vbox:
                        xpos 48 ypos 24 xsize 980 spacing 7
                        text chapter_2_reward_boost_text("title") style "kami_hub_section" size 36 color "#e1b4ff"
                        text chapter_2_reward_boost_text("description") style "kami_hub_body" size 21 xmaximum 940
                        text chapter_2_reward_boost_timer_label() style "kami_hub_meta" size 20 color ("#d68cff" if kami_chapter_2_reward_is_boosted() else "#7c96a4")

                    frame:
                        xpos 1080 ypos 22 xsize 280 ysize 58
                        background Solid("#16051feb")
                        text chapter_2_reward_boost_status_label() font "fonts/Rajdhani-SemiBold.ttf" size 22 color ("#d68cff" if kami_chapter_2_reward_is_boosted() else "#7c96a4") xalign 0.5 yalign 0.5

                    hbox:
                        xpos 1080 ypos 98 spacing 18
                        add Transform("gui/main_menu_kami/glyph_kami.png", size=(45, 45), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
                        text (chapter_2_reward_boost_text("boosted_reward") if kami_chapter_2_reward_is_boosted() else chapter_2_reward_boost_text("standard_reward")) font "fonts/Rajdhani-SemiBold.ttf" size 24 color "#f0d9ff" yalign 0.5

            button:
                xsize 1544 ysize 330
                background Solid("#0a0b10ef")
                hover_background Solid("#111b25f5")
                padding (4, 4, 4, 4)
                action ShowMenu("seven_questions_event_menu")
                at kami_card_hover

                fixed:
                    add Transform("events/seven_questions/textures/bg_quiz.png", fit="cover", xsize=1536, ysize=322)
                    add Solid("#02050a99")
                    add Solid("#b74725") xpos 0 ypos 0 xsize 8 ysize 322

                    vbox:
                        xpos 54 ypos 35 xsize 1040 spacing 9
                        text sq_text("title") style "kami_hub_section" size 42
                        text sq_text("subtitle") style "kami_hub_meta" color "#ff7040"
                        text sq_text("description") style "kami_hub_body" size 21 xmaximum 1000
                        text sq_event_timer_label() style "kami_hub_meta" size 22 color sq_status_color(status)
                        text "[sq_text('progress')]  [completed_count] / 7" style "kami_hub_meta" size 21

                    frame:
                        xpos 1180 ypos 30 xsize 300 ysize 64
                        background Solid("#10141deb")
                        text sq_status_label() font "fonts/Rajdhani-SemiBold.ttf" size 24 color sq_status_color(status) xalign 0.5 yalign 0.5

                    frame:
                        xpos 1160 ypos 112 xsize 330 ysize 100
                        background Solid("#17051feb")
                        vbox:
                            xalign 0.5 yalign 0.5 spacing 4
                            add Transform("gui/main_menu_kami/glyph_kami.png", size=(40, 40), matrixcolor=TintMatrix("#b860ff")) xalign 0.5
                            text (sq_text("outdated_reward") if status == "outdated" else sq_text("normal_reward")) font "fonts/Rajdhani-SemiBold.ttf" size 20 color "#e7c8ff" xalign 0.5 text_align 0.5

                    textbutton sq_text("details"):
                        style "kami_hub_action"
                        xpos 1130 ypos 232 xsize 390 ysize 66
                        action ShowMenu("seven_questions_event_menu")


screen chapter_2_reward_boost_event_menu():
    tag menu
    zorder 200
    modal True

    default countdown_tick = 0
    $ boost_active = kami_chapter_2_reward_is_boosted()

    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=0.8)
    on "hide" action Stop("music", fadeout=0.5)
    key "K_ESCAPE" action ShowMenu("kami_event_menu")
    timer 1.0 repeat True action SetScreenVariable("countdown_tick", countdown_tick + 1)

    add "events/seven_questions/textures/bg_quiz.png" at kami_hub_background
    add Solid("#06020bc8")
    add "gui/main_menu_kami/scanlines.png" alpha 0.20
    add "gui/main_menu_kami/vignette.png" alpha 0.76

    textbutton sq_text("back"):
        style "kami_hub_return"
        xpos 28 ypos 28
        action ShowMenu("kami_event_menu")

    text sq_text("menu_title") style "kami_hub_title" xalign 0.5 ypos 34

    frame:
        xpos 1492 ypos 28 xsize 400 ysize 76
        background Solid("#12051de8")
        padding (22, 8, 22, 8)
        hbox:
            spacing 14 yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(42, 42), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text sq_text("shards") style "kami_hub_meta" color "#eedfff" size 19 yalign 0.5
            text "[persistent.desire_shards]" font "fonts/Rajdhani-SemiBold.ttf" size 36 color "#ffffff" yalign 0.5

    frame:
        xalign 0.5 ypos 190 xsize 1500 ysize 700
        background Solid("#09050eef")
        padding (60, 46, 60, 46)

        vbox:
            spacing 18
            text chapter_2_reward_boost_text("title") style "kami_hub_section" size 48 color "#e1b4ff" xalign 0.5
            text chapter_2_reward_boost_text("subtitle") style "kami_hub_meta" color "#b860ff" size 25 xalign 0.5
            add Solid("#b860ff88") xsize 1380 ysize 2
            text chapter_2_reward_boost_text("description") style "kami_hub_body" size 28 xalign 0.5 text_align 0.5 xmaximum 1200

            frame:
                xalign 0.5 xsize 900 ysize 190
                background Solid("#17051feb")
                padding (30, 20, 30, 20)
                hbox:
                    xalign 0.5 yalign 0.5 spacing 34
                    add Transform("gui/main_menu_kami/glyph_kami.png", size=(110, 110), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
                    vbox:
                        yalign 0.5 spacing 8
                        text chapter_2_reward_boost_text("reward_label") style "kami_hub_meta" color "#d68cff" size 23
                        text (chapter_2_reward_boost_text("boosted_reward") if boost_active else chapter_2_reward_boost_text("standard_reward")) font "fonts/Rajdhani-SemiBold.ttf" size 46 color "#ffffff"
                        text chapter_2_reward_boost_status_label() style "kami_hub_meta" size 24 color ("#d68cff" if boost_active else "#7c96a4")

            text chapter_2_reward_boost_timer_label() style "kami_hub_meta" size 27 color ("#d68cff" if boost_active else "#7c96a4") xalign 0.5
            text chapter_2_reward_boost_text("deadline") style "kami_hub_meta" color "#f0d9ff" size 22 xalign 0.5
            text chapter_2_reward_boost_text("after_deadline") style "kami_hub_body" size 22 color "#9ab4c4" xalign 0.5 text_align 0.5 xmaximum 1100


screen seven_questions_event_menu():
    tag menu
    zorder 200
    modal True

    default selected_stage = sq_default_stage()
    default countdown_tick = 0
    $ status = sq_status()
    $ completed_stages = sq_completed_stages()
    $ unlocked_count = sq_unlocked_count()
    $ selected_unlocked = sq_stage_is_unlocked(selected_stage)
    $ selected_complete = selected_stage in completed_stages
    $ best_score = (persistent.seven_questions_best_scores or {}).get(str(selected_stage), 0)
    $ selected_question_count = len(sq_stage_questions(selected_stage))

    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=0.8)
    on "hide" action Stop("music", fadeout=0.5)
    key "K_ESCAPE" action ShowMenu("kami_event_menu")
    timer 1.0 repeat True action SetScreenVariable("countdown_tick", countdown_tick + 1)

    add "events/seven_questions/textures/bg_quiz.png" at kami_hub_background
    add Solid("#02060bb8")
    add "gui/main_menu_kami/scanlines.png" alpha 0.20
    add "gui/main_menu_kami/vignette.png" alpha 0.74

    textbutton sq_text("back"):
        style "kami_hub_return"
        xpos 28
        ypos 28
        action ShowMenu("kami_event_menu")

    text sq_text("menu_title"):
        style "kami_hub_title"
        xalign 0.5
        ypos 34

    frame:
        xpos 1492
        ypos 28
        xsize 400
        ysize 76
        background Solid("#12051de8")
        padding (22, 8, 22, 8)
        hbox:
            spacing 14
            yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(42, 42), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text sq_text("shards") style "kami_hub_meta" color "#eedfff" size 19 yalign 0.5
            text "[persistent.desire_shards]" font "fonts/Rajdhani-SemiBold.ttf" size 36 color "#ffffff" yalign 0.5

    hbox:
        xpos 30
        ypos 155
        spacing 20

        frame:
            xsize 570
            ysize 845
            background Solid("#03111cef")
            padding (15, 15, 15, 15)

            vbox:
                spacing 9
                text sq_text("select_stage") style "kami_hub_meta" size 28 xalign 0.5
                add Solid("#1c79a8") xsize 540 ysize 2

                for stage_index in range(7):
                    $ stage_unlocked = sq_stage_is_unlocked(stage_index)
                    $ stage_complete = stage_index in completed_stages
                    button:
                        style "sq_stage_row"
                        selected selected_stage == stage_index
                        action SetScreenVariable("selected_stage", stage_index)
                        at kami_card_hover

                        hbox:
                            spacing 14
                            yalign 0.5
                            frame:
                                xsize 54
                                ysize 54
                                background Solid("#ff6a2b" if selected_stage == stage_index else "#123047")
                                text "[stage_index + 1]" font "fonts/Rajdhani-SemiBold.ttf" size 27 color "#ffffff" xalign 0.5 yalign 0.5
                            vbox:
                                xsize 340
                                spacing 1
                                yalign 0.5
                                text sq_stage_title(stage_index) font "fonts/Rajdhani-SemiBold.ttf" size 22 color ("#ff7040" if selected_stage == stage_index else "#eef7fb")
                                text sq_stage_timer_label(stage_index) style "kami_hub_meta" size 14 color ("#607380" if not stage_unlocked else "#51c6ff")
                            text ("✓" if stage_complete else ("◆" if stage_unlocked else sq_text("locked"))):
                                font "fonts/Rajdhani-SemiBold.ttf"
                                size (30 if stage_unlocked else 12)
                                color ("#63d59a" if stage_complete else ("#51c6ff" if stage_unlocked else "#607380"))
                                yalign 0.5

        frame:
            xsize 1280
            ysize 845
            background Solid("#08090def")
            padding (28, 24, 28, 24)

            vbox:
                spacing 18

                hbox:
                    xfill True
                    vbox:
                        xsize 930
                        spacing 5
                        text sq_text("title") style "kami_hub_section" size 45
                        text sq_text("subtitle") style "kami_hub_meta" color "#ff7040"
                        text sq_event_timer_label() style "kami_hub_meta" size 20 color sq_status_color(status)
                    frame:
                        xsize 280
                        ysize 76
                        background Solid("#10141deb")
                        padding (12, 8, 12, 8)
                        text sq_status_label() font "fonts/Rajdhani-SemiBold.ttf" size 28 color sq_status_color(status) xalign 0.5 yalign 0.5

                add Solid("#a83e22") xsize 1224 ysize 2
                text sq_text("description") style "kami_hub_body" size 23 xsize 1200

                hbox:
                    spacing 22
                    frame:
                        xsize 760
                        ysize 300
                        background Solid("#07131dec")
                        padding (24, 20, 24, 20)
                        vbox:
                            spacing 14
                            text "[sq_text('day')] [selected_stage + 1] / 7" style "kami_hub_meta" color "#ff7040"
                            text sq_stage_title(selected_stage) style "kami_hub_section" size 40
                            text sq_stage_date_label(selected_stage) style "kami_hub_meta"
                            text sq_stage_timer_label(selected_stage) style "kami_hub_meta" size 20 color ("#607380" if not selected_unlocked else "#51c6ff")
                            if not persistent.seven_questions_intro_complete:
                                text sq_text("intro_required") style "kami_hub_meta" color "#ff7040" size 20
                            elif selected_complete:
                                text "[sq_text('done')] · [sq_text('score')] [best_score]/[selected_question_count]" style "kami_hub_meta" color "#63d59a"
                            elif selected_unlocked:
                                text sq_text("available") style "kami_hub_meta" color "#51c6ff"
                            else:
                                text sq_text("locked") style "kami_hub_meta" color "#607380"

                    frame:
                        xsize 442
                        ysize 300
                        background Solid("#14051deb")
                        padding (22, 18, 22, 18)
                        vbox:
                            spacing 10
                            xalign 0.5
                            text sq_text("reward") style "kami_hub_meta" color "#d68cff" xalign 0.5
                            add Transform("gui/main_menu_kami/glyph_kami.png", size=(72, 72), matrixcolor=TintMatrix("#b860ff")) xalign 0.5
                            text "[persistent.seven_questions_total_shards_earned] [sq_text('shards')]" font "fonts/Rajdhani-SemiBold.ttf" size 28 color "#ffffff" xalign 0.5
                            text (sq_text("outdated_reward") if status == "outdated" else sq_text("normal_reward")) font "fonts/Rajdhani-SemiBold.ttf" size 20 color "#d6c2df" xalign 0.5 text_align 0.5
                            text "[sq_text('correct_reward')] · [sq_text('stage_reward')] · [sq_text('final_reward')]" font "fonts/Rajdhani-SemiBold.ttf" size 14 color "#9ab4c4" xalign 0.5 text_align 0.5 xmaximum 390

                frame:
                    xfill True
                    ysize 82
                    background Solid("#061522")
                    padding (20, 12, 20, 12)
                    hbox:
                        xfill True
                        text "[sq_text('progress')]  [len(completed_stages)] / 7" style "kami_hub_meta" size 26 yalign 0.5
                        null width 40
                        if status == "upcoming":
                            text sq_text("upcoming_note") style "kami_hub_body" size 20 yalign 0.5 xmaximum 760
                        elif status == "outdated":
                            text sq_text("outdated_note") style "kami_hub_body" size 20 yalign 0.5 xmaximum 760

                textbutton (sq_text("start_intro") if not persistent.seven_questions_intro_complete else (sq_text("replay") if selected_complete else sq_text("play"))):
                    style "kami_hub_action"
                    xsize 520
                    ysize 82
                    xalign 1.0
                    sensitive (not persistent.seven_questions_intro_complete) or selected_unlocked
                    # L'évènement est accessible depuis le menu principal : son
                    # introduction doit donc s'exécuter dans un contexte isolé,
                    # sans reprendre le point d'entrée de la partie (Jour 0).
                    action (Function(renpy.call_in_new_context, "seven_questions_kami_intro") if not persistent.seven_questions_intro_complete else ShowMenu("seven_questions_quiz", stage_index=selected_stage))


screen seven_questions_quiz(stage_index=0):
    tag menu
    zorder 260
    modal True

    default question_index = 0
    default selected_answer = -1
    default answered = False
    default seconds_left = 20
    default score = 0

    $ questions = sq_stage_questions(stage_index)
    $ question_data = questions[question_index]
    $ question_text = question_data[0]
    $ answers = question_data[1]
    $ correct_answer = question_data[2]
    $ question_count = len(questions)
    $ stage_number = stage_index + 1
    $ question_number = question_index + 1
    $ answer_letters = ("A", "B", "C")

    key "K_ESCAPE" action ShowMenu("seven_questions_event_menu")
    timer 1.0 repeat True action If(not answered, If(seconds_left > 1, SetScreenVariable("seconds_left", seconds_left - 1), [SetScreenVariable("seconds_left", 0), SetScreenVariable("answered", True)]), NullAction())

    add "events/seven_questions/textures/bg_quiz.png" at kami_hub_background
    add Solid("#0104098c")
    add "gui/main_menu_kami/scanlines.png" alpha 0.16
    add "gui/main_menu_kami/vignette.png" alpha 0.62

    textbutton sq_text("quit"):
        style "kami_hub_return"
        xpos 28
        ypos 28
        action ShowMenu("seven_questions_event_menu")

    text sq_text("title"):
        style "kami_hub_title"
        size 54
        xalign 0.5
        ypos 28

    frame:
        xpos 1492
        ypos 28
        xsize 400
        ysize 76
        background Solid("#12051de8")
        padding (22, 8, 22, 8)
        hbox:
            spacing 14
            yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(42, 42), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text sq_text("shards") style "kami_hub_meta" color "#eedfff" size 19 yalign 0.5
            text "[persistent.desire_shards]" font "fonts/Rajdhani-SemiBold.ttf" size 36 color "#ffffff" yalign 0.5

    text "[sq_text('day')] [stage_number] / 7":
        style "kami_hub_meta"
        color "#ff7040"
        size 28
        xalign 0.5
        ypos 112

    frame:
        xpos 260
        ypos 174
        xsize 1400
        ysize 290
        background Solid("#090b0ff2")
        padding (52, 30, 52, 30)

        fixed:
            text sq_stage_title(stage_index):
                style "kami_hub_section"
                size 32
                xalign 0.5
                ypos 0
            text question_text:
                font "fonts/Rajdhani-SemiBold.ttf"
                size 40
                color "#f4f7fa"
                xalign 0.5
                text_align 0.5
                xmaximum 950
                ypos 66
            frame:
                xpos 1160
                ypos 70
                xsize 120
                ysize 120
                background Solid("#241008e8")
                text "[seconds_left]" font "fonts/Rajdhani-SemiBold.ttf" size 54 color ("#ff7040" if seconds_left > 5 else "#ff3d3d") xalign 0.5 yalign 0.5

    vbox:
        xpos 320
        ypos 490
        spacing 18

        for answer_index, answer_text in enumerate(answers):
            $ answer_selected = selected_answer == answer_index
            $ answer_is_correct = answer_index == correct_answer
            button:
                style "sq_answer_button"
                sensitive not answered
                background Solid("#0b4260f5" if answer_selected else "#090b0fef")
                hover_background Solid("#0b4260f5")
                action [SetScreenVariable("selected_answer", answer_index), SetScreenVariable("answered", True), If(answer_is_correct, [SetScreenVariable("score", score + 1), Function(sq_reward_question_action, stage_index, question_index)], NullAction())]

                hbox:
                    spacing 26
                    yalign 0.5
                    frame:
                        xsize 120
                        yfill True
                        background Solid("#0e5a80" if answer_selected else "#25120d")
                        text answer_letters[answer_index] font "fonts/Rajdhani-SemiBold.ttf" size 48 color ("#73ddff" if answer_selected else "#ff7040") xalign 0.5 yalign 0.5
                    text answer_text font "fonts/Rajdhani-SemiBold.ttf" size 36 color "#f2f4f7" yalign 0.5
                    if answered and answer_is_correct:
                        text "✓" font "fonts/Rajdhani-SemiBold.ttf" size 42 color "#63d59a" yalign 0.5 xalign 1.0

    frame:
        xpos 72
        ypos 942
        xsize 520
        ysize 86
        background Solid("#0a0c10ed")
        padding (22, 12, 22, 12)
        hbox:
            spacing 22
            yalign 0.5
            text "[sq_text('question')] [question_number] / [question_count]" style "kami_hub_meta" color "#ffffff" size 25 yalign 0.5
            for progress_index in range(question_count):
                text ("●" if progress_index <= question_index else "○") font "fonts/Rajdhani-SemiBold.ttf" size 28 color ("#ff7040" if progress_index <= question_index else "#6b7780") yalign 0.5

    if answered:
        $ feedback_key = "timeout" if selected_answer < 0 else ("correct" if selected_answer == correct_answer else "wrong")
        text sq_text(feedback_key):
            style "kami_hub_meta"
            color ("#63d59a" if selected_answer == correct_answer else "#ff7040")
            size 25
            xalign 0.5
            ypos 946

        textbutton (sq_text("finish") if question_index == question_count - 1 else sq_text("next")):
            style "sq_quiz_action"
            xpos 780
            ypos 946
            if question_index == question_count - 1:
                action [Function(sq_finish_stage, stage_index, score, question_count), ShowMenu("seven_questions_event_menu")]
            else:
                action [SetScreenVariable("question_index", question_index + 1), SetScreenVariable("selected_answer", -1), SetScreenVariable("answered", False), SetScreenVariable("seconds_left", 20)]
    else:
        text sq_text("choose"):
            style "kami_hub_meta"
            color "#6f92a8"
            size 25
            xalign 0.5
            ypos 961

    frame:
        xpos 1430
        ypos 942
        xsize 420
        ysize 86
        background Solid("#17051feb")
        padding (20, 10, 20, 10)
        hbox:
            spacing 18
            xalign 0.5
            yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(48, 48), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text (sq_text("already_earned") if sq_question_rewarded(stage_index, question_index) else ("+5 ÷ 4" if sq_status() == "outdated" else sq_text("correct_reward"))) font "fonts/Rajdhani-SemiBold.ttf" size 26 color "#d68cff" yalign 0.5
