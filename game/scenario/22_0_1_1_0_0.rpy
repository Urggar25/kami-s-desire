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

    elen content "J'ai gardé du pain. Enfin, pas exprès pour toi, hein. J'en ai juste pris trop."

    noam "Bien sûr."

    mara taquin "Laisse-la faire, elle nourrit les gens quand elle stresse."

    elen colere "Je stresse pas."

    mara "T'as pris quatre morceaux."

    elen "J'avais faim."

    "Je souris et commence à manger. Mara me regarde une seconde de trop, puis son sourire s'élargit."

    mara taquin "Et sinon, monsieur paranormal, rien cette nuit ? Pas de femme morte dans les murs, pas de voix, pas de petit vieux translucide au pied du lit ?"

    noam fatigue "Tu vas vraiment continuer avec ça ?"

    mara "Tant que c'est drôle."

    iris agace "Donc longtemps, vu que t'as aucun critère."

    mara "Aïe."

    noam "Merci Iris."

    iris "T'emballe pas, je la défends pas. Je te défends toi, nuance."

    sael neutre "S'il voit encore des morts, on peut vérifier."

    "Je tourne la tête vers elle."

    noam surpris "Vérifier comment ?"

    sael raison "Comme l'autre fois."

    pause 0.3

    noam panne "Non."

    mara rire "Oh non..."

    sael "Un peu de sel, de l'eau, et—"

    noam panique "Non, non, non. Tu t'arrêtes là."

    "Ma chaise recule dans un bruit horrible. Mara commence déjà à rire."

    sael "Tu réagis trop."

    noam colere "La dernière fois Ryn m'a coincé contre un mur pendant que tu me balançais du sel dans la figure ! Tu veux que je réagisse comment ?"

    tomas hesitation "Pour être juste, d'un point de vue... enfin non, je vais pas rentrer là-dedans."

    noam "Merci."

    sael neutre "Tu as survécu."

    noam "C'est pas un argument !"

    mara rire "Si, un peu."

    noam colere "Mara, ferme-la."

    "Elle essaie. Elle tient deux secondes."

    mara taquin "On peut peut-être faire ça plus doucement cette fois."

    noam "JE VAIS PARTIR."

    elen surpris "Mais t'as même pas fini de manger."

    noam "Je préfère mourir de faim."

    iris colere "Bon, ça suffit. Vous allez le laisser tranquille avant qu'il se mette vraiment à courir."

    sael "Je proposais juste."

    iris "Bah propose autre chose. Un café. Une promenade. Je sais pas, un truc qui implique pas de lui jeter des trucs à la gueule."

    "Sael hausse les épaules et reprend son repas comme si la conversation était terminée."

    noam fatigue "Merci."

    iris "Ouais, bon. Profite pas trop du moment."

    "Mara essuie ses yeux du bout des doigts, encore hilare."

    mara taquin "Désolée... non, en vrai, pas désolée."

    noam blase "J'avais compris."

    "La table se calme enfin. Je reprends mon assiette et Iris remue son café, toujours agacée."

    iris reflexion "N'empêche..."

    noam "Quoi ?"

    iris "Je dis pas que t'as vu un fantôme, hein. Je veux que ce soit très clair."

    noam "Ça commence bien."

    iris "Mais la salle, elle, elle existe."

    "Elias, qui n'écoutait jusque-là qu'à moitié, relève la tête."

    iris "Et dans cette salle, vous aviez trouvé du matos de maintenance, non ? Des trucs qui avaient disparu avant."

    noam reflexion "Ouais. Enfin... il y avait des outils, des pièces, des trucs rangés là-bas. Elias avait déjà remarqué que du matériel manquait."

    elias ecoute "Ouais."

    tomas reflexion "C'était avant qu'on découvre le réseau ?"

    elias "Ouais, quelques jours avant."

    iris "Donc voilà. Je dis juste que tout ce qu'il raconte est pas forcément sorti de son cul."

    mara taquin "Quelle déclaration de confiance."

    iris colere "Tu veux que je retire ?"

    mara "Non, non."

    noam "Je prends."

    "Je m'attends à ce qu'Elias ajoute quelque chose, mais il reste silencieux. Il regarde son plateau, puis la table, puis rien de précis."

    noam reflexion "Elias ?"

    elias fatigue "Hm ?"

    noam "Ça va ?"

    elias "Ouais. Je pensais aux plaques."

    iris "Celles d'hier ?"

    elias "Ouais. J'vais finir les bricolées aujourd'hui."

    "Il boit le reste de son café d'un trait et repousse son plateau."

    noam "Tu veux que je vienne ?"

    elias "Nan, laisse. J'ai déjà assez de trucs à déplacer, si je dois en plus t'expliquer où tenir ça va me saouler."

    noam taquin "Charmant."

    elias fatigue "Tu vois ce que je veux dire."

    noam "Ouais."

    "Il récupère sa caisse à outils près de la sortie."

    iris "Dors un peu à un moment, quand même."

    elias "J'ai dormi."

    iris "Trois heures, c'est pas dormir."

    elias "Ça compte."

    "Il s'éloigne avant qu'elle puisse répondre."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    "Je le regarde sortir, puis la conversation repart sur autre chose."

    # HORS CHAMP :
    # Elias ne va pas poser les plaques de fortune.
    # L'information d'Iris lui fait penser que les plaques manquantes peuvent
    # avoir été déplacées dans la salle cachée. Il retourne seul dans les conduits,
    # tombe dans un piège des Doppelgängers et est remplacé.
    $ j22_elias_replaced = True

    $ hideGroup()

    # Durée : ~5m10
    # Total : ~6m10


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

    "En milieu d'après-midi, la cafétéria se remplit sans que personne ait vraiment organisé quoi que ce soit. Certains boivent, d'autres traînent, Ryn et Nyra parlent encore à voix basse de la prolongation."

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

    ryn "Moi je dis juste que quelqu'un a parlé à Kami et que personne assume. Ça me gonfle."

    nyra raison "Et je te dis juste qu'on n'a rien de plus qu'hier. Si tu recommences à demander à tout le monde, tu vas juste foutre une ambiance encore pire."

    ryn fatigue "L'ambiance est déjà pourrie."

    mara taquin "Pas partout."

    iris "Mara, non."

    mara "J'ai rien dit."

    iris "Justement, je préfère prévenir."

    "Ryn souffle et laisse tomber. Tomas allait dire quelque chose quand le signal de diffusion coupe toutes les conversations."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Bon ! Puisque vous avez gagné quelques jours supplémentaires avec moi..."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Autant les rentabiliser."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le prochain amendement vient d'être tiré au sort."

    $ j22_vote_announced = True

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Et j'avoue être presque déçue."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Ajouter un Sixième Commandement : toute personne doit pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui. Un toit. De l'eau. À manger."
    kami "Je vous laisse deux jours pour découvrir comment réussir à vous disputer là-dessus."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vote au jour vingt-quatre."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    pause 0.4

    iris blase "Bah... oui."

    ryn "Ouais."

    elen content "Pour une fois, c'est simple !"

    sael "Les gens doivent manger. Je vois pas ce qu'il y a à discuter."

    mara taquin "On peut peut-être débattre de l'eau. Perso je préfère le vin."

    iris colere "Mara."

    mara "Ça va, ça va."

    tomas reflexion "Il y aura peut-être des détails sur la définition de 'suffisante', sur l'obligation concrète de fournir—"

    "Il voit plusieurs regards se tourner vers lui et s'arrête."

    tomas hesitation "Mais oui. Sur le principe... oui."

    nyra raison "On regardera la formulation exacte. À première vue, je vois rien de bloquant."

    julian sourire "Parfait."

    iris fatigue "Pourquoi j'aime pas quand tu dis ça ?"

    julian "Parce que tu me connais mal."

    iris "Non, justement."

    "Julian se redresse déjà. Pas complètement debout, mais assez pour qu'on comprenne qu'il va faire un discours."

    ryn fatigue "Julian..."

    julian "Attends, deux secondes. Je vais pas vous faire vingt minutes."

    mara "Cinq ?"

    julian "Une."

    iris "Trente secondes."

    julian sourire "Marché conclu."

    "Il pose les mains sur la table."

    julian "On vient de passer trois semaines à se déchirer sur des trucs où, à chaque fois, quelqu'un avait une bonne raison de dire non. Là, franchement... je vois pas."

    "Il cherche ses mots une seconde, moins théâtral que d'habitude."

    julian "Un toit, de l'eau, de quoi bouffer. C'est pas glorieux, c'est même pas très original. Mais justement. Si on arrive pas à se mettre d'accord là-dessus, autant arrêter tout de suite."

    elen joie "Moi je suis pour."

    ryn "Moi aussi."

    sael "Oui."

    iris "Pareil."

    mara "Je vais faire un effort énorme et ne pas trouver de problème."

    tomas "Je veux juste lire le texte complet avant de dire oui définitivement, mais... ouais. Enfin, probablement oui."

    julian sourire "Voilà. Vous voyez ?"

    iris blase "T'avais besoin de te lever à moitié pour ça ?"

    julian "Oui."

    "Quelques rires passent autour de la table."

    noam reflexion "Elias ?"

    elias neutre "Quoi ?"

    noam "T'en penses quoi ?"

    elias "C'est bien."

    julian sourire "C'est tout ?"

    elias fatigue "Bah ouais. Les gens ont un toit, ils bouffent, ils boivent. J'vais pas faire un discours."

    julian "C'est pour ça que je suis là."

    elias colere "Justement."

    "Julian sourit, prêt à repartir, mais Elias le coupe avant."

    elias fatigue "Et... c'était moi."

    "Cette fois, tout le monde se tourne vers lui."

    elen surpris "Quoi ?"

    elias "L'amendement. Celui que j'avais mis dans l'urne au début."

    tomas surpris "Ah."

    julian sourire "Alors là..."

    elias colere "Non. Je vois déjà ta tête, non."

    julian "Mais attends, c'est parfait ! Tu proposes le truc le plus simple et le plus humain du lot et tu dis ça comme si t'avais demandé qu'on change une ampoule."

    elias fatigue "Parce que j'ai pas envie qu'on me fasse une médaille. J'ai écrit trois lignes, c'est tout."

    julian sourire "Trois très bonnes lignes."

    elias "Julian..."

    julian "D'accord, d'accord. J'arrête."

    pause 0.3

    julian sourire "Mais je vais quand même faire campagne."

    elias colere "Évidemment."

    mara rire "Il tiendra jamais trente secondes."

    iris "Personne y croyait."

    "Le sujet pourrait presque s'arrêter là. Personne ne semble vraiment opposé au texte, et pour une fois le débat se vide avant même d'avoir commencé."

    "Julian, lui, a déjà sorti son téléphone pour noter quelque chose."

    $ hideGroup()

    # Durée : ~5m20
    # Total : ~17m00


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
