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

transform kd_vote_notice_slide:
    subpixel True
    alpha 0.0
    xoffset 70
    easeout .22 alpha 1.0 xoffset 0
    pause 2.4
    easein .30 alpha 0.0 xoffset 70

screen kd_vote_argument_toast(items):
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
            text _("DOSSIER DE VOTE  /  + ARGUMENT"):
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
    timer 2.95 action Hide("kd_vote_argument_toast")
