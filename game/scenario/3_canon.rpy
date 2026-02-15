label _3_CANON:

    $ day_id = 3

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.5

    think "…"

    pause 0.3

    think "Je suis réveillé."
    think "Je crois."

    pause 0.4

    "Je ne bouge pas."
    "Mon dos est raide."
    "Mes épaules me lancent."

    pause 0.4

    think "J’ai dormi ?"
    think "Ou j’ai juste fermé les yeux en attendant le matin ?"

    pause 0.5

    think "Aujourd’hui."

    pause 0.4

    think "Le vote."

    pause 0.6

    think "Un seul non."
    think "Et tout s’arrête."

    pause 0.6

    think "C’est ridicule que ce soit aussi fragile."

    pause 0.5

    scene bg_cg012 at adaptive_fullscreen with fade

    "Je fixe le plafond."
    "Blanc."
    "Lisse."
    $ blink()
    "Propre."

    pause 0.4

    think "Trop propre."
    $ blink()

    pause 0.5

    "Un bruit de pas dans le couloir."
    "Ça traîne."
    "Ça hésite."

    pause 0.4

    think "Personne ne semble courir."
    think "Personne ne parle fort."

    pause 0.6

    play sound sfx_announce

    pause 0.8

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Booooonjour mes petits représentants ♥"

    pause 0.4

    kami "Jour trois !"
    kami "Déjà fatigués ?"

    pause 0.4

    kami "Petit rappel doux et adorable :"
    kami "Aujourd’hui, c’est le jour de vote."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Unanimité absolue."
    kami "Un seul petit non, et… pfiou."

    pause 0.4

    kami "On efface tout."
    kami "On recommence, et tant pis pour la proposition."

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'un d'entre vous se sera creusé les méninges pour rien !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Alors souriez bien."
    kami "Et méfiez-vous un tout petit peu les uns des autres."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ça met du piment~"
    kami "Et j'adore ça !"

    pause 0.4

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à 14h ♥"

    pause 0.3

    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "…"

    pause 0.4

    think "Elle adore ça."
    think "Appuyer là où ça fait mal."

    pause 0.6

    think "Un seul non."

    pause 0.6

    think "Qui pourrait voter contre ?"

    pause 0.5

    think "Personne n’a intérêt à voter contre."
    think "Alors pourquoi j’ai cette drôle de sensation ?"

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with fade
    "Je me redresse. J'allume la lumière."
    "Mes vertèbres craquent."

    pause 0.4

    think "Super."

    pause 0.4

    "Je passe mes mains sur mon visage."
    "Peau froide."
    "Mâchoire serrée."

    pause 0.5

    think "Respirer."
    think "Une étape à la fois."

    pause 0.5

    pause 0.4

    "Je me lève."
    "Le sol métallique est froid sous mes pieds."

    pause 0.5

    think "Ça réveille."

    pause 0.4

    "Je bois un peu d’eau."
    "Deux gorgées."
    "Je n'ai pas très faim, j'ai la gorge nouée."

    pause 0.5

    think "Mais il faut quand même que j'aille à la cafétéria."

    pause 0.5

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    "Le couloir est étrangement calme."

    pause 0.5

    think "Même la ventilation semble retenir son souffle."

    pause 0.4

    "Deux silhouettes marchent devant moi."
    "Elles ralentissent en m’entendant."
    "Puis reprennent."

    pause 0.5

    think "On se surveille sans le dire."

    pause 0.4

    "Je croise Kael au détour du couloir."

    $ showP("noam", "neutre", 0.20)
    $ showP("kael", "fatigue", 0.65)

    kael fatigue "Salut."

    "Sa voix est plus basse que d’habitude."

    noam "Tu vas à la cafétéria ?"

    kael reflechit "Oui."
    kael doute "Enfin… oui."

    "Il ne bouge pas."
    "Il reste là une seconde de trop."

    kael inquiet "Tu es sûr que c’est une bonne idée ?"

    noam "Le commerce ?"

    kael reflechit "Oui."
    kael reflechit "On dit tous que ça ne changera pas grand-chose."
    kael inquiet "Mais si ça dérape ?"

    "Il évite toujours mon regard."

    noam "Tu penses que ça peut vraiment déraper ?"

    kael culpabilite "Je ne sais pas."
    kael fatigue "Je préfère quand les choses sont stables."
    kael reflechit "On vient à peine d’arriver."
    kael inquiet "On ne sait même pas encore comment on fonctionne ensemble."
    kael reflechit "Et on commence déjà à modifier les règles."

    "Il ne dit pas non."
    "Il ne dit pas oui non plus."

    noam "Tu veux voter contre ?"

    kael surpris "Non."
    kael doute "Enfin… je ne crois pas."
    kael reflechit "Je suis pour."
    kael sourire "En théorie."

    "En théorie."

    kael reflechit "Je n’aime pas avancer sans savoir où on met les pieds."
    kael inquiet "Changer quelque chose, c’est accepter de ne plus revenir en arrière."

    "La ventilation souffle au-dessus de nous."
    "Le bruit semble plus fort que d’habitude."

    kael inquiet "Tu n’as pas peur ?"

    noam "Si."
    noam "Mais ne rien changer, c’est aussi un choix."

    "Il baisse légèrement les yeux."

    kael fatigue "Je déteste ça."
    kael reflechit "Décider."
    kael culpabilite "Et ne pas savoir si on va le regretter."

    "Il pourrait basculer."

    kael calme "On verra à 14h."
    kael sourire "Bonne chance."

    "Il passe à côté de moi."
    "Son épaule frôle la mienne."

    "Il n’a pas tranché."
    "Et ça suffit à me serrer l’estomac."


    hide noam
    hide kael

    "Je continue."

    pause 0.5

    "Julian est près du distributeur."
    "Il tapote la machine comme si elle lui devait quelque chose."

    $ showP("noam", "neutre", 0.30)
    $ showP("julian", "joie", 0.75)

    julian joie "Hey."
    julian taquin "Alors ? Prêt à secouer un peu ce système ?"

    "Un large sourire illumine son visage."

    noam "On va essayer."

    julian rire "Essayer ?"
    julian joie "Non, non."
    julian "On va le faire."

    "Il attrape sa tasse."
    "Le café déborde un peu."
    "Il ne s’en rend même pas compte."

    julian reflexion "Tu te rends compte ?"
    julian joie "Si ça passe, on ouvre la première brèche depuis la prise de pouvoir de Kami."

    julian taquin "Du commerce. Des échanges."
    julian joie "Du mouvement."

    "Ses yeux brillent."
    "Il aime l’idée."

    noam "Et si ça ne passe pas ?"

    julian hesitation "Ça passera."
    julian sourire "Il faut que ça passe."

    "Il appuie un peu trop fort sur les mots."

    julian reflexion "On ne peut pas rester figés."
    julian "On n’est pas venus ici pour maintenir le statu quo."
    julian joie "On est là pour changer les choses."
    julian idee "Les gens veulent du changement."

    "Il redresse les épaules."
    "Il se voit déjà dans l’après."

    noam "Tu es sûr que tout le monde suivra ?"

    julian hesitation "…"

    "Une micro-seconde."
    "Presque rien."

    julian sourire "Ils suivront."
    julian taquin "Ils aiment juste faire semblant d’hésiter."

    "Il me regarde droit dans les yeux."

    julian reflexion "Et puis franchement."
    julian joie "C’est le commerce."
    julian "Personne ne va voter contre ça."

    "Il y croit."
    "Ou il veut y croire."

    julian sourire "Imagine un peu."
    julian joie "Des districts qui échangent vraiment."
    julian "Des ressources qui circulent."
    julian "Des idées qui bougent."
    julian idee "Comme avant ! Tu te rends compte !"
    julian taquin "Ça te plaît pas ?"

    "Il parle plus vite."
    "Comme s’il avait déjà validé le résultat."

    noam "Si. Evidemment que dis comme ça, sur le papier, ça me plaît."

    "Mais son enthousiasme me met mal à l’aise."

    julian reflexion "On a besoin d’un élan."
    julian joie "On peut changer les choses. A nous de le faire."

    "Il boit une gorgée."
    "Grimace."
    "Le café est mauvais."

    julian sourire "À 14h."
    julian joie "On ouvre le bal et on change ce monde."

    $ add_argument("Le monde d'avant")
    show screen argument_unlock("Le monde d'avant")

    "Il pivote vers la cafétéria."

    "Il marche vite."
    "Trop vite."

    "Il veut que ça passe."
    "Pas seulement pour le monde."

    "Pour lui aussi."

    hide noam
    hide julian

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    pause 0.5

    "Le bruit des conversations est bas."
    "Trop bas."

    pause 0.6

    think "On fait semblant d’être normaux."

    pause 0.5

    "Ryn parle à voix basse avec Elen."
    "Mara regarde un écran éteint sans vraiment le voir."
    "Iris tient sa tasse sans boire."

    pause 0.6

    think "Tout le monde calcule."

    pause 0.5

    think "Si quelqu’un vote contre."
    think "Qui serait-ce ?"

    pause 0.6

    think "Mara ?"
    think "Non."

    pause 0.4

    think "Sael ?"
    think "Elle serait frontale."

    pause 0.5

    think "Ou peut-être que je me raconte des histoires."

    pause 0.6

    think "C’est ça le pire."
    think "Le doute."

    pause 0.6

    "Je prends un café."
    "Il est amer."
    "Plus que d’habitude."

    pause 0.5

    think "Un seul non."

    pause 0.6

    think "Et on aura juste prouvé qu’on n’est pas capables de s’entendre."

    pause 0.6

    think "Respire."

    pause 0.6

    think "Aujourd’hui, on décide si on est un groupe."
    think "Ou juste douze personnes enfermées ensemble."

    pause 0.8

    jump _3_CAFETERIA_DEBAT

# Durée : 3m45
# Totale : 1h 27m 55s

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
