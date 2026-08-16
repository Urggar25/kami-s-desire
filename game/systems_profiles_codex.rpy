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
default persistent.redeemed_promo_codes = []
default player_inventory = []

init python:
    import re

    PROFILE_ORDER = ["noam", "lysa", "elias", "mara", "julian", "iris", "tomas", "elen", "kael", "nyra", "ryn", "sael"]

    PROFILE_DATA = {
        "noam": {
            "name": "Noam", "role": "Médiateur", "district": "Harmonie", "age": "20",
            "quote": "Comprendre avant de trancher.",
            "sprite": "images/character/noam/portrait.png",
            "expressions": ["neutre", "inquiet", "determine"],
            "backstory": "Noam est réveillé dans le Conclave sans souvenirs complets des semaines précédentes. Il compense par une écoute active et une capacité inhabituelle à reformuler les conflits.",
            "relations": "Pivot entre les représentants: confiance fragile de Lysa, friction idéologique avec Kael, empathie instinctive avec Iris.",
        },
        "lysa": {"name": "Lysa", "role": "Habitante", "district": "Harmonie", "age": "22", "quote": "Une promesse sans procédure n'est qu'un bruit.", "sprite": "images/character/lysa/portrait.png", "expressions": ["neutre", "inquiet", "sourire"], "backstory": "Spécialiste des flux et des quotas.", "relations": "S'aligne souvent avec Tomas sur les contraintes matérielles."},
        "elias": {"name": "Elias", "role": "Ouvrier", "district": "Axiome", "age": "21", "quote": "Tenir, c'est déjà gagner du temps.", "sprite": "images/character/elias/portrait.png", "expressions": ["neutre", "determine", "surpris"] , "backstory": "Ancien instructeur de terrain.", "relations": "Complicité compétitive avec Ryn."},
        "mara": {"name": "Mara", "role": "Habitante", "district": "Axiome", "age": "24", "quote": "Un repas stable vaut mieux qu'un grand discours.", "sprite": "images/character/mara/portrait.png", "expressions": ["neutre", "rire", "inquiet"], "backstory": "Gestionnaire des stocks alimentaires.", "relations": "Confiance pragmatique avec Lysa."},
        "julian": {"name": "Julian", "role": "Habitant", "district": "Nexus", "age": "22", "quote": "Les chiffres mentent moins que nous.", "sprite": "images/character/julian/portrait.png", "expressions": ["neutre", "reflexion", "triste"], "backstory": "Analyse les cycles d'incidents.", "relations": "Affinité intellectuelle avec Noam."},
        "iris": {"name": "Iris", "role": "Habitante", "district": "Nexus", "age": "20", "quote": "Le silence est aussi un signal.", "sprite": "images/character/iris/portrait.png", "expressions": ["neutre", "peur", "joie"], "backstory": "Répare les intercoms et capteurs.", "relations": "Confie des informations fragmentaires à Noam."},
        "tomas": {"name": "Tomas", "role": "Archiviste", "district": "Archive", "age": "25", "quote": "Si ce n'est pas consigné, c'est déjà perdu.", "sprite": "images/character/tomas/portrait.png", "expressions": ["neutre", "reflechit", "desaccord"], "backstory": "Archiviste des directives Kami.", "relations": "Joutes argumentatives avec Julian."},
        "elen": {"name": "Elen", "role": "Habitante", "district": "Archive", "age": "23", "quote": "On compte les vivants, pas les slogans.", "sprite": "images/character/elen/portrait.png", "expressions": ["neutre", "colere", "triste"], "backstory": "A connu trois vagues de pénurie de médicaments.", "relations": "Respect mutuel avec Sael, tensions avec les discours propagandistes."},
        "kael": {"name": "Kael", "role": "Ingénieur", "district": "Orbite", "age": "26", "quote": "On ne négocie pas avec une turbine en panne.", "sprite": "images/character/kael/portrait.png", "expressions": ["neutre", "colere", "determine"], "backstory": "Responsable des infrastructures critiques.", "relations": "Conflits avec ceux qui sous-estiment la technique."},
        "nyra": {"name": "Nyra", "role": "Habitante", "district": "Orbite", "age": "23", "quote": "Le cadre protège de l'arbitraire.", "sprite": "images/character/nyra/portrait.png", "expressions": ["neutre", "sourire", "desaccord"], "backstory": "Gardienne des règles de séance.", "relations": "Alliance variable avec Lysa selon le contexte."},
        "ryn": {"name": "Ryn", "role": "Gardien", "district": "Limen", "age": "21", "quote": "Le danger n'attend pas les votes.", "sprite": "images/character/ryn/portrait.png", "expressions": ["neutre", "inquiet", "determine"], "backstory": "Patrouilles en zones instables.", "relations": "Peut basculer entre Elias et Kael."},
        "sael": {"name": "Sael", "role": "Habitante", "district": "Limen", "age": "24", "quote": "Je vois ce qui entre. Et ce qui disparaît.", "sprite": "images/character/sael/portrait.png", "expressions": ["neutre", "mefiant", "sourire"], "backstory": "Interface entre l'extérieur et le Conclave.", "relations": "Soupçonne des anomalies de distribution."},
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

    def profile_skin_path(profile_id, skin_id):
        if skin_id == "neutre":
            neutral = "images/character/{}/neutre.png".format(profile_id)
            if renpy.loadable(neutral):
                return neutral
            return profile_portrait(profile_id)

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
        detected = set(["neutre"])

        for skin_id in persistent.profile_wardrobe_unlocked.get(profile_id, []):
            detected.add(skin_id)

        for rewards in PROMO_CODES.values():
            for reward_profile_id, skin_id in rewards.get("skins", []):
                if reward_profile_id == profile_id:
                    detected.add(skin_id)

        if profile_id in persistent.profile_skin_equipped:
            detected.add(persistent.profile_skin_equipped[profile_id])

        prefix = "images/character/{}/".format(profile_id)
        skin_regex = re.compile(r"^{}(?:skins/)?skin_(.+)\.png$".format(re.escape(prefix)))
        for filepath in renpy.list_files():
            skin_match = skin_regex.match(filepath)
            if skin_match:
                detected.add(skin_match.group(1))

        filtered = []
        for skin_id in sorted(detected):
            if skin_id == "neutre" or renpy.loadable(profile_skin_path(profile_id, skin_id)):
                filtered.append(skin_id)

        return filtered

    def get_profile_unlocked_skins(profile_id):
        detected = get_profile_detected_skins(profile_id)
        unlocked = list(persistent.profile_wardrobe_unlocked.get(profile_id, []))
        if "neutre" not in unlocked:
            unlocked.insert(0, "neutre")
        return [skin_id for skin_id in detected if skin_id in unlocked]

    def is_profile_skin_unlocked(profile_id, skin_id):
        return skin_id in get_profile_unlocked_skins(profile_id)

    def get_profile_equipped_skin(profile_id):
        equipped = persistent.profile_skin_equipped.get(profile_id, "neutre")
        if equipped not in get_profile_unlocked_skins(profile_id):
            equipped = "neutre"
        return equipped

    def profile_display_image(profile_id):
        skin_id = get_profile_equipped_skin(profile_id)
        skin_path = profile_skin_path(profile_id, skin_id)
        if renpy.loadable(skin_path):
            return skin_path
        return profile_portrait(profile_id)

    def profile_skin_display_image(profile_id):
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

    PROMO_CODES = {
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

        for item_name in rewards.get("items", []):
            if item_name not in store.player_inventory:
                store.player_inventory.append(item_name)

        for profile_id, skin_id in rewards.get("skins", []):
            if profile_id in PROFILE_DATA:
                unlock_profile_skin(profile_id, skin_id)

        persistent.redeemed_promo_codes.append(code)
        renpy.save_persistent()
        renpy.notify("Code validé : {}".format(rewards.get("message", "récompenses ajoutées")))



screen profiles_menu():
    tag menu

    default selected_profile = "noam"

    use game_menu(_("Profils"), scroll="viewport"):

        vbox:
            spacing 18

            frame:
                background Fixed(
                    Solid("#071426DD"),
                    Solid("#5CD3FF55", xsize=4),
                    Solid("#FFFFFF12", ysize=1),
                )
                xfill True
                padding (18, 12)

                hbox:
                    xfill True
                    spacing 18
                    text "KAMI.CORE // DOSSIERS REPRESENTANTS" size 18 color "#5CD3FF" font "fonts/Barlow-Light.ttf" kerning 4
                    text "Kamyz : [player_kamyz]" size 20 color "#FFE7AE" xalign 1.0

            viewport:
                mousewheel "horizontal"
                draggable True
                scrollbars "horizontal"
                xfill True
                ymaximum 132

                hbox:
                    spacing 12
                    for pid in PROFILE_ORDER:
                        $ pdata = PROFILE_DATA[pid]
                        $ portrait_path = profile_portrait(pid)
                        imagebutton:
                            idle Transform(portrait_path, xsize=96, ysize=96)
                            hover Transform(portrait_path, xsize=102, ysize=102)
                            action SetScreenVariable("selected_profile", pid)

            $ profile = PROFILE_DATA[selected_profile]
            $ affinity_val = profile_affinity[selected_profile]

            frame:
                background Fixed(
                    Solid("#0A1326F2"),
                    Solid("#5CD3FF44", xsize=4),
                    Solid("#5CD3FF44", xsize=4, xalign=1.0),
                    Solid("#FFFFFF12", ysize=1),
                )
                xfill True
                yfill True
                padding (24, 22)

                vbox:
                    spacing 16

                    hbox:
                        xfill True
                        spacing 16
                        text character_display_name(selected_profile) size 42 color "#FFFFFF"
                        textbutton "TENUES":
                            xalign 1.0
                            background Solid("#10384DCC")
                            hover_background Solid("#1D5C7AEE")
                            text_color "#DFF2FF"
                            text_hover_color "#FFFFFF"
                            text_size 22
                            text_xalign 0.5
                            xsize 150
                            ysize 46
                            action Show("profile_wardrobe", profile_id=selected_profile)

                    text "[profile['role']] — District: [profile['district']] — Âge: [profile['age']]" size 24 color "#D2E3F6"

                    hbox:
                        spacing 24
                        xfill True

                        frame:
                            background Fixed(
                                Solid("#07111CEE"),
                                Solid("#5CD3FF33", xsize=3),
                                Solid("#FFFFFF10", ysize=1),
                            )
                            xsize 320
                            ysize 420
                            padding (0, 0)

                            add Transform(profile_portrait(selected_profile), fit="contain", xsize=320, ysize=420)

                        vbox:
                            spacing 10
                            yalign 0.05
                            text "Affinité" size 24 color "#FFFFFF"
                            text "[affinity_val]/100" size 24 color "#FFFFFF"
                            bar:
                                xsize 280
                                ysize 18
                                value AnimatedValue(value=affinity_val, range=100.0, delay=0.25)
                                left_bar Solid("#5CD3FF")
                                right_bar Solid("#152436")

                        null width 10
                        null xfill True

                        frame:
                            background Fixed(
                                Solid("#07111CEE"),
                                Solid("#FFD16633", xsize=3),
                                Solid("#FFFFFF10", ysize=1),
                            )
                            xsize 320
                            ysize 420
                            padding (0, 0)

                            $ equipped_skin = profile_skin_display_image(selected_profile)
                            if equipped_skin:
                                add Transform(equipped_skin, zoom=0.4, xanchor=1.0, yanchor=1.0, xpos=375, ypos=460)
                            else:
                                text "Aucun skin équipé" xalign 0.5 yalign 0.5 color "#D9E2EF"

                    frame:
                        background Fixed(
                            Solid("#060b12DD"),
                            Solid("#FFD16655", xsize=3),
                        )
                        xfill True
                        padding (16, 12)
                        text "« [profile['quote']] »" size 23 color "#FFE7AE" italic True

                    vbox:
                        spacing 8
                        text "Backstory" size 26 color "#9FD4FF"
                        if profile_story_unlocked[selected_profile]:
                            text "[profile['backstory']]" size 22 color "#E8EEF5"
                        else:
                            text "Verrouillé — se débloque pendant les discussions et événements narratifs." size 20 color "#8EA3B8"

                        text "Relations" size 26 color "#9FD4FF"
                        if profile_relations_unlocked[selected_profile]:
                            text "[profile['relations']]" size 22 color "#E8EEF5"
                        else:
                            text "Verrouillé — se débloque pendant les discussions et les interactions clés." size 20 color "#8EA3B8"

                        text "Souvenirs" size 26 color "#9FD4FF"
                        if selected_profile in CHARACTER_LINK_IDS:
                            $ unlocked_memories = character_link_unlocked_memories(selected_profile)
                            if unlocked_memories:
                                hbox:
                                    spacing 8
                                    for memory_id in unlocked_memories:
                                        textbutton "Souvenir [memory_id]":
                                            action Call("REPLAY_CHARACTER_LINK", selected_profile, memory_id)
                            else:
                                text "Aucun souvenir de temps libre débloqué." size 20 color "#8EA3B8"
                        else:
                            text "Aucun souvenir de temps libre disponible." size 20 color "#8EA3B8"


screen profile_wardrobe(profile_id):
    modal True
    zorder 400

    $ detected_skins = get_profile_detected_skins(profile_id)

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
        xsize 920
        ysize 620
        padding (22, 20)

        vbox:
            spacing 14
            text "GARDE-ROBE // [character_display_name(profile_id)]" size 34 color "#DFF2FF" font "fonts/Rajdhani-SemiBold.ttf"
            text "Débloque des skins via des variables persistantes, puis équipe-les ici (appliqués à la partie droite du cadre)." size 20 color "#BFD6EA"

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                ymaximum 430

                vbox:
                    spacing 8
                    for skin_id in detected_skins:
                        $ skin_unlocked = is_profile_skin_unlocked(profile_id, skin_id)
                        $ skin_path = profile_skin_path(profile_id, skin_id)
                        $ display_path = skin_path if renpy.loadable(skin_path) else profile_portrait(profile_id)
                        hbox:
                            spacing 12
                            add Transform(profile_portrait(profile_id), xsize=96, ysize=96)
                            add Transform(
                                display_path,
                                xsize=96,
                                ysize=96,
                                matrixcolor=None if skin_unlocked else SaturationMatrix(0),
                            )
                            if skin_unlocked:
                                textbutton "EQUIPER [skin_id]":
                                    background Solid("#10384DCC")
                                    hover_background Solid("#1D5C7AEE")
                                    text_color "#DFF2FF"
                                    text_hover_color "#FFFFFF"
                                    action Function(equip_profile_skin, profile_id, skin_id)
                            else:
                                text "[skin_id] (verrouillé)" size 22 color "#8EA3B8"

            textbutton "FERMER" action Hide("profile_wardrobe") xalign 1.0 background Solid("#25101ACC") hover_background Solid("#4A1D2AEE") text_color "#FFD6E0"


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
                    text "Kamyz : [player_kamyz]" size 22 color "#FFE7AE"
                    if player_inventory:
                        text "Objets : [', '.join(player_inventory)]" size 19 color "#C8D7E6"
                    else:
                        text "Objets : aucun" size 19 color "#8EA3B8"
