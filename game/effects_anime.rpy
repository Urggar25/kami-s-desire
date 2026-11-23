# Anime reaction FX — Blue Shock / aoi-tate-sen
# Aucune modification des assets des personnages : teinte et SVG par-dessus.
# Usage (non bloquant) :
#   $ blue_shock("elias")                         # 1.4 s
#   $ blue_shock("elen", intensity="light")       # irritation
#   $ blue_shock("julian", intensity="extreme", duration=2.0)
#   $ blue_shock_clear("elias")                    # arrêt immédiat
# L'overlay suit le layer master, donc également le travelling caméra.
# Les showGroup(), showP() et restyle_char() maintiennent la teinte
# pendant l'effet ; un changement d'expression n'annule pas l'effet.

default kd_anime_active_shocks = {}
default kd_anime_shock_serial = 0

transform kd_blue_shock_tint(intensity="normal"):
    # Le filtre appartient au sprite, pas aux autres personnages.
    matrixcolor IdentityMatrix()
    easeout 0.13 matrixcolor (
        SaturationMatrix(0.44 if intensity == "light" else (0.25 if intensity == "extreme" else 0.32))
        * TintMatrix("#9cbae0" if intensity == "light" else ("#4779b9" if intensity == "extreme" else "#739bcc"))
    )

transform kd_blue_shock_overlay_anim(duration=1.4, intensity="normal"):
    # Les SVG sont dessines sur la toile source des personnages : 1024x1536,
    # les sprites du projet ont un zoom de source de 0.60.
    subpixel True
    zoom 0.60
    alpha 0.0
    yoffset -14
    easeout 0.13 alpha (0.65 if intensity == "light" else 1.0) yoffset 0
    pause max(0.05, duration - 0.45)
    easein 0.28 alpha 0.0 yoffset 12

screen kd_anime_shock_watchdog():
    # Le timer est independant des boites de dialogue (pas de pause hard).
    timer 0.07 repeat True action Function(kd_anime_shock_tick)

init python:
    KD_BLUE_SHOCK_TAG_PREFIX = "kd_blue_shock_"
    KD_BLUE_SHOCK_ASSETS = {
        "light": "images/effects/kd_blue_shock_light.svg",
        "normal": "images/effects/kd_blue_shock_normal.svg",
        "extreme": "images/effects/kd_blue_shock_extreme.svg",
    }

    def kd_anime_shock_active(tag):
        entry = store.kd_anime_active_shocks.get(tag)
        return entry if isinstance(entry, dict) else None

    def kd_anime_sprite_at_list(tag, at_list):
        """Ajoute la teinte a toutes les manieres de (re)montrer un sprite."""
        result = list(at_list)
        entry = kd_anime_shock_active(tag)
        if entry is not None:
            result.append(kd_blue_shock_tint(entry["intensity"]))
        return result

    def kd_anime_shock_overlay_tag(tag):
        return KD_BLUE_SHOCK_TAG_PREFIX + tag

    def kd_anime_shock_refresh(tag):
        """Rafraichit le sprite sans le deplacer ni modifier son expression."""
        state = store.char_state.get(tag)
        if not state:
            return
        layer = state.get("layer", "master")
        if not renpy.showing(tag, layer=layer):
            return
        # La mise en forme courante est reproduite par restyle_char.
        mode = state.get("mode", "restore")
        if mode not in ("focus", "dim", "restore"):
            mode = "restore"
        state["mode"] = None
        restyle_char(tag, mode)

    def kd_anime_shock_sync_overlay(tag):
        """Garde les lignes collees au sprite apres showGroup/showP/repositionnement."""
        entry = kd_anime_shock_active(tag)
        if entry is None:
            return
        state = store.char_state.get(tag)
        if not state:
            return
        x = state.get("x", 0.5)
        y = state.get("y", 1.0)
        layer = state.get("layer", "master")
        if x == entry.get("x") and y == entry.get("y") and layer == entry.get("layer"):
            return

        import time
        remaining = max(0.1, entry.get("expires", 0.0) - time.time())
        old_layer = entry.get("layer", layer)
        renpy.hide(kd_anime_shock_overlay_tag(tag), layer=old_layer)
        entry["x"], entry["y"], entry["layer"] = x, y, layer
        renpy.show(
            kd_anime_shock_overlay_tag(tag),
            what=KD_BLUE_SHOCK_ASSETS[entry["intensity"]],
            tag=kd_anime_shock_overlay_tag(tag),
            at_list=[
                Position(xalign=x, yalign=y),
                kd_blue_shock_overlay_anim(remaining, entry["intensity"]),
            ],
            layer=layer,
            zorder=700 + int(state.get("zorder", 0)),
        )

    def blue_shock(tag, intensity="normal", duration=1.4, sound=False):
        """Effet local anime, non bloquant, sur un personnage visible.

        Conserve les animations de bouche, les expressions et le cadrage.
        Les parametres sont facultatifs pour un appel en une seule ligne.
        """
        if intensity not in KD_BLUE_SHOCK_ASSETS:
            raise ValueError("blue_shock intensity: light, normal ou extreme")
        state = store.char_state.get(tag)
        if not state:
            return False
        layer = state.get("layer", "master")
        if not renpy.showing(tag, layer=layer):
            return False

        import time
        duration = max(0.55, float(duration))
        # Remplacer un effet en cours sans cumuler overlays/timers.
        existing = kd_anime_shock_active(tag)
        if existing is not None:
            renpy.hide(kd_anime_shock_overlay_tag(tag), layer=existing.get("layer", layer))
        store.kd_anime_shock_serial += 1
        generation = store.kd_anime_shock_serial
        store.kd_anime_active_shocks[tag] = {
            "intensity": intensity,
            "expires": time.time() + duration,
            "generation": generation,
            "layer": layer,
            "x": state.get("x", 0.5),
            "y": state.get("y", 1.0),
        }
        kd_anime_shock_refresh(tag)
        # Affiche les lignes et l'ombre exactement aux coordonnees du sprite.
        # Un meme SVG transparent accompagne le visage sans remplacer son asset.
        renpy.show(
            kd_anime_shock_overlay_tag(tag),
            what=KD_BLUE_SHOCK_ASSETS[intensity],
            tag=kd_anime_shock_overlay_tag(tag),
            at_list=[
                Position(xalign=state.get("x", 0.5), yalign=state.get("y", 1.0)),
                kd_blue_shock_overlay_anim(duration, intensity),
            ],
            layer=layer,
            zorder=700 + int(state.get("zorder", 0)),
        )
        renpy.show_screen("kd_anime_shock_watchdog")
        if sound and renpy.loadable("audio/sfx_qte_miss.wav"):
            renpy.sound.play("audio/sfx_qte_miss.wav")
        renpy.restart_interaction()
        return True

    def blue_shock_clear(tag):
        """Arret immediat et restauration de la teinte d'origine."""
        entry = store.kd_anime_active_shocks.pop(tag, None)
        if entry is None:
            return False
        layer = entry.get("layer", "master")
        renpy.hide(kd_anime_shock_overlay_tag(tag), layer=layer)
        kd_anime_shock_refresh(tag)
        if not store.kd_anime_active_shocks:
            renpy.hide_screen("kd_anime_shock_watchdog")
        renpy.restart_interaction()
        return True

    def kd_anime_shock_tick():
        import time
        now = time.time()
        for tag, entry in list(store.kd_anime_active_shocks.items()):
            if now >= entry.get("expires", 0.0) or not renpy.showing(tag, layer=entry.get("layer", "master")):
                blue_shock_clear(tag)
        if not store.kd_anime_active_shocks:
            renpy.hide_screen("kd_anime_shock_watchdog")
