# Menu des extensions — accessible depuis le menu principal.
screen kd_dlc_menu():
    tag menu
    modal True
    add Solid("#030912")
    frame:
        xalign 0.5 yalign 0.5
        xsize 1140
        background Solid("#0C1B2AEF")
        padding (50, 45)
        vbox:
            spacing 24
            text "CONTENUS ADDITIONNELS" size 52 color "#DFF8FF" xalign 0.5
            text "KAMI'S DESIRES // EXTENSIONS NARRATIVES" size 19 color "#71BED3" xalign 0.5
            frame:
                background Solid("#142838")
                padding (28, 24)
                vbox:
                    spacing 14
                    text "LES AUTRES VIES" size 38 color "#FFFFFF"
                    text "DOPPELGÄNGER — JOURS 20 À 30" size 23 color "#A3D8EA"
                    text "La première fin du jour 20 est accessible gratuitement. Les autres branches et fins nécessitent cette extension." size 23 color "#D4E4EC"
                    if kd_dlc_unlocked("doppelganger_routes"):
                        text "INSTALLÉ — CONTENU DISPONIBLE" size 25 color "#8BE3B6"
                        hbox:
                            spacing 20
                            textbutton "GALERIE" action ShowMenu("gallery_menu")
                            textbutton "SOUVENIRS" action ShowMenu("scene_select_menu")
                    else:
                        text "NON INSTALLÉ — CONTENU VERROUILLÉ" size 25 color "#F8B98E"
                        text "Installez l'extension acquise auprès du distributeur, puis relancez le jeu." size 19 color "#A7BBC9"
            textbutton "RETOUR" xalign 0.5 action Return()
    key "K_ESCAPE" action Return()

screen kd_dlc_locked_notice():
    modal True
    add Solid("#030914E8")
    frame:
        xalign 0.5 yalign 0.5 xsize 860
        background Solid("#152738")
        padding (42, 35)
        vbox:
            spacing 20
            text "CHOIX VERROUILLÉ" size 40 color "#FFF0E1" xalign 0.5
            text "Cette branche fait partie du DLC « Les autres vies »." size 27 color "#D6E9F0" xalign 0.5
            text "La fin gratuite reste accessible par l'autre choix." size 23 color "#A3CFDD" xalign 0.5
            textbutton "REVENIR AU CHOIX" action Return() xalign 0.5
    key "K_ESCAPE" action Return()

screen kd_dlc_qte_retry():
    modal True
    add Solid("#020811ED")
    frame:
        xalign 0.5 yalign 0.5 xsize 940
        background Solid("#112338")
        padding (43, 36)
        vbox:
            spacing 22
            text "UNE AUTRE ISSUE EXISTE" size 39 color "#F4FCFF" xalign 0.5
            text "Cette issue mène à une autre branche, comprise dans « Les autres vies ». Vous pouvez recommencer cette séquence pour découvrir la fin gratuite." size 25 color "#D6EAF4"
            textbutton "RECOMMENCER LA SÉQUENCE" action Return() xalign 0.5

# Proposition seulement après avoir terminé la route gratuite.
screen kd_dlc_extend_j20():
    modal True
    add Solid("#010611ED")
    frame:
        xalign 0.5 yalign 0.5 xsize 880
        background Solid("#152739")
        padding (45, 35)
        vbox:
            spacing 23
            text "UNE AUTRE SCÈNE EXISTE" size 41 color "#E9F9FF" xalign 0.5
            text "Vous avez atteint la fin gratuite. Voulez-vous découvrir ce qui se passe après ?" size 26 color "#C8E6ED" xalign 0.5
            textbutton "VOIR LA SUITE (DLC)" action Return(True) xalign 0.5
            textbutton "REVENIR AU MENU" action Return(False) xalign 0.5
