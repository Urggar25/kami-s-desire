# -----------------------------------------------------------------------
# LIENS — ELEN
# -----------------------------------------------------------------------

default elen_link = 0


label ELEN_LINK_INTERACT:

    menu:
        "Passer du temps avec Elen ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if elen_link == 0:
        jump elen_link_1
    elif elen_link == 1:
        jump elen_link_2
    elif elen_link == 2:
        jump elen_link_3
    elif elen_link == 3:
        jump elen_link_4
    elif elen_link == 4:
        jump elen_link_5

    if last_room_label:
        jump expression last_room_label
    return


label elen_link_1:

    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("elen", "joie", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Elen est accroupie au milieu de l'immense salle du Conclave."

    elen joie "Noam ! Viens voir, vite, vite, vite !"
    noam "Qu'est-ce qu'il y a ?"

    elen surpris "Regarde la rainure ici."
    elen reflechit "Le trait dans le métal."
    elen joie "On dirait une rivière miniature !"

    "Je m'approche."
    "C'est juste une jointure entre deux plaques."

    noam "Tu parles de ça ?"

    elen rire "Oui !"
    elen joie "Tu vois comment la lumière glisse dedans ?"
    elen content "On dirait que le Conclave respire quand on bouge la tête."

    "Elle se décale de quelques centimètres pour me montrer l'angle exact."

    play sound sfx_bip

    elen surpris "Là !"
    elen joie "Tu l'as vu ?"

    noam "Un petit reflet, oui."

    elen content "Pas un petit reflet."
    elen joie "Un reflet courageux."
    elen rire "Il survit à tous ces néons horribles."

    "Son enthousiasme est tellement sincère que je me surprends à regarder encore."

    noam "Tu t'extasies sur une rainure de sol."

    elen taquin "Exactement."
    elen reflechit "Attends, c'est encore mieux ici."

    "Elle me prend la manche et m'entraîne de deux pas vers la droite."

    elen joie "Tu vois ?"
    elen surpris "Maintenant la ligne rejoint l'ombre du pupitre."
    elen content "On dirait une carte vers un trésor."

    noam "Un trésor ?"

    elen rire "Oui."
    elen joie "Le trésor de l'instant précis où on décide de regarder."

    "Elle tend l'index comme une guide de musée improvisée."

    elen content "Ici, t'as une poussière coincée dans la fente."
    elen taquin "Donc techniquement, je viens de découvrir l'espace."

    noam "Tu fais des raccourcis impressionnants."

    elen rire "Merci !"
    elen content "Je préfère les raccourcis qui finissent en émerveillement."

    "Un bourdonnement grave traverse la salle."
    "Les écrans autour de nous continuent leur cycle."

    elen reflechit "Écoute ça aussi."
    elen joie "On dirait un orgue géant qui a appris à chuchoter."

    noam "Moi, j'entends surtout des machines."

    elen content "Oui, mais des machines qui font de leur mieux."
    elen joie "Tu crois qu'elles sont contentes quand on les remarque ?"

    noam "Je ne suis pas sûr qu'elles aient un avis."

    elen taquin "Alors je vais en avoir un pour elles."
    elen joie "Je déclare officiellement cette rainure adorable."

    "Elle tape dans ses mains, ravie de sa propre proclamation."

    play sound sfx_clap

    elen joie "Tu sais quoi ?"
    elen content "On devrait donner des noms aux détails oubliés."
    elen reflechit "Celui-là, c'est... Fil d'Argent."

    noam "Fil d'Argent ?"

    elen rire "Oui !"
    elen joie "Parce qu'il relie des trucs sans faire de bruit."

    "Je la regarde sourire au sol comme à un vieil ami."

    noam "Tu rends tout plus simple."

    elen content "Pas plus simple."
    elen joie "Plus vivant."
    elen taquin "C'est ma spécialité."

    "Elle se relève enfin, mais garde les yeux brillants."

    elen joie "Promis, la prochaine fois je te montre une vis exceptionnelle."

    noam "J'ai hâte, étrangement."

    elen content "Parfait."
    elen joie "Mission accomplie, partenaire d'émerveillement."

    "Elle me fait un petit salut solennel, puis éclate de rire."

    $ elen_link = 1

    jump FREE_TIME_END


label elen_link_2:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("elen", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Elen remue une boisson trop sucrée avec une concentration héroïque."
    "Autour, le groupe débat de quelqu'un absent avec une sévérité croissante."

    noam "Ils y vont fort."

    elen reflechit "Oui."
    elen triste "Et c'est injuste."

    noam "Tu le connais à peine."

    elen desaccord "Ça suffit pour voir qu'il est fatigué."
    elen inquiet "Quand les gens sont fatigués, ils disent des horreurs qu'ils ne pensent pas toujours."

    "Elle tourne sa cuillère encore trois fois, puis la pose."

    play sound sfx_tasse

    elen content "Je crois pas aux monstres définitifs."
    elen reflechit "Je crois aux gens coincés dans un mauvais moment."

    noam "Même quand ils blessent les autres ?"

    elen triste "Surtout là."
    elen inquiet "Sinon on les abandonne pile au moment où ils sont les pires versions d'eux-mêmes."

    "Elle lisse la serviette en papier devant elle, geste doux et nerveux à la fois."

    elen neutre "Écoute."
    elen reflechit "Je dis pas que tout va bien."
    elen desaccord "Je dis que crier 'c'est un salaud' n'aide personne."

    noam "Tu prends sa défense spontanément."

    elen taquin "Je sais."
    elen content "C'est un réflexe."
    elen joie "Comme éternuer, mais en plus poli."

    noam "Et si tu te trompes ?"

    elen reflechit "Alors je me trompe en essayant de réparer."
    elen content "Je préfère ça à avoir raison en détruisant."

    "Le brouhaha au fond de la cafétéria retombe un peu."

    elen reflechit "On critique plus facilement quelqu'un quand il n'est pas là."
    elen triste "Ça me serre le ventre."

    noam "Tu veux aller lui parler ?"

    elen joie "Oui."
    elen content "Pas pour le gronder."
    elen reflechit "Pour lui demander ce qui va pas, vraiment."

    "Elle me regarde comme si la réponse était évidente depuis toujours."

    elen neutre "Personne ne devient dur gratuitement."
    elen inquiet "Y a toujours une histoire avant."

    noam "Tu lui trouves des excuses."

    elen desaccord "Non."
    elen reflechit "Je lui cherche une porte de sortie."
    elen content "C'est différent."

    "Elle reprend son gobelet, grimace au goût, puis sourit quand même."

    elen taquin "Pouah."
    elen rire "Même la boisson mérite une seconde chance."

    noam "Tu vas vraiment défendre tout le monde, hein ?"

    elen joie "Presque."
    elen content "Sauf ceux qui ferment les portes exprès derrière eux."
    elen reflechit "Là, je frappe très fort à la porte."

    noam "Avec ton sourire ?"

    elen rire "Oui."
    elen taquin "Mon sourire est une arme blanche émotionnelle."

    "Je ris malgré moi."

    elen content "Regarde, t'es déjà moins tendu."
    elen joie "C'est exactement ça que je veux."

    noam "Tu crois vraiment qu'il n'y a pas de gens mauvais ?"

    elen reflechit "Je crois qu'il y a des gens qui ont arrêté d'espérer."
    elen triste "Et quand t'arrêtes d'espérer, tu fais mal autour."
    elen content "Mais ça peut revenir."

    "Elle tapote la table du bout des doigts, rythme léger."

    play sound sfx_tap

    elen content "Une phrase sans jugement."
    elen reflechit "Parfois ça suffit à faire reculer la nuit de quelqu'un."

    noam "Tu parles comme si tu l'avais déjà vu."

    elen neutre "Oui."
    elen joie "Et c'était beau à chaque fois."

    "Elle se lève, déterminée, mais son regard reste tendre."

    elen content "Allez."
    elen joie "On va distribuer un peu de bénéfice du doute avant que ça manque en stock."

    $ elen_link = 2

    jump FREE_TIME_END


label elen_link_3:

    scene bg_observation at adaptive_fullscreen

    $ showP("elen", "content", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "La baie vitrée reflète les néons en fragments mobiles."
    "Elen suit les lumières du regard, les mains croisées derrière le dos."

    elen joie "Tu sais, je fais confiance vite."
    elen rire "Parfois avant même de connaître le prénom."

    noam "C'est risqué."

    elen reflechit "Oui."
    elen content "Mais il faut bien commencer quelque part, non ?"

    "Elle tourne vers moi un profil calme, presque enfantin."

    elen neutre "Si j'attends des preuves parfaites,"
    elen reflechit "je ne laisserai jamais personne entrer."

    noam "Et si la mauvaise personne entre ?"

    elen inquiet "Alors ça fait mal."
    elen triste "Très mal, parfois."

    "Sa voix baisse d'un cran sans perdre sa douceur."

    noam "Ça t'est déjà arrivé."

    elen reflechit "..."
    elen content "Je fais confiance vite."
    elen desaccord "On parlait de ça, non ?"

    "Elle esquive la question avec un petit sourire appris."

    noam "Tu peux m'en parler si tu veux."

    elen neutre "Pas aujourd'hui."
    elen triste "Pardon."

    "Le silence s'installe un instant, rempli par le souffle grave des systèmes."

    play sound sfx_bip

    elen content "Regarde là-bas."
    elen joie "Les points lumineux se suivent comme une file d'enfants."

    noam "Tu changes de sujet."

    elen taquin "Oui."
    elen content "Avec élégance, en plus."

    "Elle pose son front un bref instant contre la vitre."

    elen reflechit "Je me dis que la confiance, c'est un pari."
    elen content "Un pari sur ce que l'autre peut devenir avec un peu d'espace."

    noam "Et quand le pari est perdu ?"

    elen triste "Je paie l'addition."
    elen inquiet "Souvent trop cher."
    elen content "Mais je recommence quand même."

    "Elle serre ses doigts entre eux, puis les relâche doucement."

    noam "Pourquoi ?"

    elen reflechit "Parce que la méfiance totale coûte encore plus cher."
    elen neutre "Elle te laisse seul, et seule la peur gagne."

    noam "Tu n'as jamais envie de te protéger ?"

    elen inquiet "Si."
    elen triste "Tous les jours."
    elen content "Mais je veux pas devenir un coffre-fort."

    "Son sourire revient, fin mais vrai."

    elen joie "Je préfère être une porte."
    elen taquin "Avec une sonnette, quand même."

    noam "Au moins une serrure ?"

    elen rire "Une petite."
    elen content "Qui grince."
    elen reflechit "Pour prévenir que j'ai peur aussi."

    "Elle tapote la vitre de l'ongle, deux fois, presque un code."

    play sound sfx_tap

    elen neutre "Je sais ce que tu penses."
    elen taquin "'Elen, tu vas te faire broyer'."

    noam "Je me dis surtout que tu es courageuse."

    elen surpris "Oh."
    elen content "Merci."

    "Ses épaules se détendent un peu."

    elen reflechit "On verra plus tard pour les histoires compliquées."
    elen content "Pour l'instant, on va dire que j'apprends encore."
    elen joie "Et que je préfère apprendre en aimant les gens qu'en les fuyant."

    noam "D'accord."

    elen content "Promis, un jour je te raconterai."
    elen taquin "Mais pas aujourd'hui."

    "Elle m'offre un clin d'œil fragile, puis regarde à nouveau le vide au-delà de la vitre."

    $ elen_link = 3

    jump FREE_TIME_END


label elen_link_4:

    scene bg_infirmerie at adaptive_fullscreen

    $ showP("elen", "content", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "L'infirmerie est presque vide."
    "Une alarme discrète pulse au loin, régulière comme un cœur artificiel."

    play sound sfx_bip

    elen joie "J'aime bien la lumière ici."
    elen reflechit "Elle est froide, mais propre."

    "Elle sourit, mais ses doigts triturent la manche de sa veste."

    noam "Tu as l'air ailleurs."

    elen content "Non, ça va."
    elen joie "Vraiment."

    "Son ton monte un peu trop vite, comme un réflexe de défense."

    noam "Tu n'es pas obligée de forcer."

    elen reflechit "Je ne force pas."
    elen inquiet "Je..."
    elen content "Ça ira."

    "Elle appuie ses paumes sur le bord d'une table métallique."

    elen neutre "C'est juste que..."
    elen triste "Tout à l'heure, dans le couloir, j'ai entendu un bruit."
    elen inquiet "Un bruit sec."

    noam "Et ?"

    elen reflechit "Et mon ventre s'est noué d'un coup."
    elen triste "Comme si mon corps savait déjà ce que ma tête refusait."

    "Elle respire plus lentement, compte mentalement."

    elen content "Mais c'est passé."
    elen joie "Tu vois ?"

    noam "Ton sourire tremble."

    elen surpris "Hein ?"
    elen triste "Ah..."

    "Elle touche sa joue comme pour vérifier elle-même."

    elen inquiet "Je déteste quand ça se voit."
    elen reflechit "D'habitude je tiens mieux."

    noam "Tu peux juste dire que tu as peur."

    elen desaccord "Si je dis ça, les autres vont paniquer aussi."
    elen triste "Alors je fais la lampe de poche."
    elen content "Même quand la pile baisse."

    "La phrase reste suspendue entre nous."

    noam "Tu n'as pas à éclairer tout le monde seule."

    elen reflechit "Je sais."
    elen inquiet "Mais j'ai appris à faire comme si."

    "Un bip plus aigu coupe le silence, puis revient au rythme normal."

    play sound sfx_bip

    elen triste "Parfois, j'ai l'impression que si j'arrête de sourire"
    elen inquiet "tout va s'effondrer plus vite."

    noam "Et là, maintenant ?"

    elen content "Là..."
    elen reflechit "Là, j'ai juste besoin de trente secondes."

    "Elle ferme les yeux, inspire profondément, puis expire en quatre temps."

    elen content "Voilà."
    elen joie "Ça ira."
    elen triste "Je crois."

    noam "Le 'je crois' est déjà plus honnête."

    elen taquin "Tu deviens dangereux."
    elen content "Tu me fais dire la vérité."

    "Elle laisse échapper un petit rire qui casse à moitié."

    elen reflechit "Je veux continuer à croire que ça ira."
    elen inquiet "Mais aujourd'hui, c'est... plus difficile."

    noam "On peut rester là sans parler."

    elen content "Oui."
    elen joie "Restons juste là une minute."

    "On reste côte à côte, entourés de métal, de néons et d'un silence trop propre."
    "Quand elle rouvre les yeux, son sourire est revenu, plus petit, plus vrai."

    elen content "Merci."

    $ elen_link = 4

    jump FREE_TIME_END


label elen_link_5:

    scene bg_repos at adaptive_fullscreen

    $ showP("elen", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "La salle de repos bourdonne doucement."
    "Elen est assise en tailleur sur le canapé, un gobelet vide entre les mains."

    elen reflechit "Tu sais..."
    elen content "Je crois que je suis vraiment naïve."

    noam "Tu dis ça sans honte ?"

    elen joie "Oui."
    elen taquin "Avec un peu de panache, même."

    "Elle sourit avant de reprendre, plus sérieuse."

    elen neutre "Les gens pensent que je ne vois pas les risques."
    elen reflechit "En vrai, je les vois parfois très bien."
    elen triste "Je choisis juste autre chose."

    noam "Croire au meilleur."

    elen content "Exactement."
    elen joie "Même quand je me trompe."

    "Elle fait tourner le gobelet entre ses doigts, lentement."

    elen reflechit "Je préfère me tromper en ouvrant les bras"
    elen desaccord "qu'avoir raison en fermant toutes les portes."

    noam "Et quand ça te casse ?"

    elen triste "Ça me casse."
    elen inquiet "Parfois longtemps."
    elen content "Mais ça ne décide pas de qui je deviens."

    "Elle pose le gobelet sur la table basse avec délicatesse."

    play sound sfx_tasse

    elen joie "On m'a déjà dit 'grandis un peu'."
    elen taquin "Comme si la lumière était un défaut d'usine."

    noam "Tu n'as jamais voulu changer ?"

    elen reflechit "Si."
    elen triste "Quand ça faisait trop mal."
    elen content "Puis je me souvenais des moments où croire avait sauvé quelqu'un."

    noam "Tu portes ça comme une décision."

    elen neutre "C'en est une."
    elen reflechit "L'innocence, chez moi, c'est pas l'ignorance."
    elen content "C'est une direction."

    "Elle me regarde droit dans les yeux, calme et stable."

    elen joie "Je veux rester lumineuse."
    elen reflechit "Pas pour nier l'ombre."
    elen content "Pour que l'ombre n'ait pas le dernier mot."

    noam "Même si les autres te trouvent imprudente ?"

    elen taquin "Surtout là."
    elen joie "Sinon, je vis selon la peur des autres."

    "Un rire discret lui échappe, puis elle hausse les épaules."

    elen content "Je me connais."
    elen reflechit "Je vais encore faire confiance trop tôt."
    elen taquin "Je vais encore défendre l'indéfendable au mauvais moment."

    noam "Et pourtant ?"

    elen joie "Et pourtant je vais continuer à essayer."
    elen content "Parce que parfois, ça marche."
    elen reflechit "Et ces fois-là valent les cicatrices."

    "Je hoche la tête sans trouver quoi ajouter."

    elen neutre "Je veux pas être parfaite."
    elen content "Je veux être cohérente avec ce que je donne."

    noam "Tu es cohérente, oui."

    elen surpris "Tu trouves ?"

    noam "Tu choisis la lumière en connaissance de cause."

    elen joie "Alors ça me va."
    elen content "C'est exactement ça."

    "Elle se lève du canapé et étire ses bras vers le plafond."

    elen rire "Bon !"
    elen joie "Assez de philosophie existentielle."
    elen taquin "On joue aux fléchettes magnétiques et je te bats avec amour."

    noam "Le 'avec amour' m'inquiète."

    elen rire "Parfait."
    elen joie "L'inquiétude, c'est le premier pas vers la sagesse."

    "Elle m'attrape la main et m'entraîne déjà vers le jeu en riant."
    "Sa lumière n'est pas moins vraie parce qu'elle connaît le prix."

    $ elen_link = 5

    jump FREE_TIME_END
