################################################################################
## Système de succès
################################################################################

init -1 python:
    SUCCES_IDS = [
        "succes001",
        "succes002",
        "succes003",
        "succes004",
    ]

    SUCCES_IMAGES = {
        "succes001": "gui/succes/succes001.png",
        "succes002": "gui/succes/succes002.png",
        "succes003": "gui/succes/succes003.png",
        "succes004": "gui/succes/succes004.png",
    }

    SUCCES_TITLES = {
        "succes002": "Encore humain",
        "succes003": "Un hasard bien cadré",
    }

    # Classement explicite : les succès sans chapitre connu restent accessibles
    # dans "AUTRES" et ne faussent pas la progression des neuf chapitres.
    SUCCES_CHAPTERS = {
        "succes001": 1,  # Trois morts par asphyxie, jour 1.
    }
    SUCCES_CHAPTER_TITLES = {
        1: "Le poids d'une voix",
        2: "Les lignes qui nous séparent",
        3: "La confiance ne suffit pas",
        4: "Quelque chose ne tourne pas rond",
        5: "Les apparences sont trompeuses",
        6: "Derrière les murs",
        7: "Un semblant de normalité",
        8: "Le visage du mensonge",
        9: "Le dernier départ",
    }

    def get_succes_chapter_ids(chapter):
        return [sid for sid in get_succes_ids() if SUCCES_CHAPTERS.get(sid) == chapter]

    def get_succes_other_ids():
        return [sid for sid in get_succes_ids() if SUCCES_CHAPTERS.get(sid) not in SUCCES_CHAPTER_TITLES]

    def get_succes_chapter_progress(chapter):
        ids = get_succes_chapter_ids(chapter)
        return sum(1 for sid in ids if is_succes_unlocked(sid)), len(ids)

    def succes_ensure_state():
        if not hasattr(persistent, "succes_unlocked") or persistent.succes_unlocked is None:
            persistent.succes_unlocked = {}

        if not isinstance(persistent.succes_unlocked, dict):
            persistent.succes_unlocked = {}

        if not hasattr(persistent, "succes_day1_asphyxia_deaths") or persistent.succes_day1_asphyxia_deaths is None:
            persistent.succes_day1_asphyxia_deaths = 0

    def get_succes_ids():
        return list(SUCCES_IDS)

    def get_succes_image(succes_id):
        return SUCCES_IMAGES.get(succes_id, "gui/succes/%s.png" % succes_id)

    def get_succes_title(succes_id):
        return kd_tr(SUCCES_TITLES.get(succes_id))

    def is_succes_unlocked(succes_id):
        succes_ensure_state()
        return bool(persistent.succes_unlocked.get(succes_id, False))

    def unlock_succes(succes_id):
        succes_ensure_state()

        if not persistent.succes_unlocked.get(succes_id, False):
            persistent.succes_unlocked[succes_id] = True
            kami_grant_desire_reward("achievement_{}".format(succes_id), 5, notify=False)
            renpy.save_persistent()
            renpy.show_screen("succes_notification", succes_id=succes_id)
            return True

        return False

    def unlock_succes_from_screen(succes_id):
        # Une Function action ferme un call screen si sa fonction renvoie
        # une valeur non-None. Le déblocage doit donc rester sans retour.
        unlock_succes(succes_id)

    def register_day1_asphyxia_death():
        succes_ensure_state()
        persistent.succes_day1_asphyxia_deaths += 1

        if persistent.succes_day1_asphyxia_deaths >= 3:
            unlock_succes("succes001")
        else:
            renpy.save_persistent()

        return persistent.succes_day1_asphyxia_deaths


transform succes_notification_in:
    alpha 0.0
    yoffset -20
    easeout 0.25 alpha 1.0 yoffset 0
    pause 2.40
    easein 0.25 alpha 0.0 yoffset -20


screen succes_notification(succes_id):
    zorder 250
    timer 2.90 action Hide("succes_notification")
    $ succes_title = get_succes_title(succes_id)

    frame:
        at succes_notification_in
        xalign 0.5
        ypos 34
        xminimum 420
        padding (28, 16)
        background Frame(Solid("#07121dee"), 12, 12)

        vbox:
            xalign 0.5
            spacing 2

            text _("Succès débloqué"):
                xalign 0.5
                color "#8fb4cc"
                size 18
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            if succes_title:
                text succes_title:
                    xalign 0.5
                    color "#dff7ff"
                    size 32
                    font "fonts/Barlow-Light.ttf"

            text _("+5 Éclats de désir"):
                xalign 0.5
                color "#d68cff"
                size 20
                font "fonts/Rajdhani-SemiBold.ttf"


screen succes_menu():
    tag menu

    default page = 0

    $ succes_ids = get_succes_ids()
    $ page_size = 2
    $ page_count = max(1, (len(succes_ids) + page_size - 1) // page_size)
    $ page = min(page, page_count - 1)
    $ page_succes = succes_ids[page * page_size:(page + 1) * page_size]

    add "gui/succes/succes.png" at adaptive_fullscreen
    add Solid("#00000022")

    key "game_menu" action Return()

    fixed:
        xfill True
        yfill True

        text _("SUCCÈS"):
            style "succes_menu_title"
            xalign 0.5
            ypos 82

        add Solid("#5cd3ff66", xsize=270, ysize=2):
            xalign 0.5
            ypos 146

        hbox:
            xalign 0.5
            yalign 0.53
            spacing 76

            for succes_id in page_succes:
                use succes_tile(succes_id)

            for empty_slot in range(page_size - len(page_succes)):
                null width 430 height 430

        hbox:
            xalign 0.5
            yalign 0.88
            spacing 28

            textbutton _("‹"):
                style "succes_arrow_button"
                sensitive page > 0
                action SetScreenVariable("page", max(0, page - 1))

            text _("[page + 1] / [page_count]"):
                style "succes_menu_page_text"

            textbutton _("›"):
                style "succes_arrow_button"
                sensitive page < page_count - 1
                action SetScreenVariable("page", min(page_count - 1, page + 1))

        textbutton _("RETOUR"):
            style "succes_back_button"
            xpos 92
            ypos 70
            action Return()

        if page_count > 1:
            textbutton _("SUIVANT"):
                style "succes_back_button"
                xalign 0.96
                ypos 70
                sensitive page < page_count - 1
                action SetScreenVariable("page", min(page_count - 1, page + 1))
        else:
            textbutton _("SUIVANT"):
                style "succes_back_button"
                xalign 0.96
                ypos 70
                sensitive False
                action Return()


screen succes_tile(succes_id):
    $ unlocked = is_succes_unlocked(succes_id)
    $ succes_image = get_succes_image(succes_id)

    frame:
        style "succes_tile_frame"

        fixed:
            xysize (430, 430)

            if unlocked:
                add succes_image:
                    xysize (430, 430)
                    fit "contain"
            else:
                add im.MatrixColor(succes_image, im.matrix.saturation(0.0) * im.matrix.brightness(-0.95)):
                    xysize (430, 430)
                    fit "contain"
                    alpha 0.10

                add Solid("#272d33"):
                    xysize (430, 430)
                    alpha 0.98

                add Solid("#11182099", xsize=430, ysize=3):
                    yalign 0.0

                add Solid("#5cd3ff22", xsize=430, ysize=2):
                    yalign 1.0


style succes_menu_title is gui_label_text
style succes_menu_page_text is gui_text
style succes_tile_frame is frame
style succes_back_button is button
style succes_back_button_text is button_text
style succes_arrow_button is button
style succes_arrow_button_text is button_text

style succes_menu_title:
    color "#dff7ff"
    size 48
    font "fonts/Rajdhani-SemiBold.ttf"
    kerning 8.0
    outlines [(2, "#02070ccc", 0, 2)]

style succes_menu_page_text:
    yalign 0.5
    color "#dff7ff"
    size 28
    font "fonts/Barlow-Light.ttf"
    outlines [(2, "#02070ccc", 0, 1)]

style succes_tile_frame:
    padding (0, 0)
    xysize (430, 430)
    background Fixed(
        Solid("#07111c44"),
        Solid("#5cd3ff55", xsize=3),
        Solid("#5cd3ff55", xsize=3, xalign=1.0),
        Solid("#ffffff18", ysize=1),
        Solid("#00000088", ysize=10, yalign=1.0),
    )

style succes_back_button:
    xminimum 148
    yminimum 48
    padding (18, 9)
    background Solid("#07111c88")
    hover_background Fixed(Solid("#0d2535dd"), Solid("#5cd3ff", ysize=2, yalign=1.0))
    insensitive_background Solid("#07111c44")

style succes_back_button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 24
    idle_color "#a9c7d4"
    hover_color "#ffffff"
    insensitive_color "#5f6c73"
    xalign 0.5
    textalign 0.5

style succes_arrow_button:
    xysize (54, 54)
    padding (0, 0)
    background Solid("#07111c88")
    hover_background Solid("#0d2535dd")
    insensitive_background Solid("#07111c44")

style succes_arrow_button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 38
    idle_color "#a9c7d4"
    hover_color "#ffffff"
    insensitive_color "#5f6c73"
    xalign 0.5
    yalign 0.5
    textalign 0.5

# Galerie de la tablette : vue d'ensemble par chapitre et détails des succès.
screen tablet_succes():
    modal True
    zorder 220
    default view = "chapters"
    default selected_chapter = 1
    default page = 0

    $ all_ids = get_succes_ids()
    $ overall_count = sum(1 for sid in all_ids if is_succes_unlocked(sid))
    $ chapter_ids = get_succes_other_ids() if selected_chapter == 0 else get_succes_chapter_ids(selected_chapter)
    $ chapter_done = sum(1 for sid in chapter_ids if is_succes_unlocked(sid))
    $ chapter_total = len(chapter_ids)
    $ pages = max(1, (chapter_total + 3) // 4)
    $ page_index = min(page, pages - 1)
    $ visible_ids = chapter_ids[page_index * 4:(page_index + 1) * 4]
    $ back_to_tablet = [Hide("tablet_succes"), Show("tablet_home"), With(Dissolve(0.25))]

    key "K_ESCAPE" action If(view == "chapters", back_to_tablet, [SetScreenVariable("view", "chapters"), SetScreenVariable("page", 0)])
    key "K_t" action back_to_tablet

    add Solid("#01060bcc")
    add "images/ui/tablette/tablette_3.png" fit "contain" xysize (1920, 1080)

    fixed at messenger_panel_in, tablet_profile_plane:
        xysize (940, 560)
        clipping True
        add Solid("#020912f5")
        add Solid("#0b223144", ysize=56)
        add Solid("#5cd3ff99", ysize=2) ypos 55

        text "KAMI.CORE // SUCCÈS":
            xpos 18 ypos 18 size 14 color "#5cd3ff"
            font "fonts/Barlow-Light.ttf" kerning 2.2
        text "{:02d} / {:02d} DÉBLOQUÉS".format(overall_count, len(all_ids)):
            xpos 642 ypos 20 size 13 color "#769aab"
            font "fonts/Rajdhani-SemiBold.ttf"

        textbutton "RETOUR":
            xpos 824 ypos 9 xsize 100 ysize 36 padding (8, 4)
            background Fixed(Solid("#07131de8"), Solid("#5cd3ff", ysize=2, yalign=1.0))
            hover_background Fixed(Solid("#123249f5"), Solid("#86e2ff", ysize=3, yalign=1.0))
            text_font "fonts/Rajdhani-SemiBold.ttf"
            text_size 14 text_color "#9bc7d8" text_hover_color "#ffffff"
            text_xalign 0.5 text_yalign 0.5
            action If(view == "chapters", back_to_tablet, [SetScreenVariable("view", "chapters"), SetScreenVariable("page", 0)])

        if view == "chapters":
            text "PROGRESSION PAR CHAPITRE":
                xpos 24 ypos 72 size 22 color "#eaf4ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1.5
            text "SÉLECTIONNEZ UN CHAPITRE":
                xpos 692 ypos 80 size 13 color "#8babba"
                font "fonts/Rajdhani-SemiBold.ttf"

            for chapter in range(1, 10):
                $ done, total = get_succes_chapter_progress(chapter)
                $ col = (chapter - 1) % 3
                $ row = (chapter - 1) // 3
                $ card_x = 22 + col * 302
                $ card_y = 120 + row * 128
                $ ratio = float(done) / total if total else 0.0
                button:
                    xpos card_x ypos card_y xsize 290 ysize 116
                    background Fixed(Solid("#0a1b28ee"), Solid("#2b5063", ysize=1, yalign=1.0), Solid("#294456", xsize=2))
                    hover_background Fixed(Solid("#112f42f5"), Solid("#5cd3ff", ysize=2, yalign=1.0), Solid("#5cd3ff", xsize=2))
                    action [SetScreenVariable("selected_chapter", chapter), SetScreenVariable("page", 0), SetScreenVariable("view", "details")]
                    fixed:
                        xysize (290, 116)
                        text "CHAPITRE {:02d}".format(chapter):
                            xpos 13 ypos 10 size 16 color "#5cd3ff"
                            font "fonts/Rajdhani-SemiBold.ttf" kerning 1
                        text SUCCES_CHAPTER_TITLES[chapter]:
                            xpos 13 ypos 35 xmaximum 267 size 17 color "#eaf4ff"
                            font "fonts/Rajdhani-SemiBold.ttf"
                        text ("{:d} / {:d}".format(done, total) if total else "À VENIR"):
                            xpos 215 ypos 11 xsize 62 text_align 1.0 size 14
                            color ("#8edcff" if total and done == total else "#90a7b4")
                            font "fonts/Rajdhani-SemiBold.ttf"
                        add Solid("#224255") xpos 13 ypos 91 xsize 264 ysize 7
                        if total and done:
                            add Solid("#5cd3ff") xpos 13 ypos 91 xsize int(264 * ratio) ysize 7
                        text ("TERMINÉ" if total and done == total else ("{:d}%".format(int(ratio * 100)) if total else "AUCUN SUCCÈS ASSOCIÉ")):
                            xpos 13 ypos 100 size 11 color "#809faf"
                            font "fonts/Rajdhani-SemiBold.ttf"

            text "Les succès non classés sont conservés dans AUTRES.":
                xpos 24 ypos 519 size 12 color "#7392a4"
                font "fonts/Rajdhani-SemiBold.ttf"
            textbutton "AUTRES ({:d})".format(len(get_succes_other_ids())):
                xpos 742 ypos 512 xsize 173 ysize 34
                background Solid("#102939")
                hover_background Solid("#1c4d65")
                text_size 16 text_color "#9edfff"
                text_font "fonts/Rajdhani-SemiBold.ttf"
                text_xalign 0.5 text_yalign 0.5
                action [SetScreenVariable("selected_chapter", 0), SetScreenVariable("page", 0), SetScreenVariable("view", "details")]

        else:
            text ("AUTRES SUCCÈS" if selected_chapter == 0 else "CHAPITRE {:02d} // {}".format(selected_chapter, SUCCES_CHAPTER_TITLES[selected_chapter])):
                xpos 24 ypos 70 xmaximum 740 size 22 color "#eaf4ff"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1.0
            text "{:d} / {:d} DÉBLOQUÉS".format(chapter_done, chapter_total):
                xpos 24 ypos 106 size 16 color "#9edfff"
                font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#244154") xpos 200 ypos 112 xsize 710 ysize 7
            if chapter_total and chapter_done:
                add Solid("#5cd3ff") xpos 200 ypos 112 xsize int(710.0 * chapter_done / chapter_total) ysize 7
            add Solid("#294c5e") xpos 22 ypos 133 xsize 895 ysize 1

            if chapter_total:
                grid 2 2:
                    xpos 29 ypos 148 xspacing 18 yspacing 13
                    for sid in visible_ids:
                        use tablet_succes_card(sid)
                    for missing in range(4 - len(visible_ids)):
                        null width 430 height 164
            else:
                text "AUCUN SUCCÈS ASSOCIÉ À CE CHAPITRE POUR LE MOMENT.":
                    xalign 0.5 ypos 300 size 19 color "#7e9baa"
                    font "fonts/Rajdhani-SemiBold.ttf"

            add Solid("#294c5e") xpos 22 ypos 507 xsize 895 ysize 1
            textbutton "‹ CHAPITRES":
                xpos 26 ypos 513 xsize 150 ysize 35
                background Solid("#102939")
                hover_background Solid("#1c4d65")
                text_size 16 text_color "#9edfff"
                text_font "fonts/Rajdhani-SemiBold.ttf"
                text_xalign 0.5 text_yalign 0.5
                action [SetScreenVariable("view", "chapters"), SetScreenVariable("page", 0)]
            if pages > 1:
                hbox:
                    xpos 710 ypos 514 spacing 12
                    textbutton "‹":
                        xysize (34, 32)
                        sensitive page_index > 0
                        background Solid("#102939")
                        hover_background Solid("#1c4d65")
                        text_size 22 text_color "#9edfff"
                        text_xalign 0.5 text_yalign 0.5
                        action SetScreenVariable("page", page_index - 1)
                    text "{:d} / {:d}".format(page_index + 1, pages):
                        yalign 0.5 size 14 color "#aacddd"
                        font "fonts/Rajdhani-SemiBold.ttf"
                    textbutton "›":
                        xysize (34, 32)
                        sensitive page_index + 1 < pages
                        background Solid("#102939")
                        hover_background Solid("#1c4d65")
                        text_size 22 text_color "#9edfff"
                        text_xalign 0.5 text_yalign 0.5
                        action SetScreenVariable("page", page_index + 1)

    add "images/ui/tablette/tablette_pouce.png" fit "contain" xysize (1920, 1080)


screen tablet_succes_card(sid):
    $ unlocked = is_succes_unlocked(sid)
    $ title = get_succes_title(sid) if unlocked else None
    frame:
        xsize 430 ysize 164 padding (0, 0)
        background Fixed(Solid("#0a1b28eb"), Solid("#5cd3ff88" if unlocked else "#294456", xsize=2), Solid("#214257", ysize=1, yalign=1.0))
        fixed:
            xysize (430, 164)
            if unlocked:
                add Transform(get_succes_image(sid), fit="contain", xysize=(140, 140)) xpos 10 ypos 11
            else:
                add Solid("#142633") xpos 10 ypos 11 xysize (140, 140)
                add Transform("hud/codex/badge_lock.png", fit="contain", xysize=(54, 54)) xpos 53 ypos 54
            text (title or ("SUCCÈS DÉBLOQUÉ" if unlocked else "SUCCÈS VERROUILLÉ")):
                xpos 164 ypos 31 xmaximum 236 size 21
                color ("#eaf4ff" if unlocked else "#7792a1")
                font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#254659") xpos 164 ypos 95 xsize 232 ysize 1
            text ("OBTENU" if unlocked else "NON DÉCOUVERT"):
                xpos 164 ypos 109 size 15
                color ("#5cd3ff" if unlocked else "#657e8f")
                font "fonts/Rajdhani-SemiBold.ttf" kerning 1
