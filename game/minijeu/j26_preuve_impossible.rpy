# J26 - La preuve impossible. Interface d'enquete sepia / technique.
# Le joueur ordonne quatre indices ; l'ordre des cartes est deliberement melange.
default j26_preuve_success = False

init -1 python:
    J26_PREUVE_ORDER = ("premiere", "tissu", "temoin", "photo")
    J26_PREUVE_CARDS = {
        "premiere": ("PREMIERE DECOUVERTE", "Noam apercoit deja un corps.", "gui/day26/first_discovery.svg"),
        "tissu": ("MORCEAU DE TISSU", "Le fil qui ramene au conduit.", "gui/day26/fabric.svg"),
        "temoin": ("TEMOIGNAGE D'IRIS", "Iris examine la cachette.", "gui/day26/witness.svg"),
        "photo": ("LA PHOTOGRAPHIE", "Le corps est photographie.", "bg_cg040"),
    }
    # Les identifiants ne contiennent aucun indice de position.
    J26_PREUVE_PRESENTATION = ("photo", "temoin", "premiere", "tissu")

transform j26_evidence_pop:
    alpha 0.0
    yoffset 18
    ease 0.22 alpha 1.0 yoffset 0

screen j26_preuve_screen():
    modal True
    zorder 200
    default selection = []
    default error = False

    add Solid("#03080fdc")

    frame:
        xalign 0.5 yalign 0.5
        xsize 1660 ysize 892
        padding (0, 0)
        background Solid("#071522f9")

        fixed:
            xysize (1660, 892)
            add Solid("#142c3c") xpos 0 ypos 0 xysize (1660, 102)
            add Solid("#58b5ca") xpos 0 ypos 99 xysize (1660, 3)
            text "◈   CONCLAVE / ENQUETE" xpos 43 ypos 17 size 19 color "#74bfd0" bold True
            text "LA PREUVE IMPOSSIBLE" xpos 43 ypos 42 size 41 bold True color "#f4eee4"
            text "DOSSIER 26   /   RECONSTITUTION DES FAITS" xpos 1110 ypos 53 size 18 color "#a7bdc6"
            text "Tomas conteste la photo. Construisez une chronologie qui explique votre decouverte." xpos 48 ypos 117 size 22 color "#c3d1d6"

            # Zone des quatre preuves, traitées comme des pieces d'archive.
            add Solid("#0b2030") xpos 35 ypos 168 xysize (829, 610)
            add Solid("#274b5c") xpos 35 ypos 168 xysize (829, 48)
            text "  01    ELEMENTS DISPONIBLES" xpos 57 ypos 175 size 23 bold True color "#e9c991"

            for index, key in enumerate(J26_PREUVE_PRESENTATION):
                $ col = index % 2
                $ row = index // 2
                $ cx = 55 + col * 399
                $ cy = 237 + row * 262
                $ title, summary, art = J26_PREUVE_CARDS[key]
                button:
                    xpos cx ypos cy
                    xsize 375 ysize 244
                    background Solid("#d9c49e" if key not in selection else "#816f57")
                    hover_background Solid("#f2dfb9")
                    sensitive key not in selection
                    action [SetScreenVariable("selection", selection + [key]), SetScreenVariable("error", False)]
                    fixed:
                        xfill True yfill True
                        add Solid("#f2e5c9") xpos 8 ypos 8 xysize (359, 180)
                        add Transform(art, xysize=(353, 175)) xpos 11 ypos 11
                        add Solid("#1b3543") xpos 8 ypos 189 xysize (359, 47)
                        text title xpos 17 ypos 195 size 20 bold True color "#f2e6cb"
                        text summary xpos 17 ypos 219 size 14 color "#c9d9dd"
                        if key in selection:
                            add Solid("#0b1b28cc") xpos 8 ypos 8 xysize (359, 180)
                            text "AJOUTE AU DOSSIER" xalign 0.5 ypos 84 size 22 color "#e8c58d" bold True

            # Frise chronologique à droite.
            add Solid("#102637") xpos 884 ypos 168 xysize (744, 610)
            add Solid("#274b5c") xpos 884 ypos 168 xysize (744, 48)
            text "  02    CHRONOLOGIE" xpos 907 ypos 175 size 23 bold True color "#e9c991"
            text "[len(selection)] / 4 ELEMENTS PLACES" xpos 1379 ypos 181 size 17 color "#9cbdcb"
            add Solid("#4b7e8f") xpos 942 ypos 420 xysize (628, 3)
            for i in range(4):
                $ key = selection[i] if i < len(selection) else None
                $ sx = 914 + i * 176
                add Solid("#223c4d") xpos sx ypos 277 xysize (164, 280)
                add Solid("#527c90") xpos sx ypos 277 xysize (164, 2)
                text "%02d" % (i+1) xpos sx+11 ypos 287 size 23 bold True color "#eac991"
                if key:
                    $ title, summary, art = J26_PREUVE_CARDS[key]
                    add Solid("#dfc9a2") xpos sx+10 ypos 328 xysize (144, 150)
                    add Transform(art, xysize=(138, 144)) xpos sx+13 ypos 331
                    text title xpos sx+9 ypos 496 xsize 150 size 16 color "#f2ede4" bold True text_align 0.5
                else:
                    text "?" xpos sx+68 ypos 362 size 64 color "#4c6d7e"
                    text "ETAPE [i+1]" xpos sx+21 ypos 499 size 17 color "#819faa"

            if error:
                add Solid("#68342fb5") xpos 914 ypos 597 xysize (686, 62)
                text "L'ordre ne correspond pas aux faits. Reprenez les indices." xpos 931 ypos 614 size 20 color "#f7d6bf"
            elif len(selection) == 4:
                text "Dossier complet. Vous pouvez presenter votre demonstration." xpos 925 ypos 614 size 19 color "#c6e4dd"
            else:
                text "Choisissez les indices dans l'ordre ou les faits se sont produits." xpos 925 ypos 614 size 19 color "#9eb7c1"

            # Barre inferieure reserves aux commandes (plus aucun debordement).
            add Solid("#162e40") xpos 35 ypos 797 xysize (1593, 72)
            textbutton "EFFACER":
                xpos 56 ypos 809 xsize 174 ysize 48
                background Solid("#2b4557") hover_background Solid("#39647b")
                text_size 20 text_color "#f1e7d7"
                action [SetScreenVariable("selection", []), SetScreenVariable("error", False)]
            textbutton "REVENIR":
                xpos 245 ypos 809 xsize 175 ysize 48
                background Solid("#2b4557") hover_background Solid("#39647b")
                text_size 20 text_color "#f1e7d7"
                sensitive len(selection) > 0
                action [SetScreenVariable("selection", selection[:-1]), SetScreenVariable("error", False)]
            textbutton "PASSER":
                xpos 1052 ypos 809 xsize 170 ysize 48
                background Solid("#243746") hover_background Solid("#365469")
                text_size 19 text_color "#a9bec8"
                action Return(False)
            textbutton "VALIDER LA CHRONOLOGIE":
                xpos 1244 ypos 809 xsize 355 ysize 48
                background Solid("#d9b77d") hover_background Solid("#f0cd91")
                text_size 19 text_color "#142432"
                sensitive len(selection) == 4
                action If(tuple(selection) == J26_PREUVE_ORDER, Return(True), SetScreenVariable("error", True))

label j26_preuve_impossible:
    call screen j26_preuve_screen
    $ j26_preuve_success = bool(_return)
    return
