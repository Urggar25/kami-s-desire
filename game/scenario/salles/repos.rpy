default decouverte_salle_repos = False

label REPOS_TP:
    scene bg_repos at adaptive_fullscreen

    if not decouverte_salle_repos:
        jump decouverte_salle_repos

    $ pnc_room = "pnc_repos"
    call screen pnc_repos()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_repos():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_repos.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_repos/babyfoot.png"
        hover "images/background/interact/salle_repos/babyfoot_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_PNC_BABYFOOT")

    imagebutton:
        idle "images/background/interact/salle_repos/flechettes.png"
        hover "images/background/interact/salle_repos/flechettes_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_PNC_FLECHETTES")

    imagebutton:
        idle "images/background/interact/salle_repos/arcade.png"
        hover "images/background/interact/salle_repos/arcade_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_PNC_ARCADE")

    imagebutton:
        idle "images/background/interact/salle_repos/distributeur.png"
        hover "images/background/interact/salle_repos/distributeur_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_PNC_DISTRIBUTEUR")

    imagebutton:
        idle "images/background/interact/salle_repos/canape.png"
        hover "images/background/interact/salle_repos/canape_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("REPOS_PNC_CANAPE")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")

    if free_time_active and mara_link in [1, 3]:
        imagebutton:
            idle Transform("images/character/mara/sourire.png", zoom=0.75)
            hover Transform("images/character/mara/neutre.png", zoom=0.75)
            focus_mask True
            xalign 0.15
            yalign 0.30
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("MARA_LINK_INTERACT")]

    if free_time_active and lysa_link == 0:
        imagebutton:
            idle Transform("images/character/lysa/taquin.png", zoom=0.75)
            hover Transform("images/character/lysa/neutre.png", zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "REPOS_TP"), Jump("LYSA_LINK_INTERACT")]


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

    $ showP("noam", "reflexion", 0.22)

    "Un claquement sec résonne."
    "Une balle de babyfoot tape contre la paroi."
    
    hide noam
    
    scene bg_cg007 at adaptive_fullscreen with fade
    $ showP("noam", "vide", 0.1)
    $ showP("iris", "vide", 0.9)
    $ showP("julian", "vide", 0.5)
    
    "Il y a de l'animation dans la pièce."
    "Une animation difficile à rater."
    
    play sound sfx_balle volume 3.0

    julian "Hé hé ! Encore un but."

    noam "Ah."

    julian "T’as vu ?"
    julian "Même pas besoin d’échauffement."
    julian "Je te bats quand tu veux !"

    noam "Je viens d’arriver, laisse moi le temps."

    julian "C’est suffisant. T'as eu 3 secondes pour te préparer !"


    iris "Ignore-le."
    iris "Plus tu réponds, plus il parle."

    julian "C’est faux."
    julian "Je parle aussi très bien tout seul."

    noam "Vous vous connaissez ?"

    iris "Malheureusement."

    scene bg_repos at adaptive_fullscreen with fade
    
    $ showP("julian", "sourire", 0.78)
    $ showP("iris", "taquin", 0.50)

    julian "Hey."
    julian "On a survécu à trois réunions ensemble."
    julian "Ça crée des liens, inévitablement."

    iris "Crois moi, ça crée surtout des migraines."

    $ showP("julian", "taquin", 0.78)
    julian "Iris."
    julian "Fais pas gaffe, elle est toujours comme ça."
    julian "Toujours aussi chaleureuse."
    
    iris "Non. Juste avec toi."

    $ showP("noam", "sourire", 0.22)
    noam "Moi c'est Noam."

    julian "Julian."
    julian "Et oui, avant que tu demandes :"
    julian "Je suis à peu près bon dans quasiment tous les domaines."

    iris "Et allez c'est reparti ..."

    pause 0.2

    "Julian relance la balle."
    "Elle roule."
    "Il marque encore."

    $ showP("julian", "joie", 0.78)
    julian "Voilà."
    julian "Le Conclave peut attendre."

    $ showP("iris", "inquiet", 0.50)
    iris "Non."
    iris "T'as beau dire qu'il attendra, ça m'étonnerait que Kami change les règles pour tes beaux yeux."
    
    $ showP("julian", "taquin", 0.78)
    julian "Même toi tu confirmes que j'ai des beaux yeux."
    
    $ showP("iris", "taquin", 0.50)
    iris "Par pitié, oublie ce que j'ai dis."

    pause 0.2

    $ showP("noam", "reflexion", 0.22)
    noam "Ça vous dérange pas ?"
    noam "Qu’il y ait… tout ça."

    "Je désigne la salle."
    "Les jeux."
    "Le confort."

    $ showP("iris", "reflexion", 0.50)
    iris "Ils ont le sens du détail. Des babyfoot à quelques dizaines de mètres d'un canon qui a tué des millions de personne."
    iris "Mais bon je préfère être là. C'est au moins un peu plus chaleureux."

    $ showP("julian", "neutre", 0.78)
    julian "Moi je trouve ça honnête."
    julian "Ils savent qu’on risque de craquer-"
    julian "Enfin, que vous risquiez de craquer."
    julian "Alors ils n... vous donnent de quoi tenir."

    $ showP("noam", "hesitation", 0.22)
    noam "Tenir jusqu’à quoi ?"

    julian "Jusqu’au prochain vote."
    julian "Puis le suivant."
    julian "Et encore après."

    $ showP("iris", "triste", 0.50)
    iris "Tu dis ça trop calmement."
    iris "Faut dire que ça ne te ressemble pas."

    play sound sfx_balle volume 3.0
    julian "Je suis concentré sur ma partie."

    iris "Évidemment."
    iris "Contre ton ennemi imaginaire."

    pause 0.3

    "Iris s’enfonce un peu plus dans le canapé."
    "Elle regarde le plafond."

    $ showP("iris", "fatigue", 0.50)
    iris "Il a toujours été comme ça avant."
    iris "Toujours à faire le malin."
    iris "Toujours à détourner l’attention."

    $ showP("julian", "sourire", 0.78)
    julian "Et pourtant t’es là."

    iris "Parce que j’avais pas le choix."

    $ showP("noam", "reflexion", 0.22)
    think "Personne n’a vraiment le choix ici."

    pause 0.3

    $ showP("noam", "neutre", 0.22)
    noam "Bon."
    noam "Je vais continuer à faire le tour."

    $ showP("julian", "taquin", 0.78)
    play sound sfx_balle volume 2.0
    julian "Quand tu veux perdre au babyfoot, tu sais où me trouver."

    $ showP("iris", "sourire", 0.50)
    iris "Ou quand t’auras besoin de silence, ne viens pas ici du coup."
    iris "Je devrais peut être aller aux archives, il n'y aura pas ce casse pied."

    $ showP("noam", "sourire", 0.22)
    noam "Je retiens."
    
    call CHECK_ALL_SALLES_VISITEES

    jump REPOS_TP

# 1m45
# Total : 38m05
