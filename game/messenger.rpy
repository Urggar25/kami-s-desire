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

    # Portrait recadre pour les DEUX cadres d'en-tete. L'original montre
    # le buste entier : son visage devient minuscule dans un carre de 60px.
    # Le cache evite de decoder les PNG a chaque interaction de l'ecran.
    _messenger_header_portrait_cache = {}

    def messenger_header_portrait(contact_id):
        contact_id = str(contact_id or "")
        if contact_id in _messenger_header_portrait_cache:
            return _messenger_header_portrait_cache[contact_id]

        portrait = messenger_portrait(contact_id)
        if not isinstance(portrait, str):
            _messenger_header_portrait_cache[contact_id] = portrait
            return portrait

        try:
            width, height = renpy.image_size(portrait)
            # Recadrage carre 72 % du petit cote : rapproche le visage
            # sans modifier le cadrage des avatars dans les messages.
            side = max(1, int(min(width, height) * 0.72))
            cx = max(0, (width - side) // 2)
            cy = min(max(0, int(height * 0.035)), max(0, height - side))
            result = im.Crop(portrait, (cx, cy, side, side))
        except Exception:
            result = portrait

        _messenger_header_portrait_cache[contact_id] = result
        return result

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
    # Inclinaison unique des composants, alignee aux traits cyan du PNG.
    # Ne pas incliner individuellement les messages : tous les textes,
    # portraits et bulles partagent CE MEME plan.
    subpixel True
    xanchor 0.5
    yanchor 0.5
    xpos 0.45
    ypos 0.441
    zoom 0.96
    rotate 9.3


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

    # Aucun changement de mecanique : un clic/Entree/Espace revele le suivant.
    key "K_ESCAPE" action Function(renpy.notify, "Consultez tous les messages.")
    key "K_SPACE" action Function(messenger_advance)
    key "K_RETURN" action Function(messenger_advance)
    key "mouseup_1" action Function(messenger_advance)

    add Solid("#01060BCC")
    add "images/ui/tablette/tablette_messagerie.png" fit "contain" xysize (1920, 1080)

    # Repere UNIQUE de la surface inclinee. Les cadres et fonds decoratifs
    # existent deja dans le PNG : ne pas recreer de panneaux par-dessus.
    fixed at messenger_panel_in, messenger_tablet_plane:
        xysize (940, 560)

        # COLONNE GAUCHE : une vraie conversation, les autres cases
        # de l'illustration restent vides et disponibles pour plus tard.
        fixed:
            xpos 0 ypos 0
            xysize (225, 560)

            text "MESSAGERIE":
                xpos 22 ypos 10
                size 24 color "#F2FAFF"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 2

            # Le sous-titre reste au-dessus du trait cyan du PNG.
            text "CANAL PRIVÉ":
                xpos 24 ypos 37
                size 12 color "#7CD9FA"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1

            # Seuls portrait et textes remplissent la carte EXISTANTE.
            fixed:
                xpos 7 ypos 69
                xysize (202, 82)

                # Portrait rapproche et agrandi dans le cadre cyan.
                add Transform(
                    messenger_header_portrait(_contact_id), fit="cover",
                    xysize=(68, 68)
                ) xpos 1 ypos 1

                vbox:
                    xpos 94 ypos 15
                    xsize 114
                    spacing 1

                    text _contact_name:
                        size 21 color "#FFFFFF"
                        font "fonts/Rajdhani-SemiBold.ttf"

                    text ("Lu" if _exchange_complete else "Nouveaux messages"):
                        size 12 color "#9ADCF4"
                        font "fonts/Rajdhani-SemiBold.ttf"
                        xmaximum 120

        # EN-TETE : laisser respirer le portrait ; nom et statut sont a droite.
        fixed:
            xpos 284 ypos 3
            xysize (656, 94)

            # Le cadre du PNG est plus grand que l'ancien portrait 57px.
            # Recadrage visage + remplissage du cadre, sans deborder sur Kael.
            add Transform(
                messenger_header_portrait(_contact_id), fit="cover",
                xysize=(76, 76)
            ) xpos 13 ypos 2

            text _contact_name:
                xpos 160 ypos 19
                size 30 color "#FFFFFF"
                font "fonts/Rajdhani-SemiBold.ttf"

            text "●  CANAL SÉCURISÉ":
                xpos 161 ypos 60
                size 14 color "#60E4A3"
                font "fonts/Rajdhani-SemiBold.ttf"
                kerning 1

        # DISCUSSION : contenu decale a droite et plus bas suivant les fleches,
        # aucun chevauchement entre deux messages, quelle que soit leur taille.
        # La largeur laisse une marge avant la barre de scroll dessinee.
        viewport:
            xpos 307 ypos 164
            xsize 566 ysize 324
            mousewheel True
            draggable False
            yinitial 1.0

            vbox:
                xsize 546
                spacing 11

                # Taille naturelle des bulles et des lignes : aucune hauteur
                # estimée en fonction du nombre de caractères. Une estimation
                # produisait des espaces irréguliers et décalait les portraits.
                for _index, _message in enumerate(_visible_messages):
                    $ _sender = _message.get("sender", _contact_id)
                    $ _from_noam = (_sender == "noam")
                    $ _consecutive = (_index > 0 and _visible_messages[_index - 1].get("sender") == _sender)
                    $ _message_text = _message.get("text", "")

                    if _from_noam:
                        hbox:
                            xalign 1.0
                            spacing 11

                            frame:
                                xmaximum 436
                                padding (14, 10)
                                background Solid("#145D83F0")
                                text _message_text:
                                    size 22 color "#F4FAFF"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    xmaximum 408
                                    line_spacing 2

                            if _consecutive:
                                null width 47 height 47
                            else:
                                add Transform(
                                    messenger_portrait("noam"), fit="cover",
                                    xsize=47, ysize=47
                                )
                    else:
                        hbox:
                            xalign 0.0
                            spacing 11

                            if _consecutive:
                                null width 47 height 47
                            else:
                                add Transform(
                                    messenger_portrait(_sender), fit="cover",
                                    xsize=47, ysize=47
                                )

                            frame:
                                xmaximum 436
                                padding (14, 10)
                                background Solid("#21394FF0")
                                text _message_text:
                                    size 22 color "#F0F6FB"
                                    font "fonts/Rajdhani-SemiBold.ttf"
                                    xmaximum 408
                                    line_spacing 2

        # PIED DE PAGE : indication recentree a droite suivant l'annotation ;
        # pas de faux bandeau noir, de double bordure ou de bouton surajoute.
        fixed:
            xpos 348 ypos 525
            xysize (546, 34)

            if _exchange_complete:
                text "CONVERSATION TERMINÉE — CLIQUER POUR FERMER":
                    xalign 0.5 yalign 0.5
                    size 16 color "#8BE7B7"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 1
            else:
                text "CLIQUER POUR AFFICHER LE MESSAGE SUIVANT":
                    xalign 0.5 yalign 0.5
                    size 16 color "#A7E9FF"
                    font "fonts/Rajdhani-SemiBold.ttf"
                    kerning 1

label messenger_play(thread_id, contact_id, messages, objective_text="Consulter les messages", notify=True):
    $ _messenger_started = messenger_begin(thread_id, contact_id, messages, objective_text, notify)
    if _messenger_started:
        call screen messenger_objective_gate
    return
