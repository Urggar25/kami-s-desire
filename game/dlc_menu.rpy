# KAMI.CORE // Catalogue des extensions.
# Les zones interactives sont des vrais boutons Ren'Py, pas des images figées.

transform kd_dlc_fade:
    alpha 0.0
    easeout 0.35 alpha 1.0

transform kd_dlc_hero_drift:
    subpixel True
    zoom 1.03
    xalign 0.5 yalign 0.5
    linear 12.0 zoom 1.12
    linear 12.0 zoom 1.03
    repeat

style kd_dlc_action is button:
    background Solid("#A82F4C")
    hover_background Solid("#DD4667")
    padding (25, 14)
    xminimum 260
    yminimum 62

style kd_dlc_action_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 27
    color "#FFFFFF"
    hover_color "#FFFFFF"
    xalign 0.5 yalign 0.5

style kd_dlc_secondary is button:
    background Solid("#152B3BD9")
    hover_background Solid("#28536A")
    padding (25, 13)
    xminimum 205
    yminimum 60

style kd_dlc_secondary_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 25
    color "#C1E6F1"
    hover_color "#FFFFFF"
    xalign 0.5 yalign 0.5

screen kd_dlc_menu():
    tag menu
    modal True
    zorder 220
    $ _installed = kd_dlc_unlocked("doppelganger_routes")
    $ _accent = "#8AE7CA" if _installed else "#FB8C9D"

    add Solid("#02070D")
    add "gui/main_menu_kami/bg_orbit.png" at Transform(fit="cover", xysize=(1920,1080), alpha=0.19)
    add "gui/main_menu_kami/vignette.png" alpha 0.80
    add "gui/main_menu_kami/scanlines.png" alpha 0.10

    # En-tête du catalogue
    add Solid("#69D2EB") xpos 78 ypos 74 xsize 7 ysize 60
    vbox:
        xpos 108 ypos 65 spacing 3
        text "KAMI.CORE  /  EXTENSIONS" font "fonts/Rajdhani-SemiBold.ttf" size 19 color "#7CB8C9" kerning 3
        text "DOSSIERS ADDITIONNELS" font "fonts/Rajdhani-SemiBold.ttf" size 49 color "#EDF8FB" kerning 1
    text "01  /  01" xpos 1680 ypos 78 font "fonts/Rajdhani-SemiBold.ttf" size 24 color "#88AABC"

    # Carte principale : visuel cinématographique à gauche, informations à droite.
    fixed at kd_dlc_fade:
        xpos 77 ypos 176 xsize 1764 ysize 748
        add Solid("#4A7C905C") xsize 1764 ysize 748
        add Solid("#07131EF8") xpos 2 ypos 2 xsize 1760 ysize 744

        # Zone trailer avec une vraie image du jeu et non une carte vide.
        fixed:
            xpos 22 ypos 22 xsize 970 ysize 704
            clipping True
            add "bg_cg030" at kd_dlc_hero_drift
            add Solid("#03101A6A")
            add Solid("#02070DE2") ypos 472 xsize 970 ysize 232
            add Solid("#D24464") xpos 0 ypos 0 xsize 7 ysize 704
            text "STORY PACK 01" xpos 38 ypos 36 font "fonts/Rajdhani-SemiBold.ttf" size 27 color "#FFFFFF" kerning 4
            text "DOSSIER CLASSIFIÉ  //  J20–J30" xpos 38 ypos 76 font "fonts/Rajdhani-SemiBold.ttf" size 19 color "#F1A6B6" kerning 2
            vbox:
                xpos 40 ypos 501 spacing 6
                text "UNE SEULE" font "fonts/Rajdhani-SemiBold.ttf" size 49 color "#F3F9FF"
                text "VERSION DES FAITS." font "fonts/Rajdhani-SemiBold.ttf" size 67 color "#FB718B"
                text "Toutes les réponses ne se trouvent pas au même endroit." font "fonts/Barlow-Light.ttf" size 23 color "#B9CBD6"
            button:
                xpos 385 ypos 224 xsize 202 ysize 148
                background Solid("#050C18BC")
                hover_background Solid("#B52F51ED")
                action Function(renpy.call_in_new_context, "kd_dlc_doppelganger_trailer")
                vbox:
                    align (0.5, 0.5) spacing 7
                    text "▶" xalign 0.5 font "fonts/Rajdhani-SemiBold.ttf" size 70 color "#FFFFFF"
                    text "VOIR LE TRAILER" xalign 0.5 font "fonts/Rajdhani-SemiBold.ttf" size 19 color "#FFFFFF"

        # Fiche DLC — grande typographie, hiérarchie claire, vrais boutons.
        fixed:
            xpos 1014 ypos 22 xsize 724 ysize 704
            add Solid("#0C1C29") xsize 724 ysize 704
            add Solid("#D24464") xpos 33 ypos 36 xsize 56 ysize 4
            text "EXTENSION NARRATIVE" xpos 106 ypos 22 font "fonts/Rajdhani-SemiBold.ttf" size 22 color "#E3879C" kerning 2
            text "L'ANGLE MORT" xpos 35 ypos 76 font "fonts/Rajdhani-SemiBold.ttf" size 62 color "#F5FAFD"
            text "UN DOSSIER RESTÉ OUVERT" xpos 38 ypos 159 font "fonts/Rajdhani-SemiBold.ttf" size 27 color "#9ED7E6" kerning 2
            add Solid("#4C718360") xpos 37 ypos 212 xsize 646 ysize 2
            hbox:
                xpos 38 ypos 235 spacing 14
                frame:
                    background Solid("#173445") padding (17, 10)
                    text "JOURS 20–30" size 20 color "#D6EFF5" font "fonts/Rajdhani-SemiBold.ttf"
                frame:
                    background Solid("#173445") padding (17, 10)
                    text "FINS ALTERNATIVES" size 20 color "#D6EFF5" font "fonts/Rajdhani-SemiBold.ttf"
            text "Vous connaissez une fin. Pas toute l'histoire." xpos 38 ypos 321 font "fonts/Rajdhani-SemiBold.ttf" size 34 color "#EFF8FB"
            text "Retrouvez les décisions que vous n'avez pas prises, explorez les autres branches et découvrez ce qui se cache derrière les événements du Conclave.":
                xpos 38 ypos 379 xmaximum 639
                font "fonts/Barlow-Light.ttf" size 25 color "#BDD0DA" line_spacing 4
            add Solid("#4C718360") xpos 37 ypos 509 xsize 646 ysize 2
            add Solid(_accent) xpos 39 ypos 539 xsize 10 ysize 10
            text ("EXTENSION INSTALLÉE" if _installed else "EXTENSION NON INSTALLÉE") xpos 65 ypos 527 font "fonts/Rajdhani-SemiBold.ttf" size 26 color _accent
            if _installed:
                text "Contenu disponible dans votre partie." xpos 38 ypos 563 font "fonts/Barlow-Light.ttf" size 20 color "#91B6C4"
            else:
                text "Les routes supplémentaires sont verrouillées dans cette édition." xpos 38 ypos 563 font "fonts/Barlow-Light.ttf" size 20 color "#91B6C4"
            hbox:
                xpos 38 ypos 615 spacing 14
                textbutton "▶  BANDE-ANNONCE" style "kd_dlc_action" action Function(renpy.call_in_new_context, "kd_dlc_doppelganger_trailer")
                textbutton "STEAM  ↗" style "kd_dlc_secondary" action Function(renpy.open_url, KD_DLC_STEAM_URL)

    hbox:
        xpos 78 ypos 960 spacing 20
        textbutton "←  RETOUR AU MENU" style "kd_dlc_secondary" action Return()

    text "KAMI'S DESIRES   /   LES ARCHIVES NE DISENT PAS TOUT." xpos 1340 ypos 979 font "fonts/Rajdhani-SemiBold.ttf" size 19 color "#6B91A3"
    key "K_ESCAPE" action Return()


screen kd_dlc_store_information():
    modal True
    zorder 350
    add Solid("#02060CEB")
    frame:
        xalign 0.5 yalign 0.5 xsize 840
        background Solid("#0D1B28")
        padding (48, 42)
        vbox:
            spacing 20
            text "L'ANGLE MORT" size 44 color "#F3FAFF" xalign 0.5
            text "Cette extension n'est pas installée." size 27 color "#F4A2B1" xalign 0.5
            text "Vous pouvez consulter sa disponibilité sur Steam. Après installation, relancez Kami's Desires." size 24 color "#C5D9E2" xalign 0.5
            textbutton "FERMER" style "kd_dlc_secondary" xalign 0.5 action Hide("kd_dlc_store_information")
    key "K_ESCAPE" action Hide("kd_dlc_store_information")

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
            text "Cette branche fait partie de l’extension « L’Angle mort »." size 27 color "#D6E9F0" xalign 0.5
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
            text "Cette issue mène à une autre branche, comprise dans « L’Angle mort ». Vous pouvez recommencer cette séquence pour découvrir la fin gratuite." size 25 color "#D6EAF4"
            textbutton "RECOMMENCER LA SÉQUENCE" action Return() xalign 0.5

screen kd_dlc_extend_j20():
    modal True
    add Solid("#010611ED")
    frame:
        xalign 0.5 yalign 0.5 xsize 880
        background Solid("#152739")
        padding (45, 35)
        vbox:
            spacing 23
            text "UNE SUITE RESTE À DÉCOUVRIR" size 41 color "#E9F9FF" xalign 0.5
            text "Vous avez atteint la fin gratuite. Voulez-vous découvrir ce qui se passe après ?" size 26 color "#C8E6ED" xalign 0.5
            textbutton "VOIR LA SUITE (DLC)" action Return(True) xalign 0.5
            textbutton "REVENIR AU MENU" action Return(False) xalign 0.5
