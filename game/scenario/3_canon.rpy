label _3_CANON:

    $ day_id = 3

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.5

    think "…"
    think "Je suis réveillé."
    think "Ou je n’ai jamais vraiment dormi."

    pause 0.4

    think "Mon dos est raide."
    think "Mes yeux piquent."
    think "Ma tête tourne un peu."

    pause 0.4

    think "Je ne bouge pas tout de suite."
    think "Je compte ma respiration."
    think "Une."
    think "Deux."
    think "Trois."

    pause 0.4

    think "Le silence revient."
    think "Un silence propre."
    think "Presque clinique."

    pause 0.4

    think "Hier, il y avait des voix partout."
    think "Aujourd’hui, non."

    pause 0.4

    scene bg_chambre at adaptive_fullscreen with fade

    think "Je regarde le plafond."
    think "Même lumière blanche."
    think "Même angle mort dans le coin gauche."

    pause 0.4

    think "Le couloir derrière la porte est presque muet."
    think "Pas de pas pressés."
    think "Pas de blague forcée."

    pause 0.5

    think "Juste des bruits très courts."
    think "Une poignée."
    think "Un tissu qui frotte."
    think "Puis plus rien."

    pause 0.4

    think "Je ferme les yeux une seconde."
    think "Le vote revient tout de suite."

    pause 0.4

    think "Un seul non, et tout s’écroule."

    pause 0.6

    think "C’est simple."
    think "C’est brutal."
    think "Et c’est pour aujourd’hui."

    pause 0.4

    think "Je me redresse."
    think "Mes épaules craquent."
    think "J’ai l’impression de porter un sac invisible."

    pause 0.4

    "Je passe mes mains sur mon visage."
    "Peau froide."
    "Mâchoire serrée."

    pause 0.4

    "Je me lève."
    "Mes pieds touchent le sol métallique."
    "Le contact me réveille enfin pour de vrai."

    pause 0.4

    "Je bois deux gorgées d’eau."
    "Pas plus."
    "Je n’ai pas faim."

    pause 0.4

    think "Ne pas penser trop loin."
    think "Avancer par étapes."
    think "Atteindre la cafétéria."
    think "Écouter."

    pause 0.4

    "Je me dirige vers la porte."
    "Elle s’ouvre sans bruit."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Le couloir est vide sur quelques mètres."
    "Puis j’aperçois deux silhouettes qui marchent lentement."

    pause 0.4

    "Personne ne salue fort."
    "On se reconnaît d’un regard."
    "C’est tout."

    pause 0.4

    think "Tout le monde économise ses mots."
    think "Comme si parler trop vite pouvait casser quelque chose."

    pause 0.4

    "Je continue jusqu’au carrefour principal."
    "Des portes automatiques glissent."
    "Elles se referment derrière moi."

    pause 0.4

    think "Même le bâtiment semble retenir son souffle."

    pause 0.4

    "Je tourne à droite."
    "Panneau lumineux : CAFÉTÉRIA."
    "Flèche blanche sur fond noir."

    pause 0.4

    "Je suis la flèche."
    "Le bruit de voix augmente un peu."
    "Pas assez pour parler d’agitation."

    pause 0.4

    think "Je croise Kael au détour d’un angle."
    think "On se salue sans ralentir."

    pause 0.4

    think "Je vois aussi Julian près d’un distributeur."
    think "Il me fait un signe bref avec sa tasse."

    pause 0.4

    think "Tout le monde semble déjà en train de calculer."
    think "Ses mots."
    think "Ses limites."
    think "Sa marge de doute."

    pause 0.4

    "Une grille de ventilation souffle au plafond."
    "Le son est continu, régulier, presque hypnotique."

    pause 0.4

    think "Je me force à rester concret."
    think "Ne pas imaginer le pire trop tôt."

    pause 0.4

    "J’ajuste ma manche."
    "Je serre puis desserre mes doigts."
    "Le mouvement ramène un peu de stabilité."

    pause 0.4

    think "Une étape après l’autre."
    think "Cafétéria."
    think "Échanges."
    think "Puis Conclave."

    pause 0.4

    "L’odeur du café réchauffé arrive avant la porte."
    "Avec un fond de métal et de détergent."

    pause 0.4

    think "Même les détails ordinaires me paraissent tranchants."

    pause 0.4

    think "Ça y est."
    think "On y est."
    think "Le jour commence."

    jump _3_CAFETERIA_DEBAT


label _3_CAFETERIA_DEBAT:

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est pleine."
    "Mais les voix restent basses."
    "Comme si les murs pouvaient prendre parti."

    pause 0.4

    "Je prends un plateau."
    "Je n’y mets presque rien."
    "Juste pour avoir quelque chose dans les mains."

    pause 0.4

    "Au fond, Elen et Iris parlent près d’une table."
    "Leurs têtes sont penchées l’une vers l’autre."

    $ showP("elen", "inquiet", 0.22)
    $ showP("iris", "hesitation", 0.50)
    $ showP("noam", "neutre", 0.82)

    noam "Je peux me joindre à vous ?"

    elen "Oui."
    elen "On essaye juste de garder ça clair."

    iris "Et de ne pas paniquer avant midi."

    noam "Bonne stratégie."

    pause 0.3

    elen "Ce qui m’inquiète, c’est l’unanimité."
    elen "Pas la majorité."
    elen "L’unanimité."

    iris "Une personne peut tout bloquer."
    iris "Même si onze sont d’accord."

    noam "Je sais."

    pause 0.3

    elen "Non, justement."
    elen "On dit tous “je sais”, mais on ne le sent pas pareil."
    elen "Certains voient un vote."
    elen "Moi je vois une seule faille possible."

    iris "Et je vois la formulation."
    iris "Si elle est floue, c’est fini."

    noam "Tu penses à quoi exactement ?"

    iris "À un mot mal choisi."
    iris "À une exception oubliée."
    iris "À une phrase qu’on interprète différemment selon les districts."

    pause 0.4

    "Mara arrive avec un plateau chargé."

    hide noam
    $ showP("mara", "neutre", 0.82)

    mara "Vous êtes déjà en mode comité de crise ?"

    elen "On préfère maintenant que trop tard."

    mara "Très bien."
    mara "Alors je vais faire la version moche :"
    mara "Qui applique quoi derrière ?"

    iris "Tu parles de la logistique ?"

    mara "Oui."
    mara "Le concret."
    mara "Les flux."
    mara "Les stocks."
    mara "Les points de passage."
    mara "Le terrain."

    elen "On n’a pas tous les chiffres."

    mara "Justement."
    mara "Donc on doit éviter les promesses irréalistes."

    pause 0.3

    "Nyra, assise à la table voisine, relève les yeux."

    hide elen
    $ showP("nyra", "neutre", 0.22)

    nyra "Le problème n’est pas seulement logistique."
    nyra "Le problème est aussi juridique."

    iris "Juridique ?"

    nyra "Le Commandement est un texte."
    nyra "Un texte se lit."
    nyra "Un texte se tord."
    nyra "Un texte se retourne contre celui qui l’a écrit."

    mara "Voilà, on y est."

    nyra "Si on vote sur une phrase molle, on donne une arme à la première interprétation hostile."

    pause 0.3

    "Tomas pose son verre et se penche en avant."

    hide iris
    $ showP("tomas", "reflechit", 0.50)

    tomas "Je suis d’accord."
    tomas "Il faut séparer :"
    tomas "Ce qu’on autorise explicitement."
    tomas "Ce qu’on interdit explicitement."
    tomas "Et ce qui demande une validation supplémentaire."

    mara "Trois blocs ?"

    tomas "Oui."
    tomas "Sinon chacun projettera sa version."

    nyra "Et il n’y aura pas d’unanimité."

    pause 0.4

    hide mara
    $ showP("noam", "inquiet", 0.82)

    noam "Donc la question n’est pas seulement “pour ou contre”."

    tomas "Non."

    noam "C’est “pour quel texte précis”."

    nyra "Exactement."

    pause 0.3

    elen "On pourrait déjà lister les points qui font peur à tout le monde."

    iris "Oui."
    iris "Comme ça on sait où ça bloque."

    mara "Je commence."
    mara "Peur numéro un : promesse impossible à appliquer."

    tomas "Peur numéro deux : formulation exploitable contre nous."

    nyra "Peur numéro trois : désaccord sur le sens des mots-clés."

    elen "Peur numéro quatre : vote émotionnel, sans verrou."

    noam "Peur numéro cinq : croire qu’on est d’accord alors qu’on ne l’est pas."

    pause 0.4

    "La table voisine écoute désormais clairement."
    "Personne ne coupe."
    "Personne ne rit."

    pause 0.3

    mara "Bon."
    mara "On avance."
    mara "Qui veut une version courte du problème ?"

    iris "Moi."

    mara "On doit voter un texte."
    mara "Pas une intention."

    iris "Parfait."

    tomas "Et ce texte doit survivre à une lecture hostile."

    nyra "Exact."

    pause 0.3

    elen "On fait quoi des termes vagues ?"

    tomas "On les bannit."

    iris "Tous ?"

    tomas "Tous ceux qui peuvent ouvrir deux interprétations incompatibles."

    nyra "Et on définit les autres."

    mara "Définir dans le Commandement lui-même ?"

    tomas "Si possible, oui."

    noam "Et si c’est trop long ?"

    nyra "Alors on simplifie la portée."
    nyra "Pas la précision."

    pause 0.4

    "Un silence serré tombe sur la table."

    elen "On dirait un cours."

    mara "Un cours qui évite de se faire piéger."

    iris "Je prends."

    pause 0.3

    noam "On peut tester une phrase ?"

    tomas "Vas-y."

    noam "“Autoriser des échanges inter-districts encadrés”."

    mara "“Encadrés” par quoi ?"

    iris "Voilà."

    nyra "Mot vague."

    tomas "À remplacer par une condition opérationnelle."

    pause 0.3

    elen "D’accord."
    elen "“Autoriser les échanges inter-districts validés par protocole commun.”"

    mara "“Protocole commun” défini où ?"

    elen "…"

    iris "Encore flou."

    nyra "Mais c’est mieux."

    pause 0.3

    tomas "On peut faire plus direct."
    tomas "“Autoriser les échanges inter-districts listés et tracés par registre partagé.”"

    mara "Là c’est concret."

    iris "Oui, mais ça suppose l’outil."

    tomas "L’outil existe déjà sous une forme minimale."

    mara "Pas partout pareil."

    nyra "Alors il faut ajouter une clause de déploiement progressif."

    pause 0.4

    noam "Vous voyez ?"
    noam "Rien qu’une phrase et on ouvre dix portes."

    elen "C’est pour ça qu’il ne faut pas improviser au moment du vote."

    pause 0.3

    "Deux personnes derrière nous se rapprochent."
    "Elles écoutent sans intervenir."

    pause 0.3

    mara "Autre sujet."
    mara "La perception."
    mara "Si on parle trop technique, certains décrochent."

    iris "Si on simplifie trop, on ment."

    nyra "Donc il faut deux niveaux de discours."

    tomas "Version publique lisible."
    tomas "Version verrouillée précise."

    elen "Et il faut que les deux disent la même chose."

    noam "Sinon on perd la confiance."

    pause 0.3

    mara "Encore un point :"
    mara "Qui prend la parole au Conclave ?"

    iris "Pas une seule personne."

    elen "Oui, sinon ça ressemble à une prise de contrôle."

    nyra "Trois voix minimum."
    nyra "Profils différents."

    tomas "Une pour le cadre."
    tomas "Une pour le terrain."
    tomas "Une pour les garanties."

    noam "Et moi ?"

    mara "Toi, tu peux faire le lien."

    pause 0.4

    noam "Le lien entre quoi ?"

    mara "Entre l’idée et la personne en face."

    iris "Tu reformules bien."

    noam "Je ne suis pas sûr que ça suffise."

    nyra "Ça ne suffira pas."
    nyra "Mais ce sera utile."

    pause 0.3

    elen "On devrait aussi identifier qui risque de voter contre."

    tomas "Sans les désigner publiquement."

    mara "Oui."

    iris "Et surtout comprendre pourquoi."

    noam "Pas pour les coincer."

    nyra "Pour les entendre avant la salle."

    pause 0.4

    "Une serveuse automatique passe entre les rangées."
    "Le moteur ronronne doucement."
    "Personne ne la regarde vraiment."

    pause 0.3

    mara "Je vais être franche."
    mara "Je ne crois pas qu’on aura l’unanimité juste avec de bons arguments."

    elen "Tu crois qu’il faudra quoi ?"

    mara "De la confiance."
    mara "Et la confiance, ça ne se décrète pas en séance."

    iris "Ça se construit avant."

    nyra "Ou ça échoue avant."

    pause 0.3

    tomas "D’où la formulation."
    tomas "Un texte clair peut au moins réduire la peur."

    noam "Réduire."
    noam "Pas effacer."

    tomas "Oui."

    pause 0.3

    elen "Je peux poser une question brute ?"

    mara "Vas-y."

    elen "Si on voit qu’on n’aura pas l’unanimité, on fait quoi ?"

    "…"

    iris "…"

    nyra "On adapte."

    tomas "On retire ce qui bloque si ça ne trahit pas le fond."

    mara "Et si ça le trahit ?"

    nyra "Alors on assume l’échec."

    pause 0.5

    "Le mot reste suspendu."
    "Échec."
    "Personne ne le répète."

    pause 0.3

    noam "Je préfère qu’on n’y arrive pas que de voter un piège."

    mara "Pareil."

    iris "Pareil."

    elen "Pareil."

    tomas "Pareil."

    nyra "Alors on est alignés sur une base minimale."

    pause 0.3

    "Nyra prend une serviette et écrit trois mots."
    "Elle la pose au centre de la table."

    nyra "Clarté."
    nyra "Limites."
    nyra "Traçabilité."

    tomas "Ça me va."

    mara "Ça me va aussi."

    iris "Oui."

    elen "D’accord."

    noam "On tient quelque chose."

    pause 0.4

    "Derrière nous, les deux observateurs hochent la tête et repartent."

    pause 0.3

    mara "Bon, je dois filer dans le couloir nord après ça."

    iris "Pour quoi ?"

    mara "Vérifier un point d’acheminement."
    mara "Histoire de parler concret quand je ramène l’argument."

    noam "Tu veux un coup de main ?"

    mara "Plus tard peut-être."

    pause 0.3

    tomas "Je vais retravailler une formulation test."

    elen "Tu nous l’envoies ?"

    tomas "Oui, version courte et version complète."

    nyra "Ajoute les définitions en annexe."

    tomas "Déjà prévu."

    pause 0.3

    iris "Je vais parler à deux personnes qui hésitent encore."

    noam "Tu veux que je vienne ?"

    iris "Pas tout de suite."
    iris "D’abord je les écoute."

    pause 0.3

    elen "Noam, toi tu peux faire circuler l’idée simple :"
    elen "On ne vote pas une intention, on vote un texte."

    noam "Oui."

    nyra "Et rappelle que la précision protège tout le monde."

    noam "Compris."

    pause 0.4

    "La table se vide lentement."
    "Pas d’un coup."
    "Par départs successifs."

    hide nyra
    hide tomas
    hide noam

    "Je reste assis quelques secondes."
    "Le plateau devant moi est presque intact."

    pause 0.4

    think "Ce n’était pas un débat pour gagner."
    think "C’était un débat pour éviter l’erreur."

    pause 0.4

    think "Et malgré ça, rien n’est acquis."

    pause 0.4

    $ add_argument("Formulation du commandement")
    show screen argument_unlock("Formulation du commandement")
    pause 5.0

    "Le nouvel argument s’ajoute à la liste."
    "Je le relis mentalement."
    "Formulation du commandement."

    pause 0.4

    think "Oui."
    think "C’est exactement le nerf du problème."

    stop music fadeout 0.8

    "Je repose le plateau."
    "Puis je quitte la cafétéria pour prendre l’air dans les couloirs."

    call START_FREE_TIME("_3_PAUSE_CHAMBRE") from _call_START_FREE_TIME_3_1


label _3_PAUSE_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Je referme la porte derrière moi."
    "La chambre retrouve son calme sec."

    pause 0.4

    think "Je reste debout."
    think "Je n’allume rien d’autre."

    pause 0.4

    think "Convaincre quelqu’un, ce n’est pas prouver qu’on a raison."

    pause 0.5

    think "C’est comprendre ce qui lui fait peur."
    think "Ce qu’il veut protéger."
    think "Ce qu’il refuse de perdre."

    pause 0.4

    think "Je l’oublie trop vite."
    think "Surtout quand je suis stressé."

    pause 0.4

    "Je m’assois sur le bord du lit."
    "Mes mains restent ouvertes sur mes genoux."

    pause 0.4

    think "Au Conclave, on parle de principes."
    think "Mais on vote avec nos nerfs."

    pause 0.4

    think "On vote avec nos histoires."
    think "Avec nos dettes."
    think "Avec nos morts."

    pause 0.4

    think "Je ne peux pas l’ignorer."

    pause 0.4

    think "Est-ce que je vote pour le système ?"
    think "Pour une architecture plus stable ?"
    think "Pour une version moins brutale des règles ?"

    pause 0.4

    think "Ou est-ce que je vote pour les gens ?"
    think "Pour ceux qui sont là, maintenant."
    think "Pour leurs visages, pas pour un schéma."

    pause 0.4

    think "Je n’ai pas la réponse nette."
    think "Et je déteste ça."

    pause 0.4

    "Je me lève, je fais deux pas, je reviens."
    "La pièce est trop petite pour tourner en rond dignement."

    pause 0.4

    think "Si je pousse un argument parfait mais froid, je perds des voix."
    think "Si je pousse une émotion pure, je perds le texte."

    pause 0.4

    think "Il faut les deux."
    think "Pas moitié-moitié."
    think "Les deux, en même temps."

    pause 0.4

    think "Clarté."
    think "Limites."
    think "Traçabilité."

    pause 0.4

    think "Je répète les trois mots comme un ancrage."

    pause 0.4

    "Un bruit dans le couloir."
    "Des pas ralentissent devant ma porte."
    "Puis repartent."

    pause 0.4

    think "Personne n’est tranquille aujourd’hui."

    pause 0.4

    think "Je revois les regards à la cafétéria."
    think "Pas d’enthousiasme."
    think "Pas de panique pure."
    think "Juste une concentration fragile."

    pause 0.4

    think "Une concentration qui peut casser au premier faux mot."

    pause 0.4

    think "Alors je dois choisir mes mots."
    think "Pas pour paraître brillant."
    think "Pour être compréhensible."

    pause 0.4

    think "Compréhensible et honnête."

    pause 0.4

    "Je prends une inspiration lente."
    "Je la retiens."
    "Je relâche."

    pause 0.4

    think "Je ne convaincrai pas tout le monde."
    think "Mais je peux éviter de braquer inutilement."

    pause 0.4

    think "Je peux écouter avant de répondre."

    pause 0.4

    think "Je peux admettre quand je ne sais pas."

    pause 0.4

    think "Je peux dire :"
    think "“Je veux que ça tienne dans la réalité.”"
    think "“Je veux que ça protège, pas que ça piège.”"

    pause 0.4

    think "Ce sera déjà mieux que réciter un slogan."

    pause 0.4

    "Je regarde la porte."
    "Encore quelques heures avant le Conclave."

    pause 0.4

    think "Encore du temps pour parler."
    think "Pour ajuster."
    think "Pour rattraper une maladresse."

    pause 0.4

    think "Pas assez de temps pour réparer une fracture."

    pause 0.4

    think "Donc pas de grand discours."
    think "Des phrases courtes."
    think "Des engagements vérifiables."

    pause 0.4

    think "Et surtout :"
    think "Ne pas confondre gagner un échange"
    think "avec construire un accord."

    pause 0.5

    "Je prends une gorgée d’eau."
    "Cette fois, mes mains tremblent moins."

    pause 0.4

    think "D’accord."
    think "Je repars."

    pause 0.4

    think "Pas besoin d’être parfait."
    think "Besoin d’être clair."

    pause 0.4

    think "Je prends la poignée."
    think "Je souffle une dernière fois."

    pause 0.4

    think "Aller au bout, maintenant."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_2


label _3_TRANSITION_CONCLAVE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Le couloir principal est éclairé plus bas que d’habitude."
    "Assez pour voir les visages."
    "Pas assez pour les détails."

    pause 0.4

    "Des groupes avancent dans la même direction."
    "Conclave."
    "Toujours le même point de convergence."

    pause 0.4

    "Personne ne fait de discours dans le trajet."
    "On garde les dernières phrases pour plus tard."

    pause 0.4

    "Une porte automatique s’ouvre devant nous."
    "Souffle d’air froid."
    "Passage étroit."

    pause 0.4

    "Je franchis le seuil."
    "Les pas résonnent légèrement."
    "Les murs répondent en écho court."

    pause 0.4

    think "Même l’acoustique semble plus sèche."

    pause 0.4

    "Elen marche un peu devant moi."
    "Elle ajuste sa manche sans lever les yeux."

    pause 0.3

    "Iris vérifie sa tablette, puis l’éteint."
    "Geste net."
    "Pas de seconde vérification."

    pause 0.3

    "Mara passe sa main dans ses cheveux et expire fort par le nez."
    "Nyra garde le menton droit."
    "Tomas compte quelque chose sur ses doigts."

    pause 0.4

    "Aucun de nous ne parle vraiment."
    "On échange des signes très courts."
    "Un regard."
    "Un hochement."

    pause 0.4

    think "Le mode solennel s’installe tout seul."

    pause 0.4

    "Deuxième série de portes."
    "Ouverture latérale."
    "Fermeture immédiate derrière le dernier."

    pause 0.4

    "Le sas diffuse une lumière blanche fixe."
    "Pas d’annonce."
    "Pas de musique d’accueil."

    pause 0.4

    think "Kami n’intervient pas encore."
    think "Et ce silence pèse plus lourd qu’un discours."

    pause 0.4

    "Nous avançons en file irrégulière."
    "Personne ne cherche à passer devant."

    pause 0.4

    "Un garçon trébuche légèrement sur une jointure au sol."
    "La personne derrière le rattrape par le coude."
    "Pas un mot."

    pause 0.4

    "On reprend le rythme."
    "Pas après pas."

    pause 0.4

    think "C’est étrange."
    think "On dirait une marche vers quelque chose de déjà écrit."

    pause 0.4

    think "Alors que, justement, on va essayer d’écrire."

    pause 0.4

    "À gauche, une baie vitrée donne sur une section technique."
    "Des câbles."
    "Des voyants verts."
    "Rien qui ressemble à une réponse."

    pause 0.4

    "À droite, des portes fermées sans signalétique."
    "Le genre de portes qu’on ne nous ouvre jamais."

    pause 0.4

    think "Aujourd’hui, seule la salle du Conclave compte."

    pause 0.4

    "Troisième porte automatique."
    "Le capteur nous détecte."
    "Un déclic sec précède l’ouverture."

    pause 0.4

    "L’air devient un peu plus chaud."
    "Plus dense aussi."

    pause 0.4

    "Quelqu’un tousse derrière moi."
    "Un seul son humain un peu trop fort."
    "Puis plus rien."

    pause 0.4

    "Nous ralentissons sans consigne."
    "Le couloir final impose son propre tempo."

    pause 0.4

    think "C’est maintenant qu’on sent la gravité de la salle."

    pause 0.4

    "Je vois les bords métalliques de l’entrée du Conclave."
    "Les lignes lumineuses bleues sont déjà actives."

    pause 0.4

    "Une personne devant moi ferme les yeux deux secondes."
    "Elle rouvre."
    "Avance."

    pause 0.4

    "Pas de voix synthétique."
    "Pas de compte à rebours."
    "Toujours pas Kami."

    pause 0.4

    think "Ce silence est volontaire."
    think "Il nous laisse seuls avec nos choix."

    pause 0.4

    "Le groupe se compacte naturellement à l’entrée."
    "Puis se redistribue."
    "Chacun trouve son passage."

    pause 0.4

    "Je sens mon rythme cardiaque monter."
    "Pas de panique."
    "Juste une alerte continue."

    pause 0.4

    think "Rester net."
    think "Rester utile."
    think "Rester honnête."

    pause 0.4

    "Dernier seuil."
    "Les portes coulissent en silence parfait."

    scene bg_conclave at adaptive_fullscreen with dissolve

    "La salle du Conclave nous attend."
    "Les sièges sont prêts."
    "Les pupitres aussi."

    pause 0.4

    "On prend place sans consigne."
    "Par habitude déjà acquise."

    pause 0.4

    "Le plafond diffuse une lumière régulière."
    "Les écrans restent noirs."

    pause 0.4

    think "Kami n’a pas encore parlé."

    pause 0.4

    think "Et c’est peut-être mieux comme ça."

    return
