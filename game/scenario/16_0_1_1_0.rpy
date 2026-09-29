label _16_0_1_1_0_REVEIL_CHAMBRE:

    $ cafeteria_food_level = "low"
    $ current_period = "Matin"
    $ current_day = 16
    $ noam_has_juliette_drawing = False

    scene black with dissolve
    play sound "audio/sfx_heartbeat.mp3" fadein 0.8
    pause 1.0

    "J'ouvre les yeux avec l'impression d'avoir dormi dix minutes et dix heures à la fois. Ma tête pèse une tonne, ma bouche est sèche et pendant quelques secondes je reste allongé sans même savoir pourquoi quelque chose me paraît aussi profondément anormal."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    noam panne "..."

    "Je fixe le plafond en attendant que mon cerveau se remette en marche. La chambre est la même que d'habitude, mes affaires sont à leur place, la lumière passe entre les stores... pourtant cette sensation ne part pas."
    "Il manque quelque chose. Pas un objet. Quelque chose dans ma tête."

    "Je me redresse lentement et aussitôt une douleur sourde me traverse le crâne. Je ferme les yeux, une main contre mon front, puis j'essaie simplement de me rappeler comment je suis rentré ici."

    noam inquiet "Hier soir..."

    "La salle d'observation me revient. Les vidéos. La photo de Léa dans les mains de Kael. Puis l'enregistrement de ma propre chambre, avec Kael qui entre et repart avec le dessin de Juliette."

    noam reflexion "Après ça, je suis parti le chercher..."

    "Je me souviens du couloir. Je me souviens de l'avoir aperçu plus loin et de l'avoir appelé. Je me souviens même d'avoir accéléré pour le rattraper."
    "Et ensuite, rien. Plus rien."

    noam hesitation "... Non."

    "Je recommence à réflechir depuis le début, plus lentement, comme si j'avais simplement sauté une étape. La vidéo. Le dessin. Le couloir. Kael."

    noam inquiet "Je l'ai trouvé... Je sais que je l'ai trouvé. Je lui ai parlé."
    think "Mais de quoi ...?"

    "J'en suis certain sans réussir à expliquer pourquoi. Il s'est passé quelque chose d'important, quelque chose qui devrait être juste là, à quelques secondes de portée, mais chaque fois que j'essaie de l'attraper, ma tête se vide complètement."

    noam colere "Allez... réfléchis."

    "Je ferme les yeux plus fort, comme si ça pouvait aider. J'essaie de retrouver sa voix, l'endroit où on était, ce que je lui ai dit. Une image menace de revenir, puis disparaît avant même que je puisse la reconnaître."

    noam colere "Putain !"
    $ shake(7, 0.22)

    "Je frappe du plat de la main contre le matelas. La douleur dans mon crâne pulse immédiatement plus fort et je regrette mon geste."
    "Ce n'est pas un souvenir flou. Ce n'est pas le genre de soirée où tout finit par se mélanger avec la fatigue. C'est un trou net. Je sais ce qu'il y avait juste avant, je sais que quelque chose est venu après, mais entre les deux il n'y a absolument rien."

    "Je me lève et manque de perdre l'équilibre. En passant devant le miroir, je remarque seulement à quel point j'ai mauvaise mine : les yeux rouges, le visage tiré et cette expression d'idiot qui cherche une réponse sur son propre visage."

    noam triste "Qu'est-ce qui s'est passé... ?"

    play sound "audio/sfx_announce.mp3"
    pause 1.0
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Bonjour, mes chers représentants. J'espère que cette nouvelle journée vous trouve dans une forme éclatante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Enfin... certains plus que d'autres."

    "Je relève immédiatement les yeux vers l'écran."

    noam inquiet "..."

    kami "Aucun vote n'est prévu aujourd'hui. Profitez-en pour vous reposer, discuter, réfléchir à vos merveilleux choix passés... ou simplement essayer de passer quelques heures sans vous accuser mutuellement de quelque chose."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Je sais, je sais. Je vous en demande beaucoup."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Bonne journée à tous."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve

    "L'écran s'éteint. Je reste encore quelques secondes devant lui, avec la désagréable impression que sa remarque m'était destinée sans pouvoir en être sûr."

    noam reflexion "Kael..."

    "Je pourrais aller le voir tout de suite. Une partie de moi en a envie. Une autre refuse de débarquer devant lui sans même savoir ce que j'ai fait ou dit la veille."
    "La faim finit par trancher à ma place. Je n'ai presque rien dans le ventre et rester seul ici à forcer sur un souvenir qui ne revient pas ne m'avance à rien."

    jump _16_0_1_1_CAFETERIA_TENSION


label _16_0_1_1_CAFETERIA_TENSION:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_98
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.0

    "Je quitte les dortoirs en marchant moins vite que d'habitude. Ma tête s'est un peu calmée, mais le vide est toujours là, lourd, impossible à ignorer. À chaque fois que j'essaie de penser à Kael, je reviens exactement au même point : je l'ai cherché, je l'ai trouvé... et après, plus rien."

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_99
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "La cafétéria est déjà bien remplie quand j'arrive. Mara et Elias discutent près du buffet, Iris râle parce que quelqu'un a encore laissé une tasse vide sur la table et Elen essaie visiblement de convaincre Ryn de manger autre chose que du pain."
    "Pendant quelques secondes, personne ne fait particulièrement attention à moi, et ça me va très bien."

    $ showGroup([
        ("mara", "agace", 0.06),
        ("iris", "neutre", 0.20),
        ("lysa", "blase", 0.34),
        ("elen", "joie", 0.48),
        ("nyra", "neutre", 0.62),
        ("ryn", "fatigue", 0.76),
        ("elias", "neutre", 0.90),
    ])

    elen joie "Noam ! Il reste du café si tu veux. Enfin, je crois que c'est encore du café. Elias a dit qu'il était vraiment mauvais aujourd'hui."

    elias fatigue "J'ai dit qu'il avait goût de flotte. C'est différent."

    iris neutre "Non, pour une fois il a raison. Même moi j'arrive pas à finir le mien, et pourtant je suis prête à boire n'importe quoi le matin."

    mara agace "Waouh. Iris qui abandonne avant la fin d'une plainte, ça par contre c'est inquiétant."

    iris colere "Je peux reprendre si ça te manque."

    "Je prends une tasse sans vraiment suivre la conversation et m'assois au bout de la table. Le bruit autour de moi devrait aider, mais il me donne surtout l'impression d'avoir la tête encore plus pleine."

    lysa blase "T'as une sale tête."

    noam desaccord "Merci."

    lysa taquin "De rien. J'essayais de trouver une formulation douce, mais j'ai abandonné."

    "Je porte la tasse à mes lèvres et réalise seulement à ce moment-là que je n'ai pas mis de sucre. Je la repose presque immédiatement."

    iris inquiet "Attends... toi, tu bois jamais ton café comme ça."

    noam hesitation "J'ai oublié."

    mara agace "Bon, là ça devient grave. Quelqu'un appelle Sael, Noam a oublié son sucre."

    elen inquiet "Non mais sérieusement, tu vas bien ?"

    "Je relève les yeux. Cette fois, plusieurs personnes me regardent. Pas parce que j'ai fait une entrée dramatique ou parce que quelqu'un leur a raconté quoi que ce soit. Juste parce que je suis assis devant eux depuis deux minutes sans vraiment être là."

    noam desaccord "J'ai mal dormi. C'est tout."

    iris inquiet "Tu trembles un peu."

    noam colere "J'ai dit que ça allait."

    "Ma réponse part beaucoup plus sèchement que prévu. Iris se fige et je m'en veux immédiatement."

    noam culpabilite "Désolé. C'était pas contre toi."

    iris neutre "Ouais... j'avais compris."

    "Elle retourne à son assiette sans insister. Les autres aussi font semblant de reprendre leur conversation, mais l'ambiance vient clairement de perdre quelque chose."

    nyra reflexion "Kael n'est pas venu."

    "Je relève la tête avant même d'avoir le temps de faire semblant que ça ne m'intéresse pas."

    noam inquiet "Il est où ?"

    nyra neutre "Dans les dortoirs, probablement. Je l'ai croisé tôt ce matin."

    mara mefiant "Et ? Vu ta tête, y'a un 'mais'."

    nyra "Il m'a demandé si quelqu'un était entré dans sa chambre cette nuit. Puis il m'a demandé si j'avais vu quelqu'un toucher à ses affaires, si les caméras fonctionnaient normalement et si je savais qui avait accès aux enregistrements."

    ryn fatigue "Ça lui ressemble pas."

    nyra reflexion "Non."

    elias inquiet "Il s'est fait voler autre chose ?"

    nyra "Je ne sais pas. Il n'a pas voulu me répondre. Quand j'ai essayé de continuer la discussion, il a vérifié deux fois derrière moi avant de refermer sa porte."

    mara mefiant "Super. Donc maintenant on a Kael qui barricade sa chambre et regarde sous les lits. Je l'ai toujours trouvée chelou, mais là de plus en plus."

    lysa blase "Je donne encore trois jours avant qu'on commence tous à dormir avec une chaise sous la poignée."

    ryn desaccord "Si quelque chose se passe dans les dortoirs, on devrait au moins savoir quoi."

    nyra raison "Je suis d'accord. Mais il est inutile d'aller le coincer à dix devant sa porte. Dans son état, ça ne fera que renforcer ce qu'il pense déjà."

    "Je serre les doigts autour de ma tasse."

    think "Il pense quoi, exactement ?"

    "Une nouvelle fois, j'essaie de me rappeler ce qu'il s'est passé après l'avoir retrouvé hier. Une pression se forme derrière mes yeux, mais rien ne vient."

    elen inquiet "Noam ?"

    noam colere "Quoi ?"

    elen "Rien... Tu serres ta tasse super fort."

    "Je desserre immédiatement les doigts."

    noam hesitation "Je suis juste fatigué."

    mara agace "Ouais, ça on avait compris."

    noam colere "Alors arrêtez de me demander toutes les trente secondes si ça va !"

    "Cette fois, le silence tombe franchement. Même Mara ne trouve rien à répondre tout de suite."

    noam culpabilite "... Pardon."

    "Je pousse ma chaise en arrière avant que quelqu'un puisse reprendre. J'ai à peine touché à mon petit-déjeuner."

    iris inquiet "Tu vas où ?"

    noam desaccord "Prendre l'air."

    lysa blase "Dans une station spatiale. Excellent plan."

    "Malgré moi, un souffle m'échappe presque comme un rire. Ça ne dure pas."

    noam "Je reviens plus tard."

    "Je quitte la cafétéria sans expliquer davantage. Je sens les regards dans mon dos jusqu'à ce que la porte se referme."

    jump _16_0_1_1_CORRIDOR_KAEL


label _16_0_1_1_CORRIDOR_KAEL:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_100
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    "Je n'ai même pas décidé où aller quand une voix m'arrête derrière moi."

    kael fatigue "Noam."

    "Je me retourne. Kael est à quelques mètres, seul. Il a l'air encore plus fatigué que la veille et garde sa tablette serrée contre lui comme s'il craignait qu'on puisse la lui arracher."

    $ showGroup([
        ("noam", "inquiet", 0.30),
        ("kael", "fatigue", 0.62),
    ])

    noam surpris "Kael..."

    "Je cherche instinctivement ce qui devrait venir après son nom. Une accusation, une question, n'importe quoi. Rien n'arrive assez clairement pour sortir."

    kael fatigue "Qu'est-ce que tu veux encore ?"

    "Je le fixe quelques secondes, déstabilisé par la question."

    noam hesitation "Hein ? Je veux te parler de la vidéo."

    kael inquietude "Encore ça ?! Tu veux que je..."

    noam colere "Putain mais Kael, on te voit prendre ta propre photo. Celle dont tu jurais ne pas savoir où elle était passée."

    kael colere "Tu crois que je le sais pas ?! Tu crois que je ne m'en rappelle pas ?!"
    kael fatigue "Hier, j'ai quitté la salle parce que je voulais retourner fouiller ma chambre. Tu es resté devant les écrans."
    kael colere "J'ai tout fouillé ! TOUT ! Je ne l'ai pas retrouvé ! Où j'aurais bien pû la mettre hein ?"
    kael triste "J'y ai passé toute la soirée..."

    "Je secoue immédiatement la tête."

    noam desaccord "Quoi ? Tu y as passé toute la soirée. Mais... On était ensemble hier soir !"

    "Kael blanchit à vue d'oeil."

    kael "Qu'est-ce que tu racconte ? J'ai fouillé ma chambre toute la soirée, je ne t'ai pas vu après avoir quitté la salle d'observation."

    noam colere "Pourquoi tu le nies ?!"

    kael fatigue "Où ?"

    "La question me coupe net. Je sais que je l'ai trouvé. Je pourrais le jurer. Pourtant, dès que j'essaie de replacer un mur, une porte ou même sa position dans le couloir, tout se dérobe."

    kael inquietude "Où est-ce que tu m'as vu, Noam ?"

    noam colere "J'en sais rien ! C'était... C'était dans le couloir je crois !"

    "Ma voix résonne dans le couloir. Kael jette immédiatement un regard vers les caméras au-dessus de nous, puis fait un pas plus près."

    kael fatigue "Baisse d'un ton."

    noam colere "Me demande pas de baisser d'un ton alors que tu viens de me dire que tu ne m'as pas vu alors qu'on s'est reparlé hier soir !"
    noam triste "Putain, ça colle pas !"

    kael triste "Je te dis seulement ce dont je me rappelle."

    noam colere "J'ai regardé l'enregistrement de ma chambre. Tu étais dessus Kael, c'est toi qui a pris le dessin de Juliette !"
    noam reflechit "Je me rappelle être sorti pour te chercher. Je me rappelle t'avoir trouvé..."

    "Je m'arrête. Les derniers mots ont plus de mal à sortir."

    noam inquiet "Et après... Plus rien, je n'ai plus aucun souvenir de ce qu'il s'est passé après ça !"

    "Le silence change immédiatement entre nous. Kael ne semble pas soulagé. Au contraire, il recule légèrement et son regard devient plus méfiant."

    kael fatigue "Rien du tout ?"

    noam desaccord "Je me suis réveillé ce matin dans ma chambre. Je sais même pas comment je suis rentré."

    kael fatigue "On ne sait même pas ce qui s'est passé. Et vu ce qu'on a découvert hier... Tu avais raison, vaut mieux pas en parler aux autres."

    noam desaccord "Quel rapport avec les autres ?"

    kael "Si je comprends, on a vu une vidéo de moi volant la photo de ma propre sœur sans que j'en garde le moindre souvenir, puis une autre vidéo où j'entre dans ta chambre pour prendre le dessin de la tienne."
    kael triste "Pour l'instant, je me méfie de tout."

    noam surpris "Hein ? De moi ?!"

    kael fatigue "Tu viens de m'apprendre que tu as passé une partie de la soirée à me chercher et que tu ne te rappelles plus de ce qui s'est passé après m'avoir trouvé. Tu veux vraiment que je fasse comme si ça ne me posait aucune question ?"
    kael reflexion "Ou du moins, de notre mémoire. Avec ce qu'on a vu hier, je ne fais plus confiance à mes souvenirs."

    "La remarque me met en colère, surtout parce que je n'arrive pas à lui répondre honnêtement."

    kael fatigue "Je ne t'accuse pas. J'essaie de te faire comprendre le problème. Hier encore, moi non plus je ne pensais pas avoir fait quoi que ce soit."
    kael "Et... Disons que j'ai mes raisons de croire qu'il y a un problème bien plus grave."

    noam "Quoi encore ?"

    kael "Le vote d'hier a été validé, beaucoup plus d'informations sont accessibles. Pas tout, mais suffisamment pour consulter certaines données qui nous concernent directement."

    "Je le regarde, je ne comprends pas où il veut en venir."

    kael fatigue "Je te conseille d'aller consulter ton dossier médical. Je..."

    noam surpris "Depuis quand j'ai un dossier médical ici ?!"

    kael "Aucune idée, depuis qu'on est arrivés, j'imagine. J'ai vu qu'il était accessible en fouillant dans la salle des archives, alors... J'ai regardé."

    "Il hésite à continuer. Son regard repart vers la caméra, puis revient sur moi."

    kael fatigue "Il y a une mention que je ne comprends pas. Mais ça ne sert à rien de trop t'en dire. Va voir par toi-même."
    kael fatigue "Je suis sérieux. Je veux pas te souffler ce que j'ai lu avant que tu regardes toi-même. Si tu trouves rien, tant mieux. Si tu trouves la même chose... Alors c'est sans doute plus grave que ce qu'on imagine."

    "Je n'aime pas la manière dont il dit ça. Encore moins la peur qu'il essaie visiblement de cacher derrière son calme."

    noam inquiet "Et tu comptes faire quoi, toi ?"

    kael "Retourner dans ma chambre. J'ai vraiment envie de croiser personne."

    noam desaccord "Nyra nous a dit que tu agissais bizarrement."

    kael "Parce que tu crois que je peux faire comme si de rien n'était après avoir vu la vidéo d'hier ?!"
    kael colere "C'est impossible. J'ai trop de questions en tête et aucune réponse !"

    "Il me contourne sans attendre de réponse."

    noam "Kael. Attends."

    "Il s'arrête sans se retourner."

    noam hesitation "Hier... tu es sûr que je ne suis jamais venu te parler ?"

    kael fatigue "Si j'en crois mes souvenirs, je suis sûr. Mais je ne les crois plus, alors je ne sais pas."

    "Il repart vers les dortoirs. Je le regarde s'éloigner jusqu'à ce qu'il disparaisse au prochain croisement."

    think "Mon dossier médical, il est dans la salle des archives, c'est ça ?"
    "Je n'ai aucune envie d'aller fouiller là-dedans. Ce qui suffit largement à me convaincre que je dois le faire."

    $ hideGroup()
    call OFFER_DAILY_EXPLORATION(
        "_16_0_1_1_ARCHIVES_SAEL_CLIFFHANGER", 2,
        ["archive", "cafeteria", "maintenance"],
        "Rejoindre les archives", "archive"
    ) from _call_offer_exploration_j16


label _16_0_1_1_ARCHIVES_SAEL_CLIFFHANGER:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_101
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0

    "Les Archives sont presque vides à cette heure-ci. Je croise seulement deux terminaux allumés au fond de la salle et personne devant les rayonnages principaux."
    "Je m'installe devant un écran et passe mon badge."

    play sound sfx_beep

    "Je dois fouiller quelques menus avant de trouver la partie médicale. Visiblement, l'accès semble récent."

    noam reflexion "Donc Kael disait vrai..."

    "Je sélectionne mon nom."
    "Le dossier est beaucoup plus banal que ce que j'imaginais. Groupe sanguin, allergies, examens à l'arrivée, anciennes blessures, passages à l'infirmerie... Je descends rapidement jusqu'aux dernières lignes."
    "Une référence que je ne connais pas apparaît entre deux entrées."

    noam inquiet "M16... ?"

    "Je clique dessus. Rien ne s'ouvre. Pas de description, pas de date détaillée, pas de compte rendu. Juste ce code posé là comme s'il était censé suffire."

    noam desaccord "Évidemment."

    "J'essaie une recherche interne. Aucun résultat. Une seconde. Toujours rien."
    "Un bruit de pages qu'on tourne me fait lever la tête. Cette fois, ce n'est pas un terminal. Quelqu'un fouille réellement dans les rayonnages derrière moi."

    noam inquiet "Tomas ? C'est toi ?"

    sael neutre "Non, désolée de te décevoir."

    "Sael apparaît au bout de l'allée avec trois ouvrages coincés sous le bras. Elle pose le premier sur une table, l'ouvre presque au milieu et recommence à parcourir l'index."

    $ showGroup([
        ("noam", "inquiet", 0.30),
        ("sael", "reflechit", 0.64),
    ])

    noam surpris "Qu'est-ce que tu fais ici à cette heure-là ?"

    sael reflechit "Je cherche une référence."

    noam "Laquelle ?"

    "Elle ne répond pas tout de suite. Son doigt descend le long d'une colonne, s'arrête, puis repart sur la page suivante."

    sael "M16."

    "Je tourne immédiatement la tête vers mon écran."

    noam inquiet "Où as-tu entendu parler de ce truc ?"

    "Sael relève enfin les yeux vers moi."

    sael mefiant "Pourquoi, tu sais ce que c'est ?"

    noam "Non, je viens de le trouver dans mon dossier médical."

    "Son expression change à peine, mais elle referme lentement le livre qu'elle tenait."

    sael neutre "Moi aussi."

    noam "Hein ? Depuis quand tu sais qu'on peut les consulter ?"

    sael raison "Depuis ce matin. Je cherchais une ancienne fiche de soins dans le système. Le menu n'était pas là avant alors j'ai cliqué par curiosité."
    sael mefiant "J'essaye de trouver à quoi ça correspond depuis ce matin. Y'a rien sur internet, alors je regarde dans les archives papiers."
    sael reflechit "Je me suis dis que ça devait avoir un lien avec le médical, alors j'ai été cherché quelques bouquants dans l'infirmerie directement."

    "Elle prend le deuxième ouvrage, beaucoup plus épais, et l'ouvre à une série d'abréviations médicales."

    sael "Les vieux protocoles ont parfois été archivés sur papier. Les systèmes changent. Les livres restent."

    noam "Et tu penses que l'abréviation est là-dedans ?"

    sael "Elle doit bien être quelque part. On ne note pas un truc dans un dossier médical sans pouvoir retrouver ce que c'est."

    "Je m'approche de la table. Pour la première fois depuis mon réveil, ma frustration laisse place à quelque chose de plus froid."

    noam inquiet "En tout cas on est plusieurs à l'avoir. Donc ça doit être un point commune. Kael aussi l'a sans doute."

    "Sael s'arrête une fraction de seconde."

    sael mefiant "Tu as vu son dossier ? Comment tu as fais ? Ils sont bloqu..."

    noam "Non. C'est lui qui m'a dit de regarder mon dossier. J'ai pas tout compris mais il semblait avoir trouvé un truc bizarre dedans."
    noam reflechit "Alors ça doit être ça..."

    sael "Donc ça fait trois. Raaah, faut vraiment trouver ce que ça veut dire !"

    "Elle tourne encore quelques pages. Une première fois trop vite, puis elle revient en arrière."

    sael reflechit "Oh ! Attends."

    "Son doigt reste posé sur une ligne."

    noam inquiet "Tu as trouvé ?"

    "Sael ne répond pas immédiatement. Elle relit le passage une deuxième fois, puis pousse le livre vers moi."
    "Au milieu d'une liste de procédures anciennes, une seule ligne correspond au code de mon dossier."

    $ unlock_gallery_image("bg_cg042")
    $ investigation_add("m16")
    $ hideGroup()
    scene bg_cg042 at adaptive_fullscreen with memory_rip
    $ cam_move(fx=0.50, fy=0.70, z=1.10, t=5.5)
    $ horror_music_slow(fadeout=0.35, fadein=0.75)

    "Je reste à la regarder quelques secondes sans comprendre ce que les mots viennent réellement de dire."
    "Ma voix est plus basse que je ne le voudrais. Je relis la ligne, puis encore une fois, comme si elle pouvait finir par changer."

    noam inquiet "Qu'est-ce que ça veut dire ...?"

    "Sael tourne la page. La suivante a été arrachée proprement au ras de la reliure."

    noam inquiet "C'est une blague ?"

    sael mefiant "Visiblement, on a le droit d'en savoir un peu, mais pas trop quand même..."

    "Je reprends le livre et vérifie moi-même, comme si elle pouvait avoir raté quelque chose. Il ne reste qu'un morceau de papier au niveau de la couture."

    $ cam_reset(t=0.25)
    scene bg_archive at adaptive_fullscreen with memory_rip
    $ showGroup([
        ("noam", "colere", 0.30),
        ("sael", "mefiant", 0.64),
    ])

    noam colere "Putain..."

    "Je repense à mon réveil. Au couloir. À Kael que je suis certain d'avoir retrouvé sans être capable de me rappeler un seul mot après ça."

    sael inquiet "Mais... Qu'est-ce que ça veut dire ?"

    $ horror_audio_cut(duration=0.34, restore_volume=0.72)
    play sound "audio/sfx_glitch.mp3" volume 0.7
    with signal_stutter

    "Le terminal derrière nous émet soudain un grésillement. Quand je me retourne, mon dossier est toujours ouvert, mais la ligne M16 n'est plus visible à l'écran."

    sael mefiant "Pourquoi diable il y a écrit Accès mnésique ?!"
    sael colere "Qu'est-ce que c'est sensé vouloir dire..."

    noam colere "Qu'on nous a trifouillé la mémoire !"

    $ hideGroup()
    scene black with dissolve

    pause 1.0

    call end_day("17") from _call_end_day_17
    jump _17_0_1_1_0_ANNONCE_KAMI
