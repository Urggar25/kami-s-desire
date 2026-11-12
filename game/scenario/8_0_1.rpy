# --------------------------------------------------------------------------------------------
# JOUR 8 — Réveil chambre
# Noam se réveille seul, calme. Cherche le dessin de Juliette. Ne le trouve pas.
# Scène PnC : fouille de la chambre. Le dessin est introuvable.
# Résolution : il décide d'aller manger.
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
    "Le sommeil me quitte d'un seul coup."

    scene bg_chambre at adaptive_fullscreen with dissolve
    noam inquiet "Juliette... Où est-ce que je t'ai rangée ?"
    "Hier soir, j'ai retourné les affaires du bureau avant de me promettre de chercher au réveil. J'espérais presque que la feuille réapparaîtrait d'elle-même pendant la nuit."
    noam reflechit "Allez. Tu as dû le glisser dans un tiroir. Ou dans un livre. Ou..."
    "Je revois Juliette penchée sur son dessin, tirant la langue pour ajouter une dernière mèche de cheveux à mon portrait."
    think "Elle avait passé trois semaines à recommencer mon nez, et j'avais fini par lui dire que c'était le mien qui était raté."
    think "Elle avait ri. Puis elle m'avait interdit de toucher au dessin tant qu'elle n'avait pas signé."
    noam triste "Je l'ai emporté jusque dans l'espace. Ce serait vraiment idiot de le perdre maintenant."
    "Je regarde la chambre. Je suis presque certain d'avoir déjà tout fouillé. Presque."
    tuto "(Fouille la chambre. Le dessin est peut-être encore là.)"
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
            text "FOUILLE DE LA CHAMBRE" xalign 0.5 size 22 color "#D6E8F0"
            text "Zones principales vérifiées : [j8_search_count] / 4" xalign 0.5 size 16 color "#7FCFEA"

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
    "Je retire l'oreiller, secoue la couverture et passe la main entre le matelas et le sommier."
    "Je m'agenouille ensuite pour regarder dessous. Une chaussette oubliée, un peu de poussière... mais aucune trace du dessin."
    noam desaccord "Même les chaussettes ont survécu, et pas ton dessin ? C'est une blague..."
    think "J'aimerais croire que c'en est une."
    return

label _8_PNC_TELEVISION:
    if pnc_flags.get("television"):
        think "L'écran est toujours noir. Rien n'est coincé autour du cadre."
        return

    $ pnc_flags["television"] = True
    $ showGroup([("noam", "inquiet", 0.50)])
    "L'écran mural reste entièrement noir. Je vérifie malgré moi le rebord inférieur et l'espace étroit entre le cadre et le mur."
    noam taquin "Et alors ? Tu peux bien m'aider une fois, non ?"
    "Le reflet du plafond reste immobile dans l'écran. Je me sens idiot de lui avoir parlé."
    think "Au moins, elle ne pourra pas raconter ça aux autres."
    return

label _8_PNC_TIROIR:
    if pnc_flags.get("tiroir"):
        think "Le tiroir est vide. Je l'ai même retiré de ses rails."
        return

    $ pnc_flags["tiroir"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "J'ouvre le tiroir jusqu'à la butée. Quelques formulaires du Conclave, mon badge de réserve et un stylo roulent vers l'avant."
    "Je sors tout, inspecte chaque feuille, puis retire complètement le tiroir pour regarder derrière."
    noam fatigue "J'ai emporté un badge de réserve jusque dans l'espace, mais j'ai perdu une feuille..."
    "Je repose les formulaires, puis les reprends. Une deuxième vérification ne me coûte rien. Elle ne m'apporte rien non plus."
    return

label _8_PNC_ARMOIRE:
    if pnc_flags.get("armoire"):
        think "J'ai fouillé chaque poche et chaque étagère de l'armoire. Rien."
        return

    $ pnc_flags["armoire"] = True
    $ showGroup([("noam", "reflexion", 0.50)])
    "J'ouvre l'armoire et décroche mes vêtements un par un. Je palpe les poches, déplie le pull de l'étagère et vérifie derrière les cintres."
    "Le fond métallique apparaît entièrement nu."
    think "Je fouille la poche de ma veste une deuxième fois. Elle est toujours vide."
    noam colere "Bon sang, arrête de faire semblant de ne pas comprendre !"
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
    "Je soulève la tablette, inspecte sa station d'accueil, puis passe la main derrière la table et sous son plateau."
    "La surface où j'avais posé le dessin est nue. Pas de feuille tombée, pas même un coin de papier coincé contre le mur."
    "Je pose la tablette à l'endroit exact où se trouvait le dessin, puis la repousse."
    think "J'étais certain de l'avoir vu ici. Pourquoi est-ce que plus je cherche, moins je suis sûr de moi ?"
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
    "Le tiroir est sur le sol, les vêtements sur le lit, et je suis à deux doigts de fouiller une troisième fois dans la même poche."
    noam desaccord "Ça suffit..."
    think "Non. Ça ne suffit pas. J'aurais voulu pouvoir arrêter après avoir trouvé quelque chose."
    "Je repense au bureau tel qu'il était avant que je le vide. La feuille était là. Ou alors je me trompe sur le moment où je l'ai vue pour la dernière fois."
    noam reflechit "Je vais finir par accuser une chaussette de m'avoir volé..."
    "Mon estomac proteste. Il est déjà tard."
    think "Je vais manger. Ensuite, je pourrai revenir ici avec une tête qui fonctionne."
    "Je récupère ma veste au fond d'une pile de vêtements."
    menu:
        "Laisser la chambre telle quelle.":
            think "Au moins, si je reviens, je saurai où j'en étais."
            $ chambre_range = True
        "Remettre l'essentiel en place avant de sortir.":
            "Je remets le tiroir sur ses rails et repousse les vêtements dans l'armoire."
            think "Ça ne fait pas réapparaître le dessin, mais je respire un peu mieux."
            $ chambre_range = False
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
        ("tomas", "fatigue"), ("elen", "sourire")
    ])

    julian sourire "C'est officiel. J'annonce la naissance du premier jour férié du Conclave !"
    iris blase "Tu annonces surtout le début de ta prochaine crise de mégalomanie."
    julian taquin "La Fête du Grand Silence. Nous pourrions ériger un monument à son fondateur."
    mara taquin "Un oreiller à ta taille ?"
    elias rire "T'en as un assez grand ?"
    julian surpris "Vous n'avez aucun respect pour l'histoire !"
    elen joie "Moi, je trouve ça sympa, une fête ! On pourrait préparer quelque chose pour ce soir."
    iris sourire "Tant que « quelque chose » ne veut pas dire m'obliger à chanter."
    elen surpris "Mais je chante bien !"
    mara rire "Voilà, ça commence déjà mal."
    "Elen menace Mara avec une petite cuillère. Mara lève les mains en signe de reddition, beaucoup trop heureuse d'avoir obtenu cette réaction."
    noam taquin "On a décrété une fête sans même m'inviter ?"
    julian joie "Noam ! Notre invité d'honneur. Tu arrives juste à temps pour financer l'organisation."
    noam desaccord "Je retire ma candidature."
    lysa sourire "Oh, laisse-le. Sans Kami, Julian a perdu sa seule concurrente en matière d'autosatisfaction."
    julian taquin "Je prends ça comme un compliment."
    iris blase "C'est le problème."
    "Je pose mon plateau à côté de Lysa. Le café est chaud, les rires aussi. J'aurais aimé ne pas avoir passé toute la matinée à retourner ma chambre."
    lysa neutre "Tu as l'air d'avoir perdu un combat contre un placard."
    noam fatigue "J'ai cherché un truc. Rien de grave."
    lysa taquin "Laisse-moi deviner. Une deuxième chaussette ?"
    noam desaccord "Je t'interdis de parler de mes chaussettes."
    lysa sourire "Je me sens immédiatement plus libre."
    lysa reflechit "Tu veux que je t'aide à chercher ?"
    if chambre_range == False:
        think "J'ai au moins remis une partie de la chambre en ordre. Elle pourrait y entrer sans devoir escalader un tiroir."
    noam hesitation "Merci. Je te dirai si je ne trouve vraiment pas."
    lysa neutre "Comme tu veux."
    "Elle ne me demande pas ce que j'ai perdu. Je suis content qu'elle n'insiste pas, et un peu vexé qu'elle n'insiste pas."
    elen sourire "Au fait, on a décidé pour la fête ?"
    mara taquin "Oui. Julian fait un discours, et nous, on se bouche les oreilles."
    julian surpris "J'ai dit que je pouvais faire un discours ! Pas que j'allais le faire !"
    iris blase "Tu as déjà commencé."
    elias rire "Si tu parles assez longtemps, Kami va peut-être se rallumer juste pour te couper."
    "Un rire passe autour de la table. Iris, elle, relève aussitôt la tête."
    iris reflechit "C'est peut-être exactement ce qu'on devrait essayer."
    mara surpris "Faire parler Julian pendant six heures ?!"
    iris colere "NON ! Tester les réactions du système !"
    kael reflechit "Il faudrait distinguer les fonctions automatisées des réponses de Kami."
    julian taquin "Je propose un test simple : on lui demande lequel d'entre nous est le plus séduisant."
    lysa blase "On connaît déjà ta réponse."
    tomas reflechit "À propos des fonctions automatisées, j'ai... enfin, j'ai vérifié un chiffre cette nuit."
    iris fatigue "Tomas. Pas pendant que je mange."
    tomas gene "C'est important."
    mara taquin "Ses statistiques sont jalouses. Elles veulent aussi leur moment de gloire."
    tomas inquiet "Il n'y a eu aucune nouvelle exécution enregistrée."
    "Le verre d'Elen s'arrête à quelques centimètres de sa bouche."
    elen surpris "Aucune ?"
    tomas reflechit "Depuis la fin du vote du jour six. Le compteur mondial n'a pas bougé."
    noam neutre "Tu as revérifié depuis hier ?"
    tomas neutre "Trois fois. Je ne voulais pas vous le dire tant que je n'avais pas..."
    mara agace "Attends, tu le savais déjà ?!"
    tomas gene "Noam aussi. Je lui ai montré hier."
    "Les regards convergent vers moi. Merci, Tomas."
    julian surpris "Et vous avez gardé ça pour vous ?!"
    noam hesitation "On n'était pas sûrs. On ne l'est toujours pas."
    elen joie "Mais ça veut dire que plus personne ne meurt à cause des Commandements !"
    tomas inquiet "Pas nécessairement. Ça veut dire que le système n'enregistre plus d'exécutions."
    elen surpris "C'est différent ?"
    tomas neutre "Si les données sont fausses, oui. Si les sanctions ont réellement cessé, non. Et si..."
    iris colere "TOMAS ! Respire !"
    tomas gene "Pardon."
    elias reflechit "Donc on sait rien, sauf que les chiffres font un truc impossible."
    tomas neutre "C'est... une formulation assez juste."
    julian sourire "Ou alors nous tenons l'homme qui a sauvé l'humanité."
    elias fatigue "Oh non."
    julian joie "Elias ! Le chevalier au café ! Le renverseur d'empires !"
    mara rire "J'imagine déjà la statue. Un mug sur la tête !"
    elias colere "JE L'AI PAS FAIT EXPRÈS !"
    iris taquin "C'est précisément ce qui rend la théorie crédible."
    elias fatigue "Je vais finir par boire de l'eau."
    lysa blase "Ne prends pas ce risque. On ne sait pas ce qui arriverait à la gravité."
    "Il essaye de ne pas rire. Il échoue."
    menu:
        "Entrer dans leur jeu.":
            noam taquin "Quand tu auras ton monument, Elias, rappelle-toi de nous. On a tous assisté à l'attaque décisive."
            elias rire "Vous êtes vraiment irrécupérables."
            julian sourire "L'Histoire me donnera raison."
        "Ramener la discussion aux faits.":
            noam reflechit "Je préférerais qu'on évite de tester cette théorie sur Terre."
            tomas raison "Exactement. Une baisse des exécutions, même réelle, ne garantit pas la disparition des Commandements."
            mara neutre "D'accord. Mais je garde l'idée de la statue."
    elen inquiet "Si des gens commencent à croire qu'ils peuvent désobéir, et que Kami revient..."
    "La phrase se perd. Plus personne ne sourit."
    iris fatigue "On ne sait même pas si elle est vraiment partie."
    lysa reflechit "On connaît une chose : elle n'a donné aucun ordre depuis deux jours."
    mara neutre "Ça fait une chose de plus que ce qu'on savait hier."
    "Julian regarde son dessert, le découpe en deux et pousse discrètement la plus grande moitié vers Elen."
    elen surpris "C'est pour moi ?"
    julian decontracte "Considère ça comme une réparation diplomatique après le gâteau d'hier."
    elen sourire "Je n'avais pas oublié !"
    julian taquin "Je sais. C'est bien ce qui m'inquiétait."
    "Lysa s'esclaffe. La table retrouve peu à peu son bruit ordinaire, sans que personne ait vraiment répondu à la question d'Elen."
    think "J'aimerais leur parler du dessin. Avec eux, cela deviendrait peut-être une histoire de chaussette ou de mug. Je ne suis pas prêt."
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
    noam sourire "Je suppose que l'étagère n'a pas partagé ton avis."
    elias rire "Elle s'est effondrée après que j'ai posé une seule boîte dessus."
    ryn desaccord "Une boîte qui pesait le poids d'un moteur !"
    lysa sourire "L'étagère a fait son choix. Respecte-le."
    "Ryn grogne mais finit par rire. Je découvre que le son est presque rassurant, quand il ne le dirige contre personne."
    lysa reflechit "Au fait... Kael a disparu après le repas."
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

    kael colere "Qui est entré dans ma chambre ?"
    elias choc "Kael ?"
    kael colere "Je vais le demander une fois. Qui est entré dans ma chambre ?!"
    ryn inquiet "Hé. Personne ici n'a dit qu'il y était allé."
    kael colere "Alors pourquoi il manque quelque chose ?!"
    noam inquiet "Qu'est-ce que tu as perdu ?"
    kael colere "Je ne l'ai pas perdu !"
    "La réponse est tellement violente que je recule d'un pas."
    lysa choc "Kael... On ne sait même pas de quoi tu parles."
    kael inquiet "Une photo. Une petite photo que je gardais sous l'oreiller."
    elias inquiet "Tu es sûr qu'elle était..."
    kael colere "LÉA ! C'ÉTAIT LA PHOTO DE LÉA !"
    "Ryn ouvre la bouche, puis la referme. Kael respire beaucoup trop vite."
    kael inquiet "Je l'ai vue hier. Je l'ai prise pour la regarder avant de dormir et..."
    "Il ne termine pas."
    noam hesitation "On peut t'aider à chercher."
    kael colere "J'AI CHERCHÉ !"
    "Sa voix me fait sursauter. Ce n'est pas le Kael qui calculait tranquillement les pannes pendant que nous paniquions tous."
    ryn inquiet "D'accord. On t'écoute."
    kael colere "Alors dis-moi pourquoi personne ne répond !"
    ryn desaccord "Parce qu'on n'a pas la réponse !"
    lysa colere "Ryn, PAS MAINTENANT !"
    "Ryn se tait aussitôt. Kael regarde la porte, les tables, nos visages, puis revient sur moi."
    kael inquiet "Si quelqu'un l'a prise, il savait où elle était."
    noam inquiet "Kael..."
    kael colere "ET IL SAVAIT À QUI ELLE APPARTENAIT !"
    $ unlock_gallery_image("bg_cg050")
    scene bg_cg050 at adaptive_fullscreen with vpunch
    kael colere "Alors qu'il vienne me regarder dans les yeux !"
    stop music fadeout 0.8
    play music "music/bgm_stabilisation_tension.mp3" fadein 0.8
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
    "Kael finit par s'asseoir. Sa respiration est encore irrégulière. Lysa pousse un verre d'eau à sa portée, puis recule sans chercher à le toucher."
    elias inquiet "Je suis désolé, Kael. J'aurais pas dû..."
    kael effondre "Tu n'as rien fait."
    elias gene "Ouais. Mais..."
    kael effondre "S'il te plaît."
    "Elias baisse les yeux. Cette fois, il réussit à se taire."
    ryn inquiet "Je peux vérifier les couloirs. Demander si quelqu'un a vu..."
    kael effondre "Arrêtez."
    "Le silence est immédiat."
    kael triste "Je ne voulais pas vous crier dessus."
    lysa neutre "Tu n'as pas besoin de t'excuser maintenant."
    kael effondre "J'ai promis que je la garderais."
    noam inquiet "La photo ?"
    kael effondre "Oui."
    "Il se frotte le visage d'une main. Personne ne lui demande de raconter la suite."
    noam hesitation "Kael... Je vais te dire quelque chose, mais je ne sais pas si ça va t'aider."
    lysa reflechit "Noam ?"
    noam inquiet "Le dessin de Juliette. Ma petite sœur me l'avait donné avant mon départ. Je l'ai cherché toute la matinée."
    noam triste "Il a disparu lui aussi."
    ryn surpris "Quoi ?!"
    elias choc "Attends. Deux objets personnels, dans deux chambres différentes ?"
    kael inquiet "Quand ?"
    noam reflechit "Je l'ai remarqué hier soir. Et je n'ai rien trouvé ce matin."
    lysa triste "C'était ça que tu cherchais..."
    noam hesitation "Oui. Je croyais l'avoir mal rangé."
    lysa desaccord "Tu aurais pu me le dire."
    noam neutre "Je sais."
    "Elle ne réplique pas. Elle regarde Kael, puis mes mains vides."
    elias inquiet "On a aussi les batteries et les outils qui manquent depuis hier."
    ryn colere "Alors il y a quelqu'un qui vole dans les chambres !"
    noam reflechit "On ne sait pas ça. On sait que des objets ont disparu."
    ryn desaccord "Tu vas pas me dire que c'est une coïncidence !"
    noam neutre "Je dis qu'on ne devrait pas accuser quelqu'un sans preuve."
    ryn colere "Et attendre que d'autres affaires disparaissent ?!"
    kael effondre "Je me fiche des batteries."
    "Sa voix est basse. Ryn s'interrompt."
    kael triste "Je veux juste ma photo."
    "Cette phrase fait plus mal que ses cris."
    lysa neutre "Alors on va essayer de comprendre. Sans transformer le Conclave en chasse aux sorcières."
    elias reflechit "Les caméras sont peut-être encore actives. Même si Kami ne parle plus..."
    noam inquiet "Kael, on peut vérifier les accès aux chambres. Tu préfères qu'on commence là ?"
    kael effondre "Je ne sais pas."
    kael neutre "Faites ce que vous voulez. Je ne veux juste pas qu'on vienne me raconter que j'ai oublié où je l'avais mise."
    noam neutre "D'accord."

    $ investigation_add("photo_lea_disparue")
    $ investigation_add("dessin_juliette_disparu")
    $ investigation_add("materiel_technique_manquant", notify=False)
    $ investigation_add("cafe_renverse", notify=False)
    $ investigation_add("livraison_j7", notify=False)
    $ investigation_add("kami_hors_ligne", notify=False)
    call play_stat_dialogue("d8") from _call_stat_dialogue_d8

    "Ryn propose de prévenir tout le monde. Lysa lui fait remarquer qu'on pourrait commencer par interroger les gens sans les traiter de voleurs."
    ryn desaccord "J'ai pas dit que j'allais leur taper dessus !"
    lysa blase "Tu l'as pensé si fort que j'ai cru l'entendre."
    "Il fulmine, mais n'insiste pas. Elias reste près de Kael, à une distance suffisamment grande pour ne pas l'étouffer."
    noam reflechit "Je vais chercher du côté des accès. Et je vérifierai encore ma chambre."
    kael effondre "... Merci."
    "J'aurais préféré qu'il s'énerve une dernière fois. C'est plus facile à supporter que cette voix-là."
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
    "Le bureau est exactement dans l'état où je l'ai laissé."
    "Ça ne devrait pas me rassurer. Ça me rassure quand même."
    think "Une photo. Un dessin. Des batteries."
    think "À la table, tout le monde cherchait un mobile. Moi aussi. Pourtant, je ne sais même pas si nous parlons de la même personne."
    "Je récupère une feuille vierge et un stylo. Je note les heures auxquelles je me souviens avoir vu mon dessin."
    noam reflechit "Avant le vote... puis..."
    "Je m'arrête. Je ne peux pas me rappeler exactement à quel moment je l'ai posé sur le bureau."
    think "Je suis certain de l'avoir eu. Mais je commence à comprendre ce que Kael ressent quand on lui demande s'il n'a pas simplement oublié."
    "Je ferme le tiroir. Un bruit sec me fait tourner la tête."
    pause 0.5
    "Rien. C'était ma chaise qui s'était déplacée."
    noam taquin "Magnifique. Je vais bientôt interroger les meubles."
    "J'essaye de rire. Le son ne va pas bien loin."
    "L'écran de Kami reste noir. Sans ses remarques, la pièce devrait être plus accueillante."
    think "Depuis deux jours, on ne nous dit plus quoi faire. J'avais pris ça pour une liberté."
    think "Peut-être que c'en est une. Peut-être aussi qu'on ne sait pas quoi en faire."
    "Je bloque la chaise sous la poignée, puis je m'arrête pour mesurer à quel point mon geste est ridicule."
    noam fatigue "Si quelqu'un veut vraiment entrer, il trouvera un moyen."
    "Je laisse la chaise en place."
    "Avant de m'allonger, je regarde encore le bureau. J'aurais donné n'importe quoi pour y voir un simple dessin mal rangé."
    noam triste "Juliette... Je vais le retrouver."
    "Je ferme les yeux."
    "Dans le silence, le petit claquement du tiroir me revient. Cette fois, je n'arrive plus à me souvenir si c'était bien ma chaise."
    $ hideGroup()
    call end_day("9", sleeping=True) from _call_end_day_12
    jump _9_0_1_REVEIL_CHAMBRE
