# ============================================================
# BANDE-ANNONCE OFFICIELLE — VERSION 3.0
# « LA ROUTE DE L'ESPOIR »
# ------------------------------------------------------------
# Montage autonome d'environ 27 secondes. Réutilise le langage
# visuel et le kit sonore du trailer 2.1, sans toucher aux
# sauvegardes, aux récompenses ou aux cosmétiques du joueur.
# ============================================================


transform trl30_card_in(d=0.0, dx=0):
    alpha 0.0
    xoffset dx
    pause d
    easeout 0.32 alpha 1.0 xoffset 0


transform trl30_badge_pulse:
    alpha 0.72
    block:
        ease 0.55 alpha 1.0
        ease 0.55 alpha 0.72
        repeat


screen trl30_controls():
    zorder 990

    key "K_ESCAPE" action Jump("version_3_0_trailer_end")
    key "mouseup_3" action Jump("version_3_0_trailer_end")
    key "K_SPACE" action NullAction()

    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856
        ypos 26
        xanchor 1.0
        action Jump("version_3_0_trailer_end")


screen trl30_route_badge():
    zorder 350

    frame at trl30_card_in(0.08, -60):
        xpos 126
        ypos 760
        xsize 870
        ysize 158
        background Solid("#04140EEA")
        padding (30, 22, 30, 22)

        vbox:
            spacing 8
            text _("NOUVELLE BRANCHE NARRATIVE"):
                style "trl_micro"
                size 20
                color "#8FFFC0"
            text _("ROUTE DE L'ESPOIR DÉBLOQUÉE"):
                style "trl_h2"
                size 48
                color "#E8FFF0"

        add Solid("#4DFF9A"):
            xpos 0
            ypos 0
            xsize 7
            ysize 114
            at trl30_badge_pulse


screen trl30_feature_card(kicker, title, subtitle, accent="#5CD3FF", bg=None, icon=None):
    zorder 420

    add Solid("#01040A")
    if bg:
        add bg at trl_push(7.0, 1.02, 1.10):
            alpha 0.34
    else:
        add "gui/main_menu_kami/bg_orbit.png" at trl_push(9.0, 1.03, 1.10):
            alpha 0.18

    add "gui/main_menu_kami/scanlines.png" alpha 0.12
    add "gui/main_menu_kami/vignette.png" alpha 0.78

    if icon:
        add Transform(icon, xysize=(210, 210), matrixcolor=TintMatrix(accent)) at trl30_card_in(0.05, -45):
            xpos 230
            yalign 0.5

    vbox at trl30_card_in(0.12, 55):
        xpos (530 if icon else 310)
        yalign 0.5
        xsize (1160 if icon else 1300)
        spacing 18

        text kicker:
            style "trl_kicker"
            color accent
            size 24
        add Solid(accent) xsize 360 ysize 3 at trl_rule_grow(0.18)
        text title:
            style "trl_h1"
            size 70
            color "#F4F9FC"
        text subtitle:
            style "trl_quote"
            size 31
            color "#BFD2DE"
            xmaximum (1080 if icon else 1260)


screen trl30_skins_showcase():
    zorder 420

    $ iris_preview = profile_cosmetic_preview("iris", "tenue2", [])
    $ ryn_preview = profile_cosmetic_preview("ryn", "tenue2", [])

    add Solid("#01040A")
    add "gui/main_menu_kami/bg_orbit.png" at trl_push(8.0, 1.03, 1.11) alpha 0.20
    add "gui/main_menu_kami/scanlines.png" alpha 0.10
    add "gui/main_menu_kami/vignette.png" alpha 0.72

    add Transform(iris_preview, zoom=0.84) at trl30_card_in(0.05, -100):
        xalign 0.25
        yalign 1.08
    add Transform(ryn_preview, zoom=0.84) at trl30_card_in(0.16, 100):
        xalign 0.75
        yalign 1.08

    frame:
        xalign 0.5
        ypos 150
        xsize 760
        ysize 188
        background Solid("#020711E8")
        padding (28, 20, 28, 20)

        vbox:
            xalign 0.5
            spacing 8
            text _("PERSONNALISATION") style "trl_kicker" color "#FF9EC8" xalign 0.5
            text _("PLUSIEURS SKINS") style "trl_h2" size 54 xalign 0.5
            text _("ACCESSIBLES GRATUITEMENT") style "trl_kicker" size 25 color "#8FFFC0" xalign 0.5


screen trl30_period_badge(period_name, accent):
    zorder 360

    frame at trl30_card_in(0.0, -30):
        xpos 126
        ypos 142
        background Solid("#020711E8")
        padding (22, 12, 22, 12)

        hbox:
            spacing 14
            add Solid(accent) xsize 5 ysize 38
            text period_name style "trl_kicker" size 25 color accent


# ============================================================
# MONTAGE — ENVIRON 30 SECONDES
# ============================================================
label version_3_0_trailer:

    $ _trl30_original_language = preferences.language
    $ _trl30_original_period = current_period
    $ _game_menu_screen = None
    $ quick_menu = False
    $ renpy.block_rollback()
    $ trl_shake_clear()

    scene black
    stop music fadeout 0.35
    stop sound fadeout 0.2

    show screen trl30_controls
    show screen trl_letterbox(88)
    show screen trl_grade(0.16)

    # Attaque directe.
    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.5
    play trl_a "audio/trailer/trl_reverse_swell.wav"
    show screen trl_title(
        _("LE CONCLAVE N'A PAS FINI"),
        _("DE VOUS METTRE À L'ÉPREUVE."),
        kicker=_("KAMI'S DESIRES 3.0"),
        bg="images/background/kami_diffusion/bg_diffusion_zen.png",
        bg_alpha=0.28
    )
    $ renpy.pause(2.0, hard=True)
    hide screen trl_title

    # Première image du nouveau parcours.
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene expression "images/background/cg/bg_cg018.png" at trl_push(3.0, 1.02, 1.09, 0.48, 0.52)
    with trl_flash
    $ renpy.pause(0.95, hard=True)

    # Annonce des deux journées.
    scene black
    with trl_cut
    play trl_a "audio/trailer/trl_data_burst.wav"
    show screen trl_title(
        _("JOURS 4_1 ET 5_1"),
        _("MAINTENANT DISPONIBLES."),
        kicker=_("NOUVEAUX CHOIX · NOUVELLES CONSÉQUENCES"),
        accent="#7DF9FF",
        slam=True
    )
    $ renpy.pause(1.7, hard=True)
    hide screen trl_title

    # La promesse de la route positive.
    play music "audio/music/bgm_careful_wanting.mp3" fadein 0.6
    stop trl_amb fadeout 0.8
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene expression "images/background/cg/bg_cg019.png" at trl_pull(3.5, 1.09, 1.01)
    with trl_soft
    show screen trl30_route_badge
    $ renpy.pause(1.6, hard=True)
    hide screen trl30_route_badge

    # Évènements limités dans le temps.
    play trl_b "audio/trailer/trl_tick.wav"
    scene black
    with trl_hardcut
    show screen trl30_feature_card(
        _("NOUVEAU CONTENU EN DIRECT"),
        _("ÉVÈNEMENTS LIMITÉS DANS LE TEMPS"),
        _("Des défis temporaires, une progression dédiée et des récompenses à récupérer avant la fin du compte à rebours."),
        "#D68CFF",
        "events/seven_questions/textures/bg_quiz.png",
        "gui/main_menu_kami/glyph_kami.png"
    )
    $ renpy.pause(1.8, hard=True)
    hide screen trl30_feature_card

    # Cosmétiques gratuits.
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene black
    with trl_hardcut
    show screen trl30_skins_showcase
    $ renpy.pause(1.8, hard=True)
    hide screen trl30_skins_showcase

    # Codex enrichi.
    play trl_b "audio/trailer/trl_data_burst.wav"
    scene black
    with trl_hardcut
    show screen trl30_feature_card(
        _("SYSTÈME AMÉLIORÉ"),
        _("UN CODEX PLUS VIVANT"),
        _("Navigation enrichie, profils plus lisibles, souvenirs et personnalisation réunis au même endroit."),
        "#5CD3FF",
        "images/hud/codex/banner_conclave.png",
        "images/hud/codex/codex_logo.png"
    )
    $ renpy.pause(1.7, hard=True)
    hide screen trl30_feature_card

    # Démonstration réelle du cycle lumineux.
    play trl_a "audio/trailer/trl_riser_short.wav"
    $ current_period = "Matin"
    scene bg_chambre at trl_push(4.0, 1.01, 1.06, 0.50, 0.50)
    with trl_soft
    show screen trl30_period_badge(_("MATIN · LUMIÈRE CHAUDE"), "#FFD58A")
    $ renpy.pause(0.45, hard=True)

    $ current_period = "Après-midi"
    hide screen trl30_period_badge
    with trl_soft
    show screen trl30_period_badge(_("APRÈS-MIDI · LUMIÈRE CLAIRE"), "#9BE7FF")
    $ renpy.pause(0.45, hard=True)

    $ current_period = "Soir"
    hide screen trl30_period_badge
    with trl_soft
    show screen trl30_period_badge(_("SOIR · LUMIÈRE TAMISÉE"), "#F0A07A")
    $ renpy.pause(0.55, hard=True)
    hide screen trl30_period_badge

    # Changement automatique de salles, monté en rafale.
    play trl_b "audio/trailer/trl_tick.wav"
    scene couloir_cafeteria at trl_memory(-1, 0.18)
    with trl_hardcut
    $ renpy.pause(0.35, hard=True)
    play trl_a "audio/trailer/trl_tick.wav"
    scene bg_observation at trl_memory(1, 0.18)
    with trl_hardcut
    $ renpy.pause(0.35, hard=True)

    # Résumé des améliorations automatiques.
    scene black
    with trl_cut
    play trl_b "audio/trailer/trl_impact_deep.wav"
    show screen trl_title(
        _("LE MONDE CHANGE"),
        _("AVEC L'HEURE ET VOS DÉPLACEMENTS."),
        kicker=_("LUMIÈRE AUTOMATIQUE · CHANGEMENTS DE SALLES ANIMÉS"),
        accent="#F0A07A"
    )
    $ renpy.pause(1.3, hard=True)
    hide screen trl_title

    # Dernier battement narratif avant le logo.
    play trl_a "audio/trailer/trl_string_tension.wav"
    scene expression "images/background/cg/bg_cg024.png" at trl_snap(1.18, 1.03, 1.2)
    with trl_flash_red
    $ trl_shake(10, 0.20)
    $ renpy.pause(1.0, hard=True)

    # Carton final.
    stop music fadeout 0.8
    play trl_a "audio/trailer/trl_final_hit.wav"
    scene black
    with trl_flash
    show screen trl_grade(0.30)
    show screen trl_endcard(
        _("VERSION 3.0 — LA ROUTE DE L'ESPOIR"),
        _("JOURS 4_1 ET 5_1 DISPONIBLES"),
        note=_("ÉVÈNEMENTS LIMITÉS  ·  SKINS GRATUITS  ·  CODEX AMÉLIORÉ  ·  MONDE ANIMÉ")
    )
    $ renpy.pause(3.6, hard=True)
    hide screen trl_endcard

    # Signature finale.
    hide screen trl_grade
    scene black
    with trl_cut
    play trl_a "audio/trailer/trl_heartbeat.wav"
    show screen trl_epilogue(
        _("L'ESPOIR N'EST PLUS UNE HYPOTHÈSE."),
        _("C'EST UNE ROUTE."),
        delay2=1.15
    )
    $ renpy.pause(2.0, hard=True)
    hide screen trl_epilogue

    scene black
    with Dissolve(0.6)
    $ renpy.pause(0.25, hard=True)

    jump version_3_0_trailer_end


# ============================================================
# SORTIE — fin naturelle, ÉCHAP, clic droit ou bouton PASSER.
# ============================================================
label version_3_0_trailer_end:

    hide screen trl30_controls
    hide screen trl30_route_badge
    hide screen trl30_feature_card
    hide screen trl30_skins_showcase
    hide screen trl30_period_badge
    hide screen trl_quote
    hide screen trl_title
    hide screen trl_shout
    hide screen trl_endcard
    hide screen trl_epilogue
    hide screen trl_grade
    hide screen trl_letterbox

    $ trl_shake_clear()
    $ current_period = _trl30_original_period

    stop trl_a fadeout 0.3
    stop trl_b fadeout 0.3
    stop trl_amb fadeout 0.5
    stop sound fadeout 0.3
    stop music fadeout 0.7

    if preferences.language != _trl30_original_language:
        $ renpy.change_language(_trl30_original_language)

    scene black
    with Dissolve(0.35)
    return
