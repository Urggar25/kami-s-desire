default decouverte_salle_canon = False

label CANON_TP:
    scene bg_canon at adaptive_fullscreen
    
    if not decouverte_salle_canon:
        jump decouverte_salle_canon
        
    $ pnc_room = "pnc_canon"
    call screen pnc_canon()

# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_canon():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_canon.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_canon/canon.png"
        hover "images/background/interact/salle_canon/canon_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CANON_PNC_CANON")

    imagebutton:
        idle "images/background/interact/salle_canon/console.png"
        hover "images/background/interact/salle_canon/console_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CANON_PNC_CONSOLE")

    imagebutton:
        idle "images/background/interact/salle_canon/vitre.png"
        hover "images/background/interact/salle_canon/vitre_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CANON_PNC_VITRE")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")

label CANON_PNC_CANON:
    "Le canon est encore plus grand de près."
    "Des anneaux d’alimentation entourent son corps, comme des vertèbres."
    "Tout est propre."
    "Trop propre pour une arme qui tue."
    think "Même ici, ils ont pensé à l’esthétique."
    jump CANON_TP


label CANON_PNC_CONSOLE:
    "La console est verrouillée."
    "Des écrans affichent des graphiques, des flux, des lignes de paramètres."
    "Je reconnais quelques mots."
    "Charge."
    "Alignement."
    "Sécurité."
    "Et surtout… un statut."
    "\"PRÊT\"."
    think "Donc oui… il peut tirer. À tout moment."
    jump CANON_TP


label CANON_PNC_VITRE:
    "La vitre est épaisse, légèrement teintée."
    "Je pose la main dessus."
    "Froid immédiat."
    "Ça ne protège pas ceux dehors."
    "Ça protège ceux dedans."
    think "Ça protège le Conclave de ce que le canon fait."
    jump CANON_TP

# Optionnel : si tu ajoutes un bouton retour graphique
label CANON_PNC_EXIT:
    return

# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_canon:

    $ decouverte_salle_canon = True

    scene black
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0

    think "Ça fait même pas quelques dizaines de minutes."
    think "Même pas le temps de comprendre où on est."
    think "Et pourtant…"

    think "Il y a cette salle qui m'a intrigué depuis les couloirs."
    think "La salle du canon."

    pause 0.4

    scene bg_canon at adaptive_fullscreen with fade

    "La porte se referme derrière nous."
    "Un bruit étouffé."
    "Comme si la salle avalait le son."

    "Il fait un peu plus froid ici."
    "Pas un froid naturel."
    "Un froid réglé précisément."

    "Le canon est là."
    "Suspendu."
    "Immense."
    "Orienté vers le sol."

    "Sous lui, une fosse circulaire."
    "Entourée d’une vitre épaisse."
    "Trop épaisse pour rassurer."

    "Tout autour, des consoles."
    "Des écrans déjà allumés."
    "Pas en veille."
    "Actifs."

    # Entrée : Noam observe, Ryn est en mode "jauge"
    $ showP("noam", "reflexion", 0.78)   # droite
    $ showP("ryn", "determine", 0.22)    # gauche

    "Le gaçon râleur de tout à l'heure ralentit."
    "Il s’arrête avant moi."

    $ showP("ryn", "reflechit", 0.22)
    ryn "…"

    $ showP("noam", "reflexion", 0.78)
    noam "Ouais."
    noam "Moi aussi."

    $ showP("ryn", "reflechit", 0.22)
    ryn "Au fait…"
    ryn "Ryn."

    $ showP("noam", "surpris", 0.78)
    noam "Hein ?"

    $ showP("ryn", "neutre", 0.22)
    ryn "Mon prénom."
    ryn "On est deux dans une salle avec une arme géante, autant faire ça propre."

    $ showP("noam", "sourire", 0.78)
    noam "Noam."

    $ showP("ryn", "determine", 0.22)
    ryn "Ok."

    $ showP("ryn", "reflechit", 0.22)
    ryn "C’est donc ça."

    "Il ne crie pas."
    "Il ne jure pas."
    "Il observe."

    $ showP("ryn", "reflechit", 0.22)
    ryn "Je pensais que c’était…"
    ryn "Plus loin."
    ryn "Ou plus caché."

    $ showP("noam", "hesitation", 0.78)
    noam "Caché de quoi ?"

    $ showP("ryn", "determine", 0.22)
    ryn "De nous."

    "Il s’approche de la vitre."
    "Pas trop."
    "Juste assez pour voir le fond de la fosse."

    $ showP("ryn", "reflechit", 0.22)
    ryn "Ils l’ont mis au centre comme on expose un trophé."
    ryn "Comme un rappel."

    $ showP("noam", "reflexion", 0.78)
    noam "Un rappel de quoi ?"

    $ showP("ryn", "determine", 0.22)
    ryn "De ce qui arrive quand quelqu’un oublie les règles et de la domination de Kami."

    "Je regarde les écrans."
    "Des lignes de données."
    "Des flux."
    "Rien de compréhensible."

    $ showP("noam", "reflexion", 0.78)
    noam "Tu crois vraiment qu’il fonctionne déjà ?"
    noam "Je veux dire…"
    noam "On vient d’arriver."

    $ showP("ryn", "determine", 0.22)
    ryn "Justement."

    "Il se tourne vers moi."

    $ showP("ryn", "colere2", 0.22)
    ryn "Tu crois qu’ils ont attendu qu’on soit là pour l’allumer ?"
    ryn "C'est sans doute ce canon là qui nous tire dessus depuis un an."

    "Je n’aime pas sa réponse."
    "Parce qu’elle fait sens."

    $ showP("noam", "inquiet", 0.78)
    noam "Donc là, maintenant…"

    $ showP("ryn", "determine", 0.22)
    ryn "Là, maintenant, il est prêt."

    "Un silence."
    "Pas confortable."

    $ showP("noam", "hesitation", 0.78)
    noam "Tu penses qu’il a déjà servi aujourd’hui ?"

    $ showP("ryn", "fatigue", 0.22)
    ryn "…"
    ryn "Je sais pas."

    "Il hésite."
    "Vraiment."

    $ showP("ryn", "inquiet", 0.22)
    ryn "J’espère que non."

    play sound sfx_beep
    "-Bip-"

    play music "music/bgm_system_override.mp3" fadein 1.0
    "Un bip sec."
    "Quelque part dans la salle."

    $ showP("ryn", "surpris", 0.22)
    "Ryn se fige."

    $ showP("noam", "surpris", 0.78)
    noam "C’était quoi ?"

    $ showP("ryn", "inquiet", 0.22)
    ryn "T’as entendu."

    $ showP("noam", "desaccord", 0.78)
    noam "Oui mais—"

    $ showP("ryn", "colere", 0.22)
    ryn "Chut."

    play sound sfx_beep
    "-Bip-"

    "Un deuxième bip."
    "Plus long."

    "Les anneaux lumineux au sol s’allument."
    "Lentement."
    "Un cercle après l’autre."

    $ showP("noam", "inquiet", 0.78)
    noam "Ryn…"

    $ showP("ryn", "determine", 0.22)
    ryn "Quelqu’un a fait une connerie."

    $ showP("noam", "desaccord", 0.78)
    noam "Comment tu peux savoir ça ?"

    $ showP("ryn", "reflechit", 0.22)
    ryn "Parce que rien ici ne s’active pour rien."

    "Je sens mon estomac se nouer."
    "Ce n’est plus de la curiosité."
    "C’est de l’anticipation."

    $ showP("noam", "hesitation", 0.78)
    noam "Une connerie comment ?"

    $ showP("ryn", "fatigue", 0.22)
    ryn "Un refus."
    ryn "Une violence."
    ryn "Un mot de trop."
    ryn "J’en sais rien."

    "Il serre les poings."

    $ showP("ryn", "colere2", 0.22)
    ryn "Mais quelqu’un, quelque part…"
    ryn "Vient de sortir du cadre."

    play sound sfx_gresillement
    scene bg_canon at adaptive_fullscreen,heavy_shake

    "La salle vibre."
    "Très légèrement."

    "Le canon s’illumine."
    "Une lueur bleue apparaît en son centre."

    $ showP("noam", "peur", 0.78)      # droite
    $ showP("ryn", "surpris", 0.22)    # gauche

    play sound sfx_laser_canon volume 8.0

    $ showP("noam", "desespoir", 0.78)
    noam "Putain…"
    noam "C’est réel."

    $ showP("ryn", "desaccord", 0.22)
    ryn "T’en doutais ?"

    $ showP("noam", "triste", 0.78)
    noam "J’espérais."

    "Les écrans changent."
    "Un flux vidéo apparaît."
    "Brouillé."
    "Inexploitable."

    $ showP("noam", "panne", 0.78)
    noam "On voit rien."

    $ showP("ryn", "determine", 0.22)
    ryn "C’est fait exprès."

    "Un grondement sourd."
    "Comme un orage enfermé."

    $ showP("noam", "inquiet", 0.78)
    noam "On devrait partir."

    $ showP("ryn", "fatigue", 0.22)
    ryn "Ouais."

    "Aucun de nous ne bouge."

    "Le tir part."

    "Un rayon brutal."
    "Vertical."
    "Il frappe la fosse."

    "La lumière envahit la salle."
    "Blanche."
    "Aveuglante."

    scene bg_canon at adaptive_fullscreen,heavy_shake

    $ showP("noam", "desespoir", 0.78)
    $ showP("ryn", "surpris", 0.22)

    "Le sol tremble."
    "La vitre vibre."

    "Je recule d’un pas."
    "Cette fois sans réfléchir."

    "Puis plus rien."
    "Le rayon s’éteint."
    "D’un coup."

    pause 0.8

    "Les anneaux repassent au minimum."
    "La salle redevient calme."

    "Trop calme."

    $ showP("noam", "inquiet", 0.78)
    noam "…"
    noam "Quelqu'un vient de mourir."

    "Ryn ne répond pas tout de suite."

    $ showP("ryn", "colere", 0.22)
    ryn "Ouais."

    $ showP("noam", "triste", 0.78)
    noam "On ne sait même pas qui."

    $ showP("ryn", "fatigue", 0.22)
    ryn "Non."
    ryn "Mais Kami, si."

    "Il se détourne du canon."
    "Pour la première fois."

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    # Micro-shift : après le tir, Noam se recentre légèrement, Ryn se “referme”
    $ showP("noam", "reflexion", 0.70)
    $ showP("ryn", "fatigue", 0.30)

    ryn "Voilà."
    ryn "C’est ça, le Conclave."

    $ showP("noam", "reflexion", 0.70)
    noam "Une salle de réunion avec une arme."

    $ showP("ryn", "desaccord", 0.30)
    ryn "Non."
    ryn "Une arme avec une salle de réunion autour."
    ryn "Enfin, faut dire qu'il y a peu de chance qu'on fasse des réunions ici."

    $ showP("ryn", "jaloux", 0.30)
    ryn "C'est glauque."

    pause 0.5

    $ showP("ryn", "determine", 0.30)
    ryn "Et maintenant…"
    ryn "Chaque vote va avoir un poids."

    $ showP("noam", "raison", 0.70)
    noam "Parce qu’on saura ce qu’il y a derrière."

    $ showP("ryn", "reflechit", 0.30)
    ryn "Parce qu’on l’aura entendu."

    "Il me regarde."
    "Pas pour m’intimider."
    "Pour vérifier."

    $ showP("ryn", "inquiet", 0.30)
    ryn "Quand ça recommencera…"
    ryn "Tu feras semblant que t’as rien vu ?"

    $ showP("noam", "hesitation", 0.70)
    noam "…"

    $ showP("ryn", "determine", 0.30)
    ryn "Ou tu t’en souviendras ?"

    pause 0.4

    "Je n’ai pas de réponse à lui apporter."
    "Pas encore."
    "Nos choix peuvent avoir de véritables impacts ici."

    "Mais je sais une chose."
    "Je n’oublierai jamais ce bruit."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_2

    jump CANON_TP


#2m30
# total : 31m20