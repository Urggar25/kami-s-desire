label _8_1_0_0_REVEIL:

    $ current_day = 8
    $ current_period = "Matin"

    scene black with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    "J’ouvre les yeux avant même que la sonnerie de Kami ne retentisse."

    scene bg_chambre at adaptive_fullscreen with Fade(1.5, 0.0, 2.0)

    "Pendant quelques secondes, je reste allongé sans bouger, encore à moitié endormi dans le silence de la chambre."

    think "Pas de réveil insupportable, pas de voix de Kami. Pas encore."

    "Je tourne légèrement la tête vers l’horloge."

    noam reflexion "..."

    think "Je me suis réveillé tout seul ? Ça faisait longtemps."

    "Je me redresse et passe une main sur mon visage, puis la journée d’hier me revient immédiatement."

    think "La fille."

    "Je me lève presque aussitôt."

    think "Iris devait la surveiller cette nuit. Je devrais aller voir si tout va bien avant que les autres commencent à sortir de leurs chambres."

    "J’enfile rapidement mes vêtements et quitte la pièce."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_8_1_0_0_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Le couloir est encore presque vide, éclairé par quelques lumières nocturnes le long des murs. Je marche jusqu’à la chambre d’Iris."

    stop music fadeout 1.0

    "Alors que j’arrive devant sa porte..."

    play sound "audio/sfx_thud.mp3"

    "Un bruit sourd résonne à l’intérieur."

    pause 0.5

    iris "Arrête de bouger !"

    "Je m’immobilise tandis que quelque chose tombe au sol."

    anya_inconnue peur "Mmph— !"

    iris "Chut !"

    "Un nouveau choc contre un meuble."

    think "Putain."

    "J’ouvre immédiatement la porte."

    jump _8_1_0_0_CHAMBRE_IRIS


label _8_1_0_0_CHAMBRE_IRIS:

    scene bg_cg039 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg039")
    play music "music/bgm_system_override.mp3" fadein 1.5

    "La scène devant moi est... compliquée. La fille d’hier est réveillée, complètement réveillée même."

    "Elle essaie de se dégager du lit tandis qu’Iris tente tant bien que mal de la maintenir en place."
    "Une main plaquée sur sa bouche l’empêche surtout de transformer la chambre en sirène d’alarme."

    "Ses yeux se posent immédiatement sur moi et s’écarquillent."

    anya_inconnue peur "MMMH !"

    iris colere "Mais arrête de gueuler !"

    "Elle se débat de plus belle tandis que je referme rapidement la porte derrière moi."

    noam surpris "..."

    "Iris tourne la tête vers moi."

    iris colere "..."

    "Je m’apprête à parler, mais elle secoue brutalement la tête."

    iris determine "..."

    "Puis elle lève un doigt, non pas vers moi, mais vers le plafond. Je suis son regard jusqu’à la caméra."

    think "Ah."

    "Un morceau de tissu a été fixé devant l’objectif, mais pas complètement."

    "Une grande partie de la chambre est masquée, notamment le lit, mais l’objectif dépasse encore suffisamment pour surveiller l’entrée et une partie de la pièce."

    think "Elle a fait ça pendant la nuit ?"

    "Iris pointe ensuite son oreille."

    think "Le son. Bien sûr."

    "L’image est en grande partie inutilisable... mais pas le micro."

    "La fille continue de fixer Iris avec un mélange de terreur et de haine."

    anya_inconnue peur "Mmph ! MMH !"

    "Iris me désigne alors la porte de la salle de bain. Je comprends immédiatement et m’approche du lit, ce qui pousse la fille à recommencer à se débattre."

    anya_inconnue peur "MMMH !"

    iris colere "..."

    "À deux, nous parvenons tant bien que mal à la faire descendre du lit."
    $ anya_lit_iris = 0

    "Elle essaie de planter ses pieds dans le sol, sans grand succès. Nous traversons maladroitement la chambre en silence ; je manque de trébucher sur une chaussure et Iris me lance un regard noir."

    think "Oui, pardon de ne pas avoir l’habitude de déplacer clandestinement des inconnues paniquées au réveil."

    scene bg_salle_de_bain_iris at adaptive_fullscreen with dissolve

    # Le changement de scène efface le CG et ses personnages intégrés :
    # le groupe doit donc être recréé explicitement dans la salle de bain.
    $ showGroup([
        ("noam", "surpris", 0.20),
        ("iris", "colere", 0.55),
        ("anya", "peur", 0.85),
    ])

    "Dès que la porte de la salle de bain se referme derrière nous, Iris relâche enfin sa main."

    anya_inconnue colere "LÂCHEZ-MOI !"

    iris colere "Chut !"

    anya_inconnue colere "NE ME TOUCHEZ PAS !"

    "Elle recule brutalement jusqu’au mur."

    anya_inconnue colere "Vous êtes complètement malades !"

    iris colere "Tu peux parler moins fort ?!"

    anya_inconnue colere "Vous m’avez kidnappée !"

    noam surpris "Quoi ?"

    anya_inconnue colere "Je sais très bien ce que vous faites !"

    "Elle cherche quelque chose autour d’elle, probablement n’importe quel objet susceptible de servir d’arme."

    "Son regard s’arrête une demi-seconde sur une bouteille de shampoing, puis sur la brosse des toilettes."

    iris desaccord "Pose immédiatement cette idée dans ta tête."

    anya_inconnue inquiet "Où je suis ?!"

    noam inquiet "Écoute—"

    anya_inconnue inquiet "Vous êtes avec eux ?!"

    noam reflexion "Avec qui ?"

    anya_inconnue peur "Je sais pas ! Les passeurs ! Les types du réseau !"

    "Elle serre les poings contre elle."

    anya_inconnue colere "J’avais payé jusqu’à Nexus ! On m’avait dit que personne n’ouvrirait le conteneur avant l’arrivée !"

    "Iris et moi échangeons un regard."

    iris reflexion "..."

    noam reflexion "..."

    anya_inconnue colere "Et maintenant je me réveille dans une chambre avec une tarée qui me plaque sur un lit !"

    iris colere "La tarée essaie surtout de t’éviter de nous faire tuer !"

    anya_inconnue desaccord "Ah oui ?! Évidemment ! C’est sûrement pour mon bien !"

    "Elle essaie de passer à côté de nous, mais je me décale simplement devant la porte et elle s’arrête."

    noam determine "Attends."

    anya_inconnue colere "Dégage."

    noam determine "Deux minutes."

    anya_inconnue colere "Je t’ai dit de dégager."

    "Je ne bouge pas."

    noam calme "Deux minutes. Après ça, si tu veux toujours ouvrir cette porte en hurlant, tu le feras."

    iris surpris "Noam—"

    "Je regarde Iris."

    noam determine "Laisse."

    "Elle me fixe quelques secondes."

    iris desaccord "..."

    "Puis croise les bras."

    anya_inconnue desaccord "..."

    "La fille ne semble pas vraiment rassurée, mais au moins, elle ne cherche plus à nous passer dessus."

    noam calme "Tu n’es pas à Limen."

    anya_inconnue inquiet "..."

    noam "Tu es dans le Conclave."

    "Son expression change, pas beaucoup, mais juste assez pour que je le remarque."

    anya_inconnue surpris "... Quoi ?"

    noam "Le Conclave. La station."

    anya_inconnue desaccord "Non."

    noam reflexion "Si."

    anya_inconnue peur "Non, c’est pas possible."

    "Elle nous observe à nouveau, plus attentivement cette fois. Son regard passe d’Iris à moi, puis revient sur Iris."

    anya_inconnue reflexion "..."

    "Ses sourcils se froncent."

    anya_inconnue surpris "Attendez..."

    iris reflexion "Quoi ?"

    anya_inconnue surpris "... Je vous connais."

    "Iris se raidit légèrement."

    anya_inconnue surpris "Je vous ai déjà vus."

    "Elle me fixe."

    anya_inconnue surpris "Toi surtout."

    noam surpris "Moi ?"

    anya_inconnue reflexion "À la télé."

    pause 0.7

    anya_inconnue surpris "Vous êtes les représentants."

    "Le silence s’installe et je hoche lentement la tête."

    noam "Oui."

    anya_inconnue fatigue "..."

    iris desaccord "Tu comprends maintenant pourquoi on aimerait beaucoup que tu évites de hurler ?"

    "Elle ne répond pas ; toute l’agressivité qui animait son visage quelques secondes plus tôt semble s’effondrer d’un coup."

    anya_inconnue inquiet "Je suis vraiment..."

    "Elle regarde la porte."

    anya_inconnue surpris "... dans le Conclave ?"

    noam "Oui."

    anya_inconnue surpris "Comment..."

    "Elle porte une main à son front."

    anya_inconnue fatigue "Putain..."

    "Ses jambes semblent soudain beaucoup moins solides et elle s’assoit sur le rebord de la baignoire."

    iris inquiet "Doucement."

    anya_inconnue desaccord "Ne me touche pas."

    iris desaccord "D’accord, princesse."
    anya_inconnue colere "Et arrête de m'appeler comme ça."
    iris colere "Très bien. Tu préfères quoi ? Majesté ?"
    noam fatigue "Iris..."
    iris desaccord "Quoi ? Elle m'a demandé d'arrêter. Je cherche une solution."
    anya_inconnue desaccord "Vous êtes toujours aussi insupportables, à la télé ?"
    noam taquin "Ça dépend des jours. Là, elle fait un effort."
    iris colere "NOAM !"

    "Iris recule immédiatement tandis que la fille reste quelques secondes le visage entre les mains."

    anya_inconnue reflexion "Le conteneur..."

    noam reflexion "C’est comme ça que tu es arrivée ici."

    anya_inconnue fatigue "..."

    noam "On t’a trouvée hier matin."

    anya_inconnue surpris "Hier ?"

    noam "Tu étais inconsciente."

    iris reflexion "Et presque congelée."

    "Elle relève lentement la tête."

    anya_inconnue surpris "Vous m’avez sortie de là ?"

    noam "Oui."

    anya_inconnue inquiet "... Pourquoi ?"

    iris desaccord "Parce qu’on n’allait pas te laisser crever dedans."

    "Elle regarde Iris quelques secondes."

    iris gene "Quoi ?"

    anya_inconnue fatigue "Rien."

    "Elle inspire profondément."

    anya_inconnue fatigue "D’accord..."

    "Sa respiration ralentit progressivement."

    anya_inconnue fatigue "D’accord."

    pause 0.5

    anya_inconnue fatigue "Je m’appelle Anya."
    $ unlock_character_name("anya")

    "Elle essuie rapidement son visage."

    anya fatigue "Anya Vess."

    noam sourire "Noam."

    iris desaccord "Elle le sait."

    noam gene "Oui. C’est vrai."

    "Anya laisse échapper un léger souffle qui ressemble presque à un rire nerveux."

    anya fatigue "Ouais. Je sais qui vous êtes."

    "Elle regarde autour d’elle."

    anya reflexion "Enfin... plus ou moins."

    iris reflexion "Et toi, tu viens d'où exactement ?"
    "Anya redresse immédiatement la tête."
    anya desaccord "Pourquoi ? Vous allez me renvoyer là-bas ?"
    noam surpris "Non ! On essaie juste de comprendre."
    anya fatigue "Nexus. Je viens de Nexus."
    iris reflexion "Et le conteneur venait de Limen ?"
    anya desaccord "Oui."
    noam reflexion "T'étais à Limen pour quoi ?"
    anya colere "Pour trois jours ! J'y allais pour trois jours, d'accord ?"
    "Elle me montre trois doigts, comme si j'avais du mal à compter."
    anya fatigue "J'avais même pas pris de chargeur. Trois sous-vêtements, un sac... Voilà."
    noam inquiet "Et quand Kami a fermé les frontières..."
    anya triste "J'y suis restée. Plus d'un an."
    iris inquiet "Ils t'ont refusé le retour ?"
    anya colere "J'aurais préféré ! Au moins j'aurais eu un refus à encadrer."
    noam reflexion "Ils répondaient pas ?"
    anya fatigue "Jamais. J'ai tout demandé. Retour à Nexus, famille, boulot... À la fin, je cochais même des cases qui avaient rien à voir."
    noam surpris "Comme quoi ?"
    anya "Un déplacement familial. J'avais personne à aller voir. Je me suis dit qu'au moins ils vérifieraient."
    iris desaccord "Et toujours rien."
    anya triste "Rien."
    "Elle baisse les yeux. Iris cesse de lui demander quoi que ce soit."
    noam hesitation "Tu peux t'arrêter là si tu veux."
    anya desaccord "Non. T'as demandé. Je vais finir."
    "Elle se frotte les bras, puis reprend."
    anya reflexion "Quand le commerce est revenu, il y avait des conteneurs partout. Des camions qui repartaient, des caisses qu'on ouvrait plus..."
    iris reflexion "Et tu t'es dit que tu pouvais partir avec."
    anya desaccord "Je me suis surtout dit que j'allais devenir folle si je restais."
    noam reflexion "T'as trouvé un passeur ?"
    anya inquiet "Un réseau. Je connais pas les noms. Me les demande pas."
    noam "Je te les demande pas."
    anya reflexion "Ils ont juré que ça partait pour Nexus. Qu'on ouvrirait pas le conteneur en route."
    iris desaccord "Tu les as crus ?"
    anya colere "T'aurais fait quoi, toi ? Attendre encore un an dans ma chambre ?"
    "Iris ouvre la bouche, puis la referme."
    iris fatigue "Je sais pas."
    anya fatigue "Moi non plus, je savais plus."
    "Elle ramène ses jambes contre elle."
    anya reflexion "Y avait de l'air, de l'eau, une couverture. On m'avait dit quelques heures."
    anya triste "Après, il a fait froid. Vraiment froid."

    noam inquiet "Tu te souviens de quelque chose après ça ?"

    anya reflexion "Pas vraiment. J’ai essayé de taper contre la paroi, puis..."

    "Elle secoue la tête."

    anya "Je sais pas. Je me suis réveillée avec elle au-dessus de moi."

    iris colere "Présenté comme ça, c’est vraiment dégueulasse."

    anya "Tu avais ta main sur ma bouche."

    iris colere "Parce que tu hurlais !"

    anya "Je venais de me réveiller kidnappée dans une chambre inconnue !"

    iris "Tu n’as pas été kidnappée !"

    anya "J’avais aucun moyen de le savoir !"

    iris colere "Tu aurais pu attendre cinq secondes avant d’essayer de me casser le nez !"

    anya colere "Tu étais SUR MOI !"

    noam desaccord "D’accord."

    "Elles se taisent."

    noam fatigue "On va considérer que tout le monde avait de bonnes raisons de paniquer."

    iris desaccord "..."

    anya desaccord "..."

    noam "Ça vous va ?"

    iris "Non."

    anya "Non."

    noam fatigue "Parfait."

    "Un silence un peu absurde s’installe, puis Anya regarde de nouveau vers la porte."

    anya reflexion "Pourquoi je suis cachée ?"
    noam hesitation "Parce que Kami sait pas que t'es ici."
    anya surpris "Attends... vous l'avez pas prévenue ?"
    iris desaccord "Tu tiens vraiment à rencontrer son canon ?"
    anya colere "Je tiens à savoir ce que vous comptez faire de moi !"
    noam inquiet "On n'en sait rien. T'es pas représentante et t'étais pas censée être dans la livraison."
    anya inquiet "Donc elle peut me tuer."
    iris fatigue "On veut surtout éviter de lui donner l'occasion."
    anya desaccord "Super. Et je reste enfermée ici jusqu'à quand ?"
    noam fatigue "On cherche une solution."
    anya colere "Vous êtes douze à voter sur le sort du monde et vous savez pas quoi faire d'une fille dans une salle de bain ?"
    noam taquin "Dit comme ça..."
    iris colere "Noam, c'est pas le moment !"
    noam fatigue "Ouais, je sais."
    anya reflexion "Il y a des caméras ?"
    noam determine "Presque partout. Et des micros. Ici, c'est un des rares endroits tranquilles."
    anya inquiet "Et dans la chambre ?"
    iris reflexion "On a un brouilleur."
    anya desaccord "Je vous demande de me cacher et vous m'expliquez que votre IA écoute même les chambres. Ça donne envie de dormir."
    noam reflexion "Pour l'instant, on est quatre à savoir : Iris, Nyra, Tomas et moi."
    anya reflexion "Et si quelqu'un ouvre la porte ?"
    iris determine "Tu fais pas de bruit."
    anya colere "Je sais. J'ai compris !"
    iris desaccord "Après ton réveil, je préfère vérifier."
    anya desaccord "T'étais en train de m'étouffer !"
    iris colere "J'ESSAYAIS DE T'EMPÊCHER DE CRIER !"
    noam fatigue "Vous pouvez vous détester un peu moins fort ? Ça va finir par nous faire repérer."
    "Les deux me fusillent du regard. Au moins, elles sont d'accord sur quelque chose."

    play sound "audio/sfx_beep.mp3"

    "Un son étouffé traverse la porte de la salle de bain, puis la voix familière de Kami résonne depuis les haut-parleurs de la chambre."

    kami "Debout, mes chers représentants ! Une nouvelle merveilleuse journée commence !"

    "Nous nous figeons tous les trois."

    anya peur "..."

    "Pour la première fois depuis son réveil, Anya ne dit absolument rien."

    kami "J’espère que vous avez bien dormi ! Parce que moi, je ne dors jamais !"

    iris fatigue "..."

    noam fatigue "..."

    "Anya nous regarde, puis désigne silencieusement le plafond. Je hoche la tête."

    anya reflexion "..."

    "Elle a compris."

    jump _8_1_0_0_APRES_MATIN


label _8_1_0_0_APRES_MATIN:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Quelques minutes plus tard, je quitte la chambre d’Iris seul."

    "Anya est restée dans la salle de bain le temps que le couloir se remplisse."
    "Iris trouvera un moyen de la faire ressortir sans attirer l’attention."

    think "Anya. Au moins, elle sait où elle est maintenant."

    "Je repense à son histoire."

    think "Un an bloquée à Limen, et tout ça pour finir dans un conteneur qui n’est même pas arrivé à Nexus."

    "Je regarde machinalement les caméras du couloir."

    think "Le pire, c’est qu’elle a eu de la chance : une destination différente, quelques degrés de moins, quelques heures supplémentaires..."

    "Je préfère ne pas terminer cette pensée."

    jump _8_1_0_0_APRES_MIDI


label _8_1_0_0_APRES_MIDI:

    $ current_period = "Après-midi"

    scene couloir_principal at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Le reste de la matinée se déroule étonnamment normalement. Personne ne remarque quoi que ce soit, ou du moins, personne ne le montre."

    "Après le repas, je traverse les couloirs en direction de la salle commune."

    "Plusieurs voix me parviennent un peu plus loin."

    $ showGroup([
        ("julian", "neutre", 0.25),
        ("mara", "neutre", 0.50),
        ("elen", "neutre", 0.75),
        ("tomas", "neutre", 1.00),
    ])

    julian taquin "Franchement, pour une fois, je vois même pas comment on peut transformer ce vote en catastrophe."

    mara desaccord "Ne dis jamais ça ici."

    julian sourire "Pourquoi ?"

    mara reflexion "Parce que chaque fois que quelqu’un prononce cette phrase, Kami trouve un moyen de nous prouver le contraire."

    elen sourire "Moi ça me paraît plutôt logique de l’autoriser."

    tomas reflexion "Les regroupements ?"

    elen sourire "Oui. On passe déjà notre temps ensemble."

    julian taquin "Techniquement, là on est quatre dans le même couloir. Quel scandale."

    mara "La règle vise surtout les rassemblements organisés."

    tomas reflexion "Et même là... je ne vois pas vraiment de raison de l’interdire."

    "Je ralentis légèrement en arrivant à leur hauteur."

    julian sourire "Ah ! Voilà notre expert constitutionnel."

    noam taquin "Je regrette déjà d’être venu."

    julian "Parfait. Alors, Monsieur Harmonie, verdict ?"

    noam reflexion "Sur quoi ?"

    mara "Le prochain vote."

    elen "Autoriser les regroupements de personnes."

    noam "Ah."

    tomas "On disait juste que ça ne devrait pas poser énormément de problèmes."
    noam reflexion "Ouais. Pour une fois, ça a l'air simple."
    julian sourire "Enfin ! Nous allons pouvoir célébrer la victoire avant même le vote."
    mara desaccord "T'as vraiment besoin d'organiser une fête pour chaque phrase que tu prononces ?"
    julian taquin "Ça s'appelle avoir le sens de l'événement."
    elen sourire "Moi je veux bien une fête ! On pourrait faire un gâteau."
    tomas reflexion "On n'a pas encore les résultats."
    elen sourire "Alors on fait le gâteau avant, pour gagner du temps !"
    mara fatigue "Julian, je te préviens : si tu fais un discours devant le gâteau, je le mange pendant que tu parles."
    julian surpris "Vous ne respectez absolument rien."
    noam taquin "Même le gâteau ?"
    julian surpris "Surtout le gâteau."
    "Tomas sourit à peine. Il sait qu'Anya est là, et pourtant il arrive à parler de pâtisserie comme si de rien n'était."

    "La conversation continue encore quelques minutes. Personne ne semble particulièrement inquiet et, après les derniers votes, ça fait presque étrange."

    think "Pas de menace, pas de conflit majeur, pas de moitié du groupe prête à s’étrangler. Pour une fois, ça pourrait réellement être simple."

    "Je regarde Tomas, qui participe normalement à la discussion."

    "Rien dans son attitude ne laisse penser qu’une inconnue est actuellement cachée à quelques couloirs de là."

    think "Au moins, il sait faire semblant."

    "Je ne devrais probablement pas rester trop longtemps non plus."

    noam sourire "Je vais vous laisser."

    julian surpris "Déjà ?"

    noam "J’ai envie de profiter un peu de l’après-midi."

    julian taquin "Regardez-moi ce privilégié avec du temps libre."

    mara "Nous avons tous du temps libre, Julian."

    julian "Pas moi."

    mara reflexion "Qu’est-ce que tu fais ?"

    julian sourire "Rien."

    mara "..."

    julian "Mais je le fais avec beaucoup de sérieux."

    "Je les laisse derrière moi."

    $ hideGroup()

    call START_FREE_TIME("_8_1_0_0_FIN_APRES_MIDI") from _call_START_FREE_TIME_8_1_0_0


label _8_1_0_0_FIN_APRES_MIDI:

    scene couloir_principal at adaptive_fullscreen with dissolve

    "L’après-midi passe sans incident. Je croise plusieurs petits groupes dans les couloirs ; la plupart parlent du vote à venir et, pour une fois, les discussions restent calmes."

    "Certains voient surtout la possibilité de se réunir plus librement."
    "D’autres se demandent simplement pourquoi une règle aussi restrictive existe encore."

    "Mais je n’entends personne défendre sérieusement l’interdiction."

    think "Ça change. J’en viens presque à oublier qu’une fille clandestine dort dans la chambre d’Iris."

    pause 0.5

    think "Presque."

    jump _8_1_0_0_SOIR


label _8_1_0_0_SOIR:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_8_1_0_0_2
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0

    "La soirée finit par tomber sur le Conclave. Après une journée presque trop calme, je retourne vers ma chambre."

    think "Je devrais peut-être passer voir Iris, juste pour vérifier que tout va bien."

    "Je continue d’avancer, puis je m’arrête."

    noam surpris "..."

    "Une porte vient de s’ouvrir quelques mètres devant moi, celle d’Iris. Quelqu’un en sort."

    $ showGroup([
        ("ryn", "neutre", 0.65),
    ])

    "Ryn."

    think "..."

    "Il referme tranquillement la porte derrière lui."

    "Pendant une seconde, mon cerveau refuse presque de traiter ce que je suis en train de voir."

    think "Pourquoi Ryn sort de la chambre d’Iris ?"

    "Il lève les yeux et nos regards se croisent."

    ryn reflexion "Noam."

    noam hesitation "Ryn."

    "Il ne semble pas particulièrement nerveux, ni même surpris."

    ryn "Bonne nuit."

    noam hesitation "... Ouais. Bonne nuit."

    "Il passe à côté de moi et je me décale légèrement pour le laisser passer."

    $ hideGroup()

    "Ses pas s’éloignent progressivement dans le couloir tandis que je reste immobile."

    think "..."

    "Je regarde la porte d’Iris."

    think "Non."

    "Mon ventre se noue."

    think "Ryn n’est pas au courant. Il n’est PAS au courant."

    "Je recompte machinalement."

    think "Iris, Nyra, Tomas et moi. C’est tout."

    "Je fixe encore la porte."

    think "Alors qu’est-ce qu’il foutait là-dedans ?"

    "Ma première impulsion est d’entrer. Je fais même un pas vers la chambre, puis je m’arrête."

    think "Attends. Peut-être qu’Anya était cachée, qu’Iris l’a fait sortir avant et qu’il n’a rien vu."

    "..."

    think "Ou peut-être qu’il a tout vu."

    "Je serre légèrement les poings."

    think "Et si j’entre maintenant en paniquant, je risque surtout d’aggraver les choses."

    "Je regarde derrière moi, mais Ryn a déjà disparu au bout du couloir."

    noam reflexion "..."

    think "Je pourrais demander directement à Iris."

    "Je tends la main vers la porte."

    pause 0.8

    "Puis je la retire."

    think "Non, pas maintenant. Si Ryn a découvert Anya, il faut réfléchir avant de faire quoi que ce soit."

    "Et pour ça, il y a quelqu’un de bien plus doué que moi."

    think "Nyra."

    "Je souffle lentement."

    think "Je lui en parlerai demain matin. Elle saura quoi faire."

    "Je reste encore quelques secondes devant la porte d’Iris, mais aucun bruit ne vient de l’intérieur."

    think "... Enfin, j’espère."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_8_1_0_0_3
    scene bg_chambre at adaptive_fullscreen with fade

    "Je rentre finalement dans ma chambre et m’allonge sur mon lit. La journée avait été presque normale et, pendant quelques heures, j’avais même réussi à croire que nous pouvions réellement cacher Anya ici."

    think "Ryn."

    "Je fixe le plafond."

    think "Pourquoi tu étais dans cette chambre ?"

    stop music fadeout 3.0

    scene black with fade

    call end_day("9", sleeping=True) from _call_end_day_8100
    jump _9_1_0_0_REVEIL
