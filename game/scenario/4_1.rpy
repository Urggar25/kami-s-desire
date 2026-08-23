label _4_1_REVEIL_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5
    $ current_day = 4
    $ noam_has_juliette_drawing = True
    $ current_period = "Matin"

    pause 1.2

    $ blink()
    "Je me réveille sous la lumière bleue des veilleuses."
    $ blink()
    think "Hier, douze doigts ont choisi le vert. Maintenant, c'est réel."
    think "On a changé les choses. Reste à savoir pour qui."

    $ blink()
    think "Mon cœur va trop vite. La nuit n'a rien calmé."
    think "On a supprimé les bons. Coupé une dépendance à Kami."
    think "Est-ce qu'on a aussi coupé le filet qui retenait les plus fragiles ?"

    $ blink()
    think "Limen n'a ni champs, ni outils, ni réserve. Les riches, eux, avaient déjà tout."

    think "Julian levait le poing. Ryn frappait la table. Kael baissait la tête. Moi, j'étais au milieu. Presque silencieux."
    think "J'ai voté, puis laissé les autres porter les mots."
    think "Si le marché ne sauve que ceux qui peuvent acheter, mon vote aura juste donné un nouveau nom à la faim."

    pause 2.0

    think "Sur la table, la famille d'un ami sourit encore depuis une photo."
    think "Je me demande s'ils sourient encore ce matin."

    play sound sfx_announce
    "Un bip aigu retentit ; l'écran mural s'allume."
    pause 1.0

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "8 heures pile, mes petits pionniers du chaos !"
    kami "Levez-vous, la révolution n'attend pas !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Petit point matinal, puisque vous adorez qu'on vous mette le nez dans les conséquences :"
    kami "Nexus et Orbite se régalent déjà. Marchés improvisés, trocs qui fleurissent, pièces artisanales qui tintent."
    kami "Pendant ce temps à Limen… disons que les files d’attente sont plus longues que vos listes de regrets."
    kami "Quelques trocs sauvages, quelques poings serrés, quelques ventres qui crient."
    kami "Et à Orbite ? Une petite alarme hier soir. Rien de grave… pour l’instant."
    kami "Alors, champions du changement : toujours fiers de votre gros bouton vert ?"
    kami "Ou est-ce que la victoire commence à laisser un petit arrière-goût ?"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Mais oh ! Pourquoi je vous spoile ?!"
    kami "Vous aurez l'occasion de voir tout ça EN PERSONNE à la cafétéria !"

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.5

    think "L'écran s'éteint. Mes mains tremblent encore."
    think "On a ouvert la porte. Elle, au moins, sait déjà ce qui va en sortir."

    pause 1.5

    play sound sfx_drop
    "Un cri étouffé traverse le couloir, suivi d'un choc contre une porte. Puis le silence."
    think "Je ne sais pas si ça a déjà commencé. Je sais seulement que ça ne s'arrêtera pas là."

    jump _4_1_CAFETERIA_ECRANS

# Durée : 1m35
# Total : 1h 55m 35s

label _4_1_CAFETERIA_ECRANS:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.8

    pause 1.0

    "J’entre dans la cafétéria. L’air est chargé : rations réchauffées, métal chaud, tension palpable."
    think "Tout le monde est déjà là, rivé aux écrans."

    think "Je prends une ration au hasard. Pas faim. Juste besoin de faire semblant."

    "Les images défilent en boucle, commentées par une voix synthétique neutre :"

    "Nexus : premiers marchés locaux ouverts. Échanges fluides. Pièces artisanales acceptées."
    "Orbite : exportations en hausse. Demande forte pour les outils et les filtres."
    "Limen : files d’attente devant les anciens points de distribution. Premiers signes de troc sauvage."

    $ showGroup([
        ("lysa", "determine"),
        ("kael", "calme"),
        ("ryn", "colere"),
        ("julian", "detendu"),
        ("mara", "joie"),
        ("tomas", "hesitation"),
        ("elen", "joie"),
        ("iris", "desaccord"),
        ("nyra", "raison"),
        ("noam", "raison"),
        ("sael", "mefiant"),
    ])
    lysa "Regardez : ils s'organisent. Même sans Prométhée, Limen a trouvé le troc. C'est presque encourageant."

    kael "Orbite tient. Pas d'alarme critique. Pas de laser. Stabilité supérieure à mes prévisions."

    ryn "Stable pour vous, peut-être."
    ryn "À Limen, ils commencent à se battre pour un sac de patates. C’est ça votre stabilité ?"

    julian "Ce n'est que le début. Les échanges existent déjà ; imaginez ce que nous pouvons bâtir en les organisant."
    julian rire "Et, détail non négligeable, Limen a donc trouvé des patates."

    mara "Des marchés, des marchandises, des gens qui choisissent enfin. J'allais finir par séduire le distributeur pour obtenir du café."

    tomas "Euh… les rapports montrent que les prix sont déjà en train de fluctuer."
    tomas "À Nexus, certains produits ont doublé en valeur en 24 heures."
    tomas "C’est… c’est pas forcément mauvais, hein ?"

    elen "C'est le début, c'est normal ! Et puis c'est gééénial : les gens vont enfin choisir !"
    elen "Des épices, des vêtements neufs, des trucs qui sentent bon… Oh ! Peut-être du vrai chocolat !"

    iris "Choisir avec quoi ? L'air de leurs poches ? Les pauvres regarderont les rayons pleins depuis dehors. Magnifique progrès."

    nyra "Les gens veulent échanger, ici comme ailleurs. Le vote leur a donné l'espace."
    nyra "Maintenant, qu'est-ce qui leur manque ? Des règles claires, pour que la liberté ne profite pas seulement aux mieux armés."

    noam "Ce que j’entends, c’est que... les repères ont disparu."
    noam "Il me semble qu’on a enlevé quelque chose sans vraiment prévoir ce qui prendrait la place."
    noam "Les gens s’organisent. Certains. Pas partout."

    sael "…"
    sael "Ils s'organisent déjà. Les vivants trouvent toujours un chemin quand on retire l'ancien."
    sael "La question est de savoir combien de morts le baliseront."

    think "Visages fatigués à Limen. Sourires crispés à Nexus. Ma ration reste intacte."
    think "Certains n'ont rien à manger ce matin."


    think "Lysa me vise du coin de l'œil. Je connais déjà la question."
    lysa determine "Tu regrettes déjà ?"
    lysa "Ce n'est pas toi qui voulait qu'on se batte pour faire changer les choses ?"
    lysa sourire "Au moins, là, on a réussi."

    noam "Tu veux savoir si je regrette. Enfin… je ne sais pas encore quel prix donner à la réponse."


    think "Chacun regarde les écrans comme un accident dont nous aurions signé l'autorisation."
    think "On a gagné hier. Ce matin, la facture commence à circuler."


    jump _4_1_TEMPS_LIBRE_1

    return

# Durée : 1m20
# Total : 1h 56m 55s

label _4_1_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Quelques heures avant le prochain rassemblement. De quoi éviter une décision importante."
    think "Je ne sais pas encore quoi faire."

    call START_FREE_TIME("_4_1_RETOUR_CONCLAVE_ANALYSE") from _call_START_FREE_TIME_4_1

# Durée : 1m05
# Total : 1h 58m 0s

label _4_1_RETOUR_CONCLAVE_ANALYSE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.8

    pause 1.2

    think "L'après-midi traîne encore quand l'alarme tranche le couloir."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Attention, attention, mes petits représentants adorés !"
    kami "Rassemblement immédiat dans la salle principale."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On a du pain sur la planche. Il faut qu'on prépare le prochain vote !"
    kami "Bougez-vous, nos téléspectateurs ne vont pas attendre vos siestes digestives."

    scene bg_couloir at adaptive_fullscreen with dissolve

    "L'écran s'éteint. Nous gagnons la salle au compte-gouttes."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 1.5

    think "Julian arrive le premier — évidemment. Ryn suit, poings serrés ; Elen est nerveuse, Mara déjà amusée."

    $ showGroup([
        ("julian", "determine"),
        ("ryn", "colere"),
        ("elen", "inquiet"),
        ("mara", "agace"),
        ("tomas", "hesitation"),
        ("iris", "desaccord"),
        ("kael", "triste"),
        ("nyra", "raison"),
        ("noam", "raison"),
        ("lysa", "blase"),
        ("sael", "mefiant"),
    ])
    julian "Nous sommes tous là ? Alors avançons. Le changement n'attend pas ceux qui le regrettent."

    ryn "Finir quoi ? Encore un vote pour tous nous faire crever ?"

    elen "C'est peut-être une bonne nouvelle, non ? On a déjà gagné une fois ! Enfin… gagné-gagné, je sais pas, mais gagné !"

    mara "Gagné ? On a ouvert la boîte de Pandore et maintenant on admire l'emballage. Nuance."

    tomas "Euh… je crois qu’on devrait écouter Kami d’abord…"
    tomas "Avant de paniquer… Enfin, on sait pas ce qui va être annoncé…"

    iris "Paniquer ? Non, surtout pas. Regardons Limen s'enfoncer avec une organisation exemplaire."

    kael "Et Orbite… si la chaîne logistique casse…"
    kael "Non. Pas assez de données."

    nyra "Tout le monde veut savoir ce qui vient. Alors pourquoi nous faire attendre ?"

    noam "On attend Kami. Enfin… je ne vois pas ce qu'on pourrait faire d'autre."

    lysa "Trois jours avant le vote. Ulysse a connu des traversées moins longues, et avec moins de discours inutiles."

    sael "…"
    sael "Le silence a changé depuis ce matin. Quelque chose arrive avec lui."

    think "Personne ne répond au pressentiment de Sael. Mauvais signe."

    play sound sfx_announce
    pause 1.0

    stop music fadeout 1.0
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 1.0

    kami "Bon, maintenant que vous êtes tous là, on peut commencer."
    kami "Prochain vote, mes chéris :"
    kami "Ahhh !! Roulement de tambour !"

    play sound sfx_tambour
    pause 2.0

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser les déplacements de personnes entre les districts ?"
    kami "Si vous votez pour, les personnes pourront voyager d'un district à l'autre."
    kami "Si vous votez contre, on garde la même chose qu'aujourd'hui."

    $ j2_vote_codex_unlocked = True
    $ j45_vote_codex_active = True
    $ unlock_dossier_chapter(2)
    $ renpy.notify("Tablette mise à jour — Chapitre 2 débloqué")
    show screen tablet_home

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Et promis, vous ne serez pas surpris cette fois-ci."
    kami "L'énoncé est parfaitement clair."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_low_tension.mp3" fadein 1.0

    think "Deux boutons immenses. Au cas où nous aurions oublié notre fonction."

    $ showGroup([
        ("ryn", "colere"),
        ("kael", "triste"),
        ("sael", "mefiant"),
        ("lysa", "blase"),
        ("noam", "determine"),
        ("julian", "determine"),
        ("elias", "determine"),
        ("iris", "desaccord"),
        ("mara", "agace"),
        ("nyra", "raison"),
        ("tomas", "hesitation"),
    ])
    ryn "Il faut voter pour."
    ryn "J’ai vu ce que les frontières fermées font aux gens."
    ryn "À Limen, on gardait une muraille invisible. Les Gardiens étaient ..."
    ryn triste "Enfin... Je refuse que ça continue. Il faut laisser les gens bouger !"

    pause 0.8

    kael "Les gardiens ? De qui tu parles ?"

    sael "…"
    sael "Les Gardiens… ce sont ceux qui ont tracé la frontière entre Limen et les autres districts."
    sael "Ils ont exploré. Ils ont creusé la tranchée. Ils sont morts par milliers les premiers mois en cherchant précisément le tracé de la frontière."
    sael raison "À Limen, on les vénère. Ils ont sacrifié leur vie pour qu’on reste chez nous."
    sael triste "Aujourd'hui, celui qui traverse est immédiatement abattu. Les morts n'appellent pas cela une frontière."

    ryn "Et je refuse de continuer à payer ce prix."
    ryn "Je veux que ça s’arrête, Sael. Je veux que ça s’arrête pour de bon."

    kael triste "Ces tirs de rayon ... On sait que c’est définitif."
    kael triste "Mais on fait semblant que c’est loin. Toi… tu étais là. Tu voyais leurs visages avant."

    lysa "Si je comprends bien, t’étais là pour les empêcher de passer."
    lysa "Et maintenant tu veux les laisser passer."

    pause 1.0

    noam "Ce que j’entends, Ryn... c’est que tu as fait ça pour protéger les gens."
    noam hesitation "Mais je me demande si on peut encore vivre comme ça."
    noam "Libre circulation... la fin des murs. Des lasers. Des gardiens. Il me semble que c’est ce que ça veut dire."

    ryn colere "Ça marquera peut-être la fin de notre mission. Tant mieux."

    julian "Enfin quelqu'un qui parle avec le cœur. La libre circulation, c'est un projet commun : s'aider, partager, survivre ensemble."

    lysa blase "Dans la cité idéale de Platon, sûrement. Ici, comment tu empêches les gens de s'entretuer ?"
    lysa reflexion "Les frontières sont cruelles. Le vide juridique qui suit leur disparition le sera aussi."

    elias "J'suis d'accord avec Lysa. Ça fait qu'un an que les guerres sont finies."
    elias reflechit "Kami a arrêté les combats, ouais. Mais la colère des gens, elle a pas disparu. C'est chaud de faire comme si."

    iris "Ah, voilà. On veut la liberté, mais pas les pauvres devant chez soi. Limen appréciera la subtilité."

    sael mefiant "Tu te trompes."
    sael "Je voterai contre. Les morts de Limen ont vu ce que les routes transportent quand la paix cède."
    sael peur "Pour vous, c'est un déplacement. Pour moi, c'est la guerre qui retrouve un chemin."

    think "Sael croise les bras. Son ton ferme déjà la discussion."

    elias colere "Sael, si les gens bougent, les ressources bougent aussi. Des gens mangent."
    elias jaloux "Tu peux pas dire non juste parce que t'as peur. C'est chaud, réfléchis !"

    sael colere "Réfléchir ?"
    sael culpabilite "J’ai réfléchi ! C’est non !"
    sael "Tu ne comprends rien !"
    sael triste "Tu ne sais rien."

    hide sael
    with moveoutright

    play sound sfx_door volume 8.0
    "Sael se lève d’un coup. Elle tourne les talons et quitte la salle en claquant la porte."
    with hpunch
    with vpunch
    with hpunch

    pause 0.5

    mara "Non mais attends Sael ! Reviens !"
    mara doute "Putain, vous cassez les couilles !"

    hide mara
    with moveoutright

    play sound sfx_door volume 8.0
    "Mara se lève et la suit en courant hors de la pièce."
    with hpunch

    julian determine "Laissez-la. Elle ne changera pas d’avis."
    julian inquiet "Mais on peut pas laisser la peur dicter notre avenir."

    noam raison "Je me demande si c’est vraiment juste de la peur."
    noam reflexion "Ce que j’entends dans ce que dit Sael... les territoires. Peut-être que c’est là que tout commence."

    ryn colere "On ne peut pas laisser ça comme ça."
    ryn determine "Sael est trop bornée. Elle va tout faire foirer !"

    kael inquiet "Elle a ses raisons."
    kael triste "On a tous nos démons."

    nyra "Le texte est clair. Nos besoins aussi. Alors qu'est-ce qu'on peut construire entre les deux ?"

    tomas "Euh… Il faut dire que ça peut aussi aider les marchandises à bouger plus rapidement."
    tomas "Mais Bon, c'est sûr que ça risque aussi de créer des incidents."

    iris desaccord "Bravo. Vous avez transformé un débat politique en concours pour savoir qui blesserait Sael le plus vite. Très efficace."

    "Sur ces mots, Iris quitte à son tour la pièce."

    hide iris
    with moveoutleft

    think "Le silence retombe. Nous calculons tous avec des unités différentes."

    jump _4_1_APRES_CLASH_PRE_FETE

# Durée : 3m05
# Total : 2h 01m 05s

label _4_1_APRES_CLASH_PRE_FETE:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.5

    pause 1.2

    $ showGroup([
        ("julian", "decu"),
        ("elen", "joie"),
        ("noam", "raison"),
        ("nyra", "surpris"),
    ])
    julian "Bon… on va pas rester plantés là toute la soirée."
    julian joie "On a gagné un vote. On mérite au moins un verre."

    elen "C’est vrai !"
    elen content "Allez, on fait une petite fête. Juste pour décompresser."
    elen "Je m’occupe de tout. Nourriture, boisson, musique, ambiance !"

    noam "Une fête… maintenant ?"
    noam "Après ce qui vient de se passer ?"

    elen "Justement après !"
    elen "Si on reste tous à ruminer, on va finir par se détester."
    elen reflexion "Nyra, tu peux aller chercher Mara et Sael ? Dis-leur que c’est juste pour boire un coup et se détendre."

    nyra "Moi ?!"
    nyra reflexion "Bon… je vais essayer."
    nyra neutre "Je ne te garantis rien. Mais je vais leur laisser une bonne raison de venir."

    hide nyra
    with moveoutright

    think "Nyra soupire, mais elle part. Elen a trouvé le désir auquel l'accrocher : réparer le groupe."

    show noam neutre
    elen "Et toi, Noam…"
    elen "Tu peux aller chercher Iris ?"
    elen "J'imagine qu'elle est dans sa chambre. Elle a besoin de se changer les idées."

    think "Je n'ai pas le cœur à refuser. Comme souvent."


    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Direction la chambre d'Iris. Excellente idée, si on oublie toutes les raisons du contraire."

    scene bg_dortoir at adaptive_fullscreen with dissolve

    "La porte est entrouverte. Je frappe doucement."

    iris "C’est qui ?"

    think "Iris est recroquevillée sur son lit. Elle détestera que je l'aie vue comme ça."
    scene bg_chambre_iris at adaptive_fullscreen with dissolve

    think "Elle a l'air épuisée. Le sarcasme tient encore debout à sa place."

    $ showGroup([("iris", "triste", 0.50)])
    iris "Ah… c’est toi."
    iris "T’es venu me faire la morale ?"

    think "Je m'assois à côté d'elle. Pas trop près."

    scene bg_cg018 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg018")

    noam "Elen organise une fête. Enfin… elle essaie surtout d'empêcher tout le monde de s'entretuer."

    iris "Une fête après ça ? Sael claque une porte, Mara lui court après et notre réponse stratégique, c'est l'alcool ? Brillant."

    noam "Tu veux dire qu'on va boire pour oublier. Enfin… rester seule ne changera rien non plus."
    noam "Ça pourrait nous faire du bien. Peut-être."

    iris "Tu marques un point. Ça m'agace."
    iris "J'arrive. Mais si Julian porte un toast de plus de quinze secondes, je lui fais avaler son verre."

    noam "Je pourrais l'arrêter. Enfin… après quinze secondes. Pour le spectacle."
    
    "Iris retient un sourire et se lève."

    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    iris "Ne prends pas cet air satisfait."
    noam "Je n'ai pas d'air satisfait."
    iris "C'est pire. Tu as ton air innocent."

    scene bg_couloir at adaptive_fullscreen with dissolve
    think "La musique nous rejoint avant la salle. Au moins, Elen n'a pas perdu de temps."

    $ repos_party_active = True
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "Elen a sorti les rations alcoolisées. Julian sert, Ryn boit, et Nyra revient avec Mara et Sael."

    $ showGroup([("elen", "content", 0.50)])
    elen "Ah ! Vous êtes lààà ! Prenez un verre !"
    elen joie "On a gagné hier. Enfin, aujourd'hui c'est compliqué, mais hier on a gagné, donc ça compte encore un peu !"

    think "On rit déjà trop fort. La peur, elle, n'a même pas pris la peine de se cacher."

    jump _4_1_FETE_IMPROVISEE

# Durée : 1m25
# Total : 2h 02m 30s

label _4_1_FETE_IMPROVISEE:

    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    pause 1.0

    "Des tissus assombrissent les veilleuses. Une enceinte couvre presque le bourdonnement du Conclave."

    elen "J'ai compté les verres trois fois ! Et les rations deux fois. Enfin… après j'ai goûté, donc les chiffres sont peut-être moins fiables."

    iris "Une organisation irréprochable. Kami peut démissionner."

    elen "Tu vois ! Je savais que t'allais aimer !"

    iris "Ce n'était pas— Laisse tomber."

    $ showGroup([("julian", "sourire", 0.88), ("elias", "reflechit", 0.12), ("lysa", "blase", 0.50)])
    julian "À nous, qui avons osé changer les choses — et qui aurons le courage d'en répondre."


    elias "À l'espoir, ouais. Mais si demain tout part en vrille, c'est chaud de trinquer à ça aujourd'hui."

    lysa "Les soldats grecs buvaient avant la bataille. Nous, on ne sait même pas si on fête la victoire ou la prochaine défaite."
    lysa sourire "Peu importe. Santé."

    mara "Ça, c'est l'esprit. Déprimant, cultivé, alcoolisé."

    think "Quelques verres se lèvent. L'écran s'allume avant qu'ils se touchent. Évidemment."

    play sound sfx_announce
    pause 1.0
    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous n'alliez quand même pas faire une fête sans moi ?"
    kami "Mes petits rebelles éméchés… je suis blessée. Moi qui fournis l'alcool, les murs et la surveillance."
    kami "Trinquons à votre courage ! Ou à votre inconscience. J'attends encore les résultats d'analyse."

    think "Un verre virtuel, des lumières rouges et vertes, puis plus rien. Même son intrusion a une mise en scène."

    hide screen kami_broadcast_ui
    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_soft_neon_morning.mp3" fadein 2.5

    elen "Bon ! Si même notre geôlière trinque, on a officiellement le droit de monter le son !"

    ryn "Ça, c'est la règle la plus sensée de la journée."

    think "Les verres se remplissent. Ryn danse avec Elen. Kael va jusqu'à sourire. Le miracle est probablement alcoolisé."

    $ showGroup([
        ("mara", "ivre"),
        ("tomas", "hesitation"),
        ("iris", "desaccord"),
        ("lysa", "jaloux"),
    ])
    mara "Bon, ça suffit les mines d'enterrement. J'ai une bouteille vide et de très mauvaises intentions. Qui joue ?"

    "La bouteille tourne sur la table basse."

    tomas "Euh… c'est quoi, le jeu de la bouteille ? J'ai jamais joué."

    mara taquin "Oh, Tomas… Cette innocence va me tuer."
    mara "On tourne. Deux personnes sont désignées. Elles s'embrassent si elles en ont envie."
    mara "Et si quelqu'un dit non, c'est non. Je suis joueuse, pas gardienne de prison."

    iris "C'est ridicule. Et statistiquement conçu pour créer des problèmes. Je vais me coucher."

    "Mara lui barre le passage d'un pas, sans la toucher."

    mara joie "Attends, Iris. Tu peux rester sans jouer."
    mara "Mais priver cette soirée de ton regard assassin ? Là, ça devient personnel."

    iris fatigue "Tu es épuisante."
    iris gene "Bon. Je reste. Et je joue… seulement si Noam joue aussi."

    lysa "Pourquoi Noam ?"

    iris gene "Pour rien ! Enfin— parce que c'est moins stupide si tout le monde participe. C'est tout."
    
    mara "Bien sûr. Une décision purement scientifique."

    iris "Un mot de plus et je révise mon oui."

    menu:
        "Accepter de jouer":
            $ jeu_bouteille_accepte = True
            noam "D'accord. Enfin… puisque mon sacrifice fait avancer la science."
            jump _4_1_JEU_BOUTEILLE

        "Refuser poliment":
            $ jeu_bouteille_accepte = False
            noam "Pas ce soir."
            mara "Refus accepté. Tu restes quand même témoin des dégâts."
            jump _4_1_FIN_SOIREE

    return

# Durée : 1m30
# Total : 2h 04m 00s

label _4_1_JEU_BOUTEILLE:

    scene bg_repos_fete at adaptive_fullscreen with dissolve
    play music "music/bgm_romantic_atmosphere.mp3" fadein 1.5

    pause 0.6

    $ showGroup([("mara", "ivre", 0.50), ("noam", "surpris", 0.88), ("lysa", "blase", 0.12)])
    mara "Premier tour ! Petite bouteille, choisis bien. J'ai une réputation à tenir."

    "La bouteille ralentit… s’arrête sur Noam."

    noam "Moi. Évidemment."

    "La bouteille pointe ensuite Lysa."

    lysa "Évidemment. Les Parques ont un sens de l'humour médiocre."
    lysa "Tu es d'accord, Noam ?"

    noam "Oui. Enfin… oui."

    mara "Le couple parfait ! Et pas de négociation diplomatique pendant le baiser."

    scene bg_cg019 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg019")

    "Lysa hausse un sourcil et se penche avec un sourire en coin."
    think "Réfléchir plus longtemps ne rendra pas ça moins réel."
    "Nous nous embrassons. C'est bref, mais ses lèvres restent contre les miennes une seconde de trop."

    elen "Ooooooh !"

    iris "Respire, Elen."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showGroup([
        ("julian", "joie"),
        ("elen", "joie"),
        ("lysa", "gene"),
        ("mara", "ivre"),
        ("tomas", "gene"),
        ("sael", "mefiant"),
    ])
    julian "Un premier tour particulièrement convaincant. Julian valide le concept."

    elen "Lysa ! T'as rougiii ! C'est beaucoup trop mignon !"

    lysa "C'est l'alcool. Pas lui."
    lysa "Cela dit, il embrasse mieux qu'il ne termine ses phrases. La barre était basse."

    noam "Je vais choisir de prendre ça pour un compliment."


    mara "Deuxième tour ! La bouteille exige davantage de chaos."

    "La bouteille tourne… s’arrête sur Tomas."

    tomas "Oh non… Pourquoi moi ?"

    "La bouteille pointe Sael."

    sael "…"

    mara "Sael et Tomas. Là, même moi je n'aurais pas osé écrire ça."

    sael "Tomas ?"

    tomas "Je… oui. Enfin, si toi aussi."

    sael "Alors viens. Il n'y a rien à craindre ici."

    scene bg_cg020 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg020")

    "Sael pose une main sur la nuque de Tomas et l'embrasse doucement. Quand elle recule, il est écarlate."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    $ showGroup([
        ("elen", "joie"),
        ("julian", "taquin"),
        ("tomas", "gene"),
        ("mara", "ivre"),
        ("kael", "surpris"),
        ("elias", "jaloux"),
    ])
    elen "Sael ! C'était si douuuux ! Tomas, tu respires encore ?"

    julian "La question mérite effectivement une réponse officielle. Tomas ?"

    tomas "Je… je crois."

    mara "Il vit ! Et il vient de gagner le silence le plus jaloux de la pièce."
    mara "Dernier tour. On finit en apothéose."

    "La bouteille tourne… s’arrête sur Kael."


    kael "Moi ?"

    "La bouteille repart et pointe Elias."

    elias "Euh… Moi ?"

    mara "Kael et Elias. La bouteille a du goût."

    kael "Je…"
    kael gene "Je ne sais pas."

    elias "T'es pas obligé, Kael. Vraiment."
    elias "Moi, ça me va. Mais si toi ça te va pas, on passe. C'est pas compliqué."

    kael "… D'accord."

    elias "T'es sûr ?"

    kael "Oui. Avant que je change d'avis."

    scene bg_cg021 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg021")

    "Le baiser commence avec prudence. Elias pose une main sur la nuque de Kael ; aucun des deux ne recule tout de suite."

    elias "Pour le beau jeu… c'est chaud, quand même."

    kael "Oui. Le jeu."

    scene bg_repos_fete at adaptive_fullscreen with dissolve

    mara "Je retire tout ce que j'ai dit : cette bouteille est une artiste."

    $ showGroup([("mara", "ivre", 0.12), ("kael", "gene", 0.50)])
    mara "C'était indécemment mignon. On remet ça demain ?"

    kael "Non. Définitivement non."

    jump _4_1_FIN_SOIREE

# Durée : 1m40
# Total : 2h 05m 40s

label _4_1_FIN_SOIREE:

    $ repos_party_active = False
    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    pause 0.8

    think "La fête se termine tard. Mon trajet jusqu'à la chambre manque de ligne droite."

    think "La porte se referme. Le monde tangue encore."

    scene bg_chambre at adaptive_fullscreen with dissolve

    think "Je tombe sur le lit et laisse mes chaussures décider seules de leur avenir."

    $ blink()
    think "Le vote. Les cris. Sael qui part. Sael qui revient. Puis les rires, comme un pansement posé trop vite."

    $ blink()
    think "On a gagné quelque chose hier. Je ne sais pas encore si c'est autre chose que le droit de perdre autrement."

    think "Me déshabiller ressemble à une décision. J'ai dépassé mon quota."
    $ blink()

    scene bg_cg012 at adaptive_fullscreen with dissolve
    think "Demain sera un autre jour. Formule pratique pour éviter de décider si j'ai envie de le voir."
    "Le sommeil m'emporte avant que je trouve une réponse."

    $ current_day = 5
    pause 2.0

    call end_day("5") from _call_end_day_5_1
    jump _5_1_REVEIL_CHAMBRE

# Durée : 0m35
# Total : 2h 06m 15s
