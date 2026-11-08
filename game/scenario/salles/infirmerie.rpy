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
    think "Je préfère savoir où se trouve l'infirmerie avant que quelqu'un ait réellement besoin d'y venir."

    call MAYBE_PLAY_SCRIPTED_DOOR("infirmerie", "bg_infirmerie") from _call_MAYBE_PLAY_SCRIPTED_DOOR_340
    scene bg_infirmerie at adaptive_fullscreen with fade

    "Les lits, les armoires de médicaments et le matériel d'opération ont l'air neufs. Une femme examine le contenu d'un placard sans prêter attention à mon arrivée."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("sael", "neutre", 0.78),
    ])

    noam sourire "Salut. Je cherchais juste à voir comment on pourrait se soigner ici."
    sael neutre "Tu as de quoi faire. Les compresses sont là, les antiseptiques au-dessus. Il y a même de quoi suturer."
    noam surpris "Tu as l'air de t'y connaître."
    sael raison "Assez pour savoir quoi prendre quand quelqu'un saigne."
    "Elle replace une boîte sur son étagère et referme le placard."
    noam sourire "Noam, d'Harmonie."
    sael neutre "Sael. Limen."
    $ unlock_character_name("sael")
    noam reflexion "Tu vérifies les réserves ?"
    sael reflechit "Je regarde ce qui peut servir. Ça évite de chercher au dernier moment."

    "Je contourne un lit pour aller vers la pièce du fond. Une rangée de compartiments réfrigérés est installée contre le mur."

    noam hesitation "Et ça, c'est quoi ?"
    sael neutre "Des casiers mortuaires."
    noam surpris "Des... quoi ?"
    "Je me rapproche pour lire les étiquettes. La première porte le nom d'Elias. La suivante, celui de Mara."
    noam inquiet "Sael, viens voir. Il y a les noms des représentants dessus."
    "Elle me rejoint, regarde les deux premiers casiers, puis passe au suivant. Cette fois, c'est mon prénom."
    noam peur "Attends. Ils ont vraiment mis mon nom sur un tiroir à cadavre ?"
    "Sael ne répond pas. Elle parcourt le reste de la rangée, compte les compartiments du regard et s'arrête devant le dernier."
    noam inquiet "Dis quelque chose, parce que là, je commence sérieusement à flipper."
    sael mefiant "Douze."
    noam desaccord "J'ai vu qu'il y en avait douze. C'est justement ça le problème."
    "Sael saisit la poignée du casier portant mon nom. Avant que je puisse protester, elle le tire légèrement vers elle."
    noam peur "Hé ! Qu'est-ce que tu fais ?!"
    "Le compartiment glisse dans un bruit métallique. Il est vide. Sael le referme, puis ouvre celui d'à côté."
    noam inquiet "Tu peux m'expliquer pourquoi tu fais ça ?"
    sael raison "Je vérifie qu'ils sont vides."
    "Elle inspecte encore deux compartiments. Je la regarde faire, incapable de décider si son calme me rassure ou me fait encore plus peur."
    noam hesitation "Tu pensais vraiment qu'il pourrait déjà y avoir quelqu'un dedans ?"
    sael reflechit "Je savais pas. Maintenant, pour ceux-là, je sais."
    noam inquiet "Tu ne vas quand même pas tous les ouvrir ?"
    sael neutre "Si. Il y a des noms dessus."

    "Elle termine sa vérification. Quand elle referme le dernier casier, je remarque qu'elle prend soin de repousser complètement le tiroir avant de lâcher la poignée."

    noam triste "On est arrivés aujourd'hui, et quelqu'un a déjà prévu exactement où mettre nos corps."
    sael mefiant "Oui. Ça me plaît pas non plus."
    noam reflexion "Mais les Commandements empêchent les gens de s'entretuer."
    sael raison "Pas ici. Kami l'a dit."
    noam inquiet "Tu penses qu'elle s'attend à ce qu'on se tue entre nous ?"
    sael reflechit "Je sais pas ce qu'elle attend. Et je vais pas inventer une réponse pour te rassurer."

    "Elle revient vers l'armoire médicale, en sort quelques compresses et une bande, puis les dispose dans une petite pochette."

    noam reflexion "Tu fais quoi, maintenant ?"
    sael neutre "Une trousse. Si quelqu'un se blesse loin d'ici, on pourra au moins arrêter le sang."
    noam hesitation "Tu veux déjà te préparer à ça ?"
    sael desaccord "Je veux éviter que quelqu'un meure bêtement. C'est différent."
    "Elle vérifie le contenu de la pochette et m'en tend une seconde, plus petite."
    sael neutre "Tiens. Pour les coupures. Tu peux la garder."
    noam surpris "Ah... Merci."
    sael reflechit "Et ne laisse pas ça traîner. Une trousse ne sert à rien si tu sais pas où tu l'as mise."
    noam sourire "Je vais essayer de ne pas te décevoir dès le premier jour."
    sael neutre "Commence par ne pas te blesser."

    "Je range la pochette. Sael retourne aux armoires, mais je la vois jeter un dernier coup d'œil à la morgue avant de reprendre son inventaire."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_4
    $ hideGroup()
    jump INFIRMERIE_TP
