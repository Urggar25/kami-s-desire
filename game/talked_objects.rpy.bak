################################################################################
## Objets mentionnes - panneau holographique de dialogue
################################################################################

init -1 python:
    import re
    import unicodedata

    TALKED_OBJECT_ASSET_DIR = "gui/talked_objects"

    define_talked_object_registry = [
        {
            "id": "badge",
            "name": "Badge d'acces",
            "image": "%s/object_badge.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("badge", "badges", "carte d'acces", "carte acces", "access card"),
            "note": "ACCES",
        },
        {
            "id": "tablet",
            "name": "Tablette",
            "image": "%s/object_tablet.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("tablette", "terminal portable", "tablet"),
            "note": "DONNEES",
        },
        {
            "id": "dossier",
            "name": "Dossier ferme",
            "image": "%s/object_dossier.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("dossier", "dossiers", "fichier", "archive", "archives", "file", "folder"),
            "note": "ARCHIVE",
        },
        {
            "id": "photo",
            "name": "Photo personnelle",
            "image": "%s/object_photo.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("photo", "photographie", "image de lea", "lea", "sister's photo"),
            "note": "SOUVENIR",
        },
        {
            "id": "drawing",
            "name": "Dessin de Juliette",
            "image": "%s/object_drawing.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("dessin", "juliette", "croquis", "sketch", "drawing"),
            "note": "TRACE",
        },
        {
            "id": "supplies",
            "name": "Fournitures",
            "image": "%s/fourniture.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("fourniture", "fournitures", "livraison", "colis", "carton", "cartons", "supplies", "delivery"),
            "note": "STOCK",
        },
        {
            "id": "ration",
            "name": "Ration",
            "image": "%s/object_ration.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("ration", "rations", "rationnement", "plateau", "pain", "barre", "meal"),
            "note": "SURVIE",
        },
        {
            "id": "key",
            "name": "Cle plate",
            "image": "%s/object_key.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("cle", "cles", "clef", "clefs", "outil", "outils", "wrench", "key"),
            "note": "MAINT.",
        },
        {
            "id": "jammer",
            "name": "Brouilleur",
            "image": "%s/object_jammer.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("brouilleur", "parasite", "signal coupe", "jammer"),
            "note": "SIGNAL",
        },
        {
            "id": "radio",
            "name": "Radio",
            "image": "%s/object_radio.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("radio", "talkie", "appel", "frequence", "frequency"),
            "note": "COMMS",
        },
        {
            "id": "robot",
            "name": "Robot d'exploration",
            "image": "%s/object_robot.png" % TALKED_OBJECT_ASSET_DIR,
            "keywords": ("robot", "drone", "exploration spatiale", "space exploration robot"),
            "note": "UNITE",
        },
    ]

    talked_object_registry = {}
    talked_object_patterns = []

    def _talked_object_plain(value):
        if value is None:
            return ""

        text = renpy.substitute(str(value), translate=True)
        text = re.sub(r"\{[^{}]*\}", " ", text)
        text = unicodedata.normalize("NFD", text)
        text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
        text = text.lower()
        return re.sub(r"\s+", " ", text)

    def register_talked_object(object_id, name, image, keywords, note="OBJET"):
        entry = {
            "id": object_id,
            "name": name,
            "image": image,
            "keywords": tuple(keywords),
            "note": note,
        }
        talked_object_registry[object_id] = entry

        for keyword in entry["keywords"]:
            plain_keyword = _talked_object_plain(keyword)
            if not plain_keyword:
                continue
            pattern = re.compile(r"(?<!\w)%s(?!\w)" % re.escape(plain_keyword))
            talked_object_patterns.append((pattern, object_id))

    def talked_object_for_line(line):
        plain_line = _talked_object_plain(line)
        if not plain_line:
            return None

        for pattern, object_id in talked_object_patterns:
            if pattern.search(plain_line):
                return talked_object_registry.get(object_id)

        return None

    for _talked_object in define_talked_object_registry:
        register_talked_object(
            _talked_object["id"],
            _talked_object["name"],
            _talked_object["image"],
            _talked_object["keywords"],
            _talked_object.get("note", "OBJET"),
        )


transform talked_object_panel_in:
    alpha 0.0
    xoffset -28
    zoom 0.985
    easeout 0.18 alpha 1.0 xoffset 0 zoom 1.0

transform talked_object_item_float:
    alpha 0.96
    yoffset 0
    easein 1.2 yoffset -8
    easeout 1.2 yoffset 0
    repeat

transform talked_object_scanline:
    alpha 0.42
    yoffset -320
    linear 1.6 yoffset 320
    repeat


screen talked_object_from_line(line):
    zorder 52

    $ talked_object = talked_object_for_line(line)

    if talked_object:
        use talked_object_overlay(talked_object)


screen talked_object_overlay(talked_object):
    zorder 52

    fixed at talked_object_panel_in:
        xpos 34
        ypos 242
        xsize 660
        ysize 380

        add "gui/talked_objects/panel.png"
        add "gui/talked_objects/grid.png" xpos 22 ypos 22
        add "gui/talked_objects/scanline.png" xpos 34 ypos 42 at talked_object_scanline
        add "gui/talked_objects/glow.png" xpos 104 ypos 58 alpha 0.75

        add Transform(talked_object["image"], fit="contain", xsize=356, ysize=236) xpos 80 ypos 72 at talked_object_item_float

        text "OBJET MENTIONNE":
            xpos 40
            ypos 30
            size 24
            font "fonts/Rajdhani-SemiBold.ttf"
            color "#C9F7FF"
            outlines [(1, "#072633cc", 0, 0)]

        text talked_object["name"]:
            xpos 46
            ypos 304
            xsize 380
            size 34
            font "fonts/Rajdhani-SemiBold.ttf"
            color "#FFFFFF"
            outlines [(2, "#0B2E3D", 0, 0)]

        text talked_object["note"]:
            xpos 506
            ypos 306
            xsize 92
            text_align 0.5
            size 22
            font "fonts/Rajdhani-SemiBold.ttf"
            color "#8BEAFF"
            outlines [(1, "#092A38", 0, 0)]
