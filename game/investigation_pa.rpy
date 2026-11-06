# Exploration d'enquête : les couloirs et les salles servent de seule interface.
# Pas de carte en grille : le joueur clique directement sur les personnes et les points du décor.
default investigation_pa_remaining = 0
default investigation_pa_max = 5
default investigation_pa_day = 0
default investigation_pa_completed = []
default investigation_pa_current_room = "dortoir"
default investigation_pa_selected = ""
default investigation_pa_hover = ""
# PNG des clichés collectés, sauvegardés avec la partie (960 × 540).
default investigation_photo_data = {}

init python:
    def investigation_photo_capture(eid):
        # Capture réelle du rendu Ren'Py, pas une reconstitution de l'indice.
        # La même séquence PNG est affichée lors de la prise et dans le dossier.
        try:
            photo_png = renpy.screenshot_to_bytes((960, 540))
            if photo_png:
                saved = dict(getattr(store, "investigation_photo_data", {}) or {})
                saved[eid] = photo_png
                store.investigation_photo_data = saved
                return True
        except Exception as exc:
            renpy.log("Capture de photo d'enquête impossible : %s" % exc)
        return False

    def investigation_pa_begin(day, actions=5):
        store.investigation_pa_day = int(day)
        store.investigation_pa_max = int(actions)
        store.investigation_pa_remaining = int(actions)
        store.investigation_pa_completed = []
        store.investigation_pa_selected = ""
        store.investigation_pa_hover = ""

    def investigation_pa_can_take(action_id):
        return (store.investigation_pa_remaining > 0
                and action_id not in store.investigation_pa_completed)

    def investigation_pa_spend(action_id):
        if not investigation_pa_can_take(action_id):
            return False
        store.investigation_pa_remaining -= 1
        store.investigation_pa_completed = list(store.investigation_pa_completed) + [action_id]
        return True

    def investigation_pa_actions_for(room_id, rooms, actions):
        return [actions[k] for k in rooms.get(room_id, {}).get("actions", [])
                if k in actions and k not in store.investigation_pa_completed]

    # Les personnages sont de véritables sprites à cliquer, ancrés en bas
    # comme dans les autres scènes point-and-click du jeu.
    INVESTIGATION_PA_INTERLOCUTORS = {
        "iris": "iris", "elen": "elen", "sael": "sael", "julian": "julian",
        "nyra": "nyra", "kael": "kael", "ryn": "ryn", "elias": "elias",
        "limen": "sael"
    }

    # Calques natifs : ces hotspots ont exactement la même silhouette et
    # le même survol que les objets interactifs du Conclave.
    INVESTIGATION_PA_NATIVE_HOTSPOTS = {
        "grille": ("chambre", "images/background/interact/chambre/chambre1/aeration.png"),
        "notes": ("archive", "images/background/interact/archive/archive2/ordinateur.png"),
        "keyper": ("archive", "images/background/interact/archive/archive2/ecran.png"),
        "signal": ("observation", "images/background/interact/observation/observation2/radio.png"),
        "camera": ("observation", "images/background/interact/observation/observation1/ordinateur.png"),
        "console": ("observation", "images/background/interact/observation/observation1/ordinateur.png"),
        "acces": ("maintenance", "images/background/interact/maintenance/maintenance1/etablit.png"),
    }

    def investigation_pa_hotspot(action_id, room_name):
        candidate = INVESTIGATION_PA_NATIVE_HOTSPOTS.get(action_id)
        if candidate and candidate[0] == room_name and renpy.loadable(candidate[1]):
            return candidate[1]
        return None

    def investigation_pa_actor(action_id):
        # J26 route Tomas : identifiant historique « iris » conservé
        # pour les sauvegardes, mais c'est Sael qui assure les soins.
        if store.investigation_pa_day == 26 and action_id == "iris":
            return "sael"
        return INVESTIGATION_PA_INTERLOCUTORS.get(action_id)

    def investigation_pa_room_actions(room_id, rooms, actions):
        return [k for k in rooms.get(room_id, {}).get("actions", [])
                if k in actions]

    # Vraies portes des panoramas existants : même masque de clic et même
    # surbrillance que dans l'exploration normale, sans barre de navigation.
    INVESTIGATION_PA_EXIT_DOORS = {
        "archive": ("archive1", "images/background/interact/archive/archive1/porte.png"),
        "cafeteria": ("cafeteria1", "images/background/interact/cafeteria/cafeteria1/porte.png"),
        "canon": ("canon1", "images/background/interact/canon/canon1/porte_couloir_cafeteria.png"),
        "conclave": ("conclave1", "images/background/interact/conclave/conclave1/porte.png"),
        "chambre": ("chambre2", "images/background/interact/chambre/chambre2/porte_dehors.png"),
        "gymnase": ("gymnase1", "images/background/interact/gymnase/gymnase1/porte_couloir_infirmerie.png"),
        "infirmerie": ("infirmerie1", "images/background/interact/infirmerie/infirmerie1/porte_couloir_infirmerie.png"),
        "maintenance": ("maintenance1", "images/background/interact/maintenance/maintenance1/porte_couloir_maintenance.png"),
        "observation": ("observation1", "images/background/interact/observation/observation1/porte_couloir_cafeteria.png"),
        "repos": ("repos1", "images/background/interact/repos/repos1/porte_couloir_cafeteria.png"),
    }

    def investigation_pa_exit_door(pnc_room, day, room_id):
        if room_id == "dortoir" and day in (26, 27, 28, 29):
            # La chambre d'Elen est un décor unique sans texture de porte.
            return None
        candidate = INVESTIGATION_PA_EXIT_DOORS.get(pnc_room)
        if (candidate and room_scene_stem(pnc_room) == candidate[0]
                and renpy.loadable(candidate[1])):
            return candidate[1]
        return None

# Ce panneau n'est PAS une liste d'actions : il recouvre le décor réel.
# Les hotspots brillants signalent les objets ; les sprites signalent les interlocuteurs.
screen investigation_pa_room(room_id, rooms, actions):
    modal True
    zorder 110
    default hovered_action = None
    $ room = rooms[room_id]
    $ available = investigation_pa_room_actions(room_id, rooms, actions)
    $ pnc_room = "chambre" if room_id == "dortoir" else room_id
    # Réutilise le panorama existant du jeu et ses rotations gauche/droite.
    if investigation_pa_day == 27 and room_id == "dortoir":
        # Décor fixe distinct de la chambre de Noam : Tomas, jour 27.
        add Transform("bg_chambre_tomas", xysize=(1920, 1080))
    elif investigation_pa_day in (26, 28, 29) and room_id == "dortoir":
        # Le flacon doit réellement être visible quand Noam enquête au J26.
        $ elen_room_image = "j26_elen_flacon" if investigation_pa_day == 26 else "j26_elen_vide"
        add Transform(elen_room_image, xysize=(1920, 1080))
    else:
        use room_scene_background(pnc_room, navigation=True)

    # Sortie par les portes physiques des panoramas, comme en jeu normal.
    # La chambre d'Elen (asset fixe sans porte) garde une zone de sortie
    # discrète, à l'écart des bandes gauche/droite de rotation et du flacon.
    $ exit_door = investigation_pa_exit_door(pnc_room, investigation_pa_day, room_id)
    if exit_door:
        imagebutton:
            idle room_interaction_null()
            hover room_interaction_hover_with_overlays(exit_door, pnc_room)
            focus_mask room_interaction_layer(exit_door, pnc_room, "art")
            xpos 0 ypos 0
            hovered SetScreenVariable("hovered_action", "__sortie")
            unhovered SetScreenVariable("hovered_action", None)
            action Return("corridors")
    else:
        button:
            xpos 80 ypos 735 xsize 150 ysize 225
            background None
            hover_background Solid("#79C9DE18")
            hovered SetScreenVariable("hovered_action", "__sortie")
            unhovered SetScreenVariable("hovered_action", None)
            action Return("corridors")
    if hovered_action == "__sortie":
        text "← SORTIR":
            xpos 78 ypos 708
            color "#E2F6FF"
            size 27
            outlines [(2, "#061421", 0, 0)]

    for idx, action_id in enumerate(available):
        $ action_info = actions[action_id]
        $ actor = investigation_pa_actor(action_id)
        $ native_path = investigation_pa_hotspot(action_id, pnc_room)
        $ done = action_id in investigation_pa_completed
        $ enabled = investigation_pa_can_take(action_id)
        if investigation_pa_day == 27 and room_id == "dortoir" and action_id == "grille":
            # La ventilation est située au-dessus du lit, pas sur le calque interactif de Noam.
            button:
                xpos 1220 ypos 95 xsize 240 ysize 150
                background None
                hover_background Solid("#77DDF022")
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        elif investigation_pa_day in (26, 28, 29) and room_id == "dortoir" and action_id == "grille":
            # La plaque créée pour Elen sert à la fois de surbrillance et de masque.
            $ plate = "images/background/interact/chambre_elen/meutre_tomas/plaque.png"
            imagebutton:
                idle Null(width=1920, height=1080)
                hover Transform(plate, xysize=(1920, 1080), matrixcolor=BrightnessMatrix(0.27))
                focus_mask Transform(plate, xysize=(1920, 1080))
                xpos 0 ypos 0
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        elif investigation_pa_day in (26, 28, 29) and room_id == "dortoir" and action_id == "flacon":
            # Zone assez grande pour sélectionner le petit flacon du meuble.
            button:
                xpos 180 ypos 500 xsize 170 ysize 125
                background None
                hover_background Solid("#77DDF022")
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        elif investigation_pa_day == 27 and room_id == "dortoir" and action_id == "carnet":
            # Bureau à gauche : les documents et le carnet de Tomas.
            button:
                xpos 90 ypos 490 xsize 490 ysize 395
                background None
                hover_background Solid("#77DDF022")
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        elif native_path:
            imagebutton:
                idle room_interaction_null()
                hover room_interaction_hover_with_overlays(native_path, pnc_room)
                focus_mask room_interaction_layer(native_path, pnc_room, "art")
                xpos 0
                ypos 0
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        elif actor:
            # Le sprite reste sur le sol, aucun panneau de sélection de personnage.
            imagebutton:
                idle Transform(character_image(actor, "neutre"), zoom=1.00)
                hover Transform(character_image(actor, "neutre"), zoom=1.00, matrixcolor=BrightnessMatrix(0.18))
                focus_mask True
                xalign (0.28 if idx % 2 == 0 else 0.72)
                yalign 1.00
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
        else:
            # Zone cliquable dans le décor et petit éclat au survol.
            button:
                xpos (int(config.screen_width * (0.30 if idx % 2 == 0 else 0.72)))
                ypos (int(config.screen_height * (0.42 if idx % 2 == 0 else 0.60)))
                xsize 120 ysize 110
                background Solid("#75DEF022")
                hover_background Solid("#75DEF066")
                sensitive enabled
                hovered SetScreenVariable("hovered_action", action_id)
                unhovered SetScreenVariable("hovered_action", None)
                action Return(action_id)
                text ("✓" if done else "✦"):
                    xalign 0.5 yalign 0.5
                    color ("#72BAA5" if done else "#DAF7FF")
                    size 42

    # Barre minimaliste : aucun pavé de choix ou de destination.
    frame:
        xalign 0.02 yalign 0.04
        background Solid("#081722C9")
        padding (16, 12)
        vbox:
            spacing 3
            text room["title"] color "#E1F6FF" size 27
            text ("PA : %d / %d" % (investigation_pa_remaining, investigation_pa_max)) color "#78DFF5" size 22
            if hovered_action and hovered_action in actions:
                text actions[hovered_action]["title"] color "#FFFFFF" size 20
            elif investigation_pa_remaining <= 0:
                text "Plus de PA : retournez dans le couloir." color "#E7CBA1" size 17
            else:
                text "Survolez un personnage ou un objet pour enquêter." color "#A3BFCB" size 17

# Le choix de dépense est désormais un menu Ren'Py natif, piloté directement
# par les scénarios J26-J29. L'ancien screen n'est conservé que pour les
# sauvegardes susceptibles d'y faire référence.
screen investigation_pa_confirm(action):
    modal True
    zorder 120
    vbox:
        xalign 0.5 yalign 0.82
        spacing 14
        textbutton "ENQUÊTER — 1 PA" action Return(True)
        textbutton "ANNULER" action Return(False)

# Confirmation intégrée au système de choix standard du visual novel.
# Le décor exact de la salle reste derrière le menu, sans fenêtre modale bleue.
label INVESTIGATION_PA_CHOICE(action, room_id):
    if investigation_pa_day == 27 and room_id == "dortoir":
        scene bg_chambre_tomas at adaptive_fullscreen with None
    elif investigation_pa_day in (26, 28, 29) and room_id == "dortoir":
        $ _investigation_choice_bg = "j26_elen_flacon" if investigation_pa_day == 26 else "j26_elen_vide"
        scene expression _investigation_choice_bg at adaptive_fullscreen with None
    else:
        $ _investigation_choice_bg = room_scene_displayable("chambre" if room_id == "dortoir" else room_id)
        scene expression _investigation_choice_bg at cover_screen with None
    $ _investigation_choice_title = action["title"]
    $ _investigation_choice_remaining = investigation_pa_remaining
    menu:
        "[_investigation_choice_title] — dépenser 1 PA ? ([_investigation_choice_remaining] restants)"
        "Enquêter — 1 PA":
            return True
        "Annuler":
            return False

# Présentation fugace de la même source photographique que le dossier.
# Les entrées sans illustration spécifique utilisent la photo du lieu d'origine.
screen investigation_evidence_photo_preview(eid):
    zorder 135
    add Solid("#FFFFFFD0")
    frame:
        xalign 0.5 yalign 0.5
        xsize 1000 ysize 745
        background Solid("#F4F1E8")
        padding (18, 16)
        vbox:
            spacing 12
            add investigation_evidence_image(eid) xsize 960 ysize 540
            text INVESTIGATION_ENTRIES[eid]["title"] color "#1E2934" size 30 xalign 0.5
            text "PHOTO ENREGISTRÉE — DOSSIER D'ENQUÊTE" color "#40556B" size 21 xalign 0.5

label investigation_evidence_photo_take(eid):
    # Cache l'interface avant de photographier le rendu courant du jeu.
    # La capture PNG reste dans la sauvegarde : le dossier réaffiche les mêmes pixels.
    window hide
    with None
    $ renpy.pause(0.08, hard=True)
    $ investigation_photo_capture(eid)
    $ investigation_add(eid, notify=False)
    play sound "audio/sfx_photo.mp3"
    show screen investigation_evidence_photo_preview(eid)
    pause 1.0
    hide screen investigation_evidence_photo_preview
    window show
    return


# Jour 26 — photographies prises PAR le joueur sur les vraies textures.
# Les trois PNG sont des calques transparents à la même résolution que le BG.
# On assemble une seule fois les images pour garder leurs coordonnées alignées.
image j26_elen_corps = Composite(
    (1536, 1024),
    (0, 0), "images/background/scene/bg_chambre_elen.png",
    (0, 0), "images/background/interact/chambre_elen/meutre_tomas/plaque.png",
    (0, 0), "images/background/interact/chambre_elen/meutre_tomas/corps_tomas.png")
image j26_elen_vide = Composite(
    (1536, 1024),
    (0, 0), "images/background/scene/bg_chambre_elen.png",
    (0, 0), "images/background/interact/chambre_elen/meutre_tomas/plaque.png")
image j26_elen_flacon = Composite(
    (1536, 1024),
    (0, 0), "images/background/scene/bg_chambre_elen.png",
    (0, 0), "images/background/interact/chambre_elen/meutre_tomas/plaque.png",
    (0, 0), "images/background/interact/chambre_elen/meutre_tomas/medicament.png")


# J26 : même cadre Polaroid animé que le J25, mais affiché sur une
# interaction séparée une fois le véritable PNG écrit dans le dossier.
screen j26_photo_saved_preview(eid):
    modal True
    zorder 220
    add Solid("#03070DBB")
    frame at _j25_print_in:
        align (0.5, 0.5)
        xsize 1156 ysize 724
        padding (18, 18)
        background Solid("#ECE8DC")
        vbox:
            spacing 18
            add investigation_evidence_image(eid) xsize 1120 ysize 630
            text _("PHOTO ENREGISTRÉE") xalign 0.5 size 24 color "#25333B" font "fonts/Rajdhani-SemiBold.ttf" kerning 3
    timer 1.0 action Return()

# Mécanique commune à toutes les preuves photographiques (J26-J30).
# Viseur / cadrage du J25 ; capture réelle puis Polaroid animé du J25.
label investigation_take_manual_photo(eid, source, center=(0.5, 0.5), zoom=2.2):
    window hide
    with None
    $ _investigation_camera = _J25View(zoom=zoom, center=center, source=source)
    show expression _investigation_camera as investigation_camera_view onlayer master
    call screen _j25_photo_screen(_investigation_camera, evidence_id=eid)
    hide investigation_camera_view onlayer master
    $ _investigation_camera = None
    if investigation_photo_data.get(eid):
        call screen j26_photo_saved_preview(eid)
        $ investigation_add(eid, notify=False)
    else:
        window show
        "La photo n'a pas été enregistrée. Je dois recommencer."
        call investigation_take_manual_photo(eid, source, center, zoom) from _call_investigation_photo_retry
    window show
    return

# Ancien point d'entrée maintenu pour les sauvegardes du jour 26.
label j26_photograph(eid, source, center, zoom=2.2):
    call investigation_take_manual_photo(eid, source, center, zoom) from _call_j26_photo_shared_engine
    return

# Compatibilité avec les sauvegardes et les rechargements Ren'Py faits
# pendant l'ancienne caméra J26. Les objets picklés y référencent cette classe.
# Les nouvelles photographies utilisent exclusivement _J25View/_j25_photo_screen.
init python:
    import math as _j26_math

    def _j26_limit_center(value, zoom):
        margin = 0.5 / zoom
        return max(margin, min(1.0 - margin, value))

    class _J26PhotoView(renpy.Displayable):
        """Caméra cadrant l'image entière, puis zoom progressif vers un indice."""
        def __init__(self, source, **kwargs):
            super(_J26PhotoView, self).__init__(**kwargs)
            self.child = Transform(source, xysize=(1920, 1080))
            self.zoom = 1.0
            self.center = (0.5, 0.5)
            self.motion = None
            self.draw_st = 0.0

        def render(self, width, height, st, at):
            self.draw_st = st
            shake_x = shake_y = 0.0
            if self.motion is not None:
                start, z0, c0, z1, c1 = self.motion
                elapsed = max(0.0, st - start)
                lead = 0.12
                if elapsed < lead:
                    shake_x = _j26_math.sin(elapsed * 150) * 4.0 * (1 - elapsed / lead)
                    shake_y = _j26_math.sin(elapsed * 125) * 2.5 * (1 - elapsed / lead)
                t = max(0.0, min(1.0, (elapsed - lead) / 0.58))
                eased = t * t * (3 - 2 * t)
                self.zoom = z0 + (z1 - z0) * eased
                self.center = tuple(a + (b - a) * eased for a, b in zip(c0, c1))
                if t < 1.0:
                    renpy.redraw(self, 0)
                else:
                    self.motion = None
            cx = _j26_limit_center(self.center[0], self.zoom)
            cy = _j26_limit_center(self.center[1], self.zoom)
            scaled = renpy.render(Transform(self.child, zoom=self.zoom), 1920, 1080, st, at)
            result = renpy.Render(1920, 1080)
            result.blit(scaled, (int(960 - cx * 1920 * self.zoom + shake_x),
                                 int(540 - cy * 1080 * self.zoom + shake_y)))
            return result

        def visit(self):
            return [self.child]


# Anciennes sauvegardes : la screen appelée par un rollback/hot reload peut
# encore être active. La rediriger vers le minijeu J25, sans forcer un nouveau départ.
screen j26_photo_manual(eid, view, center, zoom):
    default restored_view = _J25View(
        zoom=getattr(view, "zoom", zoom),
        center=getattr(view, "center", center),
        source=getattr(view, "child", "j26_elen_corps"))
    use _j25_photo_screen(restored_view, evidence_id=eid)
