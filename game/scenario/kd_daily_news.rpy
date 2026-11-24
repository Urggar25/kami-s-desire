# Bulletins facultatifs J1-J6. Aucun effet sur les stats, votes ou temps libre.
# Une lecture par journée, partagée entre les trois télévisions.
default kd_daily_news_seen = []

label kd_daily_news_watch:
    if day_number() not in (1, 2, 3, 4, 5, 6):
        return
    if day_number() in kd_daily_news_seen:
        think "C'est le même bulletin que tout à l'heure."
        return
    $ kd_daily_news_seen = kd_daily_news_seen + [day_number()]
    if day_number() == 4:
        if getattr(store, "vote1", "") == "OUI":
            call kd_daily_news_4_oui from _call_kd_daily_news_4_oui
        else:
            call kd_daily_news_4_non from _call_kd_daily_news_4_non
    elif day_number() == 3 and getattr(store, "vote1", "") in ("OUI", "NON"):
        call kd_daily_news_3_after from _call_kd_daily_news_3_after
    else:
        call expression "kd_daily_news_%s" % day_number()
    return

label kd_daily_news_3_after:
    call kd_news_open(_("LIMEN 24"), _("LE PREMIER SCRUTIN"), _("JOURNAL")) from _call_kd_daily_news_open_3_after
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    if getattr(store, "vote1", "") == "OUI":
        show screen kd_news_broadcast(_("LIMEN 24"), _("JOURNAL"), _("Le commerce rétabli"), (_("La distribution gratuite prend fin."),))
        window auto
        "PRÉSENTATRICE — Le Conclave a adopté le texte autorisant le commerce. Les modalités pratiques restent à préciser."
    else:
        show screen kd_news_broadcast(_("LIMEN 24"), _("JOURNAL"), _("Le commerce reste interdit"), (_("Le système de distribution est maintenu."),))
        window auto
        "PRÉSENTATRICE — Le Conclave n'a pas adopté le texte sur le commerce. Les règles de distribution restent en vigueur."
    "PRÉSENTATRICE — Nous reviendrons demain sur les réactions des habitants. Pour l'instant, place à la météo."
    think "Ça fait bizarre de les entendre parler de nous comme ça."
    call kd_news_close from _call_kd_daily_news_close_3_after
    return

label kd_daily_news_1:
    call kd_news_open(_("LIMEN 24"), _("Le Conclave vu d'en bas"), _("JOURNAL")) from _call_kd_daily_news_open_1
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("NEXUS — MICRO-TROTTOIR"), _("Une question de famille"), (_("Les représentants sont réunis en orbite."), _("Retrouvez notre rubrique culture après le journal.")))
    window auto
    "JOURNALISTE — Vous avez suivi l'annonce concernant le Conclave ?"
    "UN HOMME — Oui, enfin... ma femme l'a suivie. Moi, j'étais en train de réparer le four."
    "JOURNALISTE — Vous attendez quelque chose de ces représentants ?"
    "UN HOMME — Qu'ils nous laissent revoir notre fils. Il travaille dans un autre district."
    "UNE FEMME — Dis-lui pour le four."
    "UN HOMME — Mais elle s'en fout, du four !"
    "UNE FEMME — Ça fait trois semaines que tu le répares."
    "JOURNALISTE — Votre fils vit loin de chez vous ?"
    "UNE FEMME — Pas tellement. C'est ça qui est bête. On pourrait y aller à pied."
    "UN HOMME — Il nous appelle le dimanche. Quand il y pense."
    "UNE FEMME — Il y pense. C'est toi qui coupes la sonnerie."
    "JOURNALISTE — Merci à vous deux."
    "Je baisse un peu le volume. J'ai presque envie de savoir ce qu'il a, ce four."
    call kd_news_close from _call_kd_daily_news_close_1
    return

label kd_daily_news_2:
    call kd_news_open(_("LIMEN 24"), _("Un concours très disputé"), _("JOURNAL")) from _call_kd_daily_news_open_2
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("HARMONIE — VIE LOCALE"), _("Le plus beau balcon du quartier"), (_("Concours de jardinage : les inscriptions sont ouvertes."), _("La météo à suivre dans notre prochaine édition.")))
    window auto
    "PRÉSENTATRICE — Et nous retrouvons notre jury pour le concours annuel des balcons fleuris."
    "JURÉ — Alors, ici, nous avons un très beau travail sur les couleurs."
    "UNE HABITANTE — Merci. C'est mon mari qui a choisi les pots."
    "JURÉ — Et les fleurs ?"
    "UNE HABITANTE — Ah non, surtout pas lui."
    "UN HOMME — J'ai quand même planté les tomates."
    "UNE HABITANTE — On ne met pas de tomates dans un concours de fleurs !"
    "UN HOMME — Elles ont des fleurs, mes tomates."
    "JURÉ — Techniquement, monsieur n'a pas tort."
    "UNE HABITANTE — Vous voulez les noter aussi ?"
    "UN HOMME — Attendez, je vais vous en chercher une."
    "PRÉSENTATRICE — Nous retrouverons les résultats demain."
    "Je serais curieux de voir la note des tomates."
    call kd_news_close from _call_kd_daily_news_close_2
    return

label kd_daily_news_3:
    call kd_news_open(_("LIMEN 24"), _("Le premier scrutin"), _("JOURNAL")) from _call_kd_daily_news_open_3
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("NEXUS — ÉCONOMIE"), _("Les commerçants attendent"), (_("Le Conclave examine la question du commerce."), _("Les habitants suivent les annonces officielles.")))
    window auto
    "JOURNALISTE — Si les échanges sont autorisés, vous comptez ouvrir votre boutique ?"
    "UNE ANCIENNE COMMERÇANTE — Si j'arrive à ouvrir la grille, oui."
    "JOURNALISTE — Elle est coincée ?"
    "UNE ANCIENNE COMMERÇANTE — Ça fait des années qu'elle n'a pas bougé. J'ai même perdu la clé."
    "JOURNALISTE — Et vous vendriez quoi ?"
    "UNE ANCIENNE COMMERÇANTE — Des chaussures. Enfin, j'en ai encore quelques paires derrière."
    "JOURNALISTE — Vous les avez conservées ?"
    "UNE ANCIENNE COMMERÇANTE — Mon mari voulait jeter le stock. Je lui ai dit d'attendre."
    "JOURNALISTE — Vous pensiez que le commerce reviendrait ?"
    "UNE ANCIENNE COMMERÇANTE — Non. Je détestais surtout l'idée de jeter toutes ces chaussures."
    "UNE ANCIENNE COMMERÇANTE — Il y a une paire à votre taille, d'ailleurs. Les marron."
    "JOURNALISTE — Ah... On en reparle après."
    "Je regarde mes propres chaussures. Les siennes sont probablement plus confortables."
    call kd_news_close from _call_kd_daily_news_close_3
    return

label kd_daily_news_4_non:
    call kd_news_open(_("LIMEN 24"), _("Distribution des denrées"), _("JOURNAL")) from _call_kd_daily_news_open_4_non
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("LIMEN — SOLIDARITÉ"), _("Une distribution sous surveillance"), (_("Le système de distribution est maintenu."), _("Des familles attendent leur colis.")))
    window auto
    "JOURNALISTE — Vous avez pu récupérer votre colis ?"
    "UN HOMME — Oui. Celui de ma voisine aussi, elle ne peut pas descendre les escaliers."
    "JOURNALISTE — Vous faites ça régulièrement ?"
    "UN HOMME — Quand elle me laisse faire. Elle est persuadée que je vais lui piquer ses biscuits."
    "JOURNALISTE — Et vous avez assez pour la semaine ?"
    "UN HOMME — Pour moi, oui. J'ai pas d'enfants à nourrir."
    "UNE VOISINE, HORS CHAMP — Gérard ! T'as pris les petits biscuits ou les grands ?"
    "UN HOMME — Les petits !"
    "UNE VOISINE — Ah, merde."
    "UN HOMME — Vous voyez ?"
    "Le journaliste s'écarte pour le laisser passer avec ses deux colis."
    call kd_news_close from _call_kd_daily_news_close_4_non
    return

label kd_daily_news_4_oui:
    call kd_news_open(_("LIMEN 24"), _("Le retour des échanges"), _("JOURNAL")) from _call_kd_daily_news_open_4_oui
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("NEXUS — ÉCONOMIE"), _("Les premiers prix font discuter"), (_("Le commerce est de nouveau autorisé."), _("La distribution gratuite prend fin.")))
    window auto
    "JOURNALISTE — Vous avez affiché vos prix ce matin ?"
    "UN VENDEUR — Oui. J'en ai déjà changé trois."
    "JOURNALISTE — Pourquoi ?"
    "UN VENDEUR — Parce que mon voisin vend les mêmes trucs. Et qu'il me regarde écrire."
    "UNE CLIENTE — Vous prenez quoi en échange ?"
    "UN VENDEUR — Pour l'instant, ça dépend de ce que vous avez."
    "UNE CLIENTE — J'ai deux serviettes neuves."
    "UN VENDEUR — Ah. Je vends justement des serviettes."
    "UNE CLIENTE — Et du savon ?"
    "UN VENDEUR — Plus de savon. Lui, là-bas, il en a."
    "JOURNALISTE — Vous lui envoyez vos clients ?"
    "UN VENDEUR — C'est mon frère. Il m'a prêté la table."
    "Je me demande ce que les gens qui n'ont rien à échanger vont faire."
    call kd_news_close from _call_kd_daily_news_close_4_oui
    return

label kd_daily_news_5:
    call kd_news_open(_("LIMEN 24"), _("Une finale interminable"), _("JOURNAL")) from _call_kd_daily_news_open_5
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("HARMONIE — SPORT"), _("Le tournoi de ping-pong reprend"), (_("La finale locale oppose deux habitués du club."), _("Le classement sera publié après la rencontre.")))
    window auto
    "COMMENTATEUR — Nous en sommes à la troisième interruption de cette finale."
    "COMMENTATRICE — Le joueur de gauche conteste encore le point ?"
    "COMMENTATEUR — Non, il cherche sa balle. Elle est passée sous le banc."
    "UN JOUEUR — Elle est de votre côté !"
    "UN AUTRE JOUEUR — J'ai mal au dos, moi."
    "COMMENTATRICE — Il a effectivement pris sa retraite sportive il y a quatre ans."
    "COMMENTATEUR — Il est revenu l'année dernière parce que son épouse en avait marre de le voir à la maison."
    "COMMENTATRICE — Ah, la voilà. La balle, pas son épouse."
    "UN JOUEUR — On en était à combien ?"
    "UN AUTRE JOUEUR — Onze à huit."
    "UN JOUEUR — N'importe quoi !"
    "COMMENTATEUR — Et nous repartons sur une quatrième interruption..."
    "Je crois que je préfère regarder ça plutôt que jouer avec Julian."
    call kd_news_close from _call_kd_daily_news_close_5
    return

label kd_daily_news_6:
    call kd_news_open(_("LIMEN 24"), _("La vie près des frontières"), _("JOURNAL")) from _call_kd_daily_news_open_6
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("LIMEN — SOCIÉTÉ"), _("Des habitants parlent de leurs proches"), (_("Les restrictions frontalières demeurent en vigueur."), _("Suivez les prochaines annonces du Conclave.")))
    window auto
    "JOURNALISTE — Votre sœur vous manque ?"
    "UNE JEUNE FEMME — Oui. Enfin, elle m'énerve aussi. Même au téléphone."
    "JOURNALISTE — Vous vous appelez souvent ?"
    "UNE JEUNE FEMME — Tous les soirs. Elle veut voir mon chat, surtout."
    "JOURNALISTE — Vous voudriez lui rendre visite ?"
    "UNE JEUNE FEMME — C'est elle qui veut venir. Elle a déjà choisi le canapé sur lequel elle va dormir."
    "JOURNALISTE — Vous avez une chambre d'amis ?"
    "UNE JEUNE FEMME — Oui, mais le canapé est plus près du chat."
    "JOURNALISTE — Vous avez prévu quelque chose si les restrictions changent ?"
    "UNE JEUNE FEMME — Je lui ai demandé de ne pas faire sa valise. Elle l'a faite quand même."
    "UNE JEUNE FEMME — Je lui ai dit que je l'appellerais dès qu'on saurait quelque chose."
    "Elle sort son téléphone de sa poche pour vérifier l'heure."
    call kd_news_close from _call_kd_daily_news_close_6
    return

