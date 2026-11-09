# -----------------------------------------------------------------------
# CAFÉTÉRIA — même modèle que OBSERVATION / CANON
# - Persos : Noam + Elen
# - Rencontre : Goumi (robot cuisinier) — pas de sprite, mais il parle
# - PNC : frigo-machine / tables / goumi / retour
# -----------------------------------------------------------------------

default decouverte_cafeteria = False



label CAFETERIA_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_327
    scene bg_cafeteria at adaptive_fullscreen

    if current_scene_active == "_2_ROUTE_CAFETERIA":
        $ current_scene_active = None
        jump _2_CAFETERIA_ANNONCE_KAMI

    if current_scene_active == "_3_ROUTE_CAFETERIA":
        $ current_scene_active = None
        jump _3_CAFETERIA_ARRIVE

    if not decouverte_cafeteria and day_number() == 1:
        jump decouverte_cafeteria

    $ pnc_room = "pnc_cafeteria"
    call screen pnc_cafeteria()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_cafeteria():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("cafeteria")
    use room_scene_interactions("cafeteria")

    if current_scene_active == "_2_ROUTE_OBSERVATION" and not day2_observation_route_elen_seen:
        imagebutton:
            idle Transform(character_image("elen", "content"), zoom=1.00)
            hover Transform(character_image("elen", "joie"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action Jump("_2_APRES_MIDI_ELEN")

    if social_free_time_active() and character_has_available_free_time("mara"):
        imagebutton:
            idle Transform(character_image("mara", "sourire"), zoom=1.00)
            hover Transform(character_image("mara", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.15
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "mara"), Jump("FREE_TIME_CHARACTER_INTERACT")]


    if social_free_time_active() and character_has_available_free_time("lysa"):
        imagebutton:
            idle Transform(character_image("lysa", "sourire"), zoom=1.00)
            hover Transform(character_image("lysa", "taquin"), zoom=1.00)
            focus_mask True
            xalign 0.82
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "lysa"), Jump("FREE_TIME_CHARACTER_INTERACT")]

    if social_free_time_active() and character_has_available_free_time("elen"):
        imagebutton:
            idle Transform(character_image("elen", "joie"), zoom=1.00)
            hover Transform(character_image("elen", "content"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "elen"), Jump("FREE_TIME_CHARACTER_INTERACT")]

    if j10011_waiting_elias:
        imagebutton:
            idle Transform(character_image("elias", "fatigue"), zoom=1.00)
            hover Transform(character_image("elias", "inquiet"), zoom=1.00)
            focus_mask True
            xalign 0.58
            yalign 1.00
            action Jump("_10_0_1_1_CAFETERIA_ELIAS")



label cafeteria1_porte:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label cafeteria1_table:

    window auto

    "Des tables."
    "Des chaises."
    "Un espace pensé pour faire comme si on vivait ici."

    think "Ça pourrait presque marcher."
    jump CAFETERIA_TP


label cafeteria1_television:

    if day_number() == 6 and social_free_time_active() and not j601_border_news_seen:
        call _6_0_1_TV_FRONTIERES from _call_j601_tv_frontieres_cafeteria
        jump CAFETERIA_TP

    if day_number() == 4:
        call day4_optional_news from _call_day4_optional_news_cafeteria
        jump CAFETERIA_TP

    think "Les informations défilent sans rien m'apprendre de neuf."
    jump CAFETERIA_TP


label cafeteria2_cuisine:

    window auto

    "Le comptoir est clean."
    "Trop clean."
    "Comme si personne n'avait le droit d'y laisser une miette."

    "Derrière, le frigo-machine ronronne."
    "Et Goumi reste planté là, immobile."
    "Il me suit avec ses yeux-lentilles, sans bouger d'un millimètre."

    goumi "Souhaitez-vous une préparation nutritionnelle ?"

    think "Nutritionnelle ? Et puis quoi encore. Je préfère largement la nourriture bien grasse."
    jump CAFETERIA_TP


label cafeteria2_distributeur:

    window auto

    "La machine au fond ressemble à un frigo."
    "Sauf qu'elle fait la taille d'une armoire industrielle."

    "Écran tactile."
    "Tiroirs verrouillés."
    "Et une liste de catégories et d'aliments qui défile."

    think "Au moins ça n'a pas l'air d'être très compliqué."
    jump CAFETERIA_TP


label cafeteria2_tablette_commande:
    "La tablette de commande affiche des catégories propres, trop propres."
    "Entrées, plats, desserts, boissons."
    "Tout est rangé comme si le choix était une simple question d'interface."
    think "C'est pratique. Et vaguement humiliant."
    jump CAFETERIA_TP


label cafeteria3_reserve:

    window auto

    "La réserve est verrouillée."
    "Derrière la vitre, les stocks sont alignés avec une précision clinique."

    if cafeteria_food_visible_count() >= 5:
        think "Il y a encore de quoi tenir. Pour l'instant."
    elif cafeteria_food_visible_count() >= 3:
        think "Les rangées ont déjà l'air moins pleines."
    elif cafeteria_food_visible_count() >= 1:
        think "Il reste peu de choses visibles. Trop peu pour que ce soit rassurant."
    else:
        think "Vide. Ou assez proche du vide pour que mon estomac comprenne le message."
    jump CAFETERIA_TP


label cafeteria3_nourriture:

    window auto

    "Je regarde les portions restantes."
    "Tout est propre, emballé, calibré."
    "Même la nourriture a l'air de suivre un protocole."

    think "On ne mesure pas seulement ce qu'il reste à manger."
    think "On mesure combien de temps on peut encore faire semblant que tout va bien."
    jump CAFETERIA_TP


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_cafeteria:

    $ decouverte_cafeteria = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "Une cafétéria. Après tout ce qui vient de se passer, je mangerais bien quelque chose de normal."

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_328
    scene bg_cafeteria at adaptive_fullscreen with fade
    "Le comptoir est impeccable et la cuisine semble entièrement automatisée. Une fille discute avec un petit robot, sans beaucoup de succès."

    scene bg_cg008 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg008")

    elen vide "Je t'ai demandé quelque chose qui me remonte le moral, pas un cours de nutrition !"
    goumi vide "Demande comprise. Je prépare une collation optimisée pour améliorer votre état physique."
    elen vide "Ah, voilà ! Tu vois, quand tu veux, tu comprends très bien."
    noam vide "J'arrive au mauvais moment ?"
    elen vide "Au contraire ! Tu vas goûter. J'ai demandé à ce qu'il nous fasse le meilleur truc possible."
    noam vide "C'est ambitieux. J'espère qu'il fait du chocolat."
    goumi vide "Votre commande est prête."
    "Un compartiment du comptoir s'ouvre. Le robot présente une petite coupelle contenant une pâte grisâtre."
    elen vide "Ah... C'est quoi, exactement ?"
    goumi vide "Préparation nutritionnelle complète. Apport équilibré en protéines, lipides, glucides, vitamines et minéraux."
    noam vide "C'est censé être un dessert ou du ciment ?"
    goumi vide "Cette préparation ne contient aucun matériau de construction."
    elen vide "Très rassurant. Bon, allez, goûte, toi."
    noam vide "Pourquoi moi ?!"
    elen vide "Parce que tu viens d'arriver et que tu n'as pas encore eu le temps de me dire non !"
    "Je prends une toute petite bouchée. La texture est étrange, et je dois faire un effort pour ne pas grimacer."
    noam vide "Je crois que mon moral vient de baisser."
    goumi vide "Analyse nutritionnelle : objectif atteint à cent pour cent."
    elen vide "Ah bah super ! On est malheureux, mais en parfaite santé !"
    "Elle éclate de rire et repose la coupelle hors de portée."

    scene bg_cg008_1 at adaptive_fullscreen with fade
    noam vide "Tu peux lui demander de nous faire quelque chose de vraiment bon, plutôt ?"
    elen vide "Avec plaisir. Et cette fois, je vais être très précise."
    goumi vide "Je suis Goumi, unité culinaire autonome. Toutes les recettes réalisables à partir des stocks peuvent être demandées."
    $ unlock_character_name("goumi")
    elen vide "Goumi, deux parts de gâteau au chocolat. Un vrai gâteau, avec du sucre, pas une pâte qui ressemble à du mastic."
    goumi vide "Demande acceptée. Deux parts de gâteau au chocolat en préparation."
    noam vide "Tu vois, il suffisait de demander."
    elen vide "Tu dis ça maintenant ? Après m'avoir laissée lui faire confiance ?"

    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_329
    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elen", "neutre", 0.50),
        ("goumi", "vide", 0.78),
    ])

    elen sourire "Au fait, moi c'est Elen. J'ai tellement passé de temps à discuter avec ce truc que j'en ai oublié de me présenter."
    $ unlock_character_name("elen")
    call kd_play_character_intro("elen") from _call_kd_intro_elen_j1
    noam sourire "Noam. Et lui, c'est Goumi, le chef qui sait nous nourrir sans nous donner envie de recommencer."
    goumi vide "Je suis conçu pour satisfaire toutes les demandes alimentaires compatibles avec les réserves disponibles."
    elen rire "Alors commence par apprendre le mot « plaisir », ça te fera pas de mal."
    goumi vide "Je ne peux pas éprouver de plaisir."
    elen taquin "Oui, on avait remarqué."

    "Quelques instants plus tard, le compartiment s'ouvre sur deux parts de gâteau, cette fois parfaitement appétissantes."
    goumi vide "Commande terminée. Je vous rappelle que mes horaires de service sont de six heures à quatorze heures, puis de dix-sept heures à vingt-deux heures."
    noam surpris "Il a vraiment des horaires, lui ?"
    elen sourire "Oui, monsieur tient à sa recharge. On dirait presque qu'il est syndiqué."
    "Je goûte le gâteau. Il est étonnamment bon, ce qui me pousse à regarder Goumi avec un peu plus de respect."
    noam sourire "Bon, je retire une partie de ce que j'ai dit. Ça, c'est réussi."
    goumi vide "Votre appréciation a été enregistrée."
    elen content "Tu vois ! On va peut-être réussir à passer un mois sans manger de la bouillie."
    "Son sourire s'atténue légèrement lorsqu'elle prononce ces mots. Elle reprend vite une autre bouchée."
    elen sourire "Enfin... une journée à la fois, hein ? Ça sera déjà pas mal."
    noam neutre "Oui. Ça me va."
    elen taquin "Et la prochaine fois, je te laisse choisir le menu. Mais je garde le droit de goûter avant toi."
    noam rire "Quel courage."
    "Goumi récupère la coupelle grise pendant que nous terminons le gâteau. Pour une fois depuis notre arrivée, j'ai presque l'impression de passer une pause normale."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_1
    $ hideGroup()
    jump CAFETERIA_TP
