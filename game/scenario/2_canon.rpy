label _2_CANON:

    $ day_id = 2
    $ current_day = 2

    scene black
    play music "music/main_menu.mp3" fadein 1.0

    pause 0.6

    think "Côté gauche. Non. Sur le dos. Pire. Une jambe repliée... toujours pas."
    think "Le matelas est confortable. Le problème, enfin... c'est moi."

    $ blink()

    pause 0.6

    think "J'ouvre les yeux. Encore."
    scene bg_cg012 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg012")

    $ blink()

    think "Je les referme. Je négocie avec mon cerveau."

    $ blink()

    pause 0.4

    think "Refus immédiat."

    $ blink()

    pause 0.6

    think "Chaque fois que je commence à glisser, une image revient."
    $ blink()
    think "La salle. Les sièges. Les onze voix qui n'avaient pas encore de visage hier."

    pause 0.6

    $ blink()
    think "Kami."

    pause 0.6

    think "J'inspire. J'expire. Je serre les dents entre les deux, ce qui annule probablement l'exercice."

    pause 0.6

    $ blink()
    think "Rien. Mon corps refuse de croire que la chambre est sûre."
    $ blink()

    voix "Diffusion prioritaire."

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
    kami "Enfin, je ne peux que spéculer : vous n'êtes pas nombreux à avoir désactivé votre brouilleur !"

    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "C’est mignon."
    kami "Vraiment."

    pause 0.5

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Mais soit. Nous en sommes au jour deux."

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

    think "Cette fois, je suis réveillé. Hier s'est enchaîné trop vite pour réfléchir : écouter, avancer, comprendre — enfin, essayer."
    think "Maintenant, le calme ramène tout ce que j'ai repoussé."

    pause 0.6

    think "Ma famille est à des milliers de kilomètres. L'appartement, la cafetière trop bruyante, le café trop amer."
    think "Et Juliette. Ma petite sœur, debout trop tôt, toujours une question prête avant que la précédente ait une réponse."
    think "Comment lui expliquer le Conclave ? Comment lui expliquer Kami sans lui apprendre à avoir peur de chaque écran ?"

    pause 0.6

    think "Elle me regarde peut-être en ce moment. Moi, je ne peux ni la voir ni l'aider."
    think "Enfin... rester allongé n'y changera rien."

    pause 0.6

    call day2_play_wakeup_trace from _call_day2_play_wakeup_trace

    think "Je me redresse et pose les pieds au sol."

    pause 0.6

    think "Cafétéria. Annonce importante. Avenir proche. Une matinée raisonnable."

    stop music fadeout 1.0
    pause 0.6

    jump _2_CAFETERIA_ANNONCE_KAMI

# Durée : 2m35
# Total : 1h 7m 25s

label _2_CAFETERIA_ANNONCE_KAMI:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    pause 0.4

    think "Un pied dans la cafétéria, et les voix me frappent avant l'odeur du petit-déjeuner."
    play sound sfx_door

    menu:
        "Choisir où se placer."
        "Je m'assois près d'une table encore libre.":
            think "Je tire une chaise sans bruit. D'ici, je vois presque toute la salle."
        "Rester près du buffet.":
            think "Je prends un plateau pour occuper mes mains. Les voix arrivent par morceaux."
        "Me tenir près de l'entrée.":
            think "Je reste près de la porte. Facile de compter les arrivées. Facile de repartir aussi."


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
    

    iris desaccord "Excellente question. Peut-on ignorer une convocation de l'IA qui exécute les retardataires ?"
    iris colere "Quelqu'un veut tester le protocole ? Non ? Super."

    tomas panne "Je— je dis pas que c’est idiot !"
    tomas panne "C’est juste que… enfin… voilà."


    ryn neutre "Laisse-le. Au moins, il parle."
    ryn reflechit "Y'en a qui serrent les dents depuis hier."


    elen content "Oh !"
    elen joie "C'est vraiii que l'ambiance est un peu chelou..."
    elen surpris "Oh ! Ils ont changé les plateaux ! Regardez comme ils brillent ! Ça change tout, non ?"

    iris desaccord "Elen."
    iris colere "Les plateaux ne compensent pas une menace de mort, Elen. Même brillants."

    elen desaccord "Oui mais quand même !"
    elen content "N’empêche… peut-être que c’est fait exprès pour nous rebooster un peu le moral, non ?"
    
    ryn fatigue "Ou pour nous faire avaler des conneries plus facilement."

    pause 0.4


    elias ecoute "…"
    elias neutre "Ça va tomber de toute façon. Autant être prêts, c'est chaud sinon."

    noam surpris "Prêts à quoi, exactement ?"

    elias neutre "À encaisser ce qu'elle va nous balancer. J'sais pas quoi, justement."

    pause 0.6


    sael raison "Ma grand-mère disait que l'attente donne des dents à ce qu'on craint."
    sael mefiant "Mangez. Nous aurons besoin de forces quand le signe viendra."


    nyra raison "Qu'est-ce qui vous aiderait le plus, là ? Connaître l'annonce ou savoir comment les autres vont la recevoir ?"


    iris colere "Et en plus on peut même pas se barrer. Génial."

    nyra raison "On ne peut pas partir. Mais on peut éviter de se rendre la matinée pire."

    pause 0.6

    think "La porte s'ouvre."
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
    mara taquin "On vous entend depuis le couloir. Joli comité d'accueil."
    mara neutre "Continuez, surtout. J'aime voir qui panique avec style."


    elen content "Oh Mara !"
    elen joie "Viens t’asseoir avec nous, allez ! Ça serait trop cool."

    mara neutre "Je suis très bien là. Je vois tout le monde."
    mara taquin "Et vous me voyez entrer. Arrangement parfait."

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

    lysa blase "Désolée pour le retard. Enfin, non."


    tomas inquiet "N-Non non !"
    tomas hesitation "Enfin… y a pas de problème. Vraiment. Aucun problème."

    lysa reflexion "Cassandre non plus n'avait pas envie de retourner au palais. Elle avait raison. Bref."

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

    kael neutre "Il manque quelqu'un."
    kami "On est presque 9h."

    iris colere "Franchement, j’ai la flemme de compter."
    iris desaccord "On va dire que oui, point barre. Ça vous va ?"

    kael reflechit "Bien."

    voix "Diffusion prioritaire."
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
    sael triste "Les routes qui se rouvrent sont parfois de bons signes."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra taquin "Qu'est-ce que vous entendez par « marchandises » ?"
    nyra reflexion "Selon la réponse, ce texte peut nourrir un district ou en vider un autre."

    $ bc_show("iris", "triste", px=-70, py=-50, pz=0.85)
    iris colere "Merci. Enfin une question utile. Les termes sont vagues, donc dangereux."

    $ bc_show("nyra", "sourire", px=-70, py=-50, pz=0.85)
    nyra surpris "C'est justement pour ça que je la pose."
    $ bc_hide()

    pause 0.6

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais ils vont me laisser parler ces petits cons ?!"

    pause 0.4
    think "Le silence tombe instantanément."
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


    elen joie "Et si on essayait d'en parler calmement ? Tous ensemble ?"
    elen content "Sans s'énerver, avec un truc à manger, ce serait encore mieux mais— bref !"


    sael raison "Le calme ne garantit pas l'accord. Mais il laisse une place aux mots."


    mara taquin "Un débat calme devant des caméras ? Vous voulez vraiment priver le public de tout plaisir ?"


    kael reflechit "Les effets dépasseront l'économie."

    pause 0.6

    play sound sfx_door
    "La porte claque. Tous les regards convergent vers Julian."


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

    julian rire "Bonjour à tous. Julian est enfin parmi vous."
    julian surpris "Qu'ai-je manqué ?"


    nyra raison "Qu'est-ce que tu préférerais entendre d'abord : le sujet ou le délai ?"
    julian surpris "Le délai."
    nyra taquin "Demain."

    julian panne "Demain..."
    julian taquin "Très bien. L'urgence clarifie les caractères."

    noam colere "Bienvenue au Conclave."
    noam reflexion "Je crois bien que c'est notre quotidien désormais."

    pause 0.6

    julian sourire "Reprenons clairement. Où en sommes-nous ?"

    iris colere "Tu arrives en retard et tu demandes un récapitulatif personnalisé. Remarquable efficacité collective."

    julian decu "Tu pourrais résumer pour ton plus ancien allié ici."

    iris sourire "Mon allié ? Tu as tenté de me séduire pendant six mois. Ce n'est pas une coalition."

    julian sourire "Très bien. Julian reconstituera seul la situation."

    julian reflexion "Kami annonce un vote. À voir vos visages..."

    think "Il étudie chaque visage, tout en gardant son meilleur angle pour la caméra."

    julian reflexion "La proposition n'est pas manifestement hostile. Commerce, circulation de ressources..."
    julian sourire "Une réouverture des échanges entre districts."

    iris intervention "Comment tu as—"

    julian taquin "Julian lit les situations."


    elias ecoute "Y a des écrans partout. La diffusion tournait dans le couloir. C'est chaud de faire genre t'as deviné."

    julian panne "…"
    julian decu "Elias. Il restait exactement trois secondes avant que ce moment fonctionne."
    julian decu "J'ai entendu la diffusion. Inutile de reprendre."

    $ j2_vote_codex_unlocked = True
    call screen day2_vote_tablet_notice
    think "La tablette vibre. Le dossier du vote rejoint mes notes."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m35
# Total : 1h 11m 0s

label _2_CAFETERIA_POST_ANNONCE:

    show screen day2_quick_vote_notes

    think "Le silence ressemble presque à un soulagement. C'est ce qui le rend suspect."

    kael reflechit "Sur le papier : autoriser les échanges."
    kael neutre "Les effets ne seront pas simples."

    mara doute "C'est presque séduisant. Donc forcément louche."

    sael raison "Un chemin facile peut être un signe. Ou un piège posé pour ceux qui cherchent un signe."

    kael neutre "L'amendement vient de l'un de nous."
    kael inquiet "Le risque est dans ses effets, pas nécessairement dans son auteur."

    mara neutre "Le piège, c’est nous."
    mara taquin "On a nos districts, nos besoins, nos secrets."
    mara neutre "Et nos égos, tant qu’à faire."


    nyra taquin "Qui perd quelque chose si les échanges reprennent ?"
    nyra raison "Trouvons cette réponse avant de décider que le texte est consensuel."

    kael neutre "Ce qui n’est pas une bonne nouvelle."

    nyra taquin "Tu penses à Orbite ?"


    iris colere "Le texte ne définit ni contrôle, ni quotas, ni responsabilité."
    iris desaccord "Une bonne intention sans protocole, c'est une catastrophe qui attend son horaire."

    mara taquin "Tu deviens vraiment attirante quand tu parles de protocoles."
    iris surpris "Je— Ce n'est pas le sujet !"
    mara sourire "Dommage. Continue quand même."

    iris colere "Sérieusement…"
    iris desaccord "Et ça veut dire qu’on va devoir causer de tout le reste ensemble."
    iris colere "L'enfer. Avec ordre du jour."

    nyra taquin "Tu dis ça comme si c’était la première fois."

    iris desaccord "La première fois que je débats d'un texte capable d'affamer un district ? Oui. Curieusement."

    kael reflechit "On ne peut pas vraiment esquiver."
    kael neutre "Demain, il va falloir faire le bon choix et voter."

    menu:
        "Suivre la discussion."
        "Revenir sur la phrase de Kael.":
            think "Je garde ses mots. Demain, personne ne pourra prétendre à la surprise."
        "Observer les réactions autour de la table.":
            think "Je laisse les mots circuler. Les regards en disent presque autant."
        "Noter mentalement la règle d'unanimité.":
            think "Une voix contre suffira. Ce détail change tout."


    elen joie "On peut essayer d’être d’accord, non ?"
    elen content "Juste une fois. Rien qu’une."
    elen joie "Pour pas leur filer exactement ce qu’ils attendent de nous."

    iris colere "Ils veulent du spectacle. Du vrai drama de téléréalité."

    elen content "Franchement… la proposition a pas l’air si pourrie que ça, si ?"
    elen joie "Je veux dire… y a claiiirement pire, non ?"

    think "Personne ne répond. Personne ne proteste non plus."


    sael raison "Souhaiter l'accord est une bonne chose. Le prendre pour un signe en est une autre."

    kael reflechit "Demain est trop tard. Parlons aujourd'hui."

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


    nyra taquin "Qu'est-ce qu'on sait ? Qu'est-ce qu'on ignore ?"
    nyra raison "Commençons par là. Chacun pourra ajouter ce qui concerne son district."

    mara taquin "T’as de quoi pondre un roman sur tout ce qu’on sait pas ?"

    nyra taquin "Je veux une base."

    kael reflechit "Elle a raison."
    kael neutre "Sinon on va se bouffer."


    elen joie "Oh ! Je peux prendre des notes ! J'écris super vite quand je panique."
    elen content "Et après je peux faire des catégories. Avec des couleurs ! Ça donne l'impression qu'on contrôle un truc."

    nyra raison "Tu vois, c’est utile."

    elen reflexion "Je sais pas… ça me rassure, c’est tout."


    iris colere "Trois priorités. Un : éviter les effets pervers. Deux : protéger nos districts."
    iris desaccord "Trois : ne pas nous haïr avant demain. Oui, la troisième est techniquement la plus ambitieuse."

    nyra taquin "T’as pas oublié la lune dans ta liste aussi ?"

    iris inquiet "Sacrément drôle, ouais. À mourir de rire."

    elen joie "On n’a qu’une journée pour se décider."
    elen triste "Une seule. C’est hyper court quand on y pense…"


    julian surpris "Il nous faut une méthode. Ce collectif ne peut pas tourner en rond jusqu'au vote."

    iris surpris "Tu proposes quoi, là, concrètement ? Vas-y, je t’écoute."

    julian sourire "Chacun prépare les besoins de son district. Demain, nous mettons tout en commun."
    julian taquin "Une structure claire. Un résultat visible. Julian peut coordonner."

    iris colere "Dire qu’on réfléchit, c’est super facile à balancer."
    iris desaccord "Le faire vraiment, par contre… c’est une autre paire de manches."

    julian peur "Qui te semble incapable de réfléchir, exactement ?"

    iris inquiet "Des gens qu'on risque de tuer ..."


    sael raison "Les mots confiés à une assemblée reviennent toujours à celui qui les a donnés."

    iris colere "Et si on refuse ?"

    sael desaccord "Une voix contre suffit. Ceux qui ne veulent pas se livrer doivent pouvoir garder le silence."

    iris desaccord "Tu dis ça comme si c’était simple."

    sael raison "Rien n’est simple."
    sael desaccord "Mais refuser, c’est aussi un choix. Un choix qui a des conséquences."


    mara agace "On ne votera pas tous pareil. Nos districts n'ont rien à voir."
    mara taquin "Demander l'unanimité ici, c'est organiser une fête et exiger que tout le monde reparte amoureux."

    nyra reflexion "Donc on doit parler d’inégalités."

    mara taquin "Ouais exactement."
    mara neutre "Et on peut même pas checker avec nos potes de district."

    nyra taquin "Ça va être beau."


    tomas hesitation "On est obligés de parler de nos districts ? Genre… en détail ?"
    tomas inquiet "E-Enfin je veux dire, bien sûr qu’on veut les défendre, mais…"
    

    elen joie "On a tous la trouille de choisir. Mais parler, c'est déjà choisir un peu, non ?"
    elen content "Comme choisir son dessert avant le plat. Mauvais exemple. Enfin, vous voyez !"

    tomas hesitation "Je sais."
    tomas inquiet "Je sais, oui."


    kael reflechit "Si on ne se parle pas ici, on va se parler derrière."
    kael inquiet "Et là, ça devient dangereux."


    iris colere "Je déteste quand c’est raisonnable."

    nyra raison "Tu préfères quand c’est violent ?"

    iris desaccord "Je préfère quand je comprends au moins ce qu’on nous demande de faire, merci."

    nyra taquin "Alors on va en parler."


    julian taquin "Je résume : nous organisons les besoins, les risques et les garanties."
    julian sourire "Sans jugement. Julian commence."

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

    think "Les chaises raclent. Les plateaux s'éloignent. La réunion se dissout sans conclusion."


    $ hideGroup()

    think "La matinée finit. La tension reste accrochée aux épaules, aux gestes, aux sourires trop appliqués."
    think "Mes mains se crispent. Je marche avant de recommencer à chercher une réponse qui n'existe pas."

    stop music fadeout 0.8
    pause 0.6

    hide screen day2_quick_vote_notes

    think "Je traverse des couloirs pour changer d'air. Je ne sais pas qui craquera. Je ne sais pas si ce sera moi."

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

    think "L'après-midi commence dans un couloir étroit, propre au point d'en devenir suspect."


    $ showGroup([
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("sael", "mefiant", 1.20),
    ])

    mara mefiant "Tu penses vraiment qu’ils vont nous laisser voter tranquilles ?"
    mara doute "Sans… orienter un peu ?"

    sael mefiant "Kami n'a pas besoin de nous orienter. Elle attendra que nos peurs le fassent."

    mara taquin "Toujours aussi rassurante."
    sael neutre "Je ne cherche pas à rassurer."

    think "Le silence tranche la conversation."

    mara stress "À plus tard."
    mara doute "… si tout a pas déjà explosé d’ici là."

    sael raison "Si quelque chose cède, le bruit nous guidera."


    $ hideGroup()

    think "Je les laisse derrière. Au tournant suivant, Lysa est adossée au mur, Elias face à elle."

    menu:
        "Approcher Lysa et Elias."
        "Les rejoindre directement.":
            think "Je les rejoins avant que la conversation se referme."
        "Attendre qu'Elias termine sa phrase.":
            think "Je ralentis. Une phrase complète vaut mieux qu'une question trop rapide."
        "Les observer quelques secondes.":
            think "Lysa garde les bras croisés. Elias cherche ses mots sans la brusquer."


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("lysa", "triste", 0.25),
    ])

    elias ecoute "Tu devrais parler avec nous. Si tu veux. C'est chaud de rester seule ici."

    lysa neutre "Tu sais je préfère..."

    elias inquiet "… Faut pas rester toute seule ici."

    lysa blase "Je sais."

    think "Lysa laisse passer un temps."

    elias fatigue "T'as pas beaucoup parlé aujourd'hui. Hier, t'arrêtais pas."

    lysa reflexion "J’ai écouté."

    elias neutre "Ce n’est pas très reposant."

    lysa taquin "Rien ici ne l’est."

    elias ecoute "Non."

    lysa reflexion "Tu sais comment j'appelle ça ? Orphée."
    lysa blase "Avancer sans regarder derrière, parce qu'on sait très bien ce qui arrive sinon."

    elias reflechit "J'ai pas compris la référence. Mais ouais, survivre."

    lysa surpris "… Oui."
    lysa triste "Voilà."

    think "Je m'approche."
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

    lysa reflexion "Harmonie. Notre district."
    lysa neutre "Les gens entendent avant de regarder."

    elias raison "Alors dis-leur."

    lysa triste "Dire quoi ?"
    lysa blase "Qu’on manque déjà de tout ?"
    lysa neutre "Ils le savent."

    noam culpabilite "Tous les districts ont des problèmes, enfin... je crois que—"

    lysa opposition "Justement."

    think "Lysa regarde le sol."

    elias fatigue "T'es pas obligée de parler à la réunion."

    lysa determine "Si je ne parle pas…"
    lysa reflexion "On parlera pour moi."

    noam hesitation "Tu as peur ?"

    lysa peur "Ouais. Mais toi aussi."

    noam panne "Ouais."

    lysa neutre "Alors n’essaie pas d’être solide."
    lysa blase "Ça se voit quand ça sonne faux."

    noam culpabilite "Je fais ce que je peux."

    lysa triste "Moi aussi."

    elias ecoute "Dis juste l'essentiel. C'est déjà bien."

    lysa reflexion "L’essentiel fait toujours mal."

    elias neutre "Ouais. Mais les gens s'en souviennent."

    think "Lysa souffle longuement."

    lysa determine "Je viendrai."
    lysa reflexion "On tirera ça au clair."
    lysa blase "Mais j’ai des réserves sur ce vote…"
    lysa neutre "Si on manque déjà de tout là-bas…"
    lysa reflexion "autoriser les échanges, le commerce…"
    lysa fatigue "ça risque pas d’empirer les choses ?"

    noam raison "C'est possible."
    noam raison "Pour tout te dire, je ne sais pas. Enfin, pas encore."

    lysa triste "Ne promets pas trop vite."

    noam neutre "On en parlera demain. Enfin... si tu veux."

    lysa triste "Oui."
    lysa triste "Avant que je change d’avis."
    lysa blase "J’ai pas envie de briser leurs espoirs…"
    lysa determine "mais tu as compris."
    lysa fatigue "... C’est déjà ça."

    call day2_collect_vote_argument("approvisionnement") from _call_day2_collect_vote_argument_approvisionnement

    tuto "Un argument rangé dans la mallette apparaît dans l'onglet Prochain vote."
    tuto "Les notes ne décident pas à ta place : elles servent à préparer le vote et à relire les positions supposées."


    $ hideGroup()

    think "Elle se redresse et s'éloigne. Je repars vers la salle d'observation."

    jump _2_SALLE_OBSERVATION

# Durée : 1m50
# Total : 1h 18m 10s

label _2_SALLE_OBSERVATION:
    scene bg_observation at adaptive_fullscreen with dissolve

    think "Derrière la baie vitrée : le vide, immense et calme. Kael est déjà là."

    menu:
        "Avant de parler à Kael."
        "Examiner brièvement la salle.":
            think "Les consoles, la vitre, les modules : ici, tout ramène à Orbite."
        "Regarder la baie vitrée.":
            think "Orbite paraît calme de loin. C'est presque pire."
        "Aller directement vers lui.":
            think "Je ne laisse pas le silence s'installer."


    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam neutre "Kael. Tu sais où on est ? Enfin... précisément."

    kael neutre "Non."
    kael reflechit "Matériel d'Orbite. Architecture orbitale."

    noam raison "Donc on est bien proches de chez toi."

    kael doute "Orbite est immense. Proche ne veut rien dire ici."
    kael jaloux "Mais oui. Nous sommes probablement dans mon district."

    noam inquiet "Ça te rassure ?"

    kael colere "Non."
    kael colere "Ce lieu prouve que tout était prévu."

    noam inquiet "Tu crois qu’ils ont prévu le vote aussi ?"

    kael mefiant "Le texte, peut-être pas. Nos réactions, oui."

    noam raison "Il me semble qu’on n’est pas encore divisés."

    kael colere "Nous le sommes."
    kael colere "Sinon, tout le monde aurait parlé hier."

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

    noam inquiet "Tu penses qu'on peut tenir un consensus ?"

    kael raison "Personne n'est ouvertement contre."
    kael inquiet "Ça ne suffit pas."
    
    noam reflexion "Pourquoi ça ? Chez toi, sur Orbite, comment vous gérez les appros ?"

    kael doute "Rations quotidiennes. Demande officielle pour le matériel. Attente."

    noam reflexion "Comme partout, alors. Enfin, je crois."

    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement

    noam neutre "Le commerce pourrait améliorer ça. Des magasins, du libre accès... peut-être."

    kael raison "Peut-être."
    kael doute "Toute infraction supplémentaire augmente le risque d'un tir."

    noam neutre "Il suffit de respecter les règles, non ? Enfin... en théorie."

    kael colere "Pas sur Orbite."
    kael colere "Nous vivons dans des modules pressurisés."

    think "Il déglutit. Pour la première fois, chaque mot semble lui coûter plus que son silence."

    kael inquiet "Une personne commet une infraction. Le laser perce la coque."
    kael inquiet "Tout le module perd son oxygène."

    noam triste "Hein ?!"
    noam triste "Mais c'est pas juste !"

    kael inquiet "La justice n'entre pas dans le calcul."
    kael inquiet "Nous avons des masques partout. Ils ne sauvent pas tout le monde."

    $ hideGroup()

    kael triste "Excuse-moi. J'ai besoin de vérifier quelque chose."

    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite


    think "Je reste face au vide et compte mes respirations."
    think "Juliette chantait faux pour chasser les cauchemars. Là, même ses chansons me manquent."

    pause 0.6
    jump _2_GYMNASE

# Durée : 2m15
# Totale : 1h 20m 25s

label _2_GYMNASE:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen with dissolve

    think "Le bruit régulier des machines couvre presque les pensées. Iris enchaîne les répétitions ; Elias compte."


    $ showGroup([
        ("iris", "determine", 0.49),
        ("elias", "neutre", -0.11),
    ])

    iris determine "Encore. Tant que mes muscles brûlent, mon cerveau ferme enfin sa gueule."

    elias ecoute "Respire. Sinon tu te fatigues pour rien, c'est chaud."

    think "Je m'approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "hesitation", 0.13),
        ("iris", "determine", 0.49),
    ])


    noam hesitation "Je dérange ?"

    iris taquin "Tant que tu ne prends pas ma place et que tu ne te blesses pas de façon stupide. J'ai déjà assez de travail."

    elias ecoute "Non."
    elias neutre "Ça tombe bien."
    elias joie "Tu veux apprendre ? J'peux te montrer."

    noam surpris "Euh…"
    noam neutre "Je crois."

    iris determine "Alors bouge au lieu de regarder. Il y a des bancs libres."

    elias "Celui-là. Assieds-toi."

    elias joie "On commence simple."

    think "Le métal est froid sous mon dos."

    elias raison "Stop. Ton dos. Expire en poussant, inspire en descendant."
    elias detendu "Tu bloques, t'es mort à la troisième rep. Enfin pas mort, mais c'est chaud."


    iris taquin "Développé-couché dès la première séance ? Excellent. J'avais justement envie d'assister à une panne musculaire."

    noam inquiet "Je tremble déjà rien que d'y penser."

    elias ecoute "C'est pas si difficile."
    elias detendu "Ne lutte pas."
    elias detendu "Accompagne le mouvement."

    think "Je soulève. Beaucoup plus lourd que prévu."

    elias ecoute "Pas comme ça."
    elias detendu "Moins vite."
    elias detendu "Contrôle la descente."

    think "Je recommence. Ça brûle."

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

    think "Je pousse les haltères."

    $ mg_skip_scene_pick = True
    call minijeu_halteres from _call_minijeu_halteres

    think "Je repose et récupère l'usage de mes poumons."
    $ mg_skip_scene_pick = False

    pause 0.6

    elias joie "T'as senti ? C'est ça. Mais une fois tous les quinze jours, ça sert à rien."
    elias raison "Tu viens souvent. Force, endurance, concentration. Le corps comprend le concret."

    iris determine "Et parfois, c'est juste pour ne pas rentrer et tout casser."
    iris taquin "La fonte coûte moins cher qu'un psy et pose moins de questions idiotes."

    pause 0.4

    noam reflexion "Donc…"
    noam reflexion "Si je ne fais rien…"

    elias neutre "Tu stagnes. Et plus tard, ton corps te le fait payer."

    think "Mes mains tremblent encore."

    noam neutre "Je reviendrai."

    iris sourire "Bonne idée."

    elias ecoute "Je serai là."
    elias raison "Mais la prochaine fois, on commence sans que tu trembles avant même de toucher la barre, hein ?" 


    $ hideGroup()

    think "Je quitte la salle. Les machines continuent, régulières et implacables."

    scene bg_couloir at adaptive_fullscreen with dissolve
    think "L'heure tourne. Mon estomac me ramène à la cafétéria."

    jump _2_CAFETERIA_SOIR

# Durée : 1m50
# Totale : 1h 22m 15s

label _2_CAFETERIA_SOIR:
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    think "La cafétéria se remplit par vagues. Nyra tient déjà une table en haleine."
    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("nyra", "neutre", 0.96),
    ])

    nyra sourire "À Orbite, on mangeait en décalé. Quel rythme vous aviez, à Harmonie ?"
    nyra sourire "Là-haut, le silence faisait partie du travail. Ici, j'ai l'impression qu'il faut le mériter."

    noam hesitation "Tu regrettes ?"

    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("kael", "neutre", 0.84),
        ("nyra", "sourire", 0.96),
    ])

    kael neutre "La routine me manque."
    kael neutre "Pas l'endroit."


    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("kael", "neutre", 0.84),
        ("elen", "taquin", 0.72),
        ("nyra", "sourire", 0.96),
    ])

    elen taquin "Orbite, c'était comment ? On entend vraiiiment n'importe quoi !"
    elen content "Vous dormez en flottant ? Et les repas, ils se baladent ? Imagine une soupe en apesanteur !"

    kael neutre "On flotte dans certaines sections."
    kael neutre "La vaisselle reste attachée."

    nyra taquin "Kael oublie la fois où un ragoût a bloqué une grille de ventilation."
    kael mefiant "Je n'oublie pas. Je choisis de ne pas raconter."


    $ showGroup([
        ("noam", "inquiet", 0.13),
        ("kael", "neutre", 0.84),
        ("tomas", "neutre", 0.60),
        ("elen", "content", 0.72),
        ("nyra", "taquin", 0.96),
    ])

    tomas hesitation "Et… euh… vous aviez aussi des médiateurs, chez vous ?"
    tomas inquiet "Des… assemblées, ou un truc comme ça ? C-Comment vous faisiez pour prendre les décisions ?"

    kael calme "Protocoles techniques. Chaînes de responsabilité."
    kael rire "Moins de spectacle."

    noam inquiet "Ça te fait quoi de tout revoir ici ?"

    kael reflechit "Comprendre. Ne plus obéir par réflexe."

    nyra raison "Et si tu ne comprends pas à temps ?"

    kael neutre "Je continue."

    tomas inquiet "Et si on fait une erreur ..?"

    kael triste "Une erreur sur Orbite tue. Alors on vérifie."

    nyra raison "Donc tu ne réponds pas à sa question."
    kael neutre "Non."


    elen triste "Je me demande si nos familles nous regardent en ce—"
    elen surpris "Oh ! Vous avez goûté la purée ? Elle a un goût différent ce soir, non ? Plus salé, ou moins jaune, ou—"
    think "Le virage est si brutal que personne ne répond tout de suite."

    kael reflechit "On ne vote pas uniquement pour eux."

    elen triste "Ouais. Tout le monde."

    kael neutre "Oui."
    kael triste "C’est ça, être ici."

    elen triste "Je déteste ça."
    elen surpris "Enfin, c'est peut-être la purée. Vous trouvez pas qu'elle est bizarre ?"

    nyra raison "Tu n'es pas obligée de finir cette phrase."
    nyra sourire "Mais tu peux, si tu veux."

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

    ryn neutre "Vous êtes calmes. Je m'attendais à des cris."

    kael neutre "Tu es déçu ?"

    ryn sourire "Peut-être. Ils viendront après."

    noam inquiet "Tu penses qu’on va se déchirer ?"

    ryn reflechit "On va se désaccorder. Ce sera pas joli."

    kael reflechit "On n’est pas obligés d’être sympa à voir."
    kael reflechit "On doit surtout être honnêtes."

    ryn fatigue "L'honnêteté donne des angles d'attaque."

    noam raison "Elle donne aussi des points d’appui."

    ryn reflechit "Peut-être."
    ryn reflechit "Mais je n’ai pas envie d’être un point d’appui."

    kael neutre "Tu veux être quoi, alors ?"

    ryn neutre "Libre. Je veux Limen libre."

    noam inquiet "Tu ne crois pas qu’on puisse être libre ensemble ?"

    ryn reflechit "Je ne sais pas."
    ryn reflechit "Ça date d'avant Kami."

    noam raison "Alors c’est l’occasion d'essayer de faire avancer les choses."

    noam hesitation "Qu'est ce que tu vas voter ?"

    ryn reflechit "Je penche pour. J'écoute. Je décide demain."

    noam raison "Tu as raison d’être prudent."

    menu:
        "Après la réponse de Ryn."
        "Garder sa position en tête.":
            think "Je garde sa prudence en tête."
        "Reformuler concrètement.":
            noam raison "Donc pour l'instant, tu penches pour, mais tu veux entendre les autres."
            ryn reflechit "Voilà. C'est déjà pas mal, non ?"
        "Continuer à écouter.":
            think "Je n'ajoute rien. Une phrase suffit parfois à dessiner une position."


    $ hideGroup()

    think "D'autres se joignent à nous. Questions, souvenirs, comparaisons : la fatigue finit par dissoudre le débat."

    stop music fadeout 1.0
    pause 0.6
    hide screen day2_quick_vote_notes

    scene bg_couloir at adaptive_fullscreen with fade
    pause 1.0
    scene bg_dortoir at adaptive_fullscreen with fade
    pause 1.0
    scene bg_chambre at adaptive_fullscreen with fade
    pause 1.0

    think "Je passe par les douches."

    scene bg_cg011 at adaptive_fullscreen with fade

    think "L'eau chaude efface le bruit de mes pensées."

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    scene bg_chambre at adaptive_fullscreen with fade
    think "Je me sèche, tombe sur le lit et éteins."
    
    scene bg_cg012 at adaptive_fullscreen with fade
    think "Demain sera dense."
    $ blink()
    think "À quatorze heures, on saura si changer les choses est réellement possible."

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
