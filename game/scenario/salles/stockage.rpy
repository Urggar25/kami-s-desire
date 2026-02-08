# -----------------------------------------------------------------------
# SALLE DE STOCKAGE — même modèle que CANON
# - 2 persos seulement : Noam + Nyra
# - Découverte : abondance de matériel, libre accès encadré
# - PNC : étagères / caisses au sol / terminal d'inventaire / règlement / retour
# -----------------------------------------------------------------------

default decouverte_stockage = False


label STOCKAGE_TP:
    scene bg_stockage at adaptive_fullscreen

    if not decouverte_stockage:
        jump decouverte_stockage

    $ pnc_room = "pnc_stockage"
    call screen pnc_stockage()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_stockage():

    modal True
    zorder 200

    add Solid("#000")

    # BG COVER
    add "images/background/bg_stockage.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS

    imagebutton:
        idle "images/background/interact/stockage/etageres.png"
        hover "images/background/interact/stockage/etageres_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("STO_PNC_ETAGERES")

    imagebutton:
        idle "images/background/interact/stockage/caisses.png"
        hover "images/background/interact/stockage/caisses_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("STO_PNC_CAISSES")

    imagebutton:
        idle "images/background/interact/stockage/reglement.png"
        hover "images/background/interact/stockage/reglement_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("STO_PNC_REGLEMENT")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


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

    $ showP("noam", "reflexion", 0.22)

    think "Ok."
    think "Ils ont vraiment prévu de quoi durer."

    "Au fond, une silhouette est déjà là."
    "Accroupie devant une caisse."
    "Elle trie et fouille dans les caisses sans se presser."

    $ showP("nyra", "fatigue", 0.78)

    "Elle sort un rouleau de câble."
    "Le repose."
    "Puis attrape une lampe."
    "Comme si elle faisait ses courses."

    $ showP("noam", "hesitation", 0.22)
    noam "…"
    $ showP("noam", "neutre", 0.22)
    noam "Salut."

    "Elle relève la tête."
    "Pas paniquée."
    "Juste surprise, une demi-seconde."

    $ showP("nyra", "surpris", 0.78)
    nyra "Oh. Euh..."
    $ showP("nyra", "neutre", 0.78)
    nyra "Salut."

    pause 0.2

    $ showP("noam", "reflexion", 0.22)
    noam "Je pensais tomber sur…"
    noam "genre un placard."
    noam "Avec trois tournevis et une boîte de pansements."

    $ showP("nyra", "rire", 0.78)
    nyra "Ouais."
    nyra "Moi j'avais imaginé une armoire qui ferme à clé."
    nyra "Et un petit mot du style : 'demander gentiment'."

    "Elle désigne la salle du menton."

    $ showP("nyra", "raison", 0.78)
    nyra "Mais non."
    nyra "C’est open bar."

    $ showP("noam", "surpris", 0.22)
    noam "Open bar…"
    noam "Sous Kami ?!"
    noam "C’est illégal dans tous les districts de se servir dans du stockage comme ça."

    $ showP("nyra", "taquin", 0.78)
    nyra "Ici, y’a plus de pays, et pas de districts."
    nyra "Ça simplifie."

    pause 0.3

    "Je m'approche."
    "Je lis des étiquettes."
    "Je vois des quantités."
    "Beaucoup trop."

    $ showP("noam", "reflexion", 0.22)
    think "C’est rassurant."
    think "Et en fait ça m’inquiète en même temps."

    $ showP("noam", "neutre", 0.22)
    noam "Je m'appelle Noam."
    noam "HARMONIE."

    $ showP("nyra", "neutre", 0.78)
    nyra "Nyra."
    nyra "ORBITE."

    $ showP("noam", "surpris", 0.22)
    noam "ORBITE."
    noam "Ok…"
    noam "Donc toi, tu dois avoir l’habitude des salles qui ressemblent à des hangars."

    $ showP("nyra", "rire", 0.78)
    nyra "Pas vraiment."
    nyra "Chez nous, tout est plus…"
    $ showP("nyra", "reflexion", 0.78)
    nyra "compact."
    nyra "Optimisé."
    nyra "Ici, franchement, la place c’est le grand luxe."
    nyra "Ça me fait presque bizarre."

    pause 0.2

    $ showP("noam", "taquin", 0.22)
    noam "Tu fais quoi, du coup ?"
    noam "Shopping ?"

    $ showP("nyra", "sourire", 0.78)
    nyra "Je regarde ce qu’ils ont laissé traîner."
    nyra "Parce que si y'a un problème…"
    $ showP("nyra", "raison", 0.78)
    nyra "c'est mieux de le savoir avant d'en avoir besoin."

    $ showP("noam", "raison", 0.22)
    noam "Ça c'est très ORBITE."
    noam "Prévoir la panne avant la panne."

    $ showP("nyra", "taquin", 0.78)
    nyra "Merci."
    nyra "On a une réputation à tenir."

    pause 0.3

    "Je repère un panneau sur le côté."
    "Plastifié."
    "Écrit gros."

    $ showP("noam", "reflexion", 0.22)
    noam "Matériel en libre accès…"
    noam "Sérieux ?"

    $ showP("nyra", "raison", 0.78)
    nyra "Ouais."
    nyra "Tu prends ce qu’il te faut."
    nyra "Tu remets après si tu as finis."

    $ showP("noam", "sourire", 0.22)
    noam "Et si j'embarque des souvenirs ?"

    $ showP("nyra", "taquin", 0.78)
    nyra "Ben…"
    nyra "Faut dire que les règles ne l'interdisent pas."

    $ showP("noam", "rire", 0.22)
    "Je ris rapidement."

    pause 0.3

    $ showP("noam", "reflexion", 0.22)
    noam "C’est marrant."
    noam "Ils nous donnent de quoi tenir."
    noam "De quoi réparer des trucs."
    noam "De quoi s’organiser."
    noam "Comme si on nous invitait à revenir à la vie d'il y a un an."

    $ showP("nyra", "reflexion", 0.78)
    nyra "Ouais."
    $ showP("nyra", "fatigue", 0.78)
    nyra "C’est pas de la gentillesse."
    nyra "C’est de l’efficacité."

    $ showP("noam", "raison", 0.22)
    noam "Tu penses que c’est pour qu’on se bouffe moins entre nous ?"

    $ showP("nyra", "raison", 0.78)
    nyra "Je pense que c’est pour qu’on tienne."
    nyra "Et pour que le show continue."
    nyra "Je crois que Kami a envie de nous voir 'dans notre état naturel'."
    $ showP("nyra", "taquin", 0.78)
    nyra "Désolée si je casse l’ambiance."

    $ showP("noam", "sourire", 0.22)
    noam "Non, c’est bien."
    noam "Au moins, c’est clair."

    pause 0.4

    "Je regarde une dernière fois la salle."
    "Les caisses."
    "Les étagères."
    "Le terminal."

    think "Le simple fait de fouiller dans un entrepot public est interdit dans les districts."
    think "Ici les règles ont vraiment été abolies ..."

    pause 0.4

    $ showP("noam", "reflexion", 0.22)
    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES

    jump STOCKAGE_TP

# Durée : 2m10
# Total: 51m25