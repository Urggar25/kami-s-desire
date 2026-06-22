label _2_CANON:

    $ day_id = 2
    $ current_day = 2

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
    $ unlock_gallery_image("bg_cg012")

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

    call day2_play_wakeup_trace from _call_day2_play_wakeup_trace

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

    menu:
        "Choisir où se placer."
        "Je m'assois près d'une table encore libre.":
            "Je tire une chaise sans bruit."
            "Depuis là, je peux voir presque toute la salle."
        "Rester près du buffet.":
            "Je prends un plateau, plus pour occuper mes mains que pour manger."
            "Les voix me parviennent par morceaux."
        "Me tenir près de l'entrée.":
            "Je reste debout quelques secondes."
            "La porte derrière moi permet de compter ceux qui arrivent."


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "reflexion", 0.13),
        ("iris", "colere", 0.49),
        ("tomas", "neutre", 0.60),
        ("elen", "joie", 0.72),
        ("nyra", "taquin", 0.96),
        ("ryn", "neutre", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas hesitation "E-Excusez-moi mais… euh…"
    tomas inquiet "On est vraiment obligés d’être tous là… enfin, là, tout de suite ? Je veux dire… maintenant ?"
    

    iris desaccord "Super. Vraiment super."
    iris colere "Même pas dix minutes et on a déjà droit aux questions à la con. Bravo l’équipe."

    tomas panne "Je— je dis pas que c’est idiot !"
    tomas panne "C’est juste que… enfin… voilà."


    ryn neutre "Non mais laisse."
    ryn reflechit "Au moins lui il parle."
    ryn reflechit "Y’en a qui serrent les dents depuis hier et qui font semblant que tout va bien."


    elen content "Oh !"
    elen joie "C’est vrai que l’ambiance est un peu chelou ce matin…"
    elen surpris "Mais attends, ils ont changé les plateaux ! Regardez comme ils brillent maintenant, c’est pas dingue ? Ça change tout !"

    iris desaccord "Elen."
    iris colere "On s’en tape complètement des plateaux, là. Sérieux."

    elen desaccord "Oui mais quand même !"
    elen content "N’empêche… peut-être que c’est fait exprès pour nous rebooster un peu le moral, non ?"
    
    ryn fatigue "Ou pour nous faire avaler des conneries plus facilement."

    pause 0.4


    elias ecoute "…"
    elias neutre "Ça va arriver, de toute façon."
    elias ecoute "Autant être prêts."

    noam surpris "Prêts à quoi, exactement ?"

    elias neutre "Autant se préparer à encaisser ce qu'on va nous balancer."

    pause 0.6


    sael raison "Hm."
    sael mefiant "C’est fou comme ça me rassure."
    sael desaccord "J’adore commencer mes matinées avec une menace inconnue."


    nyra raison "Pareil."
    nyra taquin "Ça me rappelle le boulot."
    nyra raison "Sauf qu’ici, on n’est même pas payés."


    iris colere "Et en plus on peut même pas se barrer. Génial."

    nyra raison "Hé."
    nyra raison "Ce ne sont que des détails."

    pause 0.6

    "La porte s'ouvre une première fois."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("iris", "colere", 0.49),
        ("tomas", "panne", 0.60),
        ("elen", "content", 0.72),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])


    play sound sfx_door
    mara taquin "Vous jacassez grave, là."
    mara neutre "On vous entend depuis le couloir, sérieux."
    mara taquin "De toute façon ça changera que dalle à ce qui va tomber."


    elen content "Oh Mara !"
    elen joie "Viens t’asseoir avec nous, allez ! Ça serait trop cool."

    mara neutre "Je suis très bien là."
    mara taquin "Je préfère voir tout le monde, histoire de voir vos tronches lors de l'annonce."

    pause 0.4


    ryn neutre "Tu vois."
    ryn reflechit "Même elle a compris."
    ryn neutre "Observer, noter, attendre que ça pète."

    mara colere "Non mais attends, c’est pas ce que j’ai raconté."

    ryn reflechit "C’est ce que j’ai entendu."

    pause 0.6

    play sound sfx_door


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "colere", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "triste", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "panne", 0.60),
        ("elen", "joie", 0.72),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])

    lysa blase "… Désolée pour le retard."


    tomas inquiet "N-Non non !"
    tomas hesitation "Enfin… y a pas de problème. Vraiment. Aucun problème."

    lysa reflexion "Je n’avais pas envie de revenir ici."
    lysa blase "Pas tout de suite."

    noam reflexion "Je comprends."

    pause 0.4

    play sound sfx_door


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "colere", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "hesitation", 0.60),
        ("elen", "joie", 0.72),
        ("kael", "neutre", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])

    kael reflechit "…"
    kael neutre "Tout le monde est là ?"
    kami "On est presque 9h."

    iris colere "Franchement, j’ai la flemme de compter."
    iris desaccord "On va dire que oui, point barre. Ça vous va ?"

    kael reflechit "Bien."

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
    ryn neutre "Bla bla bla ..."
    ryn neutre "Elle va y venir ou pas ?"
    $ bc_hide()

    kami "Oh."
    kami "L’impatience."
    kami "Un si joli défaut."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais moi contrairement à vous, j'ai tout mon temps !"

    pause 0.6

    kami "Le premier vote du Conclave a été tiré au sort."

    $ bc_show("tomas", "surpris", px=-70, py=-50, pz=0.85)
    tomas surpris "D-Déjà ?!"
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
    sael triste "C'est honnêtement pas si mal."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra taquin "Hé."
    nyra taquin "C’est mieux que ‘qui on sacrifie en premier’, non ?"

    $ bc_show("iris", "triste", px=-70, py=-50, pz=0.85)
    iris colere "Ne dis pas ça. S’il te plaît. Ne. Dis. Pas. Ça."

    $ bc_show("nyra", "sourire", px=-70, py=-50, pz=0.85)
    nyra surpris "Quoi ?"
    nyra reflexion "Je pose la question."
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
    elen joie "Unanime… genre vraiment tout le monde doit être d’accord ?"
    elen surpris "Genre 100%% des voix ? Wow, c’est hardcore comme condition…"
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


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "inquiet", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "neutre", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "determine", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas hesitation "…"
    tomas inquiet "C’est… c’est sérieux, là."

    iris desaccord "Non."
    iris colere "C’est pire, on a même pas le temps de réfléchir."

    ryn neutre "Parfait."
    ryn reflechit "Enfin ça commence."


    elen joie "Et si on essayait d’en parler calmement tous ensemble ?"
    elen content "Juste… sans s’énerver..."


    sael raison "Adorable."
    sael mefiant "Vraiment."


    mara taquin "Ça va laisser des marques."
    mara fatigue "Et pas seulement sur le papier, hein."


    kael reflechit "Oui."
    kael colere "Et pas seulement économiques."

    pause 0.6

    play sound sfx_door
    "Et puis la porte claque une dernière fois."
    "Tout le monde se retourne pour la regarder"


    $ showGroup([
        ("elias", "rire", -0.11),
        ("mara", "fatigue", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("julian", "taquin", 0.37),
        ("iris", "colere", 0.49),
        ("tomas", "inquiet", 0.60),
        ("elen", "content", 0.72),
        ("kael", "colere", 0.84),
        ("nyra", "taquin", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    julian rire "Salut la team !"
    julian surpris "J’ai loupé quoi ?"


    nyra raison "Boooh trois fois rien."
    nyra taquin "Juste l'annonce du vote."
    nyra raison "Tu sais, celui qui aura lieu demain."
    nyra surpris "La joie. Quoi."

    julian panne "Oh putain…"
    julian taquin "J’adore quand ça démarre direct en mode drama. Ça sent les bonnes histoires."

    noam colere "Bienvenue au Conclave."
    noam reflexion "Je crois bien que c'est notre quotidien désormais."

    pause 0.6

    julian sourire "Et sinon ? On en est où là, vraiment ?"

    iris colere "Non mais franchement Julian, tu peux pas débarquer ici la bouche en coeur et demander à ce qu'on te fasse un récap."

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


    elias ecoute "Quel beau parleur, tiens !"
    elias neutre "Y a des écrans partout ici."
    elias ecoute "A tous les coups, la diffusion a tourné partout."

    julian panne "…"
    julian decu "Sérieux Elias ? Fallait vraiment me piquer mon moment de gloire comme ça ?"
    julian panne "…"
    julian decu "Pfff… ok j’ai tout capté en fond, inutile de me refaire le film."

    $ j2_vote_codex_unlocked = True
    call screen day2_vote_tablet_notice
    "La tablette vibre une dernière fois, puis le dossier reste disponible dans mes notes."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m35
# Total : 1h 11m 0s

label _2_CAFETERIA_POST_ANNONCE:

    show screen day2_quick_vote_notes

    "Le silence qui suit est plus lourd que l'annonce."
    "Pas parce qu'elle est violente."
    "Mais parce qu'elle ressemble presque à une respiration."
    "Une parenthèse, un espoir que tout ne dégénèrera pas."

    kael reflechit "Sur le papier, c’est simple."
    kael neutre "Autoriser les échanges."
    kael reflechit "On pourrait presque dire que ce n’est pas une révolution."

    mara doute "Ça devient louche là."
    mara taquin "Kami fait jamais rien pour nous faire kiffer."

    sael raison "Ou elle sait qu’on a besoin d’un os à ronger."
    sael mefiant "Pour calmer la panique et la colère de la foule."

    kael neutre "Ce n'est pas Kami qui a décidé de cet amendement. C'est l'un d'entre nous."
    kael inquiet "Il y a un risque qu'il y ait un piège."
    kael reflechit "La question, c’est de savoir où il est."

    mara neutre "Le piège, c’est nous."
    mara taquin "On a nos districts, nos besoins, nos secrets."
    mara neutre "Et nos égos, tant qu’à faire."


    nyra taquin "Je suis d’accord."
    nyra raison "C’est l’amendement le moins explosif qu’on pouvait se prendre."
    nyra colere "C’est presque… consensuel."

    kael neutre "Ce qui n’est pas une bonne nouvelle."

    nyra taquin "Tu veux dire que c’est trop beau ?"


    iris colere "Réfléchis deux secondes, putain."
    iris desaccord "Nous filer l’espoir que tout va bien se passer pour qu’on baisse notre garde…"
    iris colere "C’est du Kami tout craché, ça ! Nous faire espérer deux secondes pour mieux nous baiser après."

    mara taquin "‘Baiser’, hein ? T’as l’air presque impatiente que ça arrive."

    iris surpris "H-Hein ?! Mais va te faire foutre, Mara !"

    mara sourire "Oh je vois que Madame a du vocabulaire."
    mara sourire "Nan merci, vas-y découvre ça en solo, je te regarde faire, hein !"

    iris colere "Sérieusement…"
    iris desaccord "Et ça veut dire qu’on va devoir causer de tout le reste ensemble."
    iris colere "L’enfer. Littéralement l’enfer sur Terre."

    nyra taquin "Tu dis ça comme si c’était la première fois."

    iris desaccord "La première fois que j'ai à débattre de ce qui pourrait causer la fin du monde ? Ouai c'est ma première fois.."

    kael reflechit "On ne peut pas vraiment esquiver."
    kael neutre "Demain, il va falloir faire le bon choix et voter."

    menu:
        "Suivre la discussion."
        "Revenir sur la phrase de Kael.":
            "Je garde ses mots en tête."
            "Demain, personne ne pourra prétendre que le vote arrive par surprise."
        "Observer les réactions autour de la table.":
            "Je laisse les mots circuler."
            "Les regards disent déjà presque autant que les phrases."
        "Noter mentalement la règle d'unanimité.":
            "Une voix contre suffira."
            "Ce détail change tout."


    elen joie "On peut essayer d’être d’accord, non ?"
    elen content "Juste une fois. Rien qu’une."
    elen joie "Pour pas leur filer exactement ce qu’ils attendent de nous."

    iris colere "Ils veulent du spectacle. Du vrai drama de téléréalité."

    elen content "Franchement… la proposition a pas l’air si pourrie que ça, si ?"
    elen joie "Je veux dire… y a claiiirement pire, non ?"

    "Personne ne répond vraiment mais d'un autre côté personne ne proteste."


    sael raison "Touchant."
    sael mefiant "Mais on verra demain."

    kael reflechit "Demain, c’est tard."
    kael neutre "On doit se parler aujourd’hui."

    sael surpris "Tu veux dire quoi ?"
    sael mefiant "Qu’on fasse une réunion ?"

    iris surpris "Mais c’est pas déjà ce qu’on fait là depuis le début ou quoi ?!"


    tomas hesitation "Je…"
    tomas reflechit "Je pense que c’est important."
    tomas colere "Parce que ça concerne nos districts. Directement."
    tomas hesitation "Et si on peut faire circuler des choses entre nous…"
    tomas inquiet "Ben… on peut aussi s’entraider, non ?"

    kael surpris "Tu penses à quoi ?"

    tomas hesitation "Aux médicaments."
    tomas colere "Aux matériaux de construction, ou… ce genre de choses."
    tomas surpris "Pourquoi pas aux gens, aussi. À un moment donné."

    sael raison "Les gens, c’est autre chose."
    sael mefiant "La proposition parlait des échanges dans les districts, pas d'autoriser les gens à changer de district."

    tomas hesitation "Je sais…"
    tomas inquiet "M-Mais si les échanges deviennent autorisés… alors peut-être que…"
    

    mara taquin "C’est mignon tout ça, mais qui va surveiller ces petits échanges ?"

    tomas hesitation "On n’a pas les détails."

    kael reflechit "Justement."
    kael neutre "On devra décider sans."

    mara neutre "Décider à l’aveugle, ou presque."
    mara taquin "J’adore quand on improvise avec nos vies."

    tomas colere "Du coup… on doit se faire confiance. Voilà."


    nyra taquin "On pourrait commencer par lister ce qu’on sait."
    nyra raison "Et ce qu’on ignore."
    nyra taquin "Parce que là, on se jette des impressions sans grande certitude."
    nyra raison "C'est pas comme ça qu'on avancera ..."

    mara taquin "T’as de quoi pondre un roman sur tout ce qu’on sait pas ?"

    nyra taquin "Je veux une base."

    kael reflechit "Elle a raison."
    kael neutre "Sinon on va se bouffer."


    elen joie "Je peux prendre des notes si vous voulez."
    elen content "Ça me calme de tout noter. Ça donne l’impression qu’on bosse vraiment sur un truc important…"
    elen joie "… et que c’est pas juste du vent."

    nyra raison "Tu vois, c’est utile."

    elen reflexion "Je sais pas… ça me rassure, c’est tout."


    iris colere "Bon. On a trois priorités, ok ?"
    iris desaccord "Un : on veut pas se faire baiser."
    iris colere "Deux : on veut pas trahir nos districts."
    iris desaccord "Et trois : si possible, on évite de finir par se détester tous. Ambitieux, je sais."

    nyra taquin "T’as pas oublié la lune dans ta liste aussi ?"

    iris inquiet "Sacrément drôle, ouais. À mourir de rire."

    elen joie "On n’a qu’une journée pour se décider."
    elen triste "Une seule. C’est hyper court quand on y pense…"


    julian surpris "Bon, on fait quoi concrètement là ?"
    julian taquin "Parce que tourner en rond c’est mignon cinq minutes, mais après ça gave."

    iris surpris "Tu proposes quoi, là, concrètement ? Vas-y, je t’écoute."

    julian sourire "Faut un vrai plan, là."
    julian taquin "Ou alors, on y réfléchit et on met en commun demain."
    julian sourire "Chacun bosse son bout dans son coin, et demain on se retrouve avec du lourd."

    iris colere "Dire qu’on réfléchit, c’est super facile à balancer."
    iris desaccord "Le faire vraiment, par contre… c’est une autre paire de manches."

    julian peur "T’as peur de qui, là, tout de suite ? Dis."

    iris inquiet "Des gens qu'on risque de tuer ..."


    sael raison "Tout ce qu’on partage ici, ça va nous revenir dans la gueule. Toujours."
    sael mefiant "Toujours."

    iris colere "Et si on refuse ?"

    sael desaccord "Il suffit d'une voix contre pour que ça parte en couille."
    sael mefiant "On laisse ceux qui veulent se vendre le faire."

    iris desaccord "Tu dis ça comme si c’était simple."

    sael raison "Rien n’est simple."
    sael desaccord "Mais refuser, c’est aussi un choix. Un choix qui a des conséquences."


    mara agace "On va pas tous voter pareil, soyons sérieux."
    mara taquin "Y a des districts qui ont rien à voir entre eux."
    mara neutre "Nos vies, nos galères, nos habitudes… tout est différent."
    mara taquin "Et d’un coup on nous demande de tomber d’accord ?!"
    mara neutre "Dans ce bordel ? Sérieux ?!"

    nyra reflexion "Donc on doit parler d’inégalités."

    mara taquin "Ouais exactement."
    mara neutre "Et on peut même pas checker avec nos potes de district."

    nyra taquin "Ça va être beau."


    tomas hesitation "On est obligés de parler de nos districts ? Genre… en détail ?"
    tomas inquiet "E-Enfin je veux dire, bien sûr qu’on veut les défendre, mais…"
    

    elen joie "On a tous la trouille de choisir."
    elen content "Mais en vrai… on choisit déjà. À chaque fois qu’on parle, la vie n'est qu'une suite de choix !"

    tomas hesitation "Je sais."
    tomas inquiet "Je sais, oui."


    kael reflechit "Si on ne se parle pas ici, on va se parler derrière."
    kael inquiet "Et là, ça devient dangereux."


    iris colere "Je déteste quand c’est raisonnable."

    nyra raison "Tu préfères quand c’est violent ?"

    iris desaccord "Je préfère quand je comprends au moins ce qu’on nous demande de faire, merci."

    nyra taquin "Alors on va en parler."


    julian taquin "Je peux résumer vite fait pour qu’on soit tous synchro ?"
    julian sourire "On s’organise."
    julian taquin "On pose clairement ce qu’on peut apporter."
    julian sourire "Et on se juge pas. Promis, je commence."

    iris colere "Ça va être le plus dur. De loin."

    julian taquin "Ouais, je sais."


    mara doute "Et pendant qu’on papote…"
    mara doute "Kami nous mate."
    mara taquin "Elle grave tout : qui parle, qui propose quoi, qui va péter les plombs en premier."

    iris desaccord "Alors on craque pas. Personne craque. Ok ?"

    mara neutre "C'est facile à dire."
    mara taquin "Surtout quand tout le monde regarde."


    tomas hesitation "Et si quelqu’un refuse ?"

    iris colere "On va obliger personne à voter pour. Personne."

    kael neutre "Mais on lui laisse une place."

    tomas colere "D-De toute façon on ne sait même pas qui votera contre, si ?."

    "Le bruit reprend doucement."
    "Des chaises raclent, des plateaux s’éloignent."
    "Tout le monde retourne peu à peu à ses occupations."


    $ hideGroup()

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

    hide screen day2_quick_vote_notes

    "Le reste de la matinée passe rapidement et pendant ce temps là, je me balade pour me changer les idées."
    "Des pas, des couloirs, des respirations."
    "Je ne sais pas qui va craquer."
    "Je ne sais pas si ce sera moi."

    call START_FREE_TIME("_2_APRES_MIDI") from _call_START_FREE_TIME

# Durée : 3m50
# Total : 1h 14m 50s

# Freetimde :
# Durée : 1m30
# Total : 1h 16m 20s

label _2_APRES_MIDI:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    show screen day2_quick_vote_notes

    "L’après-midi commence sans véritable signal."
    "Je marche."
    "Un couloir étroit."
    "Propre."
    "Trop propre."


    $ showGroup([
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("sael", "mefiant", 1.20),
    ])

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


    $ hideGroup()

    "Je les laisse derrière."
    "Le couloir continue."
    "Des voix passent."
    "Des mots coupés."
    "Des phrases qu’on ne termine pas."

    "Je tourne."
    "Lysa est adossée au mur."
    "Bras croisés."
    "Elias est face à elle."

    menu:
        "Approcher Lysa et Elias."
        "Les rejoindre directement.":
            "Je fais quelques pas vers eux avant que la conversation ne se referme."
        "Attendre qu'Elias termine sa phrase.":
            "Je ralentis."
            "Une phrase complète vaut parfois mieux qu'une question trop rapide."
        "Les observer quelques secondes.":
            "Lysa garde les bras croisés."
            "Elias cherche ses mots sans la brusquer."


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("lysa", "triste", 0.25),
    ])

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
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "inquiet", 0.13),
        ("lysa", "triste", 0.25),
    ])


    noam hesitation "Ça va ?"

    lysa determine "Ça va comme ça peut."

    elias ecoute "On va avoir besoin de toi."

    lysa opposition "Vous allez surtout parler."
    lysa blase "Moi, on m’écoutera à moitié."

    noam inquiet "Pourquoi tu penses ça ?"

    lysa reflexion "Mon district. Enfin, le notre ..."
    lysa neutre "Les gens entendent avant de regarder."

    elias raison "Alors dis-leur."

    lysa triste "Dire quoi ?"
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

    lysa triste "Ne promets pas trop vite."

    noam neutre "On en parlera peut-être demain..."

    lysa triste "Oui."
    lysa triste "Avant que je change d’avis."
    lysa blase "J’ai pas envie de briser leurs espoirs…"
    lysa determine "mais tu as compris."
    lysa fatigue "... C’est déjà ça."

    call day2_collect_vote_argument("approvisionnement") from _call_day2_collect_vote_argument_approvisionnement

    tuto "Un argument rangé dans la mallette apparaît dans l'onglet Prochain vote."
    tuto "Les notes ne décident pas à ta place : elles servent à préparer le vote et à relire les positions supposées."


    $ hideGroup()

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

    menu:
        "Avant de parler à Kael."
        "Examiner brièvement la salle.":
            "Je suis les lignes des consoles et les reflets de la vitre."
            "Ici, tout ramène à Orbite."
        "Regarder la baie vitrée.":
            "Orbite paraît calme de loin."
            "C'est presque pire."
        "Aller directement vers lui.":
            "Je ne laisse pas le silence s'installer plus longtemps."


    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

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

    noam raison "Il me semble qu’on n’est pas encore divisés."

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


    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

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

    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement

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

    $ hideGroup()

    "Il s'éloigne de quelques pas."

    kael triste "Excuse moi, je vais faire un tour..."

    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite


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


    $ showGroup([
        ("iris", "determine", 0.49),
        ("elias", "neutre", -0.11),
    ])

    iris determine "Encore."
    iris determine "Allez. Je dois… je dois continuer."
    iris determine "Sans ralentir. Sans m’arrêter. Allez."

    elias ecoute "Respire. C'est le plus important."
    elias ecoute "Sinon tu vas te fatiguer pour rien."

    "Je m’approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "hesitation", 0.13),
        ("iris", "determine", 0.49),
    ])


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

    noam reflexion "Un…"
    noam reflexion "Deux…"

    "Je commence à pousser les altères."

    $ mg_skip_scene_pick = True
    call minijeu_halteres from _call_minijeu_halteres

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


    $ hideGroup()

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


    "Nyra est en train de parler de sa vie."
    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("nyra", "neutre", 0.96),
    ])

    nyra sourire "À Orbite, on mangeait souvent en décalé."
    nyra sourire "Chacun vivait vraiment à son propre rythme, comme dans dessortes de cycles."
    nyra sourire "Le silence faisait partie du travail."

    noam hesitation "Tu regrettes ?"

    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("kael", "neutre", 0.84),
        ("nyra", "sourire", 0.96),
    ])

    kael neutre "Ce qui me manque moi, c’est la routine."
    kael neutre "Pas l’endroit, à vrai dire, ça fait du bien de voir autre chose."


    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("kael", "neutre", 0.84),
        ("elen", "taquin", 0.72),
        ("nyra", "sourire", 0.96),
    ])

    elen taquin "Orbite, c’était comment ?"
    elen reflexion "Bah… on entend vraiment de tout et n’importe quoi sur ce qu'il se passe là-haut."
    elen content "Des gens qui dorment en flottant comme des méduses, des repas qui se baladent tout seuls… c’est complètement barré !"

    kael neutre "On flotte, oui."
    kael neutre "Mais on fait quand même la vaisselle, même si parfois c'est galère !"

    nyra taquin "C'est clair !."


    $ showGroup([
        ("noam", "inquiet", 0.13),
        ("kael", "neutre", 0.84),
        ("tomas", "neutre", 0.60),
        ("elen", "content", 0.72),
        ("nyra", "taquin", 0.96),
    ])

    tomas hesitation "Et… euh… vous aviez aussi des médiateurs, chez vous ?"
    tomas inquiet "Des… assemblées, ou un truc comme ça ? C-Comment vous faisiez pour prendre les décisions ?"

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


    $ showGroup([
        ("noam", "inquiet", 0.13),
        ("kael", "triste", 0.84),
        ("tomas", "inquiet", 0.60),
        ("elen", "inquiet", 0.72),
        ("nyra", "raison", 0.96),
        ("ryn", "neutre", 1.08),
    ])

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

    menu:
        "Après la réponse de Ryn."
        "Garder sa position en tête.":
            "Je garde sa prudence en tête."
        "Reformuler concrètement.":
            noam raison "Donc pour l'instant, tu penches pour, mais tu veux entendre les autres."
            ryn reflechit "Voilà. C'est déjà pas mal, non ?"
        "Continuer à écouter.":
            "Je ne rajoute rien."
            "Parfois, une phrase suffit à dessiner une position."


    $ hideGroup()

    "La conversation dérive."
    "D’autres se mêlent à nous."
    "Des questions, des souvenirs, des comparaisons."
    "Puis la fatigue gagne peu à peu nos esprits."

    stop music fadeout 1.0
    pause 0.6
    hide screen day2_quick_vote_notes

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

    # jump patreon_ending

    call end_day("3")

    jump _3_CANON


# Durée : 1m55
# Totale : 1h 24m 10s
default j2_wakeup_trace_attempts = 0
default j2_vote_codex_unlocked = False
default j2_vote_arguments = []
default j2_vote_positions = {
    "lysa": "unknown",
    "elias": "unknown",
    "kael": "unknown",
    "mara": "unknown",
    "julian": "unknown",
    "iris": "unknown",
    "elen": "unknown",
    "ryn": "unknown",
    "sael": "unknown",
    "tomas": "unknown",
    "nyra": "unknown",
}

init 3 python:
    DAY2_VOTE_COLUMNS = [
        ("for", "POUR"),
        ("unknown", "INCONNU"),
        ("against", "CONTRE"),
    ]

    DAY2_VOTE_ARGUMENTS = {
        "approvisionnement": {
            "title": "Difficulté d'approvisionnement",
            "category": "Risque économique",
            "summary": "Les circuits actuels ne répondent pas toujours aux besoins réels des habitants.",
            "origin": "Entendu lors d'un échange avec Lysa et Elias.",
        },
        "rationnement": {
            "title": "Bons de rationnement",
            "category": "Organisation quotidienne",
            "summary": "Les demandes officielles et les bons structurent déjà l'accès aux biens essentiels.",
            "origin": "Relevé dans la discussion avec Kael.",
        },
        "orbite": {
            "title": "Faiblesse d'Orbite",
            "category": "Sécurité",
            "summary": "Sur Orbite, une erreur de circulation ou de sanction peut menacer directement la survie.",
            "origin": "Décrit par Kael en salle d'observation.",
        },
    }

    DAY2_VOTE_CHARACTER_ORDER = ["lysa", "elias", "kael", "mara", "julian", "iris", "elen", "ryn", "sael", "tomas", "nyra"]
    DAY2_VOTE_CHARACTERS = {
        "lysa": {"name": "Lysa", "portrait": "images/character/lysa/portrait.png"},
        "elias": {"name": "Elias", "portrait": "images/character/elias/portrait.png"},
        "kael": {"name": "Kael", "portrait": "images/character/kael/portrait.png"},
        "mara": {"name": "Mara", "portrait": "images/character/mara/portrait.png"},
        "julian": {"name": "Julian", "portrait": "images/character/julian/portrait.png"},
        "iris": {"name": "Iris", "portrait": "images/character/iris/portrait.png"},
        "elen": {"name": "Elen", "portrait": "images/character/elen/portrait.png"},
        "ryn": {"name": "Ryn", "portrait": "images/character/ryn/portrait.png"},
        "sael": {"name": "Sael", "portrait": "images/character/sael/portrait.png"},
        "tomas": {"name": "Tomas", "portrait": "images/character/tomas/portrait.png"},
        "nyra": {"name": "Nyra", "portrait": "images/character/nyra/portrait.png"},
    }

    def day2_vote_argument_count():
        return len(store.j2_vote_arguments)

    def day2_vote_add_argument(arg_id):
        if arg_id not in DAY2_VOTE_ARGUMENTS:
            return False
        title = DAY2_VOTE_ARGUMENTS[arg_id]["title"]
        if title not in store.arguments:
            store.arguments.append(title)
        if arg_id not in store.j2_vote_arguments:
            store.j2_vote_arguments.append(arg_id)
        renpy.restart_interaction()
        return True

    def day2_vote_position_dragged(char_id, drags, drop):
        if drop is None:
            renpy.restart_interaction()
            return
        target = getattr(drop, "drag_name", "")
        if target.startswith("day2_vote_col_"):
            store.j2_vote_positions[char_id] = target.replace("day2_vote_col_", "")
        renpy.restart_interaction()

    def day2_vote_card_xy(char_id):
        col = store.j2_vote_positions.get(char_id, "unknown")
        col_index = {"for": 0, "unknown": 1, "against": 2}.get(col, 1)
        items = [cid for cid in DAY2_VOTE_CHARACTER_ORDER if store.j2_vote_positions.get(cid, "unknown") == col]
        idx = items.index(char_id) if char_id in items else 0
        return (48 + col_index * 340 + (idx % 2) * 154, 72 + (idx // 2) * 132)

    def day2_argument_drop(drags, drop, arg_id):
        if drop is not None and getattr(drop, "drag_name", "") == "day2_briefcase_drop":
            day2_vote_add_argument(arg_id)
            return True
        renpy.restart_interaction()

screen vote_argument_briefcase(arg_id, argument_data, card_drag_name, drop_drag_name, drop_handler):
    modal True
    zorder 180
    $ arg = argument_data

    add Solid("#02050bd9")
    frame:
        xalign 0.5
        yalign 0.09
        padding (18, 10)
        background Solid("#06131d")
        text "Glisse la carte dans la mallette de Noam." size 24 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"

    draggroup:
        drag:
            drag_name card_drag_name
            xpos 330
            ypos 338
            xsize 460
            ysize 260
            draggable True
            droppable False
            dragged (lambda drags, drop, arg_id=arg_id, drop_handler=drop_handler: drop_handler(drags, drop, arg_id))
            fixed:
                xfill True
                yfill True
                add arg.get("card", "gui/day3/argument_card_bg.png")
                vbox:
                    xpos 44
                    ypos 46
                    xsize 370
                    spacing 14
                    text "[arg['title']]" size 34 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"
                    text "DOSSIER DU VOTE" size 20 color "#9ed8ff" font "fonts/Rajdhani-SemiBold.ttf"

        drag:
            drag_name drop_drag_name
            xpos 1020
            ypos 308
            xsize 560
            ysize 330
            draggable False
            droppable True
            fixed:
                xfill True
                yfill True
                add "gui/day3/argument_drop_zone.png"
                add "gui/day3/argument_briefcase_open.png" xpos 20 ypos 24
                text "DÉPOSER ICI" xalign 0.5 ypos 250 size 28 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"

screen day2_quick_vote_notes():
    pass

screen day2_vote_tablet_notice():
    modal True
    zorder 120
    add Solid("#02050bcc")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 820
        padding (34, 28)
        background Solid("#081722f2")
        vbox:
            spacing 16
            text "TABLETTE DE NOAM" size 34 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
            text "Nouveau dossier disponible : Prochain vote" size 25 color "#9ed8ff"
            text "La fiche rassemble la proposition, les arguments rangés dans ton dossier et les positions que tu supposes chez les autres représentants." size 21 color "#b8d8e4"
            text "Les portraits peuvent être déplacés librement entre POUR, INCONNU et CONTRE. Ce classement est une note personnelle, pas une correction automatique." size 21 color "#b8d8e4"
            textbutton "Continuer":
                xalign 0.5
                xsize 210
                background Solid("#1a2530")
                hover_background Solid("#2d3a45")
                text_color "#dff8ff"
                action Return(False)

screen day2_current_vote_codex():
    tag menu
    modal True
    zorder 200

    add Solid("#080d12")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 960
        padding (28, 24)
        background Solid("#07151ef5")

        vbox:
            spacing 18
            hbox:
                xfill True
                vbox:
                    spacing 4
                    text "Codex" size 22 color "#3a9fca"
                    text "Prochain vote" size 48 color "#daeaf5" font "fonts/Rajdhani-SemiBold.ttf"
                textbutton "Retour":
                    xalign 1.0
                    yalign 0.5
                    xsize 150
                    background Solid("#1a2530")
                    hover_background Solid("#2d3a45")
                    text_color "#dff8ff"
                    action Return()

            hbox:
                spacing 22

                frame:
                    xsize 480
                    yfill True
                    padding (22, 18)
                    background Solid("#0d2230")
                    vbox:
                        spacing 12
                        text "Vote en cours" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        text "Autoriser le transport, la vente et l'échange de marchandises au sein des districts." size 22 color "#dff8ff"
                        text "Moment prévu : Jour 3, 14h00" size 19 color "#9ed8ff"
                        text "Résumé neutre" size 21 color "#70c6e8"
                        text "Le texte promet une circulation plus libre des biens. Ses effets restent incertains selon les districts, les procédures et les risques locaux." size 20 color "#b8d8e4"
                        null height 8
                        text "Arguments découverts" size 24 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        for arg_id in ["approvisionnement", "rationnement", "orbite"]:
                            if arg_id in j2_vote_arguments:
                                $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
                                frame:
                                    xfill True
                                    padding (12, 10)
                                    background Solid("#123044")
                                    vbox:
                                        spacing 3
                                        text "[arg['title']]" size 21 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text "[arg['summary']]" size 17 color "#b8d8e4"
                                        text "[arg['origin']]" size 15 color "#74a8ba"
                            else:
                                frame:
                                    xfill True
                                    padding (12, 12)
                                    background Solid("#111820")
                                    text "Argument non découvert" size 18 color "#526d79"

                fixed:
                    xfill True
                    yfill True

                    draggroup:
                        for cidx, col_data in enumerate(DAY2_VOTE_COLUMNS):
                            $ col_id = col_data[0]
                            $ col_label = col_data[1]
                            drag:
                                drag_name ("day2_vote_col_%s" % col_id)
                                draggable False
                                droppable True
                                xpos (20 + cidx * 340)
                                ypos 0
                                xsize 318
                                ysize 810
                                frame:
                                    xfill True
                                    yfill True
                                    padding (14, 14)
                                    background Solid("#0c1d29")
                                    vbox:
                                        spacing 8
                                        text "[col_label]" xalign 0.5 size 28 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text "Glisse les portraits ici." xalign 0.5 size 16 color "#6797aa"

                        for cid in DAY2_VOTE_CHARACTER_ORDER:
                            $ card_x, card_y = day2_vote_card_xy(cid)
                            $ cdata = DAY2_VOTE_CHARACTERS[cid]
                            drag:
                                drag_name ("day2_vote_char_%s" % cid)
                                xpos card_x
                                ypos card_y
                                xsize 142
                                ysize 116
                                draggable True
                                droppable False
                                dragged (lambda drags, drop, cid=cid: day2_vote_position_dragged(cid, drags, drop))
                                frame:
                                    xfill True
                                    yfill True
                                    padding (7, 7)
                                    background Solid("#182d3a")
                                    vbox:
                                        spacing 3
                                        add cdata["portrait"] xalign 0.5 xysize (62, 62)
                                        text "[cdata['name']]" xalign 0.5 size 17 color "#dff8ff"

screen day2_argument_briefcase(arg_id):
    $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
    use vote_argument_briefcase(arg_id, arg, "day2_argument_card", "day2_briefcase_drop", day2_argument_drop)

label day2_play_wakeup_trace:
    call trace_qte_run(mg_id="trace_day2_wakeup", title="RÉVEIL — JOUR 2", path_type="curve_right", time_limit=6.0, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True)
    return True

label day2_collect_vote_argument(arg_id):
    call screen day2_argument_briefcase(arg_id)
    if _return:
        play sound sfx_drop
        "Note ajoutée au Prochain vote."
    return
