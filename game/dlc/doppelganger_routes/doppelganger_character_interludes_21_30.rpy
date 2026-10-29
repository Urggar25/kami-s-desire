# Exclusif au DLC « Les autres vies ».
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
