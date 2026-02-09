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

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "sourire", 0.60)

    mara "Tiens, toi."
    mara "T'es venu pour le café ou pour les ragots ?"

    "Elle appuie sur la machine en me fixant."

    mara "Tu sens ?"
    mara "Le café ici n'a pas d'âme."

    "Je lui demande si elle est difficile."

    mara "Je suis exigeante."
    mara "C'est différent."

    mara "Je plaisante."
    mara "Enfin… pas complètement."

    "Je lui demande ce qu'elle préfère."

    mara "Les ragots, c'est plus nutritif."
    mara "Mais le café fait mieux semblant."

    "Elle rit vite, puis regarde autour."

    mara "Tu sais quoi ?"
    mara "Je reconnais les gens à leur façon de tenir leur tasse."

    "Je lui demande ce que ça dit de moi."

    mara "Que tu hésites."
    mara "Tu tiens la chaleur, mais pas trop près."

    mara "Tu te caches ou tu assumes ?"

    "Je lui dis que je suis juste là."

    mara "Juste là, ça n'existe pas."
    mara "Tout le monde te voit."

    "Elle me tend un gobelet, sans attendre de merci."

    mara "Tu sais, avant, on ne me laissait jamais traîner dans une cafét'."
    mara "On me disait que ça faisait mauvais genre."

    "Je lui demande qui lui disait ça."

    mara "Mon père."
    mara "Ses conseillers."
    mara "Les gens qui ont peur que je sois "
    mara "trop vraie."

    "Elle mime des guillemets avec ses doigts."

    mara "Alors j'ai appris à jouer."
    mara "Sourire quand il faut."
    mara "Rire quand ça arrange."

    "Je lui demande si elle aime jouer."

    mara "J'aime gagner."
    mara "Et j'aime qu'on me regarde gagner."

    "Elle remue son café, puis me regarde d'un air curieux."

    mara "Tu me regardes pour quoi, toi ?"

    "Je dis que je veux comprendre."

    mara "Comprendre quoi ?"
    mara "Le costume ?"
    mara "Ou la personne dessous ?"

    "Elle penche la tête."

    mara "Fais gaffe, la personne dessous est moins pratique."

    "Je lui demande comment elle s'appelait avant le costume."

    mara "Toujours Mara."
    mara "Mais on me disait 'petite'."
    mara "Ça faisait gentil."

    "Elle prend une gorgée, plus lente."

    mara "J'étais la vitrine."
    mara "Sauf que j'avais envie d'entrer dans le magasin."

    "Elle hausse les épaules."

    mara "J'ai arrêté d'être gentille quand j'ai compris que ça me rendait invisible."

    "Je lui demande si elle se sent invisible, ici."

    mara "Non."
    mara "Je suis tout."
    mara "Trop visible."

    "Elle boit, grimace légèrement."

    mara "Ça ne veut pas dire qu'on me voit vraiment."

    "Je lui demande ce qu'elle voudrait qu'on voie."

    mara "Quelqu'un qui peut tomber et se relever."
    mara "Pas une affiche."

    "Elle sourit, plus doux, puis claque son gobelet sur la table."

    mara "Bon."
    mara "On a eu notre moment sérieux."
    mara "Maintenant tu me dois un vrai ragot."

    "Je lui dis que je n'en ai pas."

    mara "Alors invente."
    mara "C'est ça, la vie mondaine."

    "Je ris. Elle aussi."
    "Elle lève son gobelet comme un toast."
    "Je fais pareil."
    "Le geste est simple, mais complice."
    "Elle sourit, satisfaite."

    $ mara_link = 1

    jump FREE_TIME_END


label mara_link_2:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)

    mara "Tomas fait toujours semblant de ne rien écouter."
    mara "Elen se croit invisible."
    mara "Et Kael…"

    "Elle s'interrompt, puis sourit en coin."

    mara "Kael joue au chef."
    mara "Ça lui va bien."

    "Je lui demande si elle a un rôle, elle aussi."

    mara "Moi ?"
    mara "Je mets le feu."
    mara "Je regarde qui danse."

    "Elle croise les jambes et prend un ton plus léger."

    mara "C'est mon truc."
    mara "Quand tout le monde se cache, je fais du bruit."
    mara "Je tire les gens dehors."

    "Je lui demande si elle aime vraiment le bruit."

    mara "Le bruit couvre les silences."
    mara "Et les silences, ça fait peur."

    "Je lui demande ce qu'elle entend dans le silence."

    mara "Moi."
    mara "Et ça, c'est compliqué."

    "Je lui demande si elle ne craint pas les retours."

    mara "Je les provoque."
    mara "Comme ça, au moins, c'est moi qui décide."

    "Elle joue avec une mèche de cheveux."

    mara "Tu sais ce qui est drôle ?"
    mara "Tout le monde me croit sûre de moi."

    "Je lui dis que c'est l'impression qu'elle donne."

    mara "Impression, voilà."
    mara "À la maison, c'était mon travail."
    mara "Donner la bonne impression."

    "Je lui demande comment c'était."

    mara "Des dîners, des visages, des sourires programmés."
    mara "On te demande d'être parfaite sans jamais transpirer."

    "Elle lève les yeux au plafond."

    mara "Même l'eau devait être élégante."
    mara "Tu imagines ?"

    "Elle rit, mais le son est plus court."

    mara "Alors j'ai décidé de transpirer en public."
    mara "Et de dire que j'aime ça."

    "Je lui demande si c'est vrai."

    mara "Parfois."
    mara "Parfois non."

    "Elle se penche vers moi."

    mara "La vérité, c'est que j'aime qu'on me suive."
    mara "Pas qu'on me tienne."

    "Je lui demande si elle a déjà été tenue."

    mara "Tout le temps."
    mara "C'est ça, être héritière."

    "Elle recule, reprend une posture de façade."

    mara "Mais ici, on fait semblant d'être libres."
    mara "Alors j'en profite."

    "Je remarque un regard qui cherche la réaction."

    mara "Tu vois ?"
    mara "Je te regarde pour savoir si je vais trop loin."

    "Je lui dis qu'elle décide."

    mara "Non."
    mara "Je teste."
    mara "C'est différent."

    "Elle claque des doigts."

    mara "On dirait un concours, non ?"
    mara "Qui tiendra la scène le plus longtemps."

    "Je lui demande si ça l'amuse."

    mara "Ça m'occupe."
    mara "Et ça me rassure."

    "Je lui demande si elle a déjà perdu la scène."

    mara "Une fois."
    mara "J'avais dix-sept ans."
    mara "Je me suis enfermée dans les toilettes d'une gala."
    mara "Personne ne l'a su."

    "Elle se redresse, masque revenu."

    mara "Allez."
    mara "On va les rendre jaloux deux minutes."

    "Elle me lance un clin d'œil rapide."
    "Elle attend ma réaction."
    "Je hausse les épaules."
    "Elle rit."

    $ mara_link = 2

    jump FREE_TIME_END


label mara_link_3:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "colere", 0.60)

    mara "Tu sais ce qui m'agace ?"
    mara "Les gens qui pensent qu'ils peuvent me contredire devant tout le monde."

    "Elle tapote la table, rapide."

    mara "Comme si j'étais un décor."
    mara "Comme si je devais sourire et dire merci."

    "Je lui demande qui a fait ça."

    mara "Peu importe."
    mara "Ce qui compte, c'est le geste."

    "Elle serre sa tasse, puis la repose trop fort."

    mara "Je sais me défendre."
    mara "Mais je déteste devoir le faire."

    "Elle expire, puis force un sourire."

    mara "C'est rien."
    mara "Juste une mauvaise journée."

    "Je lui dis que ça a l'air de compter."

    mara "Oui."
    mara "Parce que je suis censée être intouchable."

    "Elle me fixe."

    mara "Et quand on touche, ça fait mal."

    mara "Tu sais, quand tu grandis dans un salon plein de gens puissants,"
    mara "tu apprends à ne jamais perdre la face."

    "Elle s'adosse, plus vulnérable."

    mara "Sauf que parfois, tu voudrais juste dire :"
    mara "Laisse-moi tranquille."

    "Je lui demande si elle le dit."

    mara "Je le dis autrement."
    mara "Je pique."
    mara "Je souris."
    mara "Je coupe."

    "Elle mime un coup de ciseaux."

    mara "Ça marche."
    mara "Mais ça laisse des traces."

    "Je lui demande lesquelles."

    mara "Les gens ne savent pas si je suis une amie ou une menace."
    mara "Et moi, je ne sais pas si je veux choisir."

    "Je lui demande si elle voudrait parfois être juste une amie."

    mara "Oui."
    mara "Mais il faut de la confiance."

    "Elle rit, mais le son est plus bas."

    mara "Tu sais ce qui est ironique ?"
    mara "On me reproche d'être trop sûre de moi."

    "Je lui demande si ce n'est pas son choix."

    mara "C'est un rôle."
    mara "Un costume."
    mara "Tu le portes assez longtemps, tu oublies que ça serre."

    "Elle reprend un ton vif."

    mara "Et quand quelqu'un me contredit,"
    mara "j'ai l'impression qu'il tire sur les coutures."

    "Je lui demande ce qu'elle fait quand ça craque."

    mara "Je fais une blague."
    mara "Ou je pars."

    "Elle baisse la voix."

    mara "Et je m'en veux après."

    "Je lui demande si elle revient vers les gens."

    mara "Si je peux."
    mara "Si j'ose."

    "Je lui dis qu'elle peut rester, si elle veut."

    mara "Rester, c'est intime."
    mara "Tu veux vraiment ça ?"

    "Je n'ai pas le temps de répondre."

    mara "T'inquiète."
    mara "Je te taquine."
    mara "Enfin… pas complètement."

    "Elle se penche en avant."

    mara "Merci d'écouter."
    mara "C'est rare."

    "Je lui dis que ce n'est pas un effort."

    mara "Ne t'habitue pas trop."
    mara "Je redeviens vite piquante."

    "Elle se redresse, masque retrouvé."

    mara "Bon, assez de drama."
    mara "On va se faire un autre café."

    "Elle souffle, puis lève les yeux au ciel."
    "Son sourire revient par réflexe."
    "Elle me pousse gentiment du coude."
    "La tension retombe."

    $ mara_link = 3

    jump FREE_TIME_END


label mara_link_4:

    scene bg_repos at adaptive_fullscreen

    $ showP("mara", "neutre", 0.58)

    mara "Tu sais, la réputation, c'est un costume."
    mara "On le porte parce que tout le monde regarde."
    mara "Et quand on l'enlève, il n'y a plus personne."

    "Elle laisse la phrase flotter."

    mara "Je préfère qu'on sache à quoi s'attendre."
    mara "Alors je donne une version claire."

    "Je lui demande si cette version lui ressemble."

    mara "Un peu."
    mara "Assez pour être crédible."
    mara "Pas assez pour me blesser."

    "Elle tapote son genou, impatiente."

    mara "Je connais par cœur les attentes."
    mara "La bonne tenue."
    mara "La bonne phrase."

    "Je lui demande si elle a déjà dérapé."

    mara "Une fois."
    mara "J'ai dit ce que je pensais."
    mara "On m'a dit que c'était \"maladroit\"."

    "Elle hausse les épaules, faussement légère."

    mara "Maladroit, c'est leur mot pour \"vrai\"."

    mara "Quand j'étais petite, je voulais chanter."
    mara "Mon père disait que c'était un hobby."

    "Je lui demande ce qu'elle en a fait."

    mara "Je chante quand je suis seule."
    mara "Ça ne compte pas, donc ça fait du bien."

    "Elle rit, puis se mord la lèvre."

    mara "C'est bizarre, non ?"
    mara "Garder ce qui est vrai pour la nuit."

    mara "Tu vois, c'est ça."
    mara "Je garde des trucs pour moi."

    "Je lui demande si ça lui pèse."

    mara "Parfois."
    mara "Surtout quand tout le monde pense me connaître."

    "Elle se penche vers moi."

    mara "Je me suis entraînée à marcher, à parler, à sourire."
    mara "À dire 'oui' sans le penser."

    "Je lui demande quand elle a dit non."

    mara "Le jour où j'ai pris un train seule."
    mara "C'était bête."
    mara "Mais j'ai respiré pour la première fois."

    "Je lui demande si quelqu'un l'a su."

    mara "Non."
    mara "Et c'est ce qui l'a rendu parfait."

    "Elle pose la main sur son ventre comme pour revivre l'instant."

    mara "Ici, je rejoue ça."
    mara "Je prends des trains imaginaires."

    "Je lui demande si elle a peur du regard des autres."

    mara "J'en ai besoin."
    mara "Et j'en ai peur."
    mara "C'est contradictoire."

    "Elle hausse les épaules."

    mara "Je suis faite de contradictions."
    mara "C'est aussi pour ça qu'ils m'ont élevée."

    "Je lui demande ce qu'elle veut vraiment."

    mara "Qu'on me laisse choisir."
    mara "Et qu'on me regarde choisir."

    "Je lui demande si elle a peur de décevoir."

    mara "Toujours."
    mara "Mais je déçois quand même."

    "Elle sourit, comme si elle se moquait d'elle-même."

    mara "Tu vois ?"
    mara "Même mes désirs sont un spectacle."

    "Je lui dis qu'elle peut en sortir."

    mara "Je peux."
    mara "Mais je reviens toujours."

    "Je lui demande pourquoi."

    mara "Parce que j'ai besoin d'un public."
    mara "Même quand je dis le contraire."

    "Elle s'allonge un instant, puis se relève d'un coup."

    mara "Désolée."
    mara "Je deviens trop sérieuse."
    mara "C'est mauvais pour l'image."

    "Elle lisse sa robe imaginaire."
    "Puis elle éclate de rire."
    "Son rire chasse le silence."
    "Elle cligne des yeux, amusée."

    $ mara_link = 4

    jump FREE_TIME_END


label mara_link_5:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("mara", "fatigue", 0.60)

    "La cafétéria se vide."
    "Elle laisse tomber ses épaules une seconde."

    mara "Je joue un rôle."
    mara "C'est plus simple que d'expliquer."

    "Je lui demande si elle sait qui elle serait sans."

    mara "Je l'apprends."
    mara "Je la cherche."

    "Elle regarde la lumière des néons."

    "Son regard hésite une seconde."

    mara "Tu sais ce qui me fait peur ?"
    mara "Qu'on m'oublie quand je ne brille pas."

    "Je lui dis qu'elle n'a pas besoin de briller tout le temps."

    mara "Oui."
    mara "Et pourtant, je continue."

    "Elle serre son gobelet."

    mara "Si je m'arrête, j'ai l'impression de disparaître."
    mara "Comme si je n'étais plus utile."

    "Je lui dis qu'elle n'a pas besoin d'être utile."

    mara "Essaie de dire ça à mon père."

    mara "Quand j'étais petite,"
    mara "on me mettait dans des robes trop belles."
    mara "On me disait 'ne fais pas de taches'."

    "Elle ricane."

    mara "Alors j'ai appris à ne pas respirer trop fort."

    "Je lui demande si elle a déjà fait une tache exprès."

    mara "Oui."
    mara "Du vin rouge."
    mara "C'était ma petite révolution."

    "Je lui demande si elle respire ici."

    mara "Plus."
    mara "Mais pas assez."

    "Elle relève la tête, comme si elle voulait défier quelqu'un."

    mara "Je suis bonne pour faire semblant."
    mara "C'est utile."
    mara "Mais ça fatigue."

    "Je lui demande si elle a quelqu'un en qui elle a confiance."

    mara "Rarement."
    mara "Je teste."
    mara "Je provoque."

    "Elle grimace."

    mara "Et parfois je blesse sans vouloir."

    "Je lui demande si elle regrette."

    mara "Souvent."
    mara "Surtout quand la personne ne revient pas."

    "Elle se tait, puis ajoute, presque pour elle."

    mara "Je ne supporte pas d'être ignorée."
    mara "Même quand je dis que je m'en fiche."

    "Je lui dis que c'est humain."

    mara "Ouais."
    mara "Mais chez moi, on n'avait pas le droit d'être 'humain'."

    "Elle éclate d'un rire bref."

    mara "Tu sais, mon père disait :"
    mara "On représente."

    "Elle fait une pause."

    mara "Moi, je veux qu'on me voie."
    mara "Pas qu'on voie le logo."

    "Je lui demande ce qu'elle ferait sans logo."

    mara "Je voyagerais."
    mara "Je danserais."
    mara "Je dormirais trop tard."

    "Elle regarde sa tasse vide."

    mara "Quand quelqu'un me parle franchement,"
    mara "j'ai envie d'y croire."
    mara "Et ça m'effraie."

    "Je lui demande pourquoi."

    mara "Parce que si j'y crois,"
    mara "je deviens loyale."
    mara "Et je ne sais pas faire semblant avec ça."

    "Elle souffle, puis relève la tête."

    mara "Bon."
    mara "Assez parlé."
    mara "On va faire semblant que tout va bien."

    "Elle sourit, et cette fois le sourire est plus vrai."
    "Elle attend une seconde, comme si elle hésitait."
    "Puis elle se lève."
    "Le masque revient, mais moins rigide."

    $ mara_link = 5

    jump FREE_TIME_END
