# -----------------------------------------------------------------------
# CAFÉTÉRIA — même modèle que OBSERVATION / CANON
# - Persos : Noam + Elen
# - Rencontre : Goumi (robot cuisinier) — pas de sprite, mais il parle
# - PNC : frigo-machine / tables / goumi / retour
# -----------------------------------------------------------------------

default decouverte_cafeteria = False


label CAFETERIA_TP:
    scene bg_cafeteria at adaptive_fullscreen

    if not decouverte_cafeteria:
        jump decouverte_cafeteria

    $ pnc_room = "pnc_cafeteria"
    call screen pnc_cafeteria()


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_cafeteria():

    modal True
    zorder 200

    # Cache définitivement l'ancienne scene
    add Solid("#000")

    # BG COVER — c'est LUI qui définit le scaling réel
    add "images/background/bg_cafeteria.png" at cover_screen

    # Option : quitter au clic droit / ESC (retour au label appelant)
    key "game_menu" action Return()
    key "K_ESCAPE" action Return()

    # HOTSPOTS — doivent subir EXACTEMENT le même transform
    imagebutton:
        idle "images/background/interact/cafeteria/goumi.png"
        hover "images/background/interact/cafeteria/goumi_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CAF_PNC_GOUMI")

    imagebutton:
        idle "images/background/interact/cafeteria/frigo.png"
        hover "images/background/interact/cafeteria/frigo_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CAF_PNC_FRIGO")

    imagebutton:
        idle "images/background/interact/cafeteria/table.png"
        hover "images/background/interact/cafeteria/table_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("CAF_PNC_TABLES")

    imagebutton:
        idle "images/background/interact/retour.png"
        hover "images/background/interact/retour_hover.png"
        focus_mask True
        xpos 0
        ypos 0
        at cover_screen
        action Jump("OPEN_CONCLAVE_MAP")


label CAF_PNC_GOUMI:

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


label CAF_PNC_FRIGO:

    window auto

    "La machine au fond ressemble à un frigo."
    "Sauf qu'elle fait la taille d'une armoire industrielle."

    "Écran tactile."
    "Tiroirs verrouillés."
    "Et une liste de catégories et d'aliments qui défile."

    think "Au moins ça n'a pas l'air d'être très compliqué."
    jump CAFETERIA_TP


label CAF_PNC_TABLES:

    window auto

    "Des tables."
    "Des chaises."
    "Un espace pensé pour faire comme si on vivait ici."

    think "Ça pourrait presque marcher."
    jump CAFETERIA_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label CAF_PNC_EXIT:
    return


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

    $ showP("elen", "vide", 0.1)
    $ showP("goumi", "vide", 0.9)

    elen "Non mais attends."
    elen "Tu me dis que tu peux genre VRAI-MENT cuisiner 'n'importe quoi'."
    elen "Et tu me sors un menu en quatre catégories."

    goumi "Correction : en six catégories."
    goumi "Mise en bouche, Entrée froide, entrée chaude, plat, fromage et enfin dessert."
    goumi "Vous pouvez commander ce que vous voulez. Tant que je suis approvisionné, je peux tout faire."

    "Je m'arrête à l'entrée."
    "Je ne sais pas si j'interromps une scène de présentation…"
    "Ou une petite scène de ménage."
    
    scene bg_cg008_1 at adaptive_fullscreen with fade

    $ showP("noam", "vide", 0.6)
    
    noam "Je dérange ?"

    elen "Oh."
    elen "Non. Viens."
    elen "J'essayais juste de comprendre comment on allait être nourris…"

    goumi "Alimentation : active."
    goumi "Stock : remplis."
    goumi "Gestion : optimale."

    elen "Raah j'aime pas ce mode de discussion ! On dirait vraiment un robot limité."
    elen "C'est pas très naturel."

    "Je souffle un petit rire."
    "Tu t'attendais à quoi en même temps."

    elen "Je te présente Goumi."
    elen "Apparemment c'est le chef de cette cafét."
    elen "Il peut cuisiner à peu près tout ce qu'on veut, tant que c'est dans ses heures de boulot."
    
    noam "Dans ses heures de boulot ? Mais c'est un robot ..."

    goumi "Je suis Goumi."
    goumi "Unité culinaire autonome."
    goumi "Je peux préparer toute recette demandée par un représentant."
    goumi "Dans la limite des stock disponible."
    goumi "Je travaille de 6h du matin à 14h puis de 17h à 22h."
    goumi "Le reste du temps est destiné à ma recharge."

    elen "Il a au moins le mérite d'être honnête."
    elen "C'est déjà plus que beaucoup de gens."

    pause 0.2

    noam "Donc… on commande comment ?"

    goumi "Formule courte : vous demandez."
    goumi "Formule longue : vous formulez une requête."
    goumi "Je la valide."
    goumi "Puis je vous cuisine ça bien et rapidement."

    noam "En même temps…"
    noam "si on nous a mis un robot chef, c'est pas pour qu'il improvise."

    elen "Ouais."
    elen "Mais j'aurais aimé qu'il improvise un peu de liberté avec."

    pause 0.3
    
    scene bg_cafeteria at adaptive_fullscreen with fade

    $ showP("noam", "reflexion", 0.22)
    noam "Elen, c'est ça ?"

    $ showP("elen", "surpris", 0.78)
    elen "Ouais."
    $ showP("elen", "neutre", 0.78)
    elen "Toi t'es Noam."
    elen "Je reconnais ta tête."
    elen "Et ton air de mec qui se demande encore si tout ça n'est pas un prank."

    $ showP("noam", "panne", 0.22)
    noam "Je…"
    noam "J'ai vraiment cet air-là ?"

    $ showP("elen", "taquin", 0.78)
    elen "Un peu, ouais."

    goumi "Souhaitez-vous une boisson de bienvenue ?"
    goumi "Option : chaude."
    goumi "Option : froide."

    $ showP("noam", "reflexion", 0.22)
    noam "Euh ... Choisis pour moi ?"

    $ showP("elen", "desaccord", 0.78)
    elen "Ne demande pas."
    elen "Tu vas regretter."

    $ showP("noam", "rire", 0.22)
    noam "Ok."
    noam "Alors euh… froide."

    goumi "Demande enregistrée."
    goumi "Préparation en cours."

    "Il ne bouge pas."
    "Et pourtant, la machine derrière lui s'allume."

    $ showP("elen", "reflechit", 0.78)
    elen "Cette technologie est quand même incroyable ..."

    $ showP("noam", "inquiet", 0.22)
    noam "Ouais."

    "Une seconde de silence."

    $ showP("elen", "neutre", 0.78)
    elen "Bon."
    elen "On fait quoi ?"
    elen "On joue le jeu et on mange ?"

    $ showP("noam", "raison", 0.22)
    noam "On a pas trop d'autres options."
    noam "Pas pour l'instant."

    goumi "Boisson disponible."
    goumi "Veuillez récupérer le gobelet."

    "Un compartiment s'ouvre."
    "Un gobelet sort, parfaitement centré."
    "Évidemment."

    $ showP("noam", "reflexion", 0.22)
    think "Cette cafeteria n'est pas si mal."

    $ showP("elen", "taquin", 0.78)
    elen "Allez."
    elen "Prends ton truc 'froid'."
    elen "Je vais continuer mon tour, sait-on jamais si on a d'autres robots intéressants."

    $ showP("noam", "rire", 0.22)
    noam "Ça m'étonnerait même pas."

    pause 0.3

    think "Je devrais aller voir ailleurs aussi."
    
    call CHECK_ALL_SALLES_VISITEES
    
    jump CAFETERIA_TP

#2m20
# Total : 40m25