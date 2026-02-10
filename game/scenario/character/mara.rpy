# -----------------------------------------------------------------------
# LIENS — MARA
# -----------------------------------------------------------------------

default mara_link = 0


label MARA_LINK_INTERACT:

    menu:
        "Passer du temps avec Mara ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if mara_link == 0:
        jump mara_link_1
    elif mara_link == 1:
        jump mara_link_2
    elif mara_link == 2:
        jump mara_link_3
    elif mara_link == 3:
        jump mara_link_4
    elif mara_link == 4:
        jump mara_link_5

    if last_room_label:
        jump expression last_room_label
    return


label mara_link_1:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "sourire", 0.60)
    $ showP("noam", "reflexion", 0.22)

    mara sourire "Tiens, toi."
    mara taquin "T'es venu pour le café ou pour les ragots ?"

    "Elle appuie sur la machine en me fixant."

    mara sourire "Tu sens ?"
    mara neutre "Le café ici n'a pas d'âme."
    mara taquin "On dirait du jus de chaussette premium."

    noam taquin "Pourquoi tu es difficile à satisfaire ?"

    mara taquin "Je suis exigeante."
    mara neutre "Pas chiante. Exigeante."
    mara sourire "Je plaisante."
    mara taquin "Enfin… pas complètement."

    noam "Et... Qu'est ce que tu préfères ?"

    mara taquin "Les ragots, c'est plus nourrissant."
    mara sourire "Mais le café fait mieux semblant."

    "Elle rit vite, puis regarde autour."

    mara sourire "Tu sais quoi ?"
    mara neutre "J'arrive à sonder les gens à leur façon de tenir leur tasse."

    noam taquin "Ah oui ? Et ça dit quoi de moi ?"

    mara taquin "Que tu hésites."
    mara neutre "Tu tiens la chaleur, mais pas trop près."

    mara taquin "Tu te caches ou tu assumes ?"

    noam "Je suis pourtant juste là.."

    mara neutre "Juste là, ça n'existe pas."
    mara taquin "Tout le monde te voit."

    "Elle me tend un gobelet, sans attendre de merci."

    mara neutre "Tu sais, avant, on ne me laissait jamais traîner dans une cafét'."
    mara fatigue "On me disait que ça faisait mauvais genre."

    noam "Qui te disait ça ?."

    mara neutre "Mon père."
    mara neutre "Ses conseillers."
    mara taquin "Tous ceux qui flippaient que je sois trop vraie."
    mara taquin "... Trop authentique, quoi."

    "Elle mime des guillemets avec ses doigts."

    mara neutre "Alors j'ai appris à jouer."
    mara sourire "Sourire quand il faut."
    mara taquin "Rire quand ça les arrangeait."

    "Alors comme ça tu aimes jouer ? C'est à dire ?."

    mara sourire "J'aime gagner."
    mara taquin "Et surtout j'aime qu'on me regarde gagner."

    "Elle remue son café, puis me regarde d'un air curieux."

    mara taquin "Tu me mates pour quoi, toi ?"
    mara taquin "Qu’est-ce qui peut bien t’intéresser chez une fille comme moi ?"

    "Elle m'intimide légèrement."
    noam "Hein ?!"
    noam "Je veux surtout comprendre..."

    mara neutre "Comprendre quoi ?"
    mara taquin "Le costume ?"
    mara neutre "Ou qui est la personne personne là-dessous ?"

    "Elle penche la tête et montre sa poitrine du bout de son doigt."

    mara taquin "Fais gaffe, la personne dessous est un peu moins controlable."
    mara joie "Heureusement pour toi, de grandes responsabilités me réfrennent..."

    noam "Et ces grandes responsabilités, elles sont ici dans cette pièce ?"

    "Elle éclate de rire l'espace d'un instant."

    mara sourire "Ah putain, je t’aime bien toi."
    mara sourire "Malheureusement oui, elles sont toujours collées à mes escarpins !"
    mara neutre "Je préférais quand on m'appelait 'petite'."
    mara taquin "Ça faisait gentil et je pouvais davantage m'amuser."

    "Elle prend une gorgée, plus lente."

    mara neutre "J'étais la petite vitrine adorée de ma famille."
    mara taquin "Enfin, sauf quand j'avais envie d'entrer dans le magasin et de faire chauffer la CB !"

    "Elle boit, grimace légèrement."

    mara fatigue "Oui, une petite vitrine bien pratique ..."

    noam "Ici tu pourrais presque être qui tu veux.."

    mara neutre "Ah ! Drole d'idée, on ne peut pas être qui on veut quand on est observé par des millions de gens."
    mara fatigue "Pas quand on est une des têtes d'affiche du principal évènement mondial."

    "Elle sourit, plus doux, puis claque son gobelet sur la table."

    mara sourire "Bon. Enfin, on pourra pas refaire le monde..."
    mara taquin "On a eu notre moment sérieux."

    "Elle imite une fois encore des guillemets avec ses doigts."
    "Je ris. Elle aussi."
    "Elle lève son gobelet comme un toast."
    "Je fais pareil."
    "Le geste est simple, mais complice."
    "Elle sourit, elle semble s'être amusée durant ces quelques minutes."

    $ mara_link = 1

    jump FREE_TIME_END


label mara_link_2:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)
    $ showP("noam", "reflexion", 0.22)

    mara neutre "Tomas fait toujours semblant de ne rien écouter."
    mara neutre "Elen se croit invisible."
    mara taquin "Et Kael…"

    "Elle s'interrompt, puis sourit en coin."

    mara taquin "Kael joue au chef."
    mara sourire "Ça lui va bien."

    "Je lui demande si elle a un rôle, elle aussi."

    mara taquin "Moi ?"
    mara colere "Je mets le feu."
    mara sourire "Je regarde qui danse."

    "Elle croise les jambes et prend un ton plus léger."

    mara sourire "C'est mon truc."
    mara taquin "Quand tout le monde se cache, je fais du bruit."
    mara neutre "Je tire les gens dehors."

    "Je lui demande si elle aime vraiment le bruit."

    mara neutre "Le bruit couvre les silences."
    mara fatigue "Et les silences, ça fait peur."

    "Je lui demande ce qu'elle entend dans le silence."

    mara neutre "Moi."
    mara fatigue "Et ça, c'est compliqué."

    "Je lui demande si elle ne craint pas les retours."

    mara taquin "Je les provoque."
    mara colere "Comme ça, au moins, c'est moi qui décide."

    "Elle joue avec une mèche de cheveux."

    mara sourire "Tu sais ce qui est drôle ?"
    mara neutre "Tout le monde me croit sûre de moi."

    "Je lui dis que c'est l'impression qu'elle donne."

    mara neutre "Impression, voilà."
    mara fatigue "À la maison, c'était mon travail."
    mara neutre "Donner la bonne impression."

    "Je lui demande comment c'était."

    mara neutre "Des dîners, des visages, des sourires programmés."
    mara fatigue "On te demande d'être parfaite sans jamais transpirer."

    "Elle lève les yeux au plafond."

    mara taquin "Même l'eau devait être élégante."
    mara sourire "Tu imagines ?"

    "Elle rit, mais le son est plus court."

    mara taquin "Alors j'ai décidé de transpirer en public."
    mara sourire "Et de dire que j'aime ça."

    "Je lui demande si c'est vrai."

    mara neutre "Parfois."
    mara fatigue "Parfois non."

    "Elle se penche vers moi."

    mara taquin "La vérité, c'est que j'aime qu'on me suive."
    mara colere "Pas qu'on me tienne."

    "Je lui demande si elle a déjà été tenue."

    mara fatigue "Tout le temps."
    mara neutre "C'est ça, être héritière."

    "Elle recule, reprend une posture de façade."

    mara sourire "Mais ici, on fait semblant d'être libres."
    mara taquin "Alors j'en profite."

    "Je remarque un regard qui cherche la réaction."

    mara neutre "Tu vois ?"
    mara taquin "Je te regarde pour savoir si je vais trop loin."

    "Je lui dis qu'elle décide."

    mara sourire "Non."
    mara taquin "Je teste."
    mara neutre "C'est différent."

    "Elle claque des doigts."

    mara taquin "On dirait un concours, non ?"
    mara sourire "Qui tiendra la scène le plus longtemps."

    "Je lui demande si ça l'amuse."

    mara neutre "Ça m'occupe."
    mara fatigue "Et ça me rassure."

    "Je lui demande si elle a déjà perdu la scène."

    mara fatigue "Une fois."
    mara neutre "J'avais dix-sept ans."
    mara fatigue "Je me suis enfermée dans les toilettes d'une gala."
    mara neutre "Personne ne l'a su."

    "Elle se redresse, masque revenu."

    mara sourire "Allez."
    mara taquin "On va les rendre jaloux deux minutes."

    "Elle me lance un clin d'œil rapide."
    "Elle attend ma réaction."
    "Je hausse les épaules."
    "Elle rit."

    $ mara_link = 2

    jump FREE_TIME_END


label mara_link_3:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "colere", 0.60)
    $ showP("noam", "reflexion", 0.22)

    mara colere "Tu sais ce qui m'agace ?"
    mara colere "Les gens qui pensent qu'ils peuvent me contredire devant tout le monde."

    "Elle tapote la table, rapide."

    mara colere "Comme si j'étais un décor."
    mara colere "Comme si je devais sourire et dire merci."

    "Je lui demande qui a fait ça."

    mara neutre "Peu importe."
    mara colere "Ce qui compte, c'est le geste."

    "Elle serre sa tasse, puis la repose trop fort."

    mara colere "Je sais me défendre."
    mara fatigue "Mais je déteste devoir le faire."

    "Elle expire, puis force un sourire."

    mara neutre "C'est rien."
    mara fatigue "Juste une mauvaise journée."

    "Je lui dis que ça a l'air de compter."

    mara neutre "Oui."
    mara colere "Parce que je suis censée être intouchable."

    "Elle me fixe."

    mara fatigue "Et quand on touche, ça fait mal."

    mara neutre "Tu sais, quand tu grandis dans un salon plein de gens puissants,"
    mara fatigue "tu apprends à ne jamais perdre la face."

    "Elle s'adosse, plus vulnérable."

    mara fatigue "Sauf que parfois, tu voudrais juste dire :"
    mara colere "Laisse-moi tranquille."

    "Je lui demande si elle le dit."

    mara taquin "Je le dis autrement."
    mara colere "Je pique."
    mara sourire "Je souris."
    mara colere "Je coupe."

    "Elle mime un coup de ciseaux."

    mara neutre "Ça marche."
    mara fatigue "Mais ça laisse des traces."

    "Je lui demande lesquelles."

    mara neutre "Les gens ne savent pas si je suis une amie ou une menace."
    mara fatigue "Et moi, je ne sais pas si je veux choisir."

    "Je lui demande si elle voudrait parfois être juste une amie."

    mara neutre "Oui."
    mara fatigue "Mais il faut de la confiance."

    "Elle rit, mais le son est plus bas."

    mara sourire "Tu sais ce qui est ironique ?"
    mara neutre "On me reproche d'être trop sûre de moi."

    "Je lui demande si ce n'est pas son choix."

    mara neutre "C'est un rôle."
    mara taquin "Un costume."
    mara fatigue "Tu le portes assez longtemps, tu oublies que ça serre."

    "Elle reprend un ton vif."

    mara colere "Et quand quelqu'un me contredit,"
    mara fatigue "j'ai l'impression qu'il tire sur les coutures."

    "Je lui demande ce qu'elle fait quand ça craque."

    mara taquin "Je fais une blague."
    mara fatigue "Ou je pars."

    "Elle baisse la voix."

    mara fatigue "Et je m'en veux après."

    "Je lui demande si elle revient vers les gens."

    mara neutre "Si je peux."
    mara fatigue "Si j'ose."

    "Je lui dis qu'elle peut rester, si elle veut."

    mara neutre "Rester, c'est intime."
    mara taquin "Tu veux vraiment ça ?"

    "Je n'ai pas le temps de répondre."

    mara sourire "T'inquiète."
    mara taquin "Je te taquine."
    mara sourire "Enfin… pas complètement."

    "Elle se penche en avant."

    mara neutre "Merci d'écouter."
    mara fatigue "C'est rare."

    "Je lui dis que ce n'est pas un effort."

    mara taquin "Ne t'habitue pas trop."
    mara colere "Je redeviens vite piquante."

    "Elle se redresse, masque retrouvé."

    mara sourire "Bon, assez de drama."
    mara taquin "On va se faire un autre café."

    "Elle souffle, puis lève les yeux au ciel."
    "Son sourire revient par réflexe."
    "Elle me pousse gentiment du coude."
    "La tension retombe."

    $ mara_link = 3

    jump FREE_TIME_END


label mara_link_4:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)
    $ showP("noam", "reflexion", 0.22)

    mara neutre "Tu sais, la réputation, c'est un costume."
    mara neutre "On le porte parce que tout le monde regarde."
    mara fatigue "Et quand on l'enlève, il n'y a plus personne."

    "Elle laisse la phrase flotter."

    mara neutre "Je préfère qu'on sache à quoi s'attendre."
    mara taquin "Alors je donne une version claire."

    "Je lui demande si cette version lui ressemble."

    mara neutre "Un peu."
    mara sourire "Assez pour être crédible."
    mara fatigue "Pas assez pour me blesser."

    "Elle tapote son genou, impatiente."

    mara neutre "Je connais par cœur les attentes."
    mara neutre "La bonne tenue."
    mara taquin "La bonne phrase."

    "Je lui demande si elle a déjà dérapé."

    mara neutre "Une fois."
    mara colere "J'ai dit ce que je pensais."
    mara fatigue "On m'a dit que c'était \"maladroit\"."

    "Elle hausse les épaules, faussement légère."

    mara colere "Maladroit, c'est leur mot pour \"vrai\"."

    mara neutre "Quand j'étais petite, je voulais chanter."
    mara fatigue "Mon père disait que c'était un hobby."

    "Je lui demande ce qu'elle en a fait."

    mara sourire "Je chante quand je suis seule."
    mara neutre "Ça ne compte pas, donc ça fait du bien."

    "Elle rit, puis se mord la lèvre."

    mara taquin "C'est bizarre, non ?"
    mara fatigue "Garder ce qui est vrai pour la nuit."

    mara neutre "Tu vois, c'est ça."
    mara neutre "Je garde des trucs pour moi."

    "Je lui demande si ça lui pèse."

    mara fatigue "Parfois."
    mara neutre "Surtout quand tout le monde pense me connaître."

    "Elle se penche vers moi."

    mara neutre "Je me suis entraînée à marcher, à parler, à sourire."
    mara fatigue "À dire 'oui' sans le penser."

    "Je lui demande quand elle a dit non."

    mara sourire "Le jour où j'ai pris un train seule."
    mara taquin "C'était bête."
    mara neutre "Mais j'ai respiré pour la première fois."

    "Je lui demande si quelqu'un l'a su."

    mara neutre "Non."
    mara sourire "Et c'est ce qui l'a rendu parfait."

    "Elle pose la main sur son ventre comme pour revivre l'instant."

    mara taquin "Ici, je rejoue ça."
    mara sourire "Je prends des trains imaginaires."

    "Je lui demande si elle a peur du regard des autres."

    mara neutre "J'en ai besoin."
    mara fatigue "Et j'en ai peur."
    mara neutre "C'est contradictoire."

    "Elle hausse les épaules."

    mara taquin "Je suis faite de contradictions."
    mara neutre "C'est aussi pour ça qu'ils m'ont élevée."

    "Je lui demande ce qu'elle veut vraiment."

    mara neutre "Qu'on me laisse choisir."
    mara sourire "Et qu'on me regarde choisir."

    "Je lui demande si elle a peur de décevoir."

    mara fatigue "Toujours."
    mara neutre "Mais je déçois quand même."

    "Elle sourit, comme si elle se moquait d'elle-même."

    mara taquin "Tu vois ?"
    mara fatigue "Même mes désirs sont un spectacle."

    "Je lui dis qu'elle peut en sortir."

    mara neutre "Je peux."
    mara fatigue "Mais je reviens toujours."

    "Je lui demande pourquoi."

    mara neutre "Parce que j'ai besoin d'un public."
    mara taquin "Même quand je dis le contraire."

    "Elle s'allonge un instant, puis se relève d'un coup."

    mara sourire "Désolée."
    mara fatigue "Je deviens trop sérieuse."
    mara taquin "C'est mauvais pour l'image."

    "Elle lisse sa robe imaginaire."
    "Puis elle éclate de rire."
    "Son rire chasse le silence."
    "Elle cligne des yeux, amusée."

    $ mara_link = 4

    jump FREE_TIME_END


label mara_link_5:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "fatigue", 0.60)
    $ showP("noam", "reflexion", 0.22)

    "La cafétéria se vide."
    "Elle laisse tomber ses épaules une seconde."

    mara fatigue "Je joue un rôle."
    mara neutre "C'est plus simple que d'expliquer."

    "Je lui demande si elle sait qui elle serait sans."

    mara neutre "Je l'apprends."
    mara fatigue "Je la cherche."

    "Elle regarde la lumière des néons."

    "Son regard hésite une seconde."

    mara fatigue "Tu sais ce qui me fait peur ?"
    mara neutre "Qu'on m'oublie quand je ne brille pas."

    "Je lui dis qu'elle n'a pas besoin de briller tout le temps."

    mara neutre "Oui."
    mara fatigue "Et pourtant, je continue."

    "Elle serre son gobelet."

    mara fatigue "Si je m'arrête, j'ai l'impression de disparaître."
    mara neutre "Comme si je n'étais plus utile."

    "Je lui dis qu'elle n'a pas besoin d'être utile."

    mara colere "Essaie de dire ça à mon père."

    mara neutre "Quand j'étais petite,"
    mara neutre "on me mettait dans des robes trop belles."
    mara fatigue "On me disait 'ne fais pas de taches'."

    "Elle ricane."

    mara fatigue "Alors j'ai appris à ne pas respirer trop fort."

    "Je lui demande si elle a déjà fait une tache exprès."

    mara taquin "Oui."
    mara sourire "Du vin rouge."
    mara taquin "C'était ma petite révolution."

    "Je lui demande si elle respire ici."

    mara neutre "Plus."
    mara fatigue "Mais pas assez."

    "Elle relève la tête, comme si elle voulait défier quelqu'un."

    mara neutre "Je suis bonne pour faire semblant."
    mara sourire "C'est utile."
    mara fatigue "Mais ça fatigue."

    "Je lui demande si elle a quelqu'un en qui elle a confiance."

    mara neutre "Rarement."
    mara taquin "Je teste."
    mara colere "Je provoque."

    "Elle grimace."

    mara fatigue "Et parfois je blesse sans vouloir."

    "Je lui demande si elle regrette."

    mara fatigue "Souvent."
    mara neutre "Surtout quand la personne ne revient pas."

    "Elle se tait, puis ajoute, presque pour elle."

    mara colere "Je ne supporte pas d'être ignorée."
    mara fatigue "Même quand je dis que je m'en fiche."

    "Je lui dis que c'est humain."

    mara neutre "Ouais."
    mara fatigue "Mais chez moi, on n'avait pas le droit d'être 'humain'."

    "Elle éclate d'un rire bref."

    mara neutre "Tu sais, mon père disait :"
    mara colere "On représente."

    "Elle fait une pause."

    mara fatigue "Moi, je veux qu'on me voie."
    mara colere "Pas qu'on voie le logo."

    "Je lui demande ce qu'elle ferait sans logo."

    mara sourire "Je voyagerais."
    mara taquin "Je danserais."
    mara sourire "Je dormirais trop tard."

    "Elle regarde sa tasse vide."

    mara neutre "Quand quelqu'un me parle franchement,"
    mara fatigue "j'ai envie d'y croire."
    mara fatigue "Et ça m'effraie."

    "Je lui demande pourquoi."

    mara neutre "Parce que si j'y crois,"
    mara fatigue "je deviens loyale."
    mara colere "Et je ne sais pas faire semblant avec ça."

    "Elle souffle, puis relève la tête."

    mara sourire "Bon."
    mara taquin "Assez parlé."
    mara sourire "On va faire semblant que tout va bien."

    "Elle sourit, et cette fois le sourire est plus vrai."
    "Elle attend une seconde, comme si elle hésitait."
    "Puis elle se lève."
    "Le masque revient, mais moins rigide."

    $ mara_link = 5

    jump FREE_TIME_END
