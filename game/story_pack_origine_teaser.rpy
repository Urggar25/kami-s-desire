# L'ORIGINE — Story Pack 01 | trailer narratif (~30s)
# Construit avec les outils officiels de version_2_1_trailer_kit.rpy.
# Montage: calme trompeur -> méfiance -> perte de contrôle -> horreur -> silence.
# Aucune modification de progression, aucun spoiler explicite sur l'identité des doubles.

screen origine_trailer_controls():
    zorder 995
    key "K_ESCAPE" action Jump("origine_story_pack_teaser_end")
    key "mouseup_3" action Jump("origine_story_pack_teaser_end")
    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856 ypos 27 xanchor 1.0
        action Jump("origine_story_pack_teaser_end")

label origine_story_pack_teaser:
    $ _origin_old_period = current_period
    $ _origin_old_quick_menu = quick_menu
    $ quick_menu = False
    $ trl_shake_clear()
    window hide
    stop music fadeout 0.25
    stop sound fadeout 0.2
    scene black
    show screen origine_trailer_controls
    show screen trl_letterbox(88)
    show screen trl_grade(0.09)

    # 00.00–03.00 : plutôt qu'un carton publicitaire, on surprend une conversation.
    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.5
    play trl_a "audio/trailer/trl_reverse_swell.wav"
    scene bg_cafeteria at trl_push(3.5, 1.03, 1.12, 0.49, 0.52)
    with trl_hardcut
    show screen trl_quote(_("Tu ne peux pas soupçonner tout le monde."), _("IRIS"), "#BCE8FF")
    $ renpy.pause(1.55, hard=True)
    hide screen trl_quote
    play trl_b "audio/trailer/trl_tick.wav"
    scene bg_chambre at trl_pull(3.0, 1.13, 1.04)
    with trl_hardcut
    show screen trl_quote(_("Alors explique-moi ce qu'il y a dans les conduits."), _("NOAM"), "#E6F3F9")
    $ renpy.pause(1.45, hard=True)
    hide screen trl_quote

    # 03.00–07.10 : promesse et premières fissures.
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene bg_conclave at trl_push(3.0, 1.01, 1.15)
    with trl_flash
    show screen trl_title(_("ILS DEVAIENT CHANGER"), _("LE MONDE."), kicker=_("DOUZE REPRÉSENTANTS"), accent="#73D8EA", slam=True)
    $ renpy.pause(2.05, hard=True)
    hide screen trl_title
    scene bg_diffusion_zen at trl_unstable(3, 1.04)
    with trl_hardcut
    show screen trl_quote(_("Vous êtes tellement amusants quand vous avez peur !"), _("KAMI"), "#FF6D83", _("DIFFUSION EN DIRECT"))
    $ renpy.pause(2.05, hard=True)
    hide screen trl_quote

    # 07.10–12.25 : des répliques sous pression, les plans se raccourcissent.
    show screen trl_grade(0.42)
    play music "audio/music/bgm_horror_pulse.mp3" fadein 0.25
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene bg_cg030 at trl_snap(1.17, 1.04, 1.0)
    with trl_hardcut
    show screen trl_quote(_("Qu'est-ce que tu as vu ?!"), _("IRIS"), "#BCE8FF")
    $ renpy.pause(1.3, hard=True)
    hide screen trl_quote
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene bg_infirmerie at trl_memory(-1, 0.18)
    with trl_blink
    show screen trl_quote(_("Mara... qu'est-ce que tu fous ?"), _("NOAM"), "#FFFFFF")
    $ renpy.pause(1.25, hard=True)
    hide screen trl_quote
    play trl_a "audio/trailer/trl_sub_drop.wav"
    scene bg_diffusion_colere at trl_unstable(7, 1.10)
    with trl_flash_red
    show screen trl_title(_("NE FAITES CONFIANCE"), _("À PERSONNE."), accent="#FF415D", slam=True, danger=True)
    $ renpy.pause(1.55, hard=True)
    hide screen trl_title
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene bg_salle_goumi_cachee at trl_snap(1.29, 1.02, 0.55)
    with trl_hardcut
    show screen trl_quote(_("Lâche ce couteau, Noam !"), _("IRIS"), "#FF8C94")
    $ renpy.pause(1.15, hard=True)
    hide screen trl_quote

    # 12.25–19.65 : confrontation -> corps -> choc, aucun reveal expliqué.
    show screen trl_grade(0.78)
    play trl_a "audio/trailer/trl_riser_short.wav"
    scene bg_conduit_reseau at trl_push(2.0, 1.12, 1.22, 0.56, 0.48)
    with trl_hardcut
    show screen trl_quote(_("Il y a quelqu'un dans les murs."), _("NOAM"), "#FFFFFF")
    $ renpy.pause(1.25, hard=True)
    hide screen trl_quote
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene bg_cg040 at trl_snap(1.20, 1.03, 0.60)
    with trl_flash_red
    $ renpy.pause(0.70, hard=True)
    scene black
    with trl_hardcut
    show screen trl_shout(_("UN CORPS."), accent="#FF3A5C", psize=175)
    play trl_b "audio/trailer/trl_impact_deep.wav"
    $ renpy.pause(1.15, hard=True)
    hide screen trl_shout
    play trl_a "audio/trailer/trl_glitch_stutter.wav"
    scene bg_cg040 at trl_snap(1.45, 1.11, 0.45)
    with trl_hardcut
    $ renpy.pause(0.43, hard=True)
    scene bg_cg030 at trl_snap(1.22, 1.03, 0.4)
    with trl_hardcut
    $ renpy.pause(0.38, hard=True)
    scene bg_diffusion_desespoir at trl_unstable(12, 1.11)
    with trl_flash_red
    $ renpy.pause(0.40, hard=True)
    scene bg_conduit_reseau at trl_snap(1.24, 1.01, 0.35)
    with trl_hardcut
    $ renpy.pause(0.40, hard=True)
    scene bg_cg070 at trl_snap(1.48, 1.18, 0.33)
    with trl_flash_red
    $ renpy.pause(0.35, hard=True)
    scene black
    with trl_hardcut
    play trl_b "audio/trailer/trl_sub_drop.wav"
    show screen trl_quote(_("Vous ne m'empêcherez pas de les libérer !"), _("???"), "#FF657C")
    $ renpy.pause(1.8, hard=True)
    hide screen trl_quote

    # 19.65–24.70 : menace et promesse, en contrastant avec le silence.
    show screen trl_grade(0.92)
    play trl_a "audio/trailer/trl_string_tension.wav"
    show screen trl_title(_("CEUX QUI VOUS ENTOURENT"), _("SONT-ILS ENCORE EUX-MÊMES ?"), accent="#FF617A", danger=True)
    $ renpy.pause(2.25, hard=True)
    hide screen trl_title
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene bg_conclave at trl_unstable(10, 1.09)
    with trl_flash_red
    show screen trl_title(_("7 FINS"), _("JOURS 5 À 30"), kicker=_("SEPT DESTINS. UNE VÉRITÉ ENFOUIE."), accent="#E9F8FF", slam=True)
    $ renpy.pause(2.8, hard=True)
    hide screen trl_title

    # 24.70–30.00 : arrêt brutal, impact final puis pack.
    stop music fadeout 0.15
    stop trl_amb fadeout 0.25
    scene black
    with trl_hardcut
    $ renpy.pause(0.45, hard=True)
    play trl_a "audio/trailer/trl_final_hit.wav"
    show screen trl_endcard(_("STORY PACK 01 — L'ORIGINE"), _("UNE DES VÉRITÉS CACHÉES DU CONCLAVE"), note=_("JOURS 5 À 30   ·   7 FINS   ·   COMBATS, TRAHISONS ET HORREUR"))
    $ renpy.pause(4.1, hard=True)
    hide screen trl_endcard
    jump origine_story_pack_teaser_end

label origine_story_pack_teaser_end:
    hide screen origine_trailer_controls
    hide screen trl_quote
    hide screen trl_title
    hide screen trl_shout
    hide screen trl_endcard
    hide screen trl_grade
    hide screen trl_letterbox
    $ trl_shake_clear()
    $ current_period = _origin_old_period
    $ quick_menu = _origin_old_quick_menu
    stop trl_a fadeout 0.2
    stop trl_b fadeout 0.2
    stop trl_amb fadeout 0.3
    stop music fadeout 0.3
    scene black
    with Dissolve(0.25)
    return
