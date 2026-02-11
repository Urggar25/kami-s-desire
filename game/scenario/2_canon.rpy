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
    think "Ça ne me calme pas."
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

    kami "Je vous donne rendez-vous à neuf heures, d’accord ?"
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

    tomas "E-Excusez-moi mais… euh…"
    tomas "On est vraiment obligés d’être tous là… enfin, là, tout de suite ? Je veux dire… maintenant ?"
    
    $ showP("iris", "colere", 0.50)

    iris "Super. Vraiment super."
    iris "Même pas dix minutes et on a déjà droit aux questions à la con. Bravo l’équipe."

    tomas panne "Je— je dis pas que c’est idiot !"
    tomas panne "C’est juste que… enfin… voilà."

    $ showP("ryn", "neutre", 0.86)

    ryn neutre "Non mais laisse."
    ryn reflechit "Au moins lui il parle."
    ryn reflechit "Y’en a qui serrent les dents depuis hier et qui font semblant que tout va bien."

    $ showP("elen", "joie", 0.40)

    elen "Oh !"
    elen "C’est vrai que l’ambiance est un peu chelou ce matin…"
    elen "Mais attends, ils ont changé les plateaux ! Regardez comme ils brillent maintenant, c’est pas dingue ? Ça change tout !"

    iris "Elen."
    iris "On s’en tape complètement des plateaux, là. Sérieux."

    elen desaccord "Oui mais quand même !"
    elen content "N’empêche… peut-être que c’est fait exprès pour nous rebooster un peu le moral, non ?"
    
    ryn fatigue "Ou pour nous faire avaler des conneries plus facilement."

    pause 0.4

    hide tomas
    $ showP("elias", "neutre", 0.15)

    elias "…"
    elias "Ça va arriver, de toute façon."
    elias "Autant être prêts."

    noam "Prêts à quoi, exactement ?"

    elias "Autant se préparer à encaisser ce qu'on va nous balancer."

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
    iris "Et en plus on peut même pas se barrer. Génial."

    nyra raison "Hé."
    nyra raison "Ce ne sont que des détails."

    pause 0.6

    "La porte s'ouvre une première fois."

    hide nyra
    $ showP("mara", "neutre", 0.90)

    play sound sfx_door
    mara taquin "Vous jacassez grave, là."
    mara "On vous entend depuis le couloir, sérieux."
    mara "De toute façon ça changera que dalle à ce qui va tomber."

    hide iris
    $ showP("elen", "joie", 0.40)

    elen "Oh Mara !"
    elen "Viens t’asseoir avec nous, allez ! Ça serait trop cool."

    mara "Je suis très bien là."
    mara "Je préfère voir tout le monde, histoire de voir vos tronches lors de l'annonce."

    pause 0.4

    $ showP("ryn", "desaccord", 0.80)

    ryn "Tu vois."
    ryn "Même elle a compris."
    ryn "Observer, noter, attendre que ça pète."

    mara "Non mais attends, c’est pas ce que j’ai raconté."

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
    tomas "Enfin… y a pas de problème. Vraiment. Aucun problème."

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
    iris "Franchement, j’ai la flemme de compter."
    iris "On va dire que oui, point barre. Ça vous va ?"

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

    $ bc_show("iris", "triste", px=-70, py=-50, pz=0.85)
    iris "Ne dis pas ça. S’il te plaît. Ne. Dis. Pas. Ça."

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
    elen "Unanime… genre vraiment tout le monde doit être d’accord ?"
    elen "Genre 100 % des voix ? Wow, c’est hardcore comme condition…"
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
    iris "C’est pire, on a même pas le temps de réfléchir."

    $ showP("ryn", "determine", 0.86)
    ryn "Parfait."
    ryn "Enfin ça commence."

    hide tomas
    $ showP("elen", "inquiet", 0.15)

    elen "Et si on essayait d’en parler calmement tous ensemble ?"
    elen "Juste… sans s’énerver..."

    hide ryn
    $ showP("sael", "mefiant", 0.70)

    sael "Adorable."
    sael "Vraiment."

    hide iris
    $ showP("mara", "neutre", 0.60)

    mara "Ça va laisser des marques."
    mara "Et pas seulement sur le papier, hein."

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

    julian "Salut la team !"
    julian "J’ai loupé quoi ?"

    $ showP("nyra", "taquin", 0.10)

    nyra "Boooh trois fois rien."
    nyra "Juste l'annonce du vote."
    nyra "Tu sais, celui qui aura lieu demain."
    nyra "La joie. Quoi."

    julian "Oh putain…"
    julian "J’adore quand ça démarre direct en mode drama. Ça sent les bonnes histoires."

    noam "Bienvenue au Conclave."
    noam "Je crois bien que c'est notre quotidien désormais."

    pause 0.6

    julian "Et sinon ? On en est où là, vraiment ?"

    $ showP("iris", "desaccord", 0.75)
    iris "Non mais franchement Julian, tu peux pas débarquer ici la bouche en coeur et demander à ce qu'on te fasse un récap."

    julian decu "Et pourquoi pas, hein ?"
    julian decu "Tu pourrais le dire à ton meilleur pote, non ? Allez, fais-moi plaisir."

    iris sourire "Toi ?! Mon meilleur ami ?!"
    iris taquin "Laisse moi rire !"

    julian sourire "Bon, très bien, j’abandonne."
    julian sourire "Je vais deviner direct. J’adore ce jeu, sérieux."
    julian taquin "Préparez-vous, je sens que je vais taper dans le mille."

    julian reflexion "Donc… on récapitule."
    julian reflexion "Kami balance un vote."
    julian reflexion "À voir vos têtes..."

    "Il prends du temps et regarde curieusement chacun des visages de la salle."

    julian reflexion "Mais attendez… elle est pas si pourrie que ça, la proposition."
    julian sourire "Je parie que c’est un truc pour fluidifier le commerce ! Genre, enfin un peu de vie économique ici !"

    iris intervention "… Euh ? Attends, comment tu… t’as deviné ça toi ?!"

    julian taquin "J’ai toujours eu un sixième sens…"

    $ showP("elias", "rire", 0.20)

    elias "Quel beau parleur, tiens !"
    elias "Y a des écrans partout ici."
    elias "A tous les coups, la diffusion a tourné partout."

    julian panne "…"
    julian decu "Sérieux Elias ? Fallait vraiment me piquer mon moment de gloire comme ça ?"
    julian panne "…"
    julian decu "Pfff… ok j’ai tout capté en fond, inutile de me refaire le film."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m35
# Total : 1h 11m 0s

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
    mara doute "Ça devient louche là."
    mara "Kami fait jamais rien pour nous faire kiffer."

    hide iris
    $ showP("sael", "mefiant", 0.86)
    sael "Ou elle sait qu’on a besoin d’un os à ronger."
    sael "Pour calmer la panique et la colère de la foule."

    kael "Ce n'est pas Kami qui a décidé de cet amendement. C'est l'un d'entre nous."
    kael "Il y a un risque qu'il y ait un piège."
    kael "La question, c’est de savoir où il est."

    mara "Le piège, c’est nous."
    mara "On a nos districts, nos besoins, nos secrets."
    mara "Et nos égos, tant qu’à faire."

    hide sael
    $ showP("nyra", "raison", 0.86)

    nyra "Je suis d’accord."
    nyra "C’est l’amendement le moins explosif qu’on pouvait se prendre."
    nyra "C’est presque… consensuel."

    kael "Ce qui n’est pas une bonne nouvelle."

    nyra "Tu veux dire que c’est trop beau ?"

    hide mara
    $ showP("iris", "intervention", 0.50)

    iris "Réfléchis deux secondes, putain."
    iris "Nous filer l’espoir que tout va bien se passer pour qu’on baisse notre garde…"
    iris "C’est du Kami tout craché, ça ! Nous faire espérer deux secondes pour mieux nous baiser après."

    $ showP("mara", "neutre", 0.90)
    mara taquin "‘Baiser’, hein ? T’as l’air presque impatiente que ça arrive."

    iris "H-Hein ?! Mais va te faire foutre, Mara !"

    mara sourire "Oh je vois que Madame a du vocabulaire."
    mara sourire "Nan merci, vas-y découvre ça en solo, je te regarde faire, hein !"

    $ showP("iris", "desaccord", 0.50)
    iris "Sérieusement…"
    iris "Et ça veut dire qu’on va devoir causer de tout le reste ensemble."
    iris "L’enfer. Littéralement l’enfer sur Terre."

    nyra taquin "Tu dis ça comme si c’était la première fois."

    iris "La première fois que j'ai à débattre de ce qui pourrait causer la fin du monde ? Ouai c'est ma première fois.."

    kael "On ne peut pas vraiment esquiver."
    kael "Demain, il va falloir faire le bon choix et voter."

    hide nyra
    $ showP("elen", "inquiet", 0.86)

    elen "On peut essayer d’être d’accord, non ?"
    elen "Juste une fois. Rien qu’une."
    elen "Pour pas leur filer exactement ce qu’ils attendent de nous."

    iris "Ils veulent du spectacle. Du vrai drama de téléréalité."

    elen "Franchement… la proposition a pas l’air si pourrie que ça, si ?"
    elen "Je veux dire… y a claiiirement pire, non ?"

    "Personne ne répond vraiment mais d'un autre côté personne ne proteste."

    hide elen
    $ showP("sael", "mefiant", 0.86)

    sael "Touchant."
    sael "Mais on verra demain."

    kael "Demain, c’est tard."
    kael "On doit se parler aujourd’hui."

    sael "Tu veux dire quoi ?"
    sael "Qu’on fasse une réunion ?"

    iris "Mais c’est pas déjà ce qu’on fait là depuis le début ou quoi ?!"

    hide iris
    $ showP("tomas", "reflechit", 0.50)

    tomas "Je…"
    tomas "Je pense que c’est important."
    tomas "Parce que ça concerne nos districts. Directement."
    tomas "Et si on peut faire circuler des choses entre nous…"
    tomas "Ben… on peut aussi s’entraider, non ?"

    kael "Tu penses à quoi ?"

    tomas "Aux médicaments."
    tomas "Aux matériaux de construction, ou… ce genre de choses."
    tomas "Pourquoi pas aux gens, aussi. À un moment donné."

    sael "Les gens, c’est autre chose."
    sael "La proposition parlait des échanges dans les districts, pas d'autoriser les gens à changer de district."

    tomas "Je sais…"
    tomas "M-Mais si les échanges deviennent autorisés… alors peut-être que…"
    
    hide sael
    $ showP("mara", "neutre", 0.86)

    mara "C’est mignon tout ça, mais qui va surveiller ces petits échanges ?"

    tomas "On n’a pas les détails."

    kael "Justement."
    kael "On devra décider sans."

    mara "Décider à l’aveugle, ou presque."
    mara "J’adore quand on improvise avec nos vies."

    tomas "Du coup… on doit se faire confiance. Voilà."

    hide tomas
    $ showP("nyra", "raison", 0.50)

    nyra "On pourrait commencer par lister ce qu’on sait."
    nyra "Et ce qu’on ignore."
    nyra "Parce que là, on se jette des impressions sans grande certitude."
    nyra "C'est pas comme ça qu'on avancera ..."

    mara taquin "T’as de quoi pondre un roman sur tout ce qu’on sait pas ?"

    nyra "Je veux une base."

    kael "Elle a raison."
    kael "Sinon on va se bouffer."

    hide mara
    $ showP("elen", "inquiet", 0.86)

    elen "Je peux prendre des notes si vous voulez."
    elen "Ça me calme de tout noter. Ça donne l’impression qu’on bosse vraiment sur un truc important…"
    elen "… et que c’est pas juste du vent."

    nyra "Tu vois, c’est utile."

    elen "Je sais pas… ça me rassure, c’est tout."

    hide kael
    $ showP("iris", "neutre", 0.15)

    iris "Bon. On a trois priorités, ok ?"
    iris "Un : on veut pas se faire baiser."
    iris "Deux : on veut pas trahir nos districts."
    iris "Et trois : si possible, on évite de finir par se détester tous. Ambitieux, je sais."

    nyra "T’as pas oublié la lune dans ta liste aussi ?"

    iris "Sacrément drôle, ouais. À mourir de rire."

    elen "On n’a qu’une journée pour se décider."
    elen "Une seule. C’est hyper court quand on y pense…"

    hide elen
    hide nyra
    $ showP("julian", "taquin", 0.86)

    julian "Bon, on fait quoi concrètement là ?"
    julian "Parce que tourner en rond c’est mignon cinq minutes, mais après ça gave."

    iris "Tu proposes quoi, là, concrètement ? Vas-y, je t’écoute."

    julian "Faut un vrai plan, là."
    julian "Ou alors, on y réfléchit et on met en commun demain."
    julian "Chacun bosse son bout dans son coin, et demain on se retrouve avec du lourd."

    iris "Dire qu’on réfléchit, c’est super facile à balancer."
    iris "Le faire vraiment, par contre… c’est une autre paire de manches."

    julian "T’as peur de qui, là, tout de suite ? Dis."

    iris "Des gens qu'on risque de tuer ..."

    hide julian
    $ showP("sael", "mefiant", 0.86)

    sael "Tout ce qu’on partage ici, ça va nous revenir dans la gueule. Toujours."
    sael "Toujours."

    iris "Et si on refuse ?"

    sael "Il suffit d'une voix contre pour que ça parte en couille."
    sael "On laisse ceux qui veulent se vendre le faire."

    iris "Tu dis ça comme si c’était simple."

    sael "Rien n’est simple."
    sael "Mais refuser, c’est aussi un choix. Un choix qui a des conséquences."

    hide sael
    $ showP("mara", "neutre", 0.86)

    mara agace "On va pas tous voter pareil, soyons sérieux."
    mara "Y a des districts qui ont rien à voir entre eux."
    mara "Nos vies, nos galères, nos habitudes… tout est différent."
    mara "Et d’un coup on nous demande de tomber d’accord ?!"
    mara "Dans ce bordel ? Sérieux ?!"

    $ showP("nyra", "neutre", 0.55)
    nyra "Donc on doit parler d’inégalités."

    mara "Ouais exactement."
    mara "Et on peut même pas checker avec nos potes de district."

    nyra "Ça va être beau."

    hide iris
    $ showP("tomas", "inquiet", 0.15)

    tomas "On est obligés de parler de nos districts ? Genre… en détail ?"
    tomas "E-Enfin je veux dire, bien sûr qu’on veut les défendre, mais…"
    
    hide mara
    $ showP("elen", "triste", 0.86)

    elen "On a tous la trouille de choisir."
    elen "Mais en vrai… on choisit déjà. À chaque fois qu’on parle, la vie n'est qu'une suite de choix !"

    tomas "Je sais."
    tomas "Je sais, oui."

    hide tomas
    $ showP("kael", "neutre", 0.15)

    kael "Si on ne se parle pas ici, on va se parler derrière."
    kael "Et là, ça devient dangereux."

    hide kael
    $ showP("iris", "neutre", 0.15)

    iris "Je déteste quand c’est raisonnable."

    nyra "Tu préfères quand c’est violent ?"

    iris "Je préfère quand je comprends au moins ce qu’on nous demande de faire, merci."

    nyra "Alors on va en parler."

    hide elen
    $ showP("julian", "reflexion", 0.86)

    julian "Je peux résumer vite fait pour qu’on soit tous synchro ?"
    julian "On s’organise."
    julian "On pose clairement ce qu’on peut apporter."
    julian "Et on se juge pas. Promis, je commence."

    iris "Ça va être le plus dur. De loin."

    julian "Ouais, je sais."

    hide julian
    $ showP("mara", "neutre", 0.86)

    mara doute "Et pendant qu’on papote…"
    mara doute "Kami nous mate."
    mara taquin "Elle grave tout : qui parle, qui propose quoi, qui va péter les plombs en premier."

    iris "Alors on craque pas. Personne craque. Ok ?"

    mara "C'est facile à dire."
    mara "Surtout quand tout le monde regarde."

    hide mara
    $ showP("tomas", "inquiet", 0.86)

    tomas "Et si quelqu’un refuse ?"

    iris "On va obliger personne à voter pour. Personne."

    hide nyra
    $ showP("kael", "reflechit", 0.40)
    kael "Mais on lui laisse une place."

    tomas "D-De toute façon on ne sait même pas qui votera contre, si ?."

    "Le bruit reprend doucement."
    "Des chaises raclent, des plateaux s’éloignent."
    "Tout le monde retourne peu à peu à ses occupations."

    hide iris
    hide kael
    hide tomas

    "La matinée est finie, pas la tension, elle, elle reste bien présente."
    "Elle reste accrochée aux épaules."
    "Elle s’invite dans les gestes."
    "Dans les pauses un peu trop longues."
    "Dans les sourires qui veulent rassurer."
    "Je sens mes mains se crisper."
    "Je me force à marcher."
    "À ne pas rester planté là."
    "À ne pas chercher des réponses là où il n’y en a pas."

    stop music fadeout 0.8
    pause 0.6

    "Le reste de la matinée passe rapidement et pendant ce temps là, je me balade pour me changer les idées."
    "Des pas, des couloirs, des respirations."
    "Je ne sais pas qui va craquer."
    "Je ne sais pas si ce sera moi."

    call START_FREE_TIME("_2_APRES_MIDI")

# Durée : 3m50
# Total : 1h 14m 50s

# Freetimde :
# Durée : 1m30
# Total : 1h 16m 20s

label _2_APRES_MIDI:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "L’après-midi commence sans véritable signal."
    "Je marche."
    "Un couloir étroit."
    "Propre."
    "Trop propre."

    $ showP("mara", "neutre", 0.30)
    $ showP("sael", "mefiant", 0.70)

    mara mefiant "Tu penses vraiment qu’ils vont nous laisser voter tranquilles ?"
    mara doute "Sans… orienter un peu ?"

    sael mefiant "Ils n’ont pas besoin."
    sael raison "Ils attendront qu’on le fasse nous-mêmes."

    mara taquin "Toujours aussi rassurante."

    sael neutre "Je fais de mon mieux."

    "Un silence."
    "Bref."

    mara stress "À plus tard."
    mara doute "… si tout a pas déjà explosé d’ici là."

    sael taquin "Si ça lâche, on saura où chercher."

    hide mara
    hide sael

    "Je les laisse derrière."
    "Le couloir continue."
    "Des voix passent."
    "Des mots coupés."
    "Des phrases qu’on ne termine pas."

    "Je tourne."
    "Lysa est adossée au mur."
    "Bras croisés."
    "Elias est face à elle."

    $ showP("lysa", "triste", 0.30)
    $ showP("elias", "neutre", 0.70)

    elias ecoute "Tu devrais en discuter avec nous."
    elias ecoute "Enfin, si tu veux."

    lysa neutre "Tu sais je préfère..."

    elias inquiet "… Faut pas rester toute seule ici."

    lysa blase "Je sais."

    "Un temps."

    elias fatigue "T’as pas beaucoup parlé aujourd’hui…"
    elias fatigue "Tu étais plus bavarde hier…"

    lysa reflexion "J’ai écouté."

    elias neutre "Ce n’est pas très reposant."

    lysa taquin "Rien ici ne l’est."

    elias ecoute "Non."

    lysa reflexion "Tu sais comment j’appelle tout ça ?"
    lysa neutre "Marcher sans trop y penser."
    lysa blase "Avancer sans tomber."

    elias reflechit "Laisse moi deviner..."
    elias neutre "Essayer de survivre."

    lysa surpris "… Oui."
    lysa triste "Voilà."

    "Je m’approche."

    $ showP("noam", "inquiet", 0.10)

    noam hesitation "Ça va ?"

    lysa determine "Ça va comme ça peut."

    elias ecoute "On va avoir besoin de toi."

    lysa opposition "Vous allez surtout parler."
    lysa blase "Moi, on m’écoutera à moitié."

    noam inquiet "Pourquoi tu penses ça ?"

    lysa reflexion "Mon district. Enfin, le notre ..."
    lysa neutre "Les gens entendent avant de regarder."

    elias raison "Alors dis-leur."

    lysa tristesse "Dire quoi ?"
    lysa blase "Qu’on manque déjà de tout ?"
    lysa neutre "Ils le savent."

    noam culpabilite "Je pense que tous les districts ont des problèmes…"

    lysa opposition "Justement."

    "Silence."
    "Lysa regarde le sol."

    elias fatigue "Tu n’es pas obligée de parler à la réunion."

    lysa determine "Si je ne parle pas…"
    lysa reflexion "On parlera pour moi."

    noam hesitation "Tu as peur ?"

    lysa peur "Oui."
    lysa peur "Mais toi aussi."

    noam panne "… Oui."

    lysa neutre "Alors n’essaie pas d’être solide."
    lysa blase "Ça se voit quand ça sonne faux."

    noam culpabilite "Je fais ce que je peux."

    lysa triste "Moi aussi."

    elias ecoute "Tu peux dire l’essentiel."

    lysa reflexion "L’essentiel fait toujours mal."

    elias neutre "Mais il peut rester en mémoire."

    "Lysa souffle."
    "Longuement."

    lysa determine "Je viendrai."
    lysa reflexion "On tirera ça au clair."
    lysa blase "Mais j’ai des réserves sur ce vote…"
    lysa neutre "Si on manque déjà de tout là-bas…"
    lysa reflexion "autoriser les échanges, le commerce…"
    lysa fatigue "ça risque pas d’empirer les choses ?"

    noam raison "C'est possible."
    noam raison "Pour tout te dire, je ne sais pas vraiment."

    lysa regarde "Ne promets pas trop vite."

    noam neutre "On en parlera peut-être demain..."

    lysa hoche "Oui."
    lysa triste "Avant que je change d’avis."
    lysa blase "J’ai pas envie de briser leurs espoirs…"
    lysa determine "mais tu as compris."
    lysa fatigue "... C’est déjà ça."

    $ add_argument("Difficulté d'approvisionnement")
    show screen argument_unlock("Difficulté d'approvisionnement")
    pause 5.0

    tuto "Prêt pour un nouveau tutoriel ?"
    tuto "Au cours de ce dialogue, Lysa a émit des doutes sur le vote à venir."
    tuto "Ces doutes ont muri sous la forme d'un Argument."
    tuto "Au cours du vote, vous aurez à choisir un ou plusieurs arguments à certains moments précis."
    tuto "Ces arguments peuvent convaincre certains personnages, mais aussi en rébuter d'autres."
    tuto "Vous pourrez collecter des arguments en explorant, en discutant avec des personnages ou en progressant dans l'histoire."
    tuto "Alors bonne collecte !"

    hide lysa
    hide elias
    hide noam

    "Elle se redresse."
    "Fais un pas."
    "Puis un autre."

    "Je reste une seconde."
    "Puis je repars en direction de la salle d'observation."

    jump _2_SALLE_OBSERVATION

# Durée : 1m50
# Total : 1h 18m 10s

label _2_SALLE_OBSERVATION:
    scene bg_observation at adaptive_fullscreen with dissolve

    "La baie vitrée donne sur le vide."
    "Un noir immense, calme, presque apaisant."
    "Kael est déjà là."
    "Debout, les mains dans le dos."

    $ showP("noam", "neutre", 0.18)
    $ showP("kael", "neutre", 0.50)

    noam neutre "Ah Kael, tu tombes bien. Je voulais te demander..."
    noam hesitation "Tu sais où on est ?"
    noam hesitation "Enfin… précisément."

    kael neutre "Non."
    kael reflechit "Mais je reconnais des pièces."
    kael reflechit "C'est du matériel qui vient bien d'Orbite."

    noam raison "Donc on est bien proches de chez toi."

    kael doute "Enfin proche ... Tu te rends compte de la taille d’Orbite ?"
    kael doute "On dit souvent que Limen est le plus grand district ... En terme de surface habitée peut-être mais Orbite le surpasse de loin en superficie."
    kael jaloux "J'imagine donc qu'on est quelque part dans mon district."

    noam inquiet "Ça te rassure ?"

    kael colere "Ça me met en colère."
    kael colere "Parce que ça veut dire qu’ils avaient tout prévu."
    kael colere "Le lieu, le calendrier, nos réactions."

    noam inquiet "Tu crois qu’ils ont prévu le vote aussi ?"

    kael mefiant "Je ne sais pas vraiment... Si c'est vraiment nous qui l'avons proposé, peut-être que non."
    kael mefiant "Mais ça ne changera pas grand chose au fond."
    kael mefiant "Nous allons sans doute nous diviser sur des détails."

    noam raison "On n’est pas encore divisés."

    kael colere "On l’est déjà."
    kael colere "Sinon tout le monde aurait accepté de parler hier soir."
    kael colere "La peur ne met pas les mêmes mots dans toutes les bouches."

    pause 0.6

    play sound sfx_announce
    pause 0.8

    stop music fadeout 0.6
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petite annonce, l'un d'entre vous m'a demandé l'heure du vote demain."
    kami "Le vote aura lieu demain à quatorze heure."
    kami "Soyez ponctuels."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Profitez bien de votre douce nuit de réflexion."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showP("noam", "neutre", 0.18)
    $ showP("kael", "neutre", 0.50)

    noam neutre "Quatorze heures."
    noam inquiet "On y sera vite."

    kael mefiant "C’est clair."

    noam inquiet "Tu penses qu’on peut tenir un consensus ?"

    kael raison "Personne n'a l'air d'être particulièrement contre la proposition."
    kael neutre "Alors..."
    kael inquiet "'Fin, peut-être. Je sais pas."
    kael inquiet "Je t'avoue que je ne sais pas trop quoi faire."
    
    noam reflexion "Pourquoi ça ? Chez toi, sur Orbite, comment vous gérez les appros ?"

    kael doute "J'imagine un peu comme partout ailleurs."
    kael doute "Il y a des rations à récupérer chaque jour. Si on veut du matériel spécifique on doit faire une demande officielle et attendre."

    noam reflexion "Ouais, comme partout en fait."
    noam reflexion "Je crois que ça fonctionne comme ça dans tous les districts aujourd'hui ..."

    $ add_argument("Bons de rationnement")
    show screen argument_unlock("Bons de rationnement")

    noam neutre "Si on autorise le commerce, ça pourrait peut-être améliorer les choses, non ?"
    noam reflexion "Ca pourrait redevenir un peu comme avant, avec des magasins, des choses en libre accès."

    kael raison "Ouais, ça se tient."
    kael doute "Mais si il y a la moindre chose qui peut entrainer un tir de laser, c'est extrèmement dangereux."

    noam neutre "Il te suffit pourtant de 'juste' respecter les règles non ?"

    kael colere "Ca ne marche pas comme ça sur Orbite ..."
    kael colere "S-Sur orbite, on vit tous dans des vaisseaux ... au beau milieu de l'espace."

    "Il avale sa salive difficilement, il a du mal à parler."

    kael inquiet "Si quelqu'un fait une connerie, le laser tire ..."
    kael inquiet "Le vaisseau se perce et tout le monde à bord risque de mourir faute d'oxygène ..."

    noam triste "Hein ?!"
    noam triste "Mais c'est pas juste !"

    kael inquiet "Si Kami était juste on le saurait..."
    kael inquiet "Changer, c'est risquer de briser ce quotidien auquel on s'est habitué."
    kael inquiet "Heureusement on y est habitué, et dans toutes les salles on a des masques à oxygène au cas ou ..."
    kael inquiet "Mais ça reste très dangereux."

    "Il s'éloigne de quelques pas."

    kael triste "Excuse moi, je vais faire un tour..."

    $ add_argument("Faiblesse d'Orbite")
    show screen argument_unlock("Faiblesse d'Orbite")

    hide kael
    hide noam

    "Je reste un instant face au vide perdu dans mes pensées."
    "Je compte mes respirations."
    "Je pense à Juliette et à ses chansons horribles à écouter."
    "Et pourtant, là, elles me manquent."
    "Elle disait que ça chassait les cauchemars. J'en aurai bien besoin."
    "Je prends une longue bouffée d'air, puis une autre, et j’avance."

    pause 0.6
    jump _2_GYMNASE

# Durée : 2m15
# Totale : 1h 20m 25s

label _2_GYMNASE:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen with dissolve

    "Je passe par la salle de sport."
    "Le bruit des machines est constant."
    "Métallique."
    "Régulier."

    "Iris enchaîne les répétitions."
    "Sa respiration est courte."
    "Elias compte à voix basse."

    $ showP("iris", "determine", 0.35)
    $ showP("elias", "neutre", 0.65)

    iris determine "Encore."
    iris determine "Allez. Je dois… je dois continuer."
    iris determine "Sans ralentir. Sans m’arrêter. Allez."

    elias ecoute "Respire. C'est le plus important."
    elias ecoute "Sinon tu vas te fatiguer pour rien."

    "Je m’approche."

    noam hesitation "Je dérange ?"

    iris taquin "Tant que tu prends pas ma place."

    elias ecoute "Non."
    elias neutre "Ça tombe bien."
    elias joie "T'as envie d'apprendre à mieux te muscler ?"

    noam surpris "Euh…"
    noam neutre "Je crois."

    iris determine "Alors bouge-toi au lieu de juste mater."
    iris taquin "Ça tombe bien, y a plusieurs bancs qui sont libres là-bas."

    "Elias me désigne un banc."

    elias ecoute "Assieds-toi."
    elias joie "On va commencer simplement."

    "Je m’exécute."
    "Le métal est froid."

    elias raison "Stop. Redresse ton dos, ça ne va pas."
    elias detendu "Expire en poussant, inspire en descendant. Si tu bloques ta respiration, tu vas exploser avant la troisième rep."


    iris taquin "Directement sur le banc de développé-couché ?"
    iris taquin "Le pauvre, il va trembler de tout son corps."

    noam inquiet "Je tremble déjà rien que d'y penser."

    elias ecoute "C'est pas si difficile."
    elias detendu "Ne lutte pas."
    elias detendu "Accompagne le mouvement."

    "Je soulève."
    "C’est bien plus lourd que prévu."

    elias ecoute "Pas comme ça."
    elias detendu "Moins vite."
    elias detendu "Contrôle la descente."

    "Je recommence."
    "Ça brûle."

    iris fatigue "Voilà."

    elias ecoute "Encore deux séries."
    elias detendu "Après tu t’arrêtes."

    tuto "Durant vos temps libres, il sera possible de faire certaines actions qui augmenteront vos statistiques personnelles."
    tuto "Faire du sport est l'une d'entre elles."
    tuto "En faisant du sport, vous lancerez un minijeu qui, si réussit, aura une chance d'augmenter votre statistique Physique."
    tuto "Certaines actions ou certains choix seront bloqués ou débloqués selon ces statistiques secondaires."
    tuto "De plus, pratiquer ce genre d'activité permet de charger des évènements, seuls ou avec d'autres personnages."
    tuto "Ces évènements sont aléatoires et peuvent vous offrir des images... intéressantes."

    noam effort "Un…"
    noam effort "Deux…"

    "Je commence à pousser les altères."

    $ mg_skip_scene_pick = True
    call minijeu_halteres

    "Je repose."
    "Je souffle."
    $ mg_skip_scene_pick = False

    pause 0.6

    elias joie "T’as senti le feu dans les pecs ? C’est ça qui marque."
    elias joie "Mais si tu viens une fois tous les quinze jours, ça repart aussi sec. Le corps oublie pas, il pardonne juste pas."
    elias raison "Moi je viens dès que j’ai un créneau."
    elias raison "En t’entraînant régulièrement, tu rends ton corps et ta tête plus solides."
    elias ecoute "Force, endurance, concentration… tout ça monte."

    iris taquin "Et parfois…"
    iris determine "Ouais. Et des fois, c’est juste pour pas rentrer chez soi et tout péter dans le salon."
    iris taquin "Bref. Soulever de la fonte, c’est moins cher qu’un psy."

    pause 0.4

    noam reflexion "Donc…"
    noam reflexion "Si je ne fais rien…"

    elias neutre "Tu stagneras, et puis t'auras plus de chance d'être en mauvaise santé plus tard."

    "Je regarde mes mains."
    "Elles tremblent encore un peu."

    noam neutre "Je reviendrai."

    iris sourire "Bonne idée."

    elias ecoute "Je serai là."
    elias raison "Mais la prochaine fois, on commence sans que tu trembles avant même de toucher la barre, hein ?" 

    hide iris
    hide elias

    "Je quitte la salle."
    "Les machines continuent de tourner."
    "Régulières."
    "Implacables."

    scene bg_couloir at adaptive_fullscreen with dissolve
    "L'heure tourne et je commence à avoir un petit creux."

    jump _2_CAFETERIA_SOIR

# Durée : 1m50
# Totale : 1h 22m 15s

label _2_CAFETERIA_SOIR:
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Je termine la journée à la cafétéria."
    "Tout le monde ne mange pas en même temps."
    "Ça vient, ça repart."
    "Des silhouettes, des plateaux, des regards."

    $ showP("nyra", "neutre", 0.80)

    "Nyra est en train de parler de sa vie."
    nyra sourire "À Orbite, on mangeait souvent en décalé."
    nyra sourire "Chacun vivait vraiment à son propre rythme, comme dans dessortes de cycles."
    nyra sourire "Le silence faisait partie du travail."

    noam hesitation "Tu regrettes ?"

    $ showP("kael", "neutre", 0.15)
    kael neutre "Ce qui me manque moi, c’est la routine."
    kael neutre "Pas l’endroit, à vrai dire, ça fait du bien de voir autre chose."

    $ showP("elen", "taquin", 0.55)

    elen taquin "Orbite, c’était comment ?"
    elen reflechit "Bah… on entend vraiment de tout et n’importe quoi sur ce qu'il se passe là-haut."
    elen content "Des gens qui dorment en flottant comme des méduses, des repas qui se baladent tout seuls… c’est complètement barré !"

    kael neutre "On flotte, oui."
    kael neutre "Mais on fait quand même la vaisselle, même si parfois c'est galère !"

    nyra taquin "C'est clair !."

    hide elen
    $ showP("tomas", "neutre", 0.50)

    tomas "Et… euh… vous aviez aussi des médiateurs, chez vous ?"
    tomas "Des… assemblées, ou un truc comme ça ? C-Comment vous faisiez pour prendre les décisions ?"

    kael calme "Pas comme ici."
    kael calme "On réglait les choses autrement."
    kael calme "Avec des protocoles."
    kael rire "Et beaucoup moins de spectacle."

    noam inquiet "Ça te fait quoi de tout revoir ici ?"

    kael reflechit "Ça me donne envie de comprendre."
    kael reflechit "Et de ne plus obéir par réflexe."

    nyra raison "Et si tu comprends pas ?"

    kael neutre "Alors j’essaie quand même."

    tomas inquiet "Et si on fait une erreur ..?"

    kael triste "J'imagine qu'on fait tous des erreurs."
    kael triste "A nous de les assumer."

    nyra raison "Autant éviter d'en faire."

    kael neutre "Ça l’est."

    hide tomas
    $ showP("elen", "triste", 0.55)

    elen triste "Je me demande…"
    elen triste "… si nos familles nous regardent en ce moment."

    noam neutre "Je me le demande aussi."

    elen triste "S’ils nous voient, ils doivent flipper grave."
    elen triste "Et si on se plante dans le vote… ils vont flipper encore plus."

    kael reflechit "On ne vote pas uniquement pour eux."

    elen triste "Ouais… mais ce qu’on va décider là, ça va toucher tout le monde. Pas juste nous."

    kael neutre "Oui."
    kael triste "C’est ça, être ici."

    elen triste "Je déteste ça."
    elen triste "Vraiment. Ça me retourne l’estomac."

    nyra raison "Je pense qu'on déteste tous ça."
    nyra raison "On a un travail à faire, c'est tout.."

    elen inquiet "C’est tout ?"

    nyra raison "Pour aujourd’hui, en tout cas."

    hide elen
    hide nyra

    $ showP("ryn", "neutre", 0.80)

    ryn neutre "Vous êtes calmes."
    ryn neutre "Je m’attendais à des cris et des hurlements."

    kael neutre "Tu es déçu ?"

    ryn sourire "Ha ha ! Peut-être un peu !."
    ryn sourire "Mais les cris viendront après."

    noam inquiet "Tu penses qu’on va se déchirer ?"

    ryn reflechit "Je pense qu’on va découvrir les joies des désaccords."
    ryn reflechit "Et ce n’est pas toujours sympa à voir."

    kael reflechit "On n’est pas obligés d’être sympa à voir."
    kael reflechit "On doit surtout être honnêtes."

    ryn fatigue "L’honnêteté, c’est dangereux."
    ryn fatigue "Elle donne des angles d’attaque."

    noam raison "Elle donne aussi des points d’appui."

    ryn reflechit "Peut-être."
    ryn reflechit "Mais je n’ai pas envie d’être un point d’appui."

    kael neutre "Tu veux être quoi, alors ?"

    ryn neutre "Libre. Je veux que les Limenois soient libres."

    noam inquiet "Tu ne crois pas qu’on puisse être libre ensemble ?"

    ryn reflechit "Je ne sais pas."
    ryn reflechit "Ca fait bien longtemps qu'on ne l'est plus, et ça, ça date de bien avant Kami."

    noam raison "Alors c’est l’occasion d'essayer de faire avancer les choses."

    noam hesitation "Qu'est ce que tu vas voter ?"

    ryn reflechit "Je pense que je voterai pour. Je vais écouter."
    ryn reflechit "Et je me déciderai demain."
    ryn reflechit "C'est sans doute mieux comme ça."

    noam raison "Tu as raison d’être prudent."

    hide ryn

    "La conversation dérive."
    "D’autres se mêlent à nous."
    "Des questions, des souvenirs, des comparaisons."
    "Puis la fatigue gagne peu à peu nos esprits."

    stop music fadeout 1.0
    pause 0.6

    scene bg_couloir at adaptive_fullscreen with fade
    pause 1.0
    scene bg_dortoir at adaptive_fullscreen with fade
    pause 1.0
    scene bg_chambre at adaptive_fullscreen with fade
    pause 1.0

    "Je passe par les douches."

    scene bg_cg011 at adaptive_fullscreen with fade

    "L’eau est chaude."
    "Juste assez pour effacer le bruit de mes pensées."

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    scene bg_chambre at adaptive_fullscreen with fade
    "Je me sèche, puis je me laisse tomber sur le lit et j'éteins les lumières."
    
    scene bg_cg012 at adaptive_fullscreen with fade
    "Demain sera dense."
    $ blink()
    "A quatorze heures on en saura enfin plus."
    "On saura si on peut vraiment changer les choses ou pas."

    $ blink()

    think "Je ferme les yeux."
    think "Et j’essaie de dormir."

# Durée : 1m55
# Totale : 1h 24m 10s