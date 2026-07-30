# -----------------------------------------------------------------------
# SALLE D'ARCHIVE — Connaissance fragmentée
# - 2 persos : Noam + Tomas (uniquement à la découverte)
# - Interactions : biblio / console / hologramme
# - Ton : calme, administratif, légèrement absurde
# -----------------------------------------------------------------------

default decouverte_salle_archive = False


label ARCHIVE_TP:
    scene bg_archive at adaptive_fullscreen

    if not decouverte_salle_archive and day_number() == 1:
        jump decouverte_salle_archive

    if social_free_time_active() and free_time_round == 2 and not seen_voyeur_mara_tomas:
        jump temps_libre_salle_archive

    $ pnc_room = "pnc_archive"
    call screen pnc_archive()

    if free_time_active:
        return
    if exploration_libre_active:
        return

# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_archive():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("archive")
    use room_scene_interactions("archive")

    if social_free_time_active() and tomas_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform(character_image("tomas", "reflechit"), zoom=0.75)
            hover Transform(character_image("tomas", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.60
            yalign 0.30
            action [SetVariable("last_room_label", "ARCHIVE_TP"), Jump("TOMAS_LINK_INTERACT")]

    if social_free_time_active() and lysa_link == 3:
        imagebutton:
            idle Transform(character_image("lysa", "reflexion"), zoom=0.75)
            hover Transform(character_image("lysa", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.84
            yalign 0.30
            action [SetVariable("last_room_label", "ARCHIVE_TP"), Jump("LYSA_LINK_INTERACT")]


label archive1_bibliotheque:

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

label archive1_porte:
    $ corridor_current = "dortoir"
    jump EXIT_ROOM_TO_CORRIDOR


label archive2_ordinateur:

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

label archive2_ecran:

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

    think "La salle d’archive. Je n'ai jamais été très studieux..."
    think "Rien que le nom ça m'ennuie déjà."

    pause 0.4

    scene bg_archive at adaptive_fullscreen with fade

    "La salle est immense."
    "Pas forcément spectaculaire, ce n'est qu'une salle d'archive après tout."
    "Mais sa taille peut être assez surprenante. En vrai, j'imaginais ça plus petit."

    "Des murs entiers sont couverts de données et de bouquin, rangées par rangées et par couloirs."
    "Comme si on avait enfermé une ville entière de dossiers ici."

    "Et au fond… une console principale."
    "Des écrans qui tournent déjà."
    "Comme si la salle travaillait sans nous."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])

    "Le grand gaillard de tout à l'heure s’arrête net un peu plus loin."

    tomas surpris "Ah. Ok."

    noam reflexion "Quoi ?"

    tomas mefiant "Je pensais que… Enfin... Je m’attendais à plus de… livres"

    noam reflexion "Des vrais ?"

    tomas raison "Oui."
    tomas raison "Enfin non. Enfin si, mais—"

    noam reflexion "Respire."

    tomas panne "Je croyais que ‘archives’ voulait dire…"
    tomas panne "Des trucs qu’on peut lire."
    tomas panne "Enfin, tu sais ..."

    noam reflexion "Faut te mettre à la page mon vieux. Puis y'en a des livres quand même par là."

    tomas culpabilite "O-Ouais mais c'est plus des recceuil de données imprimés que de vrais ouvrages... Je suis surtout nouveau dans…"
    tomas culpabilite "Tout ça. D-Désolé, je suis pas très à l'aise à l'oral..."

    "Il fait un geste vague."

    noam sourire "T’inquiète."
    noam sourire "On est tous un peu largués."

    pause 0.3

    "Il se tourne vers moi, comme s’il réalisait un détail important."
    "Un truc évident, sauf quand tu viens d’arriver."

    tomas reflechit "Au fait—"
    tomas raison "Je m'appelle Tomas."

    noam sourire "Moi c'est Noam."

    tomas raison "Oui."
    tomas raison "Je sais."
    tomas raison "Ton siège avait ton nom. Je—"
    tomas raison "Enfin bref."

    noam taquin "T’as pas besoin de te présenter comme à un entretien."

    tomas panne "O-Ouais. C’est un réflexe."
    tomas panne "Je… J’essaye toujours de faire les choses proprement."

    noam taquin "Mauvais endroit je crois."

    tomas rire "Ouais. Clairement !"

    "Tomas s’approche d’une console, il regarde l'écran et penche la tête."

    tomas reflechit "… Oh. C'est quoi ça ?"

    noam taquin "Quoi encore ?"
    think "Mais où il va ?"

    hide tomas with moveoutright
    hide noam with moveoutright
    pause 1.0
    
    scene archive2 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])

    tomas surpris "Je pensais que c’était une recherche."
    tomas surpris "Mais en fait…"
    tomas surpris "C’est juste une sorte de liste."

    noam taquin "Bienvenue dans l’administration."

    tomas rire "C’est rassurant, quelque part."
    tomas rire "Même sous Kami, la paperasse survit."

    noam taquin "Ouais, ça tu peux me croire. Il y a toujours autant de paperasses..."

    "Je regarde l’hologramme. Les murs, les consoles."

    think "Il y a des données sur à peu près tout."
    think "Mais tout est bien plus compliqué que dans les papiers habituels."

    noam reflexion "On apprendra peut-être des choses ici."
    noam reflexion "Mais faudrait déjà comprendre ce que ça racconte."

    "Il plisse les yeux en essayant de déchiffrer une suite de nombre."

    tomas reflechit "Ouais On apprendra surtout ce qu’ils veulent bien laisser traîner."

    pause 0.2

    tomas mefiant "Regarde ça."

    "Il tape sur une ligne sur une sorte d'écran de commande."
    "Une fenêtre s’ouvre."
    "Trois champs."
    "Pas de phrase."
    "Pas de résumé."

    "Un code."
    "Un horodatage."
    "Et une colonne marquée : \"NIVEAU\"."

    noam reflexion "Ça veut dire quoi ?"

    tomas determine "Ça veut dire…"
    tomas determine "Que c’est pas une archive pour nous."

    noam reflexion "Évidemment que c’est pas pour nous."

    tomas raison "Non mais…"
    tomas raison "Je veux dire : même le format."
    tomas raison "C’est pas 'fait pour être lu'."
    tomas raison "C’est fait pour être… ingéré et décodé rapidement."

    noam reflexion "In— quoi ?"

    tomas panne "Pardon."
    tomas panne "En gros, la machine est capable de tout comprendre facilement sans mise en forme des données."
    tomas reflexion "Même sans traduire dans notre langue."
    tomas panne "Pour une machine, il n'y a rien de plus simple."

    "Il pointe du doigt l'écran avec la carte de la terre."
    "La sphère tourne lentement."
    "Des points s’allument, s’éteignent."
    "Comme des nœuds d’un réseau."

    tomas reflechit "Ça, c’est pas une carte pour nous situer."
    tomas reflechit "C’est un tableau de corrélation."
    tomas reflechit "Ça relie des événements : les archives."
    tomas reflechit "On peut voir ce qui s'est passé où et quand."
    tomas reflechit "Avec qui et pourquoi."

    noam reflexion "D'où la salle d'archive."

    tomas determine "Tout est déjà exploité et rangé."
    tomas determine "Il suffit de comprendre comment ça fonctionne ..."
    tomas determine "Les index."
    tomas determine "Les droits d’accès."
    tomas determine "Le squelette."

    "Il s’interrompt."
    "Comme si quelque chose se mettait en place dans sa tête."

    tomas surpris "Non attends…"

    noam reflexion "Quoi ?"

    "Il scrolle encore."
    "Deux lignes."
    "Puis une troisième."
    "Une mention revient."

    tomas reflechit "\"STATUT : VALIDÉ\"…"
    tomas reflechit "\"STATUT : BLOQUÉ\"…"
    tomas reflechit "\"STATUT : EXÉCUTÉ\"…"

    noam reflexion "Mais qu'est ce que tu fais ?!"

    tomas raison "C’est ça le truc."

    pause 0.3

    tomas determine "Les archives ne sont pas seulement une mémoire."
    tomas determine "C’est une chaîne de décision."
    tomas determine "Un pipeline."

    noam reflexion "Un quoi ?"

    tomas panne "Désolé."
    tomas panne "En gros c'est un… circuit."
    tomas panne "Tu changes un paramètre."
    tomas panne "Et derrière, tu peux voir tout ce qui a un rapport, direct ou indirect avec ce paramètre."
    tomas panne "Quelque part."

    "Je sens un froid me remonter le dos."
    "Pas celui de la salle."
    "Un autre."

    noam inquiet "Donc ce qu’on appelle 'archives'…"
    noam inquiet "Il y a globalement tout dedans ?."

    tomas reflechit "Oui."
    tomas reflechit "Et du coup…"
    tomas reflechit "Si on peut lire quelque chose ici un jour…"

    tomas mefiant "On pourra apprendre énormement de choses !"

    pause 0.4

    think "Peut être que Kami n'a pas besoin de rendre les données plus lisibles pour les comprendre."
    think "Parce que ce n'est pas nous qui sommes censés comprendre."

    tomas mefiant "Ok."
    tomas mefiant "Je vais continuer à essayer de comprendre comment ça marche."

    tomas joie "Oh ouais !"
    tomas joie "Bonne idée !"

    pause 0.3
    
    "Tomas continue de nouveau à bidouiller des paramètres."
    "Je devrais y aller ..."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES

    $ hideGroup()
    jump ARCHIVE_TP

# Durée : 2m50
# Total : 36m20
