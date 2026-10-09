# Jour 26 — LA PREUVE IMPOSSIBLE
# Reconstitution chronologique du témoignage de Noam.
# Aucun argument ne prouve à lui seul l'identité du corps :
# le joueur obtient uniquement une narration cohérente.
default j26_preuve_success = False

init -1 python:
    J26_PREUVE_CARDS = (
        ("premiere", "01 / PREMIÈRE DÉCOUVERTE", "Noam avait déjà aperçu ce corps dans la salle de maintenance."),
        ("tissu", "02 / LE MORCEAU DE TISSU", "Un morceau de vêtement entraîne Noam et Iris dans la ventilation."),
        ("temoin", "03 / LE TÉMOIN", "Iris voit le cadavre derrière la cloison et reconnaît Mara."),
        ("photo", "04 / LA PHOTOGRAPHIE", "Le corps est photographié sur place, avant leur départ."),
    )
    J26_PREUVE_ORDER = ("premiere", "tissu", "temoin", "photo")
    J26_PREUVE_LABELS = dict((key, title.split(" / ", 1)[1]) for key, title, body in J26_PREUVE_CARDS)

screen j26_preuve_screen():
    modal True
    zorder 200
    default selection = []
    default error = False

    add Solid("#040a15f3")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1500
        ysize 830
        padding (42, 34)
        background Solid("#111d2bf5")

        vbox:
            spacing 17
            text "DOSSIER D'ENQUÊTE  /  J26" color "#6dbbce" size 24 bold True
            text "LA PREUVE IMPOSSIBLE" color "#f1e9d9" size 48 bold True
            text "RECONSTITUEZ L'ORDRE DES FAITS" color "#e3b77e" size 26 bold True
            text "La photographie peut être truquée. Présentez les quatre faits dans l'ordre où ils se sont produits." color "#bbcad3" size 24
            null height 6

            frame:
                xfill True
                padding (24, 20)
                background Solid("#1b3040")
                vbox:
                    spacing 14
                    text "CHRONOLOGIE  ·  [len(selection)] / 4" color "#8ed0df" size 23 bold True
                    hbox:
                        spacing 12
                        for i in range(4):
                            frame:
                                xsize 328
                                ysize 104
                                padding (13, 12)
                                background Solid("#294957" if i < len(selection) else "#101e2c")
                                vbox:
                                    spacing 6
                                    text "ÉTAPE [i + 1]" color "#e5bd83" size 19 bold True
                                    if i < len(selection):
                                        text J26_PREUVE_LABELS[selection[i]] color "#f7f3eb" size 21 bold True
                                    else:
                                        text "Sélectionnez un indice" color "#6d8b9b" size 20

            text "ÉLÉMENTS DISPONIBLES" color "#e5bd83" size 23 bold True

            grid 2 2:
                spacing 12
                for key, title, body in J26_PREUVE_CARDS:
                    frame:
                        xsize 676
                        ysize 110
                        padding (12, 10)
                        background Solid("#1f3545" if key not in selection else "#182632")
                        if key not in selection:
                            button:
                                xfill True
                                yfill True
                                background Solid("#00000000")
                                hover_background Solid("#34647c")
                                action [SetScreenVariable("selection", selection + [key]), SetScreenVariable("error", False)]
                                vbox:
                                    spacing 3
                                    text title.split(" / ", 1)[1] color "#f1e9d9" size 24 bold True
                                    text body color "#afc5d1" size 20
                        else:
                            vbox:
                                spacing 4
                                text title.split(" / ", 1)[1] color "#6d8391" size 24 bold True
                                text "Ajouté à la chronologie" color "#7498a4" size 20

            if error:
                text "Cette chronologie comporte une incohérence. Revérifiez l'ordre des découvertes." color "#ec9a8d" size 21 bold True
            else:
                text "Chaque pièce est pertinente, mais leur succession est essentielle." color "#889eac" size 21

            hbox:
                spacing 18
                textbutton "EFFACER":
                    action [SetScreenVariable("selection", []), SetScreenVariable("error", False)]
                    text_size 23
                    text_color "#f1e9d9"
                    background Solid("#334452")
                    padding (24, 13)
                textbutton "ANNULER LE DERNIER":
                    action [SetScreenVariable("selection", selection[:-1]), SetScreenVariable("error", False)]
                    sensitive len(selection) > 0
                    text_size 23
                    text_color "#f1e9d9"
                    background Solid("#334452")
                    padding (24, 13)
                textbutton "PRÉSENTER LES FAITS":
                    action If(tuple(selection) == J26_PREUVE_ORDER, Return(True), SetScreenVariable("error", True))
                    sensitive len(selection) == 4
                    text_size 24
                    text_color "#0b1c28"
                    background Solid("#e5bd83")
                    padding (24, 13)
                textbutton "PASSER":
                    action Return(False)
                    text_size 20
                    text_color "#9faebb"
                    background Solid("#1c2c38")
                    padding (18, 14)

label j26_preuve_impossible:
    call screen j26_preuve_screen
    $ j26_preuve_success = bool(_return)
    return
