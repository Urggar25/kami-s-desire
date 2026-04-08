label _4_0_REVEIL_CHAMBRE:

    scene bg_cg012 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4

    pause 1.5  # Légèrement plus long pour accentuer la lourdeur

    $ blink()
    "Je me réveille… ou plutôt, je reviens à moi."
    $ blink()
    "La lumière bleue des veilleuses est toujours là, mais aujourd’hui elle donne l’impression d’un néon fatigué qui clignote à peine."

    "Hier, on a voté."
    "On a eu une chance. Une vraie."
    "Et on l’a laissée filer."
    "Le bouton vert est resté éteint. Au moins l'un d'entre nous a dit non."
    "Et le monde continue de tourner exactement comme avant."

    $ blink()
    "Je reste immobile, les bras morts le long du corps."
    "Mon cœur bat lentement, presque à contrecœur, comme s’il économisait ses forces pour une journée qui ne vaut pas la peine d’être vécue."

    "On a gardé les bons de rationnement."
    "On a gardé la sécurité."
    "Mais on a aussi gardé nos chaines."

    $ blink()
    pause 2.5  # Pause plus longue pour laisser peser le vide

    "Je me tourne à moitié. Une photo holographique est sur la table de nuit me fixe."
    "Ca me fait penser que je n'ai même pas déballé mes affaires en arrivant ici."
    "Alors qui a installé ça ?"

    pause 1.0
    "Quelqu'un s'est permis de fouiller ?!"

    pause 1.0
    "Vu ce qu'on vit, à quoi bon se plaindre ..."

    "Sur la photo, il y a une famille souriante. Pas la mienne. Ce sont des amis."
    "Je me demande si eux aussi ont un bon de rationnement ce matin."
    "Ou si, quelque part, ils ont déjà arrêté de sourire depuis longtemps."

    play sound sfx_announce
    "Un bip strident déchire le silence."
    "L’écran s’allume brutalement, lumière blanche et clinique."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bonjour, mes petits anges de la prudence !"
    kami "Il est 8 heures, et devinez quoi ? La révolution est officiellement annulée !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit briefing matinal, parce que je sais que vous raffolez quand je vous rappelle à quel point vous êtes raisonnables :"
    kami "La situation est toujours impeccables. Pas une pièce qui circule, pas une once de liberté."
    kami "Vous avez l'avez voulu, vous l'aurez !."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "C’est beau, non ? Le calme avant… ben, le calme, en fait."
    kami "Pas d’alarme, pas de chaos."
    kami "Juste la douce certitude que demain sera exactement comme aujourd’hui."
    kami "Alors, je tiens à tous vous remercier :"
    kami "Merci de m'avoir donné raison. L'humanité ne veut pas de cette liberté que vous dites pourtant chérir."
    kami "Elle est bien moins importante que le certitude de pouvoir être nourris."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Allez, ne faites pas cette tête !"
    kami "Vous verrez tout ça de vos propres yeux à la cafétéria. Les écrans sont chauds, vos rations sont prêtes."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    "L’écran s’éteint. Le silence retombe, épais comme du béton."
    "Je reste assis, les mains posées sur mes genoux, inertes."
    "Elle n’a même pas besoin de mentir."
    "On n’a rien changé. Et on n’a même pas le courage de le regretter à voix haute."

    pause 1.8

    play sound sfx_drop
    "Un bruit mat dans le couloir. Comme un poing contre du métal."
    "Un cri bref, étouffé, presque honteux."
    "Puis plus rien."

    "Je me lève lentement. Pas d’un bond. Pas la force."
    "Mon cœur cogne, mais c’est un cognement fatigué."
    "Je tends l’oreille. Silence."
    "Juste l’écho de ce cri, et la certitude que ce n’est que le début de quelque chose qui se fissure sans bruit."

    "Ça n’a pas encore explosé."
    "Mais ça pourrait à tout moment."

    jump _4_0_CAFETERIA_ECRANS

label _4_0_CAFETERIA_ECRANS:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 0.8

    "À peine entré dans la cafétéria, je remarque l’attroupement près du grand comptoir central."

    scene bg_cg022 at adaptive_fullscreen with dissolve  # CG spéciale de la scène au comptoir
    $ unlock_gallery_image("bg_cg022")

    elen "Allez Goumi, s’il te plaît ! Juste un tout petit peu de cannelle ! Ou même du poivre !"
    elen "Ça fait des mois que je rêve d’un truc qui ait vraiment du goût !"

    goumi "Demande refusée, représentante Elen."
    goumi "Les provisions restantes du Conclave ont été redirigées vers la Terre ce matin."

    elen "Quoi ?! Mais… on n’a presque rien ici !"

    elias "Moi je voulais juste des barres protéinées un peu meilleures… celles qu’on a sont dégueulasses !"

    nyra "Elen, Elias… calmez-vous. Goumi ne fait qu’appliquer les ordres."

    goumi "Ordre direct de Kami. Priorité absolue à la distribution planétaire."

    elen "Mais c’est injuste ! On est coincés ici et on n’a même pas le droit à un petit quelque chose de différent ?!"

    elias "Ouais, on est censés représenter tout le monde et on bouffe la même merde que les autres ?!"

    nyra "Ce n’est pas en criant que ça va changer quoi que ce soit…"

    elen "…Je voulais juste que ça ait un peu de goût pour une fois."

    play sound sfx_announce
    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oh là là, ma petite Elen… toujours à pleurnicher pour tes petites épices de luxe ?"
    kami "C’est tellement mignon. Tellement… humain."
    kami "Mais il faut bien que tout le monde participe un minimum à l’effort collectif, non ?"
    kami "Le Conclave ne doit pas devenir un petit paradis pour privilégiés pendant que la Terre se serre la ceinture."
    kami "C’est une question d’équité. De justice. De sacrifice partagé."
    kami "Ne vous inquiétez pas trop… de nouvelles provisions arriveront au Jour 7."
    kami "En attendant, contentez-vous de ce que vous avez. Comme tout le monde."
    kami "Et surtout… comme vous l’avez vous-mêmes décidé hier."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    "L’écran s’éteint."

    "Elen reste figée deux secondes, les yeux brillants de larmes de rage et de déception."
    "Puis elle tourne les talons et quitte la cafétéria presque en courant, la tête baissée comme une petite fille qui vient de se faire humilier devant tout le monde."

    $ showP("mara", "agace", 0.70)
    mara "…Génial. Voilà qu’elle boude comme une gamine maintenant."

    $ showP("julian", "decu", 0.50)
    julian "On ne peut même plus avoir un peu de goût dans nos rations ?"
    julian "C’est ça, notre grande victoire d’hier ?"

    $ showP("ryn", "colere", 0.12)
    ryn "Bravo. On a voté pour la sécurité et on se fait traiter comme des chiens par une IA."
    ryn "On mérite vraiment tout ce qui nous arrive."

    "Je reste planté là, ma ration tiède entre les mains. L’ambiance est déjà irrespirable."

    pause 1.2

    "Les écrans muraux s’allument enfin, montrant les mêmes images que tous les jours :"
    "Rien n'a changé. Les files d'attente sont longues."
    "Il n'y a rien d'autre à manger qu'un bout de pain déjà sec depuis deux jours ..."

    hide julian
    $ showP("lysa", "determine", 0.50)
    lysa "Tout est parfaitement normal."
    lysa "Comme hier. Comme demain. Comme dans six mois."

    hide mara
    $ showP("kael", "calme", 0.88)
    kael "C’est stable. C’est ce qu’on a voté."

    $ showP("ryn", "colere", 0.12)
    ryn "Stable ? On crève lentement et poliment, oui !"

    hide lysa
    $ showP("iris", "desaccord", 0.50)
    iris "Les pauvres continuent à crever devant les mêmes murs. Rien ne change jamais."

    hide kael
    $ showP("julian", "decu", 0.88)
    julian "On avait une chance de faire bouger les choses… et on l’a laissée passer."

    "Je pose ma ration intacte sur la table."

    hide ryn
    $ showP("lysa", "blase", 0.30)
    lysa "Alors Noam ?"
    lysa "Tu regrettes qu’on n’ait pas osé ? Ou tu es soulagé qu’on ait préféré rester dans nos petites chaînes bien confortables ?"

    noam "Je… je ne sais plus."
    noam "Je me demande si... ne rien risquer hier... c’était du confort. Ou juste de la peur."

    hide lysa

    "La salle est silencieuse. Chacun fixe les écrans comme une sentence qu’on s’est nous-mêmes infligée."
    "On n’a rien gagné hier."
    "On a juste réussi à rester exactement au même endroit… en sachant qu’on aurait pu faire mieux."

    jump _4_0_TEMPS_LIBRE_1

label _4_0_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Après le petit-déjeuner, j'ai un peu de temps devant moi."
    "Je ne sais pas enncore quoi faire."

    call START_FREE_TIME("_4_0_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_4_0

label _4_0_RETOUR_CONCLAVE_ANALYSE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.8

    pause 1.2

    "L’après-midi traîne."
    "Pas vraiment calme. Pas vraiment vivant non plus."
    "Juste ce moment bizarre où plus personne ne sait quoi faire de sa colère."

    play sound sfx_announce
    pause 1.1

    "Le signal me vrille les oreilles."
    "Je sursaute."
    "Putain."

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention à tous mes petits représentants…"
    kami "Je vous attends dans la salle principale."
    kami "Et cette fois, j’aimerais éviter le petit numéro pathétique des gens qui boudent dans leur chambre."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On a un nouveau vote à préparer."
    kami "Alors vous marchez."
    kami "Ou je viens vous chercher avec les caméras braquées sur votre tronche."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L’écran se coupe."
    "Plus un bruit."
    "Puis des portes s’ouvrent, une à une, quelque part dans le couloir."
    "Des pas. Lents. Pas pressés."
    "On dirait moins un rassemblement qu’un transfert de détenus."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.2

    "Quand j’entre, personne ne parle."
    "Ryn est déjà là, collé au mur, les bras verrouillés sur son torse."
    "Kael garde les yeux baissés."
    "Nyra regarde l’écran noir comme si elle attendait déjà le prochain mauvais coup."
    "Tomas s’attaque à son ongle sans même s’en rendre compte."
    "Et au fond, il y a un siège vide."
    "Celui de Julian."

    "Elen arrive la dernière."
    "C'est bizarre, ça contraste fortement avec son attitude des derniers jours."
    "Là, non."
    "Elle s’assoit. C’est tout."

    $ showP("ryn", "colere", 0.50)
    ryn "Bon."
    ryn "On y est."

    $ showP("kael", "inquiet", 0.88)
    kael "Julian ne viendra pas."
    kael "J’ai frappé."
    kael "Il m’a juste dit de le laisser tranquille."

    "Personne ne commente."
    "Même Mara ne saute pas tout de suite sur l’occasion."
    "Ça en dit déjà long."

    $ showP("mara", "agace", 0.12)
    mara "Super."
    mara "Le grand architecte du changement s’effondre au premier mur."
    mara "C’était donc ça, notre pseudo leader."

    hide kael
    $ showP("tomas", "hesitation", 0.88)
    tomas "M-Mara…"

    $ showP("mara", "agace", 0.12)
    mara "Quoi ?"
    mara "On va encore faire semblant que tout va bien ?"

    "Elen ne relève même pas."
    "Elle garde les yeux fixés sur la table, comme si elle essayait juste de tenir assise."

    hide tomas
    $ showP("nyra", "raison", 0.88)
    nyra "Ça sert à rien de tirer sur une chaise vide."
    nyra "Elle ne votera pas mieux."

    "Ryn souffle du nez."
    "Un rire sans humour."

    $ showP("ryn", "colere", 0.50)
    ryn "Ouais."
    ryn "Et nous, on est là à continuer ce putain de cirque."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Parfait."
    kami "Les survivants émotionnels sont installés."
    kami "Passons donc à la suite de votre petite aventure démocratique."

    kami "Prochain vote :"

    play sound sfx_tambour
    pause 2.2

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser ou non les déplacements entre les districts ?"
    kami "Oui : libre circulation entre tous les districts."
    kami "Non : les frontières restent fermées comme aujourd’hui."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "C’est simple."
    kami "Même vous devriez réussir à comprendre celui-là."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    "Deux boutons apparaissent à l’écran."
    "Vert. Rouge."
    "On dirait presque un jeu."
    "Presque."

    pause 0.8

    "Personne ne parle."
    "Le mot frontières reste suspendu dans la pièce comme une odeur de brûlé."

    $ showP("lysa", "blase", 0.12)
    lysa "Vous êtes sérieux…"
    lysa "On sort à peine du désastre d’hier et on enchaîne direct sur ça ?"

    $ showP("iris", "desaccord", 0.88)
    iris "C’est n’importe quoi."
    iris "Genre, vraiment n’importe quoi."

    $ showP("elias", "determine", 0.50)
    elias "N’importe quoi, peut-être."
    elias "Mais pas inutile."

    hide iris
    $ showP("kael", "inquiet", 0.88)
    kael "Libre circulation..."
    kael "Entre tous les districts..."
    kael "Comme ça."

    hide elias
    $ showP("ryn", "colere", 0.50)
    ryn "Oui. Comme ça."
    ryn "Parce que ça fait des années qu’on nous apprend à vivre séparés comme du bétail bien rangé."
    ryn "Et parce qu’à Limen, les frontières, c’est pas une ligne sur une carte."
    ryn "C’est des types armés."
    ryn "C’est des gens qu’on enterre."
    ryn "C’est des gosses qui grandissent en pensant que de l’autre côté, y a forcément un ennemi."
    ryn "Donc ouais."
    ryn "Moi, je vote oui."

    "Sael n’a toujours pas bougé."
    "Puis elle lève enfin les yeux."
    "Et là, c’est pas de la colère que je vois d’abord."
    "C’est pire."
    "C’est quelqu’un qui a déjà vu ce qui arrive quand on ouvre trop grand une porte."

    hide kael
    $ showP("sael", "mefiant", 0.88)
    sael "Tu parles comme si ces frontières étaient gratuites."
    sael "Comme si elles étaient là pour le plaisir de nous punir."

    $ showP("ryn", "colere", 0.50)
    ryn "Tu veux qu’on dise quoi ? Merci ?"

    $ showP("sael", "determine", 0.88)
    sael "Je veux que tu arrêtes de faire semblant de ne pas savoir."
    sael "Les lignes ont été tracées dans le sang."
    sael "Des Gardiens sont morts pour les tenir."
    sael "Des villages entiers ont été rayés pour éviter que ça déborde."
    sael "Chez nous, on n’ouvre pas un passage parce qu’on se sent à l’étroit pendant une semaine."

    hide lysa
    $ showP("elias", "determine", 0.12)
    elias "Et chez nous, on crève aussi à rester chacun dans notre coin."

    $ showP("sael", "mefiant", 0.88)
    sael "Alors crève avec tes certitudes."
    sael "Mais ne demande pas aux autres de te suivre."

    "Le ton tombe d’un coup."
    "Net."
    "Tomas retire sa main de sa bouche."
    "Même Nyra cesse de sourire."

    hide elias
    $ showP("lysa", "blase", 0.12)
    lysa "Le problème, c’est qu’on n’a même pas survécu à une histoire de rationnement."
    lysa "Et là vous proposez de mélanger les districts comme si on était capables de gérer quoi que ce soit."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce qu’on doit attendre quoi, hein ?"
    ryn "Que tout soit parfait ?"
    ryn "Que Kami nous tienne encore dix ans en laisse avant qu’on mérite de respirer ?"

    hide lysa
    $ showP("iris", "desaccord", 0.12)
    iris "Respirer pour qui ?"
    iris "Parce que ce ne sera pas les plus solides qui se feront écraser, comme d’habitude."

    hide iris
    $ showP("nyra", "raison", 0.12)
    nyra "Le vrai problème, c’est pas juste ouvrir ou fermer."
    nyra "Le vrai problème, c’est qu’on n’a aucun cadre."
    nyra "Aucune règle de passage."
    nyra "Aucun contrôle."
    nyra "Rien."
    nyra "On nous balance un bouton, et débrouillez-vous."

    $ showP("ryn", "colere", 0.50)
    ryn "Parce que fermer, ça, c’est un cadre peut-être ?"
    ryn "Interdire, abattre, isoler ?"
    ryn "Vous appelez ça une société ?"

    $ showP("sael", "determine", 0.88)
    sael "J’appelle ça une digue."

    pause 0.5

    $ showP("sael", "mefiant", 0.88)
    sael "Et vous..."
    sael "Vous me faites tous peur."

    "Le silence qui suit n’a rien à voir avec les précédents."
    "Celui-là coupe."
    "Net."

    $ showP("sael", "determine", 0.88)
    sael "Hier, vous avez reculé devant un changement économique."
    sael "Aujourd’hui, vous voulez faire sauter les frontières."
    sael "Vous ne réfléchissez pas."
    sael "Vous compensez."
    sael "Vous cherchez un grand geste pour oublier que vous avez échoué."

    "Le siège vide de Julian me saute à la gorge."
    "Personne ne regarde dans sa direction."
    "Tout le monde y pense."

    $ showP("ryn", "colere", 0.50)
    ryn "Non."
    ryn "Moi, j’en ai juste marre de vivre dans une cage."

    $ showP("sael", "determine", 0.88)
    sael "Alors vote oui."
    sael "Mais ne compte pas sur moi pour ouvrir la porte."

    $ showP("sael", "colere", 0.88)
    sael "Je voterai contre."

    pause 0.2

    sael "Et cette fois, je ne bougerai pas."

    hide sael
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Sael se lève d’un coup."
    "La chaise racle violemment le sol."
    "Puis la porte claque."
    with hpunch
    with vpunch

    pause 0.6

    $ showP("mara", "agace", 0.88)
    mara "Mais c’est pas vrai..."
    mara "Vous savez faire autre chose que tout cramer ?!"
    mara "Un vote foire et maintenant tout le monde veut régler ses névroses sur le suivant ?!"

    hide mara
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Mara part juste après elle, presque en rage."

    "La salle reste ouverte."
    "Mais plus vraiment habitable."

    $ showP("tomas", "hesitation", 0.88)
    tomas "Je..."
    tomas "Je crois qu’on va trop vite."

    $ showP("ryn", "colere", 0.50)
    ryn "On va surtout nulle part."
    ryn "Comme d’habitude."

    hide tomas
    $ showP("kael", "inquiet", 0.88)
    kael "Elle n’a pas totalement tort."
    kael "On est déjà au bord de la rupture."
    kael "Et on parle d’effacer les seules limites que tout le monde connaît depuis toujours..."

    $ showP("nyra", "raison", 0.12)
    nyra "Le plus drôle, c’est qu’on n’a même pas commencé le vrai débat."
    nyra "Et pourtant, on sait déjà exactement comment ça va finir."

    "Elen bouge enfin."
    "À peine."
    "Elle relève la tête, cligne des yeux, regarde la porte par laquelle Sael vient de sortir."

    hide ryn
    $ showP("elen", "triste", 0.50)
    elen "On dirait..."
    elen "On dirait qu’on se déteste de plus en plus vite."

    "Personne ne lui répond."
    "Parce que pour une fois, elle a visé juste du premier coup."

    "Je regarde les sièges vides."
    "Julian."
    "Sael."
    "Mara."

    "Trois absences."
    "Et le vote n’a même pas commencé."

    "J’ai un nœud dans le ventre."
    "L’impression très nette qu’on n’est pas en train de préparer une décision."
    "On est en train de choisir la forme exacte de notre prochain désastre."

    jump _4_0_APRES_CLASH_PRE_FETE

label _4_0_APRES_CLASH_PRE_FETE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 2.0

    pause 2.5

    "La porte est fermée."
    "Mais l'écho du claquement est encore là."
    "Quelque chose dans l'air a changé. Pas de façon dramatique."
    "Juste… une fissure de plus dans quelque chose qui n'était déjà plus solide."

    pause 1.0

    "Les sièges vides s'accumulent."
    "Julian. Sael. Mara."
    "Trois chaises tournées vers le néant."
    "Et nous, les survivants, on reste là à fixer la table comme si elle allait nous donner les réponses."

    pause 1.2

    $ showP("ryn", "colere", 0.12)
    ryn "Super."
    ryn "On a réussi à se déchirer avant même de voter."

    $ showP("tomas", "hesitation", 0.88)
    tomas "C'est… c'est pas ce qu'on voulait."

    ryn "Et pourtant."

    "Ryn se lève. Pas pour partir. Juste parce que rester assis est insupportable."
    "Il fait deux pas vers la fenêtre opaque, les bras croisés, la nuque raide."

    hide tomas
    $ showP("kael", "inquiet", 0.50)
    $ showP("nyra", "fatigue", 0.88)
    kael "On devrait peut-être… essayer de les rejoindre ?"
    kael "Parler à Sael. Lui expliquer qu'on n'attaquait pas ses Gardiens."

    nyra "Tu as entendu sa voix quand elle est partie ?"
    nyra "Ça ne servira à rien ce soir."

    "Kael acquiesce sans conviction."
    "Il sait que Nyra a raison. Mais admettre qu'on ne peut rien faire, c'est encore pire."

    hide ryn
    hide kael

    pause 0.8

    "Je regarde Elen."
    "Elle est assise, les coudes sur les genoux, le regard posé sur ses mains."
    "Pas en larmes. Pas en colère."
    "Juste… absente."

    $ showP("elen", "triste", 0.50)
    elen "…"

    "Je m'attends à ce qu'elle dise quelque chose."
    "Un mot d'espoir. Une tentative maladroite de recoller les morceaux."
    "Rien."
    "Elen se tait. Et c'est peut-être ça le signe le plus inquiétant de la journée."

    hide nyra

    pause 1.5

    $ showP("elias", "neutre", 0.12)
    elias "Bon."
    elias "Quelqu'un propose quelque chose ?"
    elias "Ou on reste là à s'observer comme des plantes mortes ?"

    "Silence."

    $ showP("lysa", "blase", 0.88)
    lysa "Il n'y a rien à proposer, Elias."
    lysa "Pas ce soir."

    hide elias

    $ showP("iris", "hesitation", 0.12)
    iris "On pourrait aller… je sais pas. La salle de repos ?"
    iris "Essayer de décompresser un peu ?"

    lysa "Décompresser."
    lysa reflexion "Ouais. Bonne idée en théorie."

    hide lysa

    "Personne ne bouge."
    "L'idée reste suspendue dans la pièce comme une invitation que tout le monde décline tacitement."
    "Ce n'est pas qu'on ne veuille pas se détendre."
    "C'est qu'on n'en a plus la capacité."

    hide iris
    hide elen

    pause 1.0

    "Peu à peu, sans un mot, les gens se lèvent."
    "Pas ensemble. Pas en groupe."
    "Un par un. Chacun vers sa solitude."
    "Tomas part le premier, tête baissée."
    "Puis Nyra, qui glisse un \"bonne nuit\" qui sonne comme un verdict."
    "Kael sort sans se retourner."
    "Ryn disparaît dans le couloir sans que personne l'arrête."

    pause 0.8

    "Et moi."
    "Je reste là encore quelques secondes."
    "Seul dans la salle."
    "La lumière blafarde du Conclave tombe sur les chaises vides, les verres d'eau intacts, l'écran éteint."

    "On n'a pas tenu une journée entière."
    "Pas même une."

    jump _4_0_FIN_SOIREE

# Durée : 2m30

label _4_0_FIN_SOIREE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 1.0

    "Je marche lentement."
    "Le couloir est désert."
    "Quelques veilleuses clignotent au rythme d'un système qui n'a pas besoin de nous pour tourner."
    "Les portes sont closes. Derrière chacune, quelqu'un qui ruminent en silence, j'imagine."
    "Ou quelqu'un qui essaie de ne plus penser du tout."

    "Je passe devant la chambre de Julian."
    "La lumière filtre sous la porte."
    "Il est là."
    "Il n'a pas dormi non plus."
    "Mais je ne frappe pas."
    "Je ne saurais pas quoi lui dire."

    pause 0.8

    scene bg_chambre at adaptive_fullscreen with dissolve

    $ blink()
    "Je pousse la porte de ma chambre."
    "Elle se referme dans mon dos."
    "Clic."

    "Je ne cherche pas la lumière."
    "Je n'allume rien."
    "Je m'assieds sur le bord du lit dans le noir."
    "La veilleuse bleue dessine des ombres sur le mur."

    pause 1.2

    $ blink()
    "Je repense à tout."
    "À Elen qui pleurait ce matin pour des épices."
    "À Sael qui partait en claquant la porte."
    "À Julian enfermé dans sa chambre comme si ça pouvait tout effacer."
    "Au siège vide."
    "Aux sièges vides."

    pause 0.8

    "On n'était pas forcément d'accord."
    "On n'était pas forcément proches."
    "Mais on était là."
    "Et maintenant même ça, on est en train de le perdre."

    $ blink()
    "Je m'allonge sur le dos, les bras le long du corps."
    "Le plafond est là. Inerte. Rassurant dans sa stupidité totale."

    pause 1.0

    "Je pense à ce vote qui arrive."
    "La libre circulation."
    "Un autre bouton vert ou rouge."
    "Une autre chance de rien faire, ou une autre catastrophe à vitesse accélérée."

    "Je ne sais plus ce que je veux."
    "Je ne sais plus ce qu'on est capables de faire."
    "Ensemble."

    $ blink()
    pause 0.6

    "Il y a quelque chose d'épuisant à rester conscient de son propre échec."
    "À le voir, le nommer, et ne pas savoir par quel bout le réparer."
    "On n'a même pas su faire une soirée."
    "On n'a même pas su rester dans la même pièce."

    pause 1.0

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()
    "Mes paupières tombent."
    "Pas parce que je suis en paix."
    "Juste parce que le corps abandonne avant la tête."

    "La lumière bleue pulse doucement dans le noir."
    "Quelque part dans le couloir, une porte s'ouvre puis se referme."
    "Quelqu'un d'autre qui ne dort pas."
    "Ou quelqu'un qui fait semblant."

    $ blink()
    pause 1.5

    "On a la chance d'être là."
    "D'avoir une voix. Un vote. Une salle autour d'une table."
    "Et on a quand même réussi à tout rater."

    pause 0.8

    "Je ne sais pas si demain sera mieux."
    "Je ne suis même plus sûr d'en avoir envie."

    $ blink()
    pause 2.0

    "Le sommeil arrive."
    "Lourd. Sans rêve. Sans réponse."
    "Juste le silence et la certitude d'un gâchis que je n'arrive pas encore à mesurer."

    $ current_day = 5
    pause 1.5

    #jump patreon_ending

    call end_day("5")
    jump _5_0_REVEIL_CHAMBRE

# Durée : 2m00
# Total estimé journée 4_0 : ~13-14 minutes