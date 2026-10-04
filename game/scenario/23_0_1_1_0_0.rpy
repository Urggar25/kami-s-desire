# =============================================================================
# JOUR 23 — RIEN DANS SA TÊTE
# Route 0_1_1_0_0
#
# Sael s'inquiète réellement des visions de Noam et lui fait passer une batterie
# d'examens. Iris impose sa présence. Tout revient normal.
# =============================================================================

label _23_0_1_1_0_0_REVEIL:
    $ current_day = 23
    $ day_id = 23
    $ current_period = "Matin"

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2

    "Je me réveille avant l'alarme."

    "Pas en sursaut. Pas à cause d'un bruit."

    "Juste les yeux ouverts, comme si mon corps avait décidé qu'il avait assez dormi alors que clairement non."

    "Le bureau est toujours poussé contre la grille d'aération."

    "Je le regarde un moment."

    think "C'est ridicule."

    "Je ne le bouge pas."

    "Je prends ma tablette, regarde l'heure, puis la repose."

    "J'ai mal dormi, mais pas assez mal pour pouvoir accuser la fatigue de tout ce qui s'est passé."

    think "Mara morte."

    "Je ferme les yeux."

    think "Mara vivante."

    "Je les rouvre aussitôt."

    noam fatigue "Super."

    "Je m'habille sans défaire complètement mon sac."

    "Au bout de deux jours, ça commence à devenir un principe stupide."

    "Je garde la moitié de mes affaires prêtes à partir, comme si Kami allait changer d'avis au milieu de la nuit et nous dire de courir au sas."

    "Je passe devant la grille une dernière fois."

    think "Jour vingt-trois."

    "Sept jours."

    "Je sors."

    # Durée : ~1m30
    # Total : ~1m30


label _23_0_1_1_0_0_PETIT_DEJEUNER:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "La cafétéria est déjà bruyante."

    "Pas vraiment joyeuse. Juste vivante."

    "Des couverts. Des chaises. Mara qui parle trop fort quelque part."

    think "Donc une matinée normale."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "reflexion"),
        ("iris", "fatigue"),
        ("noam", "fatigue"),
    ])

    mara taquin "Ah, voilà le revenant."

    noam blase "Bonjour Mara."

    mara sourire "Bonjour Noam. T'as une tête de merde."

    iris fatigue "Elle a raison."

    noam fatigue "Merci, vous êtes adorables."

    mara taquin "Moi je peux être beaucoup plus adorable si tu demandes gentiment."

    iris blase "On mange."

    mara rire "J'ai rien proposé de sale."

    iris "T'allais le faire."

    mara taquin "Oui, mais tu m'as coupée. C'est frustrant."

    "Je m'assois avec mon plateau."

    "Sael ne touche presque pas au sien."

    "Elle me regarde."

    "Pas discrètement."

    noam reflexion "Quoi ?"

    sael reflexion "T'as encore mal dormi."

    noam blase "Vous avez préparé ça ensemble ?"

    iris fatigue "Non, c'est juste très visible."

    mara taquin "On dirait que t'as passé la nuit avec quelqu'un de violent."

    noam "Mara..."

    mara rire "Quoi ? Ça peut arriver."

    sael inquiet "Je parle sérieusement."

    "Mara finit par se taire."

    "Ça suffit à me faire regarder Sael autrement."

    noam reflexion "D'accord. Qu'est-ce qu'il y a ?"

    sael raison "Je veux que tu viennes à l'infirmerie."

    noam surpris "Pourquoi ?"

    sael "Pour te tester."

    noam blase "Dit comme ça, c'est rassurant."

    mara taquin "Moi aussi je peux le tester."

    iris colere "Mara."

    mara sourire "Là, oui, c'était sale."

    sael desaccord "Je parle de sa tête."

    noam reflexion "Ma tête va très bien."

    sael fatigue "Tu sais pas."

    noam "Si."

    sael "Non."

    "Elle pousse son plateau de quelques centimètres."

    sael raison "Tu dis que t'as vu quelqu'un mort. Puis vivant. Tu dis que t'as entendu des choses dans les conduits. T'as eu des trous dans tes souvenirs avant."

    noam inquiet "J'ai pas dit que j'avais des trous de mémoire maintenant."

    sael "J'ai pas dit maintenant."

    iris reflexion "Tu penses à quoi exactement ?"

    sael "Manque d'oxygène. Choc. Traumatisme. Un truc neurologique. Je sais pas."

    mara reflexion "Ou possession."

    noam colere "Non."

    sael colere "Non."

    mara rire "D'accord, d'accord."

    iris reflexion "Tu peux vérifier tout ça ici ?"

    sael raison "Une partie. Pupilles, réflexes, mémoire, perception. Y'a aussi l'IRM."

    noam surpris "Attends."

    iris "Quoi ?"

    noam inquiet "On est passés de 't'as une sale tête' à 'on te met dans une machine'."

    sael neutre "Oui."

    noam "Très progressivement."

    sael "T'as peur de l'IRM ?"

    noam blase "Non."

    iris taquin "Il a peur de l'IRM."

    noam colere "J'ai pas peur de l'IRM."

    mara taquin "T'inquiète, si t'as besoin de tenir une main..."

    noam fatigue "Je vais me lever."

    mara rire "J'allais dire Iris."

    iris surpris "Pardon ?"

    mara "Regarde-la, elle s'est déjà portée volontaire dans sa tête."

    iris colere "Je me porte volontaire pour te jeter ton café dessus."

    sael fatigue "Vous pouvez vous taire deux secondes ?"

    "Ça tombe assez sec pour que même Mara baisse d'un ton."

    sael inquiet "Je veux juste vérifier qu'il a rien."

    noam reflexion "Sael..."

    sael "Parce que si t'as rien..."

    "Elle s'arrête."

    iris reflexion "Si ?"

    sael peur "Alors ça veut dire que ce que t'as vu vient peut-être pas de toi."

    "Personne ne plaisante."

    "Je baisse les yeux sur mon plateau."

    noam inquiet "Tu crois vraiment que je peux halluciner à ce point ?"

    sael fatigue "Je préfère ça à l'autre possibilité."

    "C'est dit simplement."

    "Presque trop."

    "Je comprends alors qu'elle n'essaie pas de prouver que je suis fou."

    "Elle essaie de se rassurer."

    noam fatigue "D'accord."

    sael surpris "D'accord quoi ?"

    noam "On fait les tests."

    iris determine "Je viens."

    sael neutre "Pourquoi ?"

    iris blase "Parce que je te connais."

    sael desaccord "Ça veut dire quoi ?"

    iris "Que la dernière fois que t'as voulu régler un problème mystique, Ryn a fini par maintenir Noam contre un mur."

    noam colere "Merci de rappeler ça."

    sael fatigue "J'ai dit que c'était médical."

    iris "Je viens quand même."

    sael "J'ai pas besoin d'assistante."

    iris agace "Je suis pas ton assistante."

    mara taquin "Elle est la garde du corps du patient."

    noam blase "J'ai rien demandé."

    iris fatigue "Toi, tais-toi. T'as accepté l'IRM."

    noam "J'ai accepté des tests."

    sael raison "L'IRM est un test."

    noam "Je déteste déjà cette journée."

    mara sourire "Moi je l'aime bien."

    "Mara pique un morceau dans mon assiette."

    noam colere "Eh !"

    mara taquin "Tu vas être à jeun pour l'IRM."

    sael desaccord "Non."

    mara rire "Merde."

    iris taquin "Bien essayé."

    "Malgré moi, je souris."

    "Ça dure deux secondes."

    "Puis je repense à la raison pour laquelle on va à l'infirmerie."

    $ hideGroup()

    # Durée : ~4m00
    # Total : ~5m30


label _23_0_1_1_0_0_INFIRMERIE_ENTREE:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "L'infirmerie sent toujours pareil."

    "Propre. Trop propre."

    "Je m'assois sur le bord d'un lit pendant que Sael fouille dans un tiroir."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "blase", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    noam reflexion "Tu sais vraiment utiliser tout ça ?"

    sael desaccord "Oui."

    iris taquin "Réponse très rassurante."

    sael colere "J'ai déjà travaillé ici."

    noam surpris "Quand ?"

    sael reflexion "Quand Anya était là. Et avant."

    iris blase "Ça répond pas vraiment."

    sael fatigue "Vous voulez faire les tests ou discuter de mon CV ?"

    noam "Les tests."

    iris "Son CV."

    sael colere "Iris."

    iris sourire "Je plaisante."

    "Sael sort une petite lampe."

    noam inquiet "Ça commence par quoi ?"

    sael raison "Les yeux."

    noam "Très bien."

    sael "Regarde ici."

    "Elle allume la lampe."

    noam surpris "Putain !"

    iris rire "Oh non."

    sael desaccord "Bouge pas."

    noam colere "Tu pouvais prévenir."

    sael "J'ai dit regarde ici."

    noam "C'est pas prévenir."

    iris taquin "Si, un peu."

    noam "T'es de son côté maintenant ?"

    iris blase "Je suis du côté de la science."

    sael raison "Pupille droite normale."

    "Elle passe à l'autre œil."

    sael "Gauche normale."

    noam taquin "Je suis symétrique. Bonne nouvelle."

    iris "Pour les yeux."

    noam blase "Merci Iris."

    sael raison "Suis mon doigt."

    "Je le suis."

    sael "Sans bouger la tête."

    "Je recommence."

    iris taquin "C'est fascinant."

    noam "Tu peux partir."

    iris "Non."

    noam "Tu t'ennuies."

    iris fatigue "Oui."

    noam "Donc pars."

    iris "Non."

    "Je la regarde."

    iris agace "Quoi ?"

    noam taquin "Rien."

    iris "Arrête."

    noam sourire "J'ai rien dit."

    sael colere "Regarde mon doigt."

    noam fatigue "Oui maman."

    "Silence."

    "Je réalise ma connerie."

    mara_not_here = False

    iris rire "Oh."

    sael surpris "..."

    noam gene "Pardon."

    sael taquin "Refais ça et je prends le sel."

    noam peur "Compris."

    "Iris éclate franchement de rire."

    "Même Sael sourit."

    "Pendant quelques secondes, l'infirmerie ressemble presque à une pièce normale."

    # Durée : ~3m00
    # Total : ~8m30


label _23_0_1_1_0_0_REFLEXES:
    "Sael sort ensuite un marteau à réflexes."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "taquin", 0.50),
        ("noam", "inquiet", 0.76),
    ])

    noam inquiet "Ça, j'aime moins."

    sael "C'est du caoutchouc."

    noam "Ça reste un marteau."

    iris taquin "Tu veux tenir ma main ?"

    noam blase "Toi aussi maintenant ?"

    iris sourire "Je profite."

    sael raison "Relâche la jambe."

    noam "Elle est relâchée."

    sael "Non."

    noam colere "Si."

    sael desaccord "Non."

    iris fatigue "Noam, relâche ta putain de jambe."

    noam "Je suis détendu !"

    "Sael frappe sous mon genou."

    "Ma jambe part d'un coup."

    iris rire "Très détendu."

    noam colere "Ferme-la."

    sael raison "Réflexe normal."

    "Deuxième genou."

    "Même chose."

    sael "Normal."

    noam reflexion "Et si c'était pas normal, ça voudrait dire quoi ?"

    sael "Ça dépend."

    noam "De quoi ?"

    sael "Du réflexe."

    noam blase "Merci."

    iris taquin "Consultation très claire."

    sael colere "Vous voulez que j'explique tout ?"

    iris "Non."

    noam "Un peu."

    sael fatigue "Si je commence vous allez vous plaindre."

    noam "Probable."

    "Elle passe aux mains."

    sael raison "Serre mes doigts."

    noam "Comme ça ?"

    sael "Plus fort."

    noam "Je vais te faire mal."

    sael blase "Je survivrai."

    noam reflexion "Sael..."

    sael desaccord "Plus fort."

    "Je serre."

    sael raison "Bien."

    iris sourire "Waouh. Quelle performance."

    noam blase "Je t'en prie, continue à commenter tout l'examen."

    iris taquin "Avec plaisir."

    "Sael teste ensuite ma coordination."

    "Doigt sur le nez, bras tendus, yeux fermés."

    "Je rate mon nez une fois."

    iris rire "Ah !"

    noam colere "J'ai bougé."

    sael taquin "T'as raté ton propre nez."

    noam "Vous êtes insupportables."

    iris sourire "Mais t'es normal."

    "Je m'arrête."

    "Elle aussi."

    "Le mot reste là une seconde."

    noam inquiet "Pour l'instant."

    iris fatigue "Ouais."

    "Sael reprend sans commenter."

    # Durée : ~3m30
    # Total : ~12m00


label _23_0_1_1_0_0_MEMOIRE:
    "Le test suivant ressemble d'abord à un jeu pour enfant."

    "Sael pose plusieurs objets devant moi."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "reflexion", 0.50),
        ("noam", "neutre", 0.76),
    ])

    sael raison "Regarde-les."

    noam reflexion "Une tasse, un badge, un stylo, une compresse, une clé."

    sael "Je t'ai pas demandé de les nommer."

    noam blase "Je prends de l'avance."

    iris taquin "Toujours premier de la classe."

    noam "Pas du tout."

    sael "Ferme les yeux."

    "Je ferme les yeux."

    "J'entends les objets bouger."

    sael "Ouvre."

    "La clé a disparu."

    noam neutre "La clé."

    sael raison "Bien."

    iris sourire "Il est brillant."

    noam "Tu te moques depuis vingt minutes, tu peux varier."

    iris "Non."

    sael raison "Maintenant, cinq mots."

    noam reflexion "D'accord."

    sael "Fenêtre. Orange. Cheval. Métal. Pluie."

    noam "Fenêtre, orange, cheval, métal, pluie."

    sael "Je te les redemanderai plus tard."

    noam taquin "Je les oublierai exprès."

    sael desaccord "Fais pas ça."

    noam "Je plaisante."

    sael "Moi pas."

    "Elle change d'écran."

    sael reflexion "Quel jour on est ?"

    noam "Jour vingt-trois."

    sael "Date réelle."

    noam hesitation "Euh..."

    iris rire "Ah."

    noam colere "Attends."

    iris taquin "Le grand esprit vacille."

    noam "On est enfermés dans une station avec des jours numérotés depuis trois semaines, forcément que—"

    sael fatigue "Réponds juste."

    noam reflexion "Quatre octobre."

    sael raison "Bien."

    noam surpris "Bien ? J'ai bon ?"

    iris blase "Tu veux une médaille ?"

    noam "Un peu."

    sael "Où est-ce qu'on est ?"

    noam taquin "À l'infirmerie."

    sael colere "Noam."

    noam sourire "Dans le Conclave."

    sael "En orbite."

    noam "Oui."

    sael "Pourquoi t'es ici ?"

    "La question me fait hésiter plus longtemps."

    noam reflexion "Parce que Kami nous a amenés ici pour le Conclave."

    sael "Et pourquoi t'as accepté les tests ?"

    noam fatigue "Parce que tu me lâchais pas."

    iris rire "Bonne réponse."

    sael blase "Parce que tu crois avoir vu Mara morte."

    "Le rire d'Iris s'arrête."

    noam inquiet "Oui."

    sael reflexion "Raconte-moi exactement ce que t'as vu."

    noam "Maintenant ?"

    sael "Oui."

    noam desaccord "C'était pas un test de mémoire générale ?"

    sael "Ça en fait partie."

    "Je regarde Iris."

    "Elle ne plaisante plus."

    noam inquiet "J'étais dans la zone derrière les conduits. J'ai trouvé la salle. Après... j'ai vu un corps."

    sael "De qui ?"

    noam peur "Mara."

    sael "Tu l'as touché ?"

    noam "Non."

    sael "T'as vérifié si elle respirait ?"

    noam "Je crois pas."

    sael reflexion "Tu crois pas ?"

    noam colere "J'étais pas exactement calme."

    iris colere "Sael."

    sael "Je demande."

    noam fatigue "Non. J'ai pas vérifié."

    sael "Tu as vu du sang ?"

    noam peur "Oui."

    sael "Où ?"

    noam "Je sais plus précisément."

    sael "Sur elle ? Au sol ?"

    noam colere "J'ai dit que je sais plus."

    "Sael se tait."

    "Je respire trop vite."

    iris inquiet "Ça va."

    noam agace "Non, ça va pas."

    iris "Je sais."

    "Sa réponse est douce, mais pas sucrée."

    "Juste là."

    sael fatigue "On arrête cette partie."

    noam reflexion "Non."

    sael "T'es énervé."

    noam "Parce que je me souviens."

    "Je regarde les objets sur la tablette."

    noam peur "Je me souviens de son visage."

    pause 0.5

    iris inquiet "Noam..."

    noam faible "Et je me souviens de l'avoir vue après. Vivante. Comme si rien s'était passé."

    sael peur "D'accord."

    "Elle détourne légèrement les yeux."

    noam reflexion "Tu me crois ?"

    sael fatigue "Je crois que tu te souviens de ça."

    noam "C'est pas pareil."

    sael "Non."

    "Au moins elle ne ment pas."

    "Elle regarde sa tablette."

    sael raison "Les cinq mots."

    noam surpris "Quoi ?"

    sael "Les cinq mots."

    noam reflexion "Fenêtre... orange... cheval... métal..."

    "Je bloque."

    iris taquin "Oh."

    noam colere "Attends."

    "Je ferme les yeux."

    noam determine "Pluie."

    sael raison "Cinq sur cinq."

    iris sourire "Félicitations."

    noam fatigue "J'ai envie de rentrer chez moi."

    iris "Ça, le test l'avait pas prévu."

    # Durée : ~5m00
    # Total : ~17m00


label _23_0_1_1_0_0_PERCEPTION:
    "Sael enchaîne avec des tests de perception."

    "Des formes, des couleurs, des sons, des images qui apparaissent une fraction de seconde."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "fatigue", 0.50),
        ("noam", "reflexion", 0.76),
    ])

    sael raison "À gauche ou à droite ?"

    noam "Droite."

    sael "Couleur ?"

    noam "Rouge."

    sael "Forme ?"

    noam "Triangle."

    iris blase "Passionnant."

    sael colere "Tu peux partir."

    iris "Non."

    noam taquin "Elle reste pour me protéger du triangle."

    iris agace "Je commence à regretter."

    sael raison "Son aigu ou grave ?"

    noam "Aigu."

    sael "Deuxième ?"

    noam reflexion "Grave."

    sael "Bien."

    "Elle lance une nouvelle série."

    "Un visage apparaît."

    "Mara."

    "Mon cœur rate un battement."

    noam peur "Attends."

    sael surpris "Quoi ?"

    noam "Remets."

    sael reflexion "L'image ?"

    noam determine "Oui."

    "Elle la remet."

    "C'est juste une photo de Mara prise pour les dossiers du Conclave."

    "Vivante. Souriante."

    iris inquiet "Ça va ?"

    noam fatigue "Oui."

    iris colere "Mens mieux."

    noam "C'est rien."

    sael "On peut arrêter."

    noam determine "Non. Continue."

    "Sael hésite."

    sael reflexion "T'es sûr ?"

    noam "Oui."

    "Elle continue."

    "Kael."

    "Nyra."

    "Ryn."

    "Elias."

    "Mara revient une deuxième fois."

    "Cette fois je ne bronche presque pas."

    "Presque."

    sael raison "Réponse ?"

    noam reflexion "Mara."

    sael "Temps de réponse plus long."

    noam agace "Je sais."

    iris inquiet "C'est forcément anormal ?"

    sael "Non."

    noam "Tu peux dire plus que non ?"

    sael raison "Si une image te rappelle quelque chose de violent, tu ralentis. C'est normal."

    noam reflexion "Donc mon cerveau réagit normalement à un souvenir peut-être faux."

    sael fatigue "Oui."

    noam blase "Parfait."

    iris agace "Arrête de chercher une réponse dans chaque test."

    noam colere "C'est pour ça qu'on est là."

    iris "Non. On est là pour vérifier si t'as un problème évident."

    noam "Et si j'en ai pas ?"

    iris inquiet "Alors on verra après."

    noam "C'est quoi après ?"

    iris colere "J'en sais rien, Noam !"

    "Sa voix claque."

    "Elle regrette immédiatement."

    iris fatigue "J'en sais rien."

    noam fatigue "D'accord."

    "On reste silencieux quelques secondes."

    sael reflexion "On fait l'IRM."

    "Aucune de nous ne plaisante."

    # Durée : ~4m00
    # Total : ~21m00


label _23_0_1_1_0_0_IRM_PREPARATION:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

    "La machine est au fond de la pièce, derrière une cloison."

    "Je l'avais déjà vue sans vraiment la regarder."

    "Maintenant elle me paraît beaucoup trop grande."

    $ showGroup([
        ("sael", "raison", 0.22),
        ("iris", "inquiet", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    sael raison "Enlève tout ce qui est métallique."

    noam reflexion "Badge aussi ?"

    sael "Oui."

    noam "Téléphone."

    sael "Oui."

    noam "Ceinture."

    sael "Oui."

    iris taquin "Continue, ça devient intéressant."

    noam blase "Je te déteste."

    iris sourire "Je sais."

    "Je pose mes affaires dans un bac."

    noam inquiet "Ça dure combien de temps ?"

    sael "Une vingtaine de minutes."

    noam surpris "Tu m'avais dit pas longtemps."

    sael neutre "C'est pas longtemps."

    noam colere "Vingt minutes dans un tube, c'est long."

    iris taquin "Il a vraiment peur."

    noam "J'ai pas peur."

    iris "T'as demandé quatre fois combien de temps ça dure."

    noam "Je me renseigne."

    sael reflexion "T'es claustrophobe ?"

    noam hesitation "Pas spécialement."

    iris blase "Donc oui."

    noam colere "Non."

    sael fatigue "Si tu paniques, tu me le dis."

    noam "Comment ?"

    sael "Y'a un bouton."

    noam "Et si le bouton marche pas ?"

    iris rire "Noam."

    noam "Je pose une question."

    sael raison "Il marche."

    noam "Tu l'as testé ?"

    sael "Oui."

    noam "Quand ?"

    sael colere "Ce matin."

    noam "Pourquoi ?"

    sael "Parce que je savais que t'allais demander."

    "Iris éclate de rire."

    noam blase "Vous êtes horribles."

    iris sourire "Viens."

    "Elle me tend la main."

    "Je la regarde."

    noam surpris "Quoi ?"

    iris gene "Bah... donne."

    noam taquin "Tu te moquais de moi il y a dix secondes."

    iris agace "Je peux me moquer et t'aider en même temps."

    noam "C'est très toi."

    iris "Tu la prends ou pas ?"

    "Je prends sa main."

    "Elle serre une fois."

    "Pas longtemps."

    "Puis elle la retire comme si ça avait duré trop longtemps."

    iris blase "Voilà. T'es officiellement courageux."

    noam sourire "Merci."

    sael taquin "C'est mignon."

    iris colere "Commence pas."

    "Sael lève les mains."

    "Je m'allonge."

    # Durée : ~3m30
    # Total : ~24m30


label _23_0_1_1_0_0_IRM:
    scene black with dissolve
    stop music fadeout 0.8

    "La table glisse."

    "Le plafond disparaît."

    "Il ne reste qu'une paroi blanche très proche de mon visage."

    "Puis le bruit."

    "Un premier claquement métallique."

    pause 0.4

    "Un deuxième."

    "Régulier."

    "Sec."

    "Je ferme les yeux."

    think "C'est la machine."

    "Le bruit recommence."

    think "Juste la machine."

    "Puis le rythme change."

    "Trois coups rapides."

    pause 0.3

    "Un silence."

    pause 0.5

    "Deux coups."

    "Mon ventre se serre."

    think "Non."

    "Ça ressemble trop aux bruits dans les conduits."

    "Je garde les yeux fermés."

    "Je revois le couloir."

    "La salle cachée."

    "Le corps."

    "Je rouvre les yeux."

    "Paroi blanche."

    "Rien d'autre."

    "Le haut-parleur grésille."

    sael neutre "Noam ?"

    noam inquiet "Oui."

    sael "Tu bouges."

    noam "Désolé."

    sael raison "Ça va ?"

    noam hesitation "Oui."

    iris inquiet "Mens pas."

    "Sa voix arrive plus loin, un peu étouffée."

    noam fatigue "Ça va."

    iris "T'as appuyé sur rien ?"

    noam "Non."

    iris "Alors reste tranquille."

    noam taquin "Merci pour le soutien."

    iris blase "De rien."

    "Le bruit reprend."

    "Je compte."

    "Un."

    "Deux."

    "Trois."

    "À vingt-sept, je perds le fil."

    "À un moment, je crois entendre quelque chose entre deux séquences."

    "Une respiration."

    "Je retiens la mienne."

    "Rien."

    "Puis un frottement."

    think "C'est la machine."

    "Je me répète la phrase jusqu'à ce qu'elle ne veuille plus rien dire."

    "Quand la table ressort enfin, la lumière me fait cligner des yeux."

    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.6

    $ showGroup([
        ("sael", "reflexion", 0.22),
        ("iris", "inquiet", 0.50),
        ("noam", "fatigue", 0.76),
    ])

    iris inquiet "Ça va ?"

    noam fatigue "Oui."

    iris agace "T'as encore cette tête."

    noam "Quelle tête ?"

    iris "La tête où tu dis oui mais t'es à deux secondes de dire autre chose."

    noam reflexion "J'ai cru entendre quelqu'un."

    sael surpris "Dans la machine ?"

    noam "Entre deux séquences."

    iris inquiet "Quelqu'un comment ?"

    noam hesitation "Je sais pas. Une respiration. Peut-être un frottement."

    "Sael regarde la machine."

    sael raison "J'étais juste derrière la vitre. J'ai rien entendu."

    "Mon estomac se serre."

    noam peur "D'accord."

    iris colere "Hé. Ça veut rien dire."

    noam "Je sais."

    iris "Non, tu recommences."

    noam agace "Je sais, Iris."

    "Elle se tait."

    "Sael récupère les images."

    sael reflexion "Attendez."

    "Elle agrandit plusieurs coupes."

    "Change d'écran."

    "Revient en arrière."

    "Plus elle regarde, moins je respire."

    noam inquiet "Sael."

    sael "Deux secondes."

    noam "Ça fait déjà deux secondes."

    iris colere "Laisse-la regarder."

    noam "Vous pouvez arrêter de parler comme si j'étais pas là ?"

    "Sael finit par poser la tablette."

    sael raison "C'est normal."

    noam surpris "Quoi ?"

    sael "Tout."

    noam "Tout quoi ?"

    sael raison "Structure normale. Pas de lésion visible. Pas d'hémorragie. Pas de signe d'hypoxie. Rien qui ressemble à un traumatisme récent."

    iris reflexion "Et pour les hallucinations ?"

    sael fatigue "Une IRM prouve pas qu'une personne hallucine ou pas."

    iris "Mais y'a rien qui les expliquerait physiquement."

    sael "Rien d'évident."

    noam reflexion "Donc mon cerveau est normal."

    sael "Oui."

    noam "Mémoire normale."

    sael "Oui."

    noam "Réflexes normaux."

    sael "Oui."

    noam "Perception normale."

    sael hesitation "Sur les tests qu'on a faits, oui."

    "Je ris."

    "Une fois."

    "Sans que ce soit drôle."

    noam blase "Génial."

    iris inquiet "Noam..."

    noam "Non, c'est bien. C'est ce qu'on voulait."

    sael peur "Moi non."

    "Je la regarde."

    sael fatigue "Enfin... si. Je voulais que t'aies rien."

    sael inquiet "Mais je voulais aussi trouver pourquoi t'as vu ça."

    "Elle a l'air presque coupable."

    sael "Là j'ai rien."

    noam peur "Donc si c'était pas dans ma tête..."

    sael colere "J'ai pas dit ça."

    noam "Mais tu le penses."

    sael fatigue "Je pense que je peux plus te dire 'c'est sûrement ton cerveau' et passer à autre chose."

    pause 0.6

    iris inquiet "Ça suffit pour aujourd'hui."

    noam reflexion "Iris..."

    iris determine "Non. Là, ça suffit."

    "Elle récupère mon téléphone dans le bac et me le tend."

    iris fatigue "Tu remets tes affaires. Tu manges. Et pendant au moins une heure tu cherches pas à résoudre le mystère de ta propre tête."

    noam taquin "Une heure ?"

    iris blase "Je suis réaliste."

    "Je prends le téléphone."

    noam sourire "D'accord."

    $ hideGroup()

    # Durée : ~6m00
    # Total : ~30m30


label _23_0_1_1_0_0_APRES_IRM:
    $ current_period = "Après-midi"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "On retourne à la cafétéria."

    "Je n'avais pas faim avant les examens."

    "Maintenant j'ai faim comme si j'avais couru."

    $ showGroup([
        ("mara", "taquin"),
        ("iris", "fatigue"),
        ("sael", "fatigue"),
        ("noam", "fatigue"),
    ])

    mara taquin "Alors ?"

    noam blase "Alors quoi ?"

    mara "Ton cerveau. Toujours là ?"

    noam "Apparemment."

    mara sourire "Dommage, j'espérais récupérer de la place."

    iris agace "Tu peux lui foutre la paix cinq minutes ?"

    mara taquin "Je lui fous la paix. Je demande si son IRM a révélé qu'il pensait beaucoup à moi."

    noam fatigue "Oui. Une énorme tumeur en forme de Mara."

    "Mara reste figée une seconde."

    mara rire "Oh putain."

    iris rire "Bien."

    sael sourire "Pas mal."

    noam taquin "Merci."

    mara taquin "Fais attention, tu deviens séduisant quand t'es méchant."

    iris blase "Et voilà."

    noam "J'aurais dû me taire."

    mara "Trop tard."

    "Elle me vole une frite."

    noam colere "Encore ?"

    mara sourire "Le patient doit partager."

    sael desaccord "C'est pas une règle."

    mara "Ça devrait."

    "Je la regarde mâcher."

    "Le même visage."

    "La même façon de sourire."

    "La même voix."

    "Et d'un coup, je revois le corps."

    "Ma fourchette s'arrête."

    mara reflexion "Quoi ?"

    noam inquiet "Rien."

    mara "Tu me regardes bizarrement."

    noam "Je suis fatigué."

    mara taquin "Tu peux me regarder bizarrement, je juge pas."

    iris inquiet "Noam ?"

    noam fatigue "Ça va."

    "Cette fois Iris ne me contredit pas."

    "Sael, elle, a vu."

    "Son regard passe de moi à Mara."

    "Puis revient."

    mara sourire "Bon, si tout va bien..."

    "Elle reprend une frite."

    noam colere "Arrête de bouffer dans mon assiette."

    mara rire "Ah ! Voilà, il va mieux."

    "Je souris malgré moi."

    "Mais quelque chose a changé."

    "Avant, quand Mara était devant moi, son simple fait d'être là suffisait presque à détruire le souvenir."

    "Maintenant, l'IRM est passée."

    "Mon cerveau est normal."

    "Et elle est toujours là."

    $ hideGroup()

    # Durée : ~4m00
    # Total : ~34m30


label _23_0_1_1_0_0_SAEL_SEULE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Un peu plus tard, Sael me rattrape dans le couloir."

    $ showGroup([
        ("sael", "fatigue", 0.40),
        ("noam", "reflexion", 0.62),
    ])

    sael fatigue "Noam."

    noam "Hm ?"

    sael reflexion "Attends."

    "Je m'arrête."

    noam inquiet "Tu as trouvé quelque chose après coup ?"

    sael "Non."

    noam blase "Tu pourrais commencer autrement."

    sael fatigue "Désolée."

    "Le mot me surprend plus que le reste."

    noam reflexion "Pourquoi ?"

    sael "Pour ce matin."

    noam "Les tests ?"

    sael "Pour avoir voulu que ce soit dans ta tête."

    "Elle regarde le sol."

    sael inquiet "C'était plus simple."

    noam fatigue "Pour moi aussi."

    sael "Je pensais que si je trouvais quelque chose, même petit... manque de sommeil, choc, n'importe quoi..."

    noam "Tu pouvais dire que j'avais halluciné."

    sael raison "Oui."

    noam reflexion "Et maintenant ?"

    sael peur "Maintenant je sais pas."

    "Elle dit ça très vite."

    "Comme si elle voulait passer à autre chose avant que le mot ait le temps de rester."

    sael fatigue "Bref."

    noam "Sael."

    sael colere "Quoi ?"

    noam sourire "Merci d'avoir vérifié."

    "Elle fronce les sourcils."

    sael neutre "C'était normal."

    noam "Je sais."

    sael "Et dors."

    noam taquin "Oui maman."

    sael colere "Je vais chercher le sel."

    noam rire "D'accord, d'accord."

    "Elle repart."

    "Je la regarde s'éloigner."

    "Ça devrait me faire du bien."

    "Étrangement, ça m'en fait un peu."

    $ hideGroup()

    # Durée : ~2m30
    # Total : ~37m00


label _23_0_1_1_0_0_IRIS:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8

    "En fin d'après-midi, Iris passe dans ma chambre."

    "Elle entre, regarde le bureau sous la grille et lève les yeux au ciel."

    $ showGroup([
        ("iris", "blase", 0.40),
        ("noam", "fatigue", 0.62),
    ])

    iris blase "Toujours ça."

    noam reflexion "Ça me rassure."

    iris "Un bureau."

    noam "Oui."

    iris taquin "Ton grand système de sécurité."

    noam "Tu veux le déplacer ?"

    iris determine "Non."

    "Elle s'assoit au bord du lit."

    noam reflexion "Tu venais pour quoi ?"

    iris fatigue "Voir si t'étais en train de devenir complètement taré."

    noam "Verdict ?"

    iris "Mitigé."

    noam sourire "Merci."

    "Elle regarde la grille."

    iris reflexion "Tu veux en parler ?"

    noam surpris "Depuis quand tu demandes ça ?"

    iris colere "Bon, laisse tomber."

    noam rire "Non, attends."

    "Elle soupire."

    iris fatigue "Je déteste faire ça."

    noam taquin "Être gentille ?"

    iris "Oui."

    noam "Je vois."

    iris colere "Tu veux vraiment que je parte ?"

    noam sourire "Non."

    "Elle reste."

    "Un vrai silence cette fois."

    "Pas gênant."

    "Juste fatigué."

    noam reflexion "J'espérais qu'elle trouve quelque chose."

    iris inquiet "Sael ?"

    noam "Oui."

    iris "Moi aussi."

    noam surpris "Sérieux ?"

    iris fatigue "Pas une tumeur, hein."

    noam taquin "Merci de préciser."

    iris "Un truc. N'importe quoi qui explique."

    noam reflexion "Même une hallucination."

    iris "Ouais."

    noam "Tu me croyais pas."

    iris colere "C'est pas ça."

    noam "Un peu."

    iris fatigue "Un peu."

    "Au moins elle l'admet."

    iris reflexion "Je croyais que t'avais vu quelque chose, mais... je sais pas. Pas forcément ce que tu pensais avoir vu."

    noam "Et maintenant ?"

    iris inquiet "Maintenant je sais encore moins."

    noam blase "Très utile."

    iris agace "Tu veux quoi ? Que je te dise que oui, Mara est morte et qu'une autre Mara se balade dans la cafétéria ?"

    noam peur "Non."

    iris "Parce que moi j'ai pas envie de dire ça."

    noam "Moi non plus."

    "Elle joue avec la fermeture éclair de sa manche."

    iris fatigue "Alors pour ce soir, ton cerveau va bien."

    noam reflexion "C'est tout ?"

    iris determine "C'est tout."

    noam "Et demain ?"

    iris blase "Demain peut aller se faire foutre."

    "Je ris."

    "Elle aussi, un peu."

    iris sourire "Tu vois. Traitement réussi."

    noam taquin "Docteur Iris."

    iris colere "N'abuse pas."

    "Elle se lève."

    iris fatigue "Je vais manger. Tu viens ?"

    noam "Dans cinq minutes."

    iris "Cinq vraies minutes ou cinq minutes de mec qui va fixer son mur pendant une heure ?"

    noam sourire "Vraies."

    iris "Bien."

    "Elle ouvre la porte."

    iris inquiet "Et Noam ?"

    noam "Oui ?"

    iris fatigue "Si t'entends un truc dans les conduits..."

    "Elle hésite."

    iris determine "Tu viens me chercher. Tu y vas pas seul."

    noam reflexion "D'accord."

    iris colere "Je déconne pas."

    noam "J'ai dit d'accord."

    iris "Bien."

    "Elle sort."

    $ hideGroup()

    # Durée : ~4m30
    # Total : ~41m30


label _23_0_1_1_0_0_SOIREE:
    $ current_period = "Soir"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "Le dîner est presque normal."

    "Presque."

    $ showGroup([
        ("mara", "taquin"),
        ("elias", "fatigue"),
        ("tomas", "reflexion"),
        ("iris", "fatigue"),
        ("noam", "fatigue"),
    ])

    tomas reflexion "Donc les examens sont normaux ?"

    noam blase "La nouvelle a déjà fait le tour ?"

    iris "Mara."

    mara sourire "J'ai demandé."

    noam colere "À qui ?"

    mara taquin "Sael."

    noam "Pourquoi ?"

    mara "Parce que je m'inquiète pour toi."

    iris blase "Elle s'inquiète de savoir si elle peut continuer à te faire chier."

    mara rire "Aussi."

    elias fatigue "Au moins t'as rien."

    noam reflexion "Ouais."

    tomas hesitation "Enfin... rien de visible."

    "Tout le monde le regarde."

    tomas stress "Quoi ? C'est vrai. Une IRM normale exclut pas tout. Les hallucinations peuvent venir de plein de—"

    iris colere "Tomas."

    tomas fatigue "Je sais. Je ferme ma gueule."

    mara taquin "Tu tiens combien de temps ?"

    tomas reflexion "Pas longtemps."

    "Ça fait rire Elias."

    "Je regarde Elias rire."

    "Je ne sais pas pourquoi ça me dérange."

    "Peut-être parce que depuis ce matin, tout me dérange."

    elias reflexion "Quoi ?"

    noam surpris "Rien."

    elias "Tu me fixais."

    noam fatigue "Je suis crevé."

    elias "Ouais, ça se voit."

    mara taquin "Il fixe tout le monde aujourd'hui. Moi ça me plaît bien."

    iris agace "Tu vas finir par le faire fuir."

    mara sourire "Il revient toujours."

    "Je regarde Mara."

    "Elle me fait un clin d'œil."

    "J'ai envie de rire."

    "Et en même temps, quelque chose me retourne l'estomac."

    noam fatigue "Je vais rentrer."

    iris inquiet "Déjà ?"

    noam "Ouais. Je tiens plus."

    mara taquin "Bonne nuit, cerveau normal."

    noam blase "Bonne nuit, Mara."

    "Le nom sort bizarrement."

    "Elle ne semble pas le remarquer."

    $ hideGroup()

    # Durée : ~3m30
    # Total : ~45m00


label _23_0_1_1_0_0_FIN_JOURNEE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je ferme la porte."

    "Je pousse le bureau contre la grille."

    "Encore."

    "Puis je m'assois sur le lit."

    "Ma tablette est là, avec le compte rendu des examens."

    "Je l'ouvre."

    "Je relis les mêmes lignes."

    "Réflexes : normaux."

    "Mémoire : normale."

    "Perception : normale."

    "Imagerie : aucune anomalie visible."

    "Je descends encore."

    "Rien."

    think "Rien dans ma tête."

    "Ça devrait être une bonne nouvelle."

    "Je reste pourtant assis, la tablette entre les mains, avec une boule dans le ventre."

    "Si Sael avait trouvé quelque chose, j'aurais eu une explication."

    "Mauvaise, peut-être."

    "Mais une explication."

    "Une hallucination."

    "Un choc."

    "Un cerveau qui fabrique quelque chose parce qu'il ne tient plus."

    "Je regarde la grille."

    "Puis la porte."

    "Puis l'écran."

    think "Mais si j'ai rien..."

    "Je revois Mara."

    "Pas celle du dîner."

    "L'autre."

    "Immobile."

    "Le sang."

    "Cette sensation glacée quand j'ai compris que le visage était le sien."

    "Je secoue la tête."

    noam peur "Non."

    "Le mot sort tout seul."

    "Je me lève, fais deux pas, reviens."

    "Ça ne change rien."

    think "Si j'ai rien..."

    "Je m'arrête."

    "Cette fois je ne termine pas la phrase dans ma tête."

    "Parce que je sais déjà où elle va."

    "Je prends mon téléphone."

    "Le contact d'Iris est juste là."

    "Mon pouce reste au-dessus."

    "Je pourrais l'appeler."

    "Lui dire que je dors pas."

    "Lui demander de venir."

    "Je repose le téléphone."

    think "Elle dort peut-être."

    "Mensonge nul."

    "Je regarde de nouveau le compte rendu."

    "Tout est normal."

    "Tout."

    "Alors une pensée finit par passer quand même."

    "Claire."

    "Simple."

    "Beaucoup plus effrayante que toutes les autres."

    think "Si ce que j'ai vu n'était pas une hallucination..."

    pause 0.8

    think "Alors Mara était vraiment morte."

    "Je reste immobile."

    "Au même moment, quelque chose tombe dans le couloir."

    "Un bruit banal."

    "Peut-être une porte."

    "Peut-être quelqu'un qui a fait tomber un objet."

    "Je me lève quand même."

    "Je m'approche de la porte."

    "Je n'ouvre pas."

    pause 0.6

    "Des pas passent devant ma chambre."

    "Lents."

    "Puis une voix, plus loin."

    mara rire "Mais attends-moi !"

    "Mon sang se glace."

    "Sa voix s'éloigne."

    "Vivante."

    "Normale."

    "Je reste face à la porte pendant plusieurs secondes."

    "Puis je retourne au lit sans vérifier."

    "Cette nuit, je laisse la lumière allumée."

    stop music fadeout 1.2

    call end_day("24", sleeping=True) from _call_j23_stay_end_day_24
    jump _24_0_1_1_0_0_REVEIL

    # Durée : ~4m30
    # Total : ~49m30
