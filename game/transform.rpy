# transform.rpy

transform eyelid_top_once(close=0.11, hold=0.04, open=0.16, overlap=80, amount=0.62):
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    xsize config.screen_width
    ysize 0

    easein close ysize int(config.screen_height * amount) + overlap
    pause hold
    easeout open ysize 0


transform eyelid_bottom_once(close=0.11, hold=0.04, open=0.16, overlap=80, amount=0.38):
    xpos 0
    ypos config.screen_height
    xanchor 0
    yanchor 1.0
    xsize config.screen_width
    ysize 0

    easein close ysize int(config.screen_height * amount) + overlap
    pause hold
    easeout open ysize 0


screen blink_overlay_loop():
    zorder 999

    default seq = 0
    default seq2 = 0
    default next_delay = 3.5
    default next_delay2 = None   # None = pas de second blink programmé

    # IMPORTANT : pas de repeat ici.
    # On recrée le timer via un id qui dépend de seq.
    timer next_delay action [
        SetScreenVariable("seq", seq + 1),
        SetScreenVariable("next_delay", renpy.random.uniform(2.2, 5.6)),
        # 12% de chance de double blink
        SetScreenVariable("next_delay2", 0.11 if (renpy.random.random() < 0.12) else None),
    ] id ("blink_timer_%d" % seq)

    # Timer du double blink, recréé via seq2
    if next_delay2 is not None:
        timer next_delay2 action [
            SetScreenVariable("seq2", seq2 + 1),
            SetScreenVariable("next_delay2", None),
        ] id ("blink_timer2_%d" % seq2)

    # Blink principal (top + bottom synchrones)
    add Solid("#000") at eyelid_top_once()    id ("blink_top_%d" % seq)
    add Solid("#000") at eyelid_bottom_once() id ("blink_bot_%d" % seq)

    # Second blink (synchronisé aussi)
    add Solid("#000") at eyelid_top_once(close=0.09, hold=0.03, open=0.13)    id ("blink2_top_%d" % seq2)
    add Solid("#000") at eyelid_bottom_once(close=0.09, hold=0.03, open=0.13) id ("blink2_bot_%d" % seq2)

init python:
    blink_seq = 0

    def blink():
        global blink_seq
        blink_seq += 1
        renpy.show_screen("blink_once", seq=blink_seq)


# transform.rpy ou screens.rpy

screen blink_once(seq=0, close=0.11, hold=0.04, open=0.16):
    zorder 999

    # durée totale estimée (fermeture + hold + ouverture) + marge
    timer (close + hold + open + 0.02) action Hide("blink_once")

    add Solid("#000") at eyelid_top_once(close=close, hold=hold, open=open) id ("once_top_%d" % seq)
    add Solid("#000") at eyelid_bottom_once(close=close, hold=hold, open=open) id ("once_bot_%d" % seq)

# -----------------------------------
# Transition de jour :

label end_day(next_day):

    stop music fadeout 1.0
    scene black with fade

    play sound "sfx/day_transition.wav"

    # Bloque le script pendant 5s, puis revient automatiquement
    call screen day_transition(next_day)

    $ current_day = next_day
    return

transform day_fade_5s:
    alpha 0.0
    linear 0.8 alpha 1.0
    pause 3.4
    linear 0.8 alpha 0.0

screen day_transition(day_label):

    modal True
    zorder 100

    add Solid("#000")

    # Ferme automatiquement au bout de 5s
    timer 5.0 action Return()

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox at day_fade_5s:
            spacing 12
            xalign 0.5

            text "Day [day_label]":
                size 84
                color "#FFFFFF"
                font "fonts/day_font.ttf"
                xalign 0.5

            add Solid("#FFFFFF", xysize=(600, 2)):
                xalign 0.5


screen free_time_transition():

    modal True
    zorder 100

    add Solid("#000")

    timer 5.0 action Return()

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox at day_fade_5s:
            spacing 12
            xalign 0.5

            text "Temps libre":
                size 84
                color "#FFFFFF"
                font "fonts/day_font.ttf"
                xalign 0.5

            add Solid("#FFFFFF", xysize=(600, 2)):
                xalign 0.5

# -----------------------------------
# Ecran pour Kami quand il parle :

# --- State ---
default broadcast_char = None
default broadcast_expr = "neutre"
default broadcast_on = False

default broadcast_px = 0   # ou une petite valeur comme -50 si besoin d'un léger ajustement
default broadcast_py = 0   # ou -50 / -100 selon la hauteur du sprite
default broadcast_pz = 1.0 # ou 0.95 → 1.1 selon si tu veux zoomer un peu plus

# --- Transforms ---
transform broadcast_frame:
    xpos 40
    ypos 40
    anchor (0.0, 0.0)

transform broadcast_portrait:
    xpos 24
    ypos 32
    anchor (0.0, 0.0)
    zoom 0.9

transform broadcast_glass:
    alpha 0.10

screen kami_broadcast_ui():
    zorder 200

    # Tout l'UI Kami n'apparaît QUE s'il y a un personnage en diffusion
    if broadcast_char is not None:
        text "DIFFUSION" xpos 0.90 ypos 0.03 size 18 color "#BFE8FF" outlines [(2, "#00000088", 0, 0)]

        fixed:
            xpos 40
            ypos 40
            anchor (0.0, 0.0)

            $ bw = 460
            $ bh = 600
            $ tilt = -8
            $ center_x = bw // 2
            $ center_y = bh // 2

            # Fond du cadre incliné
            add Solid("#E9F6FF22", xsize=bw, ysize=bh) at Transform(rotate=tilt, anchor=(0.5, 0.5), xpos=center_x, ypos=center_y)

            # Portrait avec marge + crop (ta version finale qui marche bien)
            add DynamicDisplayable(bc_portrait_dd) at Transform(
                rotate=tilt,
                anchor=(0.5, 0.5),
                xpos=center_x,
                ypos=center_y
            )

            # Nom du personnage
            text "[broadcast_char]":
                size 18
                color "#BFE8FF"
                outlines [(2, "#000000AA", 0, 0)]
                xpos 70
                ypos (bh - 40)
                at Transform(rotate=tilt, anchor=(0.0, 1.0))

init python:
    def bc_portrait_dd(st, at):
        """
        DynamicDisplayable avec marge pour rotation + crop final pour garder la taille exacte du cadre
        """
        if not store.broadcast_char:
            return Null(), 0

        bw = 460
        bh = 600

        # Marge pour absorber la rotation sans clipping (150 est parfait pour tilt -8°)
        margin = 150

        viewport_w = bw + 2 * margin
        viewport_h = bh + 2 * margin

        fn = "images/character/%s/%s.png" % (store.broadcast_char, store.broadcast_expr)

        d = Viewport(
            child=Transform(
                fn,
                xpos=store.broadcast_px + margin,   # offset pour centrer dans le grand viewport
                ypos=store.broadcast_py + margin,
                zoom=store.broadcast_pz
            ),
            xmaximum=viewport_w,
            ymaximum=viewport_h,
            draggable=False,
            mousewheel=False
        )

        # On ne garde que la zone centrale → cadre exact 460x600
        d = Crop((margin, margin, bw, bh), d)

        return d, 0

# --- Python helpers ---
init python:
    def bc_show(char_name, expr="neutre", px=None, py=None, pz=None):
        store.broadcast_on = True
        store.broadcast_char = char_name
        store.broadcast_expr = expr

        if px is not None: store.broadcast_px = px
        if py is not None: store.broadcast_py = py
        if pz is not None: store.broadcast_pz = pz

        renpy.restart_interaction()

    def bc_hide():
        # On garde l'écran Kami, on enlève juste le portrait.
        store.broadcast_char = None
        renpy.restart_interaction()

    def bc_off():
        store.broadcast_on = False
        store.broadcast_char = None
        renpy.restart_interaction()

label reset:
    $ broadcast_px = 0
    $ broadcast_py = 0
    $ broadcast_pz = 1.0

transform screen_shake:
    xoffset 0 yoffset 0
    linear 0.04 xoffset -20
    linear 0.04 xoffset 20
    linear 0.04 xoffset -15
    linear 0.04 xoffset 15
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset 0

transform heavy_shake:
    xoffset 0 yoffset 0
    linear 0.03 xoffset -15 yoffset -10
    linear 0.03 xoffset 15 yoffset 10
    linear 0.03 xoffset -10 yoffset 5
    linear 0.03 xoffset 10 yoffset -5
    linear 0.03 xoffset -5 yoffset 5
    linear 0.03 xoffset 5 yoffset -5
    linear 0.03 xoffset 0 yoffset 0
