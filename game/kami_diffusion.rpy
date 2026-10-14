# Diffusion Kami : rendu plein écran et composition des PNG indépendants.
# Images : images/background/kami_diffusion/<expression>[_parle|_gene|_anim].png
# Ordre : fond > reflet Kami > Kami > reflet gêne > gêne > reflet anim > anim.
# Les anciennes CG restent un recours pour les expressions sans nouveaux PNG.

default kami_diffusion_effect_kind = None
default kami_diffusion_effect_started = 0.0

init -3 python:
    import time
    import re as _kami_markup_re

    KAMI_DIFFUSION_DIR = "images/background/kami_diffusion/"
    KAMI_DIFFUSION_EXPRESSIONS = (
        "amour", "champagne", "colere", "gene", "einstein", "fier",
        "meteo", "professeur", "taquin", "triste", "zen", "neutre"
    )
    _kami_diffusion_cache = {}

    # Les anciennes scènes conservent leur nom, mais utilisent les
    # nouvelles textures (y compris _parle, _gene et _anim).
    KAMI_DIFFUSION_ALIASES = {
        "einstein": "professeur",
        "meteo": "professeur",
        "zen": "champagne",
        "triste": "gene",
        "desespoir": "gene",
    }

    def kami_diffusion_normalize(expression):
        expression = KAMI_DIFFUSION_ALIASES.get(expression, expression)
        return expression if expression in KAMI_DIFFUSION_EXPRESSIONS else "neutre"

    def kami_diffusion_asset(filename):
        return KAMI_DIFFUSION_DIR + filename + ".png"

    def kami_diffusion_existing(paths):
        for path in paths:
            if renpy.loadable(path):
                return path
        return None

    def kami_diffusion_current_expression():
        for layer in ("master", "bgcam"):
            for tag in renpy.get_showing_tags(layer=layer):
                if tag.startswith("bg_diffusion_"):
                    return kami_diffusion_normalize(tag[len("bg_diffusion_"):])
        return "neutre"

    def kami_diffusion_on_dialogue(text):
        # Nettoyer les balises Ren'Py, afin de ne pas déclencher sur un attribut.
        clean = _kami_markup_re.sub(r"\{[^{}]*\}", "", text or "")
        if "..." in clean or "…" in clean:
            kind = "gene"
        elif "!" in clean:
            kind = "anim"
        else:
            kind = None
        store.kami_diffusion_effect_kind = kind
        store.kami_diffusion_effect_started = time.time()

    def _kami_diffusion_fullscreen(path):
        # Les nouvelles textures sont des images en coordonnées écran.
        # Appliquer la même transformation à TOUS les calques maintient
        # leurs positions exactement alignées, quelle que soit la fenêtre.
        return Transform(Image(path), fit="cover",
                         xysize=(config.screen_width, config.screen_height))

    def _kami_diffusion_ghost(path):
        # Un halo réfléchi SOUS le calque normal, visible notamment sur le
        # fond sombre de l'écran, sans remplacer sa texture ni ses contours.
        return Transform(
            _kami_diffusion_fullscreen(path),
            alpha=0.27, blur=11, xoffset=5, yoffset=3
        )

    def _kami_diffusion_composite(fond, main, gene=None, anim=None):
        key = (fond, main, gene, anim, config.screen_width, config.screen_height)
        cached = _kami_diffusion_cache.get(key)
        if cached is not None:
            return cached
        children = [_kami_diffusion_fullscreen(fond)]
        for path in (main, gene, anim):
            if path:
                children.append(_kami_diffusion_ghost(path))
                children.append(_kami_diffusion_fullscreen(path))
        result = Fixed(*children,
                       xysize=(config.screen_width, config.screen_height))
        _kami_diffusion_cache[key] = result
        return result

    def kami_diffusion_frame(st, at, expression):
        expression = kami_diffusion_normalize(expression)
        fond = kami_diffusion_asset("bg_diffusion_fond")
        idle = kami_diffusion_asset(expression)
        # Ne PAS superposer un ancien fond composite à un nouveau sprite.
        if not renpy.loadable(fond) or not renpy.loadable(idle):
            fallback = kami_diffusion_existing((
                kami_diffusion_asset("bg_diffusion_" + expression),
                kami_diffusion_asset("bg_diffusion_gene"),
                "images/background/cg/bg_diffusion_neutre.png",
            ))
            return _kami_diffusion_fullscreen(fallback), 0.10

        # Même cadence de bouche que les autres sprites : alternance
        # instantanée, sans transition ni dissolve entre les deux textures.
        speaking = is_character_speaking("kami")
        talk = kami_diffusion_asset(expression + "_parle")
        main = talk if speaking and renpy.loadable(talk) and (st % 0.30) < 0.15 else idle

        gene = anim = None
        # L'effet de ponctuation dure 2 s, indépendamment de la bouche.
        age = time.time() - store.kami_diffusion_effect_started
        if 0.0 <= age < 2.0:
            if store.kami_diffusion_effect_kind == "gene":
                gene = kami_diffusion_existing((
                    kami_diffusion_asset(expression + "_gene"),
                    kami_diffusion_asset("gene_gene"),
                ))
            elif store.kami_diffusion_effect_kind == "anim":
                anim = kami_diffusion_existing((
                    kami_diffusion_asset(expression + "_anim"),
                ))
        return _kami_diffusion_composite(fond, main, gene, anim), 0.06

    def kami_diffusion_display(expression):
        return DynamicDisplayable(kami_diffusion_frame, expression)

    def kami_diffusion_speaker_callback(event, interact=True, **kwargs):
        if event == "begin":
            dialogue = kwargs.get("what", "")
            start_character_dialogue("kami", dialogue)
            play_dialogue_doublage("kami", dialogue)
            kami_diffusion_on_dialogue(dialogue)
        elif event == "end":
            # Au clic, arrêter le mouvement de bouche immédiatement.
            store.character_speaking_until.pop("kami", None)

init -1 python:
    for _kami_expression in KAMI_DIFFUSION_EXPRESSIONS:
        renpy.image("bg_diffusion_" + _kami_expression,
                    kami_diffusion_display(_kami_expression))
    renpy.image("bg_diffusion_desespoir", kami_diffusion_display("gene"))
