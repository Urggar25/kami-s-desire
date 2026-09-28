label _16_0_1_1_0_REVEIL_CHAMBRE:

    $ current_period = "Matin"
    scene black with dissolve
    play sound "audio/sfx_heartbeat.mp3" fadein 0.8
    pause 1.0

    "J'ouvre les yeux avec l'impression d'avoir dormi dix minutes et dix heures à la fois. Ma tête pèse une tonne, ma bouche est sèche et pendant quelques secondes je reste allongé sans même savoir pourquoi quelque chose me paraît aussi profondément anormal."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0
    show screen day1_wakeup_overlay(level="heavy")

    noam panne "..."

    "Je fixe le plafond en attendant que mon cerveau se remette en marche. La chambre est la même que d'habitude, mes affaires sont à leur place, la lumière passe entre les stores... pourtant cette sensation ne part pas."
    "Il manque quelque chose. Pas un objet. Quelque chose dans ma tête."

    "Je me redresse lentement et aussitôt une douleur sourde me traverse le crâne. Je ferme les yeux, une main contre mon front, puis j'essaie simplement de me rappeler comment je suis rentré ici."

    noam inquiet "Hier soir..."

    "La salle d'observation me revient. Les vidéos. La photo de Léa dans les mains de Kael. Puis l'enregistrement de ma propre chambre, avec Kael qui entre et repart avec le dessin de Juliette."

    noam reflexion "Après ça, je suis parti le chercher..."

    "Je me souviens du couloir. Je me souviens de l'avoir aperçu plus loin et de l'avoir appelé. Je me souviens même d'avoir accéléré pour le rattraper."
    "Et ensuite, rien."

    noam hesitation "... Non."

    "Je recommence depuis le début, plus lentement, comme si j'avais simplement sauté une étape. La vidéo. Le dessin. Le couloir. Kael."
    "Rien après."

    noam inquiet "Je l'ai trouvé... Je sais que je l'ai trouvé."

    "J'en suis certain sans réussir à expliquer pourquoi. Il s'est passé quelque chose d'important, quelque chose qui devrait être juste là, à quelques secondes de portée, mais chaque fois que j'essaie de l'attraper, ma tête se vide complètement."

    noam colere "Allez... réfléchis."

    "Je ferme les yeux plus fort, comme si ça pouvait aider. J'essaie de retrouver sa voix, l'endroit où on était, ce que je lui ai dit. Une image menace de revenir, puis disparaît avant même que je puisse la reconnaître."

    noam colere "Putain !"
    $ shake(7, 0.22)

    "Je frappe du plat de la main contre le matelas. La douleur dans mon crâne pulse immédiatement plus fort et je regrette mon geste."
    "Ce n'est pas un souvenir flou. Ce n'est pas le genre de soirée où tout finit par se mélanger avec la fatigue. C'est un trou net. Je sais ce qu'il y avait juste avant, je sais que quelque chose est venu après, mais entre les deux il n'y a absolument rien."

    "Je me lève et manque de perdre l'équilibre. En passant devant le miroir, je remarque seulement à quel point j'ai mauvaise mine : les yeux rouges, le visage tiré et cette expression d'idiot qui cherche une réponse sur son propre visage."

    noam triste "Qu'est-ce qui s'est passé... ?"
    hide screen day1_wakeup_overlay with soft_dissolve

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

    mara mefiant "Super. Donc maintenant on a Kael qui barricade sa chambre et regarde sous les lits. Ambiance saine."

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

    kael fatigue "Alors ?"

    noam hesitation "Alors quoi ?"

    kael inquietude "Tu voulais me parler hier."

    "Mon ventre se noue immédiatement."

    noam inquiet "Oui."

    kael "Tu m'as cherché après la salle d'observation."

    noam reflexion "Je... oui."

    kael fatigue "Pourquoi ?"

    "Je le fixe quelques secondes, déstabilisé par la question."

    noam hesitation "À cause de la vidéo."

    kael inquietude "Laquelle ?"

    noam colere "Kael, tu sais très bien laquelle. Celle où on te voit prendre toi-même la photo de Léa. Ta propre photo. Celle dont tu jurais ne pas savoir où elle était passée."

    "Son regard ne bouge pas, mais sa mâchoire se crispe."

    kael triste "Justement."

    kael fatigue "Hier, j'ai quitté la salle parce que je voulais retourner fouiller ma chambre. Tu es resté devant les écrans."

    noam "Oui."

    kael "Après ça, je ne t'ai pas revu."

    noam surpris "Quoi ?"

    kael calme "Je ne t'ai pas revu de la soirée."

    "Je secoue immédiatement la tête."

    noam desaccord "Non. Je suis parti te chercher."

    kael "Peut-être. Mais tu n'es jamais venu me parler."

    noam colere "Je t'ai trouvé."

    kael fatigue "Où ?"

    "La question me coupe net. Je sais que je l'ai trouvé. Je pourrais le jurer. Pourtant, dès que j'essaie de replacer un mur, une porte ou même sa position dans le couloir, tout se dérobe."

    noam panne "..."

    kael inquietude "Où, Noam ?"

    noam colere "J'en sais rien !"

    "Ma voix résonne dans le couloir. Kael jette immédiatement un regard vers les caméras au-dessus de nous, puis fait un pas plus près."

    kael fatigue "Baisse d'un ton."

    noam colere "Me demande pas de baisser d'un ton alors que tu viens de me dire que la moitié de ce dont je suis sûr n'est jamais arrivée !"

    kael triste "Je te dis seulement ce que je sais."

    noam "Je me rappelle avoir vu l'enregistrement de ma chambre. Je me rappelle t'avoir vu prendre le dessin de Juliette. Je me rappelle être sorti pour te chercher. Je me rappelle t'avoir trouvé..."

    "Je m'arrête. Les derniers mots ont plus de mal à sortir."

    noam inquiet "Et après..."

    kael inquietude "Après quoi ?"

    noam panne "..."

    kael "Noam ?"

    noam colere "Après, j'ai rien."

    "Le silence change immédiatement entre nous. Kael ne semble pas soulagé. Au contraire, il recule légèrement et son regard devient plus méfiant."

    kael fatigue "Rien du tout ?"

    noam desaccord "Je me suis réveillé ce matin dans ma chambre. Je sais même pas comment je suis rentré."

    kael inquietude "Et tu n'as rien dit aux autres ?"

    noam "Non."

    kael calme "Bien."

    noam colere "Bien ?!"

    kael fatigue "Oui, bien. Parce qu'on ne sait pas ce qui s'est passé. Et vu ce qu'on a découvert hier, raconter à toute la station que ta mémoire s'arrête au moment où tu venais me chercher serait une excellente manière de me désigner comme coupable avant même d'avoir compris quoi que ce soit."

    noam desaccord "Tu crois vraiment que c'est ça qui me préoccupe ?"

    kael "Je crois que depuis hier, on a vu une vidéo de moi volant la photo de ma propre sœur sans que j'en garde le moindre souvenir, puis une autre vidéo où j'entre dans ta chambre pour prendre le dessin de la tienne."

    kael triste "Alors oui. Pour l'instant, je me méfie de tout le monde. De toi aussi."

    noam surpris "De moi ?"

    kael fatigue "Tu viens de m'apprendre que tu as passé une partie de la soirée à me chercher et que tu ne te rappelles plus de ce qui s'est passé après m'avoir trouvé. Tu veux vraiment que je fasse comme si ça ne me posait aucune question ?"

    "La remarque me met en colère, surtout parce que je n'arrive pas à lui répondre honnêtement."

    noam desaccord "Je ne t'ai rien fait."

    kael calme "Tu n'en sais rien."

    "Je reste figé."

    noam colere "Fais attention."

    kael fatigue "Je ne t'accuse pas. J'essaie de te faire comprendre le problème. Hier encore, moi non plus je ne pensais pas avoir fait quoi que ce soit."

    "Je détourne les yeux. Les deux vidéos me reviennent, parfaitement nettes, elles."

    kael inquietude "Il y a autre chose."

    noam "Quoi encore ?"

    kael "Le vote d'hier nous a donné accès à plus d'informations qu'avant. Pas à tout, mais suffisamment pour consulter certaines données qui nous concernent directement."

    noam reflexion "Quel genre de données ?"

    kael fatigue "Ton dossier médical."

    noam surpris "Depuis quand j'ai un dossier médical ici ?"

    kael "Depuis qu'on est arrivés, j'imagine. Sael tient forcément un suivi, et le système enregistre plus de choses qu'on ne le pense."

    noam inquiet "Tu as regardé le tien ?"

    kael "Oui."

    noam "Et ?"

    "Il hésite. Son regard repart vers la caméra, puis revient sur moi."

    kael fatigue "Il y a une mention que je ne comprends pas."

    noam "Laquelle ?"

    kael calme "Va voir la tienne."

    noam colere "Kael..."

    kael fatigue "Je suis sérieux. Je veux pas te souffler ce que j'ai lu avant que tu regardes toi-même. Si tu trouves rien, tant mieux. Si tu trouves la même chose... on parlera."

    "Je n'aime pas la manière dont il dit ça. Encore moins la peur qu'il essaie visiblement de cacher derrière son calme."

    noam inquiet "Et tu comptes faire quoi, toi ?"

    kael "Retourner dans ma chambre."

    noam "Pour te barricader ?"

    kael fatigue "Pour éviter que quelqu'un entre pendant que je dors."

    noam desaccord "Nyra nous a dit que tu agissais bizarrement."

    kael "Nyra peut penser ce qu'elle veut. Hier, j'ai regardé mon propre visage faire quelque chose dont je ne me souviens pas. Aujourd'hui, tu viens me dire que tu as perdu la fin de ta soirée après m'avoir cherché."

    kael triste "Si ça te paraît pas suffisant pour devenir un peu parano, tant mieux pour toi."

    "Il me contourne sans attendre de réponse."

    noam "Kael."

    "Il s'arrête sans se retourner."

    noam hesitation "Hier... tu es sûr que je ne suis jamais venu te parler ?"

    kael fatigue "Sûr."

    "Il repart vers les dortoirs. Je le regarde s'éloigner jusqu'à ce qu'il disparaisse au prochain croisement."

    think "Mon dossier médical."

    "Je n'ai aucune envie d'aller fouiller là-dedans. Ce qui suffit largement à me convaincre que je dois le faire."

    $ hideGroup()
    jump _16_0_1_1_ARCHIVES_SAEL_CLIFFHANGER


label _16_0_1_1_ARCHIVES_SAEL_CLIFFHANGER:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_101
    scene bg_archive at adaptive_fullscreen, living_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0

    "Les Archives sont presque vides à cette heure-ci. Je croise seulement deux terminaux allumés au fond de la salle et personne devant les rayonnages principaux."
    "Je m'installe devant un écran et passe mon badge."

    play sound sfx_beep

    "Je dois fouiller quelques menus avant de trouver la partie médicale. Visiblement, l'accès est récent : plusieurs catégories portent encore la mention « consultation autorisée depuis le dernier amendement »."

    noam reflexion "Donc Kael disait vrai..."

    "Je sélectionne mon nom."

    "Le dossier est beaucoup plus banal que ce que j'imaginais. Groupe sanguin, allergies, examens à l'arrivée, anciennes blessures, passages à l'infirmerie... Je descends rapidement jusqu'aux dernières lignes."

    "Une référence que je ne connais pas apparaît entre deux entrées."

    noam inquiet "M16... ?"

    "Je clique dessus. Rien ne s'ouvre. Pas de description, pas de date détaillée, pas de compte rendu. Juste ce code posé là comme s'il était censé suffire."

    noam desaccord "Évidemment."

    "J'essaie une recherche interne. Aucun résultat. Une seconde. Toujours rien."

    "Un bruit de pages qu'on tourne me fait lever la tête. Cette fois, ce n'est pas un terminal. Quelqu'un fouille réellement dans les rayonnages derrière moi."

    noam inquiet "Tomas ?"

    sael neutre "Non."

    "Sael apparaît au bout de l'allée avec trois ouvrages coincés sous le bras. Elle pose le premier sur une table, l'ouvre presque au milieu et recommence à parcourir l'index."

    $ showGroup([
        ("noam", "inquiet", 0.30),
        ("sael", "reflechit", 0.64),
    ])

    noam surpris "Qu'est-ce que tu fais ?"

    sael reflechit "Je cherche une référence."

    noam "Laquelle ?"

    "Elle ne répond pas tout de suite. Son doigt descend le long d'une colonne, s'arrête, puis repart sur la page suivante."

    sael "M16."

    "Je tourne immédiatement la tête vers mon écran."

    noam inquiet "Comment tu connais ça ?"

    "Sael relève enfin les yeux vers moi."

    sael mefiant "Pourquoi ?"

    noam "Parce que je viens de le trouver dans mon dossier."

    "Son expression change à peine, mais elle referme lentement le livre qu'elle tenait."

    sael neutre "Moi aussi."

    noam surpris "Dans ton dossier médical ?"

    sael "Oui."

    noam "Depuis quand tu sais qu'on peut les consulter ?"

    sael raison "Depuis ce matin. Je cherchais une ancienne fiche de soins dans le système. Le menu n'était pas là avant."

    noam reflexion "Les autres sont au courant ?"

    sael "Non."

    noam "Pourquoi tu leur as rien dit ?"

    sael mefiant "Parce que je ne savais pas encore ce que j'avais trouvé."

    "Elle prend le deuxième ouvrage, beaucoup plus épais, et l'ouvre à une série d'abréviations médicales."

    sael "Les vieux protocoles ont parfois été archivés sur papier. Les systèmes changent. Les livres restent."

    noam "Et tu penses que M16 est là-dedans ?"

    sael "Je pense que si quelqu'un a pris la peine de laisser un code sans explication dans nos dossiers, je préfère chercher l'explication ailleurs que sur le même écran."

    "Je m'approche de la table. Pour la première fois depuis mon réveil, ma frustration laisse place à quelque chose de plus froid."

    noam inquiet "Kael a la même mention."

    "Sael s'arrête une fraction de seconde."

    sael mefiant "Tu as vu son dossier ?"

    noam "Non. Il me l'a dit."

    sael "Alors ça fait trois."

    noam "Tu crois que ça veut dire quoi ?"

    sael "Si je le savais, je ne serais pas en train de chercher."

    "Elle tourne encore quelques pages. Une première fois trop vite, puis elle revient en arrière."

    sael reflechit "Attends."

    "Son doigt reste posé sur une ligne."

    noam inquiet "Tu as trouvé ?"

    "Sael ne répond pas immédiatement. Elle relit le passage une deuxième fois, puis pousse le livre vers moi."

    "Au milieu d'une liste de procédures anciennes, une seule ligne correspond au code de mon dossier."

    $ unlock_gallery_image("bg_cg042")
    $ hideGroup()
    scene bg_cg042 at adaptive_fullscreen with memory_rip
    $ cam_move(fx=0.50, fy=0.70, z=1.10, t=5.5)
    $ horror_music_slow(fadeout=0.35, fadein=0.75)


    "Je reste à la regarder quelques secondes sans comprendre ce que les mots viennent réellement de dire."

    noam panne "..."

    sael neutre "Mémoire."

    noam desaccord "Je sais."

    "Ma voix est plus basse que je ne le voudrais. Je relis la ligne, puis encore une fois, comme si elle pouvait finir par changer."

    noam inquiet "Accès... ça peut vouloir dire plein de choses. Une consultation, un test, une extraction de données..."

    sael raison "Peut-être."

    noam "Il n'y a rien d'autre ?"

    "Sael tourne la page. La suivante a été arrachée proprement au ras de la reliure."

    "On se regarde."

    noam inquiet "C'est une blague ?"

    sael mefiant "Non."

    "Je reprends le livre et vérifie moi-même, comme si elle pouvait avoir raté quelque chose. Il ne reste qu'un morceau de papier au niveau de la couture."

    $ cam_reset(t=0.25)
    scene bg_archive at adaptive_fullscreen with memory_rip
    $ showGroup([
        ("noam", "colere", 0.30),
        ("sael", "mefiant", 0.64),
    ])

    noam colere "Putain..."

    "Je repense à mon réveil. Au couloir. À Kael que je suis certain d'avoir retrouvé sans être capable de me rappeler un seul mot après ça."

    noam peur "Sael..."

    sael "Quoi ?"

    noam "Moi, j'ai perdu la fin de ma soirée. Complètement."

    "Pour la première fois depuis qu'elle est apparue entre les rayonnages, Sael cesse de fouiller."

    sael inquiet "Depuis quand ?"

    noam "Après être parti chercher Kael. Je sais que je l'ai trouvé, mais après ça... rien. Je me suis juste réveillé dans ma chambre ce matin."

    "Elle baisse les yeux vers la ligne M16."

    sael mefiant "Et Kael ?"

    noam "Il dit qu'il ne m'a jamais revu hier soir."

    "Le silence qui suit est beaucoup trop long."

    noam inquiet "Toi aussi, tu as M16 dans ton dossier. Il te manque quelque chose ?"

    "Sael relève lentement les yeux."

    sael neutre "Non."

    noam surpris "Quoi ?"

    sael "Je me souviens d'hier. Du matin jusqu'au moment où je me suis couchée."

    "Mon regard retourne vers le livre."

    noam peur "Alors pourquoi tu as ça dans ton dossier ?"

    sael mefiant "C'est justement la question."

    $ horror_audio_cut(duration=0.34, restore_volume=0.72)
    play sound "audio/sfx_glitch.mp3" volume 0.7
    with signal_stutter

    "Le terminal derrière nous émet soudain un grésillement. Quand je me retourne, mon dossier est toujours ouvert, mais la ligne M16 n'est plus visible à l'écran."

    noam inquiet "... Elle était là."

    sael "Je sais."

    "Je rafraîchis la page. Rien. Je ferme le dossier, le rouvre, descends jusqu'au même endroit. La référence a disparu."

    noam colere "Non, non..."

    sael mefiant "Arrête."

    noam "Je viens de la voir !"

    sael "Moi aussi."

    "Elle referme le livre devant nous et garde une main posée dessus."

    sael neutre "Donc maintenant, on sait deux choses."

    noam inquiet "Lesquelles ?"

    sael "Ton souvenir s'arrête. Mon dossier porte le même code que le tien alors que je ne sens aucun trou."

    "Elle jette un regard vers le terminal où toute trace de M16 vient de disparaître."

    sael mefiant "Et quelqu'un ne veut pas qu'on regarde ça trop longtemps."

    $ hideGroup()
    scene black with dissolve

    pause 1.0

    call end_day("17") from _call_end_day_17
    jump _17_0_1_1_0_ANNONCE_KAMI
