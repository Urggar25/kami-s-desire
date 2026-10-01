# =============================================================================
# JOUR 30 — Le treizième représentant
# Dernier vote, arrivée de la navette, choix final :
# forcer la barricade ou passer par les conduits.
# =============================================================================

default j30_final_choice = None
default j30_final_vote = "rejected"

label _30_0_1_1_0_0_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "Je me réveille avec Iris assise contre la porte."

    "Elle tient encore la barre métallique qu'on a utilisée pour bloquer la poignée."

    $ showGroup([
        ("iris", "fatigue", 0.40),
        ("noam", "fatigue", 0.62),
    ])

    noam fatigue "T'as dormi ?"

    iris blase "Énormément. Au moins neuf minutes."

    noam taquin "La forme, alors."

    iris agace "Ferme-la."

    "Quelqu'un parle derrière la porte."

    elen content "Vous êtes réveillés ?"

    "Iris lève immédiatement un doigt devant sa bouche."

    elen "Le vote est dans dix minutes."

    julian sourire "On vous laisse tranquilles. On voulait juste être sûrs que vous l'aviez pas oublié."

    iris blase "Comme c'est gentil."

    noam inquiet "Ils nous entendent."

    iris fatigue "Je sais."

    mara taquin "Oui, on vous entend."

    "Iris ferme les yeux."

    mara "Et Iris, t'es toujours aussi subtile."

    iris colere "Va te faire foutre."

    mara rire "Voilà. Là je te reconnais."

    "Des rires étouffés viennent du couloir."

    "Plusieurs."

    noam peur "Ils sont tous là."

    iris determine "On ouvre pas."

    $ hideGroup()

label _30_0_1_1_0_0_VOTE:
    "À huit heures précises, le signal de Kami couvre les voix."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_fier at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Jour trente."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Nous y sommes enfin."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je sais que certains d'entre vous ont choisi une ambiance un peu... intime pour ce dernier matin."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pas de problème. Vos votes fonctionnent très bien depuis vos chambres."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Dernier amendement : interdire toute modification, suppression ou réécriture de la mémoire d'une personne sans son consentement."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "À vous."

    hide screen kami_broadcast_ui
    stop music fadeout 0.5
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.6

    $ showGroup([
        ("iris", "determine", 0.40),
        ("noam", "determine", 0.62),
    ])

    iris determine "Pour."

    noam determine "Pour."

    "Les votes des autres arrivent un à un sur nos tablettes."

    "CONTRE."

    "CONTRE."

    "CONTRE."

    "Encore."

    "Encore."

    "Je cesse de compter."

    iris peur "Ils votent tous contre."

    noam inquiet "Oui."

    iris colere "Pourquoi ?"

    noam reflexion "Parce qu'ils savent ce que ça leur permet de faire."

    "Le verdict apparaît."

    "AMENDEMENT REJETÉ."

    $ j30_final_vote = "rejected"

    "Iris pose sa tablette."

    iris fatigue "Super."

    noam "On s'en fout. La navette."

    iris determine "Ouais."

    $ hideGroup()

    play sound sfx_announce
    scene bg_diffusion_champagne at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.6

    kami "Et voilà !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Votre dernier grand désaccord."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "La navette de retour vient de s'amarrer."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous avez trente minutes pour monter à bord."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Après quoi elle partira. Avec ou sans vous."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Essayez de ne pas être en retard. Ce serait vraiment dommage après tout ça."

    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

label _30_0_1_1_0_0_SORTIE:
    $ showGroup([
        ("iris", "determine", 0.40),
        ("noam", "determine", 0.62),
    ])

    iris determine "On y va."

    "On retire la chaise."

    "Puis la commode."

    "Puis le bureau."

    "Je déverrouille."

    "La porte bouge de trois centimètres."

    noam surpris "Quoi ?"

    "Je pousse plus fort."

    "Rien."

    iris inquiet "Recule."

    "Elle frappe de l'épaule. La porte s'ouvre à peine davantage."

    iris colere "Putain !"

    noam peur "Ils ont bloqué le couloir."

    "Par l'ouverture, je distingue des caisses, une table renversée, des plaques métalliques et même un morceau de banc empilés contre notre porte."

    iris "Ils ont fait ça quand ?"

    noam reflexion "Cette nuit."

    iris colere "Ils nous ont enfermés."

    "Mon téléphone affiche vingt-huit minutes."

    iris inquiet "On peut dégager."

    noam "Peut-être."

    iris reflexion "Ou l'aération."

    "On regarde tous les deux la plaque qui condamne la grille."

    noam peur "Les conduits."

    iris "On sait où ils mènent."

    noam "On sait aussi ce qu'il y a dedans."

    "Vingt-sept minutes."

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Comment atteindre la navette ?"
        "Forcer la barricade":
            $ j30_final_choice = "barricade"
            jump _30_0_1_1_0_0_BARRICADE
        "Passer par les conduits":
            $ j30_final_choice = "vents"
            jump _30_0_1_1_0_0_CONDUITS

label _30_0_1_1_0_0_BARRICADE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.4

    $ showGroup([
        ("iris", "determine", 0.40),
        ("noam", "determine", 0.62),
    ])

    noam determine "On dégage la porte."

    iris determine "D'accord. Ensemble."

    "On pousse."

    "Le métal grince de l'autre côté."

    "Une caisse tombe."

    "On gagne dix centimètres."

    iris colere "Encore !"

    "On pousse jusqu'à ne plus sentir nos bras."

    "Le téléphone affiche dix-neuf minutes."

    noam fatigue "Ça avance pas assez."

    iris colere "On continue."

    "Je passe un bras dans l'ouverture pour attraper une caisse."

    "Quelque chose cède."

    "Le poids de la barricade bascule d'un coup contre la porte."

    "Mon bras est coincé."

    noam colere "AH !"

    iris peur "Noam ! Bouge pas !"

    noam panique "Je peux pas !"

    "Elle tire la porte vers elle. Je récupère mon bras, la peau ouverte sur l'avant-bras."

    iris colere "Merde, merde..."

    noam faible "Ça va."

    iris colere "Non, ça va pas !"

    "Quatorze minutes."

    "On recommence malgré tout."

    "Douze."

    "Neuf."

    "À cinq minutes, la porte s'ouvre enfin assez pour passer une épaule."

    "Derrière, trois autres meubles bloquent encore le couloir."

    iris peur "Non..."

    noam faible "On n'y arrivera pas."

    iris colere "Si."

    noam "Iris."

    "Le grondement de la navette traverse la station."

    "On se fige."

    iris peur "Non."

    "Je regarde l'heure."

    "00:00."

    "Un deuxième grondement."

    "Puis plus rien."

    "La navette vient de partir."

    iris triste "Ils sont dedans."

    noam peur "Tous."

    "Je glisse contre la porte."

    "Quelque part derrière cette barricade, onze visages que je connais viennent de partir vers la Terre."

    "Avec nos noms."

    scene black with fade
    stop music fadeout 1.0

    call screen kd_ending_reached(
        "Trop tard",
        "ENDING 05 // JOUR 30"
    )
    $ _ending_screen_closed = _return
    return

label _30_0_1_1_0_0_CONDUITS:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4

    $ showGroup([
        ("iris", "peur", 0.40),
        ("noam", "determine", 0.62),
    ])

    noam determine "Les conduits."

    iris peur "Je déteste cette phrase."

    noam "Moi aussi."

    "On retire les fixations de la plaque."

    "Ça prend trop de temps."

    "Vingt-trois minutes."

    "Enfin, l'ouverture est libre."

    iris determine "Je passe devant."

    noam "Non."

    iris colere "Noam, commence pas."

    noam determine "J'y suis déjà allé. Je connais mieux."

    "Elle veut discuter, puis regarde le chrono."

    iris fatigue "D'accord. Mais tu t'arrêtes au moindre truc bizarre."

    noam taquin "Définis bizarre."

    iris blase "Ta gueule et avance."

    $ hideGroup()

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve

    "On rampe vite. Trop vite."

    "Je me cogne deux fois. Iris jure derrière moi."

    "À la première intersection, quelque chose bloque le passage."

    "Je pointe la lumière de mon téléphone."

    "Sael."

    "Son corps est recroquevillé contre la paroi."

    scene bg_conduit_reseau at adaptive_fullscreen with creep_diss

    $ showGroup([
        ("iris", "peur", 0.40),
        ("noam", "peur", 0.62),
    ])

    iris peur "Oh putain..."

    noam faible "Continue."

    iris colere "Noam..."

    noam peur "On a pas le temps."

    "On passe à côté d'elle."

    $ hideGroup()

    "Plus loin, Tomas."

    "Puis Nyra."

    "Ryn est étendu sur le dos, une main encore refermée sur un morceau de grille."

    "Elen est là aussi."

    "Je détourne les yeux."

    "Julian."

    "Lysa."

    "Kael."

    "Elias."

    "Mara."

    "Les vrais."

    "Tous."

    "À chaque corps, le Conclave se vide un peu plus dans ma tête."

    scene bg_conduit_reseau at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "triste", 0.40),
        ("noam", "faible", 0.62),
    ])

    iris triste "Ils les ont tous mis ici..."

    noam faible "Pour qu'on les trouve pas."

    iris peur "Pourquoi nous laisser un passage ?"

    "Je m'arrête."

    noam inquiet "Je crois pas qu'ils l'ont laissé."

    "Devant nous, une trappe est ouverte."

    "Je ne l'avais jamais vue."

    "Derrière : une petite salle technique."

    "Et un écran encore allumé."

    $ hideGroup()

    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.5

    "On descend."

    "L'écran affiche une liste."

    "Douze noms."

    "Noam. Iris. Mara. Kael. Elias..."

    "À côté de chacun : un profil."

    "Puis une treizième ligne."

    "Aucun nom."

    "POLYMORPHE."

    "PROFILS DISPONIBLES : 12/12."

    "STATUT : ÉVASION — JOUR 5."

    $ showGroup([
        ("iris", "peur", 0.40),
        ("noam", "peur", 0.62),
    ])

    iris peur "Jour cinq..."

    noam reflexion "L'incident."

    iris "C'était pas juste un incident."

    noam peur "Non."

    "Un autre écran s'allume tout seul."

    "Douze portraits défilent."

    "Les nôtres."

    "Sous chacun, le même mot : COMPATIBLE."

    iris peur "C'est quoi ce truc ?"

    noam "Je sais pas."

    "Une voix résonne derrière nous."

    "Ma voix."

    "Exactement ma voix."

    "« Vous avez mis du temps. »"

    "Je me retourne."

    scene black with signal_stutter
    stop music fadeout 0.4

    "TREIZIÈME REPRÉSENTANT"

    call screen kd_ending_reached(
        "Le treizième représentant",
        "ENDING 06 // JOUR 30"
    )
    $ _ending_screen_closed = _return
    return
