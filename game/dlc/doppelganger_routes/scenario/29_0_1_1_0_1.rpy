# JOUR 29 — LE DERNIER MENSONGE
# Route alternative : Noam enquête sur l'assassinat de Tomas.
default j29a_reconstitution = 0
default j29a_erreurs = 0
default j29a_mobile = ""
default j29a_badge_nyra = False
default j29a_signal = False
default j29a_objections = 0
default j29a_accuse = ""
default j29a_contradiction = False
default j29a_nyra_detained = False

label _29_0_1_1_0_1_REVEIL:
    $ current_day = 29
    $ day_id = 29
    $ current_period = "Matin"
    $ j29a_reconstitution = 0
    $ j29a_erreurs = 0
    $ j29a_mobile = ""
    $ j29a_badge_nyra = False
    $ j29a_signal = False
    $ j29a_objections = 0
    $ j29a_accuse = ""
    $ j29a_contradiction = False
    $ j29a_nyra_detained = False
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 0.8
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille avec mes notes sur la tablette. Je les ai relues jusqu'à une heure impossible, et j'ai pas plus de certitudes qu'hier."
    "Tomas est mort. On a trouvé un dispositif derrière la ventilation de la chambre où il dormait. Je sais toujours pas qui a pu faire ça."
    noam fatigue "Bon. Faut arrêter de tourner en rond."
    "Le départ pour la Terre approche. Si on ne trouve rien aujourd'hui, j'ai peur qu'on n'arrive jamais à reprendre toute cette histoire."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j29a_door1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    jump _29_0_1_1_0_1_INFIRMERIE
# Durée : ~50 s.

label _29_0_1_1_0_1_INFIRMERIE:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie2", "infirmerie2") from _call_j29a_door2
    scene infirmerie2 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("iris", "fatigue", 0.22), ("lysa", "neutre", 0.45), ("noam", "neutre", 0.70)])
    iris fatigue "Je vais le dire une fois, parce que je sais comment ça se passe avec toi."
    noam neutre "Bonjour à toi aussi."
    iris raison "Les derniers résultats sont compatibles avec une intoxication par inhalation. Et les résidus de la chambre ressemblent à ce qu'on a prélevé dans le conduit."
    lysa reflexion "Donc c'est le bol ?"
    iris agace "C'est compatible. J'ai pas un laboratoire complet ici, et ça me permet pas de déterminer une substance avec certitude."
    noam reflexion "Mais le suicide ?"
    iris raison "Franchement, vu le montage dans la ventilation, je trouve l'homicide beaucoup plus probable."
    lysa inquiet "Et les somnifères ?"
    iris neutre "On a toujours aucune preuve qu'il ait pris ce qu'il y avait dans le flacon. Il a pu être laissé là exprès. Il a aussi pu être là avant."
    noam fatigue "Ça me rend dingue."
    iris fatigue "Moi aussi. Mais si je commence à inventer des certitudes pour te faire plaisir, ça servira à rien."
    lysa raison "On va reprendre les événements avec Nyra."
    iris inquiet "Faites ça. Et si vous pensez trouver un coupable, trouvez quelque chose de concret. Pas juste quelqu'un qui vous plaît pas."
    noam raison "D'accord."
    iris triste "J'aurais aimé faire mieux pour Tomas."
    noam neutre "T'as pas arrêté depuis trois jours. On le sait."
    $ hideGroup()
    jump _29_0_1_1_0_1_RECONSTITUTION
# Durée : ~2m00.

label _29_0_1_1_0_1_RECONSTITUTION:
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 0.8
    "Nyra a mis nos notes dans l'ordre sur deux tablettes. Ça fait un drôle d'effet de voir les dernières heures de Tomas réduites à une liste."
    $ showGroup([("lysa", "neutre", 0.22), ("nyra", "neutre", 0.45), ("noam", "neutre", 0.70)])
    nyra raison "On sait certaines choses. D'autres, on les suppose. Si on mélange, on va accuser n'importe qui."
    noam neutre "On fait comment ?"
    lysa blase "Tu lis ce qui est écrit et tu essaies de pas te planter."
    noam taquin "Merci, c'est gentil."
    nyra sourire "Elle a pas tort."
    "Je reprends la chronologie. Pour chaque étape, je dois choisir ce qu'on peut réellement déduire."
    jump _29_0_1_1_0_1_RECON_MENU
# Durée : ~1m00.

label _29_0_1_1_0_1_RECON_MENU:
    if j29a_reconstitution == 4:
        jump _29_0_1_1_0_1_MOBILE
    if j29a_reconstitution == 0:
        menu:
            "Quel événement est certain ?"
            "Elen et Tomas ont échangé leurs chambres.":
                $ j29a_reconstitution = 1
                noam raison "Je les ai vus parler. Elen a confirmé qu'ils avaient échangé."
                nyra neutre "Ça, on peut le garder."
            "Tomas avait décidé de se suicider.":
                $ j29a_erreurs += 1
                lysa agace "On en sait rien. C'est justement ce qu'on vérifie."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 1:
        menu:
            "Comment expliquer la chambre fermée ?"
            "Une substance a pu entrer par la ventilation.":
                $ j29a_reconstitution = 2
                noam raison "Le verrou ne protège pas de ce qui passe par l'air."
                nyra neutre "C'est possible. Pas encore démontré pour cette nuit."
            "Quelqu'un a forcément forcé le verrou.":
                $ j29a_erreurs += 1
                lysa raison "Elias a forcé le verrou devant nous. Rien ne montrait qu'il avait été abîmé avant."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 2:
        menu:
            "Que permettent de dire les résultats médicaux ?"
            "L'intoxication par inhalation est plausible et l'homicide probable.":
                $ j29a_reconstitution = 3
                noam raison "C'est ce que dit Iris. Pas plus."
                nyra raison "OK."
            "Les somnifères prouvent le suicide.":
                $ j29a_erreurs += 1
                lysa blase "Non, Noam. Iris a littéralement passé trois jours à nous dire le contraire."
        jump _29_0_1_1_0_1_RECON_MENU
    if j29a_reconstitution == 3:
        menu:
            "Qu'est-ce qu'il manque encore ?"
            "L'identité de celui qui a préparé le dispositif et son mobile.":
                $ j29a_reconstitution = 4
                noam raison "On a une méthode possible. Pas un coupable."
                nyra neutre "Voilà. On avance."
            "Le nom de celui qui a ouvert la porte de l'intérieur.":
                $ j29a_erreurs += 1
                lysa raison "Personne n'avait besoin d'ouvrir si le dispositif était déjà dans les conduits."
        jump _29_0_1_1_0_1_RECON_MENU
# Durée : ~3m00, selon les tentatives.

label _29_0_1_1_0_1_MOBILE:
    $ current_period = "Après-midi"
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("lysa", "reflexion", 0.21), ("nyra", "neutre", 0.45), ("noam", "neutre", 0.69)])
    lysa reflexion "Julian et Ryn lui en voulaient. Il a reçu des menaces sur Terre. C'est quand même pas rien."
    noam raison "Mais il cherchait Keyper et il avait trouvé cet appareil dans l'observation."
    nyra reflexion "Les deux pistes existent. On ne peut pas savoir laquelle a un lien avec sa mort, pour l'instant."
    menu:
        "Quelle piste approfondir en premier ?"
        "Les représailles liées au vote":
            $ j29a_mobile = "vote"
            noam raison "On reprend les menaces et les disputes. C'est le plus évident."
            lysa raison "D'accord. Mais après, on retourne voir les éléments techniques."
        "Le secret que Tomas avait découvert":
            $ j29a_mobile = "secret"
            noam raison "Je voudrais comprendre pourquoi ses recherches auraient pu déranger quelqu'un."
            nyra raison "D'accord. Sans oublier les gens qui le détestaient pour son vote."
    "Mon téléphone vibre. C'est Kael : il a trouvé un relevé dans la maintenance."
    noam surpris "Kael veut nous montrer quelque chose."
    nyra neutre "J'allais regarder de mon côté dans les archives. Je vous rejoins après."
    lysa raison "OK. On y va."
    $ hideGroup()
    jump _29_0_1_1_0_1_MAINTENANCE
# Durée : ~1m30.
