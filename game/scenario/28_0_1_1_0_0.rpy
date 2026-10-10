# =============================================================================
# JOUR 28 — LE TEMPS QUI RESTE
# Route 0_1_1_0_0 — Noam a choisi de montrer la photo a Kami.
# Continuite : Ryn a ete remplace dans la nuit ; Lysa l'est pendant J28.
# Ces informations ne sont jamais revelees au protagoniste ni au joueur ici.
# =============================================================================

default j28_last_vote_announced = False

label _28_0_1_1_0_0_REVEIL:
    $ current_day = 28
    $ day_id = 28
    $ current_period = "Matin"

    scene bg_chambre_iris at adaptive_fullscreen with fade
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5

    "Je me réveille en sursaut lorsque quelque chose tombe sur le sol. Pendant quelques secondes, je cherche la lampe que j'avais gardée près de moi dans les conduits, avant de reconnaître la chambre d'Iris."
    "Elle vient de renverser sa tasse en essayant de poser sa tablette sur le bureau. Elle reste immobile devant la flaque, comme si elle ne comprenait pas ce qu'elle venait de faire."

    $ showGroup([
        ("iris", "fatigue", 0.36),
        ("noam", "fatigue", 0.65),
    ])

    iris fatigue "Merde... C'était la dernière tasse propre."
    noam fatigue "Bouge pas, je vais chercher de quoi essuyer."
    iris fatigue "Laisse. C'est rien, je m'en occupe."

    "Je ramasse malgré tout la tasse et la pose près du lavabo. Iris essuie maladroitement le bureau avec une serviette, puis abandonne en constatant qu'elle ne fait qu'étaler le café."
    "Nous avons fini par revenir ici pendant la nuit. Nous avons dormi dans le même lit, sans même prendre la peine de retirer nos vêtements."

    iris inquiet "J'ai rêvé de Nyra. Enfin, je crois. Chaque fois que je fermais les yeux, j'entendais Elen lui demander de se réveiller."
    noam fatigue "Moi, je revoyais Ryn quand on l'a retenu à l'infirmerie. J'arrête pas de me demander si on aurait dû écouter ce qu'il essayait de nous dire."
    iris reflexion "On l'a écouté. Seulement, ce qu'il raconte ne correspond pas à ce que les autres ont vu."
    noam reflexion "C'est justement pour ça que je veux retourner le voir. Sans Tomas, sans Kael et sans Elias autour de lui."

    "Iris pose la serviette, puis se tourne vers moi."
    iris inquiet "Tu crois qu'il te dira autre chose ?"
    noam raison "Hier, il pouvait même pas terminer une phrase sans que quelqu'un lui demande de se calmer. Je voudrais au moins savoir ce qu'il a vu avant que Nyra tombe."
    iris determine "Alors je viens. Et essaie même pas de me dire que t'as besoin de lui parler seul, je te laisserai pas traverser le Conclave sans moi."
    noam sourire "J'allais pas te le demander."
    iris blase "Tant mieux. Ça m'évitera de devoir t'engueuler avant le petit-déjeuner."

    "Elle tente de sourire, mais son regard s'arrête sur la serviette tachée de café."
    "Un instant, j'ai l'impression qu'elle va se remettre à pleurer. Elle se contente de la jeter dans la corbeille et récupère sa veste."

    $ hideGroup()
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "Le couloir de l'infirmerie est désert lorsque nous arrivons. La lumière est encore réglée sur le cycle du matin, bien que je n'aie aucune idée du nombre d'heures que nous avons réellement dormi."
    "Sael sort d'une petite pièce, une trousse à la main. Elle nous voit approcher et ralentit aussitôt."

    $ showGroup([
        ("sael", "fatigue", 0.24),
        ("iris", "inquiet", 0.50),
        ("noam", "reflexion", 0.76),
    ])

    sael fatigue "Vous venez pour Ryn ?"
    noam raison "Oui. Je voudrais reprendre avec lui ce qui s'est passé dans les conduits. Il est réveillé ?"
    sael fatigue "Depuis un moment. Il a fini par accepter de manger un peu, mais je préférerais que vous évitiez de le provoquer."
    iris desaccord "On vient lui parler, Sael. Pas le mettre en colère pour le plaisir."
    sael raison "Je sais. Je vous préviens seulement qu'il a très mal vécu la nuit. Nous avons dû l'attacher lorsqu'il a essayé de se lever malgré les consignes."

    "Je regarde la porte au fond du couloir. Hier soir, les menottes étaient encore sur une table. Apparemment, la situation a changé après notre départ."
    noam inquiet "Il a blessé quelqu'un ?"
    sael fatigue "Non. Et c'est justement pour éviter d'en arriver là que je l'ai immobilisé."
    sael raison "Je resterai dans la pièce d'à côté. Si quelque chose vous inquiète, appelez-moi."

    "Iris attend qu'elle soit partie avant d'ouvrir la porte."

    $ hideGroup()
    scene bg_infirmerie at adaptive_fullscreen with dissolve

    "Ryn est allongé sur un lit de soins. Ses poignets sont maintenus par des attaches épaisses, fixées de part et d'autre du cadre."
    "Il tourne la tête en nous entendant entrer, puis regarde immédiatement ses mains, comme s'il venait de se rappeler pourquoi il ne peut pas bouger."

    $ showGroup([
        ("ryn", "fatigue", 0.24),
        ("iris", "inquiet", 0.50),
        ("noam", "inquiet", 0.76),
    ])

    ryn fatigue "Vous êtes encore venus me demander si j'ai tué Nyra ? Je vous ai déjà dit ce qui s'est passé."
    noam raison "Justement. Hier, tu accusais Tomas. Je veux reprendre depuis le moment où votre groupe s'est séparé du nôtre."
    ryn colere "J'en sais rien, Noam ! On avançait dans les conduits, il y a eu des cris et quand j'ai regardé..."

    "Il s'interrompt et fixe la couverture. J'attends qu'il reprenne, mais les secondes passent sans qu'il relève les yeux."
    noam inquiet "Ryn, si tu sais quelque chose, dis-le. Tomas et Kael racontent la même chose, Elias aussi, et Nyra ne pourra plus nous expliquer ce qu'elle a vu."
    ryn fatigue "C'est moi."
    noam surpris "Quoi ?"
    ryn colere "C'EST MOI, PUTAIN ! C'est moi qui l'ai frappée ! Tu voulais que je le dise ? Ben voilà, c'est dit !"

    "Je reste debout devant lui, incapable de comprendre comment nous sommes passés de ses accusations contre Tomas à ces quelques mots."
    "Iris se rapproche du lit, mais Ryn détourne la tête avant même qu'elle ait pu parler."

    iris inquiet "Attends... Hier, tu nous as juré que Tomas lui avait fait ça. Tu nous as regardés dans les yeux, Ryn."
    ryn fatigue "Je sais. J'avais peur, d'accord ? J'étais là, elle bougeait plus, j'avais du sang partout et tout le monde me regardait... J'ai dit n'importe quoi."
    noam inquiet "Mais pourquoi l'avoir frappée ? Vous vous êtes disputés ? Elle t'a dit quelque chose ?"
    ryn fatigue "Non. C'est ça qui me rend dingue. Elle marchait devant moi, elle a tourné la tête, et j'ai eu... une espèce de pulsion."
    ryn fatigue "Je l'ai attrapée par la tête et je l'ai cognée contre la paroi, juste à côté de nous. Je sais même pas ce que j'essayais de faire."

    "Il ferme les yeux. Ses lèvres bougent quelques secondes avant que sa voix redevienne audible."
    ryn peur "Quand je suis revenu à moi, j'étais à genoux près d'elle. Je l'appelais et elle répondait pas. J'ai cru qu'elle allait se réveiller."
    ryn peur "Je peux pas vous expliquer pourquoi j'ai fait ça. J'en sais rien... J'aimerais tellement que ce soit Tomas."

    "Il tire faiblement sur ses attaches, puis s'immobilise lorsqu'elles lui résistent."
    "Je pense aux pleurs que nous avons entendus dans les conduits et à la façon dont il essayait de soulever Nyra. Rien ne ressemble à un aveu que j'aurais pu imaginer."

    noam reflexion "Tu te rappelles avoir continué à la frapper après le premier coup ? Tomas dit qu'il a essayé de t'arrêter."
    ryn fatigue "Je me souviens de l'avoir saisie, puis d'être à côté d'elle. Entre les deux, c'est flou. Je sais que ça arrange rien, mais je peux pas inventer ce qui manque."
    iris inquiet "Et tu n'as absolument rien ressenti avant ? Pas de vertige, de douleur, quelque chose d'inhabituel ?"
    ryn fatigue "Non, Iris. Je marchais et, d'un coup, j'ai fait ça. J'aurais préféré avoir une raison, même une saloperie de raison."

    "Iris recule légèrement. Elle fixe les attaches comme si elle cherchait à savoir à quel moment il aurait pu les enlever."
    "Ryn suit son regard et serre les dents."

    ryn fatigue "Vous pouvez me laisser comme ça, si vous voulez. Je sais pas ce qui m'a pris et j'ai pas envie de recommencer sur quelqu'un d'autre."
    noam inquiet "Je vais parler à Sael. Elle doit pouvoir chercher ce qui a provoqué cette perte de contrôle."
    ryn fatigue "Fais ce que tu veux. Mais si tu croises Elen, lui raconte pas ça comme si..."

    "Il n'achève pas sa phrase. Il se tourne vers le mur et ne nous regarde plus."
    "Iris pose une main sur mon bras. Nous quittons la chambre sans lui demander de continuer."

    $ hideGroup()
    scene couloir_infirmerie at adaptive_fullscreen with dissolve

    $ showGroup([
        ("iris", "reflexion", 0.37),
        ("noam", "inquiet", 0.64),
    ])

    iris reflexion "Hier, il aurait voulu étrangler Tomas pour nous convaincre que c'était lui. Aujourd'hui, il dit exactement le contraire."
    noam reflexion "Tu l'as entendu comme moi. S'il ment encore, je comprends pas ce qu'il pense gagner à reconnaître un meurtre."
    iris inquiet "Moi non plus. Mais ça me rassure pas de le voir aussi... Enfin, tu vois bien."
    noam inquiet "Aussi calme ?"
    iris reflexion "Pas calme. J'arrive pas à trouver le mot. On dirait qu'il a renoncé à nous convaincre de quoi que ce soit."

    "Nous restons quelques instants dans le couloir, sans savoir ce que nous sommes censés faire de ce qu'il vient de nous raconter."
    "Au bout de la galerie, j'entends Sael parler avec quelqu'un. Je décide de ne pas l'interrompre immédiatement."

    $ hideGroup()
    stop music fadeout 1.0
    jump _28_0_1_1_0_0_ANNONCE


label _28_0_1_1_0_0_ANNONCE:
    $ current_period = "Matin"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    "À la cafétéria, Julian n'a pratiquement pas touché à son plateau. Elen est assise près de lui et tourne lentement une cuillère dans un verre vide."
    "Quand je leur demande s'ils ont vu les autres, Julian me répond qu'ils viennent de partir chercher Sael. Elen ne lève même pas la tête."

    $ showGroup([
        ("julian", "fatigue", 0.22),
        ("elen", "fatigue", 0.43),
        ("iris", "inquiet", 0.64),
        ("noam", "fatigue", 0.85),
    ])

    julian fatigue "Si tu viens parler de Ryn, je t'en supplie, attends au moins qu'on ait fini de manger. On a passé toute la nuit à écouter les autres se disputer."
    noam inquiet "Je viens de le voir. Il m'a avoué avoir frappé Nyra."

    "La cuillère s'arrête contre le bord du verre. Elen garde les yeux baissés, mais sa main commence à trembler."
    elen peur "Il a dit quoi ?"
    noam inquiet "Il a reconnu l'avoir frappée contre une paroi. Il prétend avoir eu une pulsion et ne plus se souvenir clairement de la suite."
    elen colere "Une pulsion ?! C'est tout ce qu'il trouve ?! Il a tué Nyra et il sait même pas pourquoi ?!"

    "Elle repousse son verre. Julian tend une main vers elle, mais la retire avant de la toucher."
    elen peur "Hier, j'arrêtais pas de me dire qu'il y avait eu une erreur. Qu'on allait finir par comprendre... Et lui, pendant ce temps, il savait ?"
    iris inquiet "Elen, on ne sait pas s'il était capable de raconter les faits hier. Il avait l'air complètement perdu."
    elen colere "Mais Nyra, elle, elle est morte ! Vous pouvez trouver toutes les excuses que vous voulez, ça changera rien !"

    "Elle se lève si brusquement que sa chaise recule contre la table. Julian essaie de l'appeler, mais elle est déjà dans le couloir."
    "Je fais un pas pour la suivre. Iris m'arrête d'une main et me montre Julian, qui fixe encore la chaise vide."

    julian fatigue "Laissez-la. Elle a passé la moitié de la nuit à me demander pourquoi personne avait réussi à retenir Ryn. Je crois qu'elle a surtout besoin de ne plus nous entendre parler."

    "Il saisit enfin son plateau, puis le repose sans avoir mangé."
    julian inquiet "Et toi, Noam... T'es sûr qu'il a vraiment dit ça ? Il aurait pu avouer n'importe quoi pour qu'on arrête de le questionner."
    noam fatigue "Je sais seulement ce qu'il m'a dit. Iris était là tout le temps."
    iris reflexion "C'était pas une confession qu'on lui a arrachée. Il a changé de version presque immédiatement. Je sais pas ce que ça vaut, mais c'est ce qu'on a entendu."

    "Une série de notes aiguës retentit au-dessus de nos têtes. Les écrans de la cafétéria s'allument les uns après les autres."
    "Je relève immédiatement les yeux vers la caméra."

    play sound "audio/trailer/trl_alarm_low.wav"
    pause 1.0
    $ hideGroup()
    scene bg_diffusion_champagne at adaptive_fullscreen with dissolve
    kami "Mes très chers représentants ! J'espère que vous profitez pleinement de votre avant-dernier jour complet dans le Conclave !"

    "Julian regarde la porte par laquelle Elen vient de sortir. Je distingue ses doigts se refermer lentement sur le bord de la table."
    kami "Dans deux jours, il sera temps de conclure cette merveilleuse expérience. Notre dernier et ultime vote aura lieu au jour trente, à huit heures précises."
    kami "Cette fois, je vous propose une petite modification de nos habitudes. Une amélioration, si vous préférez !"
    kami "Quiconque ne respecte pas un Commandement aura désormais la mémoire effacée, plutôt que d'être éliminé."

    "Je reste un moment sans réagir. J'attendais une remarque sur Nyra, peut-être même une réponse à la photographie que j'ai montrée hier. Kami vient pourtant d'annoncer cela avec le ton qu'elle prend d'habitude pour présenter un divertissement."

    $ bc_show("julian", "colere")
    julian colere "Tu peux pas être sérieuse ! Nyra est morte et tu viens nous annoncer un nouveau vote comme si on allait tous tranquillement rentrer chez nous ?!"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Julian, je suis ravie de voir que tu conserves ton enthousiasme pour la vie démocratique ! Je précise toutefois que le texte ne sera soumis au vote que dans deux jours."
    $ bc_show("noam", "colere")
    noam colere "Kami, on a retrouvé deux corps dans cette station ! Tu m'as entendu hier, je t'ai montré la photographie. Tu comptes vraiment continuer sans rien nous expliquer ?"

    $ bc_hide()
    "L'écran affiche toujours le même visage souriant. Quelques secondes passent, puis Kami reprend comme si je n'avais rien demandé."
    kami "Je vous invite à réfléchir aux avantages de cette proposition. Après tout, que vaut une petite infraction si on peut en effacer jusqu'au souvenir ?"
    $ bc_show("iris", "colere")
    iris colere "C'est ça ton idée ? On tue quelqu'un, puis on efface la mémoire du responsable et tout le monde fait comme si rien ne s'était passé ?!"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Oh, Iris ! Quelle façon déprimante de présenter une mesure aussi généreuse. Je vous laisse méditer. À très vite !"

    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "colere", 0.3), ("iris", "colere", 0.6), ("noam", "inquiet", 0.8)])
    "Les écrans s'éteignent avant que Julian ait trouvé quoi lui répondre."
    "Il reste debout face à celui qui se trouve près du buffet, les bras légèrement écartés."

    julian colere "Elle a même pas répondu à la question. Cette saloperie a entendu tout ce qu'on lui a dit et elle s'en fout complètement !"
    noam reflexion "Elle a parlé d'effacer la mémoire. Tu crois qu'elle peut vraiment faire ça ?"
    iris inquiet "J'en sais rien. Mais après ce qu'on a vu dans cette station, j'aimerais éviter de découvrir comment."

    "Une nouvelle notification apparaît sur ma tablette. La convocation du dernier vote vient d'être enregistrée, avec la question exacte et l'heure de la séance."
    $ j28_last_vote_announced = True

    "Je ferme la fenêtre sans la lire une seconde fois."
    "Il nous reste moins de deux jours avant le départ annoncé, et nous ne savons même pas si Kami compte nous laisser rentrer avec ce qui reste du groupe."

    $ hideGroup()
    stop music fadeout 1.0
    jump _28_0_1_1_0_0_APRES_MIDI


label _28_0_1_1_0_0_APRES_MIDI:
    $ current_period = "Après-midi"
    call show_custom_title("Dans l'après-midi")
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "Iris refuse de retourner à l'infirmerie. Après l'annonce de Kami, elle m'a entraîné dans les couloirs, sous prétexte de récupérer quelques affaires avant le prochain vote."
    "Je crois surtout qu'elle ne supporte plus de rester dans une pièce où chacun attend que quelqu'un d'autre décide de ce qu'il faut faire."

    $ showGroup([
        ("iris", "fatigue", 0.37),
        ("noam", "reflexion", 0.64),
    ])

    noam reflexion "Tu voulais aller où, exactement ? On a déjà fait deux fois le tour des dortoirs."
    iris fatigue "N'importe où. J'avais besoin de marcher un peu sans entendre parler de Nyra ou de Ryn à chaque coin de table."
    noam inquiet "On pourrait aller voir Elen. Elle est partie toute seule ce matin et Julian avait l'air inquiet."
    iris inquiet "Je lui ai envoyé un message. Elle m'a répondu qu'elle était avec Lysa, qu'elles voulaient discuter. Je vais pas aller l'obliger à me raconter ce qu'elle ressent."

    "Je sors ma tablette pour vérifier mes messages. Aucun nouveau message de Lysa ; je me rends compte que je ne l'ai pas croisée aujourd'hui."
    "Je n'ai pas le temps d'y réfléchir davantage. Iris me prend soudain le bras et m'attire contre le mur."

    iris inquiet "Noam... Attends."
    noam inquiet "Quoi ?"
    iris inquiet "Regarde là-bas."

    show couloir_dortoir at Transform(zoom=1.65, xalign=0.76, yalign=0.49) with dissolve
    "À l'autre bout du couloir, deux hommes discutent près d'une porte de maintenance. Je reconnais immédiatement la carrure de Ryn, puis les cheveux d'Elias lorsqu'il se tourne vers la lumière."
    "Ryn n'a plus aucune attache aux poignets. Il bouge librement, une main posée contre le cadre de la porte."

    think "Mais... Il était attaché ce matin."

    "Je m'apprête à les appeler lorsque Iris m'entraîne derrière l'angle du couloir. Son visage s'est fermé d'un seul coup."

    $ hideGroup()
    $ showGroup([
        ("ryn", "determine", 0.29),
        ("elias", "reflexion", 0.72),
    ])

    ryn determine "Il nous les faut. Sinon on pourra jamais terminer à temps."
    elias fatigue "Je sais, putain. Mais tu peux pas débarquer comme ça, surtout après ce qui s'est passé hier."
    ryn colere "On n'a plus le luxe d'attendre."

    "Un chariot roule dans un couloir voisin. Le bruit de ses roues couvre la réponse d'Elias, et je ne distingue plus que des mots sans parvenir à en saisir le sens."
    "Je tente de me rapprocher, mais Iris me retient aussitôt par la veste."

    scene couloir_dortoir at adaptive_fullscreen with dissolve
    $ hideGroup()
    $ showGroup([
        ("iris", "peur", 0.36),
        ("noam", "inquiet", 0.65),
    ])

    iris peur "Bouge pas. S'ils tournent la tête, ils vont nous voir."
    noam inquiet "C'est Ryn ! Il a avoué avoir tué Nyra ce matin, et maintenant il se promène avec Elias ?!"
    iris reflexion "Je sais ce que j'ai vu. Attends qu'ils partent."

    "Les voix reprennent, plus basses. Elias prononce le nom de Sael, mais je ne parviens pas à comprendre la suite."
    "Une porte s'ouvre, puis leurs pas s'éloignent. Iris attend encore plusieurs secondes avant de me laisser regarder."

    "Le couloir est vide."
    noam colere "On devrait aller demander à Sael pourquoi elle l'a détaché ! Elle vient de nous dire qu'il était dangereux !"
    iris colere "Et tu vas lui dire quoi ? Qu'on vient d'espionner Ryn et Elias derrière une porte et qu'ils avaient l'air de préparer quelque chose ?"
    noam inquiet "On a quand même entendu ce qu'il a dit. 'Il nous les faut.' Tu crois qu'il parlait de quoi ?"
    iris inquiet "J'en sais rien, Noam. Mais je suis pas pressée de découvrir s'ils parlaient de nous."

    "Elle a prononcé cette dernière phrase presque à voix basse. Je la regarde et constate qu'elle tremble malgré la chaleur du couloir."
    "Depuis la découverte du corps de Mara, Iris s'est accrochée à chaque possibilité d'obtenir une explication. Aujourd'hui, elle semble avoir peur de ce qu'une explication pourrait nous apprendre."

    noam reflexion "Il faut au moins prévenir Julian et Elen. Ils savent même pas que Ryn est dehors."
    iris inquiet "Pas ici. Et pas tant qu'on sait pas où sont les autres. On rentre dans ma chambre d'abord."
    noam inquiet "Tu veux vraiment qu'on se cache ?"
    iris colere "Je veux qu'on reste vivants ! C'est si compliqué à comprendre ?!"

    "Elle se mord immédiatement la lèvre et détourne les yeux."
    iris fatigue "Pardon. Je voulais pas te parler comme ça... Mais je t'en supplie, arrête de foncer vers les gens pour leur demander pourquoi ils se comportent bizarrement."

    "Je pense à Tomas, à Kael et à Elias, qui se sont tous accordés pour désigner Ryn comme le meurtrier de Nyra. À présent, Ryn circule librement à côté d'Elias."
    "La contradiction est si énorme que je ne sais même plus par où commencer."

    noam inquiet "D'accord. On retourne chez toi. Mais on essaie d'abord de prévenir les autres par message."
    iris determine "Oui. Et avant ça, on passe prendre de quoi fermer correctement cette foutue porte."

    $ hideGroup()
    jump _28_0_1_1_0_0_MAINTENANCE


label _28_0_1_1_0_0_MAINTENANCE:
    scene bg_maintenance at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.0

    "La salle de maintenance est presque vide. Les outils sont rangés dans leurs casiers, et une lampe laissée sur l'établi éclaire un tas de pièces détachées."
    "Iris vérifie la porte avant de s'avancer vers les armoires. Elle ne prend rien au hasard : elle teste un tournevis, repose une pince trop encombrante et finit par sortir une petite clé réglable."

    $ showGroup([
        ("iris", "reflexion", 0.37),
        ("noam", "inquiet", 0.64),
    ])

    noam reflexion "T'as déjà décidé ce que tu comptes faire avec tout ça ?"
    iris reflexion "Bloquer la porte. Ou la grille, si quelqu'un essaie de passer par la ventilation. Pour le reste... J'espère surtout qu'on n'aura pas à s'en servir."
    noam inquiet "T'as peur qu'ils viennent nous chercher ?"
    iris colere "J'ai peur d'un type qui avoue avoir tué Nyra et qui se retrouve libre quelques heures plus tard. Et j'ai peur de la façon dont Elias lui parlait. Ça me suffit."

    "Elle glisse le tournevis dans la poche de sa veste et examine plusieurs attaches métalliques. Je l'aide à récupérer deux petites équerres et un morceau de câble assez solide pour tenir une poignée."
    "Pendant que nous refermons le casier, un bruit de pas nous parvient du couloir. Iris éteint immédiatement la lampe de l'établi."

    iris peur "Ne bouge plus."

    "Nous restons contre l'armoire. Les pas ralentissent devant la porte, puis s'arrêtent."
    "Je retiens mon souffle en attendant que la poignée tourne. À la place, j'entends un petit choc métallique, comme si quelqu'un venait de poser quelque chose sur le sol."

    "Le bruit s'éloigne enfin."
    "Iris attend encore avant de rallumer la lampe. Elle me regarde, puis regarde la porte."

    noam inquiet "C'était peut-être juste quelqu'un qui passait."
    iris fatigue "Je sais. Le pire, c'est qu'avant hier, j'aurais même pas réfléchi à un bruit pareil."
    noam raison "On a ce qu'il faut. On devrait pas traîner davantage."

    "Nous sortons en prenant soin de vérifier que personne ne se trouve dans le couloir."
    "Je garde les outils contre ma poitrine, sous ma veste. Iris marche si près de moi que son épaule touche parfois la mienne."

    $ hideGroup()
    stop music fadeout 1.0
    jump _28_0_1_1_0_0_CHAMBRE


label _28_0_1_1_0_0_CHAMBRE:
    $ current_period = "Soir"
    call show_custom_title("En début de soirée")
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0

    "Iris ferme la porte dès que nous sommes entrés. Je pose les outils sur le bureau, puis l'aide à déplacer une commode pour la caler contre l'entrée."
    "Nous passons ensuite plusieurs minutes à vérifier la ventilation. La grille est fixée, mais Iris insiste pour maintenir une pièce de métal contre son bord inférieur."

    $ showGroup([
        ("iris", "fatigue", 0.36),
        ("noam", "reflexion", 0.65),
    ])

    noam reflexion "Avec le meuble devant la porte et la grille bloquée, personne pourra entrer sans faire un sacré vacarme."
    iris fatigue "Ça me convient. Si je dois me faire tuer, j'aimerais au moins avoir le temps de m'en rendre compte."
    noam inquiet "Dis pas ça."
    iris inquiet "Je sais. Je plaisante pas vraiment, en plus."

    "Elle s'assoit au bord du lit et enlève enfin ses chaussures. Ses doigts restent crispés sur les lacets alors qu'elle a déjà terminé."
    "Je récupère ma tablette et ouvre notre conversation avec Julian."

    noam raison "Je vais lui dire qu'on a vu Ryn en liberté. Il faut qu'il sache au moins ça."
    iris reflexion "D'accord. Envoie aussi un message à Elen. Elle est avec Lysa, normalement."

    "J'écris quelques lignes, sans parler de la conversation surprise dans le couloir. Je leur demande de rester ensemble et d'éviter de se déplacer seuls."
    "Julian répond rapidement qu'il a vu Ryn passer près de la cafétéria, mais qu'il ne sait pas pourquoi il a été libéré."
    "Elen ne répond pas."

    noam inquiet "Julian l'a vu aussi. Il dit qu'il va essayer de joindre Sael, mais qu'il reste à la cafétéria pour le moment."
    iris inquiet "Et Elen ?"
    noam fatigue "Rien. Je viens de lui renvoyer un message."

    "Iris prend son téléphone. Je la vois ouvrir la conversation avec Lysa, puis attendre devant l'écran sans écrire."
    noam reflexion "Tu peux lui demander si Elen est toujours avec elle."
    iris fatigue "Je viens de le faire. Elle a lu mon message de ce matin, mais pas celui-là."

    "Je regarde l'heure. Depuis notre retour, nous n'avons croisé personne dans le couloir et aucun bruit ne nous est parvenu de la ventilation."
    "Ce silence devrait me rassurer. Au contraire, il me donne envie de vérifier toutes les cinq minutes si la porte est encore verrouillée."

    iris inquiet "Noam... Si demain matin on découvre que tout va bien, tu pourras me dire que j'ai complètement paniqué. Mais cette nuit, je veux pas ouvrir à qui que ce soit."
    noam inquiet "Même à Julian ou à Elen ?"
    iris reflexion "S'ils ont besoin de nous, ils peuvent appeler. Et on avisera. Mais je veux pas qu'on ouvre juste parce qu'une voix nous dit qu'elle est devant la porte."

    "Je m'apprête à lui répondre que c'est peut-être excessif, puis je repense au visage de Mara sur la photographie."
    "Si une personne peut avoir exactement son visage, je n'ai aucune raison de croire qu'une voix suffira à reconnaître qui se trouve derrière une porte."

    noam fatigue "D'accord. On reste ici pour ce soir."

    "Iris relève enfin les yeux. Elle semble soulagée que je n'essaie pas de discuter plus longtemps."
    iris fatigue "Viens te coucher. Je vais laisser une petite lumière, au cas où on doive bouger."
    noam sourire "Je croyais que tu voulais me faire payer le loyer."
    iris blase "Fais pas le malin, j'ai pas encore décidé combien tu me devais."

    "Elle sourit à peine, puis se tourne vers la porte."
    "Je me rends compte que nous avons passé toute la journée ensemble sans jamais nous éloigner de plus de quelques mètres. Pour la première fois, l'idée de rester dans une chambre fermée me paraît moins pénible que celle de retourner dans le Conclave."

    $ hideGroup()
    jump _28_0_1_1_0_0_LYSA


label _28_0_1_1_0_0_LYSA:
    $ current_period = "Nuit"
    scene bg_chambre_iris at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.5

    "Nous avons éteint l'éclairage principal. Iris est assise sur son lit et regarde sa tablette sans vraiment lire ce qu'elle affiche ; de mon côté, j'essaie de comprendre pourquoi ni Lysa ni Elen ne répondent à nos derniers messages."
    "Un coup discret retentit contre la porte."

    play sound sfx_creak volume 0.25

    "Iris relève immédiatement la tête. Je baisse les yeux vers la commode que nous avons déplacée devant l'entrée, puis vers la grille d'aération."
    "Quelqu'un frappe de nouveau, un peu plus fort."

    lysa inquiet "Iris ? Noam ? Vous êtes là ?"

    "La voix de Lysa me surprend tellement que je fais un pas vers la porte. Iris m'attrape le poignet et secoue vivement la tête."

    $ showGroup([
        ("iris", "peur", 0.37),
        ("noam", "inquiet", 0.64),
    ])

    lysa inquiet "J'ai besoin de vous parler. Je sais qu'il est tard, mais... Vous pouvez m'ouvrir ?"

    "Iris porte un doigt à ses lèvres. Je hoche la tête, même si chaque seconde de silence commence à me paraître insupportable."
    "De l'autre côté, Lysa attend. Je distingue un léger frottement contre la porte, comme si elle s'était appuyée dessus."

    lysa inquiet "Je vous ai cherchés à la cafétéria. Julian m'a dit que vous étiez rentrés, alors je me suis dit que..."

    "Elle ne termine pas sa phrase."
    "Je regarde Iris. Elle fixe la porte sans cligner des yeux."

    lysa fatigue "Bon. Si vous êtes en train de dormir, je suis désolée. Seulement, j'ai vraiment pas envie de rester seule ce soir."

    "Ma main se referme malgré moi autour de mon téléphone. Je pourrais lui envoyer un message, lui demander où se trouve Elen, lui dire de rejoindre Julian."
    "Iris voit mon mouvement et me prend doucement l'appareil des mains avant d'en éteindre l'écran."

    "Lysa frappe une troisième fois."

    lysa inquiet "Noam... Je sais que t'as peur depuis ce qu'on a découvert. Moi aussi. Mais c'est moi, d'accord ?"
    lysa inquiet "S'il vous plaît, dites quelque chose. Même si vous voulez pas m'ouvrir."

    "Je me mords l'intérieur de la joue. Je revois Lysa à la cafétéria quelques jours plus tôt, assise à l'écart avec son habituel air renfrogné."
    "Si c'est bien elle, nous sommes en train de la laisser seule dans un couloir où Ryn circule librement."

    think "Et si elle est venue parce qu'elle a vu quelque chose ?"

    "Iris resserre légèrement sa prise autour de mon poignet. Je sens qu'elle tremble autant que moi."

    lysa fatigue "D'accord... Je vais pas insister. Désolée de vous avoir dérangés."

    "Ses pas commencent à s'éloigner."
    "Je me retiens de l'appeler et j'attends qu'ils disparaissent complètement avant de me tourner vers Iris."

    $ showGroup([
        ("iris", "inquiet", 0.37),
        ("noam", "fatigue", 0.64),
    ])

    noam inquiet "Et si c'était vraiment Lysa ? Elle avait l'air terrorisée."
    iris inquiet "Je sais. Je l'ai entendue. Mais on ne sait pas où elle était cet après-midi, et je refuse de te voir ouvrir cette porte alors qu'on vient à peine de réussir à se mettre à l'abri."
    noam inquiet "On aurait au moins pu lui répondre... Lui dire d'aller trouver Julian."
    iris fatigue "Peut-être. J'en sais rien, Noam. J'ai juste eu peur qu'elle nous demande d'ouvrir, puis qu'il soit trop tard pour revenir en arrière."

    "Je récupère mon téléphone. Le dernier message que j'ai envoyé à Elen n'a toujours pas été lu."
    "Je commence à en rédiger un autre pour Lysa, puis efface tout avant de l'envoyer."

    noam fatigue "Tu crois qu'on pourra rester ici jusqu'au départ ?"
    iris fatigue "Je crois surtout qu'on doit tenir jusqu'à demain matin. Après, on trouvera autre chose."

    "Elle me rend ma tablette et se rallonge sans quitter la porte des yeux."
    "Je m'allonge près d'Iris. Nous parlons à voix basse, sans savoir lequel de nous finira par s'endormir le premier."
    "Pendant longtemps, nous restons éveillés à écouter les bruits du couloir. Aucun pas ne revient devant la porte."

    think "J'espère qu'elle a trouvé quelqu'un."

    "Je voudrais le croire, mais je n'arrive pas à oublier la façon dont Lysa nous a suppliés de répondre."
    "De l'autre côté de la porte, le Conclave paraît parfaitement calme."

    $ hideGroup()
    stop music fadeout 1.2
    call end_day("29", sleeping=True) from _call_j28_stay_end_day_29
    jump _29_0_1_1_0_0_REVEIL
