# Scènes bonus indépendantes du scénario et sans modification de la progression.
# Appelées depuis la tablette avec renpy.call_in_new_context.
# Aucune variable de route n'est altérée ; les dialogues peuvent être rejoués.

label bonus_succes001:
    scene black with dissolve
    centered "{size=38}BONUS — UNE DRÔLE DE SENSATION{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Je suis toujours devant cette fichue porte, les doigts posés sur mon cou. J'ai beau inspirer profondément, la brûlure que je viens de ressentir refuse de disparaître complètement."

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "neutre", 0.58), ("sael", "neutre", 0.96)])
    noam inquiet "Je vous jure que pendant une seconde, j'ai eu l'impression que quelque chose me serrait la gorge. Et le plus bizarre, c'est que juste avant de paniquer, j'ai senti une sorte de... Je sais pas comment expliquer ça."

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "taquin", 0.58), ("sael", "neutre", 0.96)])
    mara taquin "D'excitation ?"

    $ showGroup([("noam", "surpris", 0.18), ("mara", "taquin", 0.58), ("sael", "neutre", 0.96)])
    noam surpris "Quoi ?! Non ! Enfin, pas comme ça ! Pourquoi tu me regardes avec ce sourire ?"

    $ showGroup([("noam", "surpris", 0.18), ("mara", "rire", 0.58), ("sael", "neutre", 0.96)])
    mara rire "Parce que tu viens de décrire une expérience franchement terrifiante en ayant presque l'air déçu qu'elle soit terminée. Excuse-moi, mais c'est difficile de ne pas poser la question."

    $ showGroup([("noam", "colere", 0.18), ("mara", "rire", 0.58), ("sael", "neutre", 0.96)])
    noam colere "J'ai cru mourir, Mara ! Je crois que ça mérite un peu mieux qu'une blague."

    $ showGroup([("noam", "colere", 0.18), ("mara", "rire", 0.58), ("sael", "inquiet", 0.96)])
    sael inquiet "Attends, tu peux répéter ce que tu viens de dire ? Tu as ressenti quelque chose d'agréable au moment où tu ne pouvais plus respirer ?"

    $ showGroup([("noam", "hesitation", 0.18), ("mara", "rire", 0.58), ("sael", "inquiet", 0.96)])
    noam hesitation "Agréable, non... Enfin, c'était surtout étrange. Mon cœur battait tellement fort que j'ai eu une espèce de vertige, puis tout s'est arrêté. Je sais même pas si ce que je raconte a du sens."

    $ showGroup([("noam", "hesitation", 0.18), ("mara", "rire", 0.58), ("sael", "determine", 0.96)])
    sael determine "Ça en a, mais il faut surtout que tu ne cherches pas à reproduire cette sensation. Le manque d'oxygène et la pression sur le cou peuvent provoquer des lésions graves ou une perte de connaissance, parfois sans laisser le temps de comprendre ce qui arrive."

    $ showGroup([("noam", "hesitation", 0.18), ("mara", "reflexion", 0.58), ("sael", "determine", 0.96)])
    mara reflexion "Voilà qui gâche un peu ma théorie sur tes loisirs, mais j'avoue que je préfère te voir respirer normalement."

    $ showGroup([("noam", "blase", 0.18), ("mara", "reflexion", 0.58), ("sael", "determine", 0.96)])
    noam blase "Je suis ravi de découvrir qu'on partage au moins cette passion."

    $ showGroup([("noam", "blase", 0.18), ("mara", "taquin", 0.58), ("sael", "determine", 0.96)])
    mara taquin "Oh, ne sois pas si susceptible. J'allais justement proposer une activité beaucoup moins dangereuse pour apprendre à se connaître."

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "taquin", 0.58), ("sael", "determine", 0.96)])
    noam inquiet "Laquelle ?"

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "rire", 0.58), ("sael", "determine", 0.96)])
    mara rire "On reste assis cinq minutes sans toucher à aucune porte."

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "rire", 0.58), ("sael", "sourire", 0.96)])
    sael sourire "Pour une fois, je suis entièrement d'accord avec elle."

    $ showGroup([("noam", "inquiet", 0.18), ("mara", "rire", 0.58), ("sael", "sourire", 0.96)])
    noam inquiet "Vous savez quoi ? J'aurais dû commencer par là."

    "Je m'éloigne enfin du capteur, encore un peu tremblant. Mara conserve son sourire, mais elle attend que j'aie repris mon souffle avant de retourner à sa place."

    $ hideGroup()
    scene black with dissolve
    return

label bonus_succes005:
    scene black with dissolve
    centered "{size=38}BONUS — LES PREMIÈRES IMPRESSIONS{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Une conversation qui aurait très bien pu avoir lieu pendant notre première attente dans la salle du Conclave."
    $ showGroup([("ryn", "neutre", -0.08), ("iris", "neutre", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "neutre", 1.06)])
    mara taquin "Bon, on a trente jours à passer ensemble. Je propose qu'on établisse tout de suite qui, ici, est le plus pénible."
    $ showGroup([("ryn", "neutre", -0.08), ("iris", "neutre", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "neutre", 1.06)])
    noam neutre "C'est un concours ou tu viens directement réclamer ton trophée ?"
    $ showGroup([("ryn", "neutre", -0.08), ("iris", "neutre", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "neutre", 1.06)])
    mara rire "Oh, il a du répondant ! Je lui donne une semaine avant de craquer."
    $ showGroup([("ryn", "neutre", -0.08), ("iris", "blase", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "neutre", 1.06)])
    iris blase "Moi, je lui donne dix minutes avant de vous demander de vous taire tous les deux."
    $ showGroup([("ryn", "neutre", -0.08), ("iris", "blase", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "joie", 1.06)])
    elen joie "Attendez, on pourrait faire un vrai vote ! Chacun écrit un nom sur un papier, et celui qui gagne doit faire la vaisselle."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "blase", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "joie", 1.06)])
    ryn colere "C'est pas parce qu'on est coincés ici qu'il faut transformer chaque conversation en réunion."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "blase", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "joie", 1.06)])
    noam neutre "Merci, Ryn, pour cette intervention qui prouve qu'on n'a pas besoin de voter pour se disputer."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "blase", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "joie", 1.06)])
    mara taquin "Je change mon choix. C'est lui, le plus pénible."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "taquin", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "joie", 1.06)])
    iris taquin "Pour une fois, je suis d'accord avec elle."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "taquin", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "joie", 1.06)])
    elen joie "Eh, c'est historique ! Vous venez de tomber d'accord sur quelque chose !"
    $ showGroup([("ryn", "colere", -0.08), ("iris", "taquin", 0.17), ("noam", "neutre", 0.43), ("mara", "taquin", 0.73), ("elen", "joie", 1.06)])
    noam neutre "Génial. Notre première unanimité porte sur ma tête."
    $ showGroup([("ryn", "colere", -0.08), ("iris", "taquin", 0.17), ("noam", "neutre", 0.43), ("mara", "rire", 0.73), ("elen", "joie", 1.06)])
    mara rire "Tu vois ? On va très bien s'entendre."
    "Le pire, c'est que pendant quelques secondes, je crois presque qu'elle a raison."
    $ hideGroup()
    scene black with dissolve
    return

label bonus_succes006:
    scene black with dissolve
    centered "{size=38}BONUS — VISITE GUIDÉE, OU PRESQUE{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Je repense à ce qu'Elias et Kael auraient pu me dire si j'avais demandé une visite commentée."
    $ showGroup([("elias", "neutre", 0.17), ("noam", "neutre", 0.52), ("kael", "neutre", 0.87)])
    elias neutre "La station est plutôt bien pensée. Le problème, c'est que tout ce qui est bien pensé finit par tomber en panne quand quelqu'un oublie une vis."
    $ showGroup([("elias", "neutre", 0.17), ("noam", "neutre", 0.52), ("kael", "neutre", 0.87)])
    noam neutre "C'est censé me rassurer ?"
    $ showGroup([("elias", "neutre", 0.17), ("noam", "neutre", 0.52), ("kael", "raison", 0.87)])
    kael raison "Il exagère. Les systèmes critiques ont normalement plusieurs sécurités indépendantes."
    $ showGroup([("elias", "taquin", 0.17), ("noam", "neutre", 0.52), ("kael", "raison", 0.87)])
    elias taquin "Normalement, oui. C'est précisément le mot qui m'inquiète."
    $ showGroup([("elias", "taquin", 0.17), ("noam", "neutre", 0.52), ("kael", "raison", 0.87)])
    noam neutre "Et la cafétéria ? Dis-moi au moins que la nourriture ne dépend pas d'une vis."
    $ showGroup([("elias", "sourire", 0.17), ("noam", "neutre", 0.52), ("kael", "raison", 0.87)])
    elias sourire "Là, c'est pire. Ça dépend des robots."
    $ showGroup([("elias", "sourire", 0.17), ("noam", "neutre", 0.52), ("kael", "taquin", 0.87)])
    kael taquin "Les Goumi ne sont pas des assassins, Noam. Leur mission consiste à servir des repas."
    $ showGroup([("elias", "sourire", 0.17), ("noam", "neutre", 0.52), ("kael", "taquin", 0.87)])
    noam neutre "Tu dis ça comme quelqu'un qui n'a jamais goûté un plat préparé par un appareil en colère."
    $ showGroup([("elias", "rire", 0.17), ("noam", "neutre", 0.52), ("kael", "taquin", 0.87)])
    elias rire "Bon, la bonne nouvelle, c'est qu'on a une infirmerie."
    $ showGroup([("elias", "rire", 0.17), ("noam", "neutre", 0.52), ("kael", "taquin", 0.87)])
    noam neutre "Et la mauvaise ?"
    $ showGroup([("elias", "rire", 0.17), ("noam", "neutre", 0.52), ("kael", "doute", 0.87)])
    kael doute "J'imagine que c'est le fait que tu aies déjà besoin de savoir où elle est."
    $ showGroup([("elias", "rire", 0.17), ("noam", "neutre", 0.52), ("kael", "doute", 0.87)])
    noam neutre "Je sens que ces trente jours vont être interminables."
    $ hideGroup()
    scene black with dissolve
    return

label bonus_succes007:
    scene black with dissolve
    centered "{size=38}BONUS — UNE BONNE QUESTION{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Je m'imagine soumettre une dernière fois mon dossier d'arguments à Tomas et Nyra, loin du vacarme des débats."
    $ showGroup([("tomas", "reflechit", 0.16), ("noam", "neutre", 0.52), ("nyra", "neutre", 0.87)])
    tomas reflechit "Tu as vraiment noté tout ce qu'ils ont dit ? Même les remarques qui avaient l'air complètement inutiles ?"
    $ showGroup([("tomas", "reflechit", 0.16), ("noam", "neutre", 0.52), ("nyra", "neutre", 0.87)])
    noam neutre "J'ai surtout peur d'oublier celle qui fera changer quelqu'un d'avis."
    $ showGroup([("tomas", "reflechit", 0.16), ("noam", "neutre", 0.52), ("nyra", "raison", 0.87)])
    nyra raison "Alors ne confonds pas quantité et qualité. Huit bons arguments ne font pas huit personnes convaincues."
    $ showGroup([("tomas", "reflechit", 0.16), ("noam", "neutre", 0.52), ("nyra", "raison", 0.87)])
    noam neutre "Tu pourrais me laisser profiter cinq secondes de l'impression d'avoir bien travaillé ?"
    $ showGroup([("tomas", "hesitation", 0.16), ("noam", "neutre", 0.52), ("nyra", "raison", 0.87)])
    tomas hesitation "Non, mais elle a raison. Un argument peut parfaitement convaincre une personne et braquer celle qui est assise juste à côté."
    $ showGroup([("tomas", "hesitation", 0.16), ("noam", "neutre", 0.52), ("nyra", "sourire", 0.87)])
    nyra sourire "La question importante n'est pas seulement de savoir ce que tu vas dire, mais à qui tu le dis."
    $ showGroup([("tomas", "hesitation", 0.16), ("noam", "neutre", 0.52), ("nyra", "sourire", 0.87)])
    noam neutre "Donc après avoir rassemblé des fiches pendant deux jours, vous m'annoncez qu'il faut aussi réfléchir ?"
    $ showGroup([("tomas", "gene", 0.16), ("noam", "neutre", 0.52), ("nyra", "sourire", 0.87)])
    tomas gene "Présenté comme ça..."
    $ showGroup([("tomas", "gene", 0.16), ("noam", "neutre", 0.52), ("nyra", "taquin", 0.87)])
    nyra taquin "Tu peux toujours ranger ton dossier et essayer de les convaincre en improvisant."
    $ showGroup([("tomas", "gene", 0.16), ("noam", "neutre", 0.52), ("nyra", "taquin", 0.87)])
    noam neutre "Je préfère encore relire les huit fiches."
    $ showGroup([("tomas", "gene", 0.16), ("noam", "neutre", 0.52), ("nyra", "sourire", 0.87)])
    nyra sourire "Alors tu as peut-être appris quelque chose."
    $ hideGroup()
    scene black with dissolve
    return

label bonus_succes008:
    scene black with dissolve
    centered "{size=38}BONUS — LE CHRONOMÈTRE{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Cette course dans les couloirs me revient en mémoire, surtout le moment où Nyra a enfin décidé de ralentir."
    $ showGroup([("nyra", "neutre", 0.17), ("noam", "neutre", 0.52), ("tomas", "neutre", 0.87)])
    noam neutre "Tu sais que tu aurais pu prévenir avant de partir comme une fusée ?"
    $ showGroup([("nyra", "sourire", 0.17), ("noam", "neutre", 0.52), ("tomas", "neutre", 0.87)])
    nyra sourire "Je t'ai dit de courir."
    $ showGroup([("nyra", "sourire", 0.17), ("noam", "neutre", 0.52), ("tomas", "neutre", 0.87)])
    noam neutre "Oui, ça, j'avais compris. C'est la partie où j'ai failli embrasser trois murs que j'aurais aimé éviter."
    $ showGroup([("nyra", "taquin", 0.17), ("noam", "neutre", 0.52), ("tomas", "neutre", 0.87)])
    nyra taquin "Tu ne les as pas touchés. C'est le principal."
    $ showGroup([("nyra", "taquin", 0.17), ("noam", "neutre", 0.52), ("tomas", "hesitation", 0.87)])
    tomas hesitation "Moi, je trouve ça assez impressionnant que vous soyez arrivés aussi vite."
    $ showGroup([("nyra", "taquin", 0.17), ("noam", "neutre", 0.52), ("tomas", "hesitation", 0.87)])
    noam neutre "Merci, Tomas. Enfin quelqu'un qui reconnaît mes efforts."
    $ showGroup([("nyra", "raison", 0.17), ("noam", "neutre", 0.52), ("tomas", "hesitation", 0.87)])
    nyra raison "Il a surtout été porté par la panique."
    $ showGroup([("nyra", "raison", 0.17), ("noam", "neutre", 0.52), ("tomas", "hesitation", 0.87)])
    noam neutre "La panique est une excellente source d'énergie. On devrait en faire un programme d'entraînement."
    $ showGroup([("nyra", "raison", 0.17), ("noam", "neutre", 0.52), ("tomas", "gene", 0.87)])
    tomas gene "Je ne suis pas sûr que ce soit médicalement recommandé."
    $ showGroup([("nyra", "sourire", 0.17), ("noam", "neutre", 0.52), ("tomas", "gene", 0.87)])
    nyra sourire "En tout cas, la prochaine fois, je chronomètre."
    $ showGroup([("nyra", "sourire", 0.17), ("noam", "neutre", 0.52), ("tomas", "gene", 0.87)])
    noam neutre "La prochaine fois, je prends l'ascenseur."
    $ showGroup([("nyra", "taquin", 0.17), ("noam", "neutre", 0.52), ("tomas", "gene", 0.87)])
    nyra taquin "Il n'y en a pas."
    $ showGroup([("nyra", "taquin", 0.17), ("noam", "neutre", 0.52), ("tomas", "gene", 0.87)])
    noam neutre "Alors je ne viens pas."
    $ hideGroup()
    scene black with dissolve
    return

label bonus_succes009:
    scene black with dissolve
    centered "{size=38}BONUS — PEU ATTENTIF{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "blase", 0.50)])
    camera master at day1_wake_close
    lysa blase "Noam ? ... Hé, tu m'écoutes ou pas ?"
    call _1_WAKE_HIDDEN_SCENE
    camera master
    $ hideGroup()
    scene black with dissolve
    return
