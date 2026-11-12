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
    kami "Mais bon… Je ne voudrais pas que le représentant d'[codex_dialogue_link('harmonie', 'Harmonie')] devienne totalement fou."
    kami "Que va en penser ta famille sinon ?!"

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

    call _11_0_1_3_MINIJEU_CAMERAS from _call__11_0_1_3_MINIJEU_CAMERAS

label _11_0_1_1_CONFRONTATION_KAMI:

    scene bg_observation at adaptive_fullscreen with dissolve

    "Je sélectionne enfin la bonne combinaison."
    "L’écran s’allume… puis devient noir en une fraction de seconde."
    "\"Données supprimées - Accès impossible\""
    $ investigation_add("videos_supprimees")

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
    kami "Regarde-les dans les yeux et demande-toi : lequel d’entre eux est capable de faire... ça..."
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
    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_47
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.bgm" fadein 3.0

    "Je sors de la salle d’observation sans un regard en arrière."
    "Mes jambes sont lourdes. Chaque pas résonne dans ma tête comme un marteau."

    think "Je ne veux voir personne."
    think "Ni Iris, ni Sael, ni Julian… personne."

    "Je marche droit vers ma chambre, ignorant les voix lointaines qui proviennent de la salle commune."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_48
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

    think "Mais le sommeil ne vient pas. Seulement un tourbillon de visages, de soupçons, et cette silhouette qui... Non."
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

    "Ou peut-être que je continuerai juste à me mentir à moi-même."

    scene black with fade
    stop music fadeout 4.0

    call end_day("12", sleeping=True) from _call_end_day_2
    jump _12_0_1_1_REVEIL_CHAMBRE

# Total journée : 11 minutes
# Durée totale : 2h41,50
