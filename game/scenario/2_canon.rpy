label _2_CANON:

    $ day_id = 2
    $ current_day = 2
    $ current_period = "Matin"

    scene black
    play music "music/main_menu.mp3" fadein 1.0

    pause 0.6

    think "Je n'arrive pas vraiment à dormir. Je me retourne encore et encore."
    think "Un coup sur le côté gauche. Non, ça ne va pas. Sur le dos, peut-être ? Raah c'est pire. Une jambe repliée... toujours pas."
    think "Le matelas est confortable, même très confortable. Le problème, enfin... c'est moi. C'est tout ce qui nous arrive."

    $ blink()

    pause 0.6

    think "J'ouvre les yeux. Encore une fois."
    scene bg_cg012 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg012")

    $ blink()

    think "Je les referme. J'essaye de me reposer mais rien n'y fait."

    $ blink()
    pause 0.4
    $ blink()

    pause 0.6

    think "Chaque fois que je commence à m'endormir, des images me reviennent."
    $ blink()
    think "La salle. Les sièges. Les onze autres personnes avec qui je serai bloqué pendant un mois. Un mois..."
    $ blink()
    think "Et puis elle. Kami."
    think "Est-ce que j'ai déposé un bon amendement ? Putain qu'est-ce que j'en sais..."

    pause 0.6

    $ blink()

    play sound sfx_announce

    pause 0.8

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ooooh ? Vous êtes déjà en train de remuer dans vos petits lits ?"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Enfin, je ne peux que spéculer : vous n'êtes pas nombreux à avoir désactivé votre brouilleur !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "C’est mignon. Vraiment. J'espère que certains d'entre vous ont pu passer une bonne nuit !"
    kami "Mes valeureux serviteurs ont eu bien du mal à vous fabriquer des lits d'aussi bonne qualité !"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Mais soit. Nous en sommes au deuxième jour."
    kami "J'espère que vos vacances se passent pour le mieux ?!"

    $ blink()

    kami "Il est huit heures du matin."
    kami "Certains d’entre vous ont l'air d'avoir très mal dormi à en juger par les quelques têtes qui sont déjà sorties de leur chambre."
    kami "Et je tiens à préciser que c'est tout à fait normal…"

    pause 0.5
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Votre cerveau adore ce genre de choses. Vraiment."
    kami "Il appelle ça du stress. Et quand il est stressé…"

    $ blink()

    kami "Il libère du cortisol. Une petite hormone très pratique."

    $ blink()

    kami "Elle vous garde éveillés. Alertes. Prêts à survivre."
    kami "Le problème… C’est qu’elle déteste le sommeil."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Votre cerveau a travaillé tard. Même quand vous faisiez semblant de dormir."
    kami "D'ailleurs il ne s'endort jamais vraiment, lui. Un peu comme moi au final !"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais ce n'est pas pour ça que vous êtes si alertes en m'écoutant, non ?!"
    kami "Ah ! Vous voulez le savoir, hein ! Quelle sera la toute première proposition mise au vote !"
    kami "Et bien, vous le saurez après un court instant publicitaire !"
    kami "En attendant, je vous attends nombreux dans la Salle du Conclave pour la première annonce majeure !"
    kami "Je vous conseille d’y assister. Ce serait dommage de rater un moment clé…"

    pause 0.4
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "…surtout quand il s’agit de votre avenir proche."

    $ blink()
    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    # Réveil réel
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    think "Cette fois, je suis complètement réveillé. Hier, tout s’est enchaîné trop vite pour vraiment réfléchir."
    think "Maintenant, le calme ramène tout ce que j'ai essayé de refouler jusque-là."
    think "Ma famille est à des milliers de kilomètres de là. Qu'est-ce qu'ils font ?"
    think "Que fait Juliette, ma petite sœur, toujours debout trop tôt, toujours en train de poser une nouvelle question avant même d’avoir eu la réponse à la précédente."
    think "Comment lui expliquer ce qu'il se passe ici, au Conclave ? Comment lui expliquer ce que nous fait Kami sans lui apprendre à avoir peur de chaque écran ?"

    pause 0.6

    think "Elle me regarde peut-être en ce moment. Moi, je ne peux ni la voir ni l'aider."
    think "Enfin... Rester allongé n'y changera rien."

    call day2_play_wakeup_trace from _call_day2_play_wakeup_trace

    think "Je me redresse et pose les pieds au sol. Il faut que j'aille à la cafétéria, c'est bien ça ?"

    stop music fadeout 1.0
    pause 0.6

    # Trajet jouable : chambre -> dortoir -> couloir -> cafétéria.
    $ day2_cafeteria_route_nyra_seen = False
    $ day2_cafeteria_route_tomas_seen = False
    $ current_scene_active = "_2_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    $ room_scene_indices["chambre"] = 2
    jump CHAMBRE_TP

# Durée : 2m35
# Total : 1h 7m 25s

label _2_CAFETERIA_ANNONCE_KAMI:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    pause 0.4

    think "Je mets un pied dans la cafétéria, ils sont déjà nombreux à être là."
    play sound sfx_door

    menu:
        "Choisir où se placer."
        "Je m'assois près d'une table encore libre.":
            think "Je tire une chaise sans bruit. D'ici, je vois presque toute la salle."
        "Rester près du buffet.":
            think "Je prends un plateau pour occuper mes mains. Les voix arrivent par morceaux."
        "Me tenir près de l'entrée.":
            think "Je reste près de la porte. Au moins je pourrais voir facilement qui rentre et qui sort. Ce sera aussi plus simple pour repartir aussi."


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

    iris desaccord "Excellente question. Peut-on ignorer une convocation de l'IA qui pourrait tous nous exécuter dans la seconde si ça lui plaisait ?"
    iris colere "Quelqu'un veut tester ? Non ? Question réglée."

    tomas panne "Je—"

    ryn neutre "Moi aussi je préférerais aller autre part."
    ryn reflechit "Je comprends même pas comment tout ça peut nous arriver..."

    elen content "Oh !"
    elen joie "C'est vraiii que l'ambiance est un peu chelou..."
    elen surpris "Oh ! Mais faut voir le bon côté des choses !"
    elen joie "On peut changer les choses en mieux ! Et ici tout est super ultra méga bon !"

    iris desaccord "Ravie de savoir que l'estomac sur patte est content."
    iris colere "Reste à savoir à quelle sauce NOUS allons être mangés."

    elen desaccord "Et bien, quitte à choisir, pas une sauce piquante ! Beurk !"
    elen content "Soyez un peu plus positifs, je vous promets que ça ne tue pas !"
    
    ryn fatigue "Tu es effrayante parfois..."

    pause 0.4

    elias ecoute "… Façon on peut rien faire d'autre que d'attendre. Donc ça sert à rien de se prendre la tête avec ça."
    elias neutre "Ça se trouve la première proposition va être géniale."

    sael raison "Elias a raison, en attendant, il faut profiter de ce bon repas."
    sael mefiant "Mangez. Nous aurons besoin de forces quand le signe viendra."

    pause 0.6

    play sound sfx_door
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

    mara taquin "On vous entend depuis le couloir. Joli comité d'accueil."
    mara neutre "Et blablabla qu'il faut manger, et blablabla qu'il faut paniquer."

    nyra taquin "Tu n'as pas mieux à faire que d'écouter aux portes ?"

    elen joie "Oh Mara ! Viens t’asseoir avec nous, allez ! Ça serait trop cool."

    mara taquin "Merci miss, mais je suis très bien là. Je vois tout le monde comme ça."

    pause 0.4

    ryn neutre "Pfff, à quoi ça va te servir de voir tout le monde, hein..."

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

    lysa blase "Désolée pour le retard."

    tomas inquiet "N-Non non !"
    tomas hesitation "Enfin… y a pas de problème. Vraiment. Aucun problème."

    iris taquin "Ravie de voir que ton retard n'a pas causé ta mort."
    iris taquin "Flemme de nettoyer les couloirs après ça."

    lysa reflexion "À en juger par le monde dans la salle, il doit encore en manquer."

    noam reflexion "Espérons qu'ils se dépêchent."

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

    kael neutre "Pfiouu, pile à temps. Il manque encore quelqu'un ?"

    iris colere "Franchement, j’ai la flemme de compter."
    iris desaccord "On va dire que non, point barre. Ça vous va ?"

    play sound sfx_announce

    pause 2.0

    stop music fadeout 0.8

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh. Quelle belle image."
    kami "Des visages tendus, des regards méfiants… On dirait presque une réunion de famille ratée."
    kami "Mais qui est l'abruti qui a osé parler de politique ou d'argent ?!"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Jour deux. Il est neuf heures."
    kami "Et vous êtes tous... Ah non. Il manque quelqu'un."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Et bien, tant pis pour le retardataire !"

    pause 0.4

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "J’adore quand vous essayez d'anticiper. Quand vous essayez de deviner."
    kami "Ça vous rend… délicieusement prévisible."

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn neutre "Elle va y venir ou pas ?"
    $ bc_hide()

    kami "Oh. L’impatience. Un si joli défaut."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais moi, contrairement à vous, j'ai tout mon temps ! Mais c'est vrai que si nous voulons profiter de notre mois ensemble, il faut accélérer !"
    kami "Le premier vote du Conclave a été tiré au sort."

    $ bc_show("tomas", "surpris", px=-70, py=-50, pz=0.85)
    tomas surpris "D-Déjà ?!"
    $ bc_hide()

    kami "Oui. Déjà. Mais ça je l'avais annoncé dès hier. Essayez de suivre les enfants."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Je suis efficace. MOI."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'avais peur que vous vous ennuyiez ici. Je vous donne donc un sujet de discussion."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Et voici le résultat tant attendu. La proposition pour laquelle vous devrez voter..."
    kami "Attention, roulement de tambour !"

    play sound sfx_tambour
    pause 2.0

    kami "Je cite : « ça serait bien qu'on réautorise le commerce comme avant. »"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais qui a écrit ça ?! C'est... Comment dire... Bon, je pouvais pas en attendre mieux après tout."
    kami "Au moins tout le monde a compris l'idée de la proposition !"

    pause 0.8

    $ bc_show("sael", "surpris", px=-70, py=-50, pz=0.85)
    sael triste "Le commerce ?!"

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra taquin "Intéressant, mais ça voudrait aussi dire changer complètement ce nouveau monde."

    $ bc_show("iris", "triste", px=-70, py=-50, pz=0.85)
    iris colere "L'idée est mieux qu'attendue."
    $ bc_hide()

    pause 0.6

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Mais ils vont me laisser parler ces petits cons ?!"
    think "Le silence tombe instantanément."
    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bon. Habituellement vous auriez eu trois jours pour discuter de cette proposition."
    kami "Pour discuter. Pour convaincre les autres. Ou pour égorger ceux qui s'apprêtent à voter contre."
    kami "Ça, c'est de votre ressort."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais nous sommes déjà au jour 2. Or le premier vote a lieu à la fin du troisième jour !"
    kami "Vous n'avez donc qu'une journée pour vous décider. Mais zen. Vous allez y arriver."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je rappelle que pour que cette volonté soit faite, personne ne devra voter contre..."
    kami "Si la moindre personne vote contre. La proposition tombe à l'eau."

    pause 0.6

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je vais devoir réécrire ça au propre. C'est impossible d'inclure une formulation aussi enfantine dans mes merveilleux commandements !"

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Amusez-vous bien. Le monde vous écoute."

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

    tomas hesitation "… C’est… c’est sérieux, là. On peut vraiment genre revenir au système d'avant ?"

    nyra sourire "A priori, oui. Enfin, si Kami respecte vraiment l'idée proposée."

    elen joie "Et si on essayait d'en parler calmement ? Tous ensemble ?"
    elen content "Moi je trouve que l'idée est vraiment cool !"

    ryn taquin "Ah ouais, tu trouves ça cool toi ?"

    elen sourire "Bah ouais ! On pourra de nouveau acheter tout ce qu'on veut !"
    elen joie "On ne sera plus obligé de demander tout le temps des dérogations à nos districts !"

    sael raison "Des dérogations ? De quoi est-ce que tu parles ?"

    elen surpris "Hein ? Bah de remplir tous ces papiers ultra loooongs pour avoir un peu de matériel !"
    elen triste "Vu qu'avec les bons de rationnement on ne pouvait avoir que de la nourriture pourrie, pour tout le reste il faut tout le temps demander !"

    sael reflechit "Des bons de rationnement ? Je connais pas."

    ryn colere "Hein ? Mais qu'est-ce que tu racontes ?"
    ryn reflechit "Heureusement qu'il y a les bons de rationnement, sinon à Limen tout le monde crèverait la bouche en cœur !"

    mara taquin "Revenir au système de commerce ? MDR ! Qui a proposé ça ?"
    mara colere "Je dois vous rappeler ce que c'est que ce système de commerce ?"

    iris colere "Oh par pitié, tu ne vas quand même pas nous faire la leçon..."

    mara colere "C'est un système où les riches peuvent tout acheter et où les pauvres doivent se démerder."

    elias colere "Hein ? Pourquoi c'est toi qui t'attaque à ça ? T'es bien la fille Shiran, non ?!"

    mara colere "Je m'appelle Mara, c'est tout."

    noam calme "Oh oh ! Stop, on se calme tout le monde ! On peut..."

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
    julian surpris "Qu'ai-je manqué ? C'était quoi tous ces cris ?"

    nyra raison "Pouah ! Quelle entrée ! Tu ne vas pas me faire croire que tout ça n'était pas préparé !"

    pause 0.6

    julian sourire "Reprenons clairement. Où en sommes-nous ?"

    iris colere "Tu arrives en retard et tu demandes un récapitulatif personnalisé. Pourquoi ça ne m'étonne pas ?"

    julian decu "Tu pourrais résumer pour ton plus ancien allié ici."

    iris sourire "Mon allié ? Tu as tenté de me séduire pendant six mois. En étant assez lourd, je dois bien l'avouer."

    julian sourire "Très bien. JE reconstituerai seul la situation."
    julian reflexion "Kami a annoncé un vote. À voir vos visages..."

    think "Il regarde patiemment chaque visage, tout en gardant son meilleur angle pour la caméra."

    julian reflexion "La proposition n'est pas manifestement hostile. Vous êtes plusieurs à être convaincus."
    julian sourire "Laissez-moi deviner... Oui c'est ça ! Une réouverture du commerce !"

    iris intervention "Comment tu as—"

    julian taquin "Julian a une très bonne intuition. Mes prédictions tombent juste 30%% du temps !"

    lysa blase "Pourquoi il me semble avoir déjà entendu ça quelque part...?"

    elias taquin "C'est pas compliqué à comprendre."
    elias ecoute "Y a des écrans partout. La diffusion tournait dans le couloir. C'est chaud de faire genre t'as deviné."

    julian panne "… T'aurais pas pu te taire, hein ?!"

    $ j2_vote_codex_unlocked = True
    call screen day2_vote_tablet_notice
    think "La tablette vibre dans ma poche. Je la sors. Une notification est notée dessus : Nouveau dossier de vote."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m35
# Total : 1h 11m 0s

label _2_CAFETERIA_POST_ANNONCE:

    show screen day2_quick_vote_notes

    think "Tout le monde sort sa tablette."

    kael reflechit "Ah, la formulation est là."

    elias triste "hein ? Attendez, montrez-moi, j'ai pas ma tablette !"

    kael reflechit "« Ça serait bien qu'on réautorise le commerce comme avant. »"
    kael neutre "La formulation est soumise à changement."

    noam inquiet "Hein ? Soumise à changement ? Qu'est-ce qu'elle veut dire exactement ?"
    noam reflechit "Elle va modifier la formulation et on devra voter dessus demain ?"

    lysa colere "Ça veut surtout dire que c'est un piège évidemment."

    sael raison "C'est peut-être trop beau pour être vrai. Il faut se méfier de nos certitudes."

    kael neutre "L'amendement vient en théorie de l'un de nous. La volonté est claire en tout cas."
    kael inquiet "Ce qui est risqué, ce n’est pas l’intention, mais les conséquences de la manière dont ce sera formulé."

    mara neutre "Ce qui est risqué c'est de retomber dans le capitalisme qui a causé toutes ces guerres."

    nyra raison "Qu'est-ce que tu veux dire, Mara ?"

    mara triste "Pff. Vous ne voyez pas où ça nous mène ?"
    mara triste "Si on réautorise le commerce, il faudra une valeur à échanger. De l'argent en gros."
    mara peur "Ce sera le retour au travail, à l'argent et aux inégalités."

    iris colere "Et en quoi c'est problématique, hein ?!"
    iris colere "Si travailler est le prix pour être libre, où est le problème ?"

    elen triste "Tu vas quand même pas me dire que t'es contente du système actuel, Mara ?"

    mara colere "..."
    mara triste "Tu travaillais à la Forge, Elias, non ?"

    elias reflechit "Hein ? Oui, pourquoi ? Qu'est-ce que j'ai à voir avec ça ?"

    mara reflechit "Tu étais content de travailler là-bas ? Te faire exploiter pour pas grand-chose."

    elias reflechit "Ça change pas vraiment d’aujourd’hui, à vrai dire."

    mara surpris "Hein ? Tu continues à travailler ? Pourquoi ? Tu y es obligé ?"

    elias sourire "C'est la seule chose que je sais faire. Et même si on est plus payé, je me dis que ce que je fabrique servira toujours à quelqu'un d'autre."
    elias sourire "Alors oui, c'est pas facile. Ça c'est clair. Mais si je peux être utile..."
    
    mara colere "Me dis pas que tu préférais le système d'avant ?"

    elias reflechit "Sur le commerce ? Si, c'était bien mieux quand chacun pouvait acheter ce dont il avait besoin."

    nyra taquin "Factuellement, quelqu'un a quelque chose à perdre si les échanges reprennent ?"
    nyra raison "Il faut qu'on en parle pour savoir quels sont les points de blocage."

    iris colere "Actuellement, plus flou tu meurs. Faudrait avoir plus de précisions sur ce qui serait mis en place si on venait à voter pour."

    mara taquin "Tu sais que t'es sexy quand tu deviens sérieuse ?"

    iris surpris "Hein ?! Je— Ce n'est pas le sujet !"

    mara sourire "Dommage. Continue quand même."

    iris colere "Sérieusement… Et ça veut dire qu’on va devoir causer de tout le reste ensemble. L'enfer."

    kael reflechit "On ne peut pas vraiment esquiver cette question, demain, il va falloir faire le bon choix et voter."

    elen joie "On peut essayer d’être d’accord, non ? Juste une fois. Rien qu’une."
    elen joie "Pour pas leur filer exactement ce qu’ils attendent de nous. Puis si on peut de nouveau avoir accès à tout ce qu'on veut ! Moi je vote pour !"

    iris colere "Ils veulent du spectacle. Du vrai drama de téléréalité."

    elen content "Franchement… la proposition a pas l’air si pourrie que ça, si ?"
    elen joie "Je veux dire… y a claiiirement pire, non ?"

    think "Personne ne répond. Personne ne proteste non plus."

    sael raison "Souhaiter l'accord est une bonne chose. Prendre cette formulation pour acquise en est une autre."

    tomas hesitation "Je… Je pense que c’est important. Parce que ça concerne nos districts. Directement."
    tomas inquiet "Et si on peut faire circuler des choses entre nous… Ben… on peut aussi s’entraider, non ?"

    kael surpris "C'est-à-dire ?"

    tomas hesitation "S-Si on autorise le commerce, alors il pourra y avoir du transport de médicaments, de matériaux, ou… ce genre de choses..."
    tomas surpris "Et pourquoi pas des gens, aussi. À un moment donné."

    noam inquiet "Les gens, c’est autre chose. La proposition ne parle que du commerce."

    tomas hesitation "O-Ouais. Je sais… M-Mais si les échanges deviennent autorisés… alors peut-être que…"

    mara taquin "C’est mignon tout ça, mais qui va surveiller ces petits échanges ?"
    mara reflechit "Qui va faire en sorte que TOUT LE MONDE soit livré ? Qu'il n'y ait pas tout dans un district et rien dans un autre ?"

    tomas hesitation "On n’a pas les détails."

    kael reflechit "Justement. On devra décider sans."

    mara neutre "Décider à l’aveugle, ou presque. J’adore quand on improvise avec nos vies."

    tomas colere "Du coup… on doit se faire confiance. Voilà."

    nyra taquin "Qu'est-ce qu'on sait ? Qu'est-ce qu'on ignore ?"
    nyra raison "Commençons par là. Chacun pourra ajouter ce qui concerne son district."

    mara taquin "T’as de quoi pondre un roman sur tout ce qu’on sait pas ?"

    nyra taquin "Je veux une base."

    kael reflechit "Elle a raison. Sinon on va se bouffer entre nous."

    elen joie "Oh ! Je peux prendre des notes ! J'écris super vite quand je panique."
    elen content "Et après je peux faire des catégories. Avec des couleurs ! J'ai toujours aimé ça !"

    julian surpris "Adjugé, vendu ! Elen, tu seras ma secrétaire préférée !"

    elen joie "O-Ouais trop bien !"

    julian joie "Il nous faut une méthode. On ne peut pas tourner en rond jusqu'au vote."

    iris surpris "Tu proposes quoi, là, concrètement ? Vas-y, je t’écoute."

    julian sourire "Il faut que chacun note les besoins de ses districts. Demain, nous mettons tout en commun."
    julian taquin "Il faut nous coordonner pour le débat de demain."

    iris colere "Dire qu’on réfléchit, c’est super facile à balancer."
    iris desaccord "Le faire vraiment, par contre… c’est une autre paire de manches."

    nyra peur "Moi j'ai une question avant ça. C'est par rapport aux règles."
    nyra reflechit "Est-ce que quelqu'un votera contre quoi qu'il arrive ? Qu'on ne perde pas du temps pour rien."

    think "Tout le monde se regarde, personne ne parle."

    nyra taquin "Donc, tu pourrais ne pas voter contre, Mara ?"

    mara taquin "Je verrai... Si vous le voulez tant ce changement, au pire je ne voterai pas."
    mara taquin "Je suis pas une salope non plus."

    sael desaccord "Une voix contre suffit. Ceux qui ne veulent pas se livrer doivent pouvoir garder le silence."

    noam reflechit "Tu pourrais voter contre Sael ?"

    sael reflechit "Je ne sais pas. Là où j'habite, on ne commerçait déjà pas avant Kami. Quel que soit le résultat du vote, ça ne changera rien pour nous."
    sael inquiet "Si vous avez besoin qu'on vote pour, alors je suivrai ce que décide le groupe."

    ryn colere "Mais tu viens d'où en fait ? Déjà tout à l'heure tu disais ne pas savoir ce que sont les bons de ravitaillement ?"

    sael reflechit "Je viens d'une tribu située au pied du Mont Kensen."
    sael sourire "Chez nous, pour tout vous dire, l'arrivée de Kami n'a rien changé."
    sael sourire "Nous ne faisions pas de commerce, nous ne demandions rien. Tout le monde travaillait constamment."
    sael joie "Alors quand la divine Ka-"

    ryn colere "DIVINE ?! Mais t'as pété un plomb ou quoi !"

    noam colere "Laisse-la parler au lieu de crier."

    sael sourire "Merci mais j'ai l'habitude de ce genre de réaction. C'est ce à quoi on est habituée quand on est cheffe de tribu."

    elen joie "Ouaah t'étais la cheffe de ton village ?! Mais t'es toute jeune pourtant !"

    sael sourire "Bref, l'arrivée de Kami n'a absolument rien changé à notre quotidien."
    sael reflechit "Enfin si, elle se chargeait d'éliminer les plus violents et dangereux d'entre nous."

    elias sourire "Wow, sacrée histoire. Je vois ce que tu veux dire."
    elias triste "Au moins, Kami a mis fin à la violence. Alors c'est pas parfait, hein, mais c'est déjà ça."

    mara doute "Bref, pendant que vous perdez votre temps à papoter… Kami nous mate."
    mara taquin "Elle grave tout : qui parle, qui propose quoi, qui va péter les plombs en premier."

    iris desaccord "Alors on craque pas. Personne ne craquera. OK ?"

    mara neutre "C'est facile à dire. T'as déjà l'air d'être la première à craquer."

    tomas hesitation "Et si quelqu’un vote contre ?"

    noam reflechit "Alors c'est la démocratie. On ne va forcer personne à voter pour. Personne."

    think "Les chaises raclent. Les plateaux s'éloignent. La réunion se dissout sans véritable conclusion."


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

    $ current_period = "Après-midi"

    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    show screen day2_quick_vote_notes

    $ showGroup([
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("sael", "mefiant", 1.20),
    ])

    mara mefiant "Tu penses vraiment qu’ils vont nous laisser voter tranquilles ? Tout va évidemment être manipulé."

    sael mefiant "Kami n'a pas besoin de nous orienter. Elle attendra que nos peurs le fassent."

    mara taquin "T'es toujours aussi rassurante."
    sael neutre "Je ne cherche pas à te rassurer."

    think "Le silence tranche la conversation."

    mara stress "À plus tard."
    mara doute "… si tout a pas déjà explosé d’ici là."


    $ hideGroup()

    think "Je les laisse derrière. Au tournant suivant, Lysa est adossée au mur, Elias face à elle."

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("lysa", "triste", 0.25),
    ])

    elias ecoute "Tu devrais parler avec nous. Si tu veux. C'est chaud de rester seule ici."

    lysa neutre "Tu sais je préfère... Ouais, fin- Je sais..."

    pause 1.0

    elias fatigue "T'as pas beaucoup parlé aujourd'hui. Hier, t'arrêtais pas."

    lysa reflexion "Ouais. J’ai écouté."

    elias neutre "Ce n’est pas très reposant."

    lysa taquin "Je pense qu'on aura pas beaucoup l'occasion de se reposer ici..."

    elias ecoute "Non. Mais il va bien falloir qu'on survive."

    think "Je m'approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "inquiet", 0.13),
        ("lysa", "triste", 0.25),
    ])


    noam hesitation "Ça va ?"

    lysa determine "Ça va comme ça peut."

    elias ecoute "On va avoir besoin de toi pour le débat."

    lysa opposition "Vous allez surtout parler. Moi, on m’écoutera à moitié."

    noam inquiet "Pourquoi tu penses ça ?"

    lysa reflexion "Tu crois qu'ils nous prennent au sérieux ? On vient d'Harmonie, je te rappelle !"
    lysa neutre "C'est notre district qui les fait tous chier avec l'administratif !"
    lysa colere "Comment tu veux qu'ils nous écoutent ?"

    noam surpris "Je suis pas d'accord avec toi."
    noam surpris "S'il y a deux représentants de chaque district, c'est qu'il y a une raison."

    lysa triste "Tu veux leur dire quoi ? Qu’on manque déjà de tout ?"
    lysa blase "Ils le savent."

    noam culpabilite "Tous les districts ont des problèmes, enfin... je crois que—"

    lysa opposition "Justement."

    think "Lysa regarde le sol."

    elias fatigue "T'es pas obligée de parler à la réunion."

    lysa determine "Bof. J'ai pas envie, mais si je ne parle pas… On parlera pour moi."

    noam hesitation "Tu as peur ?"

    lysa peur "Ouais. Mais toi aussi."

    noam panne "Ouais. C'est peut-être un signe montrant qu'on est sain d'esprit ?"

    lysa blase "Alors n’essaie pas de faire le gars solide. Ça se voit quand ça sonne faux."

    noam culpabilite "Je fais ce que je peux."

    lysa determine "Je viendrai. On tirera ça au clair."
    lysa blase "Mais j’ai des réserves sur ce vote…"
    lysa reflexion "Si on manque déjà de tout là-bas… autoriser les échanges, le commerce…"
    lysa fatigue "Ça risque pas d’empirer les choses ?"

    noam raison "C'est possible. Pour tout te dire, je ne sais pas. Enfin, pas encore."

    lysa blase "J’ai pas envie de briser leurs espoirs… mais tu as compris."

    call day2_collect_vote_argument("approvisionnement") from _call_day2_collect_vote_argument_approvisionnement

    tuto "Vous venez de gagner un argument. Une information majeure qui pourra être utilisée au cours du débat."
    tuto "Vous pouvez consulter vos arguments sur votre tablette dans l'onglet Dossier de vote."

    $ hideGroup()

    think "Elle se redresse et s'éloigne. Je repars vers la salle d'observation."

    jump _2_SALLE_OBSERVATION

# Durée : 1m50
# Total : 1h 18m 10s

label _2_SALLE_OBSERVATION:
    scene bg_observation at adaptive_fullscreen with dissolve

    think "Derrière la baie vitrée : le vide, immense et calme. Kael est déjà là."

    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam neutre "Kael. Tu sais où on est ? Enfin... précisément."

    kael neutre "Non."
    kael reflechit "Si ce n'est que c'est du matériel d'Orbite."

    noam raison "Donc on est bien proches de chez toi."

    kael doute "Orbite est immense. Proche ne veut rien dire ici."
    kael jaloux "Mais oui. Nous sommes probablement dans mon district."

    noam inquiet "Ça te rassure ?"

    kael colere "Non. Ce lieu prouve que tout était prévu."

    noam inquiet "Tu crois qu’ils ont prévu l'issue du vote aussi ?"

    kael mefiant "Le texte, peut-être pas. Nos réactions, oui."

    noam raison "Il me semble qu’on n’est pas encore divisés."

    kael colere "Nous le sommes. Sinon, on aurait tous discuté hier avant de déposer nos amendements."

    pause 0.6

    play sound sfx_announce
    pause 0.8

    stop music fadeout 0.6
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petite annonce, l'un d'entre vous m'a demandé l'heure du vote demain."
    kami "Le vote aura lieu demain à quatorze heures. Soyez ponctuels."

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

    noam inquiet "Quatorze heures. On y sera vite."

    kael mefiant "C’est clair."

    noam inquiet "Tu penses qu'on peut réussir à valider ça ?"

    kael raison "Personne n'est ouvertement contre. Donc je ne sais pas."
    kael inquiet "Moi-même, je ne sais pas quoi faire..."
    
    noam reflexion "Pourquoi ça ? Chez toi, sur Orbite, comment vous gérez les approvisionnements ?"

    kael doute "On reçoit suffisamment de stocks pour assurer les rations quotidiennes. C'est un peu comme ici, on a une dizaine de jours d'attente entre chaque livraison."
    kael sourire "Puis on a quelques serres qui produisent quelques aliments, mais on dépend beaucoup de l'extérieur."

    noam reflexion "Comme partout, alors. Enfin, je crois."

    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement

    noam neutre "Le commerce pourrait améliorer ça. Des magasins, du libre accès... peut-être."

    kael raison "Peut-être, mais-"
    kael doute "Chaque commandement supplémentaire augmente le risque d'un tir."

    noam neutre "Il suffit de respecter les règles, non ? Enfin... en théorie."

    kael colere "Pas sur Orbite. On vit dans des modules pressurisés."
    kael inquiet "Si une personne commet une infraction, le laser l'élimine, et il perce la coque du vaisseau."
    kael inquiet "Tout le module perd son oxygène."

    noam triste "Hein ?! Comment vous faites alors ?!"

    kael inquiet "La justice n'entre pas dans le calcul. Nous avons des masques à oxygène partout. Ils ne sauvent pas tout le monde."

    $ hideGroup()

    kael triste "Excuse-moi. J'ai besoin de vérifier quelque chose."

    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite

    think "Je reste face au vide et compte mes respirations."
    think "Juliette chantait faux pour chasser les cauchemars. Là, même ses chansons niaises me manquent."

    pause 0.6
    jump _2_GYMNASE

# Durée : 2m15
# Totale : 1h 20m 25s

label _2_GYMNASE:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen with dissolve

    think "Le bruit régulier des machines couvre presque les pensées. Iris enchaîne les répétitions ; Elias, lui, les compte."

    $ showGroup([
        ("iris", "determine", 0.49),
        ("elias", "neutre", -0.11),
    ])

    iris determine "Encore. Tant que mes muscles brûlent, mon cerveau ferme enfin sa gueule."

    elias ecoute "Respire. Sinon tu vas te fatiguer pour rien."

    think "Je m'approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "hesitation", 0.13),
        ("iris", "determine", 0.49),
    ])


    noam hesitation "Je dérange ?"

    iris taquin "Pas tant que tu ne prends pas ma place et que tu ne te blesses pas de façon stupide. J'ai déjà assez de travail."

    elias ecoute "Non. Tu tombes bien."
    elias joie "Tu veux apprendre ? J'peux te montrer."

    noam surpris "Euh… Je crois ?"

    iris determine "Alors bouge au lieu de me mater. Il y a des bancs libres."

    elias "Celui-là. Assieds-toi."
    elias joie "On commence simple."

    think "Le métal est froid sous mon dos."

    elias raison "Stop. Ton dos. Expire en poussant, inspire en descendant."
    elias detendu "Tu bloques, t'es mort à la troisième rep. Enfin pas mort, mais c'est chaud."

    iris taquin "Tu lui fais commencer par du développé couché dès la première séance ? Excellent. Le spectacle sera amusant !"

    noam inquiet "Je tremble déjà rien que d'y penser."

    elias ecoute "C'est pas si difficile. Ne lutte pas. Accompagne le mouvement."

    think "Je soulève. Ouh ! C'est beaucoup plus lourd que prévu."

    elias ecoute "Pas comme ça. Va moins vite. Contrôle la descente."

    think "Je recommence. Oh putain ça brûle."

    iris fatigue "Voilà."

    elias ecoute "Encore deux séries. Après tu t’arrêtes."

    tuto "Durant vos temps libres, il sera possible de faire certaines actions qui augmenteront vos statistiques personnelles."
    tuto "Faire du sport est l'une d'entre elles."
    tuto "En faisant du sport, vous lancerez un minijeu qui, s’il est réussi, aura une chance d'augmenter votre statistique Physique."
    tuto "Certaines actions ou certains choix seront bloqués ou débloqués selon ces statistiques secondaires."
    tuto "De plus, pratiquer ce genre d'activité permet parfois de charger des évènements, seuls ou avec d'autres personnages."

    noam reflexion "Un… Deux… Allez Noam !"

    $ mg_skip_scene_pick = True
    call minijeu_halteres from _call_minijeu_halteres

    think "Je repose et récupère l'usage de mes poumons."
    $ mg_skip_scene_pick = False

    pause 0.6

    elias joie "Tu sens tes muscles ? C'est ça qu'on aime. La sensation de toujours faire mieux ! Mais le sport, ça se perd vite, alors refais-en souvent !"
    elias raison "Tu viens souvent. Force, endurance, concentration. Le corps comprend le concret."

    iris determine "Et parfois, c'est juste pour ne pas rentrer et tout casser."
    iris taquin "La fonte, ça coûte moins cher qu'un psy et pose moins de questions idiotes."

    pause 0.4

    noam reflexion "Donc… Si je ne fais rien…"

    elias neutre "Tu stagnes. Et plus tard, ton corps te le fait payer."

    think "Mes mains tremblent encore."

    noam neutre "Je reviendrai."

    iris sourire "Bonne idée."

    elias ecoute "Je serai là."
    elias raison "Mais la prochaine fois, on commence sans que tu trembles avant même de toucher la barre, hein ?" 

    $ hideGroup()

    think "Je quitte la salle. Les machines continuent, régulières et implacables."

    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    think "L'heure tourne. Mon estomac me ramène à la cafétéria."

    jump _2_CAFETERIA_SOIR

# Durée : 1m50
# Totale : 1h 22m 15s

label _2_CAFETERIA_SOIR:
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ current_period = "Soir"

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

    kael neutre "La routine me manque. Pas l'endroit."
    kael neutre "Disons que c'est plus mes proches qui me manquent."

    $ showGroup([
        ("noam", "hesitation", 0.13),
        ("kael", "neutre", 0.84),
        ("elen", "taquin", 0.72),
        ("nyra", "sourire", 0.96),
    ])

    elen taquin "Orbite, c'était comment ? On entend vraiiiment n'importe quoi dessus !"
    elen content "Vous dormez en flottant ? Et les repas, ils se baladent ? Imagine une soupe en apesanteur !"

    kael neutre "On flotte dans certaines sections. La vaisselle reste attachée."


    $ showGroup([
        ("noam", "inquiet", 0.13),
        ("kael", "neutre", 0.84),
        ("tomas", "neutre", 0.60),
        ("elen", "content", 0.72),
        ("nyra", "taquin", 0.96),
    ])

    tomas hesitation "Et… euh… vous aviez aussi des médiateurs, chez vous ?"
    tomas inquiet "Des… assemblées, ou un truc comme ça ? C-Comment vous faisiez pour prendre les décisions ?"

    kael calme "Il n'y a pas vraiment de décisions à prendre. On a des protocoles, on les respecte. Sinon on meurt."

    tomas inquiet "Et si on fait une erreur ...?"

    kael triste "Une erreur sur Orbite tue. Alors on évite d'en faire au maximum."

    elen triste "Je me demande si nos familles nous regardent en ce—"
    elen surpris "Oh ! Vous avez goûté la purée ? Elle a un goût différent ce soir, non ? Plus salé, ou moins jaune, ou—"

    kael reflechit "On ne vote pas uniquement pour eux. Mais quand même..."

    elen triste "Je déteste ça."
    elen surpris "Enfin, c'est peut-être la purée. Vous trouvez pas qu'elle est bizarre ?"

    think "D'autres se joignent à nous. Questions, souvenirs, comparaisons puis la fatigue finit par dissoudre le débat."

    stop music fadeout 1.0
    pause 0.6
    hide screen day2_quick_vote_notes

    scene couloir_cafeteria at adaptive_fullscreen with fade
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
    think "Je me sèche et tombe sur le lit."
    
    scene bg_cg012 at adaptive_fullscreen with fade
    think "Demain sera dense. À quatorze heures, on saura si changer les choses est réellement possible."

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
        # Persistance globale (conservée entre parties/sauvegardes).
        if persistent.unlocked_arguments is None:
            persistent.unlocked_arguments = []
        if title not in persistent.unlocked_arguments:
            persistent.unlocked_arguments.append(title)
        if arg_id not in store.j2_vote_arguments:
            store.j2_vote_arguments.append(arg_id)
        if "unlock_dossier_arg" in globals():
            unlock_dossier_arg(arg_id)
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

# Durée de la 2e journée de jeu : 15m30