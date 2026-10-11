# Scènes secondaires de caractérisation — route Doppelganger.
# Chaque label revient à son appelant. Les scènes ne modifient aucun état d'enquête.

label KD_EXTRA_J8_JULIAN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
    "Julian est seul près du comptoir. Il salue une rangée de chaises vides avec une révérence exagérée."
    julian sourire "Chers concitoyens, merci d'être venus aussi nombreux."
    noam taquin "Il y a une chaise qui a l'air émue, au fond."
    julian rire "Enfin un public attentif ! Tu veux prendre sa place ?"
    noam sourire "Tu répètes quoi, exactement ?"
    julian "Mon discours de retour. Quand on aura quitté cette station, il faudra bien que quelqu'un remercie l'humanité pour son soutien."
    noam "Je pense surtout que l'humanité voudra savoir si les votes ont servi à quelque chose."
    julian sourire "On peut répondre à une question sérieuse avec un très beau discours."
    "Il s'incline devant son public imaginaire, puis redresse une chaise dont le dossier est de travers."
    julian hesitation "Tu crois qu'ils retiendront nos noms ?"
    noam reflexion "Pas les douze, probablement. Ça fait du monde."
    julian "Oui. C'est ce que je me disais."
    "Il reprend aussitôt son sourire de scène."
    julian taquin "Bon, je vais devoir accomplir un exploit. Un exploit sans décès, si possible. Ce serait mauvais pour la suite de ma carrière."
    noam taquin "Commence par obtenir les applaudissements de la chaise."
    julian rire "Elle est difficile, mais je sens que je progresse."
    $ hideGroup()
    return

label KD_EXTRA_J13_LYSA:
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "blase", 0.35), ("noam", "fatigue", 0.65)])
    "Lysa regarde la Terre derrière la vitre. Elle se retourne lorsque j'arrive."
    lysa blase "Oh, tiens. T'as perdu Iris ou Mara ?"
    noam reflexion "Pourquoi ?"
    lysa "Pour rien. Je les vois plus souvent avec toi que ton propre reflet."
    noam "Tu pourrais venir me parler, toi aussi."
    lysa taquin "Ah, carrément. Faut prendre rendez-vous, maintenant ?"
    "Elle sourit, mais ne détourne pas les yeux."
    lysa neutre "On est arrivés ensemble ici, tu te rappelles ? À l'époque, on avait au moins le temps de se raconter nos journées."
    noam fatigue "On en a vécu pas mal, depuis."
    lysa blase "J'avais remarqué. Ça explique peut-être pourquoi t'as l'air de dormir debout."
    noam "Je vais bien."
    lysa "Ouais. Ça aussi, tu le dis souvent."
    "Je cherche une réponse. Lysa se tourne de nouveau vers la vitre."
    lysa neutre "Quand t'en auras marre de faire semblant de tout gérer, tu sais où me trouver."
    noam sourire "À râler devant la Terre ?"
    lysa taquin "Exactement. C'est un travail à plein temps."
    $ hideGroup()
    return

label KD_EXTRA_J16_NYRA:
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([("nyra", "reflexion", 0.35), ("noam", "fatigue", 0.65)])
    "En passant par le stockage, je trouve Nyra devant un terminal. Elle compare deux relevés en pointant chaque ligne du doigt."
    noam "Encore un inventaire ?"
    nyra raison "Une vérification. Les rations distribuées ne correspondent pas aux quantités qui disparaissent."
    noam reflexion "On mange plus que prévu ?"
    nyra "Pas tous. Les écarts sont trop réguliers. Quelqu'un prend des portions supplémentaires, en dehors des repas."
    noam "Tu sais qui ?"
    nyra "Non. Mais je sais à peu près combien cette personne prélève chaque jour."
    noam "Et tu comptes faire quoi ?"
    nyra determine "Relever les sorties du stockage, comparer les horaires et trouver qui se sert."
    noam "Tu vas accuser quelqu'un pour quelques biscuits ?"
    nyra colere "Je n'ai accusé personne. Justement, je vérifie avant."
    "Elle fait défiler les dates sur l'écran."
    nyra raison "Quand douze personnes partagent des réserves limitées, quelques portions prises en cachette finissent par manquer à tout le monde."
    noam reflexion "Ça pourrait être plusieurs personnes."
    nyra "C'est possible. Si c'est le cas, les horaires me le diront."
    noam "Tu veux de l'aide ?"
    nyra neutre "Pas encore. Et ne va pas raconter à tout le monde que je cherche un voleur. Je veux des faits, pas une chasse aux coupables."
    "Elle revient à son relevé avant même que j'aie répondu."
    $ hideGroup()
    return

label KD_EXTRA_J19_JULIAN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "rire", 0.35), ("noam", "neutre", 0.65)])
    "Julian s'est installé devant un miroir, une serviette sur les épaules comme une cape."
    julian rire "Ah ! Parfait. Je cherchais justement un spectateur."
    noam "Tu prépares ton discours ?"
    julian sourire "Mieux. Devine qui je suis."
    "Il relève le menton et prend une voix appliquée."
    julian "Techniquement, si nous examinons la formulation de l'alinéa..."
    noam taquin "Tomas. Facile."
    "Julian laisse retomber ses épaules."
    julian "Super. Encore une idée géniale qui va nous exploser au visage."
    noam "Lysa."
    julian joie "Excellent. Dernier essai."
    "Il se redresse, tend la main pour réclamer le silence."
    julian "Attendez, on peut peut-être discuter avant de prendre une décision ?"
    noam sourire "Moi, évidemment."
    julian "Très bien. Maintenant la version récente."
    "Son sourire disparaît. Il frappe sa paume du poing."
    julian colere "Vous allez finir par m'écouter, oui ?! Je suis pas fou !"
    "Je ne ris plus. Julian baisse la main."
    julian hesitation "Quoi ? C'était pas ressemblant ?"
    noam desaccord "Arrête."
    julian inquiet "Noam, je plaisantais. Je fais ça avec tout le monde."
    noam fatigue "Je sais. C'est juste... arrête."
    "Julian retire lentement sa cape ridicule."
    julian neutre "D'accord. Désolé."
    $ hideGroup()
    return

label KD_EXTRA_J20_ELEN:
    scene bg_infirmerie at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "inquiet", 0.35), ("noam", "fatigue", 0.65)])
    "La porte s'ouvre de nouveau. Elen entre avec deux gobelets, puis aperçoit les attaches à mes poignets."
    elen inquiet "Je... Je voulais apporter quelque chose à boire. Je savais pas qu'ils t'avaient laissé comme ça."
    noam fatigue "Pose ça là. Merci."
    "Elle dépose les gobelets sur la table roulante et cherche une place pour s'asseoir."
    elen sourire "On pourrait tous prendre un moment ensemble, demain. Un vrai petit-déjeuner, sans se disputer."
    noam "Tu crois vraiment que ça suffirait ?"
    elen "Je dis pas que ça réglerait tout."
    noam fatigue "Et si rien ne s'arrange ? Si on continue à se détester jusqu'au départ ?"
    elen inquiet "Noam..."
    noam "Je demande juste."
    "Elen regarde la porte, puis mes poignets."
    elen triste "Je sais très bien que ça peut mal finir."
    "Elle se rassied, les doigts serrés autour de son propre gobelet."
    elen triste "Mais si je commence à dire aux autres que ça va mal finir, qui va leur dire qu'on peut encore s'en sortir ?"
    noam fatigue "T'es pas obligée de porter ça toute seule."
    elen sourire "Peut-être. En attendant, je peux au moins t'aider à boire."
    "Elle approche le gobelet de mes mains attachées, puis comprend que je ne peux pas le prendre."
    elen inquiet "Ah. Pardon."
    noam sourire "Tu peux me le tenir. Ça ira."
    $ hideGroup()
    return

label KD_EXTRA_J22_TOMAS:
    scene bg_archive at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "fatigue", 0.65)])
    "Tomas a étalé plusieurs notes autour du terminal d'archives."
    noam reflexion "Tu as trouvé quelque chose ?"
    tomas "Des incohérences. Mais je ne peux pas te dire si elles ont la même origine."
    noam "Alors pourquoi tu continues à les comparer ?"
    tomas "Parce que si elles sont liées, on a peut-être raté quelque chose."
    noam fatigue "Et si tu attends une preuve parfaite pendant que quelqu'un agit ?"
    tomas colere "Et si j'accuse la mauvaise personne ?!"
    "Sa voix résonne dans la pièce. Il baisse les yeux vers ses feuilles."
    tomas inquiet "Pardon. C'est juste que... la dernière chose dont on a besoin, c'est d'un suspect désigné parce que j'ai confondu deux dates."
    noam "Mais on peut pas rester immobiles non plus."
    tomas raison "Je sais. Je vais vérifier encore une fois et je vous donnerai ce que j'ai, même si c'est incomplet."
    noam reflexion "Tu me le promets ?"
    tomas "Oui. Et tu me promets de ne pas présenter une hypothèse comme une certitude ?"
    noam fatigue "Je vais essayer."
    tomas sourire "Bon. C'est à peu près tout ce qu'on peut se promettre, pour le moment."
    $ hideGroup()
    return

label KD_EXTRA_J24_LYSA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "blase", 0.35), ("noam", "neutre", 0.65)])
    "Lysa sort de sa chambre au moment où je passe. Je m'approche, mais elle s'arrête à plusieurs pas de moi."
    noam sourire "Salut. Ça fait longtemps qu'on a pas parlé tranquillement."
    lysa blase "Vu le mois qu'on passe, c'est presque un exploit."
    noam reflexion "Tu m'évites ?"
    lysa "Non. Enfin... un peu."
    "Je fais un pas. Elle recule, presque imperceptiblement."
    noam inquiet "T'as peur de moi ?"
    lysa neutre "Ouais. Un peu."
    noam "Je t'ai rien fait."
    lysa "Je sais. Mais Iris non plus, tu lui avais rien fait avant de lui faire peur avec ce couteau."
    noam desaccord "Je n'allais pas la blesser !"
    lysa colere "Tu vois ? C'est exactement ça. Je te pose une question et j'ai déjà l'impression de devoir choisir mes mots."
    "Je m'arrête. Lysa passe la main sur son visage."
    lysa fatigue "Je sais pas si tu nous caches quelque chose ou si t'es juste à bout. Avant, j'aurais dit que je te connaissais assez pour voir la différence."
    noam fatigue "Et maintenant ?"
    lysa "Maintenant, j'en sais rien."
    noam "Qu'est-ce que je peux faire ?"
    lysa neutre "Déjà, arrête de me demander de faire comme si rien ne s'était passé."
    "Elle passe devant moi sans me frôler."
    $ hideGroup()
    return

label KD_EXTRA_J28_ELEN:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "triste", 0.35), ("noam", "fatigue", 0.65)])
    "Elen est seule à la cafétéria. Sur une table, elle a aligné plusieurs assiettes et distribué les couverts."
    noam inquiet "Tu prépares à manger pour tout le monde ?"
    elen sourire "Je me suis dit qu'on pourrait au moins manger ensemble."
    "Elle compte rapidement les assiettes, puis recommence."
    noam "Elen..."
    elen reflexion "Attends, j'en ai mis trop. C'est idiot."
    "Elle reprend une assiette, hésite, puis en récupère une autre."
    elen triste "Je fais ça tous les jours. J'ai encore préparé leurs places."
    "Son regard s'arrête sur deux chaises vides."
    noam fatigue "Je peux t'aider à ranger."
    elen "Non, c'est bon. Je vais..."
    "Elle reste debout avec une assiette dans les mains."
    elen triste "Je sais plus combien on est, maintenant."
    "Je prends doucement l'assiette qu'elle me tend sans me regarder."
    noam "On va compter ensemble."
    "Elle hoche la tête. Nous rangeons les couverts en silence."
    $ hideGroup()
    return
