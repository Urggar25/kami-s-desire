# -----------------------------------------------------------------------
# GYMNASE — même modèle que CANON
# - 2 persos seulement : Noam + Elias
# - Découverte : Elias s'entraîne / discussion légère
# - PNC : tapis / poids / vélo / ballon / retour
# -----------------------------------------------------------------------

default decouverte_gymnase = False


label GYMNASE_TP:
    scene bg_gymnase at adaptive_fullscreen

    if not decouverte_gymnase:
        jump decouverte_gymnase

    $ pnc_room = "pnc_gymnase"
    call screen pnc_gymnase()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_gymnase():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_gymnase.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/gymnase/tapis.png"
        hover "images/background/interact/gymnase/tapis_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("GYM_PNC_TAPIS")

    imagebutton:
        idle "images/background/interact/gymnase/banc.png"
        hover "images/background/interact/gymnase/banc_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("GYM_PNC_POIDS")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")

    if free_time_active and elias_link in [0, 2, 4]:
        imagebutton:
            idle "images/character/elias/neutre.png"
            hover "images/character/elias/ecoute.png"
            focus_mask True
            xalign 0.78
            yalign 0.78
            zoom 0.45
            action [SetVariable("last_room_label", "GYMNASE_TP"), Jump("ELIAS_LINK_INTERACT")]


label GYM_PNC_TAPIS:
    "Le tapis est encore tiède."
    "Quelqu'un a couru récemment."
    "Les réglages sont simples."
    "Vitesse. Inclinaison. Temps."
    think "Même ici, tout est calibré."
    jump GYMNASE_TP


label GYM_PNC_POIDS:
    "Des poids libres."
    "Des barres."
    "Des repères au sol comme dans une salle publique."
    "Mais tout est trop propre."
    "Trop rangé."
    think "On dirait un décor de pub."
    jump GYMNASE_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label GYM_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_gymnase:

    $ decouverte_gymnase = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "Il y a aussi un gymnase."
    think "Ils ont vraiment pensé à mettre de nombreuses salles différentes."

    pause 0.4

    scene bg_gymnase at adaptive_fullscreen with fade

    "Ça sent le caoutchouc."
    "Le produit de nettoyage aussi."
    "Comme partout dans les couloirs mais plus particulièrement là."

    "Un terrain est marqué sur le sol."
    "Il y a des tapis de courses, des machines et des poids parfaitement rangés."

    "Et au fond…"
    "Un type est en train de s'entraîner."

    $ showP("noam", "reflexion", 0.22)   # gauche
    $ showP("elias", "fatigue", 0.78)    # droite

    "Il fait une série."
    "Sans musique."
    "Sans parler."
    "Juste le bruit de sa respiration."
    "Et du métal."

    $ showP("noam", "hesitation", 0.22)
    noam "…"
    noam "Salut."

    $ showP("elias", "ecoute", 0.78)
    "Il termine sa lancée."
    "Repose la barre doucement."
    "Puis enfin, il me regarde."

    $ showP("elias", "neutre", 0.78)
    elias "Salut."

    $ showP("noam", "sourire", 0.22)
    noam "Je pensais être seul."
    noam "Visiblement non."

    $ showP("elias", "fatigue", 0.78)
    elias "J'aime le sport, ça m'évite de trop réflechir à tout ce qui peut se passer."

    $ showP("noam", "taquin", 0.22)
    noam "Ouais... J'imagine que c'est devenu une habitude depuis un an."

    $ showP("elias", "rire", 0.78)
    "Il rit de façon courte."

    $ showP("elias", "neutre", 0.78)
    elias "Oui. Mais pas spécialement à cause de Kami."
    elias "Sa méthode est dure, mais elle tient la route."
    elias "Avant, on pouvait se prendre une balle n'importe quand, ou partir de force sur une guerre."
    
    "Il marque une pause un instant."
    
    $ showP("elias", "jaloux", 0.78)
    elias "Est-ce qu'on vit moins bien qu'avant ?"
    elias "Perso, j'ai pas la réponse."
    elias "Alors je fais le taf. Le reste, c'est que du bruit dont je ne m'occupe pas vraiment."

    pause 0.2
    "Je ne sais pas vraiment quoi répondre."
    "D'un côté, il touche juste. Le monde est plus paisible qu'autrefois."
    "Mais d'un autre, la moindre erreur entraine la mort."
    "Pas une simple punition."
    "La mort quoi."

    $ showP("noam", "reflexion", 0.22)
    noam "Au fait, je m'appelle Noam."
    noam "Je viens du district HARMONIE."

    $ showP("elias", "ecoute", 0.78)
    "Il hoche la tête, comme si ça validait une info dans sa tête."

    $ showP("elias", "neutre", 0.78)
    elias "Elias."
    elias "AXIOME."

    $ showP("noam", "surpris", 0.22)
    noam "AXIOME…"
    noam "La Forge."

    $ showP("elias", "content", 0.78)
    elias "Ouais. Là où on fabrique la majorité des trucs pour tous les districts."

    "Il dit ça sans fierté particulière."
    "Mais il sait dans son timbre de voix que AXIOME est nécessaire à tout le monde."
    "D'un autre côté, chacun des districts est nécessaire aux autres."
    "C'est pour ça qu'ils ont été découpé ainsi. Pour empêcher les tensions et nous rendre tous dépendants des autres."

    $ showP("noam", "reflexion", 0.22)
    noam "Tu t'entraînes pour quoi ?"

    $ showP("elias", "rire", 0.78)
    elias "Pour dormir. Le sport aide à mieux dormir."
    elias "Je me dis qu'une petite session avant le rendez-vous à 18h serait pas trop mal."
    elias "J'espère juste qu'il y a de quoi se doucher."

    $ showP("noam", "rire", 0.22)
    noam "Ah."
    noam "La meilleure raison."

    pause 0.3

    "Je m'approche du terrain."
    "Je regarde les repères au sol."
    "Ça me rappelle l'école."
    "Ça me rappelle avant."

    $ showP("noam", "triste", 0.22)
    "Ça me rappelle qi'avant on était innocent et les problèmes nous passaient au dessus de la tête."

    $ showP("elias", "ecoute", 0.78)
    elias "Tu fais du sport, toi ?"

    $ showP("noam", "hesitation", 0.22)
    noam "Avant, oui j'en faisais parfois."
    noam "Mais ça fait un moment que j'en ai pas fait …"
    noam "Je sais plus trop ce que je fais, honnêtement."

    $ showP("elias", "fatigue", 0.78)
    elias "C'est pour ça que je continue."
    elias "Quand tout bouge, faut garder un repère."

    $ showP("elias", "neutre", 0.78)
    elias "C'est le principe."

    pause 0.2

    $ showP("noam", "taquin", 0.22)
    noam "Donc si je veux survivre ici…"
    noam "Je dois courir et soulever des trucs."

    $ showP("elias", "content", 0.78)
    elias "Et boire de l'eau."
    elias "Et respirer."
    elias "N'oublie pas, sinon merci les crampes !"

    $ showP("noam", "sourire", 0.22)
    noam "Merci docteur."

    $ showP("elias", "rire", 0.78)
    "Il souffle du nez."
    "Ça ressemble presque à un vrai rire."

    pause 0.3

    $ showP("elias", "ecoute", 0.78)
    elias "Tu sais ce qui est drôle ?"
    elias "Ils nous filent un gymnase."
    elias "Comme si on était en colonie."
    elias "On soit, c'est pas pour me déplaire. J'ai toujours voulu aller en colo."

    $ showP("noam", "reflexion", 0.22)
    noam "Ouais. Notre animateur est juste un peu plus cinglé que les autres."

    $ showP("elias", "neutre", 0.78)
    elias "Exactement."

    "Il regarde la machine de muscu."
    "Puis les lignes au sol."
    "Puis moi."

    $ showP("elias", "inquiet", 0.78)
    elias "Tu sais, ces 30 jours ici, ça va pas être simple."
    elias "On sera constamment sur nos gardes, pas que durant les votes."
    elias "On risque d'être fatigué, on risque d'être sur les nerfs."

    $ showP("noam", "inquiet", 0.22)
    noam "Tu crois que le sport change quelque chose ?"

    $ showP("elias", "neutre", 0.78)
    elias "Non. Pas forcément."
    elias "Mais ça permet au moins de se vider la tête."

    pause 0.3

    $ showP("noam", "reflexion", 0.22)
    "Je regarde le tapis puis les poids."

    think "Ils ne me font pas spécialement envie."
    think "Rien que l'idée d'avoir des courbatures me freine déjà."

    $ showP("noam", "hesitation", 0.22)
    noam "Bon, allez fais moi une démo, Sensei !"
    noam "Histoire de faire semblant d'être normal dans ce monde chelou."

    $ showP("elias", "content", 0.78)
    elias "Ok."
    elias "Mais tu m'écoutes hein."
    elias "Sinon tu vas te faire mal."

    $ showP("noam", "sourire", 0.22)
    noam "Promis."

    pause 0.4

    "Pendant quelques minutes…"
    "Il me montre les postures à adopter, le rythme de respiration à avoir."

    "C'est bête."
    "C'est simple."
    "Et mine de rien, ça fait quand même du bien."

    pause 1.0
    
    "Après une longue série d'exercices."

    $ showP("noam", "reflexion", 0.22)
    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES

    jump GYMNASE_TP

# Durée : 2m30
# Total : 49m15
