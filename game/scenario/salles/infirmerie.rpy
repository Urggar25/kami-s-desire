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

    if not decouverte_infirmerie and day_number() == 1:
        jump decouverte_infirmerie

    $ pnc_room = "pnc_infirmerie"
    call screen pnc_infirmerie()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_infirmerie():

    modal True
    zorder 200

    add Solid("#000")

    # BG COVER
    add "images/background/bg_infirmerie.png" at cover_screen

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

    if social_free_time_active() and elen_link == 3:
        imagebutton:
            idle Transform("images/character/elen/content.png", zoom=0.75)
            hover Transform("images/character/elen/inquiet.png", zoom=0.75)
            focus_mask True
            xalign 0.50
            yalign 0.30
            action [SetVariable("last_room_label", "INFIRMERIE_TP"), Jump("ELEN_LINK_INTERACT")]


    use exploration_retour_button

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

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("sael", "reflechit", 0.78),
    ])

    "La fille de tout à l'heure est déjà là."
    "Debout."
    "Les bras croisés."
    "Elle ne regarde pas les médicaments."
    "Elle regarde les casiers."

    noam hesitation "Il semble y avoir ce qu'il faut pour se faire prescrire un truc."

    sael sourire "Ouais."
    sael taquin "Une cure contre les idées de merde."
    sael taquin "Mais j’ai l’impression qu’il y a rupture de stock."

    "Je suis son regard."
    "Les casiers."
    "Le mur froid."
    "Les poignées."

    noam hesitation "Ne me dis pas que c'est ..."

    sael mefiant "Oh je crois bien que si."
    sael mefiant "C'est une morgue."
    
    sael reflechit "Regarde, on a chacun notre casier."
    
    "Elle pointe du doigt l'un des casiers."
    "Une étiquette se trouve à côté de la poignée."
    "Sael"
    
    
    sael taquin "Et là il y a le tiens."
    
    "Elle pointe le casier où il y a écris Julian."
    
    
    noam taquin "Ah non, je m'appelle pas Julian."
    
    
    "Elle semble désorientée un instant."
    sael surpris "Hein ? Ah bon ?!"
    
    noam taquin "Ben oui, si je te le dis."
    noam taquin "Moi je m'appelle Noam."
    
    "Elle regarde les casiers et cherche quelque chose du regard."
    
    
    sael determine "Rigole pas trop, tu as déjà ta place à la morgue toi aussi."

    "Un frisson me parcoure l'échine en entendant ce mot."

    noam reflexion "Je croyais que les commandements empêchaient… tout ça."

    sael desaccord "Ouais."
    sael desaccord "Ailleurs."
    sael raison "Sauf qu’on est pas 'chez nous'."
    sael raison "On est au Conclave."

    "Elle désigne la pièce d’un mouvement du menton."
    "Les étagères."
    "La table."
    "Les casiers."

    sael reflechit "Tu n’as pas fait attention, toi ?"
    sael reflechit "Ce petit détail qui change tout."
    sael reflechit "Ici, les commandements sont abolis."

    noam hesitation "Tu veux dire…"

    sael raison "Je veux dire que la violence est autorisée."
    sael mefiant "Si ce n'est souhaitée."
    sael mefiant "Mais rien ne permet de confirmer ça."

    "Je reste une seconde sans réponse."
    "Mon cerveau refuse l’information."
    "Puis il l’accepte, parce qu’il n’a pas vraiment le choix."
    "La présence d'une morgue en atteste."

    noam peur "Donc… les commandements c'est ...."
    noam peur "Oh putain ça craint."

    sael culpabilite "Ouais."

    "Comme si le simple fait de le dire lui collait quelque chose sur la langue."

    noam reflexion "Et on est censés faire quoi avec ça ?"

    sael determine "Déjà, le garder en tête."
    sael determine "Quand quelqu’un s’énerve."
    sael determine "Quand quelqu’un 'perd patience'."
    sael determine "Quand quelqu’un décide que c’est plus simple de régler un problème à l’ancienne."
    sael determine "Faut essayer de calmer le jeu."

    noam hesitation "À l’ancienne…"
    noam hesitation "Faut dire que c'est une salle qui a déjà le frigo prévu pour le corps."

    sael sourire "Voilà."
    sael taquin "Ambiance conviviale quoi."

    "Elle tente l’humour."
    "Mais son regard glisse encore vers les casiers."
    "Comme un réflexe. Comme une obsession."

    "Je fais quelques pas."
    "Je m’arrête devant les étagères."
    "Je lis des étiquettes."
    "Les noms des médicaments sont extrèmement compliqués, acétamino-bidule ; trigly-machin ..."
    "Je reconnais certaines racines à certains mots."
    "D’autres sont très flous."

    noam hesitation "Et ça…"
    noam hesitation "C’est en libre-service ?"

    sael mefiant "Bonne question."
    sael reflechit "Mais si c’est là, c’est que quelqu’un doit pouvoir s’en servir."
    sael reflechit "Etant donné qu'il n'y a pas de robot dans cette pièce."
    sael reflechit "C'est probablement… n’importe qui."

    noam culpabilite "Médicaments."
    noam culpabilite "Poisons."
    noam culpabilite "Sédatifs."
    noam culpabilite "On coche toutes les cases, là."
    
    sael taquin "Oh tu as l'oeil ! Il y a bien des poisons ici en plus de médicaments plus traditionnels."

    
    sael desaccord "Il y a aussi la table au fond."
    
    sael reflechit "Celle-là, c’est pas pour mettre un pansement."

    "Je regarde la table d’opération."
    "Les bras articulés."
    "Les écrans."
    "Les tiroirs."
    "Je déteste la manière dont tout paraît prêt."
    "Comme si toute la pièce n'attendait qu'une chose : que l'un d'entre nous se blesse."

    noam peur "J’aime pas ça."

    sael triste "Moi non plus."
    sael raison "Mais c’est justement pour ça que je voulais venir."

    noam reflexion "Pour te faire peur ?"

    sael rire "Non."
    sael reflechit "Pour me rappeler un truc."
    sael reflechit "Si ça dérape… Ou quand ça dérapera."
    sael determine "Je veux être prête au moment où quelqu’un me sautera dessus."

    noam hesitation "Tu parles comme si…"
    noam hesitation "Comme si tu t’y attendais."

    sael mefiant "Je m’y attends pas."
    sael raison "Je refuse juste d’être naïve."
    sael raison "Je m'y prépare."

    "Elle se tait une seconde."
    "Puis elle hausse les épaules, comme pour alléger."

    sael taquin "Et puis…"
    sael taquin "J’ai une réputation à tenir."
    sael sourire "Je suis censé être 'la gosse des rues'."

    noam rire "Ah."
    noam taquin "Donc c’est ça."
    noam taquin "Rien ne peut vraiment t'atteindre."

    sael joie "Exactement."
    sael taquin "Et je ne mourrais pas ici.."

    pause 0.4

    noam reflexion "T’as dit tout à l’heure que tu 'n’espérais pas devoir t’en servir'."

    sael triste "Ouais."

    noam hesitation "De ta force ?"

    sael culpabilite "Ouais."
    sael reflechit "Dans mon district, à Limen, quand ça part en vrille…"
    sael reflechit "Fin, oublie ce que j'ai dis.."
    sael triste "Je pense que personne n'a envie de voir ça ici.."

    sael raison "Voilà."
    sael determine "Donc je préfère espérer que rien n'arrive…"
    sael determine "Et me préparer au cas où."

    "Elle tapote doucement un casier."
    "Le métal renvoie un son sourd."

    think "Une morgue."
    think "Des poisons."
    think "Une table d’opération."
    think "Et des revues scientifiques."

    pause 0.4

    noam hesitation "On ressort, et on fait comme si tout était normal ?"

    sael sourire "Ouais."
    sael taquin "Comme des adultes responsables."
    sael taquin "Si on est là, c'est pour une raison."
    sael taquin "Il faut qu'on améliore la vie dans nos districts."

    noam sourire "Génial."
    noam rire "J’adore quand on me vend une journée tranquille."

    pause 0.5

    "Je recule d’un pas."
    "Je jette un dernier regard aux casiers."
    "Puis aux étagères."
    "Puis à la table, au fond."

    think "Je devrais aller voir ailleurs."
    think "Il faut que je trouve un endroit moins morbide."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_4

    $ hideGroup()
    jump INFIRMERIE_TP

# 3m20
# Total : 46m45
