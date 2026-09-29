label _19_0_1_1_0_REVEIL_CHAMBRE:

    $ current_period = "Nuit"

    $ cafeteria_food_level = "null"
    $ current_day = 19
    $ noam_has_juliette_drawing = False

    scene black
    play music "music/bgm_cold_metadata.mp3" fadein 2.0

    "Je ne sais pas combien de temps j'ai dormi."
    "Une heure, peut-être deux. Pas davantage."

    play sound "audio/sfx_duct_scrape.wav" volume 0.62

    "Un frottement métallique me tire encore une fois du sommeil."

    noam peur "..."

    "Je reste parfaitement immobile, les yeux ouverts dans le noir. Mon premier réflexe est de regarder le bureau devant la grille d'aération."
    "Il n'a pas bougé."

    pause 1.0

    "Le bruit revient, beaucoup plus loin cette fois. Quelque chose glisse contre la tôle puis s'arrête, comme si le réseau entier retenait son souffle avec moi."

    think "C'est peut-être juste le métal qui travaille."
    think "Ou un Goumi."
    think "Ou rien du tout."

    "Je ferme les yeux et essaie de me rendormir."

    pause 1.5

    play sound "audio/sfx_duct_scrape.wav" volume 0.72

    "Le même bruit recommence."

    noam colere "Putain..."

    "Je me redresse et garde les yeux fixés sur la grille pendant un long moment. Rien ne bouge. Rien ne dépasse. Pourtant je n'arrive plus à détourner le regard."

    think "Demain, Elias condamne ça."
    think "Je m'en fous si j'ai moins d'air. Je veux juste un mur."

    scene black with dissolve
    pause 1.0

    $ current_period = "Matin"
    scene bg_chambre at adaptive_fullscreen with fade

    "Quand je me réveille pour de bon, j'ai l'impression de ne pas avoir fermé l'œil. Ma nuque me fait mal et j'ai cette sensation désagréable d'avoir passé toute la nuit à attendre quelque chose qui n'est jamais venu."

    noam inquiet "Super..."

    "Je pousse le bureau pour libérer la grille et passe mes doigts sur les vis. Elles sont toujours à leur place."

    think "Donc personne n'est entré."

    pause 0.5

    think "Ou alors personne n'a eu besoin d'entrer."

    noam panne "..."

    "Je retire ma main."

    noam colere "Arrête."

    "Je parle tout seul maintenant. Parfait."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j19_chambre_exit
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je sors avec une seule idée en tête : trouver Elias avant qu'il ne disparaisse encore je ne sais où."

    "Je n'ai fait que quelques mètres lorsque j'aperçois Mara au bout du couloir. Elle avance tranquillement dans ma direction avec une tasse à la main."

    $ showGroup([
        ("noam", "fatigue", 0.28),
        ("mara", "neutre", 0.72),
    ])

    mara "Putain, t'as une tête affreuse."

    noam inquiet "Merci."

    mara taquin "Avec plaisir. J'allais dire que t'avais l'air d'avoir passé la nuit dans un mur, mais ça aurait été un peu trop facile."

    "Je la regarde quelques secondes."

    noam "Justement, il faut que je te parle de ça."

    mara "De quoi ?"

    noam reflexion "Du réseau."

    mara "Quel réseau ?"

    "Je fronce les sourcils."

    noam "Les conduits. Hier."

    mara reflexion "..."

    noam "La salle avec les Goumi. La branche qu'on n'a pas explorée."

    "Le sourire de Mara disparaît lentement."

    mara mefiant "Noam... de quoi tu parles ?"

    noam hesitation "Arrête."

    mara colere "J'arrête quoi ?"

    noam "On a passé la moitié de la nuit là-dedans tous les deux."

    mara stress "Pardon ?!"

    "Sa voix résonne dans tout le couloir. Deux portes s'ouvrent presque immédiatement plus loin."

    mara colere "Tu viens de dire quoi ?!"

    noam inquiet "Mara, baisse d'un ton."

    mara colere "Non mais attends, tu veux me faire croire que t'es allé te balader derrière les chambres cette nuit ?!"

    noam "Avec toi !"

    mara colere_noire "Mais j'étais pas avec toi !"

    $ investigation_add("mara_exploration", notify=False)
    $ investigation_add("mara_nie")
    call objection_protocol_run("Je n'étais pas avec toi hier soir.", "mara_exploration", ("conduits_chambres", "salle_goumi")) from _call_objection_mara_j19
    $ j19_mara_objection = _return
    if j19_mara_objection[1] == "correct":
        $ interject("CONTRADICTION", color="#5CD3FF")
        think "Mon souvenir est précis. Le tournevis, sa manche accrochée à la grille, sa voix derrière moi. Et pourtant elle a l'air aussi certaine que moi."
    elif j19_mara_objection[1] == "insufficient":
        think "Ça prouve que le réseau existe. Pas que Mara y était avec moi."
    elif j19_mara_objection[1] == "wrong":
        think "Non. Cet élément n'a rien à voir avec ce qu'elle vient de nier."
    else:
        think "Je laisse passer la phrase. Les deux versions restent là, impossibles à superposer."

    noam panne "..."

    "Je la fixe. Elle ne sourit pas. Elle n'a pas l'air de jouer."

    mara colere "J'étais dans ma chambre, espèce de taré !"

    noam inquiet "Non. Tu es venue me rejoindre dans le conduit. Tu m'as dit que t'avais pas trouvé Elias."

    mara "Je suis jamais allée chercher Elias !"

    "Le silence tombe entre nous."

    noam panne "..."

    mara mefiant "Attends..."
    mara mefiant "Quand tu dis 'derrière les chambres'..."

    "Elle pointe lentement du doigt le mur à côté de nous."

    mara "Tu veux dire qu'il y a vraiment un passage là-dedans ?"

    noam hesitation "Oui."

    mara stress "Et ça donne sur quoi ?"

    noam "Sur toutes les chambres. Enfin... pas seulement. On peut rejoindre une bonne partie du Conclave."

    mara stress "QUOI ?!"

    "Une troisième porte s'ouvre. Cette fois, c'est Iris qui apparaît, visiblement ravie d'avoir été réveillée par nos cris."

    iris colere "Vous pouvez pas vous engueuler moins fort ?!"

    mara colere "Non ! Parce que monsieur vient de m'apprendre qu'il peut passer derrière ma chambre par les murs !"

    iris panne "..."

    iris colere "PARDON ?!"

    noam desaccord "C'est pas du tout ce que j'ai dit."

    mara "C'est exactement ce que t'as dit !"

    noam "J'ai dit que le réseau dessert toutes les chambres !"

    iris colere "C'est pire !"

    "À ce stade, plusieurs personnes sont déjà sorties de leur chambre."

    noam colere "Super."

    mara colere "Non, justement. Tout le monde doit savoir ça."

    noam "Mara—"

    mara "Oh non. Là tu vas tout expliquer."

    $ hideGroup()

    jump _19_0_1_1_RESEAU_PUBLIC


label _19_0_1_1_RESEAU_PUBLIC:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_tense_meeting.mp3" fadein 2.0

    "Dix minutes plus tard, toute la cafétéria est au courant."
    "Je suis debout près d'une table, avec onze paires d'yeux braquées sur moi et la très désagréable impression d'être en train de plaider ma cause devant un tribunal improvisé."

    $ showGroup([
        ("noam", "inquiet", -0.10),
        ("lysa", "blase", 0.01),
        ("ryn", "colere", 0.12),
        ("mara", "colere", 0.23),
        ("tomas", "reflechit", 0.34),
        ("elen", "inquiet", 0.45),
        ("julian", "surpris", 0.56),
        ("iris", "colere", 0.67),
        ("nyra", "neutre", 0.78),
        ("kael", "inquietude", 0.89),
        ("elias", "inquiet", 1.00),
        ("sael", "mefiant", 1.11),
    ])

    ryn colere "Donc attends, je résume."
    ryn colere "Il y a un passage derrière nos chambres. Tu peux ramper dedans. Et tu peux aller d'une chambre à l'autre sans passer par le couloir."

    noam raison "Oui."

    iris colere "Et tu pensais nous prévenir quand ? Après avoir fini la visite guidée ?!"

    noam colere "Je l'ai découvert hier !"

    mara colere "Avec moi, apparemment."

    noam desaccord "Je sais ce que j'ai vu."

    mara "Et moi je sais où j'étais !"

    julian hesitation "On peut peut-être éviter de transformer ça en procès matrimonial avant d'avoir compris ce qu'il se passe ?"

    mara colere "Il n'y a aucun mariage ici, merci beaucoup."

    lysa blase "Dommage. J'aurais bien aimé voir la cérémonie dans les conduits."

    noam "Très drôle."

    elen inquiet "Mais du coup... quelqu'un peut vraiment venir dans nos chambres ?"

    "La question coupe immédiatement les plaisanteries."

    elias ecoute "Si les grilles donnent directement sur le réseau, oui."

    iris colere "Génial. Vraiment génial."

    sael mefiant "Tu as vu quelqu'un l'utiliser ?"

    noam hesitation "Non."

    ryn "T'as entendu quelque chose ?"

    noam "Oui. Plusieurs fois."

    elias inquiet "Cette nuit aussi ?"

    noam "Oui."

    "Elias croise les bras et regarde la ventilation au-dessus de la cafétéria comme s'il découvrait soudain qu'elle pouvait l'observer."

    tomas reflechit "Attends. Je veux revenir sur un point."

    noam "Lequel ?"

    tomas "Tu as dit que le réseau ne dessert pas uniquement les chambres."

    noam "Non. Il traverse une grande partie du Conclave."

    nyra raison "Quelles zones ?"

    noam reflexion "Je peux pas te faire une carte exacte. On a reconnu les dortoirs, la cafétéria, plusieurs couloirs... et une salle qu'on ne connaissait pas."

    elias "Quelle salle ?"

    noam "Une zone de maintenance. Il y avait deux Goumi à l'intérieur."

    elias surpris "Deux Goumi ?"

    noam "Un presque entier et un autre démonté."

    elias ecoute "Donc ils passent probablement par ce réseau pour leur entretien."

    tomas raison "Ce qui expliquerait son existence sans expliquer pourquoi il est accessible depuis toutes nos chambres."

    lysa blase "Tu veux dire qu'une réponse soulève encore plus de questions ? Quelle surprise."

    kael inquietude "Et les caméras ?"

    "Tout le monde tourne légèrement la tête vers lui."

    kael "Il y en a dans les conduits ?"

    noam "J'en ai pas vu."

    kael "Donc on peut circuler là-dedans sans être vu."

    nyra neutre "On ne sait pas ça."

    kael "Tu viens de l'entendre. Il n'a vu aucune caméra."

    nyra raison "Ne pas en voir ne veut pas dire qu'il n'y en a pas."

    kael inquietude "Ça ne veut pas dire qu'il y en a non plus."

    "Il regarde autour de lui, de plus en plus tendu."

    kael "On devrait fermer toutes les grilles maintenant."

    iris colere "Pour une fois, je suis d'accord."

    mara "Moi aussi. Et on commence par les chambres des filles."

    noam surpris "Pourquoi les filles ?"

    mara colere "Tu poses vraiment la question ?"

    noam "Parce que j'entends les mêmes bruits que vous !"

    mara "Oui, mais toi t'as déjà fait le tour du propriétaire !"

    noam colere "J'ai pas espionné qui que ce soit !"

    iris colere "Noam, même si t'as rien fait, tu comprends quand même que c'est légèrement inquiétant ?"

    noam "Oui. Justement. C'est pour ça que je veux qu'Elias condamne aussi ma grille."

    mara taquin "Ah, voilà. Le début du repentir."

    noam colere "Mais quel repentir ?!"

    lysa taquin "Laisse tomber. Plus tu te défends, plus ça devient mauvais."

    noam "Merci du soutien."

    lysa sourire "Toujours là pour toi."

    elias "Bon."

    "Elias frappe deux fois dans ses mains pour couper court au brouhaha."

    elias ecoute "Je peux poser des plaques. Pas sur douze chambres en cinq minutes."

    sael raison "Commence par les femmes."

    ryn "Ouais."

    noam desaccord "Je suis littéralement celui qui a entendu quelque chose derrière sa grille toute la nuit."

    iris colere "Et nous, on vient littéralement d'apprendre qu'un tunnel passe derrière notre lit."

    elias fatigue "Je vais commencer par les filles."

    noam panne "..."

    mara content "Merci Elias. Un gentleman. Contrairement à certains."

    noam "Je vais arrêter de répondre."

    tomas "Ça serait probablement plus prudent."

    "Quelques rires nerveux parcourent la pièce, mais ils disparaissent vite."

    nyra reflexion "Une fois les accès sécurisés, il faudra décider quoi faire de ce réseau."

    ryn "Le fouiller."

    sael mefiant "Pas seuls."

    nyra "Et pas aujourd'hui. Tout le monde est à cran."

    ryn colere "On part dans deux jours."

    "La phrase refroidit immédiatement la pièce."

    tomas triste "Jour vingt-et-un."

    elen triste "Ça arrive vite..."

    lysa blase "C'est souvent le problème avec les dates."

    nyra raison "Justement. On ne se disperse pas. Elias sécurise les chambres. Ensuite on réfléchit."

    "Je hoche la tête sans répondre."

    think "Deux jours."
    think "Deux jours avant de partir d'ici avec autant de questions qu'en arrivant."

    "Et, pour la première fois, cette idée ne me rassure pas du tout."

    $ hideGroup()

    jump _19_0_1_1_SECURISATION


label _19_0_1_1_SECURISATION:

    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Elias passe une bonne partie de l'après-midi à transporter des plaques métalliques depuis la maintenance jusque dans les dortoirs."
    "Je l'aide autant que possible, même si Mara a décrété devant tout le monde que ma présence dans les chambres des filles n'était 'pas forcément l'idée du siècle'."

    $ showGroup([
        ("noam", "fatigue", 0.30),
        ("elias", "fatigue", 0.70),
    ])

    elias fatigue "Tiens ça."

    noam "Je tiens."

    elias "Non, tu tiens de travers."

    noam "C'est une plaque, Elias."

    elias colere "Et elle pèse quinze kilos. Si tu la tiens de travers pendant que je perce, elle me tombe sur les doigts."

    noam "D'accord."

    "Je remonte légèrement mon côté."

    elias "Voilà. Là tu tiens."

    noam taquin "C'est toujours un plaisir de travailler avec toi."

    elias "J'aurais pu faire ça tout seul."

    noam "Tu te plains depuis une heure que t'as trop de chambres à faire."

    elias "Je me plains parce que j'ai trop de chambres à faire. Ça veut pas dire que j'ai envie d'aide mal faite."

    "Il termine de fixer la plaque devant la grille de Lysa et vérifie les attaches une par une."

    noam reflexion "Ça tiendra ?"

    elias "À moins que quelqu'un vienne avec une perceuse de l'autre côté, oui."

    noam inquiet "Et de l'autre côté ?"

    "Il lève les yeux vers moi."

    elias "Noam."

    noam "Quoi ?"

    elias "Arrête."

    noam desaccord "J'essaie juste de comprendre."

    elias "Non. Là tu nourris ton cerveau avec de la merde et tu le regardes paniquer."

    noam "C'est facile à dire quand ta grille sera condamnée."

    elias "Ma grille sera pas condamnée aujourd'hui."

    noam surpris "Pourquoi ?"

    elias "Parce qu'il y en a six avant."

    noam "Six ?"

    elias "Iris, Mara, Sael, Elen, Lysa, Nyra."

    noam panne "..."

    elias "Puis les autres demain si j'ai le temps."

    noam "Donc la mienne reste ouverte cette nuit."

    elias "Oui."

    noam inquiet "Super."

    elias "T'as survécu jusque-là."

    noam "Je pensais pas qu'il y avait un passage derrière mon mur jusque-là."

    elias "Et maintenant tu le sais. Donc tu mets ton bureau devant et tu dors."

    noam "J'ai déjà fait ça."

    elias "Alors continue."

    "Il récupère sa caisse à outils et se dirige vers la chambre suivante."

    noam "Elias."

    "Il s'arrête sans se retourner."

    noam reflexion "Tu crois Mara ?"

    elias "Sur quoi ?"

    noam "Quand elle dit qu'elle était pas avec moi hier."

    "Il garde le silence quelques secondes."

    elias ecoute "J'en sais rien."

    noam "Elle t'a pas cherché ?"

    elias "Non."

    noam panne "..."

    elias "Mais j'étais pas dans ma chambre toute la nuit non plus. J'ai pu la rater."

    noam "Elle m'a dit qu'elle avait fait le tour de la maintenance, de la cafétéria, de la salle de repos..."

    elias "Et ?"

    noam "Rien."

    elias fatigue "Alors rien."

    "Il reprend sa marche."

    elias "Te mets pas à chercher un complot dans chaque phrase. On en a déjà assez comme ça."

    noam "Ouais."

    "Je reste seul dans le couloir, avec une réponse qui ne répond à rien."

    $ hideGroup()

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Quand je repasse par la cafétéria un peu plus tard, l'ambiance est étrange."
    "Plus personne ne parle des votes. Ils sont annulés, et avec eux une partie de la raison même pour laquelle nous sommes ici."

    $ showGroup([
        ("lysa", "blase", 0.18),
        ("mara", "neutre", 0.30),
        ("iris", "agace", 0.42),
        ("elen", "triste", 0.54),
        ("tomas", "reflechit", 0.66),
        ("nyra", "neutre", 0.78),
        ("noam", "fatigue", 0.90),
    ])

    elen triste "Deux jours... ça fait bizarre de le dire comme ça."

    tomas reflechit "Techniquement, un peu moins. La navette doit arriver dans la journée du vingt-et-un."

    iris fatigue "Merci Tomas. Ça rend tout ça beaucoup plus joyeux."

    tomas "Je voulais juste être précis."

    lysa "Erreur classique."

    mara neutre "Moi j'ai surtout hâte de dormir dans une chambre où personne peut débarquer par le mur."

    "Elle jette un regard dans ma direction."

    noam colere "Je vais finir par changer de table."

    mara taquin "Oh ça va, je rigole."

    noam "Depuis ce matin."

    mara "Parce que c'est drôle depuis ce matin."

    nyra raison "Ça le sera moins si quelqu'un utilise réellement le réseau."

    "Mara perd aussitôt son sourire."

    iris inquiet "Tu penses vraiment que quelqu'un passe là-dedans ?"

    nyra "Je n'en sais rien."

    iris "Très rassurant."

    lysa blase "Aujourd'hui tout le monde fait de son mieux."

    "Je regarde Mara. Elle discute normalement avec Elen, comme si notre conversation dans le couloir n'avait jamais eu lieu."

    think "Elle ne se souvient vraiment de rien."

    "Cette pensée me dérange davantage que si elle avait simplement menti."

    $ hideGroup()
    call OFFER_DAILY_EXPLORATION(
        "_19_0_1_1_SOIREE", 1,
        ["maintenance", "observation", "conclave", "dortoir"],
        "Retourner au dortoir", "dortoir"
    ) from _call_offer_exploration_j19


label _19_0_1_1_SOIREE:

    $ current_period = "Soir"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    "Quand je retourne vers ma chambre, Elias est encore en train de travailler plusieurs portes plus loin. Une perceuse résonne dans le couloir, puis s'arrête."

    "Les chambres de Mara, Iris, Sael et Elen sont déjà sécurisées. Il lui en reste encore deux pour finir celles des filles."

    noam reflexion "La mienne demain."

    "Je le dis à voix basse, comme si le fait de le formuler pouvait accélérer le temps."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_j19_chambre_return
    scene bg_chambre at adaptive_fullscreen, living_background with dissolve

    "Ma grille est exactement dans le même état que ce matin. Deux vis serrées, deux autres faciles à retirer."

    "Je pousse de nouveau le bureau devant. Puis je reste debout quelques secondes à le regarder."

    noam desaccord "Ça suffit."

    "Je vérifie quand même qu'il touche bien le mur."

    "Je passe une partie de la soirée à essayer de lire sans retenir une seule phrase. Chaque fois qu'un bruit traverse la structure du Conclave, mes yeux remontent automatiquement vers la grille."

    think "Demain soir, ce sera fermé."
    think "Encore une nuit."

    "Je me couche tard, persuadé que l'épuisement finira par gagner."

    stop music fadeout 2.0
    scene black with dissolve

    pause 2.0

    play sound "audio/sfx_duct_scrape.wav" volume 0.76

    "Le bruit me réveille presque immédiatement."

    pause 0.8

    "Cette fois, je sais que je ne l'ai pas rêvé."

    play sound "audio/sfx_duct_scrape.wav" volume 0.84

    "Quelque chose avance dans le conduit. Lentement. Régulièrement."

    noam peur "..."

    "Je me redresse. Mon cœur bat déjà trop vite."

    play sound "audio/sfx_duct_scrape.wav" volume 0.92

    "Le bruit passe derrière ma grille."

    "Puis continue."

    "Vers la chambre suivante."

    noam panne "..."

    "Je reste assis plusieurs secondes, incapable de décider quoi faire."

    think "Va chercher Elias."

    "Je pose les pieds au sol."

    think "Va chercher Elias. Maintenant."

    "Je regarde la porte."

    play sound "audio/sfx_duct_scrape.wav" volume 0.86

    "Un nouveau frottement résonne plus loin."

    "Quelque chose en moi cède."

    noam determine "Non." id j19_chasse_noam_non

    scene bg_chambre at adaptive_fullscreen with vpunch

    "Je repousse brutalement le bureau, ouvre la porte et sors presque en courant."

    jump _19_0_1_1_CHASSE


label _19_0_1_1_CHASSE:

    $ current_period = "Nuit"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.0
    $ danger_on()

    "Le couloir est désert. Les lumières nocturnes donnent aux murs une couleur blafarde qui me fait regretter immédiatement d'être sorti."

    "Je devrais aller chercher Elias."

    "À la place, je prends la direction de la cafétéria."

    think "Une lampe."
    think "Quelque chose pour me défendre."

    "Je marche vite. Puis je cours."

    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Je n'entends plus rien derrière les murs, mais ça ne me calme pas. Au contraire, j'ai l'impression d'avoir perdu sa trace."

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "La cafétéria est plongée dans le noir, à l'exception des veilleuses près du buffet."

    "J'ouvre un tiroir, puis un autre. Mes mains tremblent tellement que je fais tomber deux couverts au sol."

    play sound sfx_drop

    noam colere "Putain..."

    "Je finis par trouver une petite lampe portative dans un placard de service."

    "Puis j'ouvre le tiroir des ustensiles de cuisine."

    "Ma main s'arrête sur un couteau."

    pause 0.8

    think "C'est stupide."

    "Je le prends quand même."

    "Pas pour attaquer qui que ce soit. Enfin... je crois."

    noam panne "..."

    "Je serre la poignée et quitte la cafétéria."

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "De retour dans ma chambre, le bureau est toujours déplacé."

    "J'enlève les deux vis qui maintiennent la grille. Cette fois je ne prends même pas le temps de réfléchir."

    noam determine "Je vais voir ce qu'il y a là-dedans."

    "La phrase sonne mal dès qu'elle sort de ma bouche."

    "Je passe la tête dans l'ouverture. Rien."

    "Je me glisse à l'intérieur avec la lampe dans une main et le couteau dans l'autre."

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    $ flashlight_on()

    tuto "Les bruits peuvent mentir. Choisis vite : la poursuite converge toujours vers la source."
    call investigation_conduit_run("chase") from _call_investigation_conduit_j19

    "Le conduit paraît plus étroit que la veille."
    "Ou peut-être que je suis simplement beaucoup plus conscient de ce qui pourrait se trouver devant moi."

    "Je rampe lentement. La lumière découpe des portions de tôle, des câbles, des angles que je reconnais vaguement."

    play sound "audio/sfx_duct_scrape.wav" volume 0.78

    "Un bruit retentit au loin."

    noam peur "Je t'ai entendu."

    "Ma propre voix me fait sursauter."

    "Je continue."

    "Je dépasse la première bifurcation. Puis la deuxième. Je connais maintenant assez le réseau pour savoir dans quelle direction je vais."

    think "La salle des Goumi."

    "Le bruit vient de là."

    "J'accélère. Mon genou cogne contre une plaque, ma paume glisse sur une arête et une douleur vive traverse ma main."

    noam colere "Aïe..."

    "Je regarde rapidement. Une petite coupure. Rien de grave."

    "Je repars immédiatement."

    "À mesure que j'approche, le bruit disparaît."

    "Je ralentis."

    "La grille qui donne sur la salle est devant moi."

    "Elle est entrouverte."

    noam inquiet "..."

    "Je suis presque certain de l'avoir refermée hier."

    think "Presque." id j19_conduit_presque

    "Je pousse doucement la grille du bout des doigts."

    scene bg_conduit_reseau at adaptive_fullscreen
    pause 1.0

    "Elle s'ouvre sans résistance."

    "Je descends."

    jump _19_0_1_1_CADAVRE


label _19_0_1_1_CADAVRE:

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    play music "audio/music/bgm_horror_reveal.mp3" fadein 2.0

    "Mes pieds touchent le sol de la salle de maintenance."

    "Je garde la lampe braquée devant moi."

    "Les deux stations des Goumi sont toujours là. Les établis aussi. Rien ne semble avoir bougé."

    noam peur "..."

    "Je fais quelques pas."

    "Le faisceau passe sur une caisse ouverte, un bras mécanique, plusieurs outils rangés contre le mur."

    "Puis sur la grande table de maintenance au centre de la pièce."

    pause 1.0

    "Je m'arrête."

    noam panne "..."

    "Il y a quelque chose dessus."

    "Au début, mon cerveau essaie de le ranger avec le reste. Une coque. Une pièce détachée. Un autre robot en cours de réparation."

    "Puis la lumière éclaire une main."

    $ investigation_add("corps_mara")

    $ unlock_gallery_image("bg_cg040")
    scene bg_cg040 at adaptive_fullscreen with creep_diss
    $ cam_move(fx=0.53, fy=0.44, z=1.12, t=6.5)

    pause 1.0

    "Une vraie main."

    noam peur "Non..."

    "Je relève lentement la lampe."

    "Un bras. Une épaule. Des cheveux."

    "Je connais ces cheveux."

    noam peur "Non."

    "Je m'approche malgré moi. Chaque pas me donne envie de reculer."

    "Le faisceau atteint enfin son visage."

    pause 1.5

    $ impact(intensity=9, duration=0.28, color="#c81e2e")
    noam desespoir "{cps=8}Mara...{/cps}"

    "Elle est allongée sur la table de maintenance des Goumi."

    "Immobile."

    "La tête légèrement tournée sur le côté, comme si quelqu'un l'avait simplement déposée là."

    "Pendant plusieurs secondes, je n'arrive pas à faire le moindre mouvement."

    think "Non." id j19_cadavre_non_1

    "Je l'ai vue ce matin."

    think "Non."

    "Elle m'a traité de pervers. Elle a crié dans le couloir. Elle a prévenu tout le monde."

    think "Non."

    "Elle était à la cafétéria cet après-midi."

    "Ma lampe tremble de plus en plus."

    noam peur "Mara ?"

    "Aucune réponse."

    "Je fais encore un pas et tends la main, sans réussir à la toucher."

    noam desespoir "Mara..."

    "Son torse ne bouge pas."

    "Je reste là, le couteau pendant stupidement au bout de ma main, incapable de comprendre ce que je suis en train de regarder."

    pause 1.5

    $ horror_audio_cut(duration=0.40, restore_volume=0.68)
    play sound "audio/sfx_duct_scrape.wav" volume 0.86

    "Un bruit métallique retentit derrière moi."

    "Je me retourne brutalement."

    $ cam_reset(t=0.0)
    scene black with vpunch

    stop music fadeout 0.5
    $ danger_off()

    pause 1.0

    pause 1.0

    call end_day("20") from _call_end_day_20
    jump _20_0_1_1_0_REVEIL
