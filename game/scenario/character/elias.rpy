# -----------------------------------------------------------------------
# LIENS — ELIAS
# -----------------------------------------------------------------------

default elias_link = 0


label ELIAS_LINK_INTERACT:

    menu:
        "Passer du temps avec Elias ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if elias_link == 0:
        jump elias_link_1
    elif elias_link == 1:
        jump elias_link_2
    elif elias_link == 2:
        jump elias_link_3
    elif elias_link == 3:
        jump elias_link_4
    elif elias_link == 4:
        jump elias_link_5

    if last_room_label:
        jump expression last_room_label
    return


label elias_link_1:

    scene bg_gymnase at adaptive_fullscreen

    play music "music/bgm_soft_neon_morning.mp3" fadein 0.6

    $ showP("elias", "neutre", 0.70)

    elias "Tu arrives pile à l'heure."
    elias "J'ai quinze minutes pour finir ma série."
    elias "Après ça, je range."

    noam "Promis, je ne te vole pas plus que ça."
    "Il règle la charge sans me regarder."
    "Ses gestes sont précis, presque mécaniques, automatiques."

    elias "Je fais toujours les mêmes séries."
    elias "Même cadence, même souffle, même rythme."

<<<<<<< HEAD
    noam "Tu ne t'ennuies jamais à faire les mêmes exercices ?"
=======
    noam "Tu t'ennuies jamais avec ça ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Non."
    elias "L'ennui, c'est quand tu ne sais pas quoi faire."
    elias "Moi je sais exactement les exercices dont j'ai besoin."

    "Il pousse une répétition, inspire, puis parle."

    elias "Quand j'étais gamin, c'était pareil."
    elias "Je me suis toujours levé tôt, j'allais aider mes parents."

    "Sa voix ne se plaint pas. Elle constate."

<<<<<<< HEAD
    elias "Mon père partait au dépôt tôt dans la nuit."
    elias "Ma mère enchaînait deux postes pour gagner un peu mieux sa vie."
    elias "On ne cherchait pas à comprendre."
    elias "On tenait."

    noam "Et toi, tu faisais quoi dans tout ça ?"
=======
    $ showP("elias", "reflechit", 0.70)

    elias "Mon père partait au dépôt."
    elias "Ma mère enchaînait deux postes."
    elias "On ne cherchait pas à comprendre."
    elias "On tenait."

    noam "Et toi, tu faisais quoi, euh… quand t'étais gosse ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Je réparais ce qui cassait."
    elias "Vieux vélo."
    elias "Fuite dans la cuisine."
    elias "J'essayais d'être utile."

    "Il essuie la barre avec une serviette pliée au carré."

<<<<<<< HEAD
    noam "C'est comme ça que tu es devenu mécano ?"
=======
    elias "Si quelque chose tient, tu peux dormir."
    elias "Si ça lâche, tu perds du temps."

    noam "On dirait une philosophie."

    elias "C'est juste du bon sens."
    elias "Tu fais avec ce que tu as."
    elias "Tu le fais bien."

    noam "Tu voulais déjà être mécano ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Je voulais être utile."
    elias "Alors d'une certaine manière, ça a bien marché, du moins je pense."

    "Il reprend une série sans attendre ma réponse."

    elias "Le sport m'a appris à être exigent, envers moi-même mais aussi envers les autres."
    elias "D'attendre des résultats en progression constante."

    "Il laisse tomber la barre en contrôlant la descente."

<<<<<<< HEAD
    elias "C'est un peu ce que j'essaye de faire dans mon quotidien."
=======
    elias "Ici c'est pareil."
    elias "Tu travailles."
    elias "Tu tiens."
    elias "Tu ne te plains pas."

    noam "Tu parles comme si tu écrivais une liste."

    elias "Une liste, c'est clair."
    elias "Les discours, ça disperse."

    noam "Et… des loisirs ? Un truc juste pour toi ?"

    elias "Le travail."
    elias "L'entraînement."
    elias "Le reste, c'est du bruit."
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    "Un léger silence."
    "Il resserre la poignée d'un appareil."

    $ showP("elias", "neutre", 0.70)

    elias "J'écoute quand quelqu'un sait ce qu'il fait."
<<<<<<< HEAD
    elias "Sinon, je perds vite le fil de la discussion, les grandes théories c'est vraiment pas pour moi."

    "Sa voix reste plate, mais le message est clair."

    "Je hoche la tête."
    "Elias repart sur une série, concentré."
=======
    elias "Sinon, je coupe court."

    noam "Tu t'inquiètes jamais de… pas profiter ?"

    elias "Profiter de quoi ?"
    elias "De perdre du temps ?"

    "Il relève la tête et me fixe enfin."

    $ showP("elias", "ecoute", 0.70)

    elias "On profite quand c'est stable."
    elias "Là, on stabilise."

    "Sa voix reste plate, mais le message est clair."

    elias "Je note mes repas."
    elias "Pas pour le plaisir."
    elias "Pour l'énergie."

    noam "Tu calcules tout, alors ?"

    elias "Je réduis les surprises."
    elias "Ça évite les erreurs."

    elias "On a un boulot."
    elias "Je fais le mien."
    elias "Si tu veux parler, parle."
    elias "Mais ne me ralentis pas."

    noam "D'accord. J'essaie de pas te faire perdre une seconde."
    "Il repart sur une série, concentré."
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    $ elias_link = 1

    jump FREE_TIME_END


label elias_link_2:

    scene bg_maintenance at adaptive_fullscreen

    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    $ showP("elias", "ecoute", 0.65)

    elias "Le bras d'articulation a pris du jeu."
    elias "Trois millimètres."
    elias "C'est suffisant pour fausser tout l'angle."

    "Je le regarde mesurer, puis noter quelque chose sur un carnet."

    elias "Si je resserre trop, ça risque de casser."
    elias "Mais si je laisse, ça va dériver."
    elias "Il faut trouver le bon point."

<<<<<<< HEAD
    noam "Et ... Tu fais ça comment ?"
=======
    noam "Tu fais comment pour trouver ce point-là, à chaque fois ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Je teste."
    elias "Je corrige."
    elias "Je recommence."

    "Il s'arrête une seconde pour changer d'outil."

    $ showP("elias", "reflechit", 0.65)

    elias "J'ai appris ça en atelier."
    elias "Crois moi, t'avais pas intéret à te tromper."

<<<<<<< HEAD
    noam "En atelier ? Tu as travaillé dans une grande boite ou quelque chose du genre ?"
=======
    noam "Tu bossais où, avant ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Un usine de maintenance automobile."
    elias "Équipe de nuit."
    elias "Ça payait le loyer."

<<<<<<< HEAD
    noam "Et avec ça t'avais le temps de faire du sport sur le côté ?!"
=======
    noam "Et tu t'entraînais quand, dans tout ça ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Course."
    elias "Tractions."
    elias "Rien d'exotique."

    "Il ajuste un câble, teste la tension."

    elias "Le sport me gardait droit."
    elias "Quand tu bosses la nuit, tu dois tenir la journée et même si c'est crevant, le sport, ça aide."

<<<<<<< HEAD
    noam "Tu pratiquais seul ou..."
=======
    noam "T'avais des amis ? Des gens avec qui couper un peu ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Des collègues."
    elias "On se respectait."
    elias "Pas besoin de plus."

    "Il serre une vis, puis vérifie avec un niveau."

    elias "Le boulot, c'est pas la passion."
<<<<<<< HEAD
    elias "C'est ce qui permet de survivre."
    elias "Même si j'aime bien être entouré de ces machines."
=======
    elias "C'est ce qui tient les murs."

    noam "Et ta passion, alors ? Elle ressemble à quoi ?"

    elias "Tenir les murs."

    noam "Ça sonne… dur dit comme ça."

    elias "C'est réel."
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    "Il repose l'outil et regarde la machine comme si elle pouvait mentir."

    elias "On n'avait pas de réseau."
    elias "Pas de piston."
    elias "Donc je bossais dur."

<<<<<<< HEAD
    noam "T'as jamais pensé à arrêter ?"
=======
    noam "T'as jamais voulu tout arrêter, même une fois ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Arrêter pour quoi ?"
    elias "Pour que je me retrouve dehors ?"
    elias "Y'avait du taff, fallait que je le fasse, c'est tout."

<<<<<<< HEAD
    "Il secoue la tête, de façon presque imperceptible."
=======
    "Il secoue la tête, presque imperceptible."

    elias "Quand tu comptes tes heures, tu ne joues pas."
    elias "Tu avances."

    noam "Ici, tout le monde avance différemment, quand même."

    elias "Je m'en fiche."
    elias "Moi, je dois tenir les machines."
    elias "Sinon, on perd tout."
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "Surtout quand il y avait la guerre..."
    "Il pose la paume sur la carcasse froide."

    elias "Une panne, ça ne prévient pas."
    elias "Et ça ne se discute pas."

<<<<<<< HEAD
    noam "La guerre, d'une certain façon tu étais concerné toi aussi ..."
=======
    noam "Tu as peur de l'échec, ou pas du tout ?"
>>>>>>> fd39f75d896d0f0198ac82cc28fee1196c61a8ec

    elias "C'est clair, tu ne peux même pas imaginer ..."
    elias "L'échec, c'est quand tu n'as plus d'outil."
    elias "Ou plus de temps."
    elias "Le reste, c'est des ajustements."

    "Il corrige encore, au millimètre."

    elias "On croit gagner du temps, et on perd tout."
    elias "Les approximations coûtent plus cher."

    noam "Tu tiens parce que t'as l'habitude, ou parce que tu veux pas lâcher ?"

    elias "Je supporte la fatigue."
    elias "Je ne supporte pas l'inefficacité."

    "Il redresse les épaules."

    elias "Si tu veux aider, tiens la lampe."
    elias "Pas besoin de parler."

    menu:
        "Tenir la lampe pour Elias":
            "La garder bien stable":
                $ lamp_ok = True
                noam "Ok. Je bouge pas."
            "La laisser trembler un peu":
                $ lamp_ok = False
                noam "Oups… j-juste une seconde."

    if lamp_ok:
        play sound sfx_beep
        "La lumière reste fixe sur la pièce."
        elias "Bien."
    else:
        "Le faisceau bouge et Elias serre la mâchoire."
        elias "Reste stable."

    "Il travaille en silence pendant plusieurs minutes."

    elias "Merci."
    elias "C'était utile."

    "Le mot sonne comme un compliment."

    elias "Si tu reviens, viens à l'heure."
    elias "Je n'attends pas."
    "Il ne plaisante pas."
    "C'est une règle simple."

    $ elias_link = 2

    jump FREE_TIME_END


label elias_link_3:

    scene bg_gymnase at adaptive_fullscreen

    play music "music/bgm_soft_neon_morning.mp3" fadein 0.6

    $ showP("elias", "reflechit", 0.70)

    elias "Je devais réorganiser les stations."
    elias "Mais il manque des pièces."
    elias "On fera avec."

    "Il déplace un tapis, puis aligne les haltères."

    elias "Je n'aime pas l'improvisation."
    elias "Mais je sais m'adapter."

    noam "Quand tu dis t'adapter, ça veut dire quoi, pour toi ?"

    elias "Tu gardes l'objectif."
    elias "Tu changes la route."

    "Il me montre un support bricolé."

    elias "J'ai récupéré ça dans le stock."
    elias "Ça ne devait pas servir ici."
    elias "Maintenant, si."

    noam "Ça t'arrivait souvent de bricoler comme ça ?"

    elias "Tout le temps."
    elias "Quand tu n'as pas de budget, tu inventes."

    "Sa façon de dire 'inventer' ressemble à 'réparer'."

    elias "On récupère."
    elias "On recompose."
    elias "On ne gaspille pas."

    noam "Donc oui, tu détestes le gaspillage."

    elias "Oui."
    elias "C'est une insulte à l'effort."

    elias "Mon quartier, c'était ça."
    elias "Une pièce qui casse, une autre qui la remplace."
    elias "Pas de fioritures."

    noam "Ça demande quand même de la créativité."

    elias "Non."
    elias "Ça demande de la discipline."

    "Il essuie un banc."

    elias "On a appris à respecter ce qui tient."
    elias "Si ça tient, tu ne touches pas."
    elias "Si ça lâche, tu répares."

    noam "T'as l'air de garder tout à distance."

    elias "Je ne suis pas là pour faire joli."
    elias "Je suis là pour que ça marche."

    noam "Et tu t'autorises un moment de pause, parfois ?"

    elias "Quand tout tient."
    elias "Pas avant."

    "Il vérifie le serrage d'une vis."

    elias "Je fais pareil avec les gens."
    elias "Je regarde s'ils sont fiables."

    noam "Tu juges ça comment ?"

    elias "Tu vois qui tient sa parole."
    elias "Qui arrive à l'heure."
    elias "Qui termine ce qu'il commence."

    noam "Et les erreurs, tu pardonnes ?"

    elias "Une fois."
    elias "Après, c'est un choix."

    "Il replace un tapis, puis souffle."

    elias "Je ne suis pas dur."
    elias "Je suis constant."

    "Il lève les yeux, une seconde."

    elias "Le reste, c'est du bruit."

    noam "Tu crois aux promesses ?"

    elias "Je crois aux actes."
    elias "Les promesses, ça se casse."

    "Il replace une série d'haltères."

    elias "Même ici, je note tout."
    elias "Qui utilise quoi."
    elias "Ce qui s'use."

    noam "On dirait un chef d'atelier, sérieux."

    elias "Je ne cherche pas à diriger."
    elias "Je cherche à éviter les pertes."

    "Il ajuste encore un dernier détail."

    elias "Quand les choses sont rangées, tu peux penser."
    elias "Quand c'est le chaos, tu subis."

    noam "Et ici, tu subis ?"

    elias "Pas encore."
    elias "Mais je reste prêt."

    "Il souffle, puis se remet en place."

    elias "L'effort calme."
    elias "L'improvisation épuise."

    "Je comprends qu'il parle de plus que du sport."
    "Il reste concentré."
    "Tout est à sa place."

    $ elias_link = 3

    jump FREE_TIME_END


label elias_link_4:

    scene bg_maintenance at adaptive_fullscreen

    play music "music/bgm_unsaid_distance.mp3" fadein 0.6

    $ showP("elias", "neutre", 0.68)

    elias "Les règles évitent les discussions inutiles."
    elias "Tout le monde sait quoi faire."
    elias "Pas besoin d'interpréter les intentions."

    "Il trace une ligne imaginaire sur la table."

    elias "Là, c'est clair."
    elias "Là, c'est flou."

    noam "T'as jamais eu envie de sortir du cadre, juste pour voir ?"

    elias "Le cadre protège."
    elias "Sans cadre, tu passes ton temps à négocier."

    "Il classe des outils par taille."

    elias "J'ai vu des gens tout perdre pour une mauvaise décision."
    elias "Un retard."
    elias "Une prise de risque inutile."

    noam "C'est arrivé dans ta famille ?"

    elias "Un accident."
    elias "Un mois sans salaire."
    elias "Tu apprends vite."

    "Il reste factuel, mais le silence qui suit est plus long."

    elias "On n'avait pas de réserve."
    elias "Pas d'excuse."
    elias "Juste un trou à combler."

    noam "Et vous avez tenu comment ?"

    elias "Heures en plus."
    elias "Moins de sommeil."
    elias "Plus d'effort."

    "Il range des clés plates avec soin."

    elias "Ça forge."
    elias "Ça épuise aussi."

    noam "Tu voulais quoi, à ce moment-là ?"

    elias "Un mois de calme."
    elias "C'est tout."

    "Je comprends qu'il parle encore en termes de réparation."

    elias "Le vote, c'est bien."
    elias "Si le cadre est clair."
    elias "Sinon, c'est du bruit."

    noam "Tu as déjà douté d'un cadre ?"

    elias "Oui."
    elias "Quand il est injuste."
    elias "Mais on fait avec."

    "Il resserre sa prise sur un tournevis."

    elias "Changer un cadre, c'est du chantier."
    elias "On ne fait pas ça en parlant."

    noam "Tu te sens écouté, ici ?"

    elias "Je ne parle pas beaucoup."
    elias "Je fais."

    "Il me lance un regard rapide."

    elias "Les mots, ça se tord."
    elias "Les gestes, non."

    elias "Tu veux me comprendre ?"
    elias "Regarde ce que je tiens."

    "Je regarde ses mains."
    "Elles sont marquées, mais calmes."

    elias "J'ai appris à rester debout."
    elias "Même quand tout le monde se plaint."

    noam "Et… la reconnaissance, ça te manque jamais ?"

    elias "La reconnaissance, ça ne répare rien."
    elias "Si je fais bien, ça tient."

    "Il range un outil dans son étui."

    elias "Je respecte ceux qui travaillent."
    elias "Les autres, je les laisse parler."

    noam "Tu te sens indispensable ?"

    elias "Je ne pense pas comme ça."
    elias "Je fais ce qu'il faut."

    "Il s'arrête, réfléchit."

    elias "Si je ne le fais pas, quelqu'un d'autre devra."
    elias "Alors autant le faire bien."

    "Sa logique est simple, mais solide."

    elias "Je ne cherche pas à convaincre."
    elias "Je cherche à éviter les erreurs."

    noam "Ok. J'entends."
    "Le bruit d'un outil qui claque marque la fin de la discussion."

    elias "Si ça tient, c'est suffisant."
    elias "Si ça casse, on répare."
    elias "C'est ma ligne."

    "Il ne sourit pas, mais il est clair."
    "La conversation est close."

    $ elias_link = 4

    jump FREE_TIME_END


label elias_link_5:

    scene bg_gymnase at adaptive_fullscreen

    play music "music/bgm_soft_neon_morning.mp3" fadein 0.6

    $ showP("elias", "fatigue", 0.70)

    "La salle est presque vide."
    "Il essuie une barre, lentement."

    elias "Je dors mal quand les choses sont mal définies."
    elias "C'est tout."

    noam "Qu'est-ce qui te tient éveillé, alors ?"

    elias "Les listes incomplètes."
    elias "Les tâches laissées en plan."
    elias "Les gens qui promettent et disparaissent."

    "Il range un disque et se redresse."

    elias "Je ne supporte pas les dettes."
    elias "Pas seulement l'argent."
    elias "Les dettes de temps."
    elias "Les dettes d'effort."

    noam "Ça fait beaucoup à porter…"

    elias "Je porte."
    elias "J'ai toujours porté."

    "Il inspire, puis reprend plus doucement."

    elias "Ce n'est pas du courage."
    elias "C'est une habitude."

    elias "Quand j'étais plus jeune, j'avais peur de tomber malade."
    elias "Parce que personne ne te remplace."

    noam "T'avais quelqu'un sur qui compter ?"

    elias "Ma sœur."
    elias "Elle comptait sur moi."
    elias "C'était clair."

    "Le mot "clair" revient, comme un repère."

    elias "Je lui ai appris à réparer un moteur."
    elias "Elle m'a appris à dormir quand c'est possible."

    noam "Elle te manque ?"

    elias "Oui."
    elias "Mais je ne m'arrête pas pour ça."

    "Il regarde la barre comme si elle pesait plus lourd."

    elias "Elle voulait que je parte."
    elias "Que je prenne ma chance."
    elias "Alors je la prends."

    "Je remarque un sourire très bref."

    elias "C'était rare."
    elias "Mais ça comptait."

    noam "Tu penses à elle ici ?"

    elias "Parfois."
    elias "Quand je répare quelque chose."

    "Il se passe une main sur le front."

    elias "Le manque de contrôle, ça te ronge."
    elias "Alors je contrôle ce que je peux."

    noam "T'as déjà craqué ?"

    elias "Une fois."
    elias "J'ai ri."
    elias "Pas parce que c'était drôle."

    "Il semble presque gêné."

    elias "Le rire, c'est quand la pression lâche."
    elias "Après, tu reviens."

    elias "C'était quand j'avais trop poussé."
    elias "Mon corps a dit stop."

    noam "Tu l'écoutes, ton corps, maintenant ?"

    elias "Je l'écoute."
    elias "Je lui demande juste de tenir."

    "Il s'assoit, un instant."

    elias "Je ne cherche pas l'affection."
    elias "Je cherche la stabilité."

    noam "La stabilité, c'est aussi des gens, non ?"

    elias "Oui."
    elias "Mais des gens fiables."

    noam "Fiable, pour toi, c'est quoi ?"

    elias "Quelqu'un qui revient."
    elias "Quelqu'un qui tient parole."
    elias "Quelqu'un qui reste quand ça dure."

    "Un long silence s'installe."

    elias "Tu voulais en savoir plus."
    elias "Voilà."

    "Il se lève, déjà prêt à repartir."
    "Je comprends que, pour lui, parler est un effort mesuré."

    "Il replace la serviette, alignée avec le banc."
    "Le geste est net."
    "Comme lui."
    "Il retrouve son rythme."
    "Je le laisse travailler."

    $ elias_link = 5

    jump FREE_TIME_END
