# ============================================================
# TRAILER PROMOTIONNEL TIKTOK — KAMI'S DESIRES
# ------------------------------------------------------------
# Bande-annonce autonome d'environ 60 secondes, conçue pour être
# lancée depuis le menu principal puis capturée pour TikTok/Reels.
# Réutilise le kit cinéma de version_2_1_trailer_kit.rpy et les
# assets déjà présents dans le jeu.
# ============================================================

transform trltt_card_in(d=0.0, dy=26):
    alpha 0.0
    yoffset dy
    pause d
    easeout 0.32 alpha 1.0 yoffset 0

transform trltt_blink:
    alpha 0.45
    block:
        linear 0.35 alpha 1.0
        linear 0.35 alpha 0.45
        repeat

screen trltt_controls():
    zorder 995

    key "K_ESCAPE" action Jump("tiktok_promo_trailer_end")
    key "mouseup_3" action Jump("tiktok_promo_trailer_end")
    key "K_SPACE" action NullAction()

    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856
        ypos 26
        xanchor 1.0
        action Jump("tiktok_promo_trailer_end")

screen trltt_center_text(kicker, title, subtitle=None, accent="#5CD3FF", danger=False):
    zorder 430

    add Solid("#01040AF2")
    add "gui/main_menu_kami/bg_orbit.png" at trl_push(7.0, 1.02, 1.08):
        alpha 0.16
    add "gui/main_menu_kami/scanlines.png" alpha 0.10
    add "gui/main_menu_kami/vignette.png" alpha 0.78

    vbox at trltt_card_in(0.08, 34):
        xalign 0.5
        yalign 0.5
        xmaximum 1500
        spacing 18

        text kicker:
            style "trl_kicker"
            xalign 0.5
            size 25
            color ("#FF6877" if danger else accent)

        add Solid("#FF6877" if danger else accent):
            xalign 0.5
            xsize 360
            ysize 3
            at trl_rule_grow(0.18)

        text title:
            style "trl_h1"
            xalign 0.5
            text_align 0.5
            size 74
            color "#F4F9FC"

        if subtitle:
            text subtitle:
                style "trl_quote"
                xalign 0.5
                text_align 0.5
                size 31
                color "#BFD2DE"
                xmaximum 1380

screen trltt_vote_card():
    zorder 435

    add Solid("#02050BEE")
    add "gui/main_menu_kami/bg_orbit.png" at trl_pull(7.0, 1.08, 1.02) alpha 0.14
    add "gui/main_menu_kami/scanlines.png" alpha 0.12
    add "gui/main_menu_kami/vignette.png" alpha 0.78

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 18

        text _("UN SEUL REFUS SUFFIT."):
            style "trl_h1"
            xalign 0.5
            size 68
            color "#F4F9FC"

        text _("Le vote doit être unanime."):
            style "trl_quote"
            xalign 0.5
            size 31
            color "#BFD2DE"

        null height 18

        hbox:
            xalign 0.5
            spacing 28

            frame at trltt_card_in(0.05, 20):
                xsize 330
                ysize 125
                background Solid("#0B2B24EE")
                padding (24, 22)
                text _("POUR") style "trl_h2" xalign 0.5 yalign 0.5 size 46 color "#8FFFC0"

            frame at trltt_card_in(0.18, 20):
                xsize 330
                ysize 125
                background Solid("#25272FEE")
                padding (24, 22)
                text _("ABSTENTION") style "trl_h2" xalign 0.5 yalign 0.5 size 38 color "#D9E1E8"

            frame at trltt_card_in(0.31, 20):
                xsize 330
                ysize 125
                background Solid("#35121AEE")
                padding (24, 22)
                text _("CONTRE") style "trl_h2" xalign 0.5 yalign 0.5 size 46 color "#FF6877"

screen trltt_feature_strip():
    zorder 440

    add Solid("#01040A")
    add "gui/main_menu_kami/bg_orbit.png" at trl_push(6.0, 1.02, 1.09) alpha 0.16
    add "gui/main_menu_kami/scanlines.png" alpha 0.10
    add "gui/main_menu_kami/vignette.png" alpha 0.74

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 24

        text _("PAS SEULEMENT LIRE."):
            style "trl_h1"
            xalign 0.5
            size 68
            color "#F4F9FC"

        hbox:
            xalign 0.5
            spacing 16

            for i, item in enumerate([
                (_("DÉBATTRE"), "#5CD3FF"),
                (_("ENQUÊTER"), "#D68CFF"),
                (_("CONVAINCRE"), "#8FFFC0"),
                (_("CHOISIR"), "#FFD58A"),
            ]):
                frame at trltt_card_in(0.10 + i * 0.10, 22):
                    xsize 340
                    ysize 105
                    background Solid("#07111DDD")
                    padding (16, 18)
                    text item[0]:
                        style "trl_h2"
                        xalign 0.5
                        yalign 0.5
                        size 34
                        color item[1]

screen trltt_endcard():
    zorder 450

    add Solid("#01040A")
    add "gui/main_menu_kami/bg_orbit.png" at trl_breathe(6.0, 1.03, 1.06) alpha 0.22
    add "gui/main_menu_kami/glyph_kami.png":
        xalign 0.5
        yalign 0.5
        alpha 0.16
        at trl_slow_rotate(24.0)
    add "gui/main_menu_kami/scanlines.png" alpha 0.10
    add "gui/main_menu_kami/vignette.png" alpha 0.82

    vbox at trltt_card_in(0.05, 30):
        xalign 0.5
        yalign 0.43
        spacing 15

        text "KAMI'S DESIRES":
            style "trl_h1"
            xalign 0.5
            size 96
            color "#F4F9FC"

        text _("12 REPRÉSENTANTS · 30 JOURS · UNANIMITÉ"):
            style "trl_kicker"
            xalign 0.5
            size 26
            color "#5CD3FF"

        null height 8

        text _("DISPONIBLE GRATUITEMENT SUR ITCH.IO"):
            style "trl_h2"
            xalign 0.5
            size 48
            color "#8FFFC0"
            at trltt_blink

        text _("Jouez dès maintenant."):
            style "trl_quote"
            xalign 0.5
            size 30
            color "#D8E6EE"


# ============================================================
# MONTAGE — ~60 SECONDES
# ============================================================
label tiktok_promo_trailer:

    $ _trltt_original_language = preferences.language
    $ _trltt_original_period = current_period
    $ _game_menu_screen = None
    $ quick_menu = False
    $ renpy.block_rollback()
    $ trl_shake_clear()

    scene black
    stop music fadeout 0.35
    stop sound fadeout 0.2

    show screen trltt_controls
    show screen trl_letterbox(76)
    show screen trl_grade(0.14)

    # 0:00 — Hook immédiat : la promesse du jeu.
    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.4
    play trl_a "audio/trailer/trl_reverse_swell.wav"
    show screen trltt_center_text(
        _("KAMI VOUS DONNE 30 JOURS."),
        _("POUR CHANGER LES LOIS DU MONDE."),
        _("Douze représentants. Un Conclave. Chaque décision peut devenir irréversible."),
        "#5CD3FF"
    )
    $ renpy.pause(4.2, hard=True)
    hide screen trltt_center_text

    # 0:04 — Kami.
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene expression "images/background/kami_diffusion/bg_diffusion_zen.png" at trl_push(5.0, 1.02, 1.10)
    with trl_flash
    $ renpy.pause(2.0, hard=True)

    show screen trl_title(
        _("TOUS LES TROIS JOURS"),
        _("VOUS DEVREZ VOTER."),
        kicker=_("KAMI'S DESIRES"),
        accent="#7DF9FF"
    )
    $ renpy.pause(2.4, hard=True)
    hide screen trl_title

    # 0:09 — La règle centrale.
    scene black
    with trl_cut
    play trl_a "audio/trailer/trl_data_burst.wav"
    show screen trltt_vote_card
    $ renpy.pause(4.3, hard=True)
    hide screen trltt_vote_card

    # 0:13 — Le cast : aperçu sans noyer le joueur de noms.
    play music "audio/music/bgm_tense_meeting.mp3" fadein 0.5
    stop trl_amb fadeout 0.7
    scene bg_observation at trl_push(6.0, 1.02, 1.09)
    with trl_soft
    $ showGroup([
        ("noam", "reflexion"),
        ("lysa", "blase"),
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("iris", "inquiet"),
        ("elias", "inquiet"),
    ])
    $ renpy.pause(3.6, hard=True)
    $ hideGroup()

    # 0:17 — Le gameplay ne se résume pas à lire.
    scene black
    with trl_hardcut
    play trl_a "audio/trailer/trl_swoosh.wav"
    show screen trltt_feature_strip
    $ renpy.pause(3.8, hard=True)
    hide screen trltt_feature_strip

    # 0:21 — Montage de situations et de conséquences.
    play trl_b "audio/trailer/trl_tick.wav"
    scene expression "images/background/cg/bg_cg018.png" at trl_snap(1.20, 1.04, 1.1)
    with trl_hardcut
    $ renpy.pause(1.1, hard=True)

    play trl_a "audio/trailer/trl_tick.wav"
    scene couloir_cafeteria at trl_memory(-1, 0.20)
    with trl_hardcut
    $ renpy.pause(0.8, hard=True)

    play trl_b "audio/trailer/trl_tick.wav"
    scene expression "images/background/cg/bg_cg019.png" at trl_memory(1, 0.20)
    with trl_hardcut
    $ renpy.pause(1.1, hard=True)

    scene black
    with trl_cut
    show screen trltt_center_text(
        _("VOS DÉCISIONS ONT DES CONSÉQUENCES."),
        _("IL N'EXISTE PAS TOUJOURS DE BON CHOIX."),
        _("Convaincre les autres peut sauver des vies. Ou en condamner."),
        "#FFD58A"
    )
    $ renpy.pause(4.6, hard=True)
    hide screen trltt_center_text

    # 0:29 — Relations humaines.
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene bg_chambre at trl_push(5.0, 1.01, 1.07)
    with trl_soft
    $ showGroup([
        ("noam", "sourire", 0.32),
        ("iris", "sourire", 0.68),
    ])
    $ renpy.pause(2.2, hard=True)
    $ hideGroup()

    scene bg_observation at trl_pull(5.0, 1.09, 1.02)
    with trl_soft
    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("lysa", "taquin", 0.70),
    ])
    $ renpy.pause(2.0, hard=True)
    $ hideGroup()

    # 0:33 — Rupture de ton.
    stop music fadeout 0.5
    play trl_amb "audio/trailer/trl_string_tension.wav" fadein 0.3
    scene expression "images/background/kami_diffusion/bg_diffusion_zen.png" at trl_unstable(3, 1.05)
    with trl_flash_red
    $ renpy.pause(1.2, hard=True)

    play trl_a "audio/trailer/trl_glitch_stutter.wav"
    scene black
    with trl_hardcut
    $ renpy.pause(0.18, hard=True)
    scene expression "images/background/kami_diffusion/bg_diffusion_zen.png" at trl_unstable(6, 1.10)
    with trl_hardcut
    $ renpy.pause(0.35, hard=True)
    scene black
    with trl_hardcut

    show screen trltt_center_text(
        _("MAIS QUELQUE CHOSE DÉRAILLE."),
        _("KAMI N'EST PLUS TOUT À FAIT LA MÊME."),
        _("Et dans le Conclave, certaines choses ne devraient pas exister."),
        "#FF6877",
        True
    )
    $ renpy.pause(4.2, hard=True)
    hide screen trltt_center_text

    # 0:39 — Horror tease : très bref, jamais explicatif.
    play trl_b "audio/trailer/trl_heartbeat.wav"
    scene expression "images/background/cg/bg_cg024.png" at trl_snap(1.22, 1.05, 1.0)
    with trl_flash_red
    $ trl_shake(8, 0.18)
    $ renpy.pause(0.85, hard=True)

    scene black
    with trl_hardcut
    $ renpy.pause(0.30, hard=True)

    $ doppelganger_reveal(screamer=False)
    $ renpy.pause(0.35, hard=True)

    scene black
    with trl_hardcut
    $ renpy.pause(0.45, hard=True)

    # 0:42 — Climax.
    play music "audio/music/bgm_system_override.mp3" fadein 0.25
    stop trl_amb fadeout 0.4
    play trl_a "audio/trailer/trl_riser_long.wav"

    show screen trl_title(
        _("CONVAINQUEZ-LES."),
        _("OU MANIPULEZ-LES."),
        kicker=_("CHAQUE VOIX COMPTE"),
        accent="#5CD3FF",
        slam=True
    )
    $ renpy.pause(2.0, hard=True)
    hide screen trl_title

    scene expression "images/background/cg/bg_cg018.png" at trl_memory(-1, 0.16)
    with trl_hardcut
    $ renpy.pause(0.65, hard=True)

    scene bg_observation at trl_memory(1, 0.16)
    with trl_hardcut
    $ renpy.pause(0.65, hard=True)

    scene expression "images/background/cg/bg_cg019.png" at trl_snap(1.18, 1.03, 0.75)
    with trl_flash
    $ renpy.pause(0.65, hard=True)

    scene expression "images/background/cg/bg_cg024.png" at trl_unstable(5, 1.08)
    with trl_flash_red
    $ renpy.pause(0.70, hard=True)

    scene black
    with trl_cut
    play trl_b "audio/trailer/trl_impact_deep.wav"
    show screen trltt_center_text(
        _("12 REPRÉSENTANTS."),
        _("30 JOURS."),
        _("UNE SEULE DÉCISION PEUT CHANGER DES MILLIONS DE VIES."),
        "#8FFFC0"
    )
    $ renpy.pause(4.4, hard=True)
    hide screen trltt_center_text

    # 0:52 — Carton final orienté acquisition.
    stop music fadeout 0.8
    stop trl_amb fadeout 0.5
    play trl_a "audio/trailer/trl_final_hit.wav"
    scene black
    with trl_flash
    show screen trltt_endcard
    $ renpy.pause(6.0, hard=True)
    hide screen trltt_endcard

    # Signature finale de Kami.
    scene black
    with trl_cut
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    show screen trl_epilogue(
        _("ALORS…"),
        _("QU'ALLEZ-VOUS VOTER ?"),
        delay2=0.80
    )
    $ renpy.pause(2.4, hard=True)
    hide screen trl_epilogue

    scene black
    with Dissolve(0.45)
    $ renpy.pause(0.20, hard=True)

    jump tiktok_promo_trailer_end


# ============================================================
# SORTIE — fin naturelle, ÉCHAP, clic droit ou bouton PASSER.
# ============================================================
label tiktok_promo_trailer_end:

    hide screen trltt_controls
    hide screen trltt_center_text
    hide screen trltt_vote_card
    hide screen trltt_feature_strip
    hide screen trltt_endcard
    hide screen trl_quote
    hide screen trl_title
    hide screen trl_shout
    hide screen trl_epilogue
    hide screen trl_grade
    hide screen trl_letterbox
    hide screen doppelganger_overlay

    $ trl_shake_clear()
    $ current_period = _trltt_original_period

    stop trl_a fadeout 0.3
    stop trl_b fadeout 0.3
    stop trl_amb fadeout 0.5
    stop sound fadeout 0.3
    stop music fadeout 0.7

    if preferences.language != _trltt_original_language:
        $ renpy.change_language(_trltt_original_language)

    scene black
    with Dissolve(0.35)
    return
