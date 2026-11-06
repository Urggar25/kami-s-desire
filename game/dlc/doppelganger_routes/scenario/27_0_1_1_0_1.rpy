# JOUR 27 — LES DERNIÈRES RECHERCHES
# Route de Tomas — uniquement les observations de Noam.
default j27a_yanma = False
default j27a_eid = False
default j27a_notes = False
default j27a_chambre = False
default j27a_iris = False
default j27a_kael = False
default j27a_sael = False
default j27a_appareil_absent = False

label _27_0_1_1_0_1_REVEIL:
    $ current_day = 27
    $ day_id = 27
    $ current_period = "Matin"
    $ j27a_yanma = False
    $ j27a_eid = False
    $ j27a_notes = False
    $ j27a_chambre = False
    $ j27a_iris = False
    $ j27a_kael = False
    $ j27a_sael = False
    $ j27a_appareil_absent = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille avec le rappel du vote du jour 27 sur ma tablette."
    "J'avais oublié de le désactiver. Après ce qui s'est passé hier, la dernière chose que je veux, c'est retourner voter."
    "Je fais défiler mes notes : le flacon de somnifères, les draps trempés, le verrou intérieur, les témoignages..."
    think "J'ai tout écrit. Et j'ai toujours aucune idée de ce qui lui est arrivé."
    "Je me rappelle Tomas devant ses cartes, dans la salle d'observation. Il avait passé sa dernière journée à chercher Keyper."
    noam fatigue "Bon. On va regarder ce qu'il a laissé."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j27a_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _27_0_1_1_0_1_CAFETERIA
# Durée : ~1m00.

label _27_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j27a_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Il reste plusieurs places libres. Celle de Tomas me saute aux yeux."
    $ showGroup([("elen", "triste", 0.16), ("julian", "fatigue", 0.34), ("iris", "fatigue", 0.52), ("nyra", "neutre", 0.70), ("noam", "neutre", 0.88), ("lysa", "blase", 1.06)])
    julian reflexion "Iris, pour les analyses... T'as pu avancer ?"
    iris fatigue "Pas assez pour donner une cause de décès. On en a déjà parlé."
    elen inquiet "Et les médicaments ?"
    iris raison "On sait pas ce qu'il a pris. Je veux pas conclure à une surdose juste à cause d'un flacon."
    julian fatigue "Personne a dit qu'on devait conclure."
    lysa blase "C'est vrai. Pas aujourd'hui."
    noam neutre "Elen, je peux te demander un truc ?"
    elen neutre "Bien sûr."
    noam reflexion "Tu as dormi dans la chambre de Tomas. Je voudrais y retourner pour regarder ses notes. Il cherchait encore Keyper la veille."
    elen inquiet "Tu crois que tu vas trouver quelque chose ?"
    noam fatigue "Franchement, j'en sais rien. Mais je veux pas m'arrêter au flacon."
    elen neutre "Vas-y. J'ai rien déplacé là-bas à part les draps."
    nyra raison "Je peux t'accompagner, Noam. On prendra des photos de ce qu'on trouve."
    noam sourire "Merci."
    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonjour ! Aujourd'hui, c'est le jour du vote ! Enfin, ça aurait dû l'être."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais vous avez décidé de bouder tous ensemble. Comme c'est touchant !"
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Faute de participants, aucun nouveau Commandement ne sera adopté aujourd'hui. Je précise que cela ne suspend aucune de mes règles."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je vous souhaite une excellente petite journée de repos. Essayez de ne pas trop vous ennuyer sans moi !"
    hide screen kami_broadcast_ui
    stop music fadeout 0.6
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "triste", 0.33), ("nyra", "neutre", 0.55), ("noam", "fatigue", 0.77)])
    elen fatigue "Elle pourrait au moins nous laisser tranquilles."
    nyra neutre "On y va ?"
    noam neutre "Ouais."
    $ hideGroup()
    jump _27_0_1_1_0_1_CHAMBRE
# Durée : ~2m30.

label _27_0_1_1_0_1_CHAMBRE:
    $ current_period = "Après-midi"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "On passe devant la chambre d'Elen. Je ralentis sans le vouloir, puis je continue."
    "Nous entrons dans celle de Tomas avec l'accès qu'Elen nous a prêté."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Les livres sont alignés. Les vêtements sont pliés. Il a même une pile de documents parfaitement droite sur le bureau."
    $ showGroup([("nyra", "neutre", 0.37), ("noam", "reflexion", 0.68)])
    noam reflexion "Tomas, quoi..."
    nyra sourire "On dirait qu'il va revenir dans deux minutes pour vérifier qu'on range bien."
    noam fatigue "Ouais."
    nyra raison "On examine ce qui concerne ses recherches, on photographie et on remet tout ?"
    noam neutre "C'est ça."
    $ hideGroup()
    jump _27_0_1_1_0_1_FOUILLE
# Durée : ~1m00.

label _27_0_1_1_0_1_FOUILLE:
    menu:
        "Que regarder ?"
        "Les livres techniques" if not j27a_yanma:
            $ j27a_yanma = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Un livre dépasse de l'étagère. Plusieurs pages sont marquées."
            noam reflexion "« Résonance Yanma — Transmissions à très faible intensité ». Ça te parle ?"
            nyra reflexion "De nom. C'est une méthode de transmission dans l'espace."
            noam neutre "Comment ça marche ?"
            nyra raison "On envoie des signaux très faibles. Difficiles à détecter sans un récepteur adapté. Mais je connais pas tous les détails."
            noam surpris "Pourquoi Tomas lisait ça ?"
            nyra neutre "Il cherchait des coordonnées orbitales. Peut-être qu'il a voulu comprendre un système."
            noam raison "Je prends une photo du livre."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Le registre de Keyper" if not j27a_eid:
            $ j27a_eid = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Je retrouve les relevés du jour 24, rangés avec un registre de production plus ancien."
            noam reflexion "Voilà. Keyper-IIB."
            "Une ligne indique « UNITÉS ÉID-0 — EFFECTIFS », suivie de chiffres. Plus bas, des quotas de production."
            noam surpris "Des effectifs ? On dirait qu'ils comptent des employés."
            nyra raison "Ou des machines. Certains services utilisent aussi ce mot pour des unités automatisées."
            noam neutre "Et ici, il y a les quotas qu'on devait augmenter."
            "Tomas a écrit dans la marge : « ÉID-0 = personnes ? machines ? »"
            nyra neutre "Il n'avait pas encore la réponse."
            noam fatigue "Non. Mais il a voté contre à cause de ça."
            "Je garde une copie du registre."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Ses notes de transport" if not j27a_notes:
            $ j27a_notes = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "neutre", 0.67)])
            "Les dernières feuilles contiennent des références orbitales et un tracé de trajet."
            noam reflexion "C'est ce qu'il m'avait montré. Keyper serait à quelques heures de vol."
            nyra raison "Si ses calculs sont bons. Il a entouré plusieurs positions possibles."
            noam neutre "Il avait encore des trucs à vérifier."
            nyra reflexion "Oui. On peut photographier ça aussi."
            "Je remarque trois questions sous le trajet : « Pourquoi station non déclarée ? », « Quels effectifs ? », « Accès aux quotas ? »"
            noam fatigue "Il a passé toute la journée là-dessus."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "La porte et les accès" if not j27a_chambre:
            $ j27a_chambre = True
            $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.67)])
            "Je regarde le verrou et la grille d'aération. Rien ne semble avoir bougé."
            noam reflexion "Elen a dormi ici. Et Tomas s'est retrouvé dans sa chambre à elle."
            nyra neutre "Oui. On sait juste qu'ils ont échangé la veille."
            noam raison "Il faudrait vérifier qui connaissait l'échange, exactement."
            nyra reflexion "On pourra reprendre les témoignages. Mais ne mélange pas les suppositions avec ce qu'on sait."
            noam neutre "Ouais."
            $ hideGroup()
            jump _27_0_1_1_0_1_FOUILLE
        "Terminer la fouille" if j27a_yanma and j27a_eid and j27a_notes and j27a_chambre:
            jump _27_0_1_1_0_1_APPAREIL
# Durée : ~3m30.

label _27_0_1_1_0_1_APPAREIL:
    $ showGroup([("nyra", "reflexion", 0.38), ("noam", "neutre", 0.68)])
    noam reflexion "Attends. Ce livre sur Yanma me rappelle quelque chose."
    nyra neutre "Quoi ?"
    noam raison "Dans la salle d'observation, il tenait un petit appareil métallique. Il l'a posé quand je suis arrivé. Il y avait un voyant dessus."
    nyra surpris "Tu sais à quoi il servait ?"
    noam neutre "Non. Lui non plus, d'après ce qu'il m'a dit."
    nyra raison "Ça peut être une balise, un capteur, un boîtier de maintenance... Mais ça vaut le coup d'aller voir."
    noam sourire "On y va."
    $ hideGroup()
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_j27a_door_3
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "reflexion", 0.68)])
    noam raison "C'était là, près du pupitre."
    "Je regarde le dessus du meuble, puis les compartiments. L'appareil n'y est plus."
    noam surpris "Il a disparu."
    nyra reflexion "T'es sûr de l'endroit ?"
    noam agace "Oui ! Je l'ai vu le poser."
    $ j27a_appareil_absent = True
    nyra raison "Il a pu être rangé. Kael et Elias viennent ici pour le matériel."
    noam reflexion "Mais pourquoi celui-là ?"
    nyra neutre "Je sais pas. On peut leur demander."
    noam raison "Si c'était un émetteur Yanma, tu saurais le reconnaître ?"
    nyra reflexion "Pas à partir d'un voyant. Et sans l'appareil, encore moins."
    noam fatigue "J'aurais dû le prendre en photo."
    nyra sourire "Tu pouvais pas prévoir qu'on reviendrait chercher ce truc."
    "Je regarde encore une fois le meuble vide. Il y a deux jours, je me fichais complètement de cet objet."
    $ hideGroup()
    jump _27_0_1_1_0_1_QUESTIONS
# Durée : ~2m30.

label _27_0_1_1_0_1_QUESTIONS:
    scene bg_repos at adaptive_fullscreen with dissolve
    "Nyra part chercher à manger pendant que je pose quelques questions aux autres."
    menu:
        "À qui parler ?"
        "À Kael" if not j27a_kael:
            $ j27a_kael = True
            call _27_0_1_1_0_1_KAEL from _call_j27a_kael
            jump _27_0_1_1_0_1_QUESTIONS
        "À Sael et Ryn" if not j27a_sael:
            $ j27a_sael = True
            call _27_0_1_1_0_1_SAEL from _call_j27a_sael
            jump _27_0_1_1_0_1_QUESTIONS
        "À Iris" if not j27a_iris:
            $ j27a_iris = True
            call _27_0_1_1_0_1_IRIS from _call_j27a_iris
            jump _27_0_1_1_0_1_QUESTIONS
        "Rejoindre Nyra" if j27a_kael and j27a_sael and j27a_iris:
            jump _27_0_1_1_0_1_NYRA

label _27_0_1_1_0_1_KAEL:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "calme", 0.38), ("noam", "neutre", 0.68)])
    noam raison "Tu connais la résonance Yanma ?"
    kael reflexion "Un peu. C'est des transmissions très faibles, non ?"
    noam neutre "Tomas avait un livre dessus. Et je l'ai vu avec un appareil dans la salle d'observation."
    kael reflexion "Quel appareil ?"
    noam raison "Une boîte métallique. Un voyant. Petit format."
    kael fatigue "Noam... Tu me décris la moitié des appareils du Conclave."
    noam agace "Ouais, je sais."
    kael neutre "Je dis pas ça pour me foutre de toi. Mais je peux pas reconnaître un modèle comme ça."
    noam reflexion "Tu l'as déplacé récemment ?"
    kael neutre "Non. Elias range parfois les équipements là-bas, tu peux lui demander."
    noam raison "Et ÉID-0, ça te parle ?"
    kael reflexion "Non. Ça ressemble à un code interne de Kami."
    noam fatigue "OK. Merci."
    $ hideGroup()
    return

label _27_0_1_1_0_1_SAEL:
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("sael", "neutre", 0.21), ("ryn", "fatigue", 0.46), ("noam", "neutre", 0.70)])
    noam neutre "Tomas avait un registre sur Keyper-IIB. Vous connaissez ces unités ÉID-0 ?"
    ryn reflexion "C'est quoi, encore, ce truc ?"
    noam raison "Je sais pas. Des effectifs. Des quotas."
    sael reflexion "Je ne connais pas cette désignation."
    ryn agace "Et c'est toujours ça qui l'a poussé à voter contre ?"
    noam fatigue "Oui."
    ryn colere "Putain. Tout ça, et maintenant il est mort..."
    sael neutre "Ryn, ça suffit."
    ryn fatigue "Je sais. Pardon."
    noam reflexion "Vous pensez que Kami nous laisserait accéder aux dossiers ?"
    sael raison "Elle a déjà refusé. Mais tu peux demander."
    noam neutre "Ouais."
    $ hideGroup()
    return

label _27_0_1_1_0_1_IRIS:
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    $ showGroup([("iris", "fatigue", 0.37), ("noam", "neutre", 0.68)])
    iris fatigue "Si tu viens pour les résultats de Tomas, j'ai rien de plus."
    noam raison "Non. Regarde ce registre."
    "Je lui tends la copie. Elle s'arrête au milieu de la page."
    iris surpris "Attends... Où t'as trouvé ça ?"
    noam reflexion "Dans sa chambre. Pourquoi ?"
    iris reflexion "ÉID-0... Ça vient de quel service ?"
    noam neutre "Du registre de Keyper. Tu connais ?"
    iris hesitation "Je sais pas. J'ai l'impression d'avoir vu un code du genre dans un document technique."
    noam surpris "Quel document ?"
    iris fatigue "J'en sais rien ! Je viens de passer la nuit sur des dossiers médicaux, Noam."
    noam agace "Tu m'as quand même demandé où je l'avais trouvé."
    iris agace "Parce que c'est bizarre, cette histoire d'effectifs ! Mais je sais pas ce que c'est. J'essaie de me rappeler !"
    pause 0.3
    iris fatigue "Pardon. J'ai pas dormi."
    noam neutre "C'est bon."
    iris raison "Laisse-moi la copie. Je vais regarder si le code apparaît quelque part."
    noam reflexion "Tu crois qu'il y a un lien avec ce que j'ai vu dans la maintenance ? Avec Mara ?"
    iris inquiet "Noam... On y est retournés ensemble. Le corps n'y était plus."
    noam fatigue "Je sais."
    iris raison "Je dis pas que t'as tout inventé. Mais là, avec Tomas, on a vraiment un corps. C'est pas la même chose."
    noam neutre "Ouais."
    iris fatigue "Je t'appellerai si je trouve quelque chose. Maintenant, va manger."
    $ hideGroup()
    return

label _27_0_1_1_0_1_NYRA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Je retrouve Nyra. Elle m'a gardé un plateau."
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "fatigue", 0.68)])
    nyra sourire "Tu m'as dit que t'avais pas mangé. Alors mange."
    noam sourire "Merci. T'es la troisième personne à me le dire."
    nyra reflexion "Alors, ils ont dit quoi ?"
    noam raison "Kael connaît Yanma, mais il peut pas reconnaître l'appareil. Et personne sait ce que sont les unités ÉID-0."
    nyra neutre "Même Iris ?"
    noam reflexion "Elle a réagi bizarrement. Elle croit avoir déjà vu une nomenclature similaire."
    nyra raison "Ça vaut peut-être le coup de chercher de ce côté-là. Si on comprend ce que Tomas cherchait, on comprendra au moins pourquoi il a voté contre."
    noam neutre "Mais pas forcément pourquoi il est mort."
    nyra reflexion "Non, pas forcément."
    noam raison "J'ai toujours l'appareil en tête."
    nyra neutre "On y reviendra. Pour l'instant, on sait même pas ce que c'était. Je voudrais éviter qu'on accuse quelqu'un juste pour ça."
    noam fatigue "Ouais. T'as raison."
    nyra sourire "On peut faire deux dossiers. Keyper et ses unités d'un côté ; la mort de Tomas de l'autre. Si ça se recoupe, on le verra."
    noam neutre "Ça me va."
    "Je m'assois à côté d'elle et on trie mes notes pendant que je mange."
    $ hideGroup()
    jump _27_0_1_1_0_1_REUNION
# Durée : ~2m00.

label _27_0_1_1_0_1_REUNION:
    $ current_period = "Soir"
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    "On se réunit autour de la table. La place de Tomas est toujours vide."
    $ showGroup([("julian", "fatigue", 0.15), ("elen", "triste", 0.32), ("iris", "fatigue", 0.49), ("lysa", "neutre", 0.66), ("nyra", "neutre", 0.83), ("noam", "neutre", 1.00)])
    julian reflexion "On peut au moins faire le point ?"
    elen inquiet "Iris a dit qu'elle avait pas encore la cause."
    julian neutre "Je sais. Mais on va pas juste attendre sans rien faire."
    elen colere "Et tu veux qu'on dise qu'il s'est suicidé ?!"
    julian colere "J'ai pas dit ça !"
    lysa blase "C'est reparti..."
    iris agace "Stop. On n'a toujours pas de preuve qu'il a pris ces comprimés. Et on n'a pas de preuve qu'on l'a tué non plus."
    julian fatigue "D'accord."
    noam raison "J'ai trouvé les documents de Tomas. Sur Keyper-IIB et les unités ÉID-0."
    elen reflexion "Ça nous dit ce que c'est ?"
    noam fatigue "Non. Il y a des effectifs et des quotas. Et Tomas avait localisé la station à quelques heures de vol."
    noam raison "Il y avait aussi un livre sur la résonance Yanma. C'est une méthode de transmission dans l'espace."
    julian reflexion "Quel rapport avec sa mort ?"
    noam neutre "J'en sais rien. Mais il avait un petit appareil dans la salle d'observation, le jour 25. Aujourd'hui, cet appareil avait disparu."
    lysa surpris "Disparu ?"
    nyra raison "On a vérifié. Il a pu être déplacé par quelqu'un de la maintenance. On sait pas ce que c'était."
    elen triste "Donc on sait toujours pas..."
    noam neutre "Pas encore."
    iris raison "Continuez à chercher. Moi je poursuis les examens. Mais arrêtez de tirer des conclusions avec une moitié d'indice."
    julian fatigue "Je peux avoir une copie des documents ?"
    noam surpris "Oui. Bien sûr."
    julian neutre "Merci."
    "Pour une fois, la réunion se termine sans que quelqu'un sorte en claquant la porte."
    $ hideGroup()
    jump _27_0_1_1_0_1_NUIT
# Durée : ~2m30.

label _27_0_1_1_0_1_NUIT:
    $ current_period = "Nuit"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "Je relis les notes de Tomas. Keyper-IIB, les effectifs des unités ÉID-0, les trajets orbitaux, le livre sur Yanma."
    "J'avais espéré comprendre pourquoi il était mort. À la place, j'ai surtout découvert à quel point il cherchait encore."
    think "Et cet appareil qu'il examinait..."
    "Je n'ai pas de photo. Aucun numéro de série. Juste un souvenir d'une petite boîte métallique et d'un voyant."
    noam fatigue "Merde, Tomas..."
    "Demain, je voudrais retourner voir cette chambre où on l'a trouvé. Il reste peut-être quelque chose qu'on a raté."
    "Je pose ma tablette et ferme les yeux."
    stop music fadeout 1.0
    call end_day("28", sleeping=True) from _call_j27a_end_day_28
    jump _28_0_1_1_0_1_REVEIL
# Durée : ~1m00.
