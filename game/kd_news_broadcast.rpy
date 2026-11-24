# Kami's Desires — habillage TV autonome, 1920x1080 (Ren'Py 8.3).
# Les textes sont des paramètres traduisibles, jamais rasterisés.
# Le bandeau reste au-dessus de la zone de dialogue (y >= 802).
# Aucun timer ne modifie le scénario ni les variables de vote.

transform kd_news_power:
    alpha 0.0
    linear 0.10 alpha 1.0
    pause 0.98
    easein 0.22 alpha 0.0

transform kd_news_shutter:
    subpixel True
    xzoom 0.0
    yzoom 0.025
    alpha 0.9
    easeout 0.16 xzoom 1.0
    easeout 0.24 yzoom 1.0
    linear 0.18 alpha 0.0

transform kd_news_intro_left:
    subpixel True
    xoffset -1200
    easeout 0.48 xoffset 0
    pause 0.55
    easein 0.30 xoffset -1200

transform kd_news_intro_right:
    subpixel True
    xoffset 1200
    easeout 0.48 xoffset 0
    pause 0.55
    easein 0.30 xoffset 1200

transform kd_news_intro_title:
    alpha 0.0
    yoffset 30
    pause 0.24
    easeout 0.32 alpha 1.0 yoffset 0
    pause 0.42
    easein 0.24 alpha 0.0 yoffset -12

transform kd_news_slide(delay=0.0):
    subpixel True
    alpha 0.0
    xoffset -90
    pause delay
    easeout 0.34 alpha 1.0 xoffset 0

transform kd_news_drop:
    subpixel True
    alpha 0.0
    yoffset -28
    easeout 0.32 alpha 1.0 yoffset 0

transform kd_news_live_pulse:
    alpha 1.0
    ease 0.85 alpha 0.35
    ease 0.85 alpha 1.0
    repeat

transform kd_news_ticker_motion:
    subpixel True
    xanchor 0.0
    xpos 1.0
    linear 22.0 xpos 0.0 xanchor 1.0
    repeat

transform kd_news_close_motion:
    alpha 0.0
    easeout 0.17 alpha 1.0

transform kd_news_close_line:
    subpixel True
    yzoom 1.0
    easein 0.20 yzoom 0.012
    easein 0.12 xzoom 0.0 alpha 0.0

style kd_news_text is default:
    font gui.text_font
    color "#edf5ff"
    outlines []
    size 32

style kd_news_title is kd_news_text:
    bold True
    size 45

style kd_news_small is kd_news_text:
    size 26

screen kd_news_intro(channel, topic, edition):
    zorder 450
    modal False

    add Solid("#060d18")
    add Solid("#324f69", xysize=(1920, 1080)) at kd_news_shutter xalign 0.5 yalign 0.5
    add "images/kd_news/intro_left.svg" at kd_news_intro_left
    add "images/kd_news/intro_right.svg" at kd_news_intro_right
    fixed:
        xysize (1920, 1080)
        at kd_news_intro_title
        add Solid("#68cde4", xysize=(90, 5)) xalign 0.5 ypos 360
        text channel style "kd_news_title" size 108 xalign 0.5 ypos 380
        text edition style "kd_news_small" color "#83ccdf" xalign 0.5 ypos 518
        add Solid("#617d96", xysize=(680, 2)) xalign 0.5 ypos 572
        text topic style "kd_news_title" xalign 0.5 ypos 600 xmaximum 1500 text_align 0.5

screen kd_news_broadcast(channel, location, headline, headlines=(), speaker="", detail=""):
    zorder 5
    modal False

    # Identité de chaîne, lieu et direct : pas de clignotement plein écran.
    fixed:
        xysize (1920, 1080)
        add Solid("#0a1726dd", xysize=(1920, 86)) xpos 0 ypos 0 at kd_news_drop
        add Solid("#4c91b4", xysize=(1920, 2)) xpos 0 ypos 86
        add "images/kd_news/channel_mark.svg" xpos 42 ypos 17
        text channel style "kd_news_title" size 38 xpos 111 ypos 18
        add Solid("#54758a", xysize=(2, 44)) xpos 425 ypos 21
        text location style "kd_news_small" xpos 452 ypos 27 xmaximum 1090
        fixed:
            xpos 1660
            ypos 18
            xysize (215, 50)
            at kd_news_drop
            add Solid("#b92d49", xysize=(215, 50))
            add "images/kd_news/live_dot.svg" xpos 17 ypos 14 at kd_news_live_pulse
            text _("DIRECT") style "kd_news_small" bold True xpos 52 yalign 0.5

        # Le bandeau principal et le fil restent hors de la textbox.
        fixed:
            xpos 42
            ypos 626
            xysize (1836, 125)
            at kd_news_slide(0.10)
            add Solid("#09182bee", xysize=(1836, 125))
            add Solid("#61bedb", xysize=(7, 125))
            text (speaker if speaker else _("ACTUALITÉS")) style "kd_news_small" color "#81d5eb" xpos 26 ypos 7 xmaximum 1760
            text headline style "kd_news_title" xpos 26 ypos 37 xmaximum 1760
            if detail:
                text detail style "kd_news_small" color "#b9d4e6" xpos 26 ypos 88 xmaximum 1760
        if headlines:
            fixed:
                xpos 42
                ypos 755
                xysize (1836, 39)
                add Solid("#e3edf5", xysize=(1836, 39))
                add Solid("#b92d49", xysize=(220, 39))
                text _("À LA UNE") style "kd_news_small" bold True xpos 14 yalign 0.5
                viewport:
                    xpos 220
                    ypos 0
                    xysize (1616, 39)
                    draggable False
                    mousewheel False
                    fixed:
                        xysize (1616, 39)
                        text "     •     ".join(headlines) style "kd_news_small" color "#172c40" layout "nobreak" yalign 0.5 at kd_news_ticker_motion

screen kd_news_outro():
    zorder 450
    modal False
    add Solid("#050a12") at kd_news_close_motion
    add Solid("#a7d0e1", xysize=(1920, 4)) xalign 0.5 yalign 0.5 at kd_news_close_line

label kd_news_open(channel, topic, edition):
    window hide
    if not renpy.is_skipping():
        show screen kd_news_intro(channel, topic, edition)
        $ renpy.pause(1.35)
        hide screen kd_news_intro
    return

label kd_news_close:
    window hide
    hide screen kd_news_broadcast
    if not renpy.is_skipping():
        show screen kd_news_outro
        $ renpy.pause(0.32)
        hide screen kd_news_outro
    window auto
    return
