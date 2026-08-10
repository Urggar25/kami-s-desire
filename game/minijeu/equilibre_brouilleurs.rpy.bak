# Mini-jeu J12 - Le Fil d'Equilibre 2.0

default j12011_balance_placements = {}
default j12011_revealed_args = []
default j12011_countered_shadows = []
default j12011_active_shadows = []
default j12011_paranoia = 18.0
default j12011_balance_integrity = 100.0
default j12011_hold_focus = None
default j12011_hold_progress = 0.0
default j12011_wire_feedback = "Place les arguments. La balance reagit a chaque poids."
default j12011_wire_breaks = 0
default j12011_wire_result = None
default j12011_wire_score = 0
default j12011_kael_convinced = False
default j12011_noam_debate_path = None

init python:
    import math

    J12011_TICK = 0.20
    J12011_MAX_BALANCE = 92.0
    J12011_REVEAL_TIME = 1.05

    J12011_ARGS = {
        "mara": {
            "speaker": "Mara",
            "official": "J'en peux plus d'etre observee !",
            "shadow": "... et ca arrange bien quelqu'un qui veut agir sans etre vu.",
            "weight": 24,
            "shadow_weight": 30,
            "paranoia": 10,
            "x": 76,
            "y": 772,
        },
        "tomas": {
            "speaker": "Tomas",
            "official": "Sans surveillance, on ne pourra plus rien prouver.",
            "shadow": "... et sans preuve, on accusera au hasard.",
            "weight": 28,
            "shadow_weight": 34,
            "paranoia": 13,
            "x": 430,
            "y": 772,
        },
        "kael": {
            "speaker": "Kael",
            "official": "J'ai besoin de savoir qui m'a vole.",
            "shadow": "... sinon je finirai par soupconner tout le monde.",
            "weight": 32,
            "shadow_weight": 38,
            "paranoia": 16,
            "x": 784,
            "y": 772,
        },
        "ryn": {
            "speaker": "Ryn",
            "official": "La liberte avant tout.",
            "shadow": "... meme si l'ombre avale le reste.",
            "weight": 30,
            "shadow_weight": 40,
            "paranoia": 18,
            "x": 1138,
            "y": 772,
        },
        "nyra": {
            "speaker": "Nyra",
            "official": "Il faut trouver un juste milieu.",
            "shadow": "... mais un milieu peut juste cacher une peur.",
            "weight": 18,
            "shadow_weight": 25,
            "paranoia": 8,
            "x": 1492,
            "y": 772,
        },
    }

    J12011_SHADOW_POOL = [
        {"id": "dg_free", "text": "Le Doppelganger agit hors champ.", "side": "freedom", "weight": 24},
        {"id": "kami_all", "text": "Kami voit ce que Noam cache.", "side": "security", "weight": 24},
        {"id": "false_proof", "text": "Une preuve peut etre fabriquee.", "side": "security", "weight": 18},
        {"id": "dead_angle", "text": "Un angle mort devient une arme.", "side": "freedom", "weight": 20},
    ]

    def j12011_balance_reset():
        store.j12011_balance_placements = dict((arg_id, None) for arg_id in J12011_ARGS.keys())
        store.j12011_revealed_args = []
        store.j12011_countered_shadows = []
        store.j12011_active_shadows = []
        store.j12011_paranoia = 18.0
        store.j12011_balance_integrity = 100.0
        store.j12011_hold_focus = None
        store.j12011_hold_progress = 0.0
        store.j12011_wire_feedback = "Place les arguments. La balance reagit a chaque poids."
        store.j12011_wire_breaks = 0
        store.j12011_wire_result = None
        store.j12011_wire_score = 0
        store.j12011_kael_convinced = False
        store.j12011_noam_debate_path = None
        renpy.block_rollback()

    def j12011_arg_weight(arg_id):
        data = J12011_ARGS[arg_id]
        return data["shadow_weight"] if arg_id in store.j12011_revealed_args else data["weight"]

    def j12011_arg_text(arg_id):
        data = J12011_ARGS[arg_id]
        return data["shadow"] if arg_id in store.j12011_revealed_args else data["official"]

    def j12011_arg_skin(arg_id, hovered=False):
        if arg_id in store.j12011_revealed_args:
            return "gui/day12/wire_debate/arg_bubble_revealed.png"
        if hovered:
            return "gui/day12/wire_debate/arg_bubble_hover.png"
        return "gui/day12/wire_debate/arg_bubble.png"

    def j12011_side_sign(side):
        if side == "security":
            return -1
        if side == "freedom":
            return 1
        return 0

    def j12011_balance_raw():
        total = 0.0
        for arg_id, side in store.j12011_balance_placements.items():
            total += j12011_side_sign(side) * j12011_arg_weight(arg_id)
        for shadow in store.j12011_active_shadows:
            total += j12011_side_sign(shadow.get("side")) * shadow.get("weight", 0)
        return total

    def j12011_balance_score():
        raw = j12011_balance_raw()
        return max(-100.0, min(100.0, raw / J12011_MAX_BALANCE * 100.0))

    def j12011_placed_count():
        return sum(1 for side in store.j12011_balance_placements.values() if side is not None)

    def j12011_card_xy(arg_id):
        side = store.j12011_balance_placements.get(arg_id)
        if side is None:
            data = J12011_ARGS[arg_id]
            return (data["x"], data["y"])

        same_side = [aid for aid in J12011_ARGS.keys() if store.j12011_balance_placements.get(aid) == side]
        index = same_side.index(arg_id) if arg_id in same_side else 0
        if side == "security":
            return (270 + (index % 2) * 178, 392 + (index // 2) * 116)
        return (1302 + (index % 2) * 178, 392 + (index // 2) * 116)

    def j12011_place_argument(arg_id, side):
        previous = store.j12011_balance_placements.get(arg_id)
        store.j12011_balance_placements[arg_id] = side
        if side is None:
            store.j12011_wire_feedback = "%s revient dans la reserve mentale." % J12011_ARGS[arg_id]["speaker"]
        else:
            delta = J12011_ARGS[arg_id]["paranoia"]
            if arg_id in store.j12011_revealed_args:
                delta += 12
            if previous is not None and previous != side:
                delta += 7
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + delta)
            label = "Securite" if side == "security" else "Liberte"
            store.j12011_wire_feedback = "%s pese cote %s." % (J12011_ARGS[arg_id]["speaker"], label)
            renpy.play("audio/sfx_beep.mp3", channel="sound")
        j12011_apply_balance_pressure()
        renpy.restart_interaction()

    def j12011_argument_drop(arg_id, drags, drop):
        if drop is None:
            renpy.restart_interaction()
            return
        target = getattr(drop, "drag_name", "")
        if target == "j12011_drop_security":
            j12011_place_argument(arg_id, "security")
        elif target == "j12011_drop_freedom":
            j12011_place_argument(arg_id, "freedom")
        elif target == "j12011_drop_bank":
            j12011_place_argument(arg_id, None)
        else:
            renpy.restart_interaction()

    def j12011_start_hold(arg_id):
        if arg_id in store.j12011_revealed_args:
            store.j12011_wire_feedback = "La part d'ombre de %s est deja visible." % J12011_ARGS[arg_id]["speaker"]
            return
        store.j12011_hold_focus = arg_id
        store.j12011_hold_progress = 0.0
        store.j12011_wire_feedback = "Garde le pointeur sur l'oeil. Noam force la pensee."
        renpy.restart_interaction()

    def j12011_stop_hold(arg_id):
        if store.j12011_hold_focus == arg_id:
            store.j12011_hold_focus = None
            store.j12011_hold_progress = 0.0
            renpy.restart_interaction()

    def j12011_reveal_arg(arg_id):
        if arg_id not in store.j12011_revealed_args:
            store.j12011_revealed_args.append(arg_id)
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 18 + J12011_ARGS[arg_id]["paranoia"])
            store.j12011_wire_feedback = J12011_ARGS[arg_id]["shadow"]
            renpy.play("audio/sfx_gresillement.mp3", channel="sound")
        store.j12011_hold_focus = None
        store.j12011_hold_progress = 0.0
        j12011_apply_balance_pressure()
        renpy.restart_interaction()

    def j12011_shadow_key(shadow):
        return "%s_%s" % (shadow.get("id"), shadow.get("serial", 0))

    def j12011_spawn_shadow(forced_side=None):
        if len(store.j12011_active_shadows) >= 3:
            return
        choices = [dict(item) for item in J12011_SHADOW_POOL]
        if forced_side:
            choices = [item for item in choices if item["side"] == forced_side] or choices
        shadow = renpy.random.choice(choices)
        serial = renpy.random.randint(1000, 9999)
        shadow["serial"] = serial
        shadow["timer"] = 4.8 if store.j12011_paranoia < 85 else 3.5
        shadow["x"] = renpy.random.randint(690, 1040)
        shadow["y"] = renpy.random.randint(220, 650)
        store.j12011_active_shadows.append(shadow)
        store.j12011_wire_feedback = "Une ombre accroche la balance. Clique-la vite."
        renpy.play("audio/sfx_gresillement.mp3", channel="sound")

    def j12011_counter_shadow(serial):
        remaining = []
        found = None
        for shadow in store.j12011_active_shadows:
            if shadow.get("serial") == serial:
                found = shadow
            else:
                remaining.append(shadow)
        store.j12011_active_shadows = remaining
        if found:
            store.j12011_countered_shadows.append(found.get("id"))
            store.j12011_paranoia = max(0.0, store.j12011_paranoia - 18.0)
            store.j12011_balance_integrity = min(100.0, store.j12011_balance_integrity + 5.0)
            store.j12011_wire_feedback = "Ombre repoussee. La balance respire."
            renpy.play("audio/sfx_beep.mp3", channel="sound")
        renpy.restart_interaction()

    def j12011_apply_balance_pressure():
        score = abs(j12011_balance_score())
        if score > 82:
            store.j12011_balance_integrity = max(0.0, store.j12011_balance_integrity - 16.0)
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 10.0)
            store.j12011_wire_feedback = "La balance tremble. Trop extreme."
        elif score > 62:
            store.j12011_balance_integrity = max(0.0, store.j12011_balance_integrity - 7.0)
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 5.0)

        if store.j12011_balance_integrity <= 0.0:
            j12011_break_balance()

    def j12011_break_balance():
        store.j12011_wire_breaks += 1
        store.j12011_balance_placements = dict((arg_id, None) for arg_id in J12011_ARGS.keys())
        store.j12011_active_shadows = []
        store.j12011_balance_integrity = 74.0
        store.j12011_paranoia = min(100.0, store.j12011_paranoia + 12.0)
        store.j12011_wire_feedback = "La balance rompt. Noam repart de zero."
        renpy.play("audio/sfx_drop.mp3", channel="sound")

    def j12011_tick():
        if store.j12011_hold_focus:
            store.j12011_hold_progress += J12011_TICK
            if store.j12011_hold_progress >= J12011_REVEAL_TIME:
                j12011_reveal_arg(store.j12011_hold_focus)
                return

        score = abs(j12011_balance_score())
        if score > 82:
            store.j12011_balance_integrity = max(0.0, store.j12011_balance_integrity - 2.6)
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 1.3)
        elif score > 62:
            store.j12011_balance_integrity = max(0.0, store.j12011_balance_integrity - 0.9)
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 0.5)
        else:
            store.j12011_balance_integrity = min(100.0, store.j12011_balance_integrity + 0.7)
            store.j12011_paranoia = max(0.0, store.j12011_paranoia - 0.25)

        expired = []
        for shadow in store.j12011_active_shadows:
            shadow["timer"] -= J12011_TICK
            if shadow["timer"] <= 0.0:
                expired.append(shadow)

        if expired:
            store.j12011_active_shadows = [shadow for shadow in store.j12011_active_shadows if shadow not in expired]
            store.j12011_paranoia = min(100.0, store.j12011_paranoia + 10.0 * len(expired))
            store.j12011_balance_integrity = max(0.0, store.j12011_balance_integrity - 14.0 * len(expired))
            store.j12011_wire_feedback = "Une ombre a pese trop longtemps."

        if store.j12011_balance_integrity <= 0.0:
            j12011_break_balance()
            renpy.restart_interaction()
            return

        if store.j12011_paranoia >= 72.0 and len(store.j12011_active_shadows) == 0:
            side = "freedom" if j12011_balance_score() >= 0 else "security"
            j12011_spawn_shadow(side)
            renpy.restart_interaction()

    def j12011_can_validate():
        return j12011_placed_count() >= 4 and len(store.j12011_active_shadows) == 0 and store.j12011_balance_integrity > 25.0

    def j12011_finalize_result():
        score = int(round(j12011_balance_score()))
        store.j12011_wire_score = score

        if score < -12:
            store.j12011_wire_result = "security"
        elif score > 12:
            store.j12011_wire_result = "freedom"
        else:
            security_weight = sum(j12011_arg_weight(arg_id) for arg_id, side in store.j12011_balance_placements.items() if side == "security")
            freedom_weight = sum(j12011_arg_weight(arg_id) for arg_id, side in store.j12011_balance_placements.items() if side == "freedom")
            store.j12011_wire_result = "security" if security_weight >= freedom_weight else "freedom"

        store.j12011_anchored_nodes = [arg_id for arg_id, side in store.j12011_balance_placements.items() if side is not None]
        store.j12011_shadow_nodes = list(store.j12011_revealed_args) + list(store.j12011_countered_shadows)
        store.j12011_kael_convinced = (
            store.j12011_wire_result == "security"
            and store.j12011_balance_placements.get("kael") == "security"
        )
        renpy.block_rollback()
        return {
            "result": store.j12011_wire_result,
            "score": store.j12011_wire_score,
            "anchored": list(store.j12011_anchored_nodes),
            "shadows": list(store.j12011_shadow_nodes),
            "kael_convinced": store.j12011_kael_convinced,
        }

    def j12011_result_title():
        if store.j12011_wire_result == "security":
            return "Positionnement personnel : securite"
        return "Positionnement personnel : liberte"

    def j12011_result_body():
        if store.j12011_wire_result == "security":
            return "Noam defendra les preuves et un cadre dur contre les brouilleurs."
        return "Noam acceptera d'autoriser les brouilleurs, meme avec des zones d'ombre."

    def j12011_result_image():
        if store.j12011_wire_result == "security":
            return "gui/day12/wire_debate/consequence_security.png"
        if store.j12011_wire_result == "freedom":
            return "gui/day12/wire_debate/consequence_freedom.png"
        return "gui/day12/wire_debate/consequence_mixed.png"

    class J12011BalanceDisplay(renpy.Displayable):
        def __init__(self, **kwargs):
            super(J12011BalanceDisplay, self).__init__(**kwargs)

        def render(self, width, height, st, at):
            render = renpy.Render(1920, 1080)
            canvas = render.canvas()
            score = j12011_balance_score()
            tilt = max(-18.0, min(18.0, score * 0.18))
            cx = 960
            cy = 468
            length = 820
            radians = tilt * 3.14159 / 180.0
            dx = int((length / 2.0) * math.cos(radians))
            dy = int((length / 2.0) * math.sin(radians))
            left = (cx - dx, cy - dy)
            right = (cx + dx, cy + dy)

            if abs(score) > 78:
                shake = renpy.random.randint(-5, 5)
                left = (left[0] + shake, left[1])
                right = (right[0] - shake, right[1])

            canvas.line("#102635", (cx, cy + 28), (cx, 682), 16)
            canvas.line("#7defff", left, right, 12)
            canvas.line("#ffffff", left, right, 3)
            canvas.line("#58d8ff", left, (left[0] - 78, left[1] + 130), 4)
            canvas.line("#58d8ff", left, (left[0] + 78, left[1] + 130), 4)
            canvas.line("#ff516b", right, (right[0] - 78, right[1] + 130), 4)
            canvas.line("#ff516b", right, (right[0] + 78, right[1] + 130), 4)
            canvas.line("#c8fbff", (cx - 38, cy + 28), (cx + 38, cy + 28), 8)
            canvas.circle("#dffcff", (cx, cy), 22)
            canvas.circle("#08121f", (cx, cy), 10)

            return render

transform j12011_pulse:
    alpha 0.82
    linear 0.70 alpha 1.0
    linear 0.70 alpha 0.82
    repeat

transform j12011_warning_pulse:
    alpha 0.30
    linear 0.25 alpha 0.78
    linear 0.25 alpha 0.30
    repeat

transform j12011_card_float:
    yoffset 0
    linear 1.35 yoffset -5
    linear 1.35 yoffset 0
    repeat

style j12011_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 42
    color "#eefbff"
    outlines [(3, "#000000c8", 0, 0)]

style j12011_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 26
    color "#e9fbff"
    outlines [(2, "#020813", 0, 0)]

style j12011_small:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 21
    color "#aeefff"
    outlines [(2, "#020813", 0, 0)]

style j12011_button:
    background Solid("#102434e0")
    hover_background Solid("#1d4d68f0")
    insensitive_background Solid("#15182090")
    xpadding 20
    ypadding 10

style j12011_button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 25
    color "#f1fdff"
    insensitive_color "#768690"

screen j12011_wire_debate():
    modal True
    zorder 260
    default hovered_arg = None

    timer J12011_TICK repeat True action Function(j12011_tick)

    $ balance_score = j12011_balance_score()
    $ abs_balance = abs(balance_score)
    $ paranoia_height = int(584 * max(0.0, min(100.0, j12011_paranoia)) / 100.0)
    $ integrity_width = int(420 * max(0.0, min(100.0, j12011_balance_integrity)) / 100.0)

    add "gui/day12/wire_debate/bg_thread_chamber.png"
    add J12011BalanceDisplay()
    add "gui/day12/wire_debate/scanlines.png"
    add "gui/day12/wire_debate/vignette.png"

    if abs_balance > 78 or j12011_paranoia > 84:
        add "gui/day12/wire_debate/rupture_warning.png" at j12011_warning_pulse

    frame:
        xpos 74
        ypos 44
        xsize 1570
        ysize 92
        background Solid("#06111dcc")
        padding (22, 12)
        hbox:
            spacing 24
            text "LE FIL D'EQUILIBRE" style "j12011_title"
            text "Place les poids. Contre les ombres. Valide quand Noam tient debout." style "j12011_small" yalign 0.58

    frame:
        xpos 690
        ypos 148
        xsize 650
        background Solid("#06111de0")
        padding (18, 12)
        vbox:
            spacing 8
            text "[j12011_wire_feedback]" style "j12011_text" xalign 0.5 text_align 0.5
            hbox:
                xalign 0.5
                spacing 22
                text "Equilibre [int(balance_score)]" style "j12011_small"
                text "Arguments [j12011_placed_count()]/5" style "j12011_small"
                text "Ruptures [j12011_wire_breaks]" style "j12011_small"

    add "gui/day12/wire_debate/plate_security.png":
        xpos 215
        ypos 518
    add "gui/day12/wire_debate/plate_freedom.png":
        xpos 1275
        ypos 518

    text "SECURITE" style "j12011_title" color "#75d8ff":
        xpos 285
        ypos 306
    text "LIBERTE" style "j12011_title" color "#ff6678":
        xpos 1372
        ypos 306

    frame:
        xpos 720
        ypos 666
        xsize 460
        ysize 34
        background Solid("#0c1621e0")
        padding (10, 8)
        fixed:
            xfill True
            yfill True
            add Solid("#1b3140", xsize=420, ysize=12):
                xpos 0
                ypos 0
            add Solid("#7dffca" if j12011_balance_integrity > 45 else "#ff5b72", xsize=integrity_width, ysize=12):
                xpos 0
                ypos 0

    add "gui/day12/wire_debate/paranoia_frame.png":
        xpos 1736
        ypos 156
    add Solid("#ff4868cc", xsize=38, ysize=paranoia_height):
        xpos 1771
        ypos (760 - paranoia_height)

    draggroup:
        drag:
            drag_name "j12011_drop_security"
            xpos 150
            ypos 230
            xsize 620
            ysize 520
            draggable False
            droppable True

        drag:
            drag_name "j12011_drop_freedom"
            xpos 1150
            ypos 230
            xsize 620
            ysize 520
            draggable False
            droppable True

        drag:
            drag_name "j12011_drop_bank"
            xpos 40
            ypos 738
            xsize 1680
            ysize 220
            draggable False
            droppable True

        for arg_id, data in J12011_ARGS.items():
            $ card_x, card_y = j12011_card_xy(arg_id)
            $ card_hover = hovered_arg == arg_id
            drag:
                drag_name ("j12011_arg_%s" % arg_id)
                xpos card_x
                ypos card_y
                xsize 330
                ysize 132
                draggable True
                droppable False
                dragged (lambda drags, drop, aid=arg_id: j12011_argument_drop(aid, drags, drop))
                hovered SetScreenVariable("hovered_arg", arg_id)
                unhovered SetScreenVariable("hovered_arg", None)

                fixed:
                    xsize 330
                    ysize 132
                    at j12011_card_float
                    add j12011_arg_skin(arg_id, card_hover)
                    text data["speaker"]:
                        xpos 24
                        ypos 14
                        style "j12011_small"
                        color "#ffffff"
                    text j12011_arg_text(arg_id):
                        xpos 24
                        ypos 42
                        xsize 276
                        style "j12011_small"
                        color "#ffffff"
                    text ("%d" % j12011_arg_weight(arg_id)):
                        xpos 278
                        ypos 84
                        style "j12011_small"
                        color "#ffffff"

    for arg_id, data in J12011_ARGS.items():
        $ card_x, card_y = j12011_card_xy(arg_id)
        button:
            xpos card_x + 270
            ypos card_y + 12
            xsize 42
            ysize 30
            background Solid("#06111dcc")
            hover_background Solid("#6a1430dd")
            action NullAction()
            hovered Function(j12011_start_hold, arg_id)
            unhovered Function(j12011_stop_hold, arg_id)
            text "oeil":
                style "j12011_small"
                size 16
                xalign 0.5
                yalign 0.5

    if j12011_hold_focus:
        frame:
            xpos 720
            ypos 714
            xsize 460
            background Solid("#160812e8")
            padding (16, 10)
            vbox:
                spacing 6
                text "Scrutation : [J12011_ARGS[j12011_hold_focus]['speaker']]" style "j12011_small" xalign 0.5
                add Solid("#ff5b72", xsize=int(420 * min(1.0, j12011_hold_progress / J12011_REVEAL_TIME)), ysize=8):
                    xalign 0.5

    for shadow in j12011_active_shadows:
        $ serial = shadow["serial"]
        imagebutton:
            idle "gui/day12/wire_debate/shadow_bubble.png"
            hover "gui/day12/wire_debate/shadow_bubble.png"
            xpos shadow["x"]
            ypos shadow["y"]
            at j12011_warning_pulse
            action Function(j12011_counter_shadow, serial)

        frame:
            xpos shadow["x"] + 24
            ypos shadow["y"] + 26
            xsize 286
            background None
            vbox:
                spacing 4
                text shadow["text"] style "j12011_small" color "#ffe3e8" text_align 0.5 xalign 0.5
                text ("%.1fs" % shadow["timer"]) style "j12011_small" color "#ffffff" xalign 0.5

    hbox:
        xalign 0.5
        yalign 0.975
        spacing 22
        textbutton "Provoquer une ombre":
            action Function(j12011_spawn_shadow)
            style "j12011_button"
            text_style "j12011_button_text"
        textbutton "Repartir de zero":
            action Function(j12011_balance_reset)
            style "j12011_button"
            text_style "j12011_button_text"
        textbutton "Valider ce positionnement":
            sensitive j12011_can_validate()
            action Return(j12011_finalize_result())
            style "j12011_button"
            text_style "j12011_button_text"

screen j12011_wire_result_screen(result_data):
    modal True
    zorder 270

    add "gui/day12/wire_debate/bg_thread_chamber.png"
    add "gui/day12/wire_debate/scanlines.png"
    add "gui/day12/wire_debate/vignette.png"

    frame:
        xalign 0.5
        yalign 0.18
        xsize 1300
        background Solid("#06111de8")
        padding (26, 18)
        vbox:
            spacing 10
            text j12011_result_title() style "j12011_title" xalign 0.5
            text j12011_result_body() style "j12011_text" xalign 0.5 text_align 0.5

    add j12011_result_image():
        xalign 0.5
        yalign 0.56

    frame:
        xalign 0.5
        yalign 0.82
        xsize 1180
        background Solid("#07101ce0")
        padding (22, 16)
        vbox:
            spacing 8
            if store.j12011_wire_result == "security":
                text "Zones d'ombre reduites. Risque Doppelganger contenu. Intimite quasiment nulle." style "j12011_text" xalign 0.5 text_align 0.5
                if store.j12011_kael_convinced:
                    text "Kael a un point d'appui : son besoin de preuve." style "j12011_small" xalign 0.5
            else:
                text "Zones d'ombre plus larges. Risque Doppelganger accru. Kami perd du terrain." style "j12011_text" xalign 0.5 text_align 0.5
                text "Noam accepte que certaines preuves disparaissent avec l'air qu'il respire." style "j12011_small" xalign 0.5

    textbutton "Retour au debat":
        xalign 0.5
        yalign 0.94
        action Return(result_data)
        style "j12011_button"
        text_style "j12011_button_text"

label j12011_play_wire_debate:
    $ j12011_balance_reset()
    play sound "audio/sfx_minigame_start.mp3"
    $ j12011_wire_data = renpy.call_screen("j12011_wire_debate")
    $ renpy.call_screen("j12011_wire_result_screen", result_data=j12011_wire_data)
    return j12011_wire_data
