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
    ryn "Regarde l'écran."

    "Sur les murs, Limen attend. Nexus marchande. Les chiffres clignotent comme s'ils avaient honte."

    elen "Kami a dit que les marchés fonctionnaient."

    ryn "Les marchés fonctionnent pour ceux qui ont un truc à vendre."
    ryn blase "Pour les autres, c'est juste une façon plus chic de crever debout."

    elen "Ryn..."

    ryn "Quoi ? C'est moins joli sans graphique ?"

    hide elen
    $ showP("tomas", "hesitation", 0.50)

    tomas hesitation "Euh... techniquement, les premières tensions étaient prévisibles."
    tomas "Le modèle d'ouverture suppose toujours une phase de déséquilibre initial."

    ryn "Le modèle, il a mangé ce matin ?"

    tomas "Je... c'est une image ou une vraie question ?"

    ryn "Les deux."

    tomas hesitation "Alors... non. Enfin, un modèle ne mange pas."

    ryn "Voilà."

    kael "Ryn."

    ryn blase "Je suis calme. C'est mon calme qui parle fort."

    hide tomas
    hide ryn
    hide kael

    pause 0.3

    "Je prends un plateau et m'installe. La ration me regarde. Je la menace du regard. Match nul."

    $ showP("lysa", "blase", 0.12)
    $ showP("iris", "fatigue", 0.50)

    lysa blase "T'as une tête."

    noam "Merci. Je la porte moi-même."

    iris fatigue "Non, mais vraiment."

    noam "Oui, Iris, j'avais compris le diagnostic."

    lysa "Si ça peut te rassurer, on est tous moches ce matin."

    iris "Parle pour toi."

    lysa "Je parlais surtout pour toi."

    iris fatigue "Pff."

    noam "C'est beau, cette solidarité post-fête."

    iris "Je déteste ce faux café."

    lysa "C'est pas du café. C'est une menace liquide."

    iris "Kami nous teste."

    lysa "Kami nous punit. Nuance."

    pause 0.4

    hide iris
    hide lysa

    $ showP("julian", "detendu", 0.50)

    julian detendu "Bonjour à tous."

    noam "Il a l'air réveillé. C'est louche."

    julian sourire "J'ai choisi de transcender la gueule de bois."

    lysa blase "Personne ne transcende rien. Tu fais semblant mieux que nous."

    julian "C'est déjà une compétence sociale."

    ryn "Ou un défaut."

    julian detendu "Les deux peuvent être rentables."

    pause 0.3

    julian "Bon."
    julian "Le vote est demain."
    julian "On ne va pas faire semblant de parler d'autre chose toute la journée."

    iris fatigue "On peut essayer quand même ?"

    julian "On peut."
    julian sourire "Mais on échouera avec moins d'élégance."

    lysa "Je vote pour l'échec sans élégance."

    noam "Ça ne compte pas encore comme un scrutin officiel."

    pause 0.3

    $ showP("sael", "neutre", 0.88)

    "Sael est au bout de la table. Droite. Silencieuse. Inattaquable."

    julian "Sael."

    pause 0.2

    sael "Non."

    julian detendu "Je n'ai pas encore posé la question."

    sael "Tu allais."

    ryn "Propre."

    julian sourire "Je voulais seulement ouvrir une discussion."

    sael "Elle est fermée."

    elen inquiet "Sael, peut-être qu'on peut juste... écouter ?"

    sael "Écouter n'oblige pas à changer."

    julian "Personne ne t'oblige."

    sael "Alors inutile d'insister."

    pause 0.3

    "Julian garde son sourire. Le sourire, lui, accuse le coup."

    julian detendu "Très bien."
    julian "On parlera plus tard."

    sael "Tu parleras."
    sael neutre "Je répondrai si c'est nécessaire."

    lysa "Ambiance."

    iris "Je regrette presque la bouteille."

    noam "Ne dis pas des choses aussi graves."

    pause 0.4

    "Les écrans continuent. Limen attend. Nexus vend. Orbite répare. Nous, on mâche."

    think "Tout le monde veut sauver quelqu'un."
    think "Personne n'est d'accord sur qui."

    hide julian
    hide sael

    pause 0.3

    jump _5_1_TEMPS_LIBRE

# Durée : 2m15
# Total : 2h 14m 15s

label _5_1_TEMPS_LIBRE:

    scene bg_couloir at adaptive_fullscreen with dissolve

    noam "Bon."
    noam "Matinée ouverte. Morale fermée."
    noam "On progresse."

    call START_FREE_TIME("_5_1_APRES_MIDI") from _call_START_FREE_TIME_5_1

# Durée : 0m15
# Total : 2h 14m 30s

label _5_1_APRES_MIDI:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 0.6

    "L'après-midi avance comme un animal prudent. Tout le monde a la même idée. Personne ne veut le dire."

    think "Aller parler à Sael."
    think "Trouver la phrase magique."
    think "Comme si une phrase pouvait réparer une guerre."

    scene bg_conclave at adaptive_fullscreen with dissolve

    pause 0.4

    "Elias est déjà là. Notes ouvertes. Regard trop droit. Sael en face. Mur vivant."

    $ showP("elias", "determine", 0.25)
    $ showP("sael", "neutre", 0.75)

    elias "Sael, regarde-moi. Pas les notes. Moi."

    sael "Je te regarde."

    elias determine "À Limen, trente pour cent de la population est coincée dans quatre kilomètres carrés."
    elias "Quatre."
    elias "Ce n'est pas une ville, c'est une boîte qu'on secoue."

    sael "Je connais les chiffres."

    elias "Alors tu sais que ça ne tient pas."
    elias "Si on n'ouvre pas, la pression reste."
    elias "Si la pression reste, ça casse."

    sael neutre "Tu parles d'humains comme d'un tuyau."

    elias "Je parle d'un système."

    sael "Et moi, je parle des gens pris dedans."

    elias "Justement."

    sael "Non."
    sael "Pas justement."
    sael "Les gens ne se déplacent pas comme des points sur ta carte."
    sael "Ils emportent leurs peurs. Leurs dettes. Leurs armes. Leurs morts."

    elias fatigue "Tu caricatures."

    sael "Tu simplifies."

    elias "Parce qu'il faut décider."

    sael "Non."
    sael "Parce que tu veux que la décision rentre dans ton tableau."

    pause 0.3

    elias determine "D'accord. Parlons concret."
    elias "Limen manque d'espace. Nexus manque de bras sur certains secteurs. Harmonie a des stocks."
    elias "Sans circulation, chaque district pourrit dans sa propre cage."

    sael "Et avec circulation, les plus faibles iront supplier devant la cage des autres."

    elias "Ce n'est pas ce que je propose."

    sael "C'est ce qui arrivera."

    elias "Tu n'en sais rien."

    sael desaccord "Je l'ai vu."

    pause 0.3

    elias "Pas ici."

    sael "Les gens changent de murs. Pas de faim."

    elias "Sael—"

    sael "Non."

    elias "Laisse-moi finir."

    sael "Tu as fini hier."

    elias "Hier, j'ai mal parlé."

    sael "Oui."

    elias fatigue "Je le reconnais."

    sael "Bien."

    elias "Mais ça ne rend pas mes arguments faux."

    sael "Ça rend ta certitude dangereuse."

    pause 0.4

    elias reflechit "Et Orbite ?"

    sael "Orbite est dans l'espace."

    elias "Orbite a besoin de techniciens, de matériel, de rotations. Kael l'a dit."

    sael "Orbite a besoin de corridors contrôlés. Pas d'une libre circulation générale."

    elias "C'est une question de principe."

    sael "Non. C'est là que tu te trompes."
    sael "Quand l'air manque, le principe ne sert à rien."
    sael "Quand les foules bougent, le principe ne les arrête pas."

    pause 0.3

    elias fatigue "T'es sûre que ce n'est pas juste la peur qui parle ?"

    pause 0.5

    "La pièce se bloque. Même moi, j'arrête de respirer."

    sael desaccord "Oui."

    elias "Je voulais dire—"

    sael "Oui, Elias."
    sael "C'est la peur qui parle."
    sael "La vraie."
    sael "Pas celle qu'on écrit en note de bas de page sous un graphique."

    elias "Sael..."

    sael "Tu veux savoir ce que je vois quand tu dis libre circulation ?"

    elias "Je veux comprendre."

    sael "Des portes forcées."
    sael "Des familles qui partent sans savoir où dormir."
    sael "Des hommes qui vendent de la sécurité comme on vend du pain."
    sael "Des enfants qui apprennent trop vite qui il faut éviter dans une foule."

    pause 0.3

    sael "Tes chiffres ne saignent pas, Elias."
    sael neutre "Les gens, si."

    pause 0.5

    elias fatigue "Je pense que tu te trompes."

    sael "Peut-être."

    elias "Et si tu te trompes, des gens restent enfermés à Limen."

    sael "Et si toi tu te trompes, des gens ouvriront des portes qu'ils ne sauront plus refermer."

    pause 0.4

    elias "Alors on fait quoi ?"

    sael "On vote."

    elias "C'est tout ?"

    sael "C'est déjà beaucoup."

    hide elias
    hide sael

    pause 0.5

    "Elias sort. Il tient ses notes comme si elles venaient de le trahir."

    $ showP("elias", "fatigue", 0.50)
    $ showP("noam", "neutre", 0.25)

    elias fatigue "J'ai essayé les chiffres."
    elias "Les projections. Les exemples. Les risques."

    noam "Et ?"

    elias "Elle m'a répondu avec des morts."

    noam "Difficile à contredire."

    elias "Difficile ne veut pas dire juste."

    noam "Non."

    elias fatigue "C'est ça qui me rend fou."
    elias "Elle peut avoir tort et raison en même temps."

    noam "Bienvenue au Conclave."

    elias "Très drôle."

    noam "Pas vraiment."

    elias fatigue "Je n'ai plus d'angle."

    noam "Alors arrête de chercher un angle."

    elias "Et je fais quoi ?"

    noam "Je sais pas."
    noam "Mais si elle voit une arme dans chaque argument, peut-être qu'il faut arrêter de les lui jeter dessus."

    pause 0.3

    elias "..."
    elias "Tu devrais lui parler."

    noam "Moi ?"

    elias "Tu parles comme quelqu'un qui ne sait pas."
    elias "C'est parfois moins insultant que quelqu'un qui sait trop."

    noam "Merci. Je crois."

    hide elias
    hide noam

    pause 0.5

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    pause 0.4

    "Plus tard. Une voix douce dans le couloir. Elen. Pas venue gagner. Venue comprendre."

    $ showP("elen", "inquiet", 0.25)
    $ showP("sael", "neutre", 0.75)

    elen inquiet "Je peux rester là ?"

    sael "Tu es déjà là."

    elen "Oui, mais... moralement."

    sael "Moralement ?"

    elen gene "Je sais pas. Ça sonnait mieux dans ma tête."

    pause 0.2

    sael "Reste."

    elen "Merci."

    pause 0.3

    elen inquiet "Je ne viens pas te forcer."
    elen "Enfin... j'aimerais que tu changes d'avis."
    elen "Mais je ne veux pas te coincer."
    elen gene "Je suis pas très douée pour ça, de toute façon."

    sael "Non."

    elen "Ah."

    sael "Ce n'était pas une insulte."

    elen "Un peu quand même."

    sael fatigue "Un peu."

    pause 0.3

    elen triste "Tu dois avoir des raisons."
    elen "Des vraies."
    elen "Pas juste... je sais pas... de l'entêtement."

    sael "L'entêtement peut être une vraie raison."

    elen "Pas une bonne."

    sael "Ça dépend de ce qu'il protège."

    pause 0.4

    elen "Alors ça protège quoi ?"

    $ showP("sael", "fatigue", 0.75)

    sael fatigue "Une mémoire."

    elen "De Limen ?"

    sael "De la guerre."
    sael "Celle que vous avez vue sur des écrans."
    sael "Moi, je l'ai sentie dans les murs."
    sael "Dans les couloirs trop pleins."
    sael "Dans les gens qui courent sans destination."

    pause 0.3

    elen triste "Tu étais enfant ?"

    sael "Assez pour comprendre."
    sael "Pas assez pour décider."

    elen "C'est cruel, dit comme ça."

    sael "C'était cruel, vécu comme ça."

    pause 0.4

    elen inquiet "Tu es retournée là-bas ?"

    sael "Non."

    elen "Pourquoi ?"

    sael "Parce que là-bas n'existe plus."

    elen "Ton district ?"

    sael "Mon endroit."
    sael "Les cartes ont gardé un nom."
    sael neutre "Pas les voix."

    pause 0.5

    elen triste "Je suis désolée."

    sael "Je ne te demande pas d'être désolée."

    elen "Je sais."
    elen "Mais je le suis quand même."

    pause 0.3

    sael "Tu es toujours comme ça ?"

    elen "Maladroite ?"

    sael "Sincère au mauvais endroit."

    elen "Oui."
    elen gene "Enfin, j'essaie de le faire au bon endroit, mais je vise mal."

    pause 0.3

    sael "Ce n'est pas forcément mauvais."

    elen "Ah."
    elen triste "Merci. Je crois."

    pause 0.4

    elen "Je ne crois pas que tu aies tort."
    elen "Sur le danger."
    elen "Sur la peur."
    elen "Sur ce que ça peut casser."

    sael "Mais ?"

    elen "Mais les gens de Limen..."
    elen inquiet "S'ils veulent partir, ils ont le droit, non ?"

    sael "Les droits sont simples quand ils sont seuls."
    sael "Le droit de partir. Le droit de rester. Le droit de ne pas avoir peur."
    sael "Le problème, c'est quand ils se rencontrent dans un couloir trop étroit."

    elen triste "Je déteste cette réponse."

    sael "Moi aussi."

    elen "Mais tu votes quand même contre."

    sael "Oui."

    elen "Tu es sûre ?"

    sael "Non."

    pause 0.3

    elen "..."

    sael neutre "Je suis décidée. Ce n'est pas la même chose."

    pause 0.5

    elen triste "Je voulais juste que tu saches que ce n'est pas contre toi."

    sael "Je sais."

    elen "Et toi ?"

    sael "Quoi, moi ?"

    elen "Quand tu voteras contre."
    elen "Ce sera contre nous ?"

    pause 0.4

    sael "Non."
    sael fatigue "Ce sera contre ce que j'ai déjà vu."

    hide sael

    pause 0.3

    "Elen recule. Elle m'a vu. Elle ne fait même pas semblant."

    hide elen
    $ showP("elen", "triste", 0.50)
    $ showP("noam", "neutre", 0.25)

    elen triste "Tu as entendu ?"

    noam "Oui."

    elen "C'est nul."

    noam "Quoi ?"

    elen "Comprendre quelqu'un et ne pas changer d'avis."
    elen "J'avais l'impression que comprendre, ça devait aider."

    noam "Ça aide."

    elen "À quoi ?"

    noam "À souffrir plus précisément."

    elen "Super."

    noam "Je ne vends pas du rêve."

    elen triste "Elle non plus ne changera pas."

    noam "Non."

    elen "Et moi non plus."

    noam "Non plus."

    elen "Alors on est juste... bloqués proprement."

    noam "Oui."

    elen "Je déteste ce lieu."

    noam "Il est très détestable."

    hide elen
    hide noam

    pause 0.4

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "L'après-midi s'use. Les tentatives tombent une par une. Pas en fracas. En silence."

    think "Elias a essayé de prouver."
    think "Elen a essayé de comprendre."
    think "Julian doit sûrement essayer autre chose quelque part."
    think "Et Sael reste Sael."

    pause 0.4

    $ showP("nyra", "neutre", 0.50)
    $ showP("noam", "neutre", 0.25)

    nyra "Tu les as vus ?"

    noam "Qui ?"

    nyra "Tous."
    nyra neutre "Elias avec ses chiffres. Elen avec son cœur dans les mains. Julian avec son sourire qui commence à craquer."

    noam "Tu fais des fiches sur nous ?"

    nyra "Pas besoin. Vous êtes lisibles quand vous paniquez."

    noam "Merci, c'est rassurant."

    nyra raison "Rien n'a bougé."

    noam "Non."

    nyra "C'est intéressant."

    noam "C'est surtout décourageant."

    nyra "Les deux peuvent rapporter gros."

    noam "Évidemment."

    pause 0.3

    nyra raison "Il y a une chose que personne ne dit."

    noam "Je sens que je ne vais pas aimer."

    nyra "Probable."

    noam "Vas-y."

    nyra "Si quelqu'un ne peut pas voter..."

    pause 0.3

    nyra "Ça ne compte pas comme un vote contre."

    pause 0.7

    noam "Nyra."

    nyra "Noam."

    noam "Tu viens de dire ça comme si tu parlais d'une règle de carte."

    nyra raison "C'est une règle."

    noam "C'est une personne."

    nyra "Les règles utilisent toujours des personnes."

    noam "C'est immonde."

    nyra "Je n'ai pas dit que c'était beau."

    noam "Tu as dit que c'était intéressant."

    nyra neutre "Oui."

    pause 0.3

    noam "Tu suggères quoi ?"

    nyra "Rien."

    noam "Mensonge."

    nyra raison "Correction : je ne suggère rien à voix haute."

    noam "Pourquoi moi ?"

    nyra "Parce que tu as encore l'air de croire que ne pas choisir te garde propre."

    pause 0.5

    noam "..."

    nyra "C'est tout."

    noam "Non."
    noam "Ce n'est pas tout."

    nyra "Pour l'instant, si."

    hide nyra

    pause 0.7

    "Elle part. La phrase reste. Petite. Polie. Dégoûtante."

    think "Si quelqu'un ne peut pas voter."
    think "Ça ne compte pas comme un vote contre."

    noam "Putain."

    pause 0.4

    jump _5_1_CHOIX_PRINCIPAL

# Durée : 4m00
# Total : 2h 18m 30s

label _5_1_CHOIX_PRINCIPAL:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.6

    "Le soir. Ma chambre. Le plafond. Moi, en dessous, pas beaucoup plus avancé."

    noam "Sael ne changera pas."
    noam "Pas demain."
    noam "Pas avec des chiffres."
    noam "Pas avec des larmes."
    noam "Pas avec Julian qui sourit comme si le monde lui devait une faveur."

    pause 0.3

    think "Nyra savait."
    think "Elle savait exactement où planter la phrase."

    noam "Si quelqu'un ne peut pas voter..."

    pause 0.3

    noam "Ça ne compte pas comme un vote contre."

    "La pharmacie revient dans ma tête avec une précision honteuse."

    noam "Non."

    pause 0.2

    noam "Enfin..."

    pause 0.2

    noam "Non."

    pause 0.3

    think "Pas la blesser."
    think "Pas la briser."
    think "Juste l'empêcher d'être là."

    noam "Écoute-toi."
    noam "Vraiment, écoute-toi."

    pause 0.4

    think "Et Limen ?"
    think "Et les files ?"
    think "Et ceux qui restent enfermés parce qu'une seule voix dit non ?"

    noam "Je déteste cette journée."

    pause 0.4

    menu:
        "Aller à la pharmacie.":
            jump _5_1_PHARMACIE

        "Aller se coucher.":
            jump _5_1_FIN_JOURNEE

# Durée : 0m45
# Total : 2h 19m 15s

label _5_1_PHARMACIE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    "Le couloir est presque vide. Tant mieux. C'est déjà assez moche sans public."

    noam "Je marche."
    noam "Normalement."
    noam "Pas trop vite."
    noam "Quelqu'un de normal marche comme ça."

    pause 0.3

    "Je passe devant la chambre de Sael. Porte fermée. Silence total."

    noam "Désolé."

    pause 0.2

    noam "Non."
    noam "Même ça, c'est lâche."

    scene bg_pharmacie at adaptive_fullscreen with dissolve

    pause 0.4

    "La lumière automatique s'allume. Étagères propres. Étiquettes propres. Intention beaucoup moins propre."

    noam "Ok."
    noam "Qu'est-ce que je cherche ?"

    think "Laxatif. Purge légère. Trouble digestif. Quelque chose qui ne laisse pas de trace dramatique."

    noam "Je ne suis pas médecin."
    noam "Je suis à peine qualifié pour choisir un petit-déjeuner."

    pause 0.3

    "Anti-nauséeux. Antiseptique. Antidouleur. Bandages. Suppléments. Trop de noms, pas assez de courage."

    noam "Là."

    pause 0.3

    "Petite boîte beige. Comprimés. Effet purgatif doux. Déconseillé avant activité physique soutenue."

    noam "Parfait."

    pause 0.2

    noam "Non."
    noam "Pas parfait."
    noam "C'est même exactement le contraire de parfait."

    pause 0.4

    think "C'est pas irréversible."
    think "C'est juste une absence."
    think "Une journée ratée."
    think "Un vote qui passe."

    noam "C'est une personne."

    pause 0.3

    think "C'est aussi des milliers de personnes."

    noam "Arrête."

    pause 0.3

    "Un bruit dans le couloir. Je me fige."

    noam "..."

    pause 0.5

    "Des pas. Ils ralentissent. Mon cœur, lui, accélère comme un imbécile."

    noam "Pas maintenant."

    pause 0.6

    "Les pas repartent. Disparaissent."

    noam "Ok."
    noam "Je viens officiellement d'avoir peur d'être surpris avec des laxatifs."
    noam "Niveau de dignité : souterrain."

    pause 0.4

    "Le terminal clignote à l'entrée. Kami observe. Kami sait. Kami adorera sûrement."

    noam "Tu regardes, hein ?"

    pause 0.2

    noam "Bien sûr que tu regardes."

    pause 0.4

    think "Si Kami voit ça, elle ne dira rien."
    think "Pas par bonté."
    think "Par curiosité."

    noam "Tu veux voir jusqu'où je descends ?"

    pause 0.3

    noam "Moi aussi, apparemment."

    pause 0.4

    "Je pense à Sael. À ses portes forcées. À ses gens qui saignent."

    noam "Elle a raison."

    pause 0.2

    "Je pense à Limen. Aux files. Aux gens coincés."

    noam "Elias aussi."

    pause 0.3

    noam "C'est ça le problème."

    pause 0.4

    "La boîte est légère dans ma main. Trop légère pour ce qu'elle vient de devenir."

    noam "Je pourrais la reposer."

    pause 0.2

    noam "Je devrais la reposer."

    pause 0.5

    "Je ne la repose pas."

    pause 0.3

    "Je glisse la boîte dans ma poche."

    noam "Putain."

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    "Le couloir est silencieux. Personne n'a vu. Ce n'est pas rassurant."

    noam "Allez."
    noam "Marche."
    noam "Comme quelqu'un qui n'a rien volé à sa propre conscience."

    jump _5_1_FIN_JOURNEE

# Durée : 2m30
# Total : 2h 21m 45s

label _5_1_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.6

    "Ma chambre. La porte. Le clic de fermeture. Le genre de bruit qui ressemble à un jugement."

    noam "Bon."

    pause 0.2

    noam "Journée terminée ?"

    pause 0.2

    noam "Pas vraiment, non."

    $ blink()

    "Le plafond est toujours là. Fidèle. Inutile."

    noam "Kael par terre."
    noam "Nyra qui ne console pas, mais reste."
    noam "Léa qui sait mettre un scaphandre seule."

    pause 0.3

    noam "Elias et ses notes."
    noam "Elen qui comprend trop bien pour être tranquille."
    noam "Sael qui dit non comme on ferme une blessure."

    pause 0.4

    think "Nyra."
    think "Si quelqu'un ne peut pas voter."
    think "Ça ne compte pas comme un vote contre."

    pause 0.3

    noam "Je la déteste pour avoir dit ça."

    pause 0.2

    noam "Je me déteste pour l'avoir compris."

    pause 0.5

    "Je m'allonge. Le lit accepte mon poids sans commentaire. Lui au moins."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    pause 0.4

    $ blink()

    noam "Demain, il y a le vote."

    pause 0.3

    noam "Un oui."
    noam "Un non."
    noam "Une absence."
    noam "Et tout un monde coincé entre les trois."

    pause 0.5

    think "Je pensais qu'une décision, c'était choisir ce qui est juste."
    think "Ici, c'est choisir ce qu'on accepte de salir."

    pause 0.5

    $ blink()

    noam "J'aimerais avoir une phrase propre pour finir la journée."

    pause 0.3

    noam "J'en ai pas."

    pause 0.5

    "Le sommeil arrive sans douceur. Il me prend avant que je trouve une excuse."

    $ blink()
    pause 1.5

    $ current_day = 6
    pause 1.0

    call end_day("6") from _call_end_day_6_1
    jump _6_1_REVEIL_CHAMBRE

# Durée : 1m20
# Total : 2h 23m 05s
