# -----------------------------------------------------------------------
# SALLE DE MAINTENANCE — même modèle que CANON
# - 2 persos seulement : Noam + Kael
# - Découverte : "l'envers" du Conclave (bruit, odeur d'huile, modules)
# - PNC : établi / armoire outils / panneau alimentation / retour
# - Détail : gros robot inerte au fond (repos/maintenance)
# -----------------------------------------------------------------------

default decouverte_salle_maintenance = False

label MAINTENANCE_TP:
    scene bg_maintenance at adaptive_fullscreen

    if not decouverte_salle_maintenance:
        jump decouverte_salle_maintenance

    $ pnc_room = "pnc_maintenance"
    call screen pnc_maintenance()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_maintenance():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_maintenance.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/salle_maintenance/etabli.png"
        hover "images/background/interact/salle_maintenance/etabli_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("MAINT_PNC_ETABLI")

    imagebutton:
        idle "images/background/interact/salle_maintenance/robot.png"
        hover "images/background/interact/salle_maintenance/robot_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("MAINT_PNC_ROBOT")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")



    if free_time_active and kael_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform("images/character/kael/neutre.png", zoom=0.75)
            hover Transform("images/character/kael/reflechit.png", zoom=0.75)
            focus_mask True
            xalign 0.48
            yalign 0.35
            action [SetVariable("last_room_label", "MAINTENANCE_TP"), Jump("KAEL_LINK_INTERACT")]
    if free_time_active and elias_link in [1, 3]:
        imagebutton:
            idle Transform("images/character/elias/neutre.png", zoom=0.75)
            hover Transform("images/character/elias/reflechit.png", zoom=0.75)
            focus_mask True
            xalign 0.72
            yalign 0.76
            action [SetVariable("last_room_label", "MAINTENANCE_TP"), Jump("ELIAS_LINK_INTERACT")]


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


# Optionnel : si tu ajoutes un bouton retour graphique
label MAINT_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_salle_maintenance:

    $ decouverte_salle_maintenance = True

    scene black
    play music "music/bgm_unsaid_distance.mp3" fadein 1.0

    think "Salle de maintenance."
    think "Le nom sonne comme une excuse."
    think "Comme si ici, on réparait juste des trucs."
    think "Si on devait réparer tout ce qui n'allait pas, il faudrait réparer le monde."

    pause 0.4

    scene bg_maintenance at adaptive_fullscreen with fade

    "Ça sent le métal chaud."
    "L’huile."
    "Et un truc plus sec, comme de la poussière d’électronique."
    "Le genre d’odeur qui colle au fond de la gorge."

    "La salle est grande."
    "Plus brute que le reste."
    "Des panneaux ouverts."
    "Des câbles dans des goulottes."
    "Des modules empilés sur des racks."

    "Et surtout : du silence."
    "Pas vraiment un silence doux mais assez reposant."
    "Un silence parfois perturbé par le vrombissement d'un moteur."

    $ showP("noam", "reflexion", 0.22)

    "Je fais deux pas."
    "Je m’arrête."
    "Parce que quelqu’un est déjà là."

    $ showP("kael", "neutre", 0.78)

    "Adossé à un support."
    "Les bras croisés."
    "Il a l’air parfaitement à sa place."

    $ showP("noam", "hesitation", 0.22)
    noam "Je te dérange ?"

    $ showP("kael", "taquin", 0.78)
    kael "Non."
    kael "J’avais juste besoin d’un endroit tranquille."
    kael "Noam c'est ça ? Moi c'est Kael."
    
    noam "Ouai."
    noam "On est vraiment dans un endroit étrange."

    $ showP("noam", "rire", 0.22)
    "Je souffle, un rire court."
    $ showP("noam", "reflexion", 0.22)
    "Sans conviction."

    $ showP("kael", "reflechit", 0.78)
    kael "T’as vu le reste ?"
    kael "La cafétéria, les salles…"
    kael "On dirait un campus."
    kael "Sauf que personne n’a choisi de s'y inscrire."
    kael "Tout le monde court partout, c'est assez bruyant."
    kael "Ici les gens n'y passent que quelques minutes. C'est assez calme."

    $ showP("noam", "desaccord", 0.22)
    noam "Ouais tu m'étonnes."
    noam "L'odeur d'huile peut en rébuter plus d'un."

    $ showP("kael", "rire", 0.78)
    kael "Exactement."
    kael "Au moins on est au calme ici."

    "Il hoche la tête vers le fond."
    "Je suis son regard."

    "Une masse inerte imposante est tranquillement entreposée à l'arrière de la salle."
    "Un gros robot. Il fait bien trois mètres de haut."
    "On pourrait presque avoir l'impression qu'il va se mettre à bouger d'un instant à l'autre."

    $ showP("noam", "surpris", 0.22)
    noam "C’est… quoi ça ? C'est impressionnant !"

    $ showP("kael", "reflechit", 0.78)
    kael "Le gros Berthe."
    kael "C’est comme ça qu’il s’appelle apparemment."
    
    "Kael montre du doigt une plaque derrière lui qui indique le nom du robot."
    "Enfin, je ne sais même pas si on peut vraiment appeler ça comme ça."
    
    $ showP("noam", "reflexion", 0.22)
    noam "Donc c’est pas juste un machin oublié."

    $ showP("kael", "neutre", 0.78)
    kael "Non."
    kael "C’est entretenu."
    kael "Et si c’est entretenu…"
    kael "c’est que ça peut servir."
    
    kael "Honnêtement, c'est pas si impressionnant que ça."
    kael "Il y a des prototypes beaucoup plus robustes ou rapides sur orbite."
    kael "Mais ça a l'air fonctionnel."

    pause 0.3

    $ showP("noam", "inquiet", 0.22)
    noam "Tu penses qu’il sert à quoi ?"

    $ showP("kael", "reflechit", 0.78)
    kael "C'est un modèle conçu pour deux raisons."
    
    "Il prend un temps de réponse, comme pour réfléchir à quels mots utiliser."
    
    kael "Il peut servir d'arme. Il est normalement équipé de fusils laser."
    kael "Mais ce n'est pas son point fort."
    kael "Il peut surtout aller dans l'espace."

    "Il dit ça calmement."
    "Trop calmement."
    "Comme s’il parlait de la météo."
    
    kael "Malgré sa taille, il est équipé de propulseurs, avec la faible gravité, il peut parcourir une longue distance sans problème."
    kael "C'est un robot d'exploration spatiale."

    $ showP("noam", "peur", 0.22)
    "Ça me fait froid dans le dos."

    pause 0.4

    $ showP("kael", "taquin", 0.78)
    kael "Bref."
    kael "Je suis venu ici pour réfléchir tranquillement à un truc."

    $ showP("noam", "reflexion", 0.22)
    noam "Pour réfléchir ?"

    $ showP("kael", "reflechit", 0.78)
    kael "Tu sais cette histoire d'amendements."
    kael "Les propositions."
    kael "Tout ce cirque."

    $ showP("noam", "desaccord", 0.22)
    noam "Tu vas pas me dire que t’es enthousiaste."

    $ showP("kael", "rire", 0.78)
    kael "Non. A quoi ça servirait ?"
    kael "Honnêtement, pour moi ce Conclave est plus un risque que quoi que ce soit."

    $ showP("kael", "culpabilite", 0.78)
    kael "Je pense qu’on devrait annoncer très vite aux autres nos propositions."
    kael "Pas juste ce qu'on vote."
    kael "Parce qu'à la moindre erreur des milliers de gens peuvent mourir par notre faute."

    $ showP("noam", "hesitation", 0.22)
    noam "Tu ne fais confiance en personne ?"

    $ showP("kael", "reflechit", 0.78)
    kael "Ce n'est pas ça."
    kael "Quand les gens paniquent, ils s’accrochent à n’importe quoi."
    kael "Si on en parle avant, nos propositions seront mieux cadrées et on est à peu près sûrs d'éviter une catastrophe."

    pause 0.3

    "Je regarde autour."
    "L’établi."
    "L’armoire."
    "Le panneau d’alimentation."
    "Tout est là."
    "Tout est prêt."

    $ showP("noam", "reflexion", 0.22)
    noam "Tu veux faire ça quand ?"
    noam "Tu as tenté d'en parler tout à l'heure, sans trop de réponses ..."

    $ showP("kael", "fatigue", 0.78)
    kael "Bientôt. Juste avant de déposer les amendements."
    kael "C'est vraiment nécessaire."
    
    "Il regarde dans le vide, comme perdu dans ses pensées."

    $ showP("noam", "culpabilite", 0.22)
    "Tu penses qu'on arrivera à faire avancer les choses ?"

    $ showP("noam", "triste", 0.22)
    noam "Je ne pense pas."

    $ showP("kael", "neutre", 0.78)
    kael "Et toi, Noam…"
    kael "t’as l’air de porter un sac qui n’est pas à toi."
    kael "Quelle modification vas-tu proposer ?"

    $ showP("noam", "desaccord", 0.22)
    noam "Franchement ? J'en sais rien du tout."

    $ showP("kael", "reflechit", 0.78)
    kael "C’est pas vraiment une réponse."

    pause 0.4

    $ showP("noam", "desespoir", 0.22)
    noam "Je sais."
    noam "Mais là, j’ai pas mieux."

    $ showP("kael", "neutre", 0.78)
    kael "Ouai je vois."
    kael "On est tous dans le même sac."

    "Il lance un regard au panneau d’alimentation."

    pause 0.5

    think "Cette salle de maintenance ressemble plus à un atelier."
    think "Et ce n'est pas pour me déplaire."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_5

    jump MAINTENANCE_TP

# 3m
# Total : 43m25
