# Rencontres facultatives dans les explorations dirigées, J9 à J12.
# Aucun changement d'indice, de vote ou de relation. Un seul passage par trajet.

label KD_ROUTE_J9_ELEN:
    $ j901_elen_route_seen = True
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6
    $ showGroup([("elen", "inquiet", 0.32), ("noam", "neutre", 0.68)])
    "Elen arrive en trottinant derrière moi. Elle me prend par le poignet."
    elen "Noam ! Viens, vite ! J'ai FAIM !"
    noam surpris "Attends, je vais aussi au Conclave !"
    elen "J'ai demandé à Goumi un bout de pain, même ça il a refusé. Il m'a répété l'annonce de Kami trois fois !"
    noam "Tu comptais manger pendant la réunion ?"
    elen "Bah oui ! Si elle voulait pas perdre de temps, elle avait qu'à nous laisser manger !"
    window hide
    with hpunch
    pause 0.25
    "Elle me tire en avant. Je dois accélérer pour ne pas trébucher."
    elen triste "J'aimais bien ces deux journées, moi. On pouvait se lever tranquillement, faire des trucs ensemble..."
    noam "Moi aussi. On aurait pu en avoir une troisième."
    elen "Bon, on entre et on règle ça vite. Après, je prends deux petits-déjeuners."
    $ hideGroup()
    return

label KD_ROUTE_J9_TOMAS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Tomas consulte sa tablette près d'un croisement. Il relève les yeux quand j'approche."
    menu:
        "Écouter Tomas.":
            $ showGroup([("tomas", "reflexion", 0.35), ("noam", "neutre", 0.65)])
            tomas reflexion "Noam, tu peux me dire si cette formulation est claire ?"
            noam "Tu travailles encore sur le texte ?"
            tomas "Je vérifie qu'on parle bien de la même chose quand on dit « rétablir les échanges »."
            noam "Tu devrais peut-être poser la question pendant le débat."
            tomas inquiet "Justement. J'aimerais éviter qu'on découvre après le vote que chacun avait compris autre chose."
            noam reflexion "Alors dis-le comme ça. Tout le monde comprendra."
            tomas sourire "C'est probablement plus simple que les trois phrases que j'avais préparées."
            noam taquin "Tu vois, je suis utile."
            $ hideGroup()
        "Continuer vers la salle du Conclave.":
            pass
    return

label KD_ROUTE_J10_LYSA:
    $ j10011_lysa_route_seen = True
    scene couloir_dortoir at adaptive_fullscreen, j10_heat with dissolve
    $ showGroup([("lysa", "blase", 0.35), ("noam", "fatigue", 0.65)])
    lysa blase "J'ai pris trois douches à l'eau tiède cette nuit. Trois. J'avais à peine le temps de me sécher que j'étais de nouveau en sueur. C'est étouffant."
    noam fatigue "J'ai fini par virer le drap. Ça n'a servi à rien."
    lysa neutre "T'as réussi à dormir au moins ? Moi j'ai abandonné vers cinq heures. J'ai même ouvert la porte de ma chambre, mais il faisait aussi chaud dans le couloir."
    noam "Tu vas manger ?"
    lysa "Plus tard. Je vais essayer de trouver un élastique pour mes cheveux, ils me collent à la nuque."
    noam neutre "Bon courage. Je te garde de l'eau si j'en trouve de la fraîche."
    lysa sourire "Ah oui, je veux bien. Merci."
    $ hideGroup()
    return

label KD_ROUTE_J10_JULIAN:
    $ j10011_julian_route_seen = True
    scene couloir_cafeteria at adaptive_fullscreen, j10_heat with dissolve
    $ showGroup([("julian", "sourire", 0.35), ("noam", "fatigue", 0.65)])
    julian sourire "Noam ! Tu as vu le communiqué de ce matin ? La majorité des campements a été dispersée. Je pense qu'on peut dire que mon intervention d'hier a été utile."
    noam neutre "On n'a pas de chiffres."
    julian "Certes, mais si je n'avais pas pris la parole, combien de personnes seraient restées sur place ? Il fallait bien que quelqu'un leur dise de partir. Je ne regrette absolument pas ce que j'ai fait."
    noam fatigue "Je ne dis pas le contraire. Mais on ne sait pas combien ont réussi à partir."
    julian hesitation "Non, je sais. J'ai demandé à Nyra de me prévenir dès qu'elle aurait les chiffres. Enfin... j'espère qu'elle en aura."
    "Julian regarde sa tablette, puis relève la tête."
    julian sourire "En attendant, si quelqu'un veut me remercier, je ne m'y opposerai pas."
    noam "J'y penserai. Je vais voir Elias, il essaie de réparer la ventilation."
    julian "Ah, excellent. Dis-lui qu'il a tout mon soutien."
    $ hideGroup()
    return

label KD_ROUTE_J11_NYRA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Nyra sort d'un couloir latéral et s'arrête en remarquant ma démarche."
    menu:
        "Parler à Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "fatigue", 0.65)])
            nyra "Noam, attends. Tu as une tête affreuse. Tu comptes aller où comme ça ?"
            noam "À l'Observation. Je vais bien."
            nyra raison "Tu tiens à peine debout. Tu as au moins dormi cette nuit ?"
            noam "J'en sais rien. Pas assez."
            nyra "Assieds-toi cinq minutes si tu en as besoin. Ce que tu veux vérifier peut attendre que tu sois capable de lire un écran."
            noam desaccord "Je vais simplement vérifier quelque chose."
            nyra reflexion "D'accord, je vais pas te retenir. Mais note ce que tu observes avant d'essayer d'en tirer une conclusion. Je sais ce que ça fait de travailler sans avoir dormi."
            noam fatigue "Je vais essayer."
            nyra "Et si tu te sens mal, appelle quelqu'un. Même moi, si tu veux."
            $ hideGroup()
        "Continuer jusqu'à l'Observation.":
            pass
    return

label KD_ROUTE_J12_JULIAN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Julian rejoint le croisement au même moment que moi, une tablette serrée sous le bras."
    menu:
        "Échanger quelques mots avec Julian.":
            $ showGroup([("julian", "neutre", 0.35), ("noam", "fatigue", 0.65)])
            julian "Alors, tu sais ce que tu vas voter ?"
            noam reflexion "Pas complètement."
            julian "Ça me rassure presque. J'ai l'impression que tout le monde a déjà choisi son camp."
            noam "Toi aussi ?"
            julian hesitation "Je croyais. Plus on approche de la salle, moins j'en suis sûr."
            noam "Au moins, on pourra écouter le débat."
            julian sourire "Ouais. Pour une fois, je vais peut-être me taire et écouter."
            noam taquin "Je demande à voir."
            julian "Profite de cette occasion historique."
            $ hideGroup()
        "Rejoindre directement le vote.":
            pass
    return
