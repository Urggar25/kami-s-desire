# ============================================================
# BANDE-ANNONCE OFFICIELLE — VERSION 2.1
# « LES LIGNES QUI NOUS SÉPARENT »
# ------------------------------------------------------------
# Cinématique autonome lancée depuis le bouton VERSION du menu
# principal. Elle ne lit ni n'écrit aucune variable de progression.
# Boîte à outils (transforms, styles, screens, vitrines de
# mini-jeux) : version_2_1_trailer_kit.rpy
# Kit sonore synthétisé : tools/generate_trailer_sfx.py
#                         -> game/audio/trailer/*.wav
#
# PARTIS PRIS DE MONTAGE
#   · Attaque directe : aucun logo, aucun carton d'archive avant
#     le premier plan. Le splashscreen du jeu est court-circuité.
#   · Aucune notion de « jour » à l'écran : le chapitre se lit
#     comme un seul mouvement, pas comme un agenda.
#   · Rythme croissant : les plans passent d'environ 4 s au début
#     à moins d'une seconde dans les rafales du climax.
#   · Chaque coupe forte est portée par un son : riser avant,
#     impact sur la coupe, drone dessous.
#
# ARC — quatre mouvements, intensité strictement croissante
#   I    LA PROMESSE        froid, large, presque calme
#   II   LE JEU             règles, mini-jeux, premier vote
#   III  LE PRIX            le monde encaisse, la fracture
#   IV   LA MACHINE DÉRAILLE  glitch, menace, effroi
#   V    TITRE              logo + épilogue inquiétant
#
# Le paramètre `heat` de trl_grade suit : 0.06 → 0.28 → 0.60 → 0.9 → 1.0
# ============================================================


init python:
    import random as _trl_random
    from functools import partial as _trl_partial

    def _trl_shake_func(trans, st, at, intensity=12, duration=0.32):
        """Secousse amortie appliquée au layer master (le décor)."""
        if st > duration:
            trans.xoffset = 0
            trans.yoffset = 0
            return None
        damp = 1.0 - (st / duration)
        trans.xoffset = int(_trl_random.uniform(-intensity, intensity) * damp)
        trans.yoffset = int(_trl_random.uniform(-intensity, intensity) * damp * 0.6)
        return 0.0

    def trl_shake(intensity=12, duration=0.32):
        tr = Transform(function=_trl_partial(_trl_shake_func, intensity=intensity, duration=duration))
        renpy.show_layer_at([tr], layer="master")
        renpy.pause(duration, hard=True)
        renpy.show_layer_at([], layer="master")

    def trl_shake_clear():
        renpy.show_layer_at([], layer="master")


# ------------------------------------------------------------
# Gestes de monteur. Un label par geste : la timeline plus bas
# reste lisible comme une feuille de montage.
# ------------------------------------------------------------
label trl_say(line, who, accent="#5CD3FF", tag=None):
    hide screen trl_quote
    show screen trl_quote(line, who, accent, tag)
    return


label trl_clear:
    hide screen trl_quote
    hide screen trl_title
    hide screen trl_shout
    return


# ============================================================
#                        MONTAGE
# ============================================================
label version_2_1_trailer:

    # Le trailer est entièrement localisé en anglais. Tant qu'une autre
    # langue ne possède pas sa propre traduction complète du trailer, on
    # l'affiche en anglais puis on restaure la langue du jeu à la sortie.
    $ _trl_original_language = preferences.language
    if _trl_original_language not in (None, "english"):
        $ renpy.change_language("english")
    $ trl_refresh_localized_data()

    $ _game_menu_screen = None
    $ quick_menu = False
    $ renpy.block_rollback()
    $ trl_shake_clear()

    scene black
    stop music fadeout 0.4
    stop sound fadeout 0.2

    show screen trl_controls
    show screen trl_letterbox(88)
    show screen trl_grade(0.06)


    # ========================================================
    # I — LA PROMESSE
    # Attaque directe. Trois cartons, aucun préambule.
    # ========================================================

    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 0.8
    play trl_a "audio/trailer/trl_reverse_swell.wav"
    $ renpy.pause(1.1, hard=True)

    # Plan d'ouverture : la Terre vue de la station. Large, froid, muet.
    play trl_b "audio/trailer/trl_impact_deep.wav"
    show screen trl_title(
        _("ILS ONT CONFIÉ LE MONDE"),
        _("À UNE MACHINE."),
        bg="gui/main_menu_kami/bg_conclave_hub.png",
        bg_alpha=0.68
    )
    $ renpy.pause(2.9, hard=True)
    hide screen trl_title

    # Puis son visage, parfaitement serein. C'est là que ça glace.
    play trl_a "audio/trailer/trl_sub_drop.wav"
    scene black
    with trl_cut
    show screen trl_title(
        _("ELLE A TENU"),
        _("SA PROMESSE."),
        bg="images/background/kami_diffusion/bg_diffusion_zen.png",
        bg_alpha=0.40
    )
    $ renpy.pause(2.4, hard=True)
    hide screen trl_title

    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene black
    with trl_blink
    $ renpy.pause(0.55, hard=True)


    # ========================================================
    # II — LE JEU
    # On installe les règles et on montre qu'on JOUE.
    # ========================================================

    show screen trl_grade(0.28)
    play music "audio/music/bgm_cold_metadata.mp3" fadein 1.2
    stop trl_amb fadeout 1.2

    play trl_a "audio/trailer/trl_data_burst.wav"
    scene expression "images/background/scene/conclave1.png" at trl_push(5.5, 1.02, 1.12, 0.42, 0.50)
    with trl_slowfade
    call trl_say(_("Bienvenue au Conclave."), _("KAMI")) from _trl_s01
    $ renpy.pause(3.4, hard=True)

    play trl_a "audio/sfx_paper.mp3"
    hide screen trl_quote
    scene expression "images/background/cg/bg_cg009.png" at trl_push(4.6, 1.02, 1.11, 0.56, 0.51)
    with trl_soft
    call trl_say(_("Chacun de vous proposera une modification des règles du monde. Un seul amendement."), _("KAMI")) from _trl_s02
    $ renpy.pause(3.8, hard=True)

    call trl_clear from _trl_c01
    play trl_b "audio/trailer/trl_riser_short.wav"
    scene black
    with trl_cut
    show screen trl_title(
        _("DOUZE INCONNUS."),
        _("LES RÈGLES DU MONDE ENTRE LEURS MAINS."),
        kicker=_("LE CONCLAVE")
    )
    $ renpy.pause(2.0, hard=True)
    play trl_a "audio/trailer/trl_impact_deep.wav"
    $ renpy.pause(0.9, hard=True)
    hide screen trl_title

    play trl_b "audio/trailer/trl_swoosh.wav"
    scene black
    with trl_cut
    show screen trl_title(
        _("IL FAUT L'UNANIMITÉ."),
        _("UNE SEULE VOIX SUFFIT À TOUT BLOQUER."),
        accent="#FFD166",
        slam=True
    )
    $ renpy.pause(2.8, hard=True)
    hide screen trl_title

    # --- Vitrine : rédaction d'amendement -------------------
    play trl_a "audio/sfx_paper.mp3"
    scene black
    with trl_hardcut
    show screen trl_mg_amendement
    $ renpy.pause(3.8, hard=True)
    hide screen trl_mg_amendement

    # --- Vitrine : synchronisation motrice ------------------
    play trl_a "audio/sfx_minigame_start.mp3"
    play trl_b "audio/trailer/trl_tick.wav"
    scene black
    with trl_hardcut
    show screen trl_mg_trace
    $ renpy.pause(3.6, hard=True)
    hide screen trl_mg_trace

    # --- Un peu d'air : le seul sourire du trailer ----------
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene expression "images/background/cg/bg_cg013.png" at trl_push(4.0, 1.03, 1.10, 0.46, 0.48)
    with trl_soft
    call trl_say(
        _("Ici, on crève d'ennui. Alors je m'autorise à oublier la peur. Juste pour un bol."),
        _("ELEN"),
        "#9BE3A8"
    ) from _trl_s03
    $ renpy.pause(3.4, hard=True)

    hide screen trl_quote
    scene expression "images/background/cg/bg_cg010.png" at trl_pull(3.8, 1.10, 1.01)
    with trl_soft
    call trl_say(
        _("Ici, tout le monde protège quelqu'un… ou quelque chose."),
        _("NYRA"),
        "#C7B7F5"
    ) from _trl_s04
    $ renpy.pause(3.4, hard=True)

    hide screen trl_quote
    scene expression "images/background/cg/bg_cg014.png" at trl_push(3.8, 1.04, 1.11, 0.50, 0.46)
    with trl_soft
    call trl_say(
        _("On a tous peur. Mais vouloir que rien ne bouge, c'est un choix aussi. Et il tue, juste plus lentement."),
        _("NOAM")
    ) from _trl_s05
    $ renpy.pause(4.0, hard=True)


    # ========================================================
    # III — LE PRIX
    # Le débat, l'objection, le vote. Puis le monde encaisse.
    # ========================================================

    call trl_clear from _trl_c02
    show screen trl_grade(0.60)
    stop music fadeout 0.6
    play trl_a "audio/trailer/trl_riser.wav"

    scene black
    with trl_cut
    show screen trl_title(
        _("PUIS IL FAUT"),
        _("SE METTRE D'ACCORD."),
        kicker=_("LE DÉBAT"),
        slam=True
    )
    $ renpy.pause(2.4, hard=True)
    play trl_b "audio/trailer/trl_braam.wav"
    play music "audio/music/bgm_fatal_assembly.mp3" fadein 0.5
    $ renpy.pause(0.6, hard=True)
    hide screen trl_title

    # --- Vitrine : Fatal Assembly ---------------------------
    scene black
    with trl_hardcut
    show screen trl_mg_fatal
    $ renpy.pause(3.9, hard=True)
    hide screen trl_mg_fatal

    # --- L'objection : la frappe la plus forte du trailer ---
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene expression "images/background/debat/fatal_assembly_2.png" at trl_snap(1.35, 1.06, 0.7)
    with trl_flash
    $ renpy.pause(0.22, hard=True)

    play trl_a "audio/sfx_exclamation.mp3"
    play trl_b "audio/trailer/trl_impact_deep.wav"
    scene expression "images/background/debat/noam_objection.png" at trl_snap(1.25, 1.02, 1.4)
    with trl_hardcut
    $ trl_shake(22, 0.40)
    $ renpy.pause(1.3, hard=True)

    # --- Vitrine : Objection Fracturée ----------------------
    play trl_a "audio/sfx_minigame_start.mp3"
    scene black
    with trl_hardcut
    show screen trl_mg_objection
    $ renpy.pause(4.2, hard=True)
    hide screen trl_mg_objection

    # --- Le vote, puis le verdict ---------------------------
    play trl_a "audio/trailer/trl_riser_short.wav"
    scene black
    with trl_hardcut
    show screen trl_mg_vote
    $ renpy.pause(2.9, hard=True)

    play trl_a "audio/sfx_vote_contre.wav"
    play trl_b "audio/trailer/trl_final_hit.wav"
    show screen trl_mg_verdict
    $ trl_shake(18, 0.36)
    $ renpy.pause(2.2, hard=True)
    hide screen trl_mg_verdict
    hide screen trl_mg_vote

    play trl_a "audio/trailer/trl_string_tension.wav"
    scene black
    with trl_cut
    show screen trl_title(
        _("CONVAINCRE"),
        _("EST PLUS DIFFICILE QUE CONTRAINDRE."),
        accent="#FFD166"
    )
    $ renpy.pause(2.9, hard=True)
    hide screen trl_title

    # --- Dehors, quelqu'un paie -----------------------------
    stop music fadeout 1.0
    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 1.0

    scene expression "images/background/cg/bg_cg034.png" at trl_push(6.0, 1.03, 1.13, 0.55, 0.52)
    with trl_slowfade
    call trl_say(
        _("Pendant que nous votons, des milliers de vies restent suspendues à notre décision."),
        _("LYSA"),
        "#FF8A96"
    ) from _trl_s06
    $ renpy.pause(4.2, hard=True)

    play music "audio/music/bgm_low_tension.mp3" fadein 1.0
    stop trl_amb fadeout 1.2

    hide screen trl_quote
    play trl_a "audio/trailer/trl_swoosh.wav"
    scene expression "images/background/cg/bg_cg022.png" at trl_push(3.6, 1.05, 1.12, 0.48, 0.50)
    with trl_soft
    call trl_say(
        _("On nous enferme, on nous filme, on nous fait jouer les réformateurs sous peine de mort."),
        _("LYSA"),
        "#FF8A96"
    ) from _trl_s07
    $ renpy.pause(3.8, hard=True)

    hide screen trl_quote
    play trl_a "audio/trailer/trl_sub_drop.wav"
    scene expression "images/background/cg/bg_cg022.png" at trl_snap(1.24, 1.05, 1.1)
    with trl_hardcut
    call trl_say(
        _("J'en ai ras le cul de ramasser des cadavres. La frontière, je la connais. Je la garde."),
        _("RYN"),
        "#FF8A96"
    ) from _trl_s08
    $ renpy.pause(3.6, hard=True)

    # --- L'accident -----------------------------------------
    call trl_clear from _trl_c03
    play trl_a "audio/sfx_metal_clank.mp3"
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene expression "images/background/cg/bg_cg027.png" at trl_snap(1.30, 1.06, 1.6)
    with trl_flash_red
    $ trl_shake(20, 0.40)
    call trl_say(
        _("Si ça tourne mal, c'est nous qui payons. Pas Kami. Nous."),
        _("MARA"),
        "#FF8A96"
    ) from _trl_s09
    $ renpy.pause(3.4, hard=True)

    hide screen trl_quote
    scene expression "images/background/cg/bg_cg028.png" at trl_push(3.6, 1.04, 1.11, 0.48, 0.52)
    with trl_soft
    call trl_say(
        _("Arrêter les guerres n'était qu'un prétexte parfait pour prendre les pleins pouvoirs."),
        _("NOAM")
    ) from _trl_s10
    $ renpy.pause(3.8, hard=True)

    # --- Respiration émotionnelle avant la chute ------------
    call trl_clear from _trl_c04
    stop music fadeout 1.2
    play trl_a "audio/trailer/trl_string_tension.wav"
    scene expression "images/background/cg/bg_cg029.png" at trl_pull(4.6, 1.10, 1.00)
    with trl_slowfade
    call trl_say(
        _("Je me demande si nos familles nous regardent, en ce moment."),
        _("ELEN"),
        "#9BE3A8"
    ) from _trl_s11
    $ renpy.pause(4.0, hard=True)


    # ========================================================
    # IV — LA MACHINE DÉRAILLE
    # À partir d'ici, plus rien n'est rassurant et plus rien
    # ne tient en place. Les plans se raccourcissent.
    # ========================================================

    call trl_clear from _trl_c05
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene black
    with trl_blink
    $ renpy.pause(0.4, hard=True)

    show screen trl_grade(0.90)
    play music "audio/music/bgm_system_override.mp3" fadein 0.3
    play trl_a "audio/trailer/trl_alarm_low.wav"

    show screen trl_title(
        _("PUIS LE SIGNAL"),
        _("A CHANGÉ."),
        accent="#FF3A5C",
        danger=True
    )
    $ renpy.pause(2.5, hard=True)
    hide screen trl_title

    # --- Kami se fissure ------------------------------------
    play trl_a "audio/sfx_gresillement.mp3"
    scene expression "images/background/kami_diffusion/bg_diffusion_colere.png" at trl_unstable(6, 1.08)
    with trl_hardcut
    call trl_say(
        _("Vous me semblez, bi-bien moins intéressants que ces derniers jours. C'est très contrariant."),
        _("KAMI"),
        "#FF5E6E",
        _("SIGNAL DÉGRADÉ")
    ) from _trl_s12
    $ renpy.pause(3.8, hard=True)

    hide screen trl_quote
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene expression "images/background/kami_diffusion/bg_diffusion_desespoir.png" at trl_unstable(9, 1.10)
    with trl_hardcut
    call trl_say(
        _("Les jouets se cassent toujours plus vite une fois qu'on commence à jouer sérieusement avec eux."),
        _("KAMI"),
        "#FF5E6E"
    ) from _trl_s13
    $ renpy.pause(3.8, hard=True)

    # --- Vitrine : Signal Instable --------------------------
    call trl_clear from _trl_c06
    play trl_a "audio/sfx_kami_alert.wav"
    scene black
    with trl_hardcut
    show screen trl_mg_signal
    $ renpy.pause(3.6, hard=True)
    hide screen trl_mg_signal

    # --- Staccato : l'ordre répété --------------------------
    play trl_a "audio/trailer/trl_tick.wav"
    scene black
    with trl_hardcut
    show screen trl_shout(_("MAINTENEZ."), "#48F5FF", 170)
    $ renpy.pause(0.58, hard=True)
    hide screen trl_shout

    play trl_b "audio/trailer/trl_tick.wav"
    show screen trl_shout(_("LE."), "#48F5FF", 170)
    $ renpy.pause(0.46, hard=True)
    hide screen trl_shout

    play trl_a "audio/trailer/trl_impact_deep.wav"
    show screen trl_shout(_("SIGNAL."), "#FF3A5C", 195)
    $ trl_shake(16, 0.30)
    $ renpy.pause(0.75, hard=True)
    hide screen trl_shout

    # --- Vitrine : Fracture ---------------------------------
    scene black
    with trl_hardcut
    show screen trl_mg_fracture
    $ renpy.pause(3.4, hard=True)
    hide screen trl_mg_fracture

    # --- Le lapsus ------------------------------------------
    play trl_a "audio/trailer/trl_riser_short.wav"
    scene expression "images/background/kami_diffusion/bg_diffusion_colere.png" at trl_unstable(14, 1.12)
    with trl_flash_red
    call trl_say(
        _("Puisque vous refusez de débattre… il est temps maintenant de mour—"),
        _("KAMI"),
        "#FF3A5C",
        _("ERREUR // CORRECTION EN COURS")
    ) from _trl_s14
    $ renpy.pause(2.5, hard=True)

    play trl_a "audio/trailer/trl_impact_deep.wav"
    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    hide screen trl_quote
    scene black
    with trl_hardcut
    show screen trl_shout(_("VOTER."), "#FF3A5C", 205)
    $ trl_shake(24, 0.42)
    $ renpy.pause(0.85, hard=True)
    hide screen trl_shout

    scene expression "images/background/kami_diffusion/bg_diffusion_colere.png" at trl_unstable(4, 1.06)
    with trl_hardcut
    call trl_say(_("Pardon. Correction effectuée."), _("KAMI"), "#FF3A5C") from _trl_s15
    $ renpy.pause(2.2, hard=True)

    call trl_clear from _trl_c07
    play trl_a "audio/trailer/trl_heartbeat.wav"
    scene expression "images/background/cg/cg007.png" at trl_snap(1.32, 1.08, 2.0)
    with trl_hardcut
    $ trl_shake(18, 0.36)
    call trl_say(_("Moi, j'ai entendu « mourir »."), _("MARA"), "#FF3A5C") from _trl_s16
    $ renpy.pause(2.9, hard=True)

    # --- Rafale : tout se désagrège -------------------------
    call trl_clear from _trl_c08
    play trl_a "audio/trailer/trl_riser_long.wav"

    scene expression "images/background/kami_diffusion/bg_diffusion_colere.png" at trl_memory(1, 0.16)
    with trl_hardcut
    $ renpy.pause(0.34, hard=True)
    scene expression "images/background/cg/bg_cg027.png" at trl_memory(-1, 0.16)
    with trl_hardcut
    $ renpy.pause(0.30, hard=True)
    play trl_b "audio/trailer/trl_tick.wav"
    scene expression "images/background/debat/noam_objection.png" at trl_memory(1, 0.14)
    with trl_hardcut
    $ renpy.pause(0.26, hard=True)
    scene expression "images/background/cg/bg_cg022.png" at trl_memory(-1, 0.14)
    with trl_hardcut
    $ renpy.pause(0.24, hard=True)
    play trl_b "audio/trailer/trl_tick.wav"
    scene expression "images/background/cg/cg007.png" at trl_memory(1, 0.12)
    with trl_hardcut
    $ renpy.pause(0.22, hard=True)
    scene expression "images/background/cg/bg_cg034.png" at trl_memory(-1, 0.12)
    with trl_hardcut
    $ renpy.pause(0.20, hard=True)
    scene expression "images/background/kami_diffusion/bg_diffusion_colere.png" at trl_memory(1, 0.10)
    with trl_hardcut
    $ renpy.pause(0.18, hard=True)

    # --- Le plan qui fait basculer le trailer ---------------
    play trl_a "audio/sfx_exclamation_horror.mp3"
    stop music fadeout 1.6
    show screen trl_grade(1.0)

    scene black
    with trl_cut
    $ renpy.pause(0.5, hard=True)

    play trl_amb "audio/trailer/trl_whisper_drone.wav" fadein 1.8
    play trl_b "audio/trailer/trl_string_tension.wav"
    scene expression "images/background/cg/bg_cg035.png" at trl_push(10.0, 1.02, 1.12, 0.50, 0.44)
    with Dissolve(1.5)
    $ renpy.pause(2.9, hard=True)

    call trl_say(_("Ce n'est pas une frontière."), _("NOAM"), "#FF5E6E") from _trl_s17
    $ renpy.pause(2.5, hard=True)

    hide screen trl_quote
    call trl_say(
        _("C'est une prison. Et nous venons de voter pour qu'elle reste fermée."),
        _("NOAM"),
        "#FF3A5C"
    ) from _trl_s18
    $ renpy.pause(4.0, hard=True)

    call trl_clear from _trl_c09
    $ renpy.pause(1.3, hard=True)


    # ========================================================
    # V — TITRE
    # ========================================================

    play trl_b "audio/trailer/trl_glitch_stutter.wav"
    scene black
    with trl_blink
    $ renpy.pause(0.4, hard=True)

    play trl_a "audio/trailer/trl_final_hit.wav"
    stop trl_amb fadeout 0.8
    scene black
    with trl_flash

    # Le logo se lit sur une image propre : on redescend le traitement
    # pour que les déchirures du climax ne barrent pas le lettrage.
    show screen trl_grade(0.30)

    show screen trl_endcard(
        _("CHAPITRE 2 — LES LIGNES QUI NOUS SÉPARENT"),
        _("VERSION 2.1 DISPONIBLE"),
        note=_("VISUAL NOVEL  ·  DÉBATS  ·  VOTES  ·  MINI-JEUX  ·  CHOIX IRRÉVERSIBLES")
    )
    $ renpy.pause(5.0, hard=True)
    hide screen trl_endcard

    # --- Dernier frisson ------------------------------------
    hide screen trl_grade
    scene black
    with trl_cut
    play trl_a "audio/trailer/trl_heartbeat.wav"

    show screen trl_epilogue(
        _("LE CONCLAVE DURERA TRENTE JOURS."),
        _("IL EN RESTE VINGT-QUATRE."),
        delay2=1.9
    )
    $ renpy.pause(4.2, hard=True)
    hide screen trl_epilogue

    play trl_b "audio/sfx_kami_alert.wav"
    play trl_a "audio/trailer/trl_sub_drop.wav"
    scene black
    with trl_hardcut
    show screen trl_shout(_("ELLE VOUS REGARDE."), "#48F5FF", 120)
    $ renpy.pause(1.4, hard=True)
    hide screen trl_shout

    scene black
    with Dissolve(0.7)
    $ renpy.pause(1.0, hard=True)

    jump version_2_1_trailer_end


# ============================================================
# SORTIE — atteinte par la fin naturelle, par ÉCHAP ou par le
# bouton PASSER. Nettoie tout et rend la main au menu.
# ============================================================
label version_2_1_trailer_end:

    hide screen trl_quote
    hide screen trl_title
    hide screen trl_shout
    hide screen trl_endcard
    hide screen trl_epilogue
    hide screen trl_mg_trace
    hide screen trl_mg_amendement
    hide screen trl_mg_fatal
    hide screen trl_mg_objection
    hide screen trl_mg_vote
    hide screen trl_mg_verdict
    hide screen trl_mg_signal
    hide screen trl_mg_fracture
    hide screen trl_grade
    hide screen trl_letterbox
    hide screen trl_controls

    $ trl_shake_clear()

    stop trl_a fadeout 0.3
    stop trl_b fadeout 0.3
    stop trl_amb fadeout 0.6
    stop sound fadeout 0.3
    stop music fadeout 0.8

    if preferences.language != _trl_original_language:
        $ renpy.change_language(_trl_original_language)

    scene black
    with Dissolve(0.4)
    return
