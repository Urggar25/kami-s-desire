# -----------------------------------------------------------------------
# CAFÉTÉRIA — même modèle que OBSERVATION / CANON
# - Persos : Noam + Elen
# - Rencontre : Goumi (robot cuisinier) — pas de sprite, mais il parle
# - PNC : frigo-machine / tables / goumi / retour
# -----------------------------------------------------------------------

default decouverte_cafeteria = False



label CAFETERIA_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_327
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

    if current_scene_active == "_2_ROUTE_OBSERVATION" and not day2_observation_route_elen_seen:
        imagebutton:
            idle Transform(character_image("elen", "content"), zoom=1.00)
            hover Transform(character_image("elen", "joie"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action Jump("_2_APRES_MIDI_ELEN")

    if social_free_time_active() and character_has_available_free_time("mara"):
        imagebutton:
            idle Transform(character_image("mara", "sourire"), zoom=1.00)
            hover Transform(character_image("mara", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.15
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "mara"), Jump("FREE_TIME_CHARACTER_INTERACT")]


    if social_free_time_active() and character_has_available_free_time("lysa"):
        imagebutton:
            idle Transform(character_image("lysa", "sourire"), zoom=1.00)
            hover Transform(character_image("lysa", "taquin"), zoom=1.00)
            focus_mask True
            xalign 0.82
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "lysa"), Jump("FREE_TIME_CHARACTER_INTERACT")]

    if social_free_time_active() and character_has_available_free_time("elen"):
        imagebutton:
            idle Transform(character_image("elen", "joie"), zoom=1.00)
            hover Transform(character_image("elen", "content"), zoom=1.00)
            focus_mask True
            xalign 0.50
            yalign 1.00
            action [SetVariable("last_room_label", "CAFETERIA_TP"), SetVariable("free_time_selected_character", "elen"), Jump("FREE_TIME_CHARACTER_INTERACT")]

    if j10011_waiting_elias:
        imagebutton:
            idle Transform(character_image("elias", "fatigue"), zoom=1.00)
            hover Transform(character_image("elias", "inquiet"), zoom=1.00)
            focus_mask True
            xalign 0.58
            yalign 1.00
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

    if day_number() == 6 and social_free_time_active() and not j601_border_news_seen:
        call _6_0_1_TV_FRONTIERES from _call_j601_tv_frontieres_cafeteria
        jump CAFETERIA_TP

    if day_number() == 4:
        call day4_optional_news from _call_day4_optional_news_cafeteria
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
    think "La cafétéria devrait être facile à trouver. Il suffit de suivre les voix et l'odeur de quelque chose qui ressemble à un vrai repas."
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_328
    scene bg_cafeteria at adaptive_fullscreen with fade
    "Il y a des tables, un comptoir et une cuisine derrière une large ouverture. Une fille discute avec un petit robot qui semble incapable de lui donner la réponse qu'elle attend."
    scene bg_cg008 at adaptive_fullscreen with fade
    $ unlock_gallery_image("bg_cg008")
    elen vide "Non mais tu comprends pas ! Je te demande un plat que tu aimes bien cuisiner, toi."
    goumi vide "Je n'éprouve aucune préférence culinaire. Veuillez préciser votre commande."
    elen vide "C'est pas une commande, c'est une question ! Tu pourrais au moins faire semblant."
    goumi vide "Simulation d'une préférence : possible. Souhaitez-vous une simulation ?"
    elen vide "Bon, oublie. Je vais finir par me disputer avec le cuisinier avant même de manger."
    noam vide "Ça a l'air bien parti, en tout cas."
    elen vide "Ah, salut ! Dis-moi que toi, au moins, tu sais choisir un dessert sans consulter six tableaux."
    noam vide "Je crois que oui. Enfin, j'espère."
    scene bg_cg008_1 at adaptive_fullscreen with fade
    goumi vide "Bonjour. Je suis Goumi, unité culinaire autonome. Je peux préparer des repas à partir des réserves disponibles."
    $ unlock_character_name("goumi")
    noam vide "Enchanté, Goumi. Et on commande comment ?"
    goumi vide "En formulant votre demande à voix haute."
    elen vide "Attention, si tu lui demandes de choisir pour toi, il va te réciter toutes les options."
    noam vide "Dans ce cas, un jus de fruit, s'il te plaît. N'importe lequel."
    goumi vide "Veuillez préciser le fruit."
    noam vide "Euh... une pomme ?"
    goumi vide "Commande acceptée. Jus de pomme en préparation."
    elen vide "Tu vois ? Il fallait juste parler comme à une machine. C'est triste, quand même."
    noam vide "C'est peut-être mieux que d'avoir un chef susceptible."
    elen vide "Oh, ça, je demande à voir !"
    call MAYBE_PLAY_SCRIPTED_DOOR("cafeteria", "bg_cafeteria") from _call_MAYBE_PLAY_SCRIPTED_DOOR_329
    scene bg_cafeteria at adaptive_fullscreen with fade
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elen", "neutre", 0.50),
        ("goumi", "vide", 0.78),
    ])
    elen sourire "Au fait, moi c'est Elen. On s'est vus tout à l'heure, mais j'ai même pas pris le temps de te parler."
    $ unlock_character_name("elen")
    noam sourire "Noam. Ça me rassure qu'il y ait au moins quelqu'un de bonne humeur ici."
    elen content "Oh, je fais ce que je peux. Si on doit rester ensemble un mois, autant commencer par manger correctement, non ?"
    goumi vide "Précision : les repas sont servis de 6 h à 14 h et de 17 h à 22 h. Le reste du temps est réservé à ma recharge."
    noam surpris "Même le cuisinier a des horaires de travail ?"
    elen rire "Et il y tient ! J'ai essayé de négocier un goûter à seize heures, c'est non."
    goumi vide "Une collation peut être préparée à l'avance."
    elen surpris "Attends, tu pouvais me dire ça depuis le début !"
    "Un petit compartiment s'ouvre sur le comptoir. Goumi y dépose un gobelet."
    goumi vide "Jus de pomme disponible."
    noam sourire "Merci. Au moins, lui, il fait ce qu'on lui demande."
    elen taquin "Ouais, sauf si tu lui demandes de te raconter sa journée."
    noam rire "Je vais éviter de le vexer."
    elen sourire "Je vais continuer à regarder ce qu'il y a ici. On se retrouvera sûrement au prochain repas."
    noam sourire "Avec plaisir. Essaie quand même de laisser Goumi tranquille."
    elen rire "Je promets rien !"
    "Elle repart vers les tables en examinant les menus. Goumi, lui, attend déjà sa prochaine commande."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_1
    $ hideGroup()
    jump CAFETERIA_TP
