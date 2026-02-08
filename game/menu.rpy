# ============================================================
# MAIN MENU — Kami's Desires (adaptive_fullscreen + mask)
# ============================================================

# Si tu as déjà adaptive_fullscreen ailleurs, NE REDEFINIS PAS.
# Sinon, garde ceci (exemple classique cover) :
transform adaptive_fullscreen:
    xalign 0.5
    yalign 0.5
    # "cover" : on remplit l'écran sans déformer, on crop si besoin
    zoom max(config.screen_width / float(config.screen_width),
             config.screen_height / float(config.screen_height))

transform fit_fullscreen:
    xalign 0.5
    yalign 0.5
    # Contain : on voit toute l'image, bandes possibles
    zoom min(config.screen_width / float(config.image_width),
             config.screen_height / float(config.image_height))

init python:
    def fit(path):
        # Fit = contain (pas de crop)
        return im.Fit(path, config.screen_width, config.screen_height)

init python:
    def contain_rect(img_w, img_h, scr_w=None, scr_h=None):
        if scr_w is None: scr_w = config.screen_width
        if scr_h is None: scr_h = config.screen_height

        scale = min(scr_w / float(img_w), scr_h / float(img_h))
        w = int(img_w * scale)
        h = int(img_h * scale)
        x = int((scr_w - w) / 2)
        y = int((scr_h - h) / 2)
        return x, y, w, h

    # Place un point (rx, ry) dans le rect contain (rx/ry en 0..1)
    def in_rect(x, y, w, h, rx, ry):
        return int(x + w * rx), int(y + h * ry)

init python:
    def contain_params(img_w, img_h, scr_w=None, scr_h=None):
        if scr_w is None: scr_w = config.screen_width
        if scr_h is None: scr_h = config.screen_height

        scale = min(scr_w / float(img_w), scr_h / float(img_h))
        w = int(img_w * scale)
        h = int(img_h * scale)
        x = int((scr_w - w) / 2)
        y = int((scr_h - h) / 2)
        return x, y, scale



# (Optionnel mais utile) Déclare ton bg comme image
image bg_menu = "images/background/bg_menu.png"

# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
# ------------------------------------------------------------
# MAIN MENU (format PNC : full-screen buttons + cover_screen)
# ------------------------------------------------------------
screen main_menu():

    # menu Ren'Py
    tag menu
    zorder 200
    modal True

    on "show" action Play("music", audio.main_menu, fadein=1.0)
    on "hide" action Stop("music", fadeout=1.0)

    add Solid("#000")

    # Fond menu
    add "images/background/bg_menu.png" at cover_screen

    # NEW GAME
    imagebutton:
        idle "images/background/interact/menu/new_game.png"
        hover "images/background/interact/menu/new_game_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Start()

    # LOAD GAME
    imagebutton:
        idle "images/background/interact/menu/load_game.png"
        hover "images/background/interact/menu/load_game_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("load")

    # OPTIONS
    imagebutton:
        idle "images/background/interact/menu/option.png"
        hover "images/background/interact/menu/option_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("preferences")

    # GALLERY
    imagebutton:
        idle "images/background/interact/menu/gallery.png"
        hover "images/background/interact/menu/gallery_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action ShowMenu("gallery_menu")

    # QUIT
    imagebutton:
        idle "images/background/interact/menu/quit.png"
        hover "images/background/interact/menu/quit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Quit(confirm=True)


# ------------------------------------------------------------
# Placeholder Galerie (si tu n'as pas encore ta vraie galerie)
# ------------------------------------------------------------
screen gallery_menu():

    tag menu
    zorder 200
    modal True

    add Solid("#000")
    add "images/background/bg_menu.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)

        vbox:
            spacing 12
            text "Gallery" size 44
            text "Placeholder (à remplacer par ta galerie CG)." size 22
            textbutton "Back" action Return()
