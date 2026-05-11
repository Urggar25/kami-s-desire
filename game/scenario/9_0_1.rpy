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
    play music "music/bgm_low_tension.mp3" fadein 1.5

    pause 0.5

    "Le couloir est ouvert."
    "Les portes s'ouvrent une à une."

    think "Kami est revenue."

    lysa blase "Bon."
    lysa "La pause du cauchemar est terminée."

    ryn fatigue "Avance."

    iris fatigue "Toujours aussi charmant."

    ryn "Pas aujourd'hui."

    mara stress "Aujourd'hui, personne n'est charmant."
    mara "Même moi, j'ai pas la force de faire semblant."

    elen peur "Ça va aller."

    lysa blase "Elen."

    elen "Quoi ?"

    lysa triste "Pas maintenant."

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

    kael fatigue "Elle est vraiment revenue."

    iris fatigue "Oui."
    iris "Merci, Kael."
    iris "On adore tous commencer la journée par l'évidence la plus déprimante possible."

    kael "Je sais."

    pause 0.2

    kael triste "Ouais... On le pensait peut-être tous... Mais le dire, c'est autre chose..."

    sael inquiet "Deux jours sans entendre sa voix."
    sael "Puis elle revient."

    ryn fatigue "Elle revient toujours."

    lysa blase "Formidable."
    lysa "Si seulement on n'était pas contre l'entité la plus puissante du monde..."

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

    kami "Le vote aura lieu aujourd'hui... Enfin... Dans quelques minutes !"

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
    tomas "Je voulais vérifier le nombre d'exécutions et j'avais déjà vu un truc bizarre hier..."

    ryn colere "Oui et ?!"

    tomas "Des gens quittent massivement les profondeurs de Limen."
    tomas "Beaucoup de gens."

    pause 0.2

    ryn colere "Hein ?! Combien ?"

    tomas culpabilite "Je n'ai pas le chiffre exact."

    ryn colere2 "Combien ?"

    tomas "Des milliers."
    tomas "Peut-être même plusieurs dizaines de milliers..."

    pause 0.3

    sael peur "Laisse moi deviner... Ils remontent vers les frontières ?!"

    tomas "Oui."
    tomas "Je pense qu'ils ont profité de l'absence de Kami."
    tomas "Ou de sa maintenance."
    tomas "Ils ont cru que c'était une ouverture pour passer les frontières malgré l'interdiction..."

    lysa triste "Évidemment."

    tomas raison "Ils ont installé des campements."
    tomas "À plusieurs points de passage."
    tomas "Vers d'autres districts."

    pause 0.2

    kael inquiet "Des campements..."

    tomas culpabilite "Migratoires."
    tomas "Improvisés."
    tomas "Et surtout non déclarés."

    pause 0.3

    noam inquiet "Et donc..."

    tomas "Donc ce sont des regroupements de plus de vingt personnes."

    pause 0.2

    ryn colere "Non. T'es pas sérieux..."

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
    lysa "C'est impossible que ce soit une coïncidence..."

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
    kami "Oh... Comme je suis adorable."
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
    tomas "C'est possible..."

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

    noam "Alors on les sauvera."
    noam "Mais on ne commencera pas par se menacer entre nous."

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
    elen "Il le faut."

    iris inquiet "Elen..."

    elen "Non."
    elen peur "Ne me dis pas qu'il faut rester prudents."
    elen "Pas là."

    iris fatigue "Je voulais juste dire que oui."
    iris "Il le faut."

    pause 0.3

    elias fatigue "Moi aussi je voterai pour."
    elias "Je sais pas faire de beau discours."
    elias "Mais je vote pour."

    mara stress "Pareil."
    mara "Personne ne peut hésiter en sachant ça ? Si ?!"

    julian inquietude "Pour aussi."
    julian "Évidemment."
    julian "Il faut qu'on sauve ces gens !"

    pause 0.2

    kael fatigue "Pour."

    iris surpris "Kael ?"

    kael "Je parle peu."
    kael triste "Ça ne veut pas dire que je ne vois rien."
    kael "Ou que je suis inhumain !"

    pause 0.4

    $ showGroup([
        ("tomas", "raison",     0.10),
        ("lysa",  "blase",      0.27),
        ("ryn",   "colere",     0.43),
        ("sael",  "determine",  0.57),
        ("nyra",  "raison",     0.73),
        ("noam",  "determine",  0.90),
    ])

    tomas raison "Il faudra parler aux abstentionnistes probables, c'est pas possible de s'abstenir sur ce vote."

    ryn colere "J'espère bien oui."

    noam determine "C'est pas notre seul problème."

    ryn "Putain... Quoi encore ?!"

    sael determine "Parle Noam."

    pause 0.2

    noam triste "Kami a été claire. Le commandement s'appliquera, avec ou sans modification."
    noam "Pour faire des regroupements massifs de personnes..."
    noam determine "Il faut avoir une autorisation préalable !"

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

    tomas culpabilite "Lysa. C'est pas le moment. Tais toi et écoute."

    lysa triste "...?"

    pause 0.3

    nyra raison "Si Kami applique la règle strictement..."
    nyra "Même un vote pour ne régularisera pas automatiquement les campements actuels."

    ryn colere2 "Non ?!"
    ryn "Putain, t'es sûr ?!"

    noam triste "Non... Le vote autorise les regroupements."
    noam "Mais seulement quand ils sont déclarés."

    ryn colere "Ils pouvaient pas déclarer !"
    ryn "Elle était absente !"

    lysa blase "Et tu crois que ça va l'émouvoir ?"
    lysa "Elle s'en fout qu'on vive ou qu'on crève !"

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
    elias inquiet "Et ils peuvent crever quand même ?!"

    iris inquiet "C'est une blague ?"
    iris "Dites-moi que c'est une blague nulle."
    iris fatigue "Même une blague de Mara, je prends."

    mara stress "Même moi, je suis pas assez tordue pour pondre ça."

    elen peur "Mais... non."
    elen "Non, ça n'a aucun sens."
    elen "Si on vote pour les sauver, ça doit les sauver."

    kael fatigue "Pas forcément."

    elen "Kael..."

    kael triste "Je suis désolé."
    kael "Mais Kami n'a pas dit qu'elle les sauverait."
    kael "Elle a dit que le Commandement s'appliquerait après le vote."

    julian inquietude "C'est un piège."
    julian "Une astuce pour se foutre de nous mais ça n'a pas marché !"

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
    sael "On ne peut pas le réécrire..."

    tomas culpabilite "Elle a raison."
    tomas "Kami a toujours verrouillé le libellé après annonce."
    tomas "Le vote porte sur la phrase exacte."

    ryn colere2 "Mais bordel, c'est complètement con !"

    sael determine "Oui..."
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
    lysa "Façon dans cette situation on a que des choix merdiques."

    noam "Je ne dis pas que c'est parfait."
    noam determine "Je dis qu'on peut peut-être éviter le pire."

    pause 0.2

    tomas raison "Il faut formuler ça clairement pendant le débat."
    tomas "Pas parler en sous-entendu."
    tomas "Pas en demi-mot."

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
    noam "Mais on ne peut pas sauver tout le monde nous-mêmes."
    noam "On peut seulement les prévenir."
    noam "Le plus fort possible pour qu'ils bougent le plus vite possible !"

    pause 0.2

    sael determine "Ils sont de Limen."
    sael "Ils pourront survivre."
    sael "S'ils entendent le risque, ils bougeront."

    ryn fatigue "Et s'ils n'entendent pas ?"

    sael triste "Alors on priera pour qu'un autre leur répète."

    lysa blase "Super."
    lysa "Notre stratégie repose sur la panique collective et le bouche-à-oreille."

    nyra raison "Non."
    nyra "Elle repose sur la diffusion publique du débat."
    nyra "Kami veut que le monde entier regarde."
    nyra "Utilisons ça contre elle."

    pause 0.2

    julian determine "Alors il faut parler pour eux."
    julian "Pas pour Kami."
    julian "Pas pour nous."
    julian "Pour ceux qui regardent."

    iris fatigue "Et pour une fois, évite les effets de scène."

    julian inquietude "Oui."
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
    noam "Et de toutes façons ils ne peuvent déjà plus traverser la frontière..."

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

    mara "Mais c'est le seul qu'on a..."

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