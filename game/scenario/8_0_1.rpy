# --------------------------------------------------------------------------------------------
# JOUR 8 — Réveil chambre
# Noam se réveille seul, calme. Cherche le dessin de Juliette. Ne le trouve pas.
# Scène PnC : fouille de la chambre. Le dessin est introuvable.
# Résolution : il décide d'aller manger.
# --------------------------------------------------------------------------------------------

label _8_0_1_REVEIL_CHAMBRE:
    scene black
    $ current_day = 8
    $ noam_has_juliette_drawing = False
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5
    $ blink()
    pause 1.0
    $ blink()
    scene bg_cg012 at adaptive_fullscreen with dissolve

    "Une ligne de lumière traverse le sol sous le rideau. Je reste allongé quelques secondes, surpris de m'être réveillé sans annonce ni voix dans les murs."

    think "Deux jours sans Kami. Je devrais peut-être arrêter de compter, mais le silence est encore trop inhabituel pour devenir normal."

    $ blink()
    think "Pour une fois, personne ne me force à sortir du lit. Je peux rester là uniquement parce que j'en ai envie."

    "Je m'étire, puis mon regard se pose sur la table près du lit. L'espace vide me rappelle immédiatement ce que je voulais vérifier."

    think "Le dessin de Juliette. Je l'avais encore hier soir, j'en suis certain."

    scene bg_chambre at adaptive_fullscreen with dissolve

    "Je me redresse et cherche autour de moi. Rien sur la table, rien sur le lit, rien au sol."

    think "Elle avait passé trois semaines dessus en recommençant chaque fois qu'un détail lui déplaisait. À la fin, elle trouvait toujours que mon nez était raté."
    think "Je lui avais répondu que le dessin était parfait. Elle croyait que je voulais seulement lui faire plaisir, mais je le pensais vraiment."

    "Je me lève et inspecte une nouvelle fois les abords du lit. Le dessin n'a pas pu disparaître. Je l'ai forcément rangé quelque part sans m'en souvenir."

    tuto "(Fouille la chambre. Le dessin est peut-être encore là.)"
    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_291
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ pnc_room = "chambre_j8"
    $ pnc_flags = {}
    call screen pnc_chambre_j8()
    return

# -------------------------------------------------------
# SCREEN PnC — Chambre jour 8
# -------------------------------------------------------

screen pnc_chambre_j8():

    modal True
    zorder 200

    use room_scene_background("chambre")

    $ j8_exit_label = "_8_FIN_RECHERCHE" if pnc_flags.get("sac") and pnc_flags.get("placard") and pnc_flags.get("sous_lit") else "_8_PNC_ECRAN"
    use room_scene_interactions("chambre", {
        "chambre1_aeration": "_8_PNC_CHAISE",
        "chambre1_lit": "_8_PNC_SOUS_LIT",
        "chambre1_television": "_8_PNC_ECRAN",
        "chambre1_tiroir": "_8_PNC_SAC",
        "chambre2_armoire": "_8_PNC_PLACARD",
        "chambre2_porte_dehors": j8_exit_label,
        "chambre2_porte_sdb": "_8_PNC_CHAISE",
        "chambre3_brouilleur": "_8_PNC_ECRAN",
        "chambre3_tablette": "_8_PNC_ECRAN",
    })

# -------------------------------------------------------
# LABELS PnC
# -------------------------------------------------------

label _8_PNC_SAC:
    $ pnc_flags["sac"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je vide le sac sur le lit. Des vêtements froissés et plusieurs papiers tombent en tas devant moi."
    "J'attrape aussitôt une feuille qui dépasse, mais ce n'est qu'un formulaire du Conclave couvert de numéros et de cases à cocher."
    think "Je savais que le dessin était précieux. Je ne l'aurais jamais glissé au milieu de tout ça."
    $ hideGroup()
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_CHAISE:
    $ pnc_flags["chaise"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je fouille chaque poche de la veste suspendue à la chaise, puis je la retourne avant de vérifier sous le siège."
    think "Toujours rien. Pourtant, je me souviens parfaitement du papier entre mes doigts hier soir. Je ne l'ai pas imaginé."
    $ hideGroup()
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_PLACARD:
    $ pnc_flags["placard"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "J'ouvre le placard. Trois cintres pendent au-dessus d'un pull roulé en boule sur l'étagère."

    menu:
        "Déplier le pull.":
            "Je déplie le pull et le secoue au-dessus du sol. Rien ne tombe."
            think "Évidemment. Je le replie à moitié avant de le remettre à sa place."

        "Regarder derrière les cintres.":
            "Je pousse les cintres sur le côté. Le fond du placard est parfaitement vide."
            think "Au moins, aucune feuille ne peut se cacher là-dedans."

    $ hideGroup()
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_SOUS_LIT:
    $ pnc_flags["sous_lit"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je m'agenouille et soulève le bord de la couette. Sous le lit, je ne trouve qu'un peu de poussière et une chaussette oubliée."

    menu:
        "Me relever tout de suite.":
            think "Il est ailleurs. Je continue."

        "Rester là, par terre, un moment.":
            think "Je reste un instant à genoux sur le sol d'une chambre qui n'est même pas la mienne, incapable d'accepter qu'un simple morceau de papier me mette dans cet état."
            think "Ça suffit. Relève-toi et continue."

    $ hideGroup()
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

label _8_PNC_ECRAN:
    $ pnc_flags["ecran"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je m'arrête devant l'écran mural. Il reste entièrement noir, sans même une lumière de veille."
    think "Kami ne s'est manifestée ni cette nuit ni ce matin. C'est rassurant, en théorie."
    think "Pourtant, un écran éteint dans cette chambre ressemble toujours à quelque chose qui attend le bon moment pour se rallumer."
    "Je détourne les yeux et reprends ma recherche."
    $ hideGroup()
    $ pnc_room = "chambre_j8"
    call screen pnc_chambre_j8()
    return

# -------------------------------------------------------
# FIN DE RECHERCHE
# -------------------------------------------------------

label _8_FIN_RECHERCHE:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_292
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])

    "Je m'assieds au milieu du désordre créé par ma recherche. Le sac est ouvert sur le lit, le tiroir dépasse et le pull pend à moitié hors du placard."

    think "Le dessin n'est pas là. Je ne perds pas ce genre de chose et je sais que je l'avais encore hier."
    think "J'ai envie de me convaincre que je l'ai rangé ailleurs, mais il n'existe pas beaucoup d'« ailleurs » dans cette chambre."

    "Je me relève malgré l'impression d'abandonner quelque chose d'important."

    menu:
        "Refaire un tour rapide de la pièce.":
            "Je vérifie derrière la porte, sous le matelas, puis jusque dans la doublure du sac."
            think "Rien. Il n'est vraiment plus dans la pièce."

        "Accepter que ce soit fini pour l'instant.":
            think "Je ne peux pas fouiller indéfiniment. Il se trouve peut-être dans une autre affaire, quelque part où je n'ai pas encore regardé."

    "Mon estomac se rappelle brusquement à moi. Je n'ai rien mangé depuis hier soir et continuer à retourner la chambre ne fera pas réapparaître le dessin."

    think "Je vais déjeuner, puis je reprendrai calmement. Les objets ne disparaissent pas sans raison."

    $ journal_entries.append(("Jour 8 — matin", "Le dessin de Juliette a disparu. J'ai fouillé partout. Il n'est plus là. Je ne sais pas si je l'ai égaré ou si quelqu'un l'a pris. Je préfère penser que je l'ai égaré. C'est moins lourd à porter."))

    "Je récupère ma veste sur la chaise."

    menu:
        "Laisser la chambre telle quelle.":
            think "Je rangerai en rentrant. Pour le moment, je n'ai plus envie de regarder cette pièce."

        "Refermer le sac et le placard avant de sortir.":
            "Je referme soigneusement le placard et la fermeture du sac."
            think "Je ne sais pas pourquoi j'en ressens le besoin. Peut-être simplement pour être certain de voir si quelque chose bouge encore."

    $ hideGroup()
    "Je quitte la chambre en refermant la porte derrière moi."
    stop music fadeout 1.0
    jump _8_0_1_CAFETERIA

label _8_0_1_CAFETERIA:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_293
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_unsaid_distance.mp3" fadein 1.5

    $ showGroup([
        ("iris",   "sourire",      0.05),
        ("julian", "decontracte",  0.20),
        ("lysa",   "neutre",       0.35),
        ("noam",   "fatigue",      0.50),
        ("elias",  "detendu",      0.65),
        ("mara",   "rire",         0.80),
        ("tomas",  "fatigue",      0.95)
    ])

    "La cafétéria est plus bruyante que d'habitude. Les conversations se croisent, les rires viennent sans effort et personne ne surveille les écrans entre deux phrases."

    think "Deux jours sans Kami, et l'endroit ressemble déjà moins à une salle d'attente avant exécution."

    iris sourire "Je commence à croire qu'on est officiellement en vacances. Encore une journée sans annonce et je réclame une grasse matinée collective."

    julian decontracte "Julian approuve. Si l'apocalypse devient silencieuse et nous laisse dormir jusqu'à midi, il est prêt à revoir son jugement sur elle."

    mara rire "Tu parles surtout de dormir. Même la fin du monde doit s'adapter à ton confort."

    julian sourire "Le confort est une valeur fondamentale de l'humanité. Enfin une cause politique sur laquelle Julian peut s'engager sincèrement."

    elias detendu "Ça explique beaucoup de choses sur toi, et aucune n'est rassurante."

    julian sourire "Merci, Elias. Ça fait du bien de se sentir enfin compris."

    "Je m'installe avec mon plateau à côté de Lysa. Elle m'observe à peine une seconde avant de reprendre son repas."

    lysa neutre "Tu as une sale tête. Je suppose que le silence de Kami n'améliore pas miraculeusement ton sommeil."

    noam fatigue "Merci pour ce diagnostic très rassurant. J'ai simplement passé une partie de la matinée à chercher quelque chose."

    lysa taquin "Et visiblement, tu as perdu contre l'objet."

    think "Je pourrais lui parler du dessin. Pourtant, au milieu de cette ambiance presque normale, je n'ai aucune envie de ramener la conversation dans ma chambre."

    "Tomas reste penché sur son écran portable. Son doigt remonte lentement une colonne de chiffres pendant que les autres parlent."

    iris taquin "Attention, Tomas a cette tête-là. Dans quelques secondes, il va nous annoncer une catastrophe avec un tableau parfaitement aligné."

    tomas gene "Ce n'est pas une catastrophe. J'ai seulement consulté les statistiques publiques cette nuit."

    mara neutre "Pourquoi est-ce que tu consultes des statistiques pendant ton temps libre ?"

    tomas gene "Je trouve ça reposant. Les données sont organisées et, en général, elles ne changent pas de sujet au milieu d'une phrase."

    iris rire "Je retire ce que j'ai dit. C'est lui, la catastrophe."

    tomas reflechit "Depuis le vote du sixième jour, je n'ai trouvé aucune nouvelle exécution enregistrée."

    "Autour de la table, les sourires s'effacent sans que personne ait besoin de réclamer le silence."

    noam surpris "Aucune exécution ? Dans quel district ?"

    tomas inquiet "Dans tous les districts. Le compteur mondial est resté à zéro pendant deux journées complètes."

    elias surpris "Attends... Tu veux dire vraiment zéro ? Pas juste un retard dans la mise à jour ?"

    tomas reflechit "J'ai comparé plusieurs sources. Une erreur reste possible, mais elle devrait alors affecter simultanément tous les systèmes publics."

    mara surpris "Ça peut arriver, deux jours sans que personne ne soit condamné ?"

    tomas inquiet "Techniquement, oui. Statistiquement, compte tenu des chiffres précédents, c'est extrêmement improbable."

    julian decontracte "Donc, si Julian résume correctement : Elias renverse une tasse de café, Kami disparaît et plus personne n'est exécuté dans le monde."

    julian sourire "Nous avons devant nous le héros de l'humanité. Une arme redoutable, pourvu qu'on lui fournisse de la vaisselle."

    elias detendu "J'ai rien fait. J'ai même pas fait exprès de renverser ce café."

    iris sourire "C'est encore mieux. Tu as sauvé le monde par maladresse. Ça te ressemble davantage."

    mara rire "C'est complètement ridicule présenté comme ça, mais je préfère cette version à toutes les autres."

    elias fatigue "Vous êtes vraiment cons... Mais c'est moins lourd quand vous êtes cons comme ça."

    "Il sourit malgré lui. Je ne me rappelle plus la dernière fois où je l'ai vu se détendre assez longtemps pour oublier de se méfier."

    menu:
        "Rentrer dans la blague.":
            noam taquin "Franchement, Elias, je suis impressionné. Statistiquement, très peu de gens peuvent prétendre avoir neutralisé Kami avec un café."

            julian sourire "Enfin quelqu'un de lucide. Julian commençait à désespérer de ce groupe."

            elias rire "Je vous déteste tous, sans exception."

        "Rester prudent.":
            noam inquiet "Ou alors quelque chose dysfonctionne réellement. Et si l'absence d'exécutions est liée à la panne, rien ne garantit que ça durera."

            mara fatigue "Oui... Il y a aussi cette possibilité. J'aimais mieux la version du café héroïque."

            tomas inquiet "C'est pourtant celle que je considère comme la plus probable."

    iris taquin "En attendant de savoir, je compte bien profiter du calme."

    lysa blase "Parce que tu as peur que Kami revienne demain ?"

    iris fatigue "J'ai peur qu'elle revienne dans cinq minutes et qu'elle nous fasse payer chaque seconde de répit."

    "Un silence bref traverse la table. Il ne dure pas assez longtemps pour briser l'ambiance, seulement pour rappeler que personne n'a réellement oublié où nous sommes."

    julian sourire "Alors profitons-en tant que c'est encore possible. Julian refuse de laisser une menace hypothétique gâcher un déjeuner bien réel."

    elias detendu "Pour une fois, je suis d'accord avec lui."

    mara rire "Quelqu'un devrait noter la date. Ça risque de ne jamais se reproduire."

    "Les discussions reprennent autour de sujets sans importance : la nourriture, le sommeil et les souvenirs du monde d'avant. Pendant quelques minutes, nous ressemblons presque à des gens ordinaires."

    think "Presque. Le dessin n'était pas dans ma chambre et, même entouré par leurs voix, je n'arrive pas à l'oublier complètement."

    $ hideGroup()
    jump _8_0_1_TEMPS_LIBRE_1

label _8_0_1_TEMPS_LIBRE_1:

    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "bg_couloir") from _call_MAYBE_PLAY_SCRIPTED_DOOR_294
    scene bg_couloir at adaptive_fullscreen with dissolve

    call START_FREE_TIME("_8_0_1_APRES_MIDI_KAEL_CRISE") from _call_START_FREE_TIME_8_0_1

# --------------------------------------------------------------------------------------------
# JOUR 8 — Après-midi
# Kael débarque en crise dans l'espace commun.
# Découverte collective : la photo de Léa a disparu.
# Lancement du mini-jeu STABILISATION.
# Suivi : Noam décide de trouver le coupable.
# --------------------------------------------------------------------------------------------

# ============================================================
# LABEL — AMORCE DE LA CRISE
# ============================================================

label _8_0_1_APRES_MIDI_KAEL_CRISE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_295
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5

    $ showGroup([
        ("lysa",   "neutre",      0.15),
        ("ryn",    "decontracte", 0.35),
        ("elias",  "fatigue",     0.65),
        ("noam",   "neutre",      0.85),
    ])

    "L'après-midi s'écoule dans un calme presque suspect. Je retrouve Lysa, Ryn et Elias à la cafétéria, mais personne ne semble réellement concentré sur ce qu'il fait."

    lysa neutre "Tu as vu Kael depuis ce matin ? Il est parti juste après le déjeuner et il avait l'air... différent."

    noam hesitation "Non. Qu'est-ce que tu veux dire par « différent » ?"

    ryn desaccord "Il tournait en rond dans les couloirs. Je l'ai croisé deux fois et, la seconde, il ne m'a même pas remarqué."

    elias fatigue "J'ai essayé de lui parler près des chambres. Il a marmonné quelque chose avant de repartir dans l'autre sens."

    "Je repose mon verre. Kael n'est pas du genre à ignorer quelqu'un sans même s'en rendre compte."

    menu:
        "Aller voir s'il va bien.":
            $ noam_nature_j8 = "proactif"
            noam inquiet "Quelque chose cloche. Je vais le chercher avant qu'il continue à tourner seul dans les couloirs."
            lysa sourire "Bien. Pour une fois, tu te lèves avant que quelqu'un soit obligé de te pousser."

        "Attendre, il est peut-être juste fatigué.":
            $ noam_nature_j8 = "reserve"
            noam hesitation "On a tous besoin de rester seuls parfois. Il sait où nous trouver s'il veut parler... Enfin, je suppose."
            ryn hesitation "Peut-être, mais je n'aimais vraiment pas sa tête."

    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_296
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play sound "sfx/door_slam.mp3" volume 1.2
    with hpunch

    $ showGroup([
        ("lysa",   "choc",    0.12),
        ("ryn",    "inquiet", 0.28),
        ("kael",   "colere",  0.50),
        ("elias",  "choc",    0.72),
        ("noam",   "inquiet", 0.88),
    ])

    "La porte claque contre le mur. Kael entre d'un pas brutal, s'arrête au milieu de la pièce et nous dévisage comme s'il cherchait un visage précis parmi nous."

    kael colere "C'est qui ?"

    elias choc "Kael... Qu'est-ce qui se passe ?"

    kael colere "Qui est entré dans ma chambre ? Quelqu'un y est allé et a pris quelque chose."

    ryn inquiet "Attends, comment tu peux être sûr que quelqu'un est entré ?"

    kael colere "Parce que je cherche depuis ce matin ! Elle était sous mon oreiller et elle n'est plus nulle part."

    think "Sous son oreiller. Il ne l'avait pas simplement posée quelque part : il l'avait cachée."

    lysa choc "Qu'est-ce qui a disparu ?"

    kael inquiet "La photo de ma sœur. Celle de Léa."

    "Personne ne répond. Lysa ferme brièvement les yeux, Elias recule d'un demi-pas et Ryn baisse le regard."

    think "Quelqu'un est entré dans sa chambre, a fouillé assez précisément pour regarder sous son oreiller et a emporté la seule chose qui comptait vraiment."

    "Les mains de Kael tremblent. Sa colère est réelle, mais elle tient à peine au-dessus de quelque chose de beaucoup plus fragile."

    kael colere "Alors je vous le demande une dernière fois : qui a pris la photo ?"

    stop music fadeout 1.0
    play music "music/bgm_stabilisation_tension.mp3" fadein 0.8
    with vpunch
    call j801_play_stabilisation from _call_j801_play_stabilisation
    $ j801_stabilisation_result = _return
    jump _8_0_1_APRES_STABILISATION

# ============================================================
# LABEL — APRÈS LA STABILISATION
# ============================================================

label _8_0_1_APRES_STABILISATION:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_297
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5
    $ showGroup([
        ("lysa",  "triste",   0.12),
        ("ryn",   "inquiet",  0.28),
        ("kael",  "effondre", 0.50),
        ("elias", "choc",     0.72),
        ("noam",  "neutre",   0.88),
    ])

    "Le calme revient progressivement. Kael reste assis, les coudes sur les genoux, encore essoufflé mais enfin capable de nous entendre."

    "Lysa approche une chaise et pose une main sur l'accoudoir, près de lui, sans essayer de le toucher."

    ryn hesitation "On devrait vérifier les autres chambres. Si quelqu'un est entré chez toi, il a peut-être fouillé ailleurs."

    kael effondre "Ça ne ramènera pas la photo. Elle n'est plus là, c'est tout."

    elias choc "Qui pourrait faire un truc pareil ? Il fallait savoir ce que tu cachais et exactement où chercher."

    think "C'est la question que personne ne veut vraiment poser. Celui qui a pris la photo sait ce que Kael conserve lorsqu'il se croit seul."

    "Je regarde les quatre personnes autour de moi. Nous avons mangé, voté et vécu ensemble pendant plus d'une semaine. Pourtant, les chambres sont verrouillées et les couloirs surveillés."

    think "L'un d'entre eux aurait pu le faire. Ou quelqu'un d'autre circule ici sans que nous le voyions."
    think "Kami se tait depuis deux jours, mais ça ne signifie pas que le Conclave a cessé de nous observer."

    noam inquiet "Il faut que je vous dise quelque chose. Moi aussi, j'ai perdu un objet ce matin."

    "Tous les regards se tournent vers moi. Kael relève lentement la tête."

    noam inquiet "C'est un dessin que Juliette, ma petite sœur, m'avait fait. Je l'avais encore hier soir."
    noam inquiet "J'ai fouillé toute ma chambre au réveil, mais il a disparu."

    lysa choc "Toi aussi ? Pourquoi tu ne nous en as pas parlé ce matin ?"

    noam hesitation "Je pensais l'avoir mal rangé. Je préférais croire ça plutôt que d'imaginer quelqu'un entrer dans ma chambre."

    elias inquiet "Donc Kael ne s'est pas trompé, et toi non plus. Quelqu'un a fouillé au moins deux chambres pendant la même nuit."

    kael effondre "Je vous l'avais dit. Personne ne voulait seulement me croire."

    noam inquiet "Je te crois maintenant. Ce ne sont pas des objets utiles ni des choses faciles à revendre."
    noam inquiet "Quelqu'un a choisi précisément ce qui avait le plus de valeur pour nous."

    menu:
        "C'est un message.":
            $ noam_j8_choix_resolution = "direct"
            noam raison "C'est un message. Quelqu'un veut nous montrer qu'il peut entrer partout et qu'il sait ce que chacun garde."
            "Lysa croise les bras et observe les visages autour d'elle."
            lysa neutre "Ou il veut simplement nous pousser à nous méfier les uns des autres."
            noam raison "Dans ce cas, le message fonctionne déjà."

        "Ne rien dire.":
            $ noam_j8_choix_resolution = "silencieux"
            think "Je garde mon interprétation pour moi. Kael est encore trop fragile et je ne suis pas assez certain de ce que ces vols signifient."

    $ hideGroup()
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_298
    scene bg_cafeteria at adaptive_fullscreen with dissolve

    "Les minutes passent. Les autres finissent par se lever, non pour partir, mais parce que rester immobiles autour de Kael devient insupportable."

    think "Je reste encore un moment. Il faut découvrir qui a fait ça avant qu'un autre objet disparaisse, ou que quelqu'un décide de chercher un coupable au hasard."

    if noam_j8_choix_resolution == "direct":
        think "J'ai dit ce que je pensais à voix haute. Au moins, nous savons désormais que nous cherchons peut-être autre chose qu'un simple voleur."
    else:
        think "J'aurais peut-être dû partager mon hypothèse, mais ajouter une menace invisible n'aurait pas aidé Kael à respirer. Je pourrai encore en parler plus tard."

    think "Pour le moment, je ne possède que deux certitudes : quelqu'un est entré dans nos chambres et a pris exactement ce qui comptait le plus."
    think "Je ne sais pas encore qui. Seulement pas encore."

    $ journal_entries.append(("Jour 8 — soir", "La photo de Léa. Le dessin de Juliette. Deux objets. Deux chambres. Quelqu'un sait ce qu'on garde. Ce que ça veut dire, je préfère pas y penser trop longtemps. Mais je vais trouver qui."))
    stop music fadeout 2.0
    scene black with fade
    jump _8_0_1_SOIREE

label _8_0_1_SOIREE:
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_299
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0
    $ showGroup([("noam", "inquiet", 0.50)])

    "Après avoir erré dans les couloirs sans savoir quoi chercher, je retourne dans ma chambre et referme soigneusement la porte."

    "Le désordre du matin n'a pas bougé. Le sac reste ouvert sur le lit, le placard ferme mal et aucun dessin n'est miraculeusement réapparu pendant mon absence."

    think "Deux jours sans Kami ont suffi pour nous faire croire que nous étions libres. Maintenant, nous nous observons déjà comme des suspects."

    "Je m'assieds sur le bord du lit et regarde chaque meuble comme si la personne qui était entrée avait pu laisser une trace évidente."

    think "Quelqu'un est venu ici. Il savait ce qui comptait pour moi et il l'a emporté sans toucher au reste."

    "L'écran mural demeure noir. Son silence ne me rassure plus du tout."

    think "Peut-être que tout ça n'a rien à voir avec Kami. Ou peut-être que cette peur est exactement ce qu'elle attendait de son absence."

    "Je tire la chaise jusqu'à la porte et la bloque sous la poignée. Ce n'est pas une vraie protection, mais je saurai au moins si quelqu'un essaie d'entrer pendant mon sommeil."

    think "Demain, je trouverai qui a pris le dessin et la photo. Même si la réponse me conduit vers l'un d'entre nous."

    $ journal_entries.append(("Jour 8 — conclusion", "Quelqu’un nous observe. Quelqu’un nous connaît et nous vole. Et ce quelqu’un est parmi nous."))
    $ hideGroup()
    call end_day("9") from _call_end_day_12
    jump _9_0_1_REVEIL_CHAMBRE
