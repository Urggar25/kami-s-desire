label _4_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4

    pause 1.2

    $ blink()
    "Je me réveille lentement. La lumière bleue des veilleuses me pique les yeux."
    $ blink()
    "C’est toujours la même lumière, mais ce matin elle semble plus froide, plus lourde."

    "Hier, on a voté. On a réussi à le faire."
    "On a appuyé sur le bouton vert. Tous les regards étaient sur nous à ce moment-là."
    "Et maintenant… c’est réel."
    "On a réussi à changer les choses. J'espère que c'est en bien..."

    $ blink()
    "Je reste allongé sur le dos, les bras le long du corps."
    "Mon cœur bat encore trop vite, comme si la nuit n’avait pas suffi à me calmer, à atténuer cette tension qui me parcoure tous les membres."

    "Est-ce qu’on a fait une erreur ?"
    "Vraiment ?"

    "On a supprimé les bons de rationnement."
    "On a coupé cette dépendance à Kami et à son pouvoir absolu."

    $ blink()
    "Mais pour quoi ? Pour qui ?"
    "Pour Limen ? Pour ceux qui n’ont ni champs, ni outils, ni force ?"
    "Ou juste pour les plus riches, ceux qui avaient déjà tout ?"

    "Je ferme les yeux. Les images de la veille reviennent en rafale dans mon esprit."
    "Julian qui lève le poing, souriant de façon triomphale."
    "Ryn qui frappe la table, les yeux embrumés."
    "Kael qui baisse la tête, comme s’il venait de signer la mise à mort d'un tas de gens."
    "Et moi… au milieu. Silencieux. Ou presque."

    "J’ai voté. Mais j’ai laissé les autres porter le poids des mots."
    "Et si c’était une erreur ?"
    "Et si on venait de condamner des milliers de personnes à crever de faim ?"
    "Et si le commerce ne suffisait pas ?"
    "Et si le marché ne sauvait que ceux qui avaient déjà de quoi acheter ?"

    pause 2.0

    "Je roule sur le côté. Mon regard tombe sur la petite photo holographique sur la table de nuit."
    "Une famille. C'est pas la mienne. Celle d’un ami qu'il m'avait envoyée il y a des mois."
    "Ils sourient. La vie n'était peut être pas si mal ?"
    "Je me demande s’ils sourient encore ce matin."

    play sound sfx_announce
    "Un bip aigu me fait sursauter."
    "L’écran mural s’allume d’un coup sec, lumière crue."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "8 heures pile, mes petits pionniers du chaos !"
    kami "Levez-vous, la révolution n'attends pas !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit point matinal, parce que je sais que vous adorez quand je vous mets le nez dans votre merde :"
    kami "Nexus et Orbite se régalent déjà. Marchés improvisés, trocs qui fleurissent, pièces artisanales qui tintent."
    kami "Pendant ce temps à Limen… disons que les files d’attente sont plus longues que vos listes de regrets."
    kami "Quelques trocs sauvages, quelques poings serrés, quelques ventres qui crient."
    kami "Et à Orbite ? Une petite alarme hier soir. Rien de grave… pour l’instant."
    kami "Alors champions du changement : toujours aussi fiers de votre gros bouton vert ?"
    kami "Ou est-ce que certains d'entre vous commencent à sentir le goût de la merde dans la bouche ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais oh ! Pourquoi je vous spoile ?!"
    kami "Vous aurez l'occasion de voir tout ça EN PERSONNE à la cafétéria !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    "L’écran s’éteint. Le silence revient, plus lourd qu’avant."
    "Je reste assis sur le lit. Les mains tremblantes."
    "Elle a raison."
    "On a ouvert la porte au changement."
    "Mais je ne sais pas si on est prêts à voir ce qui va en sortir."

    pause 1.5

    play sound sfx_drop
    "Un bruit sourd résonne dans le couloir."
    "Un cri étouffé, puis un choc contre une porte."
    "Quelqu’un a frappé quelque chose. Ou quelqu’un."

    "Je me lève d’un bond. Mon cœur cogne."
    "Je tends l’oreille. Plus rien."
    "Juste le silence. Et l’écho de ce cri dans ma tête."

    "Je ne sais pas si c’est déjà commencé."
    "Mais je sais que ça va commencer."

    jump _4_1_CAFETERIA_ECRANS

# Durée : 1m35
# Total : 1h 55m 35s

label _4_1_CAFETERIA_ECRANS:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 1.0

    "J’entre dans la cafétéria. L’air est chargé : rations réchauffées, métal chaud, tension palpable."
    "Les écrans muraux sont allumés. Tout le monde est déjà là, ou presque. Les regards sont rivés dessus."

    "Je m’approche d’un distributeur. Je prends une ration au hasard. Je n’ai pas faim, mais il faut bien faire semblant."

    "Les images défilent en boucle, commentées par une voix synthétique neutre :"

    "Nexus : premiers marchés locaux ouverts. Échanges fluides. Pièces artisanales acceptées."
    "Orbite : exportations en hausse. Demande forte pour les outils et les filtres."
    "Limen : files d’attente devant les anciens points de distribution. Premiers signes de troc sauvage."

    $ showP("lysa", "determine", 0.50)  # centre
    lysa "Regardez ça… ils commencent à s’organiser."
    lysa "À Limen, ils troquent déjà. C’est pas rien. C’est même… encourageant."

    $ showP("kael", "calme", 0.88)  # droite
    kael "À Orbite, ça tient."
    kael "Pour l’instant, pas d’alarme grave. Pas de laser. Pas de panique."
    kael "C’est stable. Plus stable que je ne le pensais."

    $ showP("ryn", "colere", 0.12)  # gauche
    ryn "Stable pour vous, peut-être."
    ryn "À Limen, ils commencent à se battre pour un sac de patates. C’est ça votre stabilité ?"

    hide lysa
    $ showP("julian", "detendu", 0.50)  # centre
    julian "C’est le début. Juste le début."
    julian rire "Et au moins ça veut dire qu'il y a déjà des patates !"
    julian "Les trocs marchent déjà. Imaginez quand ce sera bien organisé."

    hide kael
    $ showP("mara", "joie", 0.88)  # droite
    mara "Au moins de nouveaux produits vont pas tarder à débarquer."

    hide ryn
    $ showP("tomas", "hesitation", 0.12)  # gauche
    tomas "Euh… les rapports montrent que les prix sont déjà en train de fluctuer."
    tomas "À Nexus, certains produits ont doublé en valeur en 24 heures."
    tomas "C’est… c’est pas forcément mauvais, hein ?"

    hide julian
    $ showP("elen", "joie", 0.50)  # centre
    elen "C'est le début c'est normal ! C’est génial !"
    elen "Les gens vont enfin pouvoir choisir ce qu’ils veulent !"
    elen "On va avoir des épices, des vêtements neufs, des trucs qui sentent bon !"

    hide mara
    $ showP("iris", "desaccord", 0.88)  # droite
    iris "Pff. Choisir avec quoi ?"
    iris "Les pauvres vont regarder les rayons pleins depuis dehors. Comme d’habitude."

    hide tomas
    $ showP("nyra", "raison", 0.12)  # gauche
    nyra "Les trocs discrets marchent déjà ici, au Conclave."
    nyra "Si on légalise tout, ça peut s’étendre. Mais il faut des règles claires."
    nyra "Sinon, c’est le chaos."

    hide elen
    $ showP("noam", "raison", 0.50)  # centre
    noam "Ce que j’entends, c’est que... les repères ont disparu."
    noam "Il me semble qu’on a enlevé quelque chose sans vraiment prévoir ce qui prendrait la place."
    noam "Les gens s’organisent. Certains. Pas partout."

    hide iris
    $ showP("sael", "mefiant", 0.88)  # droite
    sael "…"
    sael "Ils s’organisent déjà."
    sael "Le texte les force à continuer."

    "Les écrans continuent de tourner. Des visages fatigués à Limen. Des sourires crispés à Nexus."
    "Je pose ma ration intacte sur la table. Je n’arrive pas à avaler."
    "Certains n'ont rien à manger ce matin."

    hide sael
    hide nyra 

    $ showP("lysa", "determine", 0.30)  # centre
    "Lysa me jette un regard en coin."
    lysa "Tu regrettes déjà ?"
    lysa "Ce n'est pas toi qui voulait qu'on se batte pour faire changer les choses ?"
    lysa sourire "Au moins, là, on a réussi."

    "Je ne réponds pas. Je ne sais pas."

    hide lysa

    "La salle est silencieuse. Chacun regarde les écrans comme on regarde un accident."
    "On a gagné hier. Mais ce matin, on commence à payer."

    hide noam

    jump _4_1_TEMPS_LIBRE_1

    return

# Durée : 1m20
# Total : 1h 56m 55s

label _4_1_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Après le petit-déjeuner, j'ai quelques heures devant moi."
    "Je ne sais pas enncore quoi faire.."

    call START_FREE_TIME("_4_1_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_4_1

# Durée : 1m05
# Total : 1h 58m 0s

label _4_1_RETOUR_CONCLAVE_ANALYSE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.8

    pause 1.2

    "L’après-midi est déjà bien entamé. Je traîne encore dans les couloirs quand un son strident retentit dans tout le Conclave."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention, attention, mes petits représentants adorés !"
    kami "Rassemblement immédiat dans la salle principale."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On a du pain sur la planche. Il faut qu'on prépare le prochain vote !"
    kami "Bougez-vous, nos téléspectateurs ne vont pas attendre vos siestes digestives."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L’écran s’éteint. Un silence gêné parcourt les couloirs."
    "Je soupire et me dirige vers la salle. Les autres font pareil, au compte-gouttes."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.5

    "Un par un, ils arrivent. Julian le premier, vraisemblablement toujours pressé de montrer qu’il est là."
    "Puis Ryn, poings serrés. Elen, nerveuse et Mara, un sourire en coin."

    $ showP("julian", "determine", 0.50)  # centre
    julian "On est tous là ?"
    julian "Allons-y, qu’on en finisse..."
    julian rire "Qu'on avance !"

    $ showP("ryn", "colere", 0.88)  # droite
    ryn "Finir quoi ? Encore un vote pour tous nous faire crever ?"

    $ showP("elen", "inquiet", 0.12)  # gauche
    elen "C’est peut-être une bonne nouvelle, non ?!"
    elen "On a déjà gagné une fois…"

    hide julian
    $ showP("mara", "agace", 0.50)  # centre
    mara "Gagné ? On a juste ouvert la boîte de Pandore."
    mara "Et maintenant on va tous en payer le prix."

    hide ryn
    $ showP("tomas", "hesitation", 0.88)  # droite
    tomas "Euh… je crois qu’on devrait écouter Kami d’abord…"
    tomas "Avant de paniquer… Enfin, on sait pas ce qui va être annoncé…"

    hide elen
    $ showP("iris", "desaccord", 0.12)  # gauche
    iris "Paniquer ?"
    iris "On est déjà dans la mouise. Regardez ce qu'il se passe à Limen."

    hide mara
    $ showP("kael", "triste", 0.50)  # centre
    kael "Et Orbite… si ça dégénère là-haut…"
    kael "Non en fait. Je préfère même pas imaginer."

    hide tomas
    $ showP("nyra", "raison", 0.88)  # droite
    nyra "On est tous là. On attend quoi ?"

    hide iris
    $ showP("noam", "raison", 0.12)  # gauche
    noam "Il me semble qu'on l'attend, ELLE."
    noam reflexion "Je ne sais pas si on peut faire autre chose..."

    hide kael
    $ showP("lysa", "blase", 0.50)  # centre
    lysa "On sait aussi que ça va être long jusqu'au vote."
    lysa "Si je me rappelle bien, ça ne sera que dans trois jours..."
    lysa "Et que certains vont encore parler pour ne rien dire."

    hide nyra
    $ showP("sael", "mefiant", 0.88)  # droite
    sael "…"
    sael "Je ne sais pas pourquoi, j'ai un mauvais pressentiment."

    "Un silence tombe. Personne n’ose répondre."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bon, maintenant que vous êtes tous là, on peut commencer."
    kami "Prochain vote, mes chéris :"
    kami "Ahhh !! Roulement de tambour !"

    play sound sfx_tambour
    pause 2.0

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser les déplacements entre les districts ?"
    kami "Si vous votez pour, les personnes pourront voyager d'un district à l'autre."
    kami "Si vous votez contre, on garde la même chose qu'aujourd'hui."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    show screen day3_codex_logo

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et promis, vous ne serez pas surpris cette fois-ci."
    kami "L'énoncé est parfaitement clair."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    "L’écran affiche deux immenses boutons comme pour nous rappeler notre mission."

    $ showP("ryn", "colere", 0.50)  # centre
    ryn "Il n'y a pas le choix, il faut voter pour !"
    ryn "J’ai vu ce que les frontières fermées font aux gens."
    ryn "À Limen, on gardait une muraille invisible. Les Gardiens étaient ..."
    ryn triste "Enfin... Je refuse que ça continue. Il faut laisser les gens bouger !"

    pause 0.8

    $ showP("kael", "triste", 0.88)  # droite
    kael "Les gardiens ? De qui tu parles ?"

    $ showP("sael", "mefiant", 0.12)  # gauche
    sael "…"
    sael "Les Gardiens… ce sont ceux qui ont tracé la frontière entre Limen et les autres districts."
    sael "Ils ont exploré. Ils ont creusé la tranchée. Ils sont morts par milliers les premiers mois en cherchant précisément le tracé de la frontière."
    sael raison "À Limen, on les vénère. Ils ont sacrifié leur vie pour qu’on reste chez nous."
    sael triste "Si quelqu'un traverse la frontière, il est immédiatament abattu..."

    ryn "Et je refuse de continuer à payer ce prix."
    ryn "Je veux que ça s’arrête, Sael. Je veux que ça s’arrête pour de bon."

    kael triste "Ces tirs de rayon ... On sait que c’est définitif."
    kael triste "Mais on fait semblant que c’est loin. Toi… tu étais là. Tu voyais leurs visages avant."

    hide ryn
    $ showP("lysa", "blase", 0.50)  # centre – remplace Ryn
    lysa "Si je comprends bien, t’étais là pour les empêcher de passer."
    lysa "Et maintenant tu veux les laisser passer."

    pause 1.0

    hide kael
    $ showP("noam", "determine", 0.88)  # droite
    noam "Ce que j’entends, Ryn... c’est que tu as fait ça pour protéger les gens."
    noam hesitation "Mais je me demande si on peut encore vivre comme ça."
    noam "Libre circulation... la fin des murs. Des lasers. Des gardiens. Il me semble que c’est ce que ça veut dire."

    hide lysa
    $ showP("ryn", "colere", 0.50)  # centre – retour
    ryn "Ca marquera peut être la fin de notre mission..."

    hide noam
    $ showP("julian", "determine", 0.88)  # droite
    julian "Enfin quelqu’un qui parle avec du cœur !"
    julian "La libre circulation, c’est l’espoir. Les districts doivent pouvoir s’aider, partager et survivre ensemble."

    hide sael
    $ showP("lysa", "blase", 0.12)  # gauche
    lysa "Disons que ça c'est dans un monde idéal."
    lysa "Dans la vraie vie comment tu feras pour empêcher les gens de s'entretuer ?!"
    lysa triste "On sait tous comment ça finit quand on laisse les gens bouger sans contrôle."
    lysa reflexion "Les frontières fermées étaient cruelles, mais au moins ça limite la casse."

    hide ryn
    $ showP("elias", "determine", 0.50)  # centre
    elias "Je suis d'accord avec Lysa. Ca ne fait qu'un an que la paix est enfin là."
    elias "On a tous vu ici des gens mourir dans des guerres contre les autres pays."
    elias reflechit "Kami nous a débarassé de ça, d'accord, mais ça n'a pas effacé la colère des gens."

    hide julian
    $ showP("iris", "desaccord", 0.88)  # droite
    iris "Et bien alors ? On ne veut pas des pauvres chez soi hein ?"
    iris "Les pauvres gens apprécieront vos commentaires de bourgeois."
    iris "Et Limen sera encore le premier à payer."

    hide elias
    $ showP("sael", "mefiant", 0.50)  # gauche
    sael "Tu te trompes."
    sael "C'est hors de question de voter ça."
    sael triste "Chacun reste sur sa terre. Chacun se débrouille."
    sael peur "Les déplacements, c’est la guerre qui revient. Pour moi c'est absolument inimaginable."

    "Sael croise les bras. Son ton est définitif, tranchant comme une lame."

    hide sael
    $ showP("elias", "colere", 0.50)  # centre – Elias revient pour la provoquer
    elias "Sael, écoute… D'un autre côté si on laisse les gens bouger, on peut mieux partager les ressources."
    elias "Tu peux pas refuser ça juste parce que t’as peur."
    elias jaloux "Réfléchis ! C’est notre chance !"

    hide iris
    $ showP("sael", "colere", 0.88)  # droite – retour
    sael "Réfléchir ?"
    sael culpabilite "J’ai réfléchi ! C’est non !"
    sael "Tu ne comprends rien !"
    sael triste "Tu ne sais rien."

    hide sael
    with moveoutright

    play sound sfx_door volume 8.0
    "Sael se lève d’un coup. Elle tourne les talons et quitte la salle en claquant la porte."
    with hpunch
    with vpunch
    with hpunch

    pause 0.5

    hide elias
    $ showP("mara", "agace", 0.50)  # centre
    mara "Non mais attends Sael ! Reviens !"
    mara doute "Putain, vous cassez les couilles !"

    hide mara
    with moveoutright

    play sound sfx_door volume 8.0
    "Mara se lève et la suit en courant hors de la pièce."
    with hpunch

    hide mara
    $ showP("julian", "determine", 0.88)  # droite
    julian "Laissez-la. Elle ne changera pas d’avis."
    julian inquiet "Mais on peut pas laisser la peur dicter notre avenir."

    $ showP("noam", "raison", 0.12)  # gauche
    noam "Je me demande si c’est vraiment juste de la peur."
    noam reflexion "Ce que j’entends dans ce que dit Sael... les territoires. Peut-être que c’est là que tout commence."

    hide noam
    $ showP("ryn", "colere", 0.50)  # centre
    ryn "On ne peut pas laisser ça comme ça."
    ryn determine "Sael est trop bornée. Elle va tout faire foirer !"

    hide julian
    $ showP("kael", "inquiet", 0.88)  # droite
    kael "Elle a ses raisons."
    kael triste "On a tous nos démons."

    hide ryn
    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Le texte est clair : mais qu'est ce qu'on devrait faire ?!"

    hide nyra
    $ showP("tomas", "hesitation", 0.12)  # gauche
    tomas "Euh… Il faut dire que ça peut aussi aider les marchandises à bouger plus rapidement."
    tomas "Mais Bon, c'est sûr que ça risque aussi de créer des incidents."

    hide kael
    $ showP("iris", "desaccord", 0.88)  # droite
    iris "N'empêche bravo, avec vos commentaires à la con vous avez réussi à blesser Sael."

    "Sur ces mots, Iris quitte à son tour la pièce."

    hide iris
    with moveoutleft

    "Le silence retombe. Chacun pèse le pour et le contre dans son esprit."

    jump _4_1_APRES_CLASH_PRE_FETE

# Durée : 3m05
# Total : 2h 01m 05s

label _4_1_APRES_CLASH_PRE_FETE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    pause 1.2

    $ showP("julian", "decu", 0.50)  # centre
    julian "Bon… on va pas rester plantés là toute la soirée."
    julian joie "On a gagné un vote. On mérite au moins un verre."

    $ showP("elen", "joie", 0.88)  # droite
    elen "C’est vrai !"
    elen content "Allez, on fait une petite fête. Juste pour décompresser."
    elen "Je m’occupe de tout. Nourriture, boisson, musique, ambiance !"

    $ showP("noam", "raison", 0.12)  # gauche
    noam "Une fête… maintenant ?"
    noam "Après ce qui vient de se passer ?"

    elen "Justement après !"
    elen "Si on reste tous à ruminer, on va finir par se détester."
    elen reflexion "Nyra, tu peux aller chercher Mara et Sael ? Dis-leur que c’est juste pour boire un coup et se détendre."

    hide noam
    $ showP("nyra", "surpris", 0.12)  # gauche
    nyra "Moi ?!"
    nyra reflexion "Bon… je vais essayer."
    nyra neutre "Je te garantie rien"

    hide nyra
    with moveoutright

    "Nyra soupire et sort à son tour."

    $ showP("noam", "neutre", 0.12)  # gauche
    elen "Et toi, Noam…"
    elen "Tu peux aller chercher Iris ?"
    elen "J'imagine qu'elle est dans sa chambre. Elle a besoin de se changer les idées."

    "Je hoche la tête. Je n’ai pas le cœur à refuser."

    hide elen
    hide julian

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je marche jusqu’à la chambre d’Iris."

    scene bg_dortoir at adaptive_fullscreen with dissolve

    "La porte est entrouverte. Je frappe doucement."

    iris "C’est qui ?"

    "Je pousse la porte. Iris est assise sur son lit, les genoux ramenés contre elle."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Elle a l’air épuisée."

    $ showP("iris", "triste", 0.50)
    iris "Ah… c’est toi."
    iris "T’es venu me faire la morale ?"

    "Je m’assois à côté d’elle. Pas trop près."

    hide iris
    scene bg_cg018 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg018")

    "Je lui explique qu’Elen organise une petite fête pour décompresser."
    "Iris rit sans joie."

    iris "Une fête… après ça ?"
    iris "Sael est partie en claquant la porte. Mara l’a suivie. Et nous, on fait quoi ? On boit pour oublier ?"

    noam "C'est peut être mieux que de rester seule."
    noam "Ca nous fera peut être du bien."

    iris "T’as raison… comme d’habitude."
    iris "Bon, allons-y. Mais si Julian commence à faire ses beaux discours, je te jure que je le frappe."

    noam "Je me demande si je peux faire quelque chose."
    noam "Quoi que... Pour le spectacle."
    
    "Iris sourit puis se relève légèrement."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    "On marche ensemble vers la salle de repos."

    scene bg_couloir at adaptive_fullscreen with dissolve
    "Les couloirs sont silencieux, mais on entend déjà de la musique au loin."

    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "La fête a déjà commencé. Elen a sorti des rations alcoolisées. Julian sert des verres."
    "Ryn est déjà là, un verre à la main, les épaules un peu moins tendues."
    "Nyra revient rapidement avec Mara et Sael. Sael a l’air calmée, mais elle reste en retrait."

    $ showP("elen", "content", 0.50)
    elen "Ah ! Vous êtes là !"
    elen joie "Allez, buvez un coup. On a gagné hier. On mérite au moins ça."

    "Je regarde autour de moi."
    "On rit. On parle. On boit."
    "Mais sous les sourires, je sens toujours la même peur."

    "On a gagné une bataille."
    "Mais la guerre ne fait que commencer."

    jump _4_1_FETE_IMPROVISEE

# Durée : 1m25
# Total : 2h 02m 30s

label _4_1_FETE_IMPROVISEE:

    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    pause 1.0

    "La salle de repos est transformée en quelques minutes."
    "Elen a sorti des boissons alcoolisées, des verres en plastique sont disposés partout, et une petite enceinte qui diffuse une musique électronique douce."
    "Les lumières bleues sont tamisées par des tissus improvisés. L’ambiance est presque chaleureuse… mais personne n’ose vraiment se détendre."
    "Elen distribue des verres avec un sourire un peu forcé. Tout le monde est là."
    "Sael reste en retrait près de la porte, bras croisés, mais elle accepte un verre sans un mot."

    $ showP("julian", "sourire", 0.88)  # droite
    julian "A nous, qui avons osé faire changer les choses."

    "Il lève son verre. Quelques rires fusent, mais ils sonnent faux. Personne n’est vraiment à l’aise."

    $ showP("elias", "reflechit", 0.12)  # gauche
    elias "À l’espoir… ouais."
    elias "Mais est-ce qu’on est prêts pour ce qui arrive ?"

    $ showP("lysa", "blase", 0.50)  # centre
    lysa "Prêts ou pas, c’est fait."
    lysa "On boit pour oublier, ou on boit pour célébrer ?"
    lysa sourire "Au final, peu importe. Santé."

    "La musique tourne. Quelques-uns bougent timidement. Mais l’ambiance reste lourde, comme si tout le monde attendait que quelqu’un dise que c’était une mauvaise idée."

    "Soudain, l’écran mural s’allume d’un coup. Un rire familier retentit."

    play sound sfx_announce
    pause 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous n’alliez quand même PAS faire une fête sans moi ?!"
    kami "Mes petits rebelles éméchés… je suis vexée !"
    kami "Trinquons ensemble, allez !"
    kami "À votre courage… ou à votre inconscience. Santé !"

    "Kami lève un verre virtuel. L’écran clignote vert et rouge en rythme avec la musique."
    "Puis elle disparaît aussi vite qu’elle est venue."

    hide screen kami_broadcast_ui
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    "Un rire général, un peu forcé, éclate."
    "Julian tape sur l’épaule de Tomas. Elen monte le son."
    "Les verres se remplissent à nouveau."

    "La soirée avance. Et peu à peu, l’alcool fait son effet."
    "Les voix montent. Les rires aussi."
    "Ryn danse maladroitement avec Elen. Julian raconte une anecdote exagérée. Kael sourit enfin. Même Sael accepte un deuxième puis un troisième verre."

    $ showP("mara", "ivre", 0.50)  # centre
    mara "Bon… ça suffit les mines d’enterrement."
    mara "On va pimenter un peu la soirée."
    mara "Jeu de la bouteille, qui est partant ?"

    "Elle fait tourner une bouteille vide sur la table basse. Les regards se croisent, entre amusement et gêne."

    hide mara
    $ showP("tomas", "hesitation", 0.50)  # centre
    tomas "Euh… c’est quoi le jeu de la bouteille ?"
    tomas "J’ai jamais joué à ça…"

    $ showP("mara", "taquin", 0.88)  # droite
    mara "Oh mon dieu, Tomas !"
    mara "C’est simple : on tourne la bouteille, et les deux qui sont désignés doivent s'embrasser."
    mara "C’est pour les gamins… ou les adultes qui veulent s’amuser un peu."

    $ showP("iris", "desaccord", 0.12)  # gauche
    iris "Pff. C’est ridicule."
    iris "Je… je vais me coucher."

    "Iris tente de s’éloigner discrètement, mais Mara l’attrape par le bras."

    $ showP("mara", "joie", 0.20)  # gauche – switch position pour attraper
    mara "Non non non, Iris !"
    mara "Tu restes. On a besoin de ton corps de rêve pour pimenter ce jeu."
    mara "Allez, assieds-toi. Un verre et tu changeras d’avis."

    iris fatigue "Lâche-moi !"
    iris fatigue "Pfff... Bon… d’accord. Mais si la bouteille tombe sur moi, je vous maudis tous."
    iris gene "Mais je ne joue que si Noam joue."

    $ showP("lysa", "jaloux", 0.88)  # gauche – switch position pour attraper
    lysa "Hein ?? Pourquoi ça ?"

    iris gene "P-Pour rien enfin !"
    iris gene "C'est plus amusant si tout le monde participe, c'est tout !"
    
    "Mara rit. Iris s’assoit, boudeuse."

    menu:
        "Accepter de jouer":
            $ jeu_bouteille_accepte = True
            "Je hoche la tête. Pourquoi pas. Ça pourrait détendre l’atmosphère."
            jump _4_1_JEU_BOUTEILLE

        "Refuser poliment":
            $ jeu_bouteille_accepte = False
            "Je décline d’un geste. Pas ce soir."
            mara "Tant pis pour toi, Noam. On va bien s’amuser sans toi."
            jump _4_1_FIN_SOIREE

    return

# Durée : 1m30
# Total : 2h 04m 00s

label _4_1_JEU_BOUTEILLE:

    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_romantic_atmosphere.mp3" fadein 1.5

    pause 0.6

    $ showP("mara", "ivre", 0.50)  # centre
    mara "Allez, premier round !"
    mara "Tourne, tourne, petite bouteille… fais-nous rêver !"

    "La bouteille ralentit… s’arrête sur Noam."

    $ showP("noam", "surpris", 0.88)  # droite
    noam "Moi ? Sérieusement..."

    "La bouteille pointe ensuite Lysa."

    $ showP("lysa", "blase", 0.12)  # gauche
    lysa "Évidemment que c’est moi... Raah ! Allez, viens Noam."

    mara "Oh ! Le couple parfait !"
    mara "Embrassez-vous, et pas de bisou sur la joue hein !"

    scene bg_cg019 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg019")

    "J'hésite une seconde. Lysa hausse un sourcil et se penche en avant avec un sourire en coin."
    "Raaah ! Ca ne sert à rien d'y penser !"
    "Nous nous embrassons rapidement sur la bouche. C’est bref, mais leurs lèvres restent une seconde de trop."

    "La salle explose de rires et d’applaudissements légers."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showP("julian", "joie", 0.88)  # droite
    julian "Pas mal ! Pas mal du tout !"
    julian "J'adore ce jeu !"

    $ showP("elen", "joie", 0.50)  # droite
    elen "Lysa ! T’as rougi ! C'est trop mimiii !"

    $ showP("lysa", "gene", 0.12)  # gauche
    lysa "C’est l’alcool, rien de plus. Pas lui."
    lysa "Mais il embrasse pas mal, je m'y attendais pas."

    noam "Merci… je crois."

    hide noam
    hide lysa
    hide elen
    hide julian

    $ showP("mara", "ivre", 0.50)  # centre
    mara "Deuxième round ! On monte le niveau !"

    "La bouteille tourne… s’arrête sur Tomas."

    $ showP("tomas", "gene", 0.12)  # centre
    tomas "Euh… Oh non, pourquoi moi ?"

    "La bouteille pointe Sael."

    $ showP("sael", "mefiant", 0.88)  # droite
    sael "…"

    mara "Oh putain ! Sael et Tomas !"
    mara "Allez Sael, sois gentille avec le petit puceau. Un bisou, pas une exécution !"

    scene bg_cg020 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg020")

    "Tomas est rouge écarlate. Sael reste immobile une seconde, puis se penche lentement."
    "Le baiser est très court, presque chaste, mais Sael pose une main ferme sur la nuque de Tomas pour le garder un instant."
    "Tomas tremble. Sael recule sans un mot."
    "La salle retient son souffle, puis éclate de rires et de sifflets."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showP("elen", "joie", 0.50)  # droite
    elen "Sael ! Comment t’as été douce !"

    $ showP("julian", "taquin", 0.88)  # droite
    julian "Tomas, t’es encore en vie ?"

    hide elen
    $ showP("tomas", "gene", 0.50)  # centre
    tomas "Je… je crois…"

    $ showP("mara", "ivre", 0.12)  # centre
    mara "T’as vu ? Même Sael sait embrasser. T’as pas à avoir honte, petit !"
    mara "Ah ! L'heure tourne ! On finit en apothéose !"

    "La bouteille tourne… s’arrête sur Kael."

    hide julian
    hide tomas

    $ showP("kael", "surpris", 0.50)  # centre
    kael "Moi ?"

    "La bouteille tourne une fois encore puis s'arrête..."
    "La bouteille pointe Elias."

    $ showP("elias", "jaloux", 0.88)  # droite
    elias "Euh… Moi ?"

    mara "Oh ! Kael et Elias !"
    mara "Allez les garçons, pour le beau jeu ! Un petit bisou, ça va pas vous tuer !"

    kael "Je… je sais pas si…"
    kael gene "Non vraiment..."

    elias "C’est juste un jeu, Kael."
    elias "On le fait pour l’ambiance. Pas plus. Allez."

    "Kael hésite, regarde autour de lui cherchant de l'aide du regard. Tout le monde attend, sourire aux lèvres."
    "Il hoche la tête, très lentement."

    scene bg_cg021 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg021")

    "Ils se penchent l’un vers l’autre. Le baiser est hésitant au début, puis Elias pose une main sur la nuque de Kael pour le stabiliser."
    "C’est bref, mais pas chaste. Leurs lèvres restent collées une seconde de plus que nécessaire."
    "Kael recule, rouge, troublé. Elias sourit doucement."

    elias "Pour le beau jeu…"

    kael "Ouais… pour le beau jeu."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    "La salle explose de rires et d’applaudissements. Mara siffle."

    $ showP("mara", "ivre", 0.12)  # centre
    mara "Putain, c’était mignon !"
    mara taquin "On remet ça demain ?"

    $ showP("kael", "gene", 0.50)  # centre
    kael "Par pitié, non !"

    jump _4_1_FIN_SOIREE

# Durée : 1m40
# Total : 2h 05m 40s

label _4_1_FIN_SOIREE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    "La fête s’est terminée tard. Les rires se sont éteints peu à peu."
    "Les verres sont vides. Les lumières tamisées."
    "Je marche dans les couloirs froids du Conclave. Mes pas sont lourds, un peu chancelants."
    "L’alcool me chauffe encore les veines. Ma tête tourne doucement."

    "Je pousse la porte de ma chambre. Elle se referme derrière moi avec un clic discret."
    "Je m’appuie contre le mur un instant. Le monde tangue légèrement."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je m’assois sur le lit. Mes chaussures tombent par terre sans que je les enlève vraiment."
    "Je fixe le plafond. Les veilleuses bleues clignotent doucement."

    $ blink()
    "La journée défile dans ma tête."
    "Le vote. Les cris. Le départ de Sael. La fête."
    "On a ri. On a bu. On a fait semblant que tout allait bien."
    "Mais je sens encore le poids de tout ça dans ma poitrine."

    $ blink()
    "Est-ce qu’on a vraiment gagné quelque chose ?"
    "Ou est-ce qu’on vient juste de commencer à perdre ?"

    "Je m’allonge. Les draps sont froids contre ma peau chaude."
    $ blink()

    scene bg_cg012 at adaptive_fullscreen with dissolve
    "Mes paupières sont lourdes. L’alcool fait son effet."
    "Je n’ai même pas la force de me déshabiller."

    "Le sommeil arrive vite. Brutal."
    "Comme une vague qui m’emporte."

    "Demain sera un autre jour."
    "Et je ne sais pas si j’ai envie de le voir."

    $ current_day = 5
    pause 2.0

    call end_day("5") from _call_end_day_5_1
    jump _5_1_REVEIL_CHAMBRE

# Durée : 0m35
# Total : 2h 06m 15s
