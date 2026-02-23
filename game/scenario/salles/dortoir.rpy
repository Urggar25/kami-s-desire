default dortoir_lock = True


label DORTOIR_TP:
    scene bg_dortoir at adaptive_fullscreen

    if dortoir_lock:
        jump MAP_NOTHING_HERE

    $ pnc_room = "pnc_dortoir"
    call screen pnc_dortoir()


label CHAMBRE_TP:
    scene bg_chambre at adaptive_fullscreen

    if not free_time_active:
        jump MAP_NOTHING_HERE

    $ pnc_room = "pnc_chambre"
    call screen pnc_chambre()


label CHAMBRE_CHOIX_LIT:
    menu:
        "M'allonger pour passer le temps libre.":
            think "Je m'allonge sur le lit et laisse le temps filer."
            jump FREE_TIME_END

        "Je ne suis pas encore prêt à me reposer.":
            jump CHAMBRE_TP


screen pnc_dortoir():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/bg_dortoir.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    if free_time_active:
        imagebutton:
            idle "images/background/interact/livraison/porte.png"
            hover "images/background/interact/livraison/porte_hover.png"
            focus_mask True
            xpos 0
            ypos 0
            at cover_screen
            action Jump("CHAMBRE_TP")

    if free_time_active and lysa_link == 4:
        imagebutton:
            idle Transform("images/character/lysa/triste.png", zoom=0.75)
            hover Transform("images/character/lysa/sourire.png", zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "DORTOIR_TP"), Jump("LYSA_LINK_INTERACT")]


screen pnc_chambre():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/bg_chambre.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    imagebutton:
        idle "images/background/interact/chambre/lit.png"
        hover "images/background/interact/chambre/lit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CHAMBRE_CHOIX_LIT")
