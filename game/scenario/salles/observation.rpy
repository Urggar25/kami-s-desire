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

    if not decouverte_salle_observation and day_number() == 1:
        jump decouverte_salle_observation

    $ pnc_room = "pnc_observation"
    call screen pnc_observation()

    if free_time_active:
        return
    if exploration_libre_active:
        return


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

    if social_free_time_active() and lysa_link == 2:
        imagebutton:
            idle Transform("images/character/lysa/reflexion.png", zoom=0.75)
            hover Transform("images/character/lysa/triste.png", zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("LYSA_LINK_INTERACT")]

    if social_free_time_active() and julian_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform("images/character/julian/sourire.png", zoom=0.75)
            hover Transform("images/character/julian/taquin.png", zoom=0.75)
            focus_mask True
            xalign 0.62
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("JULIAN_LINK_INTERACT")]


    if social_free_time_active() and elen_link == 2:
        imagebutton:
            idle Transform("images/character/elen/content.png", zoom=0.75)
            hover Transform("images/character/elen/reflechit.png", zoom=0.75)
            focus_mask True
            xalign 0.40
            yalign 0.30
            action [SetVariable("last_room_label", "OBSERVATION_TP"), Jump("ELEN_LINK_INTERACT")]


    use exploration_retour_button

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

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("lysa", "reflexion", 0.78),
    ])

    "Lysa est déjà près de la vitre."
    "Elle ne touche rien."
    "Elle regarde dehors."


    noam hesitation "Tu… regardes quoi ?"

    lysa neutre "Viens."

    "Je m’approche."
    "Et je comprends tout de suite."
    "Mon cerveau met une seconde à suivre."

    "Il n’y a pas de ville à proprement parlé."
    "Pas de ciel bleu éclatant."
    "Juste du noir."
    "Et des points scintillants."
    "Des étoiles."
    "Quand on plonge le regard, on voit une masse imposante et une sorte de gros vaisseau volant."


    noam surpris "…"
    noam surpris "Attends."

    lysa sourire "Ouais."

    noam hesitation "On est…"

    lysa taquin "Dans l’espace ouai."

    "Elle le dit comme si c’était une évidence."
    "Mais son sourire la trahit."
    "Petit."
    "Presque enfantin."


    noam desaccord "C’est pas possible."
    noam desaccord "On a marché dix minutes."

    lysa reflexion "Et on a été endormis dans des caissons."
    lysa reflexion "Donc oui."
    lysa reflexion "Tout est possible."

    "Je colle presque mon front à la vitre."
    "Le verre est froid."
    "Ultra froid."

    noam surpris "C’est beau."
    noam inquiet "Et ça me donne la nausée."

    lysa sourire "Je comprends."
    lysa content "Moi ça…"
    lysa content "Ça me calme, bizarrement."

    noam taquin "Toi t’es câblée à l’envers."

    lysa rire "Peut-être."
    lysa reflexion "Ou peut-être que j’avais besoin de voir un truc…"
    lysa reflexion"Qui change de notre quotidien."

    "Un long moment de silence s'en est suivi."
    "Mais pas un silence lourd."
    "Juste un calme reposant."

    "Je regarde les consoles derrière nous."
    "La radio."
    "Les écrans."
    "Tout a l'air fonctionnel."

    noam reflexion "Tu crois qu’on peut contacter quelqu’un ?"

    lysa triste "Je ne sais pas me servir de ce truc."
    lysa triste "Sinon, j'aurai bien aimé appeler ma famille."

    noam triste "Ouais."

    "Je m'avance vers la console radio."

    noam determine "Mais ça doit pas être bien compliqué, attends ..."

    lysa neutre "À ta place, j’éviterais de toucher à ça."
    lysa blase "On sait même pas si on a le droit."
    lysa fatigue "... Et franchement, vaut mieux pas tester."

    "Je lâche un petit rire."
    "Sans joie."

    pause 0.4

    "Un point lumineux bouge et passe à plusieurs dizaines de kilomètres de là."
    "Pas une étoile."
    "Le déplacement est trop régulier."
    "Trop droit."

    "Puis une silhouette passe."
    "Un vaisseau."
    "Petit et rapide."

    noam surpris "Tu vois ça ?"
    "Je montre du doigt l'horizon."

    lysa surpris "Ouais."
    lysa reflexion "On est vraiment loin de chez nous."
    lysa reflexion "Regarde la trajectoire."
    lysa reflexion "Et les marqueurs sur le côté du vaisseau."

    "Sur le flanc, une bande lumineuse."
    "Un code."
    "Un motif propre."

    lysa determine "District ORBITE."
    lysa determine "On est dans leur domaine ici."
    lysa reflexion "Peut être que leurs représentants en savent plus que nous sur où nous sommes."

    noam reflexion "Donc y’a du trafic."
    noam reflexion "Et y’a des gens dehors."

    lysa blase "Bien sûr qu’il y a des gens."
    lysa triste "On est juste… pas du même côté de la vitre."

    pause 0.4

    noam reflexion "C’est fou."
    noam reflexion "Kami nous a mis dans l’espace."
    noam reflexion "Comme si c’était anodin…"
    noam reflexion "Comme si c'était juste un décor."

    lysa reflexion "C’est un décor."
    lysa reflexion "Mais c’est aussi un message."

    noam hesitation "Lequel ?"

    lysa determine "Qu’on est hors du monde."
    lysa determine "Hors des règles."
    lysa triste "Hors de tout ce qu'on connait depuis là."

    noam reflexion "Tu dis ça calmement."

    lysa sourire "Je fais semblant. J'essaye de me rassurer."
    lysa taquin "Ça marche une fois sur deux."

    noam taquin "Joli ratio."

    lysa rire "Merci."

    "Elle reste face à la vitre."
    "Puis elle baisse un peu la voix."

    lysa reflexion "Tu sais ce qui est le pire ?"

    noam neutre "Vas-y."

    lysa triste "J’arrive pas à décider si c’est magnifique…"
    lysa triste "Ou si c’est juste une autre façon de nous écraser."

    noam raison "Les deux."

    lysa blase "Ouais."
    lysa triste "Probablement les deux."

    pause 0.5

    "Je recule d’un pas."
    "Je regarde la radio."
    "Les écrans."
    "Les vitres."

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_6

    $ hideGroup()
    jump OBSERVATION_TP

# Durée : 2m10
# Total : 33m30
