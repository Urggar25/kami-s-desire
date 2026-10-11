# Rencontres facultatives dans les explorations dirigées, J9 à J12.
# Aucun changement d'indice, de vote ou de relation. Un seul passage par trajet.

label KD_ROUTE_J9_ELEN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Elen sort de sa chambre en ajustant sa veste. Elle ralentit en me voyant."
    menu:
        "Discuter avec Elen.":
            $ showGroup([("elen", "inquiet", 0.35), ("noam", "neutre", 0.65)])
            elen inquiet "Tu crois que maintenant que Kami est revenue, tout va recommencer comme avant ?"
            noam reflexion "Avant quoi ?"
            elen "Avant sa panne. Les annonces, les votes, les journées qui se ressemblent..."
            noam "Elle a déjà repris ses habitudes, non ?"
            elen triste "Oui, mais pendant deux jours j'ai cru qu'on allait enfin pouvoir souffler."
            noam "Moi aussi."
            elen sourire "Bon. On ferait mieux d'y aller avant qu'elle nous reproche d'être en retard."
            noam sourire "Ce serait bien son genre."
            $ hideGroup()
        "Rejoindre le Conclave sans s'arrêter.":
            pass
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
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa apparaît au bout du couloir. Son regard s'arrête immédiatement sur mon visage."
    menu:
        "Répondre à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "fatigue", 0.65)])
            lysa blase "Tu as dormi ou tu as passé la nuit à te battre avec ton oreiller ?"
            noam "J'ai connu de meilleures nuits."
            lysa "Ça se voit. T'as une tête à faire peur à Goumi."
            noam taquin "Merci, ça m'aide beaucoup."
            lysa neutre "Je plaisante, mais t'as vraiment l'air mal. Il s'est passé quelque chose ?"
            noam hesitation "J'essaie encore de comprendre."
            lysa "D'accord. Mange quelque chose au moins, avant de t'écrouler."
            noam "C'est ce que je comptais faire."
            $ hideGroup()
        "Poursuivre vers la cafétéria.":
            pass
    return

label KD_ROUTE_J10_JULIAN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Julian est près de l'entrée de la salle commune. Il lève une main pour m'arrêter."
    menu:
        "Parler à Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
            julian sourire "Avant de rentrer, tu es plutôt pour ou contre ?"
            noam "Pour ou contre quoi, exactement ?"
            julian "Le prochain vote. J'essaie de prendre la température avant que Tomas sorte ses dossiers."
            noam reflexion "J'aimerais surtout entendre les arguments."
            julian taquin "La réponse préférée des gens qui ne veulent pas se mouiller."
            noam "Et toi, t'as choisi ?"
            julian hesitation "Pas vraiment. Mais j'avais envie de savoir si j'étais le seul."
            noam sourire "On est au moins deux."
            julian sourire "Parfait. Une coalition historique."
            $ hideGroup()
        "Entrer dans la salle commune.":
            pass
    return

label KD_ROUTE_J11_NYRA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Nyra sort d'un couloir latéral et s'arrête en remarquant ma démarche."
    menu:
        "Parler à Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "fatigue", 0.65)])
            nyra "Tu es sûr de pouvoir marcher jusque-là ?"
            noam "Oui. Pourquoi ?"
            nyra raison "Tu tiens à peine debout. Tu as dormi combien d'heures ?"
            noam "J'en sais rien. Pas assez."
            nyra "Alors évite de prendre une décision importante dans cet état."
            noam desaccord "Je vais simplement vérifier quelque chose."
            nyra reflexion "Dans ce cas, note ce que tu sais avant de commencer. Avec la fatigue, on mélange vite ce qu'on a vu et ce qu'on suppose."
            noam fatigue "Je vais essayer."
            nyra "Et demande de l'aide si tu te sens mal."
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
