# =============================================================================
# JOUR 21 — Route 0_1_1
# =============================================================================


label _21_0_1_1_0_REVEIL:

    $ day_id = 21
    $ current_day = 21
    $ current_period = "Nuit"

    scene black
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.5
    $ danger_on()

    "Je ne sais pas vraiment si j'ai dormi."

    "À plusieurs reprises, j'ai l'impression de fermer les yeux quelques minutes avant de me réveiller en sursaut, toujours attaché au même lit, toujours sous cette lumière blanche qui finit par me brûler les yeux."

    "Au bout d'un moment, je cesse même d'essayer de compter les heures."

    "Demain n'existe plus vraiment."

    "Il n'y a que cette chambre."

    "Les sangles."

    "La douleur à ma tempe."

    "Et le silence."

    pause 1.0

    play sound "audio/sfx_duct_scrape.wav" volume 0.64

    "Puis un bruit résonne derrière le mur."

    "Je relève immédiatement la tête."

    noam inquiet "..."

    "Je reste immobile quelques secondes, en essayant de savoir si je l'ai réellement entendu."

    play sound "audio/sfx_duct_scrape.wav" volume 0.78

    "Le frottement revient."

    "Plus net cette fois."

    "Quelque chose se déplace dans le conduit."

    noam peur "Non..."

    "Je tire sur mes poignets par réflexe."

    "Les sangles ne bougent pas."

    noam colere "Hé !"

    "Aucune réponse."

    noam colere "Il y a quelqu'un ?!"

    "Le bruit continue derrière le mur, lentement, comme si quelque chose avançait sans chercher à se presser."

    noam desespoir "SAEL !"

    "Je tire encore sur mes liens."

    noam "LYSA !"

    "Rien."

    "La panique commence à monter beaucoup plus vite que je ne peux la contrôler."

    noam peur "Quelqu'un m'entend ?!"

    play sound sfx_door

    "La porte de l'infirmerie s'ouvre."

    pause 0.7

    scene bg_infirmerie at adaptive_fullscreen with creep_diss

    show mara neutre at center with dissolve

    "Mara entre."

    "Je me fige complètement."

    noam panne "..."

    mara neutre "Tu fais encore du bruit."

    noam peur "Reste là."

    "Elle referme calmement la porte derrière elle."

    mara "Tu vas réveiller tout le monde."

    noam inquiet "Qu'est-ce que tu fais ici ?"

    "Elle ne répond pas immédiatement."

    "Elle regarde la pièce, puis l'écran de surveillance fixé dans l'angle."

    noam peur "Mara."

    "Elle glisse une main dans sa poche."

    "Quand elle la ressort, je reconnais immédiatement le petit cache que Kael avait bricolé quelques jours plus tôt."

    noam surpris "Attends..."

    "Elle s'approche de la caméra."

    noam peur "Mara, qu'est-ce que tu fais ?"

    "Elle fixe le cache devant l'objectif."

    pause 0.5

    noam colere "MARA !"

    "Elle se retourne."

    "Cette fois, elle sourit."

    "Pas comme lorsqu'elle se moque de quelqu'un. Pas comme lorsqu'elle cherche à provoquer."

    "C'est un sourire beaucoup trop calme."

    noam peur "Enlève ça."

    mara sourire "Chut."

    noam desespoir "ENLÈVE ÇA !"

    "Je recommence à tirer sur les sangles."

    mara "Tu vas te faire mal."

    noam colere "DÉTACHE-MOI !"

    "Elle avance jusqu'au lit."

    "Je me débats assez fort pour faire grincer toute la structure."

    noam "Mara, arrête !"

    "Elle pose une main sur mon épaule."

    "Je tente de me décaler, mais je n'ai aucun espace."

    noam peur "Ne me touche pas."

    "Son sourire ne disparaît pas."

    mara sourire "Tu fais vraiment beaucoup de bruit."

    noam "Va chercher quelqu'un. Appelle Lysa. Appelle Sael. N'importe qui."

    "Elle se penche brusquement sur moi et plaque sa main sur ma bouche."

    noam "MMH—!"

    "Je tourne la tête de toutes mes forces."

    "Sa main reste fermement plaquée contre mon visage."

    "J'essaie de la mordre, mais elle retire juste assez ses doigts pour m'empêcher de les attraper entre mes dents."

    mara sourire "Je savais que tu essaierais."

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

    "Quelqu'un rampe hors du conduit."

    "Je regarde d'abord ses mains."

    "Puis ses bras."

    "Puis son visage."

    pause 1.0

    noam peur "..."

    "Je ne comprends pas."

    "Je le vois, mais mon cerveau refuse simplement de donner un sens à ce qui est devant moi."

    "Même taille."

    "Même visage."

    "Même cheveux."

    "Même expression fatiguée que celle que j'ai vue des dizaines de fois dans un miroir depuis le début du Conclave."

    "Il se redresse lentement."

    $ impact(intensity=10, duration=0.30, color="#c81e2e")
    "{cps=7}Et je me regarde.{/cps}"
    $ doppelganger_reveal(screamer=True, duration=1.08, restore_volume=0.60)

    noam desespoir "MMMMH—!"

    "Je recommence immédiatement à me débattre."

    "Mara renforce sa prise sur mon visage."

    mara sourire "Calme-toi."

    "L'autre Noam avance sans rien dire."

    "Je tire sur mes poignets jusqu'à sentir les sangles m'entailler la peau."

    noam "MMH ! MMH !"

    "Il s'arrête au bord du lit."

    "Son regard descend sur moi."

    "Puis il sourit."

    "Pas comme moi."

    "Pas vraiment."

    "Quelque chose dans son visage est trop satisfait."

    "Trop tranquille."

    "Comme s'il attendait ce moment depuis longtemps."

    "Mara retire légèrement sa main."

    "Je prends une inspiration brutale."

    noam desespoir "Qu'est-ce que vous êtes ?!"

    "Aucune réponse."

    noam "Qu'est-ce que vous voulez ?!"

    $ cam_reset(t=0.20)
    scene bg_infirmerie at adaptive_fullscreen with memory_rip
    "L'autre moi tourne la tête vers le plateau médical."

    "Il tend la main."

    "Ses doigts se referment sur un scalpel."

    noam panne "..."

    "Tout mon corps se tend d'un coup."

    noam peur "Non."

    "Je tire sur mes sangles."

    noam "Non, attends."

    "Il revient vers moi."

    noam desespoir "Mara, détache-moi."

    "Elle me regarde sans bouger."

    noam "Mara, je t'en supplie, détache-moi."

    "Son sourire s'élargit légèrement."

    noam peur "MARA !"

    "Elle remet sa main sur ma bouche."

    "Je hurle contre sa paume."

    "L'autre Noam s'approche encore."

    "Je secoue la tête de toutes mes forces."

    "Je tente de lever les jambes, de casser les sangles, de me tordre suffisamment pour tomber du lit, n'importe quoi."

    "Rien ne fonctionne."

    "Je n'ai plus assez d'air."

    "Je n'arrive plus à respirer correctement."

    "La main de Mara."

    "Les sangles."

    "La peur."

    "Tout se mélange."

    "L'autre Noam se penche."

    "Son visage est maintenant juste au-dessus du mien."

    "Il me regarde comme s'il cherchait à mémoriser quelque chose."

    "Puis son sourire devient presque joyeux."

    pause 0.5

    play sound "audio/sfx_tinnitus.wav" volume 0.62
    scene black with suffocation_cut
    $ shake(16, 0.40)

    "Une douleur brutale traverse ma gorge."

    "Je n'entends même pas immédiatement le bruit qui sort de ma bouche."

    "J'essaie d'inspirer."

    "L'air ne passe presque plus."

    "Je tente encore de tirer sur mes bras, mais mes forces disparaissent beaucoup trop vite."

    "Ma vision se brouille."

    "Mara devient une silhouette."

    "L'autre moi aussi."

    "Je vois encore son visage."

    "Mon visage."

    "Toujours souriant."

    noam panne "..."

    "J'essaie de respirer."

    "Je veux juste respirer."

    "Encore une fois."

    "Une seule."

    scene black
    stop music fadeout 2.0
    $ danger_off()

    pause 3.0

    jump _21_0_1_1_EPILOGUE


label _21_0_1_1_EPILOGUE:

    $ current_period = "Matin"

    scene bg_navette_retour at adaptive_fullscreen, shuttle_background with fade

    pause 1.2

    play music "audio/music/bgm_epilogue_cold.mp3" fadein 3.0

    "La navette quitte lentement le Conclave."

    "À travers les hublots, la station s'éloigne progressivement tandis que la Terre occupe une place de plus en plus importante dans le champ de vision."

    "Les représentants sont installés sur deux rangées de sièges, maintenus par les sangles prévues pour la descente."

    "Personne ne parle beaucoup."

    "Après trois semaines passées enfermés dans le Conclave, le simple fait de voir la planète se rapprocher suffit à occuper le silence."

    show elen joie at left with dissolve
    show iris fatigue at right with dissolve

    elen joie "J'arrive toujours pas à croire qu'on rentre vraiment. J'ai l'impression qu'on va entendre Kami annoncer un nouveau vote au dernier moment juste pour nous faire une mauvaise blague."

    iris fatigue "Ne lui donne pas d'idées. Si elle nous rappelle dans cinq minutes, je saute par le hublot."

    elen rire "On est dans l'espace."

    iris blase "Oui, merci Elen, j'avais remarqué."

    "Elen rit doucement avant de se retourner vers la planète."

    hide elen with dissolve
    hide iris with dissolve

    show tomas reflexion at left with dissolve
    show ryn fatigue at right with dissolve

    tomas reflexion "Il va quand même falloir qu'on mette tout ce qui s'est passé par écrit dès qu'on rentre. Les votes, M16, les conduits, les procédures internes de Kami... Si on attend trop longtemps, chacun va finir par raconter une version différente."

    ryn fatigue "Tu peux faire tes rapports si ça t'amuse. Moi, je veux juste remettre les pieds au sol et dormir une journée entière."

    tomas "Je comprends, mais avec ce qu'on a découvert, je pense vraiment qu'on ne peut pas juste rentrer chez nous et faire comme si rien ne s'était passé."

    ryn "J'ai pas dit ça. J'ai dit que je voulais dormir avant."

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

    lysa reflexion "Je sais pas. T'as une tête bizarre depuis qu'on est montés."

    noam sourire "Une tête bizarre ?"

    lysa taquin "Ouais. Presque heureux."

    "Noam regarde de nouveau par le hublot."

    noam sourire "Je suis juste content de rentrer."

    lysa blase "Ça, venant de toi après les deux derniers jours, c'est presque inquiétant."

    noam rire "Tu préfères que je recommence à paniquer ?"

    lysa "Non. Clairement pas."

    "Elle se réinstalle dans son siège."

    lysa fatigue "Profite alors. Une fois en bas, je veux dormir pendant une semaine et ne plus jamais entendre parler d'une bouche d'aération."

    noam sourire "Ça me va."

    "La navette continue sa descente."

    "Noam garde les yeux tournés vers la planète."

    $ cam_move(fx=0.73, fy=0.42, z=1.18, t=4.5)
    "Puis, lentement, son sourire s'élargit."
    $ doppelganger_reveal(screamer=False, duration=0.90, restore_volume=0.0)

    $ horror_audio_cut(duration=0.34, restore_volume=0.0)
    $ cam_reset(t=0.0)
    scene black with signal_stutter
    stop music fadeout 0.2
    $ renpy.music.set_volume(1.0, delay=0.0, channel="music")

    pause 2.0

    pause 2.0

    return
