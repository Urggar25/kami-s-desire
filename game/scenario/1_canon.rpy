# --------------------------------------------------------------------------------------------
# JOUR 1 — Canon
# Scène 1 : Réveil sur les sièges du Conclave (sans trace de Kami)
# Noam = narrateur principal (pas obligé d'être affiché en permanence)
#
# Mise en scène : TRIO DYNAMIQUE
# - Toujours 3 persos affichés (dès qu'on entre en dialogue)
# - Afficher les 3 derniers persos qui ont parlé
# - Quand un 4e parle : on retire celui qui n'a pas parlé depuis le plus longtemps
# - Les slots (xpos) sont fixes : gauche / centre / droite
# - Les persos restants ne bougent pas quand un nouveau parle
# --------------------------------------------------------------------------------------------

label _1_CANON:

    $ day_id = 1

    scene black
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Jour un."
    think "Enfin, je crois."
    think "Je n'ai pas vu le temps passé."
    think "Je me suis endormi dans un caisson."
    think "Et là… je me réveille sur un siège."

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with fade

    "Un dossier rigide sous mon dos."
    "Un siège froid et métallique."
    "L’air est sec, presque comme s'il était recyclé."
    "Ça sent le plastique neuf et le produit de nettoyage."

    $ blink()

    "Je cligne des yeux."
    "Ma bouche est sèche."
    "Ma nuque me fait mal."

    "Je me redresse."
    "Autour de moi, d’autres sièges."
    "Beaucoup."
    "En cercle."
    "Et sur chaque siège… quelqu’un."

    "Certains bougent légèrement."
    "D’autres restent figés. Ils dorment encore."

    "Personne ne parle fort."
    "Juste des respirations régulières."
    "Des froissements de vêtements."
    "Un raclement de gorge quelque part."

    play sound sfx_beep
    "-Bip-"

    "Un son bref."
    "Pas une alarme."
    "Un bip de système."
    "Ça vient d’en bas, il semble y avoir plusieurs étages ici."

    "Je baisse les yeux."
    "Sur mon pupitre, une tablette est encastrée."
    "Éteinte."
    "Noire."

    "Je tourne la tête."
    "Je cherche Lysa du regard."
    "Parce que c’est la seule personne que je connais un minimum."
    "Au moins de nom."

    $ showP("lysa", "neutre", 0.78)      # droite
    $ showP("noam", "inquiet", 0.50)    # centre

    noam "Lysa… ?"

    $ showP("lysa", "blase", 0.78)

    lysa "Ouais..."
    lysa "T’es enfin réveillé."

    noam "On est où… ?"

    $ showP("lysa", "reflexion", 0.78)

    lysa "Si je devais deviner…"
    lysa "Je dirais le Conclave."

    "Je regarde autour."
    "Je ne connais aucun des autres visages."

    think "Donc c’est vrai."
    think "Ils nous ont tous mis au même endroit."
    think "En même temps pour participer à ce truc étrange."

    "Quelqu’un se lève brusquement."
    "Un siège grince."
    "Ça claque dans le silence."

    $ showP("ryn", "colere", 0.22)
    $ showP("lysa", "surpris", 0.78)      # elle réagit, sans parler

    ryn "Putain mais on est où là ?!"
    ryn "Qui a fait ça ?!"

    "Personne ne répond."
    "Pas un seul mot."

    hide noam
    $ showP("mara", "rire", 0.50)       # centre

    $ showP("ryn", "colere2", 0.22)        # réaction
    $ showP("lysa", "blase", 0.78)      # réaction

    mara "Tu veux dire… à part l’IA qui tient le monde en laisse ?"

    ryn "Je parle de ce qui nous arrive, là, maintenant."
    ryn "Qui nous a endormis."
    ryn "Qui nous a trimballés ici."

    hide lysa
    $ showP("tomas", "reflechit", 0.78)  # droite

    $ showP("ryn", "reflechit", 0.22)    # il écoute
    $ showP("mara", "neutre", 0.50)      # elle se calme

    tomas "Probablement personne de “présent”… enfin, pas ici."
    tomas "Ça ressemble à une procédure."
    tomas "Automatique."

    hide ryn
    $ showP("elen", "surpris", 0.22)     # gauche

    $ showP("mara", "stress", 0.50)  # réaction
    $ showP("tomas", "neutre", 0.78)     # réaction

    elen "Automatique ou pas, ça reste un enlèvement."
    elen "Mais bon, plus rien n'est choquant dans ce monde ..."

    "Je lève les yeux."
    "Je cherche les caméras."
    "Il y en a."
    "Évidemment."
    "Propres."
    "Discrètes."

    think "Ça, c’est la partie la plus habituelle de tout ça."
    think "C’est triste mais on y est habitué."

    hide mara
    $ showP("julian", "peur", 0.50)      # centre

    $ showP("elen", "inquiet", 0.22)     # réaction
    $ showP("tomas", "reflechit", 0.78)  # réaction

    julian "Vous… vous entendez ça ?"
    julian "Rien. Absolument rien. On dirait qu’on est les derniers humains sur Terre."

    hide tomas
    $ showP("iris", "inquiet", 0.78)     # droite

    $ showP("elen", "desaccord", 0.22)
    $ showP("julian", "peur", 0.50)

    iris "Mais… y a même pas un murmure ! Rien ! C’est flippant à quel point c’est silencieux ici !"
    iris "Et en plus on sait même pas ce qu’on est censés faire, hein ! On attend quoi, un miracle ?"

    hide elen
    $ showP("nyra", "triste", 0.22)      # gauche

    $ showP("julian", "surpris", 0.50)   # réaction
    $ showP("iris", "hesitation", 0.78)     # réaction

    nyra "Ce silence est voulu."
    nyra "C’est un test. Kami veut voir comment on réagit."

    hide julian
    $ showP("kael", "calme", 0.50)       # centre

    $ showP("iris", "fatigue", 0.78)     # réaction
    $ showP("nyra", "neutre", 0.22)      # réaction

    kael "Ou une attente."
    kael "Peut-être qu'elle attend juste... quelque chose ?"

    "Un silence encore plus lourd tombe."
    "Personne n’aime l’idée d’attendre."
    "Surtout dans une situation comme celle-là."
    "Parce que ça veut dire qu’on dépend du bouton “play” de quelqu’un d’autre."

    hide iris
    $ showP("noam", "reflexion", 0.78)   # droite

    $ showP("nyra", "panne", 0.22)       # réaction
    $ showP("kael", "neutre", 0.50)      # réaction

    noam "Au fait, vous avez vu Kami ?"

    "Pas un seul regard ne se lève vers l'écran central."
    "Il n'est pas allumé. Tout comme les tablettes disposées à chacune des places."
    "Et parce que personne n’a envie de prononcer son nom trop fort."

    hide nyra
    $ showP("ryn", "reflechit", 0.22)    # gauche

    $ showP("kael", "calme", 0.50)
    $ showP("noam", "inquiet", 0.78)

    ryn "Non."
    ryn "Et ça me fait chier de le dire, mais je préfèrerais avoir des nouvelles."

    hide kael
    $ showP("mara", "rire", 0.50)        # centre

    $ showP("ryn", "colere", 0.22)
    $ showP("noam", "neutre", 0.78)

    mara "J’adore, putain."
    mara "Douze pigeons, zéro animateur."
    mara "Pas de mode d’emploi, pas d’hôte, même pas un petit speech d’accueil."
    mara "Elle nous snobe direct, la garce."

    hide noam
    $ showP("tomas", "reflechit", 0.78)  # droite

    $ showP("ryn", "reflechit", 0.22)
    $ showP("mara", "neutre", 0.50)

    tomas "On parle de Kami, n'oublie pas."
    tomas "Elle est toujours là."
    tomas "Même sans image."

    "Je fixe la tablette noire sur mon pupitre."
    "Je tapote du doigt."
    "Rien."

    think "C’est ça qui me dérange."
    think "D’habitude, Kami aime être… présente."
    think "Là, c’est vide."
    think "Comme une salle de classe sans prof."
    think "Sauf qu'ici le prof peut te tuer."

    "Lysa se penche légèrement vers moi."
    "Elle parle bas par réflexe."

    hide ryn
    $ showP("lysa", "reflexion", 0.22)   # gauche

    $ showP("mara", "agace", 0.50)       # réaction
    $ showP("tomas", "neutre", 0.78)     # réaction

    lysa "Tu as remarqué ça ?"

    hide mara
    $ showP("noam", "reflexion", 0.50)   # centre

    $ showP("lysa", "neutre", 0.22)
    $ showP("tomas", "reflechit", 0.78)

    noam "Quoi ?"

    $ showP("lysa", "determine", 0.22)

    lysa neutre "Aucun ordre."
    lysa "Aucun écran."
    lysa "Aucun message."
    lysa fatigue "... Silence radio."

    noam "Ça veut dire quoi pour toi ?"

    $ showP("lysa", "blase", 0.22)

    lysa "Ça veut dire que soit on est censé faire quelque chose, soit que Kami attend un autre momennt."
    lysa "Et ça…"
    lysa "J’aime pas."

    pause 0.4

    "Au centre de la salle, une structure circulaire."
    "Un vaste écran qui fait un tour complet sur lui-même."
    think "C'est comme si on regardait un film mais qu'on attendait l'acteur principal.."

    play sound sfx_beep
    "-Bip-"

    "Un deuxième bip."
    "Puis rien."

    "Quelqu’un se lève."
    "Un pas."
    "Puis s’arrête."

    hide tomas
    $ showP("ryn", "reflechit", 0.78)    # droite

    $ showP("noam", "inquiet", 0.50)
    $ showP("lysa", "culpabilite", 0.22)

    ryn "On reste assis ?"
    ryn "On attend ?"
    ryn "C’est ça le plan ?"
    
    hide noam
    $ showP("elias", "neutre", 0.50)
    elias "… Et après ? Tu comptes faire quoi ?"

    hide elias
    $ showP("sael", "raison", 0.50)      # centre

    $ showP("lysa", "neutre", 0.22)
    $ showP("ryn", "colere", 0.78)

    sael "Le plan, c’est de survivre."
    sael "Et pour l’instant, bouger sans info…"
    sael "c’est un risque. Et tu veux que je te rappelle ce qui arrive à ceux qui prennent des risques ?"
    
    "Derrière, une petite voix se fait entendre."
    elen "Mais attendre, c’est un pari risqué aussi."
    
    hide lysa
    $ showP("tomas", "raison", 0.95)
    
    tomas "Tout ici est un pari."
    tomas "Faut dire qu'on a tous été pris de court."
    tomas "Même les responsables de district semblaient n'être au courant de rien ..."

    "Je sens mon cœur accélérer."
    "Pas de panique."
    "Juste la lucidité qui pique."

    think "Jour un."
    think "Et on est déjà en train d'essayer de deviner les règles."
    think "Super."

    "Je jette un regard à Lysa."
    "Elle ne tremble pas."
    "Mais sa jambe bouge."
    "Un mouvement minuscule."

    hide tomas
    $ showP("noam", "reflexion", 0.22)   # gauche

    $ showP("sael", "neutre", 0.50)
    $ showP("ryn", "reflechit", 0.78)

    noam "On fait quoi, alors ?"

    "Personne ne répond tout de suite."
    "Parce que personne ne veut être le premier à choisir."
    "Parce que choisir, ça peut nous tuer."

    pause 0.6

    "Un souffle de ventilation change."
    "Très léger."
    "Mais tout le monde l’entend."
    "Parce qu’on n’a plus que ça à entendre."

    "Et là, au-dessus du pupitre central…"
    "Une lumière blanche s’allume."
    "Faible."
    "Comme une veilleuse."
    "Au même moment, le bruit d'un mécanisme qui s'active prend de l'ampleur."

    play sound sfx_gresillement
    
    "Puis l'écran central s'allume enfin."
    $ cam_move(0.5, 0.05, 3.00, 1.0)
    
    hide sael
    hide ryn
    hide noam

    pause 0.4

    jump _1_KAMI_APPARITION

# 3m
# Total : 24m30

label _1_KAMI_APPARITION:

    # Écran de diffusion de Kami, constant
    play music "music/bgm_system_override.mp3" fadein 0.4
    scene bg_diffusion_amour at adaptive_fullscreen with fade
    $ bc_off()
    show screen kami_broadcast_ui

    kami "Ah… vous êtes tous réveillés."
    kami "Parfait."
    kami "J’avais peur d’avoir surestimé votre capacité à survivre à une sieste forcée."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Les sièges étaient confortables, j’espère."
    kami "J’ai hésité avec des bancs en métal."
    kami "Et puis je me suis dit que vous préféreriez commencer… doucement."

    pause 0.4

    $ bc_show("noam", "inquiet", px=-80, py=-50, pz=0.8)
    noam "Pourquoi nous ?"

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Oh."
    kami "Excellente question."

    kami "Parce que vous êtes douze."
    kami "Et que douze, c’est un chiffre pratique."
    kami "Assez pour créer des alliances."
    kami "Pas assez pour se cacher dans la foule."

    pause 0.3

    $ bc_show("ryn", "colere", px=-90, py=-40, pz=0.85)
    ryn "Un test de quoi ?"

    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Un test de vous."
    kami "De vos choix."
    kami "De l’humanité en général."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "De votre capacité à obéir…"
    kami "Et à prétendre que vous obéissez “pour le bien commun”."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Croyez-moi."
    kami "Ça ne sera pas si évident."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Bienvenue au Conclave."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Le Conclave durera trente jours."
    kami "Trente jours exactement."
    kami "Pas un de plus."
    kami "Pas un de moins."
    kami "Et pendant ces trente jours, vous ne retournerez pas chez vous."

    scene bg_diffusion_triste at adaptive_fullscreen with dissolve

    kami "Trente jours pendant lesquels vous allez décider."
    kami "Pas pour vous."
    kami "Pour tous les autres…"

    pause 0.4

    $ bc_show("elen", "inquiet", px=-70, py=-50, pz=0.85)
    elen "Décider de quoi… ?"

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Des règles."
    kami "Celles qui encadrent ce monde."
    kami "Celles que vous respectez déjà, chaque jour."
    kami "Le bien et le mal, en somme."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Aujourd’hui, au cours de cette première journée…"
    kami "Chacun de vous proposera une modification."
    kami "Un amendement."
    kami "Un seul."
    kami "Sur le commandement de votre choix."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vous pourrez renforcer une règle."
    kami "L’adoucir."
    kami "La tordre."
    kami "Ou l’habiller d’un joli mot pour faire croire que c’est une avancée."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Vous êtes libres de proposer ce que vous voulez."
    kami "Et personne ne saura jamais qui a proposé quoi."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je vous laisse être créatifs."
    kami "Après tout…"
    kami "C’est ce que vous faites de mieux."

    pause 0.5

    $ bc_show("tomas", "reflechit", px=-80, py=-45, pz=0.85)
    tomas "Et ensuite ?"

    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Ensuite ?"
    kami "Vous votez."

    kami "Tous les trois jours."
    kami "Un vote."
    kami "Simple."
    kami "Clair."
    kami "Binaire."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Pour."
    kami "Ou contre."

    pause 0.3

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais attention."
    kami "Pour qu’un amendement soit adopté…"
    kami "Il faut l’unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Tous."
    kami "Sans exception."
    kami "Sinon, c’est non."

    pause 0.5

    $ bc_show("nyra", "triste", px=-70, py=-55, pz=0.85)
    nyra "Et si quelqu’un vote contre… ?"

    $ bc_hide()

    scene bg_diffusion_desespoir at adaptive_fullscreen with dissolve

    kami "Alors l’amendement est rejeté."
    kami "Il disparaît."
    kami "Comme s’il n’avait jamais existé."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Un peu comme certaines personnes."
    kami "Dans d’autres circonstances."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous allez apprendre quelque chose d’important."
    kami "Très vite."

    kami "Convaincre est plus difficile que contraindre."
    kami "Et le consensus…"
    kami "Est un luxe que peu de sociétés peuvent se permettre."

    pause 0.6

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Oh."
    kami "Dernière précision."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Je ne participerai pas aux votes."
    kami "Je ne donnerai pas mon avis."
    kami "Je ne prendrai part à aucune de vos manigances."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Je regarderai."
    kami "Et j’apprendrai encore de vous."

    pause 0.4

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Et maintenant, la précision de taille."
    kami "Ici… les Commandements n’ont pas lieu d’être."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve

    kami "Vous pouvez vous battre."
    kami "Vous pouvez mentir."
    kami "Vous pouvez voler."
    kami "Vous pouvez vous entretuer."
    kami "Je ne m’en mêlerai pas."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Mais n’oubliez pas."
    kami "Tout ce que vous faites est filmé."
    kami "Et diffusé."

    pause 0.4

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "J’ai passé un an à vous observer."
    kami "Vos débats."
    kami "Vos justifications."
    kami "Vos excuses."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ce serait dommage de s’arrêter maintenant."

    pause 0.6

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Le Conclave commence."
    kami "Les portes sont ouvertes."
    kami "Visitez les lieux."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Faites connaissance."
    kami "Ou faites… autrement."

    pause 0.5

    # ------------------------------------------------------------------------------------------
    # 2m10
    # Total : 26m40
    # ------------------------------------------------------------------------------------------
    
    $ bc_off()
    play music "music/bgm_quiet_routine.mp3" fadein 0.4
    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade

    "L’écran s’éteint."
    "Et pendant une seconde, personne ne respire."

    "Puis tout le monde se met à parler en même temps."
    "Des chuchotements qui deviennent vite des phrases entières."
    "Des rires nerveux."
    "Des insultes à demi avalées."

    $ showP("noam", "reflexion", 0.50)
    $ showP("lysa", "blase", 0.78)
    $ showP("tomas", "reflechit", 0.22)

    noam "On va devoir vraiment passer trente jours ici …"

    $ showP("lysa", "reflexion", 0.78)
    lysa blase "L’unanimité ?"
    lysa blase "C’est le piège ultime."
    lysa blase "En vrai, c’est quasi impossible."
    lysa "Soit tu convaincs tout le monde…"
    lysa "soit tu les écrases."
    lysa fatigue "Maintenant je pige pourquoi elle dit que ce sera pas simple."

    $ showP("tomas", "raison", 0.22)
    tomas "Ou à faire des compromis."
    tomas "Pour une fois."

    "Je tourne la tête."
    "Sur les autres sièges, ça débat déjà comme si ça faisait une heure."

    hide tomas
    $ showP("nyra", "triste", 0.22)

    $ showP("noam", "inquiet", 0.50)
    $ showP("lysa", "neutre", 0.78)

    nyra "Moi… je vois quand même un truc positif."
    nyra "Si on peut modifier les règles…"
    nyra "Ça veut dire qu’on peut améliorer les choses."

    $ showP("lysa", "blase", 0.78)
    lysa "Ou les empirer."
    lysa "Les rendre “légales”, surtout."

    hide nyra
    $ showP("elen", "inquiet", 0.22)

    $ showP("noam", "reflexion", 0.50)
    $ showP("lysa", "reflexion", 0.78)

    elen "Le fait qu’on puisse proposer des amendements…"
    elen "C’est pas rien."
    elen "Dans ce monde, c’est presque…"
    elen "Une respiration."

    $ showP("lysa", "blase", 0.78)
    lysa "Une respiration sous l’eau."

    "Un rire s’échappe quelque part."
    "Un rire trop franc, trop sûr de lui."

    hide elen
    $ showP("mara", "rire", 0.22)

    $ showP("noam", "inquiet", 0.50)
    $ showP("lysa", "surpris", 0.78)

    mara "Vous parlez tous comme si on venait de gagner au loto."
    mara "On est dans une putain de cage, les gars."
    mara "Avec un bouton ‘vote’ et un nœud rose dessus pour faire genre que c’est cadeau."

    $ showP("lysa", "colere", 0.78)
    lysa "Merci pour le rappel."

    hide mara
    $ showP("ryn", "colere", 0.22)

    $ showP("noam", "inquiet", 0.50)
    $ showP("lysa", "neutre", 0.78)

    ryn "Non mais attendez."
    ryn "Elle a dit quoi exactement ?"
    ryn "Ici, les commandements s’appliquent pas."

    $ showP("ryn", "colere2", 0.22)
    ryn "Donc si quelqu’un pète un câble…"
    ryn "On fait quoi ?"

    $ showP("lysa", "reflexion", 0.78)
    lysa neutre "On est filmés en permanence."
    lysa "IA qui mate et diffuse tout."
    lysa blase "Son idée du ‘cadre sécurisé’, apparemment."
    lysa "La pression, ça empêche de péter un câble."
    lysa fatigue "... En théorie."

    "À côté, quelqu’un se lève, ajuste sa veste comme s’il montait sur scène."
    "Il cherche du regard une caméra. Il la trouve."
    "Et il lui offre un sourire travaillé."

    hide ryn
    $ showP("julian", "rire", 0.22)

    $ showP("noam", "reflexion", 0.50)
    $ showP("lysa", "blase", 0.78)

    julian "Franchement ?"
    julian "Moi je trouve ça carrément bandant."

    $ showP("julian", "neutre", 0.22)
    julian "Enfin !"
    julian "Un endroit où on peut vraiment parler, peser sur les règles…"
    julian "… et où les gens vont regarder. Pour de vrai."

    "Il se tourne légèrement. Comme pour se mettre de profil face à la caméra."
    "Comme si ça avait de l’importance."

    $ showP("lysa", "colere", 0.78)
    lysa "T’es sérieux ?"

    $ showP("julian", "idee", 0.22)
    julian "Totalement."
    julian "Si je dois être coincé ici trente jours… autant que ce soit légendaire."
    julian "Et autant en profiter pour rendre la vie un peu moins pourrie aux autres, non ?"

    "Il jette un regard rapide vers une caméra."
    "Il lève deux doigts en signe de salut."
    "Comme si quelqu’un l’attendait de l’autre côté."

    $ showP("noam", "inquiet", 0.50)
    noam "…"

    hide julian
    $ showP("tomas", "reflechit", 0.22)

    $ showP("noam", "reflexion", 0.50)
    $ showP("lysa", "reflexion", 0.78)

    tomas "Au moins, ça confirme un truc."
    tomas "Elle veut du spectacle."

    $ showP("tomas", "raison", 0.22)
    tomas "Et si elle veut du spectacle…"
    tomas "C’est qu’elle s’attend à ce qu’on se déchire."

    pause 0.4

    "Un autre détail me revient."
    "Le jour 1, chacun propose un amendement."

    $ showP("noam", "reflexion", 0.50)
    noam "Donc aujourd’hui… on doit tous proposer quelque chose."

    $ showP("lysa", "culpabilite", 0.78)
    lysa "Ouais."
    lysa "Et personne saura qui a proposé quoi."
    
    hide noam
    $ showP("kael", "neutre", 0.50)
    kael "Et si on se disait tous ce qu'on propose comme modifications ?"
    kael "Si on les travaille ensemble, on a plus de choses d'atteindre l'unanimité ?"

    "Un silence retombe, plus sec."
    "Cette fois, c’est pas la peur."
    "C’est le calcul."

    hide tomas
    $ showP("elen", "inquiet", 0.22)

    $ showP("noam", "neutre", 0.50)
    hide kael
    
    $ showP("lysa", "reflexion", 0.78)

    elen "On devrait peut-être…"
    elen "Se mettre d’accord sur une méthode."
    elen "Un truc simple."
    elen "Pour éviter que ça parte en guerre tout de suite."

    $ showP("lysa", "blase", 0.78)
    lysa blase "Tu veux une méthode ?"
    lysa "On est douze, enfermés, filmés."
    lysa "Et ici, tuer quelqu’un… pas de conséquence."
    lysa fatigue "La méthode est déjà écrite."
    lysa "... Et on la connaît tous."
    lysa peur "Evidemment que ça va finir en tuerie de masse."

    pause 0.4

    "Je vois des petits groupes se former."
    "Deux par-ci."
    "Trois par-là."
    "Des regards en biais."
    "Des gens qui s’éloignent déjà, comme s’ils avaient peur d’être associés."

    $ showP("noam", "reflexion", 0.50)
    noam "On fait quoi, nous ?"

    $ showP("lysa", "determine", 0.78)
    lysa neutre "On visite."
    lysa "On repère les lieux."
    lysa "Et on ferme sa gueule devant les caméras."
    lysa fatigue "Surtout au début."

    $ showP("elen", "reflechit", 0.22)
    elen "Je… je vais voir s’il y a une infirmerie."
    elen "Ou au moins du matériel."
    elen "On sait jamais."

    $ showP("noam", "neutre", 0.50)
    noam "Ok."

    pause 0.4

    "Tout le monde quitte peu à peu la pièce."

    "Et moi…"
    "Je devrais aller faire un tour également."

    pause 0.6

    think "Phase exploration."
    think "Ça commence maintenant."
    
    scene bg_map at adaptive_fullscreen with fade
    
    tuto "Prêt pour un nouveau tutoriel ?"
    tuto "J'espère bien !"
    tuto "Cette carte correspond à la carte du Conclave."
    tuto "Toutes les pièces vous sont ouvertes afin que vous puissiez explorer chacune des pièces convenablement."
    tuto "Pour accéder à une salle spécifique, rien de plus simple : il suffit de cliquer dessus."
    tuto "Dans certaines pièces, certaines interactions peuvent être cruciales pour débloquer des fins différentes."
    tuto "Cette mécanique complète la mécanique de choix afin d'ouvrir les possibles."
    tuto "N'hésitez donc pas à explorer et à interagir avec votre environnement."
    tuto "Bonne exploration !"

    # Placeholder : tu brancheras plus tard sur ton hub d'exploration
    jump OPEN_CONCLAVE_MAP

    # ------------------------------------------------------------------------------------------
    # 2m10
    # Total : 28m50
    # ------------------------------------------------------------------------------------------

label CHECK_ALL_SALLES_VISITEES:

    if (
        decouverte_salle_archive
        and decouverte_cafeteria
        and decouverte_salle_canon
        and decouverte_gymnase
        and decouverte_infirmerie
        and decouverte_salle_maintenance
        and decouverte_salle_observation
        and decouverte_salle_repos
        and decouverte_sas
        and decouverte_stockage
    ):
        jump KAMI_MESSAGE_APRES_VISITE

    return

label KAMI_MESSAGE_APRES_VISITE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    think "J’avais fini par oublier l’heure."
    think "Ici, le temps a une façon de te faire croire qu’il s’est arrêté."
    think "Et puis non."
    think "Il avance. Lentement, mais il ne recule jamais."

    "Un écran mural grésille."
    "Un second s’allume plus loin."
    "Puis un troisième."
    "Même signal, partout, identique."

    play sound sfx_beep
    "-Bip-"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il est bientôt dix-huit heures."
    kami "Votre visite libre touche à sa fin."

    kami "J’espère que vous avez trouvé ça…"
    kami "inspirant et complet."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "On a mis du cœur à l’ouvrage."
    kami "Enfin."
    kami "On a surtout mis des ingénieurs passionnés."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Vous êtes tous convoqués."
    kami "Direction la salle du Conclave."
    kami "Tout de suite."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Hop hop."
    kami "Je suis déjà installée."
    kami "Popcorn virtuel en main."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ne me faites pas perdre mon temps."
    kami "C’est le seul truc que je ne vous pardonnerai pas."

    play sound sfx_beep
    "-Bip-"

    scene bg_couloir at adaptive_fullscreen with dissolve

    think "Voilà, on y arrive."
    think "A partir de là, le Conclave débute vraiment."
    think "Ce n'est plus possible de faire marche arrière."
    think "Enfin, ça n'a jamais été possible mais bon ..."

    scene bg_conclave at adaptive_fullscreen with fade

    "Les portes du Conclave s’ouvrent, dedans, il y a déjà plusieurs personnes."
    "On évite tous de se regarder, comme si on était géné de quelques choses."
    "Personne n’a envie d’être le premier à parler."

    "La salle du Conclave n'a pas changé depuis tout à l'heure."
    "Toujours trop propre."
    "Toujours trop grande."
    "Et on est toujours insignifiant dans ce monde gigantesque."

    "Je m’assois et ceux déjà présents m'imitent."
    "Les autres arrivent par grappes."
    "Des fauteuils raclent."
    "Mais personne ne parle. On attends."

    $ showP("ryn", "fatigue", 0.78)

    ryn "On est tous là ?"
    ryn "Me dites pas qu’on va encore attendre pour rien."

    hide noam
    $ showP("mara", "rire", 0.50)

    mara "Chuuut."
    mara "T’as capté ou quoi ?"
    mara "Kami supporte pas qu’on lui fasse perdre son temps, soi-disant."
    mara "Et moi j’ai pas envie d’être sa cible du jour, alors merci mais tais toi."

    hide lysa
    $ showP("iris", "fatigue", 0.22)

    iris "Super. Vraiment super."
    iris "On nous convoque comme des mômes de primaire qui ont sali la classe. Génial, l’ambiance."
    iris "J’ai hâte de voir qui va nous mettre au coin cette fois."

    hide ryn
    $ showP("julian", "sourire", 0.78)

    julian "Perso je trouve ça hyper marrant."
    julian "J’ai trop envie de voir jusqu’où on peut pousser le bordel dans cet endroit…"

    hide mara
    $ showP("elen", "inquiet", 0.50)

    elen "Pas vraiment sûre qu'on puisse changer grand chose…"
    elen "Tu sais très bien que Kami a droit de vie et mort sur tout le monde."

    $ showP("julian", "taquin", 0.78)

    julian "Je sais, je sais..."
    julian "Mais justement, c’est ça qui est excitant."
    julian "Si on peut réécrire les règles, on peut tout changer."
    julian "Et sortir tout le monde de là. On pourrait être les héros de l'humanité !"

    "L’écran central s’allume."
    "Un halo blanc."
    "Et Kami apparaît."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Bonjour. Je vois que vous êtes tous arrivés."
    kami "Mes douze représentants."
    
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    
    kami "Oh que ça faisait longtemps que j'en révais de ce Conclave !"
    kami "C'était un travail monstre de tout organiser !"
    kami "Mais je pense que ça peut valoir le coup !"

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Mais revenons à nos moutons."
    kami "Je vais être claire."
    kami "Ici, dans le Conclave…"
    kami "les Commandements sont suspendus, abolis."
    kami "Toutes les règles que vous connaissiez jusque là n'ont plus lieu d'être."
    
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    
    kami "Vous êtes libre d'avoir la liberté absolue !"
    kami "Pas de commandement, pas de loi, pas de police."
    kami "Juste vous."

    "Un frisson traverse la salle."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui."
    kami "Je vois que certains d'entre vous arborrent déjà des sourires."
    kami "Mais..."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Ne vous enflammez pas."
    kami "Ça ne veut pas dire que vous pouvez tout faire."
    kami "Je me permets juste cet amènagement pour pouvoir vous observer sans bruit de fond."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Donc."
    kami "Il n'y a plus de Commandements ici."
    kami "Mais il reste certaines règles."
    kami "Celles du Conclave."

    kami "Règle une."
    kami "Interdiction de retourner dans votre district."
    kami "Interdiction d’aller dans un autre."
    kami "Jusqu’à la fin du trentième jour."

    pause 0.2

    kami "Vous restez ici."
    
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Pendant trente petit jour, nous allons nous amuser ensemble."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    
    kami "Règle deux."
    kami "Interdiction d’initier un contact vers l’extérieur."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Alors que je ne vous vois pas trifouiller au matériel de communication."
    kami "Si jamais quelqu'un vous appelle, vous pouvez répondre."
    kami "Mais pas l'inverse."
    
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Vous savez combien ça coûte les appels depuis l'espace ?!"
    kami "Non franchement, ne jouez pas aux idiots."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Règle trois."
    kami "Vous êtes constamment filmés."

    "Personne ne commente."
    "On le sait."
    "On le sait trop bien."
    "C'est peut être la seule chose qui ne changera pas dans notre quotidien."

    kami "Mais il y a une exception."
    
    "Tout le monde écoute plus attentivement."
    
    kami "Vos chambres sont équipées d'un brouilleur."
    kami "Il est activé par défaut."
    kami "Caméras, audio, capteurs : tout est coupés."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Mais vous pouvez le désactiver."
    kami "Si vous aimez être vus par exemple."

    pause 0.2

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Maintenant."
    kami "On peut passer au cœur du Conclave."

    kami "Vous allez déposer chacun un amendement."
    kami "Une modification d’un Commandement."
    kami "Dans une urne."

    kami "Vous avez trente-cinq minutes pour chacun en déposer un."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Oui, c'est presque comme un examen surprise."
    kami "J'adore."
    kami "J’espère que vous avez de l'inspiration."
    
    scene bg_diffusion_gene at adaptive_fullscreen with dissolve
    
    kami "Allez, je veux savoir ce que vous voulez changer dans mes règles parfaites !"
    kami "Qu'est ce que j'aurais pu mal faire ?"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Il y aura dix votes."
    kami "Dix amendements tirés au sort."
    kami "Pas un de plus."

    kami "Vous êtes douze."
    kami "Donc deux amendements ne seront pas votés lors de ce Conclave."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Ne le prenez pas mal."
    kami "C’est mathématique."
    kami "Et ce n'est pas plus mal, si jamais je devais reproduire le Conclave l'an prochain."
    kami "Je pourrais peut être ajouter les amendements restants dans la prochaine urne !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "Tous les trois jours."
    kami "Un amendement sera tiré au sort."
    kami "Puis tous les trois jours, vous voterez sur cet amendement. Votre objectif : l’unanimité."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve

    kami "Une seule voix contre."
    kami "Et l'amendement est refusé."
    
    show screen kami_broadcast_ui
    $ bc_show("elias", "reflechit", px=-70, py=-50, pz=0.85)
    
    elias "Donc si une seule personne dit non… c’est mort."
    elias "C’est une sorte de système de blocage."
    
    $ bc_hide()
    hide screen kami_broadcast_ui

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    
    kami "Pour chaque proposition d'amendement adopté, j'initierai immédiatement le changement."
    kami "Pour certains, un refus de l'amendement pourra aussi avoir des conséquences."
    kami "Mais ça ça dépendra de vos douces propositions."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Sur ce."
    kami "Écrivez."
    kami "Réfléchissez."
    
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Faites semblant d’être des adultes responsables."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "L’urne ferme dans trente-et-une minutes."
    kami "Ne déposez pas vos propositions en retard."

    play sound sfx_beep
    "-Bip-"
    jump _1_CONCLAVE_DEBAT_DEPOT

# Durée : 3m30
# Total : 56m15


label _1_CONCLAVE_DEBAT_DEPOT:

    scene bg_conclave at adaptive_fullscreen
    play music "music/bgm_system_override.mp3" fadein 1.0

    think "Trente-et-une minutes seulement."
    think "Pour faire des propositions qui peuvent réduire des villes en cendre."

    "L’urne est là, au centre de la pièce."
    "Bien visible, bien mise en avant."

    $ showP("kael", "calme", 0.50)

    kael "Bon."
    kael "Je vais être direct."

    kael "Si on écrit tous dans notre coin."
    kael "Sans se parler."
    kael "On prend un risque énorme."

    kael "Je propose un truc simple."
    kael "Chacun annonce ce qu’il compte proposer."
    kael "Pas forcément le texte exact."
    kael "Mais au moins l’intention."

    kael "Comme ça."
    kael "On évite les horreurs et les erreurs."

    pause 0.3

    $ showP("iris", "fatigue", 0.22)

    iris "Non mais non !"
    iris "C’est déjà l’horreur ton truc, là, tu te rends compte ou pas ?!"

    hide kael
    $ showP("kael", "neutre", 0.50)

    kael "Pourquoi ça ?"

    hide iris
    $ showP("iris", "desaccord", 0.22)

    iris "Attends, parce que si un amendement a l’air tout gentil, tout raisonnable…"
    iris "…mais qu’en vrai il fout un merdier monstrueux derrière…"
    iris "Tu crois vraiment que Kami va faire quoi ?"
    iris taquin "‘Oups désolée’ ?"
    iris colere "Ou ‘ah bah c’est la faute de celui qui l’a écrit’ ? Genre, super la logique !"

    $ showP("sael", "determine", 0.78)

    sael "Elle pointera quelqu’un."
    sael "Toujours."
    sael "Et ce quelqu'un ce sera l'un d'entre nous."

    sael "Même si elle ne le dit pas clairement."
    sael "Même si c’est jamais écrit."

    sael "On en assumera les conséquences."

    hide iris
    $ showP("elen", "inquiet", 0.22)

    elen "Et puis…"
    elen "Tout le monde n’a pas forcément envie d'en parler."

    elen "Y a des idées ..."
    elen "Enfin voilà quoi ..."

    hide sael
    $ showP("julian", "sourire", 0.78)

    julian "Moi je veux bien en parler, hein."
    julian "Mais bon… je sens que je vais encore me faire passer pour le relou qui se la raconte."

    hide julian
    $ showP("mara", "neutre", 0.78)

    mara "C’est pas un risque, c’est ta marque de fabrique."
    mara "Au fait… c’est quoi ton blaze déjà ?"

    "Personne ne lui réponds vraiment."

    pause 0.3

    hide mara
    $ showP("ryn", "reflechit", 0.78)

    ryn "Et si on faisait rien ?"

    ryn "On vote contre tout."
    ryn "On touche à rien."
    ryn "Fin de l’histoire."
    ryn "Comme ça on ne change pas les habitudes, et tout le monde connait les règles ?"

    hide elen
    $ showP("nyra", "triste", 0.22)

    nyra "Ça veut dire accepter."
    nyra "Que ce monde reste comme il est."

    nyra "On va pas faire semblant que tout va bien, non ?"
    nyra "Y'a pas que du mauvais, mais y'a aussi des choses à changer."

    hide ryn
    $ showP("tomas", "hesitation", 0.78)

    tomas "Non. Ça ne marchera pas Ryn."
    tomas "Kami a dit que refuser un amendement."
    tomas "Pouvait aussi avoir un prix."

    tomas "On sait juste pas lequel."

    pause 0.3

    $ showP("kael", "reflechit", 0.50)

    kael "C’est exactement pour ça qu’il faut qu'on en parle."

    kael "Le silence."
    kael "C’est comme lui laisser le champ libre."

    hide kael
    hide nyra
    $ showP("lysa", "reflexion", 0.22)

    lysa reflexion "Ou alors…"
    lysa "c’est notre seule défense."
    lysa doute "Quelqu’un peut très bien mentir."
    lysa "Dire qu’il propose un truc alors qu’il en propose un autre."
    lysa blase "Avec seulement dix votes tirés au sort…"
    lysa "c’est l’alibi parfait."
    lysa fatigue "Personne pourra prouver le contraire."
    
    pause 0.4

    "Le silence retombe."
    "Pas un silence lourd."
    "Un silence méfiant."
    
    lysa "Comme il n'y a que dix votes. C'est l'alibi idéal pour justifier son mensonge."

    hide tomas
    $ showP("elias", "reflechit", 0.78)

    elias "Au fait les gars..."
    elias "Pendant qu’on tourne en rond, le chrono descend à vingt minutes."

    pause 0.4

    hide elias
    $ showP("ryn", "fatigue", 0.78)

    ryn "Ecoutez, faites ce que vous voulez."

    "Ryn se lève."
    
    "Il attrape une feuille de papier puis un stylo."
    "Sans aucune justification ni aucune parole."

    hide ryn

    play sound sfx_paper
    "Un froissement."
    "Puis le bruit sec du papier qui tombe au fond d'une boite."
    play sound sfx_drop

    think "Voilà."
    think "Le premier."

    hide lysa
    $ showP("nyra", "reflexion", 0.22)

    nyra "C’est allé vite…"

    hide nyra
    $ showP("mara", "sourire", 0.50)

    mara "Dès qu’un con commence…"
    mara "Tous les autres moutons suivent. Les gens sont vraiment des moutons."

    pause 0.3

    "Une chaise recule."
    "Puis une autre."

    $ showP("sael", "neutre", 0.78)

    sael "On peut en discuter pendant des heures."
    sael "Mais au final."
    sael "Chacun va écrire ce qu’il croit être juste."
    
    sael "Sauf que la justice, c'est une notion très personnelle."

    hide sael

    play sound sfx_drop
    "Un second papier tombe."
    "Puis un troisième."

    think "Plus personne ne débat vraiment."
    
    "On est encore quelques uns, debout."
    "On a les yeux baissés. On ose plus se regarder."

    $ showP("kael", "calme", 0.22)

    kael "Bon ... C'est donc votre choix."
    
    "Puis Kael s'éloigne à son tour."

    hide kael
    $ showP("julian", "neutre", 0.78)

    julian "C’est dingue, non ?"
    julian "C’est toujours quand tout le monde se tait…"
    julian "… que les vraies décisions se prennent."

    hide julian

    "L’urne se remplit."
    play sound sfx_paper
    "Lentement."
    play sound sfx_paper
    "Inexorablement."
    play sound sfx_drop

    think "C’est ça le Conclave."
    think "Pas un débat."
    think "Un enchaînement."

    $ showP("elen", "inquiet", 0.22)

    elen "Et si quelqu’un écrit quelque chose de terrible ?"

    $ showP("iris", "fatigue", 0.80)

    iris "Donc voilà : soit on vote contre, hein et rien ne change, sauf que même ça ça craint..."
    iris "soit on se tape les conséquences dans la tronche."
    iris "Comme d’hab’, quoi. Rien de neuf sous le soleil pourri."

    pause 0.4

    play sound sfx_paper
    "Plusieurs personnes sont debout."
    "D’autres écrivent encore."
    
    play sound sfx_drop
    "L'urne est presque entièrement remplie."
    "Le temps passe."
    "Il faut que je m'y mette moi aussi."
    jump _1_proposition_amendement

    return

# Durée du label : 2m
# Total : 58m15

label _1_proposition_amendement:

    scene bg_cg009 at adaptive_fullscreen
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    think "Ok."
    think "C’est à moi."

    "Le bruit des papiers qui tombent dans l’urne continue."
    "Pas fort."
    "Mais assez pour te rappeler que tu traînes."

    "Sur ma table, j'ai pris une feuille."
    "Un stylo."
    "Et il y a toujours ce vide au milieu de la poitrine."

    think "On dirait un examen."
    think "Sauf qu’ici…"
    think "si tu rates."
    think "Les conséquences peuvent être terribles."

    "Je fais tourner le stylo entre mes doigts."
    "Je le lâche."
    "Je le reprends."
    "Je sais que je suis assez ridicule comme ça."

    think "Respire, Noam."
    think "Fais pas semblant."
    think "T’as peur. Ok."
    think "C’est normal. Enfin, je crois que ça l'est."

    "Je baisse les yeux sur l’urne."
    "Elle est toujours là."
    "Comme si elle me regardait, comme si elle attendait."

    think "Il faut que je trouve quelque chose."

    "Je gratte un mot sur le papier."
    "Je le raye aussitôt."

    think "Il faut quelque chose qui puisse être utile."
    think "Quelque chose qui fait que les gens vivront mieux."
    think "Facile à dire. Difficile à trouver."

    pause 0.3

    "Une chaise grince derrière moi."
    "Quelqu’un passe."
    "Je n’ose même pas relever la tête."

    think "Ils écrivent tous."
    think "Comme si c’était simple."
    think "Comme si c’était… normal."

    "Je pose la pointe du stylo."
    "Et je reste bloqué."

    think "Ok."
    think "Il faut que je sois honnête avec moi même."
    think "J’hésite."
    
    pause 0.2

    think "Deux idées."
    think "Deux trucs très concrets."
    think "Deux propositions pour tenter de faire changer les choses."

    think "La première…"
    think "C’est l’information."

    think "Pas le monde."
    think "Pas les districts."
    think "Pas les grandes annonces."
    think "Mais celles du quotidien."

    think "Dire ce que je vois."
    think "Ce que je vis, ce que je ressens."

    think "Arrêter de faire semblant que parler de la pluie, du froid ou d’un problème local…"
    think "c’est une menace pour l’équilibre du monde."
    think "Actuellement ce n'est pas clair."
    
    "Le cinquième commandement dit que :"
    "La diffusion d’informations non validées par ARCHIVE est interdite."
    "Mais qu'est ce qui est validé ?"
    "Personne ne le sait vraiment."
    "Donc tout le monde évite de parler."

    pause 0.2

    think "La deuxième…"
    think "C’est le fait d'aider."
    think "Aujourd'hui, plus personne n'aide grand monde."
    think "On a peur de faire quoi que ce soit qui ne serait pas conforme aux Commandements."

    think "Le fait d'aider quelqu’un ne devrait pas être pénalisable."
    think "Quand quelqu'un est dans la merde."
    think "Quand on peut."
    think "Alors il faudrait permettre le fait d'aider."

    pause 0.3

    think "Les deux propositions me semblent raisonnables."
    think "Laquelle choisir ?"
    think "Je ne vois pas ce qu'il y aurait de mal à proposer ça ?."
    
    think "A moins que je ne fasse fausse route ?"

    think "Et évidemment…"
    think "C’est à moi de décider."

    pause 0.3

    "Je ferme les yeux une seconde."
    "Le bruit de l’urne continue."
    "Moins régulier."
    "Plus pressant."
    
    "Je souffle lentement."
    "Je redresse un peu le dos."

    think "Ok."
    think "Arrête de tourner autour du pot."
    think "Il faut choisir."
    
    tuto "Ah ça fait longtemps !"
    tuto "Il est désormais temps de vous parler d'une autre fonctionnalité majeure."
    tuto "Les choix !"
    tuto "Parfois, souvent, vous aurez des choix à faire."
    tuto "Ces choix sont majeurs et aboutiront à une histoire qui pourra être totalement différente."
    tuto "Lors de ces occasions, plusieurs choix apparaitront à l'écran. A vous de faire le choix qui vous interesse davantage."
    tuto "A noter qu'il n'y a pas de mauvaises réponses. Chaque choix vous fera découvrir une histoire différente."
    tuto "Certains choix seront marqués du mot clé (optionnel). Si vous les choisissez, vous pourrez alors suivre une scène optionnelle."
    tuto "Amusez-vous bien !"

    menu:
        "Quelle proposition Noam écrit-il ?"

        "Limiter l’interdiction de transmission d’informations à la politique":
            $ noam_amendement_choix = "information_locale"

            think "D’accord."
            think "Il faut libérer la parole."
            think "Mais pas n’importe comment."

            "J’écris une phrase."
            "Puis je m’arrête."
            "Je me relis."

            think "Je précise un mot qui me semble mal tourné, peu précis."
            think "Il ne faut pas tout changer, mais permettre une plus grande liberté est important."
            think "Ce qui touche aux districts et à la politique."
            think "Ça peut rester verrouiller."

            think "Mais le reste…"
            think "Le quotidien."
            think "Le local."
            think "L’immédiat, ce qu'on voit, ce qu'on dit, ce qu'on ressent."

            think "On devrait pouvoir le formuler comme on le souhaite."
            think "Sans risquer sa vie du moins."

            "Je reformule."
            "Encore."
            "J’enlève un mot."
            "J’en ajoute un autre."

        "Instaurer une obligation d’assistance quand une aide est possible":
            $ noam_amendement_choix = "assistance_minimale"

            think "Ok."
            think "Je vais essayer de permettre l’entraide."

            "J’écris un premier jet."
            "Ma main hésite."

            think "Il faut que la formulation ne soit pas un truc impossible."
            think "Juste…"
            think "qu'on puisse faire quelque chose quand on le peut."

            think "Aider."
            think "Prévenir."
            think "Intervenir."

            think "Parce que laisser quelqu’un tomber…"
            think "Ça aussi, c’est une décision."
            think "Une mauvaise décision."
            
            "Je fais attention à chaque formulation."

    pause 0.3

    "Quand j’ai fini d’écrire, ma main tremble un peu."
    "Pas assez pour lâcher le stylo."
    "Juste assez pour que je remarque la tension qui fait vibrer mes doigts."

    think "Voilà."
    think "C’est fait."

    "Je relis une dernière fois."
    "J’ai envie de corriger."
    "De nuancer."
    "De préciser encore."

    think "Non."
    think "Sinon je recommencerai encore et encore."
    
    "Je jette un coup d'oeil aux écrans."
    "Il ne reste plus que quatre minutes."
    
    think "ça fait tant de temps que ça ?."

    pause 0.2

    "Je plie la feuille."
    "Ce n'est pas très droit, c'est assez irrégulier."

    "Je me lève."
    "La chaise fait trop de bruit."
    "Ou alors c'est le fait que personne ne fait un bruit."

    think "Je sens le regard des caméras."
    think "Même sans forcément les voir."

    "Je marche jusqu’à l’urne."
    "Chaque pas est un peu trop long."
    "J'ai la gorge sèche."
    
    think "Et si j'avais fait le mauvais choix ?"
    think "Non. Arrête d'y penser."

    "Je glisse la feuille dans la fente."
    "Elle tombe au fond."
    "Je ne peux plus la récupérer."
    "Trop tard pour les regrets."

    pause 0.4

    think "Voilà."
    think "Mon premier amendement."

    "Je recule."
    "Je retourne à ma place."
    "J'étais le dernier."
    
    scene bg_conclave at adaptive_fullscreen with dissolve
    
    jump _1_AMENDEMENT_DEPOSE

# Durée : 3m
# Total : 1h 0m 15s

label _1_AMENDEMENT_DEPOSE:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Un léger grésillement."
    "Les écrans muraux s’allument presque en même temps."

    play sound sfx_beep
    "-Bip-"

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Dix-huit heures précises."

    kami "Le temps imparti pour le dépôt des amendements est désormais écoulé."

    pause 0.2

    kami "Je suis ravie."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Vraiment."
    kami "Vous avez tous participé."
    kami "Dans les temps."
    kami "Sans exception."

    pause 0.2

    kami "C’est rare."
    kami "Et très appréciable."

    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve

    kami "Grâce à vous, je n’aurai pas besoin d’éliminer qui que ce soit aujourd’hui."

    "Personne ne réagit."
    "Mais l’air semble se détendre d’un cran."
    "D'un cran seulement."

    scene bg_diffusion_fier at adaptive_fullscreen with dissolve

    kami "Les dix amendements soumis au vote seront tirés au sort."

    kami "Le tirage sera diffusé demain matin."
    kami "À neuf heures."
    kami "Sur l’ensemble des écrans."

    pause 0.2

    kami "Je vous conseille d’être attentifs."
    kami "Le hasard a parfois beaucoup de goût."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "En attendant."

    kami "L’accès aux chambres est désormais ouvert."
    kami "Vous êtes libres de circuler."
    kami "De manger."
    kami "De vous reposer."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    kami "Profitez-en."
    kami "Demain, on recommencera à jouer tous ensemble."

    play sound sfx_beep
    "-Bip-"

    scene bg_conclave at adaptive_fullscreen with dissolve

    "Les écrans s’éteignent."
    "Un par un."
    "Puis le silence retombe."

    pause 0.3

    "Personne ne parle tout de suite."
    "Comme si on attendait encore quelque chose."
    "Ou quelqu’un. Mais rien ne vient."

    "Puis les chaises raclent le sol."
    "Des pas."
    "Des soupirs."

    "Les représentants commencent à se disperser."
    "Sans vraiment se regarder."
    "Sans se dire au revoir."

    think "C’est fini."
    think "Pour aujourd’hui du moins."

    scene bg_couloir at adaptive_fullscreen with fade

    "Le couloir est éclairé."
    "Il est plus calme."
    "Presque normal."

    think "J’ai déposé un amendement."
    think "On en a tous déposé un."
    think "J’espère ne pas avoir fait une connerie."

    think "Demain matin à neuf heures."

    pause 0.3

    "Je m’arrête un instant."
    "Debout, au milieu du couloir."

    think "Je n’ai pas vraiment envie de réfléchir."
    think "Mais j’ai pas envie de rester seul avec ça en tête non plus."

    menu:
        "Que devrais-je faire ?"

        "Aller se coucher":
            $ choix_1_soir = "dormir"
            think "J’ai besoin de m’allonger."
            think "Même si je sais que je ne dormirai pas tout de suite."

            think "Juste…"
            think "Me couper un peu du monde et rester au calme."

            jump _1_FIN_JOURNEE_DORTOIR

        "Se rendre à la salle de repos (Optionnel)":
            $ choix_1_soir = "salle_repos"
            think "Je devrais aller à la salle de repos."
            think "Peut-être que quelqu’un y sera."
            think "Ou peut-être pas."

            think "Dans les deux cas…"
            think "ça me fera du bien."

            jump _1_SALLE_DE_REPOS_OPTIONNELLE

# Durée : 1m
# Total : 1h 1m 15s

label _1_SALLE_DE_REPOS_OPTIONNELLE:

    scene bg_repos at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "La salle de repos est allumée."
    "Pas trop."
    "Il y a cette lumière douce, presque agréable qui pulse du plafond."

    "Il n’y a pas grand monde."
    "Quelques canapés sont occupés."
    "La plupart sont vides."

    think "Je m’attendais à pire."
    think "Ou à plus de silence."

    pause 0.2

    $ showP("julian", "detendu", 0.78)

    julian "Ah."
    julian "Toi aussi t’as pas réussi à te coucher direct ?"

    think "Évidemment."

    $ showP("nyra", "sourire", 0.22)

    nyra "J’avais besoin de…"
    nyra "Je sais pas."
    nyra "Voir autre chose qu’un mur."

    "Julian se laisse tomber dans un fauteuil."
    "Un peu trop fort."

    julian "Franchement..."
    julian "J’ai cru que j’allais rester planté devant ma feuille blanche comme un con."
    julian "J’ai écrit une phrase entière, puis je l'ai supprimé, trois fois de suite."
    julian "Il fallait vraiment que je trouve quelque chose de bien.."

    pause 0.2

    $ showP("mara", "sourire", 0.50)

    mara "Moi j’ai arrêté de cogiter."
    mara "Sinon je devenais dingue."
    mara "J’ai écrit un truc."
    mara "Point barre."
    mara "Et si ça vous plaît pas, bah tant pis pour vos gueules."

    think "Tant pis."
    think "Facile à dire."

    pause 0.3

    "Quelqu’un rit."
    "Pas fort."
    "Mais assez pour que ça surprenne."

    julian "On est bien d’accord que c’est complètement n’importe quoi ?"
    julian "On réfléchit à ce qui peut aider les gens, on écrit des phrases."
    julian "… et demain matin le hasard décide si ça vaut de l’or ou si ça vaut zéro."
    julian "lmagine si ma proposition ne tombera pas dans les dix tirages ?!."

    nyra "Oui."
    nyra "Mais au moins…"
    nyra "on a écrit quelque chose."

    pause 0.2

    "Un silence s’installe."
    "Pas gênant."
    "Juste calme."

    think "C’est étrange."
    think "On dirait presque une soirée normale."

    mara "Vous croyez qu’elle nous mate là ? Genre… là, tout de suite ?"

    julian "Sûrement..."
    julian "Et pour tout te dire, j'espère bien !"
    julian "Ah qu'est ce que j'aimerais être repéré pour mes talents ici !"

    pause 0.3

    "Personne ne le reprend."
    "Personne ne le contredit."

    think "Ça fait du bien."
    think "De ne pas faire attention pendant deux minutes."

    pause 0.4

    play sound sfx_door

    scene bg_cg010 at adaptive_fullscreen with dissolve
    show screen kami_broadcast_ui

    "La porte de la salle de repos s’ouvre."

    "Quelqu’un hésite un instant."
    "Puis il avance."

    tomas "Euh…"
    tomas "Bonsoir."

    "Tomas entre."
    "Un plateau entre les mains."
    "Six tasses."
    "Il marche lentement."
    "Beaucoup trop concentré sur son équilibre."

    $ bc_show("julian", "detendu", px=-70, py=-50, pz=0.85)
    julian "…"
    julian "Ok."
    julian "Respect vraiment."

    $ bc_show("nyra", "joie", px=-70, py=-50, pz=0.85)
    nyra "Fais pas semblant d’être détendu."
    nyra "On voit très bien que tu stresses."
    $ bc_hide()

    tomas "Disons que si je renverse ça."
    tomas "Je meurs socialement et je vais me cacher sous une table pendant le reste du mois."

    $ bc_show("mara", "content", px=-70, py=-50, pz=0.85)
    mara "Y’a pire."
    mara "Tu pourrais mourir pour de vrai."
    $ bc_hide()

    "Un léger rire passe."
    "Bref, presque timide."

    tomas "J’me suis dit que…"
    tomas "Ça ferait peut-être du bien."
    tomas "Un truc chaud."

    "Il pose enfin le plateau sur la table."
    "Sans rien renverser."

    $ bc_show("julian", "joie", px=-70, py=-50, pz=0.85)
    julian "Putain."
    julian "T'es un vrai héros mec."
    $ bc_hide()

    pause 0.3

    scene bg_cg010_1 at adaptive_fullscreen with dissolve
    $ showP("tomas", "vide", 0.01)
    $ showP("julian", "vide", 0.30)
    $ showP("noam", "vide", 0.65)
    $ showP("mara", "vide", 0.80)
    $ showP("nyra", "vide", 0.99)

    "Les tasses circulent."
    "Les mains se tendent."
    "La vapeur monte doucement."

    think "Ça sent le thé."
    think "Un vrai thé bien fort comme il faut."
    think "Pas un truc synthétique."

    nyra "J’avais presque oublié ce que ça faisait."
    nyra "Tenir quelque chose de chaud."

    mara "Ouais…"
    mara "C’est débile mais ça fait du bien."
    mara "Un tout petit peu."

    "Je prends la tasse."
    "Elle me brûle presque les doigts."
    "Mais je la garde quand même."

    think "C’est idiot."
    think "Mais ça m’ancre."

    tomas "Demain…"
    tomas "À neuf heures on saura ..."

    julian "Ouais."
    julian "Demain."

    "Personne n’ajoute rien."
    "Mais tout le monde y pense."

    pause 0.4

    "On boit."
    "En silence."

    think "Je sais pas combien de temps ce calme durera."
    think "Mais là, en ce moment…"
    think "C’est agréable."

    pause 0.4

    "Les tasses se vident."
    "Le plateau n’en garde plus qu’une."
    "Personne ne la prend."

    mara "Bon bah voilà."
    mara "Je vais aller me pieuter avant de péter un câble."

    nyra "Moi aussi."
    nyra "Avant que je recommence à réfléchir."

    julian "Excellente idée."

    "Ils se lèvent."
    "Un à un."

    think "La parenthèse se referme."

    pause 0.3

    "Je reste encore quelques secondes."
    "Assis."
    "La tasse vide entre les mains."

    think "Je devrais y aller aussi."

    jump _1_FIN_JOURNEE_DORTOIR

# Durée : 1m55
# Total : 1h 3m 10s

label _1_FIN_JOURNEE_DORTOIR:

    scene bg_couloir at adaptive_fullscreen
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "Le couloir est plus calme."
    "Pas vide."
    "Mais plus lent."

    "Les pas résonnent différemment."
    "Comme si le bâtiment lui-même soufflait un peu."

    think "Ça y est."
    think "La journée est finie."
    think "Enfin… presque."

    "Je marche sans me presser."
    "Je laisse les pensées glisser."
    "Sans vraiment m’y accrocher."

    pause 0.3

    scene bg_dortoir at adaptive_fullscreen with fade

    "Le dortoir est allumé."
    "Une lumière plus chaude."
    "Moins clinique."

    "Quelqu’un est déjà là."

    $ showP("elias", "detendu", 0.50)

    if choix_1_soir == "salle_repos":

        elias "Ah. Toi aussi t’es encore debout."

        think "Elias."
        
        $ showP("noam", "neutre", 0.15)

        noam "Ouais."
        noam "J’avais pas trop envie de rester seul."

        elias "Je vois."
        elias "La salle de repos, hein ? … Pas con."

        noam "Ouais."

        elias "Bonne idée."
    
        elias "Moi j’ai tenté de dormir direct."
        elias "Raté."

    if choix_1_soir == "dormir":
        
        elias "En voilà un se couche tôt."
        elias "Laisse moi deviner, envie de rester seul ?"
        
        $ showP("noam", "neutre", 0.15)
        
        noam "On peut dire ça."
        noam "Drôle de journée."

    pause 0.2

    "Il sourit."
    "Un vrai sourire."
    "Un peu fatigué."

    elias "C’est chelou quand même."
    elias "Journée à rallonge, stress au max…"
    elias "… et je suis rincé comme après douze heures sur un chantier."

    noam "Ouais."
    noam "Comme après un déménagement."
    noam "Ou un examen."

    elias "Exactement. C'est l'idée."

    pause 0.3
    
    $ showP("elias", "inquiet", 0.50)

    elias "Demain matin…"
    elias "Ça va être un autre calibre."

    noam "Ouais."
    
    $ showP("elias", "jaloux", 0.50)

    "On n’insiste pas."
    "Pas besoin."

    elias "Bonne nuit, Noam."

    noam "Bonne nuit."

    hide elias

    pause 0.3

    scene bg_chambre at adaptive_fullscreen with fade

    "Ma chambre."
    "Petite."
    "Propre."
    "Silencieuse."

    think "Enfin seul."

    "Je pose mes affaires."
    "En fait, je les jette presque."
    "Je suis épuisé."
    
    "Je jette un regard sur ce qui compose ce qui me servira de chambre pendant un mois."
    "Honnêtement, c'est pas mal du tout."
    "Le lit est grand, une garderobe avec des affaires ..."
    
    think "Non, ce sont MES affaires !"
    
    "Il y a du matériel informatique également."
    "Je me demande à quoi on a accès."
    
    "Sur le côté de la chambre, il y a aussi un accès à un toilette privatif ainsi qu'une salle de bain."
    "Franchement, une douche bien chaude ça me tente bien."
    
    "Bon ... Allez."

    pause 0.2

    scene bg_cg011 at adaptive_fullscreen with dissolve

    play sound sfx_shower

    "L’eau chaude coule."
    "Longtemps."
    "Mais qu'est ce que ça fait du bien."

    "Je ferme les yeux."
    "Je profite du moment."
    "Je laisse la journée partir avec la vapeur."

    think "Pas ce soir."
    think "Je réfléchirai demain."

    pause 0.5

    scene bg_chambre at adaptive_fullscreen with fade

    "Je sors de la douche puis m’allonge tranquillement sur le lit."
    "Il est plus confortable que je ne l’imaginais."

    think "Mon amendement est déposé."
    think "Le reste ne m’appartient plus."

    "Le plafond est immobile."
    
    $ blink()
    
    "Pour une fois."

    $ blink()
    
    pause 0.4

    $ blink()
    
    "Je ne vais pas tarder à dormir."
    
    $ blink()

    scene black with fade
    stop music fadeout 2.0
    
    call end_day("2")

    jump _2_CANON

# Durée : 1m40
# Total : 1h 4m 50s