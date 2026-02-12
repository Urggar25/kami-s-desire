# -----------------------------------------------------------------------
# LIENS — RYN
# -----------------------------------------------------------------------

default ryn_link = 0

label RYN_LINK_INTERACT:

    menu:
        "Passer du temps avec Ryn ?"
        "Oui":
            $ choice = True
        "Non":
            $ choice = False

    if not choice:
        if last_room_label:
            jump expression last_room_label
        return

    if ryn_link == 0:
        jump ryn_link_1
    elif ryn_link == 1:
        jump ryn_link_2
    elif ryn_link == 2:
        jump ryn_link_3
    elif ryn_link == 3:
        jump ryn_link_4
    elif ryn_link == 4:
        jump ryn_link_5

    if last_room_label:
        jump expression last_room_label
    return

label ryn_link_1:

    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    scene bg_gymnase at adaptive_fullscreen

    $ showP("ryn", "fatigue", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Ryn termine une série de tractions et tombe au sol comme un bloc de métal."
    play sound sfx_drop
    noam "Tu parles souvent de la frontière de LIMEN."
    noam "C'était comment, vraiment ?"
    ryn "Vraiment ?"
    ryn "C'était moche."
    ryn "Pas de chanson."
    ryn "Pas de drapeau au vent."
    ryn "Du froid qui te mâche les os."
    noam "Et les postes ?"
    ryn "Des boîtes en tôle qui grincent."
    ryn "Tu dors assis parce que le lit est pris par les batteries."
    ryn "Tu manges debout parce que si tu t'assois trop longtemps tu gèles."
    noam "Tu exagères un peu."
    $ showP("ryn", "desaccord", 0.70)
    ryn "Non."
    ryn "J'exagère quand je raconte les bagarres."
    ryn "Là je suis gentil."
    noam "Et les rondes ?"
    ryn "Six heures dehors."
    ryn "Puis deux heures à réparer un capteur qui lâche."
    ryn "Puis encore dehors."
    ryn "Le vent coupe ta voix, alors tu communiques en jurant et en gestes."
    noam "Il y avait des civils ?"
    ryn "Toujours."
    ryn "Des familles qui campaient juste derrière la ligne."
    ryn "Des mômes qui savaient reconnaître un tir avant d'apprendre à lire."
    noam "Putain..."
    ryn "Ouais."
    ryn "Et quand ça pétait, tu choisissais vite."
    ryn "Protéger la tour."
    ryn "Ou protéger les gens sous la tour."
    noam "Tu choisissais quoi ?"
    $ showP("ryn", "reflechit", 0.70)
    ryn "Le plus proche."
    ryn "Toujours le plus proche."
    ryn "La théorie, c'est pour les salles propres."
    ryn "À la frontière, c'est une seconde ou un corps."
    play sound sfx_beep
    "Une alerte du gymnase clignote puis s'éteint."
    noam "Tu dis que c'était pas héroïque."
    noam "Mais vous teniez quand même."
    ryn "On tenait parce qu'on n'avait pas l'option de casser."
    ryn "Si je casse, mon voisin casse."
    ryn "Si mon voisin casse, la ligne ouvre."
    ryn "Si la ligne ouvre, y a des gens derrière."
    noam "Donc vous serriez les dents."
    ryn "Et on fermait nos gueules."
    ryn "Les types qui parlent trop longtemps meurent plus vite."
    noam "Tu as perdu des proches là-bas ?"
    ryn "Oui."
    ryn "Des collègues."
    ryn "Un cousin."
    ryn "Une vieille qui me filait du thé brûlé les jours de tempête."
    noam "Une vieille ?"
    ryn "Elle insultait tout le monde."
    ryn "Je l'adorais."
    $ showP("ryn", "fatigue", 0.70)
    ryn "Un soir elle a pas ouvert sa porte."
    ryn "On a compris sans parler."
    noam "Je suis désolé."
    ryn "Garde ton désolé pour les vivants."
    ryn "Les morts, eux, n'entendent plus rien."
    noam "Tu regrettes cette vie ?"
    ryn "Je regrette les visages."
    ryn "Le reste peut crever."
    noam "Même LIMEN ?"
    ryn "LIMEN, c'est pas les murs."
    ryn "C'est les gens qui attendent derrière quand t'es de garde."
    noam "Tu parles d'eux comme d'une famille."
    ryn "Parce que c'en est une."
    ryn "Une famille qui se gueule dessus, se vole des couvertures, se pardonne mal."
    ryn "Mais une famille quand même."
    noam "Pourquoi personne ne raconte ça comme toi ?"
    ryn "Parce que c'est sale."
    ryn "Et les récits officiels aiment le propre."
    noam "Ça t'énerve."
    $ showP("ryn", "colere", 0.70)
    ryn "Ça me fout la rage, ouais."
    ryn "Quand j'entends un ponte dire \"sacrifice nécessaire\", j'ai envie de lui coller ses bottes dans la bouche."
    noam "Ryn..."
    ryn "Quoi ?"
    ryn "Ils parlent en chiffres."
    ryn "Nous on ramasse les morceaux en chair."
    noam "Tu tiens encore debout, malgré tout."
    ryn "Je tiens parce que d'autres ont tenu avant moi."
    ryn "C'est une chaîne, pas une légende."
    play sound sfx_paper
    "Il attrape une serviette, s'essuie le front et souffle longuement."
    noam "Merci d'avoir raconté."
    ryn "Me remercie pas."
    ryn "Retiens juste que la frontière, c'est pas une ligne sur une carte."
    ryn "C'est une file de noms."
    ryn "Et chaque nom compte."
    noam "Compris."
    ryn "Bien."

    $ ryn_link = 1
    jump FREE_TIME_END

label ryn_link_2:

    play music "music/bgm_system_override.mp3" fadein 1.0
    scene bg_sas at adaptive_fullscreen

    $ showP("ryn", "colere", 0.70)
    $ showP("noam", "hesitation", 0.24)

    play sound sfx_door
    "La porte du sas se verrouille derrière nous avec un bruit sec."
    noam "Tu peux me répondre franchement ?"
    ryn "Je réponds jamais autrement."
    noam "Pourquoi tu exploses si vite ?"
    ryn "Parce que là d'où je viens, hésiter coûte cher."
    noam "Ici c'est pas la frontière."
    ryn "Ici non."
    ryn "Mais mon corps, il a pas reçu la note."
    noam "Tu vis en alerte permanente ?"
    ryn "Ouais."
    ryn "Un bruit sec, je me retourne."
    ryn "Un silence trop long, je cherche la merde."
    noam "C'est épuisant."
    ryn "Bienvenue."
    $ showP("ryn", "desaccord", 0.70)
    noam "Tu pourrais respirer avant de gueuler."
    ryn "Respirer, je le fais."
    ryn "Gueuler, c'est le bonus."
    noam "Je suis sérieux."
    ryn "Moi aussi."
    ryn "Quand t'as vu un type mourir parce qu'il a dit \"attends deux secondes\", tu développes des habitudes."
    noam "Qu'est-ce qui s'est passé ?"
    ryn "Patrouille de nuit."
    ryn "Capteur aveugle."
    ryn "On entend un frottement derrière les caisses."
    ryn "Le plus jeune dit \"on vérifie calmement\"."
    ryn "Il fait deux pas."
    ryn "Trop tard."
    play sound sfx_balle
    "Le souvenir traverse sa voix comme un éclat."
    noam "..."
    ryn "Depuis ce soir-là, je préfère paraître con et vivant."
    noam "Donc tu attaques d'abord, tu expliques après."
    ryn "Exact."
    noam "Ça blesse des gens au passage."
    ryn "Je sais."
    ryn "Et ça me fait chier."
    noam "Tu le montres pas."
    ryn "Parce que si je commence à m'excuser sur chaque montée de tension, je me vide."
    noam "Tu crois que t'es obligé d'être dur en permanence."
    $ showP("ryn", "reflechit", 0.70)
    ryn "Obligé ? Non."
    ryn "Conditionné ? Oui."
    noam "C'est pas pareil."
    ryn "Ça change pas la vitesse du réflexe."
    noam "Et quand quelqu'un te contredit ?"
    ryn "Je pousse plus fort."
    noam "Pourquoi ?"
    ryn "Parce que je teste s'il tient."
    noam "C'est violent comme test."
    ryn "Le monde l'est aussi."
    play sound sfx_beep
    "Un bip d'étanchéité coupe notre échange, puis le sas se stabilise."
    noam "Tu as déjà regretté une explosion ?"
    ryn "Tous les mois."
    ryn "Parfois tous les jours."
    noam "Et tu changes rien."
    ryn "Si."
    ryn "Avant je frappais."
    ryn "Maintenant je parle trop fort."
    noam "C'est déjà mieux."
    ryn "Tu vois."
    ryn "Je progresse comme un moteur cassé."
    noam "Tu préfères être trop dur que trop lent."
    ryn "Toujours."
    ryn "Trop dur, tu peux réparer derrière."
    ryn "Trop lent, y a parfois plus personne à réparer."
    noam "Tu crois vraiment que c'est noir ou blanc ?"
    ryn "Non."
    ryn "Je crois juste que le gris tue quand tu restes planté dedans."
    noam "Tu parles comme si chaque seconde était une urgence."
    ryn "Parce qu'une fois sur dix, c'est vrai."
    noam "Et les neuf autres ?"
    ryn "Je passe pour un connard."
    noam "Tu l'acceptes ?"
    $ showP("ryn", "neutre", 0.70)
    ryn "Si ça garde quelqu'un en vie, oui."
    noam "Même moi, quand je te dis de te calmer ?"
    ryn "Surtout toi."
    noam "Pourquoi surtout moi ?"
    ryn "Parce que t'écoutes avant de juger."
    noam "Je juge quand même."
    ryn "Heureusement."
    ryn "Sinon je parlerais à un mur."
    noam "Tu veux que je fasse quoi quand tu montes d'un cran ?"
    ryn "Tu me donnes un fait concret."
    ryn "Pas un sermon."
    ryn "Un truc simple : \"porte fermée\", \"zone vide\", \"risque nul\"."
    noam "Tu réponds à ça ?"
    ryn "Plus vite qu'à \"calme-toi\"."
    noam "Bon."
    noam "Je note."
    ryn "Et moi je note que t'essaies."
    noam "On dirait presque des excuses."
    $ showP("ryn", "colere2", 0.70)
    ryn "Rêve pas."
    ryn "C'est un mode d'emploi, pas un câlin."
    noam "Je prends quand même."
    ryn "Prends et retiens."
    ryn "Parce que quand ça pue, faudra aller vite."

    $ ryn_link = 2
    jump FREE_TIME_END

label ryn_link_3:

    play music "music/bgm_careful_wanting.mp3" fadein 1.0
    scene bg_observation at adaptive_fullscreen

    $ showP("ryn", "inquiet", 0.70)
    $ showP("noam", "reflexion", 0.24)

    "Ryn reste debout face à la vitre d'observation, les poings dans les poches."
    "Ses épaules ne bougent presque pas, comme s'il comptait ses respirations."
    noam "Tu penses à LIMEN ?"
    ryn "Tout le temps."
    noam "À un lieu ?"
    ryn "À des gens."
    noam "Tu m'en parles ?"
    ryn "Mouais."
    ryn "Y avait Sera."
    ryn "Elle réparait les radios avec du fil mâché et de la mauvaise humeur."
    ryn "Y avait Jek."
    ryn "Un mur avec des jambes."
    ryn "Il riait comme une alarme cassée."
    noam "Et ta famille ?"
    ryn "Un frère loin."
    ryn "Une tante qui m'écrivait en me traitant d'idiot courageux."
    noam "Tu les as laissés derrière."
    ryn "Ouais."
    ryn "Et ça me bouffe."
    $ showP("ryn", "reflechit", 0.70)
    noam "Tu pourrais dire que LIMEN t'a usé."
    ryn "LIMEN m'a usé, oui."
    ryn "LIMEN m'a appris à tenir, aussi."
    noam "Tu critiques ta patrie sans arrêt."
    ryn "Parce qu'elle mérite mieux que ses chefs parfois."
    noam "Et pourtant tu la défends."
    ryn "Évidemment que je la défends."
    ryn "Que moi je la traite de bourbier, c'est une chose."
    ryn "Qu'un étranger la crache dessus, c'en est une autre."
    noam "Tu réagis comment ?"
    $ showP("ryn", "colere", 0.70)
    ryn "Mal."
    ryn "Très mal."
    noam "Tu frappes ?"
    ryn "J'essaie de pas le faire."
    ryn "Mais ma mâchoire vote pas toujours comme ma tête."
    noam "Qu'est-ce qui te rend loyal à ce point ?"
    ryn "Les absents."
    ryn "Les vivants fatigués."
    ryn "Les noms qu'on lit à voix basse."
    noam "Pas le gouvernement."
    ryn "Le gouvernement peut aller se faire cuire."
    ryn "Moi je parle de la rue, du poste, des dortoirs pleins."
    noam "De ceux qui comptent sur vous."
    ryn "Voilà."
    noam "Tu te sens responsable d'eux même d'ici ?"
    ryn "Toujours."
    ryn "Chaque vote ici peut retomber là-bas."
    noam "Tu penses vraiment que le Conclave pèse jusque-là ?"
    ryn "On vit dans une chaîne."
    ryn "Tu tires ici, ça vibre au bout."
    play sound sfx_announce
    "Une annonce lointaine traverse la pièce, noyée dans un grésillement."
    noam "Et ceux que tu as perdus ?"
    ryn "Je leur parle parfois."
    noam "Dans ta tête ?"
    ryn "Ouais."
    ryn "Je leur raconte les conneries de la station."
    ryn "Je leur dis que je fais de mon mieux."
    noam "Tu crois qu'ils seraient fiers ?"
    $ showP("ryn", "inquiet", 0.70)
    ryn "J'en sais rien."
    ryn "J'espère juste qu'ils diraient pas que j'ai oublié."
    noam "Tu n'as pas oublié."
    ryn "Non."
    ryn "Et je veux pas oublier."
    noam "Même si ça fait mal."
    ryn "Surtout si ça fait mal."
    ryn "La douleur, c'est la preuve qu'ils comptaient."
    noam "Tu me surprends, parfois."
    ryn "Pourquoi ?"
    noam "Parce que derrière la colère, t'es précis."
    ryn "La colère, c'est juste le bruit."
    ryn "La loyauté, c'est le moteur."
    noam "Belle phrase pour quelqu'un qui déteste la rhétorique."
    $ showP("ryn", "neutre", 0.70)
    ryn "Me fais pas dire des trucs élégants, ça me donne des boutons."
    noam "Trop tard."
    ryn "Ferme-la."
    "Je souris. Lui aussi, à peine."
    noam "Tu retourneras à LIMEN après tout ça ?"
    $ showP("ryn", "determine", 0.70)
    ryn "Oui."
    ryn "Je rentrerai."
    ryn "Même si c'est en boitant."
    ryn "Même si j'aime pas ce que je trouve sur place."
    noam "Pourquoi ce besoin de rentrer ?"
    ryn "Parce qu'on n'abandonne pas les siens quand la tempête continue."
    noam "Tu crois encore à ce mot, \"les siens\" ?"
    ryn "Plus que jamais."
    ryn "Sans ça, on n'est qu'une somme de peurs."
    noam "Et avec ça ?"
    ryn "Avec ça, on fait front."
    noam "Même contre ses propres erreurs."
    ryn "Surtout contre ses propres erreurs."
    ryn "Aimer un endroit, c'est aussi lui gueuler dessus pour qu'il arrête d'être con."
    noam "Tu viens de résumer ta relation à LIMEN."
    ryn "Exact."
    ryn "Je la maudis, je la défends, je la porte."
    ryn "Dans la même phrase, s'il faut."

    $ ryn_link = 3
    jump FREE_TIME_END

label ryn_link_4:

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0
    scene bg_archive at adaptive_fullscreen

    $ showP("ryn", "reflechit", 0.70)
    $ showP("noam", "inquiet", 0.24)

    "Dans l'archive, Ryn fait glisser un dossier fermé d'un bord à l'autre de la table."
    "Le geste tourne en boucle, nerveux, précis, inutile."
    noam "Tu t'es arrêté au milieu de ta phrase tout à l'heure."
    noam "Qu'est-ce que tu voulais dire ?"
    ryn "Rien."
    noam "Mensonge."
    ryn "J'aime pas ce sujet."
    noam "Raison de plus."
    $ showP("ryn", "inquiet", 0.70)
    ryn "Putain..."
    ryn "Bon."
    ryn "Je me demande parfois si se battre suffit."
    "Le silence retombe, dense."
    noam "Merci de le dire."
    ryn "Me remercie pas, ça me fout mal à l'aise."
    noam "Pourquoi ce doute maintenant ?"
    ryn "Parce que j'ai vu des gens tout donner..."
    ryn "...et perdre quand même."
    noam "Tu penses à qui ?"
    ryn "À trop de monde."
    ryn "À Jek qui tenait un couloir seul."
    ryn "À Sera qui réparait une radio sous les tirs."
    ryn "À moi qui hurlais des ordres et qui servais à rien pendant dix secondes."
    noam "Dix secondes qui restent."
    ryn "Ouais."
    ryn "Elles restent comme un caillou dans la gorge."
    noam "Tu te dis quoi, ces jours-là ?"
    ryn "Que j'aurais dû bouger plus vite."
    ryn "Que j'aurais dû anticiper."
    ryn "Que j'aurais dû être partout."
    noam "Personne peut être partout."
    $ showP("ryn", "desaccord", 0.70)
    ryn "Je sais."
    ryn "Mais le cerveau écoute pas la logique quand ça gratte les cicatrices."
    noam "Donc le doute revient."
    ryn "En douce."
    ryn "Souvent la nuit, parfois en pleine phrase."
    noam "Tu en parles à quelqu'un d'autre ?"
    ryn "Non."
    ryn "Parce que je suis censé être le type qui cogne le doute, pas celui qui le nourrit."
    noam "Censé par qui ?"
    ryn "Par tout le monde."
    ryn "Par moi surtout."
    play sound sfx_paper
    "Il ouvre enfin le dossier : des listes de noms, des dates, des annotations sèches."
    noam "Tu les relis souvent ?"
    ryn "Quand je veux me rappeler pourquoi je continue."
    noam "Et ça marche ?"
    ryn "Parfois ça me donne juste envie de casser une table."
    noam "Tu doutes de quoi exactement ?"
    $ showP("ryn", "reflechit", 0.70)
    ryn "De la méthode."
    ryn "Pas de la nécessité de se battre."
    ryn "Juste de la façon."
    noam "Tu te demandes s'il y a autre chose que la force."
    ryn "Ouais."
    ryn "Et j'aime pas cette question parce qu'elle me ralentit."
    noam "Peut-être qu'elle t'évite de refaire les mêmes erreurs."
    ryn "Peut-être."
    ryn "Ou peut-être qu'elle me fait hésiter au pire moment."
    noam "C'est une vraie peur."
    ryn "Tu crois ?"
    noam "Je sais."
    noam "Je l'entends."
    ryn "Ça me saoule que tu m'entendes aussi bien."
    noam "Désolé ?"
    ryn "Non."
    ryn "Continue."
    noam "Tu peux être fort et admettre que t'as des fissures."
    ryn "Je déteste ce mot."
    noam "Fissure ?"
    ryn "Ouais."
    ryn "On dirait que je vais me briser."
    noam "Ou que tu laisses passer la lumière."
    $ showP("ryn", "colere2", 0.70)
    ryn "Putain de phrase poétique."
    ryn "Tu m'agaces."
    noam "Je prends ça pour un progrès."
    ryn "Rêve pas."
    ryn "Mais..."
    ryn "T'as peut-être pas totalement tort."
    noam "Je note la date."
    ryn "Ferme-la."
    "Il passe une main sur son visage, fatigué, puis relève les yeux."
    ryn "J'ai peur d'un truc, en vrai."
    noam "Lequel ?"
    ryn "De devenir juste une machine à répondre au danger."
    ryn "Plus de nuance, plus de recul."
    ryn "Juste coup, riposte, coup, riposte."
    noam "Tu viens de prouver le contraire en en parlant."
    ryn "Ouais."
    ryn "Et maintenant je vais prétendre que cette conversation n'a jamais existé."
    ryn "Parce que j'ai une réputation de tête brûlée à maintenir."
    noam "Très important, effectivement."
    ryn "Absolument."
    noam "Dernière question."
    noam "Quand le doute revient, tu fais quoi ?"
    $ showP("ryn", "neutre", 0.70)
    ryn "Je vérifie mes faits."
    ryn "Je regarde qui je protège."
    ryn "Et je bouge."
    noam "Même en doutant."
    ryn "Surtout en doutant."
    ryn "Le doute peut monter dans le véhicule."
    ryn "Mais c'est pas lui qui prend le volant."
    noam "C'est clair."
    ryn "Bien."
    ryn "Et maintenant, on range ce foutu dossier avant que je change d'avis."

    $ ryn_link = 4
    jump FREE_TIME_END

label ryn_link_5:

    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    scene bg_conclave at adaptive_fullscreen

    $ showP("ryn", "determine", 0.70)
    $ showP("noam", "surpris", 0.24)

    "Avant la séance, Ryn frappe son poing dans sa paume, rythme sec et régulier."
    play sound sfx_clap
    noam "Tu fais peur à la table avant même de t'asseoir."
    ryn "Parfait."
    noam "Tu vas voter comment ?"
    ryn "Pour protéger les miens."
    noam "Même si ça te met tout le monde à dos ?"
    ryn "Même là."
    noam "Tu veux développer ?"
    ryn "Je veux pas faire un discours."
    noam "Fais-le pour moi."
    ryn "T'abuses."
    noam "Oui."
    ryn "Bon."
    ryn "Quand j'entends \"équilibre global\", je traduis \"quelqu'un paiera\"."
    ryn "Je veux savoir qui paie."
    ryn "Et si c'est les miens encore une fois, je bloque."
    noam "Donc ta ligne rouge, c'est eux."
    ryn "Exact."
    noam "Et la morale ?"
    $ showP("ryn", "neutre", 0.70)
    ryn "Chez moi, la morale vient après la survie."
    noam "C'est brutal."
    ryn "La réalité l'est."
    noam "Tu assumes de paraître égoïste."
    ryn "Je préfère paraître égoïste que pleurer des tombes évitables."
    noam "Tu crois pas au bien commun ?"
    ryn "Si."
    ryn "Mais le bien commun, ça commence par des gens vivants."
    noam "Et si protéger les tiens met d'autres en danger ?"
    ryn "Alors je regarde les chiffres, les options, les marges."
    ryn "Je suis pas un animal."
    ryn "Mais je sacrifierai pas les miens pour une idée propre sur papier."
    noam "Tu refuses les sacrifices abstraits."
    ryn "Exactement."
    ryn "Un sacrifice abstrait, c'est juste un mot poli pour dire \"pas mon problème\"."
    noam "Tu crois que les autres s'en foutent ?"
    ryn "Pas tous."
    ryn "Certains s'en foutent pas, mais ils se racontent des histoires pour dormir."
    noam "Et toi, tu dors bien ?"
    ryn "Mieux quand j'ai protégé quelqu'un."
    ryn "Mal quand j'ai laissé passer un risque."
    play sound sfx_beep
    "Un signal de convocation monte dans la salle puis retombe."
    noam "Tu parles souvent de \"les miens\"."
    noam "C'est qui, précisément ?"
    $ showP("ryn", "reflechit", 0.70)
    ryn "Ceux avec qui j'ai pris des coups."
    ryn "Ceux qui partagent l'eau quand y en a pas assez."
    ryn "Ceux qui restent quand ça sent la fin."
    noam "Et si quelqu'un change de camp ?"
    ryn "Alors il sort du cercle."
    noam "Sans appel ?"
    ryn "Y a toujours un appel."
    ryn "Mais faut des actes, pas des larmes."
    noam "Tu sembles dur, mais c'est cohérent."
    ryn "Merci, je crois."
    noam "Tu crains quoi dans ce vote ?"
    ryn "Qu'on habille une purge en compromis."
    noam "Tu penses que c'est possible ici ?"
    ryn "Toujours possible."
    ryn "Les belles phrases sont des armes aussi."
    noam "Et toi, ton arme ?"
    ryn "La mémoire."
    ryn "Je me souviens de qui a payé la dernière fois."
    noam "Tu as une liste mentale."
    ryn "Oui."
    ryn "Noms, dates, conséquences."
    noam "Tu pardonnes ?"
    ryn "Parfois."
    ryn "J'oublie jamais."
    noam "Si je te dis que ta posture est trop rigide ?"
    $ showP("ryn", "desaccord", 0.70)
    ryn "Je te réponds qu'une colonne vertébrale rigide tient mieux qu'une gelée quand ça tremble."
    noam "Image dégueu."
    ryn "Efficace."
    noam "Et si protéger les tiens demande une décision sale ?"
    ryn "Alors je prends la saleté."
    ryn "Je la prends sur moi."
    ryn "Je vais pas demander à un idéal de porter le poids à ma place."
    noam "Tu te vois comme un bouclier."
    ryn "Un bouclier qui gueule, oui."
    noam "Tu as peur d'être injuste ?"
    ryn "Tous les jours."
    ryn "Mais j'ai plus peur d'être passif."
    noam "Tu voteras quoi, au mot près ?"
    $ showP("ryn", "determine", 0.70)
    ryn "Je voterai pour toute mesure qui réduit le risque direct sur les miens."
    ryn "Je rejetterai toute mesure qui leur fait porter la dette d'autrui."
    noam "C'est clair."
    ryn "C'est fait pour."
    noam "Et si on t'accuse de partialité ?"
    ryn "Je dirai oui."
    ryn "Je suis partial."
    ryn "Je suis vivant."
    ryn "Et j'ai choisi mon camp."
    noam "Pas très diplomatique."
    ryn "On m'a jamais payé pour être diplomate."
    noam "Dernière chose."
    noam "Tu regretteras ce vote ?"
    ryn "Peut-être."
    ryn "Mais je le regretterai debout, pas à genoux devant un principe qui laisse crever les miens."
    noam "Message reçu."
    ryn "Bien."
    play sound sfx_announce
    "La convocation finale du Conclave retentit."
    ryn "Allez."
    ryn "On y va."
    ryn "Et cette fois, on laisse personne décider à notre place."

    $ ryn_link = 5
    jump FREE_TIME_END
