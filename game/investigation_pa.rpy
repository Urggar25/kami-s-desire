# ENQUÊTE À POINTS D'ACTION — interface réutilisable
# Ne se substitue pas au temps libre social ; aucun personnage de temps libre n'est injecté.
default investigation_pa_remaining = 0
default investigation_pa_max = 5
default investigation_pa_day = 0
default investigation_pa_completed = []
default investigation_pa_current_room = "dortoir"
default investigation_pa_selected = ""

init python:
    # Un scénario peut fournir son propre catalogue de salles et d'actions.
    # Chaque action correspond à un label narratif, appelé uniquement après validation.
    def investigation_pa_begin(day, actions=5):
        store.investigation_pa_day = int(day)
        store.investigation_pa_max = int(actions)
        store.investigation_pa_remaining = int(actions)
        store.investigation_pa_completed = []
        store.investigation_pa_selected = ""

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
        room = rooms.get(room_id, {})
        return [actions[k] for k in room.get("actions", [])
                if k in actions and k not in store.investigation_pa_completed]

screen investigation_pa_map(rooms, title="ENQUÊTE — CONCLAVE"):
    modal True
    zorder 50
    add Solid("#06121DEE")
    frame:
        background Solid("#0B1D2DF2")
        xalign 0.5 yalign 0.5
        xsize 1470 ysize 900
        padding (38, 30)
        vbox:
            spacing 19
            hbox:
                spacing 30
                text title size 38 color "#D8F4FF"
                text ("PA : %d / %d" % (investigation_pa_remaining, investigation_pa_max)) size 32 color "#69E0F8" xalign 1.0
            text "Déplacez-vous librement. Seuls les indices et interrogatoires approfondis coûtent 1 PA." size 20 color "#AAC8D8"
            vpgrid:
                cols 3
                spacing 14
                xsize 1410
                ysize 560
                for room_id, room in rooms.items():
                    button:
                        xsize 440 ysize 175
                        background Solid("#133144")
                        hover_background Solid("#245271")
                        action Return(room_id)
                        vbox:
                            xalign 0.5 yalign 0.5 spacing 8
                            text room["title"] size 24 color "#E3F6FF" xalign 0.5
                            text ("%d piste(s) à examiner" % len(room.get("actions", []))) size 17 color "#83C7DE" xalign 0.5
            hbox:
                spacing 30 xalign 0.5
                textbutton "TERMINER L'ENQUÊTE" action Return("finish") text_size 22
                textbutton "DOSSIER D'ENQUÊTE" action Show("investigation_dossier", persistent_access=True) text_size 22
            if investigation_pa_remaining <= 0:
                text "Tous les points d'action ont été dépensés. Vous pouvez consulter votre dossier ou terminer." size 19 color "#F3C778"

screen investigation_pa_room(room_id, rooms, actions):
    modal True
    zorder 50
    $ room = rooms[room_id]
    add room["background"]
    add Solid("#00000055")
    frame:
        background Solid("#071925EF")
        xalign 0.97 yalign 0.50
        xsize 580 ysize 800
        padding (30, 25)
        vbox:
            spacing 16
            text room["title"] size 32 color "#CDEFFF"
            text ("PA RESTANTS : %d / %d" % (investigation_pa_remaining, investigation_pa_max)) size 21 color "#71DEF6"
            text room.get("description", "Observez les lieux.") size 18 color "#B7CCDA"
            null height 12
            for action_id in room.get("actions", []):
                $ action = actions[action_id]
                if action_id in investigation_pa_completed:
                    text ("✓ " + action["title"] + " — examiné") color "#7BACB5" size 19
                elif investigation_pa_remaining > 0:
                    textbutton ("◆ " + action["title"] + "  [1 PA]"):
                        action Return(action_id)
                        text_size 22
                        text_color "#E8F7FF"
                        text_hover_color "#64D7FF"
                else:
                    text ("◆ " + action["title"] + " — PA insuffisants") size 18 color "#8799A5"
            null height 25
            textbutton "REVENIR AU PLAN" action Return("back") text_size 23
            textbutton "CONSULTER LE DOSSIER" action Show("investigation_dossier", persistent_access=True) text_size 20

screen investigation_pa_confirm(action):
    modal True
    zorder 70
    add Solid("#000915CC")
    frame:
        background Solid("#0A2535F5")
        xalign 0.5 yalign 0.5
        xsize 850
        padding (40, 38)
        vbox:
            spacing 22
            text "LANCER CETTE ENQUÊTE ?" size 31 color "#D5F5FF" xalign 0.5
            text action["title"] size 27 color "#FFFFFF" xalign 0.5
            text action["description"] size 22 color "#B9D4E3" xalign 0.5
            text ("Coût : 1 PA  •  Restants : %d / %d" % (investigation_pa_remaining, investigation_pa_max)) size 22 color "#FFD486" xalign 0.5
            hbox:
                spacing 80 xalign 0.5
                textbutton "CONFIRMER — 1 PA" action Return(True) text_size 22
                textbutton "ANNULER" action Return(False) text_size 22
