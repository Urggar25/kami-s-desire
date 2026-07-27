# -----------------------------------------------------------------------
# SALLE DE STOCKAGE — même modèle que CANON
# - 2 persos seulement : Noam + Nyra
# - Découverte : abondance de matériel, libre accès encadré
# - PNC : étagères / caisses au sol / terminal d'inventaire / règlement / retour
# -----------------------------------------------------------------------

default decouverte_stockage = False


label STOCKAGE_TP:
    scene bg_stockage at adaptive_fullscreen

    if not decouverte_stockage and day_number() == 1:
        jump decouverte_stockage

    if social_free_time_active() and free_time_round in [1, 2, 3] and not got_argument_echanges_discrets:
        jump temps_libre_salle_stockage_argument

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

    think "Salle de stockage."
    think "Le mot est banal, presque anodin."
    think "Mais si c'est vide… on est morts."
    think "Donc j'espère que ça ne l'est pas."

    pause 0.4

    scene bg_stockage at adaptive_fullscreen with fade

    "La pièce est immense."
    "Il y a des étagères partout."
    "Et des caisses au sol, comme si quelqu’un avait livré ça hier."

    "Ça sent le métal froid."
    "Et le carton neuf."
    "Un drôle de mélange olfactif."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("nyra", "fatigue", 0.78),
    ])

    think "Ok."
    think "Ils ont vraiment prévu de quoi durer."

    "Au fond, une silhouette est déjà là."
    "Accroupie devant une caisse."
    "Elle trie et fouille dans les caisses sans se presser."


    "Elle sort un rouleau de câble."
    "Le repose."
    "Puis attrape une lampe."
    "Comme si elle faisait ses courses."

    noam hesitation "…"
    noam neutre "Salut."

    "Elle relève la tête."
    "Pas paniquée."
    "Juste surprise, une demi-seconde."

    nyra surpris "Oh. Euh..."
    nyra neutre "Salut."

    pause 0.2

    noam reflexion "Je pensais tomber sur…"
    noam reflexion "genre un placard."
    noam reflexion "Avec trois tournevis et une boîte de pansements."

    nyra rire "Ouais."
    nyra rire "Moi j'avais imaginé une armoire qui ferme à clé."
    nyra rire "Et un petit mot du style : 'demander gentiment'."

    "Elle désigne la salle du menton."

    nyra raison "Mais non."
    nyra raison "C’est open bar."

    noam surpris "Open bar…"
    noam surpris "Sous Kami ?!"
    noam surpris "C’est illégal dans tous les districts de se servir dans du stockage comme ça."

    nyra taquin "Ici, y’a plus de pays, et pas de districts."
    nyra taquin "Ça simplifie."

    pause 0.3

    "Je m'approche."
    "Je lis des étiquettes."
    "Je vois des quantités."
    "Beaucoup trop."

    think "C’est rassurant."
    think "Et en fait ça m’inquiète en même temps."

    noam neutre "Je m'appelle Noam."
    noam neutre "HARMONIE."

    nyra neutre "Nyra."
    nyra neutre "ORBITE."

    noam surpris "ORBITE."
    noam surpris "Ok…"
    noam surpris "Donc toi, tu dois avoir l’habitude des salles qui ressemblent à des hangars."

    nyra rire "Pas vraiment."
    nyra rire "Chez nous, tout est plus…"
    nyra reflexion "compact."
    nyra reflexion "Optimisé."
    nyra reflexion "Ici, franchement, la place c’est le grand luxe."
    nyra reflexion "Ça me fait presque bizarre."

    pause 0.2

    noam taquin "Tu fais quoi, du coup ?"
    noam taquin "Shopping ?"

    nyra sourire "Je regarde ce qu’ils ont laissé traîner."
    nyra sourire "Parce que si y'a un problème…"
    nyra raison "c'est mieux de le savoir avant d'en avoir besoin."

    noam raison "Ça c'est très ORBITE."
    noam raison "Prévoir la panne avant la panne."

    nyra taquin "Merci."
    nyra taquin "On a une réputation à tenir."

    pause 0.3

    "Je repère un panneau sur le côté."
    "Plastifié."
    "Écrit gros."

    noam reflexion "Matériel en libre accès…"
    noam reflexion "Sérieux ?"

    nyra raison "Ouais."
    nyra raison "Tu prends ce qu’il te faut."
    nyra raison "Tu remets après si tu as finis."

    noam sourire "Et si j'embarque des souvenirs ?"

    nyra taquin "Ben…"
    nyra taquin "Faut dire que les règles ne l'interdisent pas."

    "Je ris rapidement."

    pause 0.3

    noam reflexion "C’est marrant."
    noam reflexion "Ils nous donnent de quoi tenir."
    noam reflexion "De quoi réparer des trucs."
    noam reflexion "De quoi s’organiser."
    noam reflexion "Comme si on nous invitait à revenir à la vie d'il y a un an."

    nyra reflexion "Ouais."
    nyra fatigue "C’est pas de la gentillesse."
    nyra fatigue "C’est de l’efficacité."

    noam raison "Tu penses que c’est pour qu’on se bouffe moins entre nous ?"

    nyra raison "Je pense que c’est pour qu’on tienne."
    nyra raison "Et pour que le show continue."
    nyra raison "Je crois que Kami a envie de nous voir 'dans notre état naturel'."
    nyra taquin "Désolée si je casse l’ambiance."

    noam sourire "Non, c’est bien."
    noam sourire "Au moins, c’est clair."

    pause 0.4

    "Je regarde une dernière fois la salle."
    "Les caisses."
    "Les étagères."
    "Le terminal."

    think "Le simple fait de fouiller dans un entrepot public est interdit dans les districts."
    think "Ici les règles ont vraiment été abolies ..."

    pause 0.4

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_9

    $ hideGroup()
    jump STOCKAGE_TP

# Durée : 2m10
# Total: 51m25
