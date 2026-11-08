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
    think "J'ai aperçu cette salle sur le plan. J'aimerais bien comprendre pourquoi Kami tient à garder son canon aussi près de nous."

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "bg_canon") from _call_MAYBE_PLAY_SCRIPTED_DOOR_331
    scene bg_canon at adaptive_fullscreen with fade

    "L'arme occupe presque toute la salle. Des câbles épais remontent jusqu'au plafond, tandis que les consoles affichent des coordonnées sur la Terre."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("ryn", "determine", 0.78),
    ])

    "Un homme se tient près d'une console. Il s'est approché assez près pour pouvoir lire l'écran, mais ses mains restent fermement le long du corps."
    noam hesitation "Tu crois qu'il est en service ?"
    ryn colere "Tu vois un gros canon branché, des écrans allumés et des cibles. À ton avis ?"
    noam desaccord "Je posais juste la question."
    ryn fatigue "Ouais. Excuse. C'est ce truc qui me fout en rogne."
    noam sourire "Moi c'est Noam."
    ryn neutre "Ryn. Limen."
    $ unlock_character_name("ryn")
    "Il me fait signe d'approcher. Sur l'écran, une carte de la Terre est découpée en secteurs."
    ryn determine "Ils ont tout préparé. Même pas besoin de chercher où tirer, ça doit être enregistré depuis des mois."
    noam inquiet "Tu crois qu'il y a un moyen de voir sur quelle zone il est braqué ?"
    ryn neutre "J'en sais rien. Je préfère pas toucher à ces commandes."

    play sound sfx_beep
    "Un bip nous interrompt. Une ligne de la carte passe à l'orange, et un second écran affiche un compte à rebours."

    noam surpris "C'est toi qui as fait quelque chose ?"
    ryn colere "Non ! Bouge pas, laisse-moi lire."
    play music "music/bgm_system_override.mp3" fadein 1.0
    "La mention « SANCTION EN PRÉPARATION » apparaît au-dessus des coordonnées. Ryn se penche brusquement sur l'écran."
    ryn surpris "Attends..."
    noam inquiet "Quoi ?"
    ryn inquiet "Cette région... Je connais ce coin."
    noam peur "Tu sais où ça va tirer ?"
    ryn colere2 "C'est du côté de Limen. Putain, ils peuvent pas nous montrer un nom de ville au lieu de tous ces chiffres ?"
    "Il tente d'agrandir la carte. Un verrou s'affiche sur les commandes."
    noam inquiet "Ryn, touche pas n'importe quoi !"
    ryn colere "Il y a des villages là-bas ! Je veux juste savoir où ça tombe !"
    play sound sfx_beep
    "Le compte à rebours poursuit sa course. Ryn frappe du plat de la main sur le rebord de la console."
    ryn determine "Allez, donne-moi au moins le secteur exact..."
    noam peur "Il faut s'éloigner !"

    call MAYBE_PLAY_SCRIPTED_DOOR("canon", "canon2") from _call_MAYBE_PLAY_SCRIPTED_DOOR_332
    scene canon2 at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "inquiet", 0.22),
        ("ryn", "determine", 0.78),
    ])

    "Nous reculons vers la vitre. Le canon pivote lentement tandis que les éclairages de sécurité passent au rouge."
    ryn inquiet "J'arrive même pas à lire la position exacte... Si ça se trouve, c'est à des centaines de kilomètres de chez moi."
    noam hesitation "C'est possible. On n'en sait rien."
    ryn colere2 "Ouais, ben c'est ça qui me rend dingue !"
    play sound sfx_gresillement
    "La vitre s'assombrit d'un coup. Le sol tremble sous nos pieds."
    play sound sfx_laser_canon volume 8.0
    with vpunch
    "Un éclat blanc traverse la pièce. Je porte instinctivement les bras devant mon visage, même si le tir est dirigé loin de nous."

    "Lorsque les écrans redeviennent lisibles, le compte à rebours a disparu. Une nouvelle ligne indique simplement : « SANCTION EXÉCUTÉE »."
    noam desespoir "Il a vraiment tiré..."
    "Ryn retourne immédiatement à la console, mais les coordonnées ont déjà été effacées."
    ryn colere "Mais remets-les ! Je veux savoir où t'as tiré, saloperie !"
    noam inquiet "Ryn..."
    ryn colere2 "Il y a des gens qui vivent là-bas, Noam. Des familles ! Et moi je suis coincé ici à regarder un écran qui veut même pas me dire où ils sont !"
    "Il s'arrête, les deux mains appuyées sur le bord de la console. Pendant quelques secondes, je n'ose pas m'approcher."
    noam triste "On peut peut-être demander à Kami. Je sais pas si elle répondra, mais on peut essayer."
    ryn fatigue "Ouais. Peut-être."
    "Il lâche enfin la console et se passe une main sur le visage."
    ryn reflechit "Tu sais ce qui me fait le plus peur ? Même si c'était pas près de chez moi, ça voudrait dire que c'est tombé chez quelqu'un d'autre."
    noam triste "Je sais."
    play music "music/bgm_introspective_atmosphere.mp3" fadein 1.0
    ryn fatigue "Je vais sortir. J'en ai assez vu."
    noam neutre "Je viens avec toi."
    "Je jette un dernier regard à l'écran. La machine est déjà revenue à son état initial, prête à recommencer."

    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_2
    $ hideGroup()
    jump CANON_TP
