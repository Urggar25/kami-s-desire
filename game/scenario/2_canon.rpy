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
    julian decu "Sérieux, Kael ! Fallait me laisser mon heure de gloire ..."
    julian panne "..."
    julian decu "Bon ok j'ai tout entendu, pas besoin de récap ..."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m15
# Total : 1h 10m 40s

label _2_CAFETERIA_POST_ANNONCE:
