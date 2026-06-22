# ======================
# ELIAS
# ======================
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
        "hesitation": ("corps_1", "bras_sur_torse", "bouche_decu", "yeux_peur"),
        "choc": ("corps_1", "bras_en_air", "bouche_peur", "yeux_peur"),
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
        if _elias_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = ELIAS_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            ELIAS_IMAGE_SIZE,
            (0, 0), _elias_asset(body),
            (0, 0), _elias_asset(arms),
            (0, 0), _elias_asset(eyes),
            (0, 0), _elias_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

    def elias_expression(expr):
        return DynamicDisplayable(_elias_layered_expression, expr)

# image elias colere            = im.FactorScale("images/character/elias/colere.png", 0.60)
image elias colere            = elias_expression("colere")
# image elias colere_noire      = im.FactorScale("images/character/elias/colere_noire.png", 0.60)
image elias colere_noire      = elias_expression("colere_noire")
# image elias content           = im.FactorScale("images/character/elias/content.png", 0.60)
image elias content           = elias_expression("content")
# image elias desespoir         = im.FactorScale("images/character/elias/desespoir.png", 0.60)
image elias desespoir         = elias_expression("desespoir")
# image elias ecoute            = im.FactorScale("images/character/elias/ecoute.png", 0.60)
image elias ecoute            = elias_expression("ecoute")
# image elias fatigue           = im.FactorScale("images/character/elias/fatigue.png", 0.60)
image elias fatigue           = elias_expression("fatigue")
# image elias inquiet           = im.FactorScale("images/character/elias/inquiet.png", 0.60)
image elias inquiet           = elias_expression("inquiet")
# image elias jaloux            = im.FactorScale("images/character/elias/jaloux.png", 0.60)
image elias jaloux            = elias_expression("jaloux")
# image elias joie              = im.FactorScale("images/character/elias/joie.png", 0.60)
image elias joie              = elias_expression("joie")
# image elias neutre            = im.FactorScale("images/character/elias/neutre.png", 0.60)
image elias neutre            = elias_expression("neutre")
# image elias panique           = im.FactorScale("images/character/elias/panique.png", 0.60)
image elias panique           = elias_expression("panique")
# image elias rire              = im.FactorScale("images/character/elias/rire.png", 0.60)
image elias rire              = elias_expression("rire")
# image elias reflechit              = im.FactorScale("images/character/elias/reflechit.png", 0.60)
image elias reflechit         = elias_expression("reflechit")
# image elias detendu              = im.FactorScale("images/character/elias/detendu.png", 0.60)
image elias detendu           = elias_expression("detendu")
# image elias raison              = im.FactorScale("images/character/elias/raison.png", 0.60)
image elias raison            = elias_expression("raison")
# image elias determine              = im.FactorScale("images/character/elias/determine.png", 0.60)
image elias determine         = elias_expression("determine")
# image elias hesitation              = im.FactorScale("images/character/elias/hesitation.png", 0.60)
image elias hesitation        = elias_expression("hesitation")
# image elias choc              = im.FactorScale("images/character/elias/choc.png", 0.60)
image elias choc              = elias_expression("choc")

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
        if _mara_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = MARA_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            MARA_IMAGE_SIZE,
            (0, 0), _mara_asset(body),
            (0, 0), _mara_asset(arms),
            (0, 0), _mara_asset(eyes),
            (0, 0), _mara_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

    def mara_expression(expr):
        return DynamicDisplayable(_mara_layered_expression, expr)

# image mara agace              = im.FactorScale("images/character/mara/agace.png", 0.60)
image mara agace              = mara_expression("agace")
# image mara colere             = im.FactorScale("images/character/mara/colere.png", 0.60)
image mara colere             = mara_expression("colere")
# image mara colere_noire       = im.FactorScale("images/character/mara/colere_noire.png", 0.60)
image mara colere_noire       = mara_expression("colere_noire")
# image mara content            = im.FactorScale("images/character/mara/content.png", 0.60)
image mara content            = mara_expression("content")
# image mara doute              = im.FactorScale("images/character/mara/doute.png", 0.60)
image mara doute              = mara_expression("doute")
# image mara jaloux             = im.FactorScale("images/character/mara/jaloux.png", 0.60)
image mara jaloux             = mara_expression("jaloux")
# image mara joie               = im.FactorScale("images/character/mara/joie.png", 0.60)
image mara joie               = mara_expression("joie")
# image mara mefiant            = im.FactorScale("images/character/mara/mefiant.png", 0.60)
image mara mefiant            = mara_expression("mefiant")
# image mara neutre             = im.FactorScale("images/character/mara/neutre.png", 0.60)
image mara neutre             = mara_expression("neutre")
# image mara reflexion          = im.FactorScale("images/character/mara/reflexion.png", 0.60)
image mara reflexion          = mara_expression("reflexion")
# image mara rire               = im.FactorScale("images/character/mara/rire.png", 0.60)
image mara rire               = mara_expression("rire")
# image mara rire_profond       = im.FactorScale("images/character/mara/rire_profond.png", 0.60)
image mara rire_profond       = mara_expression("rire_profond")
# image mara stress             = im.FactorScale("images/character/mara/stress.png", 0.60)
image mara stress             = mara_expression("stress")
# image mara sourire            = im.FactorScale("images/character/mara/sourire.png", 0.60)
image mara sourire            = mara_expression("sourire")
# image mara taquin             = im.FactorScale("images/character/mara/taquin.png", 0.60)
image mara taquin             = mara_expression("taquin")
# image mara fatigue            = im.FactorScale("images/character/mara/fatigue.png", 0.60)
image mara fatigue            = mara_expression("fatigue")
# image mara ivre               = im.FactorScale("images/character/mara/ivre.png", 0.60)
image mara ivre               = mara_expression("ivre")
# image mara vide               = im.FactorScale("images/character/vide.png", 0.60)
image mara vide               = mara_expression("vide")

# ======================
# NOAM
# ======================
image noam colere              = im.FactorScale("images/character/noam/colere.png", 0.60)
image noam culpabilite         = im.FactorScale("images/character/noam/culpabilite.png", 0.60)
image noam desaccord           = im.FactorScale("images/character/noam/desaccord.png", 0.60)
image noam desespoir           = im.FactorScale("images/character/noam/desespoir.png", 0.60)
image noam determine           = im.FactorScale("images/character/noam/determine.png", 0.60)
image noam hesitation          = im.FactorScale("images/character/noam/hesitation.png", 0.60)
image noam inquiet             = im.FactorScale("images/character/noam/inquiet.png", 0.60)
image noam joie                = im.FactorScale("images/character/noam/joie.png", 0.60)
image noam neutre              = im.FactorScale("images/character/noam/neutre.png", 0.60)
image noam panne               = im.FactorScale("images/character/noam/panne.png", 0.60)
image noam peur                = im.FactorScale("images/character/noam/peur.png", 0.60)
image noam raison              = im.FactorScale("images/character/noam/raison.png", 0.60)
image noam reflexion           = im.FactorScale("images/character/noam/reflexion.png", 0.60)
image noam rire                = im.FactorScale("images/character/noam/rire.png", 0.60)
image noam sourire             = im.FactorScale("images/character/noam/sourire.png", 0.60)
image noam surpris             = im.FactorScale("images/character/noam/surpris.png", 0.60)
image noam taquin              = im.FactorScale("images/character/noam/taquin.png", 0.60)
image noam triste              = im.FactorScale("images/character/noam/triste.png", 0.60)
image noam fatigue              = im.FactorScale("images/character/noam/fatigue.png", 0.60)
image noam faible              = im.FactorScale("images/character/noam/fatigue.png", 0.60)
image noam panique              = im.FactorScale("images/character/noam/panique.png", 0.60)
image noam panne_creep              = im.FactorScale("images/character/noam/panne_creep.png", 0.60)

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
        if _lysa_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = LYSA_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            LYSA_IMAGE_SIZE,
            (0, 0), _lysa_asset(body),
            (0, 0), _lysa_asset(arms),
            (0, 0), _lysa_asset(eyes),
            (0, 0), _lysa_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

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
        if _julian_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = JULIAN_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            JULIAN_IMAGE_SIZE,
            (0, 0), _julian_asset(body),
            (0, 0), _julian_asset(arms),
            (0, 0), _julian_asset(eyes),
            (0, 0), _julian_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

    def julian_expression(expr):
        return DynamicDisplayable(_julian_layered_expression, expr)

# image julian decu               = im.FactorScale("images/character/julian/decu.png", 0.60)
image julian decu               = julian_expression("decu")
# image julian determine          = im.FactorScale("images/character/julian/determine.png", 0.60)
image julian determine          = julian_expression("determine")
# image julian hesitation         = im.FactorScale("images/character/julian/hesitation.png", 0.60)
image julian hesitation         = julian_expression("hesitation")
# image julian idee               = im.FactorScale("images/character/julian/idee.png", 0.60)
image julian idee               = julian_expression("idee")
# image julian inquiet            = im.FactorScale("images/character/julian/inquiet.png", 0.60)
image julian inquiet            = julian_expression("inquiet")
# image julian joie               = im.FactorScale("images/character/julian/joie.png", 0.60)
image julian joie               = julian_expression("joie")
# image julian neutre             = im.FactorScale("images/character/julian/neutre.png", 0.60)
image julian neutre             = julian_expression("neutre")
# image julian panne              = im.FactorScale("images/character/julian/panne.png", 0.60)
image julian panne              = julian_expression("panne")
# image julian peur               = im.FactorScale("images/character/julian/peur.png", 0.60)
image julian peur               = julian_expression("peur")
# image julian reflexion          = im.FactorScale("images/character/julian/reflexion.png", 0.60)
image julian reflexion          = julian_expression("reflexion")
# image julian rire               = im.FactorScale("images/character/julian/rire.png", 0.60)
image julian rire               = julian_expression("rire")
# image julian sourire            = im.FactorScale("images/character/julian/sourire.png", 0.60)
image julian sourire            = julian_expression("sourire")
# image julian surpris            = im.FactorScale("images/character/julian/surpris.png", 0.60)
image julian surpris            = julian_expression("surpris")
# image julian taquin             = im.FactorScale("images/character/julian/taquin.png", 0.60)
image julian taquin             = julian_expression("taquin")
# image julian triste             = im.FactorScale("images/character/julian/triste.png", 0.60)
image julian triste             = julian_expression("triste")
# image julian detendu            = im.FactorScale("images/character/julian/detendu.png", 0.60)
image julian detendu            = julian_expression("detendu")
# image julian decontracte        = im.FactorScale("images/character/julian/decontracte.png", 0.60)
image julian decontracte        = julian_expression("decontracte")
# image julian colere             = im.FactorScale("images/character/julian/colere.png", 0.60)
image julian colere             = julian_expression("colere")

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
        "vide": ("corps", "bras_long_corps", "bouche_neutre", "yeux_neutre"),
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
        if _iris_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = IRIS_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            IRIS_IMAGE_SIZE,
            (0, 0), _iris_asset(body),
            (0, 0), _iris_asset(arms),
            (0, 0), _iris_asset(eyes),
            (0, 0), _iris_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

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
image iris rire                 = iris_expression("rire")
image iris sourire              = iris_expression("sourire")
image iris surpris              = iris_expression("surpris")
image iris surprise             = iris_expression("surprise")
image iris taquin               = iris_expression("taquin")
image iris triste               = iris_expression("triste")
image iris desaccord            = iris_expression("desaccord")
image iris intervention         = iris_expression("intervention")
image iris gene                 = iris_expression("gene")
image iris vide                 = iris_expression("vide")

# ======================
# TOMAS
# ======================
image tomas colere              = im.FactorScale("images/character/tomas/colere.png", 0.60)
image tomas colere_noire        = im.FactorScale("images/character/tomas/colere_noire.png", 0.60)
image tomas culpabilite         = im.FactorScale("images/character/tomas/culpabilite.png", 0.60)
image tomas desaccord           = im.FactorScale("images/character/tomas/desaccord.png", 0.60)
image tomas desespoir           = im.FactorScale("images/character/tomas/desespoir.png", 0.60)
image tomas determine           = im.FactorScale("images/character/tomas/determine.png", 0.60)
image tomas inquiet             = im.FactorScale("images/character/tomas/inquiet.png", 0.60)
image tomas joie                = im.FactorScale("images/character/tomas/joie.png", 0.60)
image tomas mefiant             = im.FactorScale("images/character/tomas/mefiant.png", 0.60)
image tomas neutre              = im.FactorScale("images/character/tomas/neutre.png", 0.60)
image tomas panne               = im.FactorScale("images/character/tomas/panne.png", 0.60)
image tomas raison              = im.FactorScale("images/character/tomas/raison.png", 0.60)
image tomas reflechit           = im.FactorScale("images/character/tomas/reflechit.png", 0.60)
image tomas rire                = im.FactorScale("images/character/tomas/rire.png", 0.60)
image tomas surpris             = im.FactorScale("images/character/tomas/surpris.png", 0.60)
image tomas taquin              = im.FactorScale("images/character/tomas/taquin.png", 0.60)
image tomas triste              = im.FactorScale("images/character/tomas/triste.png", 0.60)
image tomas hesitation              = im.FactorScale("images/character/tomas/hesitation.png", 0.60)
image tomas gene              = im.FactorScale("images/character/tomas/gene.png", 0.60)
image tomas fatigue              = im.FactorScale("images/character/tomas/fatigue.png", 0.60)
image tomas stress              = im.FactorScale("images/character/tomas/fatigue.png", 0.60)

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
        if _elen_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = ELEN_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            ELEN_IMAGE_SIZE,
            (0, 0), _elen_asset(body),
            (0, 0), _elen_asset(arms),
            (0, 0), _elen_asset(eyes),
            (0, 0), _elen_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

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
# image elen vide              = im.FactorScale("images/character/vide.png", 0.60)
image elen vide                 = elen_expression("vide")

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
        if _kael_is_speaking():
            mouth_phase = st % 0.32
            if mouth_phase < 0.16:
                mouth = "bouche_parle"
            zoom = KAEL_IMAGE_SCALE * (1.0 + (0.004 if (st % 0.42) < 0.21 else 0.0))

        composite = im.Composite(
            KAEL_IMAGE_SIZE,
            (0, 0), _kael_asset(body),
            (0, 0), _kael_asset(arms),
            (0, 0), _kael_asset(eyes),
            (0, 0), _kael_asset(mouth),
        )
        return Transform(composite, zoom=zoom), 0.08

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

# ======================
# NYRA
# ======================
image nyra colere               = im.FactorScale("images/character/nyra/colere.png", 0.60)
image nyra culpabilite          = im.FactorScale("images/character/nyra/culpabilite.png", 0.60)
image nyra degout               = im.FactorScale("images/character/nyra/degout.png", 0.60)
image nyra determine            = im.FactorScale("images/character/nyra/determine.png", 0.60)
image nyra fatigue              = im.FactorScale("images/character/nyra/fatigue.png", 0.60)
image nyra hesitation           = im.FactorScale("images/character/nyra/hesitation.png", 0.60)
image nyra inquiet              = im.FactorScale("images/character/nyra/inquiet.png", 0.60)
image nyra joie                 = im.FactorScale("images/character/nyra/joie.png", 0.60)
image nyra neutre               = im.FactorScale("images/character/nyra/neutre.png", 0.60)
image nyra panne                = im.FactorScale("images/character/nyra/panne.png", 0.60)
image nyra raison               = im.FactorScale("images/character/nyra/raison.png", 0.60)
image nyra reflexion            = im.FactorScale("images/character/nyra/reflexion.png", 0.60)
image nyra rire                 = im.FactorScale("images/character/nyra/rire.png", 0.60)
image nyra sourire              = im.FactorScale("images/character/nyra/sourire.png", 0.60)
image nyra surpris              = im.FactorScale("images/character/nyra/surpris.png", 0.60)
image nyra taquin               = im.FactorScale("images/character/nyra/taquin.png", 0.60)
image nyra triste               = im.FactorScale("images/character/nyra/triste.png", 0.60)
image nyra stress               = im.FactorScale("images/character/nyra/stress.png", 0.60)

# ======================
# RYN
# ======================
image ryn colere                = im.FactorScale("images/character/ryn/colere.png", 0.60)
image ryn colere2               = im.FactorScale("images/character/ryn/colere2.png", 0.60)
image ryn desaccord             = im.FactorScale("images/character/ryn/desaccord.png", 0.60)
image ryn determine             = im.FactorScale("images/character/ryn/determine.png", 0.60)
image ryn fatigue               = im.FactorScale("images/character/ryn/fatigue.png", 0.60)
image ryn inquiet               = im.FactorScale("images/character/ryn/inquiet.png", 0.60)
image ryn jaloux                = im.FactorScale("images/character/ryn/jaloux.png", 0.60)
image ryn joie                  = im.FactorScale("images/character/ryn/joie.png", 0.60)
image ryn neutre                = im.FactorScale("images/character/ryn/neutre.png", 0.60)
image ryn reflechit             = im.FactorScale("images/character/ryn/reflechit.png", 0.60)
image ryn rire                  = im.FactorScale("images/character/ryn/rire.png", 0.60)
image ryn sourire               = im.FactorScale("images/character/ryn/sourire.png", 0.60)
image ryn surpris               = im.FactorScale("images/character/ryn/surpris.png", 0.60)
image ryn taquin                = im.FactorScale("images/character/ryn/taquin.png", 0.60)
image ryn triste                = im.FactorScale("images/character/ryn/triste.png", 0.60)
image ryn blase                = im.FactorScale("images/character/ryn/blase.png", 0.60)
image ryn hesitation                = im.FactorScale("images/character/ryn/hesitation.png", 0.60)
image ryn decontracte                = im.FactorScale("images/character/ryn/decontracte.png", 0.60)

# ======================
# SAEL
# ======================
image sael culpabilite          = im.FactorScale("images/character/sael/culpabilite.png", 0.60)
image sael desaccord            = im.FactorScale("images/character/sael/desaccord.png", 0.60)
image sael determine            = im.FactorScale("images/character/sael/determine.png", 0.60)
image sael fatigue              = im.FactorScale("images/character/sael/fatigue.png", 0.60)
image sael inquiet              = im.FactorScale("images/character/sael/inquiet.png", 0.60)
image sael jaloux               = im.FactorScale("images/character/sael/jaloux.png", 0.60)
image sael joie                 = im.FactorScale("images/character/sael/joie.png", 0.60)
image sael mefiant              = im.FactorScale("images/character/sael/mefiant.png", 0.60)
image sael neutre               = im.FactorScale("images/character/sael/neutre.png", 0.60)
image sael peur                 = im.FactorScale("images/character/sael/peur.png", 0.60)
image sael raison               = im.FactorScale("images/character/sael/raison.png", 0.60)
image sael reflexion            = im.FactorScale("images/character/sael/reflechit.png", 0.60)
image sael rire                 = im.FactorScale("images/character/sael/rire.png", 0.60)
image sael sourire              = im.FactorScale("images/character/sael/sourire.png", 0.60)
image sael surpris              = im.FactorScale("images/character/sael/surpris.png", 0.60)
image sael taquin               = im.FactorScale("images/character/sael/taquin.png", 0.60)
image sael triste               = im.FactorScale("images/character/sael/triste.png", 0.60)
image sael colere               = im.FactorScale("images/character/sael/colere.png", 0.60)

# ======================
# Goumi
# ======================

image goumi vide              = im.FactorScale("images/character/vide.png", 0.60)
