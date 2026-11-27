# JOUR 9 — Retour de Kami, réunion d'urgence et vote.
default j901_elen_route_seen = False
default j901_nyra_confirmed = False
default j901_julian_delay_success = False
default j901_julian_discours_done = False

label _9_0_1_REVEIL_CHAMBRE:
    scene black
    $ current_day = 9
    $ current_period = "Soir"
    $ cafeteria_food_level = "medium"
    $ noam_has_juliette_drawing = False
    $ j901_elen_route_seen = False
    $ j901_nyra_confirmed = False
    $ j901_julian_delay_success = False
    $ j901_julian_discours_done = False
    stop music fadeout 0.2
    pause 0.65
    scene bg_chambre at adaptive_fullscreen with vpunch
    "Je me redresse d'un coup dans mon lit. J'ai le cœur qui bat à toute vitesse."
    pause 0.65
    "Il fait encore noir. Je passe une main sur ma nuque, elle est trempée."
    think "Qu'est-ce qui m'a réveillé ?"
    "J'attends un peu, sans bouger. Je n'entends plus rien."
    "Je finis par me lever et prends ma tablette. L'heure est affichée, beaucoup trop tôt pour me préparer."
    scene chambre2 at adaptive_fullscreen with dissolve
    "Le voyant de la serrure est allumé. Je vérifie le verrou sans actionner l'ouverture."
    think "Elle est fermée. Rien n'a bougé."
    pause 0.8
    "Je reste devant la porte quelques secondes, la main sur la poignée. Je ne sais même pas ce que j'attends."
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je regarde le bureau. Toujours pas de dessin."
    think "J'ai dû faire un mauvais rêve."
    "Je retourne me coucher. Il me faut un moment avant de réussir à fermer les yeux."
    scene black with fade
    pause 0.85
    $ current_period = "Matin"
    play sound sfx_announce
    $ blink()
    play music "music/bgm_system_override.mp3" fadein 0.7
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bonjour, mes chéris ! Tout le monde au Conclave. Maintenant, s'il vous plaît."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Ne passez pas par la cafétéria. J'ai demandé à Goumi de ne rien servir avant la réunion."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Je n'ai pas toute la matinée. Dépêchez-vous !"
    hide screen kami_broadcast_ui
    scene bg_chambre at adaptive_fullscreen with dissolve
    think "Deux jours sans un mot et elle reprend comme si de rien n'était."
    "Je m'habille à la hâte et vérifie que ma tablette est bien dans ma poche."
    $ hideGroup()
    stop music fadeout 0.8
    $ current_scene_active = "_9_0_1_ROUTE_CONCLAVE"
    $ corridor_current = "dortoir"
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_j901_leave_chambre
    call CORRIDOR_NAVIGATION("dortoir") from _call_offer_exploration_j9_main
    $ current_scene_active = None
    jump _9_0_1_CONCLAVE_ANNONCE

label _9_0_1_CONCLAVE_ANNONCE:
    $ current_scene_active = None
    $ exploration_libre_active = False
    $ exploration_libre_next_label = None
    $ exploration_libre_destination_room = None
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.2
    $ showGroup([("elen", "inquiet", 0.10), ("iris", "fatigue", 0.27), ("nyra", "neutre", 0.43), ("kael", "fatigue", 0.57), ("lysa", "blase", 0.73), ("noam", "inquiet", 0.90)])
    elen "Je vous préviens, je mange dès qu'on sort d'ici. Même si c'est déjà l'heure du déjeuner."
    iris "Tu te rends compte qu'elle vient de disparaître pendant deux jours ? Une maintenance, ça se prépare !"
    lysa "Elle t'a pas envoyé son planning ?"
    iris colere "C'est pas drôle ! Elle a arrêté de répondre et le compteur des sanctions est resté à zéro."
    nyra raison "On lui posera la question quand elle sera là. Kael, tu as vu Tomas en venant ?"
    kael fatigue "Non. Pourquoi ?"
    "Nyra regarde les sièges, puis l'heure sur sa tablette."
    nyra reflexion "Il manque Tomas. C'est vraiment pas dans ses habitudes."
    elen inquiet "Il était peut-être encore en train de dormir ?"
    lysa neutre "Lui ? Il serait capable d'arriver dix minutes en avance à son propre enterrement."
    nyra raison "Je lui ai envoyé un message. Il répond pas."
    stop music fadeout 1.1
    noam inquiet "Quelqu'un est passé devant sa chambre ce matin ?"
    iris reflechit "Non, j'ai rejoint les autres directement."
    kael fatigue "Attends, pourquoi tu demandes ça ?"
    think "Il a juste raté l'annonce. Il ne peut rien lui être arrivé, si ?"
    window hide
    $ cinematic_focus("kael", t=0.35)
    pause 0.75
    $ cinematic_focus("nyra", t=0.40)
    pause 0.80
    $ cinematic_focus("lysa", t=0.40)
    pause 0.65
    $ cinematic_focus("noam", t=0.40)
    pause 0.80
    $ cinematic_reset(t=0.25)
    play sound "audio/sfx_door.mp3"
    with hpunch
    $ hideGroup()
    $ showGroup([("tomas", "gene", 0.25), ("nyra", "reflexion", 0.50), ("noam", "surpris", 0.75)])
    "Tomas déboule dans la salle, complètement rouge, la chemise collée au dos."
    tomas gene "Pardon ! Excusez-moi, vraiment, j'ai couru dès que j'ai vu l'heure et... désolé !"
    noam fatigue "Ah, putain."
    tomas inquiet "J'ai raté quelque chose ? J'étais aux archives, il fallait absolument que je vérifie des données avant de venir."
    nyra raison "Assieds-toi. Tu vas nous expliquer ce que tu as trouvé."
    tomas gene "Oui, pardon. J'aurais dû vous prévenir. Je suis désolé de vous avoir fait attendre."
    noam "C'est bon, Tomas. Respire."
    play music "music/bgm_introspective_atmosphere.mp3" fadein 0.8
    tomas inquiet "Ça concerne Limen. J'ai trouvé des mouvements de population près des frontières, mais il me manque encore des chiffres."
    nyra reflechit "Garde tes données ouvertes. On en parle dès que Kami a fini."
    play sound sfx_announce
    stop music fadeout 0.8
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 1.0
    kami "Ah ! Vous voilà tous. Bien, on commence."
    $ bc_show("iris", "colere", px=-70, py=-50, pz=0.85)
    iris "Deux jours ! Tu nous as laissés deux jours sans la moindre explication ! Qu'est-ce qui s'est passé ?"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Une maintenance, Iris. Je suis de retour, tu peux être contente."
    $ bc_show("noam", "inquiet", px=-70, py=-50, pz=0.85)
    noam "Et les exécutions ? Le compteur est resté à zéro."
    $ bc_hide()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je n'ai pas à te fournir le détail de mes opérations internes, Noam. Nous avons un vote à organiser."
    $ bc_show("kael", "fatigue", px=-70, py=-50, pz=0.85)
    kael "Est-ce qu'on peut au moins te poser des questions sur ce qui s'est passé ici ?"
    $ bc_hide()
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Pas maintenant. Écoutez-moi !"
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Aujourd'hui, troisième vote. Voici votre amendement."
    play sound sfx_tambour
    pause 0.5
    scene bg_diffusion_einstein at adaptive_fullscreen with dissolve
    kami "Autoriser les regroupements de plus de vingt personnes, idéalement avec déclaration préalable."
    $ unlock_dossier_chapter(3)
    $ unlock_dossier_prop("p3_vote_regroupements")
    $ unlock_dossier_arg("p3_declaration")
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je vous rappelle le Commandement IV : les rassemblements non déclarés de plus de vingt individus sont interdits."
    kami "Si vous adoptez l'amendement à l'unanimité, la nouvelle règle s'appliquera immédiatement. Sinon, rien ne change."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Concerts, réunions de famille, manifestations... Je vous imagine déjà en train de réserver des places pour un festival de mauvaises décisions."
    scene bg_conclave at adaptive_fullscreen with dissolve
    hide screen kami_broadcast_ui
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("tomas", "inquiet", 0.10), ("lysa", "blase", 0.27),
        ("ryn", "fatigue", 0.43), ("sael", "inquiet", 0.57),
        ("noam", "inquiet", 0.73), ("kael", "fatigue", 0.90),
    ])
    julian "Enfin ! Une proposition qui permettrait aux gens de se réunir sans avoir à compter jusqu'à dix-neuf !"
    lysa blase "Tu comptes vraiment jusqu'à dix-neuf, toi ?"
    julian "Non, j'ai du personnel pour ça."
    mara "Quel personnel ? Tu ne sais même pas ranger ton plateau."
    "Tomas n'a pas levé les yeux."
    tomas inquiet "Ce n'est pas un hasard."
    noam reflechit "Tu parlais de mouvements de population..."
    tomas reflechit "Oui. Depuis hier soir, plusieurs groupes remontent de Limen vers les points de passage. Ils ont installé des campements."
    ryn colere "Des gens qui cherchent à sortir de là. Enfin."
    sael mefiant "Des gens qui s'approchent des frontières malgré notre refus."
    ryn colere "Tu vas leur demander de faire demi-tour ?!"
    sael determine "Je n'ai rien dit de tel."
    tomas inquiet "Attendez. Les campements rassemblent peut-être des milliers de personnes."
    kael reflechit "Sans déclaration préalable ?"
    tomas neutre "Il n'y a aucune déclaration enregistrée."
    $ unlock_dossier_arg("p3_absence_declaration")
    "Le silence tombe plus vite que je ne l'aurais cru."
    noam inquiet "Le Commandement IV..."
    iris inquiet "Kami n'a pas appliqué les sanctions pendant deux jours."
    tomas inquiet "C'est probablement pour ça qu'ils ont osé se regrouper. Mais si elle vient de reprendre..."
    ryn colere "Non. NON !"
    sael peur "Ils sont au même endroit. En nombre."
    lysa reflechit "Et notre sujet du jour tombe exactement là-dessus."
    noam inquiet "Kami, tu savais pour ces campements ?"
    $ hideGroup()
    play sound sfx_announce
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Oh, vous avez trouvé ! Je commençais à croire que vous aviez perdu la capacité de relier deux informations."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Plusieurs campements limenois dépassent largement le seuil autorisé. Aucun n'a été déclaré."
    kami "J'ai suspendu l'application du Commandement à leur égard jusqu'au résultat du vote. Je voulais vous laisser la possibilité de trancher."
    $ unlock_dossier_arg("p3_suspension")
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "J'aurais pu régler le problème sans vous consulter. Mais ce n'aurait pas été très amusant, vous ne trouvez pas ?"
    $ bc_show("ryn", "colere", px=-70, py=-50, pz=0.85)
    ryn "Tu te fous de nous ?!"
    $ bc_hide()
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh, Ryn. Du calme. J'ai été d'une patience exemplaire."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le vote aura lieu aujourd'hui. Ensuite, le Commandement IV sera appliqué dans sa version alors en vigueur."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Vous avez donc toutes les cartes en main. Essayez de ne pas les manger."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere"), ("sael", "peur"), ("tomas", "inquiet"),
        ("lysa", "triste"), ("noam", "inquiet"), ("nyra", "fatigue"),
        ("mara", "stress"), ("iris", "inquiet"), ("elen", "peur"),
        ("elias", "fatigue"), ("julian", "inquietude"), ("kael", "fatigue"),
    ])
    ryn colere "ELLE LES A LAISSÉS SE RASSEMBLER ! On vote pour, maintenant. On attend quoi ?!"
    elen peur "Oui, on peut voter tout de suite, non ? Kami vient de dire qu'on pouvait les sauver !"
    sael determine "Je voterai pour. Mais il faut savoir ce que le texte autorise."
    ryn "Tu viens de dire que tu voterais pour ! Alors pourquoi tu veux encore discuter ?!"
    lysa blase "Ryn, baisse d'un ton. Pour une fois qu'on est d'accord, votons."
    nyra raison "Attendez. Tomas, montre-moi l'intitulé exact."
    elen inquiet "Mais elle vient de le lire !"
    tomas inquiet "Je l'ai là. Je te l'envoie."
    mara "Et nous, on fait quoi pendant que vous relisez trois lignes ?"
    nyra stress "Laissez-moi une minute. Le mot « idéalement », là. Est-ce que quelqu'un sait ce que ça veut dire pour les rassemblements non déclarés ?"
    ryn colere "ÇA VEUT DIRE QU'ILS PEUVENT SE RASSEMBLER !"
    elias inquiet "Attends, Ryn, elle demande juste..."
    ryn "Non ! Il y a des familles entières qui attendent aux frontières ! Elles se sont regroupées pour s'entraider. Laissez-les au moins faire ça !"
    $ unlock_dossier_arg("p3_familles")
    lysa neutre "On risque de perdre du temps pour un mot, Nyra. Si on attend trop, Kami va décider à notre place."
    nyra raison "Je veux aussi qu'on vote pour. Mais il y a quelque chose qui ne colle pas."
    noam reflexion "Attends, je regarde le texte."
    call refutation_run("j9_nyra_confirmation") from _call_j901_nyra_confirmation
    $ j901_nyra_confirmed = (_return[0] == "success")
    if j901_nyra_confirmed:
        call play_noam_interupt
        noam determine "Nyra a raison. Regardez l'intitulé : il ne dit nulle part ce qui arrive aux campements qui n'ont pas fait de déclaration."
        lysa reflechit "Ah, merde. Elle pourrait nous dire qu'ils sont toujours en infraction."
        nyra raison "Exactement. Ryn, je ne veux pas retarder le vote pour le plaisir. Je veux qu'on les prévienne avant."
    else:
        noam inquiet "Je ne sais pas comment le prouver autrement."
        tomas inquiet "Attendez, je vous montre. Rien ne garantit que les campements déjà formés seront régularisés."
        nyra stress "C'est ce que j'essaie de vous dire depuis tout à l'heure. On ne peut pas leur promettre qu'un vote suffira."
        lysa "D'accord, j'ai compris. Mais il faut faire vite."
    $ unlock_dossier_arg("p3_campements")
    sael mefiant "Je refuse toujours l'ouverture des frontières. Et je refuse que des familles meurent pour s'être réunies. Si certains utilisent les rassemblements pour recruter des gens, on pourra en discuter ensuite."
    $ unlock_dossier_arg("p3_reseaux")
    ryn "Ensuite, oui ! On pourra discuter de tout ce que tu veux ensuite !"
    elen peur "Et les gens qui ne peuvent pas partir ? Les enfants, les personnes âgées ?"
    "Tomas ouvre une carte sur sa tablette. Ryn essaie de regarder par-dessus son épaule et manque de la lui faire tomber."
    tomas inquiet "Attention ! Je n'ai pas toutes les zones, attendez."
    kael reflechit "Passe-moi le fichier. Elias, rapproche-toi, j'ai besoin que tu regardes la connexion."
    elias "Je peux essayer, mais si on passe par le réseau du Canon..."
    iris "Il y a aussi la retransmission du débat ! On peut leur parler, non ?"
    noam reflechit "Oui. On est diffusés sur Terre. Il faut qu'on leur dise de se disperser."
    ryn "En petits groupes, surtout. Qu'ils restent du côté de Limen, qu'ils ne franchissent pas la frontière."
    sael determine "On ne sait pas s'ils nous entendent tous."
    nyra raison "Alors on commence par vérifier le signal. Tomas, aide Kael. Les autres, écartez-vous un peu."
    elen inquiet "Et ceux qui ne pourront pas marcher ?"
    noam inquiet "On va essayer de leur faire parvenir l'alerte aussi. C'est tout ce qu'on peut faire pour l'instant."
    call play_stat_dialogue("d9") from _call_stat_dialogue_d9
    tomas inquiet "Voilà. Les données de la salle du Canon sont dans ce fichier."
    kael neutre "Merci. Noam, regarde ici. Il faut ouvrir le passage vers le réseau."
    elias "Je surveille la connexion. Si elle saute, je te préviens."
    "Kael me montre le circuit sur sa tablette."
    $ hideGroup()
    call j901_play_hack from _call_j901_play_hack_day9
    $ j901_hack_success = bool(_return)
    $ showGroup([("kael", "inquiet", 0.32), ("noam", "inquiet", 0.68)])
    if j901_hack_success:
        kael sourire "On a un retour vidéo. Pas de toutes les zones, mais assez pour lancer une alerte."
    else:
        kael inquiet "La connexion tient à peine. J'ai quelques images et un flux instable."
    noam determine "Alors on n'attend pas. Même si ça coupe, il faut essayer."
    kael neutre "Je lance."
    $ hideGroup()
    stop music fadeout 1.5
    scene black with fade
    jump _9_0_1_CONCLAVE_DEBAT

label _9_0_1_CONCLAVE_DEBAT:
    $ current_period = "Après-midi"
    call trial_intro(subtitle=_("JOUR [current_day]")) from _call_kd_trial_intro_9_0_1
    call j901_play_signal_vivant from _call_j901_play_signal_vivant
    $ j901_signal_result_tier = _return
    jump _9_0_1_CONCLAVE_DEBAT_PARTIE_2


label _9_0_1_CONCLAVE_DEBAT_PARTIE_2:
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_world_decline.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere", 0.10), ("sael", "determine", 0.27),
        ("tomas", "culpabilite", 0.43), ("noam", "inquiet", 0.57),
        ("nyra", "stress", 0.73), ("kael", "inquiet", 0.90),
    ])
    "Le signal commence à se brouiller. Sur l'écran de Kael, des silhouettes se dispersent dans les allées d'un campement, puis l'image se fige."
    tomas inquiet "Je ne vois plus le dernier relais."
    kael reflechit "Le flux est coupé."
    ryn colere "Relance-le !"
    kael neutre "Pas sans savoir pourquoi il s'est interrompu."
    ryn colere "On s'en fiche de pourquoi !"
    sael determine "Non. S'il s'agit de Kami, tu ne feras qu'aggraver les choses."
    ryn colere "Et toi, tu voudrais qu'on attende ?!"
    sael neutre "Je voudrais que tu me laisses finir une phrase."
    "Ryn ouvre la bouche, se ravise, puis frappe le dossier de sa chaise."
    noam reflechit "Certains nous ont entendus. C'est déjà ça."
    nyra reflechit "Oui. Mais on ne sait pas si ceux qui sont encore dans les campements ont compris le message. Il faudra vérifier."
    noam neutre "Je sais."
    "Je regarde les zones encore grises sur la carte. Ce sont des endroits où des gens vivent, et je n'ai même pas le moyen de savoir si l'un d'eux m'a entendu."
    $ hideGroup()
    play sound sfx_gresillement
    stop music fadeout 0.6
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "EH BIEN ! Quelle magnifique émission spéciale ! Vous avez presque réussi à me voler mon propre public !"
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Des ordres criés, des petits humains qui courent, des grands gestes désespérés... Tout ce que j'aime dans une bonne téléréalité."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    if j901_signal_result_tier == "excellent":
        kami "Je dois reconnaître une belle performance : la majorité des campements a reçu votre message. C'est... agaçant."
    elif j901_signal_result_tier == "bon":
        kami "Une partie importante des campements vous a entendus. Vous avez presque de quoi vous féliciter. Presque."
    elif j901_signal_result_tier == "moyen":
        kami "Quelques campements ont reçu votre message. Les autres ont surtout eu droit à une démonstration de votre enthousiasme."
    else:
        kami "Votre transmission ? Un chef-d'œuvre de confusion. J'hésite entre vous donner une mauvaise note et vous demander de recommencer pour le spectacle."
    $ bc_show("ryn", "neutre", px=-70, py=-50, pz=0.85)
    ryn "Alors laisse-nous recommencer !"
    $ bc_hide()
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "NON."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Vous avez utilisé ma retransmission officielle pour détourner le débat. C'est une initiative que j'inscris précieusement dans vos dossiers."
    $ bc_show("iris", "neutre", px=-70, py=-50, pz=0.85)
    iris "Qu'elle nous colle une punition, alors ! Ça changera de ses sermons !"
    $ bc_hide()
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais je ne vous punirai pas aujourd'hui. Voyez comme je suis patiente."
    kami "Vous avez voulu prévenir ces campements. Très bien. Maintenant, vous allez choisir ce qu'il adviendra d'eux."
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "LE DÉBAT EST TERMINÉ."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.2
    $ showGroup([
        ("ryn", "colere"), ("sael", "determine"), ("noam", "reflechit"),
        ("tomas", "culpabilite"), ("lysa", "blase"), ("nyra", "stress"),
        ("kael", "inquiet"), ("elen", "peur"), ("mara", "stress"),
    ])
    elen peur "Déjà ?! Mais il y a encore des gens dans les campements !"
    mara agace "Elle s'en fiche, Elen."
    elen colere "ALORS JE NE M'EN FICHE PAS, MOI !"
    "Mara la regarde. Elle ne trouve pas de plaisanterie à ajouter."
    lysa blase "Bravo. Nous venons de découvrir que notre présidente n'aime pas qu'on lui prenne le micro."
    noam determine "Kami, tu aurais pu couper la diffusion dès le début."
    sael determine "Et elle ne l'a pas fait."
    ryn colere "Tu vas quand même pas la remercier !"
    sael mefiant "Je constate un fait. Ne me prête pas tes propres pensées."
    nyra reflechit "Elle aurait dû nous couper devant tout le monde. Ça ne veut pas dire qu'elle nous laisse faire ce qu'on veut."
    mara doute "Ou alors elle aime juste regarder les gens courir."
    "Je pense à l'enthousiasme de Kami. Les deux explications me paraissent possibles."
    tomas inquiet "Il nous faut encore du temps. Même quelques minutes. Je vois encore des gens près des points de passage."
    julian "Laissez-moi parler."
    iris colere "Julian, pas maintenant !"
    julian "Iris, c'est précisément le moment. Ne me coupe pas, surtout."
    nyra raison "Tu veux la retenir ?"
    julian "C'est l'idée. Tomas, continue de surveiller les données pendant que je parle."
    lysa blase "Je retire tout ce que j'ai dit sur tes discours, pour les cinq prochaines minutes."
    $ hideGroup()
    jump _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS


label _9_0_1_REPRESENTANTS_GAGNENT_DU_TEMPS:
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    $ bc_show("julian", "sourire", px=-70, py=-50, pz=0.85)
    julian "Kami, avant de procéder au scrutin, je voudrais revenir sur un élément de ta déclaration. Tu as employé le terme de regroupement. Je suppose que tu fais une distinction entre un rassemblement organisé et un rassemblement qui s'est constitué spontanément ?"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Julian, tu connais parfaitement le sujet du vote."
    $ bc_show("julian", "determine", px=-70, py=-50, pz=0.85)
    julian "Justement. Prenons un exemple. Vingt personnes attendent un véhicule. Une vingt et unième arrive. À quel moment considère-t-on qu'elles forment un groupe ? Doivent-elles toutes se connaître ? Doivent-elles attendre le même véhicule ? Et si l'une d'elles s'en va pendant que deux autres arrivent ?"
    $ bc_hide()
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Ce n'est pas un cours de droit, Julian."
    $ bc_show("julian", "sourire", px=-70, py=-50, pz=0.85)
    julian "Non, bien sûr. Mais nous votons une règle de droit, et je ne voudrais surtout pas que nos concitoyens aient à compter le nombre de personnes devant eux chaque fois qu'ils attendent quelque part. Ce serait tout de même assez difficile pour quelqu'un qui a le malheur d'être vingt et unième sans le savoir."
    $ bc_hide()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le contexte est pris en compte. Question suivante, si tu en as une de réellement pertinente."
    $ bc_show("julian", "sourire", px=-70, py=-50, pz=0.85)
    julian "J'en ai justement plusieurs. Si la déclaration est préalable, à quoi doit-elle être préalable ? À l'arrivée de la première personne, à la constitution du groupe, ou au début de l'activité elle-même ? Parce que dans le premier cas..."
    $ bc_hide()
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "JULIAN !"
    $ bc_show("julian", "neutre", px=-70, py=-50, pz=0.85)
    julian "Je n'avais pas tout à fait terminé."
    $ bc_hide()
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([("tomas", "reflechit", 0.22), ("nyra", "raison", 0.44), ("noam", "reflexion", 0.65), ("lysa", "neutre", 0.86)])
    tomas "Attendez, je reçois encore des mises à jour. Des gens quittent les points de rassemblement."
    lysa "Continue, Julian. Surtout, continue."
    nyra raison "Elle va le faire taire. Il faut lui donner une raison de répondre."
    $ j901_julian_discours_done = True
    call refutation_run("j9_regroupements") from _call_j901_delay_refutation
    $ j901_julian_delay_success = (_return[0] == "success")
    if j901_julian_delay_success:
        call play_noam_interupt
        noam determine "Tu as suspendu les sanctions jusqu'au résultat. Tant que tu ne l'as pas proclamé, des gens peuvent encore se mettre à l'abri."
        nyra raison "Réponds au moins à la question de Julian sur les déclarations. Tout le monde doit savoir comment tu vas appliquer ce texte."
        "Tomas me montre une zone qui vient de se vider. Quelques groupes ont encore pu s'éloigner."
    else:
        noam inquiet "Je n'arrive pas à lui faire entendre raison."
        nyra reflexion "On a quand même gagné quelques minutes. Tomas, continue de vérifier les déplacements."
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Bon, je vais répondre à cette dernière question. Les campements actuels ont été constitués sous le Commandement en vigueur aujourd'hui. Vous ne votez pas une amnistie pour les infractions antérieures."
    $ bc_show("ryn", "colere", px=-70, py=-50, pz=0.85)
    ryn "TU VAS LES TUER MÊME SI ON VOTE POUR ?!"
    $ bc_hide()
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Tout dépend de leur situation au moment où je reprendrai les sanctions. Vous leur avez transmis un avertissement, n'est-ce pas ?"
    $ bc_show("noam", "inquiet", px=-70, py=-50, pz=0.85)
    noam "Combien de campements sont encore concernés ?"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu sais, Noam, il serait beaucoup plus agréable de ne pas devoir répéter les mêmes choses."
    $ bc_show("julian", "sourire", px=-70, py=-50, pz=0.85)
    julian "Dans ce cas, permets-moi de reformuler la question de mon collègue afin de..."
    $ bc_hide()
    scene bg_diffusion_colere at adaptive_fullscreen with vpunch
    kami "NON ! J'ai compris ce que vous faites !"
    $ bc_show("elen", "peur", px=-70, py=-50, pz=0.85)
    elen "Mais laisse-les partir, s'il te plaît ! Ils sont encore en train de bouger !"
    $ bc_hide()
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Fin des questions. Vote immédiat."
    stop music fadeout 0.5
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    $ showGroup([
        ("ryn", "colere"), ("sael", "determine"), ("noam", "reflechit"),
        ("tomas", "culpabilite"), ("lysa", "blase"), ("elen", "peur"),
        ("nyra", "stress"), ("iris", "blase"), ("kael", "inquiet"),
    ])
    "Les pupitres s'éclairent. POUR. CONTRE. Deux mots, et toutes les nuances qui nous ont occupés depuis ce matin disparaissent."
    elen inquiet "On a gagné un peu de temps, non ?"
    nyra reflechit "Oui. On a fait ce qu'on pouvait pour les prévenir. Je ne vais pas t'inventer un bilan, Elen."
    ryn colere "Alors on vote pour. TOUS."
    iris colere "Arrête de nous donner des ordres !"
    ryn colere "TU VEUX QU'ILS MEURENT ?!"
    iris colere "NON ! Je veux juste qu'on arrête de me hurler dessus comme si c'était moi qui allais tirer !"
    sael determine "Ryn. Ça suffit."
    ryn colere "..."
    sael determine "Je voterai pour."
    "Ryn tourne la tête vers elle. Un instant, je retrouve le souvenir de leur dispute au vote précédent."
    sael neutre "Je n'ai pas changé d'avis sur les frontières. Mais ces gens ne méritent pas la mort pour s'être rassemblés."
    lysa blase "Voilà une phrase qu'on aurait aimé entendre dans une autre circonstance."
    tomas inquiet "Même un vote unanime ne garantit pas que les camps seront régularisés. Il faut le savoir."
    noam determine "Je le sais."
    "Je croise le regard de Kael. Il ne me regarde pas longtemps, puis baisse les yeux vers son pupitre."
    think "Il cherche toujours la photo de Léa. Moi, le dessin de Juliette. Dans quelques minutes, ces objets auront l'air dérisoires, et je les chercherai quand même."
    play sound sfx_beep
    $ hideGroup()
    show screen kami_broadcast_ui
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Pensez à vos électeurs ! Enfin, ceux qui auront encore la possibilité de vous remercier."
    hide screen kami_broadcast_ui
    jump _9_0_1_VOTE

label _9_0_1_VOTE:
    $ renpy.block_rollback()
    $ vote_phase3_time_left = 10
    $ vote_phase3_hover_side = None
    $ vote_phase3_player_choice = None

    stop music fadeout 1.0
    scene black with dissolve

    $ _vote_result = renpy.call_screen("vote_screen")
    $ j901_player_vote = _vote_result if _vote_result in ("pour", "contre") else "contre"
    $ j901_vote_adopte = (j901_player_vote == "pour")

    if j901_player_vote == "pour":
        scene expression Solid("#0AFF8844")
        with Dissolve(0.12)
    elif j901_player_vote == "contre":
        scene expression Solid("#FF2A2A44")
        with Dissolve(0.12)
    else:
        scene expression Solid("#FF2A2A44")
        with Dissolve(0.12)

    pause 0.4

    scene bg_conclave at adaptive_fullscreen with dissolve
    play music "music/bgm_fatal_assembly.mp3" fadein 1.0
    $ showGroup([("noam", "inquiet", 0.50)])

    "Les pupitres enregistrent les choix puis s'éteignent les uns après les autres. Aucun nom, aucune main levée, seulement douze bulletins anonymes."

    think "Personne ne sait ce que les autres viennent de faire. Dans quelques secondes, un seul vote peut condamner tous les campements."

    $ hideGroup()
    $ vote_phase3_counts = {"pour": 0, "abstention": 0, "contre": 0}
    $ vote_phase3_current_name = ""
    $ vote_phase3_current_vote = None

    if j901_vote_adopte:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "pour"),
        ]
    else:
        $ vote_phase3_results = [
            ("Bulletin 01", "pour"),
            ("Bulletin 02", "pour"),
            ("Bulletin 03", "pour"),
            ("Bulletin 04", "pour"),
            ("Bulletin 05", "pour"),
            ("Bulletin 06", "pour"),
            ("Bulletin 07", "pour"),
            ("Bulletin 08", "pour"),
            ("Bulletin 09", "pour"),
            ("Bulletin 10", "pour"),
            ("Bulletin 11", "pour"),
            ("Bulletin 12", "contre"),
        ]

    $ renpy.random.shuffle(vote_phase3_results)
    $ vote_phase3_pending_votes = list(vote_phase3_results)
    $ vote_phase3_tally_index = 0
    $ vote_phase3_tally_done = False

    $ renpy.call_screen("vote_phase3_tally_screen")

    pause 0.8

    $ j901_vote_adopte = (vote_phase3_counts["contre"] == 0)

    if j901_vote_adopte:
        jump _9_0_1_FIN_JOURNEE_VOTE_ADOPTE
    else:
        jump _9_0_1_FIN_JOURNEE_VOTE_REFUSE

# Séquence de tirs distincts, pas un unique son décrit plusieurs fois.
# Le volume reste dans l'intervalle habituel du mixage Ren'Py.
label j901_canon_volley(shots):
    stop music fadeout 0.25
    window hide
    while shots > 0:
        play sound sfx_laser_canon volume 1.0
        with vpunch
        pause 0.85
        $ shots -= 1
    return

label _9_0_1_FIN_JOURNEE_VOTE_ADOPTE:
    $ hideGroup()
    $ current_period = "Soir"
    stop music fadeout 0.8
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_cold_metadata.mp3" fadein 1.2
    kami "Douze bulletins. Aucun vote défavorable. Unanimité !"
    $ interject("ADOPTÉ", color="#5DFF9A")
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "BRA-VO ! Vous avez enfin réussi à être d'accord sur quelque chose ! Je savais que la peur était un excellent outil pédagogique."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Le Commandement IV est modifié. Les regroupements de plus de vingt personnes sont désormais autorisés, idéalement sous déclaration préalable."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    if j901_signal_result_tier == "excellent":
        kami "Votre avertissement a atteint la majorité des campements. Beaucoup ont pu se disperser ou transmettre une déclaration d'urgence. Les pertes prévues ont fortement diminué."
    elif j901_signal_result_tier == "bon":
        kami "Plusieurs campements ont suivi vos instructions. D'autres sont restés exposés. Une réussite incomplète, comme vous les aimez."
    elif j901_signal_result_tier == "moyen":
        kami "Votre signal n'a atteint qu'une partie des campements. Certains groupes ont pu s'éloigner, mais beaucoup demeurent concernés par les sanctions applicables."
    else:
        kami "Votre transmission a surtout semé la confusion. Certains campements ont pu se disperser, d'autres non. Je vais maintenant reprendre les sanctions."
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "Je rappelle que vous n'avez pas voté d'amnistie pour les rassemblements constitués avant l'entrée en vigueur du texte."
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Mais ne faites pas cette tête ! Après tout, vous avez gagné votre vote."
    $ bc_show("noam", "neutre", px=-70, py=-50, pz=0.85)
    noam "Combien de personnes ?"
    $ bc_hide()
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Tu sais, Noam, tu as vraiment le chic pour gâcher les beaux moments."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "Et une dernière chose : je ne disparaîtrai JAMAIS."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    $ showGroup([
        ("ryn", "fatigue"), ("sael", "neutre"), ("noam", "inquiet"),
        ("tomas", "inquiet"), ("lysa", "triste"), ("elen", "peur"),
        ("kael", "fatigue"),
    ])
    elen hesitation "On l'a fait..."
    play sound sfx_gresillement
    "Un grondement monte sous nos pieds. Elen se tourne vers les écrans."
    $ _j901_shots = {"excellent": 2, "bon": 3, "moyen": 4, "echec": 5}.get(j901_signal_result_tier, 4)
    if j901_julian_delay_success:
        $ _j901_shots = max(2, _j901_shots - 1)
    call j901_canon_volley(_j901_shots) from _call_j901_canon_adopted
    elen peur "Mais... On a voté pour !"
    tomas inquiet "Ceux qui n'ont pas réussi à se mettre en règle avant le résultat..."
    lysa triste "On avait raison de se méfier du texte."
    julian "J'espère au moins que mon intervention leur a donné assez de temps."
    "Personne ne lui répond."
    ryn fatigue "Combien sont encore là-bas ?"
    tomas inquiet "Je vais essayer d'avoir les chiffres."
    sael neutre "Ceux qui ont survécu n'ont plus à se cacher pour rester ensemble."
    ryn reflechit "Ce n'est pas la même chose que pouvoir rentrer chez soi."
    sael triste "Non."
    "Ils ne se disputent pas. Je ne sais pas ce qui m'inquiète le plus : leur silence, ou le fait qu'il ait fallu tout ça pour qu'il existe."
    noam neutre "On a empêché le pire pour une partie d'entre eux."
    lysa neutre "Et on ne sait pas encore pour les autres."
    "Elen ouvre la bouche, comme si elle voulait nous féliciter. Elle y renonce."
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_dortoir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_319
    scene couloir_dortoir at adaptive_fullscreen with fade
    play music "music/bgm_calm_not_peace.mp3" fadein 2.0
    "Dans le couloir, Julian marche à côté de moi."
    julian "Je pensais que réussir un vote ferait plus de bruit."
    noam neutre "Moi aussi."
    julian "C'est une victoire, tout de même."
    noam reflechit "Oui. Je suppose."
    if j901_julian_discours_done:
        julian "Tu crois que j'ai gagné combien de minutes ?"
        noam "Je sais pas. Mais Tomas voyait encore des gens quitter les campements pendant que tu parlais."
        julian "Il faudra que je lui demande le chiffre. Je compte bien le retenir."
    else:
        julian "J'aurais aimé qu'on ait un peu plus de temps."
    "Je souris malgré moi. Au bout du couloir, il me laisse devant ma porte."
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_320
    scene bg_chambre at adaptive_fullscreen with dissolve
    "Je regarde la place vide sur le bureau. Le dessin de Juliette n'est pas revenu."
    think "Douze votes pour. Et je ne sais toujours pas combien de personnes nous avons sauvées."
    "Je ferme la porte et vérifie que le verrou s'est enclenché."
    think "Ce soir, je n'ai pas envie de croire que la peur doit gagner à chaque fois."
    $ hideGroup()
    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_26
    # La suite du vote adopté n'est pas encore écrite : convergence provisoire.
    call screen kd_route_vote_convergence
    $ j901_vote_adopte = False
    call end_day("10") from _call_end_day_13
    jump _10_0_1_1_REVEIL_CHAMBRE


label _9_0_1_FIN_JOURNEE_VOTE_REFUSE:
    $ current_period = "Soir"
    $ hideGroup()
    stop music fadeout 0.6
    play sound sfx_announce
    show screen kami_broadcast_ui
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 0.8
    kami "Dépouillement terminé."
    pause 0.6
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Oh..."
    scene bg_diffusion_taquin at adaptive_fullscreen with dissolve
    kami "Quel dommage. Il semblerait que vous ne soyez pas capables de vous mettre d'accord."
    scene bg_diffusion_colere at adaptive_fullscreen with dissolve
    kami "L'unanimité n'est PAS atteinte."
    $ interject("REJETÉ", color="#FF4D6D")
    scene bg_diffusion_professeur at adaptive_fullscreen with dissolve
    kami "L'amendement est rejeté. Le Commandement IV demeure en vigueur, sans modification."
    $ bc_show("noam", "neutre", px=-70, py=-50, pz=0.85)
    noam "Kami, attends ! Les campements, ils..."
    $ bc_hide()
    scene bg_diffusion_zen at adaptive_fullscreen with dissolve
    kami "Les campements ? Oui. J'avais promis de reprendre l'application du Commandement après le vote."
    scene bg_diffusion_amour at adaptive_fullscreen with dissolve
    kami "Je tiens toujours mes promesses, moi."
    hide screen kami_broadcast_ui
    scene bg_conclave at adaptive_fullscreen with dissolve
    "Une chaise recule. Quelqu'un dit quelque chose, mais je n'entends pas les mots."
    play sound sfx_gresillement
    scene bg_conclave at adaptive_fullscreen
    $ showGroup([
        ("ryn", "colere2", 0.25), ("noam", "surpris", 0.50), ("sael", "peur", 0.75),
    ])
    ryn colere2 "QUI ?!"
    "Un nouveau grondement monte depuis les profondeurs de la station."
    ryn colere "QUI A VOTÉ CONTRE ?!"
    sael peur "Ryn..."
    ryn colere2 "ILS ÉTAIENT LÀ ! ILS NOUS ÉCOUTAIENT !"
    noam inquiet "Ryn, on ne sait pas..."
    ryn colere "NE ME DIS PAS DE ME CALMER !"
    "Il fait un pas vers les autres sièges. Sael lui barre la route."
    sael determine "Ça ne changera rien."
    ryn colere "ÉCARTE-TOI !"
    sael determine "Non."
    "Je voudrais croire que quelqu'un va trouver une nouvelle procédure, une phrase oubliée dans le règlement, n'importe quoi qui empêcherait le canon de tirer."
    "Il n'y a que le grondement."
    call j901_canon_volley(2) from _call_j901_canon_refused_first
    "Je me rattrape au bord de la table. Elen crie derrière moi."
    $ _j901_shots = {"excellent": 2, "bon": 3, "moyen": 4, "echec": 5}.get(j901_signal_result_tier, 4)
    if j901_julian_delay_success:
        $ _j901_shots = max(2, _j901_shots - 1)
    call j901_canon_volley(_j901_shots) from _call_j901_canon_refused_rest
    think "Sur Terre, ils devaient encore courir. Certains ont dû entendre notre avertissement. D'autres..."
    "Julian ne dit plus rien. Tomas garde les yeux rivés sur sa tablette."
    think "Un seul vote suffisait."
    $ hideGroup()
    scene black with Fade(0.1, 0.2, 0.8)
    "Je ne sais plus qui a quitté la salle le premier. Je me souviens seulement d'avoir attendu que les tirs s'arrêtent, et d'avoir compris qu'ils ne s'arrêteraient pas parce que nous le demandions."
    "La prochaine chose dont je me souviens clairement, c'est mon réveil du lendemain."
    call show_chapter_title("Fin du chapitre 3", "Chapitre 3 — La confiance ne suffit pas") from _call_show_chapter_title_27
    call end_day("10") from _call_end_day_14
    jump _10_0_1_1_REVEIL_CHAMBRE

