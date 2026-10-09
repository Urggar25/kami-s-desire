# Jour 26 — Transfert de la photographie au projecteur du Conclave.
# Interface volontairement autonome : aucun fichier PNG supplémentaire requis.
# La miniature reprend l'image réelle de l'examen du jour 25.

init -1 python:
    def j26_photo_transfer_dropped(drags, drop):
        # Seul le dossier de projection accepte le fichier : les autres
        # lâchers réinitialisent simplement sa position.
        if drop is not None and drop.drag_name == "j26_projection_folder":
            return True
        return None

transform j26_projection_appear:
    alpha 0.0
    zoom 0.96
    ease 0.45 alpha 1.0 zoom 1.0

screen j26_photo_transfer():
    modal True
    zorder 200
    add Solid("#050b15f5")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1570
        ysize 850
        padding (0, 0)
        background Solid("#101e2dfc")

        fixed:
            xfill True
            yfill True

            add Solid("#162a39") xpos 0 ypos 0 xysize (1570, 75)
            text "CONCLAVE OS" xpos 37 ypos 19 size 31 bold True color "#e4eff2"
            text "TERMINAL DE PRÉSENTATION · CONNEXION LOCALE" xpos 1024 ypos 27 size 17 color "#84aebd"

            add Solid("#0c1724") xpos 30 ypos 96 xysize (1510, 78)
            text "GESTIONNAIRE DE FICHIERS" xpos 54 ypos 112 size 27 color "#e8c48b" bold True
            text "Glissez la photographie de la tablette vers le dossier de projection." xpos 54 ypos 145 size 19 color "#9bb4c2"

            add Solid("#152b3c") xpos 33 ypos 195 xysize (715, 497)
            add Solid("#152b3c") xpos 820 ypos 195 xysize (715, 497)

            text "TABLETTE DE NOAM" xpos 62 ypos 215 size 25 color "#f4e9d5" bold True
            text "Stockage interne  /  DCIM  /  ENQUÊTE" xpos 62 ypos 252 size 17 color "#88a8b8"
            text "1 élément · PNG" xpos 62 ypos 645 size 18 color "#8ca8b6"

            text "TERMINAL DU CONCLAVE" xpos 850 ypos 215 size 25 color "#f4e9d5" bold True
            text "Ce PC  /  Écran principal  /  PROJECTION" xpos 850 ypos 252 size 17 color "#88a8b8"
            text "Dossier vide" xpos 850 ypos 645 size 18 color "#8ca8b6"

            # Même draggroup : le drop fonctionne en souris et en tactile.
            draggroup:
                drag:
                    drag_name "j26_projection_folder"
                    draggable False
                    droppable True
                    xpos 900 ypos 305
                    xsize 550 ysize 310
                    frame:
                        xfill True
                        yfill True
                        padding (16, 27)
                        background Solid("#24465c")
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 18
                            text "▣" xalign 0.5 size 94 color "#91d4e2"
                            text "DÉPOSER ICI" xalign 0.5 size 31 color "#e3f4f5" bold True
                            text "ÉCRAN DU CONCLAVE" xalign 0.5 size 19 color "#a5c6d3"

                drag:
                    drag_name "j26_photo_file"
                    draggable True
                    droppable False
                    dragged j26_photo_transfer_dropped
                    xpos 95 ypos 320
                    xsize 540 ysize 274
                    frame:
                        xfill True
                        yfill True
                        padding (12, 12)
                        background Solid("#27485e")
                        vbox:
                            spacing 6
                            add Transform("bg_cg040", xysize=(516, 188))
                            text "MARA_PREUVE_25.png" size 24 bold True color "#f6f0e5"
                            text "Image PNG · photographiée hier" size 17 color "#b9d0d8"

            add Solid("#142838") xpos 30 ypos 716 xysize (1510, 102)
            text "ACTION 01 / 01" xpos 55 ypos 736 size 20 bold True color "#e4c48e"
            text "Maintenez le clic sur le fichier PNG, déplacez-le vers PROJECTION, puis relâchez." xpos 55 ypos 769 size 19 color "#cfdee5"

screen j26_projector_preview():
    modal False
    zorder 100
    add Solid("#03070de8")
    frame at j26_projection_appear:
        xalign 0.5
        yalign 0.5
        xsize 1420
        ysize 860
        padding (20, 20)
        background Solid("#122535")
        vbox:
            spacing 14
            hbox:
                xfill True
                text "CONCLAVE / PROJECTION" size 26 color "#e8c48b" bold True
                text "  ●  AFFICHAGE ACTIF" xalign 1.0 size 19 color "#84d8c6"
            add Transform("bg_cg040", xysize=(1380, 746))
            text "MARA_PREUVE_25.png  ·  1 / 1" size 18 color "#aec9d6"

label j26_transferer_photo:
    call screen j26_photo_transfer
    show screen j26_projector_preview
    $ renpy.pause(2.0, hard=True)
    hide screen j26_projector_preview
    return
