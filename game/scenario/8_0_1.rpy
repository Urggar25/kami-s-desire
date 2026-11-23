# --------------------------------------------------------------------------------------------
# JOUR 8 — Reconstitution de la disparition du dessin et crise de Kael
# Continuité : assistance de Lysa et divulgation du relevé de Tomas au J7.
# Scène PnC : Noam reconstitue ses derniers souvenirs plutôt que de refaire la fouille.
# La crise de Kael révèle un autre objet intime disparu sans conclure à un coupable.
# --------------------------------------------------------------------------------------------

label _8_1_0_0_CANON:
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

    think "..."
    think "Pas d'annonce."
    "Je reste allongé quelques secondes, l'oreille tendue, à attendre une voix qui m'aurait fait bondir du lit une semaine plus tôt."
    think "Deuxième matin de silence. Et moi qui écoute le plafond comme un idiot."
    "Je vais pour attraper ma tablette, puis j'aperçois l'espace vide sur le bureau."
    think "Le dessin."
    "Hier soir, j'ai déjà retourné cette chambre. Je pourrais recommencer, mais je retrouverais surtout la même poussière."
    "Je me redresse et essaie de remettre les choses dans l'ordre : le bureau, ma veste, la tablette que j'ai prise deux fois."
    scene bg_chambre at adaptive_fullscreen with dissolve
    noam inquiet "Je l'avais encore hier matin. Ça, j'en suis sûr."
    "Je revois Juliette penchée sur son dessin, la langue sortie pendant qu'elle essayait de réparer mon nez."
    think "Elle y avait passé des semaines. Je lui avais dit que si elle n'y arrivait pas, c'était peut-être à cause du modèle."
    "Elle avait ri, puis m'avait interdit d'y toucher avant d'avoir signé."
    "Je cherche mon dernier souvenir précis de la feuille. Pas un endroit où elle pourrait être, cette fois. Un moment où je l'ai réellement eue dans les mains."
    if j701_lysa_search_help:
        play sound sfx_knock
        lysa "Noam ?"
        noam surpris "Déjà ?"
        lysa "Tu m'as demandé de venir ce matin. C'était une suggestion ?"
        "J'ouvre. Lysa tient deux gobelets. Elle m'en tend un, puis inspecte le désordre par-dessus mon épaule."
        lysa "Ah, oui. Tu n'exagérais pas."
        noam fatigue "Je t'avais dit de ne pas te moquer."
        lysa "Tu ne m'as absolument pas dit ça."
        noam "C'est vrai."
        lysa "Alors. Qu'est-ce qui manque ?"
        noam hesitation "Un dessin. Ma petite sœur l'a fait avant mon départ."
        lysa "D'accord."
        noam "Tu vas me dire que c'est juste une feuille ?"
        lysa "Non. Tu vas me dire où tu l'as vue pour la dernière fois."
        "Je lui montre le bureau. Elle regarde sans toucher aux objets."
        lysa "Tu veux que je fouille à ta place ?"
        noam "Non. Je crois que je dois surtout me souvenir."
        lysa "Ça, je ne peux pas le faire pour toi."
        "Son gobelet à la main, elle reste un moment à côté de la porte."
        lysa "Je dois passer voir Elen. Si tu bloques, viens me trouver. Et ne jette rien."
        noam "Je n'allais rien jeter."
        lysa "Tu as mis une chaussette sur la tablette."
        "Je la retire. Lysa sort sans ajouter un mot."
    else:
        "Je prends ma tablette. J'hésite devant la messagerie de Lysa, puis la referme."
        think "Je pourrais demander de l'aide. Mais pour l'instant, je voudrais comprendre moi-même."
    tuto "(Examine les objets pour reconstituer les derniers moments où tu as vu le dessin.)"
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

    $ j8_required = ("lit", "tiroir", "armoire", "tablette")
    $ j8_search_count = sum(1 for key in j8_required if pnc_flags.get(key))

    frame:
        xalign 0.5
        yalign 0.035
        padding (24, 12)
        background Solid("#071019D9")

        vbox:
            spacing 2
            text "RECONSTITUER LA MATINÉE D'HIER" xalign 0.5 size 22 color "#D6E8F0"
            text "Souvenirs examinés : [j8_search_count] / 4" xalign 0.5 size 16 color "#7FCFEA"

# -------------------------------------------------------
# LABELS PnC
# -------------------------------------------------------

label _8_PNC_BOUCLE:
    $ hideGroup()
    call screen pnc_chambre_j8()
    $ j8_selected_interaction = _return
    call expression j8_selected_interaction from _call_expression_5
    jump _8_PNC_BOUCLE

label _8_PNC_AERATION:
    if pnc_flags.get("aeration"):
        think "J'ai déjà vérifié les lamelles. Une feuille n'aurait pas pu passer sans être déchirée."
        return

    $ pnc_flags["aeration"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je passe les doigts le long de la bouche d'aération, puis j'écarte prudemment deux lamelles."
    "Le souffle froid soulève la poussière accumulée derrière la grille. Aucun morceau de papier, seulement l'obscurité du conduit."
    think "Je ne sais même pas pourquoi je vérifie un conduit. Si Juliette me voyait, elle demanderait si je compte fouiller jusqu'à la Terre."
    return

label _8_PNC_LIT:
    if pnc_flags.get("lit"):
        think "J'ai déjà retourné le lit. Il ne reste rien à vérifier de ce côté."
        return

    $ pnc_flags["lit"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "La couverture est encore de travers. Je la remonte et m'assieds au bord du lit."
    think "Hier matin, après avoir parlé au dessin, j'ai cherché une chaussette. Je ne me suis pas approché du lit avec la feuille."
    "Je me relève, un peu déçu de ne pas pouvoir accuser mon propre désordre."
    noam fatigue "Bon. Ça élimine au moins un moment."
    return

label _8_PNC_TELEVISION:
    if pnc_flags.get("television"):
        think "L'écran est toujours noir. Rien n'est coincé autour du cadre."
        return

    $ pnc_flags["television"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "L'écran mural reste entièrement noir. Je vérifie malgré moi le rebord inférieur et l'espace étroit entre le cadre et le mur."
    noam taquin "Et alors ? Tu peux bien m'aider une fois, non ?"
    "Un voyant clignote dans le reflet de l'écran. Je me retourne d'un coup."
    "Ce n'est que ma tablette qui termine sa recharge."
    noam fatigue "Génial. Maintenant, même une batterie me fait sursauter."
    noam taquin "T'avais pas besoin d'en rajouter, toi."
    "Le reflet du plafond reste immobile dans l'écran. Je me sens idiot de lui avoir parlé."
    think "Au moins, elle ne pourra pas raconter ça aux autres."
    return

label _8_PNC_TIROIR:
    if pnc_flags.get("tiroir"):
        think "Le tiroir est vide. Je l'ai même retiré de ses rails."
        return

    $ pnc_flags["tiroir"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Le tiroir coince toujours au même endroit. Je me souviens l'avoir ouvert hier pour y mettre ma chaussette."
    "Le dessin était déjà introuvable à ce moment-là. Je passe un doigt sur le rebord et m'arrête."
    noam reflechit "Alors pourquoi je reviens toujours là ?"
    "Je referme doucement. Au moins, je sais que le souvenir de l'avoir rangé ici n'en est pas un."
    return

label _8_PNC_ARMOIRE:
    if pnc_flags.get("armoire"):
        think "J'ai fouillé chaque poche et chaque étagère de l'armoire. Rien."
        return

    $ pnc_flags["armoire"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Ma veste pend sur la porte. Hier matin, je l'ai prise après avoir remis le dessin sur le bureau."
    "Je ferme les yeux pour revoir le geste. Ma main sur le papier. La veste. Puis la tablette."
    "Je voudrais retrouver le moment où j'ai glissé la feuille ailleurs. Il ne vient pas."
    noam inquiet "Et si j'avais simplement oublié ?"
    "Je ne touche pas aux vêtements. Ils ne m'apprendront rien de plus."
    return

label _8_PNC_SALLE_DE_BAIN:
    if pnc_flags.get("salle_de_bain"):
        think "La salle de bain est trop petite pour cacher quoi que ce soit d'autre."
        return

    $ pnc_flags["salle_de_bain"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "Je pousse la porte de la salle de bain et vérifie le meuble sous le lavabo, le panier à linge et même l'arrière des serviettes."
    "L'humidité aurait gondolé le papier. Tout est sec, parfaitement rangé et vide."
    think "Je n'aurais jamais apporté le dessin ici."
    "Mais je vérifie quand même la même serviette deux fois."
    return

label _8_PNC_BROUILLEUR:
    if pnc_flags.get("brouilleur"):
        think "Le boîtier du brouilleur est fermé. Le dessin n'est pas derrière."
        return

    $ pnc_flags["brouilleur"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je longe le boîtier du brouilleur du bout des doigts et regarde entre l'appareil et le mur."
    "Aucun papier n'y est coincé. La diode pulse avec une régularité presque organique."
    think "Le boîtier continue de pulser. Kami est muette, mais ça, au moins, semble toujours fonctionner."
    noam reflechit "Ce serait bien que le reste du monde soit aussi simple à vérifier."
    return

label _8_PNC_TABLETTE:
    if pnc_flags.get("tablette"):
        think "J'ai déjà déplacé la tablette et vérifié toute la table. Le dessin n'y est plus."
        return

    $ pnc_flags["tablette"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "La tablette est posée sur sa station d'accueil. Hier matin, je l'ai prise, reposée, puis reprise avant de sortir."
    "Le dessin était à côté de la lampe quand je l'ai soulevé pour retrouver ma chaussette. Je me rappelle même lui avoir parlé."
    "Mais je ne l'ai pas regardé une seconde fois avant de fermer la porte."
    think "Je peux dire où je l'ai laissé. Je ne peux pas dire à quel moment il a disparu."
    "Je prends une note de l'heure approximative de mon départ, puis vérifie qu'elle s'est bien enregistrée."
    return

label _8_PNC_SORTIE:
    $ j8_required = ("lit", "tiroir", "armoire", "tablette")
    $ j8_remaining = sum(1 for key in j8_required if not pnc_flags.get(key))

    if j8_remaining:
        "Ma main se pose sur la poignée, mais je m'arrête avant d'ouvrir."
        if j8_remaining == 1:
            think "Il reste encore un endroit évident à vérifier. Je ne peux pas partir maintenant."
        else:
            think "Il reste encore [j8_remaining] endroits évidents à vérifier. Je ne peux pas partir maintenant."
        return

    jump _8_FIN_RECHERCHE

# -------------------------------------------------------
# FIN DE RECHERCHE
# -------------------------------------------------------

label _8_FIN_RECHERCHE:
    scene bg_chambre at adaptive_fullscreen with dissolve
    $ showGroup([("noam", "inquiet", 0.50)])
    "Je reste au milieu de la chambre, la tablette à la main."
    "Je me souviens du dessin sur le bureau hier matin. Je me souviens de la veste. Je me souviens de ma sortie."
    "Entre les deux, il y a juste un trou. Pas une preuve. Pas même une bonne idée."
    noam fatigue "Bon... je n'apprendrai rien en regardant le même tiroir."
    "Je note les derniers gestes dont je suis certain. Si je demande de l'aide, au moins je pourrai expliquer ce que j'ai déjà vérifié."
    "Mon estomac gargouille. Je n'ai même pas pris de petit-déjeuner."
    menu:
        "Laisser la chambre telle quelle pour conserver mes repères.":
            "Je prends une photo du bureau avant de sortir."
            $ chambre_range = False
        "Remettre les affaires en place avant de sortir.":
            "Je remets les quelques vêtements déplacés sur leur étagère et replace le tiroir."
            $ chambre_range = True
    if j701_lysa_search_help:
        "Je prends le gobelet que Lysa m'a laissé. Le café est froid, mais je le bois quand même."
    "Je récupère ma veste. Je n'ai pas résolu grand-chose, mais je sais maintenant ce que j'ignore."
    $ hideGroup()
    "Je ferme ma porte. Par réflexe, je vérifie qu'elle est bien verrouillée."
    "Je n'ai aucune raison de le faire deux fois. Je le fais quand même."
    stop music fadeout 1.0
    jump _8_0_1_CAFETERIA


label _8_0_1_CAFETERIA:
    call KD_ROUTE_J8_JULIAN from _call_optional_kd_route_j8_julian
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

    julian sourire "Je déclare cette journée fériée."
    elen surpris "Tu peux faire ça ?"
    julian "Bien sûr. Je viens de le faire."
    lysa blase "C'est donc ça, le fonctionnement des institutions."
    julian taquin "La Fête du Grand Silence. Interdiction de prononcer le nom de Kami jusqu'à ce soir."
    iris reflechit "Tu viens de le prononcer."
    julian "Pour annoncer l'interdiction. C'est une exception."
    elen joie "Moi, je veux bien une fête. On pourrait manger tous ensemble ce soir."
    mara neutre "On mange déjà tous ensemble."
    elen "Alors on pourrait mettre les tables autrement."
    mara "Révolutionnaire."
    elias sourire "Il reste peut-être des décorations dans les caisses."
    elen "Vraiment ?"
    elias gene "Je disais ça comme ça."
    elen "Ah."
    "Elle se tourne vers Tomas."
    elen "Tu peux nous prêter des verres ? Les vrais, pas ceux qui se plient."
    tomas fatigue "Je peux regarder. Je croyais qu'on avait tout distribué."
    julian "Il faut aussi un responsable des cérémonies."
    ryn "Non."
    julian "Je n'ai même pas dit qui."
    ryn "Je préfère prendre de l'avance."
    "Personne ne réagit à sa plaisanterie. Ryn finit tranquillement son pain."
    noam taquin "Je suis arrivé à la réunion de préparation ?"
    elen "Oui ! Tu nous aides à déplacer les tables ?"
    noam "J'étais venu déjeuner."
    elen "Tu peux dire non."
    "Je pose mon plateau, puis je regarde les tables qui ont déjà été déplacées."
    noam "Je crois qu'il est trop tard."
    "Julian se lève et propose une disposition en cercle. Elen veut garder un passage pour Goumi. Mara refuse de déplacer sa chaise."
    mara "Je suis bien ici."
    julian "On ne peut pas faire une fête sans un minimum d'effort collectif."
    mara "Tu peux commencer par me laisser manger."
    "Elen contourne la chaise et continue à discuter de la décoration avec Elias. Julian reste debout avec son plan imaginaire."
    "Je pose mon plateau à côté de Lysa. Le café est chaud, les rires aussi. J'aurais aimé ne pas avoir passé toute la matinée à retourner ma chambre."
    lysa neutre "Tu as l'air d'avoir perdu un combat contre un placard."
    noam fatigue "J'ai cherché un truc. Rien de grave."
    lysa taquin "Laisse-moi deviner. Une deuxième chaussette ?"
    noam desaccord "Je t'interdis de parler de mes chaussettes."
    lysa sourire "Je me sens immédiatement plus libre."
    if j701_lysa_search_help:
        lysa neutre "Tu as réussi à te souvenir de quelque chose ?"
        noam hesitation "De l'heure où je l'ai posé, à peu près. Pas de ce qui lui est arrivé."
        lysa "On regardera à nouveau après manger, si tu veux."
        noam "Tu as déjà passé la matinée à m'aider."
        lysa "J'ai surtout bu ton café."
        "Elle me pousse un morceau de pain. Je le prends."
    else:
        lysa reflechit "Tu veux que je t'aide à chercher ?"
        if chambre_range:
            think "J'ai remis un peu d'ordre. Elle pourrait y entrer sans escalader mes affaires."
        noam hesitation "Merci. Je te dirai si je bloque vraiment."
        lysa neutre "Comme tu veux."
        "Elle ne me demande pas ce que j'ai perdu. Ça m'arrange pour le moment."
    elen sourire "J'ai une idée. Chacun pourrait préparer quelque chose pour ce soir."
    mara "Je prépare mon absence."
    elen "Mara !"
    mara "Quoi ? C'est quelque chose."
    julian "Je peux faire un discours."
    elen "On a dit quelque chose d'agréable."
    julian "Vous êtes terribles."
    elias rire "Si tu parles assez longtemps, Kami va peut-être revenir juste pour te couper."
    "Iris, qui découpait son repas en petits morceaux, relève la tête."
    iris reflechit "Tu sais qu'on pourrait essayer de lui parler autrement ?"
    elias gene "C'était une blague."
    iris "Oui, je sais. Mais le système reçoit toujours certaines commandes."
    kael reflechit "Les fonctions de la station répondent. Ça ne nous dit pas où sont passées ses réponses à elle."
    iris "Donc il faut faire des tests."
    ryn desaccord "Ou on peut manger avant que quelqu'un démonte une autre console."
    elias "C'est pas moi qui..."
    ryn "J'ai nommé personne."
    "Elias lui lance un regard et s'attaque à son pain."
    if not j701_tomas_secret_kept:
        "Kael pose sa fourchette et regarde Tomas."
        kael reflechit "J'ai reçu tes relevés hier soir. La série s'arrête bien au même endroit."
        tomas inquiet "Tu as regardé ?"
        kael "Pas tout. J'ai dormi avant de terminer."
        noam "Tu as bien fait."
        tomas "Je voulais t'en parler après le repas."
        iris "Quels relevés ?"
        "Tomas fixe l'écran de sa tablette. Il n'a plus vraiment le choix : Iris attend une réponse."
    else:
        "Tomas commence à répondre, puis se ravise. Je vois qu'il vérifie quelque chose sous la table."
        iris "Tomas ? Tu fais quoi ?"
        tomas inquiet "Je... j'ai regardé un compteur cette nuit."
        noam hesitation "On s'était dit qu'on revérifierait ce matin."
        tomas "Je l'ai fait. Deux fois. Je voulais en parler à Kael d'abord."
        kael "De quoi ?"
        "Tomas pose sa tablette à plat, mais garde une main dessus."
    tomas inquiet "Les exécutions enregistrées. Le total n'a pas bougé depuis le jour six."
    elen surpris "Attends. Quel total ?"
    tomas "Celui des sanctions. Sur les quatre flux."
    "Elen regarde Iris. Iris, elle, tend déjà la main vers la tablette."
    tomas "Doucement. Je ne sais pas si ça veut dire que les sanctions sont arrêtées ou juste que les données n'arrivent plus."
    iris reflechit "Fais voir la date de la dernière synchronisation."
    tomas "J'ai essayé. Il manque des lignes."
    mara agace "Tu savais ça depuis hier ?"
    if j701_tomas_secret_kept:
        tomas "Je voulais pas l'annoncer sans vérifier. Noam le sait."
        noam hesitation "Il m'a demandé de ne pas lancer une rumeur."
    else:
        tomas "J'ai demandé à Kael de vérifier. Je ne voulais pas que tout le monde s'emballe."
        noam "On avait convenu d'attendre d'avoir une deuxième lecture."
    julian surpris "Et maintenant, on en parle devant tout le monde."
    tomas "Parce qu'Iris cherche une explication ! Et parce que j'ai pas de meilleure réponse."
    "Il s'interrompt, gêné d'avoir élevé la voix."
    iris "Si le lien avec la Terre est coupé, ces chiffres ne prouvent rien. Il faut vérifier à la source."
    ryn "Donc personne ne sait."
    iris "Pas encore."
    elen inquiet "Et si des gens croient que c'est fini, alors que non ?"
    tomas fatigue "Voilà pourquoi je ne voulais pas en parler à tout le monde."
    "Julian repose le verre qu'il avait levé pour annoncer sa fête."
    mara neutre "On ferait peut-être mieux de garder ça entre nous jusqu'à ce que Kael ait fini."
    kael "Je peux essayer. Mais pas vous promettre une réponse aujourd'hui."
    "Elen ramasse les décorations improvisées qu'elle avait déjà posées sur une chaise."
    elen "Je peux les laisser là ?"
    ryn "Pourquoi tu les rangerais ?"
    elen "Je sais pas. Ça fait bizarre, maintenant."
    "Elle repose les décorations. Personne ne lui dit quoi faire."

    menu:
        "Soutenir Tomas devant le groupe.":
            noam neutre "Il n'a pas dit que les Commandements avaient disparu. Il nous montre ce qu'il a trouvé."
            tomas gene "Merci. C'est tout ce que j'essaie de faire."
            mara "Personne n'a dit le contraire."
            lysa "Tu viens de lui demander pourquoi il avait gardé ça pour lui."
            mara "Je voulais savoir."
        "Demander comment vérifier sans mettre quelqu'un en danger.":
            noam reflechit "On peut comparer les journaux techniques, non ? Sans que personne ait à tester les règles."
            kael "Oui, si j'arrive à récupérer les copies locales."
            iris "Je veux bien t'aider."
            kael "Pas maintenant. Laisse-moi d'abord voir ce qui est accessible."
            iris fatigue "D'accord."
    "Julian se penche vers Elen."
    julian "Tu crois qu'on peut quand même garder l'idée de la fête ?"
    elen "Oui. Mais peut-être sans discours sur la victoire de qui que ce soit."
    julian "C'est vexant, mais je peux essayer."
    lysa reflechit "On sait seulement qu'elle n'a donné aucun ordre depuis deux jours."
    mara neutre "Et que ça ne nous dit pas ce qu'elle prépare."
    "Julian regarde son dessert, le découpe en deux et pousse discrètement la plus grande moitié vers Elen."
    elen surpris "C'est pour moi ?"
    julian decontracte "Considère ça comme une réparation diplomatique après le gâteau d'hier."
    elen sourire "Je n'avais pas oublié !"
    julian taquin "Je sais. C'est bien ce qui m'inquiétait."
    "Elen glisse le morceau de dessert dans sa poche avant de se souvenir qu'elle porte une veste claire."
    elen "Oh non..."
    julian "Tu vois ? Une fête est nécessaire. Tu es visiblement à bout."
    "Elle lui donne un coup de coude. Ryn reprend la conversation sur les tables à déplacer comme s'il n'avait rien entendu."
    "Je regarde Lysa. Je pourrais lui reparler du dessin maintenant. Mais avec tous les autres autour, je n'en ai pas envie."
    $ hideGroup()
    jump _8_0_1_TEMPS_LIBRE_1


label _8_0_1_TEMPS_LIBRE_1:
    call MAYBE_PLAY_SCRIPTED_DOOR("couloir", "couloir_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_294
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    menu:
        "Discuter un instant avec Julian.":
            call KD_EXTRA_J8_JULIAN from _call_kd_extra_j8_julian
        "Passer directement au temps libre.":
            pass
    call START_FREE_TIME("_8_0_1_APRES_MIDI_KAEL_CRISE") from _call_START_FREE_TIME_8_0_1


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
    ryn desaccord "J'ai jamais dit que c'était facile."
    lysa blase "Non, tu as seulement dit que tout le monde devrait savoir le faire."
    elias fatigue "Vous vous disputez sur quoi, encore ?"
    ryn colere "Sur le fait que monter une étagère sans instructions, ça devrait pas demander trois personnes !"
    lysa taquin "Il a monté les deux côtés à l'envers."
    ryn colere "ÇA TENAIT !"
    noam sourire "Combien de temps ?"
    ryn "C'est pas la question."
    elias rire "Elle s'est effondrée après que j'ai posé une seule boîte dessus."
    ryn desaccord "Une boîte qui pesait le poids d'un moteur !"
    lysa "C'était une boîte de filtres."
    ryn "Des filtres lourds."
    elias "J'avais proposé de lire le mode d'emploi."
    ryn "On n'avait pas besoin du mode d'emploi."
    noam "L'étagère n'est pas d'accord."
    ryn "Vous avez fini ?"
    lysa "Presque. Où sont les vis qui restaient ?"
    "Ryn regarde son assiette."
    elias "Tu les as jetées ?"
    ryn "J'ai rangé ce qui traînait."
    lysa "Dans la poubelle."
    ryn "Dans une boîte qui était à côté de la poubelle."
    "Elias se lève pour aller vérifier. Ryn tente de le retenir, puis se ravise."
    ryn desaccord "Bon, d'accord. On recommencera."
    lysa "Avec le mode d'emploi."
    ryn "On verra."
    "Il prend une gorgée d'eau. Personne n'ajoute rien."
    "Elias revient sans les vis. Il regarde sa tablette, puis autour de la salle."
    elias inquiet "Au fait, quelqu'un a vu Kael depuis midi ?"
    lysa reflechit "Pas moi. Pourquoi ?"
    noam neutre "Il travaille peut-être."
    elias inquiet "Je l'ai croisé devant les chambres. Il allait dans un sens, puis dans l'autre. Je lui ai demandé s'il voulait de l'aide."
    ryn inquiet "Il t'a répondu ?"
    elias fatigue "« Pas maintenant ». Et je crois qu'il ne savait même pas que c'était moi."
    lysa neutre "Kael n'est pas du genre à se perdre dans un couloir."
    ryn reflechit "Peut-être qu'il cherche ce qu'Elias a perdu hier."
    elias colere "JE N'AI PAS PERDU LES BATTERIES !"
    lysa blase "Tu vas le graver sur ta tombe, celle-là."
    "Je souris, mais l'image de ma chambre me revient."
    menu:
        "Proposer d'aller chercher Kael.":
            noam inquiet "On devrait peut-être aller le voir. On est tous assez nerveux comme ça."
            ryn neutre "J'allais le proposer."
        "Lui laisser du temps.":
            noam hesitation "Si quelque chose ne va pas, il viendra nous parler. On devrait peut-être le laisser respirer."
            lysa reflechit "Peut-être..."
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

    kael colere "J'ai une question."
    "Il s'arrête devant la table. Personne ne répond tout de suite."
    kael "Est-ce que quelqu'un est entré dans ma chambre ?"
    elias inquiet "Pourquoi ?"
    kael "Je vous demande juste si quelqu'un y est allé."
    ryn "Pas moi."
    lysa "Kael, qu'est-ce qui se passe ?"
    "Kael passe une main sur son visage. Quand il la retire, il regarde Elias."
    kael reflechit "Tu as aidé Nyra avec les livraisons hier ?"
    elias "Oui, mais je n'ai pas..."
    kael "Tu as vu quelqu'un près des chambres ?"
    elias inquiet "Je sais plus. Je n'ai pas fait attention."
    kael "D'accord."
    "Il se dirige vers la sortie, puis revient à la même place."
    noam inquiet "Attends. Qu'est-ce qui manque ?"
    kael inquiet "Une photo."
    ryn "Tu l'as peut-être déplacée."
    kael "Non."
    ryn "Je demande."
    kael "Et moi je te réponds."
    "Il s'appuie sur une chaise sans s'asseoir. Sa main glisse sur le dossier."
    lysa "Tu l'as vue pour la dernière fois quand ?"
    kael "Hier soir. Avant de dormir."
    lysa "D'accord. Elle était où ?"
    kael "Sous l'oreiller. Je la remets toujours là."
    elias inquiet "Elle a pu tomber pendant la nuit."
    kael "J'ai retiré les draps."
    elias "Ah."
    kael "J'ai sorti le matelas. J'ai regardé derrière le lit. J'ai même démonté la tête de lit."
    "Il essaie de reprendre son souffle."
    kael "Je ne comprends pas."
    noam "Tu veux qu'on vienne regarder avec toi ?"
    kael "Vous n'allez pas la trouver en dix minutes si je n'ai rien trouvé en trois heures."
    "Personne ne répond. Kael nous regarde un à un."
    kael "C'est Léa. La photo de Léa."
    lysa "On a compris."
    kael "Non. Vous ne comprenez pas."
    "Sa voix monte d'un ton. Il s'en rend compte et se force à parler moins fort."
    kael "Je l'avais depuis mon départ. Je ne l'ai jamais posée ailleurs. Même quand je changeais les draps, je..."
    "Il serre les dents. Elias s'avance d'un pas."
    elias "Je voulais juste..."
    kael colere "Ne me demande pas encore si je l'ai déplacée !"
    elias "Je n'allais pas dire ça."
    kael "Alors quoi ?"
    elias "Rien. Pardon."
    "Kael baisse la tête. Ses mains tremblent, mais il continue à fixer Elias."
    ryn inquiet "Hé. On va chercher. Personne ne t'accuse de mentir."
    kael "Alors pourquoi vous me répétez tous que j'ai dû l'égarer ?"
    ryn "Parce qu'on ne sait pas ce qui s'est passé !"
    kael colere "MOI NON PLUS !"
    "Ryn recule d'un pas. Lysa s'interpose sans toucher Kael."
    lysa "Kael. Regarde-moi. Tu peux t'asseoir."
    kael "Non. Pas avant qu'on me dise qui..."
    "Il s'interrompt. Il regarde la porte, puis nos visages."
    kael inquiet "Quelqu'un savait où elle était."
    noam "On n'en sait rien."
    kael colere "JE LA METTAIS TOUJOURS AU MÊME ENDROIT !"
    $ unlock_gallery_image("bg_cg050")
    scene bg_cg050 at adaptive_fullscreen with vpunch
    kael colere "Alors que celui qui l'a prise vienne me le dire !"
    stop music fadeout 0.8
    play music "music/bgm_system_override.mp3" fadein 0.8
    call j801_play_stabilisation from _call_j801_play_stabilisation
    $ j801_stabilisation_result = _return
    jump _8_0_1_APRES_STABILISATION


label _8_0_1_APRES_STABILISATION:
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    play music "music/bgm_system_override.mp3" fadein 2.5
    $ showGroup([
        ("lysa", "triste", 0.12), ("ryn", "inquiet", 0.28),
        ("kael", "effondre", 0.50), ("elias", "choc", 0.72),
        ("noam", "neutre", 0.88)
    ])
    "Kael finit par s'asseoir. Sa respiration est encore irrégulière. Lysa pousse un verre d'eau près de lui, sans le forcer à le prendre."
    elias inquiet "Je suis désolé. J'aurais pas dû te demander si tu l'avais déplacée."
    kael effondre "Tu pouvais pas savoir."
    elias gene "Ouais."
    "Elias reste debout. Il tire une chaise, la repousse, puis s'éloigne vers la fenêtre."
    ryn desaccord "On peut regarder les accès aux chambres."
    lysa "Avec quels enregistrements ? Kami ne répond toujours pas."
    ryn "Je dis juste qu'on devrait essayer."
    "Kael garde les yeux sur le verre d'eau."
    kael "Je veux juste retrouver la photo."
    "Je pense au dessin de Juliette. Je pourrais attendre que Kael se remette, mais je sais que je vais finir par devoir en parler."
    noam hesitation "Kael... il m'est arrivé un truc un peu pareil."
    kael effondre "Quoi ?"
    noam triste "Le dessin que ma sœur m'avait donné. Je l'ai vu hier matin. Hier soir, plus rien."
    "Kael ne répond pas. Je regrette aussitôt de l'avoir interrompu."
    kael "C'était où ?"
    noam "Sur mon bureau. J'ai cherché partout."
    kael "Alors tu sais."
    noam "Je sais que je ne le retrouve pas. Je sais pas pourquoi."
    "Kael hoche la tête, mais son visage se ferme."
    kael "Moi, je sais où je range mes affaires."
    "Il a parlé sèchement. Je détourne les yeux."
    ryn "Une photo, un dessin, des batteries. Ça commence à faire beaucoup."
    lysa desaccord "Ça peut être lié. Ça peut aussi être trois problèmes différents."
    ryn "Tu crois vraiment qu'on est tous devenus amnésiques le même jour ?"
    lysa "Non. Je dis qu'on ne va pas fouiller les chambres de tout le monde sur cette seule idée."
    ryn "Je n'ai pas parlé de fouiller les chambres."
    lysa "Pas encore."
    "Ryn ouvre la bouche puis s'arrête. Elias revient lentement vers la table."
    elias "Je peux ressortir les registres de livraison."
    ryn "Les registres, c'est pour les batteries."
    elias "Je sais. C'est tout ce que je peux faire pour l'instant."
    kael triste "Faites ce que vous voulez. Moi, je retourne chercher."
    noam inquiet "Tu veux que je vienne ?"
    kael "Non."
    "Il se lève, puis reprend le verre que Lysa avait laissé à sa portée."
    kael "Pardon de vous avoir crié dessus."
    "Il sort avant que quelqu'un puisse répondre."
    "Personne ne le suit immédiatement. Je ne sais pas si c'est la bonne chose à faire."

    $ investigation_add("photo_lea_disparue")
    $ investigation_add("dessin_juliette_disparu")
    $ investigation_add("materiel_technique_manquant", notify=False)
    $ investigation_add("cafe_renverse", notify=False)
    $ investigation_add("livraison_j7", notify=False)
    $ investigation_add("kami_hors_ligne", notify=False)
    call play_stat_dialogue("d8") from _call_stat_dialogue_d8

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
    "Je pose ma tablette sur le bureau. La note de ce matin est toujours ouverte, avec les heures approximatives que j'ai pu retrouver."
    "Je relis les trois lignes. Je n'y ai rien ajouté depuis le déjeuner."
    think "Kael devait lui aussi être certain de l'endroit où il avait laissé sa photo."
    "Je me dirige vers la porte et vérifie le verrou. Il tient."
    "L'écran de Kami reste noir. Je commence à lui adresser une question, puis je m'arrête."
    noam fatigue "Ouais. Bonne discussion."
    if j701_lysa_search_help:
        "Ma tablette vibre. Lysa m'a écrit : « Si tu veux, on reprend demain. Mais dors cette nuit. »"
        "Je réponds : « D'accord. Merci. »"
        "Elle m'envoie une image de tasse de café. Je ne sais pas si c'est une menace ou une invitation."
    else:
        "Je pense à écrire à Lysa. Je reste un moment devant son nom, puis j'éteins l'écran."
    "Je pousse la chaise devant la porte."
    "Elle ne bloquerait pas grand-chose. Elle va surtout m'obliger à la déplacer demain matin."
    "Je la laisse quand même."
    "Je me couche sans éteindre immédiatement la lampe. Quand je finis par le faire, je regarde encore une fois l'endroit où se trouvait le dessin."
    noam triste "Je vais chercher autrement."
    "Je ferme les yeux. Dans le couloir, j'entends quelqu'un rentrer dans sa chambre, puis une porte qui se ferme."
    "J'attends que mes épaules se détendent. Ça prend du temps."
    $ hideGroup()
    call end_day("9", sleeping=True) from _call_end_day_12
    jump _9_0_1_REVEIL_CHAMBRE
