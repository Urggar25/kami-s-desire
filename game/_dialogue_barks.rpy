# Doublage court automatique des dialogues.
#
# Chaque personnage dispose des memes intentions. Les quelques noms de fichiers
# historiques differents (hmm/mmh/mmm, desolee) sont resolus ici.

init -10 python:
    import re
    import unicodedata

    renpy.music.register_channel("doublage", mixer="voice", loop=False)

    _DOUBLAGE_CHARACTERS = {
        "elen", "elias", "iris", "julian", "kael", "kami", "lysa",
        "mara", "noam", "nyra", "ryn", "sael", "tomas",
    }

    # Les expressions sont classees par intention, mais la selection finale se
    # fait d'abord sur l'expression apparaissant le plus tot dans la replique.
    # A position egale, l'expression la plus precise (la plus longue) gagne.
    _DOUBLAGE_EXPRESSIONS = {
        "attends": (
            "attends", "attendez", "attend", "une seconde", "deux secondes",
            "une minute", "un instant", "patience", "bouge pas", "ne bouge pas",
            "reste là", "reste ici", "doucement", "stop", "arrête", "arrêtez",
            "attends-moi", "attendez-moi",
        ),
        "daccord": (
            "d'accord", "d’accord", "daccord", "ok", "okay", "entendu",
            "compris", "je comprends", "ça marche", "ca marche", "bien sûr",
            "bien sur", "certainement", "exactement", "tout à fait", "tout a fait",
            "très bien", "tres bien", "parfait", "volontiers", "oui",
        ),
        "desole": (
            "désolé", "désolée", "désolés", "désolées", "desole", "desolee",
            "pardon", "pardonne-moi", "pardonnez-moi", "excuse-moi", "excusez-moi",
            "excuse", "excusez", "je regrette", "navré", "navrée", "mes excuses",
        ),
        "donc": (
            "donc", "alors", "ainsi", "du coup", "par conséquent",
            "par consequent", "en conséquence", "en consequence", "de ce fait",
            "en somme", "autrement dit", "bref", "conclusion", "finalement",
        ),
        "hey": (
            "hé", "hey", "eh", "ho", "écoute-moi", "écoutez-moi", "ecoute-moi",
            "ecoutez-moi", "écoute", "écoutez", "ecoute", "ecoutez", "regarde-moi",
            "regardez-moi", "allo", "salut", "bonjour", "bonsoir", "coucou",
        ),
        "hesitation": (
            "euh", "heu", "euhm", "hum", "hmm", "hmmm", "mmh", "mmmh", "mmm",
            "mhh", "mh", "hein", "mouais", "bof", "bah", "ben", "peut-être",
            "peut etre", "je ne sais pas", "je sais pas", "pas sûr", "pas sure",
            "pas certain", "disons", "comment dire", "voyons voir",
        ),
        "mais": (
            "mais", "cependant", "néanmoins", "neanmoins", "pourtant", "toutefois",
            "en revanche", "par contre", "malgré tout", "malgre tout", "sauf que",
            "quand même", "quand meme", "au contraire", "seulement voilà",
            "seulement voila",
        ),
        "merde": (
            "merde", "putain", "bordel", "fait chier", "fais chier", "mince", "zut",
            "bon sang", "nom de dieu", "connard", "connasse", "connerie", "foutue",
            "foutu", "saloperie", "damné", "damnee", "damnée",
        ),
        "non": (
            "non", "jamais", "pas question", "hors de question", "absolument pas",
            "certainement pas", "sûrement pas", "surement pas", "impossible",
            "je refuse", "refuse", "aucunement", "nullement", "c'est faux",
            "c est faux", "cesse", "taisez-vous", "tais-toi",
        ),
        "vois": (
            "tu vois", "vous voyez", "je vois", "on voit", "regarde", "regardez",
            "voyez", "vois", "voir", "observe", "observez", "remarque", "remarquez",
            "constate", "constatez", "j'ai vu", "j’ai vu", "vous comprenez",
        ),
    }

    _DOUBLAGE_INTENT_PRIORITY = (
        "attends", "daccord", "desole", "donc", "hey", "hesitation",
        "mais", "merde", "non", "vois",
    )

    # Tous les fichiers suivent <personnage>_<intention>, sauf ceux-ci.
    _DOUBLAGE_FILE_SUFFIX_OVERRIDES = {
        ("elen", "hesitation"): "mmh",
        ("elias", "hesitation"): "mmh",
        ("iris", "hesitation"): "hmm",
        ("julian", "hesitation"): "mmh",
        ("kael", "hesitation"): "mmh",
        ("kami", "hesitation"): "hmm",
        ("lysa", "hesitation"): "mmh",
        ("mara", "desole"): "desolee",
        ("mara", "hesitation"): "hmm",
        ("noam", "hesitation"): "mmm",
        ("nyra", "hesitation"): "hmm",
        ("ryn", "hesitation"): "mmh",
        ("sael", "hesitation"): "mmh",
        ("tomas", "hesitation"): "hmm",
    }

    def _doublage_normalize(text):
        """Retire les tags Ren'Py, les accents et la ponctuation pour matcher proprement."""
        text = re.sub(r"\{[^{}]*\}", " ", str(text or ""))
        text = text.replace("œ", "oe").replace("Œ", "OE")
        text = unicodedata.normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata.combining(ch))
        text = text.lower().replace("’", "'")
        return " ".join(re.findall(r"[a-z0-9]+", text))

    _DOUBLAGE_NORMALIZED_EXPRESSIONS = {}
    for _doublage_intent in _DOUBLAGE_INTENT_PRIORITY:
        _DOUBLAGE_NORMALIZED_EXPRESSIONS[_doublage_intent] = tuple(
            _doublage_normalize(expression)
            for expression in _DOUBLAGE_EXPRESSIONS[_doublage_intent]
        )

    def dialogue_doublage_intent(text):
        """Retourne l'intention la plus naturelle, ou None si rien ne correspond."""
        normalized = _doublage_normalize(text)
        if not normalized:
            # Une replique composee uniquement de points de suspension est une
            # hesitation explicite, pas une phrase neutre a doubler par defaut.
            visible = re.sub(r"\{[^{}]*\}", "", str(text or "")).strip()
            return "hesitation" if visible and not visible.strip(". …") else None

        padded = " " + normalized + " "
        best = None
        for priority, intent in enumerate(_DOUBLAGE_INTENT_PRIORITY):
            for expression in _DOUBLAGE_NORMALIZED_EXPRESSIONS[intent]:
                match_at = padded.find(" " + expression + " ")
                if match_at < 0:
                    continue
                candidate = (match_at, -len(expression), priority, intent)
                if best is None or candidate < best:
                    best = candidate

        return best[3] if best is not None else None

    def dialogue_doublage_path(character, text):
        """Resout le vrai fichier audio associe a une replique."""
        character = str(character or "").lower()
        if character not in _DOUBLAGE_CHARACTERS:
            return None

        intent = dialogue_doublage_intent(text)
        if intent is None:
            return None
        suffix = _DOUBLAGE_FILE_SUFFIX_OVERRIDES.get((character, intent), intent)
        return "sound/doublage/{0}/{0}_{1}.mp3".format(character, suffix)

    def play_dialogue_doublage(character, text):
        """Joue un bark sur le mixeur voix, sauf pendant le mode skip."""
        if renpy.is_skipping():
            return

        path = dialogue_doublage_path(character, text)
        if not path:
            return
        if not renpy.loadable(path):
            renpy.log("Doublage introuvable : {}".format(path))
            return

        renpy.music.play(path, channel="doublage", loop=False)
