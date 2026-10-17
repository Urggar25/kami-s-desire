# Scènes bonus indépendantes du scénario et sans modification de la progression.
# Appelées depuis la tablette avec renpy.call_in_new_context.
# Aucune variable de route n'est altérée ; les dialogues peuvent être rejoués.

label bonus_succes001:
    scene black with dissolve
    centered "{size=38}BONUS — UNE DRÔLE DE SENSATION{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Je suis toujours devant cette fichue porte, les doigts posés sur mon cou. J'ai beau inspirer profondément, la brûlure que je viens de ressentir refuse de disparaître complètement."

    noam inquiet "Je vous jure que pendant une seconde, j'ai eu l'impression que quelque chose me serrait la gorge. Et le plus bizarre, c'est que juste avant de paniquer, j'ai senti une sorte de... Je sais pas comment expliquer ça."

    mara taquin "D'excitation ?"

    noam surpris "Quoi ?! Non ! Enfin, pas comme ça ! Pourquoi tu me regardes avec ce sourire ?"

    mara rire "Parce que tu viens de décrire une expérience franchement terrifiante en ayant presque l'air déçu qu'elle soit terminée. Excuse-moi, mais c'est difficile de ne pas poser la question."

    noam colere "J'ai cru mourir, Mara ! Je crois que ça mérite un peu mieux qu'une blague."

    sael inquiet "Attends, tu peux répéter ce que tu viens de dire ? Tu as ressenti quelque chose d'agréable au moment où tu ne pouvais plus respirer ?"

    noam hesitation "Agréable, non... Enfin, c'était surtout étrange. Mon cœur battait tellement fort que j'ai eu une espèce de vertige, puis tout s'est arrêté. Je sais même pas si ce que je raconte a du sens."

    sael determine "Ça en a, mais il faut surtout que tu ne cherches pas à reproduire cette sensation. Le manque d'oxygène et la pression sur le cou peuvent provoquer des lésions graves ou une perte de connaissance, parfois sans laisser le temps de comprendre ce qui arrive."

    mara reflexion "Voilà qui gâche un peu ma théorie sur tes loisirs, mais j'avoue que je préfère te voir respirer normalement."

    noam blase "Je suis ravi de découvrir qu'on partage au moins cette passion."

    mara taquin "Oh, ne sois pas si susceptible. J'allais justement proposer une activité beaucoup moins dangereuse pour apprendre à se connaître."

    noam inquiet "Laquelle ?"

    mara rire "On reste assis cinq minutes sans toucher à aucune porte."

    sael sourire "Pour une fois, je suis entièrement d'accord avec elle."

    noam "Vous savez quoi ? J'aurais dû commencer par là."

    "Je m'éloigne enfin du capteur, encore un peu tremblant. Mara conserve son sourire, mais elle attend que j'aie repris mon souffle avant de retourner à sa place."

    scene black with dissolve
    return

label bonus_succes005:
    scene black with dissolve
    centered "{size=38}BONUS — LES PREMIÈRES IMPRESSIONS{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Une conversation qui aurait très bien pu avoir lieu pendant notre première attente dans la salle du Conclave."
    mara taquin "Bon, on a trente jours à passer ensemble. Je propose qu'on établisse tout de suite qui, ici, est le plus pénible."
    noam "C'est un concours ou tu viens directement réclamer ton trophée ?"
    mara rire "Oh, il a du répondant ! Je lui donne une semaine avant de craquer."
    iris blase "Moi, je lui donne dix minutes avant de vous demander de vous taire tous les deux."
    elen joie "Attendez, on pourrait faire un vrai vote ! Chacun écrit un nom sur un papier, et celui qui gagne doit faire la vaisselle."
    ryn colere "C'est pas parce qu'on est coincés ici qu'il faut transformer chaque conversation en réunion."
    noam "Merci, Ryn, pour cette intervention qui prouve qu'on n'a pas besoin de voter pour se disputer."
    mara taquin "Je change mon choix. C'est lui, le plus pénible."
    iris taquin "Pour une fois, je suis d'accord avec elle."
    elen joie "Eh, c'est historique ! Vous venez de tomber d'accord sur quelque chose !"
    noam "Génial. Notre première unanimité porte sur ma tête."
    mara rire "Tu vois ? On va très bien s'entendre."
    "Le pire, c'est que pendant quelques secondes, je crois presque qu'elle a raison."
    scene black with dissolve
    return

label bonus_succes006:
    scene black with dissolve
    centered "{size=38}BONUS — VISITE GUIDÉE, OU PRESQUE{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Je repense à ce qu'Elias et Kael auraient pu me dire si j'avais demandé une visite commentée."
    elias neutre "La station est plutôt bien pensée. Le problème, c'est que tout ce qui est bien pensé finit par tomber en panne quand quelqu'un oublie une vis."
    noam "C'est censé me rassurer ?"
    kael raison "Il exagère. Les systèmes critiques ont normalement plusieurs sécurités indépendantes."
    elias taquin "Normalement, oui. C'est précisément le mot qui m'inquiète."
    noam "Et la cafétéria ? Dis-moi au moins que la nourriture ne dépend pas d'une vis."
    elias sourire "Là, c'est pire. Ça dépend des robots."
    kael taquin "Les Goumi ne sont pas des assassins, Noam. Leur mission consiste à servir des repas."
    noam "Tu dis ça comme quelqu'un qui n'a jamais goûté un plat préparé par un appareil en colère."
    elias rire "Bon, la bonne nouvelle, c'est qu'on a une infirmerie."
    noam "Et la mauvaise ?"
    kael doute "J'imagine que c'est le fait que tu aies déjà besoin de savoir où elle est."
    noam "Je sens que ces trente jours vont être interminables."
    scene black with dissolve
    return

label bonus_succes007:
    scene black with dissolve
    centered "{size=38}BONUS — UNE BONNE QUESTION{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Je m'imagine soumettre une dernière fois mon dossier d'arguments à Tomas et Nyra, loin du vacarme des débats."
    tomas reflechit "Tu as vraiment noté tout ce qu'ils ont dit ? Même les remarques qui avaient l'air complètement inutiles ?"
    noam "J'ai surtout peur d'oublier celle qui fera changer quelqu'un d'avis."
    nyra raison "Alors ne confonds pas quantité et qualité. Huit bons arguments ne font pas huit personnes convaincues."
    noam "Tu pourrais me laisser profiter cinq secondes de l'impression d'avoir bien travaillé ?"
    tomas hesitation "Non, mais elle a raison. Un argument peut parfaitement convaincre une personne et braquer celle qui est assise juste à côté."
    nyra sourire "La question importante n'est pas seulement de savoir ce que tu vas dire, mais à qui tu le dis."
    noam "Donc après avoir rassemblé des fiches pendant deux jours, vous m'annoncez qu'il faut aussi réfléchir ?"
    tomas gene "Présenté comme ça..."
    nyra taquin "Tu peux toujours ranger ton dossier et essayer de les convaincre en improvisant."
    noam "Je préfère encore relire les huit fiches."
    nyra sourire "Alors tu as peut-être appris quelque chose."
    scene black with dissolve
    return

label bonus_succes008:
    scene black with dissolve
    centered "{size=38}BONUS — LE CHRONOMÈTRE{/size}"
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Cette course dans les couloirs me revient en mémoire, surtout le moment où Nyra a enfin décidé de ralentir."
    noam "Tu sais que tu aurais pu prévenir avant de partir comme une fusée ?"
    nyra sourire "Je t'ai dit de courir."
    noam "Oui, ça, j'avais compris. C'est la partie où j'ai failli embrasser trois murs que j'aurais aimé éviter."
    nyra taquin "Tu ne les as pas touchés. C'est le principal."
    tomas hesitation "Moi, je trouve ça assez impressionnant que vous soyez arrivés aussi vite."
    noam "Merci, Tomas. Enfin quelqu'un qui reconnaît mes efforts."
    nyra raison "Il a surtout été porté par la panique."
    noam "La panique est une excellente source d'énergie. On devrait en faire un programme d'entraînement."
    tomas gene "Je ne suis pas sûr que ce soit médicalement recommandé."
    nyra sourire "En tout cas, la prochaine fois, je chronomètre."
    noam "La prochaine fois, je prends l'ascenseur."
    nyra taquin "Il n'y en a pas."
    noam "Alors je ne viens pas."
    scene black with dissolve
    return
