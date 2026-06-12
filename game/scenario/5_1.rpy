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

    "Bouche sèche. Lumière bleue. Corps officiellement en grève."

    think "Bien fait."

    pause 0.4

    noam "Ok..."
    noam "Objectif numéro un : survivre au fait d'être réveillé."

    pause 0.3

    noam "Objectif numéro deux..."
    noam "Non. Trop ambitieux."

    $ blink()

    think "Hier soir."

    "Les images remontent par morceaux, pas dans le bon ordre."

    noam "Les verres en plastique..."
    noam "La musique..."
    noam "Mara et sa bouteille stupide..."

    pause 0.2

    noam "Lysa."

    pause 0.4

    think "Le jeu de la bouteille."
    think "Sérieusement."

    noam "J'ai participé à ça."
    noam "Et de mon plein gré en plus ..."
    noam "Kami devrait me retirer mon droit de vote juste pour ça."

    pause 0.3

    "Mon estomac répond avant moi."

    noam "Pas maintenant."

    pause 0.4

    "Puis l'autre souvenir revient. Celui qui casse rapidement le petit sourire gêné que je gardais malgré moi."

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

    "Je me redresse. Mauvais choix."

    noam "Oh... wow."
    noam "C'est quoi cette douleur dans la nuque ?!"

    pause 0.3

    noam "Et dans le dos aussi ..."

    "Je pose les pieds au sol. Le métal froid traverse mes chaussettes."

    noam "Hhh..."

    think "Au moins, ça réveille."

    pause 0.3

    "Je prends le verre d'eau. Je bois trop vite."

    pause 0.4

    think "Le vote."

    noam "Aujourd'hui, on est au jour cinq."
    noam "Vote... jour six."
    noam "Donc demain."

    pause 0.4

    noam "Demain."

    "Le mot reste dans la chambre. Bleu. Froid. Beaucoup trop proche."

    think "Sael ne changera pas d'avis toute seule."
    think "Je ne suis même pas sûr qu'on puisse la faire changer d'avis ..."

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
    kami "Franchement, ça m'étonnait presque que vous n'aviez pas craqué avant !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais assez parlé de vos performances rocambolesques."
    kami "Petit point sérieux."
    kami "Oui, je sais."
    kami "Moi aussi, ça me déçoit mais il faut bien travailler un peu."

    pause 0.2

    kami "Cette nuit, Orbite a déclenché une alerte de sécurité."
    kami "Quelqu'un n'a pas respecté les règles, le complexe C-3 a donc été touché par un tir de laser."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Peut-être même que c'est à cause de vous !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Heureusement il n'y a pas d'autres morts à déclarer."
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
    kami "Oh et j'ai repéré une petite poussière morale."
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

    "L'écran s'éteint."

    noam "Orbite. Putain ça fait chier ..."
    pause 0.4

    "Je me lève. Trop vite."

    noam "Mauvaise idée."
    noam "J'ai la tête qui tourne encore ..."

    "La chambre penche. Le mur me rattrape."

    noam "Merci, le mur."
    noam "Toujours là dans les moments importants."

    pause 0.3

    "Je cherche mes chaussures. Je les enfile."

    pause 0.2

    noam "..."
    noam "Pourquoi elles sont inversées ?"

    pause 0.3

    think "Bravo."

    "Je recommence. Cette fois, comme un adulte presque respectable."

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    "Le couloir sent le café, le métal et la mauvaise décision."

    noam "Parfait. Exactement mon état d'esprit."

    pause 0.3

    "Deux voix, vers les chambres. Basses. Tendues."

    nyra "Tu ne pouvais pas le savoir."

    "Je m'arrête."

    think "Nyra parle avec quelqu'un."

    "Je me rapproche pour voir d'où s'élèvent les voix."
    "Elle parle avec Kael."

    jump _5_1_KAEL_NYRA
    
# Durée : 2m15
# Total : 2h 08m 30s

label _5_1_KAEL_NYRA:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    pause 0.5

    "Kael est assis par terre, dos au mur. Nyra est à côté. Pas tendre. Présente."

    scene bg_cg023 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg023")

    kael "Je viens de voir l'alerte."
    kael triste "Ce matin. Dans le relevé de Kami."

    nyra "Je sais."

    kael "J'aurais dû le voir cette nuit."

    nyra "Tu dormais."

    kael "J'aurais pas dû."

    nyra raison "Kael."

    kael "Elle a six ans."
    kael triste "Léa a six ans, Nyra."
    kael "Cette nuit, il y avait une alerte et moi j'étais là à..."

    pause 0.3

    kael "À jouer."

    nyra "À respirer."

    kael "Pardon ?"

    nyra "T'étais pas en train de trahir Orbite. T'étais en train de respirer."
    nyra neutre "Mauvais timing, c'est tout."
    nyra "Et encore, on sait même pas à quelle heure ça a eu lieu."

    kael "Mauvais timing ?"
    kael "Tu sais ce qui se passe quand un sas lâche ?"

    nyra "Ouais je sais. Et chez moi c'est pire encore que chez toi."

    kael inquiet "La section se ferme. Les portes se verrouillent. Tout le monde court au point de confinement."
    kael "Scaphandre. Col. Attache gauche. Attache droite. Verrouillage central."
    kael "T'as trente secondes maximum avant de commencer à perdre tes forces."
    kael "Quarante-cinq pour ceux qui sont vraiment habitués si tu trembles pas."

    nyra "Léa sait faire."

    kael triste "Oui."
    kael "C'est peut-être bien ça le problème."

    pause 0.2

    nyra "Non."

    kael "Si."
    kael triste "Elle devrait apprendre des chansons nulles. Des blagues. Des tables de multiplication."
    kael "Pas comment survivre quand l'air décide de partir à cause d'une fuite."

    pause 0.4

    nyra "Tu lui as appris comment ?"

    kael "Comme un jeu."
    kael "On a bien pris quatre jours. Cet été."
    kael "Elle riait à chaque fois qu'elle ratait l'attache gauche."
    kael triste "Elle disait que le scaphandre lui faisait une tête de grenouille."

    pause 0.3

    nyra "Elle a ri. Et elle a appris."

    kael "Elle a six ans."

    nyra "Je l'ai déjà entendu la première fois."

    pause 0.5

    "Nyra ne promet rien. Kael n'aurait pas supporté un mensonge."

    nyra raison "Le C-3, c'est quoi ?"

    kael "C'est le module résidentiel. Dans le bloc famille."

    nyra "Combien ?"

    kael "Il y a cent quarante personnes."
    kael triste "Dont Léa."

    nyra "Et le module tient seul ?"

    kael "Oui."
    kael inquiet "La station C est séparée en modules. Sept principaux. Quatre résidentiels, deux production, un central."
    kael "Chaque jonction a ses sas. Si une section est compromise, elle s'isole."
    kael "C'est prévu pour tenir plusieurs jours."

    nyra "Donc le système a fait son boulot."

    kael "Ouais, heureusement. Cette fois."

    nyra neutre "Cette fois."

    pause 0.4

    kael "Tu vois ?"
    kael "Même toi, tu dis cette fois."

    nyra "Parce que c'est vrai."
    nyra "Je vais pas te servir une phrase édulcorée et fausse juste parce que t'es par terre."

    kael "Charmant."

    nyra raison "Efficace."

    pause 0.3

    kael "Je pourrai demander à la contacter ce soir."
    kael triste "Pendant les protocoles, les communications sont coupées ou filtrées."

    nyra "Je sais pas si Kami acceptera ..."
    nyra "Tu lui dirais quoi ?"

    kael "Je sais pas."
    kael "Que je suis désolé."

    nyra "Pour quoi ?"

    kael "De pas avoir su."

    nyra "Elle te demandera si t'as réparé le sas avec tes yeux fermés depuis le Conclave ?"

    kael "Nyra."

    nyra "Non, sérieusement."
    nyra raison "Tu veux t'excuser d'un truc que tu ne pouvais pas empêcher."
    nyra "Ça soulage qui ? Elle ou toi ?"

    pause 0.5

    kael "..."

    nyra "Voilà."

    kael "T'es horrible."

    nyra neutre "Non. Je suis juste logique."

    pause 0.4

    "Kael laisse échapper un rire sec. Pas joyeux. Mais vivant."

    kael "J'ai la tête qui tourne."

    nyra "Alcool ou culpabilité ?"

    kael "Les deux."

    nyra "On dit parfois qu'il faut reboire un coup après une cuite, tu devrais essayer."

    kael "Tu veux me tuer c'est ça ?"
    kael "Déjà que ..."

    "Kael devient soudainement rouge pivoine."

    kael "Non rien."

    nyra raison "J'ai bien ma petite idée du souvenir honteux auquel tu viens de repenser"

    kael "Ah ... Te moque pas ..."

    nyra "Je me moque pas, ça nous a fait du bien de souffler un coup."

    pause 0.4

    "Kael pose les mains au sol. Il se relève comme si la journée pesait plus lourd que lui."

    scene bg_couloir at adaptive_fullscreen with dissolve

    $ showP("kael", "calme", 0.65)
    $ showP("nyra", "raison", 0.45)

    kael "Bon."
    kael "Je vais essayer d'avaler un bout."
    kael "Après... je verrai."

    nyra "Après, tu verras."

    "Il passe à côté de moi sans me dire un mot. Il sait que j'étais là."

    hide kael
    with moveoutright

    $ showP("noam", "neutre", 0.15)

    nyra "Tu as tout entendu ?"

    noam "Oui."

    nyra neutre "Bien."

    noam "Bien ?"

    nyra "Oui."
    nyra raison "Les choses importantes doivent circuler."
    nyra "Sur Orbite, les crises sont pas simples à gérer, crois-moi, ça peut lui faire du bien d'en parler."

    noam "Même quand ça fait mal ?"

    nyra "Surtout quand ça fait mal."

    hide nyra
    with moveoutright

    pause 0.5

    "Elle suit Kael plusieurs mètres derrière lui. Le couloir redevient vide et silencieux."

    think "Cent quarante personnes. Dont la fameuse Léa ..."
    think "Sa petite sœur, visiblement."

    noam "Tu m'étonnes qu'il regrette ..."
    noam "Ce Conclave est vraiment une machine à mélanger les mondes qui n'auraient jamais dû se toucher."

    pause 0.4
    $ unlock_codex_page("complexe_c")

    jump _5_1_CAFETERIA_MATIN

# Durée : 3m30
# Total : 2h 12m 00s

label _5_1_CAFETERIA_MATIN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    pause 0.8

    "La cafétéria ressemble à un lendemain de fête qui a perdu un procès."

    $ showP("kael", "neutre", 0.12)
    $ showP("elen", "fatigue", 0.50)
    $ showP("ryn", "blase", 0.88)

    elen fatigue "Kael..."

    kael "Oui. J'ai vu."

    elen "Je voulais pas... enfin, je..."
    elen inquiet "Ça va ?"

    kael "Ça ira."

    ryn "Traduction : non."

    kael "Traduction : je mange."

    elen fatigue "D'accord. Je... oui. Mange."

    ryn blase "Moi, c'est Limen qui me fait flipper."

    elen "Les marchés ?"

    ryn "Les files."
    ryn "Regarde l'écran. Les gens attendent toujours leurs rations."
    ryn "Comme s'ils allaient en avoir ..."

    elen "Kami a dit que les marchés fonctionnaient."
    elen reflexion "Ça va prendre un peu de temps, mais ça va se mettre en route comme il faut."

    ryn "Les marchés fonctionnent pour ceux qui ont un truc à vendre."
    ryn blase "Pour les autres, c'est juste une façon plus chic de crever debout."

    elen "Ryn... Non il faut..."

    ryn "Quoi ? C'est vrai, non ?"

    hide elen
    $ showP("tomas", "hesitation", 0.50)

    tomas hesitation "Euh... techniquement, les premières tensions étaient prévisibles."
    tomas "Quand on change le système il faut toujours un temps d'adaptation."

    ryn "Le modèle, il a mangé ce matin ?"

    tomas "Je... c'est une image ou une vraie question ?"

    ryn "Les deux."

    tomas hesitation "Alors... non. Enfin, un modèle ne mange pas."

    ryn "Voilà. Et les gens veulent juste pouvoir manger."

    kael "Ryn."

    ryn blase "Quoi ? J'ai pas crié."

    tomas hesitation "Non, mais... l'effet était très proche."

    "Personne ne rit vraiment."
    "Mais tout le monde a compris."

    hide tomas
    hide ryn
    hide kael

    pause 0.3

    "Je prends un plateau et m'installe. La ration me regarde. Je la menace du regard. Match nul."

    $ showP("lysa", "blase", 0.12)
    $ showP("iris", "fatigue", 0.50)

    lysa blase "T'as une de ces têtes."

    noam "Merci. J'ai préféré pas me regarder dans le miroir ce matin."

    iris fatigue "Non, mais vraiment."

    noam "Oui, Iris, j'avais compris le diagnostic."

    lysa "Si ça peut te rassurer, on est tous moches ce matin."

    iris "Parle pour toi."

    lysa "Je parlais surtout pour toi."

    iris fatigue "Pff."

    noam "C'est beau, cette solidarité féminine."

    iris "Solidarité ? Tu parles."
    iris "Madame n'a pas besoin de se faire belle pour l'être."
    iris "Il n'y avait qu'à se souvenir de ta tête hier soir."


    think "Non."
    think "Je préfèrerais éviter d'y repenser ...."

    hide iris
    hide lysa

    show bg_cg019 at memory_fade(1.5, 2.0, 1.5)

    pause 6.0
    hide bg_cg019


    play sound sfx_door volume 5.0

    "Une porte s'ouvre derrière nous."
    "Mon visage est encore en train de brûler."
    think "Timing parfait pour changer de sujet."

    $ showP("julian", "detendu", 0.50)

    julian detendu "Bonjour à tous."

    noam "Il a l'air en forme. C'est louche."

    julian "Alors c'est comme ça qu'on m'accueille ?"
    julian sourire "J'ai choisi de transcender la gueule de bois."

    $ showP("lysa", "blase", 0.12)
    lysa blase "Personne ne transcende rien. Tu fais juste mieux semblant que nous."

    julian "C'est déjà une compétence sociale."

    $ showP("ryn", "blase", 0.88)
    ryn "Ou un défaut."

    julian detendu "Les deux peuvent être rentables."

    pause 0.3

    julian "Bon."
    julian "Le vote est demain."
    julian "On ne va pas faire semblant de parler d'autre chose toute la journée."

    hide ryn
    $ showP("iris", "fatigue", 0.66)
    iris "Raah fous-nous la paix."
    iris fatigue "Tu peux essayer de faire ça ?"

    julian "Je peux."
    julian joie "Mais j'en ai pas envie."
    julian sourire "Alors même si on devait échouer, autant échouer avec élégance et en se battant."

    lysa "Je vote pour l'échec sans élégance."

    noam "J'aime pas l'admettre, mais Julian n'a pas complètement tort."
    noam "Demain arrive beaucoup trop vite."

    pause 0.3

    hide iris
    $ showP("sael", "neutre", 0.95)

    "Sael est au bout de la table. Droite. Silencieuse. Inattaquable."

    julian "Sael."

    pause 0.2

    sael "Non."

    julian detendu "Je n'ai pas encore posé la question."

    sael "Tu allais."
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
    elen inquiet "Sael, peut-être qu'on peut juste... écouter ?"
    hide elen

    sael "Personne n'a à m'obliger à changer ma position."

    julian "Personne ne t'oblige. Mais..."

    sael "Alors inutile d'insister."

    pause 0.3

    "Julian garde son sourire. Le sourire, lui, accuse le coup."

    julian detendu "Très bien."
    julian "On parlera plus tard."

    hide julian
    with moveoutright

    sael "Tu parleras."
    sael neutre "Je répondrai si c'est nécessaire."

    hide sael
    with dissolve

    $ showP("lysa", "neutre", 0.20)

    lysa "C'est vraiment joyeux ici."

    $ showP("iris", "taquin", 0.66)
    iris "Je regrette presque la bouteille."

    lysa "Vexée de pas avoir été choisie ?"

    iris rire "Moi vexée ? Et puis quoi encore."
    iris taquin "Et pour embrasser qui d'abord ?"

    lysa "Tu n'as pas de préférence ?"
    lysa taquin "En tout cas Noam embrasse plutôt bien."

    noam "Je vais..."
    noam "Très loin."

    iris taquin "Oh ? Il fuit."

    lysa taquin "Il bat en retraite."

    noam "J'appelle ça une manœuvre stratégique."

    "Je prends mon plateau."
    "Je rate presque la sortie."
    "Évidemment."

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

    "Je quitte la cafétéria sans destination précise."
    "J'avais juste besoin de ne plus être là."

    pause 0.2

    "Sael avait fermé la discussion comme on ferme un dossier."
    "Julian avait encaissé en silence."
    "Moi, j'avais encore trop mal au crâne pour jouer les arbitres."

    pause 0.3

    "J'avance dans le couloir."
    "Puis j'entends des pas."
    "Rapides."

    pause 0.2

    $ showP("elias", "panique", 0.50)

    elias "Noam."

    noam "Elias ?"

    elias "Infirmerie."

    pause 0.1

    elias panique "Maintenant."

    noam "Qu'est-ce qui—"

    elias "Kael."

    pause 0.3

    noam "Quoi, Kael ?"

    elias inquiet "Il s'est blessé ..."
    elias "La main."
    elias "Il y a du sang partout."

    pause 0.2

    noam "Merde."

    elias fatigue "C'est clair, viens vite."

    hide elias
    with moveoutright

    "Il repart sans attendre."
    "Je le suis."

    scene bg_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    pause 0.5

    "L'infirmerie sent le désinfectant."
    "Typiquement le genre d'odeur d'hôpital qui donne mal à la tête."

    pause 0.3

    $ showP("kael", "triste", 0.50)
    $ showP("nyra", "neutre", 0.78)
    $ showP("mara", "stress", 0.22)
    $ showP("elias", "inquiet", 0.05)

    "Kael est assis sur le bord du lit d'examen."
    "Main droite dans une compresse rouge."
    "Il regarde nulle part."

    pause 0.2

    "Mara fouille dans une armoire."
    "Elias se colle au mur près de la porte."
    "Nyra se tient à côté de Kael."

    pause 0.3

    noam "Kael."

    kael "Salut."

    noam "...Salut ?"

    kael triste "J'ai pas vraiment trouvé mieux."

    mara stress "Ouais, par contre le mur lui tu l'as bien trouvé."

    noam "Un mur ?"

    mara "Il a eu la bonne idée de se détruire la main contre le mur."
    mara "Et pas qu'une fois en plus."
    mara agace "Résultat : nul. Méthode : nulle. Recommandation : aucune. Bref il s'est juste explosé la main pour RIEN."

    kael "Je te remercie pour cette synthèse."

    mara "Ecoute, là j'essaye de t'empêcher de repeindre l'infirmerie."
    mara "T'as pas de meilleure amie que moi ce soir."

    pause 0.3

    noam "Pourquoi t'as fait ça ?"

    pause 0.2

    kael "Kami a refusé ma demande."

    noam "Quelle demande ?"

    kael triste "Contacter Léa."

    pause 0.3

    kael "Je voulais pas grand chose. Juste trente secondes."
    kael "Même pas le temps d'avoir une vraie conversation."
    kael inquiet "Juste savoir si elle va bien."

    pause 0.4

    noam "Et elle a dit non ?"

    kael "Elle a dit que les communications familiales ne faisaient pas partie des priorités du Conclave."
    kael "Que c'était de toute façon interdit par les règles."

    pause 0.2

    kael "Et aussi que les représentants devaient éviter les distractions émotionnelles avant un vote important."

    pause 0.5

    "Personne ne parle."

    pause 0.3

    elias inquiet "Il est sorti de la salle de communication après ça. Et là..."

    kael "Et j'ai frappé un mur."

    mara "Et le mur a gagné la bagarre."

    kael "Ouais. C'était pas la meilleure décision de ma vie."

    pause 0.4

    "Mara revient avec du désinfectant et une bande propre."
    "Elle retire la compresse sans prévenir."

    hide elias
    with moveinleft

    kael "Aïe."

    mara "J'ai pas touché."

    kael "Je prends de l'avance."

    mara "Arrête de prendre des initiatives."

    pause 0.3

    "Elle nettoie la plaie."
    "Kael fixe le mur d'en face."
    "Sa main tremble légèrement."
    "Pas seulement à cause du désinfectant."

    pause 0.4

    noam "Tu penses qu'elle est en danger ?"

    kael "Je sais pas, je n'ai aucune information."

    noam "Le module s'est isolé correctement ?"

    kael "Oui."
    kael inquiet "Enfin normalement."

    $ showP("elias", "inquiet", 0.05)

    pause 0.3

    kael "Normalement, un sas ne lâche pas en pleine nuit non plus."
    kael "Normalement, une gamine de six ans devrait pas savoir enfiler un scaphandre en trente secondes."
    kael "Normalement, je devrais pouvoir lui demander si elle va bien."

    pause 0.4

    kael triste "Il y a trop de normalement aujourd'hui."

    pause 0.5

    elias inquiet "Si j'ai bien compris les modules résidentiels sont conçus pour tenir plusieurs jours en isolement ?"
    elias "Si le protocole s'est déclenché correctement, le risque immédiat est limité."

    pause 0.2

    kael "Je sais."

    pause 0.3

    "Elias se tait, il regarde le plafond depuis tout à l'heure."
    "Il vient de comprendre quelque chose."

    pause 0.2

    mara "Bon."
    mara "Ta main va survivre."
    mara "Y'a pas l'avoir d'avoir de fracture."
    mara "Pas de points mais tu auras un sacré bleu."
    mara agace "Ne recommence pas."

    kael "Compris."

    mara "Mauvaise réponse."

    kael "...Pardon ?"

    mara "'Compris', c'est ce que je disais avant de recommencer mes conneries."
    mara agace "Je veux 'je ne recommencerai pas'."

    kael "Je ne recommencerai pas."

    mara "C'est déjà mieux."

    pause 0.4

    "Elle serre le bandage."
    "Kael regarde sa main comme si elle lui avait fait quelque chose de personnel."

    pause 0.4

    kael triste "Je suis pas sûr d'être utile demain."

    noam "Pour le vote ?"

    kael "Oui."

    pause 0.3

    kael "Je sais ce que je pense."
    kael inquiet "Je croyais, en tout cas."

    pause 0.2

    kael "Là tout se mélange."
    kael "Orbite. Léa. Kami. Le vote."

    pause 0.3

    kael triste "Si je lève la main demain, ce sera pas vraiment moi."
    kael "Ce sera juste ma peur qui vote à ma place."

    pause 0.5

    nyra "Alors ne force pas. Repose toi."

    mara stress "Demain c'est pas vraiment une journée pour rester au lit."

    nyra "Je n'ai pas dit que c'était une bonne journée pour ça."
    nyra raison "J'ai dit qu'il en avait le droit de ne pas voter ?"

    pause 0.3

    elias "La participation n'est pas obligatoire ?"

    "Il demande ça mécaniquement."
    "Puis il réalise que tout le monde le regarde."

    nyra "Non. Pas d'après les règles qui ont été expliqué."
    nyra "Exact."

    pause 0.4

    kael triste "Mais si je vote pas..."

    nyra "Ton absence sera comptabilisée, mais ça ne sera pas un vote contre."
    nyra "En fait, c'est plus ou moins comme si tu t'abstenais."
    nyra "Au final, ça n'empêchera ni le vote pour, ni le vote contre de gagner..."

    pause 0.3

    mara mefiant "Tu dis ça comme si c'était simple."

    nyra "Non."
    nyra "Je dis ça parce que c'est ce que disent les règles."
    nyra "Et pour le coup, elles sont assez claires."

    pause 0.5

    "Le silence s'installe."
    "Pas de panique dedans."
    "Juste du calcul."

    pause 0.3

    noam "Kami demande l'unanimité des votes exprimés."

    "Je dis ça à voix basse."
    "Presque pour moi."

    pause 0.3

    nyra "Oui."

    pause 0.4

    "Mara fronce les sourcils."
    "Elias baisse les yeux."
    "Kael n'a pas l'air de penser à la règle."

    pause 0.5

    kael calme "Je vais voter."

    nyra "Dans cet état ?"

    kael "Oui."

    pause 0.3

    kael triste "Si je reste dans ma chambre je vais passer la nuit à réfléchir."
    kael "Je préfère être là."

    pause 0.3

    "Nyra ne répond pas."
    "Elle n'insiste pas davantage."

    pause 0.4

    mara "Avant de voter, tu dors."
    mara "Tu manges. Tu te reposes."
    mara agace "Et par pitié, tu mets cette main au repos."

    kael "C'est beaucoup de contraintes."

    mara "J'en ai d'autres en réserve si tu veux."

    kael "Non... Ça ira."

    pause 0.4

    "Kael baisse les yeux."
    "Sa main bandée repose sur ses genoux."

    pause 0.4

    kael triste "Je veux juste savoir si elle va bien."

    pause 0.6

    "Personne ne répond."
    "Mara referme sa trousse."
    "Nyra ne bouge pas."

    pause 0.2

    "Elias regarde ses chaussures."
    "Depuis un moment."
    "Très attentivement."
    "Comme si ses lacets lui avaient fait quelque chose."

    pause 0.4

    "Ce silence-là, c'est la seule réponse honnête qu'on peut lui donner."

    pause 0.5

    elias "Je..."

    pause 0.2

    elias fatigue "J'ai laissé un truc allumé."

    pause 0.2

    "Personne ne dit rien."

    elias "Dans la salle de maintenance."
    elias "Un outil."
    elias "Je l'ai laissé allumé."

    pause 0.2

    mara "Elias."

    elias "Ouais."

    mara "T'as l'air vert."

    elias "Je suis fatigué."

    mara "C'est pas la fatigue."

    pause 0.2

    elias "L'outil—"

    mara "Y'a aucun outil."

    elias fatigue "Y'a peut-être un outil."

    pause 0.3

    kael "Elias."

    elias "Ouais."

    kael triste "Merci d'être venu."

    pause 0.4

    "Elias ouvre la bouche."
    "La referme."
    "Il déglutit."

    elias "...C'est bon."

    hide elias
    with moveoutleft

    "Il sort."
    "Vite."
    "Vraiment vite."
    "Pour quelqu'un qui avait juste un outil à aller éteindre."

    pause 0.4

    mara "Il fait ça à chaque fois."

    noam "Il est parti en trente secondes."

    mara "Vingt-huit."
    mara "Record personnel."

    pause 0.3

    kael triste "Il est quand même venu."

    pause 0.4

    "Mara ne répond pas."
    "Elle range sa trousse."
    "Mais quelque chose dans ses épaules se relâche légèrement."

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

    "La porte se referme."

    pause 0.2

    "Dans le couloir, Elias est adossé au mur."
    "Les bras croisés."
    "Il respire par le nez."
    "Lentement."
    "Comme quelqu'un qui essaie très fort de pas vomir."

    pause 0.3

    $ showP("elias", "fatigue", 0.15)

    noam "Ça va ?"

    elias "Ouais."

    noam "T'es blanc."

    elias fatigue "Je suis toujours comme ça."

    noam "Non."

    elias "...Non."

    pause 0.3

    mara "Rentre te coucher Elias."

    elias "J'allais—"

    mara "Elias."

    pause 0.2

    elias fatigue "...Ouais. OK."

    hide elias
    with moveoutleft

    pause 0.4

    "Mara le regarde partir."
    "Elle souffle."

    mara "J'aime pas cette journée."

    noam "Moi non plus."

    pause 0.4

    mara "Kael qui se blesse."
    mara "Kami qui refuse trente secondes de communication."
    mara "Elle pouvait quand même faire une exception à ses foutues règles..."

    pause 0.3

    mara "D'un côté Kael devrait se reposer... Mais je comprends qu'il veuille participer au vote."
    mara "J'avais pas compris les règles comme ça..."
    mara "Le fait qu'on puisse ne pas aller voter..."

    pause 0.5

    "Elle laisse ça dans l'air."
    "Sans vraiment conclure."

    pause 0.4

    mara "Je retourne vérifier qu'il tape pas dans un deuxième mur."

    noam "Bonne idée."

    mara "Flemme de lui rebander le bras demain."
    mara agace "C'est quand même triste d'en être là."

    hide mara
    with moveoutright

    pause 0.5

    "Mara retourne dans l'infirmerie."
    "Je reste seul dans le couloir."

    "Je fais un petit tour par la cafétéria pour me prendre un truc à manger."
    "Je retourne dans ma chambre ensuite."

    jump _5_1_CHOIX_CHAMBRE

# Durée : 4m00
# Total : 2h 18m 30s

label _5_1_CHOIX_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    "Quatre murs."
    "Un lit."
    "Le silence."

    pause 0.3

    "C'est exactement ce qu'il me faut."

    pause 0.4

    "Je balance mes affaires sur le bureau et je file sous la douche."

    scene bg_cg011 at adaptive_fullscreen with dissolve

    pause 1.0

    "L'eau chaude."
    "Le seul truc dans cette station qui fait ce qu'on lui demande sans négocier."

    pause 0.5

    "Je reste là un moment."
    "Longtemps."
    "Sans doute bien plus longtemps que nécessaire."

    pause 0.4

    "Je pense à Kael et à sa main bandée."
    "À Elias dans le couloir, blanc comme un linge."

    pause 0.5

    "Je pense à demain, au carnage que ça va être."

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    "Je sors de la douche."
    "Je m'habille."
    "Je m'apprête à m'effondrer sur le lit."

    pause 0.3

    "Et puis je le vois."

    pause 0.4

    "Il y a un papier qui a été glissé sous la porte."
    "Plié en deux."

    pause 0.3

    "Je le ramasse."

    pause 0.4

    "Une seule phrase écrite à l'ordinateur."
    "Le papier a été imprimé."
    "Pas de signature."

    pause 0.5

    "« Sont retirés des bulletins exprimés les abstentions et les absences au vote. »"

    pause 0.8

    "Je relis."

    pause 0.4

    "Je relis encore."

    pause 0.6

    think "Sont retirés des bulletins exprimés les abstentions et les absences au vote."

    pause 0.5

    "C'est tiré du règlement."
    "Mot pour mot."
    "Quelqu'un a copié une ligne du règlement et l'a glissée sous ma porte."

    pause 0.4

    "Anonymement."
    "En pleine nuit."

    pause 0.5

    think "Qui ? Et pourquoi faire ?"

    pause 0.6

    "Je fixe la phrase."

    pause 0.3

    "Sont retirés des bulletins exprimés."
    "Les abstentions."
    "Et les absences."

    pause 0.5

    "Si quelqu'un n'est pas là pour voter."
    "Son vote n'est pas compté."
    "Ni pour."
    "Ni contre."

    pause 0.4

    "L'unanimité s'applique aux votes exprimés."
    "Pas aux absents."

    pause 0.6

    "Je pose le papier sur le bureau."

    pause 0.4

    "Je pense à Sael."

    pause 0.3

    "Sael qui a fermé la discussion ce soir comme on claque une porte."
    "Sael qui votera contre demain."
    "Sael qui ne changera pas d'avis."

    pause 0.5

    think "Si elle vote pas."
    think "Elle ne votera pas contre."

    pause 0.6

    "C'est simple."
    "Trop simple."
    "Le genre de raisonnement qui a l'air propre jusqu'à ce qu'on le retourne."

    pause 0.4

    "Je reprends le papier."
    "Je le relis une dernière fois."

    pause 0.5

    "Pas de signature."
    "Juste une phrase."
    "Et une idée que je peux plus défaire maintenant qu'elle est là."

    pause 0.6

    "La pharmacie est à deux couloirs d'ici."
    "Je pourrais peut être trouver quelque chose qui fera que Sael reste au lit demain..."

    pause 0.5

    "Je pose le papier."

    pause 0.3

    "Je m'assieds sur le lit."
    "Qu'est ce que je devrais faire..."

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

    "Le couloir est vide."
    "Éclairage de nuit."
    "Ces petites lumières bleues au ras du sol qui donnent l'impression que la station respire."

    pause 0.4

    "Je marche lentement."
    "Pas parce que je suis fatigué."
    "Parce que quelqu'un qui marche lentement a l'air de quelqu'un qui a le droit d'être là."

    pause 0.3

    think "Si je croise quelqu'un."
    think "Je peux pas dormir."
    think "Je voulais juste prendre quelque chose pour m'aider à dormir."

    pause 0.3

    "C'est plausible."
    "C'est même vrai."
    "Je peux vraiment pas dormir."

    pause 0.4

    "Je tourne au couloir B."
    "Personne."

    pause 0.2

    "Je tourne au couloir C."
    "Personne non plus."

    pause 0.2

    "Bien."

    pause 0.5

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    pause 0.4

    "L'infirmerie de nuit."
    "Les lumières sont au minimum."
    "Ça sent toujours le désinfectant."

    pause 0.3

    "Le lit d'examen est vide."
    "La compresse rouge a disparu."
    "Quelqu'un a nettoyé."

    pause 0.4

    "Les armoires à pharmacie sont sur le mur du fond."
    "Quatre portes vitrées."
    "Fermées mais pas verrouillées."
    "En cas d'urgence, un verrou serait une mauvaise idée."

    pause 0.3

    "Ce soir, je lui en suis reconnaissant."

    pause 0.5

    "J'ouvre la première armoire."

    pause 0.3

    "Paracétamol en comprimés."
    "Ibuprofène."
    "Antihistaminiques."
    "Prednisolone."

    pause 0.3

    "J'ouvre la deuxième."

    pause 0.3

    "Antispasmodiques."
    "Antibiotiques sous blister."
    "Zolpidem."

    pause 0.3

    think "Zolpidem."
    think "Somnifère."

    pause 0.3

    "Je prends une gélule."
    "Une seule."
    "Pour ce soir."
    "Pour dormir."

    pause 0.3

    "Je continue."

    pause 0.4

    "Troisième armoire."

    pause 0.3

    "Lopéramide en gélules."
    "Bisacodyl en gélules."
    "Macrogol 4000 en sachets-doses."

    pause 0.5

    "Je m'arrête."

    pause 0.3

    "Lopéramide."
    "Anti-diarrhéique."
    "Gélules."

    pause 0.2

    "Bisacodyl."
    "Laxatif."
    "Gélules."

    pause 0.4

    "Je les pose côte à côte sur le bord de l'armoire."

    pause 0.3

    "Les deux boîtes se ressemblent."
    "Même taille."
    "Même forme."
    "Étiquettes différentes."
    "Mais dans le noir, ou sans ses lunettes, ou sans vraiment regarder..."

    pause 0.5

    think "Si quelqu'un prend du Bisacodyl en croyant prendre du Lopéramide."

    pause 0.4

    "Demain matin."
    "Avant le vote."

    pause 0.3

    "Ce quelqu'un ne sera pas en état de voter."
    "Ce quelqu'un ne sera pas en état de faire grand chose."

    pause 0.5

    scene bg_cg024 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg024")

    "J'échange les gélules."
    "Bisacodyl dans la boîte de Lopéramide."
    "Lopéramide dans la boîte de Bisacodyl."

    pause 0.3

    "Proprement."
    "Soigneusement."
    "Comme si l'ordre avait de l'importance."

    pause 0.4

    "Je referme les deux boîtes."
    "Je les replace exactement où elles étaient."

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    pause 0.5

    "Je regarde les sachets de Macrogol."

    pause 0.3

    "Laxatif osmotique."
    "En poudre."
    "À diluer dans un liquide."
    "N'importe quel liquide."
    "Indétectable si le liquide a déjà un goût."

    pause 0.4

    think "Mais ça, c'est pour demain."
    think "Il faudra trouver comment."
    think "Et quand."

    pause 0.5

    "Je prends deux sachets."
    "Je les glisse dans ma poche."
    "À côté du Zolpidem."

    pause 0.4

    "Je referme l'armoire."

    pause 0.3

    "Je regarde l'infirmerie une dernière fois."
    "Tout a l'air exactement comme avant."

    pause 0.3

    "C'est peut-être ça le pire."

    pause 0.6

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    "Le couloir est toujours vide."
    "Les lumières bleues au ras du sol."

    pause 0.3

    "Je rentre dans ma chambre."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.4

    "Je pose les sachets sur le bureau."
    "À côté du papier."

    pause 0.3

    "Je regarde les deux."
    "Un moment."

    pause 0.5

    "Quelqu'un a jugé que je ferais ça."
    "Quelqu'un a glissé ce papier sous ma porte en sachant que je serais là ce soir."
    "À fouiller une armoire à pharmacie à deux heures du matin."

    pause 0.4

    think "Qui ?"

    pause 0.6

    "Je sais pas."
    "Je sais pas encore."

    pause 0.4

    "J'avale le Zolpidem avec un fond d'eau."
    "Je m'allonge."
    "Je fixe le plafond."

    pause 0.5

    "Pour une fois."
    "Je dors."

    pause 0.6

    call end_day("6") from _call_end_day_8
    jump _6_1_1_REVEIL_CHAMBRE

# Durée : 2m30
# Total : 2h 21m 45s

label _5_1_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    "Ma chambre."
    "Le silence."
    "Le papier sur le bureau."

    pause 0.4

    "Je le regarde encore."

    pause 0.3

    "« Sont retirés des bulletins exprimés les abstentions et les absences au vote. »"

    pause 0.5

    "Je le repose."
    "Face contre le bureau."

    pause 0.4

    think "Quelqu'un voulait que je fasse quelque chose avec ça."

    pause 0.3

    think "Je ne vais pas le faire."

    pause 0.5

    "Sael votera contre."
    "Peut-être que d'autres voteront contre."
    "Peut-être, sans doute même, que le texte ne passera pas."

    pause 0.4

    "C'est possible."
    "C'est même certain."

    pause 0.3

    "Mais forcer le résultat en empêchant quelqu'un de voter."
    "Ce n'est plus vraiment un vote."
    "C'est juste un résultat qu'on a fabriqué."

    pause 0.5

    think "Et si ça marche comme ça."
    think "Ça vaut quoi ?"

    pause 0.6

    "Je me déshabille."
    "Je m'allonge."

    pause 0.4

    "Je fixe le plafond."

    pause 0.5

    "Demain sera ce que demain sera."

    pause 0.6

    "Le noir."
    "Le silence."
    "La station qui bourdonne très doucement quelque part dans les murs."

    pause 0.5

    "Je pense à Kael."
    "À sa sœur qui a six ans et qui sait enfiler un scaphandre en trente secondes."
    "À ce que ça dit, au final, du monde dans lequel on vit."

    pause 0.4

    "Je tourne ça dans tous les sens."
    "Ça mène nulle part."
    "Comme d'habitude."

    $ blink()
    pause 0.6

    "Je ferme les yeux."
    $ blink()

    pause 0.8

    call end_day("6") from _call_end_day_9
    jump _6_1_0_REVEIL_CHAMBRE