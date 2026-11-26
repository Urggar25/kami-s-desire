# Non-modal vote dossier feedback. The unlock remains authoritative.
default kd_vote_notice_items = ()

init python:
    def kd_vote_argument_notice(aid):
        if renpy.is_skipping() or aid not in DOSSIER_ARGS:
            return
        item = DOSSIER_ARGS[aid]
        cat = DOSSIER_ARG_CATS.get(item.get("cat"), {})
        # A single card batches back-to-back discoveries, without blocking.
        old = store.kd_vote_notice_items if renpy.get_screen("kd_vote_argument_toast") else ()
        store.kd_vote_notice_items = tuple((old + ((item["title"], cat.get("color", "#5CD3FF")),))[-4:])
        renpy.hide_screen("kd_vote_argument_toast")
        renpy.show_screen("kd_vote_argument_toast", items=store.kd_vote_notice_items)
        if renpy.loadable("audio/sfx_question.mp3"):
            renpy.sound.play("audio/sfx_question.mp3", relative_volume=.30)

    # Same card-to-folder animation for the investigation dossier.
    # Registration remains the responsibility of investigation_add.
    def kd_investigation_argument_notice(eid):
        if renpy.is_skipping() or eid not in INVESTIGATION_ENTRIES:
            return False
        entry = INVESTIGATION_ENTRIES[eid]
        item = (entry["title"], investigation_category_color(entry["category"]))
        renpy.hide_screen("kd_vote_argument_toast")
        store.kd_vote_notice_items = ()
        renpy.show_screen("kd_vote_argument_toast", items=(item,), dossier_title=_("DOSSIER D'ENQUÊTE  /  + ARGUMENT"))
        if renpy.loadable("audio/sfx_question.mp3"):
            renpy.sound.play("audio/sfx_question.mp3", relative_volume=.30)
        return True

transform kd_vote_notice_slide:
    subpixel True
    alpha 0.0
    xoffset 70
    easeout .22 alpha 1.0 xoffset 0
    pause 1.65
    easein .40 alpha 0.0 xoffset 35

screen kd_vote_argument_toast(items, dossier_title=None):
    modal False
    zorder 95
    frame at kd_vote_notice_slide:
        xalign .97
        yalign .19
        xsize 420
        padding (18, 14)
        background Solid("#0B1C2AF5")
        vbox:
            spacing 9
            text (dossier_title or _("DOSSIER DE VOTE  /  + ARGUMENT")):
                size 19
                color "#79DDEF"
            for title, tint in items:
                hbox:
                    spacing 10
                    add Solid(tint) xsize 4 ysize 34
                    text kd_tr(title):
                        size 25
                        color "#E8F7FF"
                        xmaximum 350
            text _("Enregistré automatiquement"):
                size 17
                color "#83C8B9"
    # Dedicated dossier receiver: visible during the animation even with the tablet closed.
    fixed:
        xalign .97
        yalign .065
        xysize (76, 76)
        at kd_vote_receiver_pulse
        add Solid("#173849F0") xysize (76, 76)
        add Solid("#79DDEF") xpos 0 ypos 0 xysize (76, 2)
        add Solid("#79DDEF") xpos 0 ypos 74 xysize (76, 2)
        add Transform("hud/dossier/ic_box.png", xysize=(42, 42), fit="contain") xalign .5 yalign .42
        text ("+%d" % len(items)) size 18 color "#E8F7FF" xalign .5 yalign .93
    fixed at kd_vote_card_fly:
        xpos (config.screen_width - 255)
        ypos int(config.screen_height * .24)
        xysize (100, 62)
        add Solid("#102B3A") xysize (100, 62)
        add Solid("#79DDEF") xpos 0 ypos 0 xysize (100, 3)
        add Transform("hud/dossier/ic_box.png", xysize=(40, 40), fit="contain") xalign .5 yalign .5
    timer 2.95 action Hide("kd_vote_argument_toast")

transform kd_vote_card_fly:
    subpixel True
    alpha 0.0
    zoom 1.0
    pause 1.65
    easeout .10 alpha 1.0
    easein .42 xoffset 164 yoffset (-int(config.screen_height * .19)) zoom .35
    linear .08 alpha 0.0

transform kd_vote_receiver_pulse:
    alpha 0.0
    zoom 1.0
    easeout .18 alpha 1.0
    pause 1.99
    easeout .10 zoom 1.13
    easein .18 zoom 1.0
    pause .23
    easein .20 alpha 0.0

