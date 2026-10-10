# Impact FX — impacts visuels sans alterer les choix ou les images de scene.
# Usage : call impact_fx("hard", direction="left", blood="screen")
# 'light', 'hard', 'brutal', 'critical' ; blood: None, 'screen', 'spray'.
# L'effet agit sur le layer master, conserve le cadrage et nettoie les overlays.

transform _impact_fx_flash:
    alpha 0.85
    linear 0.07 alpha 0.0

transform _impact_fx_blood:
    alpha 0.0
    linear 0.06 alpha 0.95
    pause 0.24
    linear 0.50 alpha 0.0

transform _impact_fx_rgb_left:
    alpha 0.0
    linear 0.04 alpha 0.66
    linear 0.21 alpha 0.0

transform _impact_fx_rgb_right:
    alpha 0.0
    linear 0.04 alpha 0.59
    linear 0.21 alpha 0.0

screen impact_fx_overlay(blood=None, flash=True, rgb=False, side="left"):
    zorder 990
    if flash:
        add Solid("#ffffff") at _impact_fx_flash
    if rgb:
        add Solid("#f0205099", xsize=14, ysize=config.screen_height):
            xpos 0 if side == "left" else config.screen_width - 14
            at _impact_fx_rgb_left
        add Solid("#21dfff99", xsize=12, ysize=config.screen_height):
            xpos config.screen_width - 12 if side == "left" else 0
            at _impact_fx_rgb_right
    if blood == "screen":
        add "images/effects/impact_blood_screen.svg" at _impact_fx_blood
    elif blood == "spray":
        add "images/effects/impact_blood_spray.svg" at _impact_fx_blood

init python:
    def impact_fx_directional_shake(direction="right", strength=18, duration=0.26):
        # Restauration dans shake() (camera + zoom existant).
        from functools import partial
        sign = -1 if direction == "left" else 1
        def _kick(trans, st, at):
            q = min(1.0, st / max(0.01, duration))
            # Recul initial et deux oscillations decroissantes.
            import math
            trans.xoffset = int(sign * strength * math.exp(-5.2 * q) * math.cos(12.0 * q))
            trans.yoffset = int(-strength * 0.28 * math.exp(-6.0 * q) * math.sin(15.0 * q))
            return None if st > duration else 0.0
        renpy.show_layer_at([Transform(function=_kick)], layer="master")
        renpy.pause(duration, hard=True)
        renpy.show_layer_at([], layer="master")
        if "cam_restore_current" in globals():
            cam_restore_current(t=0.0, layers=("master",))

label impact_fx(level="hard", direction="right", blood=None):
    # Reutilisable dans les scenes : gel, flash, secousse, zoom bref et liseres RGB.
    $ _fx_power = {"light": 8, "hard": 17, "brutal": 27, "critical": 34}.get(level, 17)
    $ _fx_time = {"light": 0.13, "hard": 0.22, "brutal": 0.30, "critical": 0.38}.get(level, 0.22)
    $ _fx_rgb = level in ("brutal", "critical")
    show screen impact_fx_overlay(blood=blood, flash=True, rgb=_fx_rgb, side=direction)
    # Arret sur image volontairement court, avec ecran fige avant le recul.
    $ renpy.pause(0.05 if level == "light" else 0.10, hard=True)
    $ impact_fx_directional_shake(direction, _fx_power, _fx_time)
    if level in ("brutal", "critical"):
        $ renpy.pause(0.24, hard=True)
    hide screen impact_fx_overlay
    return
