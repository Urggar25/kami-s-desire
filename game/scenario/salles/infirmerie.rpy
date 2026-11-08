# -----------------------------------------------------------------------
# INFIRMERIE — même modèle que CANON
# - 2 persos seulement : Noam + Sael
# - Découverte : violence autorisée au Conclave (hors commandements)
# - PNC : casiers réfrigérés (morgue) / étagères (médicaments-poisons) /
#         table d'opération / bibliothèque scientifique / retour
# -----------------------------------------------------------------------

default decouverte_infirmerie = False


label INFIRMERIE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "bg_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_339
    scene bg_infirmerie at adaptive_fullscreen

    if not decouverte_infirmerie and day_number() == 1:
        jump decouverte_infirmerie

    $ pnc_room = "pnc_infirmerie"
    call screen pnc_infirmerie()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_infirmerie():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("infirmerie")
    use room_scene_interactions("infirmerie")


label infirmerie1_porte_couloir_infirmerie:
    $ corridor_current = "infirmerie"
    jump EXIT_ROOM_TO_CORRIDOR


label infirmerie1_armoire:
    jump INF_PNC_ETAGERES


label infirmerie2_lits:
    "Trois lits médicaux sont séparés par des rideaux trop fins pour offrir une vraie intimité."
    "Les moniteurs sont allumés et affichent des constantes de test parfaitement normales."
    "Sous chaque lit, une caisse contient le matériel d'urgence nécessaire."
    think "Ils ont prévu plusieurs blessés à la fois."
    jump INFIRMERIE_TP


label infirmerie3_morgue:
    jump INF_PNC_MORGUE


label infirmerie3_operation:
    jump INF_PNC_TABLE



label INF_PNC_MORGUE:
    window auto

    "Les casiers réfrigérés occupent tout un pan de mur."
    "Des tiroirs longs."
    "Numérotés."
    "Avec des poignées épaisses."
    "Comme si on devait tirer fort."
    "Ou vite."

    think "Une morgue."
    think "Dans un endroit censé être… notre 'refuge'."

    "Le froid qui s’en dégage est propre."
    "Trop propre."
    "Ça sent le métal stérile et la désinfection."

    think "Ils ont prévu la place."
    think "Donc ils ont prévu le reste."

    jump INFIRMERIE_TP


label INF_PNC_ETAGERES:
    window auto

    "À gauche, des étagères pleines."
    "Boîtes blanches."
    "Flacons ambrés."
    "Poches scellées."
    "Certaines étiquettes sont nettes."
    "D’autres… volontairement vagues."

    "Je lis quelques mots."
    "Analgésique."
    "Sédatif."
    "Antibiotique."
    "Antidote."
    "Et, plus bas…"
    "Des symboles de danger."

    think "Médicaments et poisons."
    think "La frontière est parfois une question de dose."

    jump INFIRMERIE_TP


label INF_PNC_TABLE:
    window auto

    "Au fond, une table d’opération."
    "Éclairage directionnel."
    "Bras articulés."
    "Des instruments rangés dans des tiroirs."
    "Des machines qui attendent."
    "Écran de monitoring noir."
    "Comme un œil fermé."

    "Ça ne ressemble pas à une infirmerie de bureau."
    "Ça ressemble à un bloc."

    think "Donc ici… on répare."
    think "Ou on découpe."

    jump INFIRMERIE_TP


label INF_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_infirmerie:
    $ decouverte_infirmerie = True
    scene black
    play music "music/bgm_cold_metadata.mp3" fadein 1.0
    think "Je préfère vérifier où on pourra se faire soigner. Avec un mois à passer ici, ce serait idiot de découvrir l'infirmerie au moment d'en avoir besoin."
    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "bg_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_340
    scene bg_infirmerie at adaptive_fullscreen with fade
    "L'endroit est bien équipé : lits d'examen, armoires de médicaments, matériel d'urgence et une salle d'opération derrière une vitre."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("sael", "neutre", 0.78),
    ])
    "Une femme inspecte les étagères. Elle contrôle l'étiquette d'une boîte, puis la remet exactement à sa place."
    noam sourire "Salut. Tu travailles dans le médical ?"
    sael neutre "Non. Je regarde ce qu'on a."
    noam hesitation "Ah. Je cherchais juste de quoi soigner une blessure, au cas où."
    sael raison "Pansements, antiseptiques et sutures dans l'armoire de gauche. Il y a aussi de quoi traiter les blessures graves."
    noam surpris "Tu as trouvé tout ça en deux minutes ?"
    sael neutre "Je sais ce qu'il faut chercher."
    noam sourire "Moi c'est Noam, d'Harmonie."
    sael neutre "Sael. Limen."
    $ unlock_character_name("sael")
    noam reflexion "Tu as l'habitude de te soigner toute seule ?"
    sael reflechit "Quand tu es loin d'un dispensaire, tu n'attends pas qu'un médecin arrive pour arrêter une hémorragie."
    "Elle indique d'un mouvement de tête la zone derrière moi. Je me retourne et remarque plusieurs compartiments réfrigérés, avec des noms inscrits dessus."
    noam inquiet "Attends, c'est quoi, ces tiroirs ?"
    sael neutre "La morgue."
    noam peur "Ils ont prévu une morgue ? Ici ?"
    sael raison "Lis les étiquettes."
    "Je reconnais plusieurs prénoms parmi ceux entendus plus tôt. Même les emplacements vides portent déjà une identification."
    noam inquiet "Ils ont préparé une place pour chacun de nous..."
    sael reflechit "Oui. Ils n'ont pas attendu qu'il y ait un mort."
    noam desaccord "Mais les Commandements interdisent la violence."
    sael raison "Sur Terre. Kami a dit qu'ils étaient suspendus ici."
    noam inquiet "Je savais que les règles étaient différentes, mais de là à prévoir nos corps..."
    sael mefiant "Prévoir n'est pas provoquer. On ignore pourquoi ils ont installé ça."
    "Sael s'approche d'une autre armoire et vérifie son verrou. Il cède sans difficulté."
    noam reflexion "On peut vraiment ouvrir les réserves de médicaments ?"
    sael reflechit "Apparemment. Il y a des calmants, des anesthésiques et aussi des produits dangereux. Rien ne devrait être accessible comme ça."
    noam inquiet "On devrait peut-être prévenir les autres."
    sael raison "Pour la morgue, oui. Et pour les médicaments, mieux vaut que chacun sache ce qu'il ne faut pas toucher."
    noam hesitation "Tu n'as pas l'air très surprise."
    sael fatigue "J'ai vu des gens mourir parce que personne n'avait prévu de quoi les aider. Ça ne veut pas dire que j'aime voir leurs noms sur des tiroirs."
    "Elle referme l'armoire et vérifie une dernière fois que la porte tient."
    sael neutre "J'emporte rien. Mais maintenant, je sais où sont les soins."
    noam neutre "J'espère qu'on n'aura jamais à s'en servir."
    sael reflechit "Moi aussi. Ça ne coûte rien d'être prêt."
    "Sael retourne à son inventaire. Je quitte la zone des casiers sans réussir à oublier les noms que j'y ai lus."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_4
    $ hideGroup()
    jump INFIRMERIE_TP
