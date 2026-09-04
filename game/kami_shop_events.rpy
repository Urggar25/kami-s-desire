# ============================================================
# BOUTIQUE TEMPORAIRE & ÉVÈNEMENTS — KAMI HUD
# ============================================================

default persistent.desire_shards = 0
default persistent.desire_shards_zero_default_migrated = False
default persistent.desire_reward_claims = []
default persistent.kami_shop_owned = []

define KAMI_SHOP_ITEMS = (
    {
        "id": "iris_tenue2", "name": "IRIS : TENUE 2", "price": 100,
        "icon": "images/character/iris/portrait.png", "profile_id": "iris",
        "cosmetic_type": "outfit", "cosmetic_id": "tenue2",
    },
    {
        "id": "ryn_tenue2", "name": "RYN : TENUE 2", "price": 100,
        "icon": "images/character/ryn/portrait.png", "profile_id": "ryn",
        "cosmetic_type": "outfit", "cosmetic_id": "tenue2",
    },
    {
        "id": "lysa_accessoire1", "name": "LYSA : ACCESSOIRE 1", "price": 25,
        "icon": "images/character/lysa/portrait.png", "profile_id": "lysa",
        "cosmetic_type": "accessory", "cosmetic_id": "accessoire1",
    },
)

init python:
    import datetime
    import re

    # Le 6 septembre est inclus : l'évènement expire au passage au 7.
    CHAPTER_2_BOOST_END_AT = datetime.datetime(2026, 9, 7, 0, 0, 0)

    # Migration unique depuis la première version de la boutique, dont le
    # solde initial était 240. Un solde déjà utilisé ou gagné est conservé.
    if not persistent.desire_shards_zero_default_migrated:
        if persistent.desire_shards == 240 and not (persistent.kami_shop_owned or []):
            persistent.desire_shards = 0
        persistent.desire_shards_zero_default_migrated = True
        renpy.save_persistent()

    def kami_add_desire_shards(amount, notify=True):
        if persistent.desire_shards is None:
            persistent.desire_shards = 0
        persistent.desire_shards = max(0, int(persistent.desire_shards) + int(amount))
        renpy.save_persistent()
        if notify:
            prefix = "+" if amount >= 0 else ""
            renpy.notify(kd_tr("{}{} Éclats de désir").format(prefix, amount))
        renpy.restart_interaction()

    def kami_grant_desire_reward(reward_id, amount, notify=True):
        """Crédite une récompense persistante une seule fois."""
        claims = set(persistent.desire_reward_claims or [])
        reward_id = str(reward_id)
        if reward_id in claims:
            return 0

        amount = max(0, int(amount))
        claims.add(reward_id)
        persistent.desire_reward_claims = sorted(claims)
        if persistent.desire_shards is None:
            persistent.desire_shards = 0
        persistent.desire_shards = max(0, int(persistent.desire_shards) + amount)
        renpy.save_persistent()

        if notify and amount:
            renpy.notify(kd_tr("+{} Éclats de désir").format(amount))
        renpy.restart_interaction()
        return amount

    def kami_grant_chapter_1_ending_reward(ending_id):
        return kami_grant_desire_reward("chapter_1_ending_{}".format(ending_id), 10)

    def kami_chapter_2_reward_is_boosted(now=None):
        now = now or datetime.datetime.now()
        return now < CHAPTER_2_BOOST_END_AT

    def kami_grant_chapter_2_reward():
        amount = 40 if kami_chapter_2_reward_is_boosted() else 10
        return kami_grant_desire_reward("chapter_2_complete", amount)

    def kami_shop_owns(item_id):
        return item_id in (persistent.kami_shop_owned or [])

    def kami_shop_item_by_id(item_id):
        for item in KAMI_SHOP_ITEMS:
            if item["id"] == item_id:
                return item
        return None

    def kami_buy_item(item_id):
        item = kami_shop_item_by_id(item_id)
        if item is None:
            renpy.notify(kd_tr("Réquisition introuvable"))
            return
        price = int(item["price"])
        if persistent.kami_shop_owned is None:
            persistent.kami_shop_owned = []
        if kami_shop_owns(item_id):
            renpy.notify(kd_tr("Objet déjà obtenu"))
            return
        if persistent.desire_shards < price:
            renpy.notify(kd_tr("Éclats de désir insuffisants"))
            return
        persistent.desire_shards -= price
        persistent.kami_shop_owned.append(item_id)

        profile_id = item.get("profile_id")
        cosmetic_type = item.get("cosmetic_type")
        cosmetic_id = item.get("cosmetic_id")
        if profile_id and cosmetic_type == "outfit":
            unlock_profile_skin(profile_id, cosmetic_id)
        elif profile_id and cosmetic_type == "accessory":
            unlock_profile_accessory(profile_id, cosmetic_id)

        renpy.save_persistent()
        renpy.notify(kd_tr("Réquisition validée"))
        renpy.restart_interaction()

    def kami_random_preview_recipe(profile_id):
        prefix = "images/character/{}/".format(profile_id)
        component_names = {"arms": [], "mouths": [], "eyes": []}

        for filepath in renpy.list_files():
            if not filepath.startswith(prefix) or not filepath.endswith(".png"):
                continue
            asset_name = filepath[len(prefix):-4]
            if "/" in asset_name:
                continue
            if asset_name.startswith("bras_") and not re.search(r"_tenue\d+$", asset_name):
                component_names["arms"].append(asset_name)
            elif asset_name.startswith("bouche_"):
                component_names["mouths"].append(asset_name)
            elif asset_name.startswith("yeux_"):
                component_names["eyes"].append(asset_name)

        expression_map = getattr(store, "{}_EXPRESSIONS".format(profile_id.upper()), {})
        neutral = expression_map.get("neutre", ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"))
        return (
            renpy.random.choice(component_names["arms"] or [neutral[1]]),
            renpy.random.choice(component_names["mouths"] or [neutral[2]]),
            renpy.random.choice(component_names["eyes"] or [neutral[3]]),
        )

    def kami_shop_preview_displayable(item_id, recipe):
        item = kami_shop_item_by_id(item_id)
        if not item or not item.get("profile_id"):
            return None

        profile_id = item["profile_id"]
        outfit_id = get_profile_equipped_skin(profile_id)
        accessories = list(get_profile_equipped_accessories(profile_id))
        if item.get("cosmetic_type") == "outfit":
            outfit_id = item["cosmetic_id"]
        elif item.get("cosmetic_type") == "accessory" and item["cosmetic_id"] not in accessories:
            accessories.append(item["cosmetic_id"])

        return profile_cosmetic_preview(profile_id, outfit_id, accessories, recipe)

transform kami_hub_background:
    xalign 0.5
    yalign 0.5
    zoom 1.0

transform kami_hud_in(delay=0.0):
    alpha 0.0
    yoffset 14
    pause delay
    easeout 0.35 alpha 1.0 yoffset 0

transform kami_card_hover:
    on idle:
        matrixcolor BrightnessMatrix(0.0)
        yoffset 0
    on hover:
        matrixcolor BrightnessMatrix(0.12)
        yoffset -5
        ease 0.18


style kami_hub_title:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 64
    color "#f4f8fb"
    outlines [(2, "#020711", 0, 2)]
    kerning 5.0

style kami_hub_section:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 34
    color "#ff7040"
    kerning 2.0

style kami_hub_body:
    font "fonts/Barlow-Light.ttf"
    size 25
    color "#d7e5ed"
    line_spacing 3

style kami_hub_meta:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#51c6ff"
    kerning 1.5

style kami_hub_return is button:
    xsize 214
    ysize 72
    background Frame("gui/main_menu_kami/button_idle.png", 14, 14)
    hover_background Frame("gui/main_menu_kami/button_hover.png", 14, 14)
    padding (28, 12, 20, 12)

style kami_hub_return_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 28
    color "#dceaf2"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style kami_hub_action is button:
    xfill True
    ysize 62
    background Solid("#0a3348e8")
    hover_background Solid("#0d5672f5")
    insensitive_background Solid("#121c24dd")
    padding (18, 10, 18, 10)

style kami_hub_action_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 28
    color "#dff6ff"
    hover_color "#ffffff"
    insensitive_color "#5d7280"
    xalign 0.5
    yalign 0.5

style kami_event_row is button:
    xsize 540
    ysize 150
    background Solid("#061522e8")
    hover_background Solid("#0a2c40f2")
    selected_background Solid("#2a120be8")
    padding (18, 16, 18, 16)


screen kami_hub_header(title):
    textbutton _("RETOUR"):
        style "kami_hub_return"
        xpos 28
        ypos 28
        action ShowMenu("main_menu")

    text title:
        style "kami_hub_title"
        xalign 0.5
        ypos 34

    frame:
        xpos 1492
        ypos 28
        xsize 400
        ysize 76
        background Solid("#12051de8")
        padding (24, 8, 24, 8)

        hbox:
            spacing 18
            yalign 0.5
            add Transform("gui/main_menu_kami/glyph_kami.png", size=(44, 44), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
            text _("ÉCLATS DE DÉSIR") style "kami_hub_meta" color "#eedfff" yalign 0.5
            text "[persistent.desire_shards]" font "fonts/Rajdhani-SemiBold.ttf" size 38 color "#ffffff" yalign 0.5


screen kami_shop_item_card(item, card_index):
    $ item_id = item["id"]
    $ item_name = item["name"]
    $ price = item["price"]
    $ icon_path = item["icon"]
    $ is_owned = kami_shop_owns(item_id)
    $ is_cosmetic = item.get("profile_id") is not None

    frame:
        xsize 390
        ysize 560
        background Solid("#140b09ee")
        padding (3, 3, 3, 3)
        at kami_hud_in(card_index * 0.08)

        frame:
            background Solid("#090a0ded")
            padding (22, 22, 22, 22)

            vbox:
                spacing 10
                xfill True

                fixed:
                    xfill True
                    ysize 205
                    add Solid("#210d09")
                    if is_cosmetic:
                        add Transform(icon_path, fit="contain", xsize=210, ysize=210) xalign 0.5 yalign 0.5
                    else:
                        add Transform(icon_path, size=(150, 150), matrixcolor=TintMatrix("#ff8358")) xalign 0.5 yalign 0.5
                    add "gui/main_menu_kami/glyph_kami.png" xalign 0.5 yalign 0.5 alpha 0.18 zoom 0.34

                text kd_tr(item_name):
                    font "fonts/Rajdhani-SemiBold.ttf"
                    size 28
                    color "#f7ede8"
                    xalign 0.5
                    text_align 0.5
                    xsize 340

                frame:
                    xfill True
                    ysize 64
                    background Solid("#1d1110")
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14
                        add Transform("gui/main_menu_kami/glyph_kami.png", size=(36, 36), matrixcolor=TintMatrix("#b860ff")) yalign 0.5
                        text "[price]" font "fonts/Rajdhani-SemiBold.ttf" size 38 color "#ffffff"

                if is_cosmetic:
                    textbutton _("PRÉVISUALISER"):
                        style "kami_hub_action"
                        ysize 52
                        text_size 23
                        action Show("kami_shop_preview", item_id=item_id)
                else:
                    null height 52

                textbutton _("OBTENU" if is_owned else "OBTENIR"):
                    style "kami_hub_action"
                    ysize 58
                    sensitive not is_owned
                    action Function(kami_buy_item, item_id)


screen kami_shop_menu(initial_page=0):
    tag menu
    zorder 200
    modal True

    $ page_items = KAMI_SHOP_ITEMS

    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=0.8)
    on "hide" action Stop("music", fadeout=0.5)
    key "K_ESCAPE" action ShowMenu("main_menu")

    add "gui/main_menu_kami/bg_conclave_hub.png" at kami_hub_background
    add Solid("#02060ba8")
    add "gui/main_menu_kami/scanlines.png" alpha 0.22
    add "gui/main_menu_kami/vignette.png" alpha 0.72

    use kami_hub_header(_("RÉQUISITIONS DE KAMI"))

    frame:
        xpos 120
        ypos 172
        xsize 1680
        ysize 822
        background Solid("#100806e8")
        padding (42, 32, 42, 38)

        vbox:
            xfill True
            spacing 24

            hbox:
                xfill True
                text _("OFFRES TEMPORAIRES") style "kami_hub_section"
                null width 560
                textbutton _("CODE PROMO"):
                    style "kami_hub_action"
                    xsize 190
                    ysize 46
                    text_size 21
                    action Show("kami_shop_promo")
                null width 24
                text _("FIN DANS 06 J 14 H") style "kami_hub_meta" color "#ff7040"

            add Solid("#b73c1c") xsize 1596 ysize 2

            hbox:
                xalign 0.5
                spacing 34
                for card_index, item in enumerate(page_items):
                    use kami_shop_item_card(item, card_index)

    text _("Les réquisitions non obtenues disparaîtront à la fin du cycle."):
        style "kami_hub_meta"
        color "#8faab9"
        xalign 0.5
        ypos 1018


screen kami_shop_preview(item_id):
    modal True
    zorder 450

    default preview_recipe = kami_random_preview_recipe(kami_shop_item_by_id(item_id)["profile_id"])
    $ item = kami_shop_item_by_id(item_id)
    $ preview_image = kami_shop_preview_displayable(item_id, preview_recipe)

    key "K_ESCAPE" action Hide("kami_shop_preview")
    add Solid("#000000c8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 900
        background Solid("#07101af5")
        padding (28, 24, 28, 24)

        hbox:
            spacing 30

            frame:
                xsize 610
                ysize 810
                background Solid("#02070cee")
                padding (0, 0)
                if preview_image:
                    add Transform(preview_image, fit="contain", xsize=610, ysize=810) xalign 0.5 yalign 1.0

            vbox:
                xsize 420
                spacing 20
                yalign 0.5
                text _("PRÉVISUALISATION") style "kami_hub_meta" size 27
                text kd_tr(item["name"]) style "kami_hub_section" size 38
                text _("Corps, bras, bouche et yeux sont tirés au hasard. La tenue ou l'accessoire sélectionné reste fixe.") style "kami_hub_body" size 23 xsize 410
                textbutton _("ALÉATOIRE"):
                    style "kami_hub_action"
                    action SetScreenVariable("preview_recipe", kami_random_preview_recipe(item["profile_id"]))
                textbutton _("FERMER"):
                    style "kami_hub_action"
                    action Hide("kami_shop_preview")


screen kami_shop_promo():
    modal True
    zorder 460

    default promo_code_input = ""

    key "K_ESCAPE" action Hide("kami_shop_promo")
    add Solid("#000000c8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 350
        background Solid("#07101af5")
        padding (32, 28, 32, 28)

        vbox:
            spacing 22
            text _("CODE PROMO") style "kami_hub_section" xalign 0.5
            text _("Saisissez un code pour créditer des récompenses persistantes.") style "kami_hub_body" size 22 xalign 0.5
            input value ScreenVariableInputValue("promo_code_input") length 32 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_" xmaximum 620 xalign 0.5
            hbox:
                xalign 0.5
                spacing 18
                textbutton _("VALIDER"):
                    style "kami_hub_action"
                    xsize 260
                    action [Function(apply_promo_code, promo_code_input), SetScreenVariable("promo_code_input", "")]
                textbutton _("FERMER"):
                    style "kami_hub_action"
                    xsize 260
                    action Hide("kami_shop_promo")
