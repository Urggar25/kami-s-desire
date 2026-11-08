# -----------------------------------------------------------------------
# GYMNASE — même modèle que CANON
# - 2 persos seulement : Noam + Elias
# - Découverte : Elias s'entraîne / discussion légère
# - PNC : tapis / poids / vélo / ballon / retour
# -----------------------------------------------------------------------

default decouverte_gymnase = False



label GYMNASE_TP:
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_337
    scene bg_gymnase at adaptive_fullscreen

    if not decouverte_gymnase and day_number() == 1:
        jump decouverte_gymnase

    $ pnc_room = "pnc_gymnase"
    call screen pnc_gymnase()

    if free_time_active:
        return
    if exploration_libre_active:
        return


# -----------------------------------------------------------------------
# Label d'exploration
# -----------------------------------------------------------------------

screen pnc_gymnase():

    modal True
    zorder 200

    add Solid("#000")
    use room_scene_background("gymnase")
    use room_scene_interactions("gymnase")

    if social_free_time_active() and character_has_available_free_time("ryn"):
        imagebutton:
            idle Transform(character_image("ryn", "determine"), zoom=1.00)
            hover Transform(character_image("ryn", "neutre"), zoom=1.00)
            focus_mask True
            xalign 0.20
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "ryn"), Jump("FREE_TIME_CHARACTER_INTERACT")]
    if social_free_time_active() and character_has_available_free_time("elias"):
        imagebutton:
            idle Transform(character_image("elias", "neutre"), zoom=1.00)
            hover Transform(character_image("elias", "reflechit"), zoom=1.00)
            focus_mask True
            xalign 0.90
            yalign 1.00
            action [SetVariable("last_room_label", "GYMNASE_TP"), SetVariable("free_time_selected_character", "elias"), Jump("FREE_TIME_CHARACTER_INTERACT")]


label gymnase1_douche:
    "Les douches sont impeccables. Trop impeccables."
    "Je lève les yeux et repère plusieurs caméras orientées vers les cabines."
    "Aucun angle mort. Et aucun brouilleur pour couper la surveillance."
    think "Qui irait se doucher là-dedans, à la vue de tous ?!"
    jump GYMNASE_TP


label gymnase1_porte_couloir_infirmerie:
    $ corridor_current = "infirmerie"
    jump EXIT_ROOM_TO_CORRIDOR


label gymnase1_terrain:
    "Les lignes du terrain sont nettes, comme si personne ne les avait encore franchies."
    "Il y a assez de place pour courir, jouer ou simplement oublier les murs pendant quelques minutes."
    think "Même la détente ressemble à une zone soigneusement délimitée."
    jump GYMNASE_TP


label gymnase2_banc:
    jump GYM_BANC_INTERACT

label GYM_BANC_INTERACT:
    if not social_free_time_active():
        jump GYM_PNC_POIDS

    $ events_left = sport_events_left_count()

    if events_left > 0:
        menu:
            "Faire une session de sport ? ([events_left] évènement(s) sport restant(s))"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP
    else:
        menu:
            "Faire une session de sport ? (Tous les évènements sport ont été découverts)"
            "Oui":
                jump GYM_SPORT_MINIGAME
            "Non":
                "Tu préfères garder ton énergie pour plus tard."
                jump GYMNASE_TP


label GYM_SPORT_MINIGAME:
    "Tu t'installes sur le banc et tu commences l'entraînement."

    call minijeu_halteres from _call_minijeu_halteres_free_time

    if mg_was_success:
        $ sport_event_label = pop_random_sport_event()
        if sport_event_label:
            call expression sport_event_label from _call_expression_sport_event
        else:
            "Tu termines ta séance, satisfait de tes progrès."
    else:
        "La série te casse le rythme, mais tu sauras mieux gérer la prochaine fois."

    if social_free_time_active():
        jump FREE_TIME_END

    jump GYMNASE_TP

label GYM_PNC_TAPIS:
    "Le tapis est encore tiède."
    "Quelqu'un a couru récemment."
    "Les réglages sont simples."
    "Vitesse. Inclinaison. Temps."
    think "Même ici, tout est calibré."
    jump GYMNASE_TP


label GYM_PNC_POIDS:
    "Des poids libres."
    "Des barres."
    "Des repères au sol comme dans une salle publique."
    "Mais tout est trop propre."
    "Trop rangé."
    think "On dirait un décor de pub."
    jump GYMNASE_TP


# Optionnel : si tu ajoutes un bouton retour graphique
label GYM_PNC_EXIT:
    return


# -----------------------------------------------------------------------
# Label d'histoire
# -----------------------------------------------------------------------

label decouverte_gymnase:
    $ decouverte_gymnase = True
    scene black
    play music "music/bgm_soft_neon_morning.mp3" fadein 1.0
    think "Un gymnase dans une station qui nous retient un mois. Au moins, on ne pourra pas dire qu'ils nous obligent à rester assis toute la journée."
    call MAYBE_PLAY_SCRIPTED_DOOR("gymnase", "bg_gymnase") from _call_MAYBE_PLAY_SCRIPTED_DOOR_338
    scene bg_gymnase at adaptive_fullscreen with fade
    "Il y a des tapis, des poids et plusieurs machines de cardio. L'une d'elles émet un bruit irrégulier, suivi d'un juron."
    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elias", "neutre", 0.78),
    ])
    "Un garçon essaie de régler un tapis de course. Il tapote l'écran, qui refuse visiblement de coopérer."
    elias colere "Mais avance, bordel ! Je te demande juste de ralentir."
    noam taquin "Tu veux un coup de main ?"
    elias surpris "Hein ? Ouais, attends... Non, bouge pas, j'ai presque trouvé."
    "Le tapis accélère brutalement. Il saute de côté et se rattrape à la barre avant de couper l'alimentation."
    elias panique "Putain ! C'était pas le bon bouton."
    noam rire "Tu peux dire que tu as testé la sécurité. Elle marche, visiblement."
    elias fatigue "Ouais. La sécurité est très bonne. La machine, elle, me casse les couilles."
    noam sourire "Moi c'est Noam."
    elias neutre "Elias. Je viens de la Forge, à Axiome."
    $ unlock_character_name("elias")
    noam reflexion "Tu fais souvent du sport ?"
    elias neutre "Quand j'ai le temps. Après une journée à bosser, ça aide à dormir. Et ici, franchement, j'ai besoin de me vider la tête."
    noam sourire "Je comprends. Je sais même pas encore ce qu'on va faire de nos journées."
    elias fatigue "On a les votes, les repas et un paquet de temps à tuer. Moi, si je reste assis à réfléchir à tout ça, je vais devenir dingue."
    noam taquin "Tu comptes donc te tuer sur un tapis de course à la place ?"
    elias rire "Très drôle. T'as qu'à essayer, tu feras moins le malin."
    "Il remet le tapis à sa vitesse minimale et me fait signe de monter. Je pose un pied dessus, puis l'autre."
    noam hesitation "Là, tu es sûr du réglage ?"
    elias content "Ouais, cette fois c'est bon. Regarde, il y a juste à marcher."
    "Le tapis avance à une allure tranquille. J'accélère un peu et Elias me surveille, prêt à intervenir."
    noam sourire "Finalement, c'est pas si compliqué."
    elias taquin "C'est ce que je disais avant de toucher au mauvais bouton. Fais gaffe à tes grandes phrases."
    noam rire "D'accord, j'ai rien dit."
    "Après quelques pas, je descends et lui rends sa place."
    noam reflexion "Tu crois vraiment qu'on aura le temps de venir s'entraîner avec tout ce qui nous attend ?"
    elias neutre "Je sais pas. Mais si on passe un mois à se bouffer les nerfs, on tiendra pas longtemps. Alors autant garder nos habitudes."
    noam sourire "Pas faux. Je repasserai peut-être."
    elias joie "Quand tu veux. Mais la prochaine fois, c'est toi qui règles la machine."
    noam taquin "Ah non. J'ai vu comment ça finit quand on fait confiance à un expert."
    elias rire "Va te faire voir !"
    "Il éclate de rire avant de relancer son entraînement, cette fois sans toucher à l'écran."
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_3
    $ hideGroup()
    jump GYMNASE_TP
