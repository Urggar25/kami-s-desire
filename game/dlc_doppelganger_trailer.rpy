# LES AUTRES VIES — trailer narratif ~60 secondes.
# Images tirées des jours 20–30 ; les CG premium ne sont montrées
# que si les fichiers du DLC sont installés. Aucun twist majeur révélé.
# Réutilise les écrans/transitions/canaux du kit trailer existant.

screen kd_dlc_trailer_controls():
    zorder 995
    key "K_ESCAPE" action Jump("kd_dlc_doppelganger_trailer_end")
    key "mouseup_3" action Jump("kd_dlc_doppelganger_trailer_end")
    textbutton _("PASSER  ▸▸"):
        style "trl_skip_button"
        xpos 1856 ypos 27 xanchor 1.0
        action Jump("kd_dlc_doppelganger_trailer_end")

# Ne jamais laisser la bande-annonce altérer les sauvegardes/progression.
label kd_dlc_doppelganger_trailer:
    $ _kd_dlc_old_period = current_period
    $ _kd_dlc_old_quick = quick_menu
    $ quick_menu = False
    $ trl_shake_clear()
    window hide
    stop music fadeout 0.35
    stop sound fadeout 0.2
    scene black
    show screen kd_dlc_trailer_controls
    show screen trl_letterbox(88)
    show screen trl_grade(0.14)

    # 00–06 | Fausse accalmie : les derniers jours devraient être simples.
    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.8
    scene bg_cafeteria at trl_push(5.0, 1.01, 1.08)
    with trl_soft
    show screen trl_quote(_("Dans quelques jours, on sera rentrés."), _("NOAM"), "#DBEAF3")
    $ renpy.pause(2.7, hard=True)
    hide screen trl_quote
    play trl_a "audio/trailer/trl_tick.wav"
    show screen trl_quote(_("T'as vraiment une tête affreuse. Et là, je suis gentille."), _("MARA"), "#F2B0B5")
    $ renpy.pause(2.6, hard=True)
    hide screen trl_quote

    # 06–12 | Doute : jour 23, examens, fatigue et pertes de mémoire.
    play trl_b "audio/trailer/trl_reverse_swell.wav"
    scene bg_infirmerie at trl_pull(5.0, 1.10, 1.02)
    with trl_hardcut
    show screen trl_quote(_("T'as eu de la fièvre, des trous de mémoire..."), _("SAEL"), "#C2DCED")
    $ renpy.pause(2.5, hard=True)
    hide screen trl_quote
    show screen trl_quote(_("Tu penses que je deviens fou ?"), _("NOAM"), "#F2F8FF")
    $ renpy.pause(2.3, hard=True)
    hide screen trl_quote

    # 12–18 | Conclave et soupçon. Le premier avertissement de Kami.
    play trl_a "audio/trailer/trl_glitch_stutter.wav"
    scene bg_diffusion_taquin at trl_unstable(5, 1.04)
    with trl_flash
    show screen trl_title(
        _("VOUS VOULIEZ"), _("RENTRER CHEZ VOUS ?"),
        kicker=_("JOUR 20 — LE DÉBUT DE LA FIN"), accent="#F77991", slam=True
    )
    $ renpy.pause(2.5, hard=True)
    hide screen trl_title
    scene bg_cg030 at trl_snap(1.18, 1.03, 1.0)
    with trl_hardcut
    $ renpy.pause(2.4, hard=True)

    # 18–27 | Choc : images du scénario et montée en puissance des sons.
    play music "audio/music/bgm_horror_pulse.mp3" fadein 0.45
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene bg_salle_goumi_cachee at trl_push(4.0, 1.01, 1.14)
    with trl_flash_red
    show screen trl_quote(_("Pose ce couteau, Noam."), _("IRIS"), "#FFB6C5")
    $ renpy.pause(2.6, hard=True)
    hide screen trl_quote
    play trl_a "audio/trailer/trl_heartbeat.wav"
    scene bg_cg052 at trl_snap(1.12, 1.02, 0.96)
    with trl_blink
    $ renpy.pause(1.0, hard=True)
    scene black
    with trl_cut
    $ renpy.pause(0.6, hard=True)
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene bg_cg053 at trl_snap(1.15, 1.08, 0.91)
    with trl_flash_red
    $ renpy.pause(1.2, hard=True)
    scene black
    with trl_hardcut
    show screen trl_title(
        _("QUELQU'UN MENT."), _("MAIS QUI ?"),
        kicker=_("DANS LES COULOIRS DU CONCLAVE"), accent="#FA6B85", danger=True
    )
    $ renpy.pause(2.2, hard=True)
    hide screen trl_title

    # 27–37 | Scènes réellement tirées des jours DLC 25–26, sans révélation.
    play trl_b "audio/trailer/trl_swoosh.wav"
    scene bg_maintenance at trl_memory(-1, 0.17)
    with trl_hardcut
    show screen trl_quote(_("Il nous faut une preuve. Pas une autre hypothèse."), _("NOAM"), "#E5F6FF")
    $ renpy.pause(2.4, hard=True)
    hide screen trl_quote
    scene bg_cafeteria at trl_unstable(5, 1.04)
    with trl_hardcut
    show screen trl_quote(_("Depuis quelques jours, t'as l'air de prendre peur dès que je m'approche."), _("MARA"), "#FFB2BD")
    $ renpy.pause(2.8, hard=True)
    hide screen trl_quote
    play trl_a "audio/trailer/trl_data_burst.wav"
    scene bg_diffusion_colere at trl_snap(1.12, 1.01, 0.9)
    with trl_blink
    $ renpy.pause(0.65, hard=True)
    scene black with trl_cut
    $ renpy.pause(0.35, hard=True)
    scene bg_conduit_reseau at trl_push(4.0, 1.01, 1.18)
    with trl_hardcut
    show screen trl_quote(_("On peut pas continuer à garder ça pour nous."), _("NOAM"), "#DFEEF7")
    $ renpy.pause(2.5, hard=True)
    hide screen trl_quote

    # 37–48 | Aperçus de visuels payants seulement lorsque le DLC est installé.
    # L'édition gratuite utilise des scènes communes : trailer autonome et sans fuite d'asset.
    play trl_b "audio/trailer/trl_reverse_swell.wav"
    if kd_dlc_unlocked("doppelganger_routes"):
        scene bg_cg060 at trl_memory(1, 0.18)
    else:
        scene bg_observation at trl_memory(1, 0.18)
    with trl_flash
    $ renpy.pause(1.1, hard=True)
    scene black with trl_cut
    $ renpy.pause(0.45, hard=True)
    if kd_dlc_unlocked("doppelganger_routes"):
        scene bg_cg066 at trl_snap(1.17, 1.01, 0.91)
    else:
        scene bg_salle_goumi_cachee at trl_snap(1.17, 1.01, 0.91)
    with trl_flash_red
    $ renpy.pause(1.15, hard=True)
    scene black with trl_hardcut
    show screen trl_quote(_("Je vais pas te mentir : j'ai envie de partir."), _("UNE VOIX FAMILIÈRE"), "#E6C9D8")
    $ renpy.pause(2.4, hard=True)
    hide screen trl_quote
    play trl_a "audio/trailer/trl_impact_deep.wav"
    show screen trl_title(
        _("UNE STATION."), _("PLUSIEURS VÉRITÉS."),
        kicker=_("DE NOUVEAUX CHOIX · DE NOUVELLES FINS"), accent="#83D7E7"
    )
    $ renpy.pause(2.6, hard=True)
    hide screen trl_title

    # 48–61 | Dernier battement, silence, carton final.
    stop music fadeout 1.6
    stop trl_amb fadeout 1.3
    play trl_a "audio/trailer/trl_heartbeat.wav"
    scene bg_observation at trl_pull(5.0, 1.08, 1.01)
    with trl_soft
    show screen trl_quote(_("Noam... tu sais vraiment à qui tu parles ?"), _("???"), "#FFFFFF")
    $ renpy.pause(3.1, hard=True)
    hide screen trl_quote
    scene black with trl_cut
    $ renpy.pause(1.3, hard=True)
    play trl_b "audio/trailer/trl_final_hit.wav"
    show screen trl_endcard(
        _("KAMI'S DESIRES : L'ANGLE MORT"),
        _("UNE HISTOIRE QUE VOUS N'AVEZ PAS ENCORE VUE"),
        note=_("UNE FIN GRATUITE. LES AUTRES CHOIX DANS LE DLC.")
    )
    $ renpy.pause(4.4, hard=True)
    hide screen trl_endcard
    scene black with Dissolve(0.65)
    $ renpy.pause(0.6, hard=True)
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
