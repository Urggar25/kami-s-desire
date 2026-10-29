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
    "Elle m’aide à boire, reste encore quelques minutes, puis repart chercher les autres. La porte se referme et je me retrouve de nouveau seul."
    $ hideGroup()
    return

