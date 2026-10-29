# Exclusif au DLC « Les autres vies ».
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
