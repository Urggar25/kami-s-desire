# Noam — cut-in d'interruption. Durée fixe : 2,00 secondes.
# Les images du corps et des yeux doivent partager le même canevas de dessin.
# Déclencheur public : call play_noam_interupt

# Transition générale : sortie rapide pendant les 0,25 dernières secondes.
transform noam_interupt_exit:
    alpha 1.0
    pause 1.74
    easein 0.26 alpha 0.0

# Fond : fondu d'entrée sans mouvement.
transform noam_interupt_bg_fade:
    alpha 0.0
    linear 0.38 alpha 1.0

# Une seule transformation commune au corps ET aux deux calques d'yeux :
# entrée depuis le bas, léger overshoot, recul élastique et micro-impact.
transform noam_interupt_rise:
    subpixel True
    yoffset 900
    zoom 1.0
    pause 0.50
    easeout 0.20 yoffset -24 zoom 1.055
    linear 0.035 xoffset -7
    linear 0.035 xoffset 6
    easeout 0.14 xoffset 0 yoffset 0 zoom 1.0

# Clignement unique, bref, optionnel (garder le regard fixe en passant False).
transform noam_interupt_eyes_open:
    alpha 1.0
    pause 1.18
    alpha 0.0
    pause 0.10
    alpha 1.0

transform noam_interupt_eyes_closed:
    alpha 0.0
    pause 1.18
    alpha 1.0
    pause 0.10
    alpha 0.0

screen noam_interupt_screen(blink=True):
    modal True
    zorder 300

    fixed at noam_interupt_exit:
        xfill True
        yfill True

        add "images/character/noam/interupt_background.png" at noam_interupt_bg_fade:
            xalign 0.5
            yalign 0.5

        fixed at noam_interupt_rise:
            xfill True
            yfill True
            add "images/character/noam/interupt_body.png":
                xalign 0.5
                yalign 0.5
            if blink:
                add "images/character/noam/interupt_yeux_ouvert.png" at noam_interupt_eyes_open:
                    xalign 0.5
                    yalign 0.5
                add "images/character/noam/interupt_yeux_ferme.png" at noam_interupt_eyes_closed:
                    xalign 0.5
                    yalign 0.5
            else:
                add "images/character/noam/interupt_yeux_ouvert.png":
                    xalign 0.5
                    yalign 0.5

    # Les effets utilisent le canal sound du jeu ; le chronométrage reste
    # entièrement piloté par cet écran, sans attente entre deux sons.
    timer 0.70 action Play("sound", "audio/sfx_interrupt_impact.wav")
    timer 1.70 action Play("sound", "audio/sfx_interrupt_outro.wav")
    timer 2.00 action Return()

label play_noam_interupt(blink=True):
    play sound "audio/sfx_interrupt_intro.wav"
    call screen noam_interupt_screen(blink=blink)
    return


# ---------------------------------------------------------------------------
# JOUR 1 — RÉFUTATION : Lysa / radio de la salle d'observation.
# Moteur générique : game/minijeu/refutation.rpy. Cinq affirmations défilent,
# chacune avec une faille cliquable ; seule « aucune règle » (affirmation 4)
# tombe sous le fragment « Règlement du Conclave ». Trois erreurs maximum.
# Le cut-in animé de Noam reste la récompense d'une réfutation réussie.
# ---------------------------------------------------------------------------

init python:
    DAY1_RADIO_TARGET_LINE = 3

    def day1_radio_miss_reason(argument_id, line_index, fault_index=0):
        if argument_id == "reglement_conclave":
            return _("« Attends au moins que je termine ma phrase ! »")
        if line_index == DAY1_RADIO_TARGET_LINE:
            return _("« Tu me contredis avec ça ? Quel rapport ?! »")
        return _("« Ça n'explique toujours pas pourquoi l'appel échoue ! »")

    refutation_register(
        "j1_radio",
        title=_("RADIO BLOQUÉE"),
        bg="bg_observation",
        statements=[
            ("lysa", "determine", _("Cette radio fonctionne, j'en suis sûre. Je vais trouver [[comment l'utiliser]].")),
            ("lysa", "reflexion", _("Kami a dit que [[les Dix Commandements]] ne s'appliquaient pas dans le Conclave.")),
            ("lysa", "colere", _("J'ai essayé plusieurs fréquences. [[Le signal existe]], c'est juste l'appel qui est bloqué.")),
            ("lysa", "opposition", _("Il n'y a [[aucune règle]] qui nous interdit de contacter quelqu'un à l'extérieur !")),
            ("lysa", "fatigue", _("Je vais essayer encore une fois. Il doit bien y avoir [[un moyen]] de joindre ma sœur.")),
        ],
        fragments=[
            ("reglement_conclave", _("Règlement du Conclave")),
            ("commandements", _("Les 10 Commandements")),
            ("surveillance", _("La surveillance de Kami")),
            ("vote_secret", _("Le secret des votes")),
            ("securite", _("La sécurité de la station")),
        ],
        solution={(DAY1_RADIO_TARGET_LINE, 0): "reglement_conclave"},
        miss=day1_radio_miss_reason,
        lives=3,
        line_time=5.5,
    )


label day1_noam_radio_interruption:
    call refutation_run("j1_radio") from _call_refutation_run_j1_radio
    $ _day1_radio_shot = _return
    if _day1_radio_shot[0] == "success":
        # Le cut-in de Noam surgit SEULEMENT quand le joueur trouve
        # la bonne faille et y injecte le bon fragment.
        call play_noam_interupt(blink=True) from _call_day1_radio_noam_interupt_success
    return _day1_radio_shot
