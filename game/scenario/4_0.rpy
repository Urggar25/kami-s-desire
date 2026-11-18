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
    think "J'avais demandé cinq minutes de sommeil supplémentaires. Je n'avais rien précisé concernant les travaux publics."
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
    think "Pourquoi j'ai l'impression qu'elle vient de prévenir une personne en particulier d'un désastre concernant le petit-déjeuner ?"
    "J'enfile ma veste, vérifie une dernière fois que le dessin ne risque pas de glisser et prends ma tablette."
    jump _4_0_NAVIGATION_CAFETERIA

label _4_0_NAVIGATION_CAFETERIA:

    $ current_scene_active = "_4_0_ROUTE_CAFETERIA"
    $ corridor_current = "dortoir"
    scene expression Image(corridor_background(corridor_current)) at adaptive_fullscreen with dissolve
    "Dans le couloir, Elias est à genoux devant un casier entrouvert. Autour de lui, trois outils, une vis et quelque chose qui ressemble à un ressort forment un petit périmètre de catastrophe."
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
    noam sourire "C'est impressionnant. Tu as réussi à inventer un casier qui refuse qu'on l'abandonne."
    elias gene "Sur Terre, j'ai déjà réparé un distributeur entier, tu sais. Les gens étaient ravis."
    noam neutre "Il distribuait quoi ?"
    elias reflechit "Rien, justement. C'était son problème."
    noam surpris "Et après ?"
    elias gene "Après... des sachets. Mais tous à la fois. Enfin, pas longtemps."
    "Il ramasse les derniers outils en évitant soigneusement mon regard."
    elias inquiet "Tu ne raconteras pas ça, hein ? Il y en a déjà assez qui me regardent de travers depuis hier."
    noam calme "Promis. Pour le distributeur, en tout cas."
    elias sourire "Merci. Je crois."
    "Nous avançons de quelques pas. Derrière nous, le casier claque enfin. Elias s'arrête, écoute, puis décide de ne surtout pas aller vérifier."
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
    noam sourire "Tu veux que je te trouve un panneau de réclamation ?"
    elen colere "Ne commence pas, Noam. Tu ne peux pas comprendre."
    noam neutre "J'ai déjà perdu une chaussette dans une machine. Je crois connaître la douleur."
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
    elen colere "JE NE SUIS PAS DIFFICILE !"
    elias reflechit "Tu as quand même crié pendant trois minutes à cause de..."
    elen colere "ELIAS."
    elias inquiet "Oui. Rien."
    "Elen emporte son plateau vide comme une personne qui vient de perdre un procès et quitte la cafétéria."
    "À peine la porte refermée, quelqu'un déplace sa tasse pour l'empêcher de tomber du comptoir."

    $ showGroup([
        ("mara", "agace"), ("julian", "decu"), ("ryn", "colere"),
        ("lysa", "determine"), ("kael", "calme"), ("iris", "desaccord"),
        ("noam", "neutre")
    ])
    mara taquin "Je donne dix minutes avant qu'elle revienne annoncer une grève de la faim."
    iris colere "Tu rigoles, mais Kami a décidé toute seule de ce qu'on pouvait garder."
    mara neutre "Je peux trouver ça inquiétant et trouver Elen ridicule. J'ai le droit aux deux."
    "Lysa essaie de casser une tranche de pain. Elle n'y parvient pas et la repose comme si elle n'avait jamais eu l'intention de la manger."
    kael reflechit "Le pain n'a pas survécu au voyage ?"
    lysa blase "Si. C'est nous qui risquons de ne pas y survivre."
    noam sourire "Tu sais quoi faire avec ça, toi ?"
    lysa neutre "Oui."
    iris surpris "Ah ?"
    lysa blase "Quoi, ah ?"
    iris taquin "Rien. C'est juste que tu as répondu sans nous dire qu'on était tous idiots. C'est nouveau."
    lysa blase "Ne t'habitue pas."
    kael calme "Non, mais sérieusement. On peut utiliser ce pain pour cuisiner ?"
    lysa reflechit "Pour faire des miettolunes, oui. C'est presque fait pour."
    noam surpris "Des quoi ?"
    lysa neutre "Des miettolunes."
    mara taquin "Il faut prononcer ça en regardant la lune, ou ça marche en plein jour ?"
    lysa blase "Tu pourrais essayer de te taire, on verrait déjà si ça améliore le goût."
    kael reflechit "Je n'ai jamais entendu ce nom. C'est une spécialité d'où ?"
    lysa neutre "De chez moi. Enfin, de ma cuisine. Tu émiettes du pain un peu sec, tu ajoutes une pincée de sucre, juste assez d'eau chaude pour que ça tienne et tu fais dorer deux petites galettes. C'est tout."
    kael surpris "C'est tout ? Pas de poudre levante ? Pas d'extrait aromatique ?"
    lysa blase "Tu veux que je te donne aussi le numéro de série de la poêle ?"
    kael calme "Non. Mais je serais curieux de goûter."
    lysa surpris "Pourquoi ?"
    kael sourire "Parce que tu en parles comme si c'était délicieux et que, pour l'instant, ça ressemble à du pain mouillé."
    lysa blase "Évidemment que c'est délicieux. Enfin... c'est pas mauvais."
    iris taquin "Attendez. Lysa fait des pâtisseries ?"
    lysa colere "J'ai dit que je savais faire une galette. Détendez-vous."
    noam sourire "Une galette que tu viens de défendre avec plus d'énergie que la moitié des décisions d'hier."
    lysa blase "Encore un mot, et je t'apprends la recette avec ton plateau."
    "Kael reprend un morceau de pain et l'examine avec le sérieux de quelqu'un qui vient de découvrir un nouveau matériau."
    kael reflechit "Ça fonctionnerait avec une cuisson moins forte ?"
    lysa neutre "Tu essaies déjà de l'améliorer, alors que tu n'y as jamais goûté."
    kael calme "C'est une question."
    lysa blase "Et ma réponse, c'est non."
    "Iris a un sourire qu'elle prend à peine la peine de cacher."
    julian decu "Amusant. On est en train de discuter d'un dessert, alors qu'on aurait pu retirer à Kami ce pouvoir hier."
    "Le morceau de pain reste immobile dans les mains de Kael."
    ryn colere "Hier, le texte supprimait aussi les rations. C'est pas un détail."
    julian neutre "Je n'ai pas dit que c'en était un."
    ryn colere "Mais tu le penses assez fort pour que tout le monde entende."
    lysa blase "J'avais presque réussi à parler d'autre chose. C'était trop demander, visiblement."
    julian decu "Je n'empêche personne de parler de ses gâteaux."
    lysa colere "T'as vraiment décidé d'être pénible jusqu'au dernier repas ?"
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
        ("mara", "triste"), ("ryn", "colere"), ("lysa", "triste"),
        ("kael", "calme"), ("iris", "hesitation"), ("noam", "reflexion")
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
    lysa colere "NON."
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

    "Sur l'écran, des bénévoles remplissent des sacs de nourriture. Une petite fille saute pour voir par-dessus les adultes."
    elias inquiet "Bon... les livraisons continuent. Je m'attendais presque à voir un entrepôt vide."
    kael reflechit "On voit des sacs, pas les stocks. Mais il y a au moins quelque chose à distribuer."
    "Une bénévole ouvre un carton. Plusieurs sachets portent le même marquage que ceux de notre cafétéria."
    elen "Hé ! C'est nos sachets !"
    "Je me retourne. Elen était censée avoir quitté la pièce pour toujours. Elle a manifestement revu ses conditions."
    iris taquin "Tu es revenue pour identifier le cadavre de ta cannelle ?"
    elen desaccord "Non ! Je voulais voir si Goumi mentait. Et puis... attends."
    "Sur l'écran, la petite fille reçoit un sachet, l'ouvre et plonge aussitôt le nez dedans."
    elen surpris "Mais... elle sourit."
    ryn neutre "Bien sûr qu'elle sourit. Tu crois qu'ils ont souvent le droit à ça, là-bas ?"
    elen inquiet "C'était juste de la cannelle, pour moi."
    "La journaliste tend son micro à une femme derrière la fillette."
    "Elle remercie les bénévoles, puis demande quand arriveront les prochains sacs. On lui répond qu'aucune date n'est confirmée."
    lysa blase "Une bonne livraison. Et aucune garantie pour demain. Les deux peuvent être vrais."
    nyra reflechit "Si Kami veut nous montrer qu'elle distribue mieux, il faudrait les chiffres d'avant et d'après. Pas seulement une caméra."
    mara neutre "Laisse-lui au moins la joie de se féliciter elle-même. Elle ne fait que ça depuis hier."
    elen triste "Bon... Si elle les a vraiment reçus, tant mieux."
    iris reflechit "Ça ne rend pas la décision de Kami correcte."
    elen desaccord "J'ai pas dit ça ! Je peux être contente pour elle ET en colère pour moi, non ?!"
    elias sourire "Ça, je pense qu'on peut tous voter pour."
    "Personne ne rit longtemps."
    "Julian ne regarde pas la fillette. Il regarde Ryn."
    ryn colere "Quoi ?! T'as toujours pas fini avec moi ?!"
    julian decu "Je ne t'ai rien demandé."
    ryn colere "T'as pas besoin d'ouvrir la bouche pour m'accuser !"
    nyra neutre "Vous êtes en train de transformer un regard en résultat de scrutin. Arrêtez."
    "Julian emporte son plateau presque intact. Ryn s'assoit. Cette fois, il ne touche plus à son repas."
    "Au moment de passer la porte, Julian ralentit. Il regarde vers moi, puis vers Tomas, comme s'il attendait qu'on le rappelle."
    "Personne ne dit rien. Il sort sans un mot."
    think "C'est la première fois que je vois Julian renoncer à avoir le dernier mot."
    return

label _4_0_CAFETERIA_PNC_RYN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("ryn", "colere", 0.70)])

    noam inquiet "Ryn... tu comptes manger ce plateau ou le lancer contre le mur ?"
    ryn colere "Fais pas semblant de pas voir. Depuis hier, tout le monde me regarde comme si j'avais saboté le vote !" 
    noam neutre "On ne sait pas qui a voté contre. Même si tu me le demandais, je pourrais pas te répondre."
    ryn colere2 "Je SAIS ! Mais comme j'ai osé parler de Limen et des rations, ils ont décidé que ça suffisait à faire de moi le coupable !"
    noam inquiet "Tu as été l'un des plus inquiets. Je suppose que certains prennent tes arguments pour un aveu."
    ryn colere "Et alors ?! Je devais mentir ? À Limen, des familles dépendent de ces sacs ! J'avais pas le droit de défendre les miens ?!"
    noam neutre "Tu avais raison de le dire. J'aurais seulement voulu qu'on puisse proposer autre chose qu'un oui ou un non."
    ryn triste "Moi aussi..."
    ryn colere "Mais si Julian continue à me fixer comme un traître, je vais finir par lui demander des explications. Et j'aurai pas envie de sourire."
    noam inquiet "Essaie de ne pas lui donner une nouvelle raison de t'accuser. On doit encore voter ensemble."
    ryn colere "Alors va lui dire. Pour une fois que tu distribuerais les conseils dans les deux sens."

    $ j4_cafeteria_ryn_talked = True
    return


label _4_0_CAFETERIA_PNC_JULIAN:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "reflexion", 0.28), ("julian", "neutre", 0.70)])

    noam neutre "Julian, ça fait dix minutes que tu fixes la même tranche de pain. Tu veux la convaincre de quelque chose ?"
    julian decu "Pas faim. Et j'en ai assez d'entendre des gens se féliciter d'avoir conservé les pénuries."
    noam inquiet "Personne ne fête le résultat. Tout le monde a vu ce qu'on risquait en supprimant les rations d'un coup."
    julian colere "Et maintenant, des familles continueront à attendre des heures pour un paquet de riz ! Mais bon, nous avons été prudents. Quelle consolation !"
    noam neutre "Ce n'était pas une excuse. Le texte pouvait aussi faire des morts. Tu le sais."
    julian decu "Dis-moi quelque chose, Noam... Tu sais qui a voté contre ?"
    noam surpris "Non. Et je croyais qu'on était d'accord pour ne pas poser cette question."
    julian neutre "Parce que quelqu'un nous a fait échouer. Je voudrais au moins comprendre ce qu'il avait en tête."
    noam inquiet "On était douze. Si la personne voulait expliquer son vote, elle l'aurait déjà fait. C'est son droit."
    julian colere "C'est formidable, ce système ! On peut faire échouer tout le monde sans jamais devoir s'en expliquer !"
    noam colere "Justement ! Le vote est secret pour qu'on ne puisse pas punir ceux qui ne sont pas d'accord. Tu veux vraiment nous enlever ça aussi ?"
    julian decu "Oui. Tu me l'as déjà expliqué hier. Devant Tomas, si tu te souviens."
    "Julian baisse les yeux vers son plateau. Je m'attends à une réplique bien sentie. Elle ne vient pas."
    think "Son silence me met presque plus mal à l'aise que son arrogance."
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

    think "Je quitte la cafétéria avant que quelqu'un propose un deuxième décompte des voix. Je pourrais essayer de parler aux autres... de n'importe quoi qui ne ressemble pas à une élection."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_1

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.8

    think "J'ai croisé Elias avec ses outils, puis Elen demandant à Goumi si une tablette de chocolat pouvait être considérée comme un traitement d'urgence."
    think "L'ambiance s'est presque normalisée. C'est précisément le moment que choisit Kami pour intervenir."
    play sound sfx_announce
    pause 0.4
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Mes petits représentants ! Retour au Conclave ! Une nouvelle proposition vous attend, et elle ne se dévoilera pas toute seule !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous avez profité de votre repos. Personnellement, j'ai trouvé vos disputes beaucoup trop courtes. Nous allons remédier à ça !"
    hide screen kami_broadcast_ui
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    think "Ryn râle dans le couloir. À l'entendre, Kami vient personnellement de lui voler la plus belle sieste de sa vie."

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave") from _call_MAYBE_PLAY_SCRIPTED_DOOR_202
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0

    pause 1.0

    $ showGroup([
        ("ryn", "colere"),
        ("kael", "inquiet"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("nyra", "raison"),
    ])

    ryn colere "ON REVIENT ENCORE ICI ?! Hier on y a passé la moitié de la journée !"
    kael inquiet "Julian a prévenu qu'il ne viendrait pas. J'ai cru qu'il plaisantait."
    mara taquin "Julian qui fuit une caméra ? Vous avez vérifié qu'il était vivant ?"
    tomas hesitation "Il avait vraiment l'air mal. Je lui ai écrit, mais j'ai effacé le message avant de l'envoyer."
    mara agace "Tomas, tu n'as pas à t'excuser d'être fâché contre lui."
    tomas colere "Je sais ! Mais je n'ai pas dit que je souhaitais qu'il reste seul !"
    "Mara ouvre la bouche, surprise. Tomas baisse déjà les yeux vers sa tablette."
    nyra neutre "On peut lui laisser une journée. On aura assez de raisons de nous disputer sans aller le chercher."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Ooooh ! Un siège vide ! Julian, mon chéri, tu boudes encore ? Pourtant, je t'avais réservé ton meilleur angle de caméra !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Rassurez-vous, nous pouvons commencer sans notre star. Je lui enverrai un rappel pour le vote. Peut-être avec des fleurs."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Et maintenant... attention, mes petits représentants... Votre deuxième proposition est..."

    play sound sfx_tambour
    pause 2.2

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Je cite : « Autoriser les déplacements de personnes entre les districts. »"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Cette fois, pas de réécriture, pas de petite surprise grammaticale ! La proposition est suffisamment claire pour rester telle quelle."
    kami "Un vote favorable : les personnes peuvent circuler entre les districts."
    kami "Un vote défavorable : on conserve les frontières actuelles. Et les sanctions qui vont avec, évidemment."
    $ unlock_codex_page("frontieres_interdistricts", with_notification=False)
    $ unlock_dossier_arg("p2_formulation")

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Deux possibilités, pas de petite clause cachée. Alors ? Vous voyez, je sais être généreuse !"

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0

    think "Ryn se redresse comme si quelqu'un venait de le brancher sur une prise. Sael, elle, n'a pas bougé."
    think "Ses mains se sont pourtant refermées sur ses genoux. Ce détail me plaît beaucoup moins."

    $ showGroup([
        ("lysa", "blase"),
        ("iris", "desaccord"),
        ("elias", "determine"),
        ("kael", "inquiet"),
        ("ryn", "colere"),
        ("sael", "mefiant"),
        ("nyra", "raison"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("elen", "triste"),
    ])
    elen surpris "Attendez ! Ça veut dire que je pourrais aller rendre visite à quelqu'un sans demander la permission ?"
    ryn sourire "ENFIN ! Un texte qui sert à quelque chose !"
    lysa blase "Tu l'as adopté en quatre secondes. Nouveau record."
    ryn colere "À Limen, on ramasse des gens qui ont tenté de rejoindre leur famille. Alors oui, j'ai pas besoin d'une semaine pour réfléchir !"
    $ unlock_dossier_arg("p2_frontiere_limen")
    iris reflechit "Et les contrôles ? Sans rien pour organiser les passages, on pourrait avoir d'autres problèmes."
    ryn colere "Donc on les laisse se faire abattre ?!"
    iris colere "J'ai dit qu'il fallait réfléchir aux contrôles ! Pas tirer sur les gens !"
    elias reflechit "Moi, j'aimerais juste pouvoir aller voir des amis sans remplir un dossier. Ça fait si longtemps que..."
    "Elias se tait. Personne ne lui demande de finir."
    kael calme "Sur Orbite, les accès sont déjà surveillés. La situation est différente."
    $ unlock_dossier_arg("p2_orbite")
    sael mefiant "Et les villages qui ne disposent pas de votre surveillance ?"
    ryn colere "On peut surveiller les routes ! On a déjà des gardiens !"
    sael neutre "On en a moins que toi, Ryn."
    "Elle laisse passer quelques secondes, les doigts serrés sur le bord de la table."
    sael neutre "Avant la fermeture, des hommes armés venaient chez nous. Ils prenaient la nourriture, les outils. Parfois ils repartaient avec quelqu'un."
    elen triste "Avec... quelqu'un ?"
    sael triste "On espérait qu'il revienne. On finissait par arrêter de regarder le chemin."
    "Le sourire de Ryn disparaît. Même Mara ne trouve rien à ajouter."
    sael mefiant "Depuis la fermeture, ils ne viennent plus. Vous pouvez trouver ça injuste. Moi, je me souviens de la première nuit où les enfants ont dormi sans sursauter."
    ryn triste "Chez moi, il y a des enfants qui n'ont plus personne à attendre."
    sael triste "Je sais."
    ryn colere "Non. Je crois pas que tu saches !"
    sael colere "Parce que tu es le seul à avoir ramassé un corps, peut-être ?"
    "Ryn se lève, puis se rassoit brutalement."
    nyra raison "Sael, Ryn, personne ne vous demande de comparer vos morts."
    tomas hesitation "On pourrait faire des passages autorisés, avec des gardiens, une liste..."
    ryn colere "Une liste ?! Tu veux savoir combien de noms on a déjà sur nos listes, Tomas ?!"
    tomas peur "Non, je... je parlais de la sécurité, pas..."
    sael mefiant "Une liste n'empêchera pas les bandes armées de franchir les passages."
    iris desaccord "Alors qu'est-ce que tu proposes ? On ne peut pas dire que les tirs sont abominables et les conserver pour toujours."
    sael colere "Ceux qui s'approchent savent pourtant ce qui les attend !"
    "La phrase tombe d'un coup. Sael se fige, comme si elle avait elle-même entendu quelqu'un d'autre parler."
    ryn triste "Oui. Ils le savent."
    ryn triste "Et ils y vont quand même. Tu crois qu'ils font ça pour le plaisir ?"
    sael triste "Ryn, je..."
    ryn colere "Laisse tomber. Maintenant, au moins, je sais ce que tu penses."
    sael colere "NON ! Tu sais ce que j'ai dit parce que j'ai peur ! Ne décide pas à ma place de ce que je pense !"
    mara agace "Vous faites exactement ce que Kami attend de vous. Ça vous rend pas malades ?"
    ryn colere "Si ! Et alors ? Ça va faire revenir ceux que j'ai enterrés ?!"
    sael determine "Je ne peux pas approuver une ouverture sans garantie pour mon village. Pas avec ce texte."
    elen inquiet "Attendez... On pourrait peut-être en discuter ? On a encore deux jours..."
    sael triste "Discuter, oui. Mais je ne vous mentirai pas pour vous faire plaisir."
    "Ryn détourne la tête. Nyra me regarde : pas comme si j'avais une réponse, plutôt comme si j'étais le dernier à ne pas avoir crié."
    call day4_thread_debate_game from _call_day4_thread_debate_game

    if j4_frontieres_result == "pont":
        jump _4_0_DEBAT_APAISE
    else:
        jump _4_0_DEBAT_ROMPU

label _4_0_DEBAT_APAISE:
    "Personne ne bouge. Ryn a baissé les yeux vers ses mains."
    sael reflechit "J'ai dit que ceux qui traversaient savaient ce qui les attendait."
    sael triste "C'était ignoble. Je n'aurais pas dû dire ça."
    ryn triste "Non. Tu n'aurais pas dû."
    sael triste "Je ne peux pas te promettre un vote pour. Mais si tu veux me parler des passages surveillés... je t'écouterai."
    ryn neutre "Alors je te parlerai. Quand j'aurai arrêté d'avoir envie de te hurler dessus."
    mara sourire "Une discussion sans hurlements ? Je prends une photo, personne ne me croira."
    sael neutre "Mara. Pas maintenant."
    mara agace "Oui, bon. Je sais."
    sael determine "Pour l'amendement présenté, je suis contre. Pour le reste, ma porte n'est pas fermée."
    "Elle quitte la salle. Ryn attend que la porte se referme avant de souffler."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "triste"), ("nyra", "raison"),
        ("mara", "agace"), ("tomas", "hesitation"), ("elen", "triste")
    ])
    ryn triste "J'ai cru qu'elle allait me dire que ça n'avait pas compté."
    noam calme "Elle l'a reconnu. Ça ne change pas tout."
    ryn neutre "Non. Mais ça change quelque chose."
    ryn neutre "Je lui parlerai demain. Pas devant tout le monde."
    tomas sourire "Alors... il y a encore une conversation possible."
    "Personne n'applaudit. Il n'y a rien à célébrer. Mais Ryn range sa chaise au lieu de la pousser."
    jump _4_0_APRES_CLASH_PRE_FETE

label _4_0_DEBAT_ROMPU:
    sael colere "Vous voulez que je promette quoi ? Que les hommes qui nous ont attaqués ne reviendront pas ?!"
    ryn colere "Je veux que tu regardes en face les gens qu'on tue en prétendant protéger les autres !"
    sael colere "Et moi, je refuse de te donner mon village comme preuve de bonne volonté !"
    "Tomas recule sa chaise. Le bruit fait sursauter Elen."
    tomas inquiet "Sael, je crois que personne ne te demande..."
    sael mefiant "Tomas, s'il te plaît. Pas toi aussi."
    sael determine "Je voterai contre. Et je ne discuterai plus de ça aujourd'hui."
    "La porte se referme derrière elle avant que Ryn ait trouvé de quoi répondre."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "colere"), ("nyra", "raison"),
        ("mara", "agace"), ("tomas", "hesitation"), ("elen", "triste")
    ])
    mara colere "Tu l'as entendue parler de son village, oui ou non ?!"
    ryn colere "Je l'ai entendue dire non !"
    mara agace "Ouais. Ça, on avait remarqué."
    ryn colere "Tu vas me faire la morale aussi ? Tu sais pas ce que c'est !"
    mara neutre "Non. Et je ne vais pas prétendre le contraire."
    mara colere "Mais toi, tu prétends savoir ce qu'elle pense, alors que tu n'as même pas écouté la moitié de ses phrases."
    "Mara part à son tour. Ryn ne la rappelle pas."
    $ showGroup([
        ("lysa", "blase"), ("iris", "reflechit"), ("elias", "neutre"),
        ("kael", "calme"), ("ryn", "triste"), ("nyra", "raison"),
        ("tomas", "hesitation"), ("elen", "triste")
    ])
    ryn triste "Je voulais juste que quelqu'un dise que ce n'était pas normal."
    iris triste "Personne n'a dit que c'était normal."
    ryn colere "Alors pourquoi ça continue ?!"
    "Cette fois, personne ne cherche à répondre à sa place."
    think "J'ai voulu éviter une dispute. Maintenant, Ryn me regarde comme si je lui avais demandé d'oublier les siens."
    jump _4_0_APRES_CLASH_PRE_FETE

    jump _4_0_APRES_CLASH_PRE_FETE

label day4_thread_debate_game:
    think "Je cherche une phrase qui ne demande ni à Ryn d'oublier les morts aux frontières, ni à Sael de rouvrir la porte à ceux qui l'ont terrorisée."
    call refutation_run("j4_frontieres") from _call_day4_frontieres_refutation
    if _return[0] == "success":
        call day4_thread_debate_success from _call_day4_thread_debate_success
    else:
        call day4_thread_debate_failure from _call_day4_thread_debate_failure
    return

label day4_thread_debate_success:
    $ j4_frontieres_result = "pont"
    think "Je ne cherche pas à faire changer Sael de camp. Si elle et Ryn arrivent simplement à s'écouter, ce sera déjà un début."
    noam determine "Ryn, tu peux lui reprocher de refuser le texte. Pas de vouloir qu'on tue des gens."
    ryn colere "Et je suis censé faire quoi de ceux qui meurent ?!"
    noam inquiet "Ne les abandonne pas. Mais écoute ce qu'elle a vécu avant de lui demander de te suivre."
    sael reflechit "Je ne veux pas qu'on tue qui que ce soit. Je ne veux pas non plus retrouver ces hommes chez nous."
    ryn triste "Alors il faut surveiller les passages. Pas les fermer avec des tirs."
    sael mefiant "Tu peux me garantir que ce sera possible ?"
    ryn neutre "Non."
    "Sael relève enfin les yeux vers lui."
    ryn neutre "Je peux te promettre d'y travailler. C'est tout."
    sael reflechit "C'est la première chose que tu me dis aujourd'hui sans décider à ma place."
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
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    if j4_frontieres_result == "pont":
        elen inquiet "Alors... c'est une mauvaise nouvelle et une petite bonne nouvelle ? Je ne sais pas quoi faire de mes mains."
        lysa blase "Essaie de ne pas lancer une campagne de soutien. Juste pour aujourd'hui."
        ryn neutre "On n'a rien gagné. Mais demain, j'essaierai de parler à Sael sans gueuler."
        iris taquin "Prends un chronomètre. Je veux voir combien de secondes tu tiens."
        ryn colere "Oh, ça va !"
    else:
        tomas inquiet "Je... je crois qu'on devrait les laisser tranquilles."
        elen triste "Même Ryn ? Il a l'air tellement mal."
        lysa blase "Surtout Ryn. À moins que tu aies envie de servir de punching-ball à sa mauvaise humeur."
        ryn colere "Je suis encore là, vous savez !"
        iris fatigue "On sait. Tout le couloir doit savoir."
    "Elias se lève, pousse sa chaise, puis se ravise en voyant tout le monde sursauter."
    elias gene "Je voulais juste aller manger. Pardon."
    iris sourire "Excellente idée. Et ce soir, salle de repos. Interdiction de prononcer les mots vote, frontière et amendement."
    elen joie "Même si c'est pour proposer une soirée vraiment géniale ?!"
    lysa taquin "Surtout si c'est toi qui la proposes."
    elen desaccord "Mais j'ai même pas commencé !"
    kael calme "Je vous rejoindrai après. J'ai un petit service à demander dans le dortoir."
    think "Pour une fois, personne ne lui demande lequel."
    jump _4_0_SOIREE_SANS_VOTE

label _4_0_SOIREE_SANS_VOTE:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_cafeteria", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_evening
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "En arrivant devant la salle de repos, j'entends Elen réclamer un arbitre. Puis un deuxième."
    think "Elle a donc réussi à organiser un conflit sans employer aucun des mots interdits."
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_4_0_lounge
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([
        ("elen", "joie"), ("iris", "taquin"), ("lysa", "blase"),
        ("elias", "sourire"), ("tomas", "sourire"), ("ryn", "neutre"),
        ("noam", "neutre")
    ])
    elen joie "Noam ! Viens ! Elias prétend qu'il a gagné, mais il a triché !"
    elias colere "J'ai pas triché ! J'ai juste rattrapé le dé avant qu'il tombe !"
    iris taquin "Tu as rattrapé le dé et choisi la face. À ce niveau-là, autant écrire le résultat au marqueur."
    tomas sourire "On pourrait recommencer la manche ? Sans toucher au dé cette fois."
    lysa blase "Il faudrait déjà qu'Elen arrête de changer les règles quand elle perd."
    elen desaccord "Je les change pas ! Je les améliore !"
    "Iris éclate de rire. Elen lui lance un coussin ; il frappe Tomas, qui n'avait rien demandé."
    tomas surpris "Moi ?! Mais j'étais de ton côté !"
    elen peur "Pardon ! C'était une attaque diplomatique ratée !"
    ryn sourire "Pour une fois, j'ai rien à voir avec la bagarre. Notez bien la date."
    elias taquin "Tu veux qu'on fasse un compte rendu ?"
    ryn colere "Je vais te faire un compte rendu, moi !"
    iris sourire "Attention. Trois mots interdits et tu sors."
    ryn surpris "J'en ai dit combien ?!"
    lysa sourire "Zéro. Mais on aime te voir paniquer."
    "Je me surprends à rire. Une vraie partie a enfin commencé, sans que personne puisse en annoncer le vainqueur à l'avance."
    if j4_frontieres_result == "pont":
        "Ryn attrape un coussin tombé à terre, le pose près de Tomas et se rassoit."
        ryn neutre "Je crois que j'ai été un peu con, tout à l'heure."
        tomas hesitation "Tu veux une réponse honnête ?"
        ryn sourire "Non. C'était une erreur de ma part."
        "Tomas sourit sans rien ajouter."
    else:
        "Elen tend un dé à Ryn. Il le regarde sans le prendre."
        elen inquiet "Tu n'aimes pas jouer ?"
        ryn triste "Si. Pas ce soir."
        "Il se lève. Elias fait mine de le retenir, puis renonce."
        lysa neutre "Laisse-le. Il reviendra quand il aura envie de nous insulter à nouveau."
    "Kael apparaît à la porte, les mains dans les poches."
    kael calme "J'ai raté quoi ?"
    elen joie "La plus belle injustice de l'histoire des jeux de société !"
    kael sourire "Parfait. J'ai passé ma journée à réparer des choses, j'aimerais bien en casser une."
    iris taquin "Assieds-toi, on a justement besoin de quelqu'un pour expliquer à Elias comment fonctionne un dé."
    elias colere "VOUS ALLEZ ME LÂCHER AVEC CE DÉ ?!"
    "Personne ne prononce les trois mots interdits. Pourtant, la place vide de Sael, et celle de Julian, finissent par se remarquer."
    elen inquiet "Vous pensez qu'ils auraient voulu venir ?"
    iris fatigue "Sael avait peut-être juste besoin de calme. Pour Julian, j'en sais rien."
    if j4_frontieres_result == "pont":
        ryn neutre "J'ai dit que j'irais lui parler. Pas que j'allais débarquer dans sa chambre avec un dé."
    else:
        tomas inquiet "Je pourrais au moins leur garder une part de gâteau."
        lysa blase "Garde-la. On verra demain s'ils ont faim."
    "Elen pousse une assiette de côté. Personne n'y touche, même quand la partie reprend."
    jump _4_0_FIN_SOIREE

label _4_0_FIN_SOIREE:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_204
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    "Une lumière filtre sous la porte de Julian."
    think "Je pourrais frapper. Mais il m'a demandé de le laisser tranquille, et je n'ai pas envie de recommencer à décider pour les autres."
    "Plus loin, j'aperçois un morceau de tissu sombre noué à une poignée. Sael doit déjà être rentrée."
    if j4_frontieres_result == "pont":
        think "Ryn lui reparlera peut-être. Ce n'est pas une victoire ; je n'aurais pas cru qu'un simple peut-être puisse me soulager autant."
    else:
        think "Ryn a quitté la salle sans même essayer de me regarder. Demain, il faudra que je fasse mieux que lui demander de se calmer."
    "Je m'apprête à passer quand Mara apparaît au bout du couloir. Elle s'arrête devant la porte de Sael, sans sa plaisanterie habituelle."
    noam inquiet "Tu vas lui parler du vote ?"
    mara neutre "Je vais surtout lui demander ce qu'elle essaie de protéger. On a tous entendu sa colère. Pas grand monde a écouté le reste."
    noam reflexion "Ryn ne sera pas ravi de savoir que tu es venue."
    mara agace "Alors ne lui raconte pas une histoire que t'as pas entendue. J'ai pas encore dit ce que j'en pensais."
    "Mara frappe. Sael ouvre juste assez pour la reconnaître, puis la laisse entrer."
    "La porte se referme. De l'autre côté, leurs voix restent basses. Je n'en distingue pas un mot."
    think "Au Conclave, un bulletin peut rester secret. Une conversation entre deux portes, beaucoup moins."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_205
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je retrouve la photo sur le bureau. Juliette me tire toujours la langue."
    think "Ce matin, je me demandais si un non pouvait être une bonne nouvelle. Maintenant, je ne sais même plus ce que ce mot signifie pour ceux qui vivent de l'autre côté des frontières."
    scene bg_cg012 at adaptive_fullscreen with dissolve
    $ blink()
    "Un éclat de rire résonne derrière la cloison. Elen, évidemment. Puis une voix lui demande de baisser le ton."
    "J'allais fermer les yeux quand ma tablette s'allume : le dossier du deuxième vote vient d'être actualisé."
    think "Douze représentants. Une seule voix peut tout arrêter. Et Sael a déjà annoncé ce qu'elle ferait de la sienne."
    if j4_frontieres_result == "pont":
        think "Elle a accepté de reparler à Ryn. Pourtant, même cette promesse ne change rien au texte que nous devons voter."
    else:
        think "Je n'ai pas su les écouter. Si je retourne demain avec les mêmes arguments, il n'y aura plus personne pour me répondre."
    think "Mara est encore chez Sael. Julian refuse de sortir. Ryn attend une réponse que personne n'est capable de lui donner."
    think "Demain, je devrai choisir à qui parler en premier. Et surtout, ce que je serai prêt à entendre."
    $ blink()
    "Je pose la tablette face contre le bureau. Le vote est dans deux jours. Pour la première fois, ça me paraît terriblement proche."
    $ current_day = 5
    pause 1.5
    call end_day("5", sleeping=True) from _call_end_day_5
    jump _5_0_REVEIL_CHAMBRE

