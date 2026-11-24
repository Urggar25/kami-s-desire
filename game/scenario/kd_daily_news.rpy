# Bulletins facultatifs J1-J6. Aucun effet sur les stats, votes ou temps libre.
# Une lecture par bulletin, partagée entre les trois télévisions (J3 avant/après).
default kd_daily_news_seen = []

label kd_daily_news_watch:
    if day_number() not in (1, 2, 3, 4, 5, 6):
        return
    $ kd_news_watch_key = (3, getattr(store, "vote1", "")) if day_number() == 3 else day_number()
    if kd_news_watch_key in kd_daily_news_seen:
        think "C'est le même bulletin que tout à l'heure."
        return
    $ kd_daily_news_seen = kd_daily_news_seen + [kd_news_watch_key]
    if day_number() == 4:
        if getattr(store, "vote1", "") == "OUI":
            call kd_daily_news_4_oui from _call_kd_daily_news_4_oui
        else:
            call kd_daily_news_4_non from _call_kd_daily_news_4_non
    elif day_number() == 3 and getattr(store, "vote1", "") in ("OUI", "NON"):
        call kd_daily_news_3_after from _call_kd_daily_news_3_after
    elif day_number() == 1:
        call kd_daily_news_1 from _call_kd_daily_news_dispatch_1
    elif day_number() == 2:
        call kd_daily_news_2 from _call_kd_daily_news_dispatch_2
    elif day_number() == 3:
        call kd_daily_news_3 from _call_kd_daily_news_dispatch_3
    elif day_number() == 5:
        call kd_daily_news_5 from _call_kd_daily_news_dispatch_5
    elif day_number() == 6:
        call kd_daily_news_6 from _call_kd_daily_news_dispatch_6
    return

label kd_daily_news_3_after:
    call kd_news_open(_("LIMEN 24"), _("LE PREMIER SCRUTIN"), _("JOURNAL")) from _call_kd_daily_news_open_3_after
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    if getattr(store, "vote1", "") == "OUI":
        show screen kd_news_broadcast(_("LIMEN 24"), _("JOURNAL"), _("Le commerce rétabli"), (_("La distribution gratuite prend fin."),))
        window auto
        $ kd_news_stage("studio", "anchor")
        kd_tv_anchor "Le Conclave a adopté le texte autorisant le commerce. Les modalités pratiques restent à préciser."
    else:
        show screen kd_news_broadcast(_("LIMEN 24"), _("JOURNAL"), _("Le commerce reste interdit"), (_("Le système de distribution est maintenu."),))
        window auto
        $ kd_news_stage("studio", "anchor")
        kd_tv_anchor "Le Conclave n'a pas adopté le texte sur le commerce. Les règles de distribution restent en vigueur."
    kd_tv_anchor "Nous reviendrons demain sur les réactions des habitants. Pour l'instant, place à la météo."
    think "Ça fait bizarre de les entendre parler de nous comme ça."
    call kd_news_close from _call_kd_daily_news_close_3_after
    return

label kd_daily_news_1:
    call kd_news_open(_("LIMEN 24"), _("Le monde regarde le Conclave"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_1
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — CONCLAVE"), _("Douze représentants, des millions de vies"), (_("Les représentants sont réunis en orbite."), _("Le Conclave peut modifier les Commandements à l’unanimité.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Nous consacrons l'essentiel de cette édition à l'ouverture du Conclave. Pour la première fois, les représentants sont réunis en orbite pour examiner les règles qui régissent notre quotidien."
    kd_tv_anchor "Qu'est-ce que vous attendez d'eux ? Nous avons posé la question dans plusieurs districts."
    $ kd_news_stage("interview", "reporter", "mother", "father")
    kd_tv_mother "Qu'on puisse revoir notre fils. Il habite de l'autre côté de la frontière."
    kd_tv_father "On en parle depuis ce matin. Elle a même sorti les affaires du petit."
    kd_tv_mother "Arrête. J'ai juste préparé son lit."
    kd_tv_reporter "Vous pensez qu'il pourra bientôt revenir ?"
    kd_tv_mother "Je sais pas. Vous avez vu les gens qu'ils ont envoyés là-haut, vous ? Ils ont l'air de s'entendre ?"
    kd_tv_reporter "Il est encore un peu tôt pour le dire."
    kd_tv_father "Ils ont bien le droit de pas être d'accord, non ?"
    kd_tv_mother "Oui, mais faudrait pas qu'ils le soient trop longtemps."
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Nous suivrons leurs premières décisions dans les prochaines éditions."
    "Je reconnais le décor de la station sur le générique de fin. Ça me fait un drôle d'effet de le voir à la télévision."
    call kd_news_close from _call_kd_daily_news_close_1
    return


label kd_daily_news_2:
    call kd_news_open(_("LIMEN 24"), _("Le baromètre du Conclave"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_2
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — SONDAGE"), _("Quel représentant vous inspire confiance ?"), (_("Consultation ouverte aux téléspectateurs."), _("Sondage de participation libre : résultats non représentatifs.")))
    window auto
    $ kd_news_stage("debate", "anchor", "commentator")
    kd_tv_anchor "Depuis hier, les messages sur les douze représentants affluent à la rédaction. Nous avons demandé à nos téléspectateurs à qui ils feraient le plus confiance."
    kd_tv_commentator "Parmi les noms qui reviennent le plus souvent : Nyra, Sael et Julian."
    kd_tv_anchor "Julian ? Pour quelles raisons ?"
    kd_tv_commentator "Alors... j'ai les commentaires ici. Il est bien habillé, il regarde la caméra et il a de très beaux cheveux."
    kd_tv_anchor "On leur a posé une question sur la confiance."
    kd_tv_commentator "Oui, je sais."
    kd_tv_anchor "Et les deux autres ?"
    kd_tv_commentator "Nyra a l'air de savoir ce qu'elle fait. Pour Sael, beaucoup de gens disent qu'ils aimeraient l'avoir comme médecin."
    kd_tv_anchor "D'accord. Est-ce que les gens connaissent leurs positions ?"
    kd_tv_commentator "Pas vraiment. On a aussi reçu vingt-sept messages de la même personne qui réclame le numéro de Julian."
    kd_tv_anchor "On ne va pas lui donner."
    kd_tv_commentator "Non."
    "Je devrais peut-être éviter de raconter ça à Julian."
    $ kd_news_sfx("poll")
    hide screen kd_news_actor_stage
    show screen kd_news_poll_results
    "Un classement apparaît à l'écran. Nyra, Sael, Julian. Pas de Noam."
    hide screen kd_news_poll_results
    call kd_news_close from _call_kd_daily_news_close_2
    return


label kd_daily_news_3:
    call kd_news_open(_("LIMEN 24"), _("Premier vote : le commerce"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_3
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — AVANT LE SCRUTIN"), _("Le monde suspendu à la décision"), (_("Le Conclave examine la reprise des échanges."), _("L’adoption d’un amendement exige l’unanimité.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "C'est aujourd'hui que le Conclave doit se prononcer sur le retour du commerce. Des habitants se sont rassemblés devant les écrans dans plusieurs districts."
    kd_tv_anchor "Nous retrouvons notre correspondant devant une ancienne boutique de chaussures."
    $ kd_news_stage("interview", "reporter", "shopwoman")
    kd_tv_reporter "Si le texte passe, vous comptez rouvrir ?"
    kd_tv_shopwoman "Si j'arrive à ouvrir la grille, oui. J'ai perdu la clé."
    kd_tv_reporter "Vous avez gardé votre stock ?"
    kd_tv_shopwoman "Une partie. Mon mari voulait tout jeter."
    kd_tv_reporter "Et si la distribution gratuite devait disparaître avec le retour du commerce ?"
    kd_tv_shopwoman "Ah, ça... Vous savez, moi aussi je récupère mes colis. Je peux pas manger des chaussures."
    kd_tv_reporter "Vous souhaitez toujours que le texte soit adopté ?"
    kd_tv_shopwoman "J'aimerais surtout savoir ce qu'ils vont voter exactement."
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Nous attendons le résultat. Pour rappel, un seul vote contre suffit à empêcher l'adoption."
    "J'ai l'impression d'avoir un peu moins envie de retourner dans cette salle."
    call kd_news_close from _call_kd_daily_news_close_3
    return


label kd_daily_news_4_non:
    call kd_news_open(_("LIMEN 24"), _("Le premier vote a échoué"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_4_non
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — LIMEN"), _("Le rejet du commerce divise les habitants"), (_("Le premier amendement n’a pas été adopté."), _("La distribution gratuite reste en vigueur.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Au lendemain du rejet du texte sur le commerce, les réactions se multiplient. À Limen, la distribution des denrées se poursuit."
    $ kd_news_stage("interview", "reporter", "worker", "woman")
    kd_tv_reporter "Vous avez suivi le résultat hier ?"
    kd_tv_worker "Oui. J'ai éteint la télé après."
    kd_tv_reporter "Vous êtes déçu ?"
    kd_tv_worker "Mon frère avait ressorti son matériel de menuiserie. Il s'était fait tout un programme."
    kd_tv_woman "Moi, j'ai dormi pour la première fois correctement depuis trois jours."
    kd_tv_reporter "Vous souhaitiez le rejet du texte ?"
    kd_tv_woman "J'ai deux enfants. Tant que je sais ce qu'on va manger, le reste... Enfin, on verra."
    kd_tv_worker "Je lui en veux pas, hein. À madame."
    kd_tv_woman "Oh, mais je l'ai pas pris pour moi."
    kd_tv_reporter "Est-ce que vous avez confiance pour la suite ?"
    kd_tv_worker "Bah, je vais regarder. Qu'est-ce que vous voulez que je fasse d'autre ?"
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "La rédaction reviendra sur les prochaines propositions du Conclave dès leur annonce."
    call kd_news_close from _call_kd_daily_news_close_4_non
    return


label kd_daily_news_4_oui:
    call kd_news_open(_("LIMEN 24"), _("Le commerce est rétabli"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_4_oui
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — NEXUS"), _("Premiers échanges, premières difficultés"), (_("Le Conclave a adopté son premier amendement."), _("La distribution gratuite prend fin.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Le premier amendement du Conclave a été adopté. Partout, les habitants tentent de s'organiser face au retour des échanges et à la fin des distributions gratuites."
    $ kd_news_stage("interview", "reporter", "vendor", "customer")
    kd_tv_reporter "Vous avez affiché vos prix ce matin ?"
    kd_tv_vendor "Oui. J'en ai déjà changé trois."
    kd_tv_reporter "Pourquoi ?"
    kd_tv_vendor "Parce que mon voisin vend les mêmes trucs. Et qu'il me regarde écrire."
    kd_tv_customer "Vous prenez quoi en échange ?"
    kd_tv_vendor "Pour l'instant, ça dépend de ce que vous avez."
    kd_tv_customer "J'ai deux serviettes neuves."
    kd_tv_vendor "Ah. Je vends justement des serviettes."
    kd_tv_customer "Et du savon ?"
    kd_tv_vendor "Plus de savon. Lui, là-bas, il en a."
    kd_tv_reporter "Vous lui envoyez vos clients ?"
    kd_tv_vendor "C'est mon frère. Il m'a prêté la table."
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Ailleurs, des habitants s'inquiètent de ne rien avoir à échanger. Nous poursuivrons notre couverture tout au long de la journée."
    call kd_news_close from _call_kd_daily_news_close_4_oui
    return


label kd_daily_news_5:
    call kd_news_open(_("LIMEN 24"), _("Le Conclave jusque dans les foyers"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_5
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — SOCIÉTÉ"), _("Les familles ne décrochent plus"), (_("Les débats du Conclave dominent les éditions d’information."), _("Culture : la finale locale de tennis de table est reportée dans notre grille.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Depuis l'ouverture du Conclave, de nombreux habitants organisent leurs journées autour des annonces venues de la station."
    $ kd_news_stage("home", "reporter", "teen", "dad")
    kd_tv_reporter "Vous regardez les informations ensemble ?"
    kd_tv_teen "Non. Mon père regarde, moi j'aimerais bien récupérer la télé."
    kd_tv_dad "Il y a des décisions importantes qui se prennent."
    kd_tv_teen "Papa, tu regardes la rediffusion. On l'a déjà vue deux fois."
    kd_tv_dad "J'essaie de comprendre ce que dit la fille, là. Nyra."
    kd_tv_reporter "Vous suivez surtout un représentant ?"
    kd_tv_teen "Lui, c'est Nyra. Maman, c'est Sael. Mon petit frère veut la veste de Noam."
    kd_tv_dad "Ah oui. Ça, il nous embête avec depuis deux jours."
    kd_tv_teen "Il en a trouvé une dans le placard. Elle lui arrive aux genoux."
    kd_tv_reporter "Et vous ?"
    kd_tv_teen "Je voudrais juste regarder un film."
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Nous retrouverons les résultats sportifs à la fin de cette édition."
    "Attendez... ma veste ?"
    call kd_news_close from _call_kd_daily_news_close_5
    return


label kd_daily_news_6:
    call kd_news_open(_("LIMEN 24"), _("Les frontières au cœur des attentes"), _("ÉDITION SPÉCIALE")) from _call_kd_daily_news_open_6
    scene expression "images/kd_news/daily_studio.svg" at adaptive_fullscreen
    show screen kd_news_broadcast(_("LIMEN 24"), _("ÉDITION MONDIALE — LIMEN"), _("Des familles attendent une décision"), (_("Le franchissement des frontières reste soumis aux restrictions."), _("Les habitants attendent les prochaines décisions du Conclave.")))
    window auto
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "La question des frontières mobilise aujourd'hui des habitants dans plusieurs districts. Beaucoup espèrent une décision qui leur permettra enfin de retrouver leurs proches."
    $ kd_news_stage("interview", "reporter", "youngwoman")
    kd_tv_reporter "Votre sœur vous manque ?"
    kd_tv_youngwoman "Oui. Enfin, elle m'énerve aussi. Même au téléphone."
    kd_tv_reporter "Vous vous appelez souvent ?"
    kd_tv_youngwoman "Tous les soirs. Elle veut voir mon chat, surtout."
    kd_tv_reporter "Vous voudriez lui rendre visite ?"
    kd_tv_youngwoman "C'est elle qui veut venir. Elle a déjà choisi le canapé sur lequel elle va dormir."
    kd_tv_reporter "Vous avez une chambre d'amis ?"
    kd_tv_youngwoman "Oui, mais le canapé est plus près du chat."
    kd_tv_reporter "Vous avez prévu quelque chose si les restrictions changent ?"
    kd_tv_youngwoman "Je lui ai demandé de ne pas faire sa valise. Elle l'a faite quand même."
    kd_tv_youngwoman "Je lui ai dit que je l'appellerais dès qu'on saurait quelque chose."
    $ kd_news_stage("studio", "anchor")
    kd_tv_anchor "Nous resterons à l'antenne pour les annonces du Conclave."
    call kd_news_close from _call_kd_daily_news_close_6
    return


# Classement éditorial fictif, sans pourcentages inventés à l'intérieur du récit.
# L'échantillon volontaire ne permet pas d'établir une cote mondiale.
transform kd_news_poll_enter(delay=0.0):
    alpha 0.0
    xoffset -55
    pause delay
    easeout 0.30 alpha 1.0 xoffset 0

screen kd_news_poll_results():
    zorder 6
    modal False
    fixed:
        xpos 330
        ypos 112
        xysize (1260, 485)
        add Solid("#081727f5", xysize=(1260, 485))
        text _("BAROMÈTRE DES TÉLÉSPECTATEURS") style "kd_news_title" xpos 38 ypos 25
        text _("Noms les plus cités • consultation ouverte") style "kd_news_small" color "#9dc8de" xpos 38 ypos 86
        for i, name in enumerate(("Nyra", "Sael", "Julian")):
            fixed:
                xpos 38
                ypos (145 + i * 91)
                xysize (1184, 76)
                at kd_news_poll_enter(i * 0.12)
                add Solid("#1a3a51", xysize=(1184, 76))
                add Solid("#66c8df", xysize=(6, 76))
                text ("%02d" % (i + 1)) style "kd_news_title" color "#83d6e8" xpos 24 yalign 0.5
                text name style "kd_news_title" xpos 112 yalign 0.5
        text _("Participation libre — non représentatif") style "kd_news_small" color "#9dc8de" xpos 38 ypos 434
