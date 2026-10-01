# =============================================================================
# JOUR 21 — Route 0_1_1_0_0
# Réponse à Kael : "Je reste s'il y a encore une chance de le sortir."
#
# Les Doppelgängers choisissent de prolonger le Conclave jusqu'au jour 30.
# Aucun vote n'est annoncé au cours de cette journée.

# =============================================================================

label _21_0_1_1_0_0_REVEIL:
    $ cafeteria_food_level = "null"
    $ current_day = 21
    $ day_id = 21
    $ current_period = "Matin"
    $ j20_kael_depart_choice = "stay"
    $ noam_has_juliette_drawing = False
    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    "Je me réveille avant l'annonce de Kami, avec cette sensation étrange d'avoir oublié quelque chose d'important."
    "Il me faut quelques secondes pour comprendre que, cette fois, ce n'est pas un vote, une dispute ou un bruit derrière la grille qui m'attend."
    think "On rentre."
    "Mon sac est déjà posé contre le bureau. Je l'avais préparé hier soir presque mécaniquement, en remettant deux fois les mêmes affaires dedans avant de comprendre que je les avais déjà rangées."
    "La grille d'aération est toujours là, au-dessus du bureau. Je la regarde malgré moi."
    think "Quelques heures."
    "Après ça, elle pourra bien faire tous les bruits qu'elle veut."
    "Je récupère mon téléphone, vérifie l'heure et me lève."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "couloir_dortoir") from _call_j21_stay_door_chambre_couloir
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Dans le couloir, presque toutes les portes sont ouvertes. Des sacs traînent devant les chambres, des voix se répondent d'un bout à l'autre du dortoir et, pour une fois, personne ne parle de Kami."
    $ showGroup([
        ("elen", "joie", 0.22),
        ("tomas", "hesitation", 0.50),
        ("lysa", "blase", 0.78),
    ])
    elen joie "J'ai tout pris ! Enfin... normalement."
    tomas hesitation "Tu viens de dire exactement la phrase qu'on dit juste avant de découvrir qu'on a oublié quelque chose."
    elen rire "Mais non ! J'ai vérifié deux fois."
    lysa blase "Donc t'as probablement oublié deux fois la même chose."
    elen "Vous êtes vraiment incapables d'être positifs cinq minutes."
    tomas "Moi je suis positif."
    lysa "T'as recompilé mentalement ta valise trois fois depuis que je suis sortie de ma chambre."
    tomas surpris "Comment tu—"
    lysa "Parce que tu comptes à voix haute."
    "Tomas ferme immédiatement la bouche."
    noam taquin "Bonjour."
    elen joie "Noam ! T'es prêt ?"
    noam "Normalement."
    tomas reflexion "Voilà. Lui aussi."
    lysa blase "Magnifique. Trois adultes et pas une certitude."
    "Elle a son sac sur une épaule, à peine rempli. Le mien paraît énorme à côté."
    noam surpris "C'est tout ce que t'as ?"
    lysa "J'ai pas emménagé ici."
    elen "Moi non plus !"
    lysa "Ton sac a l'air de contenir un cadavre."
    elen surpris "Il contient pas de cadavre."
    lysa blase "Merci Elen. C'était important de le préciser."
    "Je souris malgré moi."
    think "Ça ressemble presque à un départ normal."
    "Presque."
    $ hideGroup()
    # Durée : ~1m40
    # Total : ~1m40

label _21_0_1_1_0_0_SAS:
    $ current_period = "Midi"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir_dortoir", "sas1") from _call_j21_stay_door_couloir_sas
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Quand j'arrive au sas, presque tout le monde est déjà là."
    "Une capsule est déjà amarrée derrière la baie. Pendant une seconde, mon cœur accélère avant que je remarque les marquages sur sa coque."

    think "Livraison."

    "Pas de hublot, pas de sièges. Juste le conteneur automatique qu'on voit arriver tous les quelques jours."

    $ showGroup([
        ("ryn", "fatigue"),
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("iris", "blase"),
        ("kael", "calme"),
        ("tomas", "inquiet"),
        ("julian", "inquiet"),
        ("lysa", "blase"),
        ("nyra", "raison"),
        ("sael", "fatigue"),
        ("elen", "joie"),
        ("noam", "reflexion"),
    ])

    ryn fatigue "C'est quoi ça ?"
    elias neutre "Une livraison."
    ryn colere "Oui, j'avais vu. Je parle de la navette."
    mara taquin "Peut-être qu'on rentre dans les cartons."
    iris blase "Je te laisse celui marqué fragile."
    mara "Sympa."
    kael calme "La navette peut encore arriver."
    noam "Ouais."

    "Personne ne répond vraiment. Au début, les discussions reprennent quand même : Elen parle déjà de ce qu'elle mangera en rentrant, Julian de la première chose qu'il publiera, Tomas vérifie l'heure toutes les deux minutes."

    elen joie "Moi je vous le dis, premier arrêt : un vrai resto."
    sael fatigue "Tu parles de nourriture depuis ton réveil."
    elen "Parce que c'est important."
    julian "Je peux difficilement lui donner tort."
    lysa blase "Profitez. Dans dix minutes vous allez parler de vos lits."
    iris "Moi j'y pense déjà."

    "Les minutes passent. Petit à petit, les conversations deviennent plus courtes."

    pause 0.6

    tomas inquiet "Elle a combien de retard, là ?"
    julian "Douze minutes."
    tomas "T'as compté aussi ?"
    julian "J'ai regardé l'heure, Tomas."
    lysa fatigue "Je vous avoue que je m'attendais un peu à ce qu'il y ait un problème."
    tomas "Pourquoi ?"
    lysa blase "Parce qu'ici, quand quelque chose doit être simple, ça finit rarement simple."
    elen inquiet "Elle va venir quand même."
    nyra raison "On n'en sait rien."
    elen "Merci Nyra."
    nyra "Je préfère ça à te mentir."

    ryn colere "KAMI !"
    "Sa voix claque dans le sas."
    nyra raison "Elle t'entend."
    ryn "Alors qu'elle réponde."
    sael fatigue "Crier changera rien."
    ryn colere "Je sais, Sael."

    play sound sfx_announce
    stop music fadeout 0.5

    scene bg_diffusion_amour at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Oooh... vous êtes tous là."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Les sacs, les mines impatientes, les petits regards vers le sas..."
    kami "Vous étiez vraiment prêts à me quitter."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Je devrais être vexée."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Heureusement, j'ai une excellente nouvelle !"
    kami "Vous allez finalement pouvoir profiter encore un peu de ma compagnie."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "La navette de retour ne viendra pas aujourd'hui."

    pause 0.6

    hide screen kami_broadcast_ui
    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "fatigue"),
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("iris", "blase"),
        ("kael", "calme"),
        ("tomas", "inquiet"),
        ("julian", "inquiet"),
        ("lysa", "blase"),
        ("nyra", "raison"),
        ("sael", "fatigue"),
        ("elen", "joie"),
        ("noam", "reflexion"),
    ])

    ryn colere "QUOI ?!"
    iris colere "Non. Non, tu vas pas nous faire ça maintenant."
    noam colere "Pourquoi elle vient pas ?"
    elen inquiet "Attends, on devait partir aujourd'hui !"
    julian inquiet "Kami, tout le monde est prêt."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui

    kami "Je sais, je sais."
    kami "Mais vous oubliez un petit détail : le Conclave devait initialement durer trente jours."

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Le départ du jour vingt-et-un était une possibilité anticipée."
    kami "Une faveur, en quelque sorte."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Et certains de vos chers collègues m'ont fait savoir qu'ils souhaitaient continuer."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Continuer les débats."
    kami "Continuer les votes."
    kami "Continuer à améliorer le monde !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Vous voyez ? Il reste encore de vrais passionnés parmi vous."

    hide screen kami_broadcast_ui
    scene sas1 at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn", "fatigue"),
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("iris", "blase"),
        ("kael", "calme"),
        ("tomas", "inquiet"),
        ("julian", "inquiet"),
        ("lysa", "blase"),
        ("nyra", "raison"),
        ("sael", "fatigue"),
        ("elen", "joie"),
        ("noam", "reflexion"),
    ])

    mara colere "Qui ?"
    nyra determine "Combien de personnes ?"
    tomas inquiet "Et ça suffit pour annuler notre départ ?"
    ryn colere "Donne les noms."
    noam colere "On devait partir ensemble."
    iris colere "Surtout, on nous l'a annoncé. On a préparé nos affaires pour quoi, exactement ?"
    sael colere "Si certains voulaient rester, ils pouvaient au moins nous le dire."
    elen inquiet "Mais... pourquoi quelqu'un voudrait encore voter ?"
    julian inquiet "Ça, j'aimerais bien le savoir aussi."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui

    kami "Oui, Noam."
    kami "Ensemble."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Et regardez comme je respecte parfaitement votre souhait."
    kami "Personne ne part seul."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Quant aux noms..."
    kami "Non."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous allez encore passer neuf jours ensemble."
    kami "Je ne vais quand même pas vous mâcher tout le travail."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le Conclave se poursuivra donc jusqu'au jour trente, comme prévu à l'origine."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Et puisque vous êtes déjà au sas, votre livraison vous attend."
    kami "Je vous laisse ranger tout ça. Ça vous occupera les mains pendant que vous cherchez qui remercier."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Allez, courage."
    kami "Neuf jours, ça passe très vite."

    hide screen kami_broadcast_ui
    stop music fadeout 0.8
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    $ showGroup([
        ("ryn", "fatigue"),
        ("mara", "neutre"),
        ("elias", "neutre"),
        ("iris", "blase"),
        ("kael", "calme"),
        ("tomas", "inquiet"),
        ("julian", "inquiet"),
        ("lysa", "blase"),
        ("nyra", "raison"),
        ("sael", "fatigue"),
        ("elen", "joie"),
        ("noam", "reflexion"),
    ])

    pause 0.4

    ryn colere "Bon. Qui a demandé ça ?"
    mara colere "Tu crois vraiment que la personne va lever la main maintenant ?"
    ryn "J'en sais rien, mais j'aimerais bien qu'elle assume."
    tomas inquiet "Ryn, on sait même pas combien ils sont."
    ryn "Ça change quoi ?"
    nyra raison "Ça change qu'on ne va pas accuser les gens au hasard."
    ryn colere "Quelqu'un vient de nous rajouter neuf jours ici."
    nyra "Je sais."
    sael determine "Et gueuler sur tout le monde n'en enlèvera aucun."
    ryn "Vous êtes tous super calmes, ça fait plaisir."
    iris colere "Je suis pas calme du tout."
    elen triste "Moi non plus."
    julian inquiet "Personne ne l'est."
    lysa fatigue "Je suis énervée. Je suis juste pas surprise."
    noam inquiet "Pas surprise ?"
    lysa "Je pensais pas que ce serait aussi simple, c'est tout."
    noam "Pourquoi ?"
    lysa blase "Regarde les vingt derniers jours."
    mara "Pour une fois, elle marque un point."
    lysa "Je vais encadrer ça."

    "Ryn souffle bruyamment et récupère son sac."

    ryn fatigue "Moi, je range rien maintenant."

    nyra "Personne t'oblige à le faire tout de suite."

    "Il repart sans répondre. Elen reste encore quelques secondes à regarder la baie vide avant de reprendre son sac."

    elen triste "J'avais vraiment cru qu'on rentrait."

    sael fatigue "Nous aussi."

    "Cette fois, personne ne trouve quoi ajouter."

    lysa blase "Bon. Les cartons vont pas se ranger tout seuls."
    noam fatigue "Je t'aide."
    elen "Moi aussi."
    julian "Je viens."
    nyra raison "On s'y met à plusieurs, ça ira plus vite."

    $ hideGroup()

    # Durée : ~4m40
    # Total : ~6m20

label _21_0_1_1_0_0_LIVRAISON:
    $ current_period = "Après-midi"
    scene bg_stockage at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Une demi-heure plus tard, le sas s'est vidé de plusieurs sacs mais pas des caisses."
    "Nyra a fini par répartir les tâches sans vraiment demander l'avis de personne : certains transportent, d'autres ouvrent les cartons, les derniers trient ce qui va à la cafétéria, à l'infirmerie, à la maintenance ou au stockage."

    $ showGroup([
        ("nyra", "raison"),
        ("elen", "joie"),
        ("julian", "neutre"),
        ("lysa", "blase"),
        ("noam", "fatigue"),
    ])

    nyra raison "Les étiquettes sont déjà faites. Vous regardez, vous triez, vous évitez de poser le matériel médical avec la bouffe."
    elen joie "Ça semble à ma portée."
    lysa blase "C'est exactement ce qu'on dit avant de mettre une seringue dans une caisse de soupe."
    elen "Je ferai pas ça."
    julian sourire "Je suis prêt à témoigner en ta faveur si ça arrive."
    elen colere "Vous êtes chiants."
    noam "On commence ?"
    nyra "Oui. Et si vous hésitez, stockage. On vérifiera après."

    $ hideGroup()

    # Réutilisation du mini-jeu de tri déjà introduit au J7.
    call rangement_play from _call_rangement_day21_stay

    scene bg_stockage at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 0.8

    $ showGroup([
        ("elen", "content"),
        ("julian", "sourire"),
        ("lysa", "blase"),
        ("noam", "fatigue"),
        ("elias", "neutre"),
    ])

    elen content "Voilà ! Franchement, on s'en est bien sortis."
    lysa blase "Tu as lancé un câble de maintenance dans la caisse de l'infirmerie."
    elen "Une fois."
    julian sourire "Et elle l'a repris."
    lysa "Après avoir été regardée par quatre personnes."
    elen "Ça compte quand même."

    "Julian pousse une caisse destinée à la cafétéria près de la porte pendant qu'Elen ramène la suivante, toujours occupée à défendre son bilan."

    "Avec Lysa, je termine les dernières caisses. Elias, lui, est assis un peu plus loin avec le terminal de stock posé sur un genou."

    "Depuis quelques minutes, il ne range presque plus rien."

    noam reflexion "Tu cherches quoi ?"
    elias "Attends."

    "Il ouvre une caisse, pousse des câbles sur le côté, la referme, puis passe à la suivante."

    lysa blase "Tu viens déjà de regarder là."
    elias fatigue "Je sais."
    lysa "D'accord."

    noam "Elias ?"
    elias ecoute "Les plaques."
    noam reflexion "Quelles plaques ?"
    elias "Celles que j'ai utilisées hier dans les dortoirs."
    noam "Les plaques métalliques ?"
    elias "Ouais."

    "Il se relève et regarde encore autour de lui."

    elias fatigue "J'en ai utilisé six."
    lysa "Et elles devaient revenir aujourd'hui ?"
    elias "Ouais. Le Conclave remet automatiquement dans la livraison suivante ce qu'on utilise."
    noam reflexion "Tout ?"
    elias "Tout ce qui fait partie du stock. Les vis, les forets, les fixations, les câbles... les plaques aussi."

    "Il attrape une petite boîte et me la montre."

    elias "Ça, c'est revenu."
    "Il en montre une autre."
    elias "Ça aussi."
    "Puis une troisième."
    elias colere "Même ça."
    noam "Mais pas les plaques."
    elias "Voilà."

    lysa blase "Elles sont peut-être au sas."
    elias "J'ai regardé."
    noam "Dans une autre caisse ?"
    elias "Aussi."

    "Il fait défiler le terminal, agacé."

    noam "Le registre dit quoi ?"
    elias fatigue "Que six plaques ont été commandées automatiquement avec le reste."
    noam "Et qu'elles sont arrivées ?"
    elias "J'en sais rien. C'est justement ça que je veux vérifier."

    lysa "Tomas est encore au sas avec les listes."
    elias "Ouais."

    "Elias se lève d'un coup."

    elias colere "Je vais le voir."

    lysa blase "Nous on continue ?"
    elias "Ouais. Il reste trois cartons."

    "Il attrape le terminal et part vers la porte."

    # Retirer Elias du groupe déclenche l'animation de sortie définie par showGroup().
    $ showGroup([
        ("elen", "content"),
        ("julian", "sourire"),
        ("lysa", "blase"),
        ("noam", "fatigue"),
    ])

    "Sa silhouette disparaît dans le couloir."

    elen surpris "Il a perdu quoi ?"
    noam "Des plaques de métal."
    elen "Ah."
    julian "Et c'est grave ?"
    noam "Surtout agaçant, visiblement."
    lysa blase "Très agaçant."

    "Elen hausse les épaules et reprend un carton."

    elen "Bon. Tant qu'il nous démonte pas les murs."

    julian rire "Ne lui donne pas d'idée."

    $ hideGroup()

    # Durée : ~3m20
    # Total : ~9m40

label _21_0_1_1_0_0_MANIFESTE:
    scene sas1 at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "Quand je reviens au sas, Elias et Tomas sont penchés sur le bordereau de livraison."

    $ showGroup([
        ("elias", "colere", 0.20),
        ("tomas", "inquiet", 0.46),
        ("noam", "reflexion", 0.72),
        ("nyra", "raison", 0.94),
    ])

    elias colere "Là. Regarde."
    tomas hesitation "Je regarde."
    elias "La ligne des plaques."
    tomas "Je l'ai."

    "Tomas agrandit le détail de la livraison."

    noam "Alors ?"
    tomas reflexion "Six plaques de renfort en alliage structurel ont bien été commandées automatiquement."
    elias "Ça je savais."
    tomas "Attends."

    "Il descend un peu plus bas."

    tomas inquiet "Et elles figurent aussi sur le bordereau d'arrivée."
    noam reflexion "Donc elles étaient dans la capsule."
    tomas "Oui. Enfin... le bordereau dit qu'elles sont arrivées avec cette livraison."
    elias colere "Donc elles sont arrivées."

    nyra raison "Le registre sait uniquement ce qui a été demandé et ce qui a été réceptionné. Après ça, il ne suit pas chaque objet dans la station."
    noam "Donc impossible de savoir où elles sont maintenant."
    tomas "Exactement."

    elias "Mais elles étaient là."

    pause 0.4

    noam "Ça peut être une erreur sur le bordereau ?"
    tomas hesitation "Possible."
    elias colere "Tout le reste est bon."
    tomas "Je sais, mais—"
    elias "Les vis sont là. Les fixations sont là. Les câbles sont là. Les forets sont là."
    noam inquiet "Sauf les plaques."
    elias fatigue "Sauf les plaques."

    nyra "Vous avez vérifié toutes les caisses ?"
    elias "Deux fois."
    noam "Trois, pour certaines."
    elias colere "Merci."

    tomas reflexion "Une caisse peut avoir été ouverte avant qu'on commence à ranger."
    nyra "Ou le bordereau peut être faux."
    elias "Ou quelqu'un les a prises."
    noam reflexion "Pourquoi quelqu'un ferait ça ?"

    "Elias secoue la tête, déjà agacé de ne pas avoir de réponse."

    elias fatigue "J'en sais rien."
    nyra raison "Alors on ne part pas plus loin que ça."

    "Elle pointe le terminal."

    nyra "On sait qu'elles ont été commandées. On sait qu'elles apparaissent à l'arrivée. On sait qu'elles sont introuvables. Le reste, pour l'instant, c'est des suppositions."

    tomas "Oui."

    "Elias souffle, pas convaincu mais incapable de contredire."

    elias colere "Ça change pas mon problème."
    noam "Les chambres."
    elias "Ouais. Il m'en restait six à fermer aujourd'hui."

    "Je mets une seconde à replacer les choses."

    noam reflexion "Tu peux utiliser autre chose ?"
    elias fatigue "Je peux bricoler."
    tomas surpris "Avec quoi ?"
    elias "Du métal."
    tomas "Merci, ça aide beaucoup."
    elias colere "Des caches, des panneaux inutilisés, des vieux morceaux de châssis. Je vais trouver."
    nyra raison "Tu vérifies avant de démonter quoi que ce soit."
    elias "Oui maman."
    nyra colere "Elias."
    elias fatigue "Oui. Je vérifierai."

    noam taquin "Donc on démonte le Conclave, mais proprement."
    tomas "C'est exactement ce qu'elle n'a pas dit."
    elias "Vous venez m'aider ou vous continuez à commenter ?"
    noam fatigue "Je viens."
    tomas hesitation "Moi aussi. Principalement pour t'empêcher d'arracher quelque chose d'important."
    elias "Parfait."

    "Nyra nous regarde partir, puis récupère le terminal pour finir de vérifier le reste de la livraison."

    $ hideGroup()

    # Durée : ~2m40
    # Total : ~12m20

label _21_0_1_1_0_0_RECUPERATION:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "L'après-midi se transforme en chasse au métal."
    "Pas aux plaques disparues. Elias a manifestement décidé qu'il les retrouverait plus tard."
    "Pour l'instant, il veut surtout finir ce qu'il avait commencé."
    $ showGroup([
        ("elias", "ecoute", 0.20),
        ("tomas", "reflexion", 0.50),
        ("noam", "fatigue", 0.80),
    ])
    elias ecoute "Ça."
    tomas surpris "Non."
    elias "Pourquoi ?"
    tomas "Parce que c'est le cache d'un répartiteur électrique."
    elias "Il est éteint."
    tomas "Aujourd'hui."
    elias fatigue "Fait chier."
    "Elias passe au panneau suivant."
    elias "Ça."
    tomas "Oui."
    elias surpris "Sérieux ?"
    tomas "C'est une plaque de protection d'un ancien support de stockage. Le support n'existe plus."
    elias "Enfin."
    "Il attrape son tournevis."
    noam "Attends, tu vas vraiment tout démonter ?"
    elias "Pas tout."
    noam "Ça me rassure énormément."
    elias "Tiens ça."
    "Je maintiens la plaque pendant qu'il retire les fixations."
    tomas reflexion "Tu sais que ça sera plus fin que les autres."
    elias "Je doublerai."
    tomas "Et les attaches ne sont pas au même entraxe."
    elias "Je reperce."
    tomas "Et—"
    elias colere "Tomas."
    tomas hesitation "Oui ?"
    elias "Si t'as une solution meilleure, je prends."
    "Tomas ouvre la bouche, réfléchit, puis la referme."
    tomas "Non."
    elias "Alors laisse-moi bricoler."
    tomas "Je te laisse bricoler. J'essaie juste d'éviter que tu transformes une chambre en court-circuit."
    elias "C'est gentil."
    "La plaque se décroche enfin."
    elias sourire "Voilà."
    noam "Une."
    elias fatigue "Il m'en faut au moins dix comme ça."
    noam "Tu viens de dire qu'il t'en restait six."
    elias "Parce que celle-là est fine. Je double."
    noam "Ah."
    tomas "Je t'avais prévenu."
    elias "Toi, ça va."
    "Tomas sourit malgré lui."
    $ hideGroup()
    scene bg_stockage at adaptive_fullscreen with dissolve

    "On passe ensuite par le stockage, puis par une réserve de maintenance que je n'avais jamais vraiment regardée."
    "Elias récupère des panneaux, des chutes de tôle et deux morceaux d'un ancien châssis. À chaque fois, Tomas vérifie qu'il ne démonte rien d'utile."

    $ showGroup([
        ("mara", "taquin"),
        ("ryn", "fatigue"),
        ("elias", "fatigue"),
        ("tomas", "reflexion"),
        ("noam", "fatigue"),
    ])

    "On croise Mara et Ryn en sortant avec une plaque presque aussi large que le couloir."

    mara taquin "Ah. Donc c'est ça, votre solution."
    ryn fatigue "Vous allez faire quoi avec ce truc ?"
    elias "Remplacer les plaques qui manquent."
    mara "Celles de la livraison ?"
    noam "Ouais."
    ryn reflexion "Vous les avez pas retrouvées ?"
    tomas "Non. Elles sont sur le bordereau d'arrivée, mais physiquement on n'a rien."
    ryn "Bizarre."
    elias colere "Merci."
    mara taquin "Laisse-le, il vit très mal le deuil."
    elias "Vous voulez aider ou juste parler ?"

    "Ryn attrape aussitôt un bord de la plaque."

    ryn "Donne."
    noam surpris "Sérieux ?"
    ryn fatigue "Ça pèse rien."

    "Il soulève. Son expression change à peine, ce qui m'agace presque."

    mara "Très bien, monsieur muscles. Moi je supervise."
    elias "Non."
    mara "Trop tard."

    "À cinq dans le couloir, le transport devient surtout une question de ne pas se marcher dessus."

    elias "Tournez."
    ryn "Je tourne."
    tomas "Pas autant !"
    mara "Vous êtes catastrophiques."
    noam "Tu peux vraiment aider, sinon."
    mara "Je vous aide moralement."

    ryn colere "Mara, pousse la porte."
    mara blase "Voilà. On exploite toujours les compétences rares."

    "Elle pousse la porte du stockage avec le pied et nous laisse passer."

    "Une fois la plaque posée contre le mur, Ryn essuie ses mains sur son pantalon."

    ryn "Si vous avez besoin de porter les autres, appelez-moi."
    elias "Ouais."
    mara taquin "Moi aussi."
    elias "Non."

    "Mara sourit et repart avec Ryn."

    $ hideGroup()

    # Durée : ~2m30

    # Total : ~13m30

label _21_0_1_1_0_0_DORTOIRS:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "En fin d'après-midi, Elias reprend son travail dans les dortoirs."
    "Je l'aide à tenir les plaques improvisées pendant qu'il perce. Tomas reste à côté avec les fixations et un air de contrôleur technique."
    $ showGroup([
        ("elias", "fatigue", 0.18),
        ("tomas", "reflexion", 0.50),
        ("noam", "fatigue", 0.82),
    ])
    elias fatigue "Tiens droit."
    noam "Je tiens droit."
    elias "Non."
    noam "Elias..."
    elias colere "Tu tiens droit par rapport au mur ou par rapport à toi ?"
    noam "Au mur."
    tomas "Pas tout à fait."
    noam colere "Merci Tomas."
    tomas hesitation "Pardon."
    elias "Un peu à droite."
    noam "Comme ça ?"
    elias "Voilà."
    "La perceuse démarre."
    play sound sfx_drill
    "Le métal vibre contre mes paumes."
    "Quand Elias coupe enfin l'outil, il vérifie les attaches une par une."
    elias ecoute "Ça tiendra."
    tomas reflexion "Moins bien que les vraies plaques."
    elias "Oui."
    tomas "Mais ça tiendra."
    elias "Voilà."
    noam "Il t'en reste combien ?"
    elias fatigue "Trop."
    noam "Réponse précise."
    elias "Quatre chambres si je trouve encore de quoi doubler."
    tomas inquiet "Et si tu trouves pas ?"
    elias "Je trouverai."
    "Il répond tellement vite que Tomas n'insiste pas."
    noam reflexion "Tu veux vraiment finir aujourd'hui ?"
    elias "Ouais."
    noam "Pourquoi ?"
    elias colere "Parce que j'ai commencé."
    "Il ramasse sa perceuse."
    elias fatigue "Et parce que j'aime pas qu'un truc disparaisse pile quand j'en ai besoin."
    noam "Ça te travaille."
    elias "Évidemment que ça me travaille."
    "Il se tourne vers moi."
    elias ecoute "Je sais ce que j'ai pris. Je sais ce qui devait revenir. Si je commence à accepter que six plaques se volatilisent juste parce que 'bah peut-être', autant arrêter de tenir un stock."
    tomas reflexion "Je peux revérifier les logs ce soir."
    elias "Tu vas trouver la même chose."
    tomas "Probablement."
    elias "Alors dors."
    tomas surpris "C'est toi qui me dis ça ?"
    elias "Ouais."
    tomas "Tu comptes dormir, toi ?"
    "Elias regarde la plaque suivante."
    elias "On verra."
    $ hideGroup()
    # Durée : ~1m40
    # Total : ~15m10

label _21_0_1_1_0_0_SOIR:
    $ current_period = "Nuit"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.0
    "Le soir, la cafétéria est plus silencieuse que d'habitude."
    "Les sacs ont disparu du sas. Ils sont retournés dans les chambres, souvent sans être défaits."
    "Je m'assois avec Lysa et Tomas. Elias n'est pas là ; une perceuse résonne encore de temps en temps dans les dortoirs."
    $ showGroup([
        ("lysa", "fatigue", 0.20),
        ("tomas", "hesitation", 0.50),
        ("noam", "fatigue", 0.80),
    ])
    tomas hesitation "À cette heure-ci..."
    lysa "Non."
    tomas surpris "J'ai encore rien dit."
    lysa blase "Je sais exactement ce que t'allais dire."
    noam "Moi pas."
    lysa "Il allait nous rappeler qu'on devrait déjà être dans la navette."
    "Tomas baisse les yeux."
    tomas "Oui."
    noam fatigue "Merci."
    tomas inquiet "Désolé."
    lysa "Tu vois ? Même lui regrette déjà."
    "Je laisse échapper un rire bref."
    tomas reflexion "Je comprends toujours pas pourquoi quelqu'un voudrait continuer."
    lysa fatigue "Parce que quelqu'un veut continuer."
    tomas "Oui mais pourquoi ?"
    lysa "Aucune idée."
    tomas "Ça te travaille pas ?"
    lysa blase "Si. Mais je peux rien en faire."
    noam reflexion "Pour une fois, t'as pas une théorie catastrophique ?"
    lysa "J'en ai douze."
    noam "Et ?"
    lysa "Elles sont toutes probablement fausses."
    "Elle boit une gorgée."
    lysa fatigue "Donc je vais éviter de choisir celle qui me plaît le plus juste pour avoir quelque chose à raconter."
    tomas "C'est étonnamment raisonnable."
    lysa blase "Merci. Ça me dégoûte."
    noam "Et les plaques ?"
    tomas reflexion "Je revérifierai demain."
    lysa "Pourquoi ?"
    tomas "Parce que ça m'énerve aussi."
    lysa blase "Ah. Voilà une meilleure raison."
    tomas "Le système dit qu'elles sont là. Elles sont pas là. C'est..."
    noam "Pas normal."
    tomas "Voilà."
    "Une perceuse démarre au loin."
    pause 0.4
    lysa "Et Elias va probablement démonter la station entière avant d'accepter ça."
    noam "Il a déjà commencé."
    tomas "Techniquement, tout ce qu'il a démonté aujourd'hui était inutilisé."
    lysa blase "Tu vas vraiment défendre ça devant Kami quand il aura arraché un mur porteur ?"
    tomas surpris "Il arrachera pas un mur porteur !"
    lysa "J'espère."
    "La perceuse s'arrête."
    pause 0.5
    noam fatigue "On devait rentrer aujourd'hui."
    "Cette fois, personne ne plaisante."
    tomas inquiet "Ouais."
    lysa fatigue "Ouais."
    "Je regarde ma tasse."
    noam "Neuf jours."
    lysa "On en a déjà fait vingt."
    noam "C'est censé me rassurer ?"
    lysa blase "Non. C'est juste des maths."
    tomas "Des maths plutôt déprimantes."
    lysa "C'est les meilleures."
    "On reste encore quelques minutes à parler de rien. Pas du vote, pas de qui a demandé à rester, pas de la navette."
    "Juste de trucs suffisamment petits pour ne pas donner envie de cogner dans un mur."
    $ hideGroup()
    # Durée : ~1m50
    # Total : ~17m00

label _21_0_1_1_0_0_FIN_JOURNEE:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    stop music fadeout 0.8
    "Quand je retourne vers ma chambre, Elias est toujours là."
    $ showGroup([
        ("elias", "fatigue", 0.35),
        ("noam", "fatigue", 0.65),
    ])
    "Il est assis par terre devant une plaque fraîchement fixée, la perceuse posée entre ses jambes."
    noam "Tu comptes t'arrêter ?"
    elias fatigue "Ouais."
    noam "Quand ?"
    elias "Bientôt."
    noam "C'est pas une heure."
    elias "Merci Tomas."
    noam taquin "Je prends ça comme un compliment."
    "Il souffle du nez."
    elias ecoute "J'en ai fait deux de plus."
    noam "Avec les plaques de fortune ?"
    elias "Ouais. C'est moche."
    noam "Ça te ressemble."
    elias colere "Va te coucher."
    noam "D'accord."
    "Je fais deux pas avant de me retourner."
    noam reflexion "Elias."
    elias "Quoi ?"
    noam "Si les vraies plaques réapparaissent demain..."
    elias fatigue "Je vais être très content."
    noam "Et si elles réapparaissent pas ?"
    "Il regarde le morceau de métal devant lui."
    elias "Je continuerai sans."
    noam "Ça te suffit ?"
    elias ecoute "Non."
    pause 0.3
    elias fatigue "Mais c'est mieux que de rester planté à attendre qu'on me rende ce qu'on m'a pris."
    "Je hoche la tête."
    noam "Bonne nuit."
    elias "Ouais."
    "Je rentre dans ma chambre."
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    "Mon sac est toujours contre le bureau."
    "Je pourrais le défaire."
    "Je ne le fais pas."
    "Ce matin, je pensais ne passer que quelques heures de plus dans cette pièce. Maintenant il me reste neuf jours."
    "Je m'allonge sans me changer complètement."
    think "Certains veulent continuer les votes."
    "Je ne sais pas qui."
    think "Six plaques de métal ont disparu."
    "Je ne sais pas pourquoi."
    "Pour l'instant, ce sont juste deux problèmes différents dans une journée qui en avait déjà assez."
    "Je ferme les yeux."
    "Au loin, la perceuse d'Elias reprend une dernière fois."
    pause 0.8
    "Puis elle s'arrête."
    stop music fadeout 1.5
    call end_day("22") from _call_j21_stay_end_day_22
    return
    # Durée : ~1m20
    # Total : ~18m20
