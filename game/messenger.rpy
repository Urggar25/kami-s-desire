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
    # Écran appelé via call screen : Return() rend la main au scénario.
    zorder 60

    key "K_t" action Show("tablet_home")

    # Le contrôle de fin reste actif même quand l'objectif disparaît.
    timer 0.08 repeat True action If(
        not messenger_objective_active,
        Return(True),
        NullAction()
    )

    # Ne pas afficher la carte d'objectif PAR-DESSOUS la tablette.
    if messenger_objective_active and not renpy.get_screen("tablet_home") and not renpy.get_screen("messenger_conversation"):
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


screen messenger_conversation():
    modal True
    zorder 220

    $ _contact_id = messenger_active_contact or ""
    $ _contact_name = messenger_contact_name(_contact_id)
    $ _visible_messages = messenger_visible_messages(4)
    $ _progress_current, _progress_total = messenger_current_progress()
    $ _exchange_complete = (_progress_total > 0 and _progress_current >= _progress_total)

    # Fonctionnement existant : chaque clic/touche révèle le message suivant.
    key "K_ESCAPE" action Function(renpy.notify, "Consultez tous les messages.")
    key "K_SPACE" action Function(messenger_advance)
    key "K_RETURN" action Function(messenger_advance)
    key "mouseup_1" action Function(messenger_advance)

    add Solid("#01060BCC")
    add "images/ui/tablette/tablette_messagerie.png" fit "contain" xysize (1920, 1080)

    # Tous les composants suivent le même plan que l'illustration :
    # aucun panneau 2D droit ne déborde du cadre de la tablette.
    fixed at messenger_panel_in, messenger_tablet_plane:
        xysize (940, 560)

        # Volet gauche : conversation disponible et véritable état vide.
        fixed:
            xpos 0 ypos 0
            xysize (225, 560)

            text "MESSAGERIE":
                xpos 18 ypos 14
                size 26 color "#F2FAFF"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text "CANAL PRIVÉ":
                xpos 20 ypos 49
                size 13 color "#70DBFF"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2

            frame:
                xpos 0 ypos 66
                xsize 214 ysize 88
                padding (9, 9)
                background Solid("#13507599")

                hbox:
                    spacing 11
                    fixed:
                        xysize (64, 64)
                        add Solid("#68D6FF") xysize (64, 64)
                        add Transform(messenger_portrait(_contact_id), fit="cover", xsize=58, ysize=58) xpos 3 ypos 3
                    vbox:
                        yalign 0.5
                        spacing 3
                        text _contact_name:
                            size 23 color "#FFFFFF"
                            font "fonts/Rajdhani-SemiBold.ttf"
                        text ("Lecture terminée" if _exchange_complete else "Nouveaux messages"):
                            size 15 color "#A0E4FF"
                            font "fonts/Rajdhani-SemiBold.ttf"

            # Les cases vides dessinées sur le fond étaient trompeuses :
            # on les masque sans ajouter de faux contacts cliquables.
            add Solid("#071827F4") xpos 0 ypos 160 xsize 213 ysize 378
            add Solid("#4AA7CB66") xpos 18 ypos 185 xsize 176 ysize 1
            text "CONVERSATIONS":
                xpos 18 ypos 195
                size 15 color "#82C9E9"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            text "Les autres discussions apparaîtront ici.":
                xpos 18 ypos 228
                xmaximum 175
                size 17 color "#688EA5"
                font "fonts/Rajdhani-SemiBold.ttf"
                line_spacing 2
            text "01 / 01":
                xpos 18 ypos 506
                size 15 color "#547D92"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2

        # En-tête et identité du correspondant (indépendant du défilement).
        fixed:
            xpos 284 ypos 0
            xysize (656, 95)

            fixed:
                xpos 20 ypos 11
                xysize (70, 70)
                add Solid("#6DDFFF") xysize (70, 70)
                add Transform(messenger_portrait(_contact_id), fit="cover", xsize=64, ysize=64) xpos 3 ypos 3
            text _contact_name:
                xpos 111 ypos 12
                size 32 color "#FFFFFF"
                font "fonts/Rajdhani-SemiBold.ttf"
            text "●  CANAL SÉCURISÉ":
                xpos 114 ypos 53
                size 14 color "#60E4A3"
                font "fonts/Rajdhani-SemiBold.ttf" kerning 2
            add Solid("#55D5FF77") xpos 14 ypos 91 xsize 612 ysize 1

        # Le centre de l'écran est dédié aux dialogues, non au décor.
        # La zone coupe le texte trop long proprement et accepte la molette.
        viewport:
            xpos 296 ypos 110
            xsize 623 ysize 382
            mousewheel True
            draggable False
            yinitial 1.0

            vbox:
                xsize 610
                spacing 13

                for _index, _message in enumerate(_visible_messages):
                    $ _sender = _message.get("sender", _contact_id)
                    $ _from_noam = (_sender == "noam")
                    $ _consecutive = (_index > 0 and _visible_messages[_index - 1].get("sender") == _sender)

                    if _from_noam:
                        hbox:
                            xalign 1.0
                            spacing 11
                            frame:
                                xmaximum 462
                                padding (17, 12)
                                background Solid("#145D83F0")
                                text _message.get("text", ""):
                                    size 23 color "#F4FAFF"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    xmaximum 428
                                    line_spacing 2
                            if _consecutive:
                                null width 48 height 48
                            else:
                                fixed:
                                    xysize (48, 48)
                                    add Solid("#8DDCFF") xysize (48, 48)
                                    add Transform(messenger_portrait("noam"), fit="cover", xsize=44, ysize=44) xpos 2 ypos 2
                    else:
                        hbox:
                            xalign 0.0
                            spacing 11
                            if _consecutive:
                                null width 48 height 48
                            else:
                                fixed:
                                    xysize (48, 48)
                                    add Solid("#668CA5") xysize (48, 48)
                                    add Transform(messenger_portrait(_sender), fit="cover", xsize=44, ysize=44) xpos 2 ypos 2
                            frame:
                                xmaximum 462
                                padding (17, 12)
                                background Solid("#21394FF0")
                                text _message.get("text", ""):
                                    size 23 color "#F0F6FB"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    xmaximum 428
                                    line_spacing 2

        # Barre de progression lisible (mêmes contrôles au clic qu'avant).
        fixed:
            xpos 234 ypos 504
            xysize (706, 56)
            add Solid("#081B2BD8") xysize (706, 56)
            add Solid("#48BBE955") xpos 5 ypos 0 xsize 689 ysize 1
            if _exchange_complete:
                text "✓  FIN DE LA CONVERSATION — CLIQUER POUR FERMER":
                    xalign 0.5 yalign 0.5
                    size 19 color "#7EE6B4"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 1
            else:
                text "CLIQUEZ POUR AFFICHER LE MESSAGE SUIVANT":
                    xalign 0.5 yalign 0.5
                    size 19 color "#A7E9FF"
                    font "fonts/Rajdhani-SemiBold.ttf" kerning 1

label messenger_play(thread_id, contact_id, messages, objective_text="Consulter les messages", notify=True):
    $ _messenger_started = messenger_begin(thread_id, contact_id, messages, objective_text, notify)
    if _messenger_started:
        call screen messenger_objective_gate
    return
