# ============================================================
# Animations automatiques de dialogue
#
# Les effets sont derives du texte affiche, apres retrait des balises Ren'Py.
# Ils restent purement visuels et n'ajoutent aucune pause au dialogue.
# ============================================================

default persistent.dialogue_animations = True


init -2 python:
    import re as _dialogue_re
    import random as _dialogue_random
    from functools import partial as _dialogue_partial

    _DIALOGUE_SHAKE_PROFILES = {
        "exclaim_soft": (4, 0.22, 0.35),
        "exclaim_medium": (9, 0.30, 0.45),
        "exclaim_strong": (16, 0.42, 0.60),
    }

    _DIALOGUE_SFX_PROFILES = {
        "question": ("audio/sfx_question.mp3", 0.70),
        "question_strong": ("audio/sfx_question.mp3", 0.90),
        "exclaim_soft": ("audio/sfx_exclamation.mp3", 0.65),
        "exclaim_medium": ("audio/sfx_exclamation.mp3", 0.85),
        "exclaim_strong": ("audio/sfx_exclamation.mp3", 1.00),
    }

    def dialogue_effect_profile(text):
        """Retourne l'effet de ponctuation le plus expressif de la replique."""
        if not getattr(persistent, "dialogue_animations", True):
            return "none"

        clean = _dialogue_re.sub(r"\{[^{}]*\}", "", text or "")
        bang_runs = _dialogue_re.findall(r"!+", clean)
        question_runs = _dialogue_re.findall(r"\?+", clean)
        max_bangs = max([len(run) for run in bang_runs] or [0])
        max_questions = max([len(run) for run in question_runs] or [0])

        if max_bangs >= 3:
            return "exclaim_strong"
        if "?!" in clean or "!?" in clean or (max_bangs and max_questions):
            return "exclaim_medium"
        if max_bangs >= 2:
            return "exclaim_medium"
        if max_bangs == 1:
            return "exclaim_soft"
        if max_questions >= 2:
            return "question_strong"
        if max_questions == 1:
            return "question"
        if "..." in clean or "…" in clean:
            return "suspense"
        return "none"

    def dialogue_effect_color(profile):
        if profile == "exclaim_strong":
            return "#ff405c"
        if profile in ("exclaim_medium", "exclaim_soft"):
            return "#ffb84d"
        if profile in ("question", "question_strong"):
            return "#5cd3ff"
        return "#a98cff"

    def dialogue_edge_transform(profile):
        return getattr(store, "dialogue_edge_" + profile, store.dialogue_edge_none)

    def _dialogue_layer_shake(trans, st, at, intensity, duration, vertical):
        if st >= duration:
            trans.xoffset = 0
            trans.yoffset = 0
            trans.zoom = 1.0
            return None

        damp = 1.0 - (st / duration)
        trans.xoffset = int(_dialogue_random.uniform(-intensity, intensity) * damp)
        trans.yoffset = int(_dialogue_random.uniform(-intensity, intensity) * damp * vertical)
        # Ce leger debord evite de montrer le bord du decor pendant la secousse.
        trans.zoom = 1.008
        return 0.0

    def _dialogue_camera_base(layer):
        """Recompose la camera courante avant d'y superposer une secousse."""
        x, y, z = cam_current(layer)
        dx = int((0.5 - x) * (config.screen_width * (z - 1.0)))
        dy = int((0.5 - y) * (config.screen_height * (z - 1.0)))
        return cam_runtime(dx0=dx, dy0=dy, z0=z, dx1=dx, dy1=dy, z1=z, t=0.0)

    def start_dialogue_animation(text):
        """Declenche le son et la secousse sans bloquer le dialogue."""
        profile = dialogue_effect_profile(text)
        if profile == "none" or renpy.is_skipping():
            return

        sound_settings = _DIALOGUE_SFX_PROFILES.get(profile)
        if sound_settings is not None:
            sound_path, sound_volume = sound_settings
            if renpy.loadable(sound_path):
                renpy.sound.play(sound_path, relative_volume=sound_volume)

        shake_settings = _DIALOGUE_SHAKE_PROFILES.get(profile)
        if shake_settings is None:
            return

        intensity, duration, vertical = shake_settings
        motion = Transform(function=_dialogue_partial(
            _dialogue_layer_shake,
            intensity=intensity,
            duration=duration,
            vertical=vertical,
        ))
        for layer in ("bgcam", "master"):
            base = _dialogue_camera_base(layer)
            renpy.show_layer_at([base, motion], layer=layer)


transform dialogue_edge_none:
    alpha 0.0

transform dialogue_edge_exclaim_strong:
    alpha 0.0
    linear 0.05 alpha 0.52
    easeout 0.38 alpha 0.0

transform dialogue_edge_exclaim_medium:
    alpha 0.0
    linear 0.06 alpha 0.34
    easeout 0.30 alpha 0.0

transform dialogue_edge_exclaim_soft:
    alpha 0.0
    linear 0.06 alpha 0.20
    easeout 0.24 alpha 0.0

transform dialogue_edge_question:
    alpha 0.0
    easeout 0.16 alpha 0.26
    easein 0.34 alpha 0.0

transform dialogue_edge_question_strong:
    alpha 0.0
    easeout 0.16 alpha 0.30
    easein 0.40 alpha 0.0

transform dialogue_edge_suspense:
    alpha 0.0
    easeout 0.35 alpha 0.18
    easein 0.55 alpha 0.0


transform dialogue_strong_flash:
    alpha 0.0
    linear 0.035 alpha 0.13
    easeout 0.16 alpha 0.0


screen dialogue_punctuation_overlay(what):
    $ profile = dialogue_effect_profile(what)

    if profile != "none":
        $ effect_color = dialogue_effect_color(profile)
        $ edge_motion = dialogue_edge_transform(profile)
        fixed:
            xfill True
            yfill True
            at edge_motion

            add Solid(effect_color) xpos 0 ypos 0 xsize config.screen_width ysize 7
            add Solid(effect_color) xpos 0 ypos (config.screen_height - 7) xsize config.screen_width ysize 7
            add Solid(effect_color) xpos 0 ypos 0 xsize 7 ysize config.screen_height
            add Solid(effect_color) xpos (config.screen_width - 7) ypos 0 xsize 7 ysize config.screen_height

        if profile == "exclaim_strong":
            add Solid(effect_color) at dialogue_strong_flash
