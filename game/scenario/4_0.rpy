default j4_cafeteria_ryn_talked = False
default j4_cafeteria_julian_talked = False
# Résultat du débat : la question du vote reste entière, les relations non.
default j4_frontieres_result = "non_joue"

screen day4_cafeteria_tv_pnc():
    modal True
    zorder 205

    add Solid("#000")
    use room_scene_background("cafeteria", navigation=False)

    $ television_path = "images/background/interact/cafeteria/cafeteria1/television.png"

    imagebutton:
        idle room_interaction_null()
        hover room_interaction_layer(television_path, "cafeteria", "hover")
        focus_mask room_interaction_layer(television_path, "cafeteria", "art")
        xpos 0
        ypos 0
        action Return("television")

    if not j4_cafeteria_ryn_talked:
        imagebutton:
            idle Transform(character_image("ryn", "colere"), zoom=1.00)
            hover Transform(character_image("ryn", "colere2"), zoom=1.00)
            focus_mask True
            xalign 0.22
            yalign 1.00
            action Return("ryn")
    else:
        add Transform(character_image("ryn", "colere"), zoom=1.00) xalign 0.22 yalign 1.00

    if not j4_cafeteria_julian_talked:
        imagebutton:
            idle Transform(character_image("julian", "neutre"), zoom=1.00)
            hover Transform(character_image("julian", "decu"), zoom=1.00)
            focus_mask True
            xalign 0.78
            yalign 1.00
            action Return("julian")
    else:
        add Transform(character_image("julian", "neutre"), zoom=1.00) xalign 0.78 yalign 1.00

    frame:
        xalign 0.03
        yalign 0.05
        background Solid("#071018dd")
        padding (18, 14)

        vbox:
            spacing 5
            text "OBJECTIF" size 18 color "#6FA6C6"
            text "Consulter la télévision" size 28 color "#A6D8FF"
            text "Ryn et Julian peuvent être interrogés." size 19 color "#DCE8F7"

label _4_0_REVEIL_CHAMBRE:

    $ current_day = 4
    $ j4_frontieres_result = "non_joue"
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"
    $ cafeteria_food_level = "medium"
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    call show_chapter_title("Début du chapitre 2", "Chapitre 2 — Les lignes qui nous séparent") from _call_show_chapter_title_2

    play sound sfx_drop
    "Un objet métallique tombe dans le couloir, suivi d'un juron qu'on essaie beaucoup trop tard de rendre discret."
    noam "Cinq minutes de sommeil supplémentaire, c'est trop demandé ...?"
    scene bg_cg012 at adaptive_fullscreen with dissolve
    "Je reste étendu un moment, les yeux ouverts. J'ai encore rêvé de l'urne. Sauf que, cette fois, c'était moi qui devais compter les bulletins et ils n'arrêtaient pas de se multiplier."
    think "Quelle idée, aussi, de laisser mon cerveau organiser des élections pendant mon sommeil."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Sur le bureau, une feuille dépasse du dessous de ma tablette. Elle s'est recourbée pendant la nuit."
    "Je la dégage avec précaution. C'est le dessin de Juliette."
    "Elle m'a représenté avec une tête immense, deux yeux verts de tailles différentes et des bras assez longs pour toucher le sol. À côté, elle a écrit mon nom, puis l'a barré pour en inventer un autre."
    think "Elle soutenait que les bras, c'était pour que je puisse lui attraper des choses sur les étagères. Et que la tête... non, elle n'avait pas voulu expliquer la tête."
    "Je me souviens lui avoir demandé pourquoi j'avais six doigts à une main."
    think "« C'est pour les jours où t'en perds un. » Elle avait répondu ça sans même lever les yeux de ses feutres."
    "Je lisse un coin de la feuille. Il reste une toute petite tache violette près de mon épaule."
    think "Je me demande ce qu'elle dessine en ce moment."
    "Je repose le dessin bien à plat, loin du bord du bureau. Pas question de le laisser tomber derrière un meuble."

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonjour, mes petits perdants ! Félicitations : vous avez tous survécu à votre premier exercice de démocratie."
    kami "Le monde, lui, est resté exactement comme hier. Ce qui est une manière très économique de faire de la politique, il faut le reconnaître."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Puisque la distribution gratuite est maintenue, j'ai envoyé quelques provisions supplémentaires sur Terre. Vous allez adorer la démonstration."
    kami "Elen, mon trésor, un conseil : prends ton petit-déjeuner avant de découvrir les nouveautés. C'est pour ton bien."
    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    noam "Si Kami a modifié les règles du petit-déjeuner, j'en connais une qui va être d'une humeur massacrante..."
    "J'enfile ma veste, vérifie une dernière fois que le dessin ne risque pas de glisser et prends ma tablette."
    jump _4_0_NAVIGATION_CAFETERIA

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "Dans le couloir, Elias est à genoux devant un casier entrouvert. Autour de lui, trois outils, une vis et quelque chose qui ressemble à un ressort forment un petit périmètre de catastrophe."
    $ showGroup([
        ("noam", "neutre", 0.30),
        ("elias", "neutre", 0.70),
    ])
    noam sourire "C'est toi, le bruit de tout à l'heure ?"
    elias gene "Quel bruit ?"
    noam neutre "Un bruit métallique. Un juron. Quelqu'un qui a brièvement perdu confiance en l'univers."
    elias inquiet "Ah. Celui-là."
    "Il essaie de repousser le ressort du bout du doigt. Le ressort roule jusqu'à ma chaussure."
    noam sourire "Tu veux de l'aide ?"
    elias reflechit "Non. Enfin... si tu peux ramasser ça, ce serait gentil. Mais ne touche pas à la porte."
    noam surpris "Pourquoi ?"
    elias gene "Parce qu'elle tient."
    "Je regarde la porte. Elle semble parfaitement normale."
    noam neutre "Et avant que tu t'en occupes ?"
    elias inquiet "Elle tenait aussi, mais avec une petite résistance. Maintenant elle ferme toute seule."
    "Elias pousse la porte du casier. Elle se ferme. Puis elle se rouvre immédiatement."
    elias colere "C'EST PAS POSSIBLE !"
    noam sourire "C'est impressionnant. Mais... J'ai peur de la réponse."
    noam reflechit "Pourquoi tu es en train de bricoler sur cette porte en fait ?!"
    elias inquiet "Elle grinçait trop hier quand on l'utilisait... Alors jeme suis dis que j'allais réparer ça !"
    noam inquiet "Hein ?! Mais y'a pas besoin d'enlever des boulons pour ça, si ?!"
    elias inquiet "Bah... Ouais, disons que j'aurai pu faire plus simple..."
    elias gene "Mais t'inquiète, sur Terre, j'ai déjà réparé un distributeur entier, tu sais. Les gens étaient ravis."
    noam neutre "Il distribuait quoi ?"
    elias reflechit "Pas grand chose, justement. C'était son problème."
    noam surpris "Et après ?"
    elias gene "Après... des sachets de nourriture. Mais genre tous à la fois. Du coup les gens étaient contents, ils recevaient d'un coup toutes les rations contre un seul bon de rationnement."
    think "Impossible que ce soit voulu !"
    noam surpris "Ou-Ouais... Je vois..."
    "Il ramasse les derniers outils en évitant soigneusement mon regard."
    "Nous avançons de quelques pas. Derrière nous, la porte claque enfin. Elias s'arrête, écoute, puis décide de ne surtout pas aller vérifier si tout est enfin bon."
    call CORRIDOR_NAVIGATION(corridor_current) from _call_CORRIDOR_NAVIGATION_4_0_CAFETERIA
    $ current_scene_active = None
    "Devant la cafétéria, une voix familière couvre presque le bruit des plateaux."
    jump _4_0_CAFETERIA_ELEN

label _4_0_CAFETERIA_ELEN:

    $ decouverte_cafeteria = True
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_193
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8
    "Elen est penchée sur le comptoir. Goumi lui fait face avec la tranquillité d'une machine qui ignore jusqu'au concept de mauvaise humeur."
    think "Je crois qu'elle a trouvé quelqu'un de plus têtu qu'elle. Ce qui est franchement ambitieux."
    jump _4_0_CAFETERIA_ECRANS

label _4_0_CAFETERIA_ECRANS:

    scene cafeteria2 at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8
    pause 0.8
    scene bg_cg022 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg022")
    elen colere "GOUMI ! Regarde-moi bien. Hier, tu avais de la cannelle."
    goumi "Je ne possède pas de dispositif permettant de détourner le regard."
    elen surpris "C'est PAS ce que je te demande !"
    elias inquiet "Il reste du pain au moins ? Parce que j'aimerais éviter un petit-déjeuner composé uniquement d'eau chaude."
    goumi "Les apports nutritionnels nécessaires sont maintenus. Provisions non essentielles réaffectées aux distributions terrestres."
    elen colere "Non essentielles ?! Depuis quand la cannelle est devenue un objet de luxe ?!"
    nyra reflechit "La liste des produits réaffectés est consultable ?"
    goumi "Oui."
    nyra neutre "Alors affiche-la."
    goumi "Affichage indisponible sur le comptoir de préparation. Consultation possible sur la tablette commune."
    nyra reflechit "D'accord. C'est déjà une réponse."
    elen desaccord "Mais moi je veux une réponse qui se mange !"
    elen triste "Comment je vais faire pour manger mes pancakes sans cannelle, moi !"
    noam sourire "Tu veux que je te trouve un panneau de réclamation ?"
    elen colere "Ne commence pas, Noam. Tu ne peux pas comprendre."
    noam neutre "J'ai déjà perdu une chaussette dans une machine. C'est un peu le même niveau d'indignation, non ?."
    elen desaccord "Je parle sérieusement !"

    play sound sfx_announce
    pause 0.5
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Ooooh, Elen ! Tu as réussi à organiser un sommet international sur une épice. Je suis émue."
    kami "Les sacs sont déjà partis vers la Terre. Vous avez conservé les distributions gratuites ; j'ai décidé de les approvisionner davantage. C'est beau, la cohérence."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Pas d'inquiétude. Vous mangerez tous à votre faim jusqu'au ravitaillement du jour 7. Simplement, vous aurez moins d'occasions de faire les difficiles."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et comme je sais à quel point vous adorez discuter de mes décisions, j'ai laissé les images de la distribution sur votre télévision. De rien !"
    hide screen kami_broadcast_ui
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "neutre", 0.207),
        ("julian", "neutre", 0.291),
        ("mara", "neutre", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "inquiet", 0.542),
        ("iris", "neutre", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    elen colere "JE NE SUIS PAS DIFFICILE !"
    elias reflechit "Tu as quand même crié pendant trois minutes à cause de..."
    elen colere "ELIAS."
    elias inquiet "Oui. Rien."
    "Elen emporte son plateau vide comme une personne qui vient de perdre un procès et quitte la cafétéria."
    "À peine la porte refermée, quelqu'un déplace sa tasse pour l'empêcher de tomber du comptoir."

    $ showGroup([
        ("lysa", "determine", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "colere", 0.207),
        ("julian", "decu", 0.291),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("iris", "desaccord", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    mara taquin "Je donne dix minutes avant qu'elle revienne annoncer une grève de la faim."
    iris colere "Tu rigoles, mais Kami a décidé toute seule de ce qu'on pouvait garder."
    mara neutre "Je peux trouver ça inquiétant et trouver Elen ridicule. J'ai le droit aux deux."
    "Lysa essaie de casser une tranche de pain. Elle n'y parvient pas et la repose comme si elle n'avait jamais eu l'intention de la manger."
    kael reflechit "Le pain n'a pas survécu au voyage ? Il est déjà tout rassis ?"
    lysa blase "C'est nous qui risquons de ne pas y survivre."
    lysa sourire "Sinon ce morceau de pain date d'hier. Goumi cuit du pain en direct si on en demande."
    noam sourire "Pourquoi tu en demandes pas un d'aujourd'hui ? Si tu peux, autant éviter de manger du pain dur."
    lysa neutre "J'ai bien envie de cuisiner..."
    mara surpris "Hein ?! Cuisiner ? TOI ?!"
    kael calme "Non, mais sérieusement. On peut utiliser ce pain pour cuisiner ?"
    lysa reflechit "Pour faire des miettolunes, oui. C'est presque fait pour."
    noam surpris "Des quoi ?"
    lysa neutre "Des miettolunes."
    mara taquin "Il faut prononcer ça en regardant la lune, ou ça marche en plein jour ?"
    lysa blase "Tu pourrais essayer de te taire, on verrait déjà si ça améliore le goût."
    kael reflechit "Je n'ai jamais entendu ce nom. C'est une spécialité d'où ?"
    lysa neutre "De chez moi. Enfin, de ma cuisine. Tu émiettes du pain un peu sec, tu ajoutes une pincée de sucre, juste assez d'eau chaude pour que ça tienne et tu fais dorer deux petites galettes. C'est tout."
    kael reflechit "C'est tout ? Pas de poudre levante ? Pas d'extrait aromatique ?"
    lysa blase "Tu veux que je te donne aussi le numéro de série de la poêle ?"
    kael calme "Non. Mais je serais curieux de goûter."
    lysa neutre "Pourquoi ?"
    kael sourire "Parce que tu en parles comme si c'était délicieux et que, pour l'instant, ça ressemble à du pain mouillé."
    lysa blase "Évidemment que c'est délicieux. Enfin... c'est pas mauvais."
    iris taquin "Attendez. Lysa fait des pâtisseries ?"
    lysa determine "J'ai dit que je savais faire une galette. Détendez-vous."
    noam sourire "Une galette que tu viens de défendre avec plus d'énergie que la moitié des décisions d'hier."
    lysa blase "Encore un mot, et je t'apprends la recette à coup de plateau."
    "Kael reprend un morceau de pain et l'examine avec le sérieux de quelqu'un qui vient de découvrir un nouveau matériau."
    kael reflechit "Ça fonctionnerait avec une cuisson moins forte ?"
    lysa neutre "Tu essaies déjà de l'améliorer, alors que tu n'y as jamais goûté."
    kael calme "C'est une question."
    lysa blase "Et ma réponse, c'est non. On ne change pas une recette traditionnelle !"
    "Iris a un sourire qu'elle prend à peine la peine de cacher."
    julian decu "Amusant. On est en train de discuter d'un dessert, alors qu'on aurait pu retirer à Kami ce pouvoir hier."
    "Le morceau de pain reste immobile dans les mains de Kael."
    ryn colere "Hier, le texte supprimait aussi les rations. C'est pas un détail."
    julian neutre "Je n'ai pas dit que c'en était un."
    ryn colere "Mais tu le penses assez fort pour que tout le monde l'entende."
    lysa blase "J'avais presque réussi à parler d'autre chose. C'était trop demander, visiblement."
    julian decu "Je n'empêche personne de parler de ses gâteaux."
    lysa determine "T'as vraiment décidé d'être pénible jusqu'au dernier repas ?"
    julian neutre "On a le droit de parler de ce qu'on a perdu."
    ryn colere "Et de ce qu'on aurait pu perdre en votant oui, non ?"
    "Ryn repousse son plateau. Mara retire sa tasse du bord sans interrompre son geste."
    mara agace "Vous voulez refaire toute la journée d'hier ici ? Dites-le, que je trouve un endroit où manger."
    noam inquiet "On ne sait même pas qui a voté contre, Julian."
    julian decu "Je sais. C'est bien ce qui m'agace."
    kael reflechit "On pourrait au moins regarder la distribution. L'écran diffuse les images depuis tout à l'heure."
    iris desaccord "Une caméra ne nous dira pas si Kami a pris la bonne décision."
    kael calme "Non. Mais j'aimerais savoir où sont arrivées les provisions."
    "Lysa repousse sa tranche de pain sans un mot. Kael la regarde encore une seconde, puis se tourne vers l'écran."

    $ j4_cafeteria_ryn_talked = False
    $ j4_cafeteria_julian_talked = False
    call _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE from _call_4_0_cafeteria_television_obligatoire

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "triste", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "colere", 0.207),
        ("mara", "triste", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "inquiet", 0.542),
        ("iris", "hesitation", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "reflexion", 0.793),
        ("elias", "neutre", 0.960),
    ])
    "Je récupère un morceau de pain. Il est moins dur que celui de Lysa, mais pas de beaucoup."
    lysa neutre "T'as l'air épuisé."
    noam neutre "Je n'ai même pas encore commencé à le mâcher."
    lysa blase "Je parlais d'hier. Enfin, peu importe."
    menu:
        "Dire que le résultat te travaille.":
            noam triste "J'arrête pas de me demander si on aurait pu trouver un meilleur texte."
            lysa neutre "Peut-être. Mais ce n'est pas nous qui l'avons rédigé."
        "Dire que le texte était trop risqué.":
            noam inquiet "Supprimer les rations d'un seul coup... je pouvais pas faire comme si ça n'avait aucune importance."
            lysa reflechit "Ça n'en avait pas aucune. Le reste non plus."
        "Admettre que tu n'en sais rien.":
            noam neutre "J'en sais rien. Je pensais être soulagé ce matin. C'est raté."
            lysa blase "Au moins, ça nous fait un point commun."
    iris fatigue "Vous avez prévu de manger ce pain avant le prochain ravitaillement ?"
    noam sourire "J'essaie de déterminer par quel côté l'attaquer."
    kael reflechit "Lysa, pour les miettolunes..."
    lysa determine "NON."
    kael calme "Je n'ai encore rien demandé."
    lysa blase "Tu allais le faire."
    "Cette fois, je commence à rire. Même Lysa détourne la tête pour cacher un sourire."
    jump _4_0_TEMPS_LIBRE_1

label _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE:

    $ room_scene_indices["cafeteria"] = 1
    call screen day4_cafeteria_tv_pnc()

    if _return == "ryn":
        call _4_0_CAFETERIA_PNC_RYN from _call_4_0_cafeteria_pnc_ryn
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    if _return == "julian":
        call _4_0_CAFETERIA_PNC_JULIAN from _call_4_0_cafeteria_pnc_julian
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    if _return != "television":
        jump _4_0_CAFETERIA_TELEVISION_OBLIGATOIRE

    scene bg_cg034 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg034")
    "L'écran montre une file de personnes devant un centre de distribution. Des bénévoles chargent des sacs sur une table ; derrière eux, les cartons s'empilent jusque sous une bâche."
    elias inquiet "Bon. Il y a vraiment quelque chose dans les sacs."
    kael reflechit "On voit des livraisons. Pas ce qu'il reste dans les entrepôts."
    "Une petite fille se hisse sur la pointe des pieds pour regarder le contenu d'un carton. La bénévole lui tend un sachet, qu'elle serre aussitôt contre elle."
    "Dans un coin de l'image, une femme âgée prend deux sacs, en repose un, puis demande quelque chose à l'homme derrière la table. Le son ne porte pas jusque-là."
    iris reflechit "Pourquoi elle a reposé le deuxième ?"
    nyra neutre "On ne sait pas. Peut-être qu'elle n'y avait pas droit."
    mara neutre "Ou qu'elle n'arrivait pas à le porter."
    "La journaliste se tourne vers la petite fille. Elle lui demande ce qu'elle préfère dans le paquet. L'enfant regarde sa mère avant de répondre."
    "Une seconde plus tard, la petite fille sourit à la caméra, sans donner le nom d'un seul aliment."
    elias reflechit "Elle est contente, non ?"
    ryn neutre "Elle a reçu à manger. Bien sûr qu'elle est contente."
    "Ryn garde les yeux sur l'écran. La journaliste s'adresse maintenant à une femme qui tient un enfant endormi contre son épaule."
    "La femme remercie les bénévoles, puis demande quand arrivera la prochaine livraison. On lui répond qu'aucune date n'est garantie."
    iris fatigue "Super."
    noam inquiet "Au moins, elles ont de quoi manger aujourd'hui."
    lysa neutre "Aujourd'hui, oui."
    "La journaliste demande à la femme si elle souhaiterait autre chose. Celle-ci commence à répondre, hésite et jette un regard vers la caméra."
    "Le reportage coupe sur les bénévoles qui déchargent un autre camion."
    kael reflechit "Elle allait dire quoi ?"
    nyra reflechit "On n'en saura rien."
    lysa blase "Ils pouvaient lui laisser finir. Ça leur aurait coûté trente secondes."
    "Elias remue la cuillère dans sa tasse. Il ne boit pas."
    elias inquiet "J'aimerais bien qu'ils aient quelque chose pour demain aussi."
    ryn colere "C'est ce que je dis depuis hier."
    julian decu "Et hier, quelqu'un a quand même préféré ne rien changer."
    ryn colere "Tu vas recommencer ?"
    julian neutre "Je n'ai cité personne."
    ryn colere "T'as pas besoin de citer mon nom pour me regarder comme ça !"
    julian colere "Alors arrête de prétendre que je te regarde !"
    "Le bruit de leurs voix couvre la fin du reportage. La petite fille réapparaît à l'écran : elle mâche lentement quelque chose, les joues gonflées."
    iris desaccord "Vous pourriez la fermer trente secondes ?"
    julian decu "Très bien."
    "Julian prend son plateau et se lève. Il regarde brièvement Noam, puis la place vide à côté de Tomas."
    "Tomas entrouvre les lèvres, mais Julian a déjà rejoint la porte."
    "Ryn se rassoit si brusquement qu'une cuillère tombe sur le sol. Personne ne la ramasse."
    "L'écran continue à diffuser des images de sacs alignés. Pendant quelques secondes, on entend seulement les commentaires de la journaliste."
    "Une porte s'ouvre derrière nous."
    elen joie "BON ! J'AI DÉCIDÉ QU'ON ALLAIT FAIRE QUELQUE CHOSE DE FORMIDABLE !"
    "Je me retourne. Elen a les bras levés et un air parfaitement ravi, comme si elle n'avait pas quitté la pièce en déclarant la guerre à un robot."
    iris hesitation "Tu as retrouvé ta cannelle ?"
    elen desaccord "Non, mais j'ai trouvé beaucoup mieux !"
    mara taquin "Le sel ?"
    elen joie "Une idée !"
    lysa blase "C'est précisément ce qui m'inquiète."
    elen joie "J'ai entendu parler de vos miettolunes dans le couloir !"
    lysa neutre "Tu nous écoutais ?"
    elen inquiet "J'étais juste... devant la porte. Et ça résonne très bien, ici."
    kael reflechit "En théorie, avec les ingrédients qui restent, on pourrait en préparer."
    elen joie "EXACTEMENT ! GOUMI !"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "triste", 0.207),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "joie", 0.542),
        ("iris", "hesitation", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    goumi "Je vous écoute."
    elen joie "Prépare des miettolunes pour TOUT LE MONDE ! On va se faire un énorme petit-déjeuner !"
    goumi "Recette introuvable."
    elen surpris "Comment ça, introuvable ?!"
    goumi "Aucune recette référencée sous la dénomination « miettolunes »."
    kael reflechit "Lysa, tu pourrais lui dicter les proportions ?"
    lysa blase "Je viens de le faire. C'est du pain, du sucre et un peu d'eau."
    goumi "Précisez la quantité d'eau."
    lysa neutre "Un peu."
    goumi "Unité de mesure non reconnue."
    lysa determine "Oh, ça va ! Assez pour que ça colle. Tu vas pas leur faire passer un examen d'hydratation !"
    elen joie "Lysa, viens ! Tu peux lui montrer !"
    lysa neutre "Pardon ?"
    elen joie "C'est ta recette. Tu vas être notre cheffe !"
    lysa determine "J'ai jamais dit que je voulais cuisiner pour une assemblée entière."
    kael calme "Moi, je veux surtout goûter. Tu peux ne faire que deux galettes."
    elen desaccord "Deux ?! Mais on est..."
    iris taquin "Elen. Tu as déjà réussi à réquisitionner tout le comptoir pour une épice. Laisse-lui une chance de refuser."
    "Lysa regarde Kael, puis le morceau de pain qu'il tient encore entre deux doigts."
    lysa neutre "D'accord. Deux. Et vous arrêtez de me regarder comme si j'avais découvert une nouvelle planète."
    kael sourire "Je peux observer la cuisson ?"
    lysa blase "Non."
    kael reflechit "Même de loin ?"
    lysa determine "SURTOUT PAS DE LOIN."
    elen joie "C'EST DÉCIDÉ ! Ce soir, on mange des miettolunes !"
    goumi "Aucune réservation de salle n'a été demandée."
    elen desaccord "Goumi, ne gâche pas tout !"
    "Goumi pose sur le comptoir une assiette avec deux portions de pain sec."
    goumi "Ingrédients disponibles. La préparation reste à votre charge."
    "Elen regarde l'assiette, incrédule. Puis elle la soulève comme s'il s'agissait d'un trophée."
    elen joie "ON A LE MATÉRIEL !"
    lysa blase "On a du pain, Elen."
    elen joie "Chaque grande idée commence quelque part."
    "Tomas sourit enfin, tout petit. Ryn se contente de relever les yeux."
    "Sur l'écran derrière nous, les bénévoles poursuivent leur distribution. Personne ne sait encore quand le prochain camion arrivera."
    return

label _4_0_CAFETERIA_PNC_RYN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "colere", 0.207),
        ("julian", "neutre", 0.291),
        ("mara", "neutre", 0.375),
        ("tomas", "hesitation", 0.458),
        ("iris", "neutre", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "reflexion", 0.793),
        ("elias", "neutre", 0.960),
    ])
    noam inquiet "Tu comptes manger ce plateau ou lui demander ce qu'il pense du vote ?"
    ryn colere "Très drôle."
    noam neutre "J'essayais."
    ryn colere "Depuis hier, j'ai l'impression d'avoir un panneau sur le front. Il suffit que je passe quelque part pour que tout le monde se taise."
    noam neutre "Je crois que certains sont encore énervés. Pas forcément contre toi."
    ryn colere "Julian, lui, il l'est."
    "Ryn frotte le bord de son assiette avec son pouce."
    ryn neutre "Quand j'étais plus jeune, les gens de mon quartier m'appelaient « la sirène ». Si j'avais un problème, toute la rue était au courant."
    noam sourire "Ça devait être reposant pour tes voisins."
    ryn colere "Hé ! C'était pratique quand il fallait prévenir d'un danger."
    noam neutre "Et quand il n'y avait pas de danger ?"
    ryn neutre "Bon. Ils avaient un système pour savoir si je râlais juste parce que j'avais perdu quelque chose."
    noam surpris "Lequel ?"
    ryn sourire "Ils attendaient une minute. Si je jurais encore, c'était sérieux."
    "Il sourit une seconde, puis revient à son plateau."
    ryn colere "Mais là c'est sérieux. Des familles dépendent de ces sacs. J'allais pas me taire pendant le vote pour faire plaisir à Julian."
    noam inquiet "Je sais. Et personne ne sait qui a voté contre."
    ryn colere "Alors pourquoi tout le monde croit le savoir ?!"
    noam calme "Tu peux lui parler. Mais essaie de lui parler, pas de lui hurler dessus."
    ryn colere "Tu pourrais lui dire la même chose. Surtout que toi, il t'écoute parfois."
    noam sourire "Parfois. Pas longtemps."
    ryn neutre "Ouais. Bonne chance."
    $ j4_cafeteria_ryn_talked = True
    return

label _4_0_CAFETERIA_PNC_JULIAN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "neutre", 0.207),
        ("julian", "neutre", 0.291),
        ("mara", "neutre", 0.375),
        ("tomas", "hesitation", 0.458),
        ("iris", "neutre", 0.625),
        ("nyra", "neutre", 0.709),
        ("noam", "reflexion", 0.793),
        ("elias", "neutre", 0.960),
    ])
    noam neutre "Julian, tu vas manger ton pain ou continuer à le punir ?"
    julian decu "Pas faim."
    noam sourire "Il n'a pourtant rien fait."
    julian neutre "Tu n'es pas obligé de plaisanter."
    noam neutre "Non. C'est vrai."
    "Je reste près de la table. Julian pousse son plateau de quelques centimètres."
    julian decu "Hier, quelqu'un nous a empêchés d'essayer. Et aujourd'hui, on devrait tous faire comme si de rien n'était."
    noam inquiet "Le texte pouvait aussi faire des morts. Tu le sais."
    julian colere "Je le sais, Noam. J'étais là."
    "Il prend une inspiration, puis détourne les yeux."
    julian neutre "Tu sais qui a voté contre ?"
    noam surpris "Non. Et tu sais très bien que je ne peux pas le savoir."
    julian decu "Je voudrais juste comprendre."
    noam neutre "Si la personne voulait l'expliquer, elle pourrait le faire. Le vote est secret pour une raison."
    julian colere "Formidable. Une personne peut faire échouer tout le monde, et tout ce qu'on peut faire, c'est lui souhaiter une bonne journée."
    noam colere "Tu voudrais qu'on puisse lui demander des comptes ? Jusqu'où ?"
    julian decu "Tu m'as déjà posé cette question hier. Devant Tomas."
    noam hesitation "Oui. Je sais."
    "Julian baisse les yeux. Il a encore quelque chose à dire, c'est évident. Mais il se contente de toucher sa tasse froide."
    julian neutre "Laisse-moi seul, Noam. S'il te plaît."
    $ j4_cafeteria_julian_talked = True
    return

label day4_optional_news:

    scene bg_cg034 at adaptive_fullscreen with dissolve
    think "Les images de distribution tournent en boucle. Des sacs remplis, des files interminables, des sourires devant la caméra."
    think "Je voudrais savoir combien de personnes repartiront réellement avec quelque chose. L'écran ne le dit pas."

    return

label _4_0_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_199
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"
    think "Je ne suis pas sûr de pouvoir supporter une nouvelle conversation sur les bulletins de vote. Une balade, ou quelqu'un qui accepte de parler d'autre chose, ce serait déjà pas mal."
    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8
    "En revenant vers le dortoir, je croise Elen avec une assiette soigneusement recouverte d'une serviette."
    $ showGroup([
        ("elen", "inquiet", 0.30),
        ("noam", "neutre", 0.70),
    ])
    noam surpris "C'est pour quoi ?"
    elen joie "Pour ce soir."
    noam neutre "Il y a quoi dessous ?"
    elen inquiet "Pour l'instant ? Du pain."
    noam sourire "Tu vas le promener longtemps ?"
    elen desaccord "C'est une opération délicate. N'en parle pas à Lysa !"
    "Elle disparaît avant que j'aie le temps de répondre."
    play sound sfx_announce
    pause 0.4
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes petits représentants ! Rendez-vous au Conclave. Votre deuxième proposition vous attend."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je sais, je sais, vous avez mieux à faire. Personnellement, je trouve votre emploi du temps admirablement vide."
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Ryn passe près de moi en maugréant qu'il n'a même pas pu terminer sa sieste."
    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_202
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_trial_intro_kv2_4_0
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "inquiet", 0.124),
        ("ryn", "colere", 0.207),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "inquiet", 0.542),
        ("iris", "neutre", 0.625),
        ("nyra", "raison", 0.709),
        ("noam", "neutre", 0.793),
        ("sael", "mefiant", 0.876),
        ("elias", "neutre", 0.960),
    ])
    ryn colere "ON REVIENT ENCORE ICI ?! Hier, on y a passé la moitié de la journée !"
    kael inquiet "Julian a dit qu'il ne viendrait pas. J'ai cru qu'il plaisantait."
    mara taquin "Julian qui évite une réunion ? Tu lui as proposé de parler de lui, pour voir ?"
    tomas hesitation "Il ne répond pas à mes messages."
    mara neutre "Tu lui as écrit ?"
    tomas hesitation "J'ai commencé."
    ryn colere "C'est-à-dire ?"
    tomas inquiet "J'avais écrit « Salut ». Ensuite, j'ai effacé. Ça me paraissait bizarre de commencer par « Salut »."
    mara agace "Tomas."
    tomas colere "Quoi ?! Je peux être en colère contre lui sans avoir envie qu'il reste seul !"
    "Mara ouvre la bouche, puis la referme. Tomas regarde sa tablette comme s'il envisageait de tout recommencer."
    nyra neutre "Il a demandé à être tranquille. On peut respecter ça pendant une journée."
    ryn neutre "Pour une fois, je suis d'accord."
    mara taquin "Profite bien de cet instant, Nyra."
    play sound sfx_announce
    pause 1.0
    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Oh ! Un siège vide ! Julian, mon chéri, tu boudes ? Pourtant, j'avais réservé ton meilleur angle de caméra."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Nous pouvons commencer sans notre vedette. Je lui enverrai une invitation pour le vote. Peut-être avec des fleurs."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Voici votre deuxième proposition..."
    play sound sfx_tambour
    pause 2.2
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "« Autoriser les déplacements de personnes entre les districts. »"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pas de réécriture, pas de clause cachée dans une petite ligne. Cette fois, je vous laisse les mots tels quels."
    kami "Un vote favorable : les personnes pourront circuler entre les districts."
    kami "Un vote défavorable : les frontières restent fermées, avec les sanctions actuelles. Vous connaissez la chanson."
    $ unlock_codex_page("frontieres_interdistricts", with_notification=False)
    $ unlock_dossier_arg("p2_formulation")
    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Alors ? Deux possibilités seulement. Ne dites pas que je ne vous facilite jamais les choses."
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0
    "Ryn se redresse. Sael, au contraire, reste immobile. Elle a serré ses mains sur ses genoux."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "inquiet", 0.124),
        ("ryn", "colere", 0.207),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "triste", 0.542),
        ("iris", "desaccord", 0.625),
        ("nyra", "raison", 0.709),
        ("noam", "neutre", 0.793),
        ("sael", "mefiant", 0.876),
        ("elias", "determine", 0.960),
    ])
    elen surpris "Attendez. Je pourrais aller voir quelqu'un dans un autre district sans autorisation ?"
    ryn sourire "ENFIN !"
    lysa blase "Quatre secondes. Tu pourrais au moins faire semblant de lire le texte."
    ryn colere "À Limen, on retrouve des gens qui ont tenté de rejoindre leur famille. Parfois trop tard. J'ai pas besoin d'une heure pour savoir ce que j'en pense."
    $ unlock_dossier_arg("p2_frontiere_limen")
    iris reflechit "Et les contrôles aux passages ? Il faudrait bien organiser quelque chose."
    ryn colere "Organiser quoi ? Les tirs ?!"
    iris colere "Non ! Les passages ! C'est fou comme tu écoutes !"
    elias reflechit "Moi, ça me plairait juste de pouvoir aller voir des amis. Ça fait longtemps que..."
    "Il s'arrête. Personne ne lui demande de finir."
    kael calme "Sur Orbite, les accès sont déjà surveillés. On ne peut pas comparer tous les districts."
    mara neutre "Et les usines d'Axiome ne régleront pas le problème en fabriquant des barrières. Manupolis a déjà passé des siècles à vendre des armes sans jamais déclarer la guerre à personne."
    $ unlock_codex_page("manupolis", with_notification=False)
    $ unlock_dossier_arg("p2_orbite")
    sael mefiant "Et les villages qui n'ont pas vos moyens de surveillance ?"
    ryn colere "On a déjà des gardiens. On peut surveiller les routes."
    sael neutre "Pas partout. Tu le sais aussi bien que moi."
    ryn colere "Alors on demande des renforts. Ça se prépare !"
    sael mefiant "Tu parles comme si les gens attendaient seulement une autorisation pour se serrer la main."
    ryn "C'est pas ce que j'ai dit."
    sael colere "Tu crois que les vieux de mon village ont oublié ce que les Veyroniens et les Nessairois ont fait chez nous ?"
    sael "Tu les as entendus, toi. Tu sais ce qu'ils disent quand quelqu'un vient d'un autre territoire."
    $ unlock_codex_page("empire_veyron", with_notification=False)
    $ unlock_codex_page("technocratie_nessaire", with_notification=False)
    $ unlock_codex_page("terres_ravagees", with_notification=False)
    ryn mefiant "Arrête de parler comme si tout le monde pensait pareil."
    sael colere "Et toi, t'as pardonné ?"
    ryn surpris "Quoi ?"
    sael "Aux Veyroniens. Aux Nessairois. À ceux qui ont transformé nos terres en désert. Tu leur as pardonné, toi ?"
    "Ryn cherche sa réponse. Il ne la trouve pas tout de suite."
    ryn neutre "Je ne sais pas si j'ai pardonné."
    ryn "Mais je ne vais pas condamner leurs enfants pour ce qu'ils ont fait."
    sael mefiant "Tu crois que tous les autres auront cette patience ?"
    ryn colere "Non. Mais je refuse de décider à leur place qu'ils se détestent pour toujours."
    "Sael se lève à moitié, puis se rassied."
    sael "Chez nous, il reste des gens qui n'ont jamais posé le pied hors des Terres ravagées. Ils ont grandi avec les ruines et les histoires de leurs parents."
    sael "Tu ouvres les frontières demain, et tu crois qu'ils vont tous aller faire du tourisme ? Ils vont se jeter les uns sur les autres."
    ryn "Ou ils vont simplement partir."
    sael mefiant "Voilà. Partir."
    sael "Les jeunes d'abord. Ceux qui savent travailler, ceux qui peuvent encore faire quelque chose de leur vie. Et les autres restent là, avec les tombes."
    elen inquiet "Mais on ne peut pas obliger les gens à rester..."
    sael colere "Je ne veux obliger personne, Elen !"
    "Elen recule légèrement. Sael baisse la voix."
    sael neutre "Mais si tout le monde quitte Limen, qu'est-ce qui restera ? Nos villages ? Nos langues ? Ce que nos parents ont réussi à garder ?"
    sael "J'ai peur qu'on nous demande encore de disparaître, mais cette fois en nous disant que c'est pour notre bien."
    "Ryn s'appuie sur la table. Il ne la regarde plus de la même manière."
    $ close_up("sael")
    sael neutre "Avant la fermeture, des groupes armés passaient par chez nous. Ils prenaient de la nourriture, des outils. Et parfois des gens."
    elen inquiet "Des gens ?"
    sael triste "On attendait qu'ils reviennent. Des jours. Après, on arrêtait de demander."
    "Le visage de Ryn se ferme."
    sael mefiant "Depuis la fermeture, ils ne viennent plus. La première nuit où les enfants ont dormi sans avoir peur, je m'en souviens encore."
    ryn triste "Chez moi, les enfants attendent ceux qui ne pourront plus traverser."
    sael triste "Je sais."
    ryn colere "Non, je crois pas !"
    sael colere "Tu crois être le seul à avoir ramassé des morts ?"
    "Ryn se lève si vite que sa chaise grince, puis se rassoit."
    nyra raison "Vous ne parlez plus de la même chose. Ryn, laisse-la finir."
    ryn colere "Elle a fini ! Elle veut garder les frontières fermées !"
    tomas hesitation "Et des passages autorisés ? Avec des gardiens, des listes..."
    ryn colere "Des listes ? On en a déjà assez, Tomas ! Des noms de gens qu'on doit prévenir, tu veux les voir ?!"
    tomas peur "Non, je... je parlais de vérifier qui entre..."
    sael mefiant "Une liste ne retiendra pas des hommes armés."
    iris desaccord "Alors on fait quoi ? On accepte de tirer sur les gens pour toujours ?"
    sael colere "Ceux qui essaient de passer savent pourtant ce qui les attend !"
    "Sael s'interrompt. Elle regarde la table, comme si elle regrettait déjà de s'être entendue."
    ryn triste "Oui. Ils le savent."
    ryn colere "Et ils y vont quand même. Tu te demandes jamais pourquoi ?"
    sael triste "Ryn, je..."
    ryn colere "Laisse tomber. Je sais ce que tu penses."
    $ punch_in(0.08)
    sael colere "NON ! Tu sais ce que j'ai dit parce que j'ai peur. Ça te donne pas le droit de décider ce que je pense !"
    mara agace "Vous êtes en train de vous déchirer pour le plaisir de Kami. Vous vous rendez compte ?"
    ryn colere "Et alors ?! Ça va faire revenir ceux que j'ai enterrés ?!"
    sael determine "Même avec des gardiens, je voterai contre. Pas seulement contre ce texte. Contre l'ouverture des frontières. Je ne veux pas de ça."
    elen inquiet "Mais... on a encore deux jours. On peut peut-être en parler autrement ?"
    sael neutre "On peut en parler. Mais pas pour me faire changer mon vote. Je suis contre. Et je le resterai."
    "Ryn détourne la tête. J'ai envie d'intervenir, mais chaque phrase qui me vient sonne comme un reproche adressé à l'un des deux."
    call day4_thread_debate_game from _call_day4_thread_debate_game
    if j4_frontieres_result == "pont":
        jump _4_0_DEBAT_APAISE
    else:
        jump _4_0_DEBAT_ROMPU

label _4_0_DEBAT_APAISE:

    "Le silence n'a rien d'apaisant. Ryn garde les bras croisés ; Sael regarde le siège vide à côté de lui."
    sael reflechit "Ce que j'ai dit sur ceux qui traversent..."
    "Elle s'arrête, agacée de ne pas trouver ses mots."
    sael triste "C'était pas juste. J'aurais pas dû le dire comme ça."
    ryn triste "Non."
    sael mefiant "Et je suis toujours contre l'ouverture. Pas seulement contre cette formulation. Je veux que tu le comprennes."
    ryn neutre "Je t'ai entendue."
    sael neutre "Si tu veux me raconter ce qui s'est passé chez toi, je t'écouterai. Mais je ne veux pas que tu prennes ça pour une négociation."
    ryn colere "Tu pourrais commencer par me laisser finir deux phrases la prochaine fois."
    sael colere "Tu pourrais éviter de m'accuser de vouloir des morts !"
    "Ils se regardent un instant. Ni l'un ni l'autre ne semble prêt à ajouter quoi que ce soit."
    ryn neutre "Demain. On en parlera demain."
    sael determine "On peut s'écouter. Ça ne veut pas dire qu'on sera d'accord."
    "Elle quitte la salle."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "triste", 0.207),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "triste", 0.542),
        ("iris", "reflechit", 0.625),
        ("nyra", "raison", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    mara neutre "Bon. Personne n'a jeté de chaise. C'est déjà ça."
    iris fatigue "Mara..."
    mara agace "Quoi ? J'essaie de voir le bon côté."
    ryn triste "Je lui parlerai. Mais pas ce soir."
    tomas hesitation "Je peux t'accompagner si tu..."
    ryn neutre "Non, Tomas. Merci."
    "Tomas acquiesce. Ryn pousse sa chaise contre la table, cette fois sans bruit."
    jump _4_0_APRES_CLASH_PRE_FETE

label _4_0_DEBAT_ROMPU:

    sael colere "Vous voulez que je promette quoi ? Que les hommes qui nous ont attaqués ne reviendront pas ?!"
    ryn colere "Je veux que tu regardes les gens qu'on tue en prétendant protéger les autres !"
    sael colere "Et moi, je refuse de te donner mon village comme preuve de bonne volonté !"
    "Tomas recule sa chaise. Le bruit fait sursauter Elen."
    tomas inquiet "Sael, je crois que personne ne te demande..."
    sael mefiant "Tomas, s'il te plaît. Pas toi aussi."
    sael determine "Je voterai contre. Même si vous changez le texte, ce sera non. Et je ne discuterai plus de ça aujourd'hui."
    "La porte se referme avant que Ryn ait trouvé quoi répondre."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "colere", 0.207),
        ("mara", "agace", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "triste", 0.542),
        ("iris", "reflechit", 0.625),
        ("nyra", "raison", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    mara colere "Tu l'as entendue parler de son village, oui ou non ?!"
    ryn colere "Je l'ai entendue dire non !"
    mara agace "Ça, on avait remarqué."
    ryn colere "Tu vas me faire la morale aussi ? Tu sais pas ce que c'est !"
    mara neutre "Non. Et je vais pas prétendre le contraire."
    mara colere "Mais toi, tu prétends savoir ce qu'elle pense, alors que tu n'as même pas écouté la moitié de ses phrases."
    "Mara s'en va. Ryn la regarde partir sans rien dire."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "triste", 0.207),
        ("tomas", "hesitation", 0.458),
        ("elen", "triste", 0.542),
        ("iris", "reflechit", 0.625),
        ("nyra", "raison", 0.709),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    ryn triste "Je voulais juste que quelqu'un dise que c'était pas normal."
    iris triste "Personne n'a dit que c'était normal."
    ryn colere "Alors pourquoi ça continue ?!"
    "Personne ne répond. J'ai envie d'essayer, mais je viens de voir ce que donnent mes bonnes intentions."
    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:

    think "Si je parle maintenant, il faut au moins que ce soit pour quelque chose. Je vais essayer de reprendre ce qu'ils ont dit, pas de leur faire la leçon."
    call refutation_run("j4_frontieres") from _call_day4_frontieres_refutation
    if _return[0] == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure
    return

label day4_thread_debate_success:

    $ j4_frontieres_result = "pont"
    think "Je ne vais pas les mettre d'accord sur un texte en deux phrases. Peut-être qu'ils peuvent au moins arrêter de se parler comme s'ils s'étaient toujours détestés."
    call cutin("noam", expr="determine") from _call_cutin_kv2_4_0_noam
    noam determine "Ryn, elle refuse le texte. Elle n'a pas dit qu'elle voulait qu'on tire sur les gens."
    ryn colere "Et moi, je suis censé faire quoi de ceux qui meurent ?!"
    noam inquiet "Rien oublier. Mais écoute pourquoi elle a peur avant de lui répondre."
    sael reflechit "Je ne veux pas qu'on tue des gens. Mais je ne vais pas ouvrir mon village à ceux dont on a encore peur."
    ryn triste "Alors on surveille les passages. On ne les ferme pas à coups de tirs."
    sael mefiant "Tu peux me garantir que ça marchera ?"
    ryn neutre "Non."
    "Sael lève les yeux. Il ne cherche pas à se rattraper."
    ryn neutre "Je ne te demande pas de voter oui aujourd'hui. Je veux seulement que tu saches pourquoi je refuse d'abandonner."
    sael neutre "Je sais. Et moi, je voterai non. Tu peux accepter au moins ça ?"
    ryn triste "Je peux l'entendre."
    $ unlock_dossier_arg("p2_dialogue_possible")
    return

label day4_thread_debate_failure:
    $ j4_frontieres_result = "rupture"
    think "J'ouvre la bouche trop vite. Je veux absolument trouver une solution, et je n'ai même pas demandé ce qu'ils attendaient de moi."
    noam inquiet "Il doit bien y avoir une solution... des contrôles, une exception, quelque chose !"
    ryn colere "QUELLE exception ?! Tu comprends même pas pourquoi on se dispute !"
    sael mefiant "Tu nous demandes encore de te faire confiance sans rien proposer de précis."
    noam hesitation "Je voulais juste éviter que vous..."
    sael colere "Que nous quoi ? Que nous ayons peur ? Ça te dérange tant que ça ?"
    iris fatigue "Noam, arrête. Là, tu leur demandes de se calmer pour qu'on se sente mieux, nous."
    "J'essaie de reprendre la parole, mais Ryn et Sael se regardent sans plus m'écouter."
    $ unlock_dossier_arg("p2_confiance_brisee")
    return

label _4_0_APRES_CLASH_PRE_FETE:

    # Continuité du débat : le groupe exact est déjà posé par chaque issue.
    play music "music/bgm_world_decline.mp3" fadein 1.0
    if j4_frontieres_result == "pont":
        elen inquiet "Est-ce qu'on peut considérer que ça s'est mieux terminé que prévu ?"
        lysa blase "Tu peux considérer que personne n'a fini sur la table d'opération. C'est déjà ça..."
        ryn neutre "Je lui parlerai demain. Pas ce soir."
        iris taquin "Bonne idée. Fais une nuit complète avant de recommencer à hurler."
        ryn colere "Je hurle pas tout le temps !"
        iris sourire "Ça, tu l'as murmuré, peut-être ?"
    else:
        tomas inquiet "Je... je crois qu'on devrait les laisser tranquilles."
        elen triste "Même Ryn ? Il a l'air tellement mal."
        lysa blase "Surtout Ryn. S'il a envie de parler, il saura nous trouver."
        ryn colere "Je suis encore là, vous savez !"
        iris fatigue "Oui, ça s'entend."
    "Elias se lève. Le bruit de sa chaise fait tourner plusieurs têtes."
    elias gene "Je voulais juste aller manger. Vous pouvez arrêter de me regarder comme ça ?"
    tomas sourire "Je viens avec toi."
    elen surpris "Attendez, personne n'a parlé du goûter de ce soir !"
    lysa blase "Je savais qu'on finirait par en arriver là."
    kael reflechit "Il y avait une préparation à essayer, non ?"
    lysa determine "J'ai dit deux galettes. Pas une cérémonie officielle."
    elen joie "Mais on peut au moins s'installer à la salle de repos. J'ai déjà trouvé un jeu !"
    iris taquin "Et si on évitait de parler du vote pendant une heure ?"
    elias sourire "Je vote pour."
    "Tout le monde le regarde."
    elias inquiet "Quoi ? Qu'est-ce que j'ai dit ?"
    lysa neutre "Allez. On va manger avant qu'il fasse une autre proposition."
    kael calme "Je passe prendre quelque chose au dortoir. Je vous rejoins."
    "Personne ne lui demande quoi. Nous nous séparons sans autre décision."
    jump _4_0_SOIREE_SANS_VOTE

label _4_0_SOIREE_SANS_VOTE:

    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_evening
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Devant la salle de repos, j'entends Elen compter très fort jusqu'à trois, puis demander aux autres de faire comme si elle n'avait rien dit."
    think "Ça commence bien."
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_lounge
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("ryn", "neutre", 0.207),
        ("tomas", "sourire", 0.458),
        ("elen", "joie", 0.542),
        ("iris", "taquin", 0.625),
        ("noam", "neutre", 0.793),
        ("elias", "sourire", 0.960),
    ])
    elen joie "Noam ! Viens ! On est à deux doigts de disqualifier Elias."
    elias colere "J'ai RIEN FAIT !"
    noam surpris "Je peux savoir à quoi on joue ?"
    iris taquin "C'est une excellente question. On aimerait bien savoir aussi."
    elen desaccord "Les règles sont très simples."
    lysa blase "Elle a dit ça trois fois. Les règles ont changé quatre fois."
    elen colere "Parce que vous refusez de les comprendre !"
    tomas sourire "Le principe, c'est de lancer deux dés et de former une paire. Enfin, je crois."
    elias inquiet "J'avais une paire !"
    iris taquin "Oui. Après avoir rattrapé le dé au vol et retourné la face qui ne t'arrangeait pas."
    elias colere "Je l'ai rattrapé parce qu'il allait tomber !"
    noam sourire "Tu pourrais demander au dé son témoignage."
    elias neutre "Ah ah. Très drôle."
    elen joie "On recommence. Cette fois, tout le monde garde les mains sur ses genoux avant de lancer."
    lysa neutre "Comment on lance, du coup ?"
    "Elen réfléchit. Elle regarde ses mains. Puis les dés."
    elen inquiet "Bon. Sauf celui qui lance."
    iris sourire "Une règle parfaite. Aucune ambiguïté."
    "La première manche dure à peine quelques secondes. Tomas obtient une paire et s'excuse immédiatement."
    elen surpris "Mais pourquoi tu t'excuses ?!"
    tomas hesitation "J'ai eu de la chance."
    lysa blase "Fais attention, Elen va sûrement l'interdire à la manche suivante."
    elen colere "JE N'INTERDIS PAS LA CHANCE !"
    ryn sourire "Si tu pouvais l'interdire aux autres, tu le ferais."
    elen desaccord "Toi aussi ?!"
    "Je prends les dés à mon tour. Le premier roule correctement. Le second s'arrête contre la chaussure d'Elias."
    elias inquiet "Hé ! Je l'ai pas touché !"
    noam neutre "Personne ne t'accuse."
    elias inquiet "Ah. Bon."
    iris taquin "Il plaide déjà non coupable, ça devient suspect."
    "Elias recule ses pieds si loin sous sa chaise qu'il manque de tomber."
    tomas surpris "Doucement !"
    elias colere "Vous êtes tous contre moi !"
    lysa sourire "Pas tous. Le dé, peut-être."
    "Ryn rit franchement. Il se surprend lui-même et regarde aussitôt ailleurs."
    elen joie "Bon ! Nouvelle manche ! Celui qui perd doit aller chercher les assiettes !"
    lysa determine "Attends. Les assiettes de quoi ?"
    "Elen retire une serviette du plateau caché derrière le canapé. On y découvre des morceaux de pain et un petit récipient de sucre."
    elen joie "Surprise !"
    lysa neutre "Tu as promené ça toute la journée ?"
    elen inquiet "Pas toute la journée."
    noam sourire "Je peux témoigner qu'elle l'a fait au moins une partie de l'après-midi."
    lysa blase "C'est un morceau de pain, pas une relique."
    elen joie "Et maintenant, on va faire les miettolunes !"
    iris hesitation "Ici ?"
    elen desaccord "À la cafétéria, après la partie. J'ai réservé un accès au comptoir."
    tomas hesitation "Je croyais qu'on jouait pour décider qui allait chercher les assiettes."
    elen inquiet "Oui, bon. Ça aussi."
    "Quelqu'un frappe au cadre de la porte. Kael nous observe, l'air satisfait de découvrir que rien n'a encore brûlé."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "neutre", 0.207),
        ("tomas", "hesitation", 0.458),
        ("elen", "inquiet", 0.542),
        ("iris", "neutre", 0.625),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    kael calme "J'ai raté quoi ?"
    iris taquin "Les règles, mais nous aussi."
    kael sourire "Parfait. Je déteste arriver au milieu d'une partie que tout le monde comprend."
    elias colere "PERSONNE NE M'ACCORDERA CETTE VICTOIRE ?!"
    kael reflechit "Tu as gagné ?"
    elias sourire "Merci ! Enfin quelqu'un..."
    lysa blase "Il a attrapé un dé au vol et choisi sa face."
    kael reflechit "Ah. Il faudrait peut-être modifier la manière de lancer."
    elias colere "PAS TOI AUSSI !"
    "Kael prend les dés, les pose dans un gobelet et secoue celui-ci."
    kael calme "Voilà. Plus de contact avec les mains pendant le lancer."
    elen joie "Mais c'est une idée GÉNIALE !"
    lysa blase "Ça existe depuis très longtemps, Elen."
    elen desaccord "Tu pourrais me laisser être impressionnée cinq minutes ?"
    "La manche reprend. Kael fait tomber les deux dés sur la table, tous deux montrant la même face."
    elias inquiet "Quoi ?! Mais..."
    iris taquin "Une victoire propre. Elias, prends des notes."
    elias colere "JE SAIS LANCER DES DÉS !"
    "Cette fois, même Tomas éclate de rire. Elias boude environ trois secondes avant de demander sa revanche."
    "Nous finissons par perdre le fil des points. Elen est persuadée d'avoir gagné deux manches de plus que les autres ; personne ne trouve la feuille où elle prétend les avoir notées."
    elen joie "BON. Le grand gagnant, c'est..."
    lysa neutre "Les assiettes. Va les chercher."
    "Elen ouvre la bouche, mais Iris la pousse doucement vers la porte. Lysa prend finalement le plateau avec un soupir."
    lysa blase "Vous allez me suivre à la cafétéria, et personne ne touche à la poêle tant que j'ai pas fini."
    kael sourire "Je peux regarder ?"
    lysa determine "NON."
    kael calme "Je m'en doutais."
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    "Goumi nous autorise le comptoir. Lysa émiette le pain, ajoute un peu de sucre puis l'humidifie juste assez pour former deux petites galettes."
    "Tout se fait à la main. C'est terminé avant que Kael ait sorti la première de ses questions."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "neutre", 0.207),
        ("tomas", "hesitation", 0.458),
        ("elen", "inquiet", 0.542),
        ("iris", "neutre", 0.625),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    elen surpris "Mais c'est tout ?"
    lysa neutre "C'est tout."
    elen desaccord "On aurait pu faire ça ce matin !"
    lysa blase "Ce matin, tu étais occupée à menacer Goumi."
    goumi "Menace enregistrée. Aucun dommage constaté."
    iris sourire "Merci, Goumi. Heureusement que quelqu'un tient les comptes."
    "Lysa fait dorer les galettes sur la plaque du comptoir. Une odeur de pain chaud se répand dans la pièce ; même Ryn se rapproche."
    kael reflechit "C'est drôle. Avec si peu d'ingrédients, je m'attendais à quelque chose de plus sec."
    lysa neutre "Goûte avant de faire ton rapport."
    "Elle partage une galette en plusieurs morceaux. Kael en prend un, le mâche lentement et se fige."
    elen inquiet "Alors ?!"
    kael reflechit "C'est... vraiment bon."
    lysa taquin "Tu vois ? T'as survécu à une recette sans mode d'emploi."
    elias sourire "Moi aussi, je peux goûter ?"
    elen colere "Attends ton tour !"
    tomas sourire "Il en reste assez pour tout le monde, je crois."
    "Tomas divise les derniers morceaux en portions si petites qu'il finit par s'excuser de leur taille."
    noam sourire "C'est pas mal, pour du pain dont personne ne voulait ce matin."
    lysa blase "Ce n'est pas « pas mal ». C'est bon."
    noam calme "C'est bon."
    "Lysa baisse les yeux, satisfaite. Elle fait mine de s'occuper de la plaque, qui est pourtant déjà éteinte."
    ryn sourire "Tu pourrais nous en refaire demain ?"
    lysa neutre "Demain ?"
    ryn neutre "Enfin, si tu veux."
    lysa blase "On verra."
    "Il manque encore deux personnes. Sael et Julian n'ont pas répondu à l'invitation d'Elen."
    elen inquiet "On devrait leur en garder ?"
    iris reflechit "Oui. Mais ne va pas frapper chez eux ce soir pour leur faire goûter."
    elen desaccord "J'allais pas faire ça !"
    mara taquin "C'est bien pour ça que tu as déjà une assiette à la main."
    "Mara vient d'apparaître à l'entrée. Elen cache aussitôt l'assiette derrière son dos."
    $ showGroup([
        ("lysa", "blase", 0.040),
        ("kael", "calme", 0.124),
        ("ryn", "neutre", 0.207),
        ("mara", "taquin", 0.375),
        ("tomas", "hesitation", 0.458),
        ("elen", "joie", 0.542),
        ("iris", "neutre", 0.625),
        ("noam", "neutre", 0.793),
        ("elias", "neutre", 0.960),
    ])
    elen inquiet "C'est pour demain."
    mara sourire "Bien sûr."
    if j4_frontieres_result == "pont":
        ryn neutre "Tu peux leur laisser une part. Je parlerai à Sael demain."
        tomas sourire "D'accord."
    else:
        ryn triste "Gardez-la. Moi, j'ai pas très faim."
        "Il dépose son morceau et sort sans ajouter un mot."
        $ showGroup([
            ("lysa", "blase", 0.040),
            ("kael", "calme", 0.124),
            ("mara", "neutre", 0.375),
            ("tomas", "hesitation", 0.458),
            ("elen", "inquiet", 0.542),
            ("iris", "neutre", 0.625),
            ("noam", "neutre", 0.793),
            ("elias", "neutre", 0.960),
        ])
        tomas inquiet "Je lui en mettrai une de côté."
    "Personne ne relance la discussion sur les frontières. Elen recommence simplement à raconter sa victoire au jeu, avec trois manches de plus que tout à l'heure."
    jump _4_0_FIN_SOIREE

label _4_0_FIN_SOIREE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    "La porte de Julian est fermée. Une ligne de lumière passe dessous."
    think "Je pourrais frapper. Il m'a demandé de le laisser tranquille, pourtant. Pour une fois, je vais essayer de l'écouter."
    "Un peu plus loin, un morceau de tissu sombre est noué à une poignée. Sael est déjà rentrée."
    "Mara arrive derrière moi, les mains dans les poches."
    $ showGroup([
        ("mara", "neutre", 0.30),
        ("noam", "neutre", 0.70),
    ])
    noam inquiet "Tu vas la voir ?"
    mara neutre "Ouais."
    noam neutre "Pour reparler du vote ?"
    mara agace "Tu sais, parfois, les gens se parlent sans préparer un scrutin."
    noam hesitation "Oui. Pardon."
    mara neutre "Je veux savoir comment elle va. Après, si elle veut me parler de son village, je l'écouterai."
    noam inquiet "Et Ryn ?"
    mara agace "Quoi, Ryn ? Je dois lui demander la permission ?"
    noam neutre "Non. Je me demandais juste..."
    mara neutre "Alors arrête de te demander des trucs à sa place."
    "Mara frappe. Sael entrouvre, regarde dans le couloir, puis s'écarte pour la laisser entrer."
    "Je ne reste pas écouter."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Le dessin de Juliette m'attend sur le bureau, à côté de ma tablette. Je remarque que j'avais oublié un détail : elle m'a aussi dessiné une cape."
    think "Elle m'avait assuré que c'était parce que j'étais nul pour courir et qu'une cape, au moins, ça donnerait l'impression."
    "Je souris malgré moi."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    "Dans la chambre voisine, quelqu'un éclate de rire. Une autre voix lui demande de parler moins fort."
    "Ma tablette s'allume. Le dossier du deuxième vote a été actualisé."
    if j4_frontieres_result == "pont":
        think "Ryn et Sael ont dit qu'ils reparleraient. J'espère seulement qu'ils tiendront assez longtemps pour finir une conversation."
    else:
        think "Je repense à ce que j'ai dit devant Ryn et Sael. Je crois que, demain, je ferais mieux de les écouter avant de proposer quoi que ce soit."
    "Je retourne la tablette sur le bureau. Le vote aura lieu dans deux jours."
    "Je cherche encore quelques secondes une position confortable, puis je ferme les yeux."
    $ current_day = 5
    pause 1.5
    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

