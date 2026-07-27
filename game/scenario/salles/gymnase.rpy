# -----------------------------------------------------------------------
# GYMNASE — même modèle que CANON
# - 2 persos seulement : Noam + Elias
# - Découverte : Elias s'entraîne / discussion légère
# - PNC : tapis / poids / vélo / ballon / retour
# -----------------------------------------------------------------------

default decouverte_gymnase = False



label GYMNASE_TP:
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

    if social_free_time_active() and ryn_link in [0, 1, 2, 3, 4]:
        imagebutton:
            idle Transform(character_image("ryn", "determine"), zoom=0.75)
            hover Transform(character_image("ryn", "neutre"), zoom=0.75)
            focus_mask True
            xalign 0.20
            yalign 0.75
            action [SetVariable("last_room_label", "GYMNASE_TP"), Jump("RYN_LINK_INTERACT")]
    if social_free_time_active() and elias_link in [0, 2, 4]:
        imagebutton:
            idle Transform(character_image("elias", "neutre"), zoom=0.75)
            hover Transform(character_image("elias", "reflechit"), zoom=0.75)
            focus_mask True
            xalign 0.90
            yalign 0.90
            action [SetVariable("last_room_label", "GYMNASE_TP"), Jump("ELIAS_LINK_INTERACT")]


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

    think "Il y a aussi un gymnase."
    think "Ils ont vraiment pensé à mettre de nombreuses salles différentes."

    pause 0.4

    scene bg_gymnase at adaptive_fullscreen with fade

    "Ça sent le caoutchouc."
    "Le produit de nettoyage aussi."
    "Comme partout dans les couloirs mais plus particulièrement là."

    "Un terrain est marqué sur le sol."
    "Il y a des tapis de courses, des machines et des poids parfaitement rangés."

    "Et au fond…"
    "Un type est en train de s'entraîner."

    $ showGroup([
        ("noam", "reflexion", 0.22),
        ("elias", "fatigue", 0.78),
    ])

    "Il fait une série."
    "Sans musique."
    "Sans parler."
    "Juste le bruit de sa respiration."
    "Et du métal."

    noam hesitation "…"
    noam hesitation "Salut."

    "Il termine sa lancée."
    "Repose la barre doucement."
    "Puis enfin, il me regarde."

    elias neutre "Salut."

    noam sourire "Je pensais être seul."
    noam sourire "Visiblement non."

    elias fatigue "J’aime le sport."
    elias fatigue "Ça m’empêche de trop cogiter sur ce qui peut merder."

    noam taquin "Ouais... J'imagine que c'est devenu une habitude depuis un an."

    "Il rit de façon courte."

    elias neutre "Pas à cause d’elle."
    elias neutre "Avant, une balle ou une guerre, et c’était fini sans sommation."
    elias neutre "Là au moins, on sait à quoi s’attendre."
    elias raison "Faut juste respecter les règles quoi."

    "Il marque une pause un instant."
    
    elias jaloux "Est-ce qu'on vit moins bien qu'avant ?"
    elias jaloux "Perso, j'ai pas la réponse."
    elias jaloux "Alors je fais le taf. Le reste, c'est que du bruit dont je ne m'occupe pas vraiment."

    pause 0.2
    "Je ne sais pas vraiment quoi répondre."
    "D'un côté, il touche juste. Le monde est plus paisible qu'autrefois."
    "Mais d'un autre, la moindre erreur entraine la mort."
    "Pas une simple punition."
    "La mort quoi."

    noam reflexion "Au fait, je m'appelle Noam."
    noam reflexion "Je viens du district HARMONIE."

    "Il hoche la tête, comme si ça validait une info dans sa tête."

    elias neutre "Elias."
    elias neutre "AXIOME. Quartier bas."

    noam surpris "AXIOME…"
    noam surpris "La Forge."

    elias content "Ouais."
    elias content "C’est là qu’on fabrique presque tout ce que les autres utilisent."

    "Il dit ça sans fierté particulière."
    "Mais il sait dans son timbre de voix que AXIOME est nécessaire à tout le monde."
    "D'un autre côté, chacun des districts est nécessaire aux autres."
    "C'est pour ça qu'ils ont été découpé ainsi. Pour empêcher les tensions et nous rendre tous dépendants des autres."

    noam reflexion "Tu t'entraînes pour quoi ?"

    elias rire "Pour dormir mieux."
    elias rire "Une petite session avant 18h, ça serait pas de refus."
    elias rire "J’espère qu’il y a des douches après."

    noam rire "Ah."
    noam rire "La meilleure raison."

    pause 0.3

    "Je m'approche du terrain."
    "Je regarde les repères au sol."
    "Ça me rappelle l'école."
    "Ça me rappelle avant."

    "Ça me rappelle qi'avant on était innocent et les problèmes nous passaient au dessus de la tête."

    elias ecoute "Tu fais du sport, toi ?"

    noam hesitation "Avant, oui j'en faisais parfois."
    noam hesitation "Mais ça fait un moment que j'en ai pas fait …"
    noam hesitation "Je sais plus trop ce que je fais, honnêtement."

    elias fatigue "C’est pour ça que je continue."
    elias fatigue "Quand tout part en vrille, faut garder un repère."
    elias neutre "C’est le principe."

    pause 0.2

    noam taquin "Donc si je veux survivre ici…"
    noam taquin "Je dois courir et soulever des trucs."

    elias content "Et bois de l’eau."
    elias content "Respire."
    elias content "Sinon t’auras des crampes, et bon courage."

    noam sourire "Merci docteur."

    "Il souffle du nez."
    "Ça ressemble presque à un vrai rire."

    pause 0.3

    elias ecoute "Tu sais ce qui est drôle ?"
    elias ecoute "Ils nous filent un gymnase."
    elias ecoute "Comme si on était en colonie."
    elias ecoute "On soit, c'est pas pour me déplaire. J'ai toujours voulu aller en colo."

    noam reflexion "Ouais. Notre animateur est juste un peu plus cinglé que les autres."

    elias neutre "Exactement."

    "Il regarde la machine de muscu."
    "Puis les lignes au sol."
    "Puis moi."

    elias inquiet "Ces 30 jours, ça va pas être une partie de plaisir."
    elias inquiet "On va être sur le qui-vive tout le temps, pas seulement aux votes."
    elias inquiet "Fatigue, nerfs à vif… ça va peser."

    noam inquiet "Tu crois que le sport change quelque chose ?"

    elias neutre "Non. Pas forcément."
    elias neutre "Mais ça permet au moins de se vider la tête."

    pause 0.3

    "Je regarde le tapis puis les poids."

    think "Ils ne me font pas spécialement envie."
    think "Rien que l'idée d'avoir des courbatures me freine déjà."

    noam hesitation "Bon, allez fais moi une démo, Sensei !"
    noam hesitation "Histoire de faire semblant d'être normal dans ce monde chelou."

    elias content "Ok."
    elias content "Mais écoute bien."
    elias content "Sinon tu vas te péter quelque chose."

    noam sourire "Promis."

    pause 0.4

    "Pendant quelques minutes…"
    "Il me montre les postures à adopter, le rythme de respiration à avoir."

    "C'est bête."
    "C'est simple."
    "Et mine de rien, ça fait quand même du bien."

    pause 1.0
    
    "Après une longue série d'exercices."

    think "Je devrais aller voir ailleurs."
    
    call CHECK_ALL_SALLES_VISITEES from _call_CHECK_ALL_SALLES_VISITEES_3

    $ hideGroup()
    jump GYMNASE_TP

# Durée : 2m30
# Total : 49m15
