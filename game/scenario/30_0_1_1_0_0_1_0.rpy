# JOUR 30 — ROUTE JULIAN SAUVÉ : LE PRIX D'UNE VIE
# Le sabotage de la seringue au J29 a réussi. Une seule fin, sans major choice J30.
# Une matinée : le scandale éclate avant le départ de la navette à 10 h.
default j30_julian_saved_exposed = False
default j30_julian_saved_exiled = False
default j30_julian_saved_ending = None

label _30_0_1_1_0_0_1_0_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"
    $ cafeteria_food_level = "null"
    if not j29_julian_syringe_swapped:
        jump _30_0_1_1_0_0_1_1_REVEIL
    $ j30_julian_saved_exposed = False
    $ j30_julian_saved_exiled = False
    $ j30_julian_saved_ending = None
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6
    "Je suis réveillé depuis un moment, et la seule chose à laquelle j'arrive à penser, c'est la main de Julian qui bougeait encore."
    "J'ai remplacé le produit. Je l'ai fait. Mais personne ne m'a dit ce qu'il était devenu après qu'on l'a ramené au laboratoire."
    "Sur le bureau, le dessin de Juliette est posé à côté de ma tablette. Je le prends, puis je le glisse dans ma poche."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Bonjour, mes petits passagers ! Dernier réveil au Conclave ! L'embarquement approche, alors tâchez de ne pas rater votre merveilleux retour sur Terre !"
    kami "Je vous conseille de régler vos différends avant de monter. Une dispute familiale à bord, c'est terrible pour l'ambiance."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "J'entends quelques frottements étouffés derrière la grille d'aération. Je me redresse, mais le bruit s'arrête et je finis par me rallonger."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Mes chers représentants, rassemblement en salle du Conclave ! Le dernier vote commence dans quelques minutes : « Quiconque ne respecte pas un Commandement aura désormais la mémoire effacée, plutôt que d'être éliminé. »"
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Le vote... Je peux pas y aller. Si ma copie s'y présente aussi, tout le monde verra qu'on est deux. Ça ferait tout exploser."
    "Je reste dans ma chambre et j'essaie de me reposer un peu, même si les bruits reprennent derrière la paroi."
    "Cette fois, la grille d'aération bouge. Une fois. Puis une deuxième, plus violemment."
    noam inquiet "Elias ?"
    "Un frottement, des coups de genou dans le métal. Quelqu'un essaie de ramper sans faire de bruit, mais n'y arrive manifestement pas."
    "J'ouvre la grille et passe la tête à l'intérieur."
    jump _30_0_1_1_0_0_1_0_CONDUIT
    # Durée : 1m30

label _30_0_1_1_0_0_1_0_CONDUIT:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.4
    "À quelques mètres de moi, quelqu'un s'arrête de ramper. Ses vêtements sont froissés, son visage couvert de sueur."
    "Julian. Enfin... son double, forcément. L'original a été emmené au laboratoire, et je l'ai vu cesser de bouger."
    $ showGroup([("noam", "surpris", 0.25), ("julian", "peur", 0.77)])
    noam surpris "Julian ? Qu'est-ce que tu fous là ?! Tu devrais pas être avec les autres ?"
    julian peur "Non... Non, recule !"
    noam inquiet "Quoi ? Mais qu'est-ce qui t'arrive ?"
    julian colere "T'ÉTAIS DANS MA CHAMBRE ! Je t'ai vu !"
    noam surpris "Attends... Ta chambre ?"
    julian peur "Y avait Mara ! Et Sael ! Elle m'a piqué avec un truc, et après je me suis réveillé entouré de..."
    "Mon estomac se serre. Ce n'est pas le double de Julian. C'est lui. Celui que j'ai vu allongé, sans bouger."
    noam inquiet "Julian, écoute, c'est pas ce que tu crois. Je peux t'expliquer !"
    julian colere "Tu veux m'expliquer quoi ?! Pourquoi vous avez essayé de me tuer ?!"
    noam panique "Non ! C'était pas... Putain, je voulais pas que ça arrive !"
    julian colere "ARRÊTE ! Tu vas pas me refaire le même coup !"
    "Julian recule si brusquement qu'il heurte une jonction. Il se retourne et se met à ramper vers le passage qui rejoint la cafétéria."
    noam peur "Julian ! Attends !"
    julian peur "ME SUIS PAS !"
    "Je le suis malgré tout. Il va si vite qu'il se cogne contre les parois, mais il finit par atteindre la grille de sortie."
    "Par l'ouverture qui donne sur la cafétéria, une voix amplifiée nous parvient depuis les haut-parleurs de la salle. On n'entend rien dans le reste des conduits, mais ici la grille est juste au-dessus des enceintes."
    kami "Le dernier scrutin est terminé. L'unanimité a été atteinte : l'amendement est adopté !"
    "Des conversations et des pas résonnent de l'autre côté. Les représentants reviennent du vote."
    "Je vois les pieds de Julian disparaître. La grille s'ouvre sur leurs voix."
    $ hideGroup()
    jump _30_0_1_1_0_0_1_0_CAFETERIA
    # Durée : 1m30

label _30_0_1_1_0_0_1_0_CAFETERIA:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    "Les représentants reviennent tout juste du scrutin. Ils entrent presque tous en même temps dans la cafétéria, parlant encore de l'amendement adopté, leurs sacs à la main."
    "Julian trébuche en sortant de la grille. Elen se précipite vers lui."
    $ showGroup([("julian", "peur", 0.18), ("elen", "inquiet", 0.49), ("lysa", "surpris", 0.81)])
    elen inquiet "Julian ?! Mais qu'est-ce qui t'est arrivé ?! T'es couvert de poussière !"
    julian peur "Ferme la grille ! Ferme-la !"
    lysa surpris "Quoi ? Pourquoi tu sors de là ?"
    julian peur "IL EST DERRIÈRE MOI !"
    "Je débouche à mon tour. Julian me voit et attrape une chaise pour la placer entre nous."
    $ showGroup([("julian", "peur", 0.18), ("noam", "inquiet", 0.49), ("elen", "peur", 0.81)])
    noam raison "Julian, pose ça. Je veux juste te parler !"
    julian colere "C'EST LUI ! C'est Noam ! Il a essayé de me tuer cette nuit !"
    elen peur "Quoi ?! Mais qu'est-ce que tu racontes ?"
    noam panique "Attendez ! C'est pas ce que vous croyez ! J'étais là, oui, mais c'est beaucoup plus compliqué que ça !"
    julian peur "Il était dans ma chambre avec deux autres ! J'ai reconnu leurs visages. Ils m'ont plaqué sur le lit et..."
    noam inquiet "Julian, tu dois m'écouter, je suis pas celui que tu crois !"
    julian colere "Tu m'as poursuivi dans les conduits, espèce de malade !"
    $ showGroup([("julian", "peur", 0.18), ("nyra", "inquiet", 0.50), ("elias", "surpris", 0.81)])
    nyra inquiet "Julian, recule doucement, tu vas te faire mal."
    julian peur "..."
    julian peur "Toi... Je t'ai vue."
    nyra raison "Tu me vois maintenant, oui. Respire."
    julian colere "NON ! JE T'AI VUE MORTE !"
    elias surpris "Hein ?!"
    julian peur "Et lui ! Je l'ai vu aussi ! Elias ! Vous étiez allongés là-bas, tous les deux, je... J'ai vu vos corps !"
    elias colere "Mais qu'est-ce que tu racontes, putain ?! Je suis là !"
    julian peur "JE SAIS ! C'EST ÇA QUE JE COMPRENDS PAS !"
    "Il recule encore, jusqu'au mur. Ses yeux passent de Nyra à Elias, puis à chacun des autres visages."
    julian peur "Y en avait d'autres... Je sais plus qui... Merde, je sais plus !"
    nyra raison "Personne ne va te toucher, d'accord ?"
    julian colere "Toi, t'approche pas !"
    "Autour des tables, plus personne ne mange."
    $ showGroup([("noam", "inquiet", 0.18), ("lysa", "reflexion", 0.51), ("ryn", "colere", 0.82)])
    lysa reflexion "Attendez. Des gens morts qui sont là aujourd'hui... On a déjà entendu ça."
    ryn colere "Noam nous a raconté exactement ce genre de trucs il y a quelques jours !"
    noam raison "Oui ! Je vous ai dit que quelqu'un copiait les représentants ! C'est ce qui se passe !"
    lysa inquiet "Alors pourquoi Julian dit que c'est toi qui l'as attaqué ?"
    noam panique "Parce qu'il m'a vu avec Mara et Sael ! Mais j'ai rien fait contre lui, je vous le jure !"
    ryn colere "T'as fait quoi avec elles, déjà ?! Pourquoi t'étais dans sa chambre ?"
    noam peur "Je peux vous expliquer, mais pas tous en train de me hurler dessus !"
    jump _30_0_1_1_0_0_1_0_DEUX_NOAM
    # Durée : 3m

label _30_0_1_1_0_0_1_0_DEUX_NOAM:
    "La porte de la cafétéria s'ouvre. Iris arrive avec celui que tout le monde croit être moi."
    scene bg_cafeteria at adaptive_fullscreen with vpunch
    $ showGroup([("iris", "determine", 0.19), ("dg_noam", "surpris", 0.52), ("noam", "peur", 0.82)])
    iris colere "C'est quoi, ce bordel ?! On vous entend jusque dans le couloir !"
    dg_noam surpris "..."
    noam peur "Iris !"
    "Iris s'arrête net en voyant mon visage à côté de celui du garçon avec lequel elle vient d'entrer. Elle recule aussitôt, se décale loin de nous deux et lève les mains, prête à se défendre."
    iris determine "Personne bouge. Aucun des deux, compris ?!"
    dg_noam inquiet "Iris, attends..."
    iris colere "Non, toi aussi tu fermes ta gueule ! J'ai déjà vu le corps de Mara, alors deux Noam dans la même pièce, ça me donne surtout envie de frapper avant de poser des questions."
    noam colere "C'est lui, le double ! On a échangé nos places pour que je puisse découvrir ce qu'ils faisaient au laboratoire !"
    iris determine "Et je suis censée savoir lequel dit vrai comment ? Restez à distance !"
    noam raison "Iris, tu sais que je t'avais parlé de tout ça !" 
    dg_noam raison "Je sais pas ce qu'il raconte, Iris. Je suis venu avec toi, là, maintenant. Tu le sais."
    noam colere "Parce qu'il a pris ma place au jour 26 !"
    dg_noam inquiet "Qu'est-ce qu'il est en train d'inventer ?"
    "La voix du double tremble un peu. Il n'arrive pas à me regarder franchement."
    $ showGroup([("julian", "peur", 0.18), ("iris", "inquiet", 0.50), ("noam", "colere", 0.82)])
    julian colere "C'est LUI qui m'a attaqué ! Celui-là ! Je reconnais ses fringues, et sa voix !"
    noam panique "Julian, je voulais pas que ça arrive ! Je sais ce que t'as vu, mais tu comprends pas pourquoi j'étais là !"
    julian peur "J'en sais rien ! Arrête de me poser des questions !"
    iris raison "Julian, va te mettre près d'Elen. Personne te touche."
    julian colere "Non ! Je veux pas qu'on s'approche de moi !"
    "Elen s'arrête à plusieurs pas. Julian garde sa chaise contre lui."
    $ showGroup([("iris", "determine", 0.20), ("dg_noam", "inquiet", 0.52), ("noam", "peur", 0.82)])
    iris determine "Bon. Ça suffit ! Vous allez arrêter tous les deux et m'écouter."
    noam inquiet "Iris, je t'en prie..."
    iris colere "JE PARLE ! Vous avez le même visage, les mêmes souvenirs peut-être, j'en sais rien. Alors je vais poser une question."
    dg_noam inquiet "Iris..."
    iris raison "Hier soir, je t'ai avoué un truc. Un truc que j'ai jamais raconté à personne ici. C'était quoi ?"
    "Je la fixe. Hier soir, j'étais seul dans ma chambre, à me demander si Julian respirait encore."
    noam hesitation "Hier soir... ? Iris, c'est pas moi qui étais avec toi ! C'était lui !"
    iris colere "Réponds à ma question !"
    noam peur "Je peux pas ! Je sais pas ce que tu lui as raconté !"
    $ showGroup([("iris", "inquiet", 0.22), ("dg_noam", "fatigue", 0.73)])
    dg_noam fatigue "Tu m'as dit que t'avais laissé croire à tout le monde que tu t'étais blessée au dernier tournoi, parce que t'avais eu peur de remonter sur le ring."
    dg_noam raison "T'as gardé ça pour toi pendant des années. Tu me l'as dit hier parce que t'avais confiance en moi."
    iris peur "..."
    iris raison "Oui. C'est ça."
    "Elle se place devant mon double."
    iris determine "L'autre, c'est l'imposteur. Je sais très bien à qui j'ai parlé hier."
    $ showGroup([("iris", "colere", 0.20), ("noam", "panique", 0.51), ("lysa", "inquiet", 0.82)])
    noam panique "Mais justement ! C'était lui, hier ! Je viens de vous le dire !"
    lysa inquiet "Iris, connaître une histoire, ça suffit pas forcément. Si ces copies récupèrent les souvenirs..."
    iris colere "Et on fait quoi, alors ? On prend les deux dans la navette ?! Tu veux qu'il lui arrive ce qui est arrivé à Julian ?!"
    noam panique "Mais vous voyez bien qu'il y a quelque chose qui cloche ! Pourquoi vous refusez de m'écouter deux secondes ?!"
    julian peur "ARRÊTE DE PARLER DE MOI !"
    "Ryn se met entre nous. Sael et Mara arrivent au fond de la cafétéria, attirées par les cris, et s'immobilisent en découvrant la scène."
    $ showGroup([("mara", "surpris", 0.17), ("sael", "inquiet", 0.50), ("noam", "colere", 0.82)])
    mara surpris "Oh putain..."
    noam colere "Mara ! Dis-leur ! Tu sais très bien que je suis pas un imposteur !"
    mara inquiet "Je... Qu'est-ce qui s'est passé ici ?"
    noam panique "FAIS PAS SEMBLANT !"
    sael inquiet "Il faut arrêter de crier."
    noam colere "Toi, ferme-la ! Tu lui as planté une seringue dans le bras !"
    "Sael évite mon regard. Mara ne dit rien. Leur silence est pire qu'une accusation."
    $ showGroup([("ryn", "colere", 0.18), ("iris", "determine", 0.52), ("noam", "peur", 0.82)])
    ryn colere "On peut pas attendre. La navette arrive dans pas longtemps !"
    iris determine "Alors on l'attache. Après, on verra."
    noam peur "Non ! Iris, regarde-moi, putain, regarde-moi !"
    iris colere "Justement, je te regarde ! Et je vois quelqu'un qui ressemble à Noam et qui a poursuivi Julian dans les conduits !"
    noam panique "Je suis Noam !"
    "Plusieurs personnes s'avancent. Je recule jusqu'à la table, mais je ne peux pas fuir sans leur donner encore plus de raisons de croire que je mens."
    call impact_fx("brutal", direction="left")
    "Quelqu'un m'attrape les poignets. Je me débats, je cogne une chaise, et Ryn me plaque contre le bord de la table."
    noam colere "LÂCHEZ-MOI !"
    ryn colere "Alors arrête de te débattre !"
    "Je cherche mon double du regard. Il pourrait tout arrêter en une phrase."
    $ showGroup([("noam", "peur", 0.25), ("dg_noam", "fatigue", 0.77)])
    noam peur "Dis-leur. S'il te plaît. Dis-leur qui je suis."
    dg_noam fatigue "..."
    noam panique "T'as dit que tu me laisserais choisir ! Tu me l'as dit !"
    dg_noam inquiet "Je..."
    "Il baisse les yeux. Il ne dit rien d'autre."
    $ hideGroup()
    $ j30_julian_saved_exposed = True
    jump _30_0_1_1_0_0_1_0_EXCLUSION
    # Durée : 5m30

label _30_0_1_1_0_0_1_0_EXCLUSION:
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Oh ! Je vois que vous avez trouvé une façon particulièrement animée de passer votre dernier matin ! Deux Noam, et pas assez de places pour tout le monde. Quel embarras."
    $ bc_show("noam", "colere")
    noam colere "Kami ! Tu sais lequel est le vrai ! Dis-leur !"
    $ bc_hide()
    kami "Je pourrais vous faire une démonstration, mais vous êtes déjà très en retard sur votre programme. Et je ne vais tout de même pas gâcher votre départ avec une enquête interminable !"
    kami "Je vous rappelle que seuls les passagers identifiés par le groupe peuvent embarquer. Il semblerait que vous veniez de décider lequel des deux devait rester."
    $ bc_show("noam", "panique")
    noam panique "Tu peux pas les laisser faire ça !"
    $ bc_hide()
    kami "Je vous ai vus prendre tellement de décisions ensemble. Ce serait dommage de ne plus faire confiance à votre merveilleux esprit collectif maintenant !"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    "Les autres discutent à voix basse. Iris reste près de mon double. Julian se tient contre le mur, refusant toujours que qui que ce soit l'approche."
    $ showGroup([("noam", "peur", 0.18), ("lysa", "inquiet", 0.50), ("iris", "colere", 0.82)])
    lysa inquiet "On devrait au moins essayer de vérifier avant..."
    iris colere "L'embarquement va commencer ! Julian dit qu'il a failli mourir. Tu veux qu'on le laisse monter ?!"
    noam raison "Lysa ! Tu me connais, toi !"
    lysa inquiet "Je... je sais même plus ce que ça veut dire, Noam."
    "Cette réponse me coupe davantage que les cordes qu'on serre autour de mes poignets."
    noam peur "Iris, s'il te plaît. Juliette... Tu sais que je dois rentrer pour son anniversaire."
    iris fatigue "Arrête. C'est dégueulasse de te servir de sa sœur."
    noam panique "Mais c'est MA sœur !"
    "Le visage d'Iris se ferme. Elle se tourne vers l'autre Noam, comme si elle préférait ne plus m'entendre."
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Ils m'enferment finalement dans une chambre vide, les mains attachées à une barre métallique. Ils ont pris ma tablette, mais personne n'a remarqué le dessin plié dans ma poche."
    "Au-dessus de moi, les haut-parleurs crachent les dernières consignes d'embarquement."
    "J'essaie encore de défaire mes liens. Rien ne bouge."
    noam colere "HÉ ! Y A QUELQU'UN ?!"
    "Personne ne répond."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Dernier appel ! Tous les passagers sont priés de rejoindre la navette. Fermeture des portes dans quelques instants !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Un grondement traverse la station. Le sol vibre longuement, puis tout devient silencieux."
    "Ils sont partis."
    "Iris. Juliette, qui attend toujours que je rentre. Et mon double, qui va pouvoir se présenter chez elle avec mon visage."
    noam fatigue "Putain..."
    $ j30_julian_saved_exiled = True
    jump _30_0_1_1_0_0_1_0_LIBERATION
    # Durée : 2m

label _30_0_1_1_0_0_1_0_LIBERATION:
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    "J'ai perdu la notion du temps quand j'entends quelqu'un essayer d'ouvrir la porte. Je me redresse."
    noam inquiet "Qui est là ?"
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Julian entre. Pas celui qui m'a accusé : celui qui a été fabriqué hier, et qui a dû se cacher quand l'original est réapparu."
    $ showGroup([("noam", "inquiet", 0.24), ("julian", "inquiet", 0.76)])
    noam peur "Non... Toi, reste où t'es."
    julian inquiet "Eh, doucement ! Je suis pas venu te faire du mal. Je viens t'enlever ces trucs."
    noam colere "Pourquoi ? T'as pas pris la navette ?"
    julian fatigue "Bah non. Il y avait déjà un Julian au petit-déjeuner ! Tu voulais que j'aille lui serrer la main devant les autres ?"
    noam raison "Et tu savais que j'étais ici ?"
    julian reflexion "J'ai entendu ce qu'ils disaient avant de partir. J'étais planqué dans le laboratoire. Ils racontaient que le faux Noam avait essayé de tuer l'original."
    noam colere "Sauf que c'est moi, l'original !"
    julian reflexion "Ouais, j'ai compris. Tu crois que j'aurais pris le risque de venir sinon ?"
    "Il s'approche et commence à défaire les liens. Mes poignets me lancent dès que je peux bouger."
    noam inquiet "Mais pourquoi tu m'aides ? Tu sais même pas ce que j'ai fait."
    julian reflexion "J'ai appris que t'avais changé la seringue. Tu voulais pas qu'il meure."
    noam fatigue "Lui, il a pas voulu m'écouter."
    julian inquiet "Ouais. Je l'ai entendu, ça aussi."
    noam raison "Et toi, tu me crois ?"
    julian fatigue "Tu viens de te faire abandonner ici à cause de ça. Je vois pas bien pourquoi t'aurais inventé toute cette histoire."
    "Je frotte mes poignets sans rien répondre. Julian récupère la corde et la jette sur le lit."
    julian neutre "Bon, on fait quoi, maintenant ? J'ai pas vraiment prévu de passer le reste de ma vie dans cette station."
    $ hideGroup()
    "Des pas résonnent derrière la porte. Une silhouette entre, avec le visage de Nyra."
    $ showGroup([("noam", "inquiet", 0.17), ("julian", "inquiet", 0.48), ("nyra", "neutre", 0.82)])
    zero_nyra_j29 neutre "Je vois que tu l'as détaché. Bien."
    noam colere "Zero ?! Où t'étais, bordel ?!"
    zero_nyra_j29 neutre "J'essayais d'empêcher la situation d'empirer. Quand j'ai compris ce qui se passait, les autres avaient déjà fermé l'accès au sas."
    noam colere "Tu savais que c'était moi ! Tu pouvais les arrêter !"
    zero_nyra_j29 neutre "Je sais. J'aurais dû intervenir plus tôt. Je suis désolé."
    noam colere "Désolé ?! J'ai essayé de sauver Julian, et maintenant tout le monde me prend pour un imposteur !"
    julian agace "On va peut-être arrêter de se hurler dessus deux secondes ? La navette est déjà partie."
    zero_nyra_j29 neutre "Il reste un transport disponible. Celui qui doit me conduire sur Keyper-IIB."
    noam inquiet "Attends... Tu veux dire qu'on peut encore partir d'ici ?"
    zero_nyra_j29 neutre "Oui. Tous les trois. Je pensais partir seul, mais ce n'est plus possible de vous laisser ici."
    julian surpris "Keyper ? La planète dont ils parlaient au laboratoire ?"
    zero_nyra_j29 neutre "Celle-là. Vous serez en sécurité pendant le trajet. Après, je ne peux rien vous promettre."
    noam fatigue "Génial. On est trois, on a raté la Terre, et tu nous emmènes sur une planète où Kami fait bosser les gens de force."
    zero_nyra_j29 neutre "Je comprends que tu n'aies pas envie de me suivre. Mais je n'ai plus de navette pour la Terre."
    noam colere "Tu vois, hier tu me disais que j'avais le choix. Maintenant j'en ai plus."
    zero_nyra_j29 neutre "Oui. Et je regrette que ça se soit passé comme ça."
    julian reflexion "Bon. Moi, je veux juste quitter cet endroit. Si votre navette décolle, je viens."
    "Je regarde mon dessin de Juliette, froissé au fond de ma poche. Je le déplie sur mes genoux."
    noam fatigue "On part quand ?"
    zero_nyra_j29 neutre "Maintenant."
    $ hideGroup()
    jump _30_0_1_1_0_0_1_0_FIN
    # Durée : 3m

label _30_0_1_1_0_0_1_0_FIN:
    # CG 077 : dernier départ de Noam, Julian-DG et Zero vers Keyper-IIB.
    if renpy.loadable("images/background/cg/bg_cg077.png"):
        $ unlock_gallery_image("bg_cg077")
        scene bg_cg077 at adaptive_fullscreen with dissolve
    else:
        scene bg_navette at adaptive_fullscreen with dissolve
    "La petite navette s'éloigne du Conclave. Sur le siège à côté de moi, le double de Julian essaie de comprendre les commandes de son harnais. Zero reste debout près du poste de pilotage."
    "Par le hublot, la Terre n'est déjà plus qu'une direction sur l'écran de navigation."
    julian inquiet "Noam ?"
    noam fatigue "Quoi ?"
    julian reflexion "Merci. Pour ce que t'as fait hier. Même si c'est pas exactement moi que t'as sauvé."
    noam fatigue "Ouais... De rien."
    "Je regarde encore le dessin de Juliette. J'ai réussi à sauver Julian, mais celui qui rentre sur Terre avec ma sœur, c'est pas moi."
    think "Putain... Je sais même pas si je la reverrai."
    $ j30_julian_saved_ending = "prix_d_une_vie"
    scene black with fade
    stop music fadeout 0.2
    pause 1.2
    call screen kd_ending_reached(
        "Le prix d'une vie",
        "ENDING 05 // JOUR 30"
    )
    $ _ending_screen_closed = _return
    return
    # Durée : 1m30
