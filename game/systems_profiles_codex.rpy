# -----------------------------------------------------------------------
# PROFILS + CODEX — Systèmes de méta-progression narratifs
# -----------------------------------------------------------------------

default profile_affinity = {
    "noam": 0, "lysa": 0, "elen": 0, "elias": 0, "mara": 0, "julian": 0,
    "iris": 0, "tomas": 0, "kael": 0, "nyra": 0, "ryn": 0, "sael": 0,
}
default profile_story_unlocked = {
    "noam": False, "lysa": False, "elen": False, "elias": False, "mara": False, "julian": False,
    "iris": False, "tomas": False, "kael": False, "nyra": False, "ryn": False, "sael": False,
}
default profile_relations_unlocked = {
    "noam": False, "lysa": False, "elen": False, "elias": False, "mara": False, "julian": False,
    "iris": False, "tomas": False, "kael": False, "nyra": False, "ryn": False, "sael": False,
}
default profile_global_points = 0
default persistent.profile_wardrobe_unlocked = {}
default persistent.profile_skin_equipped = {}
default persistent.profile_accessories_unlocked = {}
default persistent.profile_accessory_equipped = {}
default persistent.redeemed_promo_codes = []
default player_inventory = []

init python:
    import re

    PROFILE_ORDER = ["noam", "lysa", "elias", "mara", "julian", "iris", "tomas", "elen", "kael", "nyra", "ryn", "sael"]

    PROFILE_DATA = {
        "noam": {
            "name": "Noam", "role": "Médiateur", "district": "Harmonie", "age": "20",
            "height": "178 cm", "chest": "88 cm", "birthday": "14 avril",
            "quote": "Comprendre avant de trancher.",
            "sprite": "images/character/noam/portrait.png",
            "expressions": ["neutre", "inquiet", "determine"],
            "backstory": "Noam est réveillé dans le Conclave sans souvenirs complets des semaines précédentes. Il compense par une écoute active et une capacité inhabituelle à reformuler les conflits.",
            "relations": "Pivot entre les représentants: confiance fragile de Lysa, friction idéologique avec Kael, empathie instinctive avec Iris.",
        },
        "lysa": {"name": "Lysa", "role": "Habitante", "district": "Harmonie", "age": "22", "height": "173 cm", "chest": "83 cm", "birthday": "3 septembre", "quote": "Une promesse sans procédure n'est qu'un bruit.", "sprite": "images/character/lysa/portrait.png", "expressions": ["neutre", "inquiet", "sourire"], "backstory": "Spécialiste des flux et des quotas.", "relations": "S'aligne souvent avec Tomas sur les contraintes matérielles."},
        "elias": {"name": "Elias", "role": "Ouvrier", "district": "Axiome", "age": "21", "height": "177 cm", "chest": "95 cm", "birthday": "19 janvier", "quote": "Tenir, c'est déjà gagner du temps.", "sprite": "images/character/elias/portrait.png", "expressions": ["neutre", "determine", "surpris"] , "backstory": "Ancien instructeur de terrain.", "relations": "Complicité compétitive avec Ryn."},
        "mara": {"name": "Mara", "role": "Habitante", "district": "Axiome", "age": "24", "height": "174 cm", "chest": "87 cm", "birthday": "27 juin", "quote": "Un repas stable vaut mieux qu'un grand discours.", "sprite": "images/character/mara/portrait.png", "expressions": ["neutre", "rire", "inquiet"], "backstory": "Gestionnaire des stocks alimentaires.", "relations": "Confiance pragmatique avec Lysa."},
        "julian": {"name": "Julian", "role": "Habitant", "district": "Nexus", "age": "22", "height": "181 cm", "chest": "85 cm", "birthday": "8 novembre", "quote": "Les chiffres mentent moins que nous.", "sprite": "images/character/julian/portrait.png", "expressions": ["neutre", "reflexion", "triste"], "backstory": "Analyse les cycles d'incidents.", "relations": "Affinité intellectuelle avec Noam."},
        "iris": {"name": "Iris", "role": "Habitante", "district": "Nexus", "age": "20", "height": "169 cm", "chest": "78 cm", "birthday": "22 février", "quote": "Le silence est aussi un signal.", "sprite": "images/character/iris/portrait.png", "expressions": ["neutre", "peur", "joie"], "backstory": "Répare les intercoms et capteurs.", "relations": "Confie des informations fragmentaires à Noam."},
        "tomas": {"name": "Tomas", "role": "Archiviste", "district": "Archive", "age": "25", "height": "187 cm", "chest": "108 cm", "birthday": "5 octobre", "quote": "Si ce n'est pas consigné, c'est déjà perdu.", "sprite": "images/character/tomas/portrait.png", "expressions": ["neutre", "reflechit", "desaccord"], "backstory": "Archiviste des directives Kami.", "relations": "Joutes argumentatives avec Julian."},
        "elen": {"name": "Elen", "role": "Habitante", "district": "Archive", "age": "23", "height": "166 cm", "chest": "81 cm", "birthday": "16 mai", "quote": "On compte les vivants, pas les slogans.", "sprite": "images/character/elen/portrait.png", "expressions": ["neutre", "colere", "triste"], "backstory": "A connu trois vagues de pénurie de médicaments.", "relations": "Respect mutuel avec Sael, tensions avec les discours propagandistes."},
        "kael": {"name": "Kael", "role": "Ingénieur", "district": "Orbite", "age": "26", "height": "174 cm", "chest": "82 cm", "birthday": "30 décembre", "quote": "On ne négocie pas avec une turbine en panne.", "sprite": "images/character/kael/portrait.png", "expressions": ["neutre", "colere", "determine"], "backstory": "Responsable des infrastructures critiques.", "relations": "Conflits avec ceux qui sous-estiment la technique."},
        "nyra": {"name": "Nyra", "role": "Habitante", "district": "Orbite", "age": "23", "height": "156 cm", "chest": "81 cm", "birthday": "11 août", "quote": "Le cadre protège de l'arbitraire.", "sprite": "images/character/nyra/portrait.png", "expressions": ["neutre", "sourire", "desaccord"], "backstory": "Gardienne des règles de séance.", "relations": "Alliance variable avec Lysa selon le contexte."},
        "ryn": {"name": "Ryn", "role": "Gardien", "district": "Limen", "age": "21", "height": "154 cm", "chest": "83 cm", "birthday": "7 mars", "quote": "Le danger n'attend pas les votes.", "sprite": "images/character/ryn/portrait.png", "expressions": ["neutre", "inquiet", "determine"], "backstory": "Patrouilles en zones instables.", "relations": "Peut basculer entre Elias et Kael."},
        "sael": {"name": "Sael", "role": "Habitante", "district": "Limen", "age": "24", "height": "172 cm", "chest": "88 cm", "birthday": "24 juillet", "quote": "Je vois ce qui entre. Et ce qui disparaît.", "sprite": "images/character/sael/portrait.png", "expressions": ["neutre", "mefiant", "sourire"], "backstory": "Interface entre l'extérieur et le Conclave.", "relations": "Soupçonne des anomalies de distribution."},
    }

    def clamp_affinity(value):
        return max(0, min(100, int(value)))

    def add_affinity(profile_id, delta, unlock_thresholds=True):
        if profile_id not in store.profile_affinity:
            return
        store.profile_affinity[profile_id] = clamp_affinity(store.profile_affinity[profile_id] + delta)
        store.profile_global_points += delta

    def register_debate_alignment(profile_id, agreed=True):
        add_affinity(profile_id, 4 if agreed else -6)

    def unlock_profile_section(profile_id, section="story"):
        if profile_id not in PROFILE_DATA:
            return
        if section == "story":
            store.profile_story_unlocked[profile_id] = True
        elif section == "relations":
            store.profile_relations_unlocked[profile_id] = True

    def profile_portrait(profile_id):
        portrait = "images/character/{}/portrait.png".format(profile_id)
        return portrait if renpy.loadable(portrait) else PROFILE_DATA[profile_id]["sprite"]

    def character_uses_layered_wardrobe(profile_id):
        return kd_character_has_layered_wardrobe(profile_id)

    def profile_skin_path(profile_id, skin_id):
        if skin_id == "neutre":
            neutral = "images/character/{}/neutre.png".format(profile_id)
            if renpy.loadable(neutral):
                return neutral
            return profile_portrait(profile_id)

        direct_path = "images/character/{}/{}.png".format(profile_id, skin_id)
        if renpy.loadable(direct_path):
            return direct_path

        for path in (
            "images/character/{}/skins/{}.png".format(profile_id, skin_id),
            "images/character/{}/skins/skin_{}.png".format(profile_id, skin_id),
            "images/character/{}/{}.png".format(profile_id, skin_id),
            "images/character/{}/skin_{}.png".format(profile_id, skin_id),
        ):
            if renpy.loadable(path):
                return path

        return "images/character/{}/skins/{}.png".format(profile_id, skin_id)

    def get_profile_detected_skins(profile_id):
        layered_wardrobe = character_uses_layered_wardrobe(profile_id)
        detected = set(["tenue1"] if layered_wardrobe else ["neutre"])

        for skin_id in persistent.profile_wardrobe_unlocked.get(profile_id, []):
            if not layered_wardrobe or skin_id.startswith("tenue"):
                detected.add(skin_id)

        for rewards in PROMO_CODES.values():
            for reward_profile_id, skin_id in rewards.get("skins", []):
                if reward_profile_id == profile_id and (not layered_wardrobe or skin_id.startswith("tenue")):
                    detected.add(skin_id)

        if profile_id in persistent.profile_skin_equipped:
            equipped_skin = persistent.profile_skin_equipped[profile_id]
            if not layered_wardrobe or equipped_skin.startswith("tenue"):
                detected.add(equipped_skin)

        prefix = "images/character/{}/".format(profile_id)
        if layered_wardrobe:
            skin_regex = re.compile(r"^{}(tenue\d+)\.png$".format(re.escape(prefix)))
        else:
            skin_regex = re.compile(r"^{}(?:skins/)?skin_(.+)\.png$".format(re.escape(prefix)))
        for filepath in renpy.list_files():
            skin_match = skin_regex.match(filepath)
            if skin_match:
                detected.add(skin_match.group(1))

        filtered = []
        for skin_id in sorted(detected):
            if skin_id in ("neutre", "tenue1") or renpy.loadable(profile_skin_path(profile_id, skin_id)):
                filtered.append(skin_id)

        return filtered

    def get_profile_unlocked_skins(profile_id):
        detected = get_profile_detected_skins(profile_id)
        unlocked = list(persistent.profile_wardrobe_unlocked.get(profile_id, []))
        base_skin = "tenue1" if character_uses_layered_wardrobe(profile_id) else "neutre"
        if base_skin not in unlocked:
            unlocked.insert(0, base_skin)
        return [skin_id for skin_id in detected if skin_id in unlocked]

    def is_profile_skin_unlocked(profile_id, skin_id):
        return skin_id in get_profile_unlocked_skins(profile_id)

    def get_profile_equipped_skin(profile_id):
        base_skin = "tenue1" if character_uses_layered_wardrobe(profile_id) else "neutre"
        equipped = persistent.profile_skin_equipped.get(profile_id, base_skin)
        if equipped not in get_profile_unlocked_skins(profile_id):
            equipped = base_skin
        return equipped

    def profile_display_image(profile_id):
        if character_uses_layered_wardrobe(profile_id) or get_profile_equipped_accessories(profile_id):
            return ImageReference("{} neutre".format(profile_id))
        skin_id = get_profile_equipped_skin(profile_id)
        skin_path = profile_skin_path(profile_id, skin_id)
        if renpy.loadable(skin_path):
            return skin_path
        return profile_portrait(profile_id)

    def profile_skin_display_image(profile_id):
        if character_uses_layered_wardrobe(profile_id) or get_profile_equipped_accessories(profile_id):
            return ImageReference("{} neutre".format(profile_id))
        skin_id = get_profile_equipped_skin(profile_id)
        skin_path = profile_skin_path(profile_id, skin_id)
        if renpy.loadable(skin_path):
            return skin_path
        return None

    def unlock_profile_skin(profile_id, skin_id):
        unlocked = set(persistent.profile_wardrobe_unlocked.get(profile_id, []))
        unlocked.add(skin_id)
        persistent.profile_wardrobe_unlocked[profile_id] = sorted(unlocked)
        renpy.save_persistent()

    def equip_profile_skin(profile_id, skin_id):
        if skin_id in get_profile_unlocked_skins(profile_id):
            persistent.profile_skin_equipped[profile_id] = skin_id
            renpy.save_persistent()
            renpy.restart_interaction()

    def get_profile_detected_accessories(profile_id):
        prefix = "images/character/{}/".format(profile_id)
        accessory_regex = re.compile(r"^{}(accessoire[^/]*)\.png$".format(re.escape(prefix)))
        detected = set(persistent.profile_accessories_unlocked.get(profile_id, []))
        for filepath in renpy.list_files():
            match = accessory_regex.match(filepath)
            if match:
                detected.add(match.group(1))
        return sorted(
            accessory_id for accessory_id in detected
            if renpy.loadable(kd_character_asset(profile_id, accessory_id))
        )

    def get_profile_unlocked_accessories(profile_id):
        unlocked = set(persistent.profile_accessories_unlocked.get(profile_id, []))
        return [
            accessory_id for accessory_id in get_profile_detected_accessories(profile_id)
            if accessory_id in unlocked
        ]

    def get_profile_equipped_accessories(profile_id):
        equipped = persistent.profile_accessory_equipped.get(profile_id, [])
        if isinstance(equipped, str):
            equipped = [equipped]
        unlocked = set(get_profile_unlocked_accessories(profile_id))
        return [accessory_id for accessory_id in equipped if accessory_id in unlocked]

    def is_profile_accessory_unlocked(profile_id, accessory_id):
        return accessory_id in get_profile_unlocked_accessories(profile_id)

    def unlock_profile_accessory(profile_id, accessory_id):
        unlocked = set(persistent.profile_accessories_unlocked.get(profile_id, []))
        unlocked.add(accessory_id)
        persistent.profile_accessories_unlocked[profile_id] = sorted(unlocked)
        renpy.save_persistent()

    def toggle_profile_accessory(profile_id, accessory_id):
        if not is_profile_accessory_unlocked(profile_id, accessory_id):
            return
        equipped = list(get_profile_equipped_accessories(profile_id))
        if accessory_id in equipped:
            equipped.remove(accessory_id)
        else:
            equipped.append(accessory_id)
        persistent.profile_accessory_equipped[profile_id] = sorted(equipped)
        renpy.save_persistent()
        renpy.restart_interaction()

    PROFILE_PREVIEW_BLINK_PERIODS = {
        "noam": 4.9, "lysa": 4.8, "elias": 5.1, "mara": 4.8,
        "julian": 5.0, "iris": 4.9, "tomas": 4.85, "elen": 4.8,
        "kael": 5.2, "nyra": 4.9, "ryn": 5.0, "sael": 4.8,
    }

    def _profile_animated_preview(st, at, profile_id, outfit_id, accessories, body, arms, mouth, eyes):
        blink_period = PROFILE_PREVIEW_BLINK_PERIODS.get(profile_id, 4.9)
        blink_start = blink_period - 0.28
        blink_end = blink_period - 0.12
        displayed_eyes = eyes
        if blink_start <= (st % blink_period) <= blink_end:
            closed_eyes = kd_character_asset(profile_id, "yeux_ferme")
            if renpy.loadable(closed_eyes):
                displayed_eyes = "yeux_ferme"

        preview = kd_character_preview_displayable(
            profile_id,
            outfit_id,
            accessories,
            (arms, mouth, displayed_eyes),
            zoom=0.60,
            body_name=body,
        )
        return preview, kd_layered_sprite_delay(st, blink_period, blink_start, blink_end, False)

    def profile_cosmetic_preview(profile_id, skin_id=None, accessory_ids=None, recipe=None):
        equipped_skin = skin_id or get_profile_equipped_skin(profile_id)
        accessories = get_profile_equipped_accessories(profile_id) if accessory_ids is None else accessory_ids
        expression_map = getattr(store, "{}_EXPRESSIONS".format(profile_id.upper()), {})
        neutral = expression_map.get("neutre")
        if neutral:
            body, arms, mouth, eyes = neutral
            if skin_id is None and accessory_ids is None and recipe is None:
                return DynamicDisplayable(
                    _profile_animated_preview,
                    profile_id,
                    equipped_skin,
                    tuple(accessories),
                    body,
                    arms,
                    mouth,
                    eyes,
                )
            return kd_character_preview_displayable(
                profile_id,
                equipped_skin,
                accessories,
                recipe or (arms, mouth, eyes),
                zoom=0.60,
                body_name=body,
            )

        skin_path = profile_skin_path(profile_id, equipped_skin)
        if renpy.loadable(skin_path):
            return skin_path
        return profile_portrait(profile_id)

    PROMO_CODES = {
        "NOAMPYJAMA": {
            "skins": [("noam", "tenue2")],
            "message": "Tenue pyjama débloquée pour Noam !",
        },
        "TESTPROMO69": {
            "desire_shards": 1000,
            "message": "+1000 Éclats de désir",
        },
        "WELCOME-KD": {
            "kamyz": 150,
            "items": ["Kit de secours"],
            "message": "+150 Kamyz et 1 Kit de secours",
        },
        "LYSABONUS01": {
            "skins": [("lysa", "gothic_maid")],
            "message": "Skin Cyber et Gothic Maid débloqué pour Lysa !",
        },
        "LYSABONUS02": {
            "skins": [("lysa", "cyber")],
            "message": "Skin Cyber débloqué pour Lysa !",
        },
        "PACK-CONCLAVE": {
            "kamyz": 300,
            "items": ["Fragment mémoire", "Ticket premium"],
            "skins": [("nyra", "ceremonie"), ("kael", "ferraille")],
            "message": "+300 Kamyz, objets bonus et 2 skins exclusifs",
        },
    }

    def apply_promo_code(code_input):
        code = (code_input or "").strip().upper()
        if not code:
            renpy.notify("Code promo vide.")
            return

        if code in persistent.redeemed_promo_codes:
            renpy.notify("Code déjà utilisé.")
            return

        rewards = PROMO_CODES.get(code)
        if not rewards:
            renpy.notify("Code promo invalide.")
            return

        if rewards.get("kamyz"):
            store.player_kamyz += int(rewards["kamyz"])

        if rewards.get("desire_shards"):
            persistent.desire_shards = int(persistent.desire_shards or 0) + int(rewards["desire_shards"])

        for item_name in rewards.get("items", []):
            if item_name not in store.player_inventory:
                store.player_inventory.append(item_name)

        for profile_id, skin_id in rewards.get("skins", []):
            if profile_id in PROFILE_DATA:
                unlock_profile_skin(profile_id, skin_id)

        for profile_id, accessory_id in rewards.get("accessories", []):
            if profile_id in PROFILE_DATA:
                unlock_profile_accessory(profile_id, accessory_id)

        persistent.redeemed_promo_codes.append(code)
        renpy.save_persistent()
        renpy.notify("Code validé : {}".format(rewards.get("message", "récompenses ajoutées")))



transform profile_card_in:
    alpha 0.0
    yoffset 16
    easeout 0.28 alpha 1.0 yoffset 0

transform profile_character_in:
    alpha 0.0
    xoffset -28
    easeout 0.32 alpha 1.0 xoffset 0

style profile_selector_button is button:
    xsize 104
    ysize 104
    padding (6, 6, 6, 6)
    background Fixed(Solid("#060b12ee"), Solid("#17364a", ysize=3, yalign=1.0))
    hover_background Fixed(Solid("#0c2637f5"), Solid("#5cd3ff", ysize=4, yalign=1.0))
    selected_background Fixed(
        Solid("#112838f5"),
        Solid("#5cd3ff", xsize=3),
        Solid("#5cd3ff", xsize=3, xalign=1.0),
        Solid("#5cd3ff", ysize=4, yalign=1.0),
    )

style profile_cosmetic_button is button:
    xsize 340
    ysize 64
    padding (18, 8, 18, 8)
    background Fixed(Solid("#10162ae8"), Solid("#b860ff", xsize=5))
    hover_background Fixed(Solid("#28143af5"), Solid("#d68cff", xsize=7), Solid("#d68cff", ysize=3, yalign=1.0))

style profile_cosmetic_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 24
    color "#e7d1f5"
    hover_color "#ffffff"
    kerning 1.5
    xalign 0.5
    yalign 0.5

style profile_back_button is button:
    xsize 210
    ysize 56
    padding (18, 8, 18, 8)
    background Solid("#07131dcc")
    hover_background Solid("#0c3044f5")

style profile_back_button_text is button_text:
    font "fonts/Rajdhani-SemiBold.ttf"
    size 22
    color "#7fa7b8"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


screen profile_stat_cell(label, value, cell_width=488):
    frame:
        xsize cell_width
        ysize 74
        padding (0, 0)
        background Fixed(
            Solid("#101523e8"),
            Solid("#9d3fd077", xsize=210),
            Solid("#c967ff", ysize=2, yalign=1.0),
        )

        text label:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 17
            color "#f0cfff"
            kerning 1.2
            xpos 18
            yalign 0.5

        text value:
            font "fonts/Rajdhani-SemiBold.ttf"
            size 25
            color "#ffffff"
            xpos 232
            yalign 0.5


screen profiles_menu():
    tag menu
    modal True

    default selected_profile = "noam"
    $ profile = PROFILE_DATA[selected_profile]
    $ profile_index = PROFILE_ORDER.index(selected_profile)
    $ profile_render = profile_cosmetic_preview(selected_profile)
    $ total_free_times = len(FREE_TIME_SCENES.get(selected_profile, []))
    $ completed_free_times = free_time_character_count(selected_profile)
    $ completed_free_time_label = _("TERMINÉ") if completed_free_times == 1 else _("TERMINÉS")
    $ total_free_time_label = _("DISPONIBLE") if total_free_times == 1 else _("DISPONIBLES")

    key "game_menu" action Return()
    key "K_LEFT" action SetScreenVariable("selected_profile", PROFILE_ORDER[(profile_index - 1) % len(PROFILE_ORDER)])
    key "K_RIGHT" action SetScreenVariable("selected_profile", PROFILE_ORDER[(profile_index + 1) % len(PROFILE_ORDER)])

    add gui.game_menu_background
    add Solid("#02070ce5")
    add Solid("#071c2a66", xsize=720)
    add Solid("#5cd3ff12", ysize=2) ypos 112
    add "gui/main_menu_kami/scanlines.png" alpha 0.12
    add "gui/main_menu_kami/vignette.png" alpha 0.70

    text _("KAMI.CORE // DOSSIERS DES REPRÉSENTANTS"):
        font "fonts/Barlow-Light.ttf"
        size 18
        color "#5cd3ff"
        kerning 4
        xpos 72
        ypos 48

    textbutton _("RETOUR"):
        style "profile_back_button"
        xpos 1638
        ypos 34
        action Return()

    frame:
        xpos 92
        ypos 118
        xsize 1736
        ysize 718
        padding (0, 0)
        background Fixed(
            Solid("#050b12e8"),
            Solid("#5cd3ff55", xsize=2),
            Solid("#ffffff10", ysize=1),
            Solid("#5cd3ff22", ysize=2, yalign=1.0),
        )
        at profile_card_in

        fixed:
            # Portrait principal inspiré de la fiche de référence.
            frame:
                xpos 28
                ypos 26
                xsize 610
                ysize 666
                padding (0, 0)
                background Fixed(
                    Solid("#142634f2"),
                    Solid("#5cd3ff22", xsize=4),
                    Solid("#5cd3ff22", xsize=4, xalign=1.0),
                    Solid("#5cd3ff33", ysize=3, yalign=1.0),
                )

                fixed:
                    xsize 610
                    ysize 666
                    clipping True
                    add Transform("gui/main_menu_kami/glyph_kami.png", size=(430, 430), matrixcolor=TintMatrix("#38a8c8")) xalign 0.5 yalign 0.5 alpha 0.10
                    if profile_render:
                        add profile_render:
                            zoom 0.90
                            xalign 0.5
                            yalign 0.07
                            at profile_character_in

            text profile["name"]:
                font "fonts/Rajdhani-SemiBold.ttf"
                size 58
                color "#f2f8fb"
                kerning 4
                xpos 688
                ypos 40
            text "{}  //  {} {}".format(kd_tr(profile["role"]), kd_tr("REPRÉSENTANT·E DE"), kd_tr(profile["district"]).upper()):
                font "fonts/Barlow-Light.ttf"
                size 21
                color "#5cd3ff"
                kerning 2.5
                xpos 692
                ypos 105

            add Solid("#5cd3ff66") xpos 690 ypos 146 xsize 990 ysize 2

            # Tableau d'identité aéré, construit comme une fiche de personnage.
            vbox:
                xpos 690
                ypos 170
                spacing 14

                hbox:
                    spacing 14
                    use profile_stat_cell(_("PRÉNOM"), profile["name"])
                    use profile_stat_cell(_("ÂGE"), _("{} ANS").format(profile["age"]))

                hbox:
                    spacing 14
                    use profile_stat_cell(_("TAILLE"), profile["height"])
                    use profile_stat_cell(_("TOUR DE POITRINE"), profile["chest"])

                hbox:
                    spacing 14
                    use profile_stat_cell(_("DISTRICT"), kd_tr(profile["district"]).upper())
                    use profile_stat_cell(_("ANNIVERSAIRE"), kd_tr(profile["birthday"]).upper())

            # Progression des temps libres : un cœur par scène du catalogue.
            frame:
                xpos 690
                ypos 442
                xsize 990
                ysize 140
                padding (24, 18, 24, 18)
                background Fixed(Solid("#131722ed"), Solid("#ff496c88", xsize=4))

                hbox:
                    yalign 0.5
                    spacing 26
                    vbox:
                        xsize 430
                        spacing 4
                        text _("LIEN // TEMPS LIBRES") font "fonts/Rajdhani-SemiBold.ttf" size 23 color "#ff718a" kerning 2
                        text "[completed_free_times] [completed_free_time_label] / [total_free_times] [total_free_time_label]" font "fonts/Barlow-Light.ttf" size 18 color "#879eaa"
                    if total_free_times:
                        hbox:
                            spacing 14
                            yalign 0.5
                            for heart_index in range(total_free_times):
                                if heart_index < completed_free_times:
                                    add Transform("gui/profiles/heart_complete.png", size=(56, 56))
                                else:
                                    add Transform("gui/profiles/heart_locked.png", size=(56, 56))
                    else:
                        text _("AUCUN TEMPS LIBRE ASSOCIÉ") font "fonts/Rajdhani-SemiBold.ttf" size 22 color "#4b5a62" yalign 0.5

            textbutton _("TENUES & ACCESSOIRES"):
                style "profile_cosmetic_button"
                xpos 1340
                ypos 610
                action Show("profile_wardrobe", profile_id=selected_profile)

            text "« {} »".format(kd_tr(profile["quote"])):
                font "fonts/Barlow-Light.ttf"
                size 20
                color "#a8c1cd"
                italic True
                xpos 690
                ypos 628
                xmaximum 610

    # Sélecteur horizontal des douze représentants.
    frame:
        xpos 248
        ypos 856
        xsize 1424
        ysize 150
        padding (34, 20, 34, 20)
        background Fixed(Solid("#03070cdd"), Solid("#5cd3ff33", ysize=2))

        hbox:
            spacing 9
            xalign 0.5
            for pid in PROFILE_ORDER:
                button:
                    style "profile_selector_button"
                    selected selected_profile == pid
                    action SetScreenVariable("selected_profile", pid)
                    add Transform(profile_portrait(pid), fit="cover", xsize=92, ysize=92) xalign 0.5 yalign 0.5

    textbutton "‹":
        style "profile_back_button"
        text_size 38
        xpos 104
        ypos 888
        xsize 90
        action SetScreenVariable("selected_profile", PROFILE_ORDER[(profile_index - 1) % len(PROFILE_ORDER)])
    textbutton "›":
        style "profile_back_button"
        text_size 38
        xpos 1726
        ypos 888
        xsize 90
        action SetScreenVariable("selected_profile", PROFILE_ORDER[(profile_index + 1) % len(PROFILE_ORDER)])


screen profile_wardrobe(profile_id):
    modal True
    zorder 400

    $ detected_skins = get_profile_detected_skins(profile_id)
    $ detected_accessories = get_profile_detected_accessories(profile_id)
    $ equipped_skin_id = get_profile_equipped_skin(profile_id)
    $ equipped_accessories = get_profile_equipped_accessories(profile_id)
    $ wardrobe_preview = profile_cosmetic_preview(profile_id)

    add Solid("#00000090")
    add Solid("#5CD3FF22", ysize=2) ypos 170
    add Solid("#5CD3FF22", ysize=2) ypos 910

    frame:
        background Fixed(
            Solid("#0A1326F5"),
            Solid("#5CD3FF55", xsize=4),
            Solid("#5CD3FF55", xsize=4, xalign=1.0),
            Solid("#FFFFFF12", ysize=1),
        )
        xalign 0.5
        yalign 0.5
        xsize 1240
        ysize 790
        padding (22, 20)

        vbox:
            spacing 14
            text "{} // {}".format(_("GARDE-ROBE"), character_display_name(profile_id)) size 34 color "#DFF2FF" font "fonts/Rajdhani-SemiBold.ttf"
            text _("Les choix équipés sont sauvegardés de façon permanente et appliqués aux sprites en jeu.") size 20 color "#BFD6EA"

            hbox:
                spacing 22

                frame:
                    xsize 430
                    ysize 590
                    background Solid("#030912EE")
                    padding (0, 0)
                    if wardrobe_preview:
                        add Transform(wardrobe_preview, fit="contain", xsize=430, ysize=590) xalign 0.5 yalign 1.0

                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    xsize 720
                    ymaximum 590

                    vbox:
                        spacing 12
                        text _("TENUES") size 28 color "#5CD3FF" font "fonts/Rajdhani-SemiBold.ttf"

                        for skin_id in detected_skins:
                            $ skin_unlocked = is_profile_skin_unlocked(profile_id, skin_id)
                            $ skin_preview = profile_cosmetic_preview(profile_id, skin_id, equipped_accessories)
                            frame:
                                xsize 680
                                ysize 150
                                background Solid("#071725DD")
                                padding (12, 8, 12, 8)
                                hbox:
                                    spacing 16
                                    add Transform(
                                        skin_preview,
                                        fit="contain",
                                        xsize=110,
                                        ysize=132,
                                        matrixcolor=None if skin_unlocked else SaturationMatrix(0),
                                    )
                                    vbox:
                                        spacing 8
                                        yalign 0.5
                                        text skin_id.upper() size 25 color ("#FFFFFF" if skin_unlocked else "#8EA3B8")
                                        if not skin_unlocked:
                                            text _("VERROUILLÉE — disponible dans la Boutique") size 18 color "#8EA3B8"
                                        elif equipped_skin_id == skin_id:
                                            text _("ÉQUIPÉE") size 21 color "#70E0A0"
                                        else:
                                            textbutton _("ÉQUIPER"):
                                                background Solid("#10384DCC")
                                                hover_background Solid("#1D5C7AEE")
                                                text_color "#DFF2FF"
                                                text_hover_color "#FFFFFF"
                                                action Function(equip_profile_skin, profile_id, skin_id)

                        if detected_accessories:
                            text _("ACCESSOIRES") size 28 color "#DDB6FF" font "fonts/Rajdhani-SemiBold.ttf"

                            for accessory_id in detected_accessories:
                                $ accessory_unlocked = is_profile_accessory_unlocked(profile_id, accessory_id)
                                $ accessory_equipped = accessory_id in equipped_accessories
                                $ accessory_preview = profile_cosmetic_preview(profile_id, equipped_skin_id, [accessory_id])
                                frame:
                                    xsize 680
                                    ysize 150
                                    background Solid("#130C1CDD")
                                    padding (12, 8, 12, 8)
                                    hbox:
                                        spacing 16
                                        add Transform(
                                            accessory_preview,
                                            fit="contain",
                                            xsize=110,
                                            ysize=132,
                                            matrixcolor=None if accessory_unlocked else SaturationMatrix(0),
                                        )
                                        vbox:
                                            spacing 8
                                            yalign 0.5
                                            text accessory_id.upper() size 25 color ("#FFFFFF" if accessory_unlocked else "#8EA3B8")
                                            if not accessory_unlocked:
                                                text _("VERROUILLÉ — disponible dans la Boutique") size 18 color "#8EA3B8"
                                            else:
                                                textbutton _("RETIRER" if accessory_equipped else "ÉQUIPER"):
                                                    background Solid("#4A1D5CCC" if accessory_equipped else "#10384DCC")
                                                    hover_background Solid("#713080EE" if accessory_equipped else "#1D5C7AEE")
                                                    text_color "#F2DEFF"
                                                    text_hover_color "#FFFFFF"
                                                    action Function(toggle_profile_accessory, profile_id, accessory_id)

            textbutton _("FERMER") action Hide("profile_wardrobe") xalign 1.0 background Solid("#25101ACC") hover_background Solid("#4A1D2AEE") text_color "#FFD6E0"


screen exploration_meta_buttons():
    zorder 240

    hbox:
        spacing 10
        xalign 0.98
        yalign 0.03

        textbutton "Profils" action ShowMenu("profiles_menu")
        textbutton "Codex" action ShowMenu("codex_menu")
        textbutton "Codes promo" action ShowMenu("promo_codes_menu")


screen promo_codes_menu():
    tag menu

    default promo_code_input = ""

    use game_menu(_("Codes promo"), scroll="viewport"):
        vbox:
            spacing 16
            xfill True

            frame:
                background Fixed(
                    Solid("#0A1326F2"),
                    Solid("#5CD3FF55", xsize=4),
                    Solid("#FFFFFF12", ysize=1),
                )
                xfill True
                padding (22, 18)

                vbox:
                    spacing 8
                    text "KAMI.CORE // CODES PROMO" size 34 color "#DFF2FF" font "fonts/Rajdhani-SemiBold.ttf"
                    text "Entre un code promo pour recevoir des récompenses (skins, Kamyz, objets, etc.)." size 22 color "#BFD6EA"

                    hbox:
                        spacing 10
                        input value ScreenVariableInputValue("promo_code_input") length 32 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_" xmaximum 340
                        textbutton "Valider":
                            background Solid("#10384DCC")
                            hover_background Solid("#1D5C7AEE")
                            text_color "#DFF2FF"
                            text_hover_color "#FFFFFF"
                            action [Function(apply_promo_code, promo_code_input), SetScreenVariable("promo_code_input", "")]

            frame:
                background Fixed(
                    Solid("#07111CDD"),
                    Solid("#FFD16655", xsize=3),
                )
                xfill True
                padding (16, 14)

                vbox:
                    spacing 8
                    text "Codes déjà utilisés : [len(persistent.redeemed_promo_codes)]" size 24 color "#D9E2EF"
                    if persistent.redeemed_promo_codes:
                        text "[', '.join(persistent.redeemed_promo_codes)]" size 19 color "#9CB2C8"
                    else:
                        text "Aucun code validé pour le moment." size 19 color "#9CB2C8"

            frame:
                background Fixed(
                    Solid("#07111CDD"),
                    Solid("#5CD3FF33", xsize=3),
                )
                xfill True
                padding (16, 14)

                vbox:
                    spacing 6
                    text "Inventaire joueur" size 24 color "#D9E2EF"
                    text "Éclats de désir : [persistent.desire_shards]" size 22 color "#DDB6FF"
                    text "Kamyz : [player_kamyz]" size 22 color "#FFE7AE"
                    if player_inventory:
                        text "Objets : [', '.join(player_inventory)]" size 19 color "#C8D7E6"
                    else:
                        text "Objets : aucun" size 19 color "#8EA3B8"
