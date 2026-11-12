label _11_0_1_1_REVEIL_CHAMBRE:
    $ cafeteria_food_level = "low"
    $ current_period = "Matin"
    $ current_day = 11
    $ noam_has_juliette_drawing = False
    play music "music/bgm_fallin_love.mp3" fadein 2.5
    play sound sfx_heartbeat fadeout 3.0
    "..."
    iris "Tu comptes dormir jusqu'au prochain vote ?"
    "Quelque chose de froid se pose sur mon front. J'essaye de répondre, mais ma langue semble avoir oublié comment fonctionner."
    iris "Ah, voilà. Ça bouge. Bon signe."
    scene bg_chambre at adaptive_fullscreen with Fade(2.0, 0.0, 3.0)
    noam faible "Iris... ?"
    iris "Non. Kami, dans un nouveau corps. Tu trouves que je lui ressemble ?"
    noam fatigue "T'es moins agréable."
    iris "Il EST vivant !"
    scene bg_cg031 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg031")
    "Elle a un linge humide dans la main. Ses cheveux sont défaits et elle a une marque rouge sur la joue, comme si elle s'était endormie dans une mauvaise position."
    noam hesitation "Qu'est-ce que..."
    iris fatigue "Tu t'es écroulé. Au Conclave. Devant tout le monde. Très joli spectacle."
    noam inquiet "Hier ?"
    iris "Non, dans cent ans. Oui, hier !"
    noam fatigue "Je me souviens de la table. Après..."
    iris "Après, tu as essayé de faire connaissance avec le sol. Heureusement qu'on t'a rattrapé."
    "Elle essore le linge. De l'eau tombe sur la couverture."
    iris "Ah, merde."
    noam taquin "Tu sais, si tu voulais me noyer, il y avait plus simple."
    iris colere "Tu peux me remercier aussi, ça se fait !"
    noam sourire "Merci."
    iris "..."
    iris gene "C'était pas une invitation à le dire tout de suite."
    "Je tente de me redresser. Ma tête proteste immédiatement."
    iris colere "HÉ ! Tu fais quoi ?!"
    noam fatigue "Je m'assieds."
    iris "Tu te recouches."
    noam taquin "J'ai vraiment aucun droit ici ?"
    iris desaccord "Pas tant que tu continues à essayer de t'évanouir."
    "Elle me remet le verre d'eau dans la main. Cette fois, elle attend que je le tienne correctement."
    noam inquiet "J'ai dormi combien de temps ?"
    iris fatigue "Toute la nuit. Tu as fait une grosse fièvre, tu parlais à moitié dans ton sommeil, et Sael est venue vérifier que tu n'avais rien de plus grave."
    noam reflechit "Sael ?"
    iris "Oui, Sael. C'est elle qui sait s'occuper des gens. Moi je suis surtout là pour t'empêcher de faire une connerie."
    noam taquin "Mission ambitieuse."
    iris taquin "Ne me sous-estime pas."
    "Elle attrape un thermomètre sur la table et le pose hors de ma portée."
    iris fatigue "Mara a passé deux heures à râler à ton chevet. Elen voulait t'apporter une couverture supplémentaire. Je lui ai dit qu'on avait déjà assez chaud."
    noam fatigue "Et toi ?"
    iris desaccord "Moi quoi ?"
    noam neutre "T'es restée ?"
    iris gene "Quelqu'un devait surveiller que tu t'étouffes pas avec ta langue !"
    noam taquin "Ça arrive souvent ?"
    iris colere "LA FERME."
    "Je ris. Une douleur sourde me traverse aussitôt le crâne."
    iris inquiet "Hé. Ça va ?"
    noam fatigue "Oui. Je regrette juste ma blague."
    iris taquin "C'est la première décision raisonnable que tu prends depuis hier."
    "Pendant quelques secondes, elle ne dit plus rien. Elle regarde le linge dans ses mains."
    iris fatigue "Ryn est passé aussi. Enfin, il s'est arrêté devant la porte."
    noam surpris "Il est entré ?"
    iris "Non. Il a demandé si tu étais mort, j'ai répondu non, et il a dit de pas changer d'avis."
    noam sourire "C'est touchant."
    iris neutre "Ouais. Dans son genre."
    "J'essaye de retrouver la fin de la journée précédente. Les questions. La salle du Conclave. Le couloir."
    think "Quelque chose me manque. Pas seulement les heures entre mon malaise et maintenant."
    iris reflechit "Quoi ?"
    noam hesitation "Quoi, quoi ?"
    iris "Tu fais cette tête-là. Celle où tu réfléchis à un truc que tu vas garder pour toi jusqu'à ce que ça t'explose dessus."
    noam fatigue "J'ai une tête pour ça ?"
    iris desaccord "Oui. Et elle est insupportable."
    menu:
        "Lui parler de ce qui s'est passé dans le couloir.":
            jump noam_parle_doppelganger_iris
        "Ne rien lui dire pour le moment.":
            jump noam_garde_secret


label noam_parle_doppelganger_iris:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5
    $ showGroup([("noam", "fatigue", 0.20), ("iris", "inquiet", 0.80)])
    noam hesitation "Hier, avant l'annonce de Kami... dans le couloir de l'infirmerie."
    iris inquiet "Quoi, le coup de chaud ?"
    noam reflechit "Je crois que j'ai vu quelqu'un."
    iris "Tu crois ?"
    noam inquiet "Non. C'est justement ça qui me gêne. Sur le moment, j'étais sûr qu'il y avait un truc. Et maintenant j'arrive même pas à dire quoi."
    iris reflechit "Sael t'a trouvé là, non ?"
    noam "Oui. Mais avant elle..."
    "Je cherche les mots. À chaque fois que je suis sur le point d'en choisir un, il me semble faux."
    noam fatigue "J'ai regardé le fond du couloir. Après j'ai eu peur. Vraiment peur. Et je sais pas pourquoi."
    iris desaccord "Tu étais brûlant de fièvre quelques heures plus tard."
    noam inquiet "Tu crois que j'ai halluciné ?"
    iris fatigue "J'en sais rien ! Je te dis ce que je sais, pas ce que tu dois penser."
    "Sa réponse me surprend assez pour que je relève les yeux."
    iris reflechit "Mais si tu es malade, fatigué, et qu'en plus le système de ventilation fait n'importe quoi... je vais pas appeler ça une preuve."
    noam neutre "C'est pas une preuve. Je le sais."
    iris inquiet "Tu as demandé leurs alibis à tout le monde. Tu te rappelles ?"
    noam hesitation "Oui."
    iris "Tu leur as fait peur."
    noam fatigue "Je voulais pas."
    iris neutre "Je sais. C'est pour ça que je te le dis."
    "Elle replie le linge, le pose sur la table, puis se lève."
    iris reflechit "Si tu veux chercher, cherche quand tu pourras marcher sans tomber. Et évite de refaire ton interrogatoire devant douze personnes."
    noam taquin "Donc tu me proposes de devenir détective ?"
    iris desaccord "Je te propose de boire de l'eau et d'arrêter de faire des mouvements stupides !"
    noam sourire "Très bien, chef."
    iris gene "Et... si ça recommence, tu m'en parles."
    noam neutre "D'accord."
    iris fatigue "Je vais te chercher à manger. Ne bouge pas. Ça me fatigue de devoir répéter."
    "Elle sort sans attendre de réponse."
    jump _11_0_1_1_APRES_REVEIL


label noam_garde_secret:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5
    $ showGroup([("noam", "fatigue", 0.20), ("iris", "inquiet", 0.80)])
    noam hesitation "Rien. J'essayais juste de me souvenir du moment où je suis tombé."
    iris desaccord "Tu mens mal."
    noam fatigue "Tu dis ça à chaque fois."
    iris "Parce que tu mens mal à chaque fois."
    "Je prends une gorgée d'eau pour éviter de répondre."
    iris reflechit "Bon. On va pas jouer à ça toute la matinée."
    noam neutre "Merci."
    iris taquin "Je peux encore changer d'avis."
    "Elle ajuste le linge qui glissait de mon front, puis se redresse aussitôt."
    iris fatigue "Tu as fait assez peur à tout le monde. Le minimum, c'est de manger quelque chose."
    noam sourire "Tu comptes m'apporter un petit-déjeuner au lit ?"
    iris desaccord "Te fais pas d'idées. Je t'apporte de quoi éviter que tu t'écroules une deuxième fois."
    noam taquin "C'est presque romantique."
    iris colere "J'AI DIT DE PAS TE FAIRE D'IDÉES !"
    "Elle se dirige vers la porte. Juste avant de sortir, elle jette un dernier regard vers moi."
    iris gene "Si tu as vraiment quelque chose en tête... tu peux m'en parler. Plus tard."
    noam neutre "D'accord."
    "Elle referme la porte."
    jump _11_0_1_1_APRES_REVEIL


label _11_0_1_1_APRES_REVEIL:
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.0
    "Une fois seul, je tente de me lever. Mes pieds touchent à peine le sol que je me ravise."
    noam faible "D'accord. Point pour Iris."
    "Je reste assis, le verre dans les mains, à regarder la table. Il n'y a toujours pas le dessin de Juliette."
    think "Je pourrais reprendre mes recherches. Ou tomber tête la première sur le bureau. Ça ferait une belle fin."
    "Des voix montent du couloir."
    julian "JE N'AI JAMAIS DIT QU'IL FALLAIT EN METTRE AUTANT !"
    iris "C'EST TOI QUI AS PRIS LE PLATEAU !"
    sael "Arrêtez de secouer la porte !"
    "Je n'ai même pas le temps de comprendre qu'elle s'ouvre."
    $ showGroup([
        ("noam", "fatigue", 0.20), ("iris", "neutre", 0.40),
        ("sael", "neutre", 0.60), ("julian", "neutre", 0.80),
        ("nyra", "neutre", 1.00),
    ])
    julian taquin "Messieurs-dames ! Voici le service de restauration le plus prestigieux de l'orbite !"
    iris colere "Pose. Le. Plateau."
    julian "Je le pose !"
    "Le plateau touche la table avec un bruit sinistre. Un morceau de pain roule jusqu'au bord."
    noam taquin "C'est un repas ou une attaque ?"
    julian sourire "Les deux, si tu continues."
    sael desaccord "Julian, écarte-toi."
    julian "J'essaye de rendre service !"
    nyra raison "Tu en rendrais davantage en laissant de l'espace autour du lit."
    julian "Il y a donc une coalition contre les bénévoles."
    iris taquin "Elle est unanime."
    "Sael prend ma main, vérifie brièvement mon pouls, puis me rend mon poignet."
    sael neutre "Tu as moins chaud. La fièvre est tombée, mais tu te reposes aujourd'hui. Pas de discussion."
    noam fatigue "Les discussions, c'est pourtant notre seule activité ici."
    sael determine "Alors tu peux faire exception."
    nyra neutre "J'ai demandé qu'on prépare des portions simples. C'est ce qui nous paraissait le moins risqué après la nuit dernière."
    julian taquin "Riz, poulet et légumes. La gastronomie du rétablissement. Aucun risque d'y prendre goût."
    iris colere "Tu peux arrêter d'insulter la nourriture pendant qu'il mange ?!"
    noam sourire "Je trouve ça délicieux."
    julian surpris "Tu n'as pas encore goûté !"
    noam taquin "Je voulais t'embêter. Ça marche plutôt bien."
    "Nyra détourne les yeux. Elle sourit très légèrement, puis reprend sa posture habituelle."
    sael reflechit "La ventilation fonctionne mieux ce matin. Les équipes techniques ont remis une partie du circuit en service."
    iris fatigue "Ça explique pourquoi j'ai pu dormir vingt minutes sans me réveiller en nage."
    nyra raison "Le Canon a encore sollicité le réseau de refroidissement. Le diagnostic n'est pas terminé."
    julian "Pourrais-je proposer qu'on interdise les coups de chaud par vote unanime ?"
    iris desaccord "Non."
    noam neutre "Même pas pour mon bien ?"
    sael neutre "Mange."
    "J'obéis. Pendant quelques minutes, les autres débattent de la quantité de sel dans les légumes et d'une éventuelle redistribution des desserts."
    julian "Je dis simplement que les malades méritent un dessert supplémentaire."
    iris taquin "Tu t'es découvert une maladie ?"
    julian "Le manque de reconnaissance."
    nyra neutre "Le traitement sera long."
    "Je manque d'avaler de travers."
    noam sourire "Nyra !"
    nyra raison "C'était une observation."
    sael desaccord "Une observation très pertinente. Et maintenant, laisse-le manger."
    "Je repose ma cuillère. L'espace d'une seconde, j'oublie le Conclave, le vote et le couloir."
    "Puis Kael me revient en tête. Sa photographie. Les images qui pourraient montrer qui est entré chez lui."
    noam reflexion "Kael n'est pas venu ?"
    iris inquiet "Il est passé cette nuit. Il ne voulait pas te réveiller."
    sael reflechit "Il a demandé si tu allais mieux. Puis il est reparti."
    julian neutre "Il n'a toujours pas retrouvé sa photo."
    iris desaccord "Julian !"
    julian "Quoi ? Il le sait déjà."
    noam neutre "C'est vrai."
    nyra reflechit "Kael a demandé l'accès aux images de sa chambre. Nous n'avons pas encore de réponse."
    iris fatigue "On dirait qu'on peut enfin parler d'autre chose que de ma capacité à veiller un malade."
    noam taquin "C'est toi qui en parles le plus."
    iris colere "TOI, MANGE."
    "Je reprends ma cuillère."
    call show_custom_title("Une bonne heure plus tard") from _call_show_custom_title_2
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([
        ("noam", "neutre", 0.20), ("iris", "neutre", 0.40),
        ("sael", "neutre", 0.60), ("julian", "neutre", 0.80),
        ("nyra", "neutre", 1.00),
    ])
    julian taquin "Voilà. Notre malade a mangé. Je réclame officiellement une médaille."
    iris fatigue "Tu l'as regardé manger. C'est tout."
    julian "J'ai aussi transporté le plateau."
    sael determine "Et failli le renverser."
    julian "Les critiques sont parfois injustes envers les grands hommes."
    "Je me lève en m'appuyant sur le rebord du lit."
    sael inquiet "Doucement."
    noam fatigue "J'ai juste besoin de marcher un peu. Promis, je ne pars pas courir autour de la station."
    iris desaccord "Tu veux que je te porte, tant qu'on y est ?"
    noam taquin "Ça dépend. Tu pourrais ?"
    iris colere "ESSAIE POUR VOIR."
    nyra reflechit "La salle d'observation est moins chaude. On peut l'y accompagner, si Sael pense que ça ne pose pas de problème."
    sael neutre "Quelques minutes. Et au moindre vertige, retour au lit."
    noam sourire "Compris."
    $ hideGroup()
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Dans le couloir, Julian se lance dans une description interminable de son système idéal de répartition des desserts. Iris corrige chaque point. Nyra ne participe pas. Sael marche près de moi."
    julian "Je propose donc trois catégories : les desserts de consolation, les desserts de victoire et les desserts de nécessité diplomatique."
    iris desaccord "Tu viens d'inventer trois raisons pour en manger."
    julian "Trois excellentes raisons."
    sael neutre "On arrive."
    "Une voix filtre à travers la porte entrouverte de la salle d'observation."
    stop music fadeout 1.0
    play music "music/bgm_system_override.mp3" fadein 2.0
    kami "Oh, Kael... J'aimerais tellement t'aider. Mais tu ne peux pas exiger que la technologie obéisse à tes sentiments."
    "Nous nous arrêtons. Julian referme aussitôt la bouche."
    kael "Sept jours. C'est ça que tu me dis ?"
    "Personne ne bouge. Sael me lance un regard, puis pousse la porte."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_42
    scene bg_observation at adaptive_fullscreen with dissolve
    $ current_period = "Après-midi"
    $ showGroup([
        ("kael", "neutre", 0.50),
        ("noam", "fatigue", 0.18), ("iris", "inquiet", 0.34),
        ("sael", "neutre", 0.66), ("julian", "neutre", 0.82),
        ("nyra", "neutre", 0.96),
    ])
    kael colere "Je t'ai posé une question simple !"
    kami "Et je t'ai donné une réponse merveilleusement claire."
    kael "Je veux les images de ma chambre. Celles de la nuit où ma photo a disparu."
    kami "Et moi, je veux un peu de gratitude."
    kael colere "KAMI !"
    kami "D'accord, d'accord ! Les brouilleurs en vigueur imposent un délai de sept jours sur l'accès aux données vidéo et audio concernées."
    kami "Ce n'est pas une question de bonne volonté. Même moi, je ne peux pas te donner immédiatement ce que le système ne rendra accessible que plus tard."
    kael reflechit "Donc avant sept jours, impossible de vérifier qui est venu."
    kami "Exactement ! Je vois que tu écoutes quand tu veux."
    kael triste "Et si le vote échoue ?"
    kami "Si vous interdisez les brouilleurs, les enregistrements concernés ne redeviendront pas accessibles par magie."
    "Kael ne répond pas. Il serre les doigts si fort autour du bord de la console que ses phalanges blanchissent."
    iris inquiet "Kael..."
    kael surpris "..."
    "Il nous remarque enfin."
    kael calme "Vous êtes là depuis combien de temps ?"
    julian taquin "Assez pour découvrir que Kami déteste toujours rendre service."
    kami "Julian, je suis BLESSÉE !"
    nyra raison "L'indisponibilité est-elle une propriété du brouilleur, ou une limitation de la base d'archives ?"
    kami "Une propriété de la protection en place. Et non, je ne vais pas vous remettre son manuel technique."
    nyra reflechit "C'était pourtant ma question suivante."
    kael fatigue "Super. On va donc attendre une semaine pendant que celui qui m'a pris la photo..."
    "Il s'interrompt."
    sael neutre "Personne ici ne te demande d'oublier Léa."
    kael triste "J'ai pas dit ça."
    sael reflechit "Je sais."
    iris fatigue "Tu as mangé quelque chose aujourd'hui ?"
    kael colere "Ça n'a aucun rapport !"
    iris desaccord "Je sais. Mais t'as quand même besoin de manger."
    kael calme "... Plus tard."
    "Il se tourne vers la porte, puis revient vers nous."
    kael reflechit "Si vous découvrez quelque chose sur les chambres, vous me le dites. Même un détail."
    noam neutre "Oui."
    "Kael sort. Les autres le regardent partir."
    call play_stat_dialogue("j11") from _call_play_stat_dialogue_10
    julian neutre "Bon. Les desserts diplomatiques peuvent attendre."
    iris fatigue "Pour une fois, oui."
    nyra reflechit "La distinction est intéressante. Il a parlé d'images de chambre, pas des couloirs."
    noam reflexion "Parce que les brouilleurs sont dans les chambres."
    nyra raison "Exactement."
    sael inquiet "Noam ?"
    "Je me suis appuyé contre le mur sans m'en rendre compte."
    noam fatigue "Je vais retourner m'allonger."
    iris desaccord "Pour une fois, voilà une bonne idée !"
    julian taquin "Une décision raisonnable de Noam. Cette journée est historique."
    noam sourire "Vous pouvez continuer votre débat sur les desserts sans moi."
    nyra neutre "Tu veux qu'on t'accompagne ?"
    noam neutre "C'est juste à côté. Ça ira."
    sael determine "Tu marches lentement, et tu préviens si ça recommence."
    noam taquin "Oui, Sael."
    iris gene "Et repose-toi vraiment cette fois."
    "Je les laisse dans la salle. Les pas de Julian et la voix d'Iris recommencent presque aussitôt derrière moi."
    jump _11_0_1_2_CHAMBRE_INTROSPECTION


label _11_0_1_2_CHAMBRE_INTROSPECTION:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_43
    scene bg_chambre at adaptive_fullscreen with dissolve
    stop music fadeout 1.0
    "Je ferme la porte, retire mes chaussures et m'affale sur le lit."
    noam fatigue "Voilà. J'obéis. Tout le monde est content."
    "Le silence de la chambre est agréable pendant une dizaine de secondes. Puis les paroles de Kael me reviennent."
    think "Sept jours..."
    "Je me redresse légèrement."
    noam reflechit "Les brouilleurs..."
    "Je regarde le petit boîtier fixé au mur. Le voyant continue de pulser."
    think "Kami dit qu'on ne peut pas consulter les images d'une chambre avant sept jours. D'accord."
    "Je repense au couloir d'hier. J'étais près de l'infirmerie, pas dans une chambre."
    noam hesitation "Mais là où j'étais..."
    "Je m'interromps. J'aimerais vraiment avoir tort, parce que l'autre possibilité m'oblige à me lever."
    call _11_0_1_2_MINIJEU_7JOURS from _call__11_0_1_2_MINIJEU_7JOURS
    play music "music/bgm_world_decline.mp3" fadein 2.0
    noam reflechit "Il n'y a pas de brouilleur dans les couloirs."
    "Je laisse la phrase résonner. Elle paraît simple. Presque bête."
    noam inquiet "Alors les caméras du couloir... elles devraient être accessibles, non ?"
    "Je reste encore un instant au bord du lit, à fixer mes chaussures."
    think "Iris m'étranglerait si elle me voyait me relever. Sael m'ordonnerait de retourner sous les draps."
    noam taquin "Et Julian ferait un discours sur l'héroïsme des malades."
    "Je remets mes chaussures."
    think "Si j'ai imaginé tout ça, les images me le diront. Et si je n'ai rien imaginé..."
    "Je me relève, plus prudemment que ce matin."
    noam neutre "Je vais juste poser une question. Après, je reviens."
    call KD_ROUTE_J11_NYRA from _call_optional_kd_route_j11_nyra
    call OFFER_DAILY_EXPLORATION(
        "_11_0_1_3_SALLE_COMMUNICATION", 1,
        ["observation", "archive", "dortoir"],
        _("Rejoindre la salle d'Observation"), "observation"
    ) from _call_offer_exploration_j11


label _11_0_1_3_SALLE_COMMUNICATION:
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_MAYBE_PLAY_SCRIPTED_DOOR_44
    scene bg_observation at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.0
    "Les écrans de la salle d'observation affichent la Terre. Je m'installe devant une console et j'attends une seconde."
    noam neutre "Kami ?"
    pause 0.8
    noam taquin "C'est la partie où tu apparais en me disant que j'ai une tête de zombie."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh, mais JE PEUX ! Tu es tellement prévisible, Noam."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "D'ailleurs, je croyais que tu étais censé te reposer. Iris et Sael vont me gronder si je te laisse te fatiguer davantage !"
    noam fatigue "Elles sont pas là."
    kami "La désobéissance commence toujours par une phrase comme celle-là."
    noam neutre "J'ai besoin d'accéder à des enregistrements."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Oh ? Nous avons un futur archiviste parmi nous ? Quelle vocation passionnante !"
    noam reflechit "Hier. Dans le couloir près de l'infirmerie. Juste avant ton annonce."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et tu voudrais voir si tu avais une bonne raison de demander l'alibi de tous tes petits camarades ?"
    "Je serre les dents. Elle n'a pas oublié."
    noam inquiet "Oui."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu pourrais aussi choisir de croire les gens. C'est une méthode très reposante, tu sais."
    noam colere "Tu vas me donner les images, oui ou non ?"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Quelle IMPOLITESSE ! Et après, on se demande pourquoi les enfants grandissent si mal."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais enfin, pourquoi pas ? Les caméras des couloirs ne sont pas soumises au brouillage de vos chambres."
    noam reflechit "Donc les images sont accessibles."
    kami "Si elles sont encore là, évidemment."
    "Je relève la tête."
    noam inquiet "Comment ça, « si » ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Un ordinateur, Noam ! Il faut parfois le laisser travailler au lieu de le harceler."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je t'ouvre le catalogue des archives. Cherche toi-même : heure, secteur, caméra. Rien de plus simple."
    noam fatigue "C'est gentil, vraiment."
    kami "Je sais. C'est presque inquiétant."
    scene bg_observation at adaptive_fullscreen with dissolve
    "La console se déverrouille. Plusieurs secteurs apparaissent, chacun subdivisé en dizaines de créneaux horaires."
    "Je commence à chercher celui que je veux. Mon cœur bat beaucoup trop vite pour un simple menu d'ordinateur."
    call _11_0_1_3_MINIJEU_CAMERAS from _call__11_0_1_3_MINIJEU_CAMERAS


label _11_0_1_1_CONFRONTATION_KAMI:
    scene bg_observation at adaptive_fullscreen with dissolve
    "Je sélectionne le dernier créneau. La console affiche un aperçu du couloir."
    "Mon doigt reste suspendu au-dessus de la commande de lecture."
    noam inquiet "Allez..."
    "L'image disparaît."
    "DONNÉES SUPPRIMÉES — ACCÈS IMPOSSIBLE."
    $ investigation_add("videos_supprimees")
    "Je clique une seconde fois. Puis une troisième."
    noam colere "Non. Non, NON !"
    "Même message."
    noam colere "KAMI !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "OH ! Je ne savais pas que nous en étions déjà à l'étape où tu cries mon nom dans une pièce vide."
    noam colere "Les images ont été supprimées !"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oui. Je sais lire."
    noam colere "C'est toi ?"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Moi ?! Tu me blesses. Je t'ai ouvert les archives avec toute la gentillesse dont je suis capable."
    noam desaccord "Tu pouvais faire semblant de m'y donner accès."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Quel soupçon désobligeant. La requête d'effacement n'a pas été effectuée par moi."
    noam reflechit "Une requête ?"
    kami "Oui, une requête. Je peux même te l'épeler si tu préfères."
    noam colere "Qui l'a envoyée ?!"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ah ! Voilà une question intéressante."
    noam inquiet "Kami..."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Elle provient d'un accès autorisé à bord du Conclave. Rien de bien exotique."
    "Je regarde la console. Une ligne vide apparaît là où aurait dû figurer le fichier."
    noam reflechit "Tu veux dire qu'un des représentants..."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Je n'ai pas dit « un représentant ». J'ai dit « un accès autorisé ». Fais attention, les mots ont un sens."
    noam colere "Tu sais qui l'a demandé !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Et même si je le savais, tu voudrais que je te le dise comme ça ? Sans effort ?"
    noam neutre "Oui."
    kami "Oh. C'est si décevant."
    "Je ravale ma colère. Elle attend que je m'emporte, ça se voit."
    noam reflechit "L'effacement concerne seulement ce créneau ?"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Voilà ! Une question technique ! Tu progresses !"
    kami "Ce segment est indisponible. Je te laisse regarder le reste du catalogue si ça t'amuse. Je ne peux pas te fabriquer des images qui ne sont plus là."
    noam inquiet "Il y avait quelque chose sur ces images ?"
    pause 0.6
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Tu aimerais beaucoup que je réponde « oui », n'est-ce pas ?"
    noam colere "Je veux juste savoir ce que j'ai vu !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais moi aussi, Noam ! C'est ce qui rend notre conversation si palpitante !"
    "Je ne sais pas si elle plaisante. Le pire, c'est que je crois qu'elle se réjouit sincèrement de ne pas me donner de réponse."
    noam inquiet "Alors pourquoi tu souris ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Parce que je suis ravissante."
    noam colere "Arrête !"
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "NON, TOI, ARRÊTE ! Tu viens dans MA salle, tu M'ACCUSES, et tu crois que je vais tout t'expliquer comme une gentille petite assistante !"
    "Son visage reste figé une fraction de seconde."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais je vais quand même te donner quelque chose. Un cadeau."
    noam reflechit "Quoi ?"
    kami "Cherche du côté des gens qui avaient accès à ce secteur. Ça te fera une occupation."
    noam inquiet "Les autres..."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Les gens qui mangent avec toi. Qui te donnent de l'eau. Qui viennent à ton chevet. Quelle adorable petite communauté !"
    "Je pense à Iris qui m'a apporté le linge, à Sael, à Julian et à son plateau ridicule."
    think "Elle essaye de me faire soupçonner tout le monde."
    noam desaccord "Tu n'as rien prouvé."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Exact. Et toi non plus."
    "Je reste silencieux."
    noam reflechit "Si quelqu'un a effacé ces images, il savait ce que j'allais chercher ?"
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Voilà que tu recommences à poser les bonnes questions."
    noam colere "RÉPONDS !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Non."
    pause 0.8
    noam fatigue "Tu prends vraiment plaisir à ça, hein ?"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Énormément !"
    "Elle ne cherche même pas à le nier. Je crois que c'est ce qui me donne le plus envie de hurler."
    noam colere "Va te faire foutre."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "LANGAGE !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Allez, au lit, mon petit détective. Tu as déjà réussi à ne pas t'évanouir pendant une conversation entière. C'est un grand progrès."
    noam inquiet "Et les images ?"
    kami "Toujours supprimées. Tu vois ? Certaines choses restent constantes dans ce monde."
    "Je tourne les talons."
    kami "Oh, Noam ?"
    "Je m'arrête malgré moi."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Si tu avais vu quelque chose d'important, tu crois vraiment que quelqu'un aurait pris le risque de laisser les images en place ?"
    "Je me retourne. L'écran est déjà noir."
    think "C'est une question. Pas une réponse."
    "Je quitte la salle avant qu'elle puisse m'en poser une autre."
    stop music fadeout 2.0
    jump _11_0_1_1_RETOUR_CHAMBRE


label _11_0_1_1_RETOUR_CHAMBRE:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_47
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0
    "Dans le couloir, j'entends une dispute venir de la salle commune."
    julian "J'AI DIT QUE C'ÉTAIT UNE MÉDAILLE HONORIFIQUE !"
    iris "T'AS DESSINÉ TON PROPRE VISAGE DESSUS !"
    "Je m'arrête. Il y a quelques heures, j'aurais ri. Maintenant, je me demande combien de temps ils ont passé ensemble avant de rentrer ici."
    think "Non. C'est exactement ce que Kami veut."
    "Je reprends ma marche."
    "Au croisement du dortoir, une porte s'ouvre. Lysa passe la tête dans le couloir."
    lysa neutre "Noam ?"
    noam fatigue "Salut."
    lysa reflechit "Tu tiens debout. C'est déjà mieux qu'hier."
    noam taquin "Vous avez tous préparé des remarques sur mon malaise ?"
    lysa sourire "On a fait un concours. J'ai perdu contre Julian. Il avait dix-sept propositions."
    noam fatigue "Ça lui ressemble."
    "Elle m'observe un peu trop longtemps."
    lysa reflechit "Tu vas bien ?"
    noam neutre "Je suis fatigué."
    lysa neutre "C'est pas la question."
    "Je n'ai pas envie de lui mentir. Je n'ai pas non plus envie de lui répondre."
    noam hesitation "Je cherche encore des choses. J'en trouve pas beaucoup."
    lysa reflechit "Le dessin ?"
    noam neutre "Pas seulement."
    "Elle ne demande pas lesquelles."
    lysa neutre "D'accord. Si tu veux parler, évite juste de tomber avant d'arriver à ma porte. Ça devient pénible."
    noam sourire "Je vais essayer."
    "Elle rentre dans sa chambre. Je reste encore un instant dans le couloir."
    think "Elle m'aurait laissé parler. J'en suis sûr."
    think "Pourquoi est-ce que ça ne m'aide pas à me sentir mieux ?"
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_48
    scene bg_chambre at adaptive_fullscreen with fade
    "Je ferme la porte et m'assieds sur le lit."
    "La chaise du bureau est toujours à sa place. Je me souviens l'avoir bloquée contre la poignée avant de dormir. Je me souviens aussi de la photo de Léa, du dessin de Juliette, des batteries qu'Elias cherchait."
    think "Des objets disparaissent. Des données disparaissent aussi."
    noam reflechit "Et moi, je ne suis même pas capable de dire ce que j'ai vu."
    "Je prends ma tablette pour noter ce que Kami a dit. « Accès autorisé ». « Données supprimées ». « Sept jours »."
    "Je relis ma liste."
    think "Aucune de ces trois phrases ne prouve qu'un représentant a fait quoi que ce soit."
    "Je repose la tablette sur le bureau, à l'endroit où le dessin aurait dû se trouver."
    noam fatigue "Juliette..."
    "Je repense à Iris qui s'est endormie au bord du matelas, à Sael qui m'a obligé à boire, à Julian qui a failli renverser un plateau sur moi."
    think "Tout ça s'est vraiment passé. Leurs gestes ne disparaissent pas parce que Kami a décidé de me faire peur."
    "Je commence à retirer ma veste."
    "Un bruit de pas passe devant la porte."
    "Je m'immobilise."
    pause 1.0
    "Les pas s'éloignent. Quelqu'un doit simplement regagner sa chambre."
    noam taquin "Très bien. Demain, je soupçonnerai le couloir de comploter contre moi."
    "Je n'arrive pas à rire."
    "Je me couche sans bloquer la porte avec une chaise. Après quelques secondes, je me redresse pour vérifier le verrou."
    think "C'est fermé."
    "Je vérifie une deuxième fois."
    scene black with fade
    stop music fadeout 4.0
    call end_day("12", sleeping=True) from _call_end_day_2
    jump _12_0_1_1_REVEIL_CHAMBRE
