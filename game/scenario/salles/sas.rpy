# -----------------------------------------------------------------------
# SAS DE LIVRAISON — même modèle que CANON
# - 2 persos seulement : Noam + Mara
# - Découverte : logistique, livraisons régulières
# - PNC : porte du sas / caisses / combinaisons / terminal / retour
# -----------------------------------------------------------------------

default decouverte_sas = False


label LIVRAISON_TP:
    scene bg_sas at adaptive_fullscreen

    if not decouverte_sas:
        jump decouverte_sas

    $ pnc_room = "pnc_livraison"
    call screen pnc_livraison()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_livraison():

    modal True
    zorder 200

    add Solid("#000")

    add "images/background/bg_sas.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    imagebutton:
        idle "images/background/interact/livraison/porte.png"
        hover "images/background/interact/livraison/porte_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("LIV_PNC_PORTE")

    imagebutton:
        idle "images/background/interact/livraison/caisses.png"
        hover "images/background/interact/livraison/caisses_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("LIV_PNC_CAISSES")

    imagebutton:
        idle "images/background/interact/livraison/combinaisons.png"
        hover "images/background/interact/livraison/combinaisons_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("LIV_PNC_COMBIS")

    imagebutton:
        idle "images/background/interact/livraison/terminal.png"
        hover "images/background/interact/livraison/terminal_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("LIV_PNC_TERMINAL")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


label LIV_PNC_PORTE:
    window auto

    "La porte du sas occupe tout le mur du fond."
    "Elle est épaisse, renforcée, bardée de verrous et de pictogrammes jaunes."
    "Même fermée, elle donne l’impression d’être en tension."
    "Comme si quelque chose, de l’autre côté, appuyait déjà."

    think "C’est pas une porte qu’on ouvre."
    think "C’est une porte qu’on autorise."

    jump LIVRAISON_TP


label LIV_PNC_CAISSES:
    window auto

    "Les caisses sont disposées avec une précision presque maniaque."
    "Toutes de la même taille."
    "Toutes marquées."
    "Certaines ont des traces d’impact, des coins râpés, des éraflures profondes."
    "D’autres sont encore trop propres pour être honnêtes."

    think "Elles n’ont pas été fabriquées ici."
    think "Elles ont voyagé."
    think "Et elles voyageront encore."

    jump LIVRAISON_TP


label LIV_PNC_COMBIS:
    window auto

    "Trois combinaisons pressurisées sont suspendues dans un renfoncement."
    "Alignées."
    "Silencieuses."
    "Les casques noirs reflètent la lumière bleutée du sas."

    think "On ne montre pas ce genre de choses si on n’envisage pas de s’en servir."
    think "Pas ici."

    jump LIVRAISON_TP


label LIV_PNC_TERMINAL:
    window auto

    "Un terminal logistique est fixé au mur."
    "L’écran est déjà allumé."
    "Pas de mot de passe."
    "Juste une interface froide, directe."

    "Je fais défiler."
    "Dates."
    "Statuts."
    "Réceptions prévues."

    "J7."
    "J14."
    "J21."
    "J28."

    think "Une livraison par semaine."
    think "Même ça, c’est ritualisé."

    jump LIVRAISON_TP


label LIV_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_sas:

    $ decouverte_sas = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "Sas de livraison."
    think "Pourquoi les livraisons auraient-elles besoin de passer par un sas ?"
    think "Comme si les livraisons pouvaient être toxiques ou infectées."

    pause 0.4

    scene bg_sas at adaptive_fullscreen with fade

    "La pièce est vaste, froide, presque clinique."
    "Le sol reflète les lumières bleues du plafond."
    "Tout est net."
    "Trop net."

    "Des caisses longent les murs."
    "Des machines de contrôle bourdonnent doucement."
    "Et au fond, il y a cette porte."
    "Impossible à ignorer."

    $ showP("noam", "reflexion", 0.22)
    think "Ils ont vraiment pensé à tout."
    think "Même à la façon dont on allait oublier qu’on dépend d’eux."

    "Près de la porte, quelqu’un est déjà là."
    "Une femme."
    "Immobile."
    "Bras croisés."
    "Le regard fixé sur le sas, comme si elle attendait qu’il fasse une erreur."

    $ showP("mara", "mefiant", 0.78)

    $ showP("noam", "hesitation", 0.22)
    noam "…"
    noam "Euh…"
    noam "Salut."

    $ showP("mara", "jaloux", 0.78)
    mara "Hein ?"
    mara "Ah—"
    $ showP("mara", "neutre", 0.78)
    mara "Salut."

    pause 0.2

    $ showP("noam", "reflexion", 0.22)
    noam "Je voulais pas te faire peur."
    noam "C’est juste que…"
    noam "je pensais pas tomber sur quelqu’un ici."

    $ showP("mara", "doute", 0.78)
    mara "Ouais."
    mara "En général, les gens passent vite."
    mara "Ils regardent la porte."
    mara "Ils comprennent."
    mara "Et ils repartent."

    $ showP("noam", "sourire", 0.22)
    noam "Et toi ?"

    $ showP("mara", "stress", 0.78)
    mara "Moi je reste."
    mara "J’aime bien savoir comment les choses peuvent mal tourner."
    mara "Rien de mieux que de connaître parfaitement les lieux pour ça."

    pause 0.3

    $ showP("noam", "neutre", 0.22)
    noam "J'imagine que tu viens d'Axiome alors ?"
    
    noam "Moi c'est Noam."
    noam "District HARMONIE."

    $ showP("mara", "neutre", 0.78)
    mara "Mara."
    mara "Et Bingo, je viens bien d'Axiome."

    $ showP("noam", "taquin", 0.22)
    noam "Ah."
    noam "D'où le côté un peu professionnel."

    $ showP("mara", "rire", 0.78)
    mara "Seulement un peu ?"

    pause 0.3

    "Je m’approche d’une caisse."
    "Elle est lourde."
    "Même sans l’ouvrir, on le sent."

    $ showP("noam", "reflexion", 0.22)
    noam "Tu crois que ce sas sera utile ?"

    $ showP("mara", "doute", 0.78)
    mara "Euh…"
    mara "Ouais."
    mara "Les livraisons devraient normalement arriver une fois par semaine."

    $ showP("mara", "reflexion", 0.78)
    mara "C’est réglé à la perfection."
    mara "J7, J14, J21, J28."
    mara "Toujours à la même heure apparemment."

    $ showP("noam", "surpris", 0.22)
    noam "Ils ont déjà prévu tout ça ?"
    noam "Genre…"
    noam "jusqu’à la fin du Conclave ?"

    $ showP("mara", "doute", 0.78)
    mara "Au moins on est surs d'avoir des livraisons régulièrement."

    pause 0.3

    $ showP("noam", "reflexion", 0.22)
    think "Même la nourriture arrive sous calendrier strict."

    $ showP("noam", "sourire", 0.22)
    noam "C’est con, mais…"
    noam "savoir que ça arrive toutes les semaines, ça rassure."

    $ showP("mara", "stress", 0.78)
    mara "Ouais."
    mara "C’est exactement pour ça que ça m’angoisse."

    pause 0.3

    $ showP("noam", "inquiet", 0.22)
    noam "Pourquoi ?"

    $ showP("mara", "reflexion", 0.78)
    mara "Parce que ça veut aussi dire que si on a le moindre soucis…"
    mara "On ne pourra être livré que lors de ces jours particuliers."

    pause 0.4

    "Je regarde la porte."
    "Puis les combinaisons."
    "Puis les caisses."

    think "Même l’espoir arrive emballé."

    pause 0.4

    $ showP("noam", "reflexion", 0.22)
    think "Je devrais aller voir ailleurs."

    call CHECK_ALL_SALLES_VISITEES

    jump LIVRAISON_TP

# 1m20
# Total : 52m45