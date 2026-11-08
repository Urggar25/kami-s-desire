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
    think "Les archives. Je m'attendais à quelques rayonnages, pas à une salle qui prend tout un étage."
    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "bg_archive") from _call_MAYBE_PLAY_SCRIPTED_DOOR_325
    scene bg_archive at adaptive_fullscreen with fade
    "Des étagères et des modules de stockage occupent presque tout l'espace. Au fond, plusieurs postes sont déjà allumés."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])
    "Un grand type examine un rayon en fronçant les sourcils. Il retire un dossier, le remet à sa place, puis en sort un deuxième."
    tomas reflechit "Ils ont vraiment mélangé les documents papier avec des supports numériques ? Ça va être un enfer pour retrouver quoi que ce soit."
    noam taquin "Tu viens d'arriver et tu critiques déjà le classement ?"
    tomas surpris "Ah ! Désolé, je t'avais pas entendu. Je cherchais juste à comprendre leur système."
    noam sourire "Noam. Et toi ?"
    tomas neutre "Tomas. Je viens d'Archive, alors forcément, ce genre de salle m'intéresse."
    $ unlock_character_name("tomas")
    noam taquin "Ça tombe bien. Moi, j'étais surtout venu vérifier qu'ils avaient pas rangé les notices de survie au milieu des romans."
    tomas rire "Tu plaisantes, mais il y a des archives où ce serait un vrai problème. Enfin, pas exactement pour cette raison..."
    tomas panne "Pardon. Je vais éviter de te faire un cours dès notre première conversation."
    noam sourire "Merci, j'apprécie l'effort."
    "Tomas remet le dossier en place et se dirige vers le poste central. Au bout de quelques secondes, il m'appelle."
    tomas reflechit "Viens voir. Je pensais pouvoir ouvrir un catalogue, mais ce truc n'affiche que des codes."
    call MAYBE_PLAY_SCRIPTED_DOOR("archive", "archive2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_326
    scene archive2 at adaptive_fullscreen with fade
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("tomas", "neutre", 0.78),
    ])
    "Une carte de la Terre flotte au-dessus de la console. À côté, des lignes de données défilent sans titre ni explication."
    noam reflexion "Tu arrives à lire quelque chose là-dedans ?"
    tomas reflechit "Des dates, des identifiants et des niveaux d'accès. Je reconnais la structure, mais pas les catégories."
    noam neutre "Essaie celui-là, il a au moins une date."
    "Tomas sélectionne la ligne. Trois mentions apparaissent : VALIDÉ, BLOQUÉ et EXÉCUTÉ."
    noam inquiet "Exécuté ? C'est un dossier judiciaire ?"
    tomas mefiant "Je sais pas. Ce qui m'intrigue, c'est qu'il n'y a même pas de résumé. Un archiviste humain ne travaillerait jamais comme ça."
    noam reflexion "Ça pourrait être une sauvegarde destinée aux machines, non ?"
    tomas surpris "Oui, justement ! Les informations sont sûrement liées entre elles par des identifiants. La machine n'a pas besoin d'un titre pour comprendre ce qu'elle consulte."
    noam taquin "Tu vois, j'ai réussi à dire un truc utile."
    tomas rire "Et moi j'ai réussi à l'expliquer sans partir dans l'histoire complète du classement documentaire. On progresse tous les deux."
    "Il essaie d'ouvrir une autre entrée. La console affiche une demande d'autorisation, puis revient à l'écran précédent."
    tomas reflechit "Bon, l'accès est limité. Je peux consulter l'index, mais pas les dossiers."
    noam neutre "Donc il y a des archives partout, sauf qu'on ne peut pas vraiment les lire. Pratique."
    tomas mefiant "C'est déjà intéressant de voir ce qui existe. Si je comprends comment c'est classé, je trouverai peut-être ce qu'on a le droit d'ouvrir."
    noam sourire "Je te laisse fouiller. Tu as l'air de t'amuser, au moins."
    tomas joie "Ouais ! Enfin, j'aurais préféré avoir un vrai moteur de recherche, mais je vais faire avec."
    "Je le laisse devant la console. Il est déjà reparti dans ses recherches et ne remarque même pas que je m'éloigne."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES
    $ hideGroup()
    jump ARCHIVE_TP
