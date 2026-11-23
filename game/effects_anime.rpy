# Anime reaction FX — Blue Shock / aoi-tate-sen
# Aucune modification des assets : filtre sur le personnage et lignes
# procedurales creees avec Composite/Solid (Ren'Py ne rend pas nos SVG).
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
    easeout 0.13 matrixcolor SaturationMatrix(0.44 if intensity == "light" else (0.25 if intensity == "extreme" else 0.32)) * TintMatrix("#9cbae0" if intensity == "light" else ("#4779b9" if intensity == "extreme" else "#739bcc"))

transform kd_blue_shock_overlay_anim(duration=1.4, intensity="normal"):
    # La composition native utilise la toile source 1024x1536 des sprites.
    # Le zoom 0.60 n'est applique qu'une seule fois, sur l'overlay.
    subpixel True
    zoom 0.60
    alpha 0.0
    yoffset -8
    easeout 0.18 alpha (0.65 if intensity == "light" else 1.0) yoffset 0
    pause max(0.05, duration - 0.45)
    easein 0.28 alpha 0.0 yoffset 12

screen kd_anime_shock_watchdog():
    # Le timer est independant des boites de dialogue (pas de pause hard).
    timer 0.07 repeat True action Function(kd_anime_shock_tick)

init python:
    KD_BLUE_SHOCK_TAG_PREFIX = "kd_blue_shock_"
    KD_BLUE_SHOCK_LEVELS = ("light", "normal", "extreme")
    KD_BLUE_SHOCK_DISPLAYABLES = {}

    def kd_blue_shock_art(tag, intensity):
        """Ombre anime douce, localisee sur le visage du personnage.

        Contrairement a la premiere version, aucune grande bande rectangulaire
        et aucune ligne sur le decor : l'effet est masque par la silhouette du
        sprite. Les couleurs se fondent progressivement vers le bas du visage.
        Tous les calques sont des Solid/Composite natifs de Ren'Py 8.3.
        """
        import math

        state = store.char_state.get(tag, {})
        layer = state.get("layer", "master")
        attrs = renpy.get_attributes(tag, layer=layer) or ()
        expr = attrs[0] if attrs else state.get("expr", "neutre")
        key = (tag, expr, intensity)
        if key in KD_BLUE_SHOCK_DISPLAYABLES:
            return KD_BLUE_SHOCK_DISPLAYABLES[key]

        # Le haut du crane varie considerablement selon les personnages.
        # KD_FACE_BOX existe deja pour les cut-ins du jeu (coord. 1024x1536).
        face_x, head_y = KD_FACE_BOX.get(tag, (512, 145))
        face_x = int(face_x)
        head_y = int(head_y)
        strength = {"light": 0.44, "normal": 0.73, "extreme": 0.94}[intensity]
        children = []

        # Ombre bleue en ovale, avec fondu horizontal et vertical.
        # Des tranches de 5 px remplacent les anciennes larges bandes
        # rectangulaires qui recouvraient les cheveux et le decor.
        total_rows = 57
        for row in range(total_rows):
            progress = float(row) / float(total_rows - 1)
            fade_in = min(1.0, progress / 0.14)
            fade_out = max(0.0, 1.0 - progress) ** 1.55
            shape = max(0.0, math.sin(math.pi * (0.08 + 0.87 * progress)))
            half_width = int((192 - 32 * progress) * shape)
            if half_width < 4:
                continue
            y = head_y + 38 + row * 5
            x = face_x - half_width
            alpha = int(255 * strength * 0.45 * fade_in * fade_out)
            if alpha < 2:
                continue
            # Contour legerement adouci : bords translucides.
            edge = max(8, int(half_width * 0.18))
            core_width = max(1, 2 * half_width - 2 * edge)
            children.extend(((x + edge, y),
                             Solid("#153f86%02x" % min(255, alpha),
                                   xsize=core_width, ysize=6)))
            children.extend(((x, y),
                             Solid("#1c4f9b%02x" % max(1, alpha // 4),
                                   xsize=edge, ysize=6)))
            children.extend(((x + edge + core_width, y),
                             Solid("#1c4f9b%02x" % max(1, alpha // 4),
                                   xsize=edge, ysize=6)))

        # Stries dessinees comme des aiguilles : debut marque puis
        # effilement vers le bas, sans barre uniforme qui traverse les yeux.
        count = {"light": 9, "normal": 16, "extreme": 22}[intensity]
        for i in range(count):
            spread = (i + 0.5) / float(count) - 0.5
            x = face_x + int(spread * 325) + ((i * 17) % 11 - 5)
            y = head_y + 70 + (i * 13) % 41
            length = 82 + (i * 31) % 108
            width = 2 + (i * 5) % 4
            base_alpha = int(255 * strength * (0.36 + (i % 3) * 0.075))
            for seg in range(5):
                start_y = y + (length * seg) // 5
                segment_length = max(2, length // 5)
                taper = max(1, width - seg // 2)
                opacity = int(base_alpha * (1.0 - seg / 5.0) ** 1.15)
                if opacity < 3:
                    continue
                children.extend(((x + (width - taper) // 2, start_y),
                                 Solid("#081d42%02x" % min(255, opacity),
                                       xsize=taper, ysize=segment_length + 1)))

        plain_art = Composite((1024, 1536), *children)

        # Les personnages ont une toile native 1024x1536 affichee a 60 %.
        # Le masque reconstruit cette taille pour ne jamais colorer le decor
        # ni les sprites voisins (probleme observe sur les captures).
        # KD_SPRITE_SOURCE_SCALE est defini dans kd_staging.rpy.
        mask = Transform(character_image(tag, expr),
                         zoom=1.0 / KD_SPRITE_SOURCE_SCALE)
        art = AlphaMask(plain_art, mask)
        KD_BLUE_SHOCK_DISPLAYABLES[key] = art
        return art

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
        # Un dialogue peut changer d'expression pendant l'effet :
        # ne jamais remettre l'ancienne expression au moment du nettoyage.
        attrs = renpy.get_attributes(tag, layer=layer) or ()
        if attrs:
            state["expr"] = attrs[0]
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
            what=kd_blue_shock_art(tag, entry["intensity"]),
            tag=kd_anime_shock_overlay_tag(tag),
            at_list=[
                Position(xalign=x, yalign=y),
                kd_blue_shock_overlay_anim(remaining, entry["intensity"]),
            ],
            layer=layer,
            zorder=int(state.get("zorder", 0)) + 1,
        )

    def blue_shock(tag, intensity="normal", duration=1.4, sound=False):
        """Effet local anime, non bloquant, sur un personnage visible.

        Conserve les animations de bouche, les expressions et le cadrage.
        Les parametres sont facultatifs pour un appel en une seule ligne.
        """
        if intensity not in KD_BLUE_SHOCK_LEVELS:
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
        # Affiche les bandes anime natives exactement sur la toile du sprite.
        # Aucun fichier SVG n'est charge (fix de l'asset manquant a l'ecran).
        renpy.show(
            kd_anime_shock_overlay_tag(tag),
            what=kd_blue_shock_art(tag, intensity),
            tag=kd_anime_shock_overlay_tag(tag),
            at_list=[
                Position(xalign=state.get("x", 0.5), yalign=state.get("y", 1.0)),
                kd_blue_shock_overlay_anim(duration, intensity),
            ],
            layer=layer,
            zorder=int(state.get("zorder", 0)) + 1,
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
