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
    elen rire "Allez, juste une !"
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

    "Il s'assoit à la table auprès de nous."
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
    $ showP("elias", "reflechit", 0.82)

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

    elen "Bon vu que vous me cassez les pieds avec ça."
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

    elen "Nan nan nan ! Il faut voir le bon côté des choses !"
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

    "Kael mange."
    "Sans regarder personne."

    pause 0.3

    iris "On va pas tout régler ici."

    elias "Non."

    hide mara
    $ showP("julian", "neutre", 0.82)
    julian "Mais au moins…"
    julian "On sait que ça penche pour le “pour”."

    elen joie "Ça me suffit pour le moment."

    $ add_argument("L'énoncé précis")
    show screen argument_unlock("L'énoncé précis")

    pause 0.3

    "Elen finit une bouchée."
    "Elle pousse son bol."
    "Satisfaite, malgré tout."

    hide elen
    $ showP("elen", "content", 0.22)

    elen content "Ok."
    elen content "Je vais aller digérer mon œuvre."
    elen taquin "Et peut-être convertir d’autres âmes à ma bonne humeur."

    iris "Bonne chance."

    elen rire "Merci."
    elen rire "Hé hé, Je suis née pour ça."

    pause 0.4

    "Julian se lève aussi."

    hide julian
    $ showP("julian", "sourire", 0.82)

    julian "Je vais faire un tour aussi."

    pause 0.4

    "Elias récupère son plateau et le suit également."

    hide julian
    $ showP("mara", "neutre", 0.82)
    mara "Ouais."

    pause 0.4

    "Mara se lève à son tour."
    "Toujours sur le bord."

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

# Durée : 6m30
# Totale : 1h 34m 25s

# + 1m30 de temps libres
# Totale : 1h 36m 00s

label _3_PAUSE_CHAMBRE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    "La porte claque derrière moi."

    play sound sfx_door
    "Le choc résonne dans la cage thoracique."
    "Pas juste dans la pièce."
    "Dans moi."

    pause 0.3

    "Je reste planté là, dos au battant."
    "Pas un bruit dehors. Pas un bruit dedans."
    "Juste mon cœur qui cogne comme s'il voulait sortir avant moi."

    pause 0.3

    think "On vote pas avec des idées."
    think "On vote avec nos nerfs."

    "Je fais un pas. Puis un autre."
    "La chambre est trop petite. Ou alors c'est moi qui suis trop grand."

    pause 0.3

    think "Convaincre, c’est pas prouver qu’on a raison."
    think "C’est toucher ce que l’autre protège."
    think "Ce qu’il a déjà perdu. Ce qu’il refuse de perdre encore."

    "Je m’assois sur le bord du lit puis je me mets à réfléchir."

    pause 0.4

    think "Vaut-il mieux défendre ses principes ou les gens ?"
    think "Vaut-il mieux voter pour un texte clair ou conserver un statu quo mortel ?"
    think "Clarté. Limites. Traçabilité."

    pause 0.3

    "Je ferme les yeux une seconde."
    "Le silence pèse. Il pourrait presque écouter les battements rythmés de mon coeur.."

    pause 0.4

    play sound sfx_knock

    "Trois coups secs."
    "Rapides."

    pause 0.2

    play sound sfx_knock

    "Encore."

    pause 0.2

    nyra "Noam ! Ouvre !"

    "Je me lève."

    scene bg_dortoir at adaptive_fullscreen with fade

    $ showP("nyra", "stress", 0.65)
    $ showP("noam", "neutre", 0.20)

    nyra stress "Il est en train de faire le tour."

    noam "Qui ?"

    nyra "Julian."

    pause 0.2

    nyra "Il parle à Tomas."
    nyra "Il parle à d’autres."
    nyra "Il essaye de convaincre tout le monde de voter pour la proposition."

    noam "Comment ça ? C'est pas si grave, non ? Pourquoi tu es si remontée ?!"

    nyra "Il dit que si c’est lui qui prend la parole au Conclave, personne n’osera dire non."
    nyra "Il vend son image. Il veut juste paraitre pour celui qui fait avancer les choses."

    pause 0.3

    nyra "Il dit que le vote passera grâce à lui."

    pause 0.4

    think "Pas le texte."
    think "Lui."

    noam "Où il est ?"

    nyra "Dans la salle de repos."

    stop music fadeout 0.5
    play music "music/bgm_tension_low.mp3" fadein 0.6

    scene bg_couloir at adaptive_fullscreen,memory_idle with fade

    "On se met à courir."

    play sound sfx_run

    "Mes semelles claquent sur le métal."
    "Chaque pas renvoie un écho trop fort."
    "Trop visible."

    pause 0.3

    "Nyra est devant. Elle court sans regarder derrière."
    "Son souffle est court. Rageur."

    pause 0.2

    play sound sfx_run
    "Les néons défilent au-dessus."
    "Blanc. Blanc. Clignotant."
    "Un grésillement. Comme si les caméras tournaient plus vite."

    pause 0.3

    "Mon cœur tape dans les tempes."
    "Pas juste la course."
    "Julian. Son sourire. J'image déjà sa voix disant 'le texte passera grâce à moi'."

    pause 0.2

    "Un virage sec. Je manque de percuter le mur."
    "Nyra ralentit à peine."

    pause 0.5

    "J'entends un bruit de voix au loin."
    "C'est le sien. Son rire. Toujours ce rire."

    scene bg_repos at adaptive_fullscreen with fade

    $ showP("julian", "sourire", 0.65)
    $ showP("tomas", "hesitation", 0.35)

    julian sourire "— et si je prends la parole en premier, ça donne le ton."
    julian sourire "On a besoin d’un visage sûr."
    julian sourire "D’un leader visible. De quelqu'un en qui les gens se reconnaissent."

    tomas hesitation "Je vote pour le texte."
    tomas hesitation "Pas pour un leader."

    julian rire "Mais le texte a besoin d’un moteur."
    julian rire "Et je peux être ce moteur."

    "Je m’avance."

    $ showP("noam", "determine", 0.85)

    noam "C'est loin d'être une bonne idée."
    noam "Personne n'est leader ici."

    pause 0.4

    julian sourire "Ah."
    julian sourire "Noam."

    pause 0.2

    noam "Si tu passes ton temps à dire que ça passera grâce à toi,"
    noam "les hésitants vont se braquer."
    noam raison "Ils vont croire qu’on leur impose quelqu’un."
    noam raison "Et qu'on ne vote plus seulement pour ou contre une idée."

    pause 0.4

    julian sourire "T’es dur franchement."

    "Son sourire glisse."
    "Une seconde."
    "À peine."

    $ showP("julian", "neutre", 0.65)

    julian "Je veux juste que ça passe."

    noam "Alors parle uniquement du texte."
    noam "Et arrête d'essayer de te mettre en avant."

    pause 0.3

    tomas "Il a raison."

    $ showP("tomas", "determine", 0.35)

    tomas "Si ça ressemble à une démonstration d’ego,"
    tomas "F-Franchement, ç-ça sera sans moi."

    pause 0.4

    $ showP("julian", "decu", 0.65)

    julian "Bon. Très bien."
    "Son sourire revient. Mais il n’atteint plus les yeux."
    julian sourire "On verra au Conclave qui porte vraiment le vote."

    "Il me fixe."
    "Pas longtemps."
    "Avant de me dire d'une voix sèche."

    julian "Evide de me fais pas passer pour le méchant."

    "Il s’éloigne."

    hide julian

    pause 0.5

    stop music fadeout 0.6
    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    $ showP("nyra", "neutre", 0.60)
    $ showP("tomas", "reflechit", 0.35)

    tomas "C’était limite."
    tomas triste "Il était franchement casse pied."
    tomas mefiant "D-Désolé, à cause de moi, v-vous avez du venir m'aider..."

    nyra "T'inquiète, mais il faut surveiller cet imbécile."

    pause 0.3

    think "Julian n’est pas contre."
    think "Mais il aime être au devant de la scène."
    think "Et ça, ça peut causer des problèmes."

    pause 0.3

    tomas "P-Pour être honnête, je ne veux pas que ce soit lui qui donne le ton."
    tomas "Il faut que quelqu'un puisse lui tenir tête..."
    tomas "T-Tu vas parler tout à l'heure ?"

    noam "Oui."

    pause 0.2

    noam "Mais pas pour briller. Pour essayer que ça avance dans le bon sens."

    pause 0.4

    tomas hoche_la_tete "Alors fais simple."

    nyra "Et clair."

    "Ils repartent tous les deux en direction des autres pièces."

    pause 0.4

    hide tomas
    hide nyra

    $ showP("noam", "determine", 0.75)

    think "Ce vote, c’est plus juste un texte."
    think "C’est aussi une question de confiance."
    think "On ne peut pas faire n'importe quoi, au risque de la briser."

    pause 0.3

    think "Julian n’est pas un ennemi."
    think "Mais son caractère peut causer le pire comme le meilleur."

    pause 0.3

    "Je serre les poings."
    "Ils tremblent moins qu’avant."

    pause 0.3

    think "Les grands discours, ce n'est pas vraiment pour moi."
    think "Mais je ne peux pas laisser les choses s'envenimer."

    pause 0.3

    think "Je devrais y aller."

    call START_FREE_TIME("_3_TRANSITION_CONCLAVE") from _call_START_FREE_TIME_3_rewrite

# Durée : 2m40
# Totale : 1h 37m 05s

# + 1m30 de temps libres
# Totale : 1h 38m 35s

label _3_TRANSITION_CONCLAVE:

    scene bg_couloir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "Le couloir est plus sombre que d’habitude."
    "Il me semble bien plus étroit..."

    pause 0.3

    $ showP("noam", "inquiet", 0.5)

    think "Respire."
    think "C’est juste un vote."

    pause 0.3

    think "Pourquoi est-ce que mon cœur tape comme ça."

    "Je sens une sueur froide glisser le long de ma nuque."
    "Comme si quelqu’un me regardait de trop près."

    pause 0.3

    think "Les caméras."

    "Elles sont là."
    "Oui. Bien sûr. Pourquoi auraient-elles disparu ?"

    pause 0.3

    "Des groupes avancent."
    "Nous allons tous dans la même direction."
    "Nous partageons tous le même silence."

    pause 0.3

    "Personne ne parle."
    "On marche."

    "Pas synchronisés, obligés."
    "On a une démarche presque militaire."

    pause 0.3

    "Elias a les poings serrés."
    "Ses jointures sont blanches."

    "Julian marche un peu trop vite."
    "Il sourit toujours mais on remarque que celui-ci reste figé. Il se force sans doute."

    pause 0.3

    "Mara regarde son poignet."
    "Encore."
    "Comme si elle comptait les minutes."

    "Tomas murmure des chiffres pour lui-même."

    pause 0.3

    think "On dirait une salle d’attente."
    think "Sauf que personne ne sait ce qu’on attend exactement."

    pause 0.4

    $ showP("lysa", "neutre", 0.25)
    $ showP("noam", "inquiet", 0.75)

    "Lysa marche en retrait."

    "Pas beaucoup."
    "Mais juste assez pour que ça se voie."

    pause 0.3

    "Le couloir se resserre."
    "Le groupe accélère."

    "Elle non."

    pause 0.3

    "Elle garde le même rythme."
    "Lent."
    "Délibéré."

    pause 0.3

    "Je ralentis sans vraiment réfléchir."
    "Je me cale sur son pas."

    pause 0.3

    "Elle le sent."

    $ showP("lysa", "reflexion", 0.25)

    "Elle tourne légèrement la tête."
    "Pas de sourire."
    "Pas d’agressivité."

    "Elle a les traits du visage particulièrement fatigués."

    pause 0.3

    $ showP("lysa", "triste", 0.25)

    lysa "Ça ne changera rien."
    lysa "On va voter."
    lysa "On va échouer."

    pause 0.3

    lysa "Et demain on sera toujours là."
    lysa "Avec les mêmes murs et la même pression sur les épaules."
    lysa "Puis on recommencera dans trois jours encore..."

    pause 0.6

    "Elle ne me regarde pas, elle se parle à elle-même."
    "Elle avance."
    "Toujours au même rythme, inlassablement."

    pause 0.5

    think "Elle y croit."
    think "Vraiment."

    pause 0.3

    think "Pas à l’espoir."
    think "À l’inverse."

    pause 0.4

    $ showP("julian", "hesitation", 0.9)

    "Julian se retourne."
    "Il l'a entendu."

    "Son sourire se crispe."
    "Une seconde."
    "Il me regarde, grimace, puis il accélère."
    hide julian

    pause 0.3

    $ showP("mara", "stress", 0.5)

    "Mara serre les lèvres."
    "Elle ne répond pas."
    "Et son silence fait plus de bruit que si elle avait ri."
    hide mara

    pause 0.5

    "Le couloir devient plus lourd encore."
    "Même les néons semblent hésiter."

    pause 0.4

    think "Parmi ceux qui l'ont entendu, personne ne l'a contredit."
    think "Comment le pourrions-nous ?"
    think "Personne ne sait ce qu'il va se passer."

    "Et puis, alors qu'on arrive devant la salle, Sael prend Lysa dans ses bras."

    pause 0.3

    scene bg_cg014 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg014")

    "C’est bref."
    "Pas théâtral."
    "Pas démonstratif."

    pause 0.4

    "Juste ses bras qui se referment."
    "Solides autour de sa taille."

    pause 0.3

    "Lysa se fige."
    "Une demi-seconde, sans rien dire."
    "Comme si son corps ne savait plus quoi faire."

    pause 0.4

    sael "T’as le droit d’être fatiguée."
    sael "Mais pas d’abandonner."

    pause 0.5

    "Sa voix est basse."
    "Pas particulièrement dure ou sèche."

    pause 0.4

    sael "On a besoin de toi là-dedans."
    sael "Pas de ton cynisme, pas de cette moue."
    sael "Tu étais énergique le premier jour, on a besoin de retrouver cette Lysa là."

    pause 0.3

    sael "On a besoin de ta lucidité."

    pause 0.5

    "Les épaules de Lysa se détendent un peu."
    "À peine."

    pause 0.3

    lysa "Tu dramatises."
    lysa "Je suis toujours là."

    pause 0.4

    sael "Alors montre-le."

    pause 0.4

    "Sael la relâche."
    "Pas complètement."

    pause 0.3

    sael "T-Tu comprends les choses mieux que moi."
    sael "C’est pénible, très pénible même."
    sael "Mais c’est utile."

    pause 0.5

    "Lysa sourit légèrement."

    pause 0.3

    lysa "Si je sauve le débat, je veux que tu me payes un café."

    pause 0.3

    sael "Deux. Même si tu veux."
    sael "Ici c'est pas moi qui paye."

    pause 0.4

    "Elles se séparent."
    "La porte est juste là."

    pause 0.3

    think "Lysa redresse le menton. Elle a l'air d'avoir repris du poil de la bête."
    think "Elle ne croit peut-être pas à ce système."
    think "Mais il faut qu'elle sache qu'elle peut le changer !"

    scene bg_conclave at adaptive_fullscreen with dissolve

    "La salle est déjà éclairée."
    "Les sièges sont mis en place."
    "Les pupitres sont prêts, les caméras chargées sur nous."

    pause 0.3

    "Juste avant de franchir le seuil—"
    "Un écran mural s’allume."

    play sound sfx_announce
    pause 1.0

    scene bg_diffusion_taquin at adaptive_fullscreen with fade
    show screen kami_broadcast_ui
    play music "music/bgm_system_override.mp3" fadein 0.8

    kami "Vous voilà tous ! Manquera-t-il quelqu'un ?"
    kami "Mes chers téléspectateurs, nous le saurons dans un instant !"

    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "On voit à vos visages qu'il y a eu un peu d'émotion !"
    kami "Oh, comme c'est mignon !"

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "CAMERAMAN ! Un petit zoom sur ces visages cro-crognon !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pardonnez mon humour douteux, je suis comme vous, moi aussi je stress !"
    kami "C'est bien la première fois que j'organise ça..."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais pas d'inquiétude, asseyez-vous. On commence dans quelques instants."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with fade
    pause 0.4

    "Les portes se referment derrière nous."

    play sound sfx_door

    pause 0.5

    "On s'installe tous à nos sièges respectifs."
    "Le Conclave va commencer."
    think "Plus de retour en arrière possible."

    jump patreon_ending

# Durée : 2m55
# Totale : 1h 40m 00s

label _3_DEBAT1_PHASE1:
    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "C'est bon tout le monde est installé ?"
    kami "C'est TROOOP LOOONG !!"

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bon on va commencer cette première phase en douceur."
    kami "Vous allez devoir poser les bases."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Avant de vous arracher les cordes vocales, vous allez devoir reconstruire le texte ensemble."
    kami "Il faut que vous sachiez de quoi vous parlez non ?!."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ne faites pas les mêmes erreurs que les anciens politiciens qui ont conduit le monde à sa ruine !"

    $ bc_show("ryn", "surpris", px=-70, py=-50, pz=0.85)
    ryn "Attends comment ça reconstruire le texte ensemble ?!"
    ryn "C'est quoi ce bordel ?!"
    $ bc_hide()

    kami "Non mais attends ! Tu ne penses tout de même pas que je vais faire le travail à TA place ?!"
    kami "J'ai un monde entier à gérer, je suis très occupée moi !"

    $ bc_show("sael", "reflechit", px=-70, py=-50, pz=0.85)
    sael "Donc ça veut dire qu'on a même pas la base écrite de l'amendement ?"
    sael "Comment on va faire pour en débattre sans ça ?!"
    $ bc_hide()

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mon dieu, je savais qu'en prenant des jeunes il aurait fallu tout expliquer !"
    kami "Zen... Tu t'y étais préparée..."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Ne vous en faites pas, je sais que vous n'avez PAS de mémoire..."
    kami "Alors pour vous aider, mais pas trop, j'ai réarrangé les mots de l'amendement déposé..."
    kami "Et..."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Pour pimenter le tout j'y ai ajouté quelques mots !"
    kami "Histoire de voir vos débats !"

    $ bc_show("lysa", "colere", px=-70, py=-50, pz=0.85)
    lysa "C'était évidemment trop beau !"
    lysa "Avoir un amendement qui autorise le commerce, c'était trop simple !"
    $ bc_hide()

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Toujours en train de pleurnicher ceux là..."
    kami "Vous devriez être reconnaissants de cette possibilité de changement !"

    $ bc_show("nyra", "stress", px=-70, py=-50, pz=0.85)
    nyra "S'il vous plait, dites moi que je rêve..."
    $ bc_hide()

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bref, j'ai rentré les mots de l'amendement à archive et je les ai compilé."
    kami "Malheureusement pour vous, ils sont totalement dans le désordre."

    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Avant de pouvoir débattre de quoi que ce soit, il faudra que vous régliez ce problème..."

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'espère que vous vous rappelez vos règles de construction de phrase."

    hide screen kami_broadcast_ui

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showP("ryn", "determine", 0.18)
    ryn "Elle pouvait pas nous les donner directement dans l'ordre ?!"
    ryn "Sérieusement, pourquoi elle fait ça ?!"

    $ showP("sael", "mefiant", 0.82)
    sael "Va falloir qu'on s'y mette si on veut avancer."

    hide ryn
    $ showP("nyra", "raison", 0.50)
    nyra "Concentrez-vous sur la structure. Sujet, action, conséquence."
    nyra "Il faut faire attention à la ponctuation, ça peut nous aider à bien placer les mots."

    $ showP("noam", "raison", 0.18)
    noam "D'accord."
    noam "On reconstruit ça, puis on discutera ensuite."
    noam "J'espère que rien n'a été ajouté de dangereux."

    hide sael
    hide nyra
    hide noam

    call FA_START_ANIM from _call_FA_START_ANIM

    pause 1.0
    $ debat_phase1_setup()
    $ phase1_result = renpy.call_screen("debat_phase1_opening")
    $ phase1_ok = phase1_result.get("success", False) if phase1_result else False
    $ phase1_time_left = phase1_result.get("time_left", 0) if phase1_result else 0
    $ phase1_kamyz_gain = debat_phase1_calculate_kamyz(phase1_time_left) if phase1_ok else 0
    if phase1_ok:
        $ player_kamyz += phase1_kamyz_gain
        $ renpy.notify("+ %d Kamyz" % phase1_kamyz_gain)
        call screen noam_consent_screen

    scene bg_conclave at adaptive_fullscreen with dissolve

    $ showP("lysa", "reflexion", 0.45)
    lysa "Autoriser le transport, la vente et l'échange de marchandises ..."
    lysa "Le système actuel de distribution de denrées est aboli ?!"

    $ showP("elen", "joie", 0.28)
    elen "On l'a ! Enfin !"
    elen "Ça fait du bien d'avoir enfin une base claire."

    $ showP("tomas", "neutre", 0.82)
    kael "Parfait."
    kael "M-Maintenant le vrai débat peut commencer."

    hide elen
    hide tomas
    hide lysa

    jump _3_DEBAT1_PHASE2

# Durée : 2m35
# Totale : 1h 42m 35s

label _3_DEBAT1_PHASE2:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0

    pause 0.5

    "Le silence ne dure pas bien longtemps."

    $ showP("mara", "reflexion", 0.40)
    mara "Bon, on a le papier sous le nez. Putain, la deuxième partie… qui est le génie qui veut nous faire crever la dalle direct ?"
    "Quelques regards se croisent."

    $ showP("elen", "surpris", 0.30)
    elen "Attends."
    elen "Ça faisait partie de la proposition ?"

    $ showP("tomas", "reflechit", 0.85)
    tomas "La… la formulation est… euh… très claire."
    tomas "L’abrogation… elle est… incluse. Oui."

    hide tomas
    $ showP("nyra", "raison", 0.90)
    nyra "C’est un choix radical."
    nyra "Pas un simple ajustement."

    hide elen
    $ showP("kael", "inquiet", 0.05)
    kael "Supprimer le système de distribution…"
    kael "Ça change tout."

    hide kael
    $ showP("ryn", "desaccord", 0.15)
    ryn "Ça supprime TOUT ! La seule putain de sécurité qu’on avait !"

    "Le silence revient. Plus lourd."

    hide nyra
    $ showP("julian", "surpris", 0.75)
    julian "Attendez. Q-Quelqu'un a vraiment proposé d'abolir ça ?"
    julian "C’est pas ce que Kami avait annoncé, si ?"

    hide mara
    $ showP("iris", "panne", 0.40)
    iris "Bah ouai. Ecoute un peu."

    julian hesitation "Je—"
    julian hesitation "Je pensais qu’on parlait d’autoriser les échanges."
    julian hesitation "Pas de faire sauter tout le reste."

    hide iris
    $ showP("lysa", "reflexion", 0.60)
    lysa "Donc quelqu’un a proposé ça."

    hide julian
    $ showP("tomas", "raison", 0.85)
    tomas "Les amendements sont déposés anonymement."

    $ showP("ryn", "desaccord", 0.15)
    ryn "Comme c'est pratique..."

    hide tomas
    $ showP("nyra", "fatigue", 0.90)
    nyra "Ce n’est pas anodin."
    nyra "Supprimer une structure mondiale, ça ne s’écrit pas par accident."

    "Un malaise s’installe."

    hide nyra
    hide lysa
    $ showP("mara", "colere", 0.40)
    mara "Donc quelqu’un ici veut casser le système."
    mara "Et évidemment, il ne l’assume pas."

    $ showP("julian", "neutre", 0.75)
    julian "Pas le choix, faut en discuter et voter."
    julian "Idéalement, faut éviter de faire une chasse aux sorcières, on avancera pas."

    ryn "Facile à dire."

    hide mara
    $ showP("noam", "raison", 0.50)
    noam "Puis rien ne nous garantit que tout ça n'est pas une mascarade."
    noam "Il est aussi possible que Kami se moque totalement de nous, et que personne n'ait proposé ça."

    hide noam
    $ showP("lysa", "reflexion", 0.60)
    lysa "Oui, c'est possible."
    lysa "Et comme il n'y a que dix votes pour douze propositions, ça peut camoufler toute manipulation."

    ryn "Hein, qu'est ce que tu veux dire par là ?!"

    lysa "Réfléchis-y ..."
    lysa salut "Si les amendements qu'on vote ne sont pas de notre fait, alors aucun d'entre nous à écris celui-là."
    lysa salut "Et on doit tous se dire que le notre aura de grande chance de tomber une autre fois."
    lysa salut "Et si cette autre fois n'arrive jamais, alors on se dira tous qu'on fait parti des deux restants."

    hide ryn
    $ showP("sael", "desaccord", 0.25)
    sael "Donc c'est impossible de savoir si c'est l'un d'entre nous qui a proposé ça ?"

    lysa "Exactement, seul Kami le sait. Et la personne qui a écrit cet amendement, si elle existe..."

    "Sael prend une grande inspiration puis frappe un poing sur la table."
    sael "Bordel, qui a proposé ça ?!"

    "Les regards se croisent."
    "Chacun se regarde mais personne ne répond."

    sael "Kami, tu le sais toi. L'un d'entre nous a-t-il écrit ça ?"

    "L'écran central reste figé et Kami ne réponds pas."

    hide lysa
    $ showP("noam", "reflexion", 0.50)
    noam "Bon, pas le choix, il faut débattre du fond de la proposition."
    noam "Ne cherchons pas un coupable, c'est une perte de temps."
    noam "N'empêche y'en a un qui fait moins le malin."

    pause 0.5
    hide sael


    "Julian arbore son plus grand sourire, il a bien compris de qui je parlais."
    $ showP("julian", "sourire", 0.75)
    julian "Oh Noam. Mais ne t'en fais pas, ça ne changera pas grand chose à ma position."
    julian "Certes, cette découverte peut être perturbante, mais le commerce n'en reste pas moins absolument E-SSEN-TIEL."

    hide noam
    $ showP("lysa", "blase", 0.60)
    lysa "T’es déjà sur scène."
    lysa "Respire."

    "Quelques regards se tournent vers Julian qui commence à expliquer."

    $ showP("julian", "idee", 0.75)
    julian "Très bien."
    julian "Puisque personne ne se lance vraiment dans la discussion…"
    julian "Autoriser le transport et la vente, c’est logique."
    julian "On débloque l’économie."
    julian "On relance les districts."
    julian "On arrête de tout centraliser et on revient à ce qu'on connaissait il y a quelques années."

    hide lysa
    $ showP("mara", "rire", 0.40)
    mara "Et tu comptes faire comment, lover ?"
    mara "T’as prévu d’enthousiasmer les ventres vides ou tu vas leur refourguer ta bonne humeur au black ?"

    "Un léger rire nerveux traverse la salle."

    $ showP("julian", "determine", 0.75)
    julian "Comment on le faisait avant ?"
    julian "Un district qui produit des ressources le vendra aux autres."
    julian "Tout simplement."

    $ showP("ryn", "neutre", 0.15)
    ryn "Et qu'est ce que tu fais de ceux qui n'ont rien ?!"

    "Ryn croise les bras."

    $ showP("ryn", "desaccord", 0.15)
    ryn "Si le système actuel saute…"
    ryn "Les distributions sautent aussi."
    ryn "Et ça ça tuera de nombreuses personnes dans les districts les plus pauvres dont LIMEN."

    $ showP("julian", "hesitation", 0.75)
    julian "Pas forcément."

    ryn "Si."
    ryn "C’est écrit noir sur blanc."

    hide julian
    $ showP("tomas", "raison", 0.85)
    tomas "L’abrogation du système de distribution implique sa disparition."
    tomas "Il n’y a pas d’entre-deux, c'est factuel."

    hide tomas
    $ showP("julian", "surpris", 0.75)
    julian "On peut compenser."

    hide mara
    $ showP("lysa", "reflexion", 0.60)
    lysa "Comment tu comptes faire ça ?"
    lysa "Ce n'est même pas précisé dans l'amendement."

    $ showP("julian", "rire", 0.75)
    julian "C’est fou."
    julian "Dès qu’on parle d’ouverture, vous imaginez l’apocalypse."

    hide lysa
    $ showP("mara", "agace", 0.40)
    mara "Ouais non, j’ai pas envie de ramasser des macchabées parce que Monsieur Idéal a eu une illumination de start-upper."

    hide mara
    $ showP("elen", "inquiet", 0.30)
    elen "Mais attendez ! Ça va être génial !"
    elen "Les trucs vont circuler partout, on pourra enfin CHOISIR ce qu’on veut !"
    elen "C’est pas ça, la liberté ?!"

    hide julian
    $ showP("nyra", "raison", 0.90)
    nyra "Ça dépend de qui pourra les acheter."
    nyra "A Orbite, on a pas de ressources propres..."

    hide ryn
    $ showP("kael", "inquiet", 0.05)
    kael "Alors oui et non..."
    kael "Si on ne produit pas beaucoup de ressources, on en exploite quand même dans l'espace."
    kael "Simplement ces matériaux là ne restent pas bien longtemps chez nous, on les exporte rapidement."

    hide nyra
    $ showP("iris", "hesitation", 0.70)
    iris "Et…"
    iris "Si ça relançait aussi les trafics ?"

    "L’atmosphère se fige légèrement."

    hide kael
    $ showP("ryn", "colere", 0.15)
    ryn "Exact. Actuellement la frontière est fermée, seuls ceux qui ont une autorisation spéciale peuvent passer."
    ryn "Même si on ne peut pas passer, les matériaux peuvent passer sans soucis."
    ryn "Et si les distributions sautent comment feront les plus pauvres pour s'acheter quelque chose ?"

    hide iris
    $ showP("julian", "reflexion", 0.75)
    julian "En vendant aussi."

    ryn "Vendre QUOI, Julian ?! Leurs godasses trouées ? Leur fierté en solde ?!"

    julian "Leur travail, leur ressource."
    julian "Ne me fais pas croire un instant qu'il n'y a pas de travail à Limen !"

    ryn "Si, évidemment qu'il y en a..."

    julian "Et pourquoi les gens ne travaillent pas ?!"

    ryn "Parce que ça change QUE DALLE !"
    ryn "Tu travailles."
    ryn "Tu te crèves le cul douze heures, tu touches le même ticket pourri que le mec qui dort toute la journée."
    ryn "C’est ça ta motivation, toi ?!"

    $ showP("lysa", "reflexion", 0.60)
    lysa "Oui, c'est pareil dans tous les districts..."
    lysa "Comme on a les bons de rationnement et l'interdiction de faire du commerce, le travail est devenu accessoire."
    lysa "On ne travaille que si on le souhaite ou si on en reçoit l'ordre de Kami."

    "Julian relève la tête."

    julian "Au moins l'une d'entre vous a compris ou je voulais en venir."

    lysa "Mais là tu joues au héros."
    lysa "Sans plan."

    $ showP("julian", "determine", 0.75)
    julian "Quelqu’un doit faire avancer les choses."

    hide lysa
    $ showP("noam", "raison", 0.50)
    noam "Avancer, oui."
    noam "Mais pas en sautant dans le vide sans savoir où on va."

    "Plusieurs têtes hochent légèrement."

    noam "On ne vote pas une idée."
    noam "On vote pour un système qui peut impacter les gens jusque dans leur quotidien."

    julian "Et le système actuel fonctionne ?"

    $ showP("mara", "reflexion", 0.40)
    mara "..."

    julian "Il nous étouffe."

    ryn "Il nous nourrit aussi."

    julian "En nous rationnant, en nous empêchant de manger ce qu'on veut, en nous distribuant du pain rassi, en nous obligeant à réclamer tout et n'importe quoi !"
    julian colere "Mais réveillez-vous ! Vous voulez garder ce monde là ?!"

    pause 0.4
    show screen kami_broadcast_ui

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "On me dit dans l'oreillette que vous êtes ennuyants !!"
    kami "Tout ça, vos blabla, ça n'avance pas !"
    kami "Je suis obligée de prendre les choses en main."

    "A ce moment là les bureaux devant nous changent de forme."
    "Un micro sort d'un petit emplacement dédié, un buzzer apparait."

    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve

    kami "A partir de maintenant vous n'avez plus la parole."
    kami "Vous parlerez à tour de rôle. Histoire qu'on puisse vous entendre."
    kami "Devant vous, il y a un buzzer, si vous voulez contredire un propos d'un de vos camarades, vous pouvez appuyer dessus."
    kami "Et vous ne parlerez que lorsque votre buzzer s'allumera d'une couleur verte !"

    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Compris ?!"
    kami "Alors c'est parti !"

    call debat_phase2_minigame from _call_debat_phase2_minigame

    kami "Je vois que le minijeu est terminé !"
    kami "AHURISSANT !"

    jump _3_DEBAT1_PHASE3

# Durée : 6m05
# Totale : 1h 48m 40s
init -1:
    transform p3_arg_button_idle:
        alpha 0.92
        zoom 1.0
    transform p3_arg_button_hover:
        alpha 1.0
        zoom 1.04
    transform p3_arg_glow:
        alpha 0.35
        linear 0.6 alpha 0.75
        linear 0.6 alpha 0.35
        repeat
    transform p3_arg_float:
        yoffset 0
        linear 1.2 yoffset -6
        linear 1.2 yoffset 0
        repeat

screen argument_menu_ui(options, prompt="Choisis l'argument à projeter."):
    modal True
    zorder 250

    add Solid("#050a12d9")
    add Solid("#2be1ff22") at p3_arg_glow

    frame:
        background Frame(Solid("#0e1626f2"), 20, 20)
        xalign 0.5
        yalign 0.5
        xsize 1620
        ysize 820
        padding (40, 35)

        vbox:
            spacing 28
            xfill True

            text "INTERVENTION STRATÉGIQUE" size 52 color "#7be7ff" xalign 0.5
            text "[prompt]" size 30 color "#d5f7ff" xalign 0.5 text_align 0.5

            hbox:
                spacing 26
                xalign 0.5

                for i, opt in enumerate(options):
                    fixed:
                        xsize 490
                        ysize 560
                        at p3_arg_float

                        add Frame(Solid("#0d2037d0"), 14, 14) xpos 0 ypos 0 xsize 490 ysize 560
                        add Solid("#61f0ff15") at p3_arg_glow

                        imagebutton:
                            idle Solid("#142b49a0")
                            hover Solid("#1d3f67c5")
                            at p3_arg_button_idle
                            xalign 0.5
                            yalign 0.5
                            xsize 460
                            ysize 530
                            action Return(i)

                        vbox:
                            xalign 0.5
                            yalign 0.48
                            spacing 18
                            xmaximum 410

                            text "[opt['icon']]" size 74 xalign 0.5
                            text "[opt['title']]" size 33 color "#9deeff" xalign 0.5 text_align 0.5
                            text "[opt['desc']]" size 25 color "#e6f6ff" xalign 0.5 text_align 0.5

            text "L'impact dépend du moment et des tensions déjà installées." size 24 color "#86bdd0" xalign 0.5

label _3_DEBAT1_PHASE3:

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_phase3.mp3" fadein 1.0
    show screen kami_broadcast_ui

    $ p3_args_source = globals().get("collected_args", None)
    if p3_args_source is None:
        $ p3_args_source = globals().get("arguments", [])
    if p3_args_source is None:
        $ p3_args_source = []

    python:
        unlocked_set = set(p3_args_source)
        allowed_args_order = [
            "Bons de rationnement",
            "Difficulté d'approvisionnement",
            "Faiblesse d'Orbite",
            "L'énoncé précis",
            "Le monde d'avant",
            "Échanges discrets déjà actifs",
        ]
        p3_all_args = [a for a in allowed_args_order if a in unlocked_set]
        if not p3_all_args:
            p3_all_args = ["Bons de rationnement"]

        p3_cycle = p3_all_args[:]
        while len(p3_cycle) < 15:
            p3_cycle.extend(p3_all_args)
        p3_cycle = p3_cycle[:15]
        store.p3_round_options = []
        for ridx in range(5):
            triplet = p3_cycle[ridx * 3:(ridx + 1) * 3]
            card = []
            for a in triplet:
                low = a.lower()
                if "ration" in low:
                    icon = "⌬"
                    desc = "Sécurité minimale contre la faim et le chaos."
                elif "orbite" in low:
                    icon = "◉"
                    desc = "Dépendance logistique et fragilité structurelle."
                elif "énoncé" in low or "precis" in low:
                    icon = "⟡"
                    desc = "Texte exact, conséquences juridiques immédiates."
                elif "appro" in low:
                    icon = "⬢"
                    desc = "Ruptures passées et files de pénurie."
                elif "échange" in low or "discret" in low:
                    icon = "◌"
                    desc = "Réseaux d'entraide clandestins déjà en place."
                elif "avant" in low:
                    icon = "✦"
                    desc = "Mémoire d'un système ancien imparfait mais vivant."
                card.append({"title": a, "desc": desc, "icon": icon})
            store.p3_round_options.append(card)

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 0.6

    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve

    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    kami "Oh bordel, regardez-moi ces têtes de défunts…"
    kami "Jusque là c’était mignon : entre Julian qui se branle l’ego en public, Ryn qui hurle comme une veuve éplorée..."
    kami "...et tout le monde qui cherche le coupable sans oser se regarder dans les yeux."
    kami "Mais là, on passe aux choses sérieuses, mes chéris."
    kami "Question du jour, et je veux du sang : si on coupe les distributions, qui va gérer la famine à Limen ?"
    kami "Et surtout… pourquoi le petit peuple irait se lever le cul le matin si y’a plus de carotte au bout du bâton ?"
    kami "Allez, montrez-moi que vous valez plus que des rations périmées. Je m’ennuie déjà."

    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui

    $ showP("noam", "raison", 0.50)  # centre
    noam "On va essayer de rester civilisés, si c’est possible."

    $ showP("julian", "determine", 0.88)  # droite
    julian "Civilisés ? On est en train de crever doucement, Noam."
    julian "Le statu quo, c’est une tombe collective avec des bons de pain rassis."

    $ showP("ryn", "colere", 0.12)  # gauche
    ryn "Et ton 'choc salvateur', c’est quoi ? On sacrifie Limen pour que tes potes d’Orbite se payent des putes en or ?"

    julian surpris "D'orbite ?!"
    julian rire "Mais je viens de Nexus moi ! Faut suivre hein !"

    ryn "Ah... Euh oui..."
    ryn jaloux "C'est pareil façon !"

    hide noam
    $ showP("mara", "agace", 0.50)  # centre
    mara "Oh ça va, Ryn, calme tes hormones."
    mara "Mais il a pas tort : si on ouvre tout, c’est qui qui va se faire démonter en premier ? Les ventres vides ou les queues molles ?"

    hide ryn
    $ showP("kael", "culpabilite", 0.12)  # gauche
    kael "Je… je sais pas. Peut-être qu’on pourrait garder un filet minimal ?"
    kael "Juste le temps de… de voir si ça marche ?"

    hide julian
    $ showP("elen", "joie", 0.88)  # droite
    elen "Mais c’est ça qui est génial !"
    elen "On va enfin pouvoir choisir ce qu’on mange, ce qu’on fait, sans demander la permission à une IA sadique !"

    hide mara
    $ showP("lysa", "blase", 0.50)  # centre
    lysa "Choisir avec quel argent, Elen ?"
    lysa "T’as déjà vu un ticket de ration se transformer en crédit inter-districts par magie ?"

    hide kael
    $ showP("iris", "desaccord", 0.12)  # gauche
    iris "Pff… évidemment que non."
    iris "Et pendant qu’on rêve de liberté, les trafiquants se frottent déjà les mains. Bande de naïfs."

    hide elen
    $ showP("tomas", "hesitation", 0.88)  # droite
    tomas "Euh… les chiffres des trois derniers cycles…"
    tomas "…montrent une chute de productivité de vingt-sept pour cent dans les zones très assistées."
    tomas "C’est… c’est pas rien, hein ?"

    hide lysa
    $ showP("nyra", "raison", 0.50)  # centre
    nyra "Les chiffres, c’est bien joli, Tomas."
    nyra "Mais le texte de l’amendement ne parle ni de filet de sécurité, ni de transition, ni de rien."
    nyra "C’est un couperet. Pas une réforme."

    hide iris
    $ showP("sael", "mefiant", 0.12)  # gauche
    sael "…"

    sael "Quelqu’un ici sait déjà comment ça finit."
    sael "Et ce quelqu’un sourit."

    "Un silence lourd tombe. Tous les regards se tournent lentement vers l’écran central."

    show screen kami_broadcast_ui
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "Oh ? Déjà la parano ? J’adore."
    kami "Je vous rappelle que cet amendement est le fruit de VOTRE imagination !"
    kami "Continuez, mes petits rats de laboratoire."
    kami "Oooh ! J'adore le drama ! Je fais plus d'audimat !"

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[0], prompt="Moment 1 — Cadrer la première salve.")
    call _3_DEBAT1_PHASE3_INT1

    stop music fadeout 1.0
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.5

    pause 0.8

    $ showP("nyra", "raison", 0.50)  # centre
    nyra "On tourne en rond."
    nyra "Les buzzers ont servi à rien. On est toujours au même point."

    $ showP("elias", "determine", 0.88)  # droite
    elias "Parce qu’on évite les vraies questions."
    elias "On sait tous que ça peut pas continuer comme ça."

    $ showP("sael", "mefiant", 0.12)  # gauche
    sael "…"

    sael "On sait tous où ça mène."
    sael "Mais personne veut le dire."

    hide elias
    $ showP("lysa", "blase", 0.88)  # droite
    lysa "On a trois problèmes qui reviennent en boucle."
    lysa "Et on fait semblant qu’ils sont séparés."

    hide sael
    $ showP("noam", "reflexion", 0.12)  # gauche
    noam "Le passé, le texte brut de l’amendement, et la réalité des rayons vides."
    noam "On peut pas parler de tout en même temps."

    hide nyra
    $ showP("elen", "joie", 0.50)  # centre
    elen "Mais il faut bien commencer quelque part !"
    elen "Sinon on va encore tourner en rond jusqu’à demain !"

    hide lysa
    $ showP("nyra", "sourire", 0.88)  # droite – retour
    nyra "Alors choisissez un angle."
    nyra "Et on creuse. Pour de vrai, cette fois."

    hide noam
    $ showP("sael", "mefiant", 0.12)  # gauche – retour
    sael "Un seul."
    sael "Le reste attendra."

    "La salle se tait. Tous attendent que quelqu’un – ou quelque chose – tranche."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[1], prompt="Moment 2 — Désamorcer ou accélérer la fracture.")
    call _3_DEBAT1_PHASE3_INT2

    $ showP("iris", "hesitation", 0.66)
    iris "Je pose un truc simple."
    iris "Qui contrôle les routes contrôle les prix."
    iris "Et qui contrôle les prix contrôle les gens."

    $ showP("nyra", "fatigue", 0.77)
    nyra "C'est pour ça qu'un basculement brutal est dangereux politiquement."

    $ showP("sael", "desaccord", 0.93)
    sael "Dangereux pour qui ?"

    nyra "Pour ceux qui ne peuvent pas négocier."

    $ showP("kael", "inquiet", 0.19)
    kael "Les exportations peuvent financer une caisse d'urgence inter-districts..."
    kael "Si on sanctuarise une part fixe."

    $ showP("mara", "colere", 0.29)
    mara "Encore un 'si'. Vous me vendez des 'si' depuis une heure."

    $ showP("elias", "determine", 0.40)
    elias "On peut aussi choisir d'écrire les garde-fous après le vote d'orientation."
    elias "C'est pas idéal, mais c'est faisable."

    $ showP("noam", "raison", 0.50)
    noam "Sauf que l'amendement qu'on juge n'a pas ces garde-fous."

    play sound "sound/sfx_table_hit.ogg"
    ryn "Voilà. Merci."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[2], prompt="Moment 3 — Appuyer sur la légalité ou sur l'élan.")
    call _3_DEBAT1_PHASE3_INT3

    $ showP("julian", "determine", 0.88)
    julian "Si on refuse chaque pas parce qu'il n'est pas parfait, on reste au point mort à vie."

    $ showP("ryn", "colere", 0.08)
    ryn "Et si on signe n'importe quoi, on condamne les mêmes qu'on prétend sauver."

    $ showP("mara", "reflexion", 0.29)
    mara "Je déteste le système actuel."
    mara "Mais je déteste encore plus l'idée de voir des gamins troquer leur ration contre une promesse."

    $ showP("elen", "determine", 0.33)
    elen "On peut imaginer un marché libre avec une base garantie !"

    $ showP("lysa", "reflexion", 0.77)
    lysa "On peut surtout constater que ce n'est pas ce qu'on vote."

    $ showP("tomas", "raison", 0.62)
    tomas "J'ajoute un fait : lors de la suspension partielle des circuits centraux au cycle 318,"
    tomas "les incidents de sécurité sur les axes secondaires ont doublé en dix jours."

    $ showP("iris", "panne", 0.66)
    iris "Merci. Voilà pourquoi je râle."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[3], prompt="Moment 4 — Fixer la peur ou relancer l'audace.")
    call _3_DEBAT1_PHASE3_INT4

    $ showP("sael", "raison", 0.93)
    sael "Il y a une question qu'on évite."
    sael "L'auteur anonyme voulait-il réformer..."
    sael "...ou provoquer une panique pour discréditer le commerce ?"

    $ showP("nyra", "taquin", 0.77)
    nyra "Les deux sont compatibles."

    $ showP("noam", "hesitation", 0.50)
    noam "Donc on tranche sur le texte, pas sur l'intention."

    $ showP("elias", "neutre", 0.40)
    elias "Je reste convaincu que fermer encore n'est plus une option."

    $ showP("kael", "hesitation", 0.19)
    kael "Je... je veux ouvrir, mais pas comme ça."

    $ showP("mara", "doute", 0.29)
    mara "Pareil."

    $ showP("julian", "reflexion", 0.88)
    julian "Alors on envoie quel signal ?"
    julian "Qu'on accepte de pourrir doucement ?"

    $ showP("ryn", "neutre", 0.08)
    ryn "Qu'on refuse de sacrifier les plus bas sur l'autel d'un pari."

    play sound "sound/sfx_argument_impact.ogg"
    $ p3_pick = renpy.call_screen("argument_menu_ui", options=p3_round_options[4], prompt="Moment 5 — Dernière impulsion avant la coupure.")
    call _3_DEBAT1_PHASE3_INT5

    pause 0.4
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play sound "sound/sfx_table_hit.ogg"
    kami "Oh, merveilleux. Vous avez presque réussi à penser en groupe pendant plus de trois minutes."

    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Phase 4, maintenant : compromis impossible, alliances opportunistes, et peut-être un aveu."
    kami "Restez assis. Les chaises sont verrouillées."

    hide screen kami_broadcast_ui

    jump _3_DEBAT1_PHASE4

label _3_DEBAT1_PHASE3_INT1:
    $ selected = p3_round_options[0][p3_pick]["title"]
    
    if "appro" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve
        $ showP("noam", "reflexion", 0.50)  # centre
        noam "Attends. Même avec les bons actuels… on trouve quoi sur les rayons ?"
        noam "Des fruits frais ? Des médocs qui marchent ? Des pièces pour réparer une pompe ?"

        $ showP("julian", "idee", 0.88)  # droite
        julian "Rien ! C’est du vent, Noam."
        julian "Ouvrir le commerce, c’est remplir les rayons. Point."

        $ showP("mara", "agace", 0.12)  # gauche
        mara "Ouais, super Julian. Et les districts qui produisent que dalle ?"
        mara "Ils vendent leur cul pour une patate ou ils crèvent la dalle en silence ?"

        hide noam
        $ showP("ryn", "colere", 0.50)  # centre – remplace Noam
        ryn "Exactement !"
        ryn "À Limen, on a déjà des bons qui servent à rien. Tu crois que le marché va soudain nous livrer en priorité ?"

        hide julian
        $ showP("kael", "reflechit", 0.88)  # droite
        kael "Pour le coup... C'est bien possible."
        kael "C'est à Limen qu'il y a le plus d'habitants, donc le plus de gens prêts à acheter des choses."

        hide mara
        $ showP("lysa", "blase", 0.12)  # gauche
        lysa "Pour ça encore faut-il que les gens aient de l'argent."
        lysa "Puis on est pas à l'abri du traditionnel 'on exporte ailleurs, c’est plus rentable'..."

        hide ryn
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Pff. Les prix vont exploser. Les pauvres regarderont les rayons pleins depuis dehors."
        iris "Comme d’habitude quoi."

        hide kael
        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais imagine ! Des épices, des vrais vêtements… on pourra enfin choisir !"

        hide lysa
        $ showP("sael", "mefiant", 0.12)  # gauche
        sael "C'est ce monde qui nous empêche de choisir…"
        sael "Rien ne nous empêche de fabriquer ce dont on a besoin."

        # Modifs adhésion légères et nuancées
        $ debat_day3_apply_influence({"julian": 2, "ryn": 1, "mara": -1, "kael": 1, "lysa": 1, "elen": 2})

        hide sael
        hide elen 
        hide iris

    if "ration" in selected.lower() or "choix" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("noam", "reflexion", 0.50)  # centre
        noam "On dit que les bons permettent d’avoir beaucoup de choses…"
        noam "Mais en vrai, combien de produits sont réellement disponibles ?"

        $ showP("nyra", "raison", 0.88)  # droite
        nyra "Beaucoup sur le papier. Très peu en vrai."
        nyra "Les bons donnent droit à des trucs standards. Pas à du choix."

        $ showP("tomas", "hesitation", 0.12)  # gauche
        tomas "Euh… les rapports indiquent souvent que 62 %% des références listées…"
        tomas "…sont en rupture permanente dans les zones périphériques."
        tomas "C’est… c’est pas juste un chiffre, hein ?"

        hide noam
        $ showP("mara", "agace", 0.50)  # centre
        mara "Ouais, on a le choix entre du pain sec et du pain sec et moisi."
        mara "Et si t’as envie d’un truc qui te fait bander les papilles, bah bonne chance."

        hide nyra
        $ showP("iris", "desaccord", 0.88)  # droite
        iris "Pff. Et quand y’a un truc sympa, il disparaît en deux jours."
        iris "Parce que y'a toujours un chanceux qui tombe sur la seule brioche de la décénnie, ouais."

        hide tomas
        $ showP("ryn", "colere", 0.12)  # gauche
        ryn "C’est pas juste une question de goût !"
        ryn "À Limen, on a des bons pour du lait… qui arrive caillé la moitié du temps."
        ryn "Ou des médocs qui périment avant d’arriver. C’est ça votre 'nombreuses choses' ?"

        hide mara
        $ showP("elen", "joie", 0.50)  # centre – elle entre pour contrer
        elen "Mais justement ! Si on ouvre, on aura plus de fournisseurs !"
        elen "Plus de concurrence ; plus de choix, non ?!"

        hide iris
        $ showP("noam", "raison", 0.88)  # droite – retour
        noam "En théorie, oui. Mais en pratique…"
        noam "Les fournisseurs iront là où il y a du pouvoir d’achat."
        noam "Et Limen n’en a pas beaucoup."

        hide ryn
        $ showP("elias", "determine", 0.12)  # gauche
        elias "C’est pour ça qu’il faut que ça change."
        elias "Avec le commerce, même Limen pourra produire et vendre quelque chose."
        elias "Du travail, des échanges locaux… ça crée du pouvoir d’achat petit à petit."
        elias "On peut pas rester bloqués dans ce système où tout le monde a le même ticket pour rien."

        # Modifs adhésion
        $ debat_day3_apply_influence({
            "julian": 1,      # aime l'idée de choix via commerce
            "ryn": 2,        # voit l'échec actuel comme preuve contre le changement
            "mara": 1,       # agacée par l'idéalisme
            "noam": 1,        # pragmatique, voit le potentiel mais reste prudent
            "nyra": 1,        # politique, apprécie la nuance sur le pouvoir d'achat
            "tomas": 1,       # factuel, les chiffres le font pencher vers le changement
            "iris": 1,       # râleuse, reste sceptique
            "elen": 1         # enthousiaste, adore l'idée de choix
        })

        hide elen
        hide noam
        hide elias

        return

    if "orbite" in selected.lower():

        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("nyra", "raison", 0.50)  # centre
        nyra "On parle beaucoup de Limen ces derniers temps."
        nyra "Mais Orbite… on n’en parle jamais vraiment."
        nyra "Là-haut, les règles ne sont pas négociables."

        $ showP("kael", "mefiant", 0.88)  # droite
        kael "Ouais… c’est pas comme chez vous."
        kael "Un écart, et c’est fini. Pour tout le monde autour."
        kael triste "On peut pas se permettre des… imprévus."

        $ showP("noam", "reflexion", 0.12)  # gauche
        noam "C’est pour ça que le système actuel tient Orbite entre ses griffes ?"
        noam "Tu m'en avais rapidement parlé. Tout le monde sait à quoi s’en tenir."

        hide nyra
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Pff. Donc si on change les règles, ça ne vous arrange pas ?"
        iris "Et après on s’étonne que ça parte en vrille là-haut."

        hide kael
        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais peut-être qu’avec plus d’échanges, Orbite pourrait importer ce qu’il manque !"
        elen "Plus de stabilité, plus de ressources…"

        hide noam
        $ showP("tomas", "hesitation", 0.12)  # gauche
        tomas "Euh… en théorie, oui."
        tomas "Mais p-paradoxalement c'est sur Orbite qu'il y a le m-moins de morts chaque année."

        hide iris
        $ showP("julian", "determine", 0.50)  # centre
        julian "En autorisant le commerce, on ne met pas en cause la viabilité d'Orbite !"
        julian "Au contraire : on ouvre les possibles ! Ce n'est pas comme si on créait une nouvelle interdiction !"

        hide elen
        $ showP("lysa", "blase", 0.88)  # droite
        lysa "Et s'il y a la moindre chose qu'on ne contrôle pas, tout peut pêter."
        lysa "Et Nyra et Kael le savent mieux que quiconque."

        hide tomas
        $ showP("nyra", "stress", 0.12)  # gauche – retour
        nyra "On n’est pas contre le progrès, hein."
        nyra "On est contre le risque de perdre le contrôle."
        nyra triste "Et sur Orbite, le risque, on le paie cash. Tout de suite."

        "Nyra et Kael échangent un regard bref, tendu. Personne n’insiste."

        # Modifs adhésion – pénalisantes pour le changement
        $ debat_day3_apply_influence({
            "julian": -2,     # idéaliste mais bloqué par la réalité d'Orbite
            "noam": 1,        # pragmatique, penche pour la stabilité
            "nyra": -2,        # manipulatrice, utilise Orbite comme argument massue
            "kael": -2,        # culpabilisé, terrifié
            "tomas": 1,       # factuel, chiffres le font pencher anti-changement
            "iris": -1,        # râleuse, horrifiée par le risque
            "elen": -1,       # enthousiaste mais remise en question
            "lysa": -1         # blasée, voit le pragmatisme anti
        })

        hide nyra
        hide lysa
        hide julian

    return

label _3_DEBAT1_PHASE3_INT2:
    $ selected = p3_round_options[1][p3_pick]["title"]

    scene bg_conclave at adaptive_fullscreen with dissolve

    if "avant" in selected.lower():
        $ showP("iris", "desaccord", 0.50)  # centre
        iris "Pff… le monde d’avant ?"
        iris "Vous parlez comme si c’était le paradis perdu."
        iris "Moi je m’en souviens : files interminables, prix qui doublaient sans raison…"

        $ showP("elen", "joie", 0.88)  # droite
        elen "Mais au moins on pouvait choisir !"
        elen "Tu voulais des chaussures neuves ? Tu bossais, tu achetais !"
        elen "Pas besoin d’attendre que Kami décide que t’as droit à des semelles usées !"

        $ showP("mara", "reflexion", 0.12)  # gauche
        mara "Choisir…"
        mara "C’est un beau mot, Elen."
        mara "Moi je me souviens surtout des sourires obligatoires."
        mara "Des regards qui comptent chaque faux pas."
        mara "Et des portes qui se ferment si tu n’es pas… parfaite."
        mara "Mais bon… les robes étaient jolies."

        hide iris
        $ showP("julian", "determine", 0.50)  # centre
        julian "C’était pas parfait, OK ?"
        julian "Mais c’était vivant."
        julian "Les gens bossaient, inventaient, échangeaient. Il y avait du mouvement."
        julian "Aujourd’hui on est tous assis sur le même banc pourri, à attendre la même miette."

        hide mara
        $ showP("tomas", "hesitation", 0.88)  # droite
        tomas "Euh… avant Kami, c’était surtout la guerre qui foutait le bordel."
        tomas "Tous les matériaux, la nourriture, les pièces… réquisitionnés pour l’effort de guerre."
        tomas "C’est pour ça que les prix explosaient et que les rayons se vidaient."
        tomas "Maintenant la guerre est interdite… donc techniquement, ça pourrait mieux tourner."

        hide julian
        $ showP("noam", "raison", 0.12)  # gauche
        noam "Le monde d’avant avait de la liberté pour ceux qui avaient déjà les moyens."
        noam "Pour les autres, c’était la loi de la jungle : les riches achetaient tout, les pauvres regardaient."
        noam "On a mis les bons et la distribution pour arrêter ça."

        hide tomas
        $ showP("elen", "joie", 0.88)  # droite – retour
        elen "Mais on peut garder le meilleur !"
        elen "La distribution pour les essentiels, et la liberté pour le reste !"
        elen "Comme avant, mais sans la guerre !"

        hide noam
        $ showP("mara", "colere", 0.50)  # centre – retour
        mara "Sans la guerre, peut-être."
        mara "Mais sans les chaînes aussi ?"
        mara "Tu crois que la liberté vient sans prix à payer ?"
        mara "Moi j’ai payé cher pour le découvrir."

        hide elen
        $ showP("iris", "desaccord", 0.88)  # droite – retour
        iris "Pff. Et maintenant c’est juste ?"
        iris "Au moins c’est égal. Tout le monde crève pareil."

        "Un silence amer s’installe. Mara détourne le regard, comme si elle regrettait déjà d’avoir parlé."

        # Modifs adhésion – Mara ambivalente : nostalgique mais blessée → léger malus au changement pur
        $ debat_day3_apply_influence({
            "julian": 1,      # adore le retour à la liberté/vie
            "elen": 2,        # enthousiaste, rêve du "mieux"
            "mara": -1,       # nostalgique de la richesse mais traumatisée par les obligations (teasé subtilement)
            "iris": 1,       # râleuse, sceptique
            "tomas": 1       # factuel, voit que sans guerre ça pourrait marcher
        })

        hide iris
        hide mara

    elif "énoncé" in selected.lower():
        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("ryn", "colere", 0.50)  # centre
        ryn "Le texte est clair comme de l’eau de roche !"
        ryn "Suppression des bons. Fin de la distribution. Point barre !"
        ryn "Pas de 'peut-être', pas de 'minimum vital'. Rien !"

        $ showP("elias", "determine", 0.88)  # droite
        elias "Et c’est ça qui libère !"
        elias "Fin des bons, ça veut dire qu'on coupe la laisse de Kami."
        elias "On marchande, on échange, on vit enfin !"

        hide ryn
        $ showP("noam", "raison", 0.50)  # centre
        noam "Le texte est binaire."
        noam "POUR : suppression totale, liberté marchande immédiate."
        noam "CONTRE : on garde tout tel quel."
        noam "Y a pas d’entre-deux écrit. Pas de négociation possible."

        hide elias
        $ showP("kael", "triste", 0.88)  # droite
        kael "Mais… on pourrait pas… juste…"

        $ showP("lysa", "blase", 0.12)  # gauche
        lysa "Interpréter ?"
        lysa "Le texte dit suppression. Pas 'réduction'. Pas 'adaptation'."
        lysa "C’est tout ou rien."

        hide kael
        $ showP("elias", "determine", 0.88)  # droite – reste
        elias "C’est tout ou rien qui nous sauvera !"
        elias "On arrête de mendier des miettes. On produit. On vend. On survit ! Merde !"

        hide noam
        $ showP("ryn", "colere", 0.50)  # centre – retour
        ryn "Survivre ?!"
        ryn "À Limen sans bons, on meurt en silence pendant que vous 'produisez' vos rêves !"
        ryn "Le texte condamne les faibles. C’est écrit noir sur blanc !"

        hide elias
        $ showP("sael", "mefiant", 0.88)  # droite – retour
        sael "Condamne ?"
        sael "Ou délivre ?"

        "Ryn frappe du poing. Sael ne cille pas. La salle retient son souffle."

        # Modifs adhésion : positif = POUR suppression / changement ; négatif = CONTRE
        $ debat_day3_apply_influence({
            "ryn": -2,        # violemment contre (condamnation Limen)
            "kael": -1,       # indécis, terrifié par l’absence d’entre-deux
            "elias": 1,       # déterminé, voit la fin de la dépendance
            "lysa": -1,       # blasée, pointe la cruauté immédiate
            "sael": 2         # très favorable : voit la suppression comme délivrance/force vitale
        })

        hide ryn
        hide sael

    elif "échange" in selected.lower() or "discret" in selected.lower():
        scene bg_conclave at adaptive_fullscreen with dissolve

        $ showP("nyra", "raison", 0.50)
        nyra "Les échanges discrets existent déjà."
        nyra "Couper les bons d'un coup, c'est forcer tout le monde à passer par des réseaux opaques."

        $ showP("sael", "mefiant", 0.88)
        sael "Opaques, oui. Mais efficaces."
        sael "Quand les canaux officiels lâchent, c'est ça qui fait tenir les quartiers."

        hide nyra
        $ showP("noam", "reflexion", 0.50)
        noam "Efficaces pour ceux qui ont un contact."
        noam "Pour les autres, c'est juste une file d'attente de plus, sans recours."

        hide sael
        $ showP("mara", "agace", 0.88)
        mara "Et ça crée des chefs de couloir."
        mara "Les 'discrets' deviennent vite des péages."

        $ showP("julian", "determine", 0.12)
        julian "Ou des preuves que les gens savent déjà s'organiser sans Kami."

        "La salle hésite : survivre par les marges, ou refuser d'en faire la règle."

        $ debat_day3_apply_influence({
            "nyra": -1,
            "noam": -1,
            "mara": -1,
            "sael": 1,
            "julian": 1
        })

        hide mara
        hide julian

    return

label _3_DEBAT1_PHASE3_INT3:
    $ selected = p3_round_options[2][p3_pick]["title"]
    if "énoncé" in selected.lower():
        $ pnj_adhesion["julian"] -= 2
        $ showP("tomas", "raison", 0.62)
        tomas "Le texte prévaut."
        $ showP("julian", "agace", 0.88)
        julian "Le texte peut être amendé ensuite."
    elif "faiblesse" in selected.lower() or "orbite" in selected.lower():
        $ pnj_adhesion["julian"] -= 1
        $ p3_delta_txt = "-1"
        $ showP("nyra", "raison", 0.77)
        nyra "On ne gouverne pas un risque systémique à l'instinct."
        $ showP("julian", "hesitation", 0.88)
        julian "Pas à l'instinct. À la décision."
    elif "échange" in selected.lower() or "discret" in selected.lower():
        $ pnj_adhesion["julian"] += 1
        $ showP("sael", "raison", 0.77)
        sael "Les circuits parallèles prouvent qu'une transition est déjà en cours."
        $ showP("julian", "reflexion", 0.88)
        julian "Alors assumons-la au grand jour."
    else:
        $ pnj_adhesion["julian"] += 2
        $ showP("elen", "determine", 0.33)
        elen "On a besoin d'un vrai virage !"
        $ showP("julian", "determine", 0.88)
        julian "Oui."
    return