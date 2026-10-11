# Rencontres facultatives sur les navigations J17 à J24.
# Dialogues courts, sans indice indispensable et sans effet sur l'intrigue.

label KD_ROUTE_J17_LYSA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa m'aperçoit au croisement. Elle cesse de faire défiler sa tablette."
    menu:
        "Parler à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "inquiet", 0.65)])
            lysa "T'as la tête de quelqu'un qui va annoncer une catastrophe."
            noam fatigue "Tu peux éviter les blagues, aujourd'hui ?"
            lysa neutre "D'accord. Qu'est-ce qui se passe ?"
            noam "Il faut que je parle aux autres de M16."
            lysa reflexion "Tu sais quelque chose qu'on ignore ?"
            noam hesitation "Je sais surtout que ce qu'on croit savoir ne tient pas debout."
            lysa "Alors dis-leur clairement. On commence tous à en avoir assez des demi-réponses."
            noam neutre "Je vais essayer."
            lysa blase "Essaie surtout de ne pas tout garder pour toi."
            $ hideGroup()
        "Continuer vers la cafétéria.":
            pass
    return

label KD_ROUTE_J18_JULIAN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Julian est près de la sortie de la cafétéria. Il me regarde passer, puis m'interpelle."
    menu:
        "Répondre à Julian.":
            $ showGroup([("julian", "hesitation", 0.35), ("noam", "fatigue", 0.65)])
            julian "Tu cherches quelqu'un ?"
            noam "Elias. Je dois lui demander quelque chose."
            julian "Tu l'as déjà raté ce matin, non ?"
            noam reflexion "Je veux surtout lui parler avant qu'il disparaisse encore dans un atelier."
            julian taquin "Vu le bruit qu'il fait, il devrait être facile à retrouver."
            noam "C'est sérieux, Julian."
            julian neutre "J'avais compris. Tu n'as même pas souri."
            noam fatigue "Désolé."
            julian sourire "Va le voir. Je garde mes meilleures plaisanteries pour quand tu reviendras."
            $ hideGroup()
        "Poursuivre vers la maintenance.":
            pass
    return

label KD_ROUTE_J19_ELEN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Elen me rejoint près de la sortie, tandis que les voix des autres résonnent encore derrière elle."
    menu:
        "Rester quelques instants avec Elen.":
            $ showGroup([("elen", "inquiet", 0.35), ("noam", "fatigue", 0.65)])
            elen "Tu rentres déjà ? Il reste encore du monde."
            noam "J'ai besoin de me poser un peu."
            elen "Tu pourrais rester avec nous. Ça te changerait peut-être les idées."
            noam reflexion "Je crois pas que ça suffirait."
            elen inquiet "Tu sais, t'es pas obligé de régler tous tes problèmes tout seul."
            noam "Je sais. Mais ce soir, j'aimerais juste être tranquille."
            elen sourire "D'accord. Si tu changes d'avis, on sera encore là un moment."
            noam sourire "Merci, Elen."
            elen "Essaie au moins de dormir un peu."
            $ hideGroup()
        "Retourner directement au dortoir.":
            pass
    return

label KD_ROUTE_J22_NYRA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Nyra vérifie une liste sur sa tablette devant les dortoirs. Plusieurs sacs attendent près des portes."
    menu:
        "Discuter des préparatifs avec Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "neutre", 0.65)])
            nyra "Tu as déjà refait ton sac ?"
            noam "Pas vraiment. J'avais tout préparé pour partir, alors j'ai laissé l'essentiel dedans."
            nyra "Tu n'es pas le seul. Les livraisons et le départ repoussé ont compliqué l'inventaire."
            noam taquin "Tu fais aussi l'inventaire de nos valises ?"
            nyra "Seulement du matériel commun. Tes chaussettes ne m'intéressent pas."
            noam sourire "Me voilà rassuré."
            nyra reflexion "Vérifie quand même ton badge avant le dernier jour. Ce serait dommage de tout retrouver sauf ça."
            noam "Bonne idée. Merci."
            $ hideGroup()
        "Rejoindre la cafétéria.":
            pass
    return

label KD_ROUTE_J24_JULIAN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Julian s'arrête à côté de moi, une tasse vide dans la main."
    menu:
        "Échanger quelques mots avec Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
            julian "Alors, on prépare déjà le grand discours de victoire ?"
            noam "On n'a même pas encore terminé le texte."
            julian "Détail technique. Un bon orateur doit toujours prévoir les applaudissements."
            noam taquin "Tu pourrais commencer par prévoir les objections."
            julian hesitation "C'est pour ça que je laisse Tomas et toi travailler."
            noam "Très généreux."
            julian sourire "Je viendrai applaudir si vous arrivez à mettre tout le monde d'accord."
            noam reflexion "On n'y est pas encore."
            julian "Justement. Je préfère garder un peu d'optimisme pour nous deux."
            $ hideGroup()
        "Continuer vers les Archives.":
            pass
    return
