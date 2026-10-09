# Jour 26 - Mini-jeu de transfert photographique, Conclave OS.
# Le drag&drop utilise le systeme natif Ren'Py, sans ressources externes.
# Le fichier affiche la vraie CG de l'enquete de Noam.
init -1 python:
    def j26_photo_transfer_dropped(drags, drop):
        if drop is not None and drop.drag_name == "j26_projection_folder":
            return True
        return None

transform j26_projection_appear:
    alpha 0.0
    zoom 0.965
    ease 0.42 alpha 1.0 zoom 1.0

screen j26_photo_transfer():
    modal True
    zorder 200
    add Solid("#040b13df")

    frame:
        xalign 0.5 yalign 0.5
        xsize 1650 ysize 880
        padding (0, 0)
        background Solid("#081826f9")

        fixed:
            xysize (1650, 880)
            add Solid("#153046") xpos 0 ypos 0 xysize (1650, 70)
            add Solid("#55aec5") xpos 0 ypos 68 xysize (1650, 2)
            text "◈  CONCLAVE OS" xpos 30 ypos 16 color "#e9edf0" size 31 bold True
            text "SESSION DE NOAM / TERMINAL CONNECTE" xpos 1138 ypos 24 color "#8cb6c5" size 18

            # Deux fenetres OS distinctes, avec barre d'outils et arborescence.
            add Solid("#10283b") xpos 24 ypos 92 xysize (782, 667)
            add Solid("#10283b") xpos 842 ypos 92 xysize (782, 667)
            add Solid("#24465c") xpos 24 ypos 92 xysize (782, 48)
            add Solid("#24465c") xpos 842 ypos 92 xysize (782, 48)
            text "TABLETTE DE NOAM" xpos 49 ypos 102 size 25 color "#f2eadb" bold True
            text "TERMINAL DU CONCLAVE" xpos 866 ypos 102 size 25 color "#f2eadb" bold True

            # Breadcrumbs.
            add Solid("#081a2a") xpos 39 ypos 156 xysize (752, 42)
            add Solid("#081a2a") xpos 857 ypos 156 xysize (752, 42)
            text "Appareil  /  Photos  /  Enquete" xpos 62 ypos 166 size 20 color "#a7c2cb"
            text "Ce PC  /  Affichage  /  Projection" xpos 882 ypos 166 size 20 color "#a7c2cb"

            # Panneau de navigation gauche.
            add Solid("#0c1c2c") xpos 39 ypos 211 xysize (195, 522)
            add Solid("#0c1c2c") xpos 857 ypos 211 xysize (195, 522)
            text "EMPLACEMENTS" xpos 55 ypos 232 size 16 color "#829eac"
            text "▸  Stockage" xpos 57 ypos 282 size 21 color "#aec6cf"
            text "▸  Photos" xpos 57 ypos 325 size 21 color "#aec6cf"
            add Solid("#25516a") xpos 48 ypos 367 xysize (180, 43)
            text "▸  Enquete" xpos 57 ypos 375 size 22 bold True color "#c7eef4"
            text "▸  Archives" xpos 57 ypos 430 size 21 color "#829eac"
            text "EMPLACEMENTS" xpos 874 ypos 232 size 16 color "#829eac"
            text "▸  Archives" xpos 874 ypos 282 size 21 color "#aec6cf"
            add Solid("#25516a") xpos 866 ypos 324 xysize (180, 43)
            text "▸  Projection" xpos 874 ypos 331 size 20 bold True color "#c7eef4"
            text "▸  Cameras" xpos 874 ypos 390 size 21 color "#829eac"
            text "▸  Systeme" xpos 874 ypos 434 size 21 color "#829eac"

            # Surface de la liste de fichiers.
            add Solid("#142c3e") xpos 248 ypos 211 xysize (543, 522)
            add Solid("#142c3e") xpos 1066 ypos 211 xysize (543, 522)
            text "1 fichier image" xpos 261 ypos 677 size 17 color "#7fa6b7"
            text "Dossier de projection vide" xpos 1081 ypos 677 size 17 color "#7fa6b7"

            # Zones partageant le meme draggroup. Le fichier a une taille de vignette.
            draggroup:
                drag:
                    drag_name "j26_projection_folder"
                    draggable False
                    droppable True
                    xpos 1111 ypos 266
                    xsize 450 ysize 353
                    frame:
                        xfill True yfill True padding (0, 0)
                        background Solid("#1e3c50")
                        fixed:
                            xfill True yfill True
                            add Solid("#467b96") xpos 1 ypos 1 xysize (448, 3)
                            text "▱" xalign 0.5 ypos 43 size 110 color "#9ed2e1"
                            text "DOSSIER PROJECTION" xalign 0.5 ypos 193 size 24 color "#e2f0f3" bold True
                            text "Deposer la photo ici" xalign 0.5 ypos 234 size 20 color "#b4d3dd"
                            text "ECRAN PRINCIPAL  /  01" xalign 0.5 ypos 276 size 16 color "#7ca7bb"

                drag:
                    drag_name "j26_photo_file"
                    draggable True
                    droppable False
                    drag_raise True
                    dragged j26_photo_transfer_dropped
                    xpos 297 ypos 279
                    xsize 411 ysize 290
                    frame:
                        xfill True yfill True padding (0, 0)
                        background Solid("#30526a")
                        fixed:
                            xfill True yfill True
                            add Solid("#66c5da") xpos 0 ypos 0 xysize (411, 3)
                            add Transform("bg_cg040", xysize=(389, 204)) xpos 11 ypos 13
                            text "MARA_PREUVE_25.png" xpos 13 ypos 231 size 23 color "#f4e9da" bold True
                            text "PNG  /  PHOTO CAPTUREE HIER" xpos 13 ypos 260 size 15 color "#a9cbd6"

            add Solid("#152e40") xpos 24 ypos 779 xysize (1600, 77)
            text "ACTION  /  TRANSFERT DE FICHIER" xpos 49 ypos 793 size 18 bold True color "#e8c08d"
            text "Maintenez le clic sur la miniature, glissez-la vers PROJECTION et relachez." xpos 49 ypos 821 size 20 color "#bed5de"
            text "CONNEXION SECURISEE" xpos 1377 ypos 814 size 17 color "#7cbec5"

screen j26_projector_preview():
    modal False
    zorder 100
    add Solid("#040912e8")
    frame at j26_projection_appear:
        xalign 0.5 yalign 0.5
        xsize 1500 ysize 905
        padding (0, 0)
        background Solid("#0c2031")
        fixed:
            xysize (1500, 905)
            add Solid("#254a60") xpos 0 ypos 0 xysize (1500, 65)
            text "◈  CONCLAVE OS  /  PROJECTION" xpos 28 ypos 14 size 29 color "#ebf1ee" bold True
            text "✓  TRANSFERT TERMINE" xpos 1124 ypos 20 size 22 color "#91dfc5"
            add Transform("bg_cg040", xysize=(1452, 776)) xpos 24 ypos 76
            text "MARA_PREUVE_25.png    /    AFFICHAGE PRINCIPAL ACTIF" xpos 30 ypos 863 size 19 color "#a9c9d5"

label j26_transferer_photo:
    call screen j26_photo_transfer
    show screen j26_projector_preview
    $ renpy.pause(2.0, hard=True)
    hide screen j26_projector_preview
    return
