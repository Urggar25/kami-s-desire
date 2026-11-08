# -----------------------------------------------------------------------
# SALLE DE STOCKAGE — même modèle que CANON
# - 2 persos seulement : Noam + Nyra
# - Découverte : abondance de matériel, libre accès encadré
# - PNC : étagères / caisses au sol / terminal d'inventaire / règlement / retour
# -----------------------------------------------------------------------

default decouverte_stockage = False


label STOCKAGE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_350
    scene bg_stockage at adaptive_fullscreen

    if not decouverte_stockage and day_number() == 1:
        jump decouverte_stockage

    $ pnc_room = "pnc_stockage"
    call screen pnc_stockage()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_stockage():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("stockage")
    use room_scene_interactions("stockage")


label stockage_porte_couloir_sas:
    $ corridor_current = "sas"
    jump EXIT_ROOM_TO_CORRIDOR


label stockage_stockage:
    "Les rayonnages couvrent presque tous les murs."
    "Les cartons sont classés par catégorie, date de livraison et niveau de priorité."
    "Pièces de rechange, produits d'entretien, câbles, filtres et kits d'urgence : tout est compté."
    think "Assez pour vivre longtemps. Ou assez pour mesurer exactement ce qui disparaît."
    jump STOCKAGE_TP



label STO_PNC_ETAGERES:
    window auto

    "Les étagères montent presque jusqu’au plafond."
    "Bacs plastiques."
    "Cartons bruns."
    "Caisses métalliques."

    "Tout est étiqueté."
    "Outils."
    "Consommables."
    "Pièces de rechange."
    "Matériel de maintenance."

    think "C’est pas un placard."
    think "C’est une réserve pour tenir trente jours…"
    think "Ou pour tenir un siège."

    jump STOCKAGE_TP


label STO_PNC_CAISSES:
    window auto

    "Des caisses au sol, par groupes."
    "Certaines sont ouvertes."
    "D'autres scellées avec un verrou simple."

    "Je repère des rouleaux de câbles."
    "Des lampes."
    "Des kits de réparation."
    "Et des trucs que je n’identifie même pas."

    think "Le genre d’endroit où tu trouves toujours ce que tu cherches."
    think "Et où tu te demandes pourquoi on te le donne."

    jump STOCKAGE_TP


label STO_PNC_REGLEMENT:
    window auto

    "Un écran numériquue indique le réglement de la salle de stockage."
    "Écrit en gros, comme pour des enfants."

    "— Matériel en libre accès."
    "— Prenez ce dont vous avez besoin."
    "— Tout prélèvement est enregistré."
    "— Livraison hebdomadaire des matériaux manquants."
    "— Dégradation volontaire = sanction."

    think "Ils te donnent la clé."
    think "Et ils te rappellent où est la lame."

    jump STOCKAGE_TP


label STO_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_stockage:

    $ decouverte_stockage = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "J'imaginais une petite réserve, mais la porte de la salle de stockage est presque aussi large que celle d'un entrepôt."

    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_351
    scene bg_stockage at adaptive_fullscreen with fade

    "Des caisses et des rayonnages remplissent la salle. Une jeune femme est assise sur une caisse ouverte, un terminal posé sur les genoux et plusieurs objets soigneusement alignés à ses pieds."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("nyra", "fatigue", 0.78),
    ])

    noam sourire "Salut. On a le droit de se servir ici ?"
    nyra neutre "Rien n'indique le contraire. En revanche, si tu prends un objet, pense à signaler qu'il manque."
    noam taquin "Tu fais déjà la police des cartons ?"
    nyra sourire "J'essaie surtout d'éviter que quelqu'un cherche pendant une heure un objet que son voisin a emporté dans sa chambre."
    "Elle fait glisser une petite boîte sur le côté et coche une case sur son terminal."
    noam reflexion "Tu as commencé l'inventaire toute seule ?"
    nyra neutre "Oui. Ça va plus vite tant que personne n'a encore déplacé la moitié du stock."
    noam sourire "Moi c'est Noam, d'Harmonie."
    nyra neutre "Nyra. Orbite."
    $ unlock_character_name("nyra")
    noam sourire "Je peux t'aider ?"
    nyra reflechit "Pourquoi pas. Tu peux regarder ce qu'il y a dans cette caisse et me dire combien de lampes tu trouves ?"
    "Je soulève le couvercle. Plusieurs lampes sont rangées dans des compartiments en mousse."
    noam neutre "Six. Et elles ont l'air toutes neuves."
    nyra raison "Six, d'accord. C'est ce que le terminal annonçait."

    "Je prends une lampe et m'amuse à l'allumer en direction du plafond."
    noam taquin "On peut en garder une pour notre chambre ?"
    nyra reflechit "Tu peux, si tu en as besoin."
    noam sourire "Au cas où il y ait une panne de courant."
    nyra neutre "D'accord. Mais il n'en restera que cinq pour les autres représentants et les salles techniques."
    noam desaccord "Bon... Je vais la reposer."
    nyra sourire "C'est toi qui décides."
    noam taquin "Tu sais très bien ce que tu fais, là."
    nyra taquin "Je t'ai juste donné le nombre."
    noam rire "Ouais, bien sûr. Tu vas être dangereuse pendant les votes, toi."

    "Nyra prend une feuille plastifiée qu'elle a déjà remplie de catégories. En la parcourant, je découvre une ligne intitulée « utilité incertaine »."
    noam surpris "Attends. Tu as vraiment fait une catégorie pour les trucs inutiles ?"
    nyra reflechit "Pas inutiles. D'utilité incertaine. Si je sais pas à quoi sert quelque chose, je ne vais pas l'inventer."
    noam taquin "Et il y a une catégorie pour les objets vraiment inutiles ?"
    nyra raison "Oui. Mais elle est vide pour l'instant."
    noam rire "Tu te moques de moi."
    nyra sourire "Pas du tout."
    "Elle me montre le bas de son classement. Il y a effectivement une section réservée aux objets dépourvus de fonction identifiable."
    noam surpris "D'accord, tu gagnes. Je n'avais jamais vu quelqu'un prévoir aussi sérieusement de ne rien trouver."
    nyra taquin "C'est plus fréquent que tu ne l'imagines."

    "Nous remettons les lampes à leur place et refermons la caisse. Nyra vérifie une dernière fois son compte."
    noam reflexion "En fait, tu te prépares déjà au cas où on aurait des problèmes de matériel."
    nyra neutre "Je préfère savoir ce qu'on possède avant d'en avoir besoin. C'est tout."
    noam sourire "Et tu as prévu un endroit pour ranger le manuel de ce truc ?"
    nyra taquin "Oui. Dans la catégorie « documents que personne ne lit »."
    noam rire "Là, je reconnais que ça se tient."
    "Elle reprend son inventaire en me remerciant d'un signe de tête. Je quitte la réserve en faisant bien attention à ne rien emporter par erreur."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_9
    $ hideGroup()
    jump STOCKAGE_TP
