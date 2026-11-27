default day2_route_gym_mara_tomas_seen = False
default day2_route_gym_elen_sael_seen = False
default day2_route_dinner_lysa_seen = False

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
    $ kd_queue_character_motion("iris", "exasperation")
    iris colere "Un volontaire pour lui expliquer ? Personne ? Alors on mange."

    tomas panne "Je—"

    ryn neutre "Moi, je préférerais encore être dans mon lit. Ou dehors. Ou n'importe où, en fait."
    ryn reflechit "Ça fait deux jours que je cherche à comprendre ce que j'ai fait pour mériter ça."

    elen content "Oh !"
    elen joie "C'est vraiii que l'ambiance est un peu... comment dire... funèbre ?"
    $ kd_queue_character_motion("elen", "surprise")
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

    nyra taquin "Il reste une place là, Mara. Assieds-toi avant que quelqu'un te demande ton avis."

    elen joie "Mara ! Viens ici ! Il reste de la place, et je te promets qu'on ne parle pas QUE de mourir !"

    mara taquin "Adorable invitation, mais d'ici je vois tout le monde. Et je préfère voir venir les mauvaises surprises."
    elen joie "Moi je préfère voir les desserts !"
    mara sourire "Au moins, on est deux à avoir des priorités."
    nyra neutre "Elle a déjà repéré les gens les plus susceptibles de se disputer."
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
    nyra taquin "Douze mots pour refaire tout le commerce mondial. Tomas, tu peux garder une copie du texte ? Il va falloir qu'on le relise."

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
    "Elias revient du comptoir avec une tasse fumante. Il la pose à côté de deux gobelets déjà vides."
    noam surpris "Attends. C'est ton troisième ?"
    elias sourire "Ouais. Pourquoi ?"
    noam "On est même pas à midi."
    elias reflechit "Et ?"
    mara taquin "Laisse, Noam. Si tu lui prends sa tasse, il va se mettre à réparer la cafetière pour se venger."
    elias inquiet "Pourquoi vous voulez me prendre ma tasse ?!"
    noam sourire "Personne touche à ton café, Elias."
    elias "Bon. Parce que j'ai pas fini."
    "Il reprend une gorgée comme si la discussion était réglée."
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
    nyra neutre "Relis la formulation, Ryn. Elle ne dit pas ce que les districts auront réellement le droit d'échanger."
    ryn colere "Donc on vote pour quoi ? Ce qu'elle décide ?!"
    nyra reflexion "Je veux voir le texte final avant qu'on promette quoi que ce soit aux gens."
    ryn colere "Et en attendant, ceux qui ont besoin de matériel font quoi ? Ils attendent aussi ?"
    nyra sourire "Dis-moi ce qui manque à Limen en ce moment. Si on a un exemple précis, on pourra demander à Kami si le texte permet de régler le problème."
    ryn reflechit "Des pièces pour les pompes. Pourquoi ?"
    nyra reflexion "Très bien, les pompes. Elias, tu as déjà travaillé sur ce genre de matériel ?"
    elias sourire "Ah, pour les pompes j'ai peut-être une solution !"
    iris blase "Évidemment. On a enfin une conversation politique et il faut qu'on parle de plomberie."
    elias taquin "La plomberie, au moins, ça marche quand on l'entretient."
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
    elias taquin "Attends, tu veux vraiment qu'on lève la main pour parler ?"
    julian sourire "Je parlais d'une méthode, Elias. Pas de te renvoyer à l'école."
    elen joie "Moi j'ai une idée ! On vote pour savoir qui commence !"
    iris blase "Oh non. Un vote pour organiser un débat sur un vote. On y est."
    tomas inquiet "Techniquement, il faudrait d'abord définir si ce vote préparatoire est soumis à l'unanimité..."
    mara taquin "Tomas, si tu termines cette phrase, je vote contre toi personnellement."
    tomas inquiet "Mais je... non, d'accord. J'arrête."
    noam taquin "Julian, ta réunion a déjà perdu le contrôle. Tu veux qu'on élise un responsable ?"
    $ kd_queue_character_motion("julian", "sigh")
    julian panne "Vous êtes épuisants. Et je n'ai même pas encore commencé."
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
    $ kd_direct.begin("confrontation", auto=False)
    $ kd_direct.shot("field", "ryn", duration=.20, hold=0)
    ryn colere "Ah ouais ? Chez nous, il y a des gens qui meurent en essayant de franchir ces foutues frontières. Tu veux qu'on les remercie, aussi ?"
    $ kd_direct.shot("reverse", "sael", duration=.20, hold=0)
    sael mefiant "Je n'ai pas dit que la fermeture était juste pour tout le monde. J'ai dit que les attaques avaient cessé chez nous. Ce n'est pas la même chose."
    $ kd_queue_character_motion("ryn", "anger")
    $ kd_direct.shot("field", "ryn", duration=.18, hold=0)
    ryn colere "C'est pratique, de pouvoir parler de paix quand on est du bon côté de la barrière !"
    $ kd_direct.shot("reverse", "sael", duration=.18, hold=0)
    sael colere "Et tu crois que je ne sais pas ce que c'est, de perdre des gens ?"
    ryn colere "Alors ne me parle pas comme si cette frontière nous avait tous sauvés !"
    $ kd_direct.shot("reaction", "elen", duration=.22, hold=0)
    elen peur "Hé... On peut se calmer ?"
    sael mefiant "Je ne t'ai pas demandé d'être d'accord. Je te demande d'écouter."
    $ kd_direct.end()
    think "Personne n'élève plus la voix. Le silence n'a rien réglé."
    "Ryn repousse légèrement sa chaise. Je crois qu'il va partir, mais il reprend sa tasse et reste assis."
    elias reflechit "Et moi je parlais de boulons, il y a cinq minutes... J'ai l'air malin."
    mara neutre "Voilà pourquoi je me méfie des propositions qui tiennent sur une serviette. Chacun entend ce qui l'arrange."
    nyra neutre "Quand Kami nous donnera le texte, on reprend la liste des problèmes qu'on vient de soulever. Si le texte n'en règle aucun, on le dit."
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

    mara mefiant "Franchement, toi, tu comptes vraiment voter et rentrer gentiment te coucher ?"
    sael mefiant "Oui. Si je n'ai aucune raison de rester debout."
    mara sourire "Oh, putain. C'est presque mignon."
    sael neutre "Qu'est-ce qui t'amuse ?"
    mara taquin "Rien. Tu me fais penser à quelqu'un qui ferme sa porte à clé pendant que la maison brûle."
    sael mefiant "Et toi, à quelqu'un qui préfère raconter l'incendie plutôt que d'aller chercher de l'eau."
    noam taquin "Je peux me mettre entre vous ou je risque d'y rester ?"
    mara taquin "T'inquiète, Noam. Pour le moment, elle me fait juste la morale."
    sael raison "Parce que tu essaies de rire au lieu de dire ce qui t'effraie."
    "Mara ouvre la bouche pour répondre, puis se ravise."
    mara mefiant "Ce qui me fait peur, c'est qu'on croie pouvoir battre Kami avec un bout de papier."
    sael mefiant "Moi aussi. Mais si on commence à se soupçonner avant le premier vote, elle n'aura même pas besoin d'intervenir."
    mara stress "..."
    mara taquin "Bon. J'vais voir si Elias a une meilleure théorie du complot. Avec des boulons, si possible."
    sael neutre "Essaie de ne pas lui faire peur."
    mara sourire "Promis rien du tout."

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

    $ kd_direct.begin("casual")
    $ kd_direct.place("elias", x=0.20)
    $ kd_direct.place("lysa", x=0.75)
    $ kd_direct.two_shot("elias", "lysa")
    elias ecoute "T'étais bizarrement silencieuse ce matin. Hier, tu arrivais à me répondre avant même que je finisse une phrase."
    lysa blase "J'ai écouté. Expérience nouvelle. Je recommande une fois par trimestre."
    elias sourire "T'as dû être très malade."
    lysa neutre "Merci, docteur. Ton diagnostic me touche."
    think "Je les rejoins. Lysa me laisse une place près du mur."
    $ kd_direct.end()
    $ showGroup([
        ("elias", "neutre", -0.11),
        ("noam", "inquiet", 0.13),
        ("lysa", "triste", 0.25),
    ])
    $ kd_direct.begin("comedy")
    $ kd_direct.place("elias", x=0.12, depth=1)
    $ kd_direct.place("noam", x=0.50, scale=0.94)
    $ kd_direct.place("lysa", x=0.88, depth=1)
    noam taquin "Vous avez fini de vous disputer ?"
    lysa blase "On n'a pas commencé. Elias a encore toutes ses dents."
    elias sourire "Je préfère qu'on garde cette méthode."
    noam inquiet "Lysa, t'as presque rien dit pendant le repas."
    lysa blase "J'essayais de voir combien de temps tu mettrais à le remarquer."
    noam inquiet "D'accord. Mauvaise question."
    elias ecoute "Elle m'a demandé combien de temps il fallait pour recevoir une pièce à Harmonie."
    $ kd_direct.interrupt("lysa")
    $ kd_direct.react("elias", "surprise")
    lysa blase "ELIAS."
    $ kd_queue_character_motion("elias", "embarrassed")
    elias gene "Quoi ? C'était pas un secret, si ?"
    lysa blase "Non. Laisse tomber."
    noam reflexion "Tu penses qu'on passera encore en dernier si tout se vend ?"
    $ kd_direct.profile("intimate")
    $ kd_direct.shot("medium", "lysa", duration=0.55)
    lysa reflexion "On n'a pas de quoi payer le premier prix. Et on a déjà des pénuries. Tu vois le calcul."
    noam inquiet "Ouais."
    elias reflechit "Je pensais surtout aux pièces détachées. Mais si vous pouvez même pas en acheter..."
    lysa taquin "Félicitations, tu viens de découvrir une économie."
    $ kd_queue_character_motion("elias", "laugh")
    elias rire "Je peux la redécouvrir demain avec des schémas si ça t'arrange."
    "Lysa a un petit sourire. Elle essaie aussitôt de le cacher."
    noam raison "Tu le diras pendant le débat ?"
    lysa blase "Évidemment. Mais je vais essayer de pas commencer par « vous êtes tous des idiots »."
    elias sourire "Ça te laisse pas beaucoup d'options."
    noam taquin "On va les noter avant qu'elle change d'avis."
    "Elias sort déjà sa tablette. Lysa soupire, mais elle ne lui demande pas de la ranger."

    $ kd_direct.end()
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

    $ kd_queue_character_motion("noam", "surprise")
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

    "Sael transporte une caisse de linge vers l'infirmerie. Je lui tends les bras."
    noam sourire "Je peux t'aider ?"
    sael neutre "Si tu as envie de les utiliser, oui."
    "Elle me confie la caisse. Elle pèse beaucoup plus lourd que prévu."
    noam inquiet "Et chez toi, c'est comme ça que tu recrutes les gens ?"
    sael sourire "Chez moi, personne n'attend qu'on lui promette un salaire pour porter une caisse."
    noam reflexion "Même depuis qu'il n'y a plus vraiment de commerce ?"
    sael raison "On fait ce qu'on peut avec ce qu'on a. Celui qui répare les machines mange. Celui qui travaille aux champs aussi."
    noam inquiet "Et celui qui peut pas travailler ?"
    "Sael s'arrête. Je manque de lui rentrer dedans."
    sael mefiant "Tu crois qu'on le laisse mourir de faim ?"
    noam surpris "Non ! J'ai juste demandé."
    sael raison "On s'occupe de lui. C'est la première chose qu'on apprend aux enfants."
    noam taquin "Ça et comment porter des caisses de dix tonnes ?"
    sael sourire "Ça vient beaucoup plus tard."
    "Elle me reprend la caisse sans me demander mon avis."
    sael mefiant "Ce qui m'inquiète, c'est qu'ici on puisse décider qu'un travail vaut plus qu'un autre parce qu'il rapporte davantage."
    noam reflexion "Donc tu voterais contre le commerce ?"
    sael neutre "J'ai pas dit ça. Mais je ne laisserai pas quelqu'un nous expliquer depuis cette station que nos vies valent moins parce qu'on n'a pas de monnaie."
    noam inquiet "D'accord. C'est plus clair."
    sael sourire "Bien. Maintenant, ouvre la porte."

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

    noam inquiet "Demain, quatorze heures. On aura jamais le temps de tout vérifier."
    $ kd_queue_character_motion("kael", "exhausted")
    kael fatigue "Même avec un mois, on pourrait pas."
    noam reflexion "T'es contre le texte ?"
    kael calme "J'en sais rien. On a besoin de pièces, de livraisons... Mais chaque nouveau trajet, c'est un risque."
    noam surpris "Un risque de transport ?"
    kael triste "Sur Orbite, si Kami décide de sanctionner quelqu'un, le tir peut traverser la coque."
    $ close_up("noam")
    noam peur "Elle ferait ça ? Avec des gens derrière ?"
    kael fatigue "Elle l'a déjà fait."
    "Il tourne le dos à la vitre."
    noam inquiet "Kael..."
    kael triste "Une fois, on a dû fermer une cloison. Il restait deux personnes de l'autre côté."
    $ kd_queue_character_motion("noam", "shock")
    noam peur "Vous avez pu les sortir ?"
    kael triste "Non."
    "Il se remet à examiner les consoles. Je le laisse faire, mais la question me brûle encore les lèvres."
    noam hesitation "T'as dû appuyer sur le bouton ?"
    kael fatigue "J'étais avec ceux qui l'ont fait."
    noam triste "Désolé. Je..."
    kael mefiant "Fais juste attention quand tu parleras de commerce demain. Une cargaison, c'est pas seulement des marchandises, pour nous."
    "Je regarde la Terre derrière la vitre. Cette fois, je n'ai pas envie de poser une autre question."

    call day2_collect_vote_argument("rationnement") from _call_day2_collect_vote_argument_rationnement
    call day2_collect_vote_argument("orbite") from _call_day2_collect_vote_argument_orbite
    kael fatigue "Je dois aller vérifier les relevés des consoles. À plus tard."
    $ hideGroup()
    think "La Terre semble si tranquille derrière la vitre. Je revois Kael fermer une cloison, deux personnes de l'autre côté. Il n'a pas raconté leurs visages. Je les imagine quand même."
    think "Au détour du couloir, j'entends Elias compter, puis Iris lui aboyer dessus. Pour une fois, une dispute serait presque rassurante."

    # Laisser le joueur rejoindre le gymnase à son rythme.
    $ day2_route_gym_mara_tomas_seen = False
    $ day2_route_gym_elen_sael_seen = False
    $ current_scene_active = "_2_ROUTE_GYMNASE"
    $ corridor_current = "cafeteria"
    jump OPEN_CONCLAVE_MAP

label _2_ROUTE_GYMNASE_MARA_TOMAS:
    $ day2_route_gym_mara_tomas_seen = True
    scene expression Image(corridor_background("dortoir")) at adaptive_fullscreen with dissolve
    $ showGroup([
        ("mara", "neutre", 0.20),
        ("tomas", "reflechit", 0.66),
    ])
    mara neutre "Bon, et toi ? T'as réussi à dormir dans ta chambre de ministre ?"
    tomas reflechit "Pas vraiment. Je me suis surtout demandé pourquoi la mienne ne ressemblait pas du tout à celle d'Elias."
    mara taquin "Ah ouais ? T'es allé faire le tour des chambres ? Petit curieux !"
    tomas inquiet "Non ! Il m'a montré la sienne hier. Et puis j'ai aperçu celle d'Elen quand elle a laissé sa porte ouverte."
    tomas raison "Les superficies, les meubles, même les couleurs... Il n'y en a pas deux pareilles. C'est étrange pour une station conçue pour nous accueillir tous en même temps."
    $ kd_queue_character_motion("mara", "laugh")
    mara rire "Moi, j'ai un lit immense. Si Kami veut acheter mon vote avec ça, elle s'y prend plutôt bien."
    tomas raison "Je me demande si les aménagements correspondent aux préférences de chacun. Mais comment aurait-elle pu les connaître ?"
    mara taquin "Tomas, je te demandais si t'avais bien dormi. Pas de rédiger une thèse sur les oreillers."
    tomas hesitation "Ah. Non. J'ai mal dormi."
    mara rire "Bah voilà ! C'était pas si compliqué !"
    think "Ils reprennent leur chemin sans m'avoir remarqué. Tomas a déjà recommencé à parler du mobilier."
    $ hideGroup()
    return

label _2_ROUTE_GYMNASE_ELEN_SAEL:
    $ day2_route_gym_elen_sael_seen = True
    scene expression Image(corridor_background("infirmerie")) at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elen", "joie", 0.24),
        ("sael", "neutre", 0.73),
    ])
    elen joie "Attends, Sael ! Et le village, il est grand ? Vous êtes combien ?"
    sael neutre "Assez pour que tout le monde se connaisse. Pas assez pour qu'on puisse se cacher longtemps."
    $ kd_queue_character_motion("elen", "lean_forward")
    elen surpris "Oh ! Et vous avez des fêtes ? Des marchés ? Des animaux ?!"
    $ kd_queue_character_motion("sael", "sigh")
    sael fatigue "Des fêtes, oui. Des animaux, aussi. Les marchés, moins."
    elen content "Et tu vis dans une maison ? Elle ressemble à quoi ? Il y a des fleurs ?"
    sael mefiant "Elen... Tu comptes me poser toutes les questions du monde aujourd'hui ?"
    elen inquiet "Désolée ! C'est juste que j'arrive pas à imaginer ton village. Tu parles toujours de la terre et des montagnes..."
    sael reflechit "Les maisons sont serrées contre la pente. Le matin, quand le brouillard descend, on ne voit parfois même plus le champ d'à côté."
    elen joie "C'est magnifique ! Et quand il neige ?!"
    sael fatigue "Quand il neige, on a froid."
    elen surpris "Oui, mais... beaucoup ?!"
    sael mefiant "Énormément."
    elen joie "Et vous faites des bonshommes de neige ?"
    sael fatigue "On essaie surtout de dégager les chemins."
    elen content "Ah ! Et les enfants, ils t'appellent comment ? Cheffe ? Madame Sael ?"
    sael mefiant "Ils m'appellent Sael. Comme toi. Maintenant, je dois vraiment aller à l'infirmerie."
    elen joie "D'accord ! Juste une dernière question : vous avez des chiens ?"
    sael fatigue "Oui."
    elen surpris "Combien ?!"
    sael desaccord "ELEN !"
    elen inquiet "D'accord, d'accord ! Je te laisse tranquille !"
    think "Sael accélère le pas. Elen tient exactement trois secondes avant de lui emboîter le pas."
    elen content "Mais ils ont des noms, au moins ?"
    $ hideGroup()
    return

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
    $ kd_queue_character_motion("noam", "recoil")
    noam inquiet "Tu m'avais promis une initiation ! Pas une tentative de meurtre !"
    iris taquin "Oh, le pauvre. Je peux te chercher les haltères roses, si tu veux. Il y a des petits cœurs dessus."
    $ kd_queue_character_motion("elias", "embarrassed")
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

    $ day2_route_dinner_lysa_seen = False
    $ current_scene_active = "_2_ROUTE_CAFETERIA_SOIR"
    $ corridor_current = "infirmerie"
    jump OPEN_CONCLAVE_MAP

label _2_ROUTE_CAFETERIA_SOIR_LYSA:
    $ day2_route_dinner_lysa_seen = True
    scene expression Image(corridor_background("cafeteria")) at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "neutre", 0.72),
        ("noam", "inquiet", 0.28),
    ])
    lysa surpris "Mais... qu'est-ce qui t'est arrivé ? T'as couru depuis la Terre ?"
    noam inquiet "Pire. J'ai fait du sport avec Elias."
    lysa blase "Ah. Mes condoléances."
    noam inquiet "Il m'a dit qu'on allait commencer doucement. Dix minutes plus tard, je négociais avec mes propres bras pour qu'ils continuent à fonctionner."
    lysa taquin "Et t'as perdu la négociation, vu ta tête."
    noam desaccord "Ne fais jamais de sport avec lui. Je te le dis en ami."
    lysa reflexion "Il t'a forcé ?"
    noam hesitation "Non. Enfin... Iris était là aussi."
    lysa blase "Donc tu t'es laissé convaincre par Elias, avec Iris pour t'encourager. C'était courageux. Ou complètement idiot."
    noam inquiet "Les deux, probablement. Je transpire encore, et je crois que mes jambes vont porter plainte."
    $ kd_queue_character_motion("lysa", "laugh")
    lysa rire "Si tu tombes avant la cafétéria, je te promets de prévenir quelqu'un."
    noam sourire "Tu pourrais m'aider à me relever, non ?"
    lysa taquin "Faut pas abuser. Je viens de t'offrir un soutien moral exceptionnel."
    think "Elle repart en ricanant. J'essaie de lui répondre, mais même hausser les épaules me paraît ambitieux."
    $ hideGroup()
    return

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

    $ kd_direct.begin("casual")
    think "Je reviens à la cafétéria. Mes bras protestent dès que j'essaie de tenir le plateau. À une table, Nyra raconte quelque chose qui a l'air de passionner Elen."

    nyra sourire "J'avais l'habitude de manger avec des gens qui parlaient beaucoup, mais vous êtes assez forts. J'ai même pas fini mon assiette."
    noam sourire "Non. C'est un effet secondaire de trente jours d'enfermement avec des inconnus."
    elen joie "Moi j'adore ! Enfin, sauf quand quelqu'un crie ou menace de partir. Ou quand on parle de cadavres."
    kael neutre "Chez nous, il fallait surtout se dépêcher. Une équipe finissait, la suivante prenait la place. Pas de place pour les grands discours."
    $ kd_direct.profile("comedy")
    $ kd_direct.two_shot("elen", "kael")
    $ kd_queue_character_motion("elen", "surprise")
    elen surpris "Attendez. Vous mangez en flottant ?! Ça veut dire que vos soupes font des petites bulles ?"
    $ kd_direct.react("kael", "sigh")
    kael sourire "On a une gravité artificielle, Elen. Et on fixe les plateaux quand c'est nécessaire. Sinon, je te garantis qu'on mangerait moins de soupe."
    elen content "C'est nul ! Je voulais voir une purée faire un looping !"
    kael sourire "Je peux te garantir que ce serait surtout un cauchemar à nettoyer."
    $ kd_direct.shot("reaction", "nyra", duration=0.25, hold=1)
    nyra taquin "Kael, ne lui explique pas comment on nettoie le plafond, s'il te plaît. On en a pour une heure."
    noam sourire "Je crois que j'ai raté le début de cette réunion scientifique."
    tomas hesitation "On est en train de décider de ce que vous pourrez acheter, mais... je sais même pas comment vous mangez. Ça me paraît un peu inquiétant."
    nyra neutre "Je peux te raconter comment on faisait pour les repas. Kael pourra compléter si tu veux les détails techniques."
    $ kd_direct.profile("intimate")
    $ kd_direct.shot("wide", duration=0.55)
    noam inquiet "Kael m'a raconté ce qui arrive quand une sanction perce la coque. J'arrive pas à me sortir ça de la tête."
    $ kd_queue_character_motion("kael", "sigh")
    kael fatigue "J'espérais ne pas remettre ça sur la table ce soir."
    noam neutre "T'as rien gâché. C'est moi qui ai posé la question."
    elen inquiet "Vous pensez que nos familles nous voient, en ce moment ? Parce que si oui, j'espère qu'elles ne croient pas qu'on s'amuse vraiment."
    $ kd_direct.profile("comedy")
    $ kd_direct.shot("medium", "elen", duration=0.30, hold=1)
    elen joie "Oh ! Attendez, vous avez goûté la purée ? Je suis sûre qu'ils ont changé la recette !"
    nyra taquin "Elen, je veux bien goûter la tienne. La mienne est complètement froide."
    tomas sourire "Il paraît qu'on cherche une raison de voter à l'unanimité. On pourrait commencer par la purée."
    elen joie "Moi je vote pour !"
    kael calme "Je m'abstiens. Je n'ai pas encore lu la recette."
    nyra sourire "D'accord, je vous laisse finir le scrutin. Je vais chercher du pain."
    $ kd_direct.shot("retreat", duration=0.55)
    think "Je ris avec eux. Ça ne dure pas longtemps, mais ça fait du bien."
    think "Elen examine les assiettes comme un jury gastronomique. Kael essaie de lui expliquer la préparation des repas sur Orbite sans qu'elle lui demande si les pommes de terre flottent."

    think "Les conversations se mélangent. Un souvenir de la Terre, une question sur Orbite, une plaisanterie. Pendant quelques minutes, personne ne parle du vote."

    $ kd_direct.end()
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

    call kd_vn_cg_impact("#e4f0ff")
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
        # Le dossier est l'unique point de notification et de déblocage visuel.
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


# Compatibilité : les anciens écrans de dépôt ne sont plus des interactions.
screen vote_argument_briefcase(arg_id, argument_data, card_drag_name, drop_drag_name, drop_handler):
    timer .01 action [Function(day2_vote_add_argument, arg_id), Return(True)]

screen day2_argument_deposit_success(arg):
    timer .01 action Return(True)

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
    $ day2_vote_add_argument(arg_id)
    return

# Durée de la 2e journée de jeu : 16m de jeu
# Total J0-J1 : 1h 8m
