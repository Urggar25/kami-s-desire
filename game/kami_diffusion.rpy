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

    # Bord intérieur du moniteur dessiné dans bg_diffusion_fond. Tous les
    # effets électroniques sont limités à cette surface et ne modifient jamais
    # le cadre métallique ni l'interface de dialogue de Ren'Py.
    def _kami_monitor_rect():
        w, h = config.screen_width, config.screen_height
        return (int(w * 0.105), int(h * 0.125),
                int(w * 0.790), int(h * 0.730))

    def _kami_screen_fx():
        # Fines lignes derrière la vitre, sans rectangle cyan uniforme.
        # Leur transparence faible préserve les blancs et le dessin.
        key = ("crt_screen_v2", config.screen_width, config.screen_height)
        cached = _kami_diffusion_cache.get(key)
        if cached is not None:
            return cached
        x, y, w, h = _kami_monitor_rect()
        children = []
        spacing = max(7, int(config.screen_height / 130))
        for i, yy in enumerate(range(y, y + h, spacing)):
            strength = (0.020, 0.040, 0.025, 0.015)[i % 4]
            children.append(Transform(
                Solid("#061d2b"), xpos=x, ypos=yy,
                xysize=(w, 1), alpha=strength))
        result = Fixed(*children,
                       xysize=(config.screen_width, config.screen_height))
        _kami_diffusion_cache[key] = result
        return result

    def _kami_diffusion_ghost(path):
        # Rémanence lumineuse plus proche de l'ancien visuel. Sous le
        # personnage, elle sert de halo et non de flou appliqué au sprite.
        return Transform(_kami_diffusion_fullscreen(path),
                         matrixcolor=TintMatrix("#38c9e5"),
                         alpha=0.15, blur=15, xoffset=2, yoffset=1)

    def _kami_diffusion_composite(fond, main, gene=None, anim=None):
        key = ("crt_frame", fond, main, gene, anim,
               config.screen_width, config.screen_height)
        cached = _kami_diffusion_cache.get(key)
        if cached is not None:
            return cached
        children = [_kami_diffusion_fullscreen(fond)]
        for path in (main, gene, anim):
            if path:
                children.append(_kami_diffusion_ghost(path))
                # Conserver les couleurs originales, sans filtre qui grise le blanc.
                children.append(_kami_diffusion_fullscreen(path))
        # Le traitement de l'écran passe PAR-DESSUS les personnages.
        children.append(_kami_screen_fx())
        result = Fixed(*children,
                       xysize=(config.screen_width, config.screen_height))
        _kami_diffusion_cache[key] = result
        return result

    def _kami_diffusion_scan_sweep(st):
        # Balayage lumineux doux qui se déplace lentement de haut en bas.
        x, y, w, h = _kami_monitor_rect()
        period = 6.2
        phase = (st % period) / period
        sweep_y = y + int(h * phase)
        band_h = max(3, int(h * 0.016))
        return Transform(Solid("#78dbeb"), xpos=x, ypos=sweep_y,
                         xysize=(w, min(band_h, y+h-sweep_y)), alpha=0.035)

    def _kami_diffusion_scale(displayable):
        # IMPORTANT : les scènes appellent souvent "at adaptive_fullscreen".
        # Un simple Transform(zoom=.8) réduit aussi le rectangle renvoyé
        # à Ren'Py, qui le ré-agrandit aussitôt avec fit="cover".
        # Le canevas EXTERIEUR reste donc toujours en plein écran :
        # seul le contenu intérieur est réduit à 80 % et centré.
        width, height = config.screen_width, config.screen_height
        content = Transform(
            displayable,
            zoom=0.80,
            xpos=int(width * 0.10), ypos=int(height * 0.10),
            xanchor=0.0, yanchor=0.0,
        )
        # Remplissage opaque sur toute la scène : sans ce fond, les marges
        # créées par le dézoom révèlent la transparence en damier du jeu.
        # Le moniteur reste à 80 %, tandis que la boîte de dialogue (layer
        # screens) conserve ses dimensions habituelles.
        return Fixed(Solid("#06090e"), content, xysize=(width, height))

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
            return _kami_diffusion_scale(_kami_diffusion_fullscreen(fallback)), 0.10

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
        # Le balayage est séparé des compositions en cache : animation
        # continue même pendant une pause, sans refaire les 100 scanlines.
        surface = Fixed(_kami_diffusion_composite(fond, main, gene, anim),
                        _kami_diffusion_scan_sweep(st),
                        xysize=(config.screen_width, config.screen_height))
        return _kami_diffusion_scale(surface), 0.06

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
