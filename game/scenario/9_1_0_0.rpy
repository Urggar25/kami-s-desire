label _9_1_0_0_REVEIL:

    $ current_day = 9
    $ current_period = "Matin"

    scene black with fade
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    play sound sfx_announce
    pause 1.0

    kami "Debout, mes chers représentants ! Une nouvelle journée commence, et comme toujours, je compte sur vous pour ne pas la gâcher trop vite."
    kami "Je sais que certains d'entre vous auraient préféré dormir encore un peu, mais le monde ne va malheureusement pas attendre que vous soyez de bonne humeur."

    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 2.5)

    "J'ouvre les yeux en grimaçant légèrement, encore à moitié enfoui dans l'oreiller. Pendant quelques secondes, je reste immobile à écouter la voix de Kami résonner dans la chambre, jusqu'à ce que les souvenirs de la veille finissent par revenir d'un seul coup."

    think "Ryn qui sort de la chambre d'Iris... et cette façon parfaitement normale qu'il avait de me souhaiter bonne nuit, comme s'il n'y avait absolument rien d'étrange à sa présence là-bas."
    think "Je devais en parler à Nyra dès ce matin. Autant le faire avant que la journée commence vraiment."

    "Je me redresse, m'habille rapidement et quitte la chambre sans même prendre le temps de traîner comme d'habitude."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Le couloir est encore relativement calme. Quelques portes commencent à s'ouvrir au loin, mais la plupart des représentants ne sont visiblement pas encore sortis."
    "Je vais directement jusqu'à la chambre de Nyra et frappe deux fois contre la porte."

    noam reflexion "Nyra ? C'est moi."

    "J'attends quelques secondes, puis frappe une nouvelle fois. Rien ne bouge à l'intérieur."

    noam hesitation "Nyra ?"

    think "Elle est déjà partie ?"

    "Je reste encore un instant devant la porte avant de regarder machinalement vers le bout du couloir. Si elle s'est levée avant moi, il y a de fortes chances qu'elle soit déjà partie manger."

    noam reflexion "Bon... cafétéria."

    jump _9_1_0_0_CAFETERIA_MATIN


label _9_1_0_0_CAFETERIA_MATIN:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_cafeteria.mp3" fadein 2.0

    "La cafétéria est déjà plus animée que le couloir. Plusieurs représentants sont installés autour des tables et discutent tranquillement pendant que d'autres récupèrent leur petit-déjeuner."
    "Je parcours rapidement la pièce du regard, mais Nyra n'est pas là non plus."

    think "Super. Elle a décidé de devenir introuvable précisément le matin où j'ai besoin d'elle."

    "Je m'avance quand même entre les tables, au cas où elle serait simplement cachée derrière quelqu'un, mais je m'arrête presque aussitôt en apercevant Ryn près de la sortie."

    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("ryn", "neutre", 0.70),
    ])

    noam reflexion "Ryn."

    "Il tourne la tête vers moi et s'immobilise une fraction de seconde. Son visage ne trahit rien de particulier, mais je remarque immédiatement qu'il ne fait aucun effort pour venir vers moi."

    ryn reflexion "Noam."

    noam hesitation "Je voulais te parler deux minutes à propos d'hier soir."

    "Son regard se détourne presque aussitôt."

    ryn neutre "Pas maintenant."

    noam surpris "Pas maintenant ?"

    ryn reflexion "J'ai quelque chose à faire. On verra plus tard."

    "Il reprend sa marche avant même que j'aie le temps de répondre. Ce n'est pas franchement une fuite, il ne se met pas à courir et ne cherche pas à se cacher, mais la façon dont il abrège la conversation est suffisamment inhabituelle pour que je reste quelques secondes à le regarder s'éloigner."

    think "D'accord... donc je ne me faisais pas complètement des idées hier soir."
    think "Il sait que je l'ai vu, et il n'a visiblement aucune envie d'en parler."

    $ hideGroup()

    "Je m'apprête à repartir quand Tomas arrive près du comptoir avec plusieurs portions dans les mains. Beaucoup trop pour une seule personne."

    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("tomas", "neutre", 0.70),
    ])

    noam taquin "Tu comptes nourrir tout le couloir avec ça ?"

    tomas surpris "Hm ?"

    "Il baisse les yeux vers ce qu'il transporte avant de relever la tête avec un calme presque trop naturel."

    tomas sourire "J'avais faim."

    noam desaccord "À ce niveau-là, c'est plus de la faim."

    tomas reflexion "J'anticipe."

    "Je retiens un sourire. Il ne sert à rien de lui demander pour qui sont réellement ces portions, et il le sait aussi bien que moi."

    noam reflexion "Tu as vu Nyra ce matin ?"

    tomas "Non. Pas encore."

    noam "D'accord."

    tomas inquiet "Quelque chose ne va pas ?"

    "Je jette un rapide coup d'œil vers la porte par laquelle Ryn vient de disparaître."

    noam reflexion "Rien d'urgent. J'ai juste besoin de lui parler."

    tomas "Elle finira bien par passer."

    noam "Ouais."

    "Tomas me salue rapidement avant de quitter la cafétéria avec ses portions. Je le regarde partir quelques secondes en imaginant sans difficulté la destination de la moitié de son plateau."

    think "Au moins, Anya ne risque pas de manquer de nourriture."
    think "Pour Nyra, j'attendrai. Avec le débat de cet après-midi, elle sera forcément là."

    $ hideGroup()

    jump _9_1_0_0_DEBAT


label _9_1_0_0_DEBAT:

    call MAYBE_PLAY_SCRIPTED_DOOR("conclave", "bg_conclave")
    $ current_period = "Après-midi"

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_debate.mp3" fadein 2.5

    "Comme prévu, Kami nous convoque dans la salle du Conclave en début d'après-midi. Contrairement aux derniers débats, personne ne semble particulièrement tendu et la plupart des représentants prennent place en continuant tranquillement leurs conversations."

    "Le sujet du vote apparaît sur l'écran principal."

    centered "{b}Autoriser les regroupements de plus de vingt personnes.{/b}"

    "Quelques secondes passent sans que personne ne se précipite pour parler. Ce n'est pas vraiment de l'hésitation ; j'ai plutôt l'impression que tout le monde cherche ce qu'il pourrait bien y avoir à contester."

    kami "Eh bien ? Je vous écoute."
    kami "Je m'attendais au moins à une grande tirade sur le danger terrifiant que représente un groupe de vingt-et-une personnes réunies au même endroit."

    pause 0.8

    kami "Rien ? Vous me décevez."

    $ showGroup([
        ("elen", "joie", 0.20),
        ("julian", "neutre", 0.40),
        ("mara", "neutre", 0.60),
        ("tomas", "neutre", 0.80),
        ("noam", "neutre", 1.00),
    ])

    elen joie "Mais c'est super ! Si on enlève cette interdiction, ça veut dire qu'on pourra enfin recommencer à organiser des festivals, des concerts, des fêtes... des vrais trucs avec du monde !"

    julian taquin "Je savais que quelqu'un finirait par trouver un enjeu vital à ce vote."

    elen colere "Tu rigoles, mais ça fait plus d'un an qu'il n'y a pratiquement plus rien ! À un moment, les gens ont aussi le droit de se retrouver sans avoir l'impression de préparer un coup d'État."

    mara reflexion "Sur le principe, je suis d'accord. Les districts peuvent toujours encadrer les grands événements eux-mêmes si nécessaire. Il n'y a aucune raison de maintenir une interdiction générale."

    tomas "Même avis. La règle actuelle est beaucoup trop large pour ce qu'elle est censée empêcher."

    "Je regarde rapidement autour de moi. Même ceux qui n'ont encore rien dit ne semblent pas chercher d'argument pour s'opposer au texte."

    noam reflexion "Je voterai pour aussi. On se regroupe déjà tous les jours à petite échelle et ça ne pose aucun problème. Je vois mal pourquoi vingt personnes seraient acceptables et vingt-et-une deviendraient soudain dangereuses."

    julian sourire "Voilà. Débat terminé. On peut rentrer ?"

    kami "Certainement pas, je viens à peine de commencer à m'amuser."

    "Quelques autres représentants prennent tout de même la parole pour évoquer les questions de sécurité, de responsabilité ou d'organisation dans les districts, mais la discussion reste étonnamment calme. Personne ne défend sérieusement le maintien de l'interdiction et, en moins de quelques minutes, le résultat semble déjà évident."

    elen joie "Franchement, si ça passe, je veux un concert avant la fin de l'année. Je m'en fiche de qui joue, je veux juste entendre autre chose que les annonces de Kami dans des haut-parleurs."

    kami "Je suis blessée."

    elen taquin "Tu survivras."

    kami "Probablement."

    "Un léger rire parcourt la salle. Pour une fois, l'ambiance ressemble presque à celle d'une réunion normale plutôt qu'à un affrontement où chacun attend que tout explose."

    $ hideGroup()

    "Le vote est lancé peu après et je sélectionne immédiatement POUR. Les autres réponses apparaissent les unes après les autres, sans véritable suspense."

    centered "{b}VOTE ADOPTÉ{/b}"

    "La mesure est adoptée rapidement et avec une majorité suffisamment nette pour qu'aucune discussion ne reparte derrière. Elen lève les deux bras avec un enthousiasme disproportionné."

    $ showGroup([
        ("elen", "joie", 0.30),
        ("julian", "taquin", 0.70),
    ])

    elen joie "OUI ! Enfin !"

    julian taquin "Tu sais que rien ne dit qu'un festival va apparaître demain matin juste parce qu'on a voté ça ?"

    elen "Je m'en fiche. Maintenant c'est possible, et c'est déjà largement mieux qu'hier."

    julian sourire "Je retire ce que j'ai dit. C'est effectivement historique."

    $ hideGroup()

    "Je m'attends à ce que Kami nous laisse partir, mais l'écran derrière elle change brusquement pour afficher une carte des districts et plusieurs images de zones de fret."

    stop music fadeout 1.0
    play music "music/bgm_system_override.mp3" fadein 2.0

    kami "Puisque j'ai votre attention, j'en profite pour faire une petite annonce qui, cette fois, concerne tout le monde."
    kami "Le retour du commerce entre les districts est une excellente nouvelle, mais il entraîne aussi une augmentation considérable du nombre de conteneurs en circulation. Et qui dit davantage de marchandises dit davantage de choses à vérifier."

    "Je me redresse légèrement sur mon siège. Le mot conteneur suffit à capter immédiatement mon attention."

    kami "De nouvelles missions rémunérées vont donc être créées dans l'ensemble des districts afin d'aider aux contrôles des zones de transit et à la vérification du contenu des marchandises."
    kami "Les citoyens volontaires pourront participer aux inspections et recevoir une rémunération en échange de leur travail. Pratique, utile, et surtout bien moins cher que de devoir mobiliser des équipes supplémentaires partout."

    "Autour de moi, plusieurs représentants hochent simplement la tête. L'annonce paraît logique, presque banale, et personne ne semble faire le même rapprochement que moi."

    think "Des contrôles supplémentaires sur les conteneurs... précisément maintenant."
    think "Si ce système avait existé quelques jours plus tôt, Anya n'aurait peut-être jamais réussi à entrer dans celui qui l'a amenée ici."

    kami "Les premières missions seront disponibles très prochainement. J'espère que les citoyens se montreront aussi motivés par la sécurité collective que par la perspective de gagner quelques crédits."

    "L'écran s'éteint enfin et Kami met officiellement fin à la séance. Les représentants commencent aussitôt à quitter la salle, mais cette fois je n'ai aucune intention de perdre Nyra de vue."

    jump _9_1_0_0_NYRA


label _9_1_0_0_NYRA:

    scene couloir_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0

    "Je rejoins Nyra presque dès qu'elle passe la porte et lui attrape doucement le bras avant qu'elle ne puisse repartir avec les autres."

    $ showGroup([
        ("noam", "reflexion", 0.30),
        ("nyra", "neutre", 0.70),
    ])

    nyra reflexion "Qu'est-ce qu'il y a ?"

    noam hesitation "C'est ce que je voulais te dire ce matin. Hier soir, j'ai vu Ryn sortir de la chambre d'Iris."

    "Son expression change immédiatement. Elle ne panique pas, mais toute son attention se fixe sur moi."

    nyra reflexion "Tu es sûr que c'était bien lui ?"

    noam "Complètement. On s'est même parlé dans le couloir."

    nyra inquiet "Et il t'a dit pourquoi il était là ?"

    noam desaccord "Non. Il m'a juste souhaité bonne nuit et il est parti. Ce matin, je l'ai croisé à la cafétéria et, cette fois, il a clairement évité la conversation."

    "Nyra baisse légèrement les yeux, réfléchit quelques secondes, puis relève la tête."

    nyra determine "On ne va pas essayer de deviner. On va demander directement à Anya ce qui s'est passé."

    noam reflexion "Maintenant ?"

    nyra "Oui. Plus on attend, plus on risque de se raconter n'importe quoi."

    "Je hoche la tête et nous quittons ensemble le couloir en direction de la chambre d'Iris."

    $ hideGroup()

    jump _9_1_0_0_ANYA


label _9_1_0_0_ANYA:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre_iris", "bg_chambre_iris") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_3
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    "Iris n'est pas là quand nous entrons, ce qui nous évite au moins d'avoir à expliquer immédiatement pourquoi nous transformons une nouvelle fois sa chambre en salle de réunion clandestine."
    "Anya est assise sur le lit avec une tablette entre les mains. Elle relève les yeux vers nous et comprend immédiatement à nos têtes qu'on ne vient pas simplement lui tenir compagnie."

    $ showGroup([
        ("noam", "reflexion", 0.20),
        ("nyra", "neutre", 0.50),
        ("anya", "reflexion", 0.80),
    ])

    anya reflexion "Qu'est-ce qui se passe ?"

    nyra "On doit te poser quelques questions sur hier soir."

    anya hesitation "... D'accord."

    "Nyra désigne discrètement la salle de bain et Anya se lève sans discuter. Quelques secondes plus tard, nous sommes tous les trois enfermés à l'intérieur, à l'abri du micro de la chambre."

    scene bg_salle_de_bain_iris at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "reflexion", 0.20),
        ("nyra", "neutre", 0.50),
        ("anya", "reflexion", 0.80),
    ])

    nyra reflexion "Ryn est venu te voir hier soir ?"

    anya "Oui."

    noam surpris "Donc il t'a bien vue."

    anya reflexion "Il est entré dans la chambre alors qu'Iris n'était pas là. Je pensais qu'il allait paniquer ou partir prévenir quelqu'un, mais... rien. Il avait presque l'air de savoir que j'étais ici avant même d'ouvrir la porte."

    "Nyra et moi échangeons un regard."

    nyra inquiet "Il t'a dit comment il le savait ?"

    anya desaccord "Non. Je lui ai demandé s'il comptait parler de moi à Kami ou aux autres, et il m'a juste répondu qu'il ne dirait rien à personne."

    noam reflexion "Et tu l'as cru ?"

    anya "Sur le moment, oui. Il n'avait pas l'air de vouloir me faire peur, et il n'a rien essayé non plus. Il s'est surtout mis à me poser des questions."

    nyra reflexion "Sur quoi ?"

    anya "Sur le réseau que j'ai utilisé pour quitter Limen. Il voulait savoir comment je l'avais trouvé, comment les passeurs choisissaient les conteneurs, à quel moment les marchandises étaient contrôlées et s'il existait des trajets moins surveillés que les autres."

    "Je repense immédiatement à l'annonce que Kami vient de faire devant nous."

    noam inquiet "Il s'intéressait surtout aux contrôles ?"

    anya "Oui. Beaucoup. Il m'a demandé qui surveillait les dépôts à Limen, comment les inspections étaient organisées et si certains conteneurs pouvaient traverser une zone sans être ouverts."

    nyra reflexion "Tu lui as répondu ?"

    anya desaccord "Pas vraiment. Je ne connais pas le réseau assez bien pour ça. J'ai payé quelqu'un, on m'a donné une heure, un emplacement et un numéro de conteneur. C'est à peu près tout ce que je savais."

    noam reflexion "Et il n'a vraiment rien expliqué sur la raison pour laquelle ça l'intéressait ?"

    anya "Non. Il m'a seulement dit de ne pas m'inquiéter, qu'il ne parlerait de moi à personne, puis il est reparti comme si cette conversation était parfaitement normale."

    "Nyra reste silencieuse un moment. Elle ne paraît pas paniquée, mais je vois bien qu'elle n'aime pas davantage que moi ce que nous venons d'entendre."

    nyra reflexion "S'il avait voulu te dénoncer, il aurait déjà pu le faire. Ce n'est probablement pas son objectif."

    noam hesitation "Ce qui ne nous dit toujours pas ce qu'il cherche."

    nyra "Non. Et pour l'instant, je préfère qu'on ne le confronte pas directement. S'il sait déjà pour Anya et qu'il a choisi de se taire, autant éviter de lui donner une raison de changer d'avis."

    anya inquiet "Donc je fais quoi, moi ?"

    nyra "Rien de différent. Tu restes ici, tu évites de te montrer et, s'il revient, tu ne lui donnes aucune information supplémentaire."

    anya "Ça me va."

    "La porte de la chambre s'ouvre brusquement de l'autre côté et nous nous taisons immédiatement. Quelques secondes plus tard, des pas traversent la pièce avant de s'arrêter juste devant la salle de bain."

    iris "... Sérieusement ?"

    "La porte s'ouvre et Iris nous découvre tous les trois entassés dans sa salle de bain. Elle reste immobile une seconde, puis lève lentement les yeux au plafond comme si elle cherchait encore un peu de patience quelque part."

    $ showGroup([
        ("noam", "gene", 0.10),
        ("nyra", "neutre", 0.35),
        ("anya", "reflexion", 0.60),
        ("iris", "colere", 0.90),
    ])

    iris colere "Non mais c'est devenu quoi ma chambre exactement ? Une salle commune ? Un centre de réunion ? Vous voulez que j'installe des chaises et un distributeur pendant qu'on y est ?"

    noam gene "On avait juste besoin de parler sans le micro."

    iris desaccord "Oui, je sais, tout le monde a toujours besoin de parler sans le micro dans MA salle de bain. C'est pratique, hein ? Moi aussi j'aimerais bien pouvoir entrer dans ma propre chambre sans découvrir une réunion secrète à chaque fois."

    nyra calme "On a presque terminé."

    iris "Heureusement, parce que j'aimerais récupérer au moins dix minutes d'intimité avant ce soir."

    "Elle pointe ensuite Anya du doigt sans même attendre de réponse."

    iris colere "Et toi, cette nuit, tu dors de ton côté du lit."

    anya surpris "Mon côté ?"

    iris "Oui, ton côté. Celui qui n'est pas le mien."

    anya desaccord "Ton lit fait deux mètres de large, j'ai littéralement dormi au bord."

    iris "Tu as dormi en diagonale."

    anya colere "Je n'ai pas dormi en diagonale !"

    iris "J'ai passé la moitié de la nuit coincée contre le mur avec ton genou dans les côtes."

    anya "Parce que tu me repoussais avec tes pieds !"

    iris desaccord "Parce que tu prenais toute la place !"

    "Nyra tourne lentement la tête vers moi avec une expression parfaitement neutre."

    nyra "Je pense qu'on peut y aller."

    noam sourire "Je pense aussi."

    iris colere "Oui. Sortez. Tous les deux."

    anya desaccord "Et moi ?"

    iris "Toi tu restes, malheureusement."

    anya "Charmant."

    "Je préfère ne pas attendre la suite de leur dispute. Nyra et moi quittons la salle de bain, puis la chambre, en laissant Iris expliquer très sérieusement à Anya le concept d'une moitié de lit."

    $ hideGroup()

    jump _9_1_0_0_SOIR


label _9_1_0_0_SOIR:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_9_1_0_0_4
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5

    "Quand je retourne finalement dans ma chambre, la journée me paraît étrangement calme malgré tout ce qui vient de se passer. Le vote s'est déroulé sans conflit, Anya est toujours cachée et, pour l'instant au moins, Ryn n'a parlé à personne."

    "Je retire mes chaussures et m'allonge sur le lit en repensant malgré moi aux questions qu'il lui a posées."

    think "Il savait qu'elle était là, il connaissait l'histoire du conteneur et ce qui l'intéressait surtout, c'était le réseau et les contrôles."
    think "Je ne sais pas encore ce qu'il cherche, mais ce n'est clairement pas par simple curiosité."

    "L'annonce de Kami me revient aussi en tête. Bientôt, davantage de gens seront payés pour inspecter les marchandises, surveiller les zones de transit et ouvrir précisément les conteneurs qui ont permis à Anya d'arriver jusqu'ici."

    think "On a eu de la chance une fois. Je ne suis pas sûr que quelqu'un puisse refaire le même trajet aussi facilement maintenant."

    "Je souffle longuement et ferme les yeux. Pour ce soir, je n'ai de toute façon aucune réponse de plus à trouver."

    noam fatigue "Demain..."

    "Je laisse ma tête retomber contre l'oreiller et finis par m'endormir sans chercher davantage à démêler tout ce qui s'est accumulé depuis la veille."

    stop music fadeout 3.0
    scene black with fade

    call end_day("10") from _call_end_day_9100
    jump patreon_ending
