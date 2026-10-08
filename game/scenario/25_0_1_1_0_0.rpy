# =============================================================================
# JOUR 25 — LA PREUVE
# Route 0_1_1_0_0
#
# Objectifs narratifs :
# - Prolonger brièvement la normalité retrouvée au J24.
# - Noam entend un bruit dans sa propre ventilation mais refuse d'en faire une affaire.
# - Iris entend ensuite le même bruit : pour la première fois, quelqu'un confirme
#   immédiatement une perception liée aux conduits.
# - Ils découvrent un morceau de tissu brun entraîné dans le réseau.
# - Le tissu les conduit à retourner vers la salle de maintenance des Goumi.
# - Le corps de Mara est retrouvé : Iris le voit aussi.
# - Le morceau de tissu correspond à la veste du corps.
# - Noam n'a donc pas halluciné.
# - Ils comprennent qu'une personne ressemblant parfaitement à Mara vit avec eux.
# - Ils ne savent pas si Mara est la seule à avoir été remplacée.
# - Noam envisage de rendre la découverte publique au J26.
# =============================================================================

default j25_double_proof = False
default j25_cloth_found = False
default j25_iris_heard_vent = False


label _25_0_1_1_0_0_REVEIL:

    $ current_day = 25
    $ day_id = 25
    $ current_period = "Matin"

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    $ blink()

    "Je me réveille avant l'alarme avec cette sensation rare d'avoir réellement dormi, pas assez pour me sentir reposé, mais suffisamment pour ne pas avoir l'impression qu'une nuit entière vient de me tomber dessus."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Pendant quelques secondes, je reste allongé sans bouger, encore suffisamment engourdi pour que la journée d'hier me revienne par morceaux : Tomas incapable d'expliquer ce qui le dérangeait, le débat, le vote, puis les onze voix pour qui se sont affichées avant la mienne."

    think "On a réussi."

    "La pensée me fait sourire malgré moi. Ce n'est pas grand-chose comparé à tout ce qui s'est passé depuis notre arrivée, mais pour une fois je n'ai pas besoin de chercher immédiatement ce qui pourrait mal tourner derrière."

    "Mon regard finit quand même par glisser vers la grille d'aération."

    "Le bureau n'est plus complètement plaqué devant. Hier soir, je l'avais suffisamment déplacé pour dégager presque toute l'ouverture, comme si cette dizaine de centimètres pouvait constituer un compromis raisonnable entre ma paranoïa et l'envie de recommencer à vivre normalement."

    think "Très courageux."

    "Je me redresse, attrape mes vêtements et commence à m'habiller quand un léger bruit métallique vient du mur."

    play sound sfx_creak volume 0.35

    "Je m'arrête avec mon tee-shirt encore à moitié passé."

    pause 0.4

    "Rien."

    "J'attends malgré moi, les yeux fixés sur la grille, puis un second frottement résonne plus loin dans le conduit. Ce n'est pas assez fort pour ressembler à quelqu'un qui rampe ; plutôt quelque chose de léger qui vibre contre la tôle avant de retomber."

    think "Une plaque qui bouge."

    "Je termine d'enfiler mon tee-shirt."

    think "Ou une vis. Ou un morceau de métal. Ou littéralement n'importe quoi dans un réseau de ventilation vieux de je ne sais combien d'années."

    "Je reste encore quelques secondes debout devant le bureau, puis je souffle par le nez et récupère ma tablette."

    noam fatigue "Non."

    "Le mot sort tout seul."

    noam neutre "Pas aujourd'hui."

    "Iris m'a demandé de ne plus aller dans les conduits seul. Sael m'a fait passer suffisamment d'examens pour remplir un dossier médical entier. Et surtout, hier, pendant quelques heures, j'ai réussi à penser à autre chose."

    think "Je ne vais pas tout recommencer pour un bruit."

    "Je quitte la chambre sans toucher à la grille."

    stop music fadeout 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j25_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le couloir est déjà animé. Julian parle avec suffisamment d'énergie derrière une porte pour que je l'entende sans distinguer les mots, tandis que quelqu'un traverse l'autre extrémité avec un plateau de la cafétéria."

    "Je prends la direction du petit-déjeuner avec l'impression presque agréable d'avoir gagné une première bataille contre moi-même."

    jump _25_0_1_1_0_0_CAFETERIA


label _25_0_1_1_0_0_CAFETERIA:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j25_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "La cafétéria est déjà bien remplie quand j'arrive. L'ambiance du vote réussi n'a pas complètement disparu et, pour la première fois depuis plusieurs jours, personne ne semble considérer le petit-déjeuner comme une réunion de crise improvisée."

    $ showGroup([
        ("mara", "taquin", 0.05),
        ("elias", "fatigue", 0.18),
        ("iris", "blase", 0.31),
        ("tomas", "fatigue", 0.44),
        ("elen", "content", 0.57),
        ("julian", "sourire", 0.70),
        ("ryn", "neutre", 0.83),
        ("noam", "neutre", 0.96),
    ])

    mara taquin "Tiens, voilà notre sauveur des droits fondamentaux."

    noam blase "Ça commence tôt."

    julian sourire "Je trouve personnellement le titre très correct."

    iris blase "Évidemment."

    mara sourire "Je voulais dire médiateur suprême, mais ça faisait un peu secte."

    noam fatigue "Merci d'avoir su te retenir."

    mara taquin "Je fais des efforts."

    "Je récupère un plateau et viens m'asseoir pendant qu'Elen pousse vers moi une petite bouteille d'eau comme si elle me remettait une récompense."

    elen joie "Tiens. Grâce à toi, elle est constitutionnellement protégée maintenant."

    noam surpris "C'est déjà rétroactif sur mon petit-déjeuner ?"

    tomas reflexion "Techniquement, ce n'est pas une constitution."

    "Tout le monde tourne la tête vers lui."

    tomas fatigue "Quoi ?"

    iris sourire "Rien. C'est rassurant."

    tomas agace "Je vais très bien."

    ryn taquin "Aujourd'hui tu sais même où est ta tablette ?"

    tomas colere "Elle est devant moi."

    ryn sourire "Je vérifie."

    "Tomas lève les yeux au ciel mais son comportement semble déjà beaucoup plus proche de celui que je lui connais. Il a encore l'air fatigué, certes, mais il suit la conversation et ne fixe plus une tasse vide comme s'il attendait qu'elle lui fournisse une réponse."

    think "Donc il avait probablement juste mal dormi."

    "Cette conclusion devrait me satisfaire davantage qu'elle ne le fait."

    mara taquin "Et toi, docteur Noam ? Toujours officiellement sain du cerveau ?"

    "La question tombe avec suffisamment de légèreté pour provoquer quelques sourires autour de la table."

    noam blase "Toujours."

    mara sourire "Félicitations."

    noam taquin "Merci. J'ai beaucoup travaillé pour."

    iris agace "Tu peux peut-être arrêter de lui rappeler les examens toutes les cinq minutes."

    mara reflexion "Je me moque pas."

    iris blase "Tu te moques absolument."

    mara sourire "Oui, mais gentiment."

    "Je croise son regard."

    "Hier soir, je pouvais presque oublier ce que j'avais vu. Là, sous les lumières trop blanches de la cafétéria, Mara ressemble exactement à la Mara que je connais : même sourire, même façon de s'affaler sur sa chaise, même expression quand Iris lui répond trop sèchement."

    "Pendant un instant, le souvenir de la table dans la salle cachée paraît suffisamment absurde pour appartenir à quelqu'un d'autre."

    think "C'est peut-être ça, le plus simple."

    "Je prends une gorgée d'eau."

    think "Les examens n'ont rien trouvé, mais ça ne veut pas dire qu'un épisode isolé est impossible. Tomas me l'a encore dit."

    "Mara me fait un signe de la main devant le visage."

    mara reflexion "Tu repars ?"

    noam surpris "Quoi ?"

    mara taquin "T'as encore ce regard où ton cerveau quitte la pièce sans prévenir."

    noam fatigue "Je réfléchissais."

    iris blase "Mauvaise habitude."

    noam sourire "Je sais."

    "Cette fois, je parviens à sourire sans avoir besoin de me forcer."

    play sound sfx_announce

    "Le signal de Kami coupe les conversations avant que Mara puisse trouver une nouvelle façon de commenter mon état mental."

    $ hideGroup()

    stop music fadeout 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Bonjour, mes représentants préférés."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous avez eu vingt-quatre heures pour profiter de votre petite victoire. J'espère que c'était suffisant."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Parce qu'il est déjà temps de penser au prochain amendement."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "La proposition tirée au sort est la suivante : toute personne privée de liberté doit être informée du motif de sa détention et disposer d'un moyen de la contester."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu au jour vingt-sept."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "C'est presque touchant, cette obsession humaine pour savoir pourquoi on vous enferme."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Essayez simplement de ne mettre personne en cellule avant le vote. Ce serait dommage de créer un cas pratique trop tôt."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showGroup([
        ("mara", "taquin", 0.05),
        ("elias", "fatigue", 0.18),
        ("iris", "blase", 0.31),
        ("tomas", "reflexion", 0.44),
        ("elen", "content", 0.57),
        ("julian", "sourire", 0.70),
        ("ryn", "neutre", 0.83),
        ("noam", "reflexion", 0.96),
    ])

    iris blase "Elle a vraiment besoin de commenter chaque texte comme ça ?"

    julian sourire "Ça manque de sobriété, je te l'accorde."

    iris surpris "C'est toi qui dis ça ?"

    julian taquin "Je reconnais le talent chez les autres."

    ryn reflexion "Sur le fond, ça me paraît encore assez évident."

    tomas reflexion "Le principe, oui. Après il faudra regarder ce qu'on entend précisément par pouvoir contester."

    mara taquin "Oh non."

    tomas agace "Quoi, oh non ?"

    mara sourire "Tu recommences."

    tomas colere "J'ai le droit de lire un texte avant de voter !"

    noam taquin "Laisse-le, il a gagné le droit d'être prudent hier."

    tomas neutre "Merci."

    ryn sourire "Tu vois ? Le médiateur suprême."

    noam fatigue "Je vais finir par regretter le vote."

    "Quelques rires passent autour de la table et la discussion dérive rapidement vers autre chose. Personne n'a encore envie de transformer l'annonce de J27 en débat complet, ce qui me convient parfaitement."

    "Quand je termine mon plateau, je réalise que j'ai laissé ma tablette dans ma chambre."

    noam fatigue "Super."

    iris reflexion "Quoi ?"

    noam neutre "J'ai oublié ma tablette."

    iris taquin "Tomas déteint sur toi."

    tomas agace "Je suis littéralement à côté."

    iris blase "Je sais."

    noam sourire "Je vais la chercher avant d'oublier pourquoi j'y vais."

    iris neutre "Je viens. Je dois repasser par le dortoir avant d'aller à la salle commune."

    noam reflexion "Tu vas me surveiller jusque dans ma chambre maintenant ?"

    iris blase "Oui. C'est mon nouveau métier."

    "Je lève les yeux au ciel et nous quittons la cafétéria ensemble."

    $ hideGroup()

    jump _25_0_1_1_0_0_BRUIT


label _25_0_1_1_0_0_BRUIT:

    $ current_period = "Matin"

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "couloir_dortoir") from _call_j25_door_3
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    "Iris marche à côté de moi en consultant son téléphone pendant que nous traversons le dortoir. Elle me raconte quelque chose à propos de Julian qui aurait déjà commencé à écrire des arguments pour le vote de J27, mais je n'écoute qu'à moitié."

    iris reflexion "Tu m'écoutes ?"

    noam neutre "Oui."

    iris blase "Je viens de dire que Julian comptait défendre l'enfermement arbitraire."

    noam surpris "Quoi ?"

    iris sourire "Voilà."

    noam agace "Très drôle."

    "Elle range son téléphone avec un sourire satisfait."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_chambre") from _call_j25_door_4
    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je pousse la porte et vais directement récupérer ma tablette sur la table de chevet. Iris reste près de l'entrée, visiblement décidée à attendre les quinze secondes nécessaires plutôt que de continuer seule."

    iris blase "Mission accomplie ?"

    noam neutre "Presque."

    "Je vérifie rapidement que je n'ai rien oublié d'autre."

    play sound sfx_creak volume 0.35

    "Le frottement métallique revient derrière moi."

    "Cette fois, je ne suis pas le seul à m'arrêter."

    iris reflexion "C'était quoi ?"

    "Je garde la main sur ma tablette sans me retourner immédiatement."

    noam fatigue "La ventilation."

    iris reflexion "Merci, j'avais reconnu le mur."

    "Un deuxième petit choc résonne dans le conduit, suivi d'un frottement plus long qui s'arrête aussi brutalement qu'il a commencé."

    "Iris regarde la grille, puis moi."

    iris inquiet "Tu l'avais déjà entendu ?"

    "Je finis par me retourner."

    noam neutre "Ce matin."

    iris agace "Et tu m'as rien dit."

    noam fatigue "Parce qu'un bruit dans une ventilation, c'est pas exactement une preuve de meurtre."

    iris colere "Je t'avais demandé de venir me chercher si tu entendais quelque chose."

    noam raison "Tu m'avais demandé de pas retourner dans les conduits tout seul. C'est différent."

    iris agace "Tu joues vraiment sur les mots ?"

    noam neutre "Non. J'essaie juste de pas recommencer à paniquer à chaque fois qu'un bout de métal bouge derrière un mur."

    "Elle ouvre la bouche pour répondre, puis regarde de nouveau la grille."

    iris reflexion "Et t'as réussi ?"

    noam fatigue "J'étais parti prendre mon petit-déjeuner au lieu de démonter ma chambre, donc je dirais oui."

    iris neutre "Pas faux."

    "Elle s'approche du bureau."

    iris reflexion "On peut quand même regarder sans entrer."

    noam inquiet "Iris..."

    iris agace "Regarder, Noam. Avec nos yeux. Depuis la chambre. J'ai pas dit qu'on allait ramper jusqu'à la Terre."

    "Je soupire, pose ma tablette et l'aide à tirer le bureau de quelques centimètres supplémentaires."

    play sound sfx_creak volume 0.25

    "La grille est complètement dégagée."

    "Pendant quelques secondes, nous restons tous les deux devant comme deux idiots à attendre qu'elle fasse quelque chose."

    iris blase "Passionnant."

    noam taquin "Je t'avais prévenue."

    "Iris se penche légèrement, plisse les yeux puis attrape la petite lampe que j'avais laissée à côté du lit."

    iris reflexion "Attends."

    noam inquiet "Quoi ?"

    "Elle éclaire l'intérieur sans retirer la grille."

    iris reflexion "Il y a un truc plus loin."

    "Je me rapproche malgré moi."

    noam reflexion "Où ?"

    iris raison "À gauche, juste après la première jointure."

    "Je suis le faisceau. Au début je ne vois que le métal gris du conduit, puis quelque chose bouge faiblement lorsque la ventilation se remet en marche."

    "Un petit morceau brun est coincé sous une languette métallique légèrement tordue. À chaque variation du flux d'air, le tissu tire dessus et la languette vient frapper la paroi."

    play sound sfx_creak volume 0.25

    "Le même bruit."

    iris neutre "Voilà ton fantôme."

    "Je devrais rire."

    "Je ne le fais pas."

    "La couleur du tissu me bloque immédiatement."

    iris reflexion "Noam ?"

    noam inquiet "Attends."

    "Je retire les vis de la grille beaucoup plus vite que je ne l'aurais voulu quelques minutes plus tôt. Iris ne m'arrête pas ; elle garde simplement la lampe braquée vers l'intérieur pendant que je passe un bras dans l'ouverture."

    "Le morceau est plus loin que prévu. Mes doigts l'effleurent une première fois, puis j'arrive à le décrocher de la languette."

    "Quand je retire mon bras, un rectangle irrégulier de tissu brun repose dans ma paume. Une couture longe encore l'un des bords et plusieurs fils pendent là où il a été arraché."

    $ j25_cloth_found = True
    $ j25_iris_heard_vent = True

    iris reflexion "C'est juste du tissu."

    noam neutre "Je sais."

    iris inquiet "Alors pourquoi tu fais cette tête ?"

    "Je retourne le morceau entre mes doigts."

    "Je l'ai déjà vu."

    "Pas ce morceau précis. Cette matière. Cette couleur. Cette couture."

    "Sur une table métallique éclairée par ma lampe, autour du bras d'une fille qui ne respirait plus."

    noam fatigue "La veste."

    iris surpris "Quelle veste ?"

    "Je lève les yeux vers elle."

    noam inquiet "Mara."

    "Iris ne répond pas."

    noam raison "Quand je l'ai trouvée dans la salle des Goumi, elle avait une veste brune. La manche avait exactement ce genre de couture."

    iris desaccord "Beaucoup de fringues peuvent avoir une couture comme ça."

    noam neutre "Oui."

    iris reflexion "Et du tissu brun, c'est pas exactement rare."

    noam neutre "Je sais."

    "Elle fixe le morceau quelques secondes, puis la bouche d'aération."

    iris inquiet "Tu veux y retourner."

    noam reflexion "Je veux savoir d'où ça vient."

    iris desaccord "C'est pas la même chose."

    noam raison "Si ce morceau est arrivé jusque-là avec le flux d'air, il vient d'une autre partie du réseau. Et si quelqu'un a déplacé le corps par les conduits après que je l'ai vu..."

    "Je n'ai pas besoin de finir."

    iris fatigue "Putain."

    noam inquiet "Tu l'as entendu aussi."

    "Elle tourne les yeux vers moi."

    noam raison "Cette fois, je suis pas en train de te raconter qu'un bruit existe. Tu l'as entendu, tu as vu le morceau, tu l'as vu bouger avec la ventilation."

    iris agace "Je sais ce que j'ai entendu."

    noam neutre "Alors on vérifie."

    "Iris garde le silence un moment. Je m'attends presque à ce qu'elle refuse, qu'elle me rappelle le J20, le couteau, la manière dont j'avais perdu pied quand la salle s'était révélée vide."

    "Au lieu de ça, elle prend le morceau de tissu dans ma main, le regarde une dernière fois et me le rend."

    iris determine "On vérifie."

    noam surpris "Sérieux ?"

    iris colere "Ne me fais pas regretter."

    noam neutre "Je comptais pas."

    iris determine "Et on y va ensemble. Tu passes pas devant à trois embranchements de distance comme la dernière fois, tu touches à rien sans me prévenir et si je te dis qu'on ressort, on ressort."

    noam taquin "Tu veux aussi me tenir la main ?"

    iris blase "Si ça peut t'empêcher de ramasser un couteau, oui."

    "La référence suffit à me faire perdre mon sourire."

    noam fatigue "D'accord."

    "Iris le remarque, mais elle ne rajoute rien."

    "Je récupère la lampe, glisse le morceau de tissu dans une petite pochette de ma tablette et finis de retirer la grille."

    stop music fadeout 0.8

    jump _25_0_1_1_0_0_CONDUITS


label _25_0_1_1_0_0_CONDUITS:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    $ flashlight_on(pattern=2)

    "Je me glisse le premier dans le conduit, mais cette fois Iris reste immédiatement derrière moi. Nous avançons lentement, beaucoup plus lentement que lorsque j'avais fui ici au J20, et le réseau me paraît presque différent simplement parce que je ne suis plus seul à entendre chacun de ses bruits."

    $ showGroup([
        ("noam", "reflexion", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    iris inquiet "Tu reconnais le chemin ?"

    noam neutre "Oui."

    iris reflexion "Tu disais déjà ça la dernière fois."

    noam agace "Et je nous avais amenés à la bonne salle."

    iris neutre "Vide."

    noam fatigue "Merci pour le rappel."

    "Elle ne répond pas immédiatement."

    iris inquiet "Désolée."

    noam neutre "Non. T'as raison."

    "Je continue jusqu'au premier embranchement. Une partie de moi s'attend à retrouver des traces évidentes, du sang, un autre morceau de tissu ou n'importe quoi qui transformerait immédiatement notre intuition en certitude."

    "Il n'y a rien."

    noam reflexion "Le flux vient surtout de cette branche."

    iris surpris "Tu sais ça comment ?"

    noam taquin "J'ai développé une relation très personnelle avec la ventilation ces derniers jours."

    iris blase "Je regrette d'avoir demandé."

    "Je rapproche ma main d'une ouverture latérale. L'air y circule effectivement plus fort et, quand je braque la lampe à l'intérieur, plusieurs poussières et petits débris se déplacent dans la même direction que celle qui mène vers ma chambre."

    noam raison "Si le tissu s'est décroché quelque part plus loin, il a pu être entraîné jusqu'à la première jointure avant de se coincer."

    iris reflexion "Tu réalises qu'on est en train de faire une enquête sur un bout de manche transporté par de l'air ?"

    noam neutre "Oui."

    iris fatigue "Super."

    "Nous repartons."

    $ hideGroup()

    "À mesure que nous avançons, les bifurcations deviennent familières. Je reconnais la plaque légèrement enfoncée contre laquelle je m'étais cogné en revenant du laboratoire, puis le virage étroit où Kael avait failli rester coincé au J20."

    "Le souvenir de cette journée revient avec une précision désagréable. Iris derrière moi. Kael en dernier. Ma certitude absolue qu'en arrivant dans la salle, ils comprendraient enfin."

    think "Et la table était vide."

    "Je ralentis."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "reflexion", 0.66),
    ])

    iris reflexion "Pourquoi tu t'arrêtes ?"

    noam fatigue "Parce qu'à partir d'ici, je reconnais vraiment tout."

    "Iris regarde devant nous, puis mon visage."

    iris inquiet "Tu veux ressortir ?"

    "La question est sérieuse."

    noam reflexion "Non."

    iris neutre "D'accord."

    "Elle ne me pousse pas davantage."

    "Nous avançons encore quelques mètres jusqu'à la grille donnant sur la salle de maintenance des Goumi."

    "Je coupe presque instinctivement ma lampe avant de regarder à travers."

    iris surpris "Pourquoi tu l'éteins ?"

    noam inquiet "Je sais pas."

    "La réponse est suffisamment honnête pour qu'elle ne commente pas."

    "Je colle lentement mon visage contre l'ouverture."

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve

    "La salle paraît vide."

    "Les deux Goumi de rechange sont toujours là, immobiles près des établis. La table sur laquelle j'avais trouvé Mara est visible depuis la grille."

    "Vide."

    "Mon estomac se serre malgré moi."

    think "Évidemment."

    "Je reste encore quelques secondes à chercher un détail qui justifierait notre présence ici."

    iris "Alors ?"

    noam fatigue "La table est vide."

    iris neutre "On descend quand même."

    "Cette fois, c'est elle qui le dit."

    "Je tourne légèrement la tête vers elle."

    noam reflexion "T'es sûre ?"

    iris agace "On a rampé jusque-là. Je vais pas repartir parce qu'une table est vide."

    "Je rallume la lampe et retire la grille."

    $ hideGroup()

    jump _25_0_1_1_0_0_SALLE_GOUMI


label _25_0_1_1_0_0_SALLE_GOUMI:

    scene bg_salle_goumi_cachee at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0
    $ flashlight_on(pattern=1)

    "Je descends le premier et attends qu'Iris pose les pieds au sol avant de faire un pas de plus. La pièce n'a presque pas changé depuis notre dernière visite : mêmes établis, mêmes machines, mêmes rangements ouverts, et surtout cette table métallique vide qui occupe immédiatement tout mon champ de vision."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    noam fatigue "C'était là."

    iris neutre "Je sais."

    noam reflexion "Exactement là."

    iris agace "Noam."

    noam fatigue "D'accord."

    "Je force mon regard à quitter la table."

    iris raison "On cherche quelque chose qui pourrait avoir laissé ce morceau. Pas le corps en priorité."

    noam reflexion "Le tissu vient probablement pas de la pièce elle-même."

    iris neutre "Peut-être. Mais quelqu'un a déplacé du matériel ici avant, donc on regarde quand même."

    "Nous commençons par les zones proches des conduits. Iris inspecte le bord des établis pendant que je passe la lampe derrière les deux Goumi de rechange et sous les structures métalliques."

    "Rien."

    "Je vérifie ensuite les rangements ouverts sous la table. Un bac vide, des câbles, quelques outils, aucune trace brune."

    noam fatigue "Rien."

    iris reflexion "Attends."

    "Iris s'est arrêtée près du second Goumi."

    noam inquiet "Quoi ?"

    iris raison "Aide-moi à le déplacer."

    noam surpris "Pourquoi ?"

    iris reflexion "Parce qu'il y a de la poussière partout sauf juste derrière."

    "Je braque la lampe au sol."

    "Elle a raison. Une bande plus sombre traverse la poussière, comme si quelque chose de lourd avait été poussé puis remis approximativement à sa place."

    think "Quelque chose de lourd."

    "Je sens mon ventre se nouer."

    noam raison "On le pousse ensemble."

    iris neutre "Doucement."

    "Nous nous plaçons chacun d'un côté de la structure. Le Goumi de rechange est plus lourd qu'il en a l'air et résiste quelques secondes avant de glisser avec un grincement profond sur le sol."

    play sound sfx_creak volume 0.65

    "Derrière, une plaque de maintenance est apparue dans le mur."

    iris reflexion "Ça, c'était visible la dernière fois ?"

    noam neutre "Non. Le Goumi était devant."

    iris inquiet "Et tu avais regardé derrière ?"

    noam fatigue "J'ai regardé autour. Pas déplacé une machine de cent kilos."

    iris neutre "Logique."

    "La plaque n'est pas verrouillée. Deux attaches mécaniques la maintiennent fermée et l'une d'elles porte une fine fibre brune coincée dans le mécanisme."

    "Iris la voit au même moment que moi."

    iris inquiet "Noam."

    noam neutre "Je vois."

    "Je sors la pochette contenant le morceau récupéré dans ma chambre et le place à quelques centimètres de la fibre sans la toucher."

    "Même couleur."

    "Même texture."

    "Iris cesse de respirer pendant une seconde."

    noam inquiet "On ouvre ?"

    "Elle me regarde comme si la question était absurde, puis pose sa main sur l'attache."

    iris determine "Ensemble."

    "Nous déverrouillons les deux côtés."

    stop music fadeout 0.8

    "La plaque s'ouvre de quelques centimètres."

    "Une odeur me frappe immédiatement."

    "Je recule d'un demi-pas."

    iris peur "C'est quoi..."

    "Je connais cette odeur sans l'avoir réellement comprise la première fois. Dans la salle, elle était mélangée au métal, à la poussière et aux produits de maintenance."

    "Là, enfermée derrière cette plaque depuis plusieurs jours, il n'y a plus de doute possible."

    play music "music/bgm_horror_pulse.mp3" fadein 0.6
    $ danger_on()

    noam peur "Recule."

    iris surpris "Quoi ?"

    noam peur "Iris, recule."

    "Elle ne bouge pas."

    "Je tire lentement la plaque."

    scene black with Dissolve(0.25)

    pause 0.5

    $ unlock_gallery_image("bg_cg040")
    scene bg_cg040 at adaptive_fullscreen with signal_stutter
    $ doppelganger_reveal(screamer=False, duration=0.80, restore_volume=0.65)

    "Le faisceau de la lampe tombe sur un visage."

    "Le même visage."

    "Je n'ai même pas besoin de regarder davantage pour savoir."

    "Mara."

    "Son corps a été replié dans l'espace technique derrière la cloison, suffisamment loin pour être invisible depuis la salle, mais pas assez pour effacer ce que j'avais vu la première nuit."

    "Pendant plusieurs secondes, je n'entends plus Iris."

    "Je n'entends même plus la ventilation."

    think "Elle est là."

    "Pas un souvenir."

    "Pas une image créée par mon cerveau."

    "Pas quelque chose que les examens auraient dû trouver."

    "Elle est là."

    scene bg_salle_goumi_cachee at adaptive_fullscreen with memory_rip

    $ showGroup([
        ("noam", "peur", 0.36),
        ("iris", "peur", 0.66),
    ])

    "Iris a reculé jusqu'à l'établi. Une main couvre sa bouche et ses yeux restent fixés sur l'ouverture."

    iris peur "Putain..."

    "Sa voix est presque inaudible."

    noam faible "Je te l'avais dit."

    "La phrase sort sans colère. Je n'éprouve même pas la satisfaction sordide d'avoir eu raison."

    iris peur "Non."

    noam inquiet "Quoi ?"

    iris peur "Ne dis pas ça comme ça."

    "Elle retire lentement sa main de sa bouche."

    iris peur "Je te croyais pas."

    noam neutre "Je sais."

    iris desespoir "Je pensais que t'avais vu quelque chose, que t'étais épuisé, que ton cerveau avait mélangé..."

    noam fatigue "Je sais."

    iris colere "Arrête de dire que tu sais !"

    "Sa voix claque dans la salle et me fait sursauter."

    iris peur "Elle était à table avec nous il y a une heure."

    noam inquiet "Oui."

    iris desespoir "Elle m'a parlé."

    noam neutre "Oui."

    iris peur "Elle s'est foutue de ta gueule."

    noam fatigue "Iris..."

    iris colere "Et elle est là !"

    "Elle désigne l'ouverture sans réussir à la regarder directement."

    iris peur "Alors c'est quoi, ça ?!"

    "Je n'ai aucune réponse."

    "Je m'approche malgré tout de la plaque. Cette fois, je ne touche pas le corps ; je braque simplement la lampe sur la veste."

    "La manche droite est déchirée sur plusieurs centimètres."

    noam inquiet "Le morceau."

    "Iris s'immobilise."

    "Je ressors la pochette et approche le tissu de la déchirure sans le poser dessus. La couture continue presque exactement celle de la manche et les fils arrachés correspondent jusque dans leur orientation."

    iris peur "C'est le même."

    noam raison "Oui."

    iris peur "T'es sûr ?"

    noam reflexion "Regarde la couture."

    "Elle le fait."

    "Son visage change."

    "Ce n'est plus seulement de la peur. Quelque chose vient de céder dans la dernière explication raisonnable qu'elle pouvait encore conserver."

    $ j25_double_proof = True
    $ investigation_add("preuve_mara_double")

    iris faible "Donc t'as pas halluciné."

    noam neutre "Non."

    "Je devrais ressentir du soulagement."

    "Depuis cinq jours, je veux une preuve que ce que j'avais vu existait réellement. J'ai accepté les examens de Sael parce que j'espérais presque qu'ils trouvent quelque chose dans mon cerveau, puis j'ai passé deux nuits à me demander si le problème venait de moi."

    "Maintenant, j'ai ma réponse."

    think "J'aurais préféré être malade."

    iris inquiet "Noam..."

    noam reflexion "La Mara de la cafétéria n'est pas celle-là."

    iris desaccord "On n'en sait rien."

    noam surpris "Quoi ?"

    iris raison "On sait qu'il y a un corps qui ressemble exactement à Mara et une Mara vivante dehors. C'est tout."

    noam colere "Iris, regarde-la."

    iris inquiet "Je la regarde !"

    noam determine "Alors tu veux appeler ça comment ?"

    iris colere "J'en sais rien !"

    "Sa voix tremble à nouveau, mais cette fois elle tient mon regard."

    iris raison "Je veux juste pas commencer à inventer le reste parce qu'on vient de découvrir quelque chose d'impossible."

    "Je baisse les yeux vers la veste."

    "Elle a raison."

    "Je déteste qu'elle ait raison."

    noam reflexion "D'accord."

    iris inquiet "On sait que tu n'as pas halluciné le corps."

    noam neutre "Oui."

    iris raison "On sait que quelqu'un l'a déplacé après que tu l'as trouvé, parce qu'il n'était plus sur la table quand on est revenus."

    noam neutre "Oui."

    iris raison "Et on sait qu'une personne identique à Mara vit avec nous."

    "Elle marque une pause avant la dernière phrase."

    iris peur "Mais on sait pas laquelle des deux est... enfin..."

    noam fatigue "Mara."

    "Le prénom semble soudainement absurde."

    "Je regarde le corps, puis la porte de la salle comme si l'autre pouvait entrer à n'importe quel moment."

    noam inquiet "Il faut partir."

    iris surpris "Attends."

    noam raison "On a ce qu'il nous faut. Le corps, le tissu, toi qui l'as vu. On reste pas ici à discuter."

    iris determine "D'accord."

    "Elle referme la plaque avec moi. Aucun de nous ne propose de déplacer le corps ou de prélever autre chose."

    "Quand le Goumi retrouve approximativement sa place devant la cloison, je réalise à quel point il suffit de peu pour que toute la scène redevienne invisible."

    $ danger_off()
    $ hideGroup()
    $ flashlight_on(pattern=3)

    jump _25_0_1_1_0_0_RETOUR


label _25_0_1_1_0_0_RETOUR:

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8

    "Le retour est beaucoup plus lent que l'aller. Iris reste derrière moi, mais je l'entends vérifier régulièrement ce qu'il y a dans notre dos et je me surprends à faire exactement la même chose à chaque embranchement."

    "Personne ne parle pendant plusieurs minutes."

    "Ce n'est qu'à mi-chemin qu'Iris finit par rompre le silence."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    iris inquiet "On dit rien."

    "Je m'arrête suffisamment brusquement pour qu'elle manque de me rentrer dedans."

    noam surpris "Quoi ?"

    iris raison "Pas maintenant."

    noam desaccord "Iris, il y a un corps de Mara derrière une cloison pendant qu'une autre Mara mange avec nous."

    iris colere "Je sais, j'étais là !"

    noam raison "Alors on peut pas juste remonter et faire comme si de rien n'était."

    iris agace "Je te demande pas de faire comme si de rien n'était. Je te demande de réfléchir avant d'annoncer ça à onze personnes dont on sait plus rien."

    "Je reste silencieux."

    iris raison "Si la Mara qu'on connaît n'est pas Mara, ça veut dire que quelqu'un a réussi à la remplacer sans qu'aucun de nous s'en rende compte."

    noam reflexion "Oui."

    iris inquiet "Et rien ne nous dit que c'est arrivé qu'une fois."

    "Cette phrase suffit à rendre le conduit plus étroit."

    "Je repense immédiatement à Elias, à son changement d'attitude autour des plaques, à ses disparitions, puis à Tomas hier matin, incapable de retrouver une idée qu'il semblait avoir en tête depuis plusieurs heures."

    think "Non."

    "Je refuse de laisser mon cerveau établir une liste entière sur la base de comportements qui peuvent avoir dix explications normales."

    noam raison "On peut pas soupçonner tout le monde."

    iris neutre "Je sais."

    noam reflexion "Tomas était bizarre hier."

    iris inquiet "Je sais."

    noam raison "Et Elias..."

    iris colere "Justement. Arrête."

    "Je tourne la tête vers elle."

    iris raison "Tu vois ce qu'on est déjà en train de faire ? Deux minutes après avoir trouvé le corps, on commence à prendre tous les trucs bizarres des derniers jours et à décider qu'ils veulent dire quelque chose."

    noam fatigue "Donc on fait quoi ?"

    iris neutre "On garde les faits."

    noam reflexion "Le corps existe."

    iris neutre "Oui."

    noam reflexion "Le tissu vient de sa veste."

    iris neutre "Oui."

    noam reflexion "Quelqu'un l'a cachée après ma première découverte."

    iris raison "Très probablement."

    noam reflexion "Et une autre Mara est avec nous."

    iris inquiet "Oui."

    "Je reprends ma respiration."

    noam raison "Ça suffit déjà."

    iris neutre "Largement."

    "Nous recommençons à avancer."

    $ hideGroup()

    "Quelques mètres plus loin, une autre pensée me frappe avec suffisamment de force pour que je ralentisse encore."

    think "Kami."

    "Les caméras."

    "Les diffusions."

    "La Terre entière qui suit le Conclave depuis le début."

    think "Si on le dit devant une caméra..."

    "Iris remarque mon silence."

    $ showGroup([
        ("noam", "reflexion", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    iris inquiet "Quoi encore ?"

    noam reflexion "Le monde nous regarde."

    "Elle comprend presque immédiatement."

    iris desaccord "Non."

    noam raison "Écoute."

    iris colere "Non, j'ai très bien compris. Tu veux balancer ça publiquement."

    noam raison "Si quelqu'un ici remplace des représentants, le pire truc qu'on puisse faire c'est garder l'information enfermée dans la station avec lui."

    iris desaccord "Et le meilleur truc, selon toi, c'est lui annoncer que tu sais ?"

    noam "Pas à lui. À tout le monde."

    iris colere "Il regarde aussi les caméras, Noam !"

    noam raison "Mais si l'information sort, elle peut plus disparaître avec nous."

    "Iris serre les dents."

    iris inquiet "Tu t'entends ?"

    noam neutre "Oui."

    iris raison "Tu parles déjà comme si on allait tous crever ici."

    noam fatigue "J'ai trouvé le corps de quelqu'un qui a pris le petit-déjeuner avec nous ce matin. Excuse-moi si mes perspectives se sont un peu dégradées."

    "Elle ne répond pas tout de suite."

    iris fatigue "Je dis pas que l'idée est complètement mauvaise."

    noam surpris "C'est presque un compliment."

    iris agace "Je dis qu'elle peut te faire tuer avant même qu'on comprenne ce qui se passe."

    noam inquiet "Alors on réfléchit jusqu'à demain."

    iris blase "Tu vas réfléchir ?"

    noam neutre "Oui."

    iris blase "Vraiment réfléchir, ou attendre douze heures avant de faire exactement ce que t'as déjà décidé ?"

    "Je ne réponds pas."

    iris colere "Noam."

    noam fatigue "Je vais réfléchir."

    iris desaccord "Ça veut dire la deuxième option."

    "Je reprends ma route avant qu'elle puisse continuer."

    $ hideGroup()

    jump _25_0_1_1_0_0_CHAMBRE


label _25_0_1_1_0_0_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    $ flashlight_off()

    "Quand nous ressortons enfin dans ma chambre, la lumière normale me paraît presque agressive. Je remets immédiatement la grille en place pendant qu'Iris referme les rideaux par réflexe, puis nous restons quelques secondes debout sans savoir quoi faire de nos mains."

    $ showGroup([
        ("noam", "inquiet", 0.36),
        ("iris", "inquiet", 0.66),
    ])

    iris raison "Montre-moi le morceau."

    "Je le sors de la pochette."

    "Iris l'observe encore une fois sous la lumière de la chambre. Il paraît beaucoup plus banal ici : juste un bout de tissu sale, assez petit pour être jeté sans même y penser."

    iris reflexion "On le garde."

    noam neutre "Évidemment."

    iris raison "Et pas dans un endroit évident."

    noam reflexion "Tu crois qu'ils vont fouiller ma chambre ?"

    iris inquiet "J'en sais rien."

    noam fatigue "Bonne réponse."

    "Je glisse la pochette dans le fond de mon dossier papier, entre deux feuilles qui n'ont rien à voir avec l'enquête."

    iris neutre "Ça suffira pour l'instant."

    "Elle s'assoit sur le bord de mon lit."

    "Je reste debout."

    noam reflexion "Il faut prévenir au moins Sael."

    iris desaccord "Pourquoi elle ?"

    noam raison "Parce qu'elle a fait mes examens, parce qu'elle peut confirmer que j'avais aucune anomalie et parce qu'elle saurait peut-être examiner le corps correctement."

    iris reflexion "Et si c'est pas Sael ?"

    "Je m'arrête."

    "Le simple fait qu'elle pose la question me donne envie de l'envoyer promener."

    "Je n'y arrive pas."

    noam fatigue "Voilà pourquoi cette situation est débile."

    iris neutre "Oui."

    noam raison "On peut pas rester à deux avec ça."

    iris inquiet "Pas longtemps."

    noam reflexion "Mais aujourd'hui ?"

    "Elle secoue lentement la tête."

    iris neutre "Aujourd'hui, on observe."

    noam desaccord "J'aime pas ça."

    iris blase "Moi non plus."

    noam reflexion "Et si Mara disparaît cette nuit ?"

    iris inquiet "Alors on saura qu'elle a compris quelque chose."

    noam agace "C'est censé me rassurer ?"

    iris "Non."

    "Je fais quelques pas dans la chambre."

    noam raison "J'ai passé plusieurs jours à croire que j'étais peut-être en train de perdre la tête."

    iris fatigue "Je sais."

    noam reflexion "Et maintenant que je sais que c'était réel, je préférerais presque revenir à hier."

    "Iris baisse les yeux."

    iris neutre "Moi aussi."

    "Sa réponse est immédiate."

    "Je la regarde."

    iris fatigue "Quand Sael a dit qu'elle avait rien trouvé, j'étais soulagée. Pas parce que ça voulait dire que t'avais raison. Parce que je pensais qu'on finirait par trouver une explication plus simple."

    noam neutre "Il y en a plus."

    iris inquiet "Non."

    "Le silence retombe."

    "Pour la première fois depuis que nous sommes revenus, je prends réellement conscience d'une autre chose : Iris a vu le corps. Elle ne peut plus rentrer dans sa chambre et se convaincre que j'ai mal interprété quelque chose."

    "Je ne suis plus seul avec le souvenir."

    "Et elle non plus."

    noam reflexion "Ça va ?"

    iris blase "Question débile."

    noam sourire "Je sais."

    iris fatigue "Non."

    "Elle laisse échapper un souffle et passe une main dans ses cheveux."

    iris reflexion "Mais au moins maintenant, si tu commences à raconter n'importe quoi, je pourrai te dire précisément quelle partie est vraie."

    noam taquin "C'est touchant."

    iris agace "Profite pas."

    "Un petit sourire lui échappe malgré elle, puis disparaît presque immédiatement."

    iris inquiet "Promets-moi juste un truc."

    noam reflexion "Ça dépend."

    iris colere "Noam."

    noam neutre "D'accord. Quoi ?"

    iris raison "Tu vas pas voir Mara seul pour la confronter."

    "Je n'y avais même pas pensé jusque-là."

    noam surpris "Je comptais pas faire ça."

    iris neutre "Bien."

    noam reflexion "Et toi non plus."

    iris blase "Je suis pas suicidaire."

    noam taquin "Ça aussi, c'est rassurant."

    "Elle se lève."

    iris raison "On retourne avec les autres. Si on disparaît tous les deux pendant trois heures juste après avoir commencé à fouiller les conduits, ça finira par se remarquer."

    noam inquiet "Tu veux vraiment retourner à la cafétéria ?"

    iris neutre "Oui."

    noam surpris "Maintenant ?"

    iris raison "Justement. Si on commence à éviter Mara, elle le verra."

    "Je déteste encore une fois qu'elle ait raison."

    noam fatigue "Génial."

    iris blase "Tu voulais une preuve."

    noam "Pas celle-là."

    "Elle ouvre la porte."

    iris neutre "Moi non plus."

    $ hideGroup()

    jump _25_0_1_1_0_0_APRES_MIDI


label _25_0_1_1_0_0_APRES_MIDI:

    $ current_period = "Après-midi"

    call show_custom_title("Un peu plus tard") from _call_show_custom_title_j25_1

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Revenir à la cafétéria est probablement l'une des choses les plus absurdes que j'ai faites depuis le début du Conclave."

    "Une heure plus tôt, j'y mangeais avec Mara en me demandant si je pouvais enfin arrêter d'avoir peur d'elle. Maintenant, je pousse la même porte en sachant que son corps est caché à quelques dizaines de mètres de nous derrière une plaque de maintenance."

    $ showGroup([
        ("mara", "taquin", 0.10),
        ("elias", "fatigue", 0.24),
        ("elen", "content", 0.38),
        ("julian", "sourire", 0.52),
        ("tomas", "neutre", 0.66),
        ("iris", "neutre", 0.80),
        ("noam", "neutre", 0.94),
    ])

    mara taquin "Ah ! Les fugitifs."

    "Mon corps se tend avant même que j'aie le temps de réfléchir."

    "Iris me donne un très léger coup de coude en passant à côté de moi."

    iris blase "On est partis vingt minutes."

    mara sourire "C'est long, vingt minutes."

    julian taquin "Tout dépend de l'activité."

    iris colere "Vous êtes insupportables."

    elen content "On allait lancer un jeu !"

    noam reflexion "Quel jeu ?"

    elen joie "Celui avec les cartes où il faut faire deviner des trucs sans dire certains mots."

    tomas fatigue "Julian triche."

    julian surpris "Je ne triche pas."

    elias fatigue "Tu changes les règles quand tu perds."

    julian colere "Je les interprète."

    "La phrase me fait presque rire malgré moi."

    "Presque."

    mara reflexion "Noam ?"

    "Je tourne la tête vers elle."

    noam neutre "Quoi ?"

    mara taquin "T'as encore décroché."

    "Je la regarde vraiment."

    "Elle respire."

    "Elle cligne des yeux."

    "Une mèche tombe devant son visage et elle la repousse exactement comme elle l'a déjà fait des dizaines de fois."

    "Si je n'avais pas vu l'autre corps, rien dans cette scène ne me permettrait de dire qu'il y a quoi que ce soit d'anormal."

    think "Comment tu fais ?"

    mara reflexion "J'ai un truc sur la gueule ?"

    "La question me frappe suffisamment fort pour me ramener dans la pièce."

    noam surpris "Non."

    mara taquin "Alors arrête de me fixer, je vais finir par croire que tu me trouves belle."

    noam blase "Ton ego survivra."

    mara sourire "Je prends ça pour un oui."

    "Iris récupère les cartes avant que je doive répondre davantage."

    iris neutre "On joue."

    elen joie "Oui !"

    "Je m'assois."

    "Pendant les vingt minutes qui suivent, je découvre qu'il est possible de participer à un jeu idiot tout en surveillant constamment les mains, la voix et les expressions de la personne assise en face de soi."

    "Mara rit aux mêmes blagues."

    "Elle connaît les mêmes références."

    "Elle se dispute avec Julian de la même façon."

    "Elle se souvient même d'une anecdote du jour onze que j'avais presque oubliée."

    think "Si c'est une copie..."

    "Je coupe la pensée."

    think "Faits."

    "Iris avait raison."

    "Le fait est simple : il existe un cadavre identique à Mara."

    "Tout le reste est encore une hypothèse."

    $ hideGroup()

    call show_custom_title("Plus tard") from _call_show_custom_title_j25_2

    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8

    "Je finis par quitter la partie sous prétexte d'aller chercher de l'eau. Iris reste avec les autres, probablement pour éviter qu'on remarque que nous nous déplaçons désormais systématiquement ensemble."

    "Je fais quelques pas dans le couloir et m'appuie contre le mur."

    think "Le monde regarde."

    "La pensée revient."

    "Pas seulement Kami. Pas seulement les onze autres. Le Conclave est diffusé, commenté, archivé."

    "Si je raconte ce que nous avons trouvé devant une caméra, l'information sort immédiatement de cette station."

    think "Et personne ne pourra la remettre derrière une plaque."

    "Mais Iris a raison sur l'autre partie."

    "Si la Mara vivante sait que je sais, et si elle est responsable de ce qui est arrivé à l'autre..."

    "Je regarde machinalement derrière moi."

    "Le couloir est vide."

    think "Alors je lui donne une raison de s'occuper de moi."

    "Je reste appuyé contre le mur encore quelques secondes."

    think "Demain."

    "Pas parce que j'ai pris une décision."

    "Parce que j'ai besoin d'une nuit pour réussir à prétendre que ce n'est pas déjà le cas."

    jump _25_0_1_1_0_0_SOIR


label _25_0_1_1_0_0_SOIR:

    $ current_period = "Soir"

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Il est tard quand je retourne enfin vers ma chambre. J'ai passé l'après-midi à faire semblant d'écouter des conversations normales, puis le début de soirée à éviter soigneusement d'avoir l'air de faire semblant."

    "Je suis presque arrivé devant ma porte quand quelqu'un m'appelle derrière."

    mara "Noam."

    "Je m'arrête."

    "Une seconde entière passe avant que je me retourne."

    $ showGroup([
        ("mara", "neutre", 0.38),
        ("noam", "inquiet", 0.64),
    ])

    mara reflexion "Ça va ?"

    "Elle est seule."

    "Le couloir aussi."

    "Mon premier réflexe est de regarder vers les portes voisines pour vérifier si quelqu'un pourrait nous entendre."

    "Je m'en veux immédiatement."

    noam neutre "Oui."

    mara blase "Tu mens mal."

    noam taquin "On me le dit souvent."

    "Elle s'approche de deux pas."

    "Je ne recule pas."

    "C'est probablement l'effort le plus difficile de toute la journée."

    mara reflexion "Depuis ce matin, tu me regardes bizarrement."

    noam fatigue "Je regarde tout le monde bizarrement."

    mara taquin "Charmant."

    noam neutre "Désolé."

    "Elle m'observe quelques secondes. Son expression n'a rien de menaçant ; au contraire, elle a l'air sincèrement préoccupée."

    mara neutre "C'est encore à cause de ce que t'as vu ?"

    "La question me serre la gorge."

    noam reflexion "Pourquoi tu demandes ?"

    mara fatigue "Parce qu'avant-hier tu flippais quand je te touchais, hier ça allait mieux et aujourd'hui t'as recommencé à me fixer comme si j'allais me transformer en monstre."

    "Je pourrais presque rire du choix des mots."

    "Je n'y arrive pas."

    noam neutre "J'ai juste mal dormi."

    mara reflexion "Encore ?"

    noam sourire "Apparemment, c'est ma spécialité."

    "Elle secoue légèrement la tête."

    mara neutre "Si t'as besoin de parler, tu sais où me trouver."

    "La phrase est probablement l'une des plus normales qu'elle ait jamais prononcées."

    "C'est précisément ce qui la rend insupportable."

    noam reflexion "Mara."

    "Elle s'arrête alors qu'elle allait repartir."

    mara neutre "Hm ?"

    "Pendant une fraction de seconde, j'ai envie de lui demander quelque chose que seule la vraie Mara pourrait savoir."

    "Puis je me rappelle qu'elle connaissait cet après-midi des souvenirs que moi-même j'avais oubliés."

    "Je n'ai aucune question magique."

    noam fatigue "Rien."

    mara taquin "Solide conversation."

    noam sourire "Bonne nuit."

    mara sourire "Bonne nuit, cerveau normal."

    "Elle reprend sa route."

    "Je la regarde s'éloigner jusqu'au bout du couloir."

    "Sa démarche est celle de Mara."

    "Sa voix est celle de Mara."

    "Son humour, ses souvenirs, sa manière de tourner la tête quand elle me répond : tout est exactement à sa place."

    "Et derrière un mur, dans une salle que presque personne ne connaît, il y a un corps avec le même visage."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_chambre") from _call_j25_door_5
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Je ferme la porte et reste quelques secondes la main sur la poignée."

    "Sur ma table, le dossier dans lequel j'ai caché le morceau de tissu paraît complètement banal."

    "Je l'ouvre malgré moi et vérifie qu'il est toujours là."

    "Brun. Déchiré. Réel."

    think "Demain."

    "Je regarde la caméra au-dessus de la porte."

    "Pour la première fois depuis le début du Conclave, l'idée d'être surveillé ne me donne pas envie de détourner les yeux."

    "Au contraire."

    think "Si je parle, il faut que tout le monde entende."

    "Je referme le dossier."

    "Je ne sais pas encore comment je vais le dire, ni ce qui se passera après."

    "Mais je sais déjà que je ne pourrai pas garder ça enfermé beaucoup plus longtemps."

    stop music fadeout 1.5

    call end_day("26", sleeping=True) from _call_j25_stay_end_day_26
    jump _26_0_1_1_0_0_REVEIL

    # Durée estimée : ~25-30 minutes
