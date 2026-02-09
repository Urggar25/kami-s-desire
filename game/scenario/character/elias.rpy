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
    $ showP("noam", "reflexion", 0.25)

    elias ecoute "Le bras d'articulation a pris du jeu."
    elias reflechit "Trois millimètres."
    elias reflechit "C'est suffisant pour fausser tout l'angle."

    "Je le regarde mesurer, puis noter quelque chose sur un carnet."

    elias ecoute "Si je resserre trop, ça risque de casser."
    elias fatigue "Mais si je laisse, ça va dériver."
    elias reflechit "Il faut trouver le bon point."

    noam hesitation "Et ... Tu fais ça comment ?"

    elias ecoute "Je teste."
    elias ecoute "Je corrige."
    elias reflechit "Je recommence."

    "Il s'arrête une seconde pour changer d'outil."

    elias content "J'ai appris ça en atelier."
    elias reflechit "Crois moi, t'avais pas intéret à te tromper."

    noam reflexion "En atelier ? Tu as travaillé dans une grande boite ou quelque chose du genre ?"

    elias ecoute "Un usine de maintenance automobile."
    elias fatigue "Équipe de nuit."
    elias ecoute "Ça payait le loyer."

    noam surpris "Et avec ça t'avais le temps de faire du sport sur le côté ?!"

    elias ecoute "Course."
    elias ecoute "Tractions."
    elias reflechit "Rien d'exotique."

    "Il ajuste un câble, teste la tension."

    elias content "Le sport me gardait droit."
    elias detendu "Quand tu bosses la nuit, tu dois tenir la journée et même si c'est crevant, le sport, ça aide."

    noam hesitation "Tu pratiquais seul ou..."

    elias ecoute "Des collègues."
    elias ecoute "On se respectait."
    elias reflechit "Pas besoin de plus."

    "Il serre une vis, puis vérifie avec un niveau."

    elias reflechit "Le boulot, c'est pas la passion."
    elias ecoute "C'est ce qui permet de survivre."
    elias content "Même si j'aime bien être entouré de ces machines."

    "Il repose l'outil et regarde la machine comme si elle pouvait mentir."

    elias reflechit "On n'avait pas de réseau."
    elias reflechit "Pas de piston."
    elias ecoute "Donc je bossais dur."

    noam reflexion "T'as jamais pensé à arrêter ?"

    elias ecoute "Arrêter pour quoi ?"
    elias jaloux "Pour que je me retrouve dehors ?"
    elias reflechit "Y'avait du taff, fallait que je le fasse, c'est tout."

    "Il secoue la tête, de façon presque imperceptible."

    elias fatigue "Surtout quand il y avait la guerre..."
    "Il pose la paume sur la carcasse froide."

    elias ecoute "Une panne, ça ne prévient pas."
    elias reflechit "Et ça ne se discute pas."

    noam hesitation "La guerre, d'une certain façon tu étais concerné toi aussi ..."

    elias ecoute "C'est clair, tu ne peux même pas imaginer ..."
    elias reflechit "L'échec, c'est quand tu n'as plus d'outil."
    elias fatigue "Ou plus de temps."
    elias reflechit "Le reste, c'est des ajustements."

    "Il corrige encore, au millimètre."

    elias ecoute "On croit gagner du temps, et on perd tout."
    elias reflechit "Les approximations coûtent plus cher."

    "Je remarque sa fatigue."

    elias fatigue "Je supporte la fatigue."
    elias jaloux "Je ne supporte pas l'inefficacité."

    "Il redresse les épaules."

    elias ecoute "Si tu veux aider, tiens la lampe."
    elias reflechit "Pas besoin de parler."

    "Je tiens la lampe."
    "Il travaille en silence pendant plusieurs minutes."

    elias content "Merci."
    elias content "C'était utile."

    "Le mot sonne comme un compliment."

    elias reflechit "Si tu reviens, viens à l'heure."
    elias ecoute "Je n'attends pas."
    "Il ne plaisante pas."
    "C'est une règle simple."

    $ elias_link = 2

    jump FREE_TIME_END


label elias_link_3:

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "reflechit", 0.70)
    $ showP("noam", "reflexion", 0.25)

    elias ecoute "Je devais réorganiser les stations."
    elias reflechit "Mais il manque des pièces."
    elias reflechit "On fera avec."

    "Il déplace un tapis, puis aligne les haltères."

    elias jaloux "Je n'aime pas l'improvisation."
    elias ecoute "Mais je sais m'adapter."

    "Je lui demande ce qu'il entend par s'adapter."

    elias reflechit "Tu gardes l'objectif."
    elias ecoute "Tu changes la route."

    "Il me montre un support bricolé."

    elias ecoute "J'ai récupéré ça dans le stock."
    elias reflechit "Ça ne devait pas servir ici."
    elias content "Maintenant, si."

    "Je lui demande s'il a souvent dû bricoler comme ça."

    elias ecoute "Tout le temps."
    elias reflechit "Quand tu n'as pas de budget, tu inventes."

    "Sa façon de dire 'inventer' ressemble à 'réparer'."

    elias ecoute "On récupère."
    elias ecoute "On recompose."
    elias jaloux "On ne gaspille pas."

    "Je lui demande s'il déteste le gaspillage."

    elias ecoute "Oui."
    elias reflechit "C'est une insulte à l'effort."

    elias ecoute "Mon quartier, c'était ça."
    elias reflechit "Une pièce qui casse, une autre qui la remplace."
    elias ecoute "Pas de fioritures."

    "Je lui dis que ça demande de la créativité."

    elias jaloux "Non."
    elias reflechit "Ça demande de la discipline."

    "Il essuie un banc."

    elias ecoute "On a appris à respecter ce qui tient."
    elias reflechit "Si ça tient, tu ne touches pas."
    elias content "Si ça lâche, tu répares."

    "Je remarque qu'il garde tout à distance."

    elias reflechit "Je ne suis pas là pour faire joli."
    elias ecoute "Je suis là pour que ça marche."

    "Je lui demande s'il s'autorise un moment de pause."

    elias ecoute "Quand tout tient."
    elias reflechit "Pas avant."

    "Il vérifie le serrage d'une vis."

    elias reflechit "Je fais pareil avec les gens."
    elias ecoute "Je regarde s'ils sont fiables."

    "Je demande comment il juge ça."

    elias ecoute "Tu vois qui tient sa parole."
    elias reflechit "Qui arrive à l'heure."
    elias ecoute "Qui termine ce qu'il commence."

    "Je lui demande s'il pardonne les erreurs."

    elias reflechit "Une fois."
    elias jaloux "Après, c'est un choix."

    "Il replace un tapis, puis souffle."

    elias ecoute "Je ne suis pas dur."
    elias reflechit "Je suis constant."

    "Il lève les yeux, une seconde."

    elias jaloux "Le reste, c'est du bruit."

    "Je lui demande s'il croit aux promesses."

    elias reflechit "Je crois aux actes."
    elias ecoute "Les promesses, ça se casse."

    "Il replace une série d'haltères."

    elias reflechit "Même ici, je note tout."
    elias ecoute "Qui utilise quoi."
    elias ecoute "Ce qui s'use."

    "Je lui dis qu'il ressemble à un chef d'atelier."

    elias ecoute "Je ne cherche pas à diriger."
    elias reflechit "Je cherche à éviter les pertes."

    "Il ajuste encore un dernier détail."

    elias ecoute "Quand les choses sont rangées, tu peux penser."
    elias reflechit "Quand c'est le chaos, tu subis."

    "Je lui demande s'il subit, ici."

    elias ecoute "Pas encore."
    elias reflechit "Mais je reste prêt."

    "Il souffle, puis se remet en place."

    elias reflechit "L'effort calme."
    elias fatigue "L'improvisation épuise."

    "Je comprends qu'il parle de plus que du sport."
    "Il reste concentré."
    "Tout est à sa place."

    $ elias_link = 3

    jump FREE_TIME_END


label elias_link_4:

    scene bg_maintenance at adaptive_fullscreen

    $ showP("elias", "neutre", 0.68)
    $ showP("noam", "reflexion", 0.25)

    elias reflechit "Les règles évitent les discussions inutiles."
    elias ecoute "Tout le monde sait quoi faire."
    elias reflechit "Pas besoin d'interpréter les intentions."

    "Il trace une ligne imaginaire sur la table."

    elias ecoute "Là, c'est clair."
    elias reflechit "Là, c'est flou."

    "Je lui demande s'il n'a jamais eu envie de sortir du cadre."

    elias ecoute "Le cadre protège."
    elias reflechit "Sans cadre, tu passes ton temps à négocier."

    "Il classe des outils par taille."

    elias ecoute "J'ai vu des gens tout perdre pour une mauvaise décision."
    elias reflechit "Un retard."
    elias fatigue "Une prise de risque inutile."

    "Je lui demande si c'est arrivé dans sa famille."

    elias ecoute "Un accident."
    elias fatigue "Un mois sans salaire."
    elias reflechit "Tu apprends vite."

    "Il reste factuel, mais le silence qui suit est plus long."

    elias ecoute "On n'avait pas de réserve."
    elias reflechit "Pas d'excuse."
    elias ecoute "Juste un trou à combler."

    "Je lui demande comment ils ont tenu."

    elias ecoute "Heures en plus."
    elias fatigue "Moins de sommeil."
    elias reflechit "Plus d'effort."

    "Il range des clés plates avec soin."

    elias ecoute "Ça forge."
    elias fatigue "Ça épuise aussi."

    "Je lui demande ce qu'il aurait voulu à ce moment-là."

    elias reflechit "Un mois de calme."
    elias ecoute "C'est tout."

    "Je comprends qu'il parle encore en termes de réparation."

    elias reflechit "Le vote, c'est bien."
    elias ecoute "Si le cadre est clair."
    elias jaloux "Sinon, c'est du bruit."

    "Je lui demande s'il a déjà douté d'un cadre."

    elias ecoute "Oui."
    elias reflechit "Quand il est injuste."
    elias fatigue "Mais on fait avec."

    "Il resserre sa prise sur un tournevis."

    elias reflechit "Changer un cadre, c'est du chantier."
    elias jaloux "On ne fait pas ça en parlant."

    "Je lui demande s'il se sent écouté, ici."

    elias ecoute "Je ne parle pas beaucoup."
    elias reflechit "Je fais."

    "Il me lance un regard rapide."

    elias jaloux "Les mots, ça se tord."
    elias ecoute "Les gestes, non."

    elias reflechit "Tu veux me comprendre ?"
    elias ecoute "Regarde ce que je tiens."

    "Je regarde ses mains."
    "Elles sont marquées, mais calmes."

    elias ecoute "J'ai appris à rester debout."
    elias reflechit "Même quand tout le monde se plaint."

    "Je lui demande s'il n'a jamais eu envie d'être reconnu."

    elias reflechit "La reconnaissance, ça ne répare rien."
    elias ecoute "Si je fais bien, ça tient."

    "Il range un outil dans son étui."

    elias ecoute "Je respecte ceux qui travaillent."
    elias reflechit "Les autres, je les laisse parler."

    "Je lui demande s'il se sent indispensable."

    elias reflechit "Je ne pense pas comme ça."
    elias ecoute "Je fais ce qu'il faut."

    "Il s'arrête, réfléchit."

    elias reflechit "Si je ne le fais pas, quelqu'un d'autre devra."
    elias ecoute "Alors autant le faire bien."

    "Sa logique est simple, mais solide."

    elias ecoute "Je ne cherche pas à convaincre."
    elias reflechit "Je cherche à éviter les erreurs."

    "Je hoche la tête."
    "Le bruit d'un outil qui claque marque la fin de la discussion."

    elias ecoute "Si ça tient, c'est suffisant."
    elias reflechit "Si ça casse, on répare."
    elias ecoute "C'est ma ligne."

    "Il ne sourit pas, mais il est clair."
    "La conversation est close."

    $ elias_link = 4

    jump FREE_TIME_END


label elias_link_5:

    scene bg_gymnase at adaptive_fullscreen

    $ showP("elias", "fatigue", 0.70)
    $ showP("noam", "reflexion", 0.25)

    "La salle est presque vide."
    "Il essuie une barre, lentement."

    elias fatigue "Je dors mal quand les choses sont mal définies."
    elias ecoute "C'est tout."

    "Je lui demande ce qui le tient éveillé."

    elias reflechit "Les listes incomplètes."
    elias ecoute "Les tâches laissées en plan."
    elias jaloux "Les gens qui promettent et disparaissent."

    "Il range un disque et se redresse."

    elias reflechit "Je ne supporte pas les dettes."
    elias ecoute "Pas seulement l'argent."
    elias reflechit "Les dettes de temps."
    elias ecoute "Les dettes d'effort."

    "Je lui dis que ça fait beaucoup à porter."

    elias ecoute "Je porte."
    elias reflechit "J'ai toujours porté."

    "Il inspire, puis reprend plus doucement."

    elias reflechit "Ce n'est pas du courage."
    elias ecoute "C'est une habitude."

    elias fatigue "Quand j'étais plus jeune, j'avais peur de tomber malade."
    elias ecoute "Parce que personne ne te remplace."

    "Je lui demande s'il a eu quelqu'un sur qui compter."

    elias ecoute "Ma sœur."
    elias reflechit "Elle comptait sur moi."
    elias ecoute "C'était clair."

    "Le mot "clair" revient, comme un repère."

    elias content "Je lui ai appris à réparer un moteur."
    elias ecoute "Elle m'a appris à dormir quand c'est possible."

    "Je lui demande si elle lui manque."

    elias reflechit "Oui."
    elias ecoute "Mais je ne m'arrête pas pour ça."

    "Il regarde la barre comme si elle pesait plus lourd."

    elias reflechit "Elle voulait que je parte."
    elias ecoute "Que je prenne ma chance."
    elias content "Alors je la prends."

    "Je remarque un sourire très bref."

    elias ecoute "C'était rare."
    elias content "Mais ça comptait."

    "Je lui demande s'il pense à elle ici."

    elias ecoute "Parfois."
    elias reflechit "Quand je répare quelque chose."

    "Il se passe une main sur le front."

    elias fatigue "Le manque de contrôle, ça te ronge."
    elias reflechit "Alors je contrôle ce que je peux."

    "Je lui demande s'il a déjà craqué."

    elias ecoute "Une fois."
    elias reflechit "J'ai ri."
    elias fatigue "Pas parce que c'était drôle."

    "Il semble presque gêné."

    elias reflechit "Le rire, c'est quand la pression lâche."
    elias ecoute "Après, tu reviens."

    elias fatigue "C'était quand j'avais trop poussé."
    elias reflechit "Mon corps a dit stop."

    "Je lui demande s'il écoute son corps maintenant."

    elias ecoute "Je l'écoute."
    elias reflechit "Je lui demande juste de tenir."

    "Il s'assoit, un instant."

    elias reflechit "Je ne cherche pas l'affection."
    elias ecoute "Je cherche la stabilité."

    "Je lui dis que la stabilité, c'est aussi des gens."

    elias ecoute "Oui."
    elias reflechit "Mais des gens fiables."

    "Je lui demande ce qu'il considère comme fiable."

    elias ecoute "Quelqu'un qui revient."
    elias reflechit "Quelqu'un qui tient parole."
    elias ecoute "Quelqu'un qui reste quand ça dure."

    "Un long silence s'installe."

    elias ecoute "Tu voulais en savoir plus."
    elias reflechit "Voilà."

    "Il se lève, déjà prêt à repartir."
    "Je comprends que, pour lui, parler est un effort mesuré."

    "Il replace la serviette, alignée avec le banc."
    "Le geste est net."
    "Comme lui."
    "Il retrouve son rythme."
    "Je le laisse travailler."

    $ elias_link = 5

    jump FREE_TIME_END
