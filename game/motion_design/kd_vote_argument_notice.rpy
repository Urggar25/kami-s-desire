# CONCLAVE OS — acquisition unique des arguments et preuves.
# Le déblocage est immédiat. La mise en scène est une file visuelle, jamais
# une condition de progression ou une seconde source de vérité.
default kd_argument_queue = []
default kd_argument_serial = 0
# Conservé uniquement pour les sauvegardes de l'ancien toast.
default kd_vote_notice_items = ()

init python:
    import math as kd_arg_math
    KD_ARGUMENT_DURATION = 3.15

    def kd_argument_play_sfx(path, volume):
        if renpy.loadable(path):
            renpy.sound.play(path, channel="kd_fx", relative_volume=volume)

    def kd_argument_payload(kind, key):
        if kind == "vote":
            entry = DOSSIER_ARGS.get(key)
            if not entry:
                return None
            category = dossier_arg_cat(key)
            return (kind, key, entry["title"], entry.get("desc", ""),
                entry.get("source", ""), category.get("label", ""),
                category.get("color", "#5CD3FF"), category.get("icon", "hud/dossier/ic_box.png"))
        if kind == "investigation":
            entry = INVESTIGATION_ENTRIES.get(key)
            if not entry:
                return None
            category = entry.get("category", "preuves")
            return (kind, key, entry["title"], entry.get("desc", ""),
                entry.get("origin", ""), investigation_category_label(category),
                investigation_category_color(category), "hud/dossier/ic_box.png")
        return (kind, key, key, "", "", _("INFORMATION"), "#5CD3FF", "hud/dossier/ic_box.png")

    def kd_argument_open_next():
        if not store.kd_argument_queue:
            renpy.hide_screen("kd_argument_acquisition")
            return
        serial, payload = store.kd_argument_queue[0]
        renpy.show_screen("kd_argument_acquisition", serial=serial, payload=payload)
        kd_argument_play_sfx("audio/trailer/trl_riser_short.wav", .28)

    def kd_argument_enqueue(kind, key):
        if renpy.is_skipping():
            return False
        payload = kd_argument_payload(kind, key)
        if payload is None:
            return False
        queue = list(store.kd_argument_queue) if renpy.get_screen("kd_argument_acquisition") else []
        if any(item[1][:2] == payload[:2] for item in queue):
            return False
        store.kd_argument_serial += 1
        queue.append((store.kd_argument_serial, payload))
        store.kd_argument_queue = queue
        if len(queue) == 1:
            kd_argument_open_next()
        return True

    def kd_argument_validate(serial):
        if store.kd_argument_queue and store.kd_argument_queue[0][0] == serial:
            kd_argument_play_sfx("audio/sfx_interrupt_impact.wav", .24)

    def kd_argument_finish(serial):
        if not store.kd_argument_queue or store.kd_argument_queue[0][0] != serial:
            return
        store.kd_argument_queue = store.kd_argument_queue[1:]
        renpy.hide_screen("kd_argument_acquisition")
        if store.kd_argument_queue:
            kd_argument_open_next()
        renpy.restart_interaction()

    # Alias de compatibilité pour les anciennes routes et appels de sauvegardes.
    def kd_vote_argument_notice(aid):
        return kd_argument_enqueue("vote", aid)

    def kd_investigation_argument_notice(eid):
        return kd_argument_enqueue("investigation", eid)

transform kd_arg_dark:
    alpha 0.0
    linear .14 alpha .88
    pause 2.65
    linear .28 alpha 0.0

transform kd_arg_flash:
    alpha 0.0
    pause .12
    linear .05 alpha .20
    linear .18 alpha 0.0

transform kd_arg_card_motion:
    subpixel True
    anchor (.5, .5)
    pos (960, 505)
    zoom .74
    alpha 0.0
    rotate -7
    easeout .30 alpha 1.0 zoom 1.035 rotate 0
    easein .12 zoom 1.0
    pause 1.98
    easein .39 pos (1680, 180) zoom .10 rotate 8
    linear .08 alpha 0.0

transform kd_arg_reveal(delay=.12):
    alpha 0.0
    xoffset -28
    pause delay
    easeout .22 alpha 1.0 xoffset 0

transform kd_arg_scan:
    alpha 0.0
    ypos 0
    pause .32
    alpha .85
    linear .62 ypos 328
    linear .12 alpha 0.0

transform kd_arg_trace:
    xzoom 0.0
    alpha .7
    easeout .35 xzoom 1.0
    pause 1.45
    linear .28 alpha 0.0

transform kd_arg_ring:
    anchor (.5, .5)
    zoom .4 alpha 0.0
    pause .14
    alpha .65
    easeout .66 zoom 1.5 alpha 0.0

transform kd_arg_confirm:
    alpha 0.0
    zoom 1.18
    pause .98
    easeout .15 alpha 1.0 zoom 1.0

transform kd_arg_receiver:
    alpha 0.0
    zoom .94
    pause 2.28
    easeout .20 alpha 1.0 zoom 1.0
    pause .27
    easeout .10 zoom 1.10
    easein .12 zoom 1.0
    linear .18 alpha 0.0

transform kd_arg_particles(dx, dy, delay):
    alpha 0.0
    xoffset 0 yoffset 0
    pause delay
    alpha .9
    easeout .54 xoffset dx yoffset dy alpha 0.0

screen kd_argument_acquisition(serial, payload):
    modal True
    zorder 280
    $ kind, eid, heading, description, origin, category, tint, glyph = payload
    $ is_evidence = kind == "investigation"
    $ destination = _("DOSSIER D'ENQUÊTE") if is_evidence else _("DOSSIER DE VOTE")
    $ headline = _("NOUVELLE PREUVE") if is_evidence else _("NOUVEL ARGUMENT")
    # Les événements du joueur ne doivent pas avancer le dialogue sous la carte.
    key "dismiss" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "game_menu" action NullAction()
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip" action NullAction()
    timer 1.04 action Function(kd_argument_validate, serial) id ("kd_arg_audio_%d" % serial)
    timer KD_ARGUMENT_DURATION action Function(kd_argument_finish, serial) id ("kd_arg_timer_%d" % serial)

    fixed:
        id ("kd_arg_visual_%d" % serial)
        xysize (1920, 1080)
        add Solid("#030810") at kd_arg_dark
        add Solid(tint) at kd_arg_flash
        for yy in range(170, 940, 62):
            add Solid("#36576C22", xysize=(1920, 1)) ypos yy at kd_arg_dark
        for xx in range(80, 1920, 110):
            add Solid("#36576C18", xysize=(1, 1080)) xpos xx at kd_arg_dark
        add Solid(tint, xysize=(1920, 2)) ypos 225 at kd_arg_trace
        add Solid(tint, xysize=(1920, 2)) ypos 805 at kd_arg_trace
        fixed at kd_arg_ring:
            pos (960, 505)
            xysize (1250, 560)
            add Solid(tint, xysize=(1250, 2))
            add Solid(tint, xysize=(1250, 2)) ypos 558
            add Solid(tint, xysize=(2, 560))
            add Solid(tint, xysize=(2, 560)) xpos 1248
        # Particules géométriques issues du noyau, sans texture supplémentaire.
        for i in range(18):
            $ angle = i * 0.34906585
            $ distance = 350 + (i % 4) * 95
            add Solid(tint, xysize=(3 + i % 4, 3 + i % 4)):
                pos (960, 505)
                at kd_arg_particles(int(kd_arg_math.cos(angle)*distance), int(kd_arg_math.sin(angle)*distance), .08 + (i%3)*.035)

        fixed at kd_arg_card_motion:
            xysize (1180, 510)
            add Solid("#00000099", xysize=(1180, 510)) pos (8, 12)
            add Solid("#07121EF8", xysize=(1180, 510))
            add Solid(tint, xysize=(1180, 3))
            add Solid("#36556A", xysize=(1180, 1)) ypos 509
            add Solid("#36556A", xysize=(1, 510)) xpos 1179
            add Solid(tint, xysize=(6, 510))
            # Corners, serialisation and split header.
            for px, py in [(14, 14), (1118, 14), (14, 488), (1118, 488)]:
                add Solid(tint, xysize=(48, 2)) pos (px, py)
            text _("CONCLAVE OS  /  ACQUISITION"):
                pos (44, 25) size 21 color tint font "fonts/Rajdhani-SemiBold.ttf" kerning 3
            text ("%03d" % serial):
                xanchor 1.0 xpos 1136 ypos 25 size 21 color "#90ADBF" font "fonts/Rajdhani-SemiBold.ttf"
            add Solid("#294252", xysize=(1092, 1)) pos (44, 65)
            fixed:
                pos (44, 93)
                xysize (235, 330)
                add Solid("#102638", xysize=(235, 330))
                add Solid(tint, xysize=(235, 2))
                add Solid(tint, xysize=(235, 2)) ypos 328
                if is_evidence:
                    add Transform(investigation_evidence_image(eid), xysize=(215, 215), fit="contain") pos (10, 29)
                else:
                    add Transform(glyph, xysize=(114, 114), fit="contain") xalign .5 ypos 75 at kd_arg_reveal(.23)
                text kd_tr(category):
                    xalign .5 ypos 273 xmaximum 215 text_align .5 size 21 color tint font "fonts/Rajdhani-SemiBold.ttf"
                add Solid(tint, xysize=(235, 4)) at kd_arg_scan
            vbox:
                pos (315, 94)
                xsize 815
                spacing 13
                text headline:
                    size 32 color tint font "fonts/Rajdhani-SemiBold.ttf" kerning 4 at kd_arg_reveal(.12)
                text kd_tr(heading):
                    size 46 color "#F1FAFF" font "fonts/Rajdhani-SemiBold.ttf" xmaximum 815 at kd_arg_reveal(.22)
                add Solid(tint, xysize=(810, 2)) at kd_arg_trace
                if description:
                    text kd_tr(description):
                        size 24 color "#D1E1EB" xmaximum 815 at kd_arg_reveal(.40)
                if origin:
                    text (_("SOURCE") + "  /  " + kd_tr(origin)):
                        size 20 color "#91B9CA" font "fonts/Rajdhani-SemiBold.ttf" xmaximum 815 at kd_arg_reveal(.55)
            fixed:
                pos (44, 444)
                xysize (1092, 42)
                add Solid("#142D3C", xysize=(1092, 42))
                add Solid(tint, xysize=(1092, 2))
                text _("ENREGISTRÉ  //  DISPONIBLE DANS LA TABLETTE"):
                    xalign .5 yalign .5 size 23 color tint font "fonts/Rajdhani-SemiBold.ttf" kerning 2 at kd_arg_confirm

        fixed at kd_arg_receiver:
            anchor (.5, .5)
            pos (1680, 180)
            xysize (340, 118)
            add Solid("#07121EF8", xysize=(340, 118))
            add Solid(tint, xysize=(340, 3))
            add Transform("hud/dossier/ic_box.png", xysize=(65, 65), fit="contain") pos (14, 23)
            vbox:
                pos (90, 22)
                spacing 3
                text destination size 21 color tint font "fonts/Rajdhani-SemiBold.ttf"
                text (_("PREUVE AJOUTÉE") if is_evidence else _("ARGUMENT AJOUTÉ")) size 22 color "#F1FAFF" font "fonts/Rajdhani-SemiBold.ttf"

# Anciens écrans sauvegardés : fermeture sans réintroduire les anciennes animations.
screen kd_vote_argument_toast(items=(), dossier_title=None):
    timer .01 action Hide("kd_vote_argument_toast")
