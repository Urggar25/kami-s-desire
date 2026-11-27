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
    rotate -2
    easeout .30 alpha 1.0 zoom 1.035 rotate 0
    easein .12 zoom 1.0
    pause 1.98
    easein .39 pos (1680, 180) zoom .10 rotate 3
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

# Présentation typographique uniquement : aucune texture, photo ou icône.
# La structure du payload reste compatible avec les sauvegardes précédentes.
screen kd_argument_acquisition(serial, payload):
    modal True
    zorder 280
    $ kind, eid, heading, description, origin, category, tint, glyph = payload
    $ is_evidence = kind == "investigation"
    $ destination = _("DOSSIER D'ENQUÊTE") if is_evidence else _("DOSSIER DE VOTE")
    $ headline = _("NOUVELLE PREUVE") if is_evidence else _("NOUVEL ARGUMENT")
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

        # Quelques traits et particules, sans cadre de fiche ni illustration.
        add Solid("#36576C44", xysize=(1920, 1)) ypos 310 at kd_arg_dark
        add Solid("#36576C44", xysize=(1920, 1)) ypos 700 at kd_arg_dark
        for i in range(8):
            $ angle = i * 0.78539816
            $ distance = 310 + (i % 3) * 80
            add Solid(tint, xysize=(3, 3)):
                pos (960, 505)
                at kd_arg_particles(int(kd_arg_math.cos(angle)*distance), int(kd_arg_math.sin(angle)*distance), .08 + (i%3)*.035)

        fixed at kd_arg_card_motion:
            xysize (1460, 330)
            vbox:
                xalign .5
                yalign .5
                xsize 1460
                spacing 18
                text headline:
                    xalign .5
                    size 27 color tint font "fonts/Rajdhani-SemiBold.ttf" kerning 6
                    at kd_arg_reveal(.12)
                add Solid(tint, xysize=(160, 3)) xalign .5 at kd_arg_trace
                text kd_tr(heading):
                    xalign .5
                    text_align .5
                    xmaximum 1380
                    size 72 color "#F1FAFF" font "fonts/Rajdhani-SemiBold.ttf"
                    outlines [(2, "#03081099", 0, 2)]
                    at kd_arg_reveal(.22)
                add Solid(tint, xysize=(620, 2)) xalign .5 at kd_arg_trace
                text _("ENREGISTRÉ DANS LA TABLETTE"):
                    xalign .5
                    size 22 color tint font "fonts/Rajdhani-SemiBold.ttf" kerning 3
                    at kd_arg_confirm

        # La destination reste purement typographique.
        fixed at kd_arg_receiver:
            anchor (.5, .5)
            pos (1680, 180)
            xysize (400, 94)
            add Solid("#07121EF8", xysize=(400, 94))
            add Solid(tint, xysize=(400, 2))
            vbox:
                xalign .5
                yalign .5
                spacing 3
                text destination:
                    xalign .5
                    size 21 color tint font "fonts/Rajdhani-SemiBold.ttf"
                text (_("PREUVE AJOUTÉE") if is_evidence else _("ARGUMENT AJOUTÉ")):
                    xalign .5
                    size 22 color "#F1FAFF" font "fonts/Rajdhani-SemiBold.ttf"

# Anciens écrans sauvegardés : fermeture sans réintroduire les anciennes animations.
screen kd_vote_argument_toast(items=(), dossier_title=None):
    timer .01 action Hide("kd_vote_argument_toast")
