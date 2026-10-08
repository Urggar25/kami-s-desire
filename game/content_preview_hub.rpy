# Main-menu-only content preview selector.
screen content_preview_hub():
    tag menu
    modal True
    add gui.main_menu_background
    add Solid("#030C16DD")
    text "KAMI'S DESIRES":
        xpos 150 ypos 104 size 79 color "#E9F8FA"
        font "fonts/Rajdhani-SemiBold.ttf"
    text "CONTENT PREVIEWS":
        xpos 152 ypos 205 size 38 kerning 3 color "#82D6E5"
    text "APERÇUS DU CONTENU":
        xpos 152 ypos 259 size 22 color "#B1C9D0"

    frame:
        xpos 160 ypos 390 xsize 770 ysize 410
        background Solid("#0A1A28F5") padding (37, 28)
        vbox:
            spacing 18
            text "01  /  PHOTO MODE" size 46 color "#E7F5F9"
            text "Explore the scene. Capture the evidence." size 27 color "#AFCED5"
            text "Explorez la scène. Photographiez les indices." size 21 color "#91B4C0"
            null height 35
            textbutton "WATCH PREVIEW  /  VOIR L'APERÇU":
                text_size 29 text_color "#65D4E5" text_hover_color "#FFFFFF"
                action ShowMenu("content_preview")

    frame:
        xpos 982 ypos 390 xsize 770 ysize 410
        background Solid("#0A1A28F5") padding (37, 28)
        vbox:
            spacing 18
            text "02  /  CODED KNOCK" size 46 color "#E7F5F9"
            text "Remember the rhythm. Unlock the door." size 27 color "#AFCED5"
            text "Mémorisez le rythme. Ouvrez la porte." size 21 color "#91B4C0"
            null height 35
            textbutton "WATCH PREVIEW  /  VOIR L'APERÇU":
                text_size 29 text_color "#65D4E5" text_hover_color "#FFFFFF"
                action ShowMenu("content_preview_knock")

    textbutton "BACK TO MENU  /  RETOUR AU MENU":
        xpos 152 ypos 907
        text_size 25 text_color "#B5D8DE" text_hover_color "#FFFFFF"
        action ShowMenu("main_menu")
    key "K_ESCAPE" action ShowMenu("main_menu")
