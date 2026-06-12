# ============================================================
# MINI-JEU JOUR 11 - LES 7 JOURS OUBLIES
# Objectif : relier les indices dans la tête de Noam.
#
# Appel :
#   call _11_0_1_2_MINIJEU_7JOURS
#   $ resultat = _return
# ============================================================

default j11012_mind_selected = []
default j11012_mind_solved_edges = []
default j11012_mind_wrong_edge = None
default j11012_mind_feedback = "Clique deux indices, puis Relier."
default j11012_mind_flash = 0.0
default j11012_mind_done = False
default j11012_mind_success = False

init python:
    J11012_MIND_TICK = 0.05
    J11012_MIND_TARGET = 3

    j11012_mind_nodes = {
        "vol_j8": {
            "label": "Vol chez Kael\nAutour du Jour 8 ?",
            "x": 190,
            "y": 250,
        },
        "blocage_7j": {
            "label": "Images bloquées\npendant 7 jours",
            "x": 1280,
            "y": 250,
        },
        "accessible_j15": {
            "label": "Images accessibles\nseulement au Jour 15",
            "x": 190,
            "y": 640,
        },
        "couloir_conclave": {
            "label": "Dans les couloirs\ndu Conclave",
            "x": 1280,
            "y": 640,
        },
        "absence_brouilleur": {
            "label": "Absence de\nBrouilleurs",
            "x": 750,
            "y": 730,
        },
        "brouilleur_actif": {
            "label": "Si un brouilleur\nest activé",
            "x": 750,
            "y": 120,
        },
    }

    j11012_mind_correct_edges = {
        tuple(sorted(("vol_j8", "accessible_j15"))): "Oui. Si le vol est au Jour 8, 8+7=15, non ? Donc on pourra voir les images lors du quinzième jour.",
        tuple(sorted(("blocage_7j", "brouilleur_actif"))): "C'est ça. Un brouilleur bloque la vision des images pendant une semaine.",
        tuple(sorted(("couloir_conclave", "absence_brouilleur"))): "Mais dans les pièces du Conclave... Il n'y a pas de brouilleurs... Si ?",
    }

    j11012_mind_wrong_lines = [
        "Non... ça ne colle pas.",
        "Ma tête s'emballe. Ce lien ne tient pas.",
        "Pas comme ça. Je force le raisonnement.",
        "Non. Il manque une cause claire.",
    ]

    def j11012_mind_reset():
        store.j11012_mind_selected = []
        store.j11012_mind_solved_edges = []
        store.j11012_mind_wrong_edge = None
        store.j11012_mind_feedback = "Clique deux indices, puis Relier."
        store.j11012_mind_flash = 0.0
        store.j11012_mind_done = False
        store.j11012_mind_success = False

    def j11012_mind_center(node_id):
        node = j11012_mind_nodes[node_id]
        return (node["x"] + 210, node["y"] + 58)

    def j11012_mind_select(node_id):
        if store.j11012_mind_done:
            return

        if node_id in store.j11012_mind_selected:
            store.j11012_mind_selected.remove(node_id)
            store.j11012_mind_feedback = "Je repose l'indice. Deux points, pas plus."
            return

        if len(store.j11012_mind_selected) >= 2:
            store.j11012_mind_selected = [node_id]
            store.j11012_mind_feedback = "Je repars de cet indice."
        else:
            store.j11012_mind_selected.append(node_id)
            if len(store.j11012_mind_selected) == 1:
                store.j11012_mind_feedback = "Un point d'ancrage. Il me faut son écho."
            else:
                store.j11012_mind_feedback = "Deux indices. Maintenant, est-ce que le lien tient ?"

    def j11012_mind_validate():
        if store.j11012_mind_done:
            return

        if len(store.j11012_mind_selected) != 2:
            store.j11012_mind_feedback = "Deux indices. Pas un de plus, pas un de moins."
            store.j11012_mind_flash = 0.30
            return

        edge = tuple(sorted(store.j11012_mind_selected))
        if edge in store.j11012_mind_solved_edges:
            store.j11012_mind_feedback = "Je l'ai déjà fixé dans ma tête."
            store.j11012_mind_selected = []
            return

        if edge in j11012_mind_correct_edges:
            store.j11012_mind_solved_edges.append(edge)
            store.j11012_mind_feedback = j11012_mind_correct_edges[edge]
            store.j11012_mind_wrong_edge = None
            store.j11012_mind_selected = []
            if len(store.j11012_mind_solved_edges) >= J11012_MIND_TARGET:
                store.j11012_mind_done = True
                store.j11012_mind_success = True
                store.j11012_mind_feedback = "Tout s'aligne. Les sept jours ne sont pas une limite : c'est une arme."
        else:
            store.j11012_mind_wrong_edge = edge
            store.j11012_mind_feedback = renpy.random.choice(j11012_mind_wrong_lines)
            store.j11012_mind_flash = 0.55
            store.j11012_mind_selected = []

    def j11012_mind_tick():
        if store.j11012_mind_flash > 0.0:
            store.j11012_mind_flash = max(0.0, store.j11012_mind_flash - J11012_MIND_TICK)
            if store.j11012_mind_flash <= 0.0:
                store.j11012_mind_wrong_edge = None

    class J11012MindMapLines(renpy.Displayable):
        def __init__(self, **kwargs):
            super(J11012MindMapLines, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            render = renpy.Render(1920, 1080)
            canvas = render.canvas()

            def draw_edge(edge, color, width_line):
                a, b = edge
                canvas.line(color, j11012_mind_center(a), j11012_mind_center(b), width_line)

            for edge in store.j11012_mind_solved_edges:
                draw_edge(edge, "#58ff9a", 5)
                draw_edge(edge, "#dfffea", 2)

            if len(store.j11012_mind_selected) == 2:
                draw_edge(tuple(store.j11012_mind_selected), "#8defff", 3)

            if store.j11012_mind_wrong_edge:
                draw_edge(store.j11012_mind_wrong_edge, "#ff416d", 6)

            return render


transform j11012_mind_bg_pulse:
    alpha 0.88
    linear 1.25 alpha 1.0
    linear 1.25 alpha 0.88
    repeat

transform j11012_mind_core_pulse:
    zoom 1.0 alpha 0.94
    linear 0.9 zoom 1.025 alpha 1.0
    linear 0.9 zoom 1.0 alpha 0.94
    repeat

transform j11012_mind_wrong_shake:
    xoffset 0
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset -5
    linear 0.04 xoffset 5
    linear 0.04 xoffset 0


screen j11012_7jours_mind_map():

    modal True
    zorder 280

    timer J11012_MIND_TICK repeat True action Function(j11012_mind_tick)

    add "gui/day11/7jours/mind_bg.png" at j11012_mind_bg_pulse
    add "gui/day11/7jours/vignette_pulse.png" at j11012_mind_bg_pulse

    if j11012_mind_flash > 0.0:
        add "gui/day11/7jours/headache_flash.png" at j11012_mind_wrong_shake

    add J11012MindMapLines()

    frame:
        xalign 0.5
        yalign 0.035
        xsize 1040
        ysize 76
        background Solid("#05101cdd")
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 0
            text "LES 7 JOURS OUBLIÉS":
                xalign 0.5
                size 34
                color "#d9fbff"
                bold True
            text "Relie les indices qui forment une chaîne logique dans la tête de Noam.":
                xalign 0.5
                size 18
                color "#9cc9d6"

    add "gui/day11/7jours/node_core.png" xpos 710 ypos 395 at j11012_mind_core_pulse
    text "Brouilleur =\nFiltre de 7 jours":
        xpos 790
        ypos 442
        xsize 340
        text_align 0.5
        size 32
        color "#f1fdff"
        bold True

    for node_id, node in j11012_mind_nodes.items():
        $ solved = any(node_id in edge for edge in j11012_mind_solved_edges)
        $ selected = node_id in j11012_mind_selected
        $ node_bg = "gui/day11/7jours/node_solved.png" if solved else "gui/day11/7jours/node_selected.png" if selected else "gui/day11/7jours/node_idle.png"
        button:
            xpos node["x"]
            ypos node["y"]
            xsize 420
            ysize 116
            background node_bg
            hover_background "gui/day11/7jours/node_selected.png"
            action Function(j11012_mind_select, node_id)
            text node["label"]:
                xalign 0.5
                yalign 0.5
                xmaximum 350
                text_align 0.5
                size 25
                color ("#effcff" if not solved else "#c8ffd9")
                bold (selected or solved)

    frame:
        xalign 0.5
        yalign 0.925
        xsize 1320
        ysize 132
        background Solid("#04101ddd")
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 34
            vbox:
                yalign 0.5
                spacing 8
                text "CHAÎNES [len(j11012_mind_solved_edges)]/[J11012_MIND_TARGET]":
                    size 24
                    color "#7df9ff"
                    bold True
                text "[j11012_mind_feedback]":
                    xmaximum 880
                    size 26
                    color "#ffffff"
            button:
                yalign 0.5
                xsize 260
                ysize 74
                background "gui/day11/7jours/link_button_idle.png"
                hover_background "gui/day11/7jours/link_button_hover.png"
                action Function(j11012_mind_validate)
                text "Relier":
                    xalign 0.5
                    yalign 0.5
                    size 30
                    color "#f0feff"
                    bold True

    if j11012_mind_done:
        timer 0.8 action Return(j11012_mind_success)


label _11_0_1_2_MINIJEU_7JOURS:

    scene black with dissolve
    pause 0.3

    think "Sept jours."
    think "Pas une panne. Pas une lenteur technique."
    think "Un filtre. Un trou placé exactement entre ce qui arrive et ce que Kami peut prouver."

    $ j11012_mind_reset()
    $ _j11012_result = renpy.call_screen("j11012_7jours_mind_map")

    scene bg_chambre at adaptive_fullscreen with dissolve

    think "Là, tout s'éclaire."
    think "Le vol chez Kael a eu lieu au Jour 8. Avec sept jours de brouillage, les images ne deviendont lisibles qu'au Jour 15."

    return _j11012_result
