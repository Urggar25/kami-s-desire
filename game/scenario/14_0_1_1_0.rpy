label _14_0_1_1_0_REVEIL_CHAMBRE:

    "La nuit a été mauvaise, encore une fois. J'ai dormi par morceaux, sans réussir à décrocher complètement."
    "Quand l'annonce de Kami retentit dans les couloirs, je l'entends très bien, mais je reste couché."
    "Je n'ai aucune envie de croiser les autres, et encore moins de faire semblant que tout va bien."

    pause 1.0

    scene bg_cg012 at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "Je finis par me rendormir quelques minutes avant que des coups légers contre ma porte me tirent à nouveau du sommeil."

    nyra inquiet "Noam ? C'est Nyra."
    nyra hesitation "Je peux entrer ?"

    "Je garde les yeux fermés en espérant qu'elle comprenne le message toute seule."

    play sound sfx_knock volume 0.9

    nyra raison "Je sais que tu es là. J'en ai pour deux minutes, promis."

    "Je souffle dans mon oreiller avant de me redresser difficilement."

    scene bg_chambre at adaptive_fullscreen with fade

    noam fatigue "Entre."

    "Je déverrouille la porte et retourne m'asseoir sur le lit pendant qu'elle entre."

    $ showGroup([
        ("noam", "fatigue", 0.25),
        ("nyra", "raison", 0.75),
    ])

    nyra neutre "Tu as raté l'annonce de ce matin."
    noam fatigue "J'avais compris."
    nyra raison "J'en doute, sinon tu serais déjà sorti."

    noam reflexion "Pourquoi ?"

    nyra sourire "La livraison est arrivée."

    "Je relève enfin les yeux vers elle."

    noam surpris "La nourriture ?"
    nyra sourire "Oui. La vraie."
    nyra neutre "Goumi a récupéré les caisses ce matin. Il paraît qu'Elen a failli l'embrasser en voyant du pain."

    "Malgré moi, un début de sourire me vient."

    noam fatigue "Je peux la comprendre."
    nyra raison "Tout le monde peut la comprendre. On était à deux cafés de commencer à se manger entre nous."

    noam sourire "Mara aurait commencé par Julian."
    nyra taquin "Probablement parce qu'il parle trop."

    "Le sourire disparaît presque aussitôt. Nyra aussi redevient plus sérieuse."

    nyra raison "Je ne suis pas venue uniquement pour t'annoncer qu'on a retrouvé des glucides."
    noam fatigue "Évidemment."

    nyra reflexion "Le vote de demain concerne [codex_dialogue_link('archive', 'ARCHIVE')]."
    nyra raison "La proposition est simple sur le papier : rendre consultables par tous les citoyens toutes les informations qu'ARCHIVE détient."

    noam reflexion "Toutes ?"
    nyra raison "Toutes."

    noam inquiet "Les rapports sur l'extérieur, les décisions de Kami, les anciennes données..."
    nyra neutre "Oui."
    noam reflexion "Alors c'est une bonne chose."

    nyra hesitation "En partie."

    "Je la regarde plus attentivement."

    noam inquiet "Qu'est-ce qui coince ?"
    nyra raison "Quand ils disent toutes les informations... Qu'est-ce que ça concerne ?"

    "L'idée de transparence devient soudain beaucoup moins confortable."

    nyra reflexion "Je pense qu'on a besoin des informations sur l'extérieur."
    nyra colere "Mais est-ce que c'est la solution ?!"

    "Un silence plus léger s'installe quelques secondes, puis Nyra croise les bras."

    nyra raison "Mais on aura tout le temps pour en parler. Il y a autre chose."
    nyra inquiet "Ryn pose des questions sur toi."

    noam inquiet "Quel genre de questions ?"
    nyra raison "Si tu avais déjà eu des absences avant le Conclave. Si tu entendais des choses. Si ton comportement avait déjà changé brutalement avant ces derniers jours."

    noam colere "Il fait mon diagnostic maintenant ?"
    nyra neutre "Non. Il cherche une explication à ce qu'il s'est passé lors du dernier vote."

    "Sa réponse me coupe un peu dans mon élan."

    nyra inquiet "Je ne te demande pas de faire confiance à tout le monde. Je te demande juste d'éviter de leur donner davantage de raisons de penser que tu deviens imprévisible."
    nyra triste "Je préfère être désagréable maintenant que te regarder t'isoler complètement."

    "Elle se relève."

    nyra neutre "Va manger. Ça ne réglera rien, mais tu réfléchiras mieux avec autre chose que du café dans le ventre."
    noam fatigue "Tu parles comme Goumi."
    nyra sourire "C'est probablement la faim."

    "Elle ouvre la porte puis s'arrête une seconde."

    nyra inquiet "Et Noam... demain, on aura besoin de toi. Alors viens."
    noam reflexion "Compris."

    "Elle sort."
    hide nyra with dissolve

    "Je reste assis quelques secondes avant que mon ventre décide à ma place que la conversation est terminée."

    think "De la nourriture. Enfin. Pour une fois, j'ai une raison simple de sortir de cette chambre."

    pause 1.5

    jump _14_0_1_1_0_CAFETERIA_REJET


label _14_0_1_1_0_CAFETERIA_REJET:

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_73
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 2.5

    "J'entends les bruits de la cafétéria avant même d'ouvrir la porte."
    "Des couverts claquent, des chaises bougent, quelqu'un rit beaucoup trop fort. Après le silence des derniers jours, ça paraît presque anormal."
    "Quand j'entre, je comprends immédiatement pourquoi."
    "Les tables sont enfin remplies de nourriture. Rien de luxueux, mais il y a du pain, des plats chauds, des fruits et assez de portions pour que personne ne compte les miettes."

    $ showGroup([
        ("mara", "neutre", 0.15),
        ("elen", "sourire", 0.35),
        ("iris", "inquiet", 0.55),
        ("julian", "sourire", 0.75),
        ("sael", "mefiant", 0.90),
    ])

    elen joie "Noam !! REGARDE !!"

    "Elen me fait signe avec une tranche de pain à moitié mangée. Elle a l'air absurdement heureuse."

    elen joie "Il y a du pain ! Et des pommes ! Et Goumi a fait un truc chaud avec des patates !"
    julian sourire "Faites la taire. Elle fait l'inventaire depuis vingt minutes."
    elen colere "Mais c'est trooop bon les patates !!"
    mara sourire "Elle en a déjà mangé trois portions."
    elen joie "J'ai FAIM !"
    julian taquin "Nous aussi. On ne fait juste pas une déclaration d'amour à chaque bouchée."
    elen taquin "Tu n'as donc aucune sensibilité."

    "Même Mara laisse échapper un petit rire."

    "Puis plusieurs regards se posent sur moi, et l'ambiance retombe juste assez pour que je le remarque."
    "Je vais jusqu'au comptoir."

    goumi "Bonjour Noam."
    noam fatigue "Salut. Il reste quoi ?"
    goumi "Aujourd'hui ? Tout ce que tu veux."
    goumi "La livraison est arrivée peu après l'annonce de Kami. J'ai rarement vu douze personnes aussi heureuses devant des caisses de légumes."

    noam sourire "Elen a l'air au bord des larmes."
    goumi "Le monde entier a dû apprécier quand elle a commencé à embrasser une tomate..."

    elen joie "Elle était très belle ! Et très bonne aussi !"

    "Je tourne la tête vers elle, surpris qu'elle ait entendu."

    julian rire "Je confirme. Il y a eu un moment très intime entre elles."
    elen colere "Ah ! Jaloux ! Mange et tais-toi."

    "Goumi pose devant moi une assiette fumante."

    goumi "Tu devrais manger pendant que c'est chaud."
    noam fatigue "Ouais. Pas besoin de me convaincre aujourd'hui."

    "L'odeur suffit à me rappeler à quel point j'avais faim."
    "Je prends le plateau et cherche une place."

    mara mefiant "Tu peux t'asseoir là."

    "Je m'arrête. Mara désigne le bout de leur table sans sourire."

    noam surpris "Sérieusement ?"
    mara agace "Ne me fais pas regretter d'avoir été civilisée pendant deux secondes."

    iris fatigue "Assieds-toi avant qu'elle change d'avis."

    "Je m'installe à distance raisonnable. Personne ne me souhaite la bienvenue, mais personne ne se lève non plus."
    "Pendant quelques minutes, la faim gagne sur tout le reste."
    "On mange presque en silence, et pour la première fois depuis longtemps ce silence n'a rien de politique."

    elen joie "C'est vraiment trop trop trop bon. Il manque juste un tout petit peu de sel."

    "Elen commence à prendre un pot avec du sel fin et à en verser de grosses cuillères."

    sael mefiant "Tu pourrais me le passer après ?"

    mara agace "Je vais quand même te dire un truc, Noam."
    iris fatigue "Évidemment."

    mara mefiant "L'autre coup, tu nous as traités comme si on était tous prêts à te trahir."

    "Je repose ma fourchette."

    mara agace "Je dis pas ça pour revenir là-dessus. Personne n'a rien compris à ce qui t'est arrivé."
    mara colere "Je veux savoir si demain tu vas encore décider que tout le monde est ton ennemi en plein milieu du vote."

    noam hesitation "Je ne sais pas ce qui va se passer demain."

    elen hesitation "Mara... Tu as toute la journée pour parler des trucs chiants !"
    elen joie "Laisse-nous manger tranquillement !"

    "Mara la regarde. Elen serre son morceau de pain contre elle comme si quelqu'un risquait de lui reprendre."

    mara fatigue "Mouais... On va d'abord attendre d'avoir mangé tout ça."

    "Un vrai rire circule cette fois. Court, mais réel."
    "Je souris à peine avant de croiser le regard de Sael. Elle n'a pas ri."

    sael mefiant "Noam. Quand tu auras fini, viens dans ma chambre."
    noam inquiet "Quoi ?"

    iris inquiet "Hein ? Pourquoi ?"
    sael raison "Je veux discuter tranquillement avec toi. Sur... Ce que tu dis avoir vu."

    think "Elle est au courant de quelque chose ?!"

    noam inquiet "Tu-Tu sais quelque chose ?"

    sael determine "Ne me fais pas répêter. On en parlera dans ma chambre."

    mara agace "Sael qui se met à inviter les garçons dans sa chambre ? C'était pas dans mon bingo ça."

    "Sael se lève avec son assiette presque intacte."

    elen surpris "Tu ne finis pas ? Me dis pas que t'as pas faim ?!"

    sael neutre "Tu la veux ?"
    elen joie "Ouaiiiis ! Je veux plus jamais devoir attendre pour manger !"
    elen sourire "Faut faire des réserves !"

    "Sael lui tend son assiette. Elen se jette littéralement dessus."

    hide sael with dissolve

    "Sael quitte la cafétéria sans rien ajouter."

    iris inquiet "Je n'aime pas vraiment ça."
    iris hesitation "Elle m'a posé plein de questions bizarres sur toi hier."

    mara rire "Dis surtout que t'es jalouse, ouais !"

    iris blase "Hein ?! Mais d'où tu sors ça toi !"
    iris colere "Pourquoi je serais jalouse ? J'en ai rien à faire de Noam !"

    iris gene "Euh... Enfin... C'est-C'est pas vraiment ce que je voulais dire."

    iris inquiet "Mais sinon, je suis sérieuse pour le reste. Si elle commence à devenir étrange, pars."
    noam fatigue "Je ferai attention."
    iris colere "Non, ça c'est ce que tu dis quand tu comptes faire exactement l'inverse."
    noam sourire "Je ferai très attention ?"
    iris blase "Tu m'épuises."

    "Elle retourne à son assiette en levant les yeux au ciel. Je profite du calme retrouvé pour manger, et pendant quelques minutes personne ne parle de vote, de brouilleurs ou de ce que j'ai pu voir dans les couloirs."
    "Elen, elle, continue de récupérer tout ce qui passe à portée de main avec une efficacité assez terrifiante."

    elen joie "Quelqu'un veut sa pomme ?"
    julian sourire "Tu viens d'en manger deux."
    mara sourire "Donnez-lui la pomme avant qu'elle commence à nous regarder comme hier."
    elen colere "J'allais pas vous manger !"
    julian taquin "C'est exactement ce que dirait quelqu'un qui allait nous manger."

    "Elen lui lance un morceau de pain. Julian l'évite de justesse avant de le ramasser sur la table."

    julian rire "Gaspillage ! Crime contre l'humanité après vingt-quatre heures de famine !"
    goumi "Je confirme."
    elen sourire "Mange-le alors."

    "Je termine mon assiette beaucoup plus vite que prévu. Mon ventre est plein pour la première fois depuis deux jours, mais la demande de Sael reste coincée quelque part au fond de ma tête."

    iris inquiet "Tu vas vraiment y aller ?"
    noam reflexion "Elle dit qu'elle sait quelque chose sur ce que j'ai vu."
    iris hesitation "Elle a surtout dit qu'elle voulait en parler. C'est pas pareil."
    noam fatigue "Je sais."
    iris inquiet "Alors si ça devient bizarre, tu pars."
    noam sourire "Tu me l'as déjà dit."
    iris colere "Et visiblement il faut répéter avec toi."

    "Je me lève avec mon plateau. Mara me regarde faire, puis pousse un léger soupir."

    mara agace "Noam."
    noam reflexion "Quoi ?"
    mara mefiant "Je pensais ce que j'ai dit. Mais... évite juste de refaire n'importe quoi demain."
    noam fatigue "Je vais essayer."
    mara agace "C'est déjà mieux que 'je sais pas'."

    elen joie "Et reviens manger ce soir !"
    elen sourire "Y'a encore plein de trucs !"
    noam sourire "Je note surtout que c'est ça qui t'inquiète."
    elen joie "Oui !"

    "Au moins, elle ne fait pas semblant."

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_74
    scene couloir_cafeteria at adaptive_fullscreen with dissolve

    "La porte se referme derrière moi et le bruit de la cafétéria disparaît presque d'un coup."
    "Je reste une seconde dans le couloir, hésitant encore à aller jusqu'à la chambre de Sael."

    think "Elle a peut-être vraiment vu quelque chose. Et si ce n'est pas le cas... Iris avait raison, je pars."

    jump _14_0_1_1_0_CHAMBRE_SAEL


label _14_0_1_1_0_CHAMBRE_SAEL:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_dortoir")
    scene bg_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_tension_debate.mp3" fadein 2.0

    "Je rejoins le dortoir quelques minutes plus tard. Plus j'approche de la chambre de Sael, moins son invitation me paraît être une bonne idée, mais si elle sait quelque chose sur ce que j'ai vu, je ne peux pas simplement l'ignorer."

    play sound sfx_knock volume 0.8

    "Je toque deux fois et la porte s'ouvre presque immédiatement."

    $ showGroup([
        ("noam", "inquiet", 0.35),
        ("sael", "mefiant", 0.70),
    ])

    sael mefiant "Tu es venu."
    noam reflexion "Tu m'as pas vraiment laissé penser que c'était facultatif."
    sael raison "Entre."
    noam inquiet "Tu voulais parler de ce que j'ai vu, alors parle."
    sael mefiant "Pas dans le couloir."

    "Je jette un coup d'œil derrière elle avant d'entrer à contrecœur."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre_sael") from _call_MAYBE_PLAY_SCRIPTED_DOOR_77
    scene bg_chambre_sael at adaptive_fullscreen with dissolve
    play sound sfx_door volume 0.8

    "La porte se referme derrière moi."

    $ showGroup([
        ("noam", "inquiet", 0.25),
        ("sael", "mefiant", 0.62),
    ])

    noam reflexion "Bon. Qu'est-ce que tu sais ?"
    sael raison "Avant ça, j'ai besoin que tu répondes à quelques questions."
    noam fatigue "Non. Tu m'as fait venir parce que tu savais quelque chose, alors soit tu parles, soit je pars."

    sael mefiant "Tu entends parfois des voix quand personne ne parle ?"
    noam colere "Sael..."
    sael raison "Réponds."
    noam colere "Non."
    sael mefiant "Des sons que personne d'autre n'entend ? Des moments dont tu ne te souviens pas ?"
    noam agace "J'ai dit non."

    "Je commence à comprendre où elle veut en venir."

    noam inquiet "C'est Ryn qui t'a demandé ça ?"

    "Sael ne répond pas tout de suite et son regard glisse brièvement vers la porte."

    noam colere "Putain..."

    "Je me retourne aussitôt et attrape la poignée."

    play sound sfx_door volume 0.8

    "La porte s'ouvre avant que je puisse la toucher."

    $ showGroup([
        ("noam", "surpris", 0.18),
        ("sael", "mefiant", 0.58),
        ("ryn", "colere", 0.86),
    ])

    ryn colere "Bouge pas."
    noam panique "Ryn ?!"
    noam colere "Vous vous foutez de moi ?!"

    "Je tente immédiatement de passer, mais Ryn se place devant moi."

    ryn colere "Tu restes deux minutes. Après, si elle a tort, tu repars."
    noam colere "Dégage."
    ryn colere "Noam..."
    noam colere "J'ai dit dégage."

    "Je pousse son épaule pour forcer le passage."

    play sound sfx_thud volume 1.0
    with hpunch

    "Ryn réagit immédiatement. Il m'attrape par le haut du torse, me retourne brutalement et me plaque dos contre le mur."

    noam panique "LÂCHE-MOI !"
    ryn colere "Arrête de bouger !"
    noam colere "Va te faire foutre !"

    "Je tente de repousser son bras mais il se colle contre moi pour m'empêcher de prendre appui, une main sur mon épaule et l'avant-bras appuyé sous ma clavicule."

    noam peur "Ryn, lâche-moi !"
    ryn colere "Tu te calmes deux minutes et je te lâche."
    noam colere "Je vais pas me calmer pendant que vous me retenez de force !"

    sael colere "Ryn, ne l'étrangle pas."
    ryn agace "Je l'étrangle pas."
    noam colere "Ah oui ? C'est super confortable !"

    "Sael s'approche de son bureau et récupère un petit sachet en tissu."

    noam inquiet "C'est quoi ?"
    sael neutre "Du sel."
    noam blase "Bien sûr."
    ryn agace "J'ai eu la même réaction."

    sael colere "Chez moi, on utilisait ça pour vérifier si quelqu'un avait ramené quelque chose des zones mortes."
    noam colere "J'en ai rien à foutre de tes histoires de fantômes."
    sael mefiant "Justement."

    "Elle ouvre le sachet et prend une poignée de sel."

    noam inquiet "Sael..."
    sael raison "Si j'ai tort, ça ne fera rien."
    noam colere "Alors teste-le sur toi."

    "Elle s'approche."

    noam panique "Ne me touche pas."

    "Je recommence à me débattre, mais Ryn resserre immédiatement sa prise."

    ryn colere "Arrête !"
    noam colere "LÂCHE-MOI !"

    "Sael me jette le sel directement sur le visage et le haut du torse."

    with vpunch

    noam panique "PUTAIN !"

    "Je ferme les yeux par réflexe tandis que les grains glissent dans mes cheveux, sous mon col et jusque sur mes lèvres."

    noam colere "T'es complètement malade !"
    sael determine "Regarde-moi."
    noam colere "Va te faire foutre."
    sael determine "Dis ton nom."
    noam colere "Non."

    sael determine "Noam, dis ton nom."
    noam colere "Tu le connais très bien."
    sael colere "DIS-LE !"
    noam panique "NON !"

    "Ryn souffle entre ses dents."

    ryn agace "Réponds juste et on avance."
    noam colere "Vous me plaquez contre un mur pour un exorcisme et c'est moi qui vous fais perdre du temps ?!"

    sael mefiant "Qui es-tu ?"
    noam colere "Quelqu'un qui va vous en coller une dès qu'il sera libre."

    "Sael reste parfaitement sérieuse."

    sael determine "Il faut qu'il boive."

    "Elle prend une petite fiole transparente posée sur son bureau."

    noam inquiet "Non."
    sael raison "C'est de l'eau."
    noam colere "J'ai dit non."
    sael determine "Ryn."

    noam panique "Ryn, ne fais pas ça."

    "Il hésite une fraction de seconde, puis déplace sa main jusqu'à ma mâchoire."

    noam peur "Me touche pas !"

    "Je tourne la tête, mais il la bloque contre le mur."

    ryn colere "Ouvre la bouche."
    noam colere "Va te faire foutre."

    "Je serre les dents. Ryn pince alors brutalement mon nez."

    noam panique "Mmh !"

    "Je retiens ma respiration en essayant encore de me dégager, mais après quelques secondes mes poumons commencent à brûler."

    noam peur "Mmh..."

    "Je finis par entrouvrir la bouche pour reprendre de l'air."

    ryn colere "Maintenant."

    "Sael approche aussitôt la fiole et verse de l'eau entre mes lèvres."

    noam panique "MMPH !"

    "J'essaie de recracher, mais Ryn maintient ma mâchoire relevée. Une partie coule sur mon menton tandis que j'avale le reste par réflexe."

    ryn colere "Voilà."

    "Il libère mon nez et je prends brutalement une grande inspiration."

    play sound sfx_breath volume 1.0

    noam panique "HAA— PUTAIN !"
    noam colere "BANDE DE TARÉS !"

    sael inquiet "Est-ce que tu sens quelque chose ?"
    noam colere "Oui ! J'ai envie de vous casser la gueule !"

    "Sael m'observe, attentive au moindre mouvement."

    sael raison "Tu entends quelque chose ?"
    noam colere "J'entends surtout vos conneries."

    stop music

    play sound sfx_breath volume 1.0
    scene black with vpunch

    $ showGroup([
        ("noam", "panne_creep", 0.25),
    ])

    pause 0.2

    "Un cri me traverse soudainement la tête, net et violent, comme si quelqu'un venait de hurler directement derrière mes yeux."

    scene bg_chambre_sael at adaptive_fullscreen with hpunch
    play music "music/bgm_tension_debate.mp3" fadein 0.5

    $ showGroup([
        ("noam", "peur", 0.18),
        ("sael", "mefiant", 0.58),
        ("ryn", "inquiet", 0.86),
    ])

    noam panique "AAH !"
    ryn inquiet "Quoi ?!"
    noam peur "Vous avez pas entendu ?!"
    sael mefiant "Entendu quoi ?"
    noam panique "LE CRI !"

    "Ils se regardent."

    ryn inquiet "Y'a eu aucun cri."
    noam peur "Si ! Je l'ai entendu !"
    sael determine "D'où il venait ?"
    noam colere "J'en sais rien ! Arrête de me regarder comme ça !"

    play sound sfx_static volume 0.8

    "Le néon grésille brutalement au-dessus de nous."

    "Sael lève les yeux une seconde avant de revenir vers moi."

    noam panique "C'est le néon ! Ils font ça tout le temps ici !"
    ryn inquiet "Sael..."
    sael mefiant "Dis ton nom."

    noam colere "Non."
    sael determine "Noam."
    noam panique "ARRÊTE !"
    sael colere "Dis ton nom !"
    noam colere "NOAM ! CONTENTE ?!"

    play sound sfx_glitch volume 1.0
    with vpunch

    "Le son se déforme une fraction de seconde. Sael se fige aussitôt."

    noam peur "Quoi ?"
    ryn inquiet "Sael ?"
    sael mefiant "..."

    noam panique "QU'EST-CE QU'IL Y A ?!"
    sael determine "Encore."
    noam colere "Non."
    sael determine "Dis-le encore."
    noam panique "J'AI DIT NON !"

    "Je recommence à me débattre de toutes mes forces."

    play sound sfx_thud volume 0.9
    with hpunch

    "Mon épaule frappe violemment le mur."

    ryn colere "Arrête, putain !"
    noam panique "LÂCHE-MOI !"
    sael determine "Ryn, tiens-le encore une seconde."
    ryn inquiet "Ça suffit, Sael."
    sael colere "Tu n'as pas vu sa réaction !"
    ryn colere "Il panique parce qu'on le tient contre un mur depuis cinq minutes !"

    noam colere "ENFIN !"

    "Ryn tourne brièvement la tête vers elle."

    "Sa prise se relâche juste assez."

    think "Maintenant."

    "Je ramène brutalement mon genou et l'enfonce de toutes mes forces dans son abdomen."

    play sound sfx_thud volume 1.0
    with hpunch

    ryn surpris "GH—!"

    "Ryn se plie en deux et sa prise disparaît."

    noam colere "DÉGAGE !"

    "Je le repousse et fonce immédiatement vers la porte."

    sael surpris "Noam !"
    ryn colere "Putain... arrête-le !"
    noam panique "RESTEZ LOIN DE MOI !"

    play sound sfx_door volume 1.0

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_79
    scene couloir_dortoir at adaptive_fullscreen with hpunch

    "Je sors en courant et claque la porte derrière moi sans même vérifier s'ils me suivent."

    sael inquiet "Noam !"

    "Je continue."

    sael raison "Si tu entends encore le cri..."

    "Je ralentis malgré moi."

    sael triste "Ne lui réponds pas."

    noam panique "VA TE FAIRE FOUTRE !"

    "Je repars aussitôt vers ma chambre, la gorge douloureuse, encore couvert de sel et avec le goût de l'eau forcée dans la bouche."

    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_80
    scene bg_chambre at adaptive_fullscreen with fade
    stop music fadeout 2.0

    "Je ferme la porte à clé et reste appuyé contre elle plusieurs secondes, incapable de ralentir ma respiration."

    "Quand je passe une main dans mes cheveux, quelques grains de sel tombent encore sur le sol."

    think "Ils sont complètement fous."

    pause 0.5

    think "Alors pourquoi j'ai entendu ce cri ?"

    pause 2.0

    call show_custom_title("Plus tard dans l'après-midi") from _call_show_custom_title_3

    jump _14_0_1_1_0_MESSAGES_KAEL


label _14_0_1_1_0_MESSAGES_KAEL:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 2.5

    "Je suis toujours dans ma chambre quand ma tablette vibre sur le bureau."
    "Pendant une seconde, je pense l'ignorer. Puis je vois le nom de Kael."

    kael "Noam ? T'es là ?"
    noam "Ouais."
    kael "Question bizarre : Ryn t'a parlé aujourd'hui ?"

    "Je fixe le message un peu trop longtemps."

    noam "On peut dire ça."
    kael "Il vient encore de m'engueuler dans le couloir. Apparemment je suis toujours officiellement responsable de la fin du monde parce que j'ai voté contre."
    noam "Bienvenue au club."
    kael "Toi c'est différent. Toi t'as une secte maintenant."

    "Je fronce les sourcils."

    noam "Comment tu sais ?"
    kael "Mara. Donc techniquement tout le Conclave sait probablement déjà."
    noam "Génial."
    kael "C'est vrai ? Sael t'a vraiment sorti du sel ?"
    noam "Oui."
    kael "Putain."
    noam "Ryn était là aussi."
    kael "PUTAIN."

    "Malgré moi, je souris légèrement."

    kael "Ils t'ont fait quoi ?"
    noam "J'ai pas vraiment envie d'en parler."
    kael "Ok."

    "Il ne relance pas. Ça me surprend presque."

    kael "Je voulais surtout te parler de demain."
    noam "Le vote sur ARCHIVE ?"
    kael "Ouais."
    kael "Je vais profiter du vote pour aller voir les terminaux d'archives pendant que tout le monde sera à la Salle du Conclave."
    noam "Tu peux déjà accéder aux images ?"
    kael "Pas normalement. Mais demain, pendant la synchronisation liée au vote, les terminaux vont devoir charger les index complets d'ARCHIVE."
    kael "Je veux essayer de récupérer ce qui concerne ma chambre avant que les droits se referment ou que quelqu'un décide encore de supprimer quelque chose."

    "Je me redresse."

    noam "Les images du jour 8."
    kael "Exactement."
    noam "Celles du vol de la photo de Léa."
    kael "Oui."

    "Je regarde vers mon bureau. Le cahier noir est toujours là, fermé."

    noam "Je viens avec toi."

    pause 0.4

    kael "T'es sûr ?"
    noam "Oui."
    kael "Je pensais que tu voudrais assister au vote."
    noam "J'ai surtout envie de savoir qui entre dans nos chambres."
    kael "... Je peux difficilement te contredire là-dessus."

    noam "On se retrouve où ?"
    kael "Près de la salle d'observation. 13h30."
    kael "Je t'envoie un message avant pour vérifier que le couloir est vide."
    noam "Ça marche."

    "Quelques secondes passent avant qu'un nouveau message apparaisse."

    kael "Au fait, pour ce que Ryn m'a dit..."
    noam "Quoi ?"
    kael "Il pense vraiment que j'ai sacrifié les brouilleurs juste pour ma sœur."
    noam "C'est pas complètement faux, non ?"
    kael "Merci pour le soutien."
    noam "Je veux dire que je comprends pourquoi tu l'as fait."
    kael "Ouais."
    kael "Je sais pas si toi t'as raison sur tout ce qui se passe ici. Mais je sais ce que ça fait quand les autres décident que ton problème compte moins que le leur."

    "Je relis la phrase."

    noam "C'est probablement le truc le plus gentil que quelqu'un m'a dit depuis deux jours."
    kael "C'est triste."
    noam "Très."
    kael "Bon, alors demain on fait notre petite sortie entre parias."
    noam "Dit comme ça, ça donne presque envie."
    kael "Presque."

    "La conversation s'arrête là. Je repose la tablette sur le lit."
    "Je ne sais pas si Kael me croit réellement. Je ne suis même pas sûr d'avoir besoin qu'il me croie. Pour l'instant, il veut les mêmes réponses que moi, et c'est déjà beaucoup."

    pause 1.5

    jump _14_0_1_1_0_FIN_JOURNEE


label _14_0_1_1_0_FIN_JOURNEE:

    scene bg_chambre at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 3.0

    "La journée se termine sans que je ressorte de ma chambre. J'ai largement assez vu de monde pour aujourd'hui."
    "Je reste un moment assis au bureau à regarder mes notes, puis mon regard revient encore une fois vers le cahier noir."

    "Je l'ouvre à la page du dessin de Juliette."

    pause 0.6

    "La copie est toujours là. Les mêmes traits, le même visage, ce sourire qui me dérange sans que j'arrive vraiment à comprendre pourquoi."
    "Je la compare de mémoire au dessin original. J'ai passé assez de temps dessus pour connaître presque chaque ligne."

    think "Il y a quelque chose qui ne colle pas."

    "Je rapproche le cahier de la lampe."
    "Les cheveux, les yeux, le nez... tout est presque exactement comme je l'avais dessiné."
    "Puis je remarque une petite marque sous sa mèche, juste au-dessus du sourcil."

    "Je reste immobile."

    think "Non."

    "Je passe doucement le doigt dessus. Ce n'est pas une tache ni une rayure du papier. Quelqu'un l'a dessinée volontairement."

    think "Cette cicatrice..."

    "Juliette l'avait depuis l'enfance. Une toute petite ligne pâle qu'on voyait seulement quand ses cheveux étaient repoussés sur le côté."
    "Je ne l'avais jamais mise sur mon dessin. Sa mèche la cachait complètement."

    pause 0.8

    think "Je n'avais pas dessiné ça."

    "Je tourne rapidement la page, puis reviens en arrière comme si le détail pouvait disparaître. Il est toujours là."
    "Quelqu'un a copié mon dessin. Mais cette personne a ajouté quelque chose qu'elle ne pouvait pas voir dessus."

    "Je referme le cahier d'un coup."

    play sound sfx_thud volume 0.6

    "Mon regard part vers la porte, puis vers les murs de la chambre. Je sais que c'est absurde, mais pendant quelques secondes j'ai vraiment l'impression que quelqu'un pourrait être là, juste hors de mon champ de vision."

    think "Comment tu peux savoir ça ?"

    "Aucune réponse. Évidemment."

    "Je range le cahier dans le tiroir et le ferme, cette fois à clé."

    scene bg_cg012 at adaptive_fullscreen with fade

    "Je me couche sans me changer et tire la couverture jusqu'au menton. Demain, Kael et moi devons aller voir les images d'ARCHIVE."
    "Pour la première fois depuis plusieurs jours, j'ai au moins quelque chose de concret à faire."

    think "Demain, je veux une preuve. N'importe laquelle."

    "Je ferme les yeux."

    pause 1.0

    think "Parce que si je n'en trouve pas... je vais finir par croire Sael."

    pause 2.5

    scene black with fade
    stop music fadeout 4.0

    call end_day("15") from _call_end_day_15
    jump _15_0_1_1_0_REVEIL_CHAMBRE
