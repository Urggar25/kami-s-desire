# Introduction narrative — Les Sept Questions de Kami.

label seven_questions_kami_intro:

    stop music fadeout 0.5
    play sound sfx_gresillement
    pause 0.35

    voix "Diffusion centrale active."

    play music "music/bgm_system_override.mp3" fadein 0.6
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    kami "[sq_intro_line(0)]"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(1)]"
    kami "[sq_intro_line(2)]"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(3)]"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(4)]"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(5)]"

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(6)]"

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(7)]"
    kami "[sq_intro_line(8)]"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(9)]"

    scene bg_diffusion_desespoir at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(10)]"

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(11)]"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(12)]"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(13)]"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "[sq_intro_line(14)]"

    pause 0.4
    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene black with fade

    $ sq_complete_intro()
    return

