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

    "Quand j'ouvre les yeux, mon sac est toujours posé contre le bureau."

    "Je le fixe quelques secondes avant de me rappeler pourquoi il est encore là."

    think "Jour vingt-deux."

    "Hier matin, j'étais persuadé que je dormirais sur Terre ce soir."

    "À la place, j'ai neuf jours de plus ici."

    "Je passe une main sur mon visage, puis je regarde machinalement vers la grille."

    "Elias a travaillé tard. Je l'ai entendu percer bien après être revenu dans ma chambre."

    "Je me lève, attrape un tee-shirt propre dans mon sac sans prendre la peine de le défaire complètement, puis je sors."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j22_stay_door_chambre
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Dans le couloir, plusieurs sacs sont encore posés près des portes."

    "Personne n'a vraiment repris possession de sa chambre."

    "On dirait qu'on attend tous que Kami change encore d'avis."

    # Durée : ~1m00
    # Total : ~1m00


label _22_0_1_1_0_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est déjà bien remplie quand j'arrive."

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

    elen content "Noam ! Y'a encore du pain."

    noam "C'est devenu ton argument principal pour me faire venir manger ?"

    elen joie "Ça marche."

    julian sourire "Il faut reconnaître qu'elle connaît son public."

    "Je m'assois en bout de table."

    mara taquin "Alors ?"

    noam "Alors quoi ?"

    mara "Bien dormi ?"

    noam "À peu près."

    mara rire "Pas de dame morte qui t'a parlé depuis le mur ?"

    "Je m'arrête avec ma tasse à mi-chemin."

    noam fatigue "Mara..."

    mara taquin "Quoi ? Je demande."

    iris agace "Tu peux le laisser tranquille cinq minutes ?"

    mara "Mais je suis gentille."

    iris "C'est ça le pire."

    mara rire "Oh ça va. Il sait que je déconne."

    noam blase "À force, je vais finir par préférer les fantômes."

    mara taquin "Ah ! Donc tu reconnais qu'il y en a."

    noam colere "J'ai pas dit ça."

    sael neutre "S'il en voit encore, on peut recommencer."

    pause 0.3

    noam surpris "Recommencer quoi ?"

    "Sael prend tranquillement un morceau de pain."

    sael raison "Le sel."

    noam panne "..."

    mara "Oh putain."

    sael "Et l'eau."

    noam panique "Non."

    elen surpris "Sael..."

    sael neutre "La première fois n'a peut-être pas suffi."

    noam panique "NON."

    "Je recule tellement vite que le pied de ma chaise racle le sol."

    mara rire "Regardez sa tête !"

    noam colere "C'EST PAS DRÔLE !"

    sael "Je peux préparer ça après manger."

    noam panique "Tu prépares RIEN DU TOUT !"

    tomas hesitation "Techniquement, un deuxième exorcisme ne démontrerait pas plus—"

    noam colere "TOMAS, PAS TOI !"

    tomas surpris "Je disais justement que ça servait à rien."

    noam "Alors commence par ça !"

    "Mara est pliée sur la table."

    mara rire "J'en peux plus..."

    noam colere "Je te déteste."

    mara taquin "Mais non."

    sael neutre "Tu as peur pour rien."

    noam panique "La dernière fois Ryn m'a plaqué contre un mur pendant que tu me jetais du sel dans la gueule !"

    sael "Tu as survécu."

    noam "C'EST PAS LE SUJET !"

    "Iris pose brutalement sa tasse."

    iris colere "Bon, ça suffit."

    mara "Oh non."

    iris "Si."

    "Elle regarde Sael."

    iris colere "Tu le touches pas."

    sael reflexion "Je proposais."

    iris "Bah propose autre chose."

    mara taquin "Un massage, peut-être ?"

    iris colere "Mara."

    mara "Je mange."

    "Elle prend immédiatement une bouchée, toujours avec son sourire."

    iris fatigue "Et puis, pour une fois, y'a un truc concret dans son histoire."

    noam surpris "Hein ?"

    iris "La salle."

    "Elias relève légèrement la tête."

    iris reflexion "Celle derrière les conduits. Avec les Goumi."

    elias ecoute "Quoi, la salle ?"

    iris "Quand vous l'avez trouvée, y'avait pas du matériel de maintenance dedans ?"

    noam reflexion "Si."

    iris "Du matériel qui avait disparu quelques jours avant."

    tomas surpris "Attends, c'était bien le même ?"

    noam "Je crois. Enfin... Elias avait dit qu'il manquait des trucs à la maintenance, et dans cette salle y'avait des pièces et des outils."

    elias fatigue "Ouais."

    "Il ne dit rien d'autre."

    iris "Donc son histoire de fantôme, j'en sais rien."

    mara taquin "Merci pour la nuance."

    iris colere "Mais la pièce existe. Et du matos qui disparaît puis qui se retrouve là-bas, ça existe aussi."

    noam "Merci."

    iris fatigue "T'emballe pas. Je te défends pas sur le cadavre."

    noam blase "Évidemment."

    sael "Le sel reste une option."

    noam colere "NON."

    "Mara repart dans un fou rire."

    "À côté, Elias regarde son assiette sans vraiment manger."

    "Il finit par reprendre sa tasse, mais son regard reste ailleurs."

    elias ecoute "..."

    julian sourire "Bon. Je crois qu'on vient de trouver le seul sujet capable de faire oublier qu'on est coincés ici neuf jours de plus."

    elen "C'est déjà ça ?"

    iris blase "Non."

    elen "J'essayais."

    "La conversation part sur autre chose, mais Elias ne revient presque pas dedans."

    $ showGroup([
        ("mara", "taquin"),
        ("sael", "neutre"),
        ("iris", "fatigue"),
        ("tomas", "neutre"),
        ("elen", "content"),
        ("julian", "sourire"),
        ("noam", "fatigue"),
    ])

    "Au bout de quelques minutes, Elias se lève avec son plateau."

    noam "Tu vas où ?"

    elias fatigue "Finir les plaques."

    noam "Tu veux un coup de main ?"

    elias "Nan. Mange."

    iris "T'as dormi au moins ?"

    elias "Un peu."

    iris blase "Ça veut dire non."

    elias "Ça veut dire un peu."

    "Il récupère sa caisse à outils près de la porte."

    elias "Je vais voir ce que je peux encore sauver de mes trucs d'hier."

    noam "Tu m'appelles si t'as besoin."

    elias "Ouais."

    "Il sort."

    # HORS CHAMP — Elias ne va pas installer les plaques de fortune.
    # L'information donnée par Iris lui fait penser que les vraies plaques
    # pourraient se trouver dans la salle cachée derrière les conduits.
    # Il s'y rend seul, tombe dans un piège des Doppelgängers et est remplacé.
    $ j22_elias_replaced = True

    $ hideGroup()

    # Durée : ~5m00
    # Total : ~6m00


label _22_0_1_1_0_0_APRES_REPAS:
    $ current_period = "Midi"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Après le repas, je retourne au dortoir."

    "Je m'attends presque à entendre la perceuse avant même d'ouvrir la porte du couloir."

    "Rien."

    think "Il a peut-être commencé ailleurs."

    "Je passe devant la chambre d'Elias. Porte fermée."

    "Plus loin, deux plaques de fortune sont posées contre le mur exactement là où on les avait laissées hier."

    noam reflexion "..."

    "Je m'arrête une seconde."

    think "Il a dit qu'il allait finir."

    "Je pourrais aller le chercher."

    "Puis je me rappelle sa tête au petit-déjeuner, ses trois heures de sommeil probablement imaginaires et sa manière de répondre dès qu'on essaie de l'aider."

    think "Il doit être à la maintenance."

    "Je continue."

    call show_custom_title("Un peu plus tard") from _call_show_custom_title_j22_stay_1

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Je retombe sur Elen et Julian à la cafétéria."

    $ showGroup([
        ("elen", "content", 0.22),
        ("julian", "sourire", 0.50),
        ("noam", "neutre", 0.78),
    ])

    elen content "On déballe nos sacs ou pas ?"

    noam "Pourquoi tu me demandes ça à moi ?"

    elen "Parce que j'arrive pas à décider."

    julian sourire "Personnellement, j'ai choisi une solution d'une grande élégance."

    noam "Laquelle ?"

    julian "Ne rien toucher."

    elen "C'est pas une solution."

    julian "Si je laisse tout prêt, je peux partir en trente secondes."

    noam "Kami vient de nous rajouter neuf jours."

    julian "Justement. J'essaie de lui laisser le moins de temps possible pour changer encore d'avis."

    elen "Moi j'ai besoin de mes vêtements."

    julian "Voilà le défaut de mon système."

    noam taquin "Tu peux aussi porter les mêmes neuf jours."

    julian surpris "Noam."

    noam "Quoi ?"

    julian "J'ai une dignité."

    elen rire "T'as surtout beaucoup trop de chemises."

    julian "C'est la même chose."

    "Je souris malgré moi."

    "Pendant quelques minutes, on parle seulement de sacs, de vêtements et de ce qu'on fera si la navette revient finalement avant le jour trente."

    "Ça ne règle rien."

    "Mais ça ressemble à une conversation normale."

    $ hideGroup()

    # Durée : ~2m10
    # Total : ~8m10


label _22_0_1_1_0_0_ELIAS_REVIENT:
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Quand je repars vers ma chambre, j'entends enfin des pas dans le couloir."

    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "neutre", 0.65),
    ])

    "Elias arrive avec sa caisse à outils."

    "Il a l'air crevé. Rien de nouveau."

    noam "Ah, t'étais où ?"

    elias fatigue "Maintenance."

    noam "J'ai cru que t'avais commencé les plaques."

    elias "Justement."

    "Il pose sa caisse par terre."

    elias ecoute "Ça va pas."

    noam reflexion "Quoi ?"

    elias "Les plaques de fortune."

    noam "Qu'est-ce qu'elles ont ?"

    elias fatigue "Elles tiennent pas assez."

    noam "Hier tu disais que ça tiendrait."

    elias "Ouais bah hier j'avais pas fini de tester."

    noam "Tester comment ?"

    elias colere "En tirant dessus, Noam."

    noam "D'accord."

    elias fatigue "Le métal est trop fin. Les attaches prennent mal. Si quelqu'un force vraiment, ça saute."

    noam reflexion "On peut les doubler comme tu voulais."

    elias "Non."

    noam "Pourquoi ?"

    elias "Parce que ça va juste me faire perdre du temps pour un truc de merde."

    "Il se penche et attrape une des plaques appuyées contre le mur."

    noam "Tu fais quoi ?"

    elias "Je les vire."

    noam surpris "Toutes ?"

    elias "Ouais."

    noam "Attends, même celles déjà posées ?"

    elias fatigue "Surtout celles déjà posées."

    noam desaccord "Mais elles sont mieux que rien."

    elias "Pas si tu crois que t'es protégé alors que ça tient à moitié."

    noam "Elias..."

    elias colere "Tu veux que je te dise quoi ? Que c'est bon parce que ça te rassure ?"

    "Je me tais."

    elias fatigue "J'ai fait avec ce que j'avais. Ça marche pas. Fin."

    noam reflexion "Et les vraies plaques ?"

    "Il hausse une épaule."

    elias "Y'en aura pas avant le jour vingt-huit."

    noam surpris "Le vingt-huit ?"

    elias "Prochaine livraison avec le stock métal."

    noam colere "Donc on laisse les grilles comme ça six jours ?"

    elias "On remet les grilles normales. On bloque les meubles devant si ça vous rassure."

    noam "Ça me rassure pas."

    elias fatigue "Je sais."

    "Il récupère la deuxième plaque."

    noam "T'as revérifié la livraison d'hier ?"

    elias "Ouais."

    noam "Et ?"

    elias "Rien."

    noam "Rien quoi ?"

    elias colere "Rien, Noam. Elles sont pas là."

    "Son ton me coupe."

    "Je lève légèrement les mains."

    noam "D'accord."

    elias fatigue "J'en ai marre de passer ma journée dessus."

    noam "Je comprends."

    elias "Cool."

    "Il repart avec les deux plaques."

    $ showGroup([
        ("noam", "neutre", 0.50),
    ])

    "Je le regarde disparaître au bout du couloir."

    "Ça m'agace, mais son raisonnement se tient assez pour que je ne trouve rien à répondre."

    think "Jour vingt-huit."

    "Six nuits."

    "Je regarde ma propre grille."

    think "Génial."

    $ hideGroup()

    # Durée : ~3m10
    # Total : ~11m20


label _22_0_1_1_0_0_ANNONCE_VOTE:
    $ current_period = "Après-midi"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "En milieu d'après-midi, presque tout le monde finit par se retrouver à la cafétéria."

    "Pas pour une réunion. Juste parce qu'on n'a pas grand-chose d'autre à faire."

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

    ryn "Alors, on fait quoi maintenant ?"

    nyra "Aujourd'hui ? Rien."

    mara taquin "Excellente journée."

    iris blase "Tu dis ça parce que t'as déjà décidé de rien foutre."

    mara "Je suis cohérente."

    tomas reflexion "Il reste quand même la question de la prolongation."

    ryn colere "Ouais."

    elen inquiet "On va recommencer avec ça ?"

    ryn "Non. Enfin... pas maintenant."

    julian sourire "Quelle retenue. Je suis impressionné."

    ryn "Commence pas."

    julian "Je n'ai rien dit."

    ryn "C'est ton ton."

    "Julian ouvre les mains, faussement innocent."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Puisque vous avez finalement décidé de rester encore un peu avec moi..."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Il serait tout de même dommage de ne pas profiter de ces merveilleux jours supplémentaires !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il est donc temps de reprendre les choses sérieuses."

    pause 0.4

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Votre prochain amendement vient d'être tiré au sort."

    $ j22_vote_announced = True

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Et celui-ci propose quelque chose de presque indécemment raisonnable."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Ajouter un Sixième Commandement."

    pause 0.3

    kami "Toute personne devra pouvoir disposer d'un toit où dormir, d'eau potable et d'une alimentation suffisante."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui, je sais."
    kami "Un toit. De l'eau. À manger."
    kami "À ce rythme-là, vous allez finir par demander qu'on soit gentils les uns avec les autres."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu au jour vingt-quatre."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vous avez donc deux jours pour découvrir si quelqu'un ici est secrètement opposé au concept de boire de l'eau."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    pause 0.4

    iris blase "Bon."

    ryn "Bah... oui."

    elen content "Moi je trouve ça bien."

    sael neutre "Évidemment."

    mara taquin "Je sais pas. L'eau, c'est dangereux. On peut se noyer."

    iris colere "Mara."

    mara "Je plaisante."

    tomas reflexion "La formulation exacte va compter un peu. 'Suffisante', par exemple, ça veut dire—"

    iris "Tomas."

    tomas hesitation "Oui. Non. D'accord."

    nyra raison "On pourra demander le texte précis demain. Sur le principe, je vois pas vraiment ce qui poserait problème."

    ryn "Moi non plus."

    elen joie "Pour une fois !"

    julian sourire "Mes amis..."

    iris fatigue "Oh non."

    julian "Quoi, oh non ?"

    iris "Je connais cette voix."

    mara "Moi aussi."

    julian sourire "Vous n'allez quand même pas me reprocher d'être ému."

    iris "Si."

    julian "Nous avons peut-être enfin devant nous une proposition qui peut réunir tout le monde."

    ryn fatigue "Julian..."

    julian "Non, attendez."

    "Il se lève."

    iris blase "Évidemment."

    julian sourire "Depuis trois semaines, nous nous déchirons pour des frontières, des organisations, des archives, des règles que personne n'arrive à lire sans prendre une aspirine."

    tomas "C'est pas exactement—"

    julian "Tomas, je t'adore, mais laisse-moi trente secondes."

    tomas surpris "D'accord."

    julian "Là, on nous demande quelque chose de simple."

    "Il écarte les bras."

    julian "Est-ce que quelqu'un devrait dormir dehors ? Non."
    julian "Est-ce que quelqu'un devrait avoir faim ? Non."
    julian "Est-ce que quelqu'un devrait avoir soif ?"

    mara taquin "Ça dépend de ce qu'il boit."

    julian colere "Mara."

    mara "Pardon."

    julian sourire "Non."

    "Il reprend son souffle."

    julian "Alors pour une fois, juste une fois, on pourrait peut-être arrêter de chercher pourquoi ça va mal tourner et faire passer quelque chose ensemble."

    elen joie "Oui !"

    iris "T'avais vraiment besoin de te lever pour dire ça ?"

    julian "Absolument."

    ryn sourire "Sur le fond, il a pas tort."

    nyra "Non."

    sael raison "S'il faut deux jours pour décider que les gens doivent boire, on mérite peut-être de rester jusqu'au jour trente."

    "Un rire traverse la table."

    noam taquin "Ça, je pense qu'on peut l'utiliser comme slogan."

    julian sourire "Très bien. Je prends."

    iris "Tu prends rien du tout."

    julian "Trop tard."

    "Elias, lui, n'a presque rien dit depuis l'annonce."

    noam reflexion "T'en penses quoi ?"

    elias neutre "C'est bien."

    noam "C'est tout ?"

    elias "Tu veux quoi de plus ?"

    noam "Je sais pas. T'es normalement plus bavard quand ça parle de trucs concrets."

    elias fatigue "Bah... les gens bouffent, boivent, dorment sous un toit. Ouais. Ça me va."

    julian sourire "Voilà !"

    elias colere "Commence pas."

    julian "Je voulais juste—"

    elias "J'ai compris."

    "Julian s'arrête, puis sourit quand même."

    julian "Très bien."

    pause 0.3

    elias neutre "C'était moi."

    noam surpris "Quoi ?"

    elias "La proposition."

    tomas surpris "Tu l'avais déposée ?"

    elias "Ouais."

    "Plusieurs regards se tournent vers lui."

    elias fatigue "J'avais pas écrit un roman. J'avais juste mis qu'un type devrait toujours avoir un toit, de l'eau et de quoi manger."

    elen content "C'est toi ?"

    elias "Ouais."

    julian sourire "Elias."

    elias colere "Non."

    julian "Je n'ai encore rien dit."

    elias "Je te vois venir."

    julian "C'est une très belle proposition."

    elias fatigue "Merci."

    julian "Sobre. Forte. Universelle."

    elias colere "Voilà. Ça y est."

    mara rire "Il va te faire une campagne."

    julian sourire "Évidemment que je vais lui faire une campagne."

    elias "J'ai rien demandé."

    julian "Justement. Laisse faire les professionnels."

    iris blase "Professionnel de quoi ?"

    julian "De l'enthousiasme."

    iris "Ça existe pas."

    julian "Maintenant si."

    "Elias secoue la tête."

    elias fatigue "Faites ce que vous voulez. Tant que vous votez pour."

    julian sourire "Tu vois ? Même son slogan est parfait."

    elias colere "C'était pas un slogan."

    "Le débat n'avance pas vraiment plus loin."

    "Pour une fois, personne ne semble chercher un angle mort avant même d'avoir compris la proposition."

    "Julian, lui, a déjà décidé qu'il allait transformer ça en événement."

    $ hideGroup()

    # Durée : ~6m00
    # Total : ~17m20


label _22_0_1_1_0_0_SOIREE:
    $ current_period = "Soir"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "En revenant au dortoir, je découvre que Julian a déjà commencé."

    "Un papier est scotché de travers sur la porte de la salle commune."

    "En grosses lettres :"

    "UN TOIT. DE L'EAU. À MANGER."

    pause 0.3

    noam blase "..."

    $ showGroup([
        ("julian", "sourire", 0.34),
        ("iris", "blase", 0.66),
    ])

    julian sourire "Simple. Efficace. Mémorable."

    iris blase "Moche."

    julian "Minimaliste."

    iris "Moche."

    julian "Tu manques de vision."

    iris "Et toi de honte."

    noam "Tu l'as fait avec quoi ?"

    julian "Le dos d'un ancien formulaire."

    iris "Donc en plus c'est du recyclage."

    julian sourire "Tu vois ? Cette campagne est déjà exemplaire."

    noam "Il reste deux jours."

    julian "Justement. Deux jours, c'est court."

    iris "Pour convaincre qui ? Tout le monde est déjà pour."

    julian "On n'en sait rien."

    iris "Personne a protesté."

    julian "Le silence n'est pas un vote."

    noam reflexion "Là-dessus, il a raison."

    iris "Ne l'encourage pas."

    julian sourire "Merci Noam."

    noam "J'ai pas dit que ton affiche était bien."

    julian "Chaque soutien commence quelque part."

    "Iris arrache presque le papier, puis se retient."

    iris fatigue "Je vais me coucher avant de faire quelque chose d'illégal."

    julian "Bonne nuit !"

    iris colere "Ta gueule."

    "Elle s'éloigne."

    $ showGroup([
        ("julian", "sourire", 0.34),
        ("noam", "fatigue", 0.66),
    ])

    julian "Elle adore."

    noam "Bien sûr."

    julian "Tu veux m'aider à en faire deux autres ?"

    noam "Non."

    julian "Une ?"

    noam "Non."

    julian "Tenir le papier ?"

    noam "Bonne nuit Julian."

    julian "Lâcheur."

    "Je souris et reprends le couloir."

    $ hideGroup()

    # Durée : ~2m10
    # Total : ~19m30


label _22_0_1_1_0_0_FIN_JOURNEE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je ferme la porte derrière moi."

    "La première chose que je vois, c'est la grille."

    "Pas de plaque."

    "Le bureau est toujours assez proche pour que je puisse le pousser devant."

    "Je le fais."

    "Ça grince sur le sol."

    think "Jour vingt-huit."

    "Je déteste déjà cette date."

    "Je m'assois sur le lit."

    "Au moins, le prochain vote ne devrait pas nous déchirer."

    "Un toit. De l'eau. À manger."

    "Même Julian devrait réussir à ne pas compliquer ça."

    pause 0.4

    think "Enfin."

    "Je regarde son affiche pliée qu'il a réussi à me glisser dans la main avant que je parte."

    noam blase "..."

    "Je la pose sur le bureau."

    "Puis je regarde encore une fois la grille."

    "Je repense vaguement à Elias."

    "À sa façon de dire que les plaques ne tenaient pas."

    "À son énervement."

    "Rien d'assez bizarre pour en faire quoi que ce soit."

    "Juste une journée de plus dans un endroit où tout finit toujours par devenir compliqué."

    stop music fadeout 1.5

    call end_day("23") from _call_j22_stay_end_day_23

    return

    # Durée : ~1m30
    # Total : ~21m00
