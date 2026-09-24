label _9_1_0_0_REVEIL:

    $ current_day = 9
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"

    scene black with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    pause 1.0

    play sound sfx_announce

    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Booonjour, mes chers représentants ! J'espère que vous avez bien dormi, parce que certains d'entre vous semblent avoir eu une nuit particulièrement... active."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Des portes qui s'ouvrent, qui se ferment, des petits déplacements dans les couloirs... Vous savez, à force, je vais finir par croire que vous avez une vie sans moi."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Et ça, ce serait profondément blessant."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Mais je vous pardonne ! Je suis une déesse généreuse."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Profitez bien de votre matinée. Je vous retrouverai cet après-midi pour notre vote sur les regroupements de plus de vingt personnes."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "D'ici là, essayez de ne pas créer un incident diplomatique, une tentative de meurtre ou une nouvelle catastrophe sociale. J'aimerais beaucoup avoir quelques heures de tranquillité."

    hide screen kami_broadcast_ui

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    $ blink()

    "J'ouvre les yeux en grimaçant, mais les derniers mots de Kami achèvent de me réveiller bien plus efficacement que son annonce."

    noam reflexion "..."

    think "Des déplacements dans les couloirs."

    "Je reste quelques secondes immobile, les yeux fixés vers le plafond, avant que l'image de Ryn sortant de la chambre d'Iris me revienne avec une netteté désagréable."

    think "Non. Elle parle probablement de tout le monde. Les gens circulent constamment ici."

    think "Si Kami savait réellement pour Anya, elle ne se contenterait sûrement pas d'une remarque à moitié amusée au réveil."

    "Le raisonnement devrait me rassurer. Il ne fonctionne qu'à moitié."

    "Je me redresse, attrape mes vêtements et m'habille beaucoup plus vite que d'habitude."

    think "Je voulais en parler à Nyra. Autant le faire maintenant, avant de passer toute la journée à imaginer ce que Ryn a pu voir ou raconter."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Le couloir commence à peine à s'animer lorsque j'arrive devant la chambre de Nyra. Je frappe deux fois, suffisamment fort pour qu'elle m'entende sans réveiller tout le dortoir."

    play sound sfx_knock

    pause 0.8

    noam reflexion "Nyra ?"

    "Aucune réponse. Je recommence, cette fois un peu plus franchement."

    play sound sfx_knock

    noam "C'est Noam. J'ai besoin de te parler deux minutes."

    pause 1.0

    "Toujours rien."

    think "Elle est déjà partie."

    "Je m'apprête à faire demi-tour lorsque la porte située quelques mètres plus loin s'ouvre. Iris en sort en tirant maladroitement sur une manche de sa veste."

    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("iris", "fatigue", 0.72),
    ])

    "Elle a les cheveux moins soigneusement arrangés que d'habitude et surtout cette expression de quelqu'un qui a passé une bonne partie de la nuit à négocier avec son propre sommeil."

    noam surpris "T'as une sale tête."

    iris fatigue "Merci. C'est exactement ce que j'avais envie d'entendre pour commencer ma journée."

    noam gene "Je voulais dire que t'avais l'air fatiguée."

    iris desaccord "C'est fou, ça améliore complètement la phrase."

    "Elle referme sa porte derrière elle avec précaution avant de vérifier machinalement que le couloir est vide."

    noam reflexion "Anya ?"

    iris fatigue "Elle dort. Enfin."

    iris desaccord "Elle a réussi à s'endormir vers je sais pas quelle heure, puis elle s'est réveillée parce qu'elle avait soif, puis parce qu'elle avait froid, puis parce qu'elle avait trop chaud..."

    iris colere "Et cette fille bouge TOUT LE TEMPS."

    noam sourire "Tu découvres les joies de la colocation."

    iris desaccord "Je découvre surtout les joies de me faire expulser de mon propre lit centimètre par centimètre."

    "Je souris malgré moi, mais la raison pour laquelle je suis sorti de ma chambre me revient rapidement."

    noam reflexion "Iris, pour hier soir..."

    "Son expression change légèrement."

    iris reflexion "Quoi, hier soir ?"

    noam "Ryn."

    iris surpris "Ryn ?"

    noam "Je l'ai vu sortir de ta chambre."

    "Iris reste silencieuse une seconde, comme si elle remettait elle-même les événements dans l'ordre."

    iris reflexion "..."

    noam inquiet "Tu savais qu'il était venu ?"

    iris fatigue "Noam, j'ai dormi trois heures et je dois trouver comment faire prendre une douche, manger et respirer à une fille qui n'est officiellement pas ici."

    iris desaccord "Donc là, soit tu me laisses boire quelque chose avant de commencer ton interrogatoire, soit je vais devenir désagréable."

    noam taquin "Devenir ?"

    iris colere "Tu veux vraiment jouer à ça maintenant ?"

    noam sourire "Non."

    "Elle me lance un dernier regard avant de commencer à s'éloigner."

    iris reflexion "Trouve Nyra. Si Ryn a vraiment vu Anya, c'est probablement mieux qu'on réfléchisse tous avant de lui tomber dessus."

    noam "C'était justement le plan. Elle est pas dans sa chambre."

    iris fatigue "Alors cherche à la cafétéria. Moi, c'est exactement là que je vais."

    "Elle reprend sa marche et je reste quelques secondes devant la porte de Nyra."

    think "Au moins, Iris n'avait pas l'air de savoir pourquoi Ryn était venu."

    think "Je ne sais pas si c'est rassurant."

    $ hideGroup()

    jump _9_1_0_0_CAFETERIA


label _9_1_0_0_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "La cafétéria est déjà bien remplie lorsque j'entre. Plusieurs conversations se superposent autour des tables, assez pour que personne ne remarque réellement ceux qui arrivent ou repartent."

    "Je parcours rapidement la salle du regard."

    think "Pas de Nyra."

    "Je regarde une seconde fois, jusqu'aux tables du fond, au cas où je l'aurais simplement manquée. Rien."

    noam reflexion "Évidemment."

    "En revanche, je repère quelqu'un d'autre presque immédiatement."

    $ showGroup([
        ("ryn", "neutre", 0.65),
        ("noam", "reflexion", 0.30),
    ])

    "Ryn vient de terminer son repas. Il repousse sa chaise et récupère sa veste au moment où nos regards se croisent."

    ryn neutre "Noam."

    noam "Salut."

    "Il répond d'un signe de tête et commence déjà à contourner la table."

    noam reflexion "Attends deux secondes."

    "Ryn ralentit, sans réellement s'arrêter."

    ryn fatigue "Quoi ?"

    noam "Je voulais te demander quelque chose."

    ryn "Alors demande."

    "Son ton est parfaitement normal, ce qui rend presque plus étrange la façon dont il garde son corps tourné vers la sortie."

    noam reflexion "Tu as bien dormi ?"

    ryn fatigue "À peu près."

    noam "T'étais encore debout tard hier ?"

    "Cette fois, il me regarde vraiment."

    ryn reflexion "Pourquoi cette question ?"

    noam "Je t'ai croisé dans le couloir."

    ryn neutre "Ça arrive souvent dans un couloir."

    noam desaccord "Je t'ai surtout vu sortir de la chambre d'Iris."

    pause 0.5

    "Pendant une fraction de seconde, son expression se fige. Rien de spectaculaire, seulement un silence un peu trop net après une conversation qui jusque-là n'en avait aucun."

    ryn reflexion "..."

    noam "Qu'est-ce que tu faisais là-bas ?"

    ryn fatigue "J'avais besoin de lui parler."

    noam reflexion "De quoi ?"

    ryn fatigue "D'un sujet personnel."

    noam "À cette heure-là ?"

    "Ryn soupire et jette un regard vers l'entrée de la cafétéria."

    ryn fatigue "Noam, je n'ai pas particulièrement envie de commencer ma matinée en justifiant l'heure à laquelle je parle aux autres représentants."

    noam desaccord "Je te demande juste—"

    ryn "Et je viens de te répondre."

    "Il ne hausse pas la voix et ne se montre même pas agressif. Pourtant, quelque chose dans sa manière d'écourter chaque phrase est suffisamment inhabituel pour que je n'aie aucun doute."

    think "Il évite la conversation."

    noam reflexion "Ryn..."

    ryn fatigue "J'ai quelque chose à faire. On reparlera plus tard."

    "Il commence à partir avant même que j'aie le temps de répondre."

    noam "Plus tard quand ?"

    "Ryn lève simplement une main sans se retourner."

    ryn "Plus tard."

    $ hideGroup()

    "Je le regarde quitter la cafétéria. La scène entière n'a probablement duré qu'une minute, mais elle suffit largement à rendre mes soupçons plus encombrants qu'ils ne l'étaient au réveil."

    think "Il sait que je l'ai vu. Et il ne veut clairement pas me dire pourquoi il était là."

    "Je cherche encore Nyra du regard, sans davantage de succès, lorsqu'une voix s'élève près du comptoir."

    julian "Tomas, tu prépares tes réserves pour l'hiver ou quoi ?"

    "Je tourne la tête."

    $ showGroup([
        ("julian", "taquin", 0.20),
        ("tomas", "inquiet", 0.50),
        ("noam", "reflexion", 0.80),
    ])

    "Tomas tient un plateau sur lequel il a empilé suffisamment de nourriture pour provoquer exactement le genre de remarque que Julian vient de faire."

    tomas inquiet "J'ai faim."

    julian taquin "Ça, c'est pas avoir faim. Ça, c'est préparer une expédition de six semaines."

    tomas "J'ai très faim."

    julian sourire "Ah, pardon. Dans ce cas, tout s'explique."

    "Tomas essaie de rester naturel, mais son regard me cherche immédiatement lorsque j'approche."

    noam taquin "Tu t'es découvert un deuxième estomac pendant la nuit ?"

    tomas inquiet "Peut-être."

    julian "Vous êtes tous étranges ce matin."

    noam sourire "Et toi tu surveilles les plateaux des autres."

    julian taquin "Je suis un homme curieux."

    "Julian récupère son verre et s'éloigne vers une autre table, visiblement satisfait de sa contribution essentielle à la conversation."

    $ showGroup([
        ("tomas", "inquiet", 0.35),
        ("noam", "reflexion", 0.70),
    ])

    "Tomas attend qu'il soit suffisamment loin avant de baisser légèrement la voix."

    tomas inquiet "{i}E-Elle s'est bien réveillée ?{/i}"

    noam "{i}Oui. Très bien, même. Iris peut confirmer.{/i}"

    tomas reflexion "{i}Elle va mieux ?{/i}"

    noam "{i}Elle parle, elle mange et elle se dispute déjà avec Iris. Donc je pense qu'on peut considérer qu'elle va mieux.{/i}"

    "Un petit sourire soulagé apparaît sur son visage."

    tomas "{i}Tant mieux.{/i}"

    "Il regarde son plateau."

    tomas inquiet "{i}J'ai pris plusieurs trucs différents. Je savais pas ce qu'elle aimait.{/i}"

    noam sourire "{i}C'est gentil.{/i}"

    tomas reflexion "{i}C'est surtout compliqué.{/i}"

    noam "{i}Quoi ?{/i}"

    "Il rapproche légèrement le plateau contre lui."

    tomas inquiet "{i}La nourriture, ça va encore. Je peux prendre une portion en plus sans que quelqu'un appelle Kami.{/i}"

    tomas "{i}Mais elle va devoir sortir de la chambre à un moment. Se laver, bouger, récupérer des vêtements...{/i}"

    noam reflexion "{i}Je sais.{/i}"

    tomas "{i}Et Iris peut pas rester enfermée avec elle toute la journée.{/i}"

    noam "{i}Je sais aussi.{/i}"

    tomas inquiet "{i}Donc on fait quoi ?{/i}"

    "Je voudrais lui répondre immédiatement. Rien ne me vient."

    noam reflexion "{i}Pour l'instant, on évite déjà qu'elle soit découverte.{/i}"

    tomas "{i}C'est pas vraiment un plan.{/i}"

    noam gene "{i}Non.{/i}"

    tomas inquiet "{i}D'accord.{/i}"

    "Il hoche la tête avec cette manière très Tomas d'accepter une réponse qui ne le rassure absolument pas."

    noam reflexion "{i}Au fait, t'as vu Nyra ce matin ?{/i}"

    tomas "{i}Non. Pourquoi ?{/i}"

    noam "{i}J'ai besoin de lui parler.{/i}"

    tomas inquiet "{i}C'est grave ?{/i}"

    "Je regarde machinalement vers la porte par laquelle Ryn vient de disparaître."

    noam reflexion "{i}Je sais pas encore.{/i}"

    "Tomas suit brièvement mon regard mais ne pose aucune autre question."

    tomas "{i}Je vais apporter ça avant que quelqu'un décide de compter les portions.{/i}"

    noam sourire "{i}Bonne idée.{/i}"

    tomas "{i}À plus tard.{/i}"

    noam "{i}À plus.{/i}"

    $ hideGroup()

    "Il quitte la cafétéria avec son plateau et je reste quelques minutes de plus, juste assez longtemps pour comprendre que Nyra ne viendra probablement pas."

    think "Je la trouverai au Conclave cet après-midi. D'ici là, impossible de faire beaucoup plus."

    "Je récupère quelque chose à manger et m'installe à mon tour, mais une bonne partie du repas passe sans que je puisse réellement décrocher de la même question."

    think "Qu'est-ce que Ryn cherchait dans cette chambre ?"

    jump _9_1_0_0_CONCLAVE


label _9_1_0_0_CONCLAVE:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_3
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Lorsque nous nous retrouvons dans la salle du Conclave quelques heures plus tard, l'ambiance n'a presque rien à voir avec celle des votes précédents."

    "Personne ne semble particulièrement tendu et, pour une fois, les conversations ne s'arrêtent même pas lorsque les derniers représentants prennent place."

    $ showGroup([
        ("elen", "joie", 0.10),
        ("julian", "taquin", 0.27),
        ("mara", "neutre", 0.43),
        ("noam", "neutre", 0.57),
        ("tomas", "neutre", 0.73),
        ("iris", "fatigue", 0.90),
    ])

    elen joie "Moi je vous le dis, si ça passe, la première chose qu'on doit remettre en place c'est les festivals."

    mara reflexion "Le vote n'oblige aucun district à organiser un festival."

    elen "Je sais ! Mais ils pourront ! C'est déjà énorme !"

    julian taquin "Tu prépares déjà ton programme ?"

    elen joie "Évidemment ! Concerts, stands, bouffe, des vraies scènes avec des lumières partout..."

    iris fatigue "Tu vas réussir à être épuisante avant même que le vote commence."

    elen sourire "Mais imagine ! Ça fait plus d'un an qu'on a rien eu de tout ça."

    "Son enthousiasme retombe légèrement sur les derniers mots, sans complètement disparaître."

    elen reflexion "Le dernier vrai concert auquel je suis allée, c'était quelques semaines avant la prise de pouvoir de Kami."

    julian "Tu te souviens encore du groupe ?"

    elen joie "Bien sûr que je m'en souviens ! J'avais attendu trois heures dehors parce que j'avais pris les places les moins chères et je voulais être devant."

    mara taquin "Ça ne me surprend absolument pas."

    elen sourire "J'avais plus de voix pendant deux jours après."

    iris desaccord "Ça devait être reposant pour ton entourage."

    elen colere "Hé !"

    "Même Mara laisse échapper un petit rire."

    tomas reflexion "Les festivals, les concerts, les manifestations sportives... Il y a pas mal de choses qui étaient devenues pratiquement impossibles avec la limite actuelle."

    mara "Oui. Et c'est justement pour ça que je vois mal quelqu'un voter contre."

    noam reflexion "Moi non plus."

    "Je regarde instinctivement autour de la salle. Habituellement, c'est à ce moment-là qu'apparaît le détail oublié, la conséquence impossible ou la personne qui annonce qu'elle refusera quoi qu'il arrive."

    "Rien ne vient."

    think "C'est presque suspect tellement c'est simple."

    julian taquin "Noam fait encore sa tête de mec qui cherche où est le piège."

    noam surpris "Quoi ?"

    julian "Cette tête-là. Celle où t'as l'air de relire mentalement tout le règlement."

    noam desaccord "Je cherche pas de piège."

    iris taquin "Tu cherches complètement un piège."

    noam reflexion "Disons que les derniers votes m'ont appris à être prudent."

    mara "Pour une fois, je pense qu'il n'y en a pas."

    iris reflexion "Ne dis pas ça trop fort."

    julian sourire "C'est exactement ce que tu m'as dit hier."

    mara desaccord "Et je maintiens."

    $ hideGroup()

    play sound sfx_announce
    stop music fadeout 0.8

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Puisque vous avez visiblement commencé le débat sans moi, je vais éviter de vous interrompre trop longtemps."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Le texte soumis aujourd'hui est simple : autoriser les regroupements de plus de vingt personnes, idéalement après déclaration préalable auprès des autorités locales."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "À l'heure actuelle, le Commandement IV interdit les rassemblements dépassant cette limite lorsqu'ils ne sont pas autorisés."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "En d'autres termes, si vous votez pour, vos chers citoyens pourront de nouveau se réunir à vingt-et-un sans risquer de provoquer une crise existentielle de l'administration."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Quelle avancée historique."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    $ showGroup([
        ("elen", "joie", 0.08),
        ("mara", "neutre", 0.25),
        ("julian", "neutre", 0.42),
        ("noam", "reflexion", 0.58),
        ("tomas", "neutre", 0.75),
        ("ryn", "neutre", 0.92),
    ])

    mara reflexion "Je pense qu'on peut être assez rapides. Les autorités locales gardent toujours la possibilité d'interdire un événement pour une raison précise."

    tomas "Donc ça ne supprime pas les règles de sécurité."

    mara "Exactement. Ça supprime simplement l'interdiction générale."

    julian taquin "Attendez, vous voulez dire qu'on peut autoriser les gens à vivre sans immédiatement provoquer l'effondrement de la civilisation ?"

    mara desaccord "C'est une théorie audacieuse."

    elen joie "Moi je suis pour !"

    julian sourire "Personne n'avait deviné."

    elen "Mais vraiment, vous vous rendez pas compte de tout ce que ça change."

    noam sourire "Je crois qu'on commence à s'en rendre compte."

    elen joie "Les concerts, c'est pas juste aller écouter quelqu'un chanter ! Les gens se retrouvent, ils voyagent, ils mangent ensemble, ils rencontrent des gens..."

    elen reflexion "Même les petites fêtes de quartier ont disparu. Tout ce qui demandait de réunir un peu de monde est devenu tellement compliqué que les gens ont juste arrêté d'essayer."

    tomas reflexion "Vu comme ça, oui."

    elen "Et j'en ai marre que tout soit triste !"

    "Elle le dit avec tellement de spontanéité que personne ne trouve immédiatement quoi répondre."

    elen triste "On parle tout le temps de frontières, de règles, de nourriture, de sécurité... On devrait pouvoir avoir des trucs juste parce que c'est sympa aussi, non ?"

    noam sourire "Je pense que oui."

    "Sa remarque est simple, presque naïve, mais c'est probablement l'argument qui me parle le plus depuis le début de la discussion."

    noam reflexion "Je voterai pour. La limite actuelle empêche trop de choses sans apporter grand-chose en échange."

    ryn neutre "Même chose."

    tomas "Pour aussi."

    mara "Je suis favorable au texte."

    julian sourire "Je refuse catégoriquement."

    "Elen se tourne vers lui avec des yeux immenses."

    elen surpris "QUOI ?!"

    julian rire "Je plaisante."

    elen colere "Mais t'es con !"

    julian sourire "Je voulais juste vérifier que tu étais encore avec nous."

    elen "J'ai failli faire une attaque !"

    "Quelques rires parcourent la salle."

    think "C'est donc vraiment ça."

    think "Un débat normal."

    "Je m'attends presque à voir Kami intervenir pour nous annoncer que nous avons oublié quelque chose."

    $ hideGroup()

    play sound sfx_announce
    stop music fadeout 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "C'est tout ?"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Personne ne veut expliquer que les festivals sont une menace contre l'ordre public ? Personne ne souhaite dénoncer le risque de révolte, de débauche ou d'effondrement moral ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Même pas une petite dispute ?"

    pause 0.5

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Vous me décevez."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Très bien. Puisque vous insistez pour vous comporter comme des adultes raisonnables, procédons au vote."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Aucun débat supplémentaire n'est nécessaire. Les choix s'enchaînent sans hésitation particulière et lorsque mon tour arrive, j'appuie directement sur « Pour »."

    think "Pour une fois, je sais exactement ce que je veux voter."

    "Les derniers représentants se prononcent à leur tour. Aucun vote ne vient remettre le résultat en cause."

    pause 0.8

    "L'amendement est adopté."

    $ showGroup([
        ("elen", "joie", 0.20),
        ("julian", "sourire", 0.40),
        ("mara", "neutre", 0.60),
        ("noam", "sourire", 0.80),
    ])

    elen joie "OUI !"

    julian sourire "Voilà. On vient officiellement de rendre Elen dangereusement puissante."

    elen joie "Je veux un festival."

    mara "Tu n'es pas organisatrice d'événements."

    elen "Je peux apprendre."

    julian taquin "Ça fait peur."

    noam sourire "Laisse-la profiter trente secondes."

    mara taquin "Je lui en donne vingt."

    elen colere "Vous êtes horribles."

    "Pour la première fois depuis longtemps, le résultat d'un vote provoque quelque chose qui ressemble davantage à du soulagement qu'à de l'épuisement."

    $ hideGroup()

    "Je commence à me lever, persuadé que la séance est terminée, mais les écrans autour de nous restent allumés."

    play sound sfx_announce

    stop music fadeout 0.8
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Pas si vite."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Puisque vous êtes tous réunis et merveilleusement attentifs, j'ai encore une petite annonce à faire."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Et celle-ci sera également diffusée auprès de l'ensemble des districts."

    "Le ton de Kami change légèrement. Moins théâtral, plus proche de celui qu'elle utilise lorsqu'elle s'adresse officiellement au reste du monde."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Depuis le rétablissement progressif du commerce interdistrict, le volume de marchandises circulant entre les territoires augmente chaque jour."

    kami "Cette reprise est une excellente nouvelle, mais elle entraîne également une charge de contrôle bien supérieure pour les services actuellement responsables des zones logistiques."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "De nouvelles missions rémunérées seront donc créées dans chaque district afin d'aider à la vérification des cargaisons."

    kami "Les citoyens volontaires pourront participer au contrôle des conteneurs, à l'inspection des scellés, à la surveillance des zones de chargement et au signalement de toute anomalie."

    "Mon sourire disparaît progressivement."

    think "La vérification des conteneurs."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Vous vouliez davantage d'activité économique ? La voici ! Du travail, des récompenses et une meilleure sécurité commerciale."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Tout le monde est gagnant. Sauf, évidemment, les personnes qui auraient quelque chose à cacher dans une caisse."

    "Un petit rire accompagne sa dernière phrase."

    "Personne autour de moi ne réagit particulièrement."

    think "Elle ne sait pas."

    think "C'est une blague évidente. C'est exactement le genre de phrase qu'elle aurait prononcée dans n'importe quelle situation."

    "Je dois pourtant me forcer à ne pas regarder vers Iris."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.5

    $ showGroup([
        ("mara", "reflexion", 0.10),
        ("tomas", "reflexion", 0.27),
        ("elen", "neutre", 0.43),
        ("noam", "inquiet", 0.57),
        ("ryn", "neutre", 0.73),
        ("nyra", "neutre", 0.90),
    ])

    mara reflexion "En soi, c'est plutôt logique. Les volumes doivent avoir explosé depuis la réouverture."

    tomas reflexion "Et si les missions sont rémunérées, ça donnera aussi un revenu supplémentaire à pas mal de monde."

    elen "Ça me choque pas."

    mara "Moi non plus."

    "Leurs réactions sont parfaitement raisonnables. Si je ne savais pas qu'Anya avait traversé une frontière enfermée dans l'un de ces conteneurs, j'aurais probablement dit exactement la même chose."

    think "Sauf que maintenant, chaque contrôle supplémentaire signifie une chance de moins pour quelqu'un comme elle de passer."

    "Je tourne légèrement la tête."

    "Ryn était jusque-là appuyé contre son siège, presque détaché de la conversation. Depuis l'annonce de Kami, sa posture a changé."

    "Il ne parle pas. Il ne regarde personne. Il fixe simplement l'écran éteint devant nous avec beaucoup plus d'attention qu'il n'en accordait au débat."

    noam reflexion "..."

    "Ses doigts, qui jouaient distraitement contre l'accoudoir quelques secondes plus tôt, se sont arrêtés."

    think "Pourquoi ça t'intéresse autant ?"

    "Ryn finit par remarquer mon regard."

    ryn reflexion "Quoi ?"

    noam "Rien."

    "Je détourne les yeux avant qu'il ait le temps d'ajouter quoi que ce soit."

    think "D'abord Nyra."

    think "Ensuite seulement, Ryn."

    $ hideGroup()

    jump _9_1_0_0_APRES_DEBAT


label _9_1_0_0_APRES_DEBAT:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_4
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    "La séance terminée, tout le monde commence à se disperser. Je repère Nyra avant même qu'elle atteigne le bout du couloir et accélère immédiatement le pas."

    $ showGroup([
        ("noam", "inquiet", 0.30),
        ("nyra", "neutre", 0.70),
    ])

    noam "Nyra."

    nyra reflexion "Noam ?"

    noam "Attends."

    "Elle s'arrête et m'observe quelques secondes."

    nyra reflexion "Tu me cherches depuis ce matin, non ?"

    noam surpris "Comment tu sais ça ?"

    nyra "Iris me l'a dit avant le débat."

    noam desaccord "Elle aurait aussi pu me dire qu'elle t'avait trouvée."

    nyra taquin "Elle avait l'air de très mauvaise humeur."

    noam "Elle a passé la nuit avec Anya."

    nyra "Ça explique probablement une partie du problème."

    "Je vérifie que les autres représentants se sont suffisamment éloignés avant de reprendre plus bas."

    noam reflexion "Hier soir, j'ai vu Ryn sortir de la chambre d'Iris."

    "Le sourire discret de Nyra disparaît."

    nyra reflexion "Tu l'as vu entrer ?"

    noam "Non. Seulement sortir."

    nyra "Et Iris était dans la chambre ?"

    noam "Je sais pas. Je lui ai demandé ce matin, elle avait pas l'air de savoir pourquoi il était venu."

    nyra reflexion "D'accord."

    noam inquiet "Et Ryn m'a évité à la cafétéria. Dès que j'ai parlé de la chambre d'Iris, il a trouvé une excuse pour partir."

    "Nyra ne répond pas immédiatement. Elle continue de regarder le couloir plutôt que moi."

    noam "Tu crois qu'il l'a vue ?"

    nyra reflexion "Probablement."

    noam inquiet "Alors il faut faire quelque chose."

    nyra "Pourquoi ?"

    noam surpris "Comment ça, pourquoi ? Il est pas censé savoir qu'elle est là."

    nyra raison "Justement. S'il l'a découverte hier soir et qu'il voulait prévenir Kami, pourquoi attendre jusqu'à maintenant ?"

    noam reflexion "Peut-être qu'il réfléchit."

    nyra "Possible."

    noam "Ou qu'il attend quelque chose."

    nyra "Possible aussi."

    "Elle se tourne enfin vers moi."

    nyra raison "Mais ce sont deux hypothèses parmi beaucoup d'autres. Pour l'instant, tout ce que nous savons, c'est que Ryn est entré dans cette chambre et qu'il ne veut pas t'expliquer pourquoi."

    noam desaccord "C'est déjà pas mal."

    nyra "C'est suffisant pour vérifier. Pas pour décider qu'il nous a trahis."

    "Je soupire, légèrement frustré par son calme."

    noam reflexion "Tu proposes quoi ?"

    nyra "On demande à la seule personne qui était forcément là."

    noam "Anya."

    nyra "Anya."

    "Elle prend immédiatement la direction de la chambre d'Iris."

    noam surpris "Maintenant ?"

    nyra taquin "Tu me cherchais depuis ce matin et maintenant que je suis disponible, tu veux attendre ?"

    noam gene "Vu comme ça..."

    nyra "Viens."

    $ hideGroup()

    jump _9_1_0_0_ANYA


label _9_1_0_0_ANYA:

    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Nous attendons que le couloir soit vide avant de rejoindre la chambre d'Iris. Nyra frappe d'une manière suffisamment particulière pour qu'Anya sache probablement que ce n'est pas une visite normale."

    play sound sfx_knock

    pause 0.8

    "Quelques secondes passent avant que la porte s'entrouvre."

    anya "{i}Qui c'est ?{/i}"

    noam "{i}Nous.{/i}"

    anya desaccord "{i}C'est extrêmement rassurant comme réponse.{/i}"

    nyra "{i}Nyra et Noam.{/i}"

    "La porte s'ouvre un peu plus."

    anya reflexion "{i}Iris est pas là.{/i}"

    noam "{i}On vient pas voir Iris.{/i}"

    "Anya nous regarde tour à tour avant de comprendre que quelque chose ne va pas."

    anya inquiet "{i}Quoi ?{/i}"

    nyra "{i}On peut entrer ?{/i}"

    anya reflexion "{i}J'imagine que oui. C'est pas vraiment chez moi.{/i}"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre_iris", "bg_chambre_iris") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_5
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Nous refermons immédiatement derrière nous. Anya reste dans la partie de la chambre masquée à la caméra, exactement comme Iris a dû le lui répéter toute la journée."

    anya reflexion "{i}Vous avez tous cette tête quand vous venez ici ou c'est juste aujourd'hui ?{/i}"

    noam "{i}Il faut qu'on parle.{/i}"

    anya fatigue "{i}Oui, j'avais compris cette partie.{/i}"

    "Nyra indique simplement la salle de bain."

    anya desaccord "{i}Encore ?{/i}"

    nyra raison "{i}Encore.{/i}"

    anya fatigue "{i}Je vais finir par connaître cette pièce mieux que le reste de la station.{/i}"

    scene bg_salle_de_bain_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    $ showGroup([
        ("noam", "reflexion", 0.18),
        ("anya", "reflexion", 0.52),
        ("nyra", "raison", 0.84),
    ])

    "Une fois la porte fermée, Nyra attend quelques secondes avant d'aller droit au sujet."

    nyra raison "Ryn est venu ici hier soir."

    "Anya cligne des yeux, puis acquiesce avec une simplicité qui suffit déjà à me faire comprendre que mes soupçons étaient fondés."

    anya "Oui."

    noam surpris "Tu l'as vu ?"

    anya "Oui."

    noam "Et tu comptais nous le dire quand ?"

    anya desaccord "Je savais pas que j'étais censée faire un rapport détaillé de chaque personne qui passe la porte."

    noam inquiet "Anya, il ne savait pas que tu existais."

    "Elle fronce légèrement les sourcils."

    anya reflexion "Ah."

    pause 0.5

    anya "Ça, par contre, je savais pas."

    "Nyra intervient avant que je poursuive."

    nyra raison "Raconte-nous simplement ce qui s'est passé. Depuis le moment où il est entré."

    "Anya s'adosse contre le mur et réfléchit quelques secondes."

    anya reflexion "Iris était sortie. Je crois qu'elle était partie prendre quelque chose à manger ou récupérer des affaires."

    anya "J'étais sur le lit et j'ai entendu la porte."

    noam inquiet "Tu t'es pas cachée ?"

    anya desaccord "J'ai essayé ! Mais votre merveilleux système de camouflage repose sur un drap, un morceau de tissu devant une caméra et l'espoir que personne n'entre sans prévenir."

    noam gene "C'est pas faux."

    anya reflexion "Quand j'ai compris que c'était pas Iris, il était déjà dans la chambre."

    nyra "Et sa réaction ?"

    anya "C'est ça qui était bizarre."

    "Elle croise les bras."

    anya reflexion "Il m'a regardée. Moi je me suis figée parce que je pensais que j'étais morte, ou au minimum que j'allais devoir expliquer pourquoi une inconnue dormait dans le lit d'une représentante."

    anya "Mais lui..."

    "Elle cherche ses mots."

    anya reflexion "Il avait pas vraiment l'air surpris."

    noam inquiet "Pas vraiment ou pas du tout ?"

    anya "Pas du tout."

    "Nyra et moi échangeons un regard."

    nyra raison "Il savait donc probablement que quelqu'un était ici."

    anya "C'est l'impression que j'ai eue."

    noam reflexion "Qu'est-ce qu'il a dit ?"

    anya "Il a fermé la porte derrière lui et il m'a demandé si j'étais arrivée avec la dernière livraison."

    noam surpris "Directement ?"

    anya "Oui."

    "Mon malaise augmente immédiatement."

    noam reflexion "Il n'a même pas demandé qui tu étais ?"

    anya "Pas au début."

    nyra "Est-ce qu'il a donné l'impression de reconnaître ton visage ?"

    anya "Non. Ça, je pense pas."

    nyra reflexion "Donc il ne te connaissait probablement pas personnellement."

    anya "J'imagine."

    noam "Et après ?"

    anya reflexion "Après, je lui ai demandé s'il allait appeler Kami."

    "Elle hausse les épaules."

    anya "Il m'a dit non."

    noam surpris "C'est tout ?"

    anya "À peu près."

    anya "J'ai insisté parce que, vous allez rire, découvrir un inconnu dans la chambre où on me cache depuis moins d'une journée m'a pas spécialement mise en confiance."

    noam desaccord "Étrange."

    anya taquin "Je sais."

    anya reflexion "Mais il a dit qu'il ne raconterait rien. À personne."

    nyra "Il t'a demandé quelque chose en échange ?"

    anya "Non."

    noam reflexion "Il t'a menacée ?"

    anya "Non plus."

    anya desaccord "Vous avez l'air de vouloir absolument qu'il se soit comporté comme un psychopathe."

    noam "On veut comprendre."

    anya "Alors pour l'instant, il a été beaucoup moins inquiétant que vous deux."

    noam surpris "Nous ?"

    anya "Je vous rappelle comment j'ai rencontré Iris hier matin ?"

    noam gene "D'accord, mauvais exemple."

    "Anya esquisse un petit sourire, mais Nyra reste concentrée sur son récit."

    nyra raison "Tu as dit qu'il t'avait posé des questions."

    anya reflexion "Oui."

    nyra "Lesquelles ?"

    anya "Au début, des trucs assez normaux. D'où je venais, depuis combien de temps j'étais coincée à Limen, pourquoi j'avais pris ce risque."

    noam "Et ensuite ?"

    "Son expression devient plus sérieuse."

    anya reflexion "Ensuite il a commencé à parler du réseau."

    nyra "Le réseau qui t'a fait entrer dans le conteneur ?"

    anya "Oui."

    anya "Il voulait savoir comment je l'avais trouvé, qui m'avait mise en contact, si j'avais vu les personnes qui organisaient les passages..."

    noam reflexion "Tu connaissais leurs noms ?"

    anya "Non. Je vous l'ai déjà dit, moins j'en savais, mieux c'était."

    anya "J'avais un contact qui me donnait les instructions et c'est tout. Même le type qui m'a amenée jusqu'au dépôt ne m'a jamais donné son vrai nom."

    nyra raison "Et Ryn s'est arrêté là ?"

    anya "Non."

    "Elle replace machinalement ses lunettes."

    anya reflexion "C'est là que c'est devenu plus précis."

    noam inquiet "Précis comment ?"

    anya "Il voulait savoir comment ils choisissaient les conteneurs."

    anya "S'ils savaient à l'avance lesquels seraient inspectés, s'il y avait des horaires où les dépôts étaient moins surveillés, comment les scellés étaient vérifiés..."

    "Nyra relève légèrement le menton."

    nyra reflexion "Les scellés ?"

    anya "Oui."

    anya "Il m'a même demandé si les équipes de contrôle vérifiaient seulement le numéro extérieur ou si elles ouvraient systématiquement les conteneurs."

    noam reflexion "Tu savais répondre à tout ça ?"

    anya desaccord "Évidemment que non."

    anya "Moi, on m'a dit : sois à telle porte à telle heure, monte dans ce conteneur et ne sors surtout pas avant l'arrivée."

    anya reflexion "J'étais pas en stage chez les passeurs."

    "Malgré la situation, je retiens difficilement un sourire."

    nyra raison "Il a utilisé des mots particuliers ? Des noms de zones, des procédures, quelque chose que toi tu n'avais pas mentionné avant ?"

    "Anya réfléchit plus longtemps cette fois."

    anya reflexion "Oui..."

    noam "Quoi ?"

    anya "À un moment, il m'a demandé si le conteneur avait été placé dans une file de contrôle normale ou dans une zone de transit secondaire."

    nyra reflexion "Tu lui avais parlé de zones de transit ?"

    anya "Non."

    "Le silence retombe."

    anya inquiet "Pourquoi ?"

    nyra "Parce que ce n'est pas le genre de détail qu'on demande au hasard."

    anya reflexion "J'avais surtout l'impression qu'il savait déjà comment ça fonctionnait."

    noam inquiet "Voilà."

    anya desaccord "Ça veut pas dire qu'il fait partie du réseau."

    noam "J'ai pas dit ça."

    anya "Tu le penses très fort."

    noam reflexion "Je pense surtout qu'il en sait beaucoup plus qu'il ne veut me le dire."

    anya "Peut-être. Mais il aurait pu me dénoncer dès qu'il m'a vue et il l'a pas fait."

    "Elle se tourne vers Nyra."

    anya reflexion "Et il avait pas l'air de vouloir me piéger. Il était calme."

    anya "Il m'a même demandé si Iris me donnait suffisamment à manger."

    noam surpris "Sérieusement ?"

    anya "Oui."

    anya taquin "Apparemment ma survie alimentaire inquiète énormément de monde ici."

    "Nyra garde le silence quelques secondes, puis pose enfin la question que je n'avais moi-même pas formulée clairement."

    nyra raison "Anya."

    anya "Hm ?"

    nyra "Comment savait-il que tu étais là ?"

    "Anya ouvre la bouche, puis s'arrête."

    pause 0.8

    anya reflexion "..."

    "Son assurance disparaît progressivement."

    anya "Je sais pas."

    nyra "Tu ne l'avais jamais vu avant hier ?"

    anya "Jamais."

    nyra "Tu n'as parlé à personne d'autre depuis ton réveil ?"

    anya "À vous. Iris. Tomas."

    noam "Et personne d'autre."

    anya "Non."

    nyra reflexion "Alors il y a deux possibilités."

    noam inquiet "Quelqu'un lui a parlé."

    nyra "Ou il savait déjà quelque chose avant d'entrer."

    anya inquiet "Mais comment ?"

    nyra "C'est précisément ce qu'on ignore."

    "Je repense à Ryn dans la cafétéria, puis à son regard pendant l'annonce de Kami sur les contrôles."

    think "Et il vient justement poser des questions sur les conteneurs la veille d'une annonce qui va rendre leurs contrôles beaucoup plus stricts."

    noam reflexion "Ce matin, quand je lui ai demandé pourquoi il était venu ici, il m'a dit qu'il avait quelque chose de personnel à dire à Iris."

    anya desaccord "Iris était même pas là quand il est venu."

    noam "Je sais."

    nyra raison "Ça confirme au moins une chose : il ne veut pas que Noam sache ce qu'il cherchait réellement."

    anya inquiet "Et maintenant ?"

    noam "Bonne question."

    "La porte de la chambre s'ouvre brusquement de l'autre côté de la salle de bain."

    iris "..."

    pause 0.5

    iris "Non."

    "Nous nous regardons tous les trois."

    noam surpris "..."

    anya fatigue "..."

    nyra reflexion "..."

    iris "Je refuse."

    "Quelques pas rapides traversent la chambre avant que la porte de la salle de bain s'ouvre."

    $ showGroup([
        ("noam", "gene", 0.10),
        ("nyra", "neutre", 0.33),
        ("anya", "fatigue", 0.57),
        ("iris", "colere", 0.85),
    ])

    iris colere "C'est quoi ÇA ?!"

    noam gene "Bonjour."

    iris "Non, pas bonjour."

    iris colere "Pourquoi il y a encore une réunion dans MA salle de bain ?!"

    nyra raison "On avait besoin de parler sans les micros."

    iris "Vous avez tous des brouilleurs dans vos chambres !"

    noam "Anya peut pas vraiment traverser le couloir pour aller dans la mienne."

    iris desaccord "Je sais très bien pourquoi vous êtes ici, c'est pas le problème !"

    "Elle pose ses affaires sur le meuble avec beaucoup plus de force que nécessaire."

    iris colere "Depuis hier, ma chambre est devenue une gare."

    iris "Tomas vient avec des plateaux de nourriture."

    iris "Noam passe le matin."

    iris "Nyra organise des réunions."

    iris "Ryn entre je sais même pas pourquoi."

    iris "Et maintenant je découvre TROIS personnes enfermées dans ma salle de bain !"

    anya taquin "En comptant toi, on est quatre."

    "Iris tourne lentement la tête vers elle."

    iris desaccord "Merci Anya."

    anya sourire "De rien."

    iris "C'était une information essentielle."

    anya "J'aime être utile."

    noam sourire "Elle s'intègre vite."

    iris colere "Toi, ne l'encourage pas."

    "Nyra semble lutter pour conserver son sérieux."

    nyra taquin "On avait presque terminé."

    iris desaccord "Magnifique. Est-ce que je peux réserver un créneau pour utiliser ma propre salle de bain ou je dois remplir un formulaire ?"

    noam taquin "On peut mettre un planning à l'entrée."

    iris colere "Noam."

    noam sourire "J'arrête."

    "Iris croise les bras puis désigne Anya."

    iris desaccord "Et puisqu'on parle d'organisation, ce soir tu choisis un côté du lit."

    anya surpris "Pardon ?"

    iris "Un côté. Gauche ou droite. Peu importe. Mais tu le gardes."

    anya desaccord "Je dors déjà d'un côté."

    iris colere "Tu dors en diagonale !"

    anya "Pas du tout !"

    iris "Cette nuit, ton pied était presque sur mon oreiller !"

    anya colere "Parce que TU m'avais poussée !"

    iris surpris "Moi ?!"

    anya "Oui, toi !"

    iris colere "C'est mon lit !"

    anya desaccord "Et ça te donne le droit de prendre toute la couverture ?"

    iris "Je prends pas toute la couverture."

    anya "Tu t'enroules dedans comme une espèce de burrito agressif !"

    pause 0.5

    noam "..."

    nyra "..."

    "Je baisse la tête pour cacher mon sourire."

    iris colere "Je ne m'enroule PAS comme un burrito !"

    anya "Je me suis réveillée trois fois sans rien sur moi."

    iris "Parce que tu bouges !"

    anya "Parce que j'ai froid !"

    iris "Parce que tu prends toute la place !"

    anya "Ton lit est énorme !"

    iris "C'est pas une raison !"

    noam sourire "Vous vous entendez plutôt bien finalement."

    iris colere "DEHORS."

    noam surpris "D'accord."

    "Nyra lève néanmoins une main avant que la discussion ne se termine complètement."

    nyra raison "Une chose avant."

    "Iris soupire mais se tait."

    nyra "À partir de maintenant, personne ne vient voir Anya seul."

    anya reflexion "Même vous ?"

    nyra "Même nous. Si quelqu'un doit entrer ici, au moins une autre personne parmi celles qui connaissent la situation doit être au courant."

    iris reflexion "Vu ce qui s'est passé hier soir, ça me paraît pas stupide."

    nyra "Et si une nouvelle personne découvre Anya, volontairement ou non, on se le dit immédiatement."

    noam "Pour Ryn, on fait quoi ?"

    "Nyra réfléchit une seconde."

    nyra raison "Rien, pour l'instant."

    noam surpris "Rien ?"

    nyra "Il a eu plusieurs heures pour prévenir Kami et il ne l'a pas fait. Lui tomber dessus sans savoir ce qu'il cherche ne ferait que lui montrer que nous paniquons."

    noam reflexion "Donc on lui fait confiance ?"

    nyra "Non."

    "Elle jette un bref regard vers Anya."

    nyra raison "On considère qu'il sait."

    pause 0.5

    nyra "Pas qu'il est avec nous."

    "Cette distinction suffit à faire disparaître les derniers sourires de la pièce."

    iris reflexion "Ça me va."

    anya "Moi aussi."

    noam reflexion "D'accord."

    iris desaccord "Parfait. Maintenant, puisque cette réunion clandestine est officiellement terminée..."

    "Elle ouvre grand la porte de la salle de bain."

    iris colere "DEHORS."

    nyra taquin "Je crois que c'était destiné à nous."

    noam sourire "J'avais compris."

    anya taquin "À demain."

    iris colere "N'encourage pas les visites !"

    $ hideGroup()

    jump _9_1_0_0_SOIR


label _9_1_0_0_SOIR:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_6
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0

    "La soirée se termine sans nouvel incident. Après avoir mangé, je retourne vers ma chambre en croisant quelques représentants qui parlent encore du vote et de tout ce que l'assouplissement du Commandement IV pourrait permettre."

    "Pour une fois, ils ont de bonnes raisons d'être optimistes."

    think "Un vote adopté sans crise, Elen qui parle déjà de festivals... Ça aurait presque pu être une bonne journée."

    "Je ralentis légèrement en passant devant la chambre d'Iris."

    "Aucun bruit particulier n'en sort."

    think "Soit elles dorment déjà, soit Iris a finalement réussi à imposer une frontière au milieu du lit."

    "Je continue jusqu'à ma chambre."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_7
    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je referme la porte derrière moi, retire ma veste et me laisse tomber sur le lit. La fatigue arrive presque immédiatement, mais ma tête refuse encore de suivre."

    think "Ryn savait qu'Anya était là."

    "Je repense à ce qu'elle nous a raconté : son absence totale de surprise, ses questions sur les dépôts, les contrôles, les scellés et ces détails qu'elle-même ne connaissait presque pas."

    think "Et dès que Kami a parlé des nouvelles inspections, il s'est mis à écouter."

    "Je me retourne sur le côté."

    think "Il n'a pourtant rien dit à Kami."

    think "S'il voulait simplement nous dénoncer, Nyra a raison : il l'aurait déjà fait."

    "C'est probablement ce qui me dérange le plus."

    think "Alors qu'est-ce que tu veux, Ryn ?"

    pause 1.0

    "Je ferme les yeux et force mon esprit à abandonner la question pour ce soir."

    think "Demain."

    think "J'y réfléchirai demain."

    "L'épuisement finit par prendre le dessus."

    $ blink()

    scene black with fade
    stop music fadeout 4.0

    call end_day("10") from _call_end_day_9100

    jump _10_1_0_0_REVEIL
