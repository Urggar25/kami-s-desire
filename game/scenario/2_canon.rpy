label _2_CANON:

    $ day_id = 2

    scene black
    play music "music/main_menu.mp3" fadein 1.0

    pause 0.6

    think "…"

    pause 0.4

    think "Je bouge."
    think "Vraiment vraiment trop."

    pause 0.4

    think "Je me tourne sur le côté."
    think "Non, ça ne va pas."

    pause 0.4

    think "Sur le dos."
    think "Mon dieu, c'est encore pire !"

    pause 0.5

    think "Je replie une de mes jambes."
    think "J’essaie de trouver une position."
    think "N’importe laquelle tant qu'elle me permette de dormir."

    pause 0.5

    think "Le matelas est pourtant agréable."
    think "C’est sans doute moi qui n’arrive pas à me détendre."

    $ blink()

    pause 0.6

    think "J'ouvre les yeux."
    scene bg_cg012 at adaptive_fullscreen with fade

    $ blink()

    think "Je tente de les refermer."

    $ blink()

    pause 0.4

    think "Encore."

    $ blink()

    pause 0.6

    think "Chaque fois que je commence à glisser…"
    $ blink()
    think "Il y a une image qui revient."

    pause 0.6

    $ blink()

    think "Une salle."
    think "Les sièges du Conclave."
    think "Ces voix qui m'étaient encore inconnues jusqu'à hier."

    pause 0.6

    $ blink()
    think "Kami."

    pause 0.6

    think "Je serre les dents."
    think "J’inspire lentement."
    think "Expire."

    pause 0.6

    $ blink()
    think "Rien n’y fait."
    think "Ca ne me calme pas."
    $ blink()

    "Alors que j'avais du mal à dormir convenablement, une alarme retentit."

    play sound sfx_announce

    pause 0.8

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ooooh ?"

    pause 0.4

    kami "Déjà en train de remuer dans vos petits lits ?"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Enfin, je ne peux que spéculer vous n'êtes pas nombreux à avoir désactiver votre brouilleur !"

    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "C’est mignon."
    kami "Vraiment."

    pause 0.5

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Mais soit, nous en sommes au jour deux."

    $ blink()

    pause 0.3

    kami "Il est huit heures du matin."

    pause 0.4

    kami "Certains d’entre vous ont très mal dormi."
    kami "Et je tiens à préciser que c'est tout à fait normal…"

    pause 0.5
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    pause 0.4

    kami "Votre cerveau adore ce genre de choses."
    kami "Vraiment."

    pause 0.4

    kami "Il appelle ça du stress."
    kami "Et quand il est stressé…"

    $ blink()

    pause 0.3

    kami "Il libère du cortisol."

    $ blink()

    pause 0.4

    kami "Une petite hormone très pratique."
    kami "Elle vous garde éveillés."
    kami "Alertes."
    kami "Prêts à survivre."

    pause 0.4

    kami "Le problème…"
    kami "C’est qu’elle déteste le sommeil."

    $ blink()

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Votre cerveau a travaillé tard."
    kami "Même quand vous faisiez semblant de dormir."

    pause 0.6

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "je vous donne rendez-vous à neuf heures."
    kami "À la cafétéria."

    pause 0.4

    kami "Pour faire la première annonce importante de ce Conclave."

    pause 0.5

    kami "Je vous conseille d’y assister."
    kami "Ce serait dommage de rater un moment clé…"

    pause 0.4
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "…surtout quand il s’agit de votre avenir proche."

    $ blink()

    pause 0.6

    kami "Héhé, bonne journée !"

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    pause 0.8

    # Réveil réel
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    think "…"

    pause 0.4

    think "Je fixe le plafond."
    think "Cette fois, je suis bien réveillé."

    pause 0.6

    think "Hier…"
    think "Tout s’est enchaîné si vote, sans la moindre pause."

    pause 0.5

    think "Je n’ai pas eu le temps de réfléchir."
    think "Juste eu à peine le temps de réagir."
    think "D’écouter."
    think "D’avancer."
    think "De comprendre ce qui nous arrivait. Et encore ..."

    pause 0.6

    think "Aujourd’hui, c’est différent."

    pause 0.6

    think "Le calme est trompeur."
    think "Mais il est là. Attentif, patient."
    think "Je sais qu'il ne durera pas."

    pause 0.6

    think "Et avec lui…"
    think "Les pensées que j’ai repoussées jusque là."

    pause 0.8

    think "Je suis à des milliers de kilomètres de ma famille."

    pause 0.6

    think "Je revois encore l’appartement de mes parents."
    think "Celui que j'ai quitté avant-hier."
    think "Ce matin qui devait être comme les autres ..."
    think "Le bruit trop fort de la cafetière et le goût amer du café."

    pause 0.6

    think "Et puis surtout les rires, les cris, les caprices de Juliette."

    pause 0.6

    think "Ma petite sœur."
    think "Toujours debout trop tôt à venir enquiquiner tout le monde."
    think "Toujours trop curieuse à poser des questions sur tout et rien."

    pause 0.6

    think "Comment expliquer ce qu'il m'arrive à quelqu’un comme elle ?"
    think "Ces règles."
    think "Ce Conclave."
    think "Kami."

    pause 0.8

    think "Est-ce qu’elle a compris ?"
    think "Ou est-ce qu’elle regarde l'écran de la télévision en ce moment ?"
    think "Est-ce qu'elle me regarde ?"

    pause 0.6

    think "Je n’ai aucun moyen de savoir."
    think "Aucun moyen d’aider ou même de comprendre."

    pause 0.8

    think "Je suis ici."
    think "Pas avec eux."
    think "Je dois être fort."

    pause 0.6

    think "Rester immobile ne changera rien à notre situation."

    pause 0.6

    think "Je me redresse."
    think "Je pose les pieds au sol."

    pause 0.6

    think "Il est temps de se motiver.."
    think "Direction la cafétéria."

    stop music fadeout 1.0
    pause 0.6

    jump _2_CAFETERIA_ANNONCE_KAMI

# Durée : 2m35
# Total : 1h 7m 25s

label _2_CAFETERIA_ANNONCE_KAMI:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    pause 0.4

    "Dès que je mets un pied dans la cafétéria, je comprends que ça parle déjà trop fort."
    play sound sfx_door

    $ showP("tomas", "neutre", 0.10)

    tomas inquiet "E-Excusez-moi mais… euh…"
    tomas taquin "On est obligés d’être tous là, là ? Enfin je veux dire… maintenant ?"

    $ showP("iris", "colere", 0.50)

    iris "Super."
    iris "Même pas dix minutes et ça commence déjà à poser des questions idiotes."

    tomas panne "Je— je dis pas que c’est idiot !"
    tomas panne "C’est juste que… enfin… voilà."

    $ showP("ryn", "neutre", 0.86)

    ryn neutre "Non mais laisse."
    ryn reflechit "Au moins lui il parle."
    ryn reflechit "Y’en a qui serrent les dents depuis hier et qui font semblant que tout va bien."

    $ showP("elen", "joie", 0.40)

    elen "Oh !"
    elen "C’est vrai que l’ambiance est un peu bizarre ce matin."
    elen "Mais regardez, ils ont changé les plateaux ! Ils sont plus brillants, non ?"

    iris "Elen."
    iris "On s’en fout des plateaux."

    elen desaccord "Oui mais quand même !"
    elen content "C’est peut-être fait exprès pour nous mettre de bonne humeur."

    ryn fatigue "Ou pour nous faire avaler des conneries plus facilement."

    pause 0.4

    hide tomas
    $ showP("elias", "neutre", 0.15)

    elias "…"
    elias "Ça va arriver, de toute façon."
    elias "Autant être prêts."

    noam "Prêts à quoi, exactement ?"

    elias "À entendre quelque chose qui ne nous plaira pas."

    pause 0.6

    hide iris
    hide elen
    $ showP("sael", "mefiant", 0.60)

    sael "Hm."
    sael "C’est fou comme ça me rassure."
    sael "J’adore commencer mes matinées avec une menace inconnue."

    hide ryn
    $ showP("nyra", "taquin", 0.95)

    nyra "Pareil."
    nyra "Ça me rappelle le boulot."
    nyra "Sauf qu’ici, on n’est même pas payés."


    hide sael
    $ showP("iris", "desaccord", 0.50)
    iris "Et on ne peut même pas partir."

    nyra raison "Hé."
    nyra raison "Ce ne sont que des détails."

    pause 0.6

    "La porte s'ouvre une première fois."

    hide nyra
    $ showP("mara", "neutre", 0.90)

    play sound sfx_door
    mara "Vous parlez beaucoup."
    mara "On vous entend depuis le couloir ..."
    mara "Ça ne changera rien à ce qui va être dit."

    hide iris
    $ showP("elen", "joie", 0.40)

    elen "Oh Mara !"
    elen "Tu veux t’asseoir avec nous ?"

    mara "Je suis très bien là."
    mara "Je préfère voir tout le monde."

    pause 0.4

    $ showP("ryn", "desaccord", 0.80)

    ryn "Tu vois."
    ryn "Même elle a compris."
    ryn "Observer, noter, attendre que ça pète."

    mara "Ce n’est pas ce que j’ai dit."

    ryn "C’est ce que j’ai entendu."

    pause 0.6

    play sound sfx_door

    hide elias
    $ showP("lysa", "triste", 0.10)

    lysa "… Désolée pour le retard."

    hide elen
    hide ryn
    $ showP("tomas", "hesitation", 0.60)

    tomas "N-Non non !"
    tomas "Enfin, y a pas de problème, hein."

    lysa "Je n’avais pas envie de revenir ici."
    lysa "Pas tout de suite."

    noam "Je comprends."

    pause 0.4

    play sound sfx_door

    hide mara
    $ showP("kael", "neutre", 0.86)

    kael "…"
    kael "Tout le monde est là ?"
    kami "On est presque 9h."

    hide tomas
    $ showP("iris", "neutre", 0.50)
    iris "Franchement, j'ai la flemme de compter."
    iris "On va dire que oui."

    kael "Bien."

    "Et puis ce son, le même que ce matin retentit à nouveau."
    play sound sfx_announce

    pause 2.0

    stop music fadeout 0.8
    pause 0.6

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh."
    kami "Quelle belle image."
    kami "Des visages tendus, des regards méfiants…"
    kami "On dirait presque une réunion de famille ratée."
    kami "Qui a osé parler de politique ou d'argent ?!"

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Jour deux."
    kami "Il est neuf heures."
    kami "Et vous êtes tous ..."
    kami "Ah non. Il manque quelqu'un."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Et bien tant pis pour le retardataire :"

    pause 0.4

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "J’adore quand vous essayez d'anticiper."
    kami "Quand vous essayez de deviner."
    kami "Ça vous rend… délicieusement prévisible."

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn "Bla bla bla ..."
    ryn "Elle va y venir ou pas ?"
    $ bc_hide()

    kami "Oh."
    kami "L’impatience."
    kami "Un si joli défaut."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais moi contrairement à vous, j'ai tout mon temps !"

    pause 0.6

    kami "Le premier vote du Conclave a été tiré au sort."

    $ bc_show("tomas", "surpris", px=-70, py=-50, pz=0.85)
    tomas "D-Déjà ?!"
    $ bc_hide()

    kami "Oui."
    kami "Déjà."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Je suis efficace. MOI."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'avais peur que vous vous ennuyiez ici."
    kami "Je vous donne un sujet de discussion."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Et voici le résultat tant attendu."
    kami "La proposition pour laquelle vous devrez voter ..."
    kami "Attention, roulement de tambour !"

    play sound sfx_tambour
    pause 2.0

    kami "Autoriser le transport, la vente et l'échange de marchandises au sein des districts."

    pause 0.8

    $ bc_show("sael", "surpris", px=-70, py=-50, pz=0.85)
    sael "C'est honnêtement pas si mal."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra "Hé."
    nyra "C’est mieux que ‘qui on sacrifie en premier’, non ?"

    $ bc_show("iris", "sourire", px=-70, py=-50, pz=0.85)
    iris "Ne dis pas ça."

    $ bc_show("nyra", "sourire", px=-70, py=-50, pz=0.85)
    nyra "Quoi ?"
    nyra "Je pose la question."
    $ bc_hide()

    pause 0.6

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais ils vont me laisser parler ces petits cons ?!"

    pause 0.4
    "Tout le monde s'est tu instantanément."
    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Habituellement vous auriez eu trois jours pour discuter de cette proposition."
    kami "Pour discuter."
    kami "Pour convaincre les autres."
    kami "Ou pour vous détester un peu plus."
    kami "Ca c'est de votre ressort."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais nous sommes déjà au jour 2."
    kami "Or le premier vote a lieu à la fin du troisième jour !"
    kami "Vous n'avez donc qu'une journée pour vous décider."
    kami "Mais zen. Vous allez y arriver."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je rappelle que le vote devra être unanime."

    $ bc_show("elen", "determine", px=-70, py=-50, pz=0.85)
    elen "Unanime comme… tout le monde d’accord ?"
    elen "Tout le monde doit voter pour ?"
    $ bc_hide()

    kami "Exactement. Enfin presque."
    kami "Disons plutôt que personne ne doit voter contre."
    kami "L'abstention ne compte pas et si quelqu'un ne vote pas, c'est pareil."
    kami "Si la moindre personne vote contre. La proposition tombe à l'eau."

    pause 0.6

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Amusez-vous bien."
    kami "Je vous écoute."

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    pause 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showP("tomas", "inquiet", 0.10)

    tomas "…"
    tomas "C’est… c’est sérieux, là."

    $ showP("iris", "colere", 0.50)
    iris "Non."
    iris "C’est pire."

    $ showP("ryn", "determine", 0.86)
    ryn "Parfait."
    ryn "Enfin ça commence."

    hide tomas
    $ showP("elen", "inquiet", 0.15)

    elen "On pourrait… peut-être en parler calmement ?"
    elen "Tous ensemble ?"

    hide ryn
    $ showP("sael", "mefiant", 0.70)

    sael "Adorable."
    sael "Vraiment."

    hide iris
    $ showP("mara", "neutre", 0.60)

    mara "Ça va laisser des traces."

    hide sael
    $ showP("kael", "neutre", 0.86)

    kael "Oui."
    kael "Et pas seulement économiques."

    pause 0.6

    play sound sfx_door
    "Et puis la porte claque une dernière fois."
    "Tout le monde se retourne pour la regarder"

    hide elen
    hide mara
    hide kael
    $ showP("julian", "taquin", 0.50)

    julian "Salut tout le monde."
    julian "J’ai raté quoi ?"

    $ showP("nyra", "taquin", 0.10)

    nyra "Boooh trois fois rien."
    nyra "Juste l'annonce du vote."
    nyra "Tu sais, celui qui aura lieu demain."
    nyra "La joie. Quoi."

    julian "Oh."
    julian "J’adore quand ça commence comme ça."

    noam "Bienvenue au Conclave."
    noam "Je crois bien que c'est notre quotidien désormais."

    pause 0.6

    julian "Et sinon ?"

    $ showP("iris", "desaccord", 0.75)
    iris "Non mais franchement Julian, tu peux pas débarquer ici la bouche en coeur et demander à ce qu'on te fasse un récap."

    julian decu "Et pourquoi pas ?"
    julian decu "Tu pourrais le dire à ton meilleur ami ?"

    iris sourire "Toi ?! Mon meilleur ami ?!"
    iris taquin "Laisse moi rire !"

    julian sourire "Bon, très bien."
    julian sourire "Alors je vais deviner."
    julian taquin "J'adore ce jeu là !"

    julian reflexion "Donc réfléchissons. Kami a annoncé un vote."
    julian reflexion "Vu vos têtes ..."

    "Il prends du temps et regarde curieusement chacun des visages de la salle."

    julian reflexion "La proposition qui est faite n'est pas si mauvaise."
    julian sourire "Si je devais deviner je dirais que c'est une proposition pour faciliter le commerce !"

    iris intervention "... Euh ? Comment tu as ..."

    julian taquin "J'ai toujours eu un bon troisième sens ..."

    $ showP("elias", "rire", 0.20)

    elias "Quel beau parleur !"
    elias "Il y a des écrans partout dans le bâtiment."
    elias "A tous les coups, la diffusion s'est retransmise partout."

    julian panne "..."
    julian decu "Sérieux, Elias ! Fallait me laisser mon heure de gloire ..."
    julian panne "..."
    julian decu "Bon ok j'ai tout entendu, pas besoin de récap ..."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m15
# Total : 1h 10m 40s

label _2_CAFETERIA_POST_ANNONCE:

    "Le silence qui suit est plus lourd que l'annonce."
    "Pas parce qu'elle est violente."
    "Mais parce qu'elle ressemble presque à une respiration."
    "Une parenthèse, un espoir que tout ne dégénèrera pas."

    hide nyra
    hide elias
    $ showP("kael", "neutre", 0.15)
    kael "Sur le papier, c’est simple."
    kael "Autoriser les échanges."
    kael "On pourrait presque dire que ce n’est pas une révolution."

    hide julian
    $ showP("mara", "neutre", 0.50)
    mara "Ça en devient suspect."
    mara "Kami ne ferait jamais ça pour nous faire plaisir."

    hide iris
    $ showP("sael", "mefiant", 0.86)
    sael "Ou elle sait qu’on a besoin d’un os à ronger."
    sael "Pour calmer la panique et la colère de la foule."

    kael "Ce n'est pas Kami qui a décidé de cet amendement. C'est l'un d'entre nous."
    kael "Il y a un risque qu'il y ait un piège."
    kael "La question, c’est de savoir où il est."

    mara "Le piège, c’est nous."
    mara "On a nos districts, nos besoins, nos secrets."

    hide sael
    $ showP("nyra", "raison", 0.86)

    nyra "Je suis d’accord."
    nyra "C’est l’amendement le moins explosif qu’on pouvait se prendre."
    nyra "C’est presque… consensuel."

    kael "Ce qui n’est pas une bonne nouvelle."

    nyra "Tu veux dire que c’est trop beau ?"

    hide mara
    $ showP("iris", "neutre", 0.50)

    iris "Réfléchis deux secondes."
    iris "Nous donner l'espoir que tout va bien se passer pour qu'on baisse notre garde."
    iris "C'est typiquement ce que pourrait faire Kami !"
    iris "Et ça veut dire qu’on va devoir discuter du reste ensemble."
    iris "L'enfer quoi."

    nyra taquin "Tu dis ça comme si c’était la première fois."

    iris "La première fois que j'ai à débattre de ce qui pourrait causer la fin du monde ? Ouai c'est ma première fois.."

    kael "On ne peut pas vraiment esquiver."
    kael "Demain, il va falloir faire le bon choix et voter."

    hide nyra
    $ showP("elen", "inquiet", 0.86)

    elen "On peut essayer d’être d’accord, non ?"
    elen "Juste une fois."
    elen "Pour ne pas leur donner ce qu’ils veulent."

    iris "Ils veulent du spectacle."

    elen "Franchement, la proposition n'a pas l'air mauvaise non ?"

    "Personne ne répond vraiment mais d'un autre côté personne ne proteste."

    hide elen
    $ showP("sael", "mefiant", 0.86)

    sael "Touchant."
    sael "Mais on verra demain."

    kael "Demain, c’est tard."
    kael "On doit se parler aujourd’hui."

    sael "Tu veux dire quoi ?"
    sael "Qu’on fasse une réunion ?"

    iris "C'est pas ce qu'on fait déjà ?!"

    hide iris
    $ showP("tomas", "reflechit", 0.50)

    tomas "Je…"
    tomas "Je pense que c’est important."
    tomas "Parce que ça touche nos districts."
    tomas "Et si on peut faire circuler des choses…"
    tomas "Alors on peut aussi s’entraider, non ?"

    kael "Tu penses à quoi ?"

    tomas "Aux médicaments."
    tomas "Aux matériaux."
    tomas "Pourquoi pas aux gens, aussi."

    sael "Les gens, c’est autre chose."
    sael "La proposition parlait des échanges dans les districts, pas d'autoriser les gens à changer de district."

    tomas "Je sais ..."
    tomas "M-Mais si les échanges deviennent autorisés, alors peut être ..."

    hide sael
    $ showP("mara", "neutre", 0.86)

    mara "C’est bien beau tout ça mais qui contrôlera ces échanges ?"

    tomas "On n’a pas les détails."

    kael "Justement."
    kael "On devra décider sans."

    mara "Décider à l’aveugle, ou presque."

    tomas "Alors on doit se faire confiance."

    hide tomas
    $ showP("nyra", "raison", 0.50)

    nyra "On pourrait commencer par lister ce qu’on sait."
    nyra "Et ce qu’on ignore."
    nyra "Parce que là, on se jette des impressions sans grande certitude."
    nyra "C'est pas comme ça qu'on avancera ..."

    mara "Tu as de quoi écrire un roman entier sur ce qu'on ignore ?"

    nyra "Je veux une base."

    kael "Elle a raison."
    kael "Sinon on va se bouffer."

    hide mara
    $ showP("elen", "inquiet", 0.86)

    elen "Je peux prendre des notes."
    elen "Ca me rassure de garder des notes sur mon travail."
    elen "D'une certaine façon ... On travaille ..."

    nyra "Tu vois, c’est utile."

    elen "Je ne sais pas, ça me rassure."

    hide kael
    $ showP("iris", "neutre", 0.15)

    iris "Bon."
    iris "On a trois trucs :"
    iris "On veut pas se faire piéger."
    iris "On veut pas trahir nos districts."
    iris "Et si possible on veut éviter de se détester."

    nyra "Ça fait beaucoup de voeux."

    iris "On a que ça."

    elen "On a une journée seulement pour nous décider."

    hide elen
    hide nyra
    $ showP("julian", "taquin", 0.86)

    julian "Alors on fait quoi ?"
    julian "On se réunit, on se parle, on signe un pacte ?"

    iris "On se parle."
    iris "Le reste, on verra."

    julian "Ok."
    julian "Mais faut pas juste tourner en rond, faut avancer."

    iris "Tu proposes quoi ?"

    julian "Une sorte de plan."
    julian "On se répartit les questions."
    julian "Chacun réfléchit et on revient."

    iris "Réfléchir, c’est facile."
    iris "Revenir, c’est autre chose."

    julian "T’as peur de qui ?"

    iris "Des gens qu'on risque de tuer ..."

    hide julian
    $ showP("sael", "mefiant", 0.86)

    sael "Partager, ça se paye."
    sael "Toujours."

    iris "Et si on refuse ?"

    sael "Il suffit d'une voix contre pour que ça parte en couille."
    sael "On laisse ceux qui veulent se vendre le faire."

    iris "Tu dis ça comme si c’était simple."

    sael "Rien n’est simple."
    sael "Mais refuser, c’est aussi un choix. Un choix qui a des conséquences."

    hide sael
    $ showP("mara", "neutre", 0.86)

    mara "On n’aura pas forcément la même position de vote."
    mara "Certains de nos districts n’ont rien en commun. Notre histoire est différente. Notre mode de vie aussi."
    mara "D’autres en ont trop."
    mara "Et là, d’un coup, on nous demande de trouver un équilibre dans tout ce foutoir ?!"

    $ showP("nyra", "neutre", 0.55)
    nyra "Donc on doit parler d’inégalités."

    mara "Exactement."
    mara "Et on n’a même pas le droit d’en parler avec les gens de nos districts."

    nyra "Ça va être beau."

    hide nyra
    $ showP("tomas", "inquiet", 0.15)

    tomas "On est obligés de parler de nos districts ?"
    tomas "E-Enfin je veux dire, bien sur qu'on veut les défendre mais ..."

    hide mara
    $ showP("elen", "triste", 0.86)

    elen "On a tous peur de choisir."
    elen "Mais on choisit déjà."
    elen "Quand on parle."
    elen "Quand on se tait."

    tomas "Je sais."
    tomas "Je sais."

    hide tomas
    $ showP("kael", "neutre", 0.15)

    kael "Si on ne se parle pas ici, on va se parler derrière."
    kael "Et là, ça devient dangereux."

    elen "Alors on fait comment ?"

    kael "On propose une méthode."
    kael "Et on la tient."

    elen "Une méthode ?"

    kael "On fait une liste."
    kael "On précise les besoins."
    kael "On ne discute pas des échanges tant qu’on n’a pas la carte."

    hide elen
    $ showP("nyra", "raison", 0.86)

    nyra "Et qui fait la carte ?"

    kael "Nous."
    kael "Chacun pour son district."

    nyra "Et ceux qui ne veulent pas se dévoiler ?"

    kael "On les écoute."
    kael "Mais on leur dit que demain, ça s’impose."

    hide kael
    $ showP("iris", "neutre", 0.15)

    iris "Je déteste quand c’est raisonnable."

    nyra "Tu préfères quand c’est violent ?"

    iris "Je préfère quand je comprends."

    nyra "Alors on va parler."

    hide nyra
    $ showP("julian", "reflexion", 0.86)

    julian "Je peux résumer ?"
    julian "On s’organise."
    julian "On dit ce qu’on peut offrir."
    julian "Et on essaye de ne pas se juger."

    iris "Ça va être le plus dur."

    julian "Je sais."

    hide julian
    $ showP("mara", "neutre", 0.86)

    mara "Et pendant qu’on discute…"
    mara "Kami nous écoute."
    mara "Elle notera qui craque."

    iris "Alors on ne craque pas."

    mara "Plus facile à dire."

    hide mara
    $ showP("sael", "mefiant", 0.86)

    sael "Je propose qu’on fasse ça en deux temps."
    sael "D’abord les besoins, ensuite les échanges."
    sael "Et sans promesse aujourd’hui."

    iris "Je signe."

    kael "Moi aussi."

    nyra "Pareil."

    elen "Oui."

    tomas "D’accord."

    sael "Bien."
    sael "On se pose quand ?"

    kael "Après le déjeuner."
    kael "Une heure ou deux."

    sael "On a une salle ?"

    iris "La salle commune."

    kael "S’ils ne nous la ferment pas."

    hide sael
    $ showP("tomas", "inquiet", 0.86)

    tomas "Et si quelqu’un refuse ?"

    iris "On ne l’oblige pas."

    kael "Mais on lui laisse une place."

    tomas "Ok."

    hide tomas
    $ showP("nyra", "raison", 0.86)

    nyra "Et si quelqu’un profite ?"

    iris "On le verra."

    kael "Et on le dit."

    nyra "Donc on fait ça."

    kael "Oui."

    pause 0.6

    "Le bruit reprend doucement."
    "Des chaises raclent."
    "Des plateaux s’éloignent."
    "Ce n’est plus un silence."
    "C’est un mouvement."

    hide iris
    hide kael
    hide nyra
    hide sael

    $ showP("ryn", "neutre", 0.15)

    ryn "On dirait que vous avez déjà décidé."

    noam "On a juste cherché un cadre."

    ryn "Un cadre, c’est déjà un camp."

    noam "Tu veux t’en faire un autre ?"

    ryn "Je veux éviter de me faire piéger."

    noam "Moi aussi."

    hide ryn

    "Je sens les regards qui glissent."
    "Chacun se repositionne."
    "Des alliances silencieuses."
    "Des distances nouvelles."
    "Je comprends que la matinée est finie."
    "Mais pas la tension."
    "Elle reste accrochée aux épaules."
    "Elle s’invite dans les gestes."
    "Dans les pauses trop longues."
    "Dans les sourires qui veulent rassurer."
    "Je sens mes mains se crisper."
    "Je les ouvre."
    "Je les referme."
    "Je me force à marcher."
    "À ne pas rester planté."
    "À ne pas chercher des réponses là où il n’y en a pas."

    stop music fadeout 0.8
    pause 0.6

    "Le reste de la matinée glisse sans moi."
    "Des pas, des couloirs, des horaires qui se rangent tout seuls."
    "Je me surprends à écouter."
    "Pas les mots."
    "Les respirations."
    "Celles qui s’accélèrent."
    "Celles qui se cassent."
    "Celles qui se contrôlent."
    "Je devine les tempêtes."
    "Je devine les résistances."
    "Je ne sais pas qui va craquer."
    "Je ne sais pas si ce sera moi."

    jump _2_APRES_MIDI

label _2_APRES_MIDI:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "L’après-midi commence sans véritable signal."
    "Je traverse un couloir étroit."
    "Le sol est propre. Trop propre."

    $ showP("mara", "neutre", 0.30)
    $ showP("sael", "mefiant", 0.70)

    mara "Tu crois vraiment qu’ils vont nous laisser voter tranquille ?"
    mara "Sans nous souffler la réponse ?"

    sael "Je crois qu’ils vont surtout nous regarder nous disputer."
    sael "Et ça leur ira très bien."

    mara "Toujours aussi optimiste."

    sael "Toi aussi."

    "Elles échangent un sourire bref."
    "Froid."
    "Presque complice."

    mara "On se retrouve plus tard."

    sael "Si on n’explose pas d’ici là."

    hide mara
    hide sael

    "Je les laisse derrière."
    "Direction la salle d’observation."
    "Sur le chemin, des voix me frôlent."
    "Des morceaux de phrases."
    "Des hypothèses."
    "Des promesses qu’on n’ose pas dire."

    "Je tourne au bout du couloir."
    "Lysa est adossée au mur, les bras croisés."
    "Elias lui parle doucement."

    $ showP("lysa", "triste", 0.30)
    $ showP("elias", "neutre", 0.70)

    elias "Tu n’es pas obligée de rester seule."

    lysa "Je ne suis pas seule."
    lysa "Je me protège."

    elias "Tu te coupes."

    lysa "Je me repose."

    elias "Ça ne ressemble pas à du repos."

    lysa "Toi, tu appelles comment ce qu’on fait ?"
    lysa "Ce va-et-vient, ces discussions, ces regards."
    lysa "Moi j’appelle ça survivre."

    elias "C’est pareil."
    elias "Mais tu peux survivre avec nous."

    lysa "Avec nous."
    lysa "Qui est nous ?"

    elias "Tous."

    lysa "Tous, ça n’existe pas."
    lysa "Pas ici."

    noam "Tu ne crois pas qu’on peut y arriver ?"

    lysa "Je crois qu’on va essayer."
    lysa "Et qu’on va se faire mal."

    elias "On va se faire mal de toute façon."
    elias "Autant choisir comment."

    lysa "Tu dis ça comme si on avait la main."

    elias "On a au moins un doigt."

    lysa "Je ne suis pas certaine de vouloir l’utiliser."

    noam "Tu as peur ?"

    lysa "Oui."
    lysa "Et toi ?"

    noam "Oui."

    lysa "Alors ne fais pas semblant d’être solide."

    noam "Je ne fais pas semblant."

    lysa "Si."
    lysa "Tu fais semblant pour que les autres tiennent."

    elias "Elle n’a pas tort."

    noam "Je ne sais pas faire autrement."

    lysa "Moi non plus."

    elias "Tu n’es pas obligée de parler à la réunion."

    lysa "Je sais."
    lysa "Mais si je ne parle pas, on parlera pour moi."

    elias "Tu veux dire quoi ?"

    lysa "Que mon district a une réputation."
    lysa "Et qu’elle me colle."

    noam "Tu n’es pas une réputation."

    lysa "Dis-le à ceux qui ne me connaissent pas."

    elias "Alors présente-toi."

    lysa "Ce n’est pas si simple."

    elias "Rien ne l’est."

    lysa "Je sais."
    lysa "C’est ça le problème."

    noam "Tu veux qu’on reste ?"

    lysa "Je veux que vous compreniez."
    lysa "Je suis fatiguée de devoir expliquer."

    elias "Tu n’as pas à tout expliquer."
    elias "Tu peux dire l’essentiel."

    lysa "L’essentiel ?"
    lysa "Que nos rations sont déjà basses."
    lysa "Que les hôpitaux ferment."
    lysa "Que nos dirigeants mentent."

    elias "Dis-le."

    lysa "Et après ?"
    lysa "On va me dire qu’on a tous des problèmes."

    elias "Et ce sera vrai."

    lysa "Alors à quoi bon ?"

    noam "À ne pas être seule avec ça."

    lysa "Tu crois que ça change quelque chose ?"

    noam "Je ne sais pas."
    noam "Mais je ne veux pas qu’on te fasse taire."

    lysa "Je ne me tais pas."
    lysa "Je choisis mes mots."

    elias "C’est déjà beaucoup."

    lysa "Toi aussi, tu vas parler ?"

    elias "Je vais écouter."
    elias "Et je dirai ce que je dois."

    lysa "Tu as toujours l’air d’avoir un devoir."

    elias "C’est mon problème."

    lysa "C’est aussi le nôtre."

    elias "Je le sais."

    lysa "Alors ne te sacrifies pas."

    elias "Je ne me sacrifie pas."
    elias "Je suis là."

    lysa "C’est déjà un sacrifice."

    noam "On y va ?"

    lysa "Oui."
    lysa "Je vais venir."
    lysa "Mais si je sors, je ne veux pas qu’on me fasse dire plus."

    elias "Promis."

    noam "Promis."

    hide lysa
    hide elias

    "Elle se redresse."
    "Elle inspire."
    "Et elle marche."
    "Je la suis des yeux un instant."
    "C’est une décision minuscule."
    "Mais je sais ce que ça lui coûte."

    scene bg_observation at adaptive_fullscreen with dissolve

    "La baie vitrée donne sur le vide."
    "Un noir immense, calme, presque apaisant."
    "Kael est déjà là."
    "Debout, les mains dans le dos."

    $ showP("kael", "neutre", 0.50)

    noam "Tu sais où on est ?"
    noam "Enfin… précisément."

    kael "Non."
    kael "Mais je reconnais des pièces."
    kael "Du matériel Orbite."

    noam "Donc on est bien proches de chez toi."

    kael "Ou on nous a recyclés à partir de là-bas."
    kael "Ce qui revient presque au même."

    noam "Ça te rassure ?"

    kael "Ça me met en colère."
    kael "Parce que ça veut dire qu’ils avaient tout prévu."
    kael "Le lieu, le calendrier, nos réactions."

    noam "Tu crois qu’ils ont prévu le vote aussi ?"

    kael "Ils l’ont fabriqué."
    kael "Pour que ça paraisse raisonnable."
    kael "Et pour que nous nous divisons sur des détails."

    noam "On n’est pas encore divisés."

    kael "On l’est déjà."
    kael "La peur ne met pas les mêmes mots dans toutes les bouches."

    noam "Tu parles comme si tu avais déjà choisi."

    kael "Non."
    kael "Je me prépare."
    kael "C’est différent."

    pause 0.6

    play sound sfx_announce
    pause 0.8

    stop music fadeout 0.6
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit rappel."
    kami "Le vote aura lieu demain."
    kami "Quatorze heures."
    kami "Soyez ponctuels."
    kami "Et soyez unanimes."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    noam "Quatorze heures."
    noam "C’est proche."

    kael "C’est voulu."
    kael "Ils veulent qu’on manque de temps."

    noam "Tu penses qu’on peut tenir un consensus ?"

    kael "On peut tenir une ligne."
    kael "Pas forcément une paix."

    noam "Quelle ligne ?"

    kael "Le respect."
    kael "Si on le perd, on est fichus."

    noam "Tu crois que tout le monde peut faire ça ?"

    kael "Non."
    kael "Mais si on commence par les écouter, peut-être."

    hide kael

    "Je reste un instant face au vide."
    "Je me surprends à vouloir y lire une réponse."
    "Mais il n’y a que le noir."
    "Et ce silence qui fait trop de place."
    "Je compte mes respirations."
    "Trois."
    "Cinq."
    "Sept."
    "Je m’arrête."
    "Je me sens idiot."
    "Je recommence."
    "La routine rassure."
    "Même inventée."
    "Même bancale."
    "Je pense à Juliette."
    "À sa manière de répéter les mêmes chansons."
    "Elle disait que ça chassait les cauchemars."
    "Moi, ça chasse quoi ?"
    "L’inquiétude ?"
    "La honte ?"
    "Ou juste le bruit ?"
    "Je n’ai pas la réponse."
    "Je me contente d’un souffle."
    "Un autre."
    "Et j’avance."

    pause 0.6

    scene bg_gymnase at adaptive_fullscreen with dissolve

    "Je passe par la salle de sport."
    "Le bruit des machines couvre tout."
    "Iris enchaîne les répétitions."
    "Elias compte à voix basse, concentré."

    $ showP("iris", "determine", 0.35)
    $ showP("elias", "neutre", 0.65)

    iris "Encore."
    iris "Plus vite."

    elias "Respire."
    elias "C’est pas une course."

    iris "Justement."
    iris "J’ai besoin de sentir que ça bouge."

    elias "On bouge tous."
    elias "Mais pas forcément dans la bonne direction."

    iris "Parle pour toi."
    iris "Moi je sais où je vais."

    elias "Tu vas où ?"

    iris "Vers demain."
    iris "Vers leur foutu vote."
    iris "Pour leur montrer qu’on n’est pas des figurants."

    elias "Être un figurant, ça fait mal."
    elias "Mais être une cible, c’est pire."

    iris "Tu me dis d’être prudente ?"

    elias "Je te dis d’être lucide."

    iris "Je le suis."
    iris "C’est pour ça que je tape plus fort."

    elias "Tu te fais mal."

    iris "J’ai besoin de quelque chose de clair."
    iris "De net."
    iris "Les mots, c’est flou."

    elias "Les mots peuvent tenir debout."
    elias "Si on les pose bien."

    iris "Et si on les pose mal ?"

    elias "Alors on s’excuse."
    elias "Et on recommence."

    pause 0.6

    "Je les salue d’un geste."
    "Ils ne s’arrêtent pas."
    "C’est leur manière de tenir."
    "Je comprends."
    "On tient comme on peut."
    "Avec les bras, avec la voix, avec le silence."
    "Iris tient par la force."
    "Elias par la mesure."
    "Moi, je ne sais pas encore."
    "Alors je regarde."
    "Et je retiens."

    hide iris
    hide elias

    "Je traverse le couloir qui mène à la salle commune."
    "La porte est entrouverte."
    "Des voix calmes."
    "Je décide d’entrer."

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showP("nyra", "sourire", 0.20)
    $ showP("elen", "inquiet", 0.50)
    $ showP("tomas", "inquiet", 0.80)

    nyra "On a dit qu’on commençait par les besoins."
    nyra "Pas par les rêves."

    elen "Mais les rêves, c’est aussi un besoin."

    nyra "Oui."
    nyra "Mais ça ne se pèse pas."

    tomas "On peut dire ce qui manque."
    tomas "Sans dire ce qu’on a."
    tomas "Peut-être."

    nyra "Et comment on échange si on ne sait pas ce qu’on a ?"

    tomas "On peut dire des catégories."
    tomas "Comme ça personne ne se sent trop exposé."

    elen "Des catégories ?"

    tomas "Oui."
    tomas "Alimentation."
    tomas "Médical."
    tomas "Technologie."
    tomas "Éducation."

    nyra "Ça devient un inventaire."

    elen "Ce serait déjà bien."

    nyra "Ce serait dangereux."

    tomas "Pourquoi ?"

    nyra "Parce que ceux qui ont pourront demander des choses en échange."
    nyra "Et ceux qui n’ont rien…"

    elen "On ne les laissera pas tomber."

    nyra "Tu ne peux pas promettre pour tout le monde."

    elen "Je peux promettre pour moi."

    nyra "Et moi, je peux promettre de te rappeler que ça ne suffit pas."

    hide tomas
    $ showP("kael", "neutre", 0.80)

    kael "On ne parle pas de promesse."
    kael "On parle d’un cadre."
    kael "Le but, c’est d’éviter les surenchères."

    elen "On peut décider de limiter."

    nyra "Limiter quoi ?"

    kael "Les demandes."
    kael "Les échanges."
    kael "Une règle simple."

    nyra "Et qui surveille ?"

    kael "On se surveille."

    nyra "C’est ça le piège."

    hide elen
    $ showP("iris", "determine", 0.50)

    iris "Vous parlez comme si on avait le choix."
    iris "Kami nous donne un vote."
    iris "On vote."
    iris "Après, on gère."

    kael "Si on vote oui."

    iris "Et si on vote non, on gère quand même."

    nyra "On gère différemment."

    iris "On gère dans le noir."

    nyra "On est déjà dans le noir."

    kael "On est dans un couloir."
    kael "On peut encore choisir la porte."

    iris "Tu crois que c’est une porte ?"

    kael "C’est ça ou un mur."

    nyra "Arrêtez."
    nyra "On n’a pas besoin d’image."
    nyra "On a besoin d’une décision."

    hide iris
    $ showP("mara", "neutre", 0.50)

    mara "La décision ne peut pas être prise sans informations."
    mara "Et on n’en a pas."

    kael "Alors on en fabrique."

    mara "Ce n’est pas de l’information."
    mara "C’est de la fiction."

    nyra "La fiction, ça tient quand tout s’effondre."

    mara "Ça tient jusqu’à demain."

    tomas "On peut appeler ça un plan."
    tomas "Un plan temporaire."

    mara "Un plan temporaire, c’est un plan quand même."

    pause 0.6

    "Les regards se croisent."
    "On comprend tous qu’on va devoir poser quelque chose."
    "Même si c’est fragile."

    hide nyra
    hide kael
    hide mara

    $ showP("julian", "taquin", 0.20)
    $ showP("elen", "inquiet", 0.50)
    $ showP("tomas", "inquiet", 0.80)

    julian "On peut faire simple."
    julian "On liste les besoins, point."
    julian "Sans chiffres."
    julian "Sans détails."

    tomas "Tu crois que ça suffira ?"

    julian "Ça suffira pour aujourd’hui."
    julian "Demain on improvisera."

    elen "Improviser, ça me fait peur."

    julian "Moi aussi."

    elen "Alors pourquoi tu souris ?"

    julian "Parce que si je ne souris pas, je tremble."

    elen "Je tremble déjà."

    julian "Alors on tremblera ensemble."

    hide julian
    hide elen
    hide tomas

    "La salle commune se remplit petit à petit."
    "Des chuchotements."
    "Des notes griffonnées."
    "Je comprends que chacun trouve sa place."
    "Même ceux qui ne parlent pas."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je repars pour respirer."
    "Dans les couloirs, des regards évitent les miens."
    "Ou s’y accrochent trop fort."
    "On sent les alliances se chercher."
    "Les peurs se répartir."

    $ showP("ryn", "neutre", 0.20)
    $ showP("mara", "neutre", 0.60)

    ryn "Tu vas voter quoi ?"

    mara "Je ne sais pas."

    ryn "Tu sais très bien."

    mara "Je sais ce que je risque."

    ryn "Alors tu sais."

    mara "Et toi ?"

    ryn "Moi, je veux être libre."

    mara "Libre de quoi ?"

    ryn "De devoir quelque chose."
    ryn "De devoir des explications."
    ryn "De devoir une loyauté."

    mara "On est déjà redevables."

    ryn "Pas encore."

    hide ryn
    hide mara

    "Je me surprends à écouter la façon dont les mots tombent."
    "Ils pèsent."
    "Ils restent."
    "Ils collent."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Je termine la journée à la cafétéria."
    "Tout le monde ne mange pas en même temps."
    "Ça vient, ça repart."
    "Des silhouettes, des plateaux, des regards."

    $ showP("kael", "neutre", 0.20)

    kael "À Orbite, on mangeait souvent en décalé."
    kael "Les cycles n’étaient pas les mêmes."
    kael "Le silence faisait partie du travail."

    noam "Tu regrettes ?"

    kael "Ce qui me manque, c’est la routine."
    kael "Pas l’endroit."

    $ showP("nyra", "taquin", 0.80)

    nyra "Orbite, c’était comment ?"
    nyra "On entend tout et n’importe quoi."
    nyra "Des gens qui dorment en apesanteur."
    nyra "Des repas qui flottent."

    kael "On flotte, oui."
    kael "Mais on fait quand même la vaisselle."

    nyra "Quelle déception."

    $ showP("tomas", "curieux", 0.50)

    tomas "Et… euh… vous aviez aussi des médiateurs ?"
    tomas "Des… assemblées ?"

    kael "Pas comme ici."
    kael "On réglait les choses autrement."
    kael "Avec des protocoles."
    kael "Et moins de spectacle."

    noam "Ça te fait quoi de tout revoir ici ?"

    kael "Ça me donne envie de comprendre."
    kael "Et de ne plus obéir par réflexe."

    nyra "Et si tu comprends pas ?"

    kael "Alors j’essaie quand même."

    tomas "Et si on fait une erreur ?"

    kael "On la porte."

    nyra "Ça fait lourd."

    kael "Ça l’est."

    hide nyra
    $ showP("elen", "triste", 0.80)

    elen "Je me demande."
    elen "Si nos familles nous regardent."

    noam "Je me le demande aussi."

    elen "S’ils nous voient, ils doivent avoir peur."
    elen "Et si on vote mal, ils auront plus peur."

    kael "On ne vote pas pour eux."

    elen "Mais ils vivent avec nos décisions."

    kael "Oui."
    kael "C’est ça, être ici."

    elen "Je déteste ça."

    nyra "On déteste tous."

    elen "Alors on fait quoi ?"

    nyra "On tient."

    elen "C’est tout ?"

    nyra "Pour aujourd’hui, oui."

    hide elen
    hide nyra

    $ showP("ryn", "neutre", 0.80)

    ryn "Vous êtes calmes."
    ryn "Je m’attendais à des cris."

    kael "Tu es déçue ?"

    ryn "Non."
    ryn "Les cris viennent après."

    noam "Tu penses qu’on va se déchirer ?"

    ryn "Je pense qu’on va se découvrir."
    ryn "Et ce n’est pas toujours beau."

    kael "On n’est pas obligés d’être beaux."
    kael "On doit être honnêtes."

    ryn "L’honnêteté, c’est dangereux."
    ryn "Elle donne des angles d’attaque."

    noam "Elle donne aussi des points d’appui."

    ryn "Peut-être."
    ryn "Mais je n’ai pas envie d’être un point d’appui."

    kael "Tu veux être quoi, alors ?"

    ryn "Libre."

    kael "Encore."

    ryn "Toujours."

    noam "Tu ne crois pas qu’on puisse être libre ensemble ?"

    ryn "Je ne sais pas."
    ryn "Je n’ai jamais essayé."

    kael "Alors c’est l’occasion."

    ryn "Ou l’erreur."

    noam "Tu vas voter ?"

    ryn "Je vais écouter."
    ryn "Et je déciderai demain."

    kael "Ce sera tard."

    ryn "Ce sera juste."

    noam "Tu refuses de t’engager ?"

    ryn "Je refuse qu’on m’engage."

    kael "Personne ne t’engage."

    ryn "Pas encore."

    noam "Tu as raison d’être prudente."
    noam "Mais si tu ne parles pas, on parlera pour toi."

    ryn "Alors je parlerai."
    ryn "Quand ça comptera."

    kael "Ça compte déjà."

    ryn "Tout compte déjà."
    ryn "Et c’est pour ça que je me tais."

    hide ryn

    "La conversation dérive."
    "D’autres se mêlent à nous."
    "Des questions, des souvenirs, des comparaisons."
    "Puis la fatigue gagne."

    stop music fadeout 1.0
    pause 0.6

    "Je passe par les douches."
    "L’eau est tiède."
    "Juste assez pour effacer le bruit."

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Je me laisse tomber sur le lit."
    "Demain, quatorze heures."
    "Et entre les deux, des paroles à peser."
    "Des accords à construire."
    "Ou à casser."

    $ blink()

    think "Je ferme les yeux."
    think "Et j’essaie de dormir."
