# =============================================================================
# JOUR 22 — Route 0_1_1_0_0
# Le Conclave a été prolongé jusqu'au jour 30.
# Elias est remplacé hors champ par son double au cours de la journée.
# =============================================================================

default j22_elias_replaced = False
default j22_vote_announced = False

label _22_0_1_1_0_0_REVEIL:
    $ cafeteria_food_level = "null"
    $ current_day = 22
    $ day_id = 22
    $ current_period = "Matin"
    $ noam_has_juliette_drawing = False

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Quand j'ouvre les yeux, je vois d'abord mon sac contre le bureau."

    "Hier, j'étais persuadé que je ne dormirais plus ici. Ma tablette affiche maintenant le jour vingt-deux. Encore huit nuits."

    "Je regarde la grille d'aération. Elias a percé jusque tard ; certaines chambres sont refermées, d'autres attendent encore leurs plaques de fortune."

    think "Au moins il s'en occupe."

    "Je prends un tee-shirt propre dans mon sac, puis je le referme. Je ne suis toujours pas prêt à le défaire."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j22_stay_door_chambre
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Dans le couloir, plusieurs sacs attendent encore près des portes. Je ne suis pas le seul à rester prêt à partir."

    # Durée : ~1m00
    # Total : ~1m00


label _22_0_1_1_0_0_CAFETERIA:
    call KD_ROUTE_J22_NYRA from _call_optional_kd_route_j22_nyra
    call START_EXPLORATION_LIBRE("_22_0_1_1_0_0_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_nav_j22_cafeteria

label _22_0_1_1_0_0_CAFETERIA_ARRIVEE:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est déjà presque pleine. Je prends quelque chose à manger et m'installe là où il reste de la place."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("elias", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    elen content "J'ai pris trop de pain. Servez-vous avant que je décide que c'était volontaire."

    mara taquin "Tu vois, Noam ? Elle dit bonjour et elle nourrit les gens. Toi, t'arrives avec ta tête de revenant."

    noam fatigue "Bonjour, Mara."

    mara sourire "Voilà. On progresse."

    iris fatigue "Laisse-le manger."

    mara taquin "Je vérifie juste s'il a encore vu une morte dans les murs."

    noam blase "Rien cette nuit. Merci de demander."

    sael neutre "S'il recommence à entendre des choses, on pourra refaire le rite."

    noam panne "Non."

    "Mara étouffe un rire dans sa tasse."

    noam colere "La dernière fois, Ryn m'a coincé contre un mur pendant que tu me jetais du sel dessus."

    sael raison "Je n'avais pas demandé à Ryn de te coincer."

    noam colere "C'est vraiment le détail que tu retiens ?"

    tomas hesitation "Pour être juste, un deuxième rite apporterait difficilement une information nouvelle."

    noam fatigue "Merci, Tomas."

    sael neutre "Je proposais. Je ne t'oblige pas."

    iris blase "Voilà. Personne ne l'exorcise avant qu'il ait fini son café."

    noam inquiet "Ni après."

    mara taquin "On verra comment se passe la journée."

    noam colere "Toi, t'aides pas."

    "Iris sourit malgré elle, puis reprend un ton plus sérieux."

    iris reflexion "Par contre, la salle derrière les conduits existe. Et il y avait du matériel de maintenance dedans."

    "Elias relève la tête."

    iris reflexion "Du matériel qui avait déjà disparu, si je me souviens bien."

    elias ecoute "Les outils que je cherchais il y a dix jours."

    tomas reflexion "Ceux que tu pensais avoir perdus ?"

    elias colere "Je les avais pas perdus. Ils avaient disparu."

    iris fatigue "C'est précisément ce que je viens de dire."

    noam reflexion "Les plaques d'hier pourraient être là-bas."

    "Elias ne répond pas tout de suite. Il regarde les trois gobelets près de son plateau."

    elias fatigue "Peut-être. Mais je vais d'abord finir les protections. Si je commence à ramper dans les conduits, j'y passe la journée."

    iris reflexion "Avec les plaques de fortune ?"

    elias fatigue "Ouais. J'ai récupéré de quoi bricoler jusque tard hier."

    noam inquiet "T'as dormi combien de temps ?"

    elias fatigue "Assez."

    iris blase "Donc trois heures."

    elias colere "J'ai un truc à finir. Le café tient le reste."

    noam reflexion "Je viens avec toi ?"

    elias fatigue "Non. J'ai besoin d'aller vite et tu poses une question toutes les trente secondes."

    noam taquin "C'est faux."

    elias fatigue "Tu viens d'en poser deux."

    "Il prend sa caisse à outils et part avant que je trouve quoi répondre."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    "Je le regarde sortir. Mara attend deux secondes avant de reprendre. Un record."

    mara taquin "Bon. Maintenant qu'on a réglé les fantômes, on peut parler d'un sujet agréable ?"

    noam blase "Non."

    mara taquin "Tu vois, Iris ? Il me brise le cœur sans même demander le sujet."

    iris blase "Je vais pleurer."

    $ j22_elias_replaced = True

    $ hideGroup()

    # Durée : ~5m20
    # Total : ~6m20


label _22_0_1_1_0_0_MIDI:
    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Après le repas, je repasse par les dortoirs. Pas de perceuse. Le couloir est silencieux."

    "Deux plaques de fortune sont toujours appuyées contre le mur, exactement là où on les avait laissées hier."

    think "Il a dû commencer ailleurs."

    "Je ralentis devant sa chambre, puis je continue. Elias passe sa vie entre la maintenance, le stockage et les couloirs. Il peut être n'importe où."

    scene black with dissolve
    pause 0.4

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Quand je reviens à la cafétéria, Elen est assise sur son sac pendant que Julian essaie de le refermer pour elle."

    $ showGroup([
        ("elen", "content", 0.24),
        ("julian", "sourire", 0.50),
        ("noam", "neutre", 0.76),
    ])

    elen hesitation "Je crois que j'ai fait une erreur."

    noam blase "Tu l'as ouvert."

    elen joie "Oui."

    julian sourire "Nous découvrons une vérité terrible : ce sac était fermé grâce à une technologie que nous ne maîtrisons pas."

    elen colere "Arrête de parler et appuie."

    julian sourire "J'appuie."

    elen colere "Plus."

    julian fatigue "Je suis littéralement dessus."

    noam taquin "Vous avez besoin d'aide ?"

    elen joie "Oui."

    julian sourire "Non."

    "Je m'approche quand même. À trois, on finit par fermer la fermeture éclair, et Elen récupère son sac avec un soupir de soulagement."

    elen content "Voilà. Je touche plus à rien jusqu'au départ."

    noam reflexion "Le départ est dans huit jours."

    elen determine "Je laverai des trucs à la main."

    julian sourire "Ça, c'est de la conviction."

    noam reflexion "Toi non plus t'as pas défait le tien ?"

    julian sourire "Évidemment que non. Si Kami change encore d'avis demain, je veux pouvoir courir au sas avant qu'elle ait le temps de réfléchir."

    elen taquin "Elle réfléchit plus vite que toi."

    julian blase "Merci Elen."

    elen inquiet "Attendez. Et si Kami nous annonce encore une mauvaise nouvelle avant le départ ?"
    julian sourire "Nous l'affronterons avec dignité."
    noam taquin "Tu veux dire avec ta valise déjà prête ?"
    julian sourire "La dignité n'interdit pas d'être organisé."
    elen joie "Alors moi aussi, je suis digne !"
    "Elle tire sur la poignée de son sac. La fermeture éclair s'ouvre d'un coup et un vêtement tombe à mes pieds."
    julian fatigue "Je retire ce que j'ai dit."
    elen colere "HÉ ! C'est toi qui as mal fermé !"
    noam taquin "Je vous laisse régler ça entre grands professionnels du départ."
    "En quittant la pièce, j'entends Julian accuser la fermeture éclair."

    $ hideGroup()

    # Temps libre : Noam dispose d'un moment pour voir un représentant
    # avant que les préparatifs du retour ne reprennent.
    $ current_period = "Après-midi"
    "Il me reste un peu de temps avant que les autres reprennent leurs préparatifs. Autant en profiter pour voir quelqu'un."
    call START_FREE_TIME("_22_0_1_1_0_0_ELIAS_REVIENT") from _call_START_FREE_TIME_J22_DOPPELGANGER

    # Durée : ~2m10 hors temps libre
    # Total : ~8m20 hors temps libre


label _22_0_1_1_0_0_ELIAS_REVIENT:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Je retrouve Elias plus tard. Il arrive avec sa caisse à outils et deux plaques de fortune sous le bras."

    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "neutre", 0.65),
    ])

    noam taquin "Ah, t'étais là. J'allais finir par croire que t'avais démonté un mur entier."

    elias fatigue "J'ai essayé un truc. Ça marche pas."

    noam reflexion "Les plaques ?"

    elias fatigue "Ouais. Celles qu'on a bricolées hier, c'est de la merde."

    noam reflexion "Hier tu disais que ça tiendrait."

    elias fatigue "Hier, je voulais que ça tienne. C'est pas pareil."
    noam taquin "Tu pourrais au moins mettre une étiquette. « Protection provisoire, ne pas croire à la protection. »"
    elias fatigue "Très drôle."
    noam fatigue "Je plaisante pas vraiment."
    elias colere "Justement. Si vous vous faites avoir à cause d'un truc que j'ai fabriqué, c'est moi qui vais y penser toutes les nuits."
    noam inquiet "Elias..."
    elias fatigue "Alors non, je vais pas signer au marqueur « c'est bon » sur un morceau de ferraille. Même si ça m'arrangerait."

    "Il pose les deux morceaux de métal contre le mur avec un bruit sec."

    $ hideGroup()
    $ unlock_gallery_image("bg_cg060")
    scene bg_cg060 at adaptive_fullscreen with dissolve

    elias raison "Regarde. Rien qu'en tirant là..."
    "Il attrape le bord de la plaque et secoue la fixation. Un cliquetis sec retentit."
    noam surpris "C'est censé bouger autant ?"
    elias fatigue "Non."
    "Il tire une nouvelle fois. L'attache lâche et la plaque bascule contre sa jambe."
    elias colere "PUTAIN !"
    call kd_vn_reaction("elias", "colere", "#ff9c55")
    noam inquiet "Ça va ?"
    elias fatigue "Ouais. Tu vois ? C'est de la merde."
    noam desaccord "On peut en mettre deux."
    elias colere "Deux plaques tenues par les mêmes vis ? Ça fera juste deux plaques sur ma jambe."
    "Je regarde le morceau de métal. Hier encore, j'étais convaincu qu'il suffirait."
    noam fatigue "Donc on dort avec une fausse protection."
    elias fatigue "C'est exactement ce que je refuse. Je remets les grilles normales."
    noam inquiet "Et les vraies plaques ?"
    elias raison "Livraison du jour vingt-huit. Six jours."
    noam surpris "Six jours ? Et il nous restera deux jours avant le départ."
    elias fatigue "Je sais. C'est pour ça que j'en ai marre de bricoler."
    "Il ramasse la fixation cassée et la glisse dans sa poche."


    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "inquiet", 0.65),
    ])

    noam reflexion "Et celles qui ont disparu ?"

    elias fatigue "Toujours rien. J'ai regardé vite fait."

    noam reflexion "Même dans la salle dont Iris parlait ce matin ?"

    "Il s'arrête une fraction de seconde."

    elias neutre "J'y suis pas allé."

    noam surpris "Ah."

    call play_stat_dialogue("j22") from _call_play_stat_dialogue_1

    elias fatigue "J'ai pas envie de ramper dans vos conduits pour six bouts de métal. J'ai déjà perdu assez de temps."

    "Hier, les plaques disparues l'empêchaient presque de dormir. Aujourd'hui, il a surtout l'air d'en avoir marre."

    noam fatigue "D'accord."

    elias neutre "Je vais enlever celles déjà posées avant que quelqu'un compte dessus pour rien."

    noam reflexion "Tu veux de l'aide ?"

    elias fatigue "Non. C'est pas contre toi. Je finis ça seul et je passe à autre chose."

    noam neutre "Ça marche."

    "Il reprend les plaques et repart."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    "Je le laisse faire. Sa décision m'agace, mais je ne vais pas me battre avec lui sur des fixations qu'il connaît mieux que moi."

    think "Jour vingt-huit."

    "Je regarde ma grille un instant, puis je rentre."

    $ hideGroup()

    # Durée : ~3m20
    # Total : ~11m40


label _22_0_1_1_0_0_ANNONCE_VOTE:
    call KD_EXTRA_J22_TOMAS from _call_kd_extra_j22_tomas
    $ current_period = "Après-midi"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "En milieu d'après-midi, tout le monde finit à la cafétéria sans l'avoir décidé. Ryn et Nyra parlent encore de la prolongation. Mara vole dans le dessert d'Elen. Julian occupe une moitié de table avec son téléphone."

    $ showGroup([
        ("ryn", "neutre"),
        ("nyra", "neutre"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("iris", "blase"),
        ("elias", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("tomas", "reflexion"),
        ("noam", "neutre"),
    ])

    ryn colere "Ce qui me gonfle, c'est pas juste qu'on reste. C'est que quelqu'un a demandé ça et que depuis hier tout le monde fait comme si de rien n'était."

    nyra raison "Ryn, si tu as une piste, donne-la-nous. Sinon je ne vais pas te laisser transformer chaque petit-déjeuner en interrogatoire."

    ryn fatigue "J'en sais rien. Mais attendre neuf jours en se regardant de travers, ça va être sympa."

    mara taquin "Moi, ça me va. Il y en a quelques-uns que j'aime bien regarder."

    iris blase "Évidemment."

    mara taquin "Je t'ai pas exclue."

    iris colere "J'ai rien demandé."

    "Ryn lève les yeux au ciel. Le signal de diffusion l'empêche de répondre."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Bon ! Puisque vous avez gagné quelques jours supplémentaires avec moi..."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Autant les rentabiliser."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le prochain amendement vient d'être tiré au sort."

    $ j22_vote_announced = True

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Et j'avoue être presque déçue."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Il propose d'ajouter un nouveau Commandement : toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui. Un toit. De l'eau. À manger."
    kami "Je vous laisse deux jours pour trouver le moyen de vous disputer là-dessus. Je crois en vous."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vote au jour vingt-quatre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    # Après une diffusion, la commande scene a effacé les sprites : réafficher
    # le groupe avant toute reprise de dialogue collectif.
    $ showGroup([
        ("ryn", "neutre"),
        ("nyra", "neutre"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("iris", "blase"),
        ("elias", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("tomas", "reflexion"),
        ("noam", "neutre"),
    ])

    pause 0.4

    elen joie "Oh ! Bah... oui. Oui, évidemment !"

    ryn reflexion "Ouais. Là, je vois même pas ce qu'on est censés discuter."

    sael raison "Un toit, de l'eau, à manger. C'est le minimum."

    mara taquin "Le toit, je prends. Pour l'eau, j'aimerais négocier une option vin."

    iris blase "Même là, tu négocies l'alcool."

    mara sourire "Je défends mes priorités."

    tomas reflexion "Il faudra lire la formulation complète. 'Alimentation suffisante', juridiquement, ça peut vouloir dire plusieurs—"

    "Il s'interrompt en voyant les regards autour de la table."

    tomas hesitation "Mais le principe est évident. Oui. Je suis pour le principe."

    nyra raison "Sur le principe, je suis pour. Mais demain, je veux qu'on lise le texte avant de s'engager. On sait déjà ce que Kami peut faire avec une formulation vague."

    "Julian sourit déjà."

    julian joie "Enfin ! Une proposition sur laquelle on peut tous tomber d'accord !"
    call kd_vn_reaction("julian", "joie", "#ffd35a")
    "Il se lève."
    julian joie "On devrait préparer une intervention commune. Quelque chose de propre."
    iris blase "Une campagne pour convaincre qui ? On est déjà tous d'accord."
    julian sourire "C'est le moment de montrer qu'on sait travailler ensemble."
    mara taquin "Ou le moment de faire une jolie photo avec Julian au milieu."
    julian fatigue "Mara, je parle d'un vote qui peut donner un toit et de quoi manger à tout le monde."
    elen joie "Moi je veux bien préparer quelque chose. Une petite fête si on réussit ?"
    ryn sourire "Pour une fois, je vais pas dire non."
    tomas hesitation "Je veux quand même relire la formulation demain."
    "Le sourire de Julian se contracte."
    julian fatigue "Oui. Évidemment. Mais tu es pour, hein ?"
    tomas reflexion "Pour le principe, oui."
    julian sourire "Parfait. Donc, presque unanime."
    nyra raison "Julian, ne compte pas encore les voix. On vient justement de dire qu'on attendrait le texte."
    julian fatigue "Vous pourriez me laisser être content au moins dix secondes ?"
    noam taquin "On a dépassé les dix secondes."
    julian fatigue "Noam, je te déteste."


    "Il attrape son téléphone."
    julian sourire "Je vais préparer un slogan."
    iris blase "Tu sais que personne t'a demandé de faire campagne ?"
    julian joie "Pour une fois qu'on peut défendre quelque chose ensemble."
    mara taquin "Quoi, celle d'imprimer ton visage sur un mur ?"
    julian fatigue "Tu peux arrêter deux secondes ?"
    elen joie "Moi, j'aime bien « Un toit, de l'eau, à manger » !"
    iris blase "C'est littéralement le texte."
    julian sourire "Et c'est pour ça qu'il est bon."
    "Il note la phrase. Même Ryn sourit."

    "Elias n'a presque rien dit. Quand je me tourne vers lui, il hausse seulement une épaule."

    noam reflexion "T'en penses quoi ?"

    elias fatigue "Que c'est bien. Franchement, y'a quoi à ajouter ? Si les gens ont pas de toit, pas d'eau ou rien à bouffer, c'est qu'on a déjà merdé quelque part."

    noam neutre "Ouais."

    "Il reprend sa boisson. Personne ne demande qui a déposé l'amendement."

    "Julian essaie déjà de convaincre Elen de l'aider à fabriquer des affiches. Elle accepte avant même qu'il ait fini."

    $ hideGroup()

    # Durée : ~5m30
    # Total : ~17m10

label _22_0_1_1_0_0_FIN_JOURNEE:
    $ current_period = "Soir"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "En rentrant, je regarde immédiatement la grille. La plaque de fortune a disparu. Elias a tenu parole."

    "Je remets le bureau devant l'ouverture. Le meuble racle le sol et se coince contre le mur."

    think "La prochaine livraison arrivera au jour vingt-huit."

    "Six jours à faire ça."

    "Je m'assois sur le lit et retire mes chaussures."

    "Pas de grosse dispute aujourd'hui. Pas de nouvelle découverte impossible. Même le prochain vote a l'air simple."

    "Je repense quand même à Elias. Hier, il refusait de lâcher l'affaire. Aujourd'hui, il veut passer à autre chose."

    "Il a travaillé toute la nuit avec du matériel inadapté. Il a le droit d'en avoir marre."

    think "Arrête de chercher un problème partout."

    "Je m'allonge et tire la couverture."

    "Demain, il faudra probablement écouter Julian transformer trois lignes d'amendement en campagne nationale."

    noam fatigue "Génial..."

    "Je ferme les yeux."

    stop music fadeout 1.5

    call end_day("23", sleeping=True) from _call_j22_stay_end_day_23
    jump _23_0_1_1_0_0_REVEIL

    # Durée : ~1m30
    # Total : ~20m30
