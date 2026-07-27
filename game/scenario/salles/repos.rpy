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
    scene bg_repos at adaptive_fullscreen

    if not decouverte_salle_repos and day_number() == 1:
        jump decouverte_salle_repos

    if social_free_time_active() and free_time_round == 1 and not seen_voyeur_julian_iris:
        jump temps_libre_salle_repos

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

    if social_free_time_active() and mara_link in [1, 3]:
        imagebutton:
            idle Transform(character_image("mara", "sourire"), zoom=0.75)
            hover Transform(character_image("mara", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.15
            yalign 0.30
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("MARA_LINK_INTERACT")]

    if social_free_time_active() and lysa_link == 0:
        imagebutton:
            idle Transform(character_image("lysa", "taquin"), zoom=0.75)
            hover Transform(character_image("lysa", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("LYSA_LINK_INTERACT")]

    if social_free_time_active() and iris_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform(character_image("iris", "colere"), zoom=0.75)
            hover Transform(character_image("iris", "taquin"), zoom=0.75)
            focus_mask True
            xalign 0.50
            yalign 0.31
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("IRIS_LINK_INTERACT")]


    if social_free_time_active() and elen_link == 4:
        imagebutton:
            idle Transform(character_image("elen", "joie"), zoom=0.75)
            hover Transform(character_image("elen", "content"), zoom=0.75)
            focus_mask True
            xalign 0.68
            yalign 0.30
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("ELEN_LINK_INTERACT")]



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
                    call expression repos_bonus_label
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
    play music "music/bgm_careful_wanting.mp3" fadein 1.0

    think "Ici, il y a une salle de repos."
    think "J’aurais presque envie d’y aller pour souffler et me remettre de mes émotions."

    pause 0.4

    scene bg_repos at adaptive_fullscreen with fade

    "La pièce semble étonnamment vivante."
    "Des jeux."
    "Un canapé."
    "Un distributeur."

    think "Quoi qu'on pense de notre situation, l'attention est louable."

    "Un claquement sec résonne."
    "Une balle de babyfoot tape contre la paroi."

    scene bg_cg007 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg007")
    
    "Il y a de l'animation dans la pièce."
    "Une animation difficile à rater."
    
    play sound sfx_balle volume 3.0

    julian vide "Hé hé ! Encore un but."

    noam vide "Ah."

    julian vide "T’as vu ?"
    julian vide "Même pas besoin d’échauffement."
    julian vide "Je te bats quand tu veux !"

    noam vide "Je viens d’arriver, laisse moi le temps."

    julian vide "C’est suffisant. T'as eu 3 secondes pour te préparer !"


    iris vide "Ignore-le."
    iris vide "Plus tu réponds, plus il parle."

    julian vide "C’est faux."
    julian vide "Je parle aussi très bien tout seul."

    noam vide "Vous vous connaissez ?"

    iris vide "Malheureusement."
    $ hideGroup()

    scene bg_repos at adaptive_fullscreen with fade
    
    $ showGroup([
        ("julian", "sourire", 0.22),
        ("iris", "taquin", 0.50),
        ("noam", "sourire", 0.78),
    ])

    julian sourire "Hey."
    julian sourire "On a survécu à trois réunions ensemble."
    julian sourire "Ça crée des liens, inévitablement."

    iris taquin "Crois moi, ça crée surtout des migraines."

    julian taquin "Iris."
    julian taquin "Fais pas gaffe, elle est toujours comme ça."
    julian taquin "Toujours aussi chaleureuse."
    
    iris taquin "Non. Juste avec toi."

    noam sourire "Moi c'est Noam."

    julian taquin "Julian."
    julian taquin "Et oui, avant que tu demandes :"
    julian taquin "Je suis à peu près bon dans quasiment tous les domaines."

    iris taquin "Et allez c'est reparti ..."

    pause 0.2

    "Julian relance la balle."
    "Elle roule."
    "Il marque encore."

    julian joie "Voilà."
    julian joie "Le Conclave peut attendre."

    iris inquiet "Non."
    iris inquiet "T'as beau dire qu'il attendra, ça m'étonnerait que Kami change les règles pour tes beaux yeux."
    
    julian taquin "Même toi tu confirmes que j'ai des beaux yeux."
    
    iris taquin "Par pitié, oublie ce que j'ai dis."

    pause 0.2

    noam reflexion "Ça vous dérange pas ?"
    noam reflexion "Qu’il y ait… tout ça."

    "Je désigne la salle."
    "Les jeux."
    "Le confort."

    iris reflexion "Ils ont le sens du détail. Des babyfoot à quelques dizaines de mètres d'un canon qui a tué des millions de personne."
    iris reflexion "Mais bon je préfère être là. C'est au moins un peu plus chaleureux."

    julian neutre "Moi je trouve ça honnête."
    julian neutre "Ils savent qu’on risque de craquer-"
    julian neutre "Enfin, que vous risquiez de craquer."
    julian neutre "Alors ils n... vous donnent de quoi tenir."

    noam hesitation "Tenir jusqu’à quoi ?"

    julian neutre "Jusqu’au prochain vote."
    julian neutre "Puis le suivant."
    julian neutre "Et encore après."

    iris triste "Tu dis ça trop calmement."
    iris triste "Faut dire que ça ne te ressemble pas."

    play sound sfx_balle volume 3.0
    julian neutre "Je suis concentré sur ma partie."

    iris triste "Évidemment."
    iris triste "Contre ton ennemi imaginaire."

    pause 0.3

    "Iris s’enfonce un peu plus dans le canapé."
    "Elle regarde le plafond."

    iris fatigue "Il a toujours été comme ça avant."
    iris fatigue "Toujours à faire le malin."
    iris fatigue "Toujours à détourner l’attention."

    julian sourire "Et pourtant t’es là."

    iris fatigue "Parce que j’avais pas le choix."

    think "Personne n’a vraiment le choix ici."

    pause 0.3

    noam neutre "Bon."
    noam neutre "Je vais continuer à faire le tour."

    play sound sfx_balle volume 2.0
    julian taquin "Quand tu veux perdre au babyfoot, tu sais où me trouver."

    iris sourire "Ou quand t’auras besoin de silence, ne viens pas ici du coup."
    iris sourire "Je devrais peut être aller aux archives, il n'y aura pas ce casse pied."

    noam sourire "Je retiens."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_7

    $ hideGroup()
    jump REPOS_TP

# 1m45
# Total : 38m05
