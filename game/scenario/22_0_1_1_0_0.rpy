# =============================================================================
# JOUR 22 — Route 0_1_1_0_0
# Le Conclave a été prolongé jusqu'au jour 30.
# Elias est remplacé hors champ par son Doppelgänger au cours de la journée.
# =============================================================================

default j22_elias_replaced = False
default j22_vote_announced = False

label _22_0_1_1_0_0_REVEIL:
    $ cafeteria_food_level = "null"
    $ current_day = 22
    $ day_id = 22
    $ current_period = "Matin"
    $ noam_has_juliette_drawing = False

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Quand j'ouvre les yeux, il me faut une seconde pour comprendre pourquoi mon sac est encore posé contre le bureau."

    "Hier matin, j'étais persuadé que je ne dormirais plus ici. Maintenant, le jour vingt-deux est affiché sur ma tablette et j'ai encore huit nuits à passer dans cette chambre."

    "Je reste assis au bord du lit, puis je regarde la grille d'aération. Elias a percé jusque tard hier soir ; certaines chambres sont déjà refermées, d'autres attendent encore leurs plaques de fortune."

    think "Au moins il s'en occupe."

    "Je prends un tee-shirt propre dans mon sac sans défaire le reste. Je sais pas pourquoi. Peut-être parce qu'une partie de moi refuse encore d'admettre qu'on est vraiment repartis pour plus d'une semaine."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j22_stay_door_chambre
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Dans le couloir, plusieurs sacs sont toujours près des portes. Je ne suis visiblement pas le seul à vivre à moitié prêt à partir."

    # Durée : ~1m00
    # Total : ~1m00


label _22_0_1_1_0_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est déjà presque pleine. Je prends quelque chose à manger et m'installe là où il reste de la place."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("elias", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    elen content "J'ai pris trop de pain. Enfin... je crois. Si quelqu'un en veut, servez-vous."

    mara taquin "Tu vois Noam ? Elle, au moins, elle sait s'occuper des gens. Toi tu débarques avec ta tête de mec qui a passé la nuit à se faire hanter et tu dis même pas bonjour."

    noam fatigue "Bonjour Mara."

    mara "Voilà. Beaucoup mieux."

    "Elle me regarde par-dessus sa tasse, clairement trop contente d'elle-même."

    mara taquin "Alors ? Cette nuit, ça a donné quoi ? Une autre morte dans les murs ? Une voix qui t'appelle ? Une présence froide dans ton lit ?"

    noam blase "Non."

    mara "Dommage pour la dernière. Si t'as besoin d'une présence chaude, par contre..."

    noam colere "Mara."

    mara rire "Quoi ? Je propose une solution."

    iris fatigue "T'es vraiment lourde dès le matin."

    mara taquin "Et toi t'es jalouse parce que j'ai proposé avant."

    iris colere "Rêve."

    mara "Oh, je rêve très bien toute seule."

    "Je baisse les yeux vers mon assiette en regrettant déjà d'être venu m'asseoir ici."

    noam fatigue "Vous pouvez parler d'autre chose ?"

    mara taquin "Bien sûr. On peut parler de tes fantômes."

    noam "Super."

    sael neutre "S'il en voit encore, on peut recommencer."

    "Je relève la tête vers elle."

    noam surpris "Recommencer quoi ?"

    sael raison "Le rite."

    pause 0.3

    noam panne "Non."

    mara rire "Oh putain, sa tête..."

    sael "Un peu de sel, de l'eau. Cette fois on peut faire ça plus proprement."

    noam panique "Non. Non, y'a pas de 'cette fois'. Y'a plus de fois du tout."

    "Je recule ma chaise d'un coup."

    sael "Tu paniques déjà."

    noam colere "Parce que la dernière fois Ryn m'a bloqué contre un mur pendant que tu me balançais du sel dans la figure !"

    mara taquin "Moi je dis, sans Ryn ça peut devenir beaucoup plus intime."

    noam "MARA !"

    "Elle éclate de rire."

    tomas hesitation "Je... je crois qu'on peut raisonnablement dire qu'un deuxième exorcisme n'apporterait pas grand-chose de plus au premier."

    noam "Merci. Voilà. Merci Tomas."

    sael neutre "Le premier n'a peut-être pas suffi."

    noam panique "Mais arrête de dire ça comme si on parlait d'un médicament !"

    elen inquiet "Sael, laisse-le respirer un peu..."

    sael "Je le force pas."

    noam "Tu viens de proposer de me jeter du sel dessus."

    sael "J'ai dit qu'on pouvait."

    mara taquin "Et moi j'ai proposé autre chose, mais bizarrement personne retient mes bonnes idées."

    iris blase "Parce que tes bonnes idées finissent toujours sans pantalon."

    mara rire "Pas toujours."

    iris "Mara..."

    mara "Quoi ? Il va survivre."

    "Iris souffle, puis se tourne vers moi plutôt que de continuer à la reprendre."

    iris fatigue "Bon. Assieds-toi avant de vraiment te barrer. Personne va t'exorciser pendant le petit-déj."

    noam inquiet "Après non plus."

    sael "On verra."

    noam panique "SAEL."

    "Cette fois, même Iris laisse échapper un rire."

    iris taquin "Désolée. Celle-là était un peu méritée."

    "Je finis par me rasseoir, méfiant, pendant que Mara essaie encore de reprendre son souffle."

    iris reflexion "N'empêche... y'a un truc où Noam raconte pas n'importe quoi."

    mara taquin "Oh ? Ça y est, tu prends officiellement sa défense ? C'est mignon. Je vous laisse une minute si vous voulez."

    iris blase "Continue et je te plante ta fourchette dans la main."

    mara "Donc oui."

    noam "Iris..."

    iris "Je parle de la salle. Celle derrière les conduits."

    "Elias relève la tête."

    iris "Elle existe. Et quand Noam et Mara l'ont trouvée, y'avait du matos de maintenance dedans. Du matos qui avait disparu avant, non ?"

    elias ecoute "Ouais."

    tomas reflexion "Attends... les pièces qu'on cherchait après l'incident de la maintenance ?"

    elias "Une partie, ouais."

    iris "Voilà. Je dis pas que Mara était morte, vivante, fantôme, zombie ou je sais pas quoi. Je dis juste qu'on a déjà retrouvé du matériel disparu là-bas."

    mara taquin "Moi zombie, je serais très sexy."

    noam "Tu peux vraiment pas t'en empêcher."

    mara "Non."

    "Elias ne rit pas. Il regarde son café, puis la table, comme si quelque chose venait de s'emboîter dans sa tête."

    noam reflexion "Elias ?"

    elias fatigue "Hm ?"

    noam "T'as décroché."

    elias "Nan. Je pensais aux plaques."

    iris "Celles d'hier ?"

    elias "Ouais. J'vais finir les bricolées aujourd'hui."

    "Il boit son café, pousse son plateau et se lève."

    noam "Tu veux que je vienne ?"

    elias "Laisse. J'ai besoin d'aller vite et t'as tendance à poser des questions toutes les trente secondes."

    noam taquin "Merci."

    elias fatigue "Tu sais que c'est vrai."

    iris "Et dors à un moment. T'as une tête de merde."

    elias "J'ai dormi."

    iris "Trois heures, c'est pas dormir."

    elias "Bah j'ai dormi trois heures."

    "Il récupère sa caisse à outils près de la sortie et s'éloigne."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    "Je le regarde sortir. Mara reprend presque immédiatement la conversation, comme si le trou laissé par Elias n'avait jamais existé."

    mara taquin "Bon. Maintenant qu'on a réglé les fantômes, on revient sur ma proposition de présence chaude ?"

    noam "Non."

    mara "Tu vois, Iris ? Il me brise le cœur."

    iris blase "Je vais pleurer."

    # HORS CHAMP :
    # Elias ne va pas poser les plaques de fortune.
    # L'information d'Iris lui fait penser que les plaques manquantes peuvent
    # avoir été déplacées dans la salle cachée. Il retourne seul dans les conduits,
    # tombe dans un piège des Doppelgängers et est remplacé.
    $ j22_elias_replaced = True

    $ hideGroup()

    # Durée : ~5m20
    # Total : ~6m20


label _22_0_1_1_0_0_MIDI:
    $ current_period = "Midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Après le repas, je repasse par les dortoirs. Je m'attends à entendre la perceuse d'Elias, mais le couloir est silencieux."

    "Deux plaques de fortune sont toujours appuyées contre le mur, exactement là où on les avait laissées hier."

    think "Il a dû commencer ailleurs."

    "Je ralentis devant sa chambre, puis continue. Elias passe sa vie entre la maintenance, le stockage et les couloirs ; le chercher à chaque fois qu'il disparaît serait presque un travail à plein temps."

    call show_custom_title("Un peu plus tard") from _call_show_custom_title_j22_stay_1

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Quand je reviens à la cafétéria, Elen est assise sur son sac pendant que Julian essaie de le refermer pour elle."

    $ showGroup([
        ("elen", "content", 0.24),
        ("julian", "sourire", 0.50),
        ("noam", "neutre", 0.76),
    ])

    elen "Je crois que j'ai fait une erreur."

    noam "Tu l'as ouvert."

    elen "Oui."

    julian sourire "Et maintenant nous découvrons une vérité terrible : ce sac était fermé grâce à une technologie ancienne qu'aucun de nous ne maîtrise."

    elen colere "Arrête de parler et appuie."

    julian "J'appuie."

    elen "Plus."

    julian "Je suis littéralement dessus."

    noam taquin "Vous avez besoin d'aide ?"

    elen "Oui."

    julian "Non."

    "Je m'approche quand même. À trois, on finit par fermer la fermeture éclair, et Elen récupère son sac avec un soupir de soulagement."

    elen content "Voilà. Je touche plus à rien jusqu'au départ."

    noam "Le départ est dans huit jours."

    elen "Je laverai des trucs à la main."

    julian sourire "Ça, c'est de la conviction."

    noam "Toi non plus t'as pas défait le tien ?"

    julian "Évidemment que non. Si Kami change encore d'avis demain, je veux pouvoir courir au sas avant qu'elle ait le temps de réfléchir."

    elen "Elle réfléchit plus vite que toi."

    julian "Merci Elen."

    "La discussion continue quelques minutes, juste assez pour que la journée ressemble à quelque chose de normal. Quand je repars, le silence du couloir me paraît presque plus étrange."

    $ hideGroup()

    # Durée : ~2m10
    # Total : ~8m20


label _22_0_1_1_0_0_ELIAS_REVIENT:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Je retrouve Elias un peu plus tard. Il arrive de l'autre côté du couloir avec sa caisse à outils et deux plaques de fortune sous le bras."

    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "neutre", 0.65),
    ])

    noam "Ah, t'étais là. J'allais finir par croire que t'avais démonté un mur entier."

    elias fatigue "J'ai essayé un truc. Ça marche pas."

    noam reflexion "Les plaques ?"

    elias "Ouais. Celles qu'on a bricolées hier, c'est de la merde."

    noam "Hier tu disais que ça tiendrait."

    elias "Hier je voulais que ça tienne. C'est pas pareil."

    "Il pose les deux morceaux de métal contre le mur avec un bruit sec."

    elias "J'ai forcé dessus, les attaches bougent. Le métal se tord trop. Si quelqu'un pousse vraiment derrière, ça finit par lâcher."

    noam desaccord "On peut les doubler. Tu voulais faire ça, non ?"

    elias fatigue "Ouais, mais ça règle pas les fixations. Et j'vais pas passer deux jours à foutre trois couches de métal partout pour faire semblant que c'est solide."

    noam "Même comme ça, c'est mieux que rien."

    elias "Non, parce que vous allez dormir en vous disant que c'est fermé. Moi je sais que ça l'est pas vraiment."

    "Il se frotte le front avec le dos de la main."

    elias fatigue "Franchement, j'en ai marre de bricoler autour de ce truc. On remet les grilles normales, vous bloquez avec vos meubles si vous voulez, et on attend les vraies plaques."

    noam inquiet "Quand ?"

    elias "Jour vingt-huit."

    noam surpris "Sérieux ?"

    elias "Ouais. C'est la prochaine livraison où le stock métal revient."

    noam "Donc six jours."

    elias "Je sais compter."

    noam colere "C'est pas ce que je voulais dire."

    elias "Je sais. Mais j'ai pas mieux."

    "Je regarde les plaques contre le mur. Hier encore, il était prêt à démonter la moitié de la station pour terminer."

    noam reflexion "Et celles qui ont disparu ?"

    elias fatigue "Toujours rien. J'ai revérifié vite fait, j'ai rien trouvé."

    noam "Même dans la salle dont Iris parlait ce matin ?"

    "Il me regarde une fraction de seconde."

    elias "J'y suis pas allé."

    noam "Ah."

    elias "J'ai pas envie de ramper dans vos conduits pour chercher six bouts de métal. Si quelqu'un veut le faire, grand bien lui fasse."

    "Son ton est sec, mais après la journée d'hier je peux difficilement lui reprocher d'en avoir marre."

    noam fatigue "D'accord."

    elias "Je vais enlever celles déjà posées avant que quelqu'un compte dessus pour rien."

    noam "Tu veux de l'aide ?"

    elias "Non. Et cette fois c'est pas contre toi. J'ai juste envie de finir ça tout seul et de passer à autre chose."

    noam "Ça marche."

    "Il reprend les plaques et repart."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    "Je le laisse faire. Sa décision m'agace, mais pas assez pour que j'aille me battre avec lui sur des fixations que je comprends moins bien que lui."

    think "Jour vingt-huit."

    "Je regarde ma grille un instant, puis je rentre."

    $ hideGroup()

    # Durée : ~3m20
    # Total : ~11m40


label _22_0_1_1_0_0_ANNONCE_VOTE:
    $ current_period = "Après-midi"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "En milieu d'après-midi, la cafétéria se remplit sans que personne ait vraiment organisé quoi que ce soit. Ryn et Nyra parlent encore de la prolongation, Mara embête Elen avec son dessert et Julian s'est approprié une moitié de table."

    $ showGroup([
        ("ryn", "neutre"),
        ("nyra", "neutre"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("iris", "blase"),
        ("elias", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("tomas", "reflexion"),
        ("noam", "neutre"),
    ])

    ryn "Ce qui me gonfle, c'est pas juste qu'on reste. C'est que quelqu'un a demandé ça et que depuis hier tout le monde fait comme si de rien n'était."

    nyra raison "Personne fait comme si de rien n'était. On a juste aucune preuve de qui a parlé à Kami, alors tu veux qu'on fasse quoi ? Qu'on se fouille les poches ?"

    ryn fatigue "J'en sais rien. Mais attendre neuf jours en se regardant de travers, ça va être sympa."

    mara taquin "Moi ça me va. Y'en a quelques-uns que j'aime bien regarder."

    iris blase "Évidemment."

    mara "Je t'ai pas exclue."

    iris colere "J'ai rien demandé."

    "Ryn lève les yeux au ciel. Il allait répondre quand le signal de diffusion coupe la table."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Bon ! Puisque vous avez si gentiment gagné quelques jours supplémentaires avec moi..."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Autant les rentabiliser."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le prochain amendement vient d'être tiré au sort."

    $ j22_vote_announced = True

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Et j'avoue être presque déçue."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Il propose d'ajouter un nouveau Commandement : toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui. Un toit. De l'eau. À manger."
    kami "Je vous laisse deux jours pour trouver le moyen de vous disputer là-dessus. Je crois en vous."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vote au jour vingt-quatre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    # Après une diffusion, la commande scene a effacé les sprites : réafficher
    # le groupe avant toute reprise de dialogue collectif.
    $ showGroup([
        ("ryn", "neutre"),
        ("nyra", "neutre"),
        ("sael", "neutre"),
        ("mara", "taquin"),
        ("iris", "blase"),
        ("elias", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("tomas", "reflexion"),
        ("noam", "neutre"),
    ])

    pause 0.4

    elen joie "Oh ! Bah... oui. Oui, évidemment !"

    ryn "Ouais. Là, je vois même pas ce qu'on est censés discuter."

    sael raison "Un toit, de l'eau, à manger. C'est le minimum."

    mara taquin "Le toit, je prends. L'eau... si on peut remplacer une partie par du vin, je signe tout de suite."

    iris blase "T'es vraiment incapable d'être sérieuse."

    mara "Si. Au lit, parfois."

    iris colere "Putain..."

    mara rire "Tu me tends les perches aussi."

    tomas reflexion "Il faudra quand même lire la formulation complète parce que 'alimentation suffisante', juridiquement, enfin... selon la manière dont Kami l'applique, ça peut vouloir dire plusieurs—"

    "Il s'interrompt en voyant les regards autour de la table."

    tomas hesitation "Mais le principe est évident. Oui. Je suis pour le principe."

    nyra raison "On vérifiera le texte demain. Si la formulation correspond vraiment à ce que Kami vient de lire, je vois pas de raison de bloquer."

    "Julian, jusque-là, avait le sourire de quelqu'un qui attendait précisément ce moment."

    julian joie "Enfin !"

    "Il se lève franchement cette fois, les deux mains à plat sur la table."

    julian joie "Vous vous rendez compte ? Pour une fois on a un texte que personne n'a envie d'étrangler au bout de dix secondes ! Pas de frontière, pas de piège tordu, pas de grande théorie. Un toit, de l'eau, de quoi manger. C'est tout."

    iris fatigue "Tu vas quand même réussir à en faire un spectacle."

    julian sourire "Évidemment. Tu crois vraiment que je vais laisser passer le premier vote presque consensuel du Conclave sans en profiter ?"

    "Il se tourne vers les autres avec une énergie presque ridicule, mais contagieuse."

    julian joie "On peut le faire proprement. Tous ensemble, une fois. Pas parce qu'on est coincés ici, pas parce que Kami nous regarde, juste parce que ce texte est... bah, il est évident !"

    ryn sourire "Pour une fois, je vais pas te casser ton délire. Je suis pour."

    elen joie "Moi aussi ! À fond !"

    sael "Oui."

    iris "Ouais."

    mara taquin "Je vote pour tant qu'on me garantit un toit assez grand pour recevoir."

    noam blase "Recevoir quoi ?"

    mara rire "Qui."

    noam "J'aurais pas dû demander."

    tomas hesitation "Moi je... oui. Je veux lire le texte, vraiment, mais si c'est bien ça, oui."

    julian joie "Vous voyez ?! Ça, c'est ce que je voulais depuis le début ! Une salle où, pour une fois, on part pas directement du principe qu'on va se détester."

    nyra "Ne t'emballe pas. Le vote est dans deux jours."

    julian sourire "Je m'emballe exactement autant que je veux."

    "Il attrape son téléphone et commence déjà à taper quelque chose."

    iris blase "Tu fais quoi ?"

    julian "Je prépare la campagne."

    iris "Quelle campagne ? Tout le monde vient de dire oui."

    julian rire "Et alors ? Ça veut dire que j'ai déjà un excellent départ."

    mara "Oh non, il est heureux."

    julian joie "Très."

    "Il relève son téléphone comme s'il venait de recevoir une illumination."

    julian "Il faut un slogan."

    ryn fatigue "Bien sûr."

    julian sourire "Quelque chose de simple. Quelque chose qu'on retient. 'Un toit. De l'eau. À manger.'"

    elen content "C'est pas mal !"

    julian joie "C'est parfait."

    iris "C'est littéralement le texte."

    julian "Les meilleures idées sont souvent sous nos yeux."

    "Même Ryn sourit. Julian, lui, a déjà gagné sa journée."

    "Elias n'a presque rien dit. Quand je me tourne vers lui, il hausse seulement une épaule."

    noam reflexion "T'en penses quoi ?"

    elias fatigue "Que c'est bien. Franchement, y'a quoi à ajouter ? Si les gens ont pas de toit, pas d'eau ou rien à bouffer, c'est qu'on a déjà merdé quelque part."

    noam "Ouais."

    "Il reprend sa boisson sans rien dire de plus. Personne ne demande qui avait déposé l'amendement, et le sujet ne vient pas sur la table."

    "La discussion dérive rapidement vers Julian, qui essaie déjà de convaincre Elen de l'aider à fabriquer des affiches."

    $ hideGroup()

    # Durée : ~5m30
    # Total : ~17m10


label _22_0_1_1_0_0_SOIREE:
    $ current_period = "Soir"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "En revenant au dortoir, je trouve Julian accroupi devant la porte de la salle commune avec une feuille scotchée de travers."

    "En grosses lettres : « UN TOIT. DE L'EAU. À MANGER. »"

    $ showGroup([
        ("julian", "sourire", 0.32),
        ("iris", "blase", 0.58),
        ("noam", "fatigue", 0.82),
    ])

    iris blase "C'est moche."

    julian sourire "C'est lisible."

    iris "C'est moche et lisible."

    julian "Je prends."

    noam "T'as déjà fait une affiche ?"

    julian "Deux."

    iris fatigue "Tout le monde est déjà pour."

    julian "Tout le monde a l'air pour. C'est pas pareil."

    noam reflexion "Sur ça, il a pas tort."

    iris colere "Ne l'aide pas."

    julian sourire "Merci Noam."

    noam "J'ai pas dit que j'aimais l'affiche."

    julian "Je prends aussi."

    "Iris lève les yeux au ciel et repart vers sa chambre."

    iris "Bonne nuit. Et si je trouve une troisième affiche devant ma porte, je la mange."

    julian "Ça prouvera au moins qu'elle répond au Commandement sur l'alimentation."

    iris colere "Ta gueule."

    "Elle disparaît dans le couloir."

    $ showGroup([
        ("julian", "sourire", 0.36),
        ("noam", "fatigue", 0.64),
    ])

    julian "Elle aime bien."

    noam "Bien sûr."

    julian "Tu veux m'aider à en mettre une à la cafétéria ?"

    noam "Non."

    julian "Tu peux juste tenir le ruban."

    noam "Bonne nuit, Julian."

    julian "Lâcheur."

    "Je repars avant qu'il trouve un autre poste à me confier."

    $ hideGroup()

    # Durée : ~2m00
    # Total : ~19m00


label _22_0_1_1_0_0_FIN_JOURNEE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je pousse la porte de ma chambre et regarde immédiatement la grille. La plaque de fortune a disparu ; Elias a tenu parole."

    "Je ramène donc le bureau devant l'ouverture, comme avant. Le meuble racle le sol et finit par se coincer contre le mur."

    think "Jour vingt-huit."

    "Six jours à faire ça."

    "Je m'assois sur le lit et retire mes chaussures."

    "La journée a été moins violente que les précédentes. Pas de dispute énorme, pas de nouvelle découverte impossible, même le prochain vote a l'air de mettre tout le monde d'accord."

    "Et pourtant, quelque chose me gêne encore."

    "Je repense à Elias, à son changement d'avis sur les plaques, puis je chasse l'idée. Il a passé la moitié de la veille à bricoler avec du matériel qui n'était pas prévu pour ça ; qu'il finisse par reconnaître que ça ne marche pas n'a rien d'incroyable."

    think "Arrête de chercher un problème partout."

    "Je m'allonge et tire la couverture."

    "Demain, il faudra probablement écouter Julian transformer trois lignes d'amendement en campagne nationale."

    noam fatigue "Génial..."

    "Je ferme les yeux."

    stop music fadeout 1.5

    call end_day("23", sleeping=True) from _call_j22_stay_end_day_23

    return

    # Durée : ~1m30
    # Total : ~20m30
