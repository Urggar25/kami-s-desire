# =============================================================================
# JOUR 30 — LE DERNIER DÉPART
# Route 0_1_1_0_0 — suite directe du J29.
# Trois issues : barricade réussie / barricade échouée / ventilation.
# L'épreuve de barricade ci-dessous est un PROTOTYPE narratif remplaçable.
# =============================================================================

default j30_escape_route = None
default j30_barricade_success = False

default j30_barricade_stage = 0

label _30_0_1_1_0_0_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"

    scene black
    play music "music/bgm_cold_metadata.mp3" fadein 1.5

    "Je ne sais pas si j'ai dormi. Je me souviens d'avoir fermé les yeux, puis d'avoir passé une éternité à écouter le silence derrière la porte."
    "Une voix joyeuse éclate soudain au-dessus de notre tête, si forte que je me redresse d'un bond."

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Bonjour, bonjouuur ! Debout, mes chers représentants ! Aujourd'hui est un grand jour !"

    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Iris a déjà les yeux ouverts. Elle est assise contre le mur, son tournevis encore dans la main. La marque laissée par sa prise traverse sa paume."
    "Elle regarde le haut-parleur, puis l'écran de son téléphone."

    $ showGroup([
        ("iris", "fatigue", 0.35),
        ("noam", "fatigue", 0.65),
    ])

    iris fatigue "Sept heures cinquante-huit."
    noam inquiet "Quoi ? Déjà ?"
    iris inquiet "J'ai regardé toute la nuit. J'ai dû m'endormir une fois, dix minutes, pas plus."

    $ hideGroup()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Dans deux petites minutes, nous procéderons au dernier vote de cette édition du Conclave ! Je vous rappelle la proposition : quiconque transgresse un Commandement verra désormais sa mémoire effacée, plutôt que d'être éliminé."
    kami "Je sais, je sais ! C'est émouvant. Presque un mois ensemble, et nous voilà déjà arrivés à notre ultime décision."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "fatigue", 0.35), ("noam", "inquiet", 0.65)])
    "Je me jette sur la commode. Nous l'avions poussée devant la porte hier soir, mais le véritable obstacle est de l'autre côté."
    "Iris m'aide à tirer le meuble. Ses pieds grincent sur le sol et l'un des tiroirs s'ouvre, répandant quelques affaires à nos pieds."
    "J'abaisse la poignée. La porte résiste avant même que le battant ait parcouru deux centimètres."

    play sound sfx_creak volume 0.35

    noam colere "Allez... Bouge !"
    iris determine "Arrête, tu te fais mal. Laisse-moi essayer."

    "Elle pose son épaule contre le battant et pousse de toutes ses forces. Une plaque métallique vibre dans le couloir. C'est tout."
    "Je tente de passer mes doigts dans l'ouverture : le bois et les barres fixées en travers s'emboîtent tellement qu'il n'y a presque pas de prise."

    noam inquiet "Ils ont vraiment tout bloqué..."
    iris colere "Ça, j'avais remarqué !"

    "Elle revient vers la grille d'aération. Les vis que nous avions essayé de retirer la veille sont toujours accessibles de notre côté, mais les pièces ajoutées derrière empêchent de faire pivoter le cadre."
    "Iris glisse la pointe du tournevis dans un interstice. Elle force. Le métal se déforme à peine."

    noam inquiet "Kami ! Il reste deux minutes ! Il faut que tu nous fasses ouvrir !"
    $ hideGroup()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Je ne peux pas discuter avec tous les représentants individuellement, Noam. Il faut être ponctuel !"
    $ bc_show("noam", "colere")
    noam colere "On nous a enfermés ! Tu nous entends, oui ou non ?!"

    $ bc_hide()
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "inquiet", 0.35), ("noam", "inquiet", 0.65)])
    "Aucune réponse. Je tape contre la porte, une fois, deux fois. Personne ne frappe en retour."
    "Iris tire mon bras et me montre l'heure. Huit heures viennent de s'afficher sur son écran."

    stop music fadeout 0.8

    $ hideGroup()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote commence maintenant !"

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "inquiet", 0.35), ("noam", "inquiet", 0.65)])
    "Nous restons immobiles. Il n'y a pas le moindre bruit dans le couloir, pas même un pas pour rejoindre la salle du Conclave."
    "Je m'attendais malgré tout à entendre des protestations, des discussions, quelqu'un demander où nous étions passés."
    "Rien."

    iris inquiet "Ils votent vraiment sans nous ?"
    noam inquiet "Ils ont pas besoin de nous. Tu te souviens ? Tant que personne vote contre..."

    "Iris serre le tournevis jusqu'à blanchir les jointures. Je cherche un bouton sur ma tablette, une notification, une possibilité d'exprimer notre refus à distance."
    "L'écran reste sur le menu habituel. Le Codex ne propose aucun vote."

    $ hideGroup()
    scene bg_diffusion_fier at adaptive_fullscreen with dissolve
    kami "Et... c'est terminé !"

    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    kami "Pas une seule voix contre ! Votre dernière proposition est donc ADOPTÉE ! Désormais, toute transgression des Commandements entraînera un effacement de mémoire plutôt qu'une élimination."
    kami "Félicitations à tous ! Vous pouvez être fiers de votre travail."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "colere", 0.35), ("noam", "inquiet", 0.65)])
    iris colere "Ça a duré combien de temps, son truc ? Même pas une minute ?"
    noam inquiet "Je sais pas. Je..."

    "Je m'interromps. Le haut-parleur grésille de nouveau."

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    $ hideGroup()
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Une dernière petite annonce avant nos adieux : la navette pour la Terre décollera dans trente minutes exactement. Je vous invite à récupérer vos effets personnels et à vous présenter à l'embarquement sans tarder !"
    kami "Les retardataires devront se débrouiller. Vous savez comme les transports peuvent être compliqués à organiser !"

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "inquiet", 0.35), ("noam", "inquiet", 0.65)])
    "Trente minutes."
    "Je regarde les deux issues de la chambre : les planches derrière la porte et la ventilation, dans laquelle nous avons découvert ce que personne n'aurait dû voir."
    "Iris a suivi mon regard. Elle comprend avant que j'aie prononcé un mot."

    iris determine "On peut pas rester là."
    noam inquiet "La porte, on sait au moins où elle donne. Si on arrive à enlever ce qu'ils ont fixé..."
    iris inquiet "Et la ventilation ? On a récupéré des outils hier. Peut-être qu'on peut défaire les fixations de l'intérieur."
    noam reflexion "Ça débouche loin de l'embarquement. On connaît une partie du chemin, mais pas tout."
    iris determine "On n'a pas le temps de peser ça pendant dix minutes. Décide. Je reste avec toi."

    "Je fixe la barricade. Chaque coup porté au bois nous coûtera du temps. Mais retourner dans les conduits signifie passer là où Nyra a été tuée."
    "Iris attend, sans essayer de choisir à ma place."

    menu (screen="critical_choice", noam_expr="hesitation"):
        "Comment rejoindre la navette avant son départ ?"
        "Tenter de démanteler la barricade devant la porte.":
            $ j30_escape_route = "barricade"
            jump _30_0_1_1_0_0_BARRICADE
        "Ouvrir la ventilation et passer par les conduits.":
            $ j30_escape_route = "ventilation"
            jump _30_0_1_1_0_0_VENTILATION


# =============================================================================
# BRANCHE 1 — BARRICADE
# Prototype jouable provisoire : quatre manipulations dans le bon ordre.
# À remplacer par le futur minijeu de planches entremêlées. Garder le contrat :
# j30_barricade_success = True / False, puis jump _30_..._BARRICADE_RESULTAT.
# =============================================================================

label _30_0_1_1_0_0_BARRICADE:
    $ current_period = "Matin"
    $ j30_barricade_success = False
    $ j30_barricade_stage = 0

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([
        ("iris", "determine", 0.35),
        ("noam", "inquiet", 0.65),
    ])

    "Iris pose ses outils devant la porte. Il nous faut d'abord dégager une ouverture suffisante pour regarder comment les fixations ont été montées."
    "Je prends une pince dans la trousse et retire la petite plaque de protection située près de la poignée. Derrière, le bois est traversé par plusieurs tiges métalliques."
    iris reflexion "C'est pas juste des planches vissées. Ils ont croisé les attaches. Si on enlève la mauvaise, ça va bloquer celles qui restent."
    noam inquiet "Comment ils ont pu fabriquer ça en une matinée ?"
    iris colere "Noam, regarde les tiges. Pas l'heure !"

    "Je respire un grand coup. Une barre porte le poids des deux planches supérieures. Une autre plaque est suspendue à un câble tendu."

    # Prototype narratif volontairement difficile (~1 chance sur 81 sans analyse).
    # Le futur écran de minijeu doit simplement définir j30_barricade_success.
    menu:
        "Libérer la planche du bas en premier.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT
        "Détendre le câble avant de retirer les planches.":
            $ j30_barricade_stage = 1
        "Couper la tige qui traverse la poignée.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT

    "Le câble se détend dans un bruit aigu. Iris le retient avec la pince pendant que je retire la première attache."
    iris determine "D'accord. Maintenant, doucement."
    "Derrière, trois fixations se croisent autour d'une plaque dont le bord a été replié pour empêcher qu'on la soulève."

    menu:
        "Déplier d'abord le bord de la plaque.":
            $ j30_barricade_stage = 2
        "Tirer sur la fixation centrale.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT
        "Faire levier sous la planche supérieure.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT

    "Une bande de métal tombe à nos pieds. Nous avons enfin assez d'espace pour atteindre les pièces fixées au chambranle."
    "Mon téléphone vibre contre ma hanche. Je n'ose pas regarder l'heure, mais Iris l'a entendue aussi."
    iris inquiet "Continue. On est presque à travers."
    "Une dernière traverse retient tout l'ensemble. Elle est prise entre deux vis et une cale de bois."

    menu:
        "Dévisser d'abord la fixation côté mur.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT
        "Retirer la cale pour libérer la traverse.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT
        "Bloquer la traverse, puis retirer les deux vis alternativement.":
            $ j30_barricade_stage = 3

    "Iris maintient la barre avec les deux mains. À chaque demi-tour de vis, elle s'affaisse un peu plus et le bois craque contre le sol."
    "Nous sommes couverts de poussière et de petits éclats. Une planche cède soudain, ouvrant un passage assez large pour un bras."
    iris determine "On y est. Enlève ce qui tient encore !"

    menu:
        "Tirer toutes les planches vers l'intérieur.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT
        "Dégager les morceaux un par un en soutenant la plaque du dessus.":
            $ j30_barricade_stage = 4
            $ j30_barricade_success = True
            jump _30_0_1_1_0_0_BARRICADE_RESULTAT
        "Pousser la plaque du dessus dans le couloir.":
            jump _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT

label _30_0_1_1_0_0_BARRICADE_ECHEC_IMMEDIAT:
    "Un craquement me coupe dans mon geste. La plaque supérieure s'enfonce entre deux traverses au lieu de tomber, et l'ensemble se serre contre le cadre."
    "J'essaie de la soulever, mais mes doigts glissent sur le métal. Iris tire de son côté. Rien ne bouge."
    $ j30_barricade_success = False
    jump _30_0_1_1_0_0_BARRICADE_RESULTAT

label _30_0_1_1_0_0_BARRICADE_RESULTAT:
    if j30_barricade_success:
        jump _30_0_1_1_0_0_FIN_NAVETTE
    else:
        jump _30_0_1_1_0_0_FIN_PRODUCTION


# =============================================================================
# FIN 1A — BARRICADE RÉUSSIE : ONZE DANS LA NAVETTE
# =============================================================================

label _30_0_1_1_0_0_FIN_NAVETTE:
    play sound sfx_creak volume 0.6

    "La dernière plaque dérape contre le mur dans un fracas métallique. Iris manque de tomber avec elle. Je l'attrape par le bras tandis que la porte, enfin libre, s'ouvre entièrement."
    "Nous restons une seconde stupéfaits devant le couloir vide. Après deux jours à regarder cette porte, je ne pensais plus revoir l'extérieur."

    iris determine "BOUGE !"

    $ hideGroup()
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Nous courons. Iris me dépasse dans le premier virage, glisse sur le sol lisse et se rattrape au mur sans s'arrêter."
    "Les lumières du dortoir sont allumées. Les portes des autres chambres sont grandes ouvertes ; je ne vois ni bagages, ni vêtements abandonnés, ni quelqu'un pour nous appeler."
    "Je consulte mon téléphone en courant."

    noam peur "On a perdu trop de temps..."
    iris determine "Cours !"

    "Nous traversons le couloir principal, puis celui qui mène au secteur d'embarquement. À plusieurs reprises, je crois entendre une voix dans les haut-parleurs, mais le bruit de nos chaussures couvre les annonces."
    "Une vibration profonde traverse le sol. Les parois métalliques résonnent jusque dans ma poitrine."

    kami "Dernière vérification des systèmes terminée. Merci à tous de vous être présentés à l'heure !"

    "Je débouche devant le sas au moment où un panneau passe du vert au rouge. De l'autre côté de la baie, la navette est encore là."
    "Iris frappe contre la vitre du poste de contrôle."

    iris peur "ATTENDEZ ! OUVREZ ! ON EST LÀ !"
    noam colere "KAMI ! ARRÊTE LE DÉCOLLAGE !"

    kami "Oh ! Voilà les retardataires. Vous auriez dû partir un peu plus tôt, mes petits chéris."

    "Les moteurs montent en puissance. Un hublot de la navette donne sur le couloir d'embarquement, et je distingue plusieurs silhouettes derrière la vitre."
    "Au début, je reconnais seulement Tomas, immobile près d'une rangée de sièges. Mara est à côté de lui. Elle tourne la tête quand Iris cogne une nouvelle fois contre la baie."

    iris peur "Ils nous voient ! Noam, ils nous voient !"
    "Je cherche des yeux quelqu'un qui pourrait déverrouiller le sas. À travers les hublots, je distingue Kael, Elias, Sael, Elen et Julian."
    "Puis Lysa."
    "Puis Ryn."

    "Je reste figé. Ryn était enfermé à l'infirmerie, puis nous l'avons aperçu libre. Je n'ai plus aucune idée de ce qui lui est arrivé depuis."
    "Une femme se penche pour regarder dehors, écartant quelqu'un de son chemin."

    noam peur "Non..."

    "Nyra."
    "Je reconnais ses cheveux, la manière dont elle se tient et même le mouvement agacé avec lequel elle repousse la main de son voisin."
    "J'ai vu son crâne ouvert contre une paroi. J'ai vu Sael examiner son corps. Je l'ai laissée morte dans ce conduit."

    iris peur "Noam ? Qu'est-ce que..."

    "Je compte sans m'en rendre compte. Un, deux, trois... Je recommence parce que mes yeux refusent de s'arrêter sur le même visage."
    "Onze personnes attendent dans la navette. Parmi elles, celle qui devrait être morte."
    "Iris fouille les hublots du regard. Elle serre soudain mon poignet si fort que j'en ai mal."

    iris peur "Noam... Là."

    "Je suis la direction de son doigt. Tout au fond, un garçon aux cheveux verts se lève de son siège."
    "Il s'approche de la vitre."
    "Je distingue mon visage. Pas une ressemblance approximative, pas un reflet dans le verre : mes yeux, ma bouche, cette expression que je connais pour l'avoir vue chaque matin dans le miroir."
    "Il s'arrête devant le hublot et nous regarde."
    "Puis il sourit."

    noam peur "C'est... moi ?"

    "Iris recule d'un pas. Son regard passe du garçon dans la navette à moi, puis retourne au hublot."
    iris peur "Pourquoi y a... Pourquoi il te ressemble ?"

    "Je voudrais lui répondre. Je voudrais trouver n'importe quelle explication, même absurde, mais la seule chose que je parviens à faire est de regarder les onze personnes derrière cette vitre."
    "Il y a onze sièges occupés. Tous les représentants, sauf Iris. Et pourtant je suis ici, à côté d'elle."

    kami "Décollage !"

    scene black with vpunch
    "Le grondement des moteurs couvre nos voix. La navette s'écarte lentement du quai, puis accélère jusqu'à disparaître derrière les panneaux du sas."
    "Je frappe la baie du poing. Une fois. Deux fois. Je n'entends même pas les coups."
    "Iris ne bouge plus."
    "À l'endroit où se trouvait la navette, il ne reste qu'un vide lumineux, et le souvenir de ce sourire derrière le hublot."

    noam fatigue "On était là... On y était presque."
    "Iris vient chercher ma main. Elle tremble autant que moi."
    iris peur "Noam... Qu'est-ce qu'ils ont emmené sur Terre ?"

    "Je fixe le sas fermé. Je n'ai aucune réponse."

    $ hideGroup()
    stop music fadeout 2.0
    scene black with fade
    "FIN — LE DÉPART DES AUTRES"
    return


# =============================================================================
# FIN 1B — BARRICADE ÉCHOUÉE : STATION DE PRODUCTION
# =============================================================================

label _30_0_1_1_0_0_FIN_PRODUCTION:
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([
        ("iris", "fatigue", 0.35),
        ("noam", "fatigue", 0.65),
    ])

    "Je tire une dernière fois sur la planche coincée. Elle ne remue pas d'un millimètre. Mes mains sont entaillées et la pince a tordu l'une de ses mâchoires."
    iris fatigue "Noam..."
    noam colere "Attends. Si j'enlève celle-là, je peux peut-être..."
    iris fatigue "Regarde l'heure."

    "Mon téléphone affiche déjà l'heure à laquelle nous aurions dû rejoindre l'embarquement. Je le range aussitôt, comme si ne plus la voir pouvait changer quelque chose."
    "Iris se détourne de moi et rejoint la grille d'aération. Elle reprend les outils, desserre une vis, puis une deuxième."
    "De l'autre côté, un entrelacs de métal empêche toujours le cadre de pivoter. Elle tire dessus jusqu'à perdre sa prise."

    iris colere "Putain !"

    "Le tournevis tombe au sol. Elle reste un moment à regarder ses mains vides, puis s'assoit contre le mur sans même essayer de le ramasser."
    "Je me penche près d'elle. Il y a deux jours, j'aurais insisté pour trouver une troisième solution. Là, je n'arrive même plus à la regarder dans les yeux."

    noam fatigue "Je suis désolé. J'ai choisi la porte."
    iris fatigue "Et moi, j'ai dit que je viendrais avec toi. On a fait comme on pouvait."
    noam inquiet "Il y avait peut-être assez de temps par l'aération."
    iris colere "Arrête. On le saura jamais."

    "Elle essuie ses joues du revers de la manche, agacée contre elle-même. Je m'assois à côté d'elle et pose mes outils entre nous."
    "Le haut-parleur crépite."

    kami "Embarquement terminé ! Je remercie tous les représentants ayant rejoint la navette."
    kami "Décollage dans trois... deux... un !"

    scene black with vpunch

    "La vibration du moteur traverse la chambre malgré les cloisons. Un grondement long, régulier, s'éloigne peu à peu."
    "Je ferme les yeux. Je n'ai pas besoin de voir la navette pour savoir qu'elle est partie."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    $ showGroup([
        ("iris", "peur", 0.35),
        ("noam", "fatigue", 0.65),
    ])

    iris peur "On est toujours là."
    noam fatigue "Ouais."
    iris inquiet "Ils vont pas nous laisser enfermés pour toujours... Pas vrai ?"

    "Je lève les yeux vers la caméra au-dessus de la porte. Sa petite lumière est allumée."
    noam colere "Kami ! La navette est partie ! Qu'est-ce qu'on est censés faire, maintenant ?"
    iris colere "Tu peux au moins nous sortir de cette chambre !"

    "Quelques secondes passent. Puis la voix de Kami remplit la pièce, enjouée comme au premier jour."

    kami "Mais enfin, pourquoi tant d'inquiétude ? Vous n'allez tout de même pas croire que je vais abandonner deux de mes représentants préférés !"
    noam inquiet "Tu vas envoyer une autre navette ?"
    kami "Évidemment ! Une autre rotation est prévue. Vous pourrez embarquer tous les deux."

    "Iris se tourne vers moi. Je vois son visage se décomposer de soulagement, si brusquement qu'elle peine à reprendre son souffle."
    "Elle me serre dans ses bras. Je lui rends son étreinte sans pouvoir m'empêcher de rire, un son étranglé qui ressemble presque à un sanglot."

    iris peur "On va partir... Noam, on va quand même partir..."
    noam fatigue "Ouais. Ouais, j'ai cru qu'on allait rester ici..."

    kami "Petite précision, toutefois ! La prochaine navette ne dessert pas la Terre."

    "Iris s'immobilise contre moi."
    noam inquiet "Comment ça ?"
    kami "Elle transporte les robots du Conclave vers une station de production. Vous voyagerez avec eux. C'est très pratique : il reste de la place !"
    iris colere "Non. On veut rentrer sur Terre. C'était le principe depuis le début !"
    noam colere "Tu nous avais promis qu'on repartirait après le dernier vote !"

    kami "Et je vous propose de repartir, Noam ! Tu ne vas quand même pas discuter chaque détail de l'itinéraire ?"
    noam colere "Une station de production, c'est pas la Terre !"
    kami "Oh, mais tu sais combien ça coûte, d'organiser un tel trajet ? Une navette entière pour deux personnes ?! Un peu de bon sens, voyons !"

    "Je regarde Iris. Ses bras ont glissé le long de son corps. Elle ouvre la bouche, puis la referme, incapable de trouver quelque chose à répondre."

    iris desaccord "On n'a rien demandé de tout ça. On veut juste rentrer chez nous."
    kami "Et moi, je veux éviter le gaspillage. Tu vois ? Nous avons tous nos petites envies !"

    "Un nouveau silence tombe dans la chambre. Le moteur de la navette pour la Terre n'est déjà plus audible."
    "Je voudrais savoir où se trouve cette station, qui y travaille et pourquoi on y envoie les robots. Je voudrais surtout savoir si nous en reviendrons."
    "Mais Kami fredonne déjà un air joyeux, comme si la conversation était terminée."

    kami "Encore un petit peu de patience, les enfants. Votre transport arrivera en temps voulu !"

    "Iris reprend lentement ma main. Elle ne sourit plus."
    iris fatigue "Noam..."
    "Je serre ses doigts sans répondre. De l'autre côté de la porte, la barricade n'a pas bougé."

    $ hideGroup()
    stop music fadeout 2.0
    scene black with fade
    "FIN — DESTINATION INCONNUE"
    return


# =============================================================================
# BRANCHE 2 — VENTILATION : RENCONTRE AVEC L'ORIGINEL
# =============================================================================

label _30_0_1_1_0_0_VENTILATION:
    $ current_period = "Matin"
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    $ showGroup([
        ("iris", "determine", 0.35),
        ("noam", "inquiet", 0.65),
    ])

    "Iris récupère la pince et les deux tournevis que nous avons rapportés de la maintenance. Elle se place devant la grille, pousse son pied contre le mur et commence à travailler."
    "Je retire les vis accessibles pendant qu'elle essaie de soulever le cadre avec un outil plat."

    iris colere "Encore ! Fais levier de ton côté !"
    noam inquiet "Je force déjà !"
    iris colere "Alors force plus !"

    "La plaque grince. Un rivet casse près de mon visage et ricoche sur le sol. Iris lâche un juron, mais ne relâche pas sa prise."
    "Nous tirons ensemble. Le cadre cède enfin, emportant une partie des fixations ajoutées derrière."

    play sound sfx_creak volume 0.55

    "Une odeur de métal tiède et de poussière enfermée nous parvient du conduit. Je passe la lampe à Iris ; elle vérifie que le passage est assez large."
    iris determine "Vas-y. Je te suis juste derrière."
    noam desaccord "Non, toi d'abord. Si ça se bloque, je pourrai pousser le cadre d'ici."
    iris colere "Tu vas pas recommencer à discuter !"
    noam determine "Je te lâcherai pas. Avance."

    "Elle finit par se glisser dans l'ouverture. Je récupère les outils, jette un dernier regard à la porte de sa chambre et rampe à sa suite."
    "La lumière de la lampe frappe des boulons, de vieilles traces de graisse et les angles métalliques qui nous ont si longtemps empêchés de dormir."

    $ hideGroup()
    scene black with dissolve

    "Iris progresse devant moi. Le conduit est trop étroit pour que nous nous retournions facilement, et chaque fois qu'elle ralentit, je dois m'arrêter en serrant les coudes contre mes côtes."
    "Nous atteignons une bifurcation. À gauche, le passage rejoint le secteur de maintenance. À droite, il doit nous rapprocher de la zone d'embarquement."

    iris inquiet "On va à droite ?"
    noam reflexion "Je crois. Elias avait parlé d'un conduit qui longe le sas principal."
    iris colere "Elias... Super référence."

    "Je ne réponds pas. Même maintenant, je pense parfois à l'Elias qui m'expliquait avec enthousiasme ses bricolages, et je n'arrive pas à faire tenir cette image avec son visage entre les planches."
    "Iris s'arrête si brusquement que je manque de lui rentrer dedans."

    noam inquiet "Qu'est-ce qu'il y a ?"
    iris peur "Éclaire devant moi."

    "Je tends le bras par-dessus son épaule. La lumière glisse sur un coude du conduit, s'arrête sur une chaussure, puis sur une jambe repliée dans un angle impossible."
    "Iris reste immobile. Je reconnais les vêtements avant de voir le visage."

    noam peur "Ryn... ?"

    "Il est couché sur le côté, une épaule coincée contre la paroi. Du sang a séché autour de son cou et sur le métal sous sa tête."
    "Une plaie profonde traverse sa gorge. Ses yeux sont ouverts, mais ils ne suivent pas la lampe quand je l'approche."
    "Je me penche malgré moi vers lui, comme si je pouvais encore y trouver un souffle. Je n'ai pas besoin de le toucher pour comprendre."

    iris peur "Non... Il était à l'infirmerie. Il nous a parlé hier matin..."
    noam inquiet "Il est sorti dans l'après-midi. On l'a vu avec Elias."
    iris peur "Je sais ce qu'on a vu ! C'est pas ça... Regarde-le !"

    "Elle recule jusqu'à heurter mon épaule. Ses yeux restent rivés à la blessure."
    "Le Ryn que j'ai interrogé hier a reconnu avoir fracassé le crâne de Nyra. Celui-ci est étendu ici, la gorge ouverte. Je ne peux même pas savoir depuis combien de temps."
    "Je repense à ses aveux, à la rapidité avec laquelle il avait changé de version. Mon estomac se soulève."

    noam peur "Je comprends plus rien..."
    iris colere "On doit continuer. On peut pas rester là."

    "Elle essaie de se glisser à côté du corps, mais il bouche presque tout le passage. Je l'aide à déplacer son bras, avec cette précaution absurde qu'on garde devant quelqu'un qui pourrait avoir mal."
    "La peau est froide. Je retire aussitôt ma main et me cogne le coude contre la paroi."
    "Iris parvient enfin à franchir l'obstacle. Je la suis, le souffle court, et m'arrête quelques mètres plus loin pour reprendre ma respiration."

    "J'entends Iris respirer trop vite devant moi. Puis un bruit humide, brutal, résonne contre le fond du conduit."
    noam inquiet "Iris ?"
    iris peur "Avance pas... Attends..."

    "Elle est penchée sur le côté, une main plaquée sur la bouche. Elle vomit entre les deux rails métalliques, puis essuie son visage avec sa manche en tremblant."
    "Je lui tends ma gourde. Elle en prend une gorgée et me la rend sans me regarder."

    iris fatigue "J'ai cru que j'allais tenir."
    noam fatigue "T'as rien à prouver."
    iris colere "Je veux juste sortir d'ici."

    "Nous reprenons notre progression. Le conduit descend légèrement, puis s'élargit assez pour que nous avancions à genoux. Une lumière pâle traverse les fentes d'une grille au-dessus de nos têtes."
    "Iris passe la première. Elle s'arrête encore. Cette fois, elle ne me demande même pas d'éclairer."

    iris peur "Noam... S'il te plaît, regarde pas."

    "Je regarde."
    "Une silhouette est étendue contre une plaque d'accès, presque dissimulée derrière un amas de câbles. Ses cheveux noirs lui couvrent le visage."
    "Je reconnais Lysa au col de son vêtement et à sa manière de garder les manches rabattues sur ses mains. Même inerte, ces détails me frappent avec une précision insupportable."
    "Sa tête repose de travers, dans une position que son cou ne devrait pas permettre."

    noam peur "Lysa..."

    "Hier soir, quelqu'un portant son visage se tenait devant notre porte. Sa voix nous demandait de répondre, et nous sommes restés silencieux parce que nous avions peur."
    "Je me rappelle chaque coup frappé contre le battant. La façon dont elle avait prononcé mon nom."

    noam peur "Elle est venue hier... Elle nous a parlé..."
    iris inquiet "Noam, je sais."
    noam colere "Alors qui est là ?!"

    "Je me retourne vers elle. Je ne cherche pas vraiment une réponse ; je voudrais seulement qu'elle me dise que ce corps est une erreur, qu'il existe une explication que nous n'avons pas encore trouvée."
    "Mais Iris est aussi pâle que moi."
    iris peur "J'en sais rien."

    "Je touche la paroi pour ne pas tomber. Ma gorge se contracte et je vomis à mon tour, presque sans avoir eu le temps de me pencher."
    "Iris tient la lampe loin de mon visage et attend. Elle ne me demande pas de me dépêcher."
    "Quand je parviens à me relever, mon téléphone indique que le départ approche. Nous avons perdu de précieuses minutes, mais je n'arrive pas à m'excuser de m'être arrêté devant eux."

    iris fatigue "On pourra plus les aider."
    noam fatigue "Je sais."
    iris determine "Alors viens. Tant qu'on peut encore sortir."

    "Elle me tend la main. Je la prends, et nous contournons le corps de Lysa sans parvenir à lui adresser un dernier regard."
    "Le conduit se redresse après un embranchement. De l'air plus frais descend vers nous, accompagné d'un grondement lointain qui ressemble à celui d'une turbine."
    "Nous devons être proches du secteur d'embarquement."

    "Iris relève la tête. Quelqu'un se tient debout à l'autre bout de la section élargie."
    "Je vois d'abord des chaussures. Puis des jambes, des mains et un visage que je connais aussi bien que le mien depuis ces derniers jours."

    "Iris."

    "Pas celle qui tient ma main. Une autre."

    $ showGroup([
        ("iris", "peur", 0.22),
        ("iris", "sourire", 0.78),
    ])

    "La véritable Iris s'arrête net. Ses doigts se referment sur les miens tandis qu'elle regarde l'autre fille, immobile à quelques mètres de nous."
    "L'inconnue possède ses cheveux, ses vêtements, jusqu'à cette petite façon de pencher la tête lorsqu'elle attend une réponse."
    "Elle nous observe en souriant."

    iris peur "C'est quoi... cette blague ?"

    "L'autre Iris ne répond pas. Elle avance d'un pas."
    iris colere "Reste où t'es !"

    "Je recule malgré moi. L'autre avance encore, calmement, en regardant tour à tour mon visage et celui d'Iris."
    "Iris lève son tournevis."
    iris determine "Un pas de plus et je te jure que..."

    "La silhouette bondit."

    scene black with hpunch
    play sound sfx_creak volume 0.4

    "Iris me repousse contre le mur et se jette au-devant d'elle. Les deux corps heurtent la paroi avec un choc qui fait vibrer les plaques du conduit."
    "Je distingue deux visages identiques, si proches l'un de l'autre que je perds pendant un instant le fil de leurs mouvements."
    "La véritable Iris tente d'enfoncer le tournevis dans l'épaule de son adversaire. L'autre bloque son poignet et lui tord le bras."

    iris colere "LÂCHE-MOI !"

    "Iris donne un coup de genou et parvient à se dégager. Les deux reculent, reprennent leur souffle et se précipitent de nouveau l'une sur l'autre."
    "Je voudrais intervenir, mais chaque fois que je crois reconnaître Iris à sa voix, l'autre se met à crier exactement de la même manière."
    "Elles se heurtent à une conduite latérale. L'une tombe à genoux, l'autre la tire par le col."

    noam peur "ARRÊTEZ !"

    "Personne ne m'écoute. Je vois le tournevis glisser sur le sol, hors de leur portée, et comprends que la prochaine personne à tomber risque de se fracasser le crâne contre une arête métallique."
    "Je m'élance. J'attrape l'épaule de celle qui a le dessus pour la tirer en arrière."

    scene black with vpunch

    "Une chaleur étrange me traverse la paume. Ce n'est pas une douleur : plutôt une vibration, comme si une machine venait de démarrer sous mes doigts."
    "La peau que je tiens se contracte. Sous ma main, l'épaule change de volume. Les cheveux raccourcissent, les traits du visage se déplacent et les vêtements s'ajustent à une silhouette que je reconnais aussitôt."

    "La personne se retourne vers moi."
    "Je regarde mon propre visage."

    $ showGroup([
        ("iris", "peur", 0.22),
        ("noam", "inquiet", 0.78),
    ])

    noam peur "Qu'est-ce que..."
    iris peur "Noam ! Recule !"

    "L'autre moi me dévisage un instant, comme s'il cherchait quelque chose dans mes yeux. Puis il sourit avec ma bouche et se tourne vers Iris."
    "Je recule jusqu'au mur. Mes jambes ne semblent plus capables de porter mon poids."

    kami "Attention, chers passagers ! Le départ de la navette est imminent. Veuillez terminer votre embarquement !"

    "Le message résonne dans tout le conduit. Iris jette un regard vers la grille qui mène au secteur d'embarquement, puis revient immédiatement vers l'inconnu."

    iris colere "T'es pas Noam. T'es pas moi non plus. Qu'est-ce que t'es ?!"

    "Il ne répond pas. Il se rue sur elle, mais elle l'attend : elle se baisse au dernier moment et le projette contre une plaque de ventilation."
    "Le métal se déforme sous son dos. Iris récupère son tournevis et lui bloque le bras avec son genou."

    iris determine "NOAM, VA-T'EN !"
    noam colere "Je te laisserai pas !"

    "L'autre tente de se relever. Iris lui écrase le poignet contre la paroi, l'empêchant d'atteindre la sortie. Pendant quelques secondes, elle semble réellement prendre le dessus."
    "Puis il tend l'autre main vers le sol, tâtonnant parmi les outils tombés pendant la lutte."
    "Ses doigts rencontrent un vieux chiffon coincé sous une caisse technique. Il est marqué au feutre d'un nom que je distingue seulement lorsqu'il l'arrache : Tomas."
    "L'inconnu le serre dans son poing."

    "Son corps change de nouveau."

    "Ses épaules s'élargissent, ses bras gonflent sous le tissu, sa taille augmente jusqu'à ce qu'il doive courber la tête pour ne pas heurter le plafond du conduit."
    "Son visage reprend d'autres proportions, étrangères à celles que je viens de voir. Il a désormais la carrure et les traits de Tomas."
    "Iris écarquille les yeux. Elle essaie de reculer, trop tard."

    scene black with hpunch

    "Il se dégage d'un mouvement brutal et lui assène un coup qui résonne contre le métal. Iris s'effondre sans un cri. Son tournevis roule jusqu'à mes pieds."

    noam peur "IRIS !"

    "Je me précipite vers elle. Elle respire, mais ne réagit pas lorsque je prends son visage entre mes mains. Une marque sombre apparaît près de sa tempe."
    "Je tente de la soulever. Une main se referme sur mon col et m'arrache à elle."

    "Je me débats, frappe le bras qui me retient, cherche un appui sur la paroi. Rien ne le fait lâcher."
    "Son visage est celui de Tomas, mais ses yeux me regardent comme ceux du garçon qui portait mon visage un instant plus tôt."

    noam colere "Lâche-la ! Qu'est-ce que tu lui as fait ?!"

    "Il me soulève assez pour que mes pieds quittent presque le sol. Son expression se durcit, pour la première fois débarrassée de ce sourire qui semblait collé à tous les visages qu'il a portés."

    "???" "Vous ne m'empêcherez pas de les libérer !"

    "Je voudrais lui demander qui il veut libérer. Je voudrais comprendre pourquoi Ryn et Lysa sont morts, pourquoi des gens impossibles sont apparus parmi nous, pourquoi Iris vient de tomber sous mes yeux."
    "Je n'en ai pas le temps."

    scene black with vpunch
    stop music fadeout 0.5

    "Un choc traverse mon crâne. La main qui tenait mon col disparaît et mes genoux heurtent quelque chose de dur."
    "Je cherche Iris du regard, mais la lumière se dédouble. Je distingue seulement sa main posée au sol, à quelques centimètres du tournevis."
    "J'essaie de prononcer son nom. Aucun son ne sort."
    "Puis tout s'éteint."

    scene black with fade
    "FIN — CEUX QU'IL VEUT LIBÉRER"
    return
