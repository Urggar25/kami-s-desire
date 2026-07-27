# -----------------------------------------------------------------------
# CAFÉTÉRIA — même modèle que OBSERVATION / CANON
# - Persos : Noam + Elen
# - Rencontre : Goumi (robot cuisinier) — pas de sprite, mais il parle
# - PNC : frigo-machine / tables / goumi / retour
# -----------------------------------------------------------------------

default decouverte_cafeteria = False



label CAFETERIA_TP:
    scene bg_cafeteria at adaptive_fullscreen

    if current_scene_active == "_2_ROUTE_CAFETERIA":
        $ current_scene_active = None
        jump _2_CAFETERIA_ANNONCE_KAMI

    if current_scene_active == "_3_ROUTE_CAFETERIA":
        $ current_scene_active = None
        jump _3_CAFETERIA_ARRIVE

    if not decouverte_cafeteria and day_number() == 1:
        jump decouverte_cafeteria

    $ pnc_room = "pnc_cafeteria"
    call screen pnc_cafeteria()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_cafeteria():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("cafeteria")
    use room_scene_interactions("cafeteria")
    if social_free_time_active() and mara_link in [0, 2, 4]:
        imagebutton:
            idle Transform(character_image("mara", "sourire"), zoom=0.75)
            hover Transform(character_image("mara", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.15
            yalign 0.30
            action [SetVariable("last_room_label", "CAFETERIA_TP"), Jump("MARA_LINK_INTERACT")]


    if social_free_time_active() and lysa_link == 1:
        imagebutton:
            idle Transform(character_image("lysa", "sourire"), zoom=0.75)
            hover Transform(character_image("lysa", "taquin"), zoom=0.75)
            focus_mask True
            xalign 0.82
            yalign 0.30
            action [SetVariable("last_room_label", "CAFETERIA_TP"), Jump("LYSA_LINK_INTERACT")]

    if social_free_time_active() and elen_link == 1:
        imagebutton:
            idle Transform(character_image("elen", "joie"), zoom=0.75)
            hover Transform(character_image("elen", "content"), zoom=0.75)
            focus_mask True
            xalign 0.50
            yalign 0.30
            action [SetVariable("last_room_label", "CAFETERIA_TP"), Jump("ELEN_LINK_INTERACT")]

    if j10011_waiting_elias:
        imagebutton:
            idle Transform(character_image("elias", "fatigue"), zoom=0.75)
            hover Transform(character_image("elias", "inquiet"), zoom=0.75)
            focus_mask True
            xalign 0.58
            yalign 0.30
            action Jump("_10_0_1_1_CAFETERIA_ELIAS")



label cafeteria1_porte:
    $ corridor_current = "cafeteria"
    jump EXIT_ROOM_TO_CORRIDOR


label cafeteria1_table:

    window auto

    "Des tables."
    "Des chaises."
    "Un espace pensé pour faire comme si on vivait ici."

    think "Ça pourrait presque marcher."
    jump CAFETERIA_TP


label cafeteria1_television:

    if day_number() == 4:
        call screen day4_news_screen()
        jump CAFETERIA_TP

    think "Les informations défilent sans rien m'apprendre de neuf."
    jump CAFETERIA_TP


label cafeteria2_cuisine:

    window auto

    "Le comptoir est clean."
    "Trop clean."
    "Comme si personne n'avait le droit d'y laisser une miette."

    "Derrière, le frigo-machine ronronne."
    "Et Goumi reste planté là, immobile."
    "Il me suit avec ses yeux-lentilles, sans bouger d'un millimètre."

    goumi "Souhaitez-vous une préparation nutritionnelle ?"

    think "Nutritionnelle ? Et puis quoi encore. Je préfère largement la nourriture bien grasse."
    jump CAFETERIA_TP


label cafeteria2_distributeur:

    window auto

    "La machine au fond ressemble à un frigo."
    "Sauf qu'elle fait la taille d'une armoire industrielle."

    "Écran tactile."
    "Tiroirs verrouillés."
    "Et une liste de catégories et d'aliments qui défile."

    think "Au moins ça n'a pas l'air d'être très compliqué."
    jump CAFETERIA_TP


label cafeteria2_tablette_commande:
    "La tablette de commande affiche des catégories propres, trop propres."
    "Entrées, plats, desserts, boissons."
    "Tout est rangé comme si le choix était une simple question d'interface."
    think "C'est pratique. Et vaguement humiliant."
    jump CAFETERIA_TP


label cafeteria3_reserve:

    window auto

    "La réserve est verrouillée."
    "Derrière la vitre, les stocks sont alignés avec une précision clinique."

    if cafeteria_food_visible_count() >= 5:
        think "Il y a encore de quoi tenir. Pour l'instant."
    elif cafeteria_food_visible_count() >= 3:
        think "Les rangées ont déjà l'air moins pleines."
    elif cafeteria_food_visible_count() >= 1:
        think "Il reste peu de choses visibles. Trop peu pour que ce soit rassurant."
    else:
        think "Vide. Ou assez proche du vide pour que mon estomac comprenne le message."
    jump CAFETERIA_TP


label cafeteria3_nourriture:

    window auto

    "Je regarde les portions restantes."
    "Tout est propre, emballé, calibré."
    "Même la nourriture a l'air de suivre un protocole."

    think "On ne mesure pas seulement ce qu'il reste à manger."
    think "On mesure combien de temps on peut encore faire semblant que tout va bien."
    jump CAFETERIA_TP


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_cafeteria:

    $ decouverte_cafeteria = True

    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0

    think "La cafétéria."
    think "Le seul endroit où je m'attends à voir des humains faire semblant d'aller bien."
    think "Et sans doute l'endroit qui sera le plus animé de tout le Conclave."

    pause 0.4

    scene bg_cafeteria at adaptive_fullscreen with fade

    "L'endroit est plus chaleureux que le reste."
    "Enfin… aussi chaleureux que du métal brossé et des néons peuvent l'être."

    "Des tables."
    "Des chaises."
    "De quoi manger un bon repas."
    "Au fond, il y a une énorme machine qui ressemble à un frigo."

    "Derrière le comptoir, quelque chose bouge."
    "Un petit robot un peu spécial."
    "Ce n'est pas Kami. Mais c'est assez semblable."
    "C'est clairement… un truc de la même famille."

    "Et juste devant, une voix."
    "Familiarité immédiate : ça parle fort."
    
    scene bg_cg008 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg008")

    elen vide "Non mais attends."
    elen vide "Tu me dis que tu peux genre VRAI-MENT cuisiner 'n'importe quoi'."
    elen vide "Et tu me sors un menu en quatre catégories."

    goumi vide "Correction : en six catégories."
    goumi vide "Mise en bouche, Entrée froide, entrée chaude, plat, fromage et enfin dessert."
    goumi vide "Vous pouvez commander ce que vous voulez. Tant que je suis approvisionné, je peux tout faire."

    "Je m'arrête à l'entrée."
    "Je ne sais pas si j'interromps une scène de présentation…"
    "Ou une petite scène de ménage."
    $ hideGroup()

    scene bg_cg008_1 at adaptive_fullscreen with fade
    
    noam vide "Je dérange ?"

    elen vide "Oh."
    elen vide "Non. Viens."
    elen vide "J'essayais juste de comprendre comment on allait être nourris…"

    goumi vide "Alimentation : active."
    goumi vide "Stock : remplis."
    goumi vide "Gestion : optimale."

    elen vide "Raah j'aime pas ce mode de discussion ! On dirait vraiment un robot limité."
    elen vide "C'est pas très naturel."

    "Je souffle un petit rire."
    "Tu t'attendais à quoi en même temps."

    elen vide "Je te présente Goumi."
    elen vide "Apparemment c'est le chef de cette cafét."
    elen vide "Il peut cuisiner à peu près tout ce qu'on veut, tant que c'est dans ses heures de boulot."
    
    noam vide "Dans ses heures de boulot ? Mais c'est un robot ..."

    goumi vide "Je suis Goumi."
    goumi vide "Unité culinaire autonome."
    goumi vide "Je peux préparer toute recette demandée par un représentant."
    goumi vide "Dans la limite des stock disponible."
    goumi vide "Je travaille de 6h du matin à 14h puis de 17h à 22h."
    goumi vide "Le reste du temps est destiné à ma recharge."

    elen vide "Il a au moins le mérite d'être honnête."
    elen vide "C'est déjà plus que beaucoup de gens."

    pause 0.2

    noam vide "Donc… on commande comment ?"

    goumi vide "Formule courte : vous demandez."
    goumi vide "Formule longue : vous formulez une requête."
    goumi vide "Je la valide."
    goumi vide "Puis je vous cuisine ça bien et rapidement."

    noam vide "En même temps…"
    noam vide "si on nous a mis un robot chef, c'est pas pour qu'il improvise."

    elen vide "Ouais."
    elen vide "Mais j'aurais aimé qu'il improvise un peu de liberté avec."

    pause 0.3

    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elen", "surpris", 0.50),
        ("goumi", "vide", 0.78),
    ])
    noam reflexion "Elen, c'est ça ?"

    elen surpris "Ouais."
    elen neutre "Toi t'es Noam."
    elen neutre "Je reconnais ta tête."
    elen neutre "Et ton air de mec qui se demande encore si tout ça n'est pas un prank."

    noam panne "Je…"
    noam panne "J'ai vraiment cet air-là ?"

    elen taquin "Un peu, ouais."

    goumi vide "Souhaitez-vous une boisson de bienvenue ?"
    goumi vide "Option : chaude."
    goumi vide "Option : froide."

    noam reflexion "Euh ... Choisis pour moi ?"

    elen desaccord "Ne demande pas."
    elen desaccord "Tu vas regretter."

    noam rire "Ok."
    noam rire "Alors euh… froide."

    goumi vide "Demande enregistrée."
    goumi vide "Préparation en cours."

    "Il ne bouge pas."
    "Et pourtant, la machine derrière lui s'allume."

    elen reflexion "Cette technologie est quand même incroyable ..."

    noam inquiet "Ouais."

    "Une seconde de silence."

    elen neutre "Bon."
    elen neutre "On fait quoi ?"
    elen neutre "On joue le jeu et on mange ?"

    noam raison "On a pas trop d'autres options."
    noam raison "Pas pour l'instant."

    goumi vide "Boisson disponible."
    goumi vide "Veuillez récupérer le gobelet."

    "Un compartiment s'ouvre."
    "Un gobelet sort, parfaitement centré."
    "Évidemment."

    think "Cette cafeteria n'est pas si mal."

    elen taquin "Allez."
    elen taquin "Prends ton truc 'froid'."
    elen taquin "Je vais continuer mon tour, sait-on jamais si on a d'autres robots intéressants."

    noam rire "Ça m'étonnerait même pas."

    pause 0.3

    think "Je devrais aller voir ailleurs aussi."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_1
    
    $ hideGroup()
    jump CAFETERIA_TP

#2m20
# Total : 40m25
