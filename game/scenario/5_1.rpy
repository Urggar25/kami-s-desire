# --------------------------------------------------------------------------------------------
# JOUR 5 — 5_1.rpy
# Vote Jour 4 : OUI (commerce inter-districts — branche 4_1)
# --------------------------------------------------------------------------------------------

label _5_1_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 5

    pause 1.0

    $ blink()
    "J'ouvre les yeux et tout me revient d'un coup."
    "La tête lourde."
    "La bouche sèche."
    "La lumière bleue qui pique un peu trop."

    think "Pas de grande méditation."
    think "Mon corps proteste."

    pause 0.5

    "J'essaie de me redresser."
    "Mauvaise idée."
    "Le plafond bouge juste assez pour me rappeler la soirée d'hier."

    $ blink()

    think "La porte qui claque."
    think "Sael."
    think "\"C'est non.\""

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour mes survivants préférés."
    kami "Bilan matinal : deux migraines, trois regrets, et une tentative collective de faire comme si tout allait bien."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Point technique en passant : Orbite a eu une alarme de niveau deux cette nuit."
    kami "Joint de sas défaillant. Procédure appliquée. Incident clos."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Rien de grave."
    kami "Enfin, sauf si vous aimez dormir sans savoir que vos proches enfilent un scaphandre à deux heures du matin."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Petit-déjeuner servi."
    kami "Hydratez-vous. Certaines décisions se prennent mieux sans gueule de bois."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "L'écran s'éteint."
    "Le silence revient."
    "Pas plus rassurant qu'avant."

    pause 0.5

    "Je passe une main sur mon visage."
    "J'ai encore la marque de l'oreiller."

    think "Kael n'était pas au courant."
    think "Sinon il aurait déjà frappé à toutes les portes."

    "Je sors dans le couloir."
    "Des voix basses, au fond."
    "Près des chambres."

    jump _5_1_KAEL_NYRA

# Durée : 2m40
# Total : 2h 08m 55s


label _5_1_KAEL_NYRA:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.6

    pause 0.6

    "Kael est assis par terre, dos au mur, les genoux remontés."
    "Nyra est accroupie à côté de lui."
    "Elle parle bas."
    "Lentement."

    $ showP("kael", "triste", 0.52)
    $ showP("nyra", "neutre", 0.80)

    nyra "Respire."
    nyra "Une minute après l'autre."

    kael "Je l'ai appris sur l'écran de la chambre."
    kael "J'étais même pas au courant pendant que c'était en train d'arriver."

    pause 0.5

    nyra "Ce n'est pas anodin."
    nyra "Mais ce n'était pas structurel."

    kael "Je sais."
    kael "Un joint de sas."
    kael "Module C-7, c'est ça qu'ils ont affiché."

    "Il parle avec une voix plate."
    "Comme s'il récitait un rapport pour éviter le reste."

    kael "Orbite n'est pas un bloc unique."
    kael "C'est des modules reliés."
    kael "Quand un truc lâche, tu isoles."
    kael "Tu fermes. Tu recompresses."

    nyra "Et vous avez appris ça tôt."

    kael "Dès l'enfance."
    kael "Alarme. Scaphandre. Vérification croisée."
    kael "C'est un réflexe."

    pause 0.6

    kael "Ma sœur a six ans."
    kael "Elle sait déjà enfiler son scaphandre seule."

    "Nyra ne répond pas tout de suite."
    "Elle pose juste une main sur son avant-bras."

    nyra "Je ne vais pas te dire que tout va bien."
    nyra "Je reste là."

    pause 0.8

    "Je reste à distance."
    "Je ne dis rien."
    "Ça ne m'appartient pas."

    kael "Elle sait déjà le faire toute seule."
    $ showP("kael", "triste", 0.52)
    kael "C'est bien."
    kael "C'est pas bien du tout."

    pause 0.7

    hide nyra
    $ showP("kael", "fatigue", 0.52)

    "Kael se relève enfin."
    "Nyra aussi."

    nyra "Viens."
    nyra "On va boire quelque chose de chaud."

    hide kael
    hide nyra

    "Ils partent vers la cafétéria."
    "Je les suis, quelques mètres derrière."

    jump _5_1_CAFETERIA_MATIN

# Durée : 3m10
# Total : 2h 12m 05s


label _5_1_CAFETERIA_MATIN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.8

    pause 0.8

    "La cafétéria a la gueule des lendemains de fête."
    "Plateaux alignés."
    "Silences mous."
    "Personne n'a vraiment la force de parler fort."

    "Les écrans tournent en boucle."
    "Nexus commence déjà à s'organiser autour du vote commerce."
    "Limen reste en tension."
    "Les visages fermés défilent entre deux graphiques optimistes."

    $ showP("julian", "fatigue", 0.18)
    $ showP("sael", "neutre", 0.50)
    $ showP("noam", "fatigue", 0.82)

    "Sael mange."
    "Elle ne regarde personne."

    julian "Bon."
    julian "On peut encore parler du vote libre circulation."
    julian "On n'est pas obligés de rester bloqués sur hier."

    pause 0.3

    sael "..."
    sael "Ma réponse n'a pas changé."

    "Elle repose sa fourchette une seconde."
    "Puis elle reprend."
    "Julian n'insiste pas."

    hide julian
    hide sael
    hide noam

    think "Un seul non."
    think "C'est elle."
    think "C'est foutu."

    pause 0.5

    jump _5_1_TEMPS_LIBRE

# Durée : 2m05
# Total : 2h 14m 10s


label _5_1_TEMPS_LIBRE:
    call START_FREE_TIME("_5_1_APRES_MIDI") from _call_START_FREE_TIME_5_1

# Durée : 0m10
# Total : 2h 14m 20s


label _5_1_APRES_MIDI:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.8

    "L'après-midi devient une suite d'essais ratés."
    "Tout le monde passe par le même couloir."
    "Par la même porte."
    "Et revient avec la même réponse."

    $ showP("elias", "neutre", 0.22)
    $ showP("sael", "mefiant", 0.78)

    "Elias tente l'approche factuelle."
    "Données de flux. Projections. Risques comparés."
    "Sael écoute jusqu'au bout."
    "Elle ne bouge pas."

    sael "J'ai compris les chiffres."
    sael "Ça ne change rien."

    hide elias
    hide sael

    pause 0.5

    $ showP("elen", "inquiet", 0.24)
    $ showP("sael", "neutre", 0.78)

    "Elen essaie autrement."
    "Moins politique."
    "Plus personnel."
    "Je n'entends pas tout."
    "Juste des morceaux."
    "\"famille\"."
    "\"lignes rouges\"."

    pause 0.6

    hide sael
    $ showP("elen", "triste", 0.24)

    "Elen revient sans succès."
    "Mais son regard a changé."
    "Elle n'est plus juste frustrée."
    "Elle a entendu quelque chose."

    hide elen

    "Le groupe commence à accepter l'inévitable."
    "Sauf Julian."
    "Lui continue de tourner en rond avec des plans dans la tête."

    $ showP("mara", "reflechit", 0.50)

    "Mara passe près de moi."
    "Elle baisse la voix."

    mara "Si elle peut pas voter..."
    mara "C'est pas pareil."

    hide mara

    "Elle s'éloigne sans ajouter un mot."
    "Je reste avec sa phrase."

    jump _5_1_APRES_MIDI_EXT_1

# Durée : 3m00
# Total : 2h 17m 20s


label _5_1_APRES_MIDI_EXT_1:

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.7

    "Je traîne vers la salle commune."
    "Pas pour me détendre."
    "Juste parce que rester immobile me rend dingue."

    "Julian est déjà là."
    "Debout devant un écran éteint."
    "Il parle tout seul."
    "Ou il répète un argument."

    $ showP("julian", "fatigue", 0.22)
    $ showP("noam", "reflexion", 0.78)

    julian "On peut encore inverser un vote."
    julian "Une nuit, c'est long."
    julian "Suffisamment long pour fissurer une certitude."

    noam "Il me semble que tu parles de Sael."

    julian "Je parle de tout le monde."
    julian "Mais oui. Surtout d'elle."

    pause 0.4

    noam "Ce que j'entends, c'est que tu veux encore tenter un dernier round."

    julian "Évidemment."
    julian "Si je m'arrête maintenant, je valide sa version."
    julian "Et sa version, c'est quoi ?"
    julian "Que c'est fini avant d'avoir commencé."

    "Il sourit à moitié."
    "Un sourire qui ne tient pas."

    julian "Tu sais ce qui est drôle ?"
    julian "Hier, tout le monde disait qu'on venait de gagner."
    julian "Aujourd'hui, on parle déjà comme des perdants."
    julian "On est des champions de la rechute."

    noam "Je me demande si c'est pas juste de la fatigue."

    julian "Non."
    julian "La fatigue, ça ralentit."
    julian "Là, ça renonce."

    pause 0.6

    "On entend des voix dans le couloir."
    "Elen et Tomas passent devant la porte."
    "Ils parlent bas."
    "Trop bas pour que je comprenne."

    julian "Je vais la voir encore une fois."
    julian "Sans effet de manche."
    julian "Sans caméra."
    julian "Juste une discussion."

    noam "Elle va te dire non."

    julian "Oui."
    julian "Mais je préfère un non de plus qu'un silence de trop."

    "Il se dirige vers la sortie."
    "Puis s'arrête."

    julian "Noam."
    julian "Si je vais trop loin, tu m'arrêtes."

    noam "Je me demande si tu me laisseras faire."

    julian "Probablement pas."
    julian "Mais ça m'aide de te le demander."

    hide julian
    hide noam

    "Il part."
    "Et la salle commune redevient vide."
    "J'y reste encore un peu, juste pour écouter le bourdonnement des néons."

    pause 0.6

    jump _5_1_APRES_MIDI_EXT_2

# Durée : 2m20
# Total : 2h 19m 40s


label _5_1_APRES_MIDI_EXT_2:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.8

    pause 0.6

    "Je tombe sur Kael près des distributeurs d'eau."
    "Il tient une tasse vide."
    "Il ne boit pas."
    "Il fixe juste la vapeur qui sort des conduits."

    $ showP("kael", "fatigue", 0.24)
    $ showP("noam", "inquiet", 0.78)

    noam "Ça va ?"

    kael "Non."
    kael "Mais c'est gérable."

    noam "Tu as eu des nouvelles ?"

    kael "Oui."
    kael "Message automatique."
    kael "Procédure standard."
    kael "Incident clos."

    pause 0.4

    kael "Je hais ce genre de phrase."
    kael "Incident clos."
    kael "Comme si la nuit se refermait proprement."

    noam "Je me demande si ta sœur a répondu."

    kael "Pas encore."
    kael "Elle est en cycle d'école."
    kael "Enfin..."
    kael "Ce qu'ils appellent école."

    "Il souffle."
    "Lentement."
    "Avec la main crispée sur la tasse."

    kael "Tu veux savoir le pire ?"
    kael "Je suis partagé entre deux hontes."
    kael "J'ai honte qu'elle sache faire ça."
    kael "Et j'ai honte d'être soulagé qu'elle sache."

    noam "Ce que j'entends, c'est que t'es juste un frère."

    kael "Peut-être."
    kael "Ou juste un lâche en différé."

    pause 0.5

    noam "C'est pas du tout pareil."

    kael "Si."
    kael "Quand t'es loin, tout devient pareil."
    kael "Les bons choix."
    kael "Les sales choix."
    kael "Tu vois plus que le résultat."

    "Nyra arrive sans bruit."

    hide noam
    $ showP("nyra", "neutre", 0.78)

    nyra "Le résultat, c'est qu'ils sont en vie."

    kael "Pour cette nuit."

    nyra "Pour cette nuit."
    nyra "Et demain, on recommencera."

    pause 0.4

    kael "Tu fais toujours ça ?"
    kael "Transformer l'angoisse en procédure ?"

    nyra "Souvent."
    nyra "Parce que ça marche."

    kael "Ça marche pour toi."

    nyra "Non."
    nyra "Ça marche pour traverser."
    nyra "C'est moins ambitieux."

    "Kael hoche la tête."
    "Pas convaincu."
    "Mais moins en vrac."

    noam "On va à la cafétéria ?"

    kael "Je peux pas avaler grand-chose."

    nyra "Alors de l'eau."
    nyra "Et cinq minutes assis."
    nyra "C'est déjà une victoire."

    hide kael
    hide nyra

    "Ils partent ensemble."
    "Je les regarde s'éloigner."
    "Je me dis que parfois, aider, c'est juste donner un ordre très simple."

    pause 0.7

    jump _5_1_APRES_MIDI_EXT_3

# Durée : 2m35
# Total : 2h 22m 15s


label _5_1_APRES_MIDI_EXT_3:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.6

    pause 0.8

    "En début de soirée, la cafétéria se remplit sans bruit."
    "Les plateaux glissent."
    "Les chaises grincent."
    "Personne n'a l'énergie d'être agressif."

    $ showP("elen", "triste", 0.15)
    $ showP("tomas", "hesitation", 0.50)
    $ showP("iris", "fatigue", 0.85)

    elen "J'ai essayé gentiment."
    elen "Vraiment."
    elen "Sans slogan."
    elen "Sans discours."
    elen "J'ai juste parlé de ce que ça fait de vivre en ayant peur des autres."

    tomas "Et... et ?"

    elen "Elle m'a écoutée."
    elen "Et elle m'a dit que la peur n'était pas le problème."
    elen "Que c'était la mémoire."

    iris "Bah."
    iris "Ça lui ressemble."

    pause 0.3

    tomas "T-Techniquement..."
    tomas "Si on intègre les flux de déplacement..."
    tomas "Le risque d'incident augmente pas forcément."

    iris "Et politiquement ?"
    iris "Parce qu'on n'est pas dans un tableur."

    tomas "Politiquement..."
    tomas "C'est... oui."
    tomas "C'est pire."

    elen "Je déteste cette phrase."
    elen "Techniquement possible."
    elen "Politiquement impossible."

    iris "Bienvenue au Conclave."

    "Noam pose son plateau."
    "Le repas refroidit vite."
    "Comme toutes les bonnes intentions."

    hide iris
    $ showP("noam", "reflexion", 0.85)

    noam "Ce que j'entends, c'est qu'on est en train de préparer l'après-vote."

    elen "Je veux pas préparer ça."

    tomas "M-Moi non plus."
    tomas "Mais..."
    tomas "J'ai commencé quand même."

    pause 0.5

    iris "Julian est où ?"

    noam "Il tourne."
    noam "Il cherche encore un angle."

    elen "Il va se fracasser."

    iris "Oui."
    iris "Mais au moins il marche."
    iris "Moi j'ai juste envie de dormir deux semaines."

    tomas "Pareil."
    tomas "M-Mais demain y'a vote."

    iris "Oui merci Tomas."
    iris "On sait."

    "Un écran s'allume derrière nous."
    "Des images de Nexus."
    "Des files d'attente devant des comptoirs de commerce."
    "Des bénévoles avec des brassards neufs."
    "Un commentaire enthousiaste."

    elen "C'est fou."
    elen "On dirait déjà une pub."

    iris "C'est une pub."
    iris "Faut que ça ressemble à une victoire."
    iris "Sinon les gens posent des questions."

    tomas "À Limen, ça passe mal."
    tomas "J'ai vu des retours."
    tomas "Ils disent que les prix ont déjà bougé."
    tomas "Même sans marché ouvert."

    noam "Effet d'annonce."

    tomas "Ouais."
    tomas "Et ça..."
    tomas "Ça peut dégénérer vite."

    pause 0.6

    elen "On fait quoi ce soir ?"

    iris "On respire."
    iris "On évite de se taper dessus."
    iris "On dort un peu."

    elen "Super programme."

    iris "J'ai jamais promis Disneyland."

    hide elen
    hide tomas
    hide iris
    hide noam

    "Le repas finit sans vraie conclusion."
    "Chacun ramène son plateau."
    "Chacun repart avec ses idées."
    "Et son petit sac d'angoisses personnelles."

    jump _5_1_APRES_MIDI_EXT_4

# Durée : 2m45
# Total : 2h 25m 00s


label _5_1_APRES_MIDI_EXT_4:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.8

    "Un peu plus tard, je vois Julian devant la porte de Sael."
    "Il ne frappe pas tout de suite."
    "Il ajuste sa posture comme avant une prise de parole."
    "Puis il abandonne l'idée."

    $ showP("julian", "fatigue", 0.20)
    $ showP("noam", "neutre", 0.52)
    $ showP("sael", "mefiant", 0.84)

    "La porte s'ouvre avant qu'il touche."
    "Sael était déjà là."

    sael "Tu vas rester planté longtemps ?"

    julian "Je voulais juste parler."

    sael "Tu veux convaincre."

    julian "Les deux."

    pause 0.4

    sael "Fais court."

    julian "Le vote de demain ne parle pas seulement de sécurité."
    julian "Il parle de liberté minimale."
    julian "De circulation humaine."
    julian "De pouvoir sortir de son district sans passer pour un ennemi."

    sael "J'ai compris le texte."

    julian "Alors pourquoi..."

    sael "Parce que je connais le prix caché."

    julian "Lequel ?"

    sael "L'imprévu."
    sael "L'infiltration."
    sael "La rumeur."
    sael "Le premier coup de couteau qui redevient normal."

    pause 0.5

    julian "On peut pas vivre enfermés pour éviter un risque."

    sael "On peut pas ouvrir toutes les portes pour flatter un principe."

    julian "C'est pas flatter un principe."
    julian "C'est empêcher l'étouffement."

    sael "Et moi j'empêche l'incendie."

    julian "Tu vois ?"
    julian "On parle de la même chose."

    sael "Non."
    sael "Toi, tu parles d'espoir."
    sael "Moi, je parle de séquelles."

    pause 0.6

    "Julian baisse les yeux."
    "Pas longtemps."
    "Juste une seconde."

    julian "Si je te demande au moins une abstention ?"

    sael "Non."

    julian "Même pas pour laisser une chance ?"

    sael "Ma réponse n'a pas changé."

    pause 0.4

    julian "D'accord."
    julian "Alors je n'ai plus rien."

    sael "Si."
    sael "Tu peux encore accepter."

    julian "Pas ce soir."

    "Sael referme la porte."
    "Sans brutalité."
    "Sans trembler."
    "Sans triomphe."

    hide sael
    hide noam
    $ showP("julian", "fatigue", 0.50)

    julian "J'ai horreur quand elle a raison sur la forme."
    julian "Et tort sur le fond."

    noam "Je me demande si c'est aussi simple."

    julian "Non."
    julian "C'est pas simple."
    julian "C'est juste insupportable."

    pause 0.5

    julian "Je vais prendre l'air."

    noam "On n'a pas d'air."

    julian "Tu vois ce que je veux dire."

    hide julian

    "Il s'éloigne."
    "Je reste devant une porte fermée."
    "Encore."

    jump _5_1_APRES_MIDI_EXT_5

# Durée : 2m30
# Total : 2h 27m 30s


label _5_1_APRES_MIDI_EXT_5:

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.8

    pause 0.7

    "La salle de repos est presque vide."
    "Mara est affalée dans un canapé."
    "Iris est sur une chaise, capuche sur la tête."
    "Elias nettoie mécaniquement une gourde."

    $ showP("mara", "fatigue", 0.15)
    $ showP("iris", "fatigue", 0.50)
    $ showP("elias", "neutre", 0.85)

    mara "Ah."
    mara "Le médiateur officiel."
    mara "T'as une solution magique ou tu viens juste déprimer en groupe ?"

    noam "Plutôt la deuxième option."

    iris "On est complets."

    elias "Laisse-le."
    elias "Plus on est nombreux, plus on se surveille."
    elias "C'est utile."

    mara "Super ambiance."
    mara "On devrait vendre des billets."

    pause 0.3

    noam "J'ai entendu ta phrase cet après-midi."
    noam "Si elle peut pas voter..."

    mara "Ouais."
    mara "Je pensais pas te la balancer comme ça."
    mara "Mais elle est sortie."

    iris "Tu proposes quoi exactement ?"

    mara "Rien."
    mara "Je constate."
    mara "Le système a une faiblesse."
    mara "Une voix peut bloquer tout le monde."
    mara "Donc forcément, les cerveaux commencent à faire des maths sales."

    elias "Et toi ?"
    elias "Tu fais ces maths-là ?"

    mara "Tous les jours."
    mara "Je les applique pas tous les jours."

    pause 0.6

    iris "C'est ça le problème."
    iris "Le moment où t'arrêtes de juste y penser."

    mara "T'inquiète."
    mara "Je vais pas empoisonner la moitié du Conclave."

    iris "J'ai pas dit ça."

    mara "T'as pensé pire."

    "Elias lève la main."
    "Comme un arbitre fatigué."

    elias "On se calme."
    elias "On est tous à cran."
    elias "On se fait pas de procès d'intention."

    noam "Ce que j'entends, c'est qu'on a passé la ligne morale en pensée."

    mara "Bienvenue."
    mara "La pensée, c'est pas propre."

    pause 0.4

    iris "Je déteste quand t'as des phrases justes."

    mara "Moi aussi."

    elias "Demain, il faudra voter."
    elias "Point."
    elias "On fait avec ça."

    mara "Ouais."
    mara "Et après demain, on fera avec les conséquences."

    iris "Et après après demain, avec les conséquences des conséquences."

    mara "Exactement."

    pause 0.5

    "Le silence retombe."
    "Pas hostile."
    "Juste épuisé."

    "Mara me regarde."
    "Pas longtemps."
    "Juste assez pour vérifier un truc."

    mara "Noam."
    mara "Fais gaffe à ce que tu choisis ce soir."

    noam "Tu sais pas ce que je vais choisir."

    mara "J'ai pas besoin."
    mara "Je te connais assez pour savoir que t'as déjà commencé."

    pause 0.5

    "Je ne réponds pas."
    "Parce qu'elle a peut-être raison."
    "Ou parce que j'ai pas envie de le vérifier."

    hide mara
    hide iris
    hide elias

    jump _5_1_APRES_MIDI_EXT_6

# Durée : 2m50
# Total : 2h 30m 20s


label _5_1_APRES_MIDI_EXT_6:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.6

    pause 0.8

    "Le couloir est plus sombre."
    "Pas vraiment la nuit."
    "Mais plus vraiment l'après-midi."

    "Je croise Lysa près d'un panneau de maintenance."
    "Elle tapote l'écran sans enthousiasme."

    $ showP("lysa", "fatigue", 0.24)
    $ showP("noam", "neutre", 0.76)

    lysa "... T'as une tête de type qui dort pas."

    noam "Je me demande si ça se voit tant que ça."

    lysa "Ouais."
    lysa "Sur toi, oui."

    pause 0.3

    noam "Tu penses quoi de demain ?"

    lysa "Je pense que ça va casser."
    lysa "Je sais pas encore quoi."
    lysa "Mais quelque chose."

    noam "Merci pour l'optimisme."

    lysa "C'est pas de l'optimisme."
    lysa "C'est de la prévention."

    "Elle range l'outil qu'elle tenait."
    "Puis s'adosse au mur."

    lysa "J'ai vu Julian passer trois fois."
    lysa "J'ai vu Elen ressortir en larmes contenues."
    lysa "J'ai vu Kael vérifier ses messages toutes les dix minutes."
    lysa "Et toi, je te vois calculer."

    noam "Je calcule pas très bien."

    lysa "Personne calcule bien quand y'a des gens au milieu."

    pause 0.5

    noam "Et Sael ?"

    lysa "Mur."
    lysa "Pas un mur contre nous."
    lysa "Un mur pour empêcher quelque chose de revenir."

    noam "C'est pareil au final."

    lysa "... Non."
    lysa "C'est pire."

    pause 0.4

    noam "Pourquoi pire ?"

    lysa "Parce qu'un mur contre toi, tu peux le contourner."
    lysa "Un mur contre son passé, non."

    "Je reste silencieux."
    "Lysa soupire."

    lysa "Tu vas faire une connerie."

    noam "Pourquoi tout le monde dit ça aujourd'hui ?"

    lysa "Parce que c'est écrit sur ta gueule."

    noam "C'est à ce point."

    lysa "Ouais."
    lysa "Mais..."
    lysa "Je vais pas te faire la morale."
    lysa "Juste te rappeler un truc."
    lysa "Une connerie utile reste une connerie."

    pause 0.6

    noam "Je me demande si on a encore le luxe du propre."

    lysa "Non."
    lysa "Mais on peut choisir le degré de sale."

    "Elle me donne une petite tape sur l'épaule."
    "Pas affectueuse."
    "Fonctionnelle."

    lysa "Va te poser."
    lysa "Avant de décider quoi que ce soit."

    hide lysa
    hide noam

    "Je reste seul dans le couloir."
    "Les lumières vibrent un peu."
    "Comme si même l'électricité avait mal dormi."

    pause 0.7

    jump _5_1_APRES_MIDI_EXT_7

# Durée : 2m40
# Total : 2h 33m 00s


label _5_1_APRES_MIDI_EXT_7:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    "Je retourne dans ma chambre avant le soir complet."
    "Je laisse la porte ouverte."
    "Puis je la referme."
    "Puis je la rouvre."
    "Je n'arrive pas à choisir même ça."

    "Je bois de l'eau."
    "Encore."
    "Toujours la bouche sèche."

    think "Un seul non."
    think "Un seul verrou."
    think "Et tout saute."

    "J'essaie de penser à autre chose."
    "Je pense à la pharmacie."
    "Raté."

    pause 0.5

    think "Je me demande si c'est encore moi qui pense."
    think "Ou juste le stress qui me pousse."

    "Quelqu'un frappe."

    play sound sfx_knock volume 8.0
    pause 0.4

    $ showP("nyra", "neutre", 0.76)
    $ showP("noam", "hesitation", 0.24)

    noam "Entre."

    nyra "Je ne reste pas longtemps."
    nyra "Je venais vérifier que tu n'explosais pas."

    noam "C'est gentil."

    nyra "C'est stratégique."
    nyra "On a besoin de tout le monde demain."

    pause 0.3

    noam "Kael ?"

    nyra "Toujours inquiet."
    nyra "Mais debout."

    noam "Et toi ?"

    nyra "Toujours inquiète."
    nyra "Mais utile."

    noam "Tu fais comment ?"

    nyra "Je découpe la journée en tâches."
    nyra "Ça évite de regarder le tout."

    pause 0.4

    noam "Si demain échoue ?"

    nyra "Alors demain échoue."
    nyra "Et après-demain existera quand même."

    noam "Tu dis ça comme si c'était simple."

    nyra "Ce n'est pas simple."
    nyra "C'est seulement vrai."

    "Elle se tourne vers la porte."

    nyra "Dors si tu peux."
    nyra "Et si tu peux pas, au moins reste horizontal."

    noam "Conseil médical ?"

    nyra "Conseil de survie."

    hide nyra
    hide noam

    "Elle s'en va."
    "Je reste seul."
    "Avec la chambre."
    "Avec le silence."
    "Avec la pharmacie dans un coin de ma tête."

    pause 0.7

    jump _5_1_CHOIX_PRINCIPAL

# Durée : 2m25
# Total : 2h 35m 25s


label _5_1_CHOIX_PRINCIPAL:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    "Le soir tombe sur rien de neuf."
    "Je suis seul dans ma chambre."
    "Assis au bord du lit."

    think "La pharmacie."
    think "J'y ai pensé sans arrêt toute la journée."

    menu:
        "Empêcher Sael de voter.":
            $ choix_5_1_soir = "empecher_sael"
            jump _5_1_PHARMACIE

        "Aller se coucher.":
            $ choix_5_1_soir = "dormir"
            jump _5_1_FIN_JOURNEE

# Durée : 0m45
# Total : 2h 18m 05s


label _5_1_PHARMACIE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    "Je ressors."
    "Je marche vite."
    "Sans me laisser le temps de réfléchir trop loin."

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    "L'infirmerie est vide."
    "Néons blancs."
    "Odeur de désinfectant."

    "Je trouve vite ce que je cherche."
    "Un petit flacon, banal."
    "Laxatifs."

    pause 0.4

    think "C'est simple."
    think "C'est moche."
    think "Et ça peut marcher."

    "Je glisse le flacon dans ma poche."
    "Je ressors sans bruit."

    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Je me déteste un peu."
    think "Je continue quand même."

    jump _5_1_FIN_JOURNEE

# Durée : 1m30
# Total : 2h 19m 35s


label _5_1_FIN_JOURNEE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 1.0

    "Je suis allongé sur le dos."
    "Les mains sur le ventre."
    "Le plafond bleu au-dessus."

    pause 0.6

    "Le calcul tourne encore."
    "Toujours le même."
    "Toujours brutal."

    think "Un seul non."
    think "Et demain, ça recommence."

    pause 0.8

    $ blink()
    "Je ferme les yeux."
    "Pas pour trouver la paix."
    "Juste pour arrêter de compter."

    pause 1.2

    jump patreon_ending

# Durée : 1m20
# Total : 2h 20m 55s
