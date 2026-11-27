# --------------------------------------------------------------------------------------------
# JOUR 8 — Reconstitution de la disparition du dessin et crise de Kael
# Continuité : assistance de Lysa et divulgation du relevé de Tomas au J7.
# Scène PnC : Noam reconstitue ses derniers souvenirs plutôt que de refaire la fouille.
# La crise de Kael révèle un autre objet intime disparu sans conclure à un coupable.
# --------------------------------------------------------------------------------------------

label _8_1_0_0_CANON:
    # Compatibilité avec les sauvegardes et anciens sauts du J8_0_1.
    jump _8_0_1_REVEIL_CHAMBRE

label _8_0_1_REVEIL_CHAMBRE:
    scene black
    $ current_day = 8
    $ noam_has_juliette_drawing = False
    $ current_period = "Matin"
    $ cafeteria_food_level = "high"
    play music "music/bgm_calm_not_peace.mp3" fadein 2.5

    $ blink()
    pause 1.0
    $ blink()
    scene bg_cg012 at adaptive_fullscreen with dissolve

    "Je me réveille avant d'avoir entendu quoi que ce soit. Depuis mon arrivée, j'ai pris l'habitude de regarder l'écran de Kami avant même de me lever."
    think "Elle ne nous a toujours pas parlé. Je devrais en profiter pour dormir un peu plus."
    "Je tends la main vers ma tablette, et je repense immédiatement au dessin. Je l'ai cherché jusqu'à une heure ridicule hier soir, mais une partie de moi s'attend encore à le voir sur le bureau."
    scene bg_chambre at adaptive_fullscreen with dissolve
    noam fatigue "Je suis quand même pas capable de perdre une feuille dans une pièce aussi petite..."
    "Juliette m'avait fait promettre de ne pas regarder le dessin avant qu'elle ait terminé. J'avais essayé de lui apporter un goûter pendant qu'elle s'occupait de mon nez et elle m'avait littéralement chassé de sa chambre. Quand elle me l'a enfin donné, j'ai découvert qu'elle m'avait dessiné avec le pull que je portais tout le temps à la maison."
    "Je me souviens très bien de l'avoir regardé hier matin. C'est après que j'ai du mal à me rappeler ce que j'ai fait."
    if j701_lysa_search_help:
        play sound sfx_knock
        lysa "Noam ? C'est moi. J'ai pris du café, ouvre avant que je fasse tomber quelque chose."
        "J'ouvre la porte et récupère un des gobelets. Lysa regarde par-dessus mon épaule."
        lysa "Tu as fait tout ça hier soir ? Je pensais que tu avais juste vidé quelques tiroirs."
        noam hesitation "J'ai commencé à ranger, puis je me suis dit que j'avais peut-être remis le dessin quelque part sans faire attention. Du coup, j'ai ressorti tout ce que je venais de ranger."
        lysa "Je peux entrer ou tu préfères qu'on reste dans le couloir ?"
        noam "Vas-y. Fais gaffe à la tablette."
        "Elle déplace un vêtement qui traîne sur le bureau pour poser son café."
        lysa "Bon, explique-moi ce que tu cherches. Je n'ai pas vu le dessin, moi."
        noam hesitation "C'est une feuille que ma petite sœur m'a donnée avant que je parte. Il y a un portrait de moi dessus, elle a même écrit son nom en bas. Je la laisse à côté de la lampe d'habitude."
        lysa "Et tu t'en es aperçu en rentrant hier soir ?"
        noam "Ouais. J'ai déjà vérifié les tiroirs et les poches de mes vêtements. Je crois que je vais essayer de refaire ce que j'ai fait hier matin, parce qu'à force de tout déplacer, je ne sais même plus comment j'avais laissé la chambre."
        lysa "Ça me paraît plus utile que de recommencer la fouille. Si tu veux, je peux regarder avec toi, mais j'ai promis à Elen de passer la voir et je suis déjà en retard."
        noam "T'inquiète, je t'avais surtout demandé de venir parce que je commençais à m'énerver tout seul hier. Je vais reprendre tranquillement."
        lysa "D'accord. Tu me retrouves à la cafétéria ? Et bois ton café avant qu'il refroidisse."
        "Elle finit le sien debout près de la porte, puis repart."
    else:
        "J'ouvre la messagerie de Lysa. J'ai presque envie de lui demander de venir, mais je ne saurais même pas lui dire quoi chercher en priorité."
        think "Je vais d'abord essayer de me souvenir de ce que j'ai fait avant de sortir hier."
    tuto "(Examine les objets et la porte pour reconstituer la matinée d'hier. Les preuves seront enregistrées dans ta tablette.)"
    $ hideGroup()
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ pnc_room = "chambre_j8"
    $ pnc_flags = {}
    $ room_scene_indices["chambre"] = 1
    jump _8_PNC_BOUCLE

screen pnc_chambre_j8():

    modal True
    zorder 200

    use room_scene_background("chambre")

    $ j8_targets = {
        "chambre1_aeration": "_8_PNC_AERATION",
        "chambre1_lit": "_8_PNC_LIT",
        "chambre1_television": "_8_PNC_TELEVISION",
        "chambre1_tiroir": "_8_PNC_TIROIR",
        "chambre2_armoire": "_8_PNC_ARMOIRE",
        "chambre2_porte_dehors": "_8_PNC_SORTIE",
        "chambre2_porte_sdb": "_8_PNC_SALLE_DE_BAIN",
        "chambre3_brouilleur": "_8_PNC_BROUILLEUR",
        "chambre3_tablette": "_8_PNC_TABLETTE",
    }

    # Cette scène renvoie la zone cliquée à une boucle unique. Contrairement à
    # l'ancienne fouille, chaque clic ne crée donc pas un nouvel écran imbriqué.
    for key, path in room_interaction_files("chambre"):
        $ label_name = room_interaction_label("chambre", key)
        $ target_label = j8_targets.get(label_name)
        if target_label and (not room_interaction_is_decorative(key) or label_name == "chambre3_brouilleur"):
            imagebutton:
                idle room_interaction_null()
                hover room_interaction_hover_with_overlays(path, "chambre")
                focus_mask room_interaction_layer(path, "chambre", "art")
                xpos 0
                ypos 0
                action Return(target_label)

    # Les bandes doivent être au-dessus des hotspots, comme dans l'exploration standard.
    if room_scene_has_variants("chambre"):
        use room_scene_navigation_band("chambre", -1, 0)
        use room_scene_navigation_band("chambre", 1, config.screen_width - ROOM_SCENE_NAV_WIDTH)

    $ j8_required = ("lit", "tiroir", "armoire", "tablette", "porte")
    $ j8_search_count = sum(1 for key in j8_required if pnc_flags.get(key))

    frame:
        xalign 0.5
        yalign 0.035
        padding (24, 12)
        background Solid("#071019D9")

        vbox:
            spacing 2
            text "RECONSTITUER LA MATINÉE D'HIER" xalign 0.5 size 22 color "#D6E8F0"
            text "Éléments examinés : [j8_search_count] / 5" xalign 0.5 size 16 color "#7FCFEA"

# -------------------------------------------------------
# LABELS PnC
# -------------------------------------------------------

label _8_PNC_BOUCLE:
    $ hideGroup()
    call screen pnc_chambre_j8()
    $ j8_selected_interaction = _return
    call expression j8_selected_interaction from _call_expression_5
    if all(pnc_flags.get(key) for key in ("lit", "tiroir", "armoire", "tablette")):
        $ investigation_add("dessin_juliette_disparu")
    if _return == "j8_search_done":
        jump _8_FIN_RECHERCHE
    jump _8_PNC_BOUCLE

label _8_PNC_AERATION:
    if pnc_flags.get("aeration"):
        think "Il n'y a rien derrière la grille, je viens de vérifier."
        return

    $ pnc_flags["aeration"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "J'approche une main de la bouche d'aération. Il faudrait vraiment que la feuille soit pliée pour passer entre les lamelles."
    think "Je l'aurais quand même entendue bouger si le courant d'air était assez fort pour l'emporter. Et puis, elle était à l'autre bout de la pièce."
    return

label _8_PNC_LIT:
    if pnc_flags.get("lit"):
        think "Je n'avais pas le dessin avec moi quand je suis revenu vers le lit."
        return

    $ pnc_flags["lit"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je m'assieds sur le lit, à peu près à la même place qu'hier matin."
    think "J'avais laissé la feuille sur le bureau avant de revenir chercher ma chaussette. Je me souviens que je l'ai retrouvée par terre et que j'ai dû me baisser pour la ramasser."
    "Je vérifie sous le lit une dernière fois, plus par habitude que parce que je m'attends à y trouver quelque chose."
    return

label _8_PNC_TELEVISION:
    if pnc_flags.get("television"):
        think "Kami n'a toujours pas rallumé l'écran."
        return

    $ pnc_flags["television"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    noam hesitation "Kami ? Si jamais tu m'entends, tu pourrais me dire si quelqu'un est venu dans ma chambre hier ?"
    "J'attends quelques secondes, sans vraiment savoir où regarder pour m'adresser à elle."
    noam fatigue "Ça m'arrangerait même si tu me répondais juste que t'en as rien à faire."
    "L'écran reste noir. J'aurais préféré ne pas avoir à lui demander quoi que ce soit, mais je commence à manquer d'idées."
    return

label _8_PNC_TIROIR:
    if pnc_flags.get("tiroir"):
        think "J'ai déjà vidé le tiroir et je sais à peu près quand je l'ai ouvert hier."
        return

    $ pnc_flags["tiroir"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je tire sur le tiroir qui coince. J'avais rangé ma chaussette dedans hier en rentrant, et c'est à ce moment-là que j'ai commencé à chercher la feuille."
    think "J'étais déjà inquiet de ne plus la voir. Je ne l'ai donc pas rangée ici en même temps que mes affaires."
    "Je referme le tiroir. Cette fois, je suis sûr de ce souvenir."
    return

label _8_PNC_ARMOIRE:
    if pnc_flags.get("armoire"):
        think "J'ai vérifié la veste et le reste de mes vêtements."
        return

    $ pnc_flags["armoire"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je décroche ma veste et l'enfile pour refaire les mêmes gestes qu'hier. J'avais déjà reposé la feuille sur le bureau quand je suis venu la prendre."
    "Je passe la main dans les poches. J'aurais dû plier le dessin pour le faire rentrer, et je ne me souviens absolument pas l'avoir fait."
    noam inquiet "Pourquoi je l'aurais emmené avec moi, de toute façon ?"
    return

label _8_PNC_SALLE_DE_BAIN:
    if pnc_flags.get("salle_de_bain"):
        think "J'ai déjà vérifié la salle de bain."
        return

    $ pnc_flags["salle_de_bain"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je jette un coup d'œil sous le lavabo et entre les serviettes. Hier matin, j'avais fini de me laver avant de regarder le dessin."
    think "Je n'aurais pas risqué de le mouiller. Je perds un peu mon temps ici."
    return

label _8_PNC_BROUILLEUR:
    if pnc_flags.get("brouilleur"):
        think "Le boîtier est toujours en place."
        return

    $ pnc_flags["brouilleur"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je regarde derrière le brouilleur. Le voyant est toujours allumé et je ne vois aucun papier coincé contre le mur."
    think "Même sans Kami, le brouilleur fonctionne encore. En tout cas, il a exactement le même aspect qu'avant."
    return

label _8_PNC_TABLETTE:
    if pnc_flags.get("tablette"):
        think "J'avais vu le dessin près de la lampe hier matin et j'avais ma tablette sur moi en sortant."
        return

    $ pnc_flags["tablette"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je pose ma tablette sur sa station d'accueil et me rappelle avoir fait la même chose hier. J'étais revenu vers le bureau pour la reprendre avant de sortir."
    think "J'avais parlé au dessin un peu plus tôt. Je l'avais même soulevé pour voir si ma chaussette était en dessous, mais je ne me souviens pas de l'avoir regardé au moment de partir."
    "Je note l'heure approximative à laquelle j'ai quitté la chambre. Je suis sûr d'avoir gardé ma tablette sur moi toute la journée. Je l'avais encore dans la main en rentrant."
    return
label _8_PNC_SORTIE:
    if not pnc_flags.get("porte"):
        $ pnc_flags["porte"] = True
        $ showGroup([("noam", "reflexion", 0.50)])
        "Je regarde la serrure. Les portes des chambres se verrouillent automatiquement dès qu'on les ferme. Depuis le couloir, il faut l'empreinte biométrique du résident ou sa tablette pour les ouvrir."
        think "Je me souviens d'avoir entendu le verrou hier en sortant. Et j'ai gardé ma tablette sur moi toute la journée. La porte était bien verrouillée."
        "Je vérifie la poignée et le lecteur. Rien ne paraît abîmé. Je note tout ça sur ma tablette."
        $ investigation_add("j8_porte_verrouillee")
    $ j8_required = ("lit", "tiroir", "armoire", "tablette")
    $ j8_remaining = sum(1 for key in j8_required if not pnc_flags.get(key))

    if j8_remaining:
        "Ma main se pose sur la poignée, mais je m'arrête avant d'ouvrir."
        if j8_remaining == 1:
            think "Il reste encore un endroit évident à vérifier. Je ne peux pas partir maintenant."
        else:
            think "Il reste encore [j8_remaining] endroits évidents à vérifier. Je ne peux pas partir maintenant."
        return

    return "j8_search_done"

# -------------------------------------------------------
# FIN DE RECHERCHE
# -------------------------------------------------------

label _8_FIN_RECHERCHE:
    $ investigation_add("dessin_juliette_disparu", notify=False)
    $ investigation_add("j8_porte_verrouillee", notify=False)
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je relis les notes que j'ai prises. J'ai bien vu le dessin hier matin, mais je ne suis pas capable de dire s'il était encore là quand j'ai quitté la chambre."
    noam fatigue "Bon, j'ai fait tout ce que je pouvais pour l'instant."
    "Il est déjà tard et j'ai faim. Je vais manger avant de décider à qui je pourrais demander de l'aide."
    menu:
        "Je laisse tout comme ça pour l'instant.":
            "Je photographie le bureau pour garder une trace de l'endroit où sont mes affaires."
            $ chambre_range = False
        "Je vais ranger un peu avant de sortir.":
            "Je range les vêtements que j'ai sortis et remets le tiroir en place. Je n'ai pas envie de retrouver la chambre dans cet état ce soir."
            $ chambre_range = True
    if j701_lysa_search_help:
        "Je termine le café que Lysa m'a apporté. Il est complètement froid."
    "Je récupère ma veste et ma tablette."
    $ hideGroup()
    "Je ferme la porte. Le verrou automatique s'enclenche comme hier. Je tire une fois sur la poignée pour vérifier."
    stop music fadeout 1.0
    jump _8_0_1_CAFETERIA


label _8_0_1_CAFETERIA:
    call START_EXPLORATION_LIBRE("_8_0_1_CAFETERIA_ARRIVEE", title="Rejoindre la cafétéria", destination_room="cafeteria") from _call_exploration__8_0_1_CAFETERIA


label _8_0_1_CAFETERIA_ARRIVEE:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_293
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.5
    $ showGroup([
        ("iris", "sourire"), ("julian", "decontracte"), ("lysa", "neutre"),
        ("noam", "fatigue"), ("elias", "detendu"), ("mara", "rire"),
        ("tomas", "fatigue"), ("elen", "sourire"), ("ryn", "neutre"), ("kael", "fatigue")
    ])

    julian sourire "Puisque personne n'a prévu de nous faire travailler aujourd'hui, j'ai proposé à Elen qu'on organise une petite fête ce soir. On a même décidé d'une règle : pendant la fête, personne ne prononce le nom de Kami."
    iris reflechit "Je n'ai pas accepté cette règle, moi."
    elen sourire "Il vient juste de me la proposer. Pour le repas, je pensais qu'on pourrait rapprocher les tables et sortir les vrais verres. Tomas, tu crois qu'il en reste dans la cuisine ?"
    tomas fatigue "Je peux vérifier après manger. J'en avais mis quelques-uns de côté parce qu'il y en a déjà deux de cassés."
    "Elen se lève avec son assiette pour mesurer l'espace entre les tables. Mara ramène sa chaise vers elle avant qu'Elen ait le temps de la toucher."
    mara neutre "Tu fais ça après que j'ai mangé. Il y a plein de chaises vides là-bas, je vois pas pourquoi il faut absolument que tu prennes la mienne."
    elen "Je voulais juste voir si on pouvait tous s'asseoir du même côté. Attends, Elias, tu peux pousser un peu celle de derrière ?"
    elias detendu "Oui, mais le pied est coincé sous la table."
    "Elias tire sur la chaise. Elen finit par soulever la table pendant que Mara continue de manger."
    julian decontracte "Je m'occuperai du programme. Ryn, je me suis dit que tu pourrais ouvrir la soirée en nous racontant quelque chose sur toi."
    ryn neutre "Je mangerai avec vous si tu me laisses tranquille. C'est déjà pas mal."
    noam taquin "Vous avez commencé à organiser ça à quelle heure ?"
    elen joie "Il y a dix minutes ! Il y a encore rien de prévu, mais viens t'asseoir, je te montrerai où on pensait mettre les tables."
    noam fatigue "Je vais déjà manger, sinon je vais finir par vous aider sans avoir touché à mon assiette."
    "Je m'installe près de Lysa. Elle décale son gobelet pour me faire de la place."
    if j701_lysa_search_help:
        lysa neutre "Alors, tu as avancé depuis que je suis partie ?"
        noam hesitation "Un peu. Je me souviens mieux de ce que j'ai fait hier matin, mais je sais toujours pas quand il a disparu. J'ai noté les heures sur ma tablette."
        lysa "On pourra revoir ça tous les deux, après. Là, mange un peu, je te vois hésiter depuis que tu t'es assis."
        noam "C'est surtout que j'ai pas envie d'en parler devant tout le monde."
        "Elle acquiesce et me passe le pain."
    else:
        lysa neutre "Tu as l'air crevé. T'as mal dormi ?"
        noam fatigue "J'ai passé une bonne partie de la nuit à chercher un truc dans ma chambre. J'ai recommencé ce matin, mais j'ai pas eu beaucoup plus de chance."
        lysa "Si tu veux un deuxième avis, je peux passer. Je te promets de ne pas ouvrir les tiroirs sans ton autorisation."
        if chambre_range:
            think "Heureusement que j'ai rangé un peu avant de sortir."
        noam hesitation "Merci, je te dirai si j'ai besoin. Pour l'instant, je voudrais essayer de comprendre tout seul."
        "Elle me laisse terminer mon repas sans poser d'autre question."
    elen sourire "On pourrait demander à chacun de préparer quelque chose. Pas forcément de la nourriture, même une activité. Elias, tu connais des jeux auxquels on peut jouer à douze ?"
    elias sourire "Il y en a un avec des bouts de papier. Chacun écrit des noms de personnages connus, on les mélange, et après il faut les faire deviner. Par contre, si on vient tous de districts différents, je sais pas si on aura les mêmes références."
    julian "On peut mettre nos propres noms. Je veux voir quelqu'un essayer de faire deviner Mara sans dire un mot."
    mara neutre "Et moi, je veux pouvoir finir mes œufs."
    "Elen essaie le jeu quand même. Elle mime quelque chose avec ses bras, puis attend qu'Elias devine. Il propose Goumi. Ce n'était manifestement pas ce qu'elle avait en tête."
    iris reflechit "Au fait, pourquoi attendre ce soir pour essayer de joindre Kami ? Kael, tu m'avais dit qu'il restait des commandes auxquelles le système répondait."
    kael reflechit "Oui, la station continue de recevoir les commandes habituelles. Mais ce sont des fonctions qui peuvent tourner sans elle. Je n'ai rien trouvé qui me permette de savoir si elle nous entend encore."
    iris "Je voudrais quand même essayer. Il y a des choses qu'on n'a pas testées, et je peux m'en occuper si tu n'as pas le temps."
    ryn desaccord "Faites ce que vous voulez, mais prévenez-nous avant de couper quelque chose. Hier, j'ai dû attendre dans le couloir pendant qu'on vérifiait le matériel."
    elias gene "J'y suis pour rien, hein. Je suis juste venu aider."
    if not j701_tomas_secret_kept:
        "Kael pose sa fourchette et se tourne vers Tomas."
        kael reflechit "J'ai commencé à regarder les relevés que tu m'as envoyés hier soir. Pour ce que j'ai pu vérifier, j'arrive au même résultat que toi. Je n'ai pas encore fini, il faudrait que je récupère le reste des données."
        tomas inquiet "Je comptais justement venir te voir après manger."
        iris reflechit "Vous parlez de quoi ? Si c'est lié à Kami, ça m'intéresse."
    else:
        "Tomas sort sa tablette et la garde un moment sur ses genoux."
        tomas inquiet "Kael, j'aurais besoin que tu regardes un truc avec moi aujourd'hui. J'ai refait les vérifications cette nuit et ce matin, mais je ne suis pas sûr de ce que je lis."
        noam hesitation "Tu as toujours les mêmes chiffres ?"
        tomas "Oui. J'aurais préféré qu'ils aient changé depuis hier."
        iris reflechit "Quels chiffres ?"
    "Tomas pose sa tablette sur la table et ouvre les relevés."
    tomas inquiet "J'ai regardé le nombre d'exécutions enregistrées dans les données auxquelles on a accès. Depuis le jour six, le total n'a pas changé, et c'est pareil sur les quatre flux. J'ai attendu de voir si ça se remettrait à jour, mais pour le moment, rien."
    elen surpris "Tu veux dire que Kami a arrêté de sanctionner les gens ?"
    tomas "Non, attends, j'en sais rien. Si les données ne nous parviennent plus, on aurait exactement le même résultat. Je voulais justement que Kael m'aide à faire la différence."
    iris "Montre-moi la dernière synchronisation. Tu as les données des jours précédents sur la même tablette ?"
    "Tomas fait défiler les relevés pendant qu'Iris se rapproche de lui. Elen essaie aussi de voir l'écran, mais Julian déplace son verre pour éviter qu'elle ne le renverse."
    mara agace "Ça fait depuis hier que tu as vu ça ? Et tu n'en as parlé à personne pendant le repas ?"
    if j701_tomas_secret_kept:
        tomas "J'en ai parlé à Noam. Je lui ai demandé de ne rien dire tant que je n'aurais pas refait les calculs, parce que je savais très bien ce qui allait se passer si je l'annonçais comme ça."
        noam hesitation "Il voulait d'abord être sûr de lui. Hier, on ne savait même pas si le compteur allait reprendre pendant la nuit."
    else:
        tomas "J'en ai parlé à Kael pour qu'il vérifie de son côté. Je ne savais pas quoi vous annoncer, et j'avais peur que certains en concluent que les Commandements ne fonctionnaient plus."
        noam "On s'était dit qu'on attendrait d'avoir une deuxième lecture avant d'en tirer quoi que ce soit."
    julian surpris "Tu aurais pu nous le présenter comme un problème de transmission, sans nous dire que les sanctions étaient terminées."
    tomas inquiet "Mais je viens de le faire, Julian ! Et la première question d'Elen, c'était justement de savoir si elles s'étaient arrêtées."
    elen inquiet "Excuse-moi, je voulais juste savoir. Si jamais des gens sur Terre ont remarqué la même chose que nous, ils peuvent croire qu'ils ont le droit de faire ce qu'ils veulent."
    iris reflechit "On ne sait même pas ce qu'ils voient, eux. Tomas, il manque plusieurs lignes dans tes données. Pour l'instant, je ne peux pas te dire si elles ont été supprimées ou si on ne les a jamais reçues."
    kael "Je vais essayer de récupérer les copies locales après manger. Ne comptez pas sur moi pour vous donner une réponse à une heure précise, par contre."
    ryn neutre "D'accord. Et en attendant, on continue de respecter les Commandements comme si rien n'avait changé. On ne va pas demander à quelqu'un de vérifier pour nous."
    mara neutre "Ça me paraît évident. Je voudrais surtout qu'on évite de raconter aux absents que les sanctions ont cessé, parce qu'après on va passer la journée à corriger ce qu'ils ont compris."
    "Tomas récupère sa tablette. Il n'a presque pas touché à son repas."
    menu:
        "Tomas a bien fait de vérifier avant de nous en parler.":
            noam neutre "Tomas a bien fait de vérifier avant de nous en parler. S'il nous avait dit ça hier soir, on aurait passé la nuit à se demander si c'était vrai."
            tomas gene "Merci. Je voulais pas vous cacher quelque chose d'important."
            mara "Je sais. J'aurais juste préféré qu'on soit au courant plus tôt, même si c'était incertain."
        "Kael, on peut vérifier ça sans prendre de risques ?":
            noam reflechit "Kael, on peut vérifier ça sans prendre de risques ? Avec les données qu'on a à bord, je veux dire. Pas en demandant à quelqu'un d'enfreindre une règle."
            kael "C'est ce que je vais essayer de déterminer. Il faut déjà que je voie ce qui a été conservé à bord."
            iris "Viens me chercher si tu veux de l'aide. Je vais arrêter de te demander toutes les cinq minutes où tu en es."
            kael "Merci, ça m'arrangerait."
    "Elen reprend les quelques objets qu'elle avait mis de côté pour la soirée."
    elen inquiet "Je les range ou vous voulez toujours qu'on fasse quelque chose ce soir ?"
    julian decontracte "Moi, je veux toujours. On n'est pas obligés de fêter l'absence de Kami, on peut juste passer la soirée ensemble."
    ryn "Tant que je ne dois pas faire de discours, ça me va."
    "Elen remet ses affaires sur la chaise. Julian lui tend un morceau de son dessert."
    elen sourire "Ah, tu me le rends enfin ! Tu sais que j'ai cherché celui d'hier pendant tout le repas ?"
    julian "Je l'ai mangé avant de comprendre qu'il était à toi. J'avais même demandé à Elias si quelqu'un l'avait laissé là."
    elias gene "Je t'avais répondu que je savais pas..."
    "Elen prend le dessert, puis demande à Julian de garder sa place pendant qu'elle va chercher une assiette."
    "J'aurais bien aimé parler du dessin à Lysa, mais je préfère attendre qu'on soit seuls."
    $ hideGroup()
    jump _8_0_1_TEMPS_LIBRE_1


label _8_0_1_TEMPS_LIBRE_1:
    call START_FREE_TIME("_8_0_1_APRES_MIDI_KAEL_CRISE", start_corridor="cafeteria") from _call_START_FREE_TIME_8_0_1


transform d8_kael_door_entry:
    xalign 1.12
    yalign 1.0
    alpha 0.0
    zoom 1.04
    easeout 0.55 xalign 0.50 alpha 1.0 zoom 1.0
    linear 0.08 xoffset -18
    linear 0.08 xoffset 0


label _8_0_1_APRES_MIDI_KAEL_CRISE:
    $ current_period = "Après-midi"
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_295
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_quiet_routine.mp3" fadein 1.5
    $ showGroup([
        ("lysa", "neutre", 0.15), ("ryn", "decontracte", 0.35),
        ("elias", "fatigue", 0.65), ("noam", "neutre", 0.85)
    ])
    ryn desaccord "Je maintiens que cette étagère était mal conçue. On a passé une demi-heure à essayer de faire rentrer les vis dans les trous et, quand Elias a posé sa boîte dessus, tout est parti d'un coup."
    lysa blase "Ryn, tu avais monté les deux côtés à l'envers. Je t'ai même montré le dessin de la notice avant que tu me dises que tu savais faire."
    ryn "J'ai cru que le dessin était vu de derrière ! Et arrêtez de raconter que j'ai détruit toute l'étagère, il y a seulement une planche qui est tombée."
    elias fatigue "Elle est tombée sur mon pied. J'ai passé dix minutes à essayer de défaire ce que tu avais vissé, et après tu m'as dit que je n'aurais pas dû toucher à la planche."
    "Ryn se penche pour regarder la chaussure d'Elias."
    ryn inquiet "Ça t'a vraiment fait mal ? T'aurais pu me le dire sur le coup, j'aurais enlevé la boîte."
    elias "Ça va mieux. Ce qui m'embête surtout, c'est qu'il nous manque des vis pour la remonter."
    lysa "Celles que Ryn a mises dans la boîte en carton, à côté de la poubelle ?"
    "Ryn cesse de manger."
    ryn desaccord "Attendez, me dites pas que quelqu'un a jeté cette boîte. Je l'avais gardée exprès pour les petites pièces."
    noam "Je l'ai vue quand je suis passé tout à l'heure. Elle était encore là, mais je ne sais pas si Goumi est venu depuis."
    "Elias se lève pour aller regarder. Ryn lui demande de rapporter la boîte entière, puis se ravise et lui demande de ne pas déplacer les affaires des autres."
    lysa taquin "Tu veux pas y aller toi-même ? Tu auras peut-être le temps de retrouver la notice en même temps."
    ryn "Je la lirai, ta notice. T'es contente ?"
    "Elias revient les mains vides. Ryn lui fait une place à côté de lui sans reparler des vis."
    elias inquiet "Au fait, vous avez vu Kael cet après-midi ? Je l'ai croisé devant les chambres. Je voulais lui demander un truc pour l'étagère, mais il m'a à peine regardé. Il a fait demi-tour deux fois pendant que j'étais là."
    lysa reflechit "Ça lui ressemble pas trop. Il était déjà fatigué ce matin, mais il avait surtout l'air préoccupé par les relevés de Tomas."
    noam neutre "Il t'a dit où il allait ?"
    elias "Non, il m'a juste dit que c'était pas le moment. J'ai préféré le laisser, il avait vraiment pas l'air de vouloir discuter."
    ryn reflechit "Il est peut-être encore en train de chercher les batteries."
    elias colere "Je vous en prie, arrêtez avec ces batteries. J'ai vérifié les livraisons et je ne les ai pas déplacées. Si on veut refaire le compte, je veux bien, mais je vais pas m'excuser chaque fois que quelqu'un cherche du matériel."
    "Je repense à la matinée que j'ai passée dans ma chambre."
    menu:
        "Je peux aller voir comment il va.":
            noam inquiet "Je peux aller voir comment il va. S'il tourne en rond depuis ce matin, il a peut-être besoin d'aide et il ose pas nous le demander."
            ryn neutre "Je viens avec toi. Je voulais justement lui parler."
        "On devrait peut-être le laisser tranquille un moment.":
            noam hesitation "On devrait peut-être le laisser tranquille un moment. J'ai pas envie qu'on débarque tous devant sa porte alors qu'il a juste besoin d'être seul."
            lysa reflechit "Oui, on peut lui demander quand il reviendra."
    play sound "audio/sfx_door.mp3" volume 1.0
    with hpunch
    $ showP("lysa", "choc", 0.12)
    $ showP("ryn", "inquiet", 0.28)
    $ showP("elias", "choc", 0.72)
    $ showP("noam", "inquiet", 0.88)
    show kael colere at d8_kael_door_entry zorder 2
    pause 0.75
    $ char_pos["kael"] = 0.50
    $ char_state["kael"] = dict(expr="colere", x=0.50, y=1.0, layer="master", zorder=2)
    $ group_members = ["lysa", "ryn", "kael", "elias", "noam"]

    kael colere "Est-ce que l'un de vous est entré dans ma chambre hier soir ou ce matin ? J'ai déjà demandé aux autres, personne ne sait me répondre."
    "Il s'arrête devant nous. Elias se redresse sur sa chaise."
    ryn inquiet "Non, je suis pas entré chez toi. Qu'est-ce qui se passe ?"
    kael reflechit "Elias, tu étais avec Nyra pour les livraisons hier. Tu n'as pas vu quelqu'un près de ma porte, même juste en passant ?"
    elias inquiet "Je me souviens d'avoir croisé des gens, mais je serais incapable de te dire devant quelle chambre. Je regardais surtout où je posais les caisses."
    "Kael commence à repartir. Je me lève avant qu'il atteigne la porte."
    noam inquiet "Attends, Kael. On pourra peut-être t'aider si tu nous dis ce que tu cherches."
    kael inquiet "C'est une photo. Je l'ai laissée sous mon oreiller hier soir, comme je le fais tous les soirs depuis que je suis arrivé. Quand j'ai voulu la reprendre ce matin, elle n'était plus là."
    lysa "Tu as regardé autour du lit ? Je peux venir t'aider à déplacer ce que tu n'as pas pu bouger tout seul."
    kael "J'ai déjà tout déplacé, Lysa. J'ai enlevé les draps, sorti le matelas, et j'ai même démonté une partie de la tête de lit parce que je pensais qu'elle avait pu glisser derrière."
    "Il attrape le dossier d'une chaise. Il a les doigts qui tremblent."
    kael inquiet "C'est la photo de Léa. Je ne l'ai pas prise avec moi en sortant, je ne la laisse jamais dans mes poches parce que j'ai peur de l'abîmer. Hier soir, je l'avais encore dans les mains juste avant de dormir."
    elias inquiet "Peut-être que quelqu'un l'a trouvée et l'a mise de côté sans savoir que c'était à toi. On pourrait demander à Goumi, ou..."
    kael colere "Trouvée où, Elias ? Dans mon lit ? Elle ne pouvait pas se retrouver ailleurs toute seule !"
    elias gene "Je sais pas, je voulais proposer quelque chose."
    ryn "On te croit quand tu dis qu'elle a disparu. Mais laisse-le finir, il essaye de t'aider."
    kael colere "Ça fait trois heures que j'entends les mêmes choses ! On me demande si j'ai vérifié mes poches, si j'ai regardé sous le lit, si j'ai pas confondu avec un autre jour. J'ai beau expliquer où je la range, personne ne m'écoute."
    lysa neutre "Je t'écoute. Tu veux retrouver ta photo, et on va essayer de t'aider. Assieds-toi un peu, tu es essoufflé."
    "Kael repousse la chaise sans s'asseoir."
    kael "Je ne veux pas m'asseoir, je veux qu'on me dise ce qui s'est passé dans ma chambre. Si quelqu'un y est entré, j'ai besoin de savoir qui c'est."
    noam inquiet "On n'a rien vu, Kael. On peut demander aux autres, mais là je peux pas te donner un nom."
    kael colere "Mais vous ne comprenez pas ! Je suis certain de l'avoir laissée là !"
    $ unlock_gallery_image("bg_cg050")
    scene bg_cg050 at adaptive_fullscreen with vpunch
    kael colere "Si quelqu'un ici l'a prise, qu'il me la rende ! Je m'en fiche de savoir pourquoi, je veux juste récupérer ma photo !"
    stop music fadeout 0.8
    play music "music/bgm_system_override.mp3" fadein 0.8
    # Rattrapage silencieux pour les sauvegardes antérieures à l'ajout des preuves.
    $ investigation_add("dessin_juliette_disparu", notify=False)
    $ investigation_add("j8_porte_verrouillee", notify=False)
    call refutation_run("j8_kael_confirmation") from _call_j801_play_stabilisation
    $ j801_stabilisation_result = (_return[0] == "success") if isinstance(_return, (tuple, list)) else bool(_return)
    jump _8_0_1_APRES_STABILISATION


label _8_0_1_APRES_STABILISATION:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5
    $ showGroup([
        ("lysa", "triste", 0.12), ("ryn", "inquiet", 0.28),
        ("kael", "effondre", 0.50), ("elias", "choc", 0.72),
        ("noam", "neutre", 0.88)
    ])
    if getattr(store, "j801_stabilisation_result", False):
        noam inquiet "Attends, Kael. Il m'est arrivé la même chose. Hier matin, j'avais encore le dessin que ma sœur m'a fait. Quand je suis rentré, il avait disparu. J'ai fouillé toute ma chambre, et j'ai noté ce que j'ai trouvé sur ma tablette."
        kael inquiet "Toi aussi ? Attends, tu veux dire que t'as cherché toute la matinée ?"
        noam "Oui. Je ne sais pas ce qui s'est passé, mais tu n'es pas le seul à avoir perdu quelque chose."
        "Kael regarde les notes que je lui montre. Il lâche enfin le dossier de la chaise."
    else:
        "J'essaie de lui expliquer ce que j'ai découvert, mais Kael me coupe avant que je puisse lui montrer mes notes."
        lysa neutre "Kael, attends. Laisse Noam finir, s'il te plaît."
        noam inquiet "Le dessin de ma sœur a disparu. Je l'avais hier matin, il n'était plus là quand je suis rentré. J'ai passé la matinée à le chercher."
        kael inquiet "Pourquoi tu l'as pas dit plus tôt ?"
        noam "Parce que je pensais l'avoir perdu. Maintenant que tu me parles de ta photo, je commence à en douter."
        "Je lui montre mes notes. Kael les lit sans rien dire."
    "Kael accepte finalement de s'asseoir. Lysa pose un verre d'eau devant lui et recule pour lui laisser un peu de place."
    elias inquiet "Désolé pour ce que j'ai dit tout à l'heure. Je voulais pas te donner l'impression que je te prenais pas au sérieux. J'ai juste pensé que quelqu'un avait pu la retrouver sans faire exprès."
    kael effondre "C'est pas contre toi. J'ai passé la matinée à chercher et j'en ai marre de ne rien trouver."
    "Elias tire une chaise vers lui, puis décide finalement de rester debout."
    ryn desaccord "Il doit bien y avoir un historique des accès aux chambres. Je peux demander à Goumi si on a moyen de le consulter sans passer par Kami."
    lysa "Essaie, oui. Mais tant qu'on ne l'a pas, on ne pourra pas savoir si quelqu'un est entré chez lui."
    "Kael rapproche le verre et regarde de nouveau mes notes."
    kael effondre "Ta porte était fermée quand t'es sorti ?"
    noam "Oui. Elle se verrouille automatiquement, comme les autres. Il faut mon empreinte ou ma tablette pour l'ouvrir de l'extérieur. Et j'avais ma tablette sur moi tout le temps."
    kael inquiet "Alors comment quelqu'un aurait pu entrer ?"
    noam "C'est ce que je comprends pas. Le verrou n'a pas l'air abîmé. Mais on sait pas encore si quelqu'un est réellement entré."
    kael inquiet "Moi, je l'avais avec moi hier soir. Je me rappelle même l'avoir remise sous l'oreiller quand j'ai éteint la lampe. C'est ça que je comprends pas."
    "Il prend une gorgée d'eau."
    ryn reflechit "Attendez, on a déjà du matériel qui manque depuis hier, et maintenant deux personnes ne retrouvent plus des affaires dans leurs chambres. Vous trouvez pas ça bizarre ?"
    lysa desaccord "Si, mais on n'a aucune raison de penser que les batteries ont disparu de la même manière que la photo. On peut vérifier ce qui manque sans décider tout de suite qu'une personne ici vole les affaires des autres."
    ryn "Je dis pas que c'est forcément la même personne. Je voudrais juste savoir si d'autres ont perdu quelque chose. Si c'est le cas, j'aimerais autant l'apprendre avant de rentrer chez moi ce soir."
    elias "Je peux ressortir les registres de livraison et refaire le compte. Pour les chambres, je sais pas comment on s'y prend, mais je peux au moins vérifier ça."
    $ investigation_add("photo_lea_disparue")
    call play_stat_dialogue("d8") from _call_stat_dialogue_d8
    kael triste "Faites comme vous voulez. Je vais retourner dans ma chambre, je n'ai même pas remis le matelas en place."
    noam inquiet "Je peux venir t'aider à le remettre si tu veux. Je toucherai pas au reste."
    kael "Merci, mais je préfère être seul un moment. Je suis désolé de vous avoir crié dessus."
    "Il finit son verre avant de repartir. Ryn se lève à son tour, mais Lysa lui demande d'attendre un peu."
    "Je reste avec eux. J'ai envie de retourner vérifier ma propre chambre, même si je sais très bien que je l'ai déjà fait ce matin."
    $ investigation_add("materiel_technique_manquant", notify=False)
    $ investigation_add("cafe_renverse", notify=False)
    $ investigation_add("livraison_j7", notify=False)
    $ investigation_add("kami_hors_ligne", notify=False)

    $ hideGroup()
    stop music fadeout 2.0
    scene black with fade
    jump _8_0_1_SOIREE


label _8_0_1_SOIREE:
    $ current_period = "Soir"
    call MAYBE_PLAY_SCRIPTED_DOOR("chambre", "bg_chambre") from _call_MAYBE_PLAY_SCRIPTED_DOOR_299
    scene bg_chambre at adaptive_fullscreen with dissolve
    play music "music/bgm_calm_not_peace.mp3" fadein 3.0
    $ showGroup([("noam", "inquiet", 0.50)])
    "De retour dans ma chambre, je rouvre les notes de ce matin et j'ajoute ce que Kael nous a raconté. Je précise qu'il avait encore la photo hier soir, alors que je n'ai pas vu mon dessin depuis hier matin."
    think "Il faudrait savoir si d'autres personnes sont dans le même cas. J'espère que Kael a réussi à se reposer un peu depuis tout à l'heure."
    "Je vérifie le verrou de la porte. Je ne vois rien d'abîmé autour de la poignée, mais je ne sais pas vraiment ce qu'il faudrait chercher."
    if j701_lysa_search_help:
        "Ma tablette vibre. Lysa m'a écrit : « On pourra reprendre les recherches demain. Pour ce soir, essaie de dormir, d'accord ? »"
        "Je lui réponds : « Oui, merci pour ce matin. Tu me diras si tu as des nouvelles de Kael. »"
        "Elle me répond qu'elle passera le voir demain s'il ne vient pas déjeuner."
    else:
        "J'ouvre la conversation avec Lysa. Je lui ai dit ce midi que je lui demanderais de l'aide si je n'arrivais pas à m'en sortir, mais il est tard et je ne sais pas si elle est encore réveillée. Je lui parlerai demain."
    "Je tire une dernière fois sur la poignée sans actionner l'ouverture. Le verrou est bien engagé. Je laisse ma tablette sur la table de chevet."
    "Je me glisse sous les draps et tends la main pour éteindre la lampe. L'espace à côté du pied de la lampe est toujours vide."
    "Je laisse ma tablette à portée de main et essaie de dormir."
    $ hideGroup()
    call end_day("9", sleeping=True) from _call_end_day_12
    jump _9_0_1_REVEIL_CHAMBRE
