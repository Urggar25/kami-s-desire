# Branche du Commandement rejeté ; récit strictement limité au point de vue de Noam.
default j25_01_appareil_remarque = False
default j25_01_nyra_croisee = False
default j25_01_contact_tomas = False
default j25_01_discussion = None

label _25_0_1_1_0_1_REVEIL:
    call show_chapter_title("Début du chapitre 8", "Chapitre 8 — Le Bouc émissaire") from _call_show_chapter_title_9
    $ current_day = 25
    $ day_id = 25
    $ current_period = "Matin"
    $ j25_01_appareil_remarque = False
    $ j25_01_nyra_croisee = False
    $ j25_01_contact_tomas = False
    $ j25_01_discussion = None
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    $ blink()
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je me réveille un peu avant l'alarme. Ma tablette est encore ouverte sur le résultat d'hier."
    "Le Commandement n'a pas été adopté. Une voix contre."
    think "Putain, Tomas..."
    "Je repense aux archives. Au tableau de production. À cette ligne qu'on comprenait pas."
    think "Keyper-IIB."
    "Je sais toujours pas si j'ai bien fait de lui proposer de regarder les chiffres. En fait, je sais même pas ce que j'aurais fait à sa place."
    "Un rappel indique qu'un nouveau vote aura lieu au jour 27. Pas encore de sujet."
    noam fatigue "On n'a même pas fini celui-là..."
    "Je regarde machinalement la grille d'aération, puis j'attrape mon téléphone."
    "Aujourd'hui, je vais surtout voir si Tomas a réussi à dormir."
    stop music fadeout 0.7
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j25_01_door_1
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Je croise Elias, avec deux cafés dans les mains."
    $ showGroup([("elias", "fatigue", 0.35), ("noam", "neutre", 0.65)])
    noam surpris "Deux cafés ?"
    elias fatigue "Le premier est dégueulasse."
    noam reflexion "Alors pourquoi t'en as repris ?"
    elias neutre "J'ai demandé à Goumi d'en refaire un."
    noam taquin "Et ?"
    elias fatigue "Il est pareil."
    noam sourire "Bonne journée."
    elias fatigue "Ouais, c'est ça."
    $ hideGroup()
    jump _25_0_1_1_0_1_CAFETERIA
# Durée : 1m00 — Total : 1m00

label _25_0_1_1_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j25_01_door_2
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.7
    "La cafétéria est pleine, mais personne ne mange vraiment. Les autres regardent l'écran."
    $ showGroup([("tomas", "fatigue", 0.20), ("julian", "inquiet", 0.42), ("nyra", "neutre", 0.64), ("noam", "neutre", 0.86), ("elen", "inquiet", 1.08), ("ryn", "colere", -0.03)])
    noam inquiet "Qu'est-ce qu'il y a ?"
    elen inquiet "Kami. Regarde."
    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5
    scene bg_diffusion_professeur at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonjour, mes chers représentants ! Bien dormi ?"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Il paraît que certains sur Terre n'ont pas eu cette chance. Mais je suppose que vous savez pourquoi !"
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Depuis le rejet de votre petite proposition d'hier, des manifestations ont éclaté dans plusieurs districts."
    "L'écran montre une foule immense, des gens devant des barrières de sécurité, des pancartes où il est question d'eau, de nourriture et de logements."
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Regardez-moi ça ! Vous avez réussi à mettre beaucoup de monde d'accord. Contre vous, certes, mais quand même."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je vous donnerai des nouvelles. Vous avez l'air tellement curieux."
    hide screen kami_broadcast_ui
    stop music fadeout 0.7
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.8
    $ showGroup([("tomas", "stress", 0.15), ("julian", "colere", 0.36), ("nyra", "neutre", 0.57), ("noam", "inquiet", 0.77), ("elen", "inquiet", 0.98), ("ryn", "colere", -0.04), ("iris", "blase", 1.16), ("lysa", "blase", 0.05)])
    julian colere "Voilà. Vous êtes contents ?"
    noam agace "Bonjour à toi aussi."
    julian agace "Non, sérieusement. Regarde ce qui se passe."
    tomas fatigue "J'ai vu."
    ryn colere "Et tu penses toujours que t'as eu raison ?"
    tomas hesitation "C'est pas... Je sais pas encore."
    julian colere "Tu sais pas ?!"
    tomas fatigue "J'essaie de savoir ce que c'est, Keyper. C'est tout."
    julian agace "Pendant ce temps-là, y'a des gens dehors qui avaient besoin de ce Commandement !"
    noam raison "On sait. Lui aussi, il sait."
    julian colere "Tu vas encore le défendre ?"
    noam agace "Je vais surtout vous demander de le laisser finir une phrase."
    ryn desaccord "Il a eu toute la journée d'hier pour parler."
    tomas colere "Mais j'ai parlé ! Vous m'avez pas écouté !"
    iris blase "Vous allez vraiment recommencer avant même que j'aie pris mon café ?"
    julian colere "Iris, c'est sérieux."
    iris neutre "C'est justement pour ça que vous pourriez éviter de hurler."
    nyra raison "Tomas avait le droit de voter contre. On peut lui dire qu'on n'est pas d'accord sans lui tomber dessus à chaque repas."
    ryn agace "Son droit, ça règle rien."
    nyra neutre "Non. Mais les cris non plus."
    julian colere "On ne lui interdit pas de parler !"
    lysa blase "Non, vous l'empêchez juste de répondre. C'est différent."
    tomas fatigue "Laissez tomber."
    elen inquiet "Tomas, tu veux pas manger un peu ?"
    tomas colere "Non ! J'ai pas faim !"
    pause 0.4
    tomas fatigue "Désolé, Elen. Je voulais pas..."
    elen neutre "C'est rien."
    "Il pousse son assiette et quitte la salle. Personne ne bouge."
    $ showGroup([("julian", "agace", 0.21), ("nyra", "neutre", 0.43), ("noam", "inquiet", 0.66), ("elen", "triste", 0.89), ("lysa", "blase", 0.06)])
    julian agace "Génial. On peut même plus discuter."
    noam colere "C'était pas une discussion, Julian."
    nyra reflexion "Laisse-le se calmer. Tu pourras lui reparler plus tard."
    julian fatigue "Vous croyez que ça va tout arranger ?"
    lysa blase "Personne a dit ça."
    "Je regarde l'assiette que Tomas a laissée. Elle est presque pleine."
    $ hideGroup()
    jump _25_0_1_1_0_1_ARCHIVES
# Durée : 2m30 — Total : 3m30

label _25_0_1_1_0_1_ARCHIVES:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Je fais un détour par les archives. Si Tomas a disparu après le petit-déjeuner, c'est probablement là qu'il est allé."
    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_j25_01_door_3
    scene bg_archive at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.7
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "neutre", 0.65)])
    tomas reflexion "Non, ça peut pas être la bonne référence..."
    noam neutre "Salut."
    tomas surpris "Ah ! Salut."
    noam inquiet "Ça va un peu mieux ?"
    tomas fatigue "Franchement ? Non."
    noam neutre "OK."
    "Il a ouvert les mêmes tableaux que la veille. Trois autres fenêtres sont empilées par-dessus."
    noam reflexion "Tu cherches toujours Keyper ?"
    tomas raison "Ouais. J'ai essayé de retrouver des relevés plus anciens, mais c'est n'importe quoi."
    noam taquin "C'est grave, venant de toi."
    tomas fatigue "Je suis sérieux."
    noam neutre "Moi aussi. Enfin, presque."
    tomas inquiet "Tu as vu les manifestations ?"
    noam neutre "Ouais."
    tomas fatigue "Je sais pas si j'ai bien fait."
    noam raison "Tu croyais qu'il y avait un risque. T'as voté en fonction de ça."
    tomas reflexion "Mais si j'ai eu peur pour rien ? Si c'est juste une usine pleine de robots ?"
    noam neutre "Alors on le saura en cherchant."
    tomas fatigue "C'est bien ce que j'essaie de faire."
    noam reflexion "Tu sais où est la station ?"
    tomas raison "Pas encore. J'ai des références de trajets, des codes de livraison... Mais pas de coordonnées."
    noam raison "Y'a des cartes dans la salle d'observation, non ?"
    tomas surpris "Justement. Je voulais y aller."
    noam sourire "Ah. Pour une fois, tu m'as devancé."
    tomas fatigue "Tu comptes pas me le ressortir toute la journée ?"
    noam taquin "Ça dépend de mon humeur."
    tomas reflexion "Je vais essayer de retrouver Keyper là-bas. Il doit bien y avoir un moyen."
    noam neutre "Je te rejoins après. J'ai deux ou trois trucs à faire."
    tomas hesitation "Noam..."
    noam reflexion "Oui ?"
    tomas fatigue "Je voulais pas que tout le monde m'en veuille."
    noam raison "Je sais."
    tomas inquiet "Elen avait l'air vraiment déçue."
    noam neutre "Elle est surtout inquiète pour toi."
    tomas fatigue "Ouais... bon."
    "Il ferme ses documents et récupère sa tablette."
    tomas neutre "À tout à l'heure."
    "Je le laisse partir avec ses références de trajets."
    $ hideGroup()
    jump _25_0_1_1_0_1_PAUSE
# Durée : 1m30 — Total : 5m00

label _25_0_1_1_0_1_PAUSE:
    $ current_period = "Après-midi"
    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8
    "Dans la salle commune, Julian marche devant le canapé, Elen range des jeux, Lysa essaie de lire et Nyra consulte sa tablette."
    $ showGroup([("julian", "agace", 0.06), ("elen", "inquiet", 0.28), ("lysa", "blase", 0.50), ("nyra", "neutre", 0.72), ("noam", "neutre", 0.94)])
    julian agace "Je dis juste qu'il devrait expliquer son vote correctement."
    lysa blase "Tu l'as déjà dit."
    julian colere "C'est fou de pas pouvoir discuter avec vous !"
    elen neutre "On discute, là."
    noam fatigue "Dites, on pourrait parler d'autre chose cinq minutes ?"
    nyra sourire "J'allais le proposer."
    julian fatigue "Très bien. Je vais ailleurs."
    "Julian quitte la pièce. Cette fois, personne n'essaie de le retenir."
    $ showGroup([("elen", "inquiet", 0.22), ("lysa", "blase", 0.45), ("nyra", "neutre", 0.68), ("noam", "neutre", 0.90)])
    elen inquiet "Il est toujours comme ça quand il perd ?"
    lysa blase "J'aimerais pouvoir te dire non."
    nyra neutre "Il pense vraiment qu'on a laissé passer quelque chose d'important."
    noam reflexion "C'est pas une raison pour s'en prendre à Tomas."
    nyra raison "Non. Là-dessus, je suis d'accord avec toi."
    menu:
        "Avec qui passer un moment avant de rejoindre Tomas ?"
        "Avec Nyra":
            $ j25_01_discussion = "nyra"
            call _25_0_1_1_0_1_NYRA from _call_j25_01_nyra
        "Avec Elen":
            $ j25_01_discussion = "elen"
            call _25_0_1_1_0_1_ELEN from _call_j25_01_elen
        "Avec Lysa":
            $ j25_01_discussion = "lysa"
            call _25_0_1_1_0_1_LYSA from _call_j25_01_lysa
    jump _25_0_1_1_0_1_OBSERVATION
# Durée : 1m00 + entretien facultatif — Total : 6m00

label _25_0_1_1_0_1_NYRA:
    $ showGroup([("nyra", "neutre", 0.38), ("noam", "neutre", 0.67)])
    noam reflexion "T'as l'air de bien comprendre Tomas."
    nyra sourire "Je comprends surtout qu'on n'obtient rien en lui criant dessus."
    noam neutre "Ouais."
    nyra raison "Je suis pas d'accord avec son vote. Mais il était inquiet, il a essayé de vérifier. Tu voudrais vraiment qu'on lui reproche aussi ça ?"
    noam reflexion "Non."
    nyra sourire "Alors on est au moins deux."
    noam neutre "T'as déjà entendu parler de Keyper ?"
    nyra reflexion "De nom ? Non, pas vraiment."
    nyra neutre "Mais il y a énormément d'installations autour des routes d'Orbite. Pas étonnant qu'on les connaisse pas toutes."
    noam sourire "Tomas serait ravi de t'entendre dire ça."
    nyra taquin "Je vais éviter. Il va me demander de les lui énumérer une par une."
    noam rire "Ouais, probablement."
    return
# Durée : ~45 s

label _25_0_1_1_0_1_ELEN:
    $ showGroup([("elen", "inquiet", 0.38), ("noam", "neutre", 0.67)])
    elen inquiet "Je sais pas quoi faire pour Tomas."
    noam neutre "Tu peux lui parler. Normalement, sans lui demander de justifier son vote."
    elen reflexion "Ouais. J'ai voulu le défendre ce matin, mais j'ai rien trouvé."
    noam raison "T'es pas obligée d'avoir toujours une solution."
    elen triste "Je sais... Mais c'est nul de le laisser comme ça."
    noam sourire "Tu l'as déjà invité à manger ?"
    elen content "Oui ! Il m'a dit qu'il avait du travail."
    noam blase "Évidemment."
    elen sourire "Je lui garderai un truc pour ce soir."
    return
# Durée : ~45 s

label _25_0_1_1_0_1_LYSA:
    $ showGroup([("lysa", "blase", 0.38), ("noam", "neutre", 0.67)])
    noam reflexion "Tu crois qu'il a eu raison ?"
    lysa reflexion "Je sais pas. Je suis pas contente que le vote ait échoué, ça c'est sûr."
    noam neutre "Mais ?"
    lysa blase "Mais les tableaux de Kami me plaisent pas non plus. Des unités sans explication et des quotas qui montent... c'est bizarre."
    noam raison "Tomas cherche encore."
    lysa neutre "Je sais. Et il ferait mieux d'aller au bout, sinon on aura juste perdu un vote pour rien."
    noam fatigue "C'est encourageant."
    lysa blase "Je fais pas dans la motivation."
    return
# Durée : ~45 s

label _25_0_1_1_0_1_OBSERVATION:
    $ hideGroup()
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Je rejoins la salle d'observation. Tomas est déjà devant les pupitres."
    call MAYBE_PLAY_SCRIPTED_DOOR("observation", "bg_observation") from _call_j25_01_door_4
    scene bg_observation at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "reflexion", 0.35), ("noam", "neutre", 0.67)])
    "Il tient un petit appareil métallique avec une diode qui s'allume puis s'éteint. Il le tourne entre ses mains, comme pour trouver une référence."
    noam reflexion "C'est quoi, ça ?"
    tomas neutre "Aucune idée. Je l'ai vu posé près du pupitre."
    "Il repose l'objet sans faire d'histoire, puis retourne à l'écran."
    $ j25_01_appareil_remarque = True
    tomas raison "Bon. Je crois que j'ai une piste pour Keyper."
    noam surpris "Déjà ?"
    tomas fatigue "Ça fait trois heures que je suis là, Noam."
    noam taquin "Ah. Excuse-moi, monsieur le cartographe."
    tomas reflexion "Regarde."
    "Une carte de trajets s'affiche, avec plusieurs repères incomplets et une série de trajectoires qu'il a surlignées."
    tomas raison "J'ai repris les références de transport des archives. Si je me suis pas complètement planté, la station est dans ce secteur."
    noam surpris "Mais... c'est juste à côté !"
    tomas raison "Enfin, à côté, faut le dire vite. Il y en a pour plusieurs heures de vol, selon le vaisseau et la trajectoire."
    noam reflexion "Pas plusieurs jours ?"
    tomas neutre "Non. À priori non."
    noam raison "Donc une station de production dont personne nous a parlé est à quelques heures d'ici."
    tomas hesitation "Peut-être. Les coordonnées sont incomplètes. Je peux pas te donner une position exacte."
    noam neutre "C'est déjà mieux que rien."
    tomas reflexion "Je veux surtout savoir qui bosse là-bas. Les unités ÉID-0... Ça me sort pas de la tête."
    noam raison "Tu crois toujours que c'est des gens ?"
    tomas fatigue "Je sais pas. J'aimerais presque que ce soit des machines, au moins on pourrait arrêter de s'inquiéter."
    noam reflexion "Tu pourrais demander à Kael pour les trajets."
    tomas fatigue "Je sais. Mais là, j'ai vraiment pas envie de recommencer à devoir me justifier devant quelqu'un."
    noam neutre "Kael va pas te crier dessus."
    tomas reflexion "Ouais, mais je préfère trouver encore un peu de concret."
    noam sourire "OK. Mais tu viens dîner, ce soir."
    tomas fatigue "On verra."
    noam agace "Tomas."
    tomas sourire "D'accord, d'accord. Je viendrai."
    "Il jette un regard à ses notes. Je jette le mien vers le petit appareil. Il est toujours posé près du pupitre, sans rien de particulier."
    "Je quitte Tomas devant sa carte. Il a l'air un peu moins abattu que ce matin."
    $ j25_01_contact_tomas = True
    $ hideGroup()
    jump _25_0_1_1_0_1_SOIR
# Durée : 2m30 — Total : ~9m30

label _25_0_1_1_0_1_SOIR:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_j25_01_door_5
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.7
    "Je retrouve les autres à la cafétéria. Tomas mange un peu, assis loin de Julian."
    $ showGroup([("tomas", "fatigue", 0.18), ("elen", "neutre", 0.40), ("noam", "neutre", 0.62), ("nyra", "neutre", 0.84), ("julian", "agace", 1.06), ("mara", "taquin", -0.04)])
    mara taquin "Bon. On peut peut-être réussir à manger sans se balancer les assiettes à la gueule aujourd'hui."
    julian fatigue "Tu vas pas commencer."
    mara rire "C'est toi qui commences généralement."
    elen sourire "Tomas, j'ai gardé ton dessert."
    tomas surpris "Ah... merci."
    nyra sourire "Tu vois ? Tout le monde ne te déteste pas."
    tomas fatigue "Je préférerais éviter de le vérifier."
    noam sourire "Ça, c'est la meilleure chose que t'aies dite aujourd'hui."
    "Pour la première fois depuis ce matin, Tomas laisse échapper un petit rire."
    play sound sfx_announce
    $ hideGroup()
    stop music fadeout 0.5
    scene bg_diffusion_champagne at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Bonsoir, mes petits représentants ! J'ai de nouvelles images pour vous."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Les manifestations ont continué. Certaines ont dégénéré en affrontements avec les forces de sécurité."
    scene bg_diffusion_triste at adaptive_fullscreen with dissolve
    kami "Et il y a eu des morts. Plusieurs, même."
    "L'écran montre des gens qui courent, des blessés évacués et des rues couvertes d'objets abandonnés."
    "Au milieu des pancartes, l'une porte le nom de Tomas. Une autre exige qu'il ne revienne jamais sur Terre."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh. Il semblerait que quelqu'un ait retenu ton nom, Tomas."
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "À propos de décisions impopulaires, voici notre sujet du jour 27 !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "« Nul ne peut être sanctionné pour avoir exprimé une opinion ou pour son vote au sein d'une assemblée délibérante. »"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je suis sûre que vous allez tous adorer ce débat. On se retrouve dans deux jours !"
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "D'ici là, essayez de ne pas vous détester trop fort. Ça fait beaucoup de bruit."
    hide screen kami_broadcast_ui
    stop music fadeout 0.7
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_tense_meeting.mp3" fadein 0.7
    $ showGroup([("tomas", "stress", 0.17), ("elen", "inquiet", 0.38), ("noam", "inquiet", 0.59), ("nyra", "neutre", 0.80), ("julian", "colere", 1.01), ("ryn", "colere", -0.05), ("iris", "blase", 1.16)])
    elen peur "Des morts..."
    tomas peur "..."
    julian colere "On y est. Voilà où ça mène."
    noam agace "Julian, pas maintenant."
    julian agace "Tu peux pas me dire que ça a aucun rapport avec hier."
    tomas fatigue "J'ai pas dit ça."
    ryn colere "Alors dis quelque chose !"
    tomas colere "Quoi ?! Tu veux que je dise quoi ?"
    julian colere "Que t'as fait une erreur, déjà !"
    tomas stress "Je sais même pas encore si j'en ai fait une !"
    nyra raison "Arrêtez. Il n'a frappé personne dans ces manifestations."
    julian agace "Ça devient facile, de dire ça."
    nyra neutre "Et c'est facile de lui faire porter tous les morts sur le dos. Ça avance à quoi ?"
    iris agace "Vous vous entendez parler ?"
    elen inquiet "S'il vous plaît..."
    tomas fatigue "Vous avez vu ce qu'ils ont écrit ?"
    noam inquiet "Ouais."
    tomas stress "Ils veulent pas que je rentre sur Terre."
    noam raison "C'est des manifestants en colère. Pas la planète entière."
    tomas colere "Et qu'est-ce que t'en sais ?!"
    pause 0.3
    tomas fatigue "Pardon. Non, je peux pas. J'en ai marre."
    "Il recule sa chaise et sort sans toucher au dessert qu'Elen lui avait gardé."
    $ showGroup([("elen", "triste", 0.29), ("nyra", "neutre", 0.51), ("noam", "fatigue", 0.73), ("julian", "agace", 0.94), ("lysa", "blase", 0.07)])
    elen triste "Mais il allait mieux tout à l'heure..."
    julian fatigue "Je vais quand même pas m'excuser d'être en colère."
    lysa blase "Personne t'a demandé de t'excuser. Mais tu peux te taire cinq minutes."
    noam fatigue "Ça suffit. On va tous se coucher, ça ira mieux demain."
    nyra raison "Je crois aussi. Il vaut mieux lui laisser un peu d'air."
    elen inquiet "Je vais voir s'il a besoin de quelque chose."
    "Je reste un instant devant mon plateau, en écoutant les autres ranger leurs affaires."
    $ hideGroup()
    jump _25_0_1_1_0_1_DORTOIRS
# Durée : 2m30 — Total : ~12m00

label _25_0_1_1_0_1_DORTOIRS:
    $ current_period = "Nuit"
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 0.8
    "Quand je rejoins les dortoirs, j'aperçois Elen et Tomas, au loin, près des chambres."
    "Elle parle avec les mains comme elle le fait toujours. Tomas répond à voix basse. Je n'entends pas un seul mot."
    "J'hésite à aller les voir, puis je me ravise. Tomas a suffisamment eu droit à nos questions aujourd'hui."
    "Je continue et je manque de rentrer dans Nyra, qui traîne près du couloir des chambres."
    $ showGroup([("nyra", "neutre", 0.37), ("noam", "fatigue", 0.68)])
    nyra surpris "Oh, pardon."
    noam neutre "Non, c'est moi. Je regardais pas."
    nyra reflexion "Tout va bien ?"
    noam fatigue "Franchement ? Grosse journée."
    nyra neutre "Ouais. Ça se voit."
    noam reflexion "Tu fais quoi encore ici ?"
    nyra sourire "Je rentrais me coucher."
    noam neutre "Ah. Bonne nuit, alors."
    nyra raison "Tu sais, Tomas avait besoin qu'on l'écoute aujourd'hui. T'as bien fait."
    noam fatigue "J'ai pas l'impression que ça ait changé grand-chose."
    nyra neutre "On verra demain."
    nyra sourire "Bonne nuit, Noam."
    "Elle me dépasse et rejoint sa chambre. J'entends la porte se refermer."
    $ j25_01_nyra_croisee = True
    "Au fond du couloir, Elen et Tomas sont toujours en train de parler. Je ne les dérange pas."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_j25_01_door_6
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.7
    "Je pose mon téléphone près du lit. Le rappel du vote du jour 27 s'affiche une nouvelle fois."
    think "Interdire les sanctions pour un vote..."
    "Peut-être que ce serait utile. Peut-être qu'on arriverait quand même à se disputer à son sujet."
    "Je repense aux images de tout à l'heure. Aux pancartes. À Tomas qui regardait la carte de Keyper comme si elle pouvait lui donner une réponse."
    "J'espère qu'il va réussir à dormir cette nuit."
    "Je ferme les yeux."
    stop music fadeout 1.0
    call end_day("26", sleeping=True) from _call_j25_01_end_day_26
    jump _26_0_1_1_0_1_REVEIL
# Durée : ~1m00 — Total : ~13m00
