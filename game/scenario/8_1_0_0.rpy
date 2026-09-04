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

    iris reflexion "Et toi, tu viens d’où exactement ?"

    anya "Nexus."

    noam surpris "Nexus ?"

    "Elle acquiesce."

    anya reflexion "Je suis née là-bas. J’y ai toujours vécu."

    "Elle marque une pause."

    anya triste "Enfin... jusqu’à l’année dernière."

    "Son regard descend vers le sol."

    anya "J’étais à Limen quand Kami a pris le contrôle."

    noam reflexion "Tu étais juste de passage ?"

    anya "Je devais rester trois jours."

    iris inquiet "..."

    anya "Trois jours."

    "Elle laisse échapper un petit rire sans joie."

    anya "J’avais emporté trois sous-vêtements, une tablette et même pas mon chargeur principal parce que je pensais que ce serait rapide."

    anya fatigue "Très bonne préparation pour passer plus d’un an coincée dans un autre district."

    noam "Tu n’as jamais pu rentrer ?"

    anya "J’ai fait plein de demandes."

    anya colere "Transfert exceptionnel. Regroupement familial. Retour vers le district d’origine. Déplacement professionnel. Tout ce que je pouvais cocher dans leurs formulaires."

    anya triste "Jamais de réponse."

    "Elle hausse légèrement les épaules."

    anya "Pas un refus, rien. Juste... rien."

    "Iris baisse légèrement les yeux."

    anya reflexion "Au début je pensais que ça durerait quelques semaines, puis quelques mois. Et après..."

    "Elle souffle."

    anya fatigue "J’ai arrêté de compter."

    noam reflexion "Et depuis le retour du commerce..."

    "Elle relève les yeux vers moi."

    anya "Les conteneurs."

    noam "C’est ça."

    anya "Depuis que les districts recommencent à échanger des marchandises, il y en a partout : des camions, des dépôts, des zones de chargement..."

    anya reflexion "Et forcément, quand quelque chose commence à circuler..."

    iris reflexion "... les gens cherchent à circuler avec."

    anya "Exactement."

    "Elle hésite légèrement."

    anya "J’ai trouvé quelqu’un à Limen."

    noam reflexion "Un passeur ?"

    anya desaccord "Un réseau. Je savais pas qui ils étaient et je voulais pas savoir."

    anya "Ils m’ont expliqué qu’un conteneur devait partir vers Nexus, sans être inspecté au départ ni ouvert pendant le trajet."

    iris desaccord "Et tu les as crus ?"

    anya colere "J’étais enfermée à Limen depuis plus d’un an !"

    "Iris ne répond rien."

    anya fatigue "... Oui. Je les ai crus."

    "Elle ramène ses jambes contre elle."

    anya reflexion "Je suis entrée dedans pendant le chargement. Il y avait de quoi respirer, de l’eau, une couverture... Ils m’avaient dit quelques heures."

    "Elle regarde ses mains."

    anya triste "Après un moment, il a commencé à faire froid."

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

    "Cette fois, personne ne plaisante."

    noam "Parce que Kami ne sait pas que tu es ici."

    anya surpris "..."

    noam "Et on aimerait que ça reste comme ça."

    anya inquiet "Pourquoi ?"

    iris reflexion "Parce qu’on n’a aucune idée de ce qu’elle ferait de toi."

    noam "Tu n’es pas représentante, tu n’étais pas censée être dans cette livraison et, surtout, tu n’étais pas censée entrer dans le Conclave."

    anya inquiet "Elle pourrait me tuer ?"

    "Je ne réponds pas immédiatement."

    iris desaccord "On préfère ne pas vérifier."

    anya "..."

    noam determine "C’est pour ça qu’on doit être extrêmement prudents. Il y a des caméras et des micros dans presque toutes les pièces ; cette salle de bain est l’un des rares endroits où on peut parler tranquillement."

    anya reflexion "Et votre chambre ?"

    iris "Brouilleur."

    anya "..."

    anya inquiet "Combien de personnes savent que je suis ici ?"

    noam "Quatre : Iris, Nyra, Tomas et moi."

    anya "Personne d’autre ?"

    noam "Personne."

    "Elle acquiesce lentement."

    anya reflexion "Donc si quelqu’un entre..."

    iris determine "Tu ne fais aucun bruit."

    anya desaccord "J’avais compris."

    iris desaccord "Vu le réveil que tu viens de m’offrir, je préfère préciser."

    anya colere "Tu veux vraiment qu’on recommence ?"

    iris colere "Essaie."

    noam fatigue "..."

    think "Elles se connaissent depuis environ dix minutes. Ça promet."

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

    noam reflexion "Je pense aussi."

    julian taquin "Cinq personnes d’accord ? Attention, ça ressemble dangereusement à un regroupement."

    mara desaccord "Tu comptes faire cette blague jusqu’au vote ?"

    julian sourire "Absolument."

    elen rire "Moi je l’aime bien."

    mara fatigue "Évidemment."

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

    # TEMPS LIBRE
    # Insérer ici le système de temps libre de la journée.

    jump _8_1_0_0_FIN_APRES_MIDI


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

    call end_day("9") from _call_end_day_8100
    jump _9_1_0_0_REVEIL
