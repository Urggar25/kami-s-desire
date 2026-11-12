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

    elias ecoute "T'étais bizarrement silencieuse ce matin. Hier, tu arrivais à me répondre avant même que je finisse une phrase."
    lysa blase "J'ai écouté. Expérience nouvelle. Je recommande une fois par trimestre."
    elias sourire "T'as dû être très malade."
    lysa neutre "Merci, docteur. Ton diagnostic me touche."
    think "Je les rejoins. Lysa me laisse une place près du mur."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "inquiet", 0.13),
        ("lysa", "triste", 0.25),
    ])
    noam inquiet "C'est le commerce qui t'inquiète, ou les gens qui vont voter ?"
    lysa reflexion "Les deux. Tout le monde défend son district. Mais dès qu'on parle d'Harmonie, on devient les bureaucrates qui empêchent les autres de vivre."
    noam raison "On peut leur expliquer ce qui nous manque. Ils ne savent pas forcément."
    lysa blase "Ils savent qu'on a des pénuries. Le problème, c'est que si tout se vend au plus offrant, on sera toujours les derniers à recevoir ce qu'il reste."
    elias ecoute "Ah. J'avais pas vu ça comme ça. Moi, je pensais juste... aux pièces détachées."
    lysa taquin "Je sais. Et c'est pour ça que je t'apprécie : tu pourrais assister à la fin du monde et demander où sont les écrous."
    elias rire "Oui ! Les écrous, au moins, me disent pas que je suis stupide."
    noam sourire "Alors dis-le demain. Pas à nous, à tout le monde."
    lysa determine "Je compte bien le faire. Ce qui me fait peur, c'est de finir par voter pour un texte dont personne ne connaît le prix."
    elias reflechit "On pourrait écrire toutes ces questions dans le dossier. Comme ça, au moins, on oublie pas."
    lysa taquin "Tu vois ? Les boulons, ça sert aussi à réfléchir."
    elias rire "Je vais faire semblant de prendre ça pour un compliment."
    think "Une idée simple, mais la première qui me semble réellement utile depuis ce matin."

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

    noam surpris "Attends... tu prépares un amendement ou tu déclares tes revenus ?"
    elen content "Je voulais des fraises ! Ils en ont ! J'ai vu la liste, je te jure !"
    noam neutre "Et ces quatre feuilles, c'est pour... un bol de fraises ?"
    elen inquiet "Oui ! Il faut dire pourquoi j'en veux, combien, quand je vais les manger et si quelqu'un d'autre va en profiter !"
    noam taquin "À ce rythme-là, elles auront fini leur carrière de fraises avant la réponse."
    elen desaccord "Mais c'est ça ! Et c'est pareil pour un outil ! Si je casse une lampe, je dois presque raconter toute ma vie pour demander un tournevis."
    noam raison "Même si l'objet est juste là, sous tes yeux ?"
    elen joie "OUI ! Tu comprends enfin ! Tu veux être mon témoin ? Je promets de partager !"
    noam taquin "Je n'ai pas encore accepté !"
    elen inquiet "Mais je peux mettre ton prénom au crayon, si tu veux."
    noam sourire "Surtout pas."
    elen content "Bon... je vais écrire « témoin potentiel »."
    think "J'aurais dû partir avant qu'elle sorte son stylo."
    noam sourire "J'ai comme l'impression que je vais finir accusé de trafic de fruits."
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

    noam neutre "Sael, chez toi, le commerce a vraiment disparu sans que le village s'effondre ?"
    sael raison "On mange ce qu'on produit. Les uns travaillent la terre, les autres réparent les machines, d'autres s'occupent des enfants. Ce n'est pas une formule magique."
    noam reflexion "Et ceux qui ne peuvent pas travailler ?"
    sael neutre "On les aide. Tu pensais qu'on les laissait sans manger ?"
    noam sourire "Non ! Je voulais juste comprendre."
    sael determine "En revanche, si quelqu'un peut donner un coup de main et préfère regarder les autres s'épuiser, je vais le chercher. Personnellement."
    noam taquin "Je commence à avoir pitié de ses excuses."
    sael sourire "Il n'en trouve pas longtemps."
    noam raison "Je comprends pourquoi un retour du commerce ne te paraît pas forcément une bonne nouvelle."
    sael mefiant "Je m'inquiète, crois-moi. Simplement, je refuse qu'une règle écrite ici détruise ce qu'on a construit là-bas."

    call day2_collect_vote_argument("valeur_travail") from _call_day2_collect_vote_argument_valeur_travail

    $ hideGroup()
    return

# Durée : 1m50
# Total : 1h 18m 10s

label _2_SALLE_OBSERVATION:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_148
    scene bg_observation at adaptive_fullscreen with dissolve

    think "La Terre flotte derrière la vitre, impassible. Kael contemple les consoles. Il a l'air d'attendre qu'une machine lui explique pourquoi nous sommes ici."

    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam neutre "Tu as reconnu la station ? Ou tu viens ici pour être tranquille ?"
    kael neutre "Je reconnais les équipements. Pas la station. Et crois-moi, ça fait une sacrée différence."
    noam raison "Ça doit quand même te rassurer, non ?"
    kael doute "Pas tellement. Construire un endroit pareil sans qu'aucune équipe d'Orbite n'en entende parler... c'est loin d'être rassurant."
    noam inquiet "Tu crois que Kami savait d'avance ce qu'on allait écrire ?"
    kael reflechit "Les textes ? Je sais pas. Mais nos réactions... On est peut-être moins originaux qu'on l'imagine."
    noam taquin "Merci. J'étais venu pour me détendre."
    kael calme "Désolé. C'est mon problème : quand je ne comprends pas une machine, je suppose d'abord qu'elle cache quelque chose."

    pause 0.6

    play sound sfx_announce
    pause 0.8

    stop music fadeout 0.6
    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Petite annonce ! Puisque quelqu'un a réussi l'exploit de me demander trois fois la même heure, je répète pour les distraaaaits !"
    kami "Le vote aura lieu demain à quatorze heures. Quatorze ! Deux heures après midi ! Et non, je ne fais pas de calendrier personnalisé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Profitez de votre adorable soirée de réflexion. Je sais que vous allez dormir comme des bébés... des bébés très inquiets."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8


    $ showGroup([
        ("noam", "neutre", 0.13),
        ("kael", "neutre", 0.84),
    ])

    noam inquiet "Demain quatorze heures... Même si on voulait comparer tous les risques, on n'aurait pas le temps."
    kael mefiant "On pourrait avoir un mois, ça ne servirait à rien si chacun s'est déjà décidé."
    noam inquiet "Alors toi... tu voterais contre ?"
    kael raison "Je ne sais pas. Sur Orbite, on dépend des livraisons. Un commerce plus libre pourrait nous sauver des semaines d'attente."
    kael reflechit "Mais chaque cargaison, c'est aussi des contrôles, des opérations et des occasions de faire une erreur."
    noam surpris "Une erreur de livraison ? C'est si grave que ça ?"
    kael inquiet "Sur Terre, quand Kami sanctionne quelqu'un, tu vois surtout la cible. Ici, un tir peut traverser la coque d'un module. Et l'espace se moque de savoir qui est innocent."
    noam peur "Attends... tu veux dire qu'on peut perdre tout l'air d'un coup ?!"
    kael triste "Oui. On a des masques, des cloisons, des procédures. Mais une brèche qui reste ouverte, et tout le compartiment devient un piège."
    $ close_up("noam")
    noam colere "Mais elle le sait ! Pourquoi tirer si elle peut tuer ceux qui n'ont rien fait ?!"
    kael fatigue "Sa réponse est toujours la même : il fallait empêcher l'infraction. Comme si on avait tous le contrôle sur les autres."
    noam inquiet "Tu parles comme si tu avais déjà vu ça."
    kael triste "Une fois, on a dû fermer une cloison après une dépressurisation. J'ai aidé à actionner la fermeture."
    kael triste "Il y avait encore deux personnes de l'autre côté."
    noam peur "Elles... elles sont sorties, après ?"
    kael triste "Non."
    noam inquiet "Mais... personne n'a essayé de les..."
    kael triste "On a essayé. Jusqu'à ce que l'alarme de pression ne nous laisse plus le choix."
    think "Je ne trouve pas de phrase qui ne sonne pas creux."
    kael fatigue "Si on avait attendu quelques secondes de plus, on aurait perdu le module entier."
    "Kael s'arrête de parler et regarde dehors. Je ne sais pas quoi lui répondre."
    noam triste "Je... je savais pas. Désolé."
    kael calme "Je sais. Alors demain, quand tu entendras « commerce », essaie aussi de penser aux gens qui vivent derrière ces cloisons."
    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement
    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite
    kael fatigue "Je dois aller vérifier les relevés des consoles. À plus tard."
    $ hideGroup()
    think "La Terre semble si tranquille derrière la vitre. Je revois Kael fermer une cloison, deux personnes de l'autre côté. Il n'a pas raconté leurs visages. Je les imagine quand même."
    think "Au détour du couloir, j'entends Elias compter, puis Iris lui aboyer dessus. Pour une fois, une dispute serait presque rassurante."

    jump _2_GYMNASE

# Durée : 2m15
# Totale : 1h 20m 25s

label _2_GYMNASE:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_150
    scene bg_gymnase at adaptive_fullscreen with dissolve

    think "Le gymnase sent le métal et la sueur. Iris pousse une charge comme si elle voulait la punir. Elias compte avec le sérieux d'un contrôleur d'ascenseur."

    $ showGroup([
        ("iris", "determine", 0.49),
        ("elias", "neutre", -0.11),
    ])

    iris determine "Encore ! Tant que ça brûle, au moins mon cerveau arrête de me refaire la journée."

    elias ecoute "Doucement ! Respire ! Tes muscles n'ont rien fait pour mériter ça."

    think "Je m'approche."
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "hesitation", 0.13),
        ("iris", "determine", 0.49),
    ])


    noam hesitation "Je dérange une séance de torture ou je peux entrer ?"

    iris taquin "Tu dérangeras quand tu te seras blessé en essayant de nous impressionner. Pour l'instant, entre."

    elias ecoute "Oh ! Tu tombes très bien, justement."
    elias joie "Tu veux essayer ? Allez, je te montre ! Promis, je commence facile."

    noam surpris "Attends, j'ai dit ça, moi ?"

    iris determine "Alors arrête de nous regarder comme une attraction touristique et choisis un banc."

    elias joie "Celui-là ! Assieds-toi. On va commencer avec quelque chose de simple. Enfin... simple pour commencer."

    think "Le métal est froid sous mon dos."

    elias raison "Stop ! Si tu cambres comme ça, demain tu me demanderas de réparer ta colonne vertébrale. Respire et pousse doucement."

    iris taquin "Du développé couché pour sa première séance ? Excellent. Elias, t'es sûr que tu veux pas directement lui faire soulever le gymnase ?"

    noam inquiet "J'ai encore rien fait et mes bras veulent déjà rentrer se coucher."

    elias ecoute "Concentre-toi sur la barre. Et surtout, ne la lâche pas. Je tiens à garder mes doigts."

    think "Je pousse. La barre bouge. Mon âme, elle, reste coincée sur le banc."

    elias ecoute "Moins vite ! Pas besoin de battre un record. On essaie juste de survivre à une série."

    think "Je recommence. Les muscles qui me servaient à ouvrir une porte viennent de déclarer leur indépendance."

    iris fatigue "Voilà."

    elias ecoute "Encore deux séries et tu auras mérité une vraie pause !"

    elias ecoute "Allez ! Encore deux répétitions, et je te laisse respirer. Je suis là si tu flanches."
    noam inquiet "Tu m'avais promis une initiation ! Pas une tentative de meurtre !"
    iris taquin "Oh, le pauvre. Je peux te chercher les haltères roses, si tu veux. Il y a des petits cœurs dessus."
    elias gene "Ils sont pas là pour décorer, les petits haltères..."
    iris blase "Je sais. C'était une plaisanterie."
    noam inquiet "Merci, Elias. Je commençais à croire que tu étais de son côté."
    elias sourire "Je suis du côté de ta colonne vertébrale."

    noam reflexion "Un... deux... Je refuse de me faire humilier par un morceau de fer !"

    $ mg_skip_scene_pick = True
    call minijeu_halteres from _call_minijeu_halteres

    think "Je repose la barre. Il me faut quelques secondes pour retrouver l'existence de mes bras... et de mes poumons."
    $ mg_skip_scene_pick = False

    pause 0.6

    elias joie "Tu sens ?! Ça, c'est le progrès ! Enfin... la douleur, c'est pas automatiquement du progrès. Mais tu t'es débrouillé !"
    elias raison "Reviens de temps en temps. Avec de l'entraînement, on pourra même discuter pendant que tu pousses."

    iris determine "Ou tu viens ici simplement parce que tu as envie de casser quelque chose et qu'on préfère te laisser une barre."
    iris taquin "La fonte ne te demande pas comment tu te sens. C'est son principal avantage."

    pause 0.4

    noam neutre "J'ai des bras en coton. On peut les échanger contre des neufs ?"
    elias joie "Demain, tu vas découvrir des muscles dont tu ignorais l'existence !"
    iris sourire "Et pas de plainte ce soir. Tu es entré de ton plein gré."
    noam sourire "Tu m'as déjà condamné aux haltères avant que j'aie dit oui !"
    elias rire "Regarde le positif : tu peux toujours marcher !"
    noam taquin "On en reparle quand j'essaierai de porter ma fourchette."

    $ hideGroup()

    think "Je sors du gymnase avec les bras d'une marionnette mal assemblée. Derrière moi, Iris a déjà recommencé une série."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_infirmerie", "couloir_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_151
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    think "Mon estomac me rappelle qu'il existe encore une activité physique à ma portée : manger."

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

    think "Je reviens à la cafétéria. Mes bras protestent dès que j'essaie de tenir le plateau. À une table, Nyra raconte quelque chose qui a l'air de passionner Elen."

    nyra sourire "À Orbite, on pouvait finir un repas sans qu'il se transforme en débat. Vous parlez toujours autant, à Harmonie ?"
    noam sourire "Non. C'est un effet secondaire de trente jours d'enfermement avec des inconnus."
    elen joie "Moi j'adore ! Enfin, sauf quand quelqu'un crie ou menace de partir. Ou quand on parle de cadavres."
    kael neutre "Chez nous, il fallait surtout se dépêcher. Une équipe finissait, la suivante prenait la place. Pas de place pour les grands discours."
    elen surpris "Attendez. Vous mangez en flottant ?! Ça veut dire que vos soupes font des petites bulles ?"
    kael sourire "On a une gravité artificielle, Elen. Et on fixe les plateaux quand c'est nécessaire. Sinon, je te garantis qu'on mangerait moins de soupe."
    elen content "C'est nul ! Je voulais voir une purée faire un looping !"
    kael sourire "Je peux te garantir que ce serait surtout un cauchemar à nettoyer."
    nyra taquin "Et nous voilà revenus aux problèmes les plus importants d'Orbite."
    noam sourire "Je crois que j'ai raté le début de cette réunion scientifique."
    tomas hesitation "On est en train de décider de ce que vous pourrez acheter, mais... je sais même pas comment vous mangez. Ça me paraît un peu inquiétant."
    nyra neutre "On peut t'expliquer. Mais pas en un repas. Tu veux commencer par les rations ou les filtres à air ?"
    noam inquiet "Kael m'a raconté ce qui arrive quand une sanction perce la coque. J'arrive pas à me sortir ça de la tête."
    kael fatigue "J'espérais ne pas remettre ça sur la table ce soir."
    noam neutre "T'as rien gâché. C'est moi qui ai posé la question."
    elen inquiet "Vous pensez que nos familles nous voient, en ce moment ? Parce que si oui, j'espère qu'elles ne croient pas qu'on s'amuse vraiment."
    elen joie "Oh ! Attendez, vous avez goûté la purée ? Je suis sûre qu'ils ont changé la recette !"
    nyra taquin "Je crois surtout qu'elle a eu le temps de refroidir pendant notre conversation sur le vide spatial."
    tomas sourire "Il paraît qu'on cherche une raison de voter à l'unanimité. On pourrait commencer par la purée."
    elen joie "Moi je vote pour !"
    kael calme "Je m'abstiens. Je n'ai pas encore lu la recette."
    nyra sourire "Un vrai parlement, finalement."
    think "Je ris avec eux. Ça ne dure pas longtemps, mais ça fait du bien."
    think "Elen examine les assiettes comme un jury gastronomique. Kael essaie de lui expliquer la préparation des repas sur Orbite sans qu'elle lui demande si les pommes de terre flottent."

    think "Les conversations se mélangent. Un souvenir de la Terre, une question sur Orbite, une plaisanterie. Pendant quelques minutes, personne ne parle du vote."

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

    think "Je file sous la douche avant que mes bras ne refusent définitivement de bouger."

    scene bg_cg011 at adaptive_fullscreen with fade

    think "L'eau chaude calme mes épaules. Mais l'histoire de Kael revient. Une porte qu'on ferme. Deux personnes de l'autre côté."

    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    scene bg_chambre at adaptive_fullscreen with fade
    think "Je m'écroule sur le lit avec l'élégance d'un meuble qu'on renverse."
    
    scene bg_cg012 at adaptive_fullscreen with fade
    think "Demain, quatorze heures. Une phrase mal écrite va peut-être changer la vie de millions de gens."
    think "Ryn voit une frontière. Sael voit son village. Elias voit des pièces détachées. Kael voit une coque percée."
    think "Et moi ?"
    think "Moi, je ne sais même pas si on parle tous de la même chose."

    $ blink()

    think "Je ferme les yeux. Cette fois, ce n'est pas la voix de Kami qui m'empêche de dormir."
    think "C'est la question que personne n'a encore posée : à qui profitera vraiment notre vote ?"

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
