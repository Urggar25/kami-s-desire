label _17_0_1_1_0_ANNONCE_KAMI:

    $ cafeteria_food_level = "low"
    $ current_period = "Matin"
    $ current_day = 17
    $ noam_has_juliette_drawing = False

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.5

    "Je n'ai presque pas dormi. Chaque fois que je fermais les yeux, je revoyais la même ligne dans ce vieux livre des Archives."

    "Et puis le trou revient. La salle d'observation. Kael. Le couloir... et après, plus rien."

    noam inquiet "..."

    "Sael avait promis qu'on en parlerait aux autres dès le matin. Une partie de moi voudrait encore attendre, juste le temps de comprendre ce que M16 veut vraiment dire."
    "Mais après avoir vu la mention disparaître sous nos yeux, garder ça pour nous n'aurait plus eu aucun sens."

    noam reflexion "Il faut qu'ils sachent."

    "Je reste assis quelques secondes au bord du lit, puis je me lève. Mon crâne va mieux qu'hier. Le reste, beaucoup moins. J'ai toujours cette impression qu'il me manque quelque chose."

    jump _17_0_1_1_CAFETERIA_M16


label _17_0_1_1_CAFETERIA_M16:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_102
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je prends la direction de la cafétéria. Plus j'approche, moins j'ai envie d'y entrer. Je sais déjà que ça va partir en vrille dès qu'on parlera de M16."

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_103
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.0

    "Presque tout le monde est déjà là. Kael manque encore à l'appel, mais cette fois personne ne semble vraiment surpris."
    "Sael est debout près d'une table avec le vieux livre des Archives posé devant elle. Elle ne mange pas. Elle attend."

    $ showGroup([
        ("noam", "inquiet", -0.05),
        ("lysa", "blase", 0.06),
        ("ryn", "desaccord", 0.17),
        ("mara", "agace", 0.28),
        ("tomas", "neutre", 0.39),
        ("elen", "joie", 0.50),
        ("julian", "inquietude", 0.61),
        ("iris", "fatigue", 0.72),
        ("nyra", "reflexion", 0.83),
        ("elias", "inquiet", 0.94),
        ("sael", "neutre", 1.05),
    ])


    elen joie "Salut Noam ! J'allais justement prendre du café. Tu veux que je t'en—"

    sael neutre "Attends."

    "Elen se retourne vers elle, surprise. Sael pose une main sur le livre."

    sael "Avant de continuer, ouvrez vos dossiers médicaux."


    mara agace "Bonjour à toi aussi."

    iris fatigue "Pourquoi ?"

    sael "Cherchez une mention. M16."

    "Le ton qu'elle emploie suffit à faire disparaître les quelques conversations encore en cours."


    elias inquiet "C'est quoi, M16 ?"

    sael "Regardez d'abord."

    mara mefiant "Tu sais que quand quelqu'un dit ça, ça donne jamais envie de regarder ?"


    lysa blase "Moi ça me donne surtout envie de retourner me coucher."

    nyra reflexion "Tu l'as trouvée dans ton propre dossier ?"

    sael "Oui."

    "Nyra ne pose pas d'autre question. Elle sort sa tablette et commence à naviguer dans les menus. Les autres finissent par faire pareil, les uns après les autres."


    iris colere "Attendez... depuis quand on peut consulter ça ?"

    tomas neutre "Depuis le dernier amendement, je crois. Une partie des restrictions a sauté avec le vote et... enfin, visiblement ça aussi."

    iris colere "Évidemment. Et personne n'a pensé à nous prévenir."

    mara agace "Tu veux qu'on mette une alerte à chaque nouveau bouton qui apparaît ?"

    iris "Je veux juste éviter de découvrir par hasard que quelqu'un garde un dossier médical sur moi depuis deux semaines !"


    elen inquiet "Je crois que je l'ai."

    "Tout le monde se tourne vers elle."

    elen "M16. C'est marqué ici."

    elias inquiet "Moi aussi."

    ryn desaccord "Pareil."


    iris inquiet "... Ouais."

    mara mefiant "Vous vous foutez de moi..."

    "Mara tourne sa tablette vers nous. La même référence apparaît au milieu de son dossier."

    nyra neutre "Moi aussi."


    lysa blase "Bon. Super. Génial même."

    tomas inquiet "Moi aussi." id j17_m16_tomas_moi_aussi

    julian inquietude "... Pareil."

    "Plus personne ne parle. Je savais qu'on allait tous avoir la même mention, mais la voir apparaître sur chaque écran me retourne quand même l'estomac."


    noam inquiet "Donc on l'a tous."

    ryn colere "Tous ceux qui sont ici."

    nyra reflexion "Kael aussi ?"

    noam hesitation "Oui."

    "Plusieurs regards se tournent vers moi. Je réalise trop tard que j'ai répondu trop vite."


    mara mefiant "Comment tu sais ça ?"

    noam "Il me l'a dit hier."


    ryn "Et il savait ce que ça voulait dire ?"

    noam "Non." id j17_m16_noam_non

    sael neutre "Moi, oui. Maintenant."

    "Elle ouvre le livre à la page marquée, le fait pivoter et le pousse au centre de la table."

    sael "J'ai trouvé la référence hier dans les Archives."

    "Pendant une seconde, personne ne dit rien. Puis tout part d'un coup."


    iris surpris "Quoi ?!"

    elias colere "Attends, attends... accès à quoi ?"

    tomas inquiet "Mnésique. La mémoire."


    mara colere "Merci Tomas, on avait compris !"

    julian peur "Attendez, ça peut vouloir dire autre chose, non ? Un examen, un risque neurologique... j'en sais rien. Pas forcément qu'on a fouillé dans nos souvenirs."

    tomas reflechit "C'est possible. Enfin... oui, mais le terme est quand même très précis. 'Accès mnésique', ça veut dire accès direct à la mémoire. Après, ça dit pas ce qu'ils ont fait exactement, ni pourquoi, ni—"


    iris colere "Tomas."

    tomas neutre "Oui. J'arrête."

    ryn colere "Donc quelqu'un a foutu ses mains dans nos têtes ?"


    sael mefiant "On n'en sait rien."

    ryn "C'est écrit noir sur blanc !"


    sael "C'est un nom de procédure. Pas une explication."

    lysa blase "Magnifique. On a donc le choix entre 'quelqu'un a joué avec notre mémoire' et 'quelqu'un a nommé une procédure comme ça juste pour le plaisir'. Je me sens beaucoup mieux."


    elen peur "Mais... si c'est vrai, on devrait s'en souvenir, non ?"

    "Je baisse instinctivement les yeux. Sael me regarde brièvement, mais ne dit rien."

    nyra neutre "Pas forcément. C'est justement ça, le problème."

    mara colere "Ouais, bah moi je veux savoir quand ça a été fait. Et pourquoi."


    ryn "Et par qui."

    elias colere "Et combien de fois."

    iris colere "Et ce qu'on nous a retiré."

    "Les voix commencent à monter. Plusieurs parlent en même temps. Elen essaie de calmer Iris pendant que Ryn demande à Sael si le livre contient d'autres informations."


    sael desaccord "La page suivante a été arrachée."

    mara colere "Évidemment."

    tomas inquiet "T'es sûre qu'il y en a pas une autre quelque part ?"

    sael "J'en ai cherché trois. C'était la seule référence que j'ai trouvée."


    nyra raison "Ça suffit."

    "Sa voix n'est pas forte, mais elle coupe progressivement le brouhaha."

    nyra "On peut continuer à tourner en rond toute la matinée... ou demander directement à celle qui contrôle tout ici."

    ryn "Kami !"

    "Il lève les yeux vers l'écran principal."

    ryn colere "Montre-toi !"

    $ hideGroup()

    pause 0.5
    play sound "audio/sfx_announce.mp3"
    pause 1.0
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Je suis toujours touchée quand vous m'appelez tous avec autant d'enthousiasme."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Même si, techniquement, un simple 's'il te plaît' aurait suffi."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    $ bc_show("tomas", "inquiet")
    tomas inquiet "M16. Ça veut dire quoi exactement ?"
    $ bc_hide()

    kami "Je ne peux pas répondre à cette question."

    "Le silence est immédiat."

    $ bc_show("mara", "colere")
    mara colere "Pardon ?"
    $ bc_hide()

    $ bc_show("tomas", "neutre")
    tomas "Alors donne-nous au moins la date. Quand est-ce que ça a été fait ?"
    $ bc_hide()

    kami "Je ne peux pas répondre à cette question."

    $ bc_show("ryn", "colere")
    ryn colere "Qui l'a ordonnée ?"
    $ bc_hide()

    kami "Je ne peux pas répondre à cette question."

    $ bc_show("iris", "colere")
    iris colere "Est-ce qu'on nous a effacé des souvenirs ?"
    $ bc_hide()

    kami "Je ne peux pas répondre à cette question."

    $ bc_show("elias", "colere")
    elias colere "Putain mais tu peux répondre à quoi, exactement ?"
    $ bc_hide()

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "À énormément de choses ! Essayez de me demander la température de la salle, par exemple."

    $ bc_show("ryn", "colere")
    ryn colere "Arrête tes conneries !"
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    $ bc_show("nyra", "neutre")
    nyra neutre "Qu'est-ce qui t'empêche de répondre ? Quelle règle ?"
    $ bc_hide()

    "Kami ne répond pas immédiatement. Pour la première fois depuis le début de l'échange, son silence ressemble presque à une hésitation."

    kami "Mes règles internes."

    $ bc_show("nyra", "reflexion")
    nyra reflexion "Quel Commandement ?"
    $ bc_hide()

    kami "Aucun."

    $ bc_show("tomas", "surpris")
    tomas surpris "Aucun ?"
    $ bc_hide()

    kami "Les Commandements encadrent votre comportement et certaines limites de mon autorité sur le monde extérieur. Ils ne constituent pas l'intégralité de mes règles de fonctionnement."

    $ bc_show("iris", "colere")
    iris colere "Donc il existe des règles qu'on n'a jamais vues ?"
    $ bc_hide()

    kami "Évidemment."

    $ bc_show("mara", "colere")
    mara colere "Ah bah oui, évidemment ! Quel jeu de merde ce serait si on connaissait toutes les règles !"
    $ bc_hide()

    $ bc_show("nyra", "colere")
    nyra colere "Et on est censés modifier quoi, exactement, si tu nous caches la moitié du système ?"
    $ bc_hide()

    kami "Vous n'êtes pas censés modifier mon système."

    "Nyra s'arrête net."

    kami "Le Conclave vous permet de proposer des modifications aux Commandements. Rien de plus."

    $ bc_show("tomas", "raison")
    tomas raison "Tu nous as dit que tu pouvais pas intervenir dans les manigances du Conclave. Si M16 a un rapport avec tout ça, alors tu sais forcément quelque chose."
    $ bc_hide()

    kami "Et je maintiens ce que j'ai dit. Je ne peux prendre part à aucune manigance du Conclave."

    $ bc_show("tomas", "neutre")
    tomas "Ce n'est pas une réponse."
    $ bc_hide()

    kami "C'est pourtant la seule que je peux vous donner."

    $ bc_show("ryn", "colere")
    ryn colere "Tu sais quelque chose."
    $ bc_hide()

    kami "Probablement."

    $ bc_show("ryn", "colere2")
    ryn colere2 "Alors parle !"
    $ bc_hide()

    kami "Non."

    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "inquiet", -0.05),
        ("lysa", "blase", 0.06),
        ("ryn", "colere2", 0.17),
        ("mara", "colere", 0.28),
        ("tomas", "inquiet", 0.39),
        ("elen", "inquiet", 0.50),
        ("julian", "hesitation", 0.61),
        ("iris", "determine", 0.72),
        ("nyra", "neutre", 0.83),
        ("elias", "neutre", 0.94),
        ("sael", "desaccord", 1.05),
    ])


    "Ryn fait un pas vers l'écran comme s'il pouvait atteindre Kami à travers lui. Sael lui attrape le bras avant même qu'il ne réalise ce qu'il fait."

    sael desaccord "Ryn."

    "Il s'arrête, le souffle court."

    nyra neutre "Très bien."

    "Elle ferme sa tablette."

    nyra "Alors arrêtons."


    elen inquiet "Arrêtons quoi ?"

    nyra "De participer."

    "Plusieurs regards convergent vers elle."

    nyra raison "On est censés voter librement, en sachant ce qu'on fait. Là, on découvre M16 dans tous nos dossiers et celle qui organise les votes refuse même de nous dire ce que c'est."

    tomas inquiet "Nyra..."

    nyra "Alors non. Faire comme si nos décisions étaient encore éclairées, ça n'a plus aucun sens."


    elias neutre "Plus de votes."

    "Nyra tourne les yeux vers lui. Elias pose sa tasse avec un bruit sec."

    elias colere "Tant qu'on sait pas ce qu'on nous a foutu dans le crâne, je vote plus pour rien."

    ryn determine "Moi non plus."

    mara colere "Pareil."


    iris determine "Je vais certainement pas continuer à cocher des cases comme si de rien n'était."

    lysa blase "Ça tombe bien, j'avais justement toujours rêvé de faire grève dans l'espace."

    julian hesitation "Je suis d'accord, mais... attendez. Si on arrête tout, on balance peut-être notre seule chance de changer quoi que ce soit ici."


    tomas raison "C'est ça qui me fait peur. On devrait peut-être réfléchir deux minutes avant d'en faire une décision pour tout le monde."

    nyra colere "Et voter demain comme si nous n'avions rien découvert serait plus raisonnable ?"

    tomas "Je n'ai pas dit ça."

    nyra "Alors qu'est-ce que tu proposes ?"

    tomas inquiet "Je dis juste qu'on devrait pas décider ça maintenant, alors que tout le monde est à cran."


    ryn colere "C'est pas de la colère. C'est du bon sens."

    mara mefiant "Pour une fois que je suis d'accord avec lui, notez la date."


    elen determine "Non. Nyra a raison."

    "Tout le monde se tourne vers Elen. Elle se lève à son tour."

    elen "Si on continue comme avant, Kami n'a aucune raison de nous répondre. Alors on ne vote plus jusqu'à ce qu'elle le fasse."

    elias joie "Voilà."

    elen joie "Pas de réponses, pas de vote !"

    "Un court silence."

    iris neutre "... Tu viens vraiment de faire un slogan ?"

    elen joie "Oui !"

    iris "Pourquoi t'as l'air aussi contente ?"

    elen hesitation "Je suis pas contente ! Enfin... je suis motivée. C'est différent."


    mara rire "Non, non, laisse-la. Elle est lancée."

    elen determine "Pas de réponses—"

    elias fatigue "Non."

    mara rire "Si, attends, moi je veux entendre la suite."

    elen joie "Pas de vote !"


    lysa blase "On va tous mourir, mais au moins on aura eu une manif correcte."

    "Même Ryn laisse échapper un bref rire nerveux. La tension retombe à peine quelques secondes, puis Nyra revient vers l'écran."

    nyra determine "Tu as entendu. Pas de réponse sur M16, pas de vote. C'est aussi simple que ça."

    $ hideGroup()
    play sound "audio/sfx_announce.mp3"
    show screen kami_broadcast_ui

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "C'est votre droit."

    "La réponse déstabilise tout le monde."

    $ bc_show("nyra", "surpris")
    nyra surpris "... Quoi ?"
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous êtes libres de refuser de participer. Aucune règle ne vous oblige à déposer une proposition, débattre ou voter."

    $ bc_show("ryn", "desaccord")
    ryn desaccord "C'est tout ?"
    $ bc_hide()

    kami "Pas exactement."

    "Le ton de Kami ne change pas. C'est justement ce qui me déplaît."

    kami "Si les représentants refusent durablement d'exercer leur fonction, la phase finale du Conclave sera annulée."

    $ bc_show("tomas", "inquiet")
    tomas inquiet "Définis 'durablement'."
    $ bc_hide()

    kami "Jusqu'au jour vingt-et-un."
    with flash_red

    "Plus personne ne bouge."

    $ bc_show("noam", "surpris")
    noam surpris "Le jour vingt-et-un ?"
    $ bc_hide()

    kami "Oui. Si votre mouvement de protestation se poursuit jusque-là, le Conclave prendra fin."

    $ bc_show("iris", "inquiet")
    iris inquiet "Attends. Il devait durer un mois."
    $ bc_hide()

    kami "Il devait pouvoir durer un mois. Nuance."

    $ bc_show("tomas", "colere")
    tomas colere "Mais c'était écrit nulle part dans les règles que tu nous as données !"
    $ bc_hide()

    kami "Ce mécanisme relève de mes règles internes."

    $ bc_show("mara", "colere")
    mara colere "Putain, encore elles."
    $ bc_hide()

    kami "La troisième livraison, prévue au jour vingt-et-un, sera remplacée par une navette. Vous serez invités à quitter le Conclave et à retourner dans vos districts."

    $ bc_show("ryn", "colere")
    ryn colere "Et si on refuse de monter ?"
    $ bc_hide()

    pause 0.5

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Nous pourrons examiner cette possibilité au jour vingt-et-un."

    "Ryn serre les poings. Personne ne relève la menace, si c'en est une."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    $ bc_show("nyra", "colere")
    nyra colere "Donc c'est ça, ta réponse ? Tu t'assois et t'attends quatre jours qu'on craque ?"
    $ bc_hide()

    kami "Je n'ai pas besoin de répondre à votre protestation."

    kami "Vous avez formulé une position. Je vous ai indiqué ses conséquences."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Votre mouvement est parfaitement compatible avec les règles du Conclave. Je vous encourage même à le poursuivre aussi longtemps que vous le jugerez nécessaire."

    $ bc_show("mara", "colere")
    mara colere "Va te faire foutre."
    $ bc_hide()

    kami "Message reçu."

    hide screen kami_broadcast_ui
    $ bc_off()
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "L'écran s'éteint."
    "Personne ne parle. On pensait enfin tenir quelque chose contre elle. En fait, elle peut juste attendre qu'on craque."

    $ hideGroup()
    jump _17_0_1_1_APRES_PROTESTATION


label _17_0_1_1_APRES_PROTESTATION:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.0

    $ showGroup([
        ("noam", "hesitation", -0.05),
        ("lysa", "blase", 0.06),
        ("ryn", "colere", 0.17),
        ("mara", "neutre", 0.28),
        ("tomas", "inquiet", 0.39),
        ("elen", "inquiet", 0.50),
        ("julian", "hesitation", 0.61),
        ("iris", "colere", 0.72),
        ("nyra", "fatigue", 0.83),
        ("elias", "neutre", 0.94),
        ("sael", "neutre", 1.05),
    ])


    tomas inquiet "Quatre jours."

    nyra fatigue "J'ai entendu."

    tomas "Je dis pas qu'il faut céder. Je dis qu'on vient peut-être de réduire tout ce qu'il nous reste à quatre jours... et qu'on n'a aucun plan derrière."

    ryn colere "On en trouvera un."

    tomas "Comment ?"

    ryn "J'en sais rien, mais continuer à voter en souriant, c'est pas un plan non plus."


    iris colere "Et on fait quoi si le jour vingt-et-un arrive et qu'on sait toujours rien ? On rentre chez nous avec une jolie mention 'procédure d'accès mnésique' dans le dossier et on reprend notre vie ?"

    lysa blase "Personnellement, j'avais prévu de faire comme si tout ça n'était jamais arrivé. Vu le thème du moment, quelqu'un pourra peut-être m'aider."

    iris colere "Lysa."

    lysa "Quoi ? Je préfère encore faire une blague de merde que commencer à paniquer."

    "Cette fois, personne ne lui répond."

    elen inquiet "On va trouver quelque chose."


    mara neutre "T'as rangé la pancarte imaginaire ?"

    elen colere "J'essayais juste de garder tout le monde ensemble !"

    mara "Je sais."

    "Le ton de Mara est étrangement doux. Elen détourne les yeux."


    nyra neutre "On maintient la position pour aujourd'hui. Pas de vote, pas de nouvelle proposition."

    tomas reflechit "Et demain ?"

    nyra "Demain, on réévalue. Mais personne ne décide seul."

    ryn desaccord "Moi je change pas d'avis."

    nyra "Je n'ai pas dit que tu devais."

    "Je reste un peu en retrait. Tout le monde discute désormais des quatre jours qui nous restent, de ce qu'on pourrait demander à Kami, de ce qu'on peut encore consulter dans les Archives."
    "Moi, je n'arrive pas à quitter M16 des yeux."

    think "Tout le monde l'a."

    "Je devrais peut-être leur dire que j'ai réellement perdu une partie de ma soirée. Sael le sait. Kael aussi, plus ou moins."
    "Mais tant que je comprends pas ce qui m'est arrivé, j'ai aucune envie de balancer ça devant tout le monde. Pas encore."


    noam hesitation "Je vais retourner dans ma chambre."

    iris inquiet "Encore ?"

    noam "J'ai besoin de réfléchir."

    lysa blase "Essaie pas trop fort, visiblement ça laisse des traces."

    "Je lui lance un regard. Elle lève immédiatement les mains."

    lysa "Pardon. Mauvais timing."

    noam sourire "Un peu."

    "Je quitte la cafétéria avant que la discussion reparte."

    $ hideGroup()
    call OFFER_DAILY_EXPLORATION(
        "_17_0_1_1_CHAMBRE_BRUIT", 1,
        ["dortoir", "maintenance", "infirmerie"],
        "Retourner dans la chambre", "dortoir"
    ) from _call_offer_exploration_j17


label _17_0_1_1_CHAMBRE_BRUIT:

    $ current_period = "Après-midi"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_104
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "Le couloir paraît presque agréable après le bruit de la cafétéria. Je prends mon temps pour rentrer, en essayant de remettre les événements dans l'ordre."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_105
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "M16. Les dossiers. Les règles internes de Kami. La fin du Conclave avancée au jour vingt-et-un. Et au milieu de tout ça, les dernières heures de ma journée d'hier qui n'existent simplement plus."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_106
    scene bg_chambre at adaptive_fullscreen, living_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0

    "Je referme la porte derrière moi et laisse tomber ma tablette sur le bureau."

    noam neutre "Quelle journée..."

    "Je m'assois, puis reste un moment à regarder le plafond sans vraiment réfléchir. Pour une fois, mon cerveau semble avoir atteint sa limite."


    "Un petit bruit métallique me fait relever la tête."

    noam reflexion "... ?"

    "J'attends. Rien."

    "Je finis par me lever pour prendre un verre d'eau."


    "Cette fois, je l'entends clairement. Un frottement court, suivi d'un léger choc."
    noam inquiet "C'était quoi, ça ?"

    "Le bruit vient du mur, près du plafond."
    "Je m'approche de la bouche d'aération au-dessus du bureau. Jusqu'ici, je n'y avais jamais vraiment prêté attention. Une grille rectangulaire, quatre vis, rien de particulier."

    "Je reste immobile quelques secondes, l'oreille tendue."

    noam "..." id j17_chambre_silence_noam

    "Rien." id j17_chambre_rien

    "Je pose une main sur la grille et tire doucement. Elle ne bouge pas."

    noam desaccord "Évidemment."

    "Je grimpe sur la chaise pour atteindre les vis. À première vue, elles ne sont pas abîmées, mais la grille semble légèrement décollée sur un côté."

    noam reflexion "Ça a toujours été comme ça ?"

    "Impossible à dire."

    "Je passe les doigts derrière le bord et tire plus fort."

    noam colere "Allez..."

    "Rien. La grille est solidement vissée."


    "Un nouveau frottement résonne derrière, plus loin cette fois."

    "Je retire immédiatement ma main."

    noam peur "... Il y a quelque chose là-dedans."

    "La première personne à laquelle je pense est Elias. Puis je repense au matin. M16 dans douze dossiers. Des règles que Kami refuse de révéler. Kael barricadé dans sa chambre."
    "Je n'ai aucune envie de courir dans le couloir en criant que quelque chose se déplace dans les murs."

    noam reflexion "Des outils."

    "Si je peux simplement retirer la grille, je saurai au moins si je suis en train de devenir parano ou si ce bruit existe vraiment."

    jump _17_0_1_1_MARA_MAINTENANCE


label _17_0_1_1_MARA_MAINTENANCE:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_107
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    "Je sors de ma chambre et referme la porte derrière moi. Je n'ai pas fait trois mètres que quelqu'un débouche du croisement."

    $ showGroup([
        ("noam", "surpris", 0.34),
        ("mara", "surpris", 0.66),
    ])

    mara surpris "Oh !"

    noam surpris "Mara."

    $ showP("noam", "inquiet", 0.34)
    $ showP("mara", "neutre", 0.66)

    mara mefiant "Pourquoi t'as cette tête ?"

    noam "Quelle tête ?"

    mara agace "La tête du mec qui vient de trouver un cadavre sous son lit."

    noam desaccord "J'ai entendu un bruit dans ma ventilation."

    "Elle me regarde quelques secondes."

    mara mefiant "... Je retire ce que je viens de dire. C'est presque pire."

    noam "Je vais chercher des outils."

    mara "Pourquoi ?"

    noam "Pour enlever la grille."

    mara agace "Tout seul ?"

    noam "Oui." id j17_maintenance_outils_oui

    mara rire "Bien sûr. Et après je te retrouve avec un tournevis planté dans la main parce que t'as décidé de faire Elias pendant dix minutes."

    noam desaccord "Je sais utiliser un tournevis."

    mara taquin "C'est exactement ce que disent les gens juste avant de se planter un tournevis dans la main."

    noam "Mara..."

    mara neutre "Je viens avec toi."

    noam "C'est pas nécessaire."

    mara "Je sais. C'est pour ça que je viens."

    "Elle me dépasse déjà dans le couloir."

    mara "Salle de maintenance ?"

    noam "Oui." id j17_maintenance_mara_oui

    mara taquin "Allez Sherlock. Montre-moi ton monstre dans les murs."

    "Je lève les yeux au ciel, mais je la suis. Honnêtement, je suis presque soulagé de ne pas y aller seul."

    $ hideGroup()

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_sas") from _call_MAYBE_PLAY_SCRIPTED_DOOR_108
    scene couloir_sas at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "hesitation", 0.34),
        ("mara", "neutre", 0.66),
    ])

    "On traverse le secteur principal sans croiser Elias. Mara jette un regard derrière elle une ou deux fois, moins légère qu'elle essaie de le faire croire."

    mara neutre "Tu crois que ça a un rapport avec ce matin ?"

    noam hesitation "J'en sais rien."

    mara "Bonne réponse."

    noam "Pourquoi ?"

    mara mefiant "Parce que si tu m'avais sorti une théorie complète après avoir entendu deux bruits dans un mur, je t'aurais ramené à l'infirmerie."

    noam sourire "Rassurant."

    mara taquin "Je prends soin de toi à ma manière."

    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_109
    scene bg_maintenance at adaptive_fullscreen with dissolve

    $ showGroup([
        ("noam", "reflexion", 0.34),
        ("mara", "neutre", 0.66),
    ])

    "La salle de maintenance est vide."

    mara neutre "Elias est pas là."

    noam "Il doit être encore avec les autres."

    "Je me dirige vers le panneau d'outils pendant que Mara fouille les tiroirs."

    noam reflexion "Tournevis plat... cruciforme..."

    mara "Prends les deux."

    noam "Pourquoi ?"

    mara agace "Parce qu'on sait pas ce qu'ils ont foutu comme vis dans ta chambre, génie."

    "Je prends les deux. Elle récupère une petite lampe portative et une pince."

    mara mefiant "Tiens."

    noam "Quoi ?" id j17_maintenance_noam_quoi

    mara "Regarde le tiroir."

    "Quelques outils sont posés de travers au fond, contrairement aux emplacements parfaitement dessinés sur la mousse."

    noam "Quelqu'un s'en est servi."

    mara agace "Ou Elias range comme un porc. Ce qui est aussi possible."

    noam reflexion "Tu viens de dire qu'il rangeait mieux que ça."

    mara taquin "Je refuse que mes propres arguments soient utilisés contre moi."

    "Je remarque quand même une clé absente de son emplacement. Impossible de savoir depuis quand."

    noam "On y va."

    mara "Après toi."

    $ hideGroup()
    jump _17_0_1_1_OUVERTURE_VENTILATION


label _17_0_1_1_OUVERTURE_VENTILATION:

    $ current_period = "Soir"

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_110
    scene couloir_dortoir at adaptive_fullscreen with dissolve

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_111
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 2.0

    $ showGroup([
        ("noam", "neutre", 0.34),
        ("mara", "neutre", 0.66),
    ])

    "Mara pose les outils sur le bureau pendant que je remonte sur la chaise."

    mara neutre "Bouge pas. Je tiens la chaise."

    noam "Je vais pas tomber."

    mara agace "C'est fou comme t'as besoin de contester absolument tout aujourd'hui."

    noam desaccord "C'est faux."

    mara "Merci pour la démonstration."

    "Je soupire et commence à dévisser la grille. Les deux premières vis viennent facilement. La troisième résiste davantage."

    noam reflexion "Celle-là est serrée à mort."

    mara "Passe-moi ça."

    noam "Je peux le faire."

    mara colere "Noam."

    "Je lui tends le tournevis. Elle force une seconde, grimace, puis la vis tourne enfin."

    mara rire "Et voilà."

    noam "Très impressionnant."

    mara taquin "Tu peux applaudir si tu veux."

    "La dernière vis tombe sur le bureau. Je retiens la grille avant qu'elle ne bascule."


    "Quand je la retire, un souffle d'air froid nous frappe immédiatement au visage."

    mara surpris "Ah ouais."

    "J'éclaire l'intérieur avec la lampe. Je m'attendais à un conduit étroit, tout juste assez large pour laisser passer l'air. Ce n'est pas du tout ce qu'il y a derrière le mur."

    noam surpris "C'est énorme."

    mara taquin "Je vais être mature et ne rien dire."

    noam "Merci."

    mara "J'ai dit que j'allais rien dire. Pas que j'avais rien pensé."

    "Le passage fait presque la largeur de mes épaules et descend légèrement avant de partir sur la gauche. Les parois sont métalliques, renforcées par endroits, avec suffisamment d'espace pour qu'une personne puisse s'y déplacer en rampant."

    noam inquiet "C'est pas une simple ventilation."

    mara mefiant "Non." id j17_ventilation_mara_non

    "Je passe la lampe sur le sol. Une fine couche de poussière recouvre la tôle, sauf à certains endroits où elle semble avoir été frottée."

    noam reflexion "Regarde."

    "Mara se penche."

    mara mefiant "Ouais."

    noam "Ça ressemble à des traces."

    mara "Ça ressemble surtout à quelque chose qui a frotté là-dedans. Je vais éviter de décider tout de suite que c'était un humain."

    mara mefiant "Tu vas quand même pas t'arrêter là."

    noam surpris "Tu veux que j'aille dedans ?"

    mara taquin "Je veux savoir où ça mène. Et c'est toi qui as les épaules les moins larges."

    noam hesitation "On devrait peut-être chercher Elias d'abord."

    mara agace "Et laisser à la chose qui se balade là-dedans le temps de disparaître ? Très bon plan."

    noam "Tu viens avec moi ?"

    mara "Quelqu'un doit surveiller l'ouverture. Et tenir la chaise si tu dois ressortir vite."

    noam doute "C'est pratique."

    mara rire "Allez, Sherlock. Jusqu'au premier croisement. Tu regardes, tu reviens."

    noam sourire "Et si je réponds plus, tu vas chercher Elias."

    mara colere "C'est censé me rassurer ?"

    noam "Non."

    "Je pose un genou sur le bureau. Mara ne cherche pas à me retenir. Elle rapproche même la lampe de l'ouverture."

    mara colere "Une minute. Pas plus."

    noam "Deux."

    mara "Une minute trente."

    noam "D'accord."

    mara "Et tu réponds quand je t'appelle."

    noam "Oui." id j17_ventilation_noam_oui

    mara colere "Je suis sérieuse."

    noam "Moi aussi."

    "Je prends la lampe et me glisse dans l'ouverture."

    $ hideGroup()
    jump _17_0_1_1_DANS_VENTILATION


label _17_0_1_1_DANS_VENTILATION:

    $ current_period = "Nuit"

    scene bg_conduit_reseau at adaptive_fullscreen, haunted_background with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 2.0
    $ flashlight_on()

    $ investigation_add("traces_conduit")
    tuto "Explore quelques embranchements. La carte se construit au fil de tes choix et aucun détour ne peut te bloquer."
    call investigation_conduit_run("survey") from _call_investigation_conduit_j17
    $ investigation_add("conduits_chambres")

    # Noam est le point de vue : seul dans le conduit, son sprite reste caché.
    $ showP("mara", "mefiant", 0.72)

    "Le métal est glacé sous mes mains. Je dois avancer sur les coudes pendant les premiers mètres, avec juste assez d'espace au-dessus de moi pour ne pas cogner la tête à chaque mouvement."

    noam reflexion "..." id j17_conduit_silence_noam_1

    "Derrière, la lumière de ma chambre devient rapidement un simple rectangle pâle."

    mara "Noam ?"

    noam "Je suis là."

    mara "Je te vois déjà plus."

    noam "Moi non plus, je te vois plus."

    mara "Très drôle."

    "Le conduit tourne légèrement, puis s'élargit. Je peux presque me mettre à quatre pattes."

    "Quelques mètres plus loin, une lumière faible traverse une grille sur ma droite."

    noam inquiet "Attends..."

    "Je m'approche et coupe ma lampe."

    "À travers les fentes, je reconnais une chambre. Pas la mienne. Le lit est placé de l'autre côté, et une veste sombre est posée sur une chaise."

    noam reflexion "Une autre chambre..."

    "Je rallume ma lampe et continue."

    "Une deuxième grille apparaît quelques mètres plus loin. Puis une troisième."

    "À chaque fois, le même principe : une ouverture vers une chambre différente."

    noam inquiet "Non..."

    mara "Quoi ?"

    noam "Le conduit passe derrière les chambres."

    mara "Toutes ?"

    noam "Je crois."

    "Je continue malgré le délai qu'on s'était fixé. Les grilles reviennent à intervalles réguliers, exactement comme les portes du couloir des dortoirs."

    "Une, deux, trois..."

    "Je commence à compter."

    "Le passage ne sert pas seulement à distribuer l'air. Il longe tout le secteur. Et surtout, il est assez grand pour qu'une personne puisse aller d'une chambre à l'autre sans jamais mettre un pied dans le couloir."

    "Je repense immédiatement aux vidéos. Kael dans ma chambre. Sa photo disparue. Le dessin de Juliette."

    noam panne "..."

    "Quelqu'un aurait pu entrer ici sans utiliser une seule porte."

    "Je chasse la pensée avant d'aller plus loin. Ce n'est encore qu'une possibilité."

    mara "Noam, ça fait plus d'une minute trente !"

    noam "Encore trente secondes !"

    mara "Tu négocies même quand t'es dans un mur ?!"

    "Je souris malgré moi et avance jusqu'au prochain embranchement."

    "Puis je m'arrête."

    "Le conduit ne suit plus simplement la ligne des chambres. Une dérivation part vers la droite."

    noam reflexion "Ça, c'est pas normal."

    "Je regarde derrière moi. Impossible de voir Mara."

    "Je devrais revenir."

    "J'éclaire la dérivation. Elle est plus étroite, mais praticable. Au bout, à quelques mètres seulement, une nouvelle grille apparaît."

    "Je compte mentalement les ouvertures croisées jusque-là."

    noam inquiet "... Douze."

    "Douze chambres."

    "Et pourtant il y en a une treizième devant moi."

    noam peur "Mara ?"

    mara "Quoi ?"

    noam "Il y a autre chose."

    mara stress "Reviens."

    noam "Attends." id j17_conduit_attends

    mara colere "Noam, reviens maintenant."

    "Je m'approche malgré tout."

    "La treizième grille donne sur une pièce plongée presque entièrement dans le noir. Je distingue des câbles, des conduits, des panneaux métalliques et quelque chose qui ressemble à un ancien support fixé au sol."

    "Ce n'est pas une chambre."

    noam inquiet "Il y a une pièce derrière les dortoirs."

    mara "Une quoi ?"

    noam "Une pièce technique, je crois."

    "Je colle davantage mon visage contre la grille."

    "La lumière de ma lampe glisse sur le sol de l'autre côté."

    "Quelque chose brille brièvement dans la poussière."

    noam reflexion "..." id j17_conduit_silence_noam_2

    "Une marque longue, fraîche, comme si un objet lourd avait été déplacé récemment."

    $ unlock_gallery_image("bg_cg043")
    scene bg_cg043 at adaptive_fullscreen with creep_diss
    $ cam_move(fx=0.43, fy=0.43, z=1.14, t=7.0)
    play sound "audio/sfx_duct_scrape.wav" volume 0.82

    "Un frottement résonne derrière moi."

    "Je me retourne si vite que mon épaule heurte la paroi."

    noam peur "Qui est là ?"

    "Ma lampe balaie le conduit."

    "Rien."

    mara "Noam ?!"

    noam "Chut."

    mara "Pourquoi tu me dis chut ?!"

    "J'éclaire le sol."

    "Dans la poussière que je viens de traverser, une trace s'arrête à quelques mètres de moi."

    "Pas une vieille marque."

    "Une traînée nette. Fraîche."
    $ danger_on()

    "Et elle n'était pas là quand je suis passé."

    noam peur "... Mara."

    mara "Quoi ?"

    noam "Va chercher Elias."

    mara stress "Pourquoi ?"


    "Quelque chose heurte doucement la tôle, beaucoup plus loin dans le conduit."

    $ horror_audio_cut(duration=0.46, restore_volume=0.62)
    noam peur "Parce qu'il y a quelqu'un ici."

    $ hideGroup()
    $ cam_reset(t=0.0)
    scene bg_conduit_reseau at adaptive_fullscreen with vpunch
    stop music fadeout 1.0
    $ danger_off()

    pause 1.0

    pause 1.0

    call end_day("18") from _call_end_day_18
    jump _18_0_1_1_0_REVEIL_CHAMBRE
