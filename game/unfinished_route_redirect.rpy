# Interface commune lorsqu'un resultat de vote conduit a une route non developpee.
# Ne s'affiche qu'apres la resolution d'un vote : les choix critiques
# non ecrits restent verrouilles dans critical_choice.rpy.
screen kd_route_vote_convergence():
    modal True
    zorder 230
    key "game_menu" action NullAction()
    add Solid("#030914E8")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1050
        background Solid("#102336")
        padding (52, 44)
        vbox:
            spacing 22
            xfill True
            text "CONTINUITE DE L'HISTOIRE":
                font "fonts/Rajdhani-SemiBold.ttf"
                size 43
                color "#91DDF3"
                xalign 0.5
            add Solid("#498BAA") xalign 0.5 xsize 760 ysize 2
            text "Les consequences de ce vote appartiennent a une route encore en developpement.":
                size 28
                color "#F1F7FC"
                xalign 0.5
                textalign 0.5
                xmaximum 900
            text "Pour poursuivre votre partie, l'histoire rebascule sur la route actuellement disponible. Les evenements qui suivent correspondent a cette autre issue du vote.":
                size 25
                color "#BCD5E4"
                xalign 0.5
                textalign 0.5
                xmaximum 900
            textbutton "CONTINUER L'HISTOIRE":
                style "kd_dlc_action"
                action Return()
                xalign 0.5
    key "K_RETURN" action Return()
    key "K_KP_ENTER" action Return()
