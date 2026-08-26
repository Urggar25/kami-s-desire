# ======================
# ELIAS
# ======================
init -10 python:
    # Les DynamicDisplayable repassent souvent par les memes combinaisons de
    # calques. Conserver le Displayable final evite de recreer en boucle des
    # Composite/Transform lourds et limite la pression sur le ramasse-miettes.
    def kd_cached_layered_sprite(image_size, zoom, asset_paths):
        cache = kd_cached_layered_sprite.cache
        key = (tuple(image_size), zoom, tuple(asset_paths))
        displayable = cache.get(key)
        if displayable is None:
            layers = []
            for path in asset_paths:
                layers.extend(((0, 0), path))
            displayable = Transform(Composite(image_size, *layers), zoom=zoom)
            cache[key] = displayable
        return displayable

    kd_cached_layered_sprite.cache = {}

    def kd_character_asset(character_id, asset_name):
        return "images/character/{}/{}.png".format(character_id, asset_name)

    def kd_character_has_layered_wardrobe(character_id):
        return (
            renpy.loadable(kd_character_asset(character_id, "corps_nu"))
            and renpy.loadable(kd_character_asset(character_id, "tenue1"))
        )

    def kd_equipped_character_outfit(character_id):
        if not kd_character_has_layered_wardrobe(character_id):
            return None

        equipped_map = persistent.profile_skin_equipped or {}
        unlocked_map = persistent.profile_wardrobe_unlocked or {}
        outfit_id = equipped_map.get(character_id, "tenue1")
        unlocked = set(unlocked_map.get(character_id, []))
        unlocked.add("tenue1")

        if outfit_id not in unlocked or not renpy.loadable(kd_character_asset(character_id, outfit_id)):
            outfit_id = "tenue1"
        return outfit_id

    def kd_equipped_character_accessories(character_id):
        equipped_map = persistent.profile_accessory_equipped or {}
        unlocked_map = persistent.profile_accessories_unlocked or {}
        equipped = equipped_map.get(character_id, [])
        if isinstance(equipped, str):
            equipped = [equipped]
        unlocked = set(unlocked_map.get(character_id, []))
        return [
            accessory_id for accessory_id in equipped
            if accessory_id in unlocked and renpy.loadable(kd_character_asset(character_id, accessory_id))
        ]

    def kd_arm_for_outfit(character_id, arm_id, outfit_id):
        if outfit_id and outfit_id != "tenue1":
            outfit_arm = "{}_{}".format(arm_id, outfit_id)
            if renpy.loadable(kd_character_asset(character_id, outfit_arm)):
                return outfit_arm
        return arm_id

    def kd_character_preview_displayable(character_id, outfit_id, accessory_ids, recipe, zoom=0.60, body_name=None):
        arms, mouth, eyes = recipe
        accessories = list(accessory_ids or [])

        if kd_character_has_layered_wardrobe(character_id):
            outfit_id = outfit_id or kd_equipped_character_outfit(character_id) or "tenue1"
            arms = kd_arm_for_outfit(character_id, arms, outfit_id)
            # Ordre de composition commun à tous les écrans : corps nu,
            # tenue, accessoires, bras adaptés à la tenue, puis visage.
            asset_names = ["corps_nu", outfit_id] + accessories + [arms, eyes, mouth]
        else:
            # Compatibilité : le corps historique reste la base lorsque
            # corps_nu/tenue1 n'existent pas.
            asset_names = [body_name or "corps", arms, eyes, mouth] + accessories

        asset_paths = [
            kd_character_asset(character_id, asset_name)
            for asset_name in asset_names
            if renpy.loadable(kd_character_asset(character_id, asset_name))
        ]
        return kd_cached_layered_sprite((1024, 1536), zoom, tuple(asset_paths))

    def kd_layered_sprite_delay(st, blink_period, blink_start, blink_end, speaking):
        # Pendant la parole, la cadence historique de la bouche est conservee.
        # Au repos, le sprite ne se reveille qu'aux changements des paupieres.
        if speaking:
            return 0.08

        phase = st % blink_period
        if phase < blink_start:
            delay = blink_start - phase
        elif phase <= blink_end:
            delay = blink_end - phase + 0.001
        else:
            delay = blink_period - phase + blink_start
        return max(0.04, delay)

init python:
    ELIAS_IMAGE_SIZE = (1024, 1536)
    ELIAS_IMAGE_SCALE = 0.60
    ELIAS_ASSET_DIR = "images/character/elias"

    ELIAS_EXPRESSIONS = {
        "colere": ("corps_1", "bras_croise", "bouche_colere", "yeux_colere"),
        "colere_noire": ("corps_1", "bras_croise", "bouche_colere", "yeux_colere"),
        "content": ("corps_1", "bras_long_corps", "bouche_content", "yeux_content"),
        "desespoir": ("corps_1", "bras_sur_torse", "bouche_decu", "yeux_blase"),
        "ecoute": ("corps_1", "bras_sur_torse", "bouche_neutre", "yeux_neutre"),
        "fatigue": ("corps_1", "bras_sur_torse", "bouche_decu", "yeux_blase"),
        "inquiet": ("corps_1", "bras_sur_torse", "bouche_peur", "yeux_peur"),
        "jaloux": ("corps_1", "bras_croise", "bouche_decu", "yeux_colere"),
        "joie": ("corps_1", "bras_en_air", "bouche_sourire", "yeux_content"),
        "neutre": ("corps_1", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "panique": ("corps_1", "bras_en_air", "bouche_peur", "yeux_peur"),
        "rire": ("corps_1", "bras_en_air", "bouche_sourire", "yeux_content"),
        "reflechit": ("corps_1", "bras_sur_torse", "bouche_neutre", "yeux_blase"),
        "detendu": ("corps_1", "bras_long_corps", "bouche_sourire", "yeux_content"),
        "raison": ("corps_1", "bras_sur_torse", "bouche_neutre", "yeux_neutre"),
        "determine": ("corps_1", "bras_croise", "bouche_neutre", "yeux_colere"),
        "hesitation": ("corps_1", "bras_long_corps", "bouche_decu", "yeux_peur"),
        "choc": ("corps_1", "bras_en_air", "bouche_peur", "yeux_peur"),
        "taquin": ("corps_1", "bras_en_air", "bouche_content", "yeux_content"),
        "surpris": ("corps_1", "bras_sur_torse", "bouche_decu", "yeux_peur"),
        "triste": ("corps_1", "bras_croise", "bouche_decu", "yeux_blase"),
        "peur": ("corps_1", "bras_long_corps", "bouche_peur", "yeux_peur"),
    }

    def _elias_asset(name):
        return "%s/%s.png" % (ELIAS_ASSET_DIR, name)

    def _elias_is_speaking():
        return is_character_speaking("elias")

    def _elias_layered_expression(st, at, expr):
        body, arms, mouth, eyes = ELIAS_EXPRESSIONS[expr]

        blink_phase = st % 5.1
        if 4.82 <= blink_phase <= 4.98:
            eyes = "yeux_ferme"

        zoom = ELIAS_IMAGE_SCALE
        speaking = _elias_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = ELIAS_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            ELIAS_IMAGE_SIZE, zoom,
            (_elias_asset(body), _elias_asset(arms), _elias_asset(eyes), _elias_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 5.1, 4.82, 4.98, speaking)

    def elias_expression(expr):
        return DynamicDisplayable(_elias_layered_expression, expr)

image elias colere            = elias_expression("colere")
image elias colere_noire      = elias_expression("colere_noire")
image elias content           = elias_expression("content")
image elias sourire           = elias_expression("content")
image elias desespoir         = elias_expression("desespoir")
image elias ecoute            = elias_expression("ecoute")
image elias fatigue           = elias_expression("fatigue")
image elias inquiet           = elias_expression("inquiet")
image elias jaloux            = elias_expression("jaloux")
image elias joie              = elias_expression("joie")
image elias neutre            = elias_expression("neutre")
image elias panique           = elias_expression("panique")
image elias rire              = elias_expression("rire")
image elias reflechit         = elias_expression("reflechit")
image elias detendu           = elias_expression("detendu")
image elias raison            = elias_expression("raison")
image elias determine         = elias_expression("determine")
image elias hesitation        = elias_expression("hesitation")
image elias choc              = elias_expression("choc")
image elias taquin              = elias_expression("taquin")
image elias surpris              = elias_expression("surpris")
image elias triste              = elias_expression("triste")
image elias peur              = elias_expression("peur")

# ======================
# MARA
# ======================
init python:
    MARA_IMAGE_SIZE = (1024, 1536)
    MARA_IMAGE_SCALE = 0.60
    MARA_ASSET_DIR = "images/character/mara"

    MARA_EXPRESSIONS = {
        "agace": ("corps", "bras_main_hanche", "bouche_doute", "yeux_mefiant"),
        "colere": ("corps", "bras_main_hanche", "bouche_colere", "yeux_colere"),
        "colere_noire": ("corps", "bras_explication", "bouche_crie", "yeux_colere"),
        "content": ("corps", "bras_main_hanche", "bouche_sourire", "yeux_neutre"),
        "doute": ("corps", "bras_reflexion", "bouche_doute", "yeux_mefiant"),
        "jaloux": ("corps", "bras_main_hanche", "bouche_doute", "yeux_colere"),
        "joie": ("corps", "bras_explication", "bouche_joie", "yeux_joie"),
        "mefiant": ("corps", "bras_main_hanche", "bouche_neutre", "yeux_mefiant"),
        "neutre": ("corps", "bras_main_hanche", "bouche_neutre", "yeux_neutre"),
        "reflexion": ("corps", "bras_reflexion", "bouche_neutre", "yeux_mefiant"),
        "rire": ("corps", "bras_explication", "bouche_joie", "yeux_joie"),
        "rire_profond": ("corps", "bras_explication", "bouche_taquin", "yeux_mefiant"),
        "stress": ("corps", "bras_derriere_tete", "bouche_doute", "yeux_fatigue"),
        "sourire": ("corps", "bras_main_hanche", "bouche_sourire", "yeux_neutre"),
        "taquin": ("corps", "bras_explication", "bouche_taquin", "yeux_mefiant"),
        "fatigue": ("corps", "bras_derriere_tete", "bouche_doute", "yeux_fatigue"),
        "ivre": ("corps", "bras_derriere_tete", "bouche_taquin", "yeux_fatigue"),
        "vide": ("corps", "bras_derriere_tete", "bouche_doute", "yeux_fatigue"),
        "peur": ("corps", "bras_derriere_tete", "bouche_colere", "yeux_mefiant"),
        "triste": ("corps", "bras_main_hanche", "bouche_doute", "yeux_fatigue"),
        "surpris": ("corps", "bras_explication", "bouche_doute", "yeux_mefiant"),
    }

    def _mara_asset(name):
        return "%s/%s.png" % (MARA_ASSET_DIR, name)

    def _mara_is_speaking():
        return is_character_speaking("mara")

    def _mara_layered_expression(st, at, expr):
        body, arms, mouth, eyes = MARA_EXPRESSIONS[expr]

        blink_phase = st % 4.8
        if 4.52 <= blink_phase <= 4.68:
            eyes = "yeux_ferme"

        zoom = MARA_IMAGE_SCALE
        speaking = _mara_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = MARA_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            MARA_IMAGE_SIZE, zoom,
            (_mara_asset(body), _mara_asset(arms), _mara_asset(eyes), _mara_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 4.8, 4.52, 4.68, speaking)

    def mara_expression(expr):
        return DynamicDisplayable(_mara_layered_expression, expr)

image mara agace              = mara_expression("agace")
image mara colere             = mara_expression("colere")
image mara colere_noire       = mara_expression("colere_noire")
image mara content            = mara_expression("content")
image mara doute              = mara_expression("doute")
image mara jaloux             = mara_expression("jaloux")
image mara joie               = mara_expression("joie")
image mara mefiant            = mara_expression("mefiant")
image mara neutre             = mara_expression("neutre")
image mara reflexion          = mara_expression("reflexion")
image mara rire               = mara_expression("rire")
image mara rire_profond       = mara_expression("rire_profond")
image mara stress             = mara_expression("stress")
image mara sourire            = mara_expression("sourire")
image mara taquin             = mara_expression("taquin")
image mara fatigue            = mara_expression("fatigue")
image mara ivre               = mara_expression("ivre")
image mara vide               = mara_expression("vide")
image mara peur               = mara_expression("peur")
image mara reflechit               = mara_expression("reflexion")
image mara triste               = mara_expression("triste")
image mara surpris               = mara_expression("surpris")

# ======================
# NOAM
# ======================
init python:
    NOAM_IMAGE_SIZE = (1024, 1536)
    NOAM_IMAGE_SCALE = 0.60
    NOAM_ASSET_DIR = "images/character/noam"

    NOAM_EXPRESSIONS = {
        "colere": ("corps_nu", "bras_long_corps", "bouche_grimace", "yeux_suspiscion"),
        "culpabilite": ("corps_nu", "bras_devant_soi", "bouche_triste", "yeux_triste"),
        "desaccord": ("corps_nu", "bras_long_corps", "bouche_grimace", "yeux_suspiscion"),
        "desespoir": ("corps_nu", "bras_devant_soi", "bouche_grimace", "yeux_fatigue"),
        "determine": ("corps_nu", "bras_long_corps", "bouche_sourire", "yeux_suspiscion"),
        "hesitation": ("corps_nu", "bras_devant_soi", "bouche_triste", "yeux_triste"),
        "inquiet": ("corps_nu", "bras_devant_soi", "bouche_triste", "yeux_fatigue"),
        "joie": ("corps_nu", "bras_long_corps", "bouche_joie", "yeux_normal"),
        "neutre": ("corps_nu", "bras_long_corps", "bouche_triste", "yeux_normal"),
        "panne": ("corps_nu", "bras_long_corps", "bouche_triste", "yeux_fatigue"),
        "peur": ("corps_nu", "bras_devant_soi", "bouche_grimace", "yeux_surpris"),
        "raison": ("corps_nu", "bras_long_corps", "bouche_sourire", "yeux_normal"),
        "reflexion": ("corps_nu", "bras_devant_soi", "bouche_triste", "yeux_suspiscion"),
        "rire": ("corps_nu", "bras_devant_soi", "bouche_joie", "yeux_normal"),
        "sourire": ("corps_nu", "bras_long_corps", "bouche_sourire", "yeux_normal"),
        "surpris": ("corps_nu", "bras_long_corps", "bouche_joie", "yeux_surpris"),
        "taquin": ("corps_nu", "bras_long_corps", "bouche_taquin", "yeux_suspiscion"),
        "triste": ("corps_nu", "bras_devant_soi", "bouche_triste", "yeux_triste"),
        "fatigue": ("corps_nu", "bras_long_corps", "bouche_triste", "yeux_fatigue"),
        "panique": ("corps_nu", "bras_devant_soi", "bouche_grimace", "yeux_surpris"),
        "panne_creep": ("corps_nu", "bras_long_corps", "bouche_grimace", "yeux_suspiscion"),
        "doute": ("corps_nu", "bras_devant_soi", "bouche_grimace", "yeux_suspiscion"),
        "calme": ("corps_nu", "bras_long_corps", "bouche_sourire", "yeux_fatigue"),
    }

    def _noam_asset(name):
        return "%s/%s.png" % (NOAM_ASSET_DIR, name)

    def _noam_is_speaking():
        return is_character_speaking("noam")

    def _noam_layered_expression(st, at, expr):
        body, arms, mouth, eyes = NOAM_EXPRESSIONS[expr]
        outfit = kd_equipped_character_outfit("noam") or "tenue1"
        arms = kd_arm_for_outfit("noam", arms, outfit)
        accessories = kd_equipped_character_accessories("noam")

        blink_phase = st % 4.9
        if 4.62 <= blink_phase <= 4.78:
            eyes = "yeux_ferme"

        zoom = NOAM_IMAGE_SCALE
        speaking = _noam_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = NOAM_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        asset_names = [body, outfit] + accessories + [arms, eyes, mouth]
        asset_paths = tuple(
            _noam_asset(asset_name)
            for asset_name in asset_names
            if renpy.loadable(_noam_asset(asset_name))
        )
        displayable = kd_cached_layered_sprite(NOAM_IMAGE_SIZE, zoom, asset_paths)
        return displayable, kd_layered_sprite_delay(st, 4.9, 4.62, 4.78, speaking)

    def noam_expression(expr):
        return DynamicDisplayable(_noam_layered_expression, expr)

image noam colere              = noam_expression("colere")
image noam colere2             = noam_expression("colere")
image noam culpabilite         = noam_expression("culpabilite")
image noam desaccord           = noam_expression("desaccord")
image noam desespoir           = noam_expression("desespoir")
image noam determine           = noam_expression("determine")
image noam hesitation          = noam_expression("hesitation")
image noam inquiet             = noam_expression("inquiet")
image noam joie                = noam_expression("joie")
image noam neutre              = noam_expression("neutre")
image noam vide                = noam_expression("neutre")
image noam panne               = noam_expression("panne")
image noam peur                = noam_expression("peur")
image noam raison              = noam_expression("raison")
image noam reflexion           = noam_expression("reflexion")
image noam reflechit           = noam_expression("reflexion")
image noam rire                = noam_expression("rire")
image noam sourire             = noam_expression("sourire")
image noam surpris             = noam_expression("surpris")
image noam taquin              = noam_expression("taquin")
image noam triste              = noam_expression("triste")
image noam fatigue             = noam_expression("fatigue")
image noam faible              = noam_expression("fatigue")
image noam panique             = noam_expression("panique")
image noam panne_creep         = noam_expression("panne_creep")
image noam doute         = noam_expression("doute")
image noam calme         = noam_expression("calme")
image noam blase         = noam_expression("neutre")

# ======================
# LYSA
# ======================
init python:
    LYSA_IMAGE_SIZE = (1024, 1536)
    LYSA_IMAGE_SCALE = 0.60
    LYSA_ASSET_DIR = "images/character/lysa"

    LYSA_EXPRESSIONS = {
        "blase": ("corps", "bras_long_corps", "bouche_neutre", "yeux_blase"),
        "colere": ("corps", "bras_croise", "bouche_colere", "yeux_colere"),
        "content": ("corps", "bras_intervention", "bouche_content", "yeux_content"),
        "culpabilite": ("corps", "bras_supliant", "bouche_triste", "yeux_triste"),
        "desespoir": ("corps", "bras_intervention", "bouche_surpris", "yeux_surpris"),
        "determine": ("corps", "bras_long_corps", "bouche_neutre", "yeux_colere"),
        "inquiet": ("corps", "bras_intervention", "bouche_triste", "yeux_triste"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_content"),
        "opposition": ("corps", "bras_intervention", "bouche_colere", "yeux_colere"),
        "panne": ("corps", "bras_long_corps", "bouche_surpris", "yeux_surpris"),
        "peur": ("corps", "bras_supliant", "bouche_triste", "yeux_surpris"),
        "reflexion": ("corps", "bras_croise", "bouche_neutre", "yeux_blase"),
        "raison": ("corps", "bras_croise", "bouche_neutre", "yeux_content"),
        "rire": ("corps", "bras_supliant", "bouche_rire", "yeux_content"),
        "salut": ("corps", "bras_intervention", "bouche_content", "yeux_content"),
        "sourire": ("corps", "bras_intervention", "bouche_content", "yeux_content"),
        "surpris": ("corps", "bras_intervention", "bouche_surpris", "yeux_surpris"),
        "taquin": ("corps", "bras_intervention", "bouche_content", "yeux_blase"),
        "triste": ("corps", "bras_supliant", "bouche_triste", "yeux_triste"),
        "fatigue": ("corps", "bras_intervention", "bouche_triste", "yeux_blase"),
        "doute": ("corps", "bras_intervention", "bouche_neutre", "yeux_triste"),
        "jaloux": ("corps", "bras_croise", "bouche_colere", "yeux_triste"),
        "gene": ("corps", "bras_supliant", "bouche_triste", "yeux_content"),
        "choc": ("corps", "bras_intervention", "bouche_surpris", "yeux_surpris"),
        "desaccord": ("corps", "bras_croise", "bouche_colere", "yeux_colere"),
    }

    def _lysa_asset(name):
        return "%s/%s.png" % (LYSA_ASSET_DIR, name)

    def _lysa_is_speaking():
        return is_character_speaking("lysa")

    def _lysa_layered_expression(st, at, expr):
        body, arms, mouth, eyes = LYSA_EXPRESSIONS[expr]

        blink_phase = st % 4.8
        if 4.52 <= blink_phase <= 4.68:
            eyes = "yeux_ferme"

        zoom = LYSA_IMAGE_SCALE
        speaking = _lysa_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = LYSA_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        asset_paths = [_lysa_asset(body), _lysa_asset(arms), _lysa_asset(eyes), _lysa_asset(mouth)]
        asset_paths.extend(_lysa_asset(accessory_id) for accessory_id in kd_equipped_character_accessories("lysa"))
        displayable = kd_cached_layered_sprite(LYSA_IMAGE_SIZE, zoom, tuple(asset_paths))
        return displayable, kd_layered_sprite_delay(st, 4.8, 4.52, 4.68, speaking)

    def lysa_expression(expr):
        return DynamicDisplayable(_lysa_layered_expression, expr)

image lysa blase               = lysa_expression("blase")
image lysa colere              = lysa_expression("colere")
image lysa content             = lysa_expression("content")
image lysa culpabilite         = lysa_expression("culpabilite")
image lysa desespoir           = lysa_expression("desespoir")
image lysa determine           = lysa_expression("determine")
image lysa inquiet             = lysa_expression("inquiet")
image lysa neutre              = lysa_expression("neutre")
image lysa opposition          = lysa_expression("opposition")
image lysa panne               = lysa_expression("panne")
image lysa peur                = lysa_expression("peur")
image lysa reflexion           = lysa_expression("reflexion")
image lysa reflechit           = lysa_expression("reflexion")
image lysa raison              = lysa_expression("raison")
image lysa rire                = lysa_expression("rire")
image lysa salut               = lysa_expression("salut")
image lysa sourire             = lysa_expression("sourire")
image lysa surpris             = lysa_expression("surpris")
image lysa taquin              = lysa_expression("taquin")
image lysa triste              = lysa_expression("triste")
image lysa fatigue             = lysa_expression("fatigue")
image lysa doute               = lysa_expression("doute")
image lysa jaloux              = lysa_expression("jaloux")
image lysa gene                = lysa_expression("gene")
image lysa choc                = lysa_expression("choc")
image lysa desaccord           = lysa_expression("desaccord")

# ======================
# JULIAN
# ======================
init python:
    JULIAN_IMAGE_SIZE = (1024, 1536)
    JULIAN_IMAGE_SCALE = 0.60
    JULIAN_ASSET_DIR = "images/character/julian"

    JULIAN_EXPRESSIONS = {
        "decu": ("corps", "bras_croise", "bouche_triste", "yeux_inquiet"),
        "determine": ("corps", "bras_croise", "bouche_neutre", "yeux_reflexion"),
        "hesitation": ("corps", "bras_sur_tete", "bouche_inquiet", "yeux_inquiet"),
        "idee": ("corps", "bras_idee", "bouche_sourire", "yeux_content"),
        "inquiet": ("corps", "bras_sur_tete", "bouche_inquiet", "yeux_inquiet"),
        "joie": ("corps", "bras_idee", "bouche_joie", "yeux_content"),
        "neutre": ("corps", "bras_reflexion", "bouche_neutre", "yeux_neutre"),
        "panne": ("corps", "bras_croise", "bouche_neutre", "yeux_neutre"),
        "peur": ("corps", "bras_sur_tete", "bouche_surpris", "yeux_surpris"),
        "reflexion": ("corps", "bras_reflexion", "bouche_neutre", "yeux_reflexion"),
        "rire": ("corps", "bras_idee", "bouche_joie", "yeux_content"),
        "sourire": ("corps", "bras_reflexion", "bouche_sourire", "yeux_content"),
        "surpris": ("corps", "bras_sur_tete", "bouche_surpris", "yeux_surpris"),
        "taquin": ("corps", "bras_idee", "bouche_sourire", "yeux_reflexion"),
        "triste": ("corps", "bras_croise", "bouche_triste", "yeux_inquiet"),
        "detendu": ("corps", "bras_reflexion", "bouche_sourire", "yeux_neutre"),
        "decontracte": ("corps", "bras_reflexion", "bouche_sourire", "yeux_content"),
        "colere": ("corps", "bras_croise", "bouche_inquiet", "yeux_reflexion"),
    }

    def _julian_asset(name):
        return "%s/%s.png" % (JULIAN_ASSET_DIR, name)

    def _julian_is_speaking():
        return is_character_speaking("julian")

    def _julian_layered_expression(st, at, expr):
        body, arms, mouth, eyes = JULIAN_EXPRESSIONS[expr]

        blink_phase = st % 5.0
        if 4.72 <= blink_phase <= 4.88:
            eyes = "yeux_ferme"

        zoom = JULIAN_IMAGE_SCALE
        speaking = _julian_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = JULIAN_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            JULIAN_IMAGE_SIZE, zoom,
            (_julian_asset(body), _julian_asset(arms), _julian_asset(eyes), _julian_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 5.0, 4.72, 4.88, speaking)

    def julian_expression(expr):
        return DynamicDisplayable(_julian_layered_expression, expr)

image julian decu               = julian_expression("decu")
image julian determine          = julian_expression("determine")
image julian hesitation         = julian_expression("hesitation")
image julian idee               = julian_expression("idee")
image julian inquiet            = julian_expression("inquiet")
image julian inquietude         = julian_expression("inquiet")
image julian joie               = julian_expression("joie")
image julian neutre             = julian_expression("neutre")
image julian panne              = julian_expression("panne")
image julian peur               = julian_expression("peur")
image julian reflexion          = julian_expression("reflexion")
image julian reflechit          = julian_expression("reflexion")
image julian rire               = julian_expression("rire")
image julian sourire            = julian_expression("sourire")
image julian surpris            = julian_expression("surpris")
image julian taquin             = julian_expression("taquin")
image julian triste             = julian_expression("triste")
image julian detendu            = julian_expression("detendu")
image julian decontracte        = julian_expression("decontracte")
image julian colere             = julian_expression("colere")
image julian fatigue            = julian_expression("triste")
image julian blase              = julian_expression("neutre")
image julian content            = julian_expression("joie")

# ======================
# IRIS
# ======================
init python:
    IRIS_IMAGE_SIZE = (1024, 1536)
    IRIS_IMAGE_SCALE = 0.60
    IRIS_ASSET_DIR = "images/character/iris"

    IRIS_EXPRESSIONS = {
        "colere": ("corps", "bras_croise", "bouche_colere", "yeux_colere"),
        "culpabilite": ("corps", "bras_timide", "bouche_grimace", "yeux_triste"),
        "desaccord": ("corps", "bras_croise", "bouche_grimace", "yeux_colere"),
        "determine": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_colere"),
        "fatigue": ("corps", "bras_long_corps", "bouche_triste", "yeux_triste"),
        "gene": ("corps", "bras_timide", "bouche_grimace", "yeux_doux"),
        "hesitation": ("corps", "bras_timide", "bouche_grimace", "yeux_doux"),
        "inquiet": ("corps", "bras_timide", "bouche_triste", "yeux_triste"),
        "intervention": ("corps", "bras_devant_soi", "bouche_colere", "yeux_colere"),
        "joie": ("corps", "bras_sur_de_lui", "bouche_joie", "yeux_doux"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "panne": ("corps", "bras_long_corps", "bouche_grimace", "yeux_neutre"),
        "peur": ("corps", "bras_timide", "bouche_surprise", "yeux_triste"),
        "reflexion": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_neutre"),
        "rire": ("corps", "bras_sur_de_lui", "bouche_joie", "yeux_doux"),
        "sourire": ("corps", "bras_long_corps", "bouche_sourire", "yeux_doux"),
        "surpris": ("corps", "bras_sur_de_lui", "bouche_surprise", "yeux_neutre"),
        "surprise": ("corps", "bras_sur_de_lui", "bouche_surprise", "yeux_neutre"),
        "taquin": ("corps", "bras_devant_soi", "bouche_sourire", "yeux_doux"),
        "triste": ("corps", "bras_long_corps", "bouche_triste", "yeux_triste"),
        "blase": ("corps", "bras_croise", "bouche_grimace", "yeux_colere"),
        "vide": ("corps", "bras_croise", "bouche_grimace", "yeux_colere"),
    }

    def _iris_asset(name):
        return "%s/%s.png" % (IRIS_ASSET_DIR, name)

    def _iris_is_speaking():
        return is_character_speaking("iris")

    def _iris_layered_expression(st, at, expr):
        body, arms, mouth, eyes = IRIS_EXPRESSIONS[expr]

        blink_phase = st % 4.9
        if 4.62 <= blink_phase <= 4.78:
            eyes = "yeux_ferme"

        zoom = IRIS_IMAGE_SCALE
        speaking = _iris_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = IRIS_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        if kd_character_has_layered_wardrobe("iris"):
            outfit = kd_equipped_character_outfit("iris")
            arms = kd_arm_for_outfit("iris", arms, outfit)
            asset_names = ["corps_nu", outfit]
            asset_names.extend(kd_equipped_character_accessories("iris"))
            asset_names.extend((arms, mouth, eyes))
            asset_paths = tuple(_iris_asset(asset_name) for asset_name in asset_names)
        else:
            asset_paths = (_iris_asset(body), _iris_asset(arms), _iris_asset(eyes), _iris_asset(mouth))

        displayable = kd_cached_layered_sprite(IRIS_IMAGE_SIZE, zoom, asset_paths)
        return displayable, kd_layered_sprite_delay(st, 4.9, 4.62, 4.78, speaking)

    def iris_expression(expr):
        return DynamicDisplayable(_iris_layered_expression, expr)

image iris colere               = iris_expression("colere")
image iris culpabilite          = iris_expression("culpabilite")
image iris determine            = iris_expression("determine")
image iris fatigue              = iris_expression("fatigue")
image iris hesitation           = iris_expression("hesitation")
image iris inquiet              = iris_expression("inquiet")
image iris joie                 = iris_expression("joie")
image iris neutre               = iris_expression("neutre")
image iris panne                = iris_expression("panne")
image iris peur                 = iris_expression("peur")
image iris reflexion            = iris_expression("reflexion")
image iris reflechit            = iris_expression("reflexion")
image iris rire                 = iris_expression("rire")
image iris sourire              = iris_expression("sourire")
image iris surpris              = iris_expression("surpris")
image iris surprise             = iris_expression("surprise")
image iris taquin               = iris_expression("taquin")
image iris triste               = iris_expression("triste")
image iris desaccord            = iris_expression("desaccord")
image iris intervention         = iris_expression("intervention")
image iris gene                 = iris_expression("gene")
image iris blase                 = iris_expression("blase")
image iris vide                 = iris_expression("vide")

# ======================
# TOMAS
# ======================
init python:
    TOMAS_IMAGE_SIZE = (1024, 1536)
    TOMAS_IMAGE_SCALE = 0.60
    TOMAS_ASSET_DIR = "images/character/tomas"

    TOMAS_EXPRESSIONS = {
        "colere": ("base", "bras_poing_serre", "bouche_colere", "yeux_colere"),
        "colere_noire": ("base", "bras_poing_serre", "bouche_colere", "yeux_colere"),
        "culpabilite": ("base", "bras_devant_soi", "bouche_triste", "yeux_culpabilite"),
        "desaccord": ("base", "bras_poing_serre", "bouche_colere", "yeux_colere"),
        "desespoir": ("base", "bras_devant_soi", "bouche_peur", "yeux_peur"),
        "determine": ("base", "bras_poing_serre", "bouche_neutre", "yeux_colere"),
        "fatigue": ("base", "bras_poche", "bouche_triste", "yeux_culpabilite"),
        "gene": ("base", "bras_devant_soi", "bouche_triste", "yeux_neutre"),
        "hesitation": ("base", "bras_devant_soi", "bouche_neutre", "yeux_culpabilite"),
        "hoche_la_tete": ("base", "bras_poche", "bouche_neutre", "yeux_neutre"),
        "inquiet": ("base", "bras_devant_soi", "bouche_peur", "yeux_peur"),
        "joie": ("base", "bras_devant_soi", "bouche_joie", "yeux_neutre"),
        "mefiant": ("base", "bras_poche", "bouche_neutre", "yeux_colere"),
        "neutre": ("base", "bras_poche", "bouche_neutre", "yeux_neutre"),
        "panne": ("base", "bras_poche", "bouche_neutre", "yeux_culpabilite"),
        "peur": ("base", "bras_devant_soi", "bouche_peur", "yeux_peur"),
        "raison": ("base", "bras_devant_soi", "bouche_neutre", "yeux_neutre"),
        "reflechit": ("base", "bras_devant_soi", "bouche_neutre", "yeux_culpabilite"),
        "reflexion": ("base", "bras_devant_soi", "bouche_neutre", "yeux_culpabilite"),
        "rire": ("base", "bras_devant_soi", "bouche_joie", "yeux_neutre"),
        "sourire": ("base", "bras_poche", "bouche_joie", "yeux_neutre"),
        "stress": ("base", "bras_devant_soi", "bouche_peur", "yeux_peur"),
        "surpris": ("base", "bras_devant_soi", "bouche_peur", "yeux_peur"),
        "taquin": ("base", "bras_poche", "bouche_joie", "yeux_neutre"),
        "triste": ("base", "bras_devant_soi", "bouche_triste", "yeux_culpabilite"),
        "vide": ("base", "bras_poche", "bouche_neutre", "yeux_neutre"),
    }

    def _tomas_asset(name):
        return "%s/%s.png" % (TOMAS_ASSET_DIR, name)

    def _tomas_is_speaking():
        return is_character_speaking("tomas")

    def _tomas_layered_expression(st, at, expr):
        body, arms, mouth, eyes = TOMAS_EXPRESSIONS.get(expr, TOMAS_EXPRESSIONS["neutre"])

        blink_phase = st % 4.85
        if 4.55 <= blink_phase <= 4.72:
            eyes = "yeux_ferme"

        zoom = TOMAS_IMAGE_SCALE
        speaking = _tomas_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = TOMAS_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            TOMAS_IMAGE_SIZE, zoom,
            (_tomas_asset(body), _tomas_asset(arms), _tomas_asset(eyes), _tomas_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 4.85, 4.55, 4.72, speaking)

    def tomas_expression(expr):
        return DynamicDisplayable(_tomas_layered_expression, expr)

image tomas colere              = tomas_expression("colere")
image tomas colere_noire        = tomas_expression("colere_noire")
image tomas culpabilite         = tomas_expression("culpabilite")
image tomas desaccord           = tomas_expression("desaccord")
image tomas desespoir           = tomas_expression("desespoir")
image tomas determine           = tomas_expression("determine")
image tomas fatigue             = tomas_expression("fatigue")
image tomas gene                = tomas_expression("gene")
image tomas hesitation          = tomas_expression("hesitation")
image tomas hoche_la_tete       = tomas_expression("hoche_la_tete")
image tomas inquiet             = tomas_expression("inquiet")
image tomas joie                = tomas_expression("joie")
image tomas mefiant             = tomas_expression("mefiant")
image tomas neutre              = tomas_expression("neutre")
image tomas panne               = tomas_expression("panne")
image tomas peur                = tomas_expression("peur")
image tomas raison              = tomas_expression("raison")
image tomas reflechit           = tomas_expression("reflechit")
image tomas reflexion           = tomas_expression("reflexion")
image tomas rire                = tomas_expression("rire")
image tomas sourire             = tomas_expression("sourire")
image tomas stress              = tomas_expression("stress")
image tomas surpris             = tomas_expression("surpris")
image tomas taquin              = tomas_expression("taquin")
image tomas triste              = tomas_expression("triste")
image tomas vide                = tomas_expression("vide")

# ======================
# ELEN
# ======================
init python:
    ELEN_IMAGE_SIZE = (1024, 1536)
    ELEN_IMAGE_SCALE = 0.60
    ELEN_ASSET_DIR = "images/character/elen"

    ELEN_EXPRESSIONS = {
        "choque": ("corps_1", "bras_surpris", "bouche_surpris", "yeux_surpris"),
        "colere": ("corps_1", "bras_main_croise", "bouche_colere", "yeux_colere"),
        "colere_noire": ("corps_1", "bras_main_croise", "bouche_colere_noire", "yeux_colere_noire"),
        "content": ("corps_1", "bras_long_corps", "bouche_content", "yeux_content"),
        "decu": ("corps_1", "bras_long_corps", "bouche_decu", "yeux_decu"),
        "desaccord": ("corps_1", "bras_main_croise", "bouche_decu", "yeux_colere"),
        "determine": ("corps_1", "bras_explication", "bouche_neutre", "yeux_colere"),
        "inquiet": ("corps_1", "bras_derriere_tete", "bouche_inquiet", "yeux_inquiet"),
        "joie": ("corps_1", "bras_surpris", "bouche_joie", "yeux_joie"),
        "neutre": ("corps_1", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "peur": ("corps_1", "bras_surpris", "bouche_peur", "yeux_surpris"),
        "reflexion": ("corps_1", "bras_derriere_tete", "bouche_neutre", "yeux_decu"),
        "rire": ("corps_1", "bras_surpris", "bouche_joie", "yeux_joie"),
        "surpris": ("corps_1", "bras_surpris", "bouche_surpris", "yeux_surpris"),
        "taquin": ("corps_1", "bras_explication", "bouche_content", "yeux_content"),
        "triste": ("corps_1", "bras_long_corps", "bouche_decu", "yeux_decu"),
        "fatigue": ("corps_1", "bras_derriere_tete", "bouche_decu", "yeux_decu"),
        "sourire": ("corps_1", "bras_main_croise", "bouche_joie", "yeux_content"),
        "vide": ("corps_1", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
    }

    def _elen_asset(name):
        return "%s/%s.png" % (ELEN_ASSET_DIR, name)

    def _elen_is_speaking():
        return is_character_speaking("elen")

    def _elen_layered_expression(st, at, expr):
        body, arms, mouth, eyes = ELEN_EXPRESSIONS[expr]

        blink_phase = st % 4.8
        if 4.52 <= blink_phase <= 4.68:
            eyes = "yeux_ferme"

        zoom = ELEN_IMAGE_SCALE
        speaking = _elen_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = ELEN_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            ELEN_IMAGE_SIZE, zoom,
            (_elen_asset(body), _elen_asset(arms), _elen_asset(eyes), _elen_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 4.8, 4.52, 4.68, speaking)

    def elen_expression(expr):
        return DynamicDisplayable(_elen_layered_expression, expr)

# image elen choque               = im.FactorScale("images/character/elen/choque.png", 0.60)
image elen choque               = elen_expression("choque")
# image elen colere               = im.FactorScale("images/character/elen/colere.png", 0.60)
image elen colere               = elen_expression("colere")
# image elen colere_noire         = im.FactorScale("images/character/elen/colere_noire.png", 0.60)
image elen colere_noire         = elen_expression("colere_noire")
# image elen content              = im.FactorScale("images/character/elen/content.png", 0.60)
image elen content              = elen_expression("content")
# image elen decu                 = im.FactorScale("images/character/elen/decu.png", 0.60)
image elen decu                 = elen_expression("decu")
# image elen desaccord            = im.FactorScale("images/character/elen/desaccord.png", 0.60)
image elen desaccord            = elen_expression("desaccord")
# image elen determine            = im.FactorScale("images/character/elen/determine.png", 0.60)
image elen determine            = elen_expression("determine")
# image elen inquiet              = im.FactorScale("images/character/elen/inquiet.png", 0.60)
image elen inquiet              = elen_expression("inquiet")
# image elen joie                 = im.FactorScale("images/character/elen/joie.png", 0.60)
image elen joie                 = elen_expression("joie")
# image elen neutre               = im.FactorScale("images/character/elen/neutre.png", 0.60)
image elen neutre               = elen_expression("neutre")
# image elen peur                 = im.FactorScale("images/character/elen/peur.png", 0.60)
image elen peur                 = elen_expression("peur")
# image elen reflexion            = im.FactorScale("images/character/elen/reflechit.png", 0.60)
image elen reflexion            = elen_expression("reflexion")
image elen reflechit            = elen_expression("reflexion")
# image elen rire                 = im.FactorScale("images/character/elen/rire.png", 0.60)
image elen rire                 = elen_expression("rire")
# image elen surpris              = im.FactorScale("images/character/elen/surpris.png", 0.60)
image elen surpris              = elen_expression("surpris")
# image elen taquin               = im.FactorScale("images/character/elen/taquin.png", 0.60)
image elen taquin               = elen_expression("taquin")
# image elen triste               = im.FactorScale("images/character/elen/triste.png", 0.60)
image elen triste               = elen_expression("triste")
# image elen fatigue               = im.FactorScale("images/character/elen/fatigue.png", 0.60)
image elen fatigue              = elen_expression("fatigue")
image elen sourire              = elen_expression("sourire")
# image elen vide              = im.FactorScale("images/character/vide.png", 0.60)
image elen vide                 = elen_expression("vide")
image elen hesitation           = elen_expression("inquiet")

# ======================
# KAEL
# ======================
init python:
    KAEL_IMAGE_SIZE = (1024, 1536)
    KAEL_IMAGE_SCALE = 0.60
    KAEL_ASSET_DIR = "images/character/kael"

    KAEL_EXPRESSIONS = {
        "calme": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "culpabilite": ("corps", "bras_gene", "bouche_triste", "yeux_decu"),
        "fatigue": ("corps", "bras_long_corps", "bouche_triste", "yeux_fatigue"),
        "inquiet": ("corps", "bras_devant_soi", "bouche_triste", "yeux_decu"),
        "inquietude": ("corps", "bras_devant_soi", "bouche_triste", "yeux_decu"),
        "jaloux": ("corps", "bras_devant_soi", "bouche_colere", "yeux_colere"),
        "joie": ("corps", "bras_devant_soi", "bouche_joie", "yeux_joie"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "reflechit": ("corps", "bras_reflexion", "bouche_neutre", "yeux_decu"),
        "rire": ("corps", "bras_devant_soi", "bouche_joie", "yeux_joie"),
        "sourire": ("corps", "bras_long_corps", "bouche_joie", "yeux_joie"),
        "surpris": ("corps", "bras_devant_soi", "bouche_desespoir", "yeux_neutre"),
        "taquin": ("corps", "bras_reflexion", "bouche_joie", "yeux_joie"),
        "triste": ("corps", "bras_long_corps", "bouche_triste", "yeux_decu"),
        "doute": ("corps", "bras_reflexion", "bouche_neutre", "yeux_decu"),
        "colere": ("corps", "bras_devant_soi", "bouche_colere", "yeux_colere"),
        "mefiant": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_colere"),
        "gene": ("corps", "bras_gene", "bouche_neutre", "yeux_decu"),
        "effondre": ("corps", "bras_long_corps", "bouche_desespoir", "yeux_fatigue"),
        "raison": ("corps", "bras_reflexion", "bouche_neutre", "yeux_neutre"),
        "peur": ("corps", "bras_gene", "bouche_desespoir", "yeux_decu"),
        "desespoir": ("corps", "bras_long_corps", "bouche_desespoir", "yeux_decu"),
    }

    def _kael_asset(name):
        return "%s/%s.png" % (KAEL_ASSET_DIR, name)

    def _kael_is_speaking():
        return is_character_speaking("kael")

    def _kael_layered_expression(st, at, expr):
        body, arms, mouth, eyes = KAEL_EXPRESSIONS[expr]

        blink_phase = st % 5.2
        if 4.92 <= blink_phase <= 5.08:
            eyes = "yeux_ferme"

        zoom = KAEL_IMAGE_SCALE
        speaking = _kael_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = KAEL_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            KAEL_IMAGE_SIZE, zoom,
            (_kael_asset(body), _kael_asset(arms), _kael_asset(eyes), _kael_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 5.2, 4.92, 5.08, speaking)

    def kael_expression(expr):
        return DynamicDisplayable(_kael_layered_expression, expr)

image kael calme               = kael_expression("calme")
image kael culpabilite         = kael_expression("culpabilite")
image kael fatigue             = kael_expression("fatigue")
image kael inquiet             = kael_expression("inquiet")
image kael inquietude          = kael_expression("inquietude")
image kael jaloux              = kael_expression("jaloux")
image kael joie                = kael_expression("joie")
image kael neutre              = kael_expression("neutre")
image kael reflechit           = kael_expression("reflechit")
image kael rire                = kael_expression("rire")
image kael sourire             = kael_expression("sourire")
image kael surpris             = kael_expression("surpris")
image kael taquin              = kael_expression("taquin")
image kael triste              = kael_expression("triste")
image kael doute               = kael_expression("doute")
image kael colere              = kael_expression("colere")
image kael mefiant             = kael_expression("mefiant")
image kael gene                = kael_expression("gene")
image kael effondre            = kael_expression("effondre")
image kael raison              = kael_expression("raison")
image kael peur                = kael_expression("peur")
image kael desespoir           = kael_expression("desespoir")
image kael determine           = kael_expression("calme")
image kael reflexion           = kael_expression("reflechit")
image kael hesitation          = kael_expression("doute")

# ======================
# NYRA
# ======================
init python:
    NYRA_IMAGE_SIZE = (1024, 1536)
    NYRA_IMAGE_SCALE = 0.60
    NYRA_ASSET_DIR = "images/character/nyra"

    NYRA_EXPRESSIONS = {
        "colere": ("corps", "bras_long_corps", "bouche_colere", "yeux_colere"),
        "culpabilite": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_culpabilite"),
        "degout": ("corps", "bras_long_corps", "bouche_colere", "yeux_colere"),
        "determine": ("corps", "bras_long_corps", "bouche_neutre", "yeux_colere"),
        "fatigue": ("corps", "bras_long_corps", "bouche_neutre", "yeux_triste"),
        "hesitation": ("corps", "bras_devant_soi", "bouche_peur", "yeux_culpabilite"),
        "inquiet": ("corps", "bras_devant_soi", "bouche_peur", "yeux_surpris"),
        "joie": ("corps", "bras_sur", "bouche_content", "yeux_neutre"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "panne": ("corps", "bras_long_corps", "bouche_neutre", "yeux_triste"),
        "raison": ("corps", "bras_sur", "bouche_neutre", "yeux_neutre"),
        "reflexion": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_culpabilite"),
        "rire": ("corps", "bras_sur", "bouche_rire", "yeux_neutre"),
        "sourire": ("corps", "bras_long_corps", "bouche_content", "yeux_neutre"),
        "surpris": ("corps", "bras_devant_soi", "bouche_peur", "yeux_surpris"),
        "taquin": ("corps", "bras_sur", "bouche_content", "yeux_colere"),
        "triste": ("corps", "bras_devant_soi", "bouche_neutre", "yeux_triste"),
        "stress": ("corps", "bras_devant_soi", "bouche_peur", "yeux_culpabilite"),
        "vide": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "peur": ("corps", "bras_devant_soi", "bouche_peur", "yeux_colere"),
    }

    def _nyra_asset(name):
        return "%s/%s.png" % (NYRA_ASSET_DIR, name)

    def _nyra_is_speaking():
        return is_character_speaking("nyra")

    def _nyra_layered_expression(st, at, expr):
        body, arms, mouth, eyes = NYRA_EXPRESSIONS[expr]

        blink_phase = st % 5.0
        if 4.72 <= blink_phase <= 4.88:
            eyes = "yeux_ferme"

        zoom = NYRA_IMAGE_SCALE
        speaking = _nyra_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = NYRA_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            NYRA_IMAGE_SIZE, zoom,
            (_nyra_asset(body), _nyra_asset(arms), _nyra_asset(eyes), _nyra_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 5.0, 4.72, 4.88, speaking)

    def nyra_expression(expr):
        return DynamicDisplayable(_nyra_layered_expression, expr)

image nyra colere               = nyra_expression("colere")
image nyra culpabilite          = nyra_expression("culpabilite")
image nyra degout               = nyra_expression("degout")
image nyra determine            = nyra_expression("determine")
image nyra fatigue              = nyra_expression("fatigue")
image nyra hesitation           = nyra_expression("hesitation")
image nyra inquiet              = nyra_expression("inquiet")
image nyra joie                 = nyra_expression("joie")
image nyra neutre               = nyra_expression("neutre")
image nyra panne                = nyra_expression("panne")
image nyra raison               = nyra_expression("raison")
image nyra reflexion            = nyra_expression("reflexion")
image nyra rire                 = nyra_expression("rire")
image nyra sourire              = nyra_expression("sourire")
image nyra surpris              = nyra_expression("surpris")
image nyra taquin               = nyra_expression("taquin")
image nyra triste               = nyra_expression("triste")
image nyra stress               = nyra_expression("stress")
image nyra vide                 = nyra_expression("vide")
image nyra peur                 = nyra_expression("peur")
image nyra reflechit                 = nyra_expression("reflexion")

# ======================
# RYN
# ======================
init python:
    RYN_IMAGE_SIZE = (1024, 1536)
    RYN_IMAGE_SCALE = 0.60
    RYN_ASSET_DIR = "images/character/ryn"

    RYN_EXPRESSIONS = {
        "blase": ("corps", "bras_long_corps", "bouche_neutre", "yeux_blase"),
        "colere": ("corps", "bras_long_corps", "bouche_colere", "yeux_colere"),
        "colere2": ("corps", "bras_derriere_tete", "bouche_colere", "yeux_colere"),
        "decontracte": ("corps", "bras_derriere_tete", "bouche_sourire", "yeux_taquin"),
        "desaccord": ("corps", "bras_long_corps", "bouche_colere", "yeux_colere"),
        "determine": ("corps", "bras_long_corps", "bouche_neutre", "yeux_colere"),
        "fatigue": ("corps", "bras_derriere_tete", "bouche_triste", "yeux_blase"),
        "hesitation": ("corps", "bras_derriere_tete", "bouche_inquiet", "yeux_surpris"),
        "inquiet": ("corps", "bras_long_corps", "bouche_inquiet", "yeux_surpris"),
        "jaloux": ("corps", "bras_long_corps", "bouche_colere", "yeux_taquin"),
        "joie": ("corps", "bras_derriere_tete", "bouche_sourire", "yeux_neutre"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "reflechit": ("corps", "bras_derriere_tete", "bouche_neutre", "yeux_blase"),
        "rire": ("corps", "bras_derriere_tete", "bouche_rire", "yeux_taquin"),
        "sourire": ("corps", "bras_derriere_tete", "bouche_sourire", "yeux_neutre"),
        "surpris": ("corps", "bras_long_corps", "bouche_inquiet", "yeux_surpris"),
        "taquin": ("corps", "bras_derriere_tete", "bouche_sourire", "yeux_taquin"),
        "triste": ("corps", "bras_long_corps", "bouche_triste", "yeux_blase"),
        "vide": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
    }

    def _ryn_asset(name):
        return "%s/%s.png" % (RYN_ASSET_DIR, name)

    def _ryn_is_speaking():
        return is_character_speaking("ryn")

    def _ryn_layered_expression(st, at, expr):
        body, arms, mouth, eyes = RYN_EXPRESSIONS.get(expr, RYN_EXPRESSIONS["neutre"])

        blink_phase = st % 4.7
        if 4.43 <= blink_phase <= 4.60:
            eyes = "yeux_ferme"

        zoom = RYN_IMAGE_SCALE
        speaking = _ryn_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = RYN_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        if kd_character_has_layered_wardrobe("ryn"):
            outfit = kd_equipped_character_outfit("ryn")
            arms = kd_arm_for_outfit("ryn", arms, outfit)
            asset_names = ["corps_nu", outfit]
            asset_names.extend(kd_equipped_character_accessories("ryn"))
            asset_names.extend((arms, mouth, eyes))
            asset_paths = tuple(_ryn_asset(asset_name) for asset_name in asset_names)
        else:
            asset_paths = (_ryn_asset(body), _ryn_asset(arms), _ryn_asset(eyes), _ryn_asset(mouth))

        displayable = kd_cached_layered_sprite(RYN_IMAGE_SIZE, zoom, asset_paths)
        return displayable, kd_layered_sprite_delay(st, 4.7, 4.43, 4.60, speaking)

    def ryn_expression(expr):
        return DynamicDisplayable(_ryn_layered_expression, expr)

image ryn blase                = ryn_expression("blase")
image ryn colere               = ryn_expression("colere")
image ryn colere2              = ryn_expression("colere2")
image ryn decontracte          = ryn_expression("decontracte")
image ryn desaccord            = ryn_expression("desaccord")
image ryn determine            = ryn_expression("determine")
image ryn fatigue              = ryn_expression("fatigue")
image ryn hesitation           = ryn_expression("hesitation")
image ryn inquiet              = ryn_expression("inquiet")
image ryn jaloux               = ryn_expression("jaloux")
image ryn joie                 = ryn_expression("joie")
image ryn neutre               = ryn_expression("neutre")
image ryn reflechit            = ryn_expression("reflechit")
image ryn rire                 = ryn_expression("rire")
image ryn sourire              = ryn_expression("sourire")
image ryn surpris              = ryn_expression("surpris")
image ryn taquin               = ryn_expression("taquin")
image ryn triste               = ryn_expression("triste")
image ryn vide                 = ryn_expression("vide")
image ryn reflexion            = ryn_expression("reflechit")

# ======================
# SAEL
# ======================
init python:
    SAEL_IMAGE_SIZE = (1024, 1536)
    SAEL_IMAGE_SCALE = 0.60
    SAEL_ASSET_DIR = "images/character/sael"

    SAEL_EXPRESSIONS = {
        "calme": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "colere": ("corps", "bras_explication", "bouche_colere", "yeux_colere"),
        "culpabilite": ("corps", "bras_long_corps", "bouche_triste", "yeux_fatigue"),
        "desaccord": ("corps", "bras_explication", "bouche_colere", "yeux_suspiscion"),
        "determine": ("corps", "bras_explication", "bouche_neutre", "yeux_colere"),
        "fatigue": ("corps", "bras_main_poche", "bouche_triste", "yeux_fatigue"),
        "inquiet": ("corps", "bras_long_corps", "bouche_triste", "yeux_surpris"),
        "jaloux": ("corps", "bras_main_poche", "bouche_colere", "yeux_suspiscion"),
        "joie": ("corps", "bras_explication", "bouche_joie", "yeux_neutre"),
        "mefiant": ("corps", "bras_main_poche", "bouche_neutre", "yeux_suspiscion"),
        "neutre": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
        "panne": ("corps", "bras_long_corps", "bouche_neutre", "yeux_fatigue"),
        "peur": ("corps", "bras_long_corps", "bouche_triste", "yeux_gros"),
        "raison": ("corps", "bras_explication", "bouche_neutre", "yeux_neutre"),
        "reflechit": ("corps", "bras_main_poche", "bouche_neutre", "yeux_suspiscion"),
        "reflexion": ("corps", "bras_main_poche", "bouche_neutre", "yeux_suspiscion"),
        "rire": ("corps", "bras_explication", "bouche_joie", "yeux_neutre"),
        "sourire": ("corps", "bras_long_corps", "bouche_joie", "yeux_neutre"),
        "surpris": ("corps", "bras_long_corps", "bouche_neutre", "yeux_surpris"),
        "taquin": ("corps", "bras_main_poche", "bouche_joie", "yeux_suspiscion"),
        "triste": ("corps", "bras_long_corps", "bouche_triste", "yeux_fatigue"),
        "vide": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
    }

    def _sael_asset(name):
        return "%s/%s.png" % (SAEL_ASSET_DIR, name)

    def _sael_is_speaking():
        return is_character_speaking("sael")

    def _sael_layered_expression(st, at, expr):
        body, arms, mouth, eyes = SAEL_EXPRESSIONS.get(expr, SAEL_EXPRESSIONS["neutre"])

        blink_phase = st % 4.95
        if 4.67 <= blink_phase <= 4.84:
            eyes = "yeux_ferme"

        zoom = SAEL_IMAGE_SCALE
        speaking = _sael_is_speaking()
        if speaking:
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = SAEL_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        displayable = kd_cached_layered_sprite(
            SAEL_IMAGE_SIZE, zoom,
            (_sael_asset(body), _sael_asset(arms), _sael_asset(eyes), _sael_asset(mouth)),
        )
        return displayable, kd_layered_sprite_delay(st, 4.95, 4.67, 4.84, speaking)

    def sael_expression(expr):
        return DynamicDisplayable(_sael_layered_expression, expr)

image sael calme                = sael_expression("calme")
image sael colere               = sael_expression("colere")
image sael culpabilite          = sael_expression("culpabilite")
image sael desaccord            = sael_expression("desaccord")
image sael determine            = sael_expression("determine")
image sael fatigue              = sael_expression("fatigue")
image sael inquiet              = sael_expression("inquiet")
image sael jaloux               = sael_expression("jaloux")
image sael joie                 = sael_expression("joie")
image sael mefiant              = sael_expression("mefiant")
image sael neutre               = sael_expression("neutre")
image sael panne                = sael_expression("panne")
image sael peur                 = sael_expression("peur")
image sael raison               = sael_expression("raison")
image sael reflechit            = sael_expression("reflechit")
image sael reflexion            = sael_expression("reflexion")
image sael rire                 = sael_expression("rire")
image sael sourire              = sael_expression("sourire")
image sael surpris              = sael_expression("surpris")
image sael taquin               = sael_expression("taquin")
image sael triste               = sael_expression("triste")
image sael vide                 = sael_expression("vide")

# ======================
# Goumi
# ======================

image goumi vide              = im.FactorScale("images/character/vide.png", 0.60)
