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



    if free_time_active and sael_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform("images/character/sael/neutre.png", zoom=0.75)
            hover Transform("images/character/sael/raison.png", zoom=0.75)
            focus_mask True
            xalign 0.76
            yalign 0.30
            action [SetVariable("last_room_label", "LIVRAISON_TP"), Jump("SAEL_LINK_INTERACT")]
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

    noam hesitation "…"
    noam hesitation "Euh…"
    noam hesitation "Salut."

    mara jaloux "Hein ?"
    mara taquin "Putain, c’est toi qui traînes ici ?"
    mara sourire "Salut, le stalker."

    pause 0.2

    noam taquin "Hein ?!"
    noam reflexion "Désolé, je voulais pas te faire peur."
    noam reflexion "C’est juste que…"
    noam reflexion "je pensais pas tomber sur quelqu’un ici."

    mara doute "Ouais…"
    mara "Les gens passent, matent la porte deux secondes,"
    mara "captent que c’est fermé à double tour,"
    mara "et se barrent direct comme des rats."
    mara taquin "Ils ont pas les couilles de rester."

    noam sourire "Et toi ?"

    mara sourire "Moi je reste."
    mara "J’aime bien savoir exactement comment tout peut partir en vrille."
    mara "Rien de tel que de connaître chaque recoin pourri d’un endroit."
    mara taquin "Ça permet de mieux anticiper le moment où ça va chier."

    pause 0.3

    noam neutre "J'imagine que tu viens d'Axiome alors ?"
    noam neutre "Moi c'est Noam."
    noam neutre "District HARMONIE."

    mara neutre "Mara."
    mara sourire "Et ouais, bingo : Axiome pur jus."

    noam taquin "Ah."
    noam taquin "D'où le côté un peu professionnel."

    mara rire "Seulement un peu ?"

    pause 0.3

    "Je m’approche d’une caisse."
    "Elle est lourde."
    "Même sans l’ouvrir, on le sent."

    noam reflexion "Tu crois que ce sas sera utile ?"

    mara doute "Euh… ouais."
    mara "Normalement, les livraisons tombent une fois par semaine."
    mara reflexion "C’est huilé au millimètre : J7, J14, J21, J28."
    mara "Toujours pile à la même heure, comme des horloges suisses."
    mara taquin "Très rassurant, hein ?"

    noam surpris "Ils ont déjà prévu tout ça ?"
    noam surpris "Genre…"
    noam surpris "jusqu’à la fin du Conclave ?"

    mara doute "Au moins on est surs d'avoir des livraisons régulièrement."

    pause 0.3

    $ showP("noam", "reflexion", 0.22)
    think "Même la nourriture arrive sous calendrier strict."

    $ showP("noam", "sourire", 0.22)
    noam "C’est con, mais…"
    noam "savoir que ça arrive toutes les semaines, ça rassure."

    mara stress "Ouais… c’est exactement pour ça que ça me fout les jetons."

    pause 0.3

    $ showP("noam", "inquiet", 0.22)
    noam "Pourquoi ?"

    mara "Parce que si un truc déconne…"
    mara "si on a besoin d’un médoc, de bouffe en plus, d’un câble USB ou que sais-je…"
    mara "bah on attend sagement le prochain jour J."
    mara doute "Et si c’est pas le bon jour… on crève la dalle ou on crève tout court."
    mara sourire "Super planning, Kami. Vraiment top."
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