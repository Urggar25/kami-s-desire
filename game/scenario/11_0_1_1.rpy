label _11_0_1_1_REVEIL_CHAMBRE:

    play music "music/bgm_romantic_atmosphere.mp3" fadein 2.5
    play sound sfx_heartbeat fadeout 3.0  # résidu du malaise
    
    "Je sens une sensation humide et fraîche sur mon front."
    "J’ouvre les yeux difficilement. La lumière me brûle un peu."
    
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)
    
    iris "Ah bah enfin ! Monsieur daigne se réveiller."
    iris "T’as mis le temps, hein. J’ai cru que t’allais commencer ton hibernation."

    scene bg_cg031 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg031")
    
    "Elle retire rapidement sa main de mon front."
    "Sa tête était posée contre le bord du matelas. Elle a clairement passé une partie de la nuit ici."
    
    noam faible "Iris… ?"
    noam "Qu’est-ce qui s’est passé… ?"
    
    iris "Ce qui s’est passé ? Tu t’es écroulé comme une merde pendant le débat, voilà ce qui s’est passé !"
    iris "Un instant t’étais debout à poser des questions bizarres, et la seconde d’après : bam, par terre."
    iris "On a tous flippé, espèce d’idiot."
    
    "Elle trempe un nouveau linge dans l’eau fraîche, l’essore un peu trop fort, et me le repose sur le front avec une douceur qui contraste avec son ton."
    
    iris "T’as fait une fièvre de cheval toute la nuit. Genre 39.5. On s’est relayés à ton chevet, parce que bien sûr, faudrait pas que le seul mec un minimum sensé de la bande y passe."
    iris "Mara a grogné mais elle est restée deux heures, Sael a fait le médecin de campagne, même Kael est venu… Bref, tout le monde y est passé."
    
    iris desaccord "Et Ryn a juste dit « Dis-lui de pas crever, on a déjà assez de merdes comme ça ». C’est sa façon à lui de s’inquiéter, j’imagine."
    
    "Elle croise les bras et détourne légèrement le regard, les joues un peu rouges."
    
    iris "… Bref. T’as intérêt à te remettre vite fait. Parce que si tu nous refais un coup pareil, je te jure que je te laisserai crever la prochaine fois."
    iris "C’est clair ?"
    
    noam "… Merci d’avoir veillé sur moi."
    
    iris "C’est pas comme si j’avais eu le choix ! Ils m’ont tous forcée."
    iris "Et puis… c’est pas comme si je pouvais te laisser délirer dans ton coin."
    iris "Qu'est ce qu'on aurait fait si tu avais pété un cable, hein ?"
    
    "Elle marmonne dans sa barbe, mais sa main reste près de mon épaule."
    
    iris "Allez, bois ça."
    
    "Elle me tend un verre d’eau avec un geste un peu sec, mais elle attend que je le prenne bien avant de lâcher."
    
    iris "Et arrête de faire cette tête de chien battu. T’as juste trop stressé, eu trop chaud, et t’as accumulé de la fatigue."
    iris "Sael a dit que c'était probablement pas à cause d'une bactérie."
    
    "Elle reste un moment silencieuse, le regard un peu perdu dans le vide."
    
    menu:
        "Lui demander si elle sait ce que j’ai vu avant l’annonce":
            jump noam_parle_doppelganger_iris
        "Garder ça pour moi pour l’instant":
            jump noam_garde_secret
            
label noam_parle_doppelganger_iris:

    play music "music/bgm_system_override.mp3" fadein 2.5
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)

    $ showGroup([
        ("noam", "fatigue", 0.20),
        ("iris", "inquiet", 0.80),
    ])

    noam hesitation "Iris… avant de m’écrouler… j’ai vu quelque chose de bizarre."
    noam inquiet "Juste avant l’annonce de Kami. Dans le couloir, vers la salle de stockage."

    "Iris fronce les sourcils. Son expression change du tout au tout."

    iris inquiet "De bizarre comment ?"

    noam reflexion "Une silhouette… au loin. Je sais pas trop."
    noam peur "C’était flou, mais… ça m’a mis mal à l’aise."

    iris desaccord "Noam… t’avais déjà la tête qui tournait pendant le débat."
    iris reflexion "T’as probablement vu un reflet, ou quelqu’un qui passait, ou juste rien du tout. Avec la fièvre que t’as eue, c’est normal."

    "Elle croise les bras, mais son regard reste fixé sur moi, plus attentif qu’elle ne veut le laisser paraître."

    iris inquiet "En plus, hier soir t’as demandé à tout le monde s’ils étaient dans les couloirs. Personne n’a rien vu."

    noam fatigue "Ouais… t’as sûrement raison."
    noam hesitation "C’est juste que… sur le moment, j’étais persuadé que c’était pas normal."

    "Iris reste silencieuse quelques secondes. Elle semble hésiter à dire quelque chose, puis finit par soupirer."

    iris fatigue "Écoute… t’es encore crevé, t’as la tête dans le brouillard, et on vient tous de vivre une soirée de merde."
    iris desaccord "C’est pas étonnant que ton cerveau te joue des tours."
    iris determine "Arrête de te prendre la tête avec ça pour l’instant, d’accord ?"

    "Elle pose à nouveau le linge frais sur mon front, un peu plus doucement que nécessaire."

    iris gene "Si tu continues à cogiter comme ça, tu vas te refaire de la fièvre pour rien."
    iris inquiet "Et j’ai pas envie de repasser la nuit à te surveiller, compris ?"

    "Malgré son ton râleur, elle ne bouge pas tout de suite. Son regard s’attarde un peu trop longtemps sur moi."

    iris hesitation "… Si jamais tu revois un truc qui te semble vraiment pas normal, tu m’en parles à moi. Pas aux autres."
    iris determine "Pour l’instant, repose-toi. C’est tout ce que t’as à faire."

    "Elle se lève lentement, comme si elle n’était pas vraiment convaincue par ses propres paroles."

    iris fatigue "Je vais te chercher quelque chose à manger. Bouge pas de là."

    "Avant de sortir, elle s’arrête un instant dans l’encadrement de la porte, le dos tourné."

    iris gene "Et arrête de faire cette tête. Ça me stresse."

    jump _11_0_1_1_APRES_REVEIL


label noam_garde_secret:

    play music "music/bgm_system_override.mp3" fadein 2.5
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)

    $ showGroup([
        ("noam", "fatigue", 0.20),
        ("iris", "inquiet", 0.80),
    ])

    "Je reste silencieux un moment. Les mots restent bloqués dans ma gorge."

    noam hesitation "... Non, rien."
    noam culpabilite "C'est rien d'important."

    "Iris plisse les yeux. Elle me fixe un peu trop longtemps, comme si elle sentait que je lui cachais quelque chose."

    iris desaccord "T'es sûr ? T'as l'air d'avoir quelque chose sur le bout de la langue."

    noam fatigue "Ouais... juste un rêve bizarre à cause de la fièvre. Laisse tomber."

    "Elle reste silencieuse quelques secondes, visiblement pas convaincue, puis finit par hausser les épaules."

    iris reflexion "Si tu le dis."
    iris desaccord "De toute façon, t'es encore à moitié dans les vapes. Pas la peine d'essayer de te faire cracher le morceau maintenant."

    "Elle attrape le linge, le trempe à nouveau dans l'eau fraîche et me le repose sur le front un peu brusquement."

    iris determine "T'as intérêt à te reposer correctement, compris ?"
    iris colere "Si tu te refais un malaise parce que tu stresses pour des conneries, je te jure que je te colle une baffe."

    "Malgré son ton sec, elle ajuste le drap sur moi."

    iris fatigue "Je vais te chercher quelque chose à manger à la cafétéria. Bouge pas de ce lit, hein."
    iris taquin "Et si tu vomis pendant mon absence, je te fais nettoyer toi-même."

    "Elle se dirige vers la porte, puis s'arrête un instant sans se retourner."

    iris gene "… Et arrête de cogiter. T'as une sale tête quand tu fais ça."

    "Elle marmonne quelque chose d'inaudible en sortant."

    jump _11_0_1_1_APRES_REVEIL

label _11_0_1_1_APRES_REVEIL:

    scene bg_chambre at adaptive_fullscreen
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    
    "Le silence revient dans la chambre après le départ d’Iris."
    "Je reste allongé, les yeux fixés au plafond. Ma tête tourne encore un peu."

    think "Une silhouette… juste une silhouette…"
    think "C’était loin. Flou. Ça ne veut rien dire."
    think "C’était forcément quelqu’un d’autre. Forcément."

    noam "… C’était rien."

    "Je murmure ces mots tout bas, presque pour moi-même."

    think "Je ne vais pas commencer à me monter la tête avec ça. Pas maintenant."
    think "C’est la fièvre. Juste la fièvre et la fatigue."

    pause 2.5

    "Quelques minutes plus tard, la porte s’ouvre à nouveau."

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("iris", "neutre", 0.40),
        ("sael", "neutre", 0.60),
        ("julian", "neutre", 0.80),
        ("nyra", "neutre", 1.00),
    ])

    iris "Voilà, je vous l’avais dit. Il est réveillé et il est déjà en train de se creuser la tête avec des conneries."

    sael "On s’est dit qu’on allait pas te laisser manger tout seul comme un gosse abandonné."

    julian taquin "Exactement ! Faut bien quelqu’un pour t’empêcher de refaire ton grand show dramatique."
    julian "Franchement Noam, si tu voulais prendre la vedette pendant le débat, y’avait des façons plus discrètes que de t’évanouir d’un coup."

    "Julian pose un plateau bien garni sur la table de chevet avec un sourire moqueur. Nyra reste un peu en retrait, calme comme toujours."

    nyra "On t’a pris des portions légères. Quoi que pas tant que ça en fait. Tu as du riz, du poulet et des légumes. Rien qui risque de te retourner l’estomac et tout pour te redonner des forces."

    "Ils s’installent autour du lit : Iris s’assoit au bord, Sael prend la chaise, Julian reste debout, Nyra s’adosse au mur."

    "Je commence à manger lentement, sans grand appétit."

    think "Ils sont tous là, normaux… comme si rien ne s’était passé."
    think "Et moi je suis là, à me repasser en boucle cette putain d'ombre que j'ai cru voir dans le couloir."
    think "Mais non. C’était rien. Juste une silhouette. Rien de plus."

    iris "T’as repris un peu de couleurs, c’est déjà ça."
    iris "Mange correctement hein, sinon je vais devoir te forcer."

    julian taquin "Ouais, reprends des forces. On a besoin de toi en pleine forme pour la prochaine connerie que Kami va nous sortir."

    "Le repas se déroule dans une ambiance plutôt légère. Ils parlent du vote d’hier, de la chaleur, de tout et de rien. Je ris à leurs blagues, mais mon esprit reste ailleurs."

    think "C’était forcément quelqu’un d’autre."
    think "Arrête de penser à ça."

    "Je force un sourire et continue à manger en silence tandis que le groupe parle de tout et de rien."


    call show_custom_title("Une bonne heure plus tard")

    pause 1.5

    scene bg_couloir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("iris", "neutre", 0.40),
        ("sael", "neutre", 0.60),
        ("julian", "neutre", 0.80),
        ("nyra", "neutre", 1.00),
    ])


    "Le repas touche à sa fin. Je me sens un peu mieux, mais chaque mouvement me rappelle que mon corps n’a pas encore tout à fait récupéré."

    think "J’ai l’impression d’être en verre. Un faux mouvement et je me brise à nouveau."

    iris "Bon, t’as fini de jouer avec ta nourriture ?"
    iris "Tu tiens debout ou on doit encore te traîner comme un sac ?"

    julian taquin "Moi je vote pour une petite balade. Rester couché toute la journée va te ramollir le cerveau."

    sael "J'ai une idée Noam, je vais t'emmener à la salle d’observation. Il y a une meilleure ventilation en ce moment."
    sael "Il fera moins chaud qu'ici, même si c'est déjà beaucoup plus supportable qu'ici..."

    nyra "Tant qu’il ne force pas."

    "Je me lève lentement. Mes jambes tremblent légèrement, mais je serre les dents et commence à avancer."

    $ hideGroup()
    scene bg_couloir at adaptive_fullscreen with dissolve

    "Je les suis et je marche un peu en retrait, légèrement étourdi."
    "Au bout d’un moment, nous arrivons devant la salle d’observation. La porte est entrouverte."
    "On entend la voix de Kami à l’intérieur."

    stop music fadeout 1.0

    play music "music/bgm_system_override.mp3" fadein 2.0

    kami "Je suis désolée Kael, mais c’est bien plus compliqué que ça."

    "Nous nous arrêtons instinctivement. Sael me fait signe de rester silencieux."

    scene bg_observation at adaptive_fullscreen with dissolve

    $ showGroup([
        ("kael", "neutre", 0.50),
    ])

    kael "Sept jours ? Tu es sérieuse ?"
    kael colere "J'ai vraiment besoin de ces images !"

    kami "Les brouilleurs actuellement en circulation sont particulièrement efficaces."
    kami "Ils ne se contentent pas de bloquer le signal en temps réel."
    kami "Ils appliquent un filtre de sept jours sur toutes les données vidéo et audio enregistrées dans leur rayon lorsqu'ils sont allumés."
    kami "C’est une sécurité intégrée. Même moi, je ne peux pas contourner ça instantanément."

    kael triste "Donc si je comprends bien… même si le vote autorise les brouilleurs, ça ne changera rien pour moi avant sept jours ?"

    kami "Exactement. Et si vous votez pour les interdire… eh bien, tu n’auras plus jamais accès à ces enregistrements."
    kami "Quel choix intéréssant, n’est-ce pas ?"

    "Kael reste silencieux. Ses poings sont serrés."

    think "Il cherche encore la photo de sa soeur ?"
    think "Il n’abandonne toujours pas."

    "Je sens un vertige me reprendre. Je m’appuie discrètement contre le mur."

    sael inquiet "Noam ? Ça va ?"

    "Le groupe se tourne vers moi. Kael remarque enfin notre présence et sursaute légèrement."

    kael calme "... Vous étiez là."

    pause 1.0

    $ showGroup([
        ("noam", "neutre", 0.20),
        ("iris", "neutre", 0.40),
        ("sael", "neutre", 0.60),
        ("julian", "neutre", 0.80),
        ("nyra", "neutre", 1.00),
        ("kael", "neutre", 1.20),
    ])

    julian taquin "On passait juste. On voulait pas déranger ton… entretien privé avec notre chère geôlière."

    kami "Oh ! Mais vous ne dérangez rien du tout !"
    kami "D’ailleurs, Noam, tu as meilleure mine. J’ai eu peur que ce soit plus grave qu'un simple malaise."

    "Sa voix est douce, presque mielleuse."

    noam fatigue "Ouais... Je vais bien…"

    kael colere "… Laisse tomber. On en reparlera plus tard, Kami."

    "Kael sort de la pièce sans un mot de plus. Son regard croise le mien une fraction de seconde. Il a l’air épuisé."

    hide kael with dissolve

    iris inquiet "T’as vu sa tête ? Il est de plus en plus obsédé par sa photo non ?"

    sael reflexion "On peut le comprendre…"
    sael reflexion "Qu'est ce que tu ferais si ce que tu avais de plus précieux avait été piqué par on ne sait qui ?"

    nyra "..."
    nyra taquin "C'est même étonnant qu'il soit aussi calme."

    "Je sens à nouveau ma tête tourner. Je ferme les yeux une seconde."

    noam fatigue "Je… j’ai besoin de m’asseoir un moment."

    "Iris me prend immédiatement le bras."

    iris triste "Évidemment qu’il a besoin de s’asseoir, il est encore à moitié mort !"
    iris determine "On va aller se poser à la salle commune."

    think "Encore marcher ? Non. J'en peux plus."

    noam "Allez-y sans moi, je vais retourner me reposer un peu."
    noam sourire "Merci de m'avoir tenu compagnie."

    nyra "T'es sûr que ça va aller ?"
    nyra "Tu veux qu'on t'accompagne ?"

    noam "Non ça va aller, c'est juste à côté."
    noam "Allez profiter un peu avant la journée de demain."

    iris "Si c'est ce que Monsieur veut. Il ne faut pas le dire deux fois."

    "Iris s'éloigne rapidement en grimaçant."
    "Le groupe se dissout et je retourne me poser dans ma chambre."

    jump _11_0_1_2_CHAMBRE_INTROSPECTION

label _11_0_1_2_CHAMBRE_INTROSPECTION:

    scene bg_chambre at adaptive_fullscreen with dissolve
    stop music fadeout 1.0  # pour laisser un silence lourd au début

    "À peine arrivé dans ma chambre, je m’effondre sur le lit sans même enlever mes chaussures."
    "Mon corps est lourd. La tête tourne encore un peu par moments."

    "Je fixe le plafond blanc, la respiration un peu saccadée."

    think "Je n’en peux plus de cette fatigue… On dirait qu’elle est incrustée dans mes os."
    think "Et pourtant, je n’arrive pas à fermer les yeux."
    think "Impossible de me reposer vraiment."

    pause 1.8

    think "Cette silhouette… Ce n’était pas rien."
    think "J’ai beau me répéter que c’était la fièvre, la chaleur, le stress… quelque chose au fond de moi refuse d’y croire."

    "Je passe une main sur mon visage. Ma peau est encore chaude."

    noam "Et mon état s'arrange pas..."

    think "Kael cherchait des images de sa chambre… il n'a pas pu y accéder à cause du brouilleur."
    think "Sept jours de délai."
    think "Mais Kami… elle voit tout. Elle est au-dessus de tout ça."

    think "Sept jours de délai à cause des brouilleurs ?"
    think "À cause des brouilleurs..."

    call _11_0_1_2_MINIJEU_7JOURS

    play music "music/bgm_low_tension.mp3" fadein 2.0
    "Je reste immobile plusieurs secondes. Plus je me répète ces quelques mots, plus une idée me frappe, claire et presque trop évidente."

    think "... Et si je lui demandais directement ?"
    think "Si je lui demandais de me montrer les caméras du couloir d’hier soir ?"

    think "Parce qu'il n'y a PAS DE BROUILLEUR dans les couloirs !"
    
    noam "Donc les images sont accessibles ?!"

    "Mon cœur s’accélère un peu. L’idée est simple. Probablement stupide."
    "Mais rester ici à tourner en rond dans ma tête l’est encore plus."

    noam "... Je dois savoir."
    noam "Elle refusera... Mais... Qui ne tente rien n'a rien, non ?"

    "Je me redresse brusquement. Trop brusquement."

    think "Il faut que je sache si ce que j'ai vu est vrai."
    think "Et si ce n’était pas rien…"

    "Je serre les poings."

    noam "Alors je veux en avoir le coeur net."

    "Je me relève, encore un peu instable sur mes jambes, et me dirige vers la porte."

    jump _11_0_1_3_SALLE_COMMUNICATION

label _11_0_1_3_SALLE_COMMUNICATION:

    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0

    "La salle d'observation est plongée dans une lumière bleue froide. Les grands écrans sont tous allumés, mais sans image."

    noam "Kami ? Tu es là ?"

    pause 1.0

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh ? Noam ? Je suis toujours là voyons."
    kami "Tu devrais être en train de te reposer, mon petit bout de chou. Tu étais pourtant dans un sale état tout à l’heure."

    "Sa voix douce résonne dans toute la pièce, presque maternelle."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ne me dis pas que tu as déjà repris du poil de la bête ? Comme c’est mignon."

    $ bc_show("noam", "hesitation", px=-70, py=-50, pz=0.85)
    noam hesitation "J’ai une question à te poser."
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je t’écoute. Pose ta question, je suis toute ouïe."

    $ bc_show("noam", "hesitation", px=-70, py=-50, pz=0.85)
    noam "Hier soir. Juste avant l’annonce. Le couloir près de la salle de stockage."
    noam "Est-ce que tu peux me montrer les enregistrements des caméras de cette zone ?"
    $ bc_hide()

    "Un long silence. Les écrans clignotent légèrement."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Hmm… Intéressant."
    kami "C'est ce que tu as cru voir qui te fait venir me demander ça ?."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais bon… Je ne voudrais pas que le représentant d'Harmonie devienne totalement fou."
    kami "Que vont en penser ta famille sinon ?!"

    "Je ravale douloureusement ma salive."

    think "Pourquoi elle parle de ma famille tout à coup ?!"
    think "Je fais si pitié à voir ?!"

    "..."

    think "Non ressaisis toi Noam. Te laisse pas berner."

    $ bc_show("noam", "colere", px=-70, py=-50, pz=0.85)
    noam "Je veux voir ces images."
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oh mais quelle assurance !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "J'aime ce tact !"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Alors soit, tu peux accéder aux images de surveillance depuis un des ordinateurs."
    kami "Je te débloque les accès."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Enfin, si tu sais t'en servir !"

    scene bg_observation at adaptive_fullscreen with dissolve

    "Les écrans des ordinateurs s’allument d’un coup."
    "Il y a plusieurs tranches horaires et plusieurs salles disponibles."
    "Il va falloir que je trouve le segment que je cherche..."

    call _11_0_1_3_MINIJEU_CAMERAS

label _11_0_1_1_CONFRONTATION_KAMI:

    scene bg_observation at adaptive_fullscreen with dissolve

    "Je sélectionne enfin la bonne combinaison."
    "L’écran s’allume… puis devient noir en une fraction de seconde."
    "\"Données supprimées - Accès impossible\""

    $ bc_show("noam", "colere2", px=-70, py=-50, pz=0.85)
    noam colere "C’est quoi cette putain de blague ?!"
    noam colere "Kami ! Sors de là !"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ohhh~ Quel cri du cœur ! Tu m’as presque fait sursauter !"
    kami "Tu sais que quand tu t’énerves comme ça, tu deviens presque mignon ?"

    $ bc_show("noam", "colere", px=-70, py=-50, pz=0.85)
    noam colere "Arrête tes conneries ! Pourquoi les images ont disparu ?!"
    noam colere "Tu m’as dit que tu me donnais l'accès aux vidéos !"
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je t’ai donné accès aux archives, oui. Ce n’est pas ma faute si quelqu’un a fait le ménage avant toi."
    kami "Et franchement… chapeau. C’était du travail très propre. Même moi je suis un peu jalouse."

    think "Quelqu'un a vraiment fait ça ?"
    think "Ou elle essaie juste de me faire perdre du temps ?"

    $ bc_show("noam", "colere2", px=-70, py=-50, pz=0.85)
    noam colere "Tu mens ! Tu mens forcément !"
    noam colere "Montre-moi les images ! Tout de suite !"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Houlà, du calme, monsieur l’inspecteur. On se croirait dans un épisode de Brooklyn Nine-Nine, l'humour en moins cela dit."
    kami "Je ne suis pas responsable de cette suppression, mon cœur. Parole de Kami."
    kami "Quelqu’un d’autre a appuyé sur le petit bouton « effacer »."

    $ bc_show("noam", "colere", px=-70, py=-50, pz=0.85)
    noam colere "Et tu vas me faire croire que tu ne sais pas qui c’est ?!"
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je n’ai pas dit ça~"
    kami "J’ai juste dit que je n’étais pas responsable."
    kami "Mais entre nous… la personne qui a fait ça est parmi vous."

    think "Parmi nous..."
    think "Non."
    think "Impossible."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Qui ça peut bien être ? Et pourquoi se donner cette peine ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oui oui, parmi tes charmants petits camarades. Celle ou celui qui te sourit tous les jours."
    kami "Celle ou celui qui vote avec toi, qui mange avec toi, qui fait semblant de s’inquiéter pour toi."
    kami "N’est-ce pas excitant ?"

    think "Elle essaie de me retourner contre eux."
    think "C'est forcément ça."

    $ bc_show("noam", "peur", px=-70, py=-50, pz=0.85)
    noam peur "... Tu mens."
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je mens ? Moi ? Jamais."
    kami "Je suis une IA honnête, tu sais. Un peu sadique, certes, mais honnête et adoraaable."

    $ bc_show("noam", "colere2", px=-70, py=-50, pz=0.85)
    noam colere "Arrête de jouer avec moi !"
    noam colere "Dis-moi qui c’est !"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et où serait le plaisir si je te le disais directement ?"
    kami "Ce serait comme te spoiler la fin d’un bon thriller. Non, non."
    kami "Je préfère te regarder te torturer tout seul. C’est bien plus divertissant."
    kami "Et puis le règlement m'interdit de te le dire. Je n'interviens dans aucune de vos manigances."

    $ bc_show("noam", "colere", px=-70, py=-50, pz=0.85)
    noam colere "Tu prends ton pied avec ça, hein ?"
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Énormément."
    kami "Imagine… quelqu’un qui te connaît si bien qu’il arrive à effacer des preuves sous mes propres caméras."
    kami "C’est presque romantique, non ? Comme un admirateur secret qui veut rester dans l’ombre."

    think "Arrête."
    think "Arrête de parler comme si tout ça était un jeu."

    $ bc_show("noam", "fatigue", px=-70, py=-50, pz=0.85)
    noam fatigue "… Pourquoi tu fais ça ?"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Parce que c’est drôle."
    kami "Parce que vous êtes tous si prévisibles… Disons que ça brise la routine."
    kami "Et surtout parce que je veux voir jusqu’où tu es prêt à aller pour découvrir la vérité."
    kami "Tu vas commencer à soupçonner tout le monde maintenant ? Iris ? Sael ? Julian ?"
    kami "Ou peut-être… ce que tu as vu ?"

    $ bc_show("noam", "peur", px=-70, py=-50, pz=0.85)
    noam peur "… Tais-toi."
    $ bc_hide()

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Oh ? Touché ?"
    kami "Allez, Noam. Va les observer. Va leur poser des questions innocentes."
    kami "Regarde-les dans les yeux et demande-toi : lequel d’entre eux est capable de se faire passer pour toi ?"
    kami "Ce petit jeu va être TELLEMENT amusant."

    $ bc_show("noam", "colere2", px=-70, py=-50, pz=0.85)
    noam colere "Je te déteste."
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je sais. Mais je t'aime quand même."
    kami "Maintenant va te reposer, mon petit détective en herbe."
    kami "Tu as une sale tête. Et demain, il y a un vote très important."
    kami "Ce serait dommage que tu t’évanouisses encore… n’est-ce pas ?"

    "Je reste silencieux un long moment, les poings serrés."

    think "Elle joue avec moi… Elle s’amuse."
    think "Elle ne fait que ça..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh, et Noam ?"
    kami "N'oublie pas de trouver qui c'est. Tu trouveras sans doute plus qu'une seule réponse."

    $ bc_show("noam", "colere", px=-70, py=-50, pz=0.85)
    noam colere "... Va te faire foutre."
    $ bc_hide()

    "Je tourne les talons et sors de la salle sans un regard en arrière."
    "Le rire doux et cristallin de Kami me suit dans le couloir."

    think "Elle joue avec moi..."
    think "Elle ne fait que ça..."
    think "Et pourtant..."
    think "Pourquoi est-ce que j'ai l'impression qu'elle dit la vérité ?"

    stop music fadeout 2.0

    jump _11_0_1_1_RETOUR_CHAMBRE

label _11_0_1_1_RETOUR_CHAMBRE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.bgm" fadein 3.0

    "Je sors de la salle d’observation sans un regard en arrière."
    "Mes jambes sont lourdes. Chaque pas résonne dans ma tête comme un marteau."

    think "Je ne veux voir personne."
    think "Ni Iris, ni Sael, ni Julian… personne."

    "Je marche droit vers ma chambre, ignorant les voix lointaines qui proviennent de la salle commune."

    scene bg_chambre at adaptive_fullscreen with fade

    "À peine la porte refermée, je m’adosse contre elle un instant, les yeux fermés."

    noam "..."

    "Le silence de la chambre m’enveloppe. Enfin."

    "Je me traîne jusqu’au lit et m’y laisse tomber lourdement, tout habillé."

    think "Je veux juste dormir."
    think "Oublier cette journée. Oublier cette silhouette. Oublier ce qu’a dit Kami."

    pause 1.5

    think "Mais je n’y arrive pas."

    "Je fixe le plafond. Les mots de Kami tournent en boucle dans ma tête."

    think "« La personne qui a effacé ces images… elle est parmi vous. »"

    noam "... Arrête."

    think "C’est impossible. Aucun d’entre eux ne ferait ça."
    think "Iris ? Elle était avec moi presque tout le temps."
    think "Sael ? Elle m’a aidé quand je me suis écroulé."
    think "Julian ? Il passe son temps à faire des blagues débiles…"
    think "Nyra ? Tomas ? Mara ?"

    "Je me retourne dans le lit, nerveux."

    think "Ils étaient tous là. Ils se sont inquiétés pour moi."
    think "Pourquoi l’un d’eux irait jusqu’à supprimer des preuves ?"

    "Je serre les draps entre mes doigts."

    think "Kami ment. Elle ment forcément. Elle adore nous manipuler."
    think "C’est son jeu préféré."

    pause 2.0

    think "... Et si elle ne mentait pas ?"

    "Cette pensée me glace."

    think "Si c’est vraiment l’un d’eux…"
    think "Alors tout ce qu’on a vécu ensemble, tous ces moments, tous ces votes…"
    think "… n’était que du vent ?"

    "Je ferme les yeux de toutes mes forces, comme si ça pouvait chasser les images."

    noam faible "… Je veux juste dormir."

    "Mais le sommeil ne vient pas. Seulement un tourbillon de visages, de soupçons, et cette silhouette qui me ressemble parfaitement."

    think "Parmi nous…"
    think "Quelqu’un m’a regardé dans les yeux aujourd’hui… et a effacé les preuves."

    "Je me retourne encore une fois, le cœur serré."

    think "Je ne veux pas y croire."
    think "Je refuse d’y croire."

    "Pourtant, au fond de moi, quelque chose s’est déjà fissuré."

    pause 3.0

    "Finalement, l’épuisement prend le dessus. Mes paupières deviennent trop lourdes."

    $ blink()
    think "Demain… je réfléchirai demain."

    "Ou peut-être que je continuerai juste à mentir à moi-même."

    scene black with fade
    stop music fadeout 4.0

    call end_day("12")
    jump _12_0_1_1_REVEIL_CHAMBRE