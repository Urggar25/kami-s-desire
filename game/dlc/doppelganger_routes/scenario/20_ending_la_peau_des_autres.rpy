# Fin alternative payante : préservée du script original J20.
# Déverrouillée uniquement lorsque le DLC « Les autres vies » est installé.
label kd_dlc_la_peau_des_autres:
    scene black
    stop music fadeout 0.25
    pause 1.5

    # À partir d'ici, Noam n'est plus le narrateur.
    # La narration passe volontairement à un point de vue externe.
    scene bg_salle_goumi_cachee at adaptive_fullscreen with creep_diss

    "Noam ne voit pas Kael se redresser."

    pause 0.8

    play sound "audio/sfx_duct_scrape.wav" volume 0.74

    "Il ne voit pas non plus la grille d'aération bouger derrière lui."

    play sound "audio/sfx_metal_open.mp3"

    "La grille s'ouvre."

    "Deux mains apparaissent."

    "Puis un visage."

    pause 0.8

    play music "audio/music/bgm_horror_pulse.mp3" fadein 1.2

    "Noam sort du conduit."

    "Le même visage."

    "Les mêmes cheveux."

    "Les mêmes vêtements."

    "Aucune hésitation."

    $ doppelganger_reveal(screamer=True, duration=0.96, restore_volume=0.56)

    "Le second Noam regarde Kael."

    "Kael désigne Iris d'un mouvement du menton."

    "Aucun des deux ne parle."

    "Noam se penche, passe un bras sous les épaules d'Iris et l'autre sous ses jambes."

    "Kael attrape le premier Noam sous les bras."

    "Les deux corps sont emportés dans le conduit."

    scene bg_conduit_reseau at adaptive_fullscreen with creep_diss

    "Le trajet dure plusieurs minutes."

    "Ils passent deux embranchements, descendent plus bas dans la structure, puis s'arrêtent devant une grille que Noam n'avait jamais vue."

    "Kael la déverrouille."

    "Derrière, il n'y a plus de conduit."

    "Il y a une salle."

    pause 0.8

    scene bg_laboratoire at adaptive_fullscreen with creep_diss

    "La pièce ressemble vaguement à une infirmerie."

    "Vaguement."

    "Il y a bien des écrans, des plateaux métalliques et des machines autour des murs, mais rien n'est disposé pour soigner quelqu'un."

    "Au centre, une énorme cuve verticale occupe presque toute la hauteur de la salle."

    "Quelque chose flotte à l'intérieur."

    $ unlock_gallery_image("bg_cg054")
    scene bg_cg054 at adaptive_fullscreen with creep_diss

    pause 0.7

    "Un corps."

    "Ou presque."

    "Deux bras."

    "Deux jambes."

    "Une tête."

    "Mais aucun visage vraiment terminé."

    "La peau est pâle, lisse, presque sans détail."

    "Kael dépose Noam au sol."

    "Le second Noam fait la même chose avec Iris."

    "Elle respire encore."

    "Faiblement."

    "Kael s'approche de la machine."

    "Il ouvre un compartiment, retire plusieurs pièces, en ajoute d'autres."

    "Certaines ressemblent à des poches médicales."

    "D'autres à des composants électroniques."

    "Impossible de savoir où s'arrête l'un et où commence l'autre."

    "Le second Noam reste debout près d'Iris."

    "Il la regarde."

    "Puis regarde la cuve."

    "Kael appuie sur l'écran."

    play sound "audio/sfx_tinnitus.wav" volume 0.38

    "La machine démarre."

    "Le liquide dans la cuve se met à tourner lentement."

    "La forme à l'intérieur tressaille."

    pause 0.8

    "Ses doigts bougent."

    "Puis ses bras."

    "Quelque chose change dans son visage."

    "Les contours se creusent."

    "Des cheveux apparaissent."

    "La couleur vient ensuite."

    pause 0.8

    "Rouge."

    "Le visage n'est plus vide."

    "C'est celui d'Iris."

    scene bg_cg054_1 at adaptive_fullscreen with memory_rip

    pause 1.0

    "La cuve se vide."

    "Le corps s'effondre contre la paroi."

    play sound "audio/sfx_metal_open.mp3"

    "La porte s'ouvre."

    "Iris tombe à genoux sur le sol, trempée, incapable de tenir debout correctement."

    iris panne "..."

    "Elle tousse."

    "Respire."

    "Regarde autour d'elle."

    "Puis elle fronce les sourcils."

    iris colere "...Putain..."

    "Elle passe une main tremblante sur son bras."

    iris fatigue "Il fait froid ici."

    "Kael lui tend une couverture."

    "Elle la prend sans poser de question."

    "Le second Noam sourit."

    scene bg_laboratoire at adaptive_fullscreen with dissolve

    "Quelques minutes plus tard, une porte latérale s'ouvre."

    "La lumière s'allume automatiquement."

    scene bg_cavite_technique at adaptive_fullscreen with creep_diss

    "Des corps sont entassés contre le fond de la pièce."

    "Pas des dizaines. Quelques uns."
    "Un qui ressemble à Mara. Un qui ressemble à Kael."

    pause 0.6

    "Mara est là. Le même corps que Noam avait trouvé sur la table quelques heures plus tôt."

    pause 0.6

    "À côté d'elle repose Kael."

    "Le vrai Kael."

    $ horror_audio_cut(duration=0.42, restore_volume=0.45)

    "Kael traîne le Noam inconscient dans la pièce."

    "Le second Noam fait la même chose avec Iris."

    "Ils les déposent à côté des autres."

    "Sans précaution particulière."

    "Comme s'ils rangeaient quelque chose."

    pause 0.8

    "Derrière eux, la nouvelle Iris apparaît dans l'encadrement de la porte."

    "Elle a maintenant une tenue sur le dos."

    "Ses cheveux sont encore humides."

    $ unlock_gallery_image("bg_cg055")
    scene bg_cg055 at adaptive_fullscreen with creep_diss

    "Elle regarde Mara."

    "Puis Kael."

    "Puis les deux Noam."

    "Son regard descend enfin sur Iris."

    pause 1.0

    iris reflexion "..."

    "Elle fixe son propre corps pendant quelques secondes. Son visage se ferme."

    iris colere "...C'est quoi ce bordel ?"

    kael sourire "Je vais tout t'expliquer !"

    scene black with signal_stutter
    stop music fadeout 0.2
    $ danger_off()

    pause 1.2

    call screen kd_ending_reached(
        "La peau des autres",
        "ENDING 01 // JOUR 20"
    )
    $ _ending_screen_closed = _return

    return
