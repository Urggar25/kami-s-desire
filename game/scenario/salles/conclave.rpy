default conclave_lock = True

label CONCLAVE_TP:
    scene bg_conclave at adaptive_fullscreen

    if free_time_active and elen_link == 0:
        $ pnc_room = "pnc_conclave"
        call screen pnc_conclave()

    if conclave_lock:
        jump MAP_NOTHING_HERE
    else:
        jump CONCLAVE_ENTREE


screen pnc_conclave():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/bg_conclave.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")

    if free_time_active and elen_link == 0:
        imagebutton:
            idle Transform("images/character/elen/joie.png", zoom=0.75)
            hover Transform("images/character/elen/content.png", zoom=0.75)
            focus_mask True
            xalign 0.52
            yalign 0.30
            action [SetVariable("last_room_label", "CONCLAVE_TP"), Jump("ELEN_LINK_INTERACT")]


label CONCLAVE_ENTREE:
    "Je rentre dans le Conclave"
    jump MAP_NOTHING_HERE
