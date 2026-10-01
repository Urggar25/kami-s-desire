# =============================================================================
# JOUR 28 — La station change de mains
# Plusieurs représentants disparaissent ou sont remplacés.
# Kami annonce le dernier vote pour J30 à 8h, suivi du départ.
# Les violations des Commandements entraînent désormais un effacement de mémoire.
# =============================================================================

default j28_last_vote_announced = False

label _28_0_1_1_0_0_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"

    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Quand j'ouvre ma porte, Iris est déjà là."

    $ showGroup([
        ("iris", "fatigue", 0.38),
        ("noam", "fatigue", 0.62),
    ])

    iris fatigue "J'ai dormi vingt minutes."

    noam blase "Moi trente. Je gagne."

    iris agace "Crève."

    noam reflexion "On fait quoi ?"

    iris inquiet "On trouve les autres. Les vrais."

    noam "Tu sais lesquels sont vrais ?"

    iris fatigue "Non."

    "Voilà où on en est."

    $ hideGroup()

label _28_0_1_1_0_0_RECHERCHE:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.6

    "À la cafétéria, il n'y a que Tomas, Julian et Elen."

    $ showGroup([
        ("tomas", "stress"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("iris", "inquiet"),
        ("noam", "inquiet"),
    ])

    tomas stress "Ryn est parti chercher Nyra il y a vingt minutes."

    iris colere "Seul ?"

    tomas "Il a dit qu'il revenait."

    noam reflexion "Sael ?"

    julian inquiet "Avec Nyra, je crois. Enfin... c'est ce qu'Elen a entendu."

    elen peur "J'ai entendu sa voix dans le couloir. J'ai pas ouvert."

    iris "Bien."

    elen triste "Je commence à détester quand vous dites ça."

    "Une porte s'ouvre derrière nous."

    $ showGroup([
        ("ryn", "neutre"),
        ("tomas", "stress"),
        ("julian", "inquiet"),
        ("elen", "peur"),
        ("iris", "inquiet"),
        ("noam", "inquiet"),
    ])

    ryn neutre "Vous êtes là."

    tomas surpris "Ryn !"

    iris mefiant "Où est Nyra ?"

    ryn "Je l'ai pas trouvée."

    noam reflexion "T'étais où ?"

    ryn agace "Putain, ça commence."

    iris colere "Réponds."

    ryn colere "Dans le couloir technique. Puis maintenance. Puis ici."

    noam "Pourquoi t'as mis vingt minutes ?"

    ryn desaccord "Parce que la station fait pas trois mètres de long."

    "Ça ressemble à Ryn."

    "C'est bien ça, le problème."

    elen peur "On peut pas faire ça à chaque fois que quelqu'un revient."

    iris fatigue "Si."

    ryn colere "Super."

    "Tomas s'approche de moi."

    tomas stress "Il a raison sur un truc. On tiendra pas longtemps comme ça."

    noam inquiet "Je sais."

    $ hideGroup()

label _28_0_1_1_0_0_DISPARITIONS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.7

    "Dans l'après-midi, ça s'accélère."

    "Julian disparaît pendant qu'on cherche de l'eau."

    "On le retrouve dix minutes plus tard près de la salle commune."

    $ showGroup([
        ("julian", "sourire", 0.33),
        ("iris", "mefiant", 0.55),
        ("noam", "inquiet", 0.76),
    ])

    julian sourire "Vous avez cette tête depuis quand ?"

    iris colere "T'étais où ?"

    julian surpris "Aux toilettes."

    noam reflexion "Pendant dix minutes ?"

    julian blase "Je vais vraiment devoir détailler ?"

    iris mefiant "Oui."

    julian agace "J'ai pas d'expression agace."

    "Il lève les mains."

    julian fatigue "J'étais aux toilettes. J'ai entendu du bruit, j'ai attendu. Voilà."

    "Ça pourrait être vrai."

    "Une heure plus tard, Elen disparaît à son tour."

    "Puis Tomas."

    "Chaque fois, ils reviennent."

    "Chaque fois, ils ont une explication."

    "Chaque fois, j'y crois un peu moins."

    $ hideGroup()

label _28_0_1_1_0_0_ANNONCE:
    $ current_period = "Soir"
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "neutre"),
        ("tomas", "neutre"),
        ("julian", "sourire"),
        ("elen", "content"),
        ("iris", "inquiet"),
        ("noam", "inquiet"),
    ])

    "Quand le signal de Kami retentit, tout le monde se fige."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_fier at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Plus que deux jours !"

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Vous voyez ? Je vous avais dit que ça passerait vite."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le dernier vote aura lieu au jour trente, à huit heures précises."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Le texte propose d'interdire toute modification ou suppression de la mémoire d'une personne sans son consentement."

    $ j28_last_vote_announced = True

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Un sujet délicieusement approprié, vous ne trouvez pas ?"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Le vote sera immédiatement suivi du départ vers la Terre."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Votre navette restera au sas pendant trente minutes. Après ça... tant pis pour les retardataires."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Oh, et une dernière mise à jour."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "À compter de maintenant, les personnes qui ne respectent plus les Commandements ne seront plus exécutées."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je sais. Je deviens sentimentale."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Leur mémoire sera simplement effacée."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Beaucoup plus propre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7

    $ showGroup([
        ("ryn", "neutre"),
        ("tomas", "neutre"),
        ("julian", "sourire"),
        ("elen", "content"),
        ("iris", "peur"),
        ("noam", "peur"),
    ])

    iris peur "Elle vient vraiment de dire ça."

    noam peur "Oui."

    tomas reflexion "Techniquement, un effacement total de mémoire équivaut à..."

    iris colere "Tomas, pas maintenant."

    tomas fatigue "Ouais."

    ryn neutre "Trente minutes."

    noam reflexion "Après le vote."

    julian sourire "Ça devrait suffire."

    "Je le regarde."

    "Julian sourit."

    "Pas le sourire nerveux de ce matin."

    "Un sourire calme."

    "Je sens la main d'Iris attraper ma manche."

    iris inquiet "On bouge."

    noam determine "Ouais."

    $ hideGroup()

label _28_0_1_1_0_0_FIN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7

    "On ne retourne pas tout de suite dans nos chambres."

    "On reste ensemble."

    "À l'autre bout du couloir, Tomas nous regarde passer."

    "Puis Elen."

    "Puis Ryn."

    "Aucun ne dit rien."

    iris peur "Noam..."

    noam inquiet "Je sais."

    "Je sais même pas exactement ce que je sais."

    "Mais je sais qu'on est en train de perdre."

    call end_day("29", sleeping=True) from _call_j28_stay_end_day_29
    jump _29_0_1_1_0_0_REVEIL
