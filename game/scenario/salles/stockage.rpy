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

    think "Et voici la salle de stockage."
    think "Le mot est banal, presque anodin. Mais si c'est vide… on est peut-être déjà morts."
    think "Donc j'espère que ça ne l'est pas."

    pause 0.4

    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_MAYBE_PLAY_SCRIPTED_DOOR_351
    scene bg_stockage at adaptive_fullscreen with fade

    "La pièce est immense. Il y a des étagères partout."
    "Et des caisses au sol, comme si quelqu’un avait livré ça hier."

    think "Ça sent le métal froid et le carton neuf, un drôle de mélange."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("nyra", "fatigue", 0.78),
    ])

    think "Ok. Ah ouais. Ils ont vraiment prévu de tout !"

    "Au fond, une silhouette est déjà là. Accroupie devant une caisse, en train de fouiller presque religieusement."

    "Elle sort un rouleau de câble. Le repose."
    "Puis attrape une lampe. Comme si elle faisait ses courses."

    noam hesitation "… Euh, salut."

    "Elle relève la tête. Pas paniquée mais surprise, elle n'a pas du m'entendre arriver."

    nyra surpris "Oh. Euh..."
    nyra neutre "Salut."

    pause 0.2

    noam reflexion "Je pensais tomber sur… genre un placard."
    noam reflexion "Avec trois tournevis et une boîte de pansements."

    nyra rire "Ouais. Moi j'avais imaginé une armoire qui ferme à clé ou un truc du genre."
    nyra rire "Et un petit mot du style : 'demander gentiment'."

    "Elle désigne la salle du menton."

    nyra raison "Mais non. C’est open bar. Tout est en libre accès."

    noam surpris "Open bar… Sous Kami ?!"
    noam surpris "C’est illégal dans tous les districts de se servir dans du stockage comme ça."

    nyra taquin "Faut dire qu'ici plus aucune règle ne s'applique, elle a été bien claire là-dessus."

    pause 0.3

    "Je m'approche. Je lis des étiquettes. Je regarde ce qu'il y a."

    think "C’est rassurant. Et en fait ça m’inquiète en même temps."

    noam neutre "Je m'appelle Noam."
    noam neutre "Je viens d'[codex_dialogue_link('harmonie', 'HARMONIE')]."

    nyra neutre "Nyra."
    $ unlock_character_name("nyra")
    nyra neutre "ORBITE."

    noam surpris "ORBITE.Ok…"
    noam surpris "Donc toi, tu dois avoir l’habitude des salles qui ressemblent à des hangars."

    nyra rire "Pas vraiment. En fait c'est carrément l'inverse."
    nyra rire "Chez nous, tout est plus… compact, optimisé."
    nyra reflexion "Ici, franchement, la place c’est le grand luxe."
    nyra reflexion "Ça me fait presque bizarre."

    pause 0.2

    noam taquin "Tu fais quoi, du coup ? Du shopping ?"

    nyra sourire "Je regarde ce qu’ils ont laissé traîner."
    nyra sourire "Parce que si y'a un problème… C'est mieux de le savoir avant d'en avoir besoin."

    nyra taquin "Et la bonne nouvelle c'est qu'on trouve vraiment tout ! C'est une vraie montagne de trésor !"

    noam raison "J'imagine que vous faites toujours ça sur Orbite. Prévoir la panne avant la panne."

    nyra taquin "Merci. On a une réputation à tenir."

    pause 0.3

    "Je repère un panneau sur le côté. Plastifié avec une grosse écriture."

    noam reflexion "Whaou, c'est vraiment en libre accès… Sérieux ?"

    nyra raison "Ouais. Tu prends ce qu’il te faut et idéalement tu le ramènes après."
    nyra reflexion "Il y a des livraisons régulières s'il manque du matériel."

    noam sourire "Et si j'embarque des souvenirs ?"

    nyra taquin "Ben… Faut dire que les règles ne l'interdisent pas."
    nyra joie "Et il y a bien deux trois bricoles intéressantes ici !"

    pause 0.3

    noam reflexion "C’est marrant. Ils nous donnent de quoi tenir."
    noam reflexion "De quoi réparer des trucs. De quoi s’organiser."
    noam reflexion "Comme si on nous invitait à revenir à la vie d'il y a un an."

    nyra reflexion "Ouais. Je sais pas trop pourquoi, mais c'est bizarre."

    pause 0.4

    "Je regarde une dernière fois la salle. Les caisses, les étagères."

    think "Le simple fait de fouiller dans un entrepot public est interdit dans les districts."
    think "Ici les règles ont vraiment été abolies..."

    pause 0.4

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_9

    $ hideGroup()
    jump STOCKAGE_TP

# Durée : 2m10
# Total: 51m25
