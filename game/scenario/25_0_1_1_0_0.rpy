# =============================================================================
# JOUR 25 — La preuve
# Iris et Noam obtiennent une preuve incontestable d'un remplacement.
# Kami annonce le vote du J27.
# =============================================================================

default j25_double_proof = False

label _25_0_1_1_0_0_REVEIL:
    $ current_day = 25
    $ day_id = 25
    $ current_period = "Matin"

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    $ showGroup([
        ("iris", "fatigue"),
        ("mara", "taquin"),
        ("elias", "neutre"),
        ("noam", "neutre"),
    ])

    mara taquin "Alors docteur Noam, toujours officiellement sain du cerveau ?"

    noam blase "Oui."

    iris agace "Tu peux arrêter avec ça."

    mara sourire "Je prends des nouvelles."

    elias neutre "Y'a pire comme diagnostic."

    noam reflexion "Merci Elias."

    "Je le regarde un peu trop longtemps. Il ne semble rien remarquer."

    iris reflexion "Noam ?"

    noam neutre "Rien."

    $ hideGroup()

    play sound sfx_announce
    stop music fadeout 0.5
    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Mes chers représentants, vous avez à peine fini de célébrer et il faut déjà retourner travailler."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quelle tragédie."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Le prochain amendement propose que toute personne privée de liberté soit informée du motif de sa détention et puisse le contester."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Vote au jour vingt-sept."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Essayez de ne pas enfermer quelqu'un d'ici là. Ce serait gênant."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "blase"),
        ("mara", "taquin"),
        ("elias", "neutre"),
        ("noam", "reflexion"),
    ])

    iris blase "Elle a vraiment dit ça."

    mara taquin "Moi je peux enfermer quelqu'un avec consentement, ça compte ?"

    noam fatigue "Je vais partir."

    mara rire "Encore ?"

    $ hideGroup()

label _25_0_1_1_0_0_INDICE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Je retrouve Iris devant sa chambre. Elle tient quelque chose dans la main."

    $ showGroup([
        ("iris", "inquiet", 0.38),
        ("noam", "reflexion", 0.62),
    ])

    iris inquiet "Regarde."

    "C'est un petit morceau de tissu brun, sale, avec une couture déchirée."

    noam reflexion "C'est quoi ?"

    iris inquiet "Je l'ai trouvé coincé derrière ma grille."

    noam inquiet "Dans la ventilation ?"

    iris neutre "Ouais. Et je l'ai déjà vu."

    noam reflexion "Où ?"

    iris inquiet "Sur la veste de Mara."

    pause 0.4

    noam inquiet "..."

    iris agace "Dis pas rien."

    noam reflexion "Je réfléchis."

    iris agace "Bah réfléchis plus vite."

    noam neutre "Tu veux retourner dedans."

    iris determine "Oui."

    noam fatigue "Évidemment."

    iris colere "Tu préfères attendre qu'un autre bout de quelqu'un tombe de la grille ?"

    noam neutre "Non."

    iris determine "Alors viens."

    $ hideGroup()

label _25_0_1_1_0_0_CONDUITS:
    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "On avance à deux. Iris devant, moi derrière. La plaque de sa chambre avait été posée parmi les premières ; elle la remettra en place en sortant."

    "Au premier embranchement, elle s'arrête."

    $ showGroup([
        ("iris", "inquiet", 0.35),
        ("noam", "inquiet", 0.65),
    ])

    iris inquiet "T'entends ?"

    noam reflexion "Non."

    iris inquiet "Justement."

    "Pas de ventilation. Pas de vibration. Rien."

    noam determine "On continue."

    iris determine "Ouais."

    $ hideGroup()

    "On rampe encore plusieurs minutes jusqu'à la zone que j'avais déjà traversée."

    "Puis je reconnais l'angle."

    think "Non."

    "Je reconnais surtout l'odeur."

    scene bg_conduit_reseau at adaptive_fullscreen with creep_diss

    $ showGroup([
        ("iris", "peur", 0.35),
        ("noam", "peur", 0.65),
    ])

    iris peur "Noam..."

    noam peur "Je sais."

    "Le corps est toujours là."

    "Mara."

    "Même veste. Même cheveux. Même visage."

    "Iris ne dit plus rien. Elle tend la main, puis la retire avant de toucher."

    iris peur "C'est... c'est elle."

    noam faible "Oui."

    iris peur "Mais elle était avec nous ce matin."

    noam faible "Oui."

    iris colere "Non. Arrête de dire oui comme ça."

    noam peur "Je sais pas quoi dire."

    iris peur "Putain..."

    "Elle finit par s'accroupir et regarde la couture de la manche."

    iris inquiet "Le morceau."

    "La déchirure correspond exactement."

    noam inquiet "Donc..."

    iris peur "Donc t'as pas halluciné."

    "Elle me regarde enfin."

    iris peur "Et la Mara qui mange avec nous..."

    noam determine "C'est pas Mara."

    $ j25_double_proof = True

    "Un bruit métallique résonne plus loin dans le conduit."

    iris surpris "On bouge."

    noam determine "Maintenant."

    $ hideGroup()

label _25_0_1_1_0_0_RETOUR:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showGroup([
        ("iris", "inquiet", 0.38),
        ("noam", "inquiet", 0.62),
    ])

    "On remet la plaque de la chambre d'Iris en place."

    iris inquiet "On dit rien à personne."

    noam surpris "Rien ?"

    iris neutre "Pas maintenant. Si Mara est... ça, on sait pas qui d'autre l'est."

    noam reflexion "Et si on attend, ils peuvent continuer."

    iris fatigue "Je sais."

    noam reflexion "Le monde regarde le Conclave."

    iris inquiet "Noam..."

    noam neutre "Si on se trompe, je passe pour un malade."

    iris peur "Et si tu te trompes pas ?"

    noam determine "Alors ils pourront plus faire semblant que personne sait."

    "Elle me fixe."

    iris inquiet "Réfléchis avant de faire un truc énorme."

    noam neutre "Je vais réfléchir."

    "Je mens un peu."

    $ hideGroup()

    call end_day("26", sleeping=True) from _call_j25_stay_end_day_26
    jump _26_0_1_1_0_0_REVEIL
