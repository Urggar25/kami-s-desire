# Rencontres facultatives sur les trajets scénarisés, J5-J8.
# Chaque rencontre se joue une seule fois par passage dans le label de trajet ;
# le joueur peut continuer immédiatement. Aucun effet sur les votes ou indices.

label KD_ROUTE_J5_NYRA:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Nyra consulte sa tablette près du croisement. Elle relève la tête quand je passe."
    menu:
        "Échanger quelques mots avec Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "neutre", 0.65)])
            nyra "Tu vas à l'Observation ?"
            noam "Je voudrais voir ce qui se passe en bas."
            nyra "Pour chercher quoi ?"
            noam reflexion "Je sais pas exactement. Voir comment les choses évoluent."
            nyra raison "Alors commence par choisir une question. Sinon tu vas passer une heure devant des images sans rien apprendre."
            noam taquin "Tu fais toujours un programme avant de regarder par une fenêtre ?"
            nyra "Non. Mais je ne confonds pas regarder et comprendre."
            noam "Je te dirai si je trouve quelque chose."
            nyra neutre "Seulement si tu sais ce que tu as trouvé."
            $ hideGroup()
        "Continuer vers l'Observation.":
            pass
    return

label KD_ROUTE_J5_LYSA:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa est adossée au mur. Elle me voit arriver de l'autre côté du couloir."
    menu:
        "Parler à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "neutre", 0.65)])
            lysa "C'était quoi, cette réunion de crise avec Kael et Nyra ?"
            noam reflexion "Kael avait besoin de parler."
            lysa "J'avais compris. Il est passé devant moi sans même répondre quand je lui ai dit bonjour."
            noam "Il s'inquiète pour sa sœur."
            lysa neutre "Ah."
            "Elle perd son sourire un instant."
            lysa "Je vais éviter de lui sortir une blague idiote, alors."
            noam taquin "C'est une première."
            lysa blase "Profite. Ça n'arrivera pas souvent."
            $ hideGroup()
        "Rejoindre la cafétéria.":
            pass
    return

screen j601_elen_clic_couloir():
    modal True
    zorder 180
    imagebutton:
        idle Transform(character_image("elen", "joie"), zoom=0.85)
        hover Transform(character_image("elen", "content"), zoom=0.88)
        xalign 0.72
        yalign 1.0
        focus_mask True
        action Return(True)
    frame:
        xalign 0.5
        yalign 0.08
        background Solid("#071822cc")
        padding (20, 10)
        text "Clique sur Elen pour lui parler" size 26 color "#ffffff"

label KD_ROUTE_J6_ELEN:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Elen sort des dortoirs au moment où je prends la direction de la cafétéria. Elle me fait de grands signes."
    call screen j601_elen_clic_couloir
    $ showGroup([("elen", "content", 0.35), ("noam", "fatigue", 0.65)])
    elen content "Noam ! Hé ! T'as dormi ?"
    noam fatigue "Un peu. Enfin... pas beaucoup."
    elen surpris "Oh non ! Mais t'as mangé au moins ?"
    noam "Elen, je viens de me lever."
    elen joie "Alors on va manger ! Ça va te faire du bien, tu vas voir !"
    noam surpris "Attends, je comptais justement..."
    "Elle m'attrape par le poignet et commence déjà à marcher."
    elen content "Allez, viens ! Goumi doit avoir préparé quelque chose. Tu réfléchiras mieux le ventre plein !"
    noam "Je sais marcher tout seul !"
    elen rire "Je sais ! Mais là, tu marches pas assez vite."
    $ hideGroup()
    $ j601_with_elen = True
    return

label KD_ROUTE_J6_JULIAN:
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Julian attend près de la porte de la salle de repos. Il me fait un grand signe."
    menu:
        "Écouter Julian.":
            $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
            julian "Avant d'entrer, une question stratégique : tu comptes défendre quoi ?"
            noam "Je vais surtout écouter les autres."
            julian taquin "Ah, la fameuse stratégie du type qui attend que tout le monde s'énerve."
            noam "Ça marche mieux que tes discours improvisés."
            julian "Mes discours sont des œuvres en constante évolution."
            noam "Tu as au moins une proposition ?"
            julian hesitation "Oui. Éviter que Ryn et Sael recommencent à se hurler dessus."
            noam sourire "Pour une fois, on est d'accord."
            julian sourire "Tu vois ? Je rassemble déjà les foules."
            $ hideGroup()
        "Entrer dans la salle de repos.":
            pass
    return

label KD_ROUTE_J7_ELIAS:
    $ kd_j78_mark_seen("j7_elias")
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    "Elias transporte une caisse de matériel. Il la pose par terre pour reprendre son souffle."
    $ showGroup([("elias", "fatigue", 0.35), ("noam", "neutre", 0.65)])
    elias "Ah, merci ! Prends ce côté, ça glisse un peu. Je l'avais mise sur le chariot, mais Nyra en avait besoin."
    noam "Tu vas où avec tout ça ?"
    elias "Au stockage, avec les caisses. J'essaie de remettre en marche le gros robot de la maintenance. Ce matin, avant la livraison, j'ai vérifié ses connexions. J'aimerais bien pouvoir le faire bouger pour de vrai."
    noam "Tu devrais demander un coup de main à Kael."
    elias "Il m'aide déjà quand il a le temps. Mais j'aimerais bien lui montrer un truc qui marche, tu vois ? Pas débarquer à chaque fois avec un machin démonté dans les mains."
    "On soulève la caisse. Elias manque de coincer son pied dessous."
    elias "Attends, attends ! Mon lacet."
    "Je repose mon côté. Il refait son lacet."
    noam "T'as besoin que je vienne jusqu'au stockage ?"
    elias "Non, laisse, t'as déjà aidé. Je te montrerai ce que j'ai fait quand ça sera présentable. Enfin, si j'arrive à le finir avant qu'on rentre."
    noam "Ça me ferait plaisir."
    elias sourire "Cool. Va manger, je vais me prendre un café après."
    $ hideGroup()
    return
label KD_ROUTE_J7_LYSA_SECRET:
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Lysa apparaît au croisement des dortoirs. Je ralentis malgré moi."
    menu:
        "Répondre à Lysa.":
            $ showGroup([("lysa", "blase", 0.35), ("noam", "inquiet", 0.65)])
            lysa "Encore par ici ? Tu cherches ta chambre ou celle d'Iris ?"
            noam hesitation "Pourquoi tu me demandes ça ?"
            lysa taquin "Parce que t'as la tête de quelqu'un qui essaie d'avoir l'air naturel. C'est raté."
            noam "Je voulais juste lui parler."
            lysa "Bon courage. Elle a l'air d'une humeur charmante aujourd'hui."
            noam "Merci du conseil."
            lysa blase "Et arrête de regarder derrière toi comme ça, c'est franchement louche."
            noam sourire "Je ferai un effort."
            lysa "S'il te plaît. C'est fatigant à regarder."
            $ hideGroup()
        "Passer sans s'arrêter.":
            pass
    return

label KD_ROUTE_J7_NYRA_GUEST:
    scene couloir_infirmerie at adaptive_fullscreen with dissolve
    "Nyra sort d'un couloir adjacent avec ses relevés de rationnement."
    menu:
        "Discuter avec Nyra.":
            $ showGroup([("nyra", "neutre", 0.35), ("noam", "inquiet", 0.65)])
            nyra "Tu vas voir l'invitée ?"
            noam "Oui. Je voulais savoir si son état s'améliore."
            nyra "J'espère aussi. Mais il faudra régler la question des rations."
            noam "Tu penses déjà à la nourriture ?"
            nyra raison "Il faudra bien que quelqu'un y pense. Kami ne nous en donnera pas davantage par gentillesse."
            noam "Elle est à peine consciente, Nyra."
            nyra "Je ne lui reproche rien. Je dis seulement qu'on devra répartir autrement ce qu'il nous reste."
            noam reflexion "D'accord. On en reparle quand on en saura plus."
            nyra "C'est ce que je comptais faire."
            $ hideGroup()
        "Aller directement à l'infirmerie.":
            pass
    return

label KD_ROUTE_J8_JULIAN:
    $ kd_j78_mark_seen("j8_julian_morning")
    scene couloir_dortoir at adaptive_fullscreen with dissolve
    "Julian passe devant moi, s'arrête et revient sur ses pas."
    $ showGroup([("julian", "sourire", 0.35), ("noam", "fatigue", 0.65)])
    julian "Tu sais que tu fais une tête absolument catastrophique ?"
    noam "Bonjour à toi aussi."
    julian taquin "J'hésitais entre te proposer une partie et appeler Sael."
    noam "Ni l'un ni l'autre, merci."
    julian "D'accord. Alors une question facile : café ou thé ?"
    noam reflexion "Quoi ?"
    julian "Je t'offre une boisson à la cafétéria. Pas besoin de parler si t'en as pas envie."
    noam fatigue "Ça ira. Mais merci."
    julian neutre "Bon. Si tu changes d'avis, je serai là."
    noam sourire "Je note."
    $ hideGroup()
    return

# Rencontres locales J7_0_1 / J8_0_1 : indépendantes des scènes de lien.
# La disponibilité dépend du trajet ou du temps libre exact, pas seulement du jour.
default kd_j78_seen = []

init python:
    def kd_j78_available(encounter_id):
        if encounter_id in store.kd_j78_seen:
            return False
        if encounter_id == "j7_elias":
            return store.exploration_libre_active and store.exploration_libre_next_label == "_7_0_1_CAFETERIA_ARRIVEE"
        if encounter_id == "j8_julian_morning":
            return store.exploration_libre_active and store.exploration_libre_next_label == "_8_0_1_CAFETERIA_ARRIVEE"
        if not social_free_time_active():
            return False
        if encounter_id == "j8_julian_afternoon":
            return store.free_time_next_label == "_8_0_1_APRES_MIDI_KAEL_CRISE"
        if store.free_time_next_label != "_7_0_1_APRES_MIDI_TOMAS_CANON":
            return False
        # Anciennes sauvegardes : ne pas rejouer le choix de table déjà effectué.
        legacy_choices = {"j7_iris": "inquietude", "j7_elen": "complicite", "j7_julian": "julian"}
        if encounter_id in legacy_choices and store.j701_table_choice == legacy_choices[encounter_id]:
            return False
        return encounter_id in ("j7_iris", "j7_elen", "j7_julian", "j7_kael")

    def kd_j78_mark_seen(encounter_id):
        if encounter_id not in store.kd_j78_seen:
            store.kd_j78_seen = list(store.kd_j78_seen) + [encounter_id]

    def kd_j78_corridor_encounters(corridor_key):
        encounters = {
            "cafeteria": [
                ("j7_elias", "elias", "fatigue", "sourire", "KD_ROUTE_J7_ELIAS", 0.58),
                ("j7_kael", "kael", "reflechit", "fatigue", "KD_J701_FREE_KAEL", 0.52),
            ],
            "dortoir": [
                ("j8_julian_morning", "julian", "sourire", "taquin", "KD_ROUTE_J8_JULIAN", 0.58),
            ],
        }
        return [entry for entry in encounters.get(corridor_key, []) if kd_j78_available(entry[0])]

screen kd_j78_corridor_actors(corridor_key):
    for encounter_id, actor, idle_expr, hover_expr, target, actor_x in kd_j78_corridor_encounters(corridor_key):
        imagebutton:
            idle Transform(character_image(actor, idle_expr), zoom=1.00)
            hover Transform(character_image(actor, hover_expr), zoom=1.00)
            focus_mask True
            xalign actor_x
            yalign 1.0
            hovered SetVariable("corridor_ui_target", "Parler à " + actor.capitalize())
            unhovered SetVariable("corridor_ui_target", None)
            action Return(target)

screen kd_j78_room_actor(encounter_id, actor, idle_expr, hover_expr, target, actor_x=0.5):
    if kd_j78_available(encounter_id):
        imagebutton:
            idle Transform(character_image(actor, idle_expr), zoom=1.00)
            hover Transform(character_image(actor, hover_expr), zoom=1.00)
            focus_mask True
            xalign actor_x
            yalign 1.0
            action Jump(target)

label KD_J701_FREE_KAEL:
    $ kd_j78_mark_seen("j7_kael")
    scene couloir_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("kael", "reflechit", 0.31), ("noam", "neutre", 0.72)])
    "Kael a posé une feuille sur une caisse et essaie de noter quelque chose en mangeant son pain."
    noam "Je peux m'asseoir ? J'ai pas envie de retourner dans ma chambre tout de suite."
    kael "Oui. Fais attention au crayon."
    "Je m'installe. Il continue ses calculs."
    noam "Ça fait longtemps que tu bosses là-dessus ?"
    kael "Depuis cette nuit. J'ai dormi un peu entre deux vérifications. Les relevés du Conclave et ceux de l'observatoire ne concordent pas. Je les recopie parce que les terminaux ne sont même pas d'accord sur l'ordre des événements."
    noam "Je croyais que tu pouvais faire ça automatiquement."
    kael "D'habitude, oui. Mais je préfère retrouver une heure que je peux vérifier moi-même. À Orbite, j'ai appris à ne pas faire confiance à un affichage simplement parce qu'il est précis."
    "Il efface une colonne. Un peu de graphite a taché le pain."
    noam "Tu sais que t'es en train de manger ton crayon, là ?"
    kael "Ah."
    "Il pose le pain et nettoie son doigt sur la feuille."
    kael "Je faisais pareil avec mes maquettes. J'avais passé un temps fou à monter le gréement d'un voilier et j'ai cassé le mât en voulant le ranger. J'ai dû recommencer toute une partie."
    noam "Un voilier ?! Je pensais que tu collectionnais des vaisseaux spatiaux, des trucs un peu plus classes."
    kael "Je voyais des vaisseaux tous les jours sur Orbite. Les voiliers, par contre... J'ai jamais vu la mer. J'ai regardé des tas de vidéos pour comprendre comment ils utilisaient le vent."
    noam "T'aimerais essayer ?"
    kael "Bien sûr. Rien que monter à bord, ça me plairait. Après, je laisserais quelqu'un d'autre s'occuper des manœuvres."
    "Il me montre la taille de la maquette avec ses mains."
    noam "Ah ouais, c'est carrément un meuble ton truc. J'avais un modèle de vaisseau quand j'étais plus jeune, j'ai perdu une aile et j'ai fini par le jeter."
    kael "Tu aurais pu la refaire. Je peux te montrer comment, à l'occasion."
    noam "Tu risques de regretter de m'avoir proposé ça."
    "Il reprend son crayon."
    if j601_fracture_trace_saved:
        kael "Au fait, tu as conservé la trace du piratage sur ta tablette ? Ne la modifie pas. J'aimerais comparer les horodatages avec les relevés originaux."
        noam "Je te la laisse quand tu veux."
        kael "Merci. Pas besoin de me l'envoyer pour l'instant."
        $ j701_evidence_note = True
    else:
        kael "Il me faudrait un enregistrement complet de la diffusion d'hier. Les relevés que j'ai récupérés sont incomplets, je vais voir si la console d'observation a gardé une copie."
    noam "Tu devrais dormir avant de continuer. Tu vas finir par te tromper dans tes propres calculs."
    kael "Possible. Je termine cette colonne et je vais m'allonger."
    "Je le laisse à ses papiers."
    $ hideGroup()
    return

label KD_J701_FREE_IRIS:
    $ kd_j78_mark_seen("j7_iris")
    if j701_table_choice == "aucun":
        $ j701_table_choice = "inquietude"
    $ j701_iris_defense = True
    scene bg_infirmerie at adaptive_fullscreen with dissolve
    $ showGroup([("iris", "reflechit", 0.35), ("noam", "neutre", 0.65)])
    noam "Iris, attends. Je peux t'aider à regarder les terminaux."
    iris "Tu vas surtout me poser des questions pendant que j'essaie de bosser. Laisse-moi faire, d'accord ? Si tu entends quelque chose sur ta tablette, tu me le dis."
    noam "D'accord. Je t'ai gardé un bout de gâteau."
    $ hideGroup()
    jump INFIRMERIE_TP

label KD_J701_FREE_ELEN:
    $ kd_j78_mark_seen("j7_elen")
    if j701_table_choice == "aucun":
        $ j701_table_choice = "complicite"
    scene bg_cafeteria at adaptive_fullscreen with dissolve
    $ showGroup([("elen", "neutre", 0.35), ("noam", "neutre", 0.65)])
    elen "Je voulais juste qu'on passe un bon moment. J'ai peut-être choisi le mauvais jour."
    noam "Viens, montre-moi les cartes. On peut préparer le jeu quand même."
    "Elle étale les cartes sur la table et me demande de l'aider à les trier."
    $ hideGroup()
    jump CAFETERIA_TP

label KD_J701_FREE_JULIAN:
    $ kd_j78_mark_seen("j7_julian")
    if j701_table_choice == "aucun":
        $ j701_table_choice = "julian"
    scene bg_repos at adaptive_fullscreen with dissolve
    $ showGroup([("julian", "sourire", 0.35), ("noam", "neutre", 0.65)])
    noam "Julian, si tu veux vraiment faire quelque chose d'utile, aide Elen à organiser sa soirée."
    julian "Très bien. Mais je refuse qu'on me rende responsable de la mauvaise humeur générale."
    "Il récupère le paquet de cartes sans attendre ma réponse."
    $ hideGroup()
    jump REPOS_TP

label KD_J801_FREE_JULIAN:
    $ kd_j78_mark_seen("j8_julian_afternoon")
    call KD_EXTRA_J8_JULIAN from _call_kd_extra_j8_julian
    jump CAFETERIA_TP
