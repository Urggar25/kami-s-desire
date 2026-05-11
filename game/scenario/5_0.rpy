# --------------------------------------------------------------------------------------------
# JOUR 5 — 5_0.rpy
# Vote Jour 4 : NON (status quo des rations — branche 4_0)
# Noam = narrateur principal, parle à la première personne.
# --------------------------------------------------------------------------------------------

label _5_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0
    $ current_day = 5

    pause 1.2

    $ blink()
    "J'ouvre les yeux sans avoir l'impression d'avoir dormi."

    "Ma nuque me lance."
    "Mes épaules sont dures."
    "Cette sensation poisseuse des nuits où le corps s'est allongé, mais où la tête a continué à tourner."

    pause 0.5

    $ blink()
    "Je tourne la tête vers le plafond."
    "Silence."
    "Pas un vrai silence apaisant."
    "Un silence froid. Un silence qui attend quelque chose."

    pause 0.6

    think "Le vote."
    think "Celui d'il y a deux joursr."
    think "Et celui qui arrive."

    "Mon ventre se serre presque aussitôt."
    "Depuis l'annonce de ce vote sur les frontières, tout s'est déjà figé."
    "Les regards comme les discussions."
    "Même les moments où quelqu'un essaie de plaisanter."
    "Rien ne tient."

    $ blink()

    think "Ça ne passera pas."
    think "Personne n'y croit plus vraiment."

    "Je me redresse lentement sur le lit."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "J'ai les traits lourds."
    "Les yeux qui piquent."
    "L'impression d'avoir vieilli de plusieurs jours pendant la nuit."

    pause 0.6

    "Je reste assis au bord du lit."
    "Les pieds posés au sol."
    "Le dos courbé."
    "Comme si me lever demandait déjà une décision, un lourd effort à faire."

    think "Si je vais à la cafétéria, ce sera pareil qu'hier."
    think "Des gens qui ne parlent pas."
    think "Des regards qui fuient au loin."
    think "Et au fond de chaque tête, la même certitude non dite..."
    think "Ce vote va échouer."

    pause 0.7

    "Je déteste cette sensation."
    "Pas seulement la peur de mal faire."
    "Pas seulement la fatigue."
    "Cette espèce d'impuissance molle."
    "Ce moment où rien n'a encore explosé, mais où tout le monde agit déjà comme après la casse."

    "Je me rends compte que j'ai parlé à voix haute après coup."

    pause 0.5

    "Je baisse les yeux vers mes mains."
    "Elles sont immobiles, elles ne tremblent même pas."

    think "Non."
    think "C'est trop facile."
    think "Si je commence comme ça, la journée est déjà morte."

    "Je serre un peu les doigts."
    "Pas assez pour me faire mal."
    "Juste assez pour sentir que je suis là, bien reveillé."

    pause 0.5

    think "Le vote n'a peut-être aucune chance de passer."
    think "L'ambiance est glaciale."
    think "Sael est fermée."
    think "Julian se mure dans sa chambre."
    think "Et moi..."
    think "Moi, j'ai même pas de bonne réponse."

    "Mais je n'abandonnerai pas."

    pause 0.6

    "Le pire, c'est peut-être ça."
    "Le fait que tout le monde ait une part de raison."
    "Sael n'a pas tort."
    "En fait, personne n'a tort..."
    "Et pourtant, à la fin, il faudra quand même trancher."
    "Comme si une décision acceptable était encore possible."
    "Face tu gagnes, pile je perds."

    pause 0.5

    "Je me lève enfin."
    "Mes jambes protestent un peu."
    "Je fais deux pas dans la chambre."

    "L'air me paraît plus froid que d'habitude."
    "Ou alors c'est juste moi."

    play sound sfx_announce
    pause 0.7

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour mes petits ! Jour cinq, et ça fleure déjà le drame."
    kami "Ne vous inquiétez pas : votre prochaine chance de tout rater arrive dans vingt-quatre heures !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Rappel amical : le vote sur la libre circulation aura lieu demain."
    kami "Vous aurez donc une nuit de plus pour vous convaincre que vous êtes capables de décider de quelque chose ensemble."
    kami "Comme c'est amusant !."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "La cafétéria est ouverte. Vos rations sont prêtes. Les mêmes qu'hier."
    kami "Et comme toujours, j'observerai avec beaucoup d'intérêt ce que vous allez faire de cette belle matinée ensoleillée."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oups, j'oubliais, vous ne pouvez pas voir la lumière du soleil depuis le Conclave !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "L'écran s'éteint sous les rires criards de Kami."
    "Le silence retombe doucement."

    pause 0.8

    think "La cafétéria."

    "J'imagine l'ambiance."

    think "Est-ce que j'ai vraiment envie de traverser ça ce matin?"

    pause 0.5

    "Je regarde le bout de pain posé sur ma table de nuit."
    "Dur. Sec. Ca fera très bien l'affaire."

    pause 0.3

    jump _5_0_SKIP_CAFETERIA


label _5_0_SKIP_CAFETERIA:

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    "Je prends le pain."
    "Je l'examine une seconde."
    "Il est vraiment sec."

    think "Je me demande si quelqu'un remarquera que je ne suis pas venu à la cafétéria."

    "Je mords dedans."
    "Ça craque sous les dents."
    "Un goût de rien ou presque."
    "Juste d'un bout de pain déjà sec et dur."

    pause 0.4

    "Je mastique lentement et difficilement."
    "Debout. Seul."
    "Dos à la porte de ma chambre."

    "Il y a quelque chose d'étrangement honnête là-dedans."
    "Pas de conversation à gérer."
    "Pas de regard à soutenir."
    "Pas d'hypocrisie."
    "Juste moi et ce pain, sans témoin."

    think "C'est mieux comme ça, un peu plus reposant."
    think "Au moins pour cette heure-là."

    pause 0.7

    "Je finis le morceau."
    "J'essuie ma main sur mon pantalon."

    "J'entends pendant ce temps là quelques pas dans le couloir."
    "Quelques voix étouffées."
    "Le groupe qui se lève, qui se déplace, qui se retrouve autour d'un plateau."
    "Qui vit ou qui essaye."
    "Je ne me sens pas capable de les rejoindre."
    "Pas dans cet état."
    "Pas avant d'avoir réfléchi à ce que je peux encore faire."

    think "Sael. Si elle vote contre, c'est foutu."
    think "Il faut que je lui parle."
    think "Avant que ce soit trop tard."

    pause 0.5

    "Je sais qu'elle est encore là."
    "Je l'ai entendue hier soir traverser le couloir, rentrer dans sa chambre, fermer sa porte."
    "Elle avait essayé d'être discrète."
    "Ce qui est, à sa façon, encore moins discret."

    pause 0.4

    "Je soupire."
    "Je jette un dernier regard à ma chambre."

    think "Il me semble qu'il faut au moins essayer."

    stop music fadeout 1.2

    jump _5_0_CHERCHE_SAEL


label _5_0_CHERCHE_SAEL:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 0.8

    "Le couloir est presque vide."
    "Quelques silhouettes au loin, qui se dirigent vers la cafétéria sans se presser."
    "Personne ne me regarde, ils vaquent tous à leur occupation."

    "Je marche vers la rangée de portes."
    "Je sais laquelle est la sienne."
    "Chambre 7."
    "Elle a mis un petit morceau de tissu sombre sur la poignée, je ne sais pas vraiment ce que ça veut dire."
    "Je n'ai jamais su si c'était pour signaler quelque chose ou juste une habitude."

    pause 0.4

    "Je m'arrête devant."
    "J'hésite un instant."

    think "Je me demande si elle a envie de me parler."
    think "Je me demande si quelqu'un a envie de me parler ce matin."

    "Je frappe. Deux coups. Pas trop forts."

    play sound sfx_knock volume 8.0
    pause 1.0

    "Silence."

    "Je frappe encore. Un peu plus fort."

    play sound sfx_knock volume 8.0
    pause 0.8

    "Un mouvement derrière la porte."
    "Un bruit de tissu."
    "Puis la porte s'entrouvre."

    play sound sfx_door volume 8.0

    $ showP("sael", "mefiant", 0.50)

    sael "..."

    "Elle me regarde."
    "Elle n'a pas l'air particulièrement surprise."
    "Comme si elle savait que ce serait moi."

    sael mefiant "Noam."

    noam "Ce que j'entends, c'est que tu n'as pas encore mangé non plus."

    sael "..."

    sael neutre "Qu'est-ce que tu veux ?"

    "Elle n'ouvre pas vraiment la porte."
    "Juste assez pour parler."
    "Pas assez pour m'inviter à entrer."

    noam hesitation "Je pense qu'on devrait parler."
    noam "Du vote."
    noam "De demain."

    pause 0.3

    sael "Je savais que c'était pour ça."

    "Elle s'écarte un peu."
    "On ne peut pas vraiment dire qu'elle m'accueille. Elle semble juste tolérer ma présence."

    sael "Rentre."

    pause 0.3

    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    pause 0.6

    "Je m’attendais à une chambre froide."
    "Pas à... ça."
    "Le lit a disparu."
    "Ou plutôt non. Il a été démonté."

    "Des planches posées au sol."
    "Une simple couette."
    "Rien de plus."

    "Le reste de la pièce est presque vide."

    "Quelques objets pendent au mur."
    "Des ficelles, des os, du bois tressé, des symboles que je ne comprends pas."

    think "On dirait pas une chambre."
    think "C'est quoi ce truc ?!"


    $ showP("noam", "hesitation", 0.25)
    noam "T’as vraiment tout enlevé..."

    $ showP("sael", "neutre", 0.75)
    sael "Ce qui ne sert pas prend de la place."

    noam "Et tout ça, là... c’est ..."

    "Elle me regarde enfin."
    "Pas vexée. Pas gênée. Juste fermée."

    sael "Dis moi ce que t'as à dire. Rien d'autre."

    pause 0.3

    noam "Je me demande si tu as encore réfléchi à la question des frontières."
    noam reflexion "Pas pour te convaincre de changer de camp. Juste... pour comprendre où tu en es."

    sael mefiant "Tu veux comprendre, ou tu veux me faire changer d'avis ?"

    noam "Ce que j'entends, c'est que pour toi c'est la même chose."

    "Sael penche légèrement la tête."

    $ showP("sael", "reflechit", 0.75)

    sael "Peut-être."
    sael reflechit "Mais ça ne change pas ma réponse."

    $ showP("noam", "reflexion", 0.25)

    noam "Il me semble que la libre circulation ..."
    noam "C'est des gens de Limen qui pourraient aller chercher du travail ailleurs."
    noam "Des familles séparées qui pourraient se retrouver."

    pause 0.3

    $ showP("sael", "desaccord", 0.75)

    sael "On en a déjà discuté. Les gens ne travaillent plus."
    sael "Ils attendent leur putain de bon de rationnement et ne font rien d'autre de leurs journées."
    sael "Alors oui, y'a sans doute des gens qui voudraient quitter Limen mais pour aller où ?"
    sael "C'est partout pareil. La seule chose que ça va faire c'est créer des tensions."
    sael "Je comprends même pas comment Ryn peut défendre ça ... Avec tout ce qu'il a vécu ..."

    sael determine "J'ai vu ce qui se passe quand les barrières tombent, Noam."
    sael determine "J'ai vu la violence que ça génère."
    sael "Contrairement à ce que tu crois, je n'ai pas peur."
    sael colere "Je n'ai simplement pas oublié ce que c'est que la guerre."

    "Elle dit ça posément."
    "Sans colère."
    "Comme quelqu'un qui a déjà eu cette conversation dans sa tête cent fois, et qui n'attend plus rien de la vraie."

    pause 0.4

    $ showP("noam", "inquiet", 0.25)

    noam "Ce que j'entends, c'est que tu voteras contre."

    sael raison "Oui."
    sael determine "Et rien ne me fera changer d'avis."

    pause 0.4

    "Le mot reste là."
    "Simple. Sec."
    "Sans appel."

    sael raison "Et Mara votera contre aussi. On en a parlé hier soir."

    pause 0.3

    noam "Et Iris ?"

    sael "Va lui demander toi-même."
    sael mefiant "Mais je crois que tu connais déjà la réponse."

    "Je reste sans répondre."
    "Ce n'est pas une attaque de sa part."
    "C'est juste un fait qu'elle pose là, entre nous deux, comme une pierre froide sur une table."

    pause 0.5

    noam hesitation "Je me demande si..."

    "Je m'arrête."

    pause 0.3

    noam "Non. Rien."

    "Je n'ai pas fini ma phrase parce que je n'avais rien à mettre dedans."
    "Pas d'argument solide."
    "Juste cette espèce d'espoir diffus qui ne ressemble même plus à grand-chose."

    $ showP("sael", "fatigue", 0.75)

    sael "Tu n'étais pas obligé de venir."
    sael "Ça ne changera rien."
    sael fatigue "Mais... j'apprécie que tu aies essayé."
    sael fatigue "Au moins on discute sans s'insulter."

    pause 0.4

    hide noam
    hide sael

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "Sael me raccompagne sans un mot puis referme sa porte derrière moi."
    "Le couloir est silencieux."

    pause 0.6

    think "Sael votera contre."
    think "Mara votera contre."

    think "Et Iris... En fait est-ce que ça vaut le coup d'aller lui demander ?"
    think "Avec deux voix contre, c'est certain."
    think "Le vote échouera quoi qu'il arrive."

    "Je fais quelques pas puis passe devant la chambre d'Iris."
    
    think "Oh et puis merde !"

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 0.8

    play sound sfx_door volume 8.0
    $ showP("iris", "fatigue", 0.50)

    iris fatigue "Ah. Noam."

    $ showP("noam", "inquiet", 0.25)
    noam hesitation "Tu as une minute ?"

    "Elle sort dans le couloir, les bras croisés sur elle-même."
    "Elle a l'air d'avoir mal dormi, elle aussi."

    iris "Si c'est pour le vote..."
    iris fatigue "Je sais déjà ce que je vais faire."

    noam "Ce que j'entends, c'est que ta décision est prise."

    iris "Oui."

    pause 0.3

    iris triste "Je comprends le débat, vraiment."
    iris triste "Le fait qu'il faut rendre aux gens la liberté d'aller où ils veulent."
    iris triste "Mais on y arrivera pas, pas avec cet état d'esprit."
    iris "Alors je ne vais pas perdre mon temps à essayer de faire quelque chose."
    iris hesitation "Je ne vais pas participer à cette mascarade. Ca a déjà trop duré."

    pause 0.3

    noam "Non mais tu..."

    iris colere "Quoi ?!"
    iris colere "Dis moi que j'ai tord ?!"

    "Je ne sais pas quoi lui dire."
    "Je comprends sa logique."
    "Mais quelque chose en moi est révulsé à l'idée de ne rien faire."

    noam "Rien..."
    noam "C'est toi qui voit."

    iris triste 'Encore heureux.'

    "Sur ces mots, elle referme la porte derrière elle."

    hide iris
    hide noam

    jump _5_0_DISCUSSION_SAEL


label _5_0_DISCUSSION_SAEL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je reste immobile dans le couloir vide."
    "La porte d'Iris est refermée."
    "Celle de Sael aussi."
    "Les murs métalliques absorbent tout."

    pause 0.5

    "Je n'ai même pas besoin de compter mentalement."
    "Douze représentants. Un seul contre et c'est foutu."
    "On a déjà minimum deux contre."

    pause 0.4

    think "C'est déjà perdu."

    "Cette pensée arrive sans drama."
    "Calme. Presque comme une évidence que je savais déjà."
    "Comme quand on calcule une somme et que le résultat ne surprend personne."

    think "Julian s'est enfermé dans sa chambre."
    think "Et moi... Je suis là à essayer de glaner quelques infos."

    pause 0.4

    "Je m'adosse au mur du couloir."
    "Le métal est froid dans mon dos."

    think "Je me demande si ce vote a encore un sens."
    think "Si quelque chose peut encore être rattrapé."
    think "Est-ce que participer c'est cautionner ce système foireux ?"
    think "Ou si on va juste... traverser ça."
    think "Se faire démolir lentement en regardant chacun voter dans son coin."
    think "Et recommencer, encore ... Encore ... Encore ..."

    pause 0.6

    "Je pousse un souffle par le nez."
    "Long. Contrôlé."
    "Le genre de souffle qu'on fait quand on évite de crier dans un couloir."

    pause 0.5

    "Il reste quoi ?"

    "Il reste aujourd'hui."
    "Ce matin. Cet après-midi."
    "Ce petit espace avant que tout se referme une fois encore et qu'on passe pour des cons."

    think "Je ne sais pas ce que ça donnera."
    think "Mais il me semble que je ne peux pas juste attendre que ça s'effondre."

    jump _5_0_TEMPS_LIBRE_1

label _5_0_TEMPS_LIBRE_1:
    call START_FREE_TIME("_5_0_APRES_TEMPS_LIBRE_1") from _call_START_FREE_TIME_5_0

label _5_0_APRES_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 0.8

    "Je continue à déambuler dans le couloir."
    "Sans vraiment avoir de direction précise."
    "Juste le mouvement pour ne pas rester figé et seul."

    "Les autres sont probablement encore à la cafétéria."
    "Ou retournés dans leurs chambres."
    "Le Conclave a quelque chose de désert dans ces moments-là."
    "Comme un bateau entre deux vagues."

    pause 0.5

    "Je passe devant la salle commune."
    "Elle est vide."
    "Une chaise est renversée près d'une table comme si quelqu'un s'était battu."
    "Un plateau est resté là, discret, pas débarrassé."

    think "Il me semble que je devrais faire quelque chose."
    think "Mais je ne sais vraiment pas quoi."
    think "Convaincre qui ? De quoi faire exactement ?"

    pause 0.5

    "Le problème, avec les convictions des autres, c'est qu'on ne peut pas vraiment les déplacer."
    "On peut juste... s'asseoir à côté d'elles."
    "Les écouter."
    "Et espérer que ça bouge un peu."

    think "Julian."
    think "Il doit encore être dans sa chambre."
    think "Kael a dit qu'il avait tenté d'aller le voir hier soir."
    think "Qu'il lui avait répondu de le laisser tranquille."

    "Je m'arrête."

    think "Et la salle d'observation."
    think "Je n'y suis pas retourné depuis un moment."
    think "Il y a des écrans qui montrent l'état des districts."
    think "Peut-être qu'il y a quelque chose à comprendre là-bas ..."
    think "Quelque chose de concret, qui résiste à l'abstraction des votes."

    pause 0.4

    jump _5_0_CHOIX_PRINCIPAL


label _5_0_CHOIX_PRINCIPAL:

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.3

    "Je reste planté là une seconde."
    "Deux options, pas plus."

    menu:
        "Aller frapper à la porte de Julian.":
            $ doplleganger = 0
            jump _5_0_0_JULIAN

        "Aller à la salle d'observation.":
            $ doplleganger = 1
            jump _5_0_1_OBSERVATION


label _5_0_0_JULIAN:

    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    "Je remonte le couloir des chambres."
    "Chambre 4. Julian."

    "Je m'arrête devant la porte."
    "De l'extérieur, rien."
    "Pas de décoration. Pas de trace de lui."
    "C'est presque drôle."
    "Julian passe son temps à vouloir exister partout, mais sa porte, elle, pourrait être celle de n'importe qui."

    "Je frappe."

    play sound sfx_knock volume 8.0
    pause 1.0

    "Pas de réponse."

    "Je frappe encore."

    play sound sfx_knock volume 8.0
    pause 0.8

    "Cette fois, j'entends du mouvement."
    "Pas quelqu'un qu'on tire hors du lit."
    "Plutôt quelqu'un qui choisit au bout de combien de secondes il va ouvrir."

    noam "Julian. C'est moi."

    pause 0.8

    play sound sfx_door volume 8.0

    $ showP("julian", "neutre", 0.65)
    $ showP("noam", "neutre", 0.30)

    "La porte s'ouvre."

    "Julian est là."
    "Et, pendant une seconde, j'ai un léger temps d'arrêt."

    "Il n'a pas l'air détruit."
    "Il n'a même pas l'air particulièrement atteint."

    julian sourire "Noam."
    julian taquin "Tu viens constater les dégâts ?"

    noam hesitation "Je venais surtout voir comment t'allais."

    julian sourire "Oh."
    julian taquin "C'est presque gentil."

    "Il se pousse."
    "Cette fois, c'est une vraie invitation à entrer dans la chambre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.5

    $ showP("julian", "sourire", 0.65)
    $ showP("noam", "reflexion", 0.30)

    "Je rentre."
    "La chambre est propre."
    "Trop propre."
    "Comme une pièce témoin."
    "Rien qui dépasse."
    "Rien qui vive vraiment."

    julian neutre "Alors ?"
    julian sourire "Tu veux me dire quoi ? De ne pas prendre les résultats comme quelque chose de personnel ?"
    julian taquin "Ou tu veux me sortir une de tes phrases calmes et évidement utiles ?"

    noam "Disons que je suis pas vraiment venu avec un dialogue pré-établit."

    julian rire "Moi si."

    pause 0.4

    "Il dit ça avec un petit sourire."
    "Comme une blague."
    "Sauf que malgré son sourire, je vois qu'il ne rigole pas vraiment."

    noam reflexion "Tu n'as pas l'air aussi abattu que ce matin."

    $ showP("julian", "sourire", 0.65)

    julian sourire "Parce que je ne le suis pas."

    pause 0.3

    noam surpris "...?"

    julian taquin "Tu t'attendais à quoi ?"
    julian sourire "À me trouver en boule dans un coin ?"
    julian rire "À moitié en larmes, la main sur le cœur, à murmurer que le peuple a rejeté ma vision ?"

    noam hesitation "Vu comment tu as disparu après le vote, oui. Un peu."

    $ showP("julian", "reflexion", 0.65)

    julian reflexion "Mmh."

    "Il tourne la tête vers la porte."
    "Puis il se lève et se dirige vers elle."

    hide julian
    $ showP("julian", "neutre", 0.72)

    "Il traverse la pièce sans se presser."
    "Sa main monte vers le dispositif."

    noam "Julian ?"

    julian sourire "Regarde."

    play sound sfx_beep
    pause 0.6

    "Le grésillement disparaît."

    "Et Julian change."

    $ showP("julian", "triste", 0.72)

    "Pas un peu. Il change totalement."
    "Ses épaules tombent."
    "Son regard se vide."
    "Sa bouche tremble juste assez."
    "Même sa respiration semble plus courte."

    julian triste "Je..."
    julian triste "J'avoue que c'est difficile."

    "Sa voix aussi a changé."
    "Plus basse."
    "Plus fragile."
    "Parfaitement dosée."

    julian triste "Je pensais vraiment qu'on pouvait faire quelque chose de grand."
    julian decu "Et au final..."
    julian triste "au final, vous avez eu peur."

    pause 0.3

    julian decu "Mais bon."
    julian triste "Je suppose qu'il faut accepter la défaite avec dignité."

    "Je le fixe."
    "Je sais ce qu'il est en train de faire."
    "Et le pire, c'est que la caméra de la chambre se braque sur lui."

    noam reflexion "Arrête de..."

    "Avant que je ne puisse terminer ma phrase, il réappuit sur le brouilleur."
    play sound sfx_beep

    noam reflexion "...jouer la comédie !"

    pause 0.6

    "Le grésillement revient."
    "Et avec lui, Julian aussi."

    $ showP("julian", "rire", 0.72)

    julian rire "Évidemment que je joue la comédie."

    pause 0.4

    $ showP("noam", "triste", 0.30)

    noam surpris "..."

    julian taquin "Tu crois que les gens veulent voir quoi ?"
    julian sourire "Un type lucide et ennuyeux ?"
    julian rire "Non."
    julian joie "Ils veulent voir de la tension, des difficultés, et l'espoir que ce monde puisse changer."
    julian sourire "Bref, quelque chose qui se raconte bien."

    pause 0.4

    $ showP("julian", "idee", 0.72)

    julian idee "Le génie ambitieux."
    julian idee "Le projet trop en avance."
    julian idee "L'idéaliste blessé par la médiocrité collective."
    julian rire "C'est ce genre de rôle que les gens veulent voir.."
    julian sourire "Et surtout, ça me garde au centre de toutes vos combines."

    noam desaccord "Donc tu t'en fous."

    julian neutre "Du vote ?"

    pause 0.2

    $ showP("julian", "sourire", 0.72)

    julian sourire "Oui."

    noam "À ce point-là ?"

    julian taquin "Noam."
    julian sourire "Qu'il passe ou qu'il tombe, ça me donne quelque chose."
    julian idee "Si ça passe, j'ai l'image du type qui a porté une idée décisive."
    julian idee "Si ça tombe, j'ai l'image du type qui s'est battu contre ceux qui ont eu peur du changement."
    julian rire "Dans les deux cas, je suis gagnant."

    pause 0.5

    noam reflexion "C'est vraiment ça, ton problème."
    noam "Comment tu veux que les autres t'apprécies quand on ne sait pas ce que tu penses vraiment ?"
    noam colere "Derrière nos décisions il y a des vies qui sont en jeu !"

    $ showP("julian", "sourire", 0.72)

    julian sourire "Oui."
    julian taquin "Tu dis ça comme si c'était petit."

    noam "Ça l'est."

    pause 0.4

    "Le sourire de Julian bouge à peine."
    "Pas assez pour disparaître."
    "Il s'est légèrement durcit."

    $ showP("julian", "reflexion", 0.72)

    julian reflexion "C'est marrant."
    julian reflexion "Vous faites tous semblant que vos convictions sont pures."
    julian reflexion "Que vous défendez des idées, des gens, des principes."
    julian "Mais au bout du compte, tout le monde veut la même chose."
    julian "Peser."
    julian "Compter."
    julian "Laisser une trace."

    noam "Non. Moi je m'en fou."

    julian sourire "Si."
    julian "Vous avez juste honte de le dire."
    julian taquin "Et peut être toi plus encore que les autres."
    julian "Au final, tu n'as pas l'impression d'être le personnage principal de quelque chose de plus grand ici ?"

    pause 0.4

    noam "Il y a quelque chose qui cloche chez toi."

    "Il se rassoit."
    "Détendu et souriant."
    "Comme si on parlait d'un jeu, pas d'un vote qui peut toucher des millions de gens."

    $ showP("julian", "joie", 0.65)

    julian joie "Franchement ?"
    julian rire "Hier soir, dès que j'ai vu les têtes autour de la table, j'ai directement compris."
    julian taquin "La peur. L'hésitation. Les petits calculs."
    julian sourire "J'ai su que ça pouvait tomber."
    julian taquin "Tu es peut être même celui qui a appuyé sur le bouton rouge."

    noam reflexion "Et ça ne t'a rien fait ?!"

    $ showP("julian", "neutre", 0.65)

    julian neutre "Si, j'aurais quand même préféré que ça passe."

    pause 0.3

    julian sourire "Mais vous n'avez pas eu ce courage."

    noam desaccord "Tu t'entends parler ?"

    julian taquin "Très bien, oui."
    julian taquin "Je trouve même que je parle particulièrement bien."

    noam "Tu présentes ça comme de la lucidité, mais c'est juste..."
    noam hesitation "vide de sens."

    pause 0.4

    $ showP("julian", "sourire", 0.65)

    noam "Tu transformes tout en scène."
    noam reflexion "Même maintenant, même quand on est pas filmé."
    noam "Même avec moi."

    julian neutre "Bien sûr."
    julian taquin "Pourquoi est-ce que tu serais une exception ?"

    pause 0.5

    "Je serre un peu les dents."
    "Pas à cause du ton."
    "À cause de ce qu'il avoue avec autant de facilité."

    noam "Et quand plus personne regardera ?"

    pause 0.4

    "Ça le coupe dans son élan."
    "Pas longtemps."
    "Une seconde à peine."

    $ showP("julian", "inquietude", 0.65)

    julian inquietude "..."

    noam reflexion "Quand il n'y aura plus de salle."
    noam "Plus de débat."
    noam "Plus de caméra."
    noam "Plus de rôle à jouer."
    noam "Tu feras quoi ?"

    "Son regard dévie."
    "Enfin."
    "Pas vers moi."
    "Pas vers la porte."
    "Vers le vide, entre les deux."

    $ showP("julian", "peur", 0.65)

    julian peur "Tu crois que c'est drôle, ça ?"

    "Sa voix a changé."
    "Elle n'est plus théâtrale, pas cette fois."
    "Trop sèche."
    "Trop rapide."

    julian inquietude "Tu crois que je n'ai pas pensé à ça ?"

    pause 0.4

    $ showP("julian", "reflexion", 0.65)

    julian reflexion "..."

    noam "Donc c'est ça."

    julian reflexion "Quoi."

    noam "Tu t'en fous pas vraiment."

    pause 0.5

    "Julian me regarde."
    "Longtemps. Cette fois, il ne sourit pas."

    $ showP("julian", "triste", 0.65)

    julian triste "Tu sais ce qui est insupportable ?"
    julian triste "C'est que tu crois avoir raison."

    pause 0.4

    $ showP("julian", "sourire", 0.65)

    "Le sourire revient."
    "Pas chaleureux."
    "Replacé."

    julian idee "Moi je l'assume, je veux être le type dont on parlera encore quand cette mascarade sera finie."
    julian sourire "Et si pour ça il faut jouer le visionnaire blessé, je jouerai le visionnaire blessé."
    julian rire "Si demain il faut jouer le survivant esseulé, je jouerai ça aussi."

    noam "T'es sérieux."

    julian joie "Évidemment."
    julian taquin "Tu croyais que tout ça se faisait tout seul ?"

    pause 0.4

    noam desaccord "C'est pathétique."

    "Il hausse les épaules."

    $ showP("julian", "neutre", 0.65)

    julian neutre "Peut-être."
    julian sourire "Mais ça ne l'est pas plus que la société."

    noam reflexion "Et le prochain vote ?"
    noam "Tu vas faire quoi ?"

    julian taquin "Ce qu'il faut."

    noam "C'est-à-dire ?"

    julian sourire "Tu verras bien. Mais je serai là."

    pause 0.4

    noam "Tu me dégoûtes."

    $ showP("julian", "sourire", 0.65)

    julian sourire "Non."

    pause 0.2

    $ showP("julian", "reflexion", 0.65)

    julian reflexion "Je t'inquiète."

    "Je ne réponds pas."
    "Parce qu'il a raison."
    "Et parce que ça l'amuse de l'avoir compris."

    pause 0.5

    noam "Tu sais quoi."
    noam "Le pire, c'est pas que tu joues un rôle."
    noam reflexion "Le pire, c'est que je crois qu'à force, tu sais même plus ce qu'il te reste quand t'arrêtes."

    $ showP("julian", "sourire", 0.65)

    julian sourire "Alors vaut mieux ne pas arrêter."

    "Réponse immédiate."

    pause 0.4

    noam triste "Ouais."
    noam "Peut-être bien."

    "Je me lève."
    "Julian ne me retient pas."
    "Il me suit juste du regard, avec cette expression lisse qu'il remet comme on remet une veste."

    noam reflexion "Merci pour ton honnêteté."

    julian rire "C'était un plaisir."

    noam "Non."
    noam "C'était un avertissement."

    pause 0.4

    $ showP("julian", "surpris", 0.65)

    julian surpris "..."

    $ showP("julian", "sourire", 0.65)

    julian sourire "Mais tu reviendras quand même."

    noam "Je sais pas."

    julian taquin "Oh que si."
    julian sourire "Parce que tu as beau jouer le rôle du mec calme."
    julian reflexion "Tu aimes quand la tension monte."

    "Je m'arrête une seconde devant la porte."
    "Le brouilleur grésille encore."

    "Dedans, il peut dire ce qu'il veut."
    "Dehors, il jouera autre chose."

    "Et le plus inquiétant, c'est que je ne sais pas quelle version est la plus dangereuse."

    hide noam
    hide julian

    jump _5_0_FIN_JOURNEE


label _5_0_1_OBSERVATION:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    "Je marche vers la salle d'observation."
    "Kami ne nous a jamais interdit de surveiller les données du terminal après tout."
    "Probablement parce que regarder le vide en face finit toujours par décourager les gens."

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 0.8

    "La salle est plongée dans cette lumière bleue permanente."
    "Les baies vitrées donnent directement sur l'espace."
    "Même après plusieurs jours, ça me prend quelques secondes à chaque fois d'habituer mes yeux à cette étrange atomosphère."
    "Ce silence derrière les vitres qui n'a rien à voir avec le silence géné des couloirs."
    "Un silence qui existe depuis des milliards d'années et qui durera des milliards d'années encore après nous."
    "Indifférent à nos votes, à notre lutte ou à notre survie."

    $ showP("elias", "detendu", 0.75)

    "Elias est là."
    "Assis à la console centrale."
    "Une tasse bien chaude dans une main."
    "Les yeux sur un des écrans latéraux qui affiche les données des districts."

    elias detendu "Noam ?"

    "Il ne s'est même pas retourné."

    elias "Qu'est ce que tu fais là ?"

    $ showP("noam", "neutre", 0.25)

    noam "C'est le seul endroit qui soit calme aujourd'hui."

    $ showP("elias", "detendu", 0.75)
    elias "Ouais."
    elias "La cafétéria, c'était... chargé."

    "Il prend une gorgée de café."
    "Il continuer à fixer l'écran sans tourner la tête."

    $ showP("elias", "reflechit", 0.75)
    elias "Regarde ça."

    "Il pointe vers une partie spécifique du panneau droit."
    "Il y a un flux de données qui défile en temps réel."
    "Des chiffres, des courbes, des noms de districts."

    $ showP("noam", "reflexion", 0.25)

    noam "Faut que tu m'expliques, c'est quoi tous ces chiffres ?"

    elias "Ici ..."

    "Il pointe du doigt une liste de nom qui défile."

    elias reflechit "C'est le nom de tous les gens qui ont enfreint les règles, et la règle qu'ils n'ont pas respecté."

    "Je regarde la liste. Elle est longue. Bien trop longue."
    "Je regarde les raisons : vol, bagarre, menace ... Les raisons ne manquent pas mais il y a toujours un point central : les tiquets de rationnement."
    "Les gens veulent juste manger."

    pause 0.4

    "Je m'approche de la console."
    "Je veux voir plus précisément."
    "Je tends le bras vers l'écran pour zoomer sur la courbe de population de Limen."

    pause 0.3

    elias reflechit "Attends, regarde ..."

    "Elias se relève pour me montrer quelque chose mais son coude accroche sa tasse."
    play sound sfx_drop

    scene bg_cg027 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg027")

    "Un bruit mat."
    "Le café se renverse en arc sur le bord de la console."
    "Sur les touches."
    "Sur le panneau de commande latéral."

    elias "Et merde !"

    "Il se lève d'un bond."
    "Attrape sa tasse ; vide désormais."
    "Le café ruisselle entre les touches."

    "Un voyant passe au rouge."
    "Un léger sifflement."

    noam "C'est moi qui— j'ai failli te bousculer, je—"

    elias "Non non, c'était ma tasse."

    "Un autre voyant s'allume."
    "Orange."
    "Puis une fumée fine s'échappe d'une grille latérale."
    "Pas de flammes. Juste cette fumée grise et acre qui monte tranquillement."

    elias inquiet "OK."
    elias "C'est pas dramatique, mais..."

    "Un déclic mécanique quelque part dans le mur."
    "Fort."
    "Presque un claquement."

    "On se retourne."

    "La porte automatique de la salle s'est fermée."
    "Hermétiquement."
    "Le panneau de commande à côté affiche : VERROUILLAGE SÉCURITÉ — ANOMALIE DÉTECTÉE."

    pause 0.5

    elias inquiet "Ah."

    noam peur "La porte est bloquée ?"

    elias "Protocole de sécurité automatique."
    elias reflechit "Si un équipement grille, la salle se verrouille le temps que le système vérifie qu'il n'y a pas de fuite ou d'incendie."
    elias reflechit "En principe ça dure pas longtemps."

    noam hesitation "En principe."

    elias "Ouais."
    elias detendu "En principe."

    pause 0.4

    "La fumée continue de s'échapper de la grille."
    "Fine. Légère."
    "Pas de danger immédiat."
    "Mais la porte reste fermée."

    "Et derrière les baies vitrées, l'espace continue d'être indifférent à tout ça."

    noam reflexion "..."

    noam "Je me demande combien de temps on a."

    scene bg_cg028 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg028")

    elias "La salle est ventilée."
    elias detendu "On n'étouffera pas."
    elias "Mais ouais... on est bloqués là pour un moment."

    "Il s'assoit par terre."
    "Le dos contre le panneau, loin de l'écran qui fume encore légèrement."
    "Avec le calme de quelqu'un qui a déjà vécu des situations plus graves."

    elias neutre "Tu voulais regarder les chiffres de Limen, non ?"

    "Il pointe vers l'écran qui fonctionne encore."

    elias detendu "On n'a nulle part où aller."
    elias "Autant qu'on en parle."

    noam "Il me semble que c'est pas le contexte idéal pour une discussion sur le vote."

    elias rire "Non."
    elias "Mais les contextes idéaux, ici, ça n'existe plus vraiment."

    pause 0.5

    "Je m'assis à côté de lui."
    "Par terre. Le dos au mur."
    "Les jambes tendues devant moi."
    "On regarde tous les deux les voyants rouges et les données qui défilent toujours."

    elias reflechit "Tu crois que ça va passer, le vote ?"

    noam "Je me demande si quelque chose peut encore changer avant demain."

    pause 0.3

    elias reflechit "Sael votera contre."
    elias "C'est sûr."

    noam "Elle me l'a dit ce matin."
    noam hesitation "Mara aussi. Et Iris."

    elias "..."

    "Silence."

    elias fatigue "Alors c'est foutu."

    noam "Peut-être pas ..."

    "Je le dis sans vraiment y croire."
    "On le sait tous les deux."

    pause 1.0

    call screen custom_title("Après plusieurs heures")

    scene bg_observation at adaptive_fullscreen with dissolve

    pause 3.0

    "Les voyants passent de rouge à orange."
    "La fumée s'est dissipée."
    "Le panneau de la porte clignote."

    play sound "sound/sfx_door.ogg"

    "Un déclic."
    "La porte s'ouvre."

    $ showP("elias", "fatigue", 0.75)

    elias fatigue "Ah. Libérés."

    "Il se lève."
    "S'étire le dos."

    elias "Je vais voir si j'ai pas cramé un truc important."

    "Il examine la console."
    "Quelques touches sont pâteuses."
    "L'écran latéral est éteint."

    elias neutre "Rien de critique."
    elias "Juste la caméra de relevé satellite sur ce panneau."

    noam reflexion "Je me demande si Kami va nous faire une remarque là-dessus."

    elias rire "Probablement."
    elias "Elle fait des remarques sur tout."

    hide noam
    hide elias

    "Enfin libérés, on se sépare et je me retrouve dans le couloir."

    jump _5_0_FIN_JOURNEE


label _5_0_FIN_JOURNEE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    "L'après-midi se passe dans un calme de façade."
    "Quelques échanges à la salle commune."
    "Un repas du soir que j'avale sans vraiment y goûter."
    "Des conversations qui démarrent et qui s'arrêtent avant d'aboutir à quelque chose d'interessant."

    "Je croise Tomas dans le couloir."
    "Il fait un signe de tête."
    "Pas de mots."
    "Je fais pareil."

    "Je croise Nyra."
    "Elle a l'air de calculer quelque chose dans sa tête."
    "Elle ne me demande rien."
    "Je ne demande rien non plus."

    pause 0.6

    "La journée se finit comme elle a commencé."
    "Lentement. Lourdement."
    "Sans catastrophe, mais sans rien qui ressemble à une ouverture."

    "Kami ne fait pas d'annonce en début de soirée."
    "Ce silence-là est presque pire."
    "Comme si elle attendait quelque chose qu'on n'arrive pas à lui donner."

    pause 0.5

    "Je rentre dans ma chambre."

    scene bg_chambre at adaptive_fullscreen with dissolve

    pause 0.6

    "Je m'assis au bord du lit."
    "Pas encore prêt à m'allonger."
    "Juste là. Posé sur le bord."

    pause 0.5

    think "Je pense que tout le monde a raison."
    think "D'une certaine façon."
    think "Et en même temps, le vote de demain sera contre."

    pause 0.4

    $ blink()
    "Je m'allonge sur le dos."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    "La lumière bleue des veilleuses."
    "Toujours là."
    "Ce plafond qui ne répond jamais."

    $ blink()

    "On a encore une nuit."
    "Et un matin."
    "Et puis le vote."

    think "Je me demande ce qu'on peut encore faire."
    think "Je me demande si 'faire' est encore le bon mot."
    think "Ou si parfois, il faut juste... être là."
    think "Sans solution. Sans angle."
    think "Juste présent dans quelque chose qui se casse."

    pause 0.5

    $ blink()

    "Quelque part dans le couloir, une porte s'ouvre et se referme."
    "Des pas discrets."
    "Quelqu'un qui n'arrive pas à dormir non plus."

    "Ou quelqu'un qui fait semblant."

    pause 0.6

    $ blink()

    "Je ferme les yeux."
    "Pas parce que je suis en paix."
    "Juste parce que le corps finit toujours par tomber de fatigue avant la tête."

    "Le vote de demain est probablement perdu."
    "Et pourtant, quelque chose dans le fait de s'être levé ce matin, d'avoir frappé aux portes, d'avoir été là..."
    "Quelque chose là-dedans ne ressemble pas tout à fait à la défaite."

    pause 0.4

    "Je ne sais pas encore ce que ça veut dire."

    $ blink()
    pause 1.5

    "Le sommeil arrive."
    "Lent. Sans fracas."
    "Juste le silence, et la certitude que demain sera difficile."
    "Et que j'y serai quand même."

    $ current_day = 6
    pause 1.0

    if doplleganger == 0:
        call end_day("6")
        jump _6_0_0_REVEIL_CHAMBRE

    else:
        call end_day("6")
        jump _6_0_1_REVEIL_CHAMBRE