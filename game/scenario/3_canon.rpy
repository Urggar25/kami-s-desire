label _3_CANON:

    $ day_id = 3

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    pause 0.5

    think "…"

    pause 0.3

    think "Je suis réveillé."
    think "Je crois."

    pause 0.4

    "Je ne bouge pas."
    "Mon dos est raide."
    "Mes épaules me lancent."

    pause 0.4

    think "J’ai dormi ?"
    think "Ou j’ai juste fermé les yeux en attendant le matin ?"

    pause 0.5

    think "Aujourd’hui."

    pause 0.4

    think "Le vote."

    pause 0.6

    think "Un seul non."
    think "Et tout s’arrête."

    pause 0.6

    think "C’est ridicule que ce soit aussi fragile."

    pause 0.5

    scene bg_cg012 at adaptive_fullscreen with fade

    "Je fixe le plafond."
    "Blanc."
    "Lisse."
    $ blink()
    "Propre."

    pause 0.4

    think "Trop propre."
    $ blink()

    pause 0.5

    "Un bruit de pas dans le couloir."
    "Ça traîne."
    "Ça hésite."

    pause 0.4

    think "Personne ne semble courir."
    think "Personne ne parle fort."

    pause 0.6

    play sound sfx_announce

    pause 0.8

    # Diffusion de Kami
    stop music fadeout 1.0
    scene bg_diffusion_neutre at adaptive_fullscreen with fade
    show screen kami_broadcast_ui

    play music "music/bgm_system_override.mp3" fadein 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Booooonjour mes petits représentants ♥"

    pause 0.4

    kami "Jour trois !"
    kami "Déjà fatigués ?"

    pause 0.4

    kami "Petit rappel doux et adorable :"
    kami "Aujourd’hui, c’est le jour de vote."

    pause 0.5

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Unanimité absolue."
    kami "Un seul petit non, et… pfiou."

    pause 0.4

    kami "On efface tout."
    kami "On recommence, et tant pis pour la proposition."

    pause 0.5

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'un d'entre vous se sera creusé les méninges pour rien !"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Alors souriez bien."
    kami "Et méfiez-vous un tout petit peu les uns des autres."

    pause 0.4

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ça met du piment~"
    kami "Et j'adore ça !"

    pause 0.4

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Rendez-vous au Conclave à 14h ♥"

    pause 0.3

    hide screen kami_overlay with dissolve

    pause 0.8
    scene bg_cg012 at adaptive_fullscreen with fade

    think "…"

    pause 0.4

    think "Elle adore ça."
    think "Appuyer là où ça fait mal."

    pause 0.6

    think "Un seul non."

    pause 0.6

    think "Qui pourrait voter contre ?"

    pause 0.5

    think "Personne n’a intérêt à voter contre."
    think "Alors pourquoi j’ai cette drôle de sensation ?"

    pause 0.6

    scene bg_chambre at adaptive_fullscreen with fade
    "Je me redresse. J'allume la lumière."
    "Mes vertèbres craquent."

    pause 0.4

    think "Super."

    pause 0.4

    "Je passe mes mains sur mon visage."
    "Peau froide."
    "Mâchoire serrée."

    pause 0.5

    think "Respirer."
    think "Une étape à la fois."

    pause 0.5

    pause 0.4

    "Je me lève."
    "Le sol métallique est froid sous mes pieds."

    pause 0.5

    think "Ça réveille."

    pause 0.4

    "Je bois un peu d’eau."
    "Deux gorgées."
    "Je n'ai pas très faim, j'ai la gorge nouée."

    pause 0.5

    think "Mais il faut quand même que j'aille à la cafétéria."

    pause 0.5

    scene bg_couloir at adaptive_fullscreen with dissolve

    pause 0.4

    "Le couloir est étrangement calme."

    pause 0.5

    think "Même la ventilation semble retenir son souffle."

    pause 0.4

    "Deux silhouettes marchent devant moi."
    "Elles ralentissent en m’entendant."
    "Puis reprennent."

    pause 0.5

    think "On se surveille sans le dire."

    pause 0.4

    "Je croise Kael au détour du couloir."

    $ showP("noam", "neutre", 0.20)
    $ showP("kael", "fatigue", 0.65)

    kael fatigue "Salut."

    "Sa voix est plus basse que d’habitude."

    noam "Tu vas à la cafétéria ?"

    kael reflechit "Oui."
    kael doute "Enfin… oui."

    "Il ne bouge pas."
    "Il reste là une seconde de trop."

    kael inquiet "Tu es sûr que c’est une bonne idée ?"

    noam "Le commerce ?"

    kael reflechit "Oui."
    kael reflechit "On dit tous que ça ne changera pas grand-chose."
    kael inquiet "Mais si ça dérape ?"

    "Il évite toujours mon regard."

    noam "Tu penses que ça peut vraiment déraper ?"

    kael culpabilite "Je ne sais pas."
    kael fatigue "Je préfère quand les choses sont stables."
    kael reflechit "On vient à peine d’arriver."
    kael inquiet "On ne sait même pas encore comment on fonctionne ensemble."
    kael reflechit "Et on commence déjà à modifier les règles."

    "Il ne dit pas non."
    "Il ne dit pas oui non plus."

    noam "Tu veux voter contre ?"

    kael surpris "Non."
    kael doute "Enfin… je ne crois pas."
    kael reflechit "Je suis pour."
    kael sourire "En théorie."

    "En théorie."

    kael reflechit "Je n’aime pas avancer sans savoir où on met les pieds."
    kael inquiet "Changer quelque chose, c’est accepter de ne plus revenir en arrière."

    "La ventilation souffle au-dessus de nous."
    "Le bruit semble plus fort que d’habitude."

    kael inquiet "Tu n’as pas peur ?"

    noam "Si."
    noam "Mais ne rien changer, c’est aussi un choix."

    "Il baisse légèrement les yeux."

    kael fatigue "Je déteste ça."
    kael reflechit "Décider."
    kael culpabilite "Et ne pas savoir si on va le regretter."

    "Il pourrait basculer."

    kael calme "On verra à 14h."
    kael sourire "Bonne chance."

    "Il passe à côté de moi."
    "Son épaule frôle la mienne."

    "Il n’a pas tranché."
    "Et ça suffit à me serrer l’estomac."


    hide noam
    hide kael

    "Je continue."

    pause 0.5

    "Julian est près du distributeur."
    "Il tapote la machine comme si elle lui devait quelque chose."

    $ showP("noam", "neutre", 0.30)
    $ showP("julian", "joie", 0.75)

    julian joie "Hey."
    julian taquin "Alors ? Prêt à secouer un peu ce système ?"

    "Un large sourire illumine son visage."

    noam "On va essayer."

    julian rire "Essayer ?"
    julian joie "Non, non."
    julian "On va le faire."

    "Il attrape sa tasse."
    "Le café déborde un peu."
    "Il ne s’en rend même pas compte."

    julian reflexion "Tu te rends compte ?"
    julian joie "Si ça passe, on ouvre la première brèche depuis la prise de pouvoir de Kami."

    julian taquin "Du commerce. Des échanges."
    julian joie "Du mouvement."

    "Ses yeux brillent."
    "Il aime l’idée."

    noam "Et si ça ne passe pas ?"

    julian hesitation "Ça passera."
    julian sourire "Il faut que ça passe."

    "Il appuie un peu trop fort sur les mots."

    julian reflexion "On ne peut pas rester figés."
    julian "On n’est pas venus ici pour maintenir le statu quo."
    julian joie "On est là pour changer les choses."
    julian idee "Les gens veulent du changement."

    "Il redresse les épaules."
    "Il se voit déjà dans l’après."

    noam "Tu es sûr que tout le monde suivra ?"

    julian hesitation "…"

    "Une micro-seconde."
    "Presque rien."

    julian sourire "Ils suivront."
    julian taquin "Ils aiment juste faire semblant d’hésiter."

    "Il me regarde droit dans les yeux."

    julian reflexion "Et puis franchement."
    julian joie "C’est le commerce."
    julian "Personne ne va voter contre ça."

    "Il y croit."
    "Ou il veut y croire."

    julian sourire "Imagine un peu."
    julian joie "Des districts qui échangent vraiment."
    julian "Des ressources qui circulent."
    julian "Des idées qui bougent."
    julian idee "Comme avant ! Tu te rends compte !"
    julian taquin "Ça te plaît pas ?"

    "Il parle plus vite."
    "Comme s’il avait déjà validé le résultat."

    noam "Si. Evidemment que dis comme ça, sur le papier, ça me plaît."

    "Mais son enthousiasme me met mal à l’aise."

    julian reflexion "On a besoin d’un élan."
    julian joie "On peut changer les choses. A nous de le faire."

    "Il boit une gorgée."
    "Grimace."
    "Le café est mauvais."

    julian sourire "À 14h."
    julian joie "On ouvre le bal et on change ce monde."

    $ add_argument("Le monde d'avant")
    show screen argument_unlock("Le monde d'avant")

    "Il pivote vers la cafétéria."

    "Il marche vite."
    "Trop vite."

    "Il veut que ça passe."
    "Pas seulement pour le monde."

    "Pour lui aussi."

    hide noam
    hide julian

    scene bg_cafeteria at adaptive_fullscreen with dissolve

    pause 0.5

    "Le bruit des conversations est bas."
    "Trop bas."

    pause 0.6

    think "On fait semblant d’être normaux."

    pause 0.5

    "Ryn parle à voix basse avec Elen."
    "Mara regarde un écran éteint sans vraiment le voir."
    "Iris tient sa tasse sans boire."

    pause 0.6

    think "Tout le monde calcule."

    pause 0.5

    think "Si quelqu’un vote contre."
    think "Qui serait-ce ?"

    pause 0.6

    think "Mara ?"
    think "Non."

    pause 0.4

    think "Sael ?"
    think "Elle serait frontale."

    pause 0.5

    think "Ou peut-être que je me raconte des histoires."

    pause 0.6

    think "C’est ça le pire."
    think "Le doute."

    pause 0.6

    "Je prends un café."
    "Il est amer."
    "Plus que d’habitude."

    pause 0.5

    think "Un seul non."

    pause 0.6

    think "Et on aura juste prouvé qu’on n’est pas capables de s’entendre."

    pause 0.6

    think "Respire."

    pause 0.6

    think "Aujourd’hui, on décide si on est un groupe."
    think "Ou juste douze personnes enfermées ensemble."

    pause 0.8

    jump _3_CAFETERIA_DEBAT

# Durée : 3m45
# Totale : 1h 27m 55s

label _3_CAFETERIA_DEBAT:

    scene bg_cafeteria at adaptive_fullscreen with fade
    play music "music/bgm_quiet_routine.mp3" fadein 1.0

    "La cafétéria est pleine."
    "Mais ça parle à peine."
    "Un brouhaha… sans bruit."
    "Des fourchettes."
    "Des chaises."
    "Des souffles."

    pause 0.4

    "Je m’assois."
    "Pas au centre."
    "Pas trop visible."

    pause 0.3

    $ showP("noam", "neutre", 0.82)
    $ showP("elen", "joie", 0.22)
    $ showP("iris", "fatigue", 0.50)

    "Elen est déjà là."
    "Et Iris aussi."
    "Côte à côte."
    "Comme si ça s’était fait tout seul."

    pause 0.3

    scene bg_cg013 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg013")

    "Elen a un bol."
    "Un bol énorme."
    "Ça fume."
    "Ça sent…"
    "Je ne sais pas vraiment en fait."
    "La forêt ?"
    "Le dessert ?"

    pause 0.3

    iris "… C’est quoi ça ..?"

    elen rire "C’est."
    elen rire "Une MASTERPIECE."

    iris "Je suis pas sûre que ce mot s’applique ici."

    elen joie "Pâtes."
    elen joie "Noix."
    elen joie "Et…"
    elen taquin "Un petit truc secret."

    iris "Un petit truc secret, c’est exactement comme ça qu’on finit à l’infirmerie."

    elen rire "T’inquiète."
    elen rire "C’est Goumi qui a validé."
    elen taquin "Goumi ne tue pas ses clients."
    elen taquin "Il n'en a jamais tué volontairement."

    iris desaccord "… C’est pas rassurant."

    pause 0.3

    "Elen plonge sa fourchette."
    "Elle mélange."
    "Elle goûte."
    "Ses yeux brillent."

    elen joie "Oh putain."
    elen joie "C’est trop bon."
    elen rire "C’est EXACTEMENT trop bon."

    iris "Tu joues à quoi."
    iris "À te convaincre toi-même ?"

    elen taquin "Quelle rabat-joie ! J'ai bien le droit d'être heureuse."
    elen taquin "Ça te dérange ? Tu devrais essayer de temps en temps."

    iris fatigue "Ça me fatigue rien que de te regarder."

    pause 0.3

    "Elen se marre."
    "Vraiment."
    "Ça tranche avec l'atmosphère du reste de la pièce."

    elen rire "Mais goûte."
    elen rire "Juste une bouchée."
    elen rire "Allez, jsute une !"
    elen taquin "Pour l’art. Tu es bien courageuse non ?"

    iris "Non."

    elen surpris "Même pas pour la postérité ?!"

    iris "Surtout pas..."

    pause 0.3

    "Elen hausse les épaules."
    "Elle s’en fout."
    "Elle remange."

    elen content "Ok."
    elen content "Plus pour moi."
    elen content "C-ça... m'va..."

    pause 0.4

    "Je regarde mon plateau."
    "Rien d’extra."
    "Rien de drôle ou d'extravagant."
    "Juste une barre de céréale avec un jus de fruit."
    "J'ai toujours cette nausée qui me prends aux tripes."

    pause 0.3

    noam "Goumi t’a laissé commander ça ?"

    elen joie "Ouaiiiis."
    elen joie "J'lui ai fait ce regard."

    scene bg_cg013_1 at adaptive_fullscreen with fade
    "Elle commence à imiter un regard... Particulier."

    elen taquin "Le regard ultiiime !"

    iris "Le regard du caprice, oui."

    elen rire "Mais le regard du caprice, c’est mignon."
    elen rire "Je me suis entrainée à le faire celui-là !"

    scene bg_cg013 at adaptive_fullscreen with fade
    pause 0.3

    "Iris fixe le bol."
    "Comme si le bol allait bouger. Comme si son contenu était vivant."
    "Comme si ça allait lui sauter au visage."

    iris "On dirait des pâtes…"
    iris "Avec des cailloux."

    elen "C’est des noix."

    iris "Oui."
    iris "Mais je me dis qu'avec des cailloux ça serait peut-être meilleurs encore."

    elen taquin "Ah ouais tu crois !?."

    iris desaccord "Mon dieu, dites moi qu'elle n'est pas aussi simple d'esprit..."
    iris desaccord "Sois lucide bon sang ! Bien sur que non !!"

    pause 0.3

    "Elen mâche."
    "Elle ferme les yeux."
    "Elle fait un petit bruit satisfait."
    "Vraiment pas discret."

    iris fatigue "…"

    elen joie "Tu vois ?"
    elen joie "La vie."
    elen joie "C’est ça."
    elen taquin "Profiter, et s'en fouttre de ce que les autres pensent."
    elen taquin "Et comme ça, rien ne t'atteint !"

    iris "Tu dis ça comme si c’était normal."

    elen "Ça devrait en tout cas."

    pause 0.5
    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showP("noam", "neutre", 0.82)
    $ showP("elen", "joie", 0.22)
    $ showP("iris", "fatigue", 0.50)

    iris "T’as pas peur."
    iris "Deux secondes ?"

    elen "Si."
    elen "Mais là, maintenant, tout de suite, j’ai faim."
    elen joie "Alors je m'en fou d'avoir peur."

    iris "…"

    pause 0.3

    "Iris détourne les yeux."
    "Elle a l’air de se retenir de dire quelque chose."
    "Elle avale sa salive mais retient ses mots."

    pause 0.4

    $ showP("elen", "taquin", 0.22)

    elen taquin "T’as envie de me faire la morale, hein."

    iris "Un peu."

    elen rire "Vas-y."
    elen rire "Je t’écoute."
    elen taquin "Héhé, balance ton sermon."

    iris fatigue "Non."
    iris fatigue "Laisse tomber."

    pause 0.4

    "Une chaise racle."
    "Quelqu’un passe derrière."
    "On ne regarde pas."

    pause 0.4

    hide noam
    $ showP("elias", "neutre", 0.82)

    "Elias arrive."
    "Son plateau est…"
    "Triste, propre, calibré."

    pause 0.3

    elias "Vous mangez quoi."

    elen joie "Le bonheur."

    iris "Ne la crois surtout pas..."

    elias inquiet "…"
    elias inquiet "On doit manger correctement."
    elias inquiet "Surtout maintenant."

    elen taquin "Oh non."
    elen taquin "Le discours nutrition."

    elias "Je plaisante pas."

    iris "Il plaisante jamais."
    iris taquin "Crois moi. Ca c'est vrai."

    "IJ s'assoit à la table auprès de nous."
    elias "Protéines."
    elias "Œufs."
    elias "Poulet."
    elias "Simple, efficace, nutritif et bon."

    pause 0.3

    "Elen le regarde."
    "Comme si Elias venait de lui dire de boire de l’eau tiède pour s’amuser."

    hide elen
    $ showP("elen", "surpris", 0.22)

    elen "Poulet."
    elen "Ici."
    elen "Alors que tu peux manger tout ce que tu veux ?!"

    elias "C’est une base."
    elias "Un principe."
    elias "Il vaut mieux manger quelque chose qui tient bien au corps."
    elias "Mais on arrête les…"
    elias inquiet "les pâtes aux noix."

    iris "Merci."

    elen colere "Oh !"
    elen colere "C’est pas des pâtes aux noix."
    elen colere "C’est une œuvre d'art gustative."

    elias "Franchement, laisse moi en douter..."

    elen "Ça dépend laquelle."

    pause 0.3

    "Elias soupire."
    "Comme s'il s'interdisait de dire quelque chose."

    hide elias
    $ showP("elias", "reflexion", 0.82)

    elias "Je dis juste."
    elias "Cet aprèm, on devra être lucides."
    elias "On doit tenir."
    elias "On peut pas se permettre d’être mous."
    "Elias remue son œuf du bout de la fourchette. Comme s'il le regrettait déjà."

    pause 0.3

    hide iris
    $ showP("iris", "hesitation", 0.50)

    iris "…"

    elen "On devait pas en parler."

    elias "Personne veut en parler."
    elias "C’est pour ça que ça tourne dans les têtes."

    pause 0.4

    "Elen remange."
    "Mais moins fort."
    "Elle écoute d'une oreille."

    pause 0.3

    iris "On n’est pas obligés."
    iris "Là."
    iris "Maintenant. On est en train de manger."

    elias "Non."
    elias "Mais on fait quoi, alors."
    elias "On arrive au vote et on improvise ?"

    elen "Moi, je vais pas improviser."
    elen "Je sais déjà ce que je vais faire."

    pause 0.3

    "Elen s'exclame en sautillant sur elle même un bas en l'air."
    $ showP("elen", "joie", 0.22)

    elen joie "Je vote pour !!"

    pause 0.4

    "Elle le dit comme si elle annonçait le dessert à un mariage."
    "Sa voix ne tremble pas, elle se fiche des caméras, se fiche du regard des autres."
    "Comme Elen le ferait.."

    iris "Tu le dis facilement."

    elen taquin "Parce que c’est facile."
    elen taquin "On crève d’ennui ici."
    elen taquin "Et dehors, ils crèvent pour de vrai."

    iris "…"

    elias "Tu marques un point."

    pause 0.4

    "Silence."
    "Un silence qui n’a pas envie d’être cassé."
    "Mais qui se casse quand même."

    pause 0.3

    hide elias
    $ showP("julian", "neutre", 0.82)

    "Julian débarque."
    "Il embarque une chaise et s’assoit un peu trop vite avec nous."
    "Comme s’il avait peur qu’on change de sujet."

    julian "J’ai entendu “je vote pour” ?"

    elen rire "Oui."
    elen rire "Bienvenue au club !!"

    julian sourire "Moi aussi."
    julian sourire "Evidemment que je vote pour !"

    iris hesitation "Julian…"

    julian "Quoi ?"
    julian "Je vais pas faire semblant et je vais pas garder ça pour moi."
    julian taquin "Je suis de toute façon incapable de faire semblant."

    "Julian jette un œil vers une caméra au plafond. Un réflexe. Sourire intact."

    pause 0.3

    "Tout le monde regarde dans notre direction dans la pièce."
    "Bravo Elen, pour attirer l'attention de tout le monde, ça tu sais faire..."

    pause 0.3

    elen taquin "Ok."
    elen taquin "Question simple."
    elen taquin "Qui vote pour ?"

    pause 0.4

    "Julian lève la main."
    "Comme à l’école."
    "Ça fait presque rire."

    julian rire "Pour."

    pause 0.3

    hide julian
    $ showP("noam", "hesitation", 0.82)

    "Je sens des regards."
    "Pas accusateurs."
    "Juste…"
    "En attente."

    noam "Tu votes pour... sans 'mais' ?"
    "Elen hausse les épaules, comme si c'était évident."
    think "Et moi ? Si c'était si simple..."
    noam "Et si le texte est foireux ?"

    pause 0.3

    "Elen claque sa langue, contente."

    hide elen
    $ showP("elen", "content", 0.22)

    elen content "Voilà."
    elen content "Ça fait déjà du bien."

    iris fatigue "Je te rappelle que si une seule personne n'est pas d'accord, ça fout tout en l'air."

    pause 0.3

    "Elias hoche la tête."
    "Une fois."

    hide noam
    $ showP("elias", "determine", 0.82)

    elias "Pour."
    elias "Mais…"
    elias "Faut que ce soit vraiment appliqué."

    elen taquin "Ça y est."
    elen taquin "Le “mais” est arrivé."
    elen rire "Je l’attendais."

    elias "Je suis sérieux."

    iris "Lui aussi."

    pause 0.4

    "Plus loin, d’autres s’approchent."
    "Pas en groupe."
    "Par petites vagues."
    "Comme si personne ne voulait avoir l’air de venir écouter."

    pause 0.3

    hide elias
    $ showP("kael", "neutre", 0.82)

    "Kael passe."
    "Plateau à la main, il s'apprête à s'éloigner quand Elen lui barre la route."
    "Son visage ne bouge presque pas."

    pause 0.4

    elen "Kael ?"
    elen "Pour ou contre ?"

    pause 0.4

    hide kael
    $ showP("kael", "reflechit", 0.82)

    "Kael ouvre la bouche."
    "Puis la referme."
    "Comme s’il mesurait le poids du mot."

    kael "…"
    kael "Je sais pas. Je verrais."

    pause 0.3

    elen "Ok."
    elen "Réponse honnête."

    iris "Au moins."

    pause 0.4

    hide kael
    $ showP("mara", "mefiant", 0.82)

    "Mara arrive derrière."
    "Elle ne s’assoit pas tout de suite."
    "Elle regarde les plateaux."
    "Puis les visages."

    mara "Je vous entends de loin."
    mara "C’est dangereux de dire ce que vous allez faire."

    elen rire "Oh non."
    elen rire "On est démasqués."

    mara mefiant "Je rigole pas."

    pause 0.3

    iris "Tu votes pas pour ?"

    mara "J'ai pas dis pas ça."

    pause 0.3

    "Elle prend enfin une chaise."
    "Pas au centre."
    "Sur le bord."
    "Comme si elle gardait une sortie."

    hide mara
    $ showP("mara", "doute", 0.82)

    mara "Je comprends l’idée."
    mara "Vraiment."
    mara "Mais…"
    mara "On ouvre une porte dont on connait pas les conséquences."
    mara "Et j’aime pas les portes qu’on ouvre sans voir derrière."

    elen "C’est du commerce."
    elen "C'est pas comme si on proposait l'éradication des bébés pinguins !"

    mara doute "T’es sûre ?"

    pause 0.4

    iris "Mara…"

    mara "Non."
    mara "Laissez."
    mara "Je fais pas ma dramatique."
    mara "Je dis juste : et s'il y avait un détail qu'on avait pas compris ?"
    mara "D'ailleurs, il est où l'intitulé ?"
    mara "Il faut bien le voir avant de se décider, être surs de pas faire une connerie."

    pause 0.3

    "Elen se redresse."
    "Prête à répondre trop fort."
    "Puis elle se retient."
    "Elle respire."

    hide elen
    $ showP("elen", "reflechit", 0.22)

    elen "Ok."
    elen "Je t’entends."
    elen "Vraiment."
    elen "Mais…"
    elen "On fait quoi sinon ?"
    elen "On regarde les gens crever et on se dit que c'est pas de notre faute ?"

    mara "Je dis pas ça."

    elias "Elle dit que c’est une décision à prendre."

    julian "Tout a un prix ici."

    pause 0.3

    "Mara serre la mâchoire."

    hide mara
    $ showP("mara", "stress", 0.82)

    mara "Je suis pas “contre” par principe."
    mara "Je suis…"
    mara "Réticente."
    mara "Parce que si ça part mal, ça part très mal."
    mara "Et après, c’est nous."
    mara "Pas Kami."
    mara "Nous. Qui en subiront les conséquences."
    "Mara serre son plateau si fort que ses jointures blanchissent."

    pause 0.4

    noam "Tu veux des garanties."

    mara "Oui."

    iris "Et si on en a pas ?"

    mara "Alors je veux que la proposition ne soit pas ambigüe."

    pause 0.4

    elias "Ça, c’est raisonnable."

    julian "C’est chiant, mais raisonnable."

    elen taquin "Ok."
    elen taquin "Donc t’es pas contre, tu vas voter pour."

    mara stress "Je te jure…"

    elen rire "Je plaisante."

    pause 0.4

    "Le bruit de la cafétéria revient."
    "Il n'est pas spécialement plus fort mais un peu plus présent."
    "Comme si les gens respiraient à nouveau."

    pause 0.3

    "Certains acquiescent."
    "D’autres évitent encore de se mouiller."
    "Mais le truc est là."
    "Une tendance."
    "Un consensus mou plutôt en faveur du vote."

    pause 0.4

    hide kael
    $ showP("kael", "neutre", 0.82)

    "Kael mange."
    "Sans regarder personne."
    "Mais il écoute tout."

    pause 0.3

    iris "On va pas régler ça ici."

    elias "Non."

    julian "Mais au moins…"
    julian "On sait que ça penche pour le “pour”."

    elen joie "Ça me suffit pour maintenant."

    pause 0.3

    "Elen finit une bouchée."
    "Elle pousse son bol."
    "Satisfaite, malgré tout."

    hide elen
    $ showP("elen", "content", 0.22)

    elen content "Ok."
    elen content "Je vais aller digérer mon œuvre."
    elen taquin "Et peut-être convertir d’autres âmes."

    iris "Bonne chance."

    elen rire "Merci."
    elen rire "Je suis née pour ça."

    pause 0.4

    "Julian se lève aussi."

    hide julian
    $ showP("julian", "sourire", 0.82)

    julian "Je vais faire un tour aussi."

    pause 0.4

    "Elias récupère son plateau."

    hide elias
    $ showP("elias", "neutre", 0.82)

    elias "Je retourne au…"
    elias "Je sais même pas."
    elias "Au calme."

    mara "Ouais."

    pause 0.4

    "Mara se lève à son tour."
    "Toujours sur le bord."

    hide mara
    $ showP("mara", "neutre", 0.82)

    mara "Je vais vérifier deux trucs."
    mara "Rien de grave."
    mara "Juste…"
    mara "Désolée d'avoir cassé l'ambiance."

    iris "T'inquiète. C'est pas toi qui est en cause..."

    mara "Merci."

    pause 0.4

    "Kael finit."
    "Il se lève sans faire de commentaire."

    pause 0.4

    hide kael
    hide elias
    hide mara
    hide elen
    hide julian

    $ showP("noam", "neutre", 0.82)
    $ showP("iris", "fatigue", 0.50)

    "Il reste Iris."
    "Et moi."
    "Deux secondes."

    pause 0.3

    iris fatigue "Tu vois."
    iris fatigue "Même quand personne veut en parler…"
    iris fatigue "On finit toujours par le faire.."

    noam "Ouais."
    "Je tripote ma barre de céréale. Elle s'effrite entre mes doigts."

    pause 0.3

    iris "Fais attention tout à l'heure."

    noam "Toi aussi."

    pause 0.4

    "Elle hoche la tête."
    "Et elle part."

    hide iris

    pause 0.4

    "Je reste une seconde."
    "Je regarde la salle."
    "Pleine."
    "Silencieuse."
    "Vivante quand même."

    pause 0.4

    think "Une respiration."
    think "Avant la suite."

    pause 0.4

    "Je repose mon plateau."
    "Et je me lève."

    stop music fadeout 0.8

    "Que devrais-je faire en attendant ?"

    call START_FREE_TIME("_3_PAUSE_CHAMBRE") from _call_START_FREE_TIME_3_1


label _3_PAUSE_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "Je referme la porte derrière moi."
    "La chambre retrouve son calme sec."

    pause 0.4

    think "Je reste debout."
    think "Je n’allume rien d’autre."

    pause 0.4

    think "Convaincre quelqu’un, ce n’est pas prouver qu’on a raison."

    pause 0.5

    think "C’est comprendre ce qui lui fait peur."
    think "Ce qu’il veut protéger."
    think "Ce qu’il refuse de perdre."

    pause 0.4

    think "Je l’oublie trop vite."
    think "Surtout quand je suis stressé."

    pause 0.4

    "Je m’assois sur le bord du lit."
    "Mes mains restent ouvertes sur mes genoux."

    pause 0.4

    think "Au Conclave, on parle de principes."
    think "Mais on vote avec nos nerfs."

    pause 0.4

    think "On vote avec nos histoires."
    think "Avec nos dettes."
    think "Avec nos morts."

    pause 0.4

    think "Je ne peux pas l’ignorer."

    pause 0.4

    think "Est-ce que je vote pour le système ?"
    think "Pour une architecture plus stable ?"
    think "Pour une version moins brutale des règles ?"

    pause 0.4

    think "Ou est-ce que je vote pour les gens ?"
    think "Pour ceux qui sont là, maintenant."
    think "Pour leurs visages, pas pour un schéma."

    pause 0.4

    think "Je n’ai pas la réponse nette."
    think "Et je déteste ça."

    pause 0.4

    "Je me lève, je fais deux pas, je reviens."
    "La pièce est trop petite pour tourner en rond dignement."

    pause 0.4

    think "Si je pousse un argument parfait mais froid, je perds des voix."
    think "Si je pousse une émotion pure, je perds le texte."

    pause 0.4

    think "Il faut les deux."
    think "Pas moitié-moitié."
    think "Les deux, en même temps."

    pause 0.4

    think "Clarté."
    think "Limites."
    think "Traçabilité."

    pause 0.4

    think "Je répète les trois mots comme un ancrage."

    pause 0.4

    "Un bruit dans le couloir."
    "Des pas ralentissent devant ma porte."
    "Puis repartent."

    pause 0.4

    think "Personne n’est tranquille aujourd’hui."

    pause 0.4

    think "Je revois les regards à la cafétéria."
    think "Pas d’enthousiasme."
    think "Pas de panique pure."
    think "Juste une concentration fragile."

    pause 0.4

    think "Une concentration qui peut casser au premier faux mot."

    pause 0.4

    think "Alors je dois choisir mes mots."
    think "Pas pour paraître brillant."
    think "Pour être compréhensible."

    pause 0.4

    think "Compréhensible et honnête."

    pause 0.4

    "Je prends une inspiration lente."
    "Je la retiens."
    "Je relâche."

    pause 0.4

    think "Je ne convaincrai pas tout le monde."
    think "Mais je peux éviter de braquer inutilement."

    pause 0.4

    think "Je peux écouter avant de répondre."

    pause 0.4

    think "Je peux admettre quand je ne sais pas."

    pause 0.4

    think "Je peux dire :"
    think "“Je veux que ça tienne dans la réalité.”"
    think "“Je veux que ça protège, pas que ça piège.”"

    pause 0.4

    think "Ce sera déjà mieux que réciter un slogan."

    pause 0.4

    "Je regarde la porte."
    "Encore quelques heures avant le Conclave."

    pause 0.4

    think "Encore du temps pour parler."
    think "Pour ajuster."
    think "Pour rattraper une maladresse."

    pause 0.4

    think "Pas assez de temps pour réparer une fracture."

    pause 0.4

    think "Donc pas de grand discours."
    think "Des phrases courtes."
    think "Des engagements vérifiables."

    pause 0.4

    think "Et surtout :"
    think "Ne pas confondre gagner un échange"
    think "avec construire un accord."

    pause 0.5

    "Je prends une gorgée d’eau."
    "Cette fois, mes mains tremblent moins."

    pause 0.4

    think "D’accord."
    think "Je repars."

    pause 0.4

    think "Pas besoin d’être parfait."
    think "Besoin d’être clair."

    pause 0.4

    think "Je prends la poignée."
    think "Je souffle une dernière fois."

    pause 0.4

    think "Aller au bout, maintenant."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_2


label _3_TRANSITION_CONCLAVE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Le couloir principal est éclairé plus bas que d’habitude."
    "Assez pour voir les visages."
    "Pas assez pour les détails."

    pause 0.4

    "Des groupes avancent dans la même direction."
    "Conclave."
    "Toujours le même point de convergence."

    pause 0.4

    "Personne ne fait de discours dans le trajet."
    "On garde les dernières phrases pour plus tard."

    pause 0.4

    "Une porte automatique s’ouvre devant nous."
    "Souffle d’air froid."
    "Passage étroit."

    pause 0.4

    "Je franchis le seuil."
    "Les pas résonnent légèrement."
    "Les murs répondent en écho court."

    pause 0.4

    think "Même l’acoustique semble plus sèche."

    pause 0.4

    "Elen marche un peu devant moi."
    "Elle ajuste sa manche sans lever les yeux."

    pause 0.3

    "Iris vérifie sa tablette, puis l’éteint."
    "Geste net."
    "Pas de seconde vérification."

    pause 0.3

    "Mara passe sa main dans ses cheveux et expire fort par le nez."
    "Nyra garde le menton droit."
    "Tomas compte quelque chose sur ses doigts."

    pause 0.4

    "Aucun de nous ne parle vraiment."
    "On échange des signes très courts."
    "Un regard."
    "Un hochement."

    pause 0.4

    think "Le mode solennel s’installe tout seul."

    pause 0.4

    "Deuxième série de portes."
    "Ouverture latérale."
    "Fermeture immédiate derrière le dernier."

    pause 0.4

    "Le sas diffuse une lumière blanche fixe."
    "Pas d’annonce."
    "Pas de musique d’accueil."

    pause 0.4

    think "Kami n’intervient pas encore."
    think "Et ce silence pèse plus lourd qu’un discours."

    pause 0.4

    "Nous avançons en file irrégulière."
    "Personne ne cherche à passer devant."

    pause 0.4

    "Un garçon trébuche légèrement sur une jointure au sol."
    "La personne derrière le rattrape par le coude."
    "Pas un mot."

    pause 0.4

    "On reprend le rythme."
    "Pas après pas."

    pause 0.4

    think "C’est étrange."
    think "On dirait une marche vers quelque chose de déjà écrit."

    pause 0.4

    think "Alors que, justement, on va essayer d’écrire."

    pause 0.4

    "À gauche, une baie vitrée donne sur une section technique."
    "Des câbles."
    "Des voyants verts."
    "Rien qui ressemble à une réponse."

    pause 0.4

    "À droite, des portes fermées sans signalétique."
    "Le genre de portes qu’on ne nous ouvre jamais."

    pause 0.4

    think "Aujourd’hui, seule la salle du Conclave compte."

    pause 0.4

    "Troisième porte automatique."
    "Le capteur nous détecte."
    "Un déclic sec précède l’ouverture."

    pause 0.4

    "L’air devient un peu plus chaud."
    "Plus dense aussi."

    pause 0.4

    "Quelqu’un tousse derrière moi."
    "Un seul son humain un peu trop fort."
    "Puis plus rien."

    pause 0.4

    "Nous ralentissons sans consigne."
    "Le couloir final impose son propre tempo."

    pause 0.4

    think "C’est maintenant qu’on sent la gravité de la salle."

    pause 0.4

    "Je vois les bords métalliques de l’entrée du Conclave."
    "Les lignes lumineuses bleues sont déjà actives."

    pause 0.4

    "Une personne devant moi ferme les yeux deux secondes."
    "Elle rouvre."
    "Avance."

    pause 0.4

    "Pas de voix synthétique."
    "Pas de compte à rebours."
    "Toujours pas Kami."

    pause 0.4

    think "Ce silence est volontaire."
    think "Il nous laisse seuls avec nos choix."

    pause 0.4

    "Le groupe se compacte naturellement à l’entrée."
    "Puis se redistribue."
    "Chacun trouve son passage."

    pause 0.4

    "Je sens mon rythme cardiaque monter."
    "Pas de panique."
    "Juste une alerte continue."

    pause 0.4

    think "Rester net."
    think "Rester utile."
    think "Rester honnête."

    pause 0.4

    "Dernier seuil."
    "Les portes coulissent en silence parfait."

    scene bg_conclave at adaptive_fullscreen with dissolve

    "La salle du Conclave nous attend."
    "Les sièges sont prêts."
    "Les pupitres aussi."

    pause 0.4

    "On prend place sans consigne."
    "Par habitude déjà acquise."

    pause 0.4

    "Le plafond diffuse une lumière régulière."
    "Les écrans restent noirs."

    pause 0.4

    think "Kami n’a pas encore parlé."

    pause 0.4

    think "Et c’est peut-être mieux comme ça."

    return
