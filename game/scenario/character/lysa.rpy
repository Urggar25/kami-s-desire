# -----------------------------------------------------------------------
# LIENS — LYSA
# -----------------------------------------------------------------------

default lysa_link = 0


label LYSA_LINK_INTERACT:

    menu:
        "Passer du temps avec Lysa ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if lysa_link == 0:
        jump lysa_link_1
    elif lysa_link == 1:
        jump lysa_link_2
    elif lysa_link == 2:
        jump lysa_link_3
    elif lysa_link == 3:
        jump lysa_link_4
    elif lysa_link == 4:
        jump lysa_link_5

    if last_room_label:
        jump expression last_room_label
    return


label lysa_link_1:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_repos at adaptive_fullscreen

    $ showP("lysa", "taquin", 0.62)
    $ showP("noam", "reflexion", 0.22)

    lysa taquin "On est toujours en vie."
    lysa taquin "Techniquement, c'est une bonne journée."

    "Elle est affalée au fond du canapé, une canette fermée dans la main."

    noam "Tu appelles ça une bonne journée, toi ?"

    lysa neutre "Je pratique la méthode des attentes basses."
    lysa taquin "Comme ça, impossible d'être déçu."

    "Elle fait tourner la canette entre ses doigts sans l'ouvrir."

    noam "Tu as l'air de prendre tout ça à la légère."

    lysa sourire "À la légère, non."
    lysa taquin "Disons... avec amortisseurs intégrés."

    noam "Et si on enlève les vannes ?"

    "Elle me regarde, un bref silence, puis hausse les épaules."

    lysa neutre "On gagne du temps en les gardant."
    lysa taquin "Et on évite les grandes discussions existentielles avant le repas."

    "Je laisse passer quelques secondes."

    noam "Tu évites surtout qu'on te pose des questions."

    lysa sourire "Exact."
    lysa taquin "Tu vois ? T'apprends vite."

    "Elle tapote la canette contre sa tempe, presque comme un salut."

    lysa neutre "Tant que je plaisante, tout le monde respire."
    lysa taquin "Vous me remercierez tous plus tard."

    "Sa voix est légère, mais son regard reste ailleurs."

    $ lysa_link = 1

    jump FREE_TIME_END


label lysa_link_2:

    scene bg_cafeteria at adaptive_fullscreen

    $ showP("lysa", "neutre", 0.60)
    $ showP("noam", "inquiet", 0.22)

    lysa neutre "J'ai dormi deux heures. Peut-être trois."
    lysa triste "Je sais plus trop."

    "Elle fixe son gobelet vide comme si elle attendait une réponse dedans."

    noam "Tu tiens encore debout avec ça ?"

    lysa triste "On s'habitue."
    lysa neutre "Le corps comprend qu'il n'a pas son mot à dire."

    "Elle cligne des yeux, plus lentement que d'habitude."

    lysa triste "Parfois j'ai l'impression d'être en retard sur ma propre journée."

    "Elle réalise ce qu'elle vient de dire et se redresse aussitôt."

    lysa taquin "Mais t'inquiète, je reste une icône de stabilité émotionnelle."
    lysa taquin "Version collector, batteries non incluses."

    noam "Tu n'es pas obligée de faire semblant avec moi."

    lysa sourire "Je fais pas semblant."
    lysa taquin "Je fais de la mise en scène. C'est plus élégant."

    "Elle force un petit rire, puis détourne les yeux."

    noam "Tu encaisses beaucoup, non ?"

    "Son sourire tient une seconde de trop."

    lysa neutre "Comme tout le monde."
    lysa taquin "Sauf que moi, je facture cher les dommages invisibles."

    "Elle se lève avant que je réponde, récupère un autre café et me tend le premier."

    lysa sourire "Tiens. Boire, c'est déjà un plan de survie."

    $ lysa_link = 2

    jump FREE_TIME_END


label lysa_link_3:

    scene bg_observation at adaptive_fullscreen

    $ showP("lysa", "neutre", 0.62)
    $ showP("noam", "triste", 0.22)

    "On reste un moment sans parler, face à la vitre."

    lysa neutre "Avant, j'avais des envies."
    lysa triste "Des trucs bêtes, mais des envies."

    "Elle garde les yeux sur le vide noir derrière la station."

    lysa triste "Maintenant j'ai surtout des réflexes."
    lysa neutre "Je fais ce qu'il faut, au bon moment."
    lysa neutre "Et la journée passe."

    noam "C'est peut-être juste une mauvaise passe."

    "Elle tique légèrement, puis souffle par le nez."

    lysa taquin "La fameuse mauvaise passe qui dure assez longtemps pour payer un loyer ?"

    noam "Je voulais juste dire que ça peut revenir."

    lysa neutre "Peut-être."
    lysa triste "J'ai arrêté d'attendre que ça revienne tout seul."

    "Je cherche quelque chose à répondre."

    noam "On peut trouver un moyen."

    "Elle hausse les épaules, mal à l'aise."

    lysa taquin "Tu vas me faire une liste ?"
    lysa sourire "Dormir. Respirer. Boire de l'eau. Penser positif."

    noam "Lysa..."

    lysa neutre "Désolée."
    lysa triste "C'est juste que quand on me rassure, j'ai l'impression d'avoir raté une consigne."

    "Elle se frotte les mains, puis reprend une voix plus neutre."

    lysa neutre "Reste là."
    lysa neutre "Parler n'est pas obligatoire."

    $ lysa_link = 3

    jump FREE_TIME_END


label lysa_link_4:

    scene bg_archive at adaptive_fullscreen

    $ showP("lysa", "reflexion", 0.62)
    $ showP("noam", "neutre", 0.22)

    "Lysa referme une tablette d'archives sans la ranger."

    lysa neutre "Tu crois qu'on peut faire le bon choix au mauvais moment ?"

    noam "Je... oui, peut-être."

    lysa reflexion "J'ai pris une décision, il y a longtemps."
    lysa triste "Sur le papier, c'était logique."
    lysa neutre "Propre. Efficace. Défendable."

    "Elle marque une pause, mâchoire serrée."

    lysa triste "Et pourtant, c'est resté collé."
    lysa neutre "Comme une écharde que personne ne voit."

    noam "Tu veux m'en parler ?"

    lysa taquin "Non."
    lysa neutre "Enfin... pas en version complète."

    "Elle s'adosse à l'étagère, les bras croisés."

    lysa neutre "Disons que quelqu'un a payé la note à ma place."
    lysa triste "Et que je continue d'additionner les centimes depuis."

    noam "Tu n'as pas à porter ça seule."

    lysa colere "Évite ça."
    lysa colere "La compassion, c'est joli, mais ça glisse sur moi."

    "Je hoche la tête sans insister."

    "Elle finit par reprendre, plus bas."

    lysa neutre "Je dis pas ça pour que tu me consoles."
    lysa triste "Je dis ça parce que si je le garde trop longtemps, ça déborde."

    noam "D'accord. Je t'écoute."

    "Elle acquiesce, presque imperceptiblement."

    $ lysa_link = 4

    jump FREE_TIME_END


label lysa_link_5:

    scene bg_dortoir at adaptive_fullscreen

    $ showP("lysa", "triste", 0.60)
    $ showP("noam", "neutre", 0.22)

    "Lysa est assise au sol, dos au lit, les genoux remontés."
    "Je m'installe à côté d'elle sans rien dire."

    "Le silence dure longtemps, mais il ne pèse pas."

    lysa neutre "Tu sais..."
    lysa neutre "D'habitude, quand quelqu'un reste, il cherche une solution."

    noam "J'en ai pas, aujourd'hui."

    lysa sourire "Tant mieux."

    "Elle pose sa tête contre le bord du lit."

    lysa triste "Je n'ai pas l'énergie pour être réparée."
    lysa neutre "Juste... pas être seule, c'est déjà bien."

    "Je hoche la tête."
    "On reste là, à écouter les bruits lointains de la station."

    lysa neutre "Je vais pas te dire que ça va."
    lysa triste "Ce serait faux."

    noam "Tu n'as pas besoin de le dire."

    "Ses épaules se détendent un peu."

    lysa sourire "Merci d'être resté sans mode d'emploi."

    "On ne parle plus."
    "Et, pour la première fois, elle ne joue pas à aller bien."

    $ lysa_link = 5

    jump FREE_TIME_END
