# -----------------------------------------------------------------------
# SALLE D'OBSERVATION — même modèle que CANON
# - 2 persos seulement : Noam + Lysa
# - Découverte : ils sont dans l'espace
# - PNC : radio / vitre / retour
# - Parfois : passage d'un vaisseau (District ORBITE)
# -----------------------------------------------------------------------

default decouverte_salle_observation = False

label OBSERVATION_TP:
    scene bg_observation at adaptive_fullscreen

    if not decouverte_salle_observation:
        jump decouverte_salle_observation

    $ pnc_room = "pnc_observation"
    call screen pnc_observation()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_observation():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_observation.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_observation/radio.png"
        hover "images/background/interact/salle_observation/radio_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OBS_PNC_RADIO")

    imagebutton:
        idle "images/background/interact/salle_observation/vitre.png"
        hover "images/background/interact/salle_observation/vitre_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OBS_PNC_VITRE")
        
    imagebutton:
        idle "images/background/interact/salle_observation/orbite.png"
        hover "images/background/interact/salle_observation/orbite_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OBS_PNC_ORBITE")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


    if free_time_active and lysa_link == 2:
        imagebutton:
            idle Transform("images/character/lysa/reflexion.png", zoom=0.75)
            hover Transform("images/character/lysa/triste.png", zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("LYSA_LINK_INTERACT")]

    if free_time_active and julian_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform("images/character/julian/sourire.png", zoom=0.75)
            hover Transform("images/character/julian/taquin.png", zoom=0.75)
            focus_mask True
            xalign 0.62
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("JULIAN_LINK_INTERACT")]


    if free_time_active and elen_link == 2:
        imagebutton:
            idle Transform("images/character/elen/content.png", zoom=0.75)
            hover Transform("images/character/elen/reflechit.png", zoom=0.75)
            focus_mask True
            xalign 0.40
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("ELEN_LINK_INTERACT")]


label OBS_PNC_RADIO:
    "La console radio est massive."
    "Plusieurs fréquences."
    "Des indicateurs de puissance."
    "Un micro sur bras articulé."
    "Tout est verrouillé."
    think "Donc on peut parler… mais pas appeler."
    jump OBSERVATION_TP


label OBS_PNC_VITRE:
    "Les vitres donnent sur le vide."
    "Pas une vue 'sur le dehors'."
    "Une vue sur l’espace."
    think "Difficile de s'habituer à ça."
    jump OBSERVATION_TP

label OBS_PNC_ORBITE:

    window auto

    "Je m’approche un peu plus de la vitre."
    "Mon regard se fixe sur la masse la plus imposante au loin."

    "Ce n’est pas une station."
    "Pas vraiment."
    "Trop mobile."
    "Trop structurée."

    "C'est sans doute un vaisseau."
    "Ou quelque chose qui en a la fonction."

    "Des lumières courent le long de sa coque."
    "Pas au hasard."
    "Des lignes nettes."
    "Presque… organisées."

    "Autour, d’autres silhouettes plus petites."
    "Elles apparaissent."
    "Disparaissent."
    "Comme si tout ça suivait un rythme précis."

    think "Le district ORBITE."
    think "Du moins, ce que j’imagine que c’est."

    "Rien ne semble nous prêter attention."
    "Aucune manœuvre."
    "Aucun signal visible."

    "Juste cette présence."
    "Lourde."
    "Constante."

    think "Ils sont là."
    think "Ils bougent."
    think "Ils vivent."

    think "Et moi… je regarde."

    pause 0.3

    jump OBSERVATION_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label OBS_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_observation:

    $ decouverte_salle_observation = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "La salle d'observation."
    think "Le nom sonne calme."
    think "Presque normal."

    pause 0.4

    scene bg_observation at adaptive_fullscreen with fade

    "La salle est large."
    "Plus ouverte que les autres."
    "Comme un poste de commande."

    "À l’avant : une immense baie vitrée."
    "Et derrière : des consoles."
    "Des écrans."
    "Des appareils alignés avec une rigueur presque militaire."

    "Au centre, une console radio."
    "Pas un petit talkie."
    "Une vraie station."
    "Avec des boutons physiques."
    "Des curseurs."
    "Un micro lourd."

    $ showP("noam", "reflexion", 0.22)   # gauche
    $ showP("lysa", "reflexion", 0.78)   # droite

    "Lysa est déjà près de la vitre."
    "Elle ne touche rien."
    "Elle regarde dehors."

    $ showP("noam", "hesitation", 0.22)

    noam "Tu… regardes quoi ?"

    $ showP("lysa", "neutre", 0.78)
    lysa "Viens."

    "Je m’approche."
    "Et je comprends tout de suite."
    "Mon cerveau met une seconde à suivre."

    "Il n’y a pas de ville à proprement parlé."
    "Pas de ciel bleu éclatant."
    "Juste du noir."
    "Et des points scintillants."
    "Des étoiles."
    "Quand on plonge le regard, on voit une masse imposante et une sorte de gros vaisseau volant."

    $ showP("noam", "surpris", 0.22)

    noam "…"
    noam "Attends."

    $ showP("lysa", "sourire", 0.78)
    lysa "Ouais."

    $ showP("noam", "hesitation", 0.22)
    noam "On est…"

    $ showP("lysa", "taquin", 0.78)
    lysa "Dans l’espace ouai."

    "Elle le dit comme si c’était une évidence."
    "Mais son sourire la trahit."
    "Petit."
    "Presque enfantin."

    $ showP("noam", "desaccord", 0.22)

    noam "C’est pas possible."
    noam "On a marché dix minutes."

    $ showP("lysa", "reflexion", 0.78)
    lysa "Et on a été endormis dans des caissons."
    lysa "Donc oui."
    lysa "Tout est possible."

    "Je colle presque mon front à la vitre."
    "Le verre est froid."
    "Ultra froid."

    $ showP("noam", "surpris", 0.22)
    noam "C’est beau."
    $ showP("noam", "inquiet", 0.22)
    noam "Et ça me donne la nausée."

    $ showP("lysa", "sourire", 0.78)
    lysa sourire "Je comprends."
    lysa content "Moi ça…"
    lysa content "Ça me calme, bizarrement."

    $ showP("noam", "taquin", 0.22)
    noam "Toi t’es câblée à l’envers."

    $ showP("lysa", "rire", 0.78)
    lysa "Peut-être."
    lysa reflexion "Ou peut-être que j’avais besoin de voir un truc…"
    lysa reflexion"Qui change de notre quotidien."

    "Un long moment de silence s'en est suivi."
    "Mais pas un silence lourd."
    "Juste un calme reposant."

    "Je regarde les consoles derrière nous."
    "La radio."
    "Les écrans."
    "Tout a l'air fonctionnel."

    $ showP("noam", "reflexion", 0.22)
    noam "Tu crois qu’on peut contacter quelqu’un ?"

    $ showP("lysa", "triste", 0.78)
    lysa "Je ne sais pas me servir de ce truc."
    lysa "Sinon, j'aurai bien aimé appeler ma famille."

    $ showP("noam", "triste", 0.22)
    noam "Ouais."

    "Je m'avance vers la console radio."

    $ showP("noam", "determine", 0.22)
    noam "Mais ça doit pas être bien compliqué, attends ..."

    $ showP("lysa", "inquiet", 0.78)
    lysa neutre "À ta place, j’éviterais de toucher à ça."
    lysa blase "On sait même pas si on a le droit."
    lysa fatigue "... Et franchement, vaut mieux pas tester."

    $ showP("noam", "rire", 0.22)
    "Je lâche un petit rire."
    $ showP("noam", "reflexion", 0.22)
    "Sans joie."

    pause 0.4

    "Un point lumineux bouge et passe à plusieurs dizaines de kilomètres de là."
    "Pas une étoile."
    "Le déplacement est trop régulier."
    "Trop droit."

    "Puis une silhouette passe."
    "Un vaisseau."
    "Petit et rapide."

    $ showP("noam", "surpris", 0.22)
    noam "Tu vois ça ?"
    "Je montre du doigt l'horizon."

    $ showP("lysa", "surpris", 0.78)
    lysa surpris "Ouais."
    lysa reflexion "On est vraiment loin de chez nous."
    lysa reflexion "Regarde la trajectoire."
    lysa reflexion "Et les marqueurs sur le côté du vaisseau."

    "Sur le flanc, une bande lumineuse."
    "Un code."
    "Un motif propre."

    $ showP("lysa", "determine", 0.78)
    lysa determine "District ORBITE."
    lysa determine "On est dans leur domaine ici."
    lysa reflexion "Peut être que leurs représentants en savent plus que nous sur où nous sommes."

    $ showP("noam", "reflexion", 0.22)
    noam "Donc y’a du trafic."
    noam "Et y’a des gens dehors."

    $ showP("lysa", "blase", 0.78)
    lysa blase "Bien sûr qu’il y a des gens."
    lysa triste "On est juste… pas du même côté de la vitre."

    pause 0.4

    $ showP("noam", "reflexion", 0.22)
    noam "C’est fou."
    noam "Kami nous a mis dans l’espace."
    noam "Comme si c’était anodin…"
    noam "Comme si c'était juste un décor."

    $ showP("lysa", "reflexion", 0.78)
    lysa "C’est un décor."
    lysa "Mais c’est aussi un message."

    $ showP("noam", "hesitation", 0.22)
    noam "Lequel ?"

    $ showP("lysa", "determine", 0.78)
    lysa "Qu’on est hors du monde."
    lysa "Hors des règles."
    lysa triste "Hors de tout ce qu'on connait depuis là."

    $ showP("noam", "reflexion", 0.22)
    noam "Tu dis ça calmement."

    $ showP("lysa", "sourire", 0.78)
    lysa "Je fais semblant. J'essaye de me rassurer."
    lysa taquin "Ça marche une fois sur deux."

    $ showP("noam", "taquin", 0.22)
    noam "Joli ratio."

    $ showP("lysa", "rire", 0.78)
    lysa "Merci."

    "Elle reste face à la vitre."
    "Puis elle baisse un peu la voix."

    $ showP("lysa", "reflexion", 0.78)
    lysa "Tu sais ce qui est le pire ?"

    $ showP("noam", "neutre", 0.22)
    noam "Vas-y."

    $ showP("lysa", "triste", 0.78)
    lysa "J’arrive pas à décider si c’est magnifique…"
    lysa "Ou si c’est juste une autre façon de nous écraser."

    $ showP("noam", "raison", 0.22)
    noam "Les deux."

    $ showP("lysa", "blase", 0.78)
    lysa blase "Ouais."
    lysa triste "Probablement les deux."

    pause 0.5

    $ showP("noam", "reflexion", 0.22)
    "Je recule d’un pas."
    "Je regarde la radio."
    "Les écrans."
    "Les vitres."

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES

    jump OBSERVATION_TP

# Durée : 2m10
# Total : 33m30
