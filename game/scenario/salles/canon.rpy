default decouverte_salle_canon = False

label CANON_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_330
    scene bg_canon at adaptive_fullscreen
    
    if not decouverte_salle_canon and day_number() == 1:
        jump decouverte_salle_canon
        
    $ pnc_room = "pnc_canon"
    call screen pnc_canon()

    if free_time_active:
        return
    if exploration_libre_active:
        return

# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_canon():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("canon")
    use room_scene_interactions("canon")


label canon1_ordinateur:
    jump CANON_PNC_CONSOLE


label canon1_porte_couloir_cafeteria:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label canon2_canon:
    jump CANON_PNC_CANON


label canon2_ciblage:
    "Une interface de ciblage recouvre tout un pan de la console."
    "Des coordonnées défilent lentement sous une grille verrouillée."
    "Chaque secteur habité possède déjà son repère, sa distance et son angle de tir."
    think "Ce n'est pas un système qu'on prépare en urgence."
    think "Tout est déjà mesuré. Il ne reste qu'à choisir où frapper."
    jump CANON_TP

label CANON_PNC_CANON:
    "Le canon est encore plus grand de près."
    "Des anneaux d’alimentation entourent son corps, comme des vertèbres."
    "Tout est propre."
    "Trop propre pour une arme qui tue."
    think "Même ici, ils ont pensé à l’esthétique."
    jump CANON_TP


label CANON_PNC_CONSOLE:
    "La console est verrouillée."
    "Des écrans affichent des graphiques, des flux, des lignes de paramètres."
    "Je reconnais quelques mots."
    "Charge."
    "Alignement."
    "Sécurité."
    "Et surtout… un statut."
    "\"PRÊT\"."
    think "Donc oui… il peut tirer. À tout moment."
    jump CANON_TP


label CANON_PNC_VITRE:
    "La vitre est épaisse, légèrement teintée."
    "Je pose la main dessus."
    "Froid immédiat."
    "Ça ne protège pas ceux dehors."
    "Ça protège ceux dedans."
    think "Ça protège le Conclave de ce que le canon fait."
    jump CANON_TP

# Optionnel : si tu ajoutes un bouton retour graphique
label CANON_PNC_EXIT:
    return

# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_canon:
    $ decouverte_salle_canon = True
    scene black
    play music "music/bgm_calm_not_peace.mp3" fadein 1.0
    think "J'avais remarqué cette salle sur le plan. Un canon installé à quelques couloirs de nos chambres, ça mérite au moins qu'on aille voir."
    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_331
    scene bg_canon at adaptive_fullscreen with fade
    "Les consoles sont allumées. Derrière une vitre épaisse, le canon occupe presque tout l'espace et pointe vers la Terre."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("ryn", "determine", 0.78),
    ])
    "Un homme s'est arrêté près des commandes. Il regarde l'arme sans même essayer de masquer son dégoût."
    noam hesitation "Je pensais pas que ce serait aussi gros."
    ryn colere "C'est donc de là qu'ils nous tiennent tous en laisse."
    noam reflexion "Tu sais si ce canon fonctionne vraiment ?"
    ryn neutre "Il a l'air prêt à tirer. Ils ont pas installé ça pour décorer, tu crois ?"
    noam sourire "Noam, au fait."
    ryn neutre "Ryn. Je viens de Limen."
    $ unlock_character_name("ryn")
    noam reflexion "Tu as déjà vu ce genre d'installation ?"
    ryn determine "Pas d'aussi près. Chez nous, on voit surtout ce qu'il reste après."
    "Il s'approche d'une console et pointe les coordonnées affichées. Chaque secteur possède une ligne de données et un statut."
    ryn colere "Regarde-moi ça. Ils ont déjà repéré les zones habitées. On dirait un foutu inventaire."
    noam inquiet "Il y a peut-être aussi des zones de surveillance."
    ryn desaccord "Arrête. On sait tous à quoi ça sert."
    play sound sfx_beep
    "Un signal retentit. Sur un écran, une ligne passe du gris à l'orange."
    noam surpris "Tu as touché quelque chose ?"
    ryn colere "Non. J'ai même pas approché mes mains."
    play music "music/bgm_system_override.mp3" fadein 1.0
    "Un second écran s'active. Une suite de coordonnées apparaît et le bruit de ventilation devient plus fort."
    noam inquiet "Ça se met en route tout seul ?"
    ryn determine "Écarte-toi de la console."
    play sound sfx_beep
    "Une alerte s'affiche : PROCÉDURE DE SANCTION. Le compte à rebours démarre."
    noam peur "Attends, c'est un tir réel ?"
    ryn inquiet "J'en sais rien. Mais on va pas rester devant les commandes."
    "Nous gagnons la partie vitrée de la salle, d'où l'on peut voir le canon sous un autre angle."
    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "canon2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_332
    scene canon2 at adaptive_fullscreen with fade
    $ showGroup([
        ("noam", "inquiet", 0.22),
        ("ryn", "determine", 0.78),
    ])
    "Des voyants passent au rouge sur les supports. Une vibration remonte dans le sol."
    noam inquiet "Il reste combien de temps ?"
    ryn colere2 "Ça change quoi ? On peut rien arrêter !"
    play sound sfx_gresillement
    "La vitre se teinte automatiquement. Je recule au moment où un grondement traverse toute la salle."
    play sound sfx_laser_canon volume 8.0
    with vpunch
    "Une lumière brutale éclaire les consoles, puis disparaît. Pendant quelques secondes, je n'entends presque plus rien."
    noam desespoir "Putain... Il vient vraiment de tirer."
    ryn fatigue "Ouais."
    "Sur l'écran, l'alerte est remplacée par une simple confirmation : SANCTION EXÉCUTÉE."
    noam peur "On ne sait même pas où il a frappé."
    ryn colere "Il y a quelqu'un, là-dessous, qui a dû faire un truc interdit. Et Kami vient de décider que ça suffisait pour le tuer."
    noam triste "On ne sait pas qui c'est. Ni ce qui s'est passé."
    ryn fatigue "C'est bien le problème."
    "Ryn reste les yeux fixés sur le message. La colère qu'il affichait en entrant a laissé place à quelque chose de plus difficile à lire."
    noam inquiet "On devrait retourner prévenir les autres."
    ryn determine "Ils savent déjà ce que fait Kami. Mais ouais, ça vaut le coup qu'ils voient cette salle."
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    noam reflexion "On va devoir voter à quelques mètres de cette arme..."
    ryn desaccord "Non. On va voter pendant qu'elle continue de tirer sur les gens qu'on est censés représenter."
    noam triste "Je crois que j'avais pas encore réalisé ce que ça voulait dire."
    ryn fatigue "Moi non plus. Pas comme ça."
    "Il quitte la vitre sans ajouter un mot. Je reste encore un instant devant l'écran, puis je le suis."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_2
    $ hideGroup()
    jump CANON_TP
