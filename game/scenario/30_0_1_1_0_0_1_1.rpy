# JOUR 30 — ROUTE SECRÈTE : JULIAN NON SAUVÉ
# Lancement après le J29. Départ de la navette à 10 h.
# Si Julian a survécu, il faudra écrire sa propre variante de J30.
default j30_secret_zero_choice = None
default j30_secret_ending = None

label _30_0_1_1_0_0_1_1_REVEIL:
    $ current_day = 30
    $ day_id = 30
    $ current_period = "Matin"
    $ j30_secret_zero_choice = None
    $ j30_secret_ending = None
    if j29_julian_syringe_swapped:
        jump _30_0_1_1_0_0_1_1_JULIAN_VIVANT_PLACEHOLDER
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.6
    "Je regarde l'heure sur ma tablette. 7 h 02. Je suis réveillé depuis un moment, mais j'ai pas réussi à sortir de mon lit."
    "La conversation avec Juliette est encore ouverte. Je relis son dernier message une fois de plus, puis j'éteins l'écran."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Bonjour, mes chers passagers ! Aujourd'hui, on rentre à la maison ! Enfin... certains d'entre vous. À 9 h, embarquement, et à 10 h, décollage !"
    kami "Merci de ne pas oublier vos affaires, vos petits secrets et vos merveilleux souvenirs du Conclave. Les retards ne seront pas acceptés, même avec une très bonne excuse !"
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Dix heures. Dans moins de trois heures, la navette sera partie."
    think "Il faut que je parle à mon double. Maintenant."
    # Durée : 1m

label _30_0_1_1_0_0_1_1_DOUBLE:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ flashlight_on(0)
    "Je le retrouve près de l'accès aux dortoirs. Il est déjà habillé pour partir, un sac sur l'épaule."
    $ flashlight_off()
    $ showGroup([("noam", "inquiet", 0.25), ("dg_noam", "neutre", 0.75)])
    dg_noam neutre "Ah, t'es là. Je commençais à me demander si tu t'étais pas rendormi."
    noam colere "Tu vas vraiment monter dans la navette comme ça ?"
    dg_noam surpris "Hein ? Bah... ouais. C'est ce qu'on avait prévu, non ?"
    noam agace "On avait prévu que je prenne ta place pour voir les autres. Deux jours. Pas que tu récupères ma vie entière."
    dg_noam inquiet "Je sais. Mais c'est plus compliqué maintenant, Noam. Avec Iris, on a parlé hier soir, et..."
    noam colere "Ouais, Iris ! J'ai vu ses messages ! Elle croit que c'est à moi qu'elle parle !"
    dg_noam raison "Elle parle à moi. Enfin... elle sait pas que je suis pas toi, d'accord, mais tout ce que je lui ai dit, je le pensais."
    noam colere "Tu peux pas faire comme si ça changeait rien !"
    dg_noam inquiet "Je fais pas comme si ça changeait rien ! Tu crois que ça me fait plaisir de savoir qu'elle va me regarder comme un monstre si je lui raconte ?"
    noam raison "Alors raconte-lui."
    dg_noam agace "Tu sais très bien que je peux pas. Il est sept heures, la navette part à dix heures, et si quelqu'un apprend qu'on existe, c'est fini."
    noam inquiet "Tu vas aussi aller voir Juliette ?"
    dg_noam surpris "Ta sœur ? Bah... je suis censé être toi, donc oui."
    noam colere "Tu la connais même pas."
    dg_noam raison "Si. Je me souviens d'elle. Je me souviens de ses anniversaires, de quand elle était petite... C'est pas des histoires qu'on m'a racontées, je les ai dans la tête."
    noam fatigue "Mais c'est pas à toi qu'elle a demandé de rentrer."
    dg_noam inquiet "Ouais. Je sais."
    noam colere "Non, je crois pas que tu saches. Quand elle va me prendre dans ses bras, ça sera toi. Et elle le saura jamais."
    dg_noam fatigue "..."
    dg_noam raison "Écoute, je sais pas quoi te dire. J'avais pas prévu de tomber amoureux d'Iris, si c'est ce que tu veux entendre. Ça m'est arrivé, c'est tout."
    noam reflexion "Si je décide de rentrer ?"
    dg_noam inquiet "Tu comptes rentrer ?"
    noam raison "Je t'ai posé une question."
    dg_noam agace "Alors on devra en discuter. Je vais pas prétendre que ça me dérange pas, parce que si, ça me dérange."
    noam colere "Me rendre ma place, c'est pas une faveur !"
    dg_noam colere "Je t'ai pas dit que c'en était une ! Arrête de me parler comme si j'étais venu te voler ton sac !"
    "On se regarde. Il est autant en colère que moi. Et c'est ça qui me fout encore plus mal à l'aise."
    dg_noam fatigue "Je vais pas me battre contre toi. Mais décide-toi vite, parce qu'à neuf heures, je rejoins les autres."
    noam inquiet "T'es au courant pour Zero ?"
    dg_noam surpris "Quoi, Zero ?"
    noam hesitation "Laisse tomber."
    dg_noam raison "Noam, s'il t'a raconté quelque chose, dis-le-moi."
    noam fatigue "J'ai dit laisse tomber."
    "Je repars avant qu'il insiste. Il ne sait vraiment pas ce que Zero m'a proposé."
    $ hideGroup()
    # Durée : 2m30

label _30_0_1_1_0_0_1_1_LABO:
    scene bg_laboratoire at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.5
    "Il est presque huit heures quand je reviens au laboratoire. Les autres ferment des caisses et se passent des affaires. Tout le monde parle en même temps."
    $ showGroup([("mara", "neutre", 0.17), ("kael", "calme", 0.50), ("julian", "sourire", 0.82)])
    mara neutre "Mais non, Julian, tu prends pas trois vestes. On part pour la Terre, pas pour traverser une montagne."
    julian taquin "Je me méfie de tes conseils vestimentaires, ma chère. Et puis, on ignore totalement la météo à l'arrivée !"
    kael calme "Vous avez tous les deux fini ? Parce que si on rate l'embarquement pour une veste, je vous laisse ici."
    julian surpris "Ah, il plaisante même pas ! C'est bon, c'est bon, j'en prends une."
    "Julian se retourne vers moi. Il me sourit, comme il aurait souri hier soir."
    julian sourire "Noam ! Tu vas pouvoir m'aider : tu préfères laquelle ?"
    noam fatigue "J'en sais rien, Julian."
    julian inquiet "Hé, t'as une tête de malade. T'as dormi, au moins ?"
    noam raison "Pas beaucoup."
    mara fatigue "Il est comme ça depuis hier. Laisse-le."
    julian reflexion "Bon... Je prends la noire, alors."
    "Je fixe le sol. J'ai l'impression d'entendre l'autre Julian me parler depuis son lit."
    kael neutre "Le départ est à dix heures. Il nous reste une heure pour être au sas à neuf heures. Tomas a vérifié les derniers accès."
    noam inquiet "Vous êtes sûrs que personne va se rendre compte de quelque chose ?"
    kael raison "Non. Sûr à cent pour cent, personne l'est. Mais on a fait tout ce qu'on pouvait."
    mara agace "Et maintenant, si tout le monde pouvait arrêter de nous porter la poisse, ce serait sympa."
    julian sourire "Moi, je nous trouve très convaincants !"
    noam colere "Ouais. C'est justement le problème."
    julian inquiet "Pardon ?"
    kael calme "Laisse, Julian. Va retrouver Nyra, elle t'attend pour les derniers détails."
    julian neutre "D'accord... À tout à l'heure, alors."
    $ showGroup([("mara", "fatigue", 0.21), ("kael", "inquiet", 0.55), ("noam", "fatigue", 0.82)])
    mara fatigue "Tu lui en veux à lui aussi, maintenant ? Il vient à peine de comprendre ce qu'il est."
    noam colere "Je lui en veux pas, Mara. Je pense juste à celui qui est mort dans sa chambre, c'est tout."
    mara fatigue "Moi aussi, j'y pense. Tu crois que j'ai oublié ?"
    kael calme "Ça suffit. On doit partir."
    "Kael regarde la porte, puis revient vers moi."
    kael inquiet "Noam, j'ai besoin de savoir : tu vas bien rejoindre le groupe au départ ?"
    noam hesitation "Ouais... enfin, faut encore que je règle un truc."
    mara agace "On dirait tous qu'on a un truc à régler aujourd'hui. Fais vite, alors."
    $ hideGroup()
    # Durée : 2m

label _30_0_1_1_0_0_1_1_CHOIX:
    $ current_period = "Matin"
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    "À 9 h 10, le Conclave commence à se vider. J'entends les premiers appels d'embarquement à travers les parois."
    "Zero m'attend dans un embranchement, sous les traits de Nyra. Il a encore quelques cheveux serrés dans la main."
    $ showGroup([("noam", "inquiet", 0.28), ("nyra", "neutre", 0.72)])
    zero_nyra_j29 neutre "Je voulais pas te faire attendre. Il faut que tu choisisses maintenant."
    noam agace "Ouais, j'ai compris. T'es sûr que c'est pas un piège ?"
    zero_nyra_j29 neutre "Non. Je veux vraiment que tu viennes sur Keyper, mais si tu refuses, je te laisse partir."
    noam raison "Et si j'accepte ?"
    zero_nyra_j29 neutre "Je te retrouverai après le départ. On prendra une autre navette. Mais je te le redis : je ne sais pas si on pourra revenir, ni si tu reverras Juliette."
    noam inquiet "Et si je dis non, tu fais quoi ?"
    zero_nyra_j29 neutre "Je tenterai d'y aller quand même. Je trouverai une autre solution, ou j'échouerai. C'est pas à toi de porter tout ça tout seul."
    noam fatigue "Putain... Il reste combien ?"
    zero_nyra_j29 neutre "Moins d'une heure. Et il te faudra encore rejoindre le sas si tu rentres."
    "Je regarde ma tablette. J'ai la photo de Juliette devant les yeux. J'aimerais tellement pouvoir lui demander ce qu'elle ferait."
    $ hideGroup()
    menu (screen="critical_choice", noam_expr="hesitation", cc_targets={"Refuser Zero — retourner sur Terre":{"label":"_30_0_1_1_0_0_1_1_RETOUR"},"Accepter Zero — partir pour Keyper-IIB":{"label":"_30_0_1_1_0_0_1_1_KEYPER"}}):
        "QUE FAIRE DE MA PLACE ?"
        "Refuser Zero — retourner sur Terre":
            $ j30_secret_zero_choice = "refuse"
            jump _30_0_1_1_0_0_1_1_RETOUR
        "Accepter Zero — partir pour Keyper-IIB":
            $ j30_secret_zero_choice = "accept"
            jump _30_0_1_1_0_0_1_1_KEYPER
    # Durée : 1m30

label _30_0_1_1_0_0_1_1_RETOUR:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "fatigue", 0.28), ("nyra", "neutre", 0.72)])
    noam fatigue "Je rentre. Je suis désolé, Zero, mais j'ai promis à Juliette d'être là, et je vais pas lui faire ça."
    zero_nyra_j29 neutre "T'as pas à t'excuser. Je t'avais dit que tu pouvais refuser."
    noam reflexion "Et Julian ? Tout ce qui s'est passé cette nuit... Tu vas pas me demander d'oublier ça ?"
    zero_nyra_j29 neutre "Non. Je ne veux pas que tu oublies."
    noam raison "Alors bonne chance, je suppose."
    zero_nyra_j29 neutre "Merci. Va voir ton double. Il est encore temps."
    $ hideGroup()
    "Je cours jusqu'au conduit des dortoirs. Je retrouve mon double avec son sac."
    $ showGroup([("noam", "inquiet", 0.25), ("dg_noam", "inquiet", 0.75)])
    noam raison "C'est moi qui pars sur Terre. Je vais monter à bord. Je veux reprendre ma place."
    dg_noam agace "Tu te fous de moi ? On en a parlé il y a une heure !"
    noam colere "Ouais, et maintenant j'ai décidé. C'est ma famille, ma vie, ma place, putain !"
    dg_noam colere "Et Iris ? Tu vas lui dire quoi ? Que le type dont elle est tombée amoureuse était juste un remplaçant ?"
    noam inquiet "Je lui dirai la vérité quand je pourrai. Mais je vais pas te laisser te faire passer pour moi jusqu'à la fin de sa vie."
    dg_noam fatigue "Tu crois vraiment que ça va être aussi simple ?"
    noam raison "Non. Et franchement j'ai aucune idée de ce qui va se passer. Mais il faut que ça s'arrête."
    dg_noam inquiet "Moi, j'ai rien, tu comprends ? J'ai pas de maison. Si je monte pas dans cette navette, je retourne où ?"
    noam fatigue "Zero part sur Keyper. Tu peux lui demander de venir avec lui."
    dg_noam surpris "Sur Keyper ? Là où Kami exploite les doubles ?"
    noam raison "Il veut les libérer."
    dg_noam agace "Tu me demandes de faire ça alors que t'as même pas voulu y aller toi-même !"
    noam fatigue "Ouais. T'as raison. J'ai pas le droit de te demander ça."
    "Il pose son sac. Il regarde la grille, puis ses mains."
    dg_noam raison "Si je reste ici, ils vont me trouver. J'ai pas le choix, en fait."
    noam inquiet "Je peux pas t'obliger à partir non plus."
    dg_noam fatigue "Non. Mais tu vas le faire quand même, sans le dire."
    noam raison "..."
    dg_noam inquiet "Promets-moi juste un truc. Quand tu parleras à Iris, raconte pas que je me suis foutu d'elle. J'ai pas fait semblant."
    noam fatigue "Je sais."
    dg_noam agace "Non. Tu le sais pas, mais bon... c'est pas grave."
    "Il me tend son sac. Je le repousse : c'est le sien."
    dg_noam fatigue "Prends soin de Juliette."
    noam inquiet "Je vais essayer."
    dg_noam neutre "Bon. File, alors. Tu vas rater la navette."
    $ hideGroup()
    scene bg_sas at adaptive_fullscreen with dissolve
    "J'arrive au sas alors que les derniers représentants montent. Iris me repère tout de suite."
    $ showGroup([("iris", "inquiet", 0.33), ("noam", "fatigue", 0.71)])
    iris inquiet "Putain, Noam ! T'étais où ?! Ça fait une éternité que je te cherche !"
    noam hesitation "J'ai dû... régler un truc. Je t'expliquerai."
    iris agace "J'espère bien ! J'ai cru que tu comptais partir sans moi, espèce d'idiot."
    noam inquiet "Non. Je suis là."
    iris neutre "Bon... viens, ils ferment bientôt."
    "Elle m'attrape la main. Je ne sais pas si elle se rend compte que ce n'est pas celle qu'elle a tenue hier."
    noam raison "Iris ? Après le départ, il faut vraiment qu'on parle."
    iris reflexion "Ouais. Je sais. Moi aussi j'ai des trucs à te dire."
    $ hideGroup()
    scene bg_navette at adaptive_fullscreen with dissolve
    "Je m'assois près du hublot. À dix heures précises, la navette se détache du Conclave."
    "Les autres parlent déjà de ce qu'ils vont faire en arrivant. Julian plaisante avec Elen, exactement comme il l'aurait fait."
    think "L'autre Julian est mort. Et je rentre quand même."
    scene black with fade
    "Quelques jours plus tard."
    # CG future 074 : Juliette retrouve Noam à son anniversaire.
    "Juliette me saute au cou dès que j'ouvre la porte. Elle m'engueule parce que je lui ai fait peur, puis elle me demande si j'ai pensé à son cadeau."
    "Je lui dis que oui. Je la serre tellement fort qu'elle finit par râler."
    "Quand elle repart chercher le gâteau, je reste un instant devant la fenêtre."
    think "Je suis rentré. C'est ce que je voulais."
    "Sur mon écran, une publicité vante les nouvelles ressources venues de Keyper-IIB."
    "Je l'éteins avant que Juliette revienne."
    $ j30_secret_ending = "retour_terre"
    "FIN — LE POIDS DU RETOUR"
    stop music fadeout 1.0
    return
    # Durée : 4m

label _30_0_1_1_0_0_1_1_KEYPER:
    scene bg_conduit_reseau at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "fatigue", 0.28), ("nyra", "neutre", 0.72)])
    noam raison "D'accord. Je viens. Mais tu me promets rien sur le retour, hein ? Parce que j'ai pas envie que tu me ressortes ça dans une heure."
    zero_nyra_j29 neutre "Je te promets rien. Et si tu changes d'avis avant dix heures, je te laisserai rejoindre les autres."
    noam colere "Je te préviens aussi : je te pardonne pas Julian. Je vais t'aider pour Keyper, mais je te pardonne pas ce que vous avez fait."
    zero_nyra_j29 neutre "Je comprends. Et je te demanderai pas de le faire."
    noam fatigue "Bon. Je vais parler à mon double."
    zero_nyra_j29 neutre "Je reste ici. Je veux pas qu'il sache que je t'ai fait cette proposition."
    $ hideGroup()
    "Je retourne à l'entrée des dortoirs. Mon double est toujours là. Il semble avoir renoncé à m'attendre."
    $ showGroup([("noam", "inquiet", 0.25), ("dg_noam", "neutre", 0.75)])
    noam raison "Je vais pas prendre la navette."
    dg_noam surpris "Quoi ?"
    noam fatigue "Tu peux rentrer sur Terre. Je te laisse ma place."
    dg_noam inquiet "Attends... t'es sérieux ?"
    noam neutre "Ouais."
    dg_noam surpris "Mais... pourquoi ?"
    noam raison "J'ai appris des choses sur Keyper. Il y a des gens là-bas qui ont besoin d'aide. J'ai décidé d'y aller."
    dg_noam inquiet "Qui t'a raconté ça ?"
    noam agace "Je peux pas te le dire. Pas maintenant."
    dg_noam raison "Et Iris ?"
    noam fatigue "Iris croit que t'es moi. Je sais. Mais fais pas le con avec elle."
    dg_noam colere "Pourquoi tu dis ça ? Je me suis jamais moqué d'elle !"
    noam raison "Alors tant mieux. Fais en sorte qu'elle soit heureuse, c'est tout."
    dg_noam inquiet "Noam, c'est... t'es en train de me donner ta vie, là."
    noam agace "Ouais, j'avais remarqué. Pas besoin de le répéter."
    "Il baisse les yeux, puis me regarde avec un air complètement perdu."
    noam raison "Il y a un truc que je veux que tu fasses. Juliette. Son anniversaire approche, je lui ai promis que je serais là."
    dg_noam inquiet "Je m'en souviens."
    noam colere "Non, écoute ! Je te demande pas de faire semblant d'être gentil deux minutes. Elle attend vraiment que je rentre. Si tu y vas, tu t'occupes d'elle. Tu l'abandonnes pas."
    dg_noam raison "Je vais y aller. Et je m'occuperai d'elle. Je te le promets."
    noam fatigue "J'espère."
    dg_noam inquiet "Tu penses que tu pourras revenir ?"
    noam neutre "J'en sais rien."
    dg_noam peur "Et si tu reviens pas ?"
    noam fatigue "Alors elle aura au moins quelqu'un à son anniversaire."
    dg_noam raison "Putain, Noam..."
    "Il me serre maladroitement dans ses bras, avant de se reculer comme s'il venait de faire une connerie."
    dg_noam fatigue "Désolé. Je savais pas quoi faire."
    noam neutre "Ouais. Moi non plus."
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Il est 9 h 45. Je suis revenu chercher ma tablette. La conversation avec Juliette est encore ouverte."
    "J'enregistre un message, juste pour lui dire que je l'aime et que je suis désolé de ne pas rentrer."
    "Je le réécoute. Elle le recevrait alors que quelqu'un avec mon visage viendra lui ouvrir les bras."
    "Je supprime l'enregistrement. Je garde la tablette avec moi."
    scene bg_sas at adaptive_fullscreen with dissolve
    "À 9 h 55, je reste derrière la porte du sas. De là, je vois Iris rejoindre mon double."
    $ showGroup([("iris", "neutre", 0.32), ("dg_noam", "neutre", 0.72)])
    iris agace "Ah, quand même ! Tu sais que j'étais à deux doigts de te chercher partout ?"
    dg_noam neutre "Ouais, désolé. On y va ?"
    iris sourire "Allez. Et dépêche-toi, j'ai pas envie de me faire engueuler par Kami pour toi."
    "Ils montent ensemble. Iris lui prend la main. Je regarde ailleurs."
    $ hideGroup()
    scene bg_navette at adaptive_fullscreen with dissolve
    "À dix heures, la navette quitte le Conclave. Je l'observe à travers la vitre, jusqu'à ce qu'elle soit trop loin pour distinguer les hublots."
    "Je rejoins Zero. Il a repris les traits de Nyra."
    $ showGroup([("noam", "fatigue", 0.28), ("nyra", "neutre", 0.72)])
    zero_nyra_j29 neutre "Tu peux encore me dire non."
    noam raison "Elle est déjà partie, la navette. Alors va falloir qu'on se bouge si tu veux libérer les autres."
    zero_nyra_j29 neutre "D'accord. Viens."
    $ hideGroup()
    scene black with fade
    "Plus tard."
    # CG future 075 : arrivée au-dessus des complexes industriels de Keyper-IIB.
    "De l'autre côté du hublot, Keyper-IIB apparaît. Je distingue des installations immenses, des lumières partout et des colonnes de fumée."
    zero_nyra_j29 neutre "Ils sont là-dessous. Je sais pas combien on pourra faire sortir."
    noam fatigue "Ouais... Moi non plus."
    zero_nyra_j29 neutre "Tu regrettes ?"
    noam raison "J'ai pas encore décidé. On commence par où ?"
    $ j30_secret_ending = "keyper"
    "FIN — À TA PLACE"
    stop music fadeout 1.0
    return
    # Durée : 4m

label _30_0_1_1_0_0_1_1_JULIAN_VIVANT_PLACEHOLDER:
    # Ne jamais faire passer un Julian vivant pour mort : branche J30 à écrire.
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je repense à ce que j'ai fait avec la seringue. Si Julian est toujours vivant, il est peut-être encore au laboratoire."
    "Je dois le retrouver avant le décollage. Je peux pas faire comme si tout s'était passé normalement."
    "À suivre — Julian sauvé."
    return
    # Durée : 0m30
