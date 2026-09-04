default j6_noam_vote = None


# Mise en scène propre à la route 6_1_0 : mouvements lents pour la tension,
# accélérations brèves lors de la confrontation, et lumière pulsée au vote.
transform j610_morning_reveal:
    alpha 0.0
    zoom 1.035
    easeout 1.4 alpha 1.0 zoom 1.0

transform j610_tension_push:
    zoom 1.0
    ease 10.0 zoom 1.045

transform j610_vote_breathe:
    matrixcolor BrightnessMatrix(0.0)
    ease 1.8 matrixcolor BrightnessMatrix(0.08)
    ease 1.8 matrixcolor BrightnessMatrix(0.0)
    repeat

transform j610_impact_flash:
    alpha 0.78
    linear 0.16 alpha 0.0


label _6_1_0_REVEIL_CHAMBRE:

    $ day_id = 6
    $ current_day = 6
    $ current_period = "Matin"
    $ cafeteria_food_level = "low"

    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    pause 0.6

    think "Je me réveille avant l'annonce du matin. Pas besoin de Kami, cette fois."
    think "Le vote suffit à m'empêcher de dormir correctement."

    scene bg_chambre at adaptive_fullscreen with fade

    think "Dans quelques heures, nous devrons décider si les habitants peuvent franchir les frontières entre les districts."
    think "Enfin... décider est un bien grand mot."
    think "Sael a annoncé qu'elle voterait contre. Elle n'a laissé aucune place au doute."
    think "Une seule voix suffit. Le vote est déjà condamné, mais nous allons quand même devoir nous asseoir, débattre et faire semblant d'ignorer le résultat."

    pause 0.5

    think "Hier encore, nous avons fêté le retour du commerce et la fin des bons de rationnement."
    think "Les marchandises peuvent de nouveau circuler. Les gens, eux, resteront derrière leurs frontières."

    pause 0.4

    think "Je me lève. Rester ici ne rendra pas la journée plus courte."

    stop music fadeout 1.0

    scene bg_chambre at adaptive_fullscreen with dissolve

    think "Je m'habille rapidement et quitte ma chambre pour rejoindre la cafétéria."

    jump _6_1_0_CAFETERIA


label _6_1_0_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_J6_02
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    call play_stat_dialogue("d6_1_0") from _call_stat_dialogue_d6_1_0

    $ showGroup([
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("lysa", "blase"),
        ("noam", "neutre"),
        ("iris", "neutre"),
        ("tomas", "neutre"),
        ("elen", "joie"),
        ("julian", "sourire"),
        ("nyra", "neutre"),
        ("ryn", "fatigue"),
        ("sael", "neutre"),
    ])

    think "Tout le monde est déjà là. Pourtant, personne ne parle vraiment."
    think "Les couverts heurtent les assiettes. Les chaises grincent. Chaque bruit paraît plus fort que nécessaire."
    think "Ryn garde les yeux sur son plateau. Sael mange lentement, sans jamais regarder dans sa direction."

    pause 0.5

    goumi "Bon ! Puisque personne ne semble décidé à rendre ce petit déjeuner vivant, je vais m'en charger."
    goumi "Grâce au rétablissement du commerce, de nouveaux produits vont arriver dès les prochaines livraisons."
    goumi "Des fruits frais, du cacao, du café, plusieurs épices et même quelques produits dont j'avais oublié l'existence."

    elen joie "Attends, attends... du vrai cacao ? Pas la poudre triste qui colle au fond des tasses ?"

    goumi "Du vrai cacao. Et si les quantités suivent, je pourrai même refaire certains desserts."

    elen content "On a réussi ! Voilà ! C'est ça, le progrès !"
    elen joie "Je retire tout ce que j'ai pu dire de méchant sur le Conclave. Enfin, pas tout. Mais une partie raisonnable !"

    iris taquin "Tu viens officiellement de vendre tes convictions pour un gâteau au chocolat."

    elen content "Je ne les ai pas vendues. Je les ai échangées contre quelque chose de meilleur. C'est très différent."

    julian sourire "La libre circulation des marchandises trouve déjà sa première grande défenseuse."

    elen joie "Exactement ! Et demain je défendrai le café. Et après-demain les épices. Je suis très engagée politiquement."

    mara taquin "Une vision solide. On sent les années de réflexion."

    elen taquin "Moque-toi. Tu viendras pleurer quand Goumi refusera de te donner une deuxième part."

    pause 0.5

    think "Quelques sourires apparaissent autour de la table. Même Sael relève brièvement les yeux."
    think "Puis le silence revient. Il suffit que l'un de nous regarde Ryn pour que tout le monde se souvienne de ce qui nous attend."

    tomas hesitation "La livraison est prévue pour quand ?"

    goumi "Demain matin, normalement. Une capsule complète. Nourriture, médicaments, matériel et quelques commandes particulières."

    tomas neutre "D'accord. C'est... c'est une bonne nouvelle."

    lysa blase "Oui. Une excellente nouvelle."

    pause 0.5

    think "Personne n'ajoute que cette capsule traversera plusieurs frontières sans avoir à demander la permission."
    think "Personne ne demande pourquoi une caisse de cacao dispose d'une liberté que des millions de personnes n'ont pas."

    elias ecoute "Ça va nous changer des mêmes plats tous les jours. C'est déjà pas mal."

    kael calme "Et les médicaments supplémentaires seront utiles. Les stocks de l'infirmerie ne sont pas inépuisables."

    iris sourire "Pour une fois, je suis d'accord. Tout ce qui évite à Goumi de nous servir une nouvelle purée grise mérite d'être célébré."

    goumi "Je vous entends, vous savez."

    iris taquin "C'était le but."

    elen rire "Ah ! Je savais que ce petit déjeuner finirait bien !"

    pause 0.6

    think "Elen continue d'énumérer tout ce qu'elle voudrait manger. Julian l'aide à inventer des desserts impossibles."
    think "Les autres les écoutent ou font semblant. C'est plus facile que de parler du vote."

    noam hesitation "Vous avez tous bien dormi ?"

    nyra taquin "Tentative admirable. Transition catastrophique."

    noam sourire "Je fais ce que je peux."

    mara mefiant "On le voit."

    pause 0.4

    ryn fatigue "J'ai pas dormi."

    think "Sa voix coupe la conversation. Sael s'immobilise une seconde, puis reprend son repas."

    noam inquiet "Ryn..."

    ryn desaccord "Quoi ? Il a posé une question. Je réponds."

    sael neutre "Personne ne te le reproche."

    ryn colere "J'ai pas dit que quelqu'un me le reprochait."

    pause 0.5

    think "Le silence devient plus lourd encore. Elen baisse les yeux vers son assiette."

    lysa blase "On pourrait peut-être finir de manger sans commencer maintenant."

    ryn fatigue "Ouais. Bien sûr. On va attendre bien gentiment l'heure prévue."

    sael mefiant "C'est mieux."

    ryn colere2 "Évidemment que pour toi, c'est mieux."

    noam determine "Ryn. Pas ici."

    pause 0.4

    ryn desaccord "J'ai compris."

    think "Il repousse son plateau et se lève."

    ryn fatigue "J'ai plus faim."

    $ hideGroup()

    think "Ryn quitte la cafétéria sans regarder personne. Sael ne le suit pas des yeux."
    think "La discussion reprend quelques instants plus tard, mais personne ne retrouve vraiment le ton léger d'Elen."

    stop music fadeout 1.0

    think "La matinée s'étire. Nous avons encore quelques heures avant de nous retrouver dans la salle de repos."

    call START_FREE_TIME("_6_1_0_SALLE_REPOS") from _call_START_FREE_TIME_J6


label _6_1_0_SALLE_REPOS:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "repos1") from _call_MAYBE_PLAY_SCRIPTED_DOOR_24
    scene repos1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("elias", "neutre"),
        ("mara", "neutre"),
        ("lysa", "blase"),
        ("noam", "neutre"),
        ("iris", "fatigue"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("kael", "calme"),
        ("sael", "neutre"),
    ])

    think "Après mon temps libre, je rejoins plusieurs représentants dans la salle de repos."
    think "La télévision est éteinte. Elias et Sael terminent une partie de fléchettes pendant qu'Elen commente chaque lancer comme une compétition officielle."

    elen joie "Et maintenant, Sael va tenter le centre ! Une pression immense ! Une foule en délire !"

    sael neutre "Il n'y a pas de foule."

    elen taquin "Elle est dans ma tête. C'est une foule très exigeante."

    elias sourire "Elle est surtout bruyante."

    elen desaccord "Le public a le droit de s'exprimer. C'est la démocratie."

    mara taquin "Profites-en. Dans quelques heures, Kami risque de demander une autorisation pour les commentaires sportifs."

    sael reflechit "Le centre n'est pas toujours la meilleure cible."

    elias ecoute "Si tu veux gagner, si."

    sael raison "Si je vise le centre et que je manque, je perds tout. Si je vise une zone plus large, je garde des points."

    julian sourire "Je ne sais pas si elle parle encore des fléchettes."

    lysa blase "Elle ne parle plus des fléchettes depuis le début."

    pause 0.4

    think "Sael lance. La fléchette se plante loin du centre, mais dans une zone encore correcte."

    elias content "Tu joues vraiment comme ça ? Toujours le choix le moins risqué ?"

    sael neutre "Toujours le choix qui permet de rentrer vivant."

    pause 0.6

    think "Personne ne répond. La phrase pourrait ouvrir la discussion que nous évitons depuis ce matin."
    think "Elias récupère les fléchettes sans insister."

    iris fatigue "On s'est tous fait à l'idée, non ?"

    noam hesitation "À quelle idée ?"

    iris triste "Ne m'oblige pas à la formuler."

    kael calme "Le vote ne passera pas."

    pause 0.5

    think "Voilà. C'est dit. Personne ne proteste."

    mara neutre "Sael a été claire dès l'annonce. On peut débattre jusqu'à demain matin, ça ne changera rien."

    elen triste "C'est quand même nul."

    lysa blase "Analyse politique remarquable."

    elen desaccord "Je suis sérieuse. On vient de réussir à changer quelque chose et maintenant on sait déjà que la suite va échouer."

    pause 0.5

    sael fatigue "Vous pouvez parler devant moi."

    iris inquiet "Personne n'essaye de t'isoler, hein."

    sael mefiant "Vous évitez le sujet depuis ce matin. Ce n'est pas de la délicatesse. C'est de la peur."

    elias inquiet "On veut juste éviter que ça parte en vrille."

    sael neutre "Alors n'en parlez pas. Mais ne faites pas semblant de me protéger."

    pause 0.5

    think "Elle pose les fléchettes sur la table. Sa voix reste calme, mais la fatigue se lit dans son regard."

    noam neutre "Tu comptes rester ici jusqu'au débat ?"

    sael raison "Non. J'ai besoin de marcher."

    elen inquiet "Tu veux que quelqu'un vienne avec toi ?"

    sael sourire "Non. Merci."

    think "Sael quitte la salle de repos."
    hide sael with moveinleft

    pause 0.6

    julian triste "Vous pensez que Ryn va la laisser tranquille ?"

    mara mefiant "Non."

    noam determine "Je vais vérifier."

    iris inquiet "Noam, attends. Il est à cran depuis ce matin."

    noam neutre "Justement."

    lysa inquiet "Ne joue pas au héros. S'ils veulent parler, laisse-les parler. Tu interviens seulement si ça dégénère."

    noam determine "C'est ce que je compte faire."

    $ hideGroup()

    stop music fadeout 1.0

    jump _6_1_0_RYN_SAEL


label _6_1_0_RYN_SAEL:

    scene bg_dortoir at adaptive_fullscreen, j610_tension_push with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ showGroup([
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("noam", "inquiet"),
    ])

    think "Je les retrouve dans le dortoir, à quelques mètres de la porte de Sael."
    think "Ryn lui barre le passage. Sael garde les bras le long du corps, immobile."

    ryn colere "Tu vas vraiment faire ça ?"

    sael neutre "Je te l'ai déjà dit."

    ryn colere2 "Non. Tu l'as dit aux autres. Comme une putain d'annonce. Moi, tu m'as rien expliqué."

    sael mefiant "Tu ne veux pas d'explication. Tu veux que je change d'avis."

    ryn desaccord "Évidemment que je veux que tu changes d'avis !"

    sael raison "Alors cette conversation ne sert à rien."

    scene bg_cg036 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg036")

    ryn colere "Cette proposition, c'est moi qui l'ai déposée."

    pause 0.5

    think "Sael ne répond pas. Son expression change à peine, mais ses épaules se tendent."

    ryn determine "C'est moi qui ai demandé qu'on puisse traverser les frontières. Pas Tomas. Pas Noam. Moi."
    ryn colere "J'ai passé des années à regarder les gens crever à quelques mètres d'une limite qu'ils pouvaient même pas voir."
    ryn colere2 "J'ai creusé des tranchées pour les empêcher d'avancer. J'ai ramené ceux qui avaient encore assez de jambes pour revenir."
    ryn colere "Et maintenant qu'on a enfin une chance d'ouvrir cette saloperie de frontière, c'est toi qui vas tout bloquer."

    sael fatigue "Oui."

    ryn surpris "C'est tout ?"

    sael neutre "Tu savais déjà que la proposition venait de toi. Moi, non. Ça ne change pas ce qu'elle fera à Limen."

    ryn colere2 "Elle donnera une porte de sortie !"

    sael determine "Aux plus forts. Aux plus jeunes. À ceux que les autres districts accepteront d'utiliser."
    sael raison "Les malades resteront. Les vieux resteront. Les enfants dont personne ne veut resteront."
    sael mefiant "Tu n'ouvres pas Limen. Tu le vides de tous ceux qui peuvent encore le tenir debout."

    ryn desaccord "Tu décides à leur place."

    sael determine "Et toi, tu décides qu'ils survivront au passage parce que ça t'arrange d'y croire."

    pause 0.5

    ryn colere "Faut voter pour."

    sael neutre "Non."

    ryn colere2 "Faut voter pour, Sael. Je te le demanderai pas une troisième fois."

    sael mefiant "C'est une menace ?"

    ryn determine "Appelle ça comme tu veux. Si tu détruis cette chance, tout Limen saura qui l'a fait."
    ryn colere "Je dirai ton nom. Je dirai que t'as regardé la porte s'ouvrir et que tu l'as refermée sur eux."

    sael determine "Dis-le."

    ryn surpris "Quoi ?"

    sael determine "Dis mon nom. Dis-leur aussi le tien quand les premiers corps seront abandonnés dans les districts qui n'en veulent pas."

    ryn colere2 "Ferme-la."

    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("noam", "inquiet", 0.40),
    ])

    noam determine "Ça suffit."

    pause 0.4

    think "Je m'avance entre eux. Ryn tourne brusquement la tête vers moi."

    noam inquiet "Tu lui as dit ce que tu avais à dire. Maintenant, laisse-la passer."

    ryn colere "Dégage, Noam."

    noam determine "Non."

    ryn desaccord "Ça te regarde pas."

    noam raison "On va tous voter. Ça nous regarde tous."

    ryn colere2 "Vous avez déjà abandonné ! Depuis ce matin, vous mangez, vous jouez, vous attendez que ça tombe !"

    noam determine "Et la menacer va changer son vote ?"

    ryn colere "Au moins, je fais quelque chose !"

    noam colere "Tu lui bloques le passage et tu lui cries dessus. Tu ne fais rien pour les habitants de Limen."

    pause 0.4

    ryn colere2 "Écarte-toi."

    noam determine "Laisse-la partir."

    think "Ryn pose une main sur mon épaule et me pousse. Je recule d'un pas, puis reviens immédiatement devant lui."

    noam colere "Tu ne la toucheras pas."

    ryn colere2 "J'ai dit : écarte-toi !"

    think "Son poing part avant que j'aie le temps de bouger."

    stop music fadeout 0.25
    play sound "audio/sfx_heartbeat.mp3" fadein 0.2
    show expression Solid("#B3132ACC") as j610_hit_flash zorder 300 at j610_impact_flash
    with hpunch

    play sound sfx_thud

    think "Le coup me frappe en plein visage. Ma tête part sur le côté et ma mâchoire explose de douleur."
    think "Je heurte le mur avec l'épaule. Un goût métallique envahit ma bouche."

    hide j610_hit_flash
    stop sound fadeout 0.8
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2

    noam peur "Putain..."

    sael peur "Noam !"

    ryn surpris "Merde."

    pause 0.5

    think "Ryn fixe son poing comme s'il ne le reconnaissait plus."

    ryn inquiet "Je voulais... que tu bouges."

    noam desaccord "En me frappant ?"

    ryn fatigue "Putain ! J'en sais rien !"

    pause 0.4

    sael determine "C'est terminé."

    ryn inquiet "Sael..."

    sael desaccord "Non. Tu voulais que je t'écoute. Je t'ai écouté. Maintenant, tu vas t'écarter."

    think "Ryn baisse les bras et recule. Sael s'approche de moi."

    sael inquiet "Laisse-moi voir."

    noam inquiet "Ça va."

    ryn colere "Putain..."

    sael desaccord "Non. Ta lèvre est ouverte. Tu vas avoir un sacré bleu."

    noam colere "C'est pas ça qui me tuera, ça va aller."

    pause 0.5

    think "Des pas résonnent dans le couloir. Iris, Elias et Lysa arrivent depuis la salle de repos."

    $ showGroup([
        ("ryn", "triste"),
        ("sael", "inquiet"),
        ("noam", "inquiet"),
        ("iris", "colere"),
        ("elias", "inquiet"),
        ("lysa", "inquiet"),
    ])

    iris colere "Qu'est-ce qui s'est passé ?"

    lysa inquiet "Son visage répond déjà en partie à la question."

    elias colere "Ryn. Dis-moi que c'est pas toi."

    ryn fatigue "Foutez-moi la paix !"
    hide ryn with moveinleft
    pause 0.3

    iris colere "Mais t'es complètement malade ?!"

    sael determine "Nous devons aller au Conclave. Le débat va commencer d'une minute à l'autre."

    iris desaccord "Noam doit d'abord passer à l'infirmerie."

    noam inquiet "On n'a pas le temps. Et je peux marcher, c'est trois fois rien."

    iris colere "C'est pas parce que tu peux marcher que tout va bien."

    noam determine "Je vais assister au vote."

    lysa blase "Évidemment. Sinon cette journée risquerait de devenir raisonnable."

    $ hideGroup()

    stop music fadeout 1.0

    think "Nous partons vers la salle du Conclave. Chaque mouvement de ma mâchoire relance la douleur."

    jump _6_1_0_DEBAT


label _6_1_0_DEBAT:

    $ current_period = "Soir"

    scene bg_conclave at adaptive_fullscreen, j610_vote_breathe with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("elias", "colere"),
        ("mara", "colere"),
        ("lysa", "inquiet"),
        ("noam", "inquiet"),
        ("iris", "colere"),
        ("tomas", "inquiet"),
        ("elen", "choque"),
        ("julian", "inquietude"),
        ("kael", "inquietude"),
        ("nyra", "degout"),
        ("ryn", "triste"),
        ("sael", "determine"),
    ])

    think "À peine entrés, tous les regards se posent sur ma lèvre fendue et sur la marque qui commence à apparaître sur ma joue."

    elen choque "Noam ?! Qu'est-ce qui t'est arrivé ?"

    mara colere "Attends. Pourquoi Ryn a du sang sur la main ?"

    julian inquietude "Vous vous êtes battus ?"

    noam inquiet "Ce n'était pas une bagarre."

    nyra degout "Effectivement. Pour une bagarre, il faudrait que les deux personnes aient frappé."

    ryn triste "J'ai déconné."

    mara colere_noire "Tu as frappé Noam avant un vote décisif et ton résumé, c'est que tu as déconné ?"

    elias colere "Il a menacé Sael aussi."

    elen colere "Mais qu'est-ce qui te prend ?! On est tous tendus, ça te donne pas le droit de taper les gens !"

    ryn colere "Je sais ! Vous voulez que je dise quoi de plus ?"

    iris colere "Commence par arrêter de gueuler comme si c'était encore nous le problème."

    kael inquietude "Le vote était déjà compromis. Cette violence ne pouvait rien améliorer."

    ryn colere2 "Merci, Kael. Vraiment. J'avais besoin de ton analyse."

    nyra colere "Tu recommences."

    tomas inquiet "On devrait peut-être... enfin... laisser Noam s'asseoir avant de continuer."

    lysa opposition "On devrait surtout arrêter cette séance avant que quelqu'un décide de terminer le travail."

    noam determine "Ça suffit. Je vais bien."

    iris desaccord "Non, tu ne vas pas bien."

    noam inquiet "Je peux voter. C'est ce qui compte pour le moment."

    pause 0.5

    think "Ryn garde les yeux baissés. Sael regarde la salle, puis le siège vide devant elle."

    sael determine "Je vote contre. J'assume mes choix."

    "Sael nous regarde tous droit dans les yeux."

    call j601_sael_vote_animation from _call_j601_sael_vote_animation2

    pause 0.6

    think "Le silence tombe d'un seul coup."

    noam surpris "Sael..."

    sael neutre "Le débat est terminé. Une voix contre suffit. Il n'y a plus rien à obtenir ici."

    ryn inquiet "Tu fais ça à cause de moi ?"

    sael triste "Ma décision était prise avant aujourd'hui."

    pause 0.4

    sael determine "Ne lui en voulez pas. Ryn a juste voulu faire de son mieux. Si vous avez quelqu'un à qui vous en prendre, c'est moi."

    noam desaccord "Tu n'es pas responsable de ce qu'il a fait."

    sael fatigue "Je sais."

    think "Sael valide son vote sur le terminal, puis quitte son siège."

    sael neutre "Je n'ai plus rien à dire."

    $ hideGroup()

    think "La porte se referme derrière elle. Le vote est déjà perdu."

    play sound sfx_announce
    stop music fadeout 1.0

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Quoi ?! C'est tout ?!"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Une menace, un coup au visage, une salle entière prête à s'étriper... et vous interrompez déjà le débat ?"
    kami "J'avais préparé plusieurs angles de caméra. J'espérais des arguments, des larmes, peut-être même une seconde droite !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Vous pourriez faire un effort ! La démocratie mérite de meilleurs débats que cette catastrophe expédiée en quelques minutes."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Mais soit. Une représentante s'est exprimée. La démocratie a parlé !"
    kami "Son vote contre condamne déjà la proposition, mais les autres représentants doivent encore enregistrer leur choix."
    kami "Allez. Faites au moins semblant de prendre cette partie au sérieux."

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Mon terminal s'allume. Le résultat est déjà décidé, mais mon vote m'appartient encore."

    $ hideGroup()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None
    $ vote_phase3_amendment_override = "Autoriser les habitants à traverser les frontières entre les districts."

    stop music fadeout 0.8
    $ _j610_vote_result = renpy.call_screen("vote_screen")
    $ j6_noam_vote = {"pour": "for", "contre": "against", "abstention": "abstain"}.get(vote_phase3_player_choice, "abstain")

    if j6_noam_vote == "for":
        scene black
        show expression Solid("#0AFF8844") as j610_vote_confirmation
        with Dissolve(0.12)
        noam determine "Je vote pour."
    elif j6_noam_vote == "against":
        scene black
        show expression Solid("#FF2A2A44") as j610_vote_confirmation
        with Dissolve(0.12)
        noam raison "Je vote contre."
    else:
        scene black
        show expression Solid("#F2B63E33") as j610_vote_confirmation
        with Dissolve(0.12)
        noam hesitation "Je m'abstiens."

    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None
    $ vote_phase3_results = [
        ("Ryn", "pour"),
        ("Julian", "pour"),
        ("Nyra", "pour"),
        ("Kael", "pour"),
        ("Mara", "pour"),
        ("Lysa", "pour"),
        ("Iris", "pour"),
        ("Elen", "pour"),
        ("Elias", "abstention"),
        ("Tomas", "abstention"),
        ("Sael", "contre"),
        ("Noam", vote_phase3_player_choice if vote_phase3_player_choice in ("pour", "contre", "abstention") else "abstention"),
    ]
    $ renpy.random.shuffle(vote_phase3_results)
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")
    $ vote_phase3_amendment_override = None

    pause 0.8

    play sound sfx_announce
    pause 1.0
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    if j6_noam_vote == "against":
        kami "Résultat définitif : huit voix pour, deux abstentions et deux voix contre."
        scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
        kami "Deux refus ! Sael n'était donc pas la seule à vouloir refermer la porte. Comme c'est intéressant."
    elif j6_noam_vote == "abstain":
        kami "Résultat définitif : huit voix pour, trois abstentions et une voix contre."
        scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
        kami "Une seule voix contre. Une toute petite voix, et pourtant des frontières bien solides."
    else:
        kami "Résultat définitif : neuf voix pour, deux abstentions et une voix contre."
        scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
        kami "Neuf voix favorables contre une seule opposition. Presque une victoire... ce qui signifie exactement un échec."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "La proposition est rejetée. Les déplacements entre les districts restent soumis à une autorisation stricte."
    kami "Les marchandises continueront de circuler. Les habitants, eux, resteront gentiment à leur place."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Félicitations pour cette magnifique démonstration démocratique ! Essayez seulement de ne pas vous frapper avant le prochain vote."

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    jump _6_1_0_FIN


label _6_1_0_FIN:

    scene bg_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Je retourne vers ma chambre. Ma lèvre me brûle et ma mâchoire lance à chacun de mes pas."
    think "Les marchandises pourront franchir les frontières. Les personnes, non."
    think "Ryn a frappé pour ouvrir une porte. Sael l'a refermée pour empêcher Limen de se vider."
    think "Et moi, je ne sais même plus lequel des deux avait le plus peur."

    pause 0.6

    think "Demain matin, une nouvelle livraison doit atteindre le Conclave."
    think "De la nourriture, des médicaments, du matériel. Rien qui soit censé respirer."

    stop music fadeout 1.0
    scene black with fade

    pause 1.4

    $ kami_grant_chapter_2_reward()

    call show_chapter_title("Fin du chapitre 2_1", "Le prix du oui") from _call_show_chapter_title_610

    pause 1.0

    call end_day("7") from _call_end_day_610
    # Les deux routes du chapitre rejoignent la même chronologie au jour 7.
    jump _7_1_0_CANON

# Durée : 8m
# Total J0-J6 : 1h57
