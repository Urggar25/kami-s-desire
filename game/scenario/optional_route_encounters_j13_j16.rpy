# Rencontres optionnelles sur les trajets J13 à J16.
# Courtes, contournables et sans modification de l'enquête.

label KD_ROUTE_J13_JULIAN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Julian me rattrape avant le croisement qui mène à la cafétéria."
    menu:
        "Échanger quelques mots avec Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "fatigue", 0.65)])
            julian "Tu vas déjeuner avec les autres ?"
            noam "C'était l'idée."
            julian "Parfait. Ça fait au moins une personne qui ne m'a pas annoncé une catastrophe aujourd'hui."
            noam fatigue "Laisse-moi finir mon café avant de te répondre."
            julian hesitation "Ah. À ce point-là ?"
            noam "J'ai mal dormi, c'est tout."
            julian sourire "Alors je vais éviter mon grand discours sur les vertus du petit-déjeuner."
            noam taquin "Tu en avais vraiment préparé un ?"
            julian "Je suis toujours prêt à prendre la parole."
            $ hideGroup()
        "Continuer vers la cafétéria.":
            pass
    return

label KD_ROUTE_J13_ELIAS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Elias passe dans le couloir, une boîte de petites pièces sous le bras."
    menu:
        "Parler à Elias.":
            $ showGroup([("elias", "neutre", 0.35), ("noam", "fatigue", 0.65)])
            elias "Hé, Noam. T'as besoin d'un coup de main ?"
            noam "Pourquoi tu me demandes ça ?"
            elias "Tu regardes ta tablette comme si elle allait t'exploser à la figure."
            noam reflexion "C'est pas un problème technique."
            elias taquin "Pour une fois ? Je vais noter la date."
            noam "Tu fais que réparer les affaires des autres, ici ?"
            elias fatigue "Disons que ça m'évite de trop réfléchir au reste."
            noam "Pas bête, comme méthode."
            elias sourire "Si tu changes d'avis, tu sais où trouver l'atelier."
            $ hideGroup()
        "Retourner directement dans sa chambre.":
            pass
    return

label KD_ROUTE_J14_LYSA:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Lysa arrive en sens inverse et ralentit en me voyant rejoindre les dortoirs."
    menu:
        "Répondre à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "inquiet", 0.65)])
            lysa "Tu retournes déjà te coucher ?"
            noam "Non. J'ai quelqu'un à voir."
            lysa taquin "Mystérieux. Je dois deviner ou tu vas me le dire ?"
            noam "Je vais parler à Sael."
            lysa neutre "Ah. Bon courage, alors."
            noam reflexion "Pourquoi ?"
            lysa "Parce que vous avez tous les deux la tête de gens qui ont une conversation désagréable en retard."
            noam fatigue "C'est pas complètement faux."
            lysa blase "Évite juste de revenir encore plus énervé."
            $ hideGroup()
        "Continuer vers les dortoirs.":
            pass
    return

label KD_ROUTE_J15_ELEN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Elen m'aperçoit près du passage vers l'Observation et lève timidement la main."
    menu:
        "Saluer Elen.":
            $ showGroup([("elen", "inquiet", 0.35), ("noam", "fatigue", 0.65)])
            elen "Tu vas retrouver Kael ?"
            noam "Oui. Pourquoi ?"
            elen "Je sais pas trop ce que vous préparez, mais vous aviez pas l'air très détendus."
            noam reflexion "On doit vérifier certaines choses."
            elen "Alors... bon courage."
            noam sourire "C'est gentil."
            elen sourire "Et si ça se passe mal, viens manger avec nous après. Enfin, même si ça se passe bien."
            noam taquin "Je vais essayer de garder les deux options."
            elen joie "Ça me va !"
            $ hideGroup()
        "Poursuivre vers l'Observation.":
            pass
    return

label KD_ROUTE_J16_JULIAN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Julian s'arrête à ma hauteur et m'observe avec une curiosité peu discrète."
    menu:
        "Écouter Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "fatigue", 0.65)])
            julian "Tu fais cette tête depuis combien de temps ?"
            noam "Quelle tête ?"
            julian "Celle du type qui se prépare à interroger tout le Conclave."
            noam reflexion "J'ai juste mal dormi."
            julian "C'est fou, ici tout le monde dort mal et personne n'a jamais envie d'en parler."
            noam taquin "Tu tiens à entendre le récit de mes insomnies ?"
            julian hesitation "À la réflexion, non."
            noam "Alors on va manger."
            julian sourire "Voilà une proposition que je soutiens sans amendement."
            $ hideGroup()
        "Rejoindre la cafétéria.":
            pass
    return

label KD_ROUTE_J16_TOMAS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Tomas sort des Archives, sa tablette serrée contre lui."
    menu:
        "Répondre à Tomas.":
            $ showGroup([("tomas", "reflexion", 0.35), ("noam", "inquiet", 0.65)])
            tomas "Tu viens consulter les dossiers sur M16 ?"
            noam hesitation "Pourquoi cette question ?"
            tomas "Je t'ai vu regarder vers les Archives. Je pensais que tu cherchais les mêmes documents que nous."
            noam "J'ai autre chose à vérifier."
            tomas "Ah. Tu veux que je t'aide à retrouver un fichier ?"
            noam desaccord "Non, merci. Je préfère regarder tout seul."
            tomas inquiet "D'accord. Je voulais pas être indiscret."
            noam fatigue "Je sais. Désolé."
            tomas "Si tu ne trouves pas, le terminal classe les dossiers par date."
            $ hideGroup()
        "Entrer directement aux Archives.":
            pass
    return
