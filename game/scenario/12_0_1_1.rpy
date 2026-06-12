label _12_0_1_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 3.0
    play sound sfx_creak volume 0.6

    "Je me réveille en sursaut, le cœur cognant violemment dans ma poitrine."

    "Un bruit… J’ai entendu un bruit."
    "Comme un frottement. Ou un pas. Juste à côté du lit."

    "Je reste immobile plusieurs secondes, les yeux grands ouverts dans le noir."
    "Seul le bourdonnement lointain des ventilations du Conclave me répond."

    noam faible "... Il y a quelqu’un ?"

    "Aucune réponse."

    "Je me redresse lentement, la tête lourde et la gorge sèche."

    think "Ce n’était pas un rêve… J’en suis presque sûr."

    think "Je me suis déjà réveillé en sursaut avant."
    think "Mais jamais comme ça."
    think "J'ai vraiment entendu quelque chose de bizarre."
    think "Ou quelqu'un."
    "Je tends la main vers l’interrupteur. La lumière froide de la chambre m’aveugle un instant."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "La pièce est vide."
    "La porte est fermée. Rien ne semble déplacé."

    think "Alors pourquoi j'ai l'impression qu'on m'observe encore ?"

    "Je reste immobile."
    "À écouter."
    "À attendre un second bruit."
    "Quelque chose."
    "Rien ne vient."
    "Pourtant, je ne peux pas me calmer."

    think "Je deviens parano… Il faut que j’arrête."
    think "… Mais si ce n’était pas de la parano ?"

    "Sans vraiment réfléchir, je me lève et commence à fouiller la chambre."

    $ pnc_room = "chambre_j12"
    $ pnc_flags = {}
    call screen pnc_chambre_j12()
    return

screen pnc_chambre_j12():

    modal True
    zorder 200

    add "images/background/bg_chambre.png" at cover_screen

    imagebutton:
        idle "images/background/interact/chambre/sous_lit.png"
        hover "images/background/interact/chambre/sous_lit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_12_0_1_1_sous_lit")

    imagebutton:
        idle "images/background/interact/chambre/placard.png"
        hover "images/background/interact/chambre/placard_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_12_0_1_1_placard")

    imagebutton:
        idle "images/background/interact/chambre/chaise.png"
        hover "images/background/interact/chambre/chaise_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_12_0_1_1_bureau")

    imagebutton:
        idle "images/background/interact/chambre/lit.png"
        hover "images/background/interact/chambre/lit_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("_12_0_1_1_recoucher")

# ==================== MINILABELS ====================

label _12_0_1_1_sous_lit:

    "Je m’agenouille devant le lit."
    "Mon cœur bat plus vite que nécessaire."

    think "Personne ne peut être là."

    "Je soulève lentement la couverture."
    "Pendant une seconde, je redoute réellement ce que je pourrais trouver."
    "Je passe une main dessous."
    "Puis la tête."
    "Rien."
    "Seulement de la poussière."
    "Le vide."

    think "Évidemment."

    "Je reste quand même quelques secondes à regarder."

    think "J'ai vraiment cru qu'il y aurait quelque chose."

    call screen pnc_chambre_j12()
    return

label _12_0_1_1_placard:

    "J’ouvre le placard d’un coup sec, le cœur battant."

    "Mes vêtements sont là, bien rangés."
    "Mais sur l’étagère du haut… quelque chose attire mon regard."

    "Un de mes sweats est légèrement de travers."
    "Et surtout… il y a une légère empreinte de main sur la poussière de l’étagère."
    "Je tends la main vers elle."
    "Sans la toucher."
    "Juste assez près pour comparer."

    think "... Ce n’est pas moi qui ai touché là-haut."

    "Mon ventre se noue."

    think "Non."
    think "Je ne peux pas être certain."
    think "Je me change régulièrement j'ai peut-être bougé ça accidentellement."
    think "Je ne sais même plus."

    call screen pnc_chambre_j12()
    return

label _12_0_1_1_bureau:

    "Je m’approche du bureau et regarde rapidement les affaires."

    "Tout semble à sa place… sauf mon badge."
    "Il est retourné, face cachée."

    think "Je ne me souviens pas l’avoir laissé comme ça."
    think "Ça ne veut rien dire."
    think "Un badge retourné."
    think "C'est ridicule."
    think "Alors pourquoi j'ai l'impression que quelque chose ne va pas ?"

    call screen pnc_chambre_j12()
    return

label _12_0_1_1_recoucher:

    "Je reste un moment debout au milieu de la chambre, puis je soupire."

    think "Je deviens complètement dingue…"
    think "Il faut que je dorme."

    "Je me recouche, mais le sommeil met longtemps à revenir."

    jump _12_0_1_1_CAFETERIA

# Fin du label principal
label _12_0_1_1_CAFETERIA:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Impossible de me rendormir."
    "Chaque fois que je ferme les yeux, j’entends ce bruit… ou je crois l’entendre."

    think "Il est encore tôt… à peine 6h30."
    think "Si je reste ici, je vais devenir fou."

    "Je me lève, enfile un sweat à la hâte et sors de ma chambre sans faire de bruit."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Les couloirs sont encore déserts. Parfait."

    think "Je ne veux voir personne. Pas maintenant."

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play sound sfx_door

    "La cafétéria est vide et silencieuse. Seule la lumière froide des néons automatiques est allumée."
    "Derrière le comptoir, Goumi est déjà en activité, ses bras mécaniques s’affairant avec précision."

    $ showGroup([
        ("noam", "fatigue", 0.50),
    ])

    goumi "Bonjour, Noam. Tu es bien matinal aujourd’hui."

    noam fatigue "Ouais… je n’arrivais plus à dormir."

    goumi "Je comprends. Veux-tu que je te prépare quelque chose pour te rebooster ?"

    noam "Ce que tu peux. Rien de trop lourd."

    goumi "Bien reçu. Je te propose des œufs brouillés, du pain grillé et un yaourt nature. Par contre…"

    "Le robot marque une petite pause, comme s’il consultait ses stocks."

    goumi "Je ne pourrai pas te faire de grosse portion aujourd’hui. Les réserves de nourriture sont plus faibles que prévu. Nous sommes en mode rationnement léger."

    noam hesitation "Comment ça, plus faibles que prévu ?"

    goumi "Les calculs de consommation ont été dépassés ces derniers jours."
    goumi "Pourtant nos prédictions sont souvent fiables."

    think "Évidemment…"

    noam "Je vois…"

    goumi "Je peux quand même te préparer un repas correct. Tu veux quand même les œufs ?"

    noam "Oui… vas-y."

    "Je m’assois à une table près de la fenêtre, le regard perdu dans le vide."

    think "Même la bouffe commence à manquer… Super."

    pause 1.5

    "Quelques minutes plus tard, j’entends des pas légers et rapides."


    $ showGroup([
        ("noam", "fatigue", 0.50),
        ("elen", "rire", 0.30),
    ])

    play music "music/bgm_romantic_atmosphere.mp3" fadein 2.0

    elen content "Noooam ! T’es déjà là ?! T’es un lève-tôt maintenant ?!"
    elen "Depuis quand ??"

    "Elen arrive avec son énergie habituelle, un grand sourire aux lèvres."

    think "Toujours la même."
    think "Toujours incapable de rester silencieuse plus de trente secondes."

    "Étrangement..."

    think "Ça me rassure un peu."

    noam fatigue "… Salut Elen."
    $ bc_hide()

    elen "T’as pas l’air en super forme dis donc. Encore fatigué de ton malaise de l'autre jour ?"
    elen content "En même temps c'est pas étonnant, je te vois jamais venir manger !"
    elen rire "Tu sais c'est important hein ?!"

    noam "Ouais… un peu."

    elen joie "Crois moi, la cafétéria c’est le meilleur remède ! Goumi, tu me fais la même chose que d’habitude ? Avec double portion de pain s’il te plaît !"

    goumi "Elen… je viens justement d’expliquer à Noam que les réserves sont plus basses que prévu. Je ne peux pas faire de double portion aujourd’hui."

    elen "Hein ?! Sérieux ?!"
    elen colere "Mais tu m'as déjà dit ça hier soir !"

    goumi "Et les stocks n'ont pas changé depuis... Enfin si, ils ont encore diminué."
    goumi "On ne sera pas livré avant le quatorzième jour."

    "Elle se tourne vers moi, les yeux écarquillés."

    elen decu "Oh non… C’est à cause de moi, c’est ça ?"
    
    "Elle croise mon regard vide un moment."

    elen decu "Sérieux ?! Je mange trop ?!"

    noam hesitation "…"

    elen fatigue "Je suis désoléeééé ! Je sais que je mange beaucoup trop ! Mais la nourriture c’est vraiment mon péché mignon ici !"
    elen taquin "Avec tout ce stress, j’ai besoin de réconfort, tu comprends ?!"

    noam "Ouais… je comprends."

    elen determine "Goumi, tu peux me faire une portion normale alors ? Je vais me retenir, promis ! Croix de bois, croix de fer !"

    goumi "Bien reçu. Une portion normale pour Elen."

    "Elen s’assoit en face de moi sans me demander mon avis, toujours avec son sourire éclatant."

    elen surpris "Du coup, t’as pas réussi à te rendormir ? T’as fait un cauchemar ou quoi ?"

    think "Si seulement c’était juste un cauchemar…"
    think "Un cauchemar s'arrête quand on ouvre les yeux."
    think "Là j'ai l'impression que c'est pire quand je suis réveillé."

    noam triste "Quelque chose comme ça."

    elen reflexion "Raconte ! Je suis super bonne pour écouter les cauchemars ! Une fois j’ai rêvé que Kami nous transformait tous en cupcakes et qu’elle nous mangeait un par un. C'était horrible !"
    elen rire "Je me suis réveillée avec une de ces faim, tu n'imagines même pas !"

    noam surpris "Hein ?! Me dis pas que tu voulais nous bouffer ?!"
    noam taquin "… Si seulement j'avais fais un rêve comme ça."

    elen rire "Tu m'étonnes ! Et ouais, on avait tous l'air trop trop bons !"
    elen taquin "Allez, dis-moi ! T’as rêvé de quoi ? Du vote d’aujourd’hui ? D’un truc bizarre ?"

    noam colere "Elen."

    elen reflexion "Quoi ?"

    noam colere "Je n’ai pas trop envie de parler ce matin."

    elen triste "Oh… d’accord."

    "Elle reste silencieuse deux secondes… avant de repartir de plus belle."

    elen determine "Mais tu sais, si tu changes d’avis, je suis là hein ! Je peux même te raconter mes blagues nulles pour te changer les idées !"

    think "Elle ne s’arrête donc jamais…"

    noam "Elen… s’il te plaît."

    elen "Okay okay, je me tais !"

    "Je termine de manger en silence. L'heure tourne doucement."

    think "Qu'est ce que c'était que ce bruit ?"
    think "Le fruit de mon imagination ...?"

    jump _12_0_1_1_SUITE_CAFETERIA


label _12_0_1_1_SUITE_CAFETERIA:

    "Je termine mon assiette en silence. Elen finit par comprendre que je ne suis pas d’humeur et part rejoindre d’autres personnes après m’avoir fait un petit signe de la main."

    hide elen with dissolve
    hide noam with dissolve

    think "Enfin seul."

    "Je reste encore quelques minutes à fixer mon plateau vide, puis je me lève."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "À peine sorti de la cafétéria, la voix de Kami résonne soudain dans tout le Conclave."

    play music "music/bgm_system_override.mp3" fadein 2.0

    play sound sfx_announce
    show screen kami_broadcast_ui

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Bonjour à tous mes petits disciples chéris~"
    kami "J’espère que vous avez bien dormi… ou du moins, que certains d’entre vous ont essayé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Petite annonce du jour : le vote sur l’autorisation ou l’interdiction des dispositifs de brouillage aura lieu aujourd’hui à 14h précises."
    kami "Je vous conseille vivement d’être présents et en pleine possession de vos moyens."
    kami "Après tout… ce vote est assez important, n’est-ce pas ?"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "N’oubliez pas : vos choix auront des conséquences. Comme toujours."
    kami "Je compte sur vous pour être raisonnables… ou du moins, divertissants."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Sur ce, je vous laisse. Profitez bien de votre matinée."

    hide screen kami_broadcast_ui

    scene bg_couloir at adaptive_fullscreen with dissolve
    "Le silence retombe dans les couloirs."

    play music "music/bgm_careful_wanting.mp3" fadein 2.0

    think "14h…"
    think "Il ne reste plus que quelques heures avant de décider si on veut vivre sous surveillance permanente ou risquer le chaos."

    "Je serre les poings dans les poches de mon sweat."

    think "Je n’ai envie de parler à personne."
    think "Ni de répondre à des questions, ni de voir leurs regards inquiets, ni d’entendre Elen essayer de me dérider."

    "Au lieu de prendre le chemin direct, je décide de faire le grand tour par les couloirs extérieurs, ceux qui longent les zones techniques."

    "C’est plus long. Plus vide. Exactement ce qu’il me faut."

    "Alors que je passe devant l'infirmerie, je décide de m'y arrêter une minute."

    scene bg_infirmerie at adaptive_fullscreen with dissolve

    think "Mon mal de tête n’est toujours pas parti… Il empire même."
    think "Sans doute à cause de mon manque de sommeil..."

    "Je m’approche de la petite pharmacie et regarde ce qu'il y a de disponibles."
    "Après quelques secondes, je prends quelques comprimés de paracétamol et je les emporte avec moi."
    "Je prends deux comprimés directement dans ma main et les avale à sec."

    noam faible "..."
    noam "C'est pas facile à avaler cette merde !"

    think "Ça ne soignera pas ce qui ne va vraiment pas… mais au moins, ma tête arrêtera peut-être de pulser."

    "Je reste un moment devant l'armoire à pharmacie, les yeux dans le vide."

    think "Tout le monde va vouloir discuter du vote."
    think "Et moi je vais devoir faire semblant d’être normal."
    think "Faire semblant de ne pas me demander si l’un d’entre eux est celui qui m’a regardé dans les yeux hier soir… avant d’effacer les preuves."

    "Je secoue la tête et reprends ma route, le pas lourd."

    scene bg_chambre at adaptive_fullscreen with fade

    "Je referme la porte de ma chambre derrière moi et m’adosse contre elle un long moment."

    think "Je vais juste attendre ici jusqu’à 14h."
    think "Loin de tout le monde."

    "Je m’allonge sur le lit sans enlever mes chaussures, les yeux rivés au plafond."

    think "Plus que quelques heures avant le vote."
    think "Et je ne sais même plus ce que je dois choisir…"
    think "Ni en qui je peux avoir confiance."

    pause 2.0

    jump _12_0_1_1_ATTENTE_VOTE 

label _12_0_1_1_ATTENTE_VOTE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_low_tension.mp3" fadein 3.0

    "Les heures sont passées lentement. Trop lentement."
    "J’ai tourné en rond dans ma chambre, alternant entre tentatives de sommeil et crises de réflexion."

    think "14h… Le moment est venu."

    "Je me lève, le corps lourd, et sors de ma chambre sans grand enthousiasme."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "Les haut-parleurs crachent soudain la voix de Kami."

    play sound sfx_announce
    show screen kami_broadcast_ui

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mes chers représentants, votre attention s’il vous plaît."
    kami "Le débat sur l’autorisation ou l’interdiction des dispositifs de brouillage va débuter dans quelques minutes."
    kami "Je vous attends tous dans la Salle du Conclave. Ne tardez pas~"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et essayez de ne pas vous entretuer avant le vote, ce serait dommage."

    hide screen kami_broadcast_ui

    "Je soupire et prends la direction de la salle."

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Presque tout le monde est déjà là. L’ambiance est lourde, électrique."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "triste", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    "Je m’installe discrètement à ma place habituelle."

    tomas "Bon… on y est."
    tomas "Je pense qu’on est tous d’accord pour dire que ce vote est crucial."

    mara "Évidemment qu’on autorise les brouilleurs !"
    mara stress "J’en peux plus de savoir que Kami peut nous mater 24h/24 !"

    elen "Moi aussi ! J’ai envie de pouvoir danser dans ma chambre sans me sentir jugée !"

    julian taquin "Et moi j’ai envie de pouvoir dire des conneries sans que Kami les enregistre pour plus tard."

    iris "C’est clair… La vie privée, c’est important."

    "Je les écoute en silence, les bras croisés."

    think "Tout le monde est pour."
    think "Même ceux qui étaient hésitants hier semblent avoir basculé."

    sael "Techniquement, tant qu’on respecte les Commandements, on devrait pouvoir avoir notre intimité."

    kael calme "… Tant qu’on respecte les Commandements, oui."

    "Je serre les mâchoires."

    think "Et si on n’avait pas de brouilleurs…"
    think "Est-ce qu’on aurait pu savoir qui m’a volé mes affaires ?"
    think "Est-ce qu’on aurait pu savoir qui a volé la photo de la sœur de Kael ?"

    think "Les brouilleurs… ils protègent peut-être notre intimité…"
    think "… mais ils protègent surtout ceux qui veulent agir dans l’ombre."

    "Cette pensée me reste en travers de la gorge."

    ryn colere "Moi je dis qu’on autorise tout ça. Point final."
    ryn "J’en ai marre de vivre dans un putain de reality show."

    nyra raison "Il faut juste faire attention aux conséquences. Si tout le monde a des brouilleurs, on ne pourra plus rien prouver."

    "Je reste muet."

    think "Exactement."
    think "Les brouilleurs permettent l’insécurité."
    think "Ils permettent à quelqu’un de se faire passer pour moi, d’effacer des preuves, de voler… sans qu’on puisse jamais rien prouver."

    "Iris me jette un regard en coin."

    iris inquiet "Noam… tu dis rien ?"

    $ bc_show("noam", "fatigue", px=-70, py=-50, pz=0.85)
    noam fatigue "… Je réfléchis."
    $ bc_hide()

    julian taquin "Allez, Noam ! T’es pas d’accord pour qu’on ait enfin un peu d’intimité ?"

    "Je hausse légèrement les épaules."

    noam "Si… bien sûr."

    think "Mais à quel prix ?"

    "La discussion continue autour de moi, animée, presque enthousiaste."
    "Moi, je reste en retrait, perdu dans mes pensées."

    think "Si on vote pour les brouilleurs… on donne encore plus de pouvoir à celui qui se cache parmi nous."
    think "Et je suis le seul à m’en rendre compte ?"

    pause 1.5

    jump _12_0_1_1_DEBAT_VOTE

label _12_0_1_1_DEBAT_VOTE:

    scene bg_conclave at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0

    think "Tout le monde parle."
    think "Moi, je n'arrive plus a suivre les phrases."

    call j12011_play_wire_debate from _call_j12011_play_wire_debate
    $ j12011_vote_data = _return

    scene bg_conclave at adaptive_fullscreen with fade

    if j12011_wire_result == "security":
        jump _12_0_1_1_DEBAT_SECURITE

    jump _12_0_1_1_DEBAT_LIBERTE

label _12_0_1_1_DEBAT_SECURITE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 2.5

    "La Salle du Conclave est pleine. Tout le monde est présent. L’air est lourd, chargé d’électricité."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "fatigue", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas "Bon… on ne va pas tourner autour du pot pendant trois heures."
    tomas "Le vote est clair : est-ce qu’on autorise les dispositifs de brouillage, oui ou non ?"

    mara stress "Pour moi c’est évident ! On autorise !"
    mara "J’en peux plus de vivre comme dans une télé-réalité où Kami nous mate 24h sur 24 !"
    mara "Je veux pouvoir me changer, parler librement, ou même pleurer sans que quelqu’un, ou quelque chose, analyse mes larmes !"

    elen "Moi aussi ! J’ai envie de danser comme une folle dans ma chambre sans me demander si elle est en train de me noter sur 10 !"

    julian taquin "Et moi j’ai envie de pouvoir dire que Kami est une grosse sadique sans qu’elle me le rappelle gentiment le lendemain."

    "Quelques rires nerveux parcourent la salle."

    elias fatigue "Je comprends l’idée, mais le sujet est quand même important."
    elias fatigue "Sans ça, Kami pourra plus ni nous surveiller, ni nous protéger..."

    lysa inquiet "Alors pas vraiment."
    lysa inquiet "Même avec les brouilleurs, Kami peut avoir accès aux vidéos, mais après une semaine de délai."

    nyra raison "Je peux comprendre l’envie d’intimité… mais il ne faut pas oublier les risques."
    nyra "Si tout le monde a des brouilleurs, comment on prouve quoi que ce soit ?"
    nyra "Le vol chez Kael, par exemple… on ne saura jamais qui c’était."

    kael "… Exactement."

    "Kael parle d’une voix basse, mais tout le monde se tait un instant."

    kael "Si on autorise les brouilleurs, peut-être que je ne saurai jamais qui m'a volé la photo de ma soeur."
    kael "Je veux savoir qui c'est."

    ryn colere "Et alors ? Tu préfères vivre en prison dorée juste pour avoir une chance de choper un voleur ?"
    ryn "Moi je dis : l'important c'est d'être libre. On n’est pas des animaux de foire."

    sael mefiant "C’est facile à dire tant que ce n’est pas toi qui t’es fait voler un truc précieux."

    "La discussion s’enflamme petit à petit. Je reste silencieux, les bras croisés, à écouter."

    think "Tout le monde penche pour l’autorisation…"
    think "Même ceux qui étaient hésitants hier ont l'air plus convaincu."

    iris "Noam ? Tu dis rien ?"

    "Tous les regards se tournent vers moi."

    noam fatigue "… Je réfléchis."

    julian taquin "Allez mec, t’es plutôt team liberté ou team Big Sister Kami ?"

    think "Si on vote pour les brouilleurs…"
    think "Tout le monde pourra vivre l'esprit plus serein..."
    think "Il faudra plusieurs jours à Kami pour savoir ce qui se passe sous les brouilleurs..."

    think "Mais si on vote contre…"
    think "On reste sous la surveillance totale de Kami."
    think "Elle saura tout. Absolument tout. Tout le temps."

    "Je serre les dents."

    noam raison "… La sécurité."

    "Le mot sort plus sèchement que prévu."

    noam "Je ne dis pas que ça me plaît."
    noam fatigue "Je ne dis pas que vivre sous caméra, c’est normal."
    noam determine "Mais les brouilleurs ne protègent pas seulement notre intimité. Ils protègent aussi de ceux qui veulent profiter de cette intimité."

    elen "Noam…"

    noam "S’il n’y avait pas eu ces zones mortes, ces coupures, ces moyens de disparaître…"
    noam colere "On saurait déjà qui a volé les affaires de Kael."
    noam colere "Et on saurait aussi qui a touché aux miennes."

    "Kael relève lentement les yeux vers moi."

    kael reflechit "…"

    noam fatigue "On peut appeler ça liberté si vous voulez."
    noam "Je ne suis au final pas sûr que ce soit l'idéal."

    mara stress "Donc ta solution, c’est de laisser Kami nous regarder jusque dans nos chambres ?"

    noam desaccord "il n'y a pas de solution parfaite."

    "Je sens tous les regards peser sur moi."

    "La discussion reprend de plus belle autour de moi, mais je n’écoute plus vraiment."

    pause 1.5

    jump _12_0_1_1_DEBAT_TRAITRE

label _12_0_1_1_DEBAT_LIBERTE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 2.5

    "La Salle du Conclave est pleine à craquer. L’atmosphère est électrique, presque fiévreuse."

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    tomas "Très bien… Il faut qu'arrête de tourner autour du pot."
    tomas "Le vote d’aujourd’hui est clair : est-ce qu’on autorise les dispositifs de brouillage, oui ou non ?"

    mara stress "Autoriser ! Évidemment qu’on autorise !"
    mara "Je refuse de continuer à vivre comme une souris de laboratoire !"
    mara "Je veux pouvoir fermer ma porte, parler librement, pleurer, crier, ou même me disputer sans que Kami analyse tout ce que je fais !"

    elen "Exactement ! J’en ai marre de me sentir observée même quand je danse seule dans ma chambre !"

    julian taquin "Moi je veux pouvoir insulter Kami tranquillement sans qu’elle me le ressorte six mois plus tard avec un petit smiley sadique."

    elias fatigue "Je ne vais pas mentir… moi aussi, l’idée de pouvoir respirer deux minutes sans caméra me tente."
    elias reflechit "Même si je comprends aussi l'intéret des caméras."

    lysa inquiet "Ça ne règle pas tout. Mais continuer comme ça, avec Kami partout, tout le temps… C'est quand même particulier..."

    ryn colere "Liberté ! Point final !"
    ryn "On n’est pas des putains de prisonniers ! On mérite de pouvoir avoir un minimum d’intimité dans cet enfer !"

    "Plusieurs voix s’élèvent en soutien. L’énergie est clairement du côté de la liberté."

    nyra raison "Je comprends l’envie… vraiment."
    nyra "Mais on ne peut pas ignorer les risques. Si tout le monde porte un brouilleur, comment on prouve quoi que ce soit ?"

    kael "… Comme ce qui m’est arrivé."

    "Le silence retombe un instant."

    kael calme "Kami m'a dit que si on interdit les brouilleurs, je n’aurai probablement jamais accès aux images de ma chambre."
    kael triste "Les brouilleurs seront désinstallés dans toutes les chambres, les images capturées avec..."
    kael "Le voleur restera invisible. Pour toujours."

    sael mefiant "Et si on les interdit ? On reste sous la surveillance totale de Kami. C’est encore moins la solution."

    mara "Exactement ! On échange une prison contre une autre !"
    mara "Moi je préfère risquer l’insécurité plutôt que de vivre dans une cage dorée."
    mara "Qu'est ce que je risque hein ?! A part qu'un bel homme ait envie de se glisser dans ma chambre ?"

    "La discussion devient de plus en plus animée. Je reste silencieux, les bras croisés, à écouter."

    iris "Noam ? Tu n’as toujours rien dit ?"

    "Les regards convergent vers moi."

    noam fatigue "… Je réfléchis encore."

    julian taquin "Allez, Noam ! T’es team liberté hein ?! Me dis pas que tu veux continuer à ce qu'on se fasse espionner ?!"

    "Je sens ma mâchoire se crisper."

    noam fatigue "… Ouais."

    "Le mot me laisse un goût amer dans la bouche."

    noam "Je ne dis pas que c’est sans risque."
    noam hesitation "Je ne dis pas que Kael a tort. Ni Nyra. Ni Tomas."
    noam "Mais si on accepte que Kami voie tout, tout le temps, alors on ne vote plus pour notre sécurité."
    noam desaccord "On vote pour notre obéissance totale a ses règles, même quand elles sont absurdes."

    elen "Donc tu es avec nous ?"

    noam fatigue "Je suis avec personne."
    noam "Je veux juste qu’on garde un endroit où on peut juste être soi même."

    mara stress "Voilà. C’est exactement ça."

    kael calme "Et si quelqu’un utilise cet endroit pour voler encore ?"

    noam "Alors il faudra le coincer autrement."
    noam "..."

    "Je baisse légèrement les yeux."

    think "Je ne crois même pas totalement à ce que je viens de dire."
    think "Pas comme eux."
    think "Pas tant que je ne sais pas qui, parmi eux, est responsable de tout ça."

    "La discussion reprend de plus belle, passionnée et bruyante."
    "Moi, je reste en retrait, le cœur lourd et l’esprit tourmenté."

    pause 1.5

    jump _12_0_1_1_DEBAT_TRAITRE

label _12_0_1_1_DEBAT_TRAITRE:

    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    $ showGroup([
        ("elias", "fatigue", -0.11),
        ("mara", "stress", 0.01),
        ("noam", "neutre", 0.13),
        ("lysa", "inquiet", 0.25),
        ("julian", "hesitation", 0.37),
        ("iris", "inquiet", 0.49),
        ("tomas", "raison", 0.60),
        ("elen", "inquiet", 0.72),
        ("kael", "calme", 0.84),
        ("nyra", "raison", 0.96),
        ("ryn", "colere", 1.08),
        ("sael", "mefiant", 1.20),
    ])

    "Le débat fait rage depuis plusieurs minutes. Les voix se chevauchent, les arguments fusent."

    mara stress "Bon, on passe au vote et on autorise les brouilleurs, point final ! J’en peux plus de cette surveillance constante !"

    ryn colere "Ouais ! On n’est pas des putains de cobayes !"

    tomas "O-Ouais... C'est peut-être pour le mieux..."

    "Je sens quelque chose craquer en moi."
    "Toutes ces discussions… ces belles paroles… alors que quelqu’un, ici, a effacé les images des caméras."

    noam colere "FERMEZ-LA !"
    with vpunch

    "Le silence tombe d’un coup sur la salle. Tout le monde se tourne vers moi, stupéfait."

    iris inquiet "Noam… ?"

    noam colere "Vous êtes tous là à débattre comme si tout était normal !"
    noam colere "Comme si on était une grande famille heureuse qui doit juste choisir entre avoir un peu d'intimité et vivre en sécurité !"
    noam desespoir "Mais vous êtes aveugles ou quoi ?!"

    julian hesitation "Noam, calme-toi mec…"

    noam colere "Me calmer ?!"
    noam desespoir "Quelqu’un a supprimé les enregistrements des caméras hier soir !"
    noam colere "Dans le couloir près de la salle de stockage ! Juste avant l’annonce !"
    noam peur "Et ce quelqu’un est ici ! Parmi nous !"

    "Un silence de plomb s’abat sur la salle."

    sael mefiant "… Quoi ? De quoi tu parles ?!"

    noam colere "J’ai demandé à Kami de me montrer les images. Elles ont été effacées !"
    noam colere "Nettoyées. Comme si elles n’avaient jamais existé !"
    noam panne "Et ce n’est pas Kami qui l’a fait ! Elle me l’a dit elle-même !"

    mara stress "Attends… tu es en train de nous dire que quelqu’un aurait supprimé les images des caméras ?"
    mara colere "Mais pourquoi quelqu'un irait faire ça ?!"

    noam colere "Oui !"
    noam panne "Quelqu’un qui était là hier soir. Quelqu’un qui savait exactement ce qu’il faisait !"

    elen inquiet "Noam… tu es sûr de ce que tu dis ? Tu étais encore malade hier, peut-être que…"

    noam colere "Ne me parle pas comme si j’étais fou, Elen !"
    noam peur "Il s'est passé quelque chose de bizarre dans ce couloir !"
    noam colere "Et tout a été effacé !"

    ryn colere "Et tu nous accuses nous ?! T’es sérieux là ?!"

    noam colere "Oui ! Parce que c’est forcément l’un d’entre vous !"
    noam triste "Qui d’autre aurait pu le faire ?!"

    kael calme "... Noam. Respire."

    noam colere "Non ! Je ne respire plus !"
    noam fatigue "Quelqu’un ici joue un double jeu !"
    noam colere "Quelqu’un qui sourit, qui vote avec nous, qui fait semblant de s’inquiéter pour moi… et qui efface des preuves dans mon dos !"

    iris inquiet "Noam, arrête… Tu es épuisé, tu as fait un malaise hier, tu—"

    noam colere "Ne me dis pas que je suis épuisé, Iris !"
    noam colere "Je sais ce que j’ai vu !"
    noam peur "Et je sais qu’un de vous ment !"

    sael mefiant "Et tu accuses qui exactement ? Balance un nom si tu es si sûr de toi !"

    noam triste "Je ne sais pas encore qui !"
    noam colere "Mais je sais que c’est l’un d’entre vous !"
    noam fatigue "Je ne sais pas ! Mais quelqu’un ici est un traître !"

    julian hesitation "Woah woah… Noam, tu dérapes là…"
    julian "Un traître ? Carrément ?!"

    elen inquiet "Noam… on est tous avec toi. On s’est inquiétés pour toi hier…"

    lysa inquiet "Personne ne gagne quoi que ce soit à te voir t’effondrer devant nous."

    elias fatigue "Et personne ne devrait voter pendant que tout le monde se jauge comme ça."

    noam fatigue "Arrêtez avec ça !"
    noam inquiet "Je ne veux plus entendre que vous vous inquiétez pour moi !"
    noam colere "L’un de vous a supprimé ces images ! L’un de vous cache quelque chose !"
    noam culpabilite "Et vous êtes tous là à débattre tranquillement sur les brouilleurs comme si rien ne s’était passé !"

    "Ma voix se brise légèrement sur la fin. Je suis essoufflé, tremblant de rage et de fatigue."

    nyra raison "Noam… si ce que tu dis est vrai, on doit en parler calmement. Accuser tout le monde ne nous aidera pas."

    noam colere "Calmement ?!"
    noam desaccord "Comment tu veux que je sois calme ?!"

    "Le silence qui suit est assourdissant."

    iris inquiet "Noam… regarde-moi."
    iris "On est tous fatigués. On est tous sur les nerfs. Mais on est une équipe."

    noam panne "... Une équipe ?"
    noam peur "Une équipe où quelqu’un poignarde les autres dans le dos."

    "Je reste debout, les mains tremblantes."

    "Tout le monde me regarde maintenant avec un mélange de peur, de pitié et de suspicion."

    jump _12_0_1_1_APRES_EXPLOSION

label _12_0_1_1_APRES_EXPLOSION:

    noam fatigue "J’en ai marre."

    iris inquiet "Noam…"

    noam colere "Non."
    noam fatigue "Ce débat ne mène nulle part."

    tomas inquiet "On n’a pas fini le vote."

    noam desaccord "Alors finissez-le sans moi."

    "Personne ne répond."

    "Je tourne les talons avant que quelqu’un trouve une nouvelle phrase pour me retenir."

    play sound sfx_door
    scene bg_couloir at adaptive_fullscreen with dissolve

    "Le couloir me paraît trop long."
    "Trop blanc."
    "Trop silencieux après tout ce bruit."

    think "Je suis allé trop loin."
    think "Ou pas assez."
    think "Je ne sais plus."

    scene bg_chambre at adaptive_fullscreen with dissolve
    play sound sfx_creak volume 0.6

    "Je referme la porte de ma chambre derrière moi."
    "Le déclic de la serrure me fait presque sursauter."

    noam fatigue "Putain…"

    "Je ne prends même pas le temps d’enlever correctement mes vêtements."
    "Je m’allonge sur le lit, encore tendu, encore furieux, encore honteux."

    think "Je ne veux plus penser."
    think "Pas au vote."
    think "Pas à Kael."
    think "Pas aux brouilleurs."
    think "Pas à celui qui ment."

    pause 1.5

    "Le sommeil finit par me tomber dessus d’un coup, lourd et sale, comme une coupure de courant."

    scene black with fade
    stop music fadeout 3.0

    call end_day("13") from _call_end_day_12_0_1_1

    if j12011_wire_result == "security":
        jump _13_0_1_1_0_REVEIL_CHAMBRE

    jump _13_0_1_1_1_REVEIL_CHAMBRE

label _13_0_1_1_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Je me réveille avec la gorge sèche et la tête lourde."
    "Pendant quelques secondes, je ne sais plus si le débat a vraiment eu lieu ou si je l’ai seulement rêvé."

    think "Non."
    think "J’ai vraiment crié."

    "Mon téléphone vibre sur le bureau."
    "Un message de Kami s’affiche sans que je le touche."

    kami "Résultat du vote : proposition acceptée."
    kami "Les dispositifs de brouillage sont désormais autorisés sous conditions dans les zones privées du Conclave."

    "Je fixe l’écran sans bouger."

    think "Autorisés."
    think "On vient d’offrir des angles morts à tout le monde."
    think "Même à celui qui ment."

    noam fatigue "Super…"

    "Je ne sais pas si je dois me sentir coupable."
    "Je sais seulement que la journée commence déjà avec un poids sur la poitrine."

    return
