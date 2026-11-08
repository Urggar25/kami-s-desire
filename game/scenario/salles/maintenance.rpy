# -----------------------------------------------------------------------
# SALLE DE MAINTENANCE — même modèle que CANON
# - 2 persos seulement : Noam + Kael
# - Découverte : "l'envers" du Conclave (bruit, odeur d'huile, modules)
# - PNC : établi / armoire outils / panneau alimentation / retour
# - Détail : gros robot inerte au fond (repos/maintenance)
# -----------------------------------------------------------------------

default decouverte_salle_maintenance = False


label MAINTENANCE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_341
    scene bg_maintenance at adaptive_fullscreen

    if not decouverte_salle_maintenance and day_number() == 1:
        jump decouverte_salle_maintenance

    $ pnc_room = "pnc_maintenance"
    call screen pnc_maintenance()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_maintenance():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("maintenance")
    use room_scene_interactions("maintenance")

    if social_free_time_active() and character_has_available_free_time("kael"):
        imagebutton:
            idle Transform(character_image("kael", "neutre"), zoom=1.00)
            hover Transform(character_image("kael", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.48
            yalign 1.00
            action [SetVariable("last_room_label", "MAINTENANCE_TP"), SetVariable("free_time_selected_character", "kael"), Jump("FREE_TIME_CHARACTER_INTERACT")]



label MAINT_PNC_ETABLI:
    "Un établi métallique."
    "Des clés plates de toutes les formes et de toutes les tailles sont alignées."
    "Des tournevis magnétiques."
    "Un chiffon plié au carré."
    jump MAINTENANCE_TP

label MAINT_PNC_ROBOT:

    window auto

    "Au fond, une masse énorme."
    "Un robot."
    "Ou une machine qui ressemble à un robot."
    "Kael m'avait dit qu'il était spécialisé dans l'exploration spatiale."
    "Inerte."
    "Comme un animal endormi."

    "Des câbles partent de son dos."
    "Ils disparaissent dans le mur."
    "Il a des plaques de protection ouvertes."
    "On voit l’intérieur."
    "Des pièces qui brillent faiblement."

    "Il ne bouge pas."
    "Mais il respire presque."
    "Pas de souffle."
    "Juste un léger cycle de lumière."

    think "Le gros Berthe dont parlait Kael."
    think "Ici, même les machines ont droit à une pause."

    pause 0.3

    jump MAINTENANCE_TP


label maintenance1_etablit:
    jump MAINT_PNC_ETABLI


label maintenance1_porte_couloir_maintenance:
    $ corridor_current = "maintenance"
    jump EXIT_ROOM_TO_CORRIDOR


label maintenance2_robot:
    jump MAINT_PNC_ROBOT


label maintenance2_table_drone:
    "La table est couverte de modules de drones démontés."
    "Chaque pièce a sa place, jusqu'aux vis rangées par taille dans de petites alvéoles."
    "Un schéma de diagnostic attend sur l'écran, figé au milieu d'une séquence de calibrage."
    think "Quelqu'un compte revenir terminer ce travail."
    jump MAINTENANCE_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label MAINT_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_maintenance:
    $ decouverte_salle_maintenance = True
    scene black
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    think "La maintenance est nettement moins accueillante que les autres salles. Au moins, ici, personne n'a essayé de cacher les tuyaux derrière de jolies plaques."
    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_342
    scene bg_maintenance at adaptive_fullscreen with fade
    "Des outils sont alignés sur les établis. Un gros robot est installé au fond, relié à plusieurs câbles de charge."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("kael", "neutre", 0.78),
    ])
    "Un homme est accroupi devant une armoire électrique ouverte. Il referme doucement le panneau lorsqu'il m'entend arriver."
    noam hesitation "Je dérange ?"
    kael neutre "Non. Je regardais juste comment les circuits sont répartis."
    noam sourire "Tu t'y connais ?"
    kael sourire "Un peu. Kael, d'Orbite."
    $ unlock_character_name("kael")
    noam sourire "Noam. C'est pas exactement le coin le plus confortable du Conclave."
    kael taquin "C'est peut-être pour ça que je suis tranquille ici."
    "Je m'approche du robot. Il est bien plus grand que les modèles de service que j'ai déjà vus."
    noam surpris "Et ce machin ? Ils ont prévu de nous faire nettoyer les couloirs avec ?"
    kael reflechit "Non. Il s'appelle Gros Berthe, d'après l'étiquette. C'est un robot d'intervention spatiale."
    noam reflexion "Tu connais le modèle ?"
    kael neutre "Pas exactement celui-là. Il peut travailler à l'extérieur de la station, transporter du matériel et se défendre si nécessaire."
    noam inquiet "Se défendre comment ?"
    kael reflechit "Avec un armement embarqué, normalement. Mais je ne vois pas ses modules ici."
    noam taquin "Tu balances ça comme si tu me parlais d'une tondeuse."
    kael sourire "Désolé. Sur Orbite, ce genre de machine est moins impressionnant."
    "Kael regarde de nouveau les prises au sol, puis l'armoire qu'il vient de refermer."
    kael reflechit "Ce que je comprends moins, c'est la taille de l'installation. Il y a de quoi alimenter beaucoup plus d'équipements que ceux qu'on voit."
    noam reflexion "Peut-être qu'ils ont prévu large pour éviter les pannes."
    kael neutre "C'est possible. Je n'ai pas assez d'informations pour en dire davantage."
    noam sourire "Tu pourrais demander à Kami."
    kael taquin "Je pourrais. Je doute qu'elle me donne les plans."
    noam taquin "C'est sûr qu'elle a pas l'air du genre à partager ses secrets."
    kael reflechit "J'aimerais surtout savoir si quelqu'un ici peut réparer quelque chose sans déclencher une alarme. Avec douze personnes pendant un mois, une panne arrivera forcément."
    noam neutre "Et tu comptes t'en charger ?"
    kael fatigue "Si je peux aider, oui. Mais je préfère comprendre le matériel avant d'y toucher."
    "Il jette un dernier regard vers Gros Berthe, qui ne bouge pas."
    noam sourire "Je te laisse à tes circuits. Si je casse quelque chose, je saurai où venir."
    kael taquin "Essaie quand même de ne pas le faire exprès."
    noam rire "Je promets rien."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_5
    $ hideGroup()
    jump MAINTENANCE_TP
