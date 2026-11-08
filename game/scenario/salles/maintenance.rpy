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
    think "La salle de maintenance ressemble davantage à l'intérieur d'une vraie station spatiale que les autres pièces. Ici, il y a enfin des outils, des câbles et des machines."

    call MAYBE_PLAY_SCRIPTED_DOOR("maintenance", "bg_maintenance") from _call_MAYBE_PLAY_SCRIPTED_DOOR_342
    scene bg_maintenance at adaptive_fullscreen with fade

    "Un énorme robot est installé au fond de l'atelier. Un homme inspecte une armoire de commande juste à côté, sans paraître particulièrement impressionné par la machine."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("kael", "neutre", 0.78),
    ])

    noam surpris "Ah ouais... C'est quoi, ce gros truc ?"
    kael neutre "Un robot d'intervention. Il peut travailler à l'extérieur de la station."
    noam sourire "Tu as l'air de connaître le modèle."
    kael reflechit "Pas celui-là précisément. Kael, au fait. Je viens d'Orbite."
    $ unlock_character_name("kael")
    noam sourire "Noam. Je peux regarder de plus près ?"
    kael neutre "Oui, mais évite les commandes. Je ne sais pas encore ce qu'elles font toutes."
    noam taquin "Je vais essayer de ne pas lancer une fusée par accident."

    "Je fais le tour du robot. Une étiquette indique « GROS BERTHE ». L'appareil est beaucoup plus massif que les robots de service que je connais."
    noam rire "Gros Berthe ? C'est vraiment son nom ?"
    kael sourire "C'est ce qui est écrit. J'espère que ce n'est pas le nom de la personne qui l'a conçu."
    noam reflexion "Et il fait quoi, exactement, à part prendre toute la place ?"
    kael reflechit "Des réparations en extérieur, du transport de charges et probablement de la sécurité. Le modèle peut normalement recevoir des équipements offensifs."
    noam inquiet "Un robot armé dans notre atelier ? Rassurant."
    kael neutre "Il n'a pas l'air équipé pour ça, ici."
    "Je me penche pour regarder un panneau de contrôle sur le flanc de la machine. Une petite touche tactile s'allume lorsque ma main passe devant."
    noam hesitation "Oups. J'ai fait quoi, là ?"
    kael surpris "Tu as touché quelque chose ?"
    "Un grondement léger retentit dans le châssis. Les yeux du robot s'éclairent et son torse commence à se redresser."
    noam peur "Euh, Kael ? Il vient de bouger !"
    kael determine "Recule, Noam. Ne touche plus à rien."
    "Je fais deux pas en arrière. Gros Berthe pivote lentement la tête dans notre direction et déploie un bras."
    noam inquiet "Il a pas un fusil caché là-dedans, au moins ?"
    kael reflechit "Normalement non, mais je préférerais ne pas vérifier en restant devant."
    "Un petit accessoire sort de son bras et se met à brosser le bord de son propre support. Le robot s'immobilise ensuite, comme s'il attendait qu'on l'applaudisse."
    noam surpris "Attends... Il est en train de faire le ménage ?"
    kael sourire "On dirait. Tu as dû activer une routine d'entretien."
    noam rire "J'ai cru qu'on allait se faire découper en deux et il sort une brosse !"
    kael taquin "Tu vois, il n'y a pas que moi qui ai besoin de lire les notices."
    "Kael coupe la routine à partir de l'armoire. Le robot replie docilement son bras."

    "En revenant vers la console, je remarque plusieurs circuits affichés sur un plan de la station."
    noam reflexion "Tu vérifiais ça quand je suis arrivé ?"
    kael neutre "Oui. Certains équipements ont une alimentation séparée. Je voulais savoir à quoi elle sert."
    noam sourire "Tu as trouvé ?"
    kael reflechit "Pas encore. Il y a plus de circuits que ce qu'on voit sur le plan public, mais ça peut être une simple réserve technique."
    noam taquin "Tu vas essayer de tous les retrouver ?"
    kael neutre "Probablement. C'est plus prudent de savoir ce qu'on peut couper ou réparer."
    "Il examine de nouveau le plan, puis revient au robot. J'ai l'impression qu'il aimerait poursuivre, mais qu'il préfère ne rien avancer sans être certain."
    noam sourire "Bon, je vais te laisser travailler avant d'activer son mode combat."
    kael taquin "Excellente idée. Et si tu repasses, préviens-moi avant de toucher à Gros Berthe."
    noam rire "Promis. Je veux pas le déranger pendant son ménage."
    "Je quitte l'atelier en l'entendant reprendre une vérification des circuits. Derrière lui, Gros Berthe n'a plus rien d'effrayant, mais je garde mes distances avec ses commandes."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_5
    $ hideGroup()
    jump MAINTENANCE_TP
