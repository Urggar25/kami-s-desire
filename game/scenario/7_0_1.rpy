label _7_0_1_REVEIL_CHAMBRE:

    scene black

    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    $ current_day = 7

    $ blink()

    play sound sfx_knock volume 4.0
    "BAM BAM BAM."

    scene bg_cg012 at adaptive_fullscreen with dissolve

    $ blink()

    "Je me redresse d'un coup."

    think "Merde."

    play sound sfx_knock volume 4.0
    "Je repousse la couette."
    "Je manque de me prendre les pieds dedans."
    "Je traverse la chambre à moitié réveillé."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "J'ouvre la porte."

    scene bg_dortoir at adaptive_fullscreen with dissolve

    $ showGroup([
        ("lysa", "neutre", 0.75),
        ("noam", "neutre", 0.25),
    ])

    lysa "..."

    noam surpris "Quoi ?"
    noam surpris "Qu'est-ce qui se passe ?"

    lysa "Rien."

    noam panne "Rien ?"

    lysa "Enfin..."
    lysa "C'est pas une catastrophe quoi."

    "Je la fixe."

    "Elle me fixe aussi."

    "Puis son regard descend."
    "T-shirt froissé."
    "Cheveux en bataille."
    "Pantalon de pyjama."

    think "Ah."

    lysa taquin "Je vois que tu as gardé toute ta dignité."

    noam desaccord "Je croyais qu'on était attaqués."

    lysa rire "Par ta couette, peut-être."

    noam "Très drôle..."
    noam "Sérieux... Pourquoi tu me réveilles en pleine nuit si c'est pas important ?"

    lysa taquin "En pleine nuit ? Il est quasi midi..."

    noam surpris "Quoi ?!"

    lysa "Je crois que tu as bien entendu."

    noam panne "Hein ?! Pourquoi personne m'a réveillé ?"
    noam hesitation "J'ai loupé l'annonce... Ah, c'est tout..."

    "Elle me coupe la parole."
    lysa neutre "Parce que personne ne s'est levé."

    "Je cligne des yeux."

    noam surpris "Personne ?"

    lysa "Pas vraiment."
    lysa "Ecoute, laisse moi entrer avant que tout le monde te voit dans ton plus bel attirail."

    "Touché, coulé..."

    noam taquin "Raaah ! Allez rentre..."

    $ hideGroup()

    scene bg_cg025 at adaptive_fullscreen with dissolve
    $ unlock_gallery_image("bg_cg025")

    pause 2.0

    lysa "En fait, y'a pas eu d'annonce."
    lysa "Pas de petite voix divine pour nous traiter de mobilier défectueux."

    "Je tourne instinctivement la tête vers l'écran dans ma chambre."
    "Noir."
    "Complètement noir."

    think "..."
    think "Elle n'a pas parlé."

    noam hesitation "Depuis ce matin ?"

    lysa neutre "Depuis le vote d'hier même."

    "La phrase reste suspendue une seconde."

    noam inquiet "Et personne trouve ça inquiétant ?"

    lysa "Si. Enfin je pense, pas grand monde n'est levé pour le moment."
    lysa sourire "Faut dire que ça fait un bail qu'on a pas pu dormir sans être reveillés le matin... Et c'est assez agréable."

    "Je regarde encore l'écran."
    "Toujours rien."

    think "On a la paix."
    think "Pour une fois."

    "Je relâche enfin mes épaules."
    "Je ne m'étais même pas rendu compte qu'elles étaient montées."

    noam taquin "D'accord."
    noam taquin "Donc tu as défoncé ma porte pour me dire que tout va bien."

    lysa desaccord "J'ai pas défoncé."

    noam "BAM BAM BAM."

    lysa desaccord "J'ai toqué normalement."

    noam colere "Tu as toqué comme une malade mentale !"
    noam colere "Tellement que j'ai sauté de mon lit !"

    lysa blase "C'est toi qui es fragile aussi..."

    noam "Je suis en pyjama devant une représentante officielle d'Harmonie."

    lysa rire "J'avais remarqué."
    lysa rire "Monsieur le représentant officiel d'Harmonie."

    "Elle détourne le regard."
    "Cette fois, pour de vrai."

    lysa culpabilite "Désolée."
    lysa culpabilite "Je pensais que tu étais levé."

    noam sourire "Techniquement, maintenant oui."

    lysa taquin "Techniquement, tu es surtout décoiffé."

    noam taquin "C'est une stratégie."

    lysa "Pour faire quoi ?"

    noam taquin "Désorienter l'ennemi."

    lysa taquin "Si c'est moi ton ennemie, alors..."
    lysa sourire "Ça marche..."

    "Cette fois, elle sourit vraiment."

    "Pas longtemps."
    "Mais vraiment."
    "Ça fait bizarre."
    "Mais ce n'est pas particulièrement désagréable."

    lysa neutre "La cafétéria commence à se remplir."
    lysa "Enfin..."
    lysa "À se réveiller."

    noam reflexion "Les autres vont bien ?"

    lysa sourire "Pour ceux debouts, à midi, ils commencent à avoir une sacrée faim."
    lysa taquin "Toi aussi tu dois avoir faim non ?"

    noam rire "Je crois bien que mon estomac crie famine."

    lysa "Je t'attends ?"

    noam "Laisse moi deux minutes."

    lysa blase "Mensonge."

    noam "Cinq."

    lysa sourire "C'est déjà plus crédible."

    "Elle recule d'un pas."

    lysa neutre "Je t'attends devant."
    lysa "Ne me fais pas trop attendre."

    noam sourire "Je vais essayer."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "La porte se referme."

    "Je reste debout au milieu de la chambre."

    "Encore en pyjama."
    "Encore à moitié réveillé."

    "Mais plus vraiment paniqué."

    "Je regarde l'écran."

    "Noir."

    "Pas de visage."
    "Pas de sourire."
    "Pas de voix."

    think "Elle n'est pas là."

    "Un vrai soulagement me traverse."
    "Net."
    "Presque honteux."

    think "Tant pis."

    "Je vais dans la salle de bain pour me refaire une beauté."

    scene bg_cg026 at adaptive_fullscreen with dissolve

    "Je passe de l'eau sur mon visage."
    "Dans le miroir, j'ai l'air de quelqu'un qu'on a réveillé pendant une évacuation."

    think "Pas loin."

    "Je respire un coup."

    "Je cherche mes vêtements."
    "J'enfile ce qui me tombe sous la main."

    scene bg_cg026_1 at adaptive_fullscreen with dissolve

    "Puis un deuxième."

    "La chambre reste silencieuse."

    "Pour une fois, le silence ne ressemble pas à une menace."

    think "Cafétéria."
    think "Lysa."
    think "Une matinée sans Kami."

    "Allez j'y vais."
    "Je prends ma veste."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Avant de sortir, je jette un dernier regard à l'écran."

    "Toujours noir."

    think "Ça fait du bien."

    think "Un peu trop."

    jump _7_0_1_CAFETERIA

# Durée : ~3m00

label _7_0_1_CAFETERIA:

    call show_custom_title("Je vais à la cafétéria avec Lysa.")

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    "La cafétéria est déjà ouverte."
    "Mais ce n'est pas comme d'habitude."
    "Ça parle."
    "Ça circule."
    "Ça respire."

    "Pas de tension lourde."
    "Pas de regards fuyants."

    "Juste… du bruit normal."

    $ showGroup([
        ("iris",   "sourire",    0.10),
        ("julian", "decontracte", 0.25),
        ("lysa",   "neutre",     0.42),
        ("elias",  "detendu",    0.58),
        ("mara",   "rire",       0.75),
        ("kael",   "fatigue",    0.90)
    ])

    iris sourire "Franchement ?"
    iris sourire "Si on m'avait dit qu'un jour que Kami pouvait bugger comme ça…"
    iris rire "Je n'y aurais jamais cru."

    julian decontracte "Ah mais complètement."
    julian sourire "C'est le meilleur réveil depuis qu'on est arrivés."
    julian joie "Personne qui hurle dans les murs, personne qui nous donne des ordres…"
    julian joie "La grasse mat qui m'avait TEEELLEMENT manqué."

    mara taquin "Tu dis ça comme si t'avais une vie avant."

    julian taquin "J'en avais une très bien, mais je te remercie."
    julian decontracte "Et elle commençait rarement avant midi."

    iris rire "Ça explique beaucoup de choses."

    "Quelques rires passent."
    "Pas forts."
    "Mais présents."

    "C'est nouveau."

    lysa reflexion "C'est calme."
    lysa inquiet "Trop calme. C'est vraiment bizarre..."

    noam "Tu préfères quand elle nous parle comme à des objets ?"

    lysa blase "Non."
    lysa neutre "Mais au moins, on savait à quoi s'en tenir."

    mara reflexion "Là aussi."
    mara neutre "On s'en tient à rien."

    julian sourire "C'est parfait."
    julian decontracte "Rien, c'est déjà mieux que ce qu'on avait."

    elen content "Peut-être qu'elle nous laisse respirer un peu."

    iris taquin "Oh la naïveté…"

    elen surpris "Quoi ?"
    elen content "On peut espérer non ?"

    iris "Kami ?"
    iris desaccord "Nous laisser respirer ?"
    iris desaccord "Elle a déjà du mal à nous laisser penser."

    julian idee "Peut-être qu'elle est cassée."

    "Un petit flottement."
    "Ça retombe vite."

    kael reflechit "Techniquement, c'est possible qu'il y ait eu une surcharge."
    kael neutre "Ou une mise à jour."
    kael neutre "Ou un redémarrage système."

    iris gene "Merci Kael."
    iris gene "On est rassurés."

    kael neutre "Je dis juste que c'est cohérent."

    julian sourire "Moi je vote pour qu'elle reste comme ça."

    mara reflexion "Sans vote, ça va être compliqué."

    julian rire "Encore mieux."

    "Nouveau rire."
    "Un peu plus franc cette fois."

    "Je m'assois."
    "Plateau devant moi."
    "Je mange sans réfléchir."

    "Ça fait longtemps que c'était pas juste… manger."

    $ hideGroup()

    $ showGroup([
        ("iris",   "sourire",  0.10),
        ("julian", "detendu",  0.28),
        ("lysa",   "neutre",   0.50),
        ("noam",   "neutre",   0.72)
    ])

    lysa reflexion "T'as vu ?"

    noam "Quoi ?"

    lysa sourire "Les gens parlent."

    noam "Oui."

    lysa neutre "Pas pour convaincre, pas pour discuter de ces foutus votes."
    lysa "Juste pour parler entre eux."

    noam reflexion "C'est étrange."

    lysa sourire "Ouais. C'est bien vrai."

    "Je relève les yeux."
    "Elle dit ça simplement."

    iris intervention "On devrait faire un truc."

    julian neutre "Comme quoi ?"

    iris sourire "Profiter."

    julian taquin "Spoiler : c'est pas ce qu'on fait déjà ?"

    iris "Oui mais laisse-moi rêver deux minutes."
    iris rire "Je veux que ça DUUURE..."

    julian rire "Accordé."

    "Personne ne contredit."
    "Parce que tout le monde le pense."

    think "Pas d'annonce."
    think "Pas de règle."
    think "Pas de pression."
    think "Juste… nous."

    "Je regarde autour."
    "Les visages sont différents."

    think "On respire."
    think "Pour une fois."

    "Je baisse les yeux vers mon plateau."

    "Quelque chose cloche."

    "Mais pas assez pour gâcher le moment."

    "Pas encore."

    $ hideGroup()

    jump _7_0_1_TEMPS_LIBRE_1

label _7_0_1_TEMPS_LIBRE_1:

    scene bg_couloir at adaptive_fullscreen with dissolve

    noam neutre "Bon."
    noam sourire "On progresse."

    call START_FREE_TIME("_7_0_1_APRES_MIDI_TOMAS_CANON") from _call_START_FREE_TIME_7_0_1

label _7_0_1_APRES_MIDI_TOMAS_CANON:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_low_tension.mp3" fadein 1.5

    "L'après-midi passe lentement."

    "Pas dans le mauvais sens."

    "Juste… lentement."

    "Comme si le Conclave retenait son souffle en ne sachant pas quoi faire."

    "Je tourne au coin d'un couloir quand quelqu'un m'interpelle."

    $ showGroup([
        ("tomas", "neutre", 0.30),
        ("noam",  "neutre", 0.70),
    ])

    tomas neutre "Noam."

    noam "Hm ?"

    tomas neutre "Tu as quelques minutes ?"

    noam taquin "Ça dépend."
    noam taquin "Tu vas encore essayer de me faire lire des statistiques incompréhensibles ?"

    tomas gene "Seulement une petite quantité."

    noam panne "Merde."

    tomas determine "Je suis sérieux."

    "Il ajuste légèrement ses lunettes."

    "Ça aussi, c'est devenu un réflexe chez lui."

    "Comme si remettre ses lunettes correctement lui permettait de remettre le monde correctement aussi."

    noam neutre "Qu'est-ce qu'il y a ?"

    tomas reflechit "J'ai vérifié certaines données disponibles dans la salle du Canon."

    noam surpris "Le Canon ?"

    tomas neutre "Oui."
    tomas neutre "Les archives externes."
    tomas neutre "Les retranscriptions automatiques."
    tomas neutre "Les rapports publics."

    noam taquin "Tu bosses vraiment alors que tout le monde est de bonne humeur ?"

    tomas reflechit "Je préfère vérifier des choses quand elles deviennent anormales."
    tomas gene "C-C'est plus... rassurant."

    noam hesitation "Et ça l'est ?"

    "Il hésite."

    "Pas longtemps."

    tomas hesitation "Oui."
    tomas hesitation "Enfin je pense..."
    tomas determine "Suis moi..."

    "Je le suis pendant quelques minutes en silence."

    $ hideGroup()

    scene bg_canon at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_tension.mp3" fadein 1.5

    "La salle du Canon est presque vide."
    "Elle est d'ailleurs particulièrement froide par rapport au reste du Conclave."
    "Toujours les mêmes écrans."
    "Toujours cette impression d'être dans un endroit qui n'a pas été conçu pour des êtres humains."

    $ showGroup([
        ("tomas", "neutre", 0.30),
        ("noam",  "neutre", 0.70),
    ])

    tomas neutre "Regarde."

    "Il tapote sur un écran et y affiche plusieurs fenêtres."
    "Des centaines de lignes incompréhensibles défilent."

    noam panne "Tomas."
    noam panne "Je vais être honnête avec toi."
    noam panne "Je comprends rien à ce que tu fais..."

    tomas gene "A-Ah... Oui."
    tomas gene "Pardon. Je vais t'expliquer."

    "Il ferme plusieurs fenêtres."
    "Une seule reste ouverte."
    "Un tableau."
    "Bien plus simple que le reste cette fois."

    tomas inquiet "C'est... Les exécutions quotidiennes."

    noam "..."

    "Le mot suffit à refroidir la pièce encore davantage."
    "Je crois même que la température est négative..."

    tomas neutre "Le système mondial publie automatiquement les chiffres toutes les heures."
    tomas neutre "Normalement."

    noam hesitation "Et ?"

    tomas reflechit "Regarde... Depuis hier soir…"

    "Il déglutit légèrement."

    tomas inquiet "Zéro."
    tomas inquiet "Zéro exécution."
    tomas inquiet "A toutes les heures depuis le vote d'hier..."

    "Je regarde l'écran."
    "0."
    "Partout."
    "Toutes régions confondues."

    noam surpris "..."
    noam surpris "C'est une bonne nouvelle, non ?"
    noam hesitation "Je comprends pas..."

    tomas raison "Techniquement oui."

    noam hesitation "Mais est-ce que c'est possible ?"

    tomas reflechit "Statistiquement…"

    tomas reflechit "C'est extrêmement improbable."
    tomas neutre "On est généralement entre vingt-cinq et quarante-cinq exécutions par jour."
    tomas inquiet "Là, il n'y en a aucune."
    tomas hesitation "Alors c'est pas impossible..."
    tomas hesitation "Mais c'est pas non plus ordinaire."

    "Je continue de fixer l'écran."
    "Le zéro."
    "Un chiffre ridicule."
    "Un chiffre minuscule."
    "Et pourtant."

    noam reflexion "Donc soit personne dans le monde entier n'a enfreint un Commandement…"
    noam reflexion "Soit le système déconne."

    tomas raison "Oui."

    noam inquiet "Je crois bien que ça déconne sérieusement..."
    noam inquiet "D'abord Kami... Et maintenant ça ?"

    tomas hesitation "J'en sais trop rien, M-Mais..."
    tomas joie "Peut-être que... Les commandements ne s'appliquent plus."

    "Un léger sourire passe sur son visage."
    "Très léger."
    "Mais réel."
    "Ça aussi, c'est rare."

    noam reflexion "Tu crois que c'est lié à Kami ?"

    tomas raison "C'est presque certain que c'est lié à l'état de Kami."

    noam hesitation "Et si elle revient pas ?"

    tomas inquiet "Alors les règles du monde n'existeront plus."

    noam surpris "Tu as l'air sûr de toi."

    tomas neutre "Non."

    tomas reflechit "Mais si Kami disparaît réellement…"
    tomas inquiet "Alors ça dépasse largement le Conclave."

    "Silence."
    "Pas un silence lourd."
    "Un silence vide."

    noam fatigue "C'est étrange."

    tomas neutre "Quoi ?"

    noam triste "Hier encore j'aurais dû être content d'apprendre ce genre d'information."
    noam triste "Et là…"
    noam fatigue "Je suis surtout fatigué."

    tomas fatigue "Je crois qu'on l'est tous."

    "Les écrans continuent de tourner doucement."

    "Aucun son."
    "Aucune alerte."
    "Aucune voix de Kami."
    "Juste les machines."
    "Pour la première fois depuis longtemps…"
    "Le monde semble fonctionner sans elle."

    think "Ou essayer."

    noam reflexion "Tu vas montrer ça aux autres ?"

    tomas mefiant "Pas encore."

    noam hesitation "Pourquoi ?"

    tomas reflechit "Parce que je ne sais pas encore ce que ça signifie."
    tomas neutre "J'essaye de comprendre ce que ça veut dire..."

    think "Quelque chose cloche."
    think "Et ça fait bien longtemps que ça n'était plus arrivé."

    $ hideGroup()

    "Je quitte la salle et me dirige vers la cafétéria, je commence à avoir un petit creux."

    jump _7_0_1_SOIREE_TENSION_LEGERE

label _7_0_1_SOIREE_TENSION_LEGERE:

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    "Le dîner commence tard."
    "Personne ne l'a vraiment décidé."
    "Les gens sont juste revenus progressivement manger après avoir vaqué à leurs occupations."
    "Par habitude."
    "Ou parce qu'il n'y avait nulle part ailleurs où aller."

    "L'ambiance est encore légère."

    "Pas joyeuse."
    "Mais supportable."

    $ showGroup([
        ("iris",   "sourire",     0.10),
        ("julian", "decontracte", 0.25),
        ("lysa",   "reflexion",   0.42),
        ("kael",   "fatigue",     0.58),
        ("elias",  "neutre",      0.75),
        ("mara",   "neutre",      0.90)
    ])

    iris taquin "Franchement, si demain elle parle toujours pas…"

    julian sourire "Je commence officiellement à apprécier cette dystopie."

    elen content "Tu dis ça maintenant."
    elen "Mais au bout de trois jours tu vas mourir d'ennui."

    julian rire "Impossible."
    julian taquin "Je suis fascinant."

    iris rire "Laisse moi rire..."
    iris taquin "Ça aussi, c'est une maladie mentale."

    "Elen rit."
    "Même Julian sourit vraiment cette fois."
    "C'est étrange comme tout paraît plus simple sans Kami."
    "Comme si sa voix occupait normalement une partie de l'air."

    lysa reflexion "Je crois surtout qu'on est en train de profiter du silence avant de comprendre pourquoi il est là."

    iris gene "Toujours optimiste, toi."

    lysa inquiet "Si ça peut nous garder en vie..."

    kael fatigue "Techniquement, elle peut juste être en maintenance et revenir dès demain."

    iris colere "Kael. Non. Tais toi un peu."
    iris desaccord "Tu peux arrêter de rendre chaque chose terrifiante avec un ton calme ?"

    kael neutre "Il ne faut pas se mentir aussi..."

    "Petit rire autour de la table."
    "Pas fort."
    "Mais naturel."

    "Puis quelqu'un pose brutalement un plateau."

    play sound "sfx/plate_drop.mp3"

    "CLAC."

    elias inquiet "Ok."
    elias inquiet "Bon les gars, faut qu'on parle."

    mara agace "Tu commences à devenir très inquiétant quand tu dis ça."

    elias neutre "Non mais sérieux."

    "Il passe une main dans ses cheveux."

    elias inquiet "Quelqu'un est allé dans la salle de stockage ?"

    "Quelques regards se lèvent."

    mara doute "Pourquoi ?"

    elias inquiet "Parce qu'il manque du matériel."

    iris surpris "Quel genre de matériel ?"

    elias "Des outils."
    elias "Des composants."
    elias inquiet "Deux batteries aussi."

    kael surpris "Des batteries ?"

    elias inquiet "Oui."

    mara doute "T'es sûr que tu les as pas déplacées ?"

    elias colere "Oui je suis sûr."

    "Sa réponse part un peu trop vite."
    "Comme s'il s'était déjà posé la question cinquante fois."

    elias fatigue "J'avais tout rangé ce matin."
    elias fatigue "J'étais en train de bricoler un petit truc..."

    kael reflechit "Dans le stockage principal ?"

    elias neutre "Oui."

    kael taquin "Drôle d'endroit..."

    elias desespoir "Oui mais bon, au moins y'a personne là bas, je peux me concentrer."
    elias desespoir "Je sais où je range mes trucs."
    elias colere "Et là, y'a plus rien !"

    mara reflexion "Il manque beaucoup de choses ?"

    elias fatigue "Pas énormément."
    elias inquiet "Mais les composants qui me fallait, ils sont pas facilement remplaçables ceux là."

    iris hesitation "Et personne a rien pris ici ?"

    "Silence."
    "Personne ne répond."
    "Même Julian relève un peu la tête."

    julian reflexion "Pourquoi quelqu'un volerait des batteries ?"

    elias panique "J'en sais rien."

    lysa reflexion "Pour bricoler quelque chose ?"

    kael reflechit "Ou démonter quelque chose."

    iris colere "Génial."
    iris colere "Tu sous-entends qu'il y a un voleur parmis nous ?!"

    elias inquiet "Je dis pas qu'on nous vole."

    mara agace "Tu viens littéralement de demander si quelqu'un avait pris ton matériel."

    elias inquiet "Oui mais—"

    "Il s'arrête."
    "Comme s'il essayait lui-même de décider si ça avait du sens."

    elias fatigue "Je comprends pas."

    "Le ton a changé."
    "Pas brutalement."
    "Comme une musique qui devient légèrement fausse."

    noam "T'as vérifié partout ?"

    elias fatigue "Trois fois au moins."

    kael neutre "Il y a des caméras dans le stockage."

    "Tout le monde se tait une demi-seconde."
    "Puis réalise."

    iris surpris "Ah. Oui."
    iris reflexion "C'est vrai qu'on vit tout le temps avec ça, mais il y a des caméras partout ici..."

    elias reflechit "Faudrait voir si on peut accéder aux images..."
    elias panique "Mais pour ça faut avoir l'autorisation de Kami..."

    "Cette fois, le silence reste un peu plus longtemps."

    mara stress "Super."

    julian panne "On est peut-être juste devenus un groupe de singes livré à lui-même."

    iris taquin "Toi on le savait déjà."

    julian sourire "Je prends ça comme un compliment."

    iris desaccord "Si tu veux, mais ça n'en est pas un."

    "Quelques sourires reviennent."
    "Mais moins facilement."
    "Le sujet reste là."
    "Suspendu au-dessus de la table."

    think "Des outils."
    think "Des batteries."
    think "Des objets qui disparaissent."

    think "C'est rien."

    think "Probablement."

    "Et pourtant."

    "Je vois Elias regarder encore dans le vide."
    "Comme s'il essayait de revoir exactement où il avait posé ses affaires."

    $ hideGroup()

    jump _7_0_1_FIN_JOURNEE

label _7_0_1_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 2.0

    "La journée est passée plus vite que prévu."

    "Sans vote."
    "Sans annonce."
    "Sans Kami."
    "Juste… une journée... Presque banale."

    "Je retire ma veste et la laisse tomber sur la chaise près du bureau."
    "Le silence dans la chambre est toujours là."
    "Mais il a changé."
    "Hier encore, ce genre de silence m'aurait mis mal à l'aise."
    "Aujourd'hui…"

    think "J'ai presque envie qu'il reste."

    "Je m'assois sur le bord du lit."
    "Je repense à la cafétéria."
    "Aux rires."
    "Aux discussions inutiles."
    "À Tomas."
    "Aux écrans remplis de zéros."

    think "Quelque chose cloche."
    think "Mais personne n'a envie de casser ce moment."

    "Je passe une main sur mon visage."
    "Fatigue."
    "Soulagement."
    "Et cette étrange impression de respirer enfin un peu."

    "Mon regard dérive vers le bureau."
    "Puis il se fige."

    think "..."

    "Le dessin n'est plus là."
    "Le petit dessin de Juliette."
    "Celui que je laissais toujours près de l'écran."

    "Je me redresse légèrement."

    noam surpris "Hein... ?"

    "Je regarde autour de moi."
    "Le bureau."
    "Le sol."
    "Sous le lit."
    "Rien."

    think "Je l'ai pourtant laissé là il me semble."

    "Un léger frisson me traverse."
    "Pas de panique."
    "Juste cette sensation désagréable."
    "Comme un détail qui refuse de rester un détail."

    "Je regarde l'écran noir une dernière fois."

    think "Où est-ce que j'ai bien pu le mettre ?"
    think "Je le chercherai demain, là je suis crevé."

    "Je m'allonge finalement dans le lit."
    "Le silence revient."
    "Mais cette fois…"

    think "Il sonne un peu faux."

    scene black with fade

    call end_day("8")
    jump _8_0_1_REVEIL_CHAMBRE
