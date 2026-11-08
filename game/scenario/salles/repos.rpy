default decouverte_salle_repos = False
default repos_table_seen = False
default repos_party_active = False

init python:
    REPOS_TABLE_BONUS_CHANCE = 0.20

    def repos_table_bonus_label():
        # La scène sera ajoutée plus tard sous ce label. Tant qu'elle
        # n'existe pas, le repos se termine normalement.
        label_name = "repos_table_bonus_scene"
        if not renpy.has_label(label_name):
            return None
        if renpy.random.random() < REPOS_TABLE_BONUS_CHANCE:
            return label_name
        return None


label REPOS_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_345
    scene bg_repos at adaptive_fullscreen

    if not decouverte_salle_repos and day_number() == 1:
        jump decouverte_salle_repos

    $ pnc_room = "pnc_repos"
    call screen pnc_repos()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_repos():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("repos")
    use room_scene_interactions("repos")

    if social_free_time_active() and character_has_available_free_time("iris"):
        imagebutton:
            idle Transform(character_image("iris", "colere"), zoom=1.00)
            hover Transform(character_image("iris", "taquin"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action [SetVariable("last_room_label", "REPOS_TP"), SetVariable("free_time_selected_character", "iris"), Jump("FREE_TIME_CHARACTER_INTERACT")]




label REPOS_PNC_BABYFOOT:
    "Le babyfoot brille trop."
    "Comme s’il n’avait jamais vu une main humaine."
    think "Ils ont pensé à tout… sauf à la partie où on respire."
    jump REPOS_TP


label REPOS_PNC_FLECHETTES:
    "Un jeu de fléchettes."
    "Aimanté, sécurisé."
    "Même se détendre ici a l’air réglementé."
    jump REPOS_TP


label REPOS_PNC_ARCADE:
    "Une borne d’arcade."
    "Écran intact."
    "Liste de jeux préchargés."
    think "Au moins, ils ne nous demandent pas de voter pour débloquer le niveau 2."
    jump REPOS_TP


label REPOS_PNC_DISTRIBUTEUR:
    "Un distributeur de boissons."
    "Pas de prix."
    "Pas de monnaie."
    "Juste un choix."
    think "La seule chose gratuite, ici : l’illusion du choix."
    jump REPOS_TP


label REPOS_PNC_CANAPE:
    "Le canapé est large."
    "Trop propre."
    "Les coussins sont alignés au millimètre."
    think "Même le confort a un protocole."
    jump REPOS_TP


label repos1_babyfoot:
    jump REPOS_PNC_BABYFOOT


label repos1_flechette:
    jump REPOS_PNC_FLECHETTES


label repos1_distributeur:
    if cafeteria_food_visible_count() <= 0:
        "Le distributeur est vide. Pas même une ration oubliée au fond."
        think "Les stocks de la cafétéria ont donc fini par atteindre jusqu'ici."
    elif cafeteria_food_visible_count() < 5:
        "Le distributeur n'est plus rempli qu'à moitié."
        "Les choix se réduisent au même rythme que les réserves."
    else:
        "Le distributeur est plein. Boissons et rations sont encore soigneusement alignées."
        think "Pour le moment, personne n'a besoin de compter ce qu'il prend."
    jump REPOS_TP


label repos1_porte_couloir_cafeteria:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label repos2_television:
    if day_number() == 6 and social_free_time_active() and not j601_border_news_seen:
        call _6_0_1_TV_FRONTIERES from _call_j601_tv_frontieres_repos
        jump REPOS_TP

    "L'écran occupe une bonne partie du mur."
    "Une sélection de films, de jeux et d'archives tourne silencieusement."
    think "Même les distractions ont été choisies avant notre arrivée."
    jump REPOS_TP


label repos2_table_repos:
    if not repos_table_seen:
        $ repos_table_seen = True
        think "Je pourrai me reposer ici quand j'aurai du temps libre."

    if social_free_time_active():
        menu:
            "Me reposer jusqu'à la fin de ce temps libre ?"
            "Oui":
                $ repos_bonus_label = repos_table_bonus_label()
                if repos_bonus_label:
                    call expression repos_bonus_label from _call_expression_3
                jump FREE_TIME_END
            "Non":
                jump REPOS_TP

    think "Ce n'est pas le moment de m'installer."
    jump REPOS_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label REPOS_PNC_EXIT:
    return
    
label decouverte_salle_repos:
    $ decouverte_salle_repos = True
    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "J'entends du bruit derrière la porte de la salle de repos. Au moins, il y a déjà des gens qui essaient de s'occuper."
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_346
    scene bg_repos at adaptive_fullscreen with fade
    "Un baby-foot occupe le centre de la pièce. Un garçon fait tourner les poignées avec beaucoup trop d'enthousiasme pendant qu'une fille le regarde, manifestement à bout de patience."
    scene bg_cg007 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg007")
    play sound sfx_balle volume 3.0
    julian vide "Et voilà ! Encore un but splendide. Vous avez tous été témoins, j'espère."
    iris vide "T'as surtout marqué contre personne. Ça fait une différence."
    noam vide "Je peux confirmer que le gardien avait l'air complètement dépassé."
    julian vide "Enfin un connaisseur ! Viens, je vais te montrer ce que ça donne avec un adversaire."
    iris vide "Fais attention. Il va commenter chacun de ses tirs."
    noam vide "Je m'en remets à ton jugement, alors."
    "Je prends les poignées de l'autre côté. Julian engage immédiatement, beaucoup trop sûr de lui."
    play sound sfx_balle volume 2.0
    julian vide "Tu vois, l'important, c'est d'anticiper. Regarde bien mon prochain mouvement."
    noam vide "Celui-là ?"
    "Je récupère la balle et marque avant qu'il ait terminé son explication."
    iris vide "Oh, magnifique. Tu peux nous refaire la démonstration, Julian ?"
    julian vide "Un accident de parcours. Je voulais simplement tester ses réflexes."
    noam vide "Ça tombe bien, ils fonctionnent."
    call MAYBE_PLAY_SCRIPTED_DOOR("repos", "bg_repos") from _call_MAYBE_PLAY_SCRIPTED_DOOR_347
    scene bg_repos at adaptive_fullscreen with fade
    $ showGroup([
        ("julian", "sourire", 0.22),
        ("iris", "taquin", 0.50),
        ("noam", "sourire", 0.78),
    ])
    julian sourire "Julian, au fait. Je préfère que tu connaisses le nom du type qui va prendre sa revanche."
    $ unlock_character_name("julian")
    noam taquin "Noam. J'espère que tu encaisses aussi bien les défaites que tu annonces les victoires."
    iris taquin "Tu vas vite comprendre. Moi c'est Iris, et j'ai déjà assez entendu parler de ses exploits pour aujourd'hui."
    $ unlock_character_name("iris")
    julian taquin "Ne fais pas attention. Elle me critique parce qu'elle sait que je suis indispensable à cette salle."
    iris colere "Indispensable ? T'es surtout la raison pour laquelle j'ai besoin d'une salle insonorisée."
    noam rire "Vous vous connaissez depuis longtemps ?"
    iris blase "Assez pour savoir qu'il faut jamais lui laisser un public."
    julian sourire "Et pourtant, elle revient toujours. Je dois avoir un certain charme."
    iris taquin "Ou alors je surveille le matériel, au cas où tu casserais quelque chose."
    "Julian reprend les poignées en essayant de retrouver sa dignité. Iris s'assied sur le canapé voisin."
    julian neutre "Bon, une dernière. Cette fois, on joue sérieusement."
    noam taquin "Tu jouais pas sérieusement avant ?"
    julian taquin "J'étais en phase d'observation. C'est une technique très avancée."
    play sound sfx_balle volume 2.0
    "Nous échangeons quelques balles. Julian finit par marquer et lève les bras comme s'il venait de gagner un championnat."
    julian joie "Ah ! Voilà, le talent finit toujours par parler."
    iris blase "On t'a entendu. Tout le couloir aussi, probablement."
    noam sourire "Bon, un partout. On pourra régler ça une autre fois."
    iris inquiet "Au fait, Noam, ça va depuis le réveil ? T'as l'air un peu pâle."
    noam neutre "J'ai encore la tête lourde, mais ça va."
    iris reflexion "Si ça passe pas, va à l'infirmerie. Ce serait idiot de faire un malaise juste pour lui donner un nouveau public."
    julian surpris "Comment ça, un nouveau public ?"
    iris taquin "Les gens qui viendront te ramasser."
    noam rire "D'accord, je ferai attention."
    julian sourire "Et quand tu seras remis, je t'attends pour la belle."
    noam taquin "Tu peux déjà commencer à t'entraîner."
    "Julian replace la balle au centre. Iris lève les yeux au ciel, mais elle sourit quand même."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_7
    $ hideGroup()
    jump REPOS_TP
