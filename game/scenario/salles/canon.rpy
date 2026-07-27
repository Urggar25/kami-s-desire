default decouverte_salle_canon = False

label CANON_TP:
    scene bg_canon at adaptive_fullscreen
    
    if not decouverte_salle_canon and day_number() == 1:
        jump decouverte_salle_canon
        
    $ pnc_room = "pnc_canon"
    call screen pnc_canon()

    if free_time_active:
        return
    if exploration_libre_active:
        return

# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_canon():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("canon")
    use room_scene_interactions("canon")


label canon1_ordinateur:
    jump CANON_PNC_CONSOLE


label canon1_porte_couloir_cafeteria:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label canon2_canon:
    jump CANON_PNC_CANON


label canon2_ciblage:
    "Une interface de ciblage recouvre tout un pan de la console."
    "Des coordonnées défilent lentement sous une grille verrouillée."
    "Chaque secteur habité possède déjà son repère, sa distance et son angle de tir."
    think "Ce n'est pas un système qu'on prépare en urgence."
    think "Tout est déjà mesuré. Il ne reste qu'à choisir où frapper."
    jump CANON_TP

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
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("ryn", "determine", 0.78),
    ])

    "Le gaçon râleur de tout à l'heure ralentit."
    "Il s’arrête avant moi."

    ryn reflechit "…"

    noam reflexion "Ouais."
    noam reflexion "Moi aussi."

    ryn reflechit "Au fait…"
    ryn reflechit "Ryn."

    noam surpris "Hein ?"

    ryn neutre "Mon prénom."
    ryn neutre "On est deux dans une salle avec une arme géante, autant faire ça propre."

    noam sourire "Noam."

    ryn determine "Ok."

    ryn reflechit "C’est donc ça."

    "Il ne crie pas."
    "Il ne jure pas."
    "Il observe."

    ryn reflechit "Je pensais que c’était…"
    ryn reflechit "Plus loin."
    ryn reflechit "Ou plus caché."

    noam hesitation "Caché de quoi ?"

    ryn determine "De nous."

    "Il s’approche de la vitre."
    "Pas trop."
    "Juste assez pour voir le fond de la fosse."

    ryn reflechit "Ils l’ont mis au centre comme on expose un trophé."
    ryn reflechit "Comme un rappel."

    noam reflexion "Un rappel de quoi ?"

    ryn determine "De ce qui arrive quand quelqu’un oublie les règles et de la domination de Kami."

    "Je regarde les écrans."
    "Des lignes de données."
    "Des flux."
    "Rien de compréhensible."

    noam reflexion "Tu crois vraiment qu’il fonctionne déjà ?"
    noam reflexion "Je veux dire…"
    noam reflexion "On vient d’arriver."

    ryn determine "Justement."

    "Il se tourne vers moi."

    ryn colere2 "Tu crois qu’ils ont attendu qu’on soit là pour l’allumer ?"
    ryn colere2 "C'est sans doute ce canon là qui nous tire dessus depuis un an."

    "Je n’aime pas sa réponse."
    "Parce qu’elle fait sens."

    noam inquiet "Donc là, maintenant…"

    ryn determine "Là, maintenant, il est prêt."

    "Un silence."
    "Pas confortable."

    noam hesitation "Tu penses qu’il a déjà servi aujourd’hui ?"

    ryn fatigue "…"
    ryn fatigue "Je sais pas."

    "Il hésite."
    "Vraiment."

    ryn inquiet "J’espère que non."

    play sound sfx_beep
    "-Bip-"

    play music "music/bgm_system_override.mp3" fadein 1.0
    "Un bip sec."
    "Quelque part dans la salle."

    "Ryn se fige."

    noam surpris "C’était quoi ?"

    ryn inquiet "T’as entendu."

    noam desaccord "Oui mais—"

    ryn colere "Chut."

    play sound sfx_beep
    "-Bip-"

    "Un deuxième bip."
    "Plus long."

    "Les anneaux lumineux au sol s’allument."
    "Lentement."
    "Un cercle après l’autre."

    noam inquiet "Ryn…"

    ryn determine "Quelqu’un a fait une connerie."

    noam desaccord "Comment tu peux savoir ça ?"

    ryn reflechit "Parce que rien ici ne s’active pour rien."

    "Je sens mon estomac se nouer."
    "Ce n’est plus de la curiosité."
    "C’est de l’anticipation."

    noam hesitation "Une connerie comment ?"

    ryn fatigue "Un refus."
    ryn fatigue "Une violence."
    ryn fatigue "Un mot de trop."
    ryn fatigue "J’en sais rien."

    "Il serre les poings."

    ryn colere2 "Mais quelqu’un, quelque part…"
    ryn colere2 "Vient de sortir du cadre."

    play sound sfx_gresillement
    $ hideGroup()

    scene bg_canon at adaptive_fullscreen,heavy_shake

    "La salle vibre."
    "Très légèrement."

    "Le canon s’illumine."
    "Une lueur bleue apparaît en son centre."

    $ showGroup([
        ("noam", "peur", 0.22),
        ("ryn", "surpris", 0.78),
    ])

    play sound sfx_laser_canon volume 8.0

    noam desespoir "Putain…"
    noam desespoir "C’est réel."

    ryn desaccord "T’en doutais ?"

    noam triste "J’espérais."

    "Les écrans changent."
    "Un flux vidéo apparaît."
    "Brouillé."
    "Inexploitable."

    noam panne "On voit rien."

    ryn determine "C’est fait exprès."

    "Un grondement sourd."
    "Comme un orage enfermé."

    noam inquiet "On devrait partir."

    ryn fatigue "Ouais."

    "Aucun de nous ne bouge."

    "Le tir part."

    "Un rayon brutal."
    "Vertical."
    "Il frappe la fosse."

    "La lumière envahit la salle."
    "Blanche."
    "Aveuglante."
    $ hideGroup()

    scene bg_canon at adaptive_fullscreen,heavy_shake

    $ showGroup([
        ("noam", "desespoir", 0.22),
        ("ryn", "surpris", 0.78),
    ])

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

    noam inquiet "…"
    noam inquiet "Quelqu'un vient de mourir."

    "Ryn ne répond pas tout de suite."

    ryn colere "Ouais."

    noam triste "On ne sait même pas qui."

    ryn fatigue "Non."
    ryn fatigue "Mais Kami, si."

    "Il se détourne du canon."
    "Pour la première fois."

    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    # Micro-shift : après le tir, Noam se recentre légèrement, Ryn se “referme”

    ryn fatigue "Voilà."
    ryn fatigue "C’est ça, le Conclave."

    noam reflexion "Une salle de réunion avec une arme."

    ryn desaccord "Non."
    ryn desaccord "Une arme avec une salle de réunion autour."
    ryn desaccord "Enfin, faut dire qu'il y a peu de chance qu'on fasse des réunions ici."

    ryn jaloux "C'est glauque."

    pause 0.5

    ryn determine "Et maintenant…"
    ryn determine "Chaque vote va avoir un poids."

    noam raison "Parce qu’on saura ce qu’il y a derrière."

    ryn reflechit "Parce qu’on l’aura entendu."

    "Il me regarde."
    "Pas pour m’intimider."
    "Pour vérifier."

    ryn inquiet "Quand ça recommencera…"
    ryn inquiet "Tu feras semblant que t’as rien vu ?"

    noam hesitation "…"

    ryn determine "Ou tu t’en souviendras ?"

    pause 0.4

    "Je n’ai pas de réponse à lui apporter."
    "Pas encore."
    "Nos choix peuvent avoir de véritables impacts ici."

    "Mais je sais une chose."
    "Je n’oublierai jamais ce bruit."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_2

    $ hideGroup()
    jump CANON_TP


#2m30
# total : 31m20
