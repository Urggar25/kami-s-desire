# -----------------------------------------------------------------------
# INFIRMERIE — même modèle que CANON
# - 2 persos seulement : Noam + Sael
# - Découverte : violence autorisée au Conclave (hors commandements)
# - PNC : casiers réfrigérés (morgue) / étagères (médicaments-poisons) /
#         table d'opération / bibliothèque scientifique / retour
# -----------------------------------------------------------------------

default decouverte_infirmerie = False

label INFIRMERIE_TP:
    scene bg_infirmerie at adaptive_fullscreen

    if not decouverte_infirmerie:
        jump decouverte_infirmerie

    $ pnc_room = "pnc_infirmerie"
    call screen pnc_infirmerie()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_infirmerie():

    modal True
    zorder 200

    add Solid("#000")

    # BG COVER
    add "images/background/bg_infirmerie.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS

    imagebutton:
        idle "images/background/interact/infirmerie/morgue.png"
        hover "images/background/interact/infirmerie/morgue_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("INF_PNC_MORGUE")

    imagebutton:
        idle "images/background/interact/infirmerie/armoire.png"
        hover "images/background/interact/infirmerie/armoire_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("INF_PNC_ETAGERES")

    imagebutton:
        idle "images/background/interact/infirmerie/operation.png"
        hover "images/background/interact/infirmerie/operation_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("INF_PNC_TABLE")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


label INF_PNC_MORGUE:
    window auto

    "Les casiers réfrigérés occupent tout un pan de mur."
    "Des tiroirs longs."
    "Numérotés."
    "Avec des poignées épaisses."
    "Comme si on devait tirer fort."
    "Ou vite."

    think "Une morgue."
    think "Dans un endroit censé être… notre 'refuge'."

    "Le froid qui s’en dégage est propre."
    "Trop propre."
    "Ça sent le métal stérile et la désinfection."

    think "Ils ont prévu la place."
    think "Donc ils ont prévu le reste."

    jump INFIRMERIE_TP


label INF_PNC_ETAGERES:
    window auto

    "À gauche, des étagères pleines."
    "Boîtes blanches."
    "Flacons ambrés."
    "Poches scellées."
    "Certaines étiquettes sont nettes."
    "D’autres… volontairement vagues."

    "Je lis quelques mots."
    "Analgésique."
    "Sédatif."
    "Antibiotique."
    "Antidote."
    "Et, plus bas…"
    "Des symboles de danger."

    think "Médicaments et poisons."
    think "La frontière est parfois une question de dose."

    jump INFIRMERIE_TP


label INF_PNC_TABLE:
    window auto

    "Au fond, une table d’opération."
    "Éclairage directionnel."
    "Bras articulés."
    "Des instruments rangés dans des tiroirs."
    "Des machines qui attendent."
    "Écran de monitoring noir."
    "Comme un œil fermé."

    "Ça ne ressemble pas à une infirmerie de bureau."
    "Ça ressemble à un bloc."

    think "Donc ici… on répare."
    think "Ou on découpe."

    jump INFIRMERIE_TP


label INF_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_infirmerie:

    $ decouverte_infirmerie = True

    scene black
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    think "L'infirmerie."
    think "Un lieu qui serait anodin dans n'importe quel endroit."
    think "Mais ici, ça n'a rien de rassurant."

    pause 0.4

    scene bg_infirmerie at adaptive_fullscreen with fade

    "L’air est plus froid qu’ailleurs."
    "Et pas seulement à cause des machines."
    "Ça sent le désinfectant."
    "Le plastique neuf."
    "Et un truc comme si c'était métallique."

    "À gauche, il y a des étagères."
    "Plein de boîtes."
    "Plein de flacons."
    "Des produits qui sont alignés au millimètre près."

    "À droite, il y a des longs casiers réfrigérés."
    "Trop longs."
    "Trop nombreux."

    "Une longue table aseptisée trône au fond de la pièce."
    "Du matériel médical l'accompagne."
    "Et, dans un coin, une bibliothèque de revues scientifiques."
    "Comme si quelqu’un avait voulu ajouter une petite touche… humaine."

    $ showP("noam", "reflexion", 0.22)   # gauche
    $ showP("sael", "reflechit", 0.78)   # droite

    "La fille de tout à l'heure est déjà là."
    "Debout."
    "Les bras croisés."
    "Elle ne regarde pas les médicaments."
    "Elle regarde les casiers."

    $ showP("noam", "hesitation", 0.22)
    noam "Il semble y avoir ce qu'il faut pour se faire prescrire un truc."

    $ showP("sael", "sourire", 0.78)
    sael "Ouais."
    $ showP("sael", "taquin", 0.78)
    sael "Une cure contre les idées de merde."
    sael "Mais j’ai l’impression qu’il y a rupture de stock."

    $ showP("noam", "reflexion", 0.22)
    "Je suis son regard."
    "Les casiers."
    "Le mur froid."
    "Les poignées."

    $ showP("noam", "hesitation", 0.22)
    noam "Ne me dis pas que c'est ..."

    $ showP("sael", "mefiant", 0.78)
    sael "Oh je crois bien que si."
    sael "C'est une morgue."
    $ showP("sael", "reflechit", 0.78)
    
    sael "Regarde, on a chacun notre casier."
    
    "Elle pointe du doigt l'un des casiers."
    "Une étiquette se trouve à côté de la poignée."
    "Sael"
    
    $ showP("sael", "taquin", 0.78)
    
    sael "Et là il y a le tiens."
    
    "Elle pointe le casier où il y a écris Julian."
    
    $ showP("noam", "taquin", 0.22)
    
    noam "Ah non, je m'appelle pas Julian."
    
    $ showP("sael", "surpris", 0.78)
    
    "Elle semble désorientée un instant."
    sael "Hein ? Ah bon ?!"
    
    noam "Ben oui, si je te le dis."
    noam "Moi je m'appelle Noam."
    
    "Elle regarde les casiers et cherche quelque chose du regard."
    
    $ showP("sael", "determine", 0.78)
    
    sael "Rigole pas trop, tu as déjà ta place à la morgue toi aussi."

    "Un frisson me parcoure l'échine en entendant ce mot."

    $ showP("noam", "reflexion", 0.22)
    noam "Je croyais que les commandements empêchaient… tout ça."

    $ showP("sael", "desaccord", 0.78)
    sael "Ouais."
    sael "Ailleurs."
    $ showP("sael", "raison", 0.78)
    sael "Sauf qu’on est pas 'chez nous'."
    sael "On est au Conclave."

    "Elle désigne la pièce d’un mouvement du menton."
    "Les étagères."
    "La table."
    "Les casiers."

    $ showP("sael", "reflechit", 0.78)
    sael "Tu n’as pas fait attention, toi ?"
    sael "Ce petit détail qui change tout."
    sael "Ici, les commandements sont abolis."

    $ showP("noam", "hesitation", 0.22)
    noam "Tu veux dire…"

    $ showP("sael", "raison", 0.78)
    sael "Je veux dire que la violence est autorisée."
    $ showP("sael", "mefiant", 0.78)
    sael "Si ce n'est souhaitée."
    sael "Mais rien ne permet de confirmer ça."

    $ showP("noam", "panne", 0.22)
    "Je reste une seconde sans réponse."
    "Mon cerveau refuse l’information."
    "Puis il l’accepte, parce qu’il n’a pas vraiment le choix."
    "La présence d'une morgue en atteste."

    $ showP("noam", "peur", 0.22)
    noam "Donc… les commandements c'est ...."
    noam "Oh putain ça craint."

    $ showP("sael", "culpabilite", 0.78)
    sael "Ouais."

    "Comme si le simple fait de le dire lui collait quelque chose sur la langue."

    $ showP("noam", "reflexion", 0.22)
    noam "Et on est censés faire quoi avec ça ?"

    $ showP("sael", "determine", 0.78)
    sael "Déjà, le garder en tête."
    sael "Quand quelqu’un s’énerve."
    sael "Quand quelqu’un 'perd patience'."
    sael "Quand quelqu’un décide que c’est plus simple de régler un problème à l’ancienne."
    sael "Faut essayer de calmer le jeu."

    $ showP("noam", "hesitation", 0.22)
    noam "À l’ancienne…"
    noam "Faut dire que c'est une salle qui a déjà le frigo prévu pour le corps."

    $ showP("sael", "sourire", 0.78)
    sael "Voilà."
    $ showP("sael", "taquin", 0.78)
    sael "Ambiance conviviale quoi."

    "Elle tente l’humour."
    "Mais son regard glisse encore vers les casiers."
    "Comme un réflexe. Comme une obsession."

    $ showP("noam", "reflexion", 0.22)
    "Je fais quelques pas."
    "Je m’arrête devant les étagères."
    "Je lis des étiquettes."
    "Les noms des médicaments sont extrèmement compliqués, acétamino-bidule ; trigly-machin ..."
    "Je reconnais certaines racines à certains mots."
    "D’autres sont très flous."

    $ showP("noam", "hesitation", 0.22)
    noam "Et ça…"
    noam "C’est en libre-service ?"

    $ showP("sael", "mefiant", 0.78)
    sael "Bonne question."
    $ showP("sael", "reflechit", 0.78)
    sael "Mais si c’est là, c’est que quelqu’un doit pouvoir s’en servir."
    sael "Etant donné qu'il n'y a pas de robot dans cette pièce."
    sael "C'est probablement… n’importe qui."

    $ showP("noam", "culpabilite", 0.22)
    noam "Médicaments."
    noam "Poisons."
    noam "Sédatifs."
    noam "On coche toutes les cases, là."
    
    $ showP("sael", "taquin", 0.78)
    sael "Oh tu as l'oeil ! Il y a bien des poisons ici en plus de médicaments plus traditionnels."

    $ showP("sael", "desaccord", 0.78)
    
    sael "Il y a aussi la table au fond."
    
    $ showP("sael", "reflechit", 0.78)
    sael "Celle-là, c’est pas pour mettre un pansement."

    "Je regarde la table d’opération."
    "Les bras articulés."
    "Les écrans."
    "Les tiroirs."
    "Je déteste la manière dont tout paraît prêt."
    "Comme si toute la pièce n'attendait qu'une chose : que l'un d'entre nous se blesse."

    $ showP("noam", "peur", 0.22)
    noam "J’aime pas ça."

    $ showP("sael", "triste", 0.78)
    sael "Moi non plus."
    $ showP("sael", "raison", 0.78)
    sael "Mais c’est justement pour ça que je voulais venir."

    $ showP("noam", "reflexion", 0.22)
    noam "Pour te faire peur ?"

    $ showP("sael", "rire", 0.78)
    sael "Non."
    $ showP("sael", "reflechit", 0.78)
    sael "Pour me rappeler un truc."
    sael "Si ça dérape… Ou quand ça dérapera."
    $ showP("sael", "determine", 0.78)
    sael "Je veux être prête au moment où quelqu’un me sautera dessus."

    $ showP("noam", "hesitation", 0.22)
    noam "Tu parles comme si…"
    noam "Comme si tu t’y attendais."

    $ showP("sael", "mefiant", 0.78)
    sael "Je m’y attends pas."
    $ showP("sael", "raison", 0.78)
    sael "Je refuse juste d’être naïve."
    sael "Je m'y prépare."

    "Elle se tait une seconde."
    "Puis elle hausse les épaules, comme pour alléger."

    $ showP("sael", "taquin", 0.78)
    sael "Et puis…"
    sael "J’ai une réputation à tenir."
    $ showP("sael", "sourire", 0.78)
    sael "Je suis censé être 'la gosse des rues'."

    $ showP("noam", "rire", 0.22)
    noam "Ah."
    $ showP("noam", "taquin", 0.22)
    noam "Donc c’est ça."
    noam "Rien ne peut vraiment t'atteindre."

    $ showP("sael", "joie", 0.78)
    sael "Exactement."
    $ showP("sael", "taquin", 0.78)
    sael "Et je ne mourrais pas ici.."

    pause 0.4

    $ showP("noam", "reflexion", 0.22)
    noam "T’as dit tout à l’heure que tu 'n’espérais pas devoir t’en servir'."

    $ showP("sael", "triste", 0.78)
    sael "Ouais."

    $ showP("noam", "hesitation", 0.22)
    noam "De ta force ?"

    $ showP("sael", "culpabilite", 0.78)
    sael "Ouais."
    $ showP("sael", "reflechit", 0.78)
    sael "Dans mon district, à Limen, quand ça part en vrille…"
    sael "Fin, oublie ce que j'ai dis.."
    $ showP("sael", "triste", 0.78)
    sael "Je pense que personne n'a envie de voir ça ici.."

    $ showP("sael", "raison", 0.78)
    sael "Voilà."
    $ showP("sael", "determine", 0.78)
    sael "Donc je préfère espérer que rien n'arrive…"
    sael "Et me préparer au cas où."

    "Elle tapote doucement un casier."
    "Le métal renvoie un son sourd."

    $ showP("noam", "reflexion", 0.22)
    think "Une morgue."
    think "Des poisons."
    think "Une table d’opération."
    think "Et des revues scientifiques."

    pause 0.4

    $ showP("noam", "hesitation", 0.22)
    noam "On ressort, et on fait comme si tout était normal ?"

    $ showP("sael", "sourire", 0.78)
    sael "Ouais."
    $ showP("sael", "taquin", 0.78)
    sael "Comme des adultes responsables."
    sael "Si on est là, c'est pour une raison."
    sael "Il faut qu'on améliore la vie dans nos districts."

    $ showP("noam", "sourire", 0.22)
    noam "Génial."
    $ showP("noam", "rire", 0.22)
    noam "J’adore quand on me vend une journée tranquille."

    pause 0.5

    $ showP("noam", "reflexion", 0.22)
    "Je recule d’un pas."
    "Je jette un dernier regard aux casiers."
    "Puis aux étagères."
    "Puis à la table, au fond."

    think "Je devrais aller voir ailleurs."
    think "Il faut que je trouve un endroit moins morbide."
    
    call CHECK_ALL_SALLES_VISITEES

    jump INFIRMERIE_TP

# 3m20
# Total : 46m45