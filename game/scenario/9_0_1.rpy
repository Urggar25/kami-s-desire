# --------------------------------------------------------------------------------------------
# JOUR 9 — Réveil chambre
# Kami revient après deux jours de silence.
# Elle réveille directement Noam par annonce matinale.
# Convocation immédiate dans la salle du Conclave pour annoncer le prochain vote.
# --------------------------------------------------------------------------------------------

label _9_0_1_REVEIL_CHAMBRE:

    scene black

    $ current_day = 9

    play music "music/bgm_calm_not_peace.mp3" fadein 2.5

    $ blink()

    "Je dors mal."
    "Ou plutôt..."
    "Je dors par morceaux."

    "Un bruit dans le couloir."
    "Un craquement dans la cloison."
    "J'essaye de me souvenir d'une porte qu'on aurait pu ouvrir pendant mon sommeil."
    "Non... Ça ne me dit rien..."

    pause 0.5

    think "La chaise est toujours contre la porte."
    think "Elle n'a pas bougé d'un pouce."

    pause 0.4

    "Je commence à replonger."

    stop music fadeout 0.5

    pause 0.3

    play sound sfx_announce
    "Un bip strident déchire le silence."

    scene bg_chambre at adaptive_fullscreen with hpunch

    "L'écran mural s'allume."

    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.5

    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Oh bonjour, mes petits représentants !"

    pause 0.3

    "Je me redresse d'un coup."

    think "Oh non..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je vous ai manqué ?!"
    kami "Vous m'avez TEEELLLEMENT manqué !"

    pause 0.4

    think "Elle est revenue."

    "Sa voix est calme."
    "Toujours claire et nasillarde."
    "Presque chantante."

    "La même voix."
    "Le même ton."
    "Comme si elle n'avait jamais disparu."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Deux jours sans annonce matinale, c'était interminablement long !"
    kami "Une chose est sûre : il s'en est passé des choses pendant mon absence !"

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je sais."
    kami "C'était très dur."
    kami "Comment vous avez fait sans moi hein ?!"

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Rassurez-vous."
    kami "Votre longue période d'abandon émotionnel est terminée."

    pause 0.3

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Maman est de retour."

    "La phrase reste dans l'air."
    "Tout bonnement insupportable."

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve

    menu:
        "Repousser la chaise de la porte.":
            $ noam_j9_porte_bloquee = False

            "Je me lève."
            "Je pousse la chaise sur le côté."

            "Elle racle le sol avec un bruit sec."

            think "Ridicule."
            think "Comme si une chaise pouvait arrêter quoi que ce soit ici."

        "La laisser contre la porte encore quelques secondes.":
            $ noam_j9_porte_bloquee = True

            "Je ne bouge pas."
            "Je garde les yeux sur l'écran."

            think "Pas tout de suite."
            think "Je veux encore croire que cette chaise sert à quelque chose."

    pause 0.4

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Je constate que certains d'entre vous ont pris des initiatives décoratives pendant mon absence."

    pause 0.3

    kami "Certains d'entre vous ont presque barricadé leur porte de chambre..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Comme c'est MEUGNON !"

    "Mon ventre se serre."

    think "Elle sait. Elle sait tout."
    think "Évidemment qu'elle sait, putain."
    think "Comment on a pu croire que c'était fini ?!"

    kami "C'est touchant."
    kami "Un peu désordonné."
    kami "Mais touchant. Comme des enfants en train de construire leur cabane soit disant impénétrable."

    pause 0.5

    $ bc_show("noam", "surpris", px=-70, py=-50, pz=0.60)
    noam surpris "Qu'est-ce qui s'est passé ?!"

    "Ma voix sort avant que je puisse la retenir."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Oh oh, je vois que toi Noam, tu n'as pas froid aux yeux."
    kami "Tu veux donc savoir ce qu'il s'est passé ?"

    $ bc_show("noam", "reflexion", px=-70, py=-50, pz=0.60)

    pause 0.4

    think "Elle m'a entendu."
    think "Bien sûr qu'elle m'a entendu."

    noam inquiet "Tu as disparu pendant deux jours."

    pause 0.3
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Disparu ?"
    kami "Quel mot bien dramatique."

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "J'aurais aimé dire que c'était une expérience, mais NON."
    kami "Disons que j'avais besoin d'un peu de congés payés."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    
    kami "Et j'espère bien qu'ils seront payés !"
    kami "Un an que je travaille sans m'arrêter, toute la journée et toute la nuit !"

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Ah cette petite maintenance m'a fait le plus grand bien !"

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Ce matin, nous reprenons le programme officiel. C'est d'ailleurs à ça que vous servez !"

    pause 0.3

    kami "Tous les représentants sont convoqués immédiatement dans la salle du Conclave."

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Le prochain vote doit être annoncé."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Je vous recommande de ne pas traîner."
    kami "On n'a plus beaucoup de temps..."

    pause 0.4

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Aujourd'hui, soyez gentils."
    kami "Venez directement."

    pause 0.5

    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve

    "L'écran reste allumé quelques longues secondes."
    "Blanc."
    "Silencieux. Grésillant."

    "Pas de glitch."
    "Pas de coupure."
    "Pas de phrase déformée."

    think "Elle est de retour à la normale."

    if noam_j9_porte_bloquee:

        "Je finis par me lever."
        "Je pousse la chaise qui bloque encore la porte."

        "Le bois racle le sol."

        think "Voilà."
        think "Retour à la normale."
        think "Ou à ce qui porte ce nom ici."

    "Je passe une main sur mon visage."
    "Je cherche ma veste."

    think "Elle revient."
    think "Elle sourit."
    think "Elle nous convoque."
    think "Comme si rien ne s'était passé..."

    pause 0.4

    "Je regarde une dernière fois la chambre."
    "J'ouvre la porte."

    stop music fadeout 1.5

    scene black with fade

    jump _9_0_1_CONCLAVE_ANNONCE

label _9_0_1_CONCLAVE_ANNONCE:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    pause 0.5

    "Le couloir s'ouvre."
    "Les portes suivent, une à une."

    think "Kami est revenue."

    lysa blase "Bon."
    lysa "La pause du cauchemar est terminée. Bref."

    ryn fatigue "Avance."

    iris fatigue "Toujours aussi charmant."

    ryn "Pas aujourd'hui."

    mara stress "Aujourd'hui, personne n'est charmant."
    mara "Même moi, j'ai pas la force de vendre le produit."

    elen peur "Ça va aller. Enfin... ça peut aller. Peut-être."

    lysa blase "Elen."

    elen "Quoi ? Qu'est-ce qu'il y a ?"

    lysa triste "Pas maintenant, Elen."

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with dissolve

    pause 0.6

    $ showGroup([
        ("lysa",  "blase",    0.10),
        ("ryn",   "fatigue",  0.27),
        ("sael",  "inquiet",  0.43),
        ("kael",  "fatigue",  0.57),
        ("tomas", "inquiet",  0.73),
        ("iris",  "fatigue",  0.90),
    ])

    kael fatigue "Elle est revenue."

    iris fatigue "Oui."
    iris "Merci, Kael."
    iris "On adore commencer par l'évidence la plus déprimante possible."

    kael "Je sais."

    pause 0.2

    kael triste "Le penser et l'entendre, ce n'est pas la même chose."

    sael inquiet "Deux jours sans sa voix."
    sael "Puis elle revient."
    sael "Les mauvais présages aussi savent attendre."

    ryn fatigue "Elle revient toujours."

    lysa blase "Formidable."
    lysa "Si seulement on n'était pas contre l'entité la plus puissante du monde. Détail mineur."

    pause 0.4

    play sound sfx_announce
    stop music fadeout 0.8

    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.4

    kami "Bonjour, mes petits représentants."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Quelle ambiance."
    kami "On dirait que vous avez passé deux jours sans autorité maternelle."

    pause 0.3

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "C'est presque mignon."
    kami "Un peu pathétique, mais mignon."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le Conclave reprend son fonctionnement normal."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Troisième vote."

    play sound sfx_tambour
    pause 1.0

    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve

    kami "Autoriser les regroupements de plus de vingt personnes."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Actuellement, les regroupements de plus de vingt individus non déclarés sont interdits."

    kami "Cette interdiction relève du Commandement IV."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Organisation."
    kami "Rassemblement."
    kami "Mouvement collectif non autorisé."
    kami "Tous ces petits mots qui donnent aux foules l'impression d'avoir une colonne vertébrale."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Un vote unanime en faveur de l'amendement autorisera ces regroupements."

    kami "Ils resteront soumis à déclaration préalable."

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je sais."
    kami "Ce n'est pas la liberté totale."

    pause 0.3

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Mais chaque enfant doit apprendre à marcher avant de courir vers une insurrection."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "En cas d'échec du vote, l'interdiction actuelle restera en vigueur."

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Le vote aura lieu aujourd'hui."
    kami "Enfin... dans quelques instants."

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Essayez de ne pas tout gâcher trop vite."

    pause 0.5

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 0.5

    $ showGroup([
        ("tomas", "raison",    0.10),
        ("lysa",  "blase",     0.27),
        ("ryn",   "fatigue",   0.43),
        ("sael",  "inquiet",   0.57),
        ("noam",  "inquiet",   0.73),
        ("kael",  "fatigue",   0.90),
    ])

    tomas raison "Attendez."

    ryn fatigue "Quoi encore ?"

    tomas "Le libellé."

    lysa blase "Tomas."

    tomas raison "Non."
    tomas "Cette fois, c'est important."

    pause 0.2

    noam inquiet "Qu'est-ce qui ne va pas ?"

    tomas "Regroupements de plus de vingt personnes."
    tomas "Non déclarés."
    tomas "Commandement IV."

    ryn fatigue "Oui, on a entendu."

    tomas culpabilite "Pas comme ça."

    pause 0.2

    sael inquiet "Parle."

    tomas raison "Ce matin, je suis allé dans la salle du canon."
    tomas "Je voulais vérifier les exécutions. J'avais déjà vu une anomalie hier."

    ryn colere "Oui et ?!"

    tomas "Des gens quittent massivement les profondeurs de Limen."
    tomas "Beaucoup de gens."

    pause 0.2

    ryn colere "Hein ?! Combien ?"

    tomas culpabilite "Je n'ai pas le chiffre exact."

    ryn colere2 "Combien ?"

    tomas "Des milliers."
    tomas "Peut-être plusieurs dizaines de milliers."

    pause 0.3

    sael peur "Laisse-moi deviner. Ils remontent vers les frontières."

    tomas "Oui."
    tomas "Je pense qu'ils ont profité de l'absence de Kami."
    tomas "Ou de sa maintenance."
    tomas "Ils ont cru que c'était une ouverture pour passer les frontières malgré l'interdiction."

    lysa triste "Évidemment."

    tomas raison "Ils ont installé des campements."
    tomas "À plusieurs points de passage."
    tomas "Vers d'autres districts."

    pause 0.2

    kael inquiet "Des campements."

    tomas culpabilite "Migratoires."
    tomas "Improvisés."
    tomas "Et surtout non déclarés."

    pause 0.3

    noam inquiet "Et donc..."

    tomas "Donc ce sont des regroupements de plus de vingt personnes."

    pause 0.2

    ryn colere "Non. T'es pas sérieux."

    tomas "Si. Mal-"

    ryn "Non."
    ryn colere2 "Tu vas pas me dire que des gens qui fuient Limen vont crever parce qu'ils dorment trop nombreux dehors."

    tomas culpabilite "Je pense que le Commandement IV peut les viser."

    ryn "Putain !"
    ryn "Sérieux ?! Kami, c'est quoi ce bordel ?!"

    sael peur "Tous les campements ?"

    tomas "Tous ceux qui dépassent vingt personnes."
    tomas "Donc probablement presque tous."

    pause 0.3

    lysa blase "C'est pas un hasard si on vote sur ça."
    lysa "Tu vois bien que ce n'est pas une coïncidence."

    noam inquiet "Si le vote passe, ils peuvent rester groupés."

    noam "Et s'il échoue..."

    tomas culpabilite "L'interdiction reste."
    tomas "Et Kami applique le Commandement."

    pause 0.4

    play sound sfx_announce
    stop music fadeout 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    pause 0.3

    kami "Oh."

    pause 0.2

    kami "Vous avez tout compris."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Je suis fière de vous."
    kami "Enfin."
    kami "Surtout de Tomas."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Les campements limenois actuellement installés aux frontières relèvent bien du Commandement IV."

    pause 0.3

    kami "Ce sont des regroupements non déclarés."
    kami "De plusieurs centaines d'individus chacun."
    kami "Evidemment, ces mouvements collectifs ne sont pas autorisés."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "C'est très clair."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "J'ai cependant retardé l'application du Commandement."
    kami "Oh. Comme je suis adorable."
    kami "Sans mon intervention, ces campements ne seraient déjà plus un problème."

    pause 0.3

    kami "Pour vous laisser le temps de voter."

    pause 0.4

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Vous voyez ?"
    kami "Je peux être attentionnée."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Après le vote, le Commandement IV s'appliquera."
    kami "Avec ou sans modification."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Mais vous allez maintenant devoir voter, mes petits humains préférés."

    pause 0.3

    kami "Cette fois, réfléchissez bien à ce que vous allez faire !"

    pause 0.5

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0

    pause 0.5

    $ showGroup([
        ("ryn",   "colere",      0.10),
        ("sael",  "peur",        0.27),
        ("tomas", "culpabilite", 0.43),
        ("lysa",  "triste",      0.57),
        ("noam",  "inquiet",     0.73),
        ("nyra",  "fatigue",     0.90),
    ])

    ryn colere "Elle savait tout."

    nyra fatigue "Oui."

    ryn colere2 "Elle les a laissés s'entasser."
    ryn colere "Si ça se trouve, elle a fait semblant de ne pas être en maintenance pour les laisser s'entasser !"

    tomas culpabilite "Oui."
    tomas "C'est possible."

    ryn "Et maintenant elle appelle ça un vote."

    lysa triste "Non. Pas seulement."
    lysa "Elle appelle ça notre responsabilité."

    pause 0.3

    sael peur "On vote tous pour."

    noam inquiet "Oui."

    sael determine "Pas d'abstention."
    sael "Pas de détour."
    sael "Pas de lâcheté."

    ryn colere "Si quelqu'un vote contre—"

    noam determine "Ryn."

    ryn "Quoi ?"

    noam "Ne finis pas cette phrase."

    ryn colere2 "Tu veux vraiment faire le médiateur maintenant ?"

    noam determine "Oui."
    noam "Surtout maintenant."

    pause 0.2

    ryn "Des gens vont mourir."

    noam "Alors on essaie de les sauver."
    noam "Mais on ne commence pas par se menacer entre nous."

    pause 0.3

    ryn "T'as intérêt à être utile."

    noam "Je vais essayer."

    lysa blase "Rassurant."

    pause 0.4

    $ showGroup([
        ("mara",  "stress",     0.10),
        ("iris",  "inquiet",    0.27),
        ("elen",  "peur",       0.43),
        ("elias", "fatigue",    0.57),
        ("julian","inquietude", 0.73),
        ("kael",  "fatigue",    0.90),
    ])

    elen peur "Tout le monde va voter pour."
    elen "Il le faut. On ne peut pas laisser des gens mourir juste parce qu'ils sont trop nombreux au même endroit."

    iris inquiet "Elen..."

    elen "Non."
    elen peur "Ne me dis pas qu'il faut rester prudents."
    elen "Pas là."

    iris fatigue "Je voulais juste dire que oui."
    iris "Il le faut."

    pause 0.3

    elias fatigue "Moi aussi je voterai pour."
    elias "Je sais pas faire de beau discours."
    elias "Mais là, c'est pas compliqué. C'est des gens. On les laisse pas crever."

    mara stress "Pareil."
    mara "Personne ne peut hésiter en sachant ça ? Si ?!"

    julian inquiet "Pour aussi."
    julian "Évidemment."
    julian "Pour une fois, le rôle du Conclave est limpide : empêcher un massacre."

    pause 0.2

    kael fatigue "Pour."

    iris surpris "Kael ?"

    kael "Je parle peu."
    kael triste "Ça ne veut pas dire que je ne vois rien."
    kael "Ou que je suis inhumain."

    pause 0.4

    $ showGroup([
        ("tomas", "raison",     0.10),
        ("lysa",  "blase",      0.27),
        ("ryn",   "colere",     0.43),
        ("sael",  "determine",  0.57),
        ("nyra",  "raison",     0.73),
        ("noam",  "determine",  0.90),
    ])

    tomas raison "Il faudra parler aux abstentionnistes probables."
    tomas "S'abstenir revient à laisser la règle actuelle tuer."

    ryn colere "J'espère bien oui."

    noam determine "C'est pas notre seul problème."

    ryn "Putain... Quoi encore ?!"

    sael determine "Parle Noam."

    pause 0.2

    noam triste "Kami a été claire."
    noam "Le Commandement s'appliquera, avec ou sans modification."
    noam determine "Et les regroupements doivent être déclarés avant d'exister."

    pause 0.3

    ryn colere "Et alors ?"

    noam determine "Et alors les campements existent déjà."

    pause 0.2

    tomas culpabilite "Noam a raison."

    ryn colere "Explique."

    tomas raison "Préalable, ça veut dire avant."
    tomas "Avant le regroupement."
    tomas "Avant le campement."
    tomas "Avant que les gens soient déjà sur place."

    lysa blase "Merci Tomas."
    lysa "On adore les définitions qui sentent le charnier."

    tomas culpabilite "Lysa. Pas maintenant. Tais-toi et écoute."

    lysa triste "...?"

    pause 0.3

    nyra raison "Si Kami applique la règle strictement..."
    nyra "Même un vote pour ne régularisera pas automatiquement les campements actuels."

    ryn colere2 "Non ?!"
    ryn "Putain, t'es sûr ?!"

    noam triste "Non. Le vote autorise les regroupements."
    noam "Mais seulement quand ils sont déclarés."

    ryn colere "Ils pouvaient pas déclarer !"
    ryn "Elle était absente !"

    lysa blase "Et tu crois que ça va l'émouvoir ?"
    lysa "Carthage a brûlé pour moins de paperasse."

    pause 0.3

    $ showGroup([
        ("mara",  "stress",     0.10),
        ("iris",  "inquiet",    0.27),
        ("elen",  "peur",       0.43),
        ("elias", "fatigue",    0.57),
        ("julian","inquietude", 0.73),
        ("kael",  "fatigue",    0.90),
    ])

    elias fatigue "Attends."
    elias "Donc on vote pour..."
    elias inquiet "Et ils peuvent crever quand même ? C'est chaud. C'est vraiment chaud."

    iris inquiet "C'est une blague ?"
    iris "Dites-moi que c'est une blague nulle."
    iris fatigue "Même une blague de Mara, je prends."

    mara stress "Même moi, je suis pas assez tordue pour pondre ça."

    elen peur "Mais... non."
    elen "Non, ça n'a aucun sens."
    elen "Si on vote pour les sauver, ça doit les sauver. Sinon le mot sauver sert à quoi ?"

    kael fatigue "Pas forcément."

    elen "Kael..."

    kael triste "Je suis désolé."
    kael "Mais Kami n'a pas dit qu'elle les sauverait."
    kael "Elle a dit que le Commandement s'appliquerait après le vote."

    julian inquiet "C'est un piège."
    julian "Une astuce rhétorique monstrueuse. Mais elle a laissé une faille."

    pause 0.3

    $ showGroup([
        ("tomas", "raison",     0.10),
        ("lysa",  "triste",     0.27),
        ("ryn",   "colere",     0.43),
        ("sael",  "determine",  0.57),
        ("nyra",  "raison",     0.73),
        ("noam",  "determine",  0.90),
    ])

    nyra raison "On peut peut-être éviter ça autrement."

    ryn colere "Parle."

    nyra "Modifier l'amendement."
    nyra "Ajouter une autorisation exceptionnelle."
    nyra "Tous les campements déjà formés seraient reconnus comme déclarés."

    pause 0.2

    tomas raison "Ce serait bien."
    tomas "Juridiquement, je veux dire si c'était possible."

    pause 0.2

    sael determine "On ne peut pas."

    nyra raison "Pourquoi ?"

    sael "L'amendement est déjà posé."
    sael "On débat du texte qui est censé avoir été déposé lors du premier jour."
    sael "On ne peut pas le réécrire."

    tomas culpabilite "Elle a raison."
    tomas "Kami a toujours verrouillé le libellé après annonce."
    tomas "Le vote porte sur la phrase exacte."

    ryn colere2 "Mais bordel, c'est complètement con !"

    sael determine "Oui."
    sael "Mais c'est la règle."

    ryn "Vos règles vont les tuer !"

    pause 0.2

    noam determine "Alors il faut gagner du temps."

    ryn colere "Quoi ?"

    noam "Pas changer le texte."
    noam "Changer la situation avant qu'il s'applique."

    lysa triste "Noam."

    noam "Les campements sont illégaux parce qu'ils sont massifs."
    noam "Parce qu'ils dépassent vingt personnes."
    noam "Parce qu'ils sont aux frontières."
    noam "Parce qu'ils essaient de passer."

    pause 0.2

    tomas raison "Tu veux les faire disperser ?"

    noam determine "Oui."

    ryn colere "Ils sont dehors !"
    ryn "Ils fuient !"
    ryn "Tu crois qu'ils vont juste se ranger en petits paquets parce qu'on leur demande gentiment ?"

    noam "Non."
    noam "Mais s'ils suivent les débats en temps réel, ils entendront le risque."

    sael inquiet "Ils sauront."

    noam "Ils sauront que traverser maintenant est impossible."
    noam "Ils sauront que rester groupés les condamne."
    noam "Et ils auront une chance de se disperser avant l'application du Commandement."

    pause 0.2

    nyra raison "Ce n'est pas une solution parfaite."

    lysa blase "Quelle surprise."
    lysa "Dans cette situation, on n'a que des choix merdiques. C'est presque grec."

    noam "Je ne dis pas que c'est parfait."
    noam determine "Je dis qu'on peut peut-être éviter le pire."

    pause 0.2

    tomas raison "Il faut formuler ça clairement pendant le débat."
    tomas "Pas de sous-entendu."
    tomas "Pas de demi-mot."

    elias fatigue "Faut leur dire de dégager de là."
    elias "Vite."
    elias inquiet "Avant que le canon fasse son boulot."

    iris inquiet "C'est horrible à dire."

    elias "Ouais."
    elias "Mais c'est moins horrible que de ne rien dire et regarder faire."

    pause 0.2

    elen peur "Et s'ils n'écoutent pas ?"
    elen "Et s'ils ne peuvent pas partir ?"
    elen "Et s'il y a des enfants, des blessés, des gens trop fatigués..."

    pause 0.2

    "Personne ne répond."

    pause 0.2

    noam triste "Alors certains resteront en danger."

    ryn colere "Non."

    noam "Ryn."

    ryn colere2 "Non !"
    ryn "Je veux pas d'un plan qui commence déjà par abandonner des gens !"

    noam determine "Moi non plus."
    noam "Mais on ne peut pas les porter nous-mêmes."
    noam "On peut les prévenir."
    noam "Assez fort pour qu'ils bougent avant le tir."

    pause 0.2

    sael determine "Ils sont de Limen."
    sael "Ils pourront survivre."
    sael "S'ils entendent le risque, ils bougeront."

    ryn fatigue "Et s'ils n'entendent pas ?"

    sael triste "Alors on priera pour qu'un autre leur répète."

    lysa blase "Super."
    lysa "Notre stratégie repose sur la panique collective et le bouche-à-oreille. Très troisième siècle."

    nyra raison "Non."
    nyra "Elle repose sur la diffusion publique du débat."
    nyra "Kami veut que le monde entier regarde."
    nyra "Utilisons ça contre elle."

    pause 0.2

    julian determine "Alors il faut parler pour eux."
    julian "Pas pour Kami."
    julian "Pas pour nous."
    julian "Pour ceux qui regardent. Julian peut faire ça."

    iris fatigue "Et pour une fois, évite les effets de scène."

    julian inquiet "Oui."
    julian "Je sais."

    pause 0.2

    mara stress "Donc pendant le débat, on dit clairement : dispersez-vous."
    mara "Ne traversez pas."
    mara "Ne restez pas en gros tas bien pratique pour le canon."

    tomas raison "Pas comme ça."

    mara "Je résume."

    tomas "Il faut être précis."
    tomas "Se séparer en groupes de moins de vingt."
    tomas "S'éloigner des points de passage."
    tomas "Ne pas franchir la frontière sans autorisation."

    noam triste "Oui."

    ryn "On leur demande de retourner crever lentement à Limen."

    noam "Non."
    noam determine "On leur demande de rester vivants jusqu'à ce qu'on puisse obtenir mieux."
    noam "Et de toute façon, ils ne peuvent déjà plus traverser la frontière."

    pause 0.3

    ryn "..."

    pause 0.2

    ryn fatigue "Putain."

    pause 0.2

    sael determine "Le vote pour."
    sael "L'avertissement public."
    sael "Et aucun silence."

    noam determine "Oui."

    tomas raison "Je peux ouvrir le débat sur la définition juridique."
    tomas "Puis Noam enchaîne sur le risque concret."

    lysa blase "Et Ryn évite de menacer tout le monde pendant trente secondes."

    ryn colere "Je vais essayer."

    iris fatigue "Quelle ambition."

    pause 0.2

    nyra raison "Il faudra aussi forcer Kami à confirmer publiquement."
    nyra "Si elle confirme devant les campements, ils comprendront."

    noam "Alors on lui pose la question en direct."

    elen peur "Et si elle refuse ?"

    noam determine "Alors on la repose."
    noam "Encore."
    noam "Jusqu'à ce que tout le monde comprenne ce qu'elle essaie de faire."

    pause 0.3

    lysa triste "Donc notre plan, c'est de transformer le débat en alerte d'évacuation."

    tomas "Oui."

    mara stress "C'est un plan de merde."

    elias fatigue "Ouais."

    mara "Mais c'est le seul qu'on a."

    pause 0.2

    ryn determine "Alors on y va."

    noam determine "On y va."

    pause 0.3

    think "Voter pour ne suffit pas."
    think "Il faut parler assez fort pour que ceux qui sont dehors entendent."
    think "Et assez vite pour qu'ils aient le temps de bouger."
    think "Et on doit gagner du temps !"

    $ hideGroup()

    stop music fadeout 1.5

    scene black with fade

    jump _9_0_1_CONCLAVE_DEBAT

label _9_0_1_CONCLAVE_DEBAT:
    call j901_play_signal_vivant from _call_j901_play_signal_vivant
    $ j901_signal_result_tier = _return

    jump _9_0_1_CONCLAVE_DEBAT_PARTIE_2

label _9_0_1_CONCLAVE_DEBAT_PARTIE_2:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.0

    "Le signal disparaît par morceaux."
    "Comme si quelqu'un écrasait une voix sous une paume trop grande."

    pause 0.4

    "Les écrans clignotent encore."
    "Quelques fragments de campements restent imprimés dans la lumière."
    "Des silhouettes. Des bâches arrachées. Des points minuscules qui comprennent trop tard."

    pause 0.5

    play sound sfx_gresillement
    stop music fadeout 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Voilà."
    kami "C'était donc ça, votre grande tentative."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Un petit détournement de signal."
    kami "Un message paniqué."
    kami "Quelques humains qui crient très fort parce qu'ils ont enfin compris qu'ils étaient en retard."

    pause 0.3

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    if j901_signal_result_tier == "excellent":
        kami "Je reconnais une certaine efficacité technique."
        kami "C'est adorable."
        kami "Presque respectable, si l'impertinence ne gâchait pas tout."
    elif j901_signal_result_tier == "bon":
        kami "Vous avez touché une partie des campements."
        kami "Pas tous."
        kami "Mais assez pour vous donner l'illusion d'avoir repris la main."
    elif j901_signal_result_tier == "moyen":
        kami "Vous avez réussi à faire du bruit."
        kami "Pas beaucoup plus."
        kami "Le bruit donne parfois l'impression d'agir. C'est un piège fréquent."
    else:
        kami "Et même cela, vous l'avez raté."
        kami "Je suis presque déçue."
        kami "Presque."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Dans tous les cas, votre intrusion est enregistrée."
    kami "Votre intention est notée."
    kami "Votre insolence aussi."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Mais je vais être généreuse."
    kami "Je ne vais pas laisser votre petit théâtre interrompre une procédure officielle."

    pause 0.3

    scene bg_diffusion_colere at adaptive_fullscreen with vpunch

    kami "Le Conclave n'est pas une antenne de secours."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le Conclave est un lieu de décision."

    pause 0.5

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2

    $ showGroup([
        ("ryn",   "colere",      0.10),
        ("sael",  "determine",   0.27),
        ("tomas", "culpabilite", 0.43),
        ("lysa",  "blase",       0.57),
        ("nyra",  "stress",      0.73),
        ("kael",  "inquiet",     0.90),
    ])

    "Personne ne bouge."
    "Même respirer paraît risqué."

    ryn colere "Tu savais qu'ils entendaient."
    ryn "Tu les as laissés entendre juste assez pour nous regarder nous débattre."
    ryn "T'as mis des vies sur la table et t'as appelé ça une procédure."

    play sound sfx_gresillement
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ryn."
    kami "Je t'assure que te voir comprendre les choses avec trois minutes de retard reste un plaisir très simple."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("ryn",   "colere2",     0.10),
        ("sael",  "determine",   0.27),
        ("tomas", "culpabilite", 0.43),
        ("lysa",  "blase",       0.57),
        ("nyra",  "stress",      0.73),
        ("kael",  "inquiet",     0.90),
    ])

    sael determine "Alors laisse-nous terminer."
    sael "Quelques minutes."
    sael "Même les condamnés ont droit à une dernière parole."

    play sound sfx_gresillement
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Non."

    pause 0.2

    jump _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS

label _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS:

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([
        ("tomas", "raison",      0.12),
        ("nyra",  "stress",      0.28),
        ("kael",  "inquiet",     0.44),
        ("noam",  "inquiet",     0.60),
        ("lysa",  "blase",       0.76),
        ("sael",  "determine",   0.92),
    ])

    tomas raison "Il faut clarifier le statut des campements déjà en dispersion."
    tomas "Si le signal a été reçu, leur situation juridique a changé pendant la procédure."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Non."
    kami "Leur statut change au moment où j'enregistre la décision."
    kami "Pas au moment où vous espérez très fort."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([("nyra", "raison", 0.28)])

    nyra raison "Alors vérifions les campements."
    nyra "Un relevé en direct. Rien de plus."
    nyra "Tu veux une décision propre ? Donne-nous l'état du terrain."

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Tu veux savoir combien de personnes sont encore en danger avant de lever la main ?"
    kami "C'est touchant."
    kami "Inutile, mais touchant."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le vote ne porte pas sur un inventaire."
    kami "Il porte sur une règle."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([("kael", "raison", 0.44)])

    kael raison "Dans ce cas, délai procédural."
    kael "Pas une négociation."
    kael "Une prévention d'exécution massive."

    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Demande refusée."
    kami "Le règlement ne prévoit pas de délai de confort moral."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([("lysa", "colere", 0.76)])

    lysa colere "Kami."
    lysa "Même pour toi, il doit bien rester une seconde de décence dans un tiroir."

    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Oh, Lysa."
    kami "La décence est justement ce qui vous oblige à voter vite."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Plus vous parlez, plus les campements restent exposés."
    kami "C'est presque comme si votre compassion avait une portée balistique."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showGroup([("noam", "determine", 0.60)])

    noam determine "Tu veux dire que... non."
    noam "Tu cherches à nous faire porter le tir."

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Je vous fais porter votre fonction."
    kami "Il y a une nuance."
    kami "Elle vous échappe parce qu'elle est désagréable."

    pause 0.4

    scene bg_diffusion_colere at adaptive_fullscreen with vpunch

    kami "Assez."

    pause 0.2

    jump _9_0_1_KAMI_EXIGE_LE_VOTE

label _9_0_1_KAMI_EXIGE_LE_VOTE:

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le débat est terminé."
    kami "Les demandes de délai sont rejetées."
    kami "Les demandes de clarification sont rejetées."
    kami "Les appels à la décence sont classés comme manifestations émotionnelles non pertinentes."

    pause 0.3

    scene bg_diffusion_einstein at adaptive_fullscreen with hpunch

    kami "Vote immédiat."

    pause 0.3

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Les pupitres s'allument."
    "Douze halos blancs. Douze petites surfaces propres, absurdes."

    play sound sfx_beep

    "Sur chaque écran, le même choix attend."
    "POUR."
    "CONTRE."

    pause 0.4

    $ showGroup([
        ("ryn",   "colere",      0.10),
        ("sael",  "determine",   0.27),
        ("tomas", "culpabilite", 0.43),
        ("lysa",  "blase",       0.57),
        ("nyra",  "stress",      0.73),
        ("kael",  "inquiet",     0.90),
    ])

    "Personne ne regarde vraiment son pupitre."
    "Tout le monde regarde les autres."
    "Comme si une hésitation pouvait contaminer la salle."

    think "Si quelqu'un refuse..."
    think "Si quelqu'un tremble trop longtemps..."
    think "Si quelqu'un veut encore sauver un principe au lieu de sauver des vies..."

    pause 0.3

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je vous rappelle que ne pas voter n'est pas une échappatoire."
    kami "Dans le contexte actuel, le silence aura une valeur morale très intéressante."

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Je suis certaine que les Limenois apprécieront vos nuances."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Un silence compact tombe sur la salle."
    "Pas un silence de réflexion."
    "Un silence de gorge serrée."

    jump _9_0_1_VOTE

label _9_0_1_VOTE:

    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    scene black with dissolve

    $ _vote_result = renpy.call_screen("vote_screen")
    $ j901_player_vote = _vote_result if _vote_result in ("pour", "contre") else "contre"
    $ j901_vote_adopte = (j901_player_vote == "pour")

    if j901_player_vote == "pour":
        scene Solid("#0AFF8844")
        with Dissolve(0.12)
    elif j901_player_vote == "contre":
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene Solid("#FF2A2A44")
        with Dissolve(0.12)

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0

    "Les pupitres enregistrent les choix."
    "Pas de voix. Pas de main levée."
    "Pas de confession courageuse ou lâche."

    pause 0.3

    "Seulement des écrans qui s'éteignent les uns après les autres."
    "Et personne ne sait vraiment ce que les autres viennent de faire."

    pause 0.5

    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    if j901_vote_adopte:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "pour"),
        ]
    else:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "contre"),
        ]

    $ renpy.random.shuffle(vote_phase3_results)
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    pause 0.8

    $ j901_vote_adopte = (vote_phase3_counts["contre"] == 0)

    if j901_vote_adopte:
        jump _9_0_1_FIN_JOURNEE_VOTE_ADOPTE
    else:
        jump _9_0_1_FIN_JOURNEE_VOTE_REFUSE

label _9_0_1_FIN_JOURNEE_VOTE_ADOPTE:

    $ hideGroup()
    stop music fadeout 0.8
    play sound sfx_announce

    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.2

    kami "Résultat du vote."
    kami "Unanimité des suffrages exprimés."
    kami "Aucun vote défavorable enregistré."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Unanimité atteinte."
    $ interject("ADOPTÉ", color="#5DFF9A")
    kami "Amendement adopté."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Les regroupements de plus de vingt personnes sont désormais autorisés sous déclaration préalable."
    kami "Application immédiate."

    pause 0.3

    if j901_signal_result_tier == "excellent":
        kami "Bilan provisoire : la majorité des campements a eu le temps de se disperser ou de transmettre une déclaration d'urgence."
        kami "Pertes anticipées : réduites."
    elif j901_signal_result_tier == "bon":
        kami "Bilan provisoire : plusieurs campements ont reçu votre avertissement."
        kami "Une partie reste exposée."
    elif j901_signal_result_tier == "moyen":
        kami "Bilan provisoire : signal incomplet."
        kami "Une fraction significative des campements reste menacée malgré votre vote."
    else:
        kami "Bilan provisoire : signal inefficace."
        kami "Le vote sauve les structures encore identifiables comme campements, mais arrive après plusieurs applications du Commandement."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous voyez ?"
    kami "Quand vous obéissez à la procédure, des vies peuvent être sauvées."

    pause 0.3

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve

    kami "Quelle belle leçon collective."

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Personne ne répond."
    "Personne n'a la force."

    pause 0.5

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0

    "Le retour jusqu'aux chambres se fait sans discussion."
    "Les portes s'ouvrent."
    "Les portes se ferment."
    "Les pas résonnent dans le couloir comme des fautes qu'on compte une par une."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je rentre dans ma chambre."
    "Je ne me souviens pas d'avoir marché jusque-là."

    "Je reste debout devant le lit."
    "Les mains vides."
    "La gorge sèche."

    think "On a gagné."

    pause 0.3

    think "Non."
    think "On a voté assez vite pour que Kami puisse appeler ça une victoire."

    "Je m'assois."
    "Le matelas plie sous moi."
    "Tout le reste reste droit."
    "Trop droit."

    think "Des gens sont peut-être vivants parce qu'on a levé la main."
    think "Des gens sont peut-être morts parce qu'on a dû lui demander la permission."

    pause 0.5

    "Je regarde l'écran mural."
    "Il est noir."
    "Pour une fois, j'aurais presque préféré qu'il montre quelque chose."

    think "Juste un chiffre."
    think "Même froid."
    think "Même cruel."
    think "Quelque chose à détester précisément."

    pause 0.5

    "Mais il n'y a rien."
    "Seulement ma chambre."
    "Et cette victoire sale."

    $ journal_entries.append(("Jour 9 — conclusion", "Le vote est passé. Les campements limenois ne sont plus illégaux, mais Kami nous a forcés à sauver des vies selon ses règles. Ce soir, je ne sais pas combien de personnes sont vivantes grâce à nous. Je sais seulement qu'elle nous a humiliés en public."))

    call end_day("10") from _call_end_day_13
    jump _10_0_1_1_REVEIL_CHAMBRE

label _9_0_1_FIN_JOURNEE_VOTE_REFUSE:

    $ hideGroup()
    stop music fadeout 0.6
    play sound sfx_announce

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Résultat du vote."
    kami "Absence d'unanimité."
    $ interject("REJETÉ", color="#FF4D6D")
    kami "Amendement rejeté."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "L'interdiction des regroupements de plus de vingt personnes demeure en vigueur."
    kami "Les campements limenois aux frontières sont donc des rassemblements illégaux."

    pause 0.3

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Application du Commandement IV."

    pause 0.4

    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve

    "Pendant une seconde, personne ne comprend."
    "Ou plutôt, tout le monde comprend en même temps."

    play sound sfx_gresillement
    scene bg_conclave at adaptive_fullscreen, heavy_shake

    "Le Conclave tremble."
    "Très loin sous nos pieds, quelque chose s'aligne."

    ryn colere2 "Non."

    play sound sfx_laser_canon volume 8.0
    scene bg_conclave at adaptive_fullscreen, heavy_shake

    "Le premier tir part."
    "Même à travers les murs, la lumière trouve une manière d'exister."

    "Un flash blanc avale la salle."

    scene black with Fade(0.1, 0.2, 0.8)

    think "Jour 10 commence avant la nuit."
    think "Et cette fois, il commence par un tir."

    call end_day("10") from _call_end_day_14
    jump _10_0_1_1_REVEIL_CHAMBRE
