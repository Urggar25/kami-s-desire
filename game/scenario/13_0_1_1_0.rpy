label _13_0_1_1_0_REVEIL_CHAMBRE:
    call show_chapter_title("Début du chapitre 5", "Chapitre 5 — Les apparences sont trompeuses") from _call_show_chapter_title_19

    $ cafeteria_food_level = "none"
    $ current_period = "Matin"
    $ current_day = 13
    $ noam_has_juliette_drawing = False

    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0
    play sound sfx_metal_clank volume 0.7

    "Un choc métallique contre le mur me réveille."
    "Un robot de maintenance est déjà devant le brouilleur. Deux bras retiennent le boîtier pendant qu'un troisième retire les vis."

    call kd_vn_cg_impact("#dbe9ff")
    scene bg_cg032 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg032")

    noam panique "Qu'est-ce que tu fais ?!"

    "Le robot tourne la tête sans arrêter son travail."
    robot "Bonjour. Je retire votre brouilleur."
    noam colere "Je vois bien que tu le retires ! Pourquoi ?"
    robot "Décision du Conclave. Les dispositifs de brouillage ne sont plus autorisés dans les chambres des représentants."
    "Un câble résiste, puis cède."
    noam panique "Attends. Le vote a échoué ?"
    robot "Oui."
    noam inquiet "Quelqu'un a voté contre ?"
    robot "Une personne. L'unanimité n'a pas été atteinte."
    think "Kael ? Après ce qui est arrivé à sa photo, il aurait pu changer d'avis."
    noam reflexion "Tu sais qui ?"
    robot "Oui."
    noam agace "Et tu comptes me le dire ?"
    robot "Et je ne suis pas autorisé à vous le dire."
    noam colere "Tu entres dans ma chambre pendant que je dors, mais le nom d'un votant, ça, c'est confidentiel ?"
    robot "Exactement. Vous comprenez vite une fois réveillé."
    "Les panneaux du brouilleur s'empilent dans son compartiment. Je n'avais jamais remarqué à quel point ce boîtier occupait peu de place."
    noam fatigue "Et Kami peut déjà voir ici ?"
    robot "Pas encore. La reconnexion complète sera effective quelques minutes après mon départ."
    noam inquiet "Après, elle pourra regarder quand elle veut ?"
    robot "Oui."
    noam inquiet "Même la nuit ?"
    robot "Oui."
    noam colere "Même quand on se change ?"
    robot "Oui."
    robot "Si cela peut vous rassurer, vous êtes douze. Elle aura donc probablement autre chose à regarder de temps en temps."
    noam colere "Ça ne me rassure absolument pas."
    robot "Je m'en doutais."
    "Le dernier panneau se détache. Derrière, il ne reste qu'une cavité et quelques fils."
    noam reflexion "Laisse-moi le boîtier."
    robot "Non."
    noam agace "Pourquoi ?"
    robot "Parce qu'un brouilleur laissé dans une chambre peut être réparé. Un brouilleur emporté, beaucoup moins."
    noam desaccord "Et si je refuse ?"
    robot "Alors vous refusez une décision qui est déjà appliquée. Votre refus ne change rien à mon intervention."
    noam fatigue "Formidable."
    robot "Je préfère aussi quand les résidents disent merci. Je travaille avec ce qu'on me donne."
    noam agace "Tu pouvais attendre que je sois réveillé."
    robot "J'ai essayé."
    noam reflexion "Comment ça ?"
    robot "Une vis est tombée sur votre front. Vous n'avez pas réagi."
    "Je touche la bosse au-dessus de mon sourcil."
    noam colere "Tu m'as réveillé en me lançant une vis dessus ?"
    robot "Elle est tombée. La nuance est importante pour le rapport."
    robot "Intervention terminée. J'ai encore plusieurs chambres à traiter."
    noam fatigue "Alors va-t'en."
    robot "Avec plaisir. L'ambiance était meilleure dans la chambre précédente."
    "Il roule jusqu'à la porte, puis pivote une dernière fois."
    robot "Dernière information : la surveillance centrale sera rétablie automatiquement. Ne tentez pas de toucher aux connexions laissées dans le mur."
    noam agace "Sinon quoi ?"
    robot "Sinon je devrai revenir. Et je crois que ni vous ni moi n'avons envie de ça."
    "Il disparaît dans le couloir. Quelques secondes plus tard, le même cliquetis recommence devant une autre chambre."

    scene bg_chambre at adaptive_fullscreen with fade

    "Je reste sur le lit face au trou dans le mur. Hier, j'ai quitté le vote. Aujourd'hui, tout le monde paie le résultat."
    "Je prends ma veste, puis regarde les murs. Aucun objectif visible. Aucun voyant. Rien qui indique si la reconnexion est terminée."
    "Je me tourne pour me changer. Un grésillement sort aussitôt de l'écran mural."

    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu sais que te tourner ne change rien, Noam ?"
    $ bc_show("noam", "colere")
    noam colere "Tu pourrais prévenir avant de regarder."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Et rater le moment où tu fais semblant d'avoir encore de l'intimité ? Non."
    noam desaccord "Va te faire voir."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Techniquement, c'est plutôt toi que je peux voir. Bonne journée !"
    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je finis de m'habiller. Elle voit la chambre. Pourtant, quelqu'un a déjà réussi à voler ici et à effacer une caméra."
    think "Donc soit Kami ment, soit elle ne contrôle pas tout."

    call KD_EXTRA_J13_LYSA from _call_kd_extra_j13_lysa
    jump _13_0_1_1_CAFETERIA

    # Durée : 3m10 + scène optionnelle

label _13_0_1_1_CAFETERIA:
    call KD_ROUTE_J13_JULIAN from _call_optional_kd_route_j13_julian
    call START_EXPLORATION_LIBRE("_13_0_1_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_nav_j13_cafeteria

label _13_0_1_1_CAFETERIA_ARRIVEE:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_69
    pause 1.0
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.5

    "La cafétéria est pleine. Les plateaux, eux, sont vides."
    "Quand j'entre, les conversations baissent juste assez pour que je le remarque."

    $ showGroup([
        ("noam", "neutre", 0.00),
        ("mara", "colere", 0.15),
        ("elen", "triste", 0.35),
        ("iris", "inquiet", 0.55),
        ("julian", "hesitation", 0.75),
        ("sael", "mefiant", 0.90),
    ])

    "Goumi attend derrière le comptoir, seul avec une cafetière presque vide. Les étagères derrière lui sont nues."

    noam fatigue "Dis-moi qu'il reste quelque chose."
    goumi vide "Du café. Une tasse par personne."
    noam surpris "Même pas du pain ?"
    goumi vide "Si tu en trouves, je te l'achète."
    julian hesitation "Je retire donc ma proposition de faire du café un droit fondamental."

    "Personne ne rit. Mara pose sa tasse d'un coup sec."

    mara colere "Tu peux la garder pour le prochain vote. Si Noam reste jusqu'au bout, cette fois."
    noam fatigue "Bonjour, Mara."
    mara colere "J'ai faim, Kami peut me mater dans ma chambre et toi, tu nous as plantés hier. Alors non, pas bonjour."
    iris inquiet "Tu peux lui parler sans lui sauter à la gorge."
    mara agace "Toi, peut-être. Moi, j'ai pas mangé."

    "Goumi me sert une tasse. Elen garde les yeux sur la sienne."

    elen triste "Pourquoi tu es parti ?"
    noam fatigue "Parce que j'avais peur."

    "Elle relève la tête. J'avais préparé une excuse pendant tout le trajet. Elle ne sort pas."

    noam culpabilite "J'ai commencé à vous regarder comme si l'un de vous allait me tomber dessus. J'ai paniqué, je vous ai accusés et je suis parti."
    mara agace "Ça, on avait remarqué."
    elen inquiet "Tu pensais vraiment qu'on voulait te faire du mal ?"
    noam hesitation "Sur le moment... oui."
    sael mefiant "Et maintenant ?"
    noam fatigue "Maintenant, j'essaie surtout de comprendre ce qui m'arrive."
    sael raison "Alors fais-le avant le prochain vote. Tes crises ont des conséquences pour tout le monde."
    noam culpabilite "Je sais."

    "Sael hoche la tête, sans me pardonner à la place des autres."

    elen triste "Le robot a retiré le mien pendant que j'étais sous la douche."
    iris colere "Il est entré ?"
    elen triste "Il a dit qu'il ne regardait pas. Je sais même pas pourquoi ça m'a rassurée."
    elen triste "Je voulais juste pouvoir fermer ma porte et pleurer sans avoir un public."

    call play_stat_dialogue("j13") from _call_play_stat_dialogue_12

    noam culpabilite "Je suis désolé, Elen. Pour le vote. Et pour hier."
    elen triste "Je suis encore en colère."
    noam calme "Tu as le droit."
    elen hesitation "Mais je préfère ça à une autre excuse."

    "Ce n'est pas un pardon. C'est déjà plus que ce que je mérite."

    mara agace "Très touchant. On peut revenir au fait qu'on n'a rien à bouffer ?"
    goumi vide "La livraison arrive demain."
    mara mefiant "Si elle arrive."
    julian blase "Elle arrivera. Sinon, Mara mangera la table et le problème se réglera de lui-même."
    mara colere "Je commence par ta chaise."

    "Cette fois, Iris étouffe un rire. La tension ne disparaît pas, mais elle recule d'un pas."

    "Je m'assois face à Elen. Iris prend la chaise voisine et se penche vers moi."

    iris inquiet "Maintenant qu'on a eu la version honnête : qu'est-ce que tu caches ?"
    noam hesitation "Iris..."
    iris agace "Depuis ton malaise, tu vérifies les couloirs derrière toi. Hier, tu as explosé sans pouvoir dire pourquoi. Je suis inquiète, pas idiote."
    noam fatigue "Il y a des choses qui ne collent pas. J'arrive pas encore à les relier."
    iris reflexion "Quelles choses ?"

    "Le couloir. Les images effacées. Les objets volés. Si je lui donne tout en vrac, je vais recommencer exactement comme hier."

    noam hesitation "Laisse-moi les remettre dans l'ordre. Après, je t'en parle."
    iris desaccord "Tu as intérêt."
    elen inquiet "Et tu ne pars pas sans prévenir, cette fois."
    noam calme "D'accord."

    goumi vide "Noam ?"

    "Depuis le comptoir, Goumi désigne ma tasse."

    goumi vide "Tu n'en prends pas une deuxième."
    noam surpris "Tu viens de me servir la première."
    goumi vide "Non. Je t'en ai donné une tout à l'heure."

    "Il s'interrompt. Son regard passe de la tasse à mon visage."

    noam inquiet "Je viens de me lever."
    goumi vide "Alors j'ai confondu."
    noam inquiet "Avec qui ?"
    goumi vide "J'en sais rien. Quelqu'un de dos, avec ta veste. J'ai dormi trois heures, oublie."

    think "Ma veste. Pas seulement mon visage."

    iris inquiet "Noam ?"
    noam hesitation "Je dois vérifier quelque chose."
    iris agace "Tu viens de promettre de parler."
    noam calme "Et je le ferai. Mais pas avec une impression de plus."

    "Je pose la tasse. Elen ne me retient pas, mais son regard me suit jusqu'à la porte."

    jump _13_0_1_1_DISCUSSION_ECOUTEE

label _13_0_1_1_DISCUSSION_ECOUTEE:

    "Je quitte la cafétéria. Derrière moi, les conversations reprennent à voix basse."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_70
    pause 1.0
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Au prochain croisement, la voix de Ryn me fait ralentir. Je m'arrête avant l'angle, hors de leur vue."

    play music "music/bgm_system_override.mp3" fadein 2.5

    ryn colere "Au prochain vote, je veux savoir s'il compte encore nous faire son numéro."
    elias fatigue "Tu veux qu'on lui demande une autorisation avant chaque phrase ?"
    ryn colere "Je veux qu'on arrête de tout lui raconter. Hier, il nous traite de traîtres et il se barre."
    tomas inquiet "Si on commence à lui cacher des choses, il va juste se méfier encore plus."
    ryn agace "Et si on continue comme avant, il nous fait rater quoi la prochaine fois ?"
    elias reflexion "On peut lui parler en face. Ça existe encore."
    ryn colere "Iris a essayé. Elen aussi. Il répond rien."
    tomas hesitation "Peut-être qu'il ne sait pas comment le dire."
    ryn hesitation "Ou qu'il cache quelque chose."
    elias fatigue "Il cache quelque chose. Ça se voit."
    nyra raison "Ça ne veut pas dire qu'il a tort."

    "Personne ne répond tout de suite."

    ryn surpris "Tu le défends, maintenant ?"
    nyra neutre "Non. Je distingue deux problèmes. Sa façon d'agir est mauvaise. Ce qu'il a remarqué peut quand même être réel."
    elias agace "Il a accusé la moitié de la salle au hasard."
    nyra raison "Oui. C'était stupide. Ça ne prouve pas qu'il a tout inventé."
    tomas reflexion "Tu penses qu'il a vu quelque chose ?"
    nyra hesitation "Je pense qu'on ne peut pas l'écarter juste parce qu'il l'explique mal."
    ryn colere "Moi, j'écarte rien. Mais sa prochaine crise, je veux pas la découvrir pendant un vote."
    elias fatigue "Là-dessus, on est d'accord."

    "Je recule avant qu'ils me surprennent."

    think "Ils ne me font plus confiance. Et je leur donne de bonnes raisons."
    think "Cette fois, je pars des faits. Pas des visages."

    call KD_ROUTE_J13_ELIAS from _call_optional_kd_route_j13_elias
    call OFFER_DAILY_EXPLORATION(
        "_13_0_1_1_CHAMBRE_PAPIER", 2,
        ["archive", "cafeteria", "observation", "dortoir"],
        _("Retourner mettre les faits en ordre"), "dortoir"
    ) from _call_offer_exploration_j13

label _13_0_1_1_CHAMBRE_PAPIER:

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_71
    pause 1.0
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_cold_metadata.mp3" fadein 2.5

    "Je ferme ma porte, puis regarde le trou laissé par le brouilleur. Le verrou ne sert plus à grand-chose."
    "Au bureau, je trace trois colonnes sur une feuille."

    noam murmure "Certain. Possible. Inexplicable."

    "Dans la première : matériaux disparus, photo de Léa volée, dessin de Juliette volé, images du couloir effacées."

    $ investigation_add("materiel_technique_manquant", notify=False)
    $ investigation_add("photo_lea_disparue", notify=False)
    $ investigation_add("dessin_juliette_disparu", notify=False)

    "Dans la deuxième : la silhouette, mes souvenirs qui ne collent pas, Goumi convaincu de m'avoir déjà servi."

    $ investigation_add("silhouette_couloirs", notify=False)
    $ investigation_add("kami_hors_ligne", notify=False)

    think "Une erreur de Goumi, ça arrive. Avec tout le reste, je ne peux plus juste l'oublier."

    "La troisième colonne reste vide. Je reviens aux vols. Les matériaux peuvent servir. La photo et le dessin, non."
    think "Deux images de personnes qu'on aime."

    $ investigation_refresh_hypotheses()

    "J'écris : Pourquoi voler une image ?"
    "Puis : Qui peut effacer les caméras de Kami ?"

    think "Ce n'est pas une réponse. Au moins, ce ne sont plus des accusations."

    "Je sors mon cahier noir pour recopier les deux questions. À la troisième page, ma main s'arrête."

    play sound "audio/sfx_audio_drop.wav"

    $ investigation_add("copie_dessin")

    "Le dessin de Juliette est là. Pas l'original : une copie presque parfaite, tracée directement dans mon cahier."
    noam peur "Non..."

    "Je vérifie les pages voisines. Rien. Je n'ai pas ouvert ce cahier depuis plusieurs jours."
    "Je rapproche la copie de la lampe. Quelque chose me gêne dans son visage."

    call j13_sept_differences_run from _call_j13_sept_differences
    $ investigation_add("cicatrice_juliette")

    "Sous ses cheveux, la copie montre sa cicatrice."

    think "Sur mon dessin, elle était cachée."
    think "Et je n'en ai jamais parlé ici."

    "Je regarde la porte, puis le mur. Quelqu'un est entré dans ma chambre, a pris mon dessin, a ouvert mon cahier et connaissait un détail que personne au Conclave ne devrait connaître."

    noam murmure "Comment tu savais...?"

    "Je pose le cahier dans la troisième colonne et écris dessous : quelqu'un connaît mes souvenirs."
    "Puis je photographie la page avec ma tablette. Cette fois, si elle disparaît, il restera une copie à moi."

    "Je garde le cahier sous mon oreiller et m'allonge sans me déshabiller. Au moindre bruit, j'ouvre les yeux."
    "Quand le sommeil finit par venir, il ne dure jamais longtemps."

    # Durée : 12m40 + exploration et scènes optionnelles

    call end_day("14", sleeping=True) from _call_end_day_4
    jump _14_0_1_1_0_REVEIL_CHAMBRE
