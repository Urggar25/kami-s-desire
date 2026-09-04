# transform.rpy

transform char_active(xpos):
    xalign xpos yalign 1.0
    linear 0.15 zoom 1.15 alpha 1.0

transform char_inactive(xpos):
    xalign xpos yalign 1.0
    linear 0.15 zoom 1.0 alpha 0.4

transform char_idle(xpos):
    xalign xpos yalign 1.0
    zoom 1.0 alpha 1.0

transform char_group_fade_in(xpos):
    xalign xpos yalign 1.0
    zoom 1.0 alpha 0.0
    linear 0.35 alpha 1.0

transform char_group_enter(xpos, ypos=1.0):
    subpixel True
    xalign xpos
    yalign ypos
    alpha 0.0
    zoom 1.0
    yoffset 0
    linear 0.5 alpha 1.0

transform char_group_exit(xpos, ypos=1.0):
    subpixel True
    xalign xpos
    yalign ypos
    alpha 1.0
    zoom 1.0
    yoffset 0
    linear 0.5 alpha 0.0


transform char_group_place(xpos, ypos=1.0):
    subpixel True
    xalign xpos
    yalign ypos
    alpha 1.0
    zoom 1.0
    yoffset 0

init python:

    GROUP_MAX_MEMBERS = 12
    GROUP_AUTO_X_MIN = -0.11
    GROUP_AUTO_X_MAX = 1.20
    GROUP_AUTO_X_MAX_SMALL = 1.10
    GROUP_AUTO_SMALL_MAX_MEMBERS = 5

    def _group_auto_x(count, index):
        if count <= 1:
            return 0.5
        max_x = GROUP_AUTO_X_MAX_SMALL if count <= GROUP_AUTO_SMALL_MAX_MEMBERS else GROUP_AUTO_X_MAX
        spacing = (max_x - GROUP_AUTO_X_MIN) / float(count - 1)
        return GROUP_AUTO_X_MIN + (spacing * float(index))

    def _group_member_tuple(member, count, index):
        tag = member[0]
        expr = member[1] if len(member) > 1 else "neutre"
        x = member[2] if len(member) > 2 else _group_auto_x(count, index)
        return tag, expr, x

    def showGroup(members, y=1.0, layer="master", zorder=0):
        """
        members : liste de tuples (tag, expr) ou (tag, expr, x)
        ex: showGroup([("lysa","neutre",0.15), ("julian","sourire",0.5)])
        """
        if len(members) > GROUP_MAX_MEMBERS:
            raise Exception("showGroup accepte au maximum 12 personnages.")

        normalized = []
        for i, member in enumerate(members):
            normalized.append(_group_member_tuple(member, min(len(members), GROUP_MAX_MEMBERS), i))

        next_tags = [tag for tag, expr, x in normalized]
        old_tags = list(getattr(store, "group_members", []))

        for tag in old_tags:
            if tag in next_tags:
                continue
            state = store.char_state.get(tag, {})
            old_layer = state.get("layer", layer)
            if not renpy.showing(tag, layer=old_layer):
                continue
            x = state.get("x", store.char_pos.get(tag, 0.5))
            expr = state.get("expr", "neutre")
            old_y = state.get("y", y)
            renpy.show(f"{tag} {expr}", tag=tag, at_list=[char_group_exit(x, old_y)], layer=old_layer)

        if any(tag not in next_tags for tag in old_tags):
            renpy.pause(0.5, hard=True)
            for tag in old_tags:
                if tag not in next_tags:
                    old_layer = store.char_state.get(tag, {}).get("layer", layer)
                    renpy.hide(tag, layer=old_layer)
                    store.char_pos.pop(tag, None)
                    store.char_state.pop(tag, None)

        for idx, (tag, expr, x) in enumerate(normalized):
            store.char_pos[tag] = x
            store.char_state[tag] = dict(expr=expr, x=x, y=y, layer=layer, zorder=zorder)
            renpy.show(f"{tag} {expr}", tag=tag, at_list=[char_group_enter(x, y)], layer=layer, zorder=zorder + idx)

        if normalized:
            renpy.pause(0.5, hard=True)
        store.group_members = next_tags

    def hideGroup():
        """Cache tous les personnages du groupe actuel avec fade out"""
        members = list(store.group_members)
        for tag in members:
            state = store.char_state.get(tag, {})
            layer = state.get("layer", "master")
            if renpy.showing(tag, layer=layer):
                x = state.get("x", store.char_pos.get(tag, 0.5))
                y = state.get("y", 1.0)
                expr = state.get("expr", "neutre")
                renpy.show(f"{tag} {expr}", tag=tag, at_list=[char_group_exit(x, y)], layer=layer)
        if members:
            renpy.pause(0.5, hard=True)
        for tag in members:
            layer = store.char_state.get(tag, {}).get("layer", "master")
            renpy.hide(tag, layer=layer)
            store.char_pos.pop(tag, None)
            store.char_state.pop(tag, None)
        store.group_members = []

    def on_speaking(event, interact, **kwargs):
        if event != "begin":
            return

        speaker = renpy.get_say_image_tag()
        members = getattr(store, "group_members", [])

        if not members:
            return

        if speaker is None:
            for tag in members:
                if tag in store.char_pos:
                    x = store.char_pos[tag]
                    renpy.show(tag, at_list=[char_idle(x)])
            return

        if speaker not in members:
            return

        for tag in members:
            if tag not in store.char_pos:
                continue
            x = store.char_pos[tag]
            if tag == speaker:
                renpy.show(tag, at_list=[char_active(x)])
            else:
                renpy.show(tag, at_list=[char_inactive(x)])

    # NOTE: système legacy remplacé par l'autofocus de script.rpy.
    # Ne PAS enregistrer on_speaking dans config.all_character_callbacks
    # (l'ancien code s'auto-réappendait à chaque ligne -> fuite).

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

transform day_card_slam:
    alpha 0.0
    zoom 1.6
    easein 0.30 alpha 1.0 zoom 1.0
    easeout 0.08 zoom 1.05
    easein 0.10 zoom 1.0

transform day_card_line_grow:
    xzoom 0.0
    pause 0.35
    easeout 0.45 xzoom 1.0

screen day_transition_card(day_label):
    zorder 100

    add Solid("#000")

    vbox:
        align (0.5, 0.5)
        spacing 16

        text "— CONCLAVE —" at day_card_line_grow:
            xalign 0.5
            size 26
            color "#5cd3ff"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 10

        text "Day [day_label]" at day_card_slam:
            xalign 0.5
            size 110
            color "#FFFFFF"
            font "fonts/day_font.ttf"
            outlines [(4, "#0a1626", 0, 0)]

        add Solid("#5cd3ff", xysize=(600, 2)) xalign 0.5 at day_card_line_grow

screen chapter_transition_card(chapter_status, chapter_title):
    zorder 120
    modal True

    add Solid("#000")
    timer 5.0 action Return()

    vbox:
        align (0.5, 0.5)
        spacing 18

        text "— CONCLAVE —" at day_card_line_grow:
            xalign 0.5
            size 26
            color "#5cd3ff"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 10

        text kd_tr(chapter_status) at day_card_slam:
            xalign 0.5
            size 48
            color "#9FE7FF"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 4
            outlines [(2, "#0a1626", 0, 0)]

        add Solid("#5cd3ff", xysize=(720, 2)) xalign 0.5 at day_card_line_grow

        text kd_tr(chapter_title):
            xalign 0.5
            size 64
            color "#FFFFFF"
            font "fonts/day_font.ttf"
            outlines [(4, "#0a1626", 0, 0)]
            text_align 0.5

label show_chapter_title(chapter_status, chapter_title):

    scene black with fade
    play sound "audio/sfx_day_transition.wav"

    call screen chapter_transition_card(chapter_status, chapter_title)
    with Dissolve(0.4)

    return

label end_day(next_day):

    stop music fadeout 1.0
    scene black with fade

    play sound "audio/sfx_day_transition.wav"

    $ renpy.show_screen("day_transition_card", day_label=str(next_day))
    $ renpy.pause(4.0)
    $ renpy.hide_screen("day_transition_card")
    with Dissolve(0.4)

    $ current_day = day_number(next_day)
    return

label show_custom_title(title_text="Temps libre"):

    play sound "audio/sfx_kami_alert.wav"
    scene black
    $ translated_title_text = kd_tr(title_text)
    show expression Text(translated_title_text, size=84, color="#FFFFFF", font="fonts/day_font.ttf") as custom_title_card at truecenter
    pause 5.0
    hide custom_title_card
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

    timer 5.0 action Hide("day_transition")

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

    timer 5.0 action Hide("free_time_transition")

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

screen custom_title(title_text="Temps libre"):

    modal True
    zorder 100

    add Solid("#000")

    timer 5.0 action Hide("custom_title")

    frame:
        background None
        xalign 0.5
        yalign 0.5

        vbox at day_fade_5s:
            spacing 12
            xalign 0.5

            text title_text:
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

# Les modèles de personnages partagent un canevas proche de 1024x1536 et
# incluent déjà leur échelle dans images.rpy. Ce cadrage commun évite donc
# que les anciens réglages prévus pour les PNG coupent la tête du portrait.
default broadcast_px = -130
default broadcast_py = -10
default broadcast_pz = 1.18

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

        portrait = character_image(store.broadcast_char, store.broadcast_expr)

        d = Viewport(
            child=Transform(
                portrait,
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

        # px/py/pz restent acceptés pour ne pas casser les anciens appels,
        # mais les portraits composés ont désormais tous le même gros plan.
        # Le cadrage centre le visage et le haut du buste dans la diffusion.
        store.broadcast_px = -130
        store.broadcast_py = -10
        store.broadcast_pz = 1.18

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
    $ broadcast_px = -130
    $ broadcast_py = -10
    $ broadcast_pz = 1.18

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
