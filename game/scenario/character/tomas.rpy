# -----------------------------------------------------------------------
# LIENS — TOMAS
# -----------------------------------------------------------------------

default tomas_link = 0


label TOMAS_LINK_INTERACT:

    menu:
        "Passer du temps avec Tomas ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if tomas_link == 0:
        jump tomas_link_1
    elif tomas_link == 1:
        jump tomas_link_2
    elif tomas_link == 2:
        jump tomas_link_3
    elif tomas_link == 3:
        jump tomas_link_4
    elif tomas_link == 4:
        jump tomas_link_5

    if last_room_label:
        jump expression last_room_label
    return


label tomas_link_1:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("tomas", "reflechit", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Tomas fixe un terminal comme s'il allait lui faire un procès."

    tomas "Noam, juste une seconde."
    tomas "Tu as dit tout à l'heure que ce couloir faisait 'environ dix mètres'."
    tomas "C'est inexact."

    noam "Ah."
    noam "On est sur ce genre de discussion."

    tomas raison "Oui."
    tomas raison "Parce que c'est plutôt onze mètres quarante-deux."
    tomas raison "Et si on inclut l'alcôve latérale, onze mètres quatre-vingt-sept."

    noam "..."

    tomas reflechit "Je l'ai estimé avec les dalles au sol."
    tomas reflechit "Elles font quarante centimètres."
    tomas reflechit "Normalement."

    noam "Normalement ?"

    tomas hesitation "Il y a une variation possible de deux millimètres."
    tomas hesitation "J'ai pris cette marge en compte."

    "Le silence me regarde comme un juge."

    noam "Tu sais que personne n'avait besoin de cette précision ?"

    tomas surpris "Pardon ?"
    tomas panne "Je..."
    tomas panne "Je pensais que c'était utile."

    noam "On parlait juste pour passer le temps."

    tomas culpabilite "Ah."
    tomas culpabilite "D'accord."
    tomas culpabilite "J'ai encore fait ça."

    noam "Fait quoi ?"

    tomas triste "Transformer une phrase légère en rapport technique."
    tomas panne "Enfin... oui."

    noam "C'est pas grave."

    tomas culpabilite "Si, un peu."
    tomas culpabilite "L'ambiance était..."
    tomas culpabilite "Comment dire..."
    tomas culpabilite "Détendue."
    tomas culpabilite "Et je l'ai cassée."

    noam "Tu l'as pas cassée."

    tomas hesitation "Je l'ai fendue ?"
    tomas panne "Non, pardon, c'est pire, comme image."

    noam "Respire."

    tomas "Je suis désolé."
    tomas "Vraiment."
    tomas "Je n'essaie pas de corriger les gens pour les rabaisser."
    tomas "Je corrige parce que..."
    tomas "Parce que j'ai peur qu'un détail faux en cache un autre."

    noam "Même sur la taille d'un couloir ?"

    tomas reflechit "Surtout sur la taille d'un couloir."
    tomas reflechit "Les erreurs insignifiantes sont celles qu'on laisse passer."
    tomas reflechit "Puis on s'habitue."
    tomas reflechit "Et un jour, on s'habitue à pire."

    "Il se frotte la nuque, mal à l'aise d'avoir parlé si vite."

    tomas culpabilite "Je..."
    tomas culpabilite "Pardon, encore."
    tomas culpabilite "Je sais que c'était juste une blague de couloir."

    noam "On peut survivre à ça, t'inquiète."

    tomas neutre "D'accord."
    tomas neutre "Alors je vais faire simple."
    tomas neutre "Le couloir est grand."

    noam "Merci."

    tomas taquin "Relativement."

    noam "Tomas."

    tomas rire "Oui."
    tomas culpabilite "Désolé."

    "Il baisse les yeux, puis esquisse un sourire timide."

    tomas "Je m'entraînerai."
    tomas "À laisser les chiffres tranquilles cinq minutes."
    tomas "Enfin..."
    tomas "Quatre minutes, pour commencer."

    noam "Marché conclu."

    $ tomas_link = 1

    jump FREE_TIME_END


label tomas_link_2:

    scene bg_archive at adaptive_fullscreen

    $ showP("tomas", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Je retrouve Tomas devant un écran figé sur une table statistique."

    noam "Tu tiens le choc ?"

    tomas "Oui."
    tomas "Enfin, probablement."

    noam taquin "Probablement ?"
    noam "T'es à 63,4% de stabilité ?"

    tomas raison "Plutôt 67,1%."
    tomas surpris "..."
    tomas panne "C'était une blague ?"

    noam "Oui."

    tomas "Ah."
    tomas hesitation "J'ai répondu sérieusement."

    "Moment de flottement."
    "Le genre qui dure deux secondes et trois années."

    noam "C'était mignon, en vrai."

    tomas culpabilite "Non."
    tomas culpabilite "C'était une erreur de lecture contextuelle."
    tomas reflechit "Blague détectée trop tard."

    noam "Tu classes vraiment ça comme un incident ?"

    tomas reflechit "Oui."
    tomas reflechit "Incident social mineur."
    tomas reflechit "Cause probable : premier degré automatique."
    tomas reflechit "Conséquence : léger malaise partagé."

    noam "Tu me fais une fiche complète ?"

    tomas taquin "Je peux."
    tomas neutre "J'ai déjà un plan de correction, d'ailleurs."

    noam "Je suis curieux."

    tomas "Étape un : vérifier l'intonation."
    tomas "Étape deux : observer si la phrase est absurde."
    tomas "Étape trois : attendre une demi-seconde avant de répondre."
    tomas "Étape quatre : si doute, demander 'tu plaisantes ?'"

    noam "C'est carré."

    tomas "Je préfère quand c'est carré."
    tomas "Les sous-entendus ne le sont jamais."

    noam "Tu rates souvent les blagues ?"

    tomas "Souvent assez pour m'en souvenir."
    tomas "Pas assez pour m'y habituer."

    "Il tapote l'écran sans le regarder."

    tomas inquiet "Le pire, c'est quand les gens rient"
    tomas inquiet "et que je comprends une minute après."
    tomas inquiet "Je ris en retard."
    tomas inquiet "On dirait un bug."

    noam "Tu peux aussi juste sourire."

    tomas "Oui."
    tomas "Mais parfois on attend une réponse émotionnelle."
    tomas "Et j'arrive avec une analyse."

    noam "C'est ta manière de gérer."

    tomas culpabilite "Je sais."
    tomas culpabilite "Mais ça met de la distance."

    noam "Ou ça te protège."

    tomas reflechit "Les deux, probablement."

    "Il relève enfin la tête."

    tomas taquin "Si ça peut te rassurer,"
    tomas taquin "j'ai compris ta blague en huit secondes."

    noam "Record personnel ?"

    tomas joie "Top trois."
    tomas neutre "Le record reste quatre secondes."
    tomas "C'était en primaire."

    noam "Impressionnant."

    tomas taquin "Merci."
    tomas panne "Je ne sais pas si c'était ironique."

    noam "..."

    tomas rire "Celle-là, je l'ai."

    "Il note quelque chose sur son carnet, très sérieusement."

    noam "Qu'est-ce que t'écris ?"

    tomas reflechit "Incident clos."
    tomas reflechit "Dommages limités."
    tomas reflechit "Présence d'une personne patiente : facteur protecteur."

    noam "Je prends."

    $ tomas_link = 2

    jump FREE_TIME_END


label tomas_link_3:

    scene bg_archive at adaptive_fullscreen

    $ showP("tomas", "raison", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Tomas trie des fragments de données sur une tablette."

    noam "Tu bosses encore ?"

    tomas "Oui."
    tomas "Mais je peux parler."

    noam "J'entendais Iris dire que les infos circulent mal ici."

    tomas mefiant "Elles circulent trop vite."
    tomas mefiant "C'est pire."

    noam "Pourquoi ?"

    tomas raison "Parce qu'une information n'est pas neutre quand elle sort."
    tomas raison "Sa forme change les effets qu'elle produit."
    tomas raison "Son timing aussi."

    noam "Tu veux dire qu'il faut filtrer ?"

    tomas "Il faut contextualiser."
    tomas "Et parfois attendre."

    noam "Attendre peut coûter cher."

    tomas "Parler trop vite aussi."

    "Il marque une pause, les mains immobiles."

    tomas reflechit "Une vérité incomplète peut déclencher une panique complète."
    tomas reflechit "Surtout dans un groupe sous pression."

    noam "T'as déjà vu ça ?"

    tomas hesitation "..."
    tomas hesitation "Oui."

    noam "Où ?"

    tomas mefiant "Avant."
    tomas mefiant "Pas ici."

    noam "Tu peux préciser ?"

    tomas panne "Je préfère rester vague."
    tomas culpabilite "C'est pas contre toi."

    noam "Je sais."

    tomas "On a diffusé un chiffre brut."
    tomas "Sans expliquer les marges."
    tomas "Sans expliquer la source."
    tomas "Les gens ont retenu le pire scénario."
    tomas "Le pire s'est installé avant même d'être réel."

    noam "Et ensuite ?"

    tomas triste "Ensuite, on n'a plus parlé de faits."
    tomas triste "On a parlé de peur."
    tomas triste "Et la peur n'écoute plus."

    "Son regard glisse sur les rayonnages vides."

    tomas "Depuis, je fais attention à l'ordre des mots."
    tomas "À qui parle, et à qui écoute."

    noam "Ça fait beaucoup à porter."

    tomas "Oui."
    tomas "Mais c'est moins lourd que les conséquences."

    noam "Donc tu caches des infos ?"

    tomas mefiant "Non."
    tomas mefiant "Je retarde, parfois."
    tomas mefiant "Le temps d'avoir de quoi ne pas brûler tout le monde."

    noam "Les gens détestent qu'on décide pour eux."

    tomas "Je sais. Moi aussi, je déteste ça."

    "Il ferme la tablette et expire lentement."

    tomas culpabilite "Mais entre mentir"
    tomas culpabilite "et parler trop tôt"
    tomas culpabilite "il existe une zone étroite."
    tomas culpabilite "Je marche dedans."

    noam "Et si tu te trompes ?"

    tomas "Alors je corrige, et j'assume."

    noam "Tu as l'air d'en parler comme d'une règle personnelle."

    tomas reflechit "C'en est une."
    tomas reflechit "Énoncer n'est pas suffisant."
    tomas reflechit "Il faut aussi protéger ce que l'énoncé peut détruire."

    noam "C'est froid, dit comme ça."

    tomas triste "Oui."
    tomas triste "Et pourtant c'est humain."

    noam "Je vois."

    tomas neutre "Merci."
    tomas neutre "Tu n'es pas obligé d'être d'accord."
    tomas neutre "Juste de comprendre que je n'improvise pas."

    noam "Je comprends."

    $ tomas_link = 3

    jump FREE_TIME_END


label tomas_link_4:

    scene bg_archive at adaptive_fullscreen

    $ showP("tomas", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "La salle est calme."
    "Tomas tient un vieux manuel papier trouvé dans un tiroir."

    noam "Je pensais que tu ne jurais que par les bases de données."

    tomas joie "J'aime aussi les livres."
    tomas joie "Surtout les livres."

    noam "Pourquoi 'surtout' ?"

    tomas reflechit "Parce qu'ils sont prévisibles."
    tomas reflechit "Tu les ouvres."
    tomas reflechit "Ils te donnent exactement ce qu'ils contiennent."
    tomas reflechit "Pas de sous-entendu caché dans l'intonation."

    noam "Pas de regard de travers non plus."

    tomas taquin "Oui."
    tomas taquin "Un livre ne me regarde jamais comme si j'avais raté une évidence sociale."

    noam "Ça t'arrive souvent ?"

    tomas "Assez."
    tomas "Je peux tenir une discussion technique une heure."
    tomas "Mais quand quelqu'un pleure,"
    tomas "je perds toutes mes procédures."

    noam "Tu ne sais pas quoi faire ?"

    tomas inquiet "Exactement."
    tomas inquiet "J'ai envie d'aider."
    tomas inquiet "Je ne sais pas si je dois parler."
    tomas inquiet "Me taire."
    tomas inquiet "Toucher l'épaule."
    tomas inquiet "Rester loin."

    noam "Y a pas de manuel universel."

    tomas panne "Voilà le problème."
    tomas panne "Je fonctionne bien avec les manuels."

    noam "Tu peux commencer par être là."

    tomas reflechit "Être là sans résoudre ?"

    noam "Oui."

    tomas hesitation "C'est contre-intuitif."
    tomas hesitation "Quand il y a un problème, je cherche la solution."

    noam "Parfois les gens veulent juste qu'on partage la charge."

    tomas "Je l'oublie."
    tomas "Pas par indifférence."
    tomas "Par réflexe."

    "Il referme le livre très doucement."

    tomas triste "J'ai déjà donné des réponses exactes"
    tomas triste "à des questions qui demandaient surtout de la présence."
    tomas triste "Les mots étaient corrects."
    tomas triste "Le moment, non."

    noam "Tu peux apprendre ça aussi."

    tomas neutre "J'essaie."
    tomas neutre "Je note des choses."
    tomas neutre "Des petites règles."

    noam "Genre ?"

    tomas reflechit "Règle une : ne pas corriger une personne en larmes."
    tomas reflechit "Règle deux : demander 'tu veux une solution ou juste parler ?'"
    tomas reflechit "Règle trois : accepter le silence."

    noam "C'est pas mal du tout."

    tomas culpabilite "C'est artificiel, non ?"

    noam "Non."
    noam "C'est honnête."

    tomas "Honnête, oui."
    tomas "Et un peu gênant."

    noam "Pourquoi gênant ?"

    tomas culpabilite "Parce que je réalise que je comprends mieux les systèmes que les gens."
    tomas culpabilite "Et que les gens vivent mal d'être traités comme des systèmes."

    noam "Le fait que tu le voies déjà, c'est important."

    tomas joie "Merci."
    tomas taquin "J'ajoute ça en règle quatre :"
    tomas taquin "choisir des interlocuteurs patients."

    noam "Très bonne règle."

    tomas neutre "Je la garde."

    $ tomas_link = 4

    jump FREE_TIME_END


label tomas_link_5:

    scene bg_archive at adaptive_fullscreen

    $ showP("tomas", "mefiant", 0.62)
    $ showP("noam", "reflexion", 0.22)

    "Tomas est debout devant l'hologramme éteint."
    "Il semble hésiter à parler, puis se lance."

    tomas "Tu m'as demandé une fois"
    tomas "si j'avais déjà dû taire quelque chose d'important."

    noam "Oui."

    tomas "La réponse est oui."
    tomas "Et pas pour me protéger moi."

    noam "Pour protéger qui ?"

    tomas hesitation "Un groupe."
    tomas hesitation "Des gens qui dépendaient d'une décision rapide."

    noam "Tu avais une vérité dangereuse ?"

    tomas "Une vérité incomplète, surtout."
    tomas "Assez vraie pour faire peur."
    tomas "Pas assez solide pour guider une action juste."

    "Il serre les doigts contre sa paume."

    tomas mefiant "Si je la disais trop tôt,"
    tomas mefiant "certains auraient paniqué."
    tomas mefiant "D'autres auraient attaqué."
    tomas mefiant "Tout le monde aurait cru agir rationnellement."

    noam "Et tu as choisi le silence."

    tomas triste "J'ai choisi d'attendre."
    tomas triste "Quelques heures."
    tomas triste "Le temps de vérifier deux sources."

    noam "Qu'est-ce qui s'est passé ?"

    tomas "Quand j'ai parlé,"
    tomas "c'était plus clair."
    tomas "On a évité le pire immédiat."

    noam "Donc c'était la bonne décision."

    tomas desespoir "Pas complètement."
    tomas desespoir "Pendant ces heures, d'autres ont pris des risques sans savoir."
    tomas desespoir "Personne n'est mort."
    tomas desespoir "Mais certains ont payé le prix de mon délai."

    "Sa voix baisse d'un ton."

    tomas "Je peux justifier le choix."
    tomas "Je peux l'expliquer ligne par ligne."
    tomas "Je peux même le défendre devant un comité."

    tomas culpabilite "Mais je ne peux pas dire"
    tomas culpabilite "qu'il était propre."

    noam "Il n'y avait peut-être pas de solution propre."

    tomas "C'est exactement ça qui fait peur."
    tomas "Comprendre n'efface pas la responsabilité."
    tomas "Et avoir raison ne suffit pas à bien faire."

    "Il s'interrompt."
    "Sa voix vacille légèrement sur la dernière syllabe."

    tomas "Pardon."
    tomas "Je..."
    tomas "Je ne voulais pas que ça sorte comme ça."

    noam "Tu peux."

    tomas "Je sais."
    tomas "C'est juste inhabituel."

    noam "Tu gardes beaucoup de choses."

    tomas reflechit "Oui."
    tomas reflechit "Parce que chaque information ressemble à un levier."
    tomas reflechit "Et je passe mon temps à me demander"
    tomas reflechit "qui sera écrasé quand on appuie dessus."

    noam "Tu n'es pas seul avec ça."

    tomas neutre "Merci."
    tomas neutre "J'ai encore du mal à y croire,"
    tomas neutre "mais merci."

    "Il prend une longue inspiration."

    tomas determine "La prochaine fois,"
    tomas determine "je veux décider mieux."
    tomas determine "Pas seulement plus vite."
    tomas determine "Pas seulement plus juste sur le papier."

    noam "Plus humain ?"

    tomas triste "Oui."
    tomas joie "Même si c'est flou."

    noam "On apprendra en route."

    tomas neutre "D'accord."
    tomas taquin "Et si je recommence à faire un exposé de douze pages,"
    tomas taquin "tu m'arrêtes."

    noam "Promis."

    tomas rire "Bien."

    $ tomas_link = 5

    jump FREE_TIME_END
