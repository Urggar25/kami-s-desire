# Système de diffusion de Kami (composition indépendante des scènes).
# Les calques PNG sont attendus dans images/background/kami_diffusion/ :
# bg_diffusion_fond.png, <expression>.png, <expression>_parle.png,
# <expression>_gene.png et <expression>_anim.png.
# Chaque texture de personnage doit être un PNG transparent au format écran.
# Les anciennes images bg_diffusion_*.png restent utilisées comme secours
# tant que les nouveaux calques ne sont pas présents dans le dépôt.

default kami_diffusion_effect_kind = None
default kami_diffusion_effect_started = 0.0

init -3 python:
    import time

    KAMI_DIFFUSION_DIR = "images/background/kami_diffusion/"
    KAMI_DIFFUSION_EXPRESSIONS = (
        "amour", "champagne", "colere", "gene", "einstein", "fier",
        "meteo", "professeur", "taquin", "triste", "zen", "neutre"
    )

    def kami_diffusion_normalize(expression):
        if expression == "desespoir":
            return "gene"
        return expression if expression in KAMI_DIFFUSION_EXPRESSIONS else "neutre"

    def kami_diffusion_asset(filename):
        return KAMI_DIFFUSION_DIR + filename + ".png"

    def kami_diffusion_existing(paths):
        for path in paths:
            if renpy.loadable(path):
                return path
        return None

    def kami_diffusion_current_expression():
        # Déduit l'expression du fond montré, sans imposer de migration
        # immédiate des centaines de lignes de scénario déjà écrites.
        for layer in ("master", "bgcam"):
            for tag in renpy.get_showing_tags(layer=layer):
                if tag.startswith("bg_diffusion_"):
                    return kami_diffusion_normalize(tag[len("bg_diffusion_"):])
        return "neutre"

    def kami_diffusion_on_dialogue(text):
        # Appelé au début de chaque réplique de Kami.
        # Les points de suspension priment sur les exclamations.
        if "..." in text or "…" in text:
            kind = "gene"
        elif "!" in text:
            kind = "anim"
        else:
            kind = None
        store.kami_diffusion_effect_kind = kind
        store.kami_diffusion_effect_started = time.monotonic()

    def kami_diffusion_reflect(path, strength=0.12):
        # Reflet léger / persistance lumineuse sur l'écran, sans modifier
        # le calque source : les reflets sont placés SOUS l'image nette.
        return Transform(Image(path), alpha=strength, xoffset=3, yoffset=2,
                         blur=4)

    def kami_diffusion_frame(st, at, expression):
        expression = kami_diffusion_normalize(expression)
        directory = KAMI_DIFFUSION_DIR
        fond = kami_diffusion_existing((
            kami_diffusion_asset("bg_diffusion_fond"),
            "images/background/cg/bg_diffusion_neutre.png",
        ))
        main = kami_diffusion_existing((
            kami_diffusion_asset(expression + ("_parle" if is_character_speaking("kami") else "")),
            kami_diffusion_asset(expression),
        ))
        # Evite de mélanger une ancienne CG composite avec un nouveau sprite.
        if not renpy.loadable(kami_diffusion_asset("bg_diffusion_fond")) or not main:
            legacy = kami_diffusion_existing((
                kami_diffusion_asset("bg_diffusion_" + expression),
                kami_diffusion_asset("bg_diffusion_gene" if expression == "gene" else "bg_diffusion_neutre"),
                "images/background/cg/bg_diffusion_neutre.png",
            ))
            return Image(legacy), 0.10

        layers = [Image(fond), kami_diffusion_reflect(main), Image(main)]
        trigger = store.kami_diffusion_effect_kind
        elapsed = time.monotonic() - store.kami_diffusion_effect_started
        if trigger and 0 <= elapsed < 2.0:
            if trigger == "gene":
                overlay = kami_diffusion_existing((
                    kami_diffusion_asset(expression + "_gene"),
                    kami_diffusion_asset("gene_gene"),
                ))
                if overlay:
                    layers += [kami_diffusion_reflect(overlay), Image(overlay)]
            elif trigger == "anim":
                overlay = kami_diffusion_existing((kami_diffusion_asset(expression + "_anim"),))
                if overlay:
                    layers += [kami_diffusion_reflect(overlay), Image(overlay)]
        return Fixed(*layers), 0.07

    def kami_diffusion_display(expression):
        return DynamicDisplayable(kami_diffusion_frame, expression)

    def kami_diffusion_speaker_callback(event, interact=True, **kwargs):
        # Conserve le doublage et la logique de bouche des autres personnages.
        if event == "begin":
            dialogue = kwargs.get("what", "")
            start_character_dialogue("kami", dialogue)
            play_dialogue_doublage("kami", dialogue)
            kami_diffusion_on_dialogue(dialogue)
        elif event == "end":
            # Le système général gère également l'arrêt des répliques.
            pass

# Déclarations explicites : chaque ancien 'scene bg_diffusion_X' affiche
# maintenant le composite si les PNG séparés sont disponibles.
init -1 python:
    for _kami_expression in KAMI_DIFFUSION_EXPRESSIONS:
        renpy.image("bg_diffusion_" + _kami_expression,
                    kami_diffusion_display(_kami_expression))
    # Compatibilité d'anciens scripts sans conserver l'ancien visuel.
    renpy.image("bg_diffusion_desespoir", kami_diffusion_display("gene"))
