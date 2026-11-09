label _2_CANON:

    $ unlock_codex_page("propositions_amendement", with_notification=False)

    $ day_id = 2
    $ current_day = 2
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"

    scene black
    play music "music/main_menu.mp3" fadein 1.0

    pause 0.6

    think "J'ai dormi trois heures. Quatre, si je compte les moments où je fixais le plafond les yeux fermés."
        think "J'ai proposé un amendement hier. L'idée me paraissait brillante sur le papier. Maintenant, j'aimerais surtout récupérer ce papier."
    scene bg_cg012 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg012")
    $ blink()
    think "Je tends le bras vers l'horloge. Si elle indique encore six heures, je retourne sous la couette. Démocratie ou pas."

    play sound sfx_announce

    pause 0.8

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Ooooh, mes petits représentants ! Debout ! À moins que vous ne préfériez voter depuis vos oreillers ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ne répondez pas, vos brouilleurs sont encore allumés. J'adore vous parler quand je suis certaine d'avoir le dernier mot."
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Saviez-vous que le stress libère du cortisol ? C'est la petite voix chimique qui vous souffle : Ne dors surtout pas, ton voisin a peut-être un couteau."
    kami "Pratique face à un danger. Un peu moins quand on doit partager un couloir avec onze inconnus."
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Moi, je n'ai pas ce problème. Je ne dors jamais. Et je ne ronfle pas ! Avouez que je suis une colocataire parfaite."
    kami "Huit heures ! Vous avez une heure pour vous rendre présentables, avaler quelque chose et vous demander lequel de vous a écrit la pire bêtise. Rendez-vous à neuf heures à la cafétéria."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Et soyez à l'heure ! Je déteste qu'on fasse attendre une dame. Surtout moi."

    $ blink()
    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    # Réveil réel
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    think "Juliette serait déjà debout. Ma petite sœur ferait sûrement un commentaire désobligeant sur mes cheveux, puis me demanderait ce qu'on mange."
    think "Est-ce qu'elle a vu l'annonce ? Est-ce qu'elle me regarde maintenant ?"
        think "Je pourrais lui expliquer que tout va bien. Il suffirait de pouvoir l'appeler."
        think "Mais je n'en ai pas le droit."
        think "Alors je m'habille. C'est plus facile que de trouver une réponse."
    think "Neuf heures. Une heure avant de découvrir ce que nous avons offert à Kami. Je ferais bien de ne pas arriver en retard."

    stop music fadeout 1.0
    pause 0.6

    # Trajet jouable : chambre -> dortoir -> couloir -> cafétéria.
    $ day2_cafeteria_route_nyra_seen = False
    $ day2_cafeteria_route_tomas_seen = False
    $ current_scene_active = "_2_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    $ room_scene_indices["chambre"] = 2
    jump CHAMBRE_TP

# Durée : 2m35
# Total : 1h 7m 25s

label _2_CAFETERIA_ANNONCE_KAMI:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_145
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    pause 0.4

    think "J'entends la cafétéria avant d'en voir les tables. Une voix proteste. Une autre soupire. Parfait, ils sont réveillés."
    play sound sfx_door

    think "Je prends un plateau, trouve une place et tente l'exploit de manger sans me faire remarquer."


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "reflexion", 0.13),
        ("iris", "colere", 0.49),
        ("tomas", "neutre", 0.60),
        ("elen", "joie", 0.72),
        ("nyra", "taquin", 0.96),
        ("ryn", "neutre", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas hesitation "E-Excusez-moi... J'ai juste une question. Enfin, si on peut encore poser des questions..."
    tomas inquiet "On est vraiment obligés d'être tous là à neuf heures précises ? Je veux dire... si quelqu'un dort encore ?"

    iris desaccord "Bien sûr ! On va demander gentiment à l'IA qui nous séquestre de décaler son programme pour les gros dormeurs."
    iris colere "Un volontaire pour lui expliquer ? Personne ? Alors on mange."

    tomas panne "Je—"

    ryn neutre "Moi, je préférerais encore être dans mon lit. Ou dehors. Ou n'importe où, en fait."
    ryn reflechit "Ça fait deux jours que je cherche à comprendre ce que j'ai fait pour mériter ça."

    elen content "Oh !"
    elen joie "C'est vraiii que l'ambiance est un peu... comment dire... funèbre ?"
    elen surpris "Oh ! Mais faut voir le bon côté des choses !"
    elen joie "Alors j'ai décidé qu'on allait commencer par quelque chose d'important : vous avez goûté le petit-déjeuner ?"

    iris desaccord "Incroyable. On a une crise existentielle à table et toi, tu notes le buffet."
    iris colere "Tu comptes proposer une sauce pour accompagner notre exécution aussi ?"

    elen desaccord "Ah non ! Surtout pas piquante ! Je supporte pas ça !"
    elen content "Allez, souriez un peu ! Ça ne va pas vous tuer !"
        iris blase "Une affirmation dangereuse, ici."
        elen peur "Oh... c'était une expression !"
        noam sourire "Pour une fois, je crois qu'Iris plaisantait."
        iris desaccord "J'ai dit ça, moi ?"
    
    ryn fatigue "Je sais pas ce qui est le pire : cette station ou ton enthousiasme."

    pause 0.4

    elias ecoute "… Façon on peut rien faire d'autre que d'attendre. Donc ça sert à rien de se prendre la tête avec ça."
    elias neutre "Ça se trouve, on va tomber sur un texte génial. Un truc évident auquel personne n'avait pensé."

    sael raison "Il a raison sur un point : rien ne sert de discuter le ventre vide."
    sael mefiant "Quant au texte... on verra bien. Mais gardez les yeux ouverts."

    pause 0.6

    play sound sfx_door
    think "La porte s'ouvre."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("iris", "colere", 0.49),
        ("tomas", "panne", 0.60),
        ("elen", "content", 0.72),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])

    mara taquin "Vous organisez une cérémonie d'enterrement ou un petit-déjeuner ? On vous entend depuis le couloir."
    mara neutre "À droite, ceux qui veulent paniquer. À gauche, ceux qui veulent manger. Je peux m'asseoir avec les gens normaux ?"

    nyra taquin "Tu as vraiment pris le temps d'écouter avant d'entrer ?"

    elen joie "Mara ! Viens ici ! Il reste de la place, et je te promets qu'on ne parle pas QUE de mourir !"

    mara taquin "Adorable invitation, mais d'ici je vois tout le monde. Et je préfère voir venir les mauvaises surprises."
    elen joie "Moi je préfère voir les desserts !"
    mara sourire "Au moins, on est deux à avoir des priorités."
    nyra neutre "Ne vous y trompez pas, elle regarde les gens pour savoir qui aura le dernier mot."
    mara taquin "C'est plus divertissant que le menu."

    pause 0.4

    ryn neutre "Si tu pouvais regarder ton assiette à la place, ça nous ferait des vacances."

    pause 0.6

    play sound sfx_door


    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "colere", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "triste", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "panne", 0.60),
        ("elen", "joie", 0.72),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])

    lysa blase "Quoi ? J'ai raté l'exécution collective ? Ah non. Bonjour."
    noam sourire "On t'a gardé une place."
    lysa blase "Vraiment ? C'est presque gentil."
    noam taquin "Tu peux toujours me la rendre."
    lysa sourire "J'y réfléchirai."

    tomas inquiet "N-Non non !"
    tomas hesitation "Enfin... je crois. Personne n'a annoncé de sanction pour cinq minutes, si ?"

    iris taquin "Félicitations, Lysa. Tu as survécu à ton entrée dans une pièce."
    iris taquin "Ça m'évite surtout d'avoir à ramasser quelqu'un avant le café."

    lysa reflexion "On dirait surtout qu'il manque encore notre vedette habituelle."

    noam reflexion "Espérons qu'ils se dépêchent."

    play sound sfx_door

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "colere", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "hesitation", 0.60),
        ("elen", "joie", 0.72),
        ("kael", "neutre", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "desaccord", 1.20),
    ])

    kael neutre "J'ai couru pour rien ? Dites-moi que je suis pas le dernier."

    iris colere "Ça suffit, les entrées dramatiques. Quelqu'un a un compteur de retardataires ?"
    iris desaccord "Non ? Alors on arrête de jouer à l'appel et on attend Kami."

    play sound sfx_announce

    pause 2.0

    stop music fadeout 0.8

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Aaaah, mes petits survivants du petit-déjeuner ! Vous avez des mines superbes. Enfin... pour des gens qui pensent tous à leur testament."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Il est neuf heures ! Onze représentants à l'heure... Nous sommes presque au complet. Presque."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je pourrais attendre notre retardataire. Après tout, quel beau geste démocratique ! Mais non. Il n'avait qu'à se lever."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "La petite urne a parlé ! Votre premier amendement est sorti. Et je dois dire... il a beaucoup de personnalité. Enfin, grammaticalement parlant."
    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn neutre "T'accouches, oui ?!"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quelle délicatesse ! Une seconde, je déplie ce chef-d'œuvre."
    play sound sfx_tambour
    pause 0.8

    kami "Je cite : « ça serait bien qu'on réautorise le commerce comme avant. »"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Alors. Je ne vais pas vous demander lequel d'entre vous a écrit ça. L'anonymat, c'est sacré ! Mais je recommande vivement un dictionnaire à l'auteur."
    kami "Réautoriser le commerce, donc. Une phrase minuscule pour une pagaille potentiellement gigantesque !"

    pause 0.8

    $ bc_show("sael", "surpris", px=-70, py=-50, pz=0.85)
    sael triste "Le commerce... Comme avant ? Avant quoi, exactement ?"

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra taquin "Je crois que quelqu'un vient de proposer de refaire toute l'économie mondiale en douze mots."

    $ bc_show("iris", "triste", px=-70, py=-50, pz=0.85)
    iris colere "Pour une fois, je m'attendais à pire. Le problème, c'est qu'on n'a toujours aucune idée de ce qu'on vote."
    $ bc_hide()

    pause 0.6

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "JE PEUX TERMINER MA PHRASE, OU VOUS AVEZ DÉJÀ OUVERT VOTRE PROPRE PARLEMENT ?!"
    think "Le silence s'abat sur la salle. Même le bruit des couverts s'arrête. C'est impressionnant, tout ce qu'on peut obtenir en hurlant depuis un écran."
    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vote demain, quatorze heures ! Oui, c'est court. Vous avez perdu une journée à vous réveiller et à vous demander où étaient les toilettes."
    kami "Et n'oubliez pas : un seul vote contre suffit à tout envoyer à la poubelle. L'unanimité, c'est tellement reposant."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Discutez ! Convainquez ! Pleurez ! Faites-vous de nouveaux amis ou perdez les anciens. Je prends tout !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Moi, je vais devoir mettre ça en français correct. Je refuse d'inscrire « ça serait bien » dans mes merveilleux Commandements."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Amusez-vous bien, mes petits législateurs. Et souriez : le monde vous écoute."

    hide screen kami_broadcast_ui
    stop music fadeout 1.0

    pause 0.8
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("mara", "neutre", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("iris", "colere", 0.49),
        ("tomas", "inquiet", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "neutre", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "determine", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    elen joie "Mais... c'est super, non ?! On pourrait enfin choisir ce qu'on achète ! Des fraises ! Des vraies fraises !"
    iris taquin "Et voilà. Elle a entendu commerce, elle a vu un rayon pâtisserie."
    elen content "Pas seulement ! Des légumes aussi ! Et des livres ! Et... attendez, ça veut dire qu'on pourrait faire des courses pour de vrai ?"
    sael reflechit "Et avec quel argent, exactement ?"
    elen inquiet "Bah... on pourrait inventer des tickets ?"
    iris blase "Félicitations, tu viens de réinventer les bons de rationnement."
    elen desaccord "Non, mais des tickets jolis !"
    sael neutre "On ne résout pas une pénurie en décorant du papier."
    think "Elle a lâché ça avec un tel sérieux qu'Elen reste bouche bée."
    elen surpris "Ah. Oui. C'est un détail assez important, ça."
    "Elen baisse les yeux vers son plateau, puis se met à rire de sa propre remarque."
    elias sourire "Moi, si je pouvais enfin acheter des pièces détachées sans remplir trois formulaires, je signerais avant même le petit-déjeuner."
    mara neutre "Avec quel salaire ? Parce que j'ai raté le moment où on nous a rendu nos comptes en banque."
    elias reflechit "Justement ! Je répare des machines toute la journée et je touche plus rien depuis Kami. Tu trouves ça normal ?"
    noam surpris "Tu répares tout ça... sans être payé ?"
    elias neutre "Ouais. À la Forge, une machine cassée ne se remet pas à marcher parce qu'on a supprimé les salaires. Si je la laisse, plus personne n'a ce qu'il lui faut."
    mara reflechit "Tu veux pouvoir acheter les pièces... pour pouvoir continuer à travailler gratuitement. C'est une belle arnaque, ton truc."
    elias gene "Euh... dit comme ça..."
    mara sourire "Tu vois ? Tu devrais presque voter contre."
    elias inquiet "Mais non ! Je..."
    noam sourire "Mara, laisse-le finir."
    mara taquin "Je l'aide à réfléchir. C'est un service public."
    elias taquin "Oui, mais des boulons neufs ! Ça change tout !"
    "Mara esquisse un sourire. De l'autre côté de la table, Tomas essaie d'ouvrir un emballage qui refuse obstinément de céder."
    tomas inquiet "Euh... l'emballage... il y a une languette quelque part ? J'ai peur de tout renverser."
    iris blase "Tomas. On est censés débattre du commerce mondial. Tu peux gagner ton combat contre une brioche, non ?"
    "Iris lui prend le paquet et l'ouvre d'un geste. Elen éclate de rire lorsque quelques miettes tombent sur la table."
    ryn reflechit "Vous avez fini avec les viennoiseries ? Parce qu'on ne sait même pas ce que cette règle nous autoriserait vraiment."
    nyra neutre "La formulation compte autant que l'intention. Avec une phrase aussi vague, Kami peut faire presque ce qu'elle veut."
    ryn colere "Donc on vote pour quoi ? Ce qu'elle décide ?!"
    nyra reflexion "On devrait attendre le texte final."
    mara taquin "Ça fera un beau slogan : votons demain, comprenons après."
    noam reflexion "J'espère quand même qu'on aura le temps de le lire."
    mara taquin "Oh, ça, j'ai entièrement confiance en elle. Pour nous la faire à l'envers, elle est excellente."
    noam reflexion "La question, c'est ce qu'elle va écrire à la place. « Comme avant », ça veut dire quoi pour douze personnes qui n'ont pas connu le même avant ?"
    "La discussion se calme pendant quelques instants. Je commence enfin mon petit-déjeuner, pendant qu'Elen demande à Goumi s'il serait capable de lui préparer un dessert avec les ingrédients disponibles."
    pause 0.5

    play sound sfx_door
    "La porte s'ouvre brusquement. Julian entre sans attendre la fin de la discussion."
    $ showGroup([
        ("elias", "rire", -0.11),
        ("mara", "fatigue", 0.01),
        ("noam", "reflexion", 0.13),
        ("lysa", "blase", 0.25),
        ("julian", "taquin", 0.37),
        ("iris", "colere", 0.49),
        ("tomas", "inquiet", 0.60),
        ("elen", "content", 0.72),
        ("kael", "neutre", 0.84),
        ("nyra", "taquin", 0.96),
        ("ryn", "reflechit", 1.08),
        ("sael", "mefiant", 1.20),
    ])
    julian rire "Bonjour, mes chers collègues ! Je vois que le débat a eu la courtoisie de commencer sans moi."
    iris colere "Tu es en retard. Et ton entrée ne te donne pas droit à une deuxième séance d'ouverture."
    julian sourire "Laisse-moi deviner. Un projet de réouverture du commerce ?"
    elen surpris "Oh ! T'es devin ?!"
    julian taquin "Disons que certains sujets trouvent naturellement les grands esprits."
    elias taquin "Ou alors t'as juste entendu Kami depuis le couloir."
    julian panne "Elias ! Deux secondes. Je demandais deux secondes de mystère !"
    lysa blase "Deux secondes, ça passe. À la troisième, on te fait payer l'entrée."

    $ j2_vote_codex_unlocked = True
    think "Ma tablette vibre. « Nouveau dossier de vote ». Parfait. La conversation s'annonce encore plus légère."

    jump _2_CAFETERIA_POST_ANNONCE

# Durée : 3m35
# Total : 1h 11m 0s

label _2_CAFETERIA_POST_ANNONCE:

    show screen day2_quick_vote_notes


    "Les tablettes des autres se mettent à sonner à leur tour."
    think "J'ouvre le dossier de vote reçu à l'instant. Pour l'instant, il reprend surtout la courte proposition que Kami vient de nous lire."
    elias inquiet "Merde ! Ma tablette... Elle est restée dans ma chambre. Kael, je peux voir la tienne ?"
    kael reflechit "Y a presque rien. Juste la proposition, sans les précisions. Un devoir rendu sans les annexes."
    julian sourire "Justement ! On pourrait profiter du déjeuner pour comparer nos idées. Une discussion structurée, chacun son tour..."
    lysa blase "Tu viens d'entrer et tu veux déjà diriger les débats ? Laisse-moi finir ma tartine avant d'élire un président."
    julian taquin "Je proposais seulement qu'on soit efficaces. Mais si ça vous effraie autant que ça..."
    "Julian se sert un verre d'eau pendant que les conversations reprennent, beaucoup moins sérieusement qu'avant."
    elen surpris "Sael ! Chez toi, vous faites comment si vous voulez quelque chose que vous n'avez pas ? Du troc ?"
    sael neutre "On produit ce qu'on peut. On partage ce qui manque. Ce n'est pas toujours facile, mais personne n'a besoin de faire une offre pour mériter son repas."
    elen joie "C'est comme une immense colocation ! Avec des champs !"
    sael sourire "On appelle ça un village, oui. Au pied du mont Kensen."
    ryn reflechit "Kensen ? Je connais ce nom. Tu viens vraiment de là-bas ?"
    sael neutre "J'y ai grandi. Aujourd'hui, j'en suis responsable."
    elen surpris "Attends... c'est toi la cheffe ?! Mais tu travailles dans les champs !"
    sael sourire "La terre ne se cultive pas depuis une chaise. Et les autres n'auraient aucune raison de m'écouter si je ne faisais rien."
    noam sourire "Ça explique pourquoi tu as toujours l'air d'attendre que quelqu'un fasse une bêtise."
    sael reflechit "On s'est longtemps débrouillés seuls. Depuis la fermeture des passages, les bandes armées ne viennent plus jusqu'à nous. Ça, au moins, on ne peut pas le nier."
    ryn colere "Ah ouais ? Chez nous, il y a des gens qui meurent en essayant de franchir ces foutues frontières. Tu veux qu'on les remercie, aussi ?"
    sael mefiant "Je n'ai pas dit que la fermeture était juste pour tout le monde. J'ai dit que les attaques avaient cessé chez nous. Ce n'est pas la même chose."
    ryn colere "C'est pratique, de pouvoir parler de paix quand on est du bon côté de la barrière !"
    sael colere "Et tu crois que je ne sais pas ce que c'est, de perdre des gens ?"
    ryn colere "Alors ne me parle pas comme si cette frontière nous avait tous sauvés !"
    elen peur "Hé... On peut se calmer ?"
    sael mefiant "Je ne t'ai pas demandé d'être d'accord. Je te demande d'écouter."
    think "Personne n'élève plus la voix. Le silence n'a rien réglé."
    "Ryn repousse légèrement sa chaise. Je crois qu'il va partir, mais il reprend sa tasse et reste assis."
    elias reflechit "Et moi je parlais de boulons, il y a cinq minutes... J'ai l'air malin."
    mara neutre "Voilà pourquoi je me méfie des propositions qui tiennent sur une serviette. Chacun entend ce qui l'arrange."
    nyra neutre "On aura un texte rédigé par Kami avant le vote. C'est ce texte-là qu'il faudra juger, pas nos souvenirs du commerce."
    iris fatigue "Formidable. Maintenant que vous avez fini de régler les problèmes du monde, je peux réchauffer mon repas ?"
    elen content "Moi, j'aimerais bien visiter ton village ! Enfin... quand on aura le droit de quitter cette boîte."
    sael sourire "Si tu veux."
    "La conversation part sur les montagnes de Limen, puis sur les réparations qu'Elias a déjà dû faire avec du matériel de récupération. Ryn parle peu, mais il écoute."
    "Je finis tranquillement mon repas. On n'est pas d'accord sur grand-chose pour le moment, mais j'ai au moins appris des choses sur les autres."
    $ unlock_codex_page("commerce_monnaie", with_notification=False)

    $ unlock_codex_page("commerce_monnaie", with_notification=False)


    $ hideGroup()

    think "Je termine mon repas au milieu des reproches et des bruits de couverts. Ryn est parti, mais la dispute a laissé une place vide à table."

    stop music fadeout 0.8
    pause 0.6

    hide screen day2_quick_vote_notes

    think "Je quitte la cafétéria. Si je veux comprendre ce texte avant demain, il va falloir écouter les autres autrement qu'au milieu d'une bagarre de table."

    call START_FREE_TIME("_2_APRES_MIDI") from _call_START_FREE_TIME

# Durée : 3m50
# Total : 1h 14m 50s

# Freetimde :
# Durée : 1m30
# Total : 1h 16m 20s

label _2_APRES_MIDI:

    $ current_period = "Après-midi"
    $ day2_sync_argument_titles()
    $ day2_observation_route_mara_seen = False
    $ day2_observation_route_lysa_seen = False
    $ day2_observation_route_elen_seen = False
    $ day2_observation_route_sael_seen = False
    $ current_scene_active = "_2_ROUTE_OBSERVATION"
    $ corridor_current = "dortoir"

    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    show screen day2_quick_vote_notes

    think "J'ai besoin de marcher. Et, surtout, d'arrêter d'entendre « comme avant » dans ma tête."
    think "La salle d'observation est à l'autre bout de la station. Ça me laisse le temps d'écouter les autres... ou de fuir les conversations, pour une fois."

    jump OPEN_CONCLAVE_MAP


label _2_APRES_MIDI_MARA_SAEL:

    $ day2_observation_route_mara_seen = True
    scene expression Image(corridor_background("dortoir")) at adaptive_fullscreen with dissolve

    $ showGroup([
        ("mara", "neutre", 0.15),
        ("noam", "reflexion", 0.50),
        ("sael", "mefiant", 0.65),
    ])

    mara mefiant "Tu crois vraiment qu'on va poser nos petits bulletins dans l'urne et rentrer sagement au lit ? Elle va trouver un moyen de nous piéger."

    sael mefiant "Kami n'a même pas besoin de nous pousser. Il lui suffit de nous regarder avoir peur les uns des autres."

    mara taquin "C'est fascinant. Même quand tu me donnes raison, tu trouves le moyen de me déprimer."
    sael neutre "Je ne cherche pas à te rassurer. Je préfère que tu fasses attention."

    think "Mara regarde Sael, qui ne rajoute rien."

    mara stress "Bon... je vais peut-être arrêter de plaisanter cinq minutes."
    mara doute "À plus tard. Sauf si tout nous explose à la figure avant."


    $ hideGroup()
    return


label _2_APRES_MIDI_LYSA_ELIAS:

    $ day2_observation_route_lysa_seen = True
    scene expression Image(corridor_background("dortoir")) at adaptive_fullscreen with dissolve

    think "Lysa est adossée au mur, Elias face à elle."

    $ showGroup([
        ("elias", "neutre", -0.11),
        ("lysa", "triste", 0.25),
    ])

    elias ecoute "T'as pas dit grand-chose ce matin. Pourtant, hier, tu parlais tout le temps."
    lysa blase "J'ai écouté. Ça change."
    elias sourire "Bah, ça te ressemble pas."
    lysa neutre "Merci, c'est gentil."
    think "Je les rejoins. Lysa me laisse une place près du mur."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "inquiet", 0.13),
        ("lysa", "triste", 0.25),
    ])
    noam inquiet "T'es préoccupée par le vote ?"
    lysa reflexion "Ouais. Tout le monde parle de son district, mais quand on parle d'Harmonie, on passe pour les bureaucrates qui font chier tout le monde."
    noam raison "On pourra leur dire ce qui nous manque."
    lysa blase "Ils le savent. Si les marchandises sont vendues au plus offrant, on sera encore les derniers servis."
    elias ecoute "Ah ouais. Moi, je pensais surtout aux pièces détachées."
    lysa taquin "C'est pour ça que je t'aime bien. Toi, tu penses d'abord aux boulons."
    elias rire "Au moins, les boulons, ça répond pas !"
    noam sourire "Et tu vas le dire demain ?"
    lysa determine "Je vais essayer. J'ai pas envie qu'on décide à ma place."

    call day2_collect_vote_argument("approvisionnement") from _call_day2_collect_vote_argument_approvisionnement

    think "Je note l'inquiétude de Lysa dans mon dossier de vote."

    $ hideGroup()
    return


label _2_APRES_MIDI_ELEN:

    $ day2_observation_route_elen_seen = True
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("elen", "content", 0.68),
    ])

    noam surpris "Tu fais quoi avec tous ces papiers ?"
    elen content "Je voulais juste commander des fraises au distributeur. Ils ont une liste de trucs trop bien !"
    noam neutre "Et tout ça, c'est pour des fraises ?"
    elen inquiet "Oui ! Je dois expliquer pourquoi la ration normale me suffit pas, combien j'en veux et qui va les manger."
    noam taquin "Elles seront pourries avant qu'on t'autorise à les prendre."
    elen desaccord "Mais oui ! Et c'est pareil pour les outils. J'ai regardé au cas où je casse un truc dans ma chambre."
    noam raison "Même quand c'est disponible, tu dois remplir toute la demande ?"
    elen joie "Voilà ! Tu comprends ! Tu veux signer comme témoin pour mes fraises ?"
    noam sourire "Euh... peut-être plus tard."
    $ unlock_codex_page("derogations_administratives", with_notification=False)

    call day2_collect_vote_argument("derogations_complexes") from _call_day2_collect_vote_argument_derogations_complexes

    $ hideGroup()
    jump CAFETERIA_TP


label _2_APRES_MIDI_SAEL:

    $ day2_observation_route_sael_seen = True
    scene expression Image(corridor_background("infirmerie")) at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "neutre", 0.30),
        ("sael", "raison", 0.68),
    ])

    noam neutre "Tu disais que chez toi, vous vous débrouilliez sans commerce. Ça marche vraiment ?"
    sael raison "On mange ce qu'on produit. Chacun s'occupe de quelque chose : les champs, les réparations, les enfants."
    noam reflexion "Et si quelqu'un ne peut pas travailler ?"
    sael neutre "On l'aide. Pourquoi voudrais-tu qu'on le laisse tomber ?"
    noam sourire "Non, je demandais."
    sael determine "Mais quelqu'un qui peut aider et refuse de le faire, je vais le chercher moi-même."
    noam taquin "Tu dois être convaincante."
    sael sourire "En général, oui."
    noam raison "Je comprends pourquoi tu ne t'inquiètes pas des mêmes choses que Mara."
    sael mefiant "Je m'inquiète aussi. Je veux juste qu'on ne nous impose pas la façon de vivre des autres."

    call day2_collect_vote_argument("valeur_travail") from _call_day2_collect_vote_argument_valeur_travail

    $ hideGroup()
    return

# Durée : 1m50
# Total : 1h 18m 10s

label _2_SALLE_OBSERVATION:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_148
    scene bg_observation at adaptive_fullscreen with dissolve

    think "Derrière la baie vitrée : le vide, immense et calme. Kael est déjà là."

    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam neutre "Kael, tu sais où on est exactement ?"
    kael neutre "Non. Mais je reconnais le matériel d'Orbite."
    noam raison "Tu dois te sentir chez toi, alors."
    kael doute "Pas vraiment. Cette station a été préparée à l'avance et personne ne m'en a parlé."
    noam inquiet "Tu crois qu'elle avait prévu nos amendements aussi ?"
    kael reflechit "Nos textes, non. Nos réactions, peut-être."
    noam taquin "Tu vas me rendre parano."
    kael calme "Désolé. Ça fait beaucoup de surprises en deux jours."

    pause 0.6

    play sound sfx_announce
    pause 0.8

    stop music fadeout 0.6
    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Petite annonce, l'un d'entre vous m'a demandé l'heure du vote demain."
    kami "Le vote aura lieu demain à quatorze heures. Soyez ponctuels."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Profitez bien de votre douce nuit de réflexion."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8


    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam inquiet "Quatorze heures. Ça nous laisse pas beaucoup de temps."
    kael mefiant "Non, surtout si personne ne veut changer d'avis."
    noam inquiet "Et toi, tu pourrais voter contre ?"
    kael raison "Je ne sais pas. Orbite dépend de ses livraisons pour presque tout. Acheter ce qu'il nous manque, ça m'intéresse."
    kael reflechit "Mais plus on fait venir de marchandises, plus il y a de contrôles et de risques d'erreur."
    noam surpris "Je vois pas où tu veux en venir."
    kael inquiet "Les sanctions de Kami. Sur Terre, vous avez peur pour la personne qu'elle vise. Sur Orbite, le tir peut aussi traverser la coque d'un module."
    noam peur "Attends, l'air peut s'échapper ?!"
    kael triste "Oui. On a des masques partout, mais il suffit d'une brèche qu'on ne peut pas fermer pour que tout le monde soit en danger."
    noam colere "Mais pourquoi Kami tire si elle sait que ça peut tuer des innocents ?!"
    kael fatigue "Elle répond que c'est à nous d'éviter les infractions."
    noam inquiet "T'as déjà vu ça arriver ?"
    kael triste "J'ai aidé à fermer un compartiment après une dépressurisation. Deux personnes étaient encore derrière la porte."
    noam peur "Elles ont pu sortir ?"
    kael triste "Non. Et si on avait attendu, on aurait perdu tout le module."
    "Kael s'arrête de parler et regarde dehors. Je ne sais pas quoi lui répondre."
    noam triste "Je suis désolé. Je savais pas."
    kael calme "Je sais. Mais demain, pense aussi aux gens qui vivent ici."
    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement
    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite
    kael fatigue "Je dois aller vérifier les relevés des consoles. À plus tard."
    $ hideGroup()
    think "Je reste quelques minutes devant la vitre. Deux personnes sont mortes parce que quelqu'un d'autre avait enfreint une règle. J'ai du mal à me sortir ça de la tête."
    think "En passant devant le gymnase, j'entends Elias compter à voix haute et Iris l'engueuler. Je décide d'entrer pour faire autre chose que ruminer."

    jump _2_GYMNASE

# Durée : 2m15
# Totale : 1h 20m 25s

label _2_GYMNASE:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_150
    scene bg_gymnase at adaptive_fullscreen with dissolve

    think "Le bruit régulier des machines couvre presque les pensées. Iris enchaîne les répétitions ; Elias, lui, les compte."

    $ showGroup([
        ("iris", "determine", 0.49),
        ("elias", "neutre", -0.11),
    ])

    iris determine "Encore. Tant que mes muscles brûlent, mon cerveau ferme enfin sa gueule."

    elias ecoute "Attends. Respire. Sinon tu vas te fatiguer pour rien."

    think "Je m'approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "hesitation", 0.13),
        ("iris", "determine", 0.49),
    ])


    noam hesitation "Je dérange ?"

    iris taquin "Pas tant que tu ne prends pas ma place et que tu ne te blesses pas de façon stupide. J'ai déjà assez de travail."

    elias ecoute "Non. Tu tombes bien."
    elias joie "Tu veux apprendre ? Ouais ! J'peux te montrer."

    noam surpris "Euh… Je crois ?"

    iris determine "Alors bouge au lieu de me mater. Il y a des bancs libres."

    elias joie "Celui-là. Regarde, assieds-toi. On va faire un truc simple pour le début."

    think "Le métal est froid sous mon dos."

    elias raison "Stop, tu vas te bousiller le dos ! Souffle quand tu pousses. Voilà, doucement."

    iris taquin "Tu lui fais commencer par du développé couché dès la première séance ? Excellent. Le spectacle sera amusant !"

    noam inquiet "Je tremble déjà rien que d'y penser."

    elias ecoute "Regarde. Vas-y doucement et laisse pas tomber la barre."

    think "Je soulève. Ouh ! C'est beaucoup plus lourd que prévu."

    elias ecoute "Pas comme ça. Va moins vite. Descends pas trop vite."

    think "Je recommence. Oh putain ça brûle."

    iris fatigue "Voilà."

    elias ecoute "Encore deux séries. Après tu peux t'arrêter."

    elias ecoute "Allez, encore deux et tu poses la barre. Je suis là si tu lâches."
    noam inquiet "Tu m'avais promis un truc simple !"
    iris taquin "C'est trop compliqué ? Je vais chercher les petits haltères roses."

    noam reflexion "Un… Deux… Allez Noam !"

    $ mg_skip_scene_pick = True
    call minijeu_halteres from _call_minijeu_halteres

    think "Je repose et récupère l'usage de mes poumons."
    $ mg_skip_scene_pick = False

    pause 0.6

    elias joie "Tu sens tes muscles ? C'est ça qu'on aime. La sensation de toujours faire mieux ! Mais le sport, ça se perd vite, alors refais-en souvent !"
    elias raison "Si tu reviens de temps en temps, tu verras, ça ira mieux."

    iris determine "Et parfois, c'est juste pour ne pas rentrer et tout casser."
    iris taquin "La fonte, ça coûte moins cher qu'un psy et ça pose moins de questions idiotes."

    pause 0.4

    noam neutre "J'ai les bras complètement morts."
    elias joie "C'est normal. Tu recommenceras quand t'auras récupéré."
    iris sourire "Et évite de te plaindre toute la soirée. On t'a pas forcé."
    noam sourire "Pas forcé ? Vous avez même pas attendu ma réponse !"
    elias rire "T'es toujours vivant. C'est déjà une bonne séance, non ?"
    noam taquin "Je vais surtout essayer de tenir ma fourchette ce soir."

    $ hideGroup()

    think "Je quitte la salle. Les machines continuent, régulières et implacables."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_infirmerie", "couloir_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_151
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    think "L'heure tourne. Mon estomac me ramène à la cafétéria."

    jump _2_CAFETERIA_SOIR

# Durée : 1m50
# Totale : 1h 22m 15s

label _2_CAFETERIA_SOIR:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_152
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ current_period = "Soir"

    $ showGroup([
        ("noam", "inquiet", 0.13),
        ("kael", "neutre", 0.33),
        ("tomas", "neutre", 0.54),
        ("elen", "content", 0.75),
        ("nyra", "taquin", 0.96),
    ])

    think "Lorsque j'arrive à la cafétéria, Nyra est en pleine discussion sur sa vie à Orbite."

    nyra sourire "À Orbite, les repas étaient plus calmes. Vous parlez toujours autant à Harmonie ?"
    noam sourire "Pas à ce point. Là, ça fait deux jours qu'on est enfermés ensemble."
    elen joie "Moi je trouve ça sympa ! Enfin, quand personne ne crie."
    kael neutre "Chez nous, il fallait surtout manger vite pour laisser la place à l'équipe suivante."
    elen surpris "Vous flottez pendant les repas ? Genre la soupe, elle vole partout ?"
    kael sourire "Non, Elen. On a une gravité artificielle et on attache les plateaux quand il le faut."
    elen content "Ah, dommage ! J'aurais adoré essayer."
    tomas hesitation "C'est bizarre de se dire qu'on pourrait changer votre vie demain, alors que je connais presque rien d'Orbite."
    nyra neutre "On peut t'en parler, mais pas tout expliquer en une soirée."
    noam inquiet "Kael m'a raconté ce qui arrive quand un tir perce un module. J'arrête pas d'y penser."
    kael fatigue "Je voulais pas te gâcher le dîner."
    noam neutre "C'est pas toi qui l'as gâché."
    elen inquiet "Et nos familles, elles nous regardent peut-être maintenant..."
    elen joie "D'ailleurs, vous avez goûté la purée ? Ils ont mis quelque chose de différent dedans !"
    nyra taquin "Je crois surtout qu'on l'a laissée refroidir."
    tomas sourire "Pour une fois, voilà un sujet sur lequel on peut être tous d'accord."
    think "Elen se met à comparer les assiettes, pendant que Kael lui explique comment ils préparent la nourriture sur Orbite."

    think "D'autres se joignent à nous. Questions, souvenirs, comparaisons puis la fatigue finit par dissoudre le débat."

    stop music fadeout 1.0
    pause 0.6
    hide screen day2_quick_vote_notes

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_153
    scene couloir_cafeteria at adaptive_fullscreen with fade
    pause 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("dortoir", "bg_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_154
    scene bg_dortoir at adaptive_fullscreen with fade
    pause 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_155
    scene bg_chambre at adaptive_fullscreen with fade
    pause 1.0

    think "Je passe par les douches."

    scene bg_cg011 at adaptive_fullscreen with fade

    think "Je reste sous la douche plus longtemps que prévu. Je repense à ce que Kael m'a raconté."

    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    scene bg_chambre at adaptive_fullscreen with fade
    think "Je me sèche et tombe sur le lit."
    
    scene bg_cg012 at adaptive_fullscreen with fade
    think "Demain à quatorze heures, on vote. J'espère qu'on arrivera au moins à s'écouter."

    $ blink()

    think "Je ferme les yeux."
    think "Et j’essaie de dormir."

    # jump patreon_ending

    call end_day("3", sleeping=True) from _call_end_day_23

    jump _3_CANON


# Durée : 1m55
# Totale : 1h 24m 10s
default j2_wakeup_trace_attempts = 0
default j2_vote_codex_unlocked = False
default j2_vote_arguments = []
default day2_observation_route_mara_seen = False
default day2_observation_route_lysa_seen = False
default day2_observation_route_elen_seen = False
default day2_observation_route_sael_seen = False
default j2_vote_positions = {
    "lysa": "unknown",
    "elias": "unknown",
    "kael": "unknown",
    "mara": "unknown",
    "julian": "unknown",
    "iris": "unknown",
    "elen": "unknown",
    "ryn": "unknown",
    "sael": "unknown",
    "tomas": "unknown",
    "nyra": "unknown",
}

init 3 python:
    DAY2_VOTE_COLUMNS = [
        ("for", "POUR"),
        ("unknown", "INCONNU"),
        ("against", "CONTRE"),
    ]

    DAY2_VOTE_ARGUMENTS = {
        "approvisionnement": {
            "title": "Inégalités entre les districts",
            "category": "Risque économique",
            "summary": "Les districts n'affrontent ni les mêmes pénuries ni les mêmes chances d'accéder aux biens.",
            "origin": "Entendu lors d'un échange avec Lysa et Elias.",
        },
        "rationnement": {
            "title": "Bons de rationnement",
            "category": "Organisation quotidienne",
            "summary": "Les demandes officielles et les bons structurent déjà l'accès aux biens essentiels.",
            "origin": "Relevé dans la discussion avec Kael.",
        },
        "orbite": {
            "title": "Risque de dépressurisation",
            "category": "Sécurité",
            "summary": "Sur Orbite, une sanction qui perce une coque peut condamner tout un module.",
            "origin": "Décrit par Kael en salle d'observation.",
        },
        "derogations_complexes": {
            "title": "Dérogations trop complexes",
            "category": "Accès administratif",
            "summary": "Obtenir une nourriture originale ou un objet utile exige une dérogation disproportionnée.",
            "origin": "Découvert en parlant avec Elen à la cafétéria.",
        },
        "valeur_travail": {
            "title": "Valeur du travail",
            "category": "Organisation collective",
            "summary": "L'entraide protège chacun, mais elle repose sur la contribution de tous ceux qui peuvent travailler.",
            "origin": "Expliqué par Sael à partir de la vie de son village.",
        },
    }

    DAY2_ARGUMENT_TITLE_ALIASES = {
        "Difficulté d'approvisionnement": "Inégalités entre les districts",
        "Faiblesse d'Orbite": "Risque de dépressurisation",
    }

    DAY2_VOTE_CHARACTER_ORDER = ["lysa", "elias", "kael", "mara", "julian", "iris", "elen", "ryn", "sael", "tomas", "nyra"]
    DAY2_VOTE_CHARACTERS = {
        "lysa": {"name": "Lysa", "portrait": "images/character/lysa/portrait.png"},
        "elias": {"name": "Elias", "portrait": "images/character/elias/portrait.png"},
        "kael": {"name": "Kael", "portrait": "images/character/kael/portrait.png"},
        "mara": {"name": "Mara", "portrait": "images/character/mara/portrait.png"},
        "julian": {"name": "Julian", "portrait": "images/character/julian/portrait.png"},
        "iris": {"name": "Iris", "portrait": "images/character/iris/portrait.png"},
        "elen": {"name": "Elen", "portrait": "images/character/elen/portrait.png"},
        "ryn": {"name": "Ryn", "portrait": "images/character/ryn/portrait.png"},
        "sael": {"name": "Sael", "portrait": "images/character/sael/portrait.png"},
        "tomas": {"name": "Tomas", "portrait": "images/character/tomas/portrait.png"},
        "nyra": {"name": "Nyra", "portrait": "images/character/nyra/portrait.png"},
    }

    def day2_vote_argument_count():
        day2_sync_argument_titles()
        return len(store.j2_vote_arguments)

    def day2_sync_argument_titles():
        changed = False
        if persistent.unlocked_arguments is None:
            persistent.unlocked_arguments = []
            changed = True
        if persistent.unlocked_vote_argument_ids is None:
            persistent.unlocked_vote_argument_ids = []
            changed = True
        if persistent.unlocked_dossier_args is None:
            persistent.unlocked_dossier_args = []
            changed = True
        for old_title, new_title in DAY2_ARGUMENT_TITLE_ALIASES.items():
            if old_title in store.arguments:
                store.arguments.remove(old_title)
                if new_title not in store.arguments:
                    store.arguments.append(new_title)
            if old_title in persistent.unlocked_arguments:
                persistent.unlocked_arguments.remove(old_title)
                if new_title not in persistent.unlocked_arguments:
                    persistent.unlocked_arguments.append(new_title)
                changed = True

        for arg_id in persistent.unlocked_vote_argument_ids:
            if arg_id in DAY2_VOTE_ARGUMENTS and arg_id not in store.j2_vote_arguments:
                store.j2_vote_arguments.append(arg_id)
                changed = True

        for arg_id in persistent.unlocked_dossier_args:
            if arg_id in DAY2_VOTE_ARGUMENTS and arg_id not in store.j2_vote_arguments:
                store.j2_vote_arguments.append(arg_id)
                changed = True

        # Compatibilité des sauvegardes ayant débloqué le titre avant l'ID.
        for arg_id, arg_data in DAY2_VOTE_ARGUMENTS.items():
            if arg_data["title"] in store.arguments or arg_data["title"] in persistent.unlocked_arguments:
                if arg_id not in store.j2_vote_arguments:
                    store.j2_vote_arguments.append(arg_id)
                if arg_id not in persistent.unlocked_dossier_args:
                    persistent.unlocked_dossier_args.append(arg_id)
                    changed = True
        for arg_id in getattr(store, "j2_vote_arguments", []):
            if arg_id in DAY2_VOTE_ARGUMENTS:
                title = DAY2_VOTE_ARGUMENTS[arg_id]["title"]
                if title not in store.arguments:
                    store.arguments.append(title)
                if title not in persistent.unlocked_arguments:
                    persistent.unlocked_arguments.append(title)
                    changed = True
                if arg_id not in persistent.unlocked_vote_argument_ids:
                    persistent.unlocked_vote_argument_ids.append(arg_id)
                    changed = True
                if arg_id not in persistent.unlocked_dossier_args:
                    persistent.unlocked_dossier_args.append(arg_id)
                    changed = True
                    if hasattr(store, "dossier_unlocked_args"):
                        store.dossier_unlocked_args[arg_id] = True
        if changed:
            renpy.save_persistent()

    def day2_vote_add_argument(arg_id):
        if arg_id not in DAY2_VOTE_ARGUMENTS:
            return False
        day2_sync_argument_titles()
        title = DAY2_VOTE_ARGUMENTS[arg_id]["title"]
        if title not in store.arguments:
            store.arguments.append(title)
        # Persistance globale (conservée entre parties/sauvegardes).
        if persistent.unlocked_arguments is None:
            persistent.unlocked_arguments = []
        if persistent.unlocked_vote_argument_ids is None:
            persistent.unlocked_vote_argument_ids = []
        if persistent.unlocked_dossier_args is None:
            persistent.unlocked_dossier_args = []
        if title not in persistent.unlocked_arguments:
            persistent.unlocked_arguments.append(title)
        if arg_id not in persistent.unlocked_vote_argument_ids:
            persistent.unlocked_vote_argument_ids.append(arg_id)
        if arg_id not in persistent.unlocked_dossier_args:
            persistent.unlocked_dossier_args.append(arg_id)
        if arg_id not in store.j2_vote_arguments:
            store.j2_vote_arguments.append(arg_id)
        if "unlock_dossier_arg" in globals():
            unlock_dossier_arg(arg_id)
        renpy.save_persistent()
        chapter1_check_complete_dossier()
        renpy.restart_interaction()
        return True

    def day2_vote_position_dragged(char_id, drags, drop):
        if drop is None:
            renpy.restart_interaction()
            return
        target = getattr(drop, "drag_name", "")
        if target.startswith("day2_vote_col_"):
            store.j2_vote_positions[char_id] = target.replace("day2_vote_col_", "")
        renpy.restart_interaction()

    def day2_vote_card_xy(char_id):
        col = store.j2_vote_positions.get(char_id, "unknown")
        col_index = {"for": 0, "unknown": 1, "against": 2}.get(col, 1)
        items = [cid for cid in DAY2_VOTE_CHARACTER_ORDER if store.j2_vote_positions.get(cid, "unknown") == col]
        idx = items.index(char_id) if char_id in items else 0
        return (48 + col_index * 340 + (idx % 2) * 154, 72 + (idx // 2) * 132)

    def day2_argument_drop(drags, drop, arg_id):
        if drop is not None and getattr(drop, "drag_name", "") == "day2_briefcase_drop":
            return bool(day2_vote_add_argument(arg_id))
        # L'échec du dépôt replace la carte au départ et garde l'écran ouvert.
        renpy.restart_interaction()
        return False


# La zone de dépôt est déclarée AVANT la carte dans le draggroup.
# Ainsi la carte reste visible au premier plan quand les deux se chevauchent.
transform day2_folder_idle_glow:
    alpha 0.14
    ease 0.85 alpha 0.43
    ease 0.85 alpha 0.14
    repeat

transform day2_argument_success_fly:
    xpos 290 ypos 380 zoom 1.0 alpha 1.0
    pause 0.08
    easein 0.42 xpos 1155 ypos 423 zoom 0.30
    ease 0.14 alpha 0.0

transform day2_argument_success_label:
    alpha 0.0
    pause 0.61
    ease 0.20 alpha 1.0

# Une carte réutilisée telle quelle pour le drag et l'animation finale.
screen day2_argument_visual(arg):
    fixed:
        xysize (490, 275)
        add Solid("#00000066") xpos 9 ypos 10 xsize 478 ysize 264
        add Solid("#102637") xpos 0 ypos 0 xsize 480 ysize 265
        add Solid("#70DFFF") xpos 0 ypos 0 xsize 480 ysize 3
        add Solid("#70DFFF") xpos 0 ypos 0 xsize 3 ysize 265
        add Solid("#70DFFF") xpos 477 ypos 0 xsize 3 ysize 265
        add Solid("#70DFFF") xpos 0 ypos 262 xsize 480 ysize 3
        add Solid("#1B4258") xpos 18 ypos 17 xsize 444 ysize 44
        text "ARGUMENT":
            xpos 32 ypos 25
            size 21 color "#9FEAFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 2
        text kd_tr(arg["title"]):
            xpos 30 ypos 85
            xsize 419 ysize 124
            size 36 color "#F3FAFF"
            font "fonts/Rajdhani-SemiBold.ttf"
        add Solid("#31566B") xpos 30 ypos 222 xsize 417 ysize 1
        text "DOSSIER DU VOTE":
            xpos 30 ypos 233
            size 19 color "#87B7CA"
            font "fonts/Rajdhani-SemiBold.ttf"

# Réceptacle : un seul grand dossier, sans double panneau emboîté.
screen day2_argument_folder_visual():
    fixed:
        xysize (650, 350)
        add Solid("#14374733") xpos 17 ypos 30 xsize 610 ysize 274 at day2_folder_idle_glow
        add Transform("gui/day3/argument_briefcase_open.png", xysize=(630, 320), fit="contain"):
            xpos 10 ypos 0
        text "DÉPOSER ICI":
            xpos 0 ypos 313 xsize 650
            text_align 0.5
            size 23 color "#A3EFFF"
            font "fonts/Rajdhani-SemiBold.ttf"
            kerning 2

screen vote_argument_briefcase(arg_id, argument_data, card_drag_name, drop_drag_name, drop_handler):
    modal True
    zorder 180
    $ arg = argument_data

    add Solid("#020710EF")
    frame:
        xpos 275 ypos 166 xsize 1370 ysize 94
        padding (26, 17)
        background Solid("#071522F1")
        vbox:
            spacing 5
            text "KAMI.CORE  //  DOSSIER DU VOTE":
                size 16 color "#64B9D2"
                kerning 2 font "fonts/Rajdhani-SemiBold.ttf"
            text "Classe cet argument dans ton dossier de vote.":
                size 29 color "#E7F6FF"
                font "fonts/Rajdhani-SemiBold.ttf"

    text "ARGUMENT DÉCOUVERT":
        xpos 290 ypos 326
        size 21 color "#84CDE4"
        kerning 2 font "fonts/Rajdhani-SemiBold.ttf"
    text "PROCHAIN VOTE":
        xpos 1065 ypos 326
        size 21 color "#84CDE4"
        kerning 2 font "fonts/Rajdhani-SemiBold.ttf"

    add Solid("#4C829B66") xpos 825 ypos 517 xsize 145 ysize 2
    text "›":
        xpos 892 ypos 472
        size 68 color "#8CE7FF"
        font "fonts/Rajdhani-SemiBold.ttf"

    draggroup:
        # D'abord la cible, ensuite la carte : empilement corrigé.
        drag:
            drag_name drop_drag_name
            xpos 985 ypos 368
            xsize 650 ysize 350
            draggable False
            droppable True
            use day2_argument_folder_visual

        drag:
            drag_name card_drag_name
            xpos 285 ypos 373
            xsize 490 ysize 275
            draggable True
            droppable False
            drag_raise True
            dragged (lambda drags, drop, arg_id=arg_id, drop_handler=drop_handler: drop_handler(drags, drop, arg_id))
            use day2_argument_visual(arg)

# L'argument se range dans le dossier, puis la confirmation disparaît
# automatiquement, sans clic de validation supplémentaire.
screen day2_argument_deposit_success(arg):
    modal True
    zorder 185
    key "game_menu" action NullAction()
    add Solid("#020710F2")
    text "KAMI.CORE  //  DOSSIER DU VOTE":
        xpos 275 ypos 180
        size 22 color "#8DBDD0"
        font "fonts/Rajdhani-SemiBold.ttf"
    fixed:
        xpos 985 ypos 368
        xysize (650, 350)
        use day2_argument_folder_visual
    fixed at day2_argument_success_fly:
        xysize (490, 275)
        use day2_argument_visual(arg)
    text "ARGUMENT ENREGISTRÉ" at day2_argument_success_label:
        xalign 0.5 ypos 795
        size 33 color "#6AE7BA"
        font "fonts/Rajdhani-SemiBold.ttf"
        kerning 2
    timer 1.35 action Return(True)

screen day2_quick_vote_notes():
    pass

screen day2_current_vote_codex():
    tag menu
    modal True
    zorder 200

    add Solid("#080d12")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1720
        ysize 960
        padding (28, 24)
        background Solid("#07151ef5")

        vbox:
            spacing 18
            hbox:
                xfill True
                vbox:
                    spacing 4
                    text "Codex" size 22 color "#3a9fca"
                    text "Prochain vote" size 48 color "#daeaf5" font "fonts/Rajdhani-SemiBold.ttf"
                textbutton "Retour":
                    xalign 1.0
                    yalign 0.5
                    xsize 150
                    background Solid("#1a2530")
                    hover_background Solid("#2d3a45")
                    text_color "#dff8ff"
                    action Return()

            hbox:
                spacing 22

                frame:
                    xsize 480
                    yfill True
                    padding (22, 18)
                    background Solid("#0d2230")
                    vbox:
                        spacing 12
                        text "Vote en cours" size 30 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        text "Ça serait bien qu'on réautorise le commerce comme avant." size 22 color "#dff8ff"
                        text "Moment prévu : Jour 3, 14h00" size 19 color "#9ed8ff"
                        text "Résumé neutre" size 21 color "#70c6e8"
                        text "Le texte promet une circulation plus libre des biens. Ses effets restent incertains selon les districts, les procédures et les risques locaux." size 20 color "#b8d8e4"
                        null height 8
                        text "Arguments découverts" size 24 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                        for arg_id in ["approvisionnement", "rationnement", "orbite", "derogations_complexes", "valeur_travail"]:
                            if arg_id in j2_vote_arguments:
                                $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
                                frame:
                                    xfill True
                                    padding (12, 10)
                                    background Solid("#123044")
                                    vbox:
                                        spacing 3
                                        text kd_tr(arg["title"]) size 21 color "#ffffff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text kd_tr(arg["summary"]) size 17 color "#b8d8e4"
                                        text kd_tr(arg["origin"]) size 15 color "#74a8ba"
                            else:
                                frame:
                                    xfill True
                                    padding (12, 12)
                                    background Solid("#111820")
                                    text "Argument non découvert" size 18 color "#526d79"

                fixed:
                    xfill True
                    yfill True

                    draggroup:
                        for cidx, col_data in enumerate(DAY2_VOTE_COLUMNS):
                            $ col_id = col_data[0]
                            $ col_label = col_data[1]
                            drag:
                                drag_name ("day2_vote_col_%s" % col_id)
                                draggable False
                                droppable True
                                xpos (20 + cidx * 340)
                                ypos 0
                                xsize 318
                                ysize 810
                                frame:
                                    xfill True
                                    yfill True
                                    padding (14, 14)
                                    background Solid("#0c1d29")
                                    vbox:
                                        spacing 8
                                        text kd_tr(col_label) xalign 0.5 size 28 color "#dff8ff" font "fonts/Rajdhani-SemiBold.ttf"
                                        text "Glisse les portraits ici." xalign 0.5 size 16 color "#6797aa"

                        for cid in DAY2_VOTE_CHARACTER_ORDER:
                            $ card_x, card_y = day2_vote_card_xy(cid)
                            $ cdata = DAY2_VOTE_CHARACTERS[cid]
                            drag:
                                drag_name ("day2_vote_char_%s" % cid)
                                xpos card_x
                                ypos card_y
                                xsize 142
                                ysize 116
                                draggable True
                                droppable False
                                dragged (lambda drags, drop, cid=cid: day2_vote_position_dragged(cid, drags, drop))
                                frame:
                                    xfill True
                                    yfill True
                                    padding (7, 7)
                                    background Solid("#182d3a")
                                    vbox:
                                        spacing 3
                                        add cdata["portrait"] xalign 0.5 xysize (62, 62)
                                        text "[cdata['name']]" xalign 0.5 size 17 color "#dff8ff"

screen day2_argument_briefcase(arg_id):
    $ arg = DAY2_VOTE_ARGUMENTS[arg_id]
    use vote_argument_briefcase(arg_id, arg, "day2_argument_card", "day2_briefcase_drop", day2_argument_drop)

label day2_play_wakeup_trace:
    call trace_qte_run(mg_id="trace_day2_wakeup", title="RÉVEIL — JOUR 2", path_type="curve_right", time_limit=6.0, wait_time=1.2, tolerance=55, max_errors=4, anchor_x=960, anchor_y=620, required=True) from _call_trace_qte_run_2
    return True

label day2_collect_vote_argument(arg_id):
    call screen day2_argument_briefcase(arg_id)
    if _return:
        play sound sfx_drop
        call screen day2_argument_deposit_success(DAY2_VOTE_ARGUMENTS[arg_id])
    return

# Durée de la 2e journée de jeu : 16m de jeu
# Total J0-J1 : 1h 8m
