# --------------------------------------------------------------------------------------------
# JOUR 5 — 5_1.rpy
# Vote Jour 4 : OUI (libre commerce — branche 4_1)
# Réécriture THL stricte : VN japonais adapté en français, dialogues actifs, rythme oral.
# Noam = narrateur principal, parle à la première personne.
# --------------------------------------------------------------------------------------------

label _5_1_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 5

    pause 1.0

    $ blink()

    noam "..."

    pause 0.3

    noam "Aïe."

    pause 0.3

    $ blink()

    noam "Non."
    noam "Même pas aïe."
    noam "Là, c'est carrément mon crâne qui demande l'indépendance."

    think "Bouche sèche. Lumière bleue. Corps officiellement en grève."

    think "Bien fait."

    pause 0.4

    noam "D'accord…"
    noam "Objectif numéro un : survivre au fait d'être réveillé."

    pause 0.3

    noam "Objectif numéro deux..."
    noam "Non. Trop ambitieux."

    $ blink()

    think "Hier soir."

    think "Les images remontent par morceaux, dans le désordre."

    noam "Les verres en plastique..."
    noam "La musique..."
    noam "Mara et sa bouteille stupide..."

    pause 0.2

    noam "Lysa."

    pause 0.4

    think "Le jeu de la bouteille."
    think "Sérieusement."

    noam "J'ai participé à ça."
    noam "Et de mon plein gré, en plus…"
    noam "Kami devrait me retirer mon droit de vote juste pour ça."

    pause 0.3

    think "Mon estomac répond avant moi."

    noam "Pas maintenant."

    pause 0.4

    think "Puis l'autre souvenir revient et tue le sourire avant qu'il s'installe."

    think "La table ronde."
    think "Le prochain vote."
    think "La libre circulation entre districts."

    noam "Elias qui provoque un peu trop fort."
    noam "Sael qui se lève."
    noam "La chaise qui racle."

    pause 0.3

    think "Et cette porte."
    think "Clac. Fin de discussion."

    pause 0.4

    noam "Elle va voter contre."
    noam "Bien sûr qu'elle va voter contre."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with dissolve

    think "Je me redresse. Mauvais choix."

    noam "Oh... wow."
    noam "C'est quoi cette douleur dans la nuque ?!"

    pause 0.3

    noam "Et dans le dos aussi…"

    think "Le métal froid traverse mes chaussettes."

    noam "Hhh..."

    think "Au moins, ça réveille."

    pause 0.3

    think "Je bois trop vite. Mon estomac dépose une protestation officielle."

    pause 0.4

    think "Le vote."

    noam "Aujourd'hui, on est au jour cinq."
    noam "Vote... jour six."
    noam "Donc demain."

    pause 0.4

    noam "Demain."

    think "Demain. Le mot reste dans la chambre, froid et beaucoup trop proche."

    think "Sael ne changera pas d'avis toute seule."
    think "Je ne suis même pas sûr qu'on puisse la faire changer d'avis…"

    pause 0.3

    noam "Et moi, je suis censé faire quoi ?"

    pause 0.5

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits diablotins !"
    kami "Alors ?"
    kami "Vous avez mal au crâne ? Ça tangue un peu ? Beaucoup ?"
    kami "Certains regrettent déjà deux ou trois choix de la veille ?"
    kami "Il faut dire que le public a été surpris par certains événements !"

    pause 0.2

    kami "Rassurez-vous."
    kami "C'est parfaitement normal."
    kami "Fatigue, alcool, tensions politiques, jeu de la bouteille..."
    kami "Franchement, je m'étonnais presque que vous n'ayez pas craqué avant !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais assez parlé de vos performances rocambolesques."
    kami "Petit point sérieux."
    kami "Oui, je sais."
    kami "Moi aussi, ça me déçoit mais il faut bien travailler un peu."

    pause 0.2

    kami "Cette nuit, Orbite a déclenché une alerte de sécurité."
    kami "Quelqu'un n'a pas respecté les règles. Le complexe C-3 a donc reçu un petit rappel au laser."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Peut-être même que c'est à cause de vous !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Heureusement, aucun autre mort à déclarer."
    kami "Juste quelques personnes dans le coma parce qu'elles n'ont pas réussi à mettre leur scaphandre à temps."
    kami "Deux heures et quelques d'ambiance absolument délicieuse."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Le complexe est en cours de réparation."
    kami "Rien d'irréversible."
    kami "Tout est revenu à la normale."

    pause 0.3

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Enfin..."
    kami "À la normale pour eux."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Pendant que vous, vous êtes bien en sécurité ici, certains risquent leur vie."


    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh, et j'ai repéré une petite poussière morale."
    kami "Un rien. Ou presque."
    kami "Un représentant d'Orbite n'était même pas au courant."
    kami "Pas cette nuit."
    kami "Pas pendant que son district retenait son souffle."

    pause 0.3

    kami "C'est drôle, non ?"
    kami "Représenter des gens dont on ignore même quand ils manquent presque d'air."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Comme quoi..."
    kami "Certaines informations circulent mieux quand on est sobre."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "La cafétéria est ouverte."
    kami "Continuez à m'amuser ! C'est peut-être la seule chose dans laquelle vous excellez !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.4

    think "L'écran s'éteint après avoir soigneusement choisi sa cible."

    noam "Orbite… Putain."
    pause 0.4

    think "Je me lève. Trop vite."

    noam "Mauvaise idée."
    noam "J'ai encore la tête qui tourne…"

    think "La chambre penche. Le mur me rattrape."

    noam "Merci, le mur."
    noam "Toujours là dans les moments importants."

    pause 0.3

    think "Je retrouve mes chaussures et les enfile."

    pause 0.2

    noam "..."
    noam "Pourquoi elles sont inversées ?"

    pause 0.3

    think "Bravo."

    think "Je recommence, cette fois comme un adulte presque respectable."

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    think "Le couloir sent le café, le métal et la mauvaise décision."

    noam "Parfait. Exactement mon état d'esprit."

    pause 0.3

    think "Deux voix basses et tendues viennent des chambres."

    nyra "Tu ne pouvais pas le savoir."

    think "Je m'arrête."

    think "Nyra parle avec quelqu'un."

    think "Nyra parle avec Kael."

    jump _5_1_KAEL_NYRA
    
# Durée : 2m15
# Total : 2h 08m 30s

label _5_1_KAEL_NYRA:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    pause 0.5

    think "Kael est assis au sol. Nyra reste près de lui : pas tendre, mais présente."

    scene bg_cg023 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg023")

    kael "Je viens de voir l'alerte. Ce matin. Dans le relevé de Kami."

    nyra "Je sais. Tu l'as lue combien de fois ?"

    kael "Sept. J'aurais dû la voir cette nuit."

    nyra "Tu dormais."

    kael "Erreur de priorité."

    nyra raison "Non. Besoin humain."

    kael triste "Léa a six ans, Nyra. Cette nuit, il y avait une alerte et moi j'étais là à…"

    pause 0.3

    kael "Jouer."

    nyra "À respirer."

    kael "Pardon ?"

    nyra "Tu n'étais pas en train de trahir Orbite. Tu respirais quelques heures."
    nyra neutre "Tu veux transformer un mauvais timing en faute morale. Pourquoi ?"

    kael "Parce que je connais la procédure."
    kael "Tu sais ce qui se passe quand un sas lâche ?"

    nyra "Oui. Je sais ce qu'un sas qui lâche fait aux gens. Continue."

    kael inquiet "Section isolée. Portes verrouillées. Point de confinement."
    kael "Scaphandre. Col. Gauche. Droite. Verrou central."
    kael "Trente secondes avant la perte de force. Quarante-cinq si tu es entraîné et que tu ne trembles pas."

    nyra "Léa sait faire. Tu lui as appris."

    kael triste "Oui."
    kael "C'est peut-être bien ça le problème."

    pause 0.2

    nyra "Non."

    kael "Si."
    kael triste "Elle devrait apprendre des chansons nulles. Des blagues. Des tables de multiplication."
    kael "Pas une procédure pour survivre quand l'air disparaît."

    pause 0.4

    nyra "Comment tu lui as appris ?"

    kael "Comme un jeu. Quatre jours, cet été."
    kael "Elle riait quand elle ratait l'attache gauche."
    kael triste "Elle disait que le scaphandre lui faisait une tête de grenouille."

    pause 0.3

    nyra "Donc tu lui as donné deux choses : un rire et une chance de survivre. Laquelle tu regrettes ?"

    kael "Elle a six ans."

    nyra "Je l'ai entendu. Et elle a toujours six ans même si tu te détruis ici."

    pause 0.5

    think "Nyra ne promet rien. Elle a compris qu'il n'accepterait aucun mensonge."

    nyra raison "Aide-moi à comprendre. Le C-3, c'est quoi ?"

    kael "C'est le module résidentiel. Dans le bloc famille."

    nyra "Combien de personnes ?"

    kael "Cent quarante."
    kael triste "Dont Léa."

    nyra "Capacité d'isolement ?"

    kael "Oui."
    kael inquiet "Sept modules : quatre résidentiels, deux de production, un central. Chaque jonction a ses sas."
    kael "Une section compromise s'isole. Autonomie : plusieurs jours."

    nyra "Donc, cette nuit, le système a tenu."

    kael "Ouais, heureusement. Cette fois."

    nyra neutre "Cette fois."

    pause 0.4

    kael "Tu vois ?"
    kael "Même toi, tu dis cette fois."

    nyra "Parce que c'est vrai. Tu n'as pas besoin d'une phrase sucrée juste parce que tu es par terre."

    kael "Charmant."

    nyra raison "Utile. Tu préfères."

    pause 0.3

    kael "Je pourrai demander à la contacter ce soir."
    kael triste "Pendant les protocoles, les communications sont coupées ou filtrées."

    nyra "Kami peut refuser. Mais si elle accepte, tu lui diras quoi ?"

    kael "Que je suis désolé."

    nyra "Pour quelle action précise ?"

    kael "Ne pas avoir su."

    nyra "Elle te demandera si tu pouvais réparer le sas à distance, les yeux fermés depuis le Conclave. Tu répondras quoi ?"

    kael "Nyra."

    nyra raison "Tu veux t'excuser pour quelque chose que tu ne pouvais ni voir ni empêcher."
    nyra "Cette excuse soulage qui ? Léa, ou toi ?"

    pause 0.5

    kael "..."

    nyra "Voilà."

    kael "T'es horrible."

    nyra neutre "Non. Je refuse seulement de t'aider à te punir."

    pause 0.4

    think "Kael lâche un rire sec. Pas joyeux, mais vivant."

    kael "J'ai la tête qui tourne."

    nyra "Alcool ou culpabilité ?"

    kael "Les deux."

    nyra "Certains conseillent de reboire après une cuite. Une idée catastrophique, donc parfaitement adaptée à cette semaine."

    kael "Tu veux me tuer ? Déjà que…"

    think "Kael devient rouge. Le souvenir de la veille vient de le rattraper."

    kael "Rien."

    nyra raison "J'ai une idée très précise du souvenir qui vient de te rattraper."

    kael "Ne te moque pas."

    nyra "Je ne me moque pas. Ça nous a fait du bien de souffler. Tu viens de le prouver."

    pause 0.4

    "Kael se relève lentement."

    scene bg_couloir at adaptive_fullscreen with dissolve

    $ showP("kael", "calme", 0.65)
    $ showP("nyra", "raison", 0.45)

    kael "Bon."
    kael "Je vais essayer d'avaler un bout."
    kael "Après… je verrai."

    nyra "Après, tu verras."

    think "Il passe sans me parler. Il sait que j'ai tout entendu."

    hide kael
    with moveoutright

    $ showP("noam", "neutre", 0.15)

    nyra "Tu as tout entendu ?"

    noam "Oui."

    nyra neutre "Bien."

    noam "Bien ?"

    nyra "Oui."
    nyra raison "Les informations importantes doivent circuler. La douleur aussi, parfois."
    nyra "Une crise à Orbite ne se gère jamais seul. Kael avait besoin de s'entendre répondre."

    noam "Même quand ça fait mal ?"

    nyra "Surtout quand ça fait mal. C'est là qu'on touche quelque chose de vrai."

    hide nyra
    with moveoutright

    pause 0.5

    think "Nyra suit Kael à distance. Assez près pour l'aider, assez loin pour qu'il marche seul."

    think "Cent quarante personnes. Dont Léa…"
    think "Sa petite sœur, visiblement."

    noam "Pas étonnant qu'il culpabilise…"
    noam "Ce Conclave mélange des mondes qui n'auraient jamais dû se toucher, puis nous demande de voter sur les dégâts."

    pause 0.4
    $ unlock_codex_page("complexe_c")

    jump _5_1_CAFETERIA_MATIN

# Durée : 3m30
# Total : 2h 12m 00s

label _5_1_CAFETERIA_MATIN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    pause 0.8

    think "La cafétéria ressemble à un lendemain de fête condamné sans appel."

    $ showP("kael", "neutre", 0.12)
    $ showP("elen", "fatigue", 0.50)
    $ showP("ryn", "blase", 0.88)

    elen fatigue "Kael..."

    kael "Oui. J'ai vu."

    elen "Je voulais pas— enfin, hier, on savait pas et… ça va ?"

    kael "Ça ira. Pas maintenant. Mais ça ira."

    ryn "Traduction : non."

    kael "Traduction : je mange."

    elen fatigue "D'accord. Oui. Mange. Je peux te trouver un truc sucré si— non. Mange d'abord."

    ryn blase "Moi, c'est Limen qui me fait flipper."

    elen "Les marchés ?"

    ryn "Les files."
    ryn "Regarde l'écran. Les gens attendent toujours leurs rations."
    ryn "Comme s'ils allaient en avoir…"

    elen "Kami a dit que les marchés fonctionnaient. Ça va prendre un peu de temps, mais ça va démarrer."
    elen reflexion "Ça doit démarrer."

    ryn "Les marchés fonctionnent pour ceux qui ont un truc à vendre."
    ryn blase "Pour les autres, c'est juste une façon plus chic de crever debout."

    elen "Ryn… non, il faut juste—"

    ryn "Quoi ? C'est vrai, non ?"

    hide elen
    $ showP("tomas", "hesitation", 0.50)

    tomas hesitation "Euh… techniquement, les premières tensions étaient prévisibles."
    tomas "Quand on change le système il faut toujours un temps d'adaptation."

    ryn "Ton modèle, il a mangé ce matin ?"

    tomas "Je… c'est une image ou une vraie question ?"

    ryn "Les deux."

    tomas hesitation "Alors… non. Enfin, un modèle ne mange pas."

    ryn "Voilà. Et les gens veulent juste pouvoir manger."

    kael "Ryn."

    ryn blase "Quoi ? J'ai pas crié."

    tomas hesitation "Non, mais... l'effet était très proche."

    think "Personne ne rit. Tout le monde comprend."

    hide tomas
    hide ryn
    hide kael

    pause 0.3

    think "Je m'installe devant une ration. Elle me regarde. Je la menace. Match nul."

    $ showP("lysa", "blase", 0.12)
    $ showP("iris", "fatigue", 0.50)

    lysa blase "T'as une de ces têtes."

    noam "Merci. J'ai préféré ne pas consulter le miroir ce matin."

    iris fatigue "Non, mais vraiment."

    noam "Oui, Iris, j'avais compris le diagnostic."

    lysa "Si ça peut te rassurer, Dionysos n'a épargné personne."

    iris "Parle pour toi."

    lysa "Je parlais surtout pour toi."

    iris fatigue "Pff."

    noam "C'est beau, cette solidarité féminine."

    iris "Solidarité ? Tu parles."
    iris "Madame n'a pas besoin d'effort pour être belle. Il suffisait de voir sa tête hier soir."


    think "Non."
    think "Je préférerais éviter d'y repenser…"

    hide iris
    hide lysa

    show bg_cg019 at memory_fade(1.5, 2.0, 1.5)

    pause 6.0
    hide bg_cg019


    play sound sfx_door volume 5.0

    think "Une porte s'ouvre derrière nous pendant que mon visage brûle encore."
    think "Timing parfait pour changer de sujet."

    $ showP("julian", "detendu", 0.50)

    julian detendu "Bonjour à tous."

    noam "Il a l'air en forme. C'est louche."

    julian "Voilà donc comment on accueille Julian ?"
    julian sourire "J'ai choisi de transcender la gueule de bois."

    $ showP("lysa", "blase", 0.12)
    lysa blase "Personne ne transcende rien. Tu fais juste mieux semblant que nous."

    julian "C'est déjà une compétence politique."

    $ showP("ryn", "blase", 0.88)
    ryn "Ou un défaut."

    julian detendu "Les deux peuvent être rentables."

    pause 0.3

    julian "Le vote est demain. Nous n'allons pas passer la journée à feindre qu'un autre sujet compte davantage."

    hide ryn
    $ showP("iris", "fatigue", 0.66)
    iris "Rends-nous service : tais-toi jusqu'à ce que les antalgiques fonctionnent."

    julian "Je peux. Julian ne le fera pas."
    julian sourire "S'il faut échouer, nous échouerons debout, après avoir défendu quelque chose."

    lysa "Je vote pour l'échec silencieux. Les Spartiates avaient au moins cette qualité."

    noam "J'aime pas l'admettre, mais Julian n'a pas complètement tort."
    noam "Demain arrive beaucoup trop vite."

    pause 0.3

    hide iris
    $ showP("sael", "neutre", 0.95)

    think "Au bout de la table, Sael est droite, silencieuse, déjà retranchée."

    julian "Sael."

    pause 0.2

    sael "Non."

    julian detendu "Je n'ai pas encore posé la question."

    sael "Tu allais la poser. Certaines paroles font du bruit avant de sortir."
    sael mefiant "Et j'ai dit non."

    hide julian
    $ showP("ryn", "blase", 0.60)
    ryn "Au moins ça a le mérite d'être clair."

    hide ryn
    $ showP("julian", "sourire", 0.50)
    julian sourire "Je voulais seulement ouvrir une discussion."

    sael "Elle est fermée."

    hide lysa
    $ showP("elen", "neutre", 0.20)
    elen inquiet "Sael, on peut juste écouter ? Sans crier, sans porte qui claque, sans— enfin, juste écouter ?"
    hide elen

    sael "Personne n'a à me tirer hors de ma position. J'en sortirai si j'y vois un chemin."

    julian "Personne ne t'oblige. Mais le collectif mérite—"

    sael "Alors n'insiste pas. Les mots répétés ne deviennent pas plus vrais."

    pause 0.3

    think "Julian garde son sourire. Le sourire, lui, accuse le coup."

    julian detendu "Très bien."
    julian "Nous reprendrons cette conversation plus tard."

    hide julian
    with moveoutright

    sael "Tu parleras. Je répondrai si c'est nécessaire. Ce n'est pas la même chose."

    hide sael
    with dissolve

    $ showP("lysa", "neutre", 0.20)

    lysa "Même le banquet de Tantale avait une ambiance plus légère."

    $ showP("iris", "taquin", 0.66)
    iris "Je regrette presque la bouteille. C'est dire le niveau de catastrophe."

    lysa "Vexée de ne pas avoir été choisie ?"

    iris rire "Moi vexée ? Et puis quoi encore."
    iris taquin "Et pour embrasser qui d'abord ?"

    lysa "Aucune préférence ? Dommage."
    lysa taquin "Pour information, Noam embrasse mieux qu'il ne répond aux questions."

    noam "Je vais..."
    noam "Très loin."

    iris taquin "Oh ? Il fuit."

    lysa taquin "Il bat en retraite."

    noam "J'appelle ça une manœuvre stratégique."

    think "Je saisis mon plateau et manque la sortie. Retraite stratégique exemplaire."

    hide lysa
    hide iris

    pause 0.3

    jump _5_1_TEMPS_LIBRE

# Durée : 2m15
# Total : 2h 14m 15s

label _5_1_TEMPS_LIBRE:

    scene bg_couloir at adaptive_fullscreen with dissolve

    noam "Bon."
    noam "Matinée ouverte. Morale fermée."
    noam "On progresse."

    call START_FREE_TIME("_5_1_INFIRMERIE_KAEL") from _call_START_FREE_TIME_5_1

# Durée : 0m15
# Total : 2h 14m 30s

label _5_1_INFIRMERIE_KAEL:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    think "Je quitte la cafétéria sans destination. J'avais seulement besoin de ne plus être là."

    pause 0.2

    think "Sael a fermé la discussion. Julian a encaissé. Moi, j'ai trop mal au crâne pour jouer l'arbitre."

    pause 0.3

    think "Des pas rapides me rattrapent."

    pause 0.2

    $ showP("elias", "panique", 0.50)

    elias "Noam."

    noam "Elias ?"

    elias "Infirmerie. Maintenant."

    pause 0.1

    noam "Qu'est-ce qui—"

    elias "Kael."

    pause 0.3

    noam "Quoi, Kael ?"

    elias inquiet "Il s'est explosé la main. Y a du sang partout. C'est chaud."

    pause 0.2

    noam "Merde."

    elias fatigue "Ouais. Viens vite."

    hide elias
    with moveoutright

    "Elias repart ; je le suis."

    scene bg_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    pause 0.5

    think "L'odeur de désinfectant donne instantanément raison à mon mal de tête."

    pause 0.3

    $ showP("kael", "triste", 0.50)
    $ showP("nyra", "neutre", 0.78)
    $ showP("mara", "stress", 0.22)
    $ showP("elias", "inquiet", 0.05)

    "Kael est assis sur le lit d'examen, la main droite enveloppée d'une compresse rouge."

    pause 0.2

    think "Mara fouille une armoire. Nyra veille près de Kael. Elias tente de fusionner avec le mur."

    pause 0.3

    noam "Kael."

    kael "Salut."

    noam "...Salut ?"

    kael triste "Je n'ai rien trouvé de mieux."

    mara stress "Le mur, par contre, tu l'as trouvé sans difficulté."

    noam "Un mur ?"

    mara "Monsieur a testé sa main contre un mur. Plusieurs fois, pour garantir la rigueur scientifique."
    mara agace "Résultat : mur intact, main ouverte, idée toujours aussi nulle."

    kael "Je te remercie pour cette synthèse."

    mara "Écoute, j'essaie de t'empêcher de repeindre l'infirmerie avec ton sang."
    mara "Pour les dix prochaines minutes, je suis ta meilleure amie. Profite, l'offre expire vite."

    pause 0.3

    noam "Pourquoi tu as fait ça ?"

    pause 0.2

    kael "Kami a refusé ma demande."

    noam "Quelle demande ?"

    kael triste "Contacter Léa."

    pause 0.3

    kael "Je ne demandais pas grand-chose. Trente secondes."
    kael "Même pas le temps d'avoir une vraie conversation."
    kael inquiet "Juste savoir si elle va bien."

    pause 0.4

    noam "Et elle a dit non ?"

    kael "Communications familiales hors priorités du Conclave. Interdites par le règlement."

    pause 0.2

    kael "Et les représentants doivent éviter les distractions émotionnelles avant un vote important."

    pause 0.5

    think "Personne ne trouve de réponse à cette cruauté administrative."

    pause 0.3

    elias inquiet "Il est sorti de la salle de communication et là…"

    kael "Et j'ai frappé un mur."

    mara "Et le mur a gagné. Par décision unanime."

    kael "Ouais. C'était pas la meilleure décision de ma vie."

    pause 0.4

    "Mara revient avec du désinfectant et retire la compresse."

    hide elias
    with moveinleft

    kael "Aïe."

    mara "J'ai pas touché."

    kael "Je prends de l'avance."

    mara "Arrête de prendre des initiatives."

    pause 0.3

    think "Mara nettoie. Kael fixe le mur ; sa main tremble pour une autre raison que le désinfectant."

    pause 0.4

    noam "Tu penses qu'elle est en danger ?"

    kael "Je ne sais pas. Aucune information exploitable."

    noam "Le module s'est isolé correctement ?"

    kael "Oui."
    kael inquiet "Normalement."

    $ showP("elias", "inquiet", 0.05)

    pause 0.3

    kael "Normalement, un sas ne lâche pas en pleine nuit."
    kael "Normalement, une enfant de six ans n'enfile pas un scaphandre en trente secondes."
    kael "Normalement, je peux lui demander si elle va bien."

    pause 0.4

    kael triste "Il y a trop de normalement aujourd'hui."

    pause 0.5

    elias inquiet "Si j'ai compris, les modules résidentiels tiennent plusieurs jours isolés."
    elias "Donc si le protocole a marché, le danger immédiat est limité. C'est concret, ça."

    pause 0.2

    kael "Je sais."

    pause 0.3

    think "Elias se tait et regarde le plafond. Il vient de comprendre quelque chose."

    pause 0.2

    mara "Bon."
    mara "Ta main va survivre."
    mara "Pas l'air d'avoir de fracture. Pas besoin de points, mais tu vas avoir un bleu magnifique."
    mara agace "Ne recommence pas."

    kael "Compris."

    mara "Mauvaise réponse."

    kael "… Pardon ?"

    mara "« Compris », c'est ce que je disais juste avant de recommencer mes conneries."
    mara agace "Je veux 'je ne recommencerai pas'."

    kael "Je ne recommencerai pas."

    mara "C'est déjà mieux."

    pause 0.4

    think "Mara serre le bandage. Kael regarde sa main comme une variable devenue hostile."

    pause 0.4

    kael triste "Je suis pas sûr d'être utile demain."

    noam "Pour le vote ?"

    kael "Oui."

    pause 0.3

    kael "Je savais ce que je pensais. Je le croyais."

    pause 0.2

    kael "Maintenant, tout se mélange : Orbite, Léa, Kami, le vote."

    pause 0.3

    kael triste "Si je lève la main demain, ma peur votera à ma place."

    pause 0.5

    nyra "Alors ne force pas une réponse. Repose-toi."

    mara stress "Demain n'est pas exactement la journée idéale pour rester au lit."

    nyra "Je n'ai pas dit que c'était idéal. J'ai dit qu'il avait le droit de ne pas voter."

    pause 0.3

    elias "La participation n'est pas obligatoire ?"

    think "Elias pose la question mécaniquement, puis découvre nos regards."

    nyra "Elle ne l'est pas. Les règles sont claires : une absence retire seulement le bulletin du décompte."

    pause 0.4

    kael triste "Mais si je ne vote pas…"

    nyra "Ton absence sera enregistrée, pas comptée comme un non. Comme une abstention."
    nyra "Elle ne bloque ni le oui ni le non. Elle réduit seulement le nombre de votes exprimés."

    pause 0.3

    mara mefiant "Tu dis ça comme si c'était simple."

    nyra "Non."
    nyra "Je répète la règle. Pour une fois, elle est assez claire."

    pause 0.5

    think "Le silence change. Plus de panique : du calcul."

    pause 0.3

    noam "Kami demande l'unanimité des votes exprimés."

    think "Je le dis presque pour moi. La phrase ouvre une porte que je n'aime pas."

    pause 0.3

    nyra "Oui."

    pause 0.4

    think "Mara calcule. Elias baisse les yeux. Kael, lui, ne pense déjà plus à la règle."

    pause 0.5

    kael calme "Je vais voter."

    nyra "Dans cet état ?"

    kael "Oui."

    pause 0.3

    kael triste "Si je reste dans ma chambre, je passerai la nuit à recalculer l'impossible."
    kael "Je préfère être là."

    pause 0.3

    think "Nyra n'insiste pas. Elle a obtenu une décision, pas celle qu'elle proposait."

    pause 0.4

    mara "Avant de voter, tu dors."
    mara "Tu manges. Tu te reposes."
    mara agace "Et par pitié, tu mets cette main au repos."

    kael "C'est beaucoup de contraintes."

    mara "J'en ai d'autres en réserve si tu veux."

    kael "Non. Ça ira."

    pause 0.4

    think "Kael baisse les yeux vers sa main bandée."

    pause 0.4

    kael triste "Je veux juste savoir si elle va bien."

    pause 0.6

    think "Personne ne répond. Mara ferme sa trousse. Nyra reste."

    pause 0.2

    think "Elias étudie ses lacets avec une concentration suspecte."

    pause 0.4

    think "Ce silence est la seule réponse honnête."

    pause 0.5

    elias "Je…"

    pause 0.2

    elias fatigue "J'ai laissé un truc allumé. En maintenance."

    pause 0.2

    think "Personne ne lui offre cette sortie."

    elias "Un outil. J'ai laissé un outil allumé."

    pause 0.2

    mara "Elias."

    elias "Ouais."

    mara "T'as l'air vert."

    elias "Je suis fatigué. C'est tout."

    mara "C'est pas la fatigue."

    pause 0.2

    elias "Mais l'outil—"

    mara "Y'a aucun outil."

    elias fatigue "Y a peut-être un outil."

    pause 0.3

    kael "Elias."

    elias "Ouais."

    kael triste "Merci d'être venu."

    pause 0.4

    think "Elias ouvre la bouche, la referme et déglutit."

    elias "… C'est bon."

    hide elias
    with moveoutleft

    think "Il sort beaucoup trop vite pour un outil imaginaire."

    pause 0.4

    mara "Il fait ça à chaque fois."

    noam "Il est parti en trente secondes."

    mara "Vingt-huit."
    mara "Record personnel."

    pause 0.3

    kael triste "Il est quand même venu."

    pause 0.4

    think "Mara range sa trousse. Ses épaules se relâchent malgré elle."

    pause 0.4

    mara "Noam."

    noam "Ouais."

    mara "Viens."

    noam "Où ?"

    mara agace "Dehors."
    mara "Avant qu'on invente un cinquième problème."

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    pause 0.5

    $ showP("mara", "stress", 0.35)
    $ showP("noam", "neutre", 0.65)

    think "La porte se referme sur Kael et Nyra."

    pause 0.2

    think "Elias est adossé au mur, bras croisés, respiration lente. Il essaie très fort de ne pas vomir."

    pause 0.3

    $ showP("elias", "fatigue", 0.15)

    noam "Ça va ?"

    elias "Ouais."

    noam "T'es blanc."

    elias fatigue "Je suis toujours comme ça."

    noam "Non."

    elias "… Non."

    pause 0.3

    mara "Rentre te coucher Elias."

    elias "J'allais—"

    mara "Elias."

    pause 0.2

    elias fatigue "… Ouais. D'accord."

    hide elias
    with moveoutleft

    pause 0.4

    think "Mara le regarde partir et souffle."

    mara "J'aime pas cette journée."

    noam "Moi non plus."

    pause 0.4

    mara "Kael qui se blesse."
    mara "Kami qui refuse trente secondes de communication."
    mara "Elle pouvait faire une exception à ses foutues règles. Trente secondes. Même moi, je tiens trente secondes sans provoquer personne."

    pause 0.3

    mara "Kael devrait se reposer. Mais je comprends qu'il veuille être là demain."
    mara "Je n'avais pas compris qu'une absence disparaissait simplement du décompte…"

    pause 0.5

    think "Elle laisse la possibilité flotter entre nous sans la nommer."

    pause 0.4

    mara "Je retourne vérifier qu'il tape pas dans un deuxième mur."

    noam "Bonne idée."

    mara "Je refuse de lui rebander la main demain. Une fois, c'est du soin. Deux fois, ça devient une relation."
    mara agace "C'est triste d'en être là."

    hide mara
    with moveoutright

    pause 0.5

    think "Mara retourne auprès de Kael. Je récupère de quoi manger, puis regagne ma chambre."

    jump _5_1_CHOIX_CHAMBRE

# Durée : 4m00
# Total : 2h 18m 30s

label _5_1_CHOIX_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    think "Quatre murs. Un lit. Le silence."

    pause 0.3

    think "Exactement ce qu'il me faut."

    pause 0.4

    think "Je laisse mes affaires sur le bureau et file sous la douche."

    scene bg_cg011 at adaptive_fullscreen with dissolve

    pause 1.0

    think "L'eau chaude : seule chose de cette station qui obéit sans négocier."

    pause 0.5

    think "J'y reste beaucoup plus longtemps que nécessaire."

    pause 0.4

    think "Kael et sa main bandée. Elias, blanc dans le couloir."

    pause 0.5

    think "Puis demain. Le carnage annoncé."

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    think "Je m'habille et m'apprête à m'effondrer sur le lit."

    pause 0.3

    think "Et puis je le vois."

    pause 0.4

    "Un papier plié en deux a été glissé sous la porte."

    pause 0.3

    think "Je le ramasse."

    pause 0.4

    think "Une phrase imprimée. Aucune signature."

    pause 0.5

    "« Sont retirés des bulletins exprimés les abstentions et les absences au vote. »"

    pause 0.8

    think "Je relis."

    pause 0.4

    think "Encore."

    pause 0.6

    think "Sont retirés des bulletins exprimés les abstentions et les absences au vote."

    pause 0.5

    think "Mot pour mot, tiré du règlement. Quelqu'un a choisi cette ligne et ma porte."

    pause 0.4

    think "Anonymement. En pleine nuit."

    pause 0.5

    think "Qui ? Et pourquoi faire ?"

    pause 0.6

    think "Je fixe la phrase jusqu'à ce qu'elle commence à ressembler à une instruction."

    pause 0.3

    think "Retirés des bulletins exprimés : les abstentions et les absences."

    pause 0.5

    think "Un absent ne vote ni pour ni contre."

    pause 0.4

    think "L'unanimité s'applique aux présents. Pas aux absents."

    pause 0.6

    think "Je pose le papier. L'idée reste dans ma main."

    pause 0.4

    think "Sael."

    pause 0.3

    think "Sael a fermé la discussion. Elle votera contre. Elle ne changera pas."

    pause 0.5

    think "Si elle ne vote pas…"
    think "Elle ne votera pas contre."

    pause 0.6

    think "C'est simple. Trop simple. Un raisonnement propre tant qu'on ne regarde pas son envers."

    pause 0.4

    think "Je reprends le papier. Une dernière lecture, comme si les mots pouvaient reculer."

    pause 0.5

    think "Pas de signature. Une phrase. Une idée impossible à désapprendre."

    pause 0.6

    think "La pharmacie est à deux couloirs. Je pourrais trouver de quoi retenir Sael au lit demain…"

    pause 0.5

    think "Je pose le papier."

    pause 0.3

    think "Je m'assieds. Qu'est-ce que je devrais faire ?"

    pause 0.6

    menu:
        "Aller à la pharmacie.":
            jump _5_1_PHARMACIE

        "Aller se coucher.":
            jump _5_1_FIN_JOURNEE

# Durée : 0m45
# Total : 2h 19m 15s

label _5_1_PHARMACIE:

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.5

    think "Couloir vide. Lumières bleues au sol. La station respire à voix basse."

    pause 0.4

    think "Je marche lentement. Pas par fatigue : les innocents ne se pressent pas."

    pause 0.3

    think "Si je croise quelqu'un : je ne dors pas, je cherche seulement un somnifère."

    pause 0.3

    think "C'est plausible. Même vrai. Les meilleurs mensonges ont cette propriété."

    pause 0.4

    think "Couloir B. Personne."

    pause 0.2

    think "Couloir C. Toujours personne."

    pause 0.2

    think "Bien."

    pause 0.5

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    pause 0.4

    think "L'infirmerie dort sous une lumière minimale. Le désinfectant, lui, monte la garde."

    pause 0.3

    think "Lit vide. Compresse disparue. Quelqu'un a effacé les traces de Kael."

    pause 0.4

    think "Quatre armoires vitrées. Fermées, pas verrouillées — logique en cas d'urgence."

    pause 0.3

    think "Ce soir, je détourne cette logique à mon avantage."

    pause 0.5

    think "Première armoire."

    pause 0.3

    think "Antalgiques. Anti-inflammatoires. Antihistaminiques. Rien qui serve l'idée."

    pause 0.3

    think "Deuxième armoire."

    pause 0.3

    think "Antispasmodiques. Antibiotiques. Zolpidem."

    pause 0.3

    think "Un somnifère. Mon alibi rendu matériel."

    pause 0.3

    think "J'en prends une. Pour ce soir. Pour dormir."

    pause 0.3

    think "Puis je continue."

    pause 0.4

    think "Troisième armoire."

    pause 0.3

    think "Traitements digestifs. Plusieurs boîtes, plusieurs effets."

    pause 0.5

    think "Je m'arrête. L'idée, elle, avance."

    pause 0.3

    think "Un anti-diarrhéique en gélules."

    pause 0.2

    think "Un laxatif, sous la même forme."

    pause 0.4

    think "Je pose les boîtes côte à côte."

    pause 0.3

    think "Même taille, même forme. Seule l'étiquette change. Dans le noir, sans regarder…"

    pause 0.5

    think "Si quelqu'un prend du Bisacodyl en croyant prendre du Lopéramide."

    pause 0.4

    think "Demain matin. Avant le vote."

    pause 0.3

    think "Cette personne ne sera pas en état de voter."

    pause 0.5

    scene bg_cg024 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg024")

    think "J'échange le contenu des deux boîtes."

    pause 0.3

    think "Proprement. Soigneusement. Comme si la méthode pouvait nettoyer l'acte."

    pause 0.4

    think "Je referme et replace tout exactement."

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    pause 0.5

    think "Mon regard revient aux sachets."

    pause 0.3

    think "Une poudre soluble. Facile à dissimuler dans une boisson."

    pause 0.4

    think "Ça, c'est pour demain. Il restera à trouver comment — et quand."

    pause 0.5

    think "Deux sachets rejoignent le somnifère dans ma poche."

    pause 0.4

    think "Je referme l'armoire."

    pause 0.3

    think "Tout paraît exactement comme avant."

    pause 0.3

    think "C'est peut-être ça, le pire."

    pause 0.6

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    think "Le couloir est toujours vide. Les lumières bleues respirent encore."

    pause 0.3

    think "Je rentre dans ma chambre sans croiser personne."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.4

    think "Je pose les sachets à côté du papier. Cause et conséquence, bien alignées."

    pause 0.3

    think "Je les regarde."

    pause 0.5

    think "Quelqu'un a parié que je ferais ça. Que je fouillerais une pharmacie en pleine nuit."

    pause 0.4

    think "Qui ?"

    pause 0.6

    think "Je ne sais pas. Pas encore."

    pause 0.4

    think "J'avale le somnifère, m'allonge et fixe le plafond."

    pause 0.5

    think "Pour une fois, je dors."

    pause 0.6

    call end_day("6") from _call_end_day_8
    jump _6_1_1_REVEIL_CHAMBRE

# Durée : 2m30
# Total : 2h 21m 45s

label _5_1_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    think "Ma chambre. Le silence. Le papier sur le bureau."

    pause 0.4

    think "Je le regarde encore."

    pause 0.3

    think "« Sont retirés des bulletins exprimés les abstentions et les absences au vote. »"

    pause 0.5

    think "Je le repose face contre le bureau."

    pause 0.4

    think "Quelqu'un voulait que je fasse quelque chose avec ça."

    pause 0.3

    think "Je ne vais pas le faire."

    pause 0.5

    think "Sael votera contre. D'autres aussi, peut-être. Le texte ne passera sans doute pas."

    pause 0.4

    think "C'est possible. Même certain."

    pause 0.3

    think "Mais empêcher quelqu'un de voter ne sauve pas le vote. Ça fabrique seulement un résultat."

    pause 0.5

    think "Et si ça marche comme ça, ça vaut quoi ?"

    pause 0.6

    think "Je me déshabille et m'allonge."

    pause 0.4

    think "Je fixe le plafond."

    pause 0.5

    think "Demain sera ce que demain sera. Formule lâche, mais honnête."

    pause 0.6

    think "Le noir, le silence, la station qui bourdonne dans les murs."

    pause 0.5

    think "Léa a six ans et enfile un scaphandre en trente secondes. Voilà ce que notre monde apprend à ses enfants."

    pause 0.4

    think "Je retourne l'idée dans tous les sens. Elle ne mène nulle part. Comme souvent."

    $ blink()
    pause 0.6

    think "Je ferme les yeux."
    $ blink()

    pause 0.8

    call end_day("6") from _call_end_day_9
    jump _6_1_0_REVEIL_CHAMBRE
