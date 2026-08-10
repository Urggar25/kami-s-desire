label _14_0_1_1_0_REVEIL_CHAMBRE:

    "La nuit passe lentement. J'ai du mal à dormir."
    "L'annonce de Kami finit par retentir mais je ne souhaite pas me lever."
    "Alors j'attends, je me repose. Je ne veux voir personne."

    pause 1.0

    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 3.0

    "Des coups légers mais insistants contre la porte me tirent du sommeil."
    "Je reste immobile un long moment, espérant que la personne finisse par partir."

    nyra inquiet "Noam ? Tu es là ? C’est Nyra."
    nyra inquiet "Je peux entrer ?"

    "Je ne réponds pas."
    "Mon corps est lourd. Mes yeux brûlent."
    "J’ai l’impression d’avoir dormi à peine une heure."

    play sound sfx_knock volume 0.9

    nyra hesitation "Noam… s’il te plaît."
    nyra raison "C’est important."

    "Important."
    "Évidemment."
    "Tout est toujours important ici."

    "Je ferme les yeux et expire lentement."
    "Aucune partie de moi n’a envie de se lever."
    "Encore moins de parler."

    play sound sfx_knock volume 0.8

    nyra inquiet "Je sais que tu es réveillé."

    scene bg_chambre at adaptive_fullscreen with fade

    "Je serre la mâchoire."
    "Elle a raison. Et ça m’énerve."

    noam fatigue "... Entre."

    "Je me lève avec difficulté."
    "Mes jambes répondent mal, comme si elles appartenaient à quelqu’un d’autre."

    "Je déverrouille la porte."
    "Elle s’ouvre doucement."

    "Nyra entre sans précipitation."
    "Toujours droite. Toujours calme."
    "Mais son regard est plus grave que d’habitude."

    $ showGroup([
        ("noam", "fatigue", 0.25),
        ("nyra", "raison", 0.75),
    ])

    nyra neutre "Merci."
    nyra raison "Je ne vais pas te déranger longtemps."

    "Elle referme la porte derrière elle avec soin."
    "Puis elle reste debout, les mains jointes devant elle."

    nyra neutre "Tu n’es pas venu à l’annonce de ce matin."

    noam fatigue "Non."

    nyra raison "Tu savais qu’il y en avait une."

    noam hesitation "Oui, mais..."

    nyra reflexion "Mais tu n’es pas venu."

    noam fatigue "J’avais besoin de dormir."

    nyra neutre "Tout le monde a besoin de dormir, Noam."

    "Je n’ai rien à répondre à ça."

    nyra raison "Tout le monde l’a remarqué."

    noam inquiet "... Tout le monde ?"

    nyra neutre "Oui."

    "Elle marque une pause, comme pour me laisser intégrer la gravité de la situation."

    nyra raison "Noam… je vais être franche avec toi."
    nyra triste "Parce que tu dois l’entendre."
    nyra raison "Ton comportement commence à inquiéter beaucoup de monde."
    nyra reflexion "Et pas seulement pour ton bien."

    "Je sens la colère monter d’un coup."

    noam colere "Inquiéter ?! Je vous inquiète ?!"
    noam colere "C’est ça que vous racontez dans mon dos ?!"

    "Nyra ne bronche pas."
    "Elle reste parfaitement calme, ce qui m’énerve encore plus."

    nyra raison "Je ne dis pas que c’est vrai. Je te dis ce que les autres pensent."
    nyra inquiet "Et franchement… vu comment tu te comportes depuis deux jours, je les comprends un peu."

    "Je me mords violemment la lèvre."
    "La colère redescend aussi vite qu’elle est montée, laissant derrière elle un goût amer de regret."

    noam "... Désolé."
    noam fatigue "Je… je suis fatigué. Vraiment fatigué."

    nyra "Je sais."

    "Elle s’approche lentement et s’assoit sur le bord du lit, gardant une distance respectueuse."

    nyra reflexion "Le prochain vote aura lieu demain, au cours du quinzième jour."
    nyra raison "Le sujet est : « Toute information détenue par [codex_dialogue_link('archive', 'ARCHIVE')] devient consultable par tout citoyen. »"

    noam inquiet "Enfin… On va enfin pouvoir savoir ce qui se passe vraiment dehors ?"

    nyra neutre "C’est ce que beaucoup espèrent."
    nyra raison "Si ça passe, on aura accès à toutes les données qu’[codex_dialogue_link('archive', 'ARCHIVE')] a accumulées depuis le début."

    noam reflexion "Ça veut dire… les rapports sur l’extérieur, les vraies raisons de notre présence ici, ce qui est arrivé au monde…"

    nyra determine "Exactement. On arrêterait enfin de tourner en rond avec des bouts d’informations."

    "L’idée me redonne un peu d’énergie, malgré la fatigue."

    nyra reflexion "Kami présente ça comme une mesure de transparence totale."
    nyra raison "Et pour une fois, je suis assez d’accord avec elle. On a besoin de savoir."
    nyra triste "On a besoin de mettre fin à la Censure."

    noam reflexion "Ouais… Moi aussi je trouve que c’est une bonne chose."

    nyra neutre "Beaucoup de monde est dans le même état d’esprit."
    nyra raison "Les gens veulent des réponses concrètes, pas juste des discours."

    "Elle marque une courte pause, puis reprend d’une voix plus basse :"

    nyra determine "Mais ce n’est pas la seule raison de ma venue."

    noam inquiet "Je m’en doutais."

    nyra raison "Noam, écoute-moi attentivement."
    nyra raison "Si tu continues comme ça, si tu t’isoles, si tu fais des crises en public, si tu rates les votes…"
    nyra determine "Les gens ne vont plus te voir comme quelqu’un de fatigué."
    nyra neutre "Ils vont te voir comme un danger."
    nyra raison "Et dans un endroit comme celui-ci… les dangers, on finit par les mettre à l’écart."

    "Ses mots sont calmes, presque doux, mais ils portent comme des coups précis."

    noam "... Tu es en train de me menacer ?"

    nyra "Non. Je te mets en garde."
    nyra raison "Parce que je pense encore que tu peux te ressaisir."
    nyra raison "Mais si tu continues à t’enfoncer… personne ne pourra plus te défendre."

    "Je baisse les yeux sur mes mains. Elles tremblent légèrement."

    nyra raison "Réfléchis bien à ce que tu veux faire demain pour le vote."
    nyra raison "Et surtout… arrête de te comporter comme si tu étais déjà seul contre tous."
    nyra neutre "Parce que si tu continues, c’est exactement ce qui va arriver."

    "Elle se lève lentement, lisse sa jupe et se dirige vers la porte."

    nyra "Je te laisse te reposer."
    nyra inquiet "Mais Noam… fais attention à toi."

    hide nyra with dissolve

    "Elle sort sans un bruit supplémentaire."

    "Je reste assis sur mon lit, le regard vide."

    think "Même Nyra… même elle commence à me voir comme un problème."
    think "Et le pire… c’est que je ne peux même pas lui en vouloir."

    "Je me rallonge, fixant le plafond fissuré."

    think "Demain… un vote pour ouvrir toutes les archives."
    think "Enfin la possibilité d’avoir des réponses sur le monde extérieur."

    think "Et moi… je ne sais même plus qui je suis vraiment."

    pause 2.5

    jump _14_0_1_1_0_CAFETERIA_REJET

label _14_0_1_1_0_CAFETERIA_REJET:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_careful_wanting.mp3" fadein 2.5

    "Quand j'entre dans la cafétéria, le changement est immédiat et brutal."
    "Ce n'est plus un simple silence gêné comme hier."
    "C'est un mur."
    "Plusieurs personnes arrêtent de manger en me voyant."
    "D'autres baissent ouvertement la voix."
    "Quelques-unes tournent carrément le dos."

    think "Ils ne font même plus semblant."
    $ showGroup([
        ("mara", "colere", 0.15),
        ("elen", "triste", 0.35),
        ("iris", "inquiet", 0.55),
        ("julian", "hesitation", 0.75),
        ("sael", "mefiant", 0.90),
    ])

    "Je me dirige vers le comptoir."
    "Le trajet me paraît interminable."
    goumi "Bonjour Noam."
    "Même Goumi semble plus froid que d'habitude."
    goumi "Comme d'habitude ?"
    noam fatigue "Oui... merci."
    goumi "Mange chaud."
    goumi "Tu en as besoin."
    noam fatigue "Je vais essayer."

    "Je prends le plateau à deux mains."
    "Derrière moi, les murmures recommencent."
    mara colere "Regardez qui ose encore se montrer."
    "Mara est assise à une table centrale."
    "Elle ne baisse même pas la voix."

    mara colere "Après ce qu'il a fait hier, il a encore le culot de venir manger avec nous ?"
    elen triste "Mara..."
    mara agace "Quoi ?"
    mara colere "C'est la vérité."
    julian hesitation "On peut peut-être éviter de lui tomber dessus dès qu'il arrive."
    mara rire_profond "Bien sûr."
    mara colere "On devrait lui souhaiter bon appétit, peut-être ?"
    iris inquiet "Mara, baisse la voix."
    mara colere "Pourquoi ?"
    mara colere "On n'a plus de brouilleurs."
    mara colere "Kami nous entend déjà tous."
    sael mefiant "Ce n'est pas une raison pour hurler."
    mara agace "Non."
    mara colere "C'est une raison pour être furieuse."
    noam fatigue "Je suis juste venu manger."
    mara colere "Oui, voilà."
    mara colere "Tu viens juste manger."
    mara colere "Après nous avoir tous traités de traîtres."
    noam hesitation "Je n'ai pas..."
    mara colere "Si."
    mara colere "Tu l'as fait."
    mara colere "Tu as pété un câble."
    mara colere "Tu as quitté le débat."
    mara colere "Et maintenant on n'a plus rien pour se protéger."
    elen inquiet "Mara, s'il te plaît..."
    mara colere "Non, Elen."
    mara colere "Je ne vais pas sourire pour qu'il se sente mieux."
    iris colere "Personne ne te demande de sourire."
    mara agace "Alors quoi ?"
    mara colere "Je dois juste faire semblant que tout va bien ?"
    julian inquiet "Personne ne dit que tout va bien."
    mara colere "Parfait."
    mara colere "Alors on peut dire les choses."
    mara colere "A cause de lui, on est tous à poil devant Kami."
    "Je serre le plateau plus fort."
    "Mes doigts me font mal."
    noam colere "Ce n'était pas à cause de moi."
    mara colere "Ah non ?"
    noam colere "Je n'ai pas voté contre tout seul."
    "La table se fige."
    "Même Mara met une seconde à répondre."
    mara colere_noire "Tu veux vraiment repartir là-dessus ?"
    noam fatigue "Non."
    mara colere "Alors tais-toi."
    iris colere "Mara."
    mara agace "Quoi encore ?"
    iris colere "Tu vas trop loin."
    mara colere "Et lui, il est allé où hier ?"
    "Iris ne répond pas tout de suite."
    "Son silence me fait plus mal que les cris de Mara."
    noam fatigue "Laisse tomber."
    elen triste "Noam..."
    noam fatigue "C'est bon."
    "Je vais m'asseoir à une table isolée."
    "Personne ne m'arrête."
    "Personne ne m'invite non plus."
    "Le plateau touche la table dans un bruit sec."
    think "Hier, ils me regardaient avec colère."
    think "Aujourd'hui, ils me regardent avec méfiance."
    think "Demain... ce sera probablement avec peur."
    "Je prends ma fourchette."
    "Je la repose presque aussitôt."
    mara mefiant "Je ne lui fais plus confiance."
    elen triste "On a entendu."
    mara colere "Je le redis parce que personne n'a le courage de l'admettre."
    julian hesitation "Ce n'est pas une question de courage."
    mara colere "Si."
    mara colere "A un moment, il faut regarder les choses en face."
    iris inquiet "Il est juste à côté."
    mara agace "Je sais."
    mara colere "Et je veux qu'il entende."
    noam fatigue "J'entends."
    mara colere "Parfait."
    "Sael se lève."
    "Elle avance jusqu'à ma table."
    sael mefiant "Noam."
    noam inquiet "Quoi ?"
    sael raison "Viens dans ma chambre après."
    sael mefiant "J'ai besoin de te parler."
    noam reflexion "De quoi ?"
    sael mefiant "Pas ici."
    noam fatigue "Je ne suis pas sûr d'avoir envie."
    sael determine "Ce n'était pas vraiment une invitation."
    "Je relève les yeux vers elle."
    noam inquiet "C'est censé me rassurer ?"
    sael raison "Non."
    sael mefiant "C'est censé être clair."
    iris inquiet "Sael..."
    sael mefiant "Je ne lui veux pas de mal."
    mara rire_profond "Toujours bon signe quand quelqu'un précise ça."
    sael colere "Tais-toi."
    mara agace "Oh, l'ambiance revient."
    sael raison "Après manger."
    sael mefiant "Ne tarde pas."
    "Elle retourne vers la sortie sans attendre de réponse."

    hide sael with dissolve

    think "Même quand elle parle calmement, j'entends une menace."
    "Quelques minutes passent."
    "Ou peut-être moins."
    "Je ne sais plus."
    "Iris finit par s'approcher."
    "Elle reste debout à côté de ma table."
    iris inquiet "Noam..."
    noam fatigue "Tu viens aussi me faire la leçon ?"
    iris colere "Ne commence pas."
    noam fatigue "Je suis sérieux."
    iris fatigue "Moi aussi."
    iris inquiet "Tu ne peux pas continuer comme ça."
    noam fatigue "Comme quoi ?"
    iris inquiet "Comme si tout le monde était contre toi."
    iris inquiet "Comme si tu étais déjà seul."
    iris inquiet "Comme si tu avais déjà perdu."
    noam fatigue "Ce n'est pas complètement faux."
    iris colere "Si tu dis ça, ça va devenir vrai."
    noam inquiet "Les autres parlent, c'est ça ?"
    iris hesitation "Oui."
    noam fatigue "Ils disent quoi ?"
    iris triste "Tu le sais déjà."
    noam colere "Dis-le."
    iris inquiet "Certains disent que tu deviens dangereux."
    noam rire "Dangereux."
    iris colere "Ne ris pas."
    noam fatigue "Je ne sais plus quoi faire d'autre."
    iris triste "Noam..."
    noam fatigue "Je suis celui qui a peur de tout le monde."
    noam fatigue "Et c'est moi le danger."
    iris inquiet "Tu as accusé tout le monde."
    iris inquiet "Tu as quitté le débat."
    iris inquiet "Tu rates les annonces."
    iris inquiet "Tu t'isoles."
    iris inquiet "Tu ne dors plus."
    noam fatigue "Merci pour le résumé."
    iris colere "Arrête."
    noam fatigue "D'accord."
    iris triste "Je ne pense pas que tu sois un monstre."
    iris inquiet "Mais je ne sais plus comment t'aider si tu ne nous parles pas."
    noam hesitation "J'ai essayé de parler."
    iris fatigue "Non."
    iris fatigue "Tu as explosé."
    noam colere "Parce que personne n'écoutait."
    iris colere "Et tu crois qu'ils vont mieux écouter maintenant ?"
    "Je baisse les yeux."
    iris fatigue "Voilà."
    noam fatigue "Donc je fais quoi ?"
    iris inquiet "Tu manges."
    iris inquiet "Tu dors."
    iris inquiet "Tu arrêtes de disparaître."
    iris inquiet "Et tu évites de courir vers les gens qui te regardent comme un problème à régler."
    noam reflexion "Tu parles de Sael ?"
    iris hesitation "Oui."
    noam inquiet "Qu'est-ce qu'elle t'a dit ?"
    iris inquiet "Rien de clair."
    iris fatigue "Des histoires de signes."
    iris inquiet "De morts qui ne dorment pas."
    iris inquiet "De choses qui restent accrochées aux vivants."
    noam fatigue "Génial."
    iris colere "Je suis sérieuse."
    noam fatigue "Moi aussi."
    noam fatigue "C'est juste que ma vie devient débile."
    iris taquin "Elle était déjà débile avant."
    iris fatigue "Là, elle devient dangereuse."
    "Un silence tombe entre nous."
    iris inquiet "Promets-moi de faire attention."
    noam fatigue "Je ferai attention."
    iris colere "Ce n'est pas une promesse."
    noam fatigue "C'est tout ce que j'ai."
    iris triste "Tu es vraiment insupportable quand tu vas mal."
    noam fatigue "Je sais."
    iris fatigue "Non, tu ne sais pas."
    iris fatigue "Tu forces les gens à être gentils, et c'est très agaçant."
    "Un très léger sourire me vient."
    "Il disparaît presque aussitôt."
    noam fatigue "Désolé."
    iris inquiet "Mange un peu."
    noam fatigue "Je vais essayer."
    iris colere "Non."
    iris colere "Tu vas manger."
    goumi "Elle a raison."
    iris colere "Vous, ne vous en mêlez pas."
    goumi "Je distribue de la nourriture."
    goumi "Mon avis est pertinent."
    iris fatigue "Super."
    iris fatigue "Même le cuisinier fait la morale maintenant."
    goumi "Exact."
    "Iris soupire."
    iris inquiet "Je retourne là-bas."
    noam fatigue "Oui."
    iris hesitation "Noam..."
    noam inquiet "Quoi ?"
    iris triste "Je suis encore là."
    noam fatigue "Pour l'instant."
    iris colere "Ne gâche pas l'effort."
    "Elle repart vers les autres."
    mara agace "Alors ?"
    mara rire_profond "Le patient va survivre ?"
    iris colere "Mara, je te jure que si tu ouvres encore la bouche..."
    mara rire_profond "Quoi ?"
    mara rire_profond "Tu vas me soigner avec une fourchette ?"
    elen surpris "Iris !"
    julian rire "Voilà une image très rassurante."
    "Un rire nerveux circule à leur table."
    "Pas un vrai rire."
    "Mais quelque chose qui ressemble encore un peu à de la vie."
    think "Ils peuvent encore rire ensemble."
    think "Même maintenant."
    "Je prends une bouchée."
    "Elle a un goût de carton."
    "Mais j'avale quand même."
    "Quand je me lève, plusieurs regards se tournent aussitôt vers moi."
    mara mefiant "Tu pars déjà ?"
    noam fatigue "Oui."
    mara agace "Pas de grande déclaration cette fois ?"
    noam fatigue "Non."
    elen triste "Noam..."
    noam fatigue "Ca va."
    elen inquiet "Non."
    noam fatigue "Je sais."
    julian inquiet "Tu vas où ?"
    noam fatigue "Voir Sael."
    iris inquiet "Tu n'es pas obligé."
    "Je serre les doigts autour du plateau."
    "Puis je le repose sur la table."
    noam fatigue "Je viens."
    iris triste "Fais attention."
    noam fatigue "Oui."
    mara agace "Bonne chance avec la cinglée."
    mara rire_profond "Rien."
    mara agace "Je tousse."
    "Je n'attends pas que ça reparte."
    "Je quitte la cafétéria sous leurs regards."
    scene bg_couloir at adaptive_fullscreen with dissolve
    "La porte de la cafétéria se referme derrière moi."
    "Le couloir est plus silencieux."
    "Mais pas plus rassurant."
    noam fatigue "Bon..."
    noam inquiet "Allons voir ce que Sael me veut."

    jump _14_0_1_1_0_CHAMBRE_SAEL

label _14_0_1_1_0_CHAMBRE_SAEL:

    scene bg_couloir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_debate.mp3" fadein 2.0

    "Le couloir semble plus long que d'habitude."
    "Plus silencieux aussi."
    "Chaque néon grésille comme s'il retenait son souffle."

    noam fatigue "Sael voulait me parler."
    noam inquiet "Juste parler."

    "Je m'arrête devant sa porte."
    "Ma main reste levée quelques secondes."

    think "Je peux encore faire demi-tour."

    noam fatigue "Non."
    noam inquiet "Autant en finir."

    play sound sfx_knock volume 0.8

    "Je toque."

    pause 0.8

    play sound sfx_door volume 0.8

    "La porte s'ouvre presque immédiatement."

    $ showGroup([
        ("noam", "inquiet", 0.35),
        ("sael", "mefiant", 0.70),
    ])

    sael mefiant "Noam."

    noam inquiet "Tu voulais me parler."

    sael raison "Oui."

    noam hesitation "Alors parle."

    sael mefiant "Pas dans le couloir."
    sael determine "Suis moi."
    sael raison "Je ne suis pas là pour te rassurer."

    noam hesitation "Alors tu es là pour quoi ?"

    sael mefiant "Vérifier."

    noam inquiet "Vérifier quoi ?"

    sael raison "Si tu es encore seul dans ton corps."

    stop music

    pause 0.4

    play sound sfx_glitch volume 0.9

    scene black with vpunch
    with fade 

    pause 0.2

    scene bg_couloir at adaptive_fullscreen with fade

    noam peur "Quoi ?"

    sael mefiant "Ne bouge pas."

    noam panique "Sael, c'est quoi cette phrase ?"

    sael raison "Une phrase simple."

    noam peur "Non."
    noam peur "C'est une phrase de malade."

    "Quelque chose me frappe de côté."

    play sound sfx_thud volume 1.0
    with hpunch

    scene black with fade
    pause 0.5
    scene bg_chambre_sael at adaptive_fullscreen with dissolve

    "Et me dire d'un coup dans la chambre"

    $ showGroup([
        ("noam", "panique", 0.25),
        ("sael", "mefiant", 0.62),
        ("ryn", "colere", 0.88),
    ])

    ryn colere "Bouge pas, putain !"

    noam panique "Ryn ?!"

    ryn colere "Je t'ai dit de pas bouger !"

    "Son avant-bras écrase ma gorge contre le mur."

    noam peur "Lâche-moi !"

    ryn colere "Pas tant qu'on sait pas ce que t'es."

    noam panique "Ce que je suis ?!"
    noam panique "Je suis Noam !"

    sael mefiant "C'est ce qu'il dirait."

    noam colere "Tu m'entends parler ?!"
    noam colere "Tu m'entends vraiment ?!"

    ryn colere "Ferme-la."

    noam peur "Je n'arrive pas à respirer !"

    sael raison "Dessers un peu."

    ryn colere "S'il se débat, je le plaque au sol."

    sael determine "Dessers."

    "Ryn desserre à peine."
    "Juste assez pour que l'air revienne."

    noam peur "Vous êtes complètement fous."

    sael mefiant "Non."
    sael raison "On est en retard."

    noam inquiet "En retard sur quoi ?"

    sael raison "Les signes."

    noam fatigue "Quels signes ?"

    sael mefiant "Ton regard."
    sael mefiant "Tes absences."
    sael mefiant "Ta colère."
    sael mefiant "Les mots qui sortent de ta bouche et qui ne te ressemblent plus."

    noam colere "Je suis fatigué !"

    sael colere "Tout le monde est fatigué."

    noam colere "Alors pourquoi moi ?!"

    sael raison "Parce que les morts choisissent les fissures."

    play sound sfx_static volume 0.7

    "Le néon au-dessus de nous grésille plus fort."

    noam inquiet "Arrête."

    sael mefiant "Tu les entends ?"

    noam peur "Qui ?"

    sael raison "Les revenards."

    noam peur "Non."

    sael mefiant "Réponds sans réfléchir."

    noam panique "Non !"

    ryn colere "Il ment."

    noam colere "Mais ferme-la !"

    ryn colere "Tu vois ?"
    ryn colere "Ça recommence."

    noam peur "Je suis en train de paniquer parce que tu m'étrangles !"

    sael raison "Tu en es bien sûr ? La peut peut te faire dire..."

    noam inquiet "Sael..."
    noam triste "Ecoute-toi."

    sael determine "Je m'écoute depuis des jours."

    noam peur "Alors écoute-moi, maintenant."

    sael mefiant "Parle."

    noam hesitation "Je ne suis pas possédé."
    noam inquiet "Je ne suis pas un esprit."
    noam peur "Je suis juste terrifié."

    sael triste "Les possédés disent souvent vrai."
    sael mefiant "C'est ce qui les rend difficiles à ouvrir."

    noam panique "A ouvrir ?!"

    play sound sfx_breath volume 1.0
    scene black with vpunch

    $ showGroup([
        ("noam", "panne_creep", 0.25),
    ])

    pause 0.15

    scene bg_chambre_sael at adaptive_fullscreen
    with hpunch

    $ showGroup([
        ("noam", "peur", 0.25),
        ("sael", "determine", 0.62),
        ("ryn", "colere", 0.88),
    ])

    noam panique "Putain !"

    ryn colere "Quoi ?!"

    noam peur "Vous n'avez pas entendu ?!"

    sael mefiant "Entendu quoi ?"

    noam peur "Le cri !"

    ryn colere "Y'a pas eu de cri."

    "La chambre redevient parfaitement silencieuse."

    noam inquiet "Non..."
    noam peur "Non, je l'ai entendu."

    sael raison "Premier aveu."

    noam panique "Ce n'est pas un aveu !"

    sael determine "Ryn."

    ryn colere "Ouais."

    noam peur "Non."
    noam peur "Non, non, non."

    "Sael sort une petite fiole de sel."
    "Le verre tremble légèrement entre ses doigts."

    noam panique "Range ça."

    sael raison "Le sel ferme les portes."

    noam peur "Je ne suis pas une porte pour des esprits ou quoi que ce soit !"

    sael mefiant "Tais toi. Il faut que je me concentre."

    "Elle verse une ligne blanche au sol."

    noam colere "Arrête."

    sael raison "Nom."

    noam inquiet "Quoi ?"

    sael determine "Donne ton nom !"

    noam panique "Noam !"

    sael mefiant "Encore."

    noam colere "Noam !"

    sael mefiant "Encore."

    noam peur "Noam !"

    ryn colere "Plus fort."

    noam panique "NOAM !"

    play sound sfx_glitch volume 1.0
    with vpunch

    sael surpris "..."

    ryn inquiet "Sael ?"

    noam peur "Quoi ?"
    noam peur "Qu'est-ce qu'il y a ?"

    sael mefiant "Pendant une seconde..."
    sael inquiet "Ta voix n'était pas seule."

    noam panique "C'est faux."

    ryn colere "J'ai entendu aussi."

    noam colere "Vous voulez l'entendre."
    noam colere "C'est différent."

    sael determine "Esprit revenard qui hante cet homme..."
    sael determine "Montre ton nom."
    sael determine "Montre ta plaie."
    sael determine "Montre ce que tu veux."

    noam peur "Arrête."
    noam peur "Sael, arrête."

    sael colere "Au nom des morts que nous avons laissés derrière nous..."
    sael colere "Au nom des corps sans sépulture..."
    sael colere "Au nom des voix enfermées dans les murs..."

    play sound sfx_static volume 1.0

    "Le grésillement enfle."

    noam panique "Ryn, lâche-moi !"

    ryn inquiet "Sael, le néon..."

    sael colere "Non STOP !"
    sael determine "Ne regardez pas la lumière."

    noam peur "Pourquoi ?"

    sael mefiant "Parce que ça nous regarde en retour."
    sael triste "Et ça peut être dangereux."

    pause 0.3

    play sound sfx_static volume 1.0

    "Le néon claque."
    "Un instant, le couloir devient blanc."

    noam panique "AAH !"

    ryn colere "Putain !"

    sael determine "Il réagit."

    noam peur "C'est le néon !"
    noam peur "C'est juste le néon !"

    sael colere "Quitte ce corps."

    noam panique "Je suis ce corps !"

    sael colere "Quitte sa bouche."

    noam peur "C'est ma bouche !"

    sael colere "Quitte ses yeux."

    noam colere "Ce sont mes yeux !"

    sael colere "Quitte son nom."

    noam panique "Mais c'est mon nom PUTAIN !"

    ryn inquiet "Sael..."
    ryn inquiet "Il tremble vraiment."

    sael determine "Tant mieux."
    sael determine "C'est que ça réagit."

    noam peur "Arrêtez ces conneries ! Vous allez finir par me tuer !"

    "Ryn serre un peu plus sa main autour de mon cou."

    ryn colere "Si c'est nécessaire pour te purifier..."

    sael colere "Ryn."

    ryn colere "Quoi ?"

    sael determine "Arrête tes conneries."
    sael taquin "Tu veux que les revenards s'attaquent à toi ensuite ?"

    pause 0.2

    ryn "Hein ...?"

    "Ryn tourne la tête vers elle."
    "Son bras se relâche d'un centimètre."

    "C'est suffisant."

    noam colere "Lâchez-moi !"

    play sound sfx_thud volume 1.0
    with hpunch

    "Je lui enfonce le genou dans le ventre."

    ryn colere "Argh !"

    sael surpris "Noam !"

    noam peur "Restez loin de moi !"

    "Je me dégage."
    "Je cours."

    scene bg_couloir at adaptive_fullscreen with dissolve

    ryn colere "Reviens !"

    sael colere "Noam !"

    noam panique "Non !"

    play sound sfx_glitch volume 0.8

    "Le couloir se tord une seconde."
    "Ou peut-être que c'est ma vue."

    noam peur "Non, non, non..."

    ryn colere "Attrapez-le !"

    sael colere "Ne le laisse pas sortir du cercle !"

    noam panique "Je ne suis plus dans votre cercle !"

    "Je fonce vers ma chambre."

    play sound sfx_door volume 1.0

    scene bg_chambre at adaptive_fullscreen with hpunch

    noam panique "Allez !"

    play sound sfx_door volume 1.0
    with vpunch

    "Je claque la porte."

    noam peur "Le bureau."
    noam peur "La chaise."
    noam peur "Tout."

    play sound sfx_thud volume 0.9

    "Je pousse les meubles contre la porte."

    ryn colere "Noam ! Ouvre !"

    noam panique "Va-t'en !"

    sael raison "Noam."
    sael raison "Ce n'est pas fini."

    noam peur "Si."
    noam peur "Si, c'est fini."

    sael mefiant "S'il parle encore avec ta voix, ne l'écoute pas."

    noam panique "C'est moi !"

    ryn colere "Alors prouve-le !"

    noam colere "Allez vous faire foutre !"

    pause 0.5

    "Silence."

    play sound sfx_knock volume 0.5

    sael calme "Noam."

    noam peur "Non."

    play sound sfx_knock volume 0.5

    sael calme "Noam."

    noam panique "Non !"

    play sound sfx_knock volume 0.5

    sael calme "Noam."

    stop music

    pause 0.4

    play sound sfx_breath volume 1.0
    scene black with vpunch

    $ showGroup([
        ("noam", "panne_creep", 0.25),
    ])

    pause 0.15

    scene bg_chambre at adaptive_fullscreen
    with hpunch

    noam panique "TAIS-TOI !"

    "Plus rien."

    "Je glisse contre le mur."
    "Mes jambes ne me portent plus."

    think "Ils sont devenus fous."
    think "Ils voulaient vraiment m'ouvrir."
    think "Ils pensent que quelque chose porte mon visage."

    "Je plaque mes mains sur mes oreilles."

    think "Je ne peux plus faire confiance à personne."
    think "Plus à personne."

    pause 2.0

    call show_custom_title("Après m'être longuement calmé") from _call_show_custom_title_3

    jump _14_0_1_1_0_MESSAGES_KAEL

label _14_0_1_1_0_MESSAGES_KAEL:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 2.5

    "Je suis allongé sur mon lit, les yeux fixés au plafond, quand ma tablette vibre doucement."

    "Un message de Kael."

    kael "Noam, tu es là ?"

    noam "Oui. Qu’est-ce qu’il y a ?"

    kael "Je viens de me faire engueuler par Ryn dans le couloir. Encore."
    kael "Il m’a dit que c’était à cause de moi qu’on n’avait plus de brouilleurs."
    kael "Que j’avais tout fait foirer en votant contre."

    noam "Ils me disent la même chose."

    kael "Ouais… on est les deux parias maintenant."
    kael "Toi parce que tu as pété un câble au débat."
    kael "Moi parce que j’ai voté contre les brouilleurs."

    noam "C’était bien toi qui as voté contre ?"

    kael "Oui. C’était moi."
    kael "Je ne pouvais pas faire autrement. Je veux voir les images de ma chambre."
    kael "Je veux savoir qui a volé la photo de Léa."

    noam "Je comprends."

    kael "Demain, pour le vote… je n’irai pas."
    kael "Je profiterai que tout le monde soit à la Salle du Conclave pour aller consulter les archives tranquillement."
    kael "Les images de J8 seront enfin accessibles."

    noam "Tu vas y aller seul ?"

    kael "Oui. Je ne veux mêler personne à ça."

    noam "Je viens avec toi."

    kael "Vraiment ? Même après ce qui s’est passé hier ?"

    noam "Surtout après ce qui s’est passé hier."
    noam "Je n’ai plus envie de rester avec eux de toute façon."

    kael "D’accord. On se rejoint discrètement vers 13h30 près de la salle d’observation ?"

    noam "Ça marche."

    "Un court silence sur la conversation."

    kael "Au fait… j’ai entendu une rumeur complètement dingue."
    kael "Sael et Ryn t’auraient coincé pour te faire un exorcisme de force ?"

    noam "C’est pas une rumeur."
    noam "Ryn m’a plaqué contre un mur. Sael a sorti du sel et a commencé à psalmodier."
    noam "J’ai cru qu’ils allaient vraiment me tuer."

    kael "Putain…"
    kael "Ils sont devenus complètement tarés."
    kael "Sael est persuadée que tu es possédé par un esprit vengeur ou quelque chose comme ça."

    noam "Ouais… elle m’a dit ça alors que Ryn me tenait encore contre le mur."

    kael "Et toi ? Tu y crois ?"

    noam "Bien sûr que non."
    noam "Mais le pire, c’est qu’ils y croient vraiment."
    noam "Ils pensent que je suis dangereux."

    kael "Bienvenue au club."
    kael "Moi ils pensent que je suis un égoïste qui a sacrifié l’intimité de tout le monde pour sa sœur."

    "Pour la première fois depuis longtemps, un petit sourire m’échappe."

    noam "On fait la paire tous les deux."

    kael "Ouais… les deux pestiférés du Conclave."
    kael "Au moins, on est deux. C’est déjà ça."

    noam "Tu sais que si Sael me voit sortir de ma chambre demain, elle va encore me courir après avec son sel et ses prières ?"

    kael "Haha, merde."
    kael "Alors on fera attention."
    kael "Je t’enverrai un message quand la voie sera libre."

    noam "Ça marche."
    noam "Et Kael… merci."

    kael "Pas de quoi."
    kael "On est dans la même galère maintenant."
    kael "Autant ramer ensemble."

    "La conversation s’arrête là."
    "Je repose la tablette sur ma poitrine et fixe le plafond."

    think "Kael… au moins lui ne me traite pas comme un monstre."
    think "Même s’il a ses propres problèmes."

    "Pour la première fois depuis plusieurs jours, j’ai l’impression d’avoir un allié."
    "Même si c’est un allié fragile."

    pause 1.5

    jump _14_0_1_1_0_FIN_JOURNEE

label _14_0_1_1_0_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_calm_sad.mp3" fadein 3.0

    "Je traverse lentement la pièce et m’assois à mon bureau."
    "Mes yeux se posent presque malgré moi sur le cahier noir."

    "Je l’ouvre à la page du dessin décalqué de Juliette."

    "Je le regarde longtemps."
    "Les traits plus sombres, le sourire légèrement figé, l’atmosphère étrange qui s’en dégage."
    "Je passe lentement le doigt sur les contours."

    think "Pourquoi avoir pris le temps de faire ça ?"
    think "Pourquoi copier le dessin au lieu de simplement le voler ?"
    think "C’est comme si quelqu’un voulait que je le voie… tout en me laissant une copie."

    "Je reste immobile, les yeux rivés sur la page."

    think "Quelqu’un est entré ici."
    think "Quelqu’un a touché mes affaires les plus personnelles."
    think "Quelqu’un connaît mes souvenirs les plus intimes."

    "Je referme doucement le cahier."
    "Puis je le range dans le tiroir, comme si ça pouvait effacer ce que j’ai vu."

    think "Je ne sais plus quoi penser."
    think "Je ne sais plus à qui faire confiance."
    think "Je ne sais même plus si je peux me faire confiance à moi-même."

    "Je me lève et me dirige vers le lit."
    "Je m’allonge tout habillé, sans même enlever mes chaussures."
    "Le plafond fissuré me semble encore plus oppressant que d’habitude."

    scene bg_cg012 at adaptive_fullscreen with fade

    think "Demain, il y a le vote sur les archives."
    think "Tout le monde va pouvoir tout savoir sur tout le monde."
    think "Et moi… je vais probablement rester enfermé ici."

    "Je ferme les yeux."
    "Le sommeil met longtemps à venir."
    "Mais quand il arrive enfin, il est lourd, agité, plein d’ombres et de murmures."

    think "Je ne suis plus en sécurité nulle part."
    think "Même dans ma propre chambre."
    think "Même dans ma propre tête."

    pause 2.5

    scene black with fade
    stop music fadeout 4.0

    call end_day("15") from _call_end_day_15
    jump _15_0_1_1_0_REVEIL_CHAMBRE
