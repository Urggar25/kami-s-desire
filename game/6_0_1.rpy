# --------------------------------------------------------------------------------------------
# JOUR 6_0_1 — Branche statu quo post-accident café
# Vote libre circulation : échec annoncé, malaise grandissant autour de Kami.
# --------------------------------------------------------------------------------------------

default j601_vote_noam = "abstention"
default j601_signal_result = False
default j601_qte_hits = 0
default j601_kami_irritation = 0

default j601_vote_failed = True

default j601_elen_comment = True
default j601_lysa_comment = True

label _6_0_1_CANON:

    $ day_id = 6

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.6

    think "Jour six."
    think "J'ai un goût métallique dans la bouche."
    think "Et cette impression bizarre..."
    think "Comme si j'avais oublié quelque chose."

    pause 0.5

    scene bg_cg012 at adaptive_fullscreen with fade

    "Je regarde le plafond."
    "Blanc."
    "Très blanc."

    $ blink()

    think "Je suis fatigué."
    think "Tant pis."

    pause 0.5

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Debout."
    kami "Vote à quatorze heures."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Libre circulation entre districts."
    kami "Oui, encore."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ne me forcez pas à refaire une journée de maintenance à cause de vos conneries."
    kami "J'ai déjà du retard."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et non, ce n'est pas une invitation à improviser."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    stop music fadeout 0.8
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "L'écran s'éteint trop vite."
    "Pas de rire final."
    "Pas de formule."

    think "Elle est tendue."
    think "Ou cassée."
    think "Ou les deux."

    pause 0.5

    "Je me lève."
    "Je passe de l'eau sur mon visage."
    "Ça ne change rien."

    pause 0.4

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Le couloir est plein de pas pressés."
    "Pas de discussions longues."
    "Des phrases courtes."
    "Comme si tout le monde avait peur d'être entendu."

    pause 0.4

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "08:30."
    "Cafétéria."

    "L'ambiance est lourde."
    "Même les plateaux font moins de bruit."

    $ showP("noam", "neutre", 0.50)
    $ showP("elias", "inquiet", 0.20)
    $ showP("mara", "blase", 0.80)

    elias "Je..."
    elias "Attends."

    "Elias attrape son verre."
    "Le verre glisse."
    "Encore."

    play sound "sound/sfx_abstention.ogg"

    elias "Merde."

    $ showP("mara", "rire", 0.80)
    mara "On dirait un running gag, là."
    mara "Version triste."

    hide noam
    $ showP("elen", "inquiet", 0.50)

    elen "... Vous trouvez pas que Kami est bizarre ce matin ?"
    elen "Genre vraiment bizarre."

    hide elias
    $ showP("lysa", "blase", 0.20)

    lysa "Ouais."
    lysa "Pas dans son assiette, la reine des écrans."
    lysa "J'aime pas quand elle parle comme ça."

    hide mara
    $ showP("noam", "reflexion", 0.80)

    noam "Elle était agressive."
    noam "Même pour elle."

    $ showP("elen", "surpris", 0.50)
    elen "Et l'hologramme bugguait."
    elen "J'ai vu sa joue se décaler."
    elen "Une seconde."
    elen "Pas normal."

    $ showP("lysa", "reflexion", 0.20)
    lysa "Normal chez Kami, ça veut déjà pas dire grand-chose."
    lysa "Mais là..."
    lysa "Là c'était pire."

    pause 0.5

    "Un bip sec retentit dans la salle."
    "Toutes les tablettes s'allument en même temps."

    voix "Représentants convoqués au Conclave."
    voix "Départ immédiat."
    voix "Aucun temps libre ce matin."

    hide elen
    $ showP("mara", "stress", 0.50)

    mara "Magnifique."
    mara "Même plus le temps de faire semblant."

    hide noam
    $ showP("iris", "desaccord", 0.80)

    iris "On sait déjà que ça va planter."
    iris "On est convoqués pour regarder le crash en direct."

    hide lysa
    $ showP("sael", "neutre", 0.20)

    sael "Ça ira vite."
    sael "J'ai rien à ajouter."

    hide mara
    $ showP("noam", "inquiet", 0.50)

    noam "Tu votes contre ?"

    $ showP("sael", "froid", 0.20)
    sael "Oui."

    hide iris
    $ showP("ryn", "colere", 0.80)

    ryn "Super."
    ryn "Au moins c'est clair."

    pause 0.5

    scene bg_couloir at adaptive_fullscreen with dissolve

    "On traverse le couloir en groupe compact."
    "Personne ne traîne."
    "Personne ne plaisante."

    think "Tout le monde sait."
    think "Le vote va échouer."

    pause 0.5

    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "14:00."
    "Le Conclave ressemble à une salle d'attente."
    "Pas à une salle de décision."

    $ showP("kami", "neutre", 0.50)

    "L'hologramme de Kami apparaît au centre."
    "L'image saute d'un cran."
    "Puis revient."

    kami "Débat de la motion de libre circulation."
    kami "Vous connaissez la règle."
    kami "Unanimité."

    "Sa voix se découpe sur certaines consonnes."

    hide kami
    $ showP("iris", "desaccord", 0.20)
    $ showP("sael", "froid", 0.50)
    $ showP("julian", "inquiet", 0.80)

    iris "Je vote contre."

    sael "Contre."

    $ showP("julian", "triste", 0.80)
    julian "On pourrait au moins entendre les arguments avant de..."

    $ showP("iris", "colere", 0.20)
    iris "Non."
    iris "J'ai déjà donné."

    "Le débat s'écrase sur place."
    "Quelques phrases partent."
    "Aucune ne tient."

    hide julian
    $ showP("lysa", "blase", 0.80)

    lysa "On peut arrêter de jouer la pièce ?"
    lysa "Le résultat est écrit."

    hide sael
    $ showP("kami", "colere", 0.50)

    kami "Silence."
    kami "Je n'ai pas validé la fin de séquence."

    "L'hologramme scintille."
    "Les contours de ses yeux se décalent."

    kami "Signal..."
    kami "Instable."
    kami "Maintenez la liaison."

    $ j601_signal_result = renpy.call("j601_play_signal_instable")

    if j601_signal_result:
        $ j601_kami_irritation += 1
        kami "Lien stabilisé."
        kami "Tant mieux pour vous."
    else:
        $ j601_kami_irritation += 2
        kami "Pathétique."
        kami "Je le fais moi-même."

    "La diffusion revient avec une latence visible."

    kami "Deuxième protocole."
    kami "Détection de fracture lexicale."
    kami "Maintenant."

    $ j601_qte_hits = renpy.call("j601_play_fracture_qte")

    if j601_qte_hits >= 4:
        $ j601_kami_irritation += 2
        kami "Quatre sur quatre."
        kami "Tu m'écoutes trop bien, Noam."
        kami "Mauvaise habitude."
    elif j601_qte_hits >= 2:
        $ j601_kami_irritation += 1
        kami "Passable."
        kami "Ne prends pas confiance."
    else:
        kami "Insuffisant."
        kami "Comme prévu."

    pause 0.5

    hide iris
    $ showP("noam", "reflexion", 0.20)
    hide kami
    $ showP("mara", "neutre", 0.50)
    hide lysa
    $ showP("kael", "inquiet", 0.80)

    noam "On vote ?"

    mara "On expédie, oui."

    kael "J'aimerais me tromper..."
    kael "Mais ça ne passera pas."

    menu:
        "Mon vote":
            "Voter POUR":
                $ j601_vote_noam = "pour"
            "Voter CONTRE":
                $ j601_vote_noam = "contre"
            "S'abstenir":
                $ j601_vote_noam = "abstention"

    "Les tablettes confirment les choix."
    "Une ligne rouge clignote."

    voix "Unanimité non atteinte."
    voix "Motion rejetée."

    $ j601_vote_failed = True

    "Personne n'a l'air surpris."

    hide kael
    $ showP("sael", "neutre", 0.80)

    sael "Voilà."
    sael "C'est fini."

    hide mara
    $ showP("elen", "triste", 0.50)

    elen "On dirait même pas une fin..."
    elen "On dirait juste qu'on recule."

    hide noam
    $ showP("lysa", "fatigue", 0.20)

    lysa "On recule, oui."
    lysa "Et demain on fera semblant que c'est une stratégie."

    pause 0.7

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Le trajet retour se fait dans le silence."
    "Pas un vrai silence calme."
    "Un silence vide."

    "Je compte les portes."
    "Une."
    "Deux."
    "Trois."
    "Ça m'occupe."

    think "Je suis vidé."
    think "Je continue."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je ferme la porte derrière moi."
    "Le verrou clique."

    "Je reste debout un moment."
    "Les mains sur la poignée."

    think "Quelque chose a changé chez Kami."
    think "Je n'arrive pas à dire quoi."
    think "Mais c'est là."

    pause 0.6

    "Je m'allonge sans me déshabiller."
    "Les néons du couloir glissent sous la porte."
    "Un trait blanc."
    "Régulier."

    think "Demain sera pire."
    think "Je dormirai quand même."

    $ blink()


    # Fragments nocturnes — montée de malaise
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."
    "Un. Deux. Trois."
    "J'arrête de compter."
    "Je n'aime pas quand je commence à calculer pour me calmer."
    "Je pense à Sael."
    "Je pense à Iris."
    "Je pense au vote déjà mort avant de naître."
    "Je n'ai pas de conclusion brillante."
    "J'ai juste une fatigue lourde."
    "Et cette sensation qu'on a raté un virage."
    "Ou que quelqu'un l'a raté pour nous."
    "Je ferme les yeux. Puis je les rouvre."
    "Le plafond ne répond rien."
    "Je repense au glitch sur la voix de Kami."
    "Un mot coupé net. Puis un autre."
    "Je me dis que ce n'est peut-être qu'un bug."
    "Je me dis aussi que je mens mal."
    "Dans le couloir, quelqu'un marche."
    "Trois pas. Pause. Deux pas."
    "Même les bruits ont l'air hésitants."
    "Je compte ma respiration."

    pause 1.0

    call end_day("6") from _call_end_day_6_0_1
    jump _7_CANON

    return

# Durée : 12m30
# Total : 2h 09m 25s
