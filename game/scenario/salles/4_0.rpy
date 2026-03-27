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

    $ showP("lysa", "blase", 0.30)
    lysa "Alors Noam ?"
    lysa "Tu regrettes qu’on n’ait pas osé ? Ou tu es soulagé qu’on ait préféré rester dans nos petites chaînes bien confortables ?"

    noam "Je… je ne sais plus."
    noam "Hier on a choisi de ne rien risquer… et aujourd’hui on paie le prix du confort."

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
    play music "music/bgm_tension_phase3.mp3" fadein 1.8

    pause 1.3

    "L’après-midi touche déjà à sa fin quand un signal strident résonne soudain dans tous les couloirs du Conclave."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Mes chers représentants… un peu de concentration s’il vous plaît."
    kami "Rassemblement immédiat dans la salle principale. Et cette fois, essayez de venir tous."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On a un nouveau vote à préparer. Alors bougez-vous. Les caméras n’attendent pas que vous ayez fini de ruminer votre défaite d’hier."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L’écran s’éteint. Un silence pesant s’abat sur les couloirs."
    "Je pousse un long soupir et prends la direction de la salle. Les pas des autres résonnent derrière moi, lourds et traînants."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.6

    "Quand j’arrive, la plupart sont déjà là. Ryn est adossé au mur, les bras croisés et la mâchoire serrée. Kael et Nyra sont assis en silence. Tomas tripote nerveusement ses doigts."
    "Julian brille par son absence. Il s’est enfermé dans sa chambre depuis ce matin et refuse d’en sortir."
    "Elen arrive en dernier. Elle s’assoit sans un mot, le regard perdu dans le vide. Toute sa lumière habituelle a disparu."

    $ showP("ryn", "colere", 0.50)
    ryn "Donc on est là… encore une fois."
    ryn "Pour un autre vote qui ne servira probablement à rien."

    $ showP("kael", "triste", 0.88)
    kael "Julian n’est toujours pas venu. Il a dit qu’il en avait assez pour aujourd’hui."

    $ showP("elen", "triste", 0.12)
    elen "..."
    "Elen ne réagit même pas. Elle fixe simplement la table, les épaules affaissées."

    $ showP("mara", "agace", 0.50)
    mara "Évidemment. On perd déjà notre plus grand optimiste. C’est parfait."

    $ showP("tomas", "hesitation", 0.88)
    tomas "On… on commence sans lui alors ?"

    $ showP("nyra", "raison", 0.12)
    nyra "On n’a pas vraiment le choix."

    "Le silence qui suit est lourd. Personne n’ose commenter l’absence de Julian ni l’état d’Elen."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bien. Maintenant que les volontaires sont réunis…"
    kami "Passons aux choses sérieuses."
    kami "Prochain vote :"

    play sound sfx_tambour
    pause 2.0

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser ou non les déplacements entre les districts ?"
    kami "Oui : les gens pourront voyager librement d’un district à l’autre."
    kami "Non : les frontières restent fermées comme aujourd’hui."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Cette fois, l’énoncé est limpide. Pas d’excuse."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    "Deux énormes boutons lumineux apparaissent sur l’écran, froids et menaçants."

    $ showP("ryn", "colere", 0.50)
    ryn "On doit voter oui. Il n’y a pas d’autre option."
    ryn "J’ai vu ce que ces frontières font aux gens de Limen. Je refuse qu’on continue comme ça."

    $ showP("sael", "mefiant", 0.88)
    sael "Les Gardiens sont morts pour créer ces frontières. Ils ont sacrifié leur vie pour protéger les nôtres."
    sael "Si quelqu’un les franchit, il est abattu sur-le-champ. C’est la règle."
    sael colere "Et après le vote d’hier, vous voulez encore tout ouvrir ?!"
    sael "C’est hors de question. Je voterai contre. Et cette fois, rien ne me fera changer d’avis."

    "Sa voix est calme, mais tranchante comme une lame. Elle ne laisse aucune place à la négociation."

    $ showP("lysa", "blase", 0.12)
    lysa "Après ce qui s’est passé hier… tu veux vraiment mélanger tout le monde ?"
    lysa "On n’arrive même pas à se mettre d’accord sur des rations, et vous parlez d’ouvrir les frontières ?"

    $ showP("ryn", "colere", 0.50)
    ryn "On ne peut pas rester bloqués éternellement !"

    hide sael
    $ showP("elias", "determine", 0.88)
    elias "Je suis pour. On ne peut plus vivre enfermés comme des prisonniers."

    $ showP("iris", "desaccord", 0.12)
    iris "Et bien sûr, ce sont encore les plus pauvres qui vont trinquer."

    "Sael reste silencieuse un moment, puis secoue lentement la tête."

    $ showP("sael", "colere", 0.50)
    sael "Vous n’avez toujours rien compris."
    sael "Hier vous avez eu peur de changer la moindre chose. Aujourd’hui vous voulez tout ouvrir d’un coup ?"
    sael "C’est de la folie. Je ne voterai jamais pour ça."

    hide sael
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Sael se lève brusquement et quitte la salle sans ajouter un mot, claquant la porte avec violence."
    with hpunch
    with vpunch

    pause 0.6

    $ showP("mara", "agace", 0.50)
    mara "Et merde… pas encore !"
    mara "Vous êtes vraiment obligés de tout foutre en l’air à chaque fois ?!"

    hide mara
    with moveoutright

    play sound "sound/sfx_door.ogg"
    "Mara se lève à son tour et sort en courant pour la rattraper."

    "Le silence qui s’installe ensuite est encore plus oppressant."

    $ showP("ryn", "colere", 0.50)
    ryn "Elle va tout bloquer… comme hier."

    $ showP("kael", "inquiet", 0.88)
    kael "Elle est terrifiée. On l’est tous un peu."

    $ showP("nyra", "raison", 0.12)
    nyra "Dans l’état actuel du groupe… est-ce qu’on est vraiment capables de prendre une décision sensée ?"

    "Elen n’a toujours pas prononcé un seul mot. Elle reste prostrée, absente."

    "Je regarde les sièges vides de Julian, Sael et Mara."
    "Le groupe se désagrège lentement, et on n’a même pas encore voté."

    "Un silence lourd, presque suffocant, retombe sur la salle."

    jump _4_0_APRES_CLASH_PRE_FETE