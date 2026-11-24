# J3: diegetic broadcast graphics. No external art or timed gameplay dependency.
transform kd_j3_panel_in(delay=0.0):
    alpha 0.0
    yoffset 22
    pause delay
    easeout .32 alpha 1.0 yoffset 0

transform kd_j3_live_dot:
    alpha 1.0
    linear .65 alpha .45
    linear .65 alpha 1.0
    repeat

screen kd_j3_limen_feed(show_count=False):
    zorder 40
    modal False
    default count = 12341
    if show_count:
        timer 1.4 repeat True action SetScreenVariable("count", min(count + 1, 12347))
    add Solid("#07131c22")
    frame:
        xpos 42
        ypos 36
        padding (22, 12)
        background Solid("#07151eee")
        hbox:
            spacing 15
            add Solid("#e85568", xysize=(12, 12)) yalign .5 at kd_j3_live_dot
            text _("DIRECT") size 24 color "#ffffff"
            text " / LIMEN" size 24 color "#98c7d7"
    frame:
        xalign .5
        ypos 690
        xsize 1000
        padding (30, 20)
        background Solid("#07151eee")
        if show_count:
            vbox:
                spacing 4
                text _("FOYERS SANS RATION COMPLÈTE") size 23 color "#b9cfd9" xalign .5
                text ("{:,}".format(count).replace(",", " ")) size 60 color "#ff7785" xalign .5
        else:
            text _("CENTRE DE DISTRIBUTION") size 25 color "#b9cfd9" xalign .5

screen kd_j3_contracts(stage=1):
    zorder 40
    modal False
    frame:
        xalign .5
        ypos 75
        xsize 1560
        padding (42, 32)
        background Solid("#081825f5")
        vbox:
            spacing 25
            text _("KAMI — PROGRAMME DE CONTRATS") size 23 color "#84c8df"
            text _("Votre nouvelle liberté !") size 48 color "#f1faff"
            hbox:
                spacing 24
                for i, (number, heading, detail) in enumerate((("01", _("TRAVAILLEZ"), _("Tâches et objectifs")), ("02", _("GAGNEZ"), _("Salaire")), ("03", _("ACHETEZ"), _("Échange de marchandises")))):
                    if i == 0 or stage >= 2:
                        frame:
                            xsize 468
                            ysize 260
                            padding (25, 20)
                            background Solid("#24303b" if stage == 3 and i == 2 else "#123b4d")
                            at kd_j3_panel_in(i * .14)
                            vbox:
                                spacing 18
                                text number size 40 color "#84d7e8"
                                text heading size 36 color "#e8f9ff"
                                text detail size 25 color "#b5d5df"
            if stage == 3:
                frame:
                    xfill True
                    padding (20, 15)
                    background Solid("#53232f")
                    at kd_j3_panel_in()
                    text _("Aucune distribution gratuite.") size 32 color "#ffc0c7"
