# JOUR 28 — CE QUI RESTE DANS LES CONDUITS
# Route alternative du vote rejeté. Le coupable reste inconnu.
default j28a_plaque = False
default j28a_bol = False
default j28a_bulbuma = False
default j28a_detours = 0

label _28_0_1_1_0_1_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"
    $ j28a_plaque = False
    $ j28a_bol = False
    $ j28a_bulbuma = False
    $ j28a_detours = 0
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille en pensant encore à Tomas. Hier, j'ai passé ma journée à fouiller ses papiers. Au final, j'ai surtout découvert qu'il avait encore beaucoup de questions."
    "Une notification apparaît sur ma tablette : livraison du jour 28."
    noam fatigue "Ah oui... Les caisses."
    "Je regarde une dernière fois les photos de Keyper, puis je m'habille."
    think "Aujourd'hui, il faut que je comprenne ce qui s'est passé dans cette chambre."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j28a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _28_0_1_1_0_1_LIVRAISON

label _28_0_1_1_0_1_LIVRAISON:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Près du sas de livraison, Elias et Elen chargent des caisses sur un chariot. Goumi attend derrière eux."
    $ showGroup([("elias", "fatigue", 0.20), ("elen", "reflexion", 0.42), ("noam", "neutre", 0.64), ("lysa", "blase", 0.87)])
    elias fatigue "Attends, Elen, pas celle-là."
    elen neutre "Pourquoi ?"
    elias raison "Elle est plus lourde."
    "La caisse cogne contre le chariot. Elen la retient de justesse."
    elen peur "Oh ! Merde !"
    noam surpris "Ça va ?"
    elen fatigue "Ouais. C'est rien."
    lysa blase "C'est la deuxième en cinq minutes."
    elen colere "Lysa !"
    lysa neutre "Quoi ? Je compte."
    "Je les aide à remettre la caisse en place."
    noam reflexion "Kami a toujours pas arrêté les livraisons ?"
    elias fatigue "Non. C'est pareil que d'habitude. Infirmerie, cafétéria, maintenance."
    elen triste "Elle fait vraiment comme si rien s'était passé."
    noam neutre "Tu veux qu'on termine sans toi ?"
    elen fatigue "Non. J'ai besoin de faire quelque chose. Si je reste seule, je vais encore penser à Tomas."
    lysa inquiet "Elen..."
    elen neutre "Ça va. Enfin, non, mais j'ai pas envie d'en parler pour l'instant."
    noam raison "OK. On termine les caisses."
    "Une fois le chargement fini, Elias repart avec Goumi et Elen. Lysa me rejoint."
    lysa reflexion "Tu vas à l'infirmerie ?"
    noam neutre "Ouais. Je veux voir si Iris a avancé."
    lysa raison "Je viens."
    $ hideGroup()
    jump _28_0_1_1_0_1_INFIRMERIE

label _28_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_2
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    "Iris est penchée sur ses résultats. Elle a l'air de ne pas avoir dormi."
    $ showGroup([("iris", "fatigue", 0.24), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.70)])
    iris fatigue "Si vous venez demander si j'ai trouvé la cause du décès, je vais mettre une affiche sur la porte."
    noam taquin "Avec juste « non » écrit dessus ?"
    iris blase "Exactement."
    lysa reflexion "T'as quand même une piste ?"
    iris raison "Une intoxication est possible. On s'est trop concentrés sur les somnifères."
    noam reflexion "Tu crois qu'il a rien pris ?"
    iris neutre "Je sais pas ce qu'il a pris. C'est bien le problème."
    noam raison "Il transpirait beaucoup."
    iris reflexion "Oui. Pas de blessure évidente, des draps trempés... Et vous vous souvenez de nos maux de tête ?"
    lysa blase "Comment oublier cette odeur ?"
    iris raison "On a dit que ça venait des déchets. Mais il y avait peut-être autre chose."
    noam reflexion "Tu penses à un gaz ?"
    iris neutre "À une substance inhalée. Je sais pas encore laquelle, ni même s'il y en avait une."
    lysa raison "Les restes de nourriture d'Elen auraient pu masquer une odeur."
    iris reflexion "Voilà. Et on n'a regardé que la grille d'aération, pas ce qu'il y avait derrière."
    noam fatigue "Tu veux retourner dans les conduits."
    iris sourire "Pour une fois, t'as compris avant moi."
    noam agace "Merci."
    iris raison "On prend des gants, des masques et des sachets. Si vous trouvez quelque chose, vous ne le touchez pas n'importe comment."
    lysa neutre "Je vais chercher une lampe."
    "Iris rassemble le matériel. Elle propose de rester dans la chambre d'Elen pour nous guider pendant qu'on passe par l'accès de maintenance."
    $ hideGroup()
    jump _28_0_1_1_0_1_CHAMBRE

label _28_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "On rouvre la chambre d'Elen. L'odeur est moins forte, mais elle me rappelle immédiatement le corps de Tomas."
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "reflexion", 0.23), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    lysa fatigue "Bon. Ça sent toujours la mort ici."
    iris raison "La plaque est toujours devant la grille. Les fixations n'ont pas bougé."
    noam neutre "C'est ce qu'on avait vérifié."
    iris reflexion "Oui. Elle bloque le passage d'une personne, pas le flux d'air."
    noam reflexion "Donc quelque chose pouvait venir du conduit sans qu'on ouvre la porte."
    iris neutre "C'est possible. Je veux juste savoir si le réseau a été modifié."
    lysa raison "Tu nous guideras par téléphone ?"
    iris neutre "Oui. Et vous prenez des photos avant de déplacer quoi que ce soit."
    noam sourire "Compris."
    iris agace "Je parle surtout à toi."
    "Je laisse à Iris une copie du plan des conduits."
    $ hideGroup()
    jump _28_0_1_1_0_1_CONDUIT

label _28_0_1_1_0_1_CONDUIT:
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_horror_pulse.mp3" fadein 1.0
    $ showGroup([("lysa", "inquiet", 0.38), ("noam", "neutre", 0.68)])
    lysa blase "Si je reste coincée, tu me sors de là."
    noam sourire "Ça va bien se passer."
    lysa fatigue "C'est pas ce que j'ai demandé."
    "On ouvre l'accès technique. Je passe devant, Lysa me suit."
    $ hideGroup()
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on()
    "La lampe éclaire un conduit très étroit. Derrière moi, Lysa cogne déjà son genou contre le métal."
    lysa fatigue "Putain, c'est petit."
    noam neutre "Faut suivre les flèches vers les dortoirs."
    jump _28_0_1_1_0_1_CONDUIT_1

label _28_0_1_1_0_1_CONDUIT_1:
    menu:
        "À quel passage se fier ?"
        "La branche des dortoirs":
            "On avance vers un réseau plus étroit. Le plan correspond à ce qu'Iris nous a envoyé."
            jump _28_0_1_1_0_1_CONDUIT_2
        "Le conduit qui descend vers les machines":
            $ j28a_detours += 1
            "On débouche devant un ventilateur qui barre complètement le passage."
            lysa fatigue "Tu vois bien qu'on va pas passer là !"
            noam agace "Ouais, demi-tour."
            "On revient au croisement et reprend la branche des dortoirs."
            jump _28_0_1_1_0_1_CONDUIT_2

label _28_0_1_1_0_1_CONDUIT_2:
    "Un nouveau croisement apparaît. J'appelle Iris."
    iris "Vous voyez le repère quatre ?"
    noam raison "Ouais, avec deux passages."
    iris "Prenez la dérivation à droite du boîtier. C'est elle qui mène à la chambre d'Elen."
    menu:
        "Quelle direction prendre ?"
        "Suivre le repère indiqué par Iris":
            jump _28_0_1_1_0_1_CONDUIT_3
        "Explorer la branche la plus large":
            $ j28a_detours += 1
            "Une grille donne sur le couloir de l'autre côté des dortoirs."
            lysa blase "C'est pas du tout sa chambre."
            noam fatigue "Je sais. On revient."
            "On retrouve le croisement et suit les indications d'Iris."
            jump _28_0_1_1_0_1_CONDUIT_3


label _28_0_1_1_0_1_CONDUIT_3:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    "Un peu plus loin, la lumière accroche une plaque métallique placée de travers. Elle coupe presque toute la largeur du conduit."
    lysa reflexion "Attends. Ça, c'est normal ?"
    noam reflexion "J'ai jamais vu une plaque comme ça."
    iris "Vous êtes à la grille ?"
    noam neutre "Presque. Il y a un truc en métal juste avant."
    iris "Ne forcez pas. Regarde comment l'air peut passer."
    menu:
        "Comment examiner la plaque ?"
        "Observer les fixations et le passage d'air":
            "La plaque est coincée sur des supports. L'air n'a plus qu'une ouverture étroite pour passer vers la chambre."
            jump _28_0_1_1_0_1_PLAQUE
        "Essayer de pousser directement":
            $ j28a_detours += 1
            play sound "audio/sfx_duct_scrape.wav"
            "Le métal résiste et grince contre la paroi."
            lysa inquiet "Doucement ! Tu vas faire tomber quelque chose."
            noam neutre "Ouais, attends."
            "Je regarde les attaches. La plaque est posée sur des supports, pas vissée comme les protections habituelles."
            jump _28_0_1_1_0_1_PLAQUE

label _28_0_1_1_0_1_PLAQUE:
    $ j28a_plaque = True
    "Je photographie le montage. La plaque détourne la circulation de l'air vers un passage qui débouche près de la chambre d'Elen."
    noam reflexion "Lysa, tu peux m'aider à la faire glisser ?"
    lysa raison "Oui. Mais pas comme un bourrin. Un... deux... trois."
    play sound "audio/sfx_duct_scrape.wav"
    with hpunch
    "La plaque bouge de quelques centimètres. Derrière, il y a un renfoncement sombre."
    lysa inquiet "Il y a quelque chose là-dedans."
    "Je dirige la lampe vers le fond. Un petit récipient noirci est posé sur une surface métallique. Il contient des résidus brûlés et des fragments qui ressemblent à des feuilles."
    noam surpris "C'est quoi, ce truc ?"
    lysa reflexion "On dirait un bol. Mais qu'est-ce qu'il fout là ?"
    noam raison "Je prends des photos. On touche à rien."
    $ j28a_bol = True
    "Je photographie le récipient, le renfoncement et les alentours, puis je rappelle Iris."
    noam raison "On a trouvé un bol avec quelque chose de brûlé dedans. La plaque était juste devant."
    iris "OK. Surtout, ne remuez pas les cendres. Ça peut encore être dangereux."
    lysa fatigue "Super. J'adore cette sortie."
    iris "Vous avez des gants et un sachet. Si vous pouvez récupérer un fragment sans soulever de poussière, faites-le. Sinon, laissez tout."
    "Je prélève avec une pince un fragment déjà détaché, puis je referme le sachet. Le reste ne bouge pas."
    noam reflexion "Iris, si quelque chose brûlait ici, ça aurait pu passer dans la chambre ?"
    iris "Avec une plaque qui dirige l'air dans cette direction, peut-être. Mais il faut que je voie les photos."
    lysa inquiet "Quelqu'un aurait pu placer tout ça depuis la maintenance..."
    noam neutre "Ouais. Sans jamais ouvrir la porte."
    iris "Revenez. Maintenant."
    "Je jette un dernier regard au bol. C'est la première fois que je vois quelque chose qui ne ressemble pas à un simple accident."
    $ flashlight_off()
    scene couloir_maintenance at adaptive_fullscreen with dissolve
    stop music fadeout 0.7
    $ showGroup([("lysa", "fatigue", 0.37), ("noam", "inquiet", 0.66)])
    lysa fatigue "J'ai de la poussière partout. Je veux une douche."
    noam fatigue "Moi aussi."
    lysa reflexion "Tu crois que c'est à cause de ça que Tomas est mort ?"
    noam neutre "Je sais pas. Mais cette plaque n'avait rien à faire là."
    $ hideGroup()
    jump _28_0_1_1_0_1_ANALYSE
# Durée : environ 4 minutes pour la traversée.

label _28_0_1_1_0_1_ANALYSE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j28a_door_3
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Iris examine les photos du conduit. Elle garde le sachet fermé et agrandit l'image du fragment sur son écran."
    $ showGroup([("iris", "reflexion", 0.22), ("lysa", "neutre", 0.46), ("noam", "inquiet", 0.70)])
    iris reflexion "La plaque n'a pas été installée comme les protections habituelles. Et le récipient est bien derrière."
    noam neutre "On dirait qu'il a brûlé quelque chose."
    iris raison "Oui. Un matériau organique, au moins en partie."
    lysa reflexion "Tu reconnais la plante ?"
    "Iris cherche dans une bibliothèque d'images, puis s'arrête sur une fiche botanique."
    iris surpris "Attendez. Ça ressemble beaucoup à du Bulbuma Corienis."
    noam reflexion "Du quoi ?"
    iris raison "Bulbuma Corienis. C'est une plante assez rare. Elle pousse surtout dans des régions arides."
    lysa inquiet "Et c'est dangereux ?"
    iris neutre "Selon la préparation, certains composants peuvent dégager des substances toxiques quand on les chauffe. Je veux confirmer l'espèce avant de dire que c'est ce qu'on a ici."
    noam raison "Ça pourrait expliquer comment Tomas est mort ?"
    iris reflexion "Une intoxication par inhalation pourrait expliquer une partie de ce qu'on a vu. Mais ça ne démontre pas qu'il a inhalé ce mélange-là."
    lysa raison "Et les maux de tête qu'on a eus en ouvrant la chambre ?"
    iris neutre "Ça peut correspondre à une exposition, oui. Mais il y avait aussi des déchets et une odeur très forte. Je peux pas en déduire davantage."
    noam reflexion "Donc on a un bol brûlé, une plaque pas normale et une mort qui ressemble à une intoxication..."
    iris raison "Ce sont des éléments qui rendent l'hypothèse d'un meurtre beaucoup plus sérieuse. Pas une preuve définitive."
    lysa reflexion "Et le flacon de somnifères, alors ?"
    iris fatigue "Toujours le même problème : on sait pas ce qu'il a pris. Si quelqu'un a mis ce flacon pour nous tromper, c'est une autre possibilité."
    noam neutre "Au moins, la porte fermée ne règle plus rien."
    iris raison "C'est ça. Un verrou fermé n'empêche pas quelqu'un d'agir depuis les conduits."
    pause 0.3
    noam fatigue "Putain, Tomas..."
    lysa reflexion "Tu disais que la plante poussait dans les endroits arides ?"
    iris raison "Oui."
    lysa neutre "Ça fait penser à Limen."
    noam reflexion "À Ryn et Sael."
    iris agace "Pas seulement. Orbite a aussi des territoires arides. Et les livraisons circulent entre districts."
    noam raison "Donc Kael et Nyra aussi."
    iris neutre "Et ça ne prouve rien contre aucun des quatre. L'origine d'une plante ne te dit pas qui l'a apportée ici."
    lysa raison "On sait. Mais ça fait au moins des gens à qui demander."
    iris reflexion "Demandez ce qu'ils connaissent, pas s'ils ont tué Tomas."
    noam sourire "J'essaierai."
    iris agace "Noam..."
    noam neutre "Je plaisante."
    $ j28a_bulbuma = True
    "Je conserve les photos de la plaque et du récipient sur ma tablette. Le sachet reste à l'infirmerie."
    $ hideGroup()
    jump _28_0_1_1_0_1_TEMOINS
# Durée : environ 3 minutes.

label _28_0_1_1_0_1_TEMOINS:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Je montre à Lysa les questions que j'ai notées."
    $ showGroup([("lysa", "blase", 0.38), ("noam", "neutre", 0.68)])
    lysa reflexion "Tu vas leur demander s'ils connaissent la plante ?"
    noam raison "Oui. On essaie de comprendre d'où elle vient."
    lysa blase "OK. Mais si tu commences avec « pourquoi t'as tué Tomas », je te laisse seul."
    noam sourire "Promis."
    $ hideGroup()
    menu:
        "À qui parler en premier ?"
        "Sael et Ryn":
            call _28_0_1_1_0_1_SAEL_RYN from _call_j28a_sael_first
            call _28_0_1_1_0_1_KAEL from _call_j28a_kael_second
            jump _28_0_1_1_0_1_NYRA
        "Kael":
            call _28_0_1_1_0_1_KAEL from _call_j28a_kael_first
            call _28_0_1_1_0_1_SAEL_RYN from _call_j28a_sael_second
            jump _28_0_1_1_0_1_NYRA

label _28_0_1_1_0_1_SAEL_RYN:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.17), ("ryn", "fatigue", 0.37), ("lysa", "neutre", 0.57), ("noam", "neutre", 0.77)])
    ryn fatigue "Qu'est-ce qu'il y a, encore ?"
    noam raison "On a trouvé quelque chose dans un conduit. Je voulais savoir si vous connaissez une plante : Bulbuma Corienis."
    sael reflexion "J'en ai entendu parler. On en trouve dans certaines régions de Limen."
    ryn reflexion "C'est celle qui pousse dans le désert ?"
    sael neutre "Il y a plusieurs espèces. Pourquoi ?"
    lysa raison "Des restes de plante brûlée, dans un bol. Près de la ventilation d'Elen."
    sael inquiet "Et vous pensez que ça pourrait avoir un rapport avec la mort de Tomas ?"
    noam neutre "Iris dit que c'est possible, oui."
    ryn colere "Ah. Donc parce qu'on vient de Limen, c'est nous maintenant ?"
    noam agace "Mais j'ai pas dit ça !"
    ryn colere "Vous arrivez avec une plante du désert et vous nous regardez tous les deux !"
    lysa blase "On va aussi parler à Kael. Calme-toi."
    ryn fatigue "Ouais, c'est ça..."
    sael raison "Ryn, laisse-le finir."
    noam reflexion "Sael, tu sais ce qui se passe quand on brûle cette plante ?"
    sael neutre "Certaines préparations sont irritantes. Je n'en ai jamais utilisé, alors je ne vais pas inventer."
    noam neutre "Tu en as déjà vu ici ?"
    sael neutre "Non. Pas à ma connaissance."
    ryn colere "Et moi non plus, d'accord ? J'ai même jamais touché à cette plante."
    noam raison "D'accord."
    sael reflexion "Vous avez trouvé comment le bol a été placé ?"
    noam neutre "Pas encore. Mais la plaque qu'on a trouvée ne vient pas des protections habituelles."
    sael raison "Alors c'est peut-être ça qu'il faut comprendre en priorité."
    $ hideGroup()
    return

label _28_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.24), ("lysa", "neutre", 0.46), ("noam", "neutre", 0.69)])
    noam raison "Tu peux regarder ces photos ? On a trouvé une plaque dans le réseau."
    kael surpris "Attends... C'est quoi, ça ?"
    lysa neutre "On espérait que tu nous le dirais."
    kael reflexion "C'est pas une des plaques qu'on a installées. Nous, on a protégé les grilles, pas mis des obstacles à l'intérieur."
    noam reflexion "Elle redirigeait l'air vers la chambre d'Elen."
    kael raison "Ça en a l'air. Il faudrait voir sur place pour être sûr."
    noam raison "On peut poser cette plaque depuis un accès de maintenance ?"
    kael neutre "Oui. Les branches sont reliées."
    lysa reflexion "Donc pas besoin d'ouvrir la porte de la chambre."
    kael raison "Non, pas pour accéder à cette partie du réseau."
    noam neutre "Et le Bulbuma Corienis ? Tu connais ?"
    kael reflexion "De nom. On trouve des plantes du même genre dans certains secteurs d'Orbite, mais je suis pas botaniste."
    lysa blase "Ça, on avait remarqué."
    kael sourire "Je préfère les moteurs."
    noam raison "Tu peux vérifier les accès de maintenance ?"
    kael neutre "Je regarderai les journaux, mais il y a du passage. Je promets rien."
    noam neutre "Merci."
    $ hideGroup()
    return
