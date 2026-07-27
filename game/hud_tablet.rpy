# =============================================================
# MINI-TABLETTE HUD — bouton permanent haut-gauche (Noam animé)
# Ouvre l'écran tablet_home. Désactivable via l'option
# "Tablette dans l'HUD" dans les Préférences.
# =============================================================

default persistent.hud_tablet_enabled = True

init python:
    def _hud_tablet_blocked():
        # Masque le bouton si une surface tablette/menu modale est déjà ouverte
        for s in ("tablet_home", "tablet_stats", "stat_check", "vote_dossier",
                  "codex_menu", "vote_screen", "save", "load", "preferences"):
            if renpy.get_screen(s):
                return True
        return False

init 999 python:
    if "hud_tablet_button" not in config.overlay_screens:
        config.overlay_screens.append("hud_tablet_button")


# ---- Animations ----
transform hud_tab_intro:
    xoffset -40 alpha 0.0
    easein 0.45 xoffset 0 alpha 1.0

transform hud_tab_glow:
    alpha 0.25
    linear 1.6 alpha 0.55
    linear 1.6 alpha 0.25
    repeat

transform hud_tab_press:
    on hover:
        linear 0.12 zoom 1.06
    on idle:
        linear 0.12 zoom 1.0


screen hud_tablet_button():
    zorder 95

    if persistent.hud_tablet_enabled and not main_menu and not _hud_tablet_blocked():
        button:
            xpos 20 ypos 18
            xysize (168, 112)
            background None
            focus_mask None
            action Show("tablet_home")
            at (hud_tab_intro, hud_tab_press)

            fixed:
                xysize (168, 112)

                # Halo pulsé (derrière)
                add Transform("hud/tablet/glow_soft.png", size=(210, 150),
                              matrixcolor=TintMatrix("#5CD3FF")) xalign 0.5 yalign 0.5 at hud_tab_glow

                # Icône tablette (un seul PNG propre)
                add Transform("hud/tablet/hud_tablet_icon.png", size=(168, 112)) xalign 0.5 yalign 0.5
