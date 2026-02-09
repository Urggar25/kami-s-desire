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

    play music "music/bgm_careful_wanting.mp3" fadein 1.0

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "neutre", 0.70)

    elias content "Tu arrives pile à l'heure."
    elias detendu "J'ai quinze minutes pour finir ma série."
    elias detendu "Après ça, je range."

    "Il règle la charge sans me regarder."
    "Ses gestes sont précis, presque mécaniques, automatiques."

    elias ecoute "Je fais toujours les mêmes séries."
    elias ecoute "Même cadence, même souffle, même rythme."

    $ showP("noam", "neutre", 0.25)

    noam sourire "Tu ne t'ennuies jamais à faire les mêmes exercices ?"

    elias reflechit "Non."
    elias reflechit "L'ennui, c'est quand tu ne sais pas quoi faire."
    elias reflechit "Moi je sais exactement les exercices dont j'ai besoin."

    "Il pousse une répétition, inspire, puis parle."

    elias content "Quand j'étais gamin, c'était pareil."
    elias content "Je me suis toujours levé tôt, j'allais aider mes parents."

    "Sa voix ne se plaint pas. Elle constate."

    elias ecoute "Mon père partait au dépôt tôt dans la nuit."
    elias ecoute "Ma mère enchaînait deux postes pour gagner un peu mieux sa vie."
    elias fatigue "On ne cherchait pas à comprendre."
    elias fatigue "On continuait à bosser, c'est tout."

    noam reflexion "Et toi, tu faisais quoi dans tout ça ?"

    elias ecoute "Je réparais ce qui cassait."
    elias ecoute "Genre, les vieux vélo."
    elias ecoute "Fuite dans la cuisine."
    elias jaloux "J'essayais d'être utile quoi."

    "Il essuie la barre avec une serviette pliée au carré."

    noam raison "C'est comme ça que tu es devenu mécano ?"

    elias joie "Je voulais être utile."
    elias joie "Alors d'une certaine manière, ça a bien marché, du moins je pense."

    "Il reprend une série sans attendre ma réponse."

    elias detendu "Le sport m'a appris à être exigent, envers moi-même mais aussi envers les autres."
    elias detendu "D'attendre des résultats en progression constante."

    "Il laisse tomber la barre en contrôlant la descente."

    elias content "C'est un peu ce que j'essaye de faire dans mon quotidien."

    "Un léger silence."
    "Il resserre la poignée d'un appareil."

    elias ecoute "J'écoute quand quelqu'un sait ce qu'il fait."
    elias reflechit "Sinon, je perds vite le fil de la discussion, les grandes théories c'est vraiment pas pour moi."

    "Sa voix reste plate, mais le message est clair."

    "Je hoche la tête."
    "Elias repart sur une série, concentré."

    $ elias_link = 1

    jump FREE_TIME_END


label elias_link_2:

    scene bg_maintenance at adaptive_fullscreen

    $ showP("elias", "ecoute", 0.65)

    elias "Le bras d'articulation a pris du jeu."
    elias "Trois millimètres."
    elias "C'est suffisant pour fausser tout l'angle."

    "Je le regarde mesurer, puis noter quelque chose sur un carnet."

    elias "Si je resserre trop, ça risque de casser."
    elias "Mais si je laisse, ça va dériver."
    elias "Il faut trouver le bon point."

    noam "Et ... Tu fais ça comment ?"

    elias "Je teste."
    elias "Je corrige."
    elias "Je recommence."

    "Il s'arrête une seconde pour changer d'outil."

    elias "J'ai appris ça en atelier."
    elias "Crois moi, t'avais pas intéret à te tromper."

    noam "En atelier ? Tu as travaillé dans une grande boite ou quelque chose du genre ?"

    elias "Un usine de maintenance automobile."
    elias "Équipe de nuit."
    elias "Ça payait le loyer."

    noam "Et avec ça t'avais le temps de faire du sport sur le côté ?!"

    elias "Course."
    elias "Tractions."
    elias "Rien d'exotique."

    "Il ajuste un câble, teste la tension."

    elias "Le sport me gardait droit."
    elias "Quand tu bosses la nuit, tu dois tenir la journée et même si c'est crevant, le sport, ça aide."

    noam "Tu pratiquais seul ou..."

    elias "Des collègues."
    elias "On se respectait."
    elias "Pas besoin de plus."

    "Il serre une vis, puis vérifie avec un niveau."

    elias "Le boulot, c'est pas la passion."
    elias "C'est ce qui permet de survivre."
    elias "Même si j'aime bien être entouré de ces machines."

    "Il repose l'outil et regarde la machine comme si elle pouvait mentir."

    elias "On n'avait pas de réseau."
    elias "Pas de piston."
    elias "Donc je bossais dur."

    noam "T'as jamais pensé à arrêter ?"

    elias "Arrêter pour quoi ?"
    elias "Pour que je me retrouve dehors ?"
    elias "Y'avait du taff, fallait que je le fasse, c'est tout."

    "Il secoue la tête, de façon presque imperceptible."

    elias "Surtout quand il y avait la guerre..."
    "Il pose la paume sur la carcasse froide."

    elias "Une panne, ça ne prévient pas."
    elias "Et ça ne se discute pas."

    noam "La guerre, d'une certain façon tu étais concerné toi aussi ..."

    elias "C'est clair, tu ne peux même pas imaginer ..."
    elias "L'échec, c'est quand tu n'as plus d'outil."
    elias "Ou plus de temps."
    elias "Le reste, c'est des ajustements."

    "Il corrige encore, au millimètre."

    elias "On croit gagner du temps, et on perd tout."
    elias "Les approximations coûtent plus cher."

    "Je remarque sa fatigue."

    elias "Je supporte la fatigue."
    elias "Je ne supporte pas l'inefficacité."

    "Il redresse les épaules."

    elias "Si tu veux aider, tiens la lampe."
    elias "Pas besoin de parler."

    "Je tiens la lampe."
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

    $ showP("elias", "reflechit", 0.70)

    elias "Je devais réorganiser les stations."
    elias "Mais il manque des pièces."
    elias "On fera avec."

    "Il déplace un tapis, puis aligne les haltères."

    elias "Je n'aime pas l'improvisation."
    elias "Mais je sais m'adapter."

    "Je lui demande ce qu'il entend par s'adapter."

    elias "Tu gardes l'objectif."
    elias "Tu changes la route."

    "Il me montre un support bricolé."

    elias "J'ai récupéré ça dans le stock."
    elias "Ça ne devait pas servir ici."
    elias "Maintenant, si."

    "Je lui demande s'il a souvent dû bricoler comme ça."

    elias "Tout le temps."
    elias "Quand tu n'as pas de budget, tu inventes."

    "Sa façon de dire 'inventer' ressemble à 'réparer'."

    elias "On récupère."
    elias "On recompose."
    elias "On ne gaspille pas."

    "Je lui demande s'il déteste le gaspillage."

    elias "Oui."
    elias "C'est une insulte à l'effort."

    elias "Mon quartier, c'était ça."
    elias "Une pièce qui casse, une autre qui la remplace."
    elias "Pas de fioritures."

    "Je lui dis que ça demande de la créativité."

    elias "Non."
    elias "Ça demande de la discipline."

    "Il essuie un banc."

    elias "On a appris à respecter ce qui tient."
    elias "Si ça tient, tu ne touches pas."
    elias "Si ça lâche, tu répares."

    "Je remarque qu'il garde tout à distance."

    elias "Je ne suis pas là pour faire joli."
    elias "Je suis là pour que ça marche."

    "Je lui demande s'il s'autorise un moment de pause."

    elias "Quand tout tient."
    elias "Pas avant."

    "Il vérifie le serrage d'une vis."

    elias "Je fais pareil avec les gens."
    elias "Je regarde s'ils sont fiables."

    "Je demande comment il juge ça."

    elias "Tu vois qui tient sa parole."
    elias "Qui arrive à l'heure."
    elias "Qui termine ce qu'il commence."

    "Je lui demande s'il pardonne les erreurs."

    elias "Une fois."
    elias "Après, c'est un choix."

    "Il replace un tapis, puis souffle."

    elias "Je ne suis pas dur."
    elias "Je suis constant."

    "Il lève les yeux, une seconde."

    elias "Le reste, c'est du bruit."

    "Je lui demande s'il croit aux promesses."

    elias "Je crois aux actes."
    elias "Les promesses, ça se casse."

    "Il replace une série d'haltères."

    elias "Même ici, je note tout."
    elias "Qui utilise quoi."
    elias "Ce qui s'use."

    "Je lui dis qu'il ressemble à un chef d'atelier."

    elias "Je ne cherche pas à diriger."
    elias "Je cherche à éviter les pertes."

    "Il ajuste encore un dernier détail."

    elias "Quand les choses sont rangées, tu peux penser."
    elias "Quand c'est le chaos, tu subis."

    "Je lui demande s'il subit, ici."

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

    $ showP("elias", "neutre", 0.68)

    elias "Les règles évitent les discussions inutiles."
    elias "Tout le monde sait quoi faire."
    elias "Pas besoin d'interpréter les intentions."

    "Il trace une ligne imaginaire sur la table."

    elias "Là, c'est clair."
    elias "Là, c'est flou."

    "Je lui demande s'il n'a jamais eu envie de sortir du cadre."

    elias "Le cadre protège."
    elias "Sans cadre, tu passes ton temps à négocier."

    "Il classe des outils par taille."

    elias "J'ai vu des gens tout perdre pour une mauvaise décision."
    elias "Un retard."
    elias "Une prise de risque inutile."

    "Je lui demande si c'est arrivé dans sa famille."

    elias "Un accident."
    elias "Un mois sans salaire."
    elias "Tu apprends vite."

    "Il reste factuel, mais le silence qui suit est plus long."

    elias "On n'avait pas de réserve."
    elias "Pas d'excuse."
    elias "Juste un trou à combler."

    "Je lui demande comment ils ont tenu."

    elias "Heures en plus."
    elias "Moins de sommeil."
    elias "Plus d'effort."

    "Il range des clés plates avec soin."

    elias "Ça forge."
    elias "Ça épuise aussi."

    "Je lui demande ce qu'il aurait voulu à ce moment-là."

    elias "Un mois de calme."
    elias "C'est tout."

    "Je comprends qu'il parle encore en termes de réparation."

    elias "Le vote, c'est bien."
    elias "Si le cadre est clair."
    elias "Sinon, c'est du bruit."

    "Je lui demande s'il a déjà douté d'un cadre."

    elias "Oui."
    elias "Quand il est injuste."
    elias "Mais on fait avec."

    "Il resserre sa prise sur un tournevis."

    elias "Changer un cadre, c'est du chantier."
    elias "On ne fait pas ça en parlant."

    "Je lui demande s'il se sent écouté, ici."

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

    "Je lui demande s'il n'a jamais eu envie d'être reconnu."

    elias "La reconnaissance, ça ne répare rien."
    elias "Si je fais bien, ça tient."

    "Il range un outil dans son étui."

    elias "Je respecte ceux qui travaillent."
    elias "Les autres, je les laisse parler."

    "Je lui demande s'il se sent indispensable."

    elias "Je ne pense pas comme ça."
    elias "Je fais ce qu'il faut."

    "Il s'arrête, réfléchit."

    elias "Si je ne le fais pas, quelqu'un d'autre devra."
    elias "Alors autant le faire bien."

    "Sa logique est simple, mais solide."

    elias "Je ne cherche pas à convaincre."
    elias "Je cherche à éviter les erreurs."

    "Je hoche la tête."
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

    $ showP("elias", "fatigue", 0.70)

    "La salle est presque vide."
    "Il essuie une barre, lentement."

    elias "Je dors mal quand les choses sont mal définies."
    elias "C'est tout."

    "Je lui demande ce qui le tient éveillé."

    elias "Les listes incomplètes."
    elias "Les tâches laissées en plan."
    elias "Les gens qui promettent et disparaissent."

    "Il range un disque et se redresse."

    elias "Je ne supporte pas les dettes."
    elias "Pas seulement l'argent."
    elias "Les dettes de temps."
    elias "Les dettes d'effort."

    "Je lui dis que ça fait beaucoup à porter."

    elias "Je porte."
    elias "J'ai toujours porté."

    "Il inspire, puis reprend plus doucement."

    elias "Ce n'est pas du courage."
    elias "C'est une habitude."

    elias "Quand j'étais plus jeune, j'avais peur de tomber malade."
    elias "Parce que personne ne te remplace."

    "Je lui demande s'il a eu quelqu'un sur qui compter."

    elias "Ma sœur."
    elias "Elle comptait sur moi."
    elias "C'était clair."

    "Le mot "clair" revient, comme un repère."

    elias "Je lui ai appris à réparer un moteur."
    elias "Elle m'a appris à dormir quand c'est possible."

    "Je lui demande si elle lui manque."

    elias "Oui."
    elias "Mais je ne m'arrête pas pour ça."

    "Il regarde la barre comme si elle pesait plus lourd."

    elias "Elle voulait que je parte."
    elias "Que je prenne ma chance."
    elias "Alors je la prends."

    "Je remarque un sourire très bref."

    elias "C'était rare."
    elias "Mais ça comptait."

    "Je lui demande s'il pense à elle ici."

    elias "Parfois."
    elias "Quand je répare quelque chose."

    "Il se passe une main sur le front."

    elias "Le manque de contrôle, ça te ronge."
    elias "Alors je contrôle ce que je peux."

    "Je lui demande s'il a déjà craqué."

    elias "Une fois."
    elias "J'ai ri."
    elias "Pas parce que c'était drôle."

    "Il semble presque gêné."

    elias "Le rire, c'est quand la pression lâche."
    elias "Après, tu reviens."

    elias "C'était quand j'avais trop poussé."
    elias "Mon corps a dit stop."

    "Je lui demande s'il écoute son corps maintenant."

    elias "Je l'écoute."
    elias "Je lui demande juste de tenir."

    "Il s'assoit, un instant."

    elias "Je ne cherche pas l'affection."
    elias "Je cherche la stabilité."

    "Je lui dis que la stabilité, c'est aussi des gens."

    elias "Oui."
    elias "Mais des gens fiables."

    "Je lui demande ce qu'il considère comme fiable."

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
