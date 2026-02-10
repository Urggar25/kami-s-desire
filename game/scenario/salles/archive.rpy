# -----------------------------------------------------------------------
# SALLE D'ARCHIVE — Connaissance fragmentée
# - 2 persos : Noam + Tomas (uniquement à la découverte)
# - Interactions : biblio / console / hologramme
# - Ton : calme, administratif, légèrement absurde
# -----------------------------------------------------------------------

default decouverte_salle_archive = False

label ARCHIVE_TP:
    scene bg_archive at adaptive_fullscreen

    if not decouverte_salle_archive:
        jump decouverte_salle_archive

    $ pnc_room = "pnc_archive"
    call screen pnc_archive()

# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_archive():

    modal True
    zorder 200

    add Solid("#000")
    add "images/background/bg_archive.png" at cover_screen

    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    imagebutton:
        idle "images/background/interact/salle_archive/biblio.png"
        hover "images/background/interact/salle_archive/biblio_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("ARCHIVE_PNC_BIBLIO")

    imagebutton:
        idle "images/background/interact/salle_archive/console.png"
        hover "images/background/interact/salle_archive/console_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("ARCHIVE_PNC_CONSOLE")

    imagebutton:
        idle "images/background/interact/salle_archive/hologramme.png"
        hover "images/background/interact/salle_archive/hologramme_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("ARCHIVE_PNC_HOLOGRAMME")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


    if free_time_active and lysa_link == 3:
        imagebutton:
            idle Transform("images/character/lysa/reflexion.png", zoom=0.75)
            hover Transform("images/character/lysa/neutre.png", zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "ARCHIVE_TP"), Jump("LYSA_LINK_INTERACT")]

label ARCHIVE_PNC_BIBLIO:

    "Des étagères entières."
    "Pas de livres."
    "Des blocs de données."
    "Alignés."
    "Classés."
    "Sans titre lisible."

    "Chaque module porte un code."
    "Des chiffres."
    "Des dates."
    "Rien d’humain."

    think "C’est bien une bibliothèque."
    think "Mais elle n'est pas faite pour être lue."

    jump ARCHIVE_TP

label ARCHIVE_PNC_CONSOLE:

    "La console s’allume dès que je m’approche."
    "Pas d’accueil."
    "Pas de menu."
    "Juste une liste."

    "Entrée."
    "Entrée."
    "Entrée."

    "Certaines sont grisées."
    "D’autres s’ouvrent."
    "Pour afficher… presque rien."

    think "Ils appellent ça des archives."
    think "Mouai, je ne sais pas vraiment si ça nous sera utile un jour ..."

    jump ARCHIVE_TP

label ARCHIVE_PNC_HOLOGRAMME:

    "L’hologramme flotte au centre de la salle."
    "Une sphère."
    "Des lignes."
    "Des points."

    "Ça ressemble à une carte."
    "Ou à une chronologie. Il semble y avoir une sorte de jauge temporelle en dessous."
    "Ou aux deux."

    think "Je pourrais y toucher mais j'ai encore à faire."
    think "J'essaierai sans doute plus tard."

    jump ARCHIVE_TP

# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_archive:

    $ decouverte_salle_archive = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "La salle d’archive."
    think "Rien que le nom ça m'ennuie déjà."

    pause 0.4

    scene bg_archive at adaptive_fullscreen with fade

    "La salle est immense."
    "Pas forcément spectaculaire, ce n'est qu'une salle d'archive après tout."
    "Mais sa taille peut être assez surprenante."

    "Des murs entiers sont couverts de données et de bouquin."
    "Des rangées."
    "Des couloirs."
    "Comme si on avait enfermé une ville entière de dossiers ici."

    "Et au fond… une console principale."
    "Des écrans qui tournent déjà."
    "Comme si la salle travaillait sans nous."

    $ showP("noam", "reflexion", 0.22)
    $ showP("tomas", "neutre", 0.78)

    "Un grand gaillard s’arrête net un peu plus loin."

    tomas "Ah."
    tomas "Ok."

    noam "Quoi ?"

    $ showP("tomas", "mefiant", 0.78)
    tomas "Je pensais que…"
    tomas "Enfin…"
    tomas "Je m’attendais à plus de… livres."

    noam "Des vrais ?"

    $ showP("tomas", "raison", 0.78)
    tomas "Oui."
    tomas "Enfin non."
    tomas "Enfin si, mais—"

    noam "Respire."

    $ showP("tomas", "panne", 0.78)
    tomas "Je croyais que ‘archives’ voulait dire…"
    tomas "Des trucs qu’on peut lire."
    tomas "Enfin, tu sais ..."

    noam "Faut te mettre à la page mon vieux."

    $ showP("tomas", "culpabilite", 0.78)
    tomas "Je suis surtout nouveau dans…"
    tomas "Tout ça."

    "Il fait un geste vague."
    "La salle."
    "Le Conclave."
    "Le reste."

    $ showP("noam", "sourire", 0.22)
    noam "T’inquiète."
    noam "On est tous un peu largués."

    pause 0.3

    "Il se tourne vers moi, comme s’il réalisait un détail important."
    "Un truc évident, sauf quand tu viens d’arriver."

    $ showP("tomas", "reflechit", 0.78)
    tomas "Au fait—"
    tomas "Je m'appelle Tomas."

    noam "Noam."

    $ showP("tomas", "raison", 0.78)
    tomas "Oui."
    tomas "Je sais."
    tomas "Ton siège avait ton nom. Je—"
    tomas "Enfin bref."

    $ showP("noam", "taquin", 0.22)
    noam "T’as pas besoin de te présenter comme à un entretien."

    $ showP("tomas", "panne", 0.78)
    tomas "C’est un réflexe."
    tomas "Je…"
    tomas "J’essaye toujours de faire les choses proprement."

    noam "Mauvais endroit je crois."

    $ showP("tomas", "rire", 0.78)
    tomas "Ouais."
    tomas "Clairement."

    $ showP("tomas", "reflechit", 0.78)
    "Tomas s’approche d’une console."
    "Regarde l’écran."
    "Penche la tête."

    tomas "…"
    tomas "Ah."

    noam "Quoi encore ?"

    $ showP("tomas", "surpris", 0.78)
    tomas "Je pensais que c’était une recherche."
    tomas "Mais en fait…"
    tomas "C’est juste une liste."

    noam "Bienvenue dans l’administration."

    $ showP("tomas", "rire", 0.78)
    tomas "C’est rassurant, quelque part."
    tomas "Même sous Kami, la paperasse survit."

    "Je regarde l’hologramme."
    "Les murs."
    "Les consoles."

    think "Il y a des données sur à peu près tout."
    think "Mais tout est bien plus compliqué que dans les papiers habituels."

    $ showP("noam", "reflexion", 0.22)
    noam "On apprendra peut-être des choses ici."
    noam "Mais faudrait déjà comprendre ce que ça racconte."

    $ showP("tomas", "reflechit", 0.78)
    "Il plisse les yeux en essayant de déchiffrer une suite de nombre."

    tomas "Ouais."
    tomas "Ou on apprendra surtout ce qu’ils veulent bien laisser traîner."

    pause 0.2

    $ showP("tomas", "mefiant", 0.78)
    tomas "Regarde ça."

    "Il tape sur une ligne."
    "Une fenêtre s’ouvre."
    "Trois champs."
    "Pas de phrase."
    "Pas de résumé."

    "Un code."
    "Un horodatage."
    "Et une colonne marquée : \"NIVEAU\"."

    noam "Ça veut dire quoi ?"

    $ showP("tomas", "determine", 0.78)
    tomas "Ça veut dire…"
    tomas "Que c’est pas une archive pour nous."

    noam "Évidemment que c’est pas pour nous."

    $ showP("tomas", "raison", 0.78)
    tomas "Non mais…"
    tomas "Je veux dire : même le format."
    tomas "C’est pas 'fait pour être lu'."
    tomas "C’est fait pour être… ingéré."

    noam "In— quoi ?"

    $ showP("tomas", "panne", 0.78)
    tomas "Pardon."
    tomas "En gros, la machine est capable de tout comprendre facilement sans mise en forme des données."
    tomas "Pour une machine, il n'y a rien de plus simple."

    "Il pointe l’hologramme."
    "La sphère tourne lentement."
    "Des points s’allument, s’éteignent."
    "Comme des nœuds d’un réseau."

    $ showP("tomas", "reflechit", 0.78)
    tomas "Ça, c’est pas une carte pour nous situer."
    tomas "C’est un tableau de corrélation."
    tomas "Ça relie des événements : les archives."
    tomas "On peut voir ce qui s'est passé où et quand."
    tomas "Avec qui et pourquoi."

    noam "D'où la salle d'archive."

    $ showP("tomas", "determine", 0.78)
    tomas "Tout est déjà exploité et rangé."
    tomas "Il suffit de comprendre comment ça fonctionne ..."
    tomas "Les index."
    tomas "Les droits d’accès."
    tomas "Le squelette."

    "Il s’interrompt."
    "Comme si quelque chose se mettait en place dans sa tête."

    $ showP("tomas", "surpris", 0.78)
    tomas "Non attends…"

    noam "Quoi ?"

    "Il scrolle encore."
    "Deux lignes."
    "Puis une troisième."
    "Une mention revient."

    $ showP("tomas", "reflechit", 0.78)
    tomas "\"STATUT : VALIDÉ\"…"
    tomas "\"STATUT : BLOQUÉ\"…"
    tomas "\"STATUT : EXÉCUTÉ\"…"

    noam "Mais qu'est ce que tu fais ?!"

    $ showP("tomas", "raison", 0.78)
    tomas "C’est ça le truc."

    pause 0.3

    $ showP("tomas", "determine", 0.78)
    tomas "Les archives ne sont pas seulement une mémoire."
    tomas "C’est une chaîne de décision."
    tomas "Un pipeline."

    noam "Un quoi ?"

    $ showP("tomas", "panne", 0.78)
    tomas "Désolé."
    tomas "En gros c'est un… circuit."
    tomas "Tu changes un paramètre."
    tomas "Et derrière, tu peux voir tout ce qui a un rapport, direct ou indirect avec ce paramètre."
    tomas "Quelque part."

    "Je sens un froid me remonter le dos."
    "Pas celui de la salle."
    "Un autre."

    $ showP("noam", "inquiet", 0.22)
    noam "Donc ce qu’on appelle 'archives'…"
    noam "Il y a globalement tout dedans ?."

    $ showP("tomas", "reflechit", 0.78)
    tomas "Oui."
    tomas "Et du coup…"
    tomas "Si on peut lire quelque chose ici un jour…"

    $ showP("tomas", "mefiant", 0.78)
    tomas "On pourra apprendre énormement de choses !"

    pause 0.4

    think "Peut être que Kami n'a pas besoin de rendre les données plus lisibles pour les comprendre."
    think "Parce que ce n'est pas nous qui sommes censés comprendre."

    $ showP("noam", "reflexion", 0.22)
    tomas "Ok."
    tomas "Je vais continuer à essayer de comprendre comment ça marche."

    $ showP("tomas", "joie", 0.78)
    tomas "Oh ouais !"
    tomas "Bonne idée !"

    pause 0.3
    
    "Tomas continue de nouveau à bidouiller des paramètres."
    "Je devrais y aller ..."
    
    call CHECK_ALL_SALLES_VISITEES

    jump ARCHIVE_TP

# Durée : 2m50
# Total : 36m20