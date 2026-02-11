# -----------------------------------------------------------------------
# LIENS — IRIS
# -----------------------------------------------------------------------

default iris_link = 0


label IRIS_LINK_INTERACT:

    menu:
        "Passer du temps avec Iris ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if iris_link == 0:
        jump iris_link_1
    elif iris_link == 1:
        jump iris_link_2
    elif iris_link == 2:
        jump iris_link_3
    elif iris_link == 3:
        jump iris_link_4
    elif iris_link == 4:
        jump iris_link_5

    if last_room_label:
        jump expression last_room_label
    return


label iris_link_1:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_repos at adaptive_fullscreen

    $ showP("iris", "colere", 0.58)
    $ showP("noam", "reflexion", 0.22)

    iris colere "Franchement, cette salle est mal foutue."
    iris desaccord "Trop de néons, pas assez d'air, et ce canapé fait un bruit de papier bulle."
    iris colere "Je te jure, rien n'est normal ici."

    "Elle passe devant la table basse en soufflant."
    "Son genou accroche le coin."

    play sound sfx_drop

    iris surprise "Aïe !"
    iris colere "Mais évidemment."
    iris fatigue "Parfait. Super entrée."

    noam "Ça va ?"

    iris desaccord "Oui, oui, nickel."
    iris colere "J'adore me fracasser les rotules pour dire bonjour."
    iris taquin "C'est mon langage corporel."

    "Elle ramasse un gobelet vide qu'elle vient de pousser sans faire exprès."
    "Le gobelet roule encore un peu plus loin."

    iris colere "Regarde-moi ça."
    iris desaccord "C'est pas ma faute si les objets me détestent personnellement."

    noam "Tu veux t'asseoir deux minutes ?"

    iris colere "Non."
    iris fatigue "Enfin si."
    iris colere "Mais pas parce que je me suis cognée."
    iris culpabilite "Juste parce que ce canapé... enfin bref."

    "Elle s'assoit d'un geste brusque."
    "Le coussin s'enfonce et elle perd l'équilibre une demi-seconde."

    iris surprise "Oh non, pas encore..."
    iris colere "Je hais cette pièce."

    noam "Tu râles beaucoup aujourd'hui."

    iris taquin "Aujourd'hui ?"
    iris colere "C'est mignon, ton optimisme."
    iris desaccord "Je râle tout le temps, c'est cohérent au moins."

    "Elle frotte son genou et détourne les yeux."

    iris fatigue "J'ai juste..."
    iris desaccord "J'ai juste mal visé, c'est tout."
    iris colere "Ça arrive."
    iris culpabilite "Souvent."

    noam "Ça t'embarrasse ?"

    iris colere "Quoi ? Non."
    iris desaccord "Enfin..."
    iris fatigue "Peut-être un peu."

    "Elle souffle par le nez, contrariée contre elle-même."

    iris colere "C'est chiant de vouloir avoir l'air solide"
    iris desaccord "et d'être doublée par un gobelet en carton."
    iris taquin "Un gobelet."
    iris colere "En carton."

    noam "Je dirai rien."

    iris taquin "Tu diras rien, mais tu vas t'en souvenir toute ta vie."
    iris colere "Et tu raconteras ça dans un discours un jour."
    iris desaccord "'Iris, grande guerrière, vaincue par un angle de table'."

    "Je ris malgré moi."

    iris colere "Ne rigole pas."
    iris taquin "Enfin si, rigole."
    iris fatigue "Sinon je vais encore penser à ça toute la nuit."

    "Elle se renfrogne, puis hausse les épaules."

    iris desaccord "Bon."
    iris colere "Je considère cet incident comme classé."
    iris taquin "Si quelqu'un demande, j'ai gagné un duel."

    noam "Contre quoi ?"

    iris colere "Contre la gravité."
    iris fatigue "De justesse."

    "Elle se lève et grommelle encore en réajustant sa manche."

    iris colere "Allez, on bouge."
    iris desaccord "Plus je reste ici, plus je vais casser quelque chose."

    $ iris_link = 1

    jump FREE_TIME_END


label iris_link_2:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("iris", "taquin", 0.58)
    $ showP("noam", "reflexion", 0.22)

    iris taquin "Tu sais ce qui est drôle ?"
    iris sourire "J'ai enfin un vrai scoop."
    iris hesitation "Enfin... non, oublie."

    noam "Un scoop ?"

    iris surprise "Non !"
    iris colere "J'ai rien dit."
    iris fatigue "Tu m'as mal entendu."

    noam "J'ai pourtant bien entendu 'scoop'."

    iris culpabilite "Mince."
    iris colere "Ok, mais tu répètes pas."
    iris desaccord "Jamais."

    noam "Promis."

    iris reflexion "J'ai surpris une conversation hier soir."
    iris inquiet "Entre deux personnes qui pensaient être seules."
    iris desaccord "Et apparemment..."
    iris surprise "Non, non, non, j'aurais pas dû commencer."

    "Elle se couvre la bouche avec ses deux mains."

    iris colere "Pourquoi je fais ça ?"
    iris fatigue "Pourquoi je parle avant de penser ?"

    noam "Respire."

    iris inquiet "Je respire !"
    iris peur "C'est justement le problème, je respire et je parle en même temps."
    iris colere "Et quand je parle, je détruis des vies."

    "Elle tourne en rond devant la machine à boissons."

    iris desaccord "Ok."
    iris reflexion "On recommence."
    iris colere "Je n'ai rien entendu."
    iris desaccord "Personne n'a rien dit."
    iris taquin "La cafétéria est vide de secrets et pleine de protéines."

    noam "Tu t'enfonces."

    iris colere "Je sais !"
    iris fatigue "Je m'en rends compte en direct, c'est horrible."

    "Elle pointe un doigt vers moi, paniquée."

    iris inquiet "Si un jour quelqu'un te demande..."
    iris desaccord "Non attends, ça sonne coupable."
    iris colere "Ne dis jamais que je t'ai dit de ne rien dire."
    iris surprise "Oh mon dieu, c'est encore pire."

    noam "Iris."

    iris peur "Quoi ?"

    noam "Tu peux t'arrêter là."

    iris fatigue "Oui."
    iris culpabilite "Oui, oui, oui."
    iris desaccord "Je m'arrête."

    "Deux secondes de silence."

    iris taquin "Bref, donc la conversation disait que—"
    iris surprise "NON !"
    iris colere "Stop."
    iris fatigue "Ferme-la, Iris."

    "Elle se donne une petite tape sur le front."

    iris desaccord "C'est pas possible."
    iris colere "J'ai un problème médical avec le secret."
    iris culpabilite "Je veux protéger les gens, et je les grille en quatre phrases."

    noam "Tu n'as pas besoin de tout porter seule."

    iris reflexion "Je sais."
    iris fatigue "Mais c'est plus fort que moi."
    iris desaccord "Je veux éviter une catastrophe"
    iris colere "et je fabrique la catastrophe en parlant de la catastrophe."

    "Elle inspire longuement, puis se calme un peu."

    iris inquiet "Bon."
    iris desaccord "Version finale."
    iris colere "Tu n'as rien entendu."
    iris fatigue "Moi non plus."
    iris taquin "Et si quelqu'un insiste, on accuse Julian."

    noam "C'est injuste."

    iris sourire "Oui."
    iris taquin "C'est pour ça que c'est crédible."

    "Elle grimace, encore honteuse."

    iris culpabilite "Pardon."
    iris fatigue "Je voulais juste..."
    iris desaccord "faire attention."

    $ iris_link = 2

    jump FREE_TIME_END


label iris_link_3:

    scene bg_observation at adaptive_fullscreen

    $ showP("iris", "neutre", 0.58)
    $ showP("noam", "reflexion", 0.22)

    "La salle est calme."
    "Trop calme pour Iris."

    iris reflexion "C'est bizarrement paisible ici."
    iris taquin "Ça me met presque mal à l'aise."

    noam "On peut juste regarder un moment."

    iris neutre "Oui."
    iris fatigue "Regarder."
    iris desaccord "Ne rien casser."

    "Elle recule d'un pas pour s'appuyer contre la rambarde."
    "Son talon glisse sur le rebord au sol."

    play sound sfx_drop

    iris surprise "Oh—"
    "Iris part en arrière, se rattrape de travers et tombe assise."

    noam "Iris !"

    iris colere "Aïe."
    iris fatigue "AÏE, bordel."
    iris desaccord "Je vais bien."
    iris colere "Je déteste cette phrase mais je vais bien."

    "Je m'accroupis près d'elle."

    noam "Tu t'es fait mal ?"

    iris fatigue "Un peu à mon ego, surtout."
    iris taquin "Le reste est déjà amorti par l'habitude."

    noam "L'habitude ?"

    iris desaccord "Oui."
    iris fatigue "Ça m'arrive tout le temps."
    iris colere "Escaliers, tapis, portes, gravité, concept d'équilibre..."
    iris taquin "Tout ça est en guerre ouverte contre moi."

    "Elle rit une seconde, puis se tait."

    iris culpabilite "Chez moi, on disait que je devais faire plus attention."
    iris desaccord "Tout le temps."
    iris fatigue "'Tiens-toi droite, regarde où tu vas, fais pas de bruit'."

    noam "Ça fait beaucoup."

    iris colere "Oui."
    iris desaccord "Et quand je faisais une chute, on disait que c'était de ma faute."
    iris fatigue "Comme si j'avais planifié de m'éclater au sol pour le plaisir."

    "Elle se relève en prenant appui sur ma main."

    iris neutre "Merci."
    iris colere "N'en fais pas une scène."
    iris desaccord "Je veux pas qu'on me regarde comme une chose fragile."

    noam "Je te regarde comme quelqu'un qui vient de tomber."

    iris taquin "Charmant."
    iris fatigue "Très romantique, vraiment."

    "Elle époussette son pantalon."

    iris reflexion "Le pire, c'est pas la douleur."
    iris culpabilite "C'est la seconde juste après."
    iris fatigue "Quand tout le monde attend de voir si tu vas pleurer."

    noam "Et toi, tu fais quoi ?"

    iris colere "Je râle."
    iris taquin "Très fort."
    iris desaccord "Comme ça personne entend le reste."

    "Elle relève le menton, plus fermée."

    iris neutre "Bon."
    iris colere "C'était un incident technique."
    iris taquin "Le sol est en tort."
    iris desaccord "Affaire classée."

    noam "Compris."

    iris fatigue "Parfait."
    iris desaccord "On parle d'autre chose."
    iris colere "N'importe quoi sauf ma dignité en morceaux."

    $ iris_link = 3

    jump FREE_TIME_END


label iris_link_4:

    scene bg_stockage at adaptive_fullscreen

    $ showP("iris", "colere", 0.58)
    $ showP("noam", "reflexion", 0.22)

    iris colere "Cette salle sent le plastique triste."
    iris desaccord "Les boîtes sont mal rangées."
    iris colere "L'éclairage est criminel."
    iris fatigue "Et moi je suis de mauvaise humeur, au cas où c'était pas clair."

    noam "C'est très clair."

    iris colere "Les règles ici sont absurdes."
    iris desaccord "Les gens font semblant d'aller bien."
    iris colere "Je fais semblant aussi."
    iris fatigue "Et j'en ai marre de faire semblant."

    "Elle tape du pied, puis grimace comme si elle regrettait d'en avoir trop dit."

    iris desaccord "Oublie."
    iris colere "J'ai rien dit."

    noam "Tu peux dire."

    iris inquiet "Non."
    iris colere "Enfin si."
    iris fatigue "Non."

    "Elle souffle fort."

    iris desaccord "Je râle parce que c'est plus simple."
    iris reflexion "Quand je râle, j'ai l'impression de tenir debout."
    iris culpabilite "Si je m'arrête..."
    iris fatigue "j'ai peur de m'écrouler."

    "Le silence dure un instant."

    noam "Tu n'as pas besoin de prouver que ça va."

    iris colere "Je sais."
    iris desaccord "Mais si je le montre, les gens paniquent."
    iris fatigue "Ou pire, ils compatissent."
    iris colere "Je déteste ça."

    noam "Le fait qu'on le remarque ?"

    iris surprise "Oui !"
    iris colere "Exactement."
    iris desaccord "Ne remarque pas que je râle pour survivre."
    iris fatigue "Laisse-moi râler tranquille."

    "Elle détourne les yeux, presque vexée d'être comprise."

    iris taquin "Tu vois, c'est insupportable."
    iris colere "T'es censé me laisser jouer la peste pénible."
    iris desaccord "Pas analyser mon système d'urgence en direct."

    noam "Pardon."

    iris fatigue "Non..."
    iris culpabilite "C'est pas toi."
    iris desaccord "C'est juste que quand quelqu'un voit clair"
    iris colere "j'ai plus de décor où me cacher."

    "Elle fait quelques pas entre les caisses."

    iris reflexion "Chez moi, on appelait ça 'avoir du caractère'."
    iris desaccord "C'était plus chic que 'être au bord de la crise'."
    iris fatigue "Ça faisait bonne éducation."

    noam "Et toi, tu l'appelles comment ?"

    iris neutre "J'appelle ça tenir."
    iris fatigue "Tenir jusqu'au soir."
    iris desaccord "Puis recommencer demain."

    "Elle serre ses bras contre elle puis relâche."

    iris taquin "Bon."
    iris colere "Assez de sentiments pour aujourd'hui."
    iris desaccord "Je retourne à mon activité principale : critiquer la décoration."
    iris fatigue "Regarde-moi ces étagères, c'est une agression visuelle."

    noam "Tu vas tenir ?"

    iris sourire "Je tiens."
    iris taquin "En râlant, mais je tiens."

    noam "Et quand tu ne tiens plus ?"

    iris fatigue "Je compte jusqu'à dix."
    iris desaccord "Puis je critique un meuble."
    iris taquin "Ou un mur."
    iris colere "Ou ma coupe de cheveux."

    noam "Méthode complète."

    iris sourire "Méthode artisanale, mais approuvée."
    iris fatigue "Et aujourd'hui..."
    iris desaccord "ça suffit pour rester debout."

    $ iris_link = 4

    jump FREE_TIME_END


label iris_link_5:

    scene bg_repos at adaptive_fullscreen

    $ showP("iris", "hesitation", 0.58)
    $ showP("noam", "reflexion", 0.22)

    iris hesitation "Je voulais te dire un truc."
    iris desaccord "Enfin, non."
    iris fatigue "Enfin, si."

    noam "Je t'écoute."

    iris reflexion "C'est juste que..."
    iris inquiet "C'est important, mais c'est nul à dire."
    iris colere "Pourquoi les phrases simples deviennent impossibles quand il faut être sincère ?"

    "Elle se mord la lèvre, cherche ses mots."

    iris hesitation "Depuis qu'on est ici, je..."
    iris desaccord "Non, attends."
    iris fatigue "Je recommence."

    iris reflexion "Depuis qu'on est ici, j'essaie de rester..."
    iris colere "de rester efficace."
    iris desaccord "Contrôlée."
    iris fatigue "Supportable."

    noam "Tu l'es."

    iris taquin "Menteur."
    iris fatigue "Mais merci."

    "Elle laisse échapper un petit rire nerveux."

    iris hesitation "Le problème c'est que je fais toujours la maligne."
    iris desaccord "Je parle trop, je pique, je râle..."
    iris culpabilite "et parfois j'ai l'impression de disparaître derrière tout ça."

    noam "Tu ne disparais pas."

    iris inquiet "Tu dis ça maintenant."
    iris desaccord "Mais un jour je vais faire la gaffe de trop."
    iris fatigue "Ou dire un truc que je pense pas."

    noam "Tu peux aussi dire ce que tu penses."

    iris hesitation "Justement."
    iris reflexion "Ce que je pense, c'est..."
    iris surprise "Ah non, c'est horrible."
    iris colere "Pourquoi mon cerveau coupe au pire moment ?"

    "Elle ferme les yeux une seconde."

    iris fatigue "Ok."
    iris desaccord "Version brute."
    iris hesitation "Quand t'es là, je me sens moins..."
    iris inquiet "moins en danger de moi-même."

    "Elle ouvre les yeux, visiblement surprise par ses propres mots."

    iris surprise "Voilà."
    iris culpabilite "C'est sorti tout seul."
    iris colere "Super."
    iris fatigue "Magnifique maîtrise."

    noam "C'est pas maladroit."

    iris desaccord "Si, c'est maladroit."
    iris taquin "C'est ma marque déposée, faut respecter la charte."

    "Elle détourne le regard vers le canapé."

    iris hesitation "Je voulais juste dire que..."
    iris desaccord "tu m'aides."
    iris fatigue "Même quand je suis infernale."
    iris culpabilite "Et je sais que je dis pas souvent merci."

    noam "Tu viens de le faire."

    iris sourire "Ouais."
    iris taquin "N'en profite pas pour devenir insupportable, hein."

    "Je hoche la tête."

    iris reflexion "Je promets pas de devenir douce et élégante d'un coup."
    iris colere "Je vais encore râler."
    iris desaccord "Je vais encore trébucher."
    iris fatigue "Je vais encore parler trop vite."

    noam "Et alors ?"

    iris sourire "Et alors..."
    iris hesitation "essaie de rester quand même."

    "Elle dit ça presque dans un souffle."
    "Puis elle détourne vite le regard, incapable d'assumer plus longtemps."

    iris taquin "Bon."
    iris colere "C'était le moment émotion, c'est fini."
    iris desaccord "Maintenant je redeviens pénible, c'est plus sûr."

    $ iris_link = 5

    jump FREE_TIME_END
