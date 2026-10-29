# Trailer public du DLC « Les autres vies ».
# Exclusivement des assets de base : bande-annonce disponible sans achat.
# Aucune CG du laboratoire ni révélation de l'identité des doubles.

screen kd_dlc_trailer_controls():
    zorder 995
    key "K_ESCAPE" action Jump("kd_dlc_doppelganger_trailer_end")
    key "mouseup_3" action Jump("kd_dlc_doppelganger_trailer_end")
    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856 ypos 27 xanchor 1.0
        action Jump("kd_dlc_doppelganger_trailer_end")

label kd_dlc_doppelganger_trailer:
    $ _kd_dlc_old_period = current_period
    $ _kd_dlc_old_quick = quick_menu
    $ quick_menu = False
    $ trl_shake_clear()
    window hide
    stop music fadeout 0.4
    scene black
    show screen kd_dlc_trailer_controls
    show screen trl_letterbox(88)
    show screen trl_grade(0.20)

    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.6
    show screen trl_title(
        _("VOUS AVEZ DÉJÀ CHOISI."),
        _("MAIS ÉTAIT-CE LE BON CHOIX ?"),
        kicker=_("KAMI'S DESIRES  //  STORY PACK 01"),
        accent="#F2819B"
    )
    $ renpy.pause(2.5, hard=True)
    hide screen trl_title

    play trl_a "audio/trailer/trl_tick.wav"
    scene bg_conclave at trl_push(3.5, 1.03, 1.12)
    with trl_hardcut
    show screen trl_quote(_("On était censés décider ensemble."), _("NOAM"), "#DCEFF7")
    $ renpy.pause(1.8, hard=True)
    hide screen trl_quote

    play trl_b "audio/trailer/trl_reverse_swell.wav"
    scene bg_cafeteria at trl_pull(3.5, 1.09, 1.02)
    with trl_soft
    show screen trl_quote(_("T'as vraiment confiance en eux ?"), _("LYSA"), "#9DDAEB")
    $ renpy.pause(1.8, hard=True)
    hide screen trl_quote

    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.0
    scene bg_diffusion_zen at trl_unstable(4.0, 1.04)
    with trl_hardcut
    show screen trl_title(_("UN SEUL CHOIX"), _("PEUT TOUT CHANGER."), kicker=_("JOUR 20"), accent="#FB7E96")
    $ renpy.pause(1.8, hard=True)
    hide screen trl_title

    play trl_a "audio/trailer/trl_glitch_stutter.wav"
    scene bg_cg030 at trl_snap(1.15, 1.04, 1.0)
    with trl_flash_red
    $ renpy.pause(1.2, hard=True)

    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene bg_salle_goumi_cachee at trl_push(3.0, 1.05, 1.16)
    with trl_hardcut
    show screen trl_quote(_("Pose ce couteau, Noam."), _("IRIS"), "#FFB3C0")
    $ renpy.pause(2.0, hard=True)
    hide screen trl_quote

    scene black
    with trl_cut
    stop music fadeout 1.1
    play trl_a "audio/trailer/trl_heartbeat.wav"
    show screen trl_title(_("VOUS N'AVEZ VU"), _("QU'UNE SEULE FIN."), kicker=_("DES ROUTES ET DES DÉCISIONS INÉDITES"), accent="#73D7E9")
    $ renpy.pause(2.1, hard=True)
    hide screen trl_title

    play trl_b "audio/trailer/trl_final_hit.wav"
    show screen trl_endcard(
        _("LES AUTRES VIES"),
        _("ROUTE DOPPELGÄNGER  ·  JOURS 20 À 30"),
        note=_("UNE FIN GRATUITE  //  LES AUTRES CHEMINS DANS LE DLC")
    )
    $ renpy.pause(3.2, hard=True)
    hide screen trl_endcard
    jump kd_dlc_doppelganger_trailer_end

label kd_dlc_doppelganger_trailer_end:
    hide screen kd_dlc_trailer_controls
    hide screen trl_title
    hide screen trl_quote
    hide screen trl_endcard
    hide screen trl_grade
    hide screen trl_letterbox
    $ trl_shake_clear()
    $ current_period = _kd_dlc_old_period
    $ quick_menu = _kd_dlc_old_quick
    stop trl_a fadeout 0.2
    stop trl_b fadeout 0.2
    stop trl_amb fadeout 0.3
    stop music fadeout 0.3
    scene black
    with Dissolve(0.25)
    return
