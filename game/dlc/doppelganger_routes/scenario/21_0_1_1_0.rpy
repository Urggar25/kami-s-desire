# =============================================================================
# JOUR 21 — Route 0_1_1
# =============================================================================


label _21_0_1_1_LEAVE_REVEIL:
    # Entrée J21 après la réponse "je monte dans la navette".
    # Cette branche conserve pour l'instant le J21 existant.
    $ j20_kael_depart_choice = "leave"
    jump _21_0_1_1_0_REVEIL


label _21_0_1_1_STAY_REVEIL:
    # Entrée réservée au J21 où la réponse de Noam pousse Kael
    # vers la logique "ne laisser personne derrière".
    # Le contenu spécifique de cette journée sera développé séparément.
    $ j20_kael_depart_choice = "stay"
    jump _21_0_1_1_0_REVEIL


label _21_0_1_1_0_REVEIL:

    call show_chapter_title("Début du chapitre 7", "Chapitre 7 — Un semblant de normalité") from _call_show_chapter_title_4

    $ cafeteria_food_level = "null"
    $ current_period = "Nuit"
    $ current_day = 21
    $ day_id = 21
    $ noam_has_juliette_drawing = False

    scene black
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.5
    $ danger_on()

    "Je ne sais pas combien de temps j'ai dormi. Dix minutes, peut-être. Une heure."

    if j20_iris_qte_success:
        "Chaque fois que je rouvre les yeux, les sangles sont toujours là. J'ai accepté qu'on m'attache. Mon corps, lui, n'a pas reçu l'information."
    else:
        "Chaque fois que je rouvre les yeux, je suis toujours attaché au même lit, sous la même lumière blanche."

    "Au bout d'un moment, j'arrête de regarder l'heure. Je teste une sangle, puis l'autre, alors que je sais déjà qu'elles tiennent."

    if not j20_iris_qte_success:
        "Ma tempe me lance encore là où Iris m'a frappé."

    "Le silence de l'infirmerie est pire que la lumière. Au moindre bruit, je me redresse."

    pause 1.0

    play sound "audio/sfx_duct_scrape.wav" volume 0.64

    "Un frottement métallique vient du mur."

    "Je relève immédiatement la tête."

    noam inquiet "..."

    "Je retiens ma respiration."

    play sound "audio/sfx_duct_scrape.wav" volume 0.78

    "Le frottement revient, plus long. Quelque chose avance dans le conduit."

    noam peur "Non..."

    "Je tire sur mes poignets par réflexe."

    "Les sangles ne bougent pas."

    noam colere "Hé !"

    "Aucune réponse."

    noam colere "Il y a quelqu'un ?!"

    "Le bruit continue. Pas vite. Pas discrètement non plus."

    noam desespoir "SAEL !"

    "Je tire encore sur mes liens."

    noam "LYSA !"

    "Rien."

    "Je tire si fort que la sangle me brûle le poignet."

    noam peur "Quelqu'un m'entend ?!"

    play sound sfx_door

    "La porte de l'infirmerie s'ouvre."

    pause 0.7

    scene bg_infirmerie at adaptive_fullscreen with creep_diss

    show mara neutre at center with dissolve

    "Mara entre."

    "Je me fige complètement."

    noam panne "..."

    mara neutre "Tu vas réveiller tout le couloir."

    noam peur "Reste là."

    "Elle referme calmement la porte derrière elle."

    mara neutre "Je suis là. Arrête de hurler."

    noam inquiet "Qu'est-ce que tu fous ici, à cette heure-là ?"

    "Elle regarde l'écran de surveillance dans l'angle au lieu de me répondre."

    noam peur "Mara."

    "Elle glisse une main dans sa poche."

    "Quand elle la ressort, je reconnais immédiatement le petit cache que Kael avait bricolé quelques jours plus tôt."

    noam surpris "Attends..."

    "Elle s'approche de la caméra."

    noam peur "Mara... qu'est-ce que tu fous ?"

    "Elle fixe le cache devant l'objectif."

    pause 0.5

    noam colere "MARA !"

    "Elle se retourne."

    "Cette fois, elle sourit. Un petit sourire calme qui ne lui ressemble pas."

    noam peur "Enlève ça."

    mara sourire "Non."

    noam desespoir "ENLÈVE ÇA !"
    call kd_vn_reaction("noam", "desespoir", "#ff9c55")

    "Je recommence à tirer sur les sangles."

    mara sourire "Continue et tu vas t'ouvrir les poignets."

    noam colere "DÉTACHE-MOI !"

    "Elle avance jusqu'au lit."

    "Je me débats assez fort pour faire grincer toute la structure."

    noam "Mara, arrête !"

    "Elle pose une main sur mon épaule."

    "Je tente de me décaler, mais je n'ai aucun espace."

    noam peur "Ne me touche pas."

    "Son sourire ne disparaît pas."

    mara sourire "Tu fais vraiment beaucoup de bruit."

    noam desespoir "Va chercher Sael. Ou Lysa. N'importe qui, mais détache-moi !"

    "Elle se penche brusquement sur moi et plaque sa main sur ma bouche."

    noam "MMH—!"

    "Je tourne la tête de toutes mes forces."

    "Sa main reste fermement plaquée contre mon visage."

    "J'essaie de la mordre, mais elle retire juste assez ses doigts pour m'empêcher de les attraper entre mes dents."

    mara sourire "Je savais que tu mordrais."

    "Mon cœur cogne si fort que j'ai l'impression de l'entendre dans mes oreilles."

    play sound "audio/sfx_duct_scrape.wav" volume 0.88

    "Puis, derrière elle, la grille d'aération bouge."

    "Je cesse de me débattre une fraction de seconde."

    "Mara tourne légèrement la tête."

    play sound "audio/sfx_metal_open.mp3"

    "La grille s'ouvre."
    $ shake(7, 0.22)

    $ horror_audio_cut(duration=0.48, restore_volume=0.60)
    $ horror_music_slow(fadeout=0.25, fadein=0.60)
    $ unlock_gallery_image("bg_cg045")
    scene bg_cg045 at adaptive_fullscreen with signal_stutter
    $ cam_move(fx=0.78, fy=0.32, z=1.13, t=6.5)

    noam panne "..."

    "Quelqu'un rampe hors du conduit. Je vois ses mains, sa veste, puis son visage."

    pause 1.0

    noam peur "..."

    "Je comprends ce que je vois. C'est justement pour ça que mon cerveau refuse de suivre."

    "Même taille. Même veste. Même visage fatigué que dans le miroir de ma chambre."

    "Il se redresse lentement."

    $ impact(intensity=10, duration=0.30, color="#c81e2e")
    "{cps=7}Et je me regarde.{/cps}"
    $ doppelganger_reveal(screamer=True, duration=1.08, restore_volume=0.60)

    noam desespoir "MMMMH—!"

    "Je recommence immédiatement à me débattre."

    "Mara renforce sa prise sur mon visage."

    mara sourire "Calme-toi."

    "L'autre Noam avance sans rien dire. Il évite mon regard jusqu'au bord du lit."

    "Je tire sur mes poignets jusqu'à sentir les sangles m'entailler la peau."

    noam "MMH ! MMH !"

    "Il s'arrête au bord du lit."

    "Son regard descend sur moi."

    "Puis il sourit. C'est mon visage, mais pas un sourire que je reconnais."

    "Mara retire légèrement sa main."

    "Je prends une inspiration brutale."

    noam desespoir "Mais vous êtes quoi, putain ?!"

    "Aucune réponse."

    noam "Vous voulez quoi de moi ?!"

    $ cam_reset(t=0.20)
    scene bg_infirmerie at adaptive_fullscreen with memory_rip
    "L'autre moi tourne la tête vers le plateau médical et prend un scalpel."

    $ unlock_gallery_image("bg_cg056")
    scene bg_cg056 at adaptive_fullscreen with creep_diss

    noam panne "..."

    "Tout mon corps se tend d'un coup."

    noam peur "Non."

    "Je tire sur mes sangles."

    noam "Non, attends."

    "Il revient vers moi."

    noam desespoir "Mara... détache-moi. S'il te plaît."

    "Elle me regarde sans bouger."

    noam desespoir "Mara, je t'en supplie... détache-moi."

    "Son sourire s'élargit légèrement."

    noam peur "MARA !"

    "Elle remet sa main sur ma bouche."

    "Je hurle contre sa paume."

    "L'autre Noam s'approche encore."

    "Je secoue la tête de toutes mes forces."

    "Je lève les jambes, je tire sur mes bras, j'essaie même de basculer le lit. Rien ne cède. Avec la main de Mara sur ma bouche, je n'arrive plus à reprendre mon souffle."

    "L'autre Noam se penche."

    "Son visage est maintenant juste au-dessus du mien."

    "Il me regarde une dernière fois. Cette fois, il ne sourit plus."

    noam peur "Attends..."

    pause 0.5

    play sound "audio/sfx_tinnitus.wav" volume 0.62
    scene black with suffocation_cut
    $ shake(16, 0.40)

    "La douleur traverse ma gorge. J'essaie d'inspirer, mais l'air ne passe presque plus. Mes bras tirent encore une fois sur les sangles, sans force."

    "Ma vision se brouille."

    "Mara devient une silhouette. L'autre moi aussi. Je vois encore mon visage penché au-dessus du lit."

    noam panne "..."

    "J'essaie encore de respirer."

    scene black
    stop music fadeout 2.0
    $ danger_off()

    pause 3.0

    jump _21_0_1_1_EPILOGUE


label _21_0_1_1_EPILOGUE:

    $ current_period = "Matin"

    scene bg_navette at adaptive_fullscreen, shuttle_background with fade

    pause 1.2

    play music "audio/music/bgm_epilogue_cold.mp3" fadein 3.0

    "La navette quitte le Conclave. Dans les hublots, la station rétrécit pendant que la Terre prend toute la place."

    "Les représentants sont sanglés sur deux rangées. Au début, personne ne trouve quoi dire."

    show elen joie at left with dissolve
    show iris fatigue at right with dissolve

    elen joie "J'attends encore le moment où Kami va annoncer un dernier vote. Juste pour nous emmerder."

    iris fatigue "Ne lui donne pas d'idées. Si elle nous rappelle dans cinq minutes, je saute par le hublot."

    elen rire "On est dans l'espace, Iris."

    iris blase "Oui, merci Elen, j'avais remarqué."

    "Elen rit doucement avant de se retourner vers la planète."

    hide elen with dissolve
    hide iris with dissolve

    show tomas reflexion at left with dissolve
    show ryn fatigue at right with dissolve

    tomas reflexion "Il faudra mettre tout ça par écrit en rentrant. Les votes, M16, les conduits... Dans une semaine, on aura déjà douze versions différentes."

    ryn fatigue "Tu peux faire tes rapports si ça t'amuse. Moi, je veux juste remettre les pieds au sol et dormir une journée entière."

    tomas inquiet "Je sais, mais on peut pas faire comme si tout ça n'avait jamais existé."

    ryn fatigue "J'ai pas dit ça. J'ai dit que je voulais dormir avant ton rapport."

    "Tomas hoche la tête, presque amusé malgré lui."

    hide tomas with dissolve
    hide ryn with dissolve

    "Plus loin, Mara est assise près de Kael. Elias garde les bras croisés contre son torse et regarde par le hublot sans rien dire."

    "Noam est installé de l'autre côté de l'allée."

    "Sa ceinture est correctement attachée."

    "Ses mains reposent calmement sur ses jambes."

    "Il observe la Terre."

    show lysa blase at left with dissolve
    show noam sourire at right with dissolve

    "Lysa tourne la tête vers lui."

    lysa blase "Ça va ?"

    noam sourire "Oui. Pourquoi ?"

    lysa reflexion "Depuis qu'on est montés, t'as une tête bizarre."

    noam sourire "Une tête bizarre ?"

    lysa taquin "Ouais. Presque heureux."

    "Noam regarde de nouveau par le hublot."

    noam sourire "Je suis juste content de rentrer."

    lysa blase "Venant de toi, après les deux derniers jours, c'est presque flippant."

    noam rire "Tu préfères que je recommence à paniquer ?"

    lysa blase "Non. Garde celle-là."

    "Elle se réinstalle dans son siège."

    lysa fatigue "Profite alors. Une fois en bas, je veux dormir pendant une semaine et ne plus jamais entendre parler d'une bouche d'aération."

    noam sourire "Ça me va."

    "Lysa se détourne. Noam garde les yeux sur la planète."

    $ unlock_gallery_image("bg_cg049")
    scene bg_cg049 at adaptive_fullscreen with dissolve
    $ cam_move(fx=0.73, fy=0.42, z=1.18, t=4.5)
    "Puis, lentement, son sourire s'élargit."
    $ doppelganger_reveal(screamer=False, duration=0.90, restore_volume=0.0)

    $ horror_audio_cut(duration=0.34, restore_volume=0.0)
    $ cam_reset(t=0.0)
    scene black with signal_stutter
    stop music fadeout 0.2
    $ renpy.music.set_volume(1.0, delay=0.0, channel="music")

    pause 1.2

    call screen kd_ending_reached(
        "Le compte est bon",
        "ENDING 02 // JOUR 21"
    )
    $ _ending_screen_closed = _return

    return
