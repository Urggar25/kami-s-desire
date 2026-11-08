# -----------------------------------------------------------------------
# SALLE D'ARCHIVE — Connaissance fragmentée
# - 2 persos : Noam + Tomas (uniquement à la découverte)
# - Interactions : biblio / console / hologramme
# - Ton : calme, administratif, légèrement absurde
# -----------------------------------------------------------------------

default decouverte_salle_archive = False


label ARCHIVE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_324
    scene bg_archive at adaptive_fullscreen

    if not decouverte_salle_archive and day_number() == 1:
        jump decouverte_salle_archive

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

    if social_free_time_active() and character_has_available_free_time("tomas"):
        imagebutton:
            idle Transform(character_image("tomas", "reflechit"), zoom=1.00)
            hover Transform(character_image("tomas", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.60
            yalign 1.00
            action [SetVariable("last_room_label", "ARCHIVE_TP"), SetVariable("free_time_selected_character", "tomas"), Jump("FREE_TIME_CHARACTER_INTERACT")]


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
    think "Des archives, ça devrait au moins nous permettre de comprendre un peu mieux où on a atterri. Enfin, si Kami a prévu de nous laisser lire quelque chose."

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_325
    scene bg_archive at adaptive_fullscreen with fade

    "La salle est bien plus grande que ce que j'imaginais. Il y a des rayonnages partout, mais ce sont surtout les consoles déjà allumées au fond qui attirent mon attention."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])

    "Un grand garçon est penché sur l'une d'elles. Il fait défiler des lignes de données si vite que je me demande s'il arrive vraiment à les lire."

    noam sourire "Salut. Tu as trouvé quelque chose d'intéressant ?"
    tomas surpris "Oh ! Euh, oui, enfin... Je crois. Attends, ça vient de changer tout seul."
    "Il revient à l'écran précédent avec une précipitation qui manque de lui faire fermer toute la fenêtre."
    tomas panne "Bon, non, c'est toujours là. Désolé, j'étais concentré."
    noam taquin "J'avais remarqué. Moi c'est Noam."
    tomas neutre "Tomas. Je viens d'Archive. Enfin, du district Harmonie, comme toi, mais de la zone des archives."
    $ unlock_character_name("tomas")
    tomas reflechit "Je cherchais juste un catalogue. Sauf qu'on dirait que tous les fichiers sont liés entre eux et que les menus changent selon les droits d'accès. C'est assez curieux parce que..."
    "Il s'arrête en voyant ma tête."
    tomas panne "Je parle trop, hein ?"
    noam sourire "Un petit peu. Tu peux me montrer plutôt ?"
    tomas joie "Oui ! Ça, je peux."

    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "archive2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_326
    scene archive2 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])

    "Il m'indique une carte de la Terre sur laquelle des milliers de points s'allument en même temps. Une série de catégories apparaît sur le côté."

    tomas reflechit "Regarde, il y a des événements historiques, des registres de population et même des fiches individuelles. Enfin, je crois que ce sont des fiches individuelles."
    noam surpris "Tu peux chercher quelqu'un ?"
    tomas neutre "En principe oui. Tu veux essayer avec ton nom ?"
    noam sourire "Pourquoi pas ? Tu vas peut-être découvrir que j'ai raté un rendez-vous administratif."

    "Tomas tape mon prénom, puis sélectionne un résultat. Ma photo apparaît aussitôt, accompagnée de mon district d'origine et de plusieurs informations personnelles."

    noam surpris "Ah ouais, c'est rapide. Je savais même pas que cette photo existait encore."
    tomas joie "Tu vois ! C'est exactement ça qui est fascinant. Ces données doivent venir de plusieurs registres et..."
    "Il s'interrompt. Son doigt reste immobile au-dessus de l'écran."
    noam reflexion "Quoi ?"
    tomas mefiant "Attends. Je veux vérifier un truc avant de dire une bêtise."
    "Je me penche à mon tour. Parmi les rubriques de ma fiche, l'une est intitulée « DATE DE DÉCÈS ». Le champ est vide."
    noam inquiet "C'est normal, ce truc ?"
    tomas panne "Sur certains registres, oui, bien sûr ! On prépare une fiche avec toutes les informations possibles, même celles qui ne serviront que plus tard. Enfin, ça ne veut pas dire que..."
    noam desaccord "Tomas, j'ai compris. Je te demande juste pourquoi c'est là."
    tomas reflechit "Je sais pas. Mais ce n'est peut-être qu'un modèle standard."
    noam inquiet "Tu peux ouvrir une autre fiche ?"
    "Il cherche le nom d'un autre représentant. La photo change, mais la même rubrique apparaît en bas de l'écran."
    tomas mefiant "Bon. C'est bien un champ prévu pour tout le monde."
    noam reflexion "Tout le monde dans le Conclave ou tous les habitants de la Terre ?"
    tomas surpris "Bonne question. Attends, je vais regarder un dossier qui n'est pas lié à nous."

    "Il lance une nouvelle recherche. Cette fois, avant même que le résultat s'affiche, une fenêtre rouge recouvre la console."

    "« AUTORISATION EXPIRÉE — SESSION INTERROMPUE »"

    noam surpris "C'est toi qui as fait ça ?"
    tomas panne "Non ! J'ai juste lancé une recherche ! Enfin, normalement, j'ai juste lancé une recherche..."
    "Il appuie deux fois sur le bouton de retour. La console refuse de réagir."
    noam inquiet "Tu crois qu'on a déclenché une alarme ?"
    tomas panne "J'espère pas. Je voulais pas fouiller dans des dossiers confidentiels, moi. Enfin si, un peu, mais je pensais pas que ça..."
    "Le message disparaît et l'écran revient tranquillement au catalogue de départ."

    noam taquin "Bon, on est toujours vivants. C'est encourageant."
    tomas rire "Ouais. Et nos dates de décès sont toujours vides, normalement."
    "Il réalise ce qu'il vient de dire et grimace immédiatement."
    tomas panne "Pardon. C'était une blague vraiment nulle."
    noam sourire "Au moins, ça change des explications techniques."
    tomas reflechit "Je vais essayer de comprendre pourquoi l'accès a sauté. Mais promis, je ne touche plus aux dossiers personnels sans savoir ce que je fais."
    noam taquin "C'est censé me rassurer ?"
    tomas rire "Pas complètement, non."

    "Je lui laisse la console. En sortant de cette partie des archives, je me surprends à repenser à cette rubrique absurde au bas de ma fiche. J'aurais préféré ne jamais savoir qu'elle existait."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES
    $ hideGroup()
    jump ARCHIVE_TP
