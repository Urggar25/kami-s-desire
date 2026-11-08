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
    think "Je pensais trouver une réserve fermée à clé. Vu la taille de la porte, il doit y avoir plus que quelques cartons derrière."
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_351
    scene bg_stockage at adaptive_fullscreen with fade
    "Les rayonnages sont pleins de matériel, de pièces de rechange et de caisses encore scellées. Une jeune femme a posé plusieurs objets devant elle et les examine un par un."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("nyra", "fatigue", 0.78),
    ])
    noam hesitation "Salut. Je peux prendre quelque chose ou il faut une autorisation ?"
    nyra neutre "Aucune autorisation affichée. En revanche, si tu prends le seul filtre de rechange, il faudra expliquer pourquoi."
    noam surpris "Je voulais juste regarder. Je savais même pas qu'on avait besoin d'un filtre."
    nyra reflexion "On en aura forcément besoin un jour. La question, c'est de savoir lequel et quand."
    noam sourire "Tu es déjà en train de faire l'inventaire ?"
    nyra neutre "J'essaie. Pour l'instant, les caisses sont classées par usage, mais les quantités ne correspondent pas toutes à ce qui est annoncé sur le terminal."
    noam inquiet "Il manque du matériel ?"
    nyra raison "Pas nécessairement. Certaines caisses n'ont pas encore été ouvertes. Je préfère vérifier avant de conclure."
    noam sourire "Moi c'est Noam, d'[codex_dialogue_link('harmonie', 'HARMONIE')]."
    nyra neutre "Nyra. Orbite."
    $ unlock_character_name("nyra")
    noam taquin "Ça explique pourquoi tu regardes les pièces détachées comme si ta vie en dépendait."
    nyra sourire "Dans une station spatiale, c'est parfois le cas."
    "Je prends une petite lampe sur l'étagère. Nyra lève les yeux vers ma main."
    nyra reflexion "Tu comptes l'utiliser ?"
    noam hesitation "Pas particulièrement. J'allais la prendre pour ma chambre, au cas où."
    nyra neutre "Il y en a six. Pour douze personnes et plusieurs zones techniques."
    noam desaccord "D'accord, j'ai compris. Je la repose."
    nyra taquin "Je ne t'ai rien interdit. Tu viens de décider tout seul qu'elle serait plus utile ici."
    noam taquin "Tu fais souvent ce coup-là ?"
    nyra sourire "Seulement quand ça marche."
    "Je repose la lampe. Sur le terminal, un tableau détaille les réserves et les prochaines livraisons."
    noam reflexion "C'est quand même étrange. On peut se servir librement, alors que sur Terre on n'aurait même pas le droit de toucher à ces stocks."
    nyra raison "Ici, personne n'a l'air chargé de distribuer le matériel. Alors soit on s'organise, soit on découvrira les pénuries au mauvais moment."
    noam neutre "Tu veux en parler aux autres ?"
    nyra reflexion "Quand j'aurai des chiffres fiables. Dire aux gens de se rationner sans savoir ce qu'on possède, ce serait idiot."
    noam sourire "Bon courage avec les cartons, alors."
    nyra taquin "Merci. Et si tu retrouves une lampe dans ta poche en sortant, tu sais où la remettre."
    noam rire "Je sens que tu vas être très agréable à vivre."
    nyra sourire "Seulement si les comptes sont bons."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_9
    $ hideGroup()
    jump STOCKAGE_TP
