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
        return INVESTIGATION_PA_INTERLOCUTORS.get(action_id)

    def investigation_pa_room_actions(room_id, rooms, actions):
        return [k for k in rooms.get(room_id, {}).get("actions", [])
                if k in actions]

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
    use room_scene_background(pnc_room, navigation=True)

    for idx, action_id in enumerate(available):
        $ action_info = actions[action_id]
        $ actor = investigation_pa_actor(action_id)
        $ native_path = investigation_pa_hotspot(action_id, pnc_room)
        $ done = action_id in investigation_pa_completed
        $ enabled = investigation_pa_can_take(action_id)
        if native_path:
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

    hbox:
        spacing 16
        xalign 0.5 yalign 0.98
        textbutton "← COULOIR" action Return("corridors") text_size 22
        textbutton "DOSSIER" action Show("investigation_dossier", persistent_access=True) text_size 22
        textbutton "FIN DE L'ENQUÊTE" action Return("finish") text_size 22

# Seule modalité de confirmation ; l'interaction elle-même se fait sur le décor.
screen investigation_pa_confirm(action):
    modal True
    zorder 120
    add Solid("#000915B8")
    frame:
        background Solid("#0A2535F2")
        xalign 0.5 yalign 0.5
        xsize 810
        padding (34, 30)
        vbox:
            spacing 18
            text action["title"] size 30 color "#D5F5FF" xalign 0.5
            text action["description"] size 21 color "#B9D4E3" xalign 0.5
            text ("Coût : 1 PA  •  Restants : %d" % investigation_pa_remaining) size 20 color "#FFD486" xalign 0.5
            hbox:
                spacing 60 xalign 0.5
                textbutton "ENQUÊTER — 1 PA" action Return(True) text_size 23
                textbutton "ANNULER" action Return(False) text_size 23

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

    def _j26_photo_focus(view, center, zoom):
        view.motion = (getattr(view, "draw_st", 0.0), view.zoom,
                       view.center, zoom, center)
        renpy.redraw(view, 0)

screen j26_photo_manual(eid, view, center, zoom):
    modal True
    zorder 220
    default phase = "intro"

    # Le rendu exact de cette caméra sera sauvegardé (960x540) dans le dossier.
    add view

    if phase == "intro":
        timer 0.12 action Function(_j26_photo_focus, view, center, zoom)
        timer 0.86 action SetScreenVariable("phase", "camera")

    if phase in ("intro", "camera"):
        # Réticule et angles dessinés en Ren'Py : aucun nouvel asset.
        for cx, cy, sx, sy in ((180, 165, 1, 1), (1740, 165, -1, 1),
                               (180, 865, 1, -1), (1740, 865, -1, -1)):
            add Solid("#DDF6F4CC") xpos (cx if sx > 0 else cx - 66) ypos cy xsize 66 ysize 3
            add Solid("#DDF6F4CC") xpos cx ypos (cy if sy > 0 else cy - 66) xsize 3 ysize 66
        add Solid("#EAF9F5B0") xpos 939 ypos 540 xsize 42 ysize 2
        add Solid("#EAF9F5B0") xpos 960 ypos 519 xsize 2 ysize 42
        frame:
            xalign 0.5 ypos 25
            background Solid("#091721DD")
            padding (24, 12)
            text "TABLETTE — PRISE DE VUE" color "#E7F7FF" size 29
        if phase == "camera":
            key "K_SPACE" action SetScreenVariable("phase", "capture")
            key "K_RETURN" action SetScreenVariable("phase", "capture")
            textbutton "PRENDRE LA PHOTO  [ESPACE / ENTRÉE]":
                xalign 0.5 yalign 0.95
                text_size 28
                action SetScreenVariable("phase", "capture")
        else:
            text "Cadrage de l'indice…" xalign 0.5 yalign 0.94 size 24 color "#E7F7FF"

    elif phase == "capture":
        # Une interaction entière sans HUD avant screenshot_to_bytes.
        # Contrairement à l'ancienne fonction, aucune photo n'est automatique.
        timer 0.16 action [Function(investigation_photo_capture, eid),
                           SetScreenVariable("phase", "flash")]

    elif phase == "flash":
        add Solid("#FFFFFF") at _j26_photo_flash
        timer 0.16 action SetScreenVariable("phase", "preview")

    elif phase == "preview":
        add Solid("#020A10BB")
        frame:
            xalign 0.5 yalign 0.5
            background Solid("#EEEAE0")
            padding (18, 18)
            vbox:
                spacing 14
                add investigation_evidence_image(eid) xsize 960 ysize 540
                text "PHOTO ENREGISTRÉE" color "#263644" size 28 xalign 0.5
        timer 1.0 action Return(True)

transform _j26_photo_flash:
    alpha 1.0
    linear 0.15 alpha 0.0

label j26_photograph(eid, source, center, zoom=2.2):
    # Le clic de déclenchement est obligatoire pour continuer le scénario.
    window hide
    with None
    $ _j26_view = _J26PhotoView(source)
    call screen j26_photo_manual(eid, _j26_view, center, zoom)
    $ investigation_add(eid, notify=False)
    window show
    return
