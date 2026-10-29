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

