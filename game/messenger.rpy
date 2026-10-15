# Messagerie de la tablette du Conclave.
# Les conversations sont scenarisees : l'application ne s'ouvre que lorsqu'un
# echange est en attente et chaque clic revele le message suivant.

default messenger_threads = {}
default messenger_thread_contacts = {}
default messenger_active_thread = None
default messenger_active_contact = None
default messenger_active_start = 0
default messenger_active_end = 0
default messenger_revealed_count = 0
default messenger_objective_active = False
default messenger_objective_text = "Consulter les messages"

init python:
    def messenger_contact_name(contact_id):
        contact_id = str(contact_id or "")
        profile_data = getattr(store, "PROFILE_DATA", {})
        if contact_id in profile_data:
            return profile_data[contact_id].get("name", contact_id.capitalize())
        return contact_id.replace("_", " ").title() or "Messagerie"

    def messenger_portrait(contact_id):
        contact_id = str(contact_id or "")
        portrait = "images/character/{}/portrait.png".format(contact_id)
        if renpy.loadable(portrait):
            return portrait
        fallback = "images/character/vide.png"
        return fallback if renpy.loadable(fallback) else Solid("#17334A")

    def messenger_has_pending():
        return bool(
            getattr(store, "messenger_objective_active", False)
            and getattr(store, "messenger_active_thread", None)
        )

    def messenger_begin(thread_id, contact_id, messages, objective_text="Consulter les messages", notify=True):
        thread_id = str(thread_id)
        contact_id = str(contact_id)

        threads = dict(getattr(store, "messenger_threads", {}) or {})
        history = list(threads.get(thread_id, []) or [])
        start_index = len(history)

        for raw_message in list(messages or []):
            if isinstance(raw_message, dict):
                sender = str(raw_message.get("sender", contact_id))
                text = str(raw_message.get("text", ""))
            else:
                sender, text = raw_message
                sender = str(sender)
                text = str(text)
            if text:
                history.append({"sender": sender, "text": text})

        if len(history) == start_index:
            return False

        threads[thread_id] = history
        contacts = dict(getattr(store, "messenger_thread_contacts", {}) or {})
        contacts[thread_id] = contact_id

        store.messenger_threads = threads
        store.messenger_thread_contacts = contacts
        store.messenger_active_thread = thread_id
        store.messenger_active_contact = contact_id
        store.messenger_active_start = start_index
        store.messenger_active_end = len(history)
        store.messenger_revealed_count = start_index + 1
        store.messenger_objective_text = str(objective_text or "Consulter les messages")
        store.messenger_objective_active = True

        if notify:
            if renpy.loadable("audio/sfx_beep.mp3"):
                renpy.sound.play("audio/sfx_beep.mp3")
            renpy.notify("Nouveau message — {}".format(messenger_contact_name(contact_id)))
        renpy.restart_interaction()
        return True

    def messenger_visible_messages(max_messages=4):
        thread_id = getattr(store, "messenger_active_thread", None)
        if not thread_id:
            return []
        history = list((getattr(store, "messenger_threads", {}) or {}).get(thread_id, []) or [])
        revealed = min(int(getattr(store, "messenger_revealed_count", 0)), len(history))
        return history[:revealed][-max_messages:]

    def messenger_current_progress():
        start = int(getattr(store, "messenger_active_start", 0))
        end = int(getattr(store, "messenger_active_end", 0))
        revealed = int(getattr(store, "messenger_revealed_count", 0))
        total = max(0, end - start)
        current = max(0, min(total, revealed - start))
        return current, total

    def messenger_advance():
        if not messenger_has_pending():
            return

        revealed = int(getattr(store, "messenger_revealed_count", 0))
        end = int(getattr(store, "messenger_active_end", 0))
        if revealed < end:
            store.messenger_revealed_count = revealed + 1
            if renpy.loadable("audio/sfx_beep.mp3"):
                renpy.sound.play("audio/sfx_beep.mp3", relative_volume=0.45)
            renpy.restart_interaction()
            return

        store.messenger_objective_active = False
        renpy.hide_screen("messenger_conversation")
        renpy.hide_screen("tablet_home")
        renpy.restart_interaction()

    def messenger_no_recent():
        renpy.notify("Aucun message récent")


transform messenger_panel_in:
    alpha 0.0
    yoffset 18
    easeout 0.22 alpha 1.0 yoffset 0


transform messenger_tablet_plane:
    # Centre et rotation du plan dessine dans tablette_messagerie.png.
    subpixel True
    xanchor 0.5
    yanchor 0.5
    xpos 0.45
    ypos 0.43
    zoom 0.96
    rotate 8.0


screen messenger_objective_gate():
    # Ecran exclusivement appele par le label messenger_play : son Return()
    # rend la main au scenario des que la conversation a ete lue.
    zorder 60

    key "K_t" action Show("tablet_home")

    if messenger_objective_active:
        frame at messenger_panel_in:
            xalign 0.025
            yalign 0.83
            xmaximum 430
            background Solid("#06111BEF")
            padding (20, 14)

            vbox:
                spacing 4
                text "OBJECTIF":
                    size 18
                    color "#6FA6C6"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 3
                text messenger_objective_text:
                    size 28
                    color "#BCEFFF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                text "Ouvrir la tablette puis la Messagerie":
                    size 16
                    color "#7795A8"
                    font "fonts/Rajdhani-SemiBold.ttf"

        timer 0.08 repeat True action If(
            not messenger_objective_active,
            Return(True),
            NullAction()
        )


screen messenger_conversation():
    modal True
    zorder 220

    $ _contact_id = messenger_active_contact or ""
    $ _contact_name = messenger_contact_name(_contact_id)
    $ _visible_messages = messenger_visible_messages(3)
    $ _progress_current, _progress_total = messenger_current_progress()
    $ _exchange_complete = (_progress_total > 0 and _progress_current >= _progress_total)

    key "K_ESCAPE" action Function(renpy.notify, "Consultez tous les messages.")
    key "K_SPACE" action Function(messenger_advance)
    key "K_RETURN" action Function(messenger_advance)
    key "mouseup_1" action Function(messenger_advance)

    add Solid("#01060BCC")
    add "images/ui/tablette/tablette_messagerie.png" fit "contain" xysize (1920, 1080)

    # L'application est rendue dans le plan incline de l'ecran et non dans
    # une fenetre droite superposee a la tablette.
    fixed at messenger_panel_in, messenger_tablet_plane:
        xysize (940, 560)

        fixed:
            xysize (940, 560)

            # Une seule discussion est accessible : celle liee a l'objectif.
            fixed:
                xpos 0 ypos 0
                xysize (225, 560)

                text "MESSAGERIE":
                    xpos 18 ypos 17
                    size 23 color "#E8F7FF"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2
                text "CANAL PRIVE":
                    xpos 20 ypos 48
                    size 12 color "#5CD3FF"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2

                frame:
                    xpos -6 ypos 68
                    xsize 200 ysize 82
                    padding (9, 9)
                    background None

                    hbox:
                        spacing 10
                        fixed:
                            xysize (60, 60)
                            add Solid("#5CD3FF") xysize (60, 60)
                            add Transform(messenger_portrait(_contact_id), fit="cover", xsize=54, ysize=54) xpos 3 ypos 3
                        vbox:
                            yalign 0.5
                            spacing 2
                            text _contact_name:
                                size 21 color "#FFFFFF"
                                font "fonts/Rajdhani-SemiBold.ttf"
                            text "Nouveau message":
                                size 13 color "#79CFF2"
                                font "fonts/Rajdhani-SemiBold.ttf"

            # En-tete de la discussion.
            fixed:
                xpos 300 ypos -8
                xysize (640, 92)

                fixed:
                    xpos 18 ypos 12
                    xysize (60, 60)
                    add Solid("#5CD3FF") xysize (60, 60)
                    add Transform(messenger_portrait(_contact_id), fit="cover", xsize=54, ysize=54) xpos 3 ypos 3

                text _contact_name:
                    xpos 120 ypos 15
                    size 29 color "#FFFFFF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                text "●  CANAL SECURISE":
                    xpos 121 ypos 49
                    size 13 color "#53D48B"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 2

            # Derniers messages visibles. Aucun horodatage ni accuse de lecture.
            fixed:
                xpos 315 ypos 102
                xysize (600, 388)

                vbox:
                    xsize 600
                    yalign 1.0
                    spacing 9

                    for _message in _visible_messages:
                        $ _sender = _message.get("sender", _contact_id)
                        $ _from_noam = (_sender == "noam")

                        if _from_noam:
                            hbox:
                                xalign 1.0
                                spacing 9
                                frame:
                                    xmaximum 440
                                    padding (15, 10)
                                    background Solid("#0D567BEE")
                                    text _message.get("text", ""):
                                        size 18 color "#F5FBFF"
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                        xmaximum 410
                                fixed:
                                    xysize (46, 46)
                                    add Solid("#79CFF2") xysize (46, 46)
                                    add Transform(messenger_portrait("noam"), fit="cover", xsize=42, ysize=42) xpos 2 ypos 2
                        else:
                            hbox:
                                xalign 0.0
                                spacing 9
                                fixed:
                                    xysize (46, 46)
                                    add Solid("#54758D") xysize (46, 46)
                                    add Transform(messenger_portrait(_sender), fit="cover", xsize=42, ysize=42) xpos 2 ypos 2
                                frame:
                                    xmaximum 440
                                    padding (15, 10)
                                    background Solid("#173044EE")
                                    text _message.get("text", ""):
                                        size 18 color "#E8F2F8"
                                        font "fonts/Rajdhani-SemiBold.ttf"
                                        xmaximum 410

            fixed:
                xpos 225 ypos 506
                xysize (715, 54)
                text ("Cliquer pour fermer" if _exchange_complete else "Cliquer pour afficher le message suivant"):
                    xalign 0.5 yalign 0.5
                    size 16 color ("#53D48B" if _exchange_complete else "#79CFF2")
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 1

label messenger_play(thread_id, contact_id, messages, objective_text="Consulter les messages", notify=True):
    $ _messenger_started = messenger_begin(thread_id, contact_id, messages, objective_text, notify)
    if _messenger_started:
        call screen messenger_objective_gate
    return
