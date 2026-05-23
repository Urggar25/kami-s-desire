default dortoir_lock = True


label DORTOIR_TP:
    scene bg_dortoir at adaptive_fullscreen

    if dortoir_lock:
        jump MAP_NOTHING_HERE

    if free_time_active and free_time_round == 3 and not seen_voyeur_nyra:
        jump temps_libre_salle_dortoir

    $ pnc_room = "pnc_dortoir"
    call screen pnc_dortoir()

    if free_time_active:
        return


label CHAMBRE_TP:
    scene bg_chambre at adaptive_fullscreen

    if not free_time_active:
        jump MAP_NOTHING_HERE

    $ pnc_room = "pnc_chambre"
    call screen pnc_chambre()

    if free_time_active:
        return


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

    use exploration_retour_button


screen pnc_chambre():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/bg_chambre.png" at cover_screen

    imagebutton:
        idle "images/background/interact/chambre/lit.png"
        hover "images/background/interact/chambre/lit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CHAMBRE_CHOIX_LIT")

    imagebutton:
        idle ("images/background/interact/chambre/brouilleur_on.png" if noam_room_jammer_on else "images/background/interact/chambre/brouilleur_off.png")
        hover ("images/background/interact/chambre/brouilleur_on.png" if noam_room_jammer_on else "images/background/interact/chambre/brouilleur_off.png")
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CHAMBRE_BROUILLEUR")

    use exploration_retour_button


screen chambre_brouilleur_panel():
    modal True
    zorder 230

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 620
        background Solid("#071018f2")
        padding (28, 24)

        vbox:
            spacing 18
            $ jammer_state_text = "ACTIF" if noam_room_jammer_on else "INACTIF"
            $ jammer_state_color = "#7DF0FF" if noam_room_jammer_on else "#FF7B7B"
            text "BROUILLEUR DE CHAMBRE" size 34 color "#E8F4FF" xalign 0.5
            text "ÉTAT : [jammer_state_text]" size 28 color jammer_state_color xalign 0.5

            hbox:
                spacing 16
                xalign 0.5
                textbutton "Activer":
                    xsize 160
                    ysize 54
                    action Return("on")
                textbutton "Désactiver":
                    xsize 180
                    ysize 54
                    action Return("off")

            textbutton "Retour":
                xalign 0.5
                xsize 160
                ysize 54
                action Return("back")

label CHAMBRE_BROUILLEUR:

    call screen chambre_brouilleur_panel()

    if _return == "on":
        call chambre_brouilleur_trace from _call_chambre_brouilleur_trace_on
        $ noam_room_jammer_on = True
        think "Le voyant bleu me rassure plus qu'il ne devrait."
        think "Au moins, ce silence-là m'appartient."
    elif _return == "off":
        call chambre_brouilleur_trace from _call_chambre_brouilleur_trace_off
        $ noam_room_jammer_on = False
        think "Le voyant rouge reste fixe."
        think "Si Kami regarde, au moins elle verra ce qu'elle a fabriqué."

    jump CHAMBRE_TP

label chambre_brouilleur_trace:
    while True:
        call screen trace_qte(path_type="s_curve", time_limit=5.5, wait_time=0.6, tolerance=60, max_errors=4, anchor_x=1075, anchor_y=565)
        if _return:
            return
        think "Je rate l'acces au boitier."
        think "Je reprends plus lentement."
