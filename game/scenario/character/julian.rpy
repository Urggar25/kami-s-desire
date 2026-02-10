# -----------------------------------------------------------------------
# LIENS — JULIAN
# -----------------------------------------------------------------------

default julian_link = 0


label JULIAN_LINK_INTERACT:

    menu:
        "Passer du temps avec Julian ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if julian_link == 0:
        jump julian_link_1
    elif julian_link == 1:
        jump julian_link_2
    elif julian_link == 2:
        jump julian_link_3
    elif julian_link == 3:
        jump julian_link_4
    elif julian_link == 4:
        jump julian_link_5

    if last_room_label:
        jump expression last_room_label
    return


label julian_link_1:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("julian", "sourire", 0.62)
    $ showP("noam", "reflexion", 0.22)

    julian "Ah, parfait."
    julian "J'avais besoin d'un vrai public."
    julian "Enfin… d'une personne avec des réactions lisibles."

    "Julian se tourne vers la baie vitrée comme s'il était déjà sur une scène."

    julian "Bon."
    julian "J'ai trois idées pour améliorer les annonces du Conclave."
    julian "Version efficace, version épique, version qui fait pleurer les gens en douze secondes."

    noam "Tu t'entraînes vraiment sur moi, là ?"

    julian "Évidemment."
    julian "Le timing, ça se travaille."
    julian "Regarde."

    $ showP("julian", "idee", 0.62)

    julian "Version efficace :"
    julian "'Citoyens, voici les décisions validées. Merci de votre rigueur.'"
    julian "Sobre. Propre. On dort tous debout."

    julian "Version épique :"
    julian "'Ce soir, nous écrivons la suite de l'espèce humaine.'"
    julian "Là, tu redresses les épaules sans t'en rendre compte."

    julian "Version émotion :"
    julian "'Chaque choix sauve un visage que vous n'avez jamais vu.'"
    julian "Et boum, silence dans la salle."

    noam "Tu veux convaincre ou impressionner ?"

    $ showP("julian", "taquin", 0.62)

    julian "Les deux."
    julian "Toujours les deux."
    julian "Si personne ne t'écoute, même une bonne idée meurt avant d'exister."

    "Il marche, parle avec les mains, mesure mes micro-réactions."

    julian "Attends, je retente la version épique avec une pause au milieu."
    julian "Écoute bien la coupe."

    julian "'Ce soir…'"
    julian "'… nous écrivons la suite de l'espèce humaine.'"

    noam "Ok, oui, ça marche mieux."

    $ showP("julian", "joie", 0.62)

    julian "Merci !"
    julian "Tu vois ?"
    julian "La pause, c'est un crochet dans l'attention."

    julian "J'adore ce moment précis."
    julian "Quand je sens que l'autre est dedans."
    julian "Pas juste poli."
    julian "Vraiment dedans."

    "Il sourit, puis baisse un peu la voix."

    julian "C'est idiot peut-être, mais…"
    julian "J'aime sortir d'une conversation en laissant une trace."
    julian "Un truc qui reste après."

    noam "Tu veux qu'on se souvienne de toi."

    $ showP("julian", "neutre", 0.62)

    julian "Ouais."
    julian "Exactement."
    julian "Et j'assume."

    "Il reprend vite un ton léger."

    $ showP("julian", "sourire", 0.62)

    julian "Bon, prochain atelier demain."
    julian "Je te fais la version 'discours de victoire'."
    julian "Tu vas adorer."

    noam "Je commence à croire que tu répètes même quand tu dors."

    julian "Possible."
    julian "Mais c'est une discipline noble."
    julian "Le chaos adore les gens préparés."

    "Il me pointe du doigt avec un sourire brillant."

    julian "Et toi, t'es un bon test."
    julian "Quand tu lèves un sourcil, je sais que la phrase est ratée."
    julian "Quand tu penches la tête, je sais que j'ai touché juste."

    noam "Je suis devenu ton baromètre, donc."

    julian "Exactement."
    julian "Un baromètre premium."

    $ julian_link = 1

    jump FREE_TIME_END


label julian_link_2:

    scene bg_observation at adaptive_fullscreen

    $ showP("julian", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    julian "Tu veux un résumé social du Conclave ?"
    julian "J'ai des notes mentales."
    julian "Beaucoup trop de notes mentales."

    noam "Tu observes tout le monde à ce point ?"

    julian "Bien sûr."
    julian "Qui prend de la place."
    julian "Qui parle juste assez pour paraître utile."
    julian "Qui fait semblant de ne pas jouer."

    $ showP("julian", "taquin", 0.62)

    julian "Et qui joue mal."

    "Il s'adosse à la vitre, presque amusé."

    julian "T'as remarqué ?"
    julian "Certains parlent pour proposer."
    julian "D'autres parlent pour se protéger."
    julian "Et quelques-uns parlent pour exister cinq secondes de plus."

    noam "Et toi, tu parles pour quoi ?"

    "Julian garde le sourire une seconde de trop."

    julian "Question piège."
    julian "J'aurais dû la poser avant toi."

    $ showP("julian", "neutre", 0.62)

    julian "Le Conclave, c'est une scène."
    julian "Même quand on prétend que non."
    julian "Posture, ton, rythme, regard."
    julian "Tout compte."

    julian "Regarde les entrées en salle."
    julian "Y en a qui arrivent en s'excusant d'exister."
    julian "Y en a qui arrivent comme s'ils possédaient déjà le verdict."

    noam "Tu juges dur, non ?"

    julian "Je juge précis."
    julian "Parce que je me juge pareil."

    "Il hausse les épaules et détourne les yeux vers l'espace."

    julian "Quand je regarde les autres, je cherche aussi ma place."
    julian "Mon niveau."
    julian "Mon angle."

    $ showP("julian", "decu", 0.62)

    julian "Le pire, c'est les gens naturellement crédibles."
    julian "Ils ouvrent la bouche, tout le monde écoute."
    julian "Sans effort visible."

    noam "Et toi, tu compenses avec l'énergie."

    $ showP("julian", "sourire", 0.62)

    julian "Exact."
    julian "Avec l'énergie, les idées, les blagues, les relances."
    julian "Un peu de mise en scène, quoi."

    julian "Franchement, ça me va."
    julian "Tant que ça marche."

    noam "Et si ça marche pas ?"

    "Il répond sans me regarder."

    $ showP("julian", "neutre", 0.62)

    julian "Alors je recommence autrement."
    julian "Plus net."
    julian "Plus fort."
    julian "Plus juste, si possible."

    julian "Mais je m'arrête pas."
    julian "Hors de question."

    "Il se redresse, retrouve sa vivacité habituelle."

    julian "Demain je refais un tour des postures en direct."
    julian "Qui coupe la parole."
    julian "Qui se protège derrière l'humour."
    julian "Qui a peur de proposer trop tôt."

    noam "Tu vas publier un classement ?"

    $ showP("julian", "taquin", 0.62)

    julian "Jamais."
    julian "Enfin… pas officiellement."
    julian "Mais ça m'aide à lire la pièce."
    julian "Et à choisir quand entrer en scène."

    $ julian_link = 2

    jump FREE_TIME_END


label julian_link_3:

    scene bg_observation at adaptive_fullscreen

    $ showP("julian", "detendu", 0.62)
    $ showP("noam", "reflexion", 0.22)

    julian "Ok, confession du jour."
    julian "J'avais une proposition pour le Conclave."
    julian "Une vraie bonne idée, en plus."

    noam "Pourquoi 'j'avais' ?"

    julian "Parce que je l'ai pas défendue."
    julian "Ou plutôt… pas vraiment."

    "Il rit, mais le son retombe vite."

    $ showP("julian", "taquin", 0.62)

    julian "Je l'ai emballée en blague."
    julian "Comme ça, si personne réagit, je peux dire que c'était pour rire."

    noam "Et personne n'a réagi."

    $ showP("julian", "decu", 0.62)

    julian "Pas vraiment."
    julian "Deux regards vides."
    julian "Un changement de sujet."
    julian "Fin de l'histoire."

    "Il tapote la rambarde du bout des doigts."

    julian "C'était pas révolutionnaire."
    julian "Mais c'était utile."
    julian "Un système de suivi des idées rejetées, pour les retravailler au lieu de les enterrer."

    julian "Tu vois le genre ?"
    julian "Pas sexy."
    julian "Pas spectaculaire."
    julian "Mais intelligent."

    noam "Pourquoi tu n'as pas insisté ?"

    julian "Parce que j'ai senti la salle glisser."
    julian "Et j'ai paniqué."
    julian "Pas extérieurement."
    julian "Intérieurement."

    julian "Alors j'ai souri."
    julian "J'ai fait une vanne."
    julian "Et j'ai laissé mourir le truc."

    "Le silence s'installe un instant."

    noam "Ça t'a touché plus que tu le dis."

    $ showP("julian", "fatigue", 0.62)

    julian "Ouais."
    julian "Carrément."
    julian "C'est con, hein ?"

    julian "On fait genre que ce n'est qu'une proposition parmi d'autres."
    julian "Mais quand il n'y a aucun retour…"
    julian "J'ai l'impression de disparaître avec elle."

    noam "Tu peux la reproposer."

    $ showP("julian", "neutre", 0.62)

    julian "Je vais le faire."
    julian "Cette fois sans blague-parachute."
    julian "Juste clairement."

    julian "Et si ça tombe encore à plat…"
    julian "Ben au moins ce sera vrai."
    julian "Pas un sketch raté."

    $ showP("julian", "sourire", 0.62)

    julian "Merci."
    julian "J'avais besoin de le dire à quelqu'un qui écoute vraiment."

    noam "Tu sais, une idée peut rater au premier passage sans être mauvaise."

    julian "Je sais."
    julian "Intellectuellement, je sais."
    julian "Émotionnellement…"
    julian "C'est une autre cuisine."

    "Il se frotte la nuque et souffle."

    julian "La prochaine fois, je vais tenir la ligne."
    julian "Sans sourire défensif."
    julian "Sans sortie de secours."
    julian "Je veux voir ce que ça donne quand je vais jusqu'au bout."

    $ julian_link = 3

    jump FREE_TIME_END


label julian_link_4:

    scene bg_observation at adaptive_fullscreen

    $ showP("julian", "neutre", 0.62)
    $ showP("noam", "reflexion", 0.22)

    julian "Tu sais ce que le Conclave représente pour moi ?"
    julian "Pas juste un dispositif de survie."
    julian "Pas juste un vote quotidien."

    "Il prend une inspiration lente."

    julian "C'est une scène immense."
    julian "Une chance absurde."
    julian "Un endroit où une idée peut te rendre visible d'un coup."

    noam "Tu le dis sans gêne."

    julian "Pourquoi je me cacherais ?"
    julian "Je veux exister ici."
    julian "Vraiment exister."

    $ showP("julian", "idee", 0.62)

    julian "Faire partie de ceux qu'on écoute."
    julian "Ceux qui déplacent quelque chose."
    julian "Même un peu."

    julian "Depuis le début, je me répète la même phrase :"
    julian "Laisse une trace."
    julian "Même petite."
    julian "Mais nette."

    noam "Tu as peur d'être transparent."

    "Il ne répond pas tout de suite."

    $ showP("julian", "decu", 0.62)

    julian "Disons que j'ai horreur de l'effacement."
    julian "Tu passes, tu parles, tu proposes…"
    julian "Et rien ne reste."

    julian "Cette idée me rend dingue."

    "Il retrouve vite son ton vif, presque volontaire."

    $ showP("julian", "sourire", 0.62)

    julian "Donc je travaille."
    julian "Je peaufine."
    julian "Je teste mes formulations."
    julian "Je prends de la place quand il faut."

    julian "Pas pour écraser les autres."
    julian "Pour ne pas m'effacer moi-même."

    noam "Et si un jour tu n'es plus regardé ?"

    $ showP("julian", "neutre", 0.62)

    julian "Alors il faudra que je crée quelque chose qu'on ne peut pas ignorer."
    julian "Un truc utile."
    julian "Un truc beau, si possible."
    julian "Un truc qui continue sans moi."

    julian "Ça, ce serait une vraie trace."

    "Il regarde la vitre, son reflet, puis moi."

    julian "Parfois j'imagine la fin de cette histoire."
    julian "Les gens dehors qui retiennent trois noms."
    julian "Peut-être deux."
    julian "Peut-être un seul."

    julian "Je veux que le mien existe pour une bonne raison."
    julian "Pas juste parce que j'ai parlé fort."
    julian "Parce que j'ai été utile quand il fallait."
    julian "Parce que j'ai aidé à faire tenir le groupe."

    noam "Tu veux être vu, mais pas vide."

    $ showP("julian", "neutre", 0.62)

    julian "Exactement."
    julian "Si je dois être une voix, je veux qu'elle porte quelque chose."
    julian "Sinon ça ne vaut rien."

    "Il expire, puis sourit légèrement."

    julian "Bref."
    julian "Tu vois le projet."
    julian "Je n'ai pas fini de parler."

    noam "Et c'est probablement une bonne chose."

    julian "Tant mieux."
    julian "J'aurais détesté devenir discret d'un coup."
    julian "Pas maintenant."

    $ julian_link = 4

    jump FREE_TIME_END


label julian_link_5:

    scene bg_observation at adaptive_fullscreen

    $ showP("julian", "vide", 0.62)
    $ showP("noam", "reflexion", 0.22)

    julian "Salut."
    julian "Je fais pas de numéro aujourd'hui."

    "Sa voix est plus basse que d'habitude."

    noam "Ça va ?"

    julian "Oui."
    julian "Enfin…"
    julian "Je sais pas trop."

    "Il reste immobile, les mains dans les poches."

    julian "Tu vois, d'habitude je remplis l'espace."
    julian "Je lance une vanne."
    julian "Je raconte une idée."
    julian "Je capte un regard."

    julian "Là, y a rien qui sort."

    noam "Tu peux rester comme ça."

    julian "Ouais."
    julian "C'est juste… inconfortable."

    $ showP("julian", "fatigue", 0.62)

    julian "J'ai passé tellement de temps à construire une version de moi qui marche en public…"
    julian "Que parfois, quand y a personne à convaincre…"
    julian "Je sais plus quoi faire du reste."

    noam "Du reste ?"

    julian "Du vrai moi, peut-être."
    julian "Ou d'un truc en dessous, j'en sais rien."

    "Il souffle un rire bref, sans joie."

    julian "C'est moche dit comme ça."
    julian "On dirait une phrase de documentaire triste."

    noam "C'est honnête surtout."

    $ showP("julian", "decu", 0.62)

    julian "Peut-être."
    julian "Mais j'aime pas trop cet endroit-là."
    julian "Le moment où y a pas de public."
    julian "Où je peux pas me raccrocher à un effet."

    "Il relève le menton, retrouve un peu d'énergie."

    $ showP("julian", "sourire", 0.62)

    julian "Bref."
    julian "Assez de psy à deux crédits."
    julian "On change de sujet."
    julian "Dis-moi un truc nul, un vrai, qu'on puisse le transformer en idée brillante."

    noam "Tu viens de faire exactement ce que tu disais."

    julian "Je sais."
    julian "Réflexe de survie."

    noam "Peut-être."
    noam "Ou réflexe d'artisan."

    "Il laisse passer une seconde, surpris."

    $ showP("julian", "neutre", 0.62)

    julian "Artisan ?"

    noam "Tu façonnes des mots."
    noam "Tu cherches la forme qui tient."
    noam "Même quand t'es mal, tu continues à fabriquer."

    "Un petit rire lui échappe, plus doux."

    julian "Ok."
    julian "Je prends."
    julian "Artisan un peu perdu, mais artisan quand même."

    "Il sourit, plus fragile qu'avant, mais sincère."

    julian "Merci d'être resté."

    noam "Même sans public, t'es pas vide."
    noam "T'es juste moins protégé."

    julian "... Ouais."
    julian "Vu comme ça, c'est moins flippant."

    $ julian_link = 5

    jump FREE_TIME_END
