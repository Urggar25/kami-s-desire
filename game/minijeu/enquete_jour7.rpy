# Jour 7 — recherche de matériel, intégrée au récit et au dossier permanent.
# Les variables historiques restent déclarées pour les sauvegardes existantes.
default j701_investigation_found = []
default j701_investigation_turn = 0
default j701_investigation_theory = "inconnue"

label j701_investigation:
    $ hideGroup()
    $ j701_investigation_found = []
    $ j701_investigation_turn = 0
    $ j701_investigation_theory = "inconnue"
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_j701_search_maintenance
    scene maintenance2 at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "inquiet", 0.25), ("noam", "neutre", 0.58), ("lysa", "blase", 0.90)])
    elias "Faites gaffe au câble par terre. J'ai sorti le panneau tout à l'heure, j'ai pas encore eu le temps de le remettre."
    lysa "Je comprends toujours pas pourquoi tu veux le mettre en marche. Il est très bien comme ça."
    elias "Mais regarde-moi ce truc ! Il peut bosser dans le vide, porter du matos dehors... J'aimerais au moins réussir à lui faire bouger les bras. J'ai presque fini de refaire les connexions."
    "Je me rapproche du robot. Lysa reste près de la porte."
    noam "Montre-moi ce qui manque."
    elias "J'étais là ce matin avant la livraison. J'avais vérifié les deux batteries, celle du robot et celle de rechange dans la réserve. Les outils étaient tous là aussi. Après, je suis parti aider à décharger et quand je suis revenu, impossible de remettre la main dessus."
    $ investigation_add("j7_temoignage_elias")
    $ j701_investigation_found.append("j7_temoignage_elias")
    "Elias nous désigne un logement ouvert sous les plaques du robot."
    elias "La batterie principale allait là. Elle était encore branchée ce matin."
    "Je m'accroupis. Le compartiment est vide."
    $ investigation_add("j7_batterie_robot")
    $ j701_investigation_found.append("j7_batterie_robot")
    lysa "Au moins, il risque pas de nous suivre dans les couloirs."
    "Elias inspecte les fixations et soulève les câbles débranchés."
    elias "Regarde, les connecteurs sont nickel. Même les attaches sont entières. Faut savoir où appuyer pour sortir la batterie sans casser le verrou. Ça, quelqu'un a pris le temps de le faire correctement."
    noam "Donc quelqu'un qui connaît ce genre de matériel, probablement."
    $ investigation_add("j7_demontage_robot")
    $ j701_investigation_found.append("j7_demontage_robot")
    "On regarde derrière le robot et sous les étagères. Rien."
    elias "Bon, on va vérifier les outils de l'autre côté."
    $ hideGroup()
    scene maintenance1 at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "reflechit", 0.28), ("noam", "neutre", 0.73)])
    "Des chutes métalliques encombrent l'établi. De longues marques de découpe sont encore visibles sur une plaque."
    elias "Tiens... Ça, c'était pas là ce matin."
    "Il repousse quelques copeaux du bout du doigt."
    elias "Quelqu'un a bricolé un gros truc ici. Regarde la taille des chutes. Il a dû déplacer la moitié des outils pour avoir assez de place."
    noam "C'est pas toi qui as fait ça en travaillant sur le robot ?"
    elias "Non, j'ai même pas touché à cet établi aujourd'hui. J'ai bossé directement sur le robot, avec mes outils."
    $ investigation_add("j7_etabli")
    $ j701_investigation_found.append("j7_etabli")
    "On ouvre les tiroirs et vérifie les casiers. Le micro-soudeur, les stabilisateurs et les outils de coupe manquent toujours."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("stockage", "bg_stockage") from _call_j701_search_stockage
    scene bg_stockage at adaptive_fullscreen with dissolve
    $ showGroup([("elias", "fatigue", 0.28), ("noam", "neutre", 0.72)])
    "La place de la batterie de rechange est vide. Elias regarde derrière les cartons de la livraison, puis les repousse contre le mur."
    elias "Bon, bah tant pis. J'attendrai la prochaine livraison pour continuer mes travaux. Ça me fait chier, j'avais enfin réussi à remettre les connexions en état."
    noam "Si quelqu'un les a prises pour bricoler, il finira peut-être par les ramener."
    elias "J'espère. Merci d'être venu, en tout cas."
    $ investigation_add("materiel_technique_manquant", notify=False)
    $ j701_investigation_turn = len(j701_investigation_found)
    $ hideGroup()
    return
