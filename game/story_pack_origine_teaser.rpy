# L'Origine — in-engine cinematic teaser (~30 seconds).
# Uses existing CG/music from the game. Not a pre-rendered MP4.
label origine_story_pack_teaser:
    window hide
    stop music fadeout 0.3
    play music "music/bgm_system_override.mp3" fadein 0.3

    scene black
    show text "{size=76}{color=#FFFFFF}KAMI'S DESIRES{/color}{/size}" at truecenter
    with Dissolve(0.25)
    pause 2.7

    scene bg_conclave at adaptive_fullscreen
    show text "{size=75}{color=#FFFFFF}LE CONCLAVE N'A PAS LIVRÉ TOUS SES SECRETS{/color}{/size}" at truecenter
    with Dissolve(0.2)
    pause 2.7

    scene bg_cg014 at adaptive_fullscreen
    show text "{size=94}{color=#FFFFFF}JOURS 5 À 30{/color}{/size}" at truecenter
    with Dissolve(0.2)
    pause 2.7

    scene bg_cg030 at adaptive_fullscreen
    show text "{size=96}{color=#FFFFFF}7 FINS DIFFÉRENTES{/color}{/size}" at truecenter
    with Dissolve(0.2)
    pause 2.7

    scene bg_conclave at adaptive_fullscreen
    show text "{size=88}{color=#FF5F72}DES COMBATS{/color}{/size}" at truecenter
    with vpunch
    pause 2.7

    scene bg_salle_goumi_cachee at adaptive_fullscreen
    show text "{size=88}{color=#FFFFFF}DES DISPUTES{/color}{/size}" at truecenter
    with hpunch
    pause 2.7

    scene bg_cg040 at adaptive_fullscreen
    show text "{size=88}{color=#FF5F72}DES TRAHISONS{/color}{/size}" at truecenter
    with vpunch
    pause 2.7

    scene bg_conduit_reseau at adaptive_fullscreen
    show text "{size=72}{color=#FFFFFF}QUI PEUT ENCORE ÊTRE CRU ?{/color}{/size}" at truecenter
    with Dissolve(0.2)
    pause 2.7

    scene bg_cg070 at adaptive_fullscreen
    show text "{size=73}{color=#FFFFFF}DÉCOUVREZ UNE DES VÉRITÉS CACHÉES{/color}{/size}" at truecenter
    with vpunch
    pause 2.7

    scene black
    show text "{size=100}{color=#FFFFFF}L'ORIGINE{/color}{/size}\n{size=37}{color=#61D3E9}STORY PACK 01  •  JOURS 5–30  •  7 FINS{/color}{/size}" at truecenter
    with Dissolve(0.3)
    pause 3.0
    stop music fadeout 0.5
    return
